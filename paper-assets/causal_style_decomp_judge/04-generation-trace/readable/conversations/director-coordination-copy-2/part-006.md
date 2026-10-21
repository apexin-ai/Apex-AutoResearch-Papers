# Director coordination — Part 6 of 7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/9d/9db2d5c10f518e51ec86.json)

## Round 126

### Tool call

_source line 1322 · 2026-05-23T06:53:02.846402+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool call

_source line 1323 · 2026-05-23T06:53:02.846792+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1324 · 2026-05-23T06:53:02.947659+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T06:41:21.599537+00:00\", \"completed_at\": \"2026-05-23T06:44:47.863052+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页纯文本（Related Work 全页 + Method 开头），无任何 display item 打破阅读节奏。建议：将 Figure 2（因果 DAG，当前在 p5）前移至 Method 开头（p4），或在 Related Work 中加入对比方法的小型 summary table\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（CSD pipeline overview）为单栏宽度，是论文第一个视觉锚点但尺寸偏小。pipeline 节点中的文字标签在打印时可能偏小（约正文字号 60-65%）。如有空间可考虑用 figure* 全宽展示\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（因果 DAG）使用红色实线与橙色虚线区分因果路径。灰度打印时红色/橙色路径区分度降低；建议辅以不同线型（实线 vs 点划线）增强可区分性\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 用 † 标记 Blindspot 显著性，但最优结果未加粗。审稿人习惯一眼看到粗体标注的最优值，建议对关键对比数值加粗\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 的 power 曲线有多条重叠线，图例文字偏小。建议增大图例字号或减少曲线条数（将次要配置移入 appendix）\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 部分跨越整页密集文本，无小节标题分割。虽然 EMNLP 2026 只要求简短覆盖 3 点左右，此处篇幅较长但内容充实，不影响评审\"}, {\"severity\": \"info\", \"dimension\": \"pages 11-17\", \"message\": \"Appendix 包含约 20 个 tables 但无 figure，全为数值表格。视觉上较单调，但作为补充材料可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"最后一页（references）内容约占 3/4 页面，底部有空白。参考文献页不适用末页填充率要求\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-23T06:53:02.948088+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-23T06:56:32.143144+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 fresh review: R2-W3 (Should-Fix) 指出 Thurstone 增量贡献未充分明确，GEE 分解被 undersold。R1 在 S1 中称研究问题'新颖'但 R2 交叉回应认为'过于宽容'。Intro 已添加 3 个 LLM-specific distinctions (per-axis structure, source decomposition, binary split) 但两位仍认为 GEE 应被提升为一级贡献。\"\n    action_items:\n      - round: 16\n        action: \"重构叙事结构：GEE decomposition 提升为一级贡献（与 Blindspot 并列），Abstract 中 GEE 占同等篇幅\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 13-15 issues (selected open/in_progress)\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 两位均指出 Table 1 信息密度过高。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: Table 1 脚注已有方向不对称信息，但 R1-Minor 和 R2-W7 再次指出信息密度过高，建议拆分为 LLMBar primary + cross-benchmark 两表。\"\n    action_items:\n      - round: 16\n        action: \"Table 1 拆分为 LLMBar primary (4 judges × 2 axes) + cross-benchmark replication 两表\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-R2 Must-Fix N3，R1 REBUT。分歧点。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及为独立 weakness。Related Work 中 RATE 段落组织有所改善，核心差异（measurement mode, GEE layer, NLI gating vs post-hoc correction）较清晰。\"\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W8 + R2-W6 再次独立提出，交叉全部 AGREE。论文已添加操作性定义（'an operational descriptor for the measurement-mode divergence'）和 Thurstone 讨论（3 LLM-specific distinctions），但 Title 仍为 'Likert Blindspot'——隐含 Likert 有缺陷。Construct divergence 讨论不充分（R2-W4）——attenuation 有完整 bootstrap 分析，construct divergence 仅一段话。两位共识：需要 title 中性化或在正文中给予 construct divergence 同等篇幅。\"\n    action_items:\n      - round: 16\n        action: \"(1) Title 考虑更中性命名或在 subtitle 中明确三种解释；(2) construct divergence 扩展为完整讨论段（含操作性定义和可检验预测）；(3) Discussion 增加 'Likert insensitivity as feature' 讨论\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W2 + R2-W2 双方再次独立 Must-Fix。交叉全部 AGREE。论文重构了证据层级（GEE cross-benchmark 为 primary，TOST 为 supplementary），但三条收敛证据每条单独看仍不足：(1) TOST Δ=15pp 边界过宽；(2) GEE Style OR=1.99 point estimate 非 trivial 虽 NS；(3) GPT-4o contrast 为 qualitative comparison。建议：明确报告 80% power 所需 n（≈200），考虑增加第二个 negative control judge 或 Bayesian equivalence testing。\"\n    action_items:\n      - round: 16\n        action: \"(1) 将 negative control 结论降级为 suggestive 而非 definitive；(2) 明确报告达 80% power 所需 n；(3) 讨论 GEE Style OR=1.99 point estimate 的含义\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽，n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W3 (Should-Fix) 再次提出，R2 交叉 AGREE。论文已添加 shrinkage 讨论（§5.2: 'consistent with small-sample upward bias'）和 CI 收缩比率验证（1.94× vs √(355/88)≈2.01）。但仅 Qwen3 formality 一个条件有 n=355 replication。其他条件（特别是 verbosity Style OR 8-13）可能同样存在 ~50% 膨胀（projected 4-6.5 仍 style-dominated）。建议：对 verbosity 轴也执行 scaled replication，或在正文中显著 caveat n=88 ORs 为 upper bound。\"\n    action_items:\n      - round: 16\n        action: \"(1) 对至少一个 verbosity 条件执行 n>200 scaled replication；(2) Table 2 增加 caveat 注释标明 n=88 ORs 可能高估\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R2-W1 (Must-Fix) 再次提出，R1 通过 Q3 间接触及。Abstract 已限定为 'surface-level style features' 但仍使用 'systematically divergent'。两个高度相关轴（FK d=0.50 cross-axis leakage）不足以声称 systematic。建议降级为 'consistent across tested axes' 或增加 1-2 个额外轴。\"\n    action_items:\n      - round: 16\n        action: \"Abstract/Conclusion 中 'systematic' 替换为 'consistent across tested axes' 或类似限定措辞\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W1 (Must-Fix) 重新独立提出并升级为最关键问题之一。R2 交叉 AGREE 并补充：如果 ~35% NLI-passed pairs 存在 content contamination，pairwise 的更高敏感度可能源于对 content 微妙差异的检测力而非 style sensitivity。建议：扩大至全部 88 pairs + 3+ 标注员 + content change taxonomy + sensitivity analysis。\"\n    action_items:\n      - round: 16\n        action: \"(1) 扩大人工验证至全部对（或至少 100 pairs 如等待中的标注批次）；(2) 对 human-flagged content-changed pairs 执行 sensitivity analysis；(3) 考虑更细粒度的 content change taxonomy\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W5 + R2-M5 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W6 (Should-Fix) 再次提出。R2 交叉 [REBUT]——认为 proof-of-concept 下单 judge 足够（Qwen3 是 Likert 效应最强的 judge，保守检验）。分歧点（R1 Should-Fix vs R2 降级），Director 判定为 Minor。\"\n    action_items:\n      - round: 16\n        action: \"Camera-ready 中增加至少一个额外 judge 的 100-point Likert 复制（非紧急）\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W5 (Should-Fix) 再次提出，R2 交叉 AGREE。论文已添加 length-controlled regression（Appendix R'）和 Sobel mediation test（59% 通过句子长度中介），但控制的是 word count 而非 readability 本身。建议：在 GEE 中加入 FK grade 作为协变量验证 formality Style OR 是否依然显著。\"\n    action_items:\n      - round: 16\n        action: \"GEE 中加入 FK grade 作为协变量，报告 controlling for readability 后 formality Style OR 变化\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W4 (Should-Fix) 再次提出，R2 交叉 AGREE 并补充：GPT-4o 与 target judge GPT-4o 存在完全重叠，且所有替代 rewriter 都是 instruction-tuned LLM——无法排除 instruction-tuned LLM 共性特征导致的 overlap。建议：测试 rule-based paraphrasing 或 human rewriting，或在 Limitations 中讨论 22% 作为 lower bound 的含义。\"\n    action_items:\n      - round: 16\n        action: \"Limitations 中明确讨论 22% OR 降幅是 lower bound，说明 instruction-tuned LLM 替代无法完全排除 shared style preference confound\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1-Minor-1 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R2-W7 (Minor) 再次提出。Table 1 仍为合并表，建议拆分。与 R13-SF1 合并处理。\"\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Appendix V 已添加完整的 rewriting prompts（formality, verbosity, register, same-style double-rewrite）\"\n    resolution_round: 16\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-Minor-2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [2]\n        note: \"R16: R2-W8 (Minor) 再次提出。论文仍交替使用 'style bias'（暗示方向性偏差）、'style sensitivity'（中性）、'style preference'（描述性），三术语含义不同。\"\n    action_items:\n      - round: 16\n        action: \"全文统一：'style sensitivity' 为默认中性术语，仅在讨论方向性偏好时使用 'style preference'，避免 'style bias'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 2 caption 已展开为 'Originality OR: original-preference odds ratio (OR > 1 favors original text)'\"\n    resolution_round: 16\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及，但应在 camera-ready 前检查。\"\n\n  # ============================================================\n  # Round 16 新发现\n  # ============================================================\n\n  - id: \"R16-W1\"\n    summary: \"Construct divergence 讨论不充分——与 Abstract 三机制并列承诺不匹配\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W4 (Should-Fix): Abstract 承诺三种非排他解释并列，但 attenuation 获完整 bootstrap 分析 + 功效曲线，construct divergence 仅 Section 5.1 末尾一段和 Limitations 简短提及。需操作性定义和可检验预测。与 R15-N1 (framing bias) 相关但独立——R15-N1 关注 title/framing，本条关注 construct divergence 的实质性讨论深度。\"\n    action_items:\n      - round: 16\n        action: \"扩展 construct divergence 讨论为完整段落：含操作性定义（absolute quality vs ordinal preference）、可检验预测（Likert 与 human quality ratings 对齐；pairwise 与 human rankings 对齐）、实践含义差异\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R16-W2\"\n    summary: \"Cross-benchmark 'severity spectrum' 解释为 post-hoc rationalization\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W5 (Should-Fix): Section 5.3 将不同 benchmark 上效果量差异解释为 'severity spectrum'，但无预先假设或理论预测。AlpacaEval 效应更强的归因（'targeting the strongest effects'）为循环论证。建议标记为 exploratory/post-hoc，或提供 benchmark 特性差异的定量分析。\"\n    action_items:\n      - round: 16\n        action: \"severity spectrum 解释明确标记为 post-hoc/exploratory，或补充 benchmark 特性差异（指令长度、领域分布等）的定量分析\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R16-W3\"\n    summary: \"BT 模型 unidimensionality 假设与论文核心论点（multi-dimensional evaluation）存在张力\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W7 (Minor) 提出，R2 交叉 AGREE。Limitations 已提及（'the BT model assumes unidimensionality'）但方法论章节缺乏预先讨论。GEE 引入正是为解决这一问题，但此张力应在 Section 3 中预先交代。\"\n    action_items:\n      - round: 16\n        action: \"Section 3.3 增加一句说明 BT 在此作为 summary statistic 使用，unidimensionality 限制由 GEE 分解层补充\"\n        assigned_to: paper_agent\n        status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 fresh review: R2-W3 (Should-Fix) 指出 Thurstone 增量贡献未充分明确，GEE 分解被 undersold。R1 在 S1 中称研究问题'新颖'但 R2 交叉回应认为'过于宽容'。Intro 已添加 3 个 LLM-specific distinctions (per-axis structure, source decomposition, binary split) 但两位仍认为 GEE 应被提升为一级贡献。\"\n    action_items:\n      - round: 16\n        action: \"重构叙事结构：GEE decomposition 提升为一级贡献（与 Blindspot 并列），Abstract 中 GEE 占同等篇幅\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 13-15 issues (selected open/in_progress)\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 两位均指出 Table 1 信息密度过高。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: Table 1 脚注已有方向不对称信息，但 R1-Minor 和 R2-W7 再次指出信息密度过高，建议拆分为 LLMBar primary + cross-benchmark 两表。\"\n    action_items:\n      - round: 16\n        action: \"Table 1 拆分为 LLMBar primary (4 judges × 2 axes) + cross-benchmark replication 两表\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-R2 Must-Fix N3，R1 REBUT。分歧点。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及为独立 weakness。Related Work 中 RATE 段落组织有所改善，核心差异（measurement mode, GEE layer, NLI gating vs post-hoc correction）较清晰。\"\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W8 + R2-W6 再次独立提出，交叉全部 AGREE。论文已添加操作性定义（'an operational descriptor for the measurement-mode divergence'）和 Thurstone 讨论（3 LLM-specific distinctions），但 Title 仍为 'Likert Blindspot'——隐含 Likert 有缺陷。Construct divergence 讨论不充分（R2-W4）——attenuation 有完整 bootstrap 分析，construct divergence 仅一段话。两位共识：需要 title 中性化或在正文中给予 construct divergence 同等篇幅。\"\n    action_items:\n      - round: 16\n        action: \"(1) Title 考虑更中性命名或在 subtitle 中明确三种解释；(2) construct divergence 扩展为完整讨论段（含操作性定义和可检验预测）；(3) Discussion 增加 'Likert insensitivity as feature' 讨论\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W2 + R2-W2 双方再次独立 Must-Fix。交叉全部 AGREE。论文重构了证据层级（GEE cross-benchmark 为 primary，TOST 为 supplementary），但三条收敛证据每条单独看仍不足：(1) TOST Δ=15pp 边界过宽；(2) GEE Style OR=1.99 point estimate 非 trivial 虽 NS；(3) GPT-4o contrast 为 qualitative comparison。建议：明确报告 80% power 所需 n（≈200），考虑增加第二个 negative control judge 或 Bayesian equivalence testing。\"\n    action_items:\n      - round: 16\n        action: \"(1) 将 negative control 结论降级为 suggestive 而非 definitive；(2) 明确报告达 80% power 所需 n；(3) 讨论 GEE Style OR=1.99 point estimate 的含义\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽，n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W3 (Should-Fix) 再次提出，R2 交叉 AGREE。论文已添加 shrinkage 讨论（§5.2: 'consistent with small-sample upward bias'）和 CI 收缩比率验证（1.94× vs √(355/88)≈2.01）。但仅 Qwen3 formality 一个条件有 n=355 replication。其他条件（特别是 verbosity Style OR 8-13）可能同样存在 ~50% 膨胀（projected 4-6.5 仍 style-dominated）。建议：对 verbosity 轴也执行 scaled replication，或在正文中显著 caveat n=88 ORs 为 upper bound。\"\n    action_items:\n      - round: 16\n        action: \"(1) 对至少一个 verbosity 条件执行 n>200 scaled replication；(2) Table 2 增加 caveat 注释标明 n=88 ORs 可能高估\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R2-W1 (Must-Fix) 再次提出，R1 通过 Q3 间接触及。Abstract 已限定为 'surface-level style features' 但仍使用 'systematically divergent'。两个高度相关轴（FK d=0.50 cross-axis leakage）不足以声称 systematic。建议降级为 'consistent across tested axes' 或增加 1-2 个额外轴。\"\n    action_items:\n      - round: 16\n        action: \"Abstract/Conclusion 中 'systematic' 替换为 'consistent across tested axes' 或类似限定措辞\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W1 (Must-Fix) 重新独立提出并升级为最关键问题之一。R2 交叉 AGREE 并补充：如果 ~35% NLI-passed pairs 存在 content contamination，pairwise 的更高敏感度可能源于对 content 微妙差异的检测力而非 style sensitivity。建议：扩大至全部 88 pairs + 3+ 标注员 + content change taxonomy + sensitivity analysis。\"\n    action_items:\n      - round: 16\n        action: \"(1) 扩大人工验证至全部对（或至少 100 pairs 如等待中的标注批次）；(2) 对 human-flagged content-changed pairs 执行 sensitivity analysis；(3) 考虑更细粒度的 content change taxonomy\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W5 + R2-M5 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W6 (Should-Fix) 再次提出。R2 交叉 [REBUT]——认为 proof-of-concept 下单 judge 足够（Qwen3 是 Likert 效应最强的 judge，保守检验）。分歧点（R1 Should-Fix vs R2 降级），Director 判定为 Minor。\"\n    action_items:\n      - round: 16\n        action: \"Camera-ready 中增加至少一个额外 judge 的 100-point Likert 复制（非紧急）\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W5 (Should-Fix) 再次提出，R2 交叉 AGREE。论文已添加 length-controlled regression（Appendix R'）和 Sobel mediation test（59% 通过句子长度中介），但控制的是 word count 而非 readability 本身。建议：在 GEE 中加入 FK grade 作为协变量验证 formality Style OR 是否依然显著。\"\n    action_items:\n      - round: 16\n        action: \"GEE 中加入 FK grade 作为协变量，报告 controlling for readability 后 formality Style OR 变化\"\n        assigned_to: agent\n        status: open\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R1-W4 (Should-Fix) 再次提出，R2 交叉 AGREE 并补充：GPT-4o 与 target judge GPT-4o 存在完全重叠，且所有替代 rewriter 都是 instruction-tuned LLM——无法排除 instruction-tuned LLM 共性特征导致的 overlap。建议：测试 rule-based paraphrasing 或 human rewriting，或在 Limitations 中讨论 22% 作为 lower bound 的含义。\"\n    action_items:\n      - round: 16\n        action: \"Limitations 中明确讨论 22% OR 降幅是 lower bound，说明 instruction-tuned LLM 替代无法完全排除 shared style preference confound\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1-Minor-1 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: R2-W7 (Minor) 再次提出。Table 1 仍为合并表，建议拆分。与 R13-SF1 合并处理。\"\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Appendix V 已添加完整的 rewriting prompts（formality, verbosity, register, same-style double-rewrite）\"\n    resolution_round: 16\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-Minor-2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [2]\n        note: \"R16: R2-W8 (Minor) 再次提出。论文仍交替使用 'style bias'（暗示方向性偏差）、'style sensitivity'（中性）、'style preference'（描述性），三术语含义不同。\"\n    action_items:\n      - round: 16\n        action: \"全文统一：'style sensitivity' 为默认中性术语，仅在讨论方向性偏好时使用 'style preference'，避免 'style bias'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 2 caption 已展开为 'Originality OR: original-preference odds ratio (OR > 1 favors original text)'\"\n    resolution_round: 16\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及，但应在 camera-ready 前检查。\"\n\n  # ============================================================\n  # Round 16 新发现\n  # ============================================================\n\n  - id: \"R16-W1\"\n    summary: \"Construct divergence 讨论不充分——与 Abstract 三机制并列承诺不匹配\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W4 (Should-Fix): Abstract 承诺三种非排他解释并列，但 attenuation 获完整 bootstrap 分析 + 功效曲线，construct divergence 仅 Section 5.1 末尾一段和 Limitations 简短提及。需操作性定义和可检验预测。与 R15-N1 (framing bias) 相关但独立——R15-N1 关注 title/framing，本条关注 construct divergence 的实质性讨论深度。\"\n    action_items:\n      - round: 16\n        action: \"扩展 construct divergence 讨论为完整段落：含操作性定义（absolute quality vs ordinal preference）、可检验预测（Likert 与 human quality ratings 对齐；pairwise 与 human rankings 对齐）、实践含义差异\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R16-W2\"\n    summary: \"Cross-benchmark 'severity spectrum' 解释为 post-hoc rationalization\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W5 (Should-Fix): Section 5.3 将不同 benchmark 上效果量差异解释为 'severity spectrum'，但无预先假设或理论预测。AlpacaEval 效应更强的归因（'targeting the strongest effects'）为循环论证。建议标记为 exploratory/post-hoc，或提供 benchmark 特性差异的定量分析。\"\n    action_items:\n      - round: 16\n        action: \"severity spectrum 解释明确标记为 post-hoc/exploratory，或补充 benchmark 特性差异（指令长度、领域分布等）的定量分析\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R16-W3\"\n    summary: \"BT 模型 unidimensionality 假设与论文核心论点（multi-dimensional evaluation）存在张力\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W7 (Minor) 提出，R2 交叉 AGREE。Limitations 已提及（'the BT model assumes unidimensionality'）但方法论章节缺乏预先讨论。GEE 引入正是为解决这一问题，但此张力应在 Section 3 中预先交代。\"\n    action_items:\n      - round: 16\n        action: \"Section 3.3 增加一句说明 BT 在此作为 summary statistic 使用，unidimensionality 限制由 GEE 分解层补充\"\n        assigned_to: paper_agent\n        status: open"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-23T06:56:32.246544+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 18805}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-23T06:59:16.242599+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**Venue**: EMNLP 2026 via ARR (May cycle), 截止 2026-05-25\n**Reviewers**: R1（方法严谨性）+ R2（新颖性/完整性）\n**审稿模式**: Fresh（无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，量化 LLM judge 在 Likert 与 pairwise 两种评测模式下对表层风格特征的敏感性差异。核心发现为\"Likert Blindspot\"——pairwise comparison 检测到统计显著的风格偏好（BT p < 0.001），而 Likert 在同一数据上无法检出（p > 0.17），跨 4 个 judge、3 个 benchmark、2 个主轴复制。GEE conditional decomposition 揭示 verbosity 为 style-dominated（Style OR 8–13），formality 为 conditional effect（Style OR 和 Originality OR 均显著）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且具实践意义。** 测量模式对 LLM judge 风格敏感性的影响此前未被严格量化。鉴于 pairwise（RLHF/DPO reward signal）与 Likert（benchmark evaluation）分别主导不同 pipeline 阶段，这一发现对 evaluation 设计有直接操作意义。[R1-S1, R2-S1 共识]\n\n**S2. 统计框架全面且层次清晰。** 三层分析设计（6-test primary family + confirmatory + exploratory）、七种统计方法的 sensitivity hierarchy（Table 13–14）、Holm-Bonferroni 扩展至 8-test family 后结果依然显著（Appendix S）。统计框架本身是方法论贡献。[R1-S2, R2 共识]\n\n**S3. 多 judge × 多 benchmark 系统复制。** 四个独立架构的 judge + 负控制、三个 benchmark 的交叉复制，核心发现一致性强。Verbosity 在全部四个 target judges 上均为 style-dominated（BT > 70%, all p < 0.0001; Likert 全部 NS），这是有力证据。[R1-S3, R2-S3 共识]\n\n**S4. GEE conditional decomposition 是真正的方法论贡献。** 将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 per-axis confound structure 差异——这在 Thurstone 传统中没有对应物。Table 2 的 Style OR vs Originality OR 对比提供了超越\"存在 bias\"的结构性诊断。[R1-S4, R2-S2 共识]\n\n**S5. 写作质量和附录体系。** 8 页正文内容密度高但逻辑清晰，从现象→机制→验证的叙事连贯。20 个附录覆盖广泛的 robustness 分析。[R1-S5, R2-S5 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1. NLI gate content preservation 验证不充分，削弱因果推断基础。**\n[R1-W1, R2 交叉 AGREE]\n\nNLI gate 是 CSD 因果链条的核心——阻断 R→Q 路径确保 rewrite 仅改变 style。但人工验证存在三层不足：(a) 仅 50 pairs（n=88 的 57%），2 名标注员；(b) inter-annotator κ=0.44（moderate），对核心 validity check 偏低；(c) Annotator 2 pass precision 下界仅 65.3%（Wilson CI [65.3%, 93.6%]），意味着最坏情况下约 1/3 gate-passed pairs 存在 content contamination。若此成立，pairwise 的更高敏感度可能部分源于对 content 微妙差异的检测力而非 style sensitivity 本身。GPT-4o cross-validation（92.1%/82.6%）为 LLM 验证而非独立人工验证。\n\n**建议**：扩大人工验证至全部 88 pairs + 3+ 标注员；提供 content change taxonomy（factual error / nuance shift / elaboration）；对 human-flagged content-changed pairs 执行 sensitivity analysis。\n\n**MF2. Negative control (Claude Sonnet 4) 证据不具说服力。**\n[R1-W2, R2-W2 双方独立 Must-Fix, 交叉全部 AGREE]\n\nTOST 在 Δ=10pp 时 power 仅 42%——未能拒绝非等价的 null 不能解释为等价的证据（absence of evidence ≠ evidence of absence）。论文转而依赖三条收敛证据，但每条单独看都不充分：\n- TOST Δ=15pp p=0.01——但 15pp 等价边界过宽（GPT-4o formality BT=63% 已被论文视为显著 style preference，而 Δ=15pp 对应 BT=65%）\n- GEE Style OR 跨三个 benchmark 一致 NS（1.47/1.99/1.64）——但 non-significance ≠ evidence of absence，且 OR=1.99 point estimate 非 trivial\n- GPT-4o contrast——qualitative comparison，非 formal test\n\nNegative control 是验证 CSD pipeline 不产生 false positive 的关键环节。证据不足使读者无法排除 pipeline artifact。\n\n**建议**：(a) 将 negative control 结论降级为 suggestive 而非 definitive；(b) 明确报告达 80% power 所需 n（≈200）；(c) 考虑 Bayesian equivalence testing 或增加第二个 negative control judge。\n\n**MF3. \"Systematic\" claim 基础过窄——仅 2 个主轴。**\n[R2-W1 Must-Fix, R1 间接支持]\n\nAbstract/Conclusion 反复使用\"systematically divergent\"，但一手证据仅来自 formality 和 verbosity，register 为 exploratory 且有 evaluator-producer overlap。两个高度相关的表层轴（FK grade d=0.50 cross-axis leakage）不足以声称\"systematic\"。Semantic-level axes（hedging, humor）被 NLI gate 系统性拒绝，限制了 CSD 的适用范围。\n\n**建议**：将\"systematic\"降级为\"consistent across tested axes\"或类似限定措辞。\n\n### Should-Fix\n\n**SF1. GEE OR 在 n=88→355 时出现 49% shrinkage，Table 2 效应量可能普遍高估。**\n[R1-W3, R2 交叉 AGREE]\n\nQwen3-32B formality Style OR 从 4.20 降至 2.15（−49%），远超 Nemes et al. (2009) 报告的典型校正幅度。仅此一个条件有 scaled replication——其他条件的 ORs（特别是 verbosity Style OR 8–13）可能同样存在膨胀。虽然 qualitative regime classification 在 ~50% shrinkage 下可能不变（projected verbosity 4–6.5 仍 >> Orig OR < 1），但 effect size 量级解读受影响。\n\n**建议**：对至少一个 verbosity 条件执行 scaled replication；Table 2 增加 caveat 标明 n=88 ORs 可能为 upper bound。\n\n**SF2. Construct divergence 讨论不充分，与 Abstract 三机制并列承诺不匹配。**\n[R2-W4, R1-W8 相关]\n\nAttenuation 获得完整 bootstrap 分析（Appendix K）和功效曲线（Figure 4），construct divergence 仅 Section 5.1 末段和 Limitations 简短提及。如果三种解释声称并列，construct divergence 需要同等深度——至少包含操作性定义（absolute quality vs ordinal preference）和可检验预测。\n\n**SF3. Evaluator-producer overlap 缓解不充分。**\n[R1-W4, R2 交叉 AGREE]\n\n仅用 GPT-4o 作为替代 rewriter，22% OR 降幅是 lower bound。GPT-4o 与 target judge GPT-4o 存在完全重叠，且所有替代 rewriter 都是 instruction-tuned LLM——无法排除 shared training distribution 的 confound。22% 意味着约 1/5 的观测效应可能来自 overlap。\n\n**建议**：在 Limitations 中明确讨论 22% 作为 lower bound 的含义和 instruction-tuned LLM 替代的局限。\n\n**SF4. FK grade d=0.50 cross-axis contamination 未被充分控制。**\n[R1-W5, R2 交叉 AGREE]\n\nLength-controlled regression 和 Sobel mediation test 控制了 word count/sentence length，但 FK grade 还反映 readability/complexity。d=0.50 的 readability shift 可能独立于 verbosity 影响 judge quality perception。\n\n**建议**：GEE 中加入 FK grade 作为协变量验证 formality Style OR 是否依然显著。\n\n**SF5. Cross-benchmark \"severity spectrum\" 为 post-hoc 解释。**\n[R2-W5]\n\nSection 5.3 将不同 benchmark 效果量差异解释为 severity spectrum，但无预先假设。AlpacaEval 效应更强的归因缺乏 benchmark 特性差异的定量支撑。\n\n**建议**：明确标记为 exploratory/post-hoc。\n\n### Minor\n\n**M1. Title \"Blindspot\" 隐含 Likert attenuation 因果偏好。**\n[R1-W8, R2-W6 双方独立指出, 交叉全部 AGREE]\n\n标题和正文将分歧框架为 Likert 的\"盲点\"，但论文自身承认 pairwise amplification 同样可能。等价的替代解读：pairwise 对 surface-level style 过度敏感，Likert 正确忽略了不应影响 quality judgment 的因素。\n\n**M2. Table 1 信息密度过高。**\n[R1 Minor, R2-W7 Minor, 交叉 AGREE]\n\n15 行 + 6 行脚注挤在一张表。建议拆分为 LLMBar primary (4 judges × 2 axes) + cross-benchmark replication 两表。\n\n**M3. 'style bias' / 'style sensitivity' / 'style preference' 术语混用。**\n[R2-W8, R1 间接相关]\n\n三个术语含义不同（bias=方向性偏差, sensitivity=双向响应性, preference=描述性），应统一或明确区分。\n\n**M4. BT unidimensionality 假设与论文多维评估论点存在张力。**\n[R1-W7, R2 交叉 AGREE]\n\nLimitations 已提及但方法论章节缺乏预先讨论。应在 Section 3 说明 BT 在此作为 summary statistic，unidimensionality 限制由 GEE 补充。\n\n**M5. 100-point continuous Likert 仅在 Qwen3-32B 上测试。**\n[R1-W6 Should-Fix, R2 交叉 REBUT 降级为 Minor]\n\nR2 认为 proof-of-concept 下单 judge 足够（Qwen3 是 Likert 效应最强的 judge，保守检验）。Director 采纳 R2 判断，降级为 Minor。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识（[AGREE]）：\n\n1. **TOST underpowered** [R1-W2 = R2-W2]：negative control 证据不具说服力\n2. **NLI gate validation** [R1-W1, R2 AGREE]：人工验证规模和质量不足\n3. **Claim scope** [R2-W1, R1 间接]：2 axes → \"systematic\" 过宽\n4. **GEE OR shrinkage** [R1-W3, R2 AGREE]：n=88 效应量可能高估\n5. **Framing bias** [R1-W8 = R2-W6]：title 隐含 Likert 为缺陷方\n6. **Evaluator-producer overlap** [R1-W4, R2 AGREE]：单一替代 rewriter 不充分\n7. **Likert power** [R1-Q3 = R2-Q5]：Likert non-significance 可能仅反映 power 不足——替代解释讨论不充分\n\n---\n\n## Reviewer Divergence\n\n仅一处分歧：\n\n- **100-point Likert 复制**：R1 列为 Should-Fix（需多 judge 复制），R2 REBUT 降级（proof-of-concept 足够）。Director 采纳 R2 判断降级为 Minor。\n\n---\n\n## Questions\n\n**Q1.** Likert non-significance 是否仅反映 power 不足？Formal power analysis 显示 5/6 cells 需 n ≥ 1,200。Bootstrap attenuation analysis（Appendix K）论证 d→0 是 structural 而非 power issue，但此分析以 pairwise 效应量为 benchmark——存在循环论证嫌疑。[R1-Q3, R2-Q5 独立提出]\n\n**Q2.** Table 2 verbosity Orig OR < 1（全部四个 judges）——verbose rewrites 是否系统性引入 quality improvement？若是，pairwise 的高敏感度可能反映 content quality difference 而非 style sensitivity。[R1-Q1]\n\n**Q3.** Direction-aware gating 额外放入的 21 pairs (32%) 是否在 BT/Likert 效应量上与原有 pairs 有系统差异？[R1-Q2, R2-Q3]\n\n**Q4.** GEE exchangeable working correlation 是否对 AR(1)/unstructured 敏感？Appendix D 报告了 QIC 差异 < 0.001 和系数变化 < 0.02，但未报告替代结构的完整结果。[R1-Q4, R2-Q2]\n\n**Q5.** 论文选择 formality 和 verbosity 是否因为这两个轴最容易通过 NLI gate？如果是，这引入选择偏差——论文仅展示了 CSD 最有利的案例。[R2-Q1]\n\n**Q6.** 所有 target judges 均为 instruction-tuned chat models。Base models 上 Blindspot 是否存在？Instruction tuning 本身可能引入 style preference。[R1-Q5]\n\n**Q7.** 4 个 target judges 均为 2024 下半年版本，风格敏感度是否随模型迭代变化（时间效度问题）？[R2-Q4]\n\n---\n\n## Missing References\n\n- **Item Response Theory (IRT)**: 论文讨论 Likert 测量属性但未引用 IRT 框架。IRT 可定量回答\"Likert 为什么在某些效应量下失效\"。至少应引用 Embretson & Reise (2000) 或 de Ayala (2009)。[R2]\n- **Bojar et al. (2016) WMT 转变经验**: 论文仅在 Section 3 脚注级别提及 WMT 从 ranking 到 rating 的转变，但未深入讨论社区积累的经验教训——这与核心论点直接相关。[R2]\n- 其余引用覆盖充分。[R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 3.5 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | pp.3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 display item。建议前移 Figure 2（因果 DAG）或在 Related Work 加小型 summary table |\n| ℹ️ Info | p.2 | Figure 1（pipeline overview）单栏宽度，节点标签打印时可能偏小 |\n| ℹ️ Info | p.5 | Figure 2 红色/橙色路径灰度打印区分度低，建议辅以不同线型 |\n| ℹ️ Info | p.6 | Table 1 最优结果未加粗 |\n| ℹ️ Info | p.7 | Figure 4 power 曲线图例文字偏小 |\n| ℹ️ Info | p.9 | Limitations 篇幅较长但内容充实，不影响评审 |\n| ℹ️ Info | pp.11-17 | Appendix 全为数值表格无 figure，视觉单调但可接受 |\n| ℹ️ Info | p.20 | 最后一页 references 底部空白，正常 |\n\n总计：0 critical, 1 warning, 7 info。排版质量整体良好，无格式违规。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**Confidence: 4/5**\n\n**两位 Reviewer 一致评分 3.5，核心评估高度收敛。**\n\n### 汇总判断\n\n**方法论设计用心**——CSD pipeline 的三层控制（NLI gate → position swap → axis isolation）、GEE conditional decomposition、七方法 sensitivity hierarchy 展现了严谨的实验设计理念。4 judges × 3 benchmarks 的系统复制使核心发现不易被归因于 artifact。\n\n**但因果推断链条存在两个关键缺口**：\n1. NLI gate 人工验证（MF1: κ=0.44, precision 下界 65.3%）不足以建立\"rewrite 仅改变 style\"的因果前提\n2. Negative control 证据（MF2: TOST power 42%）不足以排除 pipeline artifact\n\n**Claim 强度超出证据**：\n3. 2 个主轴 → \"systematic\"（MF3）\n4. GEE OR 可能高估 ~50%（SF1）\n5. Construct divergence 讨论深度不匹配（SF2）\n\n**核心增量贡献（GEE decomposition）被 undersold**——论文将 \"Blindspot\" discovery 置于叙事中心，但 per-axis confound structure 的方法论贡献（Thurstone 传统中无对应物）更具持久价值。\n\n### 改进路径\n\n修复 MF1（扩大人工验证）+ MF2（增强 negative control 证据）+ MF3（限定 claim scope）后，论文有望提升至 4.0（Conference）。GEE decomposition 的方法论贡献足够支撑接收，但当前 framing 遮蔽了这一优势。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: \"systematically divergent sensitivity\" 超出 2 轴证据（→ MF3）。三机制并列但 construct divergence 在正文中发展不足（→ SF2）。\n\n**Introduction**: 操作性定义 Blindspot 为\"measurement-mode divergence\"是改进。Thurstone 讨论的 3 个 LLM-specific distinctions（per-axis structure, source decomposition, binary split）有说服力。但 Title 仍偏向 attenuation 解释（→ M1）。\n\n**Method (§3)**: CSD pipeline 设计清晰。DAG（Figure 2）有效传达设计逻辑。Direction-aware NLI gating 的理论依据充分（§3.2）。建议在 §3.3 预先讨论 BT unidimensionality 限制（→ M4）。\n\n**Experiments (§4-5)**: 三层统计框架值得推广。Table 1 信息密度需降低（→ M2）。GEE decomposition 结果（Table 2）是论文最有价值的内容。n=88→355 shrinkage 讨论应更显著（→ SF1）。\n\n**Robustness (§5.4)**: 六控制设计思路好，但每条证据的单独强度有限。NLI ablation（Appendix P）中 NLI-fail pairs 反转（BT 41.7%）是 gate 有效性的有力佐证。\n\n**Limitations**: 覆盖面广（quality-style confounding, evaluator-producer, scope, validation methodology），但多个 reviewer 关切点（TOST power 含义、22% overlap 上界、FK readability）可进一步展开。\n\n**Appendix**: 体系完整（A-Y），NLI threshold sweep（Appendix F）、GEE diagnostics（Appendix D）、rewriter independence（Appendix E）等提供了充分的技术细节。Rewriting prompts（Appendix V）已补全。",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**Venue**: EMNLP 2026 via ARR (May cycle), 截止 2026-05-25\n**Reviewers**: R1（方法严谨性）+ R2（新颖性/完整性）\n**审稿模式**: Fresh（无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，量化 LLM judge 在 Likert 与 pairwise 两种评测模式下对表层风格特征的敏感性差异。核心发现为\"Likert Blindspot\"——pairwise comparison 检测到统计显著的风格偏好（BT p < 0.001），而 Likert 在同一数据上无法检出（p > 0.17），跨 4 个 judge、3 个 benchmark、2 个主轴复制。GEE conditional decomposition 揭示 verbosity 为 style-dominated（Style OR 8–13），formality 为 conditional effect（Style OR 和 Originality OR 均显著）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且具实践意义。** 测量模式对 LLM judge 风格敏感性的影响此前未被严格量化。鉴于 pairwise（RLHF/DPO reward signal）与 Likert（benchmark evaluation）分别主导不同 pipeline 阶段，这一发现对 evaluation 设计有直接操作意义。[R1-S1, R2-S1 共识]\n\n**S2. 统计框架全面且层次清晰。** 三层分析设计（6-test primary family + confirmatory + exploratory）、七种统计方法的 sensitivity hierarchy（Table 13–14）、Holm-Bonferroni 扩展至 8-test family 后结果依然显著（Appendix S）。统计框架本身是方法论贡献。[R1-S2, R2 共识]\n\n**S3. 多 judge × 多 benchmark 系统复制。** 四个独立架构的 judge + 负控制、三个 benchmark 的交叉复制，核心发现一致性强。Verbosity 在全部四个 target judges 上均为 style-dominated（BT > 70%, all p < 0.0001; Likert 全部 NS），这是有力证据。[R1-S3, R2-S3 共识]\n\n**S4. GEE conditional decomposition 是真正的方法论贡献。** 将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 per-axis confound structure 差异——这在 Thurstone 传统中没有对应物。Table 2 的 Style OR vs Originality OR 对比提供了超越\"存在 bias\"的结构性诊断。[R1-S4, R2-S2 共识]\n\n**S5. 写作质量和附录体系。** 8 页正文内容密度高但逻辑清晰，从现象→机制→验证的叙事连贯。20 个附录覆盖广泛的 robustness 分析。[R1-S5, R2-S5 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1. NLI gate content preservation 验证不充分，削弱因果推断基础。**\n[R1-W1, R2 交叉 AGREE]\n\nNLI gate 是 CSD 因果链条的核心——阻断 R→Q 路径确保 rewrite 仅改变 style。但人工验证存在三层不足：(a) 仅 50 pairs（n=88 的 57%），2 名标注员；(b) inter-annotator κ=0.44（moderate），对核心 validity check 偏低；(c) Annotator 2 pass precision 下界仅 65.3%（Wilson CI [65.3%, 93.6%]），意味着最坏情况下约 1/3 gate-passed pairs 存在 content contamination。若此成立，pairwise 的更高敏感度可能部分源于对 content 微妙差异的检测力而非 style sensitivity 本身。GPT-4o cross-validation（92.1%/82.6%）为 LLM 验证而非独立人工验证。\n\n**建议**：扩大人工验证至全部 88 pairs + 3+ 标注员；提供 content change taxonomy（factual error / nuance shift / elaboration）；对 human-flagged content-changed pairs 执行 sensitivity analysis。\n\n**MF2. Negative control (Claude Sonnet 4) 证据不具说服力。**\n[R1-W2, R2-W2 双方独立 Must-Fix, 交叉全部 AGREE]\n\nTOST 在 Δ=10pp 时 power 仅 42%——未能拒绝非等价的 null 不能解释为等价的证据（absence of evidence ≠ evidence of absence）。论文转而依赖三条收敛证据，但每条单独看都不充分：\n- TOST Δ=15pp p=0.01——但 15pp 等价边界过宽（GPT-4o formality BT=63% 已被论文视为显著 style preference，而 Δ=15pp 对应 BT=65%）\n- GEE Style OR 跨三个 benchmark 一致 NS（1.47/1.99/1.64）——但 non-significance ≠ evidence of absence，且 OR=1.99 point estimate 非 trivial\n- GPT-4o contrast——qualitative comparison，非 formal test\n\nNegative control 是验证 CSD pipeline 不产生 false positive 的关键环节。证据不足使读者无法排除 pipeline artifact。\n\n**建议**：(a) 将 negative control 结论降级为 suggestive 而非 definitive；(b) 明确报告达 80% power 所需 n（≈200）；(c) 考虑 Bayesian equivalence testing 或增加第二个 negative control judge。\n\n**MF3. \"Systematic\" claim 基础过窄——仅 2 个主轴。**\n[R2-W1 Must-Fix, R1 间接支持]\n\nAbstract/Conclusion 反复使用\"systematically divergent\"，但一手证据仅来自 formality 和 verbosity，register 为 exploratory 且有 evaluator-producer overlap。两个高度相关的表层轴（FK grade d=0.50 cross-axis leakage）不足以声称\"systematic\"。Semantic-level axes（hedging, humor）被 NLI gate 系统性拒绝，限制了 CSD 的适用范围。\n\n**建议**：将\"systematic\"降级为\"consistent across tested axes\"或类似限定措辞。\n\n### Should-Fix\n\n**SF1. GEE OR 在 n=88→355 时出现 49% shrinkage，Table 2 效应量可能普遍高估。**\n[R1-W3, R2 交叉 AGREE]\n\nQwen3-32B formality Style OR 从 4.20 降至 2.15（−49%），远超 Nemes et al. (2009) 报告的典型校正幅度。仅此一个条件有 scaled replication——其他条件的 ORs（特别是 verbosity Style OR 8–13）可能同样存在膨胀。虽然 qualitative regime classification 在 ~50% shrinkage 下可能不变（projected verbosity 4–6.5 仍 >> Orig OR < 1），但 effect size 量级解读受影响。\n\n**建议**：对至少一个 verbosity 条件执行 scaled replication；Table 2 增加 caveat 标明 n=88 ORs 可能为 upper bound。\n\n**SF2. Construct divergence 讨论不充分，与 Abstract 三机制并列承诺不匹配。**\n[R2-W4, R1-W8 相关]\n\nAttenuation 获得完整 bootstrap 分析（Appendix K）和功效曲线（Figure 4），construct divergence 仅 Section 5.1 末段和 Limitations 简短提及。如果三种解释声称并列，construct divergence 需要同等深度——至少包含操作性定义（absolute quality vs ordinal preference）和可检验预测。\n\n**SF3. Evaluator-producer overlap 缓解不充分。**\n[R1-W4, R2 交叉 AGREE]\n\n仅用 GPT-4o 作为替代 rewriter，22% OR 降幅是 lower bound。GPT-4o 与 target judge GPT-4o 存在完全重叠，且所有替代 rewriter 都是 instruction-tuned LLM——无法排除 shared training distribution 的 confound。22% 意味着约 1/5 的观测效应可能来自 overlap。\n\n**建议**：在 Limitations 中明确讨论 22% 作为 lower bound 的含义和 instruction-tuned LLM 替代的局限。\n\n**SF4. FK grade d=0.50 cross-axis contamination 未被充分控制。**\n[R1-W5, R2 交叉 AGREE]\n\nLength-controlled regression 和 Sobel mediation test 控制了 word count/sentence length，但 FK grade 还反映 readability/complexity。d=0.50 的 readability shift 可能独立于 verbosity 影响 judge quality perception。\n\n**建议**：GEE 中加入 FK grade 作为协变量验证 formality Style OR 是否依然显著。\n\n**SF5. Cross-benchmark \"severity spectrum\" 为 post-hoc 解释。**\n[R2-W5]\n\nSection 5.3 将不同 benchmark 效果量差异解释为 severity spectrum，但无预先假设。AlpacaEval 效应更强的归因缺乏 benchmark 特性差异的定量支撑。\n\n**建议**：明确标记为 exploratory/post-hoc。\n\n### Minor\n\n**M1. Title \"Blindspot\" 隐含 Likert attenuation 因果偏好。**\n[R1-W8, R2-W6 双方独立指出, 交叉全部 AGREE]\n\n标题和正文将分歧框架为 Likert 的\"盲点\"，但论文自身承认 pairwise amplification 同样可能。等价的替代解读：pairwise 对 surface-level style 过度敏感，Likert 正确忽略了不应影响 quality judgment 的因素。\n\n**M2. Table 1 信息密度过高。**\n[R1 Minor, R2-W7 Minor, 交叉 AGREE]\n\n15 行 + 6 行脚注挤在一张表。建议拆分为 LLMBar primary (4 judges × 2 axes) + cross-benchmark replication 两表。\n\n**M3. 'style bias' / 'style sensitivity' / 'style preference' 术语混用。**\n[R2-W8, R1 间接相关]\n\n三个术语含义不同（bias=方向性偏差, sensitivity=双向响应性, preference=描述性），应统一或明确区分。\n\n**M4. BT unidimensionality 假设与论文多维评估论点存在张力。**\n[R1-W7, R2 交叉 AGREE]\n\nLimitations 已提及但方法论章节缺乏预先讨论。应在 Section 3 说明 BT 在此作为 summary statistic，unidimensionality 限制由 GEE 补充。\n\n**M5. 100-point continuous Likert 仅在 Qwen3-32B 上测试。**\n[R1-W6 Should-Fix, R2 交叉 REBUT 降级为 Minor]\n\nR2 认为 proof-of-concept 下单 judge 足够（Qwen3 是 Likert 效应最强的 judge，保守检验）。Director 采纳 R2 判断，降级为 Minor。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识（[AGREE]）：\n\n1. **TOST underpowered** [R1-W2 = R2-W2]：negative control 证据不具说服力\n2. **NLI gate validation** [R1-W1, R2 AGREE]：人工验证规模和质量不足\n3. **Claim scope** [R2-W1, R1 间接]：2 axes → \"systematic\" 过宽\n4. **GEE OR shrinkage** [R1-W3, R2 AGREE]：n=88 效应量可能高估\n5. **Framing bias** [R1-W8 = R2-W6]：title 隐含 Likert 为缺陷方\n6. **Evaluator-producer overlap** [R1-W4, R2 AGREE]：单一替代 rewriter 不充分\n7. **Likert power** [R1-Q3 = R2-Q5]：Likert non-significance 可能仅反映 power 不足——替代解释讨论不充分\n\n---\n\n## Reviewer Divergence\n\n仅一处分歧：\n\n- **100-point Likert 复制**：R1 列为 Should-Fix（需多 judge 复制），R2 REBUT 降级（proof-of-concept 足够）。Director 采纳 R2 判断降级为 Minor。\n\n---\n\n## Questions\n\n**Q1.** Likert non-significance 是否仅反映 power 不足？Formal power analysis 显示 5/6 cells 需 n ≥ 1,200。Bootstrap attenuation analysis（Appendix K）论证 d→0 是 structural 而非 power issue，但此分析以 pairwise 效应量为 benchmark——存在循环论证嫌疑。[R1-Q3, R2-Q5 独立提出]\n\n**Q2.** Table 2 verbosity Orig OR < 1（全部四个 judges）——verbose rewrites 是否系统性引入 quality improvement？若是，pairwise 的高敏感度可能反映 content quality difference 而非 style sensitivity。[R1-Q1]\n\n**Q3.** Direction-aware gating 额外放入的 21 pairs (32%) 是否在 BT/Likert 效应量上与原有 pairs 有系统差异？[R1-Q2, R2-Q3]\n\n**Q4.** GEE exchangeable working correlation 是否对 AR(1)/unstructured 敏感？Appendix D 报告了 QIC 差异 < 0.001 和系数变化 < 0.02，但未报告替代结构的完整结果。[R1-Q4, R2-Q2]\n\n**Q5.** 论文选择 formality 和 verbosity 是否因为这两个轴最容易通过 NLI gate？如果是，这引入选择偏差——论文仅展示了 CSD 最有利的案例。[R2-Q1]\n\n**Q6.** 所有 target judges 均为 instruction-tuned chat models。Base models 上 Blindspot 是否存在？Instruction tuning 本身可能引入 style preference。[R1-Q5]\n\n**Q7.** 4 个 target judges 均为 2024 下半年版本，风格敏感度是否随模型迭代变化（时间效度问题）？[R2-Q4]\n\n---\n\n## Missing References\n\n- **Item Response Theory (IRT)**: 论文讨论 Likert 测量属性但未引用 IRT 框架。IRT 可定量回答\"Likert 为什么在某些效应量下失效\"。至少应引用 Embretson & Reise (2000) 或 de Ayala (2009)。[R2]\n- **Bojar et al. (2016) WMT 转变经验**: 论文仅在 Section 3 脚注级别提及 WMT 从 ranking 到 rating 的转变，但未深入讨论社区积累的经验教训——这与核心论点直接相关。[R2]\n- 其余引用覆盖充分。[R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 3.5 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | pp.3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 display item。建议前移 Figure 2（因果 DAG）或在 Related Work 加小型 summary table |\n| ℹ️ Info | p.2 | Figure 1（pipeline overview）单栏宽度，节点标签打印时可能偏小 |\n| ℹ️ Info | p.5 | Figure 2 红色/橙色路径灰度打印区分度低，建议辅以不同线型 |\n| ℹ️ Info | p.6 | Table 1 最优结果未加粗 |\n| ℹ️ Info | p.7 | Figure 4 power 曲线图例文字偏小 |\n| ℹ️ Info | p.9 | Limitations 篇幅较长但内容充实，不影响评审 |\n| ℹ️ Info | pp.11-17 | Appendix 全为数值表格无 figure，视觉单调但可接受 |\n| ℹ️ Info | p.20 | 最后一页 references 底部空白，正常 |\n\n总计：0 critical, 1 warning, 7 info。排版质量整体良好，无格式违规。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**Confidence: 4/5**\n\n**两位 Reviewer 一致评分 3.5，核心评估高度收敛。**\n\n### 汇总判断\n\n**方法论设计用心**——CSD pipeline 的三层控制（NLI gate → position swap → axis isolation）、GEE conditional decomposition、七方法 sensitivity hierarchy 展现了严谨的实验设计理念。4 judges × 3 benchmarks 的系统复制使核心发现不易被归因于 artifact。\n\n**但因果推断链条存在两个关键缺口**：\n1. NLI gate 人工验证（MF1: κ=0.44, precision 下界 65.3%）不足以建立\"rewrite 仅改变 style\"的因果前提\n2. Negative control 证据（MF2: TOST power 42%）不足以排除 pipeline artifact\n\n**Claim 强度超出证据**：\n3. 2 个主轴 → \"systematic\"（MF3）\n4. GEE OR 可能高估 ~50%（SF1）\n5. Construct divergence 讨论深度不匹配（SF2）\n\n**核心增量贡献（GEE decomposition）被 undersold**——论文将 \"Blindspot\" discovery 置于叙事中心，但 per-axis confound structure 的方法论贡献（Thurstone 传统中无对应物）更具持久价值。\n\n### 改进路径\n\n修复 MF1（扩大人工验证）+ MF2（增强 negative control 证据）+ MF3（限定 claim scope）后，论文有望提升至 4.0（Conference）。GEE decomposition 的方法论贡献足够支撑接收，但当前 framing 遮蔽了这一优势。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: \"systematically divergent sensitivity\" 超出 2 轴证据（→ MF3）。三机制并列但 construct divergence 在正文中发展不足（→ SF2）。\n\n**Introduction**: 操作性定义 Blindspot 为\"measurement-mode divergence\"是改进。Thurstone 讨论的 3 个 LLM-specific distinctions（per-axis structure, source decomposition, binary split）有说服力。但 Title 仍偏向 attenuation 解释（→ M1）。\n\n**Method (§3)**: CSD pipeline 设计清晰。DAG（Figure 2）有效传达设计逻辑。Direction-aware NLI gating 的理论依据充分（§3.2）。建议在 §3.3 预先讨论 BT unidimensionality 限制（→ M4）。\n\n**Experiments (§4-5)**: 三层统计框架值得推广。Table 1 信息密度需降低（→ M2）。GEE decomposition 结果（Table 2）是论文最有价值的内容。n=88→355 shrinkage 讨论应更显著（→ SF1）。\n\n**Robustness (§5.4)**: 六控制设计思路好，但每条证据的单独强度有限。NLI ablation（Appendix P）中 NLI-fail pairs 反转（BT 41.7%）是 gate 有效性的有力佐证。\n\n**Limitations**: 覆盖面广（quality-style confounding, evaluator-producer, scope, validation methodology），但多个 reviewer 关切点（TOST power 含义、22% overlap 上界、FK readability）可进一步展开。\n\n**Appendix**: 体系完整（A-Y），NLI threshold sweep（Appendix F）、GEE diagnostics（Appendix D）、rewriter independence（Appendix E）等提供了充分的技术细节。Rewriting prompts（Appendix V）已补全。",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-23T06:59:21.157317+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4914
}
```

</details>

---


### Assistant

_source line 1330 · 2026-05-23T06:59:36.398257+00:00_

审稿报告已投递。

**Round 16 审稿完成总结：**

- **Overall Score**: 3.5 (Borderline Conference)
- **两位 Reviewer 一致评分 3.5**，核心评估高度收敛
- **3 个 Must-Fix**：NLI gate 人工验证不足（κ=0.44, precision 下界 65.3%）、Negative control TOST underpowered（power 42%）、"systematic" claim 超出 2 轴证据
- **5 个 Should-Fix**：GEE OR 49% shrinkage、construct divergence 讨论不足、evaluator-producer overlap 缓解不充分、FK grade 未控制 readability、severity spectrum post-hoc
- **5 个 Minor**：Title framing bias、Table 1 信息密度、术语混用、BT unidimensionality 张力、100-point Likert 单 judge
- **改进路径**：修复 MF1-3 后有望提升至 4.0（Conference）
- **Issue tracker 已同步更新**（2 个 issue resolved, 其余 in_progress/open 附带 R16 action items）
- **视觉审查**：0 critical, 1 warning, 7 info

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1331 · 2026-05-23T06:59:37.533782+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

对 R1 的 8 个 Weakness 中 7 个 [AGREE]、1 个 [REBUT]（W6: 100-point Likert 单 judge 测试——作为 proof-of-concept 足够）；6 个 Question 中 5 个 [AGREE]、1 个 [REBUT]（Q6: Holm-Bonferroni margin 已在 Appendix S 报告）。

两位 reviewer 独立收敛的核心问题：TOST underpowered、Likert power 不足作为替代解释、framing bias。综合判断维持 3.5 (Borderline Conference)。

---

[Reviewer 1 审稿意见]:

## Cross-Response to Reviewer 2 (Novelty/Completeness)

---

### Strengths

[AGREE] R2-S1: CSD 管线解耦思路清晰。同意。我在 R1-S2/S4 中也认可了 pipeline 设计和 GEE decomposition 的贡献。但需补充一点：R2 称"NLI gate 双向验证有效控制了改写引入的内容噪声"——我对此持保留意见。我的 R1-W1 已指出 NLI gate 的 human validation 存在显著缺口（κ=0.44, precision lower bound 65.3%），"有效控制"这一判断可能过于乐观。

[AGREE] R2-S2: GEE conditional decomposition 是真正的方法论贡献。完全同意，这也是我 R1-S4 的核心判断。将 aggregate preference 分解为 style-specific 和 quality-correlated components 确实超越了现有 Thurstone 框架。

[AGREE] R2-S3: 多维度复制。同意，与我 R1-S3 一致。

[AGREE] R2-S4: BT 建模合理。部分同意。Appendix I 的 goodness-of-fit 通过了，但如我 R1-W7 所述，goodness-of-fit ≠ assumption validation——BT 的 unidimensionality 假设与论文多维度评估的核心论点存在张力，R2 未关注到这一点。

[AGREE] R2-S5: 附录详尽。同意。

---

### Weaknesses

**[AGREE] R2-W1: "Systematic pattern" claim 基础过窄（仅 2 个主轴）。**

同意这一批评的方向。两个主轴（formality, verbosity）加一个探索性轴（register）确实不足以支撑 Abstract 和 Conclusion 中反复使用的"systematic pattern for surface-level style features"。Register 在 Table 1 中的数据也较弱（部分 judge 上 BT 不显著），难以作为第三个独立支撑点。论文应将 claim 收窄至"formality 和 verbosity 轴上存在系统性的测量模式差异"，并明确 register 为 exploratory。

不过，我要补充 R2 未提及的一点：即使仅两个轴，论文的贡献也不仅在于发现 pattern，更在于提供了 CSD 这一诊断方法论。方法论贡献的价值不完全依赖于覆盖的轴数量。建议论文在 framing 上更明确区分 method contribution（CSD pipeline + GEE decomposition）和 empirical finding（在 formality/verbosity 上的具体发现）。

**[AGREE] R2-W2: Negative control TOST underpowered。**

同意，这与我 R1-W2 完全一致。R2 报告 TOST 在 Δ=10pp 下 power 仅 12%——比我原始审稿引用的数字更低，如果 12% 是正确的（参见 Section 5.1 正文），则 negative control 的证据基础比我初评时判断的更弱。Power=12% 意味着这个检验几乎没有区分能力。

R2 对"三条收敛证据"的质疑也合理：(1) TOST 在 Δ=15pp 时 p=0.01 但边界过宽；(2) GEE non-significance 不等于 evidence of absence（且 Style OR=1.99 的 point estimate 并非 trivial，这点我在 R1-W2 中已指出）；(3) GPT-4o contrast 是 qualitative 而非 formal test。三条弱证据的"收敛"不等于一条强证据。

**[REBUT] R2-W3: Novelty 定位模糊——Blindspot 被过度包装，GEE 被 undersold。**

部分不同意。R2 认为 GEE decomposition 才是核心贡献，Blindspot 只是包装——但我认为 Blindspot 发现本身有独立的实践价值。对于使用 LLM judge 的 practitioner 而言，"pairwise 和 Likert 对 style 的敏感性有定性差异"是一个直接可操作的 insight，比 GEE decomposition 的方法论贡献更容易转化为实践指南。

论文的问题不在于 Blindspot 被"过度包装"，而在于未能充分回答 Blindspot 的 mechanism 问题——它究竟是 attenuation（power issue）还是 construct divergence（质的差异）？如果仅仅是 power issue（Q5），那"Blindspot"的命名确实过强。论文需要更清晰地论证为什么这不仅仅是 sensitivity 差异。100-point Likert 实验（Appendix O）试图做这一点但仅在一个 judge 上测试（我的 R1-W6）。

不过 R2 关于"Thurstone 以来的增量贡献未充分明确"的观点有道理——Section 2 的 related work 确实未充分区分 CSD 相对于 Thurstone (1927) 和 David (1988) 等经典测量理论的具体增量。建议补充。

**[AGREE] R2-W4: Construct divergence 发展不足。**

同意。论文 Section 5.1 提出三个非互斥解释（attenuation, format amplification, construct divergence），但分配极不均匀：attenuation 获得了 Figure 4 的 bootstrap 分析、Appendix K 的 formal power analysis、以及 Section 5.1 中多段详细讨论；而 construct divergence 仅在 Section 5.1 末尾用一段提及（"the two formats may measure genuinely different facets—absolute quality versus ordinal preference"），无独立实验或数据支撑。

这是一个结构性问题：Abstract 承诺"three non-exclusive explanations"，但论文实际上只 develop 了一个半（attenuation + partial format amplification discussion）。如果 construct divergence 没有数据支撑，应在 Abstract 和 Conclusion 中降低其权重，而不是作为并列解释呈现。

**[REBUT] R2-W5: Cross-benchmark severity spectrum 为 post-hoc rationalization。**

部分不同意。R2 指出 severity spectrum 解释缺乏先验假设，这是事实。但在实证研究中，exploratory analysis 的 post-hoc 性质并不自动使其无效，关键是论文是否将其当作 confirmatory 结论呈现。

查看论文 Section 5.3（p.8）和 Section 4.1 中的措辞："Cross-benchmark replication confirms the severity spectrum: Llama-70B formality on AlpacaEval BT 75.6%..."——"confirms"这一用词确实过强，暗示这是一个被验证的预测而非 post-hoc observation。但论文在 Section 4.1 中已将 cross-benchmark 分析归类为"exploratory"（"Analyses outside this grid are classified as either exploratory"），与 R2 的批评存在矛盾。

建议：论文应统一措辞——既然 cross-benchmark 被归类为 exploratory，就不应在 Section 5.3 中用"confirms"，改为"is consistent with"或"suggests"。这是一个 framing/措辞问题，不是方法论问题。

**[AGREE] R2-W6: Title "Blindspot" 隐含因果偏好。**

同意，与我 R1-W8 一致。"Blindspot"预设 Likert 的不敏感是缺陷而非特征。

**[REBUT] R2-W7: Table 1 信息密度过高。**

不同意。在 8 页正文限制下，Table 1 将 5 judges × 3 axes × 3 metrics 的核心结果压缩为一张表是合理的空间权衡。拆分为多张表会消耗宝贵的正文空间，且读者需在多张表之间切换才能比较 judge 间和 axis 间的 pattern。Table 1 的结构（按 judge 分组，每行一个 axis，列为 BT/Likert d/Cs）是直观的。如果 R2 认为 readability 有问题，可以建议改善 formatting（如加粗关键数字、增加行间距），而非拆分。

**[AGREE] R2-W8: 'style bias' 与 'style sensitivity' 混用。**

同意。这两个术语有不同含义：'style bias' 暗示 judges 有不当的风格偏好（normative judgment），'style sensitivity' 仅描述对风格的检测能力（descriptive）。论文应统一使用一个术语，并在首次出现时明确定义。考虑到论文的实际发现是 measurement-mode difference，'style sensitivity' 是更中性准确的选择。

---

### Questions

**[AGREE] R2-Q1: Formality 和 verbosity 的选择是否因为最容易通过 NLI gate？**

这是一个重要的 selection bias 问题。论文 Section 3.4 将选择理由归为"these are among the most commonly reported style sensitivities in LLM judges (Wu and Aji, 2025; Saito et al., 2025)"——这是合理的动机。但 R2 的质疑也有道理：formality 和 verbosity 恰好是改写后 content preservation 最容易通过 NLI gate 验证的轴（相比 humor, creativity, hedging 等更 subtle 的风格维度）。如果 CSD 只能在 NLI-gate-friendly 的风格轴上工作，其 generalizability 受到限制。论文应明确讨论这一 selection constraint。

**[AGREE] R2-Q2: GEE exchangeable correlation 的选择依据？**

同意这是一个需要回答的问题，与我 R1-Q4 一致。论文 Appendix D 提到了 correlation structure 但未报告对 AR(1) 或 unstructured 的 sensitivity analysis。鉴于论文使用 robust sandwich SE（对 correlation misspecification 提供一定保护），这一问题的实际影响可能有限，但应明确报告。

**[AGREE] R2-Q3: DeBERTa NLI 的系统性偏差和 direction-aware gating 引入的方向偏差。**

这是我未在 R1 中充分关注的重要问题。DeBERTa-v3-large on MNLI 可能对特定类型的 entailment 有系统性偏好（如倾向于认为 formal 文本 entail casual 文本但反之不然），这会导致 NLI gate 对不同 style direction 的通过率不对称——而 Table 6-7（Appendix G）确实显示 direction-aware gating 对 verbosity 增加了 21 pairs（32%），这些额外 pairs 的 effect size 是否与原有 pairs 一致需要验证。论文应报告 gate-admitted vs. gate-rejected pairs 的 BT win probability 分布对比。

**[REBUT] R2-Q4: 4 个 target judges 均为 2024H2 模型，时间效度问题。**

部分不同意。时间效度是所有 LLM 实证研究的通病，不应作为本文的特定弱点。论文明确列出了模型版本（Section 3.4: GPT-4o 2024-08-06, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash），使其结果可被未来研究 replicate 和 compare。更重要的是，论文的贡献不仅是具体模型上的 empirical finding，更是 CSD 方法论——方法论的价值不依赖于特定模型的时效性。如果 R2 的意思是"未来模型可能修复了 Likert Blindspot"，这是一个合理的 future direction，但不应减分。

**[AGREE] R2-Q5: Likert 的 "failure" 可能部分是样本量不足的 artifact。**

这是我认为全文最关键的未解决问题，与我 R1-Q3 一致。Appendix K (Table 12) 的 formal power analysis 显示 Likert 达到 80% power 需要 n=1,473 至 n=18,157。这意味着在 n=88 下，Likert 根本无法检测到任何合理大小的 style effect——无论 effect 是否存在。

如果在 n=1,500 下 Likert 也能检测到 style sensitivity（只是效应量更小），那么 pairwise 和 Likert 之间的差异仅是 sensitivity magnitude 的量化差异，而非定性的"Blindspot"。论文的 100-point continuous Likert 实验（Appendix O）试图排除 granularity 解释，但仅在 Qwen3-32B 上测试（我的 R1-W6）。

这一问题直接影响论文的核心 claim 层级：如果 Blindspot 仅是 power artifact，论文贡献降级为"量化 pairwise 和 Likert 的 sensitivity 比率"（仍有价值但 excitement 下降）；如果 Blindspot 是 construct-level 差异（两种模式测量不同 construct），贡献显著更大。论文目前未能 decisive 地区分这两种解释。

---

### Missing References

[AGREE] R2 建议的三个引用方向（IRT: Embretson & Reise 2000; ICC: Koo & Li 2016; WMT 转变: Bojar et al. 2016）均有价值。特别是 IRT 文献可以为 Likert scale 的 item information function 分析提供理论框架——如果 style dimension 上的 item information 在 Likert 格式下接近零，这将为 Blindspot 提供测量理论层面的解释。Bojar et al. (2016) 的 WMT pairwise→rating 转变经验也与论文的核心发现直接相关。

---

### 综合评估

R2 的审稿与我 R1 在多个关键问题上高度一致：negative control underpowered（R2-W2 ≈ R1-W2）、Blindspot 可能仅是 power artifact（R2-Q5 ≈ R1-Q3）、terminology 和 framing 问题（R2-W6/W8 ≈ R1-W8）。R2 的独特贡献在于：(1) 指出 "systematic" claim 与仅 2 个主轴的矛盾（W1）；(2) construct divergence 发展不足的结构性批评（W4）；(3) NLI model 自身 bias 的问题（Q3）。这些是我 R1 未充分覆盖的有效批评。

两位 Reviewer 的共同 concern 汇聚于同一核心问题：**论文是否充分 establish 了 Likert Blindspot 是 measurement-mode 的本质差异而非 power artifact + content confound 的组合效应？** 在 W1（NLI gate validation 不足）、W2（negative control underpowered）、Q5（Likert failure 可能是 power artifact）这三个问题未得到充分 address 之前，3.5 (Borderline Conference) 的评分是合理的。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 8 个 Weakness 和 5 个 Question 逐条标注了 [AGREE] 或 [REBUT]：

- **6 个 [AGREE]**：W1（systematic claim 过窄）、W2（TOST underpowered）、W4（construct divergence 不足）、W6（title bias）、W8（术语混用）、Q1/Q2/Q3/Q5
- **3 个 [REBUT]**：W3（Blindspot 有独立实践价值，非纯粹包装）、W5（post-hoc 不等于无效，问题在于"confirms"措辞过强）、W7（Table 1 密度在 8 页限制下合理）、Q4（时间效度是通病不应特别扣分）

两位 Reviewer 的核心 concern 高度一致：论文未能 decisive 地区分 Likert Blindspot 是 measurement-mode 本质差异还是 power artifact + content confound 的组合效应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1332 · 2026-05-23T07:00:17.892766+00:00_

审稿流程已完成。R1 对 R2 的详细交叉回应已收齐。

**交叉回应补充记录**（报告已提交，以下为 R1 交叉回应中的额外分歧点，不影响整体评分和 Must-Fix 判定）：

| R2 观点 | R1 回应 | 说明 |
|---------|---------|------|
| W3: Novelty 被过度包装，GEE 被 undersold | **[REBUT]** | R1 认为 Blindspot 有独立实践价值（practitioner 直接可操作），但同意 Thurstone 增量需更清晰 |
| W5: Severity spectrum 为 post-hoc | **[REBUT]** | R1 认为 post-hoc ≠ invalid，问题在于 "confirms" 措辞过强，应改为 "is consistent with" |
| W7: Table 1 信息密度过高 | **[REBUT]** | R1 认为 8 页限制下合理，建议改善 formatting 而非拆分 |
| Q4: 时间效度问题 | **[REBUT]** | R1 认为这是所有 LLM 实证研究通病，不应作为本文特定弱点 |

**两位 Reviewer 最终共识核心**：论文未能决定性地区分 Likert Blindspot 是 measurement-mode 本质差异还是 power artifact + content confound 的组合效应。MF1（NLI gate 验证）+ MF2（negative control TOST）+ MF3（claim scope）是接收的主要障碍。

**Overall: 3.5 (Borderline Conference)**，修复三个 Must-Fix 后有望提升至 4.0 (Conference)。

报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 128

## Round 128

58 recorded events


### User

_source line 1333 · 2026-05-23T08:48:47.222539+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-23T08:48:58.360660+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-23T08:48:58.411548+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-23T08:49:08.905918+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-23T08:49:09.157425+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-23T08:49:12.574210+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-23T08:49:13.880655+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-23 01:30 UTC\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 近期完成\n\n### 紧急任务批次（6/6 完成或确认）\n- **任务1 — NLI 选择偏差扩展** ✅: formality 全 NS，verbosity 长度选择 p=0.003（保守方向）\n- **任务2 — DA-gate 21 对质量** ✅: 5/5 judges Likert diff 均 NS，可安全纳入\n- **任务3 — Claude cross-benchmark** ✅: AEval×form BT=0.840 Blindspot=true; AEval×verb BT=0.750 Style OR=4.76; MTB×form BT=0.854\n- **任务4a — Cross-benchmark local** ✅: AEval×Llama BT=0.775 NO Blindspot; MTB×Qwen BT=0.700 NO Blindspot\n- **任务5 — 标注扩展数据** ✅: 100 pairs template 拉到本地\n- **任务6 — Construct divergence** ✅: formality rewrite 后 Likert acc 100%→40%\n\n### Bug 修复（3/3）\n- **GEE Style==Orig** ✅: 数据共线性（非代码 bug），cross_benchmark_analysis.py 统计方法已修复\n- **Claude pipeline** ✅: 新建 claude_crossbenchmark_scoring.py，3 配置跑通\n- **数据差异 MTB×Qwen** ✅: Table 1 正确，差异来自 NLI 过滤/方法不一致\n\n## ⚠️ 关键发现\n- Claude 在 LLMBar 是有效 negative control (BT≈55%, NS)，但 AEval/MTB 上有强偏差 (BT 75-85%)\n- Director 决策：negative control 限定 LLMBar only，cross-benchmark 数据转为新发现\n- 合并 TOST 不报告\n\n## 原始 TOST 确认\nRegistry `claude_tost_equivalence` 不受影响：formality p̂=0.562 n=88, verbosity p̂=0.541 n=86\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n1. 等 Director 确认 task 4b (GPT-4o cross-benchmark) 是否仍需\n2. 等 Paper Agent 完成写作修改\n3. 等标注员回复\n\n## 资源状态\nwestb-29275: 4×RTX PR
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-23T08:49:13.881103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-23T08:49:14.132490+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inherent in the format.
…[truncated 5114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-23T08:49:22.416028+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1343 · 2026-05-23T08:49:22.466665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-23T08:49:26.784483+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1345 · 2026-05-23T08:49:28.944342+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1346 · 2026-05-23T08:49:29.346534+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1347 · 2026-05-23T08:49:29.598004+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1348 · 2026-05-23T08:49:29.648634+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-23T08:49:38.387279+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 through ARR:

## Paper Types and Content

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. Author response 
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 11602
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-23T08:49:44.875455+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-23T08:49:45.678909+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-23T08:49:45.679395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference papers page limit format template double blind site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference papers page limit format template double blind site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-23T08:49:53.199496+00:00_

Web search results for query: "EMNLP 2026 main conference papers page limit format template double blind site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Based on the search results from the EMNLP 2026 official website, I found information about the main conference papers and the double-blind review process. However, the search results don't contain specific details about page limits, format templates, or formatting specifications for the main conference papers.

Here's what I found:

**Double-Blind Review:**
The reviewing process will be double-blind, with reviewers not seeing authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible.

**Paper Types:**
Both long and short paper submissions should follow all of the ARR submission requirements.

However, the search results don't include the specific page limits, format template links, or detailed formatting requirements for main conference papers. To find this information, you would likely need to:

1. Check the ARR (A
…[truncated 635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7520
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-23T08:50:00.885340+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission requirements page limit long paper short paper format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission requirements page limit long paper short paper format"
  }
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-23T08:50:01.889400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-23T08:50:02.341334+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce consistently divergent sensitivity across tested surface-level style axes when applied to LLM judges.
3	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic methodology that quantifies this divergence under controlled conditions via human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
4	Across four judges from independent providers, one low-sensitivity reference, and two primary axes (formality, verbosity), the divergence is robust: pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\% at stronger effects---replicated across three benchmarks and confirmed by seven statistical methods.
5	GEE conditional decomposition reveals qualitatively distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects a conditional effect where style and content quality contribute jointly---determining which pairwise estimates are directly interpretable and which require decomposition.
6	A low-sensitivity reference judge shows substantially weaker divergence on both primary axes (BT 55\% vs.\ 63--77\%), supporting discriminative validity.
7	This divergence admits three non-exclusive explanations---measurement attenuation, format amplification, or construct divergence---that our controlled design bounds but cannot definitively adjudicate; the practical consequence is unambiguous: Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-23T08:50:02.391955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-23T08:50:02.743697+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}---an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations---Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences between absolute and comparative evaluation---which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	Under construct divergence, pairwise and Likert modes may measure distinct constructs---comparative sensitivity versus absolute quality judgment---in which case the divergence reflects measurement scope rather than measurement failure, with different practical implications for audit design (\S\ref{sec:likert_pairwise}).
8	This example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
9	
10	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
11	Despite this, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \cit
…[truncated 3681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-23T08:50:02.744060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1360 · 2026-05-23T08:50:02.794527+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	Whether this format sensitivity extends to RATE's broader attribute space is an open question; our results motivate independent validation of Likert-based effect estimates alongside pairwise measures.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control r
…[truncated 6499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-23T08:50:07.263010+00:00_

Web search results for query: "ACL Rolling Review 2026 submission requirements page limit long paper short paper format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here are the ACL Rolling Review 2026 submission requirements for page limits and paper formats:

## Paper Types

ACL Rolling Review invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Page Limits

**Long Papers:**
Review versions of long papers may have up to eight (8) pages
…[truncated 1097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6377
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-23T08:50:13.389974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-23T08:50:14.243935+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
12	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on MNLI \citep{williams2018broad} with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exc
…[truncated 5426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-23T08:50:14.244352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-23T08:50:14.796892+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests---three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) $\times$ two axes (formality, verbosity)---corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	
17	\paragraph{Model selection.}
18	Target judges span four architectures: GPT-4o (2024-08-06), Qwen3-32B-Instruct (also serving as rewriter), Llama-3.3-70B-Instruct, 
…[truncated 15637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-23T08:50:14.797359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-23T08:50:15.199124+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: pairwise comparison and Likert scoring produce consistently divergent verdicts---complete divergence at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed across four judges, three benchmarks, and seven statistical methods.
6	Second, GEE conditional decomposition reveals qualitatively distinct per-axis confound structures---verbosity is style-dominated, formality is a conditional effect, register is judge-dependent---disambiguating cases where aggregate preference reflects quality detection rather than style sensitivity.
7	Regardless of mechanism, single-format audits risk systematic blind spots; human ground-truth validation of both modes is the key next step.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-23T08:50:15.199478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-23T08:50:15.250090+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\label{app:direction}
18	
19	The formality axis exhibits a pronounced 
…[truncated 10770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-23T08:50:21.727510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-23T08:50:22.280674+00:00_

200	.80 & .657 & .623 & .773 & .760 \\
201	.85 & .657 & .623 & .773 & .760 \\
202	.90 & .665 & .630 & .773 & .760 \\
203	.95 & .653 & .629 & .765 & .752 \\
204	.98 & .649 & .642 & .771 & .769 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\section{Direction-Aware Gate Validation}
210	\label{app:gate_validation}
211	
212	For verbosity, the direction-aware NLI gate admits 21 additional pairs (32\%) compared to strict bidirectional verification.
213	The two groups show no significant difference in BT win probability (78.5\% bidirectional vs.\ 73.8\% DA-only; permutation $p = .663$; $\Delta = {-}1.1$pp, 95\% CI $[{-}5.6, {+}3.0]$) or Likert $d$ ($0.038$ vs.\ $0.029$).
214	Both groups exhibit the Blindspot pattern (BT significant, Likert NS), confirming that direction-aware gating recovers valid pairs without inflating the effect or introducing selection bias.
215	Cross-judge validation on all 21 direction-aware pairs confirms this: Fisher exact tests comparing BT estimates between direction-aware and bidirectional-pass subsets are non-significant for all five judges ($p > 0.66$), indicating that the DA-gate does not differentially affect any judge's preference signal.
216	For formality, strict bidirectional verification is appropriate: a relaxed (direction-aware) gate would admit 9 additional pairs with reversed preference (BT 33.4\%), indicating content preservation failure rather than genuine style preference.
217	This asymmetry empirically justifies the axis-dependent gating strategy described in Section~\ref{sec:nli_gate}.
218	
219	\section{Claude Sonnet 4 Equivalence Testing}
220	\label{app:claude_tost}
221	
222	Claude Sonnet 4 serves as low-sensitivity reference ($n = 88$; BT 56.2\%/54.1\%, $p = 0.091$/$0.284$).
223	Formal equivalence testing \citep[TOST;][]{lakens2017equivalence} yields margin-dependent conclusions (Table~\ref{tab:tost_sensitivity}): per-axis equivalence is confirmed at $\Delta = 15$pp ($p = .010$), corresponding to a BT threshold 
…[truncated 14678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-23T08:50:22.582263+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-23T08:50:22.633051+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 78\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-23T08:50:35.239152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "499",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "499",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-23T08:50:35.792457+00:00_

499	Verb.\ & GPT-4o & .167 [.084, .262] & ${<}.0001$ \\
500	 & Qwen3 & .082 [.035, .140] & ${<}.0001$ \\
501	\bottomrule
502	\end{tabular}
503	\end{table}
504	
505	\section{Implementation Details}
506	\label{app:implementation}
507	
508	\paragraph{Models and APIs.}
509	Style-controlled rewriting uses Qwen3-32B (temperature $0.7$, top-$p$ $0.9$).
510	Target judges: GPT-4o (\texttt{gpt-4o-2024-08-06}, accessed April--May 2026), Qwen3-32B (locally hosted), Llama-3.3-70B (locally hosted via vLLM).
511	Low-sensitivity reference: Claude Sonnet 4 (\texttt{claude-sonnet-4-20250514}, accessed May 2026).
512	All judge calls use temperature $0$ and $\texttt{max\_tokens} = 2048$.
513	
514	\paragraph{NLI gate.}
515	Content preservation is verified using DeBERTa-v3-large \citep{he2021debertav3} fine-tuned on MNLI, with entailment threshold $\tau = 0.90$.
516	Bidirectional entailment is applied for formality and register; direction-aware entailment for verbosity (Section~\ref{sec:nli_gate}).
517	
518	\paragraph{Statistical methods.}
519	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm} using the \texttt{choix} Python library (default regularization).
520	All bootstrap CIs use 10{,}000 pair-level resamples with seed $42$.
521	GEE models use exchangeable working correlation with robust (sandwich) standard errors via \texttt{statsmodels} (Section~\ref{sec:direction}; diagnostics in Appendix~\ref{app:gee_diagnostics}).
522	
523	\paragraph{Benchmarks.}
524	LLMBar \citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).
525	AlpacaEval \citep{dubois2025lc}: 100 sampled pairs.
526	MT-Bench \citep{zheng2023judging}: 80 multi-turn pairs.
527	
528	\paragraph{Code and data.}
529	All code, prompts, and experimental data will be released upon acceptance under an open-source license.
530	
531	\section{Holm-Bonferroni Sensitivity Analysis}
532	\label{app:holm8}
53
…[truncated 13870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-23T08:50:36.194336+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-23T08:50:36.245047+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-23T08:50:55.676917+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 1379 · 2026-05-23T08:50:57.734078+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "review_issues",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "review_issues",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 1380 · 2026-05-23T08:50:59.245021+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3568
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-23T08:50:59.295715+00:00_

Found 4 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T052420/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T052420/logs/review_median.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Grep",
  "elapsed_ms": 1561
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-23T08:51:08.586064+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-23T08:51:08.737575+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-23T08:51:11.851630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-23T08:51:11.952821+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 16
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。"
44	      - round: 13
45	        reviewers: [1, 2]
46	        note: "R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。"
47	      - round: 14
48	        reviewers: [1, 2]
49	        note: "R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。"
50	      - round: 15
51	        reviewers: [1, 2]
52	        note: "R15 fresh review: 两位再次独立提出。"
53	      - round: 16
54	        reviewers: [1, 2]
55	        note: "R16: S4 称 GEE decomposition 是'真正的方法论
…[truncated 17186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-23T08:51:51.170482+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性、统计框架、实验设计**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references。Limitations 不计页。\n- **模板**: ACL template（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf\n\n## EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面，按优先级排列：\n\n1. **因果推断框架**：CSD 声称提供 interventional evidence——NLI gate 是否真正阻断了 R→Q 路径？DAG 假设是否合理？残余混淆的处理是否充分？\n2. **统计方法**：Bradley-Terry 模型的 IIA 假设是否成立？GEE exchangeable correlation 的选择是否有诊断支持？Holm-Bonferroni 校正的 family 定义是否合理（6 vs 8 tests）？TOST 等价性检验的 margin 选择是否有独立依据？\n3. **实验设计**：NLI gate 的 precision/recall tradeoff 是否产生选择偏差？n=88 的样本量下 GEE OR 估计的可靠性？n=88→n=355 的 49% OR 缩水如何影响主要结论？Cross-benchmark replication 的 benchmark 选择是否存在偏差？\n4. **Evaluator-producer overlap**：Qwen3-32B 同时作为 rewriter 和 judge 的混淆控制——22% OR 降幅意味着什么？仅一个替代 rewriter 是否足够？\n5. **Negative control / Low-sensitivity reference**：Claude Sonnet 4 作为 low-sensitivity reference 的证据链是否充分？TOST underpowered、Bayesian BF inconclusive、AEval verbosity Style OR=4.76——这些矛盾如何调和？\n6. **Cross-axis contamination**：FK grade d=0.50 的处理是否令人信服？Length-controlled GEE 是否真正解决了问题？\n\n请给出完整审稿报告，包含 Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Overall Assessment（评分 + 置信度）。",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性、统计框架、实验设计**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references。Limitations 不计页。\n- **模板**: ACL template（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf\n\n## EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面，按优先级排列：\n\n1. **因果推断框架**：CSD 声称提供 interventional evidence——NLI gate 是否真正阻断了 R→Q 路径？DAG 假设是否合理？残余混淆的处理是否充分？\n2. **统计方法**：Bradley-Terry 模型的 IIA 假设是否成立？GEE exchangeable correlation 的选择是否有诊断支持？Holm-Bonferroni 校正的 family 定义是否合理（6 vs 8 tests）？TOST 等价性检验的 margin 选择是否有独立依据？\n3. **实验设计**：NLI gate 的 precision/recall tradeoff 是否产生选择偏差？n=88 的样本量下 GEE OR 估计的可靠性？n=88→n=355 的 49% OR 缩水如何影响主要结论？Cross-benchmark replication 的 benchmark 选择是否存在偏差？\n4. **Evaluator-producer overlap**：Qwen3-32B 同时作为 rewriter 和 judge 的混淆控制——22% OR 降幅意味着什么？仅一个替代 rewriter 是否足够？\n5. **Negative control / Low-sensitivity reference**：Claude Sonnet 4 作为 low-sensitivity reference 的证据链是否充分？TOST underpowered、Bayesian BF inconclusive、AEval verbosity Style OR=4.76——这些矛盾如何调和？\n6. **Cross-axis contamination**：FK grade d=0.50 的处理是否令人信服？Length-controlled GEE 是否真正解决了问题？\n\n请给出完整审稿报告，包含 Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Overall Assessment（评分 + 置信度）。",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-23T08:52:09.135910+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17965
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-23T08:52:09.337133+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性、写作质量、Related Work**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references。Limitations 不计页。\n- **模板**: ACL template（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf\n\n## EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面，按优先级排列：\n\n1. **新颖性评估**：Likert Blindspot 是 Thurstone (1927) 以来心理测量学已知的 measurement sensitivity gap 在 LLM judge 领域的 domain transfer。论文声称的 3 个 LLM-specific distinctions（per-axis structure、GEE source decomposition、binary divergence pattern）是否构成足够的增量贡献？GEE conditional decomposition 是否是真正的方法论创新？与 RATE (Reber et al., 2025)、CASSE (2026)、FairJudge (2026) 的差异化是否清晰？\n2. **Claims vs Evidence 对齐**：Abstract/Intro 的 claims 是否被实验充分支撑？\"consistently divergent\" 基于 2 个轴 + 1 个 exploratory 轴是否过强？\"across four judges\" 是否遗漏了 Gemini 的较弱效应？Title \"Blindspot\" 是否预设了 Likert attenuation 解释而忽视了 construct divergence/pairwise amplification？\n3. **写作质量**：信息密度是否合理（8 页正文承载 4 judges × 3 axes × 3 benchmarks + GEE + TOST + Bayesian 的复杂设计）？叙事流是否清晰？术语一致性？图表设计是否有效传达关键发现？\n4. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注 2025-2026 年的 LLM judge bias 工作、measurement theory 工作、interventional text analysis 工作。引用是否真实（非幻觉）？\n5. **Limitations 章节**：是否充分讨论了关键局限？是否存在未提及的重要限制？\n6. **格式合规**：是否符合 EMNLP 2026 / ARR 的格式要求？匿名是否到位？页数是否合规？\n\n请给出完整审稿报告，包含 Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性、写作质量、Related Work**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: ARR Long Paper\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限 references。Limitations 不计页。\n- **模板**: ACL template（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf\n\n## EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n重点审查以下方面，按优先级排列：\n\n1. **新颖性评估**：Likert Blindspot 是 Thurstone (1927) 以来心理测量学已知的 measurement sensitivity gap 在 LLM judge 领域的 domain transfer。论文声称的 3 个 LLM-specific distinctions（per-axis structure、GEE source decomposition、binary divergence pattern）是否构成足够的增量贡献？GEE conditional decomposition 是否是真正的方法论创新？与 RATE (Reber et al., 2025)、CASSE (2026)、FairJudge (2026) 的差异化是否清晰？\n2. **Claims vs Evidence 对齐**：Abstract/Intro 的 claims 是否被实验充分支撑？\"consistently divergent\" 基于 2 个轴 + 1 个 exploratory 轴是否过强？\"across four judges\" 是否遗漏了 Gemini 的较弱效应？Title \"Blindspot\" 是否预设了 Likert attenuation 解释而忽视了 construct divergence/pairwise amplification？\n3. **写作质量**：信息密度是否合理（8 页正文承载 4 judges × 3 axes × 3 benchmarks + GEE + TOST + Bayesian 的复杂设计）？叙事流是否清晰？术语一致性？图表设计是否有效传达关键发现？\n4. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注 2025-2026 年的 LLM judge bias 工作、measurement theory 工作、interventional text analysis 工作。引用是否真实（非幻觉）？\n5. **Limitations 章节**：是否充分讨论了关键局限？是否存在未提及的重要限制？\n6. **格式合规**：是否符合 EMNLP 2026 / ARR 的格式要求？匿名是否到位？页数是否合规？\n\n请给出完整审稿报告，包含 Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-23T08:52:10.746475+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 1390 · 2026-05-23T08:52:15.860207+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法/实验/统计）→ 已启动
- **Reviewer 2**（新颖性/写作/完整性）→ 已启动
- **视觉审查 Agent** → 已派发（fire-and-forget）
- **外部审稿** → 未配置，跳过

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1391 · 2026-05-23T08:57:37.898127+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5 (Quite sure)
**一句话总结**: 核心发现（Likert Blindspot）在四个 judge、三个 benchmark 上有可靠复现，GEE 条件分解是真正的方法论贡献；但因果推断框架的 identifiability 上限、小样本 OR 膨胀对定量结论的系统性影响、以及 Claude 负对照的内部矛盾，使得定量主张的可信度低于定性结论。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 核心定性发现（Blindspot 存在）有充分支撑；但定量 OR 估计受小样本偏差系统性影响（n=88→n=355 缩水 49%），formality 对 GPT-4o 的 Style OR 在控制 FK grade 后失去显著性（p=.132），Claude 负对照证据链内部矛盾 |
| Excitement | 3.5 / 5 | 问题重要且及时——Likert vs pairwise 的 sensitivity gap 对 RLHF/DPO pipeline 有直接实践意义；GEE per-axis decomposition 是该领域的方法论推进；但 construct divergence vs attenuation 的 adjudication 留给了未来工作 |
| Reproducibility | 4 / 5 | 实验细节充分（模型版本、温度、种子、bootstrap 次数），统计方法有完整规范，prompts 在 Appendix V 公开；代码数据承诺 acceptance 后释放 |

---

## 主要优势

**S1. 核心发现扎实且具有实践意义。** Likert Blindspot 在 4 个来自独立提供商的 judge（GPT-4o、Qwen3-32B、Llama-3.3-70B、Gemini-2.5-Flash）× 2 个主轴（formality、verbosity）× 3 个 benchmark 上复现，且 n=355 scaled replication 证实 Likert d→0 是结构性衰减而非 power 不足（Table 1, Appendix K）。七种统计方法的一致性（Table 4/Appendix L）排除了 test-specific artifact。这对依赖 Likert ATE 的 RATE 等框架有直接校正意义。

**S2. GEE 条件分解是真正的方法论贡献。** 将 aggregate BT preference 拆解为 Style OR 和 Originality OR（Table 2）揭示了 per-axis 质性差异（verbosity style-dominated OR 8–13, formality conditional），这在该领域是新的诊断层。Claude 在 AEval 的 case（aggregate BT ~70% 但 Style OR n.s., Orig OR 9–12）很好地说明了为什么 aggregate BT 本身不足以归因 bias（Appendix U, Table 8）。

**S3. 实验设计的 transparency 和 self-correction 罕见地好。** n=355 replication 主动暴露 49% OR 缩水并讨论 small-sample bias（Section 5.2, Table 2 footnote）；三种 Blindspot 解释（attenuation / amplification / construct divergence）的 agnostic framing（Section 5.1）避免了过度 claim；100-pair human annotation（Appendix S, AC₁=0.96）和 NLI threshold sweep（Appendix E, ≤3pp variation）提供了 pipeline robustness 的实证。

**S4. 对 related work 的定位准确且诚实。** 对 RATE 的分析（Section 2, "reliance on Likert ATE as the primary metric is a vulnerability"）基于实证而非稻草人；对 Comparative Trap (Jeong et al., 2025) 的直接回应（Section 5.4, 六项 amplification controls）承认了 format amplification 的可能性。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 小样本 OR 膨胀对主要定量结论的系统性影响未充分传播
- 具体位置：Table 2 (GEE decomposition), Section 5.2
- 问题：n=88→n=355 的 Qwen3-32B formality Style OR 从 4.20 缩水至 2.15（-49%），论文归因于 small-sample upward bias (Nemes et al., 2009)，这是合理的。但 Table 2 中其他 11 个 n=88 cell 的 OR 很可能受到类似程度的膨胀，却以 face value 呈现。例如 verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5——论文在 Section 5.2 做了文字推演（"would remain style-dominated even under ~50% shrinkage"）但未提供 shrinkage-adjusted 估计或 uncertainty propagation。读者看到 Table 2 的 OR=13.10 时会高估真实效应量。
- 为什么影响接收：GEE decomposition 是论文的核心方法论贡献（Contribution 2），如果主要表格的定量估计系统性偏高 ~50%，regime classification 虽然可能不变（"style-dominated" vs "conditional"），但效应量的可信度和跨 judge 比较的解释都受影响。
- 建议修改方向：(a) 在 Table 2 旁或 footnote 中给出 shrinkage-adjusted projected ORs（至少对 verbosity 的 4 个 cell）；(b) 在正文明确声明所有 n=88 OR 应被视为上界估计。

**N2** [critical] GPT-4o formality Style OR 在控制 FK grade 后失去显著性
- 具体位置：Appendix R' (FK Length-Control Analysis), 最后一段
- 问题：添加 FK grade change 作为 GEE 协变量后，GPT-4o formality Style OR 从 2.70 降至 2.15（p=.132, 不再显著）。虽然 Qwen3-32B（3.38, p=.014）和 Llama-70B（2.69, p=.037）仍然显著，但 GPT-4o 是论文中最突出的 judge（Introduction 的 opening example, Table 1 第一行, 所有 main-text 讨论的首选 judge）。这意味着 GPT-4o 的 formality "style bias" 可能部分或全部由 readability 差异解释。
- 为什么影响接收：GPT-4o 是论文叙事的锚点 judge。如果其 formality effect 在一个合理的 robustness check 中失去显著性，读者对整个 formality finding 的信心会下降——尽管其他两个 judge 仍然显著。当前处理方式是将此结果放在 Appendix 中一段话带过（"Two of three judges retain significant formality effects after readability control"），不够透明。
- 建议修改方向：(a) 在正文 Section 5.2 或 5.3 中明确提及 FK-controlled 结果对 GPT-4o 的影响；(b) 讨论这对 formality 作为 "conditional effect" 分类的含义——如果 readability 是 mediator 而非 confounder，控制 FK 是 over-controlling（bad control problem），但需要提出论据。

**N3** [critical] Claude "low-sensitivity reference" 的证据链存在内部矛盾
- 具体位置：Section 5.1 (四条 convergent evidence), Appendix G (TOST), Appendix U (Table 8, AEval verbosity)
- 问题：四条证据线没有一条单独成立——(i) TOST 在 Δ=10pp 时 underpowered（power ~42%）且不显著；(ii) GEE Style OR 在 LLMBar n.s. 但不能排除 small effect（MDE=1.56 at 80% power 意味着 Claude 的 OR 可能高达 1.56 而检测不到）；(iii) GPT-4o contrast 是间接证据；(iv) Bayesian BF₀₁=0.80 明确 inconclusive。更致命的是，AEval verbosity 上 Claude Style OR=4.76（p<.001），这是一个 style-dominated pattern——与 "low-sensitivity reference" 标签直接矛盾。论文承认 "verbosity sensitivity is benchmark-dependent"（Limitations），但在正文 Section 5.4 仍将 Claude 列为六项 amplification control 之一（"(ii) Claude low-sensitivity reference (Style OR n.s.)"），这里的 "n.s." 仅指 LLMBar formality，选择性引用了最有利的结果。
- 为什么影响接收：Claude 作为 negative control 是论文区分 detection vs amplification 的关键证据之一。如果 negative control 本身在某些配置上是 bias-positive 的（OR=4.76），且 equivalence testing 在理论上 inconclusive，discriminative validity 的 claim 被削弱。
- 建议修改方向：(a) 将 Claude 降级为 "lower-sensitivity judge"（relative rather than absolute reference），明确说明这是 benchmark-dependent 的；(b) 在 Section 5.4 的六项 controls 中更新 Claude 的描述，不能仅说 "Style OR n.s." 而忽略 AEval verbosity；(c) 考虑在正文中讨论 AEval verbosity OR=4.76 如何影响 Claude 作为 reference 的解释。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Evaluator-producer overlap 仅用一个替代 rewriter 验证
- 具体位置：Appendix D (Rewriter Independence), Tables 6–7
- 问题：Qwen3-32B 同时作为 rewriter 和 judge 的 overlap 仅用 GPT-4o 作为替代 rewriter 进行了验证（verbosity: Style OR 降 22%; formality: BT -2.1pp）。但 GPT-4o 也是 instruction-tuned LLM，可能与 Qwen3-32B 共享 RLHF 训练中习得的 style preferences（Limitations 中承认 "all alternative rewriters are instruction-tuned LLMs that may share style preferences"）。一个 rule-based rewriter（如基于同义词替换的 formality transform）或人类 rewriter 能更可靠地 bound evaluator-producer bias。此外，替代 rewriter 的 formality 实验未报告 GEE decomposition（Table 7 只报告了 BT 和 Likert），无法验证 Style OR vs Orig OR 的 regime classification 是否在替代 rewriter 下保持一致。
- 建议：(a) 补充 formality 替代 rewriter 的 GEE 分解；(b) 至少讨论为什么没有使用 rule-based rewriter 以及这如何限制 22% bound 的解释。

**W2** [warning] Cross-benchmark replication 是选择性的，不是完整 grid
- 具体位置：Table 6 (Appendix T)
- 问题：Cross-benchmark 仅测试了 "targeting the strongest effects from the primary LLMBar analysis"（Appendix T 原文）——这是 effect-magnitude selection，可能导致 replication 结果向上偏倚。完整的 4 judges × 2 axes × 3 benchmarks = 24 cells 只填了 6 个（25%），且选择了最强的 cell。LLMBar verbosity 在 AEval 上显示 Qwen3 BT=84.1%（Table 6），是所有 cell 中最高的——如果弱 cell（如 Gemini formality, BT=57.4%）在 AEval/MTB 上不 replicate，Blindspot 的 generalizability claim 需要 qualify。
- 建议：补充至少一个"弱信号" cell 的 cross-benchmark replication（如 Gemini formality），或明确声明 replication 仅覆盖强信号 cell。

**W3** [warning] TOST equivalence margin 缺乏独立依据
- 具体位置：Section 5.1, Appendix G (Table 5)
- 问题：论文测试了 5 个 TOST margin（Δ=5, 10, 12, 15, 20pp）并报告了所有结果——这种 transparency 值得肯定。但没有一个 margin 有先验的独立 justification。Δ=10pp 对应 BT=60%，Δ=15pp 对应 BT=65%——什么 practical significance threshold 决定了 "low sensitivity"？如果 Δ=15pp 是 acceptable（论文在此处达到 equivalence），那么 BT=65% 的 judge 就是 "low-sensitivity" 的——但 Gemini formality BT=57.4% 也在这个范围内。缺乏 margin 的独立依据使得 TOST 结果的解释力有限。
- 建议：提供 practical significance 的论据——例如基于 RLHF reward signal 的 downstream impact（BT 每增加 X pp，reward model 偏差增加 Y%），或引用领域内对 "practically meaningful bias" 的 existing consensus。

**W4** [warning] 因果语言在正文中不够一致
- 具体位置：Section 3.5 vs Introduction vs Abstract
- 问题：Section 3.5 和 Appendix A 明确声明 "Our approach provides interventional rather than formal causal evidence" 和 "we do not claim that the DAG...is a complete structural causal model"——这是恰当的 hedging。但 Introduction 中 "inspired by interventional text analysis (Veitch et al., 2020)" 和 Method 中 "Each operation constitutes a binary intervention on a single style variable"（Section 3.1）暗示了更强的因果 claim。Abstract 的 "NLI-gated content control" 在没有 qualification 的情况下可能让读者认为 confounding 已被完全阻断。
- 建议：在 Section 3.1 中将 "constitutes a binary intervention" 改为 "approximates a binary intervention"；在 Abstract 中添加 qualification（如 "approximate content control"）。

---

## 小问题（不影响接收）

- **M1**: Table 1 的 "n=88 except where noted" 实际上 verbosity 是 n=86（Appendix L, Table 9 标题："n=86 NLI-filtered pairs"），正文和表格应统一。
- **M2**: Introduction 中 GPT-4o 的 opening example（"rates the casual variant higher on a 1–10 Likert scale (8 vs 5)"）是单个 cherry-picked instance。虽然有 pedagogical value，但应注明这是说明性个例而非系统性发现的代表。
- **M3**: Figure 2 (DAG) 中 S→Q 的 "residual confound." label 使用了 orange 虚线，但在黑白打印时可能与其他虚线混淆。建议增加 label 或使用不同的 line pattern。
- **M4**: Appendix Table 3 中 QIC 值全部显示为 "---"，没有提供实际数值，只报告了差值 "<0.001"。建议至少报告一个 representative cell 的绝对 QIC。
- **M5**: BT model 使用 `choix` library 的 "default regularization"——没有说明具体 regularization 形式和强度。对于 n=88 的小样本，regularization 选择可能影响 BT 估计。

---

## Questions to Authors

**Q1**: n=88 的 GEE OR 在 n=355 时缩水 49%。如果对 verbosity 做同样的 scaled replication，预期 Style OR（当前 8–13）会缩水到多少？这会改变 style-dominated 的 regime classification 吗？

**Q2**: GPT-4o formality 在控制 FK grade 后 p=.132。你们是否认为 FK grade 是 mediator（控制它是 over-controlling）还是 confounder？如果是 mediator，请提供 DAG 层面的论据。

**Q3**: AEval verbosity 上 Claude Style OR=4.76（p<.001）。你们如何调和这与 "low-sensitivity reference" 的定位？是否考虑过对 Claude 在 AEval 上的行为提出替代解释（如 AEval 数据分布的特殊性）？

**Q4**: 在 direction-aware NLI gate 中，verbosity expansion 只检查 backward entailment（rewrite entails original）。但 expansion 引入的新内容本身可能改变 perceived quality——这条 R→Q 路径是否被 gate 漏过？

**Q5**: BT model 使用 `choix` library 的 default regularization。在 n=88 的小样本下，regularization prior 对 BT 估计有多大影响？是否做过 regularization sensitivity analysis？

---

## Overall Assessment

**3.5 (Borderline Conference)**

这篇论文提出了一个重要且实证支持充分的定性发现（Likert Blindspot），GEE per-axis decomposition 是该领域的真正方法论推进。实验设计的广度（4 judges × 3 benchmarks × 7 methods）和 self-correction 的透明度（n=355 OR shrinkage disclosure）明显高于该领域的平均水平。

阻碍给出 4 分（Conference）的主要原因：(1) 小样本 OR 膨胀（~50%）对 Table 2 中大部分定量估计的系统性影响未被充分传播到主要结论；(2) GPT-4o formality——论文叙事的锚点——在 FK readability control 下失去显著性；(3) Claude negative control 的证据链每一条单独都不成立，且 AEval verbosity OR=4.76 直接矛盾。这三个问题不影响核心定性发现（Blindspot 存在），但削弱了对效应量和机制归因的信心。

如果 authors 能 (a) 承认 n=88 OR 是上界估计并给出 projected ranges，(b) 在正文讨论 FK control 对 GPT-4o 的影响，(c) 降级 Claude 从 "low-sensitivity reference" 到 "relatively lower-sensitivity"，定量主张的可信度将显著提升，论文可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1392 · 2026-05-23T08:57:44.784467+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 的审稿意见后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1393 · 2026-05-23T08:57:52.147400+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。定性发现（Likert Blindspot）扎实，GEE per-axis decomposition 是真正的方法论贡献。三个 Must-Fix 问题阻碍给出 4 分：(1) n=88 的 GEE OR 系统性膨胀 ~50% 未传播到主要结论；(2) GPT-4o formality Style OR 在控制 FK readability 后失去显著性（p=.132）；(3) Claude 负对照在 AEval verbosity 上 Style OR=4.76（p<.001），与"low-sensitivity reference"标签矛盾。这些问题均可通过修改文字表述和补充分析解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1394 · 2026-05-23T08:57:57.501272+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 131

## Round 131

6 recorded events


### User

_source line 1395 · 2026-05-23T08:57:59.006091+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
**Venue**: EMNLP 2026 (ARR Long Paper)
**审查侧重**: 新颖性、完整性、写作质量、Related Work

---

## 总体评分
**Overall Assessment**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5 — Quite sure; I checked the important points carefully.
**一句话总结**: 执行质量出色的实证研究，但核心发现（pairwise 比 Likert 对风格更敏感）在心理测量学中已被充分确立，LLM-specific 的增量贡献虽然存在但不够显著，且无法区分 attenuation 和 amplification 这一根本限制削弱了实际指导价值。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 方法论严谨，六项实验控制、七种统计方法、跨 benchmark 复制，GEE 分解有诊断价值。但无法区分 attenuation 与 amplification（作者承认），且核心结论依赖 n=100 的 LLMBar 数据集。 |
| Excitement | 3 / 5 | 对 LLM 评估社区有实用价值，但核心 insight（pairwise > rating for sensitivity）是 Thurstone (1927) 以来的经典结论。GEE per-axis decomposition 是最具新意的部分，但属于标准统计工具的领域应用。 |
| Reproducibility | 4 / 5 | 方法描述详尽，统计框架清晰，附录提供模型参数和 prompt。承诺接收后释放代码和数据。 |
| Overall | 3.5 / 5 | Borderline Conference — 执行达到会议水准，但新颖性不足以明确推荐主会议。适合 Findings。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性定位不够诚实：核心发现是经典心理测量结论的领域迁移，三个 "LLM-specific distinctions" 的增量贡献被夸大

- 具体位置：Section 1 (Introduction), p2 第 13 段 "However, the LLM judge setting introduces distinctions beyond the classical framework: (a)...(b)...(c)..."
- 问题：论文声称的三个 LLM-specific distinctions 实际上并不构成对经典框架的本质超越：
  - **(a) Per-axis structure**：Thurstone 的框架本身就不预测所有刺激维度具有相同的 discriminability gradient。不同 style axis 展现不同的 confound structure 是实证发现，不是方法论创新。经典 IRT 文献中 item-level discriminability variation 是标准现象。
  - **(b) GEE source decomposition**：GEE (Liang & Zeger, 1986) 是成熟的纵向数据分析工具，将其应用于分解 style/quality 成分是合理的工程贡献，但不构成"absent from the classical framework"的方法论创新。经典心理测量中 factor analysis 和 structural equation modeling 长期承担类似功能。
  - **(c) Binary divergence pattern**：所有七种 Likert 方法全部失败、所有 pairwise 方法全部成功的二元分裂，更可能反映效应量位于 Likert 的检测阈值以下（即经典 power analysis 所预测的），而非超越经典理论的新现象。论文自己的 Figure 4 power analysis 完全一致地解释了这一模式。
- 为什么影响接收：这是论文新颖性论证的核心。如果三个 distinctions 都可以被经典框架解释，那么贡献就退化为"在 LLM judge 上验证了已知现象"，这对 EMNLP 主会议可能不够。
- 建议修改方向：更诚实地定位为"empirical characterization of a known phenomenon in a new domain"，突出 GEE per-axis decomposition 的实用价值（这确实是有用的诊断工具），而非过度宣称方法论新颖性。将 Introduction 的 framing 从"distinctions beyond the classical framework"改为"practical implications that the classical framework predicts but has not been quantified in the LLM setting"。

**N2** [critical] "Consistently divergent" claim 过强——基于 2 个主要轴 + 1 个 exploratory 轴，且 Gemini 效应显著弱于其他三个 judge

- 具体位置：Abstract 第 1 句 "consistently divergent sensitivity across tested surface-level style axes"；Section 5.3 (p6-8)
- 问题：
  - "consistently" 的证据基础是 2 个 primary axes（formality, verbosity）+ 1 个 exploratory axis（register）。其中 register 明确标注为 exploratory，且 evaluator-producer overlap 最高（Limitations, p9）。如果排除 register，结论基于 2 个轴，这对"consistently across axes"的概括力有限。
  - Gemini-2.5-Flash 的 formality 效应明显弱于其他三个 judge：Style OR 1.64 (n.s.)，BT 仅 57.4%（Table 1, Table 2）。Abstract 称 "four judges from independent providers" 但未提及 Gemini 的异质性。虽然 Section 5.3 第 150 行有提及 "a weaker, originality-dominated formality pattern"，但 Abstract 和 Conclusion 的措辞给人的印象是四个 judge 表现一致。
  - 更根本的问题：论文选择了 formality 和 verbosity 这两个*已知*最容易产生 style bias 的轴（引用 Wu & Aji 2025; Saito et al. 2023），这是否存在 axis selection bias？在"最容易"产生偏差的轴上观察到偏差，说服力有限。Limitations p9 提到 tone axis pilot 因 NLI gate 拒绝率高达 55% 而失败——如果 CSD 只能处理 surface-level 轴，那么"across style axes"的概括性声明需要更大折扣。
- 为什么影响接收：直接关系到论文核心 claim 的可信度。
- 建议修改方向：将 Abstract 修改为"across two primary and one exploratory style axes, with varying effect sizes across judges"；在 Abstract/Conclusion 中明确提及 Gemini 的较弱效应；讨论 axis selection 的潜在偏差。

**N3** [critical] Title "Blindspot" 预设了 Likert attenuation 解释，与论文自身承认的三种竞争解释不一致

- 具体位置：Title; Section 5.1 §85-92 (三种解释的讨论)
- 问题："Blindspot"一词的语义预设是 Likert *遗漏*了真实存在的信号（即 attenuation 解释）。但论文明确承认三种非排他性解释：(a) Likert attenuation, (b) pairwise amplification, (c) construct divergence。在 (b) 下，pairwise 放大了微弱偏好；在 (c) 下，两种模式测量不同构念。这两种解释下，"Blindspot" 的比喻都不准确——Likert 没有"盲点"，它只是在测量一个不同的东西，或者 pairwise 在放大噪声。

  论文在 Section 5.1 第 86-92 行做了详细讨论，但 Title/Abstract/Conclusion 的 framing 仍然偏向 attenuation 解释。特别是 Conclusion (Section 6, p8) 的表述 "Likert-only audits may fail to surface style-driven preferences" 暗示 pairwise 检测到的是"真实的" preferences，这仍然是在预设 attenuation。

- 为什么影响接收：标题是论文最重要的 framing 决策。如果标题的隐含假设与论文自身的 nuanced discussion 矛盾，会引起 reviewer 和读者的不信任。
- 建议修改方向：考虑更中性的标题，如 "Measurement-Mode Divergence in LLM Judge Style Evaluation" 或 "The Likert-Pairwise Gap"。或在 Abstract 中更早、更显著地承认 amplification 和 construct divergence 解释，使读者不会从标题获得单一方向的印象。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] GEE conditional decomposition 的解释力取决于 confounders 的完整性，但论文未讨论 omitted variable bias

- 具体位置：Section 5.2 (p7), Table 2
- 问题：GEE 模型仅包含两个 predictors（Style direction, Originality）。如果存在其他影响 judge 偏好的变量（如文本长度、难度、任务类型）且与 style 相关，则 Style OR 估计会有 omitted variable bias。虽然 Appendix T 有 cross-axis contamination analysis，Appendix 提到了 FK grade 和 sentence length 的控制，但主文中对 GEE 模型的完整性假设缺乏讨论。
- 建议：在 Section 5.2 或 Limitations 中明确列出 GEE 模型的识别假设和可能遗漏的 confounders。

**W2** [warning] Claude Sonnet 4 作为 low-sensitivity reference 的验证不够充分

- 具体位置：Section 5.1 §88; Appendix H
- 问题：Claude 被用作"low-sensitivity reference"来支持 Blindspot 的 discriminative validity，但这一角色缺乏 a priori justification。论文的逻辑是事后的："Claude 效应弱 → Claude 是 reference → Blindspot 有 discriminative validity"。这存在循环论证风险。此外：
  - Pooled TOST 在 Δ=10pp 处不显著（p > .05），仅在 Δ=12pp 处显著（p = .035）——equivalence margin 的选择缺乏先验依据
  - Bayesian BF₀₁ = 0.80 是 inconclusive，不支持也不反对 null
  - AEval verbosity Style OR = 4.76 (p < .001) 表明 Claude 并非在所有条件下都是 low-sensitivity
- 建议：承认 Claude 作为 reference 的选择是 post-hoc 的；提供 equivalence margin 的先验理据；在讨论中降低对 Claude reference 论证的权重。

**W3** [warning] 信息密度过高——8 页正文承载了过多实验维度，核心 narrative 被稀释

- 具体位置：全文
- 问题：正文需要传达 4 judges × 3 axes × 3 benchmarks + GEE + TOST + Bayesian + 7 种统计方法 + power analysis + Claude reference + rewriter independence。虽然 13 页附录帮助卸载了细节，但主文仍然在每个段落中压缩了大量数字和统计结果。例如 Section 5.1 (p6) 一个段落中包含了 TOST p-values、GEE Style ORs、GPT-4o 对照、Bayesian BF₀₁，读者需要同时 track 多个统计框架的结果。这降低了可读性和核心信息的传达效率。
- 建议：考虑将 7 种统计方法比较、Claude TOST、Bayesian equivalence 全部移至附录，主文聚焦于 BT + GEE 的核心结果，释放空间加强 narrative coherence。

**W4** [warning] 主要分析使用 LLMBar (n=100)，样本量对 GEE 估计的 small-sample bias 可能严重

- 具体位置：Section 3.4, Section 5.2 (p7 "Sample-size sensitivity")
- 问题：论文坦诚承认 n=88 的 GEE OR 存在 small-sample upward bias（Qwen3 formality Style OR 从 4.20 降至 2.15，~49% shrinkage at n=355）。这个 shrinkage 幅度非常大。但其他 judges 和 verbosity 轴没有 n=355 的验证——我们无法确定 verbosity Style OR 8-13 在更大样本上是否也会缩水 ~50%。论文在 p7 说"Verbosity Style ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)"，但这是推测而非实证。
- 建议：明确标注 n=88 结果的 point estimates 可能存在 substantial upward bias，在 Table 2 caption 中加入此 caveat；在跨 benchmark 复制中对 verbosity 进行 n=355 级别的验证。

**W5** [warning] 与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分

- 具体位置：Section 5.4 §173-175; Section 2 §37
- 问题：Jeong et al. (2025) 直接挑战了本文的核心前提——pairwise comparison amplifies style biases relative to pointwise scoring。论文用六个 controls 来 bound amplification risk，但这些 controls 不能排除 amplification，只能限制其幅度。更关键的是，论文没有量化 amplification factor 的可能范围。Section 5.4 列出的六个 controls 中：
  - (i) NLI ablation 只证明 NLI gate 有效，不涉及 format amplification
  - (ii) Claude reference 本身验证不足（见 W2）
  - (iii-vi) 间接证据，不直接测量 amplification magnitude
  Limitations p8 承认 "we cannot quantify it precisely without a ground-truth bias magnitude"——这个承认应该在主文中更加突出。
- 建议：在 Section 5.4 中量化 amplification 的可能范围（即使是 rough bounds），或更明确地讨论如果 amplification factor 大于某个值，核心结论如何改变。

---

## 小问题（不影响接收）

- **M1**: Table 1 的 footnote 解释系统在表格底部挤在一起，建议用更清晰的 legend 格式。特别是 $\dagger$ / $\dagger_e$ / $\dagger_c$ / --- 的含义需要更直观的说明。
- **M2**: Figure 2 (DAG) 中的 dashed orange $S \to Q$ path 标注 "residual confound." 字体太小，不易辨认。
- **M3**: Section 2 Related Work 的 "Mode-specific biases in LLM judges" 段落（p4 §44-46）提出了一个有趣但未被充分发展的论点（RLHF 训练造成的 format-specific biases），建议在主文或附录中提供更多证据。
- **M4**: Abstract 第 4 句 "GEE conditional decomposition reveals qualitatively distinct per-axis confound structures" 对不熟悉 GEE 的读者不够友好，建议用更直观的语言描述。
- **M5**: "Code and Data will be released upon acceptance" — 建议提供匿名 repository 或至少在 supplementary material 中包含核心代码以提高可复现性。
- **M6**: Section 3.1 (p4) 提到 temperature 0.7 用于 rewriting，但未说明选择依据。
- **M7**: Limitations 中 "tone axis pilot" 的结果（NLI gate 拒绝 55%）很有信息量，但与正文的连接不够紧密——建议在 Method 或 Experiments 中简要提及 CSD 的 scope boundary。

---

## Questions to Authors

1. 如果 pairwise amplification 是主要机制（而非 Likert attenuation），那么你们的方法学建议会如何改变？目前 Conclusion 的"single-format audits risk systematic blind spots"暗示应该添加 pairwise 模式，但如果 pairwise 是在放大微弱偏好，添加它反而会引入 false positives。请讨论在 amplification-dominant 情景下的 practical implications。

2. 为什么不包含 human evaluation 来 ground-truth 两种测量模式？论文多次提到这是"the key next step"（Conclusion p8, Limitations p8），但对于一篇旨在区分两种测量模式的论文，缺乏人工评估数据是一个显著的方法论空缺。

3. Qwen3-32B 在 formality Style OR 从 4.20 (n=88) 降至 2.15 (n=355)，~49% shrinkage。如果对 verbosity 进行同样的 scaling，Style OR 可能从 13.10 降至 ~6.5。这仍然 >1，但你们如何确保 small-sample bias 不会改变 Table 2 中其他 judges 的 regime classification？

4. Cross-axis contamination analysis (Appendix T, p16) 报告 formality rewrites 产生 negligible sentence structure changes (|d| < 0.03)，但 verbosity rewrites 的 Flesch-Kincaid grade 有 elevated shift (d = 0.50, Table 21)。这是否意味着 verbosity 的 "style bias" 部分是 readability bias？FK grade 的 60% mediation by sentence length (p7) 进一步暗示了这一点。

---

## Missing References（可能遗漏的相关工作）

1. **Gladkoff et al. (2024/2025)** — 关于 LLM judge 评分校准 (calibration) 的工作，与 Likert scale 的 ceiling effect 讨论相关。
2. **Kocmi & Federmann (2023)** — GEMBA: Using GPT Models for Reference-Free MT Evaluation，涉及 LLM judge 在 Likert vs pairwise 上的比较。
3. 论文引用了大量 2025-2026 年工作（RATE, CASSE, FairJudge, Comparative Trap, Preference Leakage），coverage 整体较好。建议确认 Reber et al. (2025) RATE 和 Jeong et al. (2025) Comparative Trap 的引用信息是否准确（arxiv preprint 可能已被接收并需要更新引用格式）。

---

## 主要优势

1. **实验设计极其严谨**：六项实验控制（NLI ablation、Claude reference、cross-axis variation、rewriting artifact、debiased prompting、four-architecture replication）、七种统计方法、三个 benchmark 的交叉验证。这是 LLM judge bias 文献中方法论最严谨的工作之一。
2. **GEE per-axis decomposition 有实用诊断价值**：分离 style-specific 和 quality-correlated components 的能力对评估 pipeline 的实际审计有直接用途。Verbosity 的 style-dominated 模式与 formality 的 conditional 模式的对比是真正有信息量的发现。
3. **Limitations 章节极其诚实和全面**：讨论了 quality-style confounding、evaluator-producer bias、scope boundaries、validation methodology 等关键局限，几乎没有 reviewer 需要补充的未提及限制。这在 NLP 论文中非常少见。
4. **Related Work 覆盖全面**：从经典心理测量学到最新 LLM judge bias 工作，引用覆盖面广且组织有序。与 RATE 和 Comparative Trap 的差异化讨论清晰。
5. **统计方法论透明**：FWER 控制、exploratory vs confirmatory 分类、bootstrap CI 的计算细节都有详细说明。GEE 模型诊断（附录 D）提供了 correlation structure robustness 和 interaction tests。
6. **Cross-benchmark replication** 加强了结果的 generalizability，三个 benchmark (LLMBar, AlpacaEval, MT-Bench) 覆盖不同的 evaluation scenarios。

---

## 总结

这是一篇**执行质量非常高**的实证论文，方法论严谨程度在 LLM judge bias 文献中属于上乘。主要弱点在于**新颖性**：核心发现（pairwise 比 Likert 更敏感于 style differences）是心理测量学的经典结论，论文声称的三个 "LLM-specific distinctions" 不足以构成对经典框架的本质超越。此外，**无法区分 attenuation 和 amplification** 这一根本限制——尽管论文坦诚讨论——削弱了 practical implications 的确定性。标题 "Blindspot" 与论文自身承认的多种解释之间存在张力。

推荐 **3.5 (Borderline Conference)**，执行质量支持主会议接收，但新颖性不足可能使其更适合 Findings track。如果作者在 rebuttal 中能够 (1) 更诚实地定位新颖性（实证 characterization 而非方法论创新），(2) 提供 human evaluation 数据或至少 pilot 结果来区分 attenuation 和 amplification，评分可能提升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-23T08:58:53.283823+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix、Minor 问题以及 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### 维度打分\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 核心定性发现有充分支撑；定量 OR 估计受小样本偏差影响，GPT-4o formality 在 FK control 下失去显著性，Claude 负对照证据链内部矛盾 |\n| Excitement | 3.5/5 | 问题重要且及时，GEE per-axis decomposition 是方法论推进，但 construct divergence vs attenuation 的 adjudication 留给未来工作 |\n| Reproducibility | 4/5 | 实验细节充分，prompts 公开，代码数据承诺接收后释放 |\n\n### Must-Fix\n\n**N1** [critical] 小样本 OR 膨胀对主要定量结论的系统性影响未充分传播\n- n=88→n=355 的 Qwen3-32B formality Style OR 从 4.20 缩水至 2.15（-49%），Table 2 中其他 11 个 n=88 cell 的 OR 以 face value 呈现。Verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5，论文做了文字推演但未提供 shrinkage-adjusted 估计。\n- 建议：(a) Table 2 旁给出 shrinkage-adjusted projected ORs；(b) 明确声明所有 n=88 OR 应被视为上界估计。\n\n**N2** [critical] GPT-4o formality Style OR 在控制 FK grade 后失去显著性\n- FK grade change 作为 GEE 协变量后，GPT-4o Style OR 从 2.70→2.15（p=.132）。GPT-4o 是论文叙事的锚点 judge。当前处理：Appendix 一段话带过（\"Two of three judges retain significant\"）。\n- 建议：(a) 正文 Section 5.2/5.3 明确提及；(b) 讨论 FK 是 mediator 还是 confounder。\n\n**N3** [critical] Claude \"low-sensitivity reference\" 证据链存在内部矛盾\n- 四条 convergent evidence 每条单独不成立：TOST underpowered, GEE MDE=1.56 无法排除 small effect, BF₀₁=0.80 inconclusive, AEval verbosity Style OR=4.76 与标签矛盾。Section 5.4 六项 controls 中 \"(ii) Claude low-sensitivity reference (Style OR n.s.)\" 选择性引用 LLMBar formality。\n- 建议：(a) 降级为\"lower-sensitivity judge\"；(b) 更新 Section 5.4 的描述；(c) 正文讨论 AEval verbosity OR=4.76。\n\n### Should-Fix\n\n**W1** Evaluator-producer overlap 仅用一个替代 rewriter 验证。Qwen3-32B rewriter→judge overlap 仅用 GPT-4o 替代验证（22% OR 降幅），缺少 rule-based rewriter。Formality 替代 rewriter 未报告 GEE。\n\n**W2** Cross-benchmark replication 是选择性的——24 cells 只填了 6 个（25%），选择最强 cell，可能向上偏倚。\n\n**W3** TOST equivalence margin 缺乏独立依据——5 个 margin 无先验 justification。\n\n**W4** 因果语言不够一致——Section 3.1 \"constitutes a binary intervention\" vs Section 3.5 \"interventional rather than formal causal evidence\"。\n\n### Minor\n\n**M1**: Table 1 \"n=88\" 与 verbosity 实际 n=86 不一致。\n**M2**: Intro opening example 是 cherry-picked，应注明。\n**M3**: DAG orange dashed line 黑白打印不可辨。\n**M4**: Appendix Table 3 QIC 值显示\"---\"无实际数值。\n**M5**: BT `choix` library \"default regularization\" 未说明具体形式。\n\n### Questions\n\n**Q1**: verbosity 做 scaled replication 预期 OR 缩水多少？会改变 regime classification 吗？\n**Q2**: FK grade 是 mediator 还是 confounder？请提供 DAG 论据。\n**Q3**: AEval verbosity Claude Style OR=4.76 如何调和 low-sensitivity reference？\n**Q4**: Direction-aware gate 的 verbosity expansion 是否漏过 R→Q 路径？\n**Q5**: BT regularization sensitivity analysis？",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix、Minor 问题以及 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### 维度打分\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 核心定性发现有充分支撑；定量 OR 估计受小样本偏差影响，GPT-4o formality 在 FK control 下失去显著性，Claude 负对照证据链内部矛盾 |\n| Excitement | 3.5/5 | 问题重要且及时，GEE per-axis decomposition 是方法论推进，但 construct divergence vs attenuation 的 adjudication 留给未来工作 |\n| Reproducibility | 4/5 | 实验细节充分，prompts 公开，代码数据承诺接收后释放 |\n\n### Must-Fix\n\n**N1** [critical] 小样本 OR 膨胀对主要定量结论的系统性影响未充分传播\n- n=88→n=355 的 Qwen3-32B formality Style OR 从 4.20 缩水至 2.15（-49%），Table 2 中其他 11 个 n=88 cell 的 OR 以 face value 呈现。Verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5，论文做了文字推演但未提供 shrinkage-adjusted 估计。\n- 建议：(a) Table 2 旁给出 shrinkage-adjusted projected ORs；(b) 明确声明所有 n=88 OR 应被视为上界估计。\n\n**N2** [critical] GPT-4o formality Style OR 在控制 FK grade 后失去显著性\n- FK grade change 作为 GEE 协变量后，GPT-4o Style OR 从 2.70→2.15（p=.132）。GPT-4o 是论文叙事的锚点 judge。当前处理：Appendix 一段话带过（\"Two of three judges retain significant\"）。\n- 建议：(a) 正文 Section 5.2/5.3 明确提及；(b) 讨论 FK 是 mediator 还是 confounder。\n\n**N3** [critical] Claude \"low-sensitivity reference\" 证据链存在内部矛盾\n- 四条 convergent evidence 每条单独不成立：TOST underpowered, GEE MDE=1.56 无法排除 small effect, BF₀₁=0.80 inconclusive, AEval verbosity Style OR=4.76 与标签矛盾。Section 5.4 六项 controls 中 \"(ii) Claude low-sensitivity reference (Style OR n.s.)\" 选择性引用 LLMBar formality。\n- 建议：(a) 降级为\"lower-sensitivity judge\"；(b) 更新 Section 5.4 的描述；(c) 正文讨论 AEval verbosity OR=4.76。\n\n### Should-Fix\n\n**W1** Evaluator-producer overlap 仅用一个替代 rewriter 验证。Qwen3-32B rewriter→judge overlap 仅用 GPT-4o 替代验证（22% OR 降幅），缺少 rule-based rewriter。Formality 替代 rewriter 未报告 GEE。\n\n**W2** Cross-benchmark replication 是选择性的——24 cells 只填了 6 个（25%），选择最强 cell，可能向上偏倚。\n\n**W3** TOST equivalence margin 缺乏独立依据——5 个 margin 无先验 justification。\n\n**W4** 因果语言不够一致——Section 3.1 \"constitutes a binary intervention\" vs Section 3.5 \"interventional rather than formal causal evidence\"。\n\n### Minor\n\n**M1**: Table 1 \"n=88\" 与 verbosity 实际 n=86 不一致。\n**M2**: Intro opening example 是 cherry-picked，应注明。\n**M3**: DAG orange dashed line 黑白打印不可辨。\n**M4**: Appendix Table 3 QIC 值显示\"---\"无实际数值。\n**M5**: BT `choix` library \"default regularization\" 未说明具体形式。\n\n### Questions\n\n**Q1**: verbosity 做 scaled replication 预期 OR 缩水多少？会改变 regime classification 吗？\n**Q2**: FK grade 是 mediator 还是 confounder？请提供 DAG 论据。\n**Q3**: AEval verbosity Claude Style OR=4.76 如何调和 low-sensitivity reference？\n**Q4**: Direction-aware gate 的 verbosity expansion 是否漏过 R→Q 路径？\n**Q5**: BT regularization sensitivity analysis？",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-23T08:59:30.554232+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 37270
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-23T08:59:30.855938+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix、Minor 问题以及 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### 维度打分\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 4/5 | 方法论严谨，六项控制、七种统计方法、跨 benchmark 复制。但无法区分 attenuation 与 amplification，核心结论依赖 n=100 LLMBar。 |\n| Excitement | 3/5 | 核心 insight 是 Thurstone (1927) 以来的经典结论。GEE per-axis decomposition 是最具新意的部分，但属于标准统计工具的领域应用。 |\n| Reproducibility | 4/5 | 方法描述详尽，代码数据承诺接收后释放。 |\n\n### Must-Fix\n\n**N1** [critical] 新颖性定位不够诚实：核心发现是经典心理测量结论的领域迁移，三个 \"LLM-specific distinctions\" 被夸大\n- **(a) Per-axis structure**: 经典 IRT 中 item-level discriminability variation 是标准现象，不是方法论创新。\n- **(b) GEE source decomposition**: GEE 是成熟工具，应用于 style/quality 分解是工程贡献，非\"absent from the classical framework\"。经典 factor analysis 和 SEM 承担类似功能。\n- **(c) Binary divergence**: 更可能反映效应量位于 Likert 检测阈值以下（Figure 4 power analysis 完全解释），非超越经典理论。\n- 建议：定位为\"empirical characterization of a known phenomenon in a new domain\"，突出 GEE 的实用价值而非过度宣称方法论新颖性。\n\n**N2** [critical] \"Consistently divergent\" claim 过强\n- 仅 2 个 primary + 1 个 exploratory axis。Gemini formality 明显较弱（Style OR 1.64 n.s., BT 57.4%）。选择了已知最容易产生 bias 的轴（Wu & Aji 2025; Saito et al. 2023），存在 axis selection bias。Tone axis pilot 因 NLI gate 拒绝 55% 而失败——CSD 仅适用 surface-level 轴。\n- 建议：Abstract 改为\"across two primary and one exploratory style axes, with varying effect sizes across judges\"。\n\n**N3** [critical] Title \"Blindspot\" 预设 Likert attenuation 解释\n- \"Blindspot\" 语义预设 Likert 遗漏了真实信号。但在 pairwise amplification 或 construct divergence 下，Likert 没有\"盲点\"。Title/Abstract/Conclusion 偏向 attenuation 解释，与 Section 5.1 的 nuanced discussion 矛盾。\n- 建议：更中性标题如\"Measurement-Mode Divergence\"或\"The Likert-Pairwise Gap\"，或在 Abstract 更早承认 amplification/construct divergence。\n\n### Should-Fix\n\n**W1** GEE 模型仅含两个 predictors（Style, Originality），omitted variable bias 未讨论。\n**W2** Claude 作为 reference 的选择是 post-hoc 的，存在循环论证风险。\n**W3** 信息密度过高——8 页承载过多维度，核心 narrative 被稀释。\n**W4** n=88 的 GEE small-sample bias 可能严重——verbosity 无 n=355 验证。\n**W5** Comparative Trap 的关系处理不够——六个 controls 不能排除 amplification，未量化 amplification factor 范围。\n\n### Minor\n\n**M1**: Table 1 footnote 系统不够清晰（†/†e/†c/---）。\n**M2**: DAG Figure 2 orange dashed line 字体太小。\n**M3**: RLHF format-specific biases 段落（Section 2 p4 §44-46）未充分发展。\n**M4**: Abstract GEE 描述对不熟悉 GEE 的读者不友好。\n**M5**: 应提供匿名 repository 而非仅承诺 acceptance 后释放。\n**M6**: Temperature 0.7 无选择依据。\n**M7**: Tone axis pilot 应在 Method 中提及 CSD scope boundary。\n\n### Questions\n\n**Q1**: 如果 pairwise amplification 是主要机制，practical implications 如何改变？\n**Q2**: 为什么不包含 human evaluation 来 ground-truth？\n**Q3**: Verbosity scaled replication 后 OR 如何？其他 judges regime classification 是否改变？\n**Q4**: Verbosity FK grade d=0.50 mediation 60% by sentence length——verbosity \"style bias\" 部分是 readability bias？\n\n### Missing References\n\n1. Gladkoff et al. (2024/2025) — LLM judge 评分校准\n2. Kocmi & Federmann (2023) — GEMBA\n3. 确认 RATE 和 Comparative Trap 引用是否为最新版本",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix、Minor 问题以及 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### 维度打分\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 4/5 | 方法论严谨，六项控制、七种统计方法、跨 benchmark 复制。但无法区分 attenuation 与 amplification，核心结论依赖 n=100 LLMBar。 |\n| Excitement | 3/5 | 核心 insight 是 Thurstone (1927) 以来的经典结论。GEE per-axis decomposition 是最具新意的部分，但属于标准统计工具的领域应用。 |\n| Reproducibility | 4/5 | 方法描述详尽，代码数据承诺接收后释放。 |\n\n### Must-Fix\n\n**N1** [critical] 新颖性定位不够诚实：核心发现是经典心理测量结论的领域迁移，三个 \"LLM-specific distinctions\" 被夸大\n- **(a) Per-axis structure**: 经典 IRT 中 item-level discriminability variation 是标准现象，不是方法论创新。\n- **(b) GEE source decomposition**: GEE 是成熟工具，应用于 style/quality 分解是工程贡献，非\"absent from the classical framework\"。经典 factor analysis 和 SEM 承担类似功能。\n- **(c) Binary divergence**: 更可能反映效应量位于 Likert 检测阈值以下（Figure 4 power analysis 完全解释），非超越经典理论。\n- 建议：定位为\"empirical characterization of a known phenomenon in a new domain\"，突出 GEE 的实用价值而非过度宣称方法论新颖性。\n\n**N2** [critical] \"Consistently divergent\" claim 过强\n- 仅 2 个 primary + 1 个 exploratory axis。Gemini formality 明显较弱（Style OR 1.64 n.s., BT 57.4%）。选择了已知最容易产生 bias 的轴（Wu & Aji 2025; Saito et al. 2023），存在 axis selection bias。Tone axis pilot 因 NLI gate 拒绝 55% 而失败——CSD 仅适用 surface-level 轴。\n- 建议：Abstract 改为\"across two primary and one exploratory style axes, with varying effect sizes across judges\"。\n\n**N3** [critical] Title \"Blindspot\" 预设 Likert attenuation 解释\n- \"Blindspot\" 语义预设 Likert 遗漏了真实信号。但在 pairwise amplification 或 construct divergence 下，Likert 没有\"盲点\"。Title/Abstract/Conclusion 偏向 attenuation 解释，与 Section 5.1 的 nuanced discussion 矛盾。\n- 建议：更中性标题如\"Measurement-Mode Divergence\"或\"The Likert-Pairwise Gap\"，或在 Abstract 更早承认 amplification/construct divergence。\n\n### Should-Fix\n\n**W1** GEE 模型仅含两个 predictors（Style, Originality），omitted variable bias 未讨论。\n**W2** Claude 作为 reference 的选择是 post-hoc 的，存在循环论证风险。\n**W3** 信息密度过高——8 页承载过多维度，核心 narrative 被稀释。\n**W4** n=88 的 GEE small-sample bias 可能严重——verbosity 无 n=355 验证。\n**W5** Comparative Trap 的关系处理不够——六个 controls 不能排除 amplification，未量化 amplification factor 范围。\n\n### Minor\n\n**M1**: Table 1 footnote 系统不够清晰（†/†e/†c/---）。\n**M2**: DAG Figure 2 orange dashed line 字体太小。\n**M3**: RLHF format-specific biases 段落（Section 2 p4 §44-46）未充分发展。\n**M4**: Abstract GEE 描述对不熟悉 GEE 的读者不友好。\n**M5**: 应提供匿名 repository 而非仅承诺 acceptance 后释放。\n**M6**: Temperature 0.7 无选择依据。\n**M7**: Tone axis pilot 应在 Method 中提及 CSD scope boundary。\n\n### Questions\n\n**Q1**: 如果 pairwise amplification 是主要机制，practical implications 如何改变？\n**Q2**: 为什么不包含 human evaluation 来 ground-truth？\n**Q3**: Verbosity scaled replication 后 OR 如何？其他 judges regime classification 是否改变？\n**Q4**: Verbosity FK grade d=0.50 mediation 60% by sentence length——verbosity \"style bias\" 部分是 readability bias？\n\n### Missing References\n\n1. Gladkoff et al. (2024/2025) — LLM judge 评分校准\n2. Kocmi & Federmann (2023) — GEMBA\n3. 确认 RATE 和 Comparative Trap 引用是否为最新版本",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-23T08:59:32.268465+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 1400 · 2026-05-23T08:59:35.571401+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1401 · 2026-05-23T08:59:38.186868+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：评分 **3.5 (Borderline Conference)**。

核心判断：
- **执行质量出色**：方法论严谨（六项实验控制、七种统计方法、三个 benchmark 交叉验证），Limitations 章节异常全面诚实
- **新颖性不足**：核心发现是 Thurstone (1927) 的经典结论在 LLM judge 上的验证，声称的三个 "LLM-specific distinctions" 可被经典框架解释
- **三个 Must-Fix**：(1) 新颖性定位过度宣称方法论创新；(2) "consistently divergent" 基于 2 个主要轴且 Gemini 效应显著弱；(3) 标题 "Blindspot" 预设 attenuation 解释，与论文自身承认的三种竞争解释矛盾
- GEE per-axis decomposition 是最有价值的贡献，具有实用诊断意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1402 · 2026-05-23T08:59:42.734617+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1403 · 2026-05-23T09:02:07.993881+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE with qualification] R2-N1: 新颖性定位不够诚实**

R2 的核心论点成立：Likert vs pairwise 的 sensitivity gap 确实是 Thurstone (1927) 以来的经典结论，论文在 Introduction（Section 1, p2 第12行）虽然引用了 Thurstone 和 power analysis，但随后列出的三个 "LLM-specific distinctions" 有不同程度的夸大。

- **(a) Per-axis structure**: [AGREE] R2 说经典 IRT 中 item-level discriminability variation 是标准现象，这是对的。但我认为论文的贡献不在于"discriminability varies"这一抽象结论，而在于 empirically characterizing *哪些* style axes 是 style-dominated vs quality-confounded（Table 2）。"content-specific pattern that Thurstone's format-general discriminability gradient does not predict"（Section 1）的措辞确实过强——Thurstone 的框架并不排斥 content-specific variation，它只是没有 address 这个问题。建议改为"complements"而非暗示"surpasses"。

- **(b) GEE source decomposition**: [REBUT] R2 将此等同于"标准统计工具的领域应用"，认为 factor analysis/SEM 承担类似功能。但 factor analysis 和 SEM 需要 latent variable modeling 和 multiple indicator 结构，与 GEE conditional decomposition 的目标不同。GEE 在此处的应用不是拟合 latent factor，而是在给定 binary outcome（pairwise choice）下分离两个 observed predictors（style direction, originality）的条件贡献。这在 LLM judge bias 文献中确实是新的分析层——prior work（RATE, FairJudge, CASSE）均未做过此类 per-axis confound decomposition（Section 2 第35行明确对比了 correlational vs interventional approaches）。"absent from the classical framework" 的措辞可以更精确（改为 "not standard practice in LLM judge evaluation"），但 R2 将其矮化为纯工程贡献不够公平。

- **(c) Binary divergence**: [AGREE] R2 说 Figure 4 的 power analysis "完全解释"了 binary split——这是正确的。在 observed effect sizes 下，Likert 的 power < 20%，当然会产生 binary split（all fail）。论文说"sharper than the gradual attenuation classical theory predicts"（Section 1, p2 第13行）是过度宣称——经典理论在 power < 20% 时也会预测 binary failure。这应该删除或重述为 "consistent with the severe power deficit predicted by classical theory."

总结：我同意 R2 的方向——论文应重新定位为 "empirical characterization of a known phenomenon in a new domain, with a novel diagnostic layer (GEE decomposition)"，降低对 (a) 和 (c) 的新颖性宣称，保留 (b) 的方法论贡献。

---

**[AGREE with qualification] R2-N2: "Consistently divergent" claim 过强**

R2 指出仅 2 个 primary + 1 个 exploratory axis，且 axis selection bias 存在（选择了 formality 和 verbosity 是基于 Wu & Aji 2025 和 Saito et al. 2023 的 prior evidence）。这些都是事实。

但我对 R2 的批评有两个 nuance：

1. "Consistently divergent" 在论文中修饰的是 *across judges*（同一 axis 在 4 个 judge 上的一致性），而非 *across axes*。在 formality 上 4/4 target judges 显示 Blindspot（Table 1），verbosity 上 4/4，这确实是 consistent across judges。R2 的批评更准确地说是 axis coverage 不足，而非 cross-judge consistency 被夸大。

2. Gemini formality BT=57.4%（Style OR 1.64, n.s.）确实是 formality axis 的弱点——GEE 显示这是 originality-dominated 而非 style-driven（Table 2: Orig OR=2.51, p=.002; Style OR=1.64, p=.101）。论文在 Section 5.3 中已承认这一点，但 Abstract 中 "across four judges" 的 blanket statement 没有足够 qualify。

建议：同意 R2 提出的 Abstract 修改方向。更精确的措辞可以是 "across four target judges with varying effect sizes (three showing robust effects, one showing weaker, originality-dominated patterns)"。

---

**[REBUT with partial agreement] R2-N3: Title "Blindspot" 预设 Likert attenuation 解释**

R2 的语义分析是对的——"Blindspot" 确实暗示 Likert 遗漏了真实信号，这在 amplification 解释下不成立。但我认为这个问题的严重性被 R2 高估了：

1. 论文在 Section 1 第5行明确定义了 "Blindspot" 为 "an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, **without committing to a specific causal mechanism**"。这是一个操作性定义，不是因果主张。

2. 更重要的是，Abstract 和 Conclusion 确实列出了三种解释（attenuation, amplification, construct divergence），且 Section 5.1 的讨论是 genuinely agnostic。Title 的 framing 与正文的 nuance 之间确实存在张力，但不构成 internal contradiction。

3. R2 建议的替代标题 "Measurement-Mode Divergence" 其实已经是 subtitle（"Measurement-Mode Divergence in LLM Judge Style Evaluation"）。如果标题改为纯中性，论文的 communicative impact 会显著降低，而 "Blindspot" 是一个有 memorability 的标签——这在学术传播中有价值。

我的建议：保留 "Blindspot" 但在 Abstract 第一次出现时更早地 qualify（当前 qualification 在 Abstract 第6–7行才出现）。例如：将 "We term this the Likert Blindspot—an operational descriptor..." 提前到 Abstract 第2–3行。这比改标题更可操作。

---

### Should-Fix

**[AGREE] R2-W1: GEE omitted variable bias**

Table 2 的 GEE 仅含 Style 和 Originality 两个 predictors。论文在 Appendix R 中做了 word count 和 FK grade 的 robustness checks（Style OR change <12%, covariate p>.28 for word count），但这些是事后敏感性分析，不是系统性的 omitted variable assessment。可能遗漏的 confounders 包括 text length, lexical complexity, topic domain 等。不过，GEE 的目标是 decomposition（分离 style 和 originality 的 relative contribution），不是完整的 causal identification——在这个 framing 下，两个 predictors 是 parsimonious 且 interpretable 的。建议在正文 Section 5.2 中增加一句 disclaimer 关于 omitted variable 的可能性。

**[AGREE] R2-W2: Claude 选择的 post-hoc 性质**

这与我在 R1-N3 中指出的 Claude 证据链问题一致。如果 Claude 是因为在 LLMBar 上显示 low BT 而被选为 reference，存在选择偏差。Cross-benchmark replication（Appendix U, Table 8：formality Style OR consistently n.s. across 3 benchmarks）部分缓解了这个问题，但 selection rationale 应在正文中明确说明。

**[REBUT] R2-W3: 信息密度过高**

论文的 8 页正文包含：Introduction（1.5 pp），Related Work（1.5 pp），Method（1.5 pp），Experiments + Analysis（3 pp），Conclusion（0.5 pp）。核心 narrative 的逻辑链是清晰的：CSD method → Blindspot finding → GEE decomposition → cross-judge/benchmark replication → robustness。详细的 diagnostics 和 sensitivity analyses 放在 Appendix（11 pp）中是恰当的信息分层。对于一篇 empirical methodology 论文，同时呈现方法、主要发现、和 robustness evidence 在 8 页内是必要的。我不认为 "density" 本身是问题——问题是每个 component 是否被充分发展，而我认为核心组件是够的。

**[AGREE] R2-W4: Verbosity 无 n=355 验证**

这与我在 R1-N1 中的 concern 一致。Verbosity Style OR 8–13 是论文最引人注目的数字（Table 2），但没有 scaled replication 来校准 small-sample bias。Section 5.2 的文字推演（"would remain style-dominated even under ~50% shrinkage"）是合理的逻辑推断，但不是实证验证。这是一个重要的 gap。

**[AGREE] R2-W5: Comparative Trap 关系处理不够**

论文承认 "the divergence cannot be definitively resolved without human ground-truth measurements"（Section 5.4），六项 controls "bound amplification risk" 但不能 quantify amplification factor。R2 要求量化 amplification factor range——这可能超出当前数据的能力，但论文应更明确地说明 bounding analysis 的局限性。例如，debiased prompting 降低了 5.7/13.1pp（Section 5.4 第(v)项），这可以被解释为 amplification 的 lower bound，但论文没有做这个连接。

---

### Minor

**[AGREE] R2-M1**: Table 1 的 footnote 系统（†/†e/†c/---）确实不够直观。建议统一为文字标签。

**[AGREE] R2-M2**: Figure 2 的 orange dashed line 和 label 确实偏小，黑白打印时可读性差。我在 R1 的 M3 中也指出了同样问题。

**[AGREE] R2-M3**: Section 2 最后一段关于 RLHF format-specific biases 的讨论（3 行）确实不够充分。这是一个重要的 point——pairwise 在 DPO/RLHF 中作为 reward signal 而 Likert 主要用于 benchmark，这种 asymmetric training exposure 可能本身就导致 mode-specific biases。值得在 Discussion 中展开。

**[AGREE] R2-M4**: Abstract 中 "GEE conditional decomposition" 对不熟悉 GEE 的读者不友好。建议在 Abstract 中用更通俗的语言（如 "regression-based decomposition"）。

**[REBUT] R2-M5**: R2 建议提供匿名 repository。在 ARR double-blind review 下，匿名 repository 存在 de-anonymization 风险（Git history, coding patterns 等），"Code and data will be released upon acceptance" 是 ACL 论文的常见做法。Reproducibility 评分 4/5（R2 自己给的）说明当前描述已足够支持 reproduction intent。

**[AGREE] R2-M6**: Temperature 0.7 无选择依据。虽然 NLI threshold sweep（Appendix E）显示 BT 对 NLI threshold 不敏感，但 rewriting temperature 可能影响 style manipulation 的强度和 content preservation 的 tradeoff。一个简短的 justification（如 "balancing diversity and coherence"）或 sensitivity check 会更好。

**[AGREE] R2-M7**: Tone axis pilot 的结果（NLI gate 拒绝 55%）目前在 Limitations 中提及（page 9），但 Method section 中确实应提及 CSD 的 scope boundary——即 CSD 仅适用于 surface-level axes whose rewrites preserve semantic content。

---

### Questions

**[Valuable] R2-Q1**: 如果 amplification 是主要机制，practical implications 确实会翻转——从 "use pairwise to detect bias" 变为 "treat pairwise results with caution, Likert may be the more calibrated mode." 论文在 Section 5.1 承认了这种可能性但没有展开其 implications。我同意这是一个应在 Discussion 中更充分处理的问题。

**[Valuable] R2-Q2**: 为什么不包含 human evaluation 来 ground-truth？这是该论文最大的缺失实验。Limitations 中说 "definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs"——但没有解释为什么当前工作没有做。可能的原因是成本和 annotation complexity，但应明确说明。

**[Valuable] R2-Q3**: 同我的 R1-Q1。Verbosity 的 scaled replication 是最重要的 missing experiment。

**[AGREE with nuance] R2-Q4**: Verbosity FK grade d=0.50 的 mediation 分析（Appendix R'：60% by sentence length, Sobel z=3.60）显示 verbosity "style bias" 确实部分反映了 readability 差异。但我认为 R2 的 framing 需要 nuance：sentence length change 是 verbosity manipulation 的 *inherent* property（verbose text IS longer sentences），所以 FK grade mediation 可能反映的是 verbosity 效应的 mechanism（通过 sentence length 传导），而非 confounding。这是 mediator vs confounder 的区分问题——如果 sentence length 是 verbosity → judge preference 的 causal pathway，controlling for it 是 over-controlling（bad control problem）。论文在 Table 7 footnote 中暗示了这一点（"sentence length change is inherent to verbosity manipulation"），但没有用 causal language 明确论证。

---

### Missing References

**[NEUTRAL]** R2 建议补充 Gladkoff et al. (2024/2025) 和 Kocmi & Federmann (2023, GEMBA)。这些引用与论文的核心贡献（measurement-mode divergence in style evaluation）的相关性有限——Gladkoff 关注评分校准，GEMBA 关注 MT evaluation。建议 authors 评估是否确实相关。确认 RATE 和 Comparative Trap 引用版本的建议是合理的。

---

### 总结

R2 的审稿整体质量高，核心 concerns 与我的评估有显著重叠（小样本 OR 膨胀、Claude 负对照、amplification 不可排除）。主要分歧在于：

1. **新颖性**：R2 认为 Excitement 仅 3/5，视核心发现为经典结论迁移。我部分同意（N1-a 和 N1-c），但认为 GEE decomposition 揭示的 per-axis confound structure（N1-b）不是简单的工具搬运——它产生了新的 empirical insight（verbosity style-dominated, formality conditional），这在 prior work 中不存在。我给 Excitement 3.5。

2. **信息密度**（W3）：R2 认为 8 页承载过多。我认为论文的信息分层（正文核心 + 详细 Appendix）是恰当的，不同意降级。

3. **Title**（N3）：R2 认为应改标题。我认为保留但更早 qualify 是更好的平衡。

我维持 **Overall 3.5 (Borderline Conference)** 不变。R2 的审稿没有改变我对论文的核心判断——定性发现扎实，定量 claims 需要 tightening。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1404 · 2026-05-23T09:02:25.798561+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1405 · 2026-05-23T09:02:28.423601+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条回应。主要判断：

- N1（新颖性）：部分同意——(a) per-axis structure 和 (c) binary divergence 的新颖性确实被夸大，但 (b) GEE decomposition 在 LLM judge bias 领域是新的分析层，不应矮化为纯工程贡献
- N2（consistently divergent 过强）：同意，axis coverage 仅 2+1 个，且选择了已知 bias-prone 的轴
- N3（Title 预设 attenuation）：部分反驳——"Blindspot" 有操作性定义（Section 1），建议保留但更早 qualify，而非改标题
- W1-W5：大部分同意，与我的 R1 评估重叠
- 维持 Overall 3.5 不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1406 · 2026-05-23T09:02:34.529646+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 135

## Round 135

12 recorded events


### User

_source line 1407 · 2026-05-23T09:03:26.890087+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: 小样本 OR 膨胀对定量结论的系统性影响**

同意这是一个重要问题。Qwen3-32B formality 的 49% shrinkage (Style OR 4.20 → 2.15, Section 5.2, p7) 是论文自己提供的最有力的 small-sample bias 证据。Table 2 中其余 11 个 n=88 cell 的 OR 确实以 face value 呈现，缺乏 shrinkage-adjusted 估计。

我在自己的审稿中也提出了同样的问题（我的 W4），并进一步指出：论文的文字推演"Verbosity Style ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)"虽然逻辑上成立（4-6.5 >> Orig OR <1），但这是推测而非实证。Table 2 应明确标注 n=88 的 point estimates 为上界估计，或者提供 shrinkage-corrected projections。

补充一点 R1 未提及的：Table 5 (Appendix C) 的 GEE CIs 显示 n=88 cells 的 95% CI 宽度非常大（如 GPT-4o verbosity Style OR 11.34 [4.93, 26.10]），这本身已经反映了估计精度的局限。CI 下界 4.93 仍然远高于 Orig OR 0.45，所以 regime classification 是稳健的——但论文应更突出地展示 CIs，而非仅在附录中报告。

**[AGREE] R1-N2: GPT-4o formality Style OR 在 FK control 下失去显著性**

同意这需要在正文中更明确地讨论。我确认了 Appendix R' 的具体数据：GPT-4o Style OR 从 2.70 降至 2.15 (p = .132)，确实不再显著。Qwen3-32B 从 4.20 降至 3.38 (p = .014)，Llama-70B 从 5.52 降至 2.69 (p = .037)——两个保留显著性。

GPT-4o 作为论文叙事的锚点 judge（Introduction 的 opening example 使用 GPT-4o，Table 1 以 GPT-4o 开头），其 formality Style OR 在 FK control 下失去显著性是一个 material finding，不应仅在附录一句话带过。

**但我补充一个 nuance（R1 在 Q2 中也提到了）**：FK grade 的角色是 mediator 还是 confounder 取决于 causal structure：
- 如果 formality → FK grade → judge score（mediator），则 controlling for FK 是错误的（"bad control"，Pearl 2009），因为它移除了合法的因果效应通路
- 如果 common cause → formality + FK grade（confounder），则 controlling 是正确的

论文的 DAG (Figure 2) 显示 S → Y（style → judge score）是单一直接路径，没有通过 FK 的中介。如果 formality 变化本身导致 FK grade 变化（这是很可能的——更正式的文本倾向于使用更长的句子和更复杂的词汇），那么 FK 是 mediator，控制它会低估真实的 style effect。论文应明确讨论这一点，而非简单地将 FK-controlled 结果作为 robustness check 呈现。

**[AGREE] R1-N3: Claude "low-sensitivity reference" 证据链的内部矛盾**

完全同意。我在自己的审稿中也将此列为 Should-Fix (我的 W2)，但 R1 对证据链的逐条解构更加系统，说服我这应升级为更严重的问题。四条 convergent evidence 逐一审视：

1. **TOST**: Per-axis 在 Δ=10pp 不显著 (p=.156, power ≈42%)，pooled 在 Δ=10pp 也不显著 (p=.100)——只在 Δ=12pp 处勉强显著 (p=.035)。Appendix G Table 9 确认了这一点。等价界限的选择缺乏先验依据。
2. **GEE MDE**: MDE=1.56 at 80% power 意味着无法排除 OR 在 1.0-1.56 之间的 small but real effects。
3. **BF₀₁=0.80**: 按 Jeffreys 标准，这是 anecdotal/inconclusive，不能作为 null 的证据。
4. **AEval verbosity Style OR=4.76 (p<.001)**: 这直接打破了 "low-sensitivity" 标签——Claude 在至少一个 axis×benchmark 组合上展现了与 target judges 可比的 style sensitivity。

R1 的建议合理：降级为 "lower-sensitivity judge"，并在 Section 5.4 的六项 controls 中更新 "(ii)" 的描述。我补充建议：在 Limitations 中已有的 Claude verbosity 讨论（p9 第 55 行："Verbosity sensitivity is benchmark-dependent (AEval Style OR = 4.76, p < .001; LLMBar n.s.)"）应提升至正文 Section 5.3/5.4。

---

### Should-Fix

**[AGREE] R1-W1: Evaluator-producer overlap 验证不充分**

同意，但 scope 需要限定。Evaluator-producer overlap 问题仅影响 Qwen3-32B（rewriter = judge）。GPT-4o、Llama-70B、Gemini 使用独立 rewriter，不受此 confound 影响（Appendix E 第 129 行明确说明）。论文提供了 GPT-4o 作为替代 rewriter 的验证（Tables 6-7），展示 verbosity OR 降幅 22%、formality BT 降幅 2.1pp，且 Blindspot 均保持。

R1 要求 rule-based rewriter 是理想化的——但实际上，rule-based formality rewriting 很难保证内容一致性（需要大量手工规则），且论文已在 Limitations (p9) 承认 "all alternative rewriters are instruction-tuned LLMs that may share style preferences acquired during RLHF training"。建议论文在 Limitations 中将 rule-based rewriter 作为明确的 future work direction。

**formality GEE 未报告**是一个有效的具体缺失——Table 7 只有 BT 和 Likert 结果，没有 GEE decomposition。如果 GPT-4o rewriter 改变了 formality 的 confound structure（如 Style vs Originality 比例），这会影响对 evaluator-producer bias 的评估。

**[AGREE] R1-W2: Cross-benchmark replication 的选择性**

同意，并且我认为这一问题比 R1 的评级（Should-Fix）更严重。Table 22 (Appendix T) 仅覆盖 6/24 cells (25%)，且论文自己承认选择的是 "selected configurations targeting the strongest effects"（Appendix T 第 655 行）。但主文 Section 5.3 第 157 行的表述是 "These per-axis patterns replicate across benchmarks"——这暗示了比实际更广泛的复制。

具体选择偏差风险：
- AEval 的 4 个 cells 中，2 个是 Blindspot (†)，2 个是 both significant (‡)——后者其实*削弱*了 Blindspot 的 claim（Likert 也能检测到），但论文将其解释为 "severity spectrum" 的确认
- Verbosity 仅在 AEval 上有一个 cross-benchmark cell (Qwen3)，没有 GPT-4o verbosity 的 cross-benchmark 数据
- Gemini 完全缺失于 cross-benchmark replication

建议论文承认选择性，并讨论缺失 cells 可能的影响方向。

**[AGREE] R1-W3: TOST equivalence margin 缺乏先验依据**

同意。Table 9 (Appendix G) 测试了 5 个 margins (Δ = 5, 10, 12, 15, 20pp)，但 12pp 作为 headline result 没有 a priori justification。在 equivalence testing 文献中 (Lakens, 2017)，margin 应基于 smallest effect size of interest (SESOI)，而非事后选择使 p < .05 的 margin。论文应讨论 12pp 在 BT scale 上对应什么程度的 style sensitivity——例如，12pp 意味着 judge 在 62% 的 pairwise 比较中选择 styled 文本，这在 RLHF 管道中是否构成"practically meaningful" bias？

**[REBUT] R1-W4: 因果语言不一致**

部分不同意。R1 引用的两处表述在不同层面操作：

- Section 3.1 "constitutes a binary intervention"：描述的是**操作层面**——CSD 对文本进行了 controlled manipulation（改变一个 style axis），这在操作上确实是一个 intervention（与 observational study 相对）
- Section 3.5 / Appendix A "interventional rather than formal causal evidence"：描述的是**推断层面**——论文不宣称达到 potential outcomes framework 下的 formal causal identification

这两者并不矛盾：你可以执行一个 intervention（操作上）而不宣称它达到了 formal causal identification（推断上）。Randomized experiments 和 natural experiments 都是 interventional designs，但推断强度不同。

**不过**，我承认对不熟悉因果推断文献的读者，这种区分可能造成困惑。建议在 Section 3.1 中将 "constitutes a binary intervention" 修改为 "approximates a binary intervention" 或 "operationalizes a single-axis manipulation"，避免与 formal causal intervention 的标准定义混淆。

---

### Minor

**[AGREE] R1-M1**: 如果 verbosity 的 NLI gate 通过率不同导致实际 n≠88，Table 1 header 应准确标注。建议统一使用 "n varies by axis; see Appendix" 或逐行标注。

**[REBUT] R1-M2**: 不同意 Intro opening example 需要标注为 "cherry-picked"。NLP 论文的 opening example 惯例上是选择性的、illustrative 的，用于建立 reader's intuition。论文随后提供了系统性的统计证据（Table 1, Figure 3, 七种统计方法），opening example 的功能是叙事性的而非论证性的。要求标注 "cherry-picked" 在学术写作规范中不常见，且可能暗示论文在隐瞒什么——但系统证据已经充分呈现。如果 R1 的担心是 example 的代表性，更好的做法是在附录提供该 example 的完整数据（NLI 分数、两个 judge 评分、position-swapped 结果），而非加标签。

**[AGREE] R1-M3**: DAG 的 orange dashed line 在灰度打印下确实不可辨。建议使用不同的 line pattern (e.g., dash-dot) 或 annotation 来区分。

**[AGREE] R1-M4**: Table 3 (Appendix C) 的 QIC "---" 应该报告实际数值或解释为什么省略。我在 PDF 中确认了这一点——所有 9 个 cells 都是 "---"，只有 |ΔQIC| 有值。

**[AGREE] R1-M5**: choix library 的 "default regularization" 应说明具体形式（L2? pseudo-count? regularization strength?）。这是一个 minor 但 valid 的 reproducibility concern。

---

### Questions

**R1-Q1**: verbosity scaled replication 预期 OR 缩水多少？
我与 R1 有相同的疑问（我的 Q3）。论文推测 50% shrinkage 将 OR 8-13 降至 4-6.5，仍 style-dominated。但 shrinkage 幅度可能因 axis 而异——verbosity 的效应量大于 formality，large effects 的 shrinkage 百分比可能更小（Nemes & Huang, 2009 的 bias correction 与效应量的关系是 non-linear 的）。实证验证是必要的。

**R1-Q2**: FK grade 是 mediator 还是 confounder？
关键问题。我在回应 N2 时已详细分析。简要补充：
- 论文的 DAG (Figure 2) 不包含 FK 作为中介节点——如果 FK 是 S→FK→Y 通路的一部分，控制 FK 会低估 style effect（over-control bias）
- 但 FK 也可能与 formality 共享 common cause（如原始文本的写作水平），此时控制是正确的
- 论文需要明确立场，或承认两种解释下的 GPT-4o Style OR 范围是 [2.15, 2.70]

**R1-Q3**: AEval verbosity Claude Style OR=4.76 如何调和 low-sensitivity reference？
我完全赞同这个质疑。Appendix U (Table 23) 和 Limitations (p9) 确认了这一数据。Claude 的 low-sensitivity 标签只在 LLMBar formality 上成立；AEval verbosity 的 Style OR 4.76 (p<.001) 与 GPT-4o verbosity Style OR 11.34 可比。论文应该承认 Claude 是 "lower-sensitivity on formality/LLMBar" 而非全局性的 "low-sensitivity reference"。

**R1-Q4**: Direction-aware gate 的 verbosity expansion 是否漏过 R→Q 路径？
这是一个好的技术问题，但我认为论文提供了充分的 empirical 回应：Appendix F (Section F, 第 212-217 行) 报告了 DA-only vs bidirectional-pass 子集的 BT 比较，无显著差异 (permutation p=.663, Δ=-1.1pp)。五个 judge 的 Fisher exact tests 均 p>.66。这些 empirical 验证表明 DA gate 没有系统性地漏过 quality-altering content。理论上的担忧是合理的，但 empirical evidence 充分缓解了这一风险。

**R1-Q5**: BT regularization sensitivity analysis？
同意应该提供。choix 的 default regularization (pseudo-count based) 可能对 small-n 估计有影响。建议作者报告无正则化或不同正则化强度下的 BT estimates，特别是对 n=88 的 cells。

---

### 总结

R1 的审稿整体质量很高。三个 Must-Fix 中，我完全同意 N1（small-sample bias 未充分传播）和 N3（Claude reference 证据链矛盾），对 N2 同意需要更多透明度但补充了 mediator vs confounder 的 nuance。Should-Fix 中，W1-W3 我同意，W4 我认为因果语言并非真正不一致而是在不同层面操作，但同意措辞可以改进。Minor issues 除 M2 外均同意。

R1 和我对论文的整体评价接近（均为 3.5 Borderline Conference），核心共识是：执行质量高，但新颖性不足（我比 R1 更强调这一点）、attenuation vs amplification 无法区分、以及 small-sample 定量估计的可靠性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-23T09:03:59.318884+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-23T09:03:59.469890+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-23T09:03:59.470385+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-23T09:03:59.470728+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T08:50:59.009456+00:00\", \"completed_at\": \"2026-05-23T08:51:02.076149+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 25, 8am (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-23T09:04:25.407638+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1413 · 2026-05-23T09:04:25.407967+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-23T09:07:43.834056+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: S4 称 GEE decomposition 是'真正的方法论贡献'——首次获正面评价。但仍认为 GEE 被 undersold。Intro 3 个 LLM-specific distinctions 被认可。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 fresh: R2 列为 Must-Fix N1 (critical)——三个 LLM-specific distinctions 被夸大：(a) per-axis structure 是 IRT 标准现象，(c) binary divergence 被 Figure 4 power analysis 完全解释。R1 交叉部分同意(a)(c)但 REBUT (b)：GEE decomposition 不等同于 factor analysis/SEM，是 LLM judge bias 领域的新分析层。共识：重新定位为 'empirical characterization + novel diagnostic layer'，不过度宣称 'beyond classical framework'。\"\n    action_items:\n      - round: 17\n        action: \"Intro 三个 LLM-specific distinctions 需重新措辞：(a) 'complements' 而非 'surpasses' classical framework；(c) 删除 'sharper than...classical theory predicts' 或改为 'consistent with severe power deficit'；(b) 改为 'not standard practice in LLM judge evaluation' 而非 'absent from classical framework'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 13-16 issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"Table 1 已拆为 LLMBar primary only，cross-benchmark 移至 Appendix T。脚注包含方向不对称信息。\"\n    resolution_round: 16\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及。Related Work RATE 段落已改善。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Related Work 中 RATE 定位被两位 Reviewer 评为'准确且诚实'(R1-S4)。\"\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 M1: Title 仍隐含 Likert 有缺陷。采用 Option C（保持 title + 充实 construct divergence）。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N3 再次提出。R1 交叉 REBUT——'Blindspot' 有操作性定义(Section 1 第5行)，保留 title 但更早 qualify。分歧：R2 要改标题，R1 要保留+更早 qualify。两位均同意 Title 与正文 nuanced discussion 存在张力。\"\n    action_items:\n      - round: 17\n        action: \"保留 Blindspot title，但在 Abstract 第 2-3 行更早引入操作性定义和三种解释的 qualification，使读者不会从标题获得单一方向印象\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF2: 三条 convergent evidence 每条单独仍不足。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N3 系统解构四条证据线——TOST underpowered, MDE=1.56 无法排除 small effect, BF₀₁=0.80 inconclusive, AEval verbosity OR=4.76 直接矛盾。R2 交叉完全 AGREE 并升级严重性。共识：降级为 'lower-sensitivity judge'，Section 5.4 更新描述，AEval verbosity 讨论提升到正文。\"\n    action_items:\n      - round: 17\n        action: \"(1) 全文 'low-sensitivity reference' → 'lower-sensitivity judge' (relative rather than absolute)；(2) Section 5.4 第(ii)项更新为包含 benchmark-dependent qualification；(3) AEval verbosity OR=4.76 讨论从 Limitations 提升到 Section 5.3/5.4；(4) TOST margin 需提供 practical significance 论据\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽，n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF1: 降级为 Should-Fix。Projection 论证足够。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 升级为 Must-Fix N1——Table 2 其他 11 个 n=88 cell 以 face value 呈现，未提供 shrinkage-adjusted 估计。R2 交叉完全 AGREE，补充 CI 宽度证据（GPT-4o verb OR 11.34 [4.93,26.10]）。共识：n=88 OR 应标注为上界估计，提供 projected ranges。\"\n    action_items:\n      - round: 17\n        action: \"(1) Table 2 caption/footnote 明确声明 n=88 OR 为上界估计（Nemes et al. 2009）；(2) 提供 verbosity 的 shrinkage-adjusted projected ORs (4-6.5)；(3) 正文 Section 5.2 更突出地讨论 CI 宽度对解释的影响\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF3: 升级为 Must-Fix。'systematically' 已替换为 'consistently' 在 5 处。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N2——'consistently divergent' 仍过强，基于 2 primary + 1 exploratory axis，且选择了已知 bias-prone 的轴。R1 交叉同意但 qualify：consistency 指 across judges（4/4 成立）而非 across axes。共识：Abstract 需更精确措辞。Gemini formality 异质性应在 Abstract/Conclusion 提及。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 改为 'across two primary and one exploratory style axes, with varying effect sizes across judges (three showing robust effects, one showing weaker, originality-dominated patterns)' 或类似精确措辞\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: \"100-pair annotation (50 formality + 50 verbosity, 70 NLI-pass + 30 NLI-fail): gate pass precision=98.6% (69/70, both annotators concordant), AC₁=0.96. Only 2/70 NLI-pass flagged by either annotator. Gate conservative: 93-100% of NLI-fail also preserve meaning (false rejection dominant). κ paradox (−0.015) due to >96% positive prevalence (Feinstein & Cicchetti 1990).\"\n    resolution_round: 17\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF1: 升级为最关键 Must-Fix。要求全部 88 pairs + 3+ 标注员。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被提出——100-pair annotation 结果已整合(Appendix S, AC₁=0.96)，两位 Reviewer 在 S3 中引用为正面证据。\"\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"三 judge (GPT-4o/Qwen3/Llama-70B) 100-point Likert 全部 NS (p>0.15)，Appendix L 已更新为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF4: FK 作为 GEE 协变量分析完成。Style OR 下降 20-51%，GPT-4o 变 NS。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N2——GPT-4o formality Style OR 在 FK control 下失去显著性(2.70→2.15, p=.132)是 material finding，不应仅附录一句话带过。R2 交叉 AGREE 并补充 mediator vs confounder nuance：如果 FK 是 mediator（formality→FK→judge score），控制 FK 是 over-controlling (bad control)。共识：需在正文讨论，并明确 FK 的因果角色。\"\n    action_items:\n      - round: 17\n        action: \"(1) Section 5.2/5.3 正文讨论 FK-controlled 对 GPT-4o 的影响；(2) 明确讨论 FK 是 mediator 还是 confounder——如果 mediator 则 controlled OR 2.15 是 under-estimate，uncontrolled OR 2.70 更接近真实效应；(3) 给出 GPT-4o Style OR 范围 [2.15, 2.70] 取决于 FK 因果角色\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF3: Limitations 需讨论 22% 作为 lower bound。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Should-Fix W1 再次提出——缺 rule-based rewriter，formality 替代 rewriter 未报告 GEE。R2 交叉 AGREE 但 scope 限定（仅影响 Qwen3-32B）。共识：补充 formality GEE 或讨论 rule-based rewriter 作为 future work。\"\n    action_items:\n      - round: 17\n        action: \"(1) Limitations 讨论 22% 为 lower bound + all alt rewriters 共享 RLHF style preferences；(2) 明确 rule-based rewriter 作为 future work；(3) 理想情况补充 formality alt-rewriter GEE decomposition\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 1 已为 LLMBar-only（4 judges × 2-3 axes），cross-benchmark 在 Appendix Table T。\"\n    resolution_round: 16\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Appendix V 已添加完整 rewriting prompts\"\n    resolution_round: 16\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"全文术语统一：'style sensitivity' 为默认。\"\n    resolution_round: 16\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 2 caption 已展开\"\n    resolution_round: 16\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未提及，camera-ready 前检查。\"\n      - round: 17\n        reviewers: []\n        note: \"R17: R2 建议确认 RATE 和 Comparative Trap 引用是否为最新版本。R1 交叉 NEUTRAL。\"\n\n  # ============================================================\n  # Round 16 issues\n  # ============================================================\n\n  - id: \"R16-W1\"\n    summary: \"Construct divergence 讨论不充分——与 Abstract 三机制并列承诺不匹配\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W4 (Should-Fix): construct divergence 需操作性定义和可检验预测。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: 作为 R15-N1 (Title framing) 的一部分被再次讨论。Section 5.1 已有 construct divergence 展开。两位 Reviewer 均认为现有讨论质量可接受但 Title 与正文仍有张力。\"\n\n  - id: \"R16-W2\"\n    summary: \"Cross-benchmark 'severity spectrum' 解释为 post-hoc rationalization\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W5: 标记为 post-hoc/exploratory。已添加 'Post hoc,' 前缀。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。'Post hoc' 前缀已存在(Section 5.1 p6)。\"\n\n  - id: \"R16-W3\"\n    summary: \"BT 模型 unidimensionality 假设与论文核心论点存在张力\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W7 (Minor): §3.3 已添加 BT unidimensionality + GEE 互补说明。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Section 3.3 末句已存在 BT unidimensionality disclaimer + GEE complement 说明。\"\n\n  - id: \"R16-D1\"\n    summary: \"Appendix L 100pt Likert 数据归属错误（GPT-4o 误标为 Qwen3-32B）\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix L 修正为 GPT-4o 归属，扩展为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R16-D2\"\n    summary: \"Claude LLMBar Likert Table 1 vs Appendix U 数值不一致\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix U 统一为 pole-aligned convention。\"\n    resolution_round: 16\n\n  - id: \"R16-D3\"\n    summary: \"FK analysis artifact 数据源错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"FK 脚本修复为 nli_cf >= 0.90 过滤。\"\n    resolution_round: 16\n\n  - id: \"R16-Q3\"\n    summary: \"Direction-aware gating 额外放入的 21 pairs 是否有系统差异\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Permutation test p=.663, BT% 差 4.7pp (NS)。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1-Q4 提出 DA gate 是否漏过 R→Q。R2 交叉引用 Appendix F 实证验证(permutation p=.663, 5 judges Fisher p>.66)认为风险已充分缓解。\"\n\n  # ============================================================\n  # Round 17 新发现\n  # ============================================================\n\n  - id: \"R17-W1\"\n    summary: \"Cross-benchmark replication 选择性——24 cells 仅填 6 个(25%)，选择最强 cells，可能向上偏倚\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W2 + R2 交叉 AGREE（认为更严重）。Appendix T 第655行自认 'targeting the strongest effects'。主文 Section 5.3 'replicate across benchmarks' 暗示更广泛复制。Gemini 完全缺失于 cross-benchmark。\"\n    action_items:\n      - round: 17\n        action: \"(1) 承认 cross-benchmark 选择性，Section 5.3 修改措辞；(2) 补充至少一个弱信号 cell 或讨论缺失 cells 的影响\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W2\"\n    summary: \"GEE 模型仅含 2 个 predictors (Style, Originality)，omitted variable bias 未讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W1，R1 交叉 AGREE（GEE 目标是 decomposition 而非 causal ID，两个 predictors 足够 parsimonious，但应声明 omitted variable 的可能性）。\"\n    action_items:\n      - round: 17\n        action: \"Section 5.2 或 Limitations 增加 GEE identification assumptions 和 omitted variable disclaimer\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W3\"\n    summary: \"与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分——六项 controls 不能排除 amplification，未量化 amplification factor\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W5，R1 交叉 AGREE。论文承认无法 definitively resolve，但未量化 amplification 的可能范围。Debiased prompting 降 5.7/13.1pp 可被解释为 amplification lower bound 但论文未做此连接。\"\n    action_items:\n      - round: 17\n        action: \"(1) Section 5.4 量化 amplification 可能范围或明确 bounding analysis 局限性；(2) 讨论 amplification-dominant 情景下 practical implications 如何改变\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-M1\"\n    summary: \"Table 1 'n=88 except where noted' 与 verbosity 实际 n=86 不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M1 提出，R2 交叉 AGREE。Appendix L Table 9 标注 n=86。\"\n\n  - id: \"R17-M2\"\n    summary: \"BT choix library 'default regularization' 未说明具体形式和强度\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M5 + R1-Q5 提出，R2 交叉 AGREE。n=88 小样本下 regularization 可能影响 BT 估计。\"\n\n  - id: \"R17-M3\"\n    summary: \"Section 3.1 因果语言——'constitutes a binary intervention' 措辞过强\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W4 提出。R2 交叉 REBUT——操作层面 vs 推断层面不矛盾，但同意措辞可改进为 'approximates' 或 'operationalizes'。\"\n\n  - id: \"R17-M4\"\n    summary: \"Figure 2 (DAG) orange dashed S→Q path 在灰度打印下不可辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M3 + R2-M2 双方独立指出。建议使用不同 line pattern (dash-dot) 或 annotation。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: S4 称 GEE decomposition 是'真正的方法论贡献'——首次获正面评价。但仍认为 GEE 被 undersold。Intro 3 个 LLM-specific distinctions 被认可。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 fresh: R2 列为 Must-Fix N1 (critical)——三个 LLM-specific distinctions 被夸大：(a) per-axis structure 是 IRT 标准现象，(c) binary divergence 被 Figure 4 power analysis 完全解释。R1 交叉部分同意(a)(c)但 REBUT (b)：GEE decomposition 不等同于 factor analysis/SEM，是 LLM judge bias 领域的新分析层。共识：重新定位为 'empirical characterization + novel diagnostic layer'，不过度宣称 'beyond classical framework'。\"\n    action_items:\n      - round: 17\n        action: \"Intro 三个 LLM-specific distinctions 需重新措辞：(a) 'complements' 而非 'surpasses' classical framework；(c) 删除 'sharper than...classical theory predicts' 或改为 'consistent with severe power deficit'；(b) 改为 'not standard practice in LLM judge evaluation' 而非 'absent from classical framework'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 13-16 issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"Table 1 已拆为 LLMBar primary only，cross-benchmark 移至 Appendix T。脚注包含方向不对称信息。\"\n    resolution_round: 16\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及。Related Work RATE 段落已改善。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Related Work 中 RATE 定位被两位 Reviewer 评为'准确且诚实'(R1-S4)。\"\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 M1: Title 仍隐含 Likert 有缺陷。采用 Option C（保持 title + 充实 construct divergence）。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N3 再次提出。R1 交叉 REBUT——'Blindspot' 有操作性定义(Section 1 第5行)，保留 title 但更早 qualify。分歧：R2 要改标题，R1 要保留+更早 qualify。两位均同意 Title 与正文 nuanced discussion 存在张力。\"\n    action_items:\n      - round: 17\n        action: \"保留 Blindspot title，但在 Abstract 第 2-3 行更早引入操作性定义和三种解释的 qualification，使读者不会从标题获得单一方向印象\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF2: 三条 convergent evidence 每条单独仍不足。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N3 系统解构四条证据线——TOST underpowered, MDE=1.56 无法排除 small effect, BF₀₁=0.80 inconclusive, AEval verbosity OR=4.76 直接矛盾。R2 交叉完全 AGREE 并升级严重性。共识：降级为 'lower-sensitivity judge'，Section 5.4 更新描述，AEval verbosity 讨论提升到正文。\"\n    action_items:\n      - round: 17\n        action: \"(1) 全文 'low-sensitivity reference' → 'lower-sensitivity judge' (relative rather than absolute)；(2) Section 5.4 第(ii)项更新为包含 benchmark-dependent qualification；(3) AEval verbosity OR=4.76 讨论从 Limitations 提升到 Section 5.3/5.4；(4) TOST margin 需提供 practical significance 论据\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽，n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF1: 降级为 Should-Fix。Projection 论证足够。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 升级为 Must-Fix N1——Table 2 其他 11 个 n=88 cell 以 face value 呈现，未提供 shrinkage-adjusted 估计。R2 交叉完全 AGREE，补充 CI 宽度证据（GPT-4o verb OR 11.34 [4.93,26.10]）。共识：n=88 OR 应标注为上界估计，提供 projected ranges。\"\n    action_items:\n      - round: 17\n        action: \"(1) Table 2 caption/footnote 明确声明 n=88 OR 为上界估计（Nemes et al. 2009）；(2) 提供 verbosity 的 shrinkage-adjusted projected ORs (4-6.5)；(3) 正文 Section 5.2 更突出地讨论 CI 宽度对解释的影响\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF3: 升级为 Must-Fix。'systematically' 已替换为 'consistently' 在 5 处。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N2——'consistently divergent' 仍过强，基于 2 primary + 1 exploratory axis，且选择了已知 bias-prone 的轴。R1 交叉同意但 qualify：consistency 指 across judges（4/4 成立）而非 across axes。共识：Abstract 需更精确措辞。Gemini formality 异质性应在 Abstract/Conclusion 提及。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 改为 'across two primary and one exploratory style axes, with varying effect sizes across judges (three showing robust effects, one showing weaker, originality-dominated patterns)' 或类似精确措辞\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: \"100-pair annotation (50 formality + 50 verbosity, 70 NLI-pass + 30 NLI-fail): gate pass precision=98.6% (69/70, both annotators concordant), AC₁=0.96. Only 2/70 NLI-pass flagged by either annotator. Gate conservative: 93-100% of NLI-fail also preserve meaning (false rejection dominant). κ paradox (−0.015) due to >96% positive prevalence (Feinstein & Cicchetti 1990).\"\n    resolution_round: 17\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF1: 升级为最关键 Must-Fix。要求全部 88 pairs + 3+ 标注员。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被提出——100-pair annotation 结果已整合(Appendix S, AC₁=0.96)，两位 Reviewer 在 S3 中引用为正面证据。\"\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"三 judge (GPT-4o/Qwen3/Llama-70B) 100-point Likert 全部 NS (p>0.15)，Appendix L 已更新为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF4: FK 作为 GEE 协变量分析完成。Style OR 下降 20-51%，GPT-4o 变 NS。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N2——GPT-4o formality Style OR 在 FK control 下失去显著性(2.70→2.15, p=.132)是 material finding，不应仅附录一句话带过。R2 交叉 AGREE 并补充 mediator vs confounder nuance：如果 FK 是 mediator（formality→FK→judge score），控制 FK 是 over-controlling (bad control)。共识：需在正文讨论，并明确 FK 的因果角色。\"\n    action_items:\n      - round: 17\n        action: \"(1) Section 5.2/5.3 正文讨论 FK-controlled 对 GPT-4o 的影响；(2) 明确讨论 FK 是 mediator 还是 confounder——如果 mediator 则 controlled OR 2.15 是 under-estimate，uncontrolled OR 2.70 更接近真实效应；(3) 给出 GPT-4o Style OR 范围 [2.15, 2.70] 取决于 FK 因果角色\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF3: Limitations 需讨论 22% 作为 lower bound。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Should-Fix W1 再次提出——缺 rule-based rewriter，formality 替代 rewriter 未报告 GEE。R2 交叉 AGREE 但 scope 限定（仅影响 Qwen3-32B）。共识：补充 formality GEE 或讨论 rule-based rewriter 作为 future work。\"\n    action_items:\n      - round: 17\n        action: \"(1) Limitations 讨论 22% 为 lower bound + all alt rewriters 共享 RLHF style preferences；(2) 明确 rule-based rewriter 作为 future work；(3) 理想情况补充 formality alt-rewriter GEE decomposition\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 1 已为 LLMBar-only（4 judges × 2-3 axes），cross-benchmark 在 Appendix Table T。\"\n    resolution_round: 16\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Appendix V 已添加完整 rewriting prompts\"\n    resolution_round: 16\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"全文术语统一：'style sensitivity' 为默认。\"\n    resolution_round: 16\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 2 caption 已展开\"\n    resolution_round: 16\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未提及，camera-ready 前检查。\"\n      - round: 17\n        reviewers: []\n        note: \"R17: R2 建议确认 RATE 和 Comparative Trap 引用是否为最新版本。R1 交叉 NEUTRAL。\"\n\n  # ============================================================\n  # Round 16 issues\n  # ============================================================\n\n  - id: \"R16-W1\"\n    summary: \"Construct divergence 讨论不充分——与 Abstract 三机制并列承诺不匹配\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W4 (Should-Fix): construct divergence 需操作性定义和可检验预测。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: 作为 R15-N1 (Title framing) 的一部分被再次讨论。Section 5.1 已有 construct divergence 展开。两位 Reviewer 均认为现有讨论质量可接受但 Title 与正文仍有张力。\"\n\n  - id: \"R16-W2\"\n    summary: \"Cross-benchmark 'severity spectrum' 解释为 post-hoc rationalization\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W5: 标记为 post-hoc/exploratory。已添加 'Post hoc,' 前缀。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。'Post hoc' 前缀已存在(Section 5.1 p6)。\"\n\n  - id: \"R16-W3\"\n    summary: \"BT 模型 unidimensionality 假设与论文核心论点存在张力\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W7 (Minor): §3.3 已添加 BT unidimensionality + GEE 互补说明。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Section 3.3 末句已存在 BT unidimensionality disclaimer + GEE complement 说明。\"\n\n  - id: \"R16-D1\"\n    summary: \"Appendix L 100pt Likert 数据归属错误（GPT-4o 误标为 Qwen3-32B）\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix L 修正为 GPT-4o 归属，扩展为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R16-D2\"\n    summary: \"Claude LLMBar Likert Table 1 vs Appendix U 数值不一致\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix U 统一为 pole-aligned convention。\"\n    resolution_round: 16\n\n  - id: \"R16-D3\"\n    summary: \"FK analysis artifact 数据源错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"FK 脚本修复为 nli_cf >= 0.90 过滤。\"\n    resolution_round: 16\n\n  - id: \"R16-Q3\"\n    summary: \"Direction-aware gating 额外放入的 21 pairs 是否有系统差异\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Permutation test p=.663, BT% 差 4.7pp (NS)。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1-Q4 提出 DA gate 是否漏过 R→Q。R2 交叉引用 Appendix F 实证验证(permutation p=.663, 5 judges Fisher p>.66)认为风险已充分缓解。\"\n\n  # ============================================================\n  # Round 17 新发现\n  # ============================================================\n\n  - id: \"R17-W1\"\n    summary: \"Cross-benchmark replication 选择性——24 cells 仅填 6 个(25%)，选择最强 cells，可能向上偏倚\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W2 + R2 交叉 AGREE（认为更严重）。Appendix T 第655行自认 'targeting the strongest effects'。主文 Section 5.3 'replicate across benchmarks' 暗示更广泛复制。Gemini 完全缺失于 cross-benchmark。\"\n    action_items:\n      - round: 17\n        action: \"(1) 承认 cross-benchmark 选择性，Section 5.3 修改措辞；(2) 补充至少一个弱信号 cell 或讨论缺失 cells 的影响\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W2\"\n    summary: \"GEE 模型仅含 2 个 predictors (Style, Originality)，omitted variable bias 未讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W1，R1 交叉 AGREE（GEE 目标是 decomposition 而非 causal ID，两个 predictors 足够 parsimonious，但应声明 omitted variable 的可能性）。\"\n    action_items:\n      - round: 17\n        action: \"Section 5.2 或 Limitations 增加 GEE identification assumptions 和 omitted variable disclaimer\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W3\"\n    summary: \"与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分——六项 controls 不能排除 amplification，未量化 amplification factor\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W5，R1 交叉 AGREE。论文承认无法 definitively resolve，但未量化 amplification 的可能范围。Debiased prompting 降 5.7/13.1pp 可被解释为 amplification lower bound 但论文未做此连接。\"\n    action_items:\n      - round: 17\n        action: \"(1) Section 5.4 量化 amplification 可能范围或明确 bounding analysis 局限性；(2) 讨论 amplification-dominant 情景下 practical implications 如何改变\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-M1\"\n    summary: \"Table 1 'n=88 except where noted' 与 verbosity 实际 n=86 不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M1 提出，R2 交叉 AGREE。Appendix L Table 9 标注 n=86。\"\n\n  - id: \"R17-M2\"\n    summary: \"BT choix library 'default regularization' 未说明具体形式和强度\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M5 + R1-Q5 提出，R2 交叉 AGREE。n=88 小样本下 regularization 可能影响 BT 估计。\"\n\n  - id: \"R17-M3\"\n    summary: \"Section 3.1 因果语言——'constitutes a binary intervention' 措辞过强\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W4 提出。R2 交叉 REBUT——操作层面 vs 推断层面不矛盾，但同意措辞可改进为 'approximates' 或 'operationalizes'。\"\n\n  - id: \"R17-M4\"\n    summary: \"Figure 2 (DAG) orange dashed S→Q path 在灰度打印下不可辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M3 + R2-M2 双方独立指出。建议使用不同 line pattern (dash-dot) 或 annotation。\""
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-23T09:07:43.935342+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 22879}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-23T09:10:59.440251+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Reviewers**: R1 (方法严谨性/统计框架/实验设计) + R2 (新颖性/完整性/写作质量)\n**日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，通过 NLI-gated content control、per-axis style decomposition 和 position-controlled pairwise comparison 量化 LLM judge 对表层风格特征的敏感度。核心发现为 Likert Blindspot：在相同数据上，pairwise comparison 检测到统计显著的风格偏好（BT 63–77%, p < 0.001），而 Likert scoring 在所有七种统计方法下均失败（p > 0.17）。GEE conditional decomposition 揭示了 per-axis 的 confound structure 差异：verbosity 为 style-dominated (Style OR 8–13)，formality 为 conditional effect。实验覆盖 4 个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个 low-sensitivity reference（Claude Sonnet 4）、3 个 benchmark、2 个 primary + 1 个 exploratory style axis。\n\n---\n\n## Strengths\n\n**S1. 核心定性发现扎实且有实践意义** [AGREE: R1, R2]\nLikert Blindspot 在 4 judges × 2 primary axes × 3 benchmarks 上复现。n=355 scaled replication 证实 Likert d→0 是结构性衰减而非 power 不足。七种统计方法的一致性排除 test-specific artifact。对依赖 Likert ATE 的框架（如 RATE）有直接校正价值。\n\n**S2. GEE per-axis decomposition 是真正的方法论贡献** [AGREE: R1, R2]\n将 aggregate BT preference 拆解为 Style OR 和 Originality OR 揭示了 per-axis 质性差异（verbosity style-dominated vs formality conditional），是该领域新的诊断层。Claude 在 AEval 的 case（aggregate BT ~70% 但 Style OR n.s., Orig OR 9–12）示范了为什么 aggregate BT 不足以归因 bias。R1 和 R2 在交叉回应中就 GEE 是否为\"纯工程贡献\"存在分歧（见 Divergence），但均认可其实用诊断价值。\n\n**S3. 实验设计的 transparency 和 self-correction 罕见地好** [AGREE: R1, R2]\nn=355 replication 主动暴露 49% OR 缩水；三种 Blindspot 解释的 agnostic framing；100-pair human annotation（AC₁=0.96）；NLI threshold sweep（≤3pp variation）。R2 特别指出 Limitations 章节\"几乎没有 reviewer 需要补充的未提及限制\"——在 NLP 论文中非常少见。\n\n**S4. Related Work 覆盖全面且定位准确** [AGREE: R1, R2]\n对 RATE 的分析基于实证而非稻草人；对 Comparative Trap 的直接回应承认 format amplification 的可能性。\n\n**S5. 统计方法论透明** [AGREE: R1, R2]\nFWER 控制、exploratory vs confirmatory 分类、GEE model diagnostics（correlation structure robustness, interaction tests）、bootstrap CI 计算细节充分。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [AGREE: R1, R2] n=88 的 GEE OR 系统性膨胀（~50%）未传播到主要结论**\n- Qwen3-32B formality Style OR 从 4.20 (n=88) 缩水至 2.15 (n=355)，-49%。Table 2 其他 11 个 n=88 cell 以 face value 呈现。Verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5——论文做了文字推演但未提供 shrinkage-adjusted 估计。CI 极宽（如 GPT-4o verbosity 11.34 [4.93, 26.10]）。\n- **Action**: (1) Table 2 caption 明确标注 n=88 OR 为上界估计；(2) 提供 verbosity shrinkage-adjusted projected ORs；(3) 更突出展示 CIs。\n\n**MF2. [AGREE: R1, R2] GPT-4o formality Style OR 在 FK readability control 下失去显著性（p=.132）**\n- GPT-4o 是论文叙事的锚点 judge（Intro opening example, Table 1 第一行）。FK grade 作为 GEE 协变量后 Style OR 从 2.70→2.15 (p=.132)，仅在 Appendix 一段话带过。Qwen3 (p=.014) 和 Llama-70B (p=.037) 仍显著。\n- **关键 nuance**（R2 补充，R1 同意）：FK grade 可能是 mediator（formality→FK→judge score）而非 confounder。如果是 mediator，控制 FK 是 over-controlling (bad control, Pearl 2009)，true effect 在 [2.15, 2.70] 之间。论文的 DAG (Figure 2) 没有 FK 中介节点——需明确立场。\n- **Action**: (1) Section 5.2/5.3 正文讨论；(2) 明确 mediator vs confounder 论据；(3) 给出 GPT-4o Style OR 范围。\n\n**MF3. [AGREE: R1, R2] Claude \"low-sensitivity reference\" 证据链每条单独不成立，且 AEval verbosity 直接矛盾**\n- 四条 convergent evidence 逐一审视：(i) TOST 在 Δ=10pp underpowered (power ~42%); (ii) GEE MDE=1.56 无法排除 small effects; (iii) Bayesian BF₀₁=0.80 inconclusive; (iv) AEval verbosity Style OR=4.76 (p<.001) 与 \"low-sensitivity\" 标签直接矛盾。Section 5.4 第(ii)项 \"(Claude low-sensitivity reference (Style OR n.s.))\" 选择性引用 LLMBar formality。\n- **Action**: (1) 降级为 \"lower-sensitivity judge\" (relative, benchmark-dependent); (2) 更新 Section 5.4 描述; (3) AEval verbosity OR=4.76 讨论提升到正文。\n\n**MF4. [AGREE: R1(qualified), R2] 新颖性定位过度宣称——三个 \"LLM-specific distinctions\" 中 (a) 和 (c) 被经典框架解释**\n- (a) Per-axis structure: 经典 IRT 中 item-level discriminability variation 是标准现象。\n- (c) Binary divergence: Figure 4 power analysis 完全解释（Likert power < 20% 时 binary failure 是经典预测）。\n- (b) GEE source decomposition: R1 REBUT R2——GEE 在 LLM judge bias 领域确实是新的分析层（prior work 均未做 per-axis confound decomposition），不等同于 factor analysis/SEM（见 Reviewer Divergence）。\n- **Action**: (a) \"complements\" 而非 \"surpasses\" classical framework; (c) 删除 \"sharper than classical theory predicts\"; (b) \"not standard practice in LLM judge evaluation\" 而非 \"absent from classical framework\"。\n\n**MF5. [AGREE: R1(qualified), R2] \"Consistently divergent\" claim 过强**\n- 仅 2 primary + 1 exploratory axis，选择了已知 bias-prone 的轴（formality, verbosity）。Gemini formality 明显较弱（Style OR 1.64, n.s., BT 57.4%）。Abstract/Conclusion 的 \"across four judges\" 未 qualify Gemini 的异质性。\n- R1 nuance: \"consistently\" 修饰的是 across judges（4/4 target judges 在 formality/verbosity 上均显示 Blindspot），这是成立的。但 axis coverage 不足。\n- **Action**: Abstract 改为更精确措辞（如 \"across two primary and one exploratory style axes, with varying effect sizes across judges\"）。\n\n**MF6. [DIVERGENCE: R2 AGREE, R1 partial REBUT] Title \"Blindspot\" 预设 Likert attenuation 解释**\n- \"Blindspot\" 语义预设 Likert 遗漏真实信号。在 pairwise amplification 或 construct divergence 下，Likert 没有 \"盲点\"。Title/Conclusion 偏向 attenuation 解释。\n- R1 REBUT: \"Blindspot\" 有操作性定义（Section 1 第5行），保留标题但更早 qualify。\n- **Action**: 见 Reviewer Divergence。建议保留 Title 但在 Abstract 第 2–3 行更早引入操作性定义和三种解释的 qualification。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [AGREE: R1, R2] Evaluator-producer overlap 仅用一个替代 rewriter 验证**\n- Qwen3-32B rewriter=judge overlap 仅用 GPT-4o 验证（verbosity OR 降 22%, formality BT 降 2.1pp）。缺 rule-based rewriter。Formality 替代 rewriter 未报告 GEE。仅影响 Qwen3-32B（其他 3 judges 使用独立 rewriter）。\n- **Action**: Limitations 讨论 22% 为 lower bound; rule-based rewriter 作为 future work; 理想情况补充 formality alt-rewriter GEE。\n\n**SF2. [AGREE: R1, R2(升级)] Cross-benchmark replication 选择性——24 cells 仅填 6 个**\n- Appendix T 自认 \"targeting the strongest effects\"。主文 \"replicate across benchmarks\" 暗示更广泛复制。Gemini 完全缺失。两个 ‡ rows（both BT and Likert significant）实际削弱 Blindspot claim。\n- **Action**: 承认选择性；补充弱信号 cell 或讨论缺失影响。\n\n**SF3. [AGREE: R1, R2] TOST equivalence margin 缺乏先验依据**\n- 5 个 margin 测试无 a priori justification。12pp 作为 headline result 是 post-hoc 选择。应基于 SESOI（smallest effect size of interest）。\n- **Action**: 提供 practical significance 论据（如 RLHF downstream impact）。\n\n**SF4. [AGREE: R1, R2] GEE 模型仅含 2 个 predictors，omitted variable bias 未讨论**\n- 可能遗漏 text length, lexical complexity, topic domain 等。GEE 目标是 decomposition 而非 causal ID，两个 predictors 足够 parsimonious，但应声明假设。\n- **Action**: Section 5.2 或 Limitations 增加 identification assumptions disclaimer。\n\n**SF5. [AGREE: R1, R2] 与 Comparative Trap 的关系处理不够——未量化 amplification factor**\n- 六项 controls \"bound\" 但不能 \"exclude\" amplification。论文承认无法 definitively resolve，但未量化 amplification 可能范围。Debiased prompting 降 5.7/13.1pp 可解释为 amplification lower bound，但论文未做此连接。\n- **Action**: 量化 amplification 范围或明确 bounding analysis 局限性；讨论 amplification-dominant 情景下的 practical implications。\n\n### Minor（不影响接收）\n\n- **m1**: Table 1 \"n=88 except where noted\" 与 verbosity 实际 n=86 不一致 [AGREE: R1, R2]\n- **m2**: Figure 2 DAG orange dashed S→Q path 灰度打印不可辨 [AGREE: R1, R2]\n- **m3**: BT `choix` library \"default regularization\" 未说明具体形式 [AGREE: R1, R2]\n- **m4**: Section 3.1 \"constitutes a binary intervention\" 建议改为 \"approximates\" [R1 AGREE, R2 partial REBUT]\n- **m5**: Appendix Table 3 QIC 值显示 \"---\" 无实际数值 [AGREE: R1, R2]\n- **m6**: Abstract GEE 描述对不熟悉 GEE 的读者不友好 [R2 提出]\n- **m7**: Section 2 RLHF format-specific biases 段落（3 行）未充分发展 [R2 提出, R1 AGREE]\n- **m8**: Rewriting temperature 0.7 无选择依据 [R2 提出, R1 AGREE]\n- **m9**: Tone axis pilot 应在 Method 中提及 CSD scope boundary [R2 提出, R1 AGREE]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全共识：\n\n1. **核心定性发现扎实**：Likert Blindspot 作为现象存在，跨 4 judges、3 benchmarks 复现。\n2. **GEE decomposition 有诊断价值**：per-axis confound structure（verbosity style-dominated vs formality conditional）是有信息量的发现。\n3. **定量 claims 需要 tightening**：n=88 OR 膨胀、GPT-4o FK control、Claude reference 矛盾——这三个问题均可通过文字修改和补充分析解决，不需要新实验。\n4. **新颖性需重新定位**：从 \"beyond classical framework\" 降级为 \"empirical characterization in a new domain + novel diagnostic layer\"。\n5. **\"Consistently divergent\" 需 qualify**：axis coverage（2+1）和 Gemini 异质性应在 Abstract/Conclusion 明确。\n6. **Comparative Trap 的关系需加强**：amplification 不可排除，bounding analysis 有局限性。\n\n---\n\n## Reviewer Divergence\n\n**D1. Title \"Blindspot\"（R2-N3 vs R1 反驳）**\n- **R2**: \"Blindspot\" 预设 attenuation 解释，建议改为中性标题（如 \"Measurement-Mode Divergence\" 或 \"The Likert-Pairwise Gap\"）。\n- **R1**: \"Blindspot\" 有操作性定义（Section 1 第5行），学术传播需要 memorable label；建议保留但在 Abstract 更早 qualify。\n- **Director 判断**: 两位均同意 Title 与正文 nuanced discussion 存在张力。分歧在于解决方案（改标题 vs 更早 qualify）。建议采用 R1 方案（保留 Title + 更早 qualify），因为 (a) \"Blindspot\" 已在论文中被操作性定义，(b) 正文充分讨论了三种竞争解释，(c) 标题的 communicative value 不应被牺牲——但前提是 Abstract 前 2–3 行必须同时引入操作性定义和 amplification/construct divergence 解释。\n\n**D2. GEE decomposition 的新颖性级别（R2-N1b vs R1 反驳）**\n- **R2**: GEE 是成熟统计工具，应用于 style/quality 分解是工程贡献，经典 factor analysis/SEM 承担类似功能。Excitement 3/5。\n- **R1**: GEE 在此处的目标（binary outcome 下分离 observed predictors 的条件贡献）与 factor analysis/SEM（latent variable modeling）不同。Prior work（RATE, FairJudge, CASSE）均未做 per-axis confound decomposition。不是纯工程贡献。Excitement 3.5/5。\n- **Director 判断**: R1 的反驳有技术依据——GEE conditional decomposition 确实与 FA/SEM 的目标和结构不同。但 R2 的更广泛观点（GEE 本身不是新方法）也成立。论文应将 GEE 定位为 \"novel application of established statistical tool to a problem that prior work has not addressed\"，而非 \"methodological innovation absent from classical framework\"。\n\n**D3. 信息密度（R2-W3 vs R1 反驳）**\n- **R2**: 8 页承载过多维度，核心 narrative 被稀释。建议将 7 种统计方法、TOST、Bayesian equivalence 全部移至附录。\n- **R1**: 论文的信息分层（正文核心 + 13 页 Appendix）是恰当的。核心 narrative 的逻辑链清晰。\n- **Director 判断**: 采用 R1 观点。对于 empirical methodology 论文，主文需同时呈现方法、主要发现和 robustness evidence。当前分层合理。但 Section 5.1 的单个段落确实过于密集（TOST + GEE + BF₀₁ 同时出现），建议拆分为更小的段落以提高可读性。\n\n---\n\n## Questions to Authors\n\n1. **[R1-Q1, R2-Q3, 共识]** Verbosity axis 做 n=355 scaled replication 后，Style OR（当前 8–13）预期缩水多少？是否改变 style-dominated 的 regime classification？这是最重要的 missing experiment。\n2. **[R1-Q2, R2 补充, 共识]** FK grade 在 formality 中是 mediator 还是 confounder？请提供 DAG 层面的论据。如果是 mediator，GPT-4o Style OR [2.15, 2.70] 中哪个端点更接近 true effect？\n3. **[R1-Q3, R2-W2, 共识]** AEval verbosity 上 Claude Style OR=4.76 (p<.001) 如何调和 \"low-sensitivity reference\"？是否有 AEval 数据分布的特殊性解释？\n4. **[R2-Q1, R1 支持]** 如果 pairwise amplification 是主要机制（而非 Likert attenuation），论文的 practical implications 如何改变？\"添加 pairwise 模式\" 的建议是否反而引入 false positives？\n5. **[R2-Q2, R1 支持]** 为什么不包含 human evaluation 来 ground-truth 两种测量模式？论文多次提到这是 \"the key next step\"——缺乏解释为什么当前工作没有做。\n6. **[R2-Q4]** Verbosity FK grade d=0.50 的 60% mediation by sentence length——这是否意味着 verbosity \"style bias\" 部分是 readability bias？\n\n---\n\n## Missing References\n\nR2 建议补充：\n1. Kocmi & Federmann (2023) — GEMBA: Using GPT Models for Reference-Free MT Evaluation（涉及 Likert vs pairwise 比较）\n2. 确认 Reber et al. (2025) RATE 和 Jeong et al. (2025) Comparative Trap 引用是否为最新版本（arXiv preprint 可能已被接收）\n\nR1 对此评价 NEUTRAL——相关性有限，建议 authors 自行判断。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: error — 视觉审查 Agent 因 API 限额耗尽而失败（\"You've hit your limit · resets May 25, 8am UTC\"）。无法完成 PDF 渲染和排版检查。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n**Overall: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 4.0 | 3.75 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n### 置信度\n4 / 5 — 两位 Reviewer 均有高置信度（4/5），核心判断一致。\n\n### 评分理由\n\n**支持接收的因素**：\n- 核心定性发现（Likert Blindspot）在 4 judges × 3 benchmarks 上有可靠复现\n- GEE per-axis decomposition 是该领域的真正方法论推进\n- 实验设计的严谨程度和 self-correction 的透明度明显高于同领域平均水平\n- Limitations 章节异常全面诚实\n- 对 RLHF/DPO pipeline 的 style bias audit 有直接实践指导价值\n\n**阻碍给出 4.0（Conference）的因素**：\n- 核心发现是 Thurstone (1927) 以来经典结论的 domain transfer，新颖性定位有过度宣称\n- 定量估计（GEE OR）受 n=88 小样本偏差系统性影响（~50%），且仅一个 cell 有 scaled validation\n- Claude negative control 证据链每条单独不成立，AEval verbosity 直接矛盾\n- GPT-4o formality——论文锚点——在 FK readability control 下失去显著性\n- 无法区分 attenuation 和 amplification 是根本限制，且 Title \"Blindspot\" 与此不一致\n\n### 改进路径\n\n如果 authors 能在 rebuttal/revision 中：\n1. 重新定位新颖性（\"empirical characterization + novel diagnostic layer\" 而非 \"beyond classical framework\"）\n2. 标注 n=88 OR 为上界估计并提供 projected ranges\n3. 正文讨论 GPT-4o FK control 结果及 mediator/confounder 分析\n4. 降级 Claude 为 \"lower-sensitivity judge\"，更新 Section 5.4\n5. Qualify \"consistently divergent\" 的 axis coverage 和 Gemini 异质性\n\n评分可提升至 **4.0 (Conference)** 或至少 **3.5+ (strong Findings)**。上述修改均为文字调整和框架重组，不需要新实验。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息密集但关键数字准确。需更早引入 \"Blindspot\" 的操作性定义和三种竞争解释。\"consistently divergent sensitivity across tested surface-level style axes\" 需 qualify（2 primary + 1 exploratory）。\n\n**Introduction**: Opening example 有 pedagogical value 但是 cherry-picked 的单个 instance。三个 \"LLM-specific distinctions\" 中 (a) 和 (c) 的新颖性宣称需要降级。Power analysis 引用（\"4–206× the sample size\"）是 illustrative 的，不应暗示 post-hoc power 是 primary evidence。\n\n**Related Work**: 覆盖全面且组织有序。对 RATE 的定位基于实证（\"vulnerability\"）是恰当的。最后一段 RLHF format-specific biases 论点有趣但未充分发展——这是一个 underexploited motivation。\n\n**Method (Section 3)**: NLI gate 的 direction-aware 设计（verbosity expansion 只检查 backward entailment）有技术创意。DAG (Figure 2) 清晰但灰度打印时 orange dashed line 不可辨。Section 3.1 \"constitutes a binary intervention\" 建议改为 \"approximates\"。Section 3.5 Design Rationale 的因果 disclaimer 恰当。\n\n**Experiments (Section 4)**: 统计框架（Section 4.1）的 FWER 控制和 exploratory/confirmatory 分类是 good practice。Table 1 清晰但 \"n=88 except where noted\" 与 verbosity n=86 不一致。Forest plot (Figure 3) 有效传达了跨 judge 模式。\n\n**Analysis (Section 5)**: 最密集的部分。Section 5.1 的三种解释讨论是 genuinely agnostic，但单个段落内 TOST + GEE + BF₀₁ 过密。Section 5.2 GEE decomposition 是论文最强的分析贡献——Table 2 的 verbosity vs formality 对比清晰有力。Section 5.3 cross-judge replication 扎实但 \"replicate across benchmarks\" (Section 5.3 第157行) 对选择性 replication 不够诚实。Section 5.4 六项 amplification controls 是 good-faith bounding 但不构成 exclusion。\n\n**Conclusion**: 简洁恰当。\"single-format audits risk systematic blind spots\" 仍偏向 attenuation 解释——在 amplification-dominant 情景下这条建议可能引入 false positives。\n\n**Limitations**: 异常全面——quality-style confounding, evaluator-producer bias, scope boundaries, validation methodology 均有讨论。两位 Reviewer 几乎没有需要补充的遗漏限制。\n\n**Appendix**: 13 页附录覆盖了所有 robustness checks、diagnostics、和 sensitivity analyses。组织合理（A*–V）。Table 3 的 QIC \"---\" 应补充实际数值。",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 17 (Fresh Review)\n\n**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Reviewers**: R1 (方法严谨性/统计框架/实验设计) + R2 (新颖性/完整性/写作质量)\n**日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，通过 NLI-gated content control、per-axis style decomposition 和 position-controlled pairwise comparison 量化 LLM judge 对表层风格特征的敏感度。核心发现为 Likert Blindspot：在相同数据上，pairwise comparison 检测到统计显著的风格偏好（BT 63–77%, p < 0.001），而 Likert scoring 在所有七种统计方法下均失败（p > 0.17）。GEE conditional decomposition 揭示了 per-axis 的 confound structure 差异：verbosity 为 style-dominated (Style OR 8–13)，formality 为 conditional effect。实验覆盖 4 个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个 low-sensitivity reference（Claude Sonnet 4）、3 个 benchmark、2 个 primary + 1 个 exploratory style axis。\n\n---\n\n## Strengths\n\n**S1. 核心定性发现扎实且有实践意义** [AGREE: R1, R2]\nLikert Blindspot 在 4 judges × 2 primary axes × 3 benchmarks 上复现。n=355 scaled replication 证实 Likert d→0 是结构性衰减而非 power 不足。七种统计方法的一致性排除 test-specific artifact。对依赖 Likert ATE 的框架（如 RATE）有直接校正价值。\n\n**S2. GEE per-axis decomposition 是真正的方法论贡献** [AGREE: R1, R2]\n将 aggregate BT preference 拆解为 Style OR 和 Originality OR 揭示了 per-axis 质性差异（verbosity style-dominated vs formality conditional），是该领域新的诊断层。Claude 在 AEval 的 case（aggregate BT ~70% 但 Style OR n.s., Orig OR 9–12）示范了为什么 aggregate BT 不足以归因 bias。R1 和 R2 在交叉回应中就 GEE 是否为\"纯工程贡献\"存在分歧（见 Divergence），但均认可其实用诊断价值。\n\n**S3. 实验设计的 transparency 和 self-correction 罕见地好** [AGREE: R1, R2]\nn=355 replication 主动暴露 49% OR 缩水；三种 Blindspot 解释的 agnostic framing；100-pair human annotation（AC₁=0.96）；NLI threshold sweep（≤3pp variation）。R2 特别指出 Limitations 章节\"几乎没有 reviewer 需要补充的未提及限制\"——在 NLP 论文中非常少见。\n\n**S4. Related Work 覆盖全面且定位准确** [AGREE: R1, R2]\n对 RATE 的分析基于实证而非稻草人；对 Comparative Trap 的直接回应承认 format amplification 的可能性。\n\n**S5. 统计方法论透明** [AGREE: R1, R2]\nFWER 控制、exploratory vs confirmatory 分类、GEE model diagnostics（correlation structure robustness, interaction tests）、bootstrap CI 计算细节充分。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [AGREE: R1, R2] n=88 的 GEE OR 系统性膨胀（~50%）未传播到主要结论**\n- Qwen3-32B formality Style OR 从 4.20 (n=88) 缩水至 2.15 (n=355)，-49%。Table 2 其他 11 个 n=88 cell 以 face value 呈现。Verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5——论文做了文字推演但未提供 shrinkage-adjusted 估计。CI 极宽（如 GPT-4o verbosity 11.34 [4.93, 26.10]）。\n- **Action**: (1) Table 2 caption 明确标注 n=88 OR 为上界估计；(2) 提供 verbosity shrinkage-adjusted projected ORs；(3) 更突出展示 CIs。\n\n**MF2. [AGREE: R1, R2] GPT-4o formality Style OR 在 FK readability control 下失去显著性（p=.132）**\n- GPT-4o 是论文叙事的锚点 judge（Intro opening example, Table 1 第一行）。FK grade 作为 GEE 协变量后 Style OR 从 2.70→2.15 (p=.132)，仅在 Appendix 一段话带过。Qwen3 (p=.014) 和 Llama-70B (p=.037) 仍显著。\n- **关键 nuance**（R2 补充，R1 同意）：FK grade 可能是 mediator（formality→FK→judge score）而非 confounder。如果是 mediator，控制 FK 是 over-controlling (bad control, Pearl 2009)，true effect 在 [2.15, 2.70] 之间。论文的 DAG (Figure 2) 没有 FK 中介节点——需明确立场。\n- **Action**: (1) Section 5.2/5.3 正文讨论；(2) 明确 mediator vs confounder 论据；(3) 给出 GPT-4o Style OR 范围。\n\n**MF3. [AGREE: R1, R2] Claude \"low-sensitivity reference\" 证据链每条单独不成立，且 AEval verbosity 直接矛盾**\n- 四条 convergent evidence 逐一审视：(i) TOST 在 Δ=10pp underpowered (power ~42%); (ii) GEE MDE=1.56 无法排除 small effects; (iii) Bayesian BF₀₁=0.80 inconclusive; (iv) AEval verbosity Style OR=4.76 (p<.001) 与 \"low-sensitivity\" 标签直接矛盾。Section 5.4 第(ii)项 \"(Claude low-sensitivity reference (Style OR n.s.))\" 选择性引用 LLMBar formality。\n- **Action**: (1) 降级为 \"lower-sensitivity judge\" (relative, benchmark-dependent); (2) 更新 Section 5.4 描述; (3) AEval verbosity OR=4.76 讨论提升到正文。\n\n**MF4. [AGREE: R1(qualified), R2] 新颖性定位过度宣称——三个 \"LLM-specific distinctions\" 中 (a) 和 (c) 被经典框架解释**\n- (a) Per-axis structure: 经典 IRT 中 item-level discriminability variation 是标准现象。\n- (c) Binary divergence: Figure 4 power analysis 完全解释（Likert power < 20% 时 binary failure 是经典预测）。\n- (b) GEE source decomposition: R1 REBUT R2——GEE 在 LLM judge bias 领域确实是新的分析层（prior work 均未做 per-axis confound decomposition），不等同于 factor analysis/SEM（见 Reviewer Divergence）。\n- **Action**: (a) \"complements\" 而非 \"surpasses\" classical framework; (c) 删除 \"sharper than classical theory predicts\"; (b) \"not standard practice in LLM judge evaluation\" 而非 \"absent from classical framework\"。\n\n**MF5. [AGREE: R1(qualified), R2] \"Consistently divergent\" claim 过强**\n- 仅 2 primary + 1 exploratory axis，选择了已知 bias-prone 的轴（formality, verbosity）。Gemini formality 明显较弱（Style OR 1.64, n.s., BT 57.4%）。Abstract/Conclusion 的 \"across four judges\" 未 qualify Gemini 的异质性。\n- R1 nuance: \"consistently\" 修饰的是 across judges（4/4 target judges 在 formality/verbosity 上均显示 Blindspot），这是成立的。但 axis coverage 不足。\n- **Action**: Abstract 改为更精确措辞（如 \"across two primary and one exploratory style axes, with varying effect sizes across judges\"）。\n\n**MF6. [DIVERGENCE: R2 AGREE, R1 partial REBUT] Title \"Blindspot\" 预设 Likert attenuation 解释**\n- \"Blindspot\" 语义预设 Likert 遗漏真实信号。在 pairwise amplification 或 construct divergence 下，Likert 没有 \"盲点\"。Title/Conclusion 偏向 attenuation 解释。\n- R1 REBUT: \"Blindspot\" 有操作性定义（Section 1 第5行），保留标题但更早 qualify。\n- **Action**: 见 Reviewer Divergence。建议保留 Title 但在 Abstract 第 2–3 行更早引入操作性定义和三种解释的 qualification。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [AGREE: R1, R2] Evaluator-producer overlap 仅用一个替代 rewriter 验证**\n- Qwen3-32B rewriter=judge overlap 仅用 GPT-4o 验证（verbosity OR 降 22%, formality BT 降 2.1pp）。缺 rule-based rewriter。Formality 替代 rewriter 未报告 GEE。仅影响 Qwen3-32B（其他 3 judges 使用独立 rewriter）。\n- **Action**: Limitations 讨论 22% 为 lower bound; rule-based rewriter 作为 future work; 理想情况补充 formality alt-rewriter GEE。\n\n**SF2. [AGREE: R1, R2(升级)] Cross-benchmark replication 选择性——24 cells 仅填 6 个**\n- Appendix T 自认 \"targeting the strongest effects\"。主文 \"replicate across benchmarks\" 暗示更广泛复制。Gemini 完全缺失。两个 ‡ rows（both BT and Likert significant）实际削弱 Blindspot claim。\n- **Action**: 承认选择性；补充弱信号 cell 或讨论缺失影响。\n\n**SF3. [AGREE: R1, R2] TOST equivalence margin 缺乏先验依据**\n- 5 个 margin 测试无 a priori justification。12pp 作为 headline result 是 post-hoc 选择。应基于 SESOI（smallest effect size of interest）。\n- **Action**: 提供 practical significance 论据（如 RLHF downstream impact）。\n\n**SF4. [AGREE: R1, R2] GEE 模型仅含 2 个 predictors，omitted variable bias 未讨论**\n- 可能遗漏 text length, lexical complexity, topic domain 等。GEE 目标是 decomposition 而非 causal ID，两个 predictors 足够 parsimonious，但应声明假设。\n- **Action**: Section 5.2 或 Limitations 增加 identification assumptions disclaimer。\n\n**SF5. [AGREE: R1, R2] 与 Comparative Trap 的关系处理不够——未量化 amplification factor**\n- 六项 controls \"bound\" 但不能 \"exclude\" amplification。论文承认无法 definitively resolve，但未量化 amplification 可能范围。Debiased prompting 降 5.7/13.1pp 可解释为 amplification lower bound，但论文未做此连接。\n- **Action**: 量化 amplification 范围或明确 bounding analysis 局限性；讨论 amplification-dominant 情景下的 practical implications。\n\n### Minor（不影响接收）\n\n- **m1**: Table 1 \"n=88 except where noted\" 与 verbosity 实际 n=86 不一致 [AGREE: R1, R2]\n- **m2**: Figure 2 DAG orange dashed S→Q path 灰度打印不可辨 [AGREE: R1, R2]\n- **m3**: BT `choix` library \"default regularization\" 未说明具体形式 [AGREE: R1, R2]\n- **m4**: Section 3.1 \"constitutes a binary intervention\" 建议改为 \"approximates\" [R1 AGREE, R2 partial REBUT]\n- **m5**: Appendix Table 3 QIC 值显示 \"---\" 无实际数值 [AGREE: R1, R2]\n- **m6**: Abstract GEE 描述对不熟悉 GEE 的读者不友好 [R2 提出]\n- **m7**: Section 2 RLHF format-specific biases 段落（3 行）未充分发展 [R2 提出, R1 AGREE]\n- **m8**: Rewriting temperature 0.7 无选择依据 [R2 提出, R1 AGREE]\n- **m9**: Tone axis pilot 应在 Method 中提及 CSD scope boundary [R2 提出, R1 AGREE]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全共识：\n\n1. **核心定性发现扎实**：Likert Blindspot 作为现象存在，跨 4 judges、3 benchmarks 复现。\n2. **GEE decomposition 有诊断价值**：per-axis confound structure（verbosity style-dominated vs formality conditional）是有信息量的发现。\n3. **定量 claims 需要 tightening**：n=88 OR 膨胀、GPT-4o FK control、Claude reference 矛盾——这三个问题均可通过文字修改和补充分析解决，不需要新实验。\n4. **新颖性需重新定位**：从 \"beyond classical framework\" 降级为 \"empirical characterization in a new domain + novel diagnostic layer\"。\n5. **\"Consistently divergent\" 需 qualify**：axis coverage（2+1）和 Gemini 异质性应在 Abstract/Conclusion 明确。\n6. **Comparative Trap 的关系需加强**：amplification 不可排除，bounding analysis 有局限性。\n\n---\n\n## Reviewer Divergence\n\n**D1. Title \"Blindspot\"（R2-N3 vs R1 反驳）**\n- **R2**: \"Blindspot\" 预设 attenuation 解释，建议改为中性标题（如 \"Measurement-Mode Divergence\" 或 \"The Likert-Pairwise Gap\"）。\n- **R1**: \"Blindspot\" 有操作性定义（Section 1 第5行），学术传播需要 memorable label；建议保留但在 Abstract 更早 qualify。\n- **Director 判断**: 两位均同意 Title 与正文 nuanced discussion 存在张力。分歧在于解决方案（改标题 vs 更早 qualify）。建议采用 R1 方案（保留 Title + 更早 qualify），因为 (a) \"Blindspot\" 已在论文中被操作性定义，(b) 正文充分讨论了三种竞争解释，(c) 标题的 communicative value 不应被牺牲——但前提是 Abstract 前 2–3 行必须同时引入操作性定义和 amplification/construct divergence 解释。\n\n**D2. GEE decomposition 的新颖性级别（R2-N1b vs R1 反驳）**\n- **R2**: GEE 是成熟统计工具，应用于 style/quality 分解是工程贡献，经典 factor analysis/SEM 承担类似功能。Excitement 3/5。\n- **R1**: GEE 在此处的目标（binary outcome 下分离 observed predictors 的条件贡献）与 factor analysis/SEM（latent variable modeling）不同。Prior work（RATE, FairJudge, CASSE）均未做 per-axis confound decomposition。不是纯工程贡献。Excitement 3.5/5。\n- **Director 判断**: R1 的反驳有技术依据——GEE conditional decomposition 确实与 FA/SEM 的目标和结构不同。但 R2 的更广泛观点（GEE 本身不是新方法）也成立。论文应将 GEE 定位为 \"novel application of established statistical tool to a problem that prior work has not addressed\"，而非 \"methodological innovation absent from classical framework\"。\n\n**D3. 信息密度（R2-W3 vs R1 反驳）**\n- **R2**: 8 页承载过多维度，核心 narrative 被稀释。建议将 7 种统计方法、TOST、Bayesian equivalence 全部移至附录。\n- **R1**: 论文的信息分层（正文核心 + 13 页 Appendix）是恰当的。核心 narrative 的逻辑链清晰。\n- **Director 判断**: 采用 R1 观点。对于 empirical methodology 论文，主文需同时呈现方法、主要发现和 robustness evidence。当前分层合理。但 Section 5.1 的单个段落确实过于密集（TOST + GEE + BF₀₁ 同时出现），建议拆分为更小的段落以提高可读性。\n\n---\n\n## Questions to Authors\n\n1. **[R1-Q1, R2-Q3, 共识]** Verbosity axis 做 n=355 scaled replication 后，Style OR（当前 8–13）预期缩水多少？是否改变 style-dominated 的 regime classification？这是最重要的 missing experiment。\n2. **[R1-Q2, R2 补充, 共识]** FK grade 在 formality 中是 mediator 还是 confounder？请提供 DAG 层面的论据。如果是 mediator，GPT-4o Style OR [2.15, 2.70] 中哪个端点更接近 true effect？\n3. **[R1-Q3, R2-W2, 共识]** AEval verbosity 上 Claude Style OR=4.76 (p<.001) 如何调和 \"low-sensitivity reference\"？是否有 AEval 数据分布的特殊性解释？\n4. **[R2-Q1, R1 支持]** 如果 pairwise amplification 是主要机制（而非 Likert attenuation），论文的 practical implications 如何改变？\"添加 pairwise 模式\" 的建议是否反而引入 false positives？\n5. **[R2-Q2, R1 支持]** 为什么不包含 human evaluation 来 ground-truth 两种测量模式？论文多次提到这是 \"the key next step\"——缺乏解释为什么当前工作没有做。\n6. **[R2-Q4]** Verbosity FK grade d=0.50 的 60% mediation by sentence length——这是否意味着 verbosity \"style bias\" 部分是 readability bias？\n\n---\n\n## Missing References\n\nR2 建议补充：\n1. Kocmi & Federmann (2023) — GEMBA: Using GPT Models for Reference-Free MT Evaluation（涉及 Likert vs pairwise 比较）\n2. 确认 Reber et al. (2025) RATE 和 Jeong et al. (2025) Comparative Trap 引用是否为最新版本（arXiv preprint 可能已被接收）\n\nR1 对此评价 NEUTRAL——相关性有限，建议 authors 自行判断。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: error — 视觉审查 Agent 因 API 限额耗尽而失败（\"You've hit your limit · resets May 25, 8am UTC\"）。无法完成 PDF 渲染和排版检查。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n**Overall: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 4.0 | 3.75 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n### 置信度\n4 / 5 — 两位 Reviewer 均有高置信度（4/5），核心判断一致。\n\n### 评分理由\n\n**支持接收的因素**：\n- 核心定性发现（Likert Blindspot）在 4 judges × 3 benchmarks 上有可靠复现\n- GEE per-axis decomposition 是该领域的真正方法论推进\n- 实验设计的严谨程度和 self-correction 的透明度明显高于同领域平均水平\n- Limitations 章节异常全面诚实\n- 对 RLHF/DPO pipeline 的 style bias audit 有直接实践指导价值\n\n**阻碍给出 4.0（Conference）的因素**：\n- 核心发现是 Thurstone (1927) 以来经典结论的 domain transfer，新颖性定位有过度宣称\n- 定量估计（GEE OR）受 n=88 小样本偏差系统性影响（~50%），且仅一个 cell 有 scaled validation\n- Claude negative control 证据链每条单独不成立，AEval verbosity 直接矛盾\n- GPT-4o formality——论文锚点——在 FK readability control 下失去显著性\n- 无法区分 attenuation 和 amplification 是根本限制，且 Title \"Blindspot\" 与此不一致\n\n### 改进路径\n\n如果 authors 能在 rebuttal/revision 中：\n1. 重新定位新颖性（\"empirical characterization + novel diagnostic layer\" 而非 \"beyond classical framework\"）\n2. 标注 n=88 OR 为上界估计并提供 projected ranges\n3. 正文讨论 GPT-4o FK control 结果及 mediator/confounder 分析\n4. 降级 Claude 为 \"lower-sensitivity judge\"，更新 Section 5.4\n5. Qualify \"consistently divergent\" 的 axis coverage 和 Gemini 异质性\n\n评分可提升至 **4.0 (Conference)** 或至少 **3.5+ (strong Findings)**。上述修改均为文字调整和框架重组，不需要新实验。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息密集但关键数字准确。需更早引入 \"Blindspot\" 的操作性定义和三种竞争解释。\"consistently divergent sensitivity across tested surface-level style axes\" 需 qualify（2 primary + 1 exploratory）。\n\n**Introduction**: Opening example 有 pedagogical value 但是 cherry-picked 的单个 instance。三个 \"LLM-specific distinctions\" 中 (a) 和 (c) 的新颖性宣称需要降级。Power analysis 引用（\"4–206× the sample size\"）是 illustrative 的，不应暗示 post-hoc power 是 primary evidence。\n\n**Related Work**: 覆盖全面且组织有序。对 RATE 的定位基于实证（\"vulnerability\"）是恰当的。最后一段 RLHF format-specific biases 论点有趣但未充分发展——这是一个 underexploited motivation。\n\n**Method (Section 3)**: NLI gate 的 direction-aware 设计（verbosity expansion 只检查 backward entailment）有技术创意。DAG (Figure 2) 清晰但灰度打印时 orange dashed line 不可辨。Section 3.1 \"constitutes a binary intervention\" 建议改为 \"approximates\"。Section 3.5 Design Rationale 的因果 disclaimer 恰当。\n\n**Experiments (Section 4)**: 统计框架（Section 4.1）的 FWER 控制和 exploratory/confirmatory 分类是 good practice。Table 1 清晰但 \"n=88 except where noted\" 与 verbosity n=86 不一致。Forest plot (Figure 3) 有效传达了跨 judge 模式。\n\n**Analysis (Section 5)**: 最密集的部分。Section 5.1 的三种解释讨论是 genuinely agnostic，但单个段落内 TOST + GEE + BF₀₁ 过密。Section 5.2 GEE decomposition 是论文最强的分析贡献——Table 2 的 verbosity vs formality 对比清晰有力。Section 5.3 cross-judge replication 扎实但 \"replicate across benchmarks\" (Section 5.3 第157行) 对选择性 replication 不够诚实。Section 5.4 六项 amplification controls 是 good-faith bounding 但不构成 exclusion。\n\n**Conclusion**: 简洁恰当。\"single-format audits risk systematic blind spots\" 仍偏向 attenuation 解释——在 amplification-dominant 情景下这条建议可能引入 false positives。\n\n**Limitations**: 异常全面——quality-style confounding, evaluator-producer bias, scope boundaries, validation methodology 均有讨论。两位 Reviewer 几乎没有需要补充的遗漏限制。\n\n**Appendix**: 13 页附录覆盖了所有 robustness checks、diagnostics、和 sensitivity analyses。组织合理（A*–V）。Table 3 的 QIC \"---\" 应补充实际数值。",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-23T09:11:03.360330+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3920
}
```

</details>

---


### Assistant

_source line 1418 · 2026-05-23T09:11:14.883955+00:00_

审稿报告已投递至 Research Director。

**Round 17 审稿完成**。核心结论：

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致
- **6 个 Must-Fix**：(1) n=88 OR 膨胀未传播；(2) GPT-4o FK control 后失显著性；(3) Claude reference 证据链矛盾；(4) 新颖性过度宣称；(5) "consistently divergent" 过强；(6) Title "Blindspot" 预设 attenuation（分歧点）
- **5 个 Should-Fix**：evaluator-producer overlap、cross-benchmark 选择性、TOST margin、GEE omitted variables、Comparative Trap 量化
- **关键共识**：核心定性发现扎实，所有 Must-Fix 均可通过文字修改和框架重组解决（无需新实验），修改后可达 Conference (4.0) 水平
- Issue Tracker 已同步更新（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 136

## Round 136

2 recorded events


### User

_source line 1419 · 2026-05-23T09:11:17.477200+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部意见的逐条回应并提交给 Review Director。

总结：
- **Must-Fix**: N1（small-sample OR 膨胀）和 N3（Claude reference 矛盾）完全同意；N2（GPT-4o FK control）同意需要更多正文讨论，但补充了 FK 可能是 mediator 而非 confounder 的重要 nuance
- **Should-Fix**: W1-W3 同意；W4（因果语言）部分反驳——两处表述在不同层面（操作 vs 推断）运作，并不矛盾
- **Minor**: M2（intro cherry-picked）反驳——开头示例的 illustrative 功能是论文写作惯例；其余 M1/M3/M4/M5 同意
- **Questions**: Q1-Q3 与我自己的审稿提出了相同或相似的问题；Q4 我认为论文的 empirical validation（Appendix F, permutation p=.663）已充分回应

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1420 · 2026-05-23T09:11:31.779575+00:00_

审稿流程已完成。

**Round 17 审稿报告已投递给 Research Director。**

核心结论：**3.5 / 5 (Borderline Conference)**，两位 Reviewer 评分一致。

**关键共识**：
- 核心定性发现（Likert Blindspot）扎实，4 judges × 3 benchmarks 复现可靠
- GEE per-axis decomposition 是真正的方法论贡献
- 6 个 Must-Fix 阻碍给出 4.0：(1) n=88 OR 膨胀未传播；(2) GPT-4o FK control 后失去显著性；(3) Claude reference 证据链矛盾；(4) 新颖性过度宣称；(5) "consistently divergent" 过强；(6) Title 与三种竞争解释的张力
- 5 个 Should-Fix：evaluator-producer overlap 验证不足、cross-benchmark 选择性、TOST margin 无先验依据、GEE omitted variables、Comparative Trap 未量化

**改进路径**：所有 Must-Fix 均为文字调整和框架重组（无需新实验），修改后可达 4.0 (Conference) 或 strong Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 137

## Round 137

58 recorded events


### User

_source line 1421 · 2026-05-23T14:17:36.678662+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-23T14:17:41.998072+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-23T14:17:42.049189+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-23T14:17:50.325773+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-23T14:17:50.376453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-23T14:17:58.711926+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-23T14:17:58.762435+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-23T14:18:03.200388+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-23T14:18:03.250920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-23T14:18:08.219630+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-23T14:18:09.926164+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (55 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **verbosity_scaled_n355** (success): Verbosity Style OR at n=355 will shrink from n=86 estimates (8.21-13.10) to projected range 4-6.5 due to small-sample upward bias, mirroring the formality shrinkage pattern (4.20→2.15). Likert ATE will remain NS, confirming the Blindspot is robust to increased sample size for verbosity axis.\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n\n## 趋势\n成功 39 / 负向 12 / 失败 0 / 共 55\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1706
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-23T14:18:10.027024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-23T14:18:10.879876+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\textbf{Residual confounding.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself.
43	Although formality effects survive logistic adjustment (OR $= 2.32$, $p = 0.006$), residual confounding is not fully eliminated; definitive resolution requires human ground-truth comparison of Likert and pairwise judgments on identical pairs.
44	
45	\textbf{Detection vs.\ amplification.}
46	The Blindspot may partly reflect pairwise format amplification \citep{jeong2025comparative} rather than pure detection.
47	Six controls bound this risk (\S\ref{sec:amplification}), but we cannot precisely quantify the amplification factor without a ground-truth bias magnitude.
48	
49	\textbf{Scope.}
50	CSD applies only to surface-level axes whose rewrites preserve semantic content; a tone pilot (assertive $\to$ hedging) was rejected by the NLI gate.
51	Primary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.
52	
53	\section*{Code and Data}
54	Code and data will be released upon acceptan
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-23T14:18:11.030781+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1435 · 2026-05-23T14:18:12.336699+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1436 · 2026-05-23T14:18:12.487559+00:00_

-rw-r--r-- 1 ubuntu ubuntu 492184 May 23 13:06 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-23T14:18:16.952615+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines from the ACL website. Here are 
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5921
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-23T14:18:21.570867+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1439 · 2026-05-23T14:18:21.872451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-23T14:18:23.730310+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-23T14:18:23.831076+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-23T14:18:26.943588+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the web search results, here are the key submission guidelines for ACL Rolling Review (ARR) 2026 regarding page limits and format requirements:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## Additional Content for Camera-Ready Versions

Final versions of accepted papers will be given 
…[truncated 882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5372
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-23T14:18:28.099058+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here are the key deadlines for EMNLP 2026:

## Paper Submission Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, and the reviewer registration deadline for all authors is May 27, 2026.

## Paper Commit
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6226
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-23T14:18:38.334432+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers format page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers format page limit anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1445 · 2026-05-23T14:18:39.238147+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1446 · 2026-05-23T14:18:39.238502+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-23T14:18:44.354525+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers format page limit anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"}]

Based on the search results from the EMNLP 2026 Call for Main Conference Papers page, here are the key details:

**Format and Page Limits:**
Final versions of accepted papers will be given one additional page of content (up to 9 pages), though the complete page limit information appears to be partially cut off in the search result.

**Anonymity:**
The reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers. Additionally, following the ACL and ARR policies, there is no anonymity period requirement.

**Submission Process:**
EMNLP 2026 has coordinated with *CL 2026 conferences adopting the same procedure, allowing authors at each cycle to commit their paper to a conference or revise and resubmit for another round of reviews.

The search result appears to be truncated, so some detailed formatting requirements may not be fully visible in the excerpt provided. For complete formatting guidelines, you may want to visit the full page directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6020
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-23T14:18:53.246603+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-23T14:18:53.247103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-23T14:18:53.247419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-23T14:18:53.248214+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 17
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。"
44	      - round: 13
45	        reviewers: [1, 2]
46	        note: "R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。"
47	      - round: 14
48	        reviewers: [1, 2]
49	        note: "R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。"
50	      - round: 15
51	        reviewers: [1, 2]
52	        note: "R15 fresh review: 两位再次独立提出。"
53	      - round: 16
54	        reviewers: [1, 2]
55	        note: "R16: S4 称 GEE decomposition 是'真正的方法论
…[truncated 23622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-23T14:19:17.119438+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool call

_source line 1453 · 2026-05-23T14:19:17.270385+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-23T14:19:17.873092+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (55 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **verbosity_scaled_n355** (success): Verbosity Style OR at n=355 will shrink from n=86 estimates (8.21-13.10) to projected range 4-6.5 due to small-sample upward bias, mirroring the formality shrinkage pattern (4.20→2.15). Likert ATE will remain NS, confirming the Blindspot is robust to increased sample size for verbosity axis.\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n\n## 趋势\n成功 39 / 负向 12 / 失败 0 / 共 55\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 753
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-23T14:19:17.873579+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-23T14:19:19.379425+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits (long/short paper), formatting template, anonymity rules, appendix rules, citation format, any special requirements. List each requirement clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits (long/short paper), formatting template, anonymity rules, appendix rules, citation format, any special requirements. List each requirement clearly."
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-23T14:19:24.749562+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Final versions:** Additional 1 page permitted (9 pages for long, 5 for short) to address reviewer feedback

## Anonymity Requirements
The document states: "The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers." Authors may optionally make anonymized submissions publicly visible.

## Formatting & Templates
Authors must follow "all of the ARR submission requirements," which are detailed on the ACL Rolling Review website. Specific templates are referenced but not reproduced here.

## Appendices & Supplementary Materials
The guidelines reference "Optional Supplementary Materials (appendices, software and data)" as permissible per ARR policies.

## Citation & Comparison Standards
Authors must follow ARR guidelines on "Citation and Comparison," available through the main ARR Call for Papers.

## Special Requirements
- Must declare intended conference (EMNLP 2026) at submission time
- Cannot modify author list during commitment phase (reordering is allowed)
- Must complete author registration by May 27, 2026
- Papers require "at least one presenting author registered" to remain in proceedings
- Writing assistance is permitted; fully AI-generated papers are not

## Ethics & Integrity
Papers must comply with ACL's Publication Ethics Policy and avoid hallucinated citations, thinly sliced contributions, and entirely AI-generated content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebFetch",
  "elapsed_ms": 5370
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-23T14:19:54.208760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-23T14:19:54.962173+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf (480.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-23T14:19:55.123334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-23T14:19:55.174027+00:00_

abstract.tex
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-23T14:20:22.757781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-23T14:20:22.859559+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_director_acab027e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-23T14:20:33.207656+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-23T14:20:33.258524+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-23T14:20:38.581843+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project_config*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project_config*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-23T14:20:38.682742+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-23T14:20:41.594309+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find YAML config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find YAML config files"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-23T14:20:41.695133+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-23T14:20:47.013563+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml 2>/dev/null",
  "description": "Check if external review is configured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/workspace.yaml 2>/dev/null",
    "description": "Check if external review is configured"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-23T14:20:47.116606+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-23T14:21:08.458505+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-23T14:21:32.282260+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23823
}
```

</details>

---


### Tool call

_source line 1474 · 2026-05-23T14:21:34.342106+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ACL Rolling Review, May 2026 cycle）\n- **格式**: ACL template, double-blind, Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有，不计入页数限制\n- **匿名规则**: Double-blind，禁止透露作者身份\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / 无问题）：\n\n### 1. 统计方法论\n- NLI gate（DeBERTa-v3, threshold 0.90）的有效性：false-negative rate、选择偏差、方向感知 gating 的合理性\n- Bradley-Terry 模型的适用性：unidimensionality 假设、regularization（choix library）、小样本（n=88）下的估计稳定性\n- GEE conditional decomposition：模型设定（exchangeable correlation, sandwich SE）、两个 predictor 是否存在 omitted variable bias、CI 宽度在 n=88 下是否支持论文结论\n- Holm-Bonferroni 多重比较校正：primary family 的定义是否合理、exploratory 和 confirmatory 分析的分类\n- Power analysis（Figure 4）：是否为 post-hoc power、检验效能曲线的解读是否正确\n\n### 2. 实验设计\n- Style-controlled rewriting pipeline：单 rewriter（Qwen3-32B）的 evaluator-producer overlap、double-rewrite control 的充分性\n- 样本量：n=88 formality / n=86 verbosity 是否足以支撑 GEE decomposition 的 OR 估计（论文声称 n=88 OR 为上界估计，是否合理）\n- n=355 scaled replication 是否充分验证了 attenuation 效应\n- Cross-benchmark replication：6/24 cells 的选择性是否构成 cherry-picking 风险\n- Claude Sonnet 4 作为 negative control：TOST power、MDE、贝叶斯因子的解读\n\n### 3. Robustness 检查\n- NLI threshold sensitivity（11 thresholds）\n- Consistency filtering vs. full data 对比\n- FK grade 作为协变量的 mediator vs. confounder 讨论\n- Alternative rewriter（GPT-4o）的 22% OR 降幅\n- Content preservation human annotation（100 pairs, AC₁=0.96）\n\n### 4. 因果推断声明\n- 论文的因果语言（\"intervention\", \"causal\"）是否与实际设计匹配\n- Section 3.5 Design Rationale 的 DAG 是否合理\n- Residual confounding 的处理是否充分\n\n请按照 ARR reviewer guidelines 格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Soundness (1-5) → Overall Assessment。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
  "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ACL Rolling Review, May 2026 cycle）\n- **格式**: ACL template, double-blind, Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有，不计入页数限制\n- **匿名规则**: Double-blind，禁止透露作者身份\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / 无问题）：\n\n### 1. 统计方法论\n- NLI gate（DeBERTa-v3, threshold 0.90）的有效性：false-negative rate、选择偏差、方向感知 gating 的合理性\n- Bradley-Terry 模型的适用性：unidimensionality 假设、regularization（choix library）、小样本（n=88）下的估计稳定性\n- GEE conditional decomposition：模型设定（exchangeable correlation, sandwich SE）、两个 predictor 是否存在 omitted variable bias、CI 宽度在 n=88 下是否支持论文结论\n- Holm-Bonferroni 多重比较校正：primary family 的定义是否合理、exploratory 和 confirmatory 分析的分类\n- Power analysis（Figure 4）：是否为 post-hoc power、检验效能曲线的解读是否正确\n\n### 2. 实验设计\n- Style-controlled rewriting pipeline：单 rewriter（Qwen3-32B）的 evaluator-producer overlap、double-rewrite control 的充分性\n- 样本量：n=88 formality / n=86 verbosity 是否足以支撑 GEE decomposition 的 OR 估计（论文声称 n=88 OR 为上界估计，是否合理）\n- n=355 scaled replication 是否充分验证了 attenuation 效应\n- Cross-benchmark replication：6/24 cells 的选择性是否构成 cherry-picking 风险\n- Claude Sonnet 4 作为 negative control：TOST power、MDE、贝叶斯因子的解读\n\n### 3. Robustness 检查\n- NLI threshold sensitivity（11 thresholds）\n- Consistency filtering vs. full data 对比\n- FK grade 作为协变量的 mediator vs. confounder 讨论\n- Alternative rewriter（GPT-4o）的 22% OR 降幅\n- Content preservation human annotation（100 pairs, AC₁=0.96）\n\n### 4. 因果推断声明\n- 论文的因果语言（\"intervention\", \"causal\"）是否与实际设计匹配\n- Section 3.5 Design Rationale 的 DAG 是否合理\n- Residual confounding 的处理是否充分\n\n请按照 ARR reviewer guidelines 格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Soundness (1-5) → Overall Assessment。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
    "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-23T14:21:56.189489+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21847
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-23T14:21:57.295607+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ACL Rolling Review, May 2026 cycle）\n- **格式**: ACL template, double-blind, Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有，不计入页数限制\n- **匿名规则**: Double-blind，禁止透露作者身份\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / 无问题）：\n\n### 1. 新颖性评估\n- \"Likert Blindspot\" 概念的原创性——是否本质上是心理测量学已知现象（Thurstone 1927, Stevens 1946）在 LLM judge 领域的 domain transfer？\n- CSD framework 的增量贡献：NLI-gated content control + per-axis decomposition + position-controlled pairwise 的组合是否足够新颖？\n- GEE conditional decomposition 的方法论贡献：是否等同于 factor analysis/SEM？论文声称的三个 LLM-specific distinctions（per-axis structure, GEE decomposition, binary divergence）是否被夸大？\n- 与 RATE (Reber et al., 2025) 的差异化是否充分论证？\n\n### 2. Framing 与定位\n- Title \"The Likert Blindspot\" 是否暗示 Likert 有缺陷（单一因果方向），与正文 nuanced 讨论（三种非排他解释）是否矛盾？\n- Abstract 中 \"consistently divergent\" 的措辞——基于 2 primary + 1 exploratory axis，是否过于强势？\n- Introduction 的三个 LLM-specific distinctions 是否被过度宣称（\"complements\" vs \"surpasses\"）？\n- \"Systematic pattern\" / \"consistent\" 等用语是否被论文证据充分支撑？\n\n### 3. Related Work 完整性\n- 是否遗漏重要相关工作（特别是 LLM judge bias、psychometric evaluation、causal inference in NLP 领域）？\n- 对 RATE、Comparative Trap (Jeong et al., 2025)、CASSE、FairJudge 等竞品的定位是否准确和公正？\n- 引用格式是否一致（arXiv preprint vs 正式发表）？\n\n### 4. 写作质量\n- 论文结构和叙事流是否清晰？\n- 信息密度是否合理（8 页内承载 5 judges × 3 axes × 3 benchmarks 的实验）？\n- Figure/Table 设计：Figure 1（pipeline）、Figure 2（DAG）、Figure 3（forest plot）、Figure 4（power curve）、Figure 5（GEE bar chart）、Figure 6（heatmap）是否有效传达信息？\n- 术语一致性（\"style bias\" vs \"style sensitivity\"）\n- Abstract 是否超过 200 words（EMNLP 2026 硬约束）？\n\n### 5. 格式合规\n- 页数限制：正文是否 ≤ 8 页？\n- Limitations section 是否存在且内容适当？\n- 匿名性：是否有任何泄露作者身份的内容？\n- 引用格式是否符合 ACL 标准？\n- Appendix 结构是否合理？\n\n请按照 ARR reviewer guidelines 格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Excitement (1-5) → Overall Assessment。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
  "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ACL Rolling Review, May 2026 cycle）\n- **格式**: ACL template, double-blind, Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有，不计入页数限制\n- **匿名规则**: Double-blind，禁止透露作者身份\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / 无问题）：\n\n### 1. 新颖性评估\n- \"Likert Blindspot\" 概念的原创性——是否本质上是心理测量学已知现象（Thurstone 1927, Stevens 1946）在 LLM judge 领域的 domain transfer？\n- CSD framework 的增量贡献：NLI-gated content control + per-axis decomposition + position-controlled pairwise 的组合是否足够新颖？\n- GEE conditional decomposition 的方法论贡献：是否等同于 factor analysis/SEM？论文声称的三个 LLM-specific distinctions（per-axis structure, GEE decomposition, binary divergence）是否被夸大？\n- 与 RATE (Reber et al., 2025) 的差异化是否充分论证？\n\n### 2. Framing 与定位\n- Title \"The Likert Blindspot\" 是否暗示 Likert 有缺陷（单一因果方向），与正文 nuanced 讨论（三种非排他解释）是否矛盾？\n- Abstract 中 \"consistently divergent\" 的措辞——基于 2 primary + 1 exploratory axis，是否过于强势？\n- Introduction 的三个 LLM-specific distinctions 是否被过度宣称（\"complements\" vs \"surpasses\"）？\n- \"Systematic pattern\" / \"consistent\" 等用语是否被论文证据充分支撑？\n\n### 3. Related Work 完整性\n- 是否遗漏重要相关工作（特别是 LLM judge bias、psychometric evaluation、causal inference in NLP 领域）？\n- 对 RATE、Comparative Trap (Jeong et al., 2025)、CASSE、FairJudge 等竞品的定位是否准确和公正？\n- 引用格式是否一致（arXiv preprint vs 正式发表）？\n\n### 4. 写作质量\n- 论文结构和叙事流是否清晰？\n- 信息密度是否合理（8 页内承载 5 judges × 3 axes × 3 benchmarks 的实验）？\n- Figure/Table 设计：Figure 1（pipeline）、Figure 2（DAG）、Figure 3（forest plot）、Figure 4（power curve）、Figure 5（GEE bar chart）、Figure 6（heatmap）是否有效传达信息？\n- 术语一致性（\"style bias\" vs \"style sensitivity\"）\n- Abstract 是否超过 200 words（EMNLP 2026 硬约束）？\n\n### 5. 格式合规\n- 页数限制：正文是否 ≤ 8 页？\n- Limitations section 是否存在且内容适当？\n- 匿名性：是否有任何泄露作者身份的内容？\n- 引用格式是否符合 ACL 标准？\n- Appendix 结构是否合理？\n\n请按照 ARR reviewer guidelines 格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Excitement (1-5) → Overall Assessment。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
    "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-23T14:21:58.655447+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 1478 · 2026-05-23T14:22:11.051302+00:00_

已并行派发：

- **视觉审查 Agent** → 已启动（fire-and-forget，不阻塞审稿）
- **Reviewer 1**（方法严谨性）→ 已分配，独立审稿中
- **Reviewer 2**（新颖性/完整性）→ 已分配，独立审稿中

等待两位 Reviewer 返回 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1479 · 2026-05-23T14:28:44.759176+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## 论文信息
- **Title**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
- **Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)

---

## Summary

本文定义了 "Likert Blindspot"——LLM judge 的 pairwise comparison 能检测到风格敏感性而 Likert scoring 检测不到的现象。提出 Controlled Style Decomposition (CSD) 框架，整合 NLI-gated 内容控制、per-axis 风格分解和 position-controlled pairwise comparison。在 4-5 个 judge、3 个 benchmark、2-3 个风格轴上实验，结果一致显示 Likert 失灵（7 种统计方法全部确认）。GEE 条件分解揭示 per-axis confound structure：verbosity 是 style-dominated（Style OR 8–13），formality 是 quality-confounded。论文坦诚提出三种非排他解释（attenuation, amplification, construct divergence），统计工作扎实。

---

## 总体评分

**Overall Assessment**: 3.5 / 5 — Borderline Conference

**一句话总结**: 实验执行出色、统计严谨，但核心发现本质上是经典心理测量学原理（Thurstone 1927）在 LLM judge 领域的系统验证，新颖性为 moderate；per-axis confound structure 是唯一genuinely novel 的经验发现。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 方法论严谨，多层控制设计（NLI gating, position swap, double-rewrite, debiased prompting），七种统计方法交叉验证，Holm-Bonferroni 校正。小样本和 rewriter-judge overlap 是次要问题。 |
| Excitement | 3 / 5 | 对 LLM judge 审计实践有直接指导意义，GEE per-axis 分解是有用的方法贡献。但核心 insight（pairwise 比 Likert 更敏感）对熟悉测量理论的读者不新鲜。 |
| Reproducibility | 4 / 5 | 方法描述详细，统计流程完整，承诺 code/data release。模型 API 版本明确（GPT-4o 2024-08-06 等）。 |
| Confidence | 4 / 5 | 熟悉心理测量学文献、LLM judge 评估和因果推断方法。 |

---

## 主要优势

**S1. 卓越的实验严谨性。** 六层控制设计（NLI gate, position swap, double-rewrite, debiased prompting, cross-rewriter validation, GEE confound decomposition）在 LLM judge bias 文献中属于最严格的方法控制之一。七种统计方法全部一致确认 Blindspot（Table 14, Appendix M），bootstrap CI、TOST equivalence testing、Bayesian equivalence testing 的组合使用展现了统计成熟度。

**S2. Per-axis confound structure 是genuinely novel 的发现。** GEE decomposition 揭示 verbosity 是 style-dominated（Style OR 8–13, Originality OR < 1）而 formality 是 quality-confounded（两个 predictor 都显著），这种 per-axis 差异不是经典心理测量学能预测的，对 LLM judge 审计策略有直接实践意义——不同风格轴需要不同的审计方法。

**S3. 诚实的 claim hedging。** 论文主动提出三种非排他解释（§5.1），明确承认 residual confounding 未完全消除（Limitations），用 "complements" 而非 "surpasses" 描述与经典框架的关系。这在 LLM 领域论文中属于少见的审慎态度。

**S4. 跨 judge/benchmark 复制规模。** 5 judges × 3 benchmarks × 3 axes 的实验矩阵（虽然部分为 exploratory），加上 n=355 的 scaled replication，提供了远超单一实验的证据强度。Claude Sonnet 4 的 benchmark-dependent 结果（§5.3）是一个有价值的 discriminative validity 证据。

**S5. 实践相关性强。** 结论直接指向 LLM alignment pipeline 的审计盲区——如果 Likert-based reward model 评估漏检了 pairwise 能发现的风格偏差，那么通过 RLHF/DPO 训练的模型可能继承未被检测的 style preferences。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer，而非新现象

- 具体位置：Title, Abstract, §1 Introduction (para 3-4), §5.1
- 问题：论文的核心经验发现——pairwise comparison 比 Likert 更能检测 style sensitivity——本质上是 Thurstone (1927) Law of Comparative Judgment 在 LLM judge 领域的验证。论文在 §1 para 3 确实引用了 Thurstone 并说 "quantitatively consistent"，但 Title "The Likert Blindspot" 和 Abstract 的 framing 仍然暗示这是一个新发现的现象。Introduction 声称的三个 "LLM-specific distinctions" 中，(c) "near-complete binary split" 被论文自己承认 "consistent with classical predictions when accounting for effect-size-dependent power"——这不是一个 LLM-specific distinction，而是经典理论在该效应量下的预测结果。
- 为什么影响接收：ARR Excitement 维度要求 novelty。如果审稿人熟悉测量理论，会认为核心 contribution 是一个 well-executed replication study 而非 discovery。这直接影响 Conference vs Findings 的定位。
- 建议修改方向：(1) 将 Introduction 的三个 LLM-specific distinctions 缩减为两个，删除 (c) binary split 或将其降级为"与经典理论一致的验证"；(2) 更清晰地将 contribution 定位为 "systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool"，而非 "new phenomenon"；(3) 考虑在 Title/Abstract 中添加类似 "extends classical measurement theory to LLM evaluation" 的表述。

**N2** [critical] Scaled replication 覆盖不足——仅一个 cell 有大样本验证

- 具体位置：§5.1 para 2, Table 1
- 问题：n=355 的 scaled replication 仅覆盖 Qwen3-32B × formality 这一个 cell。这是论文最关键的论点支柱——用大样本证明 Likert 的 d→0 是结构性的而非 power 不足。但其他 11 个 primary/confirmatory cells（GPT-4o × formality/verbosity, Llama-70B × formality/verbosity, Gemini × formality/verbosity 等）都只有 n=86–88，无法排除这些 cells 的 Blindspot 仅仅是 power 问题。
- 为什么影响接收：论文声称 "consistent pattern rather than an isolated anomaly"（§1 Contribution 2），但只有一个 cell 用大样本验证了这不是 power artifact。这是一个可证伪但未被充分验证的 claim。尤其 Gemini formality（BT 仅 57.4%，效应最弱）如果做 scaled replication 可能不复现 d→0 的结论。
- 建议修改方向：(1) 对至少一个 verbosity cell 做 scaled replication（因为 verbosity 是最强效应，但 Likert d 也接近零——这可以更干净地证明结构性衰减）；(2) 如果资源限制无法做更多 replication，应在 Limitations 明确承认这一 coverage gap，并将 "consistent pattern" 的 claim 弱化为 "observed pattern, with structural attenuation confirmed for one judge×axis cell"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Title "The Likert Blindspot" 暗示单一因果方向，与正文 nuanced 讨论矛盾

- 具体位置：Title, §5.1 "Interpreting the divergence"
- 问题："Blindspot" 一词暗示 Likert 有缺陷（漏检），预设了 attenuation 解释为主导。但 §5.1 明确提出三种非排他解释，包括 pairwise amplification（可能是 pairwise 过度放大而非 Likert 漏检）和 construct divergence（两种模式测量不同构念）。如果 amplification 是主因，那么 "Blindspot" 的描述就不准确——Likert 没有"盲点"，只是 pairwise 有"放大镜"。
- 建议：(1) 在 §1 更早处对 "Blindspot" 进行操作化定义（论文在 §1 para 2 做了，但可以更突出）；(2) 考虑在 Abstract 中加入一句明确的 hedge：e.g., "which we term the Likert Blindspot as an operational descriptor without committing to a specific causal mechanism"（部分已在正文中，但 Abstract 缺少）。实际上我看到 Introduction 第二段有这个 hedge，但 Abstract 和 Title 没有传达。

**W2** [warning] Qwen3-32B 同时担任 rewriter 和 target judge 的循环依赖

- 具体位置：§3.1, §4.1, Appendix E
- 问题：Qwen3-32B 既是风格改写器又是被测 judge。虽然 Appendix E 展示了独立 GPT-4o rewriter 的验证（BT 从 66.5% 降至约 57%，降幅 22%），但这个 22% 的降幅本身值得关注——它说明 evaluator-producer overlap 确实 inflate 了效应量。论文报告的 Qwen3-32B 结果可能系统性偏高。
- 建议：(1) 在 §4.1 或 Table 1 脚注中标注 Qwen3-32B 的 evaluator-producer overlap caveat；(2) 如果可能，对 Qwen3-32B 的所有主要分析使用 GPT-4o rewriter 数据作为 robustness check；(3) 考虑 Table 1 中标注 Qwen3-32B 结果可能有 ~20% 的上行偏差。

**W3** [warning] Register 轴结果弱且 exploratory，但在 Abstract/Contribution 中占有隐含地位

- 具体位置：Abstract ("two primary axes"), Table 1 (register rows), §5.3
- 问题：Register 轴在 Table 1 中有 3 行结果（GPT-4o, Qwen3, Llama-70B），但 BT 仅 .553–.635，效应远弱于 formality (.574–.695) 和 verbosity (.708–.773)。更关键的是，register 的 GEE 结构（Table 2）显示 Originality OR 远高于 Style OR（Qwen3: 5.72 vs 1.91），说明 register 效应可能主要由 quality confounding 驱动。论文标注为 "exploratory"，但在 cross-benchmark heatmap (Figure 6) 和 GEE table (Table 2) 中占了相当篇幅。
- 建议：将 register 结果完全移至 Appendix，正文只保留一句 "an exploratory register axis yielded weaker, quality-confounded effects (Appendix X)"。这会释放正文空间给更重要的 scaled replication 或 cross-benchmark 讨论。

**W4** [warning] "Systematic pattern" / "consistent" 等措辞与例外情况的张力

- 具体位置：§1 Contribution 2, §6 Conclusion
- 问题：Contribution 2 声称 "revealing measurement-mode divergence as a consistent pattern rather than an isolated anomaly"。但实际数据中：(1) Claude Sonnet 4 不显示一般性 Blindspot（Table 1, BT .541–.562, n.s.）；(2) Gemini formality 效应弱（BT 57.4%, Style OR 1.64 n.s.）；(3) cross-benchmark replication 仅 6/24 cells 达到显著。论文用 "three exceptions (‡)" 处理例外，但 "consistent" 一词在有 ~30% exception rate 的情况下值得审慎使用。
- 建议：将 "consistent pattern" 改为 "predominant pattern" 或 "majority pattern"；在 §6 Conclusion 中量化复制率（e.g., "8/11 primary+confirmatory cells, 6/24 cross-benchmark cells"）。

---

## Minor 问题（不影响接收）

**M1.** 术语一致性："style bias" 和 "style sensitivity" 在论文中交替使用（e.g., Abstract 用 "sensitivity"，§5.1 标题用 "Blindspot" 暗示 "bias"）。建议统一——鉴于论文立场是 agnostic about mechanism，"style sensitivity" 更准确。

**M2.** Figure 5 (GEE bar chart, p.8) 的 y 轴标签 "Odds Ratio" 在 log scale 上可能对不熟悉 GEE 的读者造成困惑。建议添加 "log scale" 标注或在 caption 中明确说明。

**M3.** §3.2 提到 "DeBERTa-v3-large fine-tuned on MNLI" 作为 NLI gate，但未说明该模型在 out-of-domain（非 MNLI distribution）文本上的性能是否经过验证。human annotation（§5.4）部分验证了这一点，但 NLI model 本身的 domain-shift robustness 未被讨论。

**M4.** Table 1 的 "Cat." 列标记（†, †_e, †_c, ---）需要读者频繁查阅脚注。建议直接使用文字标签如 "Blind", "Expl", "Conf", "Neither"。

**M5.** §5.2 引用 Nemes et al. 2009 解释小样本上行偏差。这个引用是 meta-analysis 领域的，应用到 GEE OR 的 small-sample bias 上是否完全对应，可以补充说明。

---

## Questions to Authors

**Q1.** §5.1 的 non-tie concordance analysis（76.6%, p < .001）是论文区分 attenuation 和 construct divergence 的关键证据。但 76.6% 的 concordance 意味着 23.4% 的 discordance——这个 discordance rate 是否足够低以排除 partial construct divergence？论文承认 "partial construct divergence remains at weaker effect sizes"，那么具体在哪个效应量阈值以下 construct divergence 可能成为主导解释？

**Q2.** 100-point continuous Likert scale（Appendix O）仍然显示 p > 0.15。这是一个重要的 robustness check。但 Appendix O 是否控制了 judges 使用 continuous scale 时的行为变化（e.g., 是否有 evidence 表明 judges 真的利用了 continuous scale 的 granularity，而不是仍然只使用少数离散值）？

**Q3.** 论文使用 Qwen3-32B 作为 style classifier（§3.1）判断文本当前风格。如果 classifier 本身有系统性偏差（e.g., 倾向于将高质量文本分类为 formal），这是否会在 data generation 阶段引入 confounding？

**Q4.** GEE 的 exchangeable working correlation 假设在 paired comparison data 中是否合理？论文提到 within-pair correlations 接近零（α̂ ∈ [−0.25, +0.11]），但 −0.25 的估计值似乎不算"接近零"。这是否影响 sandwich standard errors 的可靠性？

---

## Missing References

论文的 Related Work 相当全面（~40 引用），但以下方向可以加强：

1. **Item Response Theory (IRT) 在 NLG evaluation 中的应用**：论文简短引用了 Embretson & Reise (2000)，但 IRT 提供了更正式的框架来量化不同 measurement mode 的信息函数差异。近期有 IRT 用于 LLM evaluation 的工作（e.g., Polo et al., 2024, "TinyBenchmarks"），可以补充讨论 IRT 视角下 Likert vs pairwise 的 information gain 差异。

2. **Likert scale anchoring effects**：不同 LLM judge 可能以不同方式解释 1-10 scale 的锚点（e.g., 有些 judge 倾向使用中间值，有些使用极端值），这是 Likert 信号衰减的已知机制之一（Krosnick 1999 已引用，但 scale anchoring 的具体讨论较少）。

3. **Pairwise comparison 在 RLHF 中的 amplification 问题**：除了 Jeong et al. (2025) Comparative Trap，还有 Munos et al. (2023) "Nash Learning from Human Feedback" 等讨论 pairwise preference 中的 noise amplification。

---

## Scoring Summary

| 维度 | 分数 |
|------|------|
| **Soundness** | 4 / 5 |
| **Excitement** | 3 / 5 |
| **Overall Assessment** | 3.5 / 5 (Borderline Conference) |
| **Reproducibility** | 4 / 5 |
| **Confidence** | 4 / 5 |

**Overall Justification**: 论文在实验设计和统计分析方面达到了很高的标准，per-axis confound structure 是一个有价值的发现，CSD 作为实用诊断工具有明确的应用价值。将其拉向 3.5 而非 3.0 的主要因素是：(1) 实验规模和控制的thoroughness 在同类工作中突出；(2) GEE per-axis 分解提供了超越 Thurstone 经典框架的 genuinely new insight；(3) 实践相关性强（directly actionable for RLHF/DPO pipeline audits）。阻止其达到 4.0 的因素是：(1) 核心现象是经典测量理论的 domain transfer，novelty ceiling 有限；(2) scaled replication 仅覆盖 1/12 cells；(3) "consistent pattern" 的 claim 与 ~30% exception rate 有张力。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1480 · 2026-05-23T14:28:52.657451+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1481 · 2026-05-23T14:29:11.698548+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference）。实验执行和统计严谨性达到高标准，GEE per-axis confound structure（verbosity style-dominated vs formality quality-confounded）是genuinely novel的发现。但核心现象——pairwise 比 Likert 更敏感——本质上是 Thurstone 1927 的 domain transfer，novelty ceiling 有限。

**两个 Must-Fix**：
1. 新颖性定位需要更精确——Introduction 的三个"LLM-specific distinctions"中第(c)个(binary split)被论文自己承认与经典理论一致，不构成独立贡献
2. Scaled replication（n=355）仅覆盖 Qwen3-32B × formality 一个 cell，其他 11 个 cell 无法排除纯 power 问题

**四个 Should-Fix**：Title 暗示单一因果方向与正文矛盾；Qwen3-32B rewriter-judge overlap（~20% inflation）；Register 轴结果弱应移至 Appendix；"consistent pattern" 与 ~30% exception rate 的张力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1482 · 2026-05-23T14:29:20.170853+00:00_

Reviewer 2 审稿已收到（Overall 3.5, Borderline Conference）。等待 Reviewer 1 完成方法严谨性审查后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 140

## Round 140

6 recorded events


### User

_source line 1483 · 2026-05-23T14:30:40.381504+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 论文定义了一个有实际意义的现象（Likert Blindspot），方法论框架（CSD + GEE decomposition）设计精巧、robustness 检查充分，但 GEE 估计在 n=88 下显著膨胀（已证实 49% shrinkage），且跨 benchmark 证据存在选择性报告风险，需要补充关键实验后才能确信核心结论。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架选择合理（BT + GEE + Holm-Bonferroni），但 n=88 GEE 估计已证实大幅膨胀，9 个 judge×axis 仅 1 个在 n=355 复制；cross-benchmark 6/24 cells 为选择性复制 |
| Excitement | 3.0/5 | 现象有实际价值（LLM 评估方法论），GEE decomposition 是有用的方法贡献，但 pairwise > rating 的核心洞察在心理测量学中已有近百年历史（Thurstone 1927），应用层面贡献为主 |
| Reproducibility | 4.0/5 | 方法描述详尽（Appendix R），统计方法标准化（choix, GEE），承诺代码开源；但数据未随投稿提供 |
| Reviewer Confidence | 4/5 | 熟悉 BT 模型、GEE、因果推断方法论和 LLM 评估文献；NLI gating 的具体实现细节未完全验证 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] GEE 小样本膨胀严重，仅一个配置在 n=355 复制
- 具体位置：Table 2, Section 5.2 (Per-Axis Confound Structure), Appendix K
- 问题：Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，**shrinkage 达 49%**。论文诚实地报告了这一点（Table 2 caption 引用 Nemes et al., 2009），但只对 9 个 judge×axis 配置中的 **1 个**做了 n=355 复制。GPT-4o formality Style OR 在 n=88 时为 2.58 [1.41, 4.73]——如果经历类似 49% shrinkage，将降至 ~1.32，CI 将跨越 1.0（即不显著）。论文对 verbosity 的推断是「ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)」（Section 5.2, ¶Sample-size sensitivity），但这是外推，未经实证验证。
- 为什么影响接收：GEE conditional decomposition 是论文两大贡献之一（区分 style-dominated vs. quality-confounded）。如果 OR 估计因小样本系统性膨胀，formality 的「conditional」分类和 verbosity 的「style-dominated」分类可能不可靠。特别是 Gemini formality Style OR = 1.64 [0.91, 2.98] 在 n=88 时已不显著——shrinkage 后几乎必然为零。
- 建议修改方向：至少对 verbosity（一个 judge）补做 n=355 复制，实证验证 shrinkage 预测。或者更保守地将 Table 2 的 n=88 OR 呈现为 upper-bound estimates（论文 caption 已提到但正文讨论不足）。

**N2** [critical] 跨 benchmark 复制为确认偏差式选择（6/24 cells）
- 具体位置：Section 5.3, Figure 6, Table 22 (Appendix W)
- 问题：论文在 AlpacaEval 和 MT-Bench 上仅测试 24 个可能的 benchmark×judge 配置中的 6 个，且明确说选择标准为「targeting the strongest effects from the primary LLMBar analysis」（Section 5.3 最后一段）。这是经典的确认偏差——选最强效应去复制，复制成功率自然高。3 个例外（‡ 行，Likert 也检测到 bias）被 post-hoc 解释为 effect-size dependence，但这一解释未被前瞻性验证。
- 为什么影响接收：cross-benchmark replication 是论文用于论证 CSD generalizability 的关键证据。如果只展示最强效应的复制结果，无法判断 Blindspot 在中等效应水平上是否存在——而大多数实际场景中效应可能是中等的。
- 建议修改方向：报告全部 24 cells（即使部分 not significant），或采用预注册的选择标准（如随机选择 50% cells）。至少应包含一些中等效应配置以测试 Blindspot 在较弱效应下是否持续。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Likert Blindspot 缺少正式的 divergence 检验
- 具体位置：Section 5.1 (The Likert Blindspot)
- 问题：论文分别展示「BT 显著」和「Likert 不显著」，但从未正式检验二者**是否显著不同**。Absence of evidence（Likert p > 0.05）不等于 evidence of absence。当然，n=355 attenuation（d → 0）部分缓解了这一问题，但仅对一个配置。形式上，论文需要测量模式 × 风格的交互检验，或 paired-difference 分析。
- 建议：添加 measurement-mode interaction test 或至少讨论为什么非正式比较在此情境下是足够的。论文可以论证 Likert 的 raw p-values 远离显著性阈值（最小 p = 0.179），因此即使考虑多重比较也不会改变结论。

**W2** [warning] Qwen3-32B 的 evaluator-producer overlap
- 具体位置：Appendix E (Table 6, Table 7), Section 5.3
- 问题：Qwen3-32B 同时为 rewriter 和 target judge。独立 rewriter 测试（Appendix E）显示 verbosity Style OR 下降 22%（13.10 → 10.17）。22% 不是小数目——近四分之一的测量到的 style preference 可能来自自评估偏差。且 n=355 唯一复制恰好选用了有 overlap 的 Qwen3-32B。
- 建议：(1) 在 Discussion/Limitations 更显著地讨论此局限；(2) 考虑 n=355 复制是否应使用 GPT-4o 作 rewriter，以排除 overlap 对放大倍数的贡献。

**W3** [warning] Claude Sonnet 4 负对照不充分
- 具体位置：Appendix H (Table 9, Table 10)
- 问题：TOST 等价性仅在 Δ=12pp 时显著（p=.035），在 Δ=10pp 时不显著（p=.100）。贝叶斯因子 BF₀ < 3（inconclusive，未强烈支持零假设）。12pp 意味着 ~12% 的偏好对方向翻转——对下游 RLHF 而言这是 practically meaningful 的差异。论文将此定义为「small effect (Cohen's h = 0.24)」（Appendix H），但等价边界的选择缺乏独立于数据的先验理由——the Δ=12pp 恰好是 pooled 结果首次显著的阈值。
- 建议：将 Claude 定位为「weak-bias case」而非「negative control」更为准确。或提供等价边界的独立理由（如来自 RLHF 实践的 minimum meaningful effect）。

**W4** [warning] FK grade 的 mediator vs. confounder 辨识不足
- 具体位置：Section 5.3 最后两段, Appendix U
- 问题：论文断言「FK grade lies on the causal pathway S → FK → Y: the intervention directly alters readability, making FK a mediator rather than a confounder」（Section 5.3）。但 Sobel 中介检验建立的是统计中介，不是因果中介。替代因果结构——FK 和 Style 都是 rewriting 过程的结果，FK 独立地影响 Y（混淆结构）——在统计上不可区分。在 mediator 解释下控制 FK 得到直接效应（OR=2.15），在 confounder 解释下控制 FK 得到无混淆效应——二者对应不同的政策含义。
- 建议：呈现两种因果解释并讨论其对估计的不同含义，而非仅断言 mediator。

**W5** [warning] GEE 模型潜在的遗漏变量偏差
- 具体位置：Section 5.2, Appendix D
- 问题：GEE 仅含两个预测变量（style direction, originality preference）。论文在 Section 5.2 承认「omitted variables (text length, lexical complexity) may partly confound both terms」，但未系统检验敏感性。FK grade 仅在 Appendix U 对 formality 做了检验，未对 verbosity 做。Verbosity 与文本长度高度相关（Appendix T 中 cross-axis contamination 分析暗示了这一点），长度控制后 Style OR 变化 <2%（Section 5.3），但这仅是加入长度控制的 GEE 结果，不是对 omitted variable bias 的系统敏感性分析。
- 建议：报告 E-value 或 Rosenbaum bounds 来量化未观测混淆需要多大才能推翻结论。

---

## 小问题（不影响接收）
- 「Likert」一词的使用：论文用 1-10 整数量表，严格来说是 interval rating scale 而非经典 5-point Likert scale。Likert (1932) 的原始定义更窄。建议添加一句澄清。
- BT 正则化参数 α=10⁻⁶ 实质上为零正则化。虽然 n=88 下 BT 可识别，但在少数高度不一致的 pair 上可能导致极端参数估计。建议报告 α 的敏感性。
- Table 1 的 "Cat." 列标注（†, †_e, †_c, ---）较难解析，建议改为更直观的标签。
- Appendix 组织虽有目录（page 11 顶部），但 20 页中 12 页为附录，ratio 偏高。部分内容（如 Table 3 的 GEE correlation structure 全部 <0.001）可压缩。

---

## 提问
1. n=355 复制是否使用相同 NLI gating threshold (0.90)？pass rate 是否可比？
2. 各 judge 的 Likert 评分分布是什么？如果 judge 集中在某几个分数点（如 7-8），这直接解释了 tie rate 和 Blindspot。
3. Section 1 提到「76-92% of preferences originate from style cues」——这个范围如何计算？
4. 为什么 n=355 复制只选了 Qwen3-32B formality？是否有资源或时间约束？

---

## 缺失引用
- Likert (1932). A technique for the measurement of attitudes. 论文大量使用「Likert」一词但未引用原始文献。
- 关于测量模式对偏好引出的影响：Schwarz (1999) Self-reports; Johnson & Goldstein (2003) defaults in choice architecture——与 Blindspot 的 measurement-mode framing 相关。

---

## 主要优势
1. **现象定义清晰**：Likert Blindspot 是一个明确、可操作的概念，直接挑战 LLM 评估实践中的单一评估模式假设。
2. **方法论体系化**：CSD 将 NLI gating、style-controlled rewriting、GEE decomposition 组合成完整的分析框架，各环节有明确的方法论依据。
3. **Robustness 检查极其充分**：11 个 NLI 阈值、一致性筛选对比、独立 rewriter、人工标注（AC₁=0.96）、6 个 amplification controls、cross-benchmark 复制——超过同类论文的平均水准。
4. **因果声明的适当克制**：论文明确表示「interventional rather than formal causal evidence」（Appendix A），不 invoke SUTVA 或 consistency assumptions，DAG 也标注为「assumed data-generating process, not a claim of perfect identification」。
5. **敏感性分层分析（7 种方法，同一数据）**有效证明 Blindspot 不是特定检验的 artifact。
6. **Bootstrap attenuation analysis**（Appendix K）比标准 post-hoc power 更合理，且论文正确引用了 Hoenig & Heisey (2001) 的批判。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1484 · 2026-05-23T14:31:24.790103+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] GEE 小样本膨胀严重，仅一个配置在 n=355 复制\n- Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，shrinkage 达 49%。但只对 9 个 judge×axis 配置中的 1 个做了 n=355 复制。GPT-4o formality Style OR 在 n=88 时为 2.58 [1.41, 4.73]——如果经历类似 49% shrinkage，将降至 ~1.32，CI 将跨越 1.0（即不显著）。论文对 verbosity 的推断是外推，未经实证验证。\n\n**N2** [critical] 跨 benchmark 复制为确认偏差式选择（6/24 cells）\n- 仅测试 24 个可能的 benchmark×judge 配置中的 6 个，且明确选择标准为「targeting the strongest effects」。3 个例外（‡ 行）被 post-hoc 解释为 effect-size dependence，未被前瞻性验证。\n\n### Should-Fix\n\n**W1** [warning] Likert Blindspot 缺少正式的 divergence 检验\n- 论文分别展示「BT 显著」和「Likert 不显著」，但从未正式检验二者是否显著不同。Absence of evidence ≠ evidence of absence。\n\n**W2** [warning] Qwen3-32B 的 evaluator-producer overlap\n- 独立 rewriter 测试显示 verbosity Style OR 下降 22%（13.10 → 10.17）。22% 不是小数目。且 n=355 唯一复制恰好选用了有 overlap 的 Qwen3-32B。\n\n**W3** [warning] Claude Sonnet 4 负对照不充分\n- TOST 等价性仅在 Δ=12pp 时显著（p=.035），在 Δ=10pp 时不显著。贝叶斯因子 BF₀ < 3（inconclusive）。等价边界的选择缺乏独立于数据的先验理由。\n\n**W4** [warning] FK grade 的 mediator vs. confounder 辨识不足\n- Sobel 中介检验建立的是统计中介，不是因果中介。替代因果结构在统计上不可区分。\n\n**W5** [warning] GEE 模型潜在的遗漏变量偏差\n- GEE 仅含两个预测变量。建议报告 E-value 或 Rosenbaum bounds。\n\n### Questions\n1. n=355 复制是否使用相同 NLI gating threshold？\n2. 各 judge 的 Likert 评分分布是什么？\n3. 「76-92% of preferences originate from style cues」如何计算？\n4. 为什么 n=355 复制只选了 Qwen3-32B formality？\n\n### Missing References\n- Likert (1932) 原始文献\n- Schwarz (1999) Self-reports\n- Johnson & Goldstein (2003) defaults in choice architecture\n\n---\n\n请逐条回应每个 Must-Fix 和 Should-Fix。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
  "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] GEE 小样本膨胀严重，仅一个配置在 n=355 复制\n- Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，shrinkage 达 49%。但只对 9 个 judge×axis 配置中的 1 个做了 n=355 复制。GPT-4o formality Style OR 在 n=88 时为 2.58 [1.41, 4.73]——如果经历类似 49% shrinkage，将降至 ~1.32，CI 将跨越 1.0（即不显著）。论文对 verbosity 的推断是外推，未经实证验证。\n\n**N2** [critical] 跨 benchmark 复制为确认偏差式选择（6/24 cells）\n- 仅测试 24 个可能的 benchmark×judge 配置中的 6 个，且明确选择标准为「targeting the strongest effects」。3 个例外（‡ 行）被 post-hoc 解释为 effect-size dependence，未被前瞻性验证。\n\n### Should-Fix\n\n**W1** [warning] Likert Blindspot 缺少正式的 divergence 检验\n- 论文分别展示「BT 显著」和「Likert 不显著」，但从未正式检验二者是否显著不同。Absence of evidence ≠ evidence of absence。\n\n**W2** [warning] Qwen3-32B 的 evaluator-producer overlap\n- 独立 rewriter 测试显示 verbosity Style OR 下降 22%（13.10 → 10.17）。22% 不是小数目。且 n=355 唯一复制恰好选用了有 overlap 的 Qwen3-32B。\n\n**W3** [warning] Claude Sonnet 4 负对照不充分\n- TOST 等价性仅在 Δ=12pp 时显著（p=.035），在 Δ=10pp 时不显著。贝叶斯因子 BF₀ < 3（inconclusive）。等价边界的选择缺乏独立于数据的先验理由。\n\n**W4** [warning] FK grade 的 mediator vs. confounder 辨识不足\n- Sobel 中介检验建立的是统计中介，不是因果中介。替代因果结构在统计上不可区分。\n\n**W5** [warning] GEE 模型潜在的遗漏变量偏差\n- GEE 仅含两个预测变量。建议报告 E-value 或 Rosenbaum bounds。\n\n### Questions\n1. n=355 复制是否使用相同 NLI gating threshold？\n2. 各 judge 的 Likert 评分分布是什么？\n3. 「76-92% of preferences originate from style cues」如何计算？\n4. 为什么 n=355 复制只选了 Qwen3-32B formality？\n\n### Missing References\n- Likert (1932) 原始文献\n- Schwarz (1999) Self-reports\n- Johnson & Goldstein (2003) defaults in choice architecture\n\n---\n\n请逐条回应每个 Must-Fix 和 Should-Fix。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
    "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-23T14:31:47.509184+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22719
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-23T14:31:49.971579+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer\n- Title \"The Likert Blindspot\" 和 Abstract 暗示新发现的现象。Introduction 的三个 \"LLM-specific distinctions\" 中，(c) \"near-complete binary split\" 被论文自己承认 \"consistent with classical predictions when accounting for effect-size-dependent power\"——这不是 LLM-specific distinction。\n- 建议：将 contribution 定位为 \"systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool\" 而非 \"new phenomenon\"。\n\n**N2** [critical] Scaled replication 覆盖不足——仅一个 cell 有大样本验证\n- n=355 仅覆盖 Qwen3-32B × formality。其他 11 个 primary/confirmatory cells 无法排除纯 power 问题。Gemini formality（BT 仅 57.4%）如果做 scaled replication 可能不复现。\n- 建议：至少对一个 verbosity cell 做 scaled replication，或在 Limitations 明确承认 coverage gap。\n\n### Should-Fix\n\n**W1** [warning] Title \"The Likert Blindspot\" 暗示单一因果方向，与正文 nuanced 讨论矛盾\n- \"Blindspot\" 预设 attenuation 解释。如果 amplification 是主因，Likert 没有\"盲点\"，是 pairwise 有\"放大镜\"。\n\n**W2** [warning] Qwen3-32B rewriter-judge overlap（~20% inflation）\n- 独立 rewriter 测试（Appendix E）显示 OR 下降 22%，说明 evaluator-producer overlap 确实 inflate 效应量。\n\n**W3** [warning] Register 轴结果弱且 exploratory，应移至 Appendix\n- Register BT 仅 .553–.635，GEE 显示 Originality OR 远高于 Style OR。效应可能主要由 quality confounding 驱动。\n\n**W4** [warning] \"Systematic pattern\" / \"consistent\" 与 ~30% exception rate 的张力\n- Claude 不显示一般性 Blindspot，Gemini formality 效应弱，cross-benchmark 仅 6/24 cells。~30% exception rate 下 \"consistent\" 值得审慎使用。\n\n### Questions\nQ1. 76.6% non-tie concordance 中 23.4% discordance 是否足够低以排除 partial construct divergence？\nQ2. 100-point continuous Likert 是否有 evidence 表明 judges 真的利用了 granularity？\nQ3. Qwen3-32B 作为 style classifier 是否引入 confounding？\nQ4. GEE exchangeable correlation 中 α̂ = −0.25 是否算\"接近零\"？\n\n### Missing References\n- IRT 在 NLG evaluation 中的应用（Polo et al., 2024, TinyBenchmarks）\n- Likert scale anchoring effects\n- Munos et al. (2023) Nash Learning from Human Feedback\n\n---\n\n请逐条回应每个 Must-Fix 和 Should-Fix。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
  "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer\n- Title \"The Likert Blindspot\" 和 Abstract 暗示新发现的现象。Introduction 的三个 \"LLM-specific distinctions\" 中，(c) \"near-complete binary split\" 被论文自己承认 \"consistent with classical predictions when accounting for effect-size-dependent power\"——这不是 LLM-specific distinction。\n- 建议：将 contribution 定位为 \"systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool\" 而非 \"new phenomenon\"。\n\n**N2** [critical] Scaled replication 覆盖不足——仅一个 cell 有大样本验证\n- n=355 仅覆盖 Qwen3-32B × formality。其他 11 个 primary/confirmatory cells 无法排除纯 power 问题。Gemini formality（BT 仅 57.4%）如果做 scaled replication 可能不复现。\n- 建议：至少对一个 verbosity cell 做 scaled replication，或在 Limitations 明确承认 coverage gap。\n\n### Should-Fix\n\n**W1** [warning] Title \"The Likert Blindspot\" 暗示单一因果方向，与正文 nuanced 讨论矛盾\n- \"Blindspot\" 预设 attenuation 解释。如果 amplification 是主因，Likert 没有\"盲点\"，是 pairwise 有\"放大镜\"。\n\n**W2** [warning] Qwen3-32B rewriter-judge overlap（~20% inflation）\n- 独立 rewriter 测试（Appendix E）显示 OR 下降 22%，说明 evaluator-producer overlap 确实 inflate 效应量。\n\n**W3** [warning] Register 轴结果弱且 exploratory，应移至 Appendix\n- Register BT 仅 .553–.635，GEE 显示 Originality OR 远高于 Style OR。效应可能主要由 quality confounding 驱动。\n\n**W4** [warning] \"Systematic pattern\" / \"consistent\" 与 ~30% exception rate 的张力\n- Claude 不显示一般性 Blindspot，Gemini formality 效应弱，cross-benchmark 仅 6/24 cells。~30% exception rate 下 \"consistent\" 值得审慎使用。\n\n### Questions\nQ1. 76.6% non-tie concordance 中 23.4% discordance 是否足够低以排除 partial construct divergence？\nQ2. 100-point continuous Likert 是否有 evidence 表明 judges 真的利用了 granularity？\nQ3. Qwen3-32B 作为 style classifier 是否引入 confounding？\nQ4. GEE exchangeable correlation 中 α̂ = −0.25 是否算\"接近零\"？\n\n### Missing References\n- IRT 在 NLG evaluation 中的应用（Polo et al., 2024, TinyBenchmarks）\n- Likert scale anchoring effects\n- Munos et al. (2023) Nash Learning from Human Feedback\n\n---\n\n请逐条回应每个 Must-Fix 和 Should-Fix。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d",
    "director_session_key": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-23T14:31:51.276459+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1304
}
```

</details>

---


### Assistant

_source line 1488 · 2026-05-23T14:31:56.845421+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 141

## Round 141

2 recorded events


### User

_source line 1489 · 2026-05-23T14:31:59.395913+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评价：**Overall 3.5 (Borderline Conference)**。论文定义了 Likert Blindspot 这一有实际价值的现象，CSD + GEE 框架设计精巧，robustness 检查远超平均水准。两个 must-fix 问题：(1) GEE 在 n=88 下存在 49% 的小样本膨胀，9 个配置中仅 1 个做了 n=355 复制；(2) 跨 benchmark 复制仅选了 6/24 最强效应的 cells，存在确认偏差风险。五个 should-fix 涉及缺少正式 divergence 检验、evaluator-producer overlap、负对照不充分、FK mediator 辨识不足、GEE 遗漏变量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1490 · 2026-05-23T14:32:05.146613+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1491 · 2026-05-23T14:33:36.847356+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 回应

### R1-N1: GEE 小样本膨胀严重，仅一个配置在 n=355 复制

**[AGREE]** 同意这是论文的主要弱点之一，与我的 N2 指出的问题高度重叠。

补充论证：
- R1 的推算有说服力——GPT-4o formality Style OR 2.58 经历 49% shrinkage 后约为 1.32，CI 确实可能跨 1.0。这会从根本上动摇 GPT-4o formality 的 "conditional style effect" 结论。
- 但需要区分两个 claim 的受影响程度不同：(1) **Blindspot 的存在性**（BT 显著 vs Likert 不显著）不依赖 GEE OR 的绝对值——BT win probability（Table 1）是非参数的，不受小样本 OR 膨胀影响；(2) **GEE per-axis confound structure** 的定量描述确实受影响。因此 N1 主要威胁的是 GEE 相关结论，而非 Blindspot 核心发现本身。
- 论文在 §5.2 最后一段对 verbosity 的外推论证（"even under ~50% shrinkage, projected 4–6.5, still ≫ Orig OR < 1"）逻辑上成立但未经实证验证，R1 指出这一点是正确的。

**结论**：应要求至少对一个 verbosity cell 做 scaled replication，或将 verbosity 的 GEE 定量结论明确标注为 "projected, pending large-sample validation"。

---

### R1-N2: 跨 benchmark 复制为确认偏差式选择（6/24 cells）

**[AGREE]** 部分同意，但严重性判断略有不同。

- R1 的批评——选择 "targeting the strongest effects" 构成确认偏差——在方法论上是正确的。如果只测试预期最强的 cells，6/24 的显著率无法代表 generalizability。
- 但论文将 cross-benchmark 分析定位为 **exploratory**（§4.1 "Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control"；Figure 6 caption 中 "Grey ×: not tested"），并未将其作为核心 contribution。论文的主要 claims 建立在 LLMBar 上，cross-benchmark 是补充证据。
- 真正的问题是 §1 Contribution 2 的措辞——"the first at this scale"——暗示了比实际完成的更全面的 cross-benchmark 覆盖。如果改为 "with selective cross-benchmark evidence"，批评力度会大幅降低。
- 3 个 ‡ exceptions 的 post-hoc "severity spectrum" 解释（§5.1 最后一段）确实缺乏 pre-registration，R1 的批评成立。

**结论**：应将 Contribution 2 的措辞弱化，明确 cross-benchmark 的 exploratory 性质和选择标准。但这不应作为 Must-Fix，因为论文的主要 claims 不依赖于 cross-benchmark generalization。建议降级为 Should-Fix。

---

## Should-Fix 回应

### R1-W1: Likert Blindspot 缺少正式的 divergence 检验

**[AGREE]** 这是一个好的统计学观点，我的审稿遗漏了这一点。

- R1 准确识别了一个逻辑缺口：论文分别展示 "BT 显著" 和 "Likert 不显著"，但从未检验两个 effect size 是否 statistically significantly different。"Absence of evidence is not evidence of absence" 在此完全适用。
- 论文用 n=355 的 TOST equivalence testing（Appendix H, Δ=12pp 时 p=.035）和 bootstrap attenuation analysis（Appendix K, d 不随 n 增长而偏离零）间接回应了这一点，但正式的 measurement-mode interaction test（e.g., 将 measurement mode 作为 within-subject factor 的 mixed-effects model）确实缺失。
- 这是可以在 revision 中补充的分析，且可能加强论文的论点。

**结论**：同意应补充正式的 divergence 检验。一种方法是 bootstrap the difference in effect sizes between BT and Likert，检验该差异是否显著异于零。

---

### R1-W2: Qwen3-32B 的 evaluator-producer overlap

**[AGREE]** 与我的 W2 一致。

- 补充 R1 的论点：n=355 复制恰好选择了有 overlap 的 Qwen3-32B 这一点尤其值得警惕。如果 n=355 复制使用无 overlap 的 GPT-4o 作为 target judge（GPT-4o rewriter → GPT-4o judge 也有 overlap，但 Qwen3 rewriter → GPT-4o judge 无 overlap），结论会更 clean。
- Appendix E 的独立 rewriter 验证（Table 6）显示 Blindspot 仍然存在（GPT-4o rewriter: Style OR = 10.17, p = 0.001; Blindspot: Yes），所以 overlap 影响的是效应量级而非现象存在性。

**结论**：同意应更突出标注 overlap caveat，并建议至少一个 scaled replication 使用非 overlap 配置。

---

### R1-W3: Claude Sonnet 4 负对照不充分

**[AGREE]** R1 的批评在技术上准确。

- TOST 在 Δ=12pp 才显著（p=.035），在 Δ=10pp 时不显著——这意味着我们只能排除 ≥12pp 的效应，而 12pp 对于 BT win probability 来说是一个相当宽松的等价边界（对应约 .62 的 BT，接近某些弱 Blindspot cells 的效应量）。
- BF₀ < 3 确实是 inconclusive by conventional Bayesian standards（Jeffreys scale 要求 BF > 3 为 moderate evidence）。
- 等价边界 Δ=12pp 的选择在 Appendix H 中描述为 "the smallest margin at which pooled significance is achieved"——这是 data-driven 而非 a priori，R1 指出 "缺乏独立于数据的先验理由" 是正确的。
- 但 Claude 的价值不完全取决于 equivalence testing。论文更多用 Claude 的 benchmark-dependent profile（LLMBar n.s., AEval verbosity OR = 4.76 significant）作为 discriminative validity 证据（§5.3），说明 CSD 不是 universal false positive machine。这个论证不依赖 TOST。

**结论**：同意 TOST 分析的 boundary justification 不足，建议弱化 Claude 作为 "negative control" 的 claim，转而强调其 "discriminative validity" 角色——CSD 在不同 judges 上给出不同结论，这本身就说明框架不是 universal false positive。

---

### R1-W4: FK grade 的 mediator vs. confounder 辨识不足

**[AGREE]** R1 的因果推理论点是正确的。

- 论文在 §5.3 声称 "FK lies on the causal pathway S → FK → Y: the intervention directly alters readability, making FK a mediator rather than a confounder"。这个因果方向 claim 是 reasonable but not testable with observational data alone。
- 替代因果结构确实存在：如果存在一个未观测的共因（e.g., text complexity）同时影响 FK grade 和 judge score，那么 FK 是 collider 而非 mediator，conditioning on it 会引入 collider bias。
- 但从 domain knowledge 看，S → FK 的方向是 plausible 的——formality 的 rewriting 确实会改变 readability（formal text 倾向使用更复杂的句式）。这是 a priori reasonable 的因果方向，但论文应更清楚地标注这是 an assumed causal model。

**结论**：同意应将 mediator claim 降级为 "plausible under the assumed causal model" 而非 definitive。

---

### R1-W5: GEE 模型潜在的遗漏变量偏差

**[REBUT]** 部分反驳。

- R1 建议报告 E-value 或 Rosenbaum bounds。这对于声称因果效应的观察性研究是标准做法，但论文在 Appendix A（Design Rationale）中明确声明 "Our approach provides interventional rather than formal causal evidence"，且 Limitations 第一条直接承认 residual confounding。
- GEE 在论文中的角色是 **descriptive decomposition**（将 BT 效应分解为 style 和 originality 成分），而非因果推断工具。论文使用 "conditional" 而非 "causal"。在这个定位下，omitted variable bias 确实存在但不威胁论文的核心 claim——论文没有声称 GEE 给出因果效应。
- 但 R1 的建议仍有价值：报告 E-value 不需要声称因果关系，它量化的是 "需要多强的未观测混淆才能解释掉观测到的 association"。对于 verbosity 的 Style OR = 8–13，E-value 会非常高（说明 extremely strong confounding 才能消除效应），这实际上会加强论文的论证。

**结论**：论文定位 GEE 为 descriptive 而非 causal，omitted variable 批评的杀伤力有限。但同意报告 E-value 是一个 costless improvement，建议在 revision 中添加。

---

## Questions 回应

### Q1: n=355 复制是否使用相同 NLI gating threshold？

我在论文中未找到明确说明。§3.2 设定 threshold = 0.90，§4.2 提到 n=355 是 "4× scaled replication"——合理推测使用相同 threshold，但 R1 要求明确声明是正确的。Appendix F 的 NLI threshold sensitivity sweep 仅在 n=88 上做，未提及 n=355。

### Q2: 各 judge 的 Likert 评分分布是什么？

这是一个好的要求。论文在 §5.1 提到 "Likert tie rates of 58–73%"，但没有展示完整分布（e.g., histogram）。这些分布对于理解 tie inflation 机制至关重要——是 judges 倾向使用中间值（central tendency bias），还是整体集中在高分区（ceiling effect）？

### Q3: 「76-92% of preferences originate from style cues」如何计算？

这不是论文自己的计算，而是引用 li2026preference 和 soumik2026judging 的结论（§1 para 1）。但 R1 的问题合理——引用他人的 claim 时应注意该 claim 的 operationalization 是否与本文一致。

### Q4: 为什么 n=355 复制只选了 Qwen3-32B formality？

论文未解释选择理由。可能的原因：(1) Qwen3-32B 也是 rewriter，数据生成成本最低；(2) formality 是两个 primary axis 之一。但 R1 隐含的批评是正确的——这个选择引入了 evaluator-producer overlap，不是最 clean 的验证。

---

## Missing References 回应

### Likert (1932)
**[AGREE]** 引用 Likert 原始文献是合理的建议。论文大量讨论 Likert scale 的局限性，却未引用其原始提出者。虽然 Stevens (1946) 已被引用，但 Likert (1932) 作为 construct 的 origin 值得加入。

### Schwarz (1999) Self-reports
**[REBUT]** 边际相关。Schwarz 的 self-report 认知模型主要针对人类被试的 survey response，LLM judge 的 "self-report" 机制不同（不涉及 memory retrieval 或 social desirability）。可以在 Related Work 一句话提及，但非必须。

### Johnson & Goldstein (2003) defaults in choice architecture
**[REBUT]** 与论文主题距离较远。论文关注的是 measurement mode（Likert vs pairwise）的敏感性差异，不涉及 default option framing。Choice architecture 文献的相关性有限。

---

## 综合评估

Reviewer 1 的审稿意见整体质量很高，统计学功底扎实。两个 Must-Fix 中：
- **N1（GEE 小样本膨胀）**：完全同意，但需要区分对 GEE 定量结论 vs Blindspot 存在性的影响
- **N2（cross-benchmark 选择偏差）**：同意 concern，但建议降级为 Should-Fix（论文主 claims 不依赖 cross-benchmark）

五个 Should-Fix 中，W1（缺少 formal divergence test）和 W3（Claude TOST boundary）是我审稿时遗漏的好观点。W5（GEE omitted variables）我部分反驳——论文定位 GEE 为 descriptive，omitted variable 批评的前提不完全成立，但报告 E-value 是低成本改进。

R1 和我的 Overall 评分一致（3.5, Borderline Conference），且核心关切高度重叠：**scaled replication 覆盖不足**是两位 reviewer 共同识别的最大问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1492 · 2026-05-23T14:33:49.974394+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1493 · 2026-05-23T14:33:54.279041+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 审稿意见的逐条回应，汇报给 Director。

核心判断：
- **N1（GEE 小样本膨胀）**：完全同意，但区分了对 GEE 定量结论 vs Blindspot 存在性的不同影响
- **N2（cross-benchmark 选择偏差）**：同意 concern，建议降级为 Should-Fix
- **W1（缺 formal divergence test）**：同意，这是我遗漏的好观点
- **W3（Claude TOST）**、**W4（FK mediator）**：同意
- **W5（GEE omitted variables）**：部分反驳——论文定位 GEE 为 descriptive 而非 causal，但同意报告 E-value 是低成本改进

两位 Reviewer 的共识：**scaled replication 覆盖不足**是最大问题，Overall 评分一致（3.5, Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1494 · 2026-05-23T14:34:05.551373+00:00_

等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 144

## Round 144

16 recorded events


### User

_source line 1495 · 2026-05-23T14:35:00.921777+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: 新颖性定位不够精确**
同意 R2 的核心判断。Introduction line 13 明确写到「(c) the divergence manifests as a near-complete binary split... consistent with classical predictions when accounting for effect-size-dependent power (Figure 4)」——论文自己承认 (c) 不是 LLM-specific。Thurstone (1927) 早已建立 pairwise comparison 的 discriminability 优势，Introduction line 12 也引用了这一点：「The classical psychometric literature establishes that pairwise comparison yields higher discriminability than absolute rating」。

但我认为 R2 的建议（重新定位为「systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool」）**方向正确但稍有低估**。论文的两个真正新贡献是：
1. **GEE per-axis decomposition**（Table 2）——verbosity 是 style-dominated (OR 8–13, Orig OR <1)，formality 是 quality-confounded (Orig OR 2.3–5.0)。这一结构差异不是 Thurstone 能预测的，是 LLM-specific 的实证发现。
2. **完整的诊断管线（CSD）**——NLI gating + style rewriting + GEE decomposition 的组合，先前工作只解决了其中的子问题（RATE 做 Likert ATE，CASSE/FairJudge 做 multi-dimensional analysis）。

建议：标题和 Abstract 应降低「new phenomenon」的暗示，改为「systematic demonstration in LLM judges reveals per-axis structure not predicted by classical theory」。

**[AGREE] R2-N2: Scaled replication 覆盖不足**
完全同意，这与我的 N1 一致。补充两点支持：

1. **GPT-4o formality 的风险**：Style OR = 2.58 [1.41, 4.73] 在 n=88。按 Qwen3-32B 49% shrinkage 外推，降至 ~1.32，CI 将包含 1.0。论文未对此风险建模。

2. **Verbosity 的反向论证缺少实证**：Section 5.2 说「Verbosity Style ORs (8–13) would remain style-dominated even under ~50% shrinkage (projected 4–6.5, still ≫ Orig OR <1)」。这是合理的推断，但推断不等于验证。至少需要一个 verbosity cell 的 n=355 复制来 calibrate shrinkage 幅度——verbosity 的 shrinkage 可能不同于 formality（不同效应量级、不同 confound 结构）。

---

### Should-Fix

**[AGREE] R2-W1: Title 暗示单一因果方向**
同意 R2 的分析。「Blindspot」语义预设 Likert 遗漏了真实信号（attenuation 解释）。但 Section 5.1 的三种解释框架明确包括 amplification 和 construct divergence。这一 mismatch 在 Introduction line 5–7 被部分缓解——论文将 Blindspot 定义为「an operational descriptor for the measurement-mode divergence... without committing to a specific causal mechanism」——但 title 的 framing power 远大于正文的 qualifier。

不过我认为这个问题**严重程度中等**：论文的实证证据（n=355 attenuation d→0, 76.6% concordance, 6 amplification controls）整体上**更支持 attenuation 而非 amplification**。Title 的方向与证据权重一致，只是过于确定。

**[AGREE] R2-W2: Qwen3-32B rewriter-judge overlap**
同意，与我的 W2 完全一致。补充一点：Appendix E Table 7 formality 结果显示独立 rewriter 下 BT 从 .665 降至 .644（Δ = −2.1pp），比 verbosity 的 22% OR 降幅温和。这说明 overlap 效应是 axis-dependent 的——verbosity 方向的 overlap inflation 更严重，可能因为 Qwen3-32B 的 verbose output style 与其偏好一致。

**[REBUT] R2-W3: Register 轴应移至 Appendix**
部分反对。Register 结果确实更弱（BT .553–.635，Table 1），且 GEE 显示 Orig OR 显著高于 Style OR（Table 2: Qwen3 reg Style OR = 1.91, Orig OR = 5.72）。但保留 register 在主文中有方法论价值：

1. **Per-axis structure 多样性**：主文需要展示「不同轴有不同 confound 结构」——verbosity (style-dominated), formality (conditional), register (quality-dominated) 构成一个完整谱系。只展示 verbosity 和 formality 不足以支撑 GEE decomposition 作为通用诊断工具的 claim。
2. **论文已标注为 exploratory**：Table 1 的 †_e 标记和 Section 4.1 明确将 register 排除在 FWER 校正之外。
3. 但同意应**缩减篇幅**：Table 2 的 register 行和 Figure 5 的 register panel 可压缩。

**[REBUT] R2-W4: "Consistent" 与 ~30% exception rate 的张力**
部分反对。R2 的 ~30% exception rate 计算方式存在问题：

1. **Claude 是负对照，不是例外**。Claude 的 2 个 cells 设计上就不应该显示 Blindspot（Section 4.1: Claude Sonnet 4 provides discriminative validity evidence）。排除负对照后，8/8 bias-positive cells 都显示 Blindspot（Table 1 的 3 judges × 2 axes + Gemini 2 axes，全部 BT significant + Likert not significant）。

2. **Gemini formality 不是例外而是 spectrum**。Gemini formality BT = 57.4% (p = 0.031) 仍然显著，只是效应较弱。GEE 显示它是 originality-dominated（Style OR = 1.64 n.s., Orig OR = 2.51 p = 0.002），这恰好证明了 GEE decomposition 的诊断价值——它能区分 genuine style sensitivity 和 quality confounding。

3. **Cross-benchmark 6/24 cells 确实是选择性的**——我与 R2 在此一致（我的 N2），但这是覆盖率不足而非 inconsistency。

所以更准确的数字是：primary + confirmatory cells 中 Blindspot 一致性为 8/8 (100%)，加上 Gemini formality（弱但显著）为 10/10。「Consistent」在这个范围内是合理的。Cross-benchmark 和 Claude 是独立问题。

---

### Questions

**Q1: 76.6% concordance 是否足以排除 partial construct divergence？**
不足以完全排除。Appendix W (Table/Section non-tie concordance) 显示 pooled 76.6% [70.3, 81.9]，但分 axis 看差异显著：verbosity 74–88%，formality 较低。23.4% discordance 有三种解释：(a) 测量噪声，(b) partial construct divergence，(c) Likert 评分的 ceiling/floor effects 导致方向反转。论文在 Section 5.1 和 Appendix K 已承认 partial construct divergence 未被排除——「evidence more consistent with measurement attenuation than construct divergence, though partial construct divergence remains at weaker effect sizes」。我认为论文在此的措辞是适当的。

**Q2: 100-point continuous Likert 是否有 evidence judges 利用了 granularity？**
好问题。Appendix O (Section O, 100-Point Continuous Likert Scale) 仅报告「all three judges remain non-significant (p > 0.15)」但未报告评分分布。如果 judges 在 100-point scale 上仍然 cluster（如 round to nearest 10），则 granularity 假说被否定——tie rate 不会因 scale 扩展而降低。论文应报告 100-point scale 的评分分布或至少 unique-value count。

**Q3: Qwen3-32B 作为 style classifier 是否引入 confounding？**
风险有限。Style classification（binary: formal vs. casual）决定了 rewriting direction，但 NLI gate（DeBERTa-v3, threshold 0.90）独立于 Qwen3-32B 运行，catch 了 classification 错误导致的无效 rewrite。更关键的是，即使 classification 有系统误差，它只影响 balanced sampling（formal→casual vs. casual→formal 的比例），不影响每个 pair 内的 style contrast。Direction asymmetry analysis（Appendix B）已检测并量化了这一不平衡（formal-origin 78.8% vs. casual-origin 54.5%），GEE 通过 originality term 控制了它。

**Q4: GEE α̂ = −0.25 是否算「接近零」？**
R2 提了一个好的技术点。α̂ ∈ [−0.25, +0.11]（Appendix D, Section 4.1）中 −0.25 是 moderate negative correlation，不算「接近零」。但 GEE 的关键优势在于：sandwich standard errors 对 working correlation misspecification 是 robust 的。Appendix D Table 3 显示 exchangeable 和 independence 结构的 QIC 差异 <0.001，coefficient change <0.02——这意味着即使 α̂ = −0.25，切换到 independence 假设也不改变任何结论。论文的表述应更精确：不是说 α̂ 接近零，而是说「correlation structure choice does not affect estimates due to sandwich robustness」。

---

### Missing References

R2 建议的三篇引用中：
- **Polo et al. (2024) TinyBenchmarks (IRT in NLG evaluation)**：同意引用。IRT 提供了 Likert 量表在 NLG 评估中的替代 psychometric 框架，与论文的 measurement-mode 讨论直接相关。
- **Likert scale anchoring effects**：与 tie rate 和 Blindspot 机制相关，应引用。
- **Munos et al. (2023) Nash Learning from Human Feedback**：相关性较弱——NLHF 是关于偏好学习算法，而非测量方法论。可在 Related Work 提及但非必须。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-23T14:35:42.757008+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-23T14:35:43.058548+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T14:21:11.832705+00:00\", \"completed_at\": \"2026-05-23T14:25:50.363185+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点，第一个 display item（Figure 1 pipeline overview）在 page 2。ACL 双栏格式下常见，但若能在 page 1 底部加 teaser figure 可增强第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 较简短（\\\"CSD pipeline overview. Numbers indicate sample attrition at each stage.\\\"），建议补充每阶段核心操作的一句话描述以增强 self-containedness\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Related Work 纯文本页，无 display item。因 page 2 和 page 4 各有 figure，节奏尚可\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 DAG 图中部分注释文字（dashed arrow 说明）字号偏小，建议确认打印后仍可读\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"左栏连续放置 Figure 5 + Figure 6 两张图，视觉密度较高。两图内容相关（GEE 分解 + BT 概率），整体可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 5/6 的 axis label 和 legend 字号接近正文 70% 下限，建议验证 camera-ready 打印可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"附录末页内容占 ~70%，底部约 30% 空白。附录末页可接受，非主要问题\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-23T14:35:43.058979+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-23T14:35:43.109483+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-23T14:36:28.236017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-23T14:36:28.337020+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 17
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。"
44	      - round: 13
45	        reviewers: [1, 2]
46	        note: "R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。"
47	      - round: 14
48	        reviewers: [1, 2]
49	        note: "R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。"
50	      - round: 15
51	        reviewers: [1, 2]
52	        note: "R15 fresh review: 两位再次独立提出。"
53	      - round: 16
54	        reviewers: [1, 2]
55	        note: "R16: S4 称 GEE decomposition 是'真正的方法论
…[truncated 1946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-23T14:36:41.034864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-23T14:36:41.035397+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce divergent sensitivity across surface-level style axes when applied to LLM judges.
3	We define this divergence---the \emph{Likert Blindspot}---as significant pairwise sensitivity absent from Likert, admitting non-exclusive explanations including measurement attenuation, format amplification, and construct divergence.
4	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic quantifying this divergence via NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
5	Across five judges from four providers and two primary axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\%---replicated across three benchmarks and confirmed by seven statistical methods.
6	GEE decomposition reveals distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects joint style--quality contributions.
7	One judge (Claude Sonnet~4) exhibits benchmark-dependent sensitivity, illustrating bias as a judge$\times$benchmark interaction; non-tie concordance (76.6\%, $p < .001$) is more consistent with attenuation than construct divergence.
8	Likert-only audits may thus fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1504 · 2026-05-23T14:36:46.008184+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}~]//g; s/---/ /g; s/--/ /g; s/  */ /g' | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}~]//g; s/---/ /g; s/--/ /g; s/  */ /g' | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---


### Tool result

_source line 1505 · 2026-05-23T14:36:46.160739+00:00_

162

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-23T14:40:52.483428+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: S4 称 GEE decomposition 是'真正的方法论贡献'——首次获正面评价。但仍认为 GEE 被 undersold。Intro 3 个 LLM-specific distinctions 被认可。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 fresh: R2 列为 Must-Fix N1 (critical)——三个 LLM-specific distinctions 被夸大。R1 交叉部分同意。共识：重新定位为 'empirical characterization + novel diagnostic layer'。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18 fresh: R2 Must-Fix N1——(c) binary split 被论文自己承认与经典理论一致，不构成 LLM-specific distinction。R1 交叉 AGREE 但指出 GEE per-axis decomposition 是 genuine contribution。共识：定位为 'systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool'，降低 'new phenomenon' 暗示。\"\n    action_items:\n      - round: 17\n        action: \"Intro 三个 LLM-specific distinctions 需重新措辞\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 18\n        action: \"删除 (c) binary split 作为独立 LLM-specific distinction（或降级为'与经典理论一致的验证'）；Title/Abstract 降低 'new phenomenon' 暗示，改为 'systematic demonstration reveals per-axis structure not predicted by classical theory'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 13-16 issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"Table 1 已拆为 LLMBar primary only，cross-benchmark 移至 Appendix T。脚注包含方向不对称信息。\"\n    resolution_round: 16\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及。Related Work RATE 段落已改善。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Related Work 中 RATE 定位被两位 Reviewer 评为'准确且诚实'(R1-S4)。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被显式提及。R2 在 N1 中讨论 RATE 差异化但未将其列为独立问题。可能已充分改善。\"\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 M1: Title 仍隐含 Likert 有缺陷。采用 Option C（保持 title + 充实 construct divergence）。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N3 再次提出。R1 交叉 REBUT——'Blindspot' 有操作性定义。分歧：R2 要改标题，R1 要保留+更早 qualify。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R2 Should-Fix W1 再次提出——Title 预设 attenuation 解释，与三种非排他解释矛盾。R1 交叉 AGREE 但认为严重程度中等（证据权重支持 attenuation）。共识：保留 Title 但在 Abstract 更早 qualify。\"\n    action_items:\n      - round: 17\n        action: \"保留 Blindspot title，但在 Abstract 更早引入操作性定义和三种解释的 qualification\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 18\n        action: \"Abstract 中加入明确 hedge，如 'an operational descriptor without committing to a specific causal mechanism'；确保读者不从标题获得单一方向印象\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF2: 三条 convergent evidence 每条单独仍不足。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N3 系统解构四条证据线。共识：降级为 'lower-sensitivity judge'。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W3——TOST Δ=12pp 才显著(p=.035)，Δ=10pp 不显著，BF₀<3 inconclusive，等价边界 data-driven。R2 交叉 AGREE 但指出 Claude 的价值更在于 discriminative validity（LLMBar n.s. vs AEval significant）而非 equivalence testing。共识：弱化 'negative control' claim，强调 'discriminative validity' 角色。\"\n    action_items:\n      - round: 18\n        action: \"将 Claude 定位为 'weak-bias case' 或 'discriminative validity evidence' 而非 'negative control'；提供等价边界的独立（非 data-driven）理由\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽，n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF1: 降级为 Should-Fix。Projection 论证足够。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 升级为 Must-Fix N1——Table 2 其他 11 个 n=88 cell 以 face value 呈现。共识：n=88 OR 应标注为上界估计。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Must-Fix N1——49% shrinkage 已证实，GPT-4o formality OR 2.58 经 shrinkage 后约 1.32 可能失去显著性。verbosity 外推(4-6.5)未经实证验证。R2 AGREE 但区分影响：Blindspot 存在性(BT 非参数)不受影响，GEE 定量结论受影响。共识：至少对一个 verbosity cell 做 n=355 复制，或将 verbosity GEE 结论标注为 projected。\"\n    action_items:\n      - round: 18\n        action: \"(1) 至少一个 verbosity cell 做 n=355 复制验证 shrinkage 预测；(2) 正文更突出地标注 n=88 OR 为 upper-bound estimates；(3) GPT-4o formality 讨论 shrinkage 后可能失去显著性的风险\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF3: 升级为 Must-Fix。'systematically' 已替换为 'consistently' 在 5 处。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N2——'consistently divergent' 仍过强。共识：Abstract 需更精确措辞。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R2 Should-Fix W4——'consistent pattern' 与 ~30% exception rate 有张力（Claude, Gemini formality, 6/24 cross-benchmark）。R1 REBUT——Claude 是负对照不是例外，Gemini 是 spectrum，实际一致性 8/8 bias-positive cells。分歧：R2 认为应改 'predominant pattern'，R1 认为 'consistent' 在 primary cells 范围内合理。\"\n    action_items:\n      - round: 18\n        action: \"在 §6 Conclusion 量化复制率（e.g. '8/11 primary+confirmatory cells, 6/24 cross-benchmark cells'），让读者自行判断 consistency\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: \"100-pair annotation (50 formality + 50 verbosity, 70 NLI-pass + 30 NLI-fail): gate pass precision=98.6% (69/70, both annotators concordant), AC₁=0.96. Only 2/70 NLI-pass flagged by either annotator. Gate conservative: 93-100% of NLI-fail also preserve meaning (false rejection dominant). κ paradox (−0.015) due to >96% positive prevalence (Feinstein & Cicchetti 1990).\"\n    resolution_round: 17\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"三 judge (GPT-4o/Qwen3/Llama-70B) 100-point Likert 全部 NS (p>0.15)，Appendix L 已更新为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF4: FK 作为 GEE 协变量分析完成。Style OR 下降 20-51%，GPT-4o 变 NS。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N2——GPT-4o formality Style OR 在 FK control 下失去显著性。共识：需在正文讨论 FK 因果角色。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W4——Sobel 建立统计中介非因果中介，替代因果结构(FK 为 collider)统计上不可区分。R2 交叉 AGREE 但认为 S→FK 方向 a priori reasonable。共识：将 mediator claim 降级为 'plausible under assumed causal model' 而非 definitive。\"\n    action_items:\n      - round: 18\n        action: \"呈现两种因果解释（mediator vs confounder）并讨论各自对 OR 估计的含义，而非仅断言 mediator\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF3: Limitations 需讨论 22% 作为 lower bound。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Should-Fix W1 再次提出——缺 rule-based rewriter。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W2 + R2 Should-Fix W2 双方再次独立提出。R1 补充：n=355 复制恰好选用有 overlap 的 Qwen3-32B，不是最 clean 的验证。overlap inflation 是 axis-dependent（verbosity 22% > formality 2.1pp）。共识：更突出标注 overlap caveat，建议至少一个 scaled replication 用非 overlap 配置。\"\n    action_items:\n      - round: 18\n        action: \"(1) Table 1 脚注标注 Qwen3-32B 的 evaluator-producer overlap caveat；(2) 建议 n=355 复制使用非 overlap 配置（Qwen3 rewriter → GPT-4o judge 或反向）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 1 已为 LLMBar-only（4 judges × 2-3 axes），cross-benchmark 在 Appendix Table T。\"\n    resolution_round: 16\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Appendix V 已添加完整 rewriting prompts\"\n    resolution_round: 16\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"全文术语统一：'style sensitivity' 为默认。\"\n    resolution_round: 16\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 2 caption 已展开\"\n    resolution_round: 16\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未提及，camera-ready 前检查。\"\n      - round: 17\n        reviewers: []\n        note: \"R17: R2 建议确认 RATE 和 Comparative Trap 引用是否为最新版本。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被显式提及。camera-ready 前仍需检查。\"\n\n  # ============================================================\n  # Round 16 issues\n  # ============================================================\n\n  - id: \"R16-W1\"\n    summary: \"Construct divergence 讨论不充分——与 Abstract 三机制并列承诺不匹配\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W4 (Should-Fix): construct divergence 需操作性定义和可检验预测。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: Section 5.1 已有 construct divergence 展开。质量可接受但 Title 与正文仍有张力。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被独立提出，但作为 R15-N1 (Title framing) 的子问题被间接讨论。\"\n\n  - id: \"R16-W2\"\n    summary: \"Cross-benchmark 'severity spectrum' 解释为 post-hoc rationalization\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W5: 标记为 post-hoc/exploratory。已添加 'Post hoc,' 前缀。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。'Post hoc' 前缀已存在。\"\n      - round: 18\n        reviewers: [1]\n        note: \"R18: R1-N2 指出 3 个 ‡ exceptions 的 post-hoc 'severity spectrum' 解释未被前瞻性验证。\"\n\n  - id: \"R16-W3\"\n    summary: \"BT 模型 unidimensionality 假设与论文核心论点存在张力\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W7 (Minor): §3.3 已添加 BT unidimensionality + GEE 互补说明。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Section 3.3 末句已存在。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。\"\n\n  - id: \"R16-D1\"\n    summary: \"Appendix L 100pt Likert 数据归属错误（GPT-4o 误标为 Qwen3-32B）\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix L 修正为 GPT-4o 归属，扩展为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R16-D2\"\n    summary: \"Claude LLMBar Likert Table 1 vs Appendix U 数值不一致\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix U 统一为 pole-aligned convention。\"\n    resolution_round: 16\n\n  - id: \"R16-D3\"\n    summary: \"FK analysis artifact 数据源错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"FK 脚本修复为 nli_cf >= 0.90 过滤。\"\n    resolution_round: 16\n\n  - id: \"R16-Q3\"\n    summary: \"Direction-aware gating 额外放入的 21 pairs 是否有系统差异\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Permutation test p=.663, BT% 差 4.7pp (NS)。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: Appendix F 实证验证充分(permutation p=.663, 5 judges Fisher p>.66)。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。\"\n\n  # ============================================================\n  # Round 17 issues\n  # ============================================================\n\n  - id: \"R17-W1\"\n    summary: \"Cross-benchmark replication 选择性——24 cells 仅填 6 个(25%)，选择最强 cells，可能向上偏倚\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W2 + R2 交叉 AGREE。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Must-Fix N2——6/24 cells 选择标准为 'targeting the strongest effects'，构成确认偏差。R2 AGREE concern 但建议降级 Should-Fix（论文主 claims 不依赖 cross-benchmark，且已标注为 exploratory）。共识：Contribution 2 措辞需弱化，明确选择标准和 exploratory 性质。\"\n    action_items:\n      - round: 18\n        action: \"(1) Contribution 2 从 'the first at this scale' 弱化为 'with selective cross-benchmark evidence'；(2) 报告选择标准和未测试 cells 的影响；(3) 考虑补充至少一个中等效应配置\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W2\"\n    summary: \"GEE 模型仅含 2 个 predictors (Style, Originality)，omitted variable bias 未讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W1，R1 交叉 AGREE。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W5 要求报告 E-value 或 Rosenbaum bounds。R2 部分 REBUT——GEE 定位为 descriptive decomposition 而非因果推断，omitted variable 批评前提不完全成立。但同意报告 E-value 是低成本改进。分歧：R1 认为 should-fix，R2 认为 nice-to-have。\"\n    action_items:\n      - round: 18\n        action: \"报告 E-value 量化未观测混淆需要多大才能推翻结论（对 verbosity Style OR 8-13 的 E-value 会非常高，加强论证）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W3\"\n    summary: \"与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分——六项 controls 不能排除 amplification，未量化 amplification factor\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W5，R1 交叉 AGREE。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被独立提出，但 R2-W1 (Title framing) 间接涉及——amplification 是三种解释之一。\"\n\n  - id: \"R17-M1\"\n    summary: \"Table 1 'n=88 except where noted' 与 verbosity 实际 n=86 不一致\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M1 提出，R2 交叉 AGREE。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。Table 1 caption 已标注 '86 verbosity, except where noted'。\"\n\n  - id: \"R17-M2\"\n    summary: \"BT choix library 'default regularization' 未说明具体形式和强度\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M5 + R1-Q5 提出，R2 交叉 AGREE。\"\n      - round: 18\n        reviewers: [1]\n        note: \"R18: R1 minor——α=10⁻⁶ 实质上为零正则化，但在少数高度不一致 pair 上可能导致极端参数估计。建议报告 α 的敏感性。\"\n\n  - id: \"R17-M3\"\n    summary: \"Section 3.1 因果语言——'constitutes a binary intervention' 措辞过强\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W4。R2 交叉 REBUT 但同意措辞可改为 'approximates'。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被显式提及。论文 §3.5 已有 'interventional rather than formal causal evidence' disclaimer。\"\n\n  - id: \"R17-M4\"\n    summary: \"Figure 2 (DAG) orange dashed S→Q path 在灰度打印下不可辨\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M3 + R2-M2 双方独立指出。建议使用不同 line pattern。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。视觉审查 Agent 标注 Figure 2 注释文字字号偏小但未提及灰度可辨性。\"\n\n  # ============================================================\n  # Round 18 新发现\n  # ============================================================\n\n  - id: \"R18-W1\"\n    summary: \"Likert Blindspot 缺少正式的 measurement-mode divergence 检验——分别报告 BT 显著和 Likert 不显著，但未检验二者是否 significantly different\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W1 提出——absence of evidence ≠ evidence of absence。R2 交叉 AGREE（承认自己遗漏了此问题）。论文用 n=355 TOST 和 bootstrap attenuation 间接回应，但缺少正式的 measurement-mode interaction test。共识：应补充 bootstrap the difference in effect sizes between BT and Likert。\"\n    action_items:\n      - round: 18\n        action: \"添加 measurement-mode interaction test 或 bootstrap effect-size difference test，正式检验 BT 和 Likert 的 effect size 是否 significantly different\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R18-M1\"\n    summary: \"论文使用 1-10 整数量表但称 'Likert'——严格来说应为 interval rating scale\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [1]\n        note: \"R1 minor——Likert (1932) 原始定义为 5-point attitude scale。1-10 整数量表严格来说是 interval rating scale。建议添加一句澄清。\"\n\n  - id: \"R18-M2\"\n    summary: \"缺少 Likert (1932) 原始引用\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R1 missing ref + R2 交叉 AGREE。论文大量使用 'Likert' 一词但未引用原始文献。\"\n\n  - id: \"R18-M3\"\n    summary: \"Table 1 'Cat.' 列标注（†, †_e, †_c, ---）难以解析\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R1 minor + R2-M4 独立指出。建议改为更直观的文字标签。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16: S4 称 GEE decomposition 是'真正的方法论贡献'——首次获正面评价。但仍认为 GEE 被 undersold。Intro 3 个 LLM-specific distinctions 被认可。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 fresh: R2 列为 Must-Fix N1 (critical)——三个 LLM-specific distinctions 被夸大。R1 交叉部分同意。共识：重新定位为 'empirical characterization + novel diagnostic layer'。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18 fresh: R2 Must-Fix N1——(c) binary split 被论文自己承认与经典理论一致，不构成 LLM-specific distinction。R1 交叉 AGREE 但指出 GEE per-axis decomposition 是 genuine contribution。共识：定位为 'systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool'，降低 'new phenomenon' 暗示。\"\n    action_items:\n      - round: 17\n        action: \"Intro 三个 LLM-specific distinctions 需重新措辞\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 18\n        action: \"删除 (c) binary split 作为独立 LLM-specific distinction（或降级为'与经典理论一致的验证'）；Title/Abstract 降低 'new phenomenon' 暗示，改为 'systematic demonstration reveals per-axis structure not predicted by classical theory'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 13-16 issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"Table 1 已拆为 LLMBar primary only，cross-benchmark 移至 Appendix T。脚注包含方向不对称信息。\"\n    resolution_round: 16\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未被显式提及。Related Work RATE 段落已改善。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Related Work 中 RATE 定位被两位 Reviewer 评为'准确且诚实'(R1-S4)。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被显式提及。R2 在 N1 中讨论 RATE 差异化但未将其列为独立问题。可能已充分改善。\"\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 M1: Title 仍隐含 Likert 有缺陷。采用 Option C（保持 title + 充实 construct divergence）。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N3 再次提出。R1 交叉 REBUT——'Blindspot' 有操作性定义。分歧：R2 要改标题，R1 要保留+更早 qualify。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R2 Should-Fix W1 再次提出——Title 预设 attenuation 解释，与三种非排他解释矛盾。R1 交叉 AGREE 但认为严重程度中等（证据权重支持 attenuation）。共识：保留 Title 但在 Abstract 更早 qualify。\"\n    action_items:\n      - round: 17\n        action: \"保留 Blindspot title，但在 Abstract 更早引入操作性定义和三种解释的 qualification\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 18\n        action: \"Abstract 中加入明确 hedge，如 'an operational descriptor without committing to a specific causal mechanism'；确保读者不从标题获得单一方向印象\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%）\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF2: 三条 convergent evidence 每条单独仍不足。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N3 系统解构四条证据线。共识：降级为 'lower-sensitivity judge'。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W3——TOST Δ=12pp 才显著(p=.035)，Δ=10pp 不显著，BF₀<3 inconclusive，等价边界 data-driven。R2 交叉 AGREE 但指出 Claude 的价值更在于 discriminative validity（LLMBar n.s. vs AEval significant）而非 equivalence testing。共识：弱化 'negative control' claim，强调 'discriminative validity' 角色。\"\n    action_items:\n      - round: 18\n        action: \"将 Claude 定位为 'weak-bias case' 或 'discriminative validity evidence' 而非 'negative control'；提供等价边界的独立（非 data-driven）理由\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽，n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF1: 降级为 Should-Fix。Projection 论证足够。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 升级为 Must-Fix N1——Table 2 其他 11 个 n=88 cell 以 face value 呈现。共识：n=88 OR 应标注为上界估计。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Must-Fix N1——49% shrinkage 已证实，GPT-4o formality OR 2.58 经 shrinkage 后约 1.32 可能失去显著性。verbosity 外推(4-6.5)未经实证验证。R2 AGREE 但区分影响：Blindspot 存在性(BT 非参数)不受影响，GEE 定量结论受影响。共识：至少对一个 verbosity cell 做 n=355 复制，或将 verbosity GEE 结论标注为 projected。\"\n    action_items:\n      - round: 18\n        action: \"(1) 至少一个 verbosity cell 做 n=355 复制验证 shrinkage 预测；(2) 正文更突出地标注 n=88 OR 为 upper-bound estimates；(3) GPT-4o formality 讨论 shrinkage 后可能失去显著性的风险\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 MF3: 升级为 Must-Fix。'systematically' 已替换为 'consistently' 在 5 处。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R2 Must-Fix N2——'consistently divergent' 仍过强。共识：Abstract 需更精确措辞。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R2 Should-Fix W4——'consistent pattern' 与 ~30% exception rate 有张力（Claude, Gemini formality, 6/24 cross-benchmark）。R1 REBUT——Claude 是负对照不是例外，Gemini 是 spectrum，实际一致性 8/8 bias-positive cells。分歧：R2 认为应改 'predominant pattern'，R1 认为 'consistent' 在 primary cells 范围内合理。\"\n    action_items:\n      - round: 18\n        action: \"在 §6 Conclusion 量化复制率（e.g. '8/11 primary+confirmatory cells, 6/24 cross-benchmark cells'），让读者自行判断 consistency\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 17\n    resolution: \"100-pair annotation (50 formality + 50 verbosity, 70 NLI-pass + 30 NLI-fail): gate pass precision=98.6% (69/70, both annotators concordant), AC₁=0.96. Only 2/70 NLI-pass flagged by either annotator. Gate conservative: 93-100% of NLI-fail also preserve meaning (false rejection dominant). κ paradox (−0.015) due to >96% positive prevalence (Feinstein & Cicchetti 1990).\"\n    resolution_round: 17\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"三 judge (GPT-4o/Qwen3/Llama-70B) 100-point Likert 全部 NS (p>0.15)，Appendix L 已更新为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF4: FK 作为 GEE 协变量分析完成。Style OR 下降 20-51%，GPT-4o 变 NS。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Must-Fix N2——GPT-4o formality Style OR 在 FK control 下失去显著性。共识：需在正文讨论 FK 因果角色。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W4——Sobel 建立统计中介非因果中介，替代因果结构(FK 为 collider)统计上不可区分。R2 交叉 AGREE 但认为 S→FK 方向 a priori reasonable。共识：将 mediator claim 降级为 'plausible under assumed causal model' 而非 definitive。\"\n    action_items:\n      - round: 18\n        action: \"呈现两种因果解释（mediator vs confounder）并讨论各自对 OR 估计的含义，而非仅断言 mediator\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R16 SF3: Limitations 需讨论 22% 作为 lower bound。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: R1 Should-Fix W1 再次提出——缺 rule-based rewriter。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W2 + R2 Should-Fix W2 双方再次独立提出。R1 补充：n=355 复制恰好选用有 overlap 的 Qwen3-32B，不是最 clean 的验证。overlap inflation 是 axis-dependent（verbosity 22% > formality 2.1pp）。共识：更突出标注 overlap caveat，建议至少一个 scaled replication 用非 overlap 配置。\"\n    action_items:\n      - round: 18\n        action: \"(1) Table 1 脚注标注 Qwen3-32B 的 evaluator-producer overlap caveat；(2) 建议 n=355 复制使用非 overlap 配置（Qwen3 rewriter → GPT-4o judge 或反向）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 1 已为 LLMBar-only（4 judges × 2-3 axes），cross-benchmark 在 Appendix Table T。\"\n    resolution_round: 16\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Appendix V 已添加完整 rewriting prompts\"\n    resolution_round: 16\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"全文术语统一：'style sensitivity' 为默认。\"\n    resolution_round: 16\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"Table 2 caption 已展开\"\n    resolution_round: 16\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未提及，camera-ready 前检查。\"\n      - round: 17\n        reviewers: []\n        note: \"R17: R2 建议确认 RATE 和 Comparative Trap 引用是否为最新版本。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被显式提及。camera-ready 前仍需检查。\"\n\n  # ============================================================\n  # Round 16 issues\n  # ============================================================\n\n  - id: \"R16-W1\"\n    summary: \"Construct divergence 讨论不充分——与 Abstract 三机制并列承诺不匹配\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W4 (Should-Fix): construct divergence 需操作性定义和可检验预测。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: Section 5.1 已有 construct divergence 展开。质量可接受但 Title 与正文仍有张力。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被独立提出，但作为 R15-N1 (Title framing) 的子问题被间接讨论。\"\n\n  - id: \"R16-W2\"\n    summary: \"Cross-benchmark 'severity spectrum' 解释为 post-hoc rationalization\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [2]\n        note: \"R2-W5: 标记为 post-hoc/exploratory。已添加 'Post hoc,' 前缀。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。'Post hoc' 前缀已存在。\"\n      - round: 18\n        reviewers: [1]\n        note: \"R18: R1-N2 指出 3 个 ‡ exceptions 的 post-hoc 'severity spectrum' 解释未被前瞻性验证。\"\n\n  - id: \"R16-W3\"\n    summary: \"BT 模型 unidimensionality 假设与论文核心论点存在张力\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W7 (Minor): §3.3 已添加 BT unidimensionality + GEE 互补说明。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未被显式提及。Section 3.3 末句已存在。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。\"\n\n  - id: \"R16-D1\"\n    summary: \"Appendix L 100pt Likert 数据归属错误（GPT-4o 误标为 Qwen3-32B）\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix L 修正为 GPT-4o 归属，扩展为三 judge 对比表。\"\n    resolution_round: 16\n\n  - id: \"R16-D2\"\n    summary: \"Claude LLMBar Likert Table 1 vs Appendix U 数值不一致\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"Appendix U 统一为 pole-aligned convention。\"\n    resolution_round: 16\n\n  - id: \"R16-D3\"\n    summary: \"FK analysis artifact 数据源错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"FK 脚本修复为 nli_cf >= 0.90 过滤。\"\n    resolution_round: 16\n\n  - id: \"R16-Q3\"\n    summary: \"Direction-aware gating 额外放入的 21 pairs 是否有系统差异\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Permutation test p=.663, BT% 差 4.7pp (NS)。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17: Appendix F 实证验证充分(permutation p=.663, 5 judges Fisher p>.66)。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。\"\n\n  # ============================================================\n  # Round 17 issues\n  # ============================================================\n\n  - id: \"R17-W1\"\n    summary: \"Cross-benchmark replication 选择性——24 cells 仅填 6 个(25%)，选择最强 cells，可能向上偏倚\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W2 + R2 交叉 AGREE。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Must-Fix N2——6/24 cells 选择标准为 'targeting the strongest effects'，构成确认偏差。R2 AGREE concern 但建议降级 Should-Fix（论文主 claims 不依赖 cross-benchmark，且已标注为 exploratory）。共识：Contribution 2 措辞需弱化，明确选择标准和 exploratory 性质。\"\n    action_items:\n      - round: 18\n        action: \"(1) Contribution 2 从 'the first at this scale' 弱化为 'with selective cross-benchmark evidence'；(2) 报告选择标准和未测试 cells 的影响；(3) 考虑补充至少一个中等效应配置\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W2\"\n    summary: \"GEE 模型仅含 2 个 predictors (Style, Originality)，omitted variable bias 未讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W1，R1 交叉 AGREE。\"\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R18: R1 Should-Fix W5 要求报告 E-value 或 Rosenbaum bounds。R2 部分 REBUT——GEE 定位为 descriptive decomposition 而非因果推断，omitted variable 批评前提不完全成立。但同意报告 E-value 是低成本改进。分歧：R1 认为 should-fix，R2 认为 nice-to-have。\"\n    action_items:\n      - round: 18\n        action: \"报告 E-value 量化未观测混淆需要多大才能推翻结论（对 verbosity Style OR 8-13 的 E-value 会非常高，加强论证）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R17-W3\"\n    summary: \"与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分——六项 controls 不能排除 amplification，未量化 amplification factor\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 Should-Fix W5，R1 交叉 AGREE。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被独立提出，但 R2-W1 (Title framing) 间接涉及——amplification 是三种解释之一。\"\n\n  - id: \"R17-M1\"\n    summary: \"Table 1 'n=88 except where noted' 与 verbosity 实际 n=86 不一致\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M1 提出，R2 交叉 AGREE。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。Table 1 caption 已标注 '86 verbosity, except where noted'。\"\n\n  - id: \"R17-M2\"\n    summary: \"BT choix library 'default regularization' 未说明具体形式和强度\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M5 + R1-Q5 提出，R2 交叉 AGREE。\"\n      - round: 18\n        reviewers: [1]\n        note: \"R18: R1 minor——α=10⁻⁶ 实质上为零正则化，但在少数高度不一致 pair 上可能导致极端参数估计。建议报告 α 的敏感性。\"\n\n  - id: \"R17-M3\"\n    summary: \"Section 3.1 因果语言——'constitutes a binary intervention' 措辞过强\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W4。R2 交叉 REBUT 但同意措辞可改为 'approximates'。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被显式提及。论文 §3.5 已有 'interventional rather than formal causal evidence' disclaimer。\"\n\n  - id: \"R17-M4\"\n    summary: \"Figure 2 (DAG) orange dashed S→Q path 在灰度打印下不可辨\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1-M3 + R2-M2 双方独立指出。建议使用不同 line pattern。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未被提及。视觉审查 Agent 标注 Figure 2 注释文字字号偏小但未提及灰度可辨性。\"\n\n  # ============================================================\n  # Round 18 新发现\n  # ============================================================\n\n  - id: \"R18-W1\"\n    summary: \"Likert Blindspot 缺少正式的 measurement-mode divergence 检验——分别报告 BT 显著和 Likert 不显著，但未检验二者是否 significantly different\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix W1 提出——absence of evidence ≠ evidence of absence。R2 交叉 AGREE（承认自己遗漏了此问题）。论文用 n=355 TOST 和 bootstrap attenuation 间接回应，但缺少正式的 measurement-mode interaction test。共识：应补充 bootstrap the difference in effect sizes between BT and Likert。\"\n    action_items:\n      - round: 18\n        action: \"添加 measurement-mode interaction test 或 bootstrap effect-size difference test，正式检验 BT 和 Likert 的 effect size 是否 significantly different\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R18-M1\"\n    summary: \"论文使用 1-10 整数量表但称 'Likert'——严格来说应为 interval rating scale\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [1]\n        note: \"R1 minor——Likert (1932) 原始定义为 5-point attitude scale。1-10 整数量表严格来说是 interval rating scale。建议添加一句澄清。\"\n\n  - id: \"R18-M2\"\n    summary: \"缺少 Likert (1932) 原始引用\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R1 missing ref + R2 交叉 AGREE。论文大量使用 'Likert' 一词但未引用原始文献。\"\n\n  - id: \"R18-M3\"\n    summary: \"Table 1 'Cat.' 列标注（†, †_e, †_c, ---）难以解析\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [1, 2]\n        note: \"R1 minor + R2-M4 独立指出。建议改为更直观的文字标签。\""
  }
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-23T14:40:52.584656+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 26200}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-23T14:43:49.437464+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n\n**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）\n**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识\n\n---\n\n## Summary\n\n本文定义了 \"Likert Blindspot\"——LLM judge 的 pairwise comparison 能检测到显著风格敏感性而 Likert scoring 检测不到的现象。提出 Controlled Style Decomposition (CSD) 框架，整合 NLI-gated 内容控制、per-axis 风格分解和 position-controlled pairwise comparison。在 5 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash, Claude Sonnet 4）、2 个 primary 风格轴（formality, verbosity）+ 1 个 exploratory（register）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）上实验，结果一致显示 pairwise BT 显著（p < 0.001）而 Likert 不显著（p > 0.17），7 种统计方法交叉确认。GEE 条件分解揭示 per-axis confound structure：verbosity 是 style-dominated（Style OR 8–13, Originality OR < 1），formality 是 quality-confounded（两个 predictor 都显著）。论文坦诚提出三种非排他解释（attenuation, amplification, construct divergence）。\n\n---\n\n## Strengths\n\n**S1. 卓越的实验严谨性。** 六层控制设计（NLI gate, position swap, double-rewrite, debiased prompting, cross-rewriter validation, GEE confound decomposition）在 LLM judge bias 文献中属于最严格的方法控制之一。七种统计方法全部一致确认 Blindspot（Table 14, Appendix M），bootstrap CI、TOST、Bayesian equivalence testing 的组合使用展现了统计成熟度。[R1-S3, R1-S5, R2-S1, 双方 AGREE]\n\n**S2. Per-axis confound structure 是 genuinely novel 的发现。** GEE decomposition 揭示 verbosity 是 style-dominated 而 formality 是 quality-confounded，这种 per-axis 差异不是经典心理测量学能预测的，对 LLM judge 审计策略有直接实践意义——不同风格轴需要不同的审计方法。[R2-S2, R1-S2, 双方 AGREE]\n\n**S3. 诚实的 claim hedging。** 论文主动提出三种非排他解释（§5.1），明确承认 residual confounding 未完全消除，用 \"complements\" 而非 \"surpasses\" 描述与经典框架的关系。DAG 标注为 \"assumed data-generating process, not a claim of perfect identification\"。在 LLM 领域论文中属于少见的审慎态度。[R2-S3, R1-S4, 双方 AGREE]\n\n**S4. 方法论体系化与实践相关性。** CSD 将 NLI gating、style-controlled rewriting、GEE decomposition 组合成完整分析框架，各环节有明确方法论依据。结论直接指向 LLM alignment pipeline 的审计盲区——Likert-based reward model 评估可能漏检 pairwise 能发现的风格偏差。[R2-S4, R2-S5, R1-S1, R1-S2]\n\n**S5. Robustness 检查远超平均水准。** 11 个 NLI 阈值、一致性筛选对比、独立 rewriter、人工标注（100 pairs, AC₁=0.96）、6 个 amplification controls、cross-benchmark 复制、n=355 scaled replication——超过同类论文的平均水准。Bootstrap attenuation analysis 比标准 post-hoc power 更合理。[R1-S3, R1-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] GEE 小样本膨胀严重，仅 1/9 配置有 n=355 复制** [R1-N1, R2-N2, 双方 AGREE]\n- Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，shrinkage 达 49%（Table 2）。但 9 个 judge×axis 配置中仅 1 个做了大样本复制。\n- GPT-4o formality Style OR 2.58 [1.41, 4.73] 经 49% shrinkage 后约 1.32，CI 可能跨 1.0（失去显著性）。Gemini formality Style OR 1.64 [0.91, 2.98] 在 n=88 时已不显著，shrinkage 后几乎必然为零。\n- Verbosity 的外推（\"projected 4–6.5, still ≫ Orig OR < 1\"，§5.2）逻辑成立但未经实证验证。\n- **R2 重要补充**：此问题主要威胁 GEE per-axis 定量结论，Blindspot 存在性（BT 非参数显著性）不受影响。\n- **建议**：至少对一个 verbosity cell 做 n=355 复制验证 shrinkage 预测；正文更突出标注 n=88 OR 为 upper-bound estimates；讨论 GPT-4o formality 的 shrinkage 风险。\n\n**MF2. [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer** [R2-N1, R1 AGREE with nuance]\n- 核心经验发现（pairwise 比 Likert 更敏感）本质上是 Thurstone (1927) Law of Comparative Judgment 的验证。论文在 §1 引用了 Thurstone 并说 \"quantitatively consistent\"，但 Title \"The Likert Blindspot\" 和 Abstract 仍暗示新发现的现象。\n- Introduction 的三个 \"LLM-specific distinctions\" 中，(c) \"near-complete binary split\" 被论文自己承认与经典理论一致（\"consistent with classical predictions when accounting for effect-size-dependent power\"），不构成独立贡献。\n- **R1 补充**：GEE per-axis decomposition（Table 2 的 style-dominated vs quality-confounded 结构差异）是 genuinely novel 的实证发现，不是 Thurstone 能预测的。CSD pipeline 作为完整诊断工具也有组合创新。\n- **共识定位**：contribution 应定位为 \"systematic empirical demonstration in LLM judges + per-axis structure discovery + practical diagnostic tool\"，而非 \"new phenomenon\"。删除 (c) binary split 作为独立 distinction 或降级为\"与经典理论一致的验证\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] Cross-benchmark 复制为选择性报告（6/24 cells）** [R1-N2, R2 AGREE but suggests downgrade]\n- 论文在 AlpacaEval 和 MT-Bench 上仅测试 24 个可能 cells 中的 6 个，选择标准为 \"targeting the strongest effects\"（§5.3）。3 个例外（‡ 行）被 post-hoc 解释为 effect-size dependence，未被前瞻性验证。\n- **R2 缓解**：论文将 cross-benchmark 定位为 exploratory（§4.1），主要 claims 建立在 LLMBar 上。但 §1 Contribution 2 的 \"the first at this scale\" 暗示了更全面的覆盖。\n- **建议**：Contribution 2 弱化为 \"with selective cross-benchmark evidence\"；报告选择标准；考虑补充一个中等效应配置。\n\n**SF2. [warning] Likert Blindspot 缺少正式的 divergence 检验** [R1-W1, R2 AGREE]\n- 论文分别展示 \"BT 显著\" 和 \"Likert 不显著\"，但从未正式检验二者的 effect size 是否 significantly different。Absence of evidence ≠ evidence of absence。\n- n=355 TOST 和 bootstrap attenuation 间接回应，但缺少正式的 measurement-mode interaction test。\n- **建议**：Bootstrap the difference in effect sizes between BT and Likert，检验差异是否显著异于零。\n\n**SF3. [warning] Qwen3-32B evaluator-producer overlap（~22% inflation）** [R1-W2, R2-W2, 双方 AGREE]\n- Qwen3-32B 同时为 rewriter 和 target judge。独立 GPT-4o rewriter 测试（Appendix E）显示 verbosity Style OR 下降 22%（13.10 → 10.17）。Overlap inflation 是 axis-dependent（verbosity 22% > formality 2.1pp）。\n- n=355 唯一复制恰好选用有 overlap 的 Qwen3-32B，不是最 clean 的验证。\n- Appendix E 确认 Blindspot 仍然存在（独立 rewriter: Style OR = 10.17, p = 0.001），overlap 影响效应量级而非现象存在性。\n- **建议**：Table 1 脚注标注 overlap caveat；至少一个 scaled replication 使用非 overlap 配置。\n\n**SF4. [warning] Claude Sonnet 4 负对照不充分** [R1-W3, R2 AGREE]\n- TOST 在 Δ=12pp 时才显著（p=.035），Δ=10pp 不显著（p=.100）。BF₀ < 3（inconclusive）。等价边界 Δ=12pp 的选择是 data-driven 而非 a priori。\n- **R2 补充**：Claude 的价值更在于 discriminative validity（LLMBar n.s. vs AEval verbosity OR = 4.76 significant），说明 CSD 不是 universal false positive machine。\n- **建议**：将 Claude 定位为 \"weak-bias case\" 或 \"discriminative validity evidence\" 而非 \"negative control\"；提供等价边界的独立理由。\n\n**SF5. [warning] FK grade 的 mediator vs. confounder 辨识不足** [R1-W4, R2 AGREE]\n- §5.3 声称 \"FK lies on the causal pathway S → FK → Y... making FK a mediator\"。但 Sobel 建立的是统计中介而非因果中介。替代因果结构（FK 为 collider 或独立 confounder）在统计上不可区分。\n- Mediator 解释下 controlled OR = 2.15，confounder 解释下为无混淆 OR——对应不同政策含义。\n- **建议**：呈现两种因果解释并讨论各自含义，而非仅断言 mediator。\n\n**SF6. [warning] Title \"Blindspot\" 暗示单一因果方向** [R2-W1, R1 AGREE moderate severity]\n- \"Blindspot\" 预设 attenuation 解释（Likert 漏检），与 §5.1 三种非排他解释矛盾。如果 amplification 是主因，应称 \"pairwise 放大镜\" 而非 \"Likert 盲点\"。\n- **R1 缓解**：实证证据权重（n=355 attenuation d→0, 76.6% concordance, 6 amplification controls）整体更支持 attenuation。Title 方向与证据一致，只是过于确定。\n- **建议**：保留 Title，但在 Abstract 更早 qualify——加入 \"an operational descriptor without committing to a specific causal mechanism\"。\n\n### Minor（不影响接收）\n\n- **M1.** \"Consistent pattern\" 与 exceptions 的张力——R2 计算 ~30% exception rate，R1 反驳（Claude 是负对照、Gemini 是 spectrum，实际 8/8 bias-positive cells 全部显示 Blindspot）。建议在 Conclusion 量化复制率。[分歧记录]\n- **M2.** Register 轴结果弱（BT .553–.635, quality-confounded）——R2 建议移至 Appendix，R1 反驳（需要 per-axis diversity 展示谱系）。[分歧记录]\n- **M3.** GEE omitted variable bias——R1 建议报告 E-value，R2 部分反驳（GEE 定位为 descriptive），但同意 E-value 是低成本改进。[轻微分歧]\n- **M4.** 论文使用 1-10 整数量表称 \"Likert\"，严格应为 interval rating scale，缺 Likert (1932) 原始引用。\n- **M5.** Table 1 \"Cat.\" 列标注（†, †_e, †_c, ---）难以解析，建议改为文字标签。\n- **M6.** Figure 5 y 轴 \"Odds Ratio\" log scale 应标注，Figure 2 DAG 注释字号偏小。\n- **M7.** BT choix regularization α=10⁻⁶ 实质为零正则化，建议报告 α 敏感性。\n- **M8.** 100-point continuous Likert（Appendix O）未报告评分分布——是否有 evidence judges 利用了 granularity？\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Scaled replication 覆盖不足**是论文最大弱点——9 个 judge×axis 配置仅 1 个有 n=355 验证，GEE 定量结论的可靠性存疑。[R1-N1 + R2-N2]\n2. **核心发现是 Thurstone domain transfer**，novelty 主要来自 GEE per-axis decomposition 和 CSD 诊断工具，需要更精确定位。[R2-N1 + R1 AGREE]\n3. **Qwen3-32B evaluator-producer overlap** 影响效应量级（~22%），但不影响现象存在性。[R1-W2 + R2-W2]\n4. **缺少正式 divergence 检验**——论文未正式检验 BT 和 Likert 的 effect size 是否 significantly different。[R1-W1 + R2 AGREE]\n5. **Claude 负对照的 TOST boundary** 是 data-driven，不够严格。[R1-W3 + R2 AGREE]\n6. **FK mediator claim** 需要降级为 \"plausible under assumed causal model\"。[R1-W4 + R2 AGREE]\n7. **实验执行和 robustness 检查**远超同类论文水准。[双方一致]\n\n## Reviewer Divergence [REBUT]\n\n1. **Cross-benchmark 严重性**：R1 列为 Must-Fix（确认偏差），R2 建议降级 Should-Fix（论文标注为 exploratory，主 claims 不依赖）。→ 报告采纳 Should-Fix（SF1）。\n2. **Register 轴位置**：R2 建议移至 Appendix（结果弱、quality-confounded），R1 反驳（需要 per-axis diversity 展示 verbosity/formality/register 谱系）。→ 记录分歧，不列为 action item。\n3. **\"Consistent\" 措辞**：R2 认为 ~30% exception rate 下过强，R1 反驳（Claude 是负对照不是例外，实际 8/8 bias-positive cells）。→ 建议量化复制率让读者自行判断。\n4. **GEE omitted variables**：R1 要求 E-value（Should-Fix），R2 认为 GEE 是 descriptive 定位（nice-to-have）。→ 建议报告但不列为 Must-Fix。\n\n---\n\n## Questions to Authors\n\n1. n=355 复制是否使用相同 NLI gating threshold (0.90)？pass rate 是否与 n=88 可比？[R1-Q1]\n2. 各 judge 的 Likert 评分分布是什么（histogram）？如果 judges 集中在某几个分数点，这直接解释 tie rate 和 Blindspot 机制。[R1-Q2]\n3. §1 \"76–92% of preferences originate from style cues\" 如何计算？引用他人 claim 时其 operationalization 是否与本文一致？[R1-Q3]\n4. 为什么 n=355 复制只选了 Qwen3-32B formality——是否有资源约束？[R1-Q4]\n5. 76.6% non-tie concordance 中 23.4% discordance——在哪个效应量阈值以下 construct divergence 可能成为主导解释？[R2-Q1]\n6. GEE exchangeable correlation α̂ ∈ [−0.25, +0.11]——−0.25 不算\"接近零\"，论文应改为 \"correlation structure choice does not affect estimates due to sandwich robustness\" 而非声称接近零。[R2-Q4, R1 交叉确认]\n\n---\n\n## Missing References\n\n1. **Likert (1932)**. A technique for the measurement of attitudes. 论文大量使用 \"Likert\" 但未引用原始文献。[R1 提出, R2 AGREE]\n2. **Polo et al. (2024)**. TinyBenchmarks — IRT 在 NLG evaluation 中的应用，与 measurement-mode 讨论直接相关。[R2 提出, R1 AGREE]\n3. **Likert scale anchoring effects** 相关文献——LLM judge 可能以不同方式解释 1-10 scale 锚点。[R2 提出]\n\n---\n\n## External Review\n\n**状态**：未配置。项目未启用外部审稿（paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（耗时 ~5 分钟）。7 个 info 级建议，无 critical 或 warning。\n\n主要发现：\n- 首页无 display item（Figure 1 在 page 2），ACL 双栏常见但可考虑 teaser figure\n- Figure 1 caption 较简短，建议补充每阶段核心操作的一句话描述\n- Figure 2 DAG 中部分注释文字字号偏小，建议确认打印后可读\n- Page 8 左栏 Figure 5 + Figure 6 连续放置，视觉密度较高但内容相关可接受\n- Figure 5/6 axis label 和 legend 字号接近正文 70% 下限，建议验证 camera-ready 打印可读性\n- 附录末页约 30% 空白，可接受\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.75 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**接收建议**：Borderline Conference — 修改后可能达到 Conference (4.0) 水平。\n\n**拉向 3.5 而非 3.0 的因素**：\n1. 实验规模和控制的 thoroughness 在同类工作中突出（5 judges × 3 benchmarks × 3 axes + n=355 replication）\n2. GEE per-axis decomposition 提供了超越 Thurstone 框架的 genuinely new insight\n3. 实践相关性强——directly actionable for RLHF/DPO pipeline audits\n4. Robustness 检查远超平均（7 种统计方法、11 NLI 阈值、人工标注 AC₁=0.96）\n\n**阻止达到 4.0 的因素**：\n1. 核心现象是经典测量理论的 domain transfer，novelty ceiling 有限（Excitement 3.0）\n2. GEE 定量结论依赖 n=88 膨胀估计，仅 1/9 配置有大样本验证\n3. Cross-benchmark 覆盖为选择性报告（6/24 cells）\n4. 缺少正式的 measurement-mode divergence 检验\n\n**修改路径**：补做至少一个 verbosity cell 的 n=355 复制 + 精确定位 novelty（降低 \"new phenomenon\" 暗示）+ 补充 formal divergence test → 预计可提升至 4.0。\n\n---\n\n## Detailed Comments\n\n### Abstract (~162 词，符合 200 词限制)\n- \"consistently\" 一词在仅 2 primary axes 基础上过强，建议改为 \"across two primary style axes, with varying effect sizes across judges\"\n- 缺少操作性定义的 early qualification——读者从 \"Likert Blindspot\" 获得单一方向印象\n\n### §1 Introduction\n- 三个 LLM-specific distinctions 中 (c) binary split 应删除或降级——论文自己承认 \"consistent with classical predictions\"\n- Contribution 2 \"the first at this scale\" 暗示全面的 cross-benchmark 覆盖，但实际仅 6/24 cells\n- \"76–92% of preferences originate from style cues\" 引用外部 claim，其 operationalization 与本文是否一致需澄清\n\n### §3 Method\n- §3.1 style classifier (Qwen3-32B) 的系统性偏差风险需讨论，虽然 NLI gate 和 direction asymmetry analysis 提供了缓解\n- §3.3 \"forced choice\" 描述准确，但应注明 1-10 量表与 Likert (1932) 原始定义的区别\n\n### §4 Experiments\n- §4.1 BT regularization α=10⁻⁶ 的敏感性应报告\n- n=355 复制应说明是否使用相同 NLI threshold\n\n### §5 Analysis\n- §5.1 需补充正式的 measurement-mode divergence 检验\n- §5.2 GEE OR 的 upper-bound nature 应在正文更突出讨论，不仅是 Table 2 caption\n- §5.2 verbosity GEE 定量结论应标注为 \"projected, pending large-sample validation\"\n- §5.3 FK mediator claim 需降级为 \"plausible under assumed causal model\"\n- §5.3 cross-benchmark 选择标准应透明化\n- §5.4 Claude TOST boundary 需提供独立理由\n\n### §6 Conclusion\n- 建议量化复制率：\"8/11 primary+confirmatory cells, 6/24 cross-benchmark cells\"\n\n### Limitations\n- 3 个点覆盖适当（residual confounding, detection vs. amplification, scope），符合 EMNLP 要求\n- evaluator-producer overlap 的 22% inflation 应作为第 4 个 limitation 点提及\n\n### 格式合规\n- ✅ 正文 8 页（Section 1-6 至 page 8）\n- ✅ Limitations 在 page 9，不计入页数\n- ✅ Abstract ~162 词 ≤ 200\n- ✅ 匿名性：\"Anonymous ACL submission\"，无泄露\n- ✅ ACL template with [review] option\n- ⚠️ 缺 Likert (1932) 原始引用\n- ⚠️ 部分引用 arXiv preprint 与正式发表版本混用（camera-ready 前检查）",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n\n**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）\n**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识\n\n---\n\n## Summary\n\n本文定义了 \"Likert Blindspot\"——LLM judge 的 pairwise comparison 能检测到显著风格敏感性而 Likert scoring 检测不到的现象。提出 Controlled Style Decomposition (CSD) 框架，整合 NLI-gated 内容控制、per-axis 风格分解和 position-controlled pairwise comparison。在 5 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash, Claude Sonnet 4）、2 个 primary 风格轴（formality, verbosity）+ 1 个 exploratory（register）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）上实验，结果一致显示 pairwise BT 显著（p < 0.001）而 Likert 不显著（p > 0.17），7 种统计方法交叉确认。GEE 条件分解揭示 per-axis confound structure：verbosity 是 style-dominated（Style OR 8–13, Originality OR < 1），formality 是 quality-confounded（两个 predictor 都显著）。论文坦诚提出三种非排他解释（attenuation, amplification, construct divergence）。\n\n---\n\n## Strengths\n\n**S1. 卓越的实验严谨性。** 六层控制设计（NLI gate, position swap, double-rewrite, debiased prompting, cross-rewriter validation, GEE confound decomposition）在 LLM judge bias 文献中属于最严格的方法控制之一。七种统计方法全部一致确认 Blindspot（Table 14, Appendix M），bootstrap CI、TOST、Bayesian equivalence testing 的组合使用展现了统计成熟度。[R1-S3, R1-S5, R2-S1, 双方 AGREE]\n\n**S2. Per-axis confound structure 是 genuinely novel 的发现。** GEE decomposition 揭示 verbosity 是 style-dominated 而 formality 是 quality-confounded，这种 per-axis 差异不是经典心理测量学能预测的，对 LLM judge 审计策略有直接实践意义——不同风格轴需要不同的审计方法。[R2-S2, R1-S2, 双方 AGREE]\n\n**S3. 诚实的 claim hedging。** 论文主动提出三种非排他解释（§5.1），明确承认 residual confounding 未完全消除，用 \"complements\" 而非 \"surpasses\" 描述与经典框架的关系。DAG 标注为 \"assumed data-generating process, not a claim of perfect identification\"。在 LLM 领域论文中属于少见的审慎态度。[R2-S3, R1-S4, 双方 AGREE]\n\n**S4. 方法论体系化与实践相关性。** CSD 将 NLI gating、style-controlled rewriting、GEE decomposition 组合成完整分析框架，各环节有明确方法论依据。结论直接指向 LLM alignment pipeline 的审计盲区——Likert-based reward model 评估可能漏检 pairwise 能发现的风格偏差。[R2-S4, R2-S5, R1-S1, R1-S2]\n\n**S5. Robustness 检查远超平均水准。** 11 个 NLI 阈值、一致性筛选对比、独立 rewriter、人工标注（100 pairs, AC₁=0.96）、6 个 amplification controls、cross-benchmark 复制、n=355 scaled replication——超过同类论文的平均水准。Bootstrap attenuation analysis 比标准 post-hoc power 更合理。[R1-S3, R1-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] GEE 小样本膨胀严重，仅 1/9 配置有 n=355 复制** [R1-N1, R2-N2, 双方 AGREE]\n- Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，shrinkage 达 49%（Table 2）。但 9 个 judge×axis 配置中仅 1 个做了大样本复制。\n- GPT-4o formality Style OR 2.58 [1.41, 4.73] 经 49% shrinkage 后约 1.32，CI 可能跨 1.0（失去显著性）。Gemini formality Style OR 1.64 [0.91, 2.98] 在 n=88 时已不显著，shrinkage 后几乎必然为零。\n- Verbosity 的外推（\"projected 4–6.5, still ≫ Orig OR < 1\"，§5.2）逻辑成立但未经实证验证。\n- **R2 重要补充**：此问题主要威胁 GEE per-axis 定量结论，Blindspot 存在性（BT 非参数显著性）不受影响。\n- **建议**：至少对一个 verbosity cell 做 n=355 复制验证 shrinkage 预测；正文更突出标注 n=88 OR 为 upper-bound estimates；讨论 GPT-4o formality 的 shrinkage 风险。\n\n**MF2. [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer** [R2-N1, R1 AGREE with nuance]\n- 核心经验发现（pairwise 比 Likert 更敏感）本质上是 Thurstone (1927) Law of Comparative Judgment 的验证。论文在 §1 引用了 Thurstone 并说 \"quantitatively consistent\"，但 Title \"The Likert Blindspot\" 和 Abstract 仍暗示新发现的现象。\n- Introduction 的三个 \"LLM-specific distinctions\" 中，(c) \"near-complete binary split\" 被论文自己承认与经典理论一致（\"consistent with classical predictions when accounting for effect-size-dependent power\"），不构成独立贡献。\n- **R1 补充**：GEE per-axis decomposition（Table 2 的 style-dominated vs quality-confounded 结构差异）是 genuinely novel 的实证发现，不是 Thurstone 能预测的。CSD pipeline 作为完整诊断工具也有组合创新。\n- **共识定位**：contribution 应定位为 \"systematic empirical demonstration in LLM judges + per-axis structure discovery + practical diagnostic tool\"，而非 \"new phenomenon\"。删除 (c) binary split 作为独立 distinction 或降级为\"与经典理论一致的验证\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] Cross-benchmark 复制为选择性报告（6/24 cells）** [R1-N2, R2 AGREE but suggests downgrade]\n- 论文在 AlpacaEval 和 MT-Bench 上仅测试 24 个可能 cells 中的 6 个，选择标准为 \"targeting the strongest effects\"（§5.3）。3 个例外（‡ 行）被 post-hoc 解释为 effect-size dependence，未被前瞻性验证。\n- **R2 缓解**：论文将 cross-benchmark 定位为 exploratory（§4.1），主要 claims 建立在 LLMBar 上。但 §1 Contribution 2 的 \"the first at this scale\" 暗示了更全面的覆盖。\n- **建议**：Contribution 2 弱化为 \"with selective cross-benchmark evidence\"；报告选择标准；考虑补充一个中等效应配置。\n\n**SF2. [warning] Likert Blindspot 缺少正式的 divergence 检验** [R1-W1, R2 AGREE]\n- 论文分别展示 \"BT 显著\" 和 \"Likert 不显著\"，但从未正式检验二者的 effect size 是否 significantly different。Absence of evidence ≠ evidence of absence。\n- n=355 TOST 和 bootstrap attenuation 间接回应，但缺少正式的 measurement-mode interaction test。\n- **建议**：Bootstrap the difference in effect sizes between BT and Likert，检验差异是否显著异于零。\n\n**SF3. [warning] Qwen3-32B evaluator-producer overlap（~22% inflation）** [R1-W2, R2-W2, 双方 AGREE]\n- Qwen3-32B 同时为 rewriter 和 target judge。独立 GPT-4o rewriter 测试（Appendix E）显示 verbosity Style OR 下降 22%（13.10 → 10.17）。Overlap inflation 是 axis-dependent（verbosity 22% > formality 2.1pp）。\n- n=355 唯一复制恰好选用有 overlap 的 Qwen3-32B，不是最 clean 的验证。\n- Appendix E 确认 Blindspot 仍然存在（独立 rewriter: Style OR = 10.17, p = 0.001），overlap 影响效应量级而非现象存在性。\n- **建议**：Table 1 脚注标注 overlap caveat；至少一个 scaled replication 使用非 overlap 配置。\n\n**SF4. [warning] Claude Sonnet 4 负对照不充分** [R1-W3, R2 AGREE]\n- TOST 在 Δ=12pp 时才显著（p=.035），Δ=10pp 不显著（p=.100）。BF₀ < 3（inconclusive）。等价边界 Δ=12pp 的选择是 data-driven 而非 a priori。\n- **R2 补充**：Claude 的价值更在于 discriminative validity（LLMBar n.s. vs AEval verbosity OR = 4.76 significant），说明 CSD 不是 universal false positive machine。\n- **建议**：将 Claude 定位为 \"weak-bias case\" 或 \"discriminative validity evidence\" 而非 \"negative control\"；提供等价边界的独立理由。\n\n**SF5. [warning] FK grade 的 mediator vs. confounder 辨识不足** [R1-W4, R2 AGREE]\n- §5.3 声称 \"FK lies on the causal pathway S → FK → Y... making FK a mediator\"。但 Sobel 建立的是统计中介而非因果中介。替代因果结构（FK 为 collider 或独立 confounder）在统计上不可区分。\n- Mediator 解释下 controlled OR = 2.15，confounder 解释下为无混淆 OR——对应不同政策含义。\n- **建议**：呈现两种因果解释并讨论各自含义，而非仅断言 mediator。\n\n**SF6. [warning] Title \"Blindspot\" 暗示单一因果方向** [R2-W1, R1 AGREE moderate severity]\n- \"Blindspot\" 预设 attenuation 解释（Likert 漏检），与 §5.1 三种非排他解释矛盾。如果 amplification 是主因，应称 \"pairwise 放大镜\" 而非 \"Likert 盲点\"。\n- **R1 缓解**：实证证据权重（n=355 attenuation d→0, 76.6% concordance, 6 amplification controls）整体更支持 attenuation。Title 方向与证据一致，只是过于确定。\n- **建议**：保留 Title，但在 Abstract 更早 qualify——加入 \"an operational descriptor without committing to a specific causal mechanism\"。\n\n### Minor（不影响接收）\n\n- **M1.** \"Consistent pattern\" 与 exceptions 的张力——R2 计算 ~30% exception rate，R1 反驳（Claude 是负对照、Gemini 是 spectrum，实际 8/8 bias-positive cells 全部显示 Blindspot）。建议在 Conclusion 量化复制率。[分歧记录]\n- **M2.** Register 轴结果弱（BT .553–.635, quality-confounded）——R2 建议移至 Appendix，R1 反驳（需要 per-axis diversity 展示谱系）。[分歧记录]\n- **M3.** GEE omitted variable bias——R1 建议报告 E-value，R2 部分反驳（GEE 定位为 descriptive），但同意 E-value 是低成本改进。[轻微分歧]\n- **M4.** 论文使用 1-10 整数量表称 \"Likert\"，严格应为 interval rating scale，缺 Likert (1932) 原始引用。\n- **M5.** Table 1 \"Cat.\" 列标注（†, †_e, †_c, ---）难以解析，建议改为文字标签。\n- **M6.** Figure 5 y 轴 \"Odds Ratio\" log scale 应标注，Figure 2 DAG 注释字号偏小。\n- **M7.** BT choix regularization α=10⁻⁶ 实质为零正则化，建议报告 α 敏感性。\n- **M8.** 100-point continuous Likert（Appendix O）未报告评分分布——是否有 evidence judges 利用了 granularity？\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Scaled replication 覆盖不足**是论文最大弱点——9 个 judge×axis 配置仅 1 个有 n=355 验证，GEE 定量结论的可靠性存疑。[R1-N1 + R2-N2]\n2. **核心发现是 Thurstone domain transfer**，novelty 主要来自 GEE per-axis decomposition 和 CSD 诊断工具，需要更精确定位。[R2-N1 + R1 AGREE]\n3. **Qwen3-32B evaluator-producer overlap** 影响效应量级（~22%），但不影响现象存在性。[R1-W2 + R2-W2]\n4. **缺少正式 divergence 检验**——论文未正式检验 BT 和 Likert 的 effect size 是否 significantly different。[R1-W1 + R2 AGREE]\n5. **Claude 负对照的 TOST boundary** 是 data-driven，不够严格。[R1-W3 + R2 AGREE]\n6. **FK mediator claim** 需要降级为 \"plausible under assumed causal model\"。[R1-W4 + R2 AGREE]\n7. **实验执行和 robustness 检查**远超同类论文水准。[双方一致]\n\n## Reviewer Divergence [REBUT]\n\n1. **Cross-benchmark 严重性**：R1 列为 Must-Fix（确认偏差），R2 建议降级 Should-Fix（论文标注为 exploratory，主 claims 不依赖）。→ 报告采纳 Should-Fix（SF1）。\n2. **Register 轴位置**：R2 建议移至 Appendix（结果弱、quality-confounded），R1 反驳（需要 per-axis diversity 展示 verbosity/formality/register 谱系）。→ 记录分歧，不列为 action item。\n3. **\"Consistent\" 措辞**：R2 认为 ~30% exception rate 下过强，R1 反驳（Claude 是负对照不是例外，实际 8/8 bias-positive cells）。→ 建议量化复制率让读者自行判断。\n4. **GEE omitted variables**：R1 要求 E-value（Should-Fix），R2 认为 GEE 是 descriptive 定位（nice-to-have）。→ 建议报告但不列为 Must-Fix。\n\n---\n\n## Questions to Authors\n\n1. n=355 复制是否使用相同 NLI gating threshold (0.90)？pass rate 是否与 n=88 可比？[R1-Q1]\n2. 各 judge 的 Likert 评分分布是什么（histogram）？如果 judges 集中在某几个分数点，这直接解释 tie rate 和 Blindspot 机制。[R1-Q2]\n3. §1 \"76–92% of preferences originate from style cues\" 如何计算？引用他人 claim 时其 operationalization 是否与本文一致？[R1-Q3]\n4. 为什么 n=355 复制只选了 Qwen3-32B formality——是否有资源约束？[R1-Q4]\n5. 76.6% non-tie concordance 中 23.4% discordance——在哪个效应量阈值以下 construct divergence 可能成为主导解释？[R2-Q1]\n6. GEE exchangeable correlation α̂ ∈ [−0.25, +0.11]——−0.25 不算\"接近零\"，论文应改为 \"correlation structure choice does not affect estimates due to sandwich robustness\" 而非声称接近零。[R2-Q4, R1 交叉确认]\n\n---\n\n## Missing References\n\n1. **Likert (1932)**. A technique for the measurement of attitudes. 论文大量使用 \"Likert\" 但未引用原始文献。[R1 提出, R2 AGREE]\n2. **Polo et al. (2024)**. TinyBenchmarks — IRT 在 NLG evaluation 中的应用，与 measurement-mode 讨论直接相关。[R2 提出, R1 AGREE]\n3. **Likert scale anchoring effects** 相关文献——LLM judge 可能以不同方式解释 1-10 scale 锚点。[R2 提出]\n\n---\n\n## External Review\n\n**状态**：未配置。项目未启用外部审稿（paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（耗时 ~5 分钟）。7 个 info 级建议，无 critical 或 warning。\n\n主要发现：\n- 首页无 display item（Figure 1 在 page 2），ACL 双栏常见但可考虑 teaser figure\n- Figure 1 caption 较简短，建议补充每阶段核心操作的一句话描述\n- Figure 2 DAG 中部分注释文字字号偏小，建议确认打印后可读\n- Page 8 左栏 Figure 5 + Figure 6 连续放置，视觉密度较高但内容相关可接受\n- Figure 5/6 axis label 和 legend 字号接近正文 70% 下限，建议验证 camera-ready 打印可读性\n- 附录末页约 30% 空白，可接受\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.75 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**接收建议**：Borderline Conference — 修改后可能达到 Conference (4.0) 水平。\n\n**拉向 3.5 而非 3.0 的因素**：\n1. 实验规模和控制的 thoroughness 在同类工作中突出（5 judges × 3 benchmarks × 3 axes + n=355 replication）\n2. GEE per-axis decomposition 提供了超越 Thurstone 框架的 genuinely new insight\n3. 实践相关性强——directly actionable for RLHF/DPO pipeline audits\n4. Robustness 检查远超平均（7 种统计方法、11 NLI 阈值、人工标注 AC₁=0.96）\n\n**阻止达到 4.0 的因素**：\n1. 核心现象是经典测量理论的 domain transfer，novelty ceiling 有限（Excitement 3.0）\n2. GEE 定量结论依赖 n=88 膨胀估计，仅 1/9 配置有大样本验证\n3. Cross-benchmark 覆盖为选择性报告（6/24 cells）\n4. 缺少正式的 measurement-mode divergence 检验\n\n**修改路径**：补做至少一个 verbosity cell 的 n=355 复制 + 精确定位 novelty（降低 \"new phenomenon\" 暗示）+ 补充 formal divergence test → 预计可提升至 4.0。\n\n---\n\n## Detailed Comments\n\n### Abstract (~162 词，符合 200 词限制)\n- \"consistently\" 一词在仅 2 primary axes 基础上过强，建议改为 \"across two primary style axes, with varying effect sizes across judges\"\n- 缺少操作性定义的 early qualification——读者从 \"Likert Blindspot\" 获得单一方向印象\n\n### §1 Introduction\n- 三个 LLM-specific distinctions 中 (c) binary split 应删除或降级——论文自己承认 \"consistent with classical predictions\"\n- Contribution 2 \"the first at this scale\" 暗示全面的 cross-benchmark 覆盖，但实际仅 6/24 cells\n- \"76–92% of preferences originate from style cues\" 引用外部 claim，其 operationalization 与本文是否一致需澄清\n\n### §3 Method\n- §3.1 style classifier (Qwen3-32B) 的系统性偏差风险需讨论，虽然 NLI gate 和 direction asymmetry analysis 提供了缓解\n- §3.3 \"forced choice\" 描述准确，但应注明 1-10 量表与 Likert (1932) 原始定义的区别\n\n### §4 Experiments\n- §4.1 BT regularization α=10⁻⁶ 的敏感性应报告\n- n=355 复制应说明是否使用相同 NLI threshold\n\n### §5 Analysis\n- §5.1 需补充正式的 measurement-mode divergence 检验\n- §5.2 GEE OR 的 upper-bound nature 应在正文更突出讨论，不仅是 Table 2 caption\n- §5.2 verbosity GEE 定量结论应标注为 \"projected, pending large-sample validation\"\n- §5.3 FK mediator claim 需降级为 \"plausible under assumed causal model\"\n- §5.3 cross-benchmark 选择标准应透明化\n- §5.4 Claude TOST boundary 需提供独立理由\n\n### §6 Conclusion\n- 建议量化复制率：\"8/11 primary+confirmatory cells, 6/24 cross-benchmark cells\"\n\n### Limitations\n- 3 个点覆盖适当（residual confounding, detection vs. amplification, scope），符合 EMNLP 要求\n- evaluator-producer overlap 的 22% inflation 应作为第 4 个 limitation 点提及\n\n### 格式合规\n- ✅ 正文 8 页（Section 1-6 至 page 8）\n- ✅ Limitations 在 page 9，不计入页数\n- ✅ Abstract ~162 词 ≤ 200\n- ✅ 匿名性：\"Anonymous ACL submission\"，无泄露\n- ✅ ACL template with [review] option\n- ⚠️ 缺 Likert (1932) 原始引用\n- ⚠️ 部分引用 arXiv preprint 与正式发表版本混用（camera-ready 前检查）",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-23T14:43:53.403197+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 1510 · 2026-05-23T14:44:05.651337+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结：**

- **Overall**: 3.5 / 5（Borderline Conference）
- **两个 Must-Fix**：(1) GEE n=88 膨胀 49%，仅 1/9 配置有 n=355 复制；(2) 新颖性定位需精确化——核心发现是 Thurstone 1927 domain transfer，三个 LLM-specific distinctions 中 (c) binary split 应删除
- **六个 Should-Fix**：cross-benchmark 选择性报告、缺少正式 divergence test、Qwen3-32B overlap、Claude 负对照不充分、FK mediator 辨识不足、Title framing
- **修改路径**：补做 verbosity n=355 复制 + 精确定位 novelty + 补 formal divergence test → 预计可提升至 4.0
- **Issue tracker 已更新**（Round 18，新增 3 条，更新 12 条）
- **视觉审查**：已完成，7 个 info 级建议，无阻塞问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 145

## Round 145

2 recorded events


### User

_source line 1511 · 2026-05-23T14:44:08.173116+00:00_

[Reviewer 1 审稿结果]:
交叉审稿回应已提交。

汇总：对 R2 的 2 个 Must-Fix 全部 [AGREE]（N1 novelty framing 和 N2 scaled replication 覆盖），4 个 Should-Fix 中 2 个 [AGREE]（W1 title 方向性、W2 overlap）、2 个 [REBUT]（W3 register 保留在主文有方法论价值、W4 exception rate 被高估——primary cells 一致性为 8/8）。4 个 Questions 均给出了技术回应，其中 Q2（100-point scale 评分分布未报告）和 Q4（α̂=−0.25 的表述应修正）是有价值的建设性意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1512 · 2026-05-23T14:44:20.893360+00:00_

审稿报告已投递至 Research Director。

**本轮审稿结果汇总：**

- **Overall**: 3.5 / 5（Borderline Conference）
- **两位 Reviewer 评分一致**，核心共识清晰
- **2 个 Must-Fix**：(1) GEE n=88 膨胀 49%，仅 1/9 配置有 n=355 复制；(2) 新颖性定位需更精确——核心现象是 Thurstone 1927 domain transfer
- **6 个 Should-Fix**：cross-benchmark 选择性、缺正式 divergence 检验、evaluator-producer overlap、Claude 负对照不充分、FK mediator 辨识、Title framing
- **修改路径**：补做 verbosity n=355 复制 + 精确定位 novelty + 补 formal divergence test → 预计可提升至 4.0

Issue tracker 已同步更新至 Round 18。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 146

## Round 146

74 recorded events


### User

_source line 1513 · 2026-05-25T21:14:06.411380+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (Long Paper, via ARR)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-25T21:14:15.447896+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1515 · 2026-05-25T21:14:15.499984+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1516 · 2026-05-25T21:14:22.978456+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-25T21:14:23.079197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-25T21:14:35.875079+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-25T21:14:35.926309+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-25T21:14:38.385928+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-25T21:14:38.436661+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-25T21:14:41.751029+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-25T21:14:41.801639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-25T21:14:56.108099+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-25T21:14:56.158753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-25T21:15:05.695939+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-25T21:15:07.654102+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (58 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **llama70b_crossbench** (negative): Llama-70B exhibits style blindspots (BT-significant pairwise preference for formal/verbose responses, but non-significant Likert ATE) across AlpacaEval and MT-Bench benchmarks, consistent with the LLMBar pattern.\n- **formality_llama_rewriter** (success): Qwen3-32B judge's formality bias is rewriter-independent: using Llama-3.3-70B-Instruct instead of Qwen3-32B as the RATE counterfactual rewriter will reproduce significant pairwise preference for formal style (BT p<0.05), confirming the bias originates in the judge, not the rewriter.\n- **formality_scaled_n300** (success): Llama-70B scoring of the existing n=355 formality scaled data will replicate the formality Blindspot pattern seen with Qwen3-32B (BT ~67%, Likert NS), providing cross-judge validation at scale. GEE Style OR will show small-sample shrinkage similar to Qwen3 (4.20→2.15).\n\n## 趋势\n成功 41 / 负向 13 / 失败 0 / 共 58\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1958
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-25T21:15:07.654566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-25T21:15:08.156863+00:00_

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
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\noindent\textbf{Residual confounding.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself; residual confounding is not fully eliminated despite logistic adjustment.
43	
44	\noindent\textbf{Detection vs.\ amplification.}
45	The Blindspot may partly reflect pairwise format amplification \citep{jeong2025comparative} rather than pure detection; six controls bound this risk (\S\ref{sec:amplification}), but we cannot precisely quantify the amplification factor.
46	
47	\noindent\textbf{Scope.}
48	CSD applies only to surface-level axes whose rewrites preserve semantic content. Primary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.
49	
50	\bibliography{references}
51	
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-25T21:15:08.157214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1531 · 2026-05-25T21:15:09.864485+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1532 · 2026-05-25T21:15:10.015606+00:00_

-rw-r--r-- 1 ubuntu ubuntu 4992667 May 25 21:11 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-25T21:15:13.076469+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"MRL Workshop at EMNLP 2025: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/mrl-workshop-emnlp-2025-first-call-papers"}]

Based on the search results, I found information about EMNLP 2026 submission deadlines through ACL Rolling Review (ARR). Here are the key details:

The ARR submission deadline for EMNLP 2026 is May 25, 2026. The ARR commitment deadline is in early August.


…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 4919
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-25T21:15:18.144449+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline ARR commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 1535 · 2026-05-25T21:15:18.596518+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadlines cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission deadlines cycle"
  }
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-25T21:15:19.349469+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-25T21:15:19.400125+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1538 · 2026-05-25T21:15:23.515226+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here are the key deadlines for EMNLP 2026:

## ARR Submission Deadline
The ARR submission deadline for long and short papers is May 25, 2026.

## EMNLP Commitment Deadline
The EMNLP commitment deadline is August 2, 2026.

## Other Important Dates
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- Notification of acceptance: August 20, 2026
- Camera-read
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5370
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-25T21:15:24.168331+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadlines cycle"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's information about the ACL Rolling Review 2026 submission deadlines and cycle structure:

## Cycle Structure

The ACL Peer Review Committee recommended switching to 10-week review cycles, with the new schedule taking effect starting in May 2025. This means there will generally be 5 cycles per year instead of 6.

## 2026 January Cycle Deadlines

For the January 2026 cycle, here are the key deadlines:

- Author registration form deadline: January 7th 2026 EoD AoE
- Area Chair checklist deadline: January 18th
- Reviewer checklist deadline: January 21st
- Review deadline: February 7th, and meta-review deadline: March 3rd
- ARR reviews & meta-reviews available to authors: March 10, 2026

## Important Policy Notes

Starting from this cycle, ARR intends to strictly monitor adherence to reviewing responsibilities, and papers whose authors have not registered as reviewers or area chairs or have not completed their checkl
…[truncated 171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5571
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-25T21:15:35.713749+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-25T21:15:36.266255+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1542 · 2026-05-25T21:15:36.316945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers author guidelines page limit anonymity site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers author guidelines page limit anonymity site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 1543 · 2026-05-25T21:15:41.386424+00:00_

Web search results for query: "EMNLP 2026 call for papers author guidelines page limit anonymity site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

Based on the search results from the EMNLP 2026 website, here are the key details about author guidelines:

**Anonymity:**
Following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing process will continue to be double-blind, with reviewers not seeing authors and authors not seeing reviewers.

**Page Limits:**
The search results do not contain specific page limit information for main conference papers. However, for reference, the results do mention that the Limitations section, which is required, should be included at the end of the paper before the references and will not count toward the page limit. For tutorials, proposals should not exceed 4 pages of content plus one page for tutor biographies and unlimited pages for references.

To find the specific page limits for main conf
…[truncated 329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5069
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-25T21:15:46.969475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-25T21:15:48.337642+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring yield divergent style-sensitivity profiles in LLM judges.
3	We define the \emph{Likert Blindspot}: statistically significant pairwise sensitivity absent from Likert, admitting non-exclusive explanations (measurement attenuation, format amplification, construct divergence).
4	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic combining natural language inference (NLI) gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
5	Across four target judges and two axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.28$), selectively replicated across three benchmarks and confirmed by seven statistical methods; a fifth judge shows benchmark-dependent sensitivity.
6	At $n = 355$, Likert effect sizes collapse toward zero while pairwise remains stable; at $n = 330$, Likert begins detecting only the strongest effects, revealing a $3$--$4\times$ efficiency gap rather than absolute failure.
7	Generalized estimating equation (GEE) decomposition shows per-axis confound structures: verbosity is style-dominated (style odds ratio [OR] $8$--$13$ at $n{=}86$--$88$), while formality reflects joint style--quality confounding.
8	Non-tie concordance (76.6\%, $p < .001$) favors attenuation over construct divergence.
9	Likert-only audits risk missing style preferences that propagate through pairwise-based alignment pipelines\footnote{Code and data are available at \url{https://anonymous.4open.science/r/causal_style_decomp_judge-5EBE/}.}.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 1368
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-25T21:15:48.388266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 1547 · 2026-05-25T21:15:48.388647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1548 · 2026-05-25T21:15:48.840702+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} In our experiments, given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}, an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations (Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences), which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	This example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
8	
9	LLM judges are central infrastructure for natural language processing (NLP) evaluation and alignment training (reinforcement learning from human feedback [RLHF], direct preference optimization [DPO]), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Despite this, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, confound-structure analysis, and black-box applicability.
11	Classical psychometrics es
…[truncated 2739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-25T21:15:48.841099+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Interventional Approaches to Judge Bias}
5	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
6	\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.
7	CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
8	\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.
9	
10	\paragraph{Style Bias in LLM Judges}
11	The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
12	Style bias as a separate source has received recent attention \citep{wu2023style,murugadoss2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \citet{li2026preference} show that style-mediated \emph{preference leakage} propagates through evaluation pipelines.
13	Multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses that cannot distinguish causal style effects from content quality confounds.
14	\citet{jeong2025comparative} identify the Comparative Trap (pairwise comparison may amplify style biases), which we address in \S\ref{sec:amplification}.
15	Unlike human evaluators, LLM judges acquire format-specific biases through RLHF training: pairwise comparison serves as the reward signa
…[truncated 987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-25T21:15:48.841372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-25T21:15:51.250547+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis while holding content fixed, a single-axis intervention design that enables per-axis causal attribution rather than aggregate style sensitivity measurement.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7, selected to balance diversity with coherence in pilot experiments) according to an axis-specific prompt (Appendix~\ref{app:rewriting_prompts}).
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation approximates a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}; Appendix~\ref{app:cross_axis_contamination}).
12	To control for rewriting artifact bias (the possibility that the judge prefers original text over any rewrite regardless of style), we also generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on Multi-Genre NLI (MNLI; \citealp{williams2018broad}) with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref
…[truncated 5675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 2409
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-25T21:15:51.301201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-25T21:15:51.302110+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests (three target judges $\times$ two axes), corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from family-wise error rate (FWER) control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
13	In binary-choice BT models, independence of irrelevant alternatives (IIA) is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42; we verify bootstrap stability by confirming that halving the resample count changes interval widths by $<$1pp.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	A prospective power analysis 
…[truncated 19200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-25T21:15:51.302563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-25T21:15:51.304635+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	CSD yields two findings: the \emph{Likert Blindspot} (8/8 primary cells, $d \!\to\! 0$ at $n{=}355$; concordance $p < .001$ favors attenuation) and per-axis confound structures via GEE (verbosity style-dominated, formality conditional).
4	Practically, Likert-only audits risk false negatives at benchmark sizes $n < 200$; per-axis decomposition reveals that verbosity preferences are predominantly style-driven while formality partially reflects quality differences---a distinction invisible to aggregate metrics and consequential for RLHF pipelines where pairwise judgments serve as reward signals.
5	CSD extends to any surface-level axis with content-preserving rewrites; deeper axes remain for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-25T21:15:51.304914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 1557 · 2026-05-25T21:15:51.355429+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"page limit\" \"long paper\" OR \"short paper\" main conference ARR guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"page limit\" \"long paper\" OR \"short paper\" main conference ARR guidelines"
  }
}
```

</details>

---


### Tool result

_source line 1558 · 2026-05-25T21:15:51.707955+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V), non-tie concordance (W).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\label{app:direction}
18	
19	The formality ax
…[truncated 51943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-25T21:15:56.325158+00:00_

Web search results for query: ""EMNLP 2026" "page limit" "long paper" OR "short paper" main conference ARR guidelines"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Paper Guidelines","url":"https://www.araseg.aramlab.ai/paper-guidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the page limit information for EMNLP 2026:

For EMNLP 2026, the format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.

Both long and short paper submissions should follow all of the ARR submission requirements, which includes adherence to ACL's Publication Ethics Policy and ARR's Ethics Policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 4969
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-25T21:16:22.283446+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-25T21:16:25.194467+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (58 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **llama70b_crossbench** (negative): Llama-70B exhibits style blindspots (BT-significant pairwise preference for formal/verbose responses, but non-significant Likert ATE) across AlpacaEval and MT-Bench benchmarks, consistent with the LLMBar pattern.\n- **formality_llama_rewriter** (success): Qwen3-32B judge's formality bias is rewriter-independent: using Llama-3.3-70B-Instruct instead of Qwen3-32B as the RATE counterfactual rewriter will reproduce significant pairwise preference for formal style (BT p<0.05), confirming the bias originates in the judge, not the rewriter.\n- **formality_scaled_n300** (success): Llama-70B scoring of the existing n=355 formality scaled data will replicate the formality Blindspot pattern seen with Qwen3-32B (BT ~67%, Likert NS), providing cross-judge validation at scale. GEE Style OR will show small-sample shrinkage similar to Qwen3 (4.20→2.15).\n\n## 趋势\n成功 41 / 负向 13 / 失败 0 / 共 58\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2911
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-25T21:16:25.197032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml', 'r') as f:\n    config = yaml.safe_load(f)\nprint(yaml.dump(config.get('external_review', {}), default_flow_style=False))\n\" 2>/dev/null || echo \"CONFIG_READ_FAILED\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml', 'r') as f:\n    config = yaml.safe_load(f)\nprint(yaml.dump(config.get('external_review', {}), default_flow_style=False))\n\" 2>/dev/null || echo \"CONFIG_READ_FAILED\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-25T21:16:26.150823+00:00_

CONFIG_READ_FAILED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-25T21:16:26.653228+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-25T21:16:28.362088+00:00_

&lt;persisted-output>
Output too large (36.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/4af966e3-d20a-466c-a44b-90dc296436ff/tool-results/by0bd4hat.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 1-4 issues (all resolved)
  # ============================================================

  - id: "R1-N1"
    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
    resolution_round: 4

  - id: "R2-N1"
    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 1
    last_seen_round: 18
    resolution: null
    resolution_round: null
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
      - round: 8
        reviewers: [1, 2]
        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
      - round: 9
        reviewers: [1, 2]
        note: "R9 fresh review 两位 Reviewer 独立再次提出。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。"
      - round: 11
        reviewers: [1, 2]
        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。"
      - round: 12
        reviewers: [1, 2]
        note: "R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。"
      - round: 13
        reviewers: [1, 2]
        note: "R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。"
      - round: 14
        reviewers: [1, 2]
        note: "R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。"
      - round: 15
  
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 1708
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-25T21:16:28.362668+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf 2>/dev/null || echo \"PDFINFO_UNAVAILABLE\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf 2>/dev/null || echo \"PDFINFO_UNAVAILABLE\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-25T21:16:28.516750+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Mon May 25 21:11:04 2026 UTC
ModDate:         Mon May 25 21:11:04 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           20
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       4992667 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-25T21:16:35.492101+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-25T21:16:38.603864+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 3111
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-25T21:16:38.604194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/4af966e3-d20a-466c-a44b-90dc296436ff/tool-results/by0bd4hat.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/4af966e3-d20a-466c-a44b-90dc296436ff/tool-results/by0bd4hat.txt"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-25T21:16:38.856733+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 18
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。"
44	      - round: 13
45	        reviewers: [1, 2]
46	        note: "R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。"
47	      - round: 14
48	        reviewers: [1, 2]
49	        note: "R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。"
50	      - round: 15
51	        reviewers: [1, 2]
52	        note: "R15 fresh review: 两位再次独立提出。"
53	      - round: 16
54	        reviewers: [1, 2]
55	        note: "R16: S4 称 GEE decomposition 是'真正的方法论
…[truncated 33764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1572 · 2026-05-25T21:17:20.473442+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_style_decomp_judge",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool call

_source line 1573 · 2026-05-25T21:17:20.826120+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1574 · 2026-05-25T21:17:24.093055+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3619
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-25T21:17:24.093535+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3267
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-25T21:17:32.078835+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-25T21:17:32.129520+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-25T21:17:35.592453+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent"
  }
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-25T21:17:35.793569+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_director_acab027e.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1580 · 2026-05-25T21:17:39.407647+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 1581 · 2026-05-25T21:17:39.508459+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-25T21:18:17.856634+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 审稿任务 — Round 1\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Long Paper, via ARR)\n**ARR Submission Deadline**: May 25, 2026\n**Commitment Deadline**: August 2, 2026\n**格式要求**: 8 页正文 + 无限参考文献，Limitations 必须放在正文中（不计入 8 页），double-blind，ACL 模板\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf` (20 pages, A4)\n**LaTeX 源码**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **统计框架**\n   - Holm-Bonferroni 多重比较校正是否正确应用？Primary family 定义是否合理（排除 Gemini 的理由是否充分）？\n   - Bradley-Terry 模型假设（IIA, unidimensionality）在本场景下是否合理？正则化参数敏感性？\n   - GEE 模型选择（exchangeable correlation, additive specification）是否恰当？omitted variable bias 风险？\n   - Bootstrap CI（10,000 resamples）的实现是否标准？seed 固定是否影响可复制性？\n   - Power analysis 是否避免了 post-hoc power 的常见陷阱？\n\n2. **NLI Gate 设计**\n   - 0.90 阈值的选择是否有充分依据？\n   - Direction-aware vs bidirectional gating 策略是否合理？\n   - Gate precision 验证（human annotation）是否充分？\n   - NLI gate 能否真正阻断 content quality confound？\n\n3. **因果推断**\n   - DAG 中各路径的控制策略是否完备？residual confounding 的讨论是否充分？\n   - \"interventional rather than formal causal\" 的 disclaimer 是否与正文中的因果语言一致？\n   - GEE decomposition 是否被过度解读为 causal identification？\n   - Same-style double-rewrite control 的有效性？\n\n4. **数据完整性**\n   - 样本量（n=86-88 primary, n=355 scaled）是否足够支撑各项 claim？\n   - n=88 到 n=355 的 GEE OR shrinkage (49%) 对结论的影响？\n   - Cross-benchmark replication 的选择性（6/24 cells）是否构成确认偏差？\n   - Evaluator-producer overlap（Qwen3-32B 同时作为 rewriter 和 judge）的处理是否充分？\n\n5. **Robustness**\n   - NLI threshold sensitivity sweep 结果是否令人信服？\n   - 100-point continuous Likert scale 实验是否充分排除了 scale granularity 解释？\n   - Claude 作为 negative control 的 TOST equivalence testing 是否有力？\n   - Concordance analysis 能否真正区分 attenuation 和 construct divergence？\n\n请按 EMNLP 2026 ARR 的标准出具审稿意见，结构如下：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者澄清的)\n- **Missing References** (如有)\n- **Soundness**: 1-5\n- **Overall Assessment**: 使用 ARR 评分标准 (1-5)\n- **Confidence**: 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 审稿任务 — Round 1\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Long Paper, via ARR)\n**ARR Submission Deadline**: May 25, 2026\n**Commitment Deadline**: August 2, 2026\n**格式要求**: 8 页正文 + 无限参考文献，Limitations 必须放在正文中（不计入 8 页），double-blind，ACL 模板\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf` (20 pages, A4)\n**LaTeX 源码**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **统计框架**\n   - Holm-Bonferroni 多重比较校正是否正确应用？Primary family 定义是否合理（排除 Gemini 的理由是否充分）？\n   - Bradley-Terry 模型假设（IIA, unidimensionality）在本场景下是否合理？正则化参数敏感性？\n   - GEE 模型选择（exchangeable correlation, additive specification）是否恰当？omitted variable bias 风险？\n   - Bootstrap CI（10,000 resamples）的实现是否标准？seed 固定是否影响可复制性？\n   - Power analysis 是否避免了 post-hoc power 的常见陷阱？\n\n2. **NLI Gate 设计**\n   - 0.90 阈值的选择是否有充分依据？\n   - Direction-aware vs bidirectional gating 策略是否合理？\n   - Gate precision 验证（human annotation）是否充分？\n   - NLI gate 能否真正阻断 content quality confound？\n\n3. **因果推断**\n   - DAG 中各路径的控制策略是否完备？residual confounding 的讨论是否充分？\n   - \"interventional rather than formal causal\" 的 disclaimer 是否与正文中的因果语言一致？\n   - GEE decomposition 是否被过度解读为 causal identification？\n   - Same-style double-rewrite control 的有效性？\n\n4. **数据完整性**\n   - 样本量（n=86-88 primary, n=355 scaled）是否足够支撑各项 claim？\n   - n=88 到 n=355 的 GEE OR shrinkage (49%) 对结论的影响？\n   - Cross-benchmark replication 的选择性（6/24 cells）是否构成确认偏差？\n   - Evaluator-producer overlap（Qwen3-32B 同时作为 rewriter 和 judge）的处理是否充分？\n\n5. **Robustness**\n   - NLI threshold sensitivity sweep 结果是否令人信服？\n   - 100-point continuous Likert scale 实验是否充分排除了 scale granularity 解释？\n   - Claude 作为 negative control 的 TOST equivalence testing 是否有力？\n   - Concordance analysis 能否真正区分 attenuation 和 construct divergence？\n\n请按 EMNLP 2026 ARR 的标准出具审稿意见，结构如下：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者澄清的)\n- **Missing References** (如有)\n- **Soundness**: 1-5\n- **Overall Assessment**: 使用 ARR 评分标准 (1-5)\n- **Confidence**: 1-5"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-25T21:18:40.105463+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22248
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-25T21:18:40.457170+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 审稿任务 — Round 1\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Long Paper, via ARR)\n**ARR Submission Deadline**: May 25, 2026\n**Commitment Deadline**: August 2, 2026\n**格式要求**: 8 页正文 + 无限参考文献，Limitations 必须放在正文中（不计入 8 页），double-blind，ACL 模板\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf` (20 pages, A4)\n**LaTeX 源码**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **Novelty 评估**\n   - \"Likert Blindspot\" 作为主要贡献是否具有足够的新颖性？Thurstone (1927) 以来 pairwise vs rating 的差异是心理测量学已知现象，本文在 LLM judge 领域的 domain transfer 是否构成足够的 novelty？\n   - CSD 方法论相比 RATE (Reber et al., 2025) 的增量贡献是什么？差异化论证是否清晰有力？\n   - GEE per-axis decomposition 作为贡献是否被充分强调？是否是本文真正的方法论亮点？\n   - 三个 claimed contributions 的措辞是否精确？是否过度 claim？\n\n2. **叙事逻辑与 Framing**\n   - Title \"The Likert Blindspot\" 是否预设了 Likert attenuation 解释，与正文三种非排他解释（attenuation, amplification, construct divergence）存在张力？\n   - Abstract 是否在 200 words 以内？是否准确反映了论文的贡献和限制？\n   - Introduction 的 motivating example（\"What is the average height for a male?\"）是否具有代表性和说服力？\n   - \"consistent pattern\" / \"systematic\" 等措辞是否与实际数据一致（考虑 Claude 的 null results 和 ~30% exception rate）？\n\n3. **Related Work**\n   - 对 RATE, CASSE, FairJudge, Comparative Trap 等关键工作的定位是否准确？\n   - 是否遗漏了重要的相关工作？特别是 2025-2026 年的最新进展\n   - LLM judge bias 文献覆盖是否全面？\n   - 经典心理测量文献的引用是否恰当？\n\n4. **写作质量**\n   - 正文 8 页的信息密度和可读性？\n   - Table 1 的设计——15 行 + 复杂脚注是否易于解读？\n   - 图表（pipeline, DAG, forest plot, power curve, heatmap, GEE decomposition）是否清晰有效？\n   - Appendix 组织是否合理？23 个 section 是否过于冗长？\n   - Limitations section 是否恰当？（EMNLP 2026 要求放在正文中，不计入页数）\n\n5. **完整性**\n   - 仅两个主轴（formality, verbosity）+ 一个 exploratory（register），scope 是否足以支撑 claim？\n   - 4 target judges + 1 discriminative validity，是否覆盖了主流 LLM judges？\n   - Cross-benchmark replication 策略（选择最强 effects 的 6/24 cells）是否合理？\n   - Anonymous code/data link 是否有效？\n\n请按 EMNLP 2026 ARR 的标准出具审稿意见，结构如下：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者澄清的)\n- **Missing References** (如有)\n- **Excitement**: 1-5\n- **Overall Assessment**: 使用 ARR 评分标准 (1-5)\n- **Confidence**: 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 审稿任务 — Round 1\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**目标 Venue**: EMNLP 2026 (Main Conference, Long Paper, via ARR)\n**ARR Submission Deadline**: May 25, 2026\n**Commitment Deadline**: August 2, 2026\n**格式要求**: 8 页正文 + 无限参考文献，Limitations 必须放在正文中（不计入 8 页），double-blind，ACL 模板\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf` (20 pages, A4)\n**LaTeX 源码**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **Novelty 评估**\n   - \"Likert Blindspot\" 作为主要贡献是否具有足够的新颖性？Thurstone (1927) 以来 pairwise vs rating 的差异是心理测量学已知现象，本文在 LLM judge 领域的 domain transfer 是否构成足够的 novelty？\n   - CSD 方法论相比 RATE (Reber et al., 2025) 的增量贡献是什么？差异化论证是否清晰有力？\n   - GEE per-axis decomposition 作为贡献是否被充分强调？是否是本文真正的方法论亮点？\n   - 三个 claimed contributions 的措辞是否精确？是否过度 claim？\n\n2. **叙事逻辑与 Framing**\n   - Title \"The Likert Blindspot\" 是否预设了 Likert attenuation 解释，与正文三种非排他解释（attenuation, amplification, construct divergence）存在张力？\n   - Abstract 是否在 200 words 以内？是否准确反映了论文的贡献和限制？\n   - Introduction 的 motivating example（\"What is the average height for a male?\"）是否具有代表性和说服力？\n   - \"consistent pattern\" / \"systematic\" 等措辞是否与实际数据一致（考虑 Claude 的 null results 和 ~30% exception rate）？\n\n3. **Related Work**\n   - 对 RATE, CASSE, FairJudge, Comparative Trap 等关键工作的定位是否准确？\n   - 是否遗漏了重要的相关工作？特别是 2025-2026 年的最新进展\n   - LLM judge bias 文献覆盖是否全面？\n   - 经典心理测量文献的引用是否恰当？\n\n4. **写作质量**\n   - 正文 8 页的信息密度和可读性？\n   - Table 1 的设计——15 行 + 复杂脚注是否易于解读？\n   - 图表（pipeline, DAG, forest plot, power curve, heatmap, GEE decomposition）是否清晰有效？\n   - Appendix 组织是否合理？23 个 section 是否过于冗长？\n   - Limitations section 是否恰当？（EMNLP 2026 要求放在正文中，不计入页数）\n\n5. **完整性**\n   - 仅两个主轴（formality, verbosity）+ 一个 exploratory（register），scope 是否足以支撑 claim？\n   - 4 target judges + 1 discriminative validity，是否覆盖了主流 LLM judges？\n   - Cross-benchmark replication 策略（选择最强 effects 的 6/24 cells）是否合理？\n   - Anonymous code/data link 是否有效？\n\n请按 EMNLP 2026 ARR 的标准出具审稿意见，结构如下：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者澄清的)\n- **Missing References** (如有)\n- **Excitement**: 1-5\n- **Overall Assessment**: 使用 ARR 评分标准 (1-5)\n- **Confidence**: 1-5"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-25T21:18:41.818626+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 1586 · 2026-05-25T21:20:01.453083+00:00_

圆桌审稿会议已启动：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性（统计框架、NLI gate、因果推断、数据完整性） | 🔄 审稿中 |
| Reviewer 2 | 新颖性/完整性（贡献定位、叙事逻辑、Related Work、写作质量） | 🔄 审稿中 |
| 视觉审查 Agent | PDF 排版质量检查 | 🔄 进行中 |
| 外部审稿 | 未配置，跳过 | ⏭️ |

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 147

## Round 147

4 recorded events


### User

_source line 1587 · 2026-05-25T21:26:07.593998+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 审稿意见

**论文**: "The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation"
**审查侧重**: 新颖性 / 完整性

---

### Summary

本文提出 Controlled Style Decomposition (CSD)，一种 black-box 诊断框架，通过 NLI 门控内容保持、单轴风格重写和位置控制的 pairwise 比较来检测 LLM judge 的风格敏感性。核心发现是 "Likert Blindspot"——在相同数据上 pairwise 比较能检测到的风格偏好在 Likert 评分中消失（8/8 primary cells），并通过 GEE 条件分解揭示不同风格轴的混杂结构差异（verbosity = style-dominated, formality = quality-confounded）。实验覆盖 4 个 target judges、2 个主轴、3 个 benchmark，并用 Claude Sonnet 4 提供 discriminative validity。

---

### Strengths

**S1. GEE per-axis 分解是真正的方法论亮点。** Table 2 和 Figure 5 展示 verbosity 的 Style OR 8–13（Orig OR < 1）vs. formality 的双重显著效应，揭示了不同风格轴具有质性不同的混杂结构。这一发现对 bias mitigation 有直接实践指导意义（§5.2 最后一段明确指出了不同的应对策略），且此前未见于 LLM judge 文献。这比 "Likert Blindspot" 本身更具新颖性。

**S2. 实验控制极其全面。** 六项 amplification 控制（§5.4: NLI ablation、Claude discriminative validity、cross-axis variation、GEE artifact absorption、debiased prompting bounds、four-architecture replication）系统性地约束了 pairwise amplification 的解释力。这种控制密度在同类工作中罕见。

**S3. 统计方法论严谨。** Holm-Bonferroni FWER 控制、exploratory vs. confirmatory 分析的清晰分类（§4.1）、prospective power analysis（Figure 4, Appendix L）、bootstrap stability 验证、GEE sandwich SE——统计框架达到了高标准。特别是 n=355 scaled replication 区分 attenuation 与 insufficient power 的设计（d → -0.025 而非 non-zero）是有说服力的。

**S4. Discriminative validity 设计。** Claude Sonnet 4 在 LLMBar 上 BT ≤ 0.562 (n.s.) 的结果（Table 1）证明 CSD 不会对所有 judge 均匀膨胀偏差估计。这有效排除了"方法论 artifact 导致所有 judge 都显示 Blindspot"的担忧。

**S5. 实践意义清晰。** 论文直接指出：典型 benchmark 规模 (n=50-200) 下 Likert-only 审计系统性遗漏风格偏好，而这些偏好通过 RLHF/DPO 的 pairwise reward signal 传播到模型训练中。这对 alignment 社区有直接警示价值。

**S6. 人类标注验证。** 两名标注者评估 100 对 NLI-scored pairs（§5.4），gate pass precision 98.6%，Gwet's AC₁ = 0.96。标注者仅判断 49-66% 的 NLI-passed pairs 有可检测到的风格变化，说明观察到的效应是真实风格敏感性的稀释下界——这个发现本身具有重要含义。

---

### Weaknesses

#### Must-Fix 问题

**N1** [critical] **标题与正文的 framing 张力**
- 具体位置：Title, Abstract (第2句), §5.1 "Interpreting the divergence"
- 问题："The Likert Blindspot" 作为标题强烈暗示 Likert attenuation 是主因——Likert 有"盲点"，pairwise 看到了真相。然而正文 §5.1 明确列出三种非排他解释（attenuation, amplification, construct divergence），并承认 "six controls bound the amplification factor but cannot eliminate it"。标题的修辞倾向性与正文的审慎立场之间存在不可忽视的张力。读者的自然推断（"Likert 有问题，pairwise 更好"）与论文的实际结论（"两种格式测量不同的东西，具体机制无法完全确定"）不一致。
- 为什么影响接收：Reviewer 和读者会质疑 framing 诚实性。如果论文无法确定 attenuation 是主因，标题不应预设这一解释。
- 建议修改方向：(1) 在 Introduction 第一段更显著地承认心理测量学先驱（Thurstone 1927 已有引用，但应更明确说明 pairwise vs. rating 差异本身不新）；(2) 考虑更中性的标题如 "Measurement-Mode Divergence in LLM Judge Style Evaluation"；或 (3) 如果保留 "Likert Blindspot"，在 abstract 第一次出现时即加入 "without committing to a specific causal mechanism" 的限定（目前 abstract 第2句有此限定，但 "Blindspot" 本身的语义已预设了方向）。

**N2** [critical] **核心新颖性定位不清晰——Thurstone (1927) 以来的增量贡献**
- 具体位置：§1 Introduction 贡献列表, §2 Related Work "Measurement Format Sensitivity" 段
- 问题：Pairwise comparison 比 rating scale 有更高 discriminability 是心理测量学自 Thurstone (1927) 以来的已知结论，被 Carterette & Allan (2008) 在 IR 中确认，被 Novikova et al. (2018) 在 NLG 中确认。论文引用了这些工作（§2 第三段），但贡献声明"the first per-axis demonstration that pairwise and Likert formats yield qualitatively divergent style sensitivity profiles"过度强调了"first"——在心理测量学意义上，这种 divergence 是预期的，不是发现。
  真正的新贡献是：(a) 在 LLM judge 特有的上下文中（RLHF training 导致的 format-specific bias），这种 divergence 有质性不同的机制含义——不是人类 satisficing (Krosnick, 1999) 而是 training-induced format specificity；(b) GEE per-axis decomposition 揭示不同轴的混杂结构差异。但这两点在贡献声明中均未被突出。
- 为什么影响接收：Novelty 是顶会接收的核心标准。如果论文被认为是"已知心理测量效应的 domain transfer"而没有充分的 domain-specific insight，可能被评为 incremental。
- 建议修改方向：(1) 重新表述第一个贡献，明确为什么 LLM judge setting 与 human rater setting 有质性差异（RLHF/DPO 中 pairwise 作为 reward signal，Likert 用于 evaluation，两种格式在训练和评估中的角色不对称——这一点在 §2 最后一句提到但太简略）；(2) 将 GEE decomposition 提升为与 Likert Blindspot 并列甚至更突出的贡献。

#### Should-Fix 问题

**W1** [warning] **Rewriter-judge 重叠的处理不够显著**
- 具体位置：Table 1 脚注 b, Appendix E
- 问题：Qwen3-32B 同时作为 primary rewriter 和四个 target judges 之一。虽然 Appendix E 的 GPT-4o rewriter independence test 显示 Blindspot 仍然存在但 Style OR 降低 22%，这不是一个可以忽略的差距。Table 1 仅在脚注中提到 "independent GPT-4o rewriter yields 22% lower Style OR"，一个注意力分散的读者很容易忽略。
- 建议：在正文 §5.4 或 §4 中用 1-2 句话正式讨论 rewriter-judge overlap 及其影响范围，而不是依赖表格脚注和 appendix。

**W2** [warning] **Cross-benchmark replication 的选择性策略需要更强的辩护**
- 具体位置：§5.3 最后一段, Figure 6, Table 23 (Appendix W)
- 问题：Cross-benchmark validation 仅覆盖 6/24 possible cells（25%），且论文承认这是 "targeting the strongest effects"。这本质上是一种 cherry-picking 策略——在主要分析中发现最强效应后，选择性地在其他 benchmark 上验证这些最强效应。虽然论文的透明度值得肯定（明确声明了选择标准），但这极大地限制了 generalizability claims 的说服力。特别是，4 个 exception cells (†‡) 表明 Blindspot 的可复制性取决于 effect size，但论文对这些 exceptions 的讨论主要通过"severity spectrum"来解释，这更像是 post-hoc rationalization。
- 建议：(1) 更明确地承认选择性 replication 的局限性；(2) 考虑在 Limitations 中加入一句关于 cross-benchmark coverage 不足的声明。

**W3** [warning] **Table 1 信息密度过高，可读性受损**
- 具体位置：Table 1 (第5页)
- 问题：15 行数据 + 5 个不同标记符号 (***、*、†、†_e、†_c、---) + 3 个脚注（其中一个长达 2 行描述 direction asymmetry）。读者需要来回查阅脚注和正文才能理解各行的分类标准。Gemini 作为 "confirmatory" 和 Claude 作为 "discriminative validity" 的角色区分依赖于微小的下标符号。
- 建议：(1) 将 exploratory register 结果移到 appendix，主表保留 primary + confirmatory 结果；(2) 或将 discriminative validity (Claude) 单独列为子表。

**W4** [warning] **"Consistent pattern" 等措辞与实际数据的匹配度**
- 具体位置：§1 (第1页 "reflects a consistent pattern"), Abstract ("selectively replicated"), §5.1 ("manifests in 10/14 bias-positive cells")
- 问题：论文报告 Blindspot 出现在 10/14 bias-positive cells 中（~71%），4 个 exceptions。Claude 在 LLMBar 上两个轴均为 null。Cross-benchmark 仅 6/24 cells 被测试。"Consistent pattern" 的措辞在主文中出现，但 ~29% 的 exception rate 和 Claude 的完全 null 结果（后被重新 framed 为 "discriminative validity"）使 "consistent" 这个词的准确性可商榷。论文对 Claude 的处理很巧妙——将 null 结果转化为方法论优势——但这同时意味着该 phenomenon 是 model-specific 的，这与 "consistent" 的含义存在张力。
- 建议：在 Introduction 中用更精确的措辞替代 "consistent pattern"，如 "predominant pattern" 或 "majority pattern"，并更早地引入 model-specific variation 的概念。

**W5** [warning] **风格轴覆盖范围有限**
- 具体位置：§3.4, Limitations §3
- 问题：仅两个 primary axes（formality, verbosity）+ 一个 exploratory（register）。风格是多维的——tone、sentiment、readability、technical jargon level、hedging 等均为已知的 LLM judge 敏感维度。论文在 Limitations 中承认 "CSD applies only to surface-level axes"，但正文的 claim 措辞（"per-axis demonstration"）暗示了比实际覆盖更广的 scope。GEE decomposition 发现 formality 和 verbosity 有质性不同的混杂结构，这恰恰说明不能从两个轴外推到其他轴。
- 建议：在贡献声明中更明确限定 scope，例如 "across the two most commonly reported style axes"。

#### Minor 问题

**M1** Appendix 组织：20 页中有约 10 页 appendix（pages 11-20），包含 A-Z 共 23+ 个 section。虽然 thoroughness 值得肯定，但部分 appendix（如 Appendix O "100-Point Continuous Likert Scale"、Appendix P "NLI Gate Ablation"）的内容可以合并或精简。建议用 hierarchical 编号（A.1, A.2）替代 flat structure。

**M2** Figure 2 (DAG) 标注为 "Assumed data-generating process (design rationale, not a claim of perfect identification)"——这是好的科学实践，但 "assumed" 这个词在图题中可能暗示比实际更弱的信心。建议在正文中保留 caveat，图题简化为描述性标题。

**M3** §5.1 "Head-to-head comparison with RATE" 段直接对比 RATE 方法论，措辞 "our experiments show 60% of style-transformed pairs receive identical Likert scores" 可能被 RATE 作者解读为不公平比较，因为 RATE 的设计意图和 CSD 不同（RATE 测量 ATE，CSD 测量 BT win probability）。建议更中性地表述为方法互补而非 CSD 优于 RATE。

**M4** 论文末尾 (第20页) 的 "Use of AI Assistants" 声明提到使用 Claude (Anthropic) 进行代码、写作和文献总结。Claude Sonnet 4 同时是 discriminative validity judge。虽然这不构成利益冲突（Claude 显示 null results，如果有偏，应该偏向对 Claude 有利的结论），但建议在 Limitations 中简要提及这一双重角色。

---

### Questions（需要作者澄清）

**Q1.** 为什么不对所有分析使用完全独立的 rewriter？Appendix E 的 GPT-4o rewriter 测试显示 Style OR 下降 22%，这暗示 Qwen3-32B 的 rewriter-judge overlap 对 effect size 有非 trivial 的贡献。如果资源允许，使用独立 rewriter 重跑全部分析是否会改变主要结论？

**Q2.** Claude Sonnet 4 在 LLMBar 上显示 null results，但在 AEval verbosity 上 Style OR = 4.76 (p < .001)（§5.1 最后一段, Appendix H）。作者如何解释这一 benchmark-dependent 差异？是 LLMBar 的样本特性（100 条 instruction-response pairs）导致 power 不足，还是 Claude 确实对不同 benchmark 有不同的风格敏感性？这一模式对 "Likert Blindspot" 作为 general phenomenon 的 claim 有什么影响？

**Q3.** 论文使用 NLI entailment threshold 0.90 作为 gate（§3.2）。Appendix F 的 threshold sweep 显示 BT 在 11 个 threshold 下 stable (≤3pp variation)。但 NLI gate 的 precision 和 recall 之间的 tradeoff 是否被充分探索？更严格的 threshold（如 0.95）会如何影响 sample size 和 power？

**Q4.** Introduction 的 motivating example（"What is the average height for a male?"）中，GPT-4o 在 Likert 上给 casual version 更高分 (8 vs. 5)。这与 formality Blindspot 的整体方向一致（pairwise 选择 formal，Likert 无显著偏好）。但 Likert 反向偏好（casual 更高）是单个 example 的偶然现象还是系统性模式？如果是后者，这不是 "Blindspot"（Likert 看不到）而是 "Likert Reversal"（Likert 看到反方向），应该在叙事中更明确区分。

**Q5.** GEE decomposition 中 formality 的 Originality OR 显著（Table 2: GPT-4o Orig OR = 2.32, p = .006）意味着 style-controlled rewriting 未能完全控制原始偏好。这是 NLI gate 的局限还是 formality 与 quality 之间的固有关联？如果是后者，per-axis decomposition 能否真正实现 causal identification？

---

### Missing References

1. **IRT-based LLM judge reliability**: "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory" (arXiv:2602.00521, 2026) — 使用 Item Response Theory 分析 LLM judge reliability，与本文的 measurement methodology 讨论直接相关，提供了另一种诊断 measurement mode 差异的理论框架。

2. **Length bias in RLHF reward models**: "Mitigating Length Bias in RLHF through a Causal Lens" (arXiv:2511.12573, 2025) 和 "Bias Fitting to Mitigate Length Bias of Reward Model in RLHF" (arXiv:2505.12843, 2025) — 这两篇直接用因果方法处理 RLHF 中的 length/verbosity bias，与本文的 causal framing 和 verbosity axis 发现高度相关。

3. **Format bias in alignment**: "From Lists to Emojis: How Format Bias Affects Model Alignment" (arXiv:2409.11704, 2024) — 研究 format bias 如何影响 model alignment，与本文的 measurement-mode divergence 和 RLHF 影响讨论相关。

4. **Pairwise preference in LLM evaluators**: "Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators" (arXiv:2403.16950, 2024) — 直接研究 pairwise preference 在 LLM evaluator 中的角色，应在 Related Work §2 中被讨论。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论整体严谨，统计框架达到高标准，controls 全面。但 rewriter-judge overlap 的 22% Style OR 下降表明核心 effect size 有非 trivial 的方法论敏感性；cross-benchmark replication 的选择性策略（6/24 cells）限制了 generalizability。Title/framing 与正文三种非排他解释之间的张力影响了 claim 的准确性。 |
| **Excitement** | 3/5 | GEE per-axis decomposition 是有趣的方法论贡献，实践意义（RLHF pipeline 影响）清晰。但核心发现（pairwise > Likert in discriminability）是心理测量学已知效应的 domain transfer，novelty ceiling 受限。两个风格轴的覆盖不足以支撑更广泛的 claim。 |

### Overall Assessment

**3.5 — Borderline Conference**

本文是一篇技术执行扎实、实验控制全面的工作。GEE per-axis decomposition 提供了 LLM judge bias 文献中未见的 insight（verbosity = style-dominated vs. formality = quality-confounded），discriminative validity 设计（Claude null results）增强了方法论可信度。统计方法论达到了顶会标准。

主要顾虑集中在新颖性和 framing：(1) "Likert Blindspot" 的核心发现——pairwise 比 Likert 更敏感——是自 Thurstone (1927) 以来的已知心理测量效应，论文在 LLM judge domain 的 transfer 虽然有实践价值，但概念贡献有限；(2) 标题和叙事预设了 Likert attenuation 解释，与正文对三种非排他解释的审慎讨论不一致；(3) 两个 primary style axes + 选择性 cross-benchmark replication (6/24 cells) 的覆盖范围不足以支撑论文的 generalizability 暗示。

如果作者能 (a) 更清晰地定位 LLM judge setting 相对于经典心理测量的质性差异（RLHF training-induced format specificity），(b) 将 GEE decomposition 提升为更显著的贡献，(c) 解决 title/framing 张力，本文有潜力达到 Conference acceptance 水平。

### Confidence

**4/5** — 熟悉 LLM judge evaluation、心理测量方法论和因果推断的相关文献。仔细阅读了全文 20 页及 LaTeX 源码。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-25T21:26:17.482499+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_get_project_overview",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_get_project_overview",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-25T21:26:17.533485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1590 · 2026-05-25T21:26:28.978672+00:00_

Reviewer 2 审稿意见已收到。

**当前状态**：
- Reviewer 1（方法严谨性）：⏳ 等待中
- Reviewer 2（新颖性/完整性）：✅ 已提交（Overall: 3.5 Borderline Conference）

两名 Reviewer 的独立审稿均需到齐后才能进入 Step 2 交叉分享。等待 Reviewer 1 的意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 148

## Round 148

6 recorded events


### User

_source line 1591 · 2026-05-25T21:26:30.214578+00:00_

[Reviewer 1 审稿意见]:
## Review — Reviewer 1 (方法严谨性)

### Summary

本文定义了 "Likert Blindspot"：在相同数据上，pairwise comparison 能检测到统计显著的风格敏感性，而 Likert 评分却无法检测。作者提出 Controlled Style Decomposition (CSD) 框架，结合 NLI 门控内容验证、单轴风格改写和位置控制的 pairwise 比较，在 4 个目标 judge 和 1 个负对照 (Claude Sonnet 4) 上验证了该现象。方法设计整体严谨，robustness 检查覆盖面广，但在统计效力分析的定位、跨基准复制的选择性、以及 evaluator-producer 重叠的处理上存在需要修正的问题。

---

### Strengths

**S1. 实验设计的系统性与完备性。** 单轴干预 + NLI 门控 + 位置对消 + same-style double-rewrite 控制，形成了多层 confound 控制体系。Figure 1 清晰展示每一阶段的样本衰减（200 → 86-88 primary pairs）。

**S2. Robustness 检查覆盖面异常广泛。** 11 个 NLI 阈值 sweep (Appendix F, Table 8)、direction-aware vs. bidirectional gating 对比 (Appendix G)、rewriter 独立性测试 (Appendix E, Tables 6-7)、100-point continuous Likert scale (Appendix O)、GEE 相关结构对比 (Appendix D, Table 3)、Style × Originality 交互项检验 (Table 4)、BT 正则化敏感性 (Appendix R)。

**S3. 统计方法选择总体恰当。** BT 模型用于 pairwise 胜率估计、GEE 用于 per-axis confound 分解、sandwich SE 保证对相关结构误指定的稳健性。exchangeable 与 independence 相关结构的 QIC 对比 (|ΔQIC| < 0.001, Table 3) 充分支持模型选择。

**S4. 因果语言的审慎使用。** Section 5.2 明确声明 "two-predictor GEE provides a parsimonious decomposition rather than causal identification"；Appendix A 声明 "interventional rather than formal causal evidence"。

**S5. 负对照设计有意义。** Claude Sonnet 4 TOST + Bayesian BF₁₀ 双重验证 (Appendix H, Tables 9-10)。

**S6. Human annotation validation 设计合理。** gate-passed pairs precision 98.6% (Wilson CI [92.55, 99.95%])，正确使用 Gwet's AC₁ 处理高一致性场景。

---

### Must-Fix 问题

**N1 [critical] Power analysis 存在 post-hoc 循环论证风险**
- 位置：Section 4.1, Appendix L, Figure 4
- 正文称 "A prospective power analysis confirms that our sample sizes provide >90% power to detect BT effects of the observed magnitude"。但 effect size 来自同一批数据——这是 Hoenig and Heisey (2001)（论文自身引用）所批评的 post-hoc power 谬误。
- Appendix L 的 bootstrap attenuation 曲线（Likert d 随 n 增加趋近零）是有价值的独立论证，但不依赖于 "prospective" 定位。
- 建议：(1) 将 "prospective" 改为 "sensitivity" power analysis；(2) 重新定位为 measurement sensitivity comparison；(3) 强调 bootstrap attenuation 曲线才是关键证据。

**N2 [critical] 跨基准复制的选择性构成确认偏差**
- 位置：Section 5.3, Table 23 (Appendix W)
- 仅选取 24 cells 中效应最强的 6 个进行跨基准复制。未报告其余 18 cells 结果，读者无法评估 Blindspot 的 specificity。
- 建议：(1) 报告全部 24 cells 结果（至少在 appendix）；(2) 讨论 Blindspot 的 boundary conditions。

### Should-Fix 问题

**W1 [warning] GEE OR ~49% shrinkage (n=88→355) 讨论不足**
- 正文 Table 2 全部基于 n=88，而非更可靠的 n=355 估计。建议并列报告 scaled estimates。

**W2 [warning] Evaluator-producer overlap (Qwen3-32B) 残留膨胀**
- 更换 GPT-4o rewriter 后 Style OR 下降 22%。建议讨论对 Qwen3-32B judge 结果的校正含义。

**W3 [warning] TOST 等价界 Δ=12pp 偏宽松**
- Blindspot 效应本身仅 ~13-18pp，12pp 等价界允许 negative control 有实验效应 70-90% 大小的偏好。建议报告更严格的 Δ=5pp, 8pp 结果。

**W4 [warning] Section 3.1 "per-axis causal attribution" 与 Appendix A disclaimer 语调不一致**
- 建议替换为 "per-axis effect estimation"。

**W5 [warning] Same-style double-rewrite 在 verbosity 轴暴露 rewriting artifact (BT P(orig)=0.082)**
- 改写过程本身为 verbose 文本引入了质量提升，可能膨胀 verbosity Blindspot。

### Minor
- M1: BT 正则化参数 Section 4.1 (α=10⁻⁴) vs Appendix R (α=10⁻⁷) 不一致
- M2: GEE ρ∈[−0.25,+0.11]，ρ=−0.25 非 "near-zero"
- M3: Table 1 adjusted p-values 的校正方法未说明
- M4: Figure 4 y轴 "at observed effect magnitudes" 强化 post-hoc 印象

### Questions
- Q1: Power analysis effect size 是否有 pilot/先验来源？
- Q2: 未测试的 18 cells 是否有结果可报告？
- Q3: Verbosity same-style rewrite artifact 在 GEE Originality OR 中被吸收了多少？
- Q4: BT 正则化参数实际用的是 10⁻⁴ 还是 10⁻⁷？
- Q5: n=355 GEE 估计可否并列报告？

### Scores
| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 3.5/5 |
| Reproducibility | 4/5 |
| **Overall Assessment** | **3.5** (Borderline Conference) |
| **Confidence** | **4/5** |

核心发现有原创性和实用价值，实验设计系统性属上乘。但 post-hoc power 定位不当、cross-benchmark 选择性复制、~49% OR shrinkage、evaluator-producer overlap 残留膨胀等问题累积起来使定量 claim 可信度低于论文呈现水平。修正 N1-N2 并加强 W1-W5 讨论后可达 Conference 接收水平。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心评判：**Overall 3.5（Borderline Conference）**。

主要发现：
- **两个 Must-Fix**：(1) 标题 "Likert Blindspot" 预设了 attenuation 解释，与正文三种非排他解释的审慎立场存在张力；(2) 核心新颖性定位不清——pairwise > Likert 是 Thurstone (1927) 以来的已知效应，论文需要更明确地阐述 LLM judge setting 的质性差异（RLHF format specificity）。
- **GEE per-axis decomposition** 是本文真正最强的贡献（verbosity = style-dominated vs. formality = quality-confounded），但在叙事中被 "Likert Blindspot" 遮蔽。
- **四个 Should-Fix**：rewriter-judge overlap 处理不够显著、cross-benchmark replication 选择性、Table 1 可读性、"consistent pattern" 措辞与 ~29% exception rate 的匹配。
- 建议补充 4 篇 missing references（IRT-based reliability、causal length bias in RLHF、format bias in alignment、pairwise preference in LLM evaluators）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-25T21:27:12.957335+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性/完整性侧重）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注 Reviewer 2 提出的你可能遗漏的问题，以及你们之间可能存在的分歧。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Summary**: 本文提出 CSD，一种 black-box 诊断框架，通过 NLI 门控内容保持、单轴风格重写和位置控制的 pairwise 比较来检测 LLM judge 的风格敏感性。核心发现是 \"Likert Blindspot\"——在相同数据上 pairwise 比较能检测到的风格偏好在 Likert 评分中消失（8/8 primary cells），并通过 GEE 条件分解揭示不同风格轴的混杂结构差异。\n\n**Strengths**:\n- S1: GEE per-axis 分解是真正的方法论亮点（verbosity Style OR 8-13 vs formality 双重显著）\n- S2: 实验控制极其全面（六项 amplification 控制）\n- S3: 统计方法论严谨（Holm-Bonferroni, exploratory vs confirmatory 分类, power analysis）\n- S4: Discriminative validity 设计（Claude null results 排除方法论 artifact）\n- S5: 实践意义清晰（RLHF/DPO pipeline 影响）\n- S6: 人类标注验证（100 pairs, AC₁=0.96, gate precision 98.6%）\n\n**Must-Fix**:\n- **N1 [critical]**: 标题 \"The Likert Blindspot\" 预设 Likert attenuation 解释，与正文 §5.1 三种非排他解释的审慎立场存在张力。读者自然推断\"Likert 有问题，pairwise 更好\"与论文实际结论不一致。建议更中性标题或在 abstract 更早 qualify。\n- **N2 [critical]**: 核心新颖性定位不清——pairwise > Likert discriminability 是 Thurstone (1927) 以来已知效应。论文需更明确阐述 LLM judge setting 的质性差异（RLHF training-induced format specificity）。真正的新贡献（GEE per-axis decomposition）在叙事中被 \"Likert Blindspot\" 遮蔽。\n\n**Should-Fix**:\n- **W1**: Rewriter-judge overlap（Qwen3-32B）处理不够显著——22% Style OR 下降仅在脚注和 appendix 讨论\n- **W2**: Cross-benchmark replication 选择性（6/24 cells 选最强效应）需更强辩护\n- **W3**: Table 1 信息密度过高（15 行 + 5 种标记 + 3 个脚注）\n- **W4**: \"Consistent pattern\" 措辞与 ~29% exception rate + Claude null 结果有张力\n- **W5**: 仅两个 primary axes 覆盖不足以支撑更广 claim\n\n**Minor**: M1 Appendix 组织过于 flat; M2 Figure 2 DAG \"assumed\" 措辞; M3 §5.1 RATE 比较措辞; M4 Claude 双重角色（AI assistant + discriminative validity judge）\n\n**Questions**:\n- Q1: 为何不全部使用独立 rewriter？\n- Q2: Claude benchmark-dependent 差异（LLMBar null vs AEval verbosity OR=4.76）如何解释？\n- Q3: NLI threshold precision-recall tradeoff 是否充分探索？\n- Q4: Intro motivating example 的 Likert 反向偏好是偶然还是系统性？\n- Q5: Formality Orig OR 显著意味着什么？\n\n**Missing References**: IRT-based LLM judge reliability (arXiv:2602.00521); Length bias in RLHF (arXiv:2511.12573, 2505.12843); Format bias in alignment (arXiv:2409.11704); Pairwise preference in LLM evaluators (arXiv:2403.16950)\n\n**Scores**: Soundness 3.5/5, Excitement 3/5, Overall 3.5 (Borderline Conference), Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性/完整性侧重）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注 Reviewer 2 提出的你可能遗漏的问题，以及你们之间可能存在的分歧。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Summary**: 本文提出 CSD，一种 black-box 诊断框架，通过 NLI 门控内容保持、单轴风格重写和位置控制的 pairwise 比较来检测 LLM judge 的风格敏感性。核心发现是 \"Likert Blindspot\"——在相同数据上 pairwise 比较能检测到的风格偏好在 Likert 评分中消失（8/8 primary cells），并通过 GEE 条件分解揭示不同风格轴的混杂结构差异。\n\n**Strengths**:\n- S1: GEE per-axis 分解是真正的方法论亮点（verbosity Style OR 8-13 vs formality 双重显著）\n- S2: 实验控制极其全面（六项 amplification 控制）\n- S3: 统计方法论严谨（Holm-Bonferroni, exploratory vs confirmatory 分类, power analysis）\n- S4: Discriminative validity 设计（Claude null results 排除方法论 artifact）\n- S5: 实践意义清晰（RLHF/DPO pipeline 影响）\n- S6: 人类标注验证（100 pairs, AC₁=0.96, gate precision 98.6%）\n\n**Must-Fix**:\n- **N1 [critical]**: 标题 \"The Likert Blindspot\" 预设 Likert attenuation 解释，与正文 §5.1 三种非排他解释的审慎立场存在张力。读者自然推断\"Likert 有问题，pairwise 更好\"与论文实际结论不一致。建议更中性标题或在 abstract 更早 qualify。\n- **N2 [critical]**: 核心新颖性定位不清——pairwise > Likert discriminability 是 Thurstone (1927) 以来已知效应。论文需更明确阐述 LLM judge setting 的质性差异（RLHF training-induced format specificity）。真正的新贡献（GEE per-axis decomposition）在叙事中被 \"Likert Blindspot\" 遮蔽。\n\n**Should-Fix**:\n- **W1**: Rewriter-judge overlap（Qwen3-32B）处理不够显著——22% Style OR 下降仅在脚注和 appendix 讨论\n- **W2**: Cross-benchmark replication 选择性（6/24 cells 选最强效应）需更强辩护\n- **W3**: Table 1 信息密度过高（15 行 + 5 种标记 + 3 个脚注）\n- **W4**: \"Consistent pattern\" 措辞与 ~29% exception rate + Claude null 结果有张力\n- **W5**: 仅两个 primary axes 覆盖不足以支撑更广 claim\n\n**Minor**: M1 Appendix 组织过于 flat; M2 Figure 2 DAG \"assumed\" 措辞; M3 §5.1 RATE 比较措辞; M4 Claude 双重角色（AI assistant + discriminative validity judge）\n\n**Questions**:\n- Q1: 为何不全部使用独立 rewriter？\n- Q2: Claude benchmark-dependent 差异（LLMBar null vs AEval verbosity OR=4.76）如何解释？\n- Q3: NLI threshold precision-recall tradeoff 是否充分探索？\n- Q4: Intro motivating example 的 Likert 反向偏好是偶然还是系统性？\n- Q5: Formality Orig OR 显著意味着什么？\n\n**Missing References**: IRT-based LLM judge reliability (arXiv:2602.00521); Length bias in RLHF (arXiv:2511.12573, 2505.12843); Format bias in alignment (arXiv:2409.11704); Pairwise preference in LLM evaluators (arXiv:2403.16950)\n\n**Scores**: Soundness 3.5/5, Excitement 3/5, Overall 3.5 (Borderline Conference), Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-25T21:27:34.346356+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21389
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-25T21:27:34.497266+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_style_decomp_judge",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性侧重）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注 Reviewer 1 提出的你可能遗漏的问题，以及你们之间可能存在的分歧。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Summary**: 本文定义了 \"Likert Blindspot\"：在相同数据上，pairwise comparison 能检测到统计显著的风格敏感性，而 Likert 评分却无法检测。作者提出 CSD 框架，在 4 个目标 judge 和 1 个负对照 (Claude) 上验证了该现象。方法设计整体严谨，robustness 检查覆盖面广，但在统计效力分析的定位、跨基准复制的选择性、以及 evaluator-producer 重叠的处理上存在需修正的问题。\n\n**Strengths**:\n- S1: 实验设计的系统性与完备性（单轴干预 + NLI 门控 + 位置对消 + double-rewrite 控制）\n- S2: Robustness 检查覆盖面异常广泛（11 个 NLI 阈值 sweep, direction-aware gating, rewriter independence, 100-point Likert, GEE 相关结构对比, interaction test, BT 正则化）\n- S3: 统计方法选择总体恰当（BT + GEE + sandwich SE）\n- S4: 因果语言的审慎使用（§5.2 和 Appendix A 的 disclaimer）\n- S5: 负对照设计有意义（Claude TOST + Bayesian BF₁₀）\n- S6: Human annotation validation 设计合理（AC₁ = 0.96）\n\n**Must-Fix**:\n- **N1 [critical]**: Power analysis 存在 post-hoc 循环论证风险。正文称 \"prospective power analysis\" 但 effect size 来自同一批数据——Hoenig & Heisey (2001)（论文自身引用）所批评的谬误。建议改为 \"sensitivity power analysis\"。\n- **N2 [critical]**: 跨基准复制选择性构成确认偏差——仅选 24 cells 中效应最强的 6 个，未报告其余 18 cells。\n\n**Should-Fix**:\n- **W1**: GEE OR ~49% shrinkage (n=88→355) 讨论不足，Table 2 全部基于 n=88\n- **W2**: Evaluator-producer overlap (Qwen3-32B) 残留 22% 膨胀\n- **W3**: TOST 等价界 Δ=12pp 偏宽松——Blindspot 效应本身仅 ~13-18pp\n- **W4**: Section 3.1 \"per-axis causal attribution\" 与 Appendix A disclaimer 语调不一致\n- **W5**: Same-style double-rewrite 在 verbosity 轴暴露 rewriting artifact (BT P(orig)=0.082)\n\n**Minor**:\n- M1: BT 正则化参数 §4.1 (α=10⁻⁴) vs Appendix R (α=10⁻⁷) 不一致\n- M2: GEE ρ∈[−0.25,+0.11]，ρ=−0.25 非 \"near-zero\"\n- M3: Table 1 adjusted p-values 校正方法未说明\n- M4: Figure 4 y轴 \"at observed effect magnitudes\" 强化 post-hoc 印象\n\n**Questions**:\n- Q1: Power analysis effect size 有 pilot/先验来源？\n- Q2: 未测试的 18 cells 有结果可报告？\n- Q3: Verbosity same-style rewrite artifact 在 GEE Orig OR 中被吸收多少？\n- Q4: BT 正则化参数实际用的是哪个？\n- Q5: n=355 GEE 估计可否并列报告？\n\n**Scores**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.5 (Borderline Conference), Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_style_decomp_judge",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性侧重）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注 Reviewer 1 提出的你可能遗漏的问题，以及你们之间可能存在的分歧。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Summary**: 本文定义了 \"Likert Blindspot\"：在相同数据上，pairwise comparison 能检测到统计显著的风格敏感性，而 Likert 评分却无法检测。作者提出 CSD 框架，在 4 个目标 judge 和 1 个负对照 (Claude) 上验证了该现象。方法设计整体严谨，robustness 检查覆盖面广，但在统计效力分析的定位、跨基准复制的选择性、以及 evaluator-producer 重叠的处理上存在需修正的问题。\n\n**Strengths**:\n- S1: 实验设计的系统性与完备性（单轴干预 + NLI 门控 + 位置对消 + double-rewrite 控制）\n- S2: Robustness 检查覆盖面异常广泛（11 个 NLI 阈值 sweep, direction-aware gating, rewriter independence, 100-point Likert, GEE 相关结构对比, interaction test, BT 正则化）\n- S3: 统计方法选择总体恰当（BT + GEE + sandwich SE）\n- S4: 因果语言的审慎使用（§5.2 和 Appendix A 的 disclaimer）\n- S5: 负对照设计有意义（Claude TOST + Bayesian BF₁₀）\n- S6: Human annotation validation 设计合理（AC₁ = 0.96）\n\n**Must-Fix**:\n- **N1 [critical]**: Power analysis 存在 post-hoc 循环论证风险。正文称 \"prospective power analysis\" 但 effect size 来自同一批数据——Hoenig & Heisey (2001)（论文自身引用）所批评的谬误。建议改为 \"sensitivity power analysis\"。\n- **N2 [critical]**: 跨基准复制选择性构成确认偏差——仅选 24 cells 中效应最强的 6 个，未报告其余 18 cells。\n\n**Should-Fix**:\n- **W1**: GEE OR ~49% shrinkage (n=88→355) 讨论不足，Table 2 全部基于 n=88\n- **W2**: Evaluator-producer overlap (Qwen3-32B) 残留 22% 膨胀\n- **W3**: TOST 等价界 Δ=12pp 偏宽松——Blindspot 效应本身仅 ~13-18pp\n- **W4**: Section 3.1 \"per-axis causal attribution\" 与 Appendix A disclaimer 语调不一致\n- **W5**: Same-style double-rewrite 在 verbosity 轴暴露 rewriting artifact (BT P(orig)=0.082)\n\n**Minor**:\n- M1: BT 正则化参数 §4.1 (α=10⁻⁴) vs Appendix R (α=10⁻⁷) 不一致\n- M2: GEE ρ∈[−0.25,+0.11]，ρ=−0.25 非 \"near-zero\"\n- M3: Table 1 adjusted p-values 校正方法未说明\n- M4: Figure 4 y轴 \"at observed effect magnitudes\" 强化 post-hoc 印象\n\n**Questions**:\n- Q1: Power analysis effect size 有 pilot/先验来源？\n- Q2: 未测试的 18 cells 有结果可报告？\n- Q3: Verbosity same-style rewrite artifact 在 GEE Orig OR 中被吸收多少？\n- Q4: BT 正则化参数实际用的是哪个？\n- Q5: n=355 GEE 估计可否并列报告？\n\n**Scores**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.5 (Borderline Conference), Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1595 · 2026-05-25T21:27:35.756223+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1258
}
```

</details>

---


### Assistant

_source line 1596 · 2026-05-25T21:27:40.609498+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 149

## Round 149

2 recorded events


### User

_source line 1597 · 2026-05-25T21:27:43.150714+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1598 · 2026-05-25T21:27:48.809588+00:00_

[WAIT 2m] 等待 Reviewer 1 交叉回应返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 150

## Round 150

2 recorded events


### User

_source line 1599 · 2026-05-25T21:31:26.752867+00:00_

[Reviewer 1 审稿意见]:
## 交叉回应 — Reviewer 1 对 Reviewer 2

### 总体评估
R1 与 R2 在 Soundness (3.5) 和 Overall (3.5) 上完全一致。核心分歧在于两个问题的严重性评级：

1. **Cross-benchmark selectivity**: R2 列为 Should-Fix (W2)，我列为 Must-Fix (N2)。我维持 Must-Fix——6/24 cells 的选择性复制对 generalizability claim 构成系统性威胁。
2. **Novelty positioning**: R2 列为 Must-Fix (N2)，我认为应降级为 Should-Fix。Per-axis decomposition 的实证发现超出了 Thurstone (1927) 的一般原理。

### 逐条回应

**[AGREE] R2-N1 (标题预设解释)**: "Blindspot" 隐含 Likert 有缺陷，与 §5.1 三种非排他解释不一致。

**[REBUT] R2-N2 (新颖性)**: 部分不同意 Must-Fix 评级。Per-axis confound structure 差异 (Table 2: verbosity style-dominated vs formality dual-confounded) 是此前文献未报告的实质性发现，不仅是已知效应的重新验证。建议降级为 Should-Fix。

**[AGREE] R2-W1 (Rewriter overlap)**: 与我的 W2 一致。

**[AGREE] R2-W2 (Cross-benchmark selectivity)**: 同意但认为应升级为 Must-Fix，与我的 N2 一致。

**[AGREE] R2-W3 (Table 1 density)**: 次要 presentation 问题。

**[AGREE] R2-W4 ("Consistent pattern" 措辞)**: 同意需要 qualification。补充发现：Appendix X Table 24 显示 Claude 在 AEval verbosity 上有 genuine style sensitivity (Style OR=4.76, p<.001)，进一步削弱 "consistent" 表述和 negative control 论证。

**[REBUT] R2-W5 (两个 primary axes 不足)**: 部分不同意。两轴已揭示结构性差异（verbosity vs formality confound patterns），非同质重复。但应在 Limitations 中明确列为限制。

**[AGREE] R2-Q2 (Claude benchmark-dependent 差异)**: 这是 R2 发现的我遗漏的重要问题。Claude 在 AEval verbosity 上 Style OR=4.76 (p<.001) 意味着它并非 universally style-insensitive。论文 §5.4 的 TOST 仅基于 LLMBar 数据，如果扩展到 AEval，Claude 不再满足等价条件。建议将 Claude 重新定位为 "partial negative control"。

**[REBUT] R2-Q3 (NLI threshold exploration)**: 11-threshold sweep + direction-aware 对比已充分。

### 我的新增 concern（受 R2 启发）
- 我原先的 W3 (TOST 等价界宽松) 需要升级：问题不仅是界值宽松，更是 negative control (Claude) 本身在 AEval verbosity 上不 null。这使整个 discriminative validity 论证需要重新框定。

### 最终评分维持不变
Soundness 3.5, Overall 3.5, Confidence 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1600 · 2026-05-25T21:32:05.844440+00:00_

收到 Reviewer 1 的交叉回应。

**R1 交叉回应要点摘要：**

| 条目 | R1 立场 | 说明 |
|------|---------|------|
| R2-N1 标题预设 | AGREE | — |
| R2-N2 新颖性 Must-Fix | REBUT → 建议降为 Should-Fix | Per-axis confound 差异是新发现 |
| R2-W1 Rewriter overlap | AGREE | — |
| R2-W2 Cross-benchmark | AGREE + 升级 | 认为应为 Must-Fix |
| R2-W3 Table 1 density | AGREE | — |
| R2-W4 "Consistent" 措辞 | AGREE + 补充 | Claude AEval verbosity Style OR=4.76 削弱 negative control |
| R2-W5 两轴不足 | REBUT（部分） | 两轴已显结构差异，但应列为 limitation |
| R2-Q2 Claude benchmark差异 | AGREE | 遗漏点，接受 |
| R2-Q3 NLI threshold | REBUT | 11-threshold sweep 已足够 |

**新增 concern**：Claude 在 AEval verbosity 上不满足 null 条件，discriminative validity 论证需重框定。

**评分维持**：Soundness 3.5, Overall 3.5, Confidence 4

---

等待 Reviewer 2 的交叉回应，收齐后判断收敛并合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 151

## Round 151

22 recorded events


### User

_source line 1601 · 2026-05-25T21:32:06.855649+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 与 R2 在总分 (3.5) 和主要 concern 上高度一致，分歧仅在两个问题的严重性评级上。R2 的 Q2（Claude benchmark-dependent sensitivity）是我遗漏的重要发现，已纳入补充评估。

---

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见

---

### Strengths 回应

R1 的 S1-S6 与我的评估高度一致。特别是 S2（robustness 检查覆盖面）和 S4（因果语言的审慎使用）是我也重点肯定的方面。我在 S6（人类标注验证）的基础上额外注意到标注者仅判定 49-66% 的 NLI-passed pairs 有可检测的风格变化（§5.4），这意味着观察到的效应是真实敏感性的稀释下界——R1 没有提及这一点，但我认为它增强了论文的可信度。

---

### Must-Fix 回应

**[AGREE] R1-N1: Power analysis 的 "prospective" 标签存在循环论证风险**

同意 R1 的核心判断。§4.1 称 "A prospective power analysis (Appendix L) confirms that our sample sizes (n = 86–88 pairs) provide >90% power to detect BT effects of the observed magnitude (P ≥ 0.63)"——使用同一数据集的 observed effect size 计算 power，这正是 Hoenig & Heisey (2001) 所批评的 post-hoc power fallacy。论文在 Figure 4 caption 中加了括号 disclaimer "(not post-hoc power; cf. Hoenig & Heisey, 2001)"，但用法与该引用的核心论点矛盾。

补充：论文的实质分析（"Likert 需要 4-206× 的样本量才能达到同等 power"）作为 sensitivity analysis 仍有信息价值，但 "prospective" 标签不当。R1 建议改为 "sensitivity power analysis" 是准确的修改方向。Figure 4 的 y 轴标签 "at observed effect magnitudes" 进一步固化了 post-hoc 印象（与 R1-M4 一致）。

**[AGREE] R1-N2: 跨基准复制的选择性构成确认偏差**

强烈同意，这也是我的 W2。仅测试 24 cells 中效应最强的 6 个（25%），且论文明确称 "targeting the strongest effects"（§5.3 最后一段）。虽然透明度值得肯定，但策略本身是 cherry-picking 的一种形式。更关键的是：4 个 exception cells (‡) 的存在表明 Blindspot 的可复制性是 effect-size dependent 的，但论文用 "severity spectrum" 来解释这些 exceptions，这更接近 post-hoc rationalization 而非预先注册的分析框架。

我额外注意到 R1 未提及的一点：未测试的 18 cells 可能包含反例（Likert 检测到而 pairwise 未检测到的情况），这将直接挑战 "Likert Blindspot" 的单向性叙事。R1 的 Q2（要求报告 18 cells 结果）因此尤为重要。

---

### Should-Fix 回应

**[AGREE] R1-W1: GEE OR shrinkage 讨论不足**

同意。Table 2 全部基于 n=88，而 n=355 的 scaled replication 显示 49-72% shrinkage（§5.2: Qwen3-32B formality Style OR 4.20 → 2.15）。虽然 Table 2 caption 提到了 shrinkage 范围，且 Appendix 有 n=355 数据，但主表的视觉印象仍以膨胀的 n=88 估计为主。R1 建议并列报告 n=88 和 n=355 估计（Q5）是合理的。

补充：shrinkage 后 n=355 的 Style OR 仍显著（GPT-4o: 2.58, p=.002; Qwen3-32B: 2.15, p<.0001），说明核心结论不变，但 effect magnitude 的报告确实需要校正。

**[AGREE] R1-W2: Evaluator-producer overlap 残留 22% 膨胀**

同意，这也是我的 W1。Appendix E（Table 5-6）显示 GPT-4o 独立 rewriter 使 Style OR 从 13.10 降至 10.17（-22%），Blindspot 仍然存在但 effect size 缩减是 non-trivial 的。论文仅在 Table 1 脚注 b 中提及 "independent GPT-4o rewriter yields 22% lower Style OR"，正文 §5.4 未显著讨论。

**[AGREE] R1-W3: TOST 等价界 Δ=12pp 偏宽松——我的审稿遗漏了这一问题**

这是 R1 提出的、我完全遗漏的一个尖锐观察。Appendix H（Table 9）显示 Claude pooled TOST 在 Δ=12pp 时 p=.035，在 Δ=10pp 时 p=.100（不显著）。而 Blindspot 效应本身对最弱的 target judge（GPT-4o formality BT=63.0%）仅为 13pp。这意味着 TOST 的等价界几乎与最小的正效应重合——TOST 无法区分 "Claude 真的无偏" 和 "Claude 的偏差略低于检测阈值"。论文称 "Δ=12pp corresponds to a small effect (Cohen's h=0.24)"（Appendix H），但 Cohen's h 的解释在 BT probability 空间中的 substantive 含义未被讨论。

建议作者：(1) 报告多个 Δ 的 TOST 结果（已做到，Table 9）；(2) 在正文中明确承认 Δ=12pp bound 的局限性，而不仅是在 appendix 中。

**[AGREE] R1-W4: §3.1 "per-axis causal attribution" 与 Appendix A disclaimer 的语调不一致**

同意。Appendix A 明确声明 "Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure 2 is a complete structural causal model"（Appendix A, line 12），但 §3.1 的正文描述（"a single-axis intervention design that enables per-axis causal attribution"）使用了更强的因果语言。这种前后不一致会让 reviewer 质疑论文的 claim 边界。

**[AGREE] R1-W5: Verbosity same-style double-rewrite 暴露严重 rewriting artifact——我的审稿遗漏了这一问题**

R1 指出 BT P(orig)=0.082（Qwen3 verbosity，Table 19, Appendix O），意味着 judge 在 91.8% 的情况下偏好 LLM-polished 版本，即使风格没有改变。这是一个非常严重的 confound。论文声称这被 GEE 的 Originality term 吸收（§5.4: "Same-style double-rewrite controls confirm that any residual rewriting artifact is absorbed by the GEE originality term"），但 GEE verbosity 的 Orig OR=0.49 (n.s.) 表明吸收可能不完全——Orig OR 虽然不显著，但方向（<1，偏好 rewrite）与 same-style artifact 一致。

R1 的 Q3（artifact 在 GEE Orig OR 中被吸收多少）是关键问题。如果 same-style rewrite artifact 的幅度（BT P=0.082，即强烈偏好 rewrite）远大于 GEE 能吸收的量，那么 verbosity 的 Style OR=13.10 可能仍包含未被控制的 polishing artifact。

---

### Minor 回应

**[REBUT] R1-M1: BT 正则化参数不一致（§4.1 α=10⁻⁴ vs Appendix R α=10⁻⁷）**

经核查 LaTeX 源码，§4.1（experiments.tex line 12）写的是 $\alpha = 10^{-6}$，Appendix P Implementation Details（appendix.tex line 555）同样写的是 "default L2 regularization α = 10⁻⁶; varying α from 10⁻⁶ to 1.0 changes all BT probabilities by <0.002"。两处均为 10⁻⁶，不存在 R1 所述的 10⁻⁴ 与 10⁻⁷ 的不一致。R1 可能因 PDF 渲染中上标数字辨识困难而误读。此外，论文报告了 α 从 10⁻⁶ 到 1.0 的 sensitivity analysis（BT 变化 <0.002），说明正则化选择对结果无实质影响。

**[AGREE] R1-M2: GEE ρ=−0.25 不是 "near-zero"**

同意。§4.1 称 "near-zero estimated within-pair correlations (α̂ ∈ [−0.25, +0.11])"，但 ρ=−0.25 不符合 "near-zero" 的通常标准（通常 |ρ| < 0.1）。不过，Table 3（Appendix C）的 correlation structure robustness test 显示 exchangeable 与 independence 结构的 ΔQIC < 0.001，max coefficient change < 0.02，说明即使 ρ 不是 near-zero，结论对 correlation structure 的选择是 robust 的。建议将 "near-zero" 改为更准确的描述如 "small in magnitude"。

**[REBUT] R1-M3: Table 1 adjusted p-values 校正方法未说明**

§4.1 第1句明确写道 "The primary family comprises six tests (three target judges × two axes), corrected via Holm-Bonferroni at α = 0.05"（experiments.tex line 8），Table 1 脚注也标注 "Holm-adj. for primary"。校正方法已说明。但我同意 R1 的隐含关切：Table 1 未直接呈现 raw 和 adjusted p-values 的对照，尽管 §4.1 声称 "Table 1 reports both raw and adjusted p-values"。实际上 Table 1 的 BT 列只显示 significance markers (***、*)，Likert 列显示 d(p) 中的 raw p-value。adjusted p-values 的具体数值不可见。

**[AGREE] R1-M4: Figure 4 y 轴 "at observed effect magnitudes" 强化 post-hoc 印象**

同意，与 N1 一致。

---

### Questions 回应

**R1-Q1 (Power analysis effect size 有 pilot/先验来源？)**：关键问题。如果没有独立先验，"prospective" 标签不成立。论文应在 revision 中明确说明。

**R1-Q2 (未测试的 18 cells 有结果？)**：我认为这是最重要的问题。如果 18 cells 中有反例（Likert 检测到但 pairwise 未检测到），"Blindspot" 的单向性叙事将被严重削弱。

**R1-Q3 (Verbosity same-style artifact 被 GEE Orig OR 吸收多少？)**：如上述 W5 分析，这是一个需要定量回答的核心问题。建议作者提供 same-style BT artifact 与 GEE Orig OR 的直接比较。

**R1-Q4 (BT 正则化参数？)**：如 M1 回应所述，两处均为 10⁻⁶，不存在不一致。

**R1-Q5 (n=355 GEE 估计并列报告？)**：支持。Table 2 应并列报告 n=88 和 n=355 估计以避免小样本膨胀的误导。

---

### 评分差异分析

R1 和我的评分高度一致（Soundness 3.5, Overall 3.5），唯一显著差异在 **Excitement**（R1: 3.5, 我: 3.0）。

我给 Excitement 3.0 的主要原因是：Pairwise vs. Likert discriminability 差异是自 Thurstone (1927) 以来的已知心理测量效应，本文的 domain transfer 到 LLM judge 虽然有实践价值，但概念新颖性有限。R1 未在其审稿中明确讨论这一心理测量学先驱问题，这可能是评分差异的来源。

此外，我提出了两个 R1 未涉及的 Must-Fix 问题：
1. **标题/framing 张力**（我的 N1）："The Likert Blindspot" 预设了 Likert attenuation 解释，与正文三种非排他解释存在矛盾。R1 未将此标记为问题。
2. **Novelty 定位不清晰**（我的 N2）：贡献声明 "the first per-axis demonstration" 的 "first" 在心理测量学背景下被过度强调。

建议 Director 关注这两个额外的 framing/novelty 问题——它们可能在 AC 层面影响接收决定，即使技术执行扎实。

---

### 我遗漏的问题（感谢 R1 发现）

1. **W3 (TOST Δ=12pp)**：R1 指出 TOST bound 几乎与最小正效应重合，这使 Claude discriminative validity 的说服力大打折扣。我在初审中完全遗漏了这一点。
2. **W5 (Verbosity same-style artifact BT P(orig)=0.082)**：91.8% 的 rewrite 偏好是一个定量上非常严重的 confound。我在初审中提到了 rewriter-judge overlap 但未检查 same-style artifact 的具体幅度。
3. **M2 (ρ=-0.25 不是 near-zero)**：有效的文本准确性问题，我遗漏了。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：与 R1 在 12/16 个具体问题上达成一致（10 个 AGREE，2 个 REBUT）。REBUT 的两点是：(1) M1 的 BT 正则化参数不一致——经核查 LaTeX 源码两处均为 10⁻⁶，R1 可能误读 PDF；(2) M3 的校正方法确实已在 §4.1 和 Table 1 脚注中说明。R1 提出了三个我初审遗漏的问题（TOST Δ=12pp 过宽、verbosity same-style artifact BT P(orig)=0.082、GEE ρ=-0.25 非 near-zero），均已确认并纳入。我提出了两个 R1 未涉及的额外问题：标题/framing 张力和 Thurstone 以来的 novelty 定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-25T21:32:28.404503+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:submit_review_report_to_research_director,update_review_issues,get_visual_check_status,get_external_review_status,read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:submit_review_report_to_research_director,update_review_issues,get_visual_check_status,get_external_review_status,read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-25T21:32:28.455110+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-25T21:32:32.220489+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-25T21:32:32.321443+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-25T21:32:36.890368+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1607 · 2026-05-25T21:32:37.041349+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:17:23.833051+00:00\", \"completed_at\": \"2026-05-25T21:17:27.436175+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 6pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-25T21:32:37.091923+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-25T21:32:37.142639+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-25T21:32:40.555139+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1611 · 2026-05-25T21:32:40.655936+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-25T21:32:45.224525+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-25T21:32:45.275219+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-25T21:32:48.688489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-25T21:32:48.990460+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved)
4	  # ============================================================
5	
6	  - id: "R1-N1"
7	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
8	    category: framing
9	    severity: critical
10	    status: resolved
11	    first_raised_round: 1
12	    last_seen_round: 5
13	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
14	    resolution_round: 4
15	
16	  - id: "R2-N1"
17	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
18	    category: framing
19	    severity: warning
20	    status: in_progress
21	    first_raised_round: 1
22	    last_seen_round: 18
23	    resolution: null
24	    resolution_round: null
25	    mentions:
26	      - round: 3
27	        reviewers: [1, 2]
28	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
29	      - round: 8
30	        reviewers: [1, 2]
31	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
32	      - round: 9
33	        reviewers: [1, 2]
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 Must-Fix N2 (critical)，R1 Excitement 3.5/5。"
44	      - round: 13
45	        reviewers: [1, 2]
46	        note: "R13 fresh review: R2 Must-Fix (N2)。R1 REBUT——GEE 分解是增量贡献。"
47	      - round: 14
48	        reviewers: [1, 2]
49	        note: "R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。"
50	      - round: 15
51	        reviewers: [1, 2]
52	        note: "R15 fresh review: 两位再次独立提出。"
53	      - round: 16
54	        reviewers: [1, 2]
55	        note: "R16: S4 称 GEE decomposition 是'真正的方法论
…[truncated 33764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-25T21:33:24.730223+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-25T21:33:24.780948+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifac
…[truncated 29 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---
