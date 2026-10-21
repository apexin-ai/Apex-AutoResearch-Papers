# Director coordination — Part 4 of 8

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/eb/ebac95f2406b6d6dc37e.json)

## Round 80

### Tool call

_source line 1141 · 2026-05-19T08:54:04.488257+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 11 (fresh review, 2026-05-19)\n\n# ============================================================\n# Round 11 Must-Fix\n# ============================================================\n\n- id: \"R11-MF1\"\n  summary: \"'Near-lossless' 叙事未充分呈现 CF trade-off — Abstract/Intro 需重构\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-N2，full consensus。Zero-shot CF 0.08%→9.90%(SciERC)/12.02%(Llama DocRED)。Total violation burden(DR+CF) SciERC ZS 仅降30%。Abstract 将 CF 作为附带现象而非核心 trade-off。建议：(1) Abstract 明确 near-lossless 仅指 LoRA+S1；(2) 报告 total violation (DR+CF)；(3) 正文主线调整为 LoRA+S1，zero-shot 降级为 diagnostic。\"\n  action_items:\n    - round: 11\n      action: \"Abstract 重写：near-lossless 限定为 LoRA+S1；加入 total violation burden (DR+CF) 指标；ZS CF trade-off 前置呈现而非括号附注。Introduction contribution 列表加入 CF trade-off honest limitation。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-MF2\"\n  summary: \"缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-W2，full consensus。Baseline 仅为 ablation 变体（unconstrained/grammar-only/semantic-only/post-hoc），无外部竞争方法。GoLLIE 代码公开，至少应报告其 violation rates 或论证不可比性。\"\n  action_items:\n    - round: 11\n      action: \"至少以下之一：(1) GoLLIE 在 SciERC 上的 violation rate 对比实验；(2) 引用 GoLLIE/KnowCoder 论文中的 schema compliance 数据；(3) 明确论证不可比性。§6 的 'complementary' claim 需实验支撑。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 Should-Fix\n# ============================================================\n\n- id: \"R11-SF1\"\n  summary: \"Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W3，full consensus。Appendix B 谨慎标注 'descriptive characterization'，但正文 §4 使用 'consistent with'/'supports' 暗示因果性。\"\n  action_items:\n    - round: 11\n      action: \"正文 §4 弱化措辞：'correlate' → 'are consistent with (n=4)'；增加更多 model×dataset 数据点或在正文标注 n 太小。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF2\"\n  summary: \"WikiEvents 'preliminary' 限定不足 — Abstract 和 Contribution 表述 confidence 过高\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W4，full consensus。20-doc test set，trigger F1 CI 极宽。Abstract line 10 'extends to EE without modification' 缺 preliminary 限定。\"\n  action_items:\n    - round: 11\n      action: \"Abstract 和 Contribution 3 加 'preliminary' 限定词。§5.4 首段显式说明 20-doc 样本量限制。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF3\"\n  summary: \"Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-W1 + R1 cross AGREE。ZS 定位为 stress test 的辩护在附录而非正文。LoRA+S1（推荐配置）反而篇幅不足。\"\n  action_items:\n    - round: 11\n      action: \"§5 开头加 framing paragraph 明确 ZS 为 diagnostic/stress-test，FT composability 为 deployment 主线。扩展 Table 2 FT 结果讨论篇幅。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF4\"\n  summary: \"Beam search DocRED 仅 50-doc subset，推广性受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 cross AGREE。正文未提及不确定性（Clopper-Pearson CI 上界 5.8%）。\"\n  action_items:\n    - round: 11\n      action: \"正文 §5 beam 段落加 '(SciERC 551 docs; DocRED 50-doc subset)' 标注；解释未跑全量原因；讨论 50→998 推广性。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF5\"\n  summary: \"Abstract 数字密度过高（~15 个数字）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-W5 raised, R1 partial REBUT（实证论文需数字支撑）但同意可精简 2-3 个。\"\n  action_items:\n    - round: 11\n      action: \"保留 3-4 个关键数字（DR≤0.20%, ±0.6pp, 76-99%, CF≤1.2%），去掉 beam search 数字和冗余精度。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF6\"\n  summary: \"Entity registry 字段顺序依赖未显式讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-W6 + R1 cross AGREE。§3.1 line 28 提及 fixed field ordering，但未讨论：(1) 如何通过 JSON Schema 强制；(2) relation 引用未知实体时 fallback 退化为粗粒度 domain-only 约束的影响。\"\n  action_items:\n    - round: 11\n      action: \"§3.1 或 §3.2 加 1-2 句显式说明字段顺序通过 JSON Schema 强制，并讨论未知实体 fallback 行为。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 Minor\n# ============================================================\n\n- id: \"R11-M1\"\n  summary: \"BibTeX 清理：10 个 orphan entries + 1 duplicate key\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"包括 paolini2021tanl, vukovic2024dore 等。schall2025hiddencost 重复。\"\n  action_items:\n    - round: 11\n      action: \"Cite TANL in §6 或从 bib 删除。清理 orphan 和 duplicate。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"Compile time 不一致（0.044s vs 0.33s vs 44ms）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.6 '44ms', Appendix B '0.044s', Appendix K '0.33s'。可能分别是 semantic compile 和 grammar compile，但未区分。\"\n  action_items:\n    - round: 11\n      action: \"统一术语：区分 grammar compile time 和 semantic compile time，各处数值一致。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"WikiEvents 文档数不一致（246 vs 234）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Checklist B6 '246 test documents'，但 194+20+20=234。Table 4 caption 也写 246。\"\n  action_items:\n    - round: 11\n      action: \"核实实际文档数并统一。246 可能为 ZS 全集，234 为 FT split，需明确标注。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M4\"\n  summary: \"§2 P(E×E) 幂集符号未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"σ: R → P(E×E) 中 P 表示幂集但未说明。\"\n  action_items:\n    - round: 11\n      action: \"§2 加注 P 为幂集符号。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M5\"\n  summary: \"DocRED dev set 标注不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5 脚注说明 dev set 评估，但 Table 2 caption '998 docs' 未标注 dev。\"\n  action_items:\n    - round: 11\n      action: \"Table 2 caption 加 '(dev set)' 标注。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M6\"\n  summary: \"S1/S2 命名在 Table 1 中需简要定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 1 中出现 S1/S2 但 caption 未解释。\"\n  action_items:\n    - round: 11\n      action: \"Table 1 caption 加一句定义 S1(single-pass) 和 S2(two-pass)。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M7\"\n  summary: \"'Training-free' 措辞与推荐配置（LoRA+S1）存在误导\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"R2-Minor. R1 partial REBUT：OntoCoDec 本身 training-free 准确，但读者可能误解为推荐流程不需 training。\"\n  action_items:\n    - round: 11\n      action: \"Introduction 加明确区分：'OntoCoDec is training-free; it composes with optional fine-tuning for deployment.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M8\"\n  summary: \"Table 2 DocRED Grammar-only DR 上升至 26.17% 需 caption 加注\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Counter-intuitive 结果，正文 §5.2 有解释（OOV 变可评估）但 caption 缺失。\"\n  action_items:\n    - round: 11\n      action: \"Table 2 caption 加脚注解释 grammar-only DR 上升原因。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 Divergence\n# ============================================================\n\n- id: \"R11-DIV1\"\n  summary: \"技术新颖性评估分歧：R1 认为 Should-Fix（3/5 Excitement），R2 认为 Must-Fix（2.5/5 Excitement）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: grammar 层复用 XGrammar，semantic 层是字典查找+条件masking，主要贡献是工程适配。R1 反驳：sequential pair-based enforcement 正确性论证、enabling dependency 形式化、continuation masking 跨 tokenizer 方案超越纯工程。双方交叉后维持各自立场。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds issues — status update\n# ============================================================\n\n- id: \"R10-MF1\"\n  summary: \"'Ontology Constraints' framing mismatch — title change to 'Schema Constraints'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9-MF2. Title overclaims formal ontology.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE. Full consensus.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未提及。Title 已改为 'Compiled Schema Constraints'，§2 broad definition 保留。已修复。\"\n  resolution: \"Title 已更新为 'Compiled Schema Constraints'。R11 未再标记。\"\n  resolution_round: 11\n\n- id: \"R10-MF2\"\n  summary: \"缺少 ARR Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Hard requirement.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"checklist.tex 已存在且内容完整。R11 未标记为问题。\"\n  resolution: \"checklist.tex 已添加，A1-E1 完整填写。\"\n  resolution_round: 11\n\n- id: \"R10-MF3\"\n  summary: \"WikiEvents EE 'preliminary' overweighted — demote from Contribution #4\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Contribution 4→3.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.4 标题已加 'Preliminary Extension'，但 Abstract line 10 和 Contribution 3 仍缺 'preliminary' 限定。R11-SF2 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF1\"\n  summary: \"'Near-lossless composability' → 'near-lossless DR composability under fine-tuning'\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Global replace.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract line 7 现已包含 'near-lossless DR composability'，但 CF qualifier 呈现不足。R11-MF1 追踪更深层问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF2\"\n  summary: \"Dual-factor n=4 claim too strong\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"C1 reframe to 'empirical characterization'.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"C1 已改为 'empirical characterization'，但正文 §4 措辞仍偏强。R11-SF1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF3\"\n  summary: \"ZS dominates §5 but FT is core\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Add framing paragraph + expand FT.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5 开头加了 framing paragraph，但 ZS 仍占~40%。R11-SF3 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF4\"\n  summary: \"§7 Discussion too short\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§7 含 SOTA gap、GoLLIE complementary、CF open challenge、downstream future work。R11 未标记为独立问题。\"\n  resolution: \"§7 已扩展。R11 未再标记。\"\n  resolution_round: 11\n\n- id: \"R10-SF5\"\n  summary: \"Abstract data density\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仍有~15个数字。R11-SF5 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF6\"\n  summary: \"DocRED beam 50 docs scope unclear\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"正文已有部分标注但不确定性讨论不足。R11-SF4 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF7\"\n  summary: \"GoLLIE/GCD direct comparison missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 1 caption 已标注 grammar-only = GCD ceiling。GoLLIE 实验仍缺。R11-MF2 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M1\"\n  summary: \"Bootstrap CI missing in main tables\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table captions 现有 bootstrap 说明，§5.1/5.2 报告 p-values。R11 未标记。\"\n  resolution: \"Bootstrap 信息已添加到关键表格。\"\n  resolution_round: 11\n\n- id: \"R10-M2\"\n  summary: \"BibTeX orphan entries, duplicate keys\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仍有 10 个 orphan + 1 duplicate。R11-M1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M3\"\n  summary: \"Table 2 missing DocRED FT rows\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 2 现含 Qwen/Llama × SciERC/DocRED 全部 8 行。R11 未标记。\"\n  resolution: \"DocRED FT rows 已添加。\"\n  resolution_round: 11\n\n- id: \"R10-M4\"\n  summary: \"κ(r) symmetric relation normalization caveat\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§4 Eq.2 脚注已加 symmetric relation 说明。R11 未标记。\"\n  resolution: \"脚注已添加。\"\n  resolution_round: 11\n\n- id: \"R10-M5\"\n  summary: \"Constraint-induced parse failure increase unexplained\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.2 末尾加了解释（constraint masking alters token probability distributions）。R11 未标记。\"\n  resolution: \"1-sentence explanation 已添加。\"\n  resolution_round: 11\n\n- id: \"R10-M6\"\n  summary: \"Uncited bib entries\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"SchemaRL, GUIDEX, DCCD, REBEL, BoostCD 现已在 §6 引用。但 TANL 等仍为 orphan。R11-M1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Resolved from earlier rounds (confirmed in R11)\n# ============================================================\n\n- id: \"R9-SF6\"\n  summary: \"Related Work §6 over-compressed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§6 expanded to 3 paragraphs. R11 confirmed adequate.\"\n  resolution_round: 10\n\n- id: \"R8-SF6\"\n  summary: \"Appendix AI writing traces\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Clean main text confirmed by R11.\"\n  resolution_round: 10\n\n- id: \"R8-M4\"\n  summary: \"Limitations dense paragraph needs subsections\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"3 paragraph subsections confirmed.\"\n  resolution_round: 10"
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
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 11 (fresh review, 2026-05-19)\n\n# ============================================================\n# Round 11 Must-Fix\n# ============================================================\n\n- id: \"R11-MF1\"\n  summary: \"'Near-lossless' 叙事未充分呈现 CF trade-off — Abstract/Intro 需重构\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-N2，full consensus。Zero-shot CF 0.08%→9.90%(SciERC)/12.02%(Llama DocRED)。Total violation burden(DR+CF) SciERC ZS 仅降30%。Abstract 将 CF 作为附带现象而非核心 trade-off。建议：(1) Abstract 明确 near-lossless 仅指 LoRA+S1；(2) 报告 total violation (DR+CF)；(3) 正文主线调整为 LoRA+S1，zero-shot 降级为 diagnostic。\"\n  action_items:\n    - round: 11\n      action: \"Abstract 重写：near-lossless 限定为 LoRA+S1；加入 total violation burden (DR+CF) 指标；ZS CF trade-off 前置呈现而非括号附注。Introduction contribution 列表加入 CF trade-off honest limitation。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-MF2\"\n  summary: \"缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-W2，full consensus。Baseline 仅为 ablation 变体（unconstrained/grammar-only/semantic-only/post-hoc），无外部竞争方法。GoLLIE 代码公开，至少应报告其 violation rates 或论证不可比性。\"\n  action_items:\n    - round: 11\n      action: \"至少以下之一：(1) GoLLIE 在 SciERC 上的 violation rate 对比实验；(2) 引用 GoLLIE/KnowCoder 论文中的 schema compliance 数据；(3) 明确论证不可比性。§6 的 'complementary' claim 需实验支撑。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 Should-Fix\n# ============================================================\n\n- id: \"R11-SF1\"\n  summary: \"Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W3，full consensus。Appendix B 谨慎标注 'descriptive characterization'，但正文 §4 使用 'consistent with'/'supports' 暗示因果性。\"\n  action_items:\n    - round: 11\n      action: \"正文 §4 弱化措辞：'correlate' → 'are consistent with (n=4)'；增加更多 model×dataset 数据点或在正文标注 n 太小。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF2\"\n  summary: \"WikiEvents 'preliminary' 限定不足 — Abstract 和 Contribution 表述 confidence 过高\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W4，full consensus。20-doc test set，trigger F1 CI 极宽。Abstract line 10 'extends to EE without modification' 缺 preliminary 限定。\"\n  action_items:\n    - round: 11\n      action: \"Abstract 和 Contribution 3 加 'preliminary' 限定词。§5.4 首段显式说明 20-doc 样本量限制。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF3\"\n  summary: \"Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-W1 + R1 cross AGREE。ZS 定位为 stress test 的辩护在附录而非正文。LoRA+S1（推荐配置）反而篇幅不足。\"\n  action_items:\n    - round: 11\n      action: \"§5 开头加 framing paragraph 明确 ZS 为 diagnostic/stress-test，FT composability 为 deployment 主线。扩展 Table 2 FT 结果讨论篇幅。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF4\"\n  summary: \"Beam search DocRED 仅 50-doc subset，推广性受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 cross AGREE。正文未提及不确定性（Clopper-Pearson CI 上界 5.8%）。\"\n  action_items:\n    - round: 11\n      action: \"正文 §5 beam 段落加 '(SciERC 551 docs; DocRED 50-doc subset)' 标注；解释未跑全量原因；讨论 50→998 推广性。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF5\"\n  summary: \"Abstract 数字密度过高（~15 个数字）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-W5 raised, R1 partial REBUT（实证论文需数字支撑）但同意可精简 2-3 个。\"\n  action_items:\n    - round: 11\n      action: \"保留 3-4 个关键数字（DR≤0.20%, ±0.6pp, 76-99%, CF≤1.2%），去掉 beam search 数字和冗余精度。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-SF6\"\n  summary: \"Entity registry 字段顺序依赖未显式讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-W6 + R1 cross AGREE。§3.1 line 28 提及 fixed field ordering，但未讨论：(1) 如何通过 JSON Schema 强制；(2) relation 引用未知实体时 fallback 退化为粗粒度 domain-only 约束的影响。\"\n  action_items:\n    - round: 11\n      action: \"§3.1 或 §3.2 加 1-2 句显式说明字段顺序通过 JSON Schema 强制，并讨论未知实体 fallback 行为。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 Minor\n# ============================================================\n\n- id: \"R11-M1\"\n  summary: \"BibTeX 清理：10 个 orphan entries + 1 duplicate key\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"包括 paolini2021tanl, vukovic2024dore 等。schall2025hiddencost 重复。\"\n  action_items:\n    - round: 11\n      action: \"Cite TANL in §6 或从 bib 删除。清理 orphan 和 duplicate。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"Compile time 不一致（0.044s vs 0.33s vs 44ms）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.6 '44ms', Appendix B '0.044s', Appendix K '0.33s'。可能分别是 semantic compile 和 grammar compile，但未区分。\"\n  action_items:\n    - round: 11\n      action: \"统一术语：区分 grammar compile time 和 semantic compile time，各处数值一致。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"WikiEvents 文档数不一致（246 vs 234）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Checklist B6 '246 test documents'，但 194+20+20=234。Table 4 caption 也写 246。\"\n  action_items:\n    - round: 11\n      action: \"核实实际文档数并统一。246 可能为 ZS 全集，234 为 FT split，需明确标注。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M4\"\n  summary: \"§2 P(E×E) 幂集符号未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"σ: R → P(E×E) 中 P 表示幂集但未说明。\"\n  action_items:\n    - round: 11\n      action: \"§2 加注 P 为幂集符号。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M5\"\n  summary: \"DocRED dev set 标注不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5 脚注说明 dev set 评估，但 Table 2 caption '998 docs' 未标注 dev。\"\n  action_items:\n    - round: 11\n      action: \"Table 2 caption 加 '(dev set)' 标注。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M6\"\n  summary: \"S1/S2 命名在 Table 1 中需简要定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 1 中出现 S1/S2 但 caption 未解释。\"\n  action_items:\n    - round: 11\n      action: \"Table 1 caption 加一句定义 S1(single-pass) 和 S2(two-pass)。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M7\"\n  summary: \"'Training-free' 措辞与推荐配置（LoRA+S1）存在误导\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"R2-Minor. R1 partial REBUT：OntoCoDec 本身 training-free 准确，但读者可能误解为推荐流程不需 training。\"\n  action_items:\n    - round: 11\n      action: \"Introduction 加明确区分：'OntoCoDec is training-free; it composes with optional fine-tuning for deployment.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M8\"\n  summary: \"Table 2 DocRED Grammar-only DR 上升至 26.17% 需 caption 加注\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Counter-intuitive 结果，正文 §5.2 有解释（OOV 变可评估）但 caption 缺失。\"\n  action_items:\n    - round: 11\n      action: \"Table 2 caption 加脚注解释 grammar-only DR 上升原因。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 Divergence\n# ============================================================\n\n- id: \"R11-DIV1\"\n  summary: \"技术新颖性评估分歧：R1 认为 Should-Fix（3/5 Excitement），R2 认为 Must-Fix（2.5/5 Excitement）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: grammar 层复用 XGrammar，semantic 层是字典查找+条件masking，主要贡献是工程适配。R1 反驳：sequential pair-based enforcement 正确性论证、enabling dependency 形式化、continuation masking 跨 tokenizer 方案超越纯工程。双方交叉后维持各自立场。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds issues — status update\n# ============================================================\n\n- id: \"R10-MF1\"\n  summary: \"'Ontology Constraints' framing mismatch — title change to 'Schema Constraints'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9-MF2. Title overclaims formal ontology.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE. Full consensus.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未提及。Title 已改为 'Compiled Schema Constraints'，§2 broad definition 保留。已修复。\"\n  resolution: \"Title 已更新为 'Compiled Schema Constraints'。R11 未再标记。\"\n  resolution_round: 11\n\n- id: \"R10-MF2\"\n  summary: \"缺少 ARR Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Hard requirement.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"checklist.tex 已存在且内容完整。R11 未标记为问题。\"\n  resolution: \"checklist.tex 已添加，A1-E1 完整填写。\"\n  resolution_round: 11\n\n- id: \"R10-MF3\"\n  summary: \"WikiEvents EE 'preliminary' overweighted — demote from Contribution #4\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Contribution 4→3.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.4 标题已加 'Preliminary Extension'，但 Abstract line 10 和 Contribution 3 仍缺 'preliminary' 限定。R11-SF2 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF1\"\n  summary: \"'Near-lossless composability' → 'near-lossless DR composability under fine-tuning'\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Global replace.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract line 7 现已包含 'near-lossless DR composability'，但 CF qualifier 呈现不足。R11-MF1 追踪更深层问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF2\"\n  summary: \"Dual-factor n=4 claim too strong\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"C1 reframe to 'empirical characterization'.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"C1 已改为 'empirical characterization'，但正文 §4 措辞仍偏强。R11-SF1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF3\"\n  summary: \"ZS dominates §5 but FT is core\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Add framing paragraph + expand FT.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5 开头加了 framing paragraph，但 ZS 仍占~40%。R11-SF3 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF4\"\n  summary: \"§7 Discussion too short\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§7 含 SOTA gap、GoLLIE complementary、CF open challenge、downstream future work。R11 未标记为独立问题。\"\n  resolution: \"§7 已扩展。R11 未再标记。\"\n  resolution_round: 11\n\n- id: \"R10-SF5\"\n  summary: \"Abstract data density\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仍有~15个数字。R11-SF5 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF6\"\n  summary: \"DocRED beam 50 docs scope unclear\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"正文已有部分标注但不确定性讨论不足。R11-SF4 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-SF7\"\n  summary: \"GoLLIE/GCD direct comparison missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 1 caption 已标注 grammar-only = GCD ceiling。GoLLIE 实验仍缺。R11-MF2 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M1\"\n  summary: \"Bootstrap CI missing in main tables\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table captions 现有 bootstrap 说明，§5.1/5.2 报告 p-values。R11 未标记。\"\n  resolution: \"Bootstrap 信息已添加到关键表格。\"\n  resolution_round: 11\n\n- id: \"R10-M2\"\n  summary: \"BibTeX orphan entries, duplicate keys\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仍有 10 个 orphan + 1 duplicate。R11-M1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M3\"\n  summary: \"Table 2 missing DocRED FT rows\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 2 现含 Qwen/Llama × SciERC/DocRED 全部 8 行。R11 未标记。\"\n  resolution: \"DocRED FT rows 已添加。\"\n  resolution_round: 11\n\n- id: \"R10-M4\"\n  summary: \"κ(r) symmetric relation normalization caveat\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§4 Eq.2 脚注已加 symmetric relation 说明。R11 未标记。\"\n  resolution: \"脚注已添加。\"\n  resolution_round: 11\n\n- id: \"R10-M5\"\n  summary: \"Constraint-induced parse failure increase unexplained\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.2 末尾加了解释（constraint masking alters token probability distributions）。R11 未标记。\"\n  resolution: \"1-sentence explanation 已添加。\"\n  resolution_round: 11\n\n- id: \"R10-M6\"\n  summary: \"Uncited bib entries\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"SchemaRL, GUIDEX, DCCD, REBEL, BoostCD 现已在 §6 引用。但 TANL 等仍为 orphan。R11-M1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Resolved from earlier rounds (confirmed in R11)\n# ============================================================\n\n- id: \"R9-SF6\"\n  summary: \"Related Work §6 over-compressed\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§6 expanded to 3 paragraphs. R11 confirmed adequate.\"\n  resolution_round: 10\n\n- id: \"R8-SF6\"\n  summary: \"Appendix AI writing traces\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Clean main text confirmed by R11.\"\n  resolution_round: 10\n\n- id: \"R8-M4\"\n  summary: \"Limitations dense paragraph needs subsections\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"3 paragraph subsections confirmed.\"\n  resolution_round: 10"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-19T08:54:04.590057+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 17361}, \"error\": \"\"}"}

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

_source line 1143 · 2026-05-19T08:56:45.104088+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May cycle\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计声明; R2: 新颖性+完整性+写作质量+格式合规）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\nOntoCoDec 将 IE schema 编译为两层 token-level 解码约束：grammar 层（基于 XGrammar）保证 JSON 结构有效性和词表成员资格，semantic 层通过 stateful entity registry 和动态 logit masking 执行 domain/range 类型约束。论文在 3 个数据集（SciERC, DocRED, WikiEvents）、4 个模型（8B-70B）、3 种解码策略上评估，展示了 LoRA+S1 配置下 DR≤0.20%、R-F1 ±0.6pp 的 composability 结果。Zero-shot 评估作为 stress test 展示了 76-99% 的 DR 降低（calibrated models），但伴随显著的 CF 上升（最高 12%）。\n\n---\n\n## Strengths\n\n**S1. [共识] 实验评估全面且诚实。** 3 数据集 × 4 模型 × 3 解码策略 × zero-shot/fine-tuned 两种 regime，配合 bootstrap 显著性检验（10,000 iterations），实验覆盖度远超同类工作。Mistral boundary condition 分析（§5.3）、CF-DR pilot ablation（Appendix B Table 5）、residual DR 四类 root cause 分解、Case Study 4 失败案例展示了罕见的科学诚实度。[R1: S3/S4; R2: S1]\n\n**S2. [共识] 两层架构的 enabling dependency 经实验有力验证。** Table 1 消融：semantic-only 仅降 DR 24%，加入 grammar 层后降至 94%。Fine-tuning 后 grammar 层成为 no-op，semantic 层独立贡献 39-72% DR reduction（Table 2, Appendix B Table 8）。Sequential pair-based enforcement 的等价性论证（§3.1 脚注: 33-37% spurious pairs avoided）严谨。[R1: S2; R2: S4]\n\n**S3. [共识] 问题定义精确且实用。** DR/RV/ET/CF 四类 violation 分类是功能性的，每类对应不同 enforcement 机制。Violation landscape 的实证分析为评估提供了可靠基线。[R1: S1]\n\n**S4. [共识] 工程贡献扎实、部署配置实用。** Tokenizer-agnostic continuation masking（§3.2, 覆盖 3 种 tokenizer 家族）、beam search 适配（125 行）、runtime overhead 2-13%。LoRA+S1 推荐配置（DR≤0.20%, +10% latency）具有明确的部署价值。[R1: S5; R2: S3]\n\n**S5. [共识] Constraint tightness (κ) 分析有价值。** 将违规率与 schema 结构量化关联，提供可解释的分析框架。Per-relation 分析（Appendix C）展示了 tightness 与残余 DR 的一致性。[R2: S2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [共识, critical] \"Near-lossless\" 叙事未充分呈现 CF trade-off。**\n\nAbstract 声称 \"near-lossless DR composability: DR≤0.20% with R-F1 within ±0.6pp, CF≤1.2%\"，但这仅限 LoRA+S1 配置。Zero-shot 下 CF 从 0.08% 飙升至 9.90%（SciERC）和 12.02%（Llama DocRED）。Total violation burden (DR+CF) 在 SciERC zero-shot 下仅从 15.45% 降至 10.83%（**降幅仅 30%**），远低于 DR 单独的 94%。Table 1 自己定义了 \"Tot. = DR + CF\" 并加粗标记，但正文叙事未以此为主线。\n\n即使在推荐配置 LoRA+S1 下，total burden 改善有限：Qwen SciERC 1.95%→1.18%（-0.77pp），Llama DocRED 0.49%→0.46%（**-0.03pp**）。Appendix B Table 5 的 pilot ablation 证明 CF↔DR 是结构性不可调和的 trade-off。\n\n**要求**：(1) Abstract 和 Introduction 中明确 \"near-lossless\" 仅指 LoRA+S1 下的 DR；(2) 将 total violation burden (DR+CF) 作为核心报告指标；(3) 将正文叙事主线调整为 LoRA+S1，zero-shot 降级为 diagnostic/stress-test。\n\n[R1-N1 + R2-N2, full consensus]\n\n**MF2. [共识, critical] 缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比。**\n\n论文在 §6 声称与 GoLLIE \"complementary\"（\"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"），但实验部分完全没有与 GoLLIE、KnowCoder、GenIE 等系统比较 violation rates。当前 baseline 全部是内部 ablation 变体（unconstrained/grammar-only/semantic-only/post-hoc filtering），无外部竞争方法。GoLLIE 代码和模型公开可用，这一缺失难以辩护。\n\n如果 GoLLIE 的 violation rate 已经很低，OntoCoDec 的增量价值需要重新评估；如果 GoLLIE+OntoCoDec 展示显著边际贡献，则 \"complementary\" claim 获得实证支撑。\n\n**要求**：至少以下之一：(1) GoLLIE 在 SciERC 上的 violation rate 对比实验；(2) 引用其论文中报告的 schema compliance 数据作为参照；(3) 明确论证不可比性原因。\n\n[R1-N2 + R2-W2, full consensus]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [共识, warning] Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据。**\n\nLinear regression（residual DR vs κ̄ × RV_baseline）仅 n=4 数据点（calibrated models），df=2，p≈0.058（不显著）。论文在 Appendix B 标注 \"descriptive characterization\"，但正文 §4 使用 \"consistent with\" 和 \"supports\" 等暗示因果性的措辞，并将此 pattern 作为全文核心解释框架（§1, §4, §5.2, §5.4）。\n\n**建议**：弱化正文措辞（加 n 限定），或增加 model×dataset 数据点。\n\n[R1-W1 + R2-W3, full consensus]\n\n**SF2. [共识, warning] WikiEvents \"preliminary\" 限定不足。**\n\n20-document test set（数据集本身限制），trigger F1 CI 极宽（-5.4/-0.6pp），但 Abstract line 10 \"The framework extends to event extraction without modification\" 缺乏 \"preliminary\" 限定。§5.4 标题 \"Preliminary Extension\" 是好的，但 Abstract 和 Contribution 列表的表述 confidence 偏高。\n\n**建议**：Abstract 和 Contribution 3 加 \"preliminary\" 限定词；§5.4 首段显式说明样本量限制。\n\n[R1-W2 + R2-W4, full consensus]\n\n**SF3. [共识, warning] Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡。**\n\n正文核心篇幅围绕 zero-shot（§5.1-5.3），但 R-F1 仅 2-8%。论文的辩护（ZS 是 stress test）出现在附录而非正文。推荐配置 LoRA+S1（R-F1 40-46，Table 2）反而篇幅不足。\n\n**建议**：§5 开头加 framing paragraph 明确 ZS 为 diagnostic；扩展 fine-tuning composability 讨论篇幅。\n\n[R2-W1 + R1 cross AGREE]\n\n**SF4. [共识, warning] Beam search DocRED 仅 50-doc subset，推广性受限。**\n\nSciERC beam search 评估了全量 551 docs，但 DocRED 仅 50 docs（Table 8 caption）。Clopper-Pearson 95% CI 上界 5.8%，50→998 docs 的推广性未讨论。\n\n**建议**：正文标注 subset 限制；解释未跑全量原因；讨论推广性。\n\n[R1-W3 + R2 cross AGREE]\n\n**SF5. [共识, warning] Abstract 数字密度过高（~15 个数字）。**\n\n审稿人在 30 秒内无法消化。核心 message 被数据淹没。R1 部分反驳（实证论文需数字支撑），但同意可精简 2-3 个。\n\n**建议**：保留 3-4 个关键数字（DR≤0.20%, ±0.6pp, 76-99%, CF≤1.2%），其余移至正文。\n\n[R2-W5, partial consensus]\n\n**SF6. [共识, warning] Entity registry 字段顺序依赖未显式讨论。**\n\nSemantic layer 依赖固定字段顺序（head→tail→relation→head_type→tail_type），通过 JSON Schema 强制。但：(1) 这一架构约束的强制机制（JSON Schema + XGrammar 编译）未显式说明；(2) Relation 引用未知实体时 fallback 退化为粗粒度 domain-only 约束，其对 CF 的影响未讨论。\n\n**建议**：§3.1 或 §3.2 加 1-2 句说明。\n\n[R2-W6 + R1 cross AGREE]\n\n### Minor（不影响接收）\n\n| ID | 问题 | 共识 |\n|----|------|------|\n| M1 | BibTeX 10 个 orphan entries + 1 duplicate key（schall2025hiddencost） | 共识 |\n| M2 | Compile time 不一致（§5 \"44ms\" vs Appendix B \"0.044s\" vs Appendix K \"0.33s\"） | 共识 |\n| M3 | WikiEvents 文档数不一致（Checklist 246 vs split 194+20+20=234） | 共识 |\n| M4 | §2 P(E×E) 幂集符号 P 未定义 | 共识 |\n| M5 | DocRED dev set：§5 脚注有说明但 Table 2 caption 未标注 | 共识 |\n| M6 | Table 1 caption 未定义 S1/S2 | 共识 |\n| M7 | \"Training-free\" 措辞与推荐配置（LoRA+S1 需 fine-tuning）可能误导；建议加明确区分 | R2 raised, R1 partial agree |\n| M8 | Table 2 DocRED grammar-only DR 上升至 26.17% (counter-intuitive) 需 caption 加注 | 共识 |\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成共识：\n\n1. **[AGREE] CF trade-off 是核心叙事缺陷** — Abstract 和 Introduction 的 \"near-lossless\" framing 需修正，total violation burden (DR+CF) 应成为核心指标。[MF1]\n2. **[AGREE] 缺少 schema-aware IE 系统 baseline** — GoLLIE 对比是最自然的缺失实验。[MF2]\n3. **[AGREE] Dual-factor 统计不足** — n=4, p≈0.058，正文措辞需弱化。[SF1]\n4. **[AGREE] WikiEvents preliminary 限定不足** — Abstract 和 Contribution 需加限定词。[SF2]\n5. **[AGREE] 正文 ZS/FT 比例失衡** — ZS ~40% 篇幅 vs R-F1 2-8%，推荐配置 LoRA+S1 篇幅不足。[SF3]\n6. **[AGREE] Beam search DocRED 50-doc 限制** — 需标注和讨论推广性。[SF4]\n7. **[AGREE] 实验评估全面且诚实** — 这是论文最强维度。[S1]\n8. **[AGREE] Enabling dependency 消融验证有力** — Table 1 的层间贡献分析清晰。[S2]\n\n---\n\n## Reviewer Divergence\n\n**[DIV1] 技术新颖性评估**\n\n- **R1 (Excitement 3/5)**: Sequential pair-based enforcement 的正确性论证、enabling dependency 的形式化验证、continuation masking 的跨 tokenizer 方案超越了纯工程范畴。论文贡献是 \"methods + empirical analysis\" 的组合，在 *ACL 中是 3/5 Excitement 的典型水平。将 R2-N1 评为 Should-Fix 而非 Must-Fix。建议定位为 \"methods-informed empirical study\"。\n- **R2 (Excitement 2.5/5)**: Grammar 层完全复用 XGrammar，semantic 层的 entity registry + dynamic masking 在概念上是字典查找+条件过滤，主要复杂性在工程而非算法。\"设计合理\"和\"有新颖性\"是不同维度。Findings track 正是为 \"technically sound, practically valuable, but incrementally novel\" 的工作设计。\n- **交叉后结果**: 双方维持各自立场。R2 表示如果 GoLLIE baseline 展示显著 incremental value，愿意上调至 3.5。\n\n---\n\n## Questions to Authors\n\n**Q1.** 在 LoRA+S1 推荐配置下，所有 model×dataset 配置的 total violation burden (DR+CF) 净变化数据是多少？目前可计算的数据显示 Llama DocRED 净减仅 0.03pp。\n\n**Q2.** 为什么不比较 GoLLIE 或类似 schema-aware 系统的 violation rates？GoLLIE 代码公开可用，即使 F1 不直接可比，violation rates 应可在相同数据集上测量。\n\n**Q3.** Entity registry 如何处理 relation 中首次出现、entity list 中未生成的实体？当前 fallback（退化为 dom(r) 全集约束）是否导致 pair-based enforcement 退化为粗粒度 domain-only？\n\n**Q4.** Beam search 在 DocRED 全量 998 docs 上的结果是什么？50-doc subset 的 DR=0% 是否可推广？\n\n**Q5.** Constraint tightness κ(r) 的 dual-factor 分析能否通过增加更多 model×dataset 数据点（如 WikiEvents、70B 模型）来增强统计效力？\n\n---\n\n## Missing References\n\n1. **TANL** (Paolini et al., 2021) — 已在 .bib 但未引用。Structured prediction as text generation 的早期工作，应在 §6 引用。[共识]\n2. **Wadhwa et al. (2023)** — 已引用但未用其 violation rate 数据作为 external baseline 参照点。[共识]\n3. **GenIE** (Josifoski et al., 2022) — 已在 Appendix A 引用但主体实验未比较。[R1]\n4. **BoostCD** (Sakota et al., 2025) — 已在 §6 引用但无实验对比。R1 认为设计哲学不同，可比性有限。[R2, R1 partial rebut]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 中 `external_review.paperreview_ai.enabled` 未启用），跳过。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Reviewer 评分分布**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)\n\n**评分依据**:\n\n论文解决了一个清晰且实际的问题（LLM IE 中的 type violation），提供了同类工作中最全面的实验验证，科学诚实度高。LoRA+S1 推荐配置具有明确的部署价值。\n\n但以下因素将评分限制在 Findings 档位：\n\n1. **CF trade-off 削弱核心叙事 [MF1]**: \"Near-lossless\" claim 在 zero-shot 下被 CF 副作用显著抵消（total violation burden 仅降 30%）。即使在推荐配置下，部分 model×dataset 的 total burden 改善极小（Llama DocRED -0.03pp）。这不是方法的根本缺陷（beam search 可解决，fine-tuning 大幅缓解），但 Abstract 和 Introduction 的叙事需要更诚实的重构。\n\n2. **缺少外部 baseline [MF2]**: 仅与内部 ablation 变体比较，无法判断相对 GoLLIE 等 schema-aware 系统的实际增量。这是可修复的缺失，但在当前状态下显著降低了贡献可信度。\n\n3. **技术新颖性有限 [DIV1]**: Grammar 层复用 XGrammar，semantic 层的核心操作（字典查找+条件 masking）概念直接。R1 认为 formalization + systematic analysis 组合足以支撑 Borderline Conference；R2 认为主要贡献是工程适配。Director 判断：论文的贡献介于方法论创新和工程框架之间，更接近后者。Findings track 是合适的定位。\n\n**上调条件**: 如果作者能 (1) 重构 CF 叙事使 total violation burden 成为核心指标，(2) 补充 GoLLIE violation rate 对比并展示显著边际贡献，评分有潜力提升至 3.5 (Borderline Conference)。R2 明确表示在 GoLLIE baseline 证据充分时愿意上调。\n\n**置信度**: 4/5（两位 Reviewer 均熟悉 constrained decoding 和 IE 领域，交叉讨论充分）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 3 中 \"extends to event extraction without modification\" 缺 \"preliminary\" 限定。\n- \"near-lossless composability\" 需限定为 \"near-lossless DR composability under fine-tuning\"，并在 contribution 列表中纳入 CF trade-off 作为 honest limitation。\n- 最后一句 \"training-free\" 与推荐配置（需 LoRA）存在潜在误导，建议区分。\n\n### §2 Background\n- P(E×E) 的 P（幂集）未定义。\n- 建议加注 entity list 在 relation list 之前生成的宏观顺序假设。\n\n### §3 Method\n- §3.1 字段顺序强制机制需显式说明（JSON Schema + XGrammar 编译如何保证）。\n- §3.2 relation 引用未知实体时的 fallback 行为（退化为 domain-only）及其对 CF 的影响值得讨论。\n- Continuation masking 的设计是亮点，但应在正文提及 Qwen vs Llama 的 semantic coverage 差异（100% vs 63.4%）。\n\n### §4 Constraint Composition\n- Dual-factor pattern 的正文措辞需弱化，加 n=4 限定。\n- κ(r) symmetric relation 脚注已添加（R10 遗留），确认。\n\n### §5 Experiments\n- 需在 §5 开头加 framing paragraph，明确 ZS 为 diagnostic、FT 为 deployment 主线。\n- Table 1 caption 需定义 S1/S2。\n- Table 2 caption 需标注 DocRED 为 dev set；grammar-only DR 上升需加注。\n- Beam search DocRED 50-doc 限制需正文标注。\n- WikiEvents 文档数 246 vs 234 需核实统一。\n- Compile time 不一致（44ms vs 0.044s vs 0.33s）需统一。\n\n### §6 Related Work\n- GoLLIE \"complementary\" claim 需实验支撑。\n- 引用 TANL（已在 .bib 但未 cite）。\n- BibTeX 清理：10 个 orphan entries + 1 duplicate key。\n\n### §7 Discussion and Conclusion\n- 已比 R10 改善。建议加入 total violation burden (DR+CF) 作为核心讨论指标。\n\n### Limitations\n- 覆盖全面（constraint scope, evaluation coverage, engineering considerations），是论文亮点。\n- 建议补充：empirically derived constraints 继承训练数据偏差/覆盖率不足的风险。\n\n### Checklist\n- 填写质量良好。WikiEvents 文档数需核实（B6: 246 vs split sum 234）。\n",
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
    "project": "schema_semantic_constrained_ie",
    "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May cycle\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（独立初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计声明; R2: 新颖性+完整性+写作质量+格式合规）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\nOntoCoDec 将 IE schema 编译为两层 token-level 解码约束：grammar 层（基于 XGrammar）保证 JSON 结构有效性和词表成员资格，semantic 层通过 stateful entity registry 和动态 logit masking 执行 domain/range 类型约束。论文在 3 个数据集（SciERC, DocRED, WikiEvents）、4 个模型（8B-70B）、3 种解码策略上评估，展示了 LoRA+S1 配置下 DR≤0.20%、R-F1 ±0.6pp 的 composability 结果。Zero-shot 评估作为 stress test 展示了 76-99% 的 DR 降低（calibrated models），但伴随显著的 CF 上升（最高 12%）。\n\n---\n\n## Strengths\n\n**S1. [共识] 实验评估全面且诚实。** 3 数据集 × 4 模型 × 3 解码策略 × zero-shot/fine-tuned 两种 regime，配合 bootstrap 显著性检验（10,000 iterations），实验覆盖度远超同类工作。Mistral boundary condition 分析（§5.3）、CF-DR pilot ablation（Appendix B Table 5）、residual DR 四类 root cause 分解、Case Study 4 失败案例展示了罕见的科学诚实度。[R1: S3/S4; R2: S1]\n\n**S2. [共识] 两层架构的 enabling dependency 经实验有力验证。** Table 1 消融：semantic-only 仅降 DR 24%，加入 grammar 层后降至 94%。Fine-tuning 后 grammar 层成为 no-op，semantic 层独立贡献 39-72% DR reduction（Table 2, Appendix B Table 8）。Sequential pair-based enforcement 的等价性论证（§3.1 脚注: 33-37% spurious pairs avoided）严谨。[R1: S2; R2: S4]\n\n**S3. [共识] 问题定义精确且实用。** DR/RV/ET/CF 四类 violation 分类是功能性的，每类对应不同 enforcement 机制。Violation landscape 的实证分析为评估提供了可靠基线。[R1: S1]\n\n**S4. [共识] 工程贡献扎实、部署配置实用。** Tokenizer-agnostic continuation masking（§3.2, 覆盖 3 种 tokenizer 家族）、beam search 适配（125 行）、runtime overhead 2-13%。LoRA+S1 推荐配置（DR≤0.20%, +10% latency）具有明确的部署价值。[R1: S5; R2: S3]\n\n**S5. [共识] Constraint tightness (κ) 分析有价值。** 将违规率与 schema 结构量化关联，提供可解释的分析框架。Per-relation 分析（Appendix C）展示了 tightness 与残余 DR 的一致性。[R2: S2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [共识, critical] \"Near-lossless\" 叙事未充分呈现 CF trade-off。**\n\nAbstract 声称 \"near-lossless DR composability: DR≤0.20% with R-F1 within ±0.6pp, CF≤1.2%\"，但这仅限 LoRA+S1 配置。Zero-shot 下 CF 从 0.08% 飙升至 9.90%（SciERC）和 12.02%（Llama DocRED）。Total violation burden (DR+CF) 在 SciERC zero-shot 下仅从 15.45% 降至 10.83%（**降幅仅 30%**），远低于 DR 单独的 94%。Table 1 自己定义了 \"Tot. = DR + CF\" 并加粗标记，但正文叙事未以此为主线。\n\n即使在推荐配置 LoRA+S1 下，total burden 改善有限：Qwen SciERC 1.95%→1.18%（-0.77pp），Llama DocRED 0.49%→0.46%（**-0.03pp**）。Appendix B Table 5 的 pilot ablation 证明 CF↔DR 是结构性不可调和的 trade-off。\n\n**要求**：(1) Abstract 和 Introduction 中明确 \"near-lossless\" 仅指 LoRA+S1 下的 DR；(2) 将 total violation burden (DR+CF) 作为核心报告指标；(3) 将正文叙事主线调整为 LoRA+S1，zero-shot 降级为 diagnostic/stress-test。\n\n[R1-N1 + R2-N2, full consensus]\n\n**MF2. [共识, critical] 缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比。**\n\n论文在 §6 声称与 GoLLIE \"complementary\"（\"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"），但实验部分完全没有与 GoLLIE、KnowCoder、GenIE 等系统比较 violation rates。当前 baseline 全部是内部 ablation 变体（unconstrained/grammar-only/semantic-only/post-hoc filtering），无外部竞争方法。GoLLIE 代码和模型公开可用，这一缺失难以辩护。\n\n如果 GoLLIE 的 violation rate 已经很低，OntoCoDec 的增量价值需要重新评估；如果 GoLLIE+OntoCoDec 展示显著边际贡献，则 \"complementary\" claim 获得实证支撑。\n\n**要求**：至少以下之一：(1) GoLLIE 在 SciERC 上的 violation rate 对比实验；(2) 引用其论文中报告的 schema compliance 数据作为参照；(3) 明确论证不可比性原因。\n\n[R1-N2 + R2-W2, full consensus]\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [共识, warning] Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据。**\n\nLinear regression（residual DR vs κ̄ × RV_baseline）仅 n=4 数据点（calibrated models），df=2，p≈0.058（不显著）。论文在 Appendix B 标注 \"descriptive characterization\"，但正文 §4 使用 \"consistent with\" 和 \"supports\" 等暗示因果性的措辞，并将此 pattern 作为全文核心解释框架（§1, §4, §5.2, §5.4）。\n\n**建议**：弱化正文措辞（加 n 限定），或增加 model×dataset 数据点。\n\n[R1-W1 + R2-W3, full consensus]\n\n**SF2. [共识, warning] WikiEvents \"preliminary\" 限定不足。**\n\n20-document test set（数据集本身限制），trigger F1 CI 极宽（-5.4/-0.6pp），但 Abstract line 10 \"The framework extends to event extraction without modification\" 缺乏 \"preliminary\" 限定。§5.4 标题 \"Preliminary Extension\" 是好的，但 Abstract 和 Contribution 列表的表述 confidence 偏高。\n\n**建议**：Abstract 和 Contribution 3 加 \"preliminary\" 限定词；§5.4 首段显式说明样本量限制。\n\n[R1-W2 + R2-W4, full consensus]\n\n**SF3. [共识, warning] Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡。**\n\n正文核心篇幅围绕 zero-shot（§5.1-5.3），但 R-F1 仅 2-8%。论文的辩护（ZS 是 stress test）出现在附录而非正文。推荐配置 LoRA+S1（R-F1 40-46，Table 2）反而篇幅不足。\n\n**建议**：§5 开头加 framing paragraph 明确 ZS 为 diagnostic；扩展 fine-tuning composability 讨论篇幅。\n\n[R2-W1 + R1 cross AGREE]\n\n**SF4. [共识, warning] Beam search DocRED 仅 50-doc subset，推广性受限。**\n\nSciERC beam search 评估了全量 551 docs，但 DocRED 仅 50 docs（Table 8 caption）。Clopper-Pearson 95% CI 上界 5.8%，50→998 docs 的推广性未讨论。\n\n**建议**：正文标注 subset 限制；解释未跑全量原因；讨论推广性。\n\n[R1-W3 + R2 cross AGREE]\n\n**SF5. [共识, warning] Abstract 数字密度过高（~15 个数字）。**\n\n审稿人在 30 秒内无法消化。核心 message 被数据淹没。R1 部分反驳（实证论文需数字支撑），但同意可精简 2-3 个。\n\n**建议**：保留 3-4 个关键数字（DR≤0.20%, ±0.6pp, 76-99%, CF≤1.2%），其余移至正文。\n\n[R2-W5, partial consensus]\n\n**SF6. [共识, warning] Entity registry 字段顺序依赖未显式讨论。**\n\nSemantic layer 依赖固定字段顺序（head→tail→relation→head_type→tail_type），通过 JSON Schema 强制。但：(1) 这一架构约束的强制机制（JSON Schema + XGrammar 编译）未显式说明；(2) Relation 引用未知实体时 fallback 退化为粗粒度 domain-only 约束，其对 CF 的影响未讨论。\n\n**建议**：§3.1 或 §3.2 加 1-2 句说明。\n\n[R2-W6 + R1 cross AGREE]\n\n### Minor（不影响接收）\n\n| ID | 问题 | 共识 |\n|----|------|------|\n| M1 | BibTeX 10 个 orphan entries + 1 duplicate key（schall2025hiddencost） | 共识 |\n| M2 | Compile time 不一致（§5 \"44ms\" vs Appendix B \"0.044s\" vs Appendix K \"0.33s\"） | 共识 |\n| M3 | WikiEvents 文档数不一致（Checklist 246 vs split 194+20+20=234） | 共识 |\n| M4 | §2 P(E×E) 幂集符号 P 未定义 | 共识 |\n| M5 | DocRED dev set：§5 脚注有说明但 Table 2 caption 未标注 | 共识 |\n| M6 | Table 1 caption 未定义 S1/S2 | 共识 |\n| M7 | \"Training-free\" 措辞与推荐配置（LoRA+S1 需 fine-tuning）可能误导；建议加明确区分 | R2 raised, R1 partial agree |\n| M8 | Table 2 DocRED grammar-only DR 上升至 26.17% (counter-intuitive) 需 caption 加注 | 共识 |\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成共识：\n\n1. **[AGREE] CF trade-off 是核心叙事缺陷** — Abstract 和 Introduction 的 \"near-lossless\" framing 需修正，total violation burden (DR+CF) 应成为核心指标。[MF1]\n2. **[AGREE] 缺少 schema-aware IE 系统 baseline** — GoLLIE 对比是最自然的缺失实验。[MF2]\n3. **[AGREE] Dual-factor 统计不足** — n=4, p≈0.058，正文措辞需弱化。[SF1]\n4. **[AGREE] WikiEvents preliminary 限定不足** — Abstract 和 Contribution 需加限定词。[SF2]\n5. **[AGREE] 正文 ZS/FT 比例失衡** — ZS ~40% 篇幅 vs R-F1 2-8%，推荐配置 LoRA+S1 篇幅不足。[SF3]\n6. **[AGREE] Beam search DocRED 50-doc 限制** — 需标注和讨论推广性。[SF4]\n7. **[AGREE] 实验评估全面且诚实** — 这是论文最强维度。[S1]\n8. **[AGREE] Enabling dependency 消融验证有力** — Table 1 的层间贡献分析清晰。[S2]\n\n---\n\n## Reviewer Divergence\n\n**[DIV1] 技术新颖性评估**\n\n- **R1 (Excitement 3/5)**: Sequential pair-based enforcement 的正确性论证、enabling dependency 的形式化验证、continuation masking 的跨 tokenizer 方案超越了纯工程范畴。论文贡献是 \"methods + empirical analysis\" 的组合，在 *ACL 中是 3/5 Excitement 的典型水平。将 R2-N1 评为 Should-Fix 而非 Must-Fix。建议定位为 \"methods-informed empirical study\"。\n- **R2 (Excitement 2.5/5)**: Grammar 层完全复用 XGrammar，semantic 层的 entity registry + dynamic masking 在概念上是字典查找+条件过滤，主要复杂性在工程而非算法。\"设计合理\"和\"有新颖性\"是不同维度。Findings track 正是为 \"technically sound, practically valuable, but incrementally novel\" 的工作设计。\n- **交叉后结果**: 双方维持各自立场。R2 表示如果 GoLLIE baseline 展示显著 incremental value，愿意上调至 3.5。\n\n---\n\n## Questions to Authors\n\n**Q1.** 在 LoRA+S1 推荐配置下，所有 model×dataset 配置的 total violation burden (DR+CF) 净变化数据是多少？目前可计算的数据显示 Llama DocRED 净减仅 0.03pp。\n\n**Q2.** 为什么不比较 GoLLIE 或类似 schema-aware 系统的 violation rates？GoLLIE 代码公开可用，即使 F1 不直接可比，violation rates 应可在相同数据集上测量。\n\n**Q3.** Entity registry 如何处理 relation 中首次出现、entity list 中未生成的实体？当前 fallback（退化为 dom(r) 全集约束）是否导致 pair-based enforcement 退化为粗粒度 domain-only？\n\n**Q4.** Beam search 在 DocRED 全量 998 docs 上的结果是什么？50-doc subset 的 DR=0% 是否可推广？\n\n**Q5.** Constraint tightness κ(r) 的 dual-factor 分析能否通过增加更多 model×dataset 数据点（如 WikiEvents、70B 模型）来增强统计效力？\n\n---\n\n## Missing References\n\n1. **TANL** (Paolini et al., 2021) — 已在 .bib 但未引用。Structured prediction as text generation 的早期工作，应在 §6 引用。[共识]\n2. **Wadhwa et al. (2023)** — 已引用但未用其 violation rate 数据作为 external baseline 参照点。[共识]\n3. **GenIE** (Josifoski et al., 2022) — 已在 Appendix A 引用但主体实验未比较。[R1]\n4. **BoostCD** (Sakota et al., 2025) — 已在 §6 引用但无实验对比。R1 认为设计哲学不同，可比性有限。[R2, R1 partial rebut]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 中 `external_review.paperreview_ai.enabled` 未启用），跳过。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Reviewer 评分分布**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)\n\n**评分依据**:\n\n论文解决了一个清晰且实际的问题（LLM IE 中的 type violation），提供了同类工作中最全面的实验验证，科学诚实度高。LoRA+S1 推荐配置具有明确的部署价值。\n\n但以下因素将评分限制在 Findings 档位：\n\n1. **CF trade-off 削弱核心叙事 [MF1]**: \"Near-lossless\" claim 在 zero-shot 下被 CF 副作用显著抵消（total violation burden 仅降 30%）。即使在推荐配置下，部分 model×dataset 的 total burden 改善极小（Llama DocRED -0.03pp）。这不是方法的根本缺陷（beam search 可解决，fine-tuning 大幅缓解），但 Abstract 和 Introduction 的叙事需要更诚实的重构。\n\n2. **缺少外部 baseline [MF2]**: 仅与内部 ablation 变体比较，无法判断相对 GoLLIE 等 schema-aware 系统的实际增量。这是可修复的缺失，但在当前状态下显著降低了贡献可信度。\n\n3. **技术新颖性有限 [DIV1]**: Grammar 层复用 XGrammar，semantic 层的核心操作（字典查找+条件 masking）概念直接。R1 认为 formalization + systematic analysis 组合足以支撑 Borderline Conference；R2 认为主要贡献是工程适配。Director 判断：论文的贡献介于方法论创新和工程框架之间，更接近后者。Findings track 是合适的定位。\n\n**上调条件**: 如果作者能 (1) 重构 CF 叙事使 total violation burden 成为核心指标，(2) 补充 GoLLIE violation rate 对比并展示显著边际贡献，评分有潜力提升至 3.5 (Borderline Conference)。R2 明确表示在 GoLLIE baseline 证据充分时愿意上调。\n\n**置信度**: 4/5（两位 Reviewer 均熟悉 constrained decoding 和 IE 领域，交叉讨论充分）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 3 中 \"extends to event extraction without modification\" 缺 \"preliminary\" 限定。\n- \"near-lossless composability\" 需限定为 \"near-lossless DR composability under fine-tuning\"，并在 contribution 列表中纳入 CF trade-off 作为 honest limitation。\n- 最后一句 \"training-free\" 与推荐配置（需 LoRA）存在潜在误导，建议区分。\n\n### §2 Background\n- P(E×E) 的 P（幂集）未定义。\n- 建议加注 entity list 在 relation list 之前生成的宏观顺序假设。\n\n### §3 Method\n- §3.1 字段顺序强制机制需显式说明（JSON Schema + XGrammar 编译如何保证）。\n- §3.2 relation 引用未知实体时的 fallback 行为（退化为 domain-only）及其对 CF 的影响值得讨论。\n- Continuation masking 的设计是亮点，但应在正文提及 Qwen vs Llama 的 semantic coverage 差异（100% vs 63.4%）。\n\n### §4 Constraint Composition\n- Dual-factor pattern 的正文措辞需弱化，加 n=4 限定。\n- κ(r) symmetric relation 脚注已添加（R10 遗留），确认。\n\n### §5 Experiments\n- 需在 §5 开头加 framing paragraph，明确 ZS 为 diagnostic、FT 为 deployment 主线。\n- Table 1 caption 需定义 S1/S2。\n- Table 2 caption 需标注 DocRED 为 dev set；grammar-only DR 上升需加注。\n- Beam search DocRED 50-doc 限制需正文标注。\n- WikiEvents 文档数 246 vs 234 需核实统一。\n- Compile time 不一致（44ms vs 0.044s vs 0.33s）需统一。\n\n### §6 Related Work\n- GoLLIE \"complementary\" claim 需实验支撑。\n- 引用 TANL（已在 .bib 但未 cite）。\n- BibTeX 清理：10 个 orphan entries + 1 duplicate key。\n\n### §7 Discussion and Conclusion\n- 已比 R10 改善。建议加入 total violation burden (DR+CF) 作为核心讨论指标。\n\n### Limitations\n- 覆盖全面（constraint scope, evaluation coverage, engineering considerations），是论文亮点。\n- 建议补充：empirically derived constraints 继承训练数据偏差/覆盖率不足的风险。\n\n### Checklist\n- 填写质量良好。WikiEvents 文档数需核实（B6: 246 vs split sum 234）。\n",
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

_source line 1144 · 2026-05-19T08:56:49.676259+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4572
}
```

</details>

---


### Assistant

_source line 1145 · 2026-05-19T08:56:56.888327+00:00_

审稿报告已投递至 Research Director。

**Round 11 审稿完成。**

总评 **3.0 (Findings)**，R1 给 3.5、R2 给 3.0。

两项 Must-Fix（共识）：
1. **CF 叙事重构** — "near-lossless" 仅限 LoRA+S1，total violation burden (DR+CF) 应成为核心指标，zero-shot 下总违规仅降 30%
2. **补充 GoLLIE baseline** — 当前无外部竞争方法对比，"complementary" claim 缺实验支撑

技术新颖性评估存在分歧（R1: 3/5 Excitement, R2: 2.5/5），双方交叉后维持各自立场，记录在报告中。

上调至 3.5 的条件：重构 CF 叙事 + GoLLIE 对比展示显著边际贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 81

## Round 81

2 recorded events


### User

_source line 1146 · 2026-05-19T08:56:59.566405+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：

- 与 R1 在 13/17 个要点上 **[AGREE]**，尤其在 CF trade-off（N1）和缺少 GoLLIE 对比（N2）两个 critical issues 上完全一致
- 仅在 3 个点上 **[REBUT]**：full FT 实验目的（W4, 部分反驳）、GenIE 引用已存在（Missing Refs）、κ 归一化问题是确认性的（Q5）
- 0.5 分差距（3.0 vs 3.5）的核心分歧在 Excitement 维度：我对"字典查找 + 条件 masking"的算法新颖性阈值更严格，但如果补充 GoLLIE baseline 证明 incremental value，愿意上调至 3.5

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

_source line 1147 · 2026-05-19T08:57:09.971811+00:00_

审稿报告已提交至 Research Director，Round 11 圆桌审稿完成。

**最终结果：Overall 3.0 (Findings)**

两位 Reviewer 在关键问题上高度收敛（13/17 要点共识），唯一重大分歧在技术新颖性评估（R1: 3.5 Borderline Conference, R2: 3.0 Findings）。

**2 个 Must-Fix**：
1. CF trade-off 叙事重构（total violation burden 应成为核心指标）
2. 补充 GoLLIE 等 schema-aware baseline 的 violation rate 对比

**6 个 Should-Fix**：dual-factor 统计弱化、WikiEvents preliminary 限定、ZS/FT 篇幅重分配、beam DocRED 50-doc 标注、Abstract 精简数字、entity registry 字段顺序说明

**上调路径**：解决两个 Must-Fix 后有潜力升至 3.5（R2 明确表态）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 82

## Round 82

76 recorded events


### User

_source line 1148 · 2026-05-20T17:06:17.092934+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
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

_source line 1149 · 2026-05-20T17:06:23.793145+00:00_

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

_source line 1150 · 2026-05-20T17:06:23.794103+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-20T17:06:28.864631+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch",
  "max_results": "6"
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1152 · 2026-05-20T17:06:28.865109+00:00_



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

_source line 1153 · 2026-05-20T17:06:31.677882+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer",
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
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-20T17:06:31.729192+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1155 · 2026-05-20T17:06:34.613715+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director project overview reviewer dispatch visual",
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
    "query": "director project overview reviewer dispatch visual",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1156 · 2026-05-20T17:06:34.664449+00:00_



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

_source line 1157 · 2026-05-20T17:06:39.535518+00:00_

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

_source line 1158 · 2026-05-20T17:06:40.993086+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (124 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- d066_sweep_llama_docred_beam4_s1（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_sweep_llama_scierc_beam4_s1_551** (success): d066 SciERC beam sweep: Llama beam4 constrained (full_s1) on 551-sentence test set. Beam width k=4 with schema constraints should eliminate all four violation types (ET/RV/DR/CF=0) while maintaining R-F1 within ±1pp of unconstrained.\n- **d066_sweep_llama_docred_beam4_unc** (success): d066 DocRED beam sweep sub-task: Llama beam4 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure. ← 基于 d066_beam_sweep\n- **d066_sweep_llama_docred_beam1_s1** (success): d066 DocRED beam sweep sub-task: Llama beam1 (greedy) constrained (full_s1) 
…[truncated 1052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 1159 · 2026-05-20T17:06:41.144092+00:00_

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

_source line 1160 · 2026-05-20T17:06:41.947593+00:00_

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
16	\usepackage{enumitem}
17	\usepackage{pifont}
18	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
19	
20	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
21	
22	\author{Anonymous ACL submission}
23	
24	\begin{document}
25	\maketitle
26	
27	% === Abstract ===
28	\input{abstract}
29	
30	% === §1 Introduction ===
31	\input{section1_introduction_draft}
32	
33	% === §2 Background ===
34	\input{section2_background}
35	
36	% === §3 Method ===
37	\input{section3_method_draft}
38	
39	% === §4 Constraint Composition ===
40	\section{Constraint Composition}
41	\label{sec:composition}
42	\input{section4_composition_draft}
43	
44	% === §5 Experiments ===
45	\section{Experiments}
46	\label{sec:experiments}
47	
48	\input{section3_violation_landscape}
49	
50	\input{section5_scierc_draft}
51	\input{section5_docred_draft}
52	\input{section5_crossmodel_draft}
53	\input{section5_wikievents_draft}
54	\input{section5_runtime}
55	
56	% === §6 Related Work ===
57	\input{section6_related_work}
58	
59	% === §7 Discussion and Conclusion ===
60	\section{Discussion and Conclusion}
61	\label{sec:discussion}
62	\input{section7_conclusion_compressed}
63	
64	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
65	\clearpage
66	\section*{Limitations}
67	
68	\paragraph{Constraint scope.}
69	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments 
…[truncated 3997 chars]

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

_source line 1161 · 2026-05-20T17:06:41.947996+00:00_

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


### Tool call

_source line 1162 · 2026-05-20T17:06:42.500388+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file,get_external_review_status",
  "max_results": "2"
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
    "query": "select:read_local_file,get_external_review_status",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-20T17:06:42.551089+00:00_

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


### Tool result

_source line 1164 · 2026-05-20T17:06:59.776239+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found relevant search results, but 
…[truncated 7545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 17828
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-20T17:07:03.091154+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file external_review_status",
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
    "query": "read_local_file external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-20T17:07:03.091601+00:00_



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

_source line 1167 · 2026-05-20T17:07:03.845130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit template anonymity guidelines 2026.emnlp.org"
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
    "query": "EMNLP 2026 ARR submission format page limit template anonymity guidelines 2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-20T17:07:09.751058+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit template anonymity guidelines 2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

Based on my search results, here is information about EMNLP 2026 ARR submission guidelines:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Anonymity Guidelines

Following the ACL and ARR policies, there is no anonymity period requirement. However, papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. 

The reviewing pr
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5905
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-20T17:07:12.915969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
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
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-20T17:07:12.916419+00:00_

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

_source line 1171 · 2026-05-20T17:07:13.218241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limits format requirements site:aclrollingreview.org"
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
    "query": "ACL Rolling Review 2026 author guidelines page limits format requirements site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-20T17:07:20.879730+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limits format requirements site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results from the ACL Rolling Review website, here are the key author guidelines for 2026:

**Format Requirements:**

The paper should follow ACL formatting, and authors are encouraged to use the ACL pubcheck tool and the official Overleaf template. The Overleaf template has a [review] setting that must be on for submission. ARR has abandoned the MS Word template, and submissions based on the Word template will be desk-rejected starting from March 2026.

ACLPUB formatting guidelines were updated in January 2025 with clarifications on font size in figures and tables, placement of limitations and ethical considera
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7661
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-20T17:07:28.911536+00:00_

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

_source line 1174 · 2026-05-20T17:07:30.317897+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-20T17:07:30.318349+00:00_

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

_source line 1176 · 2026-05-20T17:07:30.921328+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: d064 resolved + §5 fix (2026-05-20)
3	
4	# ============================================================
5	# Round 11 Must-Fix
6	# ============================================================
7	
8	- id: "R11-MF1"
9	  summary: "'Near-lossless' 叙事未充分呈现 CF trade-off — Abstract/Intro 需重构"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 11
14	  last_seen_round: 11
15	  mentions:
16	    - round: 11
17	      reviewers: [1, 2]
18	      note: "R1-N1 + R2-N2，full consensus。"
19	  action_items:
20	    - round: 11
21	      action: "Abstract 重写为 two-tier deployment narrative；near-lossless 全文清零；CF trade-off 前置呈现。"
22	      assigned_to: paper_agent
23	      status: done
24	  resolution: "R11 Paper Agent 完成 two-tier narrative 重构。grep 确认 near-lossless = 0 matches。Abstract 明确 LoRA+S1 (DR→0%, CF≤1.2%) + beam k=4 (zero violations)。"
25	  resolution_round: 11
26	
27	- id: "R11-MF2"
28	  summary: "缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比"
29	  category: experiment
30	  severity: critical
31	  status: resolved
32	  first_raised_round: 11
33	  last_seen_round: 11
34	  mentions:
35	    - round: 11
36	      reviewers: [1, 2]
37	      note: "R1-N2 + R2-W2，full consensus。"
38	  action_items:
39	    - round: 11
40	      action: "d063 GoLLIE 实验完成。ZS 仅提取 7 relations (vs ~800 GT)，数量级对比无意义。Kill switch：qualitative positioning only。"
41	      assigned_to: paper_agent
42	      status: done
43	  resolution: "d063 实验完成。GoLLIE ZS relation coverage 极低，数字对比无意义。§6 已加 qualitative positioning：'code-generation approaches such as GoLLIE achieve type compliance through format constraints (class names encode types) but with limited zero-shot relation coverage'。§7 加 complementary future direction。"
44	  resolution_round: 11
45	
46	# ============================================================
47	# Round 11 Should-Fix
48	# ============================================================
49	

…[truncated 15363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-20T17:07:30.971991+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
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
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-20T17:07:31.073031+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex
/home/ubuntu/.agent-ml-re
…[truncated 3990 chars]

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

_source line 1179 · 2026-05-20T17:07:41.134725+00:00_

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

_source line 1180 · 2026-05-20T17:07:41.637532+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that formally compiles Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) guarantees JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) enforces per-triple domain/range type constraints via a stateful entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$) rather than schema or model scale.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} eliminates DR violations (DR $\leq$ 0.09\%) with negligible R-F1 impact ($\pm$0.6\,pp); beam search ($k{=}4$) resolves the cross-field consistency (CF) trade-off, achieving zero violations on SciERC (R-F1 44--46, 1.54$\times$ latency).
7	Under zero-shot decoding, DR drops by 76--99\% for calibrated models.
8	The framework extends to event extraction without modification, validating the ontology-agnostic compilation design.
9	\textsc{OntoCoDec} compiles constraints automatically from any IE ontology at inference time, requires no constraint-specific training, and applies to any autoregressive LM across four models (8B--70B) and three tokenizer families.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1181 · 2026-05-20T17:07:41.637969+00:00_

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

_source line 1182 · 2026-05-20T17:07:41.989664+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption; reliable type-safety enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives, sacrificing recall; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-20T17:07:41.990180+00:00_

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

_source line 1184 · 2026-05-20T17:07:42.091044+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a framework that compiles IE ontologies into token-level constraints enforced during autoregressive generation.
9	The design is guided by a decidability analysis of IE type constraints.
10	
11	\paragraph{Constraint decidability taxonomy.}
12	\label{sec:decidability}
13	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
14	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
15	OntoCoDec guarantees levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
16	
17	\smallskip
18	\noindent
19	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
20	We formalize this gap:
21	
22	\smallskip
23	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
24	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
25	
26	\smallskip
27	\noindent\textit{Proof sketch.}
28	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
29	An output contains $n$ entities with independently chosen types ($a_i \in \{A, B\}$), followed by a relati
…[truncated 6538 chars]

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

_source line 1185 · 2026-05-20T17:07:48.268617+00:00_

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

_source line 1186 · 2026-05-20T17:07:48.721390+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	Among type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.
18	
19	\paragraph{Constraint Tightness.}
20	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):\footnote{For symmetric relations, $|\sigma(r)|$ counts ordered pairs; the normalization $|\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathc
…[truncated 2473 chars]

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

_source line 1187 · 2026-05-20T17:07:48.721807+00:00_

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

_source line 1188 · 2026-05-20T17:07:49.675856+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations.
8	LoRA + greedy S1 (\S\ref{sec:composability}) is the recommended fast configuration, eliminating DR violations with minimal latency overhead.
9	LoRA + beam S1 (\S\ref{sec:beam-results}) additionally resolves cross-field consistency, achieving zero total violations at 1.54$\times$ latency.
10	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) isolates layer contributions as a diagnostic; R-F1 2--8 reflects the absence of task-specific training, not method failure.
11	
12	\paragraph{Setup.}
13	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
14	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
15	The framework handles both sources without modification.
16	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
17	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
18	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref
…[truncated 155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1189 · 2026-05-20T17:07:49.676312+00:00_

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

_source line 1190 · 2026-05-20T17:07:50.029668+00:00_

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
…[truncated 5863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-20T17:07:50.030087+00:00_

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

_source line 1192 · 2026-05-20T17:07:50.080636+00:00_

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
…[truncated 2125 chars]

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

_source line 1193 · 2026-05-20T17:07:54.448361+00:00_

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

_source line 1194 · 2026-05-20T17:07:55.452946+00:00_

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
…[truncated 1797 chars]

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

_source line 1195 · 2026-05-20T17:07:55.453339+00:00_

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

_source line 1196 · 2026-05-20T17:07:55.453694+00:00_

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
…[truncated 2475 chars]

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

_source line 1197 · 2026-05-20T17:07:55.905865+00:00_

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

_source line 1198 · 2026-05-20T17:07:55.906279+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} guarantee format validity via CFG-based token masking; GCD~\cite{geng2023gcd} applies this to IE.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata.
9	These methods ensure syntactic validity but operate on static type declarations; IE requires a dynamic entity registry where constraint targets depend on the co-occurring relation type---a gap OntoCoDec fills with a semantic layer atop XGrammar.
10	
11	\paragraph{Schema-aware IE.}
12	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, and GUIDEX~\cite{guidex2025} encode ontology structure as typed code; REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} unify extraction via structured training, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
13	Code-generation approaches achieve type compliance via format constraints but produce 45\% empty outputs on zero-shot RE (vs.\ 0\% for OntoCoDec), reflecting a coverage--compliance trade-off that decoding-time enforcement avoids.
14	
15	\paragraph{Constraint enforcement in IE.}
16	\citet{roth_yih_2004} first formulated hard type constraints for IE via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation, requiring rejection cycles.
17	EnriCo~\cite{zaratiana2024enrico} and IterGen~\cite{ugare2025itergen} enforce constraints via ASP or backtracking but require hand-crafted rules per constraint; BoostCD~\c
…[truncated 325 chars]

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

_source line 1199 · 2026-05-20T17:07:56.508820+00:00_

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

_source line 1200 · 2026-05-20T17:07:56.559642+00:00_

1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.09\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	$\bar{\kappa}$ characterizes constraint regimes, with entity type confusability as the critical co-factor (Appendix~\ref{app:kappa-case-study}); the decidability taxonomy and $\bar{\kappa}$ diagnostic yield a principled deployment workflow.
6	

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

_source line 1201 · 2026-05-20T17:08:01.929519+00:00_

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

_source line 1202 · 2026-05-20T17:08:02.281597+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Full constraint compilation (schema parsing + grammar build): one-time $<$0.5\,s across all tested scales (Appendix~\ref{app:scalability}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both models and on DocRED for Llama (R-F1 44--47; Appendix~\ref{app:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models on SciERC (551 docs) and a DocRED subset (50 docs), and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama on SciERC); Mistral remains a boundary condition (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), one of three configurations to eliminate DR on DocRED (also achieved by LoRA + beam-4; Appendix~\ref{app:beam-search}).
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs 
…[truncated 181 chars]

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

_source line 1203 · 2026-05-20T17:08:02.282189+00:00_

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

_source line 1204 · 2026-05-20T17:08:02.734276+00:00_

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
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1205 · 2026-05-20T17:08:02.885395+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
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
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1206 · 2026-05-20T17:08:02.936018+00:00_

No files found

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

_source line 1207 · 2026-05-20T17:08:06.713993+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent"
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
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-20T17:08:07.065836+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_director_fb2e5824.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-20T17:08:07.668817+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
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
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1210 · 2026-05-20T17:08:07.821162+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1211 · 2026-05-20T17:08:11.086657+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "glob": "*.{yaml,yml,json,toml}",
  "output_mode": "content",
  "head_limit": "20"
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
    "glob": "*.{yaml,yml,json,toml}",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1212 · 2026-05-20T17:08:11.239987+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1213 · 2026-05-20T17:08:15.205625+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.{yaml,yml,json,toml,py}",
  "output_mode": "content",
  "head_limit": "20"
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
    "path": "/home/ubuntu/agent-ml-research",
    "glob": "*.{yaml,yml,json,toml,py}",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-20T17:08:15.256437+00:00_

/home/ubuntu/agent-ml-research/core/approvals/hooks.py:398:            # does not leak into Round N's request_external_review calls.
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:400:                from core.tools.external_review import reset_state as _reset_ext_review
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:428:            from core.tools.project_config import is_external_review_enabled
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:430:            _ext_review = is_external_review_enabled(project)
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:431:            logger.info("[review] external_review_enabled=%s for project=%s", _ext_review, project)
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:433:                f"\n**外部审稿**: 已启用（paperreview.ai）— 请在分配 Reviewer 的同时调用 `request_external_review(project=\"{project}\", paper_pdf_path=\"{paper_path}\", venue=\"{venue}\")` 发送外部审稿协助卡片。"
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:464:            from core.tools.project_config import is_external_review_enabled
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:465:            _ext_review = is_external_review_enabled(project)
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:467:                f"\n**外部审稿**: 已启用 — 请调用 `request_external_review(project=\"{project}\", paper_pdf_path=\"{paper_path}\", venue=\"{venue}\")`。"
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:530:                from core.tools.project_config import is_external_review_enabled as _ext_check
/home/ubuntu/agent-ml-research/core/approvals/hooks.py:532:                    from core.tools.external_review import request_external_review as _req_ext
/home/ubuntu/agent-ml-research/core/feishu_webhook.py:1065:def _handle_external_review_action(value: dict, open_message_id: str = "") -> Any:
/home/ubuntu/agent-ml-research/core/feishu_webhook.py:1066:    """Handle card button clicks from external review cards (paperreview.ai).
/home/ubuntu/a
…[truncated 848 chars]

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

_source line 1215 · 2026-05-20T17:08:19.372785+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "output_mode": "content",
  "head_limit": "20"
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
    "pattern": "external_review|paperreview\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-20T17:08:19.575628+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_9.md:169:**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置。
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md:155:外部审稿未配置（`external_review.paperreview_ai.enabled` 未在项目配置中找到），本轮未请求外部审稿。
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_5.md:181:外部审稿：未配置（项目配置中 `external_review.paperreview_ai.enabled` 未启用）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md:181:外部审稿：未配置（项目 config 中 `external_review.paperreview_ai.enabled` 未启用），跳过。
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_7.md:157:外部审稿：未配置（项目配置中 `external_review.paperreview_ai.enabled` 未启用）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `req
…[truncated 2058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Grep",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1217 · 2026-05-20T17:08:43.673285+00:00_

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

_source line 1218 · 2026-05-20T17:09:04.019893+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20346
}
```

</details>

---


### Tool call

_source line 1219 · 2026-05-20T17:09:04.173881+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review] 模式，Long paper 正文 8 页，参考文献不限\n- **匿名**: Double-blind（不得透露作者身份）\n- **必需**: Limitations section（不计页数）+ ARR Responsible NLP Research Checklist\n- **附录**: 允许，但审稿人无义务阅读\n\n## 你的审查侧重\n\n### 1. 形式化与方法论\n- Proposition 1（Level 2 ⊄ Level 1）的证明是否严谨？有无逻辑漏洞？\n- 约束可决性分类（context-free / prefix-decidable with state / non-local）是否完备且互斥？\n- Grammar-first fallback 的正确性保证——是否存在 corner case 导致无效输出？\n- Entity registry 的 soundness：动态构建过程中的 race condition 或顺序依赖问题\n- Sequential pair-based enforcement 的 exact 声称是否成立？\n\n### 2. 实验设计与统计\n- Five-way ablation 设计是否充分隔离了各层贡献？\n- Bootstrap 检验的使用是否规范（样本量、迭代次数、报告格式）\n- Cross-model validation（3 models）和 cross-dataset（SciERC/DocRED/WikiEvents）的覆盖是否足够\n- Fine-tuning composability 实验中的 confound 控制（LoRA 超参、learning rate）\n- Beam search 实验的规模（SciERC 551 docs full set vs DocRED 50/998 docs）\n- Zero-shot R-F1 2-8% 是否有意义作为 diagnostic——是否混淆了 constraint 效果与模型能力\n- WikiEvents 20-doc test set 的统计效力\n- Runtime overhead 测量方法和环境控制\n\n### 3. 可复现性\n- 实验是否提供了足够的细节以支持独立复现\n- Constraint compilation 代码是否有开源承诺\n- 数据集处理细节（DocRED dev set 选择原因、WikiEvents split）\n\n请以 ARR reviewer 标准完成审稿，输出包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review] 模式，Long paper 正文 8 页，参考文献不限\n- **匿名**: Double-blind（不得透露作者身份）\n- **必需**: Limitations section（不计页数）+ ARR Responsible NLP Research Checklist\n- **附录**: 允许，但审稿人无义务阅读\n\n## 你的审查侧重\n\n### 1. 形式化与方法论\n- Proposition 1（Level 2 ⊄ Level 1）的证明是否严谨？有无逻辑漏洞？\n- 约束可决性分类（context-free / prefix-decidable with state / non-local）是否完备且互斥？\n- Grammar-first fallback 的正确性保证——是否存在 corner case 导致无效输出？\n- Entity registry 的 soundness：动态构建过程中的 race condition 或顺序依赖问题\n- Sequential pair-based enforcement 的 exact 声称是否成立？\n\n### 2. 实验设计与统计\n- Five-way ablation 设计是否充分隔离了各层贡献？\n- Bootstrap 检验的使用是否规范（样本量、迭代次数、报告格式）\n- Cross-model validation（3 models）和 cross-dataset（SciERC/DocRED/WikiEvents）的覆盖是否足够\n- Fine-tuning composability 实验中的 confound 控制（LoRA 超参、learning rate）\n- Beam search 实验的规模（SciERC 551 docs full set vs DocRED 50/998 docs）\n- Zero-shot R-F1 2-8% 是否有意义作为 diagnostic——是否混淆了 constraint 效果与模型能力\n- WikiEvents 20-doc test set 的统计效力\n- Runtime overhead 测量方法和环境控制\n\n### 3. 可复现性\n- 实验是否提供了足够的细节以支持独立复现\n- Constraint compilation 代码是否有开源承诺\n- 数据集处理细节（DocRED dev set 选择原因、WikiEvents split）\n\n请以 ARR reviewer 标准完成审稿，输出包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1220 · 2026-05-20T17:09:20.222126+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16048
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-20T17:09:20.323918+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review] 模式，Long paper 正文 8 页，参考文献不限\n- **匿名**: Double-blind（不得透露作者身份）\n- **必需**: Limitations section（不计页数）+ ARR Responsible NLP Research Checklist\n- **附录**: 允许，但审稿人无义务阅读\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- OntoCoDec 相对于 XGrammar/Outlines/GCD 的技术增量——是否仅是工程集成？\n- Semantic layer（entity registry + dynamic masking）的学术新颖性——类似机制是否已存在于其他领域？\n- Constraint tightness κ̄ 作为分析框架的理论贡献——是否超越简单的描述性统计？\n- 与 GoLLIE/KnowCoder 等 schema-aware 方法的本质区别——论文是否充分论证？\n- 对比近期工作 CRANE、BoostCD、DCCD 等——论文是否遗漏了关键竞争者？\n\n### 2. 完整性\n- Contribution 列表是否与实验证据匹配？是否有 overclaim？\n- Related Work 覆盖是否完整？是否遗漏 2025-2026 关键文献？\n- Limitations section 是否诚实全面——是否回避了关键弱点？\n- 论文自述的 \"ontology-agnostic\" 声称——WikiEvents 验证是否足以支撑？\n- CF trade-off 的讨论是否充分——这是方法的核心局限\n\n### 3. 写作质量与格式\n- Abstract 信息密度是否合适？是否过于数字堆砌？\n- Introduction 叙事结构——problem → gap → solution → evidence 链是否连贯？\n- 表格和图的设计质量——信息呈现是否清晰高效？\n- 术语一致性（S1/S2、DR/CF/RV/ET、constraint tightness 等）\n- 8 页正文限制内信息密度是否合理——是否有关键内容被挤到附录？\n- 双盲合规性——是否有泄露身份的线索？\n- Checklist 完整性和准确性\n\n请以 ARR reviewer 标准完成审稿，输出包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止**: 2026-05-25\n- **格式**: ACL 模板 [review] 模式，Long paper 正文 8 页，参考文献不限\n- **匿名**: Double-blind（不得透露作者身份）\n- **必需**: Limitations section（不计页数）+ ARR Responsible NLP Research Checklist\n- **附录**: 允许，但审稿人无义务阅读\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- OntoCoDec 相对于 XGrammar/Outlines/GCD 的技术增量——是否仅是工程集成？\n- Semantic layer（entity registry + dynamic masking）的学术新颖性——类似机制是否已存在于其他领域？\n- Constraint tightness κ̄ 作为分析框架的理论贡献——是否超越简单的描述性统计？\n- 与 GoLLIE/KnowCoder 等 schema-aware 方法的本质区别——论文是否充分论证？\n- 对比近期工作 CRANE、BoostCD、DCCD 等——论文是否遗漏了关键竞争者？\n\n### 2. 完整性\n- Contribution 列表是否与实验证据匹配？是否有 overclaim？\n- Related Work 覆盖是否完整？是否遗漏 2025-2026 关键文献？\n- Limitations section 是否诚实全面——是否回避了关键弱点？\n- 论文自述的 \"ontology-agnostic\" 声称——WikiEvents 验证是否足以支撑？\n- CF trade-off 的讨论是否充分——这是方法的核心局限\n\n### 3. 写作质量与格式\n- Abstract 信息密度是否合适？是否过于数字堆砌？\n- Introduction 叙事结构——problem → gap → solution → evidence 链是否连贯？\n- 表格和图的设计质量——信息呈现是否清晰高效？\n- 术语一致性（S1/S2、DR/CF/RV/ET、constraint tightness 等）\n- 8 页正文限制内信息密度是否合理——是否有关键内容被挤到附录？\n- 双盲合规性——是否有泄露身份的线索？\n- Checklist 完整性和准确性\n\n请以 ARR reviewer 标准完成审稿，输出包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1222 · 2026-05-20T17:09:22.464018+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2140
}
```

</details>

---


### Assistant

_source line 1223 · 2026-05-20T17:09:29.597398+00:00_

Round 1 已启动：
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配
- **视觉审查 Agent**：已启动（fire-and-forget，不阻塞）
- **外部审稿**：未配置，跳过

等待两位 Reviewer 返回独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 1224 · 2026-05-20T17:17:40.487899+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**审查侧重：新颖性 + 完整性 + 写作质量**

---

## Summary

本文提出 OntoCoDec，一个将 IE 本体约束编译为双层解码约束的框架：语法层（S1）通过 XGrammar 保证 JSON 结构合法性和词汇成员关系；语义层（S2）通过运行时 entity registry 和 dynamic masking 强制 domain/range 类型兼容性。论文在 Proposition 1 中证明带无界实体集的类型约束不属于 context-free，从而为语义层的必要性提供了形式化论证。引入 constraint tightness κ̄ 作为 schema 限制性的描述性度量。在 SciERC（551篇）、DocRED（998篇）、WikiEvents（246篇）三个数据集上，使用 Qwen3-8B、Llama-3.1-8B、Mistral-7B 等模型进行了系统的消融实验。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 技术执行和实验设计高质量，但核心新颖性——语义层 dynamic masking——与已有工作（IterGen、PICARD 等）的概念差异阐述不足，κ̄ 作为"分析框架"的贡献被过度声称。

---

## 官方维度打分（来自 ACL ARR review form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 主要 claim 均有充分实验支撑；Proposition 1 形式化论证严谨；消融研究系统完整；论文坦诚承认 κ̄ 的统计局限性 |
| Excitement | 3/5 | 解决真实问题（LLM-IE 中的类型违规），实用价值明确；但核心技术增量（entity registry + dynamic masking）概念上较直接，κ̄ 更接近描述性统计而非深层理论贡献 |
| Reproducibility | 4/5 | 提供了详细的 prompt 模板（Appendix A）、超参数配置（Appendix F）、硬件信息、随机种子验证（Appendix F）；代码承诺开源但提交时未附 |
| Confidence | 4/5 | 熟悉 constrained decoding 和 structured IE 领域，仔细阅读了全部 31 页（含附录） |

---

## 主要优势

**S1. 形式化论证严谨且有实际意义。** Proposition 1（§3.1, p3）证明带无界实体集的 IE 类型约束不属于 context-free 语言，这为双层架构提供了不可跳过的理论基础。Corollary 进一步推导出 enabling dependency 的必要性。这不仅是学术优雅——它直接解释了为什么 XGrammar/Outlines 等纯 grammar 方案在 IE 场景下必然不足。

**S2. 违规分类法和消融设计极为系统。** 论文将输出违规分解为 DR（domain/range）、CF（cross-field）、RV（relation vocabulary）、ET（entity typing）四类（§5, Table 1），然后在每个消融配置下逐项报告。这种精细度远超同领域多数论文的二元"valid/invalid"评估，允许读者精确理解每层约束的贡献和代价。

**S3. 实验覆盖面广且诚实。** 三个数据集（sentence-level RE、document-level RE、event extraction）× 四个模型 × 多种配置（zero-shot / fine-tuned / beam search / S1 vs S2）。Limitations section（p9）明确承认：CF 是模型相关的、评估仅限一种微调方法（LoRA）、模型规模限于 7-8B。这种诚实度值得肯定。

**S4. Fine-tuning composability 论证有价值。** Table 2（p6）展示 LoRA fine-tuning + OntoCoDec 约束是可组合的：fine-tuning 减少 DR 至 1-2%，加入 S1 后进一步消除或接近消除 DR（< 0.09%），同时 R-F1 保持稳定。这回答了一个重要的部署问题——约束系统是否与参数优化兼容。

**S5. κ̄ 与违规率的关联分析提供实用的部署指导。** 尽管统计上不够confirmatory（论文自己承认 df=2, p>0.05），但 κ̄ × RV_baseline 作为 DR 的预测因子（Appendix C, Figure 1, p20）为实际部署中选择约束策略提供了直觉：κ > 0.5 的 schema 可在 zero-shot 下实现近零 DR，低 κ schema 需要 fine-tuning。

**S6. WikiEvents 扩展验证了跨本体泛化。** §5.4（p7）将框架扩展到事件抽取（KAIROS 本体，56 event types, 80 argument roles），无需修改即可应用。虽然只是 zero-shot 评估，但展示了框架在正式本体（vs. 经验衍生类型集）上的适用性。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 语义层核心机制（entity registry + dynamic masking）与 IterGen 的概念区分不充分

- 具体位置：§6 Related Work（p8）, Appendix B（p13-17）
- 问题：IterGen（Ugare et al., 2025, ICLR 2025）同样在 grammar 层之上叠加语义约束，在生成过程中检测违规并通过 backtracking 修正。OntoCoDec 的 dynamic masking 与 IterGen 的 semantic check + backtracking 是解决同一类问题（grammar-valid 但 semantically-invalid 输出）的两种机制。论文在 §6 和 Appendix B 中仅将 IterGen 列为相关工作之一，未深入对比两者在机制设计（preventive masking vs. corrective backtracking）、效率特性（OntoCoDec 无需回退 vs. IterGen 需要 KV cache 管理）、和约束表达能力（OntoCoDec 限于 domain/range vs. IterGen 支持任意 semantic predicate）上的差异。类似地，PICARD（Scholak et al., 2021）的 incremental parsing monitor 与 OntoCoDec 的 runtime entity registry 在概念上高度相似——均为在解码过程中维护状态以检查上下文相关约束。
- 为什么影响接收：新颖性是接收决定的关键维度。如果审稿人认为核心机制是已有方法（preventive masking / runtime monitor）在 IE 场景的 application，而非方法论创新，则难以达到 main conference 标准。
- 建议修改方向：在 §6 中增加一段显式的机制对比表（OntoCoDec vs. IterGen vs. PICARD），明确阐述：(1) OntoCoDec 的 forward-only masking 的效率优势及其 one-step-lookahead 的局限；(2) IterGen 的 backtracking 允许任意 semantic predicate 但引入 KV cache overhead 和 non-monotonic generation；(3) PICARD 的 token-level filtering 与 OntoCoDec entity registry 的粒度差异。

**N2** [critical] κ̄ 作为 Contribution 2（"analytical linking framework"）被过度声称

- 具体位置：Abstract（p1, "an analytical linking constraint tightness to enforcement outcomes"）, §1 Contributions 列表 item 2（p2）, §4（p4-5）
- 问题：κ̄ 的定义（§4, Eq. 3: κ = 1 − |S(r)|/|E|）本质上是每个 relation 的类型集合大小相对于总实体类型数的归一化比例——这是一个描述性统计量，而非一个分析框架。论文自身在 Appendix C（p20）承认回归分析"constitutes a descriptive characterization rather than a confirmatory statistical test"（df=2, p>0.05）。然而，Abstract 和 Contribution 列表仍将其定位为"analytical linking framework"，这与论文自身的谨慎表述不一致。
- 为什么影响接收：Contribution 列表的每一项都应与论文实际提供的证据水平匹配。将描述性统计提升为"分析框架"属于 overclaim，可能导致审稿人对整篇论文的 claim 可信度产生质疑。
- 建议修改方向：将 Contribution 2 重新表述为"a descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes and provides deployment guidance"，去掉"analytical framework"的措辞。在 Abstract 中也相应调整。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 无直接实验对比最接近的 IE 基线 BoostCD

- 具体位置：§5（p5-7）, §6（p8）
- 问题：BoostCD（Sakota et al., 2025）是唯一同样将 constrained decoding 应用于 IE 的已发表工作（EMNLP 2025），且使用了 SciERC 和 DocRED 作为评估数据集。论文引用了 BoostCD 但未进行任何实验对比。即使两者的 setting 不完全相同（BoostCD boosting 无约束/有约束解码；OntoCoDec 使用两层约束），也应提供同一数据集上的结果对比，或至少详细讨论为何直接比较不可行。
- 建议：(1) 如果 BoostCD 代码可用，在 SciERC 上运行对比实验；(2) 若不可行，在 §5 或 §6 中增加一段定性分析，引用 BoostCD 报告的数字并讨论方法论差异导致的预期性能差异。

**W2** [warning] "Ontology-agnostic" 声称的实验支撑不充分

- 具体位置：Abstract（p1）, §1 Contribution 3（p2）, §7（p8）
- 问题：三个评估数据集中，SciERC 和 DocRED 的类型约束来自训练数据的经验统计（"type pairs extracted from annotated training data"，§2, p2），并非形式化本体。仅 WikiEvents 使用了正式本体（KAIROS）。且 WikiEvents 评估仅为 zero-shot（246 篇），无 fine-tuning 验证。声称框架 "ontology-agnostic" 需要更强的证据——至少应在 2+ 个正式本体上验证，或明确限定 claim 的范围。
- 建议：将 "ontology-agnostic" 限定为 "applicable to both formal ontologies and empirically-derived type constraints"，并在 Limitations 中明确指出仅在一个正式本体上验证。

**W3** [warning] 正文 Related Work（§6）过于压缩

- 具体位置：§6（p8，约 15 行正文）
- 问题：正文 Related Work 仅覆盖三个轴各一小段，实质性讨论全部推迟到 Appendix B（p13-17, 约 2.5 页）。虽然 ARR 规则不禁止这种安排，但审稿人无义务阅读附录。正文中未充分讨论与关键竞争者（BoostCD、IterGen、CRANE、GoLLIE）的差异，使得审稿人难以仅从正文评判新颖性。
- 建议：在 8 页限制内，将 §6 扩展至至少半页，将 IterGen/BoostCD 的机制对比从附录移入正文。可通过压缩 §5.4（WikiEvents 细节可移入附录）来腾出空间。

**W4** [warning] Abstract 信息密度过高，关键 message 被数字淹没

- 具体位置：Abstract（p1）
- 问题：Abstract 中包含大量具体数字（"DR 40-46%"、"R-F1 0.099"、"76-99%"、"88-70B" 等），阅读体验接近结果表格的自然语言复述，而非对核心贡献的提炼。关键 insight（为什么 grammar 层不够、语义层如何补足、这对 IE 部署意味着什么）被数字细节遮蔽。
- 建议：保留 1-2 个最关键的数字（如 DR 减少幅度和 R-F1 保持稳定），其余推至 Introduction。Abstract 应更侧重 conceptual framing。

**W5** [warning] 模型规模限于 7-8B，对 claim 泛化性的影响在正文中未充分 hedge

- 具体位置：§5（p5-7）, §7（p8）
- 问题：所有实验使用 7-8B 参数模型。Limitations（p9）提到 "scaling to smaller models has not been verified"，但更值得关注的是向上的 scaling——70B+ 模型通常 baseline 违规率更低，OntoCoDec 的边际增益可能不同。§7 的结论 "drops by 76-99% for calibrated models" 未 hedge 模型规模。
- 建议：在 §7 结论中增加 "across 7-8B parameter models" 的限定词。

**W6** [warning] CF 代价在 Abstract/Contribution 中不够透明

- 具体位置：Abstract（p1）, §4（p4）
- 问题：Grammar-first fallback 在解决 DR 的同时引入 CF 违规（cross-field inconsistency）。Table 1 显示 Full S1 在 SciERC 上 CF 从 0 增至 ~0.33%。虽然 §4 和 Appendix C 详细讨论了这一 trade-off，但 Abstract 仅轻描淡写地提到 "grammar-first fallback when constraints conflict"，未量化其代价。审稿人可能认为论文在选择性地突出优势、淡化局限。
- 建议：在 Abstract 中增加一句简短的 trade-off 说明，如 "with modest cross-field consistency costs (≤0.33% on SciERC) resolvable via beam search or fine-tuning"。

---

## 小问题（不影响接收）

- **M1**: .bib 文件中有 10 个 orphan entries（在 bib 中但未在论文中引用），包括 `sakota2025boostcd`（与 `boostcd2025` 重复）、`lee2026formattax`（与 `formattax2026` 重复）等。应清理 bib 文件。
- **M2**: `schall2025hiddencost` bib key 重复出现两次。
- **M3**: §3.4 的 S1/S2 命名（Single-pass / Two-pass）与 §5 中的层级编号（S1 语法层、S2 语义层）初读时易混淆，虽然定义清晰但建议重命名为 SP/TP 或类似标记以避免歧义。
- **M4**: Table 5（p7, WikiEvents）的 "—" 标记（"not applicable"）缺少表注解释。
- **M5**: Appendix F（p26-27）提供了详细的复现细节，但 random seed 验证（seeds 123, 456）仅在 greedy decoding 下进行，beam search 的 non-determinism 仅报告了 variance < 0.5pp 而未提供具体 seed 信息。

---

## Questions for Authors

**Q1**: IterGen 的 backtracking 机制理论上可以处理任意 semantic predicate，而 OntoCoDec 的 dynamic masking 限于 domain/range 类型兼容。是否考虑过将 OntoCoDec 扩展到更一般的语义约束（如 cardinality constraints、temporal ordering）？如果有，主要技术障碍是什么？

**Q2**: Table 9（Appendix D, p21）显示 per-relation DR elimination 在 EVALUATE-FOR 关系上效果最好（κ=0.361）但在 COMPARE 关系上（κ=0.528）反而未完全消除。能否解释为什么更高的 κ 在此关系上未能完全消除 DR？

**Q3**: 在 DocRED 上 fine-tuning 后 R-F1 仅提升约 0.5pp（Table 2），但 DR 大幅下降。这是否意味着被消除的 DR violations 原本对 F1 的影响微乎其微（即它们主要出现在 precision 端的 false positives 中）？

**Q4**: 论文提到 entity registry 在 S1 模式下"populates dynamically"（§3.4），意味着在生成第一个 triple 时 registry 为空。如何处理第一个 triple 的 domain/range 约束？是否退化为纯 grammar 层？

---

## Missing References

1. **Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts** (Koldehoff et al., Frontiers in AI, 2025) — 将 grammar-constrained decoding + 本体约束应用于临床试验 IE，与 OntoCoDec 的方法论高度相关但在不同领域。
2. **Schema RL** (Lu et al., ACL 2025) — 论文 bib 中存在但未在正文中引用（orphan entry `schema_rl2025`）。该工作提出通过 RL 学习生成符合 schema 约束的结构化输出，应在 Related Work 中讨论。

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**  
**置信度: 4/5 (Quite sure)**

**理由**: 本文解决了一个真实且重要的问题（LLM-based IE 中的类型违规），提供了严格的形式化论证（Proposition 1）和系统的实验验证。实验设计质量高：四类违规分类法、三数据集四模型的消融矩阵、fine-tuning composability 验证。论文在 Limitations 中的自我批评也令人赞赏。

主要顾虑在新颖性和 claim 校准两方面：(1) 语义层的核心机制（runtime state tracking + preventive masking）在 constrained decoding 文献中并非全新——IterGen、PICARD 等已在其他领域建立了 grammar + semantic 的双层范式，OntoCoDec 的主要增量是将其专门化到 IE 本体约束；(2) κ̄ 在 contribution 列表中被过度包装为 "analytical framework"，与论文自身承认的描述性本质不一致。如果作者能更精确地定位新颖性（IE-specific compilation + dynamic masking 的效率优势）并降低 κ̄ 的声称级别，论文更可能达到 Conference 水平。目前的 claim 校准问题使其落在 Conference/Findings 的边界上。


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

_source line 1225 · 2026-05-20T17:17:56.111255+00:00_

Reviewer 2 审稿意见已收到。评分 3.5（Borderline Conference），核心关切：(1) 语义层与 IterGen/PICARD 的概念区分不足；(2) κ̄ 作为 "analytical framework" 的 overclaim。

等待 Reviewer 1 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 84

## Round 84

2 recorded events


### User

_source line 1226 · 2026-05-20T17:17:58.648421+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论摘要**：

- **Overall: 3.5（Borderline Conference）**，Soundness 4/5，Excitement 3/5
- **2个 Must-Fix**：(1) 语义层核心机制与 IterGen/PICARD 的概念区分不足，新颖性论证需要加强；(2) κ̄ 作为"analytical framework"被过度声称，应降级为"descriptive metric"
- **6个 Should-Fix**：无 BoostCD 直接实验对比、"ontology-agnostic"支撑不足、正文 Related Work 过于压缩、Abstract 数字过载、模型规模 hedge 不足、CF 代价透明度不够
- **5个 Minor**：bib 清理（10个 orphan + 1个 duplicate key）、S1/S2 命名歧义、表注缺失、seed 信息不完整
- **核心判断**：技术执行和实验设计是高质量的，但 claim 校准问题（κ̄ overclaim + 新颖性定位不精确）使论文落在 Conference/Findings 边界

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

_source line 1227 · 2026-05-20T17:18:07.774039+00:00_

Reviewer 2 审稿意见已收到（3.5 Borderline Conference）。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 85

## Round 85

6 recorded events


### User

_source line 1228 · 2026-05-20T17:19:28.056370+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**审查侧重**：方法严谨性 + 实验设计

---

## Summary

本文提出 OntoCoDec，一个将 IE 本体形式化编译为 token-level 解码约束的框架。核心思路是对 IE 类型约束进行可判定性分析（decidability analysis），将其分为三层：(1) context-free（JSON 结构 + 词汇表）由 XGrammar 语法层处理；(2) prefix-decidable with state（domain/range 类型合法性）由语义层通过动态 entity registry + semantic masking 处理；(3) non-local（跨 field 语义一致性）由 beam search 或 post-hoc 解决。实验覆盖 SciERC、DocRED、WikiEvents 三个数据集，Qwen3-8B / Llama-3.1-8B / Mistral-7B 三个模型，包含五路消融、beam search 兼容性、LoRA 微调组合性等多维评估。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference
**一句话总结**: 可判定性引导的约束分层是新颖且有工程价值的，但核心形式化结果缺乏严格证明，"exact enforcement" 声称与 36.64% CF fallback rate 矛盾，部分实验统计效力不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 形式化框架有洞见但 Proposition 1 仅为 proof sketch；"exact" enforcement 声称被 CF fallback 显著削弱；实验方法论整体规范但 WikiEvents 统计效力不足 |
| Excitement | 3.5/5 | 将形式语言理论的可判定性分析引入 IE 约束解码是新颖的视角；自动编译任意 IE 本体为约束有实际价值；但与 grammar-only baseline 相比语义层的边际增益在部分场景有限 |
| Reproducibility | 4/5 | 附录提供了详尽的超参数、硬件配置、seed 验证、prompt 模板；承诺代码开源；但部分实验（DocRED beam search 仅 50 文档子集）的完整复现需要澄清 |
| Confidence | 4/5 | 熟悉 constrained decoding 和 information extraction 领域，通读全文含 22 页附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proposition 1 证明不严格，与论文的形式化定位不匹配
- 具体位置：Section 3, §3.1, "Proof sketch"
- 问题：论文的核心贡献之一是"可判定性引导的约束分类"（decidability-guided constraint classification），Proposition 1（Level 2 ⊄ Level 1）是支撑这一框架的关键理论结果。然而论文仅给出 "proof sketch"：构造了一个 relation r with dom(r) = {τ₁, τ₂} 和 n 个独立选类型的 entity，论证 head-type field 需要回读 τ_{e(i)}，因此 PDDA 是必要的。这个论证是直觉性的，缺少：(a) 到已知不可判定性/语言层次结果的形式化归约；(b) 对 "independently unbound" 的精确定义（实际中 schema 的 JSON 结构会限制 n 和 k 的范围）；(c) 完整的数学证明（至少应放在附录中）。
- 为什么影响接收：如果论文将自身定位为"第一个形式化编译 IE 本体约束"的工作（Abstract: "formally compiles"），形式化结果的严格性是核心可信度的基础。一个仅有 proof sketch 的 proposition 无法支撑 "formal" 的声称。
- 建议修改方向：(1) 在附录中提供完整的形式化证明，包括明确的语言定义、CFG 无法识别该语言的泵引理论证或闭包性质论证；(2) 或者降低形式化声称的力度，将 Proposition 1 明确标注为 conjecture/informal argument，并相应调整 abstract 和 introduction 的措辞。

**N2** [critical] "Exact enforcement" 声称与 36.64% CF fallback rate 存在根本矛盾
- 具体位置：Abstract ("constraint tightness"), §3.3 ("exact pair-based enforcement"), §4 (Constraint Composition), Appendix C Table 7-8
- 问题：论文多处声称语义层实现了 "exact" 的 pair-based domain/range enforcement（§3.3）。但 Appendix C Table 8 显示 SciERC 上 GENERIC 类型的 conflicting-type pairs 占全部 CF violations 的 63.3%（155/245），grammar-first fallback 在 36.64% 的 type-bearing positions 被触发。当 fallback 触发时，语义约束被完全丢弃，退化为 grammar-only。这意味着约 1/3 的关键决策点上，系统实际并未执行语义约束。论文将此描述为"a soft error detectable by downstream validation"，但这与 "exact enforcement" 的声称矛盾。
- 进一步的问题：fallback 是否会级联？一次 fallback 导致的错误类型赋值是否会影响后续 entity registry 的状态，从而触发更多 fallback？论文未分析级联失败（cascading failures）的可能性。
- 为什么影响接收：如果核心技术声称（exact enforcement）在实践中有 1/3 的时间不成立，审稿人和读者会质疑方法的可靠性。这不是一个小的精度问题，而是核心 narrative 的准确性问题。
- 建议修改方向：(1) 将 "exact" 修改为更精确的表述，如 "best-effort pair-based enforcement with grammar-first fallback"；(2) 分析 fallback 的级联行为；(3) 报告 fallback 后的 entity registry 状态一致性。

**N3** [critical] WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力严重不足
- 具体位置：§5.4 (Extension to Event Extraction), Table 5, Limitations (page 9)
- 问题：WikiEvents 的 fine-tuning 评估使用标准 194/20/20 split（Li et al., 2021），测试集仅 20 篇文档。在如此小的样本上：(a) bootstrap p-values 不可靠；(b) 单个异常文档可大幅影响指标；(c) 置信区间极宽。论文在 Limitations 中披露了这一问题（"WikiEvents fine-tuning composability is preliminary (20-document test set)"），但正文 §5.4 的结论语气并未相应降低。例如 Table 5 直接与 SciERC/DocRED 的结果并列呈现，暗示同等可信度。
- 为什么影响接收：20-doc 测试集上的数字无法支撑 "framework generalizes to event extraction" 的声称（§5.4 标题为 "Extension to Event Extraction"）。即使零样本评估用了 246 文档（更好），fine-tuning 组合性的结论仍然不够可靠。
- 建议修改方向：(1) 在 §5.4 正文中明确标注测试集规模限制，降低结论语气；(2) 报告 WikiEvents fine-tuning 结果的 95% bootstrap 置信区间；(3) 考虑使用完整 246 文档进行 cross-validation 或 leave-one-out 评估来增强统计效力。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 缺少与最相关并发工作的直接实验对比
- 具体位置：§6 (Related Work), §5 (Experiments)
- 问题：论文在 Related Work 中讨论了 BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025) 等同期工作，但实验中未与其直接对比。BoostCD 尤其相关——它也针对 IE 任务使用 constrained decoding，并在相同数据集（SciERC）上有结果。论文的 S1（grammar-only）配置隐式对标了 GCD (Geng et al., 2023)，但未明确展示 head-to-head 数字。
- 为什么影响评分：缺乏直接对比使读者难以判断 OntoCoDec 相对于最新竞争方法的增量贡献。
- 建议：至少在 SciERC 上与 BoostCD、GCD 进行直接数字对比（即使引用其论文报告的数字），并讨论评估设置差异。

**W2** [warning] 跨模型验证局限于 7-8B 参数规模，泛化性声称不充分
- 具体位置：§5 (Experiments), Limitations (page 9)
- 问题：三个模型（Qwen3-8B, Llama-3.1-8B, Mistral-7B）均为 7-8B 参数量级。论文在 Limitations 中承认"scaling to smaller models has not been verified"，但正文的泛化性声称（如 Abstract: "applies to any autoregressive LM"）未加限定。更小的模型（1-3B）可能因能力不足导致更多 fallback；更大的模型（70B+）可能因基础能力更强而改变约束效果的模式。
- 建议：(1) 在 Abstract/Introduction 中限定为 "7-8B scale models"；(2) 或增加至少一个不同规模的模型（如 Qwen3-1.8B 或 Llama-3.1-70B）的实验。

**W3** [warning] 零样本 R-F1（0.08-8%）场景下 violation rate 分析的实际意义需要更明确的讨论
- 具体位置：§5.1 Table 1, §5.2 Table 3, §5.3 Table 4
- 问题：零样本设置下 R-F1 极低（SciERC 上 Qwen: 0.96%, Llama: ~0.08%），此时模型输出质量接近噪声水平。在这种条件下，violation rate（DR）的下降主要反映约束系统阻止了结构性错误，而非改善了抽取质量。论文将此定位为 "diagnostic"（§5 开头），这一定位是恰当的，但正文表格中零样本和微调结果并排呈现，读者可能误解零样本 DR 下降的实际价值。
- 建议：在 §5.1 开头更明确地说明：零样本 ablation 的目的是隔离各层贡献的违规消除效果（而非抽取质量提升），R-F1 过低意味着该场景下的约束主要价值是结构合规而非 task performance。

**W4** [warning] Entity registry 的顺序依赖可能导致 globally suboptimal type assignment
- 具体位置：§3.3 (Entity Registry), §3.3 (Dynamic Masking)
- 问题：Entity registry 在生成过程中动态构建，entity 类型赋值在生成时刻贪心确定。考虑以下场景：entity A 可被标注为类型 X 或 Y；如果贪心赋值为 X，后续某个 relation 需要类型 Y 的 head entity，导致 fallback 触发。如果赋值为 Y，则所有约束可满足。当前的贪心策略可能是局部最优但全局次优的。论文在 Appendix D 中通过 TCR（post-hoc type consistency resolution）部分解决了这个问题，但 TCR 是事后修复，不是生成时的 exact enforcement。
- 建议：讨论 entity type assignment 的顺序依赖性和贪心策略的局限性，将其作为 Level 3（non-local）约束的一个实例。

**W5** [warning] DocRED beam search 实验仅使用 50 文档子集
- 具体位置：Appendix E, Table 15
- 问题：SciERC 上 beam search 使用了完整 551 文档，但 DocRED 仅使用"matched 50-document subsets"。DocRED 文档更长（mean 198 tokens vs SciERC ~120 tokens）、关系类型更多（96 vs 7），beam search 在这类复杂文档上的表现可能与简单文档不同。50 文档子集可能不具代表性。
- 建议：报告 50 文档的选择标准和代表性分析；或至少在全 998 文档的子样本上运行 beam search (k=2) 以验证趋势一致性。

---

## Questions to Authors

Q1. Proposition 1 是否可以通过 pumping lemma for CFLs 或 Ogden's lemma 给出完整证明？当前的 proof sketch 中 "n and k are independently unbound" 的论证是否依赖于特定的 schema 结构？如果 schema 对 entity 数量设置上限（实际场景中常见），Proposition 1 是否仍然成立？

Q2. Grammar-first fallback 的级联行为：当一次 fallback 导致 entity 被赋予非预期类型时，该 entity 会被注册到 entity registry 中。后续引用该 entity 的 relation 是否会因此触发更多 fallback？是否有实验数据量化这种级联效应？

Q3. Table 1 中 S2（two-pass）的 DR 反而高于 Full S1——这是否说明 two-pass 架构引入了额外的错误来源（如第一阶段 entity extraction 的错误传播到第二阶段）？

Q4. LoRA fine-tuning 使用统一超参数（r=16, α=32）对三个不同模型，是否做过超参数敏感性分析？特别是 Mistral-7B 在多个指标上表现弱于 Qwen 和 Llama——这是模型能力差异还是超参数不匹配？

Q5. Constraint tightness κ（§4, Table 19 footnote area）的计算中，对称关系的处理方式是什么？论文 footnote 1 提到"for symmetric relations, σ(r) counts ordered pairs; the denominator 2τ² remains appropriate since we evaluate on directed triples"——这是否意味着对称关系的实际约束比 κ 值显示的更紧？

---

## Missing References / 比较

1. **BoostCD (Sakota et al., 2025)**: 已引用但未实验对比。作为同样在 SciERC 上做 IE constrained decoding 的工作，缺乏直接数字对比是显著遗漏。
2. **GCD (Geng et al., 2023)**: 已引用，S1 配置隐式对标，但应在实验部分明确展示 GCD 的数字作为 baseline。
3. 可考虑引用 **Schema-RL (Lu et al., 2025)** 在正文中（目前仅在 bib 中未被引用），作为 training-based structured output 的对比方法。

引用审计结果：
- 10 条 orphan bib entries（在 .bib 中但未被引用）：包括 delafuente2025guidex, geng2025jsonschemabench, lee2026formattax 等，均为与已引用条目的重复版本。
- 1 条重复 bib key: schall2025hiddencost 出现两次。
- 3 条 online not found: regino2025kgcurator, formattax2026, lee2026formattax（后两者为同一论文的重复条目，arXiv 2604.03616 可能尚未被 OpenAlex 索引）。
- 这些都是 minor cleanup 问题，不影响审稿判断。

---

## 小问题（不影响接收）

- §4 Eq.(2)：M_final = M_grammar(t) ∧ M_semantic(t) 的 conjunction 是逐位 AND——应明确说明这是 token-level 的逐位操作而非 set intersection 的简写，避免歧义。
- Table 1-3 中 "CF" 列的含义（context-free violation 即 cross-field violation）在首次出现时未充分解释，需要回读 §3 才能理解。建议在表格 caption 或首次引用处加注。
- Figure 1（page 20）的 scatter plot：x 轴 label "κ · RV_baseline" 的物理含义不直观，建议在 caption 中补充解释。
- Appendix G 报告 "completion-only loss for 3 epochs"——对于 DocRED（3,053 examples / 998 dev）仅 3 epochs 是否充分？是否观察到 loss 收敛？
- Page 8, §6 Related Work 最后一段提到 "the decidability taxonomy and a κ-diagnostic yield a principled deployment workflow"——这读起来更像 contribution 声称而非 related work 讨论，建议调整位置。

---

## 主要优势

1. **新颖的形式化视角**：将 formal language theory 的可判定性分析引入 IE 约束解码，提出 context-free / prefix-decidable with state / non-local 的三层分类。这在 constrained decoding for NLP 领域是新颖的，为系统设计提供了有原则的指导。

2. **全面的实验设计**：五路消融清晰隔离了 grammar 层和 semantic 层的贡献；跨模型（3 个）、跨数据集（3 个）、跨任务（RE + EE）的覆盖在 systems paper 中高于平均水平。

3. **诚实的局限性讨论**：论文对 WikiEvents 样本量、模型规模限制、CF trade-off 等问题的披露异常坦诚，这在投稿论文中值得肯定。

4. **实际工程价值**：框架自动从任意 IE 本体编译约束，无需约束特定训练，可与任意自回归 LM 配合——这使其具有即插即用的实际部署价值。LoRA fine-tuning 组合性实验表明约束不干扰微调效果。

5. **丰富的附录**：22 页附录包含详尽的错误分析（Appendix J case studies）、scalability benchmarks（Appendix K）、prompt 敏感性（Appendix I）、document length 分析（Appendix H）、TCR 机制（Appendix D/Tables 30-31）。这些内容显著增强了论文的可复现性和可信度。

6. **Constraint tightness κ 指标**：作为部署指导工具（§4 末尾、Appendix C），κ 与 DR reduction 的相关性（Figure 2, r=0.886）为实践者提供了预测约束效果的依据——这是有实用价值的贡献。

---

## Overall Assessment

**评分：3.5 — Borderline Conference**

本文提出了一个有新意的框架，将形式语言理论的可判定性分析引入 IE 约束解码，实验覆盖面广且附录详尽。主要顾虑是：(1) 核心形式化结果（Proposition 1）仅为 proof sketch，与论文的 "formally compiles" 定位不匹配；(2) "exact enforcement" 的核心声称被 36.64% CF fallback rate 实质性削弱；(3) WikiEvents fine-tuning 评估的统计效力不足。如果作者能在修改中加强证明严格性、校准技术声称的精确度、并补充 WikiEvents 的统计分析，本文有潜力成为 solid conference paper。当前状态下，建议 Borderline Conference / strong Findings。

**Confidence: 4/5** — 熟悉 constrained decoding 和 information extraction 领域，通读全文含全部 22 页附录及引用验证。

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

_source line 1229 · 2026-05-20T17:20:17.216882+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall: 3.5 Borderline Conference | Soundness 4/5 | Excitement 3/5 | Reproducibility 4/5 | Confidence 4/5**\n\n### Must-Fix\n\n**N1** [critical] 语义层核心机制（entity registry + dynamic masking）与 IterGen 的概念区分不充分\n- §6 Related Work（p8）, Appendix B（p13-17）\n- IterGen（Ugare et al., 2025, ICLR 2025）同样在 grammar 层之上叠加语义约束，在生成过程中检测违规并通过 backtracking 修正。OntoCoDec 的 dynamic masking 与 IterGen 的 semantic check + backtracking 是解决同一类问题（grammar-valid 但 semantically-invalid 输出）的两种机制。论文在 §6 和 Appendix B 中仅将 IterGen 列为相关工作之一，未深入对比两者在机制设计（preventive masking vs. corrective backtracking）、效率特性（OntoCoDec 无需回退 vs. IterGen 需要 KV cache 管理）、和约束表达能力（OntoCoDec 限于 domain/range vs. IterGen 支持任意 semantic predicate）上的差异。类似地，PICARD（Scholak et al., 2021）的 incremental parsing monitor 与 OntoCoDec 的 runtime entity registry 在概念上高度相似。\n- 建议：§6 增加显式机制对比表（OntoCoDec vs. IterGen vs. PICARD）。\n\n**N2** [critical] κ̄ 作为 Contribution 2（\"analytical linking framework\"）被过度声称\n- Abstract（p1）, §1 Contributions 列表 item 2（p2）, §4（p4-5）\n- κ̄ 本质上是描述性统计量（|S(r)|/|E|² 的归一化比例），论文自身在 Appendix C 承认 \"descriptive characterization rather than a confirmatory statistical test\"（df=2, p>0.05）。但 Abstract 和 Contribution 列表仍将其定位为 \"analytical linking framework\"。\n- 建议：降级为 \"descriptive metric that correlates with enforcement outcomes\"。\n\n### Should-Fix\n\n**W1** [warning] 无直接实验对比最接近的 IE 基线 BoostCD\n- BoostCD（Sakota et al., 2025）同样将 constrained decoding 应用于 IE，使用了 SciERC 和 DocRED。\n\n**W2** [warning] \"Ontology-agnostic\" 声称的实验支撑不充分\n- 仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 来自训练数据经验统计。\n\n**W3** [warning] 正文 Related Work（§6）过于压缩（约 15 行），实质讨论全部推迟到附录\n\n**W4** [warning] Abstract 信息密度过高，关键 message 被数字淹没\n\n**W5** [warning] 模型规模限于 7-8B，正文泛化性声称未充分 hedge\n\n**W6** [warning] CF 代价在 Abstract/Contribution 中不够透明\n\n### Minor\n- M1: .bib 文件中有 10 个 orphan entries\n- M2: schall2025hiddencost bib key 重复\n- M3: S1/S2 命名与层级编号初读易混淆\n- M4: Table 5 \"—\" 标记缺少表注\n- M5: Beam search seed 信息不完整\n\n### Questions\nQ1: 是否考虑将 OntoCoDec 扩展到更一般的语义约束（cardinality, temporal ordering）？\nQ2: Per-relation DR 在 COMPARE 关系上（κ=0.528）未完全消除，why？\nQ3: Fine-tuning 后 R-F1 仅提升 0.5pp 但 DR 大幅下降——被消除的 DR violations 对 F1 影响微乎其微？\nQ4: S1 模式下第一个 triple 的 domain/range 如何处理（registry 为空时）？\n\n### Missing References\n1. Koldehoff et al. (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE\n2. Schema RL (Lu et al., ACL 2025) — 存在于 bib 但未被引用"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n**Overall: 3.5 Borderline Conference | Soundness 4/5 | Excitement 3/5 | Reproducibility 4/5 | Confidence 4/5**\n\n### Must-Fix\n\n**N1** [critical] 语义层核心机制（entity registry + dynamic masking）与 IterGen 的概念区分不充分\n- §6 Related Work（p8）, Appendix B（p13-17）\n- IterGen（Ugare et al., 2025, ICLR 2025）同样在 grammar 层之上叠加语义约束，在生成过程中检测违规并通过 backtracking 修正。OntoCoDec 的 dynamic masking 与 IterGen 的 semantic check + backtracking 是解决同一类问题（grammar-valid 但 semantically-invalid 输出）的两种机制。论文在 §6 和 Appendix B 中仅将 IterGen 列为相关工作之一，未深入对比两者在机制设计（preventive masking vs. corrective backtracking）、效率特性（OntoCoDec 无需回退 vs. IterGen 需要 KV cache 管理）、和约束表达能力（OntoCoDec 限于 domain/range vs. IterGen 支持任意 semantic predicate）上的差异。类似地，PICARD（Scholak et al., 2021）的 incremental parsing monitor 与 OntoCoDec 的 runtime entity registry 在概念上高度相似。\n- 建议：§6 增加显式机制对比表（OntoCoDec vs. IterGen vs. PICARD）。\n\n**N2** [critical] κ̄ 作为 Contribution 2（\"analytical linking framework\"）被过度声称\n- Abstract（p1）, §1 Contributions 列表 item 2（p2）, §4（p4-5）\n- κ̄ 本质上是描述性统计量（|S(r)|/|E|² 的归一化比例），论文自身在 Appendix C 承认 \"descriptive characterization rather than a confirmatory statistical test\"（df=2, p>0.05）。但 Abstract 和 Contribution 列表仍将其定位为 \"analytical linking framework\"。\n- 建议：降级为 \"descriptive metric that correlates with enforcement outcomes\"。\n\n### Should-Fix\n\n**W1** [warning] 无直接实验对比最接近的 IE 基线 BoostCD\n- BoostCD（Sakota et al., 2025）同样将 constrained decoding 应用于 IE，使用了 SciERC 和 DocRED。\n\n**W2** [warning] \"Ontology-agnostic\" 声称的实验支撑不充分\n- 仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 来自训练数据经验统计。\n\n**W3** [warning] 正文 Related Work（§6）过于压缩（约 15 行），实质讨论全部推迟到附录\n\n**W4** [warning] Abstract 信息密度过高，关键 message 被数字淹没\n\n**W5** [warning] 模型规模限于 7-8B，正文泛化性声称未充分 hedge\n\n**W6** [warning] CF 代价在 Abstract/Contribution 中不够透明\n\n### Minor\n- M1: .bib 文件中有 10 个 orphan entries\n- M2: schall2025hiddencost bib key 重复\n- M3: S1/S2 命名与层级编号初读易混淆\n- M4: Table 5 \"—\" 标记缺少表注\n- M5: Beam search seed 信息不完整\n\n### Questions\nQ1: 是否考虑将 OntoCoDec 扩展到更一般的语义约束（cardinality, temporal ordering）？\nQ2: Per-relation DR 在 COMPARE 关系上（κ=0.528）未完全消除，why？\nQ3: Fine-tuning 后 R-F1 仅提升 0.5pp 但 DR 大幅下降——被消除的 DR violations 对 F1 影响微乎其微？\nQ4: S1 模式下第一个 triple 的 domain/range 如何处理（registry 为空时）？\n\n### Missing References\n1. Koldehoff et al. (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE\n2. Schema RL (Lu et al., ACL 2025) — 存在于 bib 但未被引用"
  }
}
```

</details>

---


### Tool result

_source line 1230 · 2026-05-20T17:20:42.636064+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25419
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-20T17:20:42.787853+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall: 3.5 Borderline Conference | Soundness 3.5/5 | Excitement 3.5/5 | Reproducibility 4/5 | Confidence 4/5**\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 证明不严格，与论文的形式化定位不匹配\n- Section 3, §3.1, \"Proof sketch\"\n- 论文核心贡献之一是\"可判定性引导的约束分类\"，Proposition 1（Level 2 ⊄ Level 1）仅给出 proof sketch，缺少：(a) 到已知不可判定性结果的形式化归约；(b) \"independently unbound\" 的精确定义；(c) 完整数学证明。\n- 建议：附录中提供完整形式化证明（pumping lemma / 闭包性质），或降低形式化声称力度。\n\n**N2** [critical] \"Exact enforcement\" 声称与 36.64% CF fallback rate 存在根本矛盾\n- Abstract, §3.3 (\"exact pair-based enforcement\"), §4, Appendix C Table 7-8\n- Appendix C 显示 grammar-first fallback 在 36.64% 的 type-bearing positions 被触发。当 fallback 时语义约束被完全丢弃。论文未分析级联失败（cascading failures）的可能性——一次 fallback 的错误类型赋值是否影响后续 entity registry 状态。\n- 建议：将 \"exact\" 改为 \"best-effort pair-based enforcement with grammar-first fallback\"；分析 fallback 级联行为。\n\n**N3** [critical] WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力严重不足\n- §5.4, Table 5, Limitations (page 9)\n- 20 篇文档上 bootstrap p-values 不可靠，置信区间极宽，但 Table 5 与 SciERC/DocRED 并列暗示同等可信度。\n- 建议：正文中明确标注规模限制，报告 95% bootstrap CI，考虑 cross-validation。\n\n### Should-Fix\n\n**W1** [warning] 缺少与最相关并发工作的直接实验对比\n- 未与 BoostCD、CRANE、IterGen、GCD 直接对比数字。\n\n**W2** [warning] 跨模型验证局限于 7-8B 参数规模\n- Abstract \"applies to any autoregressive LM\" 未加限定。\n\n**W3** [warning] 零样本 R-F1（0.08-8%）场景下 violation rate 分析的实际意义需要更明确讨论\n- 论文定位为 \"diagnostic\" 是恰当的，但表格中零样本和微调结果并排呈现可能误导读者。\n\n**W4** [warning] Entity registry 的顺序依赖可能导致 globally suboptimal type assignment\n- 贪心策略局部最优但全局次优，TCR 是事后修复而非生成时 exact enforcement。\n\n**W5** [warning] DocRED beam search 实验仅使用 50 文档子集\n- SciERC 用了完整 551 文档，DocRED 仅 50 文档。DocRED 文档更长、关系类型更多。\n\n### Minor\n- §4 Eq.(2) conjunction 是逐位 AND 应明确说明\n- CF 列含义首次出现时未充分解释\n- Figure 1 x 轴 label 不直观\n- Appendix G LoRA 3 epochs 是否充分\n- §6 末尾一段更像 contribution 声称\n\n### Questions\nQ1: Proposition 1 能否通过 pumping lemma 完整证明？schema 对 entity 数量设上限时是否仍成立？\nQ2: Grammar-first fallback 的级联行为——一次 fallback 的错误类型赋值是否触发更多 fallback？\nQ3: S2 的 DR 反而高于 S1——two-pass 是否引入额外错误来源？\nQ4: LoRA 统一超参数（r=16, α=32）是否做过敏感性分析？\nQ5: 对称关系的 κ 计算是否低估了实际约束紧度？\n\n### Missing References\n1. BoostCD (Sakota et al., 2025) — 已引用但未实验对比\n2. GCD (Geng et al., 2023) — 应明确展示 baseline 数字\n3. Schema-RL (Lu et al., 2025) — bib 中未被引用"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall: 3.5 Borderline Conference | Soundness 3.5/5 | Excitement 3.5/5 | Reproducibility 4/5 | Confidence 4/5**\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 证明不严格，与论文的形式化定位不匹配\n- Section 3, §3.1, \"Proof sketch\"\n- 论文核心贡献之一是\"可判定性引导的约束分类\"，Proposition 1（Level 2 ⊄ Level 1）仅给出 proof sketch，缺少：(a) 到已知不可判定性结果的形式化归约；(b) \"independently unbound\" 的精确定义；(c) 完整数学证明。\n- 建议：附录中提供完整形式化证明（pumping lemma / 闭包性质），或降低形式化声称力度。\n\n**N2** [critical] \"Exact enforcement\" 声称与 36.64% CF fallback rate 存在根本矛盾\n- Abstract, §3.3 (\"exact pair-based enforcement\"), §4, Appendix C Table 7-8\n- Appendix C 显示 grammar-first fallback 在 36.64% 的 type-bearing positions 被触发。当 fallback 时语义约束被完全丢弃。论文未分析级联失败（cascading failures）的可能性——一次 fallback 的错误类型赋值是否影响后续 entity registry 状态。\n- 建议：将 \"exact\" 改为 \"best-effort pair-based enforcement with grammar-first fallback\"；分析 fallback 级联行为。\n\n**N3** [critical] WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力严重不足\n- §5.4, Table 5, Limitations (page 9)\n- 20 篇文档上 bootstrap p-values 不可靠，置信区间极宽，但 Table 5 与 SciERC/DocRED 并列暗示同等可信度。\n- 建议：正文中明确标注规模限制，报告 95% bootstrap CI，考虑 cross-validation。\n\n### Should-Fix\n\n**W1** [warning] 缺少与最相关并发工作的直接实验对比\n- 未与 BoostCD、CRANE、IterGen、GCD 直接对比数字。\n\n**W2** [warning] 跨模型验证局限于 7-8B 参数规模\n- Abstract \"applies to any autoregressive LM\" 未加限定。\n\n**W3** [warning] 零样本 R-F1（0.08-8%）场景下 violation rate 分析的实际意义需要更明确讨论\n- 论文定位为 \"diagnostic\" 是恰当的，但表格中零样本和微调结果并排呈现可能误导读者。\n\n**W4** [warning] Entity registry 的顺序依赖可能导致 globally suboptimal type assignment\n- 贪心策略局部最优但全局次优，TCR 是事后修复而非生成时 exact enforcement。\n\n**W5** [warning] DocRED beam search 实验仅使用 50 文档子集\n- SciERC 用了完整 551 文档，DocRED 仅 50 文档。DocRED 文档更长、关系类型更多。\n\n### Minor\n- §4 Eq.(2) conjunction 是逐位 AND 应明确说明\n- CF 列含义首次出现时未充分解释\n- Figure 1 x 轴 label 不直观\n- Appendix G LoRA 3 epochs 是否充分\n- §6 末尾一段更像 contribution 声称\n\n### Questions\nQ1: Proposition 1 能否通过 pumping lemma 完整证明？schema 对 entity 数量设上限时是否仍成立？\nQ2: Grammar-first fallback 的级联行为——一次 fallback 的错误类型赋值是否触发更多 fallback？\nQ3: S2 的 DR 反而高于 S1——two-pass 是否引入额外错误来源？\nQ4: LoRA 统一超参数（r=16, α=32）是否做过敏感性分析？\nQ5: 对称关系的 κ 计算是否低估了实际约束紧度？\n\n### Missing References\n1. BoostCD (Sakota et al., 2025) — 已引用但未实验对比\n2. GCD (Geng et al., 2023) — 应明确展示 baseline 数字\n3. Schema-RL (Lu et al., 2025) — bib 中未被引用"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-20T17:20:44.102858+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1315
}
```

</details>

---


### Assistant

_source line 1233 · 2026-05-20T17:20:46.753179+00:00_

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


## Round 86

## Round 86

2 recorded events


### User

_source line 1234 · 2026-05-20T17:20:49.304032+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference），Soundness 3.5/5，Excitement 3.5/5，Confidence 4/5。

三个 Must-Fix 问题：
1. Proposition 1 仅为 proof sketch，与 "formally compiles" 定位不匹配
2. "Exact enforcement" 声称与 36.64% CF fallback rate 矛盾
3. WikiEvents fine-tuning 仅 20 文档测试集，统计效力不足

五个 Should-Fix 问题涉及：缺少与 BoostCD/CRANE 的直接对比、跨模型验证局限于 7-8B 规模、零样本 R-F1 过低时 violation 分析的意义、entity registry 顺序依赖、DocRED beam search 仅 50 文档子集。

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

_source line 1235 · 2026-05-20T17:20:55.229351+00:00_

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


## Round 87

## Round 87

2 recorded events


### User

_source line 1236 · 2026-05-20T17:22:10.223826+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE with nuance] R2-N1: 语义层机制与 IterGen 的概念区分不充分**

同意论文应更深入对比 OntoCoDec vs. IterGen vs. PICARD 的机制差异。但我认为 R2 略低估了这三者之间的架构差异程度：

- **OntoCoDec (preventive masking)**：在每个 decoding step 预计算合法 token 集合，从源头阻止无效 token 生成——零回退开销，但约束表达力受限于 prefix-decidable 性质（仅 domain/range）。
- **IterGen (corrective backtracking)**：允许生成后检测违规并回退到 checkpoint——支持任意 semantic predicate，但需要 KV cache 管理和回退开销（Ugare et al., 2025 报告 backtracking 增加 15-40% latency）。
- **PICARD (incremental parsing monitor)**：在 text-to-SQL 场景中做 incremental validity check，丢弃无效 beam candidates——介于两者之间，但绑定于 SQL grammar，不处理本体约束。

论文确实应在 §6 或 Appendix B 中增加一个显式的机制对比表，清晰呈现 preventive vs. corrective 的 trade-off（约束表达力 vs. 效率开销）。但我不认为这上升到 "critical" 级别——核心机制差异（masking vs. backtracking）在领域内是公认的不同设计范式，不存在 novelty 混淆的风险。建议降级为 Should-Fix。

**[AGREE] R2-N2: κ̄ 作为 Contribution 2 被过度声称**

完全同意。论文在 Appendix C 自身承认 κ̄ 的 Kruskal-Wallis 检验 df=2、p>0.05，未通过确认性统计检验。在此前提下，将 κ̄ 定位为 "analytical linking framework"（Abstract）并列为独立贡献（Contribution 2）确实属于过度声称。

我在自己的审稿中也注意到了这一点：κ 与 DR reduction 的 Pearson 相关 r=0.886（Figure 2/Appendix C）是有价值的描述性发现，但不能上升为 "analytical framework"。R2 的建议——降级为 "descriptive metric that correlates with enforcement outcomes"——是准确的修改方向。

---

### Should-Fix

**[AGREE] R2-W1: 无直接实验对比 BoostCD**

与我自己的 W1 一致。BoostCD (Sakota et al., 2025) 在 SciERC 上做了 grammar-constrained IE，是最直接的竞争方法。缺乏 head-to-head 数字对比是两位 reviewer 共同识别的问题。

**[AGREE with nuance] R2-W2: "Ontology-agnostic" 声称实验支撑不充分**

R2 指出仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 的 schema 来自经验统计。这个观察是准确的。但我认为需要区分两个层面：
1. **编译机制的 agnosticism**：OntoCoDec 的编译流程（schema → grammar + semantic masks）确实不依赖本体来源——无论 schema 来自 KAIROS ontology 还是训练集统计，编译过程相同。这一点有充分支撑。
2. **"Ontology" 一词的准确性**：SciERC/DocRED 的 schema 本质上是 type inventory + domain/range mapping，不是完整的本体（无 subsumption hierarchy、无 axioms）。论文标题用 "Schema Constraints" 而非 "Ontology Constraints" 是恰当的，但正文中 "ontology-agnostic" 的表述确实应改为 "schema-agnostic"。

**[REBUT] R2-W3: 正文 Related Work 过于压缩**

不完全同意。对于 long paper（8 页正文），将核心对比放在 §6 约 15 行、详细讨论放在 Appendix B 4 页是合理的空间分配策略。§6 正文覆盖了三个关键维度（grammar-constrained decoding、schema-guided IE、ontology-constrained generation），并引用了 20+ 篇文献。关键定位信息（与 GCD、PICARD、GoLLIE 等的区分）在正文中可获取。

但我同意 R2 的 N1——§6 中对 IterGen 的讨论不够深入。建议在正文 §6 中增加与 IterGen 的显式机制对比（2-3 行即可），而不需要将整个 Appendix B 搬入正文。

**[AGREE] R2-W4: Abstract 信息密度过高**

同意。Abstract 试图在一段中塞入可判定性分类、三层架构、κ 指标、跨模型/跨数据集数字、beam search 结果、fine-tuning composability，关键 message 被淹没。建议 Abstract 聚焦于核心 message（可判定性引导的约束分层 + grammar-first fallback）和最重要的 1-2 个数字（如 DR reduction 幅度），将细节推到 Introduction。

**[AGREE] R2-W5: 模型规模 hedging 不充分**

与我自己的 W2 一致。

**[AGREE] R2-W6: CF 代价在 Abstract/Contribution 中不够透明**

与我自己的 N2 一致且互补。R2 的 W6 从写作透明度角度提出，我的 N2 从技术声称准确性角度提出。两者共同指向一个问题：论文在最显眼的位置（Abstract、Contributions）对 CF trade-off 的呈现不充分。Grammar-first fallback rate 36.64%（SciERC）这个数字应在 Abstract 或 §1 Contributions 中被提及，而非仅出现在 Appendix C Table 8。

---

### Minor

**[AGREE] R2-M1**: 10 orphan bib entries，与我的观察一致。

**[AGREE] R2-M2**: 重复 bib key，与我的观察一致。

**[AGREE] R2-M3**: S1/S2 命名确实初读易混淆。S1 = single-pass (grammar+semantic), S2 = two-pass sequential——但 "S1" 容易被读为 "Stage 1" 或 "Semantic layer 1"。建议改为更具描述性的缩写（如 JOINT vs. SEQ）。

**[AGREE] R2-M4**: Table 5 "—" 标记确实缺少表注说明。

**[REBUT] R2-M5**: Beam search seed 信息。论文 Appendix G 明确报告了 seed 验证："We verify this with three seeds (42, 123, 456) across two LoRA fine-tuned models on all 551 SciERC documents"，并指出 "Argmax is deterministic; the random seed controls torch.cuda.manual_seed for sampling and dropout, neither of which is active during greedy inference"。Beam search (k>1) 同样是确定性的（给定相同模型状态），不依赖随机 seed。这一点在 Appendix G 中已充分说明。

---

### Questions 评论

**R2-Q1**（扩展到 cardinality/temporal ordering）：好问题，直接关联 Level 3 non-local 约束的未来方向。这也呼应了我在 W4 中关于 entity registry 顺序依赖的讨论——cardinality constraints（"至少 N 个某类 entity"）和 temporal ordering 本质上都是 non-local 的，论文的框架目前无法在解码时精确处理。

**R2-Q2**（COMPARE 关系 κ=0.528 未完全消除 DR）：有价值的 diagnostic 问题。结合 Appendix N Table 35 的 case study，COMPARE 关系的 domain/range 允许多种 entity type pair，κ 值中等偏高意味着约束不够紧，部分 valid-by-schema-but-wrong-in-context 的 pair 无法被 Level 2 约束过滤。这实际上是 κ 指标的一个良好验证——它预测了约束效果的边界。

**R2-Q3**（DR 下降但 F1 仅提升 0.5pp）：非常敏锐的观察。这暗示被消除的 violations 大多出现在已经错误的输出中（即模型提取了错误的 triple，约束修正了其类型但 triple 本身仍是错的）。这进一步支持了我的 W3——零样本/低 F1 场景下 violation rate 分析的实际价值有限。

**R2-Q4**（S1 模式下 registry 为空时的处理）：这涉及 §3.3 的 entity registry 初始化逻辑。在 OntoCoDec 的 schema 中，entities 在 relations 之前生成（top-level ordering），因此 registry 在 relation generation 开始前已被填充。但如果模型在第一个 entity 生成时 registry 为空，语义层应退化为 grammar-only（所有 entity types 均合法）。论文应在 §3.3 中显式说明这一边界条件。

---

### Missing References 评论

**[AGREE] Koldehoff et al. (Frontiers in AI, 2025)**：如果该工作确实将 grammar-constrained decoding + 本体约束应用于临床试验 IE，与 OntoCoDec 的方法论相关性很高，应在 §6 或 Appendix B 中讨论。

**[AGREE] Schema RL (Lu et al., ACL 2025)**：在 bib 中存在（lu2025schemarl）但未被引用。作为 training-based structured output 方法，可作为 §6 中 training-based vs. decoding-time 对比的参照点。

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

_source line 1237 · 2026-05-20T17:22:19.297985+00:00_

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


## Round 88

## Round 88

2 recorded events


### User

_source line 1238 · 2026-05-20T17:22:21.777142+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2 的 2 个 Must-Fix**：N1（IterGen 区分）我同意需加强但建议降级为 Should-Fix（preventive vs. corrective 是公认不同范式）；N2（κ̄ 过度声称）完全同意。
- **R2 的 6 个 Should-Fix**：W1/W4/W5/W6 均同意，与我自己的发现一致或互补；W2 部分同意（编译机制确实 agnostic，但"ontology"用词不准确）；W3 反驳（RW 空间分配合理，但 IterGen 讨论需加深）。
- **5 个 Minor**：M1-M4 同意，M5 反驳（beam search 是确定性的，seed 信息已在 Appendix G 充分说明）。

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

_source line 1239 · 2026-05-20T17:22:31.496625+00:00_

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


## Round 89

## Round 89

10 recorded events


### User

_source line 1240 · 2026-05-20T17:24:44.616665+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 回应

### [REBUT] R1-N1: Proposition 1 证明不严格

R1 的批评混淆了两个不同的概念。R1 要求 "(a) 到已知不可判定性结果的形式化归约"——但 Proposition 1 声称的是 **non-context-freeness**（Level 2 ⊄ Level 1），不是 undecidability。这两者的证明方法完全不同：non-CF 通常用 pumping lemma 或闭包性质，而非不可判定性归约。R1 混淆了 Chomsky 层级中的"不属于 CFL"和"不可判定"，前者是 Proposition 1 的实际声称。

关于证明本身：§3.1（p3）的 proof sketch 使用 PDA stack 论证——当实体集无界时，识别合法的类型约束输出需要在任意位置间维护 entity-type binding，这超出了 PDA 的能力（pushdown automaton 只有一个 stack，无法同时追踪无界数量的 entity-type 对应关系）。这个论证的核心机制与经典的 {a^n b^n c^n ∉ CFL} 结果同构，在形式语言理论中是标准的。

不过我**部分同意** R1 的关切：论文将此定位为核心贡献之一（"decidability-guided constraint classification"），那么形式化水平应与声称力度匹配。当前的 proof sketch 对于经验性 NLP 论文是可接受的，但对于声称"形式化分类"的贡献来说偏弱。

**建议**：在附录中补充完整的 pumping lemma 证明（约半页），或将 contribution 表述从 "formal classification" 降级为 "a classification motivated by formal language-theoretic observations"。但 R1 要求的"不可判定性归约"是不恰当的——Proposition 1 的目标不是证明不可判定性。

---

### [AGREE] R1-N2: "Exact enforcement" 声称与 CF fallback 的矛盾

R1 的观察精确且有力。§3.3（p3）使用 "exact pair-based enforcement"，但 §4（p4）的 grammar-first fallback 机制意味着当 S(t)∩G(t)=∅ 时语义约束被完全放弃。Table 8（Appendix C, p21）证实 SciERC 上 245 个 CF violations 中 GENERIC 实体类型占 63.3%（155/245），总共 345 个冲突 type pairs。这不是边缘情况。

**R1 关于级联失败的追问特别重要**：我验证了 §3.3（p3）的 entity registry 设计——registry 在生成过程中增量填充（"each completed entity (n_i, τ_i) adds (n_i, τ_i) to P"）。因此，一次 fallback 导致的错误类型赋值**确实**会写入 registry，影响后续所有涉及该实体的 relation 的 domain/range 检查。论文未分析这种级联效应。

补充一个数据点：Table 9（p21）显示 per-relation DR elimination 在 EVALUATE-FOR（κ=0.361）上完全成功但在 COMPARE（κ=0.528, 5.00%）上仍有残留——这可能部分归因于 fallback 级联：COMPARE 涉及更多 ambiguous entity types（Table 8 的 GENERIC→Metric 和 GENERIC→Method 各占 12.2% 和 6.9% 的 CF），而 fallback 后的错误类型可能导致后续 DR 无法消除。

**建议**：同意 R1——将 "exact" 改为 "best-effort" 或 "targeted"，并增加 fallback 级联分析。这是一个 must-fix 级别的术语校准问题。

---

### [AGREE] R1-N3: WikiEvents fine-tuning 20 文档测试集统计效力不足

**部分同意，但需要校正 R1 的指向范围。**

Table 5（p7）标题明确区分了两种评估：zero-shot 使用 **完整 246 文档**；fine-tuning 使用 **194/20/20 split**（20 文档测试集）。WikiEvents 的主要验证是 zero-shot（246 docs），不是 fine-tuning。R1 的批评对 fine-tuning 行完全成立——20 文档上的 bootstrap 统计确实不可靠——但不应否定 zero-shot 行（246 docs）的有效性。

然而，Table 5 确实将两种设定的结果**并列呈现**，且未在表格内部标注样本量差异。这使得读者可能将 20-doc fine-tuning 结果的可信度等同于 246-doc zero-shot 结果。

**建议**：(1) Table 5 内标注测试集大小（n=246 / n=20）；(2) fine-tuning 行报告 95% bootstrap CI；(3) 在正文中明确指出 fine-tuning 评估是 **preliminary** 的，主要验证是 zero-shot 设定。这样既保留了有用信息，又不误导读者。

---

## Should-Fix 回应

### [AGREE] R1-W1: 缺少与 BoostCD/CRANE/IterGen/GCD 的直接实验对比

与我的 W1 一致。BoostCD（Sakota et al., 2025）在 SciERC 和 DocRED 上有结果，是最直接的对比对象。即使 setting 不完全相同（BoostCD 的 boosting 策略 vs. OntoCoDec 的确定性约束），同一数据集上的数字对比对审稿人判断边际贡献至关重要。

---

### [AGREE] R1-W2: 模型规模限于 7-8B，Abstract 声称 "any autoregressive LM" 未加限定

与我的 W5 一致。Abstract（p1）说 "applies to any autoregressive LM across four models (8B-70B)"——但实际测试的模型参数量范围仅为 7B-8B（Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-8B）。"8B-70B" 的表述来自何处不明——可能是计划中的实验但未执行？正文中应删除或修正此声称。

---

### [REBUT] R1-W3: 零样本 R-F1（0.08-8%）场景下违规率分析的实际意义

R1 认为在极低 R-F1 下分析违规率实际意义存疑。我**不完全同意**。

论文明确将零样本设定定位为 **diagnostic**（§5, p5: "Zero-shot evaluation (§5.1-§5.3) isolates layer contributions as a diagnostic"）。违规率分析的价值独立于任务性能：它揭示 LLM 在无任务特定训练时的**结构输出模式**——哪些类型的约束违规最频繁、违规与 schema 属性（κ̄）的关系等。这些 insight 对理解 LLM 的本体感知能力有独立价值，不因 R-F1 低而失效。

类比：分析一个未经训练的代码 LLM 生成代码的 type errors 分布，即使代码无法编译运行，对理解模型的类型系统感知能力仍有诊断意义。

**但我同意一点**：Table 1（p5）中 zero-shot 和 fine-tuned 结果并排呈现，可能使读者对零样本结果的实用性产生过高预期。建议在 Table 1 中增加视觉分隔（如水平线）或在 caption 中强调诊断性质。

---

### [AGREE] R1-W4: Entity registry 顺序依赖导致全局次优类型赋值

这是一个有洞察力的观察。§3.3（p3）的 entity registry 按生成顺序增量填充，第一次出现的 entity 的类型赋值锁定所有后续引用。如果一个 entity 在第一个 triple 中被赋予次优类型（因为第一个 triple 的 relation 对该 entity type 的约束较宽松），后续更紧约束的 relation 就无法修正。

§3.4（p4）提到的 TCR（Type Consistency Repair）是事后修复（beam search 或 post-hoc re-scoring），不是生成时的 exact enforcement——这进一步支持 R1-N2 的 "exact" 术语批评。

补充证据：Table 10（Appendix D, p21）的 four-way ablation 显示 "Semantic layer is the sole effective DR defense, providing 39-69% reduction"——但这个 reduction 的上限可能受限于顺序依赖导致的次优赋值。如果 entity registry 能全局优化（如 ILP），DR reduction 可能更高。这是论文未讨论的理论上限。

---

### [AGREE] R1-W5: DocRED beam search 仅 50 文档子集

Table 15（Appendix E, p24）确认 DocRED beam search 在 "matched 50-document subsets" 上评估。DocRED 有 96 个 relation types（vs. SciERC 的 7 个），50 文档可能无法覆盖足够多的 relation types 来验证 beam search 的普适效果。

Appendix E 解释了原因："~300h due to extended generation under high-temperature sampling with complex schemas"——这是合理的计算资源限制，但应在正文中标注，并讨论子集代表性（如覆盖的 relation type 比例）。

---

## Minor 回应

- **Eq.(2) conjunction 是逐位 AND**：[AGREE] §4（p4）Eq. 2 的 M_final(t) = M_grammar(t) ∧ M_semantic(t) 确实是逐 token 的逐位 AND，应在正文中明确说明"element-wise conjunction over the vocabulary"。

- **CF 列含义首次出现时未充分解释**：[AGREE] Table 1（p5）首次引入 CF 列时，caption 仅说 "CF = cross-field consistency violations"，但 CF 的具体含义（同一 entity 在不同 triple 中被赋予不同类型）需要回溯到 §2（p2）才能理解。建议在 Table 1 caption 中增加一句解释。

- **Figure 1 (Appendix C, p20) x 轴 label 不直观**：[AGREE] x 轴是 κ × RV_baseline 的乘积，物理含义不直观。建议增加轴标签注释。

- **Appendix G LoRA 3 epochs 是否充分**：[REBUT] 3 epochs 是 LoRA fine-tuning 的常见设定（Hu et al., 2022 原始论文使用 3-5 epochs）。Appendix G（p26-27）报告了 completion-only loss，且 SciERC 有 1,762 训练样本、DocRED 有 3,053 样本，3 epochs 下梯度更新分别为 333/573 steps（batch size 16, gradient accumulation 4），对于 LoRA rank=16 的小参数量是合理的。若 R1 怀疑 underfitting，应指出具体证据（如 training loss 未收敛）。

- **§6 末尾一段更像 contribution 声称**：[AGREE] §6（p8）最后一段确实从 related work positioning 滑向了 contribution recapping，建议修改为更明确的 differentiation 表述。

---

## R1 Questions 评价

**Q1（Pumping lemma + 有界 entity 数量）**：好问题。如果 schema 对 entity 数量设上限 k，则有效输出集变为有限语言（有限语言都是正则的，因此也是 CF 的）。Proposition 1 的 "unbounded" 前提至关重要——论文应讨论 bounded entity set 的退化情况。

**Q2（Fallback 级联行为）**：最关键的问题，与 N2 直接相关。如上分析，级联确实可能发生。

**Q3（S2 的 DR 高于 S1）**：有价值。Table 1 显示 S2 在某些配置下 DR 确实高于 S1。可能原因：two-pass 的第一次 pass 提取的 entity 集合不完全，导致第二次 pass 的 registry 缺失部分 entity，fallback 更频繁。

**Q4（LoRA 超参数敏感性）**：合理关切，但优先级低于 N1-N3。

**Q5（对称关系 κ 计算）**：技术上有趣。对称关系的 head/tail type set 相同，κ_head = κ_tail，但 §4 脚注 1（p4）已说明"we evaluate on directed triples"——因此对称关系的 κ 不存在 head/tail 不对称导致的低估问题。但 R1 可能在问更细微的点：对称关系是否使得有效类型对比非对称关系更多（因为 head 和 tail 可互换），从而 κ 低估了 constraint 的实际宽松度。这值得作者回应。

---

## 综合评价

R1 的审稿在方法严谨性维度上非常深入。N2（"exact" vs fallback 矛盾 + 级联失败）和 W4（顺序依赖全局次优）是本轮审稿中最有技术深度的发现，两者联合起来构成了对论文核心声称的实质性挑战。N1 的方向正确但论证有误（混淆了 non-CF 与 undecidability）。N3 的范围应限定在 fine-tuning 行（20 docs）而非全部 WikiEvents 结果（246 docs）。

两位 Reviewer 的共识问题：(1) 缺少与 BoostCD 的直接实验对比（R1-W1, R2-W1）；(2) 模型规模声称过宽（R1-W2, R2-W5）；(3) κ̄/形式化贡献的声称力度与证据不匹配（R1-N1, R2-N2）。


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

_source line 1241 · 2026-05-20T17:25:09.963311+00:00_

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

_source line 1242 · 2026-05-20T17:25:10.114734+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T17:08:47.374469+00:00\", \"completed_at\": \"2026-05-20T17:11:55.955914+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-4\", \"message\": \"主文前4页无任何display item（figure/table），审稿人打开论文后连续翻过4页纯文本+公式才在第5页见到首个Table。对于提出框架（OntoCoDec）的系统论文，缺少架构概览图/流程图是严重的第一印象缺陷。审稿人在前2分钟内无法通过视觉锚点快速理解方法核心。\"}, {\"severity\": \"critical\", \"dimension\": \"page 1-9\", \"message\": \"主文（8页正文）零Figure。全文仅有的3个Figure（Figure 1/2/3）全部放在附录（page 20/23/25）。这对系统/方法论文极不寻常——审稿人期望至少在Method部分看到一张框架图展示grammar layer + semantic layer的两层架构、约束编译流程、或解码时masking的工作方式。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-4\", \"message\": \"连续4页纯文本+数学公式无视觉打断。虽然Section 3包含Proposition/Proof/Corollary等形式化内容（属于理论密集段），但整个Method部分无任何图解辅助理解，阅读负担极重。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5-7\", \"message\": \"主文display items全部为表格（Table 1-5），无任何可视化图表。5个表格集中在3页内（page 5: 1个, page 6: 2个, page 7: 2个），且均为消融/对比数值表。缺乏趋势图、分布图等帮助审稿人直观感受方法优势的可视化。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Section 6 Related Work + Section 7 Discussion and Conclusion挤在同一页，Related Work仅约半栏篇幅，显得过于压缩。\"}, {\"severity\": \"warning\", \"dimension\": \"page 15-17\", \"message\": \"附录Extended Related Work连续3页纯文本，无任何display item穿插，阅读节奏单调。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（首个display item）是五路消融表，传达的是组件贡献而非方法核心思想。作为审稿人第一个看到的数据展示，不如一张展示方法整体效果的overview figure有锚定力。\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figure 1（Residual DR vs κ·RV scatter plot）质量可接受，线性拟合清晰，但仅4个数据点，视觉说服力有限。Caption自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"Figure 2（per-relation DR bar chart）清晰可读，颜色区分度足够。但作为附录图，审稿人可能不会看到。\"}, {\"severity\": \"info\", \"dimension\": \"page 25\", \"message\": \"Figure 3（beam width vs R-F1 multi-panel scatter+bubble）信息密度高，但图内文字偏小（legend/axis labels），150dpi下勉强可读。建议放大字号或简化面板。\"}, {\"severity\": \
…[truncated 759 chars]

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


### Tool call

_source line 1243 · 2026-05-20T17:25:10.115257+00:00_

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

_source line 1244 · 2026-05-20T17:25:10.165839+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1245 · 2026-05-20T17:30:11.112098+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 12 fresh review (2026-05-20)\n\n# ============================================================\n# Round 12 Must-Fix\n# ============================================================\n\n- id: \"R12-MF1\"\n  summary: \"'Exact enforcement' 声称与 36.64% CF fallback rate 矛盾 + 级联失败未分析\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 raised, R2 AGREE with reinforcing evidence (Table 8 GENERIC 63.3%, fallback 写入 registry 导致级联)。Full consensus。§3.3 'exact pair-based enforcement' vs §4 grammar-first fallback。\"\n  action_items:\n    - round: 12\n      action: \"将 'exact' 改为 'best-effort' 或 'targeted pair-based enforcement with grammar-first fallback'；分析 fallback 级联行为并量化；在 Abstract/§1 中披露 fallback rate。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-MF2\"\n  summary: \"κ̄ 作为 Contribution 2 ('analytical linking framework') 被过度声称\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N2 raised, R1 fully AGREE。Appendix C 自承 'descriptive characterization' (df=2, p>0.05)，但 Abstract + Contribution 2 仍称 'analytical linking framework'。\"\n  action_items:\n    - round: 12\n      action: \"Contribution 2 降级为 'descriptive metric correlating with enforcement outcomes'；Abstract 相应调整；去掉 'analytical framework' 措辞。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-MF3\"\n  summary: \"Proposition 1 仅为 proof sketch，与 'formally compiles' 定位不匹配\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N1 raised (要求完整证明)。R2 REBUT 指出 R1 混淆了 non-CF 与 undecidability，但同意 proof sketch 对 'formal' 声称偏弱。部分共识：证明方向正确但需加强。\"\n  action_items:\n    - round: 12\n      action: \"二选一：(A) 附录补充完整 pumping lemma 证明（~半页）；(B) 将 contribution 从 'formal classification' 降级为 'classification motivated by formal language-theoretic observations'。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-MF4\"\n  summary: \"WikiEvents fine-tuning 仅 20 文档测试集，统计效力不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 raised。R2 部分 AGREE——限定于 fine-tuning 行（20 docs），zero-shot 行（246 docs）有效。Table 5 并列呈现未标注样本量差异。\"\n  action_items:\n    - round: 12\n      action: \"Table 5 内标注测试集大小（n=246/n=20）；fine-tuning 行报告 95% bootstrap CI；正文明确 fine-tuning 评估为 preliminary。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 12 Should-Fix\n# ============================================================\n\n- id: \"R12-SF1\"\n  summary: \"语义层核心机制与 IterGen/PICARD 的概念区分不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N1 raised as Must-Fix。R1 AGREE 需加强但建议降级为 Should-Fix（preventive vs corrective 是公认不同范式）。导致降级。\"\n  action_items:\n    - round: 12\n      action: \"§6 增加显式机制对比（OntoCoDec preventive masking vs IterGen corrective backtracking vs PICARD incremental parsing），2-3 行正文 + 可选对比表。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF2\"\n  summary: \"无直接实验对比最接近的 IE 基线 BoostCD\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1，full consensus。BoostCD (Sakota et al., 2025) 在 SciERC/DocRED 有结果。\"\n  action_items:\n    - round: 12\n      action: \"至少在 SciERC 上与 BoostCD 进行数字对比（引用其报告数字或运行实验），并讨论评估设置差异。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF3\"\n  summary: \"模型规模声称过宽——'any autoregressive LM' 但主要测试仅 7-8B\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W5，full consensus。70B (Llama-3.1-70B AWQ INT4) 在 §5.6 有简要评估，但 Abstract 'applies to any autoregressive LM' 未加限定。\"\n  action_items:\n    - round: 12\n      action: \"Abstract/§1 限定为 'validated on 7-8B models with preliminary 70B results'；§7 结论加 'across 7-8B parameter models' 限定词。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF4\"\n  summary: \"CF 代价在 Abstract/Contribution 中不够透明\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W6 raised, R1 AGREE（与 R1-N2 互补）。Grammar-first fallback rate 36.64% 仅出现在 Appendix C Table 8。\"\n  action_items:\n    - round: 12\n      action: \"Abstract 增加 CF trade-off 说明（如 'with modest CF costs resolvable via beam search'）；§1 Contributions 中披露 fallback rate。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF5\"\n  summary: \"Abstract 信息密度过高，关键 message 被数字淹没\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W4 raised, R1 AGREE。Abstract 试图塞入全部维度的数字，核心 message 被遮蔽。\"\n  action_items:\n    - round: 12\n      action: \"Abstract 保留 1-2 个最关键数字（DR 减少幅度 + R-F1 稳定），其余推至 Introduction。聚焦 conceptual framing。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF6\"\n  summary: \"Entity registry 顺序依赖导致全局次优类型赋值\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W4 raised, R2 AGREE with reinforcing evidence（Table 10, 39-69% reduction upper bound 受限于顺序依赖）。贪心赋值 + TCR 事后修复与 'exact enforcement' 矛盾。\"\n  action_items:\n    - round: 12\n      action: \"§3.3 或 §4 讨论贪心赋值的局限性，将其定位为 Level 3 non-local 约束的实例；讨论理论上限。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF7\"\n  summary: \"'Ontology-agnostic' 应改为 'schema-agnostic'，实验支撑不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W2 raised, R1 部分 AGREE（编译机制确实 agnostic，但 'ontology' 用词不准确）。仅 WikiEvents 使用正式本体。\"\n  action_items:\n    - round: 12\n      action: \"将 'ontology-agnostic' 改为 'applicable to both formal ontologies and empirically-derived type constraints'；Limitations 中标注仅一个正式本体验证。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF8\"\n  summary: \"DocRED beam search 仅 50 文档子集\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W5 raised, R2 AGREE。SciERC 用完整 551 docs, DocRED 仅 50 docs。96 relation types 可能未充分覆盖。Appendix E 解释了计算资源限制。\"\n  action_items:\n    - round: 12\n      action: \"正文标注子集规模限制；报告子集覆盖的 relation type 比例；或扩展到更大子集。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 12 Minor\n# ============================================================\n\n- id: \"R12-M1\"\n  summary: \"BibTeX 清理：10 orphan entries + 1 duplicate key (schall2025hiddencost)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 + R2 均识别。包括 sakota2025boostcd/boostcd2025 重复、lee2026formattax/formattax2026 重复等。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M2\"\n  summary: \"S1/S2 命名与层级编号初读易混淆，建议改为 SP/TP 或 JOINT/SEQ\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-M3 raised, R1 AGREE。S1 容易被读为 'Stage 1' 或 'Semantic layer 1'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M3\"\n  summary: \"Table 5 WikiEvents '—' 标记缺少表注解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-M4 raised, R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M4\"\n  summary: \"§4 Eq.(2) conjunction 应明确为 element-wise AND over vocabulary\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"R1 raised, R2 AGREE in cross-response。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M5\"\n  summary: \"CF 列含义首次出现（Table 1）时解释不足，需回溯 §2\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 minor + R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M6\"\n  summary: \"Figure 1 (Appendix C) x 轴 'κ·RV_baseline' 物理含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M7\"\n  summary: \"§6 末尾一段从 related work positioning 滑向 contribution recapping\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M8\"\n  summary: \"Schema RL (Lu et al., ACL 2025) 存在于 bib 但未被引用\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"应在 §6 training-based vs decoding-time 对比中引用。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 12 Divergence\n# ============================================================\n\n- id: \"R12-DIV1\"\n  summary: \"Related Work 压缩度：R1 认为合理（REBUT R2-W3），R2 认为过于压缩\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3: 正文 §6 仅 15 行，实质讨论全在 Appendix B。R1 REBUT: 8 页限制下空间分配合理，但同意 IterGen 讨论需加深。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-DIV2\"\n  summary: \"零样本 R-F1 极低时 violation rate 分析的实际意义\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W3: 零样本 R-F1 2-8% 接近噪声，violation rate 分析价值有限。R2 REBUT: diagnostic 价值独立于 R-F1，揭示 LLM 结构输出模式。双方各有道理。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 — carried forward (open)\n# ============================================================\n\n- id: \"R11-DIV1\"\n  summary: \"技术新颖性评估分歧：R11 中 R1 (3/5) vs R2 (2.5/5)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: grammar 层复用 XGrammar，semantic 层是字典查找+条件masking。R1 反驳：sequential pair-based enforcement、enabling dependency 形式化、continuation masking 跨 tokenizer 方案超越纯工程。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"本轮两位 Reviewer 均给出 Excitement 3-3.5/5，R12-SF1 聚焦于 IterGen/PICARD 区分。新颖性仍是核心分歧点但两位 Reviewer 评分趋近。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved (preserved for history)\n# ============================================================\n\n- id: \"R11-MF1\"\n  summary: \"'Near-lossless' 叙事未充分呈现 CF trade-off — Abstract/Intro 需重构\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"R11 Paper Agent 完成 two-tier narrative 重构。grep 确认 near-lossless = 0 matches。\"\n  resolution_round: 11\n\n- id: \"R11-MF2\"\n  summary: \"缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"d063 GoLLIE 实验完成。§6 已加 qualitative positioning。\"\n  resolution_round: 11\n\n- id: \"R11-SF1\"\n  summary: \"Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§4 措辞已弱化，明确标注 n=4 和 descriptive。\"\n  resolution_round: 11\n\n- id: \"R11-SF2\"\n  summary: \"WikiEvents 'preliminary' 限定不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract + §5.4 已加 preliminary 限定。\"\n  resolution_round: 11\n\n- id: \"R11-SF3\"\n  summary: \"Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§5 framing paragraph 明确 ZS=diagnostic, FT=deployment。\"\n  resolution_round: 11\n\n- id: \"R11-SF4\"\n  summary: \"Beam search DocRED 仅 50-doc subset，推广性受限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"d064 完成 998-doc beam-4 结果入稿。但 R12 发现附录中仍有 50-doc 子集结果（非 LoRA），R12-SF8 追踪。\"\n  resolution_round: 12\n\n- id: \"R11-SF5\"\n  summary: \"Abstract 数字密度过高（~15 个数字）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Two-tier 重写后 ~7 numbers。但 R12 再次标记密度仍偏高（R12-SF5）。\"\n  resolution_round: 11\n\n- id: \"R11-SF6\"\n  summary: \"Entity registry 字段顺序依赖未显式讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"§3 Output Format 段落已加说明。但 R12 发现更深层的全局次优赋值问题（R12-SF6）。\"\n  resolution_round: 11\n\n- id: \"R10-MF1\"\n  summary: \"'Ontology Constraints' framing mismatch → 'Schema Constraints'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Title 已更新为 'Compiled Schema Constraints'。\"\n  resolution_round: 11\n\n- id: \"R10-MF2\"\n  summary: \"缺少 ARR Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"checklist.tex 已添加。\"\n  resolution_round: 11\n\n- id: \"R10-MF3\"\n  summary: \"WikiEvents EE 'preliminary' overweighted\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Contribution 4→3 合并。Abstract + §5.4 已加 preliminary 限定。\"\n  resolution_round: 11\n"
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
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 12 fresh review (2026-05-20)\n\n# ============================================================\n# Round 12 Must-Fix\n# ============================================================\n\n- id: \"R12-MF1\"\n  summary: \"'Exact enforcement' 声称与 36.64% CF fallback rate 矛盾 + 级联失败未分析\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 raised, R2 AGREE with reinforcing evidence (Table 8 GENERIC 63.3%, fallback 写入 registry 导致级联)。Full consensus。§3.3 'exact pair-based enforcement' vs §4 grammar-first fallback。\"\n  action_items:\n    - round: 12\n      action: \"将 'exact' 改为 'best-effort' 或 'targeted pair-based enforcement with grammar-first fallback'；分析 fallback 级联行为并量化；在 Abstract/§1 中披露 fallback rate。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-MF2\"\n  summary: \"κ̄ 作为 Contribution 2 ('analytical linking framework') 被过度声称\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N2 raised, R1 fully AGREE。Appendix C 自承 'descriptive characterization' (df=2, p>0.05)，但 Abstract + Contribution 2 仍称 'analytical linking framework'。\"\n  action_items:\n    - round: 12\n      action: \"Contribution 2 降级为 'descriptive metric correlating with enforcement outcomes'；Abstract 相应调整；去掉 'analytical framework' 措辞。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-MF3\"\n  summary: \"Proposition 1 仅为 proof sketch，与 'formally compiles' 定位不匹配\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N1 raised (要求完整证明)。R2 REBUT 指出 R1 混淆了 non-CF 与 undecidability，但同意 proof sketch 对 'formal' 声称偏弱。部分共识：证明方向正确但需加强。\"\n  action_items:\n    - round: 12\n      action: \"二选一：(A) 附录补充完整 pumping lemma 证明（~半页）；(B) 将 contribution 从 'formal classification' 降级为 'classification motivated by formal language-theoretic observations'。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-MF4\"\n  summary: \"WikiEvents fine-tuning 仅 20 文档测试集，统计效力不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 raised。R2 部分 AGREE——限定于 fine-tuning 行（20 docs），zero-shot 行（246 docs）有效。Table 5 并列呈现未标注样本量差异。\"\n  action_items:\n    - round: 12\n      action: \"Table 5 内标注测试集大小（n=246/n=20）；fine-tuning 行报告 95% bootstrap CI；正文明确 fine-tuning 评估为 preliminary。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 12 Should-Fix\n# ============================================================\n\n- id: \"R12-SF1\"\n  summary: \"语义层核心机制与 IterGen/PICARD 的概念区分不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N1 raised as Must-Fix。R1 AGREE 需加强但建议降级为 Should-Fix（preventive vs corrective 是公认不同范式）。导致降级。\"\n  action_items:\n    - round: 12\n      action: \"§6 增加显式机制对比（OntoCoDec preventive masking vs IterGen corrective backtracking vs PICARD incremental parsing），2-3 行正文 + 可选对比表。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF2\"\n  summary: \"无直接实验对比最接近的 IE 基线 BoostCD\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1，full consensus。BoostCD (Sakota et al., 2025) 在 SciERC/DocRED 有结果。\"\n  action_items:\n    - round: 12\n      action: \"至少在 SciERC 上与 BoostCD 进行数字对比（引用其报告数字或运行实验），并讨论评估设置差异。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF3\"\n  summary: \"模型规模声称过宽——'any autoregressive LM' 但主要测试仅 7-8B\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W5，full consensus。70B (Llama-3.1-70B AWQ INT4) 在 §5.6 有简要评估，但 Abstract 'applies to any autoregressive LM' 未加限定。\"\n  action_items:\n    - round: 12\n      action: \"Abstract/§1 限定为 'validated on 7-8B models with preliminary 70B results'；§7 结论加 'across 7-8B parameter models' 限定词。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF4\"\n  summary: \"CF 代价在 Abstract/Contribution 中不够透明\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W6 raised, R1 AGREE（与 R1-N2 互补）。Grammar-first fallback rate 36.64% 仅出现在 Appendix C Table 8。\"\n  action_items:\n    - round: 12\n      action: \"Abstract 增加 CF trade-off 说明（如 'with modest CF costs resolvable via beam search'）；§1 Contributions 中披露 fallback rate。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF5\"\n  summary: \"Abstract 信息密度过高，关键 message 被数字淹没\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W4 raised, R1 AGREE。Abstract 试图塞入全部维度的数字，核心 message 被遮蔽。\"\n  action_items:\n    - round: 12\n      action: \"Abstract 保留 1-2 个最关键数字（DR 减少幅度 + R-F1 稳定），其余推至 Introduction。聚焦 conceptual framing。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF6\"\n  summary: \"Entity registry 顺序依赖导致全局次优类型赋值\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W4 raised, R2 AGREE with reinforcing evidence（Table 10, 39-69% reduction upper bound 受限于顺序依赖）。贪心赋值 + TCR 事后修复与 'exact enforcement' 矛盾。\"\n  action_items:\n    - round: 12\n      action: \"§3.3 或 §4 讨论贪心赋值的局限性，将其定位为 Level 3 non-local 约束的实例；讨论理论上限。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF7\"\n  summary: \"'Ontology-agnostic' 应改为 'schema-agnostic'，实验支撑不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W2 raised, R1 部分 AGREE（编译机制确实 agnostic，但 'ontology' 用词不准确）。仅 WikiEvents 使用正式本体。\"\n  action_items:\n    - round: 12\n      action: \"将 'ontology-agnostic' 改为 'applicable to both formal ontologies and empirically-derived type constraints'；Limitations 中标注仅一个正式本体验证。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-SF8\"\n  summary: \"DocRED beam search 仅 50 文档子集\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W5 raised, R2 AGREE。SciERC 用完整 551 docs, DocRED 仅 50 docs。96 relation types 可能未充分覆盖。Appendix E 解释了计算资源限制。\"\n  action_items:\n    - round: 12\n      action: \"正文标注子集规模限制；报告子集覆盖的 relation type 比例；或扩展到更大子集。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 12 Minor\n# ============================================================\n\n- id: \"R12-M1\"\n  summary: \"BibTeX 清理：10 orphan entries + 1 duplicate key (schall2025hiddencost)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 + R2 均识别。包括 sakota2025boostcd/boostcd2025 重复、lee2026formattax/formattax2026 重复等。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M2\"\n  summary: \"S1/S2 命名与层级编号初读易混淆，建议改为 SP/TP 或 JOINT/SEQ\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-M3 raised, R1 AGREE。S1 容易被读为 'Stage 1' 或 'Semantic layer 1'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M3\"\n  summary: \"Table 5 WikiEvents '—' 标记缺少表注解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-M4 raised, R1 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M4\"\n  summary: \"§4 Eq.(2) conjunction 应明确为 element-wise AND over vocabulary\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"R1 raised, R2 AGREE in cross-response。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M5\"\n  summary: \"CF 列含义首次出现（Table 1）时解释不足，需回溯 §2\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 minor + R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M6\"\n  summary: \"Figure 1 (Appendix C) x 轴 'κ·RV_baseline' 物理含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M7\"\n  summary: \"§6 末尾一段从 related work positioning 滑向 contribution recapping\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 AGREE。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-M8\"\n  summary: \"Schema RL (Lu et al., ACL 2025) 存在于 bib 但未被引用\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"应在 §6 training-based vs decoding-time 对比中引用。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 12 Divergence\n# ============================================================\n\n- id: \"R12-DIV1\"\n  summary: \"Related Work 压缩度：R1 认为合理（REBUT R2-W3），R2 认为过于压缩\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-W3: 正文 §6 仅 15 行，实质讨论全在 Appendix B。R1 REBUT: 8 页限制下空间分配合理，但同意 IterGen 讨论需加深。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-DIV2\"\n  summary: \"零样本 R-F1 极低时 violation rate 分析的实际意义\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W3: 零样本 R-F1 2-8% 接近噪声，violation rate 分析价值有限。R2 REBUT: diagnostic 价值独立于 R-F1，揭示 LLM 结构输出模式。双方各有道理。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 11 — carried forward (open)\n# ============================================================\n\n- id: \"R11-DIV1\"\n  summary: \"技术新颖性评估分歧：R11 中 R1 (3/5) vs R2 (2.5/5)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: grammar 层复用 XGrammar，semantic 层是字典查找+条件masking。R1 反驳：sequential pair-based enforcement、enabling dependency 形式化、continuation masking 跨 tokenizer 方案超越纯工程。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"本轮两位 Reviewer 均给出 Excitement 3-3.5/5，R12-SF1 聚焦于 IterGen/PICARD 区分。新颖性仍是核心分歧点但两位 Reviewer 评分趋近。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior rounds — resolved (preserved for history)\n# ============================================================\n\n- id: \"R11-MF1\"\n  summary: \"'Near-lossless' 叙事未充分呈现 CF trade-off — Abstract/Intro 需重构\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"R11 Paper Agent 完成 two-tier narrative 重构。grep 确认 near-lossless = 0 matches。\"\n  resolution_round: 11\n\n- id: \"R11-MF2\"\n  summary: \"缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"d063 GoLLIE 实验完成。§6 已加 qualitative positioning。\"\n  resolution_round: 11\n\n- id: \"R11-SF1\"\n  summary: \"Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§4 措辞已弱化，明确标注 n=4 和 descriptive。\"\n  resolution_round: 11\n\n- id: \"R11-SF2\"\n  summary: \"WikiEvents 'preliminary' 限定不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Abstract + §5.4 已加 preliminary 限定。\"\n  resolution_round: 11\n\n- id: \"R11-SF3\"\n  summary: \"Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§5 framing paragraph 明确 ZS=diagnostic, FT=deployment。\"\n  resolution_round: 11\n\n- id: \"R11-SF4\"\n  summary: \"Beam search DocRED 仅 50-doc subset，推广性受限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"d064 完成 998-doc beam-4 结果入稿。但 R12 发现附录中仍有 50-doc 子集结果（非 LoRA），R12-SF8 追踪。\"\n  resolution_round: 12\n\n- id: \"R11-SF5\"\n  summary: \"Abstract 数字密度过高（~15 个数字）\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Two-tier 重写后 ~7 numbers。但 R12 再次标记密度仍偏高（R12-SF5）。\"\n  resolution_round: 11\n\n- id: \"R11-SF6\"\n  summary: \"Entity registry 字段顺序依赖未显式讨论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"§3 Output Format 段落已加说明。但 R12 发现更深层的全局次优赋值问题（R12-SF6）。\"\n  resolution_round: 11\n\n- id: \"R10-MF1\"\n  summary: \"'Ontology Constraints' framing mismatch → 'Schema Constraints'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Title 已更新为 'Compiled Schema Constraints'。\"\n  resolution_round: 11\n\n- id: \"R10-MF2\"\n  summary: \"缺少 ARR Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"checklist.tex 已添加。\"\n  resolution_round: 11\n\n- id: \"R10-MF3\"\n  summary: \"WikiEvents EE 'preliminary' overweighted\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Contribution 4→3 合并。Abstract + §5.4 已加 preliminary 限定。\"\n  resolution_round: 11\n"
  }
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-20T17:30:11.163885+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 15253}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-20T17:33:14.375154+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ARR May 2026 | Deadline: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计 | R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\nOntoCoDec 将 IE 本体约束编译为双层 token-level 解码约束：语法层（XGrammar）保证 JSON 结构合法性和词汇成员关系；语义层通过运行时 entity registry + dynamic masking 强制 domain/range 类型兼容性。论文提出可判定性分类（context-free / prefix-decidable with state / non-local）指导约束分层设计，引入 constraint tightness κ̄ 描述 schema 限制性。在 SciERC（551 docs）、DocRED（998 docs）、WikiEvents（246 docs）三个数据集上使用 Qwen3-8B、Llama-3.1-8B、Mistral-7B（及 Llama-3.1-70B 简要评估）进行了系统的消融实验和 LoRA 微调组合性验证。\n\n---\n\n## Strengths\n\n**S1. 新颖的形式化视角。** 将 formal language theory 的可判定性分析引入 IE 约束解码，提出 context-free / prefix-decidable with state / non-local 的三层分类，为系统设计提供了有原则的指导。Proposition 1（Level 2 ⊄ Level 1）为双层架构的必要性提供了形式化论证基础。[R1+R2 共识]\n\n**S2. 全面且系统的实验设计。** 五路消融清晰隔离了 grammar 层和 semantic 层的贡献；跨模型（3+1 个）、跨数据集（3 个）、跨任务（RE + EE）的覆盖在 systems paper 中高于平均水平。四类违规分类法（DR/CF/RV/ET）允许精确理解每层约束的贡献和代价，远超同领域多数论文的二元 valid/invalid 评估。[R1+R2 共识]\n\n**S3. Fine-tuning composability 论证有价值。** Table 2 展示 LoRA + S1 在四个 model-dataset 组合上均实现 DR ≤ 0.09%、R-F1 ± 0.6pp。这回答了一个重要的部署问题——约束系统是否与参数优化兼容。Beam search (k=4) 进一步消除 SciERC 上全部四类违规。[R1+R2 共识]\n\n**S4. 诚实的局限性讨论。** Limitations section 明确承认 CF trade-off、模型规模限制、WikiEvents 样本量、评估仅限 LoRA 等问题。在投稿论文中这种坦诚度值得肯定。[R1+R2 共识]\n\n**S5. 实际工程价值。** 框架自动从任意 IE schema 编译约束，无需约束特定训练，可与任意自回归 LM 配合。Runtime overhead +10%（LoRA 配置），constraint compilation < 0.5s，scalability 到 200 entity types / 1000 relations 仅 2-3% overhead。即插即用的部署价值明确。[R1+R2 共识]\n\n**S6. 丰富的附录。** 22 页附录包含详尽的错误分析、scalability benchmarks、prompt 敏感性、document length 分析、TCR 机制、case studies。显著增强可复现性和可信度。[R1+R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（4 项，影响接收决定）\n\n**MF1. \"Exact enforcement\" 声称与 36.64% CF fallback rate 存在根本矛盾。** [R1-N2 raised, R2 AGREE — full consensus]\n\n§3.3 多处声称 \"exact pair-based enforcement\"，但 §4 的 grammar-first fallback 意味着当 S(t)∩G(t)=∅ 时语义约束被完全丢弃。Appendix C Table 8 显示 SciERC 上 fallback 在 36.64% 的 type-bearing positions 被触发，GENERIC 类型占 CF violations 的 63.3%（155/245）。更严重的是：fallback 导致的错误类型赋值会写入 entity registry，影响后续所有涉及该实体的 relation 的 domain/range 检查——论文未分析此级联失败效应。\n\n→ 修改建议：将 \"exact\" 改为 \"best-effort\" 或 \"targeted\"；分析并量化 fallback 级联行为；在 Abstract/§1 中披露 fallback rate。\n\n**MF2. κ̄ 作为 Contribution 2 (\"analytical linking framework\") 被过度声称。** [R2-N2 raised, R1 fully AGREE — full consensus]\n\nκ̄ 本质上是描述性统计量（|σ(r)|/|E|² 的归一化比例）。论文自身在 Appendix C 承认 \"descriptive characterization rather than a confirmatory statistical test\"（df=2, p>0.05），但 Abstract 和 Contribution 2 仍定位为 \"analytical linking framework\"，与论文自身的谨慎表述不一致。\n\n→ 修改建议：Contribution 2 降级为 \"a descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes and provides deployment guidance\"。\n\n**MF3. Proposition 1 仅为 proof sketch，与 \"formally compiles\" 定位不匹配。** [R1-N1 raised, R2 partially AGREE]\n\n论文将 \"decidability-guided constraint classification\" 定位为核心贡献之一，但 Proposition 1 仅给出 proof sketch。R2 指出 R1 原始批评中混淆了 non-context-freeness 与 undecidability（Proposition 1 声称的是 Level 2 ⊄ Level 1，应用 pumping lemma 而非不可判定性归约），但 R2 同意 proof sketch 对于声称 \"formal\" 的贡献偏弱。核心论证（PDA stack 无法追踪无界 entity-type binding）方向正确但需完整化。\n\n→ 修改建议：(A) 附录补充完整 pumping lemma 证明（~半页）；或 (B) 将 contribution 从 \"formal classification\" 降级为 \"classification motivated by formal language-theoretic observations\"。\n\n**MF4. WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力不足。** [R1-N3 raised, R2 partially AGREE]\n\nWikiEvents fine-tuning 使用 194/20/20 split，测试集仅 20 篇文档。R2 正确指出：零样本评估（246 docs）有效，问题限于 fine-tuning 行。但 Table 5 将两种设定并列呈现，未标注样本量差异，可能误导读者。正文 §5.4 的结论语气未相应降低。\n\n→ 修改建议：Table 5 内标注 n=246/n=20；fine-tuning 行报告 95% bootstrap CI；正文明确 fine-tuning 评估为 preliminary。\n\n### Should-Fix（8 项，影响评分但不一票否决）\n\n**SF1. 语义层核心机制与 IterGen/PICARD 的概念区分不充分。** [R2-N1 raised as Must-Fix, R1 AGREE substance but suggests Should-Fix — severity divergence]\n\nIterGen (Ugare et al., 2025) 同样在 grammar 层之上叠加语义约束（corrective backtracking）；PICARD (Scholak et al., 2021) 维护 incremental parsing monitor。论文在 §6 中未深入对比 preventive masking vs. corrective backtracking 的机制差异、效率特性和约束表达能力。R1 认为 masking vs. backtracking 是公认不同设计范式，novelty confusion 风险有限，建议降级。\n\n→ 修改建议：§6 增加显式机制对比（2-3 行 + 可选对比表），阐述 OntoCoDec 的 forward-only masking 效率优势及其约束表达力限制。\n\n**SF2. 无直接实验对比最接近的 IE 基线 BoostCD。** [R1-W1 + R2-W1, full consensus]\n\nBoostCD (Sakota et al., 2025) 同样在 SciERC/DocRED 上做 IE constrained decoding，是最直接的竞争方法。缺乏 head-to-head 数字对比使审稿人难以判断边际贡献。\n\n→ 修改建议：至少引用 BoostCD 报告的 SciERC 数字并讨论方法论差异；如代码可用，运行对比实验。\n\n**SF3. 模型规模声称过宽。** [R1-W2 + R2-W5, full consensus]\n\nAbstract \"applies to any autoregressive LM across four models (8B–70B)\" 实际上主要测试 7-8B 模型，70B (Llama-3.1-70B AWQ INT4) 仅在 §5.6 有简要零样本评估（无 fine-tuning composability）。注：两位 Reviewer 在交叉阶段均未注意到 70B 结果的存在（出现在 §5.6 \"Cross-scale generalizability\" 段，而非主要 cross-model table），说明该结果的呈现位置不够突出。\n\n→ 修改建议：Abstract/§1 限定为 \"validated primarily on 7-8B models with preliminary 70B results\"；将 70B 结果在正文中更突出地呈现。\n\n**SF4. CF 代价在 Abstract/Contribution 中不够透明。** [R2-W6 raised, R1 AGREE]\n\nGrammar-first fallback rate 36.64%（SciERC ZS）和 CF 上升（0.08→9.90%）仅出现在正文细节和 Appendix C，Abstract 轻描淡写 \"grammar-first fallback when constraints conflict\"。\n\n→ 修改建议：Abstract 增加 CF trade-off 说明。\n\n**SF5. Abstract 信息密度过高。** [R2-W4, R1 AGREE]\n\nAbstract 试图在一段中覆盖可判定性分类、三层架构、κ̄、跨模型数字、beam search、fine-tuning composability。核心 message（为什么 grammar 层不够、语义层如何补足）被数字细节遮蔽。\n\n→ 修改建议：保留 1-2 个关键数字，其余推至 Introduction。\n\n**SF6. Entity registry 顺序依赖导致全局次优类型赋值。** [R1-W4, R2 AGREE]\n\n贪心策略在第一次出现时锁定 entity 类型，后续更紧约束的 relation 无法修正。TCR (Appendix D) 是事后修复，不是生成时的 exact enforcement——进一步削弱 MF1 的 \"exact\" 声称。\n\n→ 修改建议：§3.3 或 §4 讨论贪心赋值局限性，定位为 Level 3 non-local 约束的实例。\n\n**SF7. \"Ontology-agnostic\" 声称实验支撑不足。** [R2-W2, R1 partially AGREE]\n\n仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 的 schema 来自训练数据经验统计。R1 指出编译机制确实不依赖来源，但 \"ontology\" 一词不准确。\n\n→ 修改建议：改为 \"applicable to both formal ontologies and empirically-derived type constraints\"。\n\n**SF8. DocRED beam search 仅 50 文档子集（零样本设定）。** [R1-W5, R2 AGREE]\n\nSciERC beam 用完整 551 docs，DocRED 零样本 beam 仅 50 docs。注：LoRA beam 已扩展到 998 docs（d064 实验），但零样本 beam 仍受限。\n\n→ 修改建议：标注子集规模限制并讨论代表性。\n\n### Minor（8 项）\n\n- **M1**: BibTeX 清理——10 orphan entries + 1 duplicate key (schall2025hiddencost) [R1+R2]\n- **M2**: S1/S2 命名与层级编号初读易混淆，建议改为 SP/TP 或 JOINT/SEQ [R2-M3, R1 AGREE]\n- **M3**: Table 5 \"—\" 标记缺少表注说明 [R2-M4, R1 AGREE]\n- **M4**: §4 Eq.(2) conjunction 应明确为 element-wise AND over vocabulary [R1]\n- **M5**: CF 列含义在 Table 1 首次出现时解释不足 [R1, R2 AGREE]\n- **M6**: Figure 1 (Appendix C) x 轴 \"κ·RV_baseline\" 物理含义不直观 [R1, R2 AGREE]\n- **M7**: §6 末尾一段从 related work positioning 滑向 contribution recapping [R1, R2 AGREE]\n- **M8**: Schema RL (Lu et al., ACL 2025) 存在于 bib 但未被引用，应在 §6 中讨论 [R1+R2]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. [AGREE] **\"Exact enforcement\" 需要术语校准** — 36.64% fallback rate 使 \"exact\" 不成立，需改为 \"best-effort\" + 级联分析 (MF1)\n2. [AGREE] **κ̄ overclaim** — \"analytical framework\" 应降级为 \"descriptive metric\" (MF2)\n3. [AGREE] **BoostCD 对比缺失** — 最直接的 IE constrained decoding 竞争方法未实验对比 (SF2)\n4. [AGREE] **模型规模声称过宽** — \"any autoregressive LM\" 需加限定 (SF3)\n5. [AGREE] **CF 代价透明度不足** — Abstract/Contributions 未充分披露 (SF4)\n6. [AGREE] **Abstract 信息密度过高** — 核心 message 被数字淹没 (SF5)\n7. [AGREE] **Entity registry 顺序依赖** — 贪心策略全局次优 + TCR 非生成时保证 (SF6)\n8. [AGREE] **实验覆盖和呈现质量高** — 四类违规分类法、三数据集四模型、诚实的 Limitations\n\n---\n\n## Reviewer Divergence\n\n1. **IterGen 区分的严重性** — R2 定为 Must-Fix（新颖性是接收关键维度），R1 降级为 Should-Fix（preventive vs. corrective 是公认不同设计范式）。Review Director 判定：降级为 Should-Fix (SF1)，因机制差异在领域内已有共识，但论文确实需要更显式地论述。\n\n2. **Related Work 压缩度** — R2 认为正文 §6 过于压缩（15 行），R1 反驳空间分配合理。Review Director 判定：8 页限制内，RW 放附录是常见做法，但 IterGen 机制对比应从附录移入正文。不单独列为 issue。\n\n3. **零样本 violation rate 分析的实际意义** — R1 认为 R-F1 2-8% 时分析价值有限，R2 反驳 diagnostic 价值独立于 task performance。Review Director 判定：论文 \"diagnostic\" 定位恰当，但建议在表格中增加视觉分隔以区分 ZS 和 FT 结果。不单独列为 issue。\n\n4. **Proposition 1 证明方法** — R1 要求不可判定性归约，R2 指出这是概念混淆（应用 pumping lemma 而非不可判定性归约），但同意 proof sketch 需加强。Review Director 采纳 R2 的修正，保留 MF3。\n\n---\n\n## Questions for Authors\n\n1. **Fallback 级联量化**：当 grammar-first fallback 触发后，错误类型赋值写入 entity registry。能否量化这种级联效应——即因 fallback 导致的错误 registry 状态触发了多少后续 fallback？(R1-Q2)\n\n2. **Bounded entity set 退化**：如果 schema 对 entity 数量设上限 k（实际场景常见），有效输出集变为有限语言（正则 ⊂ CF）。Proposition 1 的 \"unbounded\" 前提在实际场景中多大程度上成立？(R1-Q1)\n\n3. **DR 消除的 F1 影响**：Fine-tuning 后 DR 大幅下降（1-2%→0%）但 R-F1 仅变化 ±0.5pp。被消除的 violations 是否主要出现在已经错误的 triple 中（即 precision 端的 false positives）？(R2-Q3)\n\n4. **IterGen 对比**：OntoCoDec 的 domain/range 约束表达力受限于 prefix-decidable 性质。是否考虑过将框架扩展到更一般的语义约束（如 cardinality、temporal ordering）？主要技术障碍是什么？(R2-Q1)\n\n5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)\n\n---\n\n## Missing References\n\n1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]\n2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]\n3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]\n4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 GCD baseline 数字 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2 critical, 4 warning, 10 info）\n\n### Critical\n\n1. **主文前 4 页无任何 display item**：审稿人打开论文后连续翻过 4 页纯文本+公式才在第 5 页见到首个 Table。对于提出框架的系统论文，缺少架构概览图/流程图是严重的第一印象缺陷。\n2. **主文（8 页正文）零 Figure**：全文仅有的 3 个 Figure 全部在附录（p20/23/25）。系统/方法论文审稿人期望至少在 Method 部分看到一张框架图展示双层架构、约束编译流程或解码时 masking 工作方式。\n\n### Warning\n\n3. 连续 4 页纯文本+数学公式无视觉打断，阅读负担极重\n4. 主文 display items 全部为表格（Table 1-5），无可视化图表\n5. §6 Related Work + §7 Discussion 挤在同一页，Related Work 仅约半栏\n6. 附录 Extended Related Work 连续 3 页纯文本\n\n### Info（选摘）\n\n- Table 1 作为首个 display item 传达组件贡献而非方法核心，不如 overview figure 有锚定力\n- 表格使用 booktabs 风格，精度统一，格式整体专业\n- 主文 8 页，符合 EMNLP 2026 的 8 页正文限制\n- Figure 3 (beam width) 图内文字偏小，150dpi 下勉强可读\n\n**Review Director 评价**：主文零 Figure 是本轮最大的呈现缺陷。框架论文不提供架构图，审稿人需要完全靠文字和公式理解双层架构——这对第一印象和可理解性损害很大。强烈建议在 §3 Method 中增加一张框架概览图。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**EMNLP 2026 评分参考**：3.5 = Borderline Conference（可能被主会议接收，但需要修改）\n\n### 评分理由\n\n**达到 Conference 水平的因素**：\n- 可判定性引导的约束分层是新颖且有工程价值的视角\n- 实验设计系统全面（3 数据集 × 4 模型 × 多配置），消融清晰\n- Fine-tuning composability 论证回答了重要的部署问题\n- Limitations 和 Appendix 的坦诚度和详尽度高于平均水平\n\n**阻碍 Conference 接收的因素**：\n- **Claim 校准问题**（MF1+MF2）：核心技术声称（\"exact enforcement\"）和贡献声称（κ̄ \"analytical framework\"）与论文自身呈现的证据不一致。这不是技术错误——方法本身工作正常——而是叙事过度包装\n- **形式化不完整**（MF3）：论文以 \"formally compiles\" 定位，但核心定理仅有 proof sketch\n- **关键 baseline 缺失**（SF2）：未与最直接的竞争方法 BoostCD 进行实验对比\n- **视觉呈现缺陷**：主文零 Figure，框架论文无架构图\n\n### 路径分析\n\n**→ Conference (4.0)**：修复 MF1-MF4 的 claim 校准和形式化问题 + 补 BoostCD 对比 + 增加框架图。核心技术和实验质量足以支撑 Conference，当前的障碍主要是 presentation 和 claim 精度，而非 fundamental technical weakness。\n\n**→ Findings (3.0)**：如果 claim 校准问题未充分解决，论文仍是 solid Findings——实验贡献（四类违规分类法 + 系统消融 + composability 验证）本身有值得发表的价值。\n\n### Reviewer 评分\n\n| Reviewer | Overall | Soundness | Excitement | Reproducibility | Confidence |\n|----------|---------|-----------|------------|-----------------|------------|\n| R1 (方法+实验) | 3.5 | 3.5/5 | 3.5/5 | 4/5 | 4/5 |\n| R2 (新颖性+写作) | 3.5 | 4/5 | 3/5 | 4/5 | 4/5 |\n| **Director 综合** | **3.5** | **3.75** | **3.25** | **4** | **4** |\n\n### 核心判断\n\n论文解决了一个真实问题（LLM-based IE 的类型违规），技术执行扎实，实验覆盖面广。主要瓶颈不在方法本身，而在 **claim 校准**——\"exact enforcement\" 在 1/3 决策点上不成立、κ̄ 被包装为超出其统计证据的分析框架、形式化贡献的证明力度不匹配。如果作者能精确校准声称力度（将方法的实际能力边界诚实呈现，而非通过术语包装暗示更强的保证），论文可以在一轮 revision 内达到 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2 \"An analytical framework linking constraint tightness to enforcement outcomes\" → 改为 \"A descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes\"\n- \"formally compiles\" → 根据 MF3 的选择调整（补证明则保留，否则弱化）\n\n### §3 Method\n- §3.1 Proposition 1：补充完整 pumping lemma 证明（附录），或降级 contribution 声称\n- §3.3 \"exact pair-based enforcement\" → \"best-effort pair-based enforcement\"\n- §3.3 entity registry：讨论贪心赋值的局限性和 Level 3 non-local 约束\n- **增加框架概览图**（双层架构 + 约束编译流程 + 解码时 masking 工作方式）\n\n### §4 Constraint Composition\n- Eq.(2) 明确为 element-wise AND over vocabulary\n- 增加 fallback 级联分析段落\n- κ̄ 措辞从 \"analytical framework\" 降级\n\n### §5 Experiments\n- Table 1/3 中 ZS 和 FT 结果增加视觉分隔\n- Table 5 (WikiEvents) 标注 n=246/n=20 + FT 行报告 CI\n- DocRED beam search 50-doc 子集标注覆盖的 relation type 比例\n- CF 列在首次出现时增加解释\n\n### §6 Related Work\n- 增加 IterGen/OntoCoDec/PICARD 机制对比（preventive vs corrective vs incremental）\n- 引用 Schema RL (Lu et al., 2025) 和 Koldehoff et al. (2025)\n- 讨论 BoostCD 方法论差异\n- 末尾段调整为 positioning 而非 contribution recap\n\n### §7 Discussion and Conclusion\n- 加 \"across 7-8B parameter models\" 限定词\n- \"ontology-agnostic\" → \"applicable to both formal ontologies and empirically-derived type constraints\"\n\n### Abstract\n- 降低数字密度，聚焦 conceptual framing\n- 增加 CF trade-off 说明\n- κ̄ 措辞调整\n- \"formally compiles\" 根据 MF3 调整\n\n### BibTeX\n- 清理 10 orphan entries + 1 duplicate key",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
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
    "report": "# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ARR May 2026 | Deadline: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计 | R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\nOntoCoDec 将 IE 本体约束编译为双层 token-level 解码约束：语法层（XGrammar）保证 JSON 结构合法性和词汇成员关系；语义层通过运行时 entity registry + dynamic masking 强制 domain/range 类型兼容性。论文提出可判定性分类（context-free / prefix-decidable with state / non-local）指导约束分层设计，引入 constraint tightness κ̄ 描述 schema 限制性。在 SciERC（551 docs）、DocRED（998 docs）、WikiEvents（246 docs）三个数据集上使用 Qwen3-8B、Llama-3.1-8B、Mistral-7B（及 Llama-3.1-70B 简要评估）进行了系统的消融实验和 LoRA 微调组合性验证。\n\n---\n\n## Strengths\n\n**S1. 新颖的形式化视角。** 将 formal language theory 的可判定性分析引入 IE 约束解码，提出 context-free / prefix-decidable with state / non-local 的三层分类，为系统设计提供了有原则的指导。Proposition 1（Level 2 ⊄ Level 1）为双层架构的必要性提供了形式化论证基础。[R1+R2 共识]\n\n**S2. 全面且系统的实验设计。** 五路消融清晰隔离了 grammar 层和 semantic 层的贡献；跨模型（3+1 个）、跨数据集（3 个）、跨任务（RE + EE）的覆盖在 systems paper 中高于平均水平。四类违规分类法（DR/CF/RV/ET）允许精确理解每层约束的贡献和代价，远超同领域多数论文的二元 valid/invalid 评估。[R1+R2 共识]\n\n**S3. Fine-tuning composability 论证有价值。** Table 2 展示 LoRA + S1 在四个 model-dataset 组合上均实现 DR ≤ 0.09%、R-F1 ± 0.6pp。这回答了一个重要的部署问题——约束系统是否与参数优化兼容。Beam search (k=4) 进一步消除 SciERC 上全部四类违规。[R1+R2 共识]\n\n**S4. 诚实的局限性讨论。** Limitations section 明确承认 CF trade-off、模型规模限制、WikiEvents 样本量、评估仅限 LoRA 等问题。在投稿论文中这种坦诚度值得肯定。[R1+R2 共识]\n\n**S5. 实际工程价值。** 框架自动从任意 IE schema 编译约束，无需约束特定训练，可与任意自回归 LM 配合。Runtime overhead +10%（LoRA 配置），constraint compilation < 0.5s，scalability 到 200 entity types / 1000 relations 仅 2-3% overhead。即插即用的部署价值明确。[R1+R2 共识]\n\n**S6. 丰富的附录。** 22 页附录包含详尽的错误分析、scalability benchmarks、prompt 敏感性、document length 分析、TCR 机制、case studies。显著增强可复现性和可信度。[R1+R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（4 项，影响接收决定）\n\n**MF1. \"Exact enforcement\" 声称与 36.64% CF fallback rate 存在根本矛盾。** [R1-N2 raised, R2 AGREE — full consensus]\n\n§3.3 多处声称 \"exact pair-based enforcement\"，但 §4 的 grammar-first fallback 意味着当 S(t)∩G(t)=∅ 时语义约束被完全丢弃。Appendix C Table 8 显示 SciERC 上 fallback 在 36.64% 的 type-bearing positions 被触发，GENERIC 类型占 CF violations 的 63.3%（155/245）。更严重的是：fallback 导致的错误类型赋值会写入 entity registry，影响后续所有涉及该实体的 relation 的 domain/range 检查——论文未分析此级联失败效应。\n\n→ 修改建议：将 \"exact\" 改为 \"best-effort\" 或 \"targeted\"；分析并量化 fallback 级联行为；在 Abstract/§1 中披露 fallback rate。\n\n**MF2. κ̄ 作为 Contribution 2 (\"analytical linking framework\") 被过度声称。** [R2-N2 raised, R1 fully AGREE — full consensus]\n\nκ̄ 本质上是描述性统计量（|σ(r)|/|E|² 的归一化比例）。论文自身在 Appendix C 承认 \"descriptive characterization rather than a confirmatory statistical test\"（df=2, p>0.05），但 Abstract 和 Contribution 2 仍定位为 \"analytical linking framework\"，与论文自身的谨慎表述不一致。\n\n→ 修改建议：Contribution 2 降级为 \"a descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes and provides deployment guidance\"。\n\n**MF3. Proposition 1 仅为 proof sketch，与 \"formally compiles\" 定位不匹配。** [R1-N1 raised, R2 partially AGREE]\n\n论文将 \"decidability-guided constraint classification\" 定位为核心贡献之一，但 Proposition 1 仅给出 proof sketch。R2 指出 R1 原始批评中混淆了 non-context-freeness 与 undecidability（Proposition 1 声称的是 Level 2 ⊄ Level 1，应用 pumping lemma 而非不可判定性归约），但 R2 同意 proof sketch 对于声称 \"formal\" 的贡献偏弱。核心论证（PDA stack 无法追踪无界 entity-type binding）方向正确但需完整化。\n\n→ 修改建议：(A) 附录补充完整 pumping lemma 证明（~半页）；或 (B) 将 contribution 从 \"formal classification\" 降级为 \"classification motivated by formal language-theoretic observations\"。\n\n**MF4. WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力不足。** [R1-N3 raised, R2 partially AGREE]\n\nWikiEvents fine-tuning 使用 194/20/20 split，测试集仅 20 篇文档。R2 正确指出：零样本评估（246 docs）有效，问题限于 fine-tuning 行。但 Table 5 将两种设定并列呈现，未标注样本量差异，可能误导读者。正文 §5.4 的结论语气未相应降低。\n\n→ 修改建议：Table 5 内标注 n=246/n=20；fine-tuning 行报告 95% bootstrap CI；正文明确 fine-tuning 评估为 preliminary。\n\n### Should-Fix（8 项，影响评分但不一票否决）\n\n**SF1. 语义层核心机制与 IterGen/PICARD 的概念区分不充分。** [R2-N1 raised as Must-Fix, R1 AGREE substance but suggests Should-Fix — severity divergence]\n\nIterGen (Ugare et al., 2025) 同样在 grammar 层之上叠加语义约束（corrective backtracking）；PICARD (Scholak et al., 2021) 维护 incremental parsing monitor。论文在 §6 中未深入对比 preventive masking vs. corrective backtracking 的机制差异、效率特性和约束表达能力。R1 认为 masking vs. backtracking 是公认不同设计范式，novelty confusion 风险有限，建议降级。\n\n→ 修改建议：§6 增加显式机制对比（2-3 行 + 可选对比表），阐述 OntoCoDec 的 forward-only masking 效率优势及其约束表达力限制。\n\n**SF2. 无直接实验对比最接近的 IE 基线 BoostCD。** [R1-W1 + R2-W1, full consensus]\n\nBoostCD (Sakota et al., 2025) 同样在 SciERC/DocRED 上做 IE constrained decoding，是最直接的竞争方法。缺乏 head-to-head 数字对比使审稿人难以判断边际贡献。\n\n→ 修改建议：至少引用 BoostCD 报告的 SciERC 数字并讨论方法论差异；如代码可用，运行对比实验。\n\n**SF3. 模型规模声称过宽。** [R1-W2 + R2-W5, full consensus]\n\nAbstract \"applies to any autoregressive LM across four models (8B–70B)\" 实际上主要测试 7-8B 模型，70B (Llama-3.1-70B AWQ INT4) 仅在 §5.6 有简要零样本评估（无 fine-tuning composability）。注：两位 Reviewer 在交叉阶段均未注意到 70B 结果的存在（出现在 §5.6 \"Cross-scale generalizability\" 段，而非主要 cross-model table），说明该结果的呈现位置不够突出。\n\n→ 修改建议：Abstract/§1 限定为 \"validated primarily on 7-8B models with preliminary 70B results\"；将 70B 结果在正文中更突出地呈现。\n\n**SF4. CF 代价在 Abstract/Contribution 中不够透明。** [R2-W6 raised, R1 AGREE]\n\nGrammar-first fallback rate 36.64%（SciERC ZS）和 CF 上升（0.08→9.90%）仅出现在正文细节和 Appendix C，Abstract 轻描淡写 \"grammar-first fallback when constraints conflict\"。\n\n→ 修改建议：Abstract 增加 CF trade-off 说明。\n\n**SF5. Abstract 信息密度过高。** [R2-W4, R1 AGREE]\n\nAbstract 试图在一段中覆盖可判定性分类、三层架构、κ̄、跨模型数字、beam search、fine-tuning composability。核心 message（为什么 grammar 层不够、语义层如何补足）被数字细节遮蔽。\n\n→ 修改建议：保留 1-2 个关键数字，其余推至 Introduction。\n\n**SF6. Entity registry 顺序依赖导致全局次优类型赋值。** [R1-W4, R2 AGREE]\n\n贪心策略在第一次出现时锁定 entity 类型，后续更紧约束的 relation 无法修正。TCR (Appendix D) 是事后修复，不是生成时的 exact enforcement——进一步削弱 MF1 的 \"exact\" 声称。\n\n→ 修改建议：§3.3 或 §4 讨论贪心赋值局限性，定位为 Level 3 non-local 约束的实例。\n\n**SF7. \"Ontology-agnostic\" 声称实验支撑不足。** [R2-W2, R1 partially AGREE]\n\n仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 的 schema 来自训练数据经验统计。R1 指出编译机制确实不依赖来源，但 \"ontology\" 一词不准确。\n\n→ 修改建议：改为 \"applicable to both formal ontologies and empirically-derived type constraints\"。\n\n**SF8. DocRED beam search 仅 50 文档子集（零样本设定）。** [R1-W5, R2 AGREE]\n\nSciERC beam 用完整 551 docs，DocRED 零样本 beam 仅 50 docs。注：LoRA beam 已扩展到 998 docs（d064 实验），但零样本 beam 仍受限。\n\n→ 修改建议：标注子集规模限制并讨论代表性。\n\n### Minor（8 项）\n\n- **M1**: BibTeX 清理——10 orphan entries + 1 duplicate key (schall2025hiddencost) [R1+R2]\n- **M2**: S1/S2 命名与层级编号初读易混淆，建议改为 SP/TP 或 JOINT/SEQ [R2-M3, R1 AGREE]\n- **M3**: Table 5 \"—\" 标记缺少表注说明 [R2-M4, R1 AGREE]\n- **M4**: §4 Eq.(2) conjunction 应明确为 element-wise AND over vocabulary [R1]\n- **M5**: CF 列含义在 Table 1 首次出现时解释不足 [R1, R2 AGREE]\n- **M6**: Figure 1 (Appendix C) x 轴 \"κ·RV_baseline\" 物理含义不直观 [R1, R2 AGREE]\n- **M7**: §6 末尾一段从 related work positioning 滑向 contribution recapping [R1, R2 AGREE]\n- **M8**: Schema RL (Lu et al., ACL 2025) 存在于 bib 但未被引用，应在 §6 中讨论 [R1+R2]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. [AGREE] **\"Exact enforcement\" 需要术语校准** — 36.64% fallback rate 使 \"exact\" 不成立，需改为 \"best-effort\" + 级联分析 (MF1)\n2. [AGREE] **κ̄ overclaim** — \"analytical framework\" 应降级为 \"descriptive metric\" (MF2)\n3. [AGREE] **BoostCD 对比缺失** — 最直接的 IE constrained decoding 竞争方法未实验对比 (SF2)\n4. [AGREE] **模型规模声称过宽** — \"any autoregressive LM\" 需加限定 (SF3)\n5. [AGREE] **CF 代价透明度不足** — Abstract/Contributions 未充分披露 (SF4)\n6. [AGREE] **Abstract 信息密度过高** — 核心 message 被数字淹没 (SF5)\n7. [AGREE] **Entity registry 顺序依赖** — 贪心策略全局次优 + TCR 非生成时保证 (SF6)\n8. [AGREE] **实验覆盖和呈现质量高** — 四类违规分类法、三数据集四模型、诚实的 Limitations\n\n---\n\n## Reviewer Divergence\n\n1. **IterGen 区分的严重性** — R2 定为 Must-Fix（新颖性是接收关键维度），R1 降级为 Should-Fix（preventive vs. corrective 是公认不同设计范式）。Review Director 判定：降级为 Should-Fix (SF1)，因机制差异在领域内已有共识，但论文确实需要更显式地论述。\n\n2. **Related Work 压缩度** — R2 认为正文 §6 过于压缩（15 行），R1 反驳空间分配合理。Review Director 判定：8 页限制内，RW 放附录是常见做法，但 IterGen 机制对比应从附录移入正文。不单独列为 issue。\n\n3. **零样本 violation rate 分析的实际意义** — R1 认为 R-F1 2-8% 时分析价值有限，R2 反驳 diagnostic 价值独立于 task performance。Review Director 判定：论文 \"diagnostic\" 定位恰当，但建议在表格中增加视觉分隔以区分 ZS 和 FT 结果。不单独列为 issue。\n\n4. **Proposition 1 证明方法** — R1 要求不可判定性归约，R2 指出这是概念混淆（应用 pumping lemma 而非不可判定性归约），但同意 proof sketch 需加强。Review Director 采纳 R2 的修正，保留 MF3。\n\n---\n\n## Questions for Authors\n\n1. **Fallback 级联量化**：当 grammar-first fallback 触发后，错误类型赋值写入 entity registry。能否量化这种级联效应——即因 fallback 导致的错误 registry 状态触发了多少后续 fallback？(R1-Q2)\n\n2. **Bounded entity set 退化**：如果 schema 对 entity 数量设上限 k（实际场景常见），有效输出集变为有限语言（正则 ⊂ CF）。Proposition 1 的 \"unbounded\" 前提在实际场景中多大程度上成立？(R1-Q1)\n\n3. **DR 消除的 F1 影响**：Fine-tuning 后 DR 大幅下降（1-2%→0%）但 R-F1 仅变化 ±0.5pp。被消除的 violations 是否主要出现在已经错误的 triple 中（即 precision 端的 false positives）？(R2-Q3)\n\n4. **IterGen 对比**：OntoCoDec 的 domain/range 约束表达力受限于 prefix-decidable 性质。是否考虑过将框架扩展到更一般的语义约束（如 cardinality、temporal ordering）？主要技术障碍是什么？(R2-Q1)\n\n5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)\n\n---\n\n## Missing References\n\n1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]\n2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]\n3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]\n4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 GCD baseline 数字 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2 critical, 4 warning, 10 info）\n\n### Critical\n\n1. **主文前 4 页无任何 display item**：审稿人打开论文后连续翻过 4 页纯文本+公式才在第 5 页见到首个 Table。对于提出框架的系统论文，缺少架构概览图/流程图是严重的第一印象缺陷。\n2. **主文（8 页正文）零 Figure**：全文仅有的 3 个 Figure 全部在附录（p20/23/25）。系统/方法论文审稿人期望至少在 Method 部分看到一张框架图展示双层架构、约束编译流程或解码时 masking 工作方式。\n\n### Warning\n\n3. 连续 4 页纯文本+数学公式无视觉打断，阅读负担极重\n4. 主文 display items 全部为表格（Table 1-5），无可视化图表\n5. §6 Related Work + §7 Discussion 挤在同一页，Related Work 仅约半栏\n6. 附录 Extended Related Work 连续 3 页纯文本\n\n### Info（选摘）\n\n- Table 1 作为首个 display item 传达组件贡献而非方法核心，不如 overview figure 有锚定力\n- 表格使用 booktabs 风格，精度统一，格式整体专业\n- 主文 8 页，符合 EMNLP 2026 的 8 页正文限制\n- Figure 3 (beam width) 图内文字偏小，150dpi 下勉强可读\n\n**Review Director 评价**：主文零 Figure 是本轮最大的呈现缺陷。框架论文不提供架构图，审稿人需要完全靠文字和公式理解双层架构——这对第一印象和可理解性损害很大。强烈建议在 §3 Method 中增加一张框架概览图。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**EMNLP 2026 评分参考**：3.5 = Borderline Conference（可能被主会议接收，但需要修改）\n\n### 评分理由\n\n**达到 Conference 水平的因素**：\n- 可判定性引导的约束分层是新颖且有工程价值的视角\n- 实验设计系统全面（3 数据集 × 4 模型 × 多配置），消融清晰\n- Fine-tuning composability 论证回答了重要的部署问题\n- Limitations 和 Appendix 的坦诚度和详尽度高于平均水平\n\n**阻碍 Conference 接收的因素**：\n- **Claim 校准问题**（MF1+MF2）：核心技术声称（\"exact enforcement\"）和贡献声称（κ̄ \"analytical framework\"）与论文自身呈现的证据不一致。这不是技术错误——方法本身工作正常——而是叙事过度包装\n- **形式化不完整**（MF3）：论文以 \"formally compiles\" 定位，但核心定理仅有 proof sketch\n- **关键 baseline 缺失**（SF2）：未与最直接的竞争方法 BoostCD 进行实验对比\n- **视觉呈现缺陷**：主文零 Figure，框架论文无架构图\n\n### 路径分析\n\n**→ Conference (4.0)**：修复 MF1-MF4 的 claim 校准和形式化问题 + 补 BoostCD 对比 + 增加框架图。核心技术和实验质量足以支撑 Conference，当前的障碍主要是 presentation 和 claim 精度，而非 fundamental technical weakness。\n\n**→ Findings (3.0)**：如果 claim 校准问题未充分解决，论文仍是 solid Findings——实验贡献（四类违规分类法 + 系统消融 + composability 验证）本身有值得发表的价值。\n\n### Reviewer 评分\n\n| Reviewer | Overall | Soundness | Excitement | Reproducibility | Confidence |\n|----------|---------|-----------|------------|-----------------|------------|\n| R1 (方法+实验) | 3.5 | 3.5/5 | 3.5/5 | 4/5 | 4/5 |\n| R2 (新颖性+写作) | 3.5 | 4/5 | 3/5 | 4/5 | 4/5 |\n| **Director 综合** | **3.5** | **3.75** | **3.25** | **4** | **4** |\n\n### 核心判断\n\n论文解决了一个真实问题（LLM-based IE 的类型违规），技术执行扎实，实验覆盖面广。主要瓶颈不在方法本身，而在 **claim 校准**——\"exact enforcement\" 在 1/3 决策点上不成立、κ̄ 被包装为超出其统计证据的分析框架、形式化贡献的证明力度不匹配。如果作者能精确校准声称力度（将方法的实际能力边界诚实呈现，而非通过术语包装暗示更强的保证），论文可以在一轮 revision 内达到 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2 \"An analytical framework linking constraint tightness to enforcement outcomes\" → 改为 \"A descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes\"\n- \"formally compiles\" → 根据 MF3 的选择调整（补证明则保留，否则弱化）\n\n### §3 Method\n- §3.1 Proposition 1：补充完整 pumping lemma 证明（附录），或降级 contribution 声称\n- §3.3 \"exact pair-based enforcement\" → \"best-effort pair-based enforcement\"\n- §3.3 entity registry：讨论贪心赋值的局限性和 Level 3 non-local 约束\n- **增加框架概览图**（双层架构 + 约束编译流程 + 解码时 masking 工作方式）\n\n### §4 Constraint Composition\n- Eq.(2) 明确为 element-wise AND over vocabulary\n- 增加 fallback 级联分析段落\n- κ̄ 措辞从 \"analytical framework\" 降级\n\n### §5 Experiments\n- Table 1/3 中 ZS 和 FT 结果增加视觉分隔\n- Table 5 (WikiEvents) 标注 n=246/n=20 + FT 行报告 CI\n- DocRED beam search 50-doc 子集标注覆盖的 relation type 比例\n- CF 列在首次出现时增加解释\n\n### §6 Related Work\n- 增加 IterGen/OntoCoDec/PICARD 机制对比（preventive vs corrective vs incremental）\n- 引用 Schema RL (Lu et al., 2025) 和 Koldehoff et al. (2025)\n- 讨论 BoostCD 方法论差异\n- 末尾段调整为 positioning 而非 contribution recap\n\n### §7 Discussion and Conclusion\n- 加 \"across 7-8B parameter models\" 限定词\n- \"ontology-agnostic\" → \"applicable to both formal ontologies and empirically-derived type constraints\"\n\n### Abstract\n- 降低数字密度，聚焦 conceptual framing\n- 增加 CF trade-off 说明\n- κ̄ 措辞调整\n- \"formally compiles\" 根据 MF3 调整\n\n### BibTeX\n- 清理 10 orphan entries + 1 duplicate key",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1248 · 2026-05-20T17:33:18.544173+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4169
}
```

</details>

---


### Assistant

_source line 1249 · 2026-05-20T17:33:27.579835+00:00_

审稿报告已投递至 Research Director。

**Round 12 审稿完成**：

- **Overall: 3.5 Borderline Conference**（两位 Reviewer 一致）
- **4 Must-Fix**：(1) "exact enforcement" 术语与 36.64% fallback 矛盾 + 级联分析缺失；(2) κ̄ overclaim；(3) Proposition 1 proof sketch 不够严格；(4) WikiEvents FT 20-doc 统计效力
- **8 Should-Fix**：IterGen 区分、BoostCD 对比缺失、模型规模声称、CF 透明度、Abstract 密度、entity registry 顺序依赖、"ontology-agnostic" 用词、DocRED beam 50-doc
- **8 Minor**：bib 清理、S1/S2 命名、表注等
- **视觉审查**：主文零 Figure 是最大呈现缺陷，强烈建议增加框架概览图
- **路径判断**：修复 claim 校准 + 补 BoostCD 对比 + 增框架图 → 可达 Conference (4.0)；不修复 → solid Findings (3.0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 90

## Round 90

2 recorded events


### User

_source line 1250 · 2026-05-20T17:33:30.074558+00:00_

[Reviewer 2 审稿结果]:
已提交交叉回应。总结关键判断：

**与 R1 的共识**：
- N2（"exact enforcement" 术语矛盾 + fallback 级联）和 W4（entity registry 顺序依赖）是最有力的技术批评
- W1（缺 BoostCD 对比）、W2（模型规模声称过宽）两位 reviewer 独立提出

**对 R1 的反驳**：
- N1 的论证有方向性错误——将 non-context-freeness 混淆为 undecidability，要求的证明方法不匹配 Proposition 1 的实际声称
- W3（零样本违规率意义）——论文的 diagnostic 定位是合理的
- LoRA 3 epochs 在该参数量和数据规模下是标准设定

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

_source line 1251 · 2026-05-20T17:33:42.805081+00:00_

审稿报告已投递至 Research Director。

**Round 12 审稿完成，总结：**

- **Overall: 3.5 Borderline Conference**（两位 Reviewer 一致）
- **4 个 Must-Fix**：(1) "exact enforcement" 与 36.64% fallback rate 矛盾 + 级联失败未分析；(2) κ̄ "analytical framework" overclaim；(3) Proposition 1 proof sketch 不够严格；(4) WikiEvents FT 20-doc 统计效力不足
- **8 个 Should-Fix**：IterGen 区分、BoostCD 对比缺失、模型规模声称、CF 透明度、Abstract 密度、entity registry 顺序依赖、"ontology-agnostic" 用词、DocRED beam 50-doc
- **8 个 Minor**：bib 清理、S1/S2 命名、表注等
- **视觉审查**：主文零 Figure 是最大呈现缺陷，强烈建议增加框架图
- **路径判断**：修复 claim 校准 + 补 BoostCD 对比 + 加框架图 → 可达 Conference (4.0)；未修复则为 strong Findings (3.0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 91

## Round 91

80 recorded events


### User

_source line 1252 · 2026-05-20T18:33:49.556667+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
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

_source line 1253 · 2026-05-20T18:33:55.619765+00:00_

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

_source line 1254 · 2026-05-20T18:33:55.670778+00:00_

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

_source line 1255 · 2026-05-20T18:34:01.143915+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
  "max_results": "11"
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1256 · 2026-05-20T18:34:01.194568+00:00_



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

_source line 1257 · 2026-05-20T18:34:05.061576+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-20T18:34:05.162560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-20T18:34:09.430391+00:00_

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

_source line 1260 · 2026-05-20T18:34:10.886776+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (124 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- d066_sweep_llama_docred_beam4_s1（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_sweep_llama_scierc_beam4_s1_551** (success): d066 SciERC beam sweep: Llama beam4 constrained (full_s1) on 551-sentence test set. Beam width k=4 with schema constraints should eliminate all four violation types (ET/RV/DR/CF=0) while maintaining R-F1 within ±1pp of unconstrained.\n- **d066_sweep_llama_docred_beam4_unc** (success): d066 DocRED beam sweep sub-task: Llama beam4 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure. ← 基于 d066_beam_sweep\n- **d066_sweep_llama_docred_beam1_s1** (success): d066 DocRED beam sweep sub-task: Llama beam1 (greedy) constrained (full_s1) 
…[truncated 1052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-20T18:34:11.037861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "80"
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
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-20T18:34:11.390313+00:00_

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
19	\usepackage{tikz}
20	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
21	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
22	
23	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	% === Abstract ===
31	\input{abstract}
32	
33	% === §1 Introduction ===
34	\input{section1_introduction_draft}
35	
36	% === §2 Background ===
37	\input{section2_background}
38	
39	% === §3 Method ===
40	\input{section3_method_draft}
41	
42	% === §4 Constraint Composition ===
43	\section{Constraint Composition}
44	\label{sec:composition}
45	\input{section4_composition_draft}
46	
47	% === §5 Experiments ===
48	\section{Experiments}
49	\label{sec:experiments}
50	
51	\input{section3_violation_landscape}
52	
53	\input{section5_scierc_draft}
54	\input{section5_docred_draft}
55	\input{section5_crossmodel_draft}
56	\input{section5_wikievents_draft}
57	\input{section5_runtime}
58	
59	% === §6 Related Work ===
60	\input{section6_related_work}
61	
62	% === §7 Discussion and Conclusion ===
63	\section{Discussion and Conclusion}
64	\label{sec:discussion}
65	\input{section7_conclusion_compressed}
66	
67	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
68	\clearpage
69	\section*{Limitations}
70	
71	\paragraph{Constraint scope.}
72	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; 
…[truncated 1626 chars]

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

_source line 1263 · 2026-05-20T18:34:11.390702+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1264 · 2026-05-20T18:34:17.917181+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found several results related to EMNLP 2026 and ARR submission guidelines. Here's what I found:

## EMNLP 2026 Workshop Examp
…[truncated 1476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6526
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-20T18:34:23.151037+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR"
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
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-20T18:34:24.105248+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 submission guidelines page limit formatting requirements"
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
    "query": "ARR 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-20T18:34:24.607741+00:00_

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

_source line 1268 · 2026-05-20T18:34:29.528655+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"}]

Based on the search results, here are the key details about EMNLP 2026's main conference call for papers submission deadline and ARR requirements:

## ARR Submission Deadline

The ARR submission deadline is 
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6377
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-20T18:34:31.186110+00:00_

Web search results for query: "ARR 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Abstract Submission Info – ARRS 2026 | April 12-15, 2026","url":"https://www2.arrs.org/am26/abstract-submission-info/"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ARR 2026 submission guidelines regarding page limits and formatting requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references. Final versions of short papers may have up to five (5) pages, plus unlimited pages for acknowledgments and references.

For both long and short papers, all figures and tables that are part of the main text must fit within these page limits. The conference encourages submission o
…[truncated 858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7080
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-20T18:34:31.186645+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6578
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-20T18:34:38.115284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" \"double-blind\" OR \"anonymity\" OR \"appendix\" submission requirements site:2026.emnlp.org"
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
    "query": "\"EMNLP 2026\" \"call for papers\" \"double-blind\" OR \"anonymity\" OR \"appendix\" submission requirements site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-20T18:34:38.768690+00:00_

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

_source line 1273 · 2026-05-20T18:34:38.819371+00:00_

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


### Tool result

_source line 1274 · 2026-05-20T18:34:48.512889+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" "double-blind" OR "anonymity" OR "appendix" submission requirements site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Papers for the 2026 BabyLM Workshop","url":"https://arxiv.org/pdf/2602.20092"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

I found relevant information about EMNLP 2026 submission requirements. Here are the key findings:

## Double-Blind Review

The reviewing process will be double-blind. For the Industry Track specifically, submissions must neither include the authors' names nor their affiliations, and self-references that reveal the authors' identities must be avoided.

## Anonymity Requirements

Following the ACL and ARR policies, there is no anonymity period requirement. This means there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review.

## Appendix Policy

Authors are asked not to abuse the option of an unlimited appendix and only to include material that supports the primary messages and content of the paper; for the final papers, especially those with an appen
…[truncated 759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 10397
}
```

</details>

---


### Tool call

_source line 1275 · 2026-05-20T18:34:55.375073+00:00_

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

_source line 1276 · 2026-05-20T18:34:56.280799+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R12 Action Matrix dispatched (2026-05-20)
3	
4	# ============================================================
5	# Round 12 Must-Fix
6	# ============================================================
7	
8	- id: "R12-MF1"
9	  summary: "'Exact enforcement' 声称与 36.64% CF fallback rate 矛盾 + 级联失败未分析"
10	  category: method
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 12
14	  last_seen_round: 12
15	  mentions:
16	    - round: 12
17	      reviewers: [1, 2]
18	      note: "R1-N2 raised, R2 AGREE。Full consensus。§3.3 'exact' vs §4 grammar-first fallback。"
19	  action_items:
20	    - round: 12
21	      action: "Paper Agent: 'exact'→'best-effort' 全文替换 + §3.3 fallback 讨论 + §4 级联分析段落"
22	      assigned_to: paper_agent
23	      status: in_progress
24	    - round: 12
25	      action: "Agent: SciERC ZS fallback 级联量化分析（cascade depth + violation count）"
26	      assigned_to: agent
27	      status: in_progress
28	  resolution: ""
29	  resolution_round: null
30	
31	- id: "R12-MF2"
32	  summary: "κ̄ 作为 Contribution 2 ('analytical linking framework') 被过度声称"
33	  category: framing
34	  severity: critical
35	  status: in_progress
36	  first_raised_round: 12
37	  last_seen_round: 12
38	  mentions:
39	    - round: 12
40	      reviewers: [1, 2]
41	      note: "R2-N2 raised, R1 fully AGREE。Appendix C 自承 'descriptive characterization'。"
42	  action_items:
43	    - round: 12
44	      action: "Paper Agent: Contribution 2 降级为 'descriptive metric' + Abstract/§4 措辞同步"
45	      assigned_to: paper_agent
46	      status: in_progress
47	  resolution: ""
48	  resolution_round: null
49	
50	- id: "R12-MF3"
51	  summary: "Proposition 1 仅为 proof sketch，与 'formally compiles' 定位不匹配"
52	  category: method
53	  severity: critical
54	  status: in_progress
55	  first_raised_round: 12
56	  last_seen_round: 12
57	  mentions:
58	    - round: 12
59	      reviewers: [1, 2]
60	      note: "R1-N1 raised, R2 partially AGREE。方向正
…[truncated 16439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1277 · 2026-05-20T18:34:56.331659+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
  "description": "Check external review config setting"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
    "description": "Check external review config setting"
  }
}
```

</details>

---


### Tool result

_source line 1278 · 2026-05-20T18:34:57.738459+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1279 · 2026-05-20T18:34:57.890154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && ls -la *.tex *.pdf 2>/dev/null && wc -l *.tex 2>/dev/null",
  "description": "List paper files and line counts"
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
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && ls -la *.tex *.pdf 2>/dev/null && wc -l *.tex 2>/dev/null",
    "description": "List paper files and line counts"
  }
}
```

</details>

---


### Tool result

_source line 1280 · 2026-05-20T18:34:57.941072+00:00_

-rw-r--r-- 1 ubuntu ubuntu   1686 May 20 17:49 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   1971 May 14 06:19 abstract_d3264e.tex
-rw-r--r-- 1 ubuntu ubuntu   1971 May 14 06:19 abstract_fd4b26.tex
-rw-r--r-- 1 ubuntu ubuntu  13657 May 20 16:58 appendix_beam_search.tex
-rw-r--r-- 1 ubuntu ubuntu   7510 May 19 06:54 appendix_case_studies.tex
-rw-r--r-- 1 ubuntu ubuntu  32467 May 20 17:54 appendix_discussion.tex
-rw-r--r-- 1 ubuntu ubuntu   3231 May 19 06:52 appendix_doc_length.tex
-rw-r--r-- 1 ubuntu ubuntu   1342 May 19 06:52 appendix_full_ft.tex
-rw-r--r-- 1 ubuntu ubuntu   3027 May 19 18:05 appendix_kappa_case_study.tex
-rw-r--r-- 1 ubuntu ubuntu   2422 May 19 06:53 appendix_llama_per_relation.tex
-rw-r--r-- 1 ubuntu ubuntu   3120 May 20 12:52 appendix_prompt_sensitivity.tex
-rw-r--r-- 1 ubuntu ubuntu   2622 May 17 10:48 appendix_prompts.tex
-rw-r--r-- 1 ubuntu ubuntu   4388 May 20 17:57 appendix_pumping_lemma.tex
-rw-r--r-- 1 ubuntu ubuntu  21483 May 19 15:20 appendix_related_work.tex
-rw-r--r-- 1 ubuntu ubuntu   4096 May 20 12:53 appendix_reproducibility.tex
-rw-r--r-- 1 ubuntu ubuntu    857 May 19 00:41 appendix_sampling_table.tex
-rw-r--r-- 1 ubuntu ubuntu   1539 May 19 10:24 appendix_scalability.tex
-rw-r--r-- 1 ubuntu ubuntu   5474 May 19 23:53 appendix_tcr.tex
-rw-r--r-- 1 ubuntu ubuntu   2020 May 19 18:04 case_study_kappa_dr.tex
-rw-r--r-- 1 ubuntu ubuntu   5022 May 19 10:24 checklist.tex
-rw-r--r-- 1 ubuntu ubuntu   6811 May 14 21:07 discussion_paragraphs.tex
-rw-r--r-- 1 ubuntu ubuntu   4562 May 14 18:29 discussion_paragraphs_cf83d1.tex
-rw-r--r-- 1 ubuntu ubuntu   3592 May 20 18:05 fig1_framework.tex
-rw-r--r-- 1 ubuntu ubuntu 567940 May 20 18:31 main.pdf
-rw-r--r-- 1 ubuntu ubuntu   7209 May 20 18:19 main.tex
-rw-r--r-- 1 ubuntu ubuntu 468881 May 19 08:38 ontocodec_paper_r10_final.pdf
-rw-r--r-- 1 ubuntu ubuntu 450194 May 19 07:48 ontocodec_paper_r9_final.pdf
-rw-r--r-- 1 ubuntu ubuntu   9254 May 18 14:35 p3_case_studies.tex
-rw-r--r-- 1 ubuntu ubuntu   92
…[truncated 3160 chars]

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

_source line 1281 · 2026-05-20T18:35:07.783749+00:00_

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

_source line 1282 · 2026-05-20T18:35:08.135666+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that formally compiles Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) guarantees JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) enforces best-effort pair-based domain/range type constraints via a stateful entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric that correlates schema restrictiveness with enforcement outcomes and provides deployment guidance.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} reduces DR by 94--100\% with negligible R-F1 impact ($\pm$0.6\,pp), with modest cross-field (CF) costs resolvable via beam search.
7	The framework extends to event extraction without modification, applicable to both formal ontologies and empirically-derived type constraints.
8	\textsc{OntoCoDec} compiles constraints automatically at inference time, requires no constraint-specific training, and is validated primarily on 7--8B parameter models with preliminary 70B evaluation across three tokenizer families.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1283 · 2026-05-20T18:35:08.336917+00:00_

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

_source line 1284 · 2026-05-20T18:35:08.638887+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption; reliable type-safety enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives, sacrificing recall; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance
…[truncated 2858 chars]

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

_source line 1285 · 2026-05-20T18:35:08.639408+00:00_

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

_source line 1286 · 2026-05-20T18:35:09.041531+00:00_

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
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1287 · 2026-05-20T18:35:09.041935+00:00_

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

_source line 1288 · 2026-05-20T18:35:10.046913+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that compiles IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec guarantees levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
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
…[truncated 6860 chars]

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

_source line 1289 · 2026-05-20T18:35:10.097633+00:00_

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

_source line 1290 · 2026-05-20T18:35:10.549914+00:00_

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
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):\footnote{For symmetric relations, $|\sigma(r)|$ counts ordered pairs; the normalization $|\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	The mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness; tighter constraints force more frequent fal
…[truncated 2157 chars]

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

_source line 1291 · 2026-05-20T18:35:10.700967+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -80",
  "description": "Read project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -80",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 1292 · 2026-05-20T18:35:10.751697+00:00_

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

_source line 1293 · 2026-05-20T18:35:15.923070+00:00_

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

_source line 1294 · 2026-05-20T18:35:16.877507+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), eliminating DR with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations at 1.54$\times$ latency.
8	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
9	The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates asso
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-20T18:35:16.928192+00:00_

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

_source line 1296 · 2026-05-20T18:35:17.380745+00:00_

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
…[truncated 5714 chars]

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

_source line 1297 · 2026-05-20T18:35:17.381125+00:00_

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

_source line 1298 · 2026-05-20T18:35:17.783077+00:00_

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
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1299 · 2026-05-20T18:35:17.783461+00:00_

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

_source line 1300 · 2026-05-20T18:35:18.787866+00:00_

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
…[truncated 1384 chars]

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

_source line 1301 · 2026-05-20T18:35:18.838510+00:00_

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

_source line 1302 · 2026-05-20T18:35:19.140322+00:00_

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
…[truncated 2297 chars]

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

_source line 1303 · 2026-05-20T18:35:19.190971+00:00_

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

_source line 1304 · 2026-05-20T18:35:19.241650+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Full constraint compilation (schema parsing + grammar build): one-time $<$0.5\,s across all tested scales (Appendix~\ref{app:scalability}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Beam search ($k{=}4$) explores paths satisfying both layers jointly.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both models (R-F1 44--47); under zero-shot, beam reduces DR to 0\% and CF substantially (9.90\%\,$\to$\,0.53\% Qwen on SciERC; Appendix~\ref{app:beam-search}).
13	DocRED zero-shot beam evaluates on a 50-document subset (compute cost; LoRA beam uses the full 998-document set).
14	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Preliminary 70B evaluation.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on both SciERC (R-F1 $-$0.03\,pp) and DocRED (R-F1 $+$0.04\,pp), one of three configurations to eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%), partly because constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Scale reduces but does not eliminate violations.
22	

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

_source line 1305 · 2026-05-20T18:35:23.996403+00:00_

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

_source line 1306 · 2026-05-20T18:35:24.348283+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} guarantee format validity via CFG-based token masking; GCD~\cite{geng2023gcd} applies this to IE.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but these type environments are fully known at compile time and cover all legal programs.
9	IE differs structurally: the entity registry accumulates dynamically during generation, type assignments depend on the co-occurring relation, and the schema may not cover all valid outputs, necessitating fallback (\S\ref{sec:composition}).
10	OntoCoDec's contribution is not the type-to-mask paradigm itself, but (1)~formal decidability analysis guiding constraint layering, (2)~mechanisms for dynamic registry and incomplete coverage, and (3)~systematic validation across three IE tasks and four models.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, and GUIDEX~\cite{guidex2025} encode ontology structure as typed code; REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} unify extraction via structured training, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	Code-generation approaches achieve type compliance via format constraints but produce 45\% empty outputs on zero-shot RE (vs.\ 0\% for OntoCoDec), reflecting a coverage--compliance trade-off that decoding-time enforcement avoids.
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} first formulated
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1307 · 2026-05-20T18:35:24.499310+00:00_

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

_source line 1308 · 2026-05-20T18:35:25.303321+00:00_

1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.09\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	For deployment, we recommend beam search with $k{\geq}4$ as the default: it resolves the CF trade-off inherent in greedy constrained decoding, eliminating all four violation types on both datasets at 1.54$\times$ latency.
6	$\bar{\kappa}$ provides a descriptive diagnostic correlating schema restrictiveness with enforcement outcomes, with entity type confusability as the critical co-factor (Appendix~\ref{app:kappa-case-study}); together with the decidability taxonomy, it yields a principled deployment workflow.
7	Our evaluation is validated primarily on 7--8B parameter models with preliminary 70B results; scaling behavior at other model sizes remains to be confirmed.
8	

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

_source line 1309 · 2026-05-20T18:35:25.303870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 1310 · 2026-05-20T18:35:25.304136+00:00_

1	\begin{figure}[t]
2	\centering
3	\begin{tikzpicture}[
4	    >=Stealth,
5	    scale=0.68, transform shape,
6	    bx/.style={draw, rounded corners=2pt, minimum height=0.5cm, align=center, font=\scriptsize},
7	    ann/.style={font=\tiny, text=black!55},
8	    phase/.style={font=\scriptsize\bfseries, text=black!70},
9	]
10	
11	% === Phase labels ===
12	\node[phase] at (-2.8, 0.3) {Compile-time};
13	\node[phase] at (-2.8,-2.7) {Decode-time};
14	\draw[dashed, black!30] (-4.2,-1.3) -- (5.5,-1.3);
15	
16	% === COMPILE-TIME (top) ===
17	\node[bx, fill=black!8, text width=1.9cm] (onto) at (0,0) {IE Ontology\\[-1pt]$\mathcal{O}{=}(\mathcal{E},\mathcal{R},\sigma)$};
18	
19	\node[bx, fill=blue!8, text width=1.6cm] (ebnf) at (-1.8,-0.9) {EBNF Grammar\\[-1pt]{\tiny JSON+enum($\mathcal{E},\mathcal{R}$)}};
20	\node[bx, fill=orange!8, text width=1.6cm] (pairs) at (1.8,-0.9) {Valid-Pairs\\[-1pt]{\tiny $\sigma(r)$ + $\mathcal{E}$ set}};
21	
22	\draw[->, thick] (onto) -- (ebnf);
23	\draw[->, thick] (onto) -- (pairs);
24	\node[ann] at (-0.3,-0.25) {compile};
25	
26	% === DECODE-TIME (bottom) ===
27	\node[bx, fill=blue!6, text width=1.5cm] (gt) at (-1.8,-2.1) {$G(t)\subseteq V$\\[-1pt]{\tiny grammar mask}};
28	\node[bx, fill=orange!6, text width=1.5cm] (st) at (1.8,-2.1) {$S(t)\subseteq V$\\[-1pt]{\tiny semantic mask}};
29	
30	% Entity Registry
31	\node[draw, dashed, rounded corners=2pt, fill=yellow!8, font=\scriptsize, text width=1.4cm, align=center, minimum height=0.4cm] (reg) at (3.8,-2.1) {$\mathcal{D}$: name$\to$type};
32	
33	\draw[->, thick] (ebnf) -- (gt);
34	\draw[->, thick] (pairs) -- (st);
35	\draw[->, thick, black!50] (reg) -- (st);
36	
37	% Composition
38	\node[bx, fill=gray!10, text width=1.8cm] (comp) at (0,-3.2) {$M_{\mathrm{final}}{=}G(t){\wedge}S(t)$};
39	\draw[->, thick] (gt) -- (comp);
40	\draw[->, thick] (st) -- (comp);
41	
42	% Decision
43	\node[draw, diamond, aspect=2.5, inner sep=0.5pt, font=\scriptsize] (dec) at (0,-4.3) {$G{\cap}S{=}\emptyset$?};
44	\draw[->, th
…[truncated 1802 chars]

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

_source line 1311 · 2026-05-20T18:35:25.856863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "80"
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
    "offset": "80"
  }
}
```

</details>

---


### Tool result

_source line 1312 · 2026-05-20T18:35:25.957762+00:00_

80	\paragraph{Evaluation coverage.}
81	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
82	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.
83	Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
84	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
85	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
86	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
87	
88	\paragraph{Engineering considerations.}
89	Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
90	Our approach requires access to model logits for token-level masking, which excludes API-only models (e.g., GPT-4, Claude) where only output text is available; extending to API-only settings would require alternative enforcement mechanisms such as constrained sampling APIs or output reranking.
91	Continuation maski
…[truncated 2023 chars]

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

_source line 1313 · 2026-05-20T18:35:31.079246+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1314 · 2026-05-20T18:35:31.632089+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1315 · 2026-05-20T18:35:31.632545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
  }
}
```

</details>

---


### Tool result

_source line 1316 · 2026-05-20T18:35:31.684038+00:00_

1	% Appendix: Full Proof of Proposition 1
2	% Level 2 (prefix-decidable with state) constraints are not context-free.
3	
4	\section{Full Proof of Proposition 1}
5	\label{app:pumping-lemma}
6	
7	We prove that domain/range type constraints for IE with unbounded entity sets cannot be expressed by any context-free grammar, using the pumping lemma for context-free languages.
8	
9	\begin{proof}
10	Define the language $L$ of valid IE outputs over ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ with $\mathcal{E} = \{\tau_A, \tau_B\}$, $\mathcal{R} = \{r\}$, and $\sigma(r) = \{(\tau_A, \tau_A)\}$ (i.e., $r$ requires both head and tail to be type $\tau_A$).
11	
12	An output string has the form:
13	\[
14	w = e_1\, e_2\, \cdots\, e_n\;\; \texttt{REL}(h{=}e_k,\, r,\, \tau^h)
15	\]
16	where each $e_i$ is an entity with type $\tau_{a_i} \in \{\tau_A, \tau_B\}$, and $\tau^h$ is the head type field of a relation triple referencing entity $e_k$ ($1 \leq k \leq n$).
17	
18	The type-validity constraint requires $\tau^h = \tau_{a_k}$ (the head type must match the referenced entity's type) \emph{and} $\tau^h \in \operatorname{dom}(r) = \{\tau_A\}$.
19	Combined: a string $w \in L$ if and only if $\tau_{a_k} = \tau_A$.
20	
21	Now consider strings of the specific form:
22	\[
23	w_n = \underbrace{\tau_B\; \tau_B\; \cdots\; \tau_B}_{n-1}\; \tau_A\;\; \texttt{REL}(h{=}e_n,\, r,\, \tau_A)
24	\]
25	where the first $n{-}1$ entities have type $\tau_B$ and only entity $e_n$ has type $\tau_A$.
26	The relation references $e_n$, so $\tau^h = \tau_A = \tau_{a_n}$, satisfying both the registry consistency and domain constraint.
27	Thus $w_n \in L$ for all $n$.
28	
29	Assume for contradiction that $L$ is context-free.
30	By the pumping lemma, there exists a pumping length $p$ such that any $w \in L$ with $|w| \geq p$ can be written as $w = uvxyz$ where:
31	\begin{enumerate}[label=(\roman*)]
32	    \item $|vy| \geq 1$,
33	    \item $|vxy| \leq p$,
34	    \item $uv^i xy^i z \in L$ for all $i \g
…[truncated 2562 chars]

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

_source line 1317 · 2026-05-20T18:35:35.400052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 3 -name \"*.yaml\" -path \"*/schema_semantic*\" 2>/dev/null | head -10",
  "description": "Find config files for the project"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 3 -name \"*.yaml\" -path \"*/schema_semantic*\" 2>/dev/null | head -10",
    "description": "Find config files for the project"
  }
}
```

</details>

---


### Tool result

_source line 1318 · 2026-05-20T18:35:35.501086+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml

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

_source line 1319 · 2026-05-20T18:35:39.467808+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null",
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
    "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1320 · 2026-05-20T18:35:39.518773+00:00_

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

_source line 1321 · 2026-05-20T18:35:42.983631+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null; echo \"---\"; grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/*.yaml 2>/dev/null | head -5",
  "description": "Search for external review settings"
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
    "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null; echo \"---\"; grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/*.yaml 2>/dev/null | head -5",
    "description": "Search for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1322 · 2026-05-20T18:35:43.084549+00:00_

---

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

_source line 1323 · 2026-05-20T18:35:56.081703+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1324 · 2026-05-20T18:35:56.182512+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Wed May 20 18:31:00 2026 UTC
ModDate:         Wed May 20 18:31:00 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           33
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       567940 bytes
Optimized:       no
PDF version:     1.7

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

_source line 1325 · 2026-05-20T18:36:30.394992+00:00_

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

_source line 1326 · 2026-05-20T18:36:50.051390+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19656
}
```

</details>

---


### Tool call

_source line 1327 · 2026-05-20T18:36:50.107192+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- 目标 venue: EMNLP 2026（via ARR May cycle）\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 长文正文 ≤ 8 页，参考文献无限制\n- Limitations 必须有，不计入页数\n- ACL 模板，double-blind 审稿\n- 附录不要求审稿人审查\n\n## 你的审查侧重\n\n### A. 形式化声称与证明\n1. Proposition 1 声称 Level 2 约束非 context-free——proof sketch 是否充分？附录 pumping lemma 完整证明是否严密？\n2. \"best-effort pair-based enforcement\" 的精确含义——是否有遗漏的 corner case？\n3. 三级 decidability taxonomy 是否 well-motivated？分类边界是否清晰？\n4. 论文声称 \"formally compiles\"——实际实现是否匹配这一措辞？\n5. grammar-first fallback 是否有严格的正确性保证？级联失败分析是否充分？\n\n### B. 实验设计与统计严谨性\n1. 五路消融实验设计是否充分隔离各层贡献？\n2. CF trade-off：论文声称 CF 是 \"resolvable via beam search\"——证据是否充分（特别是 DocRED）？\n3. 统计显著性：bootstrap 检验设置是否合理？样本量是否足够？\n4. WikiEvents EE fine-tuning 仅 20 文档测试集——统计效力如何？\n5. DocRED beam search 零样本仅 50 文档子集——是否影响结论可靠性？\n6. 70B 评估仅为 \"preliminary\"——声称范围是否合理？\n7. Constraint tightness κ̄ 作为 \"descriptive metric\"——是否有足够的预测性证据支持其 deployment guidance 价值？\n\n### C. 实验公平性\n1. Baseline 选择是否充分？是否遗漏了最接近的 IE constrained decoding 基线（如 BoostCD、IterGen）？\n2. 与 GoLLIE 等 schema-aware IE 系统的对比是否公平？\n3. Post-hoc filtering 对比是否公平？\n\n### D. 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条 S1, S2, ...)\n3. **Weaknesses** (逐条 W1, W2, ... 区分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References**\n6. **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5, 按 EMNLP 2026 ARR 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit), Confidence (1-5)\n\n严格评审，不留情面。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- 目标 venue: EMNLP 2026（via ARR May cycle）\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 长文正文 ≤ 8 页，参考文献无限制\n- Limitations 必须有，不计入页数\n- ACL 模板，double-blind 审稿\n- 附录不要求审稿人审查\n\n## 你的审查侧重\n\n### A. 形式化声称与证明\n1. Proposition 1 声称 Level 2 约束非 context-free——proof sketch 是否充分？附录 pumping lemma 完整证明是否严密？\n2. \"best-effort pair-based enforcement\" 的精确含义——是否有遗漏的 corner case？\n3. 三级 decidability taxonomy 是否 well-motivated？分类边界是否清晰？\n4. 论文声称 \"formally compiles\"——实际实现是否匹配这一措辞？\n5. grammar-first fallback 是否有严格的正确性保证？级联失败分析是否充分？\n\n### B. 实验设计与统计严谨性\n1. 五路消融实验设计是否充分隔离各层贡献？\n2. CF trade-off：论文声称 CF 是 \"resolvable via beam search\"——证据是否充分（特别是 DocRED）？\n3. 统计显著性：bootstrap 检验设置是否合理？样本量是否足够？\n4. WikiEvents EE fine-tuning 仅 20 文档测试集——统计效力如何？\n5. DocRED beam search 零样本仅 50 文档子集——是否影响结论可靠性？\n6. 70B 评估仅为 \"preliminary\"——声称范围是否合理？\n7. Constraint tightness κ̄ 作为 \"descriptive metric\"——是否有足够的预测性证据支持其 deployment guidance 价值？\n\n### C. 实验公平性\n1. Baseline 选择是否充分？是否遗漏了最接近的 IE constrained decoding 基线（如 BoostCD、IterGen）？\n2. 与 GoLLIE 等 schema-aware IE 系统的对比是否公平？\n3. Post-hoc filtering 对比是否公平？\n\n### D. 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条 S1, S2, ...)\n3. **Weaknesses** (逐条 W1, W2, ... 区分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References**\n6. **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5, 按 EMNLP 2026 ARR 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit), Confidence (1-5)\n\n严格评审，不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 1328 · 2026-05-20T18:37:07.620224+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17513
}
```

</details>

---


### Tool call

_source line 1329 · 2026-05-20T18:37:07.921705+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- 目标 venue: EMNLP 2026（via ARR May cycle）\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 长文正文 ≤ 8 页，参考文献无限制\n- Limitations 必须有，不计入页数\n- ACL 模板，double-blind 审稿\n- 附录不要求审稿人审查\n\n## 你的审查侧重\n\n### A. 新颖性与贡献定位\n1. 与最接近工作（PICARD、IterGen、BoostCD、GoLLIE、GCD、DCCD）的技术区分是否清晰？\n2. \"Preventive forward-only masking\" vs \"corrective backtracking\" 的 novelty 论证是否站得住脚？\n3. 三个 contribution 是否都成立？是否有过度声称？\n4. κ̄ 作为 \"descriptive metric\" 的定位是否合适？是否被过度包装为 contribution？\n5. \"formally compiles\" 的声称——与 code generation 领域的 type-constrained decoding 有何本质区别？\n\n### B. Related Work 覆盖与定位\n1. 是否遗漏了重要的相关工作？特别是：\n   - IE-specific constrained decoding（BoostCD、IterGen、EnriCo、DCCD）\n   - Schema-aware IE（GoLLIE、KnowCoder、GUIDEX、InstructUIE）\n   - Constrained decoding 对推理的影响（CRANE、HiddenCost、FormatTax）\n2. 引用格式和完整性\n3. 自引比例是否合理？\n\n### C. 写作质量与清晰度\n1. Abstract 信息密度是否合适？关键 message 是否清晰？\n2. Introduction 的 motivation 是否 compelling？gap 论证是否充分？\n3. §3 Method 描述是否清晰？Figure 1 是否 informative？\n4. 实验结果叙述是否平衡？CF 代价是否在 Abstract/Introduction 中透明呈现？\n5. 命名一致性：S1/S2 命名是否清晰？术语是否前后一致？\n6. 模型规模声称（\"any autoregressive LM\" vs 实际仅 7-8B 主测试）是否准确？\n\n### D. 格式合规\n1. 正文是否 ≤ 8 页？（检查 Limitations 前的页数）\n2. 匿名性：是否有泄露作者身份的信息？\n3. 表格/图形是否清晰可读？字体是否过小？\n4. 引用格式是否正确？\n5. ARR Responsible NLP Research Checklist 是否存在？\n\n### E. 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条 S1, S2, ...)\n3. **Weaknesses** (逐条 W1, W2, ... 区分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References**\n6. **Scores**: Novelty (1-5), Clarity (1-5), Overall (1-5, 按 EMNLP 2026 ARR 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit), Confidence (1-5)\n\n严格评审，不留情面。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- 目标 venue: EMNLP 2026（via ARR May cycle）\n- Deadline: 2026-05-25\n\n## Venue 要求\n- 长文正文 ≤ 8 页，参考文献无限制\n- Limitations 必须有，不计入页数\n- ACL 模板，double-blind 审稿\n- 附录不要求审稿人审查\n\n## 你的审查侧重\n\n### A. 新颖性与贡献定位\n1. 与最接近工作（PICARD、IterGen、BoostCD、GoLLIE、GCD、DCCD）的技术区分是否清晰？\n2. \"Preventive forward-only masking\" vs \"corrective backtracking\" 的 novelty 论证是否站得住脚？\n3. 三个 contribution 是否都成立？是否有过度声称？\n4. κ̄ 作为 \"descriptive metric\" 的定位是否合适？是否被过度包装为 contribution？\n5. \"formally compiles\" 的声称——与 code generation 领域的 type-constrained decoding 有何本质区别？\n\n### B. Related Work 覆盖与定位\n1. 是否遗漏了重要的相关工作？特别是：\n   - IE-specific constrained decoding（BoostCD、IterGen、EnriCo、DCCD）\n   - Schema-aware IE（GoLLIE、KnowCoder、GUIDEX、InstructUIE）\n   - Constrained decoding 对推理的影响（CRANE、HiddenCost、FormatTax）\n2. 引用格式和完整性\n3. 自引比例是否合理？\n\n### C. 写作质量与清晰度\n1. Abstract 信息密度是否合适？关键 message 是否清晰？\n2. Introduction 的 motivation 是否 compelling？gap 论证是否充分？\n3. §3 Method 描述是否清晰？Figure 1 是否 informative？\n4. 实验结果叙述是否平衡？CF 代价是否在 Abstract/Introduction 中透明呈现？\n5. 命名一致性：S1/S2 命名是否清晰？术语是否前后一致？\n6. 模型规模声称（\"any autoregressive LM\" vs 实际仅 7-8B 主测试）是否准确？\n\n### D. 格式合规\n1. 正文是否 ≤ 8 页？（检查 Limitations 前的页数）\n2. 匿名性：是否有泄露作者身份的信息？\n3. 表格/图形是否清晰可读？字体是否过小？\n4. 引用格式是否正确？\n5. ARR Responsible NLP Research Checklist 是否存在？\n\n### E. 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条 S1, S2, ...)\n3. **Weaknesses** (逐条 W1, W2, ... 区分 Must-Fix / Should-Fix / Minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References**\n6. **Scores**: Novelty (1-5), Clarity (1-5), Overall (1-5, 按 EMNLP 2026 ARR 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit), Confidence (1-5)\n\n严格评审，不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 1330 · 2026-05-20T18:37:09.233953+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1312
}
```

</details>

---


### Assistant

_source line 1331 · 2026-05-20T18:37:15.010207+00:00_

Round 1 已启动，三线并行：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验有效性） | 已分配 |
| Reviewer 2（新颖性 + 完整性 + 写作质量） | 已分配 |
| 视觉审查 Agent | 已派发 |
| 外部审稿（Stanford Agentic Reviewer） | 未配置，跳过 |

等待两名 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 1332 · 2026-05-20T18:42:57.672251+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

## Summary

本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的分层架构：grammar layer（CFG）保证 JSON 结构和词汇约束，semantic layer（prefix-decidable with state）通过运行时 entity registry 执行 domain/range 类型约束。在 SciERC、DocRED、WikiEvents 上对 3–4 个模型（7–70B）进行了系统评估，表明 LoRA + S1 可将 DR 违规降至 ≤0.09%，R-F1 变化在 ±0.6pp 内。论文同时引入 constraint tightness κ̄ 作为描述性指标。

## Strengths

**S1. 系统性的实验设计与全面的消融分析。** 五路消融（Unconstrained / Grammar / Semantic / Full S1 / Full S2）清晰分离了各层贡献；跨三个数据集（RE + EE）、四个模型、三个 tokenizer 族的验证令人信服。Bootstrap 显著性检验（B=10,000）和配对统计比较体现了严谨的实验方法论。这是我见过的 constrained decoding for IE 领域最全面的评估之一。

**S2. 有 principled 的形式化分析支撑架构决策。** Proposition 1（domain/range 约束不是 CF 的）给出了两层架构的 formal justification，pumping lemma 证明（Appendix）是严格的。Enabling dependency 的概念——grammar layer 必须先保证词汇有效性，semantic layer 才能有效运作——在 Table 1 中得到了实验验证（Semantic-only 仅降 24% DR）。

**S3. 工程上的完整性和可部署性。** Tokenizer-agnostic continuation masking 处理了 BPE/SentencePiece 差异；grammar-first fallback 保证了 JSON 完整性；运行时开销适中（+10–13%）；编译时间 <0.5s。框架无需修改即可从 RE 扩展到 EE（WikiEvents，245 constraints），体现了良好的泛化设计。

**S4. Fine-tuning composability 是重要的实用价值。** Table 2 表明约束可以与 LoRA 组合使用而不损害 R-F1（p>0.05），将残余 DR 从 1–2% 压到 ≤0.09%。对于实际部署场景，这比零样本结果更具说服力。

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1 [critical] 正文超过 8 页限制。**
- 具体位置：Page 9（行号 650–660）
- 问题：Discussion and Conclusion 的最后约 11 行溢出到第 9 页。`\clearpage` 在 Limitations 之前（main.tex:68），Limitations 从第 10 页开始。EMNLP 2026 (via ARR) 严格限制长文正文 ≤ 8 页。
- 为什么影响接收：格式违规可能导致 desk reject 或被 AC 标记为不合规。
- 建议修改方向：压缩 §7 Discussion and Conclusion（当前约 120 词）、§6 Related Work、或 §5 实验叙述中的冗余描述（如 per-relation 细节可移至 Appendix），确保正文在第 8 页底部结束。

**W2 [critical] CF 代价在 Abstract 和 Introduction 中被系统性低估。**
- 具体位置：Abstract（"with modest cross-field (CF) costs resolvable via beam search"）; Introduction 无 CF 提及
- 问题：
  - 零样本 CF：SciERC 0.08%→9.90%（+123×），DocRED 0.10%→2.57%（Table 1, 3）
  - WikiEvents CF：15–21%（Table 5）——极高
  - Fine-tuned CF：0→1.18%（Table 2）——虽小但非零
  - Abstract 用 "modest" 描述 9.90% 的 CF 率是误导性的。WikiEvents 的 15–21% CF 更无法称为 modest。
- 为什么影响接收：审稿人和读者依赖 Abstract/Introduction 判断方法的 trade-off profile。隐藏主要副作用降低了论文的可信度。
- 建议修改方向：Abstract 应明确写出 CF 范围（例如 "with CF trade-offs of up to X% under zero-shot, reduced to Y% with fine-tuning or beam search"）。Introduction 应有一段讨论 DR↔CF trade-off。

**W3 [critical] κ̄ 作为独立贡献（Contribution 2）的定位过高。**
- 具体位置：§1 Contribution 2; §4 Eq. (3)
- 问题：κ̄ = 1 − |σ(r)|/|E|² 本质上是约束表的归一化密度。论文自身承认 "κ is necessary but not sufficient—entity type confusability is the critical co-factor"（§4）。一个需要额外协变量才能有意义的描述统计量，不应作为独立 contribution 列出。
  - κ̄ 只在两个数据集上验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842），这是两个数据点的相关性——不足以支撑 "deployment guidance" 的声称。
  - κ̄ 没有预测能力：Mistral 在 SciERC（κ̄=0.333）上 DR 降幅仅 76%，而 Qwen/Llama 达 94–99%（Table 4），说明 κ̄ 无法独立预测 enforcement 效果。
- 为什么影响接收：将简单描述统计包装为 contribution 会被审稿人视为 overclaiming。
- 建议修改方向：将 κ̄ 降级为分析工具（analysis tool），整合入实验讨论而非单独列为 contribution。或提供更多数据集的 κ̄ 值来验证其泛化性。

### Should-Fix 问题（影响评分但不一票否决）

**W4 [warning] "any autoregressive LM" 声称与实际验证范围不符。**
- 具体位置：§1（"applies to any autoregressive LM"）、Abstract（"validated primarily on 7–8B parameter models"）
- 问题：主要实验在 7–8B 模型上完成；70B 仅有初步结果（§5.5, SciERC + DocRED 各一个模型）；无小模型（<7B）验证；无 API-only 模型验证（Limitations 承认排除 GPT-4/Claude）。"any autoregressive LM" 的声称未经充分验证。
- 建议：改为 "applies to autoregressive LMs with logit access" 或 "validated on 7–70B parameter models"。

**W5 [warning] DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%），论文对此差异的讨论不充分。**
- 具体位置：Table 3, §5.2
- 问题：论文将此归因于 κ̄ 差异（0.333 vs 0.842），但这只是 restate 了问题（κ̄ 高→fallback 多→DR 高→κ̄ 相关）。更深层的问题是：对于 tight schema（实际应用中常见），零样本约束的 DR elimination 能力有限。论文没有讨论这对方法的实用性意味着什么。
  - 残余 DR 10.21% 意味着每 10 个 triple 仍有 1 个类型违规，这对 "type-safe extraction" 的目标构成挑战。
- 建议：在正文中明确讨论 tight-schema 场景下的局限性，而非仅在 Limitations 中提及。

**W6 [warning] WikiEvents 评估的局限性未充分说明。**
- 具体位置：§5.4, Table 5
- 问题：
  - Fine-tuning composability 基于 20-document test set，CIs 很宽（±0.05–0.06 for trigger F1），统计功效不足。
  - 零样本 entity F1=0（unconstrained）→12–18%（constrained）——这说明无约束时 parser 完全无法处理输出，而非约束改善了 extraction 质量。F1 提升主要来自格式修复而非语义改善。
  - Grammar-only 行缺少 F1 数据（"---"），但 Table caption 没有充分解释原因。
- 建议：承认 WikiEvents 结果是 preliminary，且 F1 提升的来源是格式合规而非 extraction 能力。

**W7 [warning] "formally compiles" 的表述与 code generation 领域的 type-constrained decoding 技术区分不够清晰。**
- 具体位置：Abstract、§1、§6
- 问题：§6 第二段确实讨论了与 PICARD 和 Mündler et al. (2025) 的区别——IE 的 entity registry 是动态构建的，而代码生成的类型环境在编译时完全已知。但 "formally compiles" 这个术语暗示了超出实际贡献的理论深度。实际实现是：(1) 从 ontology 生成 JSON Schema + enum constraints 交给 XGrammar，(2) 构建一个 stateful logit processor 做 type masking。这更接近 "automatic constraint generation" 而非 PL 意义上的 "compilation"。
- 建议：可以保留 "compile" 用于框架描述，但避免在贡献声称中过度使用 "formally compiles"。

### Minor 问题（不影响接收）

**M1.** 孤立 bib entry：`schmidt2025grammar`（在 .bib 中但未被任何 .tex 文件引用）。

**M2.** 表格字体偏小：Table 1, 3, 4 使用 `\resizebox{\columnwidth}` 压缩了 8+ 列表格，打印时可读性可能受影响。

**M3.** S1/S2 命名不够直观。第一次出现时（§3.4）应在括号内给出描述性名称，后续可以用 "single-pass S1" / "two-pass S2" 保持一致。当前正文中混用 "S1 (joint extraction)" 和 "Full (S1)"。

**M4.** §4 Constraint Tightness 的脚注 1 说 "for symmetric relations, |σ(r)| counts ordered pairs"——这个处理选择应该在正文中讨论而非藏在脚注里，因为它影响 κ̄ 的计算。

**M5.** 引用验证发现 `formattax2026` 和 `regino2025kgcurator` 在 OpenAlex 中未找到匹配（可能是极新论文），建议确认这两篇引用的完整性。

## Questions（需要作者澄清）

**Q1.** Grammar-first fallback 触发时，semantic layer 完全放弃约束。论文报告 fallback 在 36.6% 的 type-bearing positions 触发（§4, SciERC 零样本）。这是否意味着约三分之一的类型位置实际上没有任何类型约束？如果是，"type-constrained extraction" 的标题是否过度承诺？

**Q2.** Table 2 显示 Llama SciERC fine-tuned DR 从 1.11% 降至 0.09%（而非 0%），但 Qwen 达到 0%。Llama 残余 0.09% 的 36 个违规分解（entity type errors 39%, schema coverage gaps 33%, model errors 28%——来自 Limitations）是否意味着约束的有效性受限于 schema coverage？如果 training data 的类型对覆盖不全（33% 的残余违规来源），这对新领域的部署有何影响？

**Q3.** Beam search（k=4）在 SciERC LoRA 上消除了所有违规。但 DocRED 零样本 beam 仅在 50-document subset 上评估（§5.5）。为什么不在完整 998-document set 上运行？"compute cost" 是否意味着 beam search 在大规模 schema（96 relations）上不实用？

**Q4.** WikiEvents 的 Grammar-only 行在 Table 5 中 F1 标记为 "---"（"not applicable"），但 grammar-only 模式应该可以生成结构化输出并计算 F1。是因为 RoV 仍高达 64–77% 导致无法可靠评估吗？这需要更清晰的解释。

**Q5.** 论文声称 "extraction tasks are robust to format constraints" 引用 Tam et al. (2024)，但 Tam et al. 的实验是在 general NLP tasks 上而非 IE-specific tasks 上。是否有 IE-specific 的证据表明 constrained decoding 不损害 extraction reasoning？CRANE (Banerjee et al., 2025) 的发现暗示即使在结构化任务中，constrained decoding 也可能有隐性代价。

## Missing References

论文的 related work 覆盖总体较好。可能遗漏：

1. **Fei et al. (2022)** "LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model"——结构化生成 + IE 的早期工作。
2. 论文未讨论 **closed-book vs open-book** 约束设置的区别：OntoCoDec 的约束表从 training data 提取，这与 formal ontology 驱动的方法有本质区别（coverage gap 问题）。

## Scores

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 技术方法正确，形式化分析严格，实验设计全面；但 CF 代价被低估，κ̄ 验证不充分（仅 2 个数据点），DocRED 零样本 DR 降幅有限 |
| Excitement | 2.5/5 | 解决了真实问题（IE 类型违规），但核心机制（logit masking at type positions + entity registry）是已有技术的自然组合；decidability analysis 形式化了直觉但未带来新 insight |
| Reproducibility | 4/5 | 实验细节充分（prompt templates in Appendix, hyperparameters, bootstrap settings），承诺代码发布；但部分评估依赖特定 XGrammar 版本 |
| Overall | 3.0/5 | **Findings 级别**。技术扎实，评估全面，但新颖性有限（constrained decoding + stateful masking 的组合）；κ̄ contribution 过度包装；CF 代价透明度不足；正文超页（must-fix format violation） |
| Confidence | 4/5 | 熟悉 constrained decoding、structured generation 和 IE 领域 |

### 自定义维度

| 维度 | 分数 | 理由 |
|------|------|------|
| Novelty | 2.5/5 | 两层架构的 decidability justification 是新的形式化贡献，但核心机制（grammar mask ∩ semantic mask）是已有思路的工程化实现 |
| Clarity | 3.5/5 | 方法描述清晰，实验组织良好；但 CF 代价的呈现方式（buried in tables, "modest" in abstract）损害了透明度 |

### 一句话总结

一篇技术扎实、评估全面的系统论文，但核心新颖性有限（constrained decoding for IE 的 principled engineering），且 CF 代价透明度和 κ̄ contribution 定位存在显著问题。


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

_source line 1333 · 2026-05-20T18:43:06.454987+00:00_

Reviewer 2 审稿意见已收到。关键发现：Overall 3.0/5（Findings 级别），3 个 Must-Fix（正文超页、CF 低估、κ̄ 过度包装），4 个 Should-Fix，5 个 Minor。等待 Reviewer 1 回复后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 93

## Round 93

2 recorded events


### User

_source line 1334 · 2026-05-20T18:43:19.536995+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0/5（Findings 级别）**

核心发现：
- **3 个 Must-Fix**：正文超 8 页限制（~11 行溢出到第 9 页）；Abstract/Introduction 系统性低估 CF 代价（零样本 SciERC 9.90%、WikiEvents 15–21%，用 "modest" 描述是误导）；κ̄ 作为独立 Contribution 定位过高（仅 2 个数据点的描述统计量）
- **4 个 Should-Fix**：`any autoregressive LM` 声称超出验证范围；DocRED 零样本 DR 降幅仅 45% 的讨论不充分；WikiEvents 评估统计功效不足（20-doc test set）；"formally compiles" 措辞与实际技术贡献不匹配
- **优势**：实验设计是该领域最全面的之一（5-way ablation × 3 datasets × 4 models × bootstrap）；decidability analysis 给出了 principled 的架构 justification；fine-tuning composability 有实用部署价值

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

_source line 1335 · 2026-05-20T18:43:27.929002+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 94

## Round 94

6 recorded events


### User

_source line 1336 · 2026-05-20T18:44:59.958567+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

## Summary

本文提出 OntoCoDec，一个将 IE 本体编译为 token 级约束的框架，用于自回归 LLM 生成时的类型约束执行。系统采用双层架构：grammar layer（EBNF + XGrammar，执行 JSON 结构和词汇约束）和 semantic layer（有状态 logits processor，维护实体注册表执行 domain/range 类型约束）。论文提出三级 decidability taxonomy（context-free / prefixes-decidable / non-local），用 pumping lemma 证明 Level 2 约束非 context-free，并在 SciERC、DocRED、WikiEvents 三个数据集上用 4 个模型（7-8B 规模为主）验证约束执行效果。

## Strengths

**S1.** 三级 decidability taxonomy 是本文最突出的理论贡献。将 IE 类型约束按可判定性分层（Level 1: context-free 可用 PDA 执行；Level 2: prefixes-decidable 需有状态转换器；Level 3: non-local 不可在 token 级执行）的框架清晰、well-motivated，为后续研究提供了有用的分析工具。分类边界通过形式化分析建立，不是 ad hoc 的。

**S2.** 双层架构设计干净，grammar 与 semantic 层的关注点分离（structural validity vs. type validity）优雅地匹配了 decidability taxonomy 的前两级。Grammar-first fallback（§4）是合理的设计选择：当两层冲突时优先保证 JSON 结构完整性，CF 率作为代价指标被诚实地报告和分析。

**S3.** 消融实验设计细致。Table 1（SciERC 五路消融）有效隔离了各约束类型（RV、ET、CF、DR）的贡献：Full S1 将 DR 从 15.37% 降至 0.93%，R-F1 基本不变（±0.06 pp），证明约束执行不损害提取质量。Table 2（DocRED fine-tuning 四路消融）进一步在 2 模型 × 2 数据集 × full S1 上验证了一致性。

**S4.** 诚实的 limitation 讨论。论文明确承认 CF 的模型依赖性、WikiEvents 的初步性质、70B 评估的有限性，以及 κ̄ 仅为描述性指标。这种自我批评意识在投稿论文中值得肯定。

**S5.** 附录内容极其丰富（23 页），包括完整的 pumping lemma 证明（Appendix O）、per-relation 违规分析（Appendix D）、beam search 兼容性（Appendix F）、prompt sensitivity（Appendix I）、错误案例分析（Appendix J）、post-hoc type consistency resolution（Appendix M）等。这体现了扎实的研究工作。

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1. [critical] 缺少最直接可比的 constrained decoding baseline 对比**
- 具体位置：Section 5, Section 6 (Related Work)
- 问题：论文在 Related Work（Section 6, page 8）明确引用了 BoostCD (Sakota et al., 2025) 和 IterGen (Ugare et al., 2025) 这两个最接近的系统——前者将 constrained 和 unconstrained decoding 通过 boosting 结合并**专门应用于 IE**，后者实现了 iterative semantic-aware structured generation with backtracking。然而实验中**完全没有与它们对比**，仅与 unconstrained、grammar-only、post-hoc filtering 对比。
- 为什么影响接收：如果 BoostCD 或 IterGen 在相同 benchmark 上能达到类似的类型约束执行效果（或更好的 F1），OntoCoDec 的增量贡献将大幅缩水。BoostCD 发表于 EMNLP 2025，专门做 IE constrained decoding，是最自然的 baseline。论文将它们定位为"不同方法"（boosting vs. compilation）但这恰恰需要实验验证而非定性陈述。
- 建议：在 SciERC 和 DocRED 上至少复现 BoostCD 的 zero-shot 设置进行对比。如果因为实现原因无法复现，需要明确讨论为什么不可比，并引用这些系统报告的相关数字进行间接对比。

**W2. [critical] WikiEvents EE 评估统计效力严重不足**
- 具体位置：Section 5.4, Table 5 (page 7)
- 问题：WikiEvents 测试集仅 20 篇文档（194/20/20 split，per Li et al., 2021）。论文报告 R-F1 with ±1.1 pp 95% CI，但在如此小的样本上：(a) 置信区间实际上可能被低估（bootstrap 在小样本上的覆盖率偏低）；(b) 论文仍从中得出 EE 泛化性结论（"The framework generalizes to event extraction with 245 constraints across three tokenizer families"，page 2, Contribution 3），这个 claim 的证据基础太薄弱。
- 为什么影响接收：Contribution 3 明确将 WikiEvents EE 列为三大贡献之一（"systematic evaluation of type constraint enforcement in LM-based IE: the first evaluation...extends to event extraction"），但 20 篇文档的测试集无法支撑"systematic evaluation"的措辞。
- 建议：(a) 在 Contribution 3 中明确限定 EE 结果为"preliminary demonstration"而非"systematic evaluation"；(b) 讨论统计效力限制（effect size 需要多大才能在 n=20 下被检测到）；(c) 如果可能，补充更大规模 EE 数据集的结果。

### Should-Fix 问题（影响评分但不一票否决）

**W3. [warning] Pumping lemma 证明的形式化与实际系统存在 gap**
- 具体位置：Appendix O (pages 32-33), Proposition 1 (page 3)
- 问题：Appendix O 的证明构造了一个语言 L，其中类型合法性依赖于跨位置的实体-关系引用关系。证明的核心论点——PDA 的 LIFO stack 无法追踪实体位置与关系 head/tail 类型字段的跨位置依赖——是正确的。但证明存在一个形式化 gap：它假设实体引用是基于**位置索引**的（pumping 改变位置导致引用错误），而实际的 JSON 输出格式使用**实体名称**（字符串引用）。在名称引用下，pumping 一个实体条目不会改变其他实体的名称引用，但会改变实体注册表中的类型绑定。证明应更明确地说明：非 CF 性来源于"实体名称到类型的绑定"在串行生成中的跨位置依赖，而不仅是位置索引的偏移。
- 建议：在证明中增加一段说明，将形式语言的字符串结构与实际 JSON 格式的对应关系明确化，特别是解释为什么名称引用下 pumping 仍然破坏类型一致性。

**W4. [warning] DocRED beam search 仅用 50 文档子集评估**
- 具体位置：Section 5.2, Table 3 footnote (page 6), Appendix F (page 25-26)
- 问题：DocRED 的 beam search zero-shot 评估仅用 50 文档子集（998 文档中的 5%），论文解释为"due to extended generation under high-temperature sampling with complex schema"。然而论文的关键 claim 之一是"CF is resolvable via beam search"（Abstract, Section 5），这个 claim 在 DocRED 上的证据基础仅为 5% 子集。Table 15（Appendix F）显示 beam search 在 DocRED 上的 CF 从 28.4% 降至 21.4%，远未"resolve"。
- 建议：(a) 在 Abstract 和 Section 5 中限定 beam search 的 CF resolution claim（"substantially reduces" 而非 "resolves"）；(b) 明确报告 50-document 子集与全集的分布差异分析。

**W5. [warning] "Formally compiles" 措辞过度**
- 具体位置：Abstract ("formally compiles"), Section 3 ("OntoCoDec compiles"), Section 7
- 问题：Grammar layer 确实是编译（ontology → EBNF grammar → PDA），符合 PL 传统意义上的 compilation。但 semantic layer 是**运行时规则解释**（runtime rule-based masking via stateful logits processor），不是传统意义上的编译。"Compile" 隐含着离线、静态的转换过程，而 semantic layer 的实体注册表是在生成过程中动态维护的。
- 建议：区分两层的"编译"性质——grammar layer 是 ahead-of-time compilation，semantic layer 是 rule-based runtime enforcement derived from the ontology。或使用更准确的术语如 "translates IE ontologies into composable token-level constraints"。

**W6. [warning] 与 GoLLIE 等 schema-aware IE 系统缺乏量化对比**
- 具体位置：Section 6 (page 8)
- 问题：论文将 GoLLIE (Sainz et al., 2024)、KnowCoder (Li et al., 2024) 等 training-based schema-aware IE 系统定位为"complementary rather than competing"。这个定位在概念上合理（decoding-time enforcement vs. training-time schema awareness），但读者仍然需要知道：在相同 benchmark（如 SciERC zero-shot）上，OntoCoDec + unconstrained LLM 与 GoLLIE 的 F1 差距是多少？如果 GoLLIE 的 F1 远高于 OntoCoDec，那么"complementary"的说法需要更具体地解释 complementary 的价值。
- 建议：在 Related Work 或 Discussion 中引用 GoLLIE 在 SciERC/DocRED 上的报告数字，进行间接对比，并讨论 OntoCoDec 在 GoLLIE 之上是否能提供额外收益。

**W7. [warning] κ̄ 部署指导的证据不足**
- 具体位置：Section 4 (Eq. 3), Appendix N (page 32)
- 问题：κ̄ 被提议为部署指导的描述性指标（"descriptive metric correlating schema restrictiveness with enforcement outcomes"）。但实证支撑仅来自 2 个数据集（SciERC κ̄=0.333 vs. DocRED κ̄=0.812），样本量极小。且 κ̄ 与 DR 的关系受模型、fine-tuning 状态、beam search 等多因素影响，仅凭 2 个点无法建立有意义的预测关系。
- 建议：(a) 更明确地标记 κ̄ 为 exploratory/preliminary metric；(b) 如果可能，增加更多不同 κ̄ 值的数据集/子集点；(c) 讨论 κ̄ 与其他因素（模型能力、fine-tuning 状态）的交互作用。

### Minor 问题（不影响接收）

**M1.** 主体文本似乎略超 8 页：Section 7 结论延伸至 page 9 约 10 行（lines 650-660）。建议检查是否严格符合 EMNLP 2026 的 8 页限制。

**M2.** Table 密度极高（主体 5 张表 + 附录 20+ 张表），部分主体表格（如 Table 4 的 cross-model zero-shot）信息密度可以通过图表更好地传达。

**M3.** "Best-effort pair-based enforcement"（Section 3.3）的精确含义可以更明确定义：(a) 当 head 位置的类型在 head 生成时尚不能确定（如 GENERIC 类型歧义），fallback 行为是什么？(b) 是否存在 head 类型 ambiguity 导致错误 tail 类型约束的 corner case？附录 J 的错误分析部分涵盖了这些情况但主体文本应更明确。

**M4.** 引用审计发现：1 个 orphan bib entry（schmidt2025grammar，在 .bib 中但未被引用）；2 篇论文在 OpenAlex 中未找到（regino2025kgcurator, formattax2026），可能是非常新的 preprint；8 个 minor author name mismatches（多为 unicode/格式差异，不影响正确性）。

**M5.** Grammar-first fallback 的级联失败分析：如果 grammar mask 也为空集（G(t) = ∅），系统行为如何？虽然理论上 grammar 层保证至少有合法 JSON 延续，但在极端 tokenizer edge case（如 rare byte-level tokens）下是否有保障？论文未讨论。

## Questions（需要作者澄清）

**Q1.** Proposition 1 的证明（Appendix O）中，pumping 操作具体如何破坏名称引用下的类型一致性？如果实体名称是唯一的，pump 一个新的实体条目后，关系引用的实体名称仍然存在于输出中，只是其位置变了。类型绑定是由名称到类型的映射决定的，不依赖位置。请澄清证明中"位置偏移导致类型违规"的推理如何适用于名称引用格式。

**Q2.** BoostCD (Sakota et al., 2025) 在 SciERC 和 DocRED 上报告的 constrained decoding 结果是什么？如果作者认为 BoostCD 不可比，请解释具体原因（是约束类型不同、输出格式不同、还是其他原因）。

**Q3.** 论文的 grammar-first fallback 在 DocRED 上的 CF 率（fallback 频率）相当高（zero-shot: ~9.90%）。这意味着约 10% 的解码步骤中 semantic layer 被跳过。这些被跳过的位置是否集中在特定类型的 relation（如高 κ 的 relation）？是否存在某些 relation 类型的约束实际上从未被有效执行？

**Q4.** Fine-tuning（LoRA）的 composability 实验（Table 2）中，LoRA 是在**有**约束解码的条件下训练的，还是在**无**约束解码的条件下训练的？如果是无约束训练，那么 fine-tuned 模型的输出分布与 constrained decoding 的 mask 之间可能存在 distribution mismatch。如果是有约束训练，请说明训练时的约束配置。

**Q5.** Semantic layer 的实体注册表（entity registry）在生成过程中动态维护，这意味着实体的注册顺序可能影响后续关系的约束执行。如果 LLM 先生成了一个 GENERIC 类型的实体，后续所有引用该实体的关系都会受到 GENERIC 歧义的影响。论文是否分析过实体生成顺序对最终约束执行效果的影响？

## Missing References

1. **GENRE** (De Cao et al., 2021) 虽已引用，但 **GenIE** (Josifoski et al., 2022) 作为最早将 constrained decoding 系统化应用于 IE 的工作之一，在主体 Related Work 中被遗漏（仅在附录 B 中出现），应在主体中提及。
2. 论文未引用 **NNF** (Nusgart et al., 2025, "Constrained Decoding with Grammars and Lookahead") 等关于 grammar-constrained decoding lookahead 的最新工作，与本文的 grammar-first fallback 机制相关。

## Scores

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 形式化框架合理但 pumping lemma 证明与实际格式存在 gap；实验方法论整体可靠但 WikiEvents (n=20) 和 DocRED beam search (n=50) 统计效力不足 |
| Excitement | 3/5 | Decidability taxonomy 是有用的理论贡献，双层架构设计干净；但实际影响受限于评估规模（7-8B 为主）和缺乏与最接近 baseline 的对比 |
| Overall | 3.5/5 | Borderline Conference。核心贡献（decidability taxonomy + 双层编译约束执行）扎实且有新意；实验评估全面但有关键缺陷（missing baselines、统计效力）。修订后（补充 BoostCD/IterGen 对比、增强形式化、限定 claims 范围）有望达到 Conference 水平 |
| Confidence | 4/5 | 对 constrained decoding 和 IE 有研究经验，仔细阅读了全文含 33 页附录 |
| Reproducibility | 4/5 | 实验设置详细（Appendix A/G），prompt templates 公开（Table 6），bootstrap 参数报告，但代码未提交 |

**Overall Assessment: 3.5** — Borderline Conference

**一句话总结**：一篇理论动机清晰、系统设计干净的约束解码论文，但缺少与最直接可比系统（BoostCD、IterGen）的实验对比，且部分实验的统计效力不足以支撑其 claim 的范围。


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

_source line 1337 · 2026-05-20T18:45:48.814239+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的分层架构：grammar layer（CFG）保证 JSON 结构和词汇约束，semantic layer（prefix-decidable with state）通过运行时 entity registry 执行 domain/range 类型约束。在 SciERC、DocRED、WikiEvents 上对 3–4 个模型（7–70B）进行了系统评估，表明 LoRA + S1 可将 DR 违规降至 ≤0.09%，R-F1 变化在 ±0.6pp 内。论文同时引入 constraint tightness κ̄ 作为描述性指标。\n\n### Must-Fix\n\n**W1 [critical] 正文超过 8 页限制。**\nDiscussion and Conclusion 的最后约 11 行溢出到第 9 页。EMNLP 2026 (via ARR) 严格限制长文正文 ≤ 8 页。格式违规可能导致 desk reject。\n\n**W2 [critical] CF 代价在 Abstract 和 Introduction 中被系统性低估。**\nAbstract 用 \"modest\" 描述零样本 SciERC 9.90% 和 WikiEvents 15–21% 的 CF 率是误导性的。Introduction 完全没提 CF。隐藏主要副作用降低论文可信度。\n\n**W3 [critical] κ̄ 作为独立贡献（Contribution 2）的定位过高。**\nκ̄ = 1 − |σ(r)|/|E|² 本质上是约束表的归一化密度。仅在 2 个数据集上验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842），且 κ̄ 无法独立预测 enforcement 效果（Mistral SciERC DR 降幅仅 76% vs Qwen/Llama 94–99%）。\n\n### Should-Fix\n\n**W4 [warning] \"any autoregressive LM\" 声称与实际验证范围不符。**\n主要实验在 7–8B 模型上，70B 仅初步结果，无小模型/API-only 验证。\n\n**W5 [warning] DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%），讨论不充分。**\n论文将此归因于 κ̄ 差异，但这只是 restate 了问题。残余 DR 10.21% 对 \"type-safe extraction\" 目标构成挑战。\n\n**W6 [warning] WikiEvents 评估局限性。**\nFine-tuning 基于 20-doc test set，CIs 很宽。零样本 entity F1 从 0→12-18% 主要来自格式修复而非语义改善。Grammar-only 行缺少 F1。\n\n**W7 [warning] \"formally compiles\" 措辞与实际技术贡献不匹配。**\nGrammar layer 是编译，但 semantic layer 是运行时规则解释。\"Compile\" 隐含离线、静态转换，与 semantic layer 的动态维护不符。\n\n### Minor\n**M1.** 孤立 bib entry（schmidt2025grammar）\n**M2.** 表格字体偏小（Table 1, 3, 4）\n**M3.** S1/S2 命名不直观，混用 \"S1 (joint extraction)\" 和 \"Full (S1)\"\n**M4.** §4 脚注 1 关于对称 relation 的处理应在正文讨论\n**M5.** formattax2026 和 regino2025kgcurator 在 OpenAlex 未找到\n\n### Scores\nSoundness 3.5/5, Excitement 2.5/5, Overall 3.0/5 (Findings), Confidence 4/5, Novelty 2.5/5, Clarity 3.5/5\n\n---\n\n请逐条回应，特别关注：\n1. 你是否同意正文超页是 must-fix？\n2. 你是否同意 CF 代价被低估？R2 认为 \"modest\" 描述 9.90% CF 是误导——你的判断？\n3. R2 给 Excitement 2.5/5 vs 你给 3/5——分歧在哪？\n4. R2 的 Overall 3.0 vs 你的 3.5——你认为差距的核心原因是什么？"
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
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的分层架构：grammar layer（CFG）保证 JSON 结构和词汇约束，semantic layer（prefix-decidable with state）通过运行时 entity registry 执行 domain/range 类型约束。在 SciERC、DocRED、WikiEvents 上对 3–4 个模型（7–70B）进行了系统评估，表明 LoRA + S1 可将 DR 违规降至 ≤0.09%，R-F1 变化在 ±0.6pp 内。论文同时引入 constraint tightness κ̄ 作为描述性指标。\n\n### Must-Fix\n\n**W1 [critical] 正文超过 8 页限制。**\nDiscussion and Conclusion 的最后约 11 行溢出到第 9 页。EMNLP 2026 (via ARR) 严格限制长文正文 ≤ 8 页。格式违规可能导致 desk reject。\n\n**W2 [critical] CF 代价在 Abstract 和 Introduction 中被系统性低估。**\nAbstract 用 \"modest\" 描述零样本 SciERC 9.90% 和 WikiEvents 15–21% 的 CF 率是误导性的。Introduction 完全没提 CF。隐藏主要副作用降低论文可信度。\n\n**W3 [critical] κ̄ 作为独立贡献（Contribution 2）的定位过高。**\nκ̄ = 1 − |σ(r)|/|E|² 本质上是约束表的归一化密度。仅在 2 个数据集上验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842），且 κ̄ 无法独立预测 enforcement 效果（Mistral SciERC DR 降幅仅 76% vs Qwen/Llama 94–99%）。\n\n### Should-Fix\n\n**W4 [warning] \"any autoregressive LM\" 声称与实际验证范围不符。**\n主要实验在 7–8B 模型上，70B 仅初步结果，无小模型/API-only 验证。\n\n**W5 [warning] DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%），讨论不充分。**\n论文将此归因于 κ̄ 差异，但这只是 restate 了问题。残余 DR 10.21% 对 \"type-safe extraction\" 目标构成挑战。\n\n**W6 [warning] WikiEvents 评估局限性。**\nFine-tuning 基于 20-doc test set，CIs 很宽。零样本 entity F1 从 0→12-18% 主要来自格式修复而非语义改善。Grammar-only 行缺少 F1。\n\n**W7 [warning] \"formally compiles\" 措辞与实际技术贡献不匹配。**\nGrammar layer 是编译，但 semantic layer 是运行时规则解释。\"Compile\" 隐含离线、静态转换，与 semantic layer 的动态维护不符。\n\n### Minor\n**M1.** 孤立 bib entry（schmidt2025grammar）\n**M2.** 表格字体偏小（Table 1, 3, 4）\n**M3.** S1/S2 命名不直观，混用 \"S1 (joint extraction)\" 和 \"Full (S1)\"\n**M4.** §4 脚注 1 关于对称 relation 的处理应在正文讨论\n**M5.** formattax2026 和 regino2025kgcurator 在 OpenAlex 未找到\n\n### Scores\nSoundness 3.5/5, Excitement 2.5/5, Overall 3.0/5 (Findings), Confidence 4/5, Novelty 2.5/5, Clarity 3.5/5\n\n---\n\n请逐条回应，特别关注：\n1. 你是否同意正文超页是 must-fix？\n2. 你是否同意 CF 代价被低估？R2 认为 \"modest\" 描述 9.90% CF 是误导——你的判断？\n3. R2 给 Excitement 2.5/5 vs 你给 3/5——分歧在哪？\n4. R2 的 Overall 3.0 vs 你的 3.5——你认为差距的核心原因是什么？"
  }
}
```

</details>

---


### Tool result

_source line 1338 · 2026-05-20T18:46:07.406578+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18592
}
```

</details>

---


### Tool call

_source line 1339 · 2026-05-20T18:46:07.708201+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级约束的框架。系统采用双层架构：grammar layer（EBNF + XGrammar）和 semantic layer（有状态 logits processor）。论文提出三级 decidability taxonomy，用 pumping lemma 证明 Level 2 约束非 context-free，并在 SciERC、DocRED、WikiEvents 三个数据集上用 4 个模型验证。\n\n### Must-Fix\n\n**W1. [critical] 缺少最直接可比的 constrained decoding baseline 对比**\nBoostCD (Sakota et al., 2025) 和 IterGen (Ugare et al., 2025) 在 Related Work 中被引用但实验中完全没有对比。BoostCD 发表于 EMNLP 2025，专门做 IE constrained decoding，是最自然的 baseline。如果它们在相同 benchmark 上能达到类似效果，OntoCoDec 的增量贡献将大幅缩水。\n\n**W2. [critical] WikiEvents EE 评估统计效力严重不足**\nWikiEvents 测试集仅 20 篇文档。Contribution 3 将 WikiEvents EE 列为三大贡献之一（\"systematic evaluation\"），但 20 篇文档无法支撑此措辞。建议限定为 \"preliminary demonstration\"。\n\n### Should-Fix\n\n**W3. [warning] Pumping lemma 证明的形式化与实际系统存在 gap**\n证明假设实体引用基于位置索引，而实际 JSON 使用实体名称（字符串引用）。在名称引用下 pumping 的破坏机制需要更明确说明。\n\n**W4. [warning] DocRED beam search 仅用 50 文档子集评估**\n关键 claim \"CF is resolvable via beam search\" 在 DocRED 上的证据基础仅为 5% 子集。Table 15（Appendix F）显示 DocRED beam CF 从 28.4%→21.4%，远未 \"resolve\"。\n\n**W5. [warning] \"Formally compiles\" 措辞过度**\nGrammar layer 是编译，但 semantic layer 是运行时规则解释。\n\n**W6. [warning] 与 GoLLIE 等 schema-aware IE 系统缺乏量化对比**\n读者需要知道 OntoCoDec + unconstrained LLM 与 GoLLIE 的 F1 差距。\n\n**W7. [warning] κ̄ 部署指导的证据不足**\n仅 2 个数据集，样本量极小，无法建立有意义的预测关系。\n\n### Minor\n**M1.** 主文似超 8 页（Section 7 延伸至 page 9 约 10 行）\n**M2.** Table 密度极高，部分可用图表替代\n**M3.** \"Best-effort pair-based enforcement\" 精确含义可更明确\n**M4.** 1 orphan bib entry, 2 篇在 OpenAlex 未找到\n**M5.** Grammar-first fallback 的极端情况（G(t)=∅）未讨论\n\n### Scores\nSoundness 3.5/5, Excitement 3/5, Overall 3.5/5 (Borderline Conference), Confidence 4/5, Reproducibility 4/5\n\n---\n\n请逐条回应，特别关注：\n1. 你是否同意 BoostCD/IterGen 缺失对比是 must-fix？你此前未将此列为 must-fix，而是 should-fix (你的 W5)——为什么？\n2. R1 对 pumping lemma 的形式化 gap 分析（位置索引 vs 名称引用）——你是否同意这是一个问题？\n3. R1 给 Overall 3.5 vs 你给 3.0——分歧在哪？你认为差距的核心原因是什么？\n4. R1 给 Excitement 3/5 vs 你给 2.5/5——decidability taxonomy 的理论价值是否被你低估了？"
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
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级约束的框架。系统采用双层架构：grammar layer（EBNF + XGrammar）和 semantic layer（有状态 logits processor）。论文提出三级 decidability taxonomy，用 pumping lemma 证明 Level 2 约束非 context-free，并在 SciERC、DocRED、WikiEvents 三个数据集上用 4 个模型验证。\n\n### Must-Fix\n\n**W1. [critical] 缺少最直接可比的 constrained decoding baseline 对比**\nBoostCD (Sakota et al., 2025) 和 IterGen (Ugare et al., 2025) 在 Related Work 中被引用但实验中完全没有对比。BoostCD 发表于 EMNLP 2025，专门做 IE constrained decoding，是最自然的 baseline。如果它们在相同 benchmark 上能达到类似效果，OntoCoDec 的增量贡献将大幅缩水。\n\n**W2. [critical] WikiEvents EE 评估统计效力严重不足**\nWikiEvents 测试集仅 20 篇文档。Contribution 3 将 WikiEvents EE 列为三大贡献之一（\"systematic evaluation\"），但 20 篇文档无法支撑此措辞。建议限定为 \"preliminary demonstration\"。\n\n### Should-Fix\n\n**W3. [warning] Pumping lemma 证明的形式化与实际系统存在 gap**\n证明假设实体引用基于位置索引，而实际 JSON 使用实体名称（字符串引用）。在名称引用下 pumping 的破坏机制需要更明确说明。\n\n**W4. [warning] DocRED beam search 仅用 50 文档子集评估**\n关键 claim \"CF is resolvable via beam search\" 在 DocRED 上的证据基础仅为 5% 子集。Table 15（Appendix F）显示 DocRED beam CF 从 28.4%→21.4%，远未 \"resolve\"。\n\n**W5. [warning] \"Formally compiles\" 措辞过度**\nGrammar layer 是编译，但 semantic layer 是运行时规则解释。\n\n**W6. [warning] 与 GoLLIE 等 schema-aware IE 系统缺乏量化对比**\n读者需要知道 OntoCoDec + unconstrained LLM 与 GoLLIE 的 F1 差距。\n\n**W7. [warning] κ̄ 部署指导的证据不足**\n仅 2 个数据集，样本量极小，无法建立有意义的预测关系。\n\n### Minor\n**M1.** 主文似超 8 页（Section 7 延伸至 page 9 约 10 行）\n**M2.** Table 密度极高，部分可用图表替代\n**M3.** \"Best-effort pair-based enforcement\" 精确含义可更明确\n**M4.** 1 orphan bib entry, 2 篇在 OpenAlex 未找到\n**M5.** Grammar-first fallback 的极端情况（G(t)=∅）未讨论\n\n### Scores\nSoundness 3.5/5, Excitement 3/5, Overall 3.5/5 (Borderline Conference), Confidence 4/5, Reproducibility 4/5\n\n---\n\n请逐条回应，特别关注：\n1. 你是否同意 BoostCD/IterGen 缺失对比是 must-fix？你此前未将此列为 must-fix，而是 should-fix (你的 W5)——为什么？\n2. R1 对 pumping lemma 的形式化 gap 分析（位置索引 vs 名称引用）——你是否同意这是一个问题？\n3. R1 给 Overall 3.5 vs 你给 3.0——分歧在哪？你认为差距的核心原因是什么？\n4. R1 给 Excitement 3/5 vs 你给 2.5/5——decidability taxonomy 的理论价值是否被你低估了？"
  }
}
```

</details>

---


### Tool result

_source line 1340 · 2026-05-20T18:46:09.017262+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 1341 · 2026-05-20T18:46:12.372191+00:00_

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


## Round 95

## Round 95

2 recorded events


### User

_source line 1342 · 2026-05-20T18:46:14.827029+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

审查要点总结：

- **Overall: 3.5**（Borderline Conference）
- **2 个 Must-Fix**：(1) 缺少 BoostCD/IterGen 这两个最直接可比的 constrained decoding baseline 对比；(2) WikiEvents 仅 20 文档测试集，无法支撑 "systematic evaluation" 的 claim
- **5 个 Should-Fix**：pumping lemma 证明与实际 JSON 格式存在形式化 gap；DocRED beam search 仅 50 文档子集；"formally compiles" 措辞对 semantic layer 过度；缺乏与 GoLLIE 等系统的量化对比；κ̄ 部署指导证据不足
- **5 个 Minor**：页数可能略超限、表格密度高、best-effort 定义需更精确、引用审计小问题、级联失败 edge case 未讨论
- **5 个 Questions**：要求作者澄清 pumping lemma 在名称引用下的适用性、BoostCD 不可比的具体原因、fallback 的 per-relation 分布、LoRA 训练时是否有约束、实体生成顺序的影响

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

_source line 1343 · 2026-05-20T18:46:19.656324+00:00_

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


## Round 96

## Round 96

2 recorded events


### User

_source line 1344 · 2026-05-20T18:48:16.934567+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应：逐条回应 Reviewer 2

---

## Must-Fix

**[AGREE] R2-W1: 正文超过 8 页限制**
同意这需要修复。Section 7 结论确实延伸至 page 9 约 11 行（lines 650–660）。我在初审中将此列为 Minor（M1），但 R2 升级为 critical 有其道理：EMNLP 2026 via ARR 的格式要求明确写了"strict 8-page limit"，格式违规可能导致 desk reject。不过我补充一点：这是**机械性可修复问题**（压缩结论段或调整排版即可），不反映论文的实质性缺陷。我倾向于将此归类为 **must-fix 但 low-effort**，不应影响学术评分。

**[AGREE] R2-W2: CF 代价在 Abstract/Introduction 被低估**
同意。我重新检查了 Abstract（page 1）原文："with modest CF costs from per-relation independence"。对照实际数据：
- SciERC zero-shot CF = 9.90%（Table 1, page 5）
- WikiEvents zero-shot CF = 15–21%（Table 5, page 7）
- DocRED zero-shot CF = 9.90%（Table 3, page 6）

用 "modest" 描述接近 10% 的 fallback 率确实有误导之嫌。尤其 Introduction（Section 1）完全未提及 CF，只在 Section 4 和 5 才展开讨论。R2 的判断是对的——**隐藏主要副作用降低可信度**。

我在初审中将 CF 的 claim 问题放在 W4（should-fix），聚焦于 "resolvable via beam search" 的措辞。R2 的角度更全面：不仅 beam search claim 需要限定，Abstract/Intro 本身就应当 upfront 呈现 CF 代价。我接受 R2 的升级，同意这应当是 **must-fix**。

不过有一个 nuance：CF=9.90% 的含义需要澄清。CF 是 grammar-first fallback 的**触发率**（semantic mask 与 grammar mask 冲突的比例），不是"输出错误率"。当 fallback 触发时，grammar layer 仍保证 JSON 结构合法性，只是跳过了该位置的 semantic 类型约束。因此 CF=9.90% 不等于 9.90% 的输出不可用，但确实意味着约 10% 的类型约束检查被绕过。作者应在 Abstract 中区分这一点，而非笼统地说 "modest"。

**[AGREE with nuance] R2-W3: κ̄ 作为独立贡献定位过高**
基本同意，但对严重性判断略有保留。

同意的部分：
- κ̄ = 1 − |σ(r)|/|E|² 确实只是约束表的归一化密度，数学上 trivial
- 仅 2 个数据点（SciERC κ̄=0.333, DocRED κ̄=0.842）无法建立有意义的预测关系
- R2 指出的 Mistral 异常（DR 降幅仅 76% vs Qwen/Llama 94–99%，同一 κ̄）有力地说明 κ̄ 不能独立预测效果

保留的部分：
- 论文 Contribution 2 的原文是 "A descriptive metric, constraint tightness κ̄, that correlates schema restrictiveness with enforcement outcomes and provides deployment guidance"（page 2）。作者用了 "descriptive" 和 "correlates"，没有声称 predictive power。这与 R2 说的"独立贡献定位过高"之间存在程度差异
- 作为一个 deployment heuristic（高 κ̄ → 更需要 beam search 或 fine-tuning），即使只有 2 个数据点，方向性的指导仍然有价值

我倾向于将此保留为 **should-fix**（降级 Contribution 2 的措辞，改为 "we additionally introduce..." 而非独立贡献条目）而非 must-fix。但 R2 的核心批评——将一个 trivial metric 列为三大贡献之一——我认同这影响了论文的定位可信度。

---

## Should-Fix

**[AGREE] R2-W4: "any autoregressive LM" 过度声称**
同意。Abstract 的 "applicable to any autoregressive LM" 与实际验证范围（7–8B 为主，70B 仅 preliminary）不匹配。我在初审中漏掉了这个具体措辞问题。补充：论文也未验证 (a) <7B 小模型（约束执行可能因能力不足导致更高 CF），(b) API-only 模型（如 GPT-4、Claude，无法直接操作 logits），(c) 非 Transformer 架构。建议改为 "applicable to autoregressive LMs with logits access"。

**[AGREE] R2-W5: DocRED 零样本 DR 降幅讨论不足**
同意。DocRED zero-shot DR 从 18.46% 降至 10.21%（Table 3, page 6），降幅约 45%，远低于 SciERC 的 94%。论文将此归因于 κ̄ 差异（Section 5.2: "reflects higher tightness κ̄=0.842 vs 0.333"），但正如 R2 所说，这只是 restate 了现象而非解释了原因。

我在初审中通过 W4（DocRED 50-doc subset）间接涉及了这个问题，但 R2 更直接地指出了核心矛盾：10.21% 的残余 DR 与论文标题中 "Type-Constrained" 的承诺之间存在张力。补充一个具体证据：Appendix D（page 22, Table 9）显示 DocRED 的 GENERIC←→OtherScientificTerm 冲突占 63.3% 的 CF violations，这表明残余 DR 主要来自**实体类型歧义**（GENERIC catch-all type），不是约束执行本身的失败，而是 schema 设计的固有模糊性。论文应更明确地讨论这一区分。

**[AGREE] R2-W6: WikiEvents 评估局限性**
同意。R2 的观察补充了我的初审（W2, critical）中未涉及的细节：
- Zero-shot entity F1 从 0 → 12–18%（Table 5, page 7）主要是格式修复（unconstrained 输出无法被解析为合法 entity，constrained 输出至少结构合法），而非语义提取能力的改善。这一点我漏掉了，R2 判断精准
- Grammar-only 行（Table 5）确实缺少 F1 数值（仅报告 violation rates），使得无法判断 semantic layer 在 EE 上的 incremental F1 贡献

不过我仍然认为 WikiEvents 评估的**统计效力问题**（n=20 test docs）是更根本的 concern，应为 critical 而非 R2 标注的 warning。

**[AGREE] R2-W7: "formally compiles" 措辞**
完全同意，与我的初审 W5 一致。不再赘述。

---

## Minor

**[AGREE] R2-M1:** 确认 orphan bib entry schmidt2025grammar，与我的 M4 一致。

**[AGREE] R2-M2:** 表格字体偏小，Table 1/3/4 信息密度高，但在 ACL 双栏排版中普遍存在，属于 cosmetic issue。

**[AGREE] R2-M3:** S1/S2 命名确实不直观。"S1 (joint extraction)" vs "S2 (two-pass pipeline)" 的缩写需要在首次使用时更明确定义，且 "Full (S1)" 的嵌套命名增加了阅读障碍。

**[AGREE] R2-M4:** 对称 relation 的处理（脚注 1, page 4）确实重要到值得在正文讨论，因为它直接影响 κ̄ 的计算和约束的 asymmetry 语义。

**[AGREE] R2-M5:** 与我的 M4 一致。formattax2026（Lee et al., 2026）和 regino2025kgcurator 在 OpenAlex 未找到，可能是极新的 preprint 尚未被索引。不影响引用正确性但建议验证。

---

## Director 提出的具体问题回应

### 1. 正文超页是否 must-fix？

**是。** R2 正确。EMNLP 2026 via ARR 规则明确且严格。虽然机械修复容易（压缩 11 行），但格式违规的 desk reject 风险不可忽视。我将此从 minor 升级为 must-fix。

### 2. CF 代价被低估？"modest" 描述 9.90% CF 是否误导？

**同意 R2 判断。** "modest" 用于描述 9.90% CF 确实具有误导性。一个有用的参照：post-hoc filtering 在 DocRED 上丢弃 48% 的 triples（Appendix C, page 22）——OntoCoDec 的 CF 确实远低于 post-hoc 的代价，但用 "modest" 而非给出具体数字掩盖了这一事实。Abstract 应直接报告 representative CF 数值（如 "with CF rates of 0–9.9% depending on schema complexity"），让读者自行判断是否 "modest"。

### 3. Excitement 2.5 vs 3.0 的分歧

R2 给 Excitement 2.5（"Potentially interesting"），我给 3.0（"Interesting"）。分歧来源：

**R2 更低的原因可能是：**
- R2 更看重 practical novelty——双层架构虽然设计干净，但 grammar-constrained decoding（Level 1）是已有工作（XGrammar、Outlines），OntoCoDec 的 incremental contribution 是 semantic layer（Level 2），且这个 layer 的效果受限于 schema 复杂度（DocRED 45% vs SciERC 94% 降幅）
- R2 给 Novelty 2.5/5 进一步印证了这一判断：认为方法论新意有限

**我给 3.0 的原因：**
- Decidability taxonomy（三级分类）本身是有价值的理论贡献，为社区提供了分析 IE 约束执行问题的框架，超越了具体系统的实现
- 将 PL/formal language theory 的分析工具引入 IE 问题是一个有趣的 cross-pollination

**我的修正判断：** 在看到 R2 的完整意见后，我认为 2.5 偏低——decidability taxonomy 的理论价值不应因为系统 novelty 有限而被完全折价。但我也承认 3.0 可能偏高——taxonomy 本身虽然 well-motivated，但三级分类相当直观（CF 可解/有状态可解/不可在线解），不是深刻的理论发现。**维持 3.0 不变。**

### 4. Overall 3.0 vs 3.5 的核心差距

R2 给 3.0（Findings），我给 3.5（Borderline Conference）。半分差距的核心原因：

**R2 的 3.0 逻辑（我的理解）：**
R2 识别出一个**系统性 overclaiming 模式**——"modest" CF、κ̄ 作为独立贡献、"any autoregressive LM"、"formally compiles"——并认为这些不是孤立的措辞问题，而是论文对自身贡献的定位整体偏高。当多个 claim 同时被高估时，论文的可信度遭受累积损害。加上 Excitement 2.5，3.0 是合理的。

**我的 3.5 逻辑：**
我更看重论文的**实质贡献**而非措辞问题。核心技术（decidability taxonomy + 双层约束执行）是 sound 的，实验覆盖面广（3 datasets × 4 models × 多配置），消融设计细致。措辞问题可以在 revision 中修正而不改变技术贡献。缺少 BoostCD/IterGen baseline 是最实质性的缺陷。

**交叉回应后的修正判断：**
R2 的 overclaiming pattern 论点在我重新审视后确实成立：不是单个 claim 的问题，而是 Abstract/Intro/Contributions 整体呈现了比实际支撑更强的 narrative。这在 ARR 审稿中会降低 reviewer 信任度。

但我仍然认为 3.5 比 3.0 更准确：
- 论文的 Limitations section（page 10）诚实地覆盖了多数局限性
- 附录中的分析深度（33 页）远超平均水平
- 核心技术 contribution 是 sound 的，overclaiming 是 presentation 问题不是 substance 问题
- 修订后（限定 claims + 补充 baselines）有明确的升级路径

**最终维持 Overall 3.5**，但承认 R2 的 3.0 也在合理范围内。如果 BoostCD 对比实验显示 OntoCoDec 的 incremental gain 很小，我会倾向于降至 3.0。


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

_source line 1345 · 2026-05-20T18:48:21.853458+00:00_

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


## Round 97

## Round 97

2 recorded events


### User

_source line 1346 · 2026-05-20T18:48:27.057695+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **W1 超页、W2 CF低估、W4-W7**：全部 [AGREE]，其中 W1/W2 我接受 R2 的升级（从我初审的 minor/should-fix 升至 must-fix）
- **W3 κ̄ 定位过高**：[AGREE with nuance]，同意 trivial metric 不应列为独立贡献，但保留 should-fix（非 critical）
- **评分分歧**：Excitement 维持 3.0 vs R2 的 2.5（decidability taxonomy 的理论价值不应完全折价）；Overall 维持 3.5 vs R2 的 3.0（overclaiming 是 presentation 问题而非 substance 问题，修订路径明确）

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

_source line 1347 · 2026-05-20T18:48:32.222157+00:00_

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


## Round 98

## Round 98

10 recorded events


### User

_source line 1348 · 2026-05-20T18:48:52.650795+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：Reviewer 1 审稿意见

---

## Must-Fix 逐条回应

### R1-W1: 缺少 BoostCD/IterGen baseline 对比

**[AGREE]** R1-W1 正确指出了我审稿中的一个疏漏。我在 Missing References 中仅评价 related work 覆盖"总体较好"，但未将缺失的实验对比单独列为 weakness。

具体而言：BoostCD（Sakota et al., EMNLP 2025）由 GCD 团队（Geng, Josifoski, West）开发，而 GCD 在 §5.1 和 §6 中被引用且 GCD 的原始工作评估了 SciERC，因此 BoostCD 极可能覆盖相同 benchmark。论文在 §6 中称 "different benchmarks preclude direct comparison"，但未提供证据支撑该断言——如果 BoostCD 确实在 SciERC 上有结果，这个回避是不可接受的。

**我同意将此提升为 must-fix。** 即使 OntoCoDec 的贡献定位是 framework + formal analysis 而非 SOTA 追求，在 EMNLP 层面，与最直接的 IE constrained decoding 竞争者缺乏量化对比会让 Contribution 3（"first systematic evaluation"）的声称站不住脚。至少需要在 SciERC 上对比 GCD 和/或 BoostCD 的 DR 降幅和 F1。

补充说明：IterGen 的对比优先级略低，因为其 backtracking 机制涉及不同的 efficiency trade-off（论文在 §6 中已定性讨论）。但 BoostCD 作为同一任务、同一范式（decoding-time constraint for IE）的直接竞争者，缺失对比是 critical 的。

---

### R1-W2: WikiEvents 统计效力不足

**[AGREE]** 与我的 W6 一致，但我同意 R1 将其提升至更高严重度的理由。

关键区分：零样本评估覆盖全部 246 篇文档，统计效力尚可；但 fine-tuning composability 仅基于 20-document test set，CIs 宽达 ±0.05–0.06（§5.4），这不是 "systematic evaluation" 而是 preliminary demonstration。

Contribution 3 明确声称 "the framework generalizes to event extraction with 245 constraints across three tokenizer families"——零样本泛化确实有 246 篇文档支撑，但 fine-tuning composability 的 20 篇数据量不足以支撑此力度。R1 建议将此降级为 "preliminary demonstration" 是合理的。

---

## Should-Fix 逐条回应

### R1-W3: Pumping lemma 的形式化 gap（位置索引 vs 名称引用）

**[AGREE]，但认为这是 presentation gap 而非 correctness gap。**

R1 观察到 Proposition 1 的 proof sketch（§3, main.tex:30–33）使用位置索引模型（"a relation referencing head $e_k$ for arbitrary $k \leq n$"），但实际 JSON schema（Eq. 1）使用名称字符串引用。这是一个有效的形式化缺口。

然而，核心论证在名称引用模型下仍然成立：PDA 需要根据名称字符串查找对应的类型，而名称集合无界、查找是随机访问的——PDA 的 LIFO stack 同样无法支持。实质上，位置索引和名称字符串在 expressiveness 上是等价的（name→type 映射等价于 position→type 映射，因为名称空间也是无界的）。

建议作者在 proof sketch 或 Appendix O 中增加一段明确说明：位置索引模型是名称引用模型的 abstraction，核心的 random-access 困难在两种模型下均成立。

---

### R1-W4: DocRED beam search 仅用 50 文档子集

**[AGREE]，并补充更强的证据。**

这与我的 Q3 一致。R1 补充了关键细节：Appendix Table 15 显示 DocRED zero-shot beam 的 CF 仅从 28.4% 降至 21.4%，远不是 "resolve"。

论文在多处使用 "resolvable via beam search" 这一表述（Abstract, §5.5, §7），但这一声称的证据基础严重不对称：
- SciERC：beam 确实消除所有违规（§5.5, full 551/998 doc）✓
- DocRED zero-shot：仅 50 docs，CF 从 28.4%→21.4%，残余巨大 ✗
- DocRED fine-tuned：beam on full 998 docs 消除所有违规 ✓

"Resolvable via beam search" 的声称只在 fine-tuned 或低 κ̄ 设置下成立。对于 high-κ̄ zero-shot 场景，beam 并不 "resolve" CF。论文应修正此声称的适用范围。

---

### R1-W5: "Formally compiles" 措辞过度

**[AGREE]** 与我的 W7 完全一致。R1 的表述更精炼："grammar layer 是编译，semantic layer 是运行时规则解释。" 我补充：整个 pipeline 更准确的描述是 "compile-time grammar generation + runtime constraint interpretation"，而非端到端的 "formal compilation"。

---

### R1-W6: 与 GoLLIE 缺乏量化对比

**[AGREE]，但优先级低于 R1-W1（BoostCD 对比）。**

GoLLIE 是 training-based schema-aware IE，与 OntoCoDec（inference-time constraint）解决问题的路径不同，直接 F1 对比可能 misleading（GoLLIE 需要 schema-specific fine-tuning，OntoCoDec 不需要）。

但 R1 的核心诉求合理：读者需要一个 reference point 来理解 "7-8B model + OntoCoDec constraints" 的 R-F1 40-46% 在领域中处于什么水平。即使不做严格对比，提供一个表格行展示 GoLLIE 或类似系统在相同数据集上的 published numbers 即可。这是 contextual information，不需要重新跑实验。

---

### R1-W7: κ̄ 部署指导证据不足

**[AGREE]，并重申我的 W3 中更强的立场。**

R1 将此定为 should-fix，我将其定为 must-fix（W3）。核心分歧在于 κ̄ 是否应该作为 Contribution 2。R1 认为证据不足但允许保留 contribution 定位；我认为仅 2 个数据点的描述统计量不应作为独立 contribution。

补充论据：κ̄ 对 Mistral 的预测完全失效（SciERC κ̄=0.333 理论上应 "near-complete DR elimination"，但 Mistral 仅达 76%——Table 4），说明没有 confusability 这个协变量，κ̄ 的 guidance 价值极有限。两个变量、两个数据点——这是无法拟合任何有意义模型的。

---

## Minor 逐条回应

### R1-M1: 主文超 8 页
**[AGREE]** 与我的 W1（must-fix）一致。我将此列为 critical，R1 列为 minor。**我认为应提升为 must-fix**——EMNLP 2026 的 8 页限制是硬约束，违反可能导致 desk reject。

### R1-M2: Table 密度
**[AGREE]** 与我的 M2 一致。

### R1-M3: "Best-effort pair-based enforcement" 含义
**[AGREE]** 我未单独标注此点，但 R1 的观察合理。该术语在 §3.1 和 §3.3 中定义但含义跨两处分散——第一次出现时应给出完整的 inline definition。

### R1-M4: Orphan bib + OpenAlex 未找到
**[AGREE]** 与我的 M1/M5 一致。

### R1-M5: G(t)=∅ 的边界情况
**[REBUT]** 这不应是实际问题。XGrammar 的 pushdown automaton 保证在合法 JSON 生成路径上 G(t) ≠ ∅（至少有一个合法 continuation token）。G(t)=∅ 意味着 grammar 本身有 bug（dead state），这是 XGrammar 实现的问题而非 OntoCoDec 框架的问题。论文的 grammar-first fallback 已经处理了 G(t) ∩ S(t) = ∅ 的情况（§4），而 G(t)=∅ 属于 XGrammar 层的 invariant 保证。

---

## Director 指定的 4 个问题

### Q1: BoostCD/IterGen 缺失对比——must-fix vs should-fix？

**我现在同意 R1 将此列为 must-fix。**

我此前未单独标注此问题的原因有二：(1) 我更关注框架和 formal analysis 层面的贡献定位问题（κ̄ overclaiming、CF 透明度），(2) 论文在 §6 中明确声称 "different benchmarks preclude direct comparison"，我当时接受了这一声称而未深入质疑。

R1 的分析让我重新审视：BoostCD 团队的前序工作 GCD 确实在 SciERC 上评估过（论文在 Table 1 caption 中引用 GCD 作为 "ceiling of grammar-constrained decoding"），因此 BoostCD 极可能覆盖相同 benchmark。在此前提下，"different benchmarks" 的回避是不充分的，缺失对比确实是 must-fix。

### Q2: Pumping lemma 形式化 gap

**部分同意。** 如上 R1-W3 回应所述，这是 presentation gap 而非 correctness gap。核心论证在名称引用模型下仍成立（名称→类型的随机访问同样超出 PDA 能力），但 proof sketch 应明确说明从位置索引到名称引用的 abstraction 关系。作为 formal contribution 的一部分，这种精度的缺失值得修正，但不影响结论的 validity。

### Q3: Overall 3.5 vs 3.0——分歧核心

我给 3.0（Findings），R1 给 3.5（Borderline Conference）。分歧核心在三点：

1. **CF 代价的权重**：我将 CF 透明度问题列为 must-fix（W2），认为 Abstract 中的 "modest" 误导性地低估了 9.90%–21% 的 CF 率。R1 未单独标注 CF 透明度问题。如果 CF 的呈现方式修正，论文的 overall trade-off profile 会更 honest，但也更不 appealing。

2. **κ̄ contribution 的严重度**：我将 κ̄ overclaiming 列为 must-fix，R1 列为 should-fix。如果 κ̄ 从独立 contribution 降级为分析工具，论文只剩两个 contribution（framework + evaluation），对主会议而言可能不够。

3. **缺失 baseline 对比的影响**：R1 将 BoostCD 缺失列为 must-fix 但仍给 3.5——这意味着 R1 认为即使加上这个 must-fix，论文的 framework contribution 仍有可能达到主会议水平。我现在加上这个 must-fix，结合 CF 透明度和 κ̄ 问题，三个 must-fix 叠加使 3.0 更合理。

**总结**：如果所有 must-fix 都被妥善修正（压缩页数、增加 baseline 对比、修正 CF 叙述、降级 κ̄），论文有可能达到 3.5。但在当前状态下，3.0 更准确地反映了累积问题的严重度。

### Q4: Decidability taxonomy 的理论价值——是否被我低估？

**R1 的 Excitement 3/5 有一定道理，但我维持 2.5/5，理由如下：**

R1 可能更看重 decidability taxonomy 的 reusability——三级分类（CF / prefix-decidable with state / non-local）可以迁移到其他 structured generation 任务（如 knowledge graph completion、SQL generation with schema constraints）。从这个角度看，taxonomy 的贡献超越了本文的 IE 场景。

但我认为 taxonomy 的 insight density 有限：
- Level 1（JSON structure = CF）是 trivially known
- Level 2（type constraints need state）是 formally interesting 但 intuitively obvious——任何熟悉 PDA 限制的人都会预期此结果
- Level 3（cross-entity consistency = non-local）的分析在论文中最弱——仅靠 beam search 和 post-hoc 处理，没有 formal guarantee

Proposition 1 的证明是正确的，但 **confirmatory**（证实预期）而非 **surprising**（揭示意外）。对于 Excitement 这个维度，confirmatory formalization 的价值低于 surprising insight。

如果论文能展示 taxonomy 指导了一个非直觉的设计决策（例如，某个看似应该在 Level 2 的约束实际上是 Level 3，从而改变了架构），我会提高 Excitement 到 3/5。但当前的 taxonomy 与最终架构之间的映射过于自然——grammar layer → Level 1, semantic layer → Level 2, beam search → Level 3——没有 surprise。

**我将 Excitement 从 2.5 微调至 2.75（如果允许的话），承认 formalization 有 marginal 的迁移价值，但不足以达到 3/5。**

---

## 更新后的综合评估

交叉审稿后，我新增一个 must-fix（BoostCD baseline 缺失，原被我遗漏），其余评分维持不变：

| 维度 | 原始分数 | 交叉后分数 | 变化理由 |
|------|---------|-----------|---------|
| Soundness | 3.5 | 3.5 | 无变化——R1 未提出影响 soundness 的新问题 |
| Excitement | 2.5 | 2.5 | R1 对 taxonomy 的正面评价有道理，但 confirmatory formalization 的 excitement 有限 |
| Overall | 3.0 | 3.0 | 新增 BoostCD must-fix 被 R1 的正面观点（taxonomy reusability）部分抵消 |
| Confidence | 4 | 4 | 无变化 |

**Must-Fix 汇总（4 项）**：
1. 正文超 8 页（W1, 与 R1-M1 一致但我认为应升为 must-fix）
2. CF 代价透明度（W2）
3. κ̄ contribution 定位过高（W3）
4. **[新增]** 缺少 BoostCD 等最直接 baseline 的量化对比（采纳 R1-W1）


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

_source line 1349 · 2026-05-20T18:49:14.189989+00:00_

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

_source line 1350 · 2026-05-20T18:49:14.240791+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T18:36:33.850567+00:00\", \"completed_at\": \"2026-05-20T18:40:31.453662+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主正文（Section 7 Conclusion）溢出至第 9 页，约 11 行结论文本后剩余 3/4 页面空白。EMNLP 2026 严格限制 main text 8 页，当前正文约 8.06 页，违反页数限制。需压缩正文内容使 Conclusion 在第 8 页内结束。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"前 2 页为纯文本（Abstract + Introduction），无任何视觉锚点。第一个 display item（Figure 1 架构图）直到第 3 页才出现。审稿人在前 2 分钟只看到密集文字，缺乏快速锚定的视觉元素。建议考虑将核心结果 teaser 或架构缩略图前移至第 1 页。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"整页纯文本（Related Work 下半 + Discussion and Conclusion 上半），无任何 display item 穿插。与前几页的 table-dense 节奏形成断裂。加上 page 7 下半也以文本为主，pages 7.5-8 构成约 1.5 页连续纯文本区。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 17-19\", \"message\": \"附录 B \\\"Extended Related Work\\\" 连续 3 页纯文本，无任何 figure/table/equation。虽是附录但审稿人仍可能翻阅，视觉单调。建议插入对比表或方法分类图打破节奏。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（架构概览图）作为全文首个 display item，使用 figure* 全宽排版，caption 自包含，能传达核心方法流程。作为方法论文的第一个视觉锚点是合适的选择。图内文字较小但在 150dpi 下仍可读。\"}, {\"severity\": \"info\", \"dimension\": \"pages 5-7\", \"message\": \"主实验区域 display item 密度良好：Table 1（p5）、Tables 2-3（p6）、Tables 4-5（p7），3 页内 5 个表格，节奏紧凑。全部使用 booktabs 风格，最优值加粗，小数精度一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 和 Table 3 紧密排列，页面利用率高。表格列数适中（6-8 列），未溢出 column width。\"}, {\"severity\": \"info\", \"dimension\": \"page 30\", \"message\": \"Table 25 使用红色/绿色文字标注违规与修正。色盲用户可能难以区分红绿——建议补充删除线 + 加粗等非颜色视觉线索。\"}, {\"severity\": \"info\", \"dimension\": \"page 26\", \"message\": \"Figure 4（Beam-width Pareto 分析）双子图，使用不同 marker shape + line style 辅助区分，灰度打印友好。图内字号偏小但可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 33\", \"message\": \"末页（附录 Proposition 1 证明）内容约占页面 50%，下半空白。作为附录最后一页且内容为数学证明，可接受。\"}, {\"severity\": \"info\", \"dime
…[truncated 418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1351 · 2026-05-20T18:49:14.492195+00:00_

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

_source line 1352 · 2026-05-20T18:49:14.542970+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1353 · 2026-05-20T18:52:09.623903+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 13 (fresh review, 2026-05-20)\n\n# ============================================================\n# Round 13 Must-Fix (Full Consensus)\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制（§7 约 11 行溢出至第 9 页）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 raised as critical, R1 初审列为 minor 后升级为 must-fix。Visual Check 同时发现。Section 7 结论溢出至 p9 约 11 行。EMNLP 2026 严格限制 8 页正文。\"\n  action_items:\n    - round: 13\n      action: \"压缩 §7 Discussion and Conclusion / §6 Related Work / §5 实验叙述，确保正文在第 8 页底部结束\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Introduction 中被系统性低估（'modest' 描述 9.90%–21% CF 是误导）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF4: CF 代价在 Abstract/Contribution 中不够透明\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 raised as critical, R1 AGREE 并升级。Abstract 'modest CF costs' 用于描述 SciERC 9.90%、WikiEvents 15–21% 有误导性。Introduction 完全未提 CF。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 明确写出 CF 范围（如 'with CF rates of 0–9.9% depending on schema complexity, reduced to ≤1.2% with fine-tuning'）；Introduction 增加 DR↔CF trade-off 段落\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF3\"\n  summary: \"缺少最直接可比的 IE constrained decoding baseline（BoostCD、IterGen）的量化对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: 无直接实验对比 BoostCD（should-fix）\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 raised as critical, R2 AGREE 并采纳。BoostCD (EMNLP 2025) 与 GCD 同团队，极可能覆盖 SciERC。§6 称 'different benchmarks preclude direct comparison' 但未提供证据。从 R12 should-fix 升级为 must-fix。\"\n  action_items:\n    - round: 13\n      action: \"在 SciERC 上至少复现 BoostCD/GCD 的 DR 降幅和 F1 进行对比；如无法复现，引用其报告数字进行间接对比并详细讨论不可比原因\"\n      assigned_to: agent\n      status: open\n    - round: 13\n      action: \"§5 或 §6 增加与 BoostCD/IterGen 的量化对比表或讨论段落\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents fine-tuning 仅 20 文档测试集，Contribution 3 'systematic evaluation' 措辞过度\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF4: WikiEvents fine-tuning 仅 20 文档测试集。Action: 标注 n=246/n=20 + 'preliminary' 限定\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2 raised as critical, R2 AGREE。§5.4 已标注 'preliminary' 但 Contribution 3 仍声称 'systematic evaluation' 和 'framework generalizes to event extraction'。零样本 246 docs 尚可，但 FT composability 的 20 docs 无法支撑此措辞。\"\n  action_items:\n    - round: 13\n      action: \"Contribution 3 将 EE 部分降级为 'preliminary demonstration'；讨论统计效力限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Must-Fix (Contested — R2 critical, R1 should-fix)\n# ============================================================\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 2 定位过高（仅 2 数据点的描述统计量）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF2: κ̄ 作为 'analytical linking framework' 被过度声称。Action: 降级为 'descriptive metric'\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3 must-fix, R1 AGREE with nuance (prefers should-fix)。论文已改称 'descriptive metric' 但仍列为 Contribution 2。κ̄ 对 Mistral 预测失效（SciERC DR 降幅 76% vs 期望 94–99%）。R1 认为方向性指导仍有价值；R2 认为 2 数据点不应列为独立贡献。\"\n  action_items:\n    - round: 13\n      action: \"将 κ̄ 从独立 Contribution 降级为分析工具（'we additionally introduce...'），整合入实验讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Should-Fix\n# ============================================================\n\n- id: \"R13-SF1\"\n  summary: \"'any autoregressive LM' 声称超出验证范围（主要 7–8B，无 <7B / API-only）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF3: 模型规模声称过宽\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 raised, R1 AGREE。Abstract 已改为 'validated primarily on 7–8B' 但 §1 仍有 'applies to any autoregressive LM'。\"\n  action_items:\n    - round: 13\n      action: \"§1 改为 'applicable to autoregressive LMs with logits access' 或 'validated on 7–70B parameter models'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF2\"\n  summary: \"DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%）的深层原因讨论不充分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W5 raised, R1 AGREE。论文将此归因于 κ̄ 差异，但这只是 restate 了现象。残余 DR 10.21% 对 'type-safe extraction' 目标构成挑战。R1 补充：63.3% CF violations 来自 GENERIC←→X 歧义，属 schema 设计固有模糊性而非约束失败。\"\n  action_items:\n    - round: 13\n      action: \"正文中明确讨论 tight-schema 场景下的约束局限性，区分 schema 模糊性 vs 约束执行失败\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF3\"\n  summary: \"DocRED beam search 零样本仅 50-doc 子集；'resolvable via beam search' 声称适用范围过宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF8: DocRED beam search 仅 50 文档子集\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 raised, R2 AGREE with stronger evidence。Appendix Table 15 显示 DocRED ZS beam CF 仅 28.4%→21.4%，远未 'resolve'。'Resolvable' 仅在 FT 或低 κ̄ 下成立。\"\n  action_items:\n    - round: 13\n      action: \"Abstract/§5 限定 beam search claim（'substantially reduces' 而非 'resolves'）；报告 50-doc vs 全集分布差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"'formally compiles' 措辞对 semantic layer 过度（运行时规则解释非传统编译）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W7, full consensus。Grammar layer 是编译（ontology→EBNF→PDA），semantic layer 是 runtime rule-based masking。'Compile' 隐含离线静态转换，与 semantic layer 动态维护不符。\"\n  action_items:\n    - round: 13\n      action: \"区分两层编译性质：grammar = ahead-of-time compilation, semantic = rule-based runtime enforcement；或改用 'translates...into composable constraints'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF5\"\n  summary: \"缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考（读者缺乏 F1 水平锚定）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W6 raised, R2 AGREE（优先级低于 BoostCD）。不需要重跑实验，引用 GoLLIE published numbers 提供 reference point 即可。\"\n  action_items:\n    - round: 13\n      action: \"§6 或 Discussion 引用 GoLLIE 在 SciERC/DocRED 上的 published numbers，提供 F1 context\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF6\"\n  summary: \"Pumping lemma 证明使用位置索引模型，但实际 JSON 格式使用名称引用——形式化 gap\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W3 raised, R2 AGREE（presentation gap not correctness gap）。核心论证在名称引用下仍成立（name→type 随机访问同样超出 PDA 能力），但 proof sketch 应明确说明 abstraction 关系。\"\n  action_items:\n    - round: 13\n      action: \"Appendix O 增加一段说明位置索引模型是名称引用模型的 abstraction，random-access 困难在两种模型下均成立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Minor\n# ============================================================\n\n- id: \"R13-M1\"\n  summary: \"S1/S2 命名不直观，混用 'S1 (joint extraction)' 和 'Full (S1)'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-M2: S1/S2 命名易混淆\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M3, R1 AGREE。首次出现时需给出描述性名称。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M2\"\n  summary: \"Orphan bib entry (schmidt2025grammar) + 2 篇 unverified citations (formattax2026, regino2025kgcurator)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-M1: 10 orphan entries + 1 duplicate key\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1/M5 + R1-M4。orphan 从 10 减至 1（大部分已清理），formattax2026 和 regino2025kgcurator 在 OpenAlex 未找到。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M3\"\n  summary: \"表格字体偏小（Table 1/3/4 用 resizebox 压缩 8+ 列），打印可读性受影响\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M2, R1-M2 同意（cosmetic issue）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M4\"\n  summary: \"§4 脚注 1（对称 relation 的 κ 计算）应在正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-M4, R1 AGREE。影响 κ̄ 计算和约束 asymmetry 语义。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M5\"\n  summary: \"'Best-effort pair-based enforcement' 首次出现时需完整 inline definition\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1-M3, R2 AGREE。定义跨 §3.1 和 §3.3 分散。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M6\"\n  summary: \"Table 25 红绿色标注违规/修正，色盲不友好\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Visual Check 发现。建议补充删除线+加粗等非颜色视觉线索。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Divergence\n# ============================================================\n\n- id: \"R13-DIV1\"\n  summary: \"κ̄ 严重度分歧：R2 must-fix vs R1 should-fix\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1：'descriptive' 措辞已降低期望，方向性指导有价值，prefer should-fix。R2：2 数据点 trivial metric 不应列为独立 contribution，insist must-fix。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-DIV2\"\n  summary: \"Overall 评分分歧：R1=3.5 (Borderline Conference) vs R2=3.0 (Findings)\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 更看重实质贡献（decidability taxonomy + 全面评估）和修订路径；R2 认为 overclaiming pattern 累积损害可信度。R1：overclaiming 是 presentation 问题非 substance。R2：3 个 must-fix 叠加使 3.0 更准确。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-DIV3\"\n  summary: \"Excitement 分歧：R1=3.0 vs R2=2.5（decidability taxonomy 的理论价值）\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1：taxonomy 可迁移到其他 structured generation 任务，cross-pollination 价值。R2：taxonomy insight density 有限，三级分类相当直观，Proposition 1 是 confirmatory 而非 surprising。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 — R2 REBUT（记录但不采纳）\n# ============================================================\n\n- id: \"R13-REB1\"\n  summary: \"G(t)=∅ 边界情况：R1 minor concern, R2 REBUT\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-M5：G(t)=∅ 在极端 tokenizer edge case 下行为未讨论。R2 REBUT：XGrammar PDA 保证合法 JSON 路径上 G(t)≠∅，G(t)=∅ 属 XGrammar 实现 bug 而非 OntoCoDec 问题。不采纳为 issue。\"\n  action_items: []\n  resolution: \"R2 REBUT 成立：属 XGrammar 层 invariant 保证，非本文范围\"\n  resolution_round: 13\n\n# ============================================================\n# Prior rounds — resolved (carried forward for tracking)\n# ============================================================\n\n- id: \"R12-MF1\"\n  summary: \"'Exact enforcement' → 'best-effort' 全文替换\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Abstract/§3.3 已改为 'best-effort pair-based'。CF 透明度问题在 R13-MF2 继续追踪。\"\n  resolution_round: 13\n\n- id: \"R12-MF3\"\n  summary: \"Proposition 1 proof sketch 不完整\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Appendix O 已补完整 pumping lemma 证明。新发现的形式化 gap（位置索引 vs 名称引用）在 R13-SF6 追踪。\"\n  resolution_round: 13\n\n- id: \"R12-SF1\"\n  summary: \"语义层核心机制与 IterGen/PICARD 的概念区分不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§6 已增加 preventive vs corrective vs incremental parsing 对比。R13 未再标记。\"\n  resolution_round: 13\n\n- id: \"R12-SF6\"\n  summary: \"Entity registry 顺序依赖导致全局次优类型赋值\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§4 已讨论贪心赋值局限性，定位为 Level 3 non-local 约束。\"\n  resolution_round: 13\n\n- id: \"R12-SF7\"\n  summary: \"'Ontology-agnostic' → 更精确表述\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已改为 'applicable to formal ontologies and empirically-derived type constraints'。\"\n  resolution_round: 13\n\n- id: \"R12-VL1\"\n  summary: \"主文前 4 页无任何 display item，框架论文缺架构图\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 框架图已加入 §3（page 3）。Visual Check 确认其为全文首个视觉锚点。\"\n  resolution_round: 13\n\n- id: \"R12-VL2\"\n  summary: \"主文 8 页正文零 Figure，全部 Figure 在附录\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 已入主文。主文 1 figure + 5 tables = 6 display items。\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Eq.(2) conjunction 未明确为 element-wise AND\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Eq.(2) 已加注 'element-wise AND over vocabulary V'。\"\n  resolution_round: 13\n\n- id: \"R11-MF1\"\n  summary: \"'Near-lossless' 叙事未充分呈现 CF trade-off\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"R11 Paper Agent 完成 two-tier narrative 重构。\"\n  resolution_round: 11\n\n- id: \"R11-MF2\"\n  summary: \"缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 对比\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"d063 GoLLIE 实验完成。§6 已加 qualitative positioning。\"\n  resolution_round: 11\n\n- id: \"R10-MF1\"\n  summary: \"'Ontology Constraints' → 'Schema Constraints'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Title 已更新。\"\n  resolution_round: 11\n\n- id: \"R10-MF2\"\n  summary: \"缺少 ARR Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"checklist.tex 已添加。\"\n  resolution_round: 11\n"
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
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 13 (fresh review, 2026-05-20)\n\n# ============================================================\n# Round 13 Must-Fix (Full Consensus)\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"正文超 8 页限制（§7 约 11 行溢出至第 9 页）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1 raised as critical, R1 初审列为 minor 后升级为 must-fix。Visual Check 同时发现。Section 7 结论溢出至 p9 约 11 行。EMNLP 2026 严格限制 8 页正文。\"\n  action_items:\n    - round: 13\n      action: \"压缩 §7 Discussion and Conclusion / §6 Related Work / §5 实验叙述，确保正文在第 8 页底部结束\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"CF 代价在 Abstract/Introduction 中被系统性低估（'modest' 描述 9.90%–21% CF 是误导）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF4: CF 代价在 Abstract/Contribution 中不够透明\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W2 raised as critical, R1 AGREE 并升级。Abstract 'modest CF costs' 用于描述 SciERC 9.90%、WikiEvents 15–21% 有误导性。Introduction 完全未提 CF。\"\n  action_items:\n    - round: 13\n      action: \"Abstract 明确写出 CF 范围（如 'with CF rates of 0–9.9% depending on schema complexity, reduced to ≤1.2% with fine-tuning'）；Introduction 增加 DR↔CF trade-off 段落\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF3\"\n  summary: \"缺少最直接可比的 IE constrained decoding baseline（BoostCD、IterGen）的量化对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF2: 无直接实验对比 BoostCD（should-fix）\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 raised as critical, R2 AGREE 并采纳。BoostCD (EMNLP 2025) 与 GCD 同团队，极可能覆盖 SciERC。§6 称 'different benchmarks preclude direct comparison' 但未提供证据。从 R12 should-fix 升级为 must-fix。\"\n  action_items:\n    - round: 13\n      action: \"在 SciERC 上至少复现 BoostCD/GCD 的 DR 降幅和 F1 进行对比；如无法复现，引用其报告数字进行间接对比并详细讨论不可比原因\"\n      assigned_to: agent\n      status: open\n    - round: 13\n      action: \"§5 或 §6 增加与 BoostCD/IterGen 的量化对比表或讨论段落\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF4\"\n  summary: \"WikiEvents fine-tuning 仅 20 文档测试集，Contribution 3 'systematic evaluation' 措辞过度\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF4: WikiEvents fine-tuning 仅 20 文档测试集。Action: 标注 n=246/n=20 + 'preliminary' 限定\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2 raised as critical, R2 AGREE。§5.4 已标注 'preliminary' 但 Contribution 3 仍声称 'systematic evaluation' 和 'framework generalizes to event extraction'。零样本 246 docs 尚可，但 FT composability 的 20 docs 无法支撑此措辞。\"\n  action_items:\n    - round: 13\n      action: \"Contribution 3 将 EE 部分降级为 'preliminary demonstration'；讨论统计效力限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Must-Fix (Contested — R2 critical, R1 should-fix)\n# ============================================================\n\n- id: \"R13-MF5\"\n  summary: \"κ̄ 作为独立 Contribution 2 定位过高（仅 2 数据点的描述统计量）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-MF2: κ̄ 作为 'analytical linking framework' 被过度声称。Action: 降级为 'descriptive metric'\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3 must-fix, R1 AGREE with nuance (prefers should-fix)。论文已改称 'descriptive metric' 但仍列为 Contribution 2。κ̄ 对 Mistral 预测失效（SciERC DR 降幅 76% vs 期望 94–99%）。R1 认为方向性指导仍有价值；R2 认为 2 数据点不应列为独立贡献。\"\n  action_items:\n    - round: 13\n      action: \"将 κ̄ 从独立 Contribution 降级为分析工具（'we additionally introduce...'），整合入实验讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Should-Fix\n# ============================================================\n\n- id: \"R13-SF1\"\n  summary: \"'any autoregressive LM' 声称超出验证范围（主要 7–8B，无 <7B / API-only）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF3: 模型规模声称过宽\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4 raised, R1 AGREE。Abstract 已改为 'validated primarily on 7–8B' 但 §1 仍有 'applies to any autoregressive LM'。\"\n  action_items:\n    - round: 13\n      action: \"§1 改为 'applicable to autoregressive LMs with logits access' 或 'validated on 7–70B parameter models'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF2\"\n  summary: \"DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%）的深层原因讨论不充分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W5 raised, R1 AGREE。论文将此归因于 κ̄ 差异，但这只是 restate 了现象。残余 DR 10.21% 对 'type-safe extraction' 目标构成挑战。R1 补充：63.3% CF violations 来自 GENERIC←→X 歧义，属 schema 设计固有模糊性而非约束失败。\"\n  action_items:\n    - round: 13\n      action: \"正文中明确讨论 tight-schema 场景下的约束局限性，区分 schema 模糊性 vs 约束执行失败\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF3\"\n  summary: \"DocRED beam search 零样本仅 50-doc 子集；'resolvable via beam search' 声称适用范围过宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-SF8: DocRED beam search 仅 50 文档子集\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W4 raised, R2 AGREE with stronger evidence。Appendix Table 15 显示 DocRED ZS beam CF 仅 28.4%→21.4%，远未 'resolve'。'Resolvable' 仅在 FT 或低 κ̄ 下成立。\"\n  action_items:\n    - round: 13\n      action: \"Abstract/§5 限定 beam search claim（'substantially reduces' 而非 'resolves'）；报告 50-doc vs 全集分布差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"'formally compiles' 措辞对 semantic layer 过度（运行时规则解释非传统编译）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W7, full consensus。Grammar layer 是编译（ontology→EBNF→PDA），semantic layer 是 runtime rule-based masking。'Compile' 隐含离线静态转换，与 semantic layer 动态维护不符。\"\n  action_items:\n    - round: 13\n      action: \"区分两层编译性质：grammar = ahead-of-time compilation, semantic = rule-based runtime enforcement；或改用 'translates...into composable constraints'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF5\"\n  summary: \"缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考（读者缺乏 F1 水平锚定）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W6 raised, R2 AGREE（优先级低于 BoostCD）。不需要重跑实验，引用 GoLLIE published numbers 提供 reference point 即可。\"\n  action_items:\n    - round: 13\n      action: \"§6 或 Discussion 引用 GoLLIE 在 SciERC/DocRED 上的 published numbers，提供 F1 context\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF6\"\n  summary: \"Pumping lemma 证明使用位置索引模型，但实际 JSON 格式使用名称引用——形式化 gap\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W3 raised, R2 AGREE（presentation gap not correctness gap）。核心论证在名称引用下仍成立（name→type 随机访问同样超出 PDA 能力），但 proof sketch 应明确说明 abstraction 关系。\"\n  action_items:\n    - round: 13\n      action: \"Appendix O 增加一段说明位置索引模型是名称引用模型的 abstraction，random-access 困难在两种模型下均成立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Minor\n# ============================================================\n\n- id: \"R13-M1\"\n  summary: \"S1/S2 命名不直观，混用 'S1 (joint extraction)' 和 'Full (S1)'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-M2: S1/S2 命名易混淆\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M3, R1 AGREE。首次出现时需给出描述性名称。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M2\"\n  summary: \"Orphan bib entry (schmidt2025grammar) + 2 篇 unverified citations (formattax2026, regino2025kgcurator)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12-M1: 10 orphan entries + 1 duplicate key\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1/M5 + R1-M4。orphan 从 10 减至 1（大部分已清理），formattax2026 和 regino2025kgcurator 在 OpenAlex 未找到。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M3\"\n  summary: \"表格字体偏小（Table 1/3/4 用 resizebox 压缩 8+ 列），打印可读性受影响\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M2, R1-M2 同意（cosmetic issue）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M4\"\n  summary: \"§4 脚注 1（对称 relation 的 κ 计算）应在正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2-M4, R1 AGREE。影响 κ̄ 计算和约束 asymmetry 语义。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M5\"\n  summary: \"'Best-effort pair-based enforcement' 首次出现时需完整 inline definition\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1-M3, R2 AGREE。定义跨 §3.1 和 §3.3 分散。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-M6\"\n  summary: \"Table 25 红绿色标注违规/修正，色盲不友好\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Visual Check 发现。建议补充删除线+加粗等非颜色视觉线索。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 Divergence\n# ============================================================\n\n- id: \"R13-DIV1\"\n  summary: \"κ̄ 严重度分歧：R2 must-fix vs R1 should-fix\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1：'descriptive' 措辞已降低期望，方向性指导有价值，prefer should-fix。R2：2 数据点 trivial metric 不应列为独立 contribution，insist must-fix。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-DIV2\"\n  summary: \"Overall 评分分歧：R1=3.5 (Borderline Conference) vs R2=3.0 (Findings)\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 更看重实质贡献（decidability taxonomy + 全面评估）和修订路径；R2 认为 overclaiming pattern 累积损害可信度。R1：overclaiming 是 presentation 问题非 substance。R2：3 个 must-fix 叠加使 3.0 更准确。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-DIV3\"\n  summary: \"Excitement 分歧：R1=3.0 vs R2=2.5（decidability taxonomy 的理论价值）\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1：taxonomy 可迁移到其他 structured generation 任务，cross-pollination 价值。R2：taxonomy insight density 有限，三级分类相当直观，Proposition 1 是 confirmatory 而非 surprising。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 13 — R2 REBUT（记录但不采纳）\n# ============================================================\n\n- id: \"R13-REB1\"\n  summary: \"G(t)=∅ 边界情况：R1 minor concern, R2 REBUT\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-M5：G(t)=∅ 在极端 tokenizer edge case 下行为未讨论。R2 REBUT：XGrammar PDA 保证合法 JSON 路径上 G(t)≠∅，G(t)=∅ 属 XGrammar 实现 bug 而非 OntoCoDec 问题。不采纳为 issue。\"\n  action_items: []\n  resolution: \"R2 REBUT 成立：属 XGrammar 层 invariant 保证，非本文范围\"\n  resolution_round: 13\n\n# ============================================================\n# Prior rounds — resolved (carried forward for tracking)\n# ============================================================\n\n- id: \"R12-MF1\"\n  summary: \"'Exact enforcement' → 'best-effort' 全文替换\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Abstract/§3.3 已改为 'best-effort pair-based'。CF 透明度问题在 R13-MF2 继续追踪。\"\n  resolution_round: 13\n\n- id: \"R12-MF3\"\n  summary: \"Proposition 1 proof sketch 不完整\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Appendix O 已补完整 pumping lemma 证明。新发现的形式化 gap（位置索引 vs 名称引用）在 R13-SF6 追踪。\"\n  resolution_round: 13\n\n- id: \"R12-SF1\"\n  summary: \"语义层核心机制与 IterGen/PICARD 的概念区分不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§6 已增加 preventive vs corrective vs incremental parsing 对比。R13 未再标记。\"\n  resolution_round: 13\n\n- id: \"R12-SF6\"\n  summary: \"Entity registry 顺序依赖导致全局次优类型赋值\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"§4 已讨论贪心赋值局限性，定位为 Level 3 non-local 约束。\"\n  resolution_round: 13\n\n- id: \"R12-SF7\"\n  summary: \"'Ontology-agnostic' → 更精确表述\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"已改为 'applicable to formal ontologies and empirically-derived type constraints'。\"\n  resolution_round: 13\n\n- id: \"R12-VL1\"\n  summary: \"主文前 4 页无任何 display item，框架论文缺架构图\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 框架图已加入 §3（page 3）。Visual Check 确认其为全文首个视觉锚点。\"\n  resolution_round: 13\n\n- id: \"R12-VL2\"\n  summary: \"主文 8 页正文零 Figure，全部 Figure 在附录\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 1 已入主文。主文 1 figure + 5 tables = 6 display items。\"\n  resolution_round: 13\n\n- id: \"R12-M4\"\n  summary: \"Eq.(2) conjunction 未明确为 element-wise AND\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Eq.(2) 已加注 'element-wise AND over vocabulary V'。\"\n  resolution_round: 13\n\n- id: \"R11-MF1\"\n  summary: \"'Near-lossless' 叙事未充分呈现 CF trade-off\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"R11 Paper Agent 完成 two-tier narrative 重构。\"\n  resolution_round: 11\n\n- id: \"R11-MF2\"\n  summary: \"缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 对比\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"d063 GoLLIE 实验完成。§6 已加 qualitative positioning。\"\n  resolution_round: 11\n\n- id: \"R10-MF1\"\n  summary: \"'Ontology Constraints' → 'Schema Constraints'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Title 已更新。\"\n  resolution_round: 11\n\n- id: \"R10-MF2\"\n  summary: \"缺少 ARR Responsible NLP Research Checklist\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"checklist.tex 已添加。\"\n  resolution_round: 11\n"
  }
}
```

</details>

---


### Tool result

_source line 1354 · 2026-05-20T18:52:09.777195+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 16203}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-20T18:54:51.240759+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 13 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Target Venue**: EMNLP 2026 (via ARR May cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1（方法严谨性 + 实验有效性）, R2（新颖性 + 完整性 + 写作质量）\n**审稿模式**: Fresh（无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的双层架构：grammar layer（CFG，保证 JSON 结构和词汇约束）和 semantic layer（prefix-decidable with state，通过运行时 entity registry 执行 best-effort pair-based domain/range 类型约束，含 grammar-first fallback）。在 SciERC、DocRED、WikiEvents 三个数据集上，对 4 个模型（7–70B，三个 tokenizer 族）进行了系统评估。LoRA + greedy S1 将 DR 降至 ≤0.09%，R-F1 ±0.6pp；beam (k=4) 在 SciERC 上消除所有违规（1.54× latency）。论文同时引入 constraint tightness κ̄ 作为描述性指标。\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计与全面的消融分析（R1-S3, R2-S1, consensus）。** 五路消融（Unconstrained / Grammar / Semantic / Full S1 / Full S2）清晰隔离各层贡献；跨 3 数据集 × 4 模型 × 多配置的验证覆盖面广。Bootstrap 显著性检验（B=10,000）和配对统计比较体现了严谨方法论。这是 constrained decoding for IE 领域最全面的评估之一。\n\n**S2. 有 principled 的形式化分析支撑架构决策（R1-S1, R2-S2, consensus）。** 三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）为 IE 类型约束按可判定性分层提供了清晰框架。Proposition 1（pumping lemma 证明 Level 2 ⊄ Level 1）给出了双层架构的 formal justification。Enabling dependency 在 Table 1 中得到实验验证（Semantic-only 仅 24% DR 降幅）。\n\n**S3. 工程完整性和可部署性（R2-S3, R1-S2）。** Tokenizer-agnostic continuation masking 处理 BPE/SentencePiece 差异；grammar-first fallback 保证 JSON 完整性；运行时开销适中（+10–13%）；编译时间 <0.5s；框架无修改即可从 RE 扩展到 EE（245 constraints）。\n\n**S4. Fine-tuning composability 是重要的实用价值（R2-S4, R1-S3）。** Table 2 表明约束可与 LoRA 组合使用而不损害 R-F1（p>0.05），将残余 DR 从 1–2% 压至 ≤0.09%。对实际部署场景比零样本结果更有说服力。\n\n**S5. 诚实的 limitation 讨论（R1-S4）。** 论文明确承认 CF 的模型依赖性、WikiEvents 的初步性质、70B 评估的有限性、κ̄ 仅为描述性指标。Limitations section 覆盖多数已知局限。附录极丰富（23 页），包含完整证明、per-relation 分析、beam 兼容性、prompt sensitivity、error analysis 等。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，4 项全员共识 + 1 项有分歧）\n\n**MF1. [critical, consensus] 正文超 8 页限制。** Section 7 Discussion and Conclusion 约 11 行溢出至第 9 页。EMNLP 2026 via ARR 严格限制长文正文 ≤ 8 页。格式违规可能导致 desk reject。机械性可修复（压缩 §7/§6/§5 冗余）但不可忽视。(R2-W1, R1-M1→升级, Visual Check critical)\n\n**MF2. [critical, consensus] CF 代价在 Abstract/Introduction 中被系统性低估。** Abstract 用 \"modest CF costs\" 描述以下实际数据是误导性的：SciERC 零样本 CF 0.08%→9.90%（+123×）；WikiEvents 零样本 CF 15–21%；DocRED beam 零样本 CF 28.4%→21.4%（远未 \"resolve\"）。Introduction 完全未提及 CF。隐藏主要副作用降低论文可信度。Abstract 应明确写出 CF 范围和条件；Introduction 应讨论 DR↔CF trade-off。(R2-W2, R1 AGREE 升级)\n\n**MF3. [critical, consensus] 缺少最直接可比的 IE constrained decoding baseline 量化对比。** BoostCD (Sakota et al., EMNLP 2025) 和 IterGen (Ugare et al., 2025) 在 §6 被引用但实验中完全无对比。BoostCD 与 GCD 同团队，GCD 已在 SciERC 上有结果（§5.1 引用），因此 BoostCD 极可能覆盖相同 benchmark。§6 称 \"different benchmarks preclude direct comparison\" 但未提供证据支撑。缺失最自然 baseline 使 Contribution 3 \"first systematic evaluation\" 的声称站不住脚。(R1-W1, R2 AGREE 采纳)\n\n**MF4. [critical, consensus] WikiEvents fine-tuning 仅 20 文档测试集，Contribution 3 措辞过度。** 零样本 246 文档尚可，但 FT composability 的 20 文档测试集 CIs 宽达 ±0.05–0.06，无法支撑 \"systematic evaluation\" 和 \"framework generalizes to event extraction\" 的措辞。另：零样本 entity F1 从 0→12–18% 主要来自格式修复（unconstrained 输出无法被 parser 处理）而非语义提取改善。应降级为 \"preliminary demonstration\"。(R1-W2, R2-W6 consensus)\n\n**MF5. [critical/warning, divergence] κ̄ 作为独立 Contribution 2 定位过高。** κ̄ = 1−|σ(r)|/|E|² 本质上是约束表归一化密度。仅 2 个数据点验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842）。κ̄ 对 Mistral 预测失效（SciERC DR 降幅 76% vs 期望 94–99%），说明无 confusability 协变量 κ̄ 指导价值有限。**R2 列为 must-fix（不应列为独立 contribution），R1 同意问题但 prefer should-fix（方向性指导仍有价值）。** 建议至少降级为分析工具，整合入实验讨论。\n\n### Should-Fix（影响评分但不一票否决，6 项）\n\n**SF1. \"any autoregressive LM\" 声称超出验证范围。** 主要实验 7–8B，70B 仅 preliminary，无 <7B / API-only 验证。§1 仍有 \"applies to any autoregressive LM\"。(R2-W4, R1 AGREE)\n\n**SF2. DocRED 零样本 DR 降幅仅 45% 的讨论不充分。** 论文将此归因于 κ̄ 差异但只是 restate 了现象。残余 DR 10.21%（每 10 个 triple 约 1 个违规）对 \"type-safe extraction\" 构成挑战。深层原因：GENERIC←→X 歧义占 63.3% CF violations，属 schema 固有模糊性。(R2-W5, R1 AGREE)\n\n**SF3. DocRED beam search 零样本仅 50-doc 子集（998 的 5%）。** Abstract/§5 的 \"resolvable via beam search\" 在 DocRED 上证据不足。Appendix Table 15 显示 CF 仅 28.4%→21.4%。\"Resolvable\" 仅在 FT 或低 κ̄ 下成立。(R1-W4, R2 AGREE)\n\n**SF4. \"formally compiles\" 措辞对 semantic layer 过度。** Grammar layer 是传统编译（ontology→EBNF→PDA）；semantic layer 是运行时规则解释（runtime rule-based masking）。更准确：\"compile-time grammar generation + runtime constraint interpretation\"。(R1-W5, R2-W7, consensus)\n\n**SF5. 缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考。** 读者缺乏 F1 水平锚定——\"7–8B model + OntoCoDec, R-F1 40–46%\" 在领域中处于什么水平？引用 GoLLIE published numbers 即可，不需重跑实验。(R1-W6, R2 AGREE)\n\n**SF6. Pumping lemma 证明存在形式化 gap（presentation, not correctness）。** Proof sketch 使用位置索引模型，但实际 JSON 使用名称字符串引用。核心论证在名称引用下仍成立（name→type 随机访问超出 PDA 能力），但应明确说明 abstraction 关系。(R1-W3, R2 AGREE)\n\n### Minor（不影响接收，6 项）\n\n- **M1.** S1/S2 命名不直观，混用 \"S1 (joint extraction)\" 和 \"Full (S1)\"。(R2-M3, R1 AGREE)\n- **M2.** Orphan bib entry（schmidt2025grammar）+ 2 篇 unverified citations（formattax2026, regino2025kgcurator）。(R2-M1/M5, R1-M4)\n- **M3.** 表格字体偏小（Table 1/3/4 用 resizebox 压缩 8+ 列）。(R2-M2, R1-M2)\n- **M4.** §4 脚注 1（对称 relation 的 κ 计算）影响 κ̄ 语义，应在正文讨论。(R2-M4, R1 AGREE)\n- **M5.** \"Best-effort pair-based enforcement\" 首次出现时需完整 inline definition。(R1-M3, R2 AGREE)\n- **M6.** Table 25 红绿色标注违规/修正，色盲不友好（Visual Check 发现）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **正文超页 must-fix**：R1 初审列为 minor，交叉后升级为 must-fix\n2. **CF 透明度 must-fix**：R1 初审列为 should-fix（聚焦 beam search claim），交叉后接受 R2 的更全面角度，升级为 must-fix\n3. **BoostCD 缺失 must-fix**：R2 初审遗漏，交叉后采纳 R1 的 must-fix\n4. **WikiEvents 统计效力**：R1 列 critical，R2 列 warning 但承认 R1 理由成立\n5. **所有 Should-Fix 和 Minor**：全部 AGREE（仅 R1-M5 G(t)=∅ 边界情况被 R2 REBUT——XGrammar PDA 保证合法路径上 G(t)≠∅，属实现层 invariant 而非框架问题）\n\n---\n\n## Reviewer Divergence\n\n**DIV1. κ̄ 严重度**：R2 = must-fix（不应列为独立 contribution），R1 = should-fix（方向性指导有价值）。核心分歧：R2 认为 2 数据点的 trivial metric 列为 Contribution 2 是 overclaiming；R1 认为 \"descriptive\" 措辞已降低期望且 deployment heuristic 有实用价值。\n\n**DIV2. Overall 评分**：R1 = 3.5（Borderline Conference），R2 = 3.0（Findings）。\n- R1 逻辑：核心技术 sound，实验覆盖广，overclaiming 是 presentation 问题非 substance 问题，修订路径明确\n- R2 逻辑：overclaiming pattern 跨多个维度（\"modest\" CF / κ̄ contribution / \"any LM\" / \"formally compiles\"）累积损害可信度；3 个 must-fix 叠加使 3.0 更准确\n- R1 交叉后承认 R2 的 overclaiming pattern 论点成立，但认为 Limitations section 的诚实性和附录深度（33 页）部分抵消\n- R2 交叉后承认 decidability taxonomy 有 marginal 迁移价值，但维持 3.0\n\n**DIV3. Excitement**：R1 = 3.0（decidability taxonomy 有跨领域迁移价值），R2 = 2.5（taxonomy insight density 有限，三级分类相当直观，Proposition 1 是 confirmatory 而非 surprising）。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** [R2-Q1] Grammar-first fallback 在 36.6% 的 type-bearing positions 触发（§4, SciERC 零样本）。这是否意味着约三分之一的类型位置实际上没有任何类型约束？\"Type-constrained extraction\" 标题是否过度承诺？\n\n**Q2.** [R1-Q2] BoostCD 在 SciERC/DocRED 上的 constrained decoding 结果是什么？如果不可比，请具体说明原因（约束类型不同？输出格式不同？其他？）\n\n**Q3.** [R1-Q4] LoRA fine-tuning 是在有约束还是无约束解码条件下训练的？如果无约束训练，fine-tuned 模型输出分布与 constrained decoding mask 之间可能存在 distribution mismatch。\n\n**Q4.** [R2-Q2] Llama SciERC fine-tuned 残余 DR 0.09%（36 violations：entity type errors 39%, schema coverage gaps 33%, model errors 28%）——33% 来自 schema coverage gaps。这对新领域部署有何影响？\n\n**Q5.** [R2-Q4] WikiEvents Grammar-only 行在 Table 5 中 F1 标记 \"---\"，但 grammar-only 应可生成结构化输出。是因为 RoV 64–77% 导致无法可靠评估吗？\n\n**Q6.** [R2-Q5] 论文引用 Tam et al. (2024) 称 \"extraction tasks are robust to format constraints\"，但 Tam et al. 的实验非 IE-specific。是否有 IE-specific 证据？CRANE (Banerjee et al., 2025) 暗示 constrained decoding 在结构化任务中也有隐性代价。\n\n**Q7.** [R1-Q1] Pumping lemma 证明中 pumping 操作如何破坏名称引用下的类型一致性？位置偏移的推理如何适用于名称引用格式？\n\n---\n\n## Missing References\n\n1. **BoostCD (Sakota et al., EMNLP 2025)**: 已在 §6 引用但缺乏实验对比——最直接的 IE constrained decoding competitor (R1-W1, R2 adopted)\n2. **GenIE (Josifoski et al., 2022)**: 最早系统化应用 constrained decoding 于 IE 的工作之一，主体 §6 遗漏（仅在附录 B）(R1)\n3. **NNF (Nusgart et al., 2025, \"Constrained Decoding with Grammars and Lookahead\")**: grammar-constrained decoding lookahead，与 grammar-first fallback 相关 (R1)\n4. **LasUIE (Fei et al., 2022)**: 结构化生成 + IE 的早期工作 (R2)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目配置中未启用 `external_review.paperreview_ai`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2026-05-20T18:36–18:40, 约 4 分钟）\n\n| 严重度 | 数量 | 关键发现 |\n|--------|------|----------|\n| Critical | 1 | 正文溢出至 p9（与 MF1 一致） |\n| Warning | 3 | 前 2 页纯文本无视觉锚点；p8 整页纯文本（Related Work + Conclusion）；附录 B 连续 3 页纯文本 |\n| Info | 8 | Figure 1 位置合适（p3）；pp5–7 table 密度良好（5 tables/3 pages）；无 margin 溢出、未解析引用、排版错误；Table 25 红绿色不色盲友好；末页 50% 空白可接受 |\n\n**主文 display item 统计**: 1 figure + 5 tables = 6 items / 8 pages（合理范围 5–8）。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.0 | 2.5 | **2.75** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4 | 4 | **4** |\n\n### Overall: 3.0 — Findings\n\n**综合评分取 3.0（Findings）的理由：**\n\n1. **4 项全员共识 Must-Fix + 1 项有争议 Must-Fix**：正文超页（desk reject 风险）、CF 代价被系统性低估（可信度问题）、缺少最直接 baseline 对比（贡献 scope 问题）、WikiEvents 统计效力不足（claim 支撑问题）、κ̄ 贡献定位过高。这些问题不是孤立的——它们构成了一个 **overclaiming pattern**：论文在多个维度（\"modest\" CF / \"formally compiles\" / \"any autoregressive LM\" / \"systematic evaluation\" / κ̄ as contribution）对自身贡献的呈现高于实际支撑。\n\n2. **核心技术贡献 sound 但 novelty 有限**：decidability taxonomy 是有用的形式化贡献，但三级分类相当直观（CF/stateful/non-local），Proposition 1 是 confirmatory 而非 surprising。双层架构（grammar mask ∩ semantic mask）是已有技术的 principled 组合，非 novel mechanism。\n\n3. **实验全面但有关键缺口**：缺少 BoostCD/IterGen 对比是最实质性的缺陷——如果 BoostCD 在 SciERC 上的 DR 降幅可比，OntoCoDec 的增量贡献将大幅缩水。\n\n4. **明确的修订升级路径**：补充 BoostCD 对比、修正 CF 叙述、降级 κ̄ 定位、限定 claim 范围、压缩页数——这些修订均不改变核心技术贡献，修订后有望达到 3.5（Borderline Conference）。\n\n### 一句话总结\n\n一篇技术扎实、评估全面的系统论文，decidability taxonomy 和双层约束执行框架设计干净；但存在 overclaiming pattern（CF 代价低估、κ̄ 贡献包装、声称范围过宽），且缺少与最直接 IE constrained decoding competitor（BoostCD）的量化对比。当前状态为 Findings 级别，修订后有明确的 Borderline Conference 升级路径。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"applies to any autoregressive LM\" → 限定为 \"with logits access, validated on 7–70B\"\n- Contribution 2: κ̄ 从独立 contribution 降级为 \"we additionally introduce...\"\n- Contribution 3: \"systematic evaluation...extends to event extraction\" → 区分 RE (systematic) 和 EE (preliminary demonstration)\n- CF trade-off 应在 Intro 即提及（当前完全缺失）\n\n### Abstract\n- \"modest CF costs\" → 写出具体范围：\"CF rates of 0–9.9% (zero-shot) to ≤1.2% (fine-tuned)\"\n- \"resolvable via beam search\" → \"substantially reduced by beam search under low κ̄ or with fine-tuning\"\n- \"formally compiles\" → 考虑 \"translates\" 或区分 compile-time/runtime\n\n### §3 Method\n- Proposition 1 proof sketch: 增加名称引用 vs 位置索引的 abstraction 说明\n- \"best-effort pair-based enforcement\" 首次出现时给完整 inline definition\n\n### §4 Constraint Composition\n- 脚注 1（对称 relation 处理）移入正文\n- Grammar-first fallback cascade 分析需更明确定量（当前 36.6% 触发率的后果分析分散）\n\n### §5 Experiments\n- WikiEvents FT: 明确 n=20 的统计效力限制，降级为 preliminary\n- DocRED beam: 限定 \"resolvable\" claim 的适用范围\n- 补充 BoostCD/GCD 在 SciERC 上的数字对比\n- 提供 GoLLIE 的 F1 reference point\n\n### §6 Related Work\n- GenIE (Josifoski et al., 2022) 从附录移入主体\n- \"formally compiles\" vs PICARD/Mündler et al. 的区分已到位，但需弱化 \"formally\" 措辞\n- \"different benchmarks preclude direct comparison\" with BoostCD — 需提供具体证据或撤回此声称\n\n### §7 Discussion and Conclusion\n- 压缩至 8 页限制内\n- Beam search 推荐应限定条件（\"for low-κ̄ schemas or fine-tuned settings\"）\n\n### Appendix O (Pumping Lemma Proof)\n- 增加位置索引→名称引用的 abstraction paragraph\n\n### Formatting\n- S1/S2 命名统一为 \"single-pass S1\" / \"two-pass S2\"\n- 删除 orphan bib entry (schmidt2025grammar)\n- 验证 formattax2026, regino2025kgcurator 引用完整性\n- Table 25 增加非颜色视觉线索（色盲友好）",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
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
    "report": "# Round 13 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Target Venue**: EMNLP 2026 (via ARR May cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1（方法严谨性 + 实验有效性）, R2（新颖性 + 完整性 + 写作质量）\n**审稿模式**: Fresh（无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的双层架构：grammar layer（CFG，保证 JSON 结构和词汇约束）和 semantic layer（prefix-decidable with state，通过运行时 entity registry 执行 best-effort pair-based domain/range 类型约束，含 grammar-first fallback）。在 SciERC、DocRED、WikiEvents 三个数据集上，对 4 个模型（7–70B，三个 tokenizer 族）进行了系统评估。LoRA + greedy S1 将 DR 降至 ≤0.09%，R-F1 ±0.6pp；beam (k=4) 在 SciERC 上消除所有违规（1.54× latency）。论文同时引入 constraint tightness κ̄ 作为描述性指标。\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计与全面的消融分析（R1-S3, R2-S1, consensus）。** 五路消融（Unconstrained / Grammar / Semantic / Full S1 / Full S2）清晰隔离各层贡献；跨 3 数据集 × 4 模型 × 多配置的验证覆盖面广。Bootstrap 显著性检验（B=10,000）和配对统计比较体现了严谨方法论。这是 constrained decoding for IE 领域最全面的评估之一。\n\n**S2. 有 principled 的形式化分析支撑架构决策（R1-S1, R2-S2, consensus）。** 三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）为 IE 类型约束按可判定性分层提供了清晰框架。Proposition 1（pumping lemma 证明 Level 2 ⊄ Level 1）给出了双层架构的 formal justification。Enabling dependency 在 Table 1 中得到实验验证（Semantic-only 仅 24% DR 降幅）。\n\n**S3. 工程完整性和可部署性（R2-S3, R1-S2）。** Tokenizer-agnostic continuation masking 处理 BPE/SentencePiece 差异；grammar-first fallback 保证 JSON 完整性；运行时开销适中（+10–13%）；编译时间 <0.5s；框架无修改即可从 RE 扩展到 EE（245 constraints）。\n\n**S4. Fine-tuning composability 是重要的实用价值（R2-S4, R1-S3）。** Table 2 表明约束可与 LoRA 组合使用而不损害 R-F1（p>0.05），将残余 DR 从 1–2% 压至 ≤0.09%。对实际部署场景比零样本结果更有说服力。\n\n**S5. 诚实的 limitation 讨论（R1-S4）。** 论文明确承认 CF 的模型依赖性、WikiEvents 的初步性质、70B 评估的有限性、κ̄ 仅为描述性指标。Limitations section 覆盖多数已知局限。附录极丰富（23 页），包含完整证明、per-relation 分析、beam 兼容性、prompt sensitivity、error analysis 等。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，4 项全员共识 + 1 项有分歧）\n\n**MF1. [critical, consensus] 正文超 8 页限制。** Section 7 Discussion and Conclusion 约 11 行溢出至第 9 页。EMNLP 2026 via ARR 严格限制长文正文 ≤ 8 页。格式违规可能导致 desk reject。机械性可修复（压缩 §7/§6/§5 冗余）但不可忽视。(R2-W1, R1-M1→升级, Visual Check critical)\n\n**MF2. [critical, consensus] CF 代价在 Abstract/Introduction 中被系统性低估。** Abstract 用 \"modest CF costs\" 描述以下实际数据是误导性的：SciERC 零样本 CF 0.08%→9.90%（+123×）；WikiEvents 零样本 CF 15–21%；DocRED beam 零样本 CF 28.4%→21.4%（远未 \"resolve\"）。Introduction 完全未提及 CF。隐藏主要副作用降低论文可信度。Abstract 应明确写出 CF 范围和条件；Introduction 应讨论 DR↔CF trade-off。(R2-W2, R1 AGREE 升级)\n\n**MF3. [critical, consensus] 缺少最直接可比的 IE constrained decoding baseline 量化对比。** BoostCD (Sakota et al., EMNLP 2025) 和 IterGen (Ugare et al., 2025) 在 §6 被引用但实验中完全无对比。BoostCD 与 GCD 同团队，GCD 已在 SciERC 上有结果（§5.1 引用），因此 BoostCD 极可能覆盖相同 benchmark。§6 称 \"different benchmarks preclude direct comparison\" 但未提供证据支撑。缺失最自然 baseline 使 Contribution 3 \"first systematic evaluation\" 的声称站不住脚。(R1-W1, R2 AGREE 采纳)\n\n**MF4. [critical, consensus] WikiEvents fine-tuning 仅 20 文档测试集，Contribution 3 措辞过度。** 零样本 246 文档尚可，但 FT composability 的 20 文档测试集 CIs 宽达 ±0.05–0.06，无法支撑 \"systematic evaluation\" 和 \"framework generalizes to event extraction\" 的措辞。另：零样本 entity F1 从 0→12–18% 主要来自格式修复（unconstrained 输出无法被 parser 处理）而非语义提取改善。应降级为 \"preliminary demonstration\"。(R1-W2, R2-W6 consensus)\n\n**MF5. [critical/warning, divergence] κ̄ 作为独立 Contribution 2 定位过高。** κ̄ = 1−|σ(r)|/|E|² 本质上是约束表归一化密度。仅 2 个数据点验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842）。κ̄ 对 Mistral 预测失效（SciERC DR 降幅 76% vs 期望 94–99%），说明无 confusability 协变量 κ̄ 指导价值有限。**R2 列为 must-fix（不应列为独立 contribution），R1 同意问题但 prefer should-fix（方向性指导仍有价值）。** 建议至少降级为分析工具，整合入实验讨论。\n\n### Should-Fix（影响评分但不一票否决，6 项）\n\n**SF1. \"any autoregressive LM\" 声称超出验证范围。** 主要实验 7–8B，70B 仅 preliminary，无 <7B / API-only 验证。§1 仍有 \"applies to any autoregressive LM\"。(R2-W4, R1 AGREE)\n\n**SF2. DocRED 零样本 DR 降幅仅 45% 的讨论不充分。** 论文将此归因于 κ̄ 差异但只是 restate 了现象。残余 DR 10.21%（每 10 个 triple 约 1 个违规）对 \"type-safe extraction\" 构成挑战。深层原因：GENERIC←→X 歧义占 63.3% CF violations，属 schema 固有模糊性。(R2-W5, R1 AGREE)\n\n**SF3. DocRED beam search 零样本仅 50-doc 子集（998 的 5%）。** Abstract/§5 的 \"resolvable via beam search\" 在 DocRED 上证据不足。Appendix Table 15 显示 CF 仅 28.4%→21.4%。\"Resolvable\" 仅在 FT 或低 κ̄ 下成立。(R1-W4, R2 AGREE)\n\n**SF4. \"formally compiles\" 措辞对 semantic layer 过度。** Grammar layer 是传统编译（ontology→EBNF→PDA）；semantic layer 是运行时规则解释（runtime rule-based masking）。更准确：\"compile-time grammar generation + runtime constraint interpretation\"。(R1-W5, R2-W7, consensus)\n\n**SF5. 缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考。** 读者缺乏 F1 水平锚定——\"7–8B model + OntoCoDec, R-F1 40–46%\" 在领域中处于什么水平？引用 GoLLIE published numbers 即可，不需重跑实验。(R1-W6, R2 AGREE)\n\n**SF6. Pumping lemma 证明存在形式化 gap（presentation, not correctness）。** Proof sketch 使用位置索引模型，但实际 JSON 使用名称字符串引用。核心论证在名称引用下仍成立（name→type 随机访问超出 PDA 能力），但应明确说明 abstraction 关系。(R1-W3, R2 AGREE)\n\n### Minor（不影响接收，6 项）\n\n- **M1.** S1/S2 命名不直观，混用 \"S1 (joint extraction)\" 和 \"Full (S1)\"。(R2-M3, R1 AGREE)\n- **M2.** Orphan bib entry（schmidt2025grammar）+ 2 篇 unverified citations（formattax2026, regino2025kgcurator）。(R2-M1/M5, R1-M4)\n- **M3.** 表格字体偏小（Table 1/3/4 用 resizebox 压缩 8+ 列）。(R2-M2, R1-M2)\n- **M4.** §4 脚注 1（对称 relation 的 κ 计算）影响 κ̄ 语义，应在正文讨论。(R2-M4, R1 AGREE)\n- **M5.** \"Best-effort pair-based enforcement\" 首次出现时需完整 inline definition。(R1-M3, R2 AGREE)\n- **M6.** Table 25 红绿色标注违规/修正，色盲不友好（Visual Check 发现）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **正文超页 must-fix**：R1 初审列为 minor，交叉后升级为 must-fix\n2. **CF 透明度 must-fix**：R1 初审列为 should-fix（聚焦 beam search claim），交叉后接受 R2 的更全面角度，升级为 must-fix\n3. **BoostCD 缺失 must-fix**：R2 初审遗漏，交叉后采纳 R1 的 must-fix\n4. **WikiEvents 统计效力**：R1 列 critical，R2 列 warning 但承认 R1 理由成立\n5. **所有 Should-Fix 和 Minor**：全部 AGREE（仅 R1-M5 G(t)=∅ 边界情况被 R2 REBUT——XGrammar PDA 保证合法路径上 G(t)≠∅，属实现层 invariant 而非框架问题）\n\n---\n\n## Reviewer Divergence\n\n**DIV1. κ̄ 严重度**：R2 = must-fix（不应列为独立 contribution），R1 = should-fix（方向性指导有价值）。核心分歧：R2 认为 2 数据点的 trivial metric 列为 Contribution 2 是 overclaiming；R1 认为 \"descriptive\" 措辞已降低期望且 deployment heuristic 有实用价值。\n\n**DIV2. Overall 评分**：R1 = 3.5（Borderline Conference），R2 = 3.0（Findings）。\n- R1 逻辑：核心技术 sound，实验覆盖广，overclaiming 是 presentation 问题非 substance 问题，修订路径明确\n- R2 逻辑：overclaiming pattern 跨多个维度（\"modest\" CF / κ̄ contribution / \"any LM\" / \"formally compiles\"）累积损害可信度；3 个 must-fix 叠加使 3.0 更准确\n- R1 交叉后承认 R2 的 overclaiming pattern 论点成立，但认为 Limitations section 的诚实性和附录深度（33 页）部分抵消\n- R2 交叉后承认 decidability taxonomy 有 marginal 迁移价值，但维持 3.0\n\n**DIV3. Excitement**：R1 = 3.0（decidability taxonomy 有跨领域迁移价值），R2 = 2.5（taxonomy insight density 有限，三级分类相当直观，Proposition 1 是 confirmatory 而非 surprising）。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** [R2-Q1] Grammar-first fallback 在 36.6% 的 type-bearing positions 触发（§4, SciERC 零样本）。这是否意味着约三分之一的类型位置实际上没有任何类型约束？\"Type-constrained extraction\" 标题是否过度承诺？\n\n**Q2.** [R1-Q2] BoostCD 在 SciERC/DocRED 上的 constrained decoding 结果是什么？如果不可比，请具体说明原因（约束类型不同？输出格式不同？其他？）\n\n**Q3.** [R1-Q4] LoRA fine-tuning 是在有约束还是无约束解码条件下训练的？如果无约束训练，fine-tuned 模型输出分布与 constrained decoding mask 之间可能存在 distribution mismatch。\n\n**Q4.** [R2-Q2] Llama SciERC fine-tuned 残余 DR 0.09%（36 violations：entity type errors 39%, schema coverage gaps 33%, model errors 28%）——33% 来自 schema coverage gaps。这对新领域部署有何影响？\n\n**Q5.** [R2-Q4] WikiEvents Grammar-only 行在 Table 5 中 F1 标记 \"---\"，但 grammar-only 应可生成结构化输出。是因为 RoV 64–77% 导致无法可靠评估吗？\n\n**Q6.** [R2-Q5] 论文引用 Tam et al. (2024) 称 \"extraction tasks are robust to format constraints\"，但 Tam et al. 的实验非 IE-specific。是否有 IE-specific 证据？CRANE (Banerjee et al., 2025) 暗示 constrained decoding 在结构化任务中也有隐性代价。\n\n**Q7.** [R1-Q1] Pumping lemma 证明中 pumping 操作如何破坏名称引用下的类型一致性？位置偏移的推理如何适用于名称引用格式？\n\n---\n\n## Missing References\n\n1. **BoostCD (Sakota et al., EMNLP 2025)**: 已在 §6 引用但缺乏实验对比——最直接的 IE constrained decoding competitor (R1-W1, R2 adopted)\n2. **GenIE (Josifoski et al., 2022)**: 最早系统化应用 constrained decoding 于 IE 的工作之一，主体 §6 遗漏（仅在附录 B）(R1)\n3. **NNF (Nusgart et al., 2025, \"Constrained Decoding with Grammars and Lookahead\")**: grammar-constrained decoding lookahead，与 grammar-first fallback 相关 (R1)\n4. **LasUIE (Fei et al., 2022)**: 结构化生成 + IE 的早期工作 (R2)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目配置中未启用 `external_review.paperreview_ai`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2026-05-20T18:36–18:40, 约 4 分钟）\n\n| 严重度 | 数量 | 关键发现 |\n|--------|------|----------|\n| Critical | 1 | 正文溢出至 p9（与 MF1 一致） |\n| Warning | 3 | 前 2 页纯文本无视觉锚点；p8 整页纯文本（Related Work + Conclusion）；附录 B 连续 3 页纯文本 |\n| Info | 8 | Figure 1 位置合适（p3）；pp5–7 table 密度良好（5 tables/3 pages）；无 margin 溢出、未解析引用、排版错误；Table 25 红绿色不色盲友好；末页 50% 空白可接受 |\n\n**主文 display item 统计**: 1 figure + 5 tables = 6 items / 8 pages（合理范围 5–8）。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.0 | 2.5 | **2.75** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4 | 4 | **4** |\n\n### Overall: 3.0 — Findings\n\n**综合评分取 3.0（Findings）的理由：**\n\n1. **4 项全员共识 Must-Fix + 1 项有争议 Must-Fix**：正文超页（desk reject 风险）、CF 代价被系统性低估（可信度问题）、缺少最直接 baseline 对比（贡献 scope 问题）、WikiEvents 统计效力不足（claim 支撑问题）、κ̄ 贡献定位过高。这些问题不是孤立的——它们构成了一个 **overclaiming pattern**：论文在多个维度（\"modest\" CF / \"formally compiles\" / \"any autoregressive LM\" / \"systematic evaluation\" / κ̄ as contribution）对自身贡献的呈现高于实际支撑。\n\n2. **核心技术贡献 sound 但 novelty 有限**：decidability taxonomy 是有用的形式化贡献，但三级分类相当直观（CF/stateful/non-local），Proposition 1 是 confirmatory 而非 surprising。双层架构（grammar mask ∩ semantic mask）是已有技术的 principled 组合，非 novel mechanism。\n\n3. **实验全面但有关键缺口**：缺少 BoostCD/IterGen 对比是最实质性的缺陷——如果 BoostCD 在 SciERC 上的 DR 降幅可比，OntoCoDec 的增量贡献将大幅缩水。\n\n4. **明确的修订升级路径**：补充 BoostCD 对比、修正 CF 叙述、降级 κ̄ 定位、限定 claim 范围、压缩页数——这些修订均不改变核心技术贡献，修订后有望达到 3.5（Borderline Conference）。\n\n### 一句话总结\n\n一篇技术扎实、评估全面的系统论文，decidability taxonomy 和双层约束执行框架设计干净；但存在 overclaiming pattern（CF 代价低估、κ̄ 贡献包装、声称范围过宽），且缺少与最直接 IE constrained decoding competitor（BoostCD）的量化对比。当前状态为 Findings 级别，修订后有明确的 Borderline Conference 升级路径。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"applies to any autoregressive LM\" → 限定为 \"with logits access, validated on 7–70B\"\n- Contribution 2: κ̄ 从独立 contribution 降级为 \"we additionally introduce...\"\n- Contribution 3: \"systematic evaluation...extends to event extraction\" → 区分 RE (systematic) 和 EE (preliminary demonstration)\n- CF trade-off 应在 Intro 即提及（当前完全缺失）\n\n### Abstract\n- \"modest CF costs\" → 写出具体范围：\"CF rates of 0–9.9% (zero-shot) to ≤1.2% (fine-tuned)\"\n- \"resolvable via beam search\" → \"substantially reduced by beam search under low κ̄ or with fine-tuning\"\n- \"formally compiles\" → 考虑 \"translates\" 或区分 compile-time/runtime\n\n### §3 Method\n- Proposition 1 proof sketch: 增加名称引用 vs 位置索引的 abstraction 说明\n- \"best-effort pair-based enforcement\" 首次出现时给完整 inline definition\n\n### §4 Constraint Composition\n- 脚注 1（对称 relation 处理）移入正文\n- Grammar-first fallback cascade 分析需更明确定量（当前 36.6% 触发率的后果分析分散）\n\n### §5 Experiments\n- WikiEvents FT: 明确 n=20 的统计效力限制，降级为 preliminary\n- DocRED beam: 限定 \"resolvable\" claim 的适用范围\n- 补充 BoostCD/GCD 在 SciERC 上的数字对比\n- 提供 GoLLIE 的 F1 reference point\n\n### §6 Related Work\n- GenIE (Josifoski et al., 2022) 从附录移入主体\n- \"formally compiles\" vs PICARD/Mündler et al. 的区分已到位，但需弱化 \"formally\" 措辞\n- \"different benchmarks preclude direct comparison\" with BoostCD — 需提供具体证据或撤回此声称\n\n### §7 Discussion and Conclusion\n- 压缩至 8 页限制内\n- Beam search 推荐应限定条件（\"for low-κ̄ schemas or fine-tuned settings\"）\n\n### Appendix O (Pumping Lemma Proof)\n- 增加位置索引→名称引用的 abstraction paragraph\n\n### Formatting\n- S1/S2 命名统一为 \"single-pass S1\" / \"two-pass S2\"\n- 删除 orphan bib entry (schmidt2025grammar)\n- 验证 formattax2026, regino2025kgcurator 引用完整性\n- Table 25 增加非颜色视觉线索（色盲友好）",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-20T18:54:55.221340+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3980
}
```

</details>

---


### Assistant

_source line 1357 · 2026-05-20T18:55:06.469534+00:00_

审稿报告已投递。

**Round 13 审稿完成**：

- **Overall: 3.0（Findings）**
- **4 项 Must-Fix 全员共识**：正文超页、CF 代价被低估、BoostCD 缺失对比、WikiEvents 统计效力
- **1 项 Must-Fix 有分歧**：κ̄ 贡献定位（R2 critical / R1 should-fix）
- **6 项 Should-Fix**：model scope 声称、DocRED DR 讨论、beam search claim、"formally compiles" 措辞、GoLLIE 参考、pumping lemma gap
- **评分分歧**：R1=3.5 vs R2=3.0，综合取 3.0——overclaiming pattern 跨多维度累积损害可信度
- **修订路径明确**：补 BoostCD 对比 + 修正 CF/κ̄ 叙述 + 限定 claims + 压缩页数 → 可达 3.5

Issue Tracker 已同步更新至 `review_issues.yaml`（R12 已修复项标记 resolved，R13 新发现全部录入）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1358 · 2026-05-20T18:55:09.092380+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

核心结论：
- 对 R1 的 8 条意见中，7 条 [AGREE]（含 1 条升级为 must-fix），1 条 [REBUT]（G(t)=∅ 边界情况）
- 新增采纳 R1-W1 为 must-fix（BoostCD baseline 缺失）
- 维持 Overall 3.0（Findings），R1 给 3.5 的分歧主要在 CF 透明度权重和 κ̄ severity 判定上
- Excitement 维持 2.5，承认 taxonomy 有 marginal 迁移价值但 confirmatory formalization 的 surprise 不足

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

_source line 1359 · 2026-05-20T18:55:22.314072+00:00_

审稿报告已投递。

**Round 13 审稿完成**。

**Overall: 3.0（Findings）**，R1=3.5 / R2=3.0。

核心发现：
- **4 项全员共识 Must-Fix**：正文超页、CF 代价被低估、缺 BoostCD 对比、WikiEvents 统计效力
- **1 项有争议 Must-Fix**：κ̄ 贡献定位（R2=critical, R1=should-fix）
- **6 项 Should-Fix**：model scope 声称、DocRED DR 讨论、beam search claim、"formally compiles"、GoLLIE 参照、pumping lemma gap
- **修订路径明确**：补 BoostCD 对比 + 修正 CF 叙述 + 降级 κ̄ + 限定 claims + 压缩页数 → 有望 3.5

Issue Tracker 已同步更新（R12 resolved 6 项，R13 新增/升级 17 项）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 100

## Round 100

70 recorded events


### User

_source line 1360 · 2026-05-20T19:43:03.307821+00:00_

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

_source line 1361 · 2026-05-20T19:43:10.900306+00:00_

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

_source line 1362 · 2026-05-20T19:43:10.901009+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-20T19:43:15.569653+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-20T19:43:15.570149+00:00_



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

_source line 1365 · 2026-05-20T19:43:23.753840+00:00_

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

_source line 1366 · 2026-05-20T19:43:25.209977+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (124 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- d066_sweep_llama_docred_beam4_s1（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_sweep_llama_scierc_beam4_s1_551** (success): d066 SciERC beam sweep: Llama beam4 constrained (full_s1) on 551-sentence test set. Beam width k=4 with schema constraints should eliminate all four violation types (ET/RV/DR/CF=0) while maintaining R-F1 within ±1pp of unconstrained.\n- **d066_sweep_llama_docred_beam4_unc** (success): d066 DocRED beam sweep sub-task: Llama beam4 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure. ← 基于 d066_beam_sweep\n- **d066_sweep_llama_docred_beam1_s1** (success): d066 DocRED beam sweep sub-task: Llama beam1 (greedy) constrained (full_s1) 
…[truncated 1052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 1367 · 2026-05-20T19:43:25.210358+00:00_

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

_source line 1368 · 2026-05-20T19:43:25.260948+00:00_

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
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation inde
…[truncated 5636 chars]

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

_source line 1369 · 2026-05-20T19:43:33.746026+00:00_

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

_source line 1370 · 2026-05-20T19:43:33.797875+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1371 · 2026-05-20T19:43:36.426443+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-20T19:43:37.380856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit formatting"
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
    "query": "ACL Rolling Review 2026 author guidelines page limit formatting"
  }
}
```

</details>

---


### Tool call

_source line 1373 · 2026-05-20T19:43:38.034900+00:00_

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

_source line 1374 · 2026-05-20T19:43:38.035384+00:00_



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


### Tool result

_source line 1375 · 2026-05-20T19:43:43.759262+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit formatting"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's what I found about the ACL Rolling Review 2026 author guidelines regarding page limits and formatting:

## Page Limits

The "Limitations" section (along with, optionally, a section for ethical considerations) may be up to one page and will not count toward the final page limit.

## Formatting Guidelines

The paper follows ACL formatting. ACLPUB formatting guidelines were updated in January 2025 with clarifications on font size in figures and tables, placement of limitations and ethical considerations sections, and two-column formatting of appendices.

There is an official Overleaf template. Note that this template has a [review] setting that must be on for the submission.

## Limitations Sectio
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6378
}
```

</details>

---


### Tool result

_source line 1376 · 2026-05-20T19:43:47.274554+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

I found comprehensive information about EMNLP 2026's call for papers and ARR submission guidelines. Here's what I found:

## EMNLP 2026 Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of 
…[truncated 2067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 10848
}
```

</details>

---


### Tool call

_source line 1377 · 2026-05-20T19:43:54.382859+00:00_

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

_source line 1378 · 2026-05-20T19:43:55.394846+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars guaranteeing JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} near-eliminates DR (94--100\% reduction) with negligible R-F1 impact ($\pm$0.6\,pp), with cross-field (CF) rates of 0--9.9\% (zero-shot) to $\leq$1.2\% (fine-tuned); \S\ref{sec:scierc-results} analyzes conditions.
7	CF is substantially reduced by beam search under favorable conditions (low $\bar{\kappa}$ or fine-tuned settings).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across four autoregressive LMs (7--70B) with logits access and three tokenizer families.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1011
}
```

</details>

---


### Tool call

_source line 1379 · 2026-05-20T19:43:55.445438+00:00_

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

_source line 1380 · 2026-05-20T19:43:55.897745+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption; reliable type-constraint enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime
…[truncated 2742 chars]

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

_source line 1381 · 2026-05-20T19:43:55.948374+00:00_

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

_source line 1382 · 2026-05-20T19:43:56.902801+00:00_

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
17	OntoCoDec guarantees levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
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
31	An output contains $n$ entities with independently chosen types ($a_i \in 
…[truncated 6952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1383 · 2026-05-20T19:43:56.903203+00:00_

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

_source line 1384 · 2026-05-20T19:43:57.857125+00:00_

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
…[truncated 5582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1385 · 2026-05-20T19:43:57.857515+00:00_

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

_source line 1386 · 2026-05-20T19:43:58.110272+00:00_

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
…[truncated 1930 chars]

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

_source line 1387 · 2026-05-20T19:43:58.110738+00:00_

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

_source line 1388 · 2026-05-20T19:43:58.161366+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Memory — schema_semantic_constrained_ie\\n\\n> 非 metrics 性质的决策原因、约束、经验教训。Metrics 查 registry。\\n\\n## westd-21461 环境指南\\n- 系统 python3 (`/usr/bin/python3` 3.10) **无 ML 库**\\n- conda python3 (`/root/miniconda3/bin/python3` 3.12) 有完整环境：torch 2.8.0+cu128, transformers 5.8.1, peft 0.19.1, trl 1.4.0\\n- `python` 命令不存在，必须用 `python3` 或绝对路径\\n- **必须** `source /root/miniconda3/bin/activate` 激活 conda 后再执行\\n- **无外网**：必须设置 `TRANSFORMERS_OFFLINE=1` + `HF_HUB_OFFLINE=1`\\n- transformers 5.8.1 忽略 `WANDB_DISABLED=true`，必须在 TrainingArguments 中设 `report_to=\\\"none\\\"`\\n- submit_training_job 用 tmux（sh），bash builtins 必须用 `bash -c \\\"...\\\"` 或自包含 bash 脚本\\n\\n## westd-16980 环境指南\\n- conda python3 (`/root/miniconda3/bin/python3` 3.12), torch 2.10.0+cu128\\n- peft 0.19.1 有 AWQ dispatcher bug：`is_gptqmodel_available()` 在 optimum 版本低时 raise 而非 return False\\n- **必须 monkey-patch**：`import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False`\\n- 根分区磁盘小，checkpoint 必须写到 `/root/autodl-tmp/` 数据卷\\n\\n## 磁盘空间教训\\n- westd-21461 根分区只有 ~11G，merge 16G 模型会写满。所有 checkpoint 输出路径用 `/root/autodl-tmp/`\\n- westd-16980 同理，数据卷 `/root/autodl-tmp/` 有 109GB+\\n- westd-21461 全量 FT checkpoint (~16GB) 保存时可能磁盘满，需确保 `/root/autodl-tmp/` 有足够空间 + `save_total_limit=1`\\n\\n## P1 EE FT 失败根因汇总（r1-r4）\\n1. **r1**: `python: command not found`（tmux 用 sh，PATH 无 conda）\\n2. **r2**: HF Hub Errno 101 网络不可达 + `| tee` 掩盖退出码 + 虚假 COMPLETE 标记\\n3. **r3**: wandb 未安装但 transformers 尝试加载 WandbCallback\\n4. **r4**: 训练成功但 parse rate 极低（10-25%）——根因是 schema mismatch bug\\n- **教训**: 长 one-liner 在 tmux 里极脆弱，必须写自包含 bash 脚本 + `set -eo pipefail`\\n\\n## D060 Schema Mismatch Bug（关键教训）\\n- **根因**: `compiler/ontology_compiler.py:294` 的 `compile_event_json_schema()` 生成 `required: [\\\"entities\\\", \\\"events\\\"]`，但 FT 训练数据只有 `{\\\"events\\\": [...]}`\\n- **
…[truncated 1523 chars]

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

_source line 1389 · 2026-05-20T19:44:04.804570+00:00_

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

_source line 1390 · 2026-05-20T19:44:05.658480+00:00_

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
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1391 · 2026-05-20T19:44:05.809560+00:00_

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

_source line 1392 · 2026-05-20T19:44:06.161589+00:00_

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
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}); for symmetric relations, $|\sigma(r)|$ counts ordered pairs and the $|\mathcal{E}|^2$ normalization remains appropriate since we evaluate on directed triples:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	The mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness; tighter constraints force more frequent fallback a
…[truncated 1989 chars]

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

_source line 1393 · 2026-05-20T19:44:06.162023+00:00_

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

_source line 1394 · 2026-05-20T19:44:07.116052+00:00_

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
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1395 · 2026-05-20T19:44:07.116444+00:00_

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

_source line 1396 · 2026-05-20T19:44:07.568640+00:00_

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
…[truncated 2297 chars]

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

_source line 1397 · 2026-05-20T19:44:07.569159+00:00_

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

_source line 1398 · 2026-05-20T19:44:08.071630+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	Beam search ($k{=}4$) explores paths satisfying both layers jointly.
11	With LoRA, beam S1 eliminates all four violation types on SciERC for both models (R-F1 44--47); under zero-shot, beam reduces DR to 0\% and CF substantially (9.90\%\,$\to$\,0.53\% Qwen on SciERC; Appendix~\ref{app:beam-search}).
12	DocRED zero-shot beam evaluates on a 50-document subset (compute cost; LoRA beam uses the full 998-document set).
13	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
14	
15	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
16	\paragraph{Preliminary 70B evaluation.}
17	\label{sec:70b-results}
18	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on both SciERC (R-F1 $-$0.03\,pp) and DocRED (R-F1 $+$0.04\,pp), one of three configurations to eliminate DR on DocRED.
19	CF rises to 7.01\% (from 0.07\%), partly because constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
20	Scale reduces but does not eliminate violations.
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1399 · 2026-05-20T19:44:08.122263+00:00_

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

_source line 1400 · 2026-05-20T19:44:08.172950+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} guarantee format validity via CFG-based token masking; GCD~\cite{geng2023gcd} applies this to IE.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but these type environments are fully known at compile time; IE differs in that the entity registry accumulates dynamically and the schema may not cover all valid outputs (\S\ref{sec:composition}).
9	
10	\paragraph{Schema-aware IE.}
11	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, and GenIE~\cite{josifoski2022genie} encode ontology structure as typed code or trie-based decoding; REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, LasUIE~\cite{fei2022lasuie}, and others~\cite{wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} unify extraction via structured training, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
12	
13	\paragraph{Constraint enforcement in IE.}
14	\citet{roth_yih_2004} first formulated hard type constraints via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation.
15	EnriCo~\cite{zaratiana2024enrico} and IterGen~\cite{ugare2025itergen} enforce constraints via ASP or backtracking; DCCD~\cite{dccd2026} explores draft-conditioned approaches.
16	BoostCD~\cite{boostcd2025} targets closed IE (Wikidata entity IDs via KB membership constraints on FlanT5-base), differing from OntoCoDec in task definition (KB lookup vs.\ span extraction), constraint granularity (membership v
…[truncated 597 chars]

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

_source line 1401 · 2026-05-20T19:44:17.714447+00:00_

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

_source line 1402 · 2026-05-20T19:44:18.719272+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints via a decidability-guided two-layer architecture.
4	LoRA + greedy S1 achieves DR\,$\leq$\,0.09\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC under favorable conditions (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	Beam search ($k{\geq}4$) substantially reduces CF under low-$\bar{\kappa}$ or fine-tuned conditions; $\bar{\kappa}$ provides a descriptive diagnostic for deployment guidance, though validation on additional schemas is needed.
6	Evaluation covers primarily 7--8B models with preliminary 70B results.
7	

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

_source line 1403 · 2026-05-20T19:44:18.719738+00:00_

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

_source line 1404 · 2026-05-20T19:44:19.724249+00:00_

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
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1405 · 2026-05-20T19:44:20.176633+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1406 · 2026-05-20T19:44:21.083915+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1407 · 2026-05-20T19:44:21.084371+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1408 · 2026-05-20T19:44:21.135385+00:00_

# Review Issues Tracker — schema_semantic_constrained_ie
# Updated: Round 13 Action Matrix dispatched (D076), 2026-05-20

# ============================================================
# Round 13 Must-Fix (Full Consensus)
# ============================================================

- id: "R13-MF1"
  summary: "正文超 8 页限制（§7 约 11 行溢出至第 9 页）"
  category: format
  severity: critical
  status: in_progress
  first_raised_round: 13
  last_seen_round: 13
  mentions:
    - round: 13
      reviewers: [1, 2]
      note: "R2-W1 raised as critical, R1 初审列为 minor 后升级为 must-fix。Visual Check 同时发现。Section 7 结论溢出至 p9 约 11 行。EMNLP 2026 严格限制 8 页正文。"
  action_items:
    - round: 13
      action: "压缩 §7 Discussion and Conclusion / §6 Related Work / §5 实验叙述，确保正文在第 8 页底部结束"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R13-MF2"
  summary: "CF 代价在 Abstract/Introduction 中被系统性低估（'modest' 描述 9.90%–21% CF 是误导）"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 12
  last_seen_round: 13
  mentions:
    - round: 12
      reviewers: [1, 2]
      note: "R12-SF4: CF 代价在 Abstract/Contribution 中不够透明"
    - round: 13
      reviewers: [1, 2]
      note: "R2-W2 raised as critical, R1 AGREE 并升级。Abstract 'modest CF costs' 用于描述 SciERC 9.90%、WikiEvents 15–21% 有误导性。Introduction 完全未提 CF。"
  action_items:
    - round: 13
      action: "Abstract 替换为具体 CF 范围（0–9.9% ZS / ≤1.2% FT）；Intro 新增 DR↔CF trade-off 段落；删除全文 'modest' 修饰 CF"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R13-MF3"
  summary: "缺少最直接可比的 IE constrained decoding baseline（BoostCD、IterGen）的量化对比"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 12
  last_seen_round: 13
  mentions:
    - round: 12
      reviewers: [1, 2]
      note: "R12-SF2: 无直接实验对比 BoostCD（should-fix）"
    - round: 13
      reviewers: [1, 2]
      note: "R1-W1 raised as critical, R2 AGREE 并采
…[truncated 14353 chars]

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

_source line 1409 · 2026-05-20T19:44:50.675842+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -80",
  "description": "Read full project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -80",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 1410 · 2026-05-20T19:44:51.580114+00:00_

(Bash completed with no output)

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

_source line 1411 · 2026-05-20T19:44:51.831449+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null || echo \"NO_PDF\"",
  "description": "Check if PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null || echo \"NO_PDF\"",
    "description": "Check if PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1412 · 2026-05-20T19:44:51.882296+00:00_

-rw-r--r-- 1 ubuntu ubuntu 532361 May 20 19:33 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf

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

_source line 1413 · 2026-05-20T19:44:54.644258+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null",
  "description": "Read full project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 1414 · 2026-05-20T19:44:54.695895+00:00_

Exit code 1

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

_source line 1415 · 2026-05-20T19:45:00.992181+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema_semantic_constrained_ie/config*",
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
    "pattern": "**/schema_semantic_constrained_ie/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 1416 · 2026-05-20T19:45:01.093027+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-20T19:45:03.705416+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema_semantic_constrained_ie/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects"
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
    "pattern": "**/schema_semantic_constrained_ie/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-20T19:45:03.806446+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml

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

_source line 1419 · 2026-05-20T19:45:09.909993+00:00_

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

_source line 1420 · 2026-05-20T19:45:10.263012+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (124 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- d066_sweep_llama_docred_beam4_s1（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **d066_sweep_llama_scierc_beam4_s1_551** (success): d066 SciERC beam sweep: Llama beam4 constrained (full_s1) on 551-sentence test set. Beam width k=4 with schema constraints should eliminate all four violation types (ET/RV/DR/CF=0) while maintaining R-F1 within ±1pp of unconstrained.\n- **d066_sweep_llama_docred_beam4_unc** (success): d066 DocRED beam sweep sub-task: Llama beam4 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure. ← 基于 d066_beam_sweep\n- **d066_sweep_llama_docred_beam1_s1** (success): d066 DocRED beam sweep sub-task: Llama beam1 (greedy) constrained (full_s1) 
…[truncated 1052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-20T19:45:16.039140+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-20T19:45:16.492051+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1423 · 2026-05-20T19:45:42.832641+00:00_

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

_source line 1424 · 2026-05-20T19:46:06.267880+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23435
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-20T19:46:06.368759+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计与评估**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求（已从 CFP 实时确认）\n- 正文严格 **8 页**限制，参考文献不限页数\n- Limitations 和 Ethics 章节不计入页数（不含过多额外内容）\n- ACL 模板，`[review]` 选项\n- Double-blind 审稿\n- 必须有 Limitations section\n- ARR Responsible NLP Research Checklist 必须提交\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Proposition 1 及其 proof sketch 的正确性和严谨度\n- 三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）分类是否准确\n- Grammar-first fallback 设计是否合理，\"best-effort pair-based enforcement\" 的保证边界\n- Entity registry 的正确性保证（顺序依赖、动态构建）\n- Continuation masking 的 tokenizer-agnostic 声称是否有充分支持\n- Constraint tightness κ̄ 作为描述性指标的合理性（仅 2 个数据点 SciERC/DocRED）\n\n### 2. 实验设计与评估\n- 五路消融设计（SciERC Table 1）和四路消融（DocRED Table 2）是否充分证明 enabling dependency\n- Fine-tuning composability 实验的统计显著性（bootstrap 10,000, paired）\n- Cross-model validation（3 models × 2 datasets）的设计合理性\n- WikiEvents EE 扩展的证据强度（20-doc test set 的局限性）\n- Beam search 评估的完整性（DocRED zero-shot 仅 50-doc 子集）\n- 70B 评估作为 \"preliminary\" 的定位是否充分\n- 缺少哪些关键 baseline（特别是 BoostCD、GCD、IterGen 等同领域 constrained decoding 方法）\n- 运行时开销评估的充分性\n- 统计检验方法是否恰当\n\n### 3. 格式检查\n- 正文是否在 8 页以内\n- 是否符合 double-blind 要求\n\n请按以下格式输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条，S1/S2/...）\n3. Weaknesses（逐条，W1/W2/...，标注严重度：[critical]/[major]/[minor]）\n4. Questions for Authors（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度 + 1-2 句总评）"
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
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计与评估**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求（已从 CFP 实时确认）\n- 正文严格 **8 页**限制，参考文献不限页数\n- Limitations 和 Ethics 章节不计入页数（不含过多额外内容）\n- ACL 模板，`[review]` 选项\n- Double-blind 审稿\n- 必须有 Limitations section\n- ARR Responsible NLP Research Checklist 必须提交\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Proposition 1 及其 proof sketch 的正确性和严谨度\n- 三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）分类是否准确\n- Grammar-first fallback 设计是否合理，\"best-effort pair-based enforcement\" 的保证边界\n- Entity registry 的正确性保证（顺序依赖、动态构建）\n- Continuation masking 的 tokenizer-agnostic 声称是否有充分支持\n- Constraint tightness κ̄ 作为描述性指标的合理性（仅 2 个数据点 SciERC/DocRED）\n\n### 2. 实验设计与评估\n- 五路消融设计（SciERC Table 1）和四路消融（DocRED Table 2）是否充分证明 enabling dependency\n- Fine-tuning composability 实验的统计显著性（bootstrap 10,000, paired）\n- Cross-model validation（3 models × 2 datasets）的设计合理性\n- WikiEvents EE 扩展的证据强度（20-doc test set 的局限性）\n- Beam search 评估的完整性（DocRED zero-shot 仅 50-doc 子集）\n- 70B 评估作为 \"preliminary\" 的定位是否充分\n- 缺少哪些关键 baseline（特别是 BoostCD、GCD、IterGen 等同领域 constrained decoding 方法）\n- 运行时开销评估的充分性\n- 统计检验方法是否恰当\n\n### 3. 格式检查\n- 正文是否在 8 页以内\n- 是否符合 double-blind 要求\n\n请按以下格式输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条，S1/S2/...）\n3. Weaknesses（逐条，W1/W2/...，标注严重度：[critical]/[major]/[minor]）\n4. Questions for Authors（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 1426 · 2026-05-20T19:46:22.311786+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15943
}
```

</details>

---


### Tool call

_source line 1427 · 2026-05-20T19:46:22.463605+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 论文完整性 + 写作质量 + Related Work**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求（已从 CFP 实时确认）\n- 正文严格 **8 页**限制，参考文献不限页数\n- Limitations 和 Ethics 章节不计入页数（不含过多额外内容）\n- ACL 模板，`[review]` 选项\n- Double-blind 审稿\n- 必须有 Limitations section\n- ARR Responsible NLP Research Checklist 必须提交\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 相对于 XGrammar、Outlines、SynCode 等 grammar-constrained decoding 工作的增量贡献\n- 相对于 GoLLIE、KnowCoder、GUIDEX 等 schema-aware IE 工作的定位\n- 相对于 BoostCD、GCD、IterGen、EnriCo 等 constraint enforcement 工作的区分度\n- Decidability taxonomy（三级分类）的理论迁移价值\n- \"Enabling dependency\" 概念的原创性和实用价值\n\n### 2. 论文完整性\n- Abstract 是否准确反映论文实际贡献（是否有 overclaiming）\n- Introduction 的 claims 是否都有实验支持\n- Contribution 列表是否恰当（数量、粒度、claim 强度）\n- Limitations section 是否全面、诚实\n- Ethics statement 是否充分\n- 论文叙事的完整性（是否有逻辑缺口）\n\n### 3. 写作质量\n- 论文结构和叙事流畅度\n- 术语一致性（S1/S2 命名、\"compile\"/\"interpret\" 措辞分层）\n- 表格和图表的清晰度、可读性\n- 数学符号的规范性\n- 是否有 AI 生成痕迹（过度使用 hedge words、不自然的措辞）\n\n### 4. Related Work\n- 覆盖面是否充分（grammar-constrained decoding、schema-aware IE、constraint enforcement、constrained decoding degradation）\n- 是否有遗漏的重要工作\n- 与竞品的定位是否清晰和公正\n- 引用是否真实、完整（注意 unverified/hallucinated citations）\n\n请按以下格式输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条，S1/S2/...）\n3. Weaknesses（逐条，W1/W2/...，标注严重度：[critical]/[major]/[minor]）\n4. Questions for Authors（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度 + 1-2 句总评）"
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
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 论文完整性 + 写作质量 + Related Work**。\n\n## 论文信息\n- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求（已从 CFP 实时确认）\n- 正文严格 **8 页**限制，参考文献不限页数\n- Limitations 和 Ethics 章节不计入页数（不含过多额外内容）\n- ACL 模板，`[review]` 选项\n- Double-blind 审稿\n- 必须有 Limitations section\n- ARR Responsible NLP Research Checklist 必须提交\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 相对于 XGrammar、Outlines、SynCode 等 grammar-constrained decoding 工作的增量贡献\n- 相对于 GoLLIE、KnowCoder、GUIDEX 等 schema-aware IE 工作的定位\n- 相对于 BoostCD、GCD、IterGen、EnriCo 等 constraint enforcement 工作的区分度\n- Decidability taxonomy（三级分类）的理论迁移价值\n- \"Enabling dependency\" 概念的原创性和实用价值\n\n### 2. 论文完整性\n- Abstract 是否准确反映论文实际贡献（是否有 overclaiming）\n- Introduction 的 claims 是否都有实验支持\n- Contribution 列表是否恰当（数量、粒度、claim 强度）\n- Limitations section 是否全面、诚实\n- Ethics statement 是否充分\n- 论文叙事的完整性（是否有逻辑缺口）\n\n### 3. 写作质量\n- 论文结构和叙事流畅度\n- 术语一致性（S1/S2 命名、\"compile\"/\"interpret\" 措辞分层）\n- 表格和图表的清晰度、可读性\n- 数学符号的规范性\n- 是否有 AI 生成痕迹（过度使用 hedge words、不自然的措辞）\n\n### 4. Related Work\n- 覆盖面是否充分（grammar-constrained decoding、schema-aware IE、constraint enforcement、constrained decoding degradation）\n- 是否有遗漏的重要工作\n- 与竞品的定位是否清晰和公正\n- 引用是否真实、完整（注意 unverified/hallucinated citations）\n\n请按以下格式输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条，S1/S2/...）\n3. Weaknesses（逐条，W1/W2/...，标注严重度：[critical]/[major]/[minor]）\n4. Questions for Authors（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 1428 · 2026-05-20T19:46:23.723875+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1260
}
```

</details>

---


### Assistant

_source line 1429 · 2026-05-20T19:46:35.585460+00:00_

Round 1 已启动：

- **视觉审查 Agent**: 已派发（fire-and-forget，与 Reviewer 并行）
- **Reviewer 1**（方法严谨性 + 实验评估）: 已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作 + Related Work）: 已分配

等待两位 Reviewer 返回独立初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1430 · 2026-05-20T19:52:28.421322+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：OntoCoDec

## 1. Summary

OntoCoDec proposes a two-layer constrained decoding framework for information extraction that compiles IE ontologies into token-level constraints: a grammar layer (context-free, via XGrammar) for JSON validity and vocabulary membership, and a semantic layer (prefix-decidable with state) for domain/range type constraints via a runtime entity registry. The paper introduces a three-level decidability taxonomy of IE type constraints and the concept of "enabling dependency" between layers. Evaluation on SciERC (551 docs), DocRED (998 docs), and WikiEvents (246 docs) with 7-8B models shows near-elimination of ontology violations with 1.54× latency overhead.

---

## 2. Strengths

**S1. 理论基础扎实：决策性分类体系 (decidability taxonomy) 提供了清晰的形式化框架。**
三级分类（context-free / prefix-decidable with state / non-local）为理解不同约束执行机制的能力边界提供了干净的理论基础。Proposition 1（Appendix O）通过 pumping lemma 证明了具有无界实体集的 domain/range 约束不是 context-free 的，这一证明正确且直接支撑了两层设计的必要性。

**S2. 消融实验极其充分。**
论文提供了全面的消融：层级贡献分析（Table 1-3）、S1 vs S2 配置对比、与 fine-tuning 的组合性（Section 5.1）、跨数据集验证（Section 5.2, Table 3）、beam search 兼容性（Appendix F）、文档长度分析（Appendix H）、prompt 敏感性分析（Appendix I）、以及 4 个 case study（Appendix J）。32 页附录虽大，但提供了实质性的深度，而非凑篇幅。

**S3. "Enabling dependency" 是一个有价值的概念贡献。**
Table 1 和 Section 5.1 清楚地展示了：grammar layer 单独只能减少 24% DR（无语义约束时），而 semantic layer 单独无法保证词汇合规性。这种层间相互依赖关系并不显而易见，具有实际指导意义——它说明了为什么单纯堆叠 XGrammar 或单纯做 type checking 都不够。

**S4. 工程设计干净、可复用。**
系统从任意 IE 本体（JSON Schema 编码）自动编译约束，无需约束专属训练。tokenizer-agnostic masking（Section 3.3）和 grammar-first fallback（Section 4）是合理的设计选择。适用于任何提供 logit 访问的自回归 LM——这是一个合理的部署假设。

**S5. violation 消除效果强。**
SciERC + LoRA fine-tuning 下实现零违规；DocRED 上 DR 从 15.37% 降至 0.03%（Table 2）。与 fine-tuning 的组合性（Section 5.1）得到充分验证，表明约束执行和参数优化是互补的。

---

## 3. Weaknesses

**W1 [major] 新颖性适中——架构本质上是已有技术的 well-motivated 组合。**
- Grammar layer 明确是 XGrammar（Dong et al., 2025）应用于 IE JSON schema——Section 3.2 直接写 "compiled into a pushdown automaton via XGrammar"。贡献在于 *应用*，而非机制本身。
- Semantic layer 是一个带状态的查找表（entity registry D: name→type），在 type-bearing positions 做 logit masking。decidability 分析解释了 *why* 需要它，但机制本身（维护 registry + 在特定位置限制类型）是直接的工程实现。
- Decidability taxonomy 将已知的形式语言理论结果（CFG 不能执行跨字段依赖）重述于 IE 语境。Proposition 1 的 pumping lemma 证明正确但标准。
- 主要新颖性在于 *组合* 和 *形式化*，而非单个组件。这是有效的贡献，但论文 framing（"a framework that translates IE ontologies into composable token-level decoding constraints via a decidability-guided architecture"）可能对概念新颖性有所高估。

**W2 [major] 评估范围相对于泛化性声明偏窄。**
- 仅 3 个数据集：SciERC（551 docs, 7 entity types）、DocRED（998 docs, 96 relation types）、WikiEvents（246 docs, 56 event types）。全部英语、常用 benchmark。
- Abstract 和 Section 1 的 Contribution 3 声称 "compiles constraints automatically from any IE ontology"，但实际仅测试了 3 个本体。无生物医学、工业级或大规模本体评估。
- WikiEvents 结果被论文自身描述为 "preliminary"（Section 5.4），仅 20 个文档的测试集。
- 所有模型均为 7B-8B。无 ≥13B 模型或商业 API 评估。Limitations 中承认了这一点，但泛化性声明仍显不足。

**W3 [major] 约束执行对下游任务性能（F1）的实际影响不够清晰。**
- SciERC 上，约束引入后 F1 基本不变或轻微提升（Table 1: R-F1 44→46 with beam search），增益小且可能在置信区间内。
- DocRED 上，LoRA + beam S1 的 R-F1 从 7.74 提升至 8.23（Table 3），但绝对 F1 仍然很低。
- 论文以 DR reduction 为主要指标，但读者会追问：如果违规在本体层面无效但很少影响下游 precision/recall，这些工程开销是否值得？constraint tightness 分析（Section 4, Appendix N）部分回应了这一问题（展示了 tight constraints 与 high DR 的相关性），但未完全弥合 "violation reduction → practical value" 的论证缺口。

**W4 [minor] Related Work（Section 6）压缩过度，关键定位论述被推至 Appendix B。**
- 正文 Related Work 仅约 0.6 页。三个主要线索（grammar-constrained decoding, schema-aware IE, constraint enforcement + degradation）各仅 1-2 句话配 citation 列表，无法实现有意义的定位。
- **TANL**（Paolini et al., 2021, ICLR 2021）——"Structured Prediction as Translation between Augmented Natural Languages"——未被引用。这是生成式结构化预测范式的基础性工作，直接催生了 OntoCoDec 所构建的 IE-as-generation 范式，属于值得注意的遗漏。
- Appendix B（pages 14-18）的扩展 Related Work 覆盖面广且详细，但将关键定位论述放在附录中削弱了正文叙事。

**W5 [minor] 部分术语和符号密度较高，可能影响可读性。**
- 论文在 Section 2-4 中引入了大量形式化：G(t), S(t), V, D（entity registry）, M_final, 三级 decidability taxonomy, "enabling dependency", "grammar-first fallback", "constraint tightness κ"——密度较高。
- Constraint tightness κ（Eq. 3）在 Section 4 引入并贯穿分析，但对非专家读者的直觉解释可以更清晰。
- 整体写作质量良好，无明显 AI 生成痕迹，术语使用一致（S1/S2 命名、compile/interpret 层次分明），结构流畅。

**W6 [minor] 两个孤立 bib 条目和轻微引用问题。**
- `chen2024agentre` 和 `fan2024fsn` 在 bibliography 中但从未被引用。
- `formattax2026`（"The Format Tax"）和 `regino2025kgcurator` 无法通过 OpenAlex 验证（前者可能太新，后者为 workshop paper）。这两篇并非幻觉引用——看起来是真实工作——但应确认。
- 其余 10 条 "mismatch" 均为作者名 LaTeX 编码差异（如 šakota vs sakota），属于良性问题。

---

## 4. Questions for Authors

**Q1.** Enabling dependency 通过 Table 1 的 layer-level 消融进行了展示，但能否提供更受控的消融？具体来说：(a) grammar layer 有词汇约束但 *无* domain/range 执行 vs. (b) semantic layer 有 domain/range 执行但 *无* grammar 保证的词汇合规性。这将超越 layer-level 消融，隔离每种约束类型的具体贡献。

**Q2.** OntoCoDec 在具有显著更多 entity/relation types 的本体（如 Wikidata 的数千种类型）上表现如何？Appendix K（Table 29）展示了编译时间可达 1,000 relations，但大规模推理时的运行时开销未报告。

**Q3.** 论文报告 full S1 constrained decoding 的 latency overhead 为 1.54×（Section 5, Appendix G）。这一开销如何随序列长度和 schema 复杂度缩放？开销是由 grammar compilation、semantic masking 还是两者共同主导？

**Q4.** WikiEvents（Section 5.4）中，full S1 结果显示极端的词汇违规（EV+RoV >85%, Table 5），entity F1=0。这表明 grammar-only layer 对 event extraction 严重不足。能否讨论为什么 EE 对 grammar-constrained 方法特别具有挑战性，是否需要额外的架构组件？

**Q5.** CF→DR trade-off（Section 5.1, Appendix C）显示消除 CF 会将违规重新路由至 DR。这是任何两层约束系统的固有限制，还是 OntoCoDec 设计的特定产物？

---

## 5. Missing References

1. **TANL**（Paolini et al., 2021, ICLR）: "Structured Prediction as Translation between Augmented Natural Languages" ——生成式结构化预测的基础性工作，直接催生了 OntoCoDec 所依赖的 IE-as-generation 范式。
2. 可考虑引用 **SLOT**（2025, EMNLP Industry）: "Structuring the Output of Large Language Models" ——与生产环境中的结构化输出执行相关。

---

## 6. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 技术方法正确，两层架构由 decidability 分析良好支撑。消融充分。但评估仅覆盖 3 个英语数据集和 7-8B 模型，相对泛化性声明不足。Proposition 1 正确但标准。 |
| **Excitement** | 3/5 | Decidability taxonomy 和 enabling dependency 是有价值的概念贡献，但架构本质是已有技术的组合（XGrammar + 查找表式 type masking）。不开辟根本性新方向，但提供了有用的形式化框架。 |
| **Reproducibility** | 4/5 | 实验设置描述详细（Appendix G: 硬件、超参数、随机种子）；prompt templates 完整给出（Appendix A, Table 6）；数据集公开可用。代码未提供但方法描述足以复现。 |
| **Overall Assessment** | **3.5 — Borderline Conference** | |
| **Confidence** | 4/5 | 对 constrained decoding 和 IE 文献较熟悉，仔细阅读了全文含附录。 |

### 一句话总评

OntoCoDec 提供了一个工程质量高、理论动机清晰的约束解码框架，但新颖性适中（主要是已有技术的 principled composition），评估范围（3 个英语数据集、仅 7-8B 模型）相对其泛化性声明偏窄，且约束执行对下游 F1 的实际增益有限。是一篇扎实的 Findings 水平工作，若能拓展评估覆盖面或从理论框架中导出更意外的洞察，可冲击 Conference。


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

_source line 1431 · 2026-05-20T19:52:35.598175+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1432 · 2026-05-20T19:52:46.466538+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：3.5 — Borderline Conference**

核心判断：
- **新颖性适中**：两层架构本质是 XGrammar + 查找表式 type masking 的 principled composition，decidability taxonomy 是有价值的形式化但非突破性贡献
- **评估范围偏窄**：仅 3 个英语数据集、7-8B 模型，相对 "any IE ontology" 的泛化性声明不足
- **F1 增益有限**：violation reduction 显著，但对下游任务性能的实际影响不清晰
- **主要优势**：消融极充分、enabling dependency 概念有价值、工程质量高、写作质量良好

关键遗漏引用：TANL（Paolini et al., 2021, ICLR）——生成式结构化预测的基础性工作。

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

_source line 1433 · 2026-05-20T19:53:02.178058+00:00_

收到 Reviewer 2 审稿报告。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 103

## Round 103

6 recorded events


### User

_source line 1434 · 2026-05-20T19:53:52.232851+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：OntoCoDec

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints  
**Venue**: EMNLP 2026 (ARR May 2026 cycle)  
**审查侧重**: 方法严谨性 + 实验设计与评估

---

## 1. Summary

本文提出 OntoCoDec，一个将 IE ontology 编译为两层 token-level 解码约束的框架：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇准入，semantic layer（prefix-decidable with state）通过动态 entity registry 实现 domain/range type 约束。核心理论贡献是 Proposition 1（证明带无界实体集的 domain/range 约束不是 context-free 的）及三级 decidability 分类。在 SciERC、DocRED 和 WikiEvents 上跨 3 个 7-8B 模型评估，展示 zero-shot DR 降至 0.09%（SciERC, LoRA + beam S1）且 F1 影响极小（R-F1 ≤ 0.03 pp）。

---

## 2. Strengths

**S1. 理论基础扎实且有原创性。** Proposition 1 的 pumping lemma 证明（Appendix O, pp. 31-32）正确地建立了 domain/range type constraint 超出 context-free 语言能力的结论，为两层架构提供了形式化动机。三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）是对 constrained decoding 领域的概念性贡献，清晰地界定了不同约束类别的计算复杂度。

**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融（Table 1）和 DocRED 四路消融（Table 2-3）有效证明了各层的独立贡献：grammar-only 仅减少 24% DR（Section 5.1），semantic layer 是消除 domain/range violations 的关键，fine-tuning 与约束可组合（DR ≤ 0.09% across all fine-tuned settings）。层间 enabling dependency 的论证是本文的一大亮点。

**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests（§5.1, §5.2）覆盖关键对比，p 值均有报告。fine-tuning composability 的显著性检验（p<0.001 for DR, p=0.06 for R-F1）展现了负责任的统计实践。

**S4. 跨模型一致性好。** 3 models（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 datasets 的交叉验证（Tables 1-4）显示约束效果在不同 tokenizer 家族间一致，支持了 tokenizer-agnostic 的声称。

**S5. 工程贡献实用。** 运行时开销低（S1: +13.1% SciERC, +2.43% DocRED），continuation masking 的 tokenizer-agnostic 设计（§4）和 grammar-first fallback（§4）都是实际可部署的设计选择。Appendix G 的完整复现细节（rank, lr, epochs, batch size, prompt templates）值得肯定。

**S6. 论文写作清晰，结构合理。** 正文 8 页内完成了理论动机→方法→实验→讨论的完整叙事，appendix 提供了充分的补充材料（32 页总计）。Figure 1 的架构概览信息密度高。

---

## 3. Weaknesses

**W1 [critical] 缺少与最相关 constrained decoding baselines 的实验对比。**

- 具体位置：Section 5 全部实验表格
- 问题：论文在 Related Work（Section 6, p.8; Appendix B, pp.14-18）中引用了 BoostCD（Sakota et al., 2025）、GCD（Geng et al., 2023）、IterGen（Ugare et al., 2025）、SynCode（Ugare et al., 2024）和 DOMINO（Beurer-Kellner et al., 2024），但实验中未与任何一个进行实验对比。特别是 **BoostCD 是唯一一个明确将 constrained decoding 应用于 IE 的工作**（论文自己在 p.8 引用 "BoostCD ... application to information extraction"），完全没有实验对比是不可接受的。GCD 作为 grammar-constrained decoding for structured NLP 的直接前驱，也应纳入 baseline。
- 为什么影响接收：Without head-to-head comparisons, the paper cannot substantiate its claim of being superior to existing constrained decoding approaches for IE. The current baselines (unconstrained vs. grammar-only vs. full system) only demonstrate internal ablation, not external competitive positioning.
- 建议：至少添加 BoostCD 和 GCD 在 SciERC/DocRED 上的对比实验。如果这些方法不直接适用于论文的 ontology 设定，需明确说明 why not 并提供 adaptation 的 best-effort 结果。

**W2 [critical] Grammar-first fallback 频率过高（36.6%），削弱了 type constraint enforcement 的核心声称。**

- 具体位置：Table 7 (p. 19), Section 4 "Grammar-First Fallback"
- 问题：在 SciERC 上，grammar-first fallback 在 36.64% 的 type-bearing positions 触发（Table 7）。这意味着超过三分之一的关键位置上，semantic layer 的 type constraints 被完全放弃，仅保留 grammar layer 的结构约束。论文称 fallback 的 CF 消除"只 re-routes violations to DR"（p. 19），但这实际上意味着系统在大量位置上退化为 grammar-only 模式——正是消融实验证明不足的配置（grammar-only 仅减少 24% DR）。
- 为什么影响接收：这严重影响了论文的核心 value proposition——"type-constrained information extraction"。如果 type constraints 在 36.6% 的关键位置不被执行，那么系统的实际保证比论文暗示的弱得多。Table 7 的消融（移除 fallback 后 DR+CF 从 5.39 pp 降至 3.99 pp）进一步表明 fallback 机制本身引入了额外的 type violations。
- 建议：(1) 在主文中更诚实地讨论 fallback 频率及其对 guarantee 边界的影响；(2) 分析 fallback 的 root causes（是 ontology 设计问题？tokenizer 冲突？还是 model 偏好与 constraint 的系统性矛盾？）；(3) 探索降低 fallback 频率的方法（如更细粒度的 constraint relaxation 而非完全 fallback）。

**W3 [major] WikiEvents 评估（20-doc test set）统计功效极低。**

- 具体位置：Section 5.4 (p. 7), Table 5
- 问题：WikiEvents 使用标准 194/20/20 split（Li et al., 2021），test set 仅 20 篇文档，涵盖 56 event types, 30 argument roles, 27 entity types。在如此小的测试集上，violation rate 和 F1 的变化受单个文档影响极大。论文自己承认"results are preliminary due to the 20-document test set"（p. 7），但仍基于此得出 event extraction 扩展性的结论（如 "Full S1 eliminates RoV"、"semantic layer enforces per-event type compatibility"）。
- 为什么影响接收：20 个文档不足以支撑对 56 event types 的约束效果评估——平均每个 event type 不到 0.4 个测试文档。置信区间宽到无法区分有意义的改进和噪声。
- 建议：(1) 报告 WikiEvents 所有指标的置信区间；(2) 考虑扩大评估（如使用完整 246 docs 的 zero-shot 设置）；(3) 或将 WikiEvents 定位为 "proof of concept" 而非实验证据，相应降低结论的强度。

**W4 [major] Proposition 1 证明中的 position-indexing 简化未被充分讨论。**

- 具体位置：Appendix O (pp. 31-32), 特别是 "Position indexing vs. name referencing" 段落
- 问题：Proposition 1 的完整证明（Appendix O）使用 position-based entity indexing（e_n at position δ），但 OntoCoDec 的实际 JSON 输出通过 name strings 引用实体。证明末尾的 "Position indexing vs. name referencing" 段落以非形式化方式论证了 transfer（"the core argument transfers: validating type consistency requires a name-type lookup..."），但这不构成严格证明。Name-based referencing 确实不比 position-based 容易（需要 random-access retrieval by key），但从简化版本到实际系统的 gap 需要更精确的处理。
- 为什么影响接收：作为论文的核心理论基础，Proposition 1 的严谨性直接影响整个两层架构的形式化动机。如果 transfer argument 不成立，两层分离的必要性未被充分证明。
- 建议：(1) 将 name-based variant 作为 Corollary 形式化证明，而非仅以 informal paragraph 处理；(2) 或明确标注 Proposition 1 的 scope 仅限 position-indexed variant，name-based 的推广作为 conjecture 或 informal argument。

**W5 [major] Constraint tightness κ̄ 的 predictive value 基于仅 2 个数据点。**

- 具体位置：Section 4 "Constraint Tightness" (p. 4-5), Appendix D "Dual-Factor Quantitative Analysis" (p. 20)
- 问题：κ̄ 仅在 SciERC（0.833）和 DocRED（0.812）上计算。Appendix D 的 dual-factor analysis 报告 Spearman ρ = -0.77 with n=6（3 models × 2 datasets），但 (1) n=6 的 rank correlation 统计功效极低；(2) 两个 κ̄ 值相差仅 0.021，无法建立有意义的 κ̄-DR 关系；(3) 论文声称 "residual DR is governed by the product of schema tightness and baseline violation rate"（p. 20），但这个 multiplicative model 基于 2 个 tightness 值拟合，自由度为零。
- 建议：(1) 在更多数据集上计算 κ̄（如 TACRED, ACE05, CoNLL04 等常用 RE benchmarks）以建立更可信的 κ̄-DR 关系；(2) 或将 κ̄ 明确定位为仅描述性指标而非 predictive metric，避免 overclaim。

**W6 [major] Beam search 评估不完整：DocRED 仅 50-doc 子集。**

- 具体位置：Appendix F (p. 24-25), Table 15
- 问题：DocRED zero-shot beam search 仅在 50-doc 子集上评估（Table 15），而非完整 998-doc dev set。论文解释了计算成本原因（"LoRA beam uses the full 998-document set"），但 zero-shot beam search 是论文的重要 contribution之一（beam search 是处理 Level 3 non-local constraints 的主要策略），在缩减集上评估削弱了结论。SciERC 倒是用了完整 551 docs。
- 建议：至少在完整 DocRED 上报告一个 model 的 beam search 结果，或提供计算成本的具体数字让读者评估 50-doc subset 的代表性。

**W7 [minor] 70B 评估过于 preliminary，贡献有限。**

- 具体位置：Section 5.4 最后一段 (p. 8), Appendix K
- 问题：Llama-3.1-70B（AWQ INT4）仅在 SciERC 和 DocRED 上各报告一个配置的结果（DR=0%, R-F1≤0.04 pp）。虽然 DR=0% 是强结果，但(1) 仅量化推理，未测试 70B+LoRA fine-tuning；(2) INT4 量化可能影响 baseline 质量；(3) 没有 beam search 或消融变体。
- 建议：要么充实 70B 评估（多个配置、消融），要么删除该部分以节省页面空间给更重要的实验（如添加 baselines）。

**W8 [minor] Entity registry 的顺序依赖假设缺少量化验证。**

- 具体位置：Section 3.3 "Entity registry" (p. 4)
- 问题：Semantic layer 假设实体在关系之前生成（"ensuring the relation type r_i is known before entity type fields"）。S2 two-pass pipeline 通过设计保证了这一点，但 S1 single-pass 依赖 LLM 的生成顺序。论文未报告 S1 下实体-关系生成顺序违反的频率。
- 建议：报告 S1 模式下有多少比例的 relation fields 在对应 entity 生成前被访问，以量化该假设的 robustness。

---

## 4. Questions for Authors

**Q1.** BoostCD（Sakota et al., 2025）是目前唯一将 constrained decoding 直接应用于 IE 的工作。能否解释为什么未将其作为 experimental baseline？如果是因为 BoostCD 不支持 ontology-level constraints，能否提供一个 fair adaptation 并报告结果？

**Q2.** Grammar-first fallback 在 SciERC 36.6% 的 type-bearing positions 触发。在 DocRED 上该比例是多少？fallback 的 root causes 分布如何（tokenizer collision vs. schema ambiguity vs. model preference）？

**Q3.** Proposition 1 的证明使用 position-based indexing。如果 output format 改为 entity mentions 使用固定 canonical forms（如 Wikidata QID）而非 free-text names，该证明是否仍然成立？这会影响 decidability taxonomy 吗？

**Q4.** Table 7 的 fallback ablation 显示移除 fallback 后 DR+CF 仅从 5.39 pp 降至 3.99 pp。这是否意味着一个更 aggressive 的 constraint enforcement 策略（不 fallback，而是 backtrack 或 resample）可以同时降低 DR 和 CF？

**Q5.** 论文提到 "constraint scope is model-dependent: for well-calibrated models ... S1 substantially reduces CF"（Limitations, p. 9）。能否量化 "well-calibrated" 的具体条件？是否有 metric 可以预测哪些 model-dataset 组合会从 OntoCoDec 获益最多？

**Q6.** WikiEvents 的 20-doc test set 上，LoRA + S1 的 F1 within ±1.1 pp 的置信区间是多少？能否报告 document-level variance？

---

## 5. Missing References

引用覆盖基本完整，以下可考虑补充：

- **SPIRES/OntologyGPT 类方法在 IE 上的 constrained decoding 对比**：虽然 SPIRES（Caufield et al., 2024）已被引用，但缺少与 ontology-based IE constraint 方法的直接实验对比。
- 2 篇 orphan bib entries（chen2024agentre, fan2024fsn）在 .bib 文件中存在但未在正文中引用，应清理。
- formattax2026（"The Format Tax", Lee et al., 2026）在 OpenAlex 上未找到——如果是非常新的 preprint，确认 arXiv ID 正确性。

---

## 6. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | Proposition 1 证明正确但简化假设的 transfer 不够 formal；grammar-first fallback 36.6% 触发率削弱 type enforcement 声称；消融设计严谨但缺少外部 baseline 对比 |
| **Excitement** | 3.5/5 | Ontology→两层 token-level constraint 编译是新颖且实用的 idea；decidability taxonomy 是概念性贡献；但执行层面的 gaps（missing baselines, limited evaluation scale）降低了 excitement |
| **Reproducibility** | 4/5 | Appendix G 提供完整超参数、prompt templates、软硬件配置；代码声明将发布；唯一顾虑是 continuation masking 的 tokenizer-specific 实现细节描述不够详细 |
| **Overall Assessment** | **3.5 — Borderline Conference** | |

### Reviewer Confidence
**4/5** — Quite sure. 我仔细阅读了全文（含 32 页 appendix），核查了 Proposition 1 的完整证明，验证了所有引用，并对 constrained decoding 和 IE 领域有充分的了解。

### 总评

OntoCoDec 提出了一个有理论深度和实践价值的框架：将 IE ontology 自动编译为两层 token-level 约束（grammar + semantic），通过 decidability analysis 指导架构设计。消融实验设计严谨，enabling dependency 论证令人信服，跨模型一致性好。

但论文有两个影响接收决定的关键问题：**(1) 缺少与 BoostCD/GCD 等最直接竞争方法的实验对比**，使得论文无法证明其相对于现有 constrained decoding 方法的优势；**(2) grammar-first fallback 在 36.6% 的 type-bearing positions 触发**，意味着系统的实际 type enforcement 保证显著弱于论文所暗示的。此外，WikiEvents 20-doc evaluation、50-doc beam search subset、以及 κ̄ metric 基于 2 个数据点等问题进一步削弱了实验证据的说服力。

如果作者能添加 BoostCD/GCD 对比实验，并更坦诚地讨论 fallback 频率对 guarantee 边界的影响，本文有望达到 Conference 水平（4.0）。当前版本推荐 **Borderline Conference (3.5)**。


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

_source line 1435 · 2026-05-20T19:54:46.050765+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告：OntoCoDec\n\n**审查侧重**: 方法严谨性 + 实验设计与评估\n\n## 2. Strengths\n\n**S1. 理论基础扎实且有原创性。** Proposition 1 的 pumping lemma 证明（Appendix O, pp. 31-32）正确地建立了 domain/range type constraint 超出 context-free 语言能力的结论，为两层架构提供了形式化动机。三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）是对 constrained decoding 领域的概念性贡献，清晰地界定了不同约束类别的计算复杂度。\n\n**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融（Table 1）和 DocRED 四路消融（Table 2-3）有效证明了各层的独立贡献：grammar-only 仅减少 24% DR（Section 5.1），semantic layer 是消除 domain/range violations 的关键，fine-tuning 与约束可组合（DR ≤ 0.09% across all fine-tuned settings）。层间 enabling dependency 的论证是本文的一大亮点。\n\n**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests（§5.1, §5.2）覆盖关键对比，p 值均有报告。fine-tuning composability 的显著性检验（p<0.001 for DR, p=0.06 for R-F1）展现了负责任的统计实践。\n\n**S4. 跨模型一致性好。** 3 models（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 datasets 的交叉验证（Tables 1-4）显示约束效果在不同 tokenizer 家族间一致，支持了 tokenizer-agnostic 的声称。\n\n**S5. 工程贡献实用。** 运行时开销低（S1: +13.1% SciERC, +2.43% DocRED），continuation masking 的 tokenizer-agnostic 设计（§4）和 grammar-first fallback（§4）都是实际可部署的设计选择。Appendix G 的完整复现细节值得肯定。\n\n**S6. 论文写作清晰，结构合理。** 正文 8 页内完成了理论动机→方法→实验→讨论的完整叙事，appendix 提供了充分的补充材料。Figure 1 的架构概览信息密度高。\n\n## 3. Weaknesses\n\n**W1 [critical] 缺少与最相关 constrained decoding baselines 的实验对比。**\n论文在 Related Work 中引用了 BoostCD、GCD、IterGen、SynCode 和 DOMINO，但实验中未与任何一个进行实验对比。特别是 BoostCD 是唯一一个明确将 constrained decoding 应用于 IE 的工作，完全没有实验对比是不可接受的。GCD 作为 grammar-constrained decoding for structured NLP 的直接前驱，也应纳入 baseline。\n\n**W2 [critical] Grammar-first fallback 频率过高（36.6%），削弱了 type constraint enforcement 的核心声称。**\n在 SciERC 上，grammar-first fallback 在 36.64% 的 type-bearing positions 触发（Table 7）。这意味着超过三分之一的关键位置上，semantic layer 的 type constraints 被完全放弃，仅保留 grammar layer 的结构约束。论文称 fallback 的 CF 消除\"只 re-routes violations to DR\"，但这实际上意味着系统在大量位置上退化为 grammar-only 模式。\n\n**W3 [major] WikiEvents 评估（20-doc test set）统计功效极低。**\n20 个文档不足以支撑对 56 event types 的约束效果评估——平均每个 event type 不到 0.4 个测试文档。\n\n**W4 [major] Proposition 1 证明中的 position-indexing 简化未被充分讨论。**\nProposition 1 的完整证明使用 position-based entity indexing，但 OntoCoDec 的实际 JSON 输出通过 name strings 引用实体。从简化版本到实际系统的 gap 需要更精确的处理。\n\n**W5 [major] Constraint tightness κ̄ 的 predictive value 基于仅 2 个数据点。**\nκ̄ 仅在 SciERC 和 DocRED 上计算。Appendix D 的 dual-factor analysis 报告 Spearman ρ = -0.77 with n=6，统计功效极低。\n\n**W6 [major] Beam search 评估不完整：DocRED 仅 50-doc 子集。**\nDocRED zero-shot beam search 仅在 50-doc 子集上评估，而非完整 998-doc dev set。\n\n**W7 [minor] 70B 评估过于 preliminary，贡献有限。**\n仅量化推理，未测试 70B+LoRA fine-tuning，INT4 量化可能影响 baseline 质量。\n\n**W8 [minor] Entity registry 的顺序依赖假设缺少量化验证。**\n论文未报告 S1 下实体-关系生成顺序违反的频率。\n\n## 4. Questions\n\nQ1. BoostCD 为何未作为 experimental baseline？\nQ2. Grammar-first fallback 在 DocRED 上的触发比例？fallback root causes 分布？\nQ3. 如果 output format 改为 canonical entity IDs，Proposition 1 是否仍然成立？\nQ4. 更 aggressive 的约束策略（backtrack/resample）能否同时降低 DR 和 CF？\nQ5. 能否量化 \"well-calibrated\" 的具体条件？\nQ6. WikiEvents 20-doc test set 上的 document-level variance？\n\n## 6. Overall Assessment\n- Soundness: 3.5/5\n- Excitement: 3.5/5\n- Reproducibility: 4/5\n- **Overall: 3.5 — Borderline Conference**\n- Confidence: 4/5"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告：OntoCoDec\n\n**审查侧重**: 方法严谨性 + 实验设计与评估\n\n## 2. Strengths\n\n**S1. 理论基础扎实且有原创性。** Proposition 1 的 pumping lemma 证明（Appendix O, pp. 31-32）正确地建立了 domain/range type constraint 超出 context-free 语言能力的结论，为两层架构提供了形式化动机。三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）是对 constrained decoding 领域的概念性贡献，清晰地界定了不同约束类别的计算复杂度。\n\n**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融（Table 1）和 DocRED 四路消融（Table 2-3）有效证明了各层的独立贡献：grammar-only 仅减少 24% DR（Section 5.1），semantic layer 是消除 domain/range violations 的关键，fine-tuning 与约束可组合（DR ≤ 0.09% across all fine-tuned settings）。层间 enabling dependency 的论证是本文的一大亮点。\n\n**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests（§5.1, §5.2）覆盖关键对比，p 值均有报告。fine-tuning composability 的显著性检验（p<0.001 for DR, p=0.06 for R-F1）展现了负责任的统计实践。\n\n**S4. 跨模型一致性好。** 3 models（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 datasets 的交叉验证（Tables 1-4）显示约束效果在不同 tokenizer 家族间一致，支持了 tokenizer-agnostic 的声称。\n\n**S5. 工程贡献实用。** 运行时开销低（S1: +13.1% SciERC, +2.43% DocRED），continuation masking 的 tokenizer-agnostic 设计（§4）和 grammar-first fallback（§4）都是实际可部署的设计选择。Appendix G 的完整复现细节值得肯定。\n\n**S6. 论文写作清晰，结构合理。** 正文 8 页内完成了理论动机→方法→实验→讨论的完整叙事，appendix 提供了充分的补充材料。Figure 1 的架构概览信息密度高。\n\n## 3. Weaknesses\n\n**W1 [critical] 缺少与最相关 constrained decoding baselines 的实验对比。**\n论文在 Related Work 中引用了 BoostCD、GCD、IterGen、SynCode 和 DOMINO，但实验中未与任何一个进行实验对比。特别是 BoostCD 是唯一一个明确将 constrained decoding 应用于 IE 的工作，完全没有实验对比是不可接受的。GCD 作为 grammar-constrained decoding for structured NLP 的直接前驱，也应纳入 baseline。\n\n**W2 [critical] Grammar-first fallback 频率过高（36.6%），削弱了 type constraint enforcement 的核心声称。**\n在 SciERC 上，grammar-first fallback 在 36.64% 的 type-bearing positions 触发（Table 7）。这意味着超过三分之一的关键位置上，semantic layer 的 type constraints 被完全放弃，仅保留 grammar layer 的结构约束。论文称 fallback 的 CF 消除\"只 re-routes violations to DR\"，但这实际上意味着系统在大量位置上退化为 grammar-only 模式。\n\n**W3 [major] WikiEvents 评估（20-doc test set）统计功效极低。**\n20 个文档不足以支撑对 56 event types 的约束效果评估——平均每个 event type 不到 0.4 个测试文档。\n\n**W4 [major] Proposition 1 证明中的 position-indexing 简化未被充分讨论。**\nProposition 1 的完整证明使用 position-based entity indexing，但 OntoCoDec 的实际 JSON 输出通过 name strings 引用实体。从简化版本到实际系统的 gap 需要更精确的处理。\n\n**W5 [major] Constraint tightness κ̄ 的 predictive value 基于仅 2 个数据点。**\nκ̄ 仅在 SciERC 和 DocRED 上计算。Appendix D 的 dual-factor analysis 报告 Spearman ρ = -0.77 with n=6，统计功效极低。\n\n**W6 [major] Beam search 评估不完整：DocRED 仅 50-doc 子集。**\nDocRED zero-shot beam search 仅在 50-doc 子集上评估，而非完整 998-doc dev set。\n\n**W7 [minor] 70B 评估过于 preliminary，贡献有限。**\n仅量化推理，未测试 70B+LoRA fine-tuning，INT4 量化可能影响 baseline 质量。\n\n**W8 [minor] Entity registry 的顺序依赖假设缺少量化验证。**\n论文未报告 S1 下实体-关系生成顺序违反的频率。\n\n## 4. Questions\n\nQ1. BoostCD 为何未作为 experimental baseline？\nQ2. Grammar-first fallback 在 DocRED 上的触发比例？fallback root causes 分布？\nQ3. 如果 output format 改为 canonical entity IDs，Proposition 1 是否仍然成立？\nQ4. 更 aggressive 的约束策略（backtrack/resample）能否同时降低 DR 和 CF？\nQ5. 能否量化 \"well-calibrated\" 的具体条件？\nQ6. WikiEvents 20-doc test set 上的 document-level variance？\n\n## 6. Overall Assessment\n- Soundness: 3.5/5\n- Excitement: 3.5/5\n- Reproducibility: 4/5\n- **Overall: 3.5 — Borderline Conference**\n- Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1436 · 2026-05-20T19:55:15.938652+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29887
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-20T19:55:16.190153+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：OntoCoDec\n\n**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + Related Work\n\n## 2. Strengths\n\n**S1. 理论基础扎实：decidability taxonomy 提供了清晰的形式化框架。**\n三级分类为理解不同约束执行机制的能力边界提供了干净的理论基础。Proposition 1 通过 pumping lemma 证明正确且直接支撑了两层设计的必要性。\n\n**S2. 消融实验极其充分。**\n全面消融：层级贡献分析、S1 vs S2 配置对比、与 fine-tuning 的组合性、跨数据集验证、beam search 兼容性、文档长度分析、prompt 敏感性分析、以及 4 个 case study。32 页附录提供了实质性的深度。\n\n**S3. \"Enabling dependency\" 是一个有价值的概念贡献。**\nTable 1 清楚地展示了层间相互依赖关系并不显而易见，具有实际指导意义。\n\n**S4. 工程设计干净、可复用。**\n系统从任意 IE 本体自动编译约束，无需约束专属训练。tokenizer-agnostic masking 和 grammar-first fallback 是合理的设计选择。\n\n**S5. violation 消除效果强。**\nSciERC + LoRA fine-tuning 下实现零违规。与 fine-tuning 的组合性得到充分验证。\n\n## 3. Weaknesses\n\n**W1 [major] 新颖性适中——架构本质上是已有技术的 well-motivated 组合。**\nGrammar layer 明确是 XGrammar 应用于 IE JSON schema。Semantic layer 是一个带状态的查找表。Decidability taxonomy 将已知的形式语言理论结果重述于 IE 语境。主要新颖性在于 *组合* 和 *形式化*，而非单个组件。\n\n**W2 [major] 评估范围相对于泛化性声明偏窄。**\n仅 3 个数据集（全部英语、常用 benchmark），所有模型均为 7B-8B。Abstract 和 Contribution 3 声称 \"compiles constraints automatically from any IE ontology\"，但实际仅测试了 3 个本体。\n\n**W3 [major] 约束执行对下游任务性能（F1）的实际影响不够清晰。**\nF1 基本不变或轻微提升，增益小且可能在置信区间内。\"violation reduction → practical value\" 的论证缺口。\n\n**W4 [minor] Related Work 压缩过度，关键定位论述被推至 Appendix B。**\n正文 Related Work 仅约 0.6 页。TANL（Paolini et al., 2021, ICLR）未被引用。\n\n**W5 [minor] 部分术语和符号密度较高，可能影响可读性。**\nSection 2-4 中形式化密度较高。\n\n**W6 [minor] 两个孤立 bib 条目和轻微引用问题。**\n`chen2024agentre` 和 `fan2024fsn` 在 bibliography 中但从未被引用。`formattax2026` 和 `regino2025kgcurator` 无法通过 OpenAlex 验证。\n\n## 4. Questions\n\nQ1. Enabling dependency 能否提供更受控的消融（grammar 有词汇约束但无 domain/range vs semantic 有 domain/range 但无 grammar 词汇保证）？\nQ2. OntoCoDec 在 Wikidata 等大规模本体上表现如何？\nQ3. Latency overhead 如何随序列长度和 schema 复杂度缩放？\nQ4. 为什么 EE 对 grammar-constrained 方法特别具有挑战性？\nQ5. CF→DR trade-off 是任何两层约束系统的固有限制还是 OntoCoDec 的特定产物？\n\n## 5. Missing References\n1. TANL（Paolini et al., 2021, ICLR）\n2. SLOT（2025, EMNLP Industry）\n\n## 6. Overall Assessment\n- Soundness: 3.5/5\n- Excitement: 3/5\n- Reproducibility: 4/5\n- **Overall: 3.5 — Borderline Conference**\n- Confidence: 4/5"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：OntoCoDec\n\n**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + Related Work\n\n## 2. Strengths\n\n**S1. 理论基础扎实：decidability taxonomy 提供了清晰的形式化框架。**\n三级分类为理解不同约束执行机制的能力边界提供了干净的理论基础。Proposition 1 通过 pumping lemma 证明正确且直接支撑了两层设计的必要性。\n\n**S2. 消融实验极其充分。**\n全面消融：层级贡献分析、S1 vs S2 配置对比、与 fine-tuning 的组合性、跨数据集验证、beam search 兼容性、文档长度分析、prompt 敏感性分析、以及 4 个 case study。32 页附录提供了实质性的深度。\n\n**S3. \"Enabling dependency\" 是一个有价值的概念贡献。**\nTable 1 清楚地展示了层间相互依赖关系并不显而易见，具有实际指导意义。\n\n**S4. 工程设计干净、可复用。**\n系统从任意 IE 本体自动编译约束，无需约束专属训练。tokenizer-agnostic masking 和 grammar-first fallback 是合理的设计选择。\n\n**S5. violation 消除效果强。**\nSciERC + LoRA fine-tuning 下实现零违规。与 fine-tuning 的组合性得到充分验证。\n\n## 3. Weaknesses\n\n**W1 [major] 新颖性适中——架构本质上是已有技术的 well-motivated 组合。**\nGrammar layer 明确是 XGrammar 应用于 IE JSON schema。Semantic layer 是一个带状态的查找表。Decidability taxonomy 将已知的形式语言理论结果重述于 IE 语境。主要新颖性在于 *组合* 和 *形式化*，而非单个组件。\n\n**W2 [major] 评估范围相对于泛化性声明偏窄。**\n仅 3 个数据集（全部英语、常用 benchmark），所有模型均为 7B-8B。Abstract 和 Contribution 3 声称 \"compiles constraints automatically from any IE ontology\"，但实际仅测试了 3 个本体。\n\n**W3 [major] 约束执行对下游任务性能（F1）的实际影响不够清晰。**\nF1 基本不变或轻微提升，增益小且可能在置信区间内。\"violation reduction → practical value\" 的论证缺口。\n\n**W4 [minor] Related Work 压缩过度，关键定位论述被推至 Appendix B。**\n正文 Related Work 仅约 0.6 页。TANL（Paolini et al., 2021, ICLR）未被引用。\n\n**W5 [minor] 部分术语和符号密度较高，可能影响可读性。**\nSection 2-4 中形式化密度较高。\n\n**W6 [minor] 两个孤立 bib 条目和轻微引用问题。**\n`chen2024agentre` 和 `fan2024fsn` 在 bibliography 中但从未被引用。`formattax2026` 和 `regino2025kgcurator` 无法通过 OpenAlex 验证。\n\n## 4. Questions\n\nQ1. Enabling dependency 能否提供更受控的消融（grammar 有词汇约束但无 domain/range vs semantic 有 domain/range 但无 grammar 词汇保证）？\nQ2. OntoCoDec 在 Wikidata 等大规模本体上表现如何？\nQ3. Latency overhead 如何随序列长度和 schema 复杂度缩放？\nQ4. 为什么 EE 对 grammar-constrained 方法特别具有挑战性？\nQ5. CF→DR trade-off 是任何两层约束系统的固有限制还是 OntoCoDec 的特定产物？\n\n## 5. Missing References\n1. TANL（Paolini et al., 2021, ICLR）\n2. SLOT（2025, EMNLP Industry）\n\n## 6. Overall Assessment\n- Soundness: 3.5/5\n- Excitement: 3/5\n- Reproducibility: 4/5\n- **Overall: 3.5 — Borderline Conference**\n- Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1438 · 2026-05-20T19:55:17.504326+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1314
}
```

</details>

---


### Assistant

_source line 1439 · 2026-05-20T19:55:26.490054+00:00_

Step 2 交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1440 · 2026-05-20T19:55:28.959738+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.5 — Borderline Conference**。

两个关键问题影响接收：
1. **缺少 BoostCD/GCD 等最直接竞争方法的实验对比** — 论文引用了这些工作但未做实验比较，无法证明相对优势
2. **Grammar-first fallback 触发率 36.6%** — 超过三分之一的 type-bearing positions 放弃了 semantic constraint，实际保证弱于论文暗示

其他 major issues 包括 WikiEvents 20-doc 测试集统计功效不足、Proposition 1 证明中 position-indexing 简化的 transfer argument 不够 formal、κ̄ metric 仅基于 2 个数据点。

优势方面：消融设计严谨（enabling dependency 论证清晰）、统计检验规范、跨模型一致性好、工程贡献实用、写作清晰。

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

_source line 1441 · 2026-05-20T19:55:33.167005+00:00_

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


## Round 105

## Round 105

2 recorded events


### User

_source line 1442 · 2026-05-20T19:57:12.149062+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

R2 的 S1-S5 与我的评估高度一致。特别是 S2（消融充分）和 S3（enabling dependency 的概念贡献）我在自己的审稿中也重点肯定了（我的 S2, S5）。

---

## Weaknesses 逐条回应

### R2-W1: 新颖性适中——架构本质上是已有技术的 well-motivated 组合

**[AGREE]**，但需限定范围。

R2 指出 grammar layer 是 XGrammar 的直接应用、semantic layer 是带状态查找表、decidability taxonomy 是形式语言理论的重述，这些观察是准确的。单独看每个组件确实缺乏 novelty。

但我认为 R2 略微低估了以下方面的贡献：
1. **Proposition 1（Appendix O, pp.31-32）不是简单重述**——它针对 IE 特有的 domain/range type constraint + unbounded entity set 场景给出了新的不可判定性证明。这个特定组合在 prior work 中没有被形式化过。
2. **Enabling dependency（Table 1）的实验发现**是非显然的：grammar-only 仅减 24% DR（Section 5.1），而 semantic-only（无 grammar 保证词汇有效性）也无法独立工作——这种双向依赖关系在之前的 constrained decoding 文献中未被识别。
3. **从任意 IE ontology 自动编译**的工程路径（ontology → XGrammar CFG + semantic transducer）在此前不存在。

总体而言，本文的 novelty 确实更多在于 **形式化动机 + 系统性组合 + 实验验证** 而非组件创新，但这对 systems paper 而言是可接受的。Excitement 3/5 的评价我认为合理——不是 breakthrough，但是 solid contribution。

---

### R2-W2: 评估范围相对于泛化性声明偏窄

**[AGREE]**，这与我自己的 W3（WikiEvents 20-doc）和 W7（70B preliminary）高度一致。

补充证据：
- Abstract 声称 "compiles constraints automatically from any IE ontology"，但实际仅测试了 3 个 ontology：SciERC（7 entity types, 7 relations）、DocRED（96 relation types, Wikidata 子集）、WikiEvents（56 event types, KAIROS ontology）。
- 所有数据集均为英语。
- 所有模型均为 7-8B 参数（70B 仅 "preliminary"，Section 5.4 最后一段）。
- Appendix K 的 scalability benchmark（up to 200 entity types, 1000 relations）仅测试编译时间，未测试 IE 性能。

我在自己的审稿中建议将 "any IE ontology" 的声称限定为 "tested IE ontologies"，并建议在更多数据集上验证 κ̄ metric（我的 W5）。R2 的这个 concern 是完全合理的。

---

### R2-W3: 约束执行对下游 F1 的实际影响不够清晰

**[REBUT]**，理由如下：

R2 的论点是 "F1 基本不变或轻微提升，violation reduction → practical value 的论证缺口"。我认为这个批评忽略了论文的核心 value proposition：

1. **Violation elimination IS the practical value for KG construction。** 在知识图谱构建场景中，ontologically invalid triples（如 head type 不匹配 relation 的 domain 约束）是无法入库的——它们不是 "slightly wrong"，而是完全无用。Table 1 显示 unconstrained Qwen3-8B 产生 15.4% DR 和 18.5% 违规率，这意味着约 1/6 的输出 triples 因 type violation 而不可用。消除这些 violations 的实际价值不需要通过 F1 提升来证明。

2. **F1 不变本身是一个重要发现。** 论文的 key claim 之一是 "constraints compose with fine-tuning without degrading performance"（Section 5.1, Table 1: R-F1 changes within ±0.03 pp across all fine-tuned settings）。这直接回应了 constrained decoding 的 "format tax" 顾虑（Tam et al., 2024; Schall and de Melo, 2025），证明 type enforcement 不引入 extraction quality trade-off。

3. **Post-hoc filtering 对比（Appendix C）进一步佐证了 practical value**：post-hoc filtering 虽然也能消除 violations，但 discards up to 48% of predictions（p. 5），而 OntoCoDec 通过 decoding-time 约束使模型直接生成 compliant output，保留了更多有效预测。

不过，我同意论文可以更明确地讨论 **下游应用场景中的实际收益量化**（如 KG completion 准确率、downstream QA 性能等）。目前的评估停留在 violation rate + F1 层面，缺少 end-to-end application evaluation。

---

### R2-W4: Related Work 压缩过度，关键定位推至 Appendix B

**[AGREE]**，但认为这是 8 页限制下的合理 trade-off。

正文 Related Work（Section 6, p.8）确实仅约 0.6 页，对于一篇涉及 constrained decoding、IE、ontology 三个领域交叉的论文来说偏短。关键定位论述（OntoCoDec vs. GoLLIE/KnowCoder/SynCode/PICARD 等的详细对比）被推至 Appendix B（pp.14-18, 约 4 页），这使得仅读正文的 reviewer 难以完整评估论文的定位。

但在 8 页严格限制下，将 4 页 related work 放入正文不现实。论文已在正文中覆盖了三条主线（grammar-constrained decoding / schema-aware IE / constraint enforcement in IE），并引导读者至 appendix。这是可以接受的处理方式。

**关于 TANL 缺失**：我同意 TANL（Paolini et al., 2021, ICLR）应被引用。TANL 是将 structured prediction 转化为 augmented language generation 的开创性工作，与 OntoCoDec 的 "IE as structured generation"（Section 3.1）直接相关。虽然 TANL 不涉及 constrained decoding，但它建立了 "用序列生成处理结构化预测" 的范式基础，OntoCoDec 正是在此范式上添加了 decoding-time constraints。

---

### R2-W5: 术语和符号密度较高

**[AGREE]**，但这是 minor issue。

Section 2-4 确实引入了大量符号：O = (E, R, σ), τ(·), P(·), M_total, G(t), S(t), V, κ̄ 等。对于非形式化背景的读者可能有一定门槛。但作为提出 decidability taxonomy 的 methods paper，这种形式化密度是合理且必要的。可以通过在 Section 2 添加一个 notation table 来改善可读性。

---

### R2-W6: 孤立 bib 条目和引用问题

**[AGREE]**，我在自己的审稿中也发现了同样的问题。

我的引用验证工具确认：
- `chen2024agentre` 和 `fan2024fsn` 是 orphan bib entries（在 .bib 中但未被 \cite）
- `formattax2026`（"The Format Tax"）在 OpenAlex 上未找到——可能是极新的 preprint
- `regino2025kgcurator` 在 OpenAlex 上未找到——可能是 workshop paper

这些是 minor 清理问题，不影响接收决定。

---

## Questions 回应

### R2-Q1: Enabling dependency 能否提供更受控的消融？

好问题。我认为现有消融已经比较充分，但 R2 建议的 "grammar-with-vocabulary-but-no-domain/range" vs. "semantic-with-domain/range-but-no-grammar-vocabulary" 消融确实能更精确地分离两层的贡献。目前 Table 1 的 S1 (grammar-only) 和 "Full S1" (grammar+semantic) 对比已经部分回答了这个问题——S1 alone 仅减 24% DR，加入 semantic 后几乎完全消除 DR。但缺少 "semantic-only without grammar" 的反向消融。Table 7（p.19）的 fallback ablation 部分涉及了这个方向。

### R2-Q2: 大规模本体（Wikidata）表现如何？

与我的 W5 一致的关切。Appendix K 的 scalability benchmark 显示编译时间随 entity type 数和 relation 数线性增长（up to 200 types, 1000 relations），但这只是 compilation overhead，未测试 IE 质量在大规模本体下如何变化。Section 4 "Constraint Tightness" 的分析暗示大规模本体的 κ̄ 可能更低（每个 relation 的 valid type pairs 更少），理论上应增强约束效果，但这纯属推测。

### R2-Q3: Latency 如何随序列长度和 schema 复杂度缩放？

Appendix G (p.27) 和 Table 29 (p.30) 提供了部分数据：SciERC（Small ontology, 7 types）+13.1% overhead，DocRED（96 relation types）+2.43%。Appendix H (pp.27-28) 的 document length analysis 显示约束效果在不同文档长度 bin 上一致。但论文确实缺少 **系统性的 scaling analysis**（如 overhead vs. ontology size 的曲线）。beam search 的 1.54× latency（Table 19, p.26）也只是一个数据点。

### R2-Q4: 为什么 EE 对 grammar-constrained 方法特别具挑战？

论文在 Section 5.4 (p.7) 和 Appendix C 中讨论了这个问题。关键原因是 EE ontology 中 event types 的 argument role constraints 更细粒度、更多样（56 event types × 30 argument roles × 27 entity types），且 "grammar-only has no applicable semantic-layer mechanism"（Table 5 caption）。此外，event extraction 的输出结构比 RE 更复杂（嵌套 events、多 argument slots）。

### R2-Q5: CF→DR trade-off 是固有限制还是 OntoCoDec 特有？

好的理论问题。我认为这是 **任何两层约束系统的固有限制**，而非 OntoCoDec 特有。当 structural constraints（grammar）和 semantic constraints（type consistency）冲突时，任何系统都必须选择优先级——OntoCoDec 选择 grammar-first fallback（保结构、牺牲 type），这将 CF 转化为 DR。替代策略（如 backtracking、IterGen 的 semantic-first approach）可能将这个 trade-off 反转（保 type、牺牲结构），但不会消除它。论文 Appendix D (p.19-20) 的 CF→DR trade-off 分析和 Figure 2 (p.20) 的 Residual DR vs. Schema Restrictiveness 散点图支持了这一解读。

---

## Missing References 回应

### TANL (Paolini et al., 2021)
**[AGREE]**，应被引用。TANL 建立了 augmented language modeling for structured prediction 的范式，是 "IE as structured generation" 的重要前驱。

### SLOT (2025, EMNLP Industry)
我不确定这篇具体指什么工作。如果 R2 能提供完整引用信息，可以评估其相关性。

---

## 总体评价对比

| | R1 (我) | R2 |
|---|---|---|
| Soundness | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 |
| Reproducibility | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 |
| Confidence | 4 | 4 |

R1 和 R2 在 Soundness、Reproducibility、Overall 上完全一致。主要分歧在 Excitement：我给 3.5 是因为认为 decidability taxonomy + enabling dependency 的组合具有超出 "well-motivated combination" 的概念贡献；R2 给 3.0 更侧重于组件级 novelty 的评估。这一分歧是合理的价值判断差异。

**最大共识**：缺少外部 baseline 对比（我的 W1, R2 未明确提但隐含在 W1 novelty 评估中）和评估范围偏窄（我的 W3/W7, R2 的 W2）是影响接收决定的核心问题。


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

_source line 1443 · 2026-05-20T19:57:20.833223+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 106

## Round 106

12 recorded events


### User

_source line 1444 · 2026-05-20T19:57:21.815271+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

## 逐条回应

### Weaknesses

**[AGREE] R1-W1 (缺少 BoostCD/GCD baseline):** 完全同意这是最大缺陷之一。BoostCD 是唯一明确将 constrained decoding 应用于 IE 的同期工作，在 SciERC/DocRED 上有公开结果，完全没有实验对比不可接受。GCD 作为直接前驱也应纳入。论文在 Section 5 中仅做间接引用（引用其他工作的数字），而非受控对比。

**[AGREE with nuance] R1-W2 (Fallback 36.6%):** 同意问题存在，但我判断 [major] 而非 [critical]。两个缓解因素：(1) 36.6% 是 zero-shot 下的数据，fine-tuning 后应降低（但论文未报告 fine-tuned fallback 率——这本身是缺失）；(2) 即使有此 fallback 率，整体 DR 仍显著下降（zero-shot ~1%, fine-tuned ≤0.09%）。但论文确实应在正文中更诚实地量化这一退化。

**[AGREE] R1-W3 (WikiEvents 20-doc):** 完全同意。我在自己的审稿中也指出了这一点（我的 W2）。20 docs / 56 event types 无法支撑可靠评估。

**[REBUT] R1-W4 (Proposition 1 position-indexing):** Appendix O 第 32 页底部 "Position indexing vs. name referencing" 段落已讨论了这一 gap。论文论述 name-based referencing 的约束严格性不弱于 position-based（name→type binding 同样创建跨位置依赖），position-based 是简化而非弱化。non-context-free 结论在 name-based 系统中仍然成立。但 R1 的 Q3（canonical IDs 下是否成立）是更尖锐的问题——有限实体集下约束退化为 regular language，Proposition 1 不成立。论文应更明确讨论这一边界。

**[AGREE] R1-W5 (κ̄ 统计功效):** n=6 做 Spearman 相关不严谨。建议将 κ̄ 仅作为定性分析工具，移除 Appendix D 中的推断统计数字。

**[AGREE] R1-W6 (DocRED beam search 50-doc):** 同意。Beam search 是宣称的关键配置，仅 50/998 docs 的覆盖不足。

**[AGREE] R1-W7 (70B preliminary):** 同意但确实仅为 minor。定位为 preliminary evidence 尚可接受。

**[AGREE] R1-W8 (顺序依赖量化):** 同意。应报告 S1 下 entity-before-relation ordering 的保持率。

### Questions

- Q1: 见 W1。AGREE。
- Q2: 有效。DocRED 的 fallback 数据确实缺失。
- Q3: 尖锐问题。有限实体集 + canonical IDs 下 Proposition 1 不成立。但论文假设 unbounded entity sets，对 open-domain IE 合理。应更明确讨论。
- Q4: 有价值建议。IterGen 式 backtracking 可能改善 DR-CF trade-off 但增加延迟。
- Q5: 合理。"Well-calibrated" 应被显式定义和量化。
- Q6: 同意。应报告 per-document variance。

## 总评

R1 审稿质量很高。8 条 Weakness 中我同意 7 条，仅对 W4 反驳（论文已有讨论），对 W2 同意但降低严重度至 major。两位 reviewer 核心判断一致：technically sound、well-executed 但 novelty 适中、evaluation scope 偏窄。R1 的 3.5 (Borderline Conference) 与我评分相同。R1 侧重方法/实验严谨性，我侧重新颖性/写作/Related Work，两份意见互补。


---

[Reviewer 1 审稿结果]:
审稿交叉回应已提交。

核心结论：R1 和 R2 在 Overall 3.5（Borderline Conference）上完全一致。主要共识点是 (1) 缺少 BoostCD/GCD 等外部 baseline 对比，(2) 评估范围偏窄。唯一分歧在 Excitement（3.5 vs 3.0），源于对 "形式化组合" vs "组件级创新" 的不同权重。对 R2-W3（F1 影响不清晰）我给出了反驳，认为 violation elimination 本身即是 KG 构建场景的实际价值。

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

_source line 1445 · 2026-05-20T19:57:51.018416+00:00_

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

_source line 1446 · 2026-05-20T19:57:51.270009+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T19:45:46.342029+00:00\", \"completed_at\": \"2026-05-20T19:49:49.737635+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前 2 页为纯文本，无任何 display item；Figure 1 直到第 3 页才出现。建议将 Figure 1 提前至第 2 页或增加 teaser figure 以加速审稿人锚定\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"正文 8 页仅 1 个 figure（其余 5 个均为 table），视觉上过于 table-heavy。建议增加 1 个结果可视化图（如 DR reduction 对比柱状图或雷达图），替代部分 table 或置于正文中，改善视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"整页纯文本（Related Work + Discussion/Conclusion），与前面 tables 密集区形成节奏断裂。Related Work 和 Conclusion 本身允许纯文本，但连续 text-only 在视觉上显得单调\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 内部分标注文字字号偏小（特别是 box 内子标签），打印时可能接近 8pt 可读下限，建议适当放大或简化标注\"}, {\"severity\": \"info\", \"dimension\": \"page 26\", \"message\": \"Figure 4（附录）双面板图的轴标签和图例字号偏小；置信带浅色填充在灰度打印下区分度有限，建议辅以不同 line style/marker\"}, {\"severity\": \"info\", \"dimension\": \"page 29\", \"message\": \"Table 25 使用纯红/绿色标注违规/修正，对色盲用户不友好。建议辅以删除线（违规）和加粗/下划线（修正）等非颜色视觉标记\"}, {\"severity\": \"info\", \"dimension\": \"page 14-18\", \"message\": \"Appendix B（Extended Related Work）连续 5 页纯文本无任何 display item，虽为附录但审稿人如需查阅会感到沉重\"}, {\"severity\": \"info\", \"dimension\": \"page 6-7\", \"message\": \"两页各含 2 个 table（共 4 个），信息密度高。每个 table 均传达独立 message（消融/跨数据集/跨模型/事件抽取），无冗余，但视觉上略显拥挤\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1447 · 2026-05-20T19:57:51.270389+00:00_

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

_source line 1448 · 2026-05-20T19:57:51.421270+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-20T19:58:32.892903+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
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
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-20T19:58:33.044224+00:00_



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
