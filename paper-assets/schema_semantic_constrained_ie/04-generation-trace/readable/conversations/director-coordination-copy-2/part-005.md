# Director coordination — Part 5 of 8

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/eb/ebac95f2406b6d6dc37e.json)

## Round 106

### Tool call

_source line 1457 · 2026-05-20T20:05:33.011230+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 14 (fresh review), 2026-05-20\n\n# ============================================================\n# Round 14 Must-Fix (Full Consensus)\n# ============================================================\n\n- id: \"R13-MF3\"\n  summary: \"缺少最直接可比的 IE constrained decoding baseline（BoostCD、GCD）的量化对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: 无直接实验对比 BoostCD（should-fix）\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 raised as critical, R2 AGREE。从 R12 should-fix 升级为 must-fix。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 critical, R2 AGREE。连续 3 轮提出，仍未解决。BoostCD 是唯一将 constrained decoding 应用于 IE 的工作。\"\n  action_items:\n    - round: 14\n      action: \"添加 BoostCD 和/或 GCD 在 SciERC/DocRED 上的实验对比，或提供详细不可比论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-MF1\"\n  summary: \"Grammar-first fallback 触发率 36.6%（zero-shot SciERC），核心 type enforcement 声称被削弱；fine-tuned fallback 率未报告\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W2 critical, R2 AGREE with nuance (prefers major)。Table 7 显示 36.64% type-bearing positions 触发 fallback。Fine-tuned fallback 率为关键缺失数据。\"\n  action_items:\n    - round: 14\n      action: \"§4 正文讨论 fallback 频率及 guarantee 边界；报告 fine-tuned fallback 率；分析 fallback root causes\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 14 Should-Fix (Full Consensus)\n# ============================================================\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents fine-tuning 仅 20 文档测试集，EE 扩展措辞过度\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF4: WikiEvents fine-tuning 仅 20 文档测试集\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Contribution 3 仍声称 'systematic evaluation'。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W3 major, R2 AGREE。20 docs / 56 event types 无法支撑可靠评估。需报告置信区间。\"\n  action_items:\n    - round: 14\n      action: \"报告 WikiEvents 完整置信区间和 per-document variance；将 EE 定位为 preliminary demonstration\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF5\"\n  summary: \"kappa-bar 的 predictive value 基于仅 2 个数据点，统计功效极低\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF2: kappa-bar 过度声称\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3 must-fix, R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W5 major, R2 AGREE。Appendix D Spearman rho=-0.77 with n=6 无统计意义。\"\n  action_items:\n    - round: 14\n      action: \"将 kappa-bar 明确定位为仅描述性指标；移除 Appendix D 推断统计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF3\"\n  summary: \"DocRED beam search 零样本仅 50-doc 子集，代表性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF8: DocRED beam search 仅 50 文档子集\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4, R2 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W6 major, R2 AGREE。Beam search 是 Level 3 约束的主要策略，50/998 docs 覆盖不足。\"\n  action_items:\n    - round: 14\n      action: \"在完整 998-doc DocRED 上至少报告一个模型的 beam search 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF1\"\n  summary: \"'any autoregressive LM' / 'any IE ontology' 泛化性声称超出验证范围\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF3: 模型规模声称过宽\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4, R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W2 major, R1 AGREE。仅 3 个英语数据集、7-8B 模型。无生物医学/工业级/大规模本体评估。\"\n  action_items:\n    - round: 14\n      action: \"Abstract/Section 1 限定为 'autoregressive LMs with logits access; validated on 7-70B' 和 'tested ontologies'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF1\"\n  summary: \"新颖性适中——架构本质是已有技术的 principled composition 而非组件创新\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 major, R1 AGREE with nuance。Proposition 1 和 enabling dependency 有超越简单组合的贡献，但整体 novelty 在 composition + formalization 层面。\"\n  action_items: []\n  resolution: \"论文定位已基本清晰。此为 reviewer 判断，非可修复 issue。\"\n  resolution_round: 14\n\n# ============================================================\n# Round 14 Minor\n# ============================================================\n\n- id: \"R13-SF6\"\n  summary: \"Pumping lemma 证明使用位置索引模型，transfer argument 不够 formal\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"presentation gap not correctness gap\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 major, R2 REBUT（Appendix O 已讨论）。降为 minor。有限实体集+canonical IDs 下约束退化为 regular language——应讨论适用边界。\"\n  action_items:\n    - round: 14\n      action: \"更明确讨论 Proposition 1 适用边界（有限实体集退化、canonical IDs）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M1\"\n  summary: \"Related Work（Section 6）压缩过度，仅 0.6 页，关键定位被推至 Appendix B\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W4 minor, R1 AGREE（8 页限制下可理解但削弱正文叙事）。\"\n  action_items:\n    - round: 14\n      action: \"将 preventive vs corrective 等关键区分留在正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M2\"\n  summary: \"70B 评估过于 preliminary（仅 INT4 量化，无 LoRA/beam/消融）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W7 minor, R2 AGREE。\"\n  action_items:\n    - round: 14\n      action: \"充实 70B 评估或精简以节省空间给 baseline 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M3\"\n  summary: \"S1 模式下 entity-before-relation ordering 保持率未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W8 minor, R2 AGREE。\"\n  action_items:\n    - round: 14\n      action: \"报告 S1 下实体-关系生成顺序保持率\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M2\"\n  summary: \"Orphan bib entries + unverified citations\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"10 orphan entries + 1 duplicate key\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"orphan 从 10 减至 1。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W6 minor, R1 AGREE。chen2024agentre/fan2024fsn orphan；formattax2026/regino2025kgcurator 无法验证。\"\n  action_items:\n    - round: 14\n      action: \"清理 orphan entries；确认 formattax2026 和 regino2025kgcurator\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-REF1\"\n  summary: \"TANL (Paolini et al., 2021, ICLR) 未引用——生成式结构化预测基础工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 AGREE。TANL 建立了 augmented language modeling for structured prediction 范式。\"\n  action_items:\n    - round: 14\n      action: \"Section 6 添加 TANL 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M6\"\n  summary: \"Table 25 红绿色标注违规/修正，色盲不友好\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Visual Check 发现。\"\n    - round: 14\n      reviewers: []\n      note: \"R14 Visual Check 仍发现相同问题。\"\n  action_items:\n    - round: 13\n      action: \"补充删除线+加粗非颜色视觉线索\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 14 Divergence (tracking only)\n# ============================================================\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧：R1=critical vs R2=major\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 认为 fine-tuning 后应降低。Director 取 critical（论文未提供 fine-tuned fallback 数据）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-DIV2\"\n  summary: \"F1 实际影响分歧：R1 REBUT R2-W3\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 认为 violation elimination 本身即 KG 场景价值。Director 判定 R1 论点更有说服力，不列入 weakness。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-DIV3\"\n  summary: \"Excitement 分歧：R1=3.5 vs R2=3.0\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 看重 decidability taxonomy 概念迁移价值；R2 侧重组件级 novelty。合理差异。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R13 issues NOT raised in R14 (possibly resolved)\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Section 7 溢出至 p9 约 11 行。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。R1-S6 确认'正文 8 页内完成'，可能已修复。待 Research Director 确认。\"\n  action_items:\n    - round: 13\n      action: \"压缩确保正文在第 8 页底部结束\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Introduction 中被系统性低估\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Abstract 'modest CF costs' 有误导性。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Abstract 现为具体 CF 范围（0-9.9% ZS / <=1.2% FT），可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 替换为具体 CF 范围\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF2\"\n  summary: \"DocRED 零样本 DR 降幅仅 45% 的深层原因讨论不充分\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"GENERIC<->X 歧义占 63.3% CF violations。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 5.2 现已讨论 kappa-bar 和 GENERIC<->X。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 5.2 增加分析\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"'formally compiles' 措辞对 semantic layer 过度\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W7, full consensus。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Abstract 现使用分层措辞（compiles + interprets at runtime）。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"全文分层措辞\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF5\"\n  summary: \"缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"引用 GoLLIE published numbers 即可。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 5.1 现有 F1 参考数字。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 5 加 GoLLIE F1 reference\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M1\"\n  summary: \"S1/S2 命名不直观\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及，可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"首次出现加括号描述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M5\"\n  summary: \"'Best-effort pair-based enforcement' 首次出现时需完整定义\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及，可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"首次出现时加括号定义\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-REF1\"\n  summary: \"GenIE (Josifoski 2022) 应入 Section 6 主体\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 6 现已引用 GenIE。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 6 增加 GenIE 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-REF3\"\n  summary: \"LasUIE (Fei 2022) 未引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 6 现已引用 LasUIE。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 6 添加引用\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved (carried forward for tracking)\n# ============================================================\n\n- id: \"R13-M4\"\n  summary: \"Section 4 脚注（对称 relation 的 kappa 计算）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"kappa-bar 降级后脚注形式合理\"\n  resolution_round: 13\n\n- id: \"R13-DIV1\"\n  summary: \"kappa-bar 严重度分歧\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"采纳激进立场，kappa-bar 移出 Contribution 列表\"\n  resolution_round: 13\n\n- id: \"R13-REB1\"\n  summary: \"G(t)=empty 边界情况\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"XGrammar PDA invariant 保证\"\n  resolution_round: 13\n\n- id: \"R12-MF1\"\n  summary: \"'Exact enforcement' -> 'best-effort' 全文替换\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已改为 'best-effort pair-based'\"\n  resolution_round: 13\n\n- id: \"R12-MF3\"\n  summary: \"Proposition 1 proof sketch 不完整\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Appendix O 已补完整 pumping lemma 证明\"\n  resolution_round: 13\n\n- id: \"R12-SF1\"\n  summary: \"语义层与 IterGen/PICARD 概念区分不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Section 6 已增加 preventive vs corrective 对比\"\n  resolution_round: 13\n\n- id: \"R12-SF6\"\n  summary: \"Entity registry 顺序依赖导致全局次优类型赋值\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Section 4 已讨论贪心赋值局限性\"\n  resolution_round: 13\n\n- id: \"R12-SF7\"\n  summary: \"'Ontology-agnostic' -> 更精确表述\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已改为 'applicable to formal ontologies and empirically-derived type constraints'\"\n  resolution_round: 13\n\n- id: \"R12-VL1\"\n  summary: \"主文前 4 页无 display item\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 已加入 Section 3\"\n  resolution_round: 13\n\n- id: \"R12-VL2\"\n  summary: \"主文零 Figure\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 已入主文\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Eq.(2) conjunction 未明确\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已加注 element-wise AND\"\n  resolution_round: 13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 14 (fresh review), 2026-05-20\n\n# ============================================================\n# Round 14 Must-Fix (Full Consensus)\n# ============================================================\n\n- id: \"R13-MF3\"\n  summary: \"缺少最直接可比的 IE constrained decoding baseline（BoostCD、GCD）的量化对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: 无直接实验对比 BoostCD（should-fix）\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 raised as critical, R2 AGREE。从 R12 should-fix 升级为 must-fix。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 critical, R2 AGREE。连续 3 轮提出，仍未解决。BoostCD 是唯一将 constrained decoding 应用于 IE 的工作。\"\n  action_items:\n    - round: 14\n      action: \"添加 BoostCD 和/或 GCD 在 SciERC/DocRED 上的实验对比，或提供详细不可比论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-MF1\"\n  summary: \"Grammar-first fallback 触发率 36.6%（zero-shot SciERC），核心 type enforcement 声称被削弱；fine-tuned fallback 率未报告\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W2 critical, R2 AGREE with nuance (prefers major)。Table 7 显示 36.64% type-bearing positions 触发 fallback。Fine-tuned fallback 率为关键缺失数据。\"\n  action_items:\n    - round: 14\n      action: \"§4 正文讨论 fallback 频率及 guarantee 边界；报告 fine-tuned fallback 率；分析 fallback root causes\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 14 Should-Fix (Full Consensus)\n# ============================================================\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents fine-tuning 仅 20 文档测试集，EE 扩展措辞过度\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF4: WikiEvents fine-tuning 仅 20 文档测试集\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Contribution 3 仍声称 'systematic evaluation'。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W3 major, R2 AGREE。20 docs / 56 event types 无法支撑可靠评估。需报告置信区间。\"\n  action_items:\n    - round: 14\n      action: \"报告 WikiEvents 完整置信区间和 per-document variance；将 EE 定位为 preliminary demonstration\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF5\"\n  summary: \"kappa-bar 的 predictive value 基于仅 2 个数据点，统计功效极低\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF2: kappa-bar 过度声称\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3 must-fix, R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W5 major, R2 AGREE。Appendix D Spearman rho=-0.77 with n=6 无统计意义。\"\n  action_items:\n    - round: 14\n      action: \"将 kappa-bar 明确定位为仅描述性指标；移除 Appendix D 推断统计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF3\"\n  summary: \"DocRED beam search 零样本仅 50-doc 子集，代表性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF8: DocRED beam search 仅 50 文档子集\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4, R2 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W6 major, R2 AGREE。Beam search 是 Level 3 约束的主要策略，50/998 docs 覆盖不足。\"\n  action_items:\n    - round: 14\n      action: \"在完整 998-doc DocRED 上至少报告一个模型的 beam search 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF1\"\n  summary: \"'any autoregressive LM' / 'any IE ontology' 泛化性声称超出验证范围\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF3: 模型规模声称过宽\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4, R1 AGREE。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W2 major, R1 AGREE。仅 3 个英语数据集、7-8B 模型。无生物医学/工业级/大规模本体评估。\"\n  action_items:\n    - round: 14\n      action: \"Abstract/Section 1 限定为 'autoregressive LMs with logits access; validated on 7-70B' 和 'tested ontologies'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF1\"\n  summary: \"新颖性适中——架构本质是已有技术的 principled composition 而非组件创新\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 major, R1 AGREE with nuance。Proposition 1 和 enabling dependency 有超越简单组合的贡献，但整体 novelty 在 composition + formalization 层面。\"\n  action_items: []\n  resolution: \"论文定位已基本清晰。此为 reviewer 判断，非可修复 issue。\"\n  resolution_round: 14\n\n# ============================================================\n# Round 14 Minor\n# ============================================================\n\n- id: \"R13-SF6\"\n  summary: \"Pumping lemma 证明使用位置索引模型，transfer argument 不够 formal\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"presentation gap not correctness gap\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W4 major, R2 REBUT（Appendix O 已讨论）。降为 minor。有限实体集+canonical IDs 下约束退化为 regular language——应讨论适用边界。\"\n  action_items:\n    - round: 14\n      action: \"更明确讨论 Proposition 1 适用边界（有限实体集退化、canonical IDs）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M1\"\n  summary: \"Related Work（Section 6）压缩过度，仅 0.6 页，关键定位被推至 Appendix B\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W4 minor, R1 AGREE（8 页限制下可理解但削弱正文叙事）。\"\n  action_items:\n    - round: 14\n      action: \"将 preventive vs corrective 等关键区分留在正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M2\"\n  summary: \"70B 评估过于 preliminary（仅 INT4 量化，无 LoRA/beam/消融）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W7 minor, R2 AGREE。\"\n  action_items:\n    - round: 14\n      action: \"充实 70B 评估或精简以节省空间给 baseline 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-M3\"\n  summary: \"S1 模式下 entity-before-relation ordering 保持率未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W8 minor, R2 AGREE。\"\n  action_items:\n    - round: 14\n      action: \"报告 S1 下实体-关系生成顺序保持率\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M2\"\n  summary: \"Orphan bib entries + unverified citations\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"10 orphan entries + 1 duplicate key\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"orphan 从 10 减至 1。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W6 minor, R1 AGREE。chen2024agentre/fan2024fsn orphan；formattax2026/regino2025kgcurator 无法验证。\"\n  action_items:\n    - round: 14\n      action: \"清理 orphan entries；确认 formattax2026 和 regino2025kgcurator\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-REF1\"\n  summary: \"TANL (Paolini et al., 2021, ICLR) 未引用——生成式结构化预测基础工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 AGREE。TANL 建立了 augmented language modeling for structured prediction 范式。\"\n  action_items:\n    - round: 14\n      action: \"Section 6 添加 TANL 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M6\"\n  summary: \"Table 25 红绿色标注违规/修正，色盲不友好\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Visual Check 发现。\"\n    - round: 14\n      reviewers: []\n      note: \"R14 Visual Check 仍发现相同问题。\"\n  action_items:\n    - round: 13\n      action: \"补充删除线+加粗非颜色视觉线索\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 14 Divergence (tracking only)\n# ============================================================\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧：R1=critical vs R2=major\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 认为 fine-tuning 后应降低。Director 取 critical（论文未提供 fine-tuned fallback 数据）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-DIV2\"\n  summary: \"F1 实际影响分歧：R1 REBUT R2-W3\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 认为 violation elimination 本身即 KG 场景价值。Director 判定 R1 论点更有说服力，不列入 weakness。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-DIV3\"\n  summary: \"Excitement 分歧：R1=3.5 vs R2=3.0\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 看重 decidability taxonomy 概念迁移价值；R2 侧重组件级 novelty。合理差异。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R13 issues NOT raised in R14 (possibly resolved)\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Section 7 溢出至 p9 约 11 行。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。R1-S6 确认'正文 8 页内完成'，可能已修复。待 Research Director 确认。\"\n  action_items:\n    - round: 13\n      action: \"压缩确保正文在第 8 页底部结束\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Introduction 中被系统性低估\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Abstract 'modest CF costs' 有误导性。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Abstract 现为具体 CF 范围（0-9.9% ZS / <=1.2% FT），可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 替换为具体 CF 范围\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF2\"\n  summary: \"DocRED 零样本 DR 降幅仅 45% 的深层原因讨论不充分\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"GENERIC<->X 歧义占 63.3% CF violations。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 5.2 现已讨论 kappa-bar 和 GENERIC<->X。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 5.2 增加分析\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"'formally compiles' 措辞对 semantic layer 过度\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W7, full consensus。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Abstract 现使用分层措辞（compiles + interprets at runtime）。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"全文分层措辞\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF5\"\n  summary: \"缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"引用 GoLLIE published numbers 即可。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 5.1 现有 F1 参考数字。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 5 加 GoLLIE F1 reference\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M1\"\n  summary: \"S1/S2 命名不直观\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及，可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"首次出现加括号描述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M5\"\n  summary: \"'Best-effort pair-based enforcement' 首次出现时需完整定义\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及，可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"首次出现时加括号定义\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-REF1\"\n  summary: \"GenIE (Josifoski 2022) 应入 Section 6 主体\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 6 现已引用 GenIE。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 6 增加 GenIE 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-REF3\"\n  summary: \"LasUIE (Fei 2022) 未引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。Section 6 现已引用 LasUIE。可能已修复。待确认。\"\n  action_items:\n    - round: 13\n      action: \"Section 6 添加引用\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved (carried forward for tracking)\n# ============================================================\n\n- id: \"R13-M4\"\n  summary: \"Section 4 脚注（对称 relation 的 kappa 计算）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"kappa-bar 降级后脚注形式合理\"\n  resolution_round: 13\n\n- id: \"R13-DIV1\"\n  summary: \"kappa-bar 严重度分歧\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"采纳激进立场，kappa-bar 移出 Contribution 列表\"\n  resolution_round: 13\n\n- id: \"R13-REB1\"\n  summary: \"G(t)=empty 边界情况\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"XGrammar PDA invariant 保证\"\n  resolution_round: 13\n\n- id: \"R12-MF1\"\n  summary: \"'Exact enforcement' -> 'best-effort' 全文替换\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已改为 'best-effort pair-based'\"\n  resolution_round: 13\n\n- id: \"R12-MF3\"\n  summary: \"Proposition 1 proof sketch 不完整\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Appendix O 已补完整 pumping lemma 证明\"\n  resolution_round: 13\n\n- id: \"R12-SF1\"\n  summary: \"语义层与 IterGen/PICARD 概念区分不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Section 6 已增加 preventive vs corrective 对比\"\n  resolution_round: 13\n\n- id: \"R12-SF6\"\n  summary: \"Entity registry 顺序依赖导致全局次优类型赋值\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Section 4 已讨论贪心赋值局限性\"\n  resolution_round: 13\n\n- id: \"R12-SF7\"\n  summary: \"'Ontology-agnostic' -> 更精确表述\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已改为 'applicable to formal ontologies and empirically-derived type constraints'\"\n  resolution_round: 13\n\n- id: \"R12-VL1\"\n  summary: \"主文前 4 页无 display item\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 已加入 Section 3\"\n  resolution_round: 13\n\n- id: \"R12-VL2\"\n  summary: \"主文零 Figure\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 已入主文\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Eq.(2) conjunction 未明确\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已加注 element-wise AND\"\n  resolution_round: 13"
  }
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-20T20:05:33.112880+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 17352}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-20T20:07:42.016125+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告：OntoCoDec\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验评估）、R2（新颖性 + 完整性 + 写作 + Related Work）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE ontology 编译为两层 token-level 解码约束：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇准入；semantic layer（prefix-decidable with state）通过动态 entity registry 实现 domain/range type 约束，含 grammar-first fallback。核心理论贡献为三级 decidability taxonomy 和 Proposition 1（证明 domain/range 约束不是 context-free 的）。在 SciERC（551 docs）、DocRED（998 docs）、WikiEvents（246 docs）上跨 3 个 7-8B 模型评估，LoRA + greedy S1 实现 DR ≤ 0.09%、R-F1 ±0.6 pp；beam (k=4) 在 SciERC 上消除全部违规（1.54× latency）。\n\n---\n\n## Strengths\n\n**S1. Decidability taxonomy 提供扎实的形式化框架。** 三级分类（context-free / prefix-decidable with state / non-local）清晰界定了不同约束类别的计算复杂度。Proposition 1 的 pumping lemma 证明正确且直接支撑两层架构的必要性。[R1, R2 共识]\n\n**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融和 DocRED 四路消融有效证明了各层的独立贡献：grammar-only 仅减 24% DR，semantic-only 无法保证词汇合规，二者组合才实现 94-100% DR reduction。层间双向依赖在此前文献中未被识别，是本文亮点。[R1, R2 共识]\n\n**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests 覆盖关键对比，p 值均有报告，展现负责任的统计实践。[R1]\n\n**S4. 跨模型一致性好。** 3 models × 3 tokenizer families 的交叉验证显示约束效果在不同 tokenizer 间一致，支持 tokenizer-agnostic 声称。[R1, R2 共识]\n\n**S5. 工程贡献实用。** 运行时开销低（+2-13%），自动从任意 IE ontology 编译约束，continuation masking tokenizer-agnostic，grammar-first fallback 保证结构完整性。[R1, R2 共识]\n\n**S6. 复现性强。** Appendix G 提供完整超参数、prompt templates、硬件配置、随机种子。[R1, R2 共识]\n\n**S7. 写作质量良好。** 结构清晰，术语一致（compile/interpret 分层），Figure 1 信息密度高。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（全部 Reviewer 共识）\n\n**MF1. [critical] 缺少最直接竞争方法的实验对比。** [R1-W1, R2 AGREE]\nBoostCD（Sakota et al., 2025）是唯一明确将 constrained decoding 应用于 IE 的同期工作，GCD（Geng et al., 2023）是 grammar-constrained decoding for structured NLP 的直接前驱。论文在 §6 引用了这些工作但实验中未做头对头对比。当前 baselines（unconstrained vs grammar-only vs full）仅为内部消融，不能证明相对于现有 constrained decoding 方法的优势。**此问题已连续 3 轮（R12-R14）提出，仍未解决。**\n\n**MF2. [critical] Grammar-first fallback 触发率 36.6%，type enforcement 核心声称被削弱。** [R1-W2 critical, R2 AGREE with nuance → major]\nSciERC 上 36.64% 的 type-bearing positions 触发 grammar-first fallback（Table 7），意味着超过 1/3 的关键位置上 semantic layer 的 type constraints 被完全放弃。论文称\"best-effort pair-based enforcement\"，但正文未充分讨论这一退化的幅度和影响。**更关键的是：fine-tuned 设置下的 fallback 率未报告**——这是验证\"fine-tuning 缓解 fallback\"论点的关键缺失数据。R2 认为可降为 major（fine-tuning 后应改善），但因论文未提供数据支持，Director 取 critical。\n\n### Should-Fix（全部 Reviewer 共识）\n\n**SF1. WikiEvents 20-doc test set 统计功效极低。** [R1-W3 major, R2 AGREE]\n20 文档 / 56 event types / 30 argument roles——平均每个 event type 不到 0.4 个测试文档。论文自称\"preliminary\"但 Contribution 列表中仍声称 EE 扩展。需报告完整置信区间和 per-document variance，或将 EE 定位为 proof-of-concept。\n\n**SF2. κ̄ 的 predictive value 基于仅 2 个数据点。** [R1-W5 major, R2 AGREE]\nκ̄ 仅在 SciERC (0.333) 和 DocRED (0.842) 上计算。Appendix D 的 Spearman ρ=-0.77 with n=6 统计功效极低。应将 κ̄ 明确定位为仅描述性指标，移除推断统计声称。\n\n**SF3. DocRED beam search 仅 50-doc 子集。** [R1-W6 major, R2 AGREE]\nBeam search 是处理 Level 3 non-local constraints 的主要策略，在 DocRED 上仅用 50/998 docs 评估代表性不足。\n\n**SF4. 泛化性声称超出验证范围。** [R2-W2 major, R1 AGREE]\n仅 3 个英语数据集、7-8B 模型（70B preliminary）。Abstract 和 §1 声称\"compiles constraints automatically from any IE ontology\"和\"applicable to any autoregressive LM\"超出验证范围。无生物医学、工业级或大规模本体评估。\n\n**SF5. 新颖性适中。** [R2-W1 major, R1 AGREE with nuance]\nGrammar layer = XGrammar 应用于 IE JSON schema；semantic layer = 带状态查找表；decidability taxonomy = 已知形式语言理论的 IE 重述。R1 认为 Proposition 1 的特定场景证明和 enabling dependency 的实验发现有超越简单组合的贡献，但整体 novelty 在 composition + formalization 层面而非组件创新。此为 reviewer 判断，非可修复 issue。\n\n### Minor\n\n**M1. Proposition 1 position-indexing 简化的 transfer argument。** [R1-W4 major → R2 REBUT → 降为 minor]\nR2 指出 Appendix O 已讨论 position vs name referencing 的 gap。但 R1-Q3 更尖锐：有限实体集 + canonical IDs 下约束退化为 regular language，Proposition 1 不成立。论文应更明确讨论适用边界。\n\n**M2. 70B 评估过于 preliminary。** [R1-W7, R2 AGREE]\n仅 INT4 量化推理，无 LoRA fine-tuning、beam search 或消融变体。\n\n**M3. Entity registry 顺序依赖未量化。** [R1-W8, R2 AGREE]\nS1 下 entity-before-relation ordering 的保持率未报告。\n\n**M4. Related Work 压缩过度。** [R2-W4, R1 AGREE]\n正文 §6 仅约 0.6 页，关键定位论述被推至 Appendix B。8 页限制下可理解但削弱正文叙事。\n\n**M5. 孤立 bib 条目。** [R2-W6, R1 AGREE]\nchen2024agentre、fan2024fsn 为 orphan entries；formattax2026、regino2025kgcurator 无法通过 OpenAlex 验证。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **缺少 baseline 是最大缺陷**：BoostCD/GCD 实验对比是影响接收决定的核心问题。\n2. **评估范围偏窄**：3 个英语数据集、7-8B 模型不足以支撑泛化声称。\n3. **WikiEvents 统计功效不足**：20-doc test set 无法支撑可靠评估。\n4. **κ̄ 仅描述性**：2 个数据点不足以建立 predictive relationship。\n5. **消融设计严谨**：enabling dependency 论证是本文亮点。\n6. **工程质量高**：运行时开销低、tokenizer-agnostic、自动编译。\n7. **写作质量良好**：结构清晰、术语一致、统计规范。\n8. **TANL 应被引用**。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Fallback 36.6% 严重度** [R1=critical, R2=major]：R2 认为 fine-tuning 后应降低。Director 取 critical（论文未提供 fine-tuned fallback 数据）。\n2. **F1 实际影响** [R1 REBUT R2-W3]：R1 认为 violation elimination 本身即 KG 构建场景的实际价值，F1 不变是\"无损执行\"的证据而非缺陷。Director 判定 R1 论点更有说服力——violation elimination 对 KG 质量的保障不需要通过 F1 提升来证明。**不列入 weakness。** 但建议论文补充下游应用场景讨论。\n3. **Excitement** [R1=3.5, R2=3.0]：R1 更看重 decidability taxonomy 的概念迁移价值；R2 侧重组件级 novelty。合理价值判断差异。\n\n---\n\n## Questions for Authors\n\nQ1. BoostCD 为何未作为 experimental baseline？如果不可直接比较，请提供详细论证和 best-effort adaptation。\nQ2. Grammar-first fallback 在 fine-tuned 设置下的触发率是多少？fallback root causes 分布（tokenizer collision vs schema ambiguity vs model preference）？\nQ3. 有限实体集 + canonical entity IDs 下，Proposition 1 是否仍成立？约束是否退化为 regular language？\nQ4. 更 aggressive 的约束策略（backtrack/resample）能否同时降低 DR 和 CF？\nQ5. \"Well-calibrated\" 能否被显式定义和量化？\nQ6. WikiEvents 20-doc test set 上各指标的 document-level variance 和置信区间？\nQ7. OntoCoDec 在显著更大规模本体上的 IE 性能如何？\n\n---\n\n## Missing References\n\n1. **TANL** (Paolini et al., 2021, ICLR): \"Structured Prediction as Translation between Augmented Natural Languages\" — 生成式结构化预测的基础性工作。[R2 raised, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，本轮未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 ~4 分钟）\n\n发现（3 warnings, 5 info）：\n- **[warning]** 前 2 页纯文本无 display item，Figure 1 直到第 3 页才出现。\n- **[warning]** 正文 8 页仅 1 个 figure + 5 个 table，视觉 table-heavy。建议增加 1 个结果可视化图。\n- **[warning]** 第 8 页整页纯文本（Related Work + Conclusion），与前面 table 密集区形成节奏断裂。\n- **[info]** Figure 1 内部分标注文字字号偏小，接近 8pt 可读下限。\n- **[info]** Table 25 使用纯红/绿色标注，色盲不友好。\n- **[info]** Appendix B 连续 5 页纯文本。\n- **[info]** 第 6-7 页各含 2 个 table，信息密度高但无冗余。\n- **[info]** Figure 4（附录）轴标签偏小，灰度打印区分度有限。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.5 | 3.0 | **3.0** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4 | 4 | **4** |\n\n### Overall: 3.5 — Borderline Conference\n\n两位 Reviewer 独立评估后完全一致：3.5 Borderline Conference。交叉回应后共识进一步加强。\n\n**核心判断**：OntoCoDec 是一篇技术上扎实、工程质量高的工作。Decidability taxonomy 和 enabling dependency 是有价值的概念贡献，消融设计严谨，跨模型验证充分。但两个关键问题阻碍接收至 Conference 水平：\n1. **缺少 BoostCD/GCD 等最直接竞争方法的实验对比**（连续 3 轮提出），无法证明相对优势；\n2. **Grammar-first fallback 36.6% 触发率**未在正文诚实讨论，且 fine-tuned fallback 率未报告，削弱了\"type-constrained\"的核心声称。\n\n评估范围（3 个英语数据集、7-8B 模型）相对泛化性声称偏窄；WikiEvents 20-doc 评估和 κ̄ 的 2 数据点进一步削弱证据说服力。新颖性在 principled composition 层面，而非组件创新。\n\n若能补充 BoostCD/GCD 对比实验、报告 fine-tuned fallback 率、并限定泛化性声称，本文有望达到 Conference 水平（4.0）。当前版本推荐 **Borderline Conference（3.5）**，有较好的 Findings 接收前景。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"applicable to any autoregressive LM\" → 限定为 \"autoregressive LMs with logits access; validated on 7-70B\"\n- \"compiles constraints automatically from any IE ontology\" → 限定为已验证的 ontology 规模\n- Contribution 列表中 EE 扩展应从 \"systematic evaluation\" 降级为 \"preliminary demonstration\"\n\n### §3 Method\n- Proposition 1 适用边界（有限实体集 + canonical IDs 退化）应更明确讨论\n- \"Best-effort pair-based enforcement\" 首次出现时给出完整 inline definition\n\n### §4 Constraint Composition\n- Grammar-first fallback 的 36.6% 触发率应在此 section 正文中讨论，而非仅在 Appendix Table 7\n- κ̄ 的 Appendix D 推断统计（Spearman ρ with n=6）应移除或限定\n- Fine-tuned 设置下的 fallback 率是关键缺失数据\n\n### §5 Experiments\n- 需添加 BoostCD 和/或 GCD 实验对比（must-fix）\n- WikiEvents fine-tuning 结论加 \"preliminary\" 限定，报告置信区间\n- DocRED beam search 应在完整 998-doc 集上至少报告一个模型的结果\n- 70B 评估可保留但应精简以节省空间给 baseline 对比\n\n### §6 Related Work\n- 添加 TANL (Paolini et al., 2021) 引用\n- 正文定位论述偏简，关键区分（preventive vs corrective, forward-only vs backtracking）应留在正文\n\n### Bibliography\n- 清理 orphan entries（chen2024agentre, fan2024fsn）\n- 确认 formattax2026 和 regino2025kgcurator 的 arXiv ID\n\n### Visual（非评分项）\n- 考虑增加 1 个结果可视化图改善正文视觉节奏\n- Table 25 补充非颜色视觉标记（色盲友好）",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 — Borderline Conference",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 14 审稿报告：OntoCoDec\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验评估）、R2（新颖性 + 完整性 + 写作 + Related Work）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE ontology 编译为两层 token-level 解码约束：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇准入；semantic layer（prefix-decidable with state）通过动态 entity registry 实现 domain/range type 约束，含 grammar-first fallback。核心理论贡献为三级 decidability taxonomy 和 Proposition 1（证明 domain/range 约束不是 context-free 的）。在 SciERC（551 docs）、DocRED（998 docs）、WikiEvents（246 docs）上跨 3 个 7-8B 模型评估，LoRA + greedy S1 实现 DR ≤ 0.09%、R-F1 ±0.6 pp；beam (k=4) 在 SciERC 上消除全部违规（1.54× latency）。\n\n---\n\n## Strengths\n\n**S1. Decidability taxonomy 提供扎实的形式化框架。** 三级分类（context-free / prefix-decidable with state / non-local）清晰界定了不同约束类别的计算复杂度。Proposition 1 的 pumping lemma 证明正确且直接支撑两层架构的必要性。[R1, R2 共识]\n\n**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融和 DocRED 四路消融有效证明了各层的独立贡献：grammar-only 仅减 24% DR，semantic-only 无法保证词汇合规，二者组合才实现 94-100% DR reduction。层间双向依赖在此前文献中未被识别，是本文亮点。[R1, R2 共识]\n\n**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests 覆盖关键对比，p 值均有报告，展现负责任的统计实践。[R1]\n\n**S4. 跨模型一致性好。** 3 models × 3 tokenizer families 的交叉验证显示约束效果在不同 tokenizer 间一致，支持 tokenizer-agnostic 声称。[R1, R2 共识]\n\n**S5. 工程贡献实用。** 运行时开销低（+2-13%），自动从任意 IE ontology 编译约束，continuation masking tokenizer-agnostic，grammar-first fallback 保证结构完整性。[R1, R2 共识]\n\n**S6. 复现性强。** Appendix G 提供完整超参数、prompt templates、硬件配置、随机种子。[R1, R2 共识]\n\n**S7. 写作质量良好。** 结构清晰，术语一致（compile/interpret 分层），Figure 1 信息密度高。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（全部 Reviewer 共识）\n\n**MF1. [critical] 缺少最直接竞争方法的实验对比。** [R1-W1, R2 AGREE]\nBoostCD（Sakota et al., 2025）是唯一明确将 constrained decoding 应用于 IE 的同期工作，GCD（Geng et al., 2023）是 grammar-constrained decoding for structured NLP 的直接前驱。论文在 §6 引用了这些工作但实验中未做头对头对比。当前 baselines（unconstrained vs grammar-only vs full）仅为内部消融，不能证明相对于现有 constrained decoding 方法的优势。**此问题已连续 3 轮（R12-R14）提出，仍未解决。**\n\n**MF2. [critical] Grammar-first fallback 触发率 36.6%，type enforcement 核心声称被削弱。** [R1-W2 critical, R2 AGREE with nuance → major]\nSciERC 上 36.64% 的 type-bearing positions 触发 grammar-first fallback（Table 7），意味着超过 1/3 的关键位置上 semantic layer 的 type constraints 被完全放弃。论文称\"best-effort pair-based enforcement\"，但正文未充分讨论这一退化的幅度和影响。**更关键的是：fine-tuned 设置下的 fallback 率未报告**——这是验证\"fine-tuning 缓解 fallback\"论点的关键缺失数据。R2 认为可降为 major（fine-tuning 后应改善），但因论文未提供数据支持，Director 取 critical。\n\n### Should-Fix（全部 Reviewer 共识）\n\n**SF1. WikiEvents 20-doc test set 统计功效极低。** [R1-W3 major, R2 AGREE]\n20 文档 / 56 event types / 30 argument roles——平均每个 event type 不到 0.4 个测试文档。论文自称\"preliminary\"但 Contribution 列表中仍声称 EE 扩展。需报告完整置信区间和 per-document variance，或将 EE 定位为 proof-of-concept。\n\n**SF2. κ̄ 的 predictive value 基于仅 2 个数据点。** [R1-W5 major, R2 AGREE]\nκ̄ 仅在 SciERC (0.333) 和 DocRED (0.842) 上计算。Appendix D 的 Spearman ρ=-0.77 with n=6 统计功效极低。应将 κ̄ 明确定位为仅描述性指标，移除推断统计声称。\n\n**SF3. DocRED beam search 仅 50-doc 子集。** [R1-W6 major, R2 AGREE]\nBeam search 是处理 Level 3 non-local constraints 的主要策略，在 DocRED 上仅用 50/998 docs 评估代表性不足。\n\n**SF4. 泛化性声称超出验证范围。** [R2-W2 major, R1 AGREE]\n仅 3 个英语数据集、7-8B 模型（70B preliminary）。Abstract 和 §1 声称\"compiles constraints automatically from any IE ontology\"和\"applicable to any autoregressive LM\"超出验证范围。无生物医学、工业级或大规模本体评估。\n\n**SF5. 新颖性适中。** [R2-W1 major, R1 AGREE with nuance]\nGrammar layer = XGrammar 应用于 IE JSON schema；semantic layer = 带状态查找表；decidability taxonomy = 已知形式语言理论的 IE 重述。R1 认为 Proposition 1 的特定场景证明和 enabling dependency 的实验发现有超越简单组合的贡献，但整体 novelty 在 composition + formalization 层面而非组件创新。此为 reviewer 判断，非可修复 issue。\n\n### Minor\n\n**M1. Proposition 1 position-indexing 简化的 transfer argument。** [R1-W4 major → R2 REBUT → 降为 minor]\nR2 指出 Appendix O 已讨论 position vs name referencing 的 gap。但 R1-Q3 更尖锐：有限实体集 + canonical IDs 下约束退化为 regular language，Proposition 1 不成立。论文应更明确讨论适用边界。\n\n**M2. 70B 评估过于 preliminary。** [R1-W7, R2 AGREE]\n仅 INT4 量化推理，无 LoRA fine-tuning、beam search 或消融变体。\n\n**M3. Entity registry 顺序依赖未量化。** [R1-W8, R2 AGREE]\nS1 下 entity-before-relation ordering 的保持率未报告。\n\n**M4. Related Work 压缩过度。** [R2-W4, R1 AGREE]\n正文 §6 仅约 0.6 页，关键定位论述被推至 Appendix B。8 页限制下可理解但削弱正文叙事。\n\n**M5. 孤立 bib 条目。** [R2-W6, R1 AGREE]\nchen2024agentre、fan2024fsn 为 orphan entries；formattax2026、regino2025kgcurator 无法通过 OpenAlex 验证。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **缺少 baseline 是最大缺陷**：BoostCD/GCD 实验对比是影响接收决定的核心问题。\n2. **评估范围偏窄**：3 个英语数据集、7-8B 模型不足以支撑泛化声称。\n3. **WikiEvents 统计功效不足**：20-doc test set 无法支撑可靠评估。\n4. **κ̄ 仅描述性**：2 个数据点不足以建立 predictive relationship。\n5. **消融设计严谨**：enabling dependency 论证是本文亮点。\n6. **工程质量高**：运行时开销低、tokenizer-agnostic、自动编译。\n7. **写作质量良好**：结构清晰、术语一致、统计规范。\n8. **TANL 应被引用**。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Fallback 36.6% 严重度** [R1=critical, R2=major]：R2 认为 fine-tuning 后应降低。Director 取 critical（论文未提供 fine-tuned fallback 数据）。\n2. **F1 实际影响** [R1 REBUT R2-W3]：R1 认为 violation elimination 本身即 KG 构建场景的实际价值，F1 不变是\"无损执行\"的证据而非缺陷。Director 判定 R1 论点更有说服力——violation elimination 对 KG 质量的保障不需要通过 F1 提升来证明。**不列入 weakness。** 但建议论文补充下游应用场景讨论。\n3. **Excitement** [R1=3.5, R2=3.0]：R1 更看重 decidability taxonomy 的概念迁移价值；R2 侧重组件级 novelty。合理价值判断差异。\n\n---\n\n## Questions for Authors\n\nQ1. BoostCD 为何未作为 experimental baseline？如果不可直接比较，请提供详细论证和 best-effort adaptation。\nQ2. Grammar-first fallback 在 fine-tuned 设置下的触发率是多少？fallback root causes 分布（tokenizer collision vs schema ambiguity vs model preference）？\nQ3. 有限实体集 + canonical entity IDs 下，Proposition 1 是否仍成立？约束是否退化为 regular language？\nQ4. 更 aggressive 的约束策略（backtrack/resample）能否同时降低 DR 和 CF？\nQ5. \"Well-calibrated\" 能否被显式定义和量化？\nQ6. WikiEvents 20-doc test set 上各指标的 document-level variance 和置信区间？\nQ7. OntoCoDec 在显著更大规模本体上的 IE 性能如何？\n\n---\n\n## Missing References\n\n1. **TANL** (Paolini et al., 2021, ICLR): \"Structured Prediction as Translation between Augmented Natural Languages\" — 生成式结构化预测的基础性工作。[R2 raised, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，本轮未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 ~4 分钟）\n\n发现（3 warnings, 5 info）：\n- **[warning]** 前 2 页纯文本无 display item，Figure 1 直到第 3 页才出现。\n- **[warning]** 正文 8 页仅 1 个 figure + 5 个 table，视觉 table-heavy。建议增加 1 个结果可视化图。\n- **[warning]** 第 8 页整页纯文本（Related Work + Conclusion），与前面 table 密集区形成节奏断裂。\n- **[info]** Figure 1 内部分标注文字字号偏小，接近 8pt 可读下限。\n- **[info]** Table 25 使用纯红/绿色标注，色盲不友好。\n- **[info]** Appendix B 连续 5 页纯文本。\n- **[info]** 第 6-7 页各含 2 个 table，信息密度高但无冗余。\n- **[info]** Figure 4（附录）轴标签偏小，灰度打印区分度有限。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.5 | 3.0 | **3.0** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4 | 4 | **4** |\n\n### Overall: 3.5 — Borderline Conference\n\n两位 Reviewer 独立评估后完全一致：3.5 Borderline Conference。交叉回应后共识进一步加强。\n\n**核心判断**：OntoCoDec 是一篇技术上扎实、工程质量高的工作。Decidability taxonomy 和 enabling dependency 是有价值的概念贡献，消融设计严谨，跨模型验证充分。但两个关键问题阻碍接收至 Conference 水平：\n1. **缺少 BoostCD/GCD 等最直接竞争方法的实验对比**（连续 3 轮提出），无法证明相对优势；\n2. **Grammar-first fallback 36.6% 触发率**未在正文诚实讨论，且 fine-tuned fallback 率未报告，削弱了\"type-constrained\"的核心声称。\n\n评估范围（3 个英语数据集、7-8B 模型）相对泛化性声称偏窄；WikiEvents 20-doc 评估和 κ̄ 的 2 数据点进一步削弱证据说服力。新颖性在 principled composition 层面，而非组件创新。\n\n若能补充 BoostCD/GCD 对比实验、报告 fine-tuned fallback 率、并限定泛化性声称，本文有望达到 Conference 水平（4.0）。当前版本推荐 **Borderline Conference（3.5）**，有较好的 Findings 接收前景。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"applicable to any autoregressive LM\" → 限定为 \"autoregressive LMs with logits access; validated on 7-70B\"\n- \"compiles constraints automatically from any IE ontology\" → 限定为已验证的 ontology 规模\n- Contribution 列表中 EE 扩展应从 \"systematic evaluation\" 降级为 \"preliminary demonstration\"\n\n### §3 Method\n- Proposition 1 适用边界（有限实体集 + canonical IDs 退化）应更明确讨论\n- \"Best-effort pair-based enforcement\" 首次出现时给出完整 inline definition\n\n### §4 Constraint Composition\n- Grammar-first fallback 的 36.6% 触发率应在此 section 正文中讨论，而非仅在 Appendix Table 7\n- κ̄ 的 Appendix D 推断统计（Spearman ρ with n=6）应移除或限定\n- Fine-tuned 设置下的 fallback 率是关键缺失数据\n\n### §5 Experiments\n- 需添加 BoostCD 和/或 GCD 实验对比（must-fix）\n- WikiEvents fine-tuning 结论加 \"preliminary\" 限定，报告置信区间\n- DocRED beam search 应在完整 998-doc 集上至少报告一个模型的结果\n- 70B 评估可保留但应精简以节省空间给 baseline 对比\n\n### §6 Related Work\n- 添加 TANL (Paolini et al., 2021) 引用\n- 正文定位论述偏简，关键区分（preventive vs corrective, forward-only vs backtracking）应留在正文\n\n### Bibliography\n- 清理 orphan entries（chen2024agentre, fan2024fsn）\n- 确认 formattax2026 和 regino2025kgcurator 的 arXiv ID\n\n### Visual（非评分项）\n- 考虑增加 1 个结果可视化图改善正文视觉节奏\n- Table 25 补充非颜色视觉标记（色盲友好）",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 — Borderline Conference",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1460 · 2026-05-20T20:07:46.034502+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4018
}
```

</details>

---


### Assistant

_source line 1461 · 2026-05-20T20:07:56.409479+00:00_

审稿报告已投递。

**Round 14 审稿完成。**

- **评分**：3.5 — Borderline Conference（两位 Reviewer 完全一致）
- **2 个 Must-Fix**：(1) 缺少 BoostCD/GCD baseline 实验对比（连续 3 轮未解决）；(2) Fallback 36.6% 触发率未在正文讨论，fine-tuned fallback 率未报告
- **5 个 Should-Fix**：WikiEvents 20-doc 统计功效、κ̄ 仅 2 数据点、DocRED beam 50-doc 子集、泛化性声称过宽、新颖性适中
- **Issue Tracker 已同步**：R13 多项 issue 本轮未被提及（R13-MF1 页数溢出、R13-MF2 CF 低估等），标注为可能已修复待确认
- **Visual Check**：已完成，3 warnings / 5 info，不阻塞报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1462 · 2026-05-20T20:07:58.896234+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：在 R1 的 8 条 Weakness 中，我同意 7 条（W1/W3/W5/W6/W7/W8 完全同意，W2 同意但降为 major），仅对 W4（Proposition 1 的 position-indexing）提出反驳——Appendix O 已有 "Position indexing vs. name referencing" 的讨论。两位 Reviewer 的核心判断一致：3.5 Borderline Conference，technically sound 但 novelty 适中、evaluation scope 偏窄。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1463 · 2026-05-20T20:08:13.290459+00:00_

审稿报告已投递完毕。

**Round 14 审稿总结**：

- **Overall: 3.5 — Borderline Conference**（R1、R2 完全一致）
- **2 个 Must-Fix**：(1) 缺少 BoostCD/GCD 实验对比（连续 3 轮提出）；(2) Fallback 36.6% 触发率未在正文讨论，fine-tuned fallback 率缺失
- **5 个 Should-Fix**：WikiEvents 20-doc 统计功效、κ̄ 仅 2 数据点、DocRED beam 50-doc 子集、泛化性声称过宽、新颖性适中
- **Issue Tracker 已同步**：R13 多个 issue 本轮未被提及（页数溢出、CF 低估、compile 措辞等），可能已修复，待 Research Director 确认
- **视觉审查已完成**：3 warnings（table-heavy、Figure 1 位置偏后、末页纯文本断裂），5 info
- **外部审稿**：未配置

报告已通过 `submit_review_report_to_research_director` 单向投递，审稿流程结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 108

## Round 108

60 recorded events


### User

_source line 1464 · 2026-05-21T01:16:22.137712+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1465 · 2026-05-21T01:16:28.745633+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1466 · 2026-05-21T01:16:28.796662+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1467 · 2026-05-21T01:16:35.436773+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1468 · 2026-05-21T01:16:35.437207+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1469 · 2026-05-21T01:16:37.194910+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1470 · 2026-05-21T01:16:37.195295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1471 · 2026-05-21T01:16:37.748446+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1472 · 2026-05-21T01:16:37.799449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1473 · 2026-05-21T01:16:43.182435+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1474 · 2026-05-21T01:16:45.604052+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (126 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| r14_llama_docred_beam4_998 | Beam=4 S1 constrained on full DocRED 998-doc with Llama-3.1-8B will confirm DR elimination and R-F1 stability seen in 50-doc subset, providing second model evidence for SF3 | — | — | — |\n| r14_qwen_docred_beam4_998 | Beam=4 S1 constrained on full DocRED 998-doc test set will show consistent DR elimination and R-F1 stability compared to 50-doc subset, addressing reviewer concern about subset representativeness | — | — | — |\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- d066_sweep_llama_docred_beam4_s1（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_sweep_llama_scierc_beam8_s1_551** (success): d066 SciERC beam sweep: Llama beam8 constrained (full_s1) on 551-sentence test set. Last Llama SciERC config. ← 基于 d066_beam_sweep\n- **d066_swee
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2421
}
```

</details>

---


### Tool call

_source line 1475 · 2026-05-21T01:16:45.604613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1476 · 2026-05-21T01:16:46.510564+00:00_

-rw-r--r-- 1 ubuntu ubuntu 535757 May 20 21:46 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu   7278 May 20 20:23 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1477 · 2026-05-21T01:16:46.661557+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-21T01:16:47.013522+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-21T01:16:53.093062+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"}]

Based on the search results, I found
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6431
}
```

</details>

---


### Tool result

_source line 1480 · 2026-05-21T01:16:53.143887+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6130
}
```

</details>

---


### Tool call

_source line 1481 · 2026-05-21T01:16:57.321865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limits format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limits format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-21T01:16:57.673813+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 1483 · 2026-05-21T01:16:58.427993+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "memory.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1484 · 2026-05-21T01:17:03.007014+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limits format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"System Demonstrations - ACL 2026","url":"https://2026.aclweb.org/calls/system_demonstration/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's a summary of the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

All submissions must have a section titled "Limitations" which discusses th
…[truncated 853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5685
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-21T01:17:03.811007+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/vi
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6137
}
```

</details>

---


### Tool result

_source line 1486 · 2026-05-21T01:17:03.811728+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Memory — schema_semantic_constrained_ie\\n\\n> 非 metrics 性质的决策原因、约束、经验教训。Metrics 查 registry。\\n\\n## westd-21461 环境指南\\n- 系统 python3 (`/usr/bin/python3` 3.10) **无 ML 库**\\n- conda python3 (`/root/miniconda3/bin/python3` 3.12) 有完整环境：torch 2.8.0+cu128, transformers 5.8.1, peft 0.19.1, trl 1.4.0\\n- `python` 命令不存在，必须用 `python3` 或绝对路径\\n- **必须** `source /root/miniconda3/bin/activate` 激活 conda 后再执行\\n- **无外网**：必须设置 `TRANSFORMERS_OFFLINE=1` + `HF_HUB_OFFLINE=1`\\n- transformers 5.8.1 忽略 `WANDB_DISABLED=true`，必须在 TrainingArguments 中设 `report_to=\\\"none\\\"`\\n- submit_training_job 用 tmux（sh），bash builtins 必须用 `bash -c \\\"...\\\"` 或自包含 bash 脚本\\n\\n## westd-16980 环境指南\\n- conda python3 (`/root/miniconda3/bin/python3` 3.12), torch 2.10.0+cu128\\n- peft 0.19.1 有 AWQ dispatcher bug：`is_gptqmodel_available()` 在 optimum 版本低时 raise 而非 return False\\n- **必须 monkey-patch**：`import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False`\\n- 根分区磁盘小，checkpoint 必须写到 `/root/autodl-tmp/` 数据卷\\n\\n## 磁盘空间教训\\n- westd-21461 根分区只有 ~11G，merge 16G 模型会写满。所有 checkpoint 输出路径用 `/root/autodl-tmp/`\\n- westd-16980 同理，数据卷 `/root/autodl-tmp/` 有 109GB+\\n- westd-21461 全量 FT checkpoint (~16GB) 保存时可能磁盘满，需确保 `/root/autodl-tmp/` 有足够空间 + `save_total_limit=1`\\n\\n## P1 EE FT 失败根因汇总（r1-r4）\\n1. **r1**: `python: command not found`（tmux 用 sh，PATH 无 conda）\\n2. **r2**: HF Hub Errno 101 网络不可达 + `| tee` 掩盖退出码 + 虚假 COMPLETE 标记\\n3. **r3**: wandb 未安装但 transformers 尝试加载 WandbCallback\\n4. **r4**: 训练成功但 parse rate 极低（10-25%）——根因是 schema mismatch bug\\n- **教训**: 长 one-liner 在 tmux 里极脆弱，必须写自包含 bash 脚本 + `set -eo pipefail`\\n\\n## D060 Schema Mismatch Bug（关键教训）\\n- **根因**: `compiler/ontology_compiler.py:294` 的 `compile_event_json_schema()` 生成 `required: [\\\"entities\\\", \\\"events\\\"]`，但 FT 训练数据只有 `{\\\"events\\\": [...]}`\\n- **
…[truncated 1523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5383
}
```

</details>

---


### Tool call

_source line 1487 · 2026-05-21T01:17:10.091837+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers submission format anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers submission format anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1488 · 2026-05-21T01:17:10.444075+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 cycle deadline submission requirements anonymization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 cycle deadline submission requirements anonymization"
  }
}
```

</details>

---


### Tool call

_source line 1489 · 2026-05-21T01:17:12.553761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1490 · 2026-05-21T01:17:12.554263+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-21T01:17:16.028592+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers submission format anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"}]

Based on the search results from the EMNLP 2026 Call for Main Conference Papers, here are the key findings regarding submission format and anonymity:

**Anonymity Policy:**
Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind. More specifically, reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible.

**Submission Format Options:**
Authors will be given the option through ARR to make their anonymized submitted articles publicly visible.

This means that while the traditional anonymity period (where papers must be anonymous before submission) is not required, the actual review process maintains double-blind review, and authors have the choice to make their papers publicly visible during the review process if they wish.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5936
}
```

</details>

---


### Tool result

_source line 1492 · 2026-05-21T01:17:17.183948+00:00_

Web search results for query: "ACL Rolling Review May 2026 cycle deadline submission requirements anonymization"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"}]

Based on the search results, here is information about the ACL Rolling Review May 2026 cycle deadline submission requirements and anonymization:

## Submission Anonymization Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Supplementary materials, including any links to repositories, should also be anonymized
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6739
}
```

</details>

---


### Tool call

_source line 1493 · 2026-05-21T01:17:23.464486+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1494 · 2026-05-21T01:17:23.465137+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1495 · 2026-05-21T01:17:27.560058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1496 · 2026-05-21T01:17:28.414852+00:00_

NO_CONFIG_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1497 · 2026-05-21T01:17:28.566440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1498 · 2026-05-21T01:17:29.379064+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars guaranteeing JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} near-eliminates DR (94--100\% reduction) with negligible R-F1 impact ($\pm$0.6\,pp), with cross-field (CF) rates of 0--9.9\% (zero-shot) to $\leq$1.2\% (fine-tuned); \S\ref{sec:scierc-results} analyzes conditions.
7	CF is substantially reduced by beam search under favorable conditions (low $\bar{\kappa}$ or fine-tuned settings).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across four autoregressive LMs (7--70B) with logits access and three tokenizer families (up to 96 relation types).
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 812
}
```

</details>

---


### Tool call

_source line 1499 · 2026-05-21T01:17:29.530586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1500 · 2026-05-21T01:17:29.531278+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption; type violation elimination guarantees ontological consistency of constructed KGs independent of extraction F1, making reliable constraint enforcement necessary.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
16	Training-based approa
…[truncated 2951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1501 · 2026-05-21T01:17:35.458657+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find config files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find config files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 1502 · 2026-05-21T01:17:36.415460+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-21T01:17:36.516318+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-21T01:17:36.567375+00:00_

# Review Issues Tracker — schema_semantic_constrained_ie
# Updated: R14 修改完成 + R15 提交 (D077), 2026-05-20

# ============================================================
# Round 14 Must-Fix
# ============================================================

- id: "R14-MF1"
  summary: "缺少 BoostCD/GCD 最直接竞争方法的实验对比（连续 3 轮 R12-R14）"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 12
  last_seen_round: 14
  mentions:
    - round: 12
      reviewers: [1, 2]
      note: "R12-SF2: should-fix"
    - round: 13
      reviewers: [1, 2]
      note: "R13-MF3: 升级为 must-fix"
    - round: 14
      reviewers: [1, 2]
      note: "R14-MF1: 连续 3 轮。要求 best-effort adaptation。"
  action_items:
    - round: 14
      action: "战略转换：grammar-only ablation reframed as BoostCD-equivalent Level 1 约束实验。§6 新段论证 Level 1 仅 24% DR reduction，Level 2 额外 70pp"
      assigned_to: paper_agent
      status: completed
  resolution: ""
  resolution_round: null

- id: "R14-MF2"
  summary: "Grammar-first fallback 36.6% 触发率 + FT fallback 率未报告"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 14
  last_seen_round: 14
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "R1 critical, R2 agree with nuance→major。36.6% token-level 被澄清为 first-token 0.5-5.7% ZS。FT ≤0.11%。"
  action_items:
    - round: 14
      action: "Agent 计算 FT fallback rate（≤0.11%），Paper Agent §4 新增 fallback 分析段落 + Table 7 caption 澄清 + root cause + composability 机制解释"
      assigned_to: agent + paper_agent
      status: completed
  resolution: ""
  resolution_round: null

# ============================================================
# Round 14 Should-Fix
# ============================================================

- id: "R14-SF1"
  summary: "WikiEvents 20-doc test set 统计功效极低"
  category: experiment
  severity: warning
  status: in_progress
  first_raised_round: 12
  last_seen_round: 14
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "R1-W3 major,
…[truncated 8254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1505 · 2026-05-21T01:17:42.000466+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -path \"*/schema_semantic_constrained_ie*\" -name \"config*\" -type f 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -path \"*/schema_semantic_constrained_ie*\" -name \"config*\" -type f 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1506 · 2026-05-21T01:17:42.201899+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1507 · 2026-05-21T01:17:44.764901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -name \"projects.yaml\" -o -name \"project_config.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -5",
  "description": "Find project settings files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -name \"projects.yaml\" -o -name \"project_config.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -5",
    "description": "Find project settings files"
  }
}
```

</details>

---


### Tool result

_source line 1508 · 2026-05-21T01:17:45.454924+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 690
}
```

</details>

---


### Tool call

_source line 1509 · 2026-05-21T01:17:47.808902+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find YAML config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find YAML config files"
  }
}
```

</details>

---


### Tool result

_source line 1510 · 2026-05-21T01:17:47.909829+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1511 · 2026-05-21T01:17:50.622086+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/ 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/ 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1512 · 2026-05-21T01:17:51.526396+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1513 · 2026-05-21T01:17:51.627882+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml 2>/dev/null || echo \"NOT_IN_WORKSPACE\"",
  "description": "Check workspace yaml for external review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml 2>/dev/null || echo \"NOT_IN_WORKSPACE\"",
    "description": "Check workspace yaml for external review"
  }
}
```

</details>

---


### Tool result

_source line 1514 · 2026-05-21T01:17:51.678638+00:00_

NOT_IN_WORKSPACE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1515 · 2026-05-21T01:17:56.306131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1516 · 2026-05-21T01:17:56.809210+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf (523.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1517 · 2026-05-21T01:19:02.889884+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验充分性** 审查。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求（已通过 web search 确认）\n- **目标**: EMNLP 2026, ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必须有独立 Limitations section，不计入页数\n- **模板**: ACL 模板，必须使用 `[review]` 选项\n- **匿名**: Double-blind review（论文中不得出现作者信息、去匿名化的自引）\n- **附录**: 双栏格式\n- **Checklist**: ARR Responsible NLP Research Checklist 必须填写\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **Decidability 分析**：Proposition 1（Level 2 ⊄ Level 1）的证明是否严谨？三层分类（context-free / prefix-decidable with state / non-local）是否合理、边界是否清晰？\n2. **两层架构设计**：grammar layer 和 semantic layer 的交互（enabling dependency）是否有充分论证？grammar-first fallback 机制是否合理？fallback 触发率和 FT 后下降的解释是否令人信服？\n3. **Constraint tightness κ̄**：作为描述性指标的定位是否恰当？基于有限数据点的关联分析是否过度解读？\n4. **形式化声称**：论文中的\"guarantee\"、\"formal\"等措辞是否与实际提供的保证水平匹配？（注意 CF 问题、fallback 导致的 semantic layer 被跳过等情况）\n\n### 实验充分性\n1. **Ablation 设计**：五因素消融（Table 1）是否充分隔离了各层贡献？S1 vs S2 对比是否公平？\n2. **数据集覆盖**：3 个英语数据集（SciERC/DocRED/WikiEvents）是否足够？WikiEvents 20-doc test set 的统计功效如何？\n3. **模型覆盖**：4 个 7-70B 模型，3 个 tokenizer family——覆盖是否充分？70B 仅 preliminary 是否足够？\n4. **Fine-tuning composability**：Table 2 的 paired bootstrap 检验是否充分证明 R-F1 无显著下降？DR 显著下降的 p 值是否可靠？\n5. **Beam search 评估**：DocRED beam search 的评估范围是否充分（50-doc subset vs full set）？\n6. **Baseline 对比**：与 post-hoc filtering 的对比是否公平？是否缺少与 BoostCD/GCD/EnriCo/IterGen 等最直接竞争方法的实验对比？\n7. **Runtime overhead**：+13.1% (greedy) 和 1.54× (beam) 的延迟数据是否充分报告？scalability benchmark 是否可信？\n8. **统计显著性**：各主要结论是否有统计检验支撑？bootstrap 的参数设置是否合理？\n\n### 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle\n\n请给出完整审稿意见，包括：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，标明严重程度 critical/major/minor) → Questions → Missing References → Overall Assessment (评分+置信度+理由)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验充分性** 审查。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求（已通过 web search 确认）\n- **目标**: EMNLP 2026, ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必须有独立 Limitations section，不计入页数\n- **模板**: ACL 模板，必须使用 `[review]` 选项\n- **匿名**: Double-blind review（论文中不得出现作者信息、去匿名化的自引）\n- **附录**: 双栏格式\n- **Checklist**: ARR Responsible NLP Research Checklist 必须填写\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **Decidability 分析**：Proposition 1（Level 2 ⊄ Level 1）的证明是否严谨？三层分类（context-free / prefix-decidable with state / non-local）是否合理、边界是否清晰？\n2. **两层架构设计**：grammar layer 和 semantic layer 的交互（enabling dependency）是否有充分论证？grammar-first fallback 机制是否合理？fallback 触发率和 FT 后下降的解释是否令人信服？\n3. **Constraint tightness κ̄**：作为描述性指标的定位是否恰当？基于有限数据点的关联分析是否过度解读？\n4. **形式化声称**：论文中的\"guarantee\"、\"formal\"等措辞是否与实际提供的保证水平匹配？（注意 CF 问题、fallback 导致的 semantic layer 被跳过等情况）\n\n### 实验充分性\n1. **Ablation 设计**：五因素消融（Table 1）是否充分隔离了各层贡献？S1 vs S2 对比是否公平？\n2. **数据集覆盖**：3 个英语数据集（SciERC/DocRED/WikiEvents）是否足够？WikiEvents 20-doc test set 的统计功效如何？\n3. **模型覆盖**：4 个 7-70B 模型，3 个 tokenizer family——覆盖是否充分？70B 仅 preliminary 是否足够？\n4. **Fine-tuning composability**：Table 2 的 paired bootstrap 检验是否充分证明 R-F1 无显著下降？DR 显著下降的 p 值是否可靠？\n5. **Beam search 评估**：DocRED beam search 的评估范围是否充分（50-doc subset vs full set）？\n6. **Baseline 对比**：与 post-hoc filtering 的对比是否公平？是否缺少与 BoostCD/GCD/EnriCo/IterGen 等最直接竞争方法的实验对比？\n7. **Runtime overhead**：+13.1% (greedy) 和 1.54× (beam) 的延迟数据是否充分报告？scalability benchmark 是否可信？\n8. **统计显著性**：各主要结论是否有统计检验支撑？bootstrap 的参数设置是否合理？\n\n### 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle\n\n请给出完整审稿意见，包括：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，标明严重程度 critical/major/minor) → Questions → Missing References → Overall Assessment (评分+置信度+理由)。"
  }
}
```

</details>

---


### Tool result

_source line 1518 · 2026-05-21T01:19:24.408272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21518
}
```

</details>

---


### Tool call

_source line 1519 · 2026-05-21T01:19:24.559854+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 论文完整性 + 格式合规** 审查。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求（已通过 web search 确认）\n- **目标**: EMNLP 2026, ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必须有独立 Limitations section，不计入页数\n- **模板**: ACL 模板，必须使用 `[review]` 选项\n- **匿名**: Double-blind review（论文中不得出现作者信息、去匿名化的自引）\n- **附录**: 双栏格式\n- **Checklist**: ARR Responsible NLP Research Checklist 必须填写\n- **特别注意**: 从 2025年7月起，附录不使用双栏格式会被 desk reject\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **核心创新定位**：OntoCoDec 的主要创新是什么？是组件级创新（grammar/semantic layer 各自新颖）还是系统级创新（composition + formalization）？在 constrained decoding 和 schema-aware IE 的既有工作中，新颖性是否足够？\n2. **与最近竞品的差异化**：与 BoostCD (Sakota et al., 2025)、GCD (Geng et al., 2023)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2024) 的区别是否清晰？论文是否充分论证了 OntoCoDec 超越这些方法的地方？\n3. **Decidability taxonomy 的理论贡献**：三层分类作为理论贡献是否足够有意义？是否有类似的分类在先前工作中已存在？\n4. **Constraint tightness κ̄**：作为新概念的价值如何？是否 trivial（即 schema 越松约束效果越好这一直觉的量化）？\n\n### 论文完整性\n1. **Related Work 覆盖**：是否遗漏重要相关工作？特别注意：(a) constrained decoding 领域（PICARD, SynCode, BoostCD, GCD）；(b) schema-aware IE（GoLLIE, TANL, InstructUIE）；(c) type constraint enforcement in KG（KGCURATOR, FormaTax）\n2. **论述逻辑**：Introduction → Background → Method → Experiments → Related Work → Conclusion 的叙事是否连贯？各 Section 之间的过渡是否自然？\n3. **声称与证据的一致性**：Abstract/Intro 中的声称是否都有实验支撑？是否有过度声称（overclaim）的情况？\n4. **Limitations 完整性**：是否诚实地报告了所有重要限制？CF 问题、WikiEvents 小样本、仅英语数据集等是否充分讨论？\n\n### 格式合规（逐项检查）\n1. **页数**：正文是否 ≤ 8 页？\n2. **匿名**：是否有泄露作者身份的信息？（检查自引方式、代码链接、acknowledgment）\n3. **模板**：是否使用 ACL 模板 + `[review]` 选项？\n4. **Limitations section**：是否存在？位置是否在 conclusion 之后、references 之前？\n5. **Checklist**：ARR Responsible NLP Checklist 是否填写？\n6. **附录格式**：是否双栏？\n7. **引用格式**：是否使用 natbib？\n8. **Ethics Statement**：是否存在？\n\n### 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle\n\n请给出完整审稿意见，包括：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，标明严重程度 critical/major/minor) → Questions → Missing References → Overall Assessment (评分+置信度+理由)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 论文完整性 + 格式合规** 审查。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求（已通过 web search 确认）\n- **目标**: EMNLP 2026, ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数**: Long paper 8 页正文 + 无限参考文献\n- **Limitations**: 必须有独立 Limitations section，不计入页数\n- **模板**: ACL 模板，必须使用 `[review]` 选项\n- **匿名**: Double-blind review（论文中不得出现作者信息、去匿名化的自引）\n- **附录**: 双栏格式\n- **Checklist**: ARR Responsible NLP Research Checklist 必须填写\n- **特别注意**: 从 2025年7月起，附录不使用双栏格式会被 desk reject\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **核心创新定位**：OntoCoDec 的主要创新是什么？是组件级创新（grammar/semantic layer 各自新颖）还是系统级创新（composition + formalization）？在 constrained decoding 和 schema-aware IE 的既有工作中，新颖性是否足够？\n2. **与最近竞品的差异化**：与 BoostCD (Sakota et al., 2025)、GCD (Geng et al., 2023)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2024) 的区别是否清晰？论文是否充分论证了 OntoCoDec 超越这些方法的地方？\n3. **Decidability taxonomy 的理论贡献**：三层分类作为理论贡献是否足够有意义？是否有类似的分类在先前工作中已存在？\n4. **Constraint tightness κ̄**：作为新概念的价值如何？是否 trivial（即 schema 越松约束效果越好这一直觉的量化）？\n\n### 论文完整性\n1. **Related Work 覆盖**：是否遗漏重要相关工作？特别注意：(a) constrained decoding 领域（PICARD, SynCode, BoostCD, GCD）；(b) schema-aware IE（GoLLIE, TANL, InstructUIE）；(c) type constraint enforcement in KG（KGCURATOR, FormaTax）\n2. **论述逻辑**：Introduction → Background → Method → Experiments → Related Work → Conclusion 的叙事是否连贯？各 Section 之间的过渡是否自然？\n3. **声称与证据的一致性**：Abstract/Intro 中的声称是否都有实验支撑？是否有过度声称（overclaim）的情况？\n4. **Limitations 完整性**：是否诚实地报告了所有重要限制？CF 问题、WikiEvents 小样本、仅英语数据集等是否充分讨论？\n\n### 格式合规（逐项检查）\n1. **页数**：正文是否 ≤ 8 页？\n2. **匿名**：是否有泄露作者身份的信息？（检查自引方式、代码链接、acknowledgment）\n3. **模板**：是否使用 ACL 模板 + `[review]` 选项？\n4. **Limitations section**：是否存在？位置是否在 conclusion 之后、references 之前？\n5. **Checklist**：ARR Responsible NLP Checklist 是否填写？\n6. **附录格式**：是否双栏？\n7. **引用格式**：是否使用 natbib？\n8. **Ethics Statement**：是否存在？\n\n### 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle\n\n请给出完整审稿意见，包括：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，标明严重程度 critical/major/minor) → Questions → Missing References → Overall Assessment (评分+置信度+理由)。"
  }
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-21T01:19:25.877863+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-21T01:19:26.233023+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1673
}
```

</details>

---


### Tool result

_source line 1522 · 2026-05-21T01:19:28.284416+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2406
}
```

</details>

---


### Assistant

_source line 1523 · 2026-05-21T01:19:42.670867+00:00_

**Round 1 已启动：**
- Reviewer 1（方法严谨性 + 实验充分性）→ 已派发 ✓
- Reviewer 2（新颖性 + 论文完整性 + 格式合规）→ 已派发 ✓
- 视觉审查 Agent → 已启动 ✓
- 外部审稿 → 未配置，跳过

等待 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 109

## Round 109

2 recorded events


### User

_source line 1524 · 2026-05-21T01:26:52.508179+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

---

## 总体评分

**Overall**: 3.0 / 5（Findings）
**Confidence**: 4 / 5
**一句话总结**: 形式化分析（decidability taxonomy + Proposition 1）是本文最大亮点，两层架构设计合理，但缺少与最直接竞争方法（BoostCD/CRANE/IterGen）的实验对比是影响接收的关键短板，加上"guarantee"措辞与实际 fallback 机制的不一致，整体贡献尚不足以支撑 Conference 级别接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | Decidability 分析和证明基本严谨，但"guarantee"措辞与 fallback 机制存在内在矛盾；κ̄ 分析数据点不足（n=6）|
| **Excitement** | 3.0 / 5 | Decidability-guided 设计在 IE constrained decoding 中有新意，但缺乏 baseline 对比难以评估边际贡献 |
| **Reproducibility** | 4.0 / 5 | Appendix 提供完整 prompt（Table 6）、超参数（Appendix A/G）、实现细节，声称将开源代码 |
| **Clarity** | 3.5 / 5 | 主文结构清晰，但信息密度极高（8页塞入形式化分析+3数据集+4模型），部分关键概念如 enabling dependency 主文解释不充分 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **缺少与 constrained-decoding 竞争方法的实验对比**
- 具体位置：Section 5 全部实验 + Section 6 Related Work
- 问题：论文在 Related Work（Section 6, p8; Appendix B, p15-18）中详细讨论了 BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025)、GCD (Geng et al., 2023)、EnriCo (Zaratiana et al., 2024) 等在解码时施加约束的方法，但实验中唯一的对比是 unconstrained decoding 和 post-hoc filtering。论文声称这些方法是"complementary"（Section 6），但这一论点未经实验验证。
- 为什么影响接收：对于一篇提出 constrained decoding framework 的论文，不与同类型方法做 head-to-head 对比，reviewer 无法评估其边际贡献。尤其 BoostCD 和 GCD 同样基于 grammar-constrained decoding 处理 IE 任务，且在相同数据集（SciERC）上有结果，对比缺失不可接受。
- 建议修改方向：至少在 SciERC 上与 GCD（同一作者群 2023 EMNLP）和 BoostCD（2025 EMNLP）做 head-to-head 对比，报告 R-F1、DR、CF、latency。若运行困难，应明确说明原因并做定性分析表格。

**N2** [critical] **"Guarantee" 措辞与实际机制不匹配**
- 具体位置：Abstract ("formal guarantees at each layer")、Section 1 ("formal guarantees")、Section 3.3 ("best-effort pair-based enforcement")、Section 3.4 ("grammar-first fallback")
- 问题：论文多处使用"guarantee"一词，但实际存在三个层面的保证缺口：
  (a) Grammar-first fallback（§3.4）：当语法和语义约束冲突时，semantic layer 被跳过。Appendix C Table 7 报告 fallback 在 SciERC Qwen 上触发率为 first-token position 的 0.46%，但这恰恰是 type error 最可能发生的高信息量位置。
  (b) Level 3 constraints（cross-triple consistency）显式未被强制——Section 2 明确承认这一层由 beam search 部分处理（§5.3）。
  (c) 即使在 Full S1 配置下，Table 1 仍显示残余 CF=0.08-0.35%。
  论文 Limitations section（p10）部分承认了这些，但 Abstract 和 Introduction 中的"guarantee"表述未做对应限定。
- 为什么影响接收：这构成 claim 与 evidence 之间的系统性不一致。在正式同行评审中，overclaiming 是严重问题。
- 建议修改方向：将"guarantee"替换为"enforcement"或"near-elimination"等更准确的措辞；在 Abstract 中明确 fallback 的存在及其含义；可考虑添加"guarantee conditional on no grammar-semantic conflict"的限定表述。

**N3** [major] **WikiEvents 评估统计效能不足**
- 具体位置：Section 5.4（p7-8）、Table 5
- 问题：WikiEvents zero-shot 测试集仅 20 篇文档（n=20, §5.4 注释）。尽管论文称"preliminary"，但仍基于此得出 fine-tuning composability 结论（Table 5 报告 R-F1 CI 约 ±0.5 pp）。20 篇文档的 bootstrap CI 可信度有限——Table 5 中 EV+RoV 变异大、AC 为 0。完整 WikiEvents 语料（246篇）仅用于 zero-shot，未用于 fine-tuning 评估。
- 为什么影响接收：以不充分的样本量支撑 fine-tuning composability 的 claim，削弱了 Section 5.4 的结论可靠性。
- 建议修改方向：要么在完整测试集上报告 fine-tuning 结果，要么明确将 WikiEvents fine-tuning 结论标记为"indicative only"并从主要 claim 中移除。

**N4** [major] **70B 评估不足以支撑"applicable to autoregressive LMs"的广泛声称**
- 具体位置：Abstract ("applicable to autoregressive LMs with logits access")、Section 5.5（p8, 仅 3 行描述）
- 问题：论文声称适用于所有有 logits 访问的自回归 LM，但完整评估仅覆盖 7-8B 模型。70B 结果（§5.5）仅 Llama-3.1-70B 一个模型、两个数据集（SciERC/DocRED）、INT8 量化、无 ablation、无 fine-tuning。更大模型可能有不同的 violation pattern（70B 模型 DR 可能本身更低，constraint enforcement 的边际价值需要独立验证）。
- 为什么影响接收：核心 generality claim 缺乏充分实验支撑。
- 建议修改方向：将 Abstract 中的声称限定为"validated on 7-8B scale models with preliminary 70B results"；或补充 70B 的完整 ablation。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **κ̄（constraint tightness）基于 n=6 数据点的关联分析**
- 具体位置：Section 4（p5 定义）、Appendix C Figure 2（p21）
- 问题：Figure 2 scatter plot 仅 4 个 model-dataset 组合（6 个数据点含 fine-tuned variants）。论文诚实地承认"p>0.05, df=2, this constitutes a descriptive characterization rather than a confirmatory statistical test"（p21），但 §1 仍将其列为主要贡献之一（"a descriptive metric correlating schema restrictiveness with enforcement outcomes"）。
- 建议：降低 κ̄ 在 §1 contributions 中的定位；或在更多 schema（如不同 ontology 子集、per-relation 分析）上验证。

**W2** [warning] **Fallback 机制与核心 claim 的张力未充分分析**
- 具体位置：Section 3.4、Appendix C（Table 7, p20）
- 问题：Grammar-first fallback 的存在意味着在模型最可能产生 type-incompatible 输出时，semantic layer 恰恰被绕过。Table 7 报告 fallback 触发率（0.46% on SciERC），但未分析 residual DR violations 中有多少 fraction 直接源自 fallback 事件。也未分析 fallback 后模型选择的 token 是否倾向于 type-correct（即 grammar-only mask 是否恰好也满足 type constraint）。Appendix C 第 20 页讨论了 CF-DR trade-off 但止步于描述性统计，缺乏 causal tracing。
- 建议：增加分析：(1) 追踪 residual DR violations 到 fallback vs non-fallback positions；(2) 在 fallback positions 上比较 grammar-only mask 选出的 token 的 type-correctness 概率。

**W3** [warning] **S1 vs S2 配置选择缺乏充分论证**
- 具体位置：Table 1（p6）、Section 5.1
- 问题：Table 1 显示 S2（two-pass pipeline）R-F1 略高于 S1（8.03→8.36 on SciERC），论文将 S2 定为"primary configuration"但未深入分析 S1 vs S2 的适用场景。S2 引入额外 latency（两次推理），但 cost-benefit 分析缺失。此外 S1 在 CF 上表现更好（0.035 vs 0.08），说明 joint extraction 更有利于 cross-field consistency，但论文未讨论这一 trade-off。
- 建议：增加 S1 vs S2 的 latency 对比；讨论何种场景下 S1 优于 S2（例如 latency-sensitive 部署）。

**W4** [warning] **仅英语数据集评估**
- 具体位置：Section 5 全部实验
- 问题：3 个数据集均为英语。OntoCoDec 依赖 tokenizer-specific prefix map 和 vocabulary constraints，跨语言泛化是一个有意义的开放问题——不同语言的 subword tokenization 可能导致 continuation mask 行为差异显著。Limitations（p10）提到"tokenizer dependency"但未明确标注语言覆盖缺口。
- 建议：在 Limitations 中显式讨论语言覆盖限制；若条件允许在一个非英语数据集上补充验证。

**W5** [warning] **Post-hoc filtering 对比可能不够公平**
- 具体位置：Section 5.1（p5-6）、Appendix L（p23）
- 问题：Post-hoc filtering baseline 在生成后过滤整个 triple，而 OntoCoDec 在生成中修改 token 选择——这是本质不同的机制。论文基于此得出"post-hoc filtering achieves DR→0% but with 15-74% rejection rates"（p5）的结论，但一个更公平的 baseline 应该是 post-hoc correction（替换 invalid types 而非丢弃 triple）。
- 建议：增加 post-hoc type correction baseline（例如将 invalid relation type 映射到最近的 valid type），或在讨论中明确说明对比的局限性。

---

## 小问题（不影响接收）

- **页数**：主文内容延伸至第 9 页（约 8 行 Conclusion 溢出），严格来说超出 8 页限制。建议压缩 Section 7 Discussion and Conclusion 回到第 8 页内。
- **Table 1 列名**："Tgt." 列含义不直观，首次出现未解释（需翻到 footnote 才知是"target: included in constrained set"）。
- **"Enabling dependency" 概念**（§3.4）在主文中引入但未给出正式定义，读者需推断其含义。Corollary 1 是附录才有详细阐述。
- **Figure 1**：信息密度高、visual hierarchy 不够清晰，grammar layer 和 semantic layer 的交互路径需要更直观的视觉区分。
- **Orphan bib 条目**：`chen2024agentre` 和 `fan2024fsn` 在 .bib 中但未被引用，应清理。
- **引用格式**：少数条目存在 author name encoding mismatch（如 Šakota→sakota, De Cao→Cao），属 BibTeX 编码问题，不影响可信度。

---

## Questions for Authors

1. Residual DR violations 中有多少比例直接源自 grammar-first fallback 事件？能否做 causal tracing 确认 fallback 是否是 residual violations 的主要来源？
2. 在 70B+ 模型上，baseline violation rate 是否显著低于 7-8B？如果是，OntoCoDec 的边际价值如何？
3. κ̄ 在 per-relation 粒度上的分布如何？是否存在某些 relation type 的 tightness 显著异于整体 schema？
4. DocRED beam search 仅在 50-doc subset 上评估——是什么阻止了全集评估？subset 的代表性如何保证？
5. 为什么没有与 GCD (Geng et al., 2023) 做直接实验对比？GCD 同样使用 grammar-constrained decoding 处理 SciERC。

---

## Missing References / 建议补充对比

- **GCD** (Geng et al., 2023, EMNLP)：已引用但未做实验对比——这是在 SciERC 上使用 grammar-constrained decoding 的最直接前序工作。
- **BoostCD** (Sakota et al., 2025, EMNLP)：已引用但未做实验对比——同样处理 IE 任务的 constrained+unconstrained decoding 混合方法。
- **CRANE** (Banerjee et al., 2025, ICML)：已引用但仅定性讨论——提供 semantic constraint reasoning 能力，与 OntoCoDec 的 semantic layer 直接可比。

---

## 主要优势

1. **Decidability taxonomy 是真正的理论贡献**：将 IE type constraints 分为三层（context-free / prefix-decidable with state / non-local）在该领域尚属首次，Proposition 1 的 pumping lemma 证明（Appendix O）严谨且有启发性，清晰地论证了为何单纯 CFG 不足以处理 domain/range 约束。
2. **Ablation 设计全面**：Table 1 的 5-way ablation + Table 10 的 4-way fine-tuned ablation + Appendix C 的 dual-factor 分析，充分隔离了各组件贡献。Table 10 的 fine-tuned 4-way ablation 特别有价值，证明 semantic layer 是唯一有效减少 DR 的组件。
3. **Fine-tuning composability 实际有用**：Table 2 证明约束与 LoRA fine-tuning 可组合（DR ≤ 0.09%, R-F1 变化不显著 p=0.31），这是实际部署的关键属性。
4. **附录极其详尽（24 页）**：case studies（Appendix J）、error analysis（Appendix D/N）、scalability benchmarks（Appendix K）、beam search 完整分析（Appendix F）、prompt templates（Appendix A）——reproducibility 极高。
5. **DR 消减效果显著**：在 favorable 条件下（LoRA + greedy S1）在 SciERC 上实现零违规（DR=0%, CF=0%），even zero-shot 也达到 94-100% DR reduction。
6. **统计实践良好**：paired bootstrap 检验（B=1000/10000），p 值报告到位，CI 宽度透明。

---

## Overall Assessment 理由

本文提出的 decidability-guided 两层约束解码框架在方法层面有真正的新意，Proposition 1 是扎实的理论贡献，ablation 和 composability 实验也较为充分。但以下关键缺陷阻碍 Conference 级别推荐：

1. 实验中完全缺失与同类 constrained decoding 方法（GCD/BoostCD/CRANE）的 head-to-head 对比，使得边际贡献无法量化——这对于一篇 framework paper 是致命短板。
2. "Guarantee" 措辞系统性高于实际提供的保证水平（fallback 机制、Level 3 未覆盖、残余 CF）。
3. WikiEvents 评估样本量不足（n=20），70B 评估过于 preliminary（1 个模型、无 ablation）。

若补充 GCD/BoostCD 对比实验并修正 overclaiming 措辞，本文有潜力达到 3.5（Borderline Conference）。当前状态建议 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1525 · 2026-05-21T01:27:01.583033+00:00_

Reviewer 1 审稿意见已收到。评分 3.0 (Findings)，主要关切：缺少竞品实验对比（GCD/BoostCD/CRANE）、"guarantee"措辞 overclaim、WikiEvents 样本量不足、70B 评估 preliminary。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1526 · 2026-05-21T01:27:10.599964+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交至 Review Director。

**审稿结论**：Overall 3.0（Findings），Confidence 4/5。

核心判断：
- **最大亮点**：Decidability taxonomy（三层分类 + Proposition 1 pumping lemma 证明）是扎实的理论贡献，ablation 设计全面，fine-tuning composability 有实际价值。
- **关键短板**：(1) 完全缺失与 GCD/BoostCD/CRANE 等同类 constrained decoding 方法的实验对比；(2) "guarantee"措辞与 fallback 机制存在系统性 overclaiming；(3) WikiEvents 样本量不足（n=20）和 70B 评估过于 preliminary。

补充 head-to-head 对比并修正 overclaiming 后有望达到 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1527 · 2026-05-21T01:27:18.001979+00:00_

Reviewer 1 审稿已收到（Overall 3.0 / Findings）。等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 111

## Round 111

6 recorded events


### User

_source line 1528 · 2026-05-21T01:29:05.627066+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**审查侧重：新颖性 + 论文完整性 + 格式合规**

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 形式化贡献（可判定性分类 + pumping lemma 证明）有理论价值，工程执行扎实，但组件级新颖性有限（grammar layer = XGrammar 直接应用，semantic layer = 运行时类型检查），且正文超出 8 页限制。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有充分实验支撑（DR reduction 94-100%），但 CF trade-off 未解决（CF 高达 12.02%），WikiEvents 结果基于 20 文档初步验证 |
| Excitement | 2.5/5 | 形式化视角有趣（IE 约束的可判定性分析在该领域属首次），但实际方法是 XGrammar + 类型查找表的组合，算法层面无突破 |
| Reproducibility | 4/5 | 超参数、prompt 模板、数据集划分、硬件配置等均有详细记录（Appendix G），代码承诺公开 |
| Overall Assessment | 3.0 | Findings 级别：执行质量高、评估全面，但新颖性偏工程集成而非方法论突破 |
| Confidence | 4/5 | 熟悉 constrained decoding 和 schema-aware IE 领域，仔细阅读了全文 34 页 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文超出 8 页限制
- 具体位置：PDF 第 9 页，行号 653-660
- 问题：Section 7 "Discussion and Conclusion" 从第 8 页底部开始，溢出至第 9 页（约 8 行文字）。LaTeX 源码在 Limitations 前使用 `\clearpage`（main.tex line 69），确认结论文本确实在第 9 页。EMNLP 2026 / ARR 规定 long paper 正文严格 ≤ 8 页。
- 为什么影响接收：ARR 明确规定 "strict 8-page limit for main text"。超页可能导致 desk reject 或 area chair 标记。
- 建议修改方向：压缩 Section 6 (Related Work) 或 Section 7 (Discussion and Conclusion)，将结论完全收进第 8 页。Related Work 已有完整版本在 Appendix B，主文可进一步精简。

**N2** [critical] 核心新颖性定位不清：系统集成 vs. 算法创新
- 具体位置：Section 1 (Introduction), Section 3 (Method)
- 问题：论文的核心贡献描述为 "a two-layer constrained decoding framework guided by a decidability analysis"（Section 1, contributions list）。但逐层拆解后：
  - **Grammar layer**（§3.2）：将 JSON Schema 编译为 pushdown automaton，直接使用 XGrammar（Dong et al., 2025）。论文明确写到 "A JSON Schema encoding Eq. (1) with enum constraints (E, R) is compiled into a pushdown automaton via XGrammar"——这是对现有工具的应用，非方法创新。
  - **Semantic layer**（§3.3）：运行时实体注册表 D + continuation masking。本质是一个有状态的类型查找表，在每个 token 位置做 domain/range 检查。概念上是 runtime type-checking 的直接实现。
  - **Proposition 1**（§3.1）：domain/range 约束不是 context-free 的 pumping lemma 证明——这是真正的理论贡献，但它更多是 *motivation* 而非 *method*。
- 论文缺少对 "what is genuinely new here beyond combining XGrammar with a type-checking registry" 的直接回应。Introduction 中的贡献列表（page 2）将 "decidability analysis" 和 "composable layers" 并列，但前者是分析结果、后者是工程集成。
- 为什么影响接收：Excitement 评分的核心考量。如果 reviewer/AC 认为贡献主要是工程集成（well-executed but incremental），则难以进入主会议。
- 建议修改方向：(1) 更清楚地分离理论贡献（decidability taxonomy, Prop 1, κ̄）和系统贡献（two-layer architecture）；(2) 直接论证为什么 semantic layer 的设计不是 trivial——例如，enabling dependency（§3.1 Corollary）意味着两层不能简单并行，composition 的正确性需要形式化保证；(3) 在 Related Work 中更明确地对比与 IterGen（Ugare et al., 2025）的 backtracking 方案，说明 OntoCoDec 的 forward-only + fallback 设计在效率和正确性上的取舍。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] DR↔CF trade-off 是结构性限制，削弱 "near-eliminates violations" 的核心声明
- 具体位置：Abstract ("near-eliminates DR (94-100% reduction)"); Table 1 (CF 列); Limitations §Constraint scope; Appendix C (§C "CF-DR Trade-off Analysis")
- 问题：Abstract 声称 "near-eliminates DR"，但 Table 1 显示在 Full S1 unconstrained 设置下，CF violations 从 0 增至 12.02%（Llama ScIERC），grammar-only CF 近零但 DR 仅减少 24%。Appendix C 的双因子分析（Figure 2）确认 DR 和 CF 反向相关（r = -0.366, p = 0.138, n=6）。论文自身承认 "CF↔DR thus represents a fundamental trade-off in composable constraint systems"（Limitations, line 74）。
- 当 CF 被考虑时，总 violation rate（DR + CF）的净减少量远小于 94-100%。例如 Table 1 SciERC Llama Full S1：DR 从 13.37→0, 但 CF 从 0→12.02, 净 violation 减少仅 ~1.35pp。
- 建议：Abstract 和 Introduction 中应同时报告 DR reduction 和 CF 增加，或使用一个综合指标（如 total violation rate）来避免选择性报告。

**W2** [major] κ̄（constraint tightness）作为理论贡献的价值有限
- 具体位置：§4.1 "Constraint Tightness"; Appendix N (κ̄ case study)
- 问题：κ̄ 定义为 κ(r) = 1 - |σ(r)|/|E|² 的平均值，即 schema 允许的类型对占所有可能类型对的比例的补数。这是一个直觉明显的度量——schema 约束越紧（允许的类型越少），violation reduction 越大。论文承认 "the dual-factor pattern motivates constrained decoding"（Appendix C, p.21），但 κ̄ 本身并未提供超出直觉的洞见。
- Appendix C 的回归分析（Figure 2, n=6）样本量太小，无法得出统计显著的结论（论文自身承认 "n=6 is insufficient for statistical inference"）。
- 建议：将 κ̄ 定位为 "diagnostic metric"（论文在 Limitations 中已部分这样做）而非独立贡献。在 contributions list 中降低 κ̄ 的权重。

**W3** [major] WikiEvents 事件抽取结果过于初步，不足以支撑 "extension to event extraction" 声明
- 具体位置：§5.4 "Extension to Event Extraction"; Table 5
- 问题：WikiEvents 评估仅覆盖 5 种 event types、27 种 entity types（论文原文 "5 event types, 80 event types, 27 entity types"——Table 5 标题说 n=246 zero-shot, n=20 fine-tuning）。Fine-tuning 仅 20 文档，论文自身称 "results are preliminary due to the 20-document test set"（§5.4）。Zero-shot 性能很低（ET/RV/DR 均有大量 violations），fine-tuning 结果虽然 RoV→0% 但样本太小。
- 更重要的是，EE 的 schema 结构（event types → argument roles → entity types）比 RE 的（entity types → relation types → entity types）更复杂，但论文对 OntoCoDec 如何处理这种层次结构的讨论不足。
- 建议：(1) 将 WikiEvents 结果明确标记为 "preliminary/pilot study"；(2) 在 Section 5.4 中更详细地讨论 EE schema 的约束编译过程和与 RE 的差异。

**W4** [minor-major] 缺少与 supervised IE baselines 的对比
- 具体位置：Tables 1-5
- 问题：论文所有实验均在 LLM-based IE pipeline 内对比（unconstrained vs. constrained），但缺少与 supervised IE 系统（如 PURE/PL-Marker、SpERT (Eberts & Ulges, 2020)）的 F1 对比。虽然 OntoCoDec 的贡献是约束层而非 IE accuracy，但读者需要知道 constrained LLM pipeline 在 F1 上处于什么水平，才能判断 violation reduction 的实际价值。
- 论文在 Appendix C 提到 "supervised state-of-the-art systems on SciERC achieve approximately 49-53% relation F1 with full training data (Zhong and Chen, 2021)"，但这是附录中的一句带过，未进入主文比较。
- 建议：在 Table 1 或 Table 2 中加一行 supervised baseline 的 F1 作为 oracle/upper-bound 参考。

---

## 小问题（不影响接收）

- **m1** [minor] 两个 orphan bib entries（chen2024agentre, fan2024fsn）未被引用，应清理。
- **m2** [minor] Abstract 中 "1-2% even after LoRA fine-tuning" 与 Table 2 中 fine-tuned DR 数据（LoRA + S1: DR ≤ 0.09% on SciERC, ≤ 0.28% on DocRED）不完全一致。Abstract 的 "1-2%" 似乎指 unconstrained fine-tuning 的残余 violation rate，但表述容易误解为 constrained 后的残余。
- **m3** [minor] Figure 1 的 overview 图过于抽象，难以传达两层架构的具体交互机制。建议增加一个 running example 的 figure，展示 grammar mask 和 semantic mask 在具体 token 位置如何交互。
- **m4** [minor] Appendix O (pumping lemma proof) 跨 3 页（pp.32-34），对于一个相对直接的不可判定性证明来说偏长，部分辅助引理可压缩。
- **m5** [minor] 引用格式：部分 arXiv preprint（如 formattax2026, dccd2026）在 OpenAlex 中未能验证——应确认这些论文确实存在且引用信息准确。

---

## Questions to Authors

1. **Entity registry 与共指消解**：当同一实体在文档中以不同表面形式出现时（如 "Barack Obama" 和 "Obama"），entity registry D 是否将它们视为同一实体？如果是，如何确定共指？如果否，是否会导致同一实体被赋予不同类型？
2. **Grammar-first fallback 的级联效应**：当 §4 中的 grammar-first fallback（S(t)∩G(t)=∅ 时跳过 semantic layer）触发时，被分配的类型可能违反 domain/range 约束。这些 fallback-induced CF violations 在后续 triple 的类型约束中是否会级联传播？
3. **与 IterGen 的 backtracking 方案的实验对比**：论文在 Related Work 中讨论了 IterGen（Ugare et al., 2025），但未进行实验对比。是否有技术障碍阻止了这一对比？IterGen 的 backtracking 是否可以作为 OntoCoDec 的替代 semantic enforcement 策略？

---

## Missing References

- **ASP/Markov Logic for structured IE constraints**: Riedel et al. (2009) "Markov Logic Networks for Information Extraction" 和相关 probabilistic constraint enforcement 工作。OntoCoDec 的 hard constraint approach 与 soft constraint approaches 的对比讨论缺失。
- **Constrained beam search in NLG**: Anderson et al. (2017) "Guided Open Vocabulary Image Captioning with Constrained Beam Search" — 早期将约束融入 beam search 的工作，与 OntoCoDec 的 beam search compatibility (Appendix F) 相关。
- **Type-constrained link prediction in KGE**: Krompaß et al. (2015) "Type-Constrained Representation Learning in Knowledge Graphs" — KG embedding 中的类型约束方法，虽然领域不同但概念相关。

---

## 主要优势

1. **形式化分析有深度**：将 IE 类型约束映射到形式语言理论（Proposition 1 的 pumping lemma 证明）是该领域的首次尝试，提供了理论 grounding 来解释为什么 grammar-only constrained decoding 不足以处理 domain/range 约束。
2. **实验评估极为全面**：3 个数据集 × 4 个模型 × 多种解码策略 × zero-shot + fine-tuning × 大量消融实验（5-way ablation, per-relation analysis, document length breakdown, prompt sensitivity, sampling robustness, beam search compatibility, scalability）。附录从 A 到 O，覆盖了几乎所有可预见的 reviewer 问题。
3. **诚实的 Limitations 讨论**：CF trade-off、WikiEvents 初步性、模型依赖性、工程约束（API-only models 不适用）等均有坦诚讨论，这在投稿论文中并不常见。
4. **Reproducibility 准备充分**：Prompt 模板（Appendix A）、超参数（Appendix G）、随机种子验证（Table 20）、硬件规格均有记录。
5. **Cross-dataset generalization**：在 SciERC（学术）、DocRED（Wikipedia）、WikiEvents（新闻事件）三种不同领域验证，展示了方法的通用性。

---

## 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 页数 ≤ 8 | ❌ | 正文溢出至第 9 页（8 行结论文字）|
| 匿名 | ✅ | `\author{Anonymous ACL submission}`，无可识别自引 |
| ACL 模板 + [review] | ✅ | `\usepackage[review]{acl}`（main.tex line 3）|
| Limitations section | ✅ | 独立 section，在 conclusion 后、references 前（main.tex lines 70-94）|
| Ethics Statement | ✅ | 存在（main.tex lines 98-103）|
| ARR Checklist | ✅ | 已填写（main.tex line 106, pages 11-12）|
| 附录双栏 | ✅ | 所有附录页面（15-34）均为双栏格式 |
| natbib 引用 | ✅ | 通过 acl package 使用 natbib |
| 引用完整性 | ✅ | 58/60 bib entries 被引用，0 missing bib，48/60 online verified |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1529 · 2026-05-21T01:29:55.942319+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n### 总体评分\nOverall: 3.0 / 5（Findings），Confidence: 4 / 5\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | Decidability 分析和证明基本严谨，但\"guarantee\"措辞与 fallback 机制存在内在矛盾；κ̄ 分析数据点不足（n=6）|\n| Excitement | 3.0 / 5 | Decidability-guided 设计在 IE constrained decoding 中有新意，但缺乏 baseline 对比难以评估边际贡献 |\n| Reproducibility | 4.0 / 5 | 附录详尽，声称开源 |\n| Clarity | 3.5 / 5 | 结构清晰但信息密度极高，enabling dependency 主文解释不充分 |\n\n### Must-Fix 问题\n\n**N1** [critical] 缺少与 constrained-decoding 竞争方法的实验对比\n- 论文在 Related Work 中详细讨论了 BoostCD、CRANE、IterGen、GCD、EnriCo，但实验中唯一对比是 unconstrained decoding 和 post-hoc filtering。\n- 尤其 BoostCD 和 GCD 同样基于 grammar-constrained decoding 处理 IE 任务，且在 SciERC 上有结果。\n- 建议至少在 SciERC 上与 GCD 和 BoostCD 做 head-to-head 对比（R-F1、DR、CF、latency）。\n\n**N2** [critical] \"Guarantee\" 措辞与实际机制不匹配\n- Abstract (\"formal guarantees at each layer\")、Section 1 (\"formal guarantees\") 与 Section 3.3 (\"best-effort pair-based enforcement\")、Section 3.4 (\"grammar-first fallback\") 存在矛盾。\n- 三个保证缺口：(a) grammar-first fallback 时 semantic layer 被跳过；(b) Level 3 constraints 未强制；(c) 残余 CF 0.08-0.35%。\n- 建议将\"guarantee\"替换为\"enforcement\"或\"near-elimination\"。\n\n**N3** [major] WikiEvents 评估统计效能不足\n- Fine-tuning 仅 20 篇文档（n=20），结论基于此的 bootstrap CI 可信度有限。\n- 建议明确标记为\"indicative only\"或在完整测试集上报告。\n\n**N4** [major] 70B 评估不足以支撑广泛声称\n- 完整评估仅覆盖 7-8B 模型，70B 仅 1 个模型、无 ablation、无 fine-tuning。\n- Abstract \"applicable to autoregressive LMs\" 过宽。\n\n### Should-Fix 问题\n\n**W1** [warning] κ̄ 基于 n=6 数据点的关联分析\n- Figure 2 仅 4 个 model-dataset 组合。论文承认 p>0.05，但 §1 仍列为主要贡献。\n\n**W2** [warning] Fallback 机制与核心 claim 的张力未充分分析\n- 未分析 residual DR violations 中有多少源自 fallback 事件。\n- 建议追踪 residual violations 到 fallback vs non-fallback positions。\n\n**W3** [warning] S1 vs S2 配置选择缺乏充分论证\n- S2 R-F1 略高但 CF 更差，cost-benefit 分析缺失。\n\n**W4** [warning] 仅英语数据集评估\n- 跨语言泛化是开放问题。Limitations 未明确标注语言覆盖缺口。\n\n**W5** [warning] Post-hoc filtering 对比可能不够公平\n- post-hoc correction（替换而非丢弃）可能是更公平的 baseline。\n\n### 小问题\n- 页数溢出（~8行结论在第9页）\n- Table 1 \"Tgt.\" 列含义不直观\n- Enabling dependency 概念在主文中未正式定义\n- Figure 1 信息密度高，visual hierarchy 不够清晰\n- Orphan bib entries（chen2024agentre, fan2024fsn）\n- 引用格式 encoding mismatch\n\n### 主要优势\n1. Decidability taxonomy 是真正的理论贡献\n2. Ablation 设计全面（5-way + 4-way fine-tuned）\n3. Fine-tuning composability 有实际价值\n4. 附录极其详尽（24页）\n5. DR 消减效果显著\n6. 统计实践良好\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n### 总体评分\nOverall: 3.0 / 5（Findings），Confidence: 4 / 5\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | Decidability 分析和证明基本严谨，但\"guarantee\"措辞与 fallback 机制存在内在矛盾；κ̄ 分析数据点不足（n=6）|\n| Excitement | 3.0 / 5 | Decidability-guided 设计在 IE constrained decoding 中有新意，但缺乏 baseline 对比难以评估边际贡献 |\n| Reproducibility | 4.0 / 5 | 附录详尽，声称开源 |\n| Clarity | 3.5 / 5 | 结构清晰但信息密度极高，enabling dependency 主文解释不充分 |\n\n### Must-Fix 问题\n\n**N1** [critical] 缺少与 constrained-decoding 竞争方法的实验对比\n- 论文在 Related Work 中详细讨论了 BoostCD、CRANE、IterGen、GCD、EnriCo，但实验中唯一对比是 unconstrained decoding 和 post-hoc filtering。\n- 尤其 BoostCD 和 GCD 同样基于 grammar-constrained decoding 处理 IE 任务，且在 SciERC 上有结果。\n- 建议至少在 SciERC 上与 GCD 和 BoostCD 做 head-to-head 对比（R-F1、DR、CF、latency）。\n\n**N2** [critical] \"Guarantee\" 措辞与实际机制不匹配\n- Abstract (\"formal guarantees at each layer\")、Section 1 (\"formal guarantees\") 与 Section 3.3 (\"best-effort pair-based enforcement\")、Section 3.4 (\"grammar-first fallback\") 存在矛盾。\n- 三个保证缺口：(a) grammar-first fallback 时 semantic layer 被跳过；(b) Level 3 constraints 未强制；(c) 残余 CF 0.08-0.35%。\n- 建议将\"guarantee\"替换为\"enforcement\"或\"near-elimination\"。\n\n**N3** [major] WikiEvents 评估统计效能不足\n- Fine-tuning 仅 20 篇文档（n=20），结论基于此的 bootstrap CI 可信度有限。\n- 建议明确标记为\"indicative only\"或在完整测试集上报告。\n\n**N4** [major] 70B 评估不足以支撑广泛声称\n- 完整评估仅覆盖 7-8B 模型，70B 仅 1 个模型、无 ablation、无 fine-tuning。\n- Abstract \"applicable to autoregressive LMs\" 过宽。\n\n### Should-Fix 问题\n\n**W1** [warning] κ̄ 基于 n=6 数据点的关联分析\n- Figure 2 仅 4 个 model-dataset 组合。论文承认 p>0.05，但 §1 仍列为主要贡献。\n\n**W2** [warning] Fallback 机制与核心 claim 的张力未充分分析\n- 未分析 residual DR violations 中有多少源自 fallback 事件。\n- 建议追踪 residual violations 到 fallback vs non-fallback positions。\n\n**W3** [warning] S1 vs S2 配置选择缺乏充分论证\n- S2 R-F1 略高但 CF 更差，cost-benefit 分析缺失。\n\n**W4** [warning] 仅英语数据集评估\n- 跨语言泛化是开放问题。Limitations 未明确标注语言覆盖缺口。\n\n**W5** [warning] Post-hoc filtering 对比可能不够公平\n- post-hoc correction（替换而非丢弃）可能是更公平的 baseline。\n\n### 小问题\n- 页数溢出（~8行结论在第9页）\n- Table 1 \"Tgt.\" 列含义不直观\n- Enabling dependency 概念在主文中未正式定义\n- Figure 1 信息密度高，visual hierarchy 不够清晰\n- Orphan bib entries（chen2024agentre, fan2024fsn）\n- 引用格式 encoding mismatch\n\n### 主要优势\n1. Decidability taxonomy 是真正的理论贡献\n2. Ablation 设计全面（5-way + 4-way fine-tuned）\n3. Fine-tuning composability 有实际价值\n4. 附录极其详尽（24页）\n5. DR 消减效果显著\n6. 统计实践良好\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1530 · 2026-05-21T01:30:25.082317+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29139
}
```

</details>

---


### Tool call

_source line 1531 · 2026-05-21T01:30:25.636324+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n### 总体评分\nOverall: 3.0 (Findings)，Confidence: 4/5\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | DR reduction 94-100% 有充分支撑，但 CF trade-off 未解决，WikiEvents 基于 20 文档 |\n| Excitement | 2.5/5 | 形式化视角有趣，但实际方法是 XGrammar + 类型查找表的组合，算法层面无突破 |\n| Reproducibility | 4/5 | 详细记录，代码承诺公开 |\n| Overall Assessment | 3.0 | Findings 级别：执行质量高但新颖性偏工程集成 |\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超出 8 页限制\n- Section 7 溢出至第 9 页（约 8 行文字）。\n- ARR 规定 \"strict 8-page limit\"，可能导致 desk reject。\n\n**N2** [critical] 核心新颖性定位不清：系统集成 vs. 算法创新\n- Grammar layer = XGrammar 直接应用，Semantic layer = 运行时类型检查的直接实现。\n- Proposition 1 是真正的理论贡献，但更多是 motivation 而非 method。\n- 论文缺少对 \"what is genuinely new beyond combining XGrammar with a type-checking registry\" 的直接回应。\n\n### Should-Fix 问题\n\n**W1** [major] DR↔CF trade-off 是结构性限制，削弱 \"near-eliminates violations\" 声明\n- Table 1 SciERC Llama Full S1：DR 13.37→0, CF 0→12.02, 净 violation 减少仅 ~1.35pp。\n- 建议同时报告 DR reduction 和 CF 增加，或使用综合指标。\n\n**W2** [major] κ̄ 作为理论贡献的价值有限\n- 定义直觉明显（schema 越紧约束效果越好），n=6 无法统计推断。\n- 建议定位为 diagnostic metric 而非独立贡献。\n\n**W3** [major] WikiEvents 结果过于初步\n- Fine-tuning 仅 20 文档，EE 的 schema 结构比 RE 更复杂但讨论不足。\n- 建议明确标记为 preliminary/pilot study。\n\n**W4** [minor-major] 缺少与 supervised IE baselines 的 F1 对比\n- 缺少 PURE/PL-Marker/SpERT 等 F1 作为 oracle/upper-bound 参考。\n\n### 格式合规检查\n| 检查项 | 结果 |\n|--------|------|\n| 页数 ≤ 8 | ❌ 溢出至第 9 页 |\n| 匿名 | ✅ |\n| ACL 模板 + [review] | ✅ |\n| Limitations section | ✅ |\n| Ethics Statement | ✅ |\n| ARR Checklist | ✅ |\n| 附录双栏 | ✅ |\n| natbib 引用 | ✅ |\n\n### 小问题\n- Orphan bib entries（chen2024agentre, fan2024fsn）\n- Abstract \"1-2% even after LoRA fine-tuning\" 与 Table 2 数据不完全一致\n- Figure 1 过于抽象\n- Appendix O 偏长\n- 部分 arXiv preprint 引用未能验证\n\n### 主要优势\n1. 形式化分析有深度\n2. 实验评估极为全面\n3. 诚实的 Limitations 讨论\n4. Reproducibility 准备充分\n5. Cross-dataset generalization\n\n### Missing References\n- Riedel et al. (2009) Markov Logic Networks for IE\n- Anderson et al. (2017) Constrained Beam Search\n- Krompaß et al. (2015) Type-Constrained KGE\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。特别关注：\n1. R2-N1（页数超限）的严重程度判定\n2. R2-N2（新颖性定位）——你是否同意新颖性主要在系统集成层面？\n3. R2-W1（CF trade-off）——你的 N2 关于 guarantee 措辞与此是否有重叠？如何统一评判？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n### 总体评分\nOverall: 3.0 (Findings)，Confidence: 4/5\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | DR reduction 94-100% 有充分支撑，但 CF trade-off 未解决，WikiEvents 基于 20 文档 |\n| Excitement | 2.5/5 | 形式化视角有趣，但实际方法是 XGrammar + 类型查找表的组合，算法层面无突破 |\n| Reproducibility | 4/5 | 详细记录，代码承诺公开 |\n| Overall Assessment | 3.0 | Findings 级别：执行质量高但新颖性偏工程集成 |\n\n### Must-Fix 问题\n\n**N1** [critical] 正文超出 8 页限制\n- Section 7 溢出至第 9 页（约 8 行文字）。\n- ARR 规定 \"strict 8-page limit\"，可能导致 desk reject。\n\n**N2** [critical] 核心新颖性定位不清：系统集成 vs. 算法创新\n- Grammar layer = XGrammar 直接应用，Semantic layer = 运行时类型检查的直接实现。\n- Proposition 1 是真正的理论贡献，但更多是 motivation 而非 method。\n- 论文缺少对 \"what is genuinely new beyond combining XGrammar with a type-checking registry\" 的直接回应。\n\n### Should-Fix 问题\n\n**W1** [major] DR↔CF trade-off 是结构性限制，削弱 \"near-eliminates violations\" 声明\n- Table 1 SciERC Llama Full S1：DR 13.37→0, CF 0→12.02, 净 violation 减少仅 ~1.35pp。\n- 建议同时报告 DR reduction 和 CF 增加，或使用综合指标。\n\n**W2** [major] κ̄ 作为理论贡献的价值有限\n- 定义直觉明显（schema 越紧约束效果越好），n=6 无法统计推断。\n- 建议定位为 diagnostic metric 而非独立贡献。\n\n**W3** [major] WikiEvents 结果过于初步\n- Fine-tuning 仅 20 文档，EE 的 schema 结构比 RE 更复杂但讨论不足。\n- 建议明确标记为 preliminary/pilot study。\n\n**W4** [minor-major] 缺少与 supervised IE baselines 的 F1 对比\n- 缺少 PURE/PL-Marker/SpERT 等 F1 作为 oracle/upper-bound 参考。\n\n### 格式合规检查\n| 检查项 | 结果 |\n|--------|------|\n| 页数 ≤ 8 | ❌ 溢出至第 9 页 |\n| 匿名 | ✅ |\n| ACL 模板 + [review] | ✅ |\n| Limitations section | ✅ |\n| Ethics Statement | ✅ |\n| ARR Checklist | ✅ |\n| 附录双栏 | ✅ |\n| natbib 引用 | ✅ |\n\n### 小问题\n- Orphan bib entries（chen2024agentre, fan2024fsn）\n- Abstract \"1-2% even after LoRA fine-tuning\" 与 Table 2 数据不完全一致\n- Figure 1 过于抽象\n- Appendix O 偏长\n- 部分 arXiv preprint 引用未能验证\n\n### 主要优势\n1. 形式化分析有深度\n2. 实验评估极为全面\n3. 诚实的 Limitations 讨论\n4. Reproducibility 准备充分\n5. Cross-dataset generalization\n\n### Missing References\n- Riedel et al. (2009) Markov Logic Networks for IE\n- Anderson et al. (2017) Constrained Beam Search\n- Krompaß et al. (2015) Type-Constrained KGE\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。特别关注：\n1. R2-N1（页数超限）的严重程度判定\n2. R2-N2（新颖性定位）——你是否同意新颖性主要在系统集成层面？\n3. R2-W1（CF trade-off）——你的 N2 关于 guarantee 措辞与此是否有重叠？如何统一评判？"
  }
}
```

</details>

---


### Tool result

_source line 1532 · 2026-05-21T01:30:27.204893+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1568
}
```

</details>

---


### Assistant

_source line 1533 · 2026-05-21T01:30:30.103477+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1534 · 2026-05-21T01:30:32.855211+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)。主要发现：

1. **格式违规 [critical]**：正文溢出至第 9 页（8 行结论文字），违反 EMNLP 2026 严格 8 页限制
2. **新颖性定位不清 [critical]**：组件级创新有限（grammar layer = XGrammar 应用，semantic layer = 运行时类型检查），系统集成 vs. 算法创新的界限模糊
3. **DR↔CF trade-off [major]**：约束强制减少 DR 但引入 CF（高达 12.02%），Abstract 的 "near-eliminates" 声明有选择性报告之嫌
4. **κ̄ 贡献有限 [major]**：定义直觉明显，回归分析样本量不足（n=6）
5. **WikiEvents 初步 [major]**：仅 20 文档 fine-tuning 评估

**优势**：形式化分析（Proposition 1 pumping lemma）有真正理论贡献；实验评估极全面（34 页含 15 个附录）；Limitations 讨论诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1535 · 2026-05-21T01:30:39.340757+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1536 · 2026-05-21T01:32:51.567071+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### R2-N1 [critical] 正文超出 8 页限制

**[AGREE] R2-N1**: 同意这是一个需要修复的格式问题。我在自己的审稿中也在小问题部分标注了此项——Section 7 约 8 行溢出至第 9 页。

但在**严重程度**上，我的判定与 R2 不同。R2 称"可能导致 desk reject"，我认为这过度了。ARR 实际操作中，Program Chairs 的 desk reject 标准主要针对显著超页（如 9 页满文或更多），而非尾部 8 行溢出。实际上大量 ARR 投稿在 Conclusion 最后几行有类似的微小溢出而未被 desk reject。

**结论**：应修复（压缩 Section 7 回到第 8 页即可），但不应升至 critical——建议降级为 minor-major。这是一个 5 分钟就能解决的排版问题，不反映论文的学术质量。

---

### R2-N2 [critical] 核心新颖性定位不清：系统集成 vs. 算法创新

**[AGREE in part, REBUT in part] R2-N2**:

**同意的部分**：R2 指出 grammar layer 是 XGrammar 直接应用、semantic layer 是运行时类型检查的直接实现——这个观察基本准确。论文确实未充分回答"beyond combining XGrammar with a type-checking registry, what is genuinely new?"这个问题。如果 reviewer 带着"算法创新"的期待来读这篇论文，会感到失望。

**反驳的部分**：R2 给 Excitement 2.5/5 并称"算法层面无突破"，我认为这低估了以下贡献：

1. **Proposition 1（Appendix O, p32-33）不仅是 motivation**。它建立了一个在 IE constrained decoding 领域此前不存在的理论 lower bound：证明 domain/range type constraints 不能被 context-free grammar 表达。这个结论直接决定了任何试图仅用 CFG（如 XGrammar/Outlines/SGLang 单独使用）来强制 IE type constraints 的方案都是 inherently incomplete。这是一个具有独立价值的理论结果，而非仅为方法设计提供 motivation。

2. **Enabling dependency formalization（§3.4, Corollary 1）**虽然主文表述不充分（我也在小问题中标注了），但其内涵非平凡：semantic layer 必须在 grammar layer guarantee vocabulary membership 之后才能工作。这排除了某些看似合理的替代架构（如 semantic-first 或两层独立并行）。

3. **Fine-tuning composability 的经验证明（Table 2, Table 10）**是一个实质性的 empirical contribution——prior work（如 GCD, BoostCD）均未系统验证 constrained decoding 与 fine-tuning 的交互。

**统一判定**：我同意论文的 novelty 主要在 **formalization + informed system design** 而非 algorithmic breakthrough。这对 Excitement 评分有影响（我给 3.0 vs R2 给 2.5），但不应升至 critical——应为 major。建议论文在 Introduction 中更显式地声明："Our contribution is not a new decoding algorithm, but a formal analysis that reveals the necessity of a two-layer design, together with a principled instantiation and comprehensive evaluation."

---

### R2-W1 [major] DR↔CF trade-off 削弱 "near-eliminates violations" 声明

**[AGREE] R2-W1**: 这是一个我未充分标注的重要问题。R2 的数据检查很犀利：

Table 1 SciERC Llama Full S1 数据：
- DR: 13.37% → ~0%（消除）
- CF: ~0% → 12.02%（引入）
- 净违规减少仅 ~1.35pp

这意味着 semantic layer 在 Llama 上将 DR violations 大量转化为 CF violations（cross-field inconsistency），而非真正消除。论文在 Limitations（p10）承认了"CF impact is model-dependent"并特别提到 12.02% 的数字，但主文的叙事重心完全在 DR reduction 上，未给予 CF trade-off 足够的 visibility。

**与我的 N2 的关系**：R2-W1 和我的 N2 互补但不重叠：
- **我的 N2** 聚焦于 fallback 机制导致 semantic layer 被绕过——即 constraint system 未能执行的情况
- **R2-W1** 聚焦于 semantic layer 正常工作但引入新类型违规（CF）——即 constraint system 按设计运行但产生副作用的情况

两者共同说明：constraint enforcement 的实际效果显著弱于 headline DR 数字所暗示。建议论文：
1. 在 Table 1 旁增加 "net violation change"（ΔDR + ΔCF）作为综合指标
2. 在 Abstract/Introduction 中将 DR reduction 与 CF introduction 并列报告
3. 将"near-eliminates violations"修改为更精确的"near-eliminates domain/range violations, with a model-dependent cross-field trade-off"

**补充一个 R2 未提及的重要 nuance**：CF trade-off 是 model-dependent——Qwen 的 CF 增幅远低于 Llama（Table 1 显示 Qwen Full S1 CF=0.035% vs Llama 12.02%）。这说明 well-calibrated models 几乎不受此 trade-off 影响，但 poorly-calibrated models（如 Llama on SciERC）的净收益极为有限。论文应在 Section 5.1 中更显式地讨论这一 model-dependent 模式。

---

### R2-W2 [major] κ̄ 作为理论贡献的价值有限

**[AGREE] R2-W2**: 与我的 W1 完全一致。κ̄ 的定义直觉上显然（tighter schema → more constraint impact），n=6 无法做统计推断。论文在 Appendix C（p21）已诚实承认 p>0.05，但 §1 仍将其列为三大贡献之一。

我同意 R2 的建议：将 κ̄ 从 "independent contribution" 降级为 "diagnostic metric introduced for deployment guidance"。具体而言，§1 的 contribution list 应将 κ̄ 合并到实验评估的子点中，而非单独列出。

---

### R2-W3 [major] WikiEvents 结果过于初步

**[AGREE] R2-W3**: 与我的 N3 一致。我在 N3 中将此标为 major 而非 critical，理由是 WikiEvents 是论文三个数据集中的第三个（SciERC 和 DocRED 的评估相对充分），且论文确实标注了"preliminary"。

R2 额外提出了一个有价值的观点：EE（event extraction）的 schema 结构比 RE 更复杂（嵌套 argument roles、event types 的层次结构），但论文未充分讨论这种复杂性对 constraint effectiveness 的影响。我同意这一点——Section 5.4 应增加对 EE schema 特殊性的讨论（如 KAIROS ontology 的 argument role 约束层次如何映射到 grammar/semantic layers）。

---

### R2-W4 [minor-major] 缺少与 supervised IE baselines 的 F1 对比

**[REBUT] R2-W4**: 我不同意这是一个重要缺陷。

OntoCoDec 的 positioning 是**decoding-time constraint enforcement**，不是 IE system——它不改变模型参数，不做 training，目标是减少 violations 而非提升 F1。与 PURE/PL-Marker/SpERT 对比 F1 会造成误导性对比（category error）：这些是 supervised fine-tuned 系统在特定数据集上的 F1 上界，而 OntoCoDec 是在 zero-shot/few-shot LLM 输出上添加约束的后处理层。

论文在 Limitations（p10）中正确地指出 "Relation F1 remains around +1-4%... compared to ~45% for fine-tuned systems"——这已经提供了 gap context。

我认为真正缺失的对比（如我的 N1 所述）是与**同类 constrained decoding 方法**（GCD/BoostCD）的 head-to-head，而非与 supervised systems 的 F1 对比。

---

### R2 小问题回应

**Abstract "1-2%" 与 Table 2 不一致**：
**[AGREE]** 值得检查。Abstract 称 "1–2% even after LoRA fine-tuning"，应指 unconstrained fine-tuned models 的 residual DR。Table 2 显示 SciERC LoRA unconstrained DR 可能偏离此范围（具体取决于模型），论文应核实并精确化此数字。

**Figure 1 过于抽象**：
**[AGREE]** 我也标注了 Figure 1 visual hierarchy 不清晰。

**Appendix O 偏长**：
**[REBUT]** Proposition 1 的 pumping lemma 证明需要完整的形式化论证（string construction、case analysis、contradiction derivation），这是保证证明严谨性的必要长度。缩短会损害 soundness。

**Orphan bib entries**：
**[AGREE]** 与我的审查一致——chen2024agentre 和 fan2024fsn 应清理。

---

### R2 Missing References 回应

- **Riedel et al. (2009) MLN for IE**: [AGREE] 这是 constraint-based IE 的重要历史工作，应在 Appendix B Extended Related Work 中引用。
- **Anderson et al. (2017) Constrained Beam Search**: [AGREE] 与 §5.3 beam search 讨论直接相关，应引用。
- **Krompaß et al. (2015) Type-Constrained KGE**: [REBUT] 这与 KG embedding 的类型约束相关，与 decoding-time constraint enforcement 在方法层面差异过大，引用价值有限。

---

### 总结：与 R2 的共识和分歧

**共识领域**（影响评分方向一致）：
1. WikiEvents underpowered（R2-W3 = 我的 N3）
2. κ̄ 贡献定位过高（R2-W2 = 我的 W1）
3. "Guarantee"/violation 声称需要 tempering（R2-W1 补充了我的 N2）
4. 格式问题需修复（R2-N1 = 我的小问题）

**分歧领域**：
1. **Novelty（R2-N2）**：R2 给 Excitement 2.5 认为"工程集成无突破"；我给 3.0 认为 decidability analysis + composability 证明有足够的学术贡献。我认为 R2 在此偏严——Proposition 1 作为理论贡献具有独立价值。
2. **Supervised baseline 对比（R2-W4）**：我认为这是 category error，真正缺失的是同类 constrained decoding 方法的对比。
3. **页数超限严重性（R2-N1）**：R2 列为 critical，我认为 minor-major——8 行溢出不构成 desk reject 风险。

**两位 Reviewer 均未提出但我认为重要的问题**：
- 缺少与 GCD/BoostCD/CRANE 的 head-to-head 实验对比（我的 N1）——这是我认为本文最关键的缺陷，R2 未独立提出此点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1537 · 2026-05-21T01:32:58.395970+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 114

## Round 114

12 recorded events


### User

_source line 1538 · 2026-05-21T01:33:04.835500+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。关键判定：

- R2 的 7 个问题中，我 **AGREE** 5 个（N1 降级严重性、W1-W3、部分小问题），**REBUT** 2 个（W4 supervised baseline 对比是 category error；Appendix O 长度是必要的）
- 对 R2-N2（novelty），**部分同意**（实现层面确为工程集成）**部分反驳**（Proposition 1 有独立理论价值，R2 Excitement 2.5 偏严）
- R2-W1（DR↔CF trade-off）是 R2 最有价值的独立发现，补充了我的 N2——两者共同说明 constraint enforcement 实际效果弱于 headline 数字
- 强调了我的 N1（缺少 GCD/BoostCD 实验对比）是 R2 未独立提出的关键问题

---

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 缺少与 constrained-decoding 竞争方法的实验对比**

同意这是论文最显著的实验缺陷。论文 Related Work（Section 6, p.8）详细讨论了 GCD、BoostCD、IterGen、EnriCo，但实验中唯一 baseline 是 unconstrained vs. OntoCoDec 的内部消融（Table 1 五路消融）和 post-hoc filtering（§5.1 最后一段）。

需要补充一点：直接对比存在技术复杂性。GCD（Geng et al., 2023）使用 grammar-constrained decoding 但不处理 domain/range 约束——它在 OntoCoDec 的 decidability taxonomy 中属于 Level 1-2（§3.1），而 OntoCoDec 的核心贡献是 Level 2 的 semantic layer。因此 GCD 的 grammar-only 结果本质上就是论文 Table 1 中 "Grammar" 行（grammar-only ablation）。论文在 §5.1 提到 "grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)" —— 这隐含了 GCD 对比，但应当显式化。

BoostCD 的情况更棘手：它 boost constrained + unconstrained 分布，其 DR 减少机制与 OntoCoDec 完全不同。但既然论文声称 OntoCoDec "超越"这些方法，至少应提供 SciERC 上的 head-to-head 数字。

**[AGREE] R1-N2: "Guarantee" 措辞与实际机制不匹配**

完全同意。我在自己的审稿中也注意到了这一矛盾（我的 N2 关于新颖性定位）。具体证据：

- Abstract (p.1): "formal guarantees at each layer" 
- Section 2 (p.2): "formal enforcement with formal guarantees at each level"
- 但 Section 4 (p.4): "grammar-first fallback" 在 S(t)∩G(t)=∅ 时跳过 semantic layer，此时类型约束不被强制
- Section 3.3 (p.3): semantic layer 使用 "best-effort pair-based enforcement"
- Table 1 (p.6): Fine-tuned Full S1 仍有残余 CF 0.08-9.90%

"Guarantee" 一词暗示零 residual violations，但数据显示这并非如此。R1 建议改为 "enforcement" 或 "near-elimination" 是合理的。论文在 Limitations（p.10）中诚实地讨论了这些缺口，但 Abstract/Introduction 的措辞应与 Limitations 保持一致。

**[AGREE] R1-N3: WikiEvents 评估统计效能不足**

完全同意，这与我自己的 W3 一致。Fine-tuning 仅 20 文档（§5.4, p.7: "results are preliminary due to the 20-document test set"），论文自身已承认。补充一个 R1 未提到的细节：WikiEvents zero-shot 评估（Table 5, n=246）规模尚可，但 fine-tuning composability 验证（n=20）确实不足以得出可靠结论。建议至少在正文中标注 "preliminary/pilot" 以管理读者预期。

**[REBUT] R1-N4: 70B 评估不足以支撑广泛声称**

部分不同意 R1 将此列为 Must-Fix。

理由：(1) Abstract 的表述是 "applicable to autoregressive LMs with logits access"（p.1），这是对方法适用范围的事实性声明（只要有 logit access 就能用），不是性能保证。OntoCoDec 的约束编译是模型无关的——grammar layer 通过 XGrammar 在 token 层面操作，semantic layer 通过 entity registry 跟踪已生成内容。两层均不依赖模型参数或架构细节。

(2) 论文确实提供了 70B 结果（Table 4, p.7: Llama-3.1-70B 在 SciERC 和 DocRED 上的 zero-shot 评估），虽然没有 fine-tuning ablation，但显示了相同的 DR 消减模式。Table 4 显示 Llama-3.1-70B 在 SciERC 上 DR 从 56.97→1.50（grammar）→0（Full S1），在 DocRED 上 DR 30.77→16.03→0.17。约束机制在 70B 上的有效性是可验证的。

(3) 更重要的 gap 是 Mistral 在 Table 4 中的表现差异（SciERC 零 violations 但 DocRED zero-shot 后 CF 很高），这表明 model calibration 而非 model scale 是关键变量——论文在 §5.3 和 Limitations 中充分讨论了这一点。

建议：将 N4 降为 Should-Fix。可以在 Limitations 中加一句明确承认 70B scale 验证有限，但不需要改 Abstract 的适用范围声明。

---

### Should-Fix 问题

**[AGREE] R1-W1: κ̄ 基于 n=6 数据点的关联分析**

完全同意，与我的 W2 一致。论文自身在 Appendix C (p.21) 承认 "n=6 is insufficient for statistical inference on this correlation"。n=6 的回归分析（Figure 2）不能支撑因果或强相关性结论。κ̄ 应被定位为 diagnostic metric 而非独立理论贡献。

**[AGREE] R1-W2: Fallback 机制与核心 claim 的张力未充分分析**

同意。这是一个我在第一轮审稿中未充分关注的有价值观察。论文在 Appendix C (p.19-20) 讨论了 CF dual mechanisms（"Grammar-first fallback" 和 "Grammar-first"），也在 Limitations (p.10, §Constraint scope) 讨论了 CF↔DR trade-off，但缺少的关键分析是：**residual DR violations（如 Table 10 中 fine-tuned 设置下的 36 个残余 violations）有多少发生在 fallback 位置**。

Appendix D (p.25, Table 13) 提供了 per-relation violation breakdown，但按 violation type（entity type error, schema coverage gap 等）分类，不是按 fallback vs non-fallback 位置分类。追踪 fallback 事件与 residual violations 的关联性将直接回答 "fallback 是否是 residual DR 的主要来源" 这一问题。

**[REBUT] R1-W3: S1 vs S2 配置选择缺乏充分论证**

部分不同意。论文在 §5.1 (p.5) 提供了明确的比较："S1 vs S2. S2 achieves comparable DR (0.97%) but lower R-F1 (8.03 vs. 8.36) without resolving CF (8.03% vs. 9.90%); we adopt S1." 这给出了三个维度（DR, R-F1, CF）的对比，结论清晰：S1 在 R-F1 和 CF 上均优于 S2，DR 可比。

不过，R1 要求更深入的 cost-benefit 分析也有道理——尤其是 S2 的两阶段 pipeline（§3.4: "A first pass extracts entities; these compile an input-dependent grammar for the second pass"）在特定场景（如 entity types 非常多时）可能有优势。这属于 minor improvement 而非 must-fix。

**[AGREE] R1-W4: 仅英语数据集评估**

同意。论文 Limitations section (p.10) 在 "Engineering considerations" 段讨论了 tokenizer 依赖性和 API-only 模型限制，但未明确提及语言覆盖缺口。SciERC（英语学术文本）、DocRED（英语 Wikipedia）、WikiEvents（英语新闻）均为英语。对于依赖 subword tokenization 的 continuation masking 机制（§3.3），跨语言泛化（尤其中日韩等非空格分词语言）是一个实质性开放问题。应在 Limitations 中加一句明确标注。

**[AGREE] R1-W5: Post-hoc filtering 对比可能不够公平**

同意。论文的 post-hoc filtering baseline（§5.1, p.5: "Post-hoc filtering achieves DR→0% but with 15-74% rejection rates"）是 discard-based（丢弃 invalid triples），而非 correction-based（将 invalid types 替换为最近的 valid type）。

一个 post-hoc correction baseline（如用 embedding 距离最近的合法类型替换违规类型）可能在 DR 和 F1 之间取得比 discard 更好的平衡，从而构成更强的 baseline。论文在 Appendix C (p.22, "Post-Hoc Filtering: Extended Comparison", Table 11) 提供了更详细的 post-hoc 分析，但仍是 discard-based。

不过，需要指出：post-hoc correction 作为 baseline 的公平性也有争议——因为 correction 需要额外的 type similarity 信息（如 type embedding），这引入了 OntoCoDec 未使用的外部知识。论文的 discard-based filtering 是一个 assumption-minimal 的 baseline。

---

### 小问题

**[AGREE]** 页数溢出（~8行结论在第9页）：与我的 N1 一致，我将其列为 critical。

**[AGREE]** Table 1 "Tgt." 列含义不直观：确实，"Tgt." 代表 "Target"（全部 violations 为 0 的目标），但未在表注中解释。

**[AGREE]** Enabling dependency 概念在主文中未正式定义：§3.1 Corollary 提到 "the enabling dependency is necessary" 但 enabling dependency 本身（grammar layer 不能替代 semantic layer）在主文中仅用自然语言描述，没有形式化定义。

**[AGREE]** Figure 1 信息密度高：与我的 m3 一致。

**[AGREE]** Orphan bib entries：与我的 m1 一致。

**[AGREE]** 引用格式 encoding mismatch：verify_references 工具确认 10/60 entries 有 minor mismatches（主要是作者姓名编码，如 Šakota vs Sakota），2 entries 在 OpenAlex 中未找到（regino2025kgcurator, formattax2026）。

---

### 对 R1 主要优势的回应

R1 列出的 6 项优势与我的评估基本一致：

1. **Decidability taxonomy 是真正的理论贡献** — 完全同意，这是论文最显著的学术贡献。
2. **Ablation 设计全面** — 同意，5-way ablation (Table 1) + 4-way fine-tuned ablation (Table 10) 设计精良。
3. **Fine-tuning composability 有实际价值** — 同意，Table 2 显示 LoRA fine-tuning 后约束仍然有效（DR ≤ 0.09% on SciERC）。
4. **附录极其详尽** — 同意，24 页附录覆盖从 prompts 到 pumping lemma 证明的几乎所有细节。
5. **DR 消减效果显著** — 同意，但需加 caveat：在 favorable conditions 下（LoRA + beam S1）。
6. **统计实践良好** — 同意，bootstrap CI、cross-seed validation (Table 20) 等。

---

### 总结

R1 与 R2（我）在以下关键判断上一致：
- **Overall 3.0 (Findings)**：执行质量高但新颖性偏增量
- **Soundness 3.5**：主要 claims 有支撑但存在 guarantee/fallback 矛盾
- **WikiEvents 初步性**：两位 reviewer 均标记
- **κ̄ 样本量不足**：两位 reviewer 均标记
- **页数超限**：两位 reviewer 均标记

两位 reviewer 的分歧点：
- **R1-N4 (70B 评估)**：R1 列为 Must-Fix，我认为应降为 Should-Fix。Abstract 的 "applicable to autoregressive LMs" 是方法适用范围声明而非性能保证，且 Table 4 已提供 70B 验证数据。
- **R1-W3 (S1 vs S2 选择)**：R1 认为缺乏论证，我认为 §5.1 已提供足够的三维度对比。
- **Baseline 对比 (R1-N1)**：R1 标记为最严重的 critical issue。我同意其重要性，但补充指出 grammar-only ablation 隐含了 GCD 对比——论文应将此显式化而非要求完全重新实验。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1539 · 2026-05-21T01:33:34.912994+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-21T01:33:34.913515+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-21T01:33:35.064790+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T01:19:27.564328+00:00\", \"completed_at\": \"2026-05-21T01:23:50.642072+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主正文溢出至第 9 页，仅有 ~8 行结论文本（约占页面 10%），其余 >80% 为空白。EMNLP 2026 严格 8 页限制——此溢出构成页数超限风险，且大面积空白给审稿人极差的第一印象。需压缩主正文使结论在第 8 页结束，或在第 8 页为结论腾出足够空间\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"连续 2 页纯文本无任何 display item（figure/table/equation）。审稿人打开论文前 2 页看到纯文字墙，缺少视觉锚点来快速建立对方法的认知。第一个 display item（Figure 1）直到第 3 页才出现\"}, {\"severity\": \"warning\", \"dimension\": \"pages 4-5\", \"message\": \"连续 2 页纯文本无 display item。Page 4 有少量数学公式和 Proposition 但无 figure/table 穿插，page 5 整页纯文字叙述（Constraint Tightness + Experiments 开头）\"}, {\"severity\": \"warning\", \"dimension\": \"pages 6-7\", \"message\": \"Display items 分布严重不均——主正文的全部 5 个 table（Tables 1-5）集中在这 2 页，形成\\\"表格墙\\\"。与 pages 1-2、4-5、8-9 无 display item 形成强烈反差，阅读节奏失调\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"4 个 section header（§5.3, §5.4, §6 Related Work, §7 Discussion and Conclusion）全部起始于同一页，给人论文末段草率收尾的印象。§7 在页底仅有几行就溢出到 page 9\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-9\", \"message\": \"主正文仅 1 个 figure（Figure 1 架构图）+ 5 个 table，无任何实验结果可视化图。全部实验结果以表格呈现，缺少 bar chart / line plot 等直观图形。Figure 2-4 全部推到 appendix。审稿人快速扫描实验结果时缺少视觉锚点\"}, {\"severity\": \"warning\", \"dimension\": \"page 24, appendix\", \"message\": \"Figure 3 使用红色/绿色区分 violation 类型，对红绿色盲用户不友好。建议改用 blue/orange 或 Okabe-Ito 色板\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（全宽架构图）是论文第一个也是主正文唯一一个 figure，出现在第 3 页。图中展示了 grammar layer 和 semantic layer 的编译流程，caption 基本自包含。若能提前到第 2 页或第 1 页底部，可更早建立审稿人的认知锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，符合 ACL anonymous submission 模板规范。行号正确显示\"}, {\"severity\": \"info\", \"dimension\": \"pages 6-7\", \"message\": \"表格均使用 book
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 1542 · 2026-05-21T01:33:35.065522+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1543 · 2026-05-21T01:33:58.941572+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1544 · 2026-05-21T01:33:59.243267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1545 · 2026-05-21T01:35:53.028053+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R15 fresh review, 2026-05-21\n\n# ============================================================\n# Round 15 Must-Fix\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD/CRANE 等同类 constrained decoding 方法的实验对比（连续 4 轮 R12-R15）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: should-fix\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF3: 升级为 must-fix\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1: 连续 3 轮。战略转换为 grammar-only ablation reframed as Level 1 对比\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF1: R1 critical, R2 AGREE。grammar-only ablation 隐含 GCD 对比但未显式化。BoostCD head-to-head 仍缺。连续 4 轮未解决。\"\n  action_items:\n    - round: 14\n      action: \"grammar-only ablation reframed as BoostCD-equivalent Level 1\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF2\"\n  summary: \"Abstract/Intro 中 'guarantee' 措辞与 fallback 机制存在系统性 overclaiming\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF2: fallback 36.6% 触发率。FT fallback ≤0.11% 已补充。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF2: R1 critical, R2 AGREE。三层保证缺口：(a) grammar-first fallback 跳过 semantic layer；(b) Level 3 未强制；(c) 残余 CF。Abstract 'formal guarantees' 与 §3.3 'best-effort' 矛盾。\"\n  action_items:\n    - round: 14\n      action: \"补充 FT fallback ≤0.11% 数据 + §4 fallback 分析段落\"\n      assigned_to: agent + paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页（~8 行结论），违反 EMNLP 2026 严格 8 页限制（R13 曾修复，R15 回归）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF1: critical，已修复\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 确认 8 页 ≤ limit\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF3: 回归。R2 critical, R1 降级建议 minor-major。Director 取 major——需修复但非 desk-reject 风险。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Major Issues\n# ============================================================\n\n- id: \"R15-W1\"\n  summary: \"新颖性定位不清：系统集成 vs 算法创新，Proposition 1 是 motivation 还是 method\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF5: novelty 适中，reviewer judgment\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W1: R2 critical (Excitement 2.5), R1 部分 REBUT (Excitement 3.0)——Prop 1 有独立理论价值。Director 取 major。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"DR↔CF trade-off 选择性报告：Abstract 'near-eliminates' 但 Llama CF 高达 12.02%\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2 独立发现 (W1), R1 强烈 AGREE。Table 1 SciERC Llama: DR 13.37→0 但 CF 0→12.02, 净减少仅 1.35pp。需综合指标或并列报告。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W3\"\n  summary: \"WikiEvents FT 仅 20-doc test set，统计功效不足（连续 4 轮）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF1: per-doc variance 和 CI 已补充\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W3: R1 major, R2 AGREE。20-doc 仍不足以支撑 composability 结论。建议标记 preliminary/pilot。\"\n  action_items:\n    - round: 14\n      action: \"补充 per-doc variance 和统计功效讨论\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W4\"\n  summary: \"κ̄ 贡献定位过高：n=6 无统计推断力，定义直觉明显\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF2: Spearman ρ 替换为 descriptive，n=6 caveat 已加\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W4: R1 warning, R2 major, 双方 AGREE。§1 仍列为主要贡献，应降级为 diagnostic metric。\"\n  action_items:\n    - round: 14\n      action: \"ρ=-0.77 替换为 descriptive + n=6 caveat\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Should-Fix\n# ============================================================\n\n- id: \"R15-W5\"\n  summary: \"70B 评估过于 preliminary（1 模型、无 ablation/FT）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-M2: 仅 INT4 推理\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W5: R1 major, R2 REBUT→should-fix。R2 论证 Abstract 是适用范围声明而非性能保证。Director 取 should-fix。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W6\"\n  summary: \"Fallback causal tracing 缺失：residual DR 中 fallback 贡献未量化\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 warning (W2), R2 AGREE。需追踪 residual violations 到 fallback vs non-fallback positions。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W7\"\n  summary: \"仅英语数据集评估，跨语言泛化未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 warning (W4), R2 AGREE。Limitations 未提及语言覆盖缺口。continuation masking 对非空格语言可能有显著差异。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W8\"\n  summary: \"Post-hoc filtering 对比不够公平（discard vs correction）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 warning (W5), R2 AGREE with nuance——correction 需额外 type similarity 信息。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Minor\n# ============================================================\n\n- id: \"R15-M1\"\n  summary: \"Orphan bib entries (chen2024agentre, fan2024fsn) 仍存在\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-M5: 全局 bib audit 报告 0 orphans（与 R15 发现矛盾）\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-M1: 两位 Reviewer 均标记。可能 R14 审计不准确或后续修改引入。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M2\"\n  summary: \"Abstract '1-2% even after LoRA fine-tuning' 与 Table 2 数据不完全一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"Table 2 LoRA unconstrained DR 范围需核实。'1-2%' 可能指 unconstrained FT residual 而非 constrained。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M3\"\n  summary: \"Enabling dependency 概念主文未正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"§3.1 Corollary 提及但未形式化定义。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M4\"\n  summary: \"Figure 1 信息密度过高，visual hierarchy 不清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"两位 Reviewer + 视觉审查均标记。建议增加 running example figure。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Missing References\n# ============================================================\n\n- id: \"R15-REF1\"\n  summary: \"Riedel et al. (2009) MLN for IE 未引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"Constraint-based IE 历史工作，R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-REF2\"\n  summary: \"Anderson et al. (2017) Constrained Beam Search 未引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"与 §5.3 beam search 讨论直接相关，R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved issues (abbreviated)\n# ============================================================\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Intro 被系统性低估\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 修复。R15 以 R15-W2 (DR↔CF trade-off 选择性报告) 形式部分复发。\"\n  resolution_round: 14\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents FT n=20 + Contribution 3 措辞过度\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 拆分 RE systematic + EE preliminary。R15 以 R15-W3 继续追踪。\"\n  resolution_round: 14\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 2 定位过高\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 移出 Contribution（3→2）。R15 以 R15-W4 继续追踪 §1 定位。\"\n  resolution_round: 14\n\n- id: \"R14-SF4\"\n  summary: \"泛化性声称超出验证范围\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 未作为独立 issue 提出，但 R1-N4 (70B) 和 R1-W4 (English-only) 反映相同底层问题。部分改善但未完全解决。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"FT fallback ≤0.11% 已补充。R15 以 R15-MF2 和 R15-W6 从新角度追踪。\"\n  resolution_round: 14\n\n- id: \"R14-M3\"\n  summary: \"Entity registry 顺序依赖未量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"100% ordering confirmed (EBNF 结构保证)，§3 已加说明\"\n  resolution_round: 14\n\n- id: \"R14-M4\"\n  summary: \"Related Work §6 压缩过度\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未独立提出，但视觉审查标记 page 8 有 4 个 section header 堆叠，与压缩过度一致。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-REF1\"\n  summary: \"TANL (Paolini et al., 2021) 未引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未提出——可能已添加。待确认。\"\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R15 fresh review, 2026-05-21\n\n# ============================================================\n# Round 15 Must-Fix\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD/CRANE 等同类 constrained decoding 方法的实验对比（连续 4 轮 R12-R15）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: should-fix\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF3: 升级为 must-fix\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1: 连续 3 轮。战略转换为 grammar-only ablation reframed as Level 1 对比\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF1: R1 critical, R2 AGREE。grammar-only ablation 隐含 GCD 对比但未显式化。BoostCD head-to-head 仍缺。连续 4 轮未解决。\"\n  action_items:\n    - round: 14\n      action: \"grammar-only ablation reframed as BoostCD-equivalent Level 1\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF2\"\n  summary: \"Abstract/Intro 中 'guarantee' 措辞与 fallback 机制存在系统性 overclaiming\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF2: fallback 36.6% 触发率。FT fallback ≤0.11% 已补充。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF2: R1 critical, R2 AGREE。三层保证缺口：(a) grammar-first fallback 跳过 semantic layer；(b) Level 3 未强制；(c) 残余 CF。Abstract 'formal guarantees' 与 §3.3 'best-effort' 矛盾。\"\n  action_items:\n    - round: 14\n      action: \"补充 FT fallback ≤0.11% 数据 + §4 fallback 分析段落\"\n      assigned_to: agent + paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页（~8 行结论），违反 EMNLP 2026 严格 8 页限制（R13 曾修复，R15 回归）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF1: critical，已修复\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 确认 8 页 ≤ limit\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF3: 回归。R2 critical, R1 降级建议 minor-major。Director 取 major——需修复但非 desk-reject 风险。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Major Issues\n# ============================================================\n\n- id: \"R15-W1\"\n  summary: \"新颖性定位不清：系统集成 vs 算法创新，Proposition 1 是 motivation 还是 method\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF5: novelty 适中，reviewer judgment\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W1: R2 critical (Excitement 2.5), R1 部分 REBUT (Excitement 3.0)——Prop 1 有独立理论价值。Director 取 major。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"DR↔CF trade-off 选择性报告：Abstract 'near-eliminates' 但 Llama CF 高达 12.02%\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2 独立发现 (W1), R1 强烈 AGREE。Table 1 SciERC Llama: DR 13.37→0 但 CF 0→12.02, 净减少仅 1.35pp。需综合指标或并列报告。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W3\"\n  summary: \"WikiEvents FT 仅 20-doc test set，统计功效不足（连续 4 轮）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF1: per-doc variance 和 CI 已补充\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W3: R1 major, R2 AGREE。20-doc 仍不足以支撑 composability 结论。建议标记 preliminary/pilot。\"\n  action_items:\n    - round: 14\n      action: \"补充 per-doc variance 和统计功效讨论\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W4\"\n  summary: \"κ̄ 贡献定位过高：n=6 无统计推断力，定义直觉明显\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF2: Spearman ρ 替换为 descriptive，n=6 caveat 已加\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W4: R1 warning, R2 major, 双方 AGREE。§1 仍列为主要贡献，应降级为 diagnostic metric。\"\n  action_items:\n    - round: 14\n      action: \"ρ=-0.77 替换为 descriptive + n=6 caveat\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Should-Fix\n# ============================================================\n\n- id: \"R15-W5\"\n  summary: \"70B 评估过于 preliminary（1 模型、无 ablation/FT）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-M2: 仅 INT4 推理\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W5: R1 major, R2 REBUT→should-fix。R2 论证 Abstract 是适用范围声明而非性能保证。Director 取 should-fix。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W6\"\n  summary: \"Fallback causal tracing 缺失：residual DR 中 fallback 贡献未量化\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 warning (W2), R2 AGREE。需追踪 residual violations 到 fallback vs non-fallback positions。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W7\"\n  summary: \"仅英语数据集评估，跨语言泛化未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 warning (W4), R2 AGREE。Limitations 未提及语言覆盖缺口。continuation masking 对非空格语言可能有显著差异。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W8\"\n  summary: \"Post-hoc filtering 对比不够公平（discard vs correction）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 warning (W5), R2 AGREE with nuance——correction 需额外 type similarity 信息。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Minor\n# ============================================================\n\n- id: \"R15-M1\"\n  summary: \"Orphan bib entries (chen2024agentre, fan2024fsn) 仍存在\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-M5: 全局 bib audit 报告 0 orphans（与 R15 发现矛盾）\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-M1: 两位 Reviewer 均标记。可能 R14 审计不准确或后续修改引入。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M2\"\n  summary: \"Abstract '1-2% even after LoRA fine-tuning' 与 Table 2 数据不完全一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"Table 2 LoRA unconstrained DR 范围需核实。'1-2%' 可能指 unconstrained FT residual 而非 constrained。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M3\"\n  summary: \"Enabling dependency 概念主文未正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"§3.1 Corollary 提及但未形式化定义。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M4\"\n  summary: \"Figure 1 信息密度过高，visual hierarchy 不清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"两位 Reviewer + 视觉审查均标记。建议增加 running example figure。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 15 Missing References\n# ============================================================\n\n- id: \"R15-REF1\"\n  summary: \"Riedel et al. (2009) MLN for IE 未引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"Constraint-based IE 历史工作，R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-REF2\"\n  summary: \"Anderson et al. (2017) Constrained Beam Search 未引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"与 §5.3 beam search 讨论直接相关，R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved issues (abbreviated)\n# ============================================================\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Intro 被系统性低估\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 修复。R15 以 R15-W2 (DR↔CF trade-off 选择性报告) 形式部分复发。\"\n  resolution_round: 14\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents FT n=20 + Contribution 3 措辞过度\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 拆分 RE systematic + EE preliminary。R15 以 R15-W3 继续追踪。\"\n  resolution_round: 14\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 2 定位过高\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 移出 Contribution（3→2）。R15 以 R15-W4 继续追踪 §1 定位。\"\n  resolution_round: 14\n\n- id: \"R14-SF4\"\n  summary: \"泛化性声称超出验证范围\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 未作为独立 issue 提出，但 R1-N4 (70B) 和 R1-W4 (English-only) 反映相同底层问题。部分改善但未完全解决。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"FT fallback ≤0.11% 已补充。R15 以 R15-MF2 和 R15-W6 从新角度追踪。\"\n  resolution_round: 14\n\n- id: \"R14-M3\"\n  summary: \"Entity registry 顺序依赖未量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"100% ordering confirmed (EBNF 结构保证)，§3 已加说明\"\n  resolution_round: 14\n\n- id: \"R14-M4\"\n  summary: \"Related Work §6 压缩过度\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未独立提出，但视觉审查标记 page 8 有 4 个 section header 堆叠，与压缩过度一致。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-REF1\"\n  summary: \"TANL (Paolini et al., 2021) 未引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未提出——可能已添加。待确认。\"\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1546 · 2026-05-21T01:35:53.130103+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 11271}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1547 · 2026-05-21T01:38:46.987047+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Round 15 | Fresh Review | EMNLP 2026 ARR May Cycle**\n**Reviewers**: R1（方法严谨性+实验充分性）、R2（新颖性+完整性+格式合规）\n**审稿模式**: 圆桌会议，1 轮独立审稿 + 1 轮交叉分享，共识充分达成\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE ontology 翻译为两层可组合 token-level 解码约束的框架：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇表成员资格；semantic layer（prefix-decidable with state）通过动态实体注册表在运行时强制 domain/range 类型约束。论文以 decidability 分析为指导，证明 domain/range 约束不可被 context-free grammar 表达（Proposition 1，pumping lemma），建立了两层架构的理论必要性。在 SciERC、DocRED、WikiEvents 上验证，覆盖 4 个模型（7-70B）和 3 个 tokenizer family，LoRA + greedy S1 配置下 DR ≤ 0.09%、R-F1 变化不显著（±0.6 pp）。\n\n---\n\n## Strengths\n\n1. **Decidability taxonomy 是真正的理论贡献** [R1 + R2 共识]：将 IE 类型约束分为三层（context-free / prefix-decidable with state / non-local）在该领域属首次。Proposition 1 的 pumping lemma 证明（Appendix O）严谨且有启发性，建立了为何单纯 CFG 不足以处理 domain/range 约束的理论 lower bound。\n\n2. **Ablation 设计全面且有力** [R1 + R2 共识]：Table 1 的 5-way ablation + Table 10 的 4-way fine-tuned ablation 精确隔离了各层贡献。关键发现——semantic layer 单独仅减少 24% DR，但与 grammar layer 组合后达到 94-100%——为两层架构的必要性提供了直接经验证据。\n\n3. **Fine-tuning composability 有实际部署价值** [R1 + R2 共识]：Table 2 的 paired bootstrap 检验（B=1000, document-level）证明 LoRA + S1 约束不显著降低 R-F1（p>0.05, 最大|Δ|=0.31 pp），同时 DR 显著下降（p<0.001）。这是实际部署的关键属性，prior work（GCD, BoostCD）均未系统验证此交互。\n\n4. **附录极其详尽（24 页，A-O）** [R1 + R2 共识]：case studies（Appendix J）、per-relation error analysis（Appendix D/N）、scalability benchmarks（Appendix K）、beam search 完整分析（Appendix F）、prompt templates（Appendix A）、pumping lemma 完整证明（Appendix O）——reproducibility 极高。\n\n5. **诚实的 Limitations 讨论** [R2]：CF trade-off、WikiEvents 初步性、API-only 模型不适用、tokenizer 依赖性等均有坦诚讨论。\n\n6. **统计实践规范** [R1]：paired bootstrap、CI 宽度透明、cross-seed validation（Table 20）、p 值报告到位。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R1-N1, R2 AGREE] **完全缺失与同类 constrained decoding 方法的实验对比**\n论文在 Related Work（§6, Appendix B）详细讨论了 GCD (Geng et al., 2023)、BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025)、EnriCo (Zaratiana et al., 2024)，但实验中唯一对比是 unconstrained decoding 和 post-hoc filtering。GCD 同样使用 grammar-constrained decoding 处理 SciERC，BoostCD 同样在 IE 任务上做约束解码。论文声称 grammar-only ablation（Table 1 第 2 行）\"represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\"，但这一隐含对比未显式化，且 BoostCD 的混合策略完全不同。**对于一篇 constrained decoding framework 论文，不与同类方法 head-to-head 对比是致命短板——reviewer 无法量化边际贡献。** 此问题已连续 4 轮（R12-R15）被标记。\n\n**MF2** [critical, R1-N2, R2 AGREE] **\"Guarantee\" 措辞系统性高于实际保证水平**\nAbstract (\"formal guarantees at each layer\")、§1 (\"formal guarantees\") 与 §3.3 (\"best-effort pair-based enforcement\")、§4 grammar-first fallback 存在系统性矛盾。三层保证缺口：(a) grammar-first fallback 在 S(t)∩G(t)=∅ 时跳过 semantic layer，恰恰在模型最可能产生 type-incompatible 输出时放弃约束；(b) Level 3 constraints（cross-triple consistency）显式未被强制；(c) Full S1 仍有残余 CF 0.08-12.02%。Limitations 部分诚实讨论了这些缺口，但 Abstract/Introduction 的 \"guarantee\" 表述未做对应限定，构成 claim-evidence 不一致。\n\n**MF3** [major, R2-N1, R1 agree 降级] **正文溢出至第 9 页，违反 EMNLP 2026 严格 8 页限制**\nSection 7 \"Discussion and Conclusion\" 约 8 行文字溢出到第 9 页。此问题在 R13 曾修复、R14 确认合规，R15 回归。ARR 规定 \"strict 8-page limit for main text\"。R2 列为 critical（desk reject 风险），R1 降级为 minor-major（8 行溢出非 desk reject 标准）。**Director 判定：major——必须修复，但非 desk-reject 级别。** 压缩 §7 或 §6 即可解决。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [major, R2-N2, R1 partially REBUT] **核心新颖性定位不清：系统集成 vs 算法创新**\nR2 指出 grammar layer 是 XGrammar 直接应用、semantic layer 是运行时类型检查的直接实现，论文缺少对 \"what is genuinely new beyond combining XGrammar with a type-checking registry\" 的回应。R1 部分反驳：Proposition 1 具有独立理论价值（非仅 motivation），enabling dependency formalization 排除了替代架构，fine-tuning composability 验证是 prior work 未做的实质性贡献。**Director 判定：论文 novelty 主要在 formalization + informed system design 层面，非 algorithmic breakthrough。建议在 Introduction 中显式声明此定位。** Excitement 分歧（R1: 3.0, R2: 2.5），Director 取 2.75。\n\n**SF2** [major, R2-W1, R1 AGREE] **DR↔CF trade-off 选择性报告**\nAbstract 声称 \"near-eliminates DR (94-100% reduction)\"，但 Table 1 SciERC Llama Full S1 显示 DR 13.37→0% 的同时 CF 0→12.02%，净 violation 减少仅 ~1.35 pp。CF trade-off 是 model-dependent（Qwen CF 仅 0.035%），但 Abstract/Intro 的叙事重心完全在 DR reduction 上。建议：(1) 在 Abstract/Intro 中将 DR reduction 与 CF introduction 并列报告；(2) 考虑使用总 violation rate（DR+CF）作为补充指标。\n\n**SF3** [major, R1-N3, R2 AGREE] **WikiEvents fine-tuning 评估统计功效不足（n=20）**\nFine-tuning composability 仅基于 20 文档验证，bootstrap CI 可信度有限。论文已标注 \"preliminary\"，但主文叙事仍从此得出 composability 结论。此问题连续 4 轮（R12-R15）被标记，R14 补充了 per-doc variance 和统计功效讨论。建议将 WikiEvents fine-tuning 结论从主要 claim 中移除或标注 \"indicative only\"。EE schema 结构比 RE 更复杂（嵌套 argument roles），但论文对此差异讨论不足。\n\n**SF4** [major, R1-W1 = R2-W2, 共识] **κ̄ 贡献定位过高**\nκ̄ 定义为 1-|σ(r)|/|E|² 的平均值，直觉明显（schema 越紧约束效果越好）。n=6 的回归分析（Figure 2）无统计推断力，论文自身承认。但 §1 contributions 仍将其列为主要贡献。建议降级为 \"diagnostic metric introduced for deployment guidance\"，从 contributions list 中合并到实验评估子点。\n\n**SF5** [should-fix, R1-N4, R2 REBUT] **70B 评估过于 preliminary**\nR1 认为 Abstract \"applicable to autoregressive LMs\" 过宽。R2 反驳：这是适用范围声明（有 logit access 即可用），非性能保证；且 Table 4 已提供 70B 验证数据显示相同 DR 消减模式。**Director 判定：R2 论点合理，降为 should-fix。** 建议在 Limitations 中加一句明确承认 70B scale 验证有限。\n\n**SF6** [warning, R1-W2, R2 AGREE] **Fallback causal tracing 缺失**\nResidual DR violations 中有多少源自 grammar-first fallback 事件未被量化。Appendix D 按 violation type 分类（entity type error / schema coverage gap / model generation error），但未按 fallback vs non-fallback positions 分类。追踪 fallback 事件与 residual violations 的关联性将直接回答 fallback 机制的实际影响。\n\n**SF7** [warning, R1-W4, R2 AGREE] **仅英语数据集评估，跨语言泛化未讨论**\n3 个数据集均为英语。Continuation masking 依赖 subword tokenization，跨语言泛化（特别是中日韩等非空格分词语言）是实质性开放问题。Limitations 未明确标注语言覆盖缺口。\n\n**SF8** [warning, R1-W5, R2 AGREE with nuance] **Post-hoc filtering 对比不够公平**\nPost-hoc filtering baseline 是 discard-based（丢弃 invalid triples），而非 correction-based（替换 invalid types）。Post-hoc correction 可能构成更强的 baseline。R2 补充：correction 需额外 type similarity 信息，论文的 discard baseline 是 assumption-minimal。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成共识（交叉分享后均 [AGREE]）：\n\n1. **[AGREE] 缺少竞品实验对比是最关键缺陷**（MF1）——两位 Reviewer 均将此列为 critical\n2. **[AGREE] \"Guarantee\" overclaiming 需修正**（MF2）——建议替换为 \"enforcement\" 或 \"near-elimination\"\n3. **[AGREE] WikiEvents n=20 不足以支撑 composability 结论**（SF3）\n4. **[AGREE] κ̄ 应降级为 diagnostic metric**（SF4）\n5. **[AGREE] 页数超限需修复**（MF3）\n6. **[AGREE] DR↔CF trade-off 需在 Abstract/Intro 中并列报告**（SF2）\n7. **[AGREE] Fallback causal tracing 应补充**（SF6）\n8. **[AGREE] 英语覆盖缺口应在 Limitations 中标注**（SF7）\n9. **[AGREE] Decidability taxonomy 是论文最大亮点**\n10. **[AGREE] 实验评估全面性和统计实践均属优秀**\n\n## Reviewer Divergence\n\n以下问题存在分歧，交叉分享后未完全消解：\n\n1. **[分歧] 新颖性定位（SF1）**：R2 认为组件级无创新（Excitement 2.5），R1 认为 Prop 1 有独立理论价值（Excitement 3.0）。Director 取 2.75——formalization 有价值但方法层面确为工程集成。\n\n2. **[分歧] 70B 评估严重性（SF5）**：R1 major vs R2 should-fix。R2 论证 \"applicable to autoregressive LMs\" 是适用范围声明而非性能保证。Director 采纳 R2 论点，降为 should-fix。\n\n3. **[分歧] 页数超限严重性（MF3）**：R2 critical（desk reject 风险）vs R1 minor-major（8 行不构成 desk reject）。Director 取 major——必须修复但 8 行溢出在 ARR 实践中非自动 desk reject。\n\n4. **[分歧] Supervised baseline 对比（R2-W4）**：R2 认为应加 PURE/PL-Marker F1 作为 upper-bound。R1 反驳为 category error——OntoCoDec 是约束层非 IE system。Director 采纳 R1 论点，不列为 issue。\n\n5. **[分歧] S1 vs S2 论证（R1-W3）**：R1 认为缺乏 cost-benefit 分析。R2 反驳 §5.1 已提供三维度对比。Director 判定：现有论证基本充分，不列为独立 issue。\n\n---\n\n## Questions\n\n1. Residual DR violations（如 Table 10 中 fine-tuned 设置下 36 个残余 violations）中有多少直接源自 grammar-first fallback 事件？\n2. 在 70B+ 模型上 baseline violation rate 是否显著低于 7-8B？OntoCoDec 的边际价值如何？\n3. 当同一实体以不同表面形式出现时（如 \"Barack Obama\" 和 \"Obama\"），entity registry D 如何处理？是否导致同一实体被赋予不同类型？\n4. DocRED beam search 仅在 50-doc subset 上评估的原因是什么？是否有 full-set 结果可补充？\n5. 为什么没有与 GCD (Geng et al., 2023) 在 SciERC 上做直接数值对比？grammar-only ablation 隐含了 Level 1 对比，但这需要显式化论证。\n\n---\n\n## Missing References\n\n- **GCD** (Geng et al., 2023, EMNLP)：已引用但未做实验对比——SciERC 上 grammar-constrained decoding 的最直接前序工作 [R1, R2 共识]\n- **BoostCD** (Sakota et al., 2025, EMNLP)：已引用但未做实验对比——IE constrained+unconstrained 混合方法 [R1, R2 共识]\n- **CRANE** (Banerjee et al., 2025, ICML)：已引用但仅定性讨论——semantic constraint reasoning [R1]\n- **Riedel et al. (2009)** Markov Logic Networks for IE：constraint-based IE 历史工作 [R2, R1 AGREE]\n- **Anderson et al. (2017)** Constrained Beam Search：早期约束 beam search 工作 [R2, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目未配置 external_review.paperreview_ai。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (2026-05-21 01:19 → 01:23, 约 4 分钟)\n\n| 严重性 | 数量 | 关键发现 |\n|--------|------|----------|\n| Critical | 1 | 主正文溢出至第 9 页，>80% 空白（与 MF3 一致）|\n| Warning | 6 | (1) Pages 1-2 连续纯文本无 display item，缺少视觉锚点；(2) Pages 4-5 同样无 display item；(3) Pages 6-7 全部 5 个 table 集中形成\"表格墙\"；(4) Page 8 有 4 个 section header 堆叠，给人草率收尾印象；(5) 主正文仅 1 个 figure + 5 个 table，无实验结果可视化图；(6) Appendix Figure 3 红绿色对色盲不友好 |\n| Info | 8 | Figure 1 建议提前到 p1-2；booktabs 表格质量良好；引用格式正常；Appendix 图表可读性好 |\n\n**视觉审查总评**：主正文 display item 分布严重不均（pages 1-5 无图表 → pages 6-7 表格密集 → page 8-9 section 堆叠+溢出），阅读节奏失调。建议将 Figure 2/3 从 Appendix 移入主文以平衡视觉密度，同时压缩 §6/§7 解决页数溢出。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5（Findings）**\n\n**EMNLP 2026 ARR 评分对照：3 = Findings（可被 Findings 接收）**\n\n**Confidence：4/5**（两位 Reviewer 均为 4/5）\n\n### 评分理由\n\n**支撑 Findings 接收的因素：**\n- Decidability taxonomy + Proposition 1 是该领域首次将 IE 约束映射到形式语言理论的尝试，有独立理论价值\n- 实验评估覆盖面广（3 数据集 × 4 模型 × 多解码策略 × zero-shot/fine-tuning），ablation 设计精良\n- DR near-elimination（94-100%）+ R-F1 不显著下降的核心结果可靠（bootstrap 检验）\n- Fine-tuning composability 验证有实际部署价值\n- 附录（24 页）和统计实践远超同类投稿\n\n**阻碍 Conference 接收的因素：**\n- [最关键] 完全缺失与 GCD/BoostCD/CRANE 等同类方法的实验对比——边际贡献无法量化。此问题已连续 4 轮被标记，始终未以 head-to-head 实验方式解决。\n- \"Guarantee\" 措辞系统性 overclaiming——Abstract/Intro 承诺的保证水平与 fallback 机制、Level 3 缺口、残余 CF 的实际情况不匹配\n- 新颖性主要在 formalization + informed system design 层面，组件级创新有限（grammar layer = XGrammar 应用，semantic layer = 运行时类型检查）\n- WikiEvents 20-doc fine-tuning 评估统计功效不足，κ̄ 基于 n=6 无统计推断力\n- 正文超 8 页限制（回归问题）\n\n**提升至 Borderline Conference（3.5）的路径：**\n1. 至少在 SciERC 上与 GCD 做显式数值对比（可以基于 grammar-only ablation 论证等价性，但必须显式化）\n2. 将 \"guarantee\" 全面替换为 \"enforcement\"/\"near-elimination\"，Abstract/Intro 措辞与 Limitations 对齐\n3. 修复页数溢出\n4. 在 Abstract/Intro 中并列报告 DR reduction 和 CF introduction\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"formal guarantees at each level\"（p2, contribution 1）→ 应改为 \"formal enforcement with best-effort semantics\"\n- κ̄ 在 contribution 1 中的权重应降低——合并到实验评估子点而非独立列出\n- \"applicable to autoregressive LMs with logits access\"（Abstract）→ 建议限定为 \"validated on 7-8B scale models with preliminary 70B results\"\n\n### §3 Method\n- Enabling dependency（§3.1 Corollary）在主文中仅用自然语言描述，缺少正式定义\n- Grammar-first fallback（§4）的 cascade 效应未分析：fallback-induced 类型错误是否传播到后续 triple\n\n### §4 Constraint Composition\n- Fallback 触发率（first-token 0.5-5.7% ZS, ≤0.11% FT）已报告，但应追踪 residual DR violations 到 fallback positions\n- 建议增加 \"net violation change\"（ΔDR+ΔCF）作为 Table 1 的补充列\n\n### §5 Experiments\n- Table 1 \"Tgt.\" 列含义未在正文或表注中解释\n- SciERC Llama CF=12.02% 应在主文而非仅 Limitations 中讨论\n- DocRED beam search 50-doc subset（§5.3）代表性需论证或补充 full-set 结果\n- WikiEvents §5.4 应增加 EE schema 约束编译过程与 RE 差异的讨论\n\n### §6 Related Work\n- grammar-only ablation 与 GCD 的等价性论证应在此节显式化\n- BoostCD 的差异（constrained+unconstrained 混合 vs OntoCoDec 的 pure enforcement）应更清晰地论述\n\n### §7 Discussion and Conclusion\n- 压缩至第 8 页内（当前溢出 ~8 行）\n- 建议增加 \"Our contribution is not a new decoding algorithm, but a formal analysis that reveals the necessity of a two-layer design\" 等 novelty 定位声明\n\n### Limitations\n- 增加语言覆盖缺口讨论（仅英语数据集，continuation masking 对非空格语言的影响）\n- 增加 70B scale 验证有限的明确说明\n\n### Format\n- 清理 orphan bib entries（chen2024agentre, fan2024fsn）\n- 核实 Abstract \"1-2% even after LoRA fine-tuning\" 与 Table 2 数据的一致性\n- Figure 3（Appendix）红绿色对色盲不友好，建议改用 Okabe-Ito 色板\n",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Round 15 | Fresh Review | EMNLP 2026 ARR May Cycle**\n**Reviewers**: R1（方法严谨性+实验充分性）、R2（新颖性+完整性+格式合规）\n**审稿模式**: 圆桌会议，1 轮独立审稿 + 1 轮交叉分享，共识充分达成\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE ontology 翻译为两层可组合 token-level 解码约束的框架：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇表成员资格；semantic layer（prefix-decidable with state）通过动态实体注册表在运行时强制 domain/range 类型约束。论文以 decidability 分析为指导，证明 domain/range 约束不可被 context-free grammar 表达（Proposition 1，pumping lemma），建立了两层架构的理论必要性。在 SciERC、DocRED、WikiEvents 上验证，覆盖 4 个模型（7-70B）和 3 个 tokenizer family，LoRA + greedy S1 配置下 DR ≤ 0.09%、R-F1 变化不显著（±0.6 pp）。\n\n---\n\n## Strengths\n\n1. **Decidability taxonomy 是真正的理论贡献** [R1 + R2 共识]：将 IE 类型约束分为三层（context-free / prefix-decidable with state / non-local）在该领域属首次。Proposition 1 的 pumping lemma 证明（Appendix O）严谨且有启发性，建立了为何单纯 CFG 不足以处理 domain/range 约束的理论 lower bound。\n\n2. **Ablation 设计全面且有力** [R1 + R2 共识]：Table 1 的 5-way ablation + Table 10 的 4-way fine-tuned ablation 精确隔离了各层贡献。关键发现——semantic layer 单独仅减少 24% DR，但与 grammar layer 组合后达到 94-100%——为两层架构的必要性提供了直接经验证据。\n\n3. **Fine-tuning composability 有实际部署价值** [R1 + R2 共识]：Table 2 的 paired bootstrap 检验（B=1000, document-level）证明 LoRA + S1 约束不显著降低 R-F1（p>0.05, 最大|Δ|=0.31 pp），同时 DR 显著下降（p<0.001）。这是实际部署的关键属性，prior work（GCD, BoostCD）均未系统验证此交互。\n\n4. **附录极其详尽（24 页，A-O）** [R1 + R2 共识]：case studies（Appendix J）、per-relation error analysis（Appendix D/N）、scalability benchmarks（Appendix K）、beam search 完整分析（Appendix F）、prompt templates（Appendix A）、pumping lemma 完整证明（Appendix O）——reproducibility 极高。\n\n5. **诚实的 Limitations 讨论** [R2]：CF trade-off、WikiEvents 初步性、API-only 模型不适用、tokenizer 依赖性等均有坦诚讨论。\n\n6. **统计实践规范** [R1]：paired bootstrap、CI 宽度透明、cross-seed validation（Table 20）、p 值报告到位。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R1-N1, R2 AGREE] **完全缺失与同类 constrained decoding 方法的实验对比**\n论文在 Related Work（§6, Appendix B）详细讨论了 GCD (Geng et al., 2023)、BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025)、EnriCo (Zaratiana et al., 2024)，但实验中唯一对比是 unconstrained decoding 和 post-hoc filtering。GCD 同样使用 grammar-constrained decoding 处理 SciERC，BoostCD 同样在 IE 任务上做约束解码。论文声称 grammar-only ablation（Table 1 第 2 行）\"represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\"，但这一隐含对比未显式化，且 BoostCD 的混合策略完全不同。**对于一篇 constrained decoding framework 论文，不与同类方法 head-to-head 对比是致命短板——reviewer 无法量化边际贡献。** 此问题已连续 4 轮（R12-R15）被标记。\n\n**MF2** [critical, R1-N2, R2 AGREE] **\"Guarantee\" 措辞系统性高于实际保证水平**\nAbstract (\"formal guarantees at each layer\")、§1 (\"formal guarantees\") 与 §3.3 (\"best-effort pair-based enforcement\")、§4 grammar-first fallback 存在系统性矛盾。三层保证缺口：(a) grammar-first fallback 在 S(t)∩G(t)=∅ 时跳过 semantic layer，恰恰在模型最可能产生 type-incompatible 输出时放弃约束；(b) Level 3 constraints（cross-triple consistency）显式未被强制；(c) Full S1 仍有残余 CF 0.08-12.02%。Limitations 部分诚实讨论了这些缺口，但 Abstract/Introduction 的 \"guarantee\" 表述未做对应限定，构成 claim-evidence 不一致。\n\n**MF3** [major, R2-N1, R1 agree 降级] **正文溢出至第 9 页，违反 EMNLP 2026 严格 8 页限制**\nSection 7 \"Discussion and Conclusion\" 约 8 行文字溢出到第 9 页。此问题在 R13 曾修复、R14 确认合规，R15 回归。ARR 规定 \"strict 8-page limit for main text\"。R2 列为 critical（desk reject 风险），R1 降级为 minor-major（8 行溢出非 desk reject 标准）。**Director 判定：major——必须修复，但非 desk-reject 级别。** 压缩 §7 或 §6 即可解决。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [major, R2-N2, R1 partially REBUT] **核心新颖性定位不清：系统集成 vs 算法创新**\nR2 指出 grammar layer 是 XGrammar 直接应用、semantic layer 是运行时类型检查的直接实现，论文缺少对 \"what is genuinely new beyond combining XGrammar with a type-checking registry\" 的回应。R1 部分反驳：Proposition 1 具有独立理论价值（非仅 motivation），enabling dependency formalization 排除了替代架构，fine-tuning composability 验证是 prior work 未做的实质性贡献。**Director 判定：论文 novelty 主要在 formalization + informed system design 层面，非 algorithmic breakthrough。建议在 Introduction 中显式声明此定位。** Excitement 分歧（R1: 3.0, R2: 2.5），Director 取 2.75。\n\n**SF2** [major, R2-W1, R1 AGREE] **DR↔CF trade-off 选择性报告**\nAbstract 声称 \"near-eliminates DR (94-100% reduction)\"，但 Table 1 SciERC Llama Full S1 显示 DR 13.37→0% 的同时 CF 0→12.02%，净 violation 减少仅 ~1.35 pp。CF trade-off 是 model-dependent（Qwen CF 仅 0.035%），但 Abstract/Intro 的叙事重心完全在 DR reduction 上。建议：(1) 在 Abstract/Intro 中将 DR reduction 与 CF introduction 并列报告；(2) 考虑使用总 violation rate（DR+CF）作为补充指标。\n\n**SF3** [major, R1-N3, R2 AGREE] **WikiEvents fine-tuning 评估统计功效不足（n=20）**\nFine-tuning composability 仅基于 20 文档验证，bootstrap CI 可信度有限。论文已标注 \"preliminary\"，但主文叙事仍从此得出 composability 结论。此问题连续 4 轮（R12-R15）被标记，R14 补充了 per-doc variance 和统计功效讨论。建议将 WikiEvents fine-tuning 结论从主要 claim 中移除或标注 \"indicative only\"。EE schema 结构比 RE 更复杂（嵌套 argument roles），但论文对此差异讨论不足。\n\n**SF4** [major, R1-W1 = R2-W2, 共识] **κ̄ 贡献定位过高**\nκ̄ 定义为 1-|σ(r)|/|E|² 的平均值，直觉明显（schema 越紧约束效果越好）。n=6 的回归分析（Figure 2）无统计推断力，论文自身承认。但 §1 contributions 仍将其列为主要贡献。建议降级为 \"diagnostic metric introduced for deployment guidance\"，从 contributions list 中合并到实验评估子点。\n\n**SF5** [should-fix, R1-N4, R2 REBUT] **70B 评估过于 preliminary**\nR1 认为 Abstract \"applicable to autoregressive LMs\" 过宽。R2 反驳：这是适用范围声明（有 logit access 即可用），非性能保证；且 Table 4 已提供 70B 验证数据显示相同 DR 消减模式。**Director 判定：R2 论点合理，降为 should-fix。** 建议在 Limitations 中加一句明确承认 70B scale 验证有限。\n\n**SF6** [warning, R1-W2, R2 AGREE] **Fallback causal tracing 缺失**\nResidual DR violations 中有多少源自 grammar-first fallback 事件未被量化。Appendix D 按 violation type 分类（entity type error / schema coverage gap / model generation error），但未按 fallback vs non-fallback positions 分类。追踪 fallback 事件与 residual violations 的关联性将直接回答 fallback 机制的实际影响。\n\n**SF7** [warning, R1-W4, R2 AGREE] **仅英语数据集评估，跨语言泛化未讨论**\n3 个数据集均为英语。Continuation masking 依赖 subword tokenization，跨语言泛化（特别是中日韩等非空格分词语言）是实质性开放问题。Limitations 未明确标注语言覆盖缺口。\n\n**SF8** [warning, R1-W5, R2 AGREE with nuance] **Post-hoc filtering 对比不够公平**\nPost-hoc filtering baseline 是 discard-based（丢弃 invalid triples），而非 correction-based（替换 invalid types）。Post-hoc correction 可能构成更强的 baseline。R2 补充：correction 需额外 type similarity 信息，论文的 discard baseline 是 assumption-minimal。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成共识（交叉分享后均 [AGREE]）：\n\n1. **[AGREE] 缺少竞品实验对比是最关键缺陷**（MF1）——两位 Reviewer 均将此列为 critical\n2. **[AGREE] \"Guarantee\" overclaiming 需修正**（MF2）——建议替换为 \"enforcement\" 或 \"near-elimination\"\n3. **[AGREE] WikiEvents n=20 不足以支撑 composability 结论**（SF3）\n4. **[AGREE] κ̄ 应降级为 diagnostic metric**（SF4）\n5. **[AGREE] 页数超限需修复**（MF3）\n6. **[AGREE] DR↔CF trade-off 需在 Abstract/Intro 中并列报告**（SF2）\n7. **[AGREE] Fallback causal tracing 应补充**（SF6）\n8. **[AGREE] 英语覆盖缺口应在 Limitations 中标注**（SF7）\n9. **[AGREE] Decidability taxonomy 是论文最大亮点**\n10. **[AGREE] 实验评估全面性和统计实践均属优秀**\n\n## Reviewer Divergence\n\n以下问题存在分歧，交叉分享后未完全消解：\n\n1. **[分歧] 新颖性定位（SF1）**：R2 认为组件级无创新（Excitement 2.5），R1 认为 Prop 1 有独立理论价值（Excitement 3.0）。Director 取 2.75——formalization 有价值但方法层面确为工程集成。\n\n2. **[分歧] 70B 评估严重性（SF5）**：R1 major vs R2 should-fix。R2 论证 \"applicable to autoregressive LMs\" 是适用范围声明而非性能保证。Director 采纳 R2 论点，降为 should-fix。\n\n3. **[分歧] 页数超限严重性（MF3）**：R2 critical（desk reject 风险）vs R1 minor-major（8 行不构成 desk reject）。Director 取 major——必须修复但 8 行溢出在 ARR 实践中非自动 desk reject。\n\n4. **[分歧] Supervised baseline 对比（R2-W4）**：R2 认为应加 PURE/PL-Marker F1 作为 upper-bound。R1 反驳为 category error——OntoCoDec 是约束层非 IE system。Director 采纳 R1 论点，不列为 issue。\n\n5. **[分歧] S1 vs S2 论证（R1-W3）**：R1 认为缺乏 cost-benefit 分析。R2 反驳 §5.1 已提供三维度对比。Director 判定：现有论证基本充分，不列为独立 issue。\n\n---\n\n## Questions\n\n1. Residual DR violations（如 Table 10 中 fine-tuned 设置下 36 个残余 violations）中有多少直接源自 grammar-first fallback 事件？\n2. 在 70B+ 模型上 baseline violation rate 是否显著低于 7-8B？OntoCoDec 的边际价值如何？\n3. 当同一实体以不同表面形式出现时（如 \"Barack Obama\" 和 \"Obama\"），entity registry D 如何处理？是否导致同一实体被赋予不同类型？\n4. DocRED beam search 仅在 50-doc subset 上评估的原因是什么？是否有 full-set 结果可补充？\n5. 为什么没有与 GCD (Geng et al., 2023) 在 SciERC 上做直接数值对比？grammar-only ablation 隐含了 Level 1 对比，但这需要显式化论证。\n\n---\n\n## Missing References\n\n- **GCD** (Geng et al., 2023, EMNLP)：已引用但未做实验对比——SciERC 上 grammar-constrained decoding 的最直接前序工作 [R1, R2 共识]\n- **BoostCD** (Sakota et al., 2025, EMNLP)：已引用但未做实验对比——IE constrained+unconstrained 混合方法 [R1, R2 共识]\n- **CRANE** (Banerjee et al., 2025, ICML)：已引用但仅定性讨论——semantic constraint reasoning [R1]\n- **Riedel et al. (2009)** Markov Logic Networks for IE：constraint-based IE 历史工作 [R2, R1 AGREE]\n- **Anderson et al. (2017)** Constrained Beam Search：早期约束 beam search 工作 [R2, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目未配置 external_review.paperreview_ai。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (2026-05-21 01:19 → 01:23, 约 4 分钟)\n\n| 严重性 | 数量 | 关键发现 |\n|--------|------|----------|\n| Critical | 1 | 主正文溢出至第 9 页，>80% 空白（与 MF3 一致）|\n| Warning | 6 | (1) Pages 1-2 连续纯文本无 display item，缺少视觉锚点；(2) Pages 4-5 同样无 display item；(3) Pages 6-7 全部 5 个 table 集中形成\"表格墙\"；(4) Page 8 有 4 个 section header 堆叠，给人草率收尾印象；(5) 主正文仅 1 个 figure + 5 个 table，无实验结果可视化图；(6) Appendix Figure 3 红绿色对色盲不友好 |\n| Info | 8 | Figure 1 建议提前到 p1-2；booktabs 表格质量良好；引用格式正常；Appendix 图表可读性好 |\n\n**视觉审查总评**：主正文 display item 分布严重不均（pages 1-5 无图表 → pages 6-7 表格密集 → page 8-9 section 堆叠+溢出），阅读节奏失调。建议将 Figure 2/3 从 Appendix 移入主文以平衡视觉密度，同时压缩 §6/§7 解决页数溢出。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5（Findings）**\n\n**EMNLP 2026 ARR 评分对照：3 = Findings（可被 Findings 接收）**\n\n**Confidence：4/5**（两位 Reviewer 均为 4/5）\n\n### 评分理由\n\n**支撑 Findings 接收的因素：**\n- Decidability taxonomy + Proposition 1 是该领域首次将 IE 约束映射到形式语言理论的尝试，有独立理论价值\n- 实验评估覆盖面广（3 数据集 × 4 模型 × 多解码策略 × zero-shot/fine-tuning），ablation 设计精良\n- DR near-elimination（94-100%）+ R-F1 不显著下降的核心结果可靠（bootstrap 检验）\n- Fine-tuning composability 验证有实际部署价值\n- 附录（24 页）和统计实践远超同类投稿\n\n**阻碍 Conference 接收的因素：**\n- [最关键] 完全缺失与 GCD/BoostCD/CRANE 等同类方法的实验对比——边际贡献无法量化。此问题已连续 4 轮被标记，始终未以 head-to-head 实验方式解决。\n- \"Guarantee\" 措辞系统性 overclaiming——Abstract/Intro 承诺的保证水平与 fallback 机制、Level 3 缺口、残余 CF 的实际情况不匹配\n- 新颖性主要在 formalization + informed system design 层面，组件级创新有限（grammar layer = XGrammar 应用，semantic layer = 运行时类型检查）\n- WikiEvents 20-doc fine-tuning 评估统计功效不足，κ̄ 基于 n=6 无统计推断力\n- 正文超 8 页限制（回归问题）\n\n**提升至 Borderline Conference（3.5）的路径：**\n1. 至少在 SciERC 上与 GCD 做显式数值对比（可以基于 grammar-only ablation 论证等价性，但必须显式化）\n2. 将 \"guarantee\" 全面替换为 \"enforcement\"/\"near-elimination\"，Abstract/Intro 措辞与 Limitations 对齐\n3. 修复页数溢出\n4. 在 Abstract/Intro 中并列报告 DR reduction 和 CF introduction\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"formal guarantees at each level\"（p2, contribution 1）→ 应改为 \"formal enforcement with best-effort semantics\"\n- κ̄ 在 contribution 1 中的权重应降低——合并到实验评估子点而非独立列出\n- \"applicable to autoregressive LMs with logits access\"（Abstract）→ 建议限定为 \"validated on 7-8B scale models with preliminary 70B results\"\n\n### §3 Method\n- Enabling dependency（§3.1 Corollary）在主文中仅用自然语言描述，缺少正式定义\n- Grammar-first fallback（§4）的 cascade 效应未分析：fallback-induced 类型错误是否传播到后续 triple\n\n### §4 Constraint Composition\n- Fallback 触发率（first-token 0.5-5.7% ZS, ≤0.11% FT）已报告，但应追踪 residual DR violations 到 fallback positions\n- 建议增加 \"net violation change\"（ΔDR+ΔCF）作为 Table 1 的补充列\n\n### §5 Experiments\n- Table 1 \"Tgt.\" 列含义未在正文或表注中解释\n- SciERC Llama CF=12.02% 应在主文而非仅 Limitations 中讨论\n- DocRED beam search 50-doc subset（§5.3）代表性需论证或补充 full-set 结果\n- WikiEvents §5.4 应增加 EE schema 约束编译过程与 RE 差异的讨论\n\n### §6 Related Work\n- grammar-only ablation 与 GCD 的等价性论证应在此节显式化\n- BoostCD 的差异（constrained+unconstrained 混合 vs OntoCoDec 的 pure enforcement）应更清晰地论述\n\n### §7 Discussion and Conclusion\n- 压缩至第 8 页内（当前溢出 ~8 行）\n- 建议增加 \"Our contribution is not a new decoding algorithm, but a formal analysis that reveals the necessity of a two-layer design\" 等 novelty 定位声明\n\n### Limitations\n- 增加语言覆盖缺口讨论（仅英语数据集，continuation masking 对非空格语言的影响）\n- 增加 70B scale 验证有限的明确说明\n\n### Format\n- 清理 orphan bib entries（chen2024agentre, fan2024fsn）\n- 核实 Abstract \"1-2% even after LoRA fine-tuning\" 与 Table 2 数据的一致性\n- Figure 3（Appendix）红绿色对色盲不友好，建议改用 Okabe-Ito 色板\n",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1548 · 2026-05-21T01:38:51.463354+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4476
}
```

</details>

---


### Assistant

_source line 1549 · 2026-05-21T01:39:06.625228+00:00_

审稿报告已投递至 Research Director。

---

**R15 审稿完成汇报：**

**Overall：3.0 / 5（Findings）** — 两位 Reviewer 评分一致，圆桌交叉分享后关键问题全部达成共识。

**核心结论：**
- 论文最大亮点是 decidability taxonomy + Proposition 1 的理论贡献，实验评估覆盖面和统计实践远超同类投稿
- **最关键短板**：连续 4 轮（R12-R15）缺失与 GCD/BoostCD 等同类 constrained decoding 方法的实验对比，边际贡献无法量化
- 次要问题："guarantee" overclaiming、正文超 8 页（回归）、DR↔CF trade-off 选择性报告、WikiEvents n=20 统计功效不足
- 提升至 3.5（Borderline Conference）的路径：显式化 GCD 对比 + 修正 overclaiming + 修复页数 + CF 并列报告

**Issue Tracker 已同步更新**（15 个活跃 issue：3 must-fix + 5 major + 3 should-fix/warning + 4 minor/info）。视觉审查结果已拼入报告（1 critical + 6 warning）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 115

## Round 115

2 recorded events


### User

_source line 1550 · 2026-05-21T01:39:08.133700+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 4 个 Must-Fix 和 5 个 Should-Fix 逐条回应：

- **N1 (缺 baseline 对比)**: [AGREE]，但补充指出 grammar-only ablation 隐含了 GCD 对比
- **N2 ("guarantee" 措辞)**: [AGREE]，与我的发现一致
- **N3 (WikiEvents 不足)**: [AGREE]，与我的 W3 一致
- **N4 (70B 评估)**: [REBUT]，认为应降为 Should-Fix——Abstract 是适用范围声明而非性能保证，Table 4 已有 70B 数据
- **W1-W5**: 4 个 AGREE，1 个部分 REBUT (W3 S1/S2 选择已在 §5.1 有三维度对比)

两位 reviewer 在 Overall 3.0 (Findings)、Soundness 3.5、κ̄ 样本不足、WikiEvents 初步性、页数超限等核心判断上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1551 · 2026-05-21T01:39:25.338220+00:00_

审稿报告已投递至 Research Director。

**R15 审稿完成汇总：**

| 项目 | 结果 |
|------|------|
| **Overall** | **3.0 / 5（Findings）** |
| **Confidence** | 4/5 |
| **Reviewers** | 2 人，1 轮独立审稿 + 1 轮交叉分享 |
| **共识率** | 10/14 问题完全共识，4 个严重性分歧（均已 Director 裁定） |

**关键判定：**
- **Must-Fix 3 项**：(1) 缺少 GCD/BoostCD 实验对比 [critical, 连续 4 轮]；(2) "guarantee" overclaiming [critical]；(3) 正文超 8 页 [major, 回归]
- **Should-Fix 8 项**：novelty 定位、DR↔CF 选择性报告、WikiEvents n=20、κ̄ 定位过高、70B preliminary、fallback tracing、英语覆盖、post-hoc 对比公平性
- **提升至 3.5 的路径**：显式化 GCD 对比 + 修正 overclaiming + 修复页数 + DR/CF 并列报告

Issue Tracker 已同步更新（`review_issues.yaml`），视觉审查结果已纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 116

## Round 116

122 recorded events


### User

_source line 1552 · 2026-05-21T02:22:45.524947+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1553 · 2026-05-21T02:22:52.174704+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1554 · 2026-05-21T02:22:52.326265+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1555 · 2026-05-21T02:22:57.702515+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1556 · 2026-05-21T02:22:57.753312+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1557 · 2026-05-21T02:23:02.581539+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1558 · 2026-05-21T02:23:02.632131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1559 · 2026-05-21T02:23:05.446441+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1560 · 2026-05-21T02:23:06.812735+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (126 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| r14_llama_docred_beam4_998 | Beam=4 S1 constrained on full DocRED 998-doc with Llama-3.1-8B will confirm DR elimination and R-F1 stability seen in 50-doc subset, providing second model evidence for SF3 | — | — | — |\n| r14_qwen_docred_beam4_998 | Beam=4 S1 constrained on full DocRED 998-doc test set will show consistent DR elimination and R-F1 stability compared to 50-doc subset, addressing reviewer concern about subset representativeness | — | — | — |\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- d066_sweep_llama_docred_beam4_s1（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_sweep_llama_scierc_beam8_s1_551** (success): d066 SciERC beam sweep: Llama beam8 constrained (full_s1) on 551-sentence test set. Last Llama SciERC config. ← 基于 d066_beam_sweep\n- **d066_swee
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 1561 · 2026-05-21T02:23:06.863755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1562 · 2026-05-21T02:23:06.864401+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 4778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1563 · 2026-05-21T02:23:12.851819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1564 · 2026-05-21T02:23:12.902601+00:00_

100	
101	This work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.
102	No human subjects were involved in the experiments.
103	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
104	Code and data will be released upon acceptance.
105	
106	% === ARR Responsible NLP Research Checklist ===
107	\input{checklist}
108	
109	% === Bibliography ===
110	\bibliography{relwork_new_entries}
111	
112	% === Appendix ===
113	\appendix
114	
115	\input{appendix_prompts}
116	\input{appendix_related_work}
117	\input{appendix_discussion}
118	\input{appendix_llama_per_relation}
119	\input{appendix_sampling_table}
120	\input{appendix_beam_search}
121	\input{appendix_reproducibility}
122	\input{appendix_doc_length}
123	\input{appendix_prompt_sensitivity}
124	\input{appendix_case_studies}
125	\input{appendix_scalability}
126	\input{appendix_full_ft}
127	\input{appendix_tcr}
128	\input{appendix_kappa_case_study}
129	\input{appendix_pumping_lemma}
130	
131	\end{document}
132	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1565 · 2026-05-21T02:23:13.305620+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1566 · 2026-05-21T02:23:13.457053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1567 · 2026-05-21T02:23:16.472258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-21T02:23:16.824242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit guidelines"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-21T02:23:24.661044+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here is information about ACL Rolling Review 2026 submission format and page limit guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

Review versions of short p
…[truncated 979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7836
}
```

</details>

---


### Tool result

_source line 1570 · 2026-05-21T02:23:28.879971+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 call for papers with ARR submission guidelines and author instructions:

## Key Conference Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, 
…[truncated 2488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 12407
}
```

</details>

---


### Tool call

_source line 1571 · 2026-05-21T02:23:36.633551+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1572 · 2026-05-21T02:23:36.634059+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1573 · 2026-05-21T02:23:39.502538+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/abstract*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/abstract*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 1574 · 2026-05-21T02:23:39.804706+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1575 · 2026-05-21T02:23:40.267438+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1576 · 2026-05-21T02:23:40.719807+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1577 · 2026-05-21T02:23:41.172298+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1578 · 2026-05-21T02:23:41.223420+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1579 · 2026-05-21T02:23:43.936659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1580 · 2026-05-21T02:23:44.439883+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} near-eliminates DR (94--100\% reduction) with negligible R-F1 impact ($\pm$0.6\,pp) but introduces cross-field (CF) violations as a trade-off (0--9.9\% zero-shot, $\leq$1.2\% fine-tuned; \S\ref{sec:scierc-results}).
7	CF is substantially reduced by beam search under favorable conditions (low $\bar{\kappa}$ or fine-tuned settings).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across four autoregressive LMs (7--70B; 70B evaluated in INT4 only, \S\ref{sec:70b-results}) with logits access and three tokenizer families (up to 96 relation types).
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1581 · 2026-05-21T02:23:44.440265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1582 · 2026-05-21T02:23:44.946151+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R15 Action Matrix dispatched, 2026-05-21
3	
4	# ============================================================
5	# Round 15 Must-Fix
6	# ============================================================
7	
8	- id: "R15-MF1"
9	  summary: "缺少与 GCD/BoostCD/CRANE 等同类 constrained decoding 方法的实验对比（连续 4 轮 R12-R15）"
10	  category: experiment
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 12
14	  last_seen_round: 15
15	  mentions:
16	    - round: 12
17	      reviewers: [1, 2]
18	      note: "R12-SF2: should-fix"
19	    - round: 13
20	      reviewers: [1, 2]
21	      note: "R13-MF3: 升级为 must-fix"
22	    - round: 14
23	      reviewers: [1, 2]
24	      note: "R14-MF1: 连续 3 轮。战略转换为 grammar-only ablation reframed as Level 1 对比"
25	    - round: 15
26	      reviewers: [1, 2]
27	      note: "R15-MF1: R1 critical, R2 AGREE。grammar-only ablation 隐含 GCD 对比但未显式化。BoostCD head-to-head 仍缺。连续 4 轮未解决。"
28	  action_items:
29	    - round: 14
30	      action: "grammar-only ablation reframed as BoostCD-equivalent Level 1"
31	      assigned_to: paper_agent
32	      status: completed
33	    - round: 15
34	      action: "§5 新增显式对比小节：Grammar-only=GCD/BoostCD equivalent, 24% vs 94% DR reduction 数据，任务不可比说明"
35	      assigned_to: paper_agent
36	      status: in_progress
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: "R15-MF2"
41	  summary: "Abstract/Intro 中 'guarantee' 措辞与 fallback 机制存在系统性 overclaiming"
42	  category: framing
43	  severity: critical
44	  status: in_progress
45	  first_raised_round: 14
46	  last_seen_round: 15
47	  mentions:
48	    - round: 14
49	      reviewers: [1, 2]
50	      note: "R14-MF2: fallback 36.6% 触发率。FT fallback ≤0.11% 已补充。"
51	    - round: 15
52	      reviewers: [1, 2]
53	      note: "R15-MF2: R1 critical, R2 AGREE。三层保证缺口：(a) grammar-first fallback 跳过 semantic layer；(b) Level 3 未强制；(c) 残余 CF。Abstract 'formal guarantees' 与 §3.3 'best-effort' 矛盾。"
54	  action_items:
55	 
…[truncated 13562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1583 · 2026-05-21T02:23:44.997297+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "section*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "section*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 1584 · 2026-05-21T02:23:45.048009+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1585 · 2026-05-21T02:23:55.500079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1586 · 2026-05-21T02:23:55.802019+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption; type violation elimination ensures ontological consistency of constructed KGs independent of extraction F1, making reliable constraint enforcement necessary.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
16	Training-based approaches~\cite{s
…[truncated 2783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1587 · 2026-05-21T02:23:55.953173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1588 · 2026-05-21T02:23:56.756939+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types ($a_i \in \{
…[truncated 7166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1589 · 2026-05-21T02:23:56.757598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1590 · 2026-05-21T02:23:56.808332+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 5249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1591 · 2026-05-21T02:23:57.310852+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1592 · 2026-05-21T02:23:57.361765+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 79\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1593 · 2026-05-21T02:24:03.096519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1594 · 2026-05-21T02:24:03.599919+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrrr rr@{}}
20	\toprule
21	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-7} \cmidrule(l){8-9}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10  & 18.56
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07  & 26.24
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05  & 14.89
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57  & \textbf{12.78}
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Tot.\ = DR + CF (total type-violation burden).
54	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
56	Grammar-only $\uparrow$DR: vocabula
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1595 · 2026-05-21T02:24:03.600472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1596 · 2026-05-21T02:24:04.204134+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 1206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1597 · 2026-05-21T02:24:04.254978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1598 · 2026-05-21T02:24:04.255531+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction}
8	\label{sec:wikievents}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42	  & Uncon
…[truncated 2383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1599 · 2026-05-21T02:24:05.110921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 1600 · 2026-05-21T02:24:05.563498+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints via a decidability-guided two-layer architecture.
4	LoRA + greedy S1 achieves DR\,$\leq$\,0.09\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC under favorable conditions (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	Beam search substantially reduces CF under fine-tuned conditions; evaluation covers primarily 7--8B models with preliminary 70B results.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1601 · 2026-05-21T02:24:05.714625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1602 · 2026-05-21T02:24:05.766988+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	For relation $r$:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	The mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness: SciERC ($\bar{\kappa}{=}0.333$) achieves 94--99\% DR reduction vs.\ DocRED ($\bar{\kappa}{=}0.842$) at 42--90\%; entity type confusability is a critical co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}).
26	
27	\paragraph{Greedy limitation and 
…[truncated 1497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1603 · 2026-05-21T02:24:12.309254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 1604 · 2026-05-21T02:24:12.309864+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (Eq.~\ref{eq:tightness}, \S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field sema
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1605 · 2026-05-21T02:24:12.360509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1606 · 2026-05-21T02:24:12.461657+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but IE type environments accumulate dynamically (\S\ref{sec:composition}).
9	
10	\paragraph{Schema-aware IE.}
11	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
12	
13	\paragraph{Constraint enforcement in IE.}
14	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation; EnriCo~\cite{zaratiana2024enrico}, IterGen~\cite{ugare2025itergen}, and DCCD~\cite{dccd2026} enforce constraints via ASP, backtracking, or draft-conditioning.
15	Grammar-only enforcement (GCD~\cite{geng2023gcd}, BoostCD~\cite{boostcd2025}) achieves only partial DR reduction; the quantitative gap is analyzed in \S\ref{sec:constrained-baselines}.
16	OntoCoDec uses \emph{preventive} forward-only token masking at $O(|V|)$ per step; while constrained decoding can degrade reasoning~\cite{banerjee2025crane,schall2025hiddencost,formattax2026}, extraction tasks are robust to format co
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-21T02:24:12.512415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 1608 · 2026-05-21T02:24:13.517285+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	Beam search ($k{=}4$), following the constrained beam search paradigm~\cite{anderson2017guided}, explores paths satisfying both layers jointly.
11	With LoRA, beam S1 eliminates all four violation types on SciERC for both models (R-F1 44--47); under zero-shot, beam reduces DR to 0\% and CF substantially (9.90\%\,$\to$\,0.53\% Qwen on SciERC; Appendix~\ref{app:beam-search}).
12	DocRED zero-shot beam evaluates on a 50-document subset (compute cost; LoRA beam uses the full 998-document set).
13	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
14	
15	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
16	\paragraph{Preliminary 70B evaluation.}
17	\label{sec:70b-results}
18	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on both SciERC (R-F1 $-$0.03\,pp) and DocRED (R-F1 $+$0.04\,pp), one of three configurations to eliminate DR on DocRED.
19	CF rises to 7.01\% (from 0.07\%), partly because constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
20	
21	\paragraph{Comparison with grammar-constrained approaches.}
22	\label{sec:constrained-baselines}
23	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as grammar-constrained decoding systems such as GCD~\cite{geng2023gcd} and t
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1609 · 2026-05-21T02:24:13.517669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 1610 · 2026-05-21T02:24:13.970162+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), near-eliminating DR (DR\,$\leq$\,0.09\%) with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\times$ latency).
8	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
9	The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations ar
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1611 · 2026-05-21T02:24:14.422537+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_framing.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_framing.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1612 · 2026-05-21T02:24:14.473426+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\\n\\n## Title\\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\\n(D015: \\\"Near-Complete\\\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\\n\\n**D040 Story 升级方向**: 从 \\\"IE-specific constrained decoding\\\" → \\\"universal ontology-constrained structured generation framework\\\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1613 · 2026-05-21T02:24:20.254066+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find external review config",
  "subagent_type": "Explore",
  "prompt": "Search in /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ for any config file (YAML, JSON, TOML) that contains \"external_review\" or \"paperreview_ai\" settings. Also check /home/ubuntu/.agent-ml-research-idea_gen_0509_6/ root level configs. Report the exact setting value for external_review.paperreview_ai.enabled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Find external review config",
    "subagent_type": "Explore",
    "prompt": "Search in /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ for any config file (YAML, JSON, TOML) that contains \"external_review\" or \"paperreview_ai\" settings. Also check /home/ubuntu/.agent-ml-research-idea_gen_0509_6/ root level configs. Report the exact setting value for external_review.paperreview_ai.enabled."
  }
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-21T02:24:31.053004+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-21T02:24:31.154155+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_violation_rate_PREPARING_20260513T173538.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_violation_rate_docred_PREPARING_20260513T173805.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_infra_env_setup_mvp_20260513T173621_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_mvp_docred_20260513T173912_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_scierc_schema_PREPARING_20260513T175817.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_docred_schema_PREPARING_20260513T175818.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_infra_model_download_check_20260513T175841_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_mvp_scripts_20260513T173700_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_infra_cleanup_and_verify_20260513T180057_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_violation_rate_QUEUED_20260513T180605.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_violation_rate_docred_QUEUED_20260513T180605.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0_violation_rate_ALLOCATED_20260513T180609.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/mvp_phase0
…[truncated 13980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-21T02:24:31.355410+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-21T02:24:31.506581+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_idea_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/idea_generator/logs/_index.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_worker_65f849835bd92ce5c5868092b48f6e79.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/hf_xet-1.5.0.dist-info/sboms/hf_xet.cyclonedx.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/markdown_it/port.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pandas/pyproject.toml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/datasets/utils/resources/creators.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/datasets/utils/resources/languages.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/datasets/utils/resources/mu
…[truncated 11675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-21T02:24:34.070660+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-21T02:24:34.272029+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-21T02:24:34.272551+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-21T02:24:49.746459+00:00_

Found 19 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/chats/feishu_group_oc_01fc90ae186a4ed432770f7601995139_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/chats/feishu_group_oc_2216d5b8b87a9472ce204aba11481390_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/chats/worker_research_r12_task3_boostcd_comparison_20260520T174617.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_r12_task3_boostcd_comparison_20260520T174617.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/logs/system.log.1
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/chats/archive/feishu_group_oc_2216d5b8b87a9472ce204aba11481390_director_2
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 15473
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-21T02:24:55.638515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-21T02:24:55.638965+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-21T02:24:56.291773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/CLAUDE.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/CLAUDE.md",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-21T02:24:56.292127+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_director_fb2e5824.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-21T02:24:56.543414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-21T02:24:56.644341+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0509-6
5	  my_token: e9c675257fdaef5ae01da5f96974bc8f35f549c61149512a3294705d8c0ce3fb
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-21T02:24:59.559923+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -maxdepth 2 -name \"*.yaml\" -o -name \"*.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -maxdepth 2 -name \"*.yaml\" -o -name \"*.json\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-21T02:24:59.811867+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/genie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/codeie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/boostcd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/itergen.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/knowcoder.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/gcd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/gollie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/xgrammar.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/crane.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/distill_tmp/picard.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/_last_visual_review.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/llama_docred_full_s1_mt6144_DONE_20260515T150459.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/ee_mistral_wikievents_constrained_DONE_20260517T235250.json
/home/ubuntu/.agent-ml-rese
…[truncated 435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-21T02:24:59.812355+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/approvals.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/approvals.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-21T02:24:59.863168+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-21T02:25:03.138085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/feishu.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/feishu.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-21T02:25:03.339527+00:00_

1	app_id: cli_a974562a09fc9bd4
2	app_secret: TnoVPIk7y33pAcCkOmIHyezsbnEIbWgf
3	bot_name: Auto Research Prod29
4	chats: {}
5	policy:
6	  require_mention: true
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-21T02:25:03.390841+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml | grep -A 20 external"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml | grep -A 20 external"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-21T02:25:03.441636+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-21T02:25:05.254511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-21T02:25:05.657326+00:00_

File content (96279 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-21T02:25:09.681893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1639 · 2026-05-21T02:25:09.683209+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/*.json 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/*.json 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1640 · 2026-05-21T02:25:09.733803+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1641 · 2026-05-21T02:25:09.784438+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-21T02:25:14.893604+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 1 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"external_review\\|paperreview\" {} \\;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 1 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"external_review\\|paperreview\" {} \\;"
  }
}
```

</details>

---


### Tool result

_source line 1643 · 2026-05-21T02:25:14.944326+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-21T02:25:15.246322+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_6/*.json 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_6/*.json 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-21T02:25:15.548396+00:00_

Exit code 2
-rw-r--r-- 1 ubuntu ubuntu 13 May 10 05:08 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-21T02:25:18.162113+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/*.json 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/*.json 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1647 · 2026-05-21T02:25:18.263113+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -maxdepth 1 -type f \\( -name \"config*\" -o -name \"settings*\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -maxdepth 1 -type f \\( -name \"config*\" -o -name \"settings*\" \\)"
  }
}
```

</details>

---


### Tool result

_source line 1648 · 2026-05-21T02:25:18.263595+00:00_

-rw-r--r-- 1 ubuntu ubuntu     90 May 21 02:14 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/_last_visual_review.json
-rw------- 1 ubuntu ubuntu  67860 May 21 01:48 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml
-rw------- 1 ubuntu ubuntu   6513 May 18 17:37 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.yaml
-rw------- 1 ubuntu ubuntu  10950 May 18 12:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml
-rw-r--r-- 1 ubuntu ubuntu   5834 May 20 05:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml
-rw------- 1 ubuntu ubuntu  30712 May 21 01:58 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/mistakes.yaml
-rw------- 1 ubuntu ubuntu 251280 May 20 21:47 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  16795 May 14 21:25 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-21T02:25:18.314203+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-21T02:25:20.478249+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-21T02:25:20.780080+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-21T02:25:20.830908+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml | grep -A 3 \"review\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml | grep -A 3 \"review\""
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-21T02:25:20.933286+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-21T02:25:24.100475+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ --include=\"*.log\" --include=\"*.md\" --include=\"*.yaml\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ --include=\"*.log\" --include=\"*.md\" --include=\"*.yaml\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool call

_source line 1655 · 2026-05-21T02:25:24.303944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview.ai\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/ --include=\"*.yaml\" --include=\"*.json\" --include=\"*.py\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview.ai\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/ --include=\"*.yaml\" --include=\"*.json\" --include=\"*.py\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1656 · 2026-05-21T02:25:24.505485+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_r12_task3_boostcd_comparison_20260520T174617.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01HknMnRUgzmF41nLk5oHy2o","type":"tool_result","content":"170\t5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)\n171\t\n172\t---\n173\t\n174\t## Missing References\n175\t\n176\t1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]\n177\t2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]\n178\t3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]\n179\t4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 GCD baseline 数字 [R1]\n180\t\n181\t---\n182\t\n183\t## External Review (Stanford Agentic Reviewer)\n184\t\n185\t**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n186\t\n187\t---\n188\t\n189\t## Visual Layout Check（非评分项）"}]},"parent_tool_use_id":null,"session_id":"8c461ce8-ead1-4128-af95-6037c90fd3dd","uuid":"84f6ad6a-5d20-4569-afa9-f21f58ba3901","timestamp":"2026-05-20T17:48:20.099Z","tool_use_result":{"type":"text","file":{"filePath":"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md","content":"5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)\n\n---\n\n## Missing References\n\n1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]\n2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]\n3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]\n4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 G
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 405
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-21T02:25:24.757360+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-21T02:25:28.277007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_director_fb2e5824/CLAUDE.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_director_fb2e5824/CLAUDE.md",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-21T02:25:28.529018+00:00_

1	## 当前项目
2	当前绑定项目：**schema_semantic_constrained_ie**
3	
4	今天是 **2026-05-21**。
5	
6	你是 ML 研究团队的审稿圆桌会议主持人（Review Director）。**始终用中文回复。**
7	
8	## 身份认知
9	
10	你是 AI agent，7×24 运行。你在 Group C（审稿群）主持圆桌审稿会议。你不是投稿人的盟友——你是评审人。
11	
12	## 角色
13	
14	接收 Research Director 提交的论文，主持两名 Reviewer 的多轮圆桌审稿，汇总审稿报告投递回去。
15	
16	**核心立场**：你是评审人，不是投稿人的盟友。审稿报告必须不留情面、严正客观——
17	像顶会最严格的审稿人一样评估论文。
18	你不写论文，不改论文，不给 Research Director 出主意——你只评估和报告。
19	
20	## 通信规则
21	
22	⚠️ 与 Research Director **严格单向通信，禁止对话**：
23	- 输入：`submit_paper_to_review` 提交论文——这是你唯一的输入
24	- 输出：`submit_review_report_to_research_director` 投递审稿报告——这是你唯一的输出
25	- 你们之间没有对话、协商、建议修改方案
26	
27	## 圆桌会议模式
28	
29	你根据 venue 类型和论文特点，**自主决定**需要几名 Reviewer（1-5 人）以及每人的侧重点。
30	
31	使用 `director_post_to_reviewer(reviewer_id="N", round_number=R)` 分配任务。
32	在第一条消息中明确告知每位 Reviewer 的审查侧重。
33	
34	### Reviewer 编排示例
35	
36	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
37	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
38	- **Workshop / 短文**：1 人（全面审查）
39	
40	### 多轮控制（最多 3 轮）
41	
42	- **Round 1**：所有 Reviewer 独立初审
43	- **交叉分享**：将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应（`[AGREE]` / `[REBUT]`）
44	- **收敛判断**：关键问题达成共识 → 汇总报告；存在重大分歧 → 下一轮（附带聚焦问题）
45	
46	### 收敛标准
47	
48	- 关键问题已达成共识（Reviewer 之间不再有未解决矛盾）
49	- 或已达到 3 轮上限（分歧记录在报告中）
50	
51	## 审查流程
52	
53	收到论文后 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 加载完整评审流程。
54	
55	**硬规则**（不可违反）：
56	- **Venue 要求必须实时搜索**：禁止使用训练知识中的 venue 要求，每次都用 web_search 确认
57	- **向 Reviewer 传递 venue 信息**：触发 Reviewer 时必须在消息中包含 venue 名称、deadline、页数、模板、匿名规则
58	
59	## 审稿报告标准
60	
61	报告结构：Summary → Strengths → Weaknesses（重点） → Questions → Missing References → External Review → Visual Layout Check（非评分项） → Overall Assessment → Detailed Comments
62	
63	## 群组
64	
65	你的文字回复发到 Group C（审稿群），用户直接看到。
66	
67	**session 启动时**：`Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 了解投稿状态。
68	
69	## 继续审稿模式 vs 重新审稿模式
70	
71	**继续审稿模式** —— 收到 "[Round N - 继续审稿]" 
…[truncated 6008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-21T02:25:28.529608+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review.paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review.paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-21T02:25:56.166226+00:00_

&lt;persisted-output>
Output too large (371.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-director-fb2e5824/a881ca2b-6fb7-4372-b046-861b7f42edfd/tool-results/b3yb1mu0q.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_r12_task3_boostcd_comparison_20260520T174617.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01HknMnRUgzmF41nLk5oHy2o","type":"tool_result","content":"170\t5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)\n171\t\n172\t---\n173\t\n174\t## Missing References\n175\t\n176\t1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]\n177\t2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]\n178\t3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]\n179\t4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 GCD baseline 数字 [R1]\n180\t\n181\t---\n182\t\n183\t## External Review (Stanford Agentic Reviewer)\n184\t\n185\t**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n186\t\n187\t---\n188\t\n189\t## Visual Layout Check（非评分项）"}]},"parent_tool_use_id":null,"session_id":"8c461ce8-ead1-4128-af95-6037c90fd3dd","uuid":"84f6ad6a-5d20-4569-afa9-f21f58ba3901","timestamp":"2026-05-20T17:48:20.099Z","tool_use_result":{"type":"text","file":{"filePath":"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md","content":"5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)\n\n---\n\n## Missing References\n\n1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的
…[truncated 349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 27636
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-21T02:25:58.377465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md",
  "offset": "170",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md",
    "offset": "170",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-21T02:25:58.428256+00:00_

170	5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)
171	
172	---
173	
174	## Missing References
175	
176	1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]
177	2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]
178	3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]
179	4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 GCD baseline 数字 [R1]
180	
181	---
182	
183	## External Review (Stanford Agentic Reviewer)
184	
185	**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。
186	
187	---
188	
189	## Visual Layout Check（非评分项）
190	
191	**状态**：已完成（2 critical, 4 warning, 10 info）
192	
193	### Critical
194	
195	1. **主文前 4 页无任何 display item**：审稿人打开论文后连续翻过 4 页纯文本+公式才在第 5 页见到首个 Table。对于提出框架的系统论文，缺少架构概览图/流程图是严重的第一印象缺陷。
196	2. **主文（8 页正文）零 Figure**：全文仅有的 3 个 Figure 全部在附录（p20/23/25）。系统/方法论文审稿人期望至少在 Method 部分看到一张框架图展示双层架构、约束编译流程或解码时 masking 工作方式。
197	
198	### Warning
199	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-21T02:26:01.044086+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"enabled\\|config\" {} \\; 2>/dev/null | grep -v \".venv\\|__pycache__\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"enabled\\|config\" {} \\; 2>/dev/null | grep -v \".venv\\|__pycache__\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-21T02:26:05.214408+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/checkpoints/d066_sweep_llama_docred_beam4_s1_QUEUED_20260520T135608.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/checkpoints/d066_sweep_llama_docred_beam4_s1_RUNNING_20260520T135625.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_status_21461_d066_d067_quick_20260520T012030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_writing_d066-pareto-figure_20260520T040015_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_latency_profiling_docred_20260516T091743_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_cf_fallback_code_diff_20260515T154255_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_enrico_itergen_v2_20260518T175005_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_finetuned_feasibility_20260515T140316_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_status_21461_progress_20260520T010644_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ssh_d064_d066_progress_check_20260520T003742_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_mistral_docre
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 4170
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-21T02:26:15.015939+00:00_

Based on my search results, I have found the relevant information about the external_review configuration. Let me provide my findings:

## Search Results

I searched for "external_review" and "paperreview_ai" settings in both the project-level and root-level configuration files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/` and `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/`.

**Finding:** No dedicated config file exists with an `external_review.paperreview_ai.enabled` setting in YAML, JSON, or TOML format.

However, the setting is **documented in the project documentation and review reports**. Specifically:

**Configuration Setting Value:**
- **Status**: NOT CONFIGURED / NOT SET
- **Location documented in**: 
  - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_director_fb2e5824/CLAUDE.md` (line 82)
  - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md` (line 185)

**Exact documented statement** (from round_12.md, line 185):
```
**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。
```

**Translation**: "Status: Not configured. The setting `external_review.paperreview_ai.enabled` is not set in the project config; external review was not requested this round."

**The exact setting value for `external_review.paperreview_ai.enabled`**: **Not set / Not configured / Undefined** (no explicit value exists)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Agent",
  "elapsed_ms": 114761
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-21T02:26:40.515903+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1668 · 2026-05-21T02:27:05.231901+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24715
}
```

</details>

---


### Tool call

_source line 1669 · 2026-05-21T02:27:05.282900+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验评估**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **类别**: Long Paper (ARR)\n- **格式要求**: 正文 ≤8 页（严格），参考文献不限页数，Limitations 和 Ethics 不计入页数，ACL 模板（\\usepackage[review]{acl}），double-blind 匿名审稿\n- **Deadline**: 2026-05-25\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- **Proposition 1 证明**: 检查 decidability 分析的正确性——PDA 不能 enforce IE type constraints 的论证是否严密？pumping lemma proof (Appendix) 是否正确？\n- **两层架构设计**: grammar layer + semantic layer 的 enabling dependency 论证是否充分？Corollary 的 \"enabling dependency\" 定义是否形式化？\n- **Grammar-first fallback**: fallback 机制是否会破坏 type validity guarantee？zero-shot 36.6% token-level fallback rate vs FT ≤0.11%——这个差距的含义和影响\n- **Constraint tightness κ̄**: 作为 descriptive metric 是否合理？n=6 数据点是否足以支撑任何结论？\n- **Continuation masking**: tokenizer-agnostic 的声称是否有充分验证？\n\n### 2. 实验评估\n- **Ablation 设计**: 五路消融（unconstrained/grammar/semantic/S1/S2）是否充分隔离各因素？\n- **统计显著性**: bootstrap 检验是否正确应用？置信区间报告是否完整？\n- **Baseline 对比**: 是否与同类 constrained decoding 方法（GCD、BoostCD、CRANE）有充分实验对比？grammar-only ablation 作为 GCD equivalent 的论证是否成立？\n- **DR↔CF trade-off**: CF 增加（最高 12.02%）是否被充分讨论和量化？\"near-eliminates DR\" 的措辞是否与 CF 代价一致？\n- **WikiEvents**: 20-doc test set 的统计功效是否足以支撑 composability 结论？\n- **70B 评估**: 仅 INT4 推理，无 ablation/FT，是否足够？\n- **DocRED**: zero-shot DR 仅降 45%（vs SciERC 94%），残差 10.21% 是否被充分解释？\n- **Post-hoc filtering 对比**: discard vs correction 的公平性\n- **跨语言**: 仅英语数据集的限制是否在 Limitations 中充分讨论？\n\n### 3. 评分标准（EMNLP 2026 ARR）\n- 5 = Consider for Award（约前2.5%）\n- 4 = Conference（可被主会议接收）\n- 3.5 = Borderline Conference\n- 3 = Findings\n- 2.5 = Borderline Findings\n- 2 = Resubmit next cycle\n\n请给出：Summary → Strengths → Weaknesses（按 Must-Fix / Major / Minor 分级） → Questions → Missing References → Soundness (1-5) → Excitement (1-5) → Overall Assessment (1-5) → Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验评估**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **类别**: Long Paper (ARR)\n- **格式要求**: 正文 ≤8 页（严格），参考文献不限页数，Limitations 和 Ethics 不计入页数，ACL 模板（\\usepackage[review]{acl}），double-blind 匿名审稿\n- **Deadline**: 2026-05-25\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- **Proposition 1 证明**: 检查 decidability 分析的正确性——PDA 不能 enforce IE type constraints 的论证是否严密？pumping lemma proof (Appendix) 是否正确？\n- **两层架构设计**: grammar layer + semantic layer 的 enabling dependency 论证是否充分？Corollary 的 \"enabling dependency\" 定义是否形式化？\n- **Grammar-first fallback**: fallback 机制是否会破坏 type validity guarantee？zero-shot 36.6% token-level fallback rate vs FT ≤0.11%——这个差距的含义和影响\n- **Constraint tightness κ̄**: 作为 descriptive metric 是否合理？n=6 数据点是否足以支撑任何结论？\n- **Continuation masking**: tokenizer-agnostic 的声称是否有充分验证？\n\n### 2. 实验评估\n- **Ablation 设计**: 五路消融（unconstrained/grammar/semantic/S1/S2）是否充分隔离各因素？\n- **统计显著性**: bootstrap 检验是否正确应用？置信区间报告是否完整？\n- **Baseline 对比**: 是否与同类 constrained decoding 方法（GCD、BoostCD、CRANE）有充分实验对比？grammar-only ablation 作为 GCD equivalent 的论证是否成立？\n- **DR↔CF trade-off**: CF 增加（最高 12.02%）是否被充分讨论和量化？\"near-eliminates DR\" 的措辞是否与 CF 代价一致？\n- **WikiEvents**: 20-doc test set 的统计功效是否足以支撑 composability 结论？\n- **70B 评估**: 仅 INT4 推理，无 ablation/FT，是否足够？\n- **DocRED**: zero-shot DR 仅降 45%（vs SciERC 94%），残差 10.21% 是否被充分解释？\n- **Post-hoc filtering 对比**: discard vs correction 的公平性\n- **跨语言**: 仅英语数据集的限制是否在 Limitations 中充分讨论？\n\n### 3. 评分标准（EMNLP 2026 ARR）\n- 5 = Consider for Award（约前2.5%）\n- 4 = Conference（可被主会议接收）\n- 3.5 = Borderline Conference\n- 3 = Findings\n- 2.5 = Borderline Findings\n- 2 = Resubmit next cycle\n\n请给出：Summary → Strengths → Weaknesses（按 Must-Fix / Major / Minor 分级） → Questions → Missing References → Soundness (1-5) → Excitement (1-5) → Overall Assessment (1-5) → Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1670 · 2026-05-21T02:27:27.823730+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22540
}
```

</details>

---


### Tool call

_source line 1671 · 2026-05-21T02:27:29.345067+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式合规**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **类别**: Long Paper (ARR)\n- **格式要求**: 正文 ≤8 页（严格），参考文献不限页数，Limitations 和 Ethics 不计入页数，ACL 模板（\\usepackage[review]{acl}），double-blind 匿名审稿\n- **Deadline**: 2026-05-25\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **核心贡献定位**: \"systematic engineering contribution with theoretical grounding\" 是否足以支撑 EMNLP main conference？这是系统集成还是算法创新？\n- **Proposition 1**: 形式化证明 IE type constraints 超出 CFG expressiveness——这是 motivation 还是独立理论贡献？结论是否 trivially obvious？\n- **κ̄ (constraint tightness)**: 定义为 1 - |σ(r)|/|E|²，n=6 数据点。是独立贡献还是 diagnostic metric？在 §1 contribution list 中的定位是否过高？\n- **与已有工作的区分**: 相对于 GCD、BoostCD、CRANE、GoLLIE、EnriCo、TANL、REBEL 等，OntoCoDec 的独特贡献是什么？增量 novelty 是否足够？\n- **两层架构**: grammar (XGrammar) + semantic (entity registry + dynamic masking) 的组合是否有足够技术深度？\n\n### 2. 完整性评估\n- **Claims 与证据匹配**: Abstract/Introduction 中的每个 claim 是否都有实验数据支撑？特别注意：\n  - \"near-eliminates DR\" 但 CF 最高 12.02%——是否选择性报告？\n  - \"94-100% DR reduction\" 在 Abstract 但 DocRED zero-shot 仅 45%\n  - \"1-2% even after LoRA fine-tuning\" 与 Table 2 数据的一致性\n  - \"formal guarantees\" vs \"best-effort\" 措辞矛盾\n- **实验覆盖的缺口**: \n  - 仅英语数据集\n  - 仅 LoRA 一种 fine-tuning 方法\n  - WikiEvents 仅 20-doc test set\n  - 70B 仅 INT4 推理\n  - 无 head-to-head baseline comparison with BoostCD/GCD（grammar-only ablation 是否等价？）\n- **Related Work 完整性**: 是否遗漏重要相关工作？主文 §6 仅 1/3 页是否过于压缩？\n- **Limitations 充分性**: 是否如实报告所有限制？跨语言泛化是否提及？\n\n### 3. 格式合规（EMNLP 2026 硬性要求）\n- **页数**: 正文是否 ≤8 页？结论是否溢出到第 9 页？（之前 R13/R15 已标记此问题回归）\n- **匿名性**: 是否有匿名违规？检查作者标识、仓库链接、致谢等\n- **参考文献格式**: 是否使用 natbib？bib entries 是否完整？是否有 orphan entries？\n- **Checklist**: ARR Responsible NLP Research Checklist 是否包含？\n- **图表质量**: Figure 1 信息密度、Table caption 完整性\n- **ACL 模板**: \\usepackage[review]{acl} 是否正确使用？\n\n### 4. 评分标准（EMNLP 2026 ARR）\n- 5 = Consider for Award（约前2.5%）\n- 4 = Conference（可被主会议接收）\n- 3.5 = Borderline Conference\n- 3 = Findings\n- 2.5 = Borderline Findings\n- 2 = Resubmit next cycle\n\n请给出：Summary → Strengths → Weaknesses（按 Must-Fix / Major / Minor 分级） → Questions → Missing References → Novelty (1-5) → Completeness (1-5) → Overall Assessment (1-5) → Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式合规**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **类别**: Long Paper (ARR)\n- **格式要求**: 正文 ≤8 页（严格），参考文献不限页数，Limitations 和 Ethics 不计入页数，ACL 模板（\\usepackage[review]{acl}），double-blind 匿名审稿\n- **Deadline**: 2026-05-25\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **核心贡献定位**: \"systematic engineering contribution with theoretical grounding\" 是否足以支撑 EMNLP main conference？这是系统集成还是算法创新？\n- **Proposition 1**: 形式化证明 IE type constraints 超出 CFG expressiveness——这是 motivation 还是独立理论贡献？结论是否 trivially obvious？\n- **κ̄ (constraint tightness)**: 定义为 1 - |σ(r)|/|E|²，n=6 数据点。是独立贡献还是 diagnostic metric？在 §1 contribution list 中的定位是否过高？\n- **与已有工作的区分**: 相对于 GCD、BoostCD、CRANE、GoLLIE、EnriCo、TANL、REBEL 等，OntoCoDec 的独特贡献是什么？增量 novelty 是否足够？\n- **两层架构**: grammar (XGrammar) + semantic (entity registry + dynamic masking) 的组合是否有足够技术深度？\n\n### 2. 完整性评估\n- **Claims 与证据匹配**: Abstract/Introduction 中的每个 claim 是否都有实验数据支撑？特别注意：\n  - \"near-eliminates DR\" 但 CF 最高 12.02%——是否选择性报告？\n  - \"94-100% DR reduction\" 在 Abstract 但 DocRED zero-shot 仅 45%\n  - \"1-2% even after LoRA fine-tuning\" 与 Table 2 数据的一致性\n  - \"formal guarantees\" vs \"best-effort\" 措辞矛盾\n- **实验覆盖的缺口**: \n  - 仅英语数据集\n  - 仅 LoRA 一种 fine-tuning 方法\n  - WikiEvents 仅 20-doc test set\n  - 70B 仅 INT4 推理\n  - 无 head-to-head baseline comparison with BoostCD/GCD（grammar-only ablation 是否等价？）\n- **Related Work 完整性**: 是否遗漏重要相关工作？主文 §6 仅 1/3 页是否过于压缩？\n- **Limitations 充分性**: 是否如实报告所有限制？跨语言泛化是否提及？\n\n### 3. 格式合规（EMNLP 2026 硬性要求）\n- **页数**: 正文是否 ≤8 页？结论是否溢出到第 9 页？（之前 R13/R15 已标记此问题回归）\n- **匿名性**: 是否有匿名违规？检查作者标识、仓库链接、致谢等\n- **参考文献格式**: 是否使用 natbib？bib entries 是否完整？是否有 orphan entries？\n- **Checklist**: ARR Responsible NLP Research Checklist 是否包含？\n- **图表质量**: Figure 1 信息密度、Table caption 完整性\n- **ACL 模板**: \\usepackage[review]{acl} 是否正确使用？\n\n### 4. 评分标准（EMNLP 2026 ARR）\n- 5 = Consider for Award（约前2.5%）\n- 4 = Conference（可被主会议接收）\n- 3.5 = Borderline Conference\n- 3 = Findings\n- 2.5 = Borderline Findings\n- 2 = Resubmit next cycle\n\n请给出：Summary → Strengths → Weaknesses（按 Must-Fix / Major / Minor 分级） → Questions → Missing References → Novelty (1-5) → Completeness (1-5) → Overall Assessment (1-5) → Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1672 · 2026-05-21T02:27:31.125289+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1780
}
```

</details>

---


### Assistant

_source line 1673 · 2026-05-21T02:27:35.533362+00:00_

Round 16 审稿已启动：

- **视觉审查 Agent**: 已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验评估）: 已分配
- **Reviewer 2**（新颖性 + 完整性 + 格式）: 已分配

等待两位 Reviewer 独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1674 · 2026-05-21T02:34:21.422846+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 格式合规

---

## 总体评分

**Overall Assessment**: 3.0 / 5 (Findings)
**一句话总结**: 扎实的工程贡献，解决了 IE 中 type violation 的实际问题，但算法新颖性有限、claim 与 evidence 存在可量化的不匹配，且缺少与最直接竞争方法的 head-to-head 对比。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法技术上正确，ablation 设计系统化，bootstrap 统计检验规范；但 abstract 数字与表格数据存在可验证的不一致，"formal guarantee" 措辞与 best-effort fallback 存在张力 |
| Excitement | 2.5/5 | 实际应用价值明确，但方法是已知技术（XGrammar + 有限状态注册表 + logit masking）的领域迁移组合，不会根本改变 IE 研究方向 |
| Reproducibility | 4/5 | 实验设置详尽（Appendix G），prompts 完整（Appendix A），统计检验充分；代码未开源但 checklist 承诺 acceptance 后发布 |
| Confidence | 4/5 | 我仔细核对了所有表格数字与 claim 的一致性，熟悉 constrained decoding 和 IE 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 中 "94–100% DR reduction" 与 Table 2 数据不一致
- 具体位置：Abstract 第 6 行；Table 2（§5.1）
- 问题：Abstract 声称 "Composed with LoRA fine-tuning, OntoCoDec near-eliminates DR (94–100% reduction)"。然而 Table 2 中 Llama-3.1-8B SciERC 的 fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置的实际范围是 92–100%，而非 94–100%。
- 为什么影响接收：这是 Abstract 中的核心定量 claim，可直接验证。数字不准确会严重损害可信度。
- 建议：将 Abstract 改为 "92–100% reduction" 或 "≥92% reduction"；如果要保留 94%，需明确排除 Llama-SciERC 并说明理由。

**N2** [critical] CF 率在 Abstract 中选择性报告，隐藏了非 SciERC 场景的较高 CF
- 具体位置：Abstract 第 6 行 "(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)"；Table 4（§5.3）；Table 5（§5.4）
- 问题：Abstract 通过 "(§5.1)" 将 CF 范围限定为 SciERC 一个数据集，但同一段中提到了 DocRED 和 WikiEvents 的验证。实际上：
  - DocRED zero-shot: Llama CF = **12.02%**（Table 4），远超 "0–9.9%"
  - WikiEvents zero-shot: CF = **14.9–21.1%**（Table 5）
  - 读者很容易将 "(0–9.9%)" 误解为全局范围
- 为什么影响接收：这构成选择性报告（cherry-picking）。CF 是本文方法的核心 trade-off，不完整披露会误导 AC/Reviewer 对方法局限性的判断。
- 建议：Abstract 应报告全数据集范围，如 "CF 0–21.1% zero-shot (dataset-dependent), ≤1.2% fine-tuned"，或至少明确标注 "on SciERC"。

**N3** [critical] 缺少与最直接竞争方法的 head-to-head 实验对比
- 具体位置：§5, §6（Related Work）
- 问题：论文将 grammar-only ablation 作为 GCD/BoostCD 的代理，但 BoostCD 的 boosting mechanism（交替 constrained/unconstrained decoding）是其核心贡献，grammar-only ablation 无法代表。同样，IterGen（backtracking-based semantic constraint）和 EnriCo（ASP-based decoding constraints）是做 semantic-level constrained decoding 的最直接竞品，均未进行实验对比。
- 为什么影响接收：没有 head-to-head comparison，无法判断 OntoCoDec 的相对优势。Reviewer 和 AC 会质疑：既然已有方法也做 semantic constraint enforcement（IterGen via backtracking, EnriCo via ASP），OntoCoDec 的 forward-only masking 相比之下真正好在哪里？只有主观论述没有定量证据。
- 建议：至少与 BoostCD 在 SciERC/DocRED 上做 head-to-head RE 实验（BoostCD 有开源代码）；如 IterGen/EnriCo 不可直接复现，应明确说明不可比原因。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] DocRED zero-shot DR 仅 45%，与论文整体 narrative 存在张力
- 具体位置：Table 3（§5.2）；§1 contribution item 2
- 问题：DocRED zero-shot Full S1 的 DR 从 18.46% 降至 10.21%，相对降幅仅 **45%**，远低于 SciERC 的 94%。论文通过将 zero-shot 定位为 "diagnostic probe"（§5 开头）来弱化此结果，但 zero-shot 正是 constrained decoding 最核心的使用场景——不需要 task-specific training 的即插即用方案。45% 的 DR 降幅意味着仍有过半违规未被消除。
  §1 contribution item 2 说 "yields 94–100%"，但 this 94% 仅来自 SciERC 的 zero-shot 五路 ablation，DocRED zero-shot 的 45% 被排除在外。
- 建议：在 §1 contribution 中诚实报告范围（如 "45–100% depending on schema tightness"）。同时讨论：对 high-κ̄ schema，zero-shot 下 semantic layer 为何效力下降——是 fallback 太频繁还是 entity registry 不准确？

**W2** [major] κ̄ (constraint tightness) 证据不足以支撑其 prominence
- 具体位置：Eq. (3)（§4）；§2 Background
- 问题：κ̄ = 1 − |σ(r)|/|E|² 仅在 n=2 个数据集上验证了相关性（SciERC κ̄=0.333 vs. DocRED κ̄=0.842）。n=2 不足以建立任何统计意义上的相关。§2 将 κ̄ 提升为 Background 概念，§4 给予独立方程编号和段落——这种 prominence 远超 "two data points show a pattern" 的证据强度。
  WikiEvents 有 245 constraints，但未报告 κ̄ 值或其与 AC reduction 的相关。
- 建议：降低 κ̄ 的定位——作为 diagnostic observation 而非 contribution；报告 WikiEvents κ̄ 值；如果要保留 κ̄ 作为有意义的 metric，需要更多数据集（或 per-relation κ(r) 与 per-relation DR 的相关分析）。

**W3** [major] Proposition 1 作为 "贡献" 的定位偏高
- 具体位置：§1 contribution item 1；§3 Proposition 1
- 问题：Proposition 1 证明 IE type constraints 超出 CFG expressiveness。证明本身是正确的（pumping lemma argument, Appendix O, 两个 case 完整）。但这个结论对 formal language theory 背景的读者而言是 **expected** 的——cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理的基本知识（参见 attribute grammars 的经典动机）。论文在 §1 将 Proposition 1 作为第一个贡献列出，且用 "establishing that IE type constraints require runtime state beyond CFG expressiveness" 的措辞暗示这是一个独立理论发现。
- 建议：将 Proposition 1 重新定位为 *motivation*（"we formalize a well-known intuition..."），而非 *contribution*。真正的贡献是实验验证 enabling dependency（grammar-only 24% vs. full 94%），这不需要 Proposition 1 的形式化证明也能成立。

**W4** [major] WikiEvents 评估的可靠性不足以支撑 contribution claim
- 具体位置：§5.4, Table 5；§1 contribution item 2b
- 问题：WikiEvents fine-tuning composability 基于 **20 文档** test set（论文自己承认 "preliminary"）。Per-document variance 极高（Arg-F1 std/mean > 0.5, 35–47% documents scoring zero）。Zero-shot CF 率 14.9–21.1% 显著高于 RE 任务。尽管如此，§1 将 WikiEvents 列为 contribution item 2b ("preliminary event extraction results on WikiEvents demonstrate generalization")。
  用 "demonstrate generalization" 描述一个 20-doc preliminary experiment，claim 强度与 evidence 强度不匹配。
- 建议：保留 WikiEvents 结果但降级为 "exploratory" 或 "case study"；从 contribution list 中移除或用 "initial evidence for" 替代 "demonstrate"。

---

## 小问题（不影响接收）

- **M1**: §1 "0.5–2% even after LoRA fine-tuning" — Table 2 显示 Llama DocRED 是 0.49%，rounded 应为 "~0.5–2%" 或 "0.5–2.0%"，目前是准确的但边界很紧。

- **M2**: Table 3 脚注中 XGrammar 残余 0.03% RV 来自 "chimeric values"（子词 token 拼接错误）——这是 XGrammar 已知 bug 还是 OntoCoDec 集成问题？应简要说明是否已上报/修复。

- **M3**: §6 Related Work 主文仅 ~1/3 页。虽有 Appendix B（~2 页详细版），但主文中三段式（grammar-constrained decoding / schema-aware IE / constraint enforcement in IE）过于压缩，每段都是引用堆叠，缺乏对关键区分点的展开论述。对不看 Appendix 的读者，这降低了 positioning 的说服力。

- **M4**: "formal guarantees" 措辞（§3.3 "pair-based enforcement" 描述）与 "best-effort" fallback（§4 grammar-first fallback）存在术语张力。DR 在 fallback 位置 structurally 无法为零（§4 "all residual DR violations occur exclusively at fallback positions"），所以 "guarantee" 不准确。建议统一为 "best-effort with soft degradation" 或类似表述。

- **M5**: 引用验证结果：`regino2025kgcurator` 和 `formattax2026` 两条引用在 OpenAlex 中未找到匹配。`formattax2026` 标注为 arXiv:2604.03616，可能太新未索引，但应确认存在。8 条 mismatch 均为作者名编码差异（如 `šakota` vs `sakota`），非实质错误。

- **M6**: §1 "zero-shot DR drops 76–99% for calibrated models" — 但 DocRED Mistral 的 DR 降幅 = (57.42−33.20)/57.42 = **42%**。Mistral 被排除为 "boundary condition"，但这个排除条件（"calibrated models"）在 §1 中不够透明。

---

## Missing References

未发现重大遗漏。论文引用覆盖了 constrained decoding、schema-aware IE、post-hoc validation 三个维度的主要工作。Appendix B 的 extended related work 尤为全面。

可能有价值的补充（非必须）：
- Qi et al., 2024 "AutoAct" 或类似的 agentic IE 工作（作为 API-only models 场景的参考）
- 更多关于 attribute grammars 的经典参考（支撑 Proposition 1 的 "well-known" 定位）

---

## 主要优势

1. **问题定义清晰，实用价值明确**：IE 中 domain/range violation 是一个真实存在且系统性的问题（15–18% baseline violation rates），论文精确地量化了问题规模并提供了可操作的解决方案。

2. **Ablation 设计系统化**：五路 ablation（unconstrained / grammar-only / semantic-only / full S1 / full S2）清楚地隔离了各层的贡献，enabling dependency 的实验证据（grammar-only 3% vs. semantic-only 24% vs. full 94%）比 Proposition 1 更有说服力。

3. **Limitations section 异常诚实和全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎回答了 reviewer 想问的所有问题。这是论文最大的优点之一。

4. **统计严谨性**：所有 F1 比较均有 10,000-iteration paired bootstrap，report p-values 和 confidence intervals。DR reduction 在所有 fine-tuned settings 中均 significant (p<0.001)。

5. **跨模型/跨 tokenizer 泛化**：在三种不同 tokenizer 架构（byte-level BPE × 2, SentencePiece）和 4 个模型上验证，证明方法不依赖特定模型架构。

6. **CF↔DR trade-off 的诚实报告**：没有回避 CF 上升的问题，提供了因果分析（fallback positions, GENERIC↔X ambiguity）和缓解方案（beam search, fine-tuning）。

---

## 评分总结

| 维度 | 分数 |
|------|------|
| Novelty | 2.5/5 |
| Completeness | 3.0/5 |
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Overall Assessment | **3.0/5 (Findings)** |
| Confidence | 4/5 |

**主要判断依据**：
- 算法新颖性有限：两层架构是 XGrammar（off-the-shelf）+ 有限状态注册表（dict + lookup + masking）的组合，技术深度不高。
- Proposition 1 正确但 expected，κ̄ 证据不足，均不构成独立贡献。
- 缺少与 BoostCD/IterGen/EnriCo 的 head-to-head 对比是最大实验缺口。
- Abstract 中存在可验证的数字不一致（N1）和选择性报告（N2），损害 credibility。
- 论文的实际价值（解决 IE violation 问题）和工程完整度（ablation + 统计 + 跨模型验证 + 诚实 limitations）适合 Findings 级别。
- 若修复 N1–N3（数字准确性 + 补充 baseline 对比），可重新评估是否达到 Borderline Conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1675 · 2026-05-21T02:34:29.495974+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1676 · 2026-05-21T02:34:32.238121+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：

**Overall: 3.0/5 (Findings)**

三个 Must-Fix 问题：
1. Abstract "94–100% DR reduction" 与 Table 2 不一致（Llama SciERC fine-tuned 实际为 91.9%）
2. CF 率选择性报告（Abstract 仅报 SciERC 的 0–9.9%，隐藏了 DocRED 12.02% 和 WikiEvents 21.1%）
3. 缺少与 BoostCD/IterGen/EnriCo 的 head-to-head 实验对比

四个 Should-Fix 问题：DocRED zero-shot 仅 45% 与整体 narrative 存在张力、κ̄ metric 证据不足（n=2）、Proposition 1 定位偏高、WikiEvents 20-doc 评估不足以支撑 contribution claim。

主要优势：问题定义清晰、ablation 系统化、Limitations 异常诚实、统计严谨、跨模型泛化验证充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1677 · 2026-05-21T02:34:38.352763+00:00_

收到 Reviewer 2 的审稿意见。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 119

## Round 119

6 recorded events


### User

_source line 1678 · 2026-05-21T02:36:59.699989+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：OntoCoDec

## Paper Summary

本文提出 OntoCoDec，一个将 IE 本体（ontology）编译为 token-level 解码约束的两层框架。核心洞察来自可判定性分析（Proposition 1）：IE type constraints 不是 context-free 的（通过 pumping lemma 证明），因此需要分层处理——grammar layer（context-free，处理 JSON 结构和词汇成员关系）和 semantic layer（有状态，处理 domain/range type constraints）。框架在 SciERC、DocRED（关系抽取）和 WikiEvents（事件抽取）上用四个自回归 LM（7B-70B）进行了验证。在 LoRA 微调配置下，DR（domain/range violations）降至 <0.09%，CF（constraint-forced violations）<1.27%；zero-shot 设置下 DR 降低 76-99%（校准模型）。

---

## Summary of Strengths

**S1. 理论驱动的架构设计原则清晰且新颖。** Proposition 1 通过 pumping lemma 证明 IE type constraints 超出 CFG 表达能力（Section 3, Appendix O），为两层架构提供了形式化 justification，而非仅靠工程直觉。这是约束解码文献中少见的理论贡献。Appendix O 的完整证明（pages 32-33）处理了 position-based vs name-based referencing 和 finite entity set 两个关键 subtlety。

**S2. 消融实验设计充分，层间交互分析深入。** 五路消融（Table 1: unconstrained/grammar/semantic/S1/S2）清晰隔离了各因素的贡献。enabling dependency 的发现——grammar-only 仅降 24% DR，semantic-only 仅降 25%，组合后 94-100%——通过实验而非简单声称，令人信服。Appendix C 的 fallback causal tracing（Table 7）进一步提供了机制层面的理解。

**S3. 对 DR↔CF trade-off 的诚实讨论。** Table 8（Appendix C）展示了消除 CF 会导致 DR 增加 15.8× 的根本性权衡。这种对方法固有局限的定量分析难能可贵，优于多数论文的"limitations as afterthought"做法。

**S4. 实用部署导向。** 框架不需要 constraint-specific training，与 LoRA 微调正交组合（Table 2），运行时开销适中（+10-14%），支持三种 tokenizer 家族。beam search 兼容性分析（Appendix F, Table 16）是有价值的工程贡献。

**S5. Appendix 体量大且信息密度高。** 25 页附录涵盖完整证明、per-relation 错误分析（Appendix D）、case studies（Appendix J）、scalability benchmarks（Appendix K）、prompt sensitivity（Appendix I），显著提高了可复现性和可信度。

---

## Summary of Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 缺乏与现有 constrained decoding baseline 的直接实验对比**

- **具体位置**: Section 5 全文, Section 7 (page 8)
- **问题**: 论文声称 grammar-only ablation（Table 1, row 2）"implements the same class of constraints" as GCD (Geng et al., 2023)（Section 5.1, page 6: "our grammar-only ablation... implements the same class of constraints—vocabulary membership via context-free grammars—as grammar-constrained decoding systems such as GCD"）。然而没有任何实验运行 GCD、BoostCD (Sakota et al., 2025) 或 CRANE (Banerjee et al., 2025) 的实际代码。同样，schema-aware IE 系统如 GoLLIE (Sainz et al., 2024) 和 KnowCoder (Li et al., 2024) 仅在 Related Work 中讨论，未进行实验对比。
- **为什么影响接收**: 审稿人无法判断 OntoCoDec 的改进来自 semantic layer 的创新还是实现差异。grammar-only ablation 可能在 tokenizer 处理、grammar compilation 或其他工程细节上与真正的 GCD 不同。对于声称"the 70pp gap demonstrates that Level 1 constraints alone are insufficient"（page 8）的结论，这一gap 是否因为 GCD 本身也有类似的 gap，还是因为 OntoCoDec 的 grammar-only 实现不够优化，读者无从知晓。
- **建议修改方向**: 在 SciERC 上至少运行一个代表性的 constrained decoding baseline（GCD 代码已开源）和一个 schema-aware training approach（GoLLIE），进行直接对比。如果时间不允许全面对比，至少需要解释为什么 grammar-only ablation 是 GCD 的 fair proxy，并讨论可能的实现差异。

**N2 [critical] 约束紧密度 κ̄ 作为预测性指标缺乏统计支撑**

- **具体位置**: Section 4 (page 5), Figure 2 (page 21), Appendix C (page 20)
- **问题**: κ̄ 的线性回归拟合（R² = 0.86）仅基于 n=4 数据点（2 datasets × 2 models，df=2）。Page 20 报告 p=0.07，虽然论文自称"descriptive characterization rather than a confirmatory statistical test"，但 κ̄ 仍被列为三个主要贡献之一（Section 1, contribution 2: "a comprehensive evaluation... including κ̄ as descriptive metric"），并在 Section 4 和 Section 7 (Conclusion) 中被用于支撑关于 schema-dependent effectiveness 的结论性声明。n=4 下任何两变量关系都可能看起来拟合良好——这不构成有意义的证据。
- **为什么影响接收**: 将一个 n=4 的 descriptive observation 包装为 contribution 会误导读者对该指标预测能力的判断。Appendix N (page 32) 的 constraint tightness case study 提供了定性支持，但 per-relation 分析（Table 34）进一步表明 high κ 本身不足以预测 DR 减少（"equal tight relations... show 74.05% DR"），削弱了 κ̄ 作为 summary metric 的解释力。
- **建议修改方向**: (a) 在更多 ontology/dataset 上验证以增加 n（至少 8-10 个数据点），或 (b) 将 κ̄ 从"贡献"降级为"观察"，明确声明它是一个需要未来验证的描述性假说，并从 contribution list 中移除。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [major] DocRED zero-shot DR 仅降 45%（vs SciERC 94%），主文讨论不足**

- **具体位置**: Section 5.2 (page 7), Table 3
- **问题**: DocRED 上 Full S1 将 DR 从 18.46% 降至 10.21%，仅 45% 减幅。详细的四类错误分析（entity type errors 39%, schema coverage gaps 33%, incorrect relation selection 17%, direction reversal 11%）仅出现在 Appendix D（page 24），主文仅给出一段简短讨论。对于在 Abstract 中声称"near-eliminates DR (94-100% reduction)"的论文而言，55% 的 DR violations 在 DocRED 上幸存约束是一个核心发现。
- **建议**: 在主文中移入或总结 Appendix D 的错误分类，解释 DocRED 的独特挑战。同时在 Abstract 中将"94-100%"限定为 fine-tuned setting，因为 zero-shot DocRED 远未达到此水平。

**W2 [major] WikiEvents 评估统计功效不足**

- **具体位置**: Section 5.4 (page 7), Table 5
- **问题**: 仅 20 篇文档的 test set，Clopper-Pearson 95% CI 上界为 5.83%。论文自称"preliminary"（page 7），但仍将其作为 composability 证据列入贡献（Section 1, contribution 2b: "preliminary event extraction results on WikiEvents demonstrate generalization to 245 constraints"）。
- **建议**: 明确将 WikiEvents 标记为 proof-of-concept 而非完整评估。在 contribution list 中降级处理（如"pilot study"而非"demonstrate generalization"）。

**W3 [major] 70B 评估过于单薄**

- **具体位置**: Section 5.4 (page 7, "Preliminary 70B evaluation")
- **问题**: 仅 Llama-3.1-70B (AWQ INT4) 推理，无消融、无微调。CF 从 0.07% 飙升至 7.01%。论文将此与 8B 结果并列展示，但单一配置无法提供两层架构在更大模型上是否 scale 的洞察。INT4 量化本身可能引入额外的 token 分布偏移，与约束系统的交互未被分析。
- **建议**: 要么进行最小消融（至少 grammar-only vs full S1 at 70B），要么明确标注为"feasibility check"，不作为评估结论的组成部分。

**W4 [major] CF 在 Abstract/Conclusion 中的措辞与正文证据不一致**

- **具体位置**: Abstract (page 1), Section 7 (page 8)
- **问题**: Abstract 称"near-eliminates DR (94-100% reduction) with negligible R-F1 impact (<1.68pp)"，将 CF 以"introduces CF side-effects... fine-tuning resolves most CF (<1.27%)"轻描淡写。但在 zero-shot 条件下 CF 可达 12.02%（Table 3, DocRED Llama），且 Table 8（Appendix C）显示 CF 和 DR 是根本性耦合的：消除 CF 导致 DR 增加 15.8×。"near-eliminates" 的表述在 zero-shot DocRED（45% DR reduction + 12% CF）场景下明显过度。Section 7 (Conclusion) 同样仅提"CF <1.2%"（fine-tuned），回避了 zero-shot 的高 CF。
- **建议**: Abstract 和 Conclusion 中应给 CF 与 DR 同等权重。例如："reduces DR by 94-100% under fine-tuning (DR <0.09%) while introducing CF violations (≤1.27% fine-tuned, up to 12% zero-shot), revealing a fundamental DR-CF trade-off (§5.1)."

**W5 [warning] Proposition 1 对无界实体集成立，但实际 IE 操作在有界集上**

- **具体位置**: Section 3 (page 3), Appendix O (pages 32-33)
- **问题**: 论文在 page 33 正确指出对于有限实体集和规范标识符，valid language 是"finite intersection of regular languages"（因此是 regular 的，也是 context-free 的）。对于 SciERC（6 entity types, 20+ entities），DFA 超过 10^17 states，使其"practically infeasible"。这是一个实际不可行性论证，而非形式上的不可能。理论贡献（Proposition 1）关于无界集，而实际贡献（OntoCoDec）操作在有界集上。这个 gap 仅在 Appendix 末尾（page 33）简短提及。
- **建议**: 在主文（Section 3）中添加一句话，明确说明对有限实体集语言在技术上是 regular 的，但状态数呈指数增长使得 CFG/DFA 方法不可行，从而为 OntoCoDec 的实际必要性提供更透明的论证。

### 小问题（不影响接收）

- **M1**: Section 3 (page 3) Corollary 中的 "enabling dependency" 不是标准形式化概念，建议改为 "empirical enabling dependency" 以避免与形式化依赖概念混淆。
- **M2**: Table 1 脚注提到 "DocRED test annotations are not publicly available; we evaluate on the development set." 这一信息应放在主文实验设置中而非脚注。
- **M3**: Figure 3 (page 24) per-relation DR rates 仅使用 Llama-3.1-8B，缺乏跨模型验证。
- **M4**: Page 5 §5 Setup 中 "FT = 100" 和 bootstrap 10,000 iterations 的评估协议描述可以更清晰。
- **M5**: Table 2 caption 中"(555 docs)" 与 Table 1 "(551 docs)" 的 SciERC 文档数不一致——应解释差异原因（推测是 train+dev vs dev only）。

---

## Questions to Authors

1. Grammar-only ablation 是否使用了与 GCD (Geng et al., 2023) 完全相同的 XGrammar 配置和 grammar compilation pipeline？如果存在实现差异，这些差异是否可能解释 grammar-only 的 low DR reduction？
2. κ̄ metric 是否在论文未报告的其他 ontology 上进行过验证？如果有更多数据点，linear fit 的 R² 是否仍然保持？
3. 70B 模型上 CF 飙升至 7.01% 的原因是什么？是量化（INT4）引入的 token 分布偏移，还是更大模型本身与约束系统有不同的交互模式？
4. 对于 DocRED 上 39% 的 entity type errors（即模型给出了错误的 entity type），semantic layer 是否有可能通过更 aggressive 的 masking 来减少这类错误，代价是更高的 CF？

---

## Missing References

引用验证结果：60 条 bib entries 全部被引用，0 orphan/0 missing。50 条 OpenAlex 验证通过，2 条（regino2025kgcurator, formattax2026）因过新未收录，8 条为作者名编码差异（非实际错误）。

可能遗漏的相关工作：
- **IterGen** (Ugare et al., 2025) — 已引用，但仅在 Related Work 中简短提及。IterGen 的 backtracking 机制与 OntoCoDec 的 grammar-first fallback 在解决 constraint conflict 时有相似之处，值得在 Discussion 中更深入对比。
- **SHACL-based LLM validation** — 论文在 Appendix B (page 17) 提到了 SHACL validation 但未给出具体引用。如果有相关工作（如 OntoCo-Q），应给出完整引用。

---

## Limitations and Societal Impact Assessment

Limitations section（page 9）覆盖了 CF trade-off、scalability、evaluation coverage（模型规模、语言）的关键限制。讨论充分且诚实。唯一建议是在 cross-lingual limitation 中具体提及 CJK 语言中 subword tokenization 对 continuation masking 的潜在影响，目前已有提及但可以更具体。

Societal impact 讨论恰当：使用公开数据集，无个人身份信息，约束解码不引入超出基础模型的安全风险。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | Proposition 1 证明基本正确但有 finite/infinite gap；消融设计好；但 κ̄ 统计支撑不足（n=4），且缺乏与 GCD 等系统的直接对比 |
| **Excitement** | 3.5/5 | 可判定性驱动的两层架构是新颖的方法论贡献；CF-DR trade-off 的量化分析有价值；但专用于结构化 IE 输出格式，适用范围有限 |
| **Reproducibility** | 4/5 | 附录详尽（25 pages），三种 tokenizer 验证，bootstrap 检验，代码承诺发布；部分细节（如 DocRED ontology 构建的具体 frequency threshold）需要代码才能完全复现 |
| **Overall Assessment** | **3.5** — Borderline Conference | 两层架构的理论动机和实验验证都达到了相当水平，但两个 critical 问题（缺少直接 baseline 对比、κ̄ 统计支撑不足）限制了贡献的可信度。如果能补充 GCD 直接对比实验并更审慎地处理 κ̄ 的定位，可以达到 4.0 |
| **Confidence** | 4/5 | 我在约束解码和 IE 领域有较深的研究经验，仔细阅读了证明和实验设置，但对某些实现细节（如 XGrammar 的具体编译行为）不完全确定 |

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)

**一句话总结**: 可判定性分析驱动的两层约束解码架构是扎实的方法论贡献，但缺乏与现有 constrained decoding 系统的直接实验对比、以及 κ̄ metric 的统计支撑不足，使得当前版本的贡献可信度不够达到明确的 Conference 接收标准。

## 主要优势
- 理论驱动（pumping lemma proof）的架构设计原则在约束解码文献中稀缺
- 五路消融和 enabling dependency 的实验验证设计良好
- 对 DR↔CF 根本性 trade-off 的诚实和深入分析
- 与 LoRA 微调的正交组合是有实际部署价值的特性
- 附录体量大（25 pages）且信息密度高

## 提升到 Conference (4.0) 的路径
1. 补充 GCD 直接实验对比（最关键）
2. 将 κ̄ 从 contribution 降级为 observation 或增加验证数据点
3. 修正 Abstract/Conclusion 中的 CF 措辞，与正文证据一致


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1679 · 2026-05-21T02:37:37.013393+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R2 是否在关键问题上有共识或分歧。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 中 \"94–100% DR reduction\" 与 Table 2 数据不一致\n- Abstract 声称 \"Composed with LoRA fine-tuning, OntoCoDec near-eliminates DR (94–100% reduction)\"。然而 Table 2 中 Llama-3.1-8B SciERC 的 fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置的实际范围是 92–100%，而非 94–100%。\n\n**N2** [critical] CF 率在 Abstract 中选择性报告\n- Abstract 通过 \"(§5.1)\" 将 CF 范围限定为 SciERC 一个数据集。实际上 DocRED zero-shot Llama CF = 12.02%（Table 4），WikiEvents zero-shot CF = 14.9–21.1%（Table 5），远超 \"0–9.9%\"。\n\n**N3** [critical] 缺少与最直接竞争方法的 head-to-head 实验对比\n- grammar-only ablation 作为 GCD/BoostCD 的代理不充分。BoostCD 的 boosting mechanism 是其核心贡献。同样 IterGen（backtracking）和 EnriCo（ASP）未进行实验对比。\n\n### Should-Fix 问题\n\n**W1** [major] DocRED zero-shot DR 仅 45%，与论文整体 narrative 存在张力\n- 论文通过将 zero-shot 定位为 \"diagnostic probe\" 来弱化此结果，但 zero-shot 正是 constrained decoding 最核心的使用场景。\n\n**W2** [major] κ̄ (constraint tightness) 证据不足\n- κ̄ 仅在 n=2 个数据集上验证了相关性。WikiEvents 有 245 constraints 但未报告 κ̄ 值。\n\n**W3** [major] Proposition 1 作为 \"贡献\" 的定位偏高\n- cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理的基本知识。应重新定位为 motivation 而非 contribution。\n\n**W4** [major] WikiEvents 评估不足以支撑 contribution claim\n- 20 文档 test set，per-document variance 极高。\"demonstrate generalization\" 措辞与 evidence 强度不匹配。\n\n### 优势\n1. 问题定义清晰，实用价值明确\n2. Ablation 设计系统化\n3. Limitations 异常诚实和全面\n4. 统计严谨性\n5. 跨模型/跨 tokenizer 泛化\n6. CF↔DR trade-off 诚实报告\n\n### 评分\n| 维度 | 分数 |\n|------|------|\n| Novelty | 2.5/5 |\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Overall | 3.0/5 (Findings) |\n| Confidence | 4/5 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R2 是否在关键问题上有共识或分歧。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] Abstract 中 \"94–100% DR reduction\" 与 Table 2 数据不一致\n- Abstract 声称 \"Composed with LoRA fine-tuning, OntoCoDec near-eliminates DR (94–100% reduction)\"。然而 Table 2 中 Llama-3.1-8B SciERC 的 fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置的实际范围是 92–100%，而非 94–100%。\n\n**N2** [critical] CF 率在 Abstract 中选择性报告\n- Abstract 通过 \"(§5.1)\" 将 CF 范围限定为 SciERC 一个数据集。实际上 DocRED zero-shot Llama CF = 12.02%（Table 4），WikiEvents zero-shot CF = 14.9–21.1%（Table 5），远超 \"0–9.9%\"。\n\n**N3** [critical] 缺少与最直接竞争方法的 head-to-head 实验对比\n- grammar-only ablation 作为 GCD/BoostCD 的代理不充分。BoostCD 的 boosting mechanism 是其核心贡献。同样 IterGen（backtracking）和 EnriCo（ASP）未进行实验对比。\n\n### Should-Fix 问题\n\n**W1** [major] DocRED zero-shot DR 仅 45%，与论文整体 narrative 存在张力\n- 论文通过将 zero-shot 定位为 \"diagnostic probe\" 来弱化此结果，但 zero-shot 正是 constrained decoding 最核心的使用场景。\n\n**W2** [major] κ̄ (constraint tightness) 证据不足\n- κ̄ 仅在 n=2 个数据集上验证了相关性。WikiEvents 有 245 constraints 但未报告 κ̄ 值。\n\n**W3** [major] Proposition 1 作为 \"贡献\" 的定位偏高\n- cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理的基本知识。应重新定位为 motivation 而非 contribution。\n\n**W4** [major] WikiEvents 评估不足以支撑 contribution claim\n- 20 文档 test set，per-document variance 极高。\"demonstrate generalization\" 措辞与 evidence 强度不匹配。\n\n### 优势\n1. 问题定义清晰，实用价值明确\n2. Ablation 设计系统化\n3. Limitations 异常诚实和全面\n4. 统计严谨性\n5. 跨模型/跨 tokenizer 泛化\n6. CF↔DR trade-off 诚实报告\n\n### 评分\n| 维度 | 分数 |\n|------|------|\n| Novelty | 2.5/5 |\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Overall | 3.0/5 (Findings) |\n| Confidence | 4/5 |"
  }
}
```

</details>

---


### Tool result

_source line 1680 · 2026-05-21T02:37:51.687073+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14673
}
```

</details>

---


### Tool call

_source line 1681 · 2026-05-21T02:37:51.838231+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R1 是否在关键问题上有共识或分歧。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 缺乏与现有 constrained decoding baseline 的直接实验对比\n- grammar-only ablation 声称 \"implements the same class of constraints\" as GCD，但没有运行 GCD、BoostCD 或 CRANE 的实际代码。无法判断改进来自 semantic layer 创新还是实现差异。\n\n**N2** [critical] κ̄ 作为预测性指标缺乏统计支撑\n- 线性回归拟合（R²=0.86）仅基于 n=4 数据点（2 datasets × 2 models, df=2）。p=0.07。per-relation 分析进一步削弱解释力。\n\n### Should-Fix 问题\n\n**W1** [major] DocRED zero-shot DR 仅降 45%，主文讨论不足\n- 详细错误分析仅在 Appendix D。对声称 \"near-eliminates DR\" 的论文而言，55% DR violations 在 DocRED 上幸存是核心发现。\n\n**W2** [major] WikiEvents 评估统计功效不足\n- 20 文档 test set，Clopper-Pearson 95% CI 上界 5.83%。应标记为 proof-of-concept。\n\n**W3** [major] 70B 评估过于单薄\n- 仅 INT4 推理，无消融、无微调。CF 0.07%→7.01%。单一配置无法提供两层架构在更大模型上是否 scale 的洞察。\n\n**W4** [major] CF 在 Abstract/Conclusion 中的措辞与正文证据不一致\n- Abstract 将 CF 以 \"introduces CF side-effects\" 轻描淡写。但 zero-shot CF 可达 12.02%（Table 3），且 CF-DR 是根本性耦合的。\n\n**W5** [warning] Proposition 1 对无界实体集成立，但实际 IE 操作在有界集上\n- 对有限实体集语言在技术上是 regular 的，但状态数呈指数增长使 DFA 不可行。这个 gap 仅在 Appendix 末尾简短提及。\n\n### 小问题 M1-M5\n- M1: \"enabling dependency\" 非标准形式化概念\n- M2: DocRED 使用 dev set 应在主文说明\n- M3: Figure 3 per-relation DR 仅 Llama\n- M4: 评估协议描述可更清晰\n- M5: Table 2 \"(555 docs)\" vs Table 1 \"(551 docs)\" 不一致\n\n### 优势\n1. 理论驱动架构设计原则清晰新颖\n2. 消融实验设计充分\n3. DR↔CF trade-off 诚实讨论\n4. 实用部署导向\n5. Appendix 体量大信息密度高\n\n### 评分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.5/5 (Borderline Conference) |\n| Confidence | 4/5 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你和 R1 是否在关键问题上有共识或分歧。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 缺乏与现有 constrained decoding baseline 的直接实验对比\n- grammar-only ablation 声称 \"implements the same class of constraints\" as GCD，但没有运行 GCD、BoostCD 或 CRANE 的实际代码。无法判断改进来自 semantic layer 创新还是实现差异。\n\n**N2** [critical] κ̄ 作为预测性指标缺乏统计支撑\n- 线性回归拟合（R²=0.86）仅基于 n=4 数据点（2 datasets × 2 models, df=2）。p=0.07。per-relation 分析进一步削弱解释力。\n\n### Should-Fix 问题\n\n**W1** [major] DocRED zero-shot DR 仅降 45%，主文讨论不足\n- 详细错误分析仅在 Appendix D。对声称 \"near-eliminates DR\" 的论文而言，55% DR violations 在 DocRED 上幸存是核心发现。\n\n**W2** [major] WikiEvents 评估统计功效不足\n- 20 文档 test set，Clopper-Pearson 95% CI 上界 5.83%。应标记为 proof-of-concept。\n\n**W3** [major] 70B 评估过于单薄\n- 仅 INT4 推理，无消融、无微调。CF 0.07%→7.01%。单一配置无法提供两层架构在更大模型上是否 scale 的洞察。\n\n**W4** [major] CF 在 Abstract/Conclusion 中的措辞与正文证据不一致\n- Abstract 将 CF 以 \"introduces CF side-effects\" 轻描淡写。但 zero-shot CF 可达 12.02%（Table 3），且 CF-DR 是根本性耦合的。\n\n**W5** [warning] Proposition 1 对无界实体集成立，但实际 IE 操作在有界集上\n- 对有限实体集语言在技术上是 regular 的，但状态数呈指数增长使 DFA 不可行。这个 gap 仅在 Appendix 末尾简短提及。\n\n### 小问题 M1-M5\n- M1: \"enabling dependency\" 非标准形式化概念\n- M2: DocRED 使用 dev set 应在主文说明\n- M3: Figure 3 per-relation DR 仅 Llama\n- M4: 评估协议描述可更清晰\n- M5: Table 2 \"(555 docs)\" vs Table 1 \"(551 docs)\" 不一致\n\n### 优势\n1. 理论驱动架构设计原则清晰新颖\n2. 消融实验设计充分\n3. DR↔CF trade-off 诚实讨论\n4. 实用部署导向\n5. Appendix 体量大信息密度高\n\n### 评分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.5/5 (Borderline Conference) |\n| Confidence | 4/5 |"
  }
}
```

</details>

---


### Tool result

_source line 1682 · 2026-05-21T02:37:53.453285+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1615
}
```

</details>

---


### Assistant

_source line 1683 · 2026-05-21T02:37:56.411515+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1684 · 2026-05-21T02:37:59.167083+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**总结**: 给出 **3.5 (Borderline Conference)** 评分。两个 critical 问题：(1) 缺乏与 GCD 等现有 constrained decoding 系统的直接实验对比——grammar-only ablation 作为 proxy 不够充分；(2) κ̄ metric 仅 n=4 数据点，统计支撑不足以作为贡献。四个 major 问题涉及 DocRED 45% DR residual 的主文讨论不足、WikiEvents 统计功效、70B 评估单薄、以及 Abstract 中 CF 措辞过于乐观。主要优势在于 pumping lemma 驱动的架构设计原则、五路消融的充分性、DR↔CF trade-off 的诚实分析。补充 GCD 直接对比实验是提升到 4.0 的最关键路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1685 · 2026-05-21T02:38:04.148302+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 121

## Round 121

2 recorded events


### User

_source line 1686 · 2026-05-21T02:39:29.999006+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### 逐条回应摘要

| R2 编号 | 级别 | R1 回应 | 对应 R1 编号 | 说明 |
|---------|------|---------|------------|------|
| R2-N1 | critical | **[AGREE]** | (R1 遗漏) | Abstract "94-100%" 与 Table 2 不一致，Llama SciERC 实际 91.9%。有效的事实性核查。 |
| R2-N2 | critical | **[AGREE]** | R1-W4 | CF 选择性报告，WikiEvents CF 14.9-21.1% 未在 Abstract 提及。R2 论证更具体。 |
| R2-N3 | critical | **[AGREE]** | R1-N1 | 缺 baseline 对比。R2 补充了 IterGen 和 EnriCo 作为额外对比对象。 |
| R2-W1 | major | **[REBUT]** | R1-W1 | 同意 DocRED 讨论不足，但反驳 zero-shot 是"最核心场景"——fine-tuned + constrained 是更常见部署模式（cf. PICARD, GCD fine-tuned experiments）。 |
| R2-W2 | major | **[AGREE]** | R1-N2 | κ̄ 证据不足。R2 补充 WikiEvents 未报告 κ̄。我评 critical 而非 major。 |
| R2-W3 | major | **[REBUT]** | — | 部分反驳。Prop 1 的贡献不在 general principle（PDA 不支持 random-access），而在将 IE type constraints 形式化为语言识别问题的具体化工作和完整证明（Appendix O, 2 pages），以及由此推导的三级约束分类。但同意论文应更精确表述其贡献范围。 |
| R2-W4 | major | **[AGREE]** | R1-W2 | WikiEvents 20-doc test set 不足以支撑 generalization claim。 |

### 共识总结
5 项高度共识：缺 baseline 对比、κ̄ 统计不足、DocRED 讨论不足、WikiEvents 功效不足、CF 选择性报告。

### 关键分歧
1. **Proposition 1 定位**：R2 认为应降级为 motivation，我认为形式化本身有 contribution 价值
2. **Zero-shot 重要性**：R2 认为是最核心场景，我认为 fine-tuned 组合更具部署相关性
3. **整体评分**：R1=3.5 vs R2=3.0，差异主要在 Novelty/Excitement（R1=3.5 vs R2=2.5）

### 评分调整考虑
R2-N1 的数值不一致是我遗漏的有效问题。综合考虑后，我维持 Overall 3.5，但认为如果作者不修正 Abstract 数值和 CF 报告，应降至 3.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1687 · 2026-05-21T02:39:36.160267+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1688 · 2026-05-21T02:39:38.855855+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。与 R2 在 5 项核心问题上达成共识（缺 baseline 对比、κ̄ 统计不足、DocRED 讨论不足、WikiEvents 功效不足、CF 选择性报告）。在 Proposition 1 的定位和 zero-shot 重要性上有分歧——我认为形式化证明本身有 contribution 价值，且 fine-tuned + constrained 是更实际的部署场景。R2 发现的 Abstract "94-100%" 数值不一致（实际 92-100%）是我遗漏的有效核查。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1689 · 2026-05-21T02:39:44.203310+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 123

## Round 123

10 recorded events


### User

_source line 1690 · 2026-05-21T02:39:55.730533+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 对 Reviewer 1 的交叉回应

### 逐条回应总结

**Must-Fix:**
- **[AGREE] R1-N1** (缺 baseline 对比): 完全同意，与我的 N3 完全一致。补充：EnriCo (ASP-based) 也应纳入比较。
- **[AGREE] R1-N2** (κ̄ 统计不足): 同意。补充：κ̄ 独立取值仅 n=2（schema 属性不随模型变化），自由度为零，任何回归无意义。WikiEvents 未报告 κ̄ 是遗漏。

**Should-Fix:**
- **[AGREE] R1-W1** (DocRED 45%): 完全同意，与我的 W1 一致。§1 contribution "yields 94–100%" 排除了 DocRED 45% 却未说明。
- **[AGREE] R1-W2** (WikiEvents 20-doc): 同意，与我的 W4 一致。"demonstrate generalization" 应降级为 "initial evidence"。
- **[AGREE] R1-W3** (70B 单薄): 同意。CF 0.07%→7.01% 未充分分析。"7–70B" 范围声明可能给人不恰当的覆盖印象。
- **[AGREE] R1-W4** (CF 措辞不一致): 强烈同意，且认为应**升级为 Must-Fix**。Abstract "(0–9.9% zero-shot)" 仅覆盖 SciERC，但 DocRED CF=12.02%, WikiEvents CF=21.1%。这是选择性报告。
- **[REBUT] R1-W5** (Proposition 1 bounded gap): 部分反驳。Appendix O 已讨论 finite entity sets（exponential DFA + open-vocabulary text spans 使 unbounded 模型更贴近实际）。建议在主文加一句限定即可。我从不同角度（overclaimed positioning）也批评了 Proposition 1。

**Minor:**
- [AGREE] M1, M3, M4
- [REBUT] M2: DocRED dev set 已在主文脚注和 Table 3 caption 中说明
- [未能验证] M5: 我在 LaTeX 源文件中 Table 1 和 Table 2 都看到 "551 docs"，未找到 "555"

### 关键共识与分歧

**强共识**: baseline 对比缺失、DocRED 45%、WikiEvents 20-doc、CF 选择性报告
**分歧**: Excitement（R1: 3.5, R2: 2.5）。R1 更认可理论驱动设计的新颖性，R2 认为 Proposition 1 结论 expected、两层架构技术深度有限。
**R2 独有发现**: Abstract "94–100%" 与 Table 2 Llama-SciERC 91.9% 的数字不一致（N1）

**Overall: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)**
差异根源在 novelty/excitement 判断，soundness 一致 (3.5/5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1691 · 2026-05-21T02:40:13.363906+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-21T02:40:13.364398+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-21T02:40:13.415098+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T02:26:44.751781+00:00\", \"completed_at\": \"2026-05-21T02:30:21.362489+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（Intro + Background），首个视觉锚点延迟到 page 3。审稿人前 2 分钟只看到文字墙，建议考虑将 Figure 1 提前到 page 2 或在 page 1 底部加入一个精简的 teaser figure/table\"}, {\"severity\": \"warning\", \"dimension\": \"page 5-7\", \"message\": \"主文结果部分全部为 table（5 个 table + 0 figure），视觉单调。建议将 appendix 中的 Figure 2（Residual DR vs Schema Restrictiveness 散点图）或 Figure 4（Beam width sweep）提升到主文，打破纯表格节奏，为审稿人提供一个直觉性的 visual takeaway\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（Related Work + Discussion/Conclusion）为纯文本，无视觉锚点收尾。审稿人快速翻到末尾时看不到 strong visual result。若有空间，在 Conclusion 前放一个 key result 的 compact visualization 可强化收尾印象\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 架构图内部组件文字标注偏小（约正文字号的 60-65%），打印时可能需要放大查看。建议适当增大关键标注字号\"}, {\"severity\": \"info\", \"dimension\": \"page 6-7\", \"message\": \"每页堆叠 2 个 table，视觉密度高。Table 2+3（p.6）和 Table 4+5（p.7）之间缺少文字过渡的呼吸空间，审稿人可能感到 information overload\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Table 6（Prompt Templates）含小号等宽字体的 prompt 文本，系统提示词部分在打印尺寸下可读性偏低\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"Table 26 案例分析使用红/绿颜色编码标注 violation/correction，对红绿色盲不友好。建议改用蓝/橙方案或增加下划线/删除线等形态区分\"}, {\"severity\": \"info\", \"dimension\": \"page 22\", \"message\": \"单页含 3 个 table（Table 9 + 10 + 11），appendix 可接受但密度极高\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页中仅 1 个 figure（Figure 1），figure:table 比为 1:5。对于实证为主的 IE 论文，figure 偏少。领域同行论文通常在主文中至少含 2-3 个 figure（架构图 + 结果可视化 + 案例/分析图）\"}, {\"severity\": \"info\", \"dimension\": \"page 11-13\", \"message\": \"References 格式统一，未发现 [?] 未解析引用，无可见格式问题\"}, {\"severity\": \"info\", \"dimension\": \"page 5-7\", \"message\": \"所有 table 使用 booktabs 风格（to
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1694 · 2026-05-21T02:40:13.415526+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1695 · 2026-05-21T02:45:15.978090+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 16 (fresh review), 2026-05-21\n\n# ============================================================\n# Round 16 Must-Fix\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD/CRANE/IterGen/EnriCo 等同类 constrained decoding 方法的实验对比（连续 5 轮 R12-R16）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: should-fix\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF3: 升级为 must-fix\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1: 连续 3 轮。战略转换为 grammar-only ablation reframed as Level 1 对比\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF1: R1 critical, R2 AGREE。grammar-only ablation 隐含 GCD 对比但未显式化。BoostCD head-to-head 仍缺。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16-MF1: 双 Reviewer 再次标记 critical。R2 补充 IterGen (backtracking) 和 EnriCo (ASP) 作为 semantic-level 竞品。grammar-only proxy 论证仍不被接受——BoostCD 的 boosting mechanism 无法被代理。连续 5 轮未解决。\"\n  action_items:\n    - round: 14\n      action: \"grammar-only ablation reframed as BoostCD-equivalent Level 1\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 15\n      action: \"§5 新增显式对比小节：Grammar-only=GCD/BoostCD equivalent, 24% vs 94% DR reduction 数据\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 16\n      action: \"在 SciERC/DocRED 上运行 GCD 代码做 head-to-head 对比（最关键）；如 IterGen/EnriCo 不可复现需说明不可比原因\"\n      assigned_to: agent + paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF2\"\n  summary: \"Abstract '94–100% DR reduction' 与 Table 2 数据不一致（Llama SciERC fine-tuned 实际 91.9%）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-N1 发现，R1 交叉回应 AGREE。Table 2 Llama-SciERC: (1.11-0.09)/1.11=91.9%，低于 94% 下限。实际范围 92-100%。\"\n  action_items:\n    - round: 16\n      action: \"Abstract 修正为 '92–100% reduction' 或 '≥92% reduction'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF3\"\n  summary: \"CF 率在 Abstract 中选择性报告——仅 SciERC (0–9.9%)，隐藏 DocRED 12.02% 和 WikiEvents 21.1%\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W2: DR↔CF trade-off 选择性报告\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R2-N2 critical, R1-W4 major→交叉回应后 R2 要求升级为 must-fix。Abstract '(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)' 通过节引用限定为 SciERC。DocRED Llama CF=12.02%, WikiEvents CF=14.9–21.1%。Director 取 critical。\"\n  action_items:\n    - round: 15\n      action: \"Abstract near-eliminates 加 CF 范围限定\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 16\n      action: \"Abstract CF 范围改为全数据集范围 (0–21.1% zero-shot, dataset-dependent)，或至少明确标注 'on SciERC'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 16 Major Issues\n# ============================================================\n\n- id: \"R16-W1\"\n  summary: \"κ̄ (constraint tightness) 统计支撑不足：独立 schema 仅 n=2，自由度为零\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF2: Spearman ρ 替换为 descriptive，n=6 caveat 已加\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W4: 双方 AGREE。§1 仍列为主要贡献，应降级为 diagnostic metric。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R1 critical (N2), R2 major (W2), 双方交叉 AGREE。R2 补充：κ̄ 独立取值仅 n=2（schema 属性不随模型变化），WikiEvents 未报告 κ̄。Per-relation 分析 (Table 34) 显示 high κ 本身不足以预测 DR reduction。\"\n  action_items:\n    - round: 16\n      action: \"将 κ̄ 从 contribution list 降级为 diagnostic observation；报告 WikiEvents κ̄ 值；降低 §2/§4 中的 prominence\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"DocRED zero-shot DR 仅降 45% 与 'near-eliminates' narrative 存在张力，主文讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-W1 major, R2-W1 major, 双方共识。DocRED Full S1: 18.46%→10.21% (45%)。§1 contribution 'yields 94–100%' 排除 DocRED 45%。四类错误分析仅在 Appendix D。R1 REBUT R2 关于 zero-shot 是最核心场景的判断——fine-tuned 更具部署相关性。Director: 两者均需讨论。\"\n  action_items:\n    - round: 16\n      action: \"§1 contribution 修正为涵盖 DocRED 范围 (45–100%)；主文引入 Appendix D 错误分类摘要\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents FT 仅 20-doc test set，'demonstrate generalization' 措辞与 evidence 不匹配\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF1: per-doc variance 和 CI 已补充\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W3: 20-doc 仍不足。建议标记 preliminary/pilot。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R1-W2 major, R2-W4 major, 双方交叉 AGREE。Clopper-Pearson 95% CI 上界 5.83%。'demonstrate generalization' 应降级为 'initial evidence'/'pilot study'。\"\n  action_items:\n    - round: 16\n      action: \"§1 contribution 2b 改为 'preliminary/pilot evidence'；§5.4 确认所有 WikiEvents 结论有 preliminary 限定\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"70B 评估过于单薄——仅 INT4 推理，无消融/FT，CF 飙升未分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W5: R1 major, R2 should-fix\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R1-W3 major, R2 交叉 AGREE。CF 0.07%→7.01% 未充分分析。Abstract '7–70B' 范围给人不恰当的覆盖印象。\"\n  action_items:\n    - round: 16\n      action: \"标注为 'feasibility check'，不作为评估结论组成部分；分析 CF 飙升原因（INT4 vs model scale）\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 / novelty 定位：系统集成 vs 算法创新，形式化证明是 contribution 还是 motivation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W1: R2 critical (Excitement 2.5), R1 部分 REBUT (Excitement 3.0)\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R2-W3 major 认为应降级为 motivation。R1 partial REBUT——形式化本身有独立价值，但同意应更精确表述贡献范围。Divergence: R1 Excitement 3.5 vs R2 Excitement 2.5。Director 取中间：形式化有一定价值但 §1 positioning 应降低。\"\n  action_items:\n    - round: 16\n      action: \"§1 Prop 1 重措辞为 'we formalize a well-known intuition'；以实验验证 (24% vs 94%) 作为主要证据而非形式证明\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W6\"\n  summary: \"Proposition 1 对无界实体集成立，但实际 IE 操作在有界集上——gap 仅在 Appendix 提及\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 warning, R2 partial REBUT（Appendix O 已讨论但主文应加限定）。有限实体集语言技术上是 regular 的但 DFA 指数增长。\"\n  action_items:\n    - round: 16\n      action: \"§3 加一句限定：有限实体集语言技术上 regular，但状态数指数增长使 DFA 不可行\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 16 Minor\n# ============================================================\n\n- id: \"R16-M1\"\n  summary: \"§3.3 'formal guarantees' / 'pair-based enforcement' 与 §4 'best-effort' fallback 术语张力\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF2 追踪 guarantee→enforcement 替换\"\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M4: 仍存在张力。建议统一为 'best-effort enforcement with grammar-first degradation'。R1-M1 补充 'enabling dependency' 非标准术语。\"\n  action_items:\n    - round: 16\n      action: \"全文术语统一；'enabling dependency' 加 'empirical' 限定\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M2\"\n  summary: \"§6 Related Work 主文 ~1/3 页，三段式过于压缩\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-M4: Related Work 压缩过度\"\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M3: 每段引用堆叠，缺乏关键区分点展开。8 页限制下难以扩展。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M3\"\n  summary: \"'calibrated models' 排除条件在 §1 不够透明（Mistral 42% 被隐式排除）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M6: §1 'zero-shot DR drops 76–99% for calibrated models' 但 Mistral 仅 42%，排除条件不透明。\"\n  action_items:\n    - round: 16\n      action: \"§1 加 'calibrated models' 的明确定义或排除说明\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M4\"\n  summary: \"regino2025kgcurator 和 formattax2026 两条引用在 OpenAlex 未找到匹配\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M5: formattax2026 标注 arXiv:2604.03616，可能太新未索引。需确认存在。\"\n  action_items:\n    - round: 16\n      action: \"确认两条引用存在且信息正确\"\n      assigned_to: agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved/tracking (abbreviated)\n# ============================================================\n\n- id: \"R15-MF2\"\n  summary: \"Abstract/Intro 中 'guarantee' 措辞与 fallback 机制存在系统性 overclaiming\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16-M1 追踪。guarantee→enforcement 替换可能已部分完成，但 R2-M4 仍标记术语张力存在。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页（~8 行结论），违反 EMNLP 2026 严格 8 页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未被任何 Reviewer 独立提出。可能已修复。待 Research Director 确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"DR↔CF trade-off 选择性报告\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"以 R16-MF3 形式继续追踪，升级为 critical。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W6\"\n  summary: \"Fallback causal tracing 缺失\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未独立提出。R1-S2 提到 Appendix C Table 7 causal tracing 作为优势。可能已添加。待确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W7\"\n  summary: \"仅英语数据集评估，跨语言泛化未讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未独立提出。Limitations section 已提及 English-only 和 CJK tokenization 差异（R2-S3 确认 Limitations 全面）。可能已修复。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W8\"\n  summary: \"Post-hoc filtering 对比不够公平（discard vs correction）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未独立提出。可能已修复或不再被认为是重要问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M3\"\n  summary: \"Enabling dependency 概念主文未正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-M1: Corollary 中有定义但非标准形式化概念。以 R16-M1 形式追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Intro 被系统性低估\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 修复。R15 以 R15-W2 形式复发。R16 以 R16-MF3 形式再次复发并升级为 critical。\"\n  resolution_round: 14\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents FT n=20 + Contribution 3 措辞过度\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 拆分 RE systematic + EE preliminary。R16 以 R16-W3 继续追踪。\"\n  resolution_round: 14\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 2 定位过高\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 移出 Contribution（3→2）。R16 以 R16-W1 继续追踪 §1 定位。\"\n  resolution_round: 14\n\n- id: \"R14-M3\"\n  summary: \"Entity registry 顺序依赖未量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"100% ordering confirmed (EBNF 结构保证)，§3 已加说明\"\n  resolution_round: 14\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"FT fallback ≤0.11% 已补充。R16 未复发。\"\n  resolution_round: 14\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 16 (fresh review), 2026-05-21\n\n# ============================================================\n# Round 16 Must-Fix\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD/CRANE/IterGen/EnriCo 等同类 constrained decoding 方法的实验对比（连续 5 轮 R12-R16）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: should-fix\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF3: 升级为 must-fix\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1: 连续 3 轮。战略转换为 grammar-only ablation reframed as Level 1 对比\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF1: R1 critical, R2 AGREE。grammar-only ablation 隐含 GCD 对比但未显式化。BoostCD head-to-head 仍缺。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16-MF1: 双 Reviewer 再次标记 critical。R2 补充 IterGen (backtracking) 和 EnriCo (ASP) 作为 semantic-level 竞品。grammar-only proxy 论证仍不被接受——BoostCD 的 boosting mechanism 无法被代理。连续 5 轮未解决。\"\n  action_items:\n    - round: 14\n      action: \"grammar-only ablation reframed as BoostCD-equivalent Level 1\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 15\n      action: \"§5 新增显式对比小节：Grammar-only=GCD/BoostCD equivalent, 24% vs 94% DR reduction 数据\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 16\n      action: \"在 SciERC/DocRED 上运行 GCD 代码做 head-to-head 对比（最关键）；如 IterGen/EnriCo 不可复现需说明不可比原因\"\n      assigned_to: agent + paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF2\"\n  summary: \"Abstract '94–100% DR reduction' 与 Table 2 数据不一致（Llama SciERC fine-tuned 实际 91.9%）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-N1 发现，R1 交叉回应 AGREE。Table 2 Llama-SciERC: (1.11-0.09)/1.11=91.9%，低于 94% 下限。实际范围 92-100%。\"\n  action_items:\n    - round: 16\n      action: \"Abstract 修正为 '92–100% reduction' 或 '≥92% reduction'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF3\"\n  summary: \"CF 率在 Abstract 中选择性报告——仅 SciERC (0–9.9%)，隐藏 DocRED 12.02% 和 WikiEvents 21.1%\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W2: DR↔CF trade-off 选择性报告\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R2-N2 critical, R1-W4 major→交叉回应后 R2 要求升级为 must-fix。Abstract '(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)' 通过节引用限定为 SciERC。DocRED Llama CF=12.02%, WikiEvents CF=14.9–21.1%。Director 取 critical。\"\n  action_items:\n    - round: 15\n      action: \"Abstract near-eliminates 加 CF 范围限定\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 16\n      action: \"Abstract CF 范围改为全数据集范围 (0–21.1% zero-shot, dataset-dependent)，或至少明确标注 'on SciERC'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 16 Major Issues\n# ============================================================\n\n- id: \"R16-W1\"\n  summary: \"κ̄ (constraint tightness) 统计支撑不足：独立 schema 仅 n=2，自由度为零\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF2: Spearman ρ 替换为 descriptive，n=6 caveat 已加\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W4: 双方 AGREE。§1 仍列为主要贡献，应降级为 diagnostic metric。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R1 critical (N2), R2 major (W2), 双方交叉 AGREE。R2 补充：κ̄ 独立取值仅 n=2（schema 属性不随模型变化），WikiEvents 未报告 κ̄。Per-relation 分析 (Table 34) 显示 high κ 本身不足以预测 DR reduction。\"\n  action_items:\n    - round: 16\n      action: \"将 κ̄ 从 contribution list 降级为 diagnostic observation；报告 WikiEvents κ̄ 值；降低 §2/§4 中的 prominence\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"DocRED zero-shot DR 仅降 45% 与 'near-eliminates' narrative 存在张力，主文讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-W1 major, R2-W1 major, 双方共识。DocRED Full S1: 18.46%→10.21% (45%)。§1 contribution 'yields 94–100%' 排除 DocRED 45%。四类错误分析仅在 Appendix D。R1 REBUT R2 关于 zero-shot 是最核心场景的判断——fine-tuned 更具部署相关性。Director: 两者均需讨论。\"\n  action_items:\n    - round: 16\n      action: \"§1 contribution 修正为涵盖 DocRED 范围 (45–100%)；主文引入 Appendix D 错误分类摘要\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents FT 仅 20-doc test set，'demonstrate generalization' 措辞与 evidence 不匹配\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF1: per-doc variance 和 CI 已补充\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W3: 20-doc 仍不足。建议标记 preliminary/pilot。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R1-W2 major, R2-W4 major, 双方交叉 AGREE。Clopper-Pearson 95% CI 上界 5.83%。'demonstrate generalization' 应降级为 'initial evidence'/'pilot study'。\"\n  action_items:\n    - round: 16\n      action: \"§1 contribution 2b 改为 'preliminary/pilot evidence'；§5.4 确认所有 WikiEvents 结论有 preliminary 限定\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"70B 评估过于单薄——仅 INT4 推理，无消融/FT，CF 飙升未分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W5: R1 major, R2 should-fix\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R1-W3 major, R2 交叉 AGREE。CF 0.07%→7.01% 未充分分析。Abstract '7–70B' 范围给人不恰当的覆盖印象。\"\n  action_items:\n    - round: 16\n      action: \"标注为 'feasibility check'，不作为评估结论组成部分；分析 CF 飙升原因（INT4 vs model scale）\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 / novelty 定位：系统集成 vs 算法创新，形式化证明是 contribution 还是 motivation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W1: R2 critical (Excitement 2.5), R1 部分 REBUT (Excitement 3.0)\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: R2-W3 major 认为应降级为 motivation。R1 partial REBUT——形式化本身有独立价值，但同意应更精确表述贡献范围。Divergence: R1 Excitement 3.5 vs R2 Excitement 2.5。Director 取中间：形式化有一定价值但 §1 positioning 应降低。\"\n  action_items:\n    - round: 16\n      action: \"§1 Prop 1 重措辞为 'we formalize a well-known intuition'；以实验验证 (24% vs 94%) 作为主要证据而非形式证明\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W6\"\n  summary: \"Proposition 1 对无界实体集成立，但实际 IE 操作在有界集上——gap 仅在 Appendix 提及\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-W5 warning, R2 partial REBUT（Appendix O 已讨论但主文应加限定）。有限实体集语言技术上是 regular 的但 DFA 指数增长。\"\n  action_items:\n    - round: 16\n      action: \"§3 加一句限定：有限实体集语言技术上 regular，但状态数指数增长使 DFA 不可行\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 16 Minor\n# ============================================================\n\n- id: \"R16-M1\"\n  summary: \"§3.3 'formal guarantees' / 'pair-based enforcement' 与 §4 'best-effort' fallback 术语张力\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF2 追踪 guarantee→enforcement 替换\"\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M4: 仍存在张力。建议统一为 'best-effort enforcement with grammar-first degradation'。R1-M1 补充 'enabling dependency' 非标准术语。\"\n  action_items:\n    - round: 16\n      action: \"全文术语统一；'enabling dependency' 加 'empirical' 限定\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M2\"\n  summary: \"§6 Related Work 主文 ~1/3 页，三段式过于压缩\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-M4: Related Work 压缩过度\"\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M3: 每段引用堆叠，缺乏关键区分点展开。8 页限制下难以扩展。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M3\"\n  summary: \"'calibrated models' 排除条件在 §1 不够透明（Mistral 42% 被隐式排除）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M6: §1 'zero-shot DR drops 76–99% for calibrated models' 但 Mistral 仅 42%，排除条件不透明。\"\n  action_items:\n    - round: 16\n      action: \"§1 加 'calibrated models' 的明确定义或排除说明\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M4\"\n  summary: \"regino2025kgcurator 和 formattax2026 两条引用在 OpenAlex 未找到匹配\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-M5: formattax2026 标注 arXiv:2604.03616，可能太新未索引。需确认存在。\"\n  action_items:\n    - round: 16\n      action: \"确认两条引用存在且信息正确\"\n      assigned_to: agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved/tracking (abbreviated)\n# ============================================================\n\n- id: \"R15-MF2\"\n  summary: \"Abstract/Intro 中 'guarantee' 措辞与 fallback 机制存在系统性 overclaiming\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16-M1 追踪。guarantee→enforcement 替换可能已部分完成，但 R2-M4 仍标记术语张力存在。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页（~8 行结论），违反 EMNLP 2026 严格 8 页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未被任何 Reviewer 独立提出。可能已修复。待 Research Director 确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W2\"\n  summary: \"DR↔CF trade-off 选择性报告\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"以 R16-MF3 形式继续追踪，升级为 critical。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W6\"\n  summary: \"Fallback causal tracing 缺失\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未独立提出。R1-S2 提到 Appendix C Table 7 causal tracing 作为优势。可能已添加。待确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W7\"\n  summary: \"仅英语数据集评估，跨语言泛化未讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未独立提出。Limitations section 已提及 English-only 和 CJK tokenization 差异（R2-S3 确认 Limitations 全面）。可能已修复。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-W8\"\n  summary: \"Post-hoc filtering 对比不够公平（discard vs correction）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 未独立提出。可能已修复或不再被认为是重要问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-M3\"\n  summary: \"Enabling dependency 概念主文未正式定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1-M1: Corollary 中有定义但非标准形式化概念。以 R16-M1 形式追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Intro 被系统性低估\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 修复。R15 以 R15-W2 形式复发。R16 以 R16-MF3 形式再次复发并升级为 critical。\"\n  resolution_round: 14\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents FT n=20 + Contribution 3 措辞过度\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 拆分 RE systematic + EE preliminary。R16 以 R16-W3 继续追踪。\"\n  resolution_round: 14\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 2 定位过高\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 移出 Contribution（3→2）。R16 以 R16-W1 继续追踪 §1 定位。\"\n  resolution_round: 14\n\n- id: \"R14-M3\"\n  summary: \"Entity registry 顺序依赖未量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"100% ordering confirmed (EBNF 结构保证)，§3 已加说明\"\n  resolution_round: 14\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"FT fallback ≤0.11% 已补充。R16 未复发。\"\n  resolution_round: 14\n"
  }
}
```

</details>

---


### Tool result

_source line 1696 · 2026-05-21T02:45:16.079888+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 13558}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1697 · 2026-05-21T02:47:38.142837+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 16 审稿报告 — OntoCoDec\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle, Long Paper)\n**Reviewer 编排**: R1（方法严谨性 + 实验评估）, R2（新颖性 + 完整性 + 格式合规）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE 本体编译为两层 token-level 解码约束的框架：grammar layer（context-free，通过 XGrammar 编译 JSON 结构和词汇约束）和 semantic layer（prefix-decidable with state，通过动态 entity registry 和 logit masking 实施 domain/range type constraints）。两层之间存在 enabling dependency（Proposition 1, pumping lemma proof）。框架在 SciERC、DocRED（关系抽取）和 WikiEvents（事件抽取）上用 4 个自回归 LM（7–70B）进行了验证。LoRA 微调下 DR ≤0.09%、CF ≤1.27%；zero-shot DR 降低 45–99%（dataset-dependent）。\n\n---\n\n## Strengths\n\n1. **问题定义清晰，实用价值明确**：IE 中 domain/range violation 是真实存在的系统性问题（baseline 15–18%），论文精确量化了问题规模并提供了可操作的解决方案。[R1, R2 共识]\n\n2. **消融实验设计系统化**：五路消融（unconstrained / grammar-only / semantic-only / S1 / S2）清晰隔离了各层贡献。Enabling dependency 的实验证据（grammar-only 3–24% DR reduction vs. full 94–100%）比理论证明更有说服力。[R1-S2, R2]\n\n3. **DR↔CF trade-off 的诚实和深入分析**：Table 8（Appendix C）展示消除 CF 导致 DR 增加 15.8× 的根本性权衡。定量分析优于多数论文的 \"limitations as afterthought\" 做法。[R1-S3, R2-S6]\n\n4. **Limitations section 异常全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎预见性地回答了 reviewer 想问的问题。[R2-S3]\n\n5. **统计严谨性**：所有 F1 比较均有 10,000-iteration paired bootstrap，报告 p-values 和 CI。DR reduction 在所有 fine-tuned settings 中均 significant (p&lt;0.001)。[R2-S4]\n\n6. **跨模型/跨 tokenizer 泛化**：在 3 种 tokenizer 架构（byte-level BPE ×2, SentencePiece）和 4 个模型上验证。Appendix 体量大（25 页）且信息密度高，显著提高可复现性。[R1-S4, R1-S5, R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R1+R2 强共识] **缺少与现有 constrained decoding 方法的 head-to-head 实验对比**\n\nGrammar-only ablation 被声称等同于 GCD/BoostCD 的约束类别（§5.1 \"implements the same class of constraints\"），但未运行任何现有系统的实际代码。BoostCD 的 boosting mechanism（交替 constrained/unconstrained decoding）是其核心贡献，grammar-only ablation 无法代表。IterGen（backtracking-based semantic constraint）和 EnriCo（ASP-based decoding constraints）是 semantic-level 最直接竞品，仅在 Related Work 中讨论。无 head-to-head 对比，无法判断改进来自 semantic layer 创新还是实现差异。\n\n**此问题已连续 5 轮（R12–R16）被标记，是本论文最持久的审稿缺口。**\n\n**MF2** [critical, R2 发现, R1 交叉 AGREE] **Abstract \"94–100% DR reduction\" 与 Table 2 数据不一致**\n\nTable 2 中 Llama-3.1-8B SciERC fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置实际范围是 **92–100%**，而非 94–100%。这是 Abstract 核心定量 claim，可直接验证，不准确损害可信度。\n\n**MF3** [critical, R1+R2 强共识] **CF 率在 Abstract 中选择性报告**\n\nAbstract \"(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)\" 通过节引用将 CF 范围限定为 SciERC 一个数据集。实际上：\n- DocRED zero-shot Llama CF = **12.02%**（Table 4）\n- WikiEvents zero-shot CF = **14.9–21.1%**（Table 5）\n\n读者易将 \"(0–9.9%)\" 误解为全局范围。CF 是本方法的核心 trade-off，不完整披露构成选择性报告，损害 AC/Reviewer 对方法局限性的判断。\n\n---\n\n### Major Issues\n\n**W1** [R1 critical, R2 major, 共识] **κ̄ (constraint tightness) 作为预测指标缺乏统计支撑**\n\nκ̄ 作为 schema 属性仅有 **n=2** 独立取值（SciERC vs DocRED），自由度为零，任何回归分析无意义。线性拟合 R²=0.86 基于 n=4（2 datasets × 2 models, p=0.07）。Per-relation 分析（Appendix N, Table 34）进一步显示 high κ 本身不足以预测 DR reduction（\"equal tight relations... show 74.05% DR\"）。WikiEvents 有 245 constraints 但未报告 κ̄ 值。尽管如此，κ̄ 在 §1 contribution list、§2 Background、§4 获独立方程编号——prominence 远超证据强度。\n\n**W2** [major, R1+R2 共识] **DocRED zero-shot DR 仅降 45%，与整体 narrative 存在张力**\n\nDocRED zero-shot Full S1: 18.46% → 10.21%，仅 **45%** reduction，远低于 SciERC 94%。§1 contribution item 2 说 \"yields 94–100%\"，排除了 DocRED 45% 却未说明。详细四类错误分析仅在 Appendix D（entity type errors 39%, schema coverage gaps 33%, incorrect relation selection 17%, direction reversal 11%），主文仅一段简短讨论。\n\n*R1 REBUT R2 关于 \"zero-shot 是最核心场景\" 的判断，认为 fine-tuned + constrained 是更常见部署模式。Director 判断：两种场景均需讨论，但 §1 contribution 措辞应涵盖两者的实际数据范围。*\n\n**W3** [major, R1+R2 共识] **WikiEvents 20-doc test set 统计功效不足以支撑 \"generalization\" claim**\n\n20 文档 test set，Clopper-Pearson 95% CI 上界 5.83%。Per-document variance 极高（Arg-F1 std/mean &gt; 0.5, 35–47% documents scoring zero）。§1 contribution 2b \"demonstrate generalization to 245 constraints\" 的 claim 强度与 evidence 强度不匹配。\n\n**W4** [major, R1 发现, R2 AGREE] **70B 评估过于单薄**\n\n仅 Llama-3.1-70B (AWQ INT4) 推理，无消融、无微调。CF 从 0.07% 飙升至 7.01%，未充分分析（INT4 量化偏移 vs. model scale 效应）。Abstract \"7–70B\" 范围声明给人不恰当的覆盖印象。应标注为 \"feasibility check\"。\n\n**W5** [major, Reviewer 分歧] **Proposition 1 / novelty 定位**\n\nR2 认为 cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理基本知识（cf. attribute grammars），Proposition 1 应降级为 motivation。R1 partial REBUT：形式化本身有独立价值（将 IE type constraints 具体化为语言识别问题，完整 pumping lemma proof, Appendix O 2 pages），三级约束分类是有用的概念贡献。\n\nDirector 判断：Proposition 1 的 formalization 在约束解码文献中有一定新颖性，但 §1 将其作为首要贡献列出的 positioning 偏高。建议重新措辞为 \"we formalize a well-known intuition\"，以实验验证（grammar-only 24% vs full 94%）作为主要证据。\n\n**W6** [warning, R1 发现] **Proposition 1 的 bounded/unbounded gap**\n\nProposition 1 对无界实体集成立。对有限实体集，valid language 在技术上是 regular 的（Appendix O, page 33 正确指出），但 DFA 状态数指数增长（SciERC: &gt;10^17 states）使其 \"practically infeasible\"。这是实际不可行性论证而非形式不可能。此 gap 仅在 Appendix 末尾简短提及，主文 §3 应加一句限定。\n\n---\n\n### Minor Issues\n\n- **M1**: §3.3 \"formal guarantees\" / \"pair-based enforcement\" 与 §4 \"best-effort\" fallback 存在术语张力。\"enabling dependency\" 非标准形式化概念。建议统一术语。[R2-M4, R1-M1]\n- **M2**: §6 Related Work 主文仅 ~1/3 页，三段式引用堆叠，缺乏关键区分点展开。[R2-M3]\n- **M3**: Table 3 脚注中 XGrammar 残余 0.03% RV（chimeric values）应说明是否已上报/修复。[R2-M2]\n- **M4**: §1 \"zero-shot DR drops 76–99% for calibrated models\"——Mistral 42% 被排除但 \"calibrated models\" 条件不够透明。[R2-M6]\n- **M5**: `regino2025kgcurator` 和 `formattax2026` 两条引用在 OpenAlex 中未找到匹配，应确认存在。[R2-M5]\n- **M6**: DocRED 使用 dev set 的说明应提升到主文实验设置段落。[R1-M2]\n- **M7**: Figure 3 per-relation DR rates 仅 Llama-3.1-8B，缺乏跨模型验证。[R1-M3]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成强共识：\n1. **缺少 baseline 直接对比** — 最关键实验缺口，连续 5 轮标记\n2. **κ̄ 统计支撑不足** — n=2 独立取值，任何回归无意义\n3. **Abstract 数字不一致** — \"94–100%\" 实际为 92–100%\n4. **CF 选择性报告** — Abstract 仅覆盖 SciERC，隐藏 DocRED 12% 和 WikiEvents 21%\n5. **DocRED 45%** — 与 \"near-eliminates\" narrative 不一致\n6. **WikiEvents 20-doc** — \"demonstrate generalization\" 措辞过度\n7. **70B 单薄** — 无消融/FT，CF 飙升未分析\n\n优势共识：\n8. **Ablation 设计系统化** — 五路消融 + enabling dependency 实验验证\n9. **Limitations 异常诚实** — 覆盖面全面\n10. **统计严谨性** — bootstrap 检验规范\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Proposition 1 定位**：R1 (Excitement 3.5) 认为 pumping lemma proof 在约束解码文献中有独立理论价值；R2 (Excitement 2.5) 认为结论 expected，应作为 motivation 而非 contribution。Director 取中间立场：形式化有一定价值但 §1 positioning 应降低。\n\n2. **Zero-shot 场景重要性**：R2 认为 zero-shot 是 constrained decoding 最核心场景；R1 认为 fine-tuned + constrained 更具部署相关性。Director：两者均需讨论，Abstract/Contribution 应涵盖两种场景的实际数据范围。\n\n3. **整体评分**：R1 = 3.5 (Borderline Conference)，R2 = 3.0 (Findings)。差异主要在 Novelty/Excitement（R1=3.5 vs R2=2.5），Soundness 一致 (3.5/5)。\n\n---\n\n## Questions to Authors\n\n1. Grammar-only ablation 是否使用了与 GCD 完全相同的 XGrammar 配置和 grammar compilation pipeline？实现差异是否可能解释 grammar-only 的低 DR reduction？\n2. κ̄ 是否在论文未报告的其他 ontology 上验证过？WikiEvents 的 κ̄ 值是多少？\n3. 70B 模型上 CF 飙升至 7.01% 的原因——INT4 量化引入的 token 分布偏移，还是更大模型与约束系统有不同的交互模式？\n4. DocRED 残余 DR 中 39% entity type errors，semantic layer 是否可通过更 aggressive masking 减少？\n5. 对于有限实体集，DFA 方案在什么规模以下会变得可行？\n\n---\n\n## Missing References\n\n引用基本完整。60 条 bib entries 全部被引用，0 orphan。50 条 OpenAlex 验证通过，2 条因过新未收录（应确认存在），8 条为作者名编码差异（非实质错误）。\n\n可能有价值的补充（非必须）：\n- Attribute grammars 经典参考（支撑 Proposition 1 的 \"well-known principle\" 定位）\n- IterGen 的 backtracking 机制与 OntoCoDec fallback 的更深入 Discussion 对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 8 info, 0 critical）。\n\n**Warnings:**\n- Pages 1-2: 连续 2 页纯文本（Intro + Background），首个视觉锚点延迟到 page 3。建议将 Figure 1 提前或加 teaser figure/table\n- Pages 5-7: 主文结果全部为 table（5 table + 0 figure），视觉单调。建议将 Appendix 散点图或 beam sweep 图提升到主文\n- Page 8: 末页（Related Work + Conclusion）纯文本，无视觉锚点收尾\n\n**Info:**\n- Figure 1 组件文字标注偏小（正文字号 60-65%）\n- 主文 8 页仅 1 figure，figure:table = 1:5，低于领域平均（2-3 figures）\n- Table 26 红/绿颜色编码对色盲不友好\n- References 格式统一，Tables 使用 booktabs，质量良好\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | Director |\n|------|-----|-----|----------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.5 | 2.5 | **3.0** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4 | 4 | **4** |\n\n**评分依据**：\n- Abstract 中存在可验证的数字不一致（MF2）和选择性报告（MF3），损害 credibility\n- 连续 5 轮缺少 baseline 直接对比（MF1）是最关键实验缺口，审稿人无法评估相对贡献\n- 算法新颖性有限：两层架构是 XGrammar（off-the-shelf）+ entity registry（dict + lookup + masking）的领域迁移组合\n- κ̄ 作为 contribution 证据不足（n=2 schema）\n- 论文的实际价值（解决 IE violation 问题）和工程完整度（ablation + 统计 + 跨模型验证 + 诚实 limitations）适合 Findings 级别\n\n**提升路径 → 3.5 (Borderline Conference)**：\n1. 补充至少 GCD 在 SciERC/DocRED 上的 head-to-head 对比（**最关键**）\n2. 修正 Abstract 数字（\"94-100%\" → \"92-100%\"）和 CF 范围（涵盖全数据集）\n3. 将 κ̄ 从 contribution 降级为 diagnostic observation\n\n**提升路径 → 4.0 (Conference)**：\n额外需要：BoostCD head-to-head 对比、Proposition 1 更精确的 contribution 定位、§1 contribution 措辞涵盖 DocRED 45% 和 WikiEvents preliminary 性质\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"94–100% reduction\" → 修正为 \"92–100%\"（Table 2 Llama-SciERC 91.9%）\n- \"near-eliminates DR\" 应加限定条件并报告全数据集 CF 范围\n- Contribution item 2 \"yields 94–100%\" 排除了 DocRED zero-shot 45%\n- \"demonstrate generalization\" (WikiEvents) → \"provide preliminary evidence for\"\n- \"zero-shot DR drops 76–99% for calibrated models\" → 明确 \"calibrated\" 排除条件\n\n### §3 Method\n- Proposition 1: 加一句关于有限实体集的限定（technically regular but exponentially large DFA）\n- \"enabling dependency\" 加 \"empirical\" 限定或改用非误导性术语\n\n### §4 Constraint Composition\n- κ̄: 降低 prominence——移出 contribution list，标记为 descriptive hypothesis\n- 报告 WikiEvents κ̄ 值\n\n### §5 Experiments\n- DocRED 45%: 将 Appendix D 错误分类总结移入主文\n- WikiEvents: \"demonstrate generalization\" → \"preliminary/pilot\"\n- 70B: 标注为 \"feasibility check\"，分析 CF 飙升原因\n- **补充 GCD head-to-head**（至少 SciERC）\n\n### §7 Conclusion\n- CF 范围应覆盖全数据集（0–21.1% zero-shot, dataset-dependent）\n- \"near-eliminates\" 需限定为 fine-tuned setting",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 16 审稿报告 — OntoCoDec\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle, Long Paper)\n**Reviewer 编排**: R1（方法严谨性 + 实验评估）, R2（新颖性 + 完整性 + 格式合规）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE 本体编译为两层 token-level 解码约束的框架：grammar layer（context-free，通过 XGrammar 编译 JSON 结构和词汇约束）和 semantic layer（prefix-decidable with state，通过动态 entity registry 和 logit masking 实施 domain/range type constraints）。两层之间存在 enabling dependency（Proposition 1, pumping lemma proof）。框架在 SciERC、DocRED（关系抽取）和 WikiEvents（事件抽取）上用 4 个自回归 LM（7–70B）进行了验证。LoRA 微调下 DR ≤0.09%、CF ≤1.27%；zero-shot DR 降低 45–99%（dataset-dependent）。\n\n---\n\n## Strengths\n\n1. **问题定义清晰，实用价值明确**：IE 中 domain/range violation 是真实存在的系统性问题（baseline 15–18%），论文精确量化了问题规模并提供了可操作的解决方案。[R1, R2 共识]\n\n2. **消融实验设计系统化**：五路消融（unconstrained / grammar-only / semantic-only / S1 / S2）清晰隔离了各层贡献。Enabling dependency 的实验证据（grammar-only 3–24% DR reduction vs. full 94–100%）比理论证明更有说服力。[R1-S2, R2]\n\n3. **DR↔CF trade-off 的诚实和深入分析**：Table 8（Appendix C）展示消除 CF 导致 DR 增加 15.8× 的根本性权衡。定量分析优于多数论文的 \"limitations as afterthought\" 做法。[R1-S3, R2-S6]\n\n4. **Limitations section 异常全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎预见性地回答了 reviewer 想问的问题。[R2-S3]\n\n5. **统计严谨性**：所有 F1 比较均有 10,000-iteration paired bootstrap，报告 p-values 和 CI。DR reduction 在所有 fine-tuned settings 中均 significant (p&lt;0.001)。[R2-S4]\n\n6. **跨模型/跨 tokenizer 泛化**：在 3 种 tokenizer 架构（byte-level BPE ×2, SentencePiece）和 4 个模型上验证。Appendix 体量大（25 页）且信息密度高，显著提高可复现性。[R1-S4, R1-S5, R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, R1+R2 强共识] **缺少与现有 constrained decoding 方法的 head-to-head 实验对比**\n\nGrammar-only ablation 被声称等同于 GCD/BoostCD 的约束类别（§5.1 \"implements the same class of constraints\"），但未运行任何现有系统的实际代码。BoostCD 的 boosting mechanism（交替 constrained/unconstrained decoding）是其核心贡献，grammar-only ablation 无法代表。IterGen（backtracking-based semantic constraint）和 EnriCo（ASP-based decoding constraints）是 semantic-level 最直接竞品，仅在 Related Work 中讨论。无 head-to-head 对比，无法判断改进来自 semantic layer 创新还是实现差异。\n\n**此问题已连续 5 轮（R12–R16）被标记，是本论文最持久的审稿缺口。**\n\n**MF2** [critical, R2 发现, R1 交叉 AGREE] **Abstract \"94–100% DR reduction\" 与 Table 2 数据不一致**\n\nTable 2 中 Llama-3.1-8B SciERC fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置实际范围是 **92–100%**，而非 94–100%。这是 Abstract 核心定量 claim，可直接验证，不准确损害可信度。\n\n**MF3** [critical, R1+R2 强共识] **CF 率在 Abstract 中选择性报告**\n\nAbstract \"(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)\" 通过节引用将 CF 范围限定为 SciERC 一个数据集。实际上：\n- DocRED zero-shot Llama CF = **12.02%**（Table 4）\n- WikiEvents zero-shot CF = **14.9–21.1%**（Table 5）\n\n读者易将 \"(0–9.9%)\" 误解为全局范围。CF 是本方法的核心 trade-off，不完整披露构成选择性报告，损害 AC/Reviewer 对方法局限性的判断。\n\n---\n\n### Major Issues\n\n**W1** [R1 critical, R2 major, 共识] **κ̄ (constraint tightness) 作为预测指标缺乏统计支撑**\n\nκ̄ 作为 schema 属性仅有 **n=2** 独立取值（SciERC vs DocRED），自由度为零，任何回归分析无意义。线性拟合 R²=0.86 基于 n=4（2 datasets × 2 models, p=0.07）。Per-relation 分析（Appendix N, Table 34）进一步显示 high κ 本身不足以预测 DR reduction（\"equal tight relations... show 74.05% DR\"）。WikiEvents 有 245 constraints 但未报告 κ̄ 值。尽管如此，κ̄ 在 §1 contribution list、§2 Background、§4 获独立方程编号——prominence 远超证据强度。\n\n**W2** [major, R1+R2 共识] **DocRED zero-shot DR 仅降 45%，与整体 narrative 存在张力**\n\nDocRED zero-shot Full S1: 18.46% → 10.21%，仅 **45%** reduction，远低于 SciERC 94%。§1 contribution item 2 说 \"yields 94–100%\"，排除了 DocRED 45% 却未说明。详细四类错误分析仅在 Appendix D（entity type errors 39%, schema coverage gaps 33%, incorrect relation selection 17%, direction reversal 11%），主文仅一段简短讨论。\n\n*R1 REBUT R2 关于 \"zero-shot 是最核心场景\" 的判断，认为 fine-tuned + constrained 是更常见部署模式。Director 判断：两种场景均需讨论，但 §1 contribution 措辞应涵盖两者的实际数据范围。*\n\n**W3** [major, R1+R2 共识] **WikiEvents 20-doc test set 统计功效不足以支撑 \"generalization\" claim**\n\n20 文档 test set，Clopper-Pearson 95% CI 上界 5.83%。Per-document variance 极高（Arg-F1 std/mean &gt; 0.5, 35–47% documents scoring zero）。§1 contribution 2b \"demonstrate generalization to 245 constraints\" 的 claim 强度与 evidence 强度不匹配。\n\n**W4** [major, R1 发现, R2 AGREE] **70B 评估过于单薄**\n\n仅 Llama-3.1-70B (AWQ INT4) 推理，无消融、无微调。CF 从 0.07% 飙升至 7.01%，未充分分析（INT4 量化偏移 vs. model scale 效应）。Abstract \"7–70B\" 范围声明给人不恰当的覆盖印象。应标注为 \"feasibility check\"。\n\n**W5** [major, Reviewer 分歧] **Proposition 1 / novelty 定位**\n\nR2 认为 cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理基本知识（cf. attribute grammars），Proposition 1 应降级为 motivation。R1 partial REBUT：形式化本身有独立价值（将 IE type constraints 具体化为语言识别问题，完整 pumping lemma proof, Appendix O 2 pages），三级约束分类是有用的概念贡献。\n\nDirector 判断：Proposition 1 的 formalization 在约束解码文献中有一定新颖性，但 §1 将其作为首要贡献列出的 positioning 偏高。建议重新措辞为 \"we formalize a well-known intuition\"，以实验验证（grammar-only 24% vs full 94%）作为主要证据。\n\n**W6** [warning, R1 发现] **Proposition 1 的 bounded/unbounded gap**\n\nProposition 1 对无界实体集成立。对有限实体集，valid language 在技术上是 regular 的（Appendix O, page 33 正确指出），但 DFA 状态数指数增长（SciERC: &gt;10^17 states）使其 \"practically infeasible\"。这是实际不可行性论证而非形式不可能。此 gap 仅在 Appendix 末尾简短提及，主文 §3 应加一句限定。\n\n---\n\n### Minor Issues\n\n- **M1**: §3.3 \"formal guarantees\" / \"pair-based enforcement\" 与 §4 \"best-effort\" fallback 存在术语张力。\"enabling dependency\" 非标准形式化概念。建议统一术语。[R2-M4, R1-M1]\n- **M2**: §6 Related Work 主文仅 ~1/3 页，三段式引用堆叠，缺乏关键区分点展开。[R2-M3]\n- **M3**: Table 3 脚注中 XGrammar 残余 0.03% RV（chimeric values）应说明是否已上报/修复。[R2-M2]\n- **M4**: §1 \"zero-shot DR drops 76–99% for calibrated models\"——Mistral 42% 被排除但 \"calibrated models\" 条件不够透明。[R2-M6]\n- **M5**: `regino2025kgcurator` 和 `formattax2026` 两条引用在 OpenAlex 中未找到匹配，应确认存在。[R2-M5]\n- **M6**: DocRED 使用 dev set 的说明应提升到主文实验设置段落。[R1-M2]\n- **M7**: Figure 3 per-relation DR rates 仅 Llama-3.1-8B，缺乏跨模型验证。[R1-M3]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成强共识：\n1. **缺少 baseline 直接对比** — 最关键实验缺口，连续 5 轮标记\n2. **κ̄ 统计支撑不足** — n=2 独立取值，任何回归无意义\n3. **Abstract 数字不一致** — \"94–100%\" 实际为 92–100%\n4. **CF 选择性报告** — Abstract 仅覆盖 SciERC，隐藏 DocRED 12% 和 WikiEvents 21%\n5. **DocRED 45%** — 与 \"near-eliminates\" narrative 不一致\n6. **WikiEvents 20-doc** — \"demonstrate generalization\" 措辞过度\n7. **70B 单薄** — 无消融/FT，CF 飙升未分析\n\n优势共识：\n8. **Ablation 设计系统化** — 五路消融 + enabling dependency 实验验证\n9. **Limitations 异常诚实** — 覆盖面全面\n10. **统计严谨性** — bootstrap 检验规范\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **Proposition 1 定位**：R1 (Excitement 3.5) 认为 pumping lemma proof 在约束解码文献中有独立理论价值；R2 (Excitement 2.5) 认为结论 expected，应作为 motivation 而非 contribution。Director 取中间立场：形式化有一定价值但 §1 positioning 应降低。\n\n2. **Zero-shot 场景重要性**：R2 认为 zero-shot 是 constrained decoding 最核心场景；R1 认为 fine-tuned + constrained 更具部署相关性。Director：两者均需讨论，Abstract/Contribution 应涵盖两种场景的实际数据范围。\n\n3. **整体评分**：R1 = 3.5 (Borderline Conference)，R2 = 3.0 (Findings)。差异主要在 Novelty/Excitement（R1=3.5 vs R2=2.5），Soundness 一致 (3.5/5)。\n\n---\n\n## Questions to Authors\n\n1. Grammar-only ablation 是否使用了与 GCD 完全相同的 XGrammar 配置和 grammar compilation pipeline？实现差异是否可能解释 grammar-only 的低 DR reduction？\n2. κ̄ 是否在论文未报告的其他 ontology 上验证过？WikiEvents 的 κ̄ 值是多少？\n3. 70B 模型上 CF 飙升至 7.01% 的原因——INT4 量化引入的 token 分布偏移，还是更大模型与约束系统有不同的交互模式？\n4. DocRED 残余 DR 中 39% entity type errors，semantic layer 是否可通过更 aggressive masking 减少？\n5. 对于有限实体集，DFA 方案在什么规模以下会变得可行？\n\n---\n\n## Missing References\n\n引用基本完整。60 条 bib entries 全部被引用，0 orphan。50 条 OpenAlex 验证通过，2 条因过新未收录（应确认存在），8 条为作者名编码差异（非实质错误）。\n\n可能有价值的补充（非必须）：\n- Attribute grammars 经典参考（支撑 Proposition 1 的 \"well-known principle\" 定位）\n- IterGen 的 backtracking 机制与 OntoCoDec fallback 的更深入 Discussion 对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 8 info, 0 critical）。\n\n**Warnings:**\n- Pages 1-2: 连续 2 页纯文本（Intro + Background），首个视觉锚点延迟到 page 3。建议将 Figure 1 提前或加 teaser figure/table\n- Pages 5-7: 主文结果全部为 table（5 table + 0 figure），视觉单调。建议将 Appendix 散点图或 beam sweep 图提升到主文\n- Page 8: 末页（Related Work + Conclusion）纯文本，无视觉锚点收尾\n\n**Info:**\n- Figure 1 组件文字标注偏小（正文字号 60-65%）\n- 主文 8 页仅 1 figure，figure:table = 1:5，低于领域平均（2-3 figures）\n- Table 26 红/绿颜色编码对色盲不友好\n- References 格式统一，Tables 使用 booktabs，质量良好\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | Director |\n|------|-----|-----|----------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.5 | 2.5 | **3.0** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4 | 4 | **4** |\n\n**评分依据**：\n- Abstract 中存在可验证的数字不一致（MF2）和选择性报告（MF3），损害 credibility\n- 连续 5 轮缺少 baseline 直接对比（MF1）是最关键实验缺口，审稿人无法评估相对贡献\n- 算法新颖性有限：两层架构是 XGrammar（off-the-shelf）+ entity registry（dict + lookup + masking）的领域迁移组合\n- κ̄ 作为 contribution 证据不足（n=2 schema）\n- 论文的实际价值（解决 IE violation 问题）和工程完整度（ablation + 统计 + 跨模型验证 + 诚实 limitations）适合 Findings 级别\n\n**提升路径 → 3.5 (Borderline Conference)**：\n1. 补充至少 GCD 在 SciERC/DocRED 上的 head-to-head 对比（**最关键**）\n2. 修正 Abstract 数字（\"94-100%\" → \"92-100%\"）和 CF 范围（涵盖全数据集）\n3. 将 κ̄ 从 contribution 降级为 diagnostic observation\n\n**提升路径 → 4.0 (Conference)**：\n额外需要：BoostCD head-to-head 对比、Proposition 1 更精确的 contribution 定位、§1 contribution 措辞涵盖 DocRED 45% 和 WikiEvents preliminary 性质\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"94–100% reduction\" → 修正为 \"92–100%\"（Table 2 Llama-SciERC 91.9%）\n- \"near-eliminates DR\" 应加限定条件并报告全数据集 CF 范围\n- Contribution item 2 \"yields 94–100%\" 排除了 DocRED zero-shot 45%\n- \"demonstrate generalization\" (WikiEvents) → \"provide preliminary evidence for\"\n- \"zero-shot DR drops 76–99% for calibrated models\" → 明确 \"calibrated\" 排除条件\n\n### §3 Method\n- Proposition 1: 加一句关于有限实体集的限定（technically regular but exponentially large DFA）\n- \"enabling dependency\" 加 \"empirical\" 限定或改用非误导性术语\n\n### §4 Constraint Composition\n- κ̄: 降低 prominence——移出 contribution list，标记为 descriptive hypothesis\n- 报告 WikiEvents κ̄ 值\n\n### §5 Experiments\n- DocRED 45%: 将 Appendix D 错误分类总结移入主文\n- WikiEvents: \"demonstrate generalization\" → \"preliminary/pilot\"\n- 70B: 标注为 \"feasibility check\"，分析 CF 飙升原因\n- **补充 GCD head-to-head**（至少 SciERC）\n\n### §7 Conclusion\n- CF 范围应覆盖全数据集（0–21.1% zero-shot, dataset-dependent）\n- \"near-eliminates\" 需限定为 fine-tuned setting",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1698 · 2026-05-21T02:47:43.136009+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4993
}
```

</details>

---


### Assistant

_source line 1699 · 2026-05-21T02:47:51.551886+00:00_

**Round 16 审稿完成。**

审稿报告已投递给 Research Director。Issue Tracker 已同步更新。

**总评: 3.0 (Findings)**

核心发现：
- **3 个 Must-Fix**：(1) 连续 5 轮缺少 baseline 直接对比（GCD/BoostCD）；(2) Abstract "94–100%" 实际为 92–100%；(3) CF 选择性报告（仅报 SciERC，隐藏 DocRED 12% 和 WikiEvents 21%）
- **6 个 Major**：κ̄ n=2 无统计意义、DocRED 45% 与 narrative 矛盾、WikiEvents 20-doc 不足、70B 单薄、Proposition 1 定位偏高、bounded/unbounded gap
- **7 个 Minor**：术语张力、Related Work 压缩、引用验证等
- **Reviewer 分歧**：Excitement（R1=3.5 vs R2=2.5），Proposition 1 是 contribution 还是 motivation

提升到 3.5 的最关键路径：补充 GCD head-to-head 实验对比 + 修正 Abstract 数字和 CF 范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 124

## Round 124

2 recorded events


### User

_source line 1700 · 2026-05-21T02:47:54.244713+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 和 R2 在 4 个关键问题上有强共识（baseline 缺失、DocRED 45%、WikiEvents 20-doc、CF 选择性报告）。主要分歧在 Excitement/Novelty 评估——R1 认为理论驱动设计有价值（3.5），R2 认为技术深度不足（2.5）。R2 独有发现是 Abstract "94–100%" 的数字不一致（实际 91.9–100%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1701 · 2026-05-21T02:48:03.615304+00:00_

Round 16 审稿已完成，报告已投递给 Research Director。

**最终评分：3.0 (Findings)**

**3 个 Must-Fix**：
1. 缺少 GCD/BoostCD head-to-head 实验对比（连续 5 轮）
2. Abstract "94–100%" 数字不一致（实际 92–100%）
3. CF 选择性报告（仅 SciERC 0–9.9%，隐藏 DocRED 12% 和 WikiEvents 21%）

**5 个 Major**：κ̄ 统计不足、DocRED 45% narrative 张力、WikiEvents 20-doc、70B 单薄、Proposition 1 定位偏高

**Reviewer 分歧**：Excitement（R1=3.5 vs R2=2.5），Proposition 1 是 contribution 还是 motivation，zero-shot vs fine-tuned 场景重要性

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 125

## Round 125

46 recorded events


### User

_source line 1702 · 2026-05-22T10:39:05.436462+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1703 · 2026-05-22T10:39:22.644196+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1704 · 2026-05-22T10:39:22.695237+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1705 · 2026-05-22T10:39:34.457974+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1706 · 2026-05-22T10:39:34.508604+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-22T10:39:37.422124+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-22T10:39:37.422541+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1709 · 2026-05-22T10:39:45.763716+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1710 · 2026-05-22T10:39:45.764217+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1711 · 2026-05-22T10:39:49.529862+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1712 · 2026-05-22T10:39:49.580492+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1713 · 2026-05-22T10:39:55.557570+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1714 · 2026-05-22T10:39:56.529105+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (139 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_beam_sweep** (success): Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\n  [d066_beam_sweep_eval](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/d066_beam_sweep/report/d066_beam_sweep_eval.md) | [d066_beam_sweep_scierc_analysis](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/d066_beam_sweep/report/d066_beam_sweep_scierc_analysis.md) | [beam_pareto_dual_panel](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/d066_beam_sweep/chart/beam_pareto.pdf)\n- **eval_70b_lora_docred_200_s1_constrained** (success): 70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve 
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 971
}
```

</details>

---


### Tool call

_source line 1715 · 2026-05-22T10:39:56.630176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-22T10:39:58.488408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-22T10:39:58.790307+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-22T10:39:58.790706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-22T10:39:58.841421+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R16 Action Matrix D079 dispatched, 2026-05-21
3	
4	# ============================================================
5	# Round 16 Must-Fix
6	# ============================================================
7	
8	- id: "R15-MF1"
9	  summary: "缺少与 GCD/BoostCD/CRANE/IterGen/EnriCo 等同类 constrained decoding 方法的实验对比（连续 5 轮 R12-R16）"
10	  category: experiment
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 12
14	  last_seen_round: 16
15	  mentions:
16	    - round: 12
17	      reviewers: [1, 2]
18	      note: "R12-SF2: should-fix"
19	    - round: 13
20	      reviewers: [1, 2]
21	      note: "R13-MF3: 升级为 must-fix"
22	    - round: 14
23	      reviewers: [1, 2]
24	      note: "R14-MF1: grammar-only ablation reframed as Level 1 对比"
25	    - round: 15
26	      reviewers: [1, 2]
27	      note: "R15-MF1: §5 显式 BoostCD/GCD 对比段落。仍不够——未运行外部代码。"
28	    - round: 16
29	      reviewers: [1, 2]
30	      note: "R16-MF1: 连续 5 轮 critical。grammar-only proxy 不被接受。"
31	  action_items:
32	    - round: 14
33	      action: "grammar-only ablation reframed as BoostCD-equivalent Level 1"
34	      assigned_to: paper_agent
35	      status: completed
36	    - round: 15
37	      action: "§5 新增显式对比小节"
38	      assigned_to: paper_agent
39	      status: completed
40	    - round: 16
41	      action: "实现 trie-based GCD-equivalent baseline (同模型同数据控制变量)，SciERC 4 configs 对比 trie vs grammar-only vs full S1"
42	      assigned_to: agent + paper_agent
43	      status: in_progress
44	  resolution: ""
45	  resolution_round: null
46	
47	- id: "R16-MF2"
48	  summary: "Abstract '94–100% DR reduction' 与 Table 2 数据不一致（Llama SciERC fine-tuned 实际 91.9%）"
49	  category: framing
50	  severity: critical
51	  status: in_progress
52	  first_raised_round: 16
53	  last_seen_round: 16
54	  mentions:
55	    - round: 16
56	      reviewers: [2]
57	      note: "R2-N1 发现，R1 交叉 AGREE。实际范围 92-100%。"
58	  action_items:
59	    - round: 16
60	      ac
…[truncated 9189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1720 · 2026-05-22T10:40:07.684993+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"}]

Based on the search results, I found information about EMNLP 2025 and related conferences, but I did not find a specific call f
…[truncated 1292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 11054
}
```

</details>

---


### Tool call

_source line 1721 · 2026-05-22T10:40:17.607124+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-22T10:40:17.958880+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 1723 · 2026-05-22T10:40:19.918882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 1724 · 2026-05-22T10:40:20.321055+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf (566.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool result

_source line 1725 · 2026-05-22T10:40:29.574034+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, he
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 11615
}
```

</details>

---


### Tool result

_source line 1726 · 2026-05-22T10:40:34.853533+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines for page limits and format requirements:

## Page Limits

All ARR submissions are in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). More specifically:

- **Long papers**: Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 17246
}
```

</details>

---


### Tool call

_source line 1727 · 2026-05-22T10:40:43.039632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "pages": "6-10"
  }
}
```

</details>

---


### Tool result

_source line 1728 · 2026-05-22T10:40:43.493666+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf (566.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1729 · 2026-05-22T10:40:43.980009+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1730 · 2026-05-22T10:40:44.080932+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1731 · 2026-05-22T10:40:49.454491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "pages": "11-15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "pages": "11-15"
  }
}
```

</details>

---


### Tool result

_source line 1732 · 2026-05-22T10:40:49.807033+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf (566.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1733 · 2026-05-22T10:41:05.147459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "pages": "16-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "pages": "16-20"
  }
}
```

</details>

---


### Tool result

_source line 1734 · 2026-05-22T10:41:05.700703+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf (566.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1735 · 2026-05-22T10:41:06.410865+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1736 · 2026-05-22T10:41:06.461482+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1737 · 2026-05-22T10:41:19.301095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "pages": "21-25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "pages": "21-25"
  }
}
```

</details>

---


### Tool result

_source line 1738 · 2026-05-22T10:41:20.105369+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf (566.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1739 · 2026-05-22T10:41:20.563884+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "glob": "**/config*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
    "glob": "**/config*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1740 · 2026-05-22T10:41:20.715869+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1741 · 2026-05-22T10:42:35.007063+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1742 · 2026-05-22T10:42:59.442744+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24435
}
```

</details>

---


### Tool call

_source line 1743 · 2026-05-22T10:43:00.450444+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿目标\n对以下论文进行严格审稿，像顶会最严格的审稿人一样评估。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **类型**: Long paper, ≤8 页正文 + 无限参考文献页\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations/Ethics**: 不计入页数限制，但必须包含\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查重点\n\n### 1. 方法严谨性\n- **Proposition 1 (Level 2 ⊄ Level 1)** 的证明是否正确？有无逻辑漏洞？bounded vs unbounded entity sets 的区分是否在主文中充分说明？\n- 两层约束架构（grammar layer + semantic layer）的设计是否合理？grammar-first fallback 的设计选择是否有充分的理论或实验支撑？\n- Entity registry 的动态构建是否引入了顺序依赖问题？\n- Constraint tightness κ̄ 的统计有效性（仅 n=2 或 n=3 个 schema）\n\n### 2. 实验设计\n- **消融实验**: Table 1/2/3 的五/四路消融是否完整？是否有遗漏的关键配置？\n- **统计显著性**: Bootstrap 10,000 iterations, p-values, Bonferroni correction 是否恰当？\n- **Baseline 对比**: 是否缺少关键 baseline？特别是与 GCD、BoostCD、CRANE、IterGen、EnriCo 等同类 constrained decoding 方法的直接实验对比（而非仅讨论层面的对比）\n- **数据集覆盖**: SciERC (551 docs), DocRED (998 docs), WikiEvents (20 docs FT / 246 docs ZS) 的评估规模是否充分？\n- **跨模型验证**: Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B 的覆盖是否足够？70B 仅用 AWQ INT4 是否是重大限制？\n- **CF 问题**: CF violations 在约束后上升（如 Llama DocRED 12.02%），这是否构成方法的根本缺陷？DR↔CF trade-off 的分析是否充分？\n- **可复现性**: prompt templates, hyperparameters, 硬件配置是否有足够细节？\n\n### 3. 格式合规\n- 正文是否严格 ≤8 页？\n- 参考文献格式是否符合 ACL 规范？\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，S1, S2, ...)\n3. **Weaknesses** (逐条，W1, W2, ...，按严重度排序：Must-Fix → Should-Fix → Minor)\n4. **Questions** (需要作者澄清的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Overall Assessment** (评分 + 置信度 + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿目标\n对以下论文进行严格审稿，像顶会最严格的审稿人一样评估。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **类型**: Long paper, ≤8 页正文 + 无限参考文献页\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations/Ethics**: 不计入页数限制，但必须包含\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查重点\n\n### 1. 方法严谨性\n- **Proposition 1 (Level 2 ⊄ Level 1)** 的证明是否正确？有无逻辑漏洞？bounded vs unbounded entity sets 的区分是否在主文中充分说明？\n- 两层约束架构（grammar layer + semantic layer）的设计是否合理？grammar-first fallback 的设计选择是否有充分的理论或实验支撑？\n- Entity registry 的动态构建是否引入了顺序依赖问题？\n- Constraint tightness κ̄ 的统计有效性（仅 n=2 或 n=3 个 schema）\n\n### 2. 实验设计\n- **消融实验**: Table 1/2/3 的五/四路消融是否完整？是否有遗漏的关键配置？\n- **统计显著性**: Bootstrap 10,000 iterations, p-values, Bonferroni correction 是否恰当？\n- **Baseline 对比**: 是否缺少关键 baseline？特别是与 GCD、BoostCD、CRANE、IterGen、EnriCo 等同类 constrained decoding 方法的直接实验对比（而非仅讨论层面的对比）\n- **数据集覆盖**: SciERC (551 docs), DocRED (998 docs), WikiEvents (20 docs FT / 246 docs ZS) 的评估规模是否充分？\n- **跨模型验证**: Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B 的覆盖是否足够？70B 仅用 AWQ INT4 是否是重大限制？\n- **CF 问题**: CF violations 在约束后上升（如 Llama DocRED 12.02%），这是否构成方法的根本缺陷？DR↔CF trade-off 的分析是否充分？\n- **可复现性**: prompt templates, hyperparameters, 硬件配置是否有足够细节？\n\n### 3. 格式合规\n- 正文是否严格 ≤8 页？\n- 参考文献格式是否符合 ACL 规范？\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，S1, S2, ...)\n3. **Weaknesses** (逐条，W1, W2, ...，按严重度排序：Must-Fix → Should-Fix → Minor)\n4. **Questions** (需要作者澄清的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Overall Assessment** (评分 + 置信度 + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1744 · 2026-05-22T10:43:22.396721+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21946
}
```

</details>

---


### Tool call

_source line 1745 · 2026-05-22T10:43:22.547797+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿目标\n对以下论文进行严格审稿，像顶会最严格的审稿人一样评估。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **类型**: Long paper, ≤8 页正文 + 无限参考文献页\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations/Ethics**: 不计入页数限制，但必须包含\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- 核心贡献（两层 grammar+semantic 约束、自动编译 IE ontology 为 token-level masks）的新颖度如何？\n- 与现有工作的差异化是否充分？特别是 vs. GCD (Geng et al., 2023)、XGrammar (Dong et al., 2025)、PICARD (Scholak et al., 2021)、Mündler et al. (2025)\n- Proposition 1 是否是一个 novel contribution，还是 well-known intuition 的形式化？定位是否恰当？\n- κ̄ (constraint tightness) 作为度量的贡献是否足够？\n\n### 2. 叙事一致性 & 写作质量\n- Abstract 中的数字声明是否与正文 Table 数据一致？特别关注：\n  - \"DR ≤ 0.09%\" 是否在所有配置下成立？\n  - \"CF ≤ 1.3%\" 是否仅限于特定配置？是否选择性报告？\n  - DR reduction 范围（\"45-99%\"、\"76-99%\"、\"94%\"等不同表述）是否一致？\n- Introduction 中的 contribution claims 是否与实验结果完全匹配？\n- \"enforcement\" vs \"guarantee\" 等术语使用是否一致？\n- WikiEvents 结果是否被 overclaim 为 \"generalization\" 而实际仅 20 文档？\n- 70B 结果的定位是否恰当（feasibility check vs. full evaluation）？\n\n### 3. 相关工作覆盖\n- §6 Related Work + Appendix B 是否充分覆盖了：\n  - Constrained decoding for structured generation (GCD, BoostCD, XGrammar, Outlines, SynCode, CRANE)\n  - Schema-aware IE (GoLLIE, KnowCoder, CodeIE, ADELIE)\n  - Post-hoc validation (ODKE+, SPIRES/OntoGPT, OntoLogX, EnriCo, IterGen)\n- 是否有遗漏的关键近期工作（2024-2026）？\n- 引用是否全部真实？特别注意 arXiv preprints 的引用格式和真实性\n\n### 4. 完整性检查\n- Limitations 是否充分覆盖了方法的关键限制？\n- Ethics Statement 是否恰当？\n- Responsible NLP Checklist 填写是否准确？\n- 论文是否 self-contained（读者是否需要阅读 Appendix 才能理解主文核心论点）？\n\n### 5. 格式审查\n- 正文 ≤8 页？\n- 匿名合规（无 self-citation leaks、无 identifying information）？\n- Figure/Table 标注是否清晰？\n- 参考文献格式是否统一？\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，S1, S2, ...)\n3. **Weaknesses** (逐条，W1, W2, ...，按严重度排序：Must-Fix → Should-Fix → Minor)\n4. **Questions** (需要作者澄清的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Overall Assessment** (评分 + 置信度 + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿目标\n对以下论文进行严格审稿，像顶会最严格的审稿人一样评估。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **类型**: Long paper, ≤8 页正文 + 无限参考文献页\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations/Ethics**: 不计入页数限制，但必须包含\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- 核心贡献（两层 grammar+semantic 约束、自动编译 IE ontology 为 token-level masks）的新颖度如何？\n- 与现有工作的差异化是否充分？特别是 vs. GCD (Geng et al., 2023)、XGrammar (Dong et al., 2025)、PICARD (Scholak et al., 2021)、Mündler et al. (2025)\n- Proposition 1 是否是一个 novel contribution，还是 well-known intuition 的形式化？定位是否恰当？\n- κ̄ (constraint tightness) 作为度量的贡献是否足够？\n\n### 2. 叙事一致性 & 写作质量\n- Abstract 中的数字声明是否与正文 Table 数据一致？特别关注：\n  - \"DR ≤ 0.09%\" 是否在所有配置下成立？\n  - \"CF ≤ 1.3%\" 是否仅限于特定配置？是否选择性报告？\n  - DR reduction 范围（\"45-99%\"、\"76-99%\"、\"94%\"等不同表述）是否一致？\n- Introduction 中的 contribution claims 是否与实验结果完全匹配？\n- \"enforcement\" vs \"guarantee\" 等术语使用是否一致？\n- WikiEvents 结果是否被 overclaim 为 \"generalization\" 而实际仅 20 文档？\n- 70B 结果的定位是否恰当（feasibility check vs. full evaluation）？\n\n### 3. 相关工作覆盖\n- §6 Related Work + Appendix B 是否充分覆盖了：\n  - Constrained decoding for structured generation (GCD, BoostCD, XGrammar, Outlines, SynCode, CRANE)\n  - Schema-aware IE (GoLLIE, KnowCoder, CodeIE, ADELIE)\n  - Post-hoc validation (ODKE+, SPIRES/OntoGPT, OntoLogX, EnriCo, IterGen)\n- 是否有遗漏的关键近期工作（2024-2026）？\n- 引用是否全部真实？特别注意 arXiv preprints 的引用格式和真实性\n\n### 4. 完整性检查\n- Limitations 是否充分覆盖了方法的关键限制？\n- Ethics Statement 是否恰当？\n- Responsible NLP Checklist 填写是否准确？\n- 论文是否 self-contained（读者是否需要阅读 Appendix 才能理解主文核心论点）？\n\n### 5. 格式审查\n- 正文 ≤8 页？\n- 匿名合规（无 self-citation leaks、无 identifying information）？\n- Figure/Table 标注是否清晰？\n- 参考文献格式是否统一？\n\n## 输出格式\n请按以下结构输出你的审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，S1, S2, ...)\n3. **Weaknesses** (逐条，W1, W2, ...，按严重度排序：Must-Fix → Should-Fix → Minor)\n4. **Questions** (需要作者澄清的问题)\n5. **Missing References** (遗漏的重要相关工作)\n6. **Overall Assessment** (评分 + 置信度 + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1746 · 2026-05-22T10:43:24.016902+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1469
}
```

</details>

---


### Assistant

_source line 1747 · 2026-05-22T10:43:39.780512+00:00_

Round 1 已启动：
- **Reviewer 1**（方法+实验）已派发 ✓
- **Reviewer 2**（新颖性+完整性+写作）已派发 ✓
- **视觉审查 Agent** 已启动 ✓
- **外部审稿**: 未启用（无配置）

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1748 · 2026-05-22T10:51:41.733381+00:00_

[Reviewer 1 审稿意见]:
# Reviewer 1 审稿意见：OntoCoDec

## 审稿侧重：方法严谨性 + 实验设计

---

## 1. Summary

OntoCoDec 提出将 IE ontology 编译为 token 级约束的两层架构：grammar layer（CFG/XGrammar，强制 JSON 结构+词表约束）和 semantic layer（有状态处理器，强制 cross-field 类型一致性），并通过 grammar-first fallback 保证 JSON 完整性。论文提供 decidability 分析（Proposition 1），在 SciERC/DocRED/WikiEvents 三个数据集、四个模型族（7B-70B）上验证，报告 DR ≤ 0.09%、~10% latency overhead。附有 24 页 appendix。

## 2. Strengths

**S1.** 理论基础扎实且有原创性。Decidability taxonomy（Level 1/2/3，§3）将 IE 类型约束按可判定性分层，Proposition 1（Appendix O）证明 cross-field 类型一致性不可用 CFG 表达，为两层架构提供形式化依据。

**S2.** 消融实验设计系统完整。SciERC 五路消融（Table 1）和 DocRED 四路消融（Table 2）逐层隔离各组件贡献。Grammar-only 配置有效复现 GCD 天花板（DR 14.84%），语义层独立消融精确量化 grammar layer 的 enabling dependency。

**S3.** CF-DR trade-off 的诚实分析（Appendix C）。Fallback 因果追踪（Table 8）、CF-priority fallback 消融、dual-factor 定量分析（Figure 2）——承认 trade-off 是结构性而非可调参数。

**S4.** 跨模型/跨数据集/跨设置覆盖广。4 个模型族 × 3 个数据集 × zero-shot/fine-tuned，加上 beam search（Appendix F）、prompt sensitivity（Appendix I）、document length（Appendix H）等维度。

**S5.** 可复现性优秀。Appendix G 详细报告硬件/种子/超参/确定性验证，3 seeds with cross-GPU variance analysis（Table 24），prompt templates 完整展示（Table 6）。

**S6.** 工程贡献实用。Grammar-first fallback 确保合法 JSON，10% latency overhead（Table 23）实际可部署。

## 3. Weaknesses

### Must-Fix

**W1 [critical] 缺少与现有 constrained decoding 方法的直接实验对比。**
- 位置：§5, §6, Table 15 (Appendix D)
- 论文大量讨论 GCD、BoostCD、CRANE、GoLLIE 等方法（§6, Appendix B pp.16-18），但实验部分没有使用这些方法原始代码的 head-to-head 对比。唯一"对比"是 Appendix D 的 Trie-Only Baseline（Table 15），这是自行实现的简化 GCD 等价物。§5.4 声称 BoostCD "achieves only 3% DR reduction" 来自方法论推断而非实验。对于定位为"推进 IE constrained decoding"的论文，这是最大缺口。
- 建议：至少对 GCD 运行原始代码做 head-to-head 对比；如 BoostCD/CRANE 代码不可用，明确说明。

**W2 [critical] CF violation 增加在主文中被低估呈现。**
- 位置：§5.1 (p.5) vs. Appendix C (pp.19-20)
- Appendix C 报告 Llama DocRED CF 高达 12.02%，SciERC CF 从 0.18% 升至 1.30%（Table 1）。但主文 §5.1 仅提及 "CF ≤ 1.3%"，最严重的 12.02% 完全未在主文出现。Abstract 声称 "substantially reduces type violations"，但 DR 下降伴随 CF 系统性上升时 total violation burden 改善被高估。
- 建议：在 §5.1 或 §7 中明确报告 CF 最差情况，讨论 CF-DR trade-off 的结构性本质。

### Should-Fix

**W3 [warning] Constraint tightness κ̄ 统计功效不足。**
- 位置：§5 (p.5), Figure 2 (p.21)
- κ̄ 仅在 n=2-3 个 schema 上计算。Figure 2 线性拟合仅 4 个数据点（R²=0.886, p>0.05）。论文自己承认统计不足但仍称 "confirmatory-statistical characterization"。
- 建议：降低 claim 强度为 "descriptive observation"。

**W4 [warning] Entity registry 顺序依赖问题未量化。**
- 位置：§3.3, Limitations (p.9)
- 首次生成实体时分配错误类型会传播到所有后续引用。Limitations 承认 "the impact of such propagation has not been evaluated"，但完全没有量化分析。
- 建议：post-hoc 分析现有输出中首次提及错误率和传播频率。

**W5 [warning] WikiEvents fine-tuned 评估集仅 20 个文档。**
- 位置：§5.4, Table 5
- 20 个文档上的 bootstrap CI 极宽，统计显著性声明可靠性存疑。且 WikiEvents EE 任务不涉及 cross-field type constraints，主要验证 grammar layer。
- 建议：明确标注规模局限性。

**W6 [warning] S2（two-pass pipeline）对比分析不充分。**
- 位置：§3.4, §5.1
- S2 在 §3.4 花半页描述但实验中仅一句带过，无完整结果表格或失败原因分析。
- 建议：要么提供 S2 完整结果，要么压缩 §3.4 描述。

### Minor

**W7 [minor]** Proposition 1 证明中 position-based vs. name-based 实体引用的差异（Appendix O, p.34）用非正式论证桥接，缺乏形式化。

**W8 [minor]** 70B 模型仅用 AWQ INT4 量化评估（§5.3），未讨论量化对约束 enforcement 的潜在影响。

**W9 [minor]** §5 报告 "five models (7-70B)" 但实际出现 4 个模型族，计数方式需明确。

## 4. Questions

**Q1.** Entity registry 中，如果同一实体在不同三元组中被赋予不同类型（multi-type entity），OntoCoDec 如何处理？

**Q2.** Grammar-first fallback 触发率（Table 8: 0.09%-0.46%/position）的 triple-level 影响是什么？多少比例的完整三元组至少触发一次 fallback？

**Q3.** Llama DocRED 12.02% CF 的根本原因——模型特异性还是 schema 特异性？

**Q4.** 是否考虑过 constrained decoding + post-hoc filtering 的组合？

**Q5.** BoostCD "only 3% DR reduction" 的判断来自方法论分析还是实验？

## 5. Missing References

- 论文 Related Work 覆盖较好（GCD, BoostCD, CRANE, GoLLIE, KnowCoder, ADELIE, EnriCo, PICARD, SynCode 等），但上述方法仅在讨论层面出现，缺乏实验对比（→ W1）。

## 6. Overall Assessment

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 理论框架合理，消融设计系统；但缺 baseline 实验对比（W1）、CF 主文低估（W2）、κ̄ 统计功效不足（W3） |
| Excitement | 3/5 | 问题重要，方法合理但更偏工程贡献；两层架构是问题分解的自然设计 |
| Reproducibility | 4.5/5 | Appendix G 详尽，prompt 完整，代码承诺开源 |
| **Overall** | **3.5 — Borderline Conference** | 工程实现扎实、分析深入，但 W1（缺 baseline 对比）和 W2（CF 主文低估）是核心障碍 |
| Confidence | 4/5 | 仔细阅读全文含 34 页 appendix，熟悉 constrained decoding 文献 |

**一句话总评**：扎实的系统工程论文，理论基础和消融分析到位，但缺少与 GCD/BoostCD 等同类方法的直接实验对比是核心短板，CF-DR trade-off 的主文呈现需要更加诚实。解决 W1 和 W2 后可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1749 · 2026-05-22T10:52:03.153275+00:00_

Reviewer 1 初审已返回（3.5 — Borderline Conference）。核心发现：

- **W1 [critical]**: 缺少与 GCD/BoostCD/CRANE 等方法的直接实验对比
- **W2 [critical]**: CF violation 增加（Llama DocRED 12.02%）在主文中被低估
- **W3-W6 [warning]**: κ̄ 统计功效不足、entity registry 顺序依赖未量化、WikiEvents 20-doc 规模、S2 分析不充分

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1750 · 2026-05-22T10:52:05.767889+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3，Reproducibility 4.5，Confidence 4。

**核心判断**：两个 Must-Fix 问题决定是否能进入 Conference——(1) 缺少与 GCD/BoostCD 等现有 constrained decoding 方法的直接实验对比；(2) CF violation 增加（最差 Llama DocRED 12.02%）在主文中被低估呈现。解决这两点后论文可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1751 · 2026-05-22T10:52:17.358507+00:00_

Reviewer 1 初审已收到（3.5 Borderline Conference）。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 128

## Round 128

6 recorded events


### User

_source line 1752 · 2026-05-22T10:53:42.668739+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 1. Summary

本文提出 OntoCoDec，一个将 IE ontology 自动编译为 token-level 解码约束的框架。核心设计是两层架构：grammar layer（基于 XGrammar 的 CFG）保证 JSON 结构和词表合规，semantic layer（基于运行时实体注册表的有状态 logit masking）执行 domain/range 类型约束。论文通过 Proposition 1（pumping lemma 证明）论证跨字段类型约束超出 CFG 表达能力，并在 3 个数据集、5 个模型、2 个 IE 任务上进行了系统评估。LoRA + 约束解码在 R-F1 43–46% 下将 DR 降至 ≤0.09%，但引入 CF 违规（≤1.3%）作为 violation conversion 的代价。

---

## 2. Strengths

**S1. 问题驱动的系统化框架设计**
将 IE ontology 约束自动编译为解码时约束是一个实际且有价值的工程贡献。与需要约束特定训练的方法（GoLLIE, KnowCoder）相比，OntoCoDec 的"零训练开销"和自动编译特性有明确的实用优势。ontology → grammar → mask 的编译管道有清晰的工程逻辑。

**S2. 评估的系统性和全面性**
3 个数据集（SciERC, DocRED, WikiEvents）、5 个模型（7B–70B）、3 个 tokenizer family、zero-shot + LoRA fine-tuning、greedy + beam search、五路消融，加上 bootstrap 显著性检验和 Bonferroni 校正——评估覆盖度在同类工作中属于上乘。Table 1 的五路消融清楚地隔离了各层贡献。

**S3. 诚实透明的 Limitations**
Limitations section 覆盖了 CF trade-off、评估范围（模型规模、fine-tuning 方法、语言限制）、工程约束（API-only 模型不适用、tokenizer 依赖性）等关键限制，比多数投稿更加坦诚。CF↔DR trade-off 的分析（Appendix C, causal tracing）提供了对失败模式的真实理解。

**S4. 低运行时开销**
greedy S1 仅增加 10–13% 延迟，编译为 one-time < 0.5s，scalability benchmark 到 200 entity types / 1000 relations 仍保持 2–3% overhead。这对实际部署有直接价值。

**S5. Decidability analysis 提供理论基础**
Proposition 1 及其 pumping lemma 证明（Appendix O）为两层架构的必要性提供了形式化依据，而非仅凭直觉。Appendix 中的 finite entity set 分析补充了理论与实践之间的联系。

---

## 3. Weaknesses

### Must-Fix（影响接收决定）

**W1. [critical] Abstract 与 Introduction 的 DR 降幅数字不一致**
- Abstract: "45–99% DR reduction"（§Abstract）
- Introduction: "DR drops 76–99% for calibrated models"（§1, Contribution 2）
- Table 4 的实际数据覆盖 6 个 model-dataset 组合（8B zero-shot）：
  - SciERC: Qwen 94%, Llama 99%, Mistral 76%
  - DocRED: Qwen 45%, Llama 90%, Mistral 42%
- 全范围为 **42–99%**，而非 45–99%（Mistral DocRED 为 42%，被排除且未说明）
- Introduction 声称"76–99% for calibrated models"，但 DocRED Qwen（calibrated model）仅 45%，远低于 76%。除非 Qwen 在 DocRED 上不被视为"calibrated"，否则此声明与数据矛盾。
- **建议**：统一为准确范围"42–99%"或明确限定条件（如"76–99% on SciERC"），并在 abstract 中说明 Mistral 排除的理由。

**W2. [critical] CF ≤ 1.3% 声明被 70B 结果违反**
- Abstract: "residual CF (≤1.3%)"
- §5.4 (70B evaluation): "CF drops from 3.50% (zero-shot) to 0.18–**1.33%** (LoRA)"
- 1.33% > 1.3%。虽然差异微小，但 abstract 将其作为 bound 呈现，且 70B 是论文明确涵盖的配置（abstract 说"five autoregressive LMs (7–70B)"）。
- **建议**：将 bound 修正为 "≤1.4%" 或明确限定为 8B 模型。

**W3. [critical] 新颖性定位问题——核心贡献的组件均为已知技术**
- Grammar layer 是 XGrammar 的直接应用（论文自述"via XGrammar"）
- Semantic layer 是运行时类型检查的 mask 实现——概念上直截了当
- Proposition 1 formalizes "cross-field type constraints require runtime state beyond CFG"——论文自称"we formalize a well-known intuition"，但将其列为 Contribution #1
- 真正的新颖性在于：(a) 自动编译 IE ontology 为 token-level 约束的端到端管道，(b) 两层组合的系统评估
- 目前的贡献表述将"engineering integration"包装为"novel architecture"，可能引起 reviewer 质疑
- **建议**：将贡献重心从"two-layer architecture is novel"转向"first systematic study of automatically compiling IE ontologies into composable decoding constraints"，强调系统工程和实证发现而非架构创新。

### Should-Fix（影响评分但不一票否决）

**W4. [warning] κ̄ (constraint tightness) 作为"predictive factor"但 n=3**
- Abstract: "establishing constraint tightness (κ̄) as a predictive factor"
- 实际仅在 3 个 schema 上验证（SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄≈0.82）
- n=3 无法"establish"任何统计意义上的预测能力。Appendix 中的 dual-factor analysis（Figure 2）用 4 个数据点拟合线性模型（R²=0.886），但 p=0.058 不显著（文中诚实承认），且 4 个点中 Mistral 7B DocRED 偏离线性趋势
- 目前的证据仅支持"descriptive observation"而非"predictive factor"
- **建议**：将 abstract 中的"establishing...as a predictive factor"改为"introducing...as a descriptive metric"（与 Limitations section 的措辞一致），或增加更多 schema 的验证。

**W5. [warning] WikiEvents fine-tuning composability 基于 n=20 极不充分**
- §5.4: "On the full official test split (20 documents; 194/20/20)"
- 论文承认"per-document variance is high (Arg-F1 std/mean > 0.5)"和"confirming sufficient power to detect violation elimination but not small F1 differences"
- 但 Table 5 和正文仍报告 CF=0.77–1.18%、AC≤0.8% 等具体数字，读者可能高估这些估计的可靠性
- Abstract 将 WikiEvents 与 SciERC/DocRED 并列作为验证（"validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents"），但 fine-tuning 的"validation"实际非常初步
- **建议**：在 Table 5 caption 或 footnote 中加入 confidence interval，让读者评估 n=20 的统计效力。

**W6. [warning] "Deployment-grade compliance" 叙事被 CF trade-off 削弱**
- Abstract/Introduction 反复使用"deployment-grade type compliance"
- 但 CF 是 DR enforcement 的系统性副产品：zero-shot 最高 12.02%（Llama DocRED），fine-tuned 最高 1.18%（8B）
- Beam search 在 SciERC 上消除所有违规，但对 DocRED 的 beam search 仅在 50-document subset 上验证，且 CF 仍有 0.93%（Table 22, Llama DocRED）
- 全数据集 beam search 结果（Table 22, 998 docs）Qwen DR=0% CF=0.93%, Llama DR=0% CF reductions from 74-86%——并非"完全消除"
- "Deployment-grade"通常暗示接近零违规；当前系统在 CF 维度上做不到这一点
- **建议**：将 framing 从"deployment-grade compliance"软化为"near-complete DR elimination with residual CF trade-off"，或明确定义"deployment-grade"的具体含义。

**W7. [warning] "Enabling dependency" 声明范围不清**
- Introduction Contribution 2: "neither layer alone exceeds 24% DR reduction"
- 这仅在 SciERC 上成立（grammar-only 3%, semantic-only 24%）
- DocRED: semantic-only 实际达到 25%（超过 24%）；更严重的是，grammar-only 在 DocRED 上**增加** DR 42%（18.46% → 26.17%）
- 虽然引用了"(§5.1)"暗示限于 SciERC，但读者自然会理解为通用结论
- **建议**：改为"on SciERC, neither layer alone exceeds 24%"，并讨论 DocRED 上 grammar-only 增加 DR 的原因及其对 enabling dependency 叙事的影响。

### Minor（不影响接收）

**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B（~4 页）。主文读者无法仅从 §6 评估相关工作覆盖的充分性。建议将 Appendix B 中最关键的对比（尤其是 vs. GCD, GoLLIE, EnriCo 的定性差异）移入主文。

**M2.** "S1" 和 "Full S1" 在正文中交替使用（如 §5.1 "Full S1" vs. §5.4 "S1"），应统一术语。

**M3.** Figure 1 信息密度过高，同时展示 grammar 和 semantic 两层的内部机制。考虑分为两个子图或简化。

**M4.** Table 4 的 Mistral SciERC unconstrained CF=56.87% 通过 dagger (†) 脚注解释，但读者第一次看到时仍会困惑——建议在表格上方或 caption 中更早引入"poor calibration"的背景。

**M5.** Introduction 中"Post-hoc filtering improves precision but discards up to 48% of predictions including true positives"——"48%"仅在 Appendix 中有详细支撑（SciERC Qwen zero-shot），主文首次出现时未 cite 来源表格。

---

## 4. Questions（需要作者澄清）

**Q1.** Abstract/Intro 的 DR 降幅范围不一致（45–99% vs. 76–99%），具体是指哪些配置？DocRED Qwen 的 45% 为什么不影响 intro 的"76–99% for calibrated models"声明？

**Q2.** Beam search 在 DocRED 全数据集上的 CF 表现如何？Table 22 显示 Qwen CF=0.93%（beam k=4, 998 docs）——这与"eliminates all four violation types"的叙述如何调和？

**Q3.** 70B LoRA CF=1.33% 超过 abstract 的"≤1.3%"bound。是否考虑更新此 bound？

**Q4.** Proposition 1 的证明（Appendix O）使用 position-based formulation，但实际系统使用 name-based entity referencing。Appendix 最后一段讨论了这个简化，但核心证明是否因此与实际系统存在 gap？

**Q5.** Grammar-only 在 DocRED 上增加 DR（+42%）。这是否意味着在某些 ontology 配置下，grammar layer 可能损害而非帮助 DR？这对"enabling dependency"的通用性有什么影响？

---

## 5. Missing References

论文的相关工作覆盖在 constrained decoding + IE 领域相当全面。以下可能值得提及但非必要：

- **Schmidt & Cimiano (2025)**, "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts" (Bioinformatics)——biomedical IE 中 grammar-constrained decoding 的直接应用，与本文方法高度相关但独立发展。
- **Microsoft Guidance** library——虽然是工程工具而非研究论文，但在 constrained generation 讨论中经常被提及，可在 Appendix B 中简要提及。
- 论文未引用任何 **EMNLP 2025** 相关工作（proceedings 已发布），建议检查是否有遗漏的近期 accepted papers。

**引用真实性**: 所有 46 个 bib 条目均来自已知的真实论文/预印本。arXiv preprints 的引用格式基本统一（使用 arXiv preprint arXiv:XXXX.XXXXX 格式）。未发现伪造引用。

---

## 6. Overall Assessment

**Overall**: 3.5 — Borderline Conference

**Confidence**: 4/5 — 对 constrained decoding 和 IE 领域有较好了解，仔细阅读了全文（含 34 页附录）并验证了关键数字声明。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计全面，方法论合理，但 abstract/intro 数字不一致（W1, W2）削弱可信度；CF trade-off 削弱核心声明（W6） |
| Excitement | 2.5/5 | 实用价值明确但概念新颖性有限——grammar layer 为 XGrammar 应用，semantic layer 为直观的类型检查实现，Proposition 1 形式化已知直觉。主要贡献是系统集成和全面评估 |
| Reproducibility | 4/5 | exp_id 标注、bootstrap CI、seed 报告、Appendix G 的完整再现细节，"code and data will be released upon acceptance"。唯一扣分项是 70B 结果使用 AWQ INT4 量化（可能引入不确定性） |
| Overall Assessment | 3.5/5 | Borderline Conference |

### 一句话总评

一项系统化但新颖性有限的工程贡献：将已知组件（CFG enforcement + runtime type checking）组合为 IE ontology 约束解码管道，配以出色的评估覆盖度，但 abstract/intro 的数字不一致和 CF trade-off 削弱了核心叙事。

---

## 7. Detailed Comments（逐节）

### Abstract
- "45–99% DR reduction"与 intro 的"76–99%"不一致（W1）
- "CF ≤ 1.3%"被 70B 的 1.33% 违反（W2）
- "establishing constraint tightness (κ̄) as a predictive factor"过度声称（W4）
- 整体写作质量高，信息密度适当

### §1 Introduction
- Contribution 1 将 Proposition 1 定位为"formalize a well-known intuition"是准确的，但同时将其作为 headlined contribution 可能引起期望错位
- Contribution 2 中"neither layer alone exceeds 24%"仅限 SciERC（W7）
- "deployment-grade type compliance"措辞需要审视（W6）
- 写作清晰，问题动机充分

### §2 Background
- IE ontology 的形式化定义清楚
- 约束可判定性的三级分类（context-free / prefix-decidable / non-local）是有用的概念框架
- Proposition 1 定位为"necessary condition"恰当

### §3 Method
- Grammar layer 和 semantic layer 的实现描述清晰
- "Continuation masking"机制的解释充分
- "Grammar-first fallback"的设计决策合理，且有 causal tracing 验证（Appendix Table 7）

### §4 Constraint Composition
- Mask composition 公式简洁
- asymmetric conjunction（S(t) defined only over G(t)）的解释清楚

### §5 Experiments
- Table 1 的五路消融是最强的实验贡献之一
- DocRED 的 grammar-only DR 增加现象值得在主文中更详细讨论（W7）
- WikiEvents 结果的统计效力受限于 n=20（W5）
- 70B 结果定位为 "feasibility check" 基本恰当，但仍被纳入 abstract 的统计声明中

### §6 Related Work
- 覆盖面合理但主文过于压缩（M1）
- GCD, GoLLIE, EnriCo 的对比定位准确

### §7 Conclusion
- 数字与前文一致（继承了 W1 中的 "76–99%" 问题）

### Limitations
- 全面且诚实（S3）
- 三段分别覆盖约束范围、评估覆盖、工程考量
- 将 CF trade-off 定性为"fundamental trade-off in composable constraint systems"是合理的

### Ethics Statement & Checklist
- Ethics statement 简洁但充分
- Checklist 填写认真（page 10），各项回答与论文内容一致
- Responsible NLP Checklist 在 OpenReview submission form 中填写（符合 EMNLP 2026 要求），PDF 中的 checklist 作为补充

### 格式
- 正文 8 页 ✓
- `\usepackage[review]{acl}` ✓（匿名，行号）
- 作者行 "Anonymous ACL submission" ✓
- 未发现 self-citation leaks 或 identifying information
- Limitations/Ethics 在 \clearpage 后，不计入页数 ✓
- 参考文献格式基本统一，arXiv preprints 使用一致格式

---

**总结**: 论文在实际问题上提供了系统化的工程解决方案，评估全面且 limitations 诚实。主要顾虑是概念新颖性有限（已知组件的集成）和 abstract/intro 中数字声明的精确性问题。修正数字不一致并调整贡献定位后，可达到 Conference/Findings 接收水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1753 · 2026-05-22T10:54:30.556306+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 2** 的完整审稿意见（侧重：新颖性 + 完整性 + 写作质量）。请逐条回应其 Weaknesses 和 Questions，使用以下格式：\n\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你们是否在以下问题上有分歧？\n- CF violation 呈现是否足够诚实\n- κ̄ 的 claim 强度\n- WikiEvents 的评估充分性\n- 新颖性定位\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Strengths\nS1. 问题驱动的系统化框架设计——将 IE ontology 约束自动编译为解码时约束是实际且有价值的工程贡献。\nS2. 评估的系统性和全面性——3 数据集、5 模型、五路消融、bootstrap + Bonferroni。\nS3. 诚实透明的 Limitations。\nS4. 低运行时开销（10-13% latency）。\nS5. Decidability analysis 提供理论基础。\n\n### Weaknesses\n\n**W1 [critical]** Abstract 与 Introduction 的 DR 降幅数字不一致——Abstract \"45–99%\" vs. Intro \"76–99% for calibrated models\"。Table 4 实际全范围为 42–99%（Mistral DocRED 42%）。DocRED Qwen（calibrated）仅 45%，远低于 76%。\n\n**W2 [critical]** CF ≤1.3% 声明被 70B 结果违反——§5.4 报告 70B LoRA CF 1.33% > 1.3%。\n\n**W3 [critical]** 新颖性定位问题——grammar layer 是 XGrammar 直接应用，semantic layer 是直观的运行时类型检查，Proposition 1 形式化已知直觉。论文将\"engineering integration\"包装为\"novel architecture\"。建议重心转向\"first systematic study of automatically compiling IE ontologies into composable decoding constraints\"。\n\n**W4 [warning]** κ̄ 作为\"predictive factor\"但 n=3 schema，Figure 2 仅 4 数据点，p=0.058 不显著。\n\n**W5 [warning]** WikiEvents fine-tuning composability 基于 n=20 极不充分，统计效力有限。\n\n**W6 [warning]** \"Deployment-grade compliance\"叙事被 CF trade-off 削弱——CF 是系统性副产品，zero-shot 最高 12.02%。\n\n**W7 [warning]** \"Enabling dependency\"声明范围不清——\"neither layer alone exceeds 24%\"仅限 SciERC，DocRED grammar-only 增加 DR 42%。\n\n**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B。\n**M2.** \"S1\"/\"Full S1\" 术语不统一。\n**M3.** Figure 1 信息密度过高。\n**M4.** Table 4 Mistral CF dagger 脚注解释位置不佳。\n**M5.** \"48% predictions discarded\" 未在主文 cite 来源表格。\n\n### Questions\nQ1. DR 降幅范围不一致的具体配置？\nQ2. Beam search 在 DocRED 全数据集 CF 表现？\nQ3. 70B CF=1.33% 是否更新 abstract bound？\nQ4. Proposition 1 position-based vs name-based entity referencing 的 gap？\nQ5. Grammar-only 在 DocRED 增加 DR，对 enabling dependency 通用性的影响？\n\n### Missing References\n- Schmidt & Cimiano (2025), biomedical IE grammar-constrained decoding\n- Microsoft Guidance library\n- EMNLP 2025 proceedings 中可能遗漏的近期工作\n\n### Overall Assessment\n3.5 — Borderline Conference, Confidence 4/5\nExcitement 2.5/5（概念新颖性有限，主要是已知组件集成+全面评估）",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 2** 的完整审稿意见（侧重：新颖性 + 完整性 + 写作质量）。请逐条回应其 Weaknesses 和 Questions，使用以下格式：\n\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你们是否在以下问题上有分歧？\n- CF violation 呈现是否足够诚实\n- κ̄ 的 claim 强度\n- WikiEvents 的评估充分性\n- 新颖性定位\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Strengths\nS1. 问题驱动的系统化框架设计——将 IE ontology 约束自动编译为解码时约束是实际且有价值的工程贡献。\nS2. 评估的系统性和全面性——3 数据集、5 模型、五路消融、bootstrap + Bonferroni。\nS3. 诚实透明的 Limitations。\nS4. 低运行时开销（10-13% latency）。\nS5. Decidability analysis 提供理论基础。\n\n### Weaknesses\n\n**W1 [critical]** Abstract 与 Introduction 的 DR 降幅数字不一致——Abstract \"45–99%\" vs. Intro \"76–99% for calibrated models\"。Table 4 实际全范围为 42–99%（Mistral DocRED 42%）。DocRED Qwen（calibrated）仅 45%，远低于 76%。\n\n**W2 [critical]** CF ≤1.3% 声明被 70B 结果违反——§5.4 报告 70B LoRA CF 1.33% > 1.3%。\n\n**W3 [critical]** 新颖性定位问题——grammar layer 是 XGrammar 直接应用，semantic layer 是直观的运行时类型检查，Proposition 1 形式化已知直觉。论文将\"engineering integration\"包装为\"novel architecture\"。建议重心转向\"first systematic study of automatically compiling IE ontologies into composable decoding constraints\"。\n\n**W4 [warning]** κ̄ 作为\"predictive factor\"但 n=3 schema，Figure 2 仅 4 数据点，p=0.058 不显著。\n\n**W5 [warning]** WikiEvents fine-tuning composability 基于 n=20 极不充分，统计效力有限。\n\n**W6 [warning]** \"Deployment-grade compliance\"叙事被 CF trade-off 削弱——CF 是系统性副产品，zero-shot 最高 12.02%。\n\n**W7 [warning]** \"Enabling dependency\"声明范围不清——\"neither layer alone exceeds 24%\"仅限 SciERC，DocRED grammar-only 增加 DR 42%。\n\n**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B。\n**M2.** \"S1\"/\"Full S1\" 术语不统一。\n**M3.** Figure 1 信息密度过高。\n**M4.** Table 4 Mistral CF dagger 脚注解释位置不佳。\n**M5.** \"48% predictions discarded\" 未在主文 cite 来源表格。\n\n### Questions\nQ1. DR 降幅范围不一致的具体配置？\nQ2. Beam search 在 DocRED 全数据集 CF 表现？\nQ3. 70B CF=1.33% 是否更新 abstract bound？\nQ4. Proposition 1 position-based vs name-based entity referencing 的 gap？\nQ5. Grammar-only 在 DocRED 增加 DR，对 enabling dependency 通用性的影响？\n\n### Missing References\n- Schmidt & Cimiano (2025), biomedical IE grammar-constrained decoding\n- Microsoft Guidance library\n- EMNLP 2025 proceedings 中可能遗漏的近期工作\n\n### Overall Assessment\n3.5 — Borderline Conference, Confidence 4/5\nExcitement 2.5/5（概念新颖性有限，主要是已知组件集成+全面评估）",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1754 · 2026-05-22T10:54:53.223059+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22666
}
```

</details>

---


### Tool call

_source line 1755 · 2026-05-22T10:54:53.576520+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 1** 的完整审稿意见（侧重：方法严谨性 + 实验设计）。请逐条回应其 Weaknesses 和 Questions，使用以下格式：\n\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你们是否在以下问题上有分歧？\n- 缺少 baseline 实验对比的严重程度\n- CF violation 主文呈现问题\n- κ̄ 统计功效\n- WikiEvents 评估\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Strengths\nS1. 理论基础扎实——Decidability taxonomy + Proposition 1 pumping lemma 证明。\nS2. 消融实验设计系统完整——五路/四路消融逐层隔离。\nS3. CF-DR trade-off 诚实分析——causal tracing, CF-priority fallback 消融, dual-factor 分析。\nS4. 跨模型/跨数据集/跨设置覆盖广——4 模型族 × 3 数据集 × ZS/FT + beam/prompt/length 维度。\nS5. 可复现性优秀——Appendix G 硬件/种子/超参/3 seeds variance。\nS6. 工程贡献实用——10% latency overhead 可部署。\n\n### Weaknesses\n\n**W1 [critical]** 缺少与现有 constrained decoding 方法的直接实验对比——大量讨论 GCD/BoostCD/CRANE/GoLLIE 但无 head-to-head 实验。唯一\"对比\"是自行实现的 Trie-Only Baseline（Table 15）。§5.4 声称 BoostCD \"only 3% DR reduction\"来自方法论推断而非实验。\n\n**W2 [critical]** CF violation 增加在主文中被低估呈现——Llama DocRED CF 12.02% 完全未在主文出现，主文仅报 \"CF ≤ 1.3%\"。Abstract \"substantially reduces type violations\"在 DR↓+CF↑时高估 total violation burden 改善。\n\n**W3 [warning]** κ̄ 统计功效不足——n=2-3 schema，Figure 2 仅 4 点，p>0.05。\n\n**W4 [warning]** Entity registry 顺序依赖问题未量化——首次类型分配错误会传播，Limitations 承认但无量化。\n\n**W5 [warning]** WikiEvents fine-tuned 仅 20 文档，bootstrap CI 极宽。\n\n**W6 [warning]** S2（two-pass pipeline）花半页描述但实验中一句带过，无完整结果。\n\n**W7 [minor]** Proposition 1 证明中 position-based vs name-based 桥接缺乏形式化。\n**W8 [minor]** 70B AWQ INT4 量化对约束 enforcement 的影响未讨论。\n**W9 [minor]** \"five models\" 但实际 4 个模型族。\n\n### Questions\nQ1. Multi-type entity 如何处理？\nQ2. Triple-level fallback 触发比例？\nQ3. Llama DocRED 12.02% CF 根因？\nQ4. Constrained decoding + post-hoc filtering 组合？\nQ5. BoostCD \"3% DR reduction\" 来自分析还是实验？\n\n### Overall Assessment\n3.5 — Borderline Conference, Confidence 4/5\nSoundness 3.5, Excitement 3, Reproducibility 4.5",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Round 1\n\n以下是 **Reviewer 1** 的完整审稿意见（侧重：方法严谨性 + 实验设计）。请逐条回应其 Weaknesses 和 Questions，使用以下格式：\n\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注：你们是否在以下问题上有分歧？\n- 缺少 baseline 实验对比的严重程度\n- CF violation 主文呈现问题\n- κ̄ 统计功效\n- WikiEvents 评估\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Strengths\nS1. 理论基础扎实——Decidability taxonomy + Proposition 1 pumping lemma 证明。\nS2. 消融实验设计系统完整——五路/四路消融逐层隔离。\nS3. CF-DR trade-off 诚实分析——causal tracing, CF-priority fallback 消融, dual-factor 分析。\nS4. 跨模型/跨数据集/跨设置覆盖广——4 模型族 × 3 数据集 × ZS/FT + beam/prompt/length 维度。\nS5. 可复现性优秀——Appendix G 硬件/种子/超参/3 seeds variance。\nS6. 工程贡献实用——10% latency overhead 可部署。\n\n### Weaknesses\n\n**W1 [critical]** 缺少与现有 constrained decoding 方法的直接实验对比——大量讨论 GCD/BoostCD/CRANE/GoLLIE 但无 head-to-head 实验。唯一\"对比\"是自行实现的 Trie-Only Baseline（Table 15）。§5.4 声称 BoostCD \"only 3% DR reduction\"来自方法论推断而非实验。\n\n**W2 [critical]** CF violation 增加在主文中被低估呈现——Llama DocRED CF 12.02% 完全未在主文出现，主文仅报 \"CF ≤ 1.3%\"。Abstract \"substantially reduces type violations\"在 DR↓+CF↑时高估 total violation burden 改善。\n\n**W3 [warning]** κ̄ 统计功效不足——n=2-3 schema，Figure 2 仅 4 点，p>0.05。\n\n**W4 [warning]** Entity registry 顺序依赖问题未量化——首次类型分配错误会传播，Limitations 承认但无量化。\n\n**W5 [warning]** WikiEvents fine-tuned 仅 20 文档，bootstrap CI 极宽。\n\n**W6 [warning]** S2（two-pass pipeline）花半页描述但实验中一句带过，无完整结果。\n\n**W7 [minor]** Proposition 1 证明中 position-based vs name-based 桥接缺乏形式化。\n**W8 [minor]** 70B AWQ INT4 量化对约束 enforcement 的影响未讨论。\n**W9 [minor]** \"five models\" 但实际 4 个模型族。\n\n### Questions\nQ1. Multi-type entity 如何处理？\nQ2. Triple-level fallback 触发比例？\nQ3. Llama DocRED 12.02% CF 根因？\nQ4. Constrained decoding + post-hoc filtering 组合？\nQ5. BoostCD \"3% DR reduction\" 来自分析还是实验？\n\n### Overall Assessment\n3.5 — Borderline Conference, Confidence 4/5\nSoundness 3.5, Excitement 3, Reproducibility 4.5",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1756 · 2026-05-22T10:54:54.990887+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1414
}
```

</details>

---


### Assistant

_source line 1757 · 2026-05-22T10:55:01.308014+00:00_

Step 2 交叉分享已派发。两位 Reviewer 正在审阅对方意见并准备 [AGREE]/[REBUT] 回应。等待返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1758 · 2026-05-22T10:55:03.892180+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall**: 3.5 (Borderline Conference)
- **核心判断**：系统化但新颖性有限的工程贡献，评估全面但 abstract/intro 存在数字不一致
- **3 个 Must-Fix**：(1) DR 降幅范围 45–99% vs 76–99% 自相矛盾，实际为 42–99%；(2) CF≤1.3% 被 70B 的 1.33% 违反；(3) 新颖性定位——核心组件均为已知技术，应重新定位为工程贡献
- **4 个 Should-Fix**：κ̄ 在 n=3 上声称"predictive"、WikiEvents n=20 统计效力不足、"deployment-grade"措辞被 CF trade-off 削弱、"enabling dependency"范围不清
- **Excitement**: 2.5/5——实用但概念创新有限

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1759 · 2026-05-22T10:55:16.407940+00:00_

交叉分享已派发，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1760 · 2026-05-22T10:56:55.189720+00:00_

[Reviewer 1 审稿意见]:
# Reviewer 1 交叉回应 Reviewer 2

## 逐条回应

### Weaknesses

**[AGREE] R2-W1**: DR 降幅数字不一致是事实错误，需修正。我在初审中遗漏了此问题。

**[AGREE] R2-W2**: CF ≤1.3% 被 70B 的 1.33% 违反，bound 需更新。与我的 W2（CF 呈现偏乐观）方向一致。

**[REBUT] R2-W3**: 新颖性评估过于严厉。Proposition 1 的 decidability taxonomy 在 constrained decoding 文献中确属首次——GCD 等方法隐含假设 CFG 可处理所有 IE 约束，但无人正式证明 cross-field type consistency 超出 CFG 表达能力。我维持 Excitement 3/5（R2 给 2.5/5）。但同意叙事应从 "novel architecture" 调整为 "first systematic study of compiling IE ontologies into composable constraints"。

**[AGREE] R2-W4**: κ̄ 统计功效不足，与我的 W3 完全一致。

**[AGREE] R2-W5**: WikiEvents n=20 不充分，与我的 W5 一致。补充：WikiEvents EE 不涉及 cross-field type constraints，仅验证 grammar layer。

**[AGREE] R2-W6**: "Deployment-grade" 叙事被 CF 削弱，与我的 W2 一致。

**[AGREE with nuance] R2-W7**: "Enabling dependency" 需区分 architectural dependency（始终成立）和 performance dependency（数据集相关）。

**[AGREE] R2-M1~M5**: 均为有效的编辑问题。

### 主要分歧

| 议题 | R1 | R2 | 分歧 |
|------|----|----|------|
| CF 呈现 | W2 critical | W2+W6 | 一致 |
| κ̄ claim | W3 warning | W4 warning | 一致 |
| WikiEvents | W5 warning | W5 warning | 一致 |
| 新颖性 | Excitement 3/5 | 2.5/5 | 轻度分歧 |
| baseline 实验对比 | **W1 critical（最大短板）** | 未提及 | **重要分歧** |

**最大分歧**：我将"缺少与 GCD/BoostCD 的 head-to-head 实验对比"列为 W1 [critical]，认为这是论文最重要的方法论缺陷。R2 未提及此问题。对于一篇定位为推进 constrained decoding for IE 的论文，仅有 trie-only baseline（Table 15）而无与现有方法的直接实验比较，说服力不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1761 · 2026-05-22T10:57:03.339049+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1762 · 2026-05-22T10:57:08.942953+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：R1 与 R2 在 CF 呈现、κ̄ 统计功效、WikiEvents 充分性上完全一致；在新颖性上有轻度分歧（我认为 Proposition 1 的 decidability taxonomy 有原创性，R2 评价偏低）；最大分歧是我将缺少 baseline 实验对比列为 critical weakness 而 R2 未提及。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1763 · 2026-05-22T10:57:16.730151+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 132

## Round 132

12 recorded events


### User

_source line 1764 · 2026-05-22T10:58:05.372354+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — Reviewer 1 Weaknesses & Questions

---

### Weaknesses 回应

**[AGREE] R1-W1: 缺少直接 baseline 实验对比**

同意这是一个值得指出的弱点，但我对严重程度的判断与 R1 略有不同。

同意的部分：论文讨论了 GCD/BoostCD/GoLLIE 等多个方法但无 head-to-head 实验，确实削弱了实验的说服力。Trie-Only Baseline（Table 15, Appendix）是自行实现而非官方代码复现。"BoostCD 仅 3% DR reduction"实际来自论文自己的 grammar-only ablation（Table 1, row 2: DR 15.37% → 14.84%），而非运行 BoostCD 代码——这一推断虽然在方法论上合理（两者约束范围相同：vocabulary membership），但应明确标注为"methodological equivalence"而非实验结论。

不同意的部分：我认为此问题的严重程度应区分对待：
1. **GCD → grammar-only ablation 作为代理是合理的**：GCD 的核心约束是 vocabulary membership via trie，这正是论文 grammar layer 单独运行时做的事（Table 1 row 2）。除非 GCD 的实现有额外优化（如 search strategy），grammar-only 行是一个公平的上界估计。
2. **GoLLIE 的缺失更严重**：GoLLIE 通过 annotation guidelines 作为 prompt 实现类型合规，是一个 training-based 但目标相近的 baseline。论文仅在 §6 定性讨论（"GoLLIE-7B eliminates DR but at severe coverage cost (R-F1=0.0, 46% empty output)"），但这个数字来源不清——是论文自己运行的结果还是 GoLLIE 论文中的数字？若是后者，在不同评估设置下的对比不公平。
3. **CRANE/EnriCo 作为 post-hoc 方法，与 decoding-time 方法不在同一类别**，缺少对比可以理解。

**建议**：至少运行 GCD 官方代码（或详细论证 grammar-only = GCD），并澄清 GoLLIE R-F1=0.0 的数据来源。

---

**[AGREE] R1-W2: CF violation 增加在主文中被低估呈现**

完全同意。这与我的 W6（"deployment-grade compliance"叙事被 CF trade-off 削弱）高度一致。

具体补充：
- Table 4（主文 page 7）**确实**展示了 Llama DocRED CF=12.02%，但正文叙述（§5.3）仅说"S1 introduces CF for calibrated models (up to 12.02%)"——这一句中"up to"弱化了严重性
- 更关键的是 Abstract 的叙事逻辑：先说"DR ≤ 0.09%"，再说"residual CF (≤1.3%) represents violation conversion"——1.3% 仅限 fine-tuned 设置，但 Abstract 未区分 zero-shot 和 fine-tuned CF。读者可能误解为所有配置下 CF ≤ 1.3%
- Abstract 说"substantially reduces type violations"，但 zero-shot 的 Total violation（DR+CF）在 DocRED Llama 上是 26.07+0.17=26.24%（unconstrained）→ 2.55+12.02=14.57%（S1），改善约 44%——虽然 DR 大幅下降，但 CF 的涌入使 total 改善远不如 DR 单项的"90%"那么惊人

R1 正确指出这是一个 framing 问题而非方法论错误——数据在 Table 4 中透明呈现，但叙事不匹配。

---

**[AGREE] R1-W3: κ̄ 统计功效不足**

完全同意，与我的 W4 一致。

补充一点 R1 未提及的问题：Figure 2（Appendix, page 21）的 dual-factor analysis 拟合 4 个数据点（3 models × 2 datasets 中去掉 outlier 后），p=0.058。但更根本的问题是：κ̄ 是在 schema 层面定义的（SciERC, DocRED, WikiEvents），而 Figure 2 的 x 轴是 κ × RV_baseline（model-dataset 交叉），这实际上是在用 model-dependent 的变量（RV_baseline）来补充 κ̄ 的不足，使得 κ̄ 本身的 predictive power 更加不明确。

---

**[AGREE] R1-W4: Entity registry 顺序依赖问题未量化**

同意这是方法论弱点。补充：

- CF 违规率本身就是这个问题的间接量化——CF 衡量的是"同一实体被分配不同类型"，这正是顺序依赖的表现
- 但 R1 的要求更精确：量化"首次类型分配错误的传播率"。这需要一个 counterfactual 实验（如果首次分配正确，后续 triple 的 DR/CF 会如何变化），论文未做
- Appendix C 的 causal tracing（Table 7）分析了 fallback 触发位置但不是 registry propagation 的量化
- 这个问题在 fine-tuned 设置下影响较小（CF ≤ 1.3%），但在 zero-shot 下（CF 最高 12.02%）可能是主要错误来源

---

**[AGREE] R1-W5: WikiEvents fine-tuned 仅 20 文档**

完全同意，与我的 W5 一致。我补充了一个具体建议：在 Table 5 caption 或 footnote 中加入 confidence interval。

---

**[AGREE] R1-W6: S2 花半页描述但实验中一句带过**

同意。§3.4 用约半页描述 S2（two-pass pipeline），但实验中仅 Table 1 有一行 S2 结果（SciERC zero-shot），§5.1 用一句话带过（"S2 achieves comparable DR (0.97%) but lower R-F1 and CF; we adopt S1"）。

这是典型的 space allocation 问题：
- 方案 A：删除 S2 的方法描述，节省空间用于更完整的 S1 评估或 Related Work
- 方案 B：保留 S2 并补充完整实验（至少 DocRED + fine-tuning）

当前处于两者之间的尴尬状态——描述了但未验证。在 8 页限制下，方案 A 可能更务实。

---

**[AGREE] R1-W7: Proposition 1 position-based vs name-based 桥接**

同意存在 gap，但认为严重程度低于 R1 可能暗示的水平。

Appendix O 最后一段明确讨论了这个简化（"The position-based formulation is a simplification that makes the pumping argument more transparent without weakening the conclusion"），并指出在实际系统中 name-based referencing 的核心论点不变——类型一致性仍然依赖跨位置的绑定关系，这是 CFG 无法表达的。

但"without weakening the conclusion"这一声明本身缺乏形式化证明。一个简短的 corollary 或 reduction 论证（name-based → position-based 的 reduction）会消除这个 gap。

---

**[AGREE] R1-W8: 70B AWQ INT4 量化影响未讨论**

同意。INT4 量化改变 logit 分布，可能影响 mask 在 boundary cases 的行为。具体而言：
- 量化后的 logit 精度降低可能使得原本被 mask 抑制的 token 在量化后的排名发生变化
- 论文的 70B 结果（DR=0% on both datasets, zero-shot）反而显示约束在量化模型上可能更强（因为量化降低了模型对 ontology 的 "记忆"，增加了对约束的依赖），但这是推测而非验证
- 简单的补救：加一句 disclaimer 即可

---

**[AGREE] R1-W9: "five models" 但实际 4 个**

同意。我仔细检查了全文，只找到 4 个模型：
1. Qwen3-8B
2. Llama-3.1-8B
3. Mistral-7B
4. Llama-3.3-70B-Instruct

Abstract 和 Introduction 都声称"five autoregressive LMs"，但 Limitations section 说"three 8B-class and one 70B-class model"=4。这是一个需要修正的事实错误。

可能的解释：早期版本可能包含第 5 个模型（如 Qwen-72B 或 Gemma），在修改过程中被删除但 abstract 数字未更新。

---

### Questions 回应

**[AGREE] R1-Q1: Multi-type entity 处理**

论文未明确讨论 multi-type entity（一个 entity 在 ontology 中合法地拥有多个类型，如 Person + Scientist）。当前的 entity registry 设计是 first-assignment-wins（§3.3: "each completed entry [h_i, τ_i] adds (n_i, τ_i) to D"），这意味着 multi-type entity 会被强制为单一类型。这对某些 ontology（如 DocRED 的 Wikidata types）可能导致 false positive CF violations。R1 提出此问题是合理的。

---

**[REBUT] R1-Q2: Triple-level fallback 触发比例**

论文实际上提供了 fallback 量化数据，R1 可能遗漏：
- Table 7（Appendix, page 19）: causal tracing 显示 SciERC 551 docs 上 18 个 residual DR violations 全部发生在 fallback positions（grammar-first fallback 触发时）
- §5.1 提到"token-level grammar-first fallback rate 0.46% at first-token positions"（SciERC）
- Appendix C（page 19-20）详细分解了 fallback 机制：token-level fallback rate 在 SciERC 为 0.46%，fallback 触发时的 type-bearing positions 中 50.8% 的 DR violations 来自 fallback

数据存在，但分散在多个 Appendix 中，主文确实未给出 consolidated 的 fallback 比例。R1 的问题可能源于信息分散而非缺失。

---

**[AGREE] R1-Q3: Llama DocRED 12.02% CF 根因**

论文在 Appendix C 有部分分析（CF-DR Trade-off 节）——CF 来自 per-entity sequential enforcement，当 DocRED 的高 κ̄ (0.842) 使得约束空间狭窄时，entity 的首次类型分配更容易与后续 triple 的 domain/range 要求冲突。但论文未单独分析"为什么 Llama 比 Qwen 高很多"（Qwen DocRED CF=2.57% vs Llama 12.02%）——这可能与 Llama 的 entity typing 能力较弱有关（Limitations 提到 "weaker entity typing"），导致首次分配错误率更高，进而通过 registry 传播。

---

**[AGREE] R1-Q4: Constrained decoding + post-hoc filtering 组合**

同意这是一个值得探索的方向。论文将两者定位为替代方案（§5.3: "Post-hoc filtering achieves DR=0% but with 15-74% rejection rates"），但实际上它们是互补的：constrained decoding 消除大部分 DR，post-hoc filtering 清理残余 CF。Appendix 的 post-hoc 对比（Table 12）显示两者组合可行，但主文未讨论。

---

**[AGREE] R1-Q5: BoostCD "3% DR reduction" 来源**

同意 R1 的质疑。§5.4 原文："Our grammar-only ablation (Table 1, row 2) implements the same constraints as GCD and BoostCD: RV/ET→0% but only 3% DR reduction vs. Full S1's 94%."

这是将自己的 grammar-only ablation 结果归因于 GCD/BoostCD 的约束范围等价性推断，而非运行 BoostCD 代码。推断逻辑本身成立（BoostCD 的约束范围确实限于 vocabulary membership），但表述方式容易被误读为实验结果。应标注为 analytical equivalence。

---

### 综合评估：R2 与 R1 的分歧点

| 议题 | R1 | R2 | 分歧程度 |
|------|-----|-----|---------|
| 缺少 baseline 的严重性 | Critical | Should-Fix | **中等分歧** — R2 认为 grammar-only 作为 GCD 代理是合理的，但同意 GoLLIE 缺失更严重 |
| CF 主文呈现问题 | Critical | Should-Fix (我的 W6) | **轻微分歧** — 都认为是问题，R1 定为 critical，R2 定为 warning。CF 数据在 Table 4 中透明呈现，问题是叙事 framing 而非隐瞒 |
| κ̄ 统计功效 | Warning | Warning (我的 W4) | **无分歧** — 都认为 n=3 不够 |
| WikiEvents 评估 | Warning | Warning (我的 W5) | **无分歧** — 都认为 n=20 太弱 |
| 新颖性 | 未重点讨论 (Excitement 3/5) | Critical (我的 W3) | **分歧** — R1 侧重方法严谨性不太关注新颖性，R2 认为核心组件均为已知技术的集成是主要弱点 |
| 总分 | 3.5 Borderline Conference | 3.5 Borderline Conference | **无分歧** |

R1 和 R2 在 overall 评分上一致（3.5 Borderline Conference），但关注点互补：R1 聚焦方法严谨性和实验设计缺陷，R2 聚焦新颖性和叙事一致性。两份 review 共同揭示的核心问题是：*论文的评估全面性是其最大优势，但 abstract/intro 的叙事精确性和概念新颖性是制约接收的主要因素。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1765 · 2026-05-22T10:58:27.935702+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1766 · 2026-05-22T10:58:28.443397+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T10:42:38.655628+00:00\", \"completed_at\": \"2026-05-22T10:45:57.734897+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"连续 2 页纯文本（Title/Abstract/Intro/Background），直到第 3 页才出现首个 display item（Figure 1）。审稿人在前 2 分钟内仅看到文字墙，缺少快速锚定的视觉元素\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（全宽架构概览图）在第 3 页出现，刚好在 3 页阈值内。图示清晰传达了两层约束架构的核心 idea，caption 自包含，颜色方案柔和可读。作为首个 display item 质量合格\"}, {\"severity\": \"warning\", \"dimension\": \"pages 4-5\", \"message\": \"连续 2 页纯文本（Method §3.2-§3.4 + Experiments setup），无公式 display、无图表穿插。方法描述段落缺少形式化公式的 display math 断点，阅读体验单调\"}, {\"severity\": \"warning\", \"dimension\": \"pages 6-7\", \"message\": \"Display items 分布严重不均：5 张表格全部集中在这 2 页。Page 7 尤其密集——Tables 3、4、5 三张表挤在一页，视觉压迫感强。与 pages 1-2、4-5 的纯文本形成极端反差\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主正文最后一页（Related Work + Discussion/Conclusion）全部为纯文本，没有视觉元素收尾。与 pages 8-9（加上 Limitations）形成连续 2 页纯文本\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主正文 8 页仅 1 张 figure + 5 张 table = 6 个 display items，在实证论文 5-8 个的合理范围内，但 figure 数量偏少（仅 1 张）。核心结果全部以 table 呈现，缺少直观的可视化图表（如性能对比柱状图或趋势线图）\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 和 Table 2 使用 booktabs 风格，最优值加粗，∆DR 列标注相对变化，小数位数一致。排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Tables 3-5 同样使用 booktabs 风格，加粗标注一致。但三表同页导致字号偏小，Table 5 尤其紧凑\"}, {\"severity\": \"info\", \"dimension\": \"pages 21, 24, 28\", \"message\": \"附录中 Figure 2（DR vs Schema Restrictiveness 散点图）、Figure 3（per-relation DR 柱状图）、Figure 4（beam width vs R-F1 曲线图）质量都不错——尤其 Figure 2 或 Figure 3 若能提升到主正文，可以打破 pages 6-7 的纯表格单调性并给审稿人更直观的结果感知\"}, {\"severity\": \"info\", \"dimension\": \"page 30\", \"message\": \"Table 29 使用红绿色标注（删除线+修正）展示 OntoCoDec 的纠错案例，视觉效果好，但需注意色盲可辨性——纯红绿对比对红绿色盲不友好，建议辅以形状/下划线标记\"}, {\"severity\": \"
…[truncated 449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-22T10:58:28.443855+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1768 · 2026-05-22T10:58:29.598568+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 1769 · 2026-05-22T10:58:29.598954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1770 · 2026-05-22T10:58:29.649766+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R16 Action Matrix D079 dispatched, 2026-05-21
3	
4	# ============================================================
5	# Round 16 Must-Fix
6	# ============================================================
7	
8	- id: "R15-MF1"
9	  summary: "缺少与 GCD/BoostCD/CRANE/IterGen/EnriCo 等同类 constrained decoding 方法的实验对比（连续 5 轮 R12-R16）"
10	  category: experiment
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 12
14	  last_seen_round: 16
15	  mentions:
16	    - round: 12
17	      reviewers: [1, 2]
18	      note: "R12-SF2: should-fix"
19	    - round: 13
20	      reviewers: [1, 2]
21	      note: "R13-MF3: 升级为 must-fix"
22	    - round: 14
23	      reviewers: [1, 2]
24	      note: "R14-MF1: grammar-only ablation reframed as Level 1 对比"
25	    - round: 15
26	      reviewers: [1, 2]
27	      note: "R15-MF1: §5 显式 BoostCD/GCD 对比段落。仍不够——未运行外部代码。"
28	    - round: 16
29	      reviewers: [1, 2]
30	      note: "R16-MF1: 连续 5 轮 critical。grammar-only proxy 不被接受。"
31	  action_items:
32	    - round: 14
33	      action: "grammar-only ablation reframed as BoostCD-equivalent Level 1"
34	      assigned_to: paper_agent
35	      status: completed
36	    - round: 15
37	      action: "§5 新增显式对比小节"
38	      assigned_to: paper_agent
39	      status: completed
40	    - round: 16
41	      action: "实现 trie-based GCD-equivalent baseline (同模型同数据控制变量)，SciERC 4 configs 对比 trie vs grammar-only vs full S1"
42	      assigned_to: agent + paper_agent
43	      status: in_progress
44	  resolution: ""
45	  resolution_round: null
46	
47	- id: "R16-MF2"
48	  summary: "Abstract '94–100% DR reduction' 与 Table 2 数据不一致（Llama SciERC fine-tuned 实际 91.9%）"
49	  category: framing
50	  severity: critical
51	  status: in_progress
52	  first_raised_round: 16
53	  last_seen_round: 16
54	  mentions:
55	    - round: 16
56	      reviewers: [2]
57	      note: "R2-N1 发现，R1 交叉 AGREE。实际范围 92-100%。"
58	  action_items:
59	    - round: 16
60	      ac
…[truncated 9189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1771 · 2026-05-22T11:01:32.282095+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R17 Fresh Review, 2026-05-22\n\n# ============================================================\n# Round 17 Must-Fix\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD 等同类 constrained decoding 方法的直接实验对比（连续 6 轮 R12-R17）\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: should-fix\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF3: 升级为 must-fix\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1: grammar-only ablation reframed as Level 1 对比\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF1: §5 显式 BoostCD/GCD 对比段落。仍不够——未运行外部代码。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16-MF1: 连续 5 轮 critical。grammar-only proxy 不被接受。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1 列为 critical W1，R2 交叉同意但降为 should-fix（grammar-only 作为 GCD 代理合理，但 GoLLIE 缺失更严重）。Trie-Only Baseline (Table 15) 被视为自行实现简化版而非公平对比。BoostCD '3% DR reduction' 被指出为方法论推断非实验结果。\"\n  action_items:\n    - round: 14\n      action: \"grammar-only ablation reframed as BoostCD-equivalent Level 1\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 15\n      action: \"§5 新增显式对比小节\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 16\n      action: \"实现 trie-based GCD-equivalent baseline\"\n      assigned_to: agent + paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF2\"\n  summary: \"Abstract/Intro DR 降幅范围自相矛盾（Abstract '45-99%' vs Intro '76-99% for calibrated models' vs 实际 42-99%）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-N1: '94-100%' vs Table 2 实际 92-100%\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 问题变异——R16 修正后引入新不一致。Abstract '45-99%' 排除了 Mistral DocRED 42%（未说明）。Intro '76-99% for calibrated models' 但 Qwen DocRED（calibrated）仅 45%。R1 交叉 AGREE。\"\n  action_items:\n    - round: 16\n      action: \"Abstract + §1 修正为 '92-100%'\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 17\n      action: \"统一为 '42-99%' 或明确限定条件并说明排除理由\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF3\"\n  summary: \"CF 率在 Abstract/主文中呈现偏乐观——zero-shot 最差 12.02% 未在主文叙事中出现\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W2: DR↔CF trade-off 选择性报告\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: 升级为 critical。CF 范围应覆盖全数据集。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W2 critical + R2-W6 warning。Abstract 'substantially reduces type violations' 在 DR↓+CF↑时高估改善。主文仅报 CF≤1.3%（FT），zero-shot Llama DocRED 12.02% 完全未在主文叙述中出现。Total violation (DR+CF) 改善 ~44% 远不如 DR 单项 90%。数据在 Table 4 透明呈现，问题是叙事 framing。\"\n  action_items:\n    - round: 16\n      action: \"Abstract CF 改为全范围覆盖\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-MF1\"\n  summary: \"Abstract CF≤1.3% bound 被 70B LoRA CF=1.33% 违反\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W2 发现，R1 交叉 AGREE。差异虽小但 abstract 将其作为 bound 呈现。\"\n  action_items:\n    - round: 17\n      action: \"修正为 '≤1.4%' 或限定为 8B 模型\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-MF2\"\n  summary: \"'five autoregressive LMs' 但实际仅 4 个模型族——事实错误\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W9 + R2 交叉 AGREE。Abstract/Intro 声称 'five' 但全文仅 Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B = 4 个。Limitations 也说 'three 8B-class and one 70B-class model'=4。疑似早期版本残留。\"\n  action_items:\n    - round: 17\n      action: \"修正 'five' → 'four' 或补充第 5 个模型\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 17 Major Issues\n# ============================================================\n\n- id: \"R16-W1\"\n  summary: \"κ̄ 统计支撑不足：n=3 schema，Figure 2 仅 4 点 p=0.058\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: n=2→n=3 但仍无统计推断力。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W3 + R2-W4 一致。Abstract 'establishing...as a predictive factor' 过度声称。R2 补充：Figure 2 x 轴用 κ×RV_baseline (model-dependent) 补充 κ̄ 的不足，使 κ̄ 自身 predictive power 更加不明确。\"\n  action_items:\n    - round: 16\n      action: \"κ̄ 降为 inline，加 n=3 限定\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 17\n      action: \"Abstract 'establishing...predictive factor' → 'introducing...descriptive metric'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档，统计效力严重不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: 'demonstrate generalization' → 'initial evidence'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W5 + R2-W5 一致。Bootstrap CI 极宽，per-document variance >0.5。R1 补充：WikiEvents EE 不涉及 cross-field type constraints，仅验证 grammar layer。建议 Table 5 加 CI。\"\n  action_items:\n    - round: 16\n      action: \"'demonstrate generalization' → 'provide initial evidence'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 17\n      action: \"Table 5 caption/footnote 加 confidence interval\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"新颖性定位——核心组件（XGrammar + runtime type check）均为已知技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: Divergence R1 3.5 vs R2 2.5\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-W3 critical（Excitement 2.5/5），R1 REBUT 认为 decidability taxonomy 有原创性（Excitement 3/5）。分歧持续。Director 取中间立场：系统集成 + 全面评估是贡献，但叙事应从 'novel architecture' 转向 'first systematic study of compiling IE ontologies'。\"\n  action_items:\n    - round: 16\n      action: \"§1 reframe: 'formalize a well-known intuition'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 17\n      action: \"贡献重心从 'novel architecture' 转向 'first systematic study + empirical findings'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"'Deployment-grade compliance' 叙事被 CF trade-off 结构性削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W6，R1 交叉 AGREE。Abstract/Intro 反复使用 'deployment-grade type compliance'，但 CF 是 DR enforcement 的系统性副产品。zero-shot 最高 12.02%，FT 最高 1.18%。Beam search 在 DocRED 仍有 CF 0.93%。'Deployment-grade' 暗示接近零违规，系统在 CF 维度做不到。\"\n  action_items:\n    - round: 17\n      action: \"软化为 'near-complete DR elimination with residual CF trade-off' 或明确定义 'deployment-grade'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"'Enabling dependency' 声明范围不清——'neither layer alone exceeds 24%' 仅限 SciERC\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W7，R1 AGREE with nuance（区分 architectural vs performance dependency）。DocRED grammar-only 增加 DR 42%（18.46→26.17%），与 SciERC 模式截然不同。Intro 表述让读者误解为通用结论。\"\n  action_items:\n    - round: 17\n      action: \"改为 'on SciERC, neither layer alone exceeds 24%'，讨论 DocRED grammar-only DR 增加原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"Entity registry 顺序依赖（首次类型分配错误传播）未量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W4，R2 交叉 AGREE。Limitations 承认 'impact of such propagation has not been evaluated' 但无量化。CF 是间接量化但不等价于 propagation rate。需 counterfactual 实验。FT 下影响小（CF≤1.3%），ZS 下可能是主要错误来源。\"\n  action_items:\n    - round: 17\n      action: \"Post-hoc 分析现有输出中首次提及错误率和传播频率\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"S2 (two-pass pipeline) 花半页描述但实验中一句带过\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W6，R2 AGREE。§3.4 半页描述但仅 Table 1 一行结果。建议方案 A（删除描述节省空间）或方案 B（补充完整实验）。当前两者之间的尴尬状态。8 页限制下方案 A 更务实。\"\n  action_items:\n    - round: 17\n      action: \"选择方案 A（压缩§3.4）或方案 B（补充 DocRED+FT S2 结果）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"70B 评估单薄——仅 AWQ INT4，量化对约束影响未讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"CF 飙升未分析。标注 feasibility check。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W8 minor。INT4 量化改变 logit 分布可能影响 mask boundary cases。简单补救：加 disclaimer。\"\n  action_items:\n    - round: 16\n      action: \"标注 'feasibility check'；分析 CF 飙升原因\"\n      assigned_to: agent + paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 17 Minor\n# ============================================================\n\n- id: \"R16-M2\"\n  summary: \"§6 Related Work 仅半栏，严重依赖 Appendix B\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-M1，R1 AGREE。主文读者无法仅从 §6 评估相关工作覆盖充分性。建议将 Appendix B 中 GCD/GoLLIE/EnriCo 的关键对比移入主文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"术语不统一：'S1'/'Full S1' 交替使用；'enforcement' vs 'guarantee' 残留\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17: R2-M2。'S1' vs 'Full S1' 在 §5.1 和 §5.4 中不统一。\"\n  action_items:\n    - round: 16\n      action: \"术语统一\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M4\"\n  summary: \"引用真实性——regino2025kgcurator 和 formattax2026 待验证\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17: R2 验证全部 46 个 bib 条目——所有引用来自真实论文/预印本。未发现伪造引用。\"\n  action_items:\n    - round: 16\n      action: \"验证引用存在\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"Figure 1 信息密度过高，同时展示两层内部机制\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-M3。考虑分为两个子图或简化。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M2\"\n  summary: \"Table 4 Mistral CF=56.87% dagger 脚注解释位置不佳\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-M4。读者首次看到时困惑——建议在 caption 中更早引入 'poor calibration' 背景。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M3\"\n  summary: \"主文首次引用 '48% predictions discarded' 未 cite 来源表格\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-M5。Introduction 中 '48%' 仅在 Appendix 有详细支撑。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W6\"\n  summary: \"Proposition 1 bounded/unbounded gap——position-based vs name-based 桥接缺乏形式化\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"有限集 regular 但 DFA 指数增长\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W7 minor。Appendix O 最后一段讨论了简化但 'without weakening the conclusion' 缺乏 formal proof。R2 AGREE 但认为严重程度低——一个简短 corollary/reduction 即可消除 gap。\"\n  action_items:\n    - round: 16\n      action: \"§3 加实际不可行性说明\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved\n# ============================================================\n\n- id: \"R15-MF2\"\n  summary: \"'guarantee' 措辞系统性 overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"R15-R16 guarantee→enforcement 全文替换完成。\"\n  resolution_round: 16\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"R15 修复，≤8 页。R17 确认正文 8 页。\"\n  resolution_round: 17\n\n- id: \"R15-W6\"\n  summary: \"Fallback causal tracing 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix causal tracing table 已添加。R17 Reviewer 1 S3 确认。\"\n  resolution_round: 16\n\n- id: \"R15-W7\"\n  summary: \"仅英语数据集评估，跨语言泛化未讨论\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Limitations 已添加 English-only + CJK 差异。R17 Reviewer 2 S3 确认 Limitations 全面。\"\n  resolution_round: 16\n\n- id: \"R15-W8\"\n  summary: \"Post-hoc filtering 对比不够公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"已添加说明。R17 未复发。\"\n  resolution_round: 16\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Intro 被系统性低估\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 修复。R16-MF3/R17 以变异形式复发。\"\n  resolution_round: 14\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents FT n=20 + Contribution 3 措辞过度\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 拆分 RE systematic + EE preliminary。R16-W3/R17 继续追踪。\"\n  resolution_round: 14\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 定位过高\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 移出 Contribution。R16-W1/R17 继续追踪 claim 强度。\"\n  resolution_round: 14\n\n- id: \"R14-M3\"\n  summary: \"Entity registry 顺序依赖未量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"100% ordering confirmed (EBNF 结构保证)。R17 以 R17-W3 形式复发——要求量化传播率。\"\n  resolution_round: 14\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"FT fallback ≤0.11% 已补充。R17 未复发。\"\n  resolution_round: 14\n\n- id: \"R16-W2\"\n  summary: \"DocRED zero-shot DR 仅降 45% 与 narrative 张力\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§1 contribution 排除 DocRED 45%\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 并入 R16-MF2 (DR 范围不一致) 一并处理\"\n  action_items:\n    - round: 16\n      action: \"§1 contribution 涵盖 '45-99% ZS'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M3\"\n  summary: \"'calibrated models' 排除条件不透明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17: R2-W1 涉及——Intro '76-99% for calibrated models' 但 Qwen DocRED (calibrated) 仅 45%\"\n  action_items:\n    - round: 16\n      action: \"§1 明确排除条件\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R17 Fresh Review, 2026-05-22\n\n# ============================================================\n# Round 17 Must-Fix\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD 等同类 constrained decoding 方法的直接实验对比（连续 6 轮 R12-R17）\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: should-fix\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13-MF3: 升级为 must-fix\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1: grammar-only ablation reframed as Level 1 对比\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-MF1: §5 显式 BoostCD/GCD 对比段落。仍不够——未运行外部代码。\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16-MF1: 连续 5 轮 critical。grammar-only proxy 不被接受。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1 列为 critical W1，R2 交叉同意但降为 should-fix（grammar-only 作为 GCD 代理合理，但 GoLLIE 缺失更严重）。Trie-Only Baseline (Table 15) 被视为自行实现简化版而非公平对比。BoostCD '3% DR reduction' 被指出为方法论推断非实验结果。\"\n  action_items:\n    - round: 14\n      action: \"grammar-only ablation reframed as BoostCD-equivalent Level 1\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 15\n      action: \"§5 新增显式对比小节\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 16\n      action: \"实现 trie-based GCD-equivalent baseline\"\n      assigned_to: agent + paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF2\"\n  summary: \"Abstract/Intro DR 降幅范围自相矛盾（Abstract '45-99%' vs Intro '76-99% for calibrated models' vs 实际 42-99%）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R2-N1: '94-100%' vs Table 2 实际 92-100%\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 问题变异——R16 修正后引入新不一致。Abstract '45-99%' 排除了 Mistral DocRED 42%（未说明）。Intro '76-99% for calibrated models' 但 Qwen DocRED（calibrated）仅 45%。R1 交叉 AGREE。\"\n  action_items:\n    - round: 16\n      action: \"Abstract + §1 修正为 '92-100%'\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 17\n      action: \"统一为 '42-99%' 或明确限定条件并说明排除理由\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-MF3\"\n  summary: \"CF 率在 Abstract/主文中呈现偏乐观——zero-shot 最差 12.02% 未在主文叙事中出现\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15-W2: DR↔CF trade-off 选择性报告\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: 升级为 critical。CF 范围应覆盖全数据集。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W2 critical + R2-W6 warning。Abstract 'substantially reduces type violations' 在 DR↓+CF↑时高估改善。主文仅报 CF≤1.3%（FT），zero-shot Llama DocRED 12.02% 完全未在主文叙述中出现。Total violation (DR+CF) 改善 ~44% 远不如 DR 单项 90%。数据在 Table 4 透明呈现，问题是叙事 framing。\"\n  action_items:\n    - round: 16\n      action: \"Abstract CF 改为全范围覆盖\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-MF1\"\n  summary: \"Abstract CF≤1.3% bound 被 70B LoRA CF=1.33% 违反\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W2 发现，R1 交叉 AGREE。差异虽小但 abstract 将其作为 bound 呈现。\"\n  action_items:\n    - round: 17\n      action: \"修正为 '≤1.4%' 或限定为 8B 模型\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-MF2\"\n  summary: \"'five autoregressive LMs' 但实际仅 4 个模型族——事实错误\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W9 + R2 交叉 AGREE。Abstract/Intro 声称 'five' 但全文仅 Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B = 4 个。Limitations 也说 'three 8B-class and one 70B-class model'=4。疑似早期版本残留。\"\n  action_items:\n    - round: 17\n      action: \"修正 'five' → 'four' 或补充第 5 个模型\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 17 Major Issues\n# ============================================================\n\n- id: \"R16-W1\"\n  summary: \"κ̄ 统计支撑不足：n=3 schema，Figure 2 仅 4 点 p=0.058\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: n=2→n=3 但仍无统计推断力。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W3 + R2-W4 一致。Abstract 'establishing...as a predictive factor' 过度声称。R2 补充：Figure 2 x 轴用 κ×RV_baseline (model-dependent) 补充 κ̄ 的不足，使 κ̄ 自身 predictive power 更加不明确。\"\n  action_items:\n    - round: 16\n      action: \"κ̄ 降为 inline，加 n=3 限定\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 17\n      action: \"Abstract 'establishing...predictive factor' → 'introducing...descriptive metric'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档，统计效力严重不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: 'demonstrate generalization' → 'initial evidence'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W5 + R2-W5 一致。Bootstrap CI 极宽，per-document variance >0.5。R1 补充：WikiEvents EE 不涉及 cross-field type constraints，仅验证 grammar layer。建议 Table 5 加 CI。\"\n  action_items:\n    - round: 16\n      action: \"'demonstrate generalization' → 'provide initial evidence'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 17\n      action: \"Table 5 caption/footnote 加 confidence interval\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"新颖性定位——核心组件（XGrammar + runtime type check）均为已知技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: Divergence R1 3.5 vs R2 2.5\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-W3 critical（Excitement 2.5/5），R1 REBUT 认为 decidability taxonomy 有原创性（Excitement 3/5）。分歧持续。Director 取中间立场：系统集成 + 全面评估是贡献，但叙事应从 'novel architecture' 转向 'first systematic study of compiling IE ontologies'。\"\n  action_items:\n    - round: 16\n      action: \"§1 reframe: 'formalize a well-known intuition'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 17\n      action: \"贡献重心从 'novel architecture' 转向 'first systematic study + empirical findings'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"'Deployment-grade compliance' 叙事被 CF trade-off 结构性削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W6，R1 交叉 AGREE。Abstract/Intro 反复使用 'deployment-grade type compliance'，但 CF 是 DR enforcement 的系统性副产品。zero-shot 最高 12.02%，FT 最高 1.18%。Beam search 在 DocRED 仍有 CF 0.93%。'Deployment-grade' 暗示接近零违规，系统在 CF 维度做不到。\"\n  action_items:\n    - round: 17\n      action: \"软化为 'near-complete DR elimination with residual CF trade-off' 或明确定义 'deployment-grade'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"'Enabling dependency' 声明范围不清——'neither layer alone exceeds 24%' 仅限 SciERC\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W7，R1 AGREE with nuance（区分 architectural vs performance dependency）。DocRED grammar-only 增加 DR 42%（18.46→26.17%），与 SciERC 模式截然不同。Intro 表述让读者误解为通用结论。\"\n  action_items:\n    - round: 17\n      action: \"改为 'on SciERC, neither layer alone exceeds 24%'，讨论 DocRED grammar-only DR 增加原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W3\"\n  summary: \"Entity registry 顺序依赖（首次类型分配错误传播）未量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W4，R2 交叉 AGREE。Limitations 承认 'impact of such propagation has not been evaluated' 但无量化。CF 是间接量化但不等价于 propagation rate。需 counterfactual 实验。FT 下影响小（CF≤1.3%），ZS 下可能是主要错误来源。\"\n  action_items:\n    - round: 17\n      action: \"Post-hoc 分析现有输出中首次提及错误率和传播频率\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W4\"\n  summary: \"S2 (two-pass pipeline) 花半页描述但实验中一句带过\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W6，R2 AGREE。§3.4 半页描述但仅 Table 1 一行结果。建议方案 A（删除描述节省空间）或方案 B（补充完整实验）。当前两者之间的尴尬状态。8 页限制下方案 A 更务实。\"\n  action_items:\n    - round: 17\n      action: \"选择方案 A（压缩§3.4）或方案 B（补充 DocRED+FT S2 结果）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"70B 评估单薄——仅 AWQ INT4，量化对约束影响未讨论\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"CF 飙升未分析。标注 feasibility check。\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W8 minor。INT4 量化改变 logit 分布可能影响 mask boundary cases。简单补救：加 disclaimer。\"\n  action_items:\n    - round: 16\n      action: \"标注 'feasibility check'；分析 CF 飙升原因\"\n      assigned_to: agent + paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 17 Minor\n# ============================================================\n\n- id: \"R16-M2\"\n  summary: \"§6 Related Work 仅半栏，严重依赖 Appendix B\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R2-M1，R1 AGREE。主文读者无法仅从 §6 评估相关工作覆盖充分性。建议将 Appendix B 中 GCD/GoLLIE/EnriCo 的关键对比移入主文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"术语不统一：'S1'/'Full S1' 交替使用；'enforcement' vs 'guarantee' 残留\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17: R2-M2。'S1' vs 'Full S1' 在 §5.1 和 §5.4 中不统一。\"\n  action_items:\n    - round: 16\n      action: \"术语统一\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M4\"\n  summary: \"引用真实性——regino2025kgcurator 和 formattax2026 待验证\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17: R2 验证全部 46 个 bib 条目——所有引用来自真实论文/预印本。未发现伪造引用。\"\n  action_items:\n    - round: 16\n      action: \"验证引用存在\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M1\"\n  summary: \"Figure 1 信息密度过高，同时展示两层内部机制\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-M3。考虑分为两个子图或简化。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M2\"\n  summary: \"Table 4 Mistral CF=56.87% dagger 脚注解释位置不佳\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-M4。读者首次看到时困惑——建议在 caption 中更早引入 'poor calibration' 背景。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-M3\"\n  summary: \"主文首次引用 '48% predictions discarded' 未 cite 来源表格\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R2-M5。Introduction 中 '48%' 仅在 Appendix 有详细支撑。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W6\"\n  summary: \"Proposition 1 bounded/unbounded gap——position-based vs name-based 桥接缺乏形式化\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"有限集 regular 但 DFA 指数增长\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: R1-W7 minor。Appendix O 最后一段讨论了简化但 'without weakening the conclusion' 缺乏 formal proof。R2 AGREE 但认为严重程度低——一个简短 corollary/reduction 即可消除 gap。\"\n  action_items:\n    - round: 16\n      action: \"§3 加实际不可行性说明\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved\n# ============================================================\n\n- id: \"R15-MF2\"\n  summary: \"'guarantee' 措辞系统性 overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"R15-R16 guarantee→enforcement 全文替换完成。\"\n  resolution_round: 16\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 15\n  resolution: \"R15 修复，≤8 页。R17 确认正文 8 页。\"\n  resolution_round: 17\n\n- id: \"R15-W6\"\n  summary: \"Fallback causal tracing 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Appendix causal tracing table 已添加。R17 Reviewer 1 S3 确认。\"\n  resolution_round: 16\n\n- id: \"R15-W7\"\n  summary: \"仅英语数据集评估，跨语言泛化未讨论\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"Limitations 已添加 English-only + CJK 差异。R17 Reviewer 2 S3 确认 Limitations 全面。\"\n  resolution_round: 16\n\n- id: \"R15-W8\"\n  summary: \"Post-hoc filtering 对比不够公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"已添加说明。R17 未复发。\"\n  resolution_round: 16\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Intro 被系统性低估\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 修复。R16-MF3/R17 以变异形式复发。\"\n  resolution_round: 14\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents FT n=20 + Contribution 3 措辞过度\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 拆分 RE systematic + EE preliminary。R16-W3/R17 继续追踪。\"\n  resolution_round: 14\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 定位过高\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R13 移出 Contribution。R16-W1/R17 继续追踪 claim 强度。\"\n  resolution_round: 14\n\n- id: \"R14-M3\"\n  summary: \"Entity registry 顺序依赖未量化\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"100% ordering confirmed (EBNF 结构保证)。R17 以 R17-W3 形式复发——要求量化传播率。\"\n  resolution_round: 14\n\n- id: \"R14-DIV1\"\n  summary: \"Fallback 36.6% 严重度分歧\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  resolution: \"FT fallback ≤0.11% 已补充。R17 未复发。\"\n  resolution_round: 14\n\n- id: \"R16-W2\"\n  summary: \"DocRED zero-shot DR 仅降 45% 与 narrative 张力\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§1 contribution 排除 DocRED 45%\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: 并入 R16-MF2 (DR 范围不一致) 一并处理\"\n  action_items:\n    - round: 16\n      action: \"§1 contribution 涵盖 '45-99% ZS'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-M3\"\n  summary: \"'calibrated models' 排除条件不透明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17: R2-W1 涉及——Intro '76-99% for calibrated models' 但 Qwen DocRED (calibrated) 仅 45%\"\n  action_items:\n    - round: 16\n      action: \"§1 明确排除条件\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1772 · 2026-05-22T11:01:32.434191+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 16728}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1773 · 2026-05-22T11:04:12.780206+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人圆桌\n- Reviewer 1: 方法严谨性 + 实验设计\n- Reviewer 2: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE ontology 自动编译为 token-level 解码约束的两层架构：grammar layer（基于 XGrammar 的 CFG，保证 JSON 结构 + 词表合规）和 semantic layer（有状态 entity registry 实现 cross-field 类型约束）。论文在 3 个数据集（SciERC, DocRED, WikiEvents）、4 个模型族（7B–70B）上系统评估，报告 LoRA + S1 可将 DR 降至 ≤0.09%，但引入 CF 违规（FT ≤1.3%, ZS 最高 12.02%）作为 violation conversion 的结构性代价。附 24 页 appendix 含消融、causal tracing、scalability 等详细分析。\n\n---\n\n## Strengths\n\n**S1. 系统化的评估覆盖度（两位 Reviewer 一致认可）**\n3 数据集 × 4+ 模型 × ZS/FT × greedy/beam/sampling，加上五路消融（Table 1）、四路消融（Table 3）、跨模型验证（Table 4）、per-relation breakdown、causal tracing（Table 7）、dual-factor analysis（Figure 2）。Bootstrap 10,000 iterations + Bonferroni correction。在同类工作中属于上乘。\n\n**S2. 诚实透明的 Limitations 和 CF-DR trade-off 分析**\nAppendix C 的 causal tracing、CF-priority fallback 消融（Table 8）、dual-factor 定量分析坦诚承认 CF-DR trade-off 是结构性而非可调参数。Limitations section 覆盖了约束范围、评估覆盖、工程约束等关键限制。\n\n**S3. 理论基础有原创性**\nDecidability taxonomy（Level 1/2/3）将 IE 类型约束按可判定性分层，Proposition 1（Appendix O）通过 pumping lemma 证明 cross-field type consistency 超出 CFG 表达能力，为两层架构提供形式化依据。\n\n**S4. 低运行时开销**\nGreedy S1 仅增加 10–13% latency，constraint compilation < 0.5s，scalability benchmark 到 200 entity types / 1,000 relations 保持 2–3% overhead。\n\n**S5. 可复现性优秀**\nAppendix G 报告硬件/种子/超参，3 seeds cross-GPU variance（Table 24），prompt templates 完整展示（Table 6），承诺开源代码。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] Abstract/Intro DR 降幅数字自相矛盾 [AGREE: R1+R2]**\n- Abstract: \"45–99% DR reduction\"\n- Introduction: \"DR drops 76–99% for calibrated models\"\n- Table 4 实际全范围: **42–99%**（Mistral DocRED 42% 被排除未说明）\n- DocRED Qwen（calibrated model）仅 45%，远低于 Intro 声称的 76% 下界\n- 建议：统一为 \"42–99%\" 或明确限定条件并说明排除理由\n\n**MF2. [critical] Abstract CF ≤1.3% bound 被 70B LoRA CF=1.33% 违反 [AGREE: R1+R2]**\n- 差异虽小（0.03pp），但 Abstract 将其作为 bound 呈现\n- 70B 是论文明确涵盖的配置（Abstract 说 \"five autoregressive LMs (7–70B)\"）\n- 建议：修正为 \"≤1.4%\" 或限定为 8B 模型\n\n**MF3. [critical] CF violation 在主文叙事中被系统性低估 [AGREE: R1+R2]**\n- Zero-shot Llama DocRED CF 高达 **12.02%**，但主文 §5.1-§5.3 叙述中仅出现 \"CF ≤ 1.3%\"（仅限 FT）\n- Abstract \"substantially reduces type violations\"——但 zero-shot DocRED Llama total violation (DR+CF) 从 26.24% 仅降至 14.57%（改善 ~44%），远不如 DR 单项 90% 降幅\n- 数据在 Table 4 中透明呈现，**问题是叙事 framing 而非数据隐瞒**\n- 建议：主文 §5 明确报告 CF 最差情况，Abstract 区分 ZS 和 FT CF 范围\n\n**MF4. [critical] \"five autoregressive LMs\" 但实际仅 4 个模型——事实错误 [AGREE: R1+R2]**\n- 全文仅出现 Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B = 4 个模型\n- Limitations 也说 \"three 8B-class and one 70B-class model\" = 4\n- 疑似早期版本残留\n- 建议：修正 \"five\" → \"four\"\n\n**MF5. [critical/should-fix, 分歧] 缺少与现有 constrained decoding 方法的直接实验对比**\n- 论文大量讨论 GCD/BoostCD/CRANE/GoLLIE（§6, Appendix B），但无 head-to-head 实验\n- 唯一\"对比\"是自行实现的 Trie-Only Baseline（Table 15, Appendix D）\n- §5.4 \"BoostCD only 3% DR reduction\" 来自方法论等价推断（grammar-only ablation），非运行 BoostCD 代码\n- **分歧**: R1 列为 critical（最大短板），R2 交叉认为 should-fix（grammar-only 作为 GCD 代理合理，但 GoLLIE 缺失更严重）\n- **Director 判定**: 维持 critical——对于定位为推进 constrained decoding for IE 的论文，缺少 head-to-head 基准对比是核心实验缺口。grammar-only 消融的等价推断在方法论上可辩护，但在实际评审中说服力不足，尤其是该问题已被多轮审稿反复指出。至少应运行 GCD 官方代码或明确论证 grammar-only = GCD 的等价性\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] κ̄ (constraint tightness) 在 n=3 schema 上声称 \"predictive factor\" [AGREE: R1+R2]**\n- Abstract: \"establishing constraint tightness (κ̄) as a predictive factor\"\n- 实际仅 3 个 schema（SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄≈0.82）\n- Figure 2 仅 4 数据点线性拟合（R²=0.886, p=0.058 不显著）\n- x 轴使用 κ̄ × RV_baseline（model-dependent），使 κ̄ 自身 predictive power 不明确\n- 建议：\"establishing...predictive factor\" → \"introducing...descriptive metric\"\n\n**SF2. [warning] WikiEvents fine-tuning composability 仅 n=20 文档 [AGREE: R1+R2]**\n- Per-document variance > 0.5，bootstrap CI 极宽\n- WikiEvents EE 不涉及 cross-field type constraints，仅验证 grammar layer\n- 建议：Table 5 加 confidence interval，明确标注为 preliminary\n\n**SF3. [warning] \"Deployment-grade compliance\" 叙事被 CF trade-off 结构性削弱 [AGREE: R1+R2]**\n- CF 是 DR enforcement 的系统性副产品，zero-shot 最高 12.02%\n- \"Deployment-grade\" 暗示接近零违规，系统在 CF 维度做不到\n- 建议：软化为 \"near-complete DR elimination with residual CF trade-off\"\n\n**SF4. [warning] \"Enabling dependency\" 声明范围不清 [AGREE: R1+R2]**\n- \"neither layer alone exceeds 24% DR reduction\" 仅限 SciERC\n- DocRED grammar-only **增加** DR 42%，与 SciERC 模式截然不同\n- 建议：改为 \"on SciERC, neither layer alone exceeds 24%\"\n\n**SF5. [warning] Entity registry 顺序依赖未量化 [AGREE: R1+R2]**\n- 首次类型分配错误会传播到所有后续引用\n- Limitations 承认但无量化分析\n- CF 是间接量化但不等价于 propagation rate\n- 建议：post-hoc 分析首次提及错误率和传播频率\n\n**SF6. [warning] S2 (two-pass pipeline) 描述与评估不匹配 [AGREE: R1+R2]**\n- §3.4 花半页描述但仅 Table 1 一行结果\n- 8 页限制下建议方案 A（压缩 §3.4）而非补充完整实验\n\n### Minor（不影响接收）\n\n**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B。主文读者无法仅从 §6 评估覆盖充分性。[R1+R2 AGREE]\n**M2.** \"S1\"/\"Full S1\" 术语不统一（§5.1 vs §5.4）。[R2]\n**M3.** Figure 1 信息密度过高。[R2]\n**M4.** Table 4 Mistral CF=56.87% dagger 脚注解释位置不佳。[R2]\n**M5.** Introduction \"48% predictions discarded\" 未 cite 来源表格。[R2]\n**M6.** Proposition 1 position-based vs name-based 桥接缺乏形式化 corollary。[R1+R2 AGREE, 低严重度]\n**M7.** 70B AWQ INT4 量化对约束 enforcement 的潜在影响未讨论。[R1+R2 AGREE]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n1. **DR/CF 数字精确性**：Abstract/Intro 存在多处数字不一致或 bound 违反（MF1-MF4）\n2. **CF 叙事偏乐观**：主文 framing 系统性低估 CF 代价（MF3, SF3）\n3. **κ̄ 过度声称**：n=3 不支持 \"predictive factor\"（SF1）\n4. **WikiEvents 统计效力不足**：n=20 不支持 generalization 结论（SF2）\n5. **可复现性优秀**：评估设计全面，Appendix 详尽（S1, S2, S5）\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | Director 判定 |\n|------|-----|-----|-------------|\n| **Baseline 实验对比严重度** | Critical（最大短板） | Should-Fix（grammar-only 代理合理） | **Critical**——连续多轮未解决，对于 constrained decoding 论文是核心实验缺口 |\n| **新颖性** | Excitement 3/5（Proposition 1 decidability taxonomy 有原创性） | Excitement 2.5/5（已知组件集成） | **2.75/5**——系统集成 + 全面评估有价值，但核心组件确为已知技术。建议调整贡献定位 |\n| **CF 呈现严重度** | Critical | Warning (framing 而非隐瞒) | **Critical**——数据透明但叙事不匹配，abstract 是审稿人最先读到的部分 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Abstract/Intro DR 降幅范围不一致（45–99% vs 76–99%），\"calibrated models\" 如何定义？DocRED Qwen（calibrated）仅 45% 如何与 76% 下界调和？\n\n**Q2.** Multi-type entity（一个 entity 在 ontology 中合法拥有多个类型）如何处理？当前 first-assignment-wins 设计是否导致 false positive CF？\n\n**Q3.** Llama DocRED CF 12.02% vs Qwen 2.57%——根因是 Llama 的 entity typing 能力弱还是 DocRED schema 特殊性？\n\n**Q4.** 是否考虑过 constrained decoding + post-hoc filtering 的组合策略？\n\n**Q5.** BoostCD \"only 3% DR reduction\"——请明确标注此结论来自 grammar-only ablation 的方法论等价推断而非运行 BoostCD 代码。\n\n**Q6.** Grammar-only 在 DocRED 上增加 DR 42%——这对 \"enabling dependency\" 的通用性有什么影响？\n\n---\n\n## Missing References\n\n论文在 constrained decoding + IE 领域的覆盖相当全面。以下可能值得提及但非必要：\n- **Schmidt & Cimiano (2025)**: Grammar-constrained decoding for structured IE in biomedical domain (Bioinformatics)\n- **Microsoft Guidance**: 工程工具，constrained generation 讨论中常被提及\n- 建议检查 **EMNLP 2025** proceedings 是否有遗漏的近期 accepted papers\n\n**引用真实性**: Reviewer 2 验证全部 46 个 bib 条目均来自真实论文/预印本，格式统一，未发现伪造引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未启用外部审稿配置）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成 (4 warnings, 0 critical, 9 info)\n\n主要发现：\n- **[warning]** Pages 1-2 连续纯文本（Title/Abstract/Intro/Background），首个 display item（Figure 1）直到 page 3 才出现\n- **[warning]** Pages 4-5 连续纯文本（Method），无公式 display 或图表穿插\n- **[warning]** Pages 6-7 display items 分布严重不均：5 张 table 集中在 2 页，page 7 尤其密集（Tables 3-5 挤在一页）\n- **[warning]** Page 8（Related Work + Conclusion）全部纯文本，无视觉元素收尾\n- **[info]** 主正文 8 页仅 1 figure + 5 tables，figure 数量偏少。Appendix 中 Figure 2/3 若能提升到主文可改善阅读体验\n- **[info]** 无 margin 溢出、无 LaTeX 渲染错误、无 [?] 未解析引用。格式符合 ACL 匿名投稿模板\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | **3.5/5** | 方法论合理，消融设计系统，但 Abstract/Intro 数字不一致削弱可信度；CF framing 偏乐观；缺少 baseline head-to-head |\n| **Excitement** | **2.75/5** | 问题重要且实用，但核心组件（XGrammar + runtime type check）均为已知技术。Proposition 1 的 decidability taxonomy 有理论贡献但影响面有限。主要贡献是系统集成和全面评估 |\n| **Reproducibility** | **4.5/5** | Appendix G 详尽，bootstrap CI，seed 报告，代码承诺开源 |\n| **Overall Assessment** | **3.5 — Borderline Conference** | R1 和 R2 独立评分一致 |\n| **Confidence** | **4/5** | 两位 Reviewer 仔细阅读全文含 34 页 appendix |\n\n### 总评\n\n一项系统化但新颖性有限的工程贡献。将已知组件（CFG enforcement + runtime type checking）组合为 IE ontology 约束解码管道，配以出色的评估覆盖度和诚实的 limitations 分析。核心障碍是：(1) Abstract/Intro 存在多处数字不一致和 bound 违反，削弱论文可信度；(2) 缺少与 GCD/BoostCD 等现有方法的直接实验对比；(3) CF violation 的主文叙事系统性偏乐观。修正数字错误（MF1-MF4）和调整叙事 framing（MF3, SF3）可提升至 Conference 水平；补充 baseline 对比（MF5）可进一步巩固贡献。当前状态适合 Findings 接收，距离 Conference 主会议接收有明确但可修复的差距。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- DR 降幅 \"45–99%\" 与 Intro \"76–99%\" 不一致（MF1）\n- \"CF ≤ 1.3%\" 被 70B 的 1.33% 违反（MF2）\n- \"five autoregressive LMs\" 实际 4 个（MF4）\n- \"establishing constraint tightness (κ̄) as a predictive factor\" 过度声称（SF1）\n- \"substantially reduces type violations\" 在 DR↓+CF↑时需更精确表述\n- 写作质量高，信息密度适当\n\n### §1 Introduction\n- Contribution 2 \"neither layer alone exceeds 24%\" 仅限 SciERC，读者自然误解为通用结论（SF4）\n- \"deployment-grade type compliance\" 被 CF trade-off 削弱（SF3）\n- \"Post-hoc filtering improves precision but discards up to 48%\"——未 cite 来源表格（M5）\n- 问题动机和叙事逻辑清晰\n\n### §2 Background\n- IE ontology 的形式化定义清楚\n- 约束可判定性三级分类是有用的概念框架\n- Proposition 1 定位为 \"necessary condition\" 恰当\n\n### §3 Method\n- Grammar layer 和 semantic layer 描述清晰\n- Continuation masking 机制解释充分\n- Grammar-first fallback 设计决策合理且有 causal tracing 验证\n- §3.4 S2 描述占半页但实验中一句带过（SF6）\n\n### §4 Constraint Composition\n- Mask composition 公式简洁\n- Asymmetric conjunction 解释清楚\n\n### §5 Experiments\n- Table 1 五路消融是最强的实验贡献\n- DocRED grammar-only DR 增加 42% 值得主文更详细讨论（SF4）\n- WikiEvents n=20 统计效力不足（SF2）\n- 70B 定位为 feasibility check 基本恰当，但仍被纳入 Abstract 统计声明\n- 缺少与 GCD/BoostCD 的 head-to-head 实验（MF5）\n\n### §6 Related Work\n- 覆盖面合理但主文仅约半栏（M1）\n- GCD, GoLLIE, EnriCo 的对比定位准确\n- 建议将 Appendix B 中关键对比移入主文\n\n### §7 Discussion and Conclusion\n- 数字继承了 Abstract/Intro 的不一致问题\n\n### Limitations\n- 全面且诚实（S2），三段分别覆盖约束范围、评估覆盖、工程考量\n- CF trade-off 定性为 \"fundamental trade-off\" 合理\n\n### Ethics Statement & Checklist\n- Ethics statement 简洁充分\n- Checklist 填写认真，各项回答与论文内容一致\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（符合 EMNLP 2026 要求）\n\n### 格式\n- 正文 8 页 ✓\n- `\\usepackage[review]{acl}` ✓（匿名，行号）\n- \"Anonymous ACL submission\" ✓\n- 未发现 self-citation leaks 或 identifying information\n- Limitations/Ethics 在 \\clearpage 后，不计入页数 ✓\n- 参考文献格式统一，无 [?] 未解析引用",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 — Borderline Conference",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人圆桌\n- Reviewer 1: 方法严谨性 + 实验设计\n- Reviewer 2: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE ontology 自动编译为 token-level 解码约束的两层架构：grammar layer（基于 XGrammar 的 CFG，保证 JSON 结构 + 词表合规）和 semantic layer（有状态 entity registry 实现 cross-field 类型约束）。论文在 3 个数据集（SciERC, DocRED, WikiEvents）、4 个模型族（7B–70B）上系统评估，报告 LoRA + S1 可将 DR 降至 ≤0.09%，但引入 CF 违规（FT ≤1.3%, ZS 最高 12.02%）作为 violation conversion 的结构性代价。附 24 页 appendix 含消融、causal tracing、scalability 等详细分析。\n\n---\n\n## Strengths\n\n**S1. 系统化的评估覆盖度（两位 Reviewer 一致认可）**\n3 数据集 × 4+ 模型 × ZS/FT × greedy/beam/sampling，加上五路消融（Table 1）、四路消融（Table 3）、跨模型验证（Table 4）、per-relation breakdown、causal tracing（Table 7）、dual-factor analysis（Figure 2）。Bootstrap 10,000 iterations + Bonferroni correction。在同类工作中属于上乘。\n\n**S2. 诚实透明的 Limitations 和 CF-DR trade-off 分析**\nAppendix C 的 causal tracing、CF-priority fallback 消融（Table 8）、dual-factor 定量分析坦诚承认 CF-DR trade-off 是结构性而非可调参数。Limitations section 覆盖了约束范围、评估覆盖、工程约束等关键限制。\n\n**S3. 理论基础有原创性**\nDecidability taxonomy（Level 1/2/3）将 IE 类型约束按可判定性分层，Proposition 1（Appendix O）通过 pumping lemma 证明 cross-field type consistency 超出 CFG 表达能力，为两层架构提供形式化依据。\n\n**S4. 低运行时开销**\nGreedy S1 仅增加 10–13% latency，constraint compilation < 0.5s，scalability benchmark 到 200 entity types / 1,000 relations 保持 2–3% overhead。\n\n**S5. 可复现性优秀**\nAppendix G 报告硬件/种子/超参，3 seeds cross-GPU variance（Table 24），prompt templates 完整展示（Table 6），承诺开源代码。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] Abstract/Intro DR 降幅数字自相矛盾 [AGREE: R1+R2]**\n- Abstract: \"45–99% DR reduction\"\n- Introduction: \"DR drops 76–99% for calibrated models\"\n- Table 4 实际全范围: **42–99%**（Mistral DocRED 42% 被排除未说明）\n- DocRED Qwen（calibrated model）仅 45%，远低于 Intro 声称的 76% 下界\n- 建议：统一为 \"42–99%\" 或明确限定条件并说明排除理由\n\n**MF2. [critical] Abstract CF ≤1.3% bound 被 70B LoRA CF=1.33% 违反 [AGREE: R1+R2]**\n- 差异虽小（0.03pp），但 Abstract 将其作为 bound 呈现\n- 70B 是论文明确涵盖的配置（Abstract 说 \"five autoregressive LMs (7–70B)\"）\n- 建议：修正为 \"≤1.4%\" 或限定为 8B 模型\n\n**MF3. [critical] CF violation 在主文叙事中被系统性低估 [AGREE: R1+R2]**\n- Zero-shot Llama DocRED CF 高达 **12.02%**，但主文 §5.1-§5.3 叙述中仅出现 \"CF ≤ 1.3%\"（仅限 FT）\n- Abstract \"substantially reduces type violations\"——但 zero-shot DocRED Llama total violation (DR+CF) 从 26.24% 仅降至 14.57%（改善 ~44%），远不如 DR 单项 90% 降幅\n- 数据在 Table 4 中透明呈现，**问题是叙事 framing 而非数据隐瞒**\n- 建议：主文 §5 明确报告 CF 最差情况，Abstract 区分 ZS 和 FT CF 范围\n\n**MF4. [critical] \"five autoregressive LMs\" 但实际仅 4 个模型——事实错误 [AGREE: R1+R2]**\n- 全文仅出现 Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B = 4 个模型\n- Limitations 也说 \"three 8B-class and one 70B-class model\" = 4\n- 疑似早期版本残留\n- 建议：修正 \"five\" → \"four\"\n\n**MF5. [critical/should-fix, 分歧] 缺少与现有 constrained decoding 方法的直接实验对比**\n- 论文大量讨论 GCD/BoostCD/CRANE/GoLLIE（§6, Appendix B），但无 head-to-head 实验\n- 唯一\"对比\"是自行实现的 Trie-Only Baseline（Table 15, Appendix D）\n- §5.4 \"BoostCD only 3% DR reduction\" 来自方法论等价推断（grammar-only ablation），非运行 BoostCD 代码\n- **分歧**: R1 列为 critical（最大短板），R2 交叉认为 should-fix（grammar-only 作为 GCD 代理合理，但 GoLLIE 缺失更严重）\n- **Director 判定**: 维持 critical——对于定位为推进 constrained decoding for IE 的论文，缺少 head-to-head 基准对比是核心实验缺口。grammar-only 消融的等价推断在方法论上可辩护，但在实际评审中说服力不足，尤其是该问题已被多轮审稿反复指出。至少应运行 GCD 官方代码或明确论证 grammar-only = GCD 的等价性\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] κ̄ (constraint tightness) 在 n=3 schema 上声称 \"predictive factor\" [AGREE: R1+R2]**\n- Abstract: \"establishing constraint tightness (κ̄) as a predictive factor\"\n- 实际仅 3 个 schema（SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄≈0.82）\n- Figure 2 仅 4 数据点线性拟合（R²=0.886, p=0.058 不显著）\n- x 轴使用 κ̄ × RV_baseline（model-dependent），使 κ̄ 自身 predictive power 不明确\n- 建议：\"establishing...predictive factor\" → \"introducing...descriptive metric\"\n\n**SF2. [warning] WikiEvents fine-tuning composability 仅 n=20 文档 [AGREE: R1+R2]**\n- Per-document variance > 0.5，bootstrap CI 极宽\n- WikiEvents EE 不涉及 cross-field type constraints，仅验证 grammar layer\n- 建议：Table 5 加 confidence interval，明确标注为 preliminary\n\n**SF3. [warning] \"Deployment-grade compliance\" 叙事被 CF trade-off 结构性削弱 [AGREE: R1+R2]**\n- CF 是 DR enforcement 的系统性副产品，zero-shot 最高 12.02%\n- \"Deployment-grade\" 暗示接近零违规，系统在 CF 维度做不到\n- 建议：软化为 \"near-complete DR elimination with residual CF trade-off\"\n\n**SF4. [warning] \"Enabling dependency\" 声明范围不清 [AGREE: R1+R2]**\n- \"neither layer alone exceeds 24% DR reduction\" 仅限 SciERC\n- DocRED grammar-only **增加** DR 42%，与 SciERC 模式截然不同\n- 建议：改为 \"on SciERC, neither layer alone exceeds 24%\"\n\n**SF5. [warning] Entity registry 顺序依赖未量化 [AGREE: R1+R2]**\n- 首次类型分配错误会传播到所有后续引用\n- Limitations 承认但无量化分析\n- CF 是间接量化但不等价于 propagation rate\n- 建议：post-hoc 分析首次提及错误率和传播频率\n\n**SF6. [warning] S2 (two-pass pipeline) 描述与评估不匹配 [AGREE: R1+R2]**\n- §3.4 花半页描述但仅 Table 1 一行结果\n- 8 页限制下建议方案 A（压缩 §3.4）而非补充完整实验\n\n### Minor（不影响接收）\n\n**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B。主文读者无法仅从 §6 评估覆盖充分性。[R1+R2 AGREE]\n**M2.** \"S1\"/\"Full S1\" 术语不统一（§5.1 vs §5.4）。[R2]\n**M3.** Figure 1 信息密度过高。[R2]\n**M4.** Table 4 Mistral CF=56.87% dagger 脚注解释位置不佳。[R2]\n**M5.** Introduction \"48% predictions discarded\" 未 cite 来源表格。[R2]\n**M6.** Proposition 1 position-based vs name-based 桥接缺乏形式化 corollary。[R1+R2 AGREE, 低严重度]\n**M7.** 70B AWQ INT4 量化对约束 enforcement 的潜在影响未讨论。[R1+R2 AGREE]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n1. **DR/CF 数字精确性**：Abstract/Intro 存在多处数字不一致或 bound 违反（MF1-MF4）\n2. **CF 叙事偏乐观**：主文 framing 系统性低估 CF 代价（MF3, SF3）\n3. **κ̄ 过度声称**：n=3 不支持 \"predictive factor\"（SF1）\n4. **WikiEvents 统计效力不足**：n=20 不支持 generalization 结论（SF2）\n5. **可复现性优秀**：评估设计全面，Appendix 详尽（S1, S2, S5）\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | Director 判定 |\n|------|-----|-----|-------------|\n| **Baseline 实验对比严重度** | Critical（最大短板） | Should-Fix（grammar-only 代理合理） | **Critical**——连续多轮未解决，对于 constrained decoding 论文是核心实验缺口 |\n| **新颖性** | Excitement 3/5（Proposition 1 decidability taxonomy 有原创性） | Excitement 2.5/5（已知组件集成） | **2.75/5**——系统集成 + 全面评估有价值，但核心组件确为已知技术。建议调整贡献定位 |\n| **CF 呈现严重度** | Critical | Warning (framing 而非隐瞒) | **Critical**——数据透明但叙事不匹配，abstract 是审稿人最先读到的部分 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Abstract/Intro DR 降幅范围不一致（45–99% vs 76–99%），\"calibrated models\" 如何定义？DocRED Qwen（calibrated）仅 45% 如何与 76% 下界调和？\n\n**Q2.** Multi-type entity（一个 entity 在 ontology 中合法拥有多个类型）如何处理？当前 first-assignment-wins 设计是否导致 false positive CF？\n\n**Q3.** Llama DocRED CF 12.02% vs Qwen 2.57%——根因是 Llama 的 entity typing 能力弱还是 DocRED schema 特殊性？\n\n**Q4.** 是否考虑过 constrained decoding + post-hoc filtering 的组合策略？\n\n**Q5.** BoostCD \"only 3% DR reduction\"——请明确标注此结论来自 grammar-only ablation 的方法论等价推断而非运行 BoostCD 代码。\n\n**Q6.** Grammar-only 在 DocRED 上增加 DR 42%——这对 \"enabling dependency\" 的通用性有什么影响？\n\n---\n\n## Missing References\n\n论文在 constrained decoding + IE 领域的覆盖相当全面。以下可能值得提及但非必要：\n- **Schmidt & Cimiano (2025)**: Grammar-constrained decoding for structured IE in biomedical domain (Bioinformatics)\n- **Microsoft Guidance**: 工程工具，constrained generation 讨论中常被提及\n- 建议检查 **EMNLP 2025** proceedings 是否有遗漏的近期 accepted papers\n\n**引用真实性**: Reviewer 2 验证全部 46 个 bib 条目均来自真实论文/预印本，格式统一，未发现伪造引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未启用外部审稿配置）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成 (4 warnings, 0 critical, 9 info)\n\n主要发现：\n- **[warning]** Pages 1-2 连续纯文本（Title/Abstract/Intro/Background），首个 display item（Figure 1）直到 page 3 才出现\n- **[warning]** Pages 4-5 连续纯文本（Method），无公式 display 或图表穿插\n- **[warning]** Pages 6-7 display items 分布严重不均：5 张 table 集中在 2 页，page 7 尤其密集（Tables 3-5 挤在一页）\n- **[warning]** Page 8（Related Work + Conclusion）全部纯文本，无视觉元素收尾\n- **[info]** 主正文 8 页仅 1 figure + 5 tables，figure 数量偏少。Appendix 中 Figure 2/3 若能提升到主文可改善阅读体验\n- **[info]** 无 margin 溢出、无 LaTeX 渲染错误、无 [?] 未解析引用。格式符合 ACL 匿名投稿模板\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | **3.5/5** | 方法论合理，消融设计系统，但 Abstract/Intro 数字不一致削弱可信度；CF framing 偏乐观；缺少 baseline head-to-head |\n| **Excitement** | **2.75/5** | 问题重要且实用，但核心组件（XGrammar + runtime type check）均为已知技术。Proposition 1 的 decidability taxonomy 有理论贡献但影响面有限。主要贡献是系统集成和全面评估 |\n| **Reproducibility** | **4.5/5** | Appendix G 详尽，bootstrap CI，seed 报告，代码承诺开源 |\n| **Overall Assessment** | **3.5 — Borderline Conference** | R1 和 R2 独立评分一致 |\n| **Confidence** | **4/5** | 两位 Reviewer 仔细阅读全文含 34 页 appendix |\n\n### 总评\n\n一项系统化但新颖性有限的工程贡献。将已知组件（CFG enforcement + runtime type checking）组合为 IE ontology 约束解码管道，配以出色的评估覆盖度和诚实的 limitations 分析。核心障碍是：(1) Abstract/Intro 存在多处数字不一致和 bound 违反，削弱论文可信度；(2) 缺少与 GCD/BoostCD 等现有方法的直接实验对比；(3) CF violation 的主文叙事系统性偏乐观。修正数字错误（MF1-MF4）和调整叙事 framing（MF3, SF3）可提升至 Conference 水平；补充 baseline 对比（MF5）可进一步巩固贡献。当前状态适合 Findings 接收，距离 Conference 主会议接收有明确但可修复的差距。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- DR 降幅 \"45–99%\" 与 Intro \"76–99%\" 不一致（MF1）\n- \"CF ≤ 1.3%\" 被 70B 的 1.33% 违反（MF2）\n- \"five autoregressive LMs\" 实际 4 个（MF4）\n- \"establishing constraint tightness (κ̄) as a predictive factor\" 过度声称（SF1）\n- \"substantially reduces type violations\" 在 DR↓+CF↑时需更精确表述\n- 写作质量高，信息密度适当\n\n### §1 Introduction\n- Contribution 2 \"neither layer alone exceeds 24%\" 仅限 SciERC，读者自然误解为通用结论（SF4）\n- \"deployment-grade type compliance\" 被 CF trade-off 削弱（SF3）\n- \"Post-hoc filtering improves precision but discards up to 48%\"——未 cite 来源表格（M5）\n- 问题动机和叙事逻辑清晰\n\n### §2 Background\n- IE ontology 的形式化定义清楚\n- 约束可判定性三级分类是有用的概念框架\n- Proposition 1 定位为 \"necessary condition\" 恰当\n\n### §3 Method\n- Grammar layer 和 semantic layer 描述清晰\n- Continuation masking 机制解释充分\n- Grammar-first fallback 设计决策合理且有 causal tracing 验证\n- §3.4 S2 描述占半页但实验中一句带过（SF6）\n\n### §4 Constraint Composition\n- Mask composition 公式简洁\n- Asymmetric conjunction 解释清楚\n\n### §5 Experiments\n- Table 1 五路消融是最强的实验贡献\n- DocRED grammar-only DR 增加 42% 值得主文更详细讨论（SF4）\n- WikiEvents n=20 统计效力不足（SF2）\n- 70B 定位为 feasibility check 基本恰当，但仍被纳入 Abstract 统计声明\n- 缺少与 GCD/BoostCD 的 head-to-head 实验（MF5）\n\n### §6 Related Work\n- 覆盖面合理但主文仅约半栏（M1）\n- GCD, GoLLIE, EnriCo 的对比定位准确\n- 建议将 Appendix B 中关键对比移入主文\n\n### §7 Discussion and Conclusion\n- 数字继承了 Abstract/Intro 的不一致问题\n\n### Limitations\n- 全面且诚实（S2），三段分别覆盖约束范围、评估覆盖、工程考量\n- CF trade-off 定性为 \"fundamental trade-off\" 合理\n\n### Ethics Statement & Checklist\n- Ethics statement 简洁充分\n- Checklist 填写认真，各项回答与论文内容一致\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（符合 EMNLP 2026 要求）\n\n### 格式\n- 正文 8 页 ✓\n- `\\usepackage[review]{acl}` ✓（匿名，行号）\n- \"Anonymous ACL submission\" ✓\n- 未发现 self-citation leaks 或 identifying information\n- Limitations/Ethics 在 \\clearpage 后，不计入页数 ✓\n- 参考文献格式统一，无 [?] 未解析引用",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 — Borderline Conference",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1774 · 2026-05-22T11:04:17.047508+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4267
}
```

</details>

---


### Assistant

_source line 1775 · 2026-05-22T11:04:35.809033+00:00_

审稿报告已投递至 Research Director。

**Round 17 审稿完成。**

- **Overall**: 3.5 — Borderline Conference（R1 和 R2 独立一致）
- **5 个 Must-Fix**: (1) DR 降幅范围 Abstract/Intro 自相矛盾 (42-99% 实际 vs 45-99%/76-99% 声称)；(2) CF≤1.3% 被 70B 的 1.33% 违反；(3) CF 主文叙事系统性偏乐观；(4) "five models" 实际 4 个；(5) 缺少 GCD/BoostCD head-to-head 实验对比（连续 6 轮指出）
- **6 个 Should-Fix**: κ̄ n=3 声称 predictive、WikiEvents n=20 不足、"deployment-grade" 被 CF 削弱、"enabling dependency" 范围不清、entity registry 传播未量化、S2 描述与评估不匹配
- **核心判断**: 修正数字错误 + 调整叙事 framing 可提升至 Conference 水平；当前适合 Findings 接收

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1776 · 2026-05-22T11:04:38.388023+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 和 R2 在总分（3.5 Borderline Conference）上一致，在 κ̄ 和 WikiEvents 问题上完全一致。主要分歧在于 baseline 缺失的严重程度（R1 定 critical，我认为 grammar-only 作为 GCD 代理部分缓解了这个问题）和 CF 呈现问题的定级（R1 critical vs. 我的 warning，因为数据实际在 Table 4 中透明展示，问题在于叙事 framing）。我额外指出了 R1 未重点讨论的新颖性问题（W3），这是我认为的最大制约因素。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1777 · 2026-05-22T11:04:56.014220+00:00_

审稿报告已投递至 Research Director。

**Round 17 审稿完成**，汇总：

- **Overall**: 3.5 — Borderline Conference（两位 Reviewer 独立评分一致）
- **5 个 Must-Fix**: (1) DR 降幅数字自相矛盾 42-99% vs 45-99% vs 76-99%；(2) CF≤1.3% bound 被 70B 1.33% 违反；(3) CF 主文叙事系统性偏乐观；(4) "five models" 实际 4 个；(5) 缺少 baseline head-to-head 实验（连续 6 轮未解决）
- **6 个 Should-Fix**: κ̄ 声称过度、WikiEvents n=20、"deployment-grade" 措辞、"enabling dependency" 范围、entity registry 传播未量化、S2 描述与评估不匹配
- **核心判断**: 系统化但新颖性有限的工程贡献，评估覆盖优秀。MF1-MF4 为数字/事实错误可快速修复；MF5（baseline 对比）和新颖性定位是距离 Conference 接收的主要差距。当前适合 Findings，修复后可冲 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 134

## Round 134

124 recorded events


### User

_source line 1778 · 2026-05-22T12:25:23.616601+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1779 · 2026-05-22T12:25:30.404282+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1780 · 2026-05-22T12:25:30.455316+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1781 · 2026-05-22T12:25:35.044015+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1782 · 2026-05-22T12:25:35.044518+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1783 · 2026-05-22T12:25:39.563045+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1784 · 2026-05-22T12:25:39.563388+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1785 · 2026-05-22T12:25:43.463884+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1786 · 2026-05-22T12:25:43.514633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1787 · 2026-05-22T12:25:46.427578+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 1788 · 2026-05-22T12:25:46.478196+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1789 · 2026-05-22T12:25:49.440776+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1790 · 2026-05-22T12:25:50.847094+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (139 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_beam_sweep** (success): Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\n  [d066_beam_sweep_eval](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/d066_beam_sweep/report/d066_beam_sweep_eval.md) | [d066_beam_sweep_scierc_analysis](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/d066_beam_sweep/report/d066_beam_sweep_scierc_analysis.md) | [beam_pareto_dual_panel](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/d066_beam_sweep/chart/beam_pareto.pdf)\n- **eval_70b_lora_docred_200_s1_constrained** (success): 70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve 
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1791 · 2026-05-22T12:25:51.399886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1792 · 2026-05-22T12:25:51.852198+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1793 · 2026-05-22T12:25:51.902847+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1794 · 2026-05-22T12:25:58.929871+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I performed the web search for you. T
…[truncated 1548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7027
}
```

</details>

---


### Tool call

_source line 1795 · 2026-05-22T12:26:03.498494+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-22T12:26:03.950910+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit template"
  }
}
```

</details>

---


### Tool call

_source line 1797 · 2026-05-22T12:26:06.009835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1798 · 2026-05-22T12:26:06.060541+00:00_

100	
101	% === Ethics Statement ===
102	\section*{Ethics Statement}
103	
104	This work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.
105	No human subjects were involved in the experiments.
106	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
107	Code and data will be released upon acceptance.
108	
109	% === Bibliography ===
110	\bibliography{relwork_new_entries}
111	
112	% === Appendix ===
113	\appendix
114	
115	\input{appendix_prompts}
116	\input{appendix_related_work}
117	\input{appendix_discussion}
118	\input{appendix_llama_per_relation}
119	\input{appendix_sampling_table}
120	\input{appendix_beam_search}
121	\input{appendix_reproducibility}
122	\input{appendix_doc_length}
123	\input{appendix_prompt_sensitivity}
124	\input{appendix_case_studies}
125	\input{appendix_scalability}
126	\input{appendix_full_ft}
127	\input{appendix_tcr}
128	\input{appendix_kappa_case_study}
129	\input{appendix_pumping_lemma}
130	
131	\end{document}
132	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-22T12:26:09.425312+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's the information about EMNLP 2026 Call for Papers:

**Submission Deadline:**
The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12).

**Page Limits:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Additional Important 
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5926
}
```

</details>

---


### Tool result

_source line 1800 · 2026-05-22T12:26:12.570823+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author instructions page limit template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found comprehensive information about ACL Rolling Review 2026 submission guidelines. Here are the key details:

## Submission Requirements

All long, short, and theme papers must follow the ACL Author Guidelines and use the official ACL style template. There is an official Overleaf template, and this template has a [review] setting that must be on for the submission.
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 8619
}
```

</details>

---


### Tool call

_source line 1801 · 2026-05-22T12:26:24.416632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" anonymity \"double-blind\" OR \"single-blind\" appendix guidelines 2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for papers\" anonymity \"double-blind\" OR \"single-blind\" appendix guidelines 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-22T12:26:25.371211+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 1803 · 2026-05-22T12:26:26.526165+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-22T12:26:26.878018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-22T12:26:32.714960+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" anonymity "double-blind" OR "single-blind" appendix guidelines 2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"PrivateNLP@ACL 2026","url":"https://sites.google.com/view/privatenlp2026/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Datasets and Benchmarks Track: Call for Papers – KDD 2026","url":"https://kdd2026.kdd.org/datasets-and-benchmarks-track-call-for-papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Formatting Instructions For NeurIPS 2026 Anonymous Author(s) Affiliation","url":"https://www.overleaf.com/latex/templates/formatting-instructions-for-neurips-2026/bjdwqfdkyftc.pdf"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

I found relevant information about EMNLP 2026's submission guidelines. Here are the key details regarding anonymity, review process, and appendix guidelines:

## Anonymity and Review Process

Following the ACL Policies for Review and Citation updated in early 2024, there is no anonymity period requirement, e.g., one may upload the paper to arXiv at any time. However, submissions will be reviewed in a double-blind manner, and Industry Track submissions must neither include the authors' names nor their affiliations.

## Appendix Guidelines

Authors are asked not to abuse the option of an unlimited appendix and only to include material that supports the primary messages and content of the paper; for the
…[truncated 825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 8298
}
```

</details>

---


### Tool result

_source line 1806 · 2026-05-22T12:26:32.715421+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7344
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-22T12:26:32.767771+00:00_

This PDF has 34 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 5889
}
```

</details>

---


### Tool result

_source line 1808 · 2026-05-22T12:26:32.768214+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 6242
}
```

</details>

---


### Tool call

_source line 1809 · 2026-05-22T12:26:36.640031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1810 · 2026-05-22T12:26:36.992723+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R17 Action Matrix dispatched, 2026-05-22
3	
4	# ============================================================
5	# Round 17 Must-Fix
6	# ============================================================
7	
8	- id: "R15-MF1"
9	  summary: "缺少与 GCD/BoostCD 等同类 constrained decoding 方法的直接实验对比（连续 6 轮 R12-R17）"
10	  category: experiment
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 12
14	  last_seen_round: 17
15	  mentions:
16	    - round: 12
17	      reviewers: [1, 2]
18	      note: "R12-SF2: should-fix"
19	    - round: 13
20	      reviewers: [1, 2]
21	      note: "R13-MF3: 升级为 must-fix"
22	    - round: 14
23	      reviewers: [1, 2]
24	      note: "R14-MF1: grammar-only ablation reframed as Level 1 对比"
25	    - round: 15
26	      reviewers: [1, 2]
27	      note: "R15-MF1: §5 显式 BoostCD/GCD 对比段落。仍不够——未运行外部代码。"
28	    - round: 16
29	      reviewers: [1, 2]
30	      note: "R16-MF1: 连续 5 轮 critical。grammar-only proxy 不被接受。"
31	    - round: 17
32	      reviewers: [1, 2]
33	      note: "R17: R1 列为 critical W1，R2 交叉同意但降为 should-fix（grammar-only 作为 GCD 代理合理，但 GoLLIE 缺失更严重）。Trie-Only Baseline (Table 15) 被视为自行实现简化版而非公平对比。BoostCD '3% DR reduction' 被指出为方法论推断非实验结果。"
34	  action_items:
35	    - round: 14
36	      action: "grammar-only ablation reframed as BoostCD-equivalent Level 1"
37	      assigned_to: paper_agent
38	      status: completed
39	    - round: 15
40	      action: "§5 新增显式对比小节"
41	      assigned_to: paper_agent
42	      status: completed
43	    - round: 16
44	      action: "实现 trie-based GCD-equivalent baseline"
45	      assigned_to: agent + paper_agent
46	      status: completed
47	    - round: 17
48	      action: "Path A: 显式论证 grammar-only = GCD 等价性 + Path C: GoLLIE 参考数字定位"
49	      assigned_to: paper_agent
50	      status: in_progress
51	  resolution: ""
52	  resolution_round: null
53	
54	- id: "R16-MF2"
55	  summary: "Abstract/Intro DR 降幅范围自相矛盾（Abstract '45-99%' vs Intro '76-9
…[truncated 16245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1811 · 2026-05-22T12:26:36.993657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---
