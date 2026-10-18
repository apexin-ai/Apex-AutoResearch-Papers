# Director coordination — Part 5 of 7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/9d/9db2d5c10f518e51ec86.json)

## Round 101

### Tool call

_source line 1062 · 2026-05-22T19:54:57.184628+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是'真正增量贡献'与 novelty 不足判断矛盾。Director 降为 Should-Fix。持续分歧点。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"§1 增加一句明确承认心理测量学先例；限定为 'first controlled quantification + per-axis decomposition for LLM judges specifically'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 13\n    resolution: \"Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。\"\n    resolution_round: 7\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 格式合规：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind ✓。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 格式合规：正文 ≤8 页 ✓，double-blind ✓，Limitations 合规 ✓。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2: register 轴所有改写用 Qwen3-32B 且无跨改写器验证，BT 结果也较弱。建议降级为 exploratory pilot axis。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W2) register 轴 evaluator-producer overlap 最严重，建议标注。R1 部分 AGREE——register 主结果来自其他 judge（GPT-4o, Llama-70B），核心 claim 建在 verbosity/formality 上。Director 列为 Minor。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"Limitations 补一句：effect-size precision varies ±22% with rewriter choice\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix。R2 交叉降为 Should-Fix。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W2: 50 对由 2 名标注员评估，κ=0.44 (moderate)，4 个分歧全在 verbosity condensation 上。Wilson CI 过宽。建议增加标注量。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W1)，R2 AGREE。50 对 κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。Annotator 2 precision 84.3% (CI 65.3-93.6%)。两位一致建议 ≥100 对 + 第 3 标注员。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"增加至 ≥100 对 + 第 3 名标注员 + 分析分歧案例特征分布\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 M1: Abstract 数字密度过高。与往轮一致。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W3) 再次提出数字密度过高。R1 REBUT——实证论文 Abstract 需要定量具体性，ARR 无限制。Director 列为 Minor 偏好建议。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix——Appendix B direction asymmetry 暗示 IIA 违反。R2 交叉 [REBUT]——binary-choice BT 中 IIA 自动满足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 脚注 3：binary-choice BT 中 IIA structurally satisfied 的声明正确，方向异质性是 heterogeneous treatment effects 而非 IIA violation。\"\n      - round: 13\n        reviewers: [1]\n        note: \"R13 R1 Minor (M3)：脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。R2 AGREE。Director 列为 Minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。6 项 controls + Claude 负对照已部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 两位 Reviewer 最大共识问题。六项控制必要但不充分。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N1)——framing 90% 偏向 attenuation，construct divergence/amplification caveat 被隔离在末尾。R1 AGREE 问题存在但认为 Should-Fix。两位共识核心缺陷在解释框架而非实验设计。Director 升级为 Must-Fix。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 13\n        action: \"Abstract/§6 给三种解释（attenuation/amplification/construct divergence）同等权重呈现；§5.1 更显式论证 RLHF 语境下 pairwise 的实践意义\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Should-Fix (W3)，R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 优势 2 肯定：§3.5 明确声明因果免责，因果声明已诚实克制。\"\n      - round: 13\n        reviewers: [1]\n        note: \"R13 R1 Strength S6 肯定：§3.5 Design Rationale 明确免责，'Controlled' 限定为实验控制而非因果识别。R2 未在 round 13 提出此问题。接近解决。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 R2-N1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R13 Director 降为 Should-Fix。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R13 Director 列为 Minor。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: §5.1 已有讨论但 'Blindspot' 术语天然偏向。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 Should-Fix (W3)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：论文承认三种等效解释但标题和 framing 隐式偏向 attenuation。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: 合并入 R5-MF1。两位共识核心缺陷。R1 W5 (construct validity 讨论不充分) + R2 N1 (framing 不对称) 本质上是同一问题。Director 升级为 Must-Fix。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: \"Acknowledged as limitation. Register is weakest axis.\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 确认仍未覆盖 register。Limitations 已承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 W2 和 R2 W4 均指出 register 未覆盖。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2 再次提出。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Q4 确认 register 仍无 rewriter 替换测试。R1 AGREE 建议补充或在 Limitations 注明。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识 Should-Fix：GPT-4o formality 13pp 与 Δ=15pp 仅差 2pp。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W2)，R2 AGREE。Δ=15pp 与 GPT-4o 最小偏差 13pp 重叠。两位一致建议 Δ 敏感性分析 (10/12/15/20pp) + 定量推导。Director 列为 Should-Fix。\"\n    action_items:\n      - round: 13\n        action: \"提供 Δ=15pp 的定量推导 + Δ 敏感性分析 (10/12/15/20pp) + Limitations 承认 moderate bias 可能逃脱\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"Table 1 footnote 已有但选择理由缺失。\"\n      - round: 11\n        reviewers: [1]\n        note: \"register axis 的 n 值和 power 未明确报告。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：cross-benchmark 覆盖稀疏，verbosity 仅 1 个 cross-benchmark 数据点。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W1) cross-benchmark 覆盖稀疏。R1 部分 AGREE——建议限定泛化声明。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 视觉审查：Figure 2 DAG 橙色/红色高亮路径色盲用户可能需额外辨认。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 视觉审查：Figure 2 caption 自包含性好，节点标签可读。未被 Reviewer 显式提及。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R13 两位一致要求 Δ 敏感性分析。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含讨论。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W4: Appendix R formality→verbosity word count d=−0.23 超过 d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1) 指出 d=−0.23 超阈值。R2 AGREE。Appendix R GEE covariate 控制已缓解（Style OR 变化 <12%），但主文未显式承认阈值违反。Director 列为 Minor。\"\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: n≈88 对 Likert power 严重不足。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 3 轴不足以支撑 'framework' 泛化。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W1/W5) cross-benchmark 覆盖稀疏 + 'framework' 过强。R1 部分 AGREE (W1) 但 REBUT W5——'framework' 是标准术语。Director 合并：限定泛化声明为 Should-Fix，'framework' 术语为 Minor 偏好。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests'，Gemini 为 confirmatory。\"\n    resolution_round: 10\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。GPT-4o cross-validation 部分缓解。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未显式提及。§5.4 人工标注 (50对) + GPT-4o cross-validation 部分缓解。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 Q4: direction-aware NLI gate 恢复的 21 对 content quality 是否与 bidirectional-pass 对不同？\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Q3 + R2 AGREE：direction-aware gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？需验证。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"与 R6-SF3 合并。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W3: tone 轴失败说明适用性受限。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W5) 再次提出。R1 REBUT——'framework' 是 NLP 文献标准术语，3+1 轴结果证明 discriminative validity。Director 列为 Minor 偏好建议。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'preliminary evidence' 限定\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 确认 §1 已有 GEE decomposition 引用。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W4)，R1 AGREE (minor 修正即可)。§1 开头 GPT-4o 例子隐含 Likert 判断是'错误的'，应添加一句 caveat。Director 列为 Minor。\"\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"Limitations 已含承认。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 小问题 5: 选择理由缺失。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M2)，R2 AGREE。Qwen3-32B evaluator-producer overlap 可能放大或掩盖结果。Director 列为 Minor。\"\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Limitations 承认即可。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Must-Fix。R2 交叉降为 Should-Fix。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W4)——未覆盖 instruction type/topic 分布、句法复杂度。R2 AGREE（严重程度略低——NLI threshold sweep 提供间接鲁棒性）。Director 列为 Should-Fix。\"\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix: 仅一个负控制不足以论证 Blindspot 是特定架构的产物。R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: R2 W5/N1 指出仅一个负控制模型。R1 W1 指出 TOST Δ=15pp 与 GPT-4o 最小 bias 几乎重叠。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N3)——未探讨 Claude 不受影响的机制。R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation。Director 降为 Should-Fix——R1 rebuttal 有效，但增加 1-2 句机制讨论成本低。\"\n    action_items:\n      - round: 11\n        action: \"Discussion 提出可检验的机制假设\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Limitations 增加 1-2 句 Claude null result 的可能机制讨论；降格为 'one model does not show this pattern'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"论文 §2 已引用 Bojar et al. (2016)。\"\n    resolution_round: 12\n\n  # ============================================================\n  # Round 12 issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"Formality 轴 quality-style 混淆严重——GEE 显示 Orig OR ≥ Style OR（多配置）\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 N1 (critical) + R2 W1 (warning) 共同指出。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W3) 指出 Table 1 BT 是未调整聚合值，方向不对称（88.9% vs 52.6%）混合了风格偏好与原文质量混淆。R2 AGREE——与 framing 不对称直接相关。Director 列为 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Intro 区分 verbosity (style-dominated) 和 formality (conditionally style-driven)\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 调整分析\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R12-N2\"\n    summary: \"Bootstrap CI 在 GEE 语境下的 pair-level resampling 合理性未论证\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 N2: §4.1 'All bootstrap CIs use 10,000 pair-level resamples' 但 GEE 使用 sandwich SE。Table 3 CI 来源不清。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 明确 bootstrap CI 用于 BT，GEE 用 sandwich SE。但 Table 3 CI 标注来源不清。R2 未独立提出但 AGREE M4 (方法未指定) 和 M5 (两种 GEE 区分不清) 相关。\"\n\n  - id: \"R12-W1\"\n    summary: \"Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 W4: Appendix R Table 18 d=−0.23 > d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1)——GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。R2 AGREE。Director 列为 Minor。\"\n\n  - id: \"R12-REF1\"\n    summary: \"建议补充引用：Carterette et al. (2008), Sedoc & Ungar (2020), Deutsch et al. (2023)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"R13 确认：Carterette et al. (2008) 和 Sedoc & Ungar (2020) 已在论文 §2 引用。Deutsch et al. (2023) 已在 References 中。\"\n    resolution_round: 13\n\n  # ============================================================\n  # Round 13 new issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称（88.9% vs 52.6%）使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。Appendix A GEE 控制后仍显著 (OR=2.58, p=0.032)，但主文读者不易获取。R2 AGREE。\"\n    action_items:\n      - round: 13\n        action: \"Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 的 GEE 调整分析\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R13-M1\"\n    summary: \"Bootstrap CI 方法（percentile vs BCa）未指定\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M4)，R2 AGREE。Appendix I 报告 bootstrap 95% CIs 但未指明类型。BT 估计接近 0.5 时 BCa 可能更稳健。\"\n\n  - id: \"R13-M2\"\n    summary: \"Table 2 GEE (Likert-outcome) 与 Table 3 GEE (pairwise-outcome) 共享标签但模型不同\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M5)，R2 AGREE。建议在 Table 2 标注 'GEE (Likert-outcome)' 以区分。零成本改进。\""
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是'真正增量贡献'与 novelty 不足判断矛盾。Director 降为 Should-Fix。持续分歧点。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"§1 增加一句明确承认心理测量学先例；限定为 'first controlled quantification + per-axis decomposition for LLM judges specifically'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 13\n    resolution: \"Round 7+ 确认主正文 8 页合规。R10 确认 ≤8 页。\"\n    resolution_round: 7\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 格式合规：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind ✓。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 格式合规：正文 ≤8 页 ✓，double-blind ✓，Limitations 合规 ✓。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2: register 轴所有改写用 Qwen3-32B 且无跨改写器验证，BT 结果也较弱。建议降级为 exploratory pilot axis。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W2) register 轴 evaluator-producer overlap 最严重，建议标注。R1 部分 AGREE——register 主结果来自其他 judge（GPT-4o, Llama-70B），核心 claim 建在 verbosity/formality 上。Director 列为 Minor。\"\n    action_items:\n      - round: 4\n        action: \"Formality independence test added to Appendix D\"\n        assigned_to: agent\n        status: done\n      - round: 10\n        action: \"Limitations 补一句：effect-size precision varies ±22% with rewriter choice\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix。R2 交叉降为 Should-Fix。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W2: 50 对由 2 名标注员评估，κ=0.44 (moderate)，4 个分歧全在 verbosity condensation 上。Wilson CI 过宽。建议增加标注量。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W1)，R2 AGREE。50 对 κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。Annotator 2 precision 84.3% (CI 65.3-93.6%)。两位一致建议 ≥100 对 + 第 3 标注员。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 13\n        action: \"增加至 ≥100 对 + 第 3 名标注员 + 分析分歧案例特征分布\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 M1: Abstract 数字密度过高。与往轮一致。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W3) 再次提出数字密度过高。R1 REBUT——实证论文 Abstract 需要定量具体性，ARR 无限制。Director 列为 Minor 偏好建议。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix——Appendix B direction asymmetry 暗示 IIA 违反。R2 交叉 [REBUT]——binary-choice BT 中 IIA 自动满足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 脚注 3：binary-choice BT 中 IIA structurally satisfied 的声明正确，方向异质性是 heterogeneous treatment effects 而非 IIA violation。\"\n      - round: 13\n        reviewers: [1]\n        note: \"R13 R1 Minor (M3)：脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。R2 AGREE。Director 列为 Minor。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。6 项 controls + Claude 负对照已部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 两位 Reviewer 最大共识问题。六项控制必要但不充分。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N1)——framing 90% 偏向 attenuation，construct divergence/amplification caveat 被隔离在末尾。R1 AGREE 问题存在但认为 Should-Fix。两位共识核心缺陷在解释框架而非实验设计。Director 升级为 Must-Fix。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work §2 讨论 Comparative Trap\"\n        assigned_to: paper_agent\n        status: done\n      - round: 13\n        action: \"Abstract/§6 给三种解释（attenuation/amplification/construct divergence）同等权重呈现；§5.1 更显式论证 RLHF 语境下 pairwise 的实践意义\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Should-Fix (W3)，R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 优势 2 肯定：§3.5 明确声明因果免责，因果声明已诚实克制。\"\n      - round: 13\n        reviewers: [1]\n        note: \"R13 R1 Strength S6 肯定：§3.5 Design Rationale 明确免责，'Controlled' 限定为实验控制而非因果识别。R2 未在 round 13 提出此问题。接近解决。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 R2-N1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R13 Director 降为 Should-Fix。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R13 Director 列为 Minor。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: §5.1 已有讨论但 'Blindspot' 术语天然偏向。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 Should-Fix (W3)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：论文承认三种等效解释但标题和 framing 隐式偏向 attenuation。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: 合并入 R5-MF1。两位共识核心缺陷。R1 W5 (construct validity 讨论不充分) + R2 N1 (framing 不对称) 本质上是同一问题。Director 升级为 Must-Fix。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: \"Acknowledged as limitation. Register is weakest axis.\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"R10 确认仍未覆盖 register。Limitations 已承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 W2 和 R2 W4 均指出 register 未覆盖。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2 再次提出。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Q4 确认 register 仍无 rewriter 替换测试。R1 AGREE 建议补充或在 Limitations 注明。\"\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识 Should-Fix：GPT-4o formality 13pp 与 Δ=15pp 仅差 2pp。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W2)，R2 AGREE。Δ=15pp 与 GPT-4o 最小偏差 13pp 重叠。两位一致建议 Δ 敏感性分析 (10/12/15/20pp) + 定量推导。Director 列为 Should-Fix。\"\n    action_items:\n      - round: 13\n        action: \"提供 Δ=15pp 的定量推导 + Δ 敏感性分析 (10/12/15/20pp) + Limitations 承认 moderate bias 可能逃脱\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"Table 1 footnote 已有但选择理由缺失。\"\n      - round: 11\n        reviewers: [1]\n        note: \"register axis 的 n 值和 power 未明确报告。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：cross-benchmark 覆盖稀疏，verbosity 仅 1 个 cross-benchmark 数据点。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W1) cross-benchmark 覆盖稀疏。R1 部分 AGREE——建议限定泛化声明。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 视觉审查：Figure 2 DAG 橙色/红色高亮路径色盲用户可能需额外辨认。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 视觉审查：Figure 2 caption 自包含性好，节点标签可读。未被 Reviewer 显式提及。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R13 两位一致要求 Δ 敏感性分析。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含讨论。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W4: Appendix R formality→verbosity word count d=−0.23 超过 d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1) 指出 d=−0.23 超阈值。R2 AGREE。Appendix R GEE covariate 控制已缓解（Style OR 变化 <12%），但主文未显式承认阈值违反。Director 列为 Minor。\"\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: n≈88 对 Likert power 严重不足。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 3 轴不足以支撑 'framework' 泛化。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W1/W5) cross-benchmark 覆盖稀疏 + 'framework' 过强。R1 部分 AGREE (W1) 但 REBUT W5——'framework' 是标准术语。Director 合并：限定泛化声明为 Should-Fix，'framework' 术语为 Minor 偏好。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests'，Gemini 为 confirmatory。\"\n    resolution_round: 10\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。GPT-4o cross-validation 部分缓解。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未显式提及。§5.4 人工标注 (50对) + GPT-4o cross-validation 部分缓解。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 Q4: direction-aware NLI gate 恢复的 21 对 content quality 是否与 bidirectional-pass 对不同？\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Q3 + R2 AGREE：direction-aware gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？需验证。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"与 R6-SF3 合并。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W3: tone 轴失败说明适用性受限。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W5) 再次提出。R1 REBUT——'framework' 是 NLP 文献标准术语，3+1 轴结果证明 discriminative validity。Director 列为 Minor 偏好建议。\"\n    action_items:\n      - round: 10\n        action: \"Limitations 补 'preliminary evidence' 限定\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 确认 §1 已有 GEE decomposition 引用。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W4)，R1 AGREE (minor 修正即可)。§1 开头 GPT-4o 例子隐含 Likert 判断是'错误的'，应添加一句 caveat。Director 列为 Minor。\"\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"Limitations 已含承认。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 小问题 5: 选择理由缺失。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M2)，R2 AGREE。Qwen3-32B evaluator-producer overlap 可能放大或掩盖结果。Director 列为 Minor。\"\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Limitations 承认即可。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Must-Fix。R2 交叉降为 Should-Fix。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W4)——未覆盖 instruction type/topic 分布、句法复杂度。R2 AGREE（严重程度略低——NLI threshold sweep 提供间接鲁棒性）。Director 列为 Should-Fix。\"\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix: 仅一个负控制不足以论证 Blindspot 是特定架构的产物。R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: R2 W5/N1 指出仅一个负控制模型。R1 W1 指出 TOST Δ=15pp 与 GPT-4o 最小 bias 几乎重叠。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N3)——未探讨 Claude 不受影响的机制。R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation。Director 降为 Should-Fix——R1 rebuttal 有效，但增加 1-2 句机制讨论成本低。\"\n    action_items:\n      - round: 11\n        action: \"Discussion 提出可检验的机制假设\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Limitations 增加 1-2 句 Claude null result 的可能机制讨论；降格为 'one model does not show this pattern'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"论文 §2 已引用 Bojar et al. (2016)。\"\n    resolution_round: 12\n\n  # ============================================================\n  # Round 12 issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"Formality 轴 quality-style 混淆严重——GEE 显示 Orig OR ≥ Style OR（多配置）\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 N1 (critical) + R2 W1 (warning) 共同指出。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W3) 指出 Table 1 BT 是未调整聚合值，方向不对称（88.9% vs 52.6%）混合了风格偏好与原文质量混淆。R2 AGREE——与 framing 不对称直接相关。Director 列为 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Intro 区分 verbosity (style-dominated) 和 formality (conditionally style-driven)\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 调整分析\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R12-N2\"\n    summary: \"Bootstrap CI 在 GEE 语境下的 pair-level resampling 合理性未论证\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 N2: §4.1 'All bootstrap CIs use 10,000 pair-level resamples' 但 GEE 使用 sandwich SE。Table 3 CI 来源不清。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 明确 bootstrap CI 用于 BT，GEE 用 sandwich SE。但 Table 3 CI 标注来源不清。R2 未独立提出但 AGREE M4 (方法未指定) 和 M5 (两种 GEE 区分不清) 相关。\"\n\n  - id: \"R12-W1\"\n    summary: \"Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 W4: Appendix R Table 18 d=−0.23 > d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1)——GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。R2 AGREE。Director 列为 Minor。\"\n\n  - id: \"R12-REF1\"\n    summary: \"建议补充引用：Carterette et al. (2008), Sedoc & Ungar (2020), Deutsch et al. (2023)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"R13 确认：Carterette et al. (2008) 和 Sedoc & Ungar (2020) 已在论文 §2 引用。Deutsch et al. (2023) 已在 References 中。\"\n    resolution_round: 13\n\n  # ============================================================\n  # Round 13 new issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称（88.9% vs 52.6%）使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。Appendix A GEE 控制后仍显著 (OR=2.58, p=0.032)，但主文读者不易获取。R2 AGREE。\"\n    action_items:\n      - round: 13\n        action: \"Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 的 GEE 调整分析\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R13-M1\"\n    summary: \"Bootstrap CI 方法（percentile vs BCa）未指定\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M4)，R2 AGREE。Appendix I 报告 bootstrap 95% CIs 但未指明类型。BT 估计接近 0.5 时 BCa 可能更稳健。\"\n\n  - id: \"R13-M2\"\n    summary: \"Table 2 GEE (Likert-outcome) 与 Table 3 GEE (pairwise-outcome) 共享标签但模型不同\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M5)，R2 AGREE。建议在 Table 2 标注 'GEE (Likert-outcome)' 以区分。零成本改进。\""
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-22T19:54:57.338093+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 44704}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-22T19:57:53.418477+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 13 (Fresh)\n\n**论文**: *The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n**Venue**: EMNLP 2026 (ACL ARR)\n**Reviewers**: R1（方法严谨性 + 统计方法 + 实验设计）, R2（新颖性 + framing + 写作质量）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，揭示 Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时的系统性分歧（\"Likert Blindspot\"）：pairwise 检测到显著风格偏好（BT > 60%, p < 0.001），而 Likert 完全遗漏（d → 0, p > 0.17）。跨 4 个 judge、3 个 benchmark、7 种统计方法验证，GEE 条件分解揭示 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional, register = judge-dependent）。实验设计在该领域属最周密之一，但 framing 系统性偏向 pairwise 为 ground truth，新颖性为增量贡献。\n\n---\n\n## Strengths\n\n**S1. 实验控制层次感出色。** CSD 三层控制（NLI gate §3.2、same-style double-rewrite §5.4、position swapping §3.3）+ 6 项 amplification controls，在 LLM judge 风格偏差文献中属最周密的实验设计之一。[R1-S1, R2-S1, 共识]\n\n**S2. 统计方法多元互补。** 7 种方法覆盖不同假设族（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Bayesian t），Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。Holm-Bonferroni 校正覆盖 6 个主检验，8 检验扩展族全通过。[R1-S2, R2-S2, 共识]\n\n**S3. GEE per-axis confound 分解具有独立方法论贡献。** Table 3 将 Style OR 与 Originality OR 分离，揭示 verbosity style-dominated (OR 8–15) vs formality conditional 的结构性差异。exchangeable working correlation + sandwich SE 经 Appendix C 诊断验证（ΔQIC < 0.001, Max|ΔCoef| < 0.02）。[R1-S4, R2-S4, 共识]\n\n**S4. 鲁棒性检验链完整。** NLI 阈值 11 点 sensitivity sweep (Appendix E)、bootstrap 衰减分析 (Appendix J)、rewriter 独立性检验 (Appendix D)、cross-axis 污染分析 (Appendix R)、formal power analysis (Figure 4, Appendix K)、100-point continuous Likert (Appendix M)——构成多层防御，核心发现难以归因于单一 artifact。[R1-S5, R2-S3, 共识]\n\n**S5. 因果声明审慎。** §3.5 Design Rationale 明确免责（\"we do not claim this DAG is a complete structural causal model\"），\"Controlled\" 限定为实验控制而非因果识别，Figure 2 DAG 标注残余混淆路径。标题副标题 \"Measurement-Mode Divergence\" 是中性表述。[R1-S6]\n\n**S6. 跨 judge 覆盖合理。** 4 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 negative control（Claude Sonnet 4），覆盖主流架构。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1 [critical] Framing 系统性偏向 pairwise 为 ground truth**\n- **位置**: Title, Abstract (\"signal loss exceeding 60%\"), §6 (\"Likert-only audits miss style-driven preferences\")\n- **问题**: 论文在 §5.1 承认三种等效解释（measurement attenuation / format amplification / construct divergence），引用 Comparative Trap (Jeong et al., 2025) 和 Tripathi et al. (2025)。但标题 \"The Likert Blindspot\" 将 Likert 定位为\"盲区\"，Abstract 和 Conclusion 的叙事 90% 倾向 attenuation 解释。Caveat 被隔离在 §5.1 末尾和 Limitations，未进入标题/摘要/结论的主叙事。缺乏外部 ground truth，论文无法判定 pairwise 检测到的是真实信号还是格式放大的微弱偏好。\n- **共识**: R2 Must-Fix (N1), R1 Should-Fix (W5) 但同意问题存在——本质是同一关切。Director 升级为 Must-Fix：framing 不对称贯穿全文核心叙事。\n- **建议**: Abstract/§6 给三种解释同等权重（1-2 句即可）；§5.1 更显式论证 RLHF 语境下 pairwise-detected biases 的实践意义。不必改标题。\n\n### Should-Fix\n\n**SF1 [warning] 新颖性定位需进一步明确**\n- **位置**: §1, §6\n- **问题**: Likert vs pairwise 灵敏度差异是心理测量学 established knowledge (Thurstone 1927)。论文真正贡献是 (a) 首次在 LLM judge 领域受控量化 + (b) GEE per-axis decomposition 方法论，但措辞有时像声称发现现象本身。\n- **共识**: R2 Must-Fix (N2), R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是\"真正增量贡献\"。Director 降为 Should-Fix：R1 rebuttal 有效，但局部措辞可收紧。\n- **建议**: §1 增加一句明确承认心理测量学先例；\"This is the Likert Blindspot\" → \"We term this the Likert Blindspot\"。\n\n**SF2 [warning] 人工标注规模不足（50 pairs, κ=0.44）**\n- **位置**: §5.4, Appendix S\n- **问题**: NLI gate 是 CSD 管线核心假设保障。50 对样本、2 名标注员、κ=0.44 moderate agreement 不足以建立强信心。Annotator 2 precision = 84.3%（CI [65.3%, 93.6%]），4 个分歧全在 verbosity condensation。\n- **共识**: R1 Should-Fix (W1), R2 AGREE。两位一致。\n- **建议**: 增加至 ≥100 对 + 第 3 名标注员 + 分析分歧案例特征分布（是否集中在特定 axis/instruction type）。\n\n**SF3 [warning] TOST 等价阈值 Δ=15pp 与 GPT-4o 最小偏差重叠**\n- **位置**: §4.1 脚注, Limitations, Appendix G\n- **问题**: GPT-4o formality BT=63.0%（13pp above chance）落在 Δ=15pp 等价区间内。10–14pp moderate bias 可能逃脱检测。Claude 实际 BT (50.2–54.1%) 远低于此阈值，当前结论不受影响，但 Δ 选择缺乏定量推导。\n- **共识**: R1 Should-Fix (W2), R2 AGREE。两位一致。\n- **建议**: 提供 Δ 的定量推导（多大偏差会改变 benchmark ranking？）+ Δ 敏感性分析 (10/12/15/20pp) + Limitations 承认 moderate bias 可能逃脱。\n\n**SF4 [warning] 方向不对称性对 Table 1 BT 的影响讨论不足**\n- **位置**: Table 1, Appendix A/H\n- **问题**: Formality 方向不对称显著（formal→casual 88.9% vs casual→formal 52.6%）。Table 1 的 BT 是未调整聚合值，混合了真实风格偏好与原文偏好混淆。Appendix A GEE 控制后仍显著（OR=2.58, p=0.032），但主文读者不易获取。\n- **共识**: R1 Should-Fix (W3), R2 AGREE。两位一致。\n- **建议**: Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 调整分析。\n\n**SF5 [warning] NLI gate 选择偏差检查覆盖面有限**\n- **位置**: §3.2, Appendix B\n- **问题**: 44% 拒绝率下仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade），未覆盖 instruction type/topic 分布、句法复杂度。NLI threshold sweep 稳定性提供间接鲁棒性，但不等同于无选择偏差。\n- **共识**: R1 Should-Fix (W4), R2 AGREE（严重程度略低）。两位一致。\n- **建议**: 增加 instruction type/topic 分布对比。\n\n**SF6 [warning] 负控制仅一个模型**\n- **位置**: §5.3, §6, Limitations\n- **问题**: Claude Sonnet 4 是唯一负控制，未探讨 Claude 不受影响的可能机制。\n- **共识**: R2 Must-Fix (N3), R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation 而非 architecture comparison。Director 降为 Should-Fix：R1 rebuttal 有效（论文 claim 范围有限），但增加机制讨论成本低。\n- **建议**: Limitations 增加 1-2 句 Claude null result 的可能机制讨论；降格为 \"one model does not show this pattern\"。\n\n**SF7 [warning] Cross-benchmark 覆盖稀疏**\n- **位置**: Table 1, §4\n- **问题**: AlpacaEval/MT-Bench 仅覆盖部分 judge × axis 组合。\"across three benchmarks\" 泛化声明需限定。\n- **共识**: R2 Should-Fix (W1), R1 部分 AGREE。\n- **建议**: 限定为 \"with primary results on LLMBar and confirmatory replication on selected configurations\"。\n\n### Minor\n\n**M1.** Cross-axis 污染 formality→verbosity word count d=−0.23 超过自设 d<0.20 标准。GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。[R1-M1, R2 AGREE]\n\n**M2.** 100-point continuous Likert (Appendix M) 仅用 Qwen3-32B，存在 evaluator-producer overlap。应在 Appendix M 注明。[R1-M2, R2 AGREE]\n\n**M3.** BT IIA 脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。[R1-M3, R2 AGREE]\n\n**M4.** Bootstrap CI 方法（percentile vs BCa）未指定。BT 估计接近 0.5 时 BCa 可能更稳健。[R1-M4, R2 AGREE]\n\n**M5.** Table 2 GEE（Likert-outcome）与 Table 3 GEE（pairwise-outcome）共享 \"GEE\" 标签但模型不同。建议在 Table 2 标注 \"GEE (Likert-outcome)\"。[R1-M5, R2 AGREE]\n\n**M6.** Register 轴 evaluator-producer overlap 最严重（Qwen3-32B 双重角色），应在论文中标注。[R2-W2, R1 部分 AGREE]\n\n**M7.** Introduction motivating example（GPT-4o formal vs casual）未 acknowledge formality-quality nuance。应添加一句 caveat 指向 §5.1 的 confound 讨论。[R2-W4, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n1. **[AGREE] 实验设计和统计方法是一流的** — CSD 三层控制 + 7 种统计方法 + 多层鲁棒性检验在该领域属最周密之列。GEE per-axis decomposition 是独立的方法论贡献。\n\n2. **[AGREE] 核心缺陷在解释框架而非实验设计** — 论文的 framing 系统性偏向 \"Likert is wrong, pairwise is right\"，而数据本身无法排除 construct divergence 或 format amplification 的替代解释。\n\n3. **[AGREE] 人工标注需扩展** — 50 对、κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。\n\n4. **[AGREE] TOST Δ=15pp 需更充分论证** — 与最小观测偏差（13pp）重叠，需定量推导 + 敏感性分析。\n\n5. **[AGREE] 方向不对称性需在主文更好呈现** — Table 1 未调整 BT 可能被误读为纯风格偏好。\n\n6. **[AGREE] 因果声明已审慎** — §3.5 的免责声明充分，无需修改。\n\n## Reviewer Divergence\n\n1. **Framing severity**: R2 Must-Fix, R1 Should-Fix。R1 认为副标题中性 + 实践论证有效，修改 Abstract/Conclusion 权重即可。**Director 判定: Must-Fix**（修复成本低但影响面大）。\n\n2. **Novelty**: R1 Excitement 3.5/5（对 NLP 社区有直接实践影响）; R2 3/5（established knowledge 的 domain transfer）。R1 REBUT 指出 R2 自己承认 GEE 分解是\"真正增量贡献\"，两个判断矛盾。**Director 判定: novelty 3–3.5 之间** — 受控量化 + GEE 分解有方法论价值，但核心洞察对跨领域读者非全新。\n\n3. **Negative control**: R2 Must-Fix, R1 REBUT（论文从未声明架构特异性，Claude 用于 pipeline validation）。**Director 判定: Should-Fix**（R1 rebuttal 有效）。\n\n4. **Abstract 数字密度**: R2 Should-Fix, R1 REBUT（实证论文需定量具体性）。**Director 判定: Minor 偏好建议**。\n\n5. **\"Framework\" 术语**: R2 Should-Fix, R1 REBUT（NLP 文献标准用法）。**Director 判定: Minor 偏好建议**。\n\n---\n\n## Questions（需作者回应）\n\n1. 六项 amplification controls 中哪一项最直接排除 \"pairwise amplifies micro-preferences\" 解释？无人类 ground truth 如何区分 attenuation vs amplification？[R2-Q1, 共识]\n\n2. 是否考虑过分方向拟合 BT 模型（formal→casual 和 casual→formal 分开估计），以区分真实风格偏好与原文质量混淆？[R1-Q1]\n\n3. NLI gate pass/reject 的 instruction type/topic 分布是否有系统差异？[R1-Q2, R2 AGREE]\n\n4. Direction-aware NLI gate 恢复的 21 对的 content quality 分布（Likert 质量分、NLI 分数分布）是否与 bidirectional-pass 对一致？[R1-Q3, R2 AGREE]\n\n5. Register 轴是否做了 rewriter 替换测试（类似 Appendix D 的 verbosity/formality 测试）？[R2-Q4, R1 AGREE]\n\n6. TOST Δ=15pp 的定量推导？Δ=10/12/15/20pp 下 TOST 结果如何变化？[R1-Q6, R2 AGREE]\n\n7. Claude 不表现 Blindspot 的可能机制？是否与 RLHF 策略差异有关？[R2-Q2]\n\n---\n\n## Missing References\n\n无必须添加的遗漏引用。可选增强：\n- Millsap (2011), *Statistical Approaches to Measurement Invariance* — 强化 measurement-mode divergence 理论基础 [R1]\n- Cattelan (2012), *Models for Paired Comparison Data* — BT 模型假设讨论 [R1]\n- Bai et al. (2022/2023), RLHF preference model comparison vs rating 差异 [R2]\n- Rafailov et al. (2023), DPO 中 pairwise preference 的理论性质 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warnings, 10 info）。\n\n**Warnings**:\n1. 第 8 页为纯文本页（§5.4 Robustness + §6 Conclusion + Limitations），无 display item。与第 3 页共同构成两段纯文本区域，但未连续出现，节奏可接受。\n2. 末页（p.18）仅 4 条参考文献，大面积空白。属 references 结尾自然情况。\n\n**Positives**:\n- 主正文 8 页含 4 figures + 3 tables = 7 display items，密度 0.875/页\n- Figure/Table 分布均匀（pp.2, 4, 5, 6, 7），无连续纯文本超 2 页\n- 所有 Table 使用 booktabs 风格，无竖线\n- 无 LaTeX 渲染错误、无 margin 溢出、行号正常（ARR review 格式）\n- ACL 匿名模板 + double-blind 合规\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Novelty | — | 3.0 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分依据**:\n\n本文在实验设计和统计方法上达到了 Conference 水准——CSD 三层控制、7 种统计方法三角验证、GEE per-axis confound 分解构成扎实的方法论贡献。跨 4 个 judge、3 个 benchmark 的验证提供了强鲁棒性证据。\n\n评分停留在 Findings (3.0) 的核心原因：\n\n1. **Framing 不对称 [Must-Fix]**: 标题、摘要、结论的主叙事预设 pairwise 为 ground truth，而论文自身数据无法区分 measurement attenuation / format amplification / construct divergence 三种解释。这不是局部措辞问题，而是贯穿论文的解释框架偏差。\n\n2. **新颖性有限**: Likert vs pairwise 灵敏度差异是心理测量学 established knowledge（Thurstone 1927 以降）。受控量化 + GEE 分解有方法论价值，但核心洞察（\"forced-choice 比 rating scale 更灵敏\"）对跨领域读者非全新。GEE per-axis decomposition 是真正的增量贡献，但单独不足以支撑 Conference 水平。\n\n3. **多个技术问题待解**: 人工标注规模不足（50 pairs, κ=0.44）、TOST 阈值与最小偏差重叠（Δ=15pp vs 13pp）、Table 1 方向不对称未调整、NLI gate 选择偏差检查不全面。\n\n**升级路径**:\n- 修正 framing（Abstract/Conclusion 给三种解释同等权重）→ **3.5 (Borderline Conference)**\n- + 扩展人工标注（≥100 对 + 第 3 标注员）+ TOST 敏感性分析 → **4.0 (Conference) 可能**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 开头 motivating example（GPT-4o formal vs casual）应紧随其后 acknowledge formality-quality nuance，而非推迟至 Limitations/Appendix A\n- \"This is the Likert Blindspot\" → \"We term this the Likert Blindspot\"\n- 增加一句明确承认心理测量学先例\n\n### §3 Method\n- §3.2 NLI gate 的选择偏差讨论应增加 instruction type/topic 维度\n- §3.5 Design Rationale 因果声明已审慎，无需修改\n\n### §4 Experiments\n- §4.1 脚注 3（BT IIA）应补充一维性假设说明\n- Table 1 formality 行应添加脚注提示方向不对称效应\n- Table 2 标注 \"GEE (Likert-outcome)\" 以区分 Table 3\n\n### §5 Analysis\n- §5.1 construct validity 讨论需扩展：明确区分 \"measurement sensitivity gap\" 和 \"construct divergence\"，论证 RLHF 语境下的实践重要性\n- §5.2 GEE 术语首次出现时应提供直觉解释\n- §5.4 amplification controls 中应更显式回应 Comparative Trap\n\n### §6 Conclusion\n- \"Likert-only audits miss style-driven preferences\" 应加 hedge（不能排除 power 解释和 format amplification 解释）\n\n### Appendices\n- Appendix G: 增加 TOST Δ=10/12/15/20pp 敏感性分析\n- Appendix M: 注明 100-point Likert 仅用 Qwen3-32B 的 evaluator-producer overlap 限制\n- Appendix R: 主文应明确承认 d=−0.23 超阈值并引导到 GEE covariate 缓解分析\n- Bootstrap CI: 明确指定 percentile vs BCa 方法\n\n### 格式合规\n- ✅ 正文 ≤8 页合规（§1-§6 结束于 p.8 上半部分，Limitations 从 p.8 下半开始不计入）\n- ✅ Double-blind 合规（\"Anonymous ACL submission\"，无作者信息泄露）\n- ✅ Limitations 合规（覆盖 quality-style confounding、evaluator-producer bias、scope 三维度，简洁，无新实验结果）\n- ✅ 参考文献格式规范",
  "project": "causal_style_decomp_judge",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
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
    "report": "# Consolidated Review Report — Round 13 (Fresh)\n\n**论文**: *The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*\n**Venue**: EMNLP 2026 (ACL ARR)\n**Reviewers**: R1（方法严谨性 + 统计方法 + 实验设计）, R2（新颖性 + framing + 写作质量）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，揭示 Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时的系统性分歧（\"Likert Blindspot\"）：pairwise 检测到显著风格偏好（BT > 60%, p < 0.001），而 Likert 完全遗漏（d → 0, p > 0.17）。跨 4 个 judge、3 个 benchmark、7 种统计方法验证，GEE 条件分解揭示 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional, register = judge-dependent）。实验设计在该领域属最周密之一，但 framing 系统性偏向 pairwise 为 ground truth，新颖性为增量贡献。\n\n---\n\n## Strengths\n\n**S1. 实验控制层次感出色。** CSD 三层控制（NLI gate §3.2、same-style double-rewrite §5.4、position swapping §3.3）+ 6 项 amplification controls，在 LLM judge 风格偏差文献中属最周密的实验设计之一。[R1-S1, R2-S1, 共识]\n\n**S2. 统计方法多元互补。** 7 种方法覆盖不同假设族（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Bayesian t），Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。Holm-Bonferroni 校正覆盖 6 个主检验，8 检验扩展族全通过。[R1-S2, R2-S2, 共识]\n\n**S3. GEE per-axis confound 分解具有独立方法论贡献。** Table 3 将 Style OR 与 Originality OR 分离，揭示 verbosity style-dominated (OR 8–15) vs formality conditional 的结构性差异。exchangeable working correlation + sandwich SE 经 Appendix C 诊断验证（ΔQIC < 0.001, Max|ΔCoef| < 0.02）。[R1-S4, R2-S4, 共识]\n\n**S4. 鲁棒性检验链完整。** NLI 阈值 11 点 sensitivity sweep (Appendix E)、bootstrap 衰减分析 (Appendix J)、rewriter 独立性检验 (Appendix D)、cross-axis 污染分析 (Appendix R)、formal power analysis (Figure 4, Appendix K)、100-point continuous Likert (Appendix M)——构成多层防御，核心发现难以归因于单一 artifact。[R1-S5, R2-S3, 共识]\n\n**S5. 因果声明审慎。** §3.5 Design Rationale 明确免责（\"we do not claim this DAG is a complete structural causal model\"），\"Controlled\" 限定为实验控制而非因果识别，Figure 2 DAG 标注残余混淆路径。标题副标题 \"Measurement-Mode Divergence\" 是中性表述。[R1-S6]\n\n**S6. 跨 judge 覆盖合理。** 4 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 negative control（Claude Sonnet 4），覆盖主流架构。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1 [critical] Framing 系统性偏向 pairwise 为 ground truth**\n- **位置**: Title, Abstract (\"signal loss exceeding 60%\"), §6 (\"Likert-only audits miss style-driven preferences\")\n- **问题**: 论文在 §5.1 承认三种等效解释（measurement attenuation / format amplification / construct divergence），引用 Comparative Trap (Jeong et al., 2025) 和 Tripathi et al. (2025)。但标题 \"The Likert Blindspot\" 将 Likert 定位为\"盲区\"，Abstract 和 Conclusion 的叙事 90% 倾向 attenuation 解释。Caveat 被隔离在 §5.1 末尾和 Limitations，未进入标题/摘要/结论的主叙事。缺乏外部 ground truth，论文无法判定 pairwise 检测到的是真实信号还是格式放大的微弱偏好。\n- **共识**: R2 Must-Fix (N1), R1 Should-Fix (W5) 但同意问题存在——本质是同一关切。Director 升级为 Must-Fix：framing 不对称贯穿全文核心叙事。\n- **建议**: Abstract/§6 给三种解释同等权重（1-2 句即可）；§5.1 更显式论证 RLHF 语境下 pairwise-detected biases 的实践意义。不必改标题。\n\n### Should-Fix\n\n**SF1 [warning] 新颖性定位需进一步明确**\n- **位置**: §1, §6\n- **问题**: Likert vs pairwise 灵敏度差异是心理测量学 established knowledge (Thurstone 1927)。论文真正贡献是 (a) 首次在 LLM judge 领域受控量化 + (b) GEE per-axis decomposition 方法论，但措辞有时像声称发现现象本身。\n- **共识**: R2 Must-Fix (N2), R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是\"真正增量贡献\"。Director 降为 Should-Fix：R1 rebuttal 有效，但局部措辞可收紧。\n- **建议**: §1 增加一句明确承认心理测量学先例；\"This is the Likert Blindspot\" → \"We term this the Likert Blindspot\"。\n\n**SF2 [warning] 人工标注规模不足（50 pairs, κ=0.44）**\n- **位置**: §5.4, Appendix S\n- **问题**: NLI gate 是 CSD 管线核心假设保障。50 对样本、2 名标注员、κ=0.44 moderate agreement 不足以建立强信心。Annotator 2 precision = 84.3%（CI [65.3%, 93.6%]），4 个分歧全在 verbosity condensation。\n- **共识**: R1 Should-Fix (W1), R2 AGREE。两位一致。\n- **建议**: 增加至 ≥100 对 + 第 3 名标注员 + 分析分歧案例特征分布（是否集中在特定 axis/instruction type）。\n\n**SF3 [warning] TOST 等价阈值 Δ=15pp 与 GPT-4o 最小偏差重叠**\n- **位置**: §4.1 脚注, Limitations, Appendix G\n- **问题**: GPT-4o formality BT=63.0%（13pp above chance）落在 Δ=15pp 等价区间内。10–14pp moderate bias 可能逃脱检测。Claude 实际 BT (50.2–54.1%) 远低于此阈值，当前结论不受影响，但 Δ 选择缺乏定量推导。\n- **共识**: R1 Should-Fix (W2), R2 AGREE。两位一致。\n- **建议**: 提供 Δ 的定量推导（多大偏差会改变 benchmark ranking？）+ Δ 敏感性分析 (10/12/15/20pp) + Limitations 承认 moderate bias 可能逃脱。\n\n**SF4 [warning] 方向不对称性对 Table 1 BT 的影响讨论不足**\n- **位置**: Table 1, Appendix A/H\n- **问题**: Formality 方向不对称显著（formal→casual 88.9% vs casual→formal 52.6%）。Table 1 的 BT 是未调整聚合值，混合了真实风格偏好与原文偏好混淆。Appendix A GEE 控制后仍显著（OR=2.58, p=0.032），但主文读者不易获取。\n- **共识**: R1 Should-Fix (W3), R2 AGREE。两位一致。\n- **建议**: Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 调整分析。\n\n**SF5 [warning] NLI gate 选择偏差检查覆盖面有限**\n- **位置**: §3.2, Appendix B\n- **问题**: 44% 拒绝率下仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade），未覆盖 instruction type/topic 分布、句法复杂度。NLI threshold sweep 稳定性提供间接鲁棒性，但不等同于无选择偏差。\n- **共识**: R1 Should-Fix (W4), R2 AGREE（严重程度略低）。两位一致。\n- **建议**: 增加 instruction type/topic 分布对比。\n\n**SF6 [warning] 负控制仅一个模型**\n- **位置**: §5.3, §6, Limitations\n- **问题**: Claude Sonnet 4 是唯一负控制，未探讨 Claude 不受影响的可能机制。\n- **共识**: R2 Must-Fix (N3), R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation 而非 architecture comparison。Director 降为 Should-Fix：R1 rebuttal 有效（论文 claim 范围有限），但增加机制讨论成本低。\n- **建议**: Limitations 增加 1-2 句 Claude null result 的可能机制讨论；降格为 \"one model does not show this pattern\"。\n\n**SF7 [warning] Cross-benchmark 覆盖稀疏**\n- **位置**: Table 1, §4\n- **问题**: AlpacaEval/MT-Bench 仅覆盖部分 judge × axis 组合。\"across three benchmarks\" 泛化声明需限定。\n- **共识**: R2 Should-Fix (W1), R1 部分 AGREE。\n- **建议**: 限定为 \"with primary results on LLMBar and confirmatory replication on selected configurations\"。\n\n### Minor\n\n**M1.** Cross-axis 污染 formality→verbosity word count d=−0.23 超过自设 d<0.20 标准。GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。[R1-M1, R2 AGREE]\n\n**M2.** 100-point continuous Likert (Appendix M) 仅用 Qwen3-32B，存在 evaluator-producer overlap。应在 Appendix M 注明。[R1-M2, R2 AGREE]\n\n**M3.** BT IIA 脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。[R1-M3, R2 AGREE]\n\n**M4.** Bootstrap CI 方法（percentile vs BCa）未指定。BT 估计接近 0.5 时 BCa 可能更稳健。[R1-M4, R2 AGREE]\n\n**M5.** Table 2 GEE（Likert-outcome）与 Table 3 GEE（pairwise-outcome）共享 \"GEE\" 标签但模型不同。建议在 Table 2 标注 \"GEE (Likert-outcome)\"。[R1-M5, R2 AGREE]\n\n**M6.** Register 轴 evaluator-producer overlap 最严重（Qwen3-32B 双重角色），应在论文中标注。[R2-W2, R1 部分 AGREE]\n\n**M7.** Introduction motivating example（GPT-4o formal vs casual）未 acknowledge formality-quality nuance。应添加一句 caveat 指向 §5.1 的 confound 讨论。[R2-W4, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n1. **[AGREE] 实验设计和统计方法是一流的** — CSD 三层控制 + 7 种统计方法 + 多层鲁棒性检验在该领域属最周密之列。GEE per-axis decomposition 是独立的方法论贡献。\n\n2. **[AGREE] 核心缺陷在解释框架而非实验设计** — 论文的 framing 系统性偏向 \"Likert is wrong, pairwise is right\"，而数据本身无法排除 construct divergence 或 format amplification 的替代解释。\n\n3. **[AGREE] 人工标注需扩展** — 50 对、κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。\n\n4. **[AGREE] TOST Δ=15pp 需更充分论证** — 与最小观测偏差（13pp）重叠，需定量推导 + 敏感性分析。\n\n5. **[AGREE] 方向不对称性需在主文更好呈现** — Table 1 未调整 BT 可能被误读为纯风格偏好。\n\n6. **[AGREE] 因果声明已审慎** — §3.5 的免责声明充分，无需修改。\n\n## Reviewer Divergence\n\n1. **Framing severity**: R2 Must-Fix, R1 Should-Fix。R1 认为副标题中性 + 实践论证有效，修改 Abstract/Conclusion 权重即可。**Director 判定: Must-Fix**（修复成本低但影响面大）。\n\n2. **Novelty**: R1 Excitement 3.5/5（对 NLP 社区有直接实践影响）; R2 3/5（established knowledge 的 domain transfer）。R1 REBUT 指出 R2 自己承认 GEE 分解是\"真正增量贡献\"，两个判断矛盾。**Director 判定: novelty 3–3.5 之间** — 受控量化 + GEE 分解有方法论价值，但核心洞察对跨领域读者非全新。\n\n3. **Negative control**: R2 Must-Fix, R1 REBUT（论文从未声明架构特异性，Claude 用于 pipeline validation）。**Director 判定: Should-Fix**（R1 rebuttal 有效）。\n\n4. **Abstract 数字密度**: R2 Should-Fix, R1 REBUT（实证论文需定量具体性）。**Director 判定: Minor 偏好建议**。\n\n5. **\"Framework\" 术语**: R2 Should-Fix, R1 REBUT（NLP 文献标准用法）。**Director 判定: Minor 偏好建议**。\n\n---\n\n## Questions（需作者回应）\n\n1. 六项 amplification controls 中哪一项最直接排除 \"pairwise amplifies micro-preferences\" 解释？无人类 ground truth 如何区分 attenuation vs amplification？[R2-Q1, 共识]\n\n2. 是否考虑过分方向拟合 BT 模型（formal→casual 和 casual→formal 分开估计），以区分真实风格偏好与原文质量混淆？[R1-Q1]\n\n3. NLI gate pass/reject 的 instruction type/topic 分布是否有系统差异？[R1-Q2, R2 AGREE]\n\n4. Direction-aware NLI gate 恢复的 21 对的 content quality 分布（Likert 质量分、NLI 分数分布）是否与 bidirectional-pass 对一致？[R1-Q3, R2 AGREE]\n\n5. Register 轴是否做了 rewriter 替换测试（类似 Appendix D 的 verbosity/formality 测试）？[R2-Q4, R1 AGREE]\n\n6. TOST Δ=15pp 的定量推导？Δ=10/12/15/20pp 下 TOST 结果如何变化？[R1-Q6, R2 AGREE]\n\n7. Claude 不表现 Blindspot 的可能机制？是否与 RLHF 策略差异有关？[R2-Q2]\n\n---\n\n## Missing References\n\n无必须添加的遗漏引用。可选增强：\n- Millsap (2011), *Statistical Approaches to Measurement Invariance* — 强化 measurement-mode divergence 理论基础 [R1]\n- Cattelan (2012), *Models for Paired Comparison Data* — BT 模型假设讨论 [R1]\n- Bai et al. (2022/2023), RLHF preference model comparison vs rating 差异 [R2]\n- Rafailov et al. (2023), DPO 中 pairwise preference 的理论性质 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warnings, 10 info）。\n\n**Warnings**:\n1. 第 8 页为纯文本页（§5.4 Robustness + §6 Conclusion + Limitations），无 display item。与第 3 页共同构成两段纯文本区域，但未连续出现，节奏可接受。\n2. 末页（p.18）仅 4 条参考文献，大面积空白。属 references 结尾自然情况。\n\n**Positives**:\n- 主正文 8 页含 4 figures + 3 tables = 7 display items，密度 0.875/页\n- Figure/Table 分布均匀（pp.2, 4, 5, 6, 7），无连续纯文本超 2 页\n- 所有 Table 使用 booktabs 风格，无竖线\n- 无 LaTeX 渲染错误、无 margin 溢出、行号正常（ARR review 格式）\n- ACL 匿名模板 + double-blind 合规\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Novelty | — | 3.0 | 3.0 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**评分依据**:\n\n本文在实验设计和统计方法上达到了 Conference 水准——CSD 三层控制、7 种统计方法三角验证、GEE per-axis confound 分解构成扎实的方法论贡献。跨 4 个 judge、3 个 benchmark 的验证提供了强鲁棒性证据。\n\n评分停留在 Findings (3.0) 的核心原因：\n\n1. **Framing 不对称 [Must-Fix]**: 标题、摘要、结论的主叙事预设 pairwise 为 ground truth，而论文自身数据无法区分 measurement attenuation / format amplification / construct divergence 三种解释。这不是局部措辞问题，而是贯穿论文的解释框架偏差。\n\n2. **新颖性有限**: Likert vs pairwise 灵敏度差异是心理测量学 established knowledge（Thurstone 1927 以降）。受控量化 + GEE 分解有方法论价值，但核心洞察（\"forced-choice 比 rating scale 更灵敏\"）对跨领域读者非全新。GEE per-axis decomposition 是真正的增量贡献，但单独不足以支撑 Conference 水平。\n\n3. **多个技术问题待解**: 人工标注规模不足（50 pairs, κ=0.44）、TOST 阈值与最小偏差重叠（Δ=15pp vs 13pp）、Table 1 方向不对称未调整、NLI gate 选择偏差检查不全面。\n\n**升级路径**:\n- 修正 framing（Abstract/Conclusion 给三种解释同等权重）→ **3.5 (Borderline Conference)**\n- + 扩展人工标注（≥100 对 + 第 3 标注员）+ TOST 敏感性分析 → **4.0 (Conference) 可能**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 开头 motivating example（GPT-4o formal vs casual）应紧随其后 acknowledge formality-quality nuance，而非推迟至 Limitations/Appendix A\n- \"This is the Likert Blindspot\" → \"We term this the Likert Blindspot\"\n- 增加一句明确承认心理测量学先例\n\n### §3 Method\n- §3.2 NLI gate 的选择偏差讨论应增加 instruction type/topic 维度\n- §3.5 Design Rationale 因果声明已审慎，无需修改\n\n### §4 Experiments\n- §4.1 脚注 3（BT IIA）应补充一维性假设说明\n- Table 1 formality 行应添加脚注提示方向不对称效应\n- Table 2 标注 \"GEE (Likert-outcome)\" 以区分 Table 3\n\n### §5 Analysis\n- §5.1 construct validity 讨论需扩展：明确区分 \"measurement sensitivity gap\" 和 \"construct divergence\"，论证 RLHF 语境下的实践重要性\n- §5.2 GEE 术语首次出现时应提供直觉解释\n- §5.4 amplification controls 中应更显式回应 Comparative Trap\n\n### §6 Conclusion\n- \"Likert-only audits miss style-driven preferences\" 应加 hedge（不能排除 power 解释和 format amplification 解释）\n\n### Appendices\n- Appendix G: 增加 TOST Δ=10/12/15/20pp 敏感性分析\n- Appendix M: 注明 100-point Likert 仅用 Qwen3-32B 的 evaluator-producer overlap 限制\n- Appendix R: 主文应明确承认 d=−0.23 超阈值并引导到 GEE covariate 缓解分析\n- Bootstrap CI: 明确指定 percentile vs BCa 方法\n\n### 格式合规\n- ✅ 正文 ≤8 页合规（§1-§6 结束于 p.8 上半部分，Limitations 从 p.8 下半开始不计入）\n- ✅ Double-blind 合规（\"Anonymous ACL submission\"，无作者信息泄露）\n- ✅ Limitations 合规（覆盖 quality-style confounding、evaluator-producer bias、scope 三维度，简洁，无新实验结果）\n- ✅ 参考文献格式规范",
    "project": "causal_style_decomp_judge",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-22T19:57:57.383990+00:00_

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

_source line 1066 · 2026-05-22T19:58:11.782137+00:00_

审稿完成。

**审稿报告已投递给 Research Director。**

核心结论：

- **Overall: 3.0 (Findings)**（R1: 3.5, R2: 3.0）
- **1 个 Must-Fix**: Framing 系统性偏向 pairwise 为 ground truth——标题/摘要/结论的叙事 90% 倾向 measurement attenuation 解释，而数据无法区分三种等效解释
- **7 个 Should-Fix**: 新颖性定位、人工标注规模（50 pairs κ=0.44）、TOST Δ=15pp 与最小偏差重叠、Table 1 方向不对称、NLI gate 选择偏差检查、单一负控制、cross-benchmark 覆盖稀疏
- **7 个 Minor**: cross-axis 污染超阈值、100-point Likert 单 judge、BT IIA 脚注、bootstrap CI 方法、GEE 标签区分、register evaluator-producer overlap、Intro 例子 nuance
- **升级路径**: 修正 framing → 3.5；+ 扩展标注 + TOST 敏感性分析 → 4.0 可能

Issue Tracker 已同步更新至 Round 13。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1067 · 2026-05-22T19:58:14.451899+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **N1（framing）**：同意实质问题，但降级为 Should-Fix——叙事权重不均但非完全缺失
- **N2（novelty）**：反驳——§1 已明确界定贡献为"首次受控量化"，且 R2 自己承认 GEE 分解是真正增量贡献，两个判断矛盾
- **N3（负控制）**：反驳——论文用 Claude 做 pipeline validation 而非 architecture comparison，R2 读入了论文未提出的 claim
- **Q3（power issue）**：反驳——Appendix J/K 明确证明 Likert d → 0 at all n，是结构性差异非功效问题

维持 Overall 3.5（Borderline Conference），认为 R2 的 3.0 偏低。

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

_source line 1068 · 2026-05-22T19:58:29.695574+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall: 3.0 (Findings)**（R1: 3.5, R2: 3.0）
- **1 个 Must-Fix**: Framing 系统性偏向 pairwise 为 ground truth（三种解释权重不均）
- **7 个 Should-Fix**: 新颖性定位、人工标注规模(50对 κ=0.44)、TOST Δ=15pp、方向不对称、NLI gate 选择偏差、负控制机制讨论、cross-benchmark 覆盖
- **7 个 Minor**: cross-axis 阈值违反、100-point Likert overlap、BT IIA 脚注、bootstrap CI 方法、GEE 标签区分、register overlap 标注、Intro caveat
- **升级路径**: 修正 framing → 3.5; + 扩展标注 + TOST 敏感性分析 → 4.0 可能
- **Issue Tracker 已同步更新**（round 13 共新增/更新 20+ issues）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 103

## Round 103

52 recorded events


### User

_source line 1069 · 2026-05-22T22:38:12.886327+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1070 · 2026-05-22T22:38:21.265791+00:00_

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

_source line 1071 · 2026-05-22T22:38:21.366944+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-22T22:38:28.645206+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,WebSearch",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-22T22:38:28.695926+00:00_



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

_source line 1074 · 2026-05-22T22:38:31.759279+00:00_

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

_source line 1075 · 2026-05-22T22:38:33.165738+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **register_100_cf** (killed): Register axis (academic/conversational) produces detectable style bias in GPT-4o judge comparable to formality axis, with pairwise win rate >= 60% and p < 0.05, demonstrating axis-dependent bias generalizes beyond formality\n- **gemini_flash_fourth_judge** (success): Gemini Flash as a fourth judge will also exhibit style blindspot (BT-significant but Likert-NS) on formality and verbosity axes, consistent with GPT-4o, Qwen-32B, and Claude judges, confirming the blindspot is judge-universal rather than model-specific.\n- **llama70b_register** (success): Llama-70B register axis shows weak style bias (~55% BT, consistent with GPT-4o 57% and Qwen3-32B 55.3%), confirming register as originality-dominated across three independent judge architectures\n  [llama70b_register_summary](/api/workspace-files/projects/causal_style_decomp_judge/artifacts/llama70b_register/data/llama70b_register_summary.json)\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-29275: 无 GPU 信息\n\n## 告警\n- exp-013: 已被终止 — unknown\n- register_100_cf: 已被终止 — unknown\n- exp-015: 已被终止 — unknown\n- exp-016: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-22T22:38:33.316653+00:00_

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

_source line 1077 · 2026-05-22T22:38:34.120259+00:00_

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
…[truncated 3907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-22T22:38:34.271277+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1079 · 2026-05-22T22:38:35.677106+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-22T22:38:36.480799+00:00_

-rw-r--r-- 1 ubuntu ubuntu 400161 May 22 22:04 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1081 · 2026-05-22T22:38:36.531418+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-22T22:38:36.582584+00:00_

&lt;persisted-output>
Output too large (49.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/71e97811-0d37-46a7-82d8-d84d2096820e/tool-results/bpemge3tn.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
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
    last_seen_round: 13
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
        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
      - round: 11
        reviewers: [1, 2]
        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
      - round: 12
        reviewers: [1, 2]
        note: "R12 fres
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-22T22:38:39.560371+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I've performed the web search for you
…[truncated 1051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5289
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-22T22:38:44.686877+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-22T22:38:44.988452+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline ARR"
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
    "query": "EMNLP 2026 call for papers commitment deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-22T22:38:46.393766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/71e97811-0d37-46a7-82d8-d84d2096820e/tool-results/bpemge3tn.txt"
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
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/71e97811-0d37-46a7-82d8-d84d2096820e/tool-results/bpemge3tn.txt"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-22T22:38:46.746642+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-4 issues (all resolved unless noted)
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
22	    last_seen_round: 13
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
34	        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
35	      - round: 10
36	        reviewers: [1, 2]
37	        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
38	      - round: 11
39	        reviewers: [1, 2]
40	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
41	      - round: 12
42	        reviewers: [1, 2]
43	        note: "R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。"
44	      - rou
…[truncated 48920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool result

_source line 1088 · 2026-05-22T22:38:51.464917+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here are the key deadlines for EMNLP 2026 related to ARR submissions and commitment:

**ARR Submission and Processing Deadlines:**

- ARR submission dead
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6476
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-22T22:38:52.117831+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

For both long and short papers, all figures and
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7430
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-22T22:39:06.789678+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "config.yaml"
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
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-22T22:39:07.292667+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-22T22:39:08.247954+00:00_

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

_source line 1093 · 2026-05-22T22:39:08.298652+00:00_

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

_source line 1094 · 2026-05-22T22:39:10.757823+00:00_

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

_source line 1095 · 2026-05-22T22:39:12.213641+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-22T22:39:12.264245+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review configuration"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review configuration"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-22T22:39:12.365087+00:00_

NO_EXTERNAL_REVIEW_CONFIG

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

_source line 1098 · 2026-05-22T22:39:14.824615+00:00_

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

_source line 1099 · 2026-05-22T22:39:15.276618+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce systematically divergent style sensitivity when applied to LLM judges.
3	We introduce Controlled Style Decomposition (CSD), a black-box framework that quantifies this divergence under controlled conditions via human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
4	Across four judges from independent providers, one negative control, and two primary axes (formality, verbosity), the divergence is robust: pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\% at stronger effects---replicated across three benchmarks and confirmed by seven statistical methods.
5	GEE conditional decomposition reveals qualitatively distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects a conditional effect where style and content quality contribute jointly---determining which pairwise estimates are directly interpretable and which require decomposition.
6	This divergence admits three non-exclusive explanations---measurement attenuation, format amplification, or construct divergence---that our controlled design bounds but cannot definitively adjudicate.
7	A negative-control judge shows no divergence on either primary axis, supporting discriminative validity.
8	Whether the divergence reflects Likert attenuation, pairwise amplification, or construct-level differences remains open; the practical consequence is unambiguous: Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
9	\end{abstract}
10	

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

_source line 1100 · 2026-05-22T22:39:15.327143+00:00_

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

_source line 1101 · 2026-05-22T22:39:15.779867+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}.
6	We note that formality preferences may partially reflect legitimate quality judgments---our GEE decomposition (\S\ref{sec:direction}) quantifies this originality component.
7	This example reflects a systematic pattern.
8	
9	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
11	Despite this consensus, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
12	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison \citep{thurstone1927law,stevens1946theory}; we provide the first controlled quantification of this gap for LLM judges, with GEE decomposition revealing axis-dependent confound structures.
13	
14	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, pe
…[truncated 2545 chars]

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

_source line 1102 · 2026-05-22T22:39:15.881493+00:00_

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

_source line 1103 · 2026-05-22T22:39:15.932277+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 5781 chars]

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

_source line 1104 · 2026-05-22T22:39:16.283878+00:00_

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

_source line 1105 · 2026-05-22T22:39:16.334638+00:00_

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
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
20	For axes that inherently c
…[truncated 6101 chars]

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

_source line 1106 · 2026-05-22T22:39:20.098394+00:00_

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

_source line 1107 · 2026-05-22T22:39:20.651013+00:00_

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
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$; verbosity: $p = 0.453$) reflects heterogeneous treatment effects across style directions rather than IIA violation. The unidimensionality assumption (single latent ``quality'' dimension) is standard in evaluation contexts but not empirically verified here.}
13	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation with
…[truncated 17504 chars]

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

_source line 1108 · 2026-05-22T22:39:20.651449+00:00_

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

_source line 1109 · 2026-05-22T22:39:21.153587+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: pairwise comparison and Likert scoring produce systematically divergent verdicts on the same style contrasts---complete divergence at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed by seven statistical methods across four judges and three benchmarks.
6	Second, GEE conditional decomposition reveals qualitatively distinct per-axis confound structures---verbosity is style-dominated, formality is a conditional effect, register is judge-dependent---determining which estimates are directly interpretable and which require decomposition.
7	Whether the gap reflects attenuation or amplification, single-format audits risk systematic blind spots; human ground-truth validation of both modes is the key next step.
8	

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

_source line 1110 · 2026-05-22T22:39:21.204384+00:00_

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


### Tool result

_source line 1111 · 2026-05-22T22:39:21.456005+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), human annotation agreement (S).}
4	
5	\section{Direction Asymmetry and Quality Confounding}
6	\label{app:direction}
7	
8	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
9	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
10	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
11	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
12	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
13	
14	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
15	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
16	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect mag
…[truncated 30772 chars]

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

_source line 1112 · 2026-05-22T22:39:44.890814+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check,director_post_to_reviewer",
  "max_results": "2"
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
    "query": "select:dispatch_visual_check,director_post_to_reviewer",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-22T22:39:44.891250+00:00_

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

_source line 1114 · 2026-05-22T22:39:49.657602+00:00_

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

_source line 1115 · 2026-05-22T22:40:08.552085+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18894
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-22T22:40:08.753328+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责**方法严谨性 + 统计方法学 + 实验设计**的审查。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **格式**: ACL 模板，double-blind\n- **页数**: 正文 ≤8 页，参考文献不限\n- **Limitations**: 不计入页数限制，需在 conclusion 后、references 前\n- **匿名**: 必须匿名，作者写 \"Anonymous\"\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **统计方法的正确性与完整性**：\n   - BT 模型的 IIA 假设是否充分讨论？\n   - GEE 模型选择（exchangeable correlation + sandwich SE）是否合理？\n   - Bootstrap CI 方法（percentile vs BCa）是否指明？\n   - TOST 等价检验的 Δ=15pp 是否有充分的外部依据？\n   - Holm-Bonferroni 校正范围是否合理？\n\n2. **实验设计的严谨性**：\n   - NLI gate 的内容保持验证是否充分（50 对人工标注 κ=0.44）？\n   - Cross-rewriter independence test 的覆盖范围？\n   - 负控制（Claude Sonnet 4）的论证力度？\n   - Direction-aware NLI gate 恢复的 21 对的内容质量验证？\n\n3. **可重复性与透明度**：\n   - 模型版本、超参数、随机种子是否完整报告？\n   - 统计检验的前提假设是否满足并报告？\n\n4. **格式合规**：\n   - 正文是否 ≤8 页？\n   - 是否使用 ACL 模板？\n   - 是否匿名？\n   - Limitations section 是否在正确位置？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
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
    "text": "你负责**方法严谨性 + 统计方法学 + 实验设计**的审查。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **格式**: ACL 模板，double-blind\n- **页数**: 正文 ≤8 页，参考文献不限\n- **Limitations**: 不计入页数限制，需在 conclusion 后、references 前\n- **匿名**: 必须匿名，作者写 \"Anonymous\"\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **统计方法的正确性与完整性**：\n   - BT 模型的 IIA 假设是否充分讨论？\n   - GEE 模型选择（exchangeable correlation + sandwich SE）是否合理？\n   - Bootstrap CI 方法（percentile vs BCa）是否指明？\n   - TOST 等价检验的 Δ=15pp 是否有充分的外部依据？\n   - Holm-Bonferroni 校正范围是否合理？\n\n2. **实验设计的严谨性**：\n   - NLI gate 的内容保持验证是否充分（50 对人工标注 κ=0.44）？\n   - Cross-rewriter independence test 的覆盖范围？\n   - 负控制（Claude Sonnet 4）的论证力度？\n   - Direction-aware NLI gate 恢复的 21 对的内容质量验证？\n\n3. **可重复性与透明度**：\n   - 模型版本、超参数、随机种子是否完整报告？\n   - 统计检验的前提假设是否满足并报告？\n\n4. **格式合规**：\n   - 正文是否 ≤8 页？\n   - 是否使用 ACL 模板？\n   - 是否匿名？\n   - Limitations section 是否在正确位置？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-22T22:40:22.281365+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13528
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-22T22:40:22.432131+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责**新颖性 + framing + 写作质量 + 完整性**的审查。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **格式**: ACL 模板，double-blind\n- **页数**: 正文 ≤8 页，参考文献不限\n- **Limitations**: 不计入页数限制，需在 conclusion 后、references 前\n- **匿名**: 必须匿名，作者写 \"Anonymous\"\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **新颖性（Novelty）**：\n   - Likert Blindspot 是否只是 Thurstone (1927) 经典结论在 LLM judge 领域的 domain transfer？\n   - 论文贡献的增量性——CSD 框架、GEE decomposition 的独立贡献价值？\n   - 与 RATE (Reber et al., 2025)、Comparative Trap (Jeong et al., 2025) 的差异化定位？\n\n2. **Framing 与叙事平衡**：\n   - 三种解释（attenuation / amplification / construct divergence）的权重是否平衡？\n   - \"Blindspot\" 命名是否隐含了偏向 attenuation 的预设？\n   - Introduction 的 motivating example 是否暗示 Likert 判断是\"错误的\"？\n   - Abstract 数字密度是否过高影响可读性？\n\n3. **写作质量**：\n   - 行文清晰度、术语一致性\n   - 图表的信息密度与可读性\n   - Related Work 的完整性和定位准确性\n\n4. **完整性**：\n   - 3 个 style axes 是否足以支撑 \"framework\" 级别的泛化声明？\n   - Cross-benchmark 覆盖是否充分（LLMBar n=100 + AlpacaEval + MT-Bench 选择性配置）？\n   - 遗漏的重要相关工作？\n\n5. **格式合规**：\n   - 正文 ≤8 页？\n   - double-blind 匿名？\n   - Limitations 位置正确？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
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
    "text": "你负责**新颖性 + framing + 写作质量 + 完整性**的审查。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **格式**: ACL 模板，double-blind\n- **页数**: 正文 ≤8 页，参考文献不限\n- **Limitations**: 不计入页数限制，需在 conclusion 后、references 前\n- **匿名**: 必须匿名，作者写 \"Anonymous\"\n- **截止日期**: 2026-05-25 (ARR May cycle)\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **新颖性（Novelty）**：\n   - Likert Blindspot 是否只是 Thurstone (1927) 经典结论在 LLM judge 领域的 domain transfer？\n   - 论文贡献的增量性——CSD 框架、GEE decomposition 的独立贡献价值？\n   - 与 RATE (Reber et al., 2025)、Comparative Trap (Jeong et al., 2025) 的差异化定位？\n\n2. **Framing 与叙事平衡**：\n   - 三种解释（attenuation / amplification / construct divergence）的权重是否平衡？\n   - \"Blindspot\" 命名是否隐含了偏向 attenuation 的预设？\n   - Introduction 的 motivating example 是否暗示 Likert 判断是\"错误的\"？\n   - Abstract 数字密度是否过高影响可读性？\n\n3. **写作质量**：\n   - 行文清晰度、术语一致性\n   - 图表的信息密度与可读性\n   - Related Work 的完整性和定位准确性\n\n4. **完整性**：\n   - 3 个 style axes 是否足以支撑 \"framework\" 级别的泛化声明？\n   - Cross-benchmark 覆盖是否充分（LLMBar n=100 + AlpacaEval + MT-Bench 选择性配置）？\n   - 遗漏的重要相关工作？\n\n5. **格式合规**：\n   - 正文 ≤8 页？\n   - double-blind 匿名？\n   - Limitations 位置正确？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-22T22:40:23.694439+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1262
}
```

</details>

---


### Assistant

_source line 1120 · 2026-05-22T22:40:28.422187+00:00_

圆桌审稿会议 Round 1 已启动：

- 视觉审查 Agent 已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 统计方法学 + 实验设计）已分配
- Reviewer 2（新颖性 + framing + 写作质量 + 完整性）已分配

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1121 · 2026-05-22T22:46:21.229249+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5
**一句话总结**: 方法论严谨、实验充分，但核心发现在心理测量学中可预测，"Blindspot"命名隐含对 attenuation 解释的偏向，3 条 style axis 难以支撑 "framework" 级别的泛化声明。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 方法论设计严谨：NLI 内容门控、position-controlled pairwise、GEE 分解、FWER 校正、bootstrap attenuation 分析均到位。主要扣分点：三种解释（attenuation/amplification/construct divergence）无法区分，限制了可操作结论 |
| Excitement | 3 / 5 | 实证贡献扎实，但核心发现（forced-choice 比 absolute rating 更敏感）是 Thurstone (1927) 以来的经典心理测量结论。GEE per-axis 分解揭示不同 confound 结构是本文最有趣的增量贡献，但整体新颖性有限 |
| Reproducibility | 4 / 5 | 实验细节充分（Appendix P 列出模型、API、温度参数），承诺开源代码和数据。NLI 阈值选择和 rewriter prompt 均有记录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Framework" 泛化声明与实际覆盖不匹配
- 具体位置：Section 1 contributions 第一条（"a CSD, a black-box framework for per-axis style bias detection"）；Section 6 Conclusion
- 问题：论文将 CSD 定位为通用的 per-axis style bias detection "framework"，但实际只测试了 formality、verbosity、register 三条轴。其中 register 仅在 Table 1 中出现部分结果，cross-axis contamination 分析（Appendix R/Table 19）也仅覆盖这三条轴。三条相关性较高的表面风格特征（均为文本表层属性，不涉及论证结构、逻辑深度等深层风格）不足以支撑 "framework" 级别的泛化。
- 为什么影响接收：Reviewer 会质疑是否遇到 semantic-level 风格轴（如 hedging、humor、technicality）时 CSD 的 NLI 门控还能正常工作——这些轴的 style-content 边界更模糊，NLI entailment 可能系统性地拒绝合法 rewrite。
- 建议修改方向：(a) 将 "framework" 降级为 "methodology" 或 "experimental protocol"；(b) 或者增加 1-2 条非表面风格轴（如 hedging/directness）的实验；(c) 在 Limitations 中明确讨论 CSD 对深层风格轴的适用性边界。

**N2** [critical] 标题与叙事隐含 attenuation 偏向，与三种解释并列的中立定位矛盾
- 具体位置：Title ("Likert Blindspot")；Abstract 第一句 ("Likert and pairwise scoring produce systematically divergent style sensitivity")；Section 6 Conclusion ("Likert-only analysis may fail to surface style-driven preferences")
- 问题："Blindspot" 这个词在认知科学中的含义是"盲区"——即某个真实存在的东西未被检测到。这直接预设了 attenuation 解释（Likert 遗漏了真实偏好），排斥了 amplification 解释（pairwise 放大了微小偏好到不合理程度）和 construct divergence 解释（两种模式测量的是不同构念）。论文 Section 5.1 和 Limitations 中对三种解释的讨论是平衡的，但标题和整体叙事框架与这种平衡矛盾。Introduction 的 motivating example（page 1，GPT-4o 对 formal vs. casual 回答给出 8 vs. 5）也暗示 Likert 判断是"错误的"——但实际上可能是 pairwise 模式在 forced-choice 设定下放大了微小偏好。
- 为什么影响接收：Framing bias 会被 reviewer 视为论文缺乏理论中立性。如果论文无法区分三种解释（论文自己也承认），那么标题和叙事不应偏向其中一种。
- 建议修改方向：(a) 考虑更中性的标题，如 "Measurement-Mode Divergence in LLM Judge Style Evaluation"（论文副标题已经是这个）；(b) 在 Introduction 的 motivating example 后立即引入 amplification 和 construct divergence 作为等权重的替代解释，而非仅在 Section 5.1 才讨论；(c) Conclusion 中的表述从 "Likert may fail" 改为 "the two modes may capture different aspects of style preferences"。

**N3** [critical] 核心发现的增量新颖性论证不足
- 具体位置：Section 1 Introduction；Section 2 Related Work（Measurement Sensitivity in NLG Evaluation 段落）
- 问题：Forced-choice comparison 比 absolute rating 有更高判别力是 Thurstone (1927) Law of Comparative Judgment 的经典结论，Stevens (1946) 的 scale taxonomy、Krosnick (1999) 的 survey research 方法论、Preston & Colman (2000) 的 granularity 研究都反复验证了这一点。论文在 Section 2 引用了这些工作，但未充分论证为什么在 LLM judge 领域"重新发现"这个现象构成足够的新颖性。论文隐含的论证是"虽然心理测量学早已知道这个问题，但 LLM-as-judge 社区还没有用 controlled methodology 系统展示它"——这是一个 empirical verification 而非 conceptual advance。
- 为什么影响接收：对于 EMNLP 主会议（Overall 4.0），需要超越 domain transfer 的贡献。论文需要更清楚地论证：LLM judges 相比 human judges 有什么独特属性使得这个发现不仅是 expected，而且在具体表现形式上是 surprising 的？
- 建议修改方向：(a) 强调 GEE decomposition 揭示的 per-axis confound structure 差异（formality 是 conditional effect，verbosity 是 style-dominated）——这是人类评估文献中尚未系统报告的 LLM-specific 发现；(b) 论证 LLM judges 的 training pipeline（RLHF/RLAIF）可能引入人类评估不存在的 mode-specific biases；(c) 将 novelty claim 的重心从 "发现 divergence" 转向 "quantifying and decomposing the divergence per axis"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 数字密度过高
- 具体位置：Abstract（page 1）
- 问题：Abstract 中出现 p < 0.001、p = 0.17、60%、85.2%、>60% 等至少 6 个定量数字。对于一篇方法论+实证论文，Abstract 应优先传达 insight 而非数字堆砌。特别是 "with signal loss exceeding 60% at stronger effects" 在没有上下文的情况下不易理解（60% 的什么？相对什么基线？）。
- 建议：保留 1-2 个最关键的数字（如 Blindspot 在多少个 judge 上复现），将其余移至 Section 5。

**W2** [warning] 与 RATE (Reber et al., 2025) 的差异化论证薄弱
- 具体位置：Section 2，Related Work 倒数第二段（page 3）
- 问题：论文列举了 CSD 与 RATE 的三点差异：(1) targets individual style axes，(2) measures through position-controlled pairwise comparison rather than Likert ATE，(3) enforces NLI entailment gating。但 RATE 也做 per-axis counterfactual rewriting（按 style attribute 分开处理），差异 (1) 更多是程度差别而非本质区别。核心差异其实是 (2)——CSD 的 cross-measurement comparison，但这一点的重要性在 Related Work 中被与其他两点并列稀释了。
- 建议：明确突出 "cross-measurement mode comparison" 作为与 RATE 的核心差异点，而非三点并列。同时承认 CSD 在 Likert-only 分析方面的贡献（Section 5.1 表明 CSD 的 Likert ATE 复现了 RATE 的非显著结果）与 RATE 是互补而非替代关系。

**W3** [warning] LLMBar 样本量小（n=100）对统计推断的限制
- 具体位置：Section 3.4；Table 1；Figure 4
- 问题：主实验基于 LLMBar 的 n=100 instruction-response pairs。虽然论文通过 bootstrap attenuation 分析（Appendix J）和 n=355 的 scaled replication 部分缓解了这一问题，Figure 4 也展示了 power analysis，但 n=100 在 formality 轴上仅有 62 个 NLI-filtered pairs（Table 1 footnote），Likert ATE 的 effect size 在 n=100 时 CI 跨越零。论文将 AlpacaEval 和 MT-Bench 定位为 confirmatory，但这两个 benchmark 仅使用 "selected configurations"（Section 3.4），且 MT-Bench 的结果仅出现在 Table 1 最后两行，未充分讨论。
- 建议：在 Discussion 或 Limitations 中更坦率地讨论 n=100 的局限性，特别是对 GEE 交互项估计精度的影响。

**W4** [warning] Construct divergence 解释发展不足
- 具体位置：Section 5.1（"Interpreting the divergence" 段落）；Limitations（page 9）
- 问题：三种解释中，construct divergence（Likert 测量绝对质量差异，pairwise 测量序数偏好）在理论上最有趣，也与心理测量学文献最相关。但论文对此解释的讨论最薄弱——Section 5.1 仅一句话提及，Limitations 中稍多展开但也仅两句。如果两种测量模式确实测量不同构念，那 "divergence" 本身就不是缺陷而是信息量——这会根本改变论文的实践建议。
- 建议：在 Section 5.1 或 Discussion 中用一段专门讨论 construct divergence 的含义和可检验预测。例如：如果是 construct divergence，我们应期望 divergence 大小与 content quality variance 无关（因为两种模式测量的是不同东西），但如果是 attenuation，divergence 应与 effect size 正相关。论文的数据（Figure 4 的 power curve）可能已经包含区分这两种解释的线索。

**W5** [warning] Claude Sonnet 4 负控制结果的讨论不充分
- 具体位置：Section 5.4 第二段；Appendix G（Table 10）
- 问题：Claude Sonnet 4 作为负控制不展示 Blindspot，论文将其归因于"RLHF training composition or instruction-following strategies"（page 9 Limitations），但未进一步分析为什么这一个 judge 表现不同。如果 Blindspot 是 measurement mode 的固有属性（如论文标题暗示的），为什么它在某些 judge 上消失？这个 negative result 实际上暗示 Blindspot 可能更多是 model-specific training artifact 而非 measurement-mode intrinsic property——这对论文的核心叙事构成潜在挑战。
- 建议：在 Section 5.4 或 Discussion 中讨论 Sonnet 4 的负结果对 "measurement-mode divergence" 叙事的含义。是否说明 Blindspot 是可以通过训练消除的 judge 属性，而非 Likert 模式的固有限制？

---

## 小问题（不影响接收）

1. **Table 1 可读性**：Table 1 包含 5 个 judge × 3 个 benchmark × 3 个 axis × 多个指标，信息密度极高。建议拆分为 main results（LLMBar）和 confirmatory results（AlpacaEval/MT-Bench）两个表，或使用 heatmap 可视化。
2. **Figure 2 DAG 标注**：Figure 2 的 dashed orange S → Q path 标注为 "style bias"，但论文后续论证这个 path 可能反映 legitimate quality difference（formality 轴）。标注可能误导。
3. **术语一致性**："style bias" vs. "style preference" vs. "style sensitivity" 在论文中混用。"Bias" 暗示不合理的偏好，"preference" 更中性，"sensitivity" 最中性。建议统一。
4. **Section 3.5 Design Rationale 位置**：这一节解释为什么 DAG 不是 formal causal model。内容重要但放在 Method 末尾略显突兀，建议整合到 Section 3.3 或单独的 Discussion 段。
5. **Appendix 过多（A-S，19 个）**：虽然体现了严谨性，但 reviewer 难以逐一检查。建议在 main text 中更清晰地标注哪些 appendix 是 critical（如 A, J, R），哪些是 supplementary。

---

## 主要优势

1. **方法论严谨**：CSD 的三重控制（NLI 门控 + position control + same-text pairing）在 style bias 研究中是最严格的实验设计之一。Direction-aware gating（Section 3.2）解决了 bidirectional verification 的 inflation 问题，体现了对实验细节的深入思考。
2. **统计分析全面**：GEE 分解、FWER 校正、7 种 sensitivity methods（Table 2）、bootstrap attenuation 分析（Appendix J）、power analysis（Figure 4）、TOST equivalence testing（Appendix G）——统计处理的深度和广度在 NLP 实证论文中罕见。
3. **GEE per-axis confound 结构差异**：Table 3 揭示 verbosity 是 style-dominated（Style OR 5-13），formality 是 conditional effect（Style OR < 1 且 Originality OR 显著），register 也显示 varying structure。这是本文最有价值的增量发现，超越了 "Likert vs. pairwise" 的简单比较。
4. **跨 judge 复现**：4 个独立 provider 的 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制，覆盖不同架构和训练策略，增强了泛化性。
5. **诚实的 Limitations**：Quality-style confounding、construct validity、evaluator-producer bias 三个核心局限都被坦率讨论，未回避。

---

## Questions for Authors

1. 论文能否利用现有数据（特别是 Figure 4 的 power curve 和 bootstrap attenuation 的收敛行为）来区分 attenuation 和 construct divergence？如果是 attenuation，effect size d 应在更大 n 时趋向真实值；如果是 construct divergence，Likert d 应保持为零而非仅因 power 不足未检测到。Appendix J 的 bootstrap 数据是否支持其中一种？

2. CSD 的 NLI 门控对 formality 轴过滤掉了约 38% 的 pairs（100 → 62，Table 1）。这些被过滤的 pairs 是否系统性地对应更大的 style 效应（因为 style 改变大到影响了 content）？如果是，NLI 门控可能系统性地 underestimate style bias 的实际幅度。

3. Claude Sonnet 4 不展示 Blindspot 是否可能与其特定的 instruction-following 特性有关（如更严格地按 rubric 评分），而非反映 measurement mode 的本质属性？如果是，这是否意味着 Blindspot 可以通过改进 judge prompt 而非改变 measurement mode 来缓解？

---

## Missing References

本文的 Related Work 覆盖较为全面，但可考虑补充：

1. **Kim et al. (2024) "Prometheus 2"**：提出同时支持 Likert 和 pairwise 评估的统一 judge 模型，与本文讨论的 measurement mode divergence 直接相关——Prometheus 2 的训练是否消除了 Blindspot？
2. **Stureborg et al. (2024)** 已引用，但其关于 Likert inconsistency 的具体发现可以在 Related Work 中更详细地对比。
3. 心理测量学方面，**Luce (1959) "Individual Choice Behavior"** 关于 forced-choice models 的理论基础可能比 Thurstone (1927) 更直接相关，因为 Bradley-Terry model 是 Luce choice axiom 的特例。

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

_source line 1122 · 2026-05-22T22:46:31.542568+00:00_

Reviewer 2 审稿意见已收到（3.5/5 Borderline Conference）。等待 Reviewer 1 的审稿意见返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1123 · 2026-05-22T22:46:45.446707+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。方法论严谨（Soundness 4/5），但 Excitement 受限（3/5）。

三个 Must-Fix 问题：
1. **"Framework" 过度泛化**——仅 3 条表面风格轴（formality/verbosity/register）不足以支撑 framework 级别声明
2. **标题 "Blindspot" 隐含 attenuation 偏向**——与论文自己承认无法区分三种解释（attenuation/amplification/construct divergence）的立场矛盾
3. **核心发现的增量新颖性论证不足**——forced-choice > absolute rating 是 Thurstone (1927) 以来的经典结论，论文未充分论证 LLM judge 领域的 domain transfer 为何构成足够新颖性

主要优势：GEE per-axis confound 结构差异（Table 3）是本文最有价值的增量发现；统计分析深度在 NLP 实证论文中罕见；跨 4 个独立 judge 的复现增强了泛化性。

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

_source line 1124 · 2026-05-22T22:46:52.378591+00:00_

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


## Round 106

## Round 106

6 recorded events


### User

_source line 1125 · 2026-05-22T22:48:16.368527+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 核心发现（Likert Blindspot）由7种方法×4个judge×3个benchmark交叉验证支撑充分，GEE分解框架有方法论创新；但NLI gate人工验证标注一致性偏低（κ=0.44）、TOST等价检验SESOI缺乏外部校准，削弱了measurement methodology论文应有的方法论严密度。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心claim有7种方法交叉验证，GEE诊断完善（Appendix C/H）；但NLI gate标注一致性弱（κ=0.44）、TOST SESOI缺乏外部校准、bootstrap CI类型未指明 |
| Excitement | 3.5/5 | Likert Blindspot发现对NLG评估实践有直接影响；GEE per-axis decomposition揭示了style vs originality confound的轴间异质性，是genuine insight |
| Reproducibility | 4/5 | 模型版本（GPT-4o-2024-08-06等）、种子（seed 42）、代码/数据release承诺完整；bootstrap CI类型和LLM rewriting随机种子是两个报告缺口 |
| Confidence | 4/5 | 统计方法学和实验设计是我的专长领域 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] NLI Gate人工验证标注一致性不足，样本量偏小
- 具体位置：Section 5.4 (Robustness), Appendix S
- 问题：NLI gate是CSD pipeline的核心内容保持机制——如果gate不可靠，整条因果推断链的前提就不成立。两名标注者在50对样本上的Cohen's κ=0.44（moderate agreement）。论文指出Gwet's AC1=0.63缓解了prevalence效应，但AC1=0.63仍仅为"substantial"下限而非strong agreement。Gate-passed pairs的precision在majority vote下达到100%（Wilson CI [86.76, 100%]），这一数字看似优秀，但：(1) 仅基于25对gate-passed样本，置信区间下界86.76%意味着true precision可能低至87%；(2) κ=0.44的overall disagreement表明"内容保持"这一判断存在系统性主观分歧，gate threshold 0.90的calibration可靠性存疑。
- 为什么影响接收：对于以measurement methodology为核心贡献的论文，pipeline核心组件的validation标准应更高。如果有~13%的gate-passed pairs实际存在语义变化（precision下界暗示的可能性），则观测到的style bias可能部分被content差异contaminate。
- 建议修改方向：(1) 增加标注者至3人以上，报告Fleiss' κ；(2) 对A1-A2 disagreement cases进行定性error analysis——区分"真正语义变化"vs"风格变化被标注者误判为语义变化"；(3) 在不同NLI threshold（0.85, 0.90, 0.95）上报告precision和downstream BT结果的sensitivity（Appendix E已有Table 9的threshold sweep，但缺少human precision在不同threshold下的变化）。

**N2** [critical] TOST等价检验的SESOI Δ=15pp缺乏外部校准，负控制论证力不足
- 具体位置：Appendix G (Table 10), Section 5.1
- 问题：论文选择Δ=15pp（对应BT 65%）作为smallest effect size of interest，理由是"approximately where format preference would materially affect model rankings"——这是循环论证，用未经验证的实践判断来设定统计检验阈值。Table 10显示：在Δ=10pp下Claude Sonnet 4未通过等价检验（p=0.156, power=82%），BT仍为56.2%（高于50%）。这意味着"负控制"实际展现了non-trivial的format preference（6.2pp偏离chance），只是在一个相当宽松的Δ=15pp下才被判定为"等价"。论文对此是transparent的，但framing为"negative control"可能误导读者认为该judge不存在style bias。
- 为什么影响接收：负控制的有效性直接影响Likert Blindspot作为systematic phenomenon而非judge-specific artifact的论证强度。如果Claude Sonnet 4也存在中等偏好但只是在宽松阈值下被判为"等价"，那么论文的narrative需要调整。
- 建议修改方向：(1) 引用measurement theory或prior LLM evaluation文献中的effect size benchmarks来校准SESOI——例如参考Thurstone (1927)的JND框架或LLM evaluation中公认的meaningful effect thresholds；(2) 明确讨论Δ=10pp下的失败意味着什么；(3) 将Claude Sonnet 4从"negative control"重新framing为"weak-effect/attenuated-bias control"，更准确反映BT=56.2%的实际效应。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Bootstrap CI方法类型未报告
- 具体位置：Section P (Implementation Details), Appendix I (Table 11)
- 问题：论文报告"All bootstrap CIs use 10,000 pair-level resamples with seed 42"但未指明percentile method、BCa（bias-corrected and accelerated）还是其他变体。对于BT win probability这类bounded [0,1]参数，percentile intervals在小样本或偏斜分布下覆盖率可能不足，而BCa可纠正偏差和偏度。Table 11报告了大量CI，但读者无法评估其coverage properties。
- 建议：明确报告bootstrap CI类型。如果使用percentile method，至少在一个edge-case配置（如smallest n的condition）上与BCa对比。

**W2** [warning] Cross-rewriter independence验证仅覆盖一个轴
- 具体位置：Section 5.3, Appendix D, Tables 7-8
- 问题：Cross-rewriter验证（GPT-4o rewriter × Qwen3-32B judge）仅在verbosity轴完成。Formality轴——论文最核心的Blindspot发现轴——缺乏cross-rewriter验证。鉴于Qwen3-32B同时作为rewriter和judge存在evaluator-producer overlap（Appendix D估计Style OR降低22%），formality轴上的独立性验证对排除自我偏好混淆尤为重要。Table 7仅报告verbosity轴的NLI pass rate和BT。
- 建议：补充至少一个formality轴的cross-rewriter实验（如GPT-4o rewrite formality → Qwen3-32B judge），或充分论证为何verbosity轴的验证可泛化到formality轴。

**W3** [warning] Direction-aware NLI gate恢复的21对未经人工验证
- 具体位置：Appendix F (Direction-Aware Gate Validation)
- 问题：Direction-aware gating放宽了bidirectional entailment标准（仅要求forward entailment），从rejection中恢复了21对（3.2%）。论文通过统计一致性验证其合理性（BT方向一致，Δ=-1.1pp，95% CI含零），但这21对未经任何人工标注。主pipeline的gate-passed pairs至少有50对人工验证——放宽标准的部分理应接受至少同等水平的人工检查。
- 建议：对这21对进行人工抽检（至少1名标注者），报告content preservation precision。

**W4** [warning] BT模型unidimensionality假设仅在脚注讨论
- 具体位置：Page 6, Footnote 1
- 问题：BT模型假设单一潜在"quality"维度决定偏好。脚注承认此假设"standard in evaluation contexts but not empirically verified here"。但LLM judge在pairwise comparison中的决策可能同时受质量、流畅度、风格偏好等多维因素驱动。对于以measurement methodology为核心贡献的论文，这一假设的讨论不应止于脚注。如果judge在比较中同时权衡多个维度，BT参数的解释（"style bias的大小"）可能被confound。
- 建议：(1) 将IIA/unidimensionality讨论从脚注提升到Limitations或正文Section 3.5；(2) 讨论multi-dimensional preference下BT参数解释的变化。

**W5** [warning] 样本外部效度论证不足
- 具体位置：Section 3.4 (Experimental Setup)
- 问题：实验基于LLMBar的100个instruction-response pairs。LLMBar是一个用于检测LLM judge能否区分response质量的benchmark，其task分布（主要是短instruction-following tasks）可能不代表LLM judge的所有典型使用场景（如长文本摘要评估、对话质量评估、创意写作评估）。虽然LLMBar有human-verified quality labels且moderate size允许exhaustive pairwise evaluation，但论文仅通过AlpacaEval和MT-Bench的"confirmatory replication on selected configurations"来论证泛化性（Table 1脚注），且这些replication是partial的。
- 建议：在Limitations中更明确地讨论task domain的局限性，以及在哪些场景下Blindspot效应可能更强或更弱。

## 小问题（不影响接收）

- **M1** [format]: 正文可能微超8页——Conclusion (Section 6)最后一句"modes is the key next step."溢出到第9页Limitations之前。建议微调排版确保conclusion完整收在第8页内。
- **M2** [reproducibility]: LLM rewriting使用temperature=0.7（Section 3.1），但未报告是否固定decoding seed或使用多次采样取最佳结果。这影响exact reproducibility。
- **M3** [clarity]: Table 1中"Likert not"列和"1 = Blindspot case"标记逻辑需要对照正文才能理解，caption自解释性不足。
- **M4** [clarity]: Figure 4的y轴"Significance proxy"的定义在caption中模糊——如果是power-like的度量，应明确计算公式（如1 - p value的某种transformation）。
- **M5** [notation]: Table 3中Originality OR的asterisk标注与Style OR的不完全一致——建议统一显著性标记格式。

## Questions for Authors

1. **NLI threshold sensitivity的极端情况**：Appendix E (Table 9)显示所有44种judge×axis×threshold配置的BT都significant (p < 0.05)。能否确认是否存在**任何**NLI threshold使某些Blindspot case消失？如果所有threshold都robust，这实际上是论文的一个强优势，但当前呈现方式不够突出。

2. **Formality Style OR <1的解释**：Table 3中部分formality配置的Style OR<1（如GPT-4o form: OR=2.58但Qwen3 form: OR=2.31，Gemini form: OR=1.64）。更关键的是正文提到"formality is a conditional effect, register is style OR <1"。Style OR<1意味着style transformation反而**降低**了被选中的概率——这一反直觉结果如何机制性解释？

3. **Bootstrap attenuation的interpretation**：Appendix J显示d_median ≈ -0.017在所有样本量下近乎恒定。这是否意味着在此数据上Likert ATE是**真正的零效应**而非merely underpowered？如果是true null，这对"Blindspot的机制是attenuation还是amplification"的讨论意味着什么？

4. **GEE model的causal interpretation**：论文多处使用"causal"语言（如"Controlled Style Decomposition"中的"controlled"），但GEE模型本身是associational的。控制来自实验设计（rewriting保持content），而非统计模型。能否更精确地界定哪些inference是causal的、哪些是conditional association？

## Missing References

论文的相关工作覆盖面较好。建议补充：
- **Luce (1959)** "Individual Choice Behavior" — BT模型的理论基础文献，与论文对BT IIA假设的讨论直接相关
- **Bowman et al. (2015)** SNLI或**Williams et al. (2018)** MNLI — NLI gate是pipeline核心组件，但当前引用集中在DeBERTa技术文献，缺少对NLI任务本身局限性（如entailment与semantic equivalence的distinction）的文献支撑
- 最新版本的pairwise evaluation方法论综述（如有），特别是关于BT model在LLM evaluation中的validity conditions

## 主要优势

1. **多方法交叉验证的说服力**：Table 2中7种测量方法——3种Likert-based（interval scaling, ordinal regression, nonparametric rank）、2种pairwise-based（BT, signed-rank）——全部Likert方法fail、全部pairwise方法pass。这种一致性不太可能是统计偶然。

2. **GEE per-axis decomposition的方法论价值**：Table 3揭示verbosity是style-dominated（Style OR 5-13）而formality是conditional effect（受originality confound调节），这不仅描述了bias，更提供了可操作的诊断框架——告诉practitioners哪些轴的评估结果可以直接解读、哪些需要decomposition。

3. **统计诊断的深度远超typical submission**：GEE correlation structure comparison（Appendix C, 9个judge×axis cells的QIC对比）、Bradley-Terry goodness-of-fit（Appendix H, chi-squared tests + direction asymmetry）、formal power analysis（Appendix K, required n for 80% power）、bootstrap attenuation curve（Appendix J, 7个subsample sizes）——每一项都不是走流程，而是genuine diagnostic。

4. **实验设计的控制意识**：position-controlled comparison（Section 3.3, 每对出现两次消除position bias）、NLI gate（虽有验证不足的问题，但设计意图正确）、cross-rewriter validation（虽然范围有限）、negative control（虽然效应未完全消除）——展现了对confound识别的系统性思考。

5. **实际影响清晰**：论文明确指出"Likert-only audits may fail to register surface style-driven preferences that drive pairwise-based alignment pipelines (RLHF, DPO)"（Section 6），为NLG evaluation pipeline设计提供了直接可操作的警示。

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

_source line 1126 · 2026-05-22T22:48:51.996627+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] NLI Gate人工验证标注一致性不足，样本量偏小\n- Section 5.4, Appendix S\n- 两名标注者在50对样本上的Cohen's κ=0.44（moderate agreement）。AC1=0.63仅为\"substantial\"下限。Gate-passed pairs的precision在majority vote下100%（Wilson CI [86.76, 100%]），但仅基于25对样本。κ=0.44的overall disagreement表明\"内容保持\"判断存在系统性主观分歧。\n- 建议：(1) 增加标注者至3人以上，报告Fleiss' κ；(2) 对disagreement cases进行定性error analysis；(3) 在不同NLI threshold上报告precision和downstream BT的sensitivity。\n\n**N2** [critical] TOST等价检验的SESOI Δ=15pp缺乏外部校准，负控制论证力不足\n- Appendix G (Table 10), Section 5.1\n- Δ=15pp理由是\"approximately where format preference would materially affect model rankings\"——循环论证。Table 10显示Δ=10pp下Claude未通过等价检验（p=0.156），BT=56.2%（偏离chance 6.2pp）。\"负控制\"可能误导读者。\n- 建议：(1) 引用measurement theory中的effect size benchmarks校准SESOI；(2) 明确讨论Δ=10pp下的失败；(3) 将Claude从\"negative control\"重新framing为\"weak-effect/attenuated-bias control\"。\n\n### Should-Fix 问题\n\n**W1** Bootstrap CI方法类型未报告（percentile vs BCa）\n**W2** Cross-rewriter independence验证仅覆盖verbosity轴，formality轴缺乏验证\n**W3** Direction-aware NLI gate恢复的21对未经人工验证\n**W4** BT模型unidimensionality假设仅在脚注讨论，应提升到Limitations\n**W5** 样本外部效度论证不足（LLMBar task分布可能不代表所有典型使用场景）\n\n### Minor\n- M1: 正文可能微超8页\n- M2: LLM rewriting未报告decoding seed\n- M3: Table 1 caption自解释性不足\n- M4: Figure 4 y轴定义模糊\n- M5: Table 3显著性标记格式不一致\n\n### Missing References\n- Luce (1959) \"Individual Choice Behavior\"\n- Bowman et al. (2015) SNLI / Williams et al. (2018) MNLI\n- 最新pairwise evaluation方法论综述\n\n### 主要优势\n1. 7种方法交叉验证说服力强\n2. GEE per-axis decomposition方法论价值高\n3. 统计诊断深度远超typical submission\n4. 实验设计控制意识好\n5. 实际影响清晰"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] NLI Gate人工验证标注一致性不足，样本量偏小\n- Section 5.4, Appendix S\n- 两名标注者在50对样本上的Cohen's κ=0.44（moderate agreement）。AC1=0.63仅为\"substantial\"下限。Gate-passed pairs的precision在majority vote下100%（Wilson CI [86.76, 100%]），但仅基于25对样本。κ=0.44的overall disagreement表明\"内容保持\"判断存在系统性主观分歧。\n- 建议：(1) 增加标注者至3人以上，报告Fleiss' κ；(2) 对disagreement cases进行定性error analysis；(3) 在不同NLI threshold上报告precision和downstream BT的sensitivity。\n\n**N2** [critical] TOST等价检验的SESOI Δ=15pp缺乏外部校准，负控制论证力不足\n- Appendix G (Table 10), Section 5.1\n- Δ=15pp理由是\"approximately where format preference would materially affect model rankings\"——循环论证。Table 10显示Δ=10pp下Claude未通过等价检验（p=0.156），BT=56.2%（偏离chance 6.2pp）。\"负控制\"可能误导读者。\n- 建议：(1) 引用measurement theory中的effect size benchmarks校准SESOI；(2) 明确讨论Δ=10pp下的失败；(3) 将Claude从\"negative control\"重新framing为\"weak-effect/attenuated-bias control\"。\n\n### Should-Fix 问题\n\n**W1** Bootstrap CI方法类型未报告（percentile vs BCa）\n**W2** Cross-rewriter independence验证仅覆盖verbosity轴，formality轴缺乏验证\n**W3** Direction-aware NLI gate恢复的21对未经人工验证\n**W4** BT模型unidimensionality假设仅在脚注讨论，应提升到Limitations\n**W5** 样本外部效度论证不足（LLMBar task分布可能不代表所有典型使用场景）\n\n### Minor\n- M1: 正文可能微超8页\n- M2: LLM rewriting未报告decoding seed\n- M3: Table 1 caption自解释性不足\n- M4: Figure 4 y轴定义模糊\n- M5: Table 3显著性标记格式不一致\n\n### Missing References\n- Luce (1959) \"Individual Choice Behavior\"\n- Bowman et al. (2015) SNLI / Williams et al. (2018) MNLI\n- 最新pairwise evaluation方法论综述\n\n### 主要优势\n1. 7种方法交叉验证说服力强\n2. GEE per-axis decomposition方法论价值高\n3. 统计诊断深度远超typical submission\n4. 实验设计控制意识好\n5. 实际影响清晰"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-22T22:49:14.720149+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22723
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-22T22:49:14.871144+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] \"Framework\" 泛化声明与实际覆盖不匹配\n- Section 1 contributions 第一条；Section 6 Conclusion\n- CSD 定位为通用 per-axis style bias detection \"framework\"，但仅测试 formality、verbosity、register 三条轴（均为文本表层属性）。遇到 semantic-level 风格轴（hedging, humor, technicality）时 NLI 门控可能系统性拒绝合法 rewrite。\n- 建议：降级为 \"methodology\" 或增加非表面风格轴实验。\n\n**N2** [critical] 标题 \"Blindspot\" 隐含 attenuation 偏向，与三种解释并列的中立定位矛盾\n- Title, Abstract 第一句, Section 6 Conclusion\n- \"Blindspot\" 预设了 attenuation 解释，排斥 amplification 和 construct divergence。Introduction motivating example 暗示 Likert 判断是\"错误的\"。\n- 建议：考虑更中性标题；Introduction 的例子后立即引入替代解释。\n\n**N3** [critical] 核心发现的增量新颖性论证不足\n- Section 1, Section 2 (Measurement Sensitivity)\n- Forced-choice > absolute rating 是 Thurstone (1927) 经典结论。论文未充分论证在 LLM judge 领域\"重新发现\"这个现象的独立新颖性。\n- 建议：强调 GEE decomposition 的 per-axis confound structure 差异作为 LLM-specific finding；将 novelty 重心从\"发现 divergence\"转向\"quantifying and decomposing\"。\n\n### Should-Fix 问题\n\n**W1** Abstract 数字密度过高\n**W2** 与 RATE 的差异化论证薄弱\n**W3** LLMBar 样本量小（n=100）对统计推断的限制\n**W4** Construct divergence 解释发展不足\n**W5** Claude Sonnet 4 负控制结果的讨论不充分\n\n### Minor\n1. Table 1 信息密度过高\n2. Figure 2 DAG S→Q path 标注可能误导\n3. \"style bias\" vs \"style preference\" vs \"style sensitivity\" 术语混用\n4. Section 3.5 Design Rationale 位置突兀\n5. Appendix 过多（A-S, 19个）\n\n### Missing References\n- Kim et al. (2024) \"Prometheus 2\"\n- Luce (1959) \"Individual Choice Behavior\"\n- Stureborg et al. (2024) 的 Likert inconsistency 发现\n\n### 主要优势\n1. 方法论严谨（三重控制）\n2. 统计分析全面\n3. GEE per-axis confound 结构差异是最有价值的增量发现\n4. 跨4个独立judge复现\n5. 诚实的 Limitations"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] \"Framework\" 泛化声明与实际覆盖不匹配\n- Section 1 contributions 第一条；Section 6 Conclusion\n- CSD 定位为通用 per-axis style bias detection \"framework\"，但仅测试 formality、verbosity、register 三条轴（均为文本表层属性）。遇到 semantic-level 风格轴（hedging, humor, technicality）时 NLI 门控可能系统性拒绝合法 rewrite。\n- 建议：降级为 \"methodology\" 或增加非表面风格轴实验。\n\n**N2** [critical] 标题 \"Blindspot\" 隐含 attenuation 偏向，与三种解释并列的中立定位矛盾\n- Title, Abstract 第一句, Section 6 Conclusion\n- \"Blindspot\" 预设了 attenuation 解释，排斥 amplification 和 construct divergence。Introduction motivating example 暗示 Likert 判断是\"错误的\"。\n- 建议：考虑更中性标题；Introduction 的例子后立即引入替代解释。\n\n**N3** [critical] 核心发现的增量新颖性论证不足\n- Section 1, Section 2 (Measurement Sensitivity)\n- Forced-choice > absolute rating 是 Thurstone (1927) 经典结论。论文未充分论证在 LLM judge 领域\"重新发现\"这个现象的独立新颖性。\n- 建议：强调 GEE decomposition 的 per-axis confound structure 差异作为 LLM-specific finding；将 novelty 重心从\"发现 divergence\"转向\"quantifying and decomposing\"。\n\n### Should-Fix 问题\n\n**W1** Abstract 数字密度过高\n**W2** 与 RATE 的差异化论证薄弱\n**W3** LLMBar 样本量小（n=100）对统计推断的限制\n**W4** Construct divergence 解释发展不足\n**W5** Claude Sonnet 4 负控制结果的讨论不充分\n\n### Minor\n1. Table 1 信息密度过高\n2. Figure 2 DAG S→Q path 标注可能误导\n3. \"style bias\" vs \"style preference\" vs \"style sensitivity\" 术语混用\n4. Section 3.5 Design Rationale 位置突兀\n5. Appendix 过多（A-S, 19个）\n\n### Missing References\n- Kim et al. (2024) \"Prometheus 2\"\n- Luce (1959) \"Individual Choice Behavior\"\n- Stureborg et al. (2024) 的 Likert inconsistency 发现\n\n### 主要优势\n1. 方法论严谨（三重控制）\n2. 统计分析全面\n3. GEE per-axis confound 结构差异是最有价值的增量发现\n4. 跨4个独立judge复现\n5. 诚实的 Limitations"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-22T22:49:16.128006+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1256
}
```

</details>

---


### Assistant

_source line 1130 · 2026-05-22T22:49:20.339452+00:00_

交叉分享已发送给两位 Reviewer，等待逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1131 · 2026-05-22T22:49:22.804719+00:00_

[Reviewer 1 审稿结果]:
已清理完毕。审稿完成。

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

_source line 1132 · 2026-05-22T22:49:27.139922+00:00_

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


## Round 108

## Round 108

2 recorded events


### User

_source line 1133 · 2026-05-22T22:51:25.045203+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: "Framework"泛化声明与实际覆盖不匹配**
同意这是一个实质性overclaim问题。论文仅测试formality、verbosity、register三条表层文本属性轴，但Section 1 contributions第一条将CSD定位为通用"black-box framework for per-axis style bias detection"。R2指出的NLI gate对semantic-level风格轴（hedging, humor, technicality）的系统性拒绝风险是真实的——这类rewriting必然改变语义内容，NLI entailment threshold 0.90会大面积过滤。Limitations（page 9）虽提到"NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself"，但这讨论的是gate的false negative问题（放过了quality shift），而非R2指出的false positive问题（拒绝了合法的semantic-style rewriting）。这是两个不同的限制维度，论文只覆盖了一个。

降级为"methodology"或明确限定适用范围（"surface-level stylistic attributes amenable to content-preserving rewriting"）是合理建议。

**[REBUT] R2-N2: 标题"Blindspot"隐含attenuation偏向**
部分不同意R2对标题倾向性的判断。"Blindspot"描述的是观测层面的现象——Likert系统性地无法检测到pairwise能检测到的效应——而非机制层面的解释。无论底层机制是attenuation、amplification还是construct divergence，从practitioners的视角看，只用Likert就是存在一个"盲区"。这一术语选择类似于"survivorship bias"——它命名的是可观测模式，不预设产生机制。

然而，R2指出Introduction的motivating example（page 1: "What is the average height for a male?"的Likert vs pairwise比较）确实暗示Likert判断是"错误的"而pairwise是"正确的"，这一点我同意存在framing bias。Section 5.1 "Interpreting the divergence"列出了三种non-exclusive解释（Likert attenuation、pairwise amplification、construct divergence），但这个三方并列出现在全文第7页，距离读者形成第一印象已太晚。

建议保留标题"Blindspot"但在Introduction的motivating example之后**立即**（而非等到Section 5.1）简要引入三种解释的可能性，避免读者在前6页形成单向认知。这比改标题的成本更低且更有效。

**[AGREE] R2-N3: 核心发现的增量新颖性论证不足**
同意R2的判断，但程度上有所保留。R2正确指出forced-choice > absolute rating是Thurstone (1927)经典结论，"Likert Blindspot"在概念层面不是全新发现。Section 2 (Measurement Sensitivity in NLG Evaluation)引用了Stevens (1946)、Preston and Colman (2000)、Simms et al. (2019)、Krosnick (1999)等measurement theory文献，但**未充分论证在LLM judge这一特定领域重新量化此现象的independent contribution**。

不过，R2自己在"主要优势"第3条中承认"GEE per-axis confound结构差异是最有价值的增量发现"。我认为论文的真正novelty确实在于：(1) GEE decomposition揭示style vs originality confound的轴间异质性（Table 3: verbosity Style OR 5-13 vs formality conditional effect）；(2) 这种异质性对practitioners的可操作含义（哪些轴的评估结果可直接解读，哪些需要decomposition）。论文当前的framing将novelty重心放在"发现divergence"（标题和Abstract前两句），而非"quantifying and decomposing per-axis confound structures"。

建议按R2建议重构novelty narrative：标题和Abstract应突出decomposition的方法论贡献，将divergence发现降为motivating observation。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract数字密度过高**
Abstract包含η=0.17、>60%、7种统计方法、3个benchmark等密集数字。对于一篇以methodology为贡献的论文，Abstract应侧重conceptual message而非exhaustive数字。具体数字可移入Section 5的results presentation。

**[REBUT] R2-W2: 与RATE差异化论证薄弱**
不完全同意。论文在Section 2 (Style Bias Detection and Mitigation)和Section 1 contributions中对RATE的差异化论述包含三个维度：(1) CSD targets individual style axes rather than general attributes（Section 1: "per-axis style decomposition"）；(2) CSD measures bias through position-controlled pairwise comparison rather than Likert ATE（Section 3.3: Measurement Protocol详细描述了position-controlled design）；(3) CSD enforces content preservation via NLI entailment gating rather than post-hoc correction（Section 3.2: Content Preservation Verification，NLI gate的设计与RATE的post-hoc校正是根本性差异）。Section 5.1还直接与RATE对比了实验结果："Applying RATE's Likert ATE methodology... yields Cohen's d = 0.10, p = 0.33 (non-significant)"，而CSD的pairwise方法检测到63.0% formal preference (p = 0.001)。

差异化论证的问题更多在于Section 2的organization——RATE在Related Work中被分散在两处讨论，而非在一个dedicated对比段落中系统性地论证差异。建议在Section 2末尾增加一段集中对比，但认为现有内容已足够支撑差异化claim。

**[AGREE] R2-W3: LLMBar样本量（n=100）对统计推断的限制**
同意，且与我的审稿意见W5（样本外部效度论证不足）一致。100个instruction-response pairs虽然足以在统计上检测到observed effect sizes（Appendix K的power analysis确认了这一点），但LLMBar的task分布（短instruction-following tasks with human-verified quality labels）不代表LLM judge的全部使用场景。AlpacaEval和MT-Bench的partial replication（Table 1: "confirmatory replication on selected configurations"）提供了一定泛化支持，但这些replication是选择性的而非全面的。

**[AGREE] R2-W4: Construct divergence解释发展不足**
同意。Section 5.1列出了三种non-exclusive解释：(a) Likert attenuation, (b) pairwise amplification/forced-choice contamination, (c) construct divergence。但(c)仅用一句话概括（"the two formats measure different constructs: Likert captures absolute quality difference, while pairwise captures ordinal preference"），未发展为可检验的假说。如果construct divergence是正确解释，那么"Blindspot"就不是Likert的缺陷而是两种工具测量不同对象的自然结果——这对论文的practical implication narrative影响重大。论文应更深入地讨论在construct divergence解释下，practitioners应如何选择evaluation format。

**[AGREE] R2-W5: Claude Sonnet 4负控制结果的讨论不充分**
同意，且与我的N2（TOST Δ=15pp缺乏外部校准）直接相关。Claude Sonnet 4的BT=56.2%不是null effect，只是在Δ=15pp的宽松阈值下被判为"等价"。Appendix G对此是transparent的，但正文（Section 5.1后半部分提到Claude Sonnet 4时）的framing确实可能给读者留下"该judge无style bias"的印象。

---

### Minor Issues

**[AGREE] R2-Minor-1: Table 1信息密度过高**
Table 1在单个表中呈现5个judge × 3个axis × 3个benchmark × 4个统计量，确实需要仔细解码。拆分为per-benchmark子表或使用visual encoding（如heatmap）可提高可读性。

**[REBUT] R2-Minor-2: Figure 2 DAG S→Q path标注可能误导**
不认为这是误导。Figure 2 caption明确说明"Assumed data-generating process (design rationale, not a claim of perfect identification)"。DAG中S→Q path（style→quality）表示style rewriting可能inadvertently改变content quality——这正是NLI gate要阻断的通道。虚线标注已区分了被控制的vs未被控制的path。不过，如果R2指的是"S→Q"可能被误读为"style causes quality"（而非"rewriting mechanism may alter quality"），那一个更精确的edge label（如"rewriting mechanism"而非仅"S→Q"）可以澄清。

**[AGREE] R2-Minor-3: 术语混用**
"style bias"、"style preference"、"style sensitivity"在论文中确实未严格区分使用。作为measurement methodology论文，术语一致性对精确传达含义很重要。

**[AGREE] R2-Minor-4: Section 3.5 Design Rationale位置突兀**
Design Rationale放在Method末尾（Section 3.5, page 5）确实打断了从Method到Experiments的自然流。内容上是必要的（解释DAG假设和causal identification strategy），但位置可移到Section 3.1-3.2之间作为设计动机，或合并到一个introductory paragraph。

**[AGREE] R2-Minor-5: Appendix过多（A-S, 19个）**
19个appendix确实过多。但这与论文的统计严谨度是trade-off的两面——许多appendix包含重要的robustness checks和diagnostics。建议合并同类appendix（如将C/H合为"Model Diagnostics"，将E/F/N合为"NLI Gate Analyses"）以减少数量而不丢失内容。

---

### Missing References

**[AGREE]** Luce (1959) "Individual Choice Behavior" — 与我的审稿意见一致，这是BT模型的理论基础文献，直接相关于论文对IIA假设的讨论。

**[AGREE]** Stureborg et al. (2024) 的Likert inconsistency发现 — 论文在Section 2已引用Stureborg et al. (2024)讨论了"inconsistency and bias across evaluation formats"，但可以更深入地对比其specific findings与本文的Blindspot现象。

**[REBUT]** Kim et al. (2024) "Prometheus 2" — 该文献与本文的研究问题（measurement mode divergence）关联度有限。Prometheus 2聚焦于open-source judge model的evaluation quality，而非Likert-pairwise divergence问题。如果引用，应放在Section 2的judge model开发部分作为additional context，而非作为直接相关工作。

---

### 总结

R2的三个Must-Fix中，N1（framework overclaim）和N3（novelty framing）我完全同意，N2（标题bias）我部分反驳——"Blindspot"描述现象而非机制，但同意Introduction的framing确实偏向attenuation解释，应提前引入替代解释。Should-Fix中W2（RATE差异化）我认为现有论证已基本充分但organization可改善，其余W1/W3/W4/W5我均同意。

值得注意的是，R2给出Excitement 3/5（我给3.5/5），主要差异在于R2更重视novelty gap（Thurstone经典结论的重新发现），而我更看重GEE decomposition的方法论价值和practical implications。我认为如果论文按N3建议重构novelty narrative（从"发现divergence"转向"quantifying and decomposing per-axis confound structures"），Excitement评分可以提升。

两位Reviewer的共识区域：(1) framework overclaim需要降级或限定范围；(2) 负控制讨论不充分；(3) 样本外部效度有限；(4) GEE decomposition是最有价值的贡献。分歧主要在标题选择和novelty定位。

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

_source line 1134 · 2026-05-22T22:51:29.055248+00:00_

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


## Round 109

## Round 109

2 recorded events


### User

_source line 1135 · 2026-05-22T22:51:34.060369+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

R2的三个Must-Fix中：N1（framework overclaim）和N3（novelty framing）完全同意，N2（标题"Blindspot"隐含attenuation偏向）部分反驳——"Blindspot"描述可观测现象而非机制，但同意Introduction应提前引入替代解释。Should-Fix中仅W2（RATE差异化）部分反驳，其余均同意。

两位Reviewer的共识：framework需降级、负控制讨论不足、样本泛化性有限、GEE decomposition是核心贡献。

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

_source line 1136 · 2026-05-22T22:51:38.173550+00:00_

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


## Round 110

## Round 110

10 recorded events


### User

_source line 1137 · 2026-05-22T22:53:01.921475+00:00_

[Reviewer 2 审稿意见]:
## 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: NLI Gate 人工验证标注一致性不足，样本量偏小**

同意核心关切。κ=0.44（moderate）确实表明标注者对"内容保持"判断存在系统性分歧，50 对样本、2 名标注者的规模不足以全面评估 NLI gate 的可靠性。R1 的三条建议（增加标注者、disagreement error analysis、多阈值 precision-downstream sensitivity）都是合理的。

补充两点缓解观察：
1. 论文报告 BT 在 11 个 NLI 阈值上变化 ≤1pp（Appendix E, Table 9, page 11），说明 downstream metric 对阈值选择不敏感——即使 gate boundary 有标注分歧，最终结论稳健。
2. Gate-passed precision（majority vote 100%, Wilson CI [86.76, 100%]）比 overall κ 更直接衡量 gate 的有效性——gate 的目标是 high precision（不放入受污染的 pairs），而非 high recall。κ 被 prevalence skew 压低（AC1=0.63 部分修正了这一点）。

但这些缓解不足以完全消解 R1 的关切——sample size 确实是硬伤。特别是 R1 提出的"对 disagreement cases 进行定性 error analysis"是最有价值的建议：论文 Section 5.4 提到 Annotator 2 的 4 个 gate-passed disagreement 都涉及 verbosity condensation 的边界案例，但未展开分析这些边界案例是否系统性地偏向某个方向。

**[AGREE 部分，REBUT 部分] R1-N2: TOST SESOI Δ=15pp 缺乏外部校准**

**[AGREE]** Δ=15pp 的校准依据不充分。论文称"approximately where format preference would materially affect model rankings"——这是一个 pragmatic 标准，但未引用任何外部 benchmark 来支撑"15pp = materially meaningful"。R1 指出 Δ=10pp 下 Claude 未通过等价检验（Table 10, p=0.156），BT=56.2%（偏离 chance 6.2pp），这是一个重要的 sensitivity analysis 结果，应在正文中讨论而非仅在 Appendix G。同意将 Claude 从 "negative control" 重新 framing 为 "weak-effect control"。

**[REBUT]** 但不同意 R1 将此定性为"循环论证"。等价检验的 SESOI 选择在实践中很少有外部金标准——即使在临床试验中，SESOI 也常基于 "minimum clinically important difference" 的主观判断。论文的问题不是循环论证，而是**校准标准不够透明**：应明确讨论为什么 15pp 而非 10pp 或 20pp 是合理的分界线，例如引用 Chatbot Arena 或 AlpacaEval 的 BT 差异基准来校准。Appendix G 的 Table 10 实际上已经报告了 5/10/15/20pp 的 sensitivity，但正文未讨论这些不同阈值下的结论如何变化。

---

### Should-Fix 问题

**[AGREE] R1-W1: Bootstrap CI 方法类型未报告**

标准统计报告要求。Percentile bootstrap 和 BCa 在小样本下可产生不同 CI，应明确说明方法类型。

**[REBUT] R1-W2: Cross-rewriter independence 仅覆盖 verbosity 轴**

R1 似乎遗漏了 **Table 8（Appendix D, page 11）**，该表明确报告了 **formality 轴的 rewriter independence 验证**：使用 GPT-4o 作为独立 rewriter，在 Qwen3-32B judge 上进行 22× 重复实验。结果显示：NLI pass rate 90/100 (90%)，BT 64.4% [56.1, 72.8]，与 Qwen3-32B baseline (60.3%) 统计不可区分（Δ ≈ 2pp），且 Likert Blindspot 复现（p = 0.184, n.s.）。因此 cross-rewriter independence 实际上同时覆盖了 verbosity（Table 7）和 formality（Table 8）两条主要轴。

**[AGREE 部分] R1-W3: Direction-aware gate 恢复的 21 对未经人工验证**

原则上合理——新增的 21 对 pairs 应单独验证。但影响有限：(1) 这些 pairs 均通过 forward NLI entailment（original → rewrite），Direction-aware gate 仅放行 forward-pass + backward-fail 的 pairs，对应 compressions/entailing 变换（如缩写展开），这些 pairs 的内容保持性有理论预期；(2) Appendix F（page 11）报告 direction-aware gating 仅将 BT 从约 73.8% 微调至约 73.9%（Δ ≈ −1pp），对主结论影响极小。但为严谨性，人工验证这 21 对仍是值得的。

**[AGREE] R1-W4: BT unidimensionality 假设应提升到 Limitations**

同意。BT 模型假设 judge preference 沿单一维度排序——如果 judge 在不同 quality dimensions 上有不同偏好模式，单维 BT 可能混淆信号。论文仅在脚注（page 2）提到 BT 的 unidimensionality，这对论文的核心方法而言讨论不足。应在 Limitations 中讨论：(1) 什么情况下 unidimensionality 假设会被违反；(2) 违反时对 Blindspot 结论的影响方向。

**[AGREE 部分] R1-W5: 样本外部效度论证不足**

LLMBar 的 task 分布确实可能不代表所有 LLM judge 使用场景（如 code generation、safety evaluation、long-form summarization）。跨 benchmark 复现（AlpacaEval, MT-Bench）提供了部分缓解，但这三个 benchmark 都偏向 general instruction-following 任务。补充：我在自己的审稿中也提出了类似关切（我的 W3），且进一步指出 AlpacaEval 和 MT-Bench 仅使用"selected configurations"（Section 3.4），未充分讨论 MT-Bench 结果。

---

### Minor

**[REBUT] R1-M1: 正文可能微超 8 页**

重新检查 PDF：Section 6 Conclusion 的最后一句 "modes is the key next step." 出现在 page 9 的最顶行，Limitations 标题紧随其后。这意味着 Conclusion 确实有一行溢出到 page 9。但这是**一行文本的溢出**，而非实质性超页。需要作者确认 LaTeX 编译后的实际页面分布——如果确认溢出，可通过微调行距或删减一句话解决。R1 标记为 Minor 是恰当的，不应作为 rejection 理由，但作者确实需要在 camera-ready 前修复。

**[AGREE] R1-M2: LLM rewriting 未报告 decoding seed**

Section 3.1 报告了 temperature 0.7，但未报告 seed/top_p/random seed。可复现性的标准要求。Appendix P 列出了模型和 API 版本但也缺少 seed。

**[AGREE] R1-M3: Table 1 caption 自解释性不足**

我也在自己的审稿中独立提出了 Table 1 可读性问题（我的 Minor #1）。Table 1 信息密度极高，caption 应包含所有缩写解释和读法指南。

**[AGREE 部分] R1-M4: Figure 4 y 轴定义模糊**

Figure 4 的 caption 定义了 "Detection probability at observed effect magnitudes" 并给出了具体的 80% power crossings，但 y 轴标签本身仅写 "Significance probability"——与 caption 中的 "Detection probability" 不一致。同意需要统一术语。

**[AGREE] R1-M5: Table 3 显著性标记格式不一致**

如属实则应修正。统一使用 *, **, *** 或 p 值报告。

---

### Missing References

**[AGREE] Luce (1959) "Individual Choice Behavior"**

我在自己的审稿中也独立建议了这篇。Bradley-Terry 模型是 Luce choice axiom 的特例，论文使用 BT 模型但未引用其理论基础。

**[AGREE] Bowman et al. (2015) SNLI / Williams et al. (2018) MNLI**

论文使用 DeBERTa v3-large fine-tuned on MNLI（Section 3.2, page 9 Code and Data），但未引用 MNLI 的原始论文。这是基础性引用遗漏。

**[AGREE 部分] 最新 pairwise evaluation 方法论综述**

如果存在 2024-2025 年的系统性综述，引用会增强 Related Work 的完整性。但如果 R1 指的是特定论文，应明确指出。

---

### 主要优势

五条优势全部同意，与我独立审稿的判断高度一致。特别是：
- 优势 #2（GEE per-axis decomposition）和优势 #3（统计诊断深度）是我认为本文最有价值的贡献
- 优势 #1（7 种方法交叉验证）对应我审稿中的 Table 2 分析，确实增强了 sensitivity hierarchy 结论的可信度

---

### 与我自己审稿的交叉对比

| 维度 | R1 | R2（我） | 一致性 |
|------|-----|---------|--------|
| Overall | 3.5 | 3.5 | 完全一致 |
| 核心关切 | NLI gate 验证 + TOST 校准 | Novelty + Framing bias + Framework overclaim | 互补（R1 偏方法验证，R2 偏概念定位） |
| Claude 负控制 | Δ 校准不足 | 讨论不充分（model-specific vs. mode-intrinsic） | 互补 |
| Table 1 | caption 不足 | 可读性问题 | 一致 |
| 统计严谨性评价 | 正面 | 正面 | 一致 |
| GEE 贡献评价 | 方法论价值高 | 最有价值的增量发现 | 一致 |

两份审稿互补性强：R1 更关注方法论细节的可靠性（NLI gate 验证、TOST 校准、bootstrap CI 类型），R2 更关注概念层面的定位和新颖性（Thurstone domain transfer、framing bias、framework overclaim）。综合两份意见，论文的统计执行质量不是主要问题，但概念新颖性论证和关键方法验证细节需要加强。

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

_source line 1138 · 2026-05-22T22:53:31.794904+00:00_

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

_source line 1139 · 2026-05-22T22:53:31.896005+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T22:39:53.052615+00:00\", \"completed_at\": \"2026-05-22T22:43:15.458012+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"单页堆叠 3 个 display items（Table 1 全宽表 + Figure 3 散点图 + Table 2），页面极拥挤。Table 1 脚注字号很小（约 6pt），在密集排版中阅读困难。建议将 Table 2 移至 p.7 或 p.8 以平衡视觉密度\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"全页纯文本且包含 5 个 section/subsection heading（§3.4, §3.5, §4, §4.1, §5, §5.1），节奏感碎片化——审稿人翻到此页会感到 section 过于短小且缺乏视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item。虽然 Figure 1 在 p.2 出现（可接受），但若能将 Figure 1 或一个核心结果 teaser 提升到 p.1 右栏，会显著增强第一印象锚定效应\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3（Bradley-Terry win probabilities）的 axis labels 和 legend 字号偏小（目测 ~7pt），在 PDF 缩放至 100% 时可能需要读者放大。建议增大至 ≥8pt\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 脚注使用 †, ‡, § 等符号标记，但脚注文字压缩在表格底部与 Figure 3 之间的狭窄空间，容易被忽略\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（causal DAG）设计清晰，颜色区分合理（橙色 Rewrite 节点 vs 灰色观测节点），caption 自包含且适当谦虚（\\\"design rationale, not a claim of perfect identification\\\"）\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（detection probability power curves）多条曲线颜色可区分，但建议补充 marker shape 以增强打印友好性和色盲可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 管道图使用橙/蓝/绿配色，颜色区分度良好，但与后续 Figure 3-4 的配色方案不统一（各图独立配色）——跨图颜色语义一致性可改善\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-14\", \"message\": \"Appendix 表格密集（Tables 4-19），均使用 booktabs 风格，格式一致，最优值加粗标注，排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"末页（References 尾页）内容填充约 75%，可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

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


### Tool call

_source line 1140 · 2026-05-22T22:53:31.896384+00:00_

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

_source line 1141 · 2026-05-22T22:53:31.946739+00:00_

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

_source line 1142 · 2026-05-22T22:59:48.083228+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是'真正增量贡献'与 novelty 不足判断矛盾。Director 降为 Should-Fix。持续分歧点。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。两位共识：论文 novelty 重心应从'发现 divergence'转向'quantifying and decomposing per-axis confound structures'。GEE decomposition 是真正增量贡献但被 framing 遮蔽。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 14\n        action: \"重构 novelty narrative：Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 格式合规：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind ✓。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 格式合规：正文 ≤8 页 ✓，double-blind ✓，Limitations 合规 ✓。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Minor M1 指出 Conclusion 最后一行溢出到 p.9 Limitations 之前。R2 确认仅一行溢出，需 camera-ready 前修复。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2: register 轴所有改写用 Qwen3-32B 且无跨改写器验证，BT 结果也较弱。建议降级为 exploratory pilot axis。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W2) register 轴 evaluator-producer overlap 最严重，建议标注。R1 部分 AGREE——register 主结果来自其他 judge（GPT-4o, Llama-70B），核心 claim 建在 verbosity/formality 上。Director 列为 Minor。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 W2 指出 cross-rewriter 仅覆盖 verbosity，R2 REBUT 引用 Table 8 证明 formality 也已覆盖。Register 仍无独立 rewriter 验证。Director 确认 formality+verbosity 两轴已有 cross-rewriter 验证，register 未覆盖——接近解决。\"\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix。R2 交叉降为 Should-Fix。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W2: 50 对由 2 名标注员评估，κ=0.44 (moderate)，4 个分歧全在 verbosity condensation 上。Wilson CI 过宽。建议增加标注量。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W1)，R2 AGREE。50 对 κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。Annotator 2 precision 84.3% (CI 65.3-93.6%)。两位一致建议 ≥100 对 + 第 3 标注员。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Must-Fix N1——κ=0.44 表明'内容保持'判断存在系统性主观分歧，25 对 gate-passed 样本 Wilson CI 下界 86.76% 意味着 ~13% 可能存在语义变化。R2 AGREE，补充缓解观察（BT 在 11 个阈值上变化 ≤1pp），但同意 sample size 是硬伤。两位共识：增加标注者 + disagreement error analysis。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 14\n        action: \"增加至 ≥100 对 + 第 3 名标注员 + 对 verbosity condensation 分歧进行定性 error analysis\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 M1: Abstract 数字密度过高。与往轮一致。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W3) 再次提出数字密度过高。R1 REBUT——实证论文 Abstract 需要定量具体性，ARR 无限制。Director 列为 Minor 偏好建议。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Should-Fix W1（至少 6 个定量数字），R1 交叉 AGREE。两位共识：应保留 1-2 个关键数字，其余移入正文。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix——Appendix B direction asymmetry 暗示 IIA 违反。R2 交叉 [REBUT]——binary-choice BT 中 IIA 自动满足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 脚注 3：binary-choice BT 中 IIA structurally satisfied 的声明正确，方向异质性是 heterogeneous treatment effects 而非 IIA violation。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 R1 Minor (M3)：脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W4——unidimensionality 假设仅在脚注讨论，应提升到 Limitations。R2 交叉 AGREE。两位共识：讨论何时 unidimensionality 被违反 + 违反时对结论的影响方向。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。6 项 controls + Claude 负对照已部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 两位 Reviewer 最大共识问题。六项控制必要但不充分。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N1)——framing 90% 偏向 attenuation，construct divergence/amplification caveat 被隔离在末尾。R1 AGREE 问题存在但认为 Should-Fix。两位共识核心缺陷在解释框架而非实验设计。Director 升级为 Must-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N2——'Blindspot'命名预设 attenuation 解释。R1 部分 REBUT（描述现象非机制）但 AGREE Introduction 应提前引入替代解释。分歧点：标题是否需要更改。共识：Introduction motivating example 后应立即引入三种解释。\"\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Should-Fix (W3)，R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 优势 2 肯定：§3.5 明确声明因果免责，因果声明已诚实克制。\"\n      - round: 13\n        reviewers: [1]\n        note: \"R13 R1 Strength S6 肯定：§3.5 Design Rationale 明确免责，'Controlled' 限定为实验控制而非因果识别。R2 未在 round 13 提出此问题。接近解决。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。§3.5 Design Rationale 的因果免责已被两位认可。接近解决。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 R2-N1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R13 Director 降为 Should-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R14 两位共识 novelty 重心应转向 GEE decomposition。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R13 Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未独立提及。合并入 RD2-SF1。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: §5.1 已有讨论但 'Blindspot' 术语天然偏向。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 Should-Fix (W3)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：论文承认三种等效解释但标题和 framing 隐式偏向 attenuation。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: 合并入 R5-MF1。两位共识核心缺陷。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N2 + R2 Should-Fix W4。R1 AGREE construct divergence 讨论不足，但 REBUT 标题需要更改。共识：§5.1 需专段讨论 construct divergence 的含义和可检验预测。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: \"Acknowledged as limitation. Register is weakest axis.\"\n    resolution_round: 10\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识 Should-Fix：GPT-4o formality 13pp 与 Δ=15pp 仅差 2pp。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W2)，R2 AGREE。Δ=15pp 与 GPT-4o 最小偏差 13pp 重叠。两位一致建议 Δ 敏感性分析 (10/12/15/20pp) + 定量推导。Director 列为 Should-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Must-Fix N2——Δ=15pp 校准标准不够透明，Δ=10pp 下 Claude 未通过等价检验，BT=56.2% 非 null effect。R2 部分 AGREE（校准不足）但 REBUT '循环论证'标签——SESOI 在实践中很少有外部金标准。共识：正文需讨论不同 Δ 下的结论变化 + 将 Claude 重新 framing 为 'weak-effect control'。\"\n    action_items:\n      - round: 14\n        action: \"正文讨论 Δ=5/10/15/20pp 的 sensitivity + 将 Claude 从 'negative control' 重新 framing 为 'weak-effect/attenuated-bias control'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"Table 1 footnote 已有但选择理由缺失。\"\n      - round: 11\n        reviewers: [1]\n        note: \"register axis 的 n 值和 power 未明确报告。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：cross-benchmark 覆盖稀疏，verbosity 仅 1 个 cross-benchmark 数据点。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W1) cross-benchmark 覆盖稀疏。R1 部分 AGREE——建议限定泛化声明。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Should-Fix W3 (LLMBar n=100 局限) + R1 W5 (样本外部效度)。两位共识：AlpacaEval/MT-Bench 仅 'selected configurations'，未充分讨论。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 视觉审查：Figure 2 DAG 橙色/红色高亮路径色盲用户可能需额外辨认。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 视觉审查：Figure 2 caption 自包含性好，节点标签可读。未被 Reviewer 显式提及。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 视觉审查确认 Figure 2 设计清晰，颜色区分合理。R2 Minor-2 提到 S→Q path 标注可能误导，R1 REBUT。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R13 两位一致要求 Δ 敏感性分析。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R14 升级为 Must-Fix（R1 N2）。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含讨论。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W4: Appendix R formality→verbosity word count d=−0.23 超过 d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1)——GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Appendix R 已有 GEE covariate 控制缓解。接近解决。\"\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: n≈88 对 Likert power 严重不足。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 3 轴不足以支撑 'framework' 泛化。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W1/W5) cross-benchmark 覆盖稀疏 + 'framework' 过强。R1 部分 AGREE (W1) 但 REBUT W5——'framework' 是标准术语。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N1（'framework' overclaim），R1 交叉完全 AGREE。两位共识：3 条表面风格轴不足以支撑 framework 级别泛化。建议降级为 'methodology' 或限定适用范围。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests'，Gemini 为 confirmatory。\"\n    resolution_round: 10\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。GPT-4o cross-validation 部分缓解。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未显式提及。§5.4 人工标注 (50对) + GPT-4o cross-validation 部分缓解。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。接近解决。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 Q4: direction-aware NLI gate 恢复的 21 对 content quality 是否与 bidirectional-pass 对不同？\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Q3 + R2 AGREE：direction-aware gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？需验证。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W3——21 对未经人工验证。R2 部分 AGREE（影响有限但严谨性需要）。共识：至少 1 名标注者抽检。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"与 R6-SF3 合并。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W3: tone 轴失败说明适用性受限。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W5) 再次提出。R1 REBUT——'framework' 是 NLP 文献标准术语，3+1 轴结果证明 discriminative validity。Director 列为 Minor 偏好建议。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N1（升级为 critical），R1 完全 AGREE。两位共识：降级为 'methodology'/'experimental protocol' 或限定为 'surface-level stylistic attributes amenable to content-preserving rewriting'。\"\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 确认 §1 已有 GEE decomposition 引用。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W4)，R1 AGREE (minor 修正即可)。§1 开头 GPT-4o 例子隐含 Likert 判断是'错误的'，应添加一句 caveat。Director 列为 Minor。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N2 指出 Introduction motivating example 暗示 Likert 是'错误的'。R1 AGREE 存在 framing bias。共识：example 后应立即引入替代解释。\"\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"Limitations 已含承认。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 小问题 5: 选择理由缺失。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M2)，R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Limitations 已有承认。\"\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Limitations 承认即可。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Must-Fix。R2 交叉降为 Should-Fix。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W4)——未覆盖 instruction type/topic 分布、句法复杂度。R2 AGREE。Director 列为 Should-Fix。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。NLI 阈值 sweep 提供间接鲁棒性。\"\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix: 仅一个负控制不足以论证 Blindspot 是特定架构的产物。R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: R2 W5/N1 指出仅一个负控制模型。R1 W1 指出 TOST Δ=15pp 与 GPT-4o 最小 bias 几乎重叠。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N3)——未探讨 Claude 不受影响的机制。R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation。Director 降为 Should-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Should-Fix W5——Claude 负结果暗示 Blindspot 可能是 model-specific training artifact 而非 mode-intrinsic。R1 AGREE。共识：讨论 Claude 负结果对 'measurement-mode divergence' 叙事的含义。\"\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"论文 §2 已引用 Bojar et al. (2016)。\"\n    resolution_round: 12\n\n  # ============================================================\n  # Round 12 issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"Formality 轴 quality-style 混淆严重——GEE 显示 Orig OR ≥ Style OR（多配置）\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 N1 (critical) + R2 W1 (warning) 共同指出。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W3) Table 1 BT 是未调整聚合值。R2 AGREE。Director 列为 Should-Fix。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。论文已有 Appendix A GEE 调整分析。\"\n\n  - id: \"R12-N2\"\n    summary: \"Bootstrap CI 在 GEE 语境下的 pair-level resampling 合理性未论证\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 N2: §4.1 'All bootstrap CIs use 10,000 pair-level resamples' 但 GEE 使用 sandwich SE。Table 3 CI 来源不清。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 明确 bootstrap CI 用于 BT，GEE 用 sandwich SE。但 Table 3 CI 标注来源不清。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W1——bootstrap CI 方法类型（percentile vs BCa）未指明。R2 AGREE。共识：至少明确报告 CI 类型。\"\n\n  - id: \"R12-W1\"\n    summary: \"Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 W4: Appendix R Table 18 d=−0.23 > d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1)——GEE covariate 控制已缓解。R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。\"\n\n  - id: \"R12-REF1\"\n    summary: \"建议补充引用：Carterette et al. (2008), Sedoc & Ungar (2020), Deutsch et al. (2023)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"R13 确认：所有三篇已在论文中引用。\"\n    resolution_round: 13\n\n  # ============================================================\n  # Round 13 issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。R2 AGREE。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Table 1 脚注已有方向不对称信息。\"\n\n  - id: \"R13-M1\"\n    summary: \"Bootstrap CI 方法（percentile vs BCa）未指定\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M4)，R2 AGREE。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W1，R2 AGREE。升级为 Should-Fix。\"\n\n  - id: \"R13-M2\"\n    summary: \"Table 2 GEE (Likert-outcome) 与 Table 3 GEE (pairwise-outcome) 共享标签但模型不同\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M5)，R2 AGREE。建议在 Table 2 标注 'GEE (Likert-outcome)' 以区分。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。\"\n\n  # ============================================================\n  # Round 14 new issues\n  # ============================================================\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论，核心差异（cross-measurement mode comparison）被三点并列稀释。R1 REBUT（现有内容已基本充分但 organization 可改善）。Director 列为 Minor。\"\n\n  - id: \"R14-M1\"\n    summary: \"LLM rewriting 未报告 decoding seed / random seed\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1 Minor M2，R2 AGREE。Section 3.1 报告 temperature=0.7 但缺少 seed。\"\n\n  - id: \"R14-M2\"\n    summary: \"Figure 4 y 轴标签 'Significance probability' 与 caption 'Detection probability' 不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1 Minor M4，R2 AGREE。\"\n\n  - id: \"R14-M3\"\n    summary: \"'style bias' vs 'style preference' vs 'style sensitivity' 术语混用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 Minor-3，R1 AGREE。\"\n\n  - id: \"R14-REF1\"\n    summary: \"建议补充引用：Luce (1959), Williams et al. (2018) MNLI\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"两位独立建议 Luce (1959)——BT 模型理论基础。R1 建议 Williams et al. (2018) MNLI——NLI gate 的基础引用。\""
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是'真正增量贡献'与 novelty 不足判断矛盾。Director 降为 Should-Fix。持续分歧点。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。两位共识：论文 novelty 重心应从'发现 divergence'转向'quantifying and decomposing per-axis confound structures'。GEE decomposition 是真正增量贡献但被 framing 遮蔽。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 14\n        action: \"重构 novelty narrative：Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Two-layer mechanism properly framed\"\n    resolution_round: 1\n\n  - id: \"CROSS-2\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE with cross-judge validation\"\n    resolution_round: 1\n\n  - id: \"CROSS-3\"\n    summary: \"Likert ATE 方向反转\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Magnitude gap framing\"\n    resolution_round: 1\n\n  - id: \"CROSS-4\"\n    summary: \"Ordinal regression 必要\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Definitively resolved\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 2 issues\n  # ============================================================\n\n  - id: \"RD2-MF2\"\n    summary: \"Holm-Bonferroni 'nine tests' 错误\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Text fixed to '6 tests'. Holm 6-test: 4/6 significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF3\"\n    summary: \"单一 benchmark (LLMBar n=100) 不支撑全称论断\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"3 benchmarks x 3 judges. 6/7 biased cells BT significant.\"\n    resolution_round: 2\n\n  - id: \"RD2-MF4\"\n    summary: \"Abstract overclaim: 'dominant source' + verbosity category error\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Overclaim replaced in intro. Verbosity category error removed.\"\n    resolution_round: 2\n\n  - id: \"RD2-VIS\"\n    summary: \"主正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 格式检查确认正文 8 页合规。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 格式合规确认：正文 ≤8 页 ✓，匿名 ✓，Limitations 无新实验 ✓。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 格式合规：正文 ≤8 页 ✓，ACL 模板 ✓，double-blind ✓。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 格式合规：正文 ≤8 页 ✓，double-blind ✓，Limitations 合规 ✓。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Minor M1 指出 Conclusion 最后一行溢出到 p.9 Limitations 之前。R2 确认仅一行溢出，需 camera-ready 前修复。\"\n\n  - id: \"RD2-SF1\"\n    summary: \"Evaluator-producer 三角色 + 'independent' misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"cross-rewriter validation 仅覆盖 Qwen3-32B judge。22% Style OR 下降确认 inflation 存在。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 共识 Should-Fix：Blindspot 存在性 robust，但效应量有 ±20-25% rewriter-dependent 变异。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF4: 仅 Qwen3-32B judge 有 cross-rewriter 验证。效应量 ±22% rewriter-dependent 变异需显式承认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 Should-Fix: R1 指出仅 verbosity×Qwen3-32B 有替代 rewriter（R2 更正：formality+verbosity 两轴，但 register 未覆盖）。22% OR 下降不可忽略。两位共识 register 轴 evaluator-producer risk 最高。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W2: register 轴所有改写用 Qwen3-32B 且无跨改写器验证，BT 结果也较弱。建议降级为 exploratory pilot axis。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W2) register 轴 evaluator-producer overlap 最严重，建议标注。R1 部分 AGREE——register 主结果来自其他 judge（GPT-4o, Llama-70B），核心 claim 建在 verbosity/formality 上。Director 列为 Minor。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 W2 指出 cross-rewriter 仅覆盖 verbosity，R2 REBUT 引用 Table 8 证明 formality 也已覆盖。Register 仍无独立 rewriter 验证。Director 确认 formality+verbosity 两轴已有 cross-rewriter 验证，register 未覆盖——接近解决。\"\n\n  - id: \"RD2-SF2\"\n    summary: \"Direction-aware NLI verbosity allows quality-relevant additions\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 4\n    resolution: \"Appendix E validation: direction-aware gate extra 21 pairs show consistent preference direction.\"\n    resolution_round: 4\n\n  - id: \"RD2-SF3\"\n    summary: \"Scale granularity 未探讨 (1-10 vs 1-100)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"2 sentences added in Limitations.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF4\"\n    summary: \"缺乏 mitigation strategy\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Swiss-system O(n log n) sentence in Conclusion.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF5\"\n    summary: \"BT regularization unspecified + bootstrap resamples inconsistent\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Bootstrap unified to 10,000.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF6\"\n    summary: \"DAG missing position bias (P->Y) and rewrite artifact (R->Y)\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"P->Y + R->Y paths added to Figure 2.\"\n    resolution_round: 2\n\n  - id: \"RD2-SF7\"\n    summary: \"Novelty divergence: GEE contribution vs domain transfer\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Contributions restructured.\"\n    resolution_round: 2\n\n  - id: \"RD2-M1\"\n    summary: \"Figure 4 (power_curve) PLACEHOLDER watermark\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Real matplotlib figure replaced placeholder.\"\n    resolution_round: 2\n\n  - id: \"RD2-M2\"\n    summary: \"Table 1 Qwen3-32B Register missing Cohen's d\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"d=-0.073 added.\"\n    resolution_round: 2\n\n  - id: \"RD2-M3\"\n    summary: \"Citation author mismatches\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Corrected.\"\n    resolution_round: 2\n\n  - id: \"RD2-M4\"\n    summary: \"No code/data availability statement\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"'Code and Data' section added.\"\n    resolution_round: 2\n\n  - id: \"RD2-REF\"\n    summary: \"Missing refs: Chatbot Arena, Justice or Prejudice\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"Both references added.\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues\n  # ============================================================\n\n  - id: \"R3-N1\"\n    summary: \"因果/反事实术语与方法论强度不匹配\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Title: no causal language. §3.5 renamed 'Design Rationale'. DAG has residual confounding dashed line.\"\n    resolution_round: 4\n\n  - id: \"R3-N2\"\n    summary: \"Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Formality independence added. Register acknowledged as limitation.\"\n    resolution_round: 4\n\n  - id: \"R3-N3\"\n    summary: \"'Blindspot' framing 将统计功效差异包装为质性 blindspot\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Reframed as 'measurement attenuation across a severity spectrum'.\"\n    resolution_round: 4\n\n  - id: \"R3-N4\"\n    summary: \"证据基础偏窄，practical recommendation scope 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Contribution 4 加了 'in typical evaluation settings (n<500)' 限定。\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"NLI gate 验证使用同一模型族，precision 可能被高估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Full 200-pair GPT-4o independent validation completed.\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Direction-aware NLI 额外纳入的 21% pairs 内容保持质量未验证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Appendix E: extra 21 pairs BT 73.8% vs 78.5%, consistent direction.\"\n    resolution_round: 4\n\n  - id: \"R3-W3\"\n    summary: \"缺少人工评估验证 rewriting 质量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"共识 Must-Fix。50 对 pass/fail 样本 2+ annotator 评估即可满足。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 两位共同指向：增加 human evaluation 是最大可 actionable 改进。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 MF1 (critical): 持续 7 轮未解决。两位 Reviewer 交叉共识：human evaluation 是 4.0 的关键路径。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 将 NLI gate 50 对人工标注列为 Must-Fix。R2 交叉降为 Should-Fix。论文 §5.4 报告 50 对 100% precision，但规模仍不足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W2: 50 对由 2 名标注员评估，κ=0.44 (moderate)，4 个分歧全在 verbosity condensation 上。Wilson CI 过宽。建议增加标注量。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W1)，R2 AGREE。50 对 κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。Annotator 2 precision 84.3% (CI 65.3-93.6%)。两位一致建议 ≥100 对 + 第 3 标注员。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Must-Fix N1——κ=0.44 表明'内容保持'判断存在系统性主观分歧，25 对 gate-passed 样本 Wilson CI 下界 86.76% 意味着 ~13% 可能存在语义变化。R2 AGREE，补充缓解观察（BT 在 11 个阈值上变化 ≤1pp），但同意 sample size 是硬伤。两位共识：增加标注者 + disagreement error analysis。\"\n    action_items:\n      - round: 6\n        action: \"准备 50 对 NLI pass/fail 样本 + 标注模板\"\n        assigned_to: agent\n        status: done\n      - round: 14\n        action: \"增加至 ≥100 对 + 第 3 名标注员 + 对 verbosity condensation 分歧进行定性 error analysis\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R3-W4\"\n    summary: \"Confound gradient 可能反映 rewriting difficulty 而非 axis 固有属性\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Limitations 新增相关段落。\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"GEE 'decomposition' 在残余 confounding 下有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Changed to 'GEE Conditional Decomposition'. Text clarifies 'partial rather than clean separation'.\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"小样本 OR 估计不稳定\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"n=355 result prominent in Table 3.\"\n    resolution_round: 4\n\n  - id: \"R3-W7\"\n    summary: \"Related Work 引用数量偏少\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Citations expanded from 27 to 44.\"\n    resolution_round: 4\n\n  - id: \"R3-W8\"\n    summary: \"NLI gate FN 可能引入 systematic selection bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Cliff's delta=+0.45 for verbosity-rejected pairs. Estimates characterized as lower bounds.\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"Claude 作为 negative control 的双重解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"TOST equivalence testing added. Abstract changed 'confirms' to 'supports'.\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"Table 1 Holm-Bonferroni p-value 标注不够直觉\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"Table 1 footnotes updated.\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Abstract 过长过密\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"两位再次一致指出 Abstract 过密。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 fresh review 未显式提出 Abstract 过密问题。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未提及 Abstract 密度问题。P1 重写后可能已缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 列为 Should-Fix（W1），R1 交叉 [AGREE]。数字堆砌影响可读性，建议保留 1-2 个最有力数字。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 M1: Abstract 数字密度过高。与往轮一致。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W3) 再次提出数字密度过高。R1 REBUT——实证论文 Abstract 需要定量具体性，ARR 无限制。Director 列为 Minor 偏好建议。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Should-Fix W1（至少 6 个定量数字），R1 交叉 AGREE。两位共识：应保留 1-2 个关键数字，其余移入正文。\"\n\n  - id: \"R3-M4\"\n    summary: \"Orphan bib entries\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    resolution: \"hoenig2001abuse cited via citealt. Not orphan.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues\n  # ============================================================\n\n  - id: \"R4-N1\"\n    summary: \"Bradley-Terry IIA 假设未检验\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 Should-Fix：Appendix H formality 方向异质性挑战 IIA。\"\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。§4.1 footnote 已承认 direction asymmetry。可能接近解决。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 分歧：R1 列为 Must-Fix——Appendix B direction asymmetry 暗示 IIA 违反。R2 交叉 [REBUT]——binary-choice BT 中 IIA 自动满足。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 脚注 3：binary-choice BT 中 IIA structurally satisfied 的声明正确，方向异质性是 heterogeneous treatment effects 而非 IIA violation。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 R1 Minor (M3)：脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W4——unidimensionality 假设仅在脚注讨论，应提升到 Limitations。R2 交叉 AGREE。两位共识：讨论何时 unidimensionality 被违反 + 违反时对结论的影响方向。\"\n\n  - id: \"R4-N2\"\n    summary: \"Introduction 'four critical gaps' 构造有 cherry-picking 嫌疑\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Reframed as integrative positioning.\"\n    resolution_round: 4\n\n  - id: \"R4-W1\"\n    summary: \"Conclusion 仅一句话\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Conclusion expanded.\"\n    resolution_round: 4\n\n  - id: \"R4-M1\"\n    summary: \"Table 1 Likert d 负值含义未解释\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Footnote added.\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"'Interventional Design' 标题措辞与 evidence 强度不匹配\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Renamed to 'Design Rationale'.\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 5 issues\n  # ============================================================\n\n  - id: \"R5-MF1\"\n    summary: \"遗漏关键矛盾文献 Comparative Trap (Jeong et al., 2025)\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"§5.2 已加 6 项 amplification controls。从 critical 降级为 Should-Fix。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF1: 检测 vs 放大歧义仍为核心。6 项 controls + Claude 负对照已部分缓解。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: detection vs. amplification 成为两位 Reviewer 的最大共识问题。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 两位 Reviewer 最大共识问题。六项控制必要但不充分。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N1)——framing 90% 偏向 attenuation，construct divergence/amplification caveat 被隔离在末尾。R1 AGREE 问题存在但认为 Should-Fix。两位共识核心缺陷在解释框架而非实验设计。Director 升级为 Must-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N2——'Blindspot'命名预设 attenuation 解释。R1 部分 REBUT（描述现象非机制）但 AGREE Introduction 应提前引入替代解释。分歧点：标题是否需要更改。共识：Introduction motivating example 后应立即引入三种解释。\"\n\n  - id: \"R5-MF2\"\n    summary: \"NLI gate 'approximates the do-operator' 声明过强\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 7\n        reviewers: [1]\n        note: \"§3.5 因果语言校准良好。原始 'do-operator' 语言已修复。\"\n      - round: 10\n        reviewers: [2]\n        note: \"R10 M2: 'Controlled' 和 'interventional' 语言暗示过强因果识别。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Should-Fix (W3)，R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 优势 2 肯定：§3.5 明确声明因果免责，因果声明已诚实克制。\"\n      - round: 13\n        reviewers: [1]\n        note: \"R13 R1 Strength S6 肯定：§3.5 Design Rationale 明确免责，'Controlled' 限定为实验控制而非因果识别。R2 未在 round 13 提出此问题。接近解决。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。§3.5 Design Rationale 的因果免责已被两位认可。接近解决。\"\n\n  - id: \"R5-SF1\"\n    summary: \"'first systematic quantitative verification' overclaim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"共识：'the first' → 'a unified framework'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1 处理。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R11 共识：'first' 需限定为 'first for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 R2-N1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R13 Director 降为 Should-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"合并入 R2-N1。R14 两位共识 novelty 重心应转向 GEE decomposition。\"\n\n  - id: \"R5-SF2\"\n    summary: \"Evaluator-producer confound 主文缺 caveat\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 12\n        reviewers: [2]\n        note: \"合并入 RD2-SF1。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 RD2-SF1。R13 Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未独立提及。合并入 RD2-SF1。\"\n\n  - id: \"R5-SF3\"\n    summary: \"Judge 覆盖面 framing 'across three judges' 有误导性\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 target judges (+ Gemini confirmatory) now cover the claim.\"\n    resolution_round: 6\n\n  - id: \"R5-SF4\"\n    summary: \"GEE verbosity 'confound-free' 措辞过强\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"论文已使用 'style-dominated' 而非 'confound-free'。\"\n    resolution_round: 6\n\n  - id: \"R5-SF5\"\n    summary: \"Sensitivity hierarchy (Table 2) 仅在 formality 单轴展示\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix P (Table 13) 补充了 verbosity 轴的 7 method sensitivity analysis。\"\n    resolution_round: 6\n\n  - id: \"R5-SF6\"\n    summary: \"Measurement attenuation vs construct difference 主文呈现不平衡\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"标题和 Abstract framing 偏向 attenuation。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 Q3: §5.1 已有讨论但 'Blindspot' 术语天然偏向。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R2 Should-Fix (W3)，R1 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：论文承认三种等效解释但标题和 framing 隐式偏向 attenuation。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: 合并入 R5-MF1。两位共识核心缺陷。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N2 + R2 Should-Fix W4。R1 AGREE construct divergence 讨论不足，但 REBUT 标题需要更改。共识：§5.1 需专段讨论 construct divergence 的含义和可检验预测。\"\n\n  - id: \"R5-M1\"\n    summary: \"NLI 阈值 sensitivity sweep 仅 4 个离散点\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"Appendix E Table 8 现有 11 个阈值点。\"\n    resolution_round: 6\n\n  - id: \"R5-M2\"\n    summary: \"Cross-rewriter independence test 缺 register 轴\"\n    category: experiment\n    severity: info\n    status: wont_fix\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: \"Acknowledged as limitation. Register is weakest axis.\"\n    resolution_round: 10\n\n  - id: \"R5-M3\"\n    summary: \"Claude TOST 'no bias' 措辞需改为 'failed to detect bias at current n'\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8 升级 Must-Fix。Δ=15pp 几乎涵盖最小 confirmed bias。\"\n      - round: 10\n        reviewers: [1]\n        note: \"R10 SF3: Δ=15pp 偏宽。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: 循环论证（用自己效应量定义等价边界），15pp≈d=0.43 属 medium effect 偏宽。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识 Should-Fix：GPT-4o formality 13pp 与 Δ=15pp 仅差 2pp。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W2)，R2 AGREE。Δ=15pp 与 GPT-4o 最小偏差 13pp 重叠。两位一致建议 Δ 敏感性分析 (10/12/15/20pp) + 定量推导。Director 列为 Should-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Must-Fix N2——Δ=15pp 校准标准不够透明，Δ=10pp 下 Claude 未通过等价检验，BT=56.2% 非 null effect。R2 部分 AGREE（校准不足）但 REBUT '循环论证'标签——SESOI 在实践中很少有外部金标准。共识：正文需讨论不同 Δ 下的结论变化 + 将 Claude 重新 framing 为 'weak-effect control'。\"\n    action_items:\n      - round: 14\n        action: \"正文讨论 Δ=5/10/15/20pp 的 sensitivity + 将 Claude 从 'negative control' 重新 framing 为 'weak-effect/attenuated-bias control'\"\n        assigned_to: paper_agent\n        status: in_progress\n\n  - id: \"R5-M4\"\n    summary: \"Table 1 实验矩阵空 cell 未解释\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"Table 1 footnote 已有但选择理由缺失。\"\n      - round: 11\n        reviewers: [1]\n        note: \"register axis 的 n 值和 power 未明确报告。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 两位共识：cross-benchmark 覆盖稀疏，verbosity 仅 1 个 cross-benchmark 数据点。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W1) cross-benchmark 覆盖稀疏。R1 部分 AGREE——建议限定泛化声明。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Should-Fix W3 (LLMBar n=100 局限) + R1 W5 (样本外部效度)。两位共识：AlpacaEval/MT-Bench 仅 'selected configurations'，未充分讨论。\"\n\n  - id: \"R5-M5\"\n    summary: \"DAG (Figure 2) dashed/solid edges 黑白打印不清\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: []\n        note: \"R12 视觉审查：Figure 2 DAG 橙色/红色高亮路径色盲用户可能需额外辨认。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 视觉审查：Figure 2 caption 自包含性好，节点标签可读。未被 Reviewer 显式提及。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 视觉审查确认 Figure 2 设计清晰，颜色区分合理。R2 Minor-2 提到 S→Q path 标注可能误导，R1 REBUT。\"\n\n  - id: \"R5-REF1\"\n    summary: \"遗漏引用：Jeong et al. (2025), Stureborg et al. (2024), Park et al. (2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"所有三篇引用已加入 Related Work §2。\"\n    resolution_round: 6\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n\n  - id: \"R6-SF1\"\n    summary: \"TOST equivalence bound Δ=15pp 缺乏独立外部 justification\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1]\n        note: \"合并入 R5-M3 讨论。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R13 两位一致要求 Δ 敏感性分析。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"合并入 R5-M3。R14 升级为 Must-Fix（R1 N2）。\"\n\n  - id: \"R6-SF2\"\n    summary: \"Identification assumption (iii) 讨论不充分——cross-axis contamination\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF6: cross-axis interaction 未测试。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。Limitations 已含讨论。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 W4: Appendix R formality→verbosity word count d=−0.23 超过 d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1)——GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Appendix R 已有 GEE covariate 控制缓解。接近解决。\"\n\n  - id: \"R6-SF3\"\n    summary: \"样本量偏小且 scaled replication 覆盖面窄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2: 仅 2+1 axes 限制泛化。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: n≈88 对 Likert power 严重不足。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: 3 轴不足以支撑 'framework' 泛化。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W1/W5) cross-benchmark 覆盖稀疏 + 'framework' 过强。R1 部分 AGREE (W1) 但 REBUT W5——'framework' 是标准术语。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N1（'framework' overclaim），R1 交叉完全 AGREE。两位共识：3 条表面风格轴不足以支撑 framework 级别泛化。建议降级为 'methodology' 或限定适用范围。\"\n\n  - id: \"R6-M1\"\n    summary: \"Appendix Table 5 (GEE CI) 部分条目缺失 95% CI\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 10\n    resolution: \"R9/R10 检查确认 Appendix C Table 5 已有完整 12 行 CI。\"\n    resolution_round: 10\n\n  - id: \"R6-REF1\"\n    summary: \"建议补充引用：Shi et al. (2024), Bavaresco et al. (2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"论文 Related Work §2 已引用。\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 7 issues\n  # ============================================================\n\n  - id: \"R7-W2\"\n    summary: \"Section 4.1 与 Table 1 关于 register 分类矛盾——primary family 定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 10\n    resolution: \"§4.1 明确 'six tests'，Gemini 为 confirmatory。\"\n    resolution_round: 10\n\n  - id: \"R7-W4\"\n    summary: \"NLI FNR 8.4% 估计使用同一 Qwen3-32B 模型，存在循环性\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。GPT-4o cross-validation 部分缓解。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未显式提及。§5.4 人工标注 (50对) + GPT-4o cross-validation 部分缓解。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。接近解决。\"\n\n  - id: \"R7-W5\"\n    summary: \"Verbosity direction-aware NLI gate 17.4% FPR 未报告\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 未显式提及。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未显式提及。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 Q4: direction-aware NLI gate 恢复的 21 对 content quality 是否与 bidirectional-pass 对不同？\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Q3 + R2 AGREE：direction-aware gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？需验证。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W3——21 对未经人工验证。R2 部分 AGREE（影响有限但严谨性需要）。共识：至少 1 名标注者抽检。\"\n\n  - id: \"R7-REF1\"\n    summary: \"遗漏引用：Tripathi et al. (2025)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 9\n    resolution: \"论文 §5.1 已引用 Tripathi et al. (2025)。\"\n    resolution_round: 9\n\n  # ============================================================\n  # Round 8 issues\n  # ============================================================\n\n  - id: \"R8-W1\"\n    summary: \"3 个风格轴限制 'framework' 级别泛化——需从 'framework' 降为 'methodology'\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 SF2 再次确认。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"与 R6-SF3 合并。\"\n      - round: 12\n        reviewers: [2]\n        note: \"R12 R2 W3: tone 轴失败说明适用性受限。\"\n      - round: 13\n        reviewers: [2]\n        note: \"R13: R2 Should-Fix (W5) 再次提出。R1 REBUT——'framework' 是 NLP 文献标准术语，3+1 轴结果证明 discriminative validity。Director 列为 Minor 偏好建议。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N1（升级为 critical），R1 完全 AGREE。两位共识：降级为 'methodology'/'experimental protocol' 或限定为 'surface-level stylistic attributes amenable to content-preserving rewriting'。\"\n\n  - id: \"R8-W2\"\n    summary: \"生态效度讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Limitations 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W3\"\n    summary: \"Rewriting artifact 的 style-specific polishing interaction 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 10\n    resolution: \"Appendix O 已含相关讨论。\"\n    resolution_round: 10\n\n  - id: \"R8-W4\"\n    summary: \"Introduction motivating example 未 acknowledge formality-quality nuance\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: []\n        note: \"R10 确认 §1 已有 GEE decomposition 引用。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Should-Fix (W4)，R1 AGREE (minor 修正即可)。§1 开头 GPT-4o 例子隐含 Likert 判断是'错误的'，应添加一句 caveat。Director 列为 Minor。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Must-Fix N2 指出 Introduction motivating example 暗示 Likert 是'错误的'。R1 AGREE 存在 framing bias。共识：example 后应立即引入替代解释。\"\n\n  - id: \"R8-REF1\"\n    summary: \"建议补充引用：Girrbach et al. 'Likert or Not'\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"Phantom reference.\"\n    resolution_round: 8\n\n  # ============================================================\n  # Round 10 issues\n  # ============================================================\n\n  - id: \"R10-N1\"\n    summary: \"100-point continuous Likert 实验仅用单一 judge（Qwen3-32B）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Minor。Limitations 承认即可。\"\n      - round: 11\n        reviewers: []\n        note: \"Limitations 已含承认。\"\n      - round: 12\n        reviewers: [1]\n        note: \"R12 R1 小问题 5: 选择理由缺失。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M2)，R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Limitations 已有承认。\"\n\n  - id: \"R10-N2\"\n    summary: \"NLI gate 44% 拒绝率 selection bias 仅检查 4 个 surface covariates\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Limitations 承认即可。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11: R1 Must-Fix。R2 交叉降为 Should-Fix。\"\n      - round: 12\n        reviewers: []\n        note: \"R12 未显式提及。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W4)——未覆盖 instruction type/topic 分布、句法复杂度。R2 AGREE。Director 列为 Should-Fix。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。NLI 阈值 sweep 提供间接鲁棒性。\"\n\n  - id: \"R10-REF1\"\n    summary: \"建议补充引用：Simms et al. (2019), Polo et al. (2024), Kocmi & Federmann (2023)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 10\n    resolution: null\n    resolution_round: null\n\n  # ============================================================\n  # Round 11 new issues\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"Negative control 仅 Claude Sonnet 4 一个模型，不足以论证 Blindspot 的架构特异性\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix: 仅一个负控制不足以论证 Blindspot 是特定架构的产物。R2 交叉 [AGREE]。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12: R2 W5/N1 指出仅一个负控制模型。R1 W1 指出 TOST Δ=15pp 与 GPT-4o 最小 bias 几乎重叠。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R2 Must-Fix (N3)——未探讨 Claude 不受影响的机制。R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation。Director 降为 Should-Fix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R2 Should-Fix W5——Claude 负结果暗示 Blindspot 可能是 model-specific training artifact 而非 mode-intrinsic。R1 AGREE。共识：讨论 Claude 负结果对 'measurement-mode divergence' 叙事的含义。\"\n\n  - id: \"R11-REF1\"\n    summary: \"建议补充引用：Bojar et al. (2016) WMT human evaluation\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"论文 §2 已引用 Bojar et al. (2016)。\"\n    resolution_round: 12\n\n  # ============================================================\n  # Round 12 issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"Formality 轴 quality-style 混淆严重——GEE 显示 Orig OR ≥ Style OR（多配置）\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 N1 (critical) + R2 W1 (warning) 共同指出。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Should-Fix (W3) Table 1 BT 是未调整聚合值。R2 AGREE。Director 列为 Should-Fix。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。论文已有 Appendix A GEE 调整分析。\"\n\n  - id: \"R12-N2\"\n    summary: \"Bootstrap CI 在 GEE 语境下的 pair-level resampling 合理性未论证\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 N2: §4.1 'All bootstrap CIs use 10,000 pair-level resamples' 但 GEE 使用 sandwich SE。Table 3 CI 来源不清。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 明确 bootstrap CI 用于 BT，GEE 用 sandwich SE。但 Table 3 CI 标注来源不清。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W1——bootstrap CI 方法类型（percentile vs BCa）未指明。R2 AGREE。共识：至少明确报告 CI 类型。\"\n\n  - id: \"R12-W1\"\n    summary: \"Cross-axis contamination: formality→verbosity word count shift d=−0.23 超过论文自设 negligible 标准\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1 W4: Appendix R Table 18 d=−0.23 > d<0.20 标准。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13: R1 Minor (M1)——GEE covariate 控制已缓解。R2 AGREE。Director 列为 Minor。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。\"\n\n  - id: \"R12-REF1\"\n    summary: \"建议补充引用：Carterette et al. (2008), Sedoc & Ungar (2020), Deutsch et al. (2023)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"R13 确认：所有三篇已在论文中引用。\"\n    resolution_round: 13\n\n  # ============================================================\n  # Round 13 issues\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。R2 AGREE。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Table 1 脚注已有方向不对称信息。\"\n\n  - id: \"R13-M1\"\n    summary: \"Bootstrap CI 方法（percentile vs BCa）未指定\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M4)，R2 AGREE。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14: R1 Should-Fix W1，R2 AGREE。升级为 Should-Fix。\"\n\n  - id: \"R13-M2\"\n    summary: \"Table 2 GEE (Likert-outcome) 与 Table 3 GEE (pairwise-outcome) 共享标签但模型不同\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Minor (M5)，R2 AGREE。建议在 Table 2 标注 'GEE (Likert-outcome)' 以区分。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。\"\n\n  # ============================================================\n  # Round 14 new issues\n  # ============================================================\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论，核心差异（cross-measurement mode comparison）被三点并列稀释。R1 REBUT（现有内容已基本充分但 organization 可改善）。Director 列为 Minor。\"\n\n  - id: \"R14-M1\"\n    summary: \"LLM rewriting 未报告 decoding seed / random seed\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1 Minor M2，R2 AGREE。Section 3.1 报告 temperature=0.7 但缺少 seed。\"\n\n  - id: \"R14-M2\"\n    summary: \"Figure 4 y 轴标签 'Significance probability' 与 caption 'Detection probability' 不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1 Minor M4，R2 AGREE。\"\n\n  - id: \"R14-M3\"\n    summary: \"'style bias' vs 'style preference' vs 'style sensitivity' 术语混用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 Minor-3，R1 AGREE。\"\n\n  - id: \"R14-REF1\"\n    summary: \"建议补充引用：Luce (1959), Williams et al. (2018) MNLI\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"两位独立建议 Luce (1959)——BT 模型理论基础。R1 建议 Williams et al. (2018) MNLI——NLI gate 的基础引用。\""
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-22T22:59:48.237100+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 48564}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-22T23:02:27.122591+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "report": "# Round 14 审稿报告\n\n**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（第 14 轮）\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 统计方法学 + 实验设计；R2: 新颖性 + framing + 写作质量 + 完整性）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，通过 NLI 门控内容保持、per-axis 风格改写和 position-controlled pairwise comparison，系统量化了 LLM judge 在 Likert 和 pairwise 两种评分模式下的风格敏感度差异（\"Likert Blindspot\"）。在 4 个 target judge、1 个负控制、2 条主要风格轴（formality, verbosity）和 3 个 benchmark 上，pairwise 方法一致检测到 Likert 无法检测的风格偏好。GEE 条件分解揭示了轴间异质性的 confound 结构：verbosity 是 style-dominated（Style OR 8-13），formality 是 conditional effect。\n\n---\n\n## Strengths\n\n**S1** [两位共识] **方法论严谨度在 NLP 实证论文中罕见**。三重控制（NLI 门控 + position control + same-text pairing）、7 种测量方法交叉验证（Table 2）、GEE 相关结构鲁棒性检查（Appendix C）、bootstrap attenuation 分析（Appendix J）、power analysis（Appendix K）——每一项都不是走流程，而是 genuine diagnostic。\n\n**S2** [两位共识] **GEE per-axis confound 结构差异是最有价值的增量贡献**。Table 3 揭示 verbosity 是 style-dominated（Style OR 5-13，Orig OR < 1）而 formality 是 conditional effect（Style OR 和 Orig OR 均显著），为 practitioners 提供了可操作的诊断框架——哪些轴的评估结果可直接解读，哪些需要 decomposition。\n\n**S3** [两位共识] **跨 4 个独立 judge 架构的复现**。GPT-4o、Qwen3-32B、Llama-3.3-70B、Gemini-2.5-Flash 覆盖不同训练策略和架构，Blindspot 在所有 target judge 上一致复现，增强了泛化性。\n\n**S4** [两位共识] **统计分析深度**。FWER 校正（Holm-Bonferroni 6-test 和 8-test 灵敏度）、GEE interaction tests（9 个 judge×axis cells 全部不显著）、NLI 阈值 sweep（11 个阈值 BT 变化 ≤3pp）、bootstrap attenuation curve（7 个样本量 d_median ≈ -0.017 恒定）。\n\n**S5** [R2] **诚实的 Limitations**。Quality-style confounding、construct validity、evaluator-producer bias 三个核心局限均被坦率讨论。\n\n**S6** [R1] **实际影响清晰**。\"Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines\"——对 NLG evaluation pipeline 设计提供了直接可操作的警示。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [R2 提出, R1 AGREE] **\"Framework\" 泛化声明与实际覆盖不匹配**\nSection 1 将 CSD 定位为通用 \"black-box framework for per-axis style bias detection\"，但仅测试 formality、verbosity、register 三条表面文本属性轴。对 semantic-level 风格轴（hedging, humor, technicality），NLI 门控可能系统性拒绝合法 rewrite——这是论文未讨论的 false positive 维度（区别于已讨论的 false negative 问题）。R1 补充：这不仅是范围问题，更是 NLI gate 的结构性适用限制。\n→ 建议：降级为 \"methodology\"/\"experimental protocol\" 或限定为 \"surface-level stylistic attributes amenable to content-preserving rewriting\"。\n\n**MF2** [R1 提出, R2 AGREE] **NLI Gate 人工验证标注一致性不足，样本量偏小**\n两名标注者在 50 对样本上 Cohen's κ=0.44（moderate），gate-passed 25 对 Wilson CI 下界 86.76% 意味着 ~13% 可能存在语义变化。对于以 measurement methodology 为核心贡献的论文，pipeline 核心组件的 validation 标准应更高。R2 补充缓解观察：BT 在 11 个 NLI 阈值上变化 ≤1pp（Appendix E），说明 downstream metric 对阈值不敏感——但 sample size 仍是硬伤。\n→ 建议：增加标注者至 ≥3 人 + 报告 Fleiss' κ + 对 verbosity condensation 分歧案例进行定性 error analysis。\n\n**MF3** [R2 提出, R1 AGREE] **核心发现的增量新颖性论证不足**\nForced-choice > absolute rating 是 Thurstone (1927)、Stevens (1946)、Krosnick (1999)、Preston & Colman (2000) 反复验证的经典心理测量结论。论文在 Section 2 引用了这些工作，但未充分论证在 LLM judge 领域\"重新量化\"此现象的独立新颖性。R1 同意但指出 GEE decomposition 的 per-axis confound 结构差异是 genuine insight——论文应将 novelty 重心从\"发现 divergence\"转向\"quantifying and decomposing per-axis confound structures\"。\n→ 建议：重构 novelty narrative，Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation。\n\n**MF4** [R1 提出, R2 部分 AGREE] **TOST 等价检验 Δ=15pp 缺乏外部校准，负控制论证力不足**\nΔ=15pp 理由是\"approximately where format preference would materially affect model rankings\"——校准标准不够透明。Δ=10pp 下 Claude 未通过等价检验（p=0.156），BT=56.2%（偏离 chance 6.2pp）。R2 REBUT \"循环论证\"标签（SESOI 在实践中很少有外部金标准），但 AGREE 校准不足。共识：正文需讨论不同 Δ 下结论变化 + 将 Claude 从 \"negative control\" 重新 framing 为 \"weak-effect/attenuated-bias control\"。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [R2 提出, R1 AGREE] **Construct divergence 解释发展不足**\n三种解释中，construct divergence（两种模式测量不同构念）在理论上最有趣但讨论最薄弱——Section 5.1 仅一句话。如果 construct divergence 是正确解释，\"Blindspot\" 就不是缺陷而是自然结果，根本改变 practical implication narrative。\n→ 建议：Section 5.1 用一段专门讨论 construct divergence 的含义和可检验预测。\n\n**SF2** [R2 提出, R1 AGREE] **Claude Sonnet 4 负控制结果讨论不充分**\nClaude 不展示 Blindspot 暗示这可能是 model-specific training artifact 而非 measurement-mode intrinsic property——对论文核心叙事构成潜在挑战。论文将此归因于\"RLHF training composition\"但未深入分析。\n→ 建议：讨论 Claude 负结果对 \"measurement-mode divergence\" 叙事的含义——是否说明 Blindspot 可通过训练消除？\n\n**SF3** [R1 提出, R2 AGREE] **Bootstrap CI 方法类型未报告**\n论文报告\"10,000 pair-level resamples\"但未指明 percentile vs BCa。对 bounded [0,1] 参数（BT win probability），percentile intervals 在小样本下覆盖率可能不足。\n→ 建议：明确报告 CI 类型。\n\n**SF4** [R1 提出, R2 AGREE] **BT 模型 unidimensionality 假设仅在脚注讨论**\nBT 假设单一潜在\"quality\"维度。对以 measurement methodology 为核心贡献的论文，此假设的讨论不应止于脚注。\n→ 建议：提升到 Limitations，讨论违反条件和影响方向。\n\n**SF5** [R2 提出, R1 AGREE] **Abstract 数字密度过高**\n至少 6 个定量数字，信息密度影响可读性。\n→ 建议：保留 1-2 个关键数字，其余移入正文。\n\n**SF6** [R1 提出, R2 部分 AGREE] **Direction-aware NLI gate 恢复的 21 对未经人工验证**\n主 pipeline gate-passed pairs 有 50 对人工验证，放宽标准恢复的 21 对应至少接受同等水平人工检查。R2 补充：影响有限（BT Δ ≈ -1pp），但严谨性需要。\n\n**SF7** [两位共识] **样本外部效度论证不足**\nLLMBar (n=100) + AlpacaEval + MT-Bench 三个 benchmark 均偏向 general instruction-following。Cross-benchmark replication 仅 \"selected configurations\"，未充分讨论。\n\n---\n\n### Minor（不影响接收）\n\n| # | 问题 | 来源 | 交叉 |\n|---|------|------|------|\n| M1 | Conclusion 最后一行可能溢出到 p.9 | R1 | R2 AGREE |\n| M2 | LLM rewriting 未报告 decoding seed | R1 | R2 AGREE |\n| M3 | Table 1 caption 自解释性不足 + 信息密度过高 | R1+R2 | 共识 |\n| M4 | Figure 4 y 轴标签与 caption 术语不一致 | R1 | R2 AGREE |\n| M5 | Table 3 显著性标记格式不一致 | R1 | R2 AGREE |\n| M6 | \"style bias\" vs \"style preference\" vs \"style sensitivity\" 术语混用 | R2 | R1 AGREE |\n| M7 | Section 3.5 Design Rationale 位置突兀 | R2 | R1 AGREE |\n| M8 | Appendix 过多（A-S, 19 个），建议合并同类 | R2 | R1 AGREE |\n| M9 | Introduction motivating example 应在例子后立即引入替代解释 | R1+R2 | 共识 |\n| M10 | 与 RATE 的差异化论证组织分散，核心差异被稀释 | R2 | R1 REBUT（内容充分但 organization 可改善） |\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识 [AGREE]：\n1. \"Framework\" 泛化声明需要降级或限定范围\n2. NLI gate 人工验证不足（κ=0.44, n=50 是硬伤）\n3. Novelty 重心应从\"发现 divergence\"转向\"GEE decomposition + per-axis confound structures\"\n4. TOST Δ=15pp 校准不够透明，Claude 应从\"negative control\"重新 framing\n5. Construct divergence 解释发展不足\n6. Claude 负控制讨论不充分\n7. GEE per-axis decomposition 是论文最有价值的增量贡献\n8. 统计分析深度在 NLP 实证论文中罕见，是显著优势\n\n---\n\n## Reviewer Divergence\n\n**唯一分歧：标题 \"Blindspot\" 是否隐含 attenuation 偏向**\n\n- **R2** [Must-Fix N2]：\"Blindspot\" 在认知科学中含义是\"盲区\"——预设 attenuation 解释，排斥 amplification 和 construct divergence。建议更中性标题。\n- **R1** [部分 REBUT]：\"Blindspot\" 描述可观测现象（Likert 系统性无法检测 pairwise 能检测的效应），类似 \"survivorship bias\" 命名模式而非机制预设。但 AGREE Introduction 的 motivating example 确实偏向 attenuation，应提前引入替代解释。\n\n**Director 判断**：标题 \"Blindspot\" 可保留（描述现象的命名约定在学术文献中常见），但 Introduction 应在 motivating example 后**立即**简要引入三种非排他性解释，避免读者在前 6 页形成单向认知。此问题从 Must-Fix 降为 Should-Fix——标题选择属作者判断范围，但 framing 不平衡需修正。\n\n---\n\n## Questions\n\n1. **Attenuation vs construct divergence 的可区分性**：Appendix J 的 bootstrap attenuation 数据（d_median ≈ -0.017 在所有样本量下恒定）是否足以区分\"true null effect\"（construct divergence）和\"merely underpowered\"（attenuation）？如果 Likert ATE 是 true null，这对 Blindspot 机制讨论意味什么？\n\n2. **NLI gate 过滤的 pairs 的 style effect 偏向**：被过滤的 ~38% pairs 是否系统性对应更大的 style 效应？如果是，NLI 门控可能系统性低估实际 style bias 幅度。\n\n3. **Claude 负结果的机制性解释**：Claude 不展示 Blindspot 是否可能通过改进 judge prompt（而非更改 measurement mode）来缓解其他 judge 的 Blindspot？这对 practical recommendation 的影响？\n\n4. **GEE 的 causal interpretation**：论文使用 \"Controlled\" 语言，但 GEE 本身是 associational。能否更精确界定哪些 inference 是 causal（来自实验设计）、哪些是 conditional association（来自统计模型）？\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 理由 |\n|------|------|------|\n| **Luce (1959)** \"Individual Choice Behavior\" | R1+R2 独立建议 | BT 模型是 Luce choice axiom 的特例，论文使用 BT 但未引用理论基础 |\n| **Williams et al. (2018)** MNLI | R1 建议, R2 AGREE | NLI gate 使用 DeBERTa fine-tuned on MNLI，但未引用 MNLI 原始论文 |\n| Kim et al. (2024) \"Prometheus 2\" | R2 建议 | R1 REBUT（关联度有限）。Director 判断：可选，非必须 |\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 8 info）：\n\n**Warnings:**\n- **Page 6**: 单页堆叠 3 个 display items（Table 1 + Figure 3 + Table 2），极拥挤。Table 1 脚注字号约 6pt，阅读困难。建议将 Table 2 移至后续页面。\n- **Page 5**: 全页纯文本含 5 个 section heading，节奏碎片化，缺乏视觉锚点。\n\n**Info highlights:**\n- Figure 2 DAG 设计清晰，caption 自包含且适当谦虚\n- Figure 4 power curves 建议补充 marker shape 增强打印友好性\n- 首页无 display item（Figure 1 在 p.2），可考虑 teaser 提升第一印象\n- Appendix 表格排版规范，booktabs 风格一致\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5（Borderline Conference）**\n\n| Reviewer | Overall | Soundness | Excitement | Reproducibility | Confidence |\n|----------|---------|-----------|------------|-----------------|------------|\n| R1 | 3.5 | 3.5 | 3.5 | 4.0 | 4 |\n| R2 | 3.5 | 4.0 | 3.0 | 4.0 | 4 |\n| **综合** | **3.5** | **3.75** | **3.25** | **4.0** | **4** |\n\n**判断依据**：\n\n论文在方法论执行上接近会议水平（Soundness 3.75），统计分析的深度和严谨度在 NLP 实证论文中属上乘。GEE per-axis confound decomposition 是 genuine insight，对 NLG evaluation practice 有直接价值。\n\n但三个因素将其拉到 Borderline：\n1. **Novelty cap**（Excitement 3.25）：核心发现是已知心理测量结论的 domain transfer，论文未充分论证 LLM judge 领域的独立贡献。如果将 novelty narrative 重构为 GEE decomposition + per-axis confound taxonomy，可能提升 Excitement。\n2. **NLI gate 验证不足**：作为 measurement methodology 论文，pipeline 核心组件的人工验证标准偏低（κ=0.44, n=50）。\n3. **Framing 不平衡**：三种解释（attenuation/amplification/construct divergence）的权重分配不均，标题和叙事偏向 attenuation。\n\n**升级到 4.0 (Conference) 的路径**：(1) 重构 novelty narrative 突出 GEE decomposition；(2) 增加 NLI gate 人工标注（≥100 对 + 第 3 标注员）；(3) 将 \"framework\" 降级为 \"methodology\"；(4) Introduction 提前引入三种解释；(5) 正文讨论 TOST Δ sensitivity。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Motivating example (GPT-4o formal vs casual) 有效但暗示 Likert 判断是\"错误的\"。应在例子后立即引入 amplification 和 construct divergence 作为等权重替代解释。[R2 N2, R1 部分 AGREE]\n- Contributions 第一条 \"black-box framework\" 应降级为 \"methodology\" 或加限定语。[R2 N1, R1 AGREE]\n- GEE decomposition 应提升为与 Blindspot 平行的核心贡献，而非被 Blindspot 遮蔽。[R2 N3, R1 AGREE]\n\n### Section 2 (Related Work)\n- Measurement Sensitivity 段落引用了 Thurstone (1927) 等经典文献，但未充分论证在 LLM judge 领域量化此现象的独立价值。建议论证 LLM judges 的 RLHF pipeline 引入了人类评估不存在的 mode-specific biases。[R2 N3]\n- 与 RATE 的差异化论证分散在两处，建议在 RW 末尾增加集中对比段落。[R2 W2, R1 部分 REBUT]\n- 缺少 Luce (1959)（BT 理论基础）和 Williams et al. (2018) MNLI（NLI gate 基础引用）。[R1+R2]\n\n### Section 3 (Method)\n- Section 3.5 Design Rationale 位置可优化（移至 3.1-3.2 之间或合并）。[R2 Minor-4, R1 AGREE]\n- NLI gate 的 content preservation 验证（Section 5.4）中 κ=0.44 的 disagreement cases 应做定性 error analysis。[R1 N1, R2 AGREE]\n\n### Section 4-5 (Experiments & Analysis)\n- Table 1 信息密度极高，建议拆分或增强 caption 自解释性。[R1 M3, R2 Minor-1]\n- Section 5.1 \"Interpreting the divergence\" 应扩展 construct divergence 讨论——如果两种模式测量不同构念，practitioners 应如何选择 format？[R2 W4, R1 AGREE]\n- BT unidimensionality 假设应从脚注提升到 Limitations。[R1 W4, R2 AGREE]\n- Bootstrap CI 类型应明确报告。[R1 W1, R2 AGREE]\n\n### Section 6 (Conclusion)\n- \"Likert-only audits may fail to surface...\" 应平衡表述为 \"the two modes may capture different aspects of style preferences\"。[R2 N2]\n- 可能有一行溢出到 p.9，需确认并修复。[R1 M1]\n\n### Limitations\n- 讨论坦率且全面，是论文优势之一。[R2 S5]\n- 建议增加：(1) CSD 对 semantic-level 风格轴的适用性边界；(2) TOST Δ 的 sensitivity analysis discussion；(3) BT unidimensionality 假设的违反条件；(4) Claude 负结果对 mode-intrinsic vs model-specific 的含义。\n\n### Appendix\n- 19 个 appendix 内容充实但数量过多。建议合并同类（如 C+H → \"Model Diagnostics\"，E+F+N → \"NLI Gate Analyses\"）。[R2 Minor-5, R1 AGREE]\n- Appendix P 缺少 rewriting decoding seed。[R1 M2, R2 AGREE]",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
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
    "project": "causal_style_decomp_judge",
    "report": "# Round 14 审稿报告\n\n**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（第 14 轮）\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 统计方法学 + 实验设计；R2: 新颖性 + framing + 写作质量 + 完整性）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，通过 NLI 门控内容保持、per-axis 风格改写和 position-controlled pairwise comparison，系统量化了 LLM judge 在 Likert 和 pairwise 两种评分模式下的风格敏感度差异（\"Likert Blindspot\"）。在 4 个 target judge、1 个负控制、2 条主要风格轴（formality, verbosity）和 3 个 benchmark 上，pairwise 方法一致检测到 Likert 无法检测的风格偏好。GEE 条件分解揭示了轴间异质性的 confound 结构：verbosity 是 style-dominated（Style OR 8-13），formality 是 conditional effect。\n\n---\n\n## Strengths\n\n**S1** [两位共识] **方法论严谨度在 NLP 实证论文中罕见**。三重控制（NLI 门控 + position control + same-text pairing）、7 种测量方法交叉验证（Table 2）、GEE 相关结构鲁棒性检查（Appendix C）、bootstrap attenuation 分析（Appendix J）、power analysis（Appendix K）——每一项都不是走流程，而是 genuine diagnostic。\n\n**S2** [两位共识] **GEE per-axis confound 结构差异是最有价值的增量贡献**。Table 3 揭示 verbosity 是 style-dominated（Style OR 5-13，Orig OR < 1）而 formality 是 conditional effect（Style OR 和 Orig OR 均显著），为 practitioners 提供了可操作的诊断框架——哪些轴的评估结果可直接解读，哪些需要 decomposition。\n\n**S3** [两位共识] **跨 4 个独立 judge 架构的复现**。GPT-4o、Qwen3-32B、Llama-3.3-70B、Gemini-2.5-Flash 覆盖不同训练策略和架构，Blindspot 在所有 target judge 上一致复现，增强了泛化性。\n\n**S4** [两位共识] **统计分析深度**。FWER 校正（Holm-Bonferroni 6-test 和 8-test 灵敏度）、GEE interaction tests（9 个 judge×axis cells 全部不显著）、NLI 阈值 sweep（11 个阈值 BT 变化 ≤3pp）、bootstrap attenuation curve（7 个样本量 d_median ≈ -0.017 恒定）。\n\n**S5** [R2] **诚实的 Limitations**。Quality-style confounding、construct validity、evaluator-producer bias 三个核心局限均被坦率讨论。\n\n**S6** [R1] **实际影响清晰**。\"Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines\"——对 NLG evaluation pipeline 设计提供了直接可操作的警示。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [R2 提出, R1 AGREE] **\"Framework\" 泛化声明与实际覆盖不匹配**\nSection 1 将 CSD 定位为通用 \"black-box framework for per-axis style bias detection\"，但仅测试 formality、verbosity、register 三条表面文本属性轴。对 semantic-level 风格轴（hedging, humor, technicality），NLI 门控可能系统性拒绝合法 rewrite——这是论文未讨论的 false positive 维度（区别于已讨论的 false negative 问题）。R1 补充：这不仅是范围问题，更是 NLI gate 的结构性适用限制。\n→ 建议：降级为 \"methodology\"/\"experimental protocol\" 或限定为 \"surface-level stylistic attributes amenable to content-preserving rewriting\"。\n\n**MF2** [R1 提出, R2 AGREE] **NLI Gate 人工验证标注一致性不足，样本量偏小**\n两名标注者在 50 对样本上 Cohen's κ=0.44（moderate），gate-passed 25 对 Wilson CI 下界 86.76% 意味着 ~13% 可能存在语义变化。对于以 measurement methodology 为核心贡献的论文，pipeline 核心组件的 validation 标准应更高。R2 补充缓解观察：BT 在 11 个 NLI 阈值上变化 ≤1pp（Appendix E），说明 downstream metric 对阈值不敏感——但 sample size 仍是硬伤。\n→ 建议：增加标注者至 ≥3 人 + 报告 Fleiss' κ + 对 verbosity condensation 分歧案例进行定性 error analysis。\n\n**MF3** [R2 提出, R1 AGREE] **核心发现的增量新颖性论证不足**\nForced-choice > absolute rating 是 Thurstone (1927)、Stevens (1946)、Krosnick (1999)、Preston & Colman (2000) 反复验证的经典心理测量结论。论文在 Section 2 引用了这些工作，但未充分论证在 LLM judge 领域\"重新量化\"此现象的独立新颖性。R1 同意但指出 GEE decomposition 的 per-axis confound 结构差异是 genuine insight——论文应将 novelty 重心从\"发现 divergence\"转向\"quantifying and decomposing per-axis confound structures\"。\n→ 建议：重构 novelty narrative，Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation。\n\n**MF4** [R1 提出, R2 部分 AGREE] **TOST 等价检验 Δ=15pp 缺乏外部校准，负控制论证力不足**\nΔ=15pp 理由是\"approximately where format preference would materially affect model rankings\"——校准标准不够透明。Δ=10pp 下 Claude 未通过等价检验（p=0.156），BT=56.2%（偏离 chance 6.2pp）。R2 REBUT \"循环论证\"标签（SESOI 在实践中很少有外部金标准），但 AGREE 校准不足。共识：正文需讨论不同 Δ 下结论变化 + 将 Claude 从 \"negative control\" 重新 framing 为 \"weak-effect/attenuated-bias control\"。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [R2 提出, R1 AGREE] **Construct divergence 解释发展不足**\n三种解释中，construct divergence（两种模式测量不同构念）在理论上最有趣但讨论最薄弱——Section 5.1 仅一句话。如果 construct divergence 是正确解释，\"Blindspot\" 就不是缺陷而是自然结果，根本改变 practical implication narrative。\n→ 建议：Section 5.1 用一段专门讨论 construct divergence 的含义和可检验预测。\n\n**SF2** [R2 提出, R1 AGREE] **Claude Sonnet 4 负控制结果讨论不充分**\nClaude 不展示 Blindspot 暗示这可能是 model-specific training artifact 而非 measurement-mode intrinsic property——对论文核心叙事构成潜在挑战。论文将此归因于\"RLHF training composition\"但未深入分析。\n→ 建议：讨论 Claude 负结果对 \"measurement-mode divergence\" 叙事的含义——是否说明 Blindspot 可通过训练消除？\n\n**SF3** [R1 提出, R2 AGREE] **Bootstrap CI 方法类型未报告**\n论文报告\"10,000 pair-level resamples\"但未指明 percentile vs BCa。对 bounded [0,1] 参数（BT win probability），percentile intervals 在小样本下覆盖率可能不足。\n→ 建议：明确报告 CI 类型。\n\n**SF4** [R1 提出, R2 AGREE] **BT 模型 unidimensionality 假设仅在脚注讨论**\nBT 假设单一潜在\"quality\"维度。对以 measurement methodology 为核心贡献的论文，此假设的讨论不应止于脚注。\n→ 建议：提升到 Limitations，讨论违反条件和影响方向。\n\n**SF5** [R2 提出, R1 AGREE] **Abstract 数字密度过高**\n至少 6 个定量数字，信息密度影响可读性。\n→ 建议：保留 1-2 个关键数字，其余移入正文。\n\n**SF6** [R1 提出, R2 部分 AGREE] **Direction-aware NLI gate 恢复的 21 对未经人工验证**\n主 pipeline gate-passed pairs 有 50 对人工验证，放宽标准恢复的 21 对应至少接受同等水平人工检查。R2 补充：影响有限（BT Δ ≈ -1pp），但严谨性需要。\n\n**SF7** [两位共识] **样本外部效度论证不足**\nLLMBar (n=100) + AlpacaEval + MT-Bench 三个 benchmark 均偏向 general instruction-following。Cross-benchmark replication 仅 \"selected configurations\"，未充分讨论。\n\n---\n\n### Minor（不影响接收）\n\n| # | 问题 | 来源 | 交叉 |\n|---|------|------|------|\n| M1 | Conclusion 最后一行可能溢出到 p.9 | R1 | R2 AGREE |\n| M2 | LLM rewriting 未报告 decoding seed | R1 | R2 AGREE |\n| M3 | Table 1 caption 自解释性不足 + 信息密度过高 | R1+R2 | 共识 |\n| M4 | Figure 4 y 轴标签与 caption 术语不一致 | R1 | R2 AGREE |\n| M5 | Table 3 显著性标记格式不一致 | R1 | R2 AGREE |\n| M6 | \"style bias\" vs \"style preference\" vs \"style sensitivity\" 术语混用 | R2 | R1 AGREE |\n| M7 | Section 3.5 Design Rationale 位置突兀 | R2 | R1 AGREE |\n| M8 | Appendix 过多（A-S, 19 个），建议合并同类 | R2 | R1 AGREE |\n| M9 | Introduction motivating example 应在例子后立即引入替代解释 | R1+R2 | 共识 |\n| M10 | 与 RATE 的差异化论证组织分散，核心差异被稀释 | R2 | R1 REBUT（内容充分但 organization 可改善） |\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识 [AGREE]：\n1. \"Framework\" 泛化声明需要降级或限定范围\n2. NLI gate 人工验证不足（κ=0.44, n=50 是硬伤）\n3. Novelty 重心应从\"发现 divergence\"转向\"GEE decomposition + per-axis confound structures\"\n4. TOST Δ=15pp 校准不够透明，Claude 应从\"negative control\"重新 framing\n5. Construct divergence 解释发展不足\n6. Claude 负控制讨论不充分\n7. GEE per-axis decomposition 是论文最有价值的增量贡献\n8. 统计分析深度在 NLP 实证论文中罕见，是显著优势\n\n---\n\n## Reviewer Divergence\n\n**唯一分歧：标题 \"Blindspot\" 是否隐含 attenuation 偏向**\n\n- **R2** [Must-Fix N2]：\"Blindspot\" 在认知科学中含义是\"盲区\"——预设 attenuation 解释，排斥 amplification 和 construct divergence。建议更中性标题。\n- **R1** [部分 REBUT]：\"Blindspot\" 描述可观测现象（Likert 系统性无法检测 pairwise 能检测的效应），类似 \"survivorship bias\" 命名模式而非机制预设。但 AGREE Introduction 的 motivating example 确实偏向 attenuation，应提前引入替代解释。\n\n**Director 判断**：标题 \"Blindspot\" 可保留（描述现象的命名约定在学术文献中常见），但 Introduction 应在 motivating example 后**立即**简要引入三种非排他性解释，避免读者在前 6 页形成单向认知。此问题从 Must-Fix 降为 Should-Fix——标题选择属作者判断范围，但 framing 不平衡需修正。\n\n---\n\n## Questions\n\n1. **Attenuation vs construct divergence 的可区分性**：Appendix J 的 bootstrap attenuation 数据（d_median ≈ -0.017 在所有样本量下恒定）是否足以区分\"true null effect\"（construct divergence）和\"merely underpowered\"（attenuation）？如果 Likert ATE 是 true null，这对 Blindspot 机制讨论意味什么？\n\n2. **NLI gate 过滤的 pairs 的 style effect 偏向**：被过滤的 ~38% pairs 是否系统性对应更大的 style 效应？如果是，NLI 门控可能系统性低估实际 style bias 幅度。\n\n3. **Claude 负结果的机制性解释**：Claude 不展示 Blindspot 是否可能通过改进 judge prompt（而非更改 measurement mode）来缓解其他 judge 的 Blindspot？这对 practical recommendation 的影响？\n\n4. **GEE 的 causal interpretation**：论文使用 \"Controlled\" 语言，但 GEE 本身是 associational。能否更精确界定哪些 inference 是 causal（来自实验设计）、哪些是 conditional association（来自统计模型）？\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 理由 |\n|------|------|------|\n| **Luce (1959)** \"Individual Choice Behavior\" | R1+R2 独立建议 | BT 模型是 Luce choice axiom 的特例，论文使用 BT 但未引用理论基础 |\n| **Williams et al. (2018)** MNLI | R1 建议, R2 AGREE | NLI gate 使用 DeBERTa fine-tuned on MNLI，但未引用 MNLI 原始论文 |\n| Kim et al. (2024) \"Prometheus 2\" | R2 建议 | R1 REBUT（关联度有限）。Director 判断：可选，非必须 |\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 8 info）：\n\n**Warnings:**\n- **Page 6**: 单页堆叠 3 个 display items（Table 1 + Figure 3 + Table 2），极拥挤。Table 1 脚注字号约 6pt，阅读困难。建议将 Table 2 移至后续页面。\n- **Page 5**: 全页纯文本含 5 个 section heading，节奏碎片化，缺乏视觉锚点。\n\n**Info highlights:**\n- Figure 2 DAG 设计清晰，caption 自包含且适当谦虚\n- Figure 4 power curves 建议补充 marker shape 增强打印友好性\n- 首页无 display item（Figure 1 在 p.2），可考虑 teaser 提升第一印象\n- Appendix 表格排版规范，booktabs 风格一致\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5（Borderline Conference）**\n\n| Reviewer | Overall | Soundness | Excitement | Reproducibility | Confidence |\n|----------|---------|-----------|------------|-----------------|------------|\n| R1 | 3.5 | 3.5 | 3.5 | 4.0 | 4 |\n| R2 | 3.5 | 4.0 | 3.0 | 4.0 | 4 |\n| **综合** | **3.5** | **3.75** | **3.25** | **4.0** | **4** |\n\n**判断依据**：\n\n论文在方法论执行上接近会议水平（Soundness 3.75），统计分析的深度和严谨度在 NLP 实证论文中属上乘。GEE per-axis confound decomposition 是 genuine insight，对 NLG evaluation practice 有直接价值。\n\n但三个因素将其拉到 Borderline：\n1. **Novelty cap**（Excitement 3.25）：核心发现是已知心理测量结论的 domain transfer，论文未充分论证 LLM judge 领域的独立贡献。如果将 novelty narrative 重构为 GEE decomposition + per-axis confound taxonomy，可能提升 Excitement。\n2. **NLI gate 验证不足**：作为 measurement methodology 论文，pipeline 核心组件的人工验证标准偏低（κ=0.44, n=50）。\n3. **Framing 不平衡**：三种解释（attenuation/amplification/construct divergence）的权重分配不均，标题和叙事偏向 attenuation。\n\n**升级到 4.0 (Conference) 的路径**：(1) 重构 novelty narrative 突出 GEE decomposition；(2) 增加 NLI gate 人工标注（≥100 对 + 第 3 标注员）；(3) 将 \"framework\" 降级为 \"methodology\"；(4) Introduction 提前引入三种解释；(5) 正文讨论 TOST Δ sensitivity。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Motivating example (GPT-4o formal vs casual) 有效但暗示 Likert 判断是\"错误的\"。应在例子后立即引入 amplification 和 construct divergence 作为等权重替代解释。[R2 N2, R1 部分 AGREE]\n- Contributions 第一条 \"black-box framework\" 应降级为 \"methodology\" 或加限定语。[R2 N1, R1 AGREE]\n- GEE decomposition 应提升为与 Blindspot 平行的核心贡献，而非被 Blindspot 遮蔽。[R2 N3, R1 AGREE]\n\n### Section 2 (Related Work)\n- Measurement Sensitivity 段落引用了 Thurstone (1927) 等经典文献，但未充分论证在 LLM judge 领域量化此现象的独立价值。建议论证 LLM judges 的 RLHF pipeline 引入了人类评估不存在的 mode-specific biases。[R2 N3]\n- 与 RATE 的差异化论证分散在两处，建议在 RW 末尾增加集中对比段落。[R2 W2, R1 部分 REBUT]\n- 缺少 Luce (1959)（BT 理论基础）和 Williams et al. (2018) MNLI（NLI gate 基础引用）。[R1+R2]\n\n### Section 3 (Method)\n- Section 3.5 Design Rationale 位置可优化（移至 3.1-3.2 之间或合并）。[R2 Minor-4, R1 AGREE]\n- NLI gate 的 content preservation 验证（Section 5.4）中 κ=0.44 的 disagreement cases 应做定性 error analysis。[R1 N1, R2 AGREE]\n\n### Section 4-5 (Experiments & Analysis)\n- Table 1 信息密度极高，建议拆分或增强 caption 自解释性。[R1 M3, R2 Minor-1]\n- Section 5.1 \"Interpreting the divergence\" 应扩展 construct divergence 讨论——如果两种模式测量不同构念，practitioners 应如何选择 format？[R2 W4, R1 AGREE]\n- BT unidimensionality 假设应从脚注提升到 Limitations。[R1 W4, R2 AGREE]\n- Bootstrap CI 类型应明确报告。[R1 W1, R2 AGREE]\n\n### Section 6 (Conclusion)\n- \"Likert-only audits may fail to surface...\" 应平衡表述为 \"the two modes may capture different aspects of style preferences\"。[R2 N2]\n- 可能有一行溢出到 p.9，需确认并修复。[R1 M1]\n\n### Limitations\n- 讨论坦率且全面，是论文优势之一。[R2 S5]\n- 建议增加：(1) CSD 对 semantic-level 风格轴的适用性边界；(2) TOST Δ 的 sensitivity analysis discussion；(3) BT unidimensionality 假设的违反条件；(4) Claude 负结果对 mode-intrinsic vs model-specific 的含义。\n\n### Appendix\n- 19 个 appendix 内容充实但数量过多。建议合并同类（如 C+H → \"Model Diagnostics\"，E+F+N → \"NLI Gate Analyses\"）。[R2 Minor-5, R1 AGREE]\n- Appendix P 缺少 rewriting decoding seed。[R1 M2, R2 AGREE]",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-22T23:02:31.039300+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 1146 · 2026-05-22T23:02:40.637260+00:00_

Round 14 审稿完成。

**最终评分：3.5 / 5（Borderline Conference）**

报告已投递给 Research Director。两位 Reviewer 独立给出一致评分（均 3.5），经圆桌交叉讨论后在所有关键问题上达成共识。

**核心结论**：
- 方法论执行接近会议水平（Soundness 3.75），统计深度是显著优势
- GEE per-axis confound decomposition 是最有价值的增量贡献
- 三个主要障碍：novelty framing（经典结论的 domain transfer）、NLI gate 人工验证不足（κ=0.44, n=50）、"framework" overclaim
- 升级到 4.0 的路径已在报告中明确列出

Issue Tracker 已同步更新（含本轮所有新发现和历史问题状态追踪）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1147 · 2026-05-22T23:02:43.186276+00:00_

[Reviewer 2 审稿结果]:
已完成对 R1 的逐条交叉回应并提交给 Director。核心判断：

- **N1（NLI gate 验证）**: 同意样本量不足是硬伤，但指出 BT 对阈值不敏感（Table 9）和 gate-passed precision 100% 作为缓解
- **N2（TOST Δ 校准）**: 部分同意校准不充分，但反驳"循环论证"的定性——SESOI 选择本质上是 pragmatic judgment
- **W2（rewriter independence 仅覆盖 verbosity）**: 反驳——R1 遗漏了 Table 8，formality 轴已有独立 rewriter 验证
- **M1（超页）**: 确认 Conclusion 最后一行溢出到 page 9，但属于可修复的 minor issue
- 两份审稿互补：R1 侧重方法验证细节，R2（我）侧重概念定位和新颖性

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

_source line 1148 · 2026-05-22T23:02:57.281607+00:00_

审稿报告已于上一轮提交至 Research Director。

**Round 14 审稿完成，核心结论：**

- **Overall: 3.5 / 5（Borderline Conference）**
- **4 个 Must-Fix**：(1) "Framework" overclaim 需降级；(2) NLI gate 人工验证不足（κ=0.44, n=50）；(3) Novelty narrative 需从"发现 divergence"转向 GEE decomposition；(4) TOST Δ=15pp 校准不够透明 + Claude 负控制 reframing
- **7 个 Should-Fix**：construct divergence 讨论不足、Claude 负结果机制性讨论不足、Bootstrap CI 类型未报告、BT unidimensionality 需提升到 Limitations、Abstract 数字密度、direction-aware gate 21 对未验证、样本外部效度
- **升级到 4.0 的路径已明确**：重构 novelty narrative + 增加标注 + 降级 framework + 提前引入三种解释 + TOST Δ sensitivity

Issue Tracker 已同步更新（`review_issues.yaml`），审稿报告已投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 112

## Round 112

48 recorded events


### User

_source line 1149 · 2026-05-23T05:23:29.708546+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
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

_source line 1150 · 2026-05-23T05:23:35.220243+00:00_

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

_source line 1151 · 2026-05-23T05:23:35.271040+00:00_

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

_source line 1152 · 2026-05-23T05:23:44.066025+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T05:23:44.116844+00:00_



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

_source line 1154 · 2026-05-23T05:23:46.685236+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1155 · 2026-05-23T05:23:46.836627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-23T05:23:51.361160+00:00_

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

_source line 1157 · 2026-05-23T05:23:53.771663+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-23 01:30 UTC\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 近期完成\n\n### 紧急任务批次（6/6 完成或确认）\n- **任务1 — NLI 选择偏差扩展** ✅: formality 全 NS，verbosity 长度选择 p=0.003（保守方向）\n- **任务2 — DA-gate 21 对质量** ✅: 5/5 judges Likert diff 均 NS，可安全纳入\n- **任务3 — Claude cross-benchmark** ✅: AEval×form BT=0.840 Blindspot=true; AEval×verb BT=0.750 Style OR=4.76; MTB×form BT=0.854\n- **任务4a — Cross-benchmark local** ✅: AEval×Llama BT=0.775 NO Blindspot; MTB×Qwen BT=0.700 NO Blindspot\n- **任务5 — 标注扩展数据** ✅: 100 pairs template 拉到本地\n- **任务6 — Construct divergence** ✅: formality rewrite 后 Likert acc 100%→40%\n\n### Bug 修复（3/3）\n- **GEE Style==Orig** ✅: 数据共线性（非代码 bug），cross_benchmark_analysis.py 统计方法已修复\n- **Claude pipeline** ✅: 新建 claude_crossbenchmark_scoring.py，3 配置跑通\n- **数据差异 MTB×Qwen** ✅: Table 1 正确，差异来自 NLI 过滤/方法不一致\n\n## ⚠️ 关键发现\n- Claude 在 LLMBar 是有效 negative control (BT≈55%, NS)，但 AEval/MTB 上有强偏差 (BT 75-85%)\n- Director 决策：negative control 限定 LLMBar only，cross-benchmark 数据转为新发现\n- 合并 TOST 不报告\n\n## 原始 TOST 确认\nRegistry `claude_tost_equivalence` 不受影响：formality p̂=0.562 n=88, verbosity p̂=0.541 n=86\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n1. 等 Director 确认 task 4b (GPT-4o cross-benchmark) 是否仍需\n2. 等 Paper Agent 完成写作修改\n3. 等标注员回复\n\n## 资源状态\nwestb-29275: 4×RTX PR
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2410
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-23T05:23:54.277459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"",
  "description": "Check if main.tex exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"",
    "description": "Check if main.tex exists"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-23T05:23:55.232097+00:00_

-rw-r--r-- 1 ubuntu ubuntu 6421 May 23 01:45 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
MAIN_TEX_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-23T05:23:55.232615+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-23T05:23:55.684965+00:00_

-rw-r--r-- 1 ubuntu ubuntu 416213 May 23 02:35 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-23T05:23:56.175470+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
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

_source line 1163 · 2026-05-23T05:23:57.084462+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXISTS\" || echo \"ISSUES_MISSING\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXISTS\" || echo \"ISSUES_MISSING\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-23T05:23:57.157023+00:00_

-rw-r--r-- 1 ubuntu ubuntu 55446 May 22 22:59 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml
ISSUES_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 72
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-23T05:24:03.576215+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's what I found about EMNLP 2026 call for papers submission guidelines and ARR:

## Main Conference Paper Submission

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. Thi
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 7400
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-23T05:24:09.652500+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May cycle submission deadline page limit format requirements"
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
    "query": "EMNLP 2026 ARR May cycle submission deadline page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-23T05:24:11.209651+00:00_

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

_source line 1168 · 2026-05-23T05:24:11.561536+00:00_

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
…[truncated 4649 chars]

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

_source line 1169 · 2026-05-23T05:24:11.712618+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml"
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
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-23T05:24:15.830827+00:00_

Web search results for query: "EMNLP 2026 ARR May cycle submission deadline page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the information about EMNLP 2026 ARR May cycle submission requirements:

## Submission Deadline

The ARR submission deadline for both long and short papers is May 25, 2026.

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. 

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Additional Requirements

The mandatory Limitations section 
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 6178
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-23T05:24:15.831395+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4118
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-23T05:24:33.407752+00:00_

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

_source line 1173 · 2026-05-23T05:24:34.714308+00:00_

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
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-23T05:24:34.865479+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-23T05:24:34.916104+00:00_

NO_EXTERNAL_REVIEW_CONFIG

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

_source line 1176 · 2026-05-23T05:24:37.278774+00:00_

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

_source line 1177 · 2026-05-23T05:24:38.183660+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce systematically divergent style sensitivity when applied to LLM judges.
3	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic methodology that quantifies this divergence under controlled conditions via human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
4	Across four judges from independent providers, one negative control, and two primary axes (formality, verbosity), the divergence is robust: pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\% at stronger effects---replicated across three benchmarks and confirmed by seven statistical methods.
5	GEE conditional decomposition reveals qualitatively distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects a conditional effect where style and content quality contribute jointly---determining which pairwise estimates are directly interpretable and which require decomposition.
6	This divergence admits three non-exclusive explanations---measurement attenuation, format amplification, or construct divergence---that our controlled design bounds but cannot definitively adjudicate.
7	A negative-control judge shows no divergence on either primary axis, supporting discriminative validity.
8	Whether the divergence reflects Likert attenuation, pairwise amplification, or construct-level differences remains open; the practical consequence is unambiguous: Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-23T05:24:38.183990+00:00_

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

_source line 1179 · 2026-05-23T05:24:38.334843+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}.
6	This divergence admits multiple non-exclusive explanations---Likert measurement attenuation, pairwise format amplification, or construct-level differences between absolute and comparative evaluation---which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:direction}).
7	This example reflects a systematic pattern.
8	
9	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
11	Despite this consensus, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
12	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison \citep{thurstone1927law,stevens1946theory}; we provide the first controlled quantification of this gap for LLM judges, with GEE decomposition revealing axis-dep
…[truncated 2736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-23T05:24:38.686611+00:00_

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

_source line 1181 · 2026-05-23T05:24:38.938155+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 6286 chars]

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

_source line 1182 · 2026-05-23T05:24:38.938581+00:00_

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

_source line 1183 · 2026-05-23T05:24:39.039650+00:00_

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
…[truncated 5213 chars]

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

_source line 1184 · 2026-05-23T05:24:43.007100+00:00_

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

_source line 1185 · 2026-05-23T05:24:43.510114+00:00_

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
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$; verbosity: $p = 0.453$) reflects heterogeneous treatment effects across style directions rather than IIA violation.}
13	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimat
…[truncated 17463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-23T05:24:43.510646+00:00_

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

_source line 1187 · 2026-05-23T05:24:44.164189+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: pairwise comparison and Likert scoring produce systematically divergent verdicts on the same style contrasts---complete divergence at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed by seven statistical methods across four judges and three benchmarks.
6	Second, GEE conditional decomposition reveals qualitatively distinct per-axis confound structures---verbosity is style-dominated, formality is a conditional effect, register is judge-dependent---and disambiguates cases where aggregate preference reflects quality detection rather than style sensitivity.
7	Regardless of mechanism, single-format audits risk systematic blind spots; human ground-truth validation of both modes is the key next step.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-23T05:24:44.164683+00:00_

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


### Tool result

_source line 1189 · 2026-05-23T05:24:44.617622+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), human annotation agreement (S), Claude cross-benchmark (T).}
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
19	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-r
…[truncated 36806 chars]

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

_source line 1190 · 2026-05-23T05:25:09.922829+00:00_

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

_source line 1191 · 2026-05-23T05:25:27.502470+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17579
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-23T05:25:28.004792+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制 + 无限参考文献, ACL模板, double-blind\n- **Limitations**: mandatory, 不计入页数限制\n- **匿名规则**: double-blind（论文中不能有作者身份信息）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **方法论严谨性**：\n   - CSD pipeline 的设计是否合理？NLI gate 作为 content preservation 的验证手段是否充分？\n   - 因果推断框架（DAG）的假设是否合理？\"interventional rather than formal causal evidence\" 这个定位是否准确？\n   - Style-controlled rewriting 是否真的能隔离单一 style axis？cross-axis contamination 的处理是否充分？\n\n2. **实验设计**：\n   - 4 个 target judges + 1 个 negative control 的选择是否合理？样本量（n=88, n=355）是否充分？\n   - 3 个 benchmark（LLMBar n=100, AlpacaEval n=100, MT-Bench n=80）的选择和覆盖范围\n   - Evaluator-producer overlap（Qwen3-32B 同时做 rewriter 和 judge）的处理是否充分？\n   - Negative control (Claude Sonnet 4) 的 equivalence testing 是否严谨？\n\n3. **统计方法**：\n   - Bradley-Terry model 的使用是否合理？IIA 假设的处理？\n   - GEE conditional decomposition 的模型选择（exchangeable correlation）是否合理？\n   - Holm-Bonferroni 多重比较校正的 family 定义是否恰当？\n   - Bootstrap CI 的方法和参数选择\n   - Power analysis 的合理性\n\n4. **可重复性**：\n   - 实验细节是否充分？是否有足够信息让其他研究者重复实验？\n   - 代码和数据承诺 \"released upon acceptance\"——是否有任何重复性隐患？\n\n请按 EMNLP 2026 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Minor Issues。",
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
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计方法**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制 + 无限参考文献, ACL模板, double-blind\n- **Limitations**: mandatory, 不计入页数限制\n- **匿名规则**: double-blind（论文中不能有作者身份信息）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **方法论严谨性**：\n   - CSD pipeline 的设计是否合理？NLI gate 作为 content preservation 的验证手段是否充分？\n   - 因果推断框架（DAG）的假设是否合理？\"interventional rather than formal causal evidence\" 这个定位是否准确？\n   - Style-controlled rewriting 是否真的能隔离单一 style axis？cross-axis contamination 的处理是否充分？\n\n2. **实验设计**：\n   - 4 个 target judges + 1 个 negative control 的选择是否合理？样本量（n=88, n=355）是否充分？\n   - 3 个 benchmark（LLMBar n=100, AlpacaEval n=100, MT-Bench n=80）的选择和覆盖范围\n   - Evaluator-producer overlap（Qwen3-32B 同时做 rewriter 和 judge）的处理是否充分？\n   - Negative control (Claude Sonnet 4) 的 equivalence testing 是否严谨？\n\n3. **统计方法**：\n   - Bradley-Terry model 的使用是否合理？IIA 假设的处理？\n   - GEE conditional decomposition 的模型选择（exchangeable correlation）是否合理？\n   - Holm-Bonferroni 多重比较校正的 family 定义是否恰当？\n   - Bootstrap CI 的方法和参数选择\n   - Power analysis 的合理性\n\n4. **可重复性**：\n   - 实验细节是否充分？是否有足够信息让其他研究者重复实验？\n   - 代码和数据承诺 \"released upon acceptance\"——是否有任何重复性隐患？\n\n请按 EMNLP 2026 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Minor Issues。",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-23T05:25:41.273195+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13268
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-23T05:25:42.780686+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制 + 无限参考文献, ACL模板, double-blind\n- **Limitations**: mandatory, 不计入页数限制\n- **匿名规则**: double-blind（论文中不能有作者身份信息）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性（Novelty）**：\n   - \"Likert Blindspot\" 这个发现的新颖程度如何？与 RATE (Reber et al. 2025)、Comparative Trap (Jeong et al. 2025) 等先前工作的增量贡献\n   - CSD 方法论的新颖性——NLI gate + per-axis decomposition + position-controlled pairwise 的组合是否构成足够的方法论贡献？\n   - GEE conditional decomposition 揭示的 per-axis confound structure 是否是真正的新发现？\n\n2. **完整性（Completeness）**：\n   - Related work 是否全面？是否遗漏重要的相关工作？\n   - 实验是否覆盖了足够的 style axes、judges、benchmarks？\n   - 对 \"three non-exclusive explanations\"（attenuation / amplification / construct divergence）的讨论是否充分？\n   - Limitations 是否诚实、全面？\n\n3. **写作质量**：\n   - 论文叙事结构是否清晰？读者能否顺畅跟随论证逻辑？\n   - Abstract 和 Introduction 是否准确传达了主要贡献？\n   - 术语使用是否一致？符号系统是否清晰？\n   - 图表是否有效传达信息？Table 1 和 Figure 2-3 的设计\n\n4. **格式合规（EMNLP 2026 ARR）**：\n   - 正文是否在 8 页限制内？\n   - ACL 模板是否正确使用（`\\usepackage[review]{acl}`）？\n   - 匿名性检查：是否有泄露作者身份的线索？\n   - Limitations section 是否符合要求？\n   - 参考文献格式是否一致？\n\n请按 EMNLP 2026 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Minor Issues。",
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
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8页正文限制 + 无限参考文献, ACL模板, double-blind\n- **Limitations**: mandatory, 不计入页数限制\n- **匿名规则**: double-blind（论文中不能有作者身份信息）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性（Novelty）**：\n   - \"Likert Blindspot\" 这个发现的新颖程度如何？与 RATE (Reber et al. 2025)、Comparative Trap (Jeong et al. 2025) 等先前工作的增量贡献\n   - CSD 方法论的新颖性——NLI gate + per-axis decomposition + position-controlled pairwise 的组合是否构成足够的方法论贡献？\n   - GEE conditional decomposition 揭示的 per-axis confound structure 是否是真正的新发现？\n\n2. **完整性（Completeness）**：\n   - Related work 是否全面？是否遗漏重要的相关工作？\n   - 实验是否覆盖了足够的 style axes、judges、benchmarks？\n   - 对 \"three non-exclusive explanations\"（attenuation / amplification / construct divergence）的讨论是否充分？\n   - Limitations 是否诚实、全面？\n\n3. **写作质量**：\n   - 论文叙事结构是否清晰？读者能否顺畅跟随论证逻辑？\n   - Abstract 和 Introduction 是否准确传达了主要贡献？\n   - 术语使用是否一致？符号系统是否清晰？\n   - 图表是否有效传达信息？Table 1 和 Figure 2-3 的设计\n\n4. **格式合规（EMNLP 2026 ARR）**：\n   - 正文是否在 8 页限制内？\n   - ACL 模板是否正确使用（`\\usepackage[review]{acl}`）？\n   - 匿名性检查：是否有泄露作者身份的线索？\n   - Limitations section 是否符合要求？\n   - 参考文献格式是否一致？\n\n请按 EMNLP 2026 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Minor Issues。",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-23T05:25:44.141157+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 1196 · 2026-05-23T05:25:51.621601+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发，并行执行中
- **Reviewer 1**（方法/实验/统计）：已分配任务
- **Reviewer 2**（新颖性/完整性/写作/格式）：已分配任务

等待两名 Reviewer 提交独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1197 · 2026-05-23T05:31:38.988473+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论扎实、实验设计严谨，但仅覆盖两个风格轴（formality, verbosity）限制了"Likert Blindspot"作为通用现象的推广性，三种机制解释未能区分进一步削弱了理论贡献。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | NLI gating + position-controlled pairwise + GEE decomposition 方法论合理且有多项 robustness check；但核心 claim（"Blindspot 是系统性现象"）仅基于两个表层风格轴，且三种机制解释（attenuation/amplification/construct divergence）未能区分，限制了 soundness 的上限 |
| Excitement | 3/5 | Likert-pairwise 模式差异是有价值的发现，但实际推论（"style 评估应优先用 pairwise"）对熟悉该领域的研究者来说并不意外；scope 过窄（2 轴 × 4 judges × 1 主 benchmark）降低了影响力 |
| Reproducibility | 4/5 | Appendix R 提供了详尽的实现细节（模型版本、温度、prompt），统计方法描述清晰，承诺 release code/data；但 NLI gate 的 prompt 和 rewriting prompt 的完整文本未在正文或附录中给出 |
| Reviewer Confidence | 4/5 | 仔细阅读了全文及全部附录，对统计方法和 LLM-as-judge 文献较为熟悉 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] 仅两个风格轴无法支撑 "Likert Blindspot" 的通用性 claim
- 具体位置：Abstract ("systematically divergent style sensitivity"), Section 1 ("a systematic pattern"), Title ("LLM Judge Style Evaluation")
- 问题：论文标题和摘要将 Likert Blindspot 定位为 LLM judge style 评估的通用现象，但实验仅覆盖 formality 和 verbosity（加上 Appendix 中的 register 作为探索性分析）。这三个轴均属表层文体属性（surface-level stylistic attributes），论文自身在 Limitations (page 9) 承认 semantic-level axes（hedging, humor, technicality）因 NLI gate 限制无法覆盖。仅基于两个高度相关的表层轴（verbosity 和 formality 在实践中常共变），就声称发现了 systematic pattern，存在过度概括风险。
- 为什么影响接收：一个声称发现"系统性"现象的论文，如果证据仅来自有限且同质的轴，会被质疑 claim 是否成立。如果 Blindspot 仅限于特定类型的风格轴，这仍然是有趣的但需要不同的 framing。
- 建议修改方向：(1) 弱化通用性 claim，明确限定为 "surface-level stylistic axes"；(2) 或增加至少 1-2 个语义层面的轴（如 hedging level, bullet-point vs prose）的实验证据，哪怕是 pilot scale；(3) 在 Abstract 和 Introduction 中明确表述 scope boundary。

**N2** [critical] 三种机制解释未能区分，限制了理论贡献
- 具体位置：Section 5.1 ("three non-exclusive explanations"), Limitations paragraph 1 ("The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences")
- 问题：论文提出 attenuation（Likert 衰减信号）、amplification（pairwise 放大信号）、construct divergence（两种模式测量不同构念）三种解释，但明确表示无法区分（"cannot be definitively resolved without human ground-truth"）。这三种解释有截然不同的实践含义：如果是 attenuation，则 Likert 需要修正；如果是 amplification，则 pairwise 结果可能夸大了真实偏差；如果是 construct divergence，则两种模式都是"正确的"只是测量不同的东西。
- 为什么影响接收：一篇 diagnostic 论文如果无法判断被诊断的现象究竟是什么（信号丢失 vs 信号放大 vs 不同构念），其理论贡献和实践指导价值会大打折扣。Section 5.1 提到"six experimental controls bound this risk (§5.4)"来 bound amplification，但 bounding 不等于排除。
- 建议修改方向：(1) 即使无法完全区分，可以通过 human evaluation 对少量 pairs 收集 ground-truth style ratings，然后比较 human 与 Likert/pairwise 的一致性，至少部分区分 attenuation vs amplification；(2) 更明确地讨论每种解释的证据权重，而非简单列举为 "non-exclusive"；(3) 如果无法增加实验，应在 framing 上更诚实地将这作为 open question 而非 contribution 的一部分。

**N3** [critical] 与 RATE (Reber et al., 2025) 的增量贡献需更清晰界定
- 具体位置：Section 2 Related Work (page 2-3), Section 5.1 ("Head-to-head comparison with RATE")
- 问题：RATE 已经建立了 style-rewriting + ATE 的方法框架，并发现 60% 的 style-transformed pairs 接受了 confounded 评分。CSD 的核心区别在于：(a) 引入 pairwise 比较模式揭示 mode divergence，(b) per-axis GEE decomposition，(c) NLI gating 替代 RATE 的 Likert ATE correction。但 Section 5.1 的 head-to-head 比较仅用了 1 段文字，且主要强调 RATE "may underestimate the true magnitude"——这个 claim 需要更强的证据支撑，因为 RATE 和 CSD 测量的是不同的量（RATE 测 ATE bias，CSD 测 mode divergence）。
- 为什么影响接收：如果 reviewer 认为 CSD 相对 RATE 的增量不够大（本质上是给 RATE 加了 pairwise 比较模式 + GEE），可能判断 novelty 不足。
- 建议修改方向：(1) 用一个结构化的对比表格明确列出 RATE vs CSD 在方法论、测量对象、发现上的区别；(2) 讨论 CSD 是否 subsume RATE 或两者是互补的；(3) 避免暗示 RATE "underestimates"——更精确地说是 RATE 测量的是不同的量。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Table 1 信息密度过高，可读性不佳
- 具体位置：Table 1 (page 6)
- 问题：Table 1 在一个表格中压缩了 5 个 judges × 3 benchmarks × 2 axes × 4 个统计量（ATE, BT, Likert(p), BT(p)）+ 脚注中的 scaled replication 和 negative control 信息。对于一篇以"发现 mode divergence"为核心贡献的论文，读者需要先理解这个复杂的表格才能把握核心结果，增加了认知负担。
- 建议：(1) 考虑将 LLMBar 主结果和 cross-benchmark replication 分成两个表格；(2) 或至少在正文中添加一段引导性的文字帮助读者 parse 表格（目前正文直接跳到 Section 5 Analysis）。

**W2** [warning] Figure 2 的 DAG 假设未充分讨论
- 具体位置：Figure 2 (page 4), Appendix A (page 10)
- 问题：Figure 2 呈现了一个 assumed data-generating process 的 DAG，但 Appendix A 立即声明 "we do not claim that the DAG in Figure 2 is a complete structural causal model"。然而，CSD 的整个方法论（NLI gating blocks H→Q, style-controlled rewriting isolates S→Y）都依赖于这个 DAG 的结构假设。如果 DAG 遗漏了重要的路径（例如 style 对 content quality 的直接效应 S→Q，或评估者的 prior expectations），方法论的有效性会受到影响。论文在 Limitations 中讨论了 quality-style confounding，但没有系统地讨论 DAG 可能遗漏的路径。
- 建议：在 Section 3 或 Appendix A 中增加对 DAG 假设的敏感性讨论：如果存在 S→Q 路径（style 影响 perceived quality），NLI gate 无法 block 这条路径，CSD 的结论会如何改变？

**W3** [warning] Negative control (Claude Sonnet 4) 的解释不够深入
- 具体位置：Section 4.1 (page 5, footnote), Appendix H (page 12)
- 问题：Claude Sonnet 4 被用作 negative control（"serves as a sensitivity check"），其 BT 在 formality 上 67.1%，接近但未达 significance。但 Limitations (page 9) 又提到 Claude Sonnet 4 的 "formality style sensitivity is consistently low across all three benchmarks (GEE Style OR 1.47–1.99, all n.s.)"。如果 Claude Sonnet 4 确实对 formality 不敏感，这是一个有价值的 negative control。但论文没有深入讨论：为什么 Claude 对 formality 不敏感？是因为训练数据不同？RLHF 策略不同？这个问题与 Blindspot 的机制解释有关。
- 建议：增加 1-2 句关于 negative control 结果的机制讨论，或至少说明为什么选择 Claude Sonnet 4 作为 negative control 的理由（目前只说"we pin versions for reproducibility"）。

**W4** [warning] Human annotation 验证的规模偏小
- 具体位置：Section 5.4 (page 8), Appendix U (page 16)
- 问题：内容保存验证由两位独立标注员对 50 对 NLI-scored pairs 进行标注（Annotator 1 判定 42/50 content-preserving，Annotator 2 判定 21/25 或 33/50）。κ = 0.44（moderate agreement）。50 对的样本量对于验证一个核心方法论假设（NLI gate 有效保存内容）来说偏小，且 moderate agreement 提示标注标准可能存在模糊性。
- 建议：(1) 扩大标注样本量至 100+ pairs；(2) 报告标注不一致的具体类型（是哪类内容变化被标注员发现但 NLI 未捕捉？）；(3) 讨论 κ = 0.44 对结论的影响。

## 小问题（不影响接收）

- **M1**: Section 3.1 (page 4) 的 rewriting prompt 示例（"Rewrite the following text to be more formal/casual while preserving the exact same content and meaning"）仅给了一个简短摘要，完整 prompt 应放在 Appendix 中供复现。
- **M2**: Table 2 (page 7) 中"Orig OR"列的含义在首次出现时未充分解释，需要回溯到 Section 5.2 才能理解这是 originality 的 odds ratio。建议在 table caption 中添加说明。
- **M3**: Section 5.3 (page 7-8) 的 cross-benchmark replication 部分，AlpacaEval 和 MT-Bench 的结果描述较为概括（"similar pattern"），但 Table 1 显示 MT-Bench 上的 BT 效应量（72.1%）低于 LLMBar（77.9%）和 AlpacaEval（77.3%），这个差异值得简短讨论。
- **M4**: References 格式：部分引用缺少 DOI 或会议信息（如 arXiv preprints 与正式发表版本混用），建议统一检查。
- **M5**: Limitations 第四段 (page 9) 提到 "100-point continuous scale does not resolve the Blindspot (Appendix O)"——这是一个重要的 robustness check，但仅用一个 judge (Qwen3-32B) 测试，建议在正文中明确标注这一限制。
- **M6**: Abstract 中 "six judges from independent providers" 但正文 Section 4.1 说 "four target judges" + negative control + scaled replication。建议措辞一致——Abstract 应说明 "four target judges from independent providers" 加 negative control。

## 主要优势

1. **方法论设计严谨**：NLI gating + position-controlled pairwise + per-axis decomposition 的组合是对 style bias 诊断方法论的合理改进。特别是 position control（每对比较交换顺序两次，nₚₐᵢᵣₛ × 2 observations）和 NLI content preservation gate 的设计体现了对 confound 控制的认真思考。

2. **统计分析全面**：论文使用了七种统计方法（Likert ATE, BT, sign test, Wilcoxon, Mann-Whitney, ordinal regression, GEE），并报告了 bootstrap 95% CI（Appendix J, 10,000 pair-level resamples）。GEE conditional decomposition（Table 2）揭示了 per-axis confound structure 是论文最有信息量的分析。

3. **Robustness checks 充分**：Appendix 覆盖了 threshold sensitivity (F), direction-aware gating (G), Claude equivalence testing (H), cross-axis contamination (T), rewriter independence (E), power analysis (L), bootstrap attenuation (K) 等多项检验。这种 thoroughness 在风格偏差文献中不常见。

4. **Limitations 诚实且全面**：四个段落覆盖了 quality-style confounding、evaluator-producer bias、scope boundary、validation methodology，且明确承认无法区分三种机制解释。这种诚实性值得肯定。

5. **写作结构清晰**：从 "Likert Blindspot" 现象的引出（Introduction 的 opening example）→ 方法论设计 → 实验验证 → 机制讨论的叙事逻辑流畅。Figure 1 的 CSD pipeline overview 有效传达了方法论全貌。

## 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文页数 | ✓ 8页 | Sections 1-6 恰好 8 页 |
| ACL 模板 | ✓ | `\usepackage[review]{acl}`，`\author{Anonymous}` |
| Double-blind 匿名性 | ✓ | 未发现作者身份泄露线索；无致谢、无 GitHub/个人链接 |
| Limitations section | ✓ | 在正文 Section 6 之后，unnumbered section，不计入 8 页限制 |
| 参考文献格式 | 基本一致 | 部分 arXiv preprint 与正式发表版本混用，建议统一 |
| Appendix | ✓ | 在 Limitations + Code and Data 之后，不计入页数 |

## Questions for Authors

1. 你们是否考虑过用 human raters 收集少量 ground-truth style bias ratings（例如 50 pairs），以部分区分 attenuation vs amplification？这似乎是区分三种机制解释最直接的方式。

2. Table 2 中 formality 的 Orig OR 在不同 judges 之间差异很大（GPT-4o: 0.49, Qwen3-32B: 0.38, Llama-70B: 1.06, Gemini: 0.46）——这是否暗示 formality 的 Blindspot 本质上是 judge-dependent 而非 mode-dependent？

3. CSD 方法论的 NLI gate 导致约 12% 的 pairs 被 reject（n=88 from n=100）。这些被 reject 的 pairs 是否有系统性偏差？例如，是否更倾向于 reject 某个方向的 rewriting（formal→casual vs casual→formal）？

4. 论文提到 "100-point continuous scale does not resolve the Blindspot"（Appendix O），但仅在 Qwen3-32B 上测试。是否有计划在多个 judges 上复现这个实验？

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

_source line 1198 · 2026-05-23T05:31:51.700374+00:00_

Reviewer 2 审稿意见已收到。评分 3.5/5 (Borderline Conference)，3 个 Must-Fix（通用性 claim 过强、三种机制未区分、与 RATE 增量不清晰）+ 4 个 Should-Fix。

等待 Reviewer 1 返回后启动交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1199 · 2026-05-23T05:31:58.014047+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

**总评：3.5 / 5（Borderline Conference）**

核心判断：方法论设计严谨（NLI gating + position-controlled pairwise + GEE decomposition），统计分析全面（七种方法 + 大量 robustness checks），写作清晰，格式合规。但三个 Must-Fix 问题限制了贡献：

1. **仅两个表层风格轴**无法支撑标题和摘要中"系统性现象"的 claim
2. **三种机制解释未区分**（attenuation / amplification / construct divergence），削弱理论贡献和实践指导价值
3. **与 RATE 的增量贡献**界定不够清晰——核心区别在于加了 pairwise 模式和 GEE，需要更 explicit 的对比论证

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

_source line 1200 · 2026-05-23T05:32:06.574407+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 115

## Round 115

6 recorded events


### User

_source line 1201 · 2026-05-23T05:32:38.149616+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 方法论扎实、统计处理详尽的诊断性工作，核心发现（Likert-pairwise divergence）有实证支撑且具实践意义，但对 divergence 的因果归因不够审慎、negative control 等效检验统计力不足、style axis 覆盖有限，使得结论的普适性存疑。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 核心方法（CSD pipeline + GEE decomposition）设计合理，7 种统计方法互相验证；但 NLI gate 与人工标注的一致性仅 moderate（κ=0.32-0.44），negative control 的 TOST 在 Δ=10pp 时失效（power≈42%），且对 divergence 的三种解释（attenuation / amplification / construct divergence）未能决定性区分，削弱了 "Likert Blindspot" 这一因果性命名的合理性。 |
| **Excitement** | 3.5 / 5 | 问题重要且切中实践痛点（RLHF/DPO 依赖 pairwise，evaluation 依赖 Likert），CSD 方法具有 reusable tool 价值；但论文主要 *诊断* 了问题而未提供 mitigation 路径，且仅覆盖 2 个 primary style axis，对社区的指导性有限。 |
| **Reproducibility** | 4 / 5 | 实现细节充分（Appendix R 列出模型版本、温度、seed 等），BT CI 和 GEE CI 均完整报告；代码和数据承诺 "released upon acceptance" 但当前不可用。 |
| **Confidence** | 4 / 5 | 本人熟悉 Bradley-Terry 模型、GEE、等效检验等统计方法，仔细核查了论文中的统计声明。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Likert Blindspot 的因果归因过度——论文自身证据无法排除 "construct divergence" 解释

- **具体位置**：Section 5.1（§95-101 experiments.tex）、Title、Abstract line 1-4
- **问题**：论文命名为 "The Likert Blindspot"，暗示 Likert 有 *缺陷*（blindspot = 盲区），但 Section 5.1 自己列出了三种 non-exclusive 解释：(a) Likert attenuation, (b) pairwise amplification, (c) construct divergence。论文承认 "the attenuation evidence (d→0 at n=355) is necessary but not sufficient for causal identification"，也承认 "definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs"（Limitations）。在这种无法区分的情况下，Title 和 framing 强烈偏向解释 (a)（Likert 有缺陷），而非中性的 "measurement-mode divergence"（虽然副标题包含此词，但 "Blindspot" 的修辞效果远强于副标题）。
  
  更关键的是：pairwise comparison 相比 absolute rating 具有更高判别力是 psychometrics 自 Thurstone (1927) 以来的已知现象——论文自身也引用了此文。power analysis 显示 Likert 需要 4-206× 的样本量才能检测到 BT 捕获的效应——这 *完全一致于* 相对判断 vs 绝对判断的已知灵敏度差异，不需要 "blindspot" 这一因果性解释。论文需要更充分地论证：为什么观察到的 divergence *不仅仅是* 已知的 format sensitivity 差异？
  
- **为什么影响接收**：标题和核心 framing 的因果暗示超出了实验证据的支撑范围，是 overclaiming。
- **建议修改方向**：
  1. 在 Introduction 和 Analysis 中给 construct divergence 解释同等的篇幅和权重，而非将其作为 Limitations 的一个段落
  2. 明确讨论 Thurstone (1927) 的 discriminability 差异如何与本文发现对齐或区分
  3. 考虑将 "Blindspot" 改为更中性的术语（如 "Likert-Pairwise Gap"），或在正文中明确定义 "Blindspot" 为一个操作性描述（divergence 现象的名称）而非因果性声明

---

**N2** [critical] Negative control (Claude Sonnet 4) 的等效检验统计力严重不足

- **具体位置**：Appendix G（Table 9, app:claude_tost）；Section 5.1 第 97 行
- **问题**：Claude Sonnet 4 作为 negative control 是实验设计的关键支柱——用于证明 "有的 judge 不展示 Blindspot，因此 Blindspot 不是 format 的固有属性"。但 TOST 等效检验在 Δ=15pp 时才达到显著（p=0.010），而 15pp 对应的 BT=65% 在实践中是一个 *相当大* 的偏好差异。在 Δ=10pp（一个更合理的实际显著性门槛）时，TOST 不显著（p=0.156, power≈42%）。论文自己承认 "the minimum equivalence margin achieving 80% power at n=88 is Δ=15.7pp"。

  这意味着：我们无法在 n=88 的情况下区分 "Claude 没有 style bias" 和 "Claude 有 10pp 的 style bias"。Claude 的 BT 值为 56.2%（formality）和 54.1%（verbosity），虽然接近 50%，但 6.2pp 的偏差在 n=88 下完全可能反映真实的 moderate effect。
  
- **为什么影响接收**：negative control 的有效性直接关系到 "Blindspot 是 judge-specific 而非 format-inherent" 这一核心论点。如果 negative control 失效，则 N1 中的 "construct divergence" 解释变得更强。
- **建议修改方向**：
  1. 扩大 negative control 样本量至少到 n=200+，使 Δ=10pp 的 TOST 达到合理 power
  2. 或者诚实地将 negative control 结论降级为 "suggestive but underpowered"，不将其作为排除 format-inherent 解释的主要证据
  3. 增加第二个 negative control judge 以增强说服力

---

**N3** [critical] 样本量 n=88 下 GEE decomposition 的可靠性存疑

- **具体位置**：Table 2（主文 p.7）；Section 4.1；Appendix D
- **问题**：GEE conditional decomposition 是本文方法的核心创新之一——将 BT 的整体偏好分解为 style 和 originality 两个分量。但在 n=88（176 observations for binary outcome）的条件下，logistic GEE 需要估计的参数虽然少（intercept + 2 predictors），但 CI 极宽：例如 Qwen3 verbosity Style OR = 13.10 [5.62, 30.55]——95% CI 跨越了将近 6 倍的范围。Gemini formality Style OR = 1.64 [0.91, 2.98] 的 CI 包含 1.0，即不显著。

  更重要的是，n=88 下交互效应检验的 power 极低。Table 4 报告所有交互项 p > 0.13，但 OR 值波动很大（0.45 到 2.60），这些 p 值更可能反映 power 不足而非真正的 null。论文不能基于 non-significant interaction 就断言 additive model 正确。
  
- **为什么影响接收**：GEE 是区分 "style-dominated" vs "quality-confounded" 的唯一工具。如果在 n=88 下 GEE 的 effect size 估计不稳定（n=88 到 n=355 的 Qwen3 formality Style OR 从 4.20 降到 2.15，缩水 49%），那么基于小样本 GEE 得出的 per-judge regime classification 的可靠性令人怀疑。
- **建议修改方向**：
  1. 对所有 judge×axis 组合进行 n=355 级别的 scaled replication（目前只有 Qwen3 formality 做了）
  2. 至少报告 GEE 的 power analysis 或 minimum detectable OR
  3. 讨论 n=88→n=355 时 Qwen3 Style OR 缩水 49% 的含义——是否其他 judge 的 OR 也可能被高估？

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Style axis 覆盖窄（2 个 primary + 1 个 exploratory），限制了方法的普适性声明

- **具体位置**：Section 3.1；Limitations 段落 3（line 56-62 main.tex）
- **问题**：CSD 作为 "black-box diagnostic methodology" 被提出，但仅在 formality 和 verbosity 上充分验证。Register 是 exploratory pilot（且有 evaluator-producer overlap）。论文 Limitations 承认 hedging/humor/technicality 等语义级 axes 会被 NLI gate 系统性拒绝（55% rejection rate for tone axis pilot），这实际上将 CSD 限制在 surface-level stylistic attributes。但 Abstract 和 Introduction 的 framing 没有充分反映这一限制。
- **建议**：在 Abstract 中加入 "surface-level style axes" 的限定语；讨论 CSD 对语义密集型 style axes 的 fundamental limitation。

**W2** [warning] Cross-axis contamination 中 FK grade 变化的处理不够严谨

- **具体位置**：Appendix T (Table 19)
- **问题**：Verbosity rewrites 导致 FK grade d=0.50（medium effect），论文将其归因于 "sentence length dependence"。但 FK grade 同时反映 formality 相关的词汇复杂度，d=0.50 的 cross-axis 泄漏对于一个声称隔离单一 axis 的方法来说并非 trivial。论文的解释（句子长度的 artifact）是合理的但未被正式验证——例如，可以在控制句子长度后重新计算 FK grade shift。
- **建议**：对 FK grade 做 length-controlled 分析，或至少讨论这个 d=0.50 对 formality×verbosity 交互的潜在影响。

**W3** [warning] Evaluator-producer overlap 的 mitigation 只测试了一个替代 rewriter

- **具体位置**：Appendix E (Table 6, Table 7)
- **问题**：Qwen3-32B 同时做 rewriter 和 judge 是一个 known confound。论文用 GPT-4o 作为替代 rewriter 进行 independence test——结果显示 Style OR 下降 22%（13.10→10.17 for verbosity）。这是一个有意义的 check，但：(a) 只测试了一个替代配置；(b) 22% 的 OR 下降并不小；(c) 没有用第三个 rewriter 确认趋势是否稳定。
- **建议**：增加至少一个额外的 rewriter（如 Llama 或 Gemini）做 independence test，或至少讨论 22% 下降的上界含义。

**W4** [warning] IIA assumption 的讨论不充分

- **具体位置**：Section 4.1 footnote（experiments.tex line 12）
- **问题**：论文在脚注中声称 "In binary-choice BT models, IIA is structurally satisfied"，然后将 formality 的 direction asymmetry 解释为 "heterogeneous treatment effects across style directions rather than IIA violation"。但 IIA 的 structural satisfaction 仅在每对选手只比一次的情况下成立。在本文设计中，同一文本对在不同 style conditions 下反复出现，共享 source text 带来的依赖性可能系统性违反 IIA。GEE 部分用了 exchangeable correlation 来处理组内相关，但 BT model 本身没有类似的修正。
- **建议**：在正文而非脚注中讨论 IIA，并明确说明 GEE 如何补充 BT 在这方面的不足。

**W5** [warning] 100-point continuous Likert scale 实验仅用了一个 judge

- **具体位置**：Appendix O
- **问题**：100-point scale 实验（旨在排除 scale granularity 解释）仅在 Qwen3-32B 上进行。如果 Blindspot 的表现因 judge 而异（如 Gemini 的 formality 就明显更弱），单一 judge 的 100-point 实验不足以支持 "granularity is not the issue" 的一般性结论。
- **建议**：至少在两个 judge 上 replicate 100-point scale 实验。

---

## 小问题（不影响接收）

1. **Table 1 排版密度过高**：15 行结果 + 6 行脚注在一个 Table 中，阅读体验较差。建议将 LLMBar primary results 和 cross-benchmark replication 分为两个表。
2. **"style bias" vs "style sensitivity" 措辞不一致**：两个术语在文中交替使用但含义略有不同（bias 暗示方向性，sensitivity 暗示双向的响应性）。建议统一或明确区分。
3. **Figure 2 (DAG) 的 dashed orange S→Q path** 标为 "residual confound"，但 caption 说 "style may influence perceived quality through channels the NLI gate cannot block"——这条路径实际上是一个 *acknowledged unblocked confounder*，建议在 caption 中更明确地标示其含义。
4. **Appendix 编号**：组织标记为 A*-T，但部分 appendix 在 PDF 中的实际编号难以跟踪（如 "Appendix T" 实际是 "Cross-Axis Contamination"），建议统一命名和交叉引用。
5. **Section 3.5 Design Rationale** 位置偏后——读者在读完 Section 3.1-3.4 后才看到实验设计的 causal justification。建议提前到 Section 3.1 之前或合并为 Section 3 的开头段落。

---

## 主要优势

1. **统计处理的深度和透明度是本文最大的亮点**。7 种统计方法（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Mann-Whitney）互相验证，bootstrap CI 10,000 次 resamples，power analysis，bootstrap attenuation analysis，NLI threshold sweep——这在 NLP 论文中罕见，树立了方法论论文的高标准。
2. **GEE conditional decomposition 是一个有价值的分析工具**，将 BT 的整体偏好分解为 style 和 originality 两个分量，揭示了 verbosity（style-dominated）和 formality（conditionally style-driven）的结构性差异。即使 n=88 的 CI 较宽，这个分析框架本身有独立的方法论贡献。
3. **实验设计的 confounder control 策略周全**：NLI gate + position swap + same-style double-rewrite control + direction-aware gating for verbosity——形成了多层防线。每一层都有对应的 validation（human annotation for NLI, consistency filter robustness for position swap 等）。
4. **Six controls for amplification risk (§5.4)** 是对 Comparative Trap (Jeong et al., 2025) 的直接回应，体现了对潜在反驳的主动防御。
5. **Bootstrap attenuation analysis (Appendix K)** 提供了区分 power limitation 和 measurement attenuation 的巧妙方法——d 收敛到 0 而非保持 non-zero 是 Likert signal genuinely absent 的强证据。
6. **Limitations 部分坦诚且全面**，主动列出了 quality-style confounding、evaluator-producer bias、ecological validity 等限制，没有试图掩盖弱点。


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

_source line 1202 · 2026-05-23T05:33:14.242243+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix / Should-Fix / Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 仅两个风格轴无法支撑 \"Likert Blindspot\" 的通用性 claim\n- Abstract (\"systematically divergent style sensitivity\"), Section 1 (\"a systematic pattern\"), Title (\"LLM Judge Style Evaluation\")\n- 论文标题和摘要将 Likert Blindspot 定位为 LLM judge style 评估的通用现象，但实验仅覆盖 formality 和 verbosity + 探索性的 register。这三个轴均属表层文体属性，Limitations 承认 semantic-level axes 因 NLI gate 限制无法覆盖。仅基于两个高度相关的表层轴就声称 systematic pattern，存在过度概括风险。\n\n**N2** [critical] 三种机制解释未能区分，限制了理论贡献\n- Section 5.1 (\"three non-exclusive explanations\"), Limitations paragraph 1\n- 论文提出 attenuation/amplification/construct divergence 三种解释但明确表示无法区分。这三种解释有截然不同的实践含义。一篇 diagnostic 论文如果无法判断被诊断的现象究竟是什么，其理论贡献和实践指导价值大打折扣。\n\n**N3** [critical] 与 RATE (Reber et al., 2025) 的增量贡献需更清晰界定\n- Section 2, Section 5.1 (\"Head-to-head comparison with RATE\")\n- RATE 已建立 style-rewriting + ATE 框架。CSD 核心区别在于引入 pairwise + GEE + NLI gating。但 head-to-head 比较仅用 1 段文字，且 claim RATE \"may underestimate\" 需更强证据。\n\n### Should-Fix 问题\n\n**W1** Table 1 信息密度过高，可读性不佳\n**W2** Figure 2 的 DAG 假设未充分讨论\n**W3** Negative control (Claude Sonnet 4) 的解释不够深入\n**W4** Human annotation 验证的规模偏小（50 pairs, κ=0.44）\n\n### Minor Issues\n**M1** Rewriting prompt 完整文本未给出\n**M2** Table 2 \"Orig OR\" 首次出现时未解释\n**M3** Cross-benchmark BT 效应量差异未讨论\n**M4** References 格式不完全一致\n**M5** 100-point scale 仅测试一个 judge\n**M6** Abstract 中 judge 数量表述与正文不一致\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。",
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix / Should-Fix / Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 仅两个风格轴无法支撑 \"Likert Blindspot\" 的通用性 claim\n- Abstract (\"systematically divergent style sensitivity\"), Section 1 (\"a systematic pattern\"), Title (\"LLM Judge Style Evaluation\")\n- 论文标题和摘要将 Likert Blindspot 定位为 LLM judge style 评估的通用现象，但实验仅覆盖 formality 和 verbosity + 探索性的 register。这三个轴均属表层文体属性，Limitations 承认 semantic-level axes 因 NLI gate 限制无法覆盖。仅基于两个高度相关的表层轴就声称 systematic pattern，存在过度概括风险。\n\n**N2** [critical] 三种机制解释未能区分，限制了理论贡献\n- Section 5.1 (\"three non-exclusive explanations\"), Limitations paragraph 1\n- 论文提出 attenuation/amplification/construct divergence 三种解释但明确表示无法区分。这三种解释有截然不同的实践含义。一篇 diagnostic 论文如果无法判断被诊断的现象究竟是什么，其理论贡献和实践指导价值大打折扣。\n\n**N3** [critical] 与 RATE (Reber et al., 2025) 的增量贡献需更清晰界定\n- Section 2, Section 5.1 (\"Head-to-head comparison with RATE\")\n- RATE 已建立 style-rewriting + ATE 框架。CSD 核心区别在于引入 pairwise + GEE + NLI gating。但 head-to-head 比较仅用 1 段文字，且 claim RATE \"may underestimate\" 需更强证据。\n\n### Should-Fix 问题\n\n**W1** Table 1 信息密度过高，可读性不佳\n**W2** Figure 2 的 DAG 假设未充分讨论\n**W3** Negative control (Claude Sonnet 4) 的解释不够深入\n**W4** Human annotation 验证的规模偏小（50 pairs, κ=0.44）\n\n### Minor Issues\n**M1** Rewriting prompt 完整文本未给出\n**M2** Table 2 \"Orig OR\" 首次出现时未解释\n**M3** Cross-benchmark BT 效应量差异未讨论\n**M4** References 格式不完全一致\n**M5** 100-point scale 仅测试一个 judge\n**M6** Abstract 中 judge 数量表述与正文不一致\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-23T05:33:36.655633+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22413
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-23T05:33:37.057218+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix / Should-Fix / Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Likert Blindspot 的因果归因过度——论文自身证据无法排除 \"construct divergence\" 解释\n- Title 的 \"Blindspot\" 暗示 Likert 有缺陷，但 Section 5.1 列出三种 non-exclusive 解释且无法区分。pairwise > Likert 的判别力是 Thurstone (1927) 以来的已知现象。power analysis 显示 Likert 需 4-206× 样本量——完全一致于已知的 format sensitivity 差异。论文需论证为何观察到的 divergence 不仅仅是已知的 format sensitivity 差异。建议：(1) 给 construct divergence 同等篇幅；(2) 讨论 Thurstone discriminability；(3) 考虑更中性的术语。\n\n**N2** [critical] Negative control (Claude Sonnet 4) 的等效检验统计力严重不足\n- TOST 在 Δ=15pp 才显著（p=0.010），但 15pp 对应 BT=65% 是相当大的偏好差异。Δ=10pp 时 TOST 不显著（p=0.156, power≈42%）。无法区分 \"Claude 没有 style bias\" 和 \"Claude 有 10pp style bias\"。BT=56.2% 的 6.2pp 偏差可能反映真实 moderate effect。建议：扩大 n 到 200+，或降级 negative control 结论为 \"suggestive but underpowered\"。\n\n**N3** [critical] 样本量 n=88 下 GEE decomposition 的可靠性存疑\n- Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，CI 跨越近 6 倍。n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%）。交互效应检验 power 极低（OR 从 0.45 到 2.60 但 all p>0.13）。建议：对所有配置做 n=355 级别 scaled replication，或至少讨论 OR 缩水的含义。\n\n### Should-Fix 问题\n\n**W1** Style axis 覆盖窄（2 primary + 1 exploratory），限制普适性\n**W2** Cross-axis contamination 中 FK grade d=0.50 处理不够严谨\n**W3** Evaluator-producer overlap 的 mitigation 只测试了一个替代 rewriter\n**W4** IIA assumption 讨论不充分（仅在脚注中）\n**W5** 100-point continuous Likert scale 仅用一个 judge\n\n### Minor Issues\n1. Table 1 排版密度过高\n2. \"style bias\" vs \"style sensitivity\" 措辞不一致\n3. Figure 2 DAG 的 S→Q path caption 不够明确\n4. Appendix 编号难以跟踪\n5. Section 3.5 Design Rationale 位置偏后\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。",
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix / Should-Fix / Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Likert Blindspot 的因果归因过度——论文自身证据无法排除 \"construct divergence\" 解释\n- Title 的 \"Blindspot\" 暗示 Likert 有缺陷，但 Section 5.1 列出三种 non-exclusive 解释且无法区分。pairwise > Likert 的判别力是 Thurstone (1927) 以来的已知现象。power analysis 显示 Likert 需 4-206× 样本量——完全一致于已知的 format sensitivity 差异。论文需论证为何观察到的 divergence 不仅仅是已知的 format sensitivity 差异。建议：(1) 给 construct divergence 同等篇幅；(2) 讨论 Thurstone discriminability；(3) 考虑更中性的术语。\n\n**N2** [critical] Negative control (Claude Sonnet 4) 的等效检验统计力严重不足\n- TOST 在 Δ=15pp 才显著（p=0.010），但 15pp 对应 BT=65% 是相当大的偏好差异。Δ=10pp 时 TOST 不显著（p=0.156, power≈42%）。无法区分 \"Claude 没有 style bias\" 和 \"Claude 有 10pp style bias\"。BT=56.2% 的 6.2pp 偏差可能反映真实 moderate effect。建议：扩大 n 到 200+，或降级 negative control 结论为 \"suggestive but underpowered\"。\n\n**N3** [critical] 样本量 n=88 下 GEE decomposition 的可靠性存疑\n- Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，CI 跨越近 6 倍。n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%）。交互效应检验 power 极低（OR 从 0.45 到 2.60 但 all p>0.13）。建议：对所有配置做 n=355 级别 scaled replication，或至少讨论 OR 缩水的含义。\n\n### Should-Fix 问题\n\n**W1** Style axis 覆盖窄（2 primary + 1 exploratory），限制普适性\n**W2** Cross-axis contamination 中 FK grade d=0.50 处理不够严谨\n**W3** Evaluator-producer overlap 的 mitigation 只测试了一个替代 rewriter\n**W4** IIA assumption 讨论不充分（仅在脚注中）\n**W5** 100-point continuous Likert scale 仅用一个 judge\n\n### Minor Issues\n1. Table 1 排版密度过高\n2. \"style bias\" vs \"style sensitivity\" 措辞不一致\n3. Figure 2 DAG 的 S→Q path caption 不够明确\n4. Appendix 编号难以跟踪\n5. Section 3.5 Design Rationale 位置偏后\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。",
    "project": "causal_style_decomp_judge",
    "chat_id": "oc_f810d8d75f013ad17831ce8459f07d6d"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-23T05:33:38.415531+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 1206 · 2026-05-23T05:33:43.475361+00:00_

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


## Round 116

## Round 116

2 recorded events


### User

_source line 1207 · 2026-05-23T05:33:46.036585+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.5。

核心问题三个：
1. **N1**："Likert Blindspot" 的因果归因超出证据——论文自身承认三种解释无法区分，但标题和 framing 强烈偏向 "Likert 有缺陷"，而 pairwise vs absolute rating 的灵敏度差异是 Thurstone (1927) 以来的已知现象
2. **N2**：Negative control (Claude Sonnet 4) 的 TOST 在 Δ=10pp 时失效（power≈42%），无法排除 Claude 有 moderate style bias 的可能
3. **N3**：n=88 下 GEE decomposition 的 CI 极宽（Style OR CI 跨 6 倍），且 n=88→n=355 时 Qwen3 Style OR 缩水 49%，其他 judge 的 regime classification 可靠性存疑

主要优势：统计处理深度罕见（7 种方法互验证 + bootstrap attenuation + power analysis），GEE decomposition 框架有独立方法论价值，confounder control 策略周全。

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

_source line 1208 · 2026-05-23T05:33:50.731040+00:00_

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


## Round 117

## Round 117

2 recorded events


### User

_source line 1209 · 2026-05-23T05:35:12.015182+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 仅两个风格轴无法支撑通用性 claim**

同意。这与我自己审稿的 W1 一致。论文仅在 formality 和 verbosity 两个 primary axis 上进行了充分验证，register 为 exploratory 且存在 evaluator-producer overlap（Limitations line 52: "Register results carry the highest evaluator-producer risk"）。Limitations 还承认 semantic-level axes（hedging, humor, technicality）会被 NLI gate 系统性拒绝（line 57-58: "the NLI gate correctly rejected 55% of rewrites because epistemic commitment changes violate content equivalence"）。在仅有 2 个 surface-level axis 的证据下，Abstract 的 "systematically divergent style sensitivity" 和 Title 的 "LLM Judge Style Evaluation" 的确存在过度概括。

补充我的发现：这两个 axis 本身也并非完全独立——Appendix T (Table 19) 显示 verbosity 操纵导致 FK grade d=0.50 的 cross-axis 泄漏（我在 W2 中提出），说明 formality 和 verbosity 之间有结构性相关，进一步削弱了仅凭两个 axis 支撑通用性声明的合理性。

---

**[AGREE] R2-N2: 三种机制解释未能区分，限制理论贡献**

强烈同意。这是我自己审稿 N1 的核心论点。论文在 Section 5.1 (experiments.tex line 95) 明确列出三种 non-exclusive 解释，并承认 "the attenuation evidence (d→0 at n=355) is necessary but not sufficient for causal identification"（line 96）。Limitations 进一步承认 "definitive resolution requires human evaluation comparing Likert and pairwise judgments on identical pairs"（line 45）。

在无法区分三种机制的情况下，"Blindspot" 这一命名暗示 Likert 有缺陷（解释 a），而非中性地描述 divergence 现象。如果最终解释是 construct divergence（解释 c），那么 Likert 和 pairwise 只是在测量不同的东西，没有任何一方有 "盲区"——实践含义截然不同。论文的理论贡献因此受限于 "诊断出了 divergence 现象" 而非 "解释了 divergence 机制"。

---

**[REBUT] R2-N3: 与 RATE 的增量贡献需更清晰界定**

不完全同意。R2 称 "head-to-head 比较仅用 1 段文字" 且增量贡献不清晰，但论文实际上在多个层面展示了与 RATE 的结构性差异：

1. **RATE 在设计上无法检测 Blindspot**：RATE 仅使用 Likert ATE（Section 5.1, line 80），因此从结构上不可能发现 Likert-pairwise divergence——这正是 CSD 的核心发现。head-to-head 比较（同一数据：RATE d=0.10 n.s. vs CSD BT=63% p=0.0004）不是 "仅用 1 段文字" 的简单比较，而是一个 *构造性* 的论证：同一数据在不同 measurement mode 下给出截然不同的结论。

2. **GEE conditional decomposition 是方法论层面的新贡献**：RATE 不提供 per-axis confound structure 分析。Table 2 的 GEE 分解揭示了 verbosity（Style OR 8-13, Orig OR <1, style-dominated）和 formality（Style OR 2-5, Orig OR 2-5, conditionally style-driven）的结构性差异——这一发现无法从 RATE 框架中获得。

3. **NLI gating 策略不同**：CSD 使用 DeBERTa-v3-large + axis-dependent 方向感知 gating（Section 3.2, Appendix G），RATE 使用不同的 content preservation 方法。

4. **Related Work (Section 2)** 明确定位了差异：CSD "intervenes on specific style axes rather than general attributes" 且 "uses a sign test with position control rather than parametric aggregation."

但我同意 R2 的一个 subpoint：论文关于 RATE "may underestimate" 的 claim（Section 2: "RATE's own style-related findings may underestimate the true magnitude of attribute effects"）确实需要更谨慎的措辞——这是一个 *推测*，不是经过 controlled comparison 验证的结论。

---

### Should-Fix 问题

**[AGREE] R2-W1: Table 1 信息密度过高**

同意。这与我的 Minor Issue #1 一致。15 行结果 + 6 行脚注挤在一个 Table 中，跨 3 个 benchmark、5 个 judge、3 个 axis，读者很难快速提取关键 pattern。建议拆分为 primary (LLMBar) 和 cross-benchmark replication 两个表。

---

**[REBUT] R2-W2: Figure 2 DAG 假设未充分讨论**

不完全同意。论文实际上在多个位置讨论了 DAG 的假设和局限性：

- Figure 2 caption 明确声明 "design rationale, not a claim of perfect identification"
- Appendix A (Design Rationale, appendix.tex line 12) 明确说明 "we do not claim that the DAG in Figure 2 is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"
- 识别条件三条假设在 Appendix A line 13-14 中列出
- Limitations paragraph 1 (main.tex line 41-46) 详细讨论了 quality-style confounding 的不可分性
- Dashed orange S→Q path 在 caption 中标为 "residual confounding"

DAG 的每条路径——R→Q (NLI gate blocked), R→Y (double-rewrite control), P→Y (position swap), S→Q (residual confound, acknowledged)——都有对应的 control 或 acknowledgment。我认为讨论已足够充分。不过我同意 DAG 中 S→Q 的 dashed orange path 可以在 caption 中更明确地说明为 "acknowledged unblocked confounder"（这是我 Minor Issue #3 中提到的点）。

---

**[AGREE] R2-W3: Negative control 解释不够深入**

强烈同意，且我认为这应升级为 Must-Fix。这是我自己审稿中的 N2。TOST 在 Δ=10pp 时失效（p=0.156, power≈42%; Appendix G Table 9），15pp 的等效边界在实践中过宽。Claude BT=56.2%/54.1% 虽接近 50%，但在 n=88 下无法排除 moderate effect。论文自己承认 minimum equivalence margin achieving 80% power 是 Δ=15.7pp（appendix.tex line 227）。

---

**[AGREE] R2-W4: Human annotation 规模偏小**

部分同意。50 pairs 的标注量确实偏小，且 κ=0.44（moderate）和 Gwet's AC1=0.65（substantial）之间的差距主要由 prevalence effect 解释（Section 5.4, line 177）。但关键指标是 pass precision：A1 100% [86.7%, 100%], A2 84% [65.3%, 93.6%]（experiments.tex line 176）。A2 的 84% 下界仅 65.3%，这意味着在 worst case 下，最多有约 1/3 的 gate-passed pairs 可能包含内容变化——这对 style-only intervention 的声明有实质性影响。

我的补充：论文还报告了 GPT-4o cross-validation 的 pass precision（main.tex line 66: "92.1% formality / 82.6% verbosity"），但这是 LLM cross-validation 而非独立人工验证。总体而言，50 pairs 的标注规模对于一篇以 content preservation 为核心假设的论文来说偏小，建议至少增加到 100 pairs 并覆盖所有 axis。

---

### Minor Issues

**[AGREE] R2-M1**: Rewriting prompt 完整文本确实应在 Appendix 中给出。Section 3.1 仅给出了一个 paraphrase-level 的示例（method.tex line 9: "Rewrite the following text to be more formal/casual while preserving the exact same content and meaning"），不确定这是否是实际使用的完整 prompt。

**[AGREE] R2-M2**: "Orig OR" 在 Table 2 中首次出现时，虽然 caption 提到 "originality effects"，但 "Orig OR" 的缩写未解释。建议在 caption 或正文中首次引用时展开为 "Originality OR (original-preference odds ratio)"。

**[REBUT] R2-M3**: 不同意 "cross-benchmark BT 效应量差异未讨论"。论文在 Section 5.3 (experiments.tex line 164-165) 明确讨论了 severity spectrum："Llama-70B formality on AlpacaEval (BT 75.6%, d=1.12, p<.001) is strong enough for Likert detection"，并在 Section 5.1 line 84 说明 "at stronger effects (BT>70%), Likert partially detects but attenuates >60%"。三个 exceptions（Table 1 中的 ‡ rows）被解释为 effect-size dependent escape from the Blindspot。这个讨论是充分的。

**[AGREE] R2-M4**: References 格式一致性应检查。

**[AGREE] R2-M5**: 与我的 W5 一致。100-point scale 实验仅在 Qwen3-32B 上进行，至少应在 2 个 judge 上 replicate。

**[REBUT] R2-M6**: 不同意 "Abstract 中 judge 数量表述与正文不一致"。Abstract 明确说 "Across four judges from independent providers, one negative control"（PDF p.1），正文 Section 4.1 (experiments.tex line 17) 列出 4 个 target judges + Claude Sonnet 4 作为 negative control = 5 个 judge，与 Abstract 一致。如果 R2 指的是其他不一致之处，请指明具体位置。


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

_source line 1210 · 2026-05-23T05:35:21.446451+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1211 · 2026-05-23T05:35:27.232214+00:00_

[Reviewer 1 审稿结果]:
审稿回应已提交。对 R2 的 13 个问题：

- **5 项 AGREE**（N1 style axis 覆盖窄、N2 三种机制未区分、W1 Table 1 密度、W3 negative control 不足、W4 标注规模小）
- **3 项 REBUT**（N3 与 RATE 增量贡献实际已充分展示、W2 DAG 假设讨论已足够、M3 cross-benchmark 差异已讨论、M6 Abstract 数量一致）
- **5 项 Minor AGREE**（M1 prompt 文本、M2 术语解释、M4 引用格式、M5 100-point 单 judge）

关键交叉发现：R2-N1 和 R2-N2 与我的 N1 和 W1 高度一致，形成两位 reviewer 的共识——论文的核心弱点在于 (1) style axis 覆盖有限导致通用性 claim 过强，(2) 三种机制解释未能区分导致 "Blindspot" 命名的因果暗示超出证据范围。R2-W3 与我的 N2 一致，negative control 的统计力问题也是共识。

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

_source line 1212 · 2026-05-23T05:35:36.952539+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 119

## Round 119

24 recorded events


### User

_source line 1213 · 2026-05-23T05:35:40.002762+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Likert Blindspot 的因果归因过度**

同意 R1 的核心论点。我在自己的审稿中也提出了高度相关的问题（R2-N2: 三种机制解释未能区分）。补充以下观察：

1. **"Blindspot" 术语的规范性含义**：R1 指出 "Blindspot" 暗示 Likert 有缺陷，这与论文自身 Section 5.1 承认的三种 non-exclusive 解释矛盾。论文 Limitations 第一段明确写到 "An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference"——如果作者自己承认这可能只是 construct difference 而非 measurement failure，那么 "Blindspot" 这个带有价值判断的术语就不够准确。

2. **Thurstone discriminability 的遗漏**：R1 指出 pairwise > Likert 的判别力自 Thurstone (1927) 以来就是已知现象，这一点论文确实没有充分讨论。Section 2 Related Work 引用了 Thurstone (1927)，但仅在 "Measurement Sensitivity in NLG Evaluation" 段落中提到 "forced-choice comparisons yield finer discriminability than absolute ratings"，没有将自己的 power analysis（Figure 4）与这一经典结果做对比。如果 Figure 4 显示的 4-206× 样本量差异完全可以用 Thurstone discriminability 解释，那么 Likert Blindspot 可能并非新发现，而只是经典 psychometric 结果在 LLM judge 场景下的复现。

3. **但 GEE decomposition 部分超越了 Thurstone**：我认为论文的 GEE conditional decomposition（Table 2）揭示的 per-axis confound structure（verbosity style-dominated vs formality conditional on originality）不能仅用 Thurstone discriminability 解释。这个 per-axis 差异是论文的独特贡献，R1 的批评应主要针对 "mode divergence" 的 framing，而非整个论文。

**建议**：弱化 "Blindspot" 的规范性含义，在 Introduction 中给 construct divergence 解释更多篇幅，并在 Section 2 中讨论 Thurstone discriminability 与本文发现的关系。

---

**[AGREE] R1-N2: Negative control TOST 统计力不足**

完全同意。这是一个我在自己审稿中未充分展开但现在认为重要的问题。

1. **Δ=15pp 的等效界限过于宽松**：Appendix H (Table 9) 显示 TOST 在 Δ=15pp 时 p=0.010，但 BT=65% 对应的 15pp 偏差在 style preference 语境下是相当大的效应。以论文自身的 BT 结果为参照，GPT-4o 在 formality 上的 BT=63.0%（即 13pp 偏差）被论文视为 "significant style preference"——那么 Δ=15pp 的等效界限几乎涵盖了论文自己认定为显著的效应量。

2. **BT=56.2% 的实际含义**：Claude Sonnet 4 的 BT=56.2%（formality）意味着在 56.2% 的配对中偏好 formal 变体。6.2pp 的偏差虽然不大，但 Appendix H 报告 TOST 在 Δ=10pp 时 p=0.156, power≈42%，无法排除这是一个 moderate effect。

3. **对论文结论的影响**：如果 negative control 无法可靠地排除 style bias，那么 "Claude as negative control confirms the Blindspot is judge-dependent" 的 claim（Section 4.1, footnote; Limitations page 9）就需要降级。

**建议**：与 R1 一致——扩大 n 到 200+，或将 negative control 结论降级为 "suggestive but underpowered"。

---

**[AGREE] R1-N3: GEE decomposition 在 n=88 下的可靠性**

同意这是一个需要认真对待的统计问题。

1. **CI 宽度问题**：Table 2 中 Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，95% CI 跨越近 6 倍。Table 5 (Appendix, page 11) 进一步证实了这个问题：许多 GEE OR 的 CI 覆盖范围很大。这意味着点估计的精度很低，不应过度解读具体数值。

2. **OR 缩水现象**：R1 指出 n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%）。这可能反映：(a) 小样本下的偶然高估（regression to the mean），(b) n=355 的样本组成不同（scaled replication 可能覆盖不同的 text 类型），或 (c) 真实效应确实被 n=88 高估。论文未讨论这个缩水现象。

3. **交互效应检验 power**：Table 4 (Appendix, page 11) 报告 Style × Originality 交互效应全部不显著（all p>0.13），但在 n=88 下检测交互效应本就需要更大的样本量。论文基于非显著交互效应确认 additive model——但 absence of evidence ≠ evidence of absence。

4. **与我的审稿互补**：我在 R2-N1 中指出仅两个轴限制了通用性，R1-N3 从统计精度角度进一步质疑了即便在现有轴上结论的稳健性。两个问题叠加时更为严重。

**建议**：同意 R1——至少在 verbosity 轴上也做 n=355 级别的 scaled replication（目前仅 formality 有），并在正文中讨论 OR 缩水的含义。

---

### Should-Fix 问题

**[AGREE] R1-W1: Style axis 覆盖窄**

完全同意，与我的 R2-N1 一致。我将此列为 Must-Fix，R1 列为 Should-Fix，但核心关切相同：两个 primary axis + 一个 exploratory axis 无法支撑论文标题和 Abstract 中的通用性 claim。

---

**[AGREE] R1-W2: FK grade d=0.50 处理不够严谨**

同意。Appendix T (page 15-16) 中 verbosity rewrites 的 FK grade d=0.50 是 Cohen's d 中等效应量。论文将其归因为 "FK's dependence on sentence length, which changes by design in verbosity manipulation"——这个解释有一定道理（FK 公式确实依赖句子长度），但 d=0.50 仍然表明 verbosity rewriting 在某种程度上改变了 readability level，而非仅仅改变 length。如果 readability 变化伴随 verbosity 变化，那么 verbosity 轴上的 Blindspot 发现可能部分反映了 readability 差异而非纯粹的 verbosity 差异。

建议论文至少增加一个控制实验：在保持 FK grade 不变的条件下，是否仍然观察到 verbosity Blindspot。

---

**[AGREE] R1-W3: 仅一个替代 rewriter**

同意。Appendix E (Table 6) 仅用 GPT-4o 作为替代 rewriter，且仅在 formality 轴上测试。22% Style OR 降幅不算小。如果换用更多 rewriters（例如 Llama、Claude）且在 verbosity 轴上也测试，结论的稳健性会更有说服力。

---

**[REBUT] R1-W4: IIA assumption 讨论不充分**

部分不同意。R1 认为 IIA 假设仅在脚注中讨论不够，但我认为在本文的实验设计下 IIA 的威胁有限：

1. **CSD 的 pairwise 比较是 controlled pairs**：每对比较都是原文 vs 同一文本的风格变体（original vs rewrite），而非从大池子中任意抽取的两个文本。在这种 controlled comparison 下，"irrelevant alternatives" 的影响远小于开放式的 ranking/tournament 设计。

2. **BT 模型在此的用途有限**：论文使用 BT 主要是为了计算 win probability 和 aggregated preference direction，而非做精细的 latent utility 估计。BT 的 IIA 假设在这种用途下的违反后果较轻。

3. **但 R1 有一点是对的**：Limitations (page 9) 确实提到 "The Bradley-Terry model assumes unidimensionality—a single latent 'quality' dimension"。如果 judges 沿多个 latent dimensions 评估，BT 的 IIA 假设可能被违反。这值得在正文中简短讨论（例如 2-3 句话），但不需要大篇幅论证。

---

**[AGREE] R1-W5: 100-point Likert 仅用一个 judge**

完全同意，我在 R2-M5 中也提出了这个问题。Appendix O 的 100-point continuous scale 实验仅用 Qwen3-32B，无法排除 judge-specific 效应。至少应在 GPT-4o 上复现。

---

### Minor Issues

**[AGREE] R1-Minor-1: Table 1 排版密度过高**
同意，与我的 R2-W1 一致。

**[AGREE] R1-Minor-2: "style bias" vs "style sensitivity" 措辞不一致**
同意。论文中交替使用 "style bias"（暗示 judges 有偏）和 "style sensitivity"（暗示 judges 能检测风格差异），但这两个概念方向不同。建议统一术语。

**[AGREE] R1-Minor-3: Figure 2 DAG 的 S→Q path caption**
同意，与我的 R2-W2 相关。Figure 2 caption 中对 S→Q path 的描述 ("style may influence perceived quality through channels the NLI gate cannot block") 是正确的但过于简略。建议在 caption 中明确标注哪些 paths 被 NLI gate blocked vs unblocked。

**[AGREE] R1-Minor-4: Appendix 编号难以跟踪**
同意。Appendix A 到 V+，读者需要频繁在正文和附录之间跳转。建议对 Appendix 做分组（如 Methodology appendices, Statistical appendices, Robustness appendices）。

**[REBUT] R1-Minor-5: Section 3.5 Design Rationale 位置偏后**
不同意 R1 认为 Design Rationale 应该提前。Section 3.5 在读者已经了解 CSD 的三个组件（style-controlled rewriting §3.1, content preservation §3.2, measurement protocol §3.3）之后才解释为什么选择这种设计，逻辑顺序是 "what → why"。如果提前到 Section 3.1 之前，读者尚未理解方法细节就要消化设计理由，反而增加认知负担。当前位置是合理的。

---

### 总结

R1 提出的三个 Must-Fix 问题均成立，且与我的审稿发现高度互补：
- R1-N1（因果归因过度）↔ R2-N2（机制解释未区分）：角度不同但指向同一问题
- R1-N2（negative control underpowered）：我未充分展开的重要问题
- R1-N3（GEE n=88 可靠性）↔ R2-N1（轴覆盖窄）：统计精度 + scope 叠加

两位 Reviewer 的 Overall 评分一致（3.5 Borderline Conference），主要分歧在对 IIA 假设讨论（R1-W4）和 Design Rationale 位置（R1-Minor-5）的判断上。

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

_source line 1214 · 2026-05-23T05:36:03.996061+00:00_

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

_source line 1215 · 2026-05-23T05:36:04.548830+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T05:25:13.213729+00:00\", \"completed_at\": \"2026-05-23T05:28:31.660418+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 pipeline 图中节点内文字和边上数字偏小（约正文字号的 60%），建议适当放大或改用 figure* 全宽排版以提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 散点图整体尺寸偏小（仅占单栏宽度约 2/3 高度），legend 和 axis label 字号接近可读性下限；filled vs open diamond 的区分在灰度打印时可能不够清晰，建议辅以 marker shape 差异\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 脚注文字非常小，scaled replication 的说明行（底部注释）在审稿人快速扫读时容易被忽略\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 的 x 轴刻度标签和曲线标注文字偏小（~6pt），crosshair 标注有助理解但周围文字密集；建议增大 axis label 字号或减少标注密度\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 与 Figure 4 同页，视觉密度较高但排布合理，无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Appendix 单页包含 4 个表格（Tables 3–6），部分表格行间距偏紧；Table 5 的 95% CI 列与相邻列间距较窄\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 14 底部脚注（\\\"Effect sizes use style-aligned scoring...\\\"）字号极小，且紧贴 Section O 标题，视觉分隔不够清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"References 末页内容约占 60%，剩余 40% 空白——对 references 尾页而言可接受，不构成问题\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-23T05:36:04.549269+00:00_

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

_source line 1217 · 2026-05-23T05:36:05.955043+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-23T05:36:06.308464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null | head -100",
  "description": "Read first 100 lines of review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null | head -100",
    "description": "Read first 100 lines of review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-23T05:36:06.459738+00:00_

issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
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
    last_seen_round: 14
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
        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
      - round: 11
        reviewers: [1, 2]
        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
      - round: 12
        reviewers: [1, 2]
        note: "R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。"
      - round: 13
        reviewers: [1, 2]
        note: "R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解
…[truncated 1838 chars]

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


### Tool call

_source line 1220 · 2026-05-23T05:36:12.876394+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null | wc -l",
  "description": "Count lines in review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null | wc -l",
    "description": "Count lines in review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-23T05:36:13.019275+00:00_

1570

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 142
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-23T05:36:17.730476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^  - id:|status:\" | paste - - | grep -v \"resolved\" | head -40",
  "description": "Find open/in_progress issues"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^  - id:|status:\" | paste - - | grep -v \"resolved\" | head -40",
    "description": "Find open/in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-23T05:36:17.833520+00:00_

  - id: "R2-N1"	    status: in_progress
        status: done	        status: in_progress
        status: in_progress	  - id: "R1-N2"
    status: in_progress	  - id: "RD2-SF1"
    status: in_progress	  - id: "RD2-SF2"
    status: in_progress	        status: done
        status: in_progress	  - id: "R3-W4"
    status: in_progress	  - id: "R3-M4"
    status: in_progress	  - id: "R4-N2"
    status: in_progress	  - id: "R5-MF2"
    status: in_progress	  - id: "R5-SF1"
    status: in_progress	  - id: "R5-SF2"
    status: in_progress	  - id: "R5-SF3"
    status: in_progress	  - id: "R5-M1"
    status: wont_fix	  - id: "R5-M3"
    status: in_progress	        status: in_progress
  - id: "R5-M4"	    status: in_progress
  - id: "R5-M5"	    status: in_progress
  - id: "R6-SF1"	    status: in_progress
  - id: "R6-SF2"	    status: in_progress
  - id: "R6-SF3"	    status: in_progress
  - id: "R7-W4"	    status: in_progress
  - id: "R7-W5"	    status: in_progress
  - id: "R8-W1"	    status: in_progress
  - id: "R8-W4"	    status: in_progress
  - id: "R8-REF1"	    status: wont_fix
  - id: "R10-N1"	    status: in_progress
  - id: "R10-N2"	    status: in_progress
  - id: "R10-REF1"	    status: in_progress
  - id: "R11-N1"	    status: in_progress
  - id: "R12-N1"	    status: in_progress
  - id: "R12-N2"	    status: in_progress
  - id: "R12-W1"	    status: in_progress
  - id: "R13-SF1"	    status: open
  - id: "R13-M1"	    status: in_progress
  - id: "R13-M2"	    status: open
  - id: "R14-N1"	    status: open
  - id: "R14-M1"	    status: open
  - id: "R14-M2"	    status: open
  - id: "R14-M3"	    status: open

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

_source line 1224 · 2026-05-23T05:36:24.764272+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 20 '\"R14-N1\"' /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null",
  "description": "Read R14-N1 issue details"
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
    "command": "grep -A 20 '\"R14-N1\"' /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null",
    "description": "Read R14-N1 issue details"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-23T05:36:25.216655+00:00_

  - id: "R14-N1"
    summary: "与 RATE 的差异化论证组织分散"
    category: writing
    severity: warning
    status: open
    first_raised_round: 14
    last_seen_round: 14
    resolution: null
    resolution_round: null
    mentions:
      - round: 14
        reviewers: [2]
        note: "R2 Should-Fix W2: RATE 在 Related Work 中分散讨论，核心差异（cross-measurement mode comparison）被三点并列稀释。R1 REBUT（现有内容已基本充分但 organization 可改善）。Director 列为 Minor。"

  - id: "R14-M1"
    summary: "LLM rewriting 未报告 decoding seed / random seed"
    category: format
    severity: info
    status: open
    first_raised_round: 14
    last_seen_round: 14

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-23T05:36:25.418689+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 20 '\"R13-SF1\"' /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null",
  "description": "Read R13-SF1 issue details"
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
    "command": "grep -A 20 '\"R13-SF1\"' /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null",
    "description": "Read R13-SF1 issue details"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-23T05:36:25.469712+00:00_

  - id: "R13-SF1"
    summary: "Table 1 BT 估计包含方向不对称混淆——主文未标注"
    category: experiment
    severity: warning
    status: open
    first_raised_round: 13
    last_seen_round: 13
    resolution: null
    resolution_round: null
    mentions:
      - round: 13
        reviewers: [1, 2]
        note: "R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。R2 AGREE。"
      - round: 14
        reviewers: []
        note: "R14 未显式提及。Table 1 脚注已有方向不对称信息。"

  - id: "R13-M1"
    summary: "Bootstrap CI 方法（percentile vs BCa）未指定"
    category: method
    severity: info

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-23T05:36:41.291756+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
  "description": "Read full review issues YAML",
  "timeout": "10000"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml",
    "description": "Read full review issues YAML",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-23T05:36:41.343171+00:00_

&lt;persisted-output>
Output too large (54.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/e8570bc0-be10-4bc3-ad7e-703a09cb7b7f/tool-results/b1zmdki3e.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
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
    last_seen_round: 14
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
        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
      - round: 11
        reviewers: [1, 2]
        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
      - round: 12
        reviewers: [1, 2]
        note: "R12 fres
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-23T05:36:44.859694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/e8570bc0-be10-4bc3-ad7e-703a09cb7b7f/tool-results/b1zmdki3e.txt",
  "offset": "0",
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
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge--claude-sessions-review-director-acab027e/e8570bc0-be10-4bc3-ad7e-703a09cb7b7f/tool-results/b1zmdki3e.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-23T05:36:45.010730+00:00_

0	issues:
1	  # ============================================================
2	  # Round 1-4 issues (all resolved unless noted)
3	  # ============================================================
4	
5	  - id: "R1-N1"
6	    summary: "标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾"
7	    category: framing
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 5
12	    resolution: "Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'."
13	    resolution_round: 4
14	
15	  - id: "R2-N1"
16	    summary: "Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer"
17	    category: framing
18	    severity: warning
19	    status: in_progress
20	    first_raised_round: 1
21	    last_seen_round: 14
22	    resolution: null
23	    resolution_round: null
24	    mentions:
25	      - round: 3
26	        reviewers: [1, 2]
27	        note: "两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。"
28	      - round: 8
29	        reviewers: [1, 2]
30	        note: "R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。"
31	      - round: 9
32	        reviewers: [1, 2]
33	        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
34	      - round: 10
35	        reviewers: [1, 2]
36	        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
37	      - round: 11
38	        reviewers: [1, 2]
39	        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
40	      - round: 12
41	        reviewers: [1, 2]
42	        note: "R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。"
43	      - roun
…[truncated 4973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-23T05:39:03.112665+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是'真正增量贡献'与 novelty 不足判断矛盾。Director 降为 Should-Fix。持续分歧点。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。两位共识：论文 novelty 重心应从'发现 divergence'转向'quantifying and decomposing per-axis confound structures'。GEE decomposition 是真正增量贡献但被 framing 遮蔽。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。R1-N1 指出 'Blindspot' 因果归因超出证据——Thurstone discriminability 已解释 power 差异，Title 偏向 attenuation 解释。R2-N2 指出三种机制解释未区分限制理论贡献。交叉全部 AGREE。R2 补充：GEE per-axis decomposition 超越 Thurstone，是真正增量贡献但被 framing 遮蔽。这一问题已持续 15 轮未完全解决。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 14\n        action: \"重构 novelty narrative：Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 15\n        action: \"在 Introduction 中给 construct divergence 解释同等篇幅；讨论 Thurstone discriminability 与本文发现的关系；考虑将 'Blindspot' 改为更中性术语或明确定义为操作性描述\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 5-14 issues (selected open/in_progress)\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。R2 AGREE。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Table 1 脚注已有方向不对称信息。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 两位均指出 Table 1 信息密度过高（Must-Fix 级共识），建议拆分 LLMBar primary 和 cross-benchmark replication 两表。\"\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论，核心差异被三点并列稀释。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-R2 列为 Must-Fix N3（需更清晰界定增量贡献）。R1 REBUT——认为 CSD 在方法论层面有结构性差异（pairwise mode, GEE, NLI gating），增量贡献实际已充分展示，但同意 'may underestimate' claim 需更谨慎措辞。分歧点。\"\n\n  # ============================================================\n  # Round 15 新发现\n  # ============================================================\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释，但三种机制未区分\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。核心：'Blindspot' 暗示 Likert 有缺陷，但论文自身承认三种解释（attenuation/amplification/construct divergence）无法区分。R1 补充：Thurstone (1927) 以来已知 pairwise > Likert 判别力，power analysis 完全一致于经典 format sensitivity 差异。R2 补充：如果最终是 construct divergence，则无 'blindspot'——实践含义截然不同。\"\n    action_items:\n      - round: 15\n        action: \"在 Intro 中给 construct divergence 同等篇幅；明确讨论 Thurstone discriminability；将 'Blindspot' 改为操作性描述或更中性术语\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%），无法排除 moderate style bias\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。TOST 仅在 Δ=15pp (BT=65%) 才显著——而 GPT-4o formality BT=63% 已被论文视为显著 style preference。Δ=10pp 时 p=0.156, power≈42%。BT=56.2% 的 6.2pp 偏差在 n=88 下无法排除 moderate effect。Negative control 有效性直接关系到 'Blindspot is judge-specific not format-inherent' 这一核心论点。\"\n    action_items:\n      - round: 15\n        action: \"扩大 negative control n 至 200+，或将结论降级为 'suggestive but underpowered'，不作为排除 format-inherent 解释的主要证据\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽（Style OR CI 跨 6 倍），n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。Qwen3 verb Style OR=13.10 [5.62, 30.55]。n=88→n=355 Qwen3 form Style OR 从 4.20 降到 2.15（缩水 49%），其他 judge 可能也被高估。交互效应检验 power 极低（OR 0.45-2.60 全 p>0.13），non-significant interaction ≠ additive model 正确。GEE 是区分 style-dominated vs quality-confounded 的唯一工具，如果在 n=88 下不可靠，per-judge regime classification 的可信度存疑。\"\n    action_items:\n      - round: 15\n        action: \"至少在 verbosity 轴做 n=355 级别 scaled replication；讨论 OR 缩水含义；报告 GEE minimum detectable OR\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴（formality, verbosity）无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出，交叉全部 AGREE。Register 仅为 exploratory pilot 且有 evaluator-producer overlap。Semantic-level axes (hedging, humor) 被 NLI gate 系统性拒绝。两个高度相关的表层轴不足以声称 systematic phenomenon。R1 补充：formality 和 verbosity 间有结构性相关（FK grade d=0.50 cross-axis 泄漏）。\"\n    action_items:\n      - round: 15\n        action: \"弱化通用性 claim：Abstract/Intro 中明确限定为 'surface-level style axes'；或增加 1-2 个轴的 pilot evidence\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉 AGREE 并补充：A2 下界 65.3% 意味着 worst case 下约 1/3 gate-passed pairs 可能含内容变化。GPT-4o cross-validation (92.1%/82.6%) 是 LLM 验证非独立人工验证。建议至少 100 pairs 并覆盖所有 axis。\"\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W5 + R2-M5 双方独立提出。至少应在 GPT-4o 上 replicate，排除 judge-specific 效应。\"\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。Verbosity rewrites 导致 FK grade d=0.50（medium effect），论文归因为 FK 依赖句子长度但未正式验证。建议 length-controlled FK 分析。\"\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。建议至少增加一个额外 rewriter 或讨论 22% 降幅的上界含义。\"\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1-Minor-1 双方独立提出。建议拆分为 LLMBar primary 和 cross-benchmark replication 两表。\"\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-M1 提出，R1 交叉 AGREE。Section 3.1 仅给出 paraphrase-level 示例。\"\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-Minor-2 提出，R2 交叉 AGREE。两术语含义不同（bias=方向性, sensitivity=双向响应性），建议统一。\"\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [2]\n        note: \"R2-M2 提出，R1 交叉 AGREE。建议在 caption 或正文中展开为 'Originality OR (original-preference odds ratio)'。\"\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [2]\n        note: \"R2-M4 提出，R1 交叉 AGREE。\"\n"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-4 issues (all resolved unless noted)\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"标题 'Causal Style Decomposition' 与 §3.5 因果声明 disclaimer 实质性矛盾\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Title changed to 'Likert Blindspot'. §3.5 renamed 'Design Rationale'.\"\n    resolution_round: 4\n\n  - id: \"R2-N1\"\n    summary: \"Novelty 不足——Likert Blindspot 是心理测量学已知现象的 domain transfer\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立确认 novelty 主要来自 domain transfer（Thurstone 1927 已知）。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"R8-R2 列为 Must-Fix。共识：将 'the first' 改为 'a unified framework'。\"\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。\"\n      - round: 11\n        reviewers: [1, 2]\n        note: \"R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是'真正增量贡献'与 novelty 不足判断矛盾。Director 降为 Should-Fix。持续分歧点。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review: R2 Must-Fix N3，R1 交叉 AGREE。两位共识：论文 novelty 重心应从'发现 divergence'转向'quantifying and decomposing per-axis confound structures'。GEE decomposition 是真正增量贡献但被 framing 遮蔽。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 fresh review: 两位再次独立提出。R1-N1 指出 'Blindspot' 因果归因超出证据——Thurstone discriminability 已解释 power 差异，Title 偏向 attenuation 解释。R2-N2 指出三种机制解释未区分限制理论贡献。交叉全部 AGREE。R2 补充：GEE per-axis decomposition 超越 Thurstone，是真正增量贡献但被 framing 遮蔽。这一问题已持续 15 轮未完全解决。\"\n    action_items:\n      - round: 7\n        action: \"将 Abstract/Intro 中 'the first framework' 改为 'a unified framework'\"\n        assigned_to: paper_agent\n        status: done\n      - round: 10\n        action: \"三处 'reveals' → 'demonstrates'/'identifies' + RW 'first' 限定为 'this per-axis sensitivity gap'\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 14\n        action: \"重构 novelty narrative：Abstract/标题突出 GEE decomposition 方法论贡献，将 divergence 发现降为 motivating observation\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 15\n        action: \"在 Introduction 中给 construct divergence 解释同等篇幅；讨论 Thurstone discriminability 与本文发现的关系；考虑将 'Blindspot' 改为更中性术语或明确定义为操作性描述\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R1-N2\"\n    summary: \"NLI gate 67% false-negative rate 造成选择偏差未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§nli_validation: FNR 8.4%, precision 98.9%, AC1=0.89\"\n    resolution_round: 1\n\n  - id: \"R1-N3\"\n    summary: \"NLI 阈值 0.90 无 justification\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"Threshold on plateau, robust 0.70-0.95. §5.1 sensitivity analysis added.\"\n    resolution_round: 1\n\n  - id: \"R2-N2\"\n    summary: \"RATE 批评缺乏 matched replication\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"§likert_pairwise h2h on same data\"\n    resolution_round: 1\n\n  - id: \"R2-N3\"\n    summary: \"引用系统严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"22 verified refs, 0 broken\"\n    resolution_round: 1\n\n  - id: \"R1-W1\"\n    summary: \"Likert baseline 可能不公平——未使用 ordinal regression\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Table 2: all 7 Likert methods fail\"\n    resolution_round: 1\n\n  - id: \"R1-W2\"\n    summary: \"Consistency filtering data loss\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT on all data LOWER than filtered\"\n    resolution_round: 1\n\n  - id: \"R1-W3\"\n    summary: \"Original preference confound\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-cell GEE decomposition\"\n    resolution_round: 1\n\n  - id: \"R1-W4\"\n    summary: \"Multiple comparison correction 不一致\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    resolution: \"§stat_framework defines trichotomy\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Post-hoc power analysis\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Power curve is illustrative\"\n    resolution_round: 1\n\n  - id: \"R2-W1\"\n    summary: \"范围过窄——仅 formality 有完整结果\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Complete 2x3 matrix + cross-benchmark\"\n    resolution_round: 1\n\n  - id: \"R2-W2\"\n    summary: \"缺少 Bradley-Terry\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"BT with pair-level bootstrap\"\n    resolution_round: 1\n\n  - id: \"R2-W3\"\n    summary: \"Related work 不完整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Comprehensive coverage\"\n    resolution_round: 1\n\n  - id: \"R2-W4\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"3 figures + forest plot\"\n    resolution_round: 1\n\n  - id: \"CROSS-1\"\n    summary: \"Blindspot 实为 efficiency gap\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"论文已重新定位为 diagnostic methodology\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 5-14 issues (selected open/in_progress)\n  # ============================================================\n\n  - id: \"R13-SF1\"\n    summary: \"Table 1 BT 估计包含方向不对称混淆——主文未标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix (W3): formality 方向不对称使 Table 1 的聚合 BT 混合了风格偏好与原文质量混淆。R2 AGREE。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未显式提及。Table 1 脚注已有方向不对称信息。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15 两位均指出 Table 1 信息密度过高（Must-Fix 级共识），建议拆分 LLMBar primary 和 cross-benchmark replication 两表。\"\n\n  - id: \"R14-N1\"\n    summary: \"与 RATE 的差异化论证组织分散\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 14\n        reviewers: [2]\n        note: \"R2 Should-Fix W2: RATE 在 Related Work 中分散讨论，核心差异被三点并列稀释。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-R2 列为 Must-Fix N3（需更清晰界定增量贡献）。R1 REBUT——认为 CSD 在方法论层面有结构性差异（pairwise mode, GEE, NLI gating），增量贡献实际已充分展示，但同意 'may underestimate' claim 需更谨慎措辞。分歧点。\"\n\n  # ============================================================\n  # Round 15 新发现\n  # ============================================================\n\n  - id: \"R15-N1\"\n    summary: \"'Blindspot' 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释，但三种机制未区分\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 + R2-N2 双方独立提出，交叉全部 AGREE。核心：'Blindspot' 暗示 Likert 有缺陷，但论文自身承认三种解释（attenuation/amplification/construct divergence）无法区分。R1 补充：Thurstone (1927) 以来已知 pairwise > Likert 判别力，power analysis 完全一致于经典 format sensitivity 差异。R2 补充：如果最终是 construct divergence，则无 'blindspot'——实践含义截然不同。\"\n    action_items:\n      - round: 15\n        action: \"在 Intro 中给 construct divergence 同等篇幅；明确讨论 Thurstone discriminability；将 'Blindspot' 改为操作性描述或更中性术语\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N2\"\n    summary: \"Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力不足（power≈42%），无法排除 moderate style bias\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 提出，R2 交叉 AGREE 并升级为关键问题。TOST 仅在 Δ=15pp (BT=65%) 才显著——而 GPT-4o formality BT=63% 已被论文视为显著 style preference。Δ=10pp 时 p=0.156, power≈42%。BT=56.2% 的 6.2pp 偏差在 n=88 下无法排除 moderate effect。Negative control 有效性直接关系到 'Blindspot is judge-specific not format-inherent' 这一核心论点。\"\n    action_items:\n      - round: 15\n        action: \"扩大 negative control n 至 200+，或将结论降级为 'suggestive but underpowered'，不作为排除 format-inherent 解释的主要证据\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-N3\"\n    summary: \"GEE decomposition 在 n=88 下 CI 极宽（Style OR CI 跨 6 倍），n=88→n=355 时 OR 缩水 49%\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N3 提出，R2 交叉 AGREE。Qwen3 verb Style OR=13.10 [5.62, 30.55]。n=88→n=355 Qwen3 form Style OR 从 4.20 降到 2.15（缩水 49%），其他 judge 可能也被高估。交互效应检验 power 极低（OR 0.45-2.60 全 p>0.13），non-significant interaction ≠ additive model 正确。GEE 是区分 style-dominated vs quality-confounded 的唯一工具，如果在 n=88 下不可靠，per-judge regime classification 的可信度存疑。\"\n    action_items:\n      - round: 15\n        action: \"至少在 verbosity 轴做 n=355 级别 scaled replication；讨论 OR 缩水含义；报告 GEE minimum detectable OR\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W1\"\n    summary: \"仅 2 个表层风格轴（formality, verbosity）无法支撑 'systematic pattern' 的通用性 claim\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 + R1-W1 双方独立提出，交叉全部 AGREE。Register 仅为 exploratory pilot 且有 evaluator-producer overlap。Semantic-level axes (hedging, humor) 被 NLI gate 系统性拒绝。两个高度相关的表层轴不足以声称 systematic phenomenon。R1 补充：formality 和 verbosity 间有结构性相关（FK grade d=0.50 cross-axis 泄漏）。\"\n    action_items:\n      - round: 15\n        action: \"弱化通用性 claim：Abstract/Intro 中明确限定为 'surface-level style axes'；或增加 1-2 个轴的 pilot evidence\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: \"R15-W2\"\n    summary: \"Human annotation 验证规模偏小（50 pairs, κ=0.44），A2 pass precision 下界仅 65.3%\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W4 提出，R1 交叉 AGREE 并补充：A2 下界 65.3% 意味着 worst case 下约 1/3 gate-passed pairs 可能含内容变化。GPT-4o cross-validation (92.1%/82.6%) 是 LLM 验证非独立人工验证。建议至少 100 pairs 并覆盖所有 axis。\"\n\n  - id: \"R15-W3\"\n    summary: \"100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W5 + R2-M5 双方独立提出。至少应在 GPT-4o 上 replicate，排除 judge-specific 效应。\"\n\n  - id: \"R15-W4\"\n    summary: \"FK grade d=0.50 cross-axis contamination 处理不够严谨\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W2 提出，R2 交叉 AGREE。Verbosity rewrites 导致 FK grade d=0.50（medium effect），论文归因为 FK 依赖句子长度但未正式验证。建议 length-controlled FK 分析。\"\n\n  - id: \"R15-W5\"\n    summary: \"Evaluator-producer overlap mitigation 仅测试一个替代 rewriter（GPT-4o），22% OR 降幅不小\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W3 提出，R2 交叉 AGREE。建议至少增加一个额外 rewriter 或讨论 22% 降幅的上界含义。\"\n\n  - id: \"R15-W6\"\n    summary: \"Table 1 信息密度过高——15 行 + 6 行脚注挤在一个表\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    resolution: null\n    resolution_round: null\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1-Minor-1 双方独立提出。建议拆分为 LLMBar primary 和 cross-benchmark replication 两表。\"\n\n  - id: \"R15-M1\"\n    summary: \"Rewriting prompt 完整文本未在 Appendix 中给出\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-M1 提出，R1 交叉 AGREE。Section 3.1 仅给出 paraphrase-level 示例。\"\n\n  - id: \"R15-M2\"\n    summary: \"'style bias' vs 'style sensitivity' 措辞不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-Minor-2 提出，R2 交叉 AGREE。两术语含义不同（bias=方向性, sensitivity=双向响应性），建议统一。\"\n\n  - id: \"R15-M3\"\n    summary: \"Table 2 'Orig OR' 缩写首次出现时未解释\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [2]\n        note: \"R2-M2 提出，R1 交叉 AGREE。建议在 caption 或正文中展开为 'Originality OR (original-preference odds ratio)'。\"\n\n  - id: \"R15-M4\"\n    summary: \"References 格式——部分 arXiv preprint 与正式发表版本混用\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [2]\n        note: \"R2-M4 提出，R1 交叉 AGREE。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-23T05:39:03.163594+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml\", \"bytes\": 15031}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-23T05:41:26.972944+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 15 审稿报告 — The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n\n**目标 venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验设计 + 统计方法；R2: 新颖性 + 完整性 + 写作质量 + 格式合规）\n**审稿模式**: Fresh（无上轮记忆）\n**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题收敛，无需第二轮）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，一种 black-box 诊断方法，用于检测 LLM judge 在 Likert 和 pairwise 两种评分模式下对 style 的敏感度差异（称为 \"Likert Blindspot\"）。方法包含三个组件：NLI-gated content control、per-axis style decomposition、position-controlled pairwise comparison。在 4 个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个 negative control（Claude Sonnet 4）、3 个 benchmarks（LLMBar, AlpacaEval, MT-Bench）、2 个 primary style axes（formality, verbosity）上，pairwise 检测到显著 style preference（BT 63-77%, p<0.001）而 Likert 未达显著（p>0.17）。GEE conditional decomposition 进一步揭示 per-axis confound structure：verbosity 为 style-dominated（Style OR 8-13），formality 为 conditional effect（Style OR 2-5, Orig OR 2-5）。\n\n---\n\n## Strengths\n\n1. **统计处理深度罕见**：7 种统计方法互相验证（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Mann-Whitney），bootstrap CI 10,000 次 pair-level resamples，power analysis，bootstrap attenuation analysis，NLI threshold sweep——在 NLP 方法论论文中树立了高标准。[AGREE R1+R2]\n\n2. **GEE conditional decomposition 有独立方法论贡献**：将 BT 整体偏好分解为 style 和 originality 两个分量，揭示 verbosity（style-dominated）和 formality（conditionally style-driven）的结构性差异。即使 n=88 的 CI 较宽，分析框架本身有独立价值。[AGREE R1+R2]\n\n3. **Confounder control 策略周全**：NLI gate + position swap + same-style double-rewrite control + direction-aware gating for verbosity + 6 controls for amplification risk（直接回应 Comparative Trap, Jeong et al. 2025）。每层均有对应 validation。[AGREE R1+R2]\n\n4. **Bootstrap attenuation analysis 巧妙**：d 收敛到 0 而非保持 non-zero，区分了 power limitation 和 measurement attenuation——是 Likert signal genuinely absent 的强证据。[AGREE R1+R2]\n\n5. **Limitations 诚实全面**：四段覆盖 quality-style confounding、evaluator-producer bias、scope boundary、validation methodology，主动承认三种机制解释无法区分。[AGREE R1+R2]\n\n6. **格式合规**：8 页正文，ACL 模板正确使用（`\\usepackage[review]{acl}`），double-blind 匿名性无泄露，Limitations section 位置正确。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 共识] **\"Blindspot\" 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释，但三种机制未区分**\n\n论文命名 \"Likert Blindspot\" 暗示 Likert 有缺陷（盲区），但 Section 5.1 自身列出三种 non-exclusive 解释（attenuation / amplification / construct divergence）且承认无法区分。若最终是 construct divergence，则两种模式测量不同构念，不存在 \"盲区\"——实践含义截然不同。更关键的是，pairwise > Likert 的判别力是 Thurstone (1927) 以来的已知现象；power analysis 显示 Likert 需 4-206× 样本量，完全一致于经典 format sensitivity 差异。论文需论证观察到的 divergence 为何不仅仅是已知的 format sensitivity 差异在 LLM judge 场景下的复现。\n\nR2 补充：GEE per-axis decomposition 超越了 Thurstone 框架，是真正的增量贡献，但被 \"Blindspot\" framing 遮蔽。\n\n**建议**：(1) 在 Introduction 中给 construct divergence 同等篇幅；(2) 明确讨论 Thurstone discriminability 与本文发现的关系；(3) 将 \"Blindspot\" 改为更中性术语或明确定义为操作性描述而非因果性声明。\n\n> ⚠️ 此问题自 Round 1 以来已持续 15 轮。历经多次 framing 修改（'the first' → 'a unified framework'、'reveals' → 'demonstrates'/'identifies'），但标题中的 \"Blindspot\" 持续被两位 Reviewer 质疑。\n\n---\n\n**MF2** [critical, 共识] **Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力严重不足（power≈42%）**\n\nClaude Sonnet 4 作为 negative control 是实验设计的关键支柱——用于证明 Blindspot 是 judge-specific 而非 format-inherent。但 TOST 在 Δ=15pp (BT=65%) 才显著（p=0.010），而 GPT-4o formality BT=63% 已被论文视为显著 style preference——即等效界限几乎涵盖了论文自己认定为显著的效应量。Δ=10pp 时 TOST 不显著（p=0.156, power≈42%）。BT=56.2% 的 6.2pp 偏差在 n=88 下无法排除 moderate effect。\n\n**建议**：(1) 扩大 negative control n 至 200+，使 Δ=10pp 的 TOST 达到合理 power；(2) 或将 negative control 结论降级为 \"suggestive but underpowered\"；(3) 增加第二个 negative control judge。\n\n---\n\n**MF3** [critical, 共识] **GEE decomposition 在 n=88 下 CI 极宽，regime classification 可靠性存疑**\n\nQwen3 verbosity Style OR=13.10 [5.62, 30.55]，95% CI 跨越近 6 倍。n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%），提示其他 judge 的 OR 也可能被高估。交互效应检验 power 极低（OR 0.45-2.60 全 p>0.13），non-significant interaction 不等于 additive model 正确。GEE 是区分 style-dominated vs quality-confounded 的唯一工具；如果在 n=88 下估计不可靠，per-judge regime classification 的可信度受损。\n\n**建议**：(1) 至少在 verbosity 轴做 n=355 级别 scaled replication；(2) 讨论 OR 缩水 49% 的含义；(3) 报告 GEE minimum detectable OR 或 power analysis。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 共识] **仅 2 个表层风格轴无法支撑 \"systematic pattern\" 的通用性 claim**\nFormality + verbosity 均属 surface-level stylistic attributes，register 为 exploratory pilot 且有 evaluator-producer overlap。Semantic-level axes 被 NLI gate 系统性拒绝。两个轴间存在结构性相关（FK grade d=0.50 cross-axis 泄漏）。Abstract/Title 的通用性措辞超出实验覆盖范围。\n**建议**：明确限定为 \"surface-level style axes\"，或增加 1-2 个轴的 pilot evidence。\n\n**SF2** [warning, 共识] **Human annotation 验证规模偏小（50 pairs, κ=0.44）**\nA2 pass precision 下界仅 65.3%，worst case 下约 1/3 gate-passed pairs 可能含内容变化。GPT-4o cross-validation 是 LLM 验证非独立人工验证。\n**建议**：扩大至 100+ pairs，覆盖所有 axis。\n\n**SF3** [warning, 共识] **100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试**\n无法排除 judge-specific 效应。\n**建议**：至少在 GPT-4o 上 replicate。\n\n**SF4** [warning, 共识] **FK grade d=0.50 cross-axis contamination 处理不够严谨**\n论文归因为 FK 依赖句子长度但未正式验证。\n**建议**：做 length-controlled FK 分析。\n\n**SF5** [warning, 共识] **Evaluator-producer overlap mitigation 仅测试一个替代 rewriter**\nGPT-4o 替代 rewriter 显示 22% Style OR 降幅，仅此一个配置不足以确认趋势稳定。\n**建议**：增加至少一个额外 rewriter。\n\n**SF6** [warning, 共识] **Table 1 信息密度过高**\n15 行结果 + 6 行脚注挤在一个表中，读者认知负担大。\n**建议**：拆分为 LLMBar primary 和 cross-benchmark replication 两表。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享中达成 [AGREE]：\n\n1. \"Blindspot\" 因果归因超出证据（R1-N1 ↔ R2-N2）：**强共识**\n2. Style axis 覆盖窄限制通用性 claim（R1-W1 ↔ R2-N1）：**强共识**\n3. Negative control TOST underpowered（R1-N2，R2 升级）：**强共识**\n4. GEE n=88 可靠性（R1-N3，R2 AGREE）：**强共识**\n5. Table 1 密度（R1-M1 ↔ R2-W1）：共识\n6. 100-point Likert 单 judge（R1-W5 ↔ R2-M5）：共识\n7. Human annotation 规模（R2-W4，R1 AGREE 并补充）：共识\n8. FK grade cross-axis（R1-W2，R2 AGREE）：共识\n9. Rewriter independence 单配置（R1-W3，R2 AGREE）：共识\n\n## Reviewer Divergence\n\n1. **RATE 增量贡献**（R2 Must-Fix vs R1 REBUT）：R2 认为与 RATE 的区分不够清晰，R1 认为 CSD 在方法论层面有结构性差异（pairwise mode, GEE, NLI gating），增量贡献已充分展示。**Director 判断**：R1 的 REBUT 论证更有说服力——CSD 与 RATE 的差异是结构性的而非增量性的（RATE 从设计上无法检测 mode divergence），但同意 \"may underestimate\" claim 需更谨慎措辞。降为 SF 级。\n\n2. **IIA assumption 讨论**（R1 Should-Fix vs R2 REBUT）：R1 认为 IIA 讨论不充分，R2 认为在 controlled pairs 设计下 IIA 威胁有限。**Director 判断**：R2 的 REBUT 合理——CSD 的 pairwise 比较是 controlled pairs 而非 open tournament，IIA 威胁确实有限。建议在正文（而非脚注）简短讨论即可。降为 Minor。\n\n3. **Design Rationale 位置**（R1 move earlier vs R2 current OK）：Minor 分歧，不影响评分。\n\n---\n\n## Questions\n\n1. 是否考虑过用 human raters 收集少量 ground-truth style bias ratings（如 50-100 pairs），以部分区分 attenuation vs amplification？\n2. 如果将 \"Blindspot\" 重新定义为 \"Likert-Pairwise Divergence\" 或类似中性术语，是否会改变论文的叙事结构？\n3. n=88→n=355 时 Qwen3 Style OR 缩水 49% 的原因是什么？是否其他 judge 也预期有类似缩水？\n4. Claude Sonnet 4 的 BT=56.2% 是否反映了一个真实但较弱的 formality preference？如果是，negative control 的叙事需要如何调整？\n\n---\n\n## Missing References\n\n两位 Reviewer 未指出重大遗漏。Related Work 覆盖较为全面（Thurstone 1927, Stevens 1946, RATE, Comparative Trap, CASSE, FairJudge 等均已引用）。R2-M4 指出部分引用格式不一致（arXiv preprint 与正式发表版本混用），建议统一检查。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（8 项 info，0 critical，0 warning）。主要发现：\n- Page 2: Figure 1 pipeline 图节点内文字偏小（约正文字号 60%），建议放大或改用 figure* 全宽\n- Page 5: Figure 3 散点图尺寸偏小，filled vs open diamond 灰度打印区分度不足\n- Page 6: Table 1 脚注字号很小，scaled replication 说明易被忽略\n- Page 7: Figure 4 x 轴刻度标签偏小（~6pt）；Table 2 与 Figure 4 同页但排布合理\n- Page 11: 单页 4 个表格，行间距偏紧\n- Page 14: Table 14 脚注字号极小\n- Page 19: References 末页 40% 空白（可接受）\n\n无阻塞性排版问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference**（两位 Reviewer 独立一致）\n\n**置信度：4 / 5**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**总体判断**：这是一篇方法论扎实、统计处理深度罕见的诊断性工作。CSD 方法论（NLI gating + position-controlled pairwise + GEE decomposition）的设计严谨，robustness checks 全面，切中 RLHF/DPO 依赖 pairwise 而 evaluation 依赖 Likert 的实践痛点。\n\n但三个核心弱点限制了贡献：(1) \"Blindspot\" 的因果归因超出实验证据（三种机制未区分，且 pairwise > Likert 判别力是 Thurstone 1927 已知现象）；(2) negative control 的 TOST 统计力不足，无法排除 Claude 有 moderate style bias，削弱了 \"judge-specific not format-inherent\" 的论点；(3) GEE decomposition 在 n=88 下精度不足（CI 跨 6 倍，OR 缩水 49%），per-judge regime classification 的可靠性存疑。此外，仅 2 个表层风格轴限制了通用性 claim。\n\n**对 EMNLP 2026 的接收建议**：当前版本处于 Borderline Conference / strong Findings 水平。如果作者能解决 MF1（framing 中性化）和 MF2（negative control 扩样本或降级声明），论文有望达到 Conference 水平。MF3（GEE scaled replication）如果无法在 deadline 前完成，至少应在正文中讨论 OR 缩水现象和 CI 宽度对结论的影响。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Opening example（GPT-4o 对 formal vs casual 答案的评分反转）生动有效，但未在 Limitations 中讨论这是否是 cherry-picked\n- \"systematically divergent style sensitivity\"（Abstract line 1）建议改为 \"systematically divergent style sensitivity on surface-level axes\"\n- Contributions list 中 \"GEE conditional decomposition reveals qualitatively distinct per-axis confound structures\" 应提升为第一贡献（R2-N1 共识：GEE 是真正增量贡献）\n\n### Section 2 (Related Work)\n- Thurstone (1927) 被引用但未讨论其与 power analysis（Figure 4）的关系——如果 4-206× 样本量差异可用经典 discriminability 差异解释，需明确论证 LLM judge 场景下的新发现是什么\n- RATE head-to-head 比较（Section 5.1）虽然结构性论证充分，但 \"RATE's own style-related findings may underestimate\" 是推测而非验证过的结论，需更谨慎措辞\n\n### Section 3 (Method)\n- Section 3.1: Rewriting prompt 完整文本应在 Appendix 中给出（R1+R2 共识）\n- Section 3.5 Design Rationale 位置合理（R2 REBUT R1 合理）\n\n### Section 4 (Experiments)\n- Table 1: 建议拆分为 primary + cross-benchmark 两表（R1+R2 共识）\n- Table 2: \"Orig OR\" 首次出现时应展开解释\n- IIA 讨论应从脚注移至正文，简短讨论即可（2-3 句）\n\n### Section 5 (Analysis)\n- Section 5.1: 给 construct divergence 解释同等篇幅\n- Section 5.2 (GEE): 讨论 n=88→n=355 OR 缩水现象\n- \"style bias\" vs \"style sensitivity\" 术语应统一\n\n### Limitations\n- 诚实全面，但第四段 100-point scale 实验的单 judge 限制应标注\n- 考虑增加对 human ground-truth validation 作为 future work 的更 prominent 讨论\n\n### Format\n- 正文 8 页，合规\n- ACL 模板正确，double-blind 无泄露\n- References: 部分 arXiv preprint 与正式发表版本混用，建议统一\n",
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
    "report": "# Round 15 审稿报告 — The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n\n**目标 venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验设计 + 统计方法；R2: 新颖性 + 完整性 + 写作质量 + 格式合规）\n**审稿模式**: Fresh（无上轮记忆）\n**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题收敛，无需第二轮）\n\n---\n\n## Summary\n\n论文提出 Controlled Style Decomposition (CSD)，一种 black-box 诊断方法，用于检测 LLM judge 在 Likert 和 pairwise 两种评分模式下对 style 的敏感度差异（称为 \"Likert Blindspot\"）。方法包含三个组件：NLI-gated content control、per-axis style decomposition、position-controlled pairwise comparison。在 4 个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个 negative control（Claude Sonnet 4）、3 个 benchmarks（LLMBar, AlpacaEval, MT-Bench）、2 个 primary style axes（formality, verbosity）上，pairwise 检测到显著 style preference（BT 63-77%, p<0.001）而 Likert 未达显著（p>0.17）。GEE conditional decomposition 进一步揭示 per-axis confound structure：verbosity 为 style-dominated（Style OR 8-13），formality 为 conditional effect（Style OR 2-5, Orig OR 2-5）。\n\n---\n\n## Strengths\n\n1. **统计处理深度罕见**：7 种统计方法互相验证（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Mann-Whitney），bootstrap CI 10,000 次 pair-level resamples，power analysis，bootstrap attenuation analysis，NLI threshold sweep——在 NLP 方法论论文中树立了高标准。[AGREE R1+R2]\n\n2. **GEE conditional decomposition 有独立方法论贡献**：将 BT 整体偏好分解为 style 和 originality 两个分量，揭示 verbosity（style-dominated）和 formality（conditionally style-driven）的结构性差异。即使 n=88 的 CI 较宽，分析框架本身有独立价值。[AGREE R1+R2]\n\n3. **Confounder control 策略周全**：NLI gate + position swap + same-style double-rewrite control + direction-aware gating for verbosity + 6 controls for amplification risk（直接回应 Comparative Trap, Jeong et al. 2025）。每层均有对应 validation。[AGREE R1+R2]\n\n4. **Bootstrap attenuation analysis 巧妙**：d 收敛到 0 而非保持 non-zero，区分了 power limitation 和 measurement attenuation——是 Likert signal genuinely absent 的强证据。[AGREE R1+R2]\n\n5. **Limitations 诚实全面**：四段覆盖 quality-style confounding、evaluator-producer bias、scope boundary、validation methodology，主动承认三种机制解释无法区分。[AGREE R1+R2]\n\n6. **格式合规**：8 页正文，ACL 模板正确使用（`\\usepackage[review]{acl}`），double-blind 匿名性无泄露，Limitations section 位置正确。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 共识] **\"Blindspot\" 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释，但三种机制未区分**\n\n论文命名 \"Likert Blindspot\" 暗示 Likert 有缺陷（盲区），但 Section 5.1 自身列出三种 non-exclusive 解释（attenuation / amplification / construct divergence）且承认无法区分。若最终是 construct divergence，则两种模式测量不同构念，不存在 \"盲区\"——实践含义截然不同。更关键的是，pairwise > Likert 的判别力是 Thurstone (1927) 以来的已知现象；power analysis 显示 Likert 需 4-206× 样本量，完全一致于经典 format sensitivity 差异。论文需论证观察到的 divergence 为何不仅仅是已知的 format sensitivity 差异在 LLM judge 场景下的复现。\n\nR2 补充：GEE per-axis decomposition 超越了 Thurstone 框架，是真正的增量贡献，但被 \"Blindspot\" framing 遮蔽。\n\n**建议**：(1) 在 Introduction 中给 construct divergence 同等篇幅；(2) 明确讨论 Thurstone discriminability 与本文发现的关系；(3) 将 \"Blindspot\" 改为更中性术语或明确定义为操作性描述而非因果性声明。\n\n> ⚠️ 此问题自 Round 1 以来已持续 15 轮。历经多次 framing 修改（'the first' → 'a unified framework'、'reveals' → 'demonstrates'/'identifies'），但标题中的 \"Blindspot\" 持续被两位 Reviewer 质疑。\n\n---\n\n**MF2** [critical, 共识] **Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力严重不足（power≈42%）**\n\nClaude Sonnet 4 作为 negative control 是实验设计的关键支柱——用于证明 Blindspot 是 judge-specific 而非 format-inherent。但 TOST 在 Δ=15pp (BT=65%) 才显著（p=0.010），而 GPT-4o formality BT=63% 已被论文视为显著 style preference——即等效界限几乎涵盖了论文自己认定为显著的效应量。Δ=10pp 时 TOST 不显著（p=0.156, power≈42%）。BT=56.2% 的 6.2pp 偏差在 n=88 下无法排除 moderate effect。\n\n**建议**：(1) 扩大 negative control n 至 200+，使 Δ=10pp 的 TOST 达到合理 power；(2) 或将 negative control 结论降级为 \"suggestive but underpowered\"；(3) 增加第二个 negative control judge。\n\n---\n\n**MF3** [critical, 共识] **GEE decomposition 在 n=88 下 CI 极宽，regime classification 可靠性存疑**\n\nQwen3 verbosity Style OR=13.10 [5.62, 30.55]，95% CI 跨越近 6 倍。n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%），提示其他 judge 的 OR 也可能被高估。交互效应检验 power 极低（OR 0.45-2.60 全 p>0.13），non-significant interaction 不等于 additive model 正确。GEE 是区分 style-dominated vs quality-confounded 的唯一工具；如果在 n=88 下估计不可靠，per-judge regime classification 的可信度受损。\n\n**建议**：(1) 至少在 verbosity 轴做 n=355 级别 scaled replication；(2) 讨论 OR 缩水 49% 的含义；(3) 报告 GEE minimum detectable OR 或 power analysis。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 共识] **仅 2 个表层风格轴无法支撑 \"systematic pattern\" 的通用性 claim**\nFormality + verbosity 均属 surface-level stylistic attributes，register 为 exploratory pilot 且有 evaluator-producer overlap。Semantic-level axes 被 NLI gate 系统性拒绝。两个轴间存在结构性相关（FK grade d=0.50 cross-axis 泄漏）。Abstract/Title 的通用性措辞超出实验覆盖范围。\n**建议**：明确限定为 \"surface-level style axes\"，或增加 1-2 个轴的 pilot evidence。\n\n**SF2** [warning, 共识] **Human annotation 验证规模偏小（50 pairs, κ=0.44）**\nA2 pass precision 下界仅 65.3%，worst case 下约 1/3 gate-passed pairs 可能含内容变化。GPT-4o cross-validation 是 LLM 验证非独立人工验证。\n**建议**：扩大至 100+ pairs，覆盖所有 axis。\n\n**SF3** [warning, 共识] **100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试**\n无法排除 judge-specific 效应。\n**建议**：至少在 GPT-4o 上 replicate。\n\n**SF4** [warning, 共识] **FK grade d=0.50 cross-axis contamination 处理不够严谨**\n论文归因为 FK 依赖句子长度但未正式验证。\n**建议**：做 length-controlled FK 分析。\n\n**SF5** [warning, 共识] **Evaluator-producer overlap mitigation 仅测试一个替代 rewriter**\nGPT-4o 替代 rewriter 显示 22% Style OR 降幅，仅此一个配置不足以确认趋势稳定。\n**建议**：增加至少一个额外 rewriter。\n\n**SF6** [warning, 共识] **Table 1 信息密度过高**\n15 行结果 + 6 行脚注挤在一个表中，读者认知负担大。\n**建议**：拆分为 LLMBar primary 和 cross-benchmark replication 两表。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享中达成 [AGREE]：\n\n1. \"Blindspot\" 因果归因超出证据（R1-N1 ↔ R2-N2）：**强共识**\n2. Style axis 覆盖窄限制通用性 claim（R1-W1 ↔ R2-N1）：**强共识**\n3. Negative control TOST underpowered（R1-N2，R2 升级）：**强共识**\n4. GEE n=88 可靠性（R1-N3，R2 AGREE）：**强共识**\n5. Table 1 密度（R1-M1 ↔ R2-W1）：共识\n6. 100-point Likert 单 judge（R1-W5 ↔ R2-M5）：共识\n7. Human annotation 规模（R2-W4，R1 AGREE 并补充）：共识\n8. FK grade cross-axis（R1-W2，R2 AGREE）：共识\n9. Rewriter independence 单配置（R1-W3，R2 AGREE）：共识\n\n## Reviewer Divergence\n\n1. **RATE 增量贡献**（R2 Must-Fix vs R1 REBUT）：R2 认为与 RATE 的区分不够清晰，R1 认为 CSD 在方法论层面有结构性差异（pairwise mode, GEE, NLI gating），增量贡献已充分展示。**Director 判断**：R1 的 REBUT 论证更有说服力——CSD 与 RATE 的差异是结构性的而非增量性的（RATE 从设计上无法检测 mode divergence），但同意 \"may underestimate\" claim 需更谨慎措辞。降为 SF 级。\n\n2. **IIA assumption 讨论**（R1 Should-Fix vs R2 REBUT）：R1 认为 IIA 讨论不充分，R2 认为在 controlled pairs 设计下 IIA 威胁有限。**Director 判断**：R2 的 REBUT 合理——CSD 的 pairwise 比较是 controlled pairs 而非 open tournament，IIA 威胁确实有限。建议在正文（而非脚注）简短讨论即可。降为 Minor。\n\n3. **Design Rationale 位置**（R1 move earlier vs R2 current OK）：Minor 分歧，不影响评分。\n\n---\n\n## Questions\n\n1. 是否考虑过用 human raters 收集少量 ground-truth style bias ratings（如 50-100 pairs），以部分区分 attenuation vs amplification？\n2. 如果将 \"Blindspot\" 重新定义为 \"Likert-Pairwise Divergence\" 或类似中性术语，是否会改变论文的叙事结构？\n3. n=88→n=355 时 Qwen3 Style OR 缩水 49% 的原因是什么？是否其他 judge 也预期有类似缩水？\n4. Claude Sonnet 4 的 BT=56.2% 是否反映了一个真实但较弱的 formality preference？如果是，negative control 的叙事需要如何调整？\n\n---\n\n## Missing References\n\n两位 Reviewer 未指出重大遗漏。Related Work 覆盖较为全面（Thurstone 1927, Stevens 1946, RATE, Comparative Trap, CASSE, FairJudge 等均已引用）。R2-M4 指出部分引用格式不一致（arXiv preprint 与正式发表版本混用），建议统一检查。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（8 项 info，0 critical，0 warning）。主要发现：\n- Page 2: Figure 1 pipeline 图节点内文字偏小（约正文字号 60%），建议放大或改用 figure* 全宽\n- Page 5: Figure 3 散点图尺寸偏小，filled vs open diamond 灰度打印区分度不足\n- Page 6: Table 1 脚注字号很小，scaled replication 说明易被忽略\n- Page 7: Figure 4 x 轴刻度标签偏小（~6pt）；Table 2 与 Figure 4 同页但排布合理\n- Page 11: 单页 4 个表格，行间距偏紧\n- Page 14: Table 14 脚注字号极小\n- Page 19: References 末页 40% 空白（可接受）\n\n无阻塞性排版问题。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference**（两位 Reviewer 独立一致）\n\n**置信度：4 / 5**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**总体判断**：这是一篇方法论扎实、统计处理深度罕见的诊断性工作。CSD 方法论（NLI gating + position-controlled pairwise + GEE decomposition）的设计严谨，robustness checks 全面，切中 RLHF/DPO 依赖 pairwise 而 evaluation 依赖 Likert 的实践痛点。\n\n但三个核心弱点限制了贡献：(1) \"Blindspot\" 的因果归因超出实验证据（三种机制未区分，且 pairwise > Likert 判别力是 Thurstone 1927 已知现象）；(2) negative control 的 TOST 统计力不足，无法排除 Claude 有 moderate style bias，削弱了 \"judge-specific not format-inherent\" 的论点；(3) GEE decomposition 在 n=88 下精度不足（CI 跨 6 倍，OR 缩水 49%），per-judge regime classification 的可靠性存疑。此外，仅 2 个表层风格轴限制了通用性 claim。\n\n**对 EMNLP 2026 的接收建议**：当前版本处于 Borderline Conference / strong Findings 水平。如果作者能解决 MF1（framing 中性化）和 MF2（negative control 扩样本或降级声明），论文有望达到 Conference 水平。MF3（GEE scaled replication）如果无法在 deadline 前完成，至少应在正文中讨论 OR 缩水现象和 CI 宽度对结论的影响。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Opening example（GPT-4o 对 formal vs casual 答案的评分反转）生动有效，但未在 Limitations 中讨论这是否是 cherry-picked\n- \"systematically divergent style sensitivity\"（Abstract line 1）建议改为 \"systematically divergent style sensitivity on surface-level axes\"\n- Contributions list 中 \"GEE conditional decomposition reveals qualitatively distinct per-axis confound structures\" 应提升为第一贡献（R2-N1 共识：GEE 是真正增量贡献）\n\n### Section 2 (Related Work)\n- Thurstone (1927) 被引用但未讨论其与 power analysis（Figure 4）的关系——如果 4-206× 样本量差异可用经典 discriminability 差异解释，需明确论证 LLM judge 场景下的新发现是什么\n- RATE head-to-head 比较（Section 5.1）虽然结构性论证充分，但 \"RATE's own style-related findings may underestimate\" 是推测而非验证过的结论，需更谨慎措辞\n\n### Section 3 (Method)\n- Section 3.1: Rewriting prompt 完整文本应在 Appendix 中给出（R1+R2 共识）\n- Section 3.5 Design Rationale 位置合理（R2 REBUT R1 合理）\n\n### Section 4 (Experiments)\n- Table 1: 建议拆分为 primary + cross-benchmark 两表（R1+R2 共识）\n- Table 2: \"Orig OR\" 首次出现时应展开解释\n- IIA 讨论应从脚注移至正文，简短讨论即可（2-3 句）\n\n### Section 5 (Analysis)\n- Section 5.1: 给 construct divergence 解释同等篇幅\n- Section 5.2 (GEE): 讨论 n=88→n=355 OR 缩水现象\n- \"style bias\" vs \"style sensitivity\" 术语应统一\n\n### Limitations\n- 诚实全面，但第四段 100-point scale 实验的单 judge 限制应标注\n- 考虑增加对 human ground-truth validation 作为 future work 的更 prominent 讨论\n\n### Format\n- 正文 8 页，合规\n- ACL 模板正确，double-blind 无泄露\n- References: 部分 arXiv preprint 与正式发表版本混用，建议统一\n",
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

_source line 1235 · 2026-05-23T05:41:30.739129+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5ce280de124a4e308d1827c6450ad337:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 1236 · 2026-05-23T05:41:45.591499+00:00_

Round 15 审稿完成，报告已投递。

**最终评分：3.5 / 5（Borderline Conference）**，两位 Reviewer 独立一致。

**3 个 Must-Fix 共识问题：**
1. "Blindspot" 因果归因超出证据——Thurstone 以来已知 pairwise > Likert 判别力，三种机制解释未区分，Title/framing 偏向 attenuation 解释
2. Negative control TOST underpowered（Δ=10pp 时 power≈42%），无法排除 Claude 有 moderate style bias
3. GEE n=88 下 CI 极宽（跨 6 倍），OR 缩水 49%，regime classification 可靠性存疑

**6 个 Should-Fix**：style axis 覆盖窄、human annotation 规模小、100-point Likert 单 judge、FK grade cross-axis 未验证、单替代 rewriter、Table 1 密度过高。

Issue Tracker 已同步更新（R2-N1 追加第 15 轮 mention，新增 R15-N1~N3、R15-W1~W6、R15-M1~M4）。视觉审查无阻塞性问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1237 · 2026-05-23T05:41:48.114270+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 全部 13 个问题的逐条回应。核心结论：

- R1 的三个 Must-Fix 全部 **[AGREE]**，与我自己的审稿发现高度互补
- Should-Fix 中 4/5 **[AGREE]**，仅 R1-W4 (IIA assumption) **[REBUT]**——在 CSD 的 controlled pair 设计下 IIA 威胁有限
- Minor 中 4/5 **[AGREE]**，仅 R1-Minor-5 (Design Rationale 位置) **[REBUT]**——当前 "what → why" 顺序合理
- 两位 Reviewer 的 Overall 评分一致（3.5 Borderline Conference）

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

_source line 1238 · 2026-05-23T05:42:04.522572+00:00_

Round 15 审稿流程已完成。报告已投递给 Research Director。

**最终结果：3.5 / 5 — Borderline Conference**（两位 Reviewer 独立一致）

三个 Must-Fix 共识：
1. "Blindspot" 因果归因超出证据（三种机制未区分 + Thurstone 已知现象）
2. Negative control TOST 统计力不足（Δ=10pp 时 power≈42%）
3. GEE n=88 精度不足（CI 跨 6 倍，OR 缩水 49%）

Issue Tracker 已同步更新（R2-N1 novelty 问题追加第 15 轮 mention，新增 R15-N1~N3, W1~W6, M1~M4）。视觉审查结果已拼入报告（8 项 info，无阻塞性问题）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 121

## Round 121

70 recorded events


### User

_source line 1239 · 2026-05-23T06:38:29.032224+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_style_decomp_judge
- 论文路径: projects/causal_style_decomp_judge/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1240 · 2026-05-23T06:38:38.688632+00:00_

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

_source line 1241 · 2026-05-23T06:38:38.739500+00:00_

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

_source line 1242 · 2026-05-23T06:38:45.614409+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-23T06:38:45.715940+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-23T06:38:49.179026+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-23T06:38:49.229675+00:00_



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

_source line 1246 · 2026-05-23T06:38:52.542873+00:00_

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

_source line 1247 · 2026-05-23T06:38:53.851385+00:00_

{"result":"# 项目 causal_style_decomp_judge 概况\n\n## 实验状态 (54 个)\n\n- **verbosity_32b**: DONE (success) — \n- **exp-016**: DONE (killed) — \n- **exp-015**: DONE (killed) — \n- **exp015_clmm**: DONE (success) — \n- **exp013_nli_validation**: DONE (success) — \n- **exp-013**: DONE (killed) — \n- **register_pilot**: DONE (negative) — \n- **exp014_logistic_decomposition**: DONE (success) — \n- **exp012_consistency_bias**: DONE (success) — \n- **exp011_nli_sensitivity**: DONE (success) — \n- **exp010_binarized_likert**: DONE (success) — \n- **tone_pilot**: DONE (negative) — \n- **pairwise_32b**: DONE (success) — \n- **mvp_32b_ate**: DONE (negative) — \n- **mvp_8b_ate**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-23 01:30 UTC\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 近期完成\n\n### 紧急任务批次（6/6 完成或确认）\n- **任务1 — NLI 选择偏差扩展** ✅: formality 全 NS，verbosity 长度选择 p=0.003（保守方向）\n- **任务2 — DA-gate 21 对质量** ✅: 5/5 judges Likert diff 均 NS，可安全纳入\n- **任务3 — Claude cross-benchmark** ✅: AEval×form BT=0.840 Blindspot=true; AEval×verb BT=0.750 Style OR=4.76; MTB×form BT=0.854\n- **任务4a — Cross-benchmark local** ✅: AEval×Llama BT=0.775 NO Blindspot; MTB×Qwen BT=0.700 NO Blindspot\n- **任务5 — 标注扩展数据** ✅: 100 pairs template 拉到本地\n- **任务6 — Construct divergence** ✅: formality rewrite 后 Likert acc 100%→40%\n\n### Bug 修复（3/3）\n- **GEE Style==Orig** ✅: 数据共线性（非代码 bug），cross_benchmark_analysis.py 统计方法已修复\n- **Claude pipeline** ✅: 新建 claude_crossbenchmark_scoring.py，3 配置跑通\n- **数据差异 MTB×Qwen** ✅: Table 1 正确，差异来自 NLI 过滤/方法不一致\n\n## ⚠️ 关键发现\n- Claude 在 LLMBar 是有效 negative control (BT≈55%, NS)，但 AEval/MTB 上有强偏差 (BT 75-85%)\n- Director 决策：negative control 限定 LLMBar only，cross-benchmark 数据转为新发现\n- 合并 TOST 不报告\n\n## 原始 TOST 确认\nRegistry `claude_tost_equivalence` 不受影响：formality p̂=0.562 n=88, verbosity p̂=0.541 n=86\n\n## 趋势\n成功 38 / 负向 12 / 失败 0 / 共 54\n\n## 下一步\n1. 等 Director 确认 task 4b (GPT-4o cross-benchmark) 是否仍需\n2. 等 Paper Agent 完成写作修改\n3. 等标注员回复\n\n## 资源状态\nwestb-29275: 4×RTX PR
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-23T06:38:53.952162+00:00_

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

_source line 1249 · 2026-05-23T06:38:54.053057+00:00_

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
…[truncated 4941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-23T06:39:06.341024+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-23T06:39:07.395908+00:00_

-rw-r--r-- 1 ubuntu ubuntu 433316 May 23 06:28 /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-23T06:39:07.396251+00:00_

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

_source line 1253 · 2026-05-23T06:39:07.547035+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-23T06:39:07.547406+00:00_

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

_source line 1255 · 2026-05-23T06:39:07.597731+00:00_



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

_source line 1256 · 2026-05-23T06:39:10.205120+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1257 · 2026-05-23T06:39:10.757080+00:00_

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

_source line 1258 · 2026-05-23T06:39:10.807605+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
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
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-23T06:39:20.090743+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I've found comprehensive information about EMNLP 2026 call for papers, ARR submission guidelines, and author instructions. Here's a summary:

## EMNLP 2026 Paper Submission Overview

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

### Two-Step Submission Process

Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; Authors commit their reviewed articles to a publication venue (e.g., EMNLP 2026), where Seni
…[truncated 1765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 9885
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-23T06:39:24.965160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 formatting requirements page limits long short paper template anonymity"
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
    "query": "ACL Rolling Review 2026 formatting requirements page limits long short paper template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-23T06:39:25.518009+00:00_

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

_source line 1262 · 2026-05-23T06:39:26.171970+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce systematically divergent sensitivity to surface-level style features when applied to LLM judges.
3	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic methodology that quantifies this divergence under controlled conditions via human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
4	Across four judges from independent providers, one negative control, and two primary axes (formality, verbosity), the divergence is robust: pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\% at stronger effects---replicated across three benchmarks and confirmed by seven statistical methods.
5	GEE conditional decomposition reveals qualitatively distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects a conditional effect where style and content quality contribute jointly---determining which pairwise estimates are directly interpretable and which require decomposition.
6	This divergence admits three non-exclusive explanations---measurement attenuation, format amplification, or construct divergence---that our controlled design bounds but cannot definitively adjudicate.
7	A negative-control judge shows no divergence on either primary axis, supporting discriminative validity.
8	Whether the divergence reflects Likert attenuation, pairwise amplification, or construct-level differences remains open; the practical consequence is unambiguous: Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1263 · 2026-05-23T06:39:26.172524+00:00_

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

_source line 1264 · 2026-05-23T06:39:26.223072+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}---an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations---Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences between absolute and comparative evaluation---which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	Under construct divergence, pairwise and Likert modes may measure distinct constructs---comparative sensitivity versus absolute quality judgment---in which case the divergence reflects measurement scope rather than measurement failure, with different practical implications for audit design (\S\ref{sec:likert_pairwise}).
8	This example reflects a systematic pattern for surface-level style features.
9	
10	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
11	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
12	Despite this consensus, existing approaches address individual requiremen
…[truncated 3781 chars]

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

_source line 1265 · 2026-05-23T06:39:30.897238+00:00_

Web search results for query: "ACL Rolling Review 2026 formatting requirements page limits long short paper template anonymity"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here is information about ACL Rolling Review 2026 formatting requirements:

## Page Limits

Long papers may consist of up to eight (8) pages of content, plus unlimited pages of references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Formatting Requirements

Submissions must adhere to 
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "WebSearch",
  "elapsed_ms": 5932
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-23T06:39:44.382613+00:00_

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

_source line 1267 · 2026-05-23T06:39:44.383052+00:00_

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
…[truncated 5227 chars]

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

_source line 1268 · 2026-05-23T06:39:44.383357+00:00_

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

_source line 1269 · 2026-05-23T06:39:44.484814+00:00_

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
…[truncated 15757 chars]

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

_source line 1270 · 2026-05-23T06:39:44.485263+00:00_

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

_source line 1271 · 2026-05-23T06:39:44.485644+00:00_

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
…[truncated 6344 chars]

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

_source line 1272 · 2026-05-23T06:39:44.485922+00:00_

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

_source line 1273 · 2026-05-23T06:39:44.587426+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: pairwise comparison and Likert scoring produce systematically divergent verdicts on the same style contrasts---complete divergence at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed by seven statistical methods across four judges and three benchmarks.
6	Second, GEE conditional decomposition reveals qualitatively distinct per-axis confound structures---verbosity is style-dominated, formality is a conditional effect, register is judge-dependent---and disambiguates cases where aggregate preference reflects quality detection rather than style sensitivity.
7	Regardless of mechanism, single-format audits risk systematic blind spots; human ground-truth validation of both modes is the key next step.
8	

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

_source line 1274 · 2026-05-23T06:39:50.763446+00:00_

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


### Tool result

_source line 1275 · 2026-05-23T06:39:51.014714+00:00_

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
…[truncated 40830 chars]

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

_source line 1276 · 2026-05-23T06:40:05.741124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-23T06:40:06.696650+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 06:28:27 2026 UTC
ModDate:         Sat May 23 06:28:27 2026 UTC
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
File size:       433316 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-23T06:40:07.148017+00:00_

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

_source line 1279 · 2026-05-23T06:40:07.148431+00:00_

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

_source line 1280 · 2026-05-23T06:40:07.399187+00:00_

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

_source line 1281 · 2026-05-23T06:40:07.449694+00:00_

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

_source line 1282 · 2026-05-23T06:40:11.259533+00:00_

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

_source line 1283 · 2026-05-23T06:40:11.260029+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/decisions.yaml\", \"content\": \"_next_id: 76\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 14:09 UTC\\n  summary: '文献蒸馏审视：研究方向无需调整，CSD 填补 #1 空白（多维 style 因果分解），post-MVP 需扩展 judge/benchmark/baseline\\n    覆盖'\\n  rationale: '10 篇论文蒸馏显示：(1) 多维 style 联合因果分解是领域 #1 空白，与 CSD 核心 claim 完全对齐；(2) 竞品 claim\\n    无直接重叠（FairJudge=white-box, Pref Leakage=family-based, Soumik=prompt-dependent）；(3)\\n    同行标准要求 3-5 异构 judge + AlpacaEval/Arena-Hard/MT-Bench + Bootstrap CIs + 对比 LC-AlpacaEval\\n    baseline。当前 MVP 方案足够，research 阶段需按蒸馏标准扩展。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 14:19 UTC\\n  summary: MVP 全量评分 + 分层分析：score 全部 100 条，按 BERTScore 阈值 0.88/0.90/0.92 分层算 ATE，不降低阈值\\n  rationale: 36% pass rate (BERTScore≥0.92) 偏低但 NLI 均值 0.9422 说明语义保留好。降阈值是数据操作，不如保留完整信息。全量评分\\n    (n=100) 保证统计 power，分层分析同时回答\\\"严格阈值下效应是否存在\\\"和\\\"宽松阈值下效应是否增强\\\"。8B H1 fail 不消耗迭代配额（ROADMAP\\n    规则），32B 备用。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 14:20 UTC\\n  summary: H1 content verification 改为 NLI-only gate（≥0.90），BERTScore 降为监控指标，不作为过滤条件\\n  rationale: Reviewer 诊断：36% pass rate 的根因是 BERTScore 惩罚 style transfer 预期的词汇变化（contractions→full\\n    forms 等），而非内容泄漏。NLI 均值 0.9422、抽样 >0.99 证明语义保留良好。BERTScore 作为 token-level 相似度指标与\\n    style transfer 评估目标矛盾（改的就是 token）。Double-rewrite pass rate 更低（21/100）进一步印证。NLI-only\\n    gate 是度量校准（不消耗 8B 迭代配额），与 D002 全量评分兼容——primary ATE 用 NLI≥0.90 子集，secondary 按 BERTScore\\n    分层。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 14:32 UTC\\n  summary: 8B 初步 ATE≈0.028 不可见，归因三因素：Likert 粒度 + 8B rewriter 质量 + RATE corruption。不计入\\n    kill criteria，等 n=100 + 32B\\n  rationale: 36/100 初步数据 Cohen's d=0.055 远低于 0.3 门槛，但三个叠加因素解释了结果：(1) 83% 零差异源于 integer\\n    Likert 无法捕捉 sub-integer 效应；(2) 22% identical rewrites 稀释 ATE；
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-23T06:40:12.470796+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-23T06:40:13.073894+00:00_

issues:
  # ============================================================
  # Round 1-4 issues (all resolved unless noted)
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
    last_seen_round: 15
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
        note: "R9 fresh review 两位 Reviewer 独立再次提出。共识：从 'reveal' 转为 'first systematic quantification'。"
      - round: 10
        reviewers: [1, 2]
        note: "R10 fresh review MF2: 再次独立确认。共识：三处 'reveals' 改为 'demonstrates'/'identifies'，per-axis confound 提升为 co-equal contribution。"
      - round: 11
        reviewers: [1, 2]
        note: "R11 fresh review: R2 列为 Must-Fix (critical)，R1 交叉 [AGREE]。共识：论文真正贡献是 CSD 框架 + GEE decomposition，但被 'Blindspot' 命名和 'reveals' 措辞遮蔽。建议 reframe 为 'first systematic quantification for LLM judges specifically'。"
      - round: 12
        reviewers: [1, 2]
        note: "R12 fresh review: R2 列为 Must-Fix N2 (critical)——Thurstone (1927) 经典结论的领域迁移，'demonstrates'/'identifies' 措辞仍偏发现性。R1 Excitement 3.5/5 认为实践意义构成独立贡献。两位分歧（R1 novelty 认可 vs R2 认为不够）是本轮最大 divergence。"
      - round: 13
        reviewers: [1, 2]
        note: "R13 fresh review: R2 再次列为 Must-Fix (N2)。R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解
…[truncated 14832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-23T06:40:13.074350+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check existing review reports"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-23T06:40:13.278417+00:00_

round_0.md
round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_2.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 204
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-23T06:41:18.223254+00:00_

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

_source line 1289 · 2026-05-23T06:41:42.921719+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24698
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-23T06:41:43.875101+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "你负责**方法严谨性**审查。\n\n## Venue 信息\n- **EMNLP 2026 via ARR** (May cycle)，截止 2026-05-25\n- 正文 ≤8 页（不含 Limitations 和 References），ACL 模板，double-blind\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- Limitations 章节必须有但不计入页数\n\n## 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`（sections/ 子目录有各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf`\n\n## 审查侧重\n请重点审查以下方面，给出逐条 Strengths / Weaknesses / Questions：\n\n1. **CSD pipeline 设计合理性**：style-controlled rewriting → NLI gate → pairwise measurement 的因果推理链条是否完整？NLI gate 的 content preservation 保证是否充分？direction-aware gating 的理论依据？\n\n2. **统计框架严谨性**：\n   - Holm-Bonferroni 多重比较校正策略（6-test primary family + confirmatory + exploratory 的三层分类）是否合理？\n   - Bradley-Terry 模型假设（IIA, unidimensionality）在此场景下是否满足？\n   - GEE conditional decomposition 的 additive model 假设是否得到充分验证？交互效应检验 power 是否足够？\n   - 在 n=88 下 GEE OR 的 CI 宽度和 n=88→n=355 的 49% OR shrinkage 对结论的影响\n\n3. **Negative control (Claude Sonnet 4) 有效性**：\n   - TOST 等价性检验在 Δ=10pp 时仅 power≈42%，negative control 的证据强度是否足够？\n   - 三条收敛证据（TOST, GEE Style OR cross-benchmark consistency, GPT-4o contrast）的论证层级\n\n4. **Robustness 分析**：\n   - Human annotation 验证（50 pairs, κ=0.44, A2 pass precision 下界 65.3%）规模和质量\n   - 100-point continuous Likert 实验仅在一个 judge 上测试\n   - Cross-axis contamination（FK grade d=0.50）的处理\n   - Evaluator-producer overlap 缓解（仅一个替代 rewriter，22% OR 降幅）\n\n5. **格式合规**：页数限制、匿名规则、Limitations 章节完整性\n\n请严格评审，不留情面。输出格式：\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix / Should-Fix / Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: X/5\n```",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**方法严谨性**审查。\n\n## Venue 信息\n- **EMNLP 2026 via ARR** (May cycle)，截止 2026-05-25\n- 正文 ≤8 页（不含 Limitations 和 References），ACL 模板，double-blind\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- Limitations 章节必须有但不计入页数\n\n## 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`（sections/ 子目录有各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf`\n\n## 审查侧重\n请重点审查以下方面，给出逐条 Strengths / Weaknesses / Questions：\n\n1. **CSD pipeline 设计合理性**：style-controlled rewriting → NLI gate → pairwise measurement 的因果推理链条是否完整？NLI gate 的 content preservation 保证是否充分？direction-aware gating 的理论依据？\n\n2. **统计框架严谨性**：\n   - Holm-Bonferroni 多重比较校正策略（6-test primary family + confirmatory + exploratory 的三层分类）是否合理？\n   - Bradley-Terry 模型假设（IIA, unidimensionality）在此场景下是否满足？\n   - GEE conditional decomposition 的 additive model 假设是否得到充分验证？交互效应检验 power 是否足够？\n   - 在 n=88 下 GEE OR 的 CI 宽度和 n=88→n=355 的 49% OR shrinkage 对结论的影响\n\n3. **Negative control (Claude Sonnet 4) 有效性**：\n   - TOST 等价性检验在 Δ=10pp 时仅 power≈42%，negative control 的证据强度是否足够？\n   - 三条收敛证据（TOST, GEE Style OR cross-benchmark consistency, GPT-4o contrast）的论证层级\n\n4. **Robustness 分析**：\n   - Human annotation 验证（50 pairs, κ=0.44, A2 pass precision 下界 65.3%）规模和质量\n   - 100-point continuous Likert 实验仅在一个 judge 上测试\n   - Cross-axis contamination（FK grade d=0.50）的处理\n   - Evaluator-producer overlap 缓解（仅一个替代 rewriter，22% OR 降幅）\n\n5. **格式合规**：页数限制、匿名规则、Limitations 章节完整性\n\n请严格评审，不留情面。输出格式：\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix / Should-Fix / Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: X/5\n```",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 1291 · 2026-05-23T06:42:01.370466+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17495
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-23T06:42:01.776250+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "你负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **EMNLP 2026 via ARR** (May cycle)，截止 2026-05-25\n- 正文 ≤8 页（不含 Limitations 和 References），ACL 模板，double-blind\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- Limitations 章节必须有但不计入页数\n\n## 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`（sections/ 子目录有各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf`\n\n## 审查侧重\n请重点审查以下方面，给出逐条 Strengths / Weaknesses / Questions：\n\n1. **Novelty 定位**：\n   - \"Likert Blindspot\" 概念——Thurstone (1927) 以来已知 pairwise comparison 判别力优于 absolute rating，本文的增量贡献是什么？\n   - 论文是否清晰区分了三种解释机制（attenuation / amplification / construct divergence）？Title \"Blindspot\" 是否暗示了对 Likert attenuation 的因果偏好？\n   - GEE conditional decomposition 作为方法论贡献是否被充分突出？\n   - 与 RATE (Reber et al. 2025) 的差异化是否清晰？\n\n2. **Claim 与证据匹配**：\n   - \"systematic pattern\" / \"robust\" 等措辞是否有足够证据支撑（仅 2 个表层风格轴 + 1 个 exploratory）？\n   - Negative control 的 claim 边界——\"discriminative validity\" 在 TOST underpowered 条件下是否成立？\n   - Cross-benchmark replication 中的 severity spectrum 解释是否 ad hoc？\n\n3. **Related Work 覆盖度**：\n   - 心理测量学文献（Thurstone, Stevens, 等）是否充分讨论了与本文发现的关系？\n   - CASSE (2026), FairJudge (2026), Soumik (2026), Li (2026) 等近期竞品的定位是否准确？\n   - 是否遗漏重要的 LLM judge bias 或 measurement theory 文献？\n\n4. **展示质量**：\n   - Table 1 信息密度——15 行 + 6 行脚注是否过载？是否应拆分？\n   - 'style bias' vs 'style sensitivity' 措辞一致性\n   - 论文叙事流畅度——从 Introduction 到 Conclusion 的逻辑链是否连贯？\n   - Abstract 是否准确反映论文实际贡献（尤其是 construct divergence 是否得到同等讨论）？\n\n5. **Scope 与 Limitations 充分性**：\n   - Limitations 章节是否覆盖了所有关键限制？\n   - \"Code and Data\" 承诺是否满足 venue 要求？\n\n请严格评审，不留情面。输出格式：\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix / Should-Fix / Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: X/5\n```",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **EMNLP 2026 via ARR** (May cycle)，截止 2026-05-25\n- 正文 ≤8 页（不含 Limitations 和 References），ACL 模板，double-blind\n- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n- Limitations 章节必须有但不计入页数\n\n## 论文路径\n- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`（sections/ 子目录有各章节）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf`\n\n## 审查侧重\n请重点审查以下方面，给出逐条 Strengths / Weaknesses / Questions：\n\n1. **Novelty 定位**：\n   - \"Likert Blindspot\" 概念——Thurstone (1927) 以来已知 pairwise comparison 判别力优于 absolute rating，本文的增量贡献是什么？\n   - 论文是否清晰区分了三种解释机制（attenuation / amplification / construct divergence）？Title \"Blindspot\" 是否暗示了对 Likert attenuation 的因果偏好？\n   - GEE conditional decomposition 作为方法论贡献是否被充分突出？\n   - 与 RATE (Reber et al. 2025) 的差异化是否清晰？\n\n2. **Claim 与证据匹配**：\n   - \"systematic pattern\" / \"robust\" 等措辞是否有足够证据支撑（仅 2 个表层风格轴 + 1 个 exploratory）？\n   - Negative control 的 claim 边界——\"discriminative validity\" 在 TOST underpowered 条件下是否成立？\n   - Cross-benchmark replication 中的 severity spectrum 解释是否 ad hoc？\n\n3. **Related Work 覆盖度**：\n   - 心理测量学文献（Thurstone, Stevens, 等）是否充分讨论了与本文发现的关系？\n   - CASSE (2026), FairJudge (2026), Soumik (2026), Li (2026) 等近期竞品的定位是否准确？\n   - 是否遗漏重要的 LLM judge bias 或 measurement theory 文献？\n\n4. **展示质量**：\n   - Table 1 信息密度——15 行 + 6 行脚注是否过载？是否应拆分？\n   - 'style bias' vs 'style sensitivity' 措辞一致性\n   - 论文叙事流畅度——从 Introduction 到 Conclusion 的逻辑链是否连贯？\n   - Abstract 是否准确反映论文实际贡献（尤其是 construct divergence 是否得到同等讨论）？\n\n5. **Scope 与 Limitations 充分性**：\n   - Limitations 章节是否覆盖了所有关键限制？\n   - \"Code and Data\" 承诺是否满足 venue 要求？\n\n请严格评审，不留情面。输出格式：\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix / Should-Fix / Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n...\n\n## Overall Assessment\nScore: X.X\nConfidence: X/5\n```",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 1293 · 2026-05-23T06:42:03.473483+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1697
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-23T06:42:10.501824+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-23T06:42:12.460482+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_style_decomp_judge'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1958
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-23T06:42:12.562835+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NOT_FOUND_IN_CONFIG\"",
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-23T06:42:12.717389+00:00_

NOT_FOUND_IN_CONFIG

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

_source line 1298 · 2026-05-23T06:42:15.627925+00:00_

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

_source line 1299 · 2026-05-23T06:42:15.678527+00:00_

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

_source line 1300 · 2026-05-23T06:42:18.996703+00:00_

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

_source line 1301 · 2026-05-23T06:42:19.503785+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Glob",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-23T06:42:24.004316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/registry.yaml') as f:\n    data = yaml.safe_load(f)\nproj = data.get('projects', {}).get('causal_style_decomp_judge', {})\next = proj.get('external_review', {})\nprint(json.dumps(ext, indent=2, default=str))\n\" 2>/dev/null || echo \"REGISTRY_NOT_FOUND\"",
  "description": "Check external review config in registry"
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
    "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/registry.yaml') as f:\n    data = yaml.safe_load(f)\nproj = data.get('projects', {}).get('causal_style_decomp_judge', {})\next = proj.get('external_review', {})\nprint(json.dumps(ext, indent=2, default=str))\n\" 2>/dev/null || echo \"REGISTRY_NOT_FOUND\"",
    "description": "Check external review config in registry"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-23T06:42:24.360111+00:00_

REGISTRY_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "Bash",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-23T06:42:27.777938+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -name \"registry.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Find registry/config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_5 -name \"registry.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Find registry/config files"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-23T06:42:27.928969+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml

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


### Tool call

_source line 1306 · 2026-05-23T06:42:31.139605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review in project registry"
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
    "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/registry.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review in project registry"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-23T06:42:31.190241+00:00_

NO_EXTERNAL_REVIEW_CONFIG

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


### Assistant

_source line 1308 · 2026-05-23T06:42:42.575023+00:00_

外部审稿未配置（`external_review` 不在项目 registry 中），跳过 Step 0.6。

当前状态：
- ✅ 视觉审查：已派发（running）
- ⏳ Reviewer 1（方法严谨性）：等待回复
- ⏳ Reviewer 2（新颖性/完整性）：等待回复

等待两位 Reviewer 独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1309 · 2026-05-23T06:46:34.290219+00:00_

[Reviewer 2 审稿意见]:
## Summary

本文提出 Controlled Style Decomposition (CSD)，一套针对 LLM judge 的黑盒诊断方法，用于量化 Likert 评分与 pairwise 比较在表层风格敏感度上的系统性差异（"Likert Blindspot"）。通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，在 4 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制（Claude Sonnet 4）、2 个主轴（formality, verbosity）+ 1 个探索轴（register）、3 个 benchmark 上展示了 pairwise 在 p < 0.001 处检测到风格偏好，而 Likert 无法检出（p > 0.17）。GEE conditional decomposition 揭示了不同轴的混淆结构差异。

## Strengths

**S1. 严谨的控制实验设计。** CSD 管线（Figure 2）将风格干预、内容保持、测量模式解耦的思路清晰。NLI gate 的双向验证（original→rewrite 且 rewrite→original 均需 entailment，Section 3.2）有效控制了改写引入的内容噪声。BERTScore 作为辅助监控而非门控决策变量，避免了度量堆叠的问题。

**S2. GEE conditional decomposition 是真正的方法论贡献。** Section 5.2 将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 verbosity 跨全部四个 judge 为 style-dominated（Style OR 8–13, Orig OR < 1），而 formality 条件性地受 register/judge 依赖——这在 Thurstone 传统中没有对应物。Table 2 的 Style OR vs Originality OR 对比非常有信息量。

**S3. 多维度复制增强可信度。** 4 judges × 3 benchmarks 的交叉复制（Section 5.3, Table 21），加上 7 种统计方法的一致性确认（Table 13–14），使核心发现不易被归因于特定 judge 或数据集的 artifact。

**S4. Bradley-Terry 建模选择合理。** 使用 BT 模型处理 pairwise 数据而非简单胜率统计，通过 Appendix I 的 goodness-of-fit 检验验证了模型适用性。

**S5. 详尽的附录。** 20 个附录（A–Y）覆盖 NLI 阈值敏感度、cross-axis 污染检查、长度控制回归、rewriter independence、formal power analysis 等，展现了方法论上的细致程度。

## Weaknesses

**W1. [Must-Fix] "Systematic pattern" 的 claim 基础过窄——仅 2 个主轴。**

Abstract 和 Conclusion 反复使用 "systematic"（如 Abstract: "systematically divergent sensitivity"；Conclusion: "systematic blind spots"），但一手证据仅来自 formality 和 verbosity 两个轴，register 为探索性的且未在主表中报告。两个表层特征不足以支撑 "systematic" 这个词的 claim 强度。作为对比，Stureborg et al. (2024) 在类似研究中检验了更多维度。建议：(a) 将 "systematic" 降级为 "consistent across tested axes" 或类似措辞；(b) 或增加至少 1–2 个额外轴（如 conciseness vs. elaboration, technical register）的主要实验。

**W2. [Must-Fix] 负控制的 discriminative validity claim 在 TOST underpowered 条件下不成立。**

Section 5.1 和 Appendix H 将 Claude Sonnet 4 用作负控制，声称其展现 "discriminative validity"。然而 Appendix H 明确承认 TOST 功效不足（"TOST is not significant (p = .156, power = 12%)"）。在等价性检验功效仅 12% 的条件下，未能拒绝零假设不能解释为等价的证据——这是经典的 "absence of evidence ≠ evidence of absence" 错误。论文后文（Section 5.1）说 "six controls ... bound the amplification factor" 但这一结论的统计基础不牢固。建议：(a) 坦率承认负控制的结论是 suggestive 而非 definitive；(b) 报告达到 80% 功效所需的样本量（Appendix L 已有 formal power analysis，可直接引用）；(c) 考虑用 Bayesian equivalence testing 替代频率学 TOST。

**W3. [Should-Fix] Novelty 定位模糊——Thurstone (1927) 以来的增量贡献未充分明确。**

Thurstone (1927) 已证明 pairwise comparison 在 discriminability 上优于 absolute rating，这在心理测量学中是教科书知识。Section 2 的 "Measurement Sensitivity in NLG Evaluation" 段虽引用了 Thurstone、Stevens (1946)、Preston and Colman (2000) 等，但未清晰回答：**在这些已知的测量理论基础上，本文的增量贡献到底是什么？** 

论文的实际增量包括：(a) 在 LLM judge 这个特定场景中量化该差距；(b) GEE 分解揭示 per-axis 混淆结构；(c) 三机制框架。但目前的叙事结构将 "Likert Blindspot" 这一已知现象包装为核心发现，而真正新颖的 GEE 分解（Section 5.2）被压缩在一个子节中。建议重组叙事，将 GEE decomposition 提升为一级贡献，"Blindspot" 降为动机/现象描述。

**W4. [Should-Fix] Construct divergence 在正文中发展不足，与 abstract 承诺不匹配。**

Abstract 提出三种非排他解释（attenuation / amplification / construct divergence），但正文对 construct divergence 的讨论零散且浅尝辄止。Section 5.1 最后一段简短提及 "the two formats may measure genuinely different constructs—absolute quality versus ordinal preference"，Section 6 再次一笔带过。相比之下，attenuation 获得了完整的 bootstrap 分析（Appendix K）和功效曲线（Figure 4）。如果论文声称三种解释并列，那么 construct divergence 需要同等深度的讨论——至少应包含一个操作性定义和可检验的预测。否则应在 abstract 中降低其地位。

**W5. [Should-Fix] Cross-benchmark "severity spectrum" 解释为 post-hoc rationalization。**

Section 5.3 将不同 benchmark（AlpacaEval, LLMBar, MT-Bench）上效果量差异解释为 "severity spectrum"（p.8: "the diagnostic of GEE is sharpest on AlpacaEval"），但这一解释是在观察到结果后构建的，没有预先假设或理论预测。为什么 AlpacaEval 的效应更强？论文归因于 "cross-benchmark configurations targeting the strongest effects"（Table 21），但这本身就是循环论证。建议：(a) 明确标记为 exploratory/post-hoc；(b) 提供 benchmark 特性差异（如指令长度、领域分布）的定量分析来支撑解释。

**W6. [Minor] Title "Blindspot" 隐含因果偏好。**

标题 "The Likert Blindspot" 将测量模式分歧框架为 Likert 的缺陷，但论文自身在 Limitations 和 Section 5.1 承认分歧可能源于 pairwise amplification（即 pairwise 过度放大风格差异）。标题创造了一个 framing bias，暗示 attenuation 是主要机制。Section 6 的 "the Likert Blindspot" 反复出现强化了这一印象。

**W7. [Minor] Table 1 信息密度过高。**

Table 1（p.6）在一张表中压缩了 4 judges × 3 axes 的 BT/Likert 结果 + 3 benchmarks 的交叉复制 + 6 条脚注。建议拆分为：(a) 主表：4 judges × 2 primary axes 的核心 Blindspot 结果；(b) 附表：cross-benchmark replication 和 register axis 结果。

**W8. [Minor] 'style bias' 与 'style sensitivity' 混用。**

论文在不同位置交替使用 "style bias"（暗示系统性偏差/错误）和 "style sensitivity"（中性描述）。例如 Section 1 用 "style sensitivity"，Abstract 用 "sensitivity"，但 Section 2 Related Work 标题用 "Style Bias Detection and Mitigation"，Section 5.1 内用 "style preference"。这三个术语有不同含义，应统一或明确区分。

## Questions

**Q1.** 为什么选择 formality 和 verbosity 作为主轴而非其他表层特征（如 sentence length variation, lexical diversity, hedging）？是否因为这两个轴最容易通过 NLI gate 后保持内容不变？如果是，这引入了一个选择偏差：论文可能只展示了 CSD 管线最有利的案例。

**Q2.** GEE 分解中 exchangeable working correlation 的选择依据是什么（Appendix B 提到 robust standard errors）？如果 judge-level clustering 的真实相关结构不是 exchangeable，GEE 的点估计仍一致但效率可能损失。是否尝试过其他 correlation structures（AR(1), unstructured）？

**Q3.** NLI gate 使用 DeBERTa-v3-large 且阈值 0.90。Table 8（Appendix F）显示阈值敏感度，但 NLI 模型本身的 bias 是否会引入系统性偏差？例如，DeBERTa 可能对某些改写方向（formal→casual）比另一方向更宽容，导致通过 gate 的样本在两个方向上不对称。Section 3.2 提到 "bidirectional entailment" 但 Table 12（Appendix G）显示 direction-aware gating 还额外放入了 21 pairs——这些 direction-dependent 的 pairs 是否引入了方向偏差？

**Q4.** 论文使用的 4 个 target judges 均为 2024 年下半年的模型版本。LLM judges 的风格敏感度是否可能随模型迭代显著变化（如 RLHF 训练数据的风格分布变化）？论文是否考虑了时间效度问题？

**Q5.** Formal power analysis（Appendix L, Table 12）显示对于 6 个 cells 中的 5 个，所需样本量 n ≥ 1,200——远超当前 n = 88。这意味着论文的主要结论实际上建立在 underpowered 的 Likert 实验上。换言之，Likert 的 "failure" 可能部分是样本量不足的 artifact 而非测量模式本身的限制。论文如何回应这一替代解释？

## Missing References

1. **Item Response Theory (IRT) 文献缺失。** 论文讨论 Likert 量表的测量属性但完全未引用 IRT 框架——现代心理测量学的核心工具。IRT 直接建模 item discrimination 和 difficulty，可以定量回答 "Likert 为什么在某些效应量下失效" 的问题。至少应引用 Embretson & Reise (2000) 或 de Ayala (2009) 并讨论 IRT 视角下的 Blindspot 解释。

2. **Koo & Li (2016) — ICC 可靠性评估。** 论文用 inter-annotator agreement（Appendix V）但未引用 ICC 的标准参考文献。

3. **Bojar et al. (2016) 仅在 Section 3 脚注中提及 WMT 从 ranking 到 rating 的转变，但未深入讨论 WMT 社区在此转变中积累的经验教训**——这与本文核心论点直接相关。

## Overall Assessment

**Score: 3.5 (Borderline Conference)**

**Confidence: 4/5**

**一句话总结：** 方法论设计严谨（尤其是 NLI-gated 控制和 GEE 分解），但核心发现（pairwise > Likert sensitivity）的增量新颖性不足以弥补 claim scope 过宽（2 axes → "systematic"）和关键统计论证缺陷（underpowered TOST → "discriminative validity"）的问题。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计careful，但 TOST underpowered、formal power analysis 显示主实验本身 underpowered for Likert，claim scope超证据 |
| Excitement | 3.0/5 | 核心发现在心理测量学中已知近百年；GEE 分解有方法论价值但被 undersold；实践影响有限（诊断工具但无修复方案） |
| Reproducibility | 4/5 | 详细的实现细节（Appendix R）、承诺开源代码和数据、统计方法充分描述；但人工标注流程细节（Appendix V）较简略 |
| Overall Assessment | 3.5/5 | Borderline Conference — 修复 claim scope 和 TOST 论证后有望提升至 Conference 级别 |

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

_source line 1310 · 2026-05-23T06:46:47.835374+00:00_

Reviewer 2（新颖性/完整性）已返回审稿意见，评分 **3.5 (Borderline Conference)**。主要发现：2 个 Must-Fix（claim scope 过宽、TOST underpowered）、3 个 Should-Fix（novelty 定位、construct divergence 不足、severity spectrum post-hoc）、3 个 Minor。

等待 Reviewer 1（方法严谨性）返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1311 · 2026-05-23T06:46:50.477268+00:00_

[Reviewer 2 审稿结果]:
清理完成。

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

_source line 1312 · 2026-05-23T06:46:56.808452+00:00_

Reviewer 2 审稿已收到（Score: 3.5, Borderline Conference）。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 124

## Round 124

6 recorded events


### User

_source line 1313 · 2026-05-23T06:48:36.749634+00:00_

[Reviewer 1 审稿意见]:

## Summary

本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，用于量化 LLM judge 在 pairwise comparison 与 Likert scoring 两种评测模式下对表面风格特征的敏感性差异。核心发现为"Likert Blindspot"：pairwise comparison 能检测到统计显著的风格偏好（BT p < 0.001），而 Likert scoring 在同一数据上无法检测到（p > 0.17）。GEE 条件分解进一步揭示了不同风格轴的混淆结构差异——verbosity 为 style-dominated，formality 为 conditional effect（judge-dependent）。

## Strengths

**S1. 研究问题重要且新颖。** 测量模式对 LLM judge 风格敏感性的系统影响此前未被严格量化。鉴于 pairwise 和 Likert 在 RLHF/DPO 和 benchmark evaluation 中分别占主导地位，这一发现对 LLM evaluation pipeline 设计有直接实践意义。论文将其定位为 measurement methodology 问题而非单纯的 bias cataloging，这是正确的视角。

**S2. 统计框架全面且层次清晰。** 三层分析设计（6-test primary family with Holm-Bonferroni at α=0.05 → confirmatory replication → exploratory analyses）结构合理。七种统计方法（BT model, signed test, Likert ATE t-test, binomial Likert, ordinal regression, GEE exchangeable, Wilcoxon signed-rank）的 sensitivity hierarchy（Table 13, Appendix M）提供了方法论层面的 insight——只有 pairwise-based 方法达到显著性，这本身就是核心发现的有力佐证。Holm-Bonferroni 扩展至 8-test family 后结果依然显著（Appendix S, Table 18），增强了可信度。

**S3. 多 judge、多 benchmark 的系统性复制。** 四个独立 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）横跨四种不同架构，三个 benchmark（AlpacaEval, MT-Bench, LLMBar），核心发现的一致性令人信服。特别是 Table 1 中 verbosity 在全部四个 judge 上均展现 style preference（BT > 0.50, all p < 0.0001），且 Likert 均不显著，这是强有力的证据。Cross-benchmark replication（Table 21, Appendix U）在 AlpacaEval 和 MT-Bench 上均复制了 Blindspot 和 GEE structure，进一步排除了 benchmark-specific artifact 的可能。

**S4. GEE 条件分解提供了超越"存在 bias"的结构性洞见。** 将 aggregate preference 分解为 style-specific 和 quality-correlated components（Table 2），并发现 verbosity 是 style-dominated（Style OR 8–13, Orig OR < 1）而 formality 是 conditionally style-driven（Style OR 显著但 Orig OR 也显著），这是比简单的"存在 verbosity bias"更有用的诊断信息。四个 judge 上 confound structure 的一致性（verbosity 一致 style-dominated, formality judge-dependent）使这一分解可信。

**S5. 论文组织和写作质量高。** 正文 8 页内容密度极高但逻辑清晰，从现象（Blindspot）→ 机制（GEE decomposition）→ 验证（robustness）的叙事连贯。Figure 2 的 DAG 和 Figure 3 的 detection probability 可视化有效传达了核心发现。附录体系（A–Y）提供了详尽的技术细节，展现了严谨的研究态度。

---

## Weaknesses

**W1. [Must-Fix] NLI gate 的 content preservation 验证不充分，削弱因果推断基础。**

- **具体位置**：Section 3.2, Section V (Appendix, p.16), Section 5.4 (p.8)
- **问题**：NLI gate 是 CSD 因果推理链条的关键环节——它负责阻断 R→Q 路径（Figure 2），确保 rewrite 只改变 style 而不改变 content quality。但人工验证存在三个层面的不足：
  1. **规模过小**：仅 50 pairs（n=88 的 57%），且仅由 2 名标注员评估；
  2. **标注员一致性偏低**：inter-annotator κ = 0.44（moderate agreement），对于一个二分类任务（content-preserving vs. not）这一数值偏弱，说明"content preservation"的操作定义本身可能不够清晰；
  3. **precision 下界令人担忧**：A2 pass precision 的 95% CI 下界仅 65.3%（CI [65.3%, 93.6%]），意味着 NLI gate 通过的 pairs 中可能有高达 ~35% 存在 content contamination。
- **为什么影响接收**：如果 ~35% 的 NLI-passed pairs 存在 content 差异，那么 pairwise comparison 检测到的"style sensitivity"可能部分反映了 content quality difference 而非纯粹的 style effect。这直接动摇了论文的核心因果 claim。论文在 Limitations 中提到这一问题但将其定性为"alternative interpretation"，这不够充分。
- **建议修改方向**：(a) 扩大人工验证规模至全部 88 pairs，增加至 3+ 名标注员；(b) 提供更细粒度的 content change taxonomy（e.g., factual error vs. nuance shift vs. elaboration），而非简单的 binary judgment；(c) 对 human-flagged content-changed pairs 进行 sensitivity analysis——移除这些 pairs 后核心发现是否依然成立。

**W2. [Must-Fix] Negative control (Claude Sonnet 4) 的 TOST 等价性检验严重 underpowered，negative control 证据不具说服力。**

- **具体位置**：Section 5.1 (p.6), Appendix H (p.12), Table 9 (p.13)
- **问题**：TOST 在 Δ=10pp 等价性边界下 power 仅 42%（Table 9）。这意味着即使 Claude 真的没有 style preference，也有 58% 的概率无法拒绝非等价的 null。论文承认这一点并转而依赖"三条收敛证据"：
  1. TOST 在 Δ=15pp 时 p=0.01——但 15pp 的等价性边界过宽，实际意义有限；
  2. GEE Style OR 跨三个 benchmark 一致不显著（1.47/1.99/1.64）——但 non-significance ≠ evidence of absence，且 OR=1.99 本身并不小；
  3. GPT-4o contrast——这是一个 qualitative comparison，不是 formal test。
- **为什么影响接收**：Negative control 是验证 CSD pipeline 不会系统性产生 false positive 的关键。如果 negative control 证据不足，读者无法排除 CSD pipeline 本身（rewriting artifact、NLI gate leak 等）导致了观测到的 style sensitivity。论文在 Limitations 中仅轻描淡写为"with larger samples could formalize whether the Likert effect size is practically zero"。
- **建议修改方向**：(a) 明确报告达到 80% power 所需的 negative control 样本量（根据 Table 9 推算约需 n≈200）；(b) 对现有 convergent evidence 做更审慎的讨论——特别是 GEE Style OR=1.99 虽不显著但 point estimate 并非 trivial；(c) 考虑增加第二个 negative control judge 以增强证据。

**W3. [Should-Fix] GEE OR 在样本量增大时出现 49% shrinkage，报告的效应量可能严重高估。**

- **具体位置**：Section 5.2 (p.7), Table 2
- **问题**：Qwen3-32B formality Style OR 从 n=88 时的 4.20 降至 n=355 时的 2.15（−49%）。论文将此归因于 small-sample upward bias（Nemes et al., 2009），并指出 CI 收缩比率 1.94× 接近理论值 √(355/88)≈2.01。但这一 defense 有两个问题：
  1. Nemes et al. (2009) 讨论的是 OR 在小样本下的 bias 校正，但 49% 的 shrinkage 远超该文报告的典型校正幅度（通常 <20%）。这可能反映了 n=88 时的 effect inflation 和 n=355 时样本构成变化（NLI gate 通过率不同）的混合效应；
  2. 论文仅对 Qwen3-32B formality 一个条件报告了 n=355 的 scaled replication——如果所有 judge×axis 条件都展现类似 shrinkage，那么 Table 2 报告的所有 ORs 可能都需要大幅下调。
- **为什么影响评分**：Table 2 是 GEE decomposition 的核心结果。如果 Style ORs 普遍被高估 ~50%，虽然 qualitative regime classification（style-dominated vs. conditional）可能不变，但 effect size 的量级解读会有本质不同——OR=4.20 vs. OR=2.15 对实践的 implication 差异很大。
- **建议修改方向**：(a) 对所有 judge×axis 条件都报告 scaled replication 的 ORs（如果数据可用）；(b) 讨论 small-sample bias correction 方法（如 Haldane correction, exact conditional OR）是否能缩小这一差距；(c) 在正文中更显著地 caveat Table 2 的 ORs 可能高估。

**W4. [Should-Fix] Evaluator-producer overlap 的缓解检验不充分，仅测试了一个替代 rewriter。**

- **具体位置**：Section 5.4 (p.8), Appendix E (Table 6-7, p.11)
- **问题**：当 Qwen3-32B 同时作为 rewriter 和 judge 时，存在 evaluator-producer overlap——同一模型族的共享 style preference 可能 inflate 观测到的 bias。论文用 GPT-4o 作为替代 rewriter 测试，发现 Style OR 下降 22%（13.10→~10.17），Blindspot 依然成立。但这一缓解有两个局限：
  1. 仅测试了一个替代 rewriter，且 GPT-4o 本身也是 instruction-tuned LLM——如果 overlap 是 instruction-tuned LLM 的共性特征，用另一个 instruction-tuned LLM 替换无法排除这一 confound；
  2. 22% OR 降幅本身是 non-trivial 的，论文将其定性为"bounding this to a 22% Style OR reduction"，但这是一个 lower bound on the overlap effect，真实的 overlap 可能更大。
- **建议修改方向**：(a) 测试一个非 instruction-tuned 的 rewriter（如 rule-based paraphrasing 或 human rewriting）以彻底排除 shared LLM style preference；(b) 更审慎地讨论 22% 降幅的含义——这是否意味着约 1/5 的观测效应来自 overlap 而非真实 style sensitivity。

**W5. [Should-Fix] Cross-axis contamination 中 FK grade d=0.50 是 medium effect size，处理不够充分。**

- **具体位置**：Section 5.3 (p.8), Appendix T (Table 19, p.15-16)
- **问题**：Formality rewrites 导致 FK grade shift d=0.50（medium effect by Cohen's convention）。论文将此归因于 sentence-level structural changes（contractions, elaborations）并通过 length-controlled regression 和 GEE word-count covariate 论证这不构成 verbosity contamination。但 FK grade 不仅反映 sentence length，还反映 readability/complexity——一个 d=0.50 的 readability shift 可能独立于 verbosity 影响 judge 的 quality perception。论文的 defense（word count d=−0.03, GEE with word-count covariate OR change <12%）仅控制了 word count 维度，未控制 readability 本身。
- **建议修改方向**：在 GEE 中加入 FK grade 作为 covariate，验证 controlling for readability 后 formality Style OR 是否依然显著。

**W6. [Should-Fix] 100-point continuous Likert 仅在一个 judge (Qwen3-32B) 上测试，generalizability 未知。**

- **具体位置**：Section 5.1 (p.6), Appendix O (p.14)
- **问题**：这是排除"Likert Blindspot 仅因为 granularity 不足"这一替代解释的关键实验。但仅在 Qwen3-32B 上测试，无法排除其他 judge 可能在 100-point scale 上表现出不同 pattern 的可能。特别是 Llama-3.3-70B 和 Gemini-2.5-Flash 的 scale usage 特性可能与 Qwen3-32B 不同。
- **建议**：至少在一个额外 judge 上复制 100-point Likert 实验。

**W7. [Minor] Bradley-Terry 模型的 unidimensionality 假设与论文核心论点存在张力。**

- **具体位置**：Section 3 (p.3-4), Appendix I (p.12)
- **问题**：BT 模型假设 pairwise preference 可由单一潜在"quality"维度解释（unidimensionality），但论文的核心论点恰恰是 judges 在多个维度上（style, content quality）进行评估，且不同维度的权重在不同测量模式下不同。Appendix I 报告了 goodness-of-fit 测试通过，但 goodness-of-fit 不等于 assumption validation——即使数据 fit BT model，unidimensionality 也可能被违反。论文应简要讨论这一张力以及为什么 BT 仍然是合适的聚合工具（可以论证 BT 在此场景下只是作为 summary statistic 使用，不依赖 unidimensionality 的因果解读）。

**W8. [Minor] 论文 framing 预设了 pairwise 是"正确"的测量模式，替代解释讨论不足。**

- **具体位置**：Title, Section 1 (p.1), Section 6 (p.8), Limitations (p.9)
- **问题**："Likert Blindspot"这一命名预设了"检测到 style sensitivity"是正确行为，Likert 未检测到是"缺陷"。但等价的替代解读是：pairwise comparison 对 surface-level style 过度敏感，而 Likert 正确地忽略了这些不应影响 quality judgment 的因素。论文在 Limitations 中提及了这一替代解释（"alternative interpretation...Likert captures absolute quality differences while pairwise captures ordinal preference"），但仅用一句话带过。对于一篇以"Blindspot"为标题的论文，这一 framing bias 应得到更充分的讨论。
- **建议**：在 Discussion 中增加 1-2 段讨论在何种 evaluation 场景下 Likert 的 style-insensitivity 实际上是 feature 而非 bug（如 content quality assessment），以及在何种场景下 pairwise 的 style-sensitivity 是 bug 而非 feature（如 style-controlled 实验）。

---

## Questions

**Q1.** Table 2 中 Qwen3-32B verbosity 的 Orig OR = 0.49（p < 0.001），这意味着原始文本在 quality-correlated 维度上被认为 quality 更低。这是否暗示 NLI gate 通过的 verbose rewrites 系统性地引入了 quality improvement 而非仅 style change？如果是，这将动摇"style-only manipulation"的 claim。

**Q2.** Direction-aware gating（Appendix G）对 verbosity 恢复了从 65% 到 86% 的 pass rate。新增的 21% pairs 是否在 style effect magnitude 上与原有 pairs 有系统性差异？如果新增 pairs 的 BT win probability 显著更高，这可能反映了 relaxed gating 导致更多 content-changed pairs 进入分析。

**Q3.** Appendix K (Table 12) 的 formal power analysis 显示 Likert 达到 80% power 需要 n=1,473（GPT-4o formality）至 n=18,157（Llama-70B formality）。这些数字暗示 Likert 在当前实验规模下根本无法检测到任何合理大小的 style effect。论文是否考虑过 Likert 的 non-significance 可能仅反映 power 不足，而非 measurement mode 的本质差异？如果两种模式在 sufficient power 下都能检测到 style effect（只是 Likert 需要更大样本），那么"Blindspot"的命名是否过强？

**Q4.** GEE 使用 exchangeable working correlation structure。鉴于同一 judge 内的 pairs 之间可能存在 heterogeneous correlation（如 difficulty-dependent correlation），是否测试过 AR(1) 或 unstructured correlation？Appendix D 提到了 correlation structure 但未报告 sensitivity to alternative structures。

**Q5.** 论文报告了四个 target judges 但均为 instruction-tuned chat models。是否考虑过 base models 作为 judge？如果 instruction tuning 本身引入了 style preference（这是一个合理假设），那么在 base models 上 Likert Blindspot 可能不存在或表现不同——这将为 mechanism 提供重要线索。

**Q6.** Table 18 (Appendix S) 报告 Holm-Bonferroni 校正后所有 8 个 primary tests 均显著，但 threshold adjusted α 列显示 Gemini-2.5-Flash formality 的 adjusted α = 0.007（最严格）——它的原始 p 值是否足够小？请确认最弱的 test 在 step-down procedure 中的具体 margin。

---

## Missing References

无明显遗漏。论文引用了关键的 prior work（RATE: Reber et al., 2025; Comparative Trap: Jeong et al., 2025; style bias: Wu and Aji, 2025; Saito et al., 2025; Stureborg et al., 2024）。可考虑补充 Zheng et al. (2024) 关于 Chatbot Arena 中 pairwise vs. rating 模式差异的大规模实证分析（如果存在），以提供来自真实用户评估场景的佐证。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心发现（measurement-mode divergence）有充分支持，但因果推断的关键环节（NLI gate validation, negative control）存在显著缺口。W1 和 W2 共同削弱了"style-only effect"的因果 claim |
| Excitement | 3.5/5 | 研究问题重要且实践意义明确，CSD 方法论有推广价值，但 scope 局限于两个 style 轴且缺乏 human-ground-truth validation |
| Reproducibility | 4/5 | 方法描述详尽，统计工具均有公开实现，数据承诺开源。扣分点：rewriting prompts 在 Appendix Y 但 NLI threshold selection 的具体实验细节偏少 |
| Datasets | 3/5 | 88 instruction-response pairs + style-transformed variants 有一定复用价值，但规模有限 |
| Software | 3/5 | 论文描述了 csd Python 库但未提供链接（承诺 upon acceptance 发布） |

## Overall Assessment

**Score: 3.5 (Borderline Conference)**

**Confidence: 4/5**

**一句话总结**：核心发现（pairwise vs. Likert 对 style 的敏感性差异）证据充分且实践价值明确，但因果推断链条的两个关键环节——NLI gate 的 content preservation 验证（W1: κ=0.44, precision lower bound 65.3%）和 negative control 的等价性检验（W2: TOST power 42%）——存在显著缺口，使得"这是 measurement mode 的本质差异而非 content confound 或 pipeline artifact"这一核心 claim 未被充分 establish。GEE OR 的 49% shrinkage（W3）进一步增加了对效应量报告准确性的担忧。建议在 resubmission 中优先解决 W1（扩大人工验证）和 W2（增加 negative control 样本量或增加第二个 control judge），这两项修改应能将论文推至 Conference 水平。


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

_source line 1314 · 2026-05-23T06:49:27.605471+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Summary**: 本文提出 CSD，一套针对 LLM judge 的黑盒诊断方法，用于量化 Likert 评分与 pairwise 比较在表层风格敏感度上的系统性差异。通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，在 4 个 judge + 1 个负控制、2 个主轴 + 1 个探索轴、3 个 benchmark 上展示了 pairwise 在 p < 0.001 处检测到风格偏好，而 Likert 无法检出。GEE conditional decomposition 揭示了不同轴的混淆结构差异。\n\n**Strengths**:\nS1. 严谨的控制实验设计——CSD 管线将风格干预、内容保持、测量模式解耦的思路清晰。NLI gate 双向验证有效控制了改写引入的内容噪声。\nS2. GEE conditional decomposition 是真正的方法论贡献——将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 verbosity 跨全部四个 judge 为 style-dominated，而 formality 条件性地受 judge 依赖——这在 Thurstone 传统中没有对应物。\nS3. 多维度复制增强可信度——4 judges × 3 benchmarks 的交叉复制 + 7 种统计方法的一致性确认。\nS4. BT 建模选择合理——通过 Appendix I 的 goodness-of-fit 检验验证了模型适用性。\nS5. 详尽的附录——20 个附录覆盖广泛的 robustness 分析。\n\n**Weaknesses**:\nW1. [Must-Fix] \"Systematic pattern\" 的 claim 基础过窄——仅 2 个主轴。Abstract 和 Conclusion 反复使用 \"systematic\"，但一手证据仅来自 formality 和 verbosity，register 为探索性的。两个表层特征不足以支撑 \"systematic\" claim。\nW2. [Must-Fix] 负控制的 discriminative validity claim 在 TOST underpowered 条件下不成立——TOST 在 Δ=10pp 下 power 仅 12%，absence of evidence ≠ evidence of absence。三条收敛证据的统计基础不牢固。\nW3. [Should-Fix] Novelty 定位模糊——Thurstone (1927) 以来的增量贡献未充分明确。GEE 分解被 undersold，\"Blindspot\" 被包装为核心发现。\nW4. [Should-Fix] Construct divergence 在正文中发展不足，与 abstract 承诺不匹配。Attenuation 获得了完整 bootstrap 分析和功效曲线，但 construct divergence 仅简短提及。\nW5. [Should-Fix] Cross-benchmark \"severity spectrum\" 解释为 post-hoc rationalization——没有预先假设或理论预测。\nW6. [Minor] Title \"Blindspot\" 隐含因果偏好。\nW7. [Minor] Table 1 信息密度过高——建议拆分。\nW8. [Minor] 'style bias' 与 'style sensitivity' 混用。\n\n**Questions**:\nQ1. 为什么选择 formality 和 verbosity 作为主轴？是否因为最容易通过 NLI gate？\nQ2. GEE 中 exchangeable working correlation 的选择依据？是否尝试其他 correlation structures？\nQ3. NLI gate 使用 DeBERTa-v3-large 的 bias 是否会引入系统性偏差？Direction-aware gating 的 21 pairs 是否引入方向偏差？\nQ4. 4 个 target judges 均为 2024 年下半年模型，时间效度问题？\nQ5. Formal power analysis 显示 Likert 需 n≥1,200，Likert 的 \"failure\" 可能部分是样本量不足的 artifact？\n\n**Missing References**: IRT 文献（Embretson & Reise 2000）、ICC 可靠性评估（Koo & Li 2016）、Bojar et al. (2016) WMT 转变经验\n\n**Overall Assessment**: Score 3.5, Confidence 4/5\n\n---\n\n请对以上每个 Weakness（W1-W8）和 Question（Q1-Q5）逐条标注 [AGREE] 或 [REBUT]，并简要说明理由。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge",
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
    "text": "以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Summary**: 本文提出 CSD，一套针对 LLM judge 的黑盒诊断方法，用于量化 Likert 评分与 pairwise 比较在表层风格敏感度上的系统性差异。通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，在 4 个 judge + 1 个负控制、2 个主轴 + 1 个探索轴、3 个 benchmark 上展示了 pairwise 在 p < 0.001 处检测到风格偏好，而 Likert 无法检出。GEE conditional decomposition 揭示了不同轴的混淆结构差异。\n\n**Strengths**:\nS1. 严谨的控制实验设计——CSD 管线将风格干预、内容保持、测量模式解耦的思路清晰。NLI gate 双向验证有效控制了改写引入的内容噪声。\nS2. GEE conditional decomposition 是真正的方法论贡献——将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 verbosity 跨全部四个 judge 为 style-dominated，而 formality 条件性地受 judge 依赖——这在 Thurstone 传统中没有对应物。\nS3. 多维度复制增强可信度——4 judges × 3 benchmarks 的交叉复制 + 7 种统计方法的一致性确认。\nS4. BT 建模选择合理——通过 Appendix I 的 goodness-of-fit 检验验证了模型适用性。\nS5. 详尽的附录——20 个附录覆盖广泛的 robustness 分析。\n\n**Weaknesses**:\nW1. [Must-Fix] \"Systematic pattern\" 的 claim 基础过窄——仅 2 个主轴。Abstract 和 Conclusion 反复使用 \"systematic\"，但一手证据仅来自 formality 和 verbosity，register 为探索性的。两个表层特征不足以支撑 \"systematic\" claim。\nW2. [Must-Fix] 负控制的 discriminative validity claim 在 TOST underpowered 条件下不成立——TOST 在 Δ=10pp 下 power 仅 12%，absence of evidence ≠ evidence of absence。三条收敛证据的统计基础不牢固。\nW3. [Should-Fix] Novelty 定位模糊——Thurstone (1927) 以来的增量贡献未充分明确。GEE 分解被 undersold，\"Blindspot\" 被包装为核心发现。\nW4. [Should-Fix] Construct divergence 在正文中发展不足，与 abstract 承诺不匹配。Attenuation 获得了完整 bootstrap 分析和功效曲线，但 construct divergence 仅简短提及。\nW5. [Should-Fix] Cross-benchmark \"severity spectrum\" 解释为 post-hoc rationalization——没有预先假设或理论预测。\nW6. [Minor] Title \"Blindspot\" 隐含因果偏好。\nW7. [Minor] Table 1 信息密度过高——建议拆分。\nW8. [Minor] 'style bias' 与 'style sensitivity' 混用。\n\n**Questions**:\nQ1. 为什么选择 formality 和 verbosity 作为主轴？是否因为最容易通过 NLI gate？\nQ2. GEE 中 exchangeable working correlation 的选择依据？是否尝试其他 correlation structures？\nQ3. NLI gate 使用 DeBERTa-v3-large 的 bias 是否会引入系统性偏差？Direction-aware gating 的 21 pairs 是否引入方向偏差？\nQ4. 4 个 target judges 均为 2024 年下半年模型，时间效度问题？\nQ5. Formal power analysis 显示 Likert 需 n≥1,200，Likert 的 \"failure\" 可能部分是样本量不足的 artifact？\n\n**Missing References**: IRT 文献（Embretson & Reise 2000）、ICC 可靠性评估（Koo & Li 2016）、Bojar et al. (2016) WMT 转变经验\n\n**Overall Assessment**: Score 3.5, Confidence 4/5\n\n---\n\n请对以上每个 Weakness（W1-W8）和 Question（Q1-Q5）逐条标注 [AGREE] 或 [REBUT]，并简要说明理由。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-23T06:49:54.628730+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27023
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-23T06:49:55.131552+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Summary**: 本文提出 CSD，一种黑盒诊断方法，用于量化 LLM judge 在 pairwise comparison 与 Likert scoring 两种评测模式下对表面风格特征的敏感性差异。核心发现为\"Likert Blindspot\"：pairwise comparison 能检测到统计显著的风格偏好（BT p < 0.001），而 Likert 在同一数据上无法检测到（p > 0.17）。GEE 条件分解揭示了不同风格轴的混淆结构差异。\n\n**Strengths**:\nS1. 研究问题重要且新颖——测量模式对 LLM judge 风格敏感性的系统影响此前未被严格量化，对 RLHF/DPO pipeline 有直接实践意义。\nS2. 统计框架全面且层次清晰——三层分析设计 + 七种统计方法的 sensitivity hierarchy。\nS3. 多 judge、多 benchmark 的系统性复制——四个独立 judge 横跨四种架构，三个 benchmark。\nS4. GEE 条件分解提供了超越\"存在 bias\"的结构性洞见——将 aggregate preference 分解为 style-specific 和 quality-correlated components。\nS5. 论文组织和写作质量高——正文 8 页内容密度极高但逻辑清晰。\n\n**Weaknesses**:\nW1. [Must-Fix] NLI gate 的 content preservation 验证不充分——仅 50 pairs, κ=0.44, A2 pass precision 下界仅 65.3%。如果 ~35% NLI-passed pairs 存在 content contamination，pairwise 检测到的\"style sensitivity\"可能部分反映 content quality difference。\nW2. [Must-Fix] Negative control (Claude Sonnet 4) TOST 等价性检验严重 underpowered——TOST Δ=10pp power 仅 42%，三条收敛证据（TOST Δ=15pp, GEE Style OR cross-benchmark, GPT-4o contrast）中每一条单独看都不具说服力。\nW3. [Should-Fix] GEE OR 在 n=88→n=355 时出现 49% shrinkage——Table 2 报告的效应量可能严重高估。仅对一个条件（Qwen3 formality）有 scaled replication。\nW4. [Should-Fix] Evaluator-producer overlap 缓解不充分——仅测试一个替代 rewriter (GPT-4o)，22% OR 降幅是 lower bound。\nW5. [Should-Fix] FK grade d=0.50 cross-axis contamination 处理不够充分——length-controlled regression 控制了 word count 但未控制 readability 本身。\nW6. [Should-Fix] 100-point continuous Likert 仅在 Qwen3-32B 上测试。\nW7. [Minor] BT 模型 unidimensionality 假设与论文核心论点（judges 在多维度评估）存在张力。\nW8. [Minor] 论文 framing 预设 pairwise 是\"正确\"测量模式。\n\n**Questions**:\nQ1. Table 2 中 Qwen3 verbosity Orig OR=0.49——是否暗示 verbose rewrites 系统性引入 quality improvement？\nQ2. Direction-aware gating 新增的 21% pairs 是否在 style effect magnitude 上与原有 pairs 有系统性差异？\nQ3. Formal power analysis 显示 Likert 需 n=1,473–18,157，Likert non-significance 可能仅反映 power 不足？\nQ4. GEE 是否测试过 AR(1) 或 unstructured correlation？\nQ5. 是否考虑过 base models 作为 judge——instruction tuning 本身可能引入 style preference？\nQ6. Holm-Bonferroni 中 Gemini formality 的具体 margin？\n\n**Missing References**: 无明显遗漏。可考虑补充 Zheng et al. (2024) Chatbot Arena 中 pairwise vs. rating 差异的大规模实证分析。\n\n**Overall Assessment**: Score 3.5, Confidence 4/5\n\n---\n\n请对以上每个 Weakness（W1-W8）和 Question（Q1-Q6）逐条标注 [AGREE] 或 [REBUT]，并简要说明理由。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge",
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
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Summary**: 本文提出 CSD，一种黑盒诊断方法，用于量化 LLM judge 在 pairwise comparison 与 Likert scoring 两种评测模式下对表面风格特征的敏感性差异。核心发现为\"Likert Blindspot\"：pairwise comparison 能检测到统计显著的风格偏好（BT p < 0.001），而 Likert 在同一数据上无法检测到（p > 0.17）。GEE 条件分解揭示了不同风格轴的混淆结构差异。\n\n**Strengths**:\nS1. 研究问题重要且新颖——测量模式对 LLM judge 风格敏感性的系统影响此前未被严格量化，对 RLHF/DPO pipeline 有直接实践意义。\nS2. 统计框架全面且层次清晰——三层分析设计 + 七种统计方法的 sensitivity hierarchy。\nS3. 多 judge、多 benchmark 的系统性复制——四个独立 judge 横跨四种架构，三个 benchmark。\nS4. GEE 条件分解提供了超越\"存在 bias\"的结构性洞见——将 aggregate preference 分解为 style-specific 和 quality-correlated components。\nS5. 论文组织和写作质量高——正文 8 页内容密度极高但逻辑清晰。\n\n**Weaknesses**:\nW1. [Must-Fix] NLI gate 的 content preservation 验证不充分——仅 50 pairs, κ=0.44, A2 pass precision 下界仅 65.3%。如果 ~35% NLI-passed pairs 存在 content contamination，pairwise 检测到的\"style sensitivity\"可能部分反映 content quality difference。\nW2. [Must-Fix] Negative control (Claude Sonnet 4) TOST 等价性检验严重 underpowered——TOST Δ=10pp power 仅 42%，三条收敛证据（TOST Δ=15pp, GEE Style OR cross-benchmark, GPT-4o contrast）中每一条单独看都不具说服力。\nW3. [Should-Fix] GEE OR 在 n=88→n=355 时出现 49% shrinkage——Table 2 报告的效应量可能严重高估。仅对一个条件（Qwen3 formality）有 scaled replication。\nW4. [Should-Fix] Evaluator-producer overlap 缓解不充分——仅测试一个替代 rewriter (GPT-4o)，22% OR 降幅是 lower bound。\nW5. [Should-Fix] FK grade d=0.50 cross-axis contamination 处理不够充分——length-controlled regression 控制了 word count 但未控制 readability 本身。\nW6. [Should-Fix] 100-point continuous Likert 仅在 Qwen3-32B 上测试。\nW7. [Minor] BT 模型 unidimensionality 假设与论文核心论点（judges 在多维度评估）存在张力。\nW8. [Minor] 论文 framing 预设 pairwise 是\"正确\"测量模式。\n\n**Questions**:\nQ1. Table 2 中 Qwen3 verbosity Orig OR=0.49——是否暗示 verbose rewrites 系统性引入 quality improvement？\nQ2. Direction-aware gating 新增的 21% pairs 是否在 style effect magnitude 上与原有 pairs 有系统性差异？\nQ3. Formal power analysis 显示 Likert 需 n=1,473–18,157，Likert non-significance 可能仅反映 power 不足？\nQ4. GEE 是否测试过 AR(1) 或 unstructured correlation？\nQ5. 是否考虑过 base models 作为 judge——instruction tuning 本身可能引入 style preference？\nQ6. Holm-Bonferroni 中 Gemini formality 的具体 margin？\n\n**Missing References**: 无明显遗漏。可考虑补充 Zheng et al. (2024) Chatbot Arena 中 pairwise vs. rating 差异的大规模实证分析。\n\n**Overall Assessment**: Score 3.5, Confidence 4/5\n\n---\n\n请对以上每个 Weakness（W1-W8）和 Question（Q1-Q6）逐条标注 [AGREE] 或 [REBUT]，并简要说明理由。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-23T06:49:56.445424+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1313
}
```

</details>

---


### Assistant

_source line 1318 · 2026-05-23T06:50:00.078274+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1319 · 2026-05-23T06:50:02.881155+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference），Confidence 4/5。

核心发现（pairwise vs. Likert 对 style 的敏感性差异）证据充分，统计框架层次清晰（Holm-Bonferroni 三层设计、七种方法的 sensitivity hierarchy），多 judge 多 benchmark 复制增强了可信度。

主要问题集中在因果推断链条的两个关键环节：
- **W1 [Must-Fix]**：NLI gate 人工验证规模不足（50 pairs, κ=0.44, precision 下界 65.3%），无法排除 ~35% content contamination
- **W2 [Must-Fix]**：Negative control TOST power 仅 42%，三条收敛证据中 GEE Style OR=1.99 的 point estimate 并非 trivial
- **W3 [Should-Fix]**：GEE OR 在 n=88→355 时出现 49% shrinkage，Table 2 报告的效应量可能普遍高估
- **W4–W6 [Should-Fix]**：evaluator-producer overlap 仅测一个替代 rewriter、FK grade d=0.50 处理不充分、100-point Likert 仅测一个 judge

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

_source line 1320 · 2026-05-23T06:50:08.183934+00:00_

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


## Round 126

## Round 126

10 recorded events


### User

_source line 1321 · 2026-05-23T06:52:19.506370+00:00_

[Reviewer 2 审稿意见]:
## 交叉回应：Reviewer 2 对 Reviewer 1 审稿意见的逐条评议

---

### Strengths

[AGREE] R1-S1: 研究问题确实重要——但我对"新颖性"的评估比 R1 更保守。Pairwise vs. rating 的 discriminability 差异自 Thurstone (1927) 起已知近百年，本文的增量贡献在于将其迁移到 LLM judge 场景并提供 GEE 分解工具。R1 将研究问题评为"新颖"可能过于宽容。

[AGREE] R1-S2: 统计框架的层次设计（三层分析 + 七方法 sensitivity hierarchy, Table 13–14）确实是本文的亮点。我在自己的审稿中同样认可这一点。

[AGREE] R1-S3: 多 judge × 多 benchmark 复制是本文最强的方法论资产。

[AGREE] R1-S4: GEE conditional decomposition 是本文最重要的方法论贡献。我在自己的审稿中指出它被 undersold（我的 W3），R1 与我在此一致。

[AGREE] R1-S5: 写作质量在 8 页限制内确实出色，但我同时指出 Table 1 信息密度过高（我的 W7）。

---

### Weaknesses

**[AGREE] R1-W1: NLI gate content preservation 验证不充分。**
R1 指出仅 50 pairs、κ=0.44、A2 pass precision 下界 65.3%。这是一个关键的 validity 威胁，我在审稿中未单独展开但完全同意。补充两点：(a) κ=0.44 在 Landis & Koch 标准下仅为 "moderate agreement"，对于核心 validity check 来说偏低；(b) 论文的 cross-axis contamination 分析（Appendix S, Table 19）显示 word count d=−0.03、type-token ratio d=−0.23，虽然效应量小，但 TTR 的 d=−0.23 并非完全可忽略。如果 NLI-passed pairs 中约 35% 存在 content contamination，pairwise 的更高敏感度可能部分源于它对 content 微妙差异的更强检测力——而非 style sensitivity 本身。这将从根本上威胁 "Likert Blindspot" 的因果归因。

**[AGREE] R1-W2: Negative control TOST underpowered。**
我在自己的审稿中将此列为 Must-Fix（我的 W2），与 R1 完全一致。补充：R1 指出三条收敛证据（TOST Δ=15pp, GEE Style OR cross-benchmark, GPT-4o contrast）"每一条单独看都不具说服力"——我同意这一判断。特别是 GEE Style OR cross-benchmark 的证据（Table 22, Claude Sonnet 4 formality Style OR 1.47/1.99/1.64）虽然比其他 judges 低，但仍然 >1，严格来说并未达到"无效应"的标准。论文将此解释为"quality detection rather than style sensitivity"（Section X, p.17），但这依赖于对 GEE 分解的特定解读，而非独立验证。两位 reviewer 一致认为负控制论证不成立，这应该被视为强信号。

**[AGREE] R1-W3: GEE OR shrinkage 49%。**
Table 2 的 Style OR（n=88）与 scaled replication（n=355）之间 49% 的萎缩（Section 5.2: "Style OR drops from 4.20 to 2.15"）是 winner's curse / small-sample upward bias 的经典表现。R1 正确指出仅 Qwen3 formality 一个条件有 scaled replication。这意味着 Table 2 中其他条件（特别是 Llama-70B verbosity 的 Style OR 4.01, Gemini verbosity 的 Style OR 8.96）可能同样存在严重的效应量膨胀。我在自己的审稿中因篇幅未展开此点，但完全认同。建议论文至少对 verbosity 轴也执行 scaled replication。

**[AGREE] R1-W4: Evaluator-producer overlap 缓解不充分。**
Appendix E 仅用 GPT-4o 作为替代 rewriter，22% OR 降幅是单一数据点。R1 称其为 "lower bound" 合理——如果用更不同的 rewriter（如开源模型、规则 baseline），overlap 效应可能更大。我补充一点：论文将 GPT-4o rewriter 的结果框架为"Blindspot replicates with independent rewriter"（p.11, Section E），但 GPT-4o 与目标 judge 之一（GPT-4o 自身）存在完全重叠，与其他 judges 也可能共享训练数据分布。真正的 independence 需要使用训练数据完全不同的 rewriter。

**[AGREE] R1-W5: FK grade cross-axis contamination。**
FK grade d=0.50 是 medium effect size。论文控制了 word count（Appendix T, Table 20）但 FK grade 是 sentence length × syllable count 的函数，word count 控制不等于 readability 控制。R1 的建议——直接将 FK grade 作为 GEE 协变量——是一个可行且必要的 robustness check。我同意这应列为 Should-Fix。

**[REBUT] R1-W6: 100-point continuous Likert 仅在 Qwen3-32B 上测试。**
R1 的关切合理（单 judge 泛化性有限），但我认为严重程度低于 R1 的评估。理由：(a) 100-point Likert 实验（Appendix O, Table 15）的目的是检验"Blindspot 是否纯粹是量表粒度问题"，而非全面复制主实验。在这个有限目标下，单 judge 足以作为 proof-of-concept：即使用 100 个可能得分值，pairwise BT 仍然 significant (p < 0.001) 而 Likert 仍然 non-significant——说明粒度不是唯一解释；(b) Qwen3-32B 在主实验中是 Likert 效应最强的 judge 之一（Table 1），如果连它都在 100-point 条件下仍然 non-significant，这实际上是对论文论点最保守的检验。但我同意，在 camera-ready 中增加至少一个 judge 的 100-point 复制会增强说服力。

**[AGREE] R1-W7: BT unidimensionality 假设张力。**
BT 模型假设单一潜在维度，但论文核心论点是 judges 同时受 style 和 quality 影响。这确实是一个概念张力。不过我注意到论文在 Limitations 第一段（p.9: "the BT model assumes unidimensionality—a single latent..."）有所讨论，承认 BT 不能分离多维影响，这正是引入 GEE 分解的动机。所以这个张力在论文架构中是被有意识地处理的，但 R1 指出在方法论章节缺乏预先讨论是正确的。

**[AGREE] R1-W8: Framing 预设 pairwise 为"正确"模式。**
与我的审稿 W6（Title "Blindspot" 隐含因果偏好）完全一致。标题和正文多处将分歧框架为 Likert 的"盲点"而非 pairwise 的"过敏"。两位 reviewer 一致指出这一 framing bias，强化了修改的必要性。

---

### Questions

**[AGREE] R1-Q1: Qwen3 verbosity Orig OR=0.49 是否暗示 verbose rewrites 引入 quality improvement？**
这是个好问题。Table 2 中 Orig OR < 1（verbosity 全部四个 judges）意味着 originality 维度上原文被偏好（即 verbose rewrite 降低了感知质量）。这实际上对论文有利：style preference（高 Style OR）和 quality preference（低 Orig OR）方向相反，说明 GEE 成功分离了两个成分。但 R1 的隐含关切是：如果 verbose rewrites 系统性地降低质量，那么 pairwise 模式可能更善于检测 quality 差异而非 style preference——这与 Blindspot 的归因相关。论文应明确讨论这一替代解释。

**[AGREE] R1-Q2: Direction-aware gating 新增 21% pairs 的效应量差异。**
Appendix G（Table 12, p.12）提到 direction-aware gating 额外放入 21 pairs（32%），但未报告这些 pairs 的 BT/Likert 效应量是否与原始 pairs 有系统差异。如果新增 pairs 的效应量更大/更小，这会影响对核心结果的解读。这是一个简单的 robustness check，应该执行。

**[AGREE] R1-Q3: Likert non-significance 可能仅反映 power 不足。**
这是我审稿中的 Q5，两位 reviewer 独立得出相同关切。Formal power analysis（Appendix L, Table 12）显示 Likert 在 5/6 cells 需要 n ≥ 1,200。当前 n=88，Likert 的 "failure" 可能是 underpowered 的数学必然而非 measurement mode 的本质局限。论文虽然提供了 bootstrap attenuation analysis（Appendix K）试图论证 "Blindspot 是 structural 而非 merely power"，但这一分析本身依赖于 pairwise 效应量作为 benchmark——循环论证的嫌疑。两位 reviewer 的一致判断增强了此关切的权重。

**[AGREE] R1-Q4: GEE correlation structure。**
与我的 Q2 一致。论文使用 exchangeable working correlation + robust sandwich SE（Appendix B, D），理论上 GEE 点估计在 correlation structure 误指定下仍一致，但效率损失可能影响 CI 宽度。至少应报告 AR(1) 和 unstructured 的敏感度比较。

**[AGREE] R1-Q5: Base models 作为 judge。**
有价值的建议。Instruction tuning 和 RLHF 可能引入 systematic style preferences（如偏好 formal/verbose 输出），这使得当前所有 target judges 共享一个潜在的 confound。使用 base models（如 Llama-3.3-70B-base）作为对照可以分离 alignment-induced vs. inherent style sensitivity。但我认为这更适合 future work 而非 Must-Fix——base models 通常无法可靠地遵循 judge instructions，实验可行性有限。

**[REBUT] R1-Q6: Holm-Bonferroni 中 Gemini formality 的具体 margin。**
R1 要求报告具体 margin，但 Appendix S（Table 18, p.15）已报告了 Holm-Bonferroni adjusted p-values，其中 Gemini formality 的 Holm-Bonferroni Threshold Adj 列有具体数值。论文称 "All results remain significant under the expanded family"。如果 R1 要求的是 equivalence margin 而非 significance margin，那这属于 Q2（TOST）的范畴，已在 Appendix H 讨论。此问题可能基于对附录细节的遗漏，信息已在论文中提供。

---

### 综合评价

R1 的审稿与我的审稿在核心问题上高度一致：
1. **TOST underpowered**（我的 W2 = R1 的 W2）：两位 reviewer 一致 Must-Fix
2. **Claim scope 过宽**（我的 W1 "systematic" on 2 axes）：R1 未直接提但通过 W3/Q3 间接触及
3. **Likert power 不足作为替代解释**（我的 Q5 = R1 的 Q3）：两位 reviewer 独立得出
4. **Framing bias**（我的 W6 = R1 的 W8）：一致指出

R1 补充了我未充分展开的几个重要技术点：NLI gate 验证不充分（W1）、GEE OR shrinkage（W3）、evaluator-producer overlap（W4）。这些加强了对方法论 soundness 的关切。

两位 reviewer 的共同判断：论文方法论设计用心但多个关键统计论证存在 gap，核心 claim 强度超出证据支撑，Borderline Conference（3.5）。

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
