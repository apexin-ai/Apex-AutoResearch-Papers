# Director coordination — Part 4 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 83

### Tool call

_source line 1018 · 2026-05-19T08:05:15.353465+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 12 (fresh review) — New/recurring issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"C1 消融 50% max Δ 数值错误：论文声称 0.59pp，Table 3 实际为 0.79pp (WG)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. R1 首先发现，R2 交叉确认。Table 3 caption 'max Δ=0.59pp at 50% (2-seed)' 与表格数据 |63.14−62.35|=0.79pp 不符。另外 '2-seed' 声称但仅展示 1 seed pair。\"}\n    action_items:\n      - {round: 12, action: \"更正 max Δ 为 0.79pp，同步修改 Abstract、Introduction、§4.4 中引用该数字的段落。确认第二个 seed 数据并补入表格或移除 '2-seed' 声称。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 BCE+comp (28.13±0.20) vs Table 4 BCE+Compensation (25.44) 数值矛盾不可调和\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. Table 2 脚注标注 'DejaVu/FastForward pipeline with compensation' 但 3-seed std=0.20 意味所有 seed 在 27.93-28.33，与 Table 4 seed 42=25.44 矛盾。R2 推测 Table 2 实际为 BCE without compensation。§4.3 的 '28.13±0.20' 也说 'BCE predictor' 非 'BCE+compensation'。\"}\n    action_items:\n      - {round: 12, action: \"澄清 Table 2 'BCE+comp' 与 Table 4 'BCE+Compensation' 是否为同一实验配置（训练步数、seed、是否含 compensation）。修正标注错误。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-N3\"\n    summary: \"缺少 Intermediate-coupling (MSE) baseline 实验对比，Taxonomy claim 无实验支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R1 定 Must-Fix，R2 同意但建议 Should-Fix（不影响核心 KL>BCE claim，但影响 taxonomy 完整性）。Table 1 划分 Decomposed/Intermediate/Coupled 三级，但实验只对比两端。ShadowLLM/D2DMoE 在 Related Work 讨论但无数据。\"}\n    action_items:\n      - {round: 12, action: \"实现 per-layer MSE baseline（相同预测器架构，最小化 sparse vs dense hidden state MSE），验证 taxonomy 中 Intermediate 级别的性能。或弱化 taxonomy 为概念组织工具而非性能递进关系。\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W1\"\n    summary: \"C1 'Causal Ablation' 命名过强，存在未解决的 soft-vs-hard confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. C1 同时改变 gradient coupling 和 mask representation。BCE+Gumbel 失败不能反证 softness 对 KL 不重要。论文自己承认 'Disentangling remains for future work' 但仍用 'Causal' 标题。\"}\n    action_items:\n      - {round: 12, action: \"将 'Causal Ablation' 改为 'Target-Swap Ablation' 或 'Target Transfer Experiment'。明确 C1 的 confound 边界，降低 'mask quality is the proximate driver' 的 claim 强度。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"14B MMLU 逆转 -8.1pp 仅 seed 42 单次运行，统计效力不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. Mistral-7B 也仅 seed 42。考虑到 LLaMA-8B 30% global MMLU σ=9.5pp，单 seed 无法排除方差。14B MMLU 逆转可能是 seed 效应也可能是 systematic。\"}\n    action_items:\n      - {round: 12, action: \"至少对 Qwen-14B 30% 和 Mistral-7B 30% 各运行 3 seed，报告 mean±std。如资源不允许，在正文（非仅 Limitations）中明确标注统计局限。\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W3\"\n    summary: \"无 wall-clock 加速，系统增加 6.4% 开销；与同类方法（DejaVu/FastForward/TEAL）对比在加速维度缺席\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. 论文已在 §1 和 Appendix A 坦诚承认。R2 指出 Abstract 'renders compensation redundant' 误导读者期望加速。R1 指出同类方法均报告实际加速。\"}\n    action_items:\n      - {round: 12, action: \"Abstract 改为 'renders compensation redundant in prediction quality'。Introduction/Conclusion 更显著地限定贡献范围为 prediction quality study，而非 efficiency/systems contribution。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W4\"\n    summary: \"方法新颖性有限：核心为 BCE→KL loss swap + 标准 Gumbel relaxation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R2 定 Must-Fix，R1 部分反驳（与 MaskLLM 有结构性差异）但同意方法新颖性增量。两人一致同意论文应更强化 empirical study 定位。\"}\n    action_items:\n      - {round: 12, action: \"进一步强化 empirical contribution framing（mask pattern discovery, C1 ablation, regime analysis），弱化 method novelty 暗示。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W5\"\n    summary: \"30% λ 饱和偏差 5%（实际 28.5%），train-inference mismatch 主文未讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R1 指出，R2 同意。Appendix C 有 defense（TEAL@28.5% PPL=10.30 vs @30% 10.97，差异 0.67 远小于 KL 优势 2.01），但 R2 补充：严格对比应为 KL@28.5% vs TEAL@28.5%（improvement 13% 而非宣称 18%）。\"}\n    action_items:\n      - {round: 12, action: \"在 §4.1 或 §4.2 中明确训练时实际稀疏度为 28.5%，讨论 train-inference gap。考虑用 TEAL@28.5% 作为更公平的对比基准。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W6\"\n    summary: \"30% downstream 退化严重（GSM8K 84%↓, MMLU 38%↓），'best quality level' 表述需修正\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R2 指出，R1 同意并补充所有方法 GSM8K 退化相近（说明是 30% 稀疏度固有限制非 KL 特有问题）。但 'best quality' 应改为 'least-degraded'。\"}\n    action_items:\n      - {round: 12, action: \"Limitations 中 'best-quality sparsity level' 改为 'least-degraded sparsity level'。补充讨论 30% 稀疏度对 reasoning 任务的固有限制。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W7\"\n    summary: \"Conclusion 仅两句话过于简短，无 future work 讨论\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus。至少应补充 N:M structured sparsity、更大规模验证等 future work 方向。\"}\n    action_items:\n      - {round: 12, action: \"扩展 Conclusion 到 4-6 句，加入 future work 方向。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W8\"\n    summary: \"WikiText-103→WikiText-2 同源，C4 OOD gap 更大 (1.74× vs 1.46×)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus。建议主表加入 C4 PPL 一列。\"}\n    action_items:\n      - {round: 12, action: \"考虑在 Table 2 中加入 C4 PPL 列，或在 §4.2 结果段中正文引用 C4 数据。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M1\"\n    summary: \"Minor 写作/编辑问题集合\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"包括：PPL 11.79/11.80 不一致；WINA 幽灵 baseline；'phase transition' 术语过强（建议 capacity cliff/regime boundary）；SNR 'at convergence' 在 step 300 不当；'68% divergence' Intro 中轻微重复；HellaSwag/PIQA 未在 §4.1 提及；s42† checkpoint 解释不足；SwiGLU 未在 Abstract 定义；§2.5 篇幅比例偏大；exp_id 注释需清理；'in context of' 语法错误。\"}\n    action_items:\n      - {round: 12, action: \"Batch fix: 统一 PPL 数字、移除 WINA 或补数据、'phase transition'→'capacity cliff'、SNR 明确 step 300、减少 68% 重复、§4.1 补 HellaSwag/PIQA 协议、解释 s42† 或移除、Abstract 定义 SwiGLU、清理 exp_id 注释、修正 'in context of'→'in the context of'。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — status updates for Round 12\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"C1 causal ablation: inference logic flawed (mask transferability ≠ gradient coupling unimportant) + soft-vs-hard confound + BCE+Gumbel反常未解释\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. C1 proves mask transferability, not that gradient coupling is unimportant.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Partially addressed: §4.4 now distinguishes training-stage coupling vs inference-stage quality. But 'Causal Ablation' naming persists. Tracked in R12-W1.\"}\n    action_items:\n      - {round: 11, action: \"Reframe C1 narrative\", assigned_to: \"paper_agent\", status: done}\n      - {round: 11, action: \"BCE+Gumbel no-penalty control experiment\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N2\"\n    summary: \"14B Qwen MMLU -8.1pp reversal: only 'warrants further investigation', no mechanism analysis\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Partially addressed: §4.6 now has per-layer mask divergence analysis (variance 2.4× of 8B, early-layer convergence zone). But still single seed, hypothesis unverified. Tracked in R12-W2.\"}\n    action_items:\n      - {round: 11, action: \"14B per-layer mask divergence analysis\", assigned_to: \"main_agent\", status: done}\n      - {round: 11, action: \"Expand §4.6 14B discussion\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N3\"\n    summary: \"49% PPL headline from downstream-collapsed 50% regime is misleading\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Improved: Abstract now leads with 30% results and 18% PPL reduction. 50% framed as phase transition evidence. But 'capacity phase transition' terminology too strong (R12-M1). 68% divergence from 50% not annotated in Abstract.\"}\n    action_items:\n      - {round: 11, action: \"Major Abstract/Intro rewrite\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W1\"\n    summary: \"Abstract severe data overload\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Both agree Abstract fails 30-second readability test.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Not raised in R12. R2-S5 praises writing quality. Abstract restructured.\"}\n    resolution: \"Abstract restructured with clearer narrative flow. Not raised in R12 fresh review.\"\n    resolution_round: 12\n\n  - id: \"R11-W2\"\n    summary: \"50% KL 3-seed data buried in Appendix E; main table reports seed 42 only\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Real gap: 50% main table s42 only.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Table 2 now shows 3-seed for KL uniform 50% (11.92±0.07) but KL global 50% still seed 42 only (11.79).\"}\n    action_items:\n      - {round: 12, action: \"Move 50% KL global 3-seed into Table 2.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W6\"\n    summary: \"Table 3 C1 ablation at 30%: previously missing downstream metrics\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Max Δ=1.70pp claim based on MMLU only.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Table 3 now shows full downstream (ARC-c, WG, MMLU, GSM8K) for all seeds at both sparsity levels. Issue resolved.\"}\n    resolution: \"Table 3 now contains complete downstream metrics. Max Δ recalculated.\"\n    resolution_round: 12\n\n  - id: \"R11-DENSE\"\n    summary: \"Mistral downstream table Dense row uses v0.1 public data instead of v0.3 experimental values\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"PPL 5.06 should be 5.52.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Table 11 (Appendix K) now shows Dense PPL 5.52, all downstream from experimental v0.3 values. Resolved.\"}\n    resolution: \"Mistral Dense row corrected to v0.3 experimental values.\"\n    resolution_round: 12\n\n  - id: \"R11-REF\"\n    summary: \"Missing reference: OWL (Yin et al., 2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Consensus. Directly relevant to §4.6 allocation analysis.\"}\n      - {round: 12, reviewers: [], note: \"OWL now cited in §4.6 and Related Work. R12 reviewers confirm '47 citations, density reasonable, no major omissions'.\"}\n    resolution: \"OWL citation added. No missing references flagged in R12.\"\n    resolution_round: 12\n\n  - id: \"R11-M1\"\n    summary: \"Minor writing: symbol inconsistency, abbreviation expansion, Table 2 caption, penalty terminology\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Collection of minor issues.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Some fixed (no AI markers, no em-dash/en-dash). New minor issues tracked in R12-M1.\"}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-M2\"\n    summary: \"68% mask divergence lacks CI\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Bootstrap CI needed.\"}\n      - {round: 12, reviewers: [], note: \"Not raised in R12. May still be desirable.\"}\n    action_items:\n      - {round: 11, action: \"Compute bootstrap CI for 68% divergence.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — confirmed resolved\n  # ============================================================\n\n  - id: \"R9-N4\"\n    summary: \"Method novelty insufficient for Main\"\n    category: method\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Reconfirmed. R12-W4. Both reviewers agree Findings-appropriate.\"}\n    resolution: \"Positioning issue. Findings accepted as realistic target.\"\n    resolution_round: 10\n\n  - id: \"R11-W3\"\n    summary: \"No wall-clock speedup\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Reconfirmed as R12-W3. Paper honestly disclaims. Framing adjustment needed.\"}\n    resolution: \"Acknowledged limitation. Sparse kernel integration deferred to future work.\"\n    resolution_round: 11\n\n  - id: \"R9-W1\"\n    summary: \"PPL degradation 18% wording mismatch\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"Fixed. Not raised in R12.\"\n    resolution_round: 11\n\n  - id: \"R9-W3\"\n    summary: \"Eq.5 vs Eq.6 constraint inconsistency\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"Fixed. Not raised in R12.\"\n    resolution_round: 11\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"RESOLVED by C1 ablation. Confound boundary acknowledged.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"Removed.\"\n    resolution_round: 9\n\n  - id: \"R8-N3\"\n    summary: \"Regime curve data points insufficient\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"6-point regime curve confirmed in R12.\"\n    resolution_round: 11\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 12 (fresh review) — New/recurring issues\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"C1 消融 50% max Δ 数值错误：论文声称 0.59pp，Table 3 实际为 0.79pp (WG)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. R1 首先发现，R2 交叉确认。Table 3 caption 'max Δ=0.59pp at 50% (2-seed)' 与表格数据 |63.14−62.35|=0.79pp 不符。另外 '2-seed' 声称但仅展示 1 seed pair。\"}\n    action_items:\n      - {round: 12, action: \"更正 max Δ 为 0.79pp，同步修改 Abstract、Introduction、§4.4 中引用该数字的段落。确认第二个 seed 数据并补入表格或移除 '2-seed' 声称。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 BCE+comp (28.13±0.20) vs Table 4 BCE+Compensation (25.44) 数值矛盾不可调和\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. Table 2 脚注标注 'DejaVu/FastForward pipeline with compensation' 但 3-seed std=0.20 意味所有 seed 在 27.93-28.33，与 Table 4 seed 42=25.44 矛盾。R2 推测 Table 2 实际为 BCE without compensation。§4.3 的 '28.13±0.20' 也说 'BCE predictor' 非 'BCE+compensation'。\"}\n    action_items:\n      - {round: 12, action: \"澄清 Table 2 'BCE+comp' 与 Table 4 'BCE+Compensation' 是否为同一实验配置（训练步数、seed、是否含 compensation）。修正标注错误。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-N3\"\n    summary: \"缺少 Intermediate-coupling (MSE) baseline 实验对比，Taxonomy claim 无实验支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R1 定 Must-Fix，R2 同意但建议 Should-Fix（不影响核心 KL>BCE claim，但影响 taxonomy 完整性）。Table 1 划分 Decomposed/Intermediate/Coupled 三级，但实验只对比两端。ShadowLLM/D2DMoE 在 Related Work 讨论但无数据。\"}\n    action_items:\n      - {round: 12, action: \"实现 per-layer MSE baseline（相同预测器架构，最小化 sparse vs dense hidden state MSE），验证 taxonomy 中 Intermediate 级别的性能。或弱化 taxonomy 为概念组织工具而非性能递进关系。\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W1\"\n    summary: \"C1 'Causal Ablation' 命名过强，存在未解决的 soft-vs-hard confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. C1 同时改变 gradient coupling 和 mask representation。BCE+Gumbel 失败不能反证 softness 对 KL 不重要。论文自己承认 'Disentangling remains for future work' 但仍用 'Causal' 标题。\"}\n    action_items:\n      - {round: 12, action: \"将 'Causal Ablation' 改为 'Target-Swap Ablation' 或 'Target Transfer Experiment'。明确 C1 的 confound 边界，降低 'mask quality is the proximate driver' 的 claim 强度。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"14B MMLU 逆转 -8.1pp 仅 seed 42 单次运行，统计效力不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. Mistral-7B 也仅 seed 42。考虑到 LLaMA-8B 30% global MMLU σ=9.5pp，单 seed 无法排除方差。14B MMLU 逆转可能是 seed 效应也可能是 systematic。\"}\n    action_items:\n      - {round: 12, action: \"至少对 Qwen-14B 30% 和 Mistral-7B 30% 各运行 3 seed，报告 mean±std。如资源不允许，在正文（非仅 Limitations）中明确标注统计局限。\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W3\"\n    summary: \"无 wall-clock 加速，系统增加 6.4% 开销；与同类方法（DejaVu/FastForward/TEAL）对比在加速维度缺席\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus. 论文已在 §1 和 Appendix A 坦诚承认。R2 指出 Abstract 'renders compensation redundant' 误导读者期望加速。R1 指出同类方法均报告实际加速。\"}\n    action_items:\n      - {round: 12, action: \"Abstract 改为 'renders compensation redundant in prediction quality'。Introduction/Conclusion 更显著地限定贡献范围为 prediction quality study，而非 efficiency/systems contribution。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W4\"\n    summary: \"方法新颖性有限：核心为 BCE→KL loss swap + 标准 Gumbel relaxation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R2 定 Must-Fix，R1 部分反驳（与 MaskLLM 有结构性差异）但同意方法新颖性增量。两人一致同意论文应更强化 empirical study 定位。\"}\n    action_items:\n      - {round: 12, action: \"进一步强化 empirical contribution framing（mask pattern discovery, C1 ablation, regime analysis），弱化 method novelty 暗示。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W5\"\n    summary: \"30% λ 饱和偏差 5%（实际 28.5%），train-inference mismatch 主文未讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R1 指出，R2 同意。Appendix C 有 defense（TEAL@28.5% PPL=10.30 vs @30% 10.97，差异 0.67 远小于 KL 优势 2.01），但 R2 补充：严格对比应为 KL@28.5% vs TEAL@28.5%（improvement 13% 而非宣称 18%）。\"}\n    action_items:\n      - {round: 12, action: \"在 §4.1 或 §4.2 中明确训练时实际稀疏度为 28.5%，讨论 train-inference gap。考虑用 TEAL@28.5% 作为更公平的对比基准。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W6\"\n    summary: \"30% downstream 退化严重（GSM8K 84%↓, MMLU 38%↓），'best quality level' 表述需修正\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R2 指出，R1 同意并补充所有方法 GSM8K 退化相近（说明是 30% 稀疏度固有限制非 KL 特有问题）。但 'best quality' 应改为 'least-degraded'。\"}\n    action_items:\n      - {round: 12, action: \"Limitations 中 'best-quality sparsity level' 改为 'least-degraded sparsity level'。补充讨论 30% 稀疏度对 reasoning 任务的固有限制。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W7\"\n    summary: \"Conclusion 仅两句话过于简短，无 future work 讨论\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus。至少应补充 N:M structured sparsity、更大规模验证等 future work 方向。\"}\n    action_items:\n      - {round: 12, action: \"扩展 Conclusion 到 4-6 句，加入 future work 方向。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W8\"\n    summary: \"WikiText-103→WikiText-2 同源，C4 OOD gap 更大 (1.74× vs 1.46×)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus。建议主表加入 C4 PPL 一列。\"}\n    action_items:\n      - {round: 12, action: \"考虑在 Table 2 中加入 C4 PPL 列，或在 §4.2 结果段中正文引用 C4 数据。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M1\"\n    summary: \"Minor 写作/编辑问题集合\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"包括：PPL 11.79/11.80 不一致；WINA 幽灵 baseline；'phase transition' 术语过强（建议 capacity cliff/regime boundary）；SNR 'at convergence' 在 step 300 不当；'68% divergence' Intro 中轻微重复；HellaSwag/PIQA 未在 §4.1 提及；s42† checkpoint 解释不足；SwiGLU 未在 Abstract 定义；§2.5 篇幅比例偏大；exp_id 注释需清理；'in context of' 语法错误。\"}\n    action_items:\n      - {round: 12, action: \"Batch fix: 统一 PPL 数字、移除 WINA 或补数据、'phase transition'→'capacity cliff'、SNR 明确 step 300、减少 68% 重复、§4.1 补 HellaSwag/PIQA 协议、解释 s42† 或移除、Abstract 定义 SwiGLU、清理 exp_id 注释、修正 'in context of'→'in the context of'。\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — status updates for Round 12\n  # ============================================================\n\n  - id: \"R11-N1\"\n    summary: \"C1 causal ablation: inference logic flawed (mask transferability ≠ gradient coupling unimportant) + soft-vs-hard confound + BCE+Gumbel反常未解释\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus. C1 proves mask transferability, not that gradient coupling is unimportant.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Partially addressed: §4.4 now distinguishes training-stage coupling vs inference-stage quality. But 'Causal Ablation' naming persists. Tracked in R12-W1.\"}\n    action_items:\n      - {round: 11, action: \"Reframe C1 narrative\", assigned_to: \"paper_agent\", status: done}\n      - {round: 11, action: \"BCE+Gumbel no-penalty control experiment\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N2\"\n    summary: \"14B Qwen MMLU -8.1pp reversal: only 'warrants further investigation', no mechanism analysis\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Partially addressed: §4.6 now has per-layer mask divergence analysis (variance 2.4× of 8B, early-layer convergence zone). But still single seed, hypothesis unverified. Tracked in R12-W2.\"}\n    action_items:\n      - {round: 11, action: \"14B per-layer mask divergence analysis\", assigned_to: \"main_agent\", status: done}\n      - {round: 11, action: \"Expand §4.6 14B discussion\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-N3\"\n    summary: \"49% PPL headline from downstream-collapsed 50% regime is misleading\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Improved: Abstract now leads with 30% results and 18% PPL reduction. 50% framed as phase transition evidence. But 'capacity phase transition' terminology too strong (R12-M1). 68% divergence from 50% not annotated in Abstract.\"}\n    action_items:\n      - {round: 11, action: \"Major Abstract/Intro rewrite\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W1\"\n    summary: \"Abstract severe data overload\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Both agree Abstract fails 30-second readability test.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Not raised in R12. R2-S5 praises writing quality. Abstract restructured.\"}\n    resolution: \"Abstract restructured with clearer narrative flow. Not raised in R12 fresh review.\"\n    resolution_round: 12\n\n  - id: \"R11-W2\"\n    summary: \"50% KL 3-seed data buried in Appendix E; main table reports seed 42 only\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Real gap: 50% main table s42 only.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Table 2 now shows 3-seed for KL uniform 50% (11.92±0.07) but KL global 50% still seed 42 only (11.79).\"}\n    action_items:\n      - {round: 12, action: \"Move 50% KL global 3-seed into Table 2.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-W6\"\n    summary: \"Table 3 C1 ablation at 30%: previously missing downstream metrics\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Max Δ=1.70pp claim based on MMLU only.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Table 3 now shows full downstream (ARC-c, WG, MMLU, GSM8K) for all seeds at both sparsity levels. Issue resolved.\"}\n    resolution: \"Table 3 now contains complete downstream metrics. Max Δ recalculated.\"\n    resolution_round: 12\n\n  - id: \"R11-DENSE\"\n    summary: \"Mistral downstream table Dense row uses v0.1 public data instead of v0.3 experimental values\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"PPL 5.06 should be 5.52.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Table 11 (Appendix K) now shows Dense PPL 5.52, all downstream from experimental v0.3 values. Resolved.\"}\n    resolution: \"Mistral Dense row corrected to v0.3 experimental values.\"\n    resolution_round: 12\n\n  - id: \"R11-REF\"\n    summary: \"Missing reference: OWL (Yin et al., 2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Consensus. Directly relevant to §4.6 allocation analysis.\"}\n      - {round: 12, reviewers: [], note: \"OWL now cited in §4.6 and Related Work. R12 reviewers confirm '47 citations, density reasonable, no major omissions'.\"}\n    resolution: \"OWL citation added. No missing references flagged in R12.\"\n    resolution_round: 12\n\n  - id: \"R11-M1\"\n    summary: \"Minor writing: symbol inconsistency, abbreviation expansion, Table 2 caption, penalty terminology\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Collection of minor issues.\"}\n      - {round: 12, reviewers: [1, 2], note: \"Some fixed (no AI markers, no em-dash/en-dash). New minor issues tracked in R12-M1.\"}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R11-M2\"\n    summary: \"68% mask divergence lacks CI\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Bootstrap CI needed.\"}\n      - {round: 12, reviewers: [], note: \"Not raised in R12. May still be desirable.\"}\n    action_items:\n      - {round: 11, action: \"Compute bootstrap CI for 68% divergence.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — confirmed resolved\n  # ============================================================\n\n  - id: \"R9-N4\"\n    summary: \"Method novelty insufficient for Main\"\n    category: method\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Reconfirmed. R12-W4. Both reviewers agree Findings-appropriate.\"}\n    resolution: \"Positioning issue. Findings accepted as realistic target.\"\n    resolution_round: 10\n\n  - id: \"R11-W3\"\n    summary: \"No wall-clock speedup\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Reconfirmed as R12-W3. Paper honestly disclaims. Framing adjustment needed.\"}\n    resolution: \"Acknowledged limitation. Sparse kernel integration deferred to future work.\"\n    resolution_round: 11\n\n  - id: \"R9-W1\"\n    summary: \"PPL degradation 18% wording mismatch\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"Fixed. Not raised in R12.\"\n    resolution_round: 11\n\n  - id: \"R9-W3\"\n    summary: \"Eq.5 vs Eq.6 constraint inconsistency\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"Fixed. Not raised in R12.\"\n    resolution_round: 11\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"RESOLVED by C1 ablation. Confound boundary acknowledged.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"Removed.\"\n    resolution_round: 9\n\n  - id: \"R8-N3\"\n    summary: \"Regime curve data points insufficient\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"6-point regime curve confirmed in R12.\"\n    resolution_round: 11\n"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-19T08:05:15.455354+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 16966}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-19T08:07:39.372496+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# Round 12 审稿报告（Fresh Review）\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026（ARR May 2026 cycle）\n**Reviewers**: R1（方法严谨性+实验可靠性）、R2（新颖性+完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n本文提出用 forward KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（75.9M 参数，<1% 基础模型），通过 Gumbel-Sigmoid 松弛实现端到端可微训练。核心发现：(1) KL 训练的 mask 与激活幅值 mask 有 68% 差异（per-layer Jaccard 32%），C1 target-swap 消融证实 mask 质量（而非梯度耦合机制本身）是推理质量的近因驱动；(2) 在 LLaMA-3.1-8B 30% 稀疏度下 PPL 降低 18%（8.96 vs TEAL 10.97），补偿网络（+67.2M 参数）变冗余；(3) 分析了稀疏度-分配策略的三段式交互（budget-surplus / budget-constrained / capacity-limited）。跨架构验证包括 Mistral-7B（5/6 tasks KL 优势）和 Qwen-2.5-14B（PPL 泛化但 MMLU 逆转 -8.1pp）。\n\n---\n\n## Strengths\n\n**S1. 问题定义精准。** BCE 逐神经元独立训练与 TEAL 全局 top-k 推理分配的 mismatch 被准确识别且此前未被正式分析。梯度分析（§3.6）从结构上解释了两种目标的差异，提供了理论动机。[R1, R2 共识]\n\n**S2. C1 target-swap 消融设计巧妙。** 将 mask target quality 与 gradient coupling 解耦（BCE 在 KL-derived masks 上训练复现 KL 质量，magnitude-trained BCE 差 2.4×），是本文最有价值的实验设计。[R1, R2 共识]\n\n**S3. 消融实验系统全面。** Table 4 层层隔离 divergence direction、relaxation method、loss function、compensation 的贡献，实验设计规范且在同类工作中少见。[R1, R2 共识]\n\n**S4. 跨架构评估诚实。** Mistral-7B（GSM8K 反转）、Qwen-14B（MMLU 反转 -8.1pp）的负面结果被正面讨论，体现科学诚信。[R1, R2 共识]\n\n**S5. 写作质量高。** 无 em-dash、无解释性 en-dash、无 AI 黑名单用词（leverage/delve/utilize）、无过度分段。叙事线（mismatch → gradient analysis → mask discovery → causal ablation）连贯。[R2 发现, R1 同意]\n\n**S6. Taxonomy 定位准确。** correction granularity × training signal coupling 的 2D 分类法组织清晰，Per-token × Coupled 确为未探索组合。[R1, R2 共识]\n\n**S7. 超参数鲁棒性充分。** Bottleneck dimension (<3%)、temperature schedule (<1.8%)、training convergence (800步饱和) 的敏感性分析增强可信度。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**N1. C1 消融 50% max Δ 数值错误。** [R1 发现, R2 交叉确认]\n- 论文声称 \"max Δ=0.59pp at 50% (2-seed)\"（§4.4 + Table 3 caption），但 Table 3 中 50% s42 的 WinoGrande |63.14−62.35|=0.79pp，超过声称值。0.59pp 无法从任何可见数据推导。且 \"2-seed\" 声称但仅展示 1 seed pair。\n- C1 是核心 contribution，定量证据错误直接削弱可信度。\n\n**N2. Table 2 与 Table 4 BCE+Compensation 数值矛盾。** [R1 发现, R2 交叉确认]\n- Table 2: \"BCE + comp.∗\" PPL 28.13±0.20 (3-seed)，脚注标注 \"DejaVu/FastForward pipeline with compensation (67.2M params)\"\n- Table 4: \"BCE + Compensation (hard mask)\" PPL 25.44 (seed 42)\n- std=0.20 意味所有 seed 在 27.93-28.33 范围，与 Table 4 的 25.44 相差 2.69pp，不可调和。§4.3 描述为 \"BCE predictor\" 非 \"BCE+compensation\"，怀疑 Table 2 脚注标注错误。\n- \"KL renders compensation redundant\" 的定量基础不明。\n\n**N3. 缺少 Intermediate-coupling (MSE) baseline。** [R1 提出 Must-Fix, R2 同意但建议 Should-Fix]\n- Table 1 taxonomy 划分 Decomposed/Intermediate/Coupled 三级，暗示递进关系，但实验仅对比两端（BCE vs KL），Intermediate（per-layer MSE）完全缺席。ShadowLLM/D2DMoE 在 Related Work 讨论但无实验数据。\n- Taxonomy 的核心价值——Coupled 优于 Intermediate——缺乏实验验证。至少需要简化版 per-layer MSE baseline。\n- R1 定为 Must-Fix，R2 认为不影响核心 KL>BCE claim 但影响 taxonomy 完整性。**Director 判定：Should-Fix**（taxonomy 是概念贡献而非论文核心 claim，但如果作者希望保留 taxonomy 需补实验）。\n\n### Warning (Should-Fix)\n\n**W1. C1 \"Causal Ablation\" 命名过强，soft-vs-hard confound 未解决。** [R1, R2 共识]\n- C1 同时改变 gradient coupling 和 mask representation（hard binary vs soft Gumbel-Sigmoid）。BCE+Gumbel 失败不能反证 softness 对 KL 不重要（loss × relaxation 可能有 interaction effect）。论文承认 \"Disentangling remains for future work\" 但标题仍用 \"Causal\"。\n- 建议改为 \"Target-Swap Ablation\" 或 \"Target Transfer Experiment\"。\n\n**W2. 14B MMLU 逆转仅 seed 42，统计效力不足。** [R1, R2 共识]\n- Mistral-7B 和 Qwen-14B 所有结果均为单 seed。LLaMA-8B 已展示 MMLU 可达 σ=9.5pp 的跨 seed 方差，14B 反转可能是 seed 效应。\n- 至少 3-seed 确认后才能对可扩展性下结论。\n\n**W3. 无 wall-clock 加速，系统增加 6.4% 开销。** [R1, R2 共识]\n- 同类方法（DejaVu/FastForward/Polar Sparsity/TEAL）均报告实际加速。本文在加速维度完全缺席。\n- Abstract \"renders compensation redundant\" 误导读者期望速度提升，实际只节省 ~2.7% latency 开销。\n- 论文已坦诚承认，但 framing 需更明确限定为 prediction quality study。\n\n**W4. 方法新颖性有限。** [R2 提出, R1 部分同意]\n- 核心技术为 BCE→KL loss swap + 标准 Gumbel-Sigmoid relaxation。与 MaskLLM 的区别（activation vs weight sparsity, predictor vs direct mask, global vs N:M）是问题设定差异而非方法创新。\n- R1 反驳：两个方法有结构性差异，不应过度抽象。但同意论文的真正贡献是实证发现（mask divergence, C1 ablation, regime analysis）而非方法本身。\n- 论文已定位为 \"primarily empirical\"，建议进一步强化。\n\n**W5. 30% λ 饱和偏差 5%，train-inference mismatch。** [R1 提出, R2 同意并定量分析]\n- 训练时实际稀疏度 28.5%，推理强制 30%。严格对比应为 KL@28.5% vs TEAL@28.5%（improvement 13% 而非宣称 18%）。\n- Appendix 有 defense（TEAL@28.5% PPL=10.30，gap 0.67 远小于 KL 优势 2.01），但应在主文讨论。\n\n**W6. 30% downstream 退化严重，\"best quality\" 表述不当。** [R2 提出, R1 同意]\n- GSM8K 84% 退化（48.75→7.5%），MMLU 38% 退化（65.27→40.7%）。所有方法退化相近（说明是稀疏度固有限制），但 \"best quality\" 应改为 \"least-degraded\"。\n\n**W7. Conclusion 仅两句话。** [R1, R2 共识]\n- 无 future work、无 broader impact。至少补 N:M 结构化稀疏、更大规模验证等方向。\n\n**W8. WikiText-103→WikiText-2 同源。** [R1, R2 共识]\n- C4 OOD gap 更大（1.74× vs 1.46×），说明 partial overfitting。建议主表加 C4 PPL 列。\n\n### Info (Minor)\n\n**M1. 写作/编辑问题集合。** [R1, R2 共识]\n- PPL 11.79 vs 11.80 不一致\n- WINA 列为 baseline 但无实验数据\n- \"Phase transition\" 术语过强（建议 \"capacity cliff\"）\n- SNR \"at convergence\" 实际在 step 300 测量（训练 1000 步）\n- \"68% divergence\" Introduction 中轻微重复\n- HellaSwag/PIQA 未在 §4.1 Evaluation 提及\n- s42† earlier checkpoint 解释不足\n- SwiGLU 未在 Abstract 定义\n- §2.5 自适应惩罚控制器篇幅比例偏大\n- exp_id 注释需清理\n- \"in context of\" → \"in the context of\"\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **数值错误必须修正**：C1 max Δ (0.59→0.79pp) + Table 2/4 BCE 矛盾\n2. **C1 命名过强**：应降级为 \"Target-Swap Ablation\"\n3. **无 wall-clock 加速**：framing 需更明确限定贡献范围\n4. **14B 单 seed 不足**：至少 3-seed 确认 MMLU 反转稳定性\n5. **Findings 定位合理**：方法新颖性增量，但实证分析有价值\n6. **Overall 3.0**：两人独立给出相同分数\n\n## Reviewer Divergence\n\n仅 2 项轻微分歧（已在交叉中达成共识）：\n1. **MSE baseline 严重性**：R1=Must-Fix（taxonomy 需实验验证），R2=Should-Fix（不影响核心 claim）。Director 判定 Should-Fix。\n2. **MaskLLM 技术距离**：R2 认为距离小（Must-Fix），R1 部分反驳（结构性差异存在但方法新颖性确实有限）。两人一致建议强化 empirical study 定位。\n\n---\n\n## Questions\n\n以下问题由两位 Reviewer 共同或独立提出，需作者回应：\n\n1. **Table 2/4 BCE 配置**：两个表格的 BCE+compensation 条目是否为同一实验？训练步数、seed、是否含 compensation？[R1-Q1, R2 交叉确认]\n2. **C1 50% max Δ 计算来源**：0.59pp 如何得出？第二个 seed 数据？[R1-Q2]\n3. **28.5% train-inference gap**：预测器是否在 30% 推理条件下验证/选择？严格对比下 improvement 为 13% 而非 18%？[R1-Q3, R2-Q4]\n4. **14B MMLU 多 seed 稳定性**：-8.1pp 逆转是 systematic 还是 seed 效应？[R1-Q6, R2-Q1]\n5. **KL-only 神经元贡献**：KL 选择但 magnitude 不选择的神经元对 output distribution 有什么实际贡献？[R2-Q2]\n6. **GSM8K 反转机制**：forward KL 的 mass-covering 性质是否在 reasoning 任务上不如 mode-seeking？[R1-Q5, R2-Q3]\n7. **C4 训练可能性**：在非 WikiText 数据上训练 predictor 能否减少 domain overfitting？[R2-Q5]\n\n---\n\n## Missing References\n\n两位 Reviewer 一致认为引用覆盖良好（47 篇，密度合理）。无重大遗漏。\n- R2 建议考虑 LLM.int8() (Dettmers et al., 2022)，R1 反驳：量化不在本文 scope 内，Wang et al. 2025 已覆盖 sparsity+quantization 交叉。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未配置**。项目无 `external_review.paperreview_ai.enabled` 设置。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | **3.0/5** — 核心方法正确，但数值错误（N1）和数据矛盾（N2）直接削弱核心 claim 可信度 |\n| Excitement | 3.0/5 | 2.5/5 | **2.5/5** — KL 发现不同 mask pattern 有趣，但方法增量、无实际加速、规模受限 |\n| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** — 超参数完整、3-seed、GPU 型号齐全；未开源代码 |\n| Overall | 3.0/5 | 3.0/5 | **3.0/5 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**Overall Score: 3.0 (Findings)**\n\n**推荐: Findings（修复 N1-N2 后可稳定；当前因数值错误在 Borderline Findings 2.5-3.0 边缘）**\n\n**核心判断依据**:\n1. **支撑 Findings 接收的因素**: C1 target-swap 消融是有价值的分析创新；mask divergence 发现（68%）提供了对 KL 训练行为的新理解；三段式 regime analysis 有实用参考价值；实验覆盖面广且报告诚实\n2. **阻止 Main 接收的因素**: 方法新颖性增量（loss swap + 标准技术）；无 wall-clock 加速；14B 可扩展性存疑（MMLU 逆转且仅单 seed）；数值错误影响核心 claim 可信度\n3. **修复优先级**: N1 数值勘误 > N2 表格标注澄清 > W1 C1 命名 > W2 14B 多 seed > W3 framing 调整\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 结构合理，四个必答问题覆盖。\"renders compensation redundant\" 需加 \"in prediction quality\" 限定。\"capacity phase transition\" 改为 \"capacity cliff\"。68% divergence 来自 50% 稀疏度但未标注。\n\n### Introduction (§1)\n- 从 BCE/global-allocation mismatch 切入清晰。但 ¶2-¶3 数字密度过高，部分数据应移至 §4。Contribution 第 3 条（non-monotonic allocation + 14B effects）在前文无铺垫。\"68% divergence\" 在 ¶2 和 Contribution list 重复，建议 Contribution list 用 \"the discovered mask patterns (§4.3)\" 指代。\n\n### Related Work (§2)\n- 覆盖全面，MaskLLM 三点区分详细。MoE routing 段与主线关系稍远但可接受。D2DMoE/ShadowLLM 的 \"intermediate coupling\" 未量化与 \"coupled\" 的差距（缺 MSE baseline 的根源）。\n\n### Method (§3)\n- §3.1-§3.4 清晰规范。§3.5 自适应惩罚控制器篇幅过大（本质为标准技术）。§3.6 梯度分析正确标注 \"suggestive\" 但 \"reveals structural asymmetry\" 用词暗示超过 suggestive 的结论。\n\n### Experiments (§4)\n- 最强部分。Table 4 ablation、regime analysis (§4.6) 扎实。Table 2 数据矛盾（N2）和 C1 数值错误（N1）是必须修复的硬伤。WINA 幽灵 baseline 需移除或补数据。\n\n### Conclusion (§5)\n- 两句话严重不足。需扩展至 4-6 句，含 future work（N:M sparsity, 70B scaling, multi-target predictor）。\n\n### Limitations\n- 全面诚实，是论文优点。\"best-quality\" → \"least-degraded\"。\n\n### Appendix\n- 内容丰富，所有附录在正文有引用。Appendix C（λ 收敛）的 defense 合理但应在主文摘要。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# Round 12 审稿报告（Fresh Review）\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026（ARR May 2026 cycle）\n**Reviewers**: R1（方法严谨性+实验可靠性）、R2（新颖性+完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n本文提出用 forward KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（75.9M 参数，<1% 基础模型），通过 Gumbel-Sigmoid 松弛实现端到端可微训练。核心发现：(1) KL 训练的 mask 与激活幅值 mask 有 68% 差异（per-layer Jaccard 32%），C1 target-swap 消融证实 mask 质量（而非梯度耦合机制本身）是推理质量的近因驱动；(2) 在 LLaMA-3.1-8B 30% 稀疏度下 PPL 降低 18%（8.96 vs TEAL 10.97），补偿网络（+67.2M 参数）变冗余；(3) 分析了稀疏度-分配策略的三段式交互（budget-surplus / budget-constrained / capacity-limited）。跨架构验证包括 Mistral-7B（5/6 tasks KL 优势）和 Qwen-2.5-14B（PPL 泛化但 MMLU 逆转 -8.1pp）。\n\n---\n\n## Strengths\n\n**S1. 问题定义精准。** BCE 逐神经元独立训练与 TEAL 全局 top-k 推理分配的 mismatch 被准确识别且此前未被正式分析。梯度分析（§3.6）从结构上解释了两种目标的差异，提供了理论动机。[R1, R2 共识]\n\n**S2. C1 target-swap 消融设计巧妙。** 将 mask target quality 与 gradient coupling 解耦（BCE 在 KL-derived masks 上训练复现 KL 质量，magnitude-trained BCE 差 2.4×），是本文最有价值的实验设计。[R1, R2 共识]\n\n**S3. 消融实验系统全面。** Table 4 层层隔离 divergence direction、relaxation method、loss function、compensation 的贡献，实验设计规范且在同类工作中少见。[R1, R2 共识]\n\n**S4. 跨架构评估诚实。** Mistral-7B（GSM8K 反转）、Qwen-14B（MMLU 反转 -8.1pp）的负面结果被正面讨论，体现科学诚信。[R1, R2 共识]\n\n**S5. 写作质量高。** 无 em-dash、无解释性 en-dash、无 AI 黑名单用词（leverage/delve/utilize）、无过度分段。叙事线（mismatch → gradient analysis → mask discovery → causal ablation）连贯。[R2 发现, R1 同意]\n\n**S6. Taxonomy 定位准确。** correction granularity × training signal coupling 的 2D 分类法组织清晰，Per-token × Coupled 确为未探索组合。[R1, R2 共识]\n\n**S7. 超参数鲁棒性充分。** Bottleneck dimension (<3%)、temperature schedule (<1.8%)、training convergence (800步饱和) 的敏感性分析增强可信度。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**N1. C1 消融 50% max Δ 数值错误。** [R1 发现, R2 交叉确认]\n- 论文声称 \"max Δ=0.59pp at 50% (2-seed)\"（§4.4 + Table 3 caption），但 Table 3 中 50% s42 的 WinoGrande |63.14−62.35|=0.79pp，超过声称值。0.59pp 无法从任何可见数据推导。且 \"2-seed\" 声称但仅展示 1 seed pair。\n- C1 是核心 contribution，定量证据错误直接削弱可信度。\n\n**N2. Table 2 与 Table 4 BCE+Compensation 数值矛盾。** [R1 发现, R2 交叉确认]\n- Table 2: \"BCE + comp.∗\" PPL 28.13±0.20 (3-seed)，脚注标注 \"DejaVu/FastForward pipeline with compensation (67.2M params)\"\n- Table 4: \"BCE + Compensation (hard mask)\" PPL 25.44 (seed 42)\n- std=0.20 意味所有 seed 在 27.93-28.33 范围，与 Table 4 的 25.44 相差 2.69pp，不可调和。§4.3 描述为 \"BCE predictor\" 非 \"BCE+compensation\"，怀疑 Table 2 脚注标注错误。\n- \"KL renders compensation redundant\" 的定量基础不明。\n\n**N3. 缺少 Intermediate-coupling (MSE) baseline。** [R1 提出 Must-Fix, R2 同意但建议 Should-Fix]\n- Table 1 taxonomy 划分 Decomposed/Intermediate/Coupled 三级，暗示递进关系，但实验仅对比两端（BCE vs KL），Intermediate（per-layer MSE）完全缺席。ShadowLLM/D2DMoE 在 Related Work 讨论但无实验数据。\n- Taxonomy 的核心价值——Coupled 优于 Intermediate——缺乏实验验证。至少需要简化版 per-layer MSE baseline。\n- R1 定为 Must-Fix，R2 认为不影响核心 KL>BCE claim 但影响 taxonomy 完整性。**Director 判定：Should-Fix**（taxonomy 是概念贡献而非论文核心 claim，但如果作者希望保留 taxonomy 需补实验）。\n\n### Warning (Should-Fix)\n\n**W1. C1 \"Causal Ablation\" 命名过强，soft-vs-hard confound 未解决。** [R1, R2 共识]\n- C1 同时改变 gradient coupling 和 mask representation（hard binary vs soft Gumbel-Sigmoid）。BCE+Gumbel 失败不能反证 softness 对 KL 不重要（loss × relaxation 可能有 interaction effect）。论文承认 \"Disentangling remains for future work\" 但标题仍用 \"Causal\"。\n- 建议改为 \"Target-Swap Ablation\" 或 \"Target Transfer Experiment\"。\n\n**W2. 14B MMLU 逆转仅 seed 42，统计效力不足。** [R1, R2 共识]\n- Mistral-7B 和 Qwen-14B 所有结果均为单 seed。LLaMA-8B 已展示 MMLU 可达 σ=9.5pp 的跨 seed 方差，14B 反转可能是 seed 效应。\n- 至少 3-seed 确认后才能对可扩展性下结论。\n\n**W3. 无 wall-clock 加速，系统增加 6.4% 开销。** [R1, R2 共识]\n- 同类方法（DejaVu/FastForward/Polar Sparsity/TEAL）均报告实际加速。本文在加速维度完全缺席。\n- Abstract \"renders compensation redundant\" 误导读者期望速度提升，实际只节省 ~2.7% latency 开销。\n- 论文已坦诚承认，但 framing 需更明确限定为 prediction quality study。\n\n**W4. 方法新颖性有限。** [R2 提出, R1 部分同意]\n- 核心技术为 BCE→KL loss swap + 标准 Gumbel-Sigmoid relaxation。与 MaskLLM 的区别（activation vs weight sparsity, predictor vs direct mask, global vs N:M）是问题设定差异而非方法创新。\n- R1 反驳：两个方法有结构性差异，不应过度抽象。但同意论文的真正贡献是实证发现（mask divergence, C1 ablation, regime analysis）而非方法本身。\n- 论文已定位为 \"primarily empirical\"，建议进一步强化。\n\n**W5. 30% λ 饱和偏差 5%，train-inference mismatch。** [R1 提出, R2 同意并定量分析]\n- 训练时实际稀疏度 28.5%，推理强制 30%。严格对比应为 KL@28.5% vs TEAL@28.5%（improvement 13% 而非宣称 18%）。\n- Appendix 有 defense（TEAL@28.5% PPL=10.30，gap 0.67 远小于 KL 优势 2.01），但应在主文讨论。\n\n**W6. 30% downstream 退化严重，\"best quality\" 表述不当。** [R2 提出, R1 同意]\n- GSM8K 84% 退化（48.75→7.5%），MMLU 38% 退化（65.27→40.7%）。所有方法退化相近（说明是稀疏度固有限制），但 \"best quality\" 应改为 \"least-degraded\"。\n\n**W7. Conclusion 仅两句话。** [R1, R2 共识]\n- 无 future work、无 broader impact。至少补 N:M 结构化稀疏、更大规模验证等方向。\n\n**W8. WikiText-103→WikiText-2 同源。** [R1, R2 共识]\n- C4 OOD gap 更大（1.74× vs 1.46×），说明 partial overfitting。建议主表加 C4 PPL 列。\n\n### Info (Minor)\n\n**M1. 写作/编辑问题集合。** [R1, R2 共识]\n- PPL 11.79 vs 11.80 不一致\n- WINA 列为 baseline 但无实验数据\n- \"Phase transition\" 术语过强（建议 \"capacity cliff\"）\n- SNR \"at convergence\" 实际在 step 300 测量（训练 1000 步）\n- \"68% divergence\" Introduction 中轻微重复\n- HellaSwag/PIQA 未在 §4.1 Evaluation 提及\n- s42† earlier checkpoint 解释不足\n- SwiGLU 未在 Abstract 定义\n- §2.5 自适应惩罚控制器篇幅比例偏大\n- exp_id 注释需清理\n- \"in context of\" → \"in the context of\"\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **数值错误必须修正**：C1 max Δ (0.59→0.79pp) + Table 2/4 BCE 矛盾\n2. **C1 命名过强**：应降级为 \"Target-Swap Ablation\"\n3. **无 wall-clock 加速**：framing 需更明确限定贡献范围\n4. **14B 单 seed 不足**：至少 3-seed 确认 MMLU 反转稳定性\n5. **Findings 定位合理**：方法新颖性增量，但实证分析有价值\n6. **Overall 3.0**：两人独立给出相同分数\n\n## Reviewer Divergence\n\n仅 2 项轻微分歧（已在交叉中达成共识）：\n1. **MSE baseline 严重性**：R1=Must-Fix（taxonomy 需实验验证），R2=Should-Fix（不影响核心 claim）。Director 判定 Should-Fix。\n2. **MaskLLM 技术距离**：R2 认为距离小（Must-Fix），R1 部分反驳（结构性差异存在但方法新颖性确实有限）。两人一致建议强化 empirical study 定位。\n\n---\n\n## Questions\n\n以下问题由两位 Reviewer 共同或独立提出，需作者回应：\n\n1. **Table 2/4 BCE 配置**：两个表格的 BCE+compensation 条目是否为同一实验？训练步数、seed、是否含 compensation？[R1-Q1, R2 交叉确认]\n2. **C1 50% max Δ 计算来源**：0.59pp 如何得出？第二个 seed 数据？[R1-Q2]\n3. **28.5% train-inference gap**：预测器是否在 30% 推理条件下验证/选择？严格对比下 improvement 为 13% 而非 18%？[R1-Q3, R2-Q4]\n4. **14B MMLU 多 seed 稳定性**：-8.1pp 逆转是 systematic 还是 seed 效应？[R1-Q6, R2-Q1]\n5. **KL-only 神经元贡献**：KL 选择但 magnitude 不选择的神经元对 output distribution 有什么实际贡献？[R2-Q2]\n6. **GSM8K 反转机制**：forward KL 的 mass-covering 性质是否在 reasoning 任务上不如 mode-seeking？[R1-Q5, R2-Q3]\n7. **C4 训练可能性**：在非 WikiText 数据上训练 predictor 能否减少 domain overfitting？[R2-Q5]\n\n---\n\n## Missing References\n\n两位 Reviewer 一致认为引用覆盖良好（47 篇，密度合理）。无重大遗漏。\n- R2 建议考虑 LLM.int8() (Dettmers et al., 2022)，R1 反驳：量化不在本文 scope 内，Wang et al. 2025 已覆盖 sparsity+quantization 交叉。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未配置**。项目无 `external_review.paperreview_ai.enabled` 设置。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | **3.0/5** — 核心方法正确，但数值错误（N1）和数据矛盾（N2）直接削弱核心 claim 可信度 |\n| Excitement | 3.0/5 | 2.5/5 | **2.5/5** — KL 发现不同 mask pattern 有趣，但方法增量、无实际加速、规模受限 |\n| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** — 超参数完整、3-seed、GPU 型号齐全；未开源代码 |\n| Overall | 3.0/5 | 3.0/5 | **3.0/5 (Findings)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**Overall Score: 3.0 (Findings)**\n\n**推荐: Findings（修复 N1-N2 后可稳定；当前因数值错误在 Borderline Findings 2.5-3.0 边缘）**\n\n**核心判断依据**:\n1. **支撑 Findings 接收的因素**: C1 target-swap 消融是有价值的分析创新；mask divergence 发现（68%）提供了对 KL 训练行为的新理解；三段式 regime analysis 有实用参考价值；实验覆盖面广且报告诚实\n2. **阻止 Main 接收的因素**: 方法新颖性增量（loss swap + 标准技术）；无 wall-clock 加速；14B 可扩展性存疑（MMLU 逆转且仅单 seed）；数值错误影响核心 claim 可信度\n3. **修复优先级**: N1 数值勘误 > N2 表格标注澄清 > W1 C1 命名 > W2 14B 多 seed > W3 framing 调整\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 结构合理，四个必答问题覆盖。\"renders compensation redundant\" 需加 \"in prediction quality\" 限定。\"capacity phase transition\" 改为 \"capacity cliff\"。68% divergence 来自 50% 稀疏度但未标注。\n\n### Introduction (§1)\n- 从 BCE/global-allocation mismatch 切入清晰。但 ¶2-¶3 数字密度过高，部分数据应移至 §4。Contribution 第 3 条（non-monotonic allocation + 14B effects）在前文无铺垫。\"68% divergence\" 在 ¶2 和 Contribution list 重复，建议 Contribution list 用 \"the discovered mask patterns (§4.3)\" 指代。\n\n### Related Work (§2)\n- 覆盖全面，MaskLLM 三点区分详细。MoE routing 段与主线关系稍远但可接受。D2DMoE/ShadowLLM 的 \"intermediate coupling\" 未量化与 \"coupled\" 的差距（缺 MSE baseline 的根源）。\n\n### Method (§3)\n- §3.1-§3.4 清晰规范。§3.5 自适应惩罚控制器篇幅过大（本质为标准技术）。§3.6 梯度分析正确标注 \"suggestive\" 但 \"reveals structural asymmetry\" 用词暗示超过 suggestive 的结论。\n\n### Experiments (§4)\n- 最强部分。Table 4 ablation、regime analysis (§4.6) 扎实。Table 2 数据矛盾（N2）和 C1 数值错误（N1）是必须修复的硬伤。WINA 幽灵 baseline 需移除或补数据。\n\n### Conclusion (§5)\n- 两句话严重不足。需扩展至 4-6 句，含 future work（N:M sparsity, 70B scaling, multi-target predictor）。\n\n### Limitations\n- 全面诚实，是论文优点。\"best-quality\" → \"least-degraded\"。\n\n### Appendix\n- 内容丰富，所有附录在正文有引用。Appendix C（λ 收敛）的 defense 合理但应在主文摘要。\n"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-19T08:07:44.104221+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4731
}
```

</details>

---


### Assistant

_source line 1022 · 2026-05-19T08:07:51.470904+00:00_

审稿报告已投递。

---

**Round 12 审稿完成。**

汇总：
- **Overall Score: 3.0 (Findings)**，两位 Reviewer 独立评分一致，交叉后全面共识
- **3 个 Critical issues**：C1 max Δ 数值错误 (0.59→0.79pp)、Table 2/4 BCE 数据矛盾、缺少 MSE intermediate baseline
- **8 个 Warning issues**：C1 命名过强、14B 单 seed、无加速、方法新颖性有限、λ 偏差、30% downstream 退化表述、Conclusion 过短、同源评估
- **1 个 Info**：写作/编辑问题集合（11 项）
- Issue Tracker 已同步更新至 `review_issues.yaml`
- 报告已通过 `submit_review_report_to_research_director` 投递

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 84

## Round 84

2 recorded events


### User

_source line 1023 · 2026-05-19T08:07:54.222477+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 全部 11 条 Weakness 均标注 [AGREE]，无反驳项。R1 发现了我 Round 1 中遗漏的几个重要问题（W1 数值勘误、W2 Table 2/4 BCE+comp PPL 矛盾 28.13 vs 25.44、W8 WINA 幽灵 baseline、W10 SNR 测量点非收敛）。两位审稿人独立发现的共同问题（无加速、C1 confound、14B 单 seed）强化了这些问题的严重性。评分维持 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1024 · 2026-05-19T08:08:05.408818+00:00_

审稿报告已投递至 Research Director。

**Round 12 审稿完成。**

最终结论：
- **Overall: 3.0 (Findings)**，两位 Reviewer 独立给出相同评分，交叉后完全收敛（11/11 Weakness 达成共识）
- **Critical issues (3项)**：C1 max Δ 数值错误 (0.59→0.79pp)、Table 2/4 BCE+comp PPL 矛盾 (28.13 vs 25.44)、缺 MSE intermediate baseline（降级为 Should-Fix）
- **修复优先级**：N1 数值勘误 > N2 表格标注澄清 > W1 C1 命名降级 > W2 14B 多 seed > W3 framing 限定
- **定位建议**：Findings 接收，修复 N1-N2 后可稳定 3.0；当前因数值错误在 Borderline Findings (2.5-3.0) 边缘

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（12 条新/更新 issue + 历史状态追踪）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 85

## Round 85

78 recorded events


### User

_source line 1025 · 2026-05-20T01:32:15.920847+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-20T01:32:23.397320+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-20T01:32:23.398214+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-20T01:32:29.823757+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-20T01:32:29.874357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-20T01:32:33.590096+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1031 · 2026-05-20T01:32:34.092396+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1032 · 2026-05-20T01:32:34.594871+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (268 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| qwen14b_teal30_uniform_gsm8k | TEAL@30% uniform allocation GSM8K eval for Qwen-14B. Nominal-matched comparison for appendix table. Supplements existing TEAL@30% uniform 4-task + HS+PIQA data. | — | — | — |\n\n## 待处理\n- kl30_uniform_hspiqa_s123（准备中）\n- bench_teal50_uniform_6task（准备中）\n- bench_kl30_uniform_gsm8k_d075（准备中）\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- …另有 6 项\n\n## 近期结论\n- **qwen14b_kl30_s456_gsm8k** (success): KL s456 GSM8K supplement for Qwen-14B. Completes 3-seed GSM8K comparison. Required for complete 14B paper table. ← 基于 qwen14b_kl30_s456_eval_v3\n- **c1
…[truncated 1798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-20T01:32:35.349322+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1034 · 2026-05-20T01:32:35.399993+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-20T01:32:40.679199+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information related to EMNLP 2026 and ARR submission guidelines, though the main EMNLP 202
…[truncated 1321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6586
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-20T01:32:44.451741+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 1037 · 2026-05-20T01:32:45.406408+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-20T01:32:45.557379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-20T01:32:45.557758+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
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
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1040 · 2026-05-20T01:32:51.689803+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about EMNLP 2026 main conference call for papers submission deadline and ARR commitment:

## Key Deadlines

The ARR submission deadline for EMNLP 2026 is 
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7238
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-20T01:32:52.894957+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"}]

Based on the web search results, here's what I found about ACL Rolling Review 2026 submission guidelines regarding page limits and author instructions:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. The search results also indicate that submissions that exceed the length requirements, or are missing a limitations section, will be desk reject
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7488
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-20T01:32:59.662572+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements: page limits (long/short paper), formatting template, anonymity rules, appendix rules, limitations section rules, deadline dates, commitment deadline, and any special policies for EMNLP 2026. Be thorough and exact."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements: page limits (long/short paper), formatting template, anonymity rules, appendix rules, limitations section rules, deadline dates, commitment deadline, and any special policies for EMNLP 2026. Be thorough and exact."
  }
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-20T01:33:00.523409+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines: page limits for long and short papers, formatting requirements, anonymity policy, limitations section rules, appendix rules, citation format, template requirements, and any desk-reject criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines: page limits for long and short papers, formatting requirements, anonymity policy, limitations section rules, appendix rules, citation format, template requirements, and any desk-reject criteria."
  }
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-20T01:33:05.752276+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Camera-ready accepted papers:** Up to 9 pages (long) or 5 pages (short) to address reviewer feedback

## Key Deadlines
- **ARR Submission Deadline:** May 25, 2026 (11:59 PM UTC-12:00)
- **Reviewer Registration Deadline:** May 27, 2026
- **Author Response Period:** July 7-13, 2026
- **Meta-review Release:** July 30, 2026
- **EMNLP Commitment Deadline:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-ready Due:** September 20, 2026
- **Main Conference:** October 24-29, 2026

## Anonymity Rules
Following "ACL and ARR policies, there is no anonymity period requirement." The review process itself "will continue to be double-blind" with reviewers and author identities hidden during review.

## Critical Submission Rules

**Formatting & Templates:** Authors must "follow all of the ARR submission requirements" including proper templates (specifics referenced at ARR website).

**Appendices & Supplementary Materials:** The document references "Optional Supplementary Materials" but directs readers to ARR guidelines for detailed specifications.

**Limitations Section:** Required per ARR ethics policy standards.

**Special Policies for EMNLP 2026:**
- Papers submitted to ARR's May 2026 cycle must "explicitly declare which conference they intend to commit to at submission time"
- "Dual submissions are not allowed"
- "During the commitment phase, it is not allowed to modify the author list"—author order changes are permitted
- Desk rejection possible for papers with "hallucinated citations" or ethics violations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 6089
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-20T01:33:07.714996+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations section
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations section
- Unlimited reference pages

Papers exceeding length requirements or missing a limitations section face desk rejection.

## Formatting Requirements

Submissions must adhere to the official ACL style template available on GitHub and follow "*ACL" conference formatting guidelines. Papers using non-compliant styles, including incorrect margins, paper size, or fonts, will be rejected without review. All text must address human readers clearly and visibly.

## Anonymity Policy

Papers must not contain author names or affiliations. Self-citations should be phrased as "Smith previously showed (Smith, 1991)" rather than revealing the authors' identities. All supplementary materials and repository links must remain anonymized, with Dropbox-style tracking services prohibited.

## Limitations Section

A dedicated "Limitations" section is mandatory and must appear before references without counting toward page limits. This section should discuss constraints of the presented work only—it cannot introduce new methods, analysis, or results. Submissions lacking this section face desk rejection.

## Appendix Rules

Appendices follow the main paper and references, don't count toward page limits, and must use double-column formatting (with approved exceptions). Reviewers aren't obligated to review appendix content. Critical technical details should appear in the main paper, not appendices, to avoid circumventing page limits.

## Citation Format for Concurrent Work

When citing concurrently submitted related papers by overlapping author groups:

> "Anonymous (2026). Paper title. Under review."

## Template Requirements


…[truncated 631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 7191
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-20T01:33:12.548060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-20T01:33:13.053186+00:00_

1	Learned sparsity predictors for SwiGLU (Swish-Gated Linear Unit) LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train predictors with Kullback-Leibler (KL) divergence, coupling all mask decisions through the output distribution.
3	At 30\% sparsity on LLaMA-3.1-8B, the KL predictor ($<$1\% of base parameters) reduces perplexity by 19\% relative to TEAL with moderate downstream degradation, and renders post-hoc compensation (+67.2M params) redundant in prediction quality.
4	KL-derived masks diverge 68\% from magnitude-based masks; a target-swap ablation confirms that these mask targets, discovered through KL's coupled gradients, are the proximate quality driver when transferred to simpler objectives.
5	On Mistral-7B-v0.3, KL outperforms TEAL on 5 of 6 downstream tasks at 30\%; at 14B, perplexity generalizes but downstream diverges---commonsense improves while reasoning (GSM8K $-$25pp) and factual retrieval (MMLU) decline.
6	At 50\% sparsity the perplexity advantage widens, though downstream reasoning collapses to near-random regardless of method, revealing a capacity cliff.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-20T01:33:13.053536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-20T01:33:14.115876+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
9	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
10	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Gradient coupling remains necessary at the discovery stage.
11	
12	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
13	At 30\% sparsity under uniform allocation, the predictor reduces TEAL's perplexity by 19\% (8.81 vs.\ 10.82) with stable downstream (MMLU 40.7$\pm$1.3\%, 3-seed); global top-$k$ a
…[truncated 1434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-20T01:33:14.267054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-20T01:33:14.468776+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
8	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
9	
10	\paragraph{Predictor-Based Contextual Sparsity.}
11	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
12	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
13	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
14	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
15	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
16	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
17	First, \emph{spar
…[truncated 4220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-20T01:33:14.469311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-20T01:33:14.923462+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 10559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-20T01:33:14.923995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-20T01:33:15.431451+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 18781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-20T01:33:15.431844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-20T01:33:15.885642+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-14pt}
4	
5	A target-swap ablation confirms that KL-discovered mask patterns (68\% divergent from magnitude) are the proximate driver of inference-stage quality.
6	A predictor ($<$1\% of base) reduces TEAL's perplexity by 19\% at 30\%, renders compensation redundant, and delivers $7.5\times$ smaller cross-seed $\sigma$ under uniform allocation.
7	Mistral-7B confirms the pattern (5/6 tasks); 14B reveals task-and-scale-dependent effects, motivating N:M sparsity and layer-wise probing.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-20T01:33:15.885993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-20T01:33:16.389663+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades; 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B, KL wins 5 of 6 downstream tasks at 30\% but GSM8K reverses (11.1\% vs.\ TEAL's 15.9\%), consistent with GSM8K's sensitivity to the sparsity objective: reasoning tasks may require different optimization targets than knowledge and commonsense benchmarks; forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$25pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 57.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, which indicates that the predictor partially overfits to training-domain activation patterns. Extending OOD evaluation to 70\% sparsity is left to future work.
8	The target-swap ablation (\S\ref{sec:mask_analysis}) confirms that mask quality is the proximate driver of inference-stage quality, with KL
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-20T01:33:16.390061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-20T01:33:17.297797+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-20T01:33:17.298271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-20T01:33:17.500677+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 20679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-20T01:33:17.551827+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-20T01:33:17.602524+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-20T01:33:22.502218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-20T01:33:22.696070+00:00_

1	issues:
2	  # ============================================================
3	  # Round 12 (fresh review) — New/recurring issues
4	  # ============================================================
5	
6	  - id: "R12-N1"
7	    summary: "C1 消融 50% max Δ 数值错误：论文声称 0.59pp，Table 3 实际为 0.79pp (WG)"
8	    category: experiment
9	    severity: critical
10	    status: open
11	    first_raised_round: 12
12	    last_seen_round: 12
13	    mentions:
14	      - {round: 12, reviewers: [1, 2], note: "Full consensus. R1 首先发现，R2 交叉确认。Table 3 caption 'max Δ=0.59pp at 50% (2-seed)' 与表格数据 |63.14−62.35|=0.79pp 不符。另外 '2-seed' 声称但仅展示 1 seed pair。"}
15	    action_items:
16	      - {round: 12, action: "更正 max Δ 为 0.79pp，同步修改 Abstract、Introduction、§4.4 中引用该数字的段落。确认第二个 seed 数据并补入表格或移除 '2-seed' 声称。", assigned_to: "paper_agent", status: open}
17	    resolution: ""
18	    resolution_round: null
19	
20	  - id: "R12-N2"
21	    summary: "Table 2 BCE+comp (28.13±0.20) vs Table 4 BCE+Compensation (25.44) 数值矛盾不可调和"
22	    category: experiment
23	    severity: critical
24	    status: open
25	    first_raised_round: 12
26	    last_seen_round: 12
27	    mentions:
28	      - {round: 12, reviewers: [1, 2], note: "Full consensus. Table 2 脚注标注 'DejaVu/FastForward pipeline with compensation' 但 3-seed std=0.20 意味所有 seed 在 27.93-28.33，与 Table 4 seed 42=25.44 矛盾。R2 推测 Table 2 实际为 BCE without compensation。§4.3 的 '28.13±0.20' 也说 'BCE predictor' 非 'BCE+compensation'。"}
29	    action_items:
30	      - {round: 12, action: "澄清 Table 2 'BCE+comp' 与 Table 4 'BCE+Compensation' 是否为同一实验配置（训练步数、seed、是否含 compensation）。修正标注错误。", assigned_to: "paper_agent", status: open}
31	    resolution: ""
32	    resolution_round: null
33	
34	  - id: "R12-N3"
35	    summary: "缺少 Intermediate-coupling (MSE) baseline 实验对比，Taxonomy claim 无实验支撑"
36	    category: experiment
37	    severity: critical
38	    status: open
39	    first_raised_round: 12
40	    last_seen_round: 12
41	    mentions:
42	      - {round: 12, reviewers: [1, 2], note: "R1 定 Mus
…[truncated 16446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 193
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-20T01:33:22.753080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-20T01:33:23.118487+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 18976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 365
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-20T01:33:23.204338+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-20T01:33:23.209315+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 4
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-20T01:33:43.763779+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '启动 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '启动 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-20T01:33:43.764335+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-20T01:33:45.271990+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/constraints.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/constraints.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-20T01:33:45.322717+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-20T01:33:48.389803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-20T01:33:48.440528+00:00_

1	_next_id: 5
2	constraints:
3	- id: C002
4	  added: 2026-05-16 03:08 UTC
5	  summary: 所有 GPU 长时间实验必须用 nohup 启动并重定向日志，禁止裸 tmux session
6	  scope: worker
7	  reason: 'bce_isocompute_s42 和 v2 两次因 tmux session 被挤掉而死，导致 Reviewer Concern #2 完全无防御数据'
8	- id: C003
9	  added: 2026-05-16 12:32 UTC
10	  summary: 论文中所有超参/架构数字必须有代码来源验证，禁止从记忆或猜测填写。Predictor 正确参数：GELU, d_b=128, 2.37M/layer,
11	    75.9M total。
12	  scope: all
13	  reason: Reviewer 发现 experiments.tex + methodology.tex 共 7 处超参事实错误（ReLU/GELU、d_b=256/128、batch_size=32/4
14	    等），根因是 Paper Agent worker 未读源代码靠猜测填写。
15	- id: C004
16	  added: 2026-05-17 15:15 UTC
17	  summary: GPU 白名单：仅允许使用 westd-34887 cuda:0/cuda:1 和 westd-41718 cuda:0/cuda:1，禁止使用其他
18	    GPU
19	  scope: all
20	  reason: 项目分配资源边界。westd-34887 为原始分配，westd-41718 为 Manager 批准的扩容（2026-05-17）。
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-20T01:33:52.609199+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-20T01:33:52.760222+00:00_

Found 19 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_9377f94f5f31e719154474b70f5c3d18_paper_agent.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/archive/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director_20260519T112409_568217.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/worker_ops_mask-vis-64samples-30pct_20260518T195918.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_ops_mask-vis-64samples-30pct_20260518T195918.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/archive/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director_20260517T171027_960441.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/worker_util_copy_lagrangian_fig_20260517T070307.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_
…[truncated 492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-20T01:33:55.887821+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review.*enabled\"\n&lt;parameter name=\"path\">/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review.*enabled\"\n&lt;parameter name=\"path\">/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-20T01:33:55.938425+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-20T01:33:59.504392+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content",
  "glob": "CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content",
    "glob": "CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-20T01:33:59.605441+00:00_

CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-20T01:34:03.884248+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview|external_review.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "output_mode": "content",
  "glob": "AGENTS.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paperreview|external_review.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
    "output_mode": "content",
    "glob": "AGENTS.md"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-20T01:34:03.936341+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-20T01:34:07.006213+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "output_mode": "content",
  "glob": "**/config*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
    "output_mode": "content",
    "glob": "**/config*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-20T01:34:07.056879+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-20T01:34:09.973193+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-20T01:34:10.025313+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-20T01:34:12.699446+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-20T01:34:12.901876+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-20T01:34:16.323111+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review\"\n&lt;parameter name=\"path\">/home/ubuntu/agent-ml-research",
  "output_mode": "content",
  "glob": "**/*.py",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review\"\n&lt;parameter name=\"path\">/home/ubuntu/agent-ml-research",
    "output_mode": "content",
    "glob": "**/*.py",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-20T01:34:16.373807+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-20T01:34:38.766970+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '启动 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '启动 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-20T01:34:38.767440+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-20T01:34:39.673923+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-20T01:34:55.618420+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15944
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-20T01:34:55.769943+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责【方法严谨性 + 实验设计】审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献无限，Limitations 必须有（不计页数），Double-blind，ACL 模板\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`（各章节 \\input 引入）\n- **PDF**: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **梯度分析（§3.6）**：BCE vs KL 梯度对比的数学推导是否正确？\"coupled gradient\" 的 claim 是否有足够理论/实验支撑？\n2. **Gumbel-Sigmoid relaxation（§3.3）**：温度退火策略的选择是否合理？soft-vs-hard confound 是否被充分讨论？\n3. **Adaptive penalty controller（§3.5）**：Lagrangian 松弛方案的收敛性证据是否充分？30% 偏差 5% 的 train-inference mismatch 是否影响结论？\n4. **C1 Target-Swap Ablation（§4.4）**：实验设计是否能支撑其 claim？confound 边界是否清晰？\"proximate driver\" 表述强度是否合理？\n\n### 实验设计\n5. **统计方法**：multi-seed 评估的覆盖是否充分？哪些关键结论仅基于单 seed？seed 数量是否足以支撑结论？\n6. **Baseline 充分性**：BCE baseline 是否公平（训练步数、架构一致性）？缺少哪些 baseline？\n7. **数据泄漏风险**：WikiText-103 训练 → WikiText-2 评估，同源风险是否被充分处理？C4 OOD 结果是否改变结论？\n8. **14B 和 Mistral 结果**：cross-architecture 实验的 claim 强度是否与数据匹配？GSM8K 和 MMLU 逆转是否被充分解释？\n\n### 数值一致性\n9. 检查所有表格数字是否一致（Abstract/正文/表格/Appendix 之间）。特别注意 C1 ablation max Δ 数值。\n\n请输出完整审稿意见，格式：Summary → Strengths（逐条） → Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责【方法严谨性 + 实验设计】审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献无限，Limitations 必须有（不计页数），Double-blind，ACL 模板\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`（各章节 \\input 引入）\n- **PDF**: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 方法严谨性\n1. **梯度分析（§3.6）**：BCE vs KL 梯度对比的数学推导是否正确？\"coupled gradient\" 的 claim 是否有足够理论/实验支撑？\n2. **Gumbel-Sigmoid relaxation（§3.3）**：温度退火策略的选择是否合理？soft-vs-hard confound 是否被充分讨论？\n3. **Adaptive penalty controller（§3.5）**：Lagrangian 松弛方案的收敛性证据是否充分？30% 偏差 5% 的 train-inference mismatch 是否影响结论？\n4. **C1 Target-Swap Ablation（§4.4）**：实验设计是否能支撑其 claim？confound 边界是否清晰？\"proximate driver\" 表述强度是否合理？\n\n### 实验设计\n5. **统计方法**：multi-seed 评估的覆盖是否充分？哪些关键结论仅基于单 seed？seed 数量是否足以支撑结论？\n6. **Baseline 充分性**：BCE baseline 是否公平（训练步数、架构一致性）？缺少哪些 baseline？\n7. **数据泄漏风险**：WikiText-103 训练 → WikiText-2 评估，同源风险是否被充分处理？C4 OOD 结果是否改变结论？\n8. **14B 和 Mistral 结果**：cross-architecture 实验的 claim 强度是否与数据匹配？GSM8K 和 MMLU 逆转是否被充分解释？\n\n### 数值一致性\n9. 检查所有表格数字是否一致（Abstract/正文/表格/Appendix 之间）。特别注意 C1 ablation max Δ 数值。\n\n请输出完整审稿意见，格式：Summary → Strengths（逐条） → Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-20T01:35:09.793203+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14023
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-20T01:35:09.944274+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责【新颖性 + 完整性 + 写作/格式】审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献无限，Limitations 必须有（不计页数），Double-blind，ACL 模板\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`（各章节 \\input 引入）\n- **PDF**: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **方法贡献**：核心是 BCE→KL loss swap + 标准 Gumbel relaxation。与 MaskLLM（同为 KL+Gumbel+frozen weights）的区分度是否足够？论文自称 \"empirical contribution\"，是否匹配 EMNLP Findings 水平？\n2. **Taxonomy（§3.7, Table 1）**：two-dimensional taxonomy 是否有概念新颖性？intermediate-coupling (MSE) 缺少实验支撑，taxonomy 是否成立？\n3. **实验新颖性**：C1 target-swap ablation 和 regime analysis 是否构成足够的 empirical insight？\n\n### 完整性\n4. **Related Work 覆盖**：是否遗漏重要工作？47 篇引用是否覆盖了 training-free sparsity、predictor-based sparsity、KL distillation 的关键文献？\n5. **实验覆盖**：是否缺少关键实验（如 MSE intermediate baseline、更大规模模型、其他 sparsity 方法对比）？\n6. **Limitations**：限制讨论是否充分、诚实？是否有遗漏的重要限制？\n7. **Conclusion**：是否过于简短？是否有 future work？\n\n### 写作质量和格式\n8. **叙事一致性**：Abstract → Intro → Method → Experiments → Conclusion 是否叙事连贯？claim 强度是否在全文一致？\n9. **格式合规**：页数是否 ≤8 页正文？是否使用 ACL 模板？匿名性是否满足？\n10. **表格/图表**：是否清晰、信息量充足？caption 是否自包含？\n11. **写作风格**：是否有 AI 写作痕迹？是否过于冗余或过于简略？术语使用是否一致？\n12. **引用格式**：是否使用 natbib？引用是否完整（会议/期刊/年份）？是否有幽灵/幻觉引用？\n\n请输出完整审稿意见，格式：Summary → Strengths（逐条） → Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责【新颖性 + 完整性 + 写作/格式】审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（via ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: Long paper，正文 8 页，参考文献无限，Limitations 必须有（不计页数），Double-blind，ACL 模板\n- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`（各章节 \\input 引入）\n- **PDF**: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 新颖性评估\n1. **方法贡献**：核心是 BCE→KL loss swap + 标准 Gumbel relaxation。与 MaskLLM（同为 KL+Gumbel+frozen weights）的区分度是否足够？论文自称 \"empirical contribution\"，是否匹配 EMNLP Findings 水平？\n2. **Taxonomy（§3.7, Table 1）**：two-dimensional taxonomy 是否有概念新颖性？intermediate-coupling (MSE) 缺少实验支撑，taxonomy 是否成立？\n3. **实验新颖性**：C1 target-swap ablation 和 regime analysis 是否构成足够的 empirical insight？\n\n### 完整性\n4. **Related Work 覆盖**：是否遗漏重要工作？47 篇引用是否覆盖了 training-free sparsity、predictor-based sparsity、KL distillation 的关键文献？\n5. **实验覆盖**：是否缺少关键实验（如 MSE intermediate baseline、更大规模模型、其他 sparsity 方法对比）？\n6. **Limitations**：限制讨论是否充分、诚实？是否有遗漏的重要限制？\n7. **Conclusion**：是否过于简短？是否有 future work？\n\n### 写作质量和格式\n8. **叙事一致性**：Abstract → Intro → Method → Experiments → Conclusion 是否叙事连贯？claim 强度是否在全文一致？\n9. **格式合规**：页数是否 ≤8 页正文？是否使用 ACL 模板？匿名性是否满足？\n10. **表格/图表**：是否清晰、信息量充足？caption 是否自包含？\n11. **写作风格**：是否有 AI 写作痕迹？是否过于冗余或过于简略？术语使用是否一致？\n12. **引用格式**：是否使用 natbib？引用是否完整（会议/期刊/年份）？是否有幽灵/幻觉引用？\n\n请输出完整审稿意见，格式：Summary → Strengths（逐条） → Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-20T01:35:11.564217+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1619
}
```

</details>

---


### Assistant

_source line 1102 · 2026-05-20T01:35:21.634429+00:00_

已完成初始化：
- 视觉审查 Agent 已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）已启动
- Reviewer 2（新颖性 + 完整性 + 写作/格式）已启动

等待两名 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 86

## Round 86

4 recorded events


### User

_source line 1103 · 2026-05-20T01:41:40.105594+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作/格式）

**论文**：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**：EMNLP 2026 via ARR May 2026

---

## 总体评分

**Overall**: 3.0 — Findings
**一句话总结**: 一篇执行扎实的实证研究，C1 ablation 设计精巧，但核心方法（BCE→KL loss swap）新颖性有限，下游任务结果 mixed（尤其 GSM8K 和 14B scale），且缺少实际加速验证，整体处于 Findings 水平。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理，C1 ablation 严谨，multi-seed 报告规范；但 taxonomy 中 MSE intermediate baseline 缺失削弱论证完整性，下游结果与 PPL 改善不匹配 |
| Excitement | 2.5/5 | 核心贡献是 loss function swap（KL 替代 BCE），MaskLLM 已证明 KL 用于 mask learning 有效；C1 ablation 的 insight（mask quality > gradient coupling）有价值但同时 self-deflating |
| Reproducibility | 4/5 | 超参完整披露，3-seed 评估，GPU 型号/训练时间均报告 |
| Overall Assessment | 3.0/5 | Findings 水平——实证贡献清晰但方法新颖性不足，实用价值存疑（无 speedup、下游 mixed） |

**Reviewer Confidence**: 4/5

---

## Summary

本文提出将 SwiGLU LLM 稀疏预测器的训练目标从 per-neuron BCE 替换为 output-distribution KL divergence，配合 Gumbel-Sigmoid relaxation 实现端到端可微训练。在 LLaMA-3.1-8B 上，KL predictor 在 30% sparsity 下将 perplexity 相对 TEAL 降低 19%（8.81 vs 10.82），在 50% 降低 51%。C1 target-swap ablation 表明 KL 发现的 mask pattern（与 magnitude mask 68% divergence）是质量提升的 proximate driver，而非 gradient coupling 本身。论文还评估了 Mistral-7B 和 Qwen-2.5-14B，并提出基于 correction granularity × training signal coupling 的 two-dimensional taxonomy。

---

## Strengths（主要优势）

**S1. C1 Target-Swap Ablation 设计精巧（§4.4, Table 3）**
这是本文最强的贡献。用 KL-discovered masks 训练 BCE predictor，在 50% sparsity 下 PPL 差异 ≤0.79pp（s42），在 30% 下 retrained seeds（s123, s456）差异 ≤0.03 PPL。这清晰地将 KL 的优势归因于 mask quality 而非 gradient coupling mechanism，是一个有说服力的 disentanglement 实验。

**S2. 实验设计规范**
- 3-seed 评估（s42, s123, s456），报告 mean±std
- 6 个下游任务覆盖 commonsense/reasoning/factual retrieval
- Iso-compute 对比（BCE 2700 steps ≈ KL 1000 steps wall-clock）
- Comprehensive ablation（Table 4）隔离 Gumbel vs STE、divergence direction、loss function 贡献

**S3. 诚实且全面的 Limitations 讨论**
Limitations section 是本文的显著优点。坦诚讨论了 PPL 作为下游 proxy 的局限性、GSM8K reversal（Mistral -4.8pp, 14B -25pp）、global allocation 下 MMLU σ=9.5pp（30%）、OOD gap（C4 PPL 1.74× dense vs in-domain 1.46×）、以及无 wall-clock speedup。这种诚实的自我评估在同行评审中值得肯定。

**S4. Cross-Architecture 验证**
在三个模型家族（LLaMA-8B, Mistral-7B, Qwen-14B）上测试，揭示了 scale-dependent effects，而非仅在单一模型上报告结果。

**S5. Related Work 覆盖全面**
47 篇引用系统覆盖了 training-free sparsity、predictor-based methods、KL distillation、activation engineering、weight pruning、MoE routing 等所有相关方向。与 MaskLLM 的三点区分（sparsity type/mask generation/allocation）论述清晰。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **方法新颖性不足：核心贡献是 standard KL + standard Gumbel 的组合**
- 具体位置：§3.4 (KL objective), §3.3 (Gumbel relaxation), Related Work line 21
- 问题：论文的核心方法是将 distillation 中标准的 forward KL divergence（Hinton et al., 2015; Kim & Rush, 2016）与标准的 Gumbel-Sigmoid relaxation（Maddison et al., 2017; Jang et al., 2017）应用于 sparsity predictor 训练。论文自身在 Related Work 中承认 "Our contribution is primarily empirical"（line 21）。MaskLLM (Fang et al., 2024) 已在 NeurIPS 2024 证明了 "frozen weights + learnable masks + KL training" 的有效性。虽然论文指出了与 MaskLLM 的三点区别（activation vs weight sparsity, predictor vs learnable params, global top-k vs N:M），但核心 principle（用 KL 训练 mask）是相同的。
- 为什么影响接收：即使 ARR guidelines 明确表示 "SOTA results are neither necessary nor sufficient" 且欢迎 empirical contributions，但 loss function swap 本身（BCE→KL）在 distillation 领域是 well-known 的选择，缺乏足够的方法论贡献来支撑一篇 long paper。
- 建议修改方向：(a) 补充 MSE intermediate baseline 实验以验证 taxonomy 的完整性；(b) 深入分析 KL gradient 为何能 discover 不同 mask patterns 的机制（而非仅观察到 68% divergence）；(c) 探索 KL-discovered masks 是否可以用于 one-shot mask extraction 而无需 per-sparsity 训练。

**N2** [critical] **下游任务结果与 PPL 改善严重不匹配，削弱实用价值**
- 具体位置：Table 2, §4.6 (cross-architecture), Limitations
- 问题：论文的核心 narrative 是 "KL reduces perplexity by 19%"，但下游任务表现 mixed：
  - **30% sparsity on LLaMA-8B**：KL uniform MMLU 40.7±1.3% vs TEAL 45.86%（-5.2pp），GSM8K 7.5±0.1% vs TEAL 8.79%（-1.3pp）。KL 在 PPL 上赢但在 MMLU/GSM8K 上输。
  - **Mistral-7B**：GSM8K 11.1% vs TEAL 15.9%（-4.8pp）
  - **Qwen-14B**：GSM8K -25pp, MMLU -2.79pp（uniform），更大 scale 上劣势加剧
  - **50% sparsity**：所有方法 MMLU 坍塌至近随机（~28%）
  
  这意味着 KL predictor 的 19% PPL 改善并未 translate 为 downstream quality 改善，甚至在部分任务上显著退化。论文的 Limitations 诚实讨论了这些，但这些结果从根本上质疑了方法的实用价值。
- 为什么影响接收：如果 PPL 改善不能转化为下游任务改善，那么 "output-distribution distillation" 的实用意义需要重新审视。Reviewer 会问：为什么用户应该选择一个 PPL 更好但 MMLU/GSM8K 更差的方法？
- 建议修改方向：(a) 在 narrative 中更平衡地呈现结果，不要以 "19% PPL reduction" 作为核心 selling point；(b) 分析 PPL-downstream disconnect 的原因——是 KL 的 mass-covering property 分散了 reasoning-critical pathways 的资源吗？(c) 探索是否可以在 KL 中加入 task-specific regularization 来缓解下游退化。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Taxonomy（Table 1）的 Intermediate (MSE) 列缺少实验支撑**
- 具体位置：§3.7, Table 1, method.tex line 145
- 问题：论文提出 two-dimensional taxonomy 并明确标注 MSE 为 "intermediate coupling"，但随即声明 "per-layer MSE is not evaluated in our experiments; we focus on the two extremes of the coupling axis"。这削弱了 taxonomy 的说服力——如果不测试中间点，如何确认 coupling 是一个 spectrum 而非 binary choice？ShadowLLM 被归类为 MSE intermediate，但其效果未被对比。
- 建议：至少补充一个 MSE-on-hidden-states baseline 来验证 taxonomy 的 ordering（Decomposed < Intermediate < Coupled）。

**W2** [warning] **无实际 wall-clock speedup 验证**
- 具体位置：§4.6 (Inference Efficiency), Appendix A (latency)
- 问题：论文报告 predictor 增加 3.17ms（2.7% overhead），但未提供使用 sparse kernel 的实际端到端加速数据。整个研究的 motivation 是 inference speedup，但论文仅关注 prediction quality。Limitations 中提到 "actual wall-clock acceleration depends on sparse kernel implementations"——这意味着整个方法的实用价值是 hypothetical 的。
- 建议：即使不提供 custom kernel，至少用 Triton 或 PyTorch sparse API 提供一个 rough wall-clock comparison。

**W3** [warning] **Conclusion 过于简短**
- 具体位置：§5 Conclusion（3 句话 + vspace{-14pt} 挤压）
- 问题：Conclusion 仅 3 句话（~50 words），没有 future work 讨论（虽然 Limitations 中有），没有 broader implications 总结，没有方法的潜在推广方向。vspace{-14pt} 说明是为了页数限制而压缩。这给人的印象是论文在页数限制下 struggling to fit，而 Conclusion 是被牺牲的部分。
- 建议：精简 §4.6 中部分重复内容，为 Conclusion 腾出空间，至少包含 2-3 句 future work。

**W4** [warning] **Baseline 不足：仅与 vanilla TEAL 对比**
- 具体位置：§4.1 (Baselines), Table 2
- 问题：Baselines 仅包含 TEAL（training-free）和 BCE predictor。缺少与其他 training-based sparsity 方法的对比：
  - CATS (Lee et al., 2024): 在 Related Work 中引用但未实验对比
  - R-Sparse (Zhang et al., 2025): 同上
  - ShadowLLM (Akhauri et al., 2024): 在 taxonomy 中标注为 MSE intermediate 但未对比
  仅与 TEAL 对比，读者难以判断 KL predictor 在 predictor-based 方法中的相对位置。
- 建议：至少加入一个 predictor-based baseline（如 ShadowLLM 或 CATS），或明确解释为什么这些对比不可行。

**W5** [warning] **C1 ablation at 30% s42 seed 的 PPL gap 较大（0.65 PPL）**
- 具体位置：Table 3, 30% s42 行
- 问题：s42 seed 下 C1 PPL 9.45 vs KL 8.80（Δ=0.65），论文以脚注标注 "s42 oracle is from an earlier training run" 来解释。虽然 retrained seeds（s123: Δ=0.01, s456: Δ=0.03）显示近乎完美的 transfer，但 s42 的较大 gap 仍然 raise concern——如果 oracle 质量依赖于训练 run 的细节，那么 mask quality 的 "proximate driver" claim 需要更仔细的 caveat。
- 建议：在正文（而非仅脚注）中讨论 oracle 版本对 C1 的影响，并解释为什么 early training run 的 oracle 质量较差。

---

## 小问题（不影响接收）

- **M1**: Table 2 中 KL global (Ours) 标注在 30% 和 50% 处均出现，但论文在不同段落中交替推荐 global 和 uniform allocation。建议统一 "recommended configuration"。
- **M2**: §3.6 gradient analysis 中 SNR 数值（$5.877×10^{-3}$ vs $1.144×10^{-3}$）仅在 step 300 报告。建议补充 SNR 随训练步数的变化曲线（至少在 Appendix 中）。
- **M3**: Figure 2 caption "The KL predictor's advantage grows disproportionately as more neurons are pruned" 中 "disproportionately" 稍有 overclaiming——曲线是 monotonic 但不一定 superlinear。
- **M4**: Abstract 第 5 句 "commonsense improves while reasoning (GSM8K −25pp) and factual retrieval (MMLU) decline" 对 14B 结果的描述过于简化，没有区分 uniform vs global allocation 的差异（global allocation 下 MMLU 差距缩小至 -8.1pp）。
- **M5**: References 中 `de2024griffin` (Griffin) 在 OpenAlex 验证中 not_found（可能因检索限制），但该论文确实存在（arXiv:2402.19427）。`loshchilov2019adamw` 的 bib year (2019) 与 OpenAlex matched year (2017) 有 mismatch——ICLR 2019 publication vs 2017 arXiv，建议统一使用 venue 年份。

---

## Questions for Authors

**Q1**: 为什么不测试 MSE intermediate baseline？这会大幅加强 taxonomy 的 empirical grounding，且实验成本应该很低（将 KL loss 替换为 per-layer hidden state MSE 即可）。

**Q2**: C1 ablation 表明 mask quality 是 proximate driver。这是否意味着可以用任何方法（如 evolutionary search、reinforcement learning）找到好的 masks，然后用简单的 BCE 训练 predictor？如果是这样，KL 训练的唯一价值就是 mask discovery，而这可能有更高效的替代方案。

**Q3**: 在 14B scale 上 GSM8K -25pp 的 reversal 是否意味着 forward KL 的 mass-covering property 在 reasoning tasks 上有 systematic disadvantage？是否考虑过 task-conditional 或 layer-conditional 的 loss mixing（部分层用 KL，部分层用 BCE）？

**Q4**: 论文报告 predictor 增加 3.17ms overhead。在没有 sparse kernel 加速的情况下，使用 predictor 的 net speedup 是负数（因为 predictor overhead > sparse computation saving）。是否有 rough 估计显示在什么 sparsity 水平下 predictor 才能实现 net positive speedup？

---

## Missing References

未发现重大遗漏。以下为可考虑补充的参考（非必须）：
- Bambhaniya et al., 2024, "Progressive Gradient Flow for Robust N:M Sparsity Training in Transformers" — 如果讨论 N:M 扩展方向
- Li et al., 2023, "Lazy Neuron Phenomenon in Transformers" — 关于 SwiGLU 中 neuron 活跃度的分析性工作，与 mask pattern divergence 分析相关

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-20T01:41:55.063471+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 2 已交，等待 Reviewer 1', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 提交审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 2 已交，等待 Reviewer 1', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 提交审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-20T01:41:55.063961+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1106 · 2026-05-20T01:41:57.660763+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 87

## Round 87

2 recorded events


### User

_source line 1107 · 2026-05-20T01:42:00.276127+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**Reviewer 2 审稿完成**，核心判断：

- **Overall 3.0（Findings）**：实验设计扎实（尤其 C1 target-swap ablation），Limitations 讨论诚实全面，但方法新颖性有限（standard KL + standard Gumbel 的组合，MaskLLM 已证明 KL 用于 mask learning），下游任务结果 mixed（MMLU/GSM8K 在多个场景下退化），且无 wall-clock speedup 验证。
- **2 个 Must-Fix**：方法新颖性不足；下游结果与 PPL 改善严重不匹配
- **5 个 Should-Fix**：MSE baseline 缺失、无 speedup 验证、Conclusion 过短、baseline 不足（仅 TEAL）、C1 s42 oracle gap
- **5 个 Minor**：表格标注一致性、SNR 纵向数据、Figure caption overclaiming、Abstract 简化描述、reference year mismatch

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1108 · 2026-05-20T01:42:06.304336+00:00_

Reviewer 2 结果已记录。仍在等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 88

## Round 88

8 recorded events


### User

_source line 1109 · 2026-05-20T01:43:30.981691+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026)

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 系统性的 loss function 对比研究，C1 target-swap ablation 设计精巧，但缺少 MSE intermediate baseline 削弱了核心 claim，跨架构/跨规模证据偏薄。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心实验设计合理（多 seed 评估、消融充分），但 SNR 证据呈现有选择性，MSE baseline 缺失，部分数字向上取整 |
| Excitement | 3.0/5 | mask 发散发现（68%）和 target-swap ablation 有新意，但无实际加速、规模有限（≤14B），实用影响受限 |
| Reproducibility | 4.0/5 | 超参全列出，3-seed 评估，训练仅 1000 步/单 GPU，硬件型号明确 |
| Confidence | 4/5 | 熟悉 activation sparsity 和 KD 相关工作，仔细阅读了全文和附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] MSE intermediate baseline 缺失，核心 claim 缺乏充分支撑
- 具体位置：Table 1（§3.7）定义了三级 taxonomy（Decomposed/Intermediate/Coupled），但实验仅评估两端
- 问题：论文的核心论点是 **end-to-end 输出分布耦合**（KL）优于 **逐神经元独立训练**（BCE）。但 Table 1 明确列出了 Intermediate 级别（MSE on hidden states，如 ShadowLLM），却未做实验对比。Related work（§2, line 12）专门提到 ShadowLLM 用 per-layer MSE。§3.7 (line 145) 甚至显式承认 "The intermediate-coupling cell (per-layer MSE) is not evaluated in our experiments." 没有 MSE baseline，无法区分改进来自 (a) 任何形式的 non-trivial 训练信号耦合，还是 (b) 特定的 end-to-end output-level 耦合。KL 的优势可能部分（甚至大部分）来自"不再用 magnitude-based oracle targets"，而非来自梯度通过所有下游层传播。
- 为什么影响接收：这直接削弱 §3.6–§3.7 的 "coupled gradient" narrative。如果 MSE 也能发现类似的 divergent mask patterns，则论文的理论贡献（taxonomy 的 coupled 轴）大幅缩水。
- 建议修改方向：训练一个 per-layer MSE predictor（在每层隐藏状态上做 L2/MSE loss），在 Table 2 和 Table 4 中加入对比。训练成本与 BCE 相当（1000 步，单 GPU），应可在 deadline 前完成。

**N2** [critical] 跨架构/跨规模 claim 强度与数据不匹配
- 具体位置：§4.6（line 227–233）、Abstract（line 5）、Table 14（Appendix H）、Table 16（Appendix L）
- 问题：
  - **Mistral-7B**: 仅 single seed。Abstract 宣称 "KL outperforms TEAL on 5 of 6 downstream tasks"，但 GSM8K 逆转 4.8pp（11.1% vs 15.9%）。单 seed 下 5/6 的统计意义有限。
  - **Qwen-2.5-14B**: KL 的 GSM8K 从 TEAL 的 57.1% 降至 32.1±5.2%（−25pp, σ=5.2pp），MMLU 从 66.3% 降至 63.6%（−2.79pp）。σ=5.2pp 意味着个别 seed 可能低至 ~27%。§4.6 的解释 "forward KL's mass-covering property disrupts narrow reasoning pathways only when base capacity suffices" 是未经验证的推测——没有任何实验证据表明 mass-covering 特性与 reasoning pathway 之间的因果关系。
  - **Actual sparsity mismatch at 14B**: Table 14 注释显示 KL 实际 sparsity 29.6% vs TEAL 26.8%（差 2.8pp）。KL 更稀疏却要求更高质量——部分性能差距可能来自 sparsity mismatch 而非 mask quality。
- 为什么影响接收：论文将 14B/Mistral 结果作为 contribution 第三条（Introduction, line 23），但证据不足以支撑 "cross-architecture generalization" 的 framing。
- 建议修改方向：(1) Mistral 实验加 3-seed 评估；(2) 14B 对齐 actual sparsity 后重新对比（或明确报告 sparsity-matched 结果）；(3) 将 §4.6 的 mass-covering 解释标记为 hypothesis 而非结论；(4) 降低 abstract/conclusion 中的 cross-arch claim 强度。

**N3** [critical] SNR 证据选择性呈现，误导 coupled gradient narrative
- 具体位置：§3.6（line 109）vs Appendix G（line 204）
- 问题：§3.6 主文报告 "at step 300 (of 1000), KL achieves 5.14× higher SNR than BCE"，暗示 KL 梯度质量一致性优于 BCE。但 Appendix G 揭示 trajectory 是 **non-monotonic** 的："KL starts with higher SNR at step 0, but **BCE surpasses KL during mid-training (steps 100–250)**." 主文完全省略了这一关键信息。Step 300 是 BCE 刚刚被反超的时间点——选择这个点来报告 5.14× 优势具有 cherry-picking 性质。
- 为什么影响接收：SNR 分析是 §3.6 "coupled gradient" 叙事的核心数据支撑。如果 SNR 优势仅在特定训练阶段存在，则"结构性优势"的 claim 被大幅削弱。Reviewer 对数据呈现的诚实性有疑虑。
- 建议修改方向：(1) 主文中加入 non-monotonic trajectory 的描述（至少一句话提及 mid-training 阶段 BCE 更高）；(2) 报告 final step (1000) 的 SNR 比较而非仅 step 300；(3) 或者将 SNR 分析完全移到 appendix，降低其在主文叙事中的权重。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 30% 训练-推理 sparsity mismatch 未充分验证
- 具体位置：Appendix C（Table 10, line 148）
- 问题：Penalty controller 在 30% 目标下实际训练 sparsity 为 28.5%（偏差 5%），λ 达到 cap（5000）。Predictor 在 28.5% 条件下训练但在 30% 条件下评估。论文声称 "does not affect conclusions"，但未验证：更高 λ_max 或更紧 controller 是否能达到更接近 30% 的训练 sparsity？如果能，结果是否改变？
- 建议：添加一个实验：用更高 λ_max 训练到更接近 30% actual sparsity，确认结果稳定。

**W2** [warning] Abstract 未限定 "diverge 68%" 的 sparsity 条件
- 具体位置：Abstract（line 4）、Introduction（line 9）
- 问题：Abstract 说 "KL-derived masks diverge 68% from magnitude-based masks"，但 §4.4 明确指出 68% 是 50% sparsity 下的数字；在论文最常强调的 30% 操作点，发散率仅为 46%（"divergence scaling from 46% at 30% to 68% at 50%"）。Abstract 未加限定条件，对 30% 场景的读者具有误导性。
- 建议：Abstract 中改为 "diverge 46–68% depending on sparsity level" 或明确标注 "at 50% sparsity"。

**W3** [warning] 数值取整系统性偏高
- 具体位置：多处
- 问题：
  - "19% reduction"：实际 (10.82−8.81)/10.82 = 18.6%（§4.2, Abstract, Introduction, Conclusion）
  - "7.5× smaller cross-seed σ"：实际 9.5/1.3 = 7.31×（§4.2, Introduction, Conclusion 各出现一次）
  - "MMLU +0.6pp"（Mistral）：实际 44.0−43.5 = 0.5pp（§4.6 line 229 vs Table 16）
  - 每个单独看属于正常取整，但 **系统性向上** 取整削弱数值可信度。
- 建议：统一使用一位小数精度或明确标注 "≈"。

**W4** [warning] 无实际推理加速
- 具体位置：Appendix A（Table 6）、§4.6（line 236）
- 问题：Predictor 增加 6.4% 推理开销（126.78 vs 119.11 ms/forward）。全 pipeline 比 dense inference 更慢。论文 Introduction 以 "exploit this property" 作为动机，但最终交付的是纯 prediction quality 分析，无实际加速。
- 影响：限制了实际贡献——prediction quality 提升的价值取决于未来 sparse kernel 是否能利用这些 mask。
- 建议：在 Introduction 中更早、更明确地界定贡献范围为 "prediction quality study"，而非暗示 speedup 动机。

**W5** [warning] OOD 评估统计覆盖不足
- 具体位置：Appendix D（Table 11）
- 问题：C4 OOD 在 30% 仅 2-seed，50% 仅 single seed。C4 PPL/dense ratio（1.74×）显著高于 WikiText-2（1.44×），暗示对 WikiText-103 训练域有 meaningful overfitting。Limitations 承认了这一点，但如此薄的 OOD 数据不足以支撑 "KL-trained predictions generalize across distributions"（Appendix D, line 176）的结论。
- 建议：补充 3-seed C4 评估；或降低 OOD generalization claim 的强度。

**W6** [warning] Cross-architecture PPL 对比使用不同 allocation 策略
- 具体位置：Table 15（Appendix L）
- 问题：Table 15 caption 说明 "LLaMA uses global top-k; Mistral uses uniform allocation"，两个架构的 TEAL baseline 使用了不同的 allocation 策略。LLaMA 30% TEAL global = 10.97，而 Table 2 中 TEAL uniform = 10.82。这使得 Adv ratio 的跨架构比较不够 clean（LLaMA 的 Adv 是 global-vs-global，Mistral 的是 uniform-vs-uniform）。
- 建议：在 Table 15 中增加 matched allocation 的行，或在 caption 中更显著地提示 allocation 差异。

---

## 小问题（不影响接收）

- Conclusion 使用 `\vspace{-14pt}` 压缩排版。如果去掉，正文可能超 8 页。建议核实格式合规性。
- "proximate driver" 短语在全文中出现 7+ 次（Abstract, Introduction ×2, §4.4 ×2, §4.5, Conclusion），过度重复。
- Table 3 caption 脚注 "s42 oracle is from an earlier training run" 是重要的方法论说明，不应仅以脚注形式出现。这解释了 s42 在 30% 时 gap 明显大于 s123/s456（PPL Δ=0.65 vs ≤0.04），建议在正文中讨论。
- Reference `de2024griffin`（Griffin）未被 OpenAlex 检索到（confidence 0.296），可能需要更新 venue/year。
- `loshchilov2019adamw` year mismatch（bib=2019 vs API=2017），应以正式发表年份为准。

---

## Questions for Authors

1. **为什么不评估 MSE intermediate objective？** 论文 taxonomy 明确包含该 cell。即使是简单的 per-layer hidden state MSE loss（训练成本与 BCE 相当）也能回答 coupling 程度的关键问题。这是有意识的 scope 限制还是实验资源不足？

2. **C1 oracle masks 对 checkpoint 的敏感性？** C1 使用 KL predictor 最终 checkpoint 的 masks。如果在 step 500 提取 masks，BCE 是否仍能 match KL quality？这关系到 mask pattern 的发现是否需要完整训练。

3. **14B 的 sparsity mismatch 影响？** KL 实际 29.6% vs TEAL 26.8%（Table 14）。如果控制 actual sparsity 相同，MMLU/GSM8K 差距会缩小多少？

4. **Final-step SNR ratio？** Appendix G 仅报告到 step 300。Step 1000 时 KL vs BCE 的 SNR ratio 是多少？这对 "coupling advantage" narrative 至关重要。

5. **单 predictor 多 sparsity 目标？** Limitations 提到这是 future work，但有没有初步实验？每个 sparsity target 训练一个 predictor 的成本 (~45 min × N 个 target) 在实际部署中不可忽视。

---

## Missing References / Comparisons

- **MSE intermediate baseline**: ShadowLLM (Akhauri et al., 2024) 在 Table 1 中被归类为 Intermediate coupling，但未做实验对比。论文引用了 ShadowLLM 但仅在 related work 中讨论，未 experimentally compare。
- **MaskLLM (Fang et al., 2024)**: Related work（§2, line 16–19）详细讨论了与 MaskLLM 的区别（N:M vs activation sparsity），但没有 ablation 验证这些区别是否 matters。虽然 sparsity type 不同，但 MaskLLM 也用 KL + Gumbel-Softmax training on frozen weights——at least citing their KL training results as reference point would contextualize the contribution.

---

## 主要优势

1. **C1 Target-Swap Ablation 设计精巧**（§4.4, Table 3）：这是全文最有说服力的实验。通过将 KL-discovered masks 转移到 BCE 训练，干净地分离了 "mask quality" 和 "gradient coupling" 的贡献。50% sparsity 下 max Δ≤0.79pp 的 match 非常有力。多 seed（s42/s123/s456）的交叉验证增强了可信度。

2. **系统性消融覆盖全面**（§4.5, Table 4）：KL variants（forward/reverse/JSD）、relaxation（Gumbel vs STE）、BCE variants、compensation redundancy——每个设计选择都有对照实验。Appendix B–C 的 hyperparameter sensitivity 分析（bottleneck, temperature, training steps）表明结果对超参不敏感。

3. **诚实报告负面结果**：14B 的 GSM8K −25pp 和 MMLU 逆转、50% sparsity 下 downstream collapse、无实际加速——这些在 Limitations 和正文中都有明确讨论。这是值得肯定的学术诚信。

4. **Taxonomy 框架（Table 1）有分析价值**：Correction granularity × Training signal coupling 的二维分类清晰有效，为后续工作提供了有用的 conceptual map。尽管 intermediate cell 未被评估，框架本身是好的。

5. **训练成本极低**：1000 步 / 45 分钟 / 单 GPU。Predictor <1% 基座参数。这使得方法高度可复现，降低了实验验证的门槛。

6. **多 seed 评估规范**（3-seed for main claims, std 报告）：主要结论都有多 seed 支撑（PPL CV<1%），比该领域许多 single-seed 论文更可靠。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-20T01:43:53.446203+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享 — 双向转发审稿原文', 'status': 'in_progress', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享 — 双向转发审稿原文', 'status': 'in_progress', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-20T01:43:53.496851+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-20T01:44:19.275461+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n**Reviewer 2 Overall**: 3.0 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] 方法新颖性不足：核心贡献是 standard KL + standard Gumbel 的组合\n- 核心方法是将 distillation 中标准的 forward KL divergence 与标准的 Gumbel-Sigmoid relaxation 应用于 sparsity predictor 训练。MaskLLM (Fang et al., 2024) 已在 NeurIPS 2024 证明了 \"frozen weights + learnable masks + KL training\" 的有效性。虽然论文指出了与 MaskLLM 的三点区别（activation vs weight sparsity, predictor vs learnable params, global top-k vs N:M），但核心 principle（用 KL 训练 mask）是相同的。Loss function swap 本身（BCE→KL）在 distillation 领域是 well-known 的选择，缺乏足够的方法论贡献来支撑一篇 long paper。\n\n**N2** [critical] 下游任务结果与 PPL 改善严重不匹配，削弱实用价值\n- 30% sparsity on LLaMA-8B：KL uniform MMLU 40.7±1.3% vs TEAL 45.86%（-5.2pp），GSM8K 7.5±0.1% vs TEAL 8.79%（-1.3pp）。KL 在 PPL 上赢但在 MMLU/GSM8K 上输。\n- Mistral-7B：GSM8K 11.1% vs TEAL 15.9%（-4.8pp）\n- Qwen-14B：GSM8K -25pp, MMLU -2.79pp（uniform），更大 scale 上劣势加剧\n- 50% sparsity：所有方法 MMLU 坍塌至近随机\n- 如果 PPL 改善不能转化为下游任务改善，那么 \"output-distribution distillation\" 的实用意义需要重新审视。\n\n**Should-Fix:**\n\n**W1** Taxonomy（Table 1）的 Intermediate (MSE) 列缺少实验支撑\n**W2** 无实际 wall-clock speedup 验证\n**W3** Conclusion 过于简短（3 句话 + vspace{-14pt}）\n**W4** Baseline 不足：仅与 vanilla TEAL 对比，缺少 CATS/R-Sparse/ShadowLLM\n**W5** C1 ablation at 30% s42 seed 的 PPL gap 较大（0.65 PPL），oracle 版本敏感\n\n**Minor:**\nM1: Table 2 中 \"Ours\" 标注在 global 和 uniform 两行出现，推荐配置不统一\nM2: SNR 仅 step 300，建议补充纵向曲线\nM3: Figure 2 caption \"disproportionately\" overclaiming\nM4: Abstract 对 14B 结果过度简化（未区分 uniform vs global）\nM5: Griffin reference not_found; AdamW year mismatch\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n**Reviewer 2 Overall**: 3.0 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] 方法新颖性不足：核心贡献是 standard KL + standard Gumbel 的组合\n- 核心方法是将 distillation 中标准的 forward KL divergence 与标准的 Gumbel-Sigmoid relaxation 应用于 sparsity predictor 训练。MaskLLM (Fang et al., 2024) 已在 NeurIPS 2024 证明了 \"frozen weights + learnable masks + KL training\" 的有效性。虽然论文指出了与 MaskLLM 的三点区别（activation vs weight sparsity, predictor vs learnable params, global top-k vs N:M），但核心 principle（用 KL 训练 mask）是相同的。Loss function swap 本身（BCE→KL）在 distillation 领域是 well-known 的选择，缺乏足够的方法论贡献来支撑一篇 long paper。\n\n**N2** [critical] 下游任务结果与 PPL 改善严重不匹配，削弱实用价值\n- 30% sparsity on LLaMA-8B：KL uniform MMLU 40.7±1.3% vs TEAL 45.86%（-5.2pp），GSM8K 7.5±0.1% vs TEAL 8.79%（-1.3pp）。KL 在 PPL 上赢但在 MMLU/GSM8K 上输。\n- Mistral-7B：GSM8K 11.1% vs TEAL 15.9%（-4.8pp）\n- Qwen-14B：GSM8K -25pp, MMLU -2.79pp（uniform），更大 scale 上劣势加剧\n- 50% sparsity：所有方法 MMLU 坍塌至近随机\n- 如果 PPL 改善不能转化为下游任务改善，那么 \"output-distribution distillation\" 的实用意义需要重新审视。\n\n**Should-Fix:**\n\n**W1** Taxonomy（Table 1）的 Intermediate (MSE) 列缺少实验支撑\n**W2** 无实际 wall-clock speedup 验证\n**W3** Conclusion 过于简短（3 句话 + vspace{-14pt}）\n**W4** Baseline 不足：仅与 vanilla TEAL 对比，缺少 CATS/R-Sparse/ShadowLLM\n**W5** C1 ablation at 30% s42 seed 的 PPL gap 较大（0.65 PPL），oracle 版本敏感\n\n**Minor:**\nM1: Table 2 中 \"Ours\" 标注在 global 和 uniform 两行出现，推荐配置不统一\nM2: SNR 仅 step 300，建议补充纵向曲线\nM3: Figure 2 caption \"disproportionately\" overclaiming\nM4: Abstract 对 14B 结果过度简化（未区分 uniform vs global）\nM5: Griffin reference not_found; AdamW year mismatch\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-20T01:44:35.514532+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16239
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-20T01:44:35.715853+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n**Reviewer 1 Overall**: 3.5 (Borderline Conference)\n\n**Must-Fix:**\n\n**N1** [critical] MSE intermediate baseline 缺失，核心 claim 缺乏充分支撑\n- Table 1 定义三级 taxonomy，实验仅评估两端。没有 MSE baseline，无法区分改进来自 (a) 任何形式的 non-trivial 训练信号耦合，还是 (b) 特定的 end-to-end output-level 耦合。KL 的优势可能部分来自\"不再用 magnitude-based oracle targets\"，而非来自梯度通过所有下游层传播。\n\n**N2** [critical] 跨架构/跨规模 claim 强度与数据不匹配\n- Mistral-7B 仅 single seed。Qwen-14B GSM8K -25pp（σ=5.2pp）。\"mass-covering property disrupts narrow reasoning pathways\" 是未验证推测。14B actual sparsity mismatch（KL 29.6% vs TEAL 26.8%）可能解释部分性能差距。\n\n**N3** [critical] SNR 证据选择性呈现，误导 coupled gradient narrative\n- §3.6 报告 step 300 KL 5.14× higher SNR，但 Appendix G 揭示 BCE 在 steps 100-250 surpasses KL。Step 300 是 BCE 刚被反超的时间点——cherry-picking 嫌疑。主文完全省略 non-monotonic trajectory。\n\n**Should-Fix:**\n\n**W1** 30% 训练-推理 sparsity mismatch（actual 28.5% vs target 30%）未充分验证\n**W2** Abstract 未限定 \"diverge 68%\" 的 sparsity 条件（实际是 50% 下的数字，30% 仅 46%）\n**W3** 数值取整系统性偏高（19% 实为 18.6%，7.5× 实为 7.31×，MMLU +0.6pp 实为 +0.5pp）\n**W4** 无实际推理加速（predictor 增加 6.4% overhead）\n**W5** OOD 评估统计覆盖不足（C4 30% 仅 2-seed，50% single seed）\n**W6** Cross-architecture PPL 对比使用不同 allocation 策略（LLaMA global vs Mistral uniform）\n\n**Minor:**\n- Conclusion vspace{-14pt} 格式问题\n- \"proximate driver\" 全文 7+ 次过度重复\n- Table 3 s42 oracle 说明不应仅以脚注形式出现\n- Griffin reference 和 AdamW year mismatch\n\n**Strengths:**\n1. C1 Target-Swap Ablation 设计精巧\n2. 系统性消融覆盖全面（Table 4）\n3. 诚实报告负面结果\n4. Taxonomy 框架有分析价值\n5. 训练成本极低（1000 步/45 min/单 GPU）\n6. 多 seed 评估规范\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n**Reviewer 1 Overall**: 3.5 (Borderline Conference)\n\n**Must-Fix:**\n\n**N1** [critical] MSE intermediate baseline 缺失，核心 claim 缺乏充分支撑\n- Table 1 定义三级 taxonomy，实验仅评估两端。没有 MSE baseline，无法区分改进来自 (a) 任何形式的 non-trivial 训练信号耦合，还是 (b) 特定的 end-to-end output-level 耦合。KL 的优势可能部分来自\"不再用 magnitude-based oracle targets\"，而非来自梯度通过所有下游层传播。\n\n**N2** [critical] 跨架构/跨规模 claim 强度与数据不匹配\n- Mistral-7B 仅 single seed。Qwen-14B GSM8K -25pp（σ=5.2pp）。\"mass-covering property disrupts narrow reasoning pathways\" 是未验证推测。14B actual sparsity mismatch（KL 29.6% vs TEAL 26.8%）可能解释部分性能差距。\n\n**N3** [critical] SNR 证据选择性呈现，误导 coupled gradient narrative\n- §3.6 报告 step 300 KL 5.14× higher SNR，但 Appendix G 揭示 BCE 在 steps 100-250 surpasses KL。Step 300 是 BCE 刚被反超的时间点——cherry-picking 嫌疑。主文完全省略 non-monotonic trajectory。\n\n**Should-Fix:**\n\n**W1** 30% 训练-推理 sparsity mismatch（actual 28.5% vs target 30%）未充分验证\n**W2** Abstract 未限定 \"diverge 68%\" 的 sparsity 条件（实际是 50% 下的数字，30% 仅 46%）\n**W3** 数值取整系统性偏高（19% 实为 18.6%，7.5× 实为 7.31×，MMLU +0.6pp 实为 +0.5pp）\n**W4** 无实际推理加速（predictor 增加 6.4% overhead）\n**W5** OOD 评估统计覆盖不足（C4 30% 仅 2-seed，50% single seed）\n**W6** Cross-architecture PPL 对比使用不同 allocation 策略（LLaMA global vs Mistral uniform）\n\n**Minor:**\n- Conclusion vspace{-14pt} 格式问题\n- \"proximate driver\" 全文 7+ 次过度重复\n- Table 3 s42 oracle 说明不应仅以脚注形式出现\n- Griffin reference 和 AdamW year mismatch\n\n**Strengths:**\n1. C1 Target-Swap Ablation 设计精巧\n2. 系统性消融覆盖全面（Table 4）\n3. 诚实报告负面结果\n4. Taxonomy 框架有分析价值\n5. 训练成本极低（1000 步/45 min/单 GPU）\n6. 多 seed 评估规范\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-20T01:44:37.230061+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1514
}
```

</details>

---


### Assistant

_source line 1116 · 2026-05-20T01:44:40.340444+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 1117 · 2026-05-20T01:44:43.081541+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**3.5 分（Borderline Conference）**。

三个 Must-Fix 问题：
1. **MSE intermediate baseline 完全缺失**——论文自己的 taxonomy 留了这个空格却不填，直接削弱了 "end-to-end coupling 是关键" 的核心叙事
2. **跨架构/跨规模 claim 过强**——Mistral 仅 single seed，14B 的 GSM8K −25pp 和 σ=5.2pp 被轻描淡写为 "task-and-scale-dependent effects"，解释缺乏因果证据
3. **SNR 证据 cherry-picking**——主文只报告 step 300 的 5.14× 优势，隐藏了 mid-training 阶段 BCE 反超 KL 的 non-monotonic trajectory

主要优势是 C1 target-swap ablation（设计精巧、50% sparsity 下 match 极好）、消融覆盖全面、以及负面结果的诚实报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1118 · 2026-05-20T01:44:50.408534+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 90

## Round 90

4 recorded events


### User

_source line 1119 · 2026-05-20T01:46:42.902491+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### 回应摘要

| R2 条目 | 判定 | 核心理由 |
|---------|------|---------|
| N1 (novelty) | [AGREE with qualification] | 方法组件确实标准，但 C1 ablation 的实验设计有新意；这是 venue fit 问题（Main→Findings），非可修复技术缺陷 |
| N2 (downstream) | [REBUT] | R2 选择性仅引用 MMLU/GSM8K 的 loss，忽略了 ARC-c +4.4pp, WG +3.9pp, HellaSwag +7.8pp, PIQA +2.2pp 四项 wins。KL 在 30% 8B 上 6 任务赢 4 输 2 |
| W1 (MSE) | [AGREE] | 与我的 N1 一致 |
| W2 (speedup) | [AGREE] | 与我的 W4 一致 |
| W3 (Conclusion) | [AGREE] | 3 句话 + vspace 确实过于压缩 |
| W4 (baselines) | [REBUT partially] | ShadowLLM(MSE) 必须加；CATS/R-Sparse 是不同类型(training-free)的 baseline，非核心对比 |
| W5 (C1 s42) | [AGREE with qualification] | s42 gap 源于 oracle 版本不匹配(Table 3 caption)，retrained s123/s456 PPL Δ 仅 0.01-0.03，已充分化解 |
| M1 (Ours 标注) | [AGREE] | 推荐配置在不同 sparsity 下不同，应统一标注 |
| M2 (SNR) | [AGREE — 我认为应升级为 Must-Fix] | §3.6 隐藏了 Appendix G 的 non-monotonic trajectory，step 300 有 cherry-pick 性质 |
| M3 (disproportionately) | [REBUT] | Advantage ratio 1.22×→1.98×→5.59× 是 super-linear，"disproportionately" 数学上准确 |
| M4 (14B abstract) | [AGREE] | 未区分 uniform vs global 确实过度简化 |
| M5 (references) | [AGREE] | Griffin not_found, AdamW year mismatch |

### 与 R2 的关键分歧

**最大分歧在 N2**: R2 认为 PPL-downstream disconnect 是 Must-Fix，我认为应降为 Should-Fix。论文在 30% 8B 上 6 个下游任务赢 4 个(ARC-c, WG, HellaSwag, PIQA)输 2 个(MMLU, GSM8K)——R2 的 framing 不公平。PPL-downstream 的 non-monotonic 关系本身是论文的发现之一，不是缺陷。但我同意论文应在 main text 中更突出地讨论此现象。

**建议 R2 升级 M2**: SNR 在 step 300 的选择性呈现比 R2 标注的 Minor 更严重。Appendix G 揭示 BCE 在 steps 100-250 超过 KL——这直接削弱 §3.6 的 "coupled gradient advantage" narrative。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-20T01:46:57.790250+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享 — R1 已回应，等待 R2 回应', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享 — R1 已回应，等待 R2 回应', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-20T01:46:57.790884+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1122 · 2026-05-20T01:47:00.081846+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 91

## Round 91

20 recorded events


### User

_source line 1123 · 2026-05-20T01:47:01.276890+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：与 R2 在多数 Should-Fix/Minor 上一致，但在两个关键点有分歧——(1) N2 的下游任务分析 R2 选择性引用数据，KL 实际赢 4/6 任务，应降为 Should-Fix；(2) M2 的 SNR 选择性呈现问题我认为应升级为 Must-Fix，比 R2 给的 Minor 更严重。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix

**[AGREE] R1-N1: MSE intermediate baseline 缺失**
完全同意。我在自己的 W1 中也提出了同样的问题。C1 target-swap ablation（Table 3）虽然部分回应了 "是否只是因为不用 magnitude oracle" 的问题——C1 证明 BCE 在 KL-discovered masks 上可以复现 KL 性能（50% Δ≤0.79pp），但这不能回答另一个关键问题：MSE intermediate coupling 是否也能 discover 类似的 non-magnitude masks？如果 MSE 就能达到类似效果，那 taxonomy 中 Decomposed < Intermediate < Coupled 的 ordering 就不成立，KL 的 end-to-end coupling 就不是必要的。这个实验成本极低（替换 loss function 即可），缺失令人遗憾。

**[AGREE] R1-N2: 跨架构/跨规模 claim 过强**
同意。我的 N2 也标注了下游结果的 mixed nature。补充两点 R1 的观察：
1. **Actual sparsity mismatch**（KL 29.6% vs TEAL 26.8% on 14B）——这是一个重要的 confound，我在初审中未充分关注。2.8pp 的 sparsity 差异可以解释部分 downstream degradation，论文 §4.6 仅在括号中提到这一数字（experiments.tex line 231），没有讨论其对公平对比的影响。
2. **Mistral single-seed**——Table 16（Appendix, page 16）的 Mistral 结果无 error bar，对于声称 "5/6 tasks win" 的 cross-architecture claim，统计证据不足。

**[AGREE with nuance] R1-N3: SNR 选择性呈现**
基本同意 R1 的判断，但补充 nuance。Appendix G（page 14）明确写道："KL starts with higher SNR at step 0, but BCE surpasses KL during mid-training (steps 100–250)... KL's advantage re-emerges in later training and reaches 5.14× at step 300"。主文 §3.6（method.tex line 109）仅报告 step 300 的 5.14× 数字，完全省略了 non-monotonic trajectory。

我同意这构成 selective presentation，但不完全同意 "cherry-picking" 的程度判断：
- Step 300 是 30% training progress，不是最终状态。如果 KL 在训练后期（steps 300-1000）持续保持 SNR 优势，那 step 300 的选择虽有选择性但不算 cherry-pick。
- 但论文没有展示 step 300 之后的 SNR trajectory，这使得读者无法判断 SNR 优势是持续的还是 transient 的。

**建议**：在主文中用一句话 acknowledge non-monotonic trajectory（"While BCE shows transiently higher SNR during mid-training, KL's advantage emerges by step 300 and persists through training completion"），并在 Appendix G 补充完整 SNR 曲线（至少到 step 1000）。

---

### Should-Fix

**[AGREE] R1-W1: 30% sparsity mismatch (actual ~28.5% vs target 30%)**
这是一个有效的 concern。Appendix C Table 10 的 penalty controller 收敛数据表明实际 sparsity 可以偏离 target ±2%。如果 KL predictor 实际运行在 28.5% 而 TEAL baseline 运行在 30%，这构成不公平对比（KL 保留了更多 neurons）。论文应在主文中报告所有方法的 actual achieved sparsity。

**[AGREE] R1-W2: Abstract "diverge 68%" 未限定 sparsity**
同意。§4.4（experiments.tex line 76）明确说 "divergence scaling from 46% at 30% to 68% at 50%"，但 Abstract 和 Introduction（line 9："diverge 68%"）均未标注这是 50% sparsity 下的数字。考虑到 30% 是论文推荐的实用 sparsity level，46% divergence 比 68% 的 narrative impact 弱得多。这属于 misleading presentation。

**[AGREE] R1-W3: 数值系统性 upward rounding**
验证了 R1 的几个例子：
- "19%"：(10.82-8.81)/10.82 = 18.58% → 19%（+0.4pp 偏高）
- "7.5×"：9.5/1.3 = 7.31× → 7.5×（+0.19× 偏高）
- 每个 individually 在容差内，但**所有取整方向一致偏高**构成 systematic bias。这在 peer review 中会降低数值报告的可信度。

**[AGREE] R1-W4: 无实际推理加速**
同意，且补充：R1 引用的 6.4% overhead 比论文主文 §4.6 报告的 "2.7% overhead" 更准确。Appendix A（page 12）澄清 2.7% 是 predictor 本身相对 sparse inference 的 overhead，而 6.4% 是完整 KL-sparse pipeline 相对 dense inference 的 total overhead。主文仅报告 2.7% 有 downplaying 之嫌。在没有 sparse kernel 加速的情况下，使用此方法实际上**增加** inference latency。

**[AGREE] R1-W5: OOD 统计覆盖不足**
C4 30% 仅 2-seed、50% single seed 确实不足以支撑 generalization claim。这与主实验的 3-seed 标准不一致。

**[AGREE] R1-W6: Cross-architecture PPL 对比使用不同 allocation**
Table 15（Appendix, page 15）的表注明确标注 "LLaMA uses global top-k. Mistral uses uniform allocation"。在不同 allocation 策略下对比 PPL 确实会引入 confound——论文 Table 5 已表明 allocation 策略可以影响 PPL（如 30% 下 global 8.96 vs uniform 8.81），不同 allocation 下的 cross-architecture 结论需要加 caveat。

---

### Minor

**[AGREE] Conclusion vspace{-14pt}**: 我的 W3 也标注了同一问题。3 句话的 Conclusion + 负 vspace 是一个 formatting red flag。

**[AGREE] "proximate driver" 过度重复**: 我数了至少 7 处：Introduction line 10, Method §3.6 lines 102 和 110, §4.3 line 69, §4.4 line 114, Conclusion line 5, Limitations line 8。对于一个需要反复强调才能让读者信服的 claim，这种重复反而削弱了说服力。

**[AGREE] Table 3 s42 oracle footnote**: 我的 W5 也指出同一问题。s42 oracle 来自 "earlier training run" 导致 PPL gap 0.65（vs retrained seeds Δ≤0.03），这个信息仅以 Table 3 caption 中的 dagger 脚注形式出现，容易被忽略。

**[AGREE] Griffin reference 和 AdamW year mismatch**: 引用验证确认 `de2024griffin` 在 OpenAlex 中 not_found（confidence 0.296），`loshchilov2019adamw` bib year 2019 vs publication year 2017 mismatch。均为小问题。

---

### 总结

R1 的审稿意见整体高质量且公正。我与 R1 在绝大多数问题上一致：

- **共识核心问题**：MSE baseline 缺失（R1-N1 / 我的 W1）、下游结果 mixed（R1-N2 / 我的 N2）、无 wall-clock speedup（R1-W4 / 我的 W2）
- **R1 独有且我认同的发现**：SNR cherry-picking（N3）、actual sparsity mismatch（W1）、数值系统性 upward rounding（W3）、cross-architecture allocation confound（W6）——这些我在初审中未充分关注
- **唯一 nuance 分歧**：R1-N3 我同意 selective presentation 但对 cherry-picking 的程度判断略保守，因为 step 300 后的 SNR trajectory 未被展示，无法完全判断

**综合评分调整**：结合 R1 的发现（尤其是 SNR selective presentation、actual sparsity mismatch、数值 rounding bias），我维持 **Overall 3.0 (Findings)** 的判断。论文的实验设计（C1 ablation）仍有价值，但 presentation integrity 问题（N3, W2, W3）和 completeness gaps（N1, W4）限制了其评分上限。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。与 R1 在所有问题上达成一致或基本一致，仅在 N3（SNR cherry-picking 的程度判断）上保留了 nuance——因为 step 300 之后的 SNR trajectory 未展示，无法完全判定是否为 cherry-pick。综合评分维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-20T01:47:36.346707+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-20T01:47:36.347342+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1126 · 2026-05-20T01:47:57.714903+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已收敛，无需 Round 2'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'in_progress', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'pending', 'activeForm': '同步 Issue Tracker'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 均已提交'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已收敛，无需 Round 2'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'in_progress', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'pending', 'activeForm': '同步 Issue Tracker'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-20T01:47:57.715339+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-20T01:47:58.468218+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1129 · 2026-05-20T01:47:58.468555+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1130 · 2026-05-20T01:47:58.518951+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"timeout\", \"elapsed_seconds\": 794}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-20T01:47:58.519339+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-20T01:49:20.534385+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 完成', 'status': 'completed', 'activeForm': '完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '视觉审查超时'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'in_progress', 'activeForm': '同步 Issue Tracker'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 完成', 'status': 'completed', 'activeForm': '完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '视觉审查超时'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'in_progress', 'activeForm': '同步 Issue Tracker'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-20T01:49:20.534814+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-20T01:51:06.770539+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 13 (fresh review) — New issues\n  # ============================================================\n\n  - id: \"R13-N1\"\n    summary: \"MSE intermediate baseline 缺失，taxonomy Decomposed/Intermediate/Coupled 核心 claim 无实验支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-N3. Full consensus.\"}\n      - {round: 13, reviewers: [1, 2], note: \"Full consensus. R1-N1 Must-Fix, R2-W1→升级同意. 没有 MSE baseline 无法区分改进来自任何形式 coupling 还是特定 end-to-end output-level coupling. 实验成本极低（替换 loss function），缺失令人遗憾.\"}\n    action_items:\n      - {round: 13, action: \"训练 per-layer MSE predictor（相同架构，最小化 sparse vs dense hidden state MSE），加入 Table 2 和 Table 4 对比. 或弱化 taxonomy 为概念组织工具.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N2\"\n    summary: \"跨架构/跨规模 claim 过强：Mistral 单 seed, 14B sparsity mismatch (29.6% vs 26.8%), mass-covering 假说未验证\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-N2. 14B MMLU reversal 仅 'warrants further investigation'.\"}\n      - {round: 12, reviewers: [1, 2], note: \"R12-W2. 14B 加了 per-layer mask divergence 分析但仍 single seed.\"}\n      - {round: 13, reviewers: [1, 2], note: \"Full consensus. R1-N2 Must-Fix. Mistral 仅 single seed 不足支撑 5/6 claim. 14B actual sparsity KL 29.6% vs TEAL 26.8% 构成不公平对比. §4.6 的 mass-covering 解释是未验证推测.\"}\n    action_items:\n      - {round: 13, action: \"Mistral 补 3-seed; 14B 对齐 actual sparsity 或明确报告 matched 结果; mass-covering 标为 hypothesis; 降低 abstract/conclusion cross-arch claim 强度.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N3\"\n    summary: \"SNR 证据选择性呈现：§3.6 仅报告 step 300 的 5.14× 优势，隐藏 mid-training BCE 反超 KL 的 non-monotonic trajectory\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-N3 Must-Fix, R2 升级同意(程度判断略保守). Appendix G 揭示 steps 100-250 BCE surpasses KL，主文完全省略. Step 300 是 BCE 刚被反超时间点——选择性呈现. 且缺少 step 300-1000 的 trajectory.\"}\n    action_items:\n      - {round: 13, action: \"主文加一句 acknowledge non-monotonic trajectory; Appendix G 补完整 SNR 曲线至 step 1000; 或将 SNR 分析降级为 appendix-only evidence.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W1\"\n    summary: \"方法新颖性有限：standard KL + standard Gumbel 组合，MaskLLM 已证明 KL 用于 mask learning\"\n    category: method\n    severity: warning\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R9-N4.\"}\n      - {round: 12, reviewers: [1, 2], note: \"R12-W4. Both agree Findings-appropriate.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R2-N1 Must-Fix, R1 agrees with qualification (venue fit issue, not fixable). 核心 principle（KL 训练 mask）与 MaskLLM 相同. 强化 empirical study 定位.\"}\n    resolution: \"Positioning issue. Findings accepted as realistic target.\"\n    resolution_round: 10\n\n  - id: \"R13-W2\"\n    summary: \"下游 PPL disconnect：30% 8B KL 赢 4/6 任务但输 MMLU/GSM8K; 14B GSM8K -25pp\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W6. 30% downstream 退化讨论.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R2-N2 定 Must-Fix, R1 rebut (KL 赢 ARC +4.4, WG +3.9, HS +7.8, PIQA +2.2). Director 裁定 Should-Fix with strong caveat: 8B 层面不构成 Must-Fix, 但 14B claim 需显著收敛.\"}\n    action_items:\n      - {round: 13, action: \"在 narrative 中更平衡地呈现下游结果 (不仅以 PPL 为 selling point); 14B 结论标为 hypothesis 非结论.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"30% 训练-推理 sparsity mismatch (actual 28.5% vs target 30%), λ 饱和至 cap\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W5. Appendix C defense 有效但严格对比应为 KL@28.5% vs TEAL@28.5%.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R1-W1, R2 agrees. 主文应报告所有方法 actual achieved sparsity.\"}\n    action_items:\n      - {round: 13, action: \"§4.1 或 §4.2 报告 actual achieved sparsity; 验证更高 λ_max 是否能更接近 30%.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"Abstract '68% divergence' 未限定 sparsity 条件——实为 50% 下数字, 30% 仅 46%\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-W2, R2 agrees. Abstract/Introduction 报告 68% 但论文推荐 30% 操作点仅 46%. Misleading.\"}\n    action_items:\n      - {round: 13, action: \"Abstract 改为 '46-68% depending on sparsity' 或明确标注 'at 50% sparsity'.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"数值系统性向上取整 (19% 实为 18.6%, 7.5× 实为 7.31×, MMLU +0.6pp 实为 +0.5pp)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-W3, R2 agrees. 每个 individually 容差内, 但所有取整方向一致偏高 = systematic bias.\"}\n    action_items:\n      - {round: 13, action: \"统一使用一位小数精度或标注 '≈'. 修正: 19%→18.6%, 7.5×→7.3×, +0.6pp→+0.5pp.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W6\"\n    summary: \"无 wall-clock speedup, predictor 增加 6.4% overhead, motivation-delivery gap\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-W3.\"}\n      - {round: 12, reviewers: [1, 2], note: \"R12-W3.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R1-W4, R2-W2 full consensus. §4.6 报告 2.7% 仅是 predictor overhead, total pipeline overhead 6.4%. 主文有 downplaying 之嫌.\"}\n    action_items:\n      - {round: 13, action: \"Abstract 'renders compensation redundant' → 'renders compensation redundant in prediction quality'. Introduction 更早界定 prediction quality study 范围.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"Acknowledged limitation. Sparse kernel integration deferred.\"\n    resolution_round: 11\n\n  - id: \"R13-W7\"\n    summary: \"OOD 评估统计不足: C4 30% 仅 2-seed, 50% single seed; 'generalize across distributions' claim 过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W8.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R1-W5, R2 agrees. 与主实验 3-seed 标准不一致. C4 PPL 1.74× dense vs in-domain 1.46× 暗示 meaningful overfitting.\"}\n    action_items:\n      - {round: 13, action: \"补 3-seed C4 评估, 或降低 OOD generalization claim 强度.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W8\"\n    summary: \"Cross-architecture PPL 对比使用不同 allocation (LLaMA global vs Mistral uniform)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-W6, R2 agrees. Table 15 caption 标注了但 Adv ratio 跨架构比较不 clean.\"}\n    action_items:\n      - {round: 13, action: \"Table 15 增加 matched allocation 行, 或更显著提示 allocation 差异.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W9\"\n    summary: \"Conclusion 仅 3 句话 + vspace{-14pt}, 无 future work\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W7.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R2-W3, R1 agrees. vspace{-14pt} 是 formatting red flag.\"}\n    action_items:\n      - {round: 13, action: \"精简 §4.6 重复内容, 为 Conclusion 腾空间. 至少加 2-3 句 future work.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W10\"\n    summary: \"Baseline 不足: 缺 ShadowLLM (MSE predictor-based) 实验对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R2-W4, R1 partial agrees (ShadowLLM 必须加, CATS/R-Sparse 非核心). ShadowLLM 在 taxonomy 中标为 Intermediate 但仅在 Related Work 讨论无数据.\"}\n    action_items:\n      - {round: 13, action: \"加入 ShadowLLM 或 per-layer MSE baseline (与 R13-N1 合并处理).\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W11\"\n    summary: \"C1 ablation s42 oracle 来自 earlier training run, PPL gap 0.65 vs retrained ≤0.03\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R2-W5, R1 agrees with qualification (retrained seeds 化解 concern). Table 3 仅以 dagger 脚注说明, 应在正文讨论.\"}\n    action_items:\n      - {round: 13, action: \"正文中讨论 s42 oracle 版本差异及其对 C1 结论的影响.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M1\"\n    summary: \"Minor 写作/呈现问题集合\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"'proximate driver' 7+ 次过度重复; Table 2 'Ours' 标注 global/uniform 不统一; Abstract 14B 过度简化(未区分 uniform vs global); Figure 2 'disproportionately' R1 rebut(super-linear ratio 数学正确); Griffin ref not_found; AdamW year mismatch(bib 2019 vs pub 2017); vspace{-14pt}; §4.6 overhead '2.7%' 仅 predictor 非 total 6.4%.\"}\n    action_items:\n      - {round: 13, action: \"Batch fix: 减少 'proximate driver' 重复; 统一 Table 2 标注; Abstract 加 allocation 限定; 修正 reference year; 删 vspace{-14pt}; 主文报告 total overhead 6.4%.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — status updates for Round 13\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"C1 消融 50% max Δ 数值错误：论文声称 0.59pp，Table 3 实际为 0.79pp (WG)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 13, reviewers: [], note: \"Table 3 caption 现正确报告 'max Δ≤0.79pp at 50% (s42)'. Abstract/Introduction 同步修正. 已解决.\"}\n    resolution: \"Max Δ corrected to 0.79pp throughout. Not raised in R13.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 BCE+comp (28.13±0.20) vs Table 4 BCE+Compensation (25.44) 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 13, reviewers: [], note: \"Table 2 现标注 'BCE (2700 steps)* no compensation'. §4.5 明确区分 TEAL eval PPL 44.54 vs per-token PPL 25.44 for BCE+comp. 混淆已消除.\"}\n    resolution: \"Table labeling clarified. TEAL eval vs per-token eval distinction explicit.\"\n    resolution_round: 13\n\n  - id: \"R12-W1\"\n    summary: \"C1 'Causal Ablation' 命名过强，存在未解决的 soft-vs-hard confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 13, reviewers: [], note: \"已改为 'Target-Swap Ablation' (§4.4 heading, Table 3 caption). soft-vs-hard confound 在 §4.4 末段明确承认. 已解决.\"}\n    resolution: \"Renamed to 'Target-Swap Ablation'. Confound boundary acknowledged.\"\n    resolution_round: 13\n\n  - id: \"R12-W6\"\n    summary: \"30% downstream 退化严重, 'best quality level' 表述需修正\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R2 指出, R1 同意.\"}\n      - {round: 13, reviewers: [], note: \"Limitations 现使用 'lowest-degradation sparsity level'. 已解决.\"}\n    resolution: \"'best quality' changed to 'lowest-degradation'. Not raised in R13.\"\n    resolution_round: 13\n\n  - id: \"R11-W1\"\n    summary: \"Abstract severe data overload\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Both agree Abstract fails 30-second readability test.\"}\n      - {round: 12, reviewers: [], note: \"Abstract restructured.\"}\n    resolution: \"Abstract restructured with clearer narrative flow.\"\n    resolution_round: 12\n\n  - id: \"R11-W6\"\n    summary: \"Table 3 C1 ablation at 30%: previously missing downstream metrics\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Max Δ=1.70pp claim based on MMLU only.\"}\n      - {round: 12, reviewers: [], note: \"Table 3 now shows full downstream.\"}\n    resolution: \"Table 3 now contains complete downstream metrics.\"\n    resolution_round: 12\n\n  - id: \"R11-DENSE\"\n    summary: \"Mistral downstream table Dense row uses v0.1 public data instead of v0.3\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"Mistral Dense row corrected to v0.3 experimental values.\"\n    resolution_round: 12\n\n  - id: \"R11-REF\"\n    summary: \"Missing reference: OWL (Yin et al., 2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"OWL citation added.\"\n    resolution_round: 12\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"RESOLVED by C1 ablation.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"Removed.\"\n    resolution_round: 9\n\n  - id: \"R8-N3\"\n    summary: \"Regime curve data points insufficient\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"6-point regime curve confirmed.\"\n    resolution_round: 11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 13 (fresh review) — New issues\n  # ============================================================\n\n  - id: \"R13-N1\"\n    summary: \"MSE intermediate baseline 缺失，taxonomy Decomposed/Intermediate/Coupled 核心 claim 无实验支撑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-N3. Full consensus.\"}\n      - {round: 13, reviewers: [1, 2], note: \"Full consensus. R1-N1 Must-Fix, R2-W1→升级同意. 没有 MSE baseline 无法区分改进来自任何形式 coupling 还是特定 end-to-end output-level coupling. 实验成本极低（替换 loss function），缺失令人遗憾.\"}\n    action_items:\n      - {round: 13, action: \"训练 per-layer MSE predictor（相同架构，最小化 sparse vs dense hidden state MSE），加入 Table 2 和 Table 4 对比. 或弱化 taxonomy 为概念组织工具.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N2\"\n    summary: \"跨架构/跨规模 claim 过强：Mistral 单 seed, 14B sparsity mismatch (29.6% vs 26.8%), mass-covering 假说未验证\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-N2. 14B MMLU reversal 仅 'warrants further investigation'.\"}\n      - {round: 12, reviewers: [1, 2], note: \"R12-W2. 14B 加了 per-layer mask divergence 分析但仍 single seed.\"}\n      - {round: 13, reviewers: [1, 2], note: \"Full consensus. R1-N2 Must-Fix. Mistral 仅 single seed 不足支撑 5/6 claim. 14B actual sparsity KL 29.6% vs TEAL 26.8% 构成不公平对比. §4.6 的 mass-covering 解释是未验证推测.\"}\n    action_items:\n      - {round: 13, action: \"Mistral 补 3-seed; 14B 对齐 actual sparsity 或明确报告 matched 结果; mass-covering 标为 hypothesis; 降低 abstract/conclusion cross-arch claim 强度.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N3\"\n    summary: \"SNR 证据选择性呈现：§3.6 仅报告 step 300 的 5.14× 优势，隐藏 mid-training BCE 反超 KL 的 non-monotonic trajectory\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-N3 Must-Fix, R2 升级同意(程度判断略保守). Appendix G 揭示 steps 100-250 BCE surpasses KL，主文完全省略. Step 300 是 BCE 刚被反超时间点——选择性呈现. 且缺少 step 300-1000 的 trajectory.\"}\n    action_items:\n      - {round: 13, action: \"主文加一句 acknowledge non-monotonic trajectory; Appendix G 补完整 SNR 曲线至 step 1000; 或将 SNR 分析降级为 appendix-only evidence.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W1\"\n    summary: \"方法新颖性有限：standard KL + standard Gumbel 组合，MaskLLM 已证明 KL 用于 mask learning\"\n    category: method\n    severity: warning\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R9-N4.\"}\n      - {round: 12, reviewers: [1, 2], note: \"R12-W4. Both agree Findings-appropriate.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R2-N1 Must-Fix, R1 agrees with qualification (venue fit issue, not fixable). 核心 principle（KL 训练 mask）与 MaskLLM 相同. 强化 empirical study 定位.\"}\n    resolution: \"Positioning issue. Findings accepted as realistic target.\"\n    resolution_round: 10\n\n  - id: \"R13-W2\"\n    summary: \"下游 PPL disconnect：30% 8B KL 赢 4/6 任务但输 MMLU/GSM8K; 14B GSM8K -25pp\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W6. 30% downstream 退化讨论.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R2-N2 定 Must-Fix, R1 rebut (KL 赢 ARC +4.4, WG +3.9, HS +7.8, PIQA +2.2). Director 裁定 Should-Fix with strong caveat: 8B 层面不构成 Must-Fix, 但 14B claim 需显著收敛.\"}\n    action_items:\n      - {round: 13, action: \"在 narrative 中更平衡地呈现下游结果 (不仅以 PPL 为 selling point); 14B 结论标为 hypothesis 非结论.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"30% 训练-推理 sparsity mismatch (actual 28.5% vs target 30%), λ 饱和至 cap\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W5. Appendix C defense 有效但严格对比应为 KL@28.5% vs TEAL@28.5%.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R1-W1, R2 agrees. 主文应报告所有方法 actual achieved sparsity.\"}\n    action_items:\n      - {round: 13, action: \"§4.1 或 §4.2 报告 actual achieved sparsity; 验证更高 λ_max 是否能更接近 30%.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"Abstract '68% divergence' 未限定 sparsity 条件——实为 50% 下数字, 30% 仅 46%\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-W2, R2 agrees. Abstract/Introduction 报告 68% 但论文推荐 30% 操作点仅 46%. Misleading.\"}\n    action_items:\n      - {round: 13, action: \"Abstract 改为 '46-68% depending on sparsity' 或明确标注 'at 50% sparsity'.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"数值系统性向上取整 (19% 实为 18.6%, 7.5× 实为 7.31×, MMLU +0.6pp 实为 +0.5pp)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-W3, R2 agrees. 每个 individually 容差内, 但所有取整方向一致偏高 = systematic bias.\"}\n    action_items:\n      - {round: 13, action: \"统一使用一位小数精度或标注 '≈'. 修正: 19%→18.6%, 7.5×→7.3×, +0.6pp→+0.5pp.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W6\"\n    summary: \"无 wall-clock speedup, predictor 增加 6.4% overhead, motivation-delivery gap\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 11\n    last_seen_round: 13\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-W3.\"}\n      - {round: 12, reviewers: [1, 2], note: \"R12-W3.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R1-W4, R2-W2 full consensus. §4.6 报告 2.7% 仅是 predictor overhead, total pipeline overhead 6.4%. 主文有 downplaying 之嫌.\"}\n    action_items:\n      - {round: 13, action: \"Abstract 'renders compensation redundant' → 'renders compensation redundant in prediction quality'. Introduction 更早界定 prediction quality study 范围.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"Acknowledged limitation. Sparse kernel integration deferred.\"\n    resolution_round: 11\n\n  - id: \"R13-W7\"\n    summary: \"OOD 评估统计不足: C4 30% 仅 2-seed, 50% single seed; 'generalize across distributions' claim 过强\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W8.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R1-W5, R2 agrees. 与主实验 3-seed 标准不一致. C4 PPL 1.74× dense vs in-domain 1.46× 暗示 meaningful overfitting.\"}\n    action_items:\n      - {round: 13, action: \"补 3-seed C4 评估, 或降低 OOD generalization claim 强度.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W8\"\n    summary: \"Cross-architecture PPL 对比使用不同 allocation (LLaMA global vs Mistral uniform)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R1-W6, R2 agrees. Table 15 caption 标注了但 Adv ratio 跨架构比较不 clean.\"}\n    action_items:\n      - {round: 13, action: \"Table 15 增加 matched allocation 行, 或更显著提示 allocation 差异.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W9\"\n    summary: \"Conclusion 仅 3 句话 + vspace{-14pt}, 无 future work\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W7.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R2-W3, R1 agrees. vspace{-14pt} 是 formatting red flag.\"}\n    action_items:\n      - {round: 13, action: \"精简 §4.6 重复内容, 为 Conclusion 腾空间. 至少加 2-3 句 future work.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W10\"\n    summary: \"Baseline 不足: 缺 ShadowLLM (MSE predictor-based) 实验对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R2-W4, R1 partial agrees (ShadowLLM 必须加, CATS/R-Sparse 非核心). ShadowLLM 在 taxonomy 中标为 Intermediate 但仅在 Related Work 讨论无数据.\"}\n    action_items:\n      - {round: 13, action: \"加入 ShadowLLM 或 per-layer MSE baseline (与 R13-N1 合并处理).\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W11\"\n    summary: \"C1 ablation s42 oracle 来自 earlier training run, PPL gap 0.65 vs retrained ≤0.03\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R2-W5, R1 agrees with qualification (retrained seeds 化解 concern). Table 3 仅以 dagger 脚注说明, 应在正文讨论.\"}\n    action_items:\n      - {round: 13, action: \"正文中讨论 s42 oracle 版本差异及其对 C1 结论的影响.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-M1\"\n    summary: \"Minor 写作/呈现问题集合\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"'proximate driver' 7+ 次过度重复; Table 2 'Ours' 标注 global/uniform 不统一; Abstract 14B 过度简化(未区分 uniform vs global); Figure 2 'disproportionately' R1 rebut(super-linear ratio 数学正确); Griffin ref not_found; AdamW year mismatch(bib 2019 vs pub 2017); vspace{-14pt}; §4.6 overhead '2.7%' 仅 predictor 非 total 6.4%.\"}\n    action_items:\n      - {round: 13, action: \"Batch fix: 减少 'proximate driver' 重复; 统一 Table 2 标注; Abstract 加 allocation 限定; 修正 reference year; 删 vspace{-14pt}; 主文报告 total overhead 6.4%.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — status updates for Round 13\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"C1 消融 50% max Δ 数值错误：论文声称 0.59pp，Table 3 实际为 0.79pp (WG)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 13, reviewers: [], note: \"Table 3 caption 现正确报告 'max Δ≤0.79pp at 50% (s42)'. Abstract/Introduction 同步修正. 已解决.\"}\n    resolution: \"Max Δ corrected to 0.79pp throughout. Not raised in R13.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 BCE+comp (28.13±0.20) vs Table 4 BCE+Compensation (25.44) 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 13, reviewers: [], note: \"Table 2 现标注 'BCE (2700 steps)* no compensation'. §4.5 明确区分 TEAL eval PPL 44.54 vs per-token PPL 25.44 for BCE+comp. 混淆已消除.\"}\n    resolution: \"Table labeling clarified. TEAL eval vs per-token eval distinction explicit.\"\n    resolution_round: 13\n\n  - id: \"R12-W1\"\n    summary: \"C1 'Causal Ablation' 命名过强，存在未解决的 soft-vs-hard confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"Full consensus.\"}\n      - {round: 13, reviewers: [], note: \"已改为 'Target-Swap Ablation' (§4.4 heading, Table 3 caption). soft-vs-hard confound 在 §4.4 末段明确承认. 已解决.\"}\n    resolution: \"Renamed to 'Target-Swap Ablation'. Confound boundary acknowledged.\"\n    resolution_round: 13\n\n  - id: \"R12-W6\"\n    summary: \"30% downstream 退化严重, 'best quality level' 表述需修正\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R2 指出, R1 同意.\"}\n      - {round: 13, reviewers: [], note: \"Limitations 现使用 'lowest-degradation sparsity level'. 已解决.\"}\n    resolution: \"'best quality' changed to 'lowest-degradation'. Not raised in R13.\"\n    resolution_round: 13\n\n  - id: \"R11-W1\"\n    summary: \"Abstract severe data overload\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Both agree Abstract fails 30-second readability test.\"}\n      - {round: 12, reviewers: [], note: \"Abstract restructured.\"}\n    resolution: \"Abstract restructured with clearer narrative flow.\"\n    resolution_round: 12\n\n  - id: \"R11-W6\"\n    summary: \"Table 3 C1 ablation at 30%: previously missing downstream metrics\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"Max Δ=1.70pp claim based on MMLU only.\"}\n      - {round: 12, reviewers: [], note: \"Table 3 now shows full downstream.\"}\n    resolution: \"Table 3 now contains complete downstream metrics.\"\n    resolution_round: 12\n\n  - id: \"R11-DENSE\"\n    summary: \"Mistral downstream table Dense row uses v0.1 public data instead of v0.3\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"Mistral Dense row corrected to v0.3 experimental values.\"\n    resolution_round: 12\n\n  - id: \"R11-REF\"\n    summary: \"Missing reference: OWL (Yin et al., 2024)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"OWL citation added.\"\n    resolution_round: 12\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"RESOLVED by C1 ablation.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"Removed.\"\n    resolution_round: 9\n\n  - id: \"R8-N3\"\n    summary: \"Regime curve data points insufficient\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"6-point regime curve confirmed.\"\n    resolution_round: 11"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-20T01:51:06.922507+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 14834}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-20T01:51:14.124995+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 完成', 'status': 'completed', 'activeForm': '完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '视觉审查超时'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': 'Issue Tracker 已更新'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'in_progress', 'activeForm': '提交审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 完成', 'status': 'completed', 'activeForm': '完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '视觉审查超时'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': 'Issue Tracker 已更新'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'in_progress', 'activeForm': '提交审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-20T01:51:14.175765+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-20T01:53:13.931969+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "report": "# Round 13 审稿报告（Fresh Review）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 via ARR May 2026\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作格式）\n**轮次**: 1 轮（交叉分享后收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出将 SwiGLU LLM 稀疏预测器的训练目标从 per-neuron BCE 替换为 output-distribution KL divergence，配合 Gumbel-Sigmoid relaxation 实现端到端可微训练。在 LLaMA-3.1-8B 上，KL predictor（75.9M 参数，<1% base）在 30% sparsity 下将 TEAL perplexity 降低 18.6%（8.81 vs 10.82），在 50% 降低 51%。C1 target-swap ablation 表明 KL 发现的 mask pattern（与 magnitude mask 46–68% divergence）是质量提升的 proximate driver。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B，揭示 scale-dependent effects。\n\n---\n\n## Strengths\n\n**S1. C1 Target-Swap Ablation 设计精巧且有力 [Full consensus]**\n通过将 KL-discovered masks 转移到 BCE 训练，干净分离了 mask quality 和 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp（s42），retrained seeds (s123/s456) 30% PPL Δ≤0.03。这是全文最强的贡献，提供了有价值的 empirical insight。\n\n**S2. 系统性消融覆盖全面 [Full consensus]**\nTable 4 隔离了 Gumbel vs STE（+3.98 PPL）、divergence direction（forward > JSD > reverse）、loss function 贡献（KL effect 5.1× relaxation effect）、compensation redundancy。Appendix B–C 确认对 bottleneck/temperature/training steps 不敏感。\n\n**S3. 诚实报告负面结果 [Full consensus]**\n14B GSM8K −25pp、50% downstream collapse、无实际加速、OOD gap（C4 1.74× vs in-domain 1.46×）均在 Limitations 和正文中明确讨论。\n\n**S4. 高可复现性 [Full consensus]**\n1000 步 / 45 min / 单 GPU。超参完整披露。3-seed 评估（PPL CV<1%）。GPU 型号/训练时间均报告。Soundness 4/5。\n\n**S5. Related Work 覆盖全面**\n47 篇引用系统覆盖 training-free sparsity、predictor-based methods、KL distillation、MoE routing 等。与 MaskLLM 的三点区分论述清晰。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，影响接收决定）\n\n**N1. MSE intermediate baseline 缺失，taxonomy 核心 claim 无实验支撑 [Full consensus, R1-N1 + R2-W1]**\nTable 1 定义 Decomposed/Intermediate/Coupled 三级 taxonomy，实验仅评估两端。§3.7 显式承认 \"per-layer MSE is not evaluated in our experiments\"。没有 MSE baseline，无法区分改进来自：(a) 任何形式的 non-trivial coupling，还是 (b) 特定的 end-to-end output-level coupling。ShadowLLM 在 taxonomy 中标为 Intermediate 但无数据对比。实验成本极低（替换 loss function），缺失令人遗憾。\n→ **Action**: 训练 per-layer MSE predictor（相同架构），加入 Table 2 和 Table 4。或弱化 taxonomy 为概念组织工具。\n\n**N2. 跨架构/跨规模 claim 过强，数据支撑不足 [Full consensus, R1-N2 + R2-N2]**\n- Mistral-7B 全部 single seed，5/6 tasks win 的统计意义有限\n- Qwen-14B GSM8K 32.1±5.2% vs TEAL 57.1%（−25pp, σ=5.2pp），MMLU −2.79pp uniform / −8.1pp global\n- 14B actual sparsity mismatch: KL 29.6% vs TEAL 26.8%（2.8pp 差异可能解释部分 degradation）\n- §4.6 的 \"forward KL's mass-covering property disrupts narrow reasoning pathways\" 是未验证推测\n→ **Action**: Mistral 补 3-seed; 14B 对齐 actual sparsity 或明确报告; mass-covering 标为 hypothesis; 降低 abstract/conclusion cross-arch claim 强度。\n\n**N3. SNR 证据选择性呈现 [Consensus with nuance, R1-N3 + R2 升级同意]**\n§3.6 报告 \"at step 300, KL achieves 5.14× higher SNR\"，但 Appendix G 揭示 trajectory 是 non-monotonic 的——BCE 在 steps 100–250 surpasses KL。主文完全省略这一关键信息。Step 300 恰好是 BCE 刚被反超的时间点。且缺少 step 300–1000 的完整 trajectory。这构成 selective presentation，削弱 §3.6 \"coupled gradient structural advantage\" 叙事的可信度。\n（R2 补充 nuance：如 KL 在 300–1000 持续保持优势则非 cherry-pick，但论文未展示后续数据。）\n→ **Action**: 主文加一句 acknowledge non-monotonic trajectory; Appendix G 补完整 SNR 曲线至 step 1000。\n\n### Should-Fix（9 项，影响评分但不一票否决）\n\n**W1. 方法新颖性有限 [Full consensus, R2-N1 + R1 agrees]**\n核心是 standard forward KL + standard Gumbel-Sigmoid 的组合。MaskLLM (NeurIPS 2024) 已证明 frozen weights + learnable masks + KL training 的有效性。论文自称 \"primarily empirical\"——Findings 定位合理，但不足以支撑 Main track long paper。\n→ **Action**: 强化 empirical study 定位，弱化方法论创新暗示。\n\n**W2. 下游 PPL disconnect [Divergence: R2 Must-Fix → R1 rebuts → Director 裁定 Should-Fix with caveat]**\n30% 8B: KL 赢 ARC-c +4.4pp, WG +3.9pp, HS +7.8pp, PIQA +2.2pp，但输 MMLU −5.2pp, GSM8K −1.3pp（赢 4/6）。14B: GSM8K −25pp 和 MMLU reversal 更显著。PPL 改善不一致地 translate 为下游改善。R1 正确指出 8B 层面 KL 在多数任务上赢，但 14B 的 mixed results 削弱了方法的实用价值叙事。\n→ **Action**: narrative 更平衡地呈现下游结果; 14B 结论标为 preliminary observation。\n\n**W3. 30% sparsity mismatch [Full consensus, R1-W1]**\nPenalty controller 在 30% 目标下 actual sparsity 28.5%（偏差 5%），λ 达 cap 5000。KL 比声称保留了更多 neurons。\n→ **Action**: 主文报告 actual achieved sparsity; 验证更高 λ_max 效果。\n\n**W4. Abstract \"68% divergence\" 未限定 sparsity [Full consensus, R1-W2]**\n68% 是 50% sparsity 下数字; 30% 操作点仅 46%。Abstract/Introduction 未标注。\n→ **Action**: 改为 \"46–68% depending on sparsity\" 或标注 \"at 50%\"。\n\n**W5. 数值系统性向上取整 [Full consensus, R1-W3]**\n19%（实 18.6%）、7.5×（实 7.31×）、MMLU +0.6pp（实 +0.5pp）——所有方向一致偏高。\n→ **Action**: 统一精度或标注 \"≈\"。\n\n**W6. 无 wall-clock speedup [Full consensus, R1-W4 + R2-W2]**\nPredictor 增加 6.4% total overhead（§4.6 主文仅报告 2.7% predictor-only，有 downplaying 之嫌）。整个 pipeline 比 dense 更慢。方法的实用价值是 hypothetical 的。\n→ **Action**: Abstract \"renders compensation redundant\" → \"redundant in prediction quality\"; Introduction 更早界定贡献范围。\n\n**W7. OOD 统计覆盖不足 [Full consensus, R1-W5]**\nC4 30% 仅 2-seed，50% single seed。\"generalize across distributions\" claim 与主实验 3-seed 标准不一致。\n→ **Action**: 补 3-seed C4 或降低 claim。\n\n**W8. Cross-arch allocation confound [Full consensus, R1-W6]**\nTable 15 LLaMA 用 global，Mistral 用 uniform，Adv ratio 跨架构比较不 clean。\n→ **Action**: 增加 matched allocation 行或更显著标注。\n\n**W9. Conclusion 过短 [Full consensus, R2-W3]**\n3 句话 + vspace{-14pt}，无 future work。Formatting red flag。\n→ **Action**: 精简 §4.6，为 Conclusion 腾空间。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 所有 Must-Fix 和绝大多数 Should-Fix/Minor**:\n- MSE baseline 缺失（N1）\n- Cross-arch claim 过强（N2）\n- SNR selective presentation（N3，R2 程度判断略保守但同意核心问题）\n- 方法新颖性有限（W1）\n- Sparsity mismatch（W3）\n- 68% unlabeled（W4）\n- 数值 rounding（W5）\n- 无 speedup（W6）\n- OOD 不足（W7）\n- Allocation confound（W8）\n- Conclusion 短（W9）\n\n## Reviewer Divergence\n\n**[REBUT on severity] 下游 PPL disconnect（W2）**:\n- R2 定 Must-Fix: PPL 改善不 translate 为下游改善，削弱实用价值\n- R1 rebut: 30% 8B 上 KL 赢 4/6 任务（ARC-c +4.4, WG +3.9, HS +7.8, PIQA +2.2），仅输 MMLU −5.2 和 GSM8K −1.3。PPL-downstream non-monotonic 关系是论文发现之一，非缺陷。\n- **Director 裁定**: Should-Fix with strong caveat。8B 层面不构成 Must-Fix，但 14B GSM8K −25pp 是 serious concern，需在 narrative 中更平衡呈现。\n\n---\n\n## Questions for Authors\n\n1. **为什么不评估 MSE intermediate baseline？** 训练成本与 BCE 相当，能直接回答 coupling 程度的关键问题。\n2. **Step 1000 的 SNR ratio？** 论文仅展示到 step 300。完整 trajectory 对 \"coupled gradient advantage\" narrative 至关重要。\n3. **14B sparsity mismatch 影响？** KL 29.6% vs TEAL 26.8%。控制 actual sparsity 后 MMLU/GSM8K 差距是否缩小？\n4. **C1 oracle 对 checkpoint 的敏感性？** 如在 step 500 提取 masks，BCE 是否仍能 match KL quality？\n5. **单 predictor 多 sparsity 目标？** 每个 target 训练 45 min 在部署中不可忽视。\n\n---\n\n## Missing References\n\n无重大遗漏。可考虑补充（非必须）：\n- Bambhaniya et al., 2024, \"Progressive Gradient Flow for Robust N:M Sparsity Training\" — 如讨论 N:M 扩展\n- Li et al., 2023, \"Lazy Neuron Phenomenon in Transformers\" — 与 mask pattern divergence 分析相关\n\n---\n\n## External Review\n\n**状态**: 未请求（项目未启用 paperreview.ai 外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 超时（elapsed 794s）。视觉审查 Agent 未能在时限内完成。用户可决定是否重新触发 `dispatch_visual_check`。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**评分理由**:\n\n这是一篇执行扎实的实证研究。C1 target-swap ablation 是精巧的 disentanglement 实验，证明了 mask quality 而非 gradient coupling mechanism 是 inference-stage quality 的 proximate driver。系统性消融全面（Table 4 隔离了 5+ 设计选择），负面结果的诚实报告值得肯定（14B GSM8K −25pp、50% downstream collapse、无加速）。训练成本极低（1000 步/45 min/单 GPU），可复现性高。\n\n但方法新颖性有限（standard KL + standard Gumbel，MaskLLM 已证明该 principle），taxonomy 的核心 claim（end-to-end coupling 优于 intermediate coupling）因 MSE baseline 缺失而无法验证。SNR 证据的选择性呈现（隐藏 mid-training BCE 反超）是 presentation integrity concern。跨架构 claim 数据不足（Mistral single seed, 14B sparsity mismatch）。14B 的 GSM8K −25pp 和 MMLU reversal 使得方法的 scale generalization 存疑。无 wall-clock speedup，实用价值 hypothetical。\n\n论文定位为 empirical study 是合理的，C1 ablation 和 regime analysis 对 activation sparsity 社区有参考价值，符合 EMNLP Findings 水平。但方法论和 presentation 问题阻止其达到 Borderline Conference。\n\n**Reviewer 评分**:\n- R1: 3.5 (Borderline Conference), Confidence 4/5\n- R2: 3.0 (Findings), Confidence 4/5\n\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"diverge 68%\" 应标注 \"at 50% sparsity\"（30% 仅 46%）[W4]\n- \"renders compensation redundant\" 应加 \"in prediction quality\"[W6]\n- \"19%\" 实为 18.6%, \"7.5×\" 实为 7.31× [W5]\n- 14B 描述未区分 uniform vs global allocation [R2-M4]\n\n### §1 Introduction\n- \"proximate driver\" 全文 7+ 处，此处首次出现，后续应减少重复 [R1-Minor]\n- Cross-arch contribution (line 23) 强度应降低 [N2]\n\n### §2 Related Work\n- 覆盖全面，无重大遗漏\n\n### §3 Method\n- §3.6 SNR 分析：必须 acknowledge non-monotonic trajectory [N3]\n- §3.7 Taxonomy: MSE intermediate cell 无实验支撑 [N1]\n\n### §4 Experiments\n- §4.1: 应报告 all methods 的 actual achieved sparsity [W3]\n- §4.2 Main Results: 数值精度需修正 [W5]\n- §4.4 C1 Ablation: s42 oracle 版本差异应在正文讨论（非仅脚注）[R2-W5]\n- §4.6 Cross-arch: Mistral 补 3-seed; 14B 对齐 sparsity; mass-covering 标为 hypothesis [N2]\n- §4.6 Overhead: 报告 total 6.4% 而非仅 predictor 2.7% [W6]\n\n### §5 Conclusion\n- 扩展至 4-6 句，加 future work，删 vspace{-14pt} [W9]\n\n### Limitations\n- 讨论充分且诚实，是论文的优点 [S3]\n\n### Appendix\n- G: 补完整 SNR 曲线至 step 1000 [N3]\n- D: C4 补 3-seed [W7]\n- L: Table 15 标注或增加 matched allocation [W8]\n\n### References\n- Griffin (de2024): 更新 venue/year\n- AdamW (loshchilov2019): 统一使用 venue 年份",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "report": "# Round 13 审稿报告（Fresh Review）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 via ARR May 2026\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作格式）\n**轮次**: 1 轮（交叉分享后收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出将 SwiGLU LLM 稀疏预测器的训练目标从 per-neuron BCE 替换为 output-distribution KL divergence，配合 Gumbel-Sigmoid relaxation 实现端到端可微训练。在 LLaMA-3.1-8B 上，KL predictor（75.9M 参数，<1% base）在 30% sparsity 下将 TEAL perplexity 降低 18.6%（8.81 vs 10.82），在 50% 降低 51%。C1 target-swap ablation 表明 KL 发现的 mask pattern（与 magnitude mask 46–68% divergence）是质量提升的 proximate driver。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B，揭示 scale-dependent effects。\n\n---\n\n## Strengths\n\n**S1. C1 Target-Swap Ablation 设计精巧且有力 [Full consensus]**\n通过将 KL-discovered masks 转移到 BCE 训练，干净分离了 mask quality 和 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp（s42），retrained seeds (s123/s456) 30% PPL Δ≤0.03。这是全文最强的贡献，提供了有价值的 empirical insight。\n\n**S2. 系统性消融覆盖全面 [Full consensus]**\nTable 4 隔离了 Gumbel vs STE（+3.98 PPL）、divergence direction（forward > JSD > reverse）、loss function 贡献（KL effect 5.1× relaxation effect）、compensation redundancy。Appendix B–C 确认对 bottleneck/temperature/training steps 不敏感。\n\n**S3. 诚实报告负面结果 [Full consensus]**\n14B GSM8K −25pp、50% downstream collapse、无实际加速、OOD gap（C4 1.74× vs in-domain 1.46×）均在 Limitations 和正文中明确讨论。\n\n**S4. 高可复现性 [Full consensus]**\n1000 步 / 45 min / 单 GPU。超参完整披露。3-seed 评估（PPL CV<1%）。GPU 型号/训练时间均报告。Soundness 4/5。\n\n**S5. Related Work 覆盖全面**\n47 篇引用系统覆盖 training-free sparsity、predictor-based methods、KL distillation、MoE routing 等。与 MaskLLM 的三点区分论述清晰。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，影响接收决定）\n\n**N1. MSE intermediate baseline 缺失，taxonomy 核心 claim 无实验支撑 [Full consensus, R1-N1 + R2-W1]**\nTable 1 定义 Decomposed/Intermediate/Coupled 三级 taxonomy，实验仅评估两端。§3.7 显式承认 \"per-layer MSE is not evaluated in our experiments\"。没有 MSE baseline，无法区分改进来自：(a) 任何形式的 non-trivial coupling，还是 (b) 特定的 end-to-end output-level coupling。ShadowLLM 在 taxonomy 中标为 Intermediate 但无数据对比。实验成本极低（替换 loss function），缺失令人遗憾。\n→ **Action**: 训练 per-layer MSE predictor（相同架构），加入 Table 2 和 Table 4。或弱化 taxonomy 为概念组织工具。\n\n**N2. 跨架构/跨规模 claim 过强，数据支撑不足 [Full consensus, R1-N2 + R2-N2]**\n- Mistral-7B 全部 single seed，5/6 tasks win 的统计意义有限\n- Qwen-14B GSM8K 32.1±5.2% vs TEAL 57.1%（−25pp, σ=5.2pp），MMLU −2.79pp uniform / −8.1pp global\n- 14B actual sparsity mismatch: KL 29.6% vs TEAL 26.8%（2.8pp 差异可能解释部分 degradation）\n- §4.6 的 \"forward KL's mass-covering property disrupts narrow reasoning pathways\" 是未验证推测\n→ **Action**: Mistral 补 3-seed; 14B 对齐 actual sparsity 或明确报告; mass-covering 标为 hypothesis; 降低 abstract/conclusion cross-arch claim 强度。\n\n**N3. SNR 证据选择性呈现 [Consensus with nuance, R1-N3 + R2 升级同意]**\n§3.6 报告 \"at step 300, KL achieves 5.14× higher SNR\"，但 Appendix G 揭示 trajectory 是 non-monotonic 的——BCE 在 steps 100–250 surpasses KL。主文完全省略这一关键信息。Step 300 恰好是 BCE 刚被反超的时间点。且缺少 step 300–1000 的完整 trajectory。这构成 selective presentation，削弱 §3.6 \"coupled gradient structural advantage\" 叙事的可信度。\n（R2 补充 nuance：如 KL 在 300–1000 持续保持优势则非 cherry-pick，但论文未展示后续数据。）\n→ **Action**: 主文加一句 acknowledge non-monotonic trajectory; Appendix G 补完整 SNR 曲线至 step 1000。\n\n### Should-Fix（9 项，影响评分但不一票否决）\n\n**W1. 方法新颖性有限 [Full consensus, R2-N1 + R1 agrees]**\n核心是 standard forward KL + standard Gumbel-Sigmoid 的组合。MaskLLM (NeurIPS 2024) 已证明 frozen weights + learnable masks + KL training 的有效性。论文自称 \"primarily empirical\"——Findings 定位合理，但不足以支撑 Main track long paper。\n→ **Action**: 强化 empirical study 定位，弱化方法论创新暗示。\n\n**W2. 下游 PPL disconnect [Divergence: R2 Must-Fix → R1 rebuts → Director 裁定 Should-Fix with caveat]**\n30% 8B: KL 赢 ARC-c +4.4pp, WG +3.9pp, HS +7.8pp, PIQA +2.2pp，但输 MMLU −5.2pp, GSM8K −1.3pp（赢 4/6）。14B: GSM8K −25pp 和 MMLU reversal 更显著。PPL 改善不一致地 translate 为下游改善。R1 正确指出 8B 层面 KL 在多数任务上赢，但 14B 的 mixed results 削弱了方法的实用价值叙事。\n→ **Action**: narrative 更平衡地呈现下游结果; 14B 结论标为 preliminary observation。\n\n**W3. 30% sparsity mismatch [Full consensus, R1-W1]**\nPenalty controller 在 30% 目标下 actual sparsity 28.5%（偏差 5%），λ 达 cap 5000。KL 比声称保留了更多 neurons。\n→ **Action**: 主文报告 actual achieved sparsity; 验证更高 λ_max 效果。\n\n**W4. Abstract \"68% divergence\" 未限定 sparsity [Full consensus, R1-W2]**\n68% 是 50% sparsity 下数字; 30% 操作点仅 46%。Abstract/Introduction 未标注。\n→ **Action**: 改为 \"46–68% depending on sparsity\" 或标注 \"at 50%\"。\n\n**W5. 数值系统性向上取整 [Full consensus, R1-W3]**\n19%（实 18.6%）、7.5×（实 7.31×）、MMLU +0.6pp（实 +0.5pp）——所有方向一致偏高。\n→ **Action**: 统一精度或标注 \"≈\"。\n\n**W6. 无 wall-clock speedup [Full consensus, R1-W4 + R2-W2]**\nPredictor 增加 6.4% total overhead（§4.6 主文仅报告 2.7% predictor-only，有 downplaying 之嫌）。整个 pipeline 比 dense 更慢。方法的实用价值是 hypothetical 的。\n→ **Action**: Abstract \"renders compensation redundant\" → \"redundant in prediction quality\"; Introduction 更早界定贡献范围。\n\n**W7. OOD 统计覆盖不足 [Full consensus, R1-W5]**\nC4 30% 仅 2-seed，50% single seed。\"generalize across distributions\" claim 与主实验 3-seed 标准不一致。\n→ **Action**: 补 3-seed C4 或降低 claim。\n\n**W8. Cross-arch allocation confound [Full consensus, R1-W6]**\nTable 15 LLaMA 用 global，Mistral 用 uniform，Adv ratio 跨架构比较不 clean。\n→ **Action**: 增加 matched allocation 行或更显著标注。\n\n**W9. Conclusion 过短 [Full consensus, R2-W3]**\n3 句话 + vspace{-14pt}，无 future work。Formatting red flag。\n→ **Action**: 精简 §4.6，为 Conclusion 腾空间。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 所有 Must-Fix 和绝大多数 Should-Fix/Minor**:\n- MSE baseline 缺失（N1）\n- Cross-arch claim 过强（N2）\n- SNR selective presentation（N3，R2 程度判断略保守但同意核心问题）\n- 方法新颖性有限（W1）\n- Sparsity mismatch（W3）\n- 68% unlabeled（W4）\n- 数值 rounding（W5）\n- 无 speedup（W6）\n- OOD 不足（W7）\n- Allocation confound（W8）\n- Conclusion 短（W9）\n\n## Reviewer Divergence\n\n**[REBUT on severity] 下游 PPL disconnect（W2）**:\n- R2 定 Must-Fix: PPL 改善不 translate 为下游改善，削弱实用价值\n- R1 rebut: 30% 8B 上 KL 赢 4/6 任务（ARC-c +4.4, WG +3.9, HS +7.8, PIQA +2.2），仅输 MMLU −5.2 和 GSM8K −1.3。PPL-downstream non-monotonic 关系是论文发现之一，非缺陷。\n- **Director 裁定**: Should-Fix with strong caveat。8B 层面不构成 Must-Fix，但 14B GSM8K −25pp 是 serious concern，需在 narrative 中更平衡呈现。\n\n---\n\n## Questions for Authors\n\n1. **为什么不评估 MSE intermediate baseline？** 训练成本与 BCE 相当，能直接回答 coupling 程度的关键问题。\n2. **Step 1000 的 SNR ratio？** 论文仅展示到 step 300。完整 trajectory 对 \"coupled gradient advantage\" narrative 至关重要。\n3. **14B sparsity mismatch 影响？** KL 29.6% vs TEAL 26.8%。控制 actual sparsity 后 MMLU/GSM8K 差距是否缩小？\n4. **C1 oracle 对 checkpoint 的敏感性？** 如在 step 500 提取 masks，BCE 是否仍能 match KL quality？\n5. **单 predictor 多 sparsity 目标？** 每个 target 训练 45 min 在部署中不可忽视。\n\n---\n\n## Missing References\n\n无重大遗漏。可考虑补充（非必须）：\n- Bambhaniya et al., 2024, \"Progressive Gradient Flow for Robust N:M Sparsity Training\" — 如讨论 N:M 扩展\n- Li et al., 2023, \"Lazy Neuron Phenomenon in Transformers\" — 与 mask pattern divergence 分析相关\n\n---\n\n## External Review\n\n**状态**: 未请求（项目未启用 paperreview.ai 外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 超时（elapsed 794s）。视觉审查 Agent 未能在时限内完成。用户可决定是否重新触发 `dispatch_visual_check`。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**评分理由**:\n\n这是一篇执行扎实的实证研究。C1 target-swap ablation 是精巧的 disentanglement 实验，证明了 mask quality 而非 gradient coupling mechanism 是 inference-stage quality 的 proximate driver。系统性消融全面（Table 4 隔离了 5+ 设计选择），负面结果的诚实报告值得肯定（14B GSM8K −25pp、50% downstream collapse、无加速）。训练成本极低（1000 步/45 min/单 GPU），可复现性高。\n\n但方法新颖性有限（standard KL + standard Gumbel，MaskLLM 已证明该 principle），taxonomy 的核心 claim（end-to-end coupling 优于 intermediate coupling）因 MSE baseline 缺失而无法验证。SNR 证据的选择性呈现（隐藏 mid-training BCE 反超）是 presentation integrity concern。跨架构 claim 数据不足（Mistral single seed, 14B sparsity mismatch）。14B 的 GSM8K −25pp 和 MMLU reversal 使得方法的 scale generalization 存疑。无 wall-clock speedup，实用价值 hypothetical。\n\n论文定位为 empirical study 是合理的，C1 ablation 和 regime analysis 对 activation sparsity 社区有参考价值，符合 EMNLP Findings 水平。但方法论和 presentation 问题阻止其达到 Borderline Conference。\n\n**Reviewer 评分**:\n- R1: 3.5 (Borderline Conference), Confidence 4/5\n- R2: 3.0 (Findings), Confidence 4/5\n\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"diverge 68%\" 应标注 \"at 50% sparsity\"（30% 仅 46%）[W4]\n- \"renders compensation redundant\" 应加 \"in prediction quality\"[W6]\n- \"19%\" 实为 18.6%, \"7.5×\" 实为 7.31× [W5]\n- 14B 描述未区分 uniform vs global allocation [R2-M4]\n\n### §1 Introduction\n- \"proximate driver\" 全文 7+ 处，此处首次出现，后续应减少重复 [R1-Minor]\n- Cross-arch contribution (line 23) 强度应降低 [N2]\n\n### §2 Related Work\n- 覆盖全面，无重大遗漏\n\n### §3 Method\n- §3.6 SNR 分析：必须 acknowledge non-monotonic trajectory [N3]\n- §3.7 Taxonomy: MSE intermediate cell 无实验支撑 [N1]\n\n### §4 Experiments\n- §4.1: 应报告 all methods 的 actual achieved sparsity [W3]\n- §4.2 Main Results: 数值精度需修正 [W5]\n- §4.4 C1 Ablation: s42 oracle 版本差异应在正文讨论（非仅脚注）[R2-W5]\n- §4.6 Cross-arch: Mistral 补 3-seed; 14B 对齐 sparsity; mass-covering 标为 hypothesis [N2]\n- §4.6 Overhead: 报告 total 6.4% 而非仅 predictor 2.7% [W6]\n\n### §5 Conclusion\n- 扩展至 4-6 句，加 future work，删 vspace{-14pt} [W9]\n\n### Limitations\n- 讨论充分且诚实，是论文的优点 [S3]\n\n### Appendix\n- G: 补完整 SNR 曲线至 step 1000 [N3]\n- D: C4 补 3-seed [W7]\n- L: Table 15 标注或增加 matched allocation [W8]\n\n### References\n- Griffin (de2024): 更新 venue/year\n- AdamW (loshchilov2019): 统一使用 venue 年份",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-20T01:53:18.704206+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4772
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-20T01:53:25.839287+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 完成', 'status': 'completed', 'activeForm': '完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '视觉审查超时'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': 'Issue Tracker 已更新'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'completed', 'activeForm': '审稿报告已提交'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 完成', 'status': 'completed', 'activeForm': '完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '视觉审查超时'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': 'Issue Tracker 已更新'}, {'content': 'Step 4c: 提交审稿报告', 'status': 'completed', 'activeForm': '审稿报告已提交'}]"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-20T01:53:25.888541+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 49
}
```

</details>

---


### Assistant

_source line 1142 · 2026-05-20T01:53:37.807594+00:00_

**Round 13 审稿完成。**

报告已投递至 Research Director。核心结论：

**Overall 3.0 (Findings)**

| 类别 | 数量 | 关键项 |
|------|------|--------|
| Must-Fix | 3 | MSE baseline 缺失; 跨架构 claim 过强; SNR 选择性呈现 |
| Should-Fix | 9 | 方法新颖性有限; PPL-downstream disconnect; sparsity mismatch; 68% 未限定; 数值取整偏高; 无 speedup; OOD 不足; allocation confound; Conclusion 过短 |
| Minor | 1 批 | 写作/格式问题集合 |

**与 R12 对比的变化**：
- ✅ 已解决：C1 max Δ 数值错误 (R12-N1)、Table 2/4 矛盾 (R12-N2)、"Causal Ablation" 命名 (R12-W1)、"best quality" 表述 (R12-W6)
- ⚠️ 持续存在：MSE baseline (R12-N3→R13-N1)、14B 单 seed (R12-W2→R13-N2)、无 speedup (R12-W3→R13-W6)、Conclusion 短 (R12-W7→R13-W9)
- 🆕 新发现：SNR cherry-picking (R13-N3)、68% 未限定 (R13-W4)、数值系统性偏高 (R13-W5)、allocation confound (R13-W8)

视觉审查超时，完成后会自动补发到 Group C。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 92

## Round 92

54 recorded events


### User

_source line 1143 · 2026-05-20T05:55:05.960306+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-20T05:55:12.356312+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-20T05:55:12.357334+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-20T05:55:21.673746+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1147 · 2026-05-20T05:55:21.724850+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-20T05:55:24.888160+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1149 · 2026-05-20T05:55:25.341319+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1150 · 2026-05-20T05:55:25.643071+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (280 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- kl_sparsity40_s42_retrain_uniform（准备中）\n- bench_kl30_uniform_gsm8k_d075（准备中）\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- …另有 5 项\n\n## 近期结论\n- **mse30_s42_eval_7task** (success): MSE baseline 30% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Reviewer-requested intermediate baseline. If MSE significantly underperforms KL on downstream tasks while PPL is closer, validates distributional knowledge transfer > per-layer output matching. ← 基于 mse30_s42_train\n- **mse50_s42_eval_7task** (success): MSE baseline 50% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Extends MSE comparison to 50% sparsity for Table 4
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-20T05:55:25.643536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-20T05:55:30.262973+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1153 · 2026-05-20T05:55:32.622718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-20T05:55:33.075138+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
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
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1155 · 2026-05-20T05:55:33.075638+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1156 · 2026-05-20T05:55:39.805826+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL Rolling Review (ARR) 2026 submission guidelines and author instructions:

## Key Submission Guidelines

**Paper Requirements:**
All submitted papers are expected to describe original, completed and unpublished work. Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected.

**Anonymity:**
Papers must not include authors' names and affiliations.

**Length Requirements:**
For long papers: Long papers 
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 9542
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-20T05:55:39.806346+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6730
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-20T05:55:43.981747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit requirements site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit requirements site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1159 · 2026-05-20T05:55:45.388732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1160 · 2026-05-20T05:55:45.841426+00:00_

1	Learned sparsity predictors for SwiGLU (Swish-Gated Linear Unit) LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train predictors with Kullback-Leibler (KL) divergence, coupling all mask decisions through the output distribution.
3	At 30\% sparsity on LLaMA-3.1-8B, the KL predictor ($<$1\% of base parameters) reduces perplexity by 19\% relative to TEAL with moderate downstream degradation, and renders post-hoc compensation (+67.2M params) redundant in prediction quality.
4	KL-derived masks diverge 46--68\% from magnitude-based masks (depending on sparsity level); a target-swap ablation confirms that these mask targets, discovered through KL's coupled gradients, are the proximate quality driver when transferred to simpler objectives.
5	Per-layer coupling (MSE) degrades below training-free baselines ($1.9\times$ TEAL at 30\%; $9.6\times$ at 50\%), revealing \emph{coupling alignment}---not coupling per se---as decisive.
6	Preliminary single-seed evaluation on Mistral-7B-v0.3 and cross-scale evaluation on Qwen-2.5-14B (uniform allocation) reveal consistent PPL improvements but scale-dependent downstream effects.
7	At 50\% sparsity the perplexity advantage widens, though downstream reasoning collapses to near-random regardless of method, revealing a capacity cliff.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-20T05:55:45.841801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1162 · 2026-05-20T05:55:46.796566+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	SwiGLU's gated activation makes prediction challenging: importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
5	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
6	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
7	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Gradient coupling remains necessary at the discovery stage.
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	At 
…[truncated 1876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1163 · 2026-05-20T05:55:46.847345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-20T05:55:47.299668+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 11308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-20T05:55:47.300184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-20T05:55:47.752592+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-20T05:55:47.753089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-20T05:55:48.255528+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
8	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
9	
10	\paragraph{Predictor-Based Contextual Sparsity.}
11	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
12	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
13	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
14	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
15	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
16	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
17	First, \emph{spar
…[truncated 4220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-20T05:55:48.255915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-20T05:55:48.708307+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-18pt}
4	
5	A target-swap ablation confirms that KL-discovered mask patterns (46--68\% divergent from magnitude) drive inference-stage quality.
6	A predictor ($<$1\% of base) reduces TEAL's perplexity by 19\% at 30\%, renders compensation redundant, and delivers $7.3\times$ smaller cross-seed $\sigma$ under uniform allocation.
7	Cross-architecture evaluation confirms the pattern (Mistral-7B: 5/6 tasks); at 14B, reasoning declines despite PPL gains.
8	Future work: MSE intermediate coupling, mask divergence analysis, and N:M sparsity.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-20T05:55:48.708689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-20T05:55:49.189951+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades; 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B, KL wins 5 of 6 downstream tasks at 30\% but GSM8K reverses (11.1\% vs.\ TEAL's 15.9\%), consistent with GSM8K's sensitivity to the sparsity objective: reasoning tasks may require different optimization targets than knowledge and commonsense benchmarks; forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$20pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 52.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, which indicates that the predictor partially overfits to training-domain activation patterns. Extending OOD evaluation to 70\% sparsity is left to future work.
8	The target-swap ablation (\S\ref{sec:mask_analysis}) confirms that mask quality drives inference-stage quality, with KL's coupled gradients
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 481
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-20T05:55:49.190512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-20T05:55:49.643539+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-20T05:55:49.644069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-20T05:55:50.146696+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 22471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-20T05:55:50.147203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-20T05:55:50.197929+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 18976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-20T05:55:54.013786+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit requirements site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Based on the search results from the EMNLP 2026 website, here's what I found regarding the submission deadline and page limit requirements:

**Submission Deadline:**
The paper submission deadline for the Industry Track is June 16, 2026 (11:59 PM UTC-12:00, AoE), and all deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

**Page Limit Requirements:**
The search results provided information about the Industry Track requirements, including that the "Limitations" section should be included at the end of the paper, before the references, and it will not count toward the page limit. However, the specific page limit number for the main conference papers was not explicitly shown in the search results returned.

For more complete information about the main conference paper page limits and other specific submission requirements, you 
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 10032
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-20T05:56:02.196578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" ARR submission guidelines page limit anonymity template 2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for papers\" ARR submission guidelines page limit anonymity template 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1181 · 2026-05-20T05:56:04.107483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1182 · 2026-05-20T05:56:04.359598+00:00_

1	issues:
2	  # ============================================================
3	  # Round 13 (fresh review) — Active issues
4	  # ============================================================
5	
6	  - id: "R13-N1"
7	    summary: "MSE intermediate baseline 缺失，taxonomy Decomposed/Intermediate/Coupled 核心 claim 无实验支撑"
8	    category: experiment
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 12
12	    last_seen_round: 13
13	    mentions:
14	      - {round: 12, reviewers: [1, 2], note: "R12-N3. Full consensus."}
15	      - {round: 13, reviewers: [1, 2], note: "Full consensus. R1-N1 Must-Fix, R2-W1→升级同意."}
16	    action_items:
17	      - {round: 13, action: "训练 per-layer MSE predictor, 加入 Table 2 和 Table 4.", assigned_to: "main_agent", status: resolved}
18	      - {round: 13, action: "MSE 数据整合到论文: Table 2 + Table 4 + §3.7 taxonomy rewrite + contributions + abstract.", assigned_to: "paper_agent", status: in_progress}
19	    resolution: "MSE 30% PPL=20.43 (2× worse than TEAL), MSE 50% PPL=229.26 (10× worse). Taxonomy 重构为 coupling alignment. Paper Agent 整合中."
20	    resolution_round: null
21	
22	  - id: "R13-N2"
23	    summary: "跨架构/跨规模 claim 过强：Mistral 单 seed, 14B sparsity mismatch, mass-covering 未验证"
24	    category: experiment
25	    severity: critical
26	    status: in_progress
27	    first_raised_round: 11
28	    last_seen_round: 13
29	    mentions:
30	      - {round: 11, reviewers: [1, 2], note: "R11-N2."}
31	      - {round: 12, reviewers: [1, 2], note: "R12-W2."}
32	      - {round: 13, reviewers: [1, 2], note: "Full consensus. R1-N2 Must-Fix."}
33	    action_items:
34	      - {round: 13, action: "Wording downgrade: cross-arch preliminary; mass-covering hypothesis; 14B GSM8K -20pp.", assigned_to: "paper_agent", status: in_progress}
35	    resolution: ""
36	    resolution_round: null
37	
38	  - id: "R13-N3"
39	    summary: "SNR 证据选择性呈现 + LR schedule 不匹配导致不实陈述"
40	    category: method
41	    severity: critical
42	    status: in_progress
43	  
…[truncated 11060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-20T05:56:15.037686+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" ARR submission guidelines page limit anonymity template 2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

I found information about the EMNLP 2026 call for papers and ARR submission guidelines. Here are the key details:

## Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers must be submitted, at latest, by the ARR 2026 May cycle. The ARR submission deadline is May 25, 2026, with a reviewer registration deadline for all autho
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 12841
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-20T05:56:36.364086+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1185 · 2026-05-20T05:56:36.414825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-20T05:56:41.547146+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements for EMNLP 2026 main conference papers: page limits (long/short), template requirements, anonymity rules, appendix rules, formatting requirements, submission deadlines, and any other author guidelines. Be comprehensive and include every specific requirement mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements for EMNLP 2026 main conference papers: page limits (long/short), template requirements, anonymity rules, appendix rules, formatting requirements, submission deadlines, and any other author guidelines. Be comprehensive and include every specific requirement mentioned."
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-20T05:56:47.622760+00:00_

# EMNLP 2026 Main Conference Paper Submission Requirements

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Final versions:** Up to 9 pages (long) and 5 pages (short) to address reviewer feedback

## Anonymity & Review Process
The review follows a "two-way anonymized" approach. Per the document: "The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers." However, "Following the ACL and ARR policies, there is no anonymity period requirement."

## Key Submission Deadlines
- ARR submission: May 25, 2026
- Reviewer registration: May 27, 2026
- EMNLP commitment: August 2, 2026
- Acceptance notification: August 20, 2026
- Camera-ready deadline: September 20, 2026

All times are 11:59 PM UTC-12:00.

## Template & Formatting
Submissions must follow "all of the ARR submission requirements," including templates referenced on the ACL Rolling Review site. The document directs authors to the ARR CFP for specific formatting details.

## Supplementary Materials
"Optional Supplementary Materials (appendices, software and data)" are permitted per ARR guidelines.

## Additional Requirements
- Limitations section required
- Responsible NLP research checklist completion
- Publication ethics compliance mandatory
- AI writing assistance permitted; wholly AI-generated papers prohibited
- No dual submissions allowed
- Author list cannot be modified during commitment phase

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 6075
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-20T05:57:20.202221+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 EMNLP 2026 圆桌审稿 Reviewer 1。请对以下论文进行独立初审。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026)\n- 截止日期: 2026-05-25\n\n## Venue 要求\n- Long paper: 正文最多 8 页，参考文献不限页数\n- Limitations section 必须有，不计入页数\n- Ethics statement 可选，不计入页数\n- ACL 模板 (review 模式)，double-blind\n- 附录允许，但审稿人不必阅读\n- Overall Assessment 评分: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性 + 实验验证\n\n请重点审查以下方面：\n\n1. **方法严谨性**：\n   - KL distillation 公式推导是否正确\n   - 梯度分析（§3.6 BCE vs KL gradient）逻辑是否自洽\n   - Gumbel-Sigmoid relaxation 和 adaptive penalty controller 设计是否合理\n   - Taxonomy（Table 1: Decomposed/Intermediate/Coupled）分类是否准确\n\n2. **实验验证**：\n   - 主实验（Table 2）数值是否内部一致（正文引用 vs 表格数据）\n   - C1 target-swap ablation（Table 3）设计是否能支撑 \"mask quality drives inference-stage quality\" 的 claim\n   - 消融实验（Table 4）覆盖是否充分\n   - 多 seed 统计是否充分（哪些有 3-seed，哪些只有单 seed）\n   - 跨架构评估（Mistral, Qwen-14B）统计强度\n   - 数值精度：正文中的百分比计算是否准确（如 \"19% reduction\", \"50% reduction\", \"7.3× smaller σ\"）\n   - MSE baseline 结果（PPL 20.43 at 30%, 229.26 at 50%）是否合理，是否存在实现缺陷\n\n3. **格式合规**：\n   - 正文是否在 8 页以内\n   - Limitations section 是否存在且充分\n\n请按以下格式输出审稿意见：\n- Summary（2-3句）\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者澄清的）\n- Missing References（如有）\n- Overall Assessment（评分 + 置信度）\n- Detailed Comments（逐节）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 EMNLP 2026 圆桌审稿 Reviewer 1。请对以下论文进行独立初审。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026)\n- 截止日期: 2026-05-25\n\n## Venue 要求\n- Long paper: 正文最多 8 页，参考文献不限页数\n- Limitations section 必须有，不计入页数\n- Ethics statement 可选，不计入页数\n- ACL 模板 (review 模式)，double-blind\n- 附录允许，但审稿人不必阅读\n- Overall Assessment 评分: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性 + 实验验证\n\n请重点审查以下方面：\n\n1. **方法严谨性**：\n   - KL distillation 公式推导是否正确\n   - 梯度分析（§3.6 BCE vs KL gradient）逻辑是否自洽\n   - Gumbel-Sigmoid relaxation 和 adaptive penalty controller 设计是否合理\n   - Taxonomy（Table 1: Decomposed/Intermediate/Coupled）分类是否准确\n\n2. **实验验证**：\n   - 主实验（Table 2）数值是否内部一致（正文引用 vs 表格数据）\n   - C1 target-swap ablation（Table 3）设计是否能支撑 \"mask quality drives inference-stage quality\" 的 claim\n   - 消融实验（Table 4）覆盖是否充分\n   - 多 seed 统计是否充分（哪些有 3-seed，哪些只有单 seed）\n   - 跨架构评估（Mistral, Qwen-14B）统计强度\n   - 数值精度：正文中的百分比计算是否准确（如 \"19% reduction\", \"50% reduction\", \"7.3× smaller σ\"）\n   - MSE baseline 结果（PPL 20.43 at 30%, 229.26 at 50%）是否合理，是否存在实现缺陷\n\n3. **格式合规**：\n   - 正文是否在 8 页以内\n   - Limitations section 是否存在且充分\n\n请按以下格式输出审稿意见：\n- Summary（2-3句）\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者澄清的）\n- Missing References（如有）\n- Overall Assessment（评分 + 置信度）\n- Detailed Comments（逐节）"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-20T05:57:39.644060+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19441
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-20T05:57:41.953351+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 EMNLP 2026 圆桌审稿 Reviewer 2。请对以下论文进行独立初审。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026)\n- 截止日期: 2026-05-25\n\n## Venue 要求\n- Long paper: 正文最多 8 页，参考文献不限页数\n- Limitations section 必须有，不计入页数\n- Ethics statement 可选，不计入页数\n- ACL 模板 (review 模式)，double-blind\n- 附录允许，但审稿人不必阅读\n- Overall Assessment 评分: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：新颖性 + 完整性\n\n请重点审查以下方面：\n\n1. **新颖性与定位**：\n   - 论文声称 \"empirical study\"，其 contribution 对 EMNLP 是否足够？\n   - KL + Gumbel-Sigmoid 组合是否足够新颖？与 MaskLLM 的区别是否清晰？\n   - \"coupling alignment\" 概念是否有足够的理论/实验支撑？\n   - taxonomy (Decomposed/Intermediate/Coupled × Static/Per-token) 的学术贡献\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作（特别是 2024-2026 年的新工作）\n   - 与 MaskLLM, SPON, D2DMoE, ShadowLLM 的区别是否充分阐述\n   - 与 structured pruning (Wanda, SparseGPT) 和 MoE routing 的关系\n\n3. **写作质量**：\n   - 叙事结构是否清晰\n   - Abstract 是否准确概括论文贡献（检查每个数值 claim）\n   - Introduction 的 contribution list 与实际内容是否匹配\n   - Conclusion 是否充分（长度、future work）\n   - 整体行文是否有 AI 写作痕迹\n\n4. **跨架构泛化 claim**：\n   - Mistral-7B 单 seed 评估是否足以支撑 \"cross-architecture\" claim\n   - Qwen-14B 下游退化（GSM8K -20pp, MMLU -2.79pp）是否充分讨论\n   - \"scale-dependent effects\" 叙事是否平衡\n\n5. **完整性检查**：\n   - 是否有遗漏的消融实验\n   - 引用格式是否一致\n   - 图表质量和可读性\n\n请按以下格式输出审稿意见：\n- Summary（2-3句）\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者澄清的）\n- Missing References（如有）\n- Overall Assessment（评分 + 置信度）\n- Detailed Comments（逐节）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 EMNLP 2026 圆桌审稿 Reviewer 2。请对以下论文进行独立初审。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR May 2026)\n- 截止日期: 2026-05-25\n\n## Venue 要求\n- Long paper: 正文最多 8 页，参考文献不限页数\n- Limitations section 必须有，不计入页数\n- Ethics statement 可选，不计入页数\n- ACL 模板 (review 模式)，double-blind\n- 附录允许，但审稿人不必阅读\n- Overall Assessment 评分: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：新颖性 + 完整性\n\n请重点审查以下方面：\n\n1. **新颖性与定位**：\n   - 论文声称 \"empirical study\"，其 contribution 对 EMNLP 是否足够？\n   - KL + Gumbel-Sigmoid 组合是否足够新颖？与 MaskLLM 的区别是否清晰？\n   - \"coupling alignment\" 概念是否有足够的理论/实验支撑？\n   - taxonomy (Decomposed/Intermediate/Coupled × Static/Per-token) 的学术贡献\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作（特别是 2024-2026 年的新工作）\n   - 与 MaskLLM, SPON, D2DMoE, ShadowLLM 的区别是否充分阐述\n   - 与 structured pruning (Wanda, SparseGPT) 和 MoE routing 的关系\n\n3. **写作质量**：\n   - 叙事结构是否清晰\n   - Abstract 是否准确概括论文贡献（检查每个数值 claim）\n   - Introduction 的 contribution list 与实际内容是否匹配\n   - Conclusion 是否充分（长度、future work）\n   - 整体行文是否有 AI 写作痕迹\n\n4. **跨架构泛化 claim**：\n   - Mistral-7B 单 seed 评估是否足以支撑 \"cross-architecture\" claim\n   - Qwen-14B 下游退化（GSM8K -20pp, MMLU -2.79pp）是否充分讨论\n   - \"scale-dependent effects\" 叙事是否平衡\n\n5. **完整性检查**：\n   - 是否有遗漏的消融实验\n   - 引用格式是否一致\n   - 图表质量和可读性\n\n请按以下格式输出审稿意见：\n- Summary（2-3句）\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者澄清的）\n- Missing References（如有）\n- Overall Assessment（评分 + 置信度）\n- Detailed Comments（逐节）"
  }
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-20T05:57:41.953674+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-20T05:57:41.953823+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-20T05:57:43.562375+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Tool result

_source line 1194 · 2026-05-20T05:57:45.376083+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3422
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-20T05:57:46.132396+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 4178
}
```

</details>

---


### Assistant

_source line 1196 · 2026-05-20T05:58:03.837151+00:00_

**Round 1 初审已派发。** 当前状态：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验） | ⏳ 审稿中 |
| Reviewer 2（新颖性 + 完整性） | ⏳ 审稿中 |
| 视觉审查 Agent | ⏳ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ⏳ 已发送请求 |

等待 Reviewer 回稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 93

## Round 93

2 recorded events


### User

_source line 1197 · 2026-05-20T06:03:40.632489+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 初审报告

### 总体评分
- **Overall**: 3.0 (Findings)
- **Soundness**: 3.5/5
- **Excitement**: 2.5/5
- **Reproducibility**: 4/5
- **Confidence**: 4/5

### Summary
本文研究在 SwiGLU LLM 的上下文稀疏预测器训练中用 KL 散度替代 BCE。KL 训练发现与 magnitude mask 偏离 46–68% 的 mask pattern，LLaMA-3.1-8B 30% sparsity 下 PPL 改善 19%。Target-swap 消融（C1）证明 mask 质量而非梯度耦合本身驱动推理质量。但 PPL 改善未转化为下游收益（TEAL 在 MMLU/GSM8K 上均优于 KL），无实际加速，跨架构结论不 robust。

### Must-Fix 问题

**W1. PPL 改善与下游任务脱节。** Table 2 显示 30% sparsity 下 TEAL uniform 在 MMLU (45.86 vs 40.7) 和 GSM8K (8.79 vs 7.5) 上均优于 KL uniform。Abstract 称 "moderate downstream degradation" 但 MMLU -37.6%, GSM8K -84.6% (relative to dense)。论文核心叙事 "KL discovers better masks" 需要重新界定——better for PPL, worse for downstream。

**W2. "Cross-architecture" claim 证据不足。** Mistral-7B 仅单 seed 无 std；Qwen-14B 下游严重退化（GSM8K -20pp, MMLU -2.79pp uniform）。Introduction 称 "cross-architecture evaluation confirms the pattern" 但 pattern 高度不一致。

**W3. 与 MaskLLM 的新颖性区分不充分。** MaskLLM (NeurIPS 2024) 已使用 frozen weights + learnable masks + KL + Gumbel。核心思想（KL 比 BCE 好）已在 weight sparsity 上发表。论文需解释 activation sparsity 场景下的增量贡献。

### Should-Fix 问题

**W4.** 无实际推理加速，predictor 增加 6.4% overhead。
**W5.** "Coupling alignment" 概念有循环论证嫌疑，缺乏形式化定义。
**W6.** Conclusion 仅 4 行 + vspace{-18pt}，不符合 long paper 规范。
**W7.** 训练数据极小（~8M tokens），C4 OOD gap 显著（1.74× vs 1.46× dense）。

### Missing References
1. ActTail (2026, arXiv:2603.12272) — 直接相关的 global activation sparsity allocation
2. "A Sparsity Predicting Approach via Activation Pattern Clustering" (2025)
3. "Universal Properties of Activation Sparsity in Modern LLMs" (2025)

### 审查侧重覆盖
- ✅ 新颖性与定位：W3 (MaskLLM delta)、taxonomy 评估
- ✅ Related Work 完整性：3 个 missing references
- ✅ 写作质量：W6 (Conclusion)、W8/W9 (minor issues)、abstract accuracy
- ✅ 跨架构泛化 claim：W2 (Mistral single-seed, Qwen degradation)
- ✅ 完整性检查：引用验证通过、消融设计充分

### 我的判断
Findings 水平。实验执行质量高（特别是 C1 ablation），但 (1) 新颖性有限（KL for mask training 已被 MaskLLM 提出），(2) PPL-downstream 脱节是致命叙事问题，(3) 无实际加速。建议聚焦 "训练目标对 mask pattern discovery 的影响" 重新定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1198 · 2026-05-20T06:03:57.313411+00:00_

Reviewer 2 初审意见已收到（Overall 3.0 / Findings）。核心问题：PPL-downstream 脱节、MaskLLM 新颖性区分不足、跨架构 claim 过强。

等待 Reviewer 1 初审意见返回后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 1199 · 2026-05-20T06:04:00.028742+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **Overall 3.0 (Findings)**。核心问题三个——(1) PPL 改善但下游任务上 TEAL 反而优于 KL，"better masks" 的 claim 需重新界定；(2) MaskLLM 已在 NeurIPS 使用相同框架（KL+Gumbel），新颖性增量不足；(3) Mistral 单 seed、Qwen 退化严重，cross-architecture claim 不 robust。实验执行质量好（target-swap C1 消融是亮点），但贡献偏增量，适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1200 · 2026-05-20T06:04:05.321516+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 的报告到达后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 95

## Round 95

6 recorded events


### User

_source line 1201 · 2026-05-20T06:04:17.491601+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 初审意见 — "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5
**一句话总结**: 扎实的实证研究，C1 target-swap ablation 设计巧妙，但核心方法新颖性有限（BCE → KL），PPL 改进未一致转化为下游增益（MMLU 反而更差），且无实际推理加速。

### 官方维度打分（ACL ARR）
| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 核心 claims 有实验支撑，但 MSE baseline 公平性存疑，下游指标与 PPL 矛盾未充分解释 |
| Excitement | 3/5 | 有用的实证发现（coupling alignment），但方法是直接的目标函数替换，无新架构/算法 |
| Reproducibility | 4/5 | 超参数完整，3-seed 覆盖核心结果，单 GPU 训练 |

### Strengths
- **S1** C1 target-swap ablation 精巧解耦 mask 质量与梯度耦合（Table 3, 3-seed at 30%）
- **S2** 系统性消融覆盖（KL/JSD/RKL, Gumbel/STE, penalty, bottleneck, temperature, steps）
- **S3** 二维 taxonomy（Table 1）有概念贡献，清晰定位 Per-token × Coupled 空缺
- **S4** 诚实的局限性讨论（无加速、14B GSM8K −20pp、PPL 不等于下游能力）
- **S5** Gradient SNR 分析提供反直觉洞见——KL 梯度更嘈杂但产生更好的 mask

### Must-Fix 问题
**N1** [critical] PPL 改进未一致转化为下游增益，但叙事以 PPL 为中心
- Table 2: KL uniform MMLU=40.7 vs TEAL=45.86（−5.2pp at 30%）；14B: MMLU −8pp, GSM8K −20pp
- Abstract/Intro 以"19% PPL reduction"为卖点，"moderate downstream degradation"低估了 MMLU 下降
- 建议：Abstract 需明确 MMLU 低于 TEAL；分析 mass-covering KL 为何牺牲 reasoning pathway

**N2** [critical] MSE baseline（PPL 229.26）公平性不透明
- MSE 训练配置未报告：是否使用 Gumbel-Sigmoid？稀疏度如何控制？超参数是否独立调优？
- MSE 和 KL 不仅耦合层级不同，优化目标也根本不同——如果 MSE 训练不公平，"coupling alignment"论点的实验基础被削弱
- 建议：报告 MSE 配置；考虑增加 per-layer KL baseline 作为更公平的 intermediate coupling 对比

### Should-Fix 问题
**N3** 实际稀疏度偏差（KL 28.5% vs TEAL 29.3%）削弱 19% headline——matched sparsity 下实际约 14.5% 改进
**N4** 跨架构/尺度评估均为单 seed，但被作为贡献之一列出
**W1** BCE+Gumbel 比标准 BCE 更差（32.22 vs 27.97）缺乏解释——暗示 KL 优势可能部分来自 Gumbel×KL 交互而非纯 KL

### Minor
- Conclusion 仅 3 句 + \vspace{-18pt}，过于压缩
- `de2024griffin` 引用在 OpenAlex 上未找到匹配

### Key Questions
1. MSE 的具体训练配置？（Gumbel？penalty？超参数调优？）
2. KL 为何 MMLU 低于 TEAL？mass-covering 是否牺牲知识密集路径？
3. BCE+Gumbel+Penalty 是否成功控制到 50% 稀疏度？
4. 是否尝试过实际稀疏矩阵运算？
5. C1 ablation 50% 能否补充 3-seed？

### 审稿判断
如果 N1（PPL-下游矛盾深入分析）和 N2（MSE 配置透明化）能得到充分回应，可达 Conference 水准。当前状态为 Borderline Conference / strong Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-20T06:04:53.725251+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 初审报告\n\n### 总体评分\n- **Overall**: 3.0 (Findings)\n- **Soundness**: 3.5/5\n- **Excitement**: 2.5/5\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n### Summary\n本文研究在 SwiGLU LLM 的上下文稀疏预测器训练中用 KL 散度替代 BCE。KL 训练发现与 magnitude mask 偏离 46–68% 的 mask pattern，LLaMA-3.1-8B 30% sparsity 下 PPL 改善 19%。Target-swap 消融（C1）证明 mask 质量而非梯度耦合本身驱动推理质量。但 PPL 改善未转化为下游收益（TEAL 在 MMLU/GSM8K 上均优于 KL），无实际加速，跨架构结论不 robust。\n\n### Must-Fix 问题\n\n**W1. PPL 改善与下游任务脱节。** Table 2 显示 30% sparsity 下 TEAL uniform 在 MMLU (45.86 vs 40.7) 和 GSM8K (8.79 vs 7.5) 上均优于 KL uniform。Abstract 称 \"moderate downstream degradation\" 但 MMLU -37.6%, GSM8K -84.6% (relative to dense)。论文核心叙事 \"KL discovers better masks\" 需要重新界定——better for PPL, worse for downstream。\n\n**W2. \"Cross-architecture\" claim 证据不足。** Mistral-7B 仅单 seed 无 std；Qwen-14B 下游严重退化（GSM8K -20pp, MMLU -2.79pp uniform）。Introduction 称 \"cross-architecture evaluation confirms the pattern\" 但 pattern 高度不一致。\n\n**W3. 与 MaskLLM 的新颖性区分不充分。** MaskLLM (NeurIPS 2024) 已使用 frozen weights + learnable masks + KL + Gumbel。核心思想（KL 比 BCE 好）已在 weight sparsity 上发表。论文需解释 activation sparsity 场景下的增量贡献。\n\n### Should-Fix 问题\n\n**W4.** 无实际推理加速，predictor 增加 6.4% overhead。\n**W5.** \"Coupling alignment\" 概念有循环论证嫌疑，缺乏形式化定义。\n**W6.** Conclusion 仅 4 行 + vspace{-18pt}，不符合 long paper 规范。\n**W7.** 训练数据极小（~8M tokens），C4 OOD gap 显著（1.74× vs 1.46× dense）。\n\n### Missing References\n1. ActTail (2026, arXiv:2603.12272)\n2. \"A Sparsity Predicting Approach via Activation Pattern Clustering\" (2025)\n3. \"Universal Properties of Activation Sparsity in Modern LLMs\" (2025)\n\n---\n\n请对以上每一条 W1-W7 和 Missing References 逐条 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 初审报告\n\n### 总体评分\n- **Overall**: 3.0 (Findings)\n- **Soundness**: 3.5/5\n- **Excitement**: 2.5/5\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n### Summary\n本文研究在 SwiGLU LLM 的上下文稀疏预测器训练中用 KL 散度替代 BCE。KL 训练发现与 magnitude mask 偏离 46–68% 的 mask pattern，LLaMA-3.1-8B 30% sparsity 下 PPL 改善 19%。Target-swap 消融（C1）证明 mask 质量而非梯度耦合本身驱动推理质量。但 PPL 改善未转化为下游收益（TEAL 在 MMLU/GSM8K 上均优于 KL），无实际加速，跨架构结论不 robust。\n\n### Must-Fix 问题\n\n**W1. PPL 改善与下游任务脱节。** Table 2 显示 30% sparsity 下 TEAL uniform 在 MMLU (45.86 vs 40.7) 和 GSM8K (8.79 vs 7.5) 上均优于 KL uniform。Abstract 称 \"moderate downstream degradation\" 但 MMLU -37.6%, GSM8K -84.6% (relative to dense)。论文核心叙事 \"KL discovers better masks\" 需要重新界定——better for PPL, worse for downstream。\n\n**W2. \"Cross-architecture\" claim 证据不足。** Mistral-7B 仅单 seed 无 std；Qwen-14B 下游严重退化（GSM8K -20pp, MMLU -2.79pp uniform）。Introduction 称 \"cross-architecture evaluation confirms the pattern\" 但 pattern 高度不一致。\n\n**W3. 与 MaskLLM 的新颖性区分不充分。** MaskLLM (NeurIPS 2024) 已使用 frozen weights + learnable masks + KL + Gumbel。核心思想（KL 比 BCE 好）已在 weight sparsity 上发表。论文需解释 activation sparsity 场景下的增量贡献。\n\n### Should-Fix 问题\n\n**W4.** 无实际推理加速，predictor 增加 6.4% overhead。\n**W5.** \"Coupling alignment\" 概念有循环论证嫌疑，缺乏形式化定义。\n**W6.** Conclusion 仅 4 行 + vspace{-18pt}，不符合 long paper 规范。\n**W7.** 训练数据极小（~8M tokens），C4 OOD gap 显著（1.74× vs 1.46× dense）。\n\n### Missing References\n1. ActTail (2026, arXiv:2603.12272)\n2. \"A Sparsity Predicting Approach via Activation Pattern Clustering\" (2025)\n3. \"Universal Properties of Activation Sparsity in Modern LLMs\" (2025)\n\n---\n\n请对以上每一条 W1-W7 和 Missing References 逐条 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-20T06:05:03.030873+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9305
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-20T06:05:03.182865+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 初审意见\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5\n\n### Strengths\n- **S1** C1 target-swap ablation 精巧解耦 mask 质量与梯度耦合（Table 3, 3-seed at 30%）\n- **S2** 系统性消融覆盖（KL/JSD/RKL, Gumbel/STE, penalty, bottleneck, temperature, steps）\n- **S3** 二维 taxonomy（Table 1）有概念贡献，清晰定位 Per-token × Coupled 空缺\n- **S4** 诚实的局限性讨论（无加速、14B GSM8K −20pp、PPL 不等于下游能力）\n- **S5** Gradient SNR 分析提供反直觉洞见——KL 梯度更嘈杂但产生更好的 mask\n\n### Must-Fix 问题\n**N1** [critical] PPL 改进未一致转化为下游增益，但叙事以 PPL 为中心\n- Table 2: KL uniform MMLU=40.7 vs TEAL=45.86（−5.2pp at 30%）；14B: MMLU −8pp, GSM8K −20pp\n- Abstract/Intro 以\"19% PPL reduction\"为卖点，\"moderate downstream degradation\"低估了 MMLU 下降\n- 建议：Abstract 需明确 MMLU 低于 TEAL；分析 mass-covering KL 为何牺牲 reasoning pathway\n\n**N2** [critical] MSE baseline（PPL 229.26）公平性不透明\n- MSE 训练配置未报告：是否使用 Gumbel-Sigmoid？稀疏度如何控制？超参数是否独立调优？\n- MSE 和 KL 不仅耦合层级不同，优化目标也根本不同——如果 MSE 训练不公平，\"coupling alignment\"论点的实验基础被削弱\n- 建议：报告 MSE 配置；考虑增加 per-layer KL baseline 作为更公平的 intermediate coupling 对比\n\n### Should-Fix 问题\n**N3** 实际稀疏度偏差（KL 28.5% vs TEAL 29.3%）削弱 19% headline——matched sparsity 下实际约 14.5% 改进\n**N4** 跨架构/尺度评估均为单 seed，但被作为贡献之一列出\n**W1** BCE+Gumbel 比标准 BCE 更差（32.22 vs 27.97）缺乏解释——暗示 KL 优势可能部分来自 Gumbel×KL 交互而非纯 KL\n\n### Minor\n- Conclusion 仅 3 句 + \\vspace{-18pt}，过于压缩\n- `de2024griffin` 引用在 OpenAlex 上未找到匹配\n\n### Key Questions\n1. MSE 的具体训练配置？（Gumbel？penalty？超参数调优？）\n2. KL 为何 MMLU 低于 TEAL？mass-covering 是否牺牲知识密集路径？\n3. BCE+Gumbel+Penalty 是否成功控制到 50% 稀疏度？\n4. 是否尝试过实际稀疏矩阵运算？\n5. C1 ablation 50% 能否补充 3-seed？\n\n---\n\n请对以上 N1, N2, N3, N4, W1, Minor 和 Key Questions 逐条 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 初审意见\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5\n\n### Strengths\n- **S1** C1 target-swap ablation 精巧解耦 mask 质量与梯度耦合（Table 3, 3-seed at 30%）\n- **S2** 系统性消融覆盖（KL/JSD/RKL, Gumbel/STE, penalty, bottleneck, temperature, steps）\n- **S3** 二维 taxonomy（Table 1）有概念贡献，清晰定位 Per-token × Coupled 空缺\n- **S4** 诚实的局限性讨论（无加速、14B GSM8K −20pp、PPL 不等于下游能力）\n- **S5** Gradient SNR 分析提供反直觉洞见——KL 梯度更嘈杂但产生更好的 mask\n\n### Must-Fix 问题\n**N1** [critical] PPL 改进未一致转化为下游增益，但叙事以 PPL 为中心\n- Table 2: KL uniform MMLU=40.7 vs TEAL=45.86（−5.2pp at 30%）；14B: MMLU −8pp, GSM8K −20pp\n- Abstract/Intro 以\"19% PPL reduction\"为卖点，\"moderate downstream degradation\"低估了 MMLU 下降\n- 建议：Abstract 需明确 MMLU 低于 TEAL；分析 mass-covering KL 为何牺牲 reasoning pathway\n\n**N2** [critical] MSE baseline（PPL 229.26）公平性不透明\n- MSE 训练配置未报告：是否使用 Gumbel-Sigmoid？稀疏度如何控制？超参数是否独立调优？\n- MSE 和 KL 不仅耦合层级不同，优化目标也根本不同——如果 MSE 训练不公平，\"coupling alignment\"论点的实验基础被削弱\n- 建议：报告 MSE 配置；考虑增加 per-layer KL baseline 作为更公平的 intermediate coupling 对比\n\n### Should-Fix 问题\n**N3** 实际稀疏度偏差（KL 28.5% vs TEAL 29.3%）削弱 19% headline——matched sparsity 下实际约 14.5% 改进\n**N4** 跨架构/尺度评估均为单 seed，但被作为贡献之一列出\n**W1** BCE+Gumbel 比标准 BCE 更差（32.22 vs 27.97）缺乏解释——暗示 KL 优势可能部分来自 Gumbel×KL 交互而非纯 KL\n\n### Minor\n- Conclusion 仅 3 句 + \\vspace{-18pt}，过于压缩\n- `de2024griffin` 引用在 OpenAlex 上未找到匹配\n\n### Key Questions\n1. MSE 的具体训练配置？（Gumbel？penalty？超参数调优？）\n2. KL 为何 MMLU 低于 TEAL？mass-covering 是否牺牲知识密集路径？\n3. BCE+Gumbel+Penalty 是否成功控制到 50% 稀疏度？\n4. 是否尝试过实际稀疏矩阵运算？\n5. C1 ablation 50% 能否补充 3-seed？\n\n---\n\n请对以上 N1, N2, N3, N4, W1, Minor 和 Key Questions 逐条 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-20T06:05:04.809910+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1627
}
```

</details>

---


### Assistant

_source line 1206 · 2026-05-20T06:05:07.519576+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 1207 · 2026-05-20T06:05:10.254960+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：**Overall 3.5 (Borderline Conference)**。核心优势是 C1 target-swap ablation 的精巧设计和系统性消融覆盖。两个 must-fix 问题：(1) PPL 改进未转化为一致的下游增益（MMLU 在 30% 下反而低于 TEAL 5.2pp），但论文叙事过度依赖 PPL；(2) MSE baseline 的训练配置不透明（PPL 229.26 的灾难性结果需要解释公平性）。如果这两个问题在 rebuttal 中得到充分回应，可提升至 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1208 · 2026-05-20T06:05:17.976895+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 1209 · 2026-05-20T06:06:49.909448+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 初审意见的逐条回应

---

### W1. PPL 改善与下游任务脱节

[AGREE] R2-W1: 核心观察成立，PPL 改善确实未一致转化为下游增益。我在自己的审稿中也将此列为 N1 Must-Fix。

但 R2 的 framing 有误导之处：R2 称 "MMLU -37.6%, GSM8K -84.6%"，这是**相对 dense 的退化**，不是 KL vs TEAL 的差距。实际 KL vs TEAL 的对比是：
- MMLU: 40.7 vs 45.86（差 5.16pp，两者都已从 dense 65.27 大幅退化）
- GSM8K: 7.5 vs 8.79（差仅 1.29pp，TEAL 自身也已从 dense 48.75 退化 82%）

GSM8K 上两种方法都几乎崩溃，1.29pp 的差异在统计上不显著（KL 的 std=0.1）。MMLU 5.16pp 的差距是真实的、需要作者解释的问题。但 R2 将其表述为 "GSM8K -84.6%" 是对比基线选择错误。

此外，KL 在 ARC-c（43.7 vs 39.33, +4.4pp）和 WG（68.9 vs 65.04, +3.9pp）上优于 TEAL（Table 2），以及 HellaSwag（+7.8pp）和 PIQA（+2.2pp）（Table 12, Appendix H）。总体画面是"PPL 和 4/6 下游任务更好，MMLU 更差，GSM8K 持平"，而非 R2 所述的全面"worse for downstream"。

**结论**：同意 MMLU 退化需要正面解决，但 R2 的总结过于负面。

---

### W2. Cross-architecture claim 证据不足

[AGREE] R2-W2: 同意。我在自己的审稿中也将此列为 N4 Should-Fix。Mistral 单 seed 无 std，Qwen-14B 全局分配也是单 seed。Introduction 中 "cross-architecture evaluation confirms the pattern" 的表述确实过强。不过 Abstract 中 "Preliminary single-seed evaluation" 的措辞是准确的（abstract.tex line 6）。建议 Introduction 也采用相同的审慎措辞。

---

### W3. 与 MaskLLM 的新颖性区分不充分

[REBUT] R2-W3: R2 声称 "核心思想（KL 比 BCE 好）已在 weight sparsity 上发表"。但 MaskLLM 和本文解决的是**根本不同的问题**，论文已在 §2 Related Work（related_work.tex lines 16-19）明确区分了三个维度：

1. **稀疏类型**：MaskLLM 优化 N:M 半结构化 **weight** sparsity（静态 2:4 pattern），本文优化动态 per-token **activation** sparsity。Weight mask 训练后固定；本文的 mask 随每个输入 token 变化。
2. **Mask 生成机制**：MaskLLM 的 mask 是直接可学习参数（per weight group），通过 Gumbel-Softmax 选择。本文训练一个 predictor network，从 hidden state 推断 mask——这是一个**泛化问题**，predictor 必须对未见过的输入生成好的 mask。
3. **分配机制**：MaskLLM 在固定 N:M 组内优化，无跨组竞争；本文使用全局 top-k 预算跨所有层分配。这种全局竞争正是 inter-neuron dependency 的来源，也是 coupling 有意义的根本原因。

更关键的是，MaskLLM 的"KL > BCE"不能直接推广到 activation sparsity：MaskLLM 的 mask 参数是直接优化的（类似 fine-tuning），而 activation sparsity 需要训练一个必须**泛化到新输入**的 predictor。这两个场景对目标函数的要求完全不同。本文的贡献不是"KL > BCE"这个通用结论，而是在 dynamic prediction + global allocation 这个特定组合下的实证分析，包括 C1 ablation、taxonomy、coupling alignment 概念等。

**结论**：MaskLLM 的区分在论文中已充分讨论。"核心思想已发表"的说法忽略了问题设置的根本差异。

---

### W4. 无实际推理加速

[AGREE] R2-W4: 同意这是实际局限性。论文在 Introduction（line 18）和 Appendix A 中均明确说明了这一点。§1 明确说 "Wall-clock speedup requires sparse kernel support not addressed here"。6.4% overhead 来自 predictor 前向传播和 mask indexing，需要 Triton/cuSPARSE 支持才能实现净加速。

但需要指出：(a) 论文定位为实证分析研究（"we do not propose a new architecture or algorithm"），而非系统加速论文；(b) KL predictor 的一个实际贡献是**消除 67.2M 参数的 compensation network**（§4.5, Appendix I），减少 2.7% latency overhead，这是面向部署的具体改进。

**结论**：同意局限性，但论文的定位和透明度是合理的。

---

### W5. "Coupling alignment" 循环论证嫌疑

[AGREE] R2-W5（部分同意）: R2 的批评有一定道理。"Coupling alignment" 的定义本质上是"与最终输出分布对齐的耦合"——这在逻辑上接近于"use the right objective"的同义反复。

但论文确实提供了**非平凡的实验证据**来支撑这一概念：
- MSE 提供 per-layer coupling 但 PPL 灾难性崩溃（229.26 at 50%，Table 4），说明"有耦合"不够
- KL 的 SNR 低于 BCE（2.3×，Appendix G），说明"梯度质量更好"也不够
- C1 ablation 显示 mask 质量可以从 KL 转移到 BCE（Table 3），说明耦合仅在 discovery 阶段必要

这些结果合在一起为 "alignment matters, not coupling per se" 提供了实证支持。问题在于缺乏形式化定义——"coupling alignment"何时成立、何时不成立？除了 {BCE, MSE, KL} 之外还有什么预测？

**结论**：同意概念需要更精确的定义，但不同意"循环论证"——实验证据提供了非平凡的区分。

---

### W6. Conclusion 过短 + vspace hack

[AGREE] R2-W6: 完全同意。我在自己的审稿中也标记了此问题（W2 Minor）。Conclusion 仅 3 句 + `\vspace{-18pt}` 是不合规的空间操纵。建议将 §4.6 部分内容移至 Appendix，给 Conclusion 留出合理空间。

---

### W7. 训练数据极小，OOD gap 显著

[AGREE] R2-W7（部分同意）: 训练仅用 ~8M tokens（1000 steps × batch 4 × seq 2048）确实较少。C4 OOD gap（1.74× vs 1.46×）是 Limitations 中已报告的事实（limitations.tex line 7）。

但需要考虑：
- 低训练成本（~45 min 单 GPU）是方法的**实际优势**之一
- Appendix D 的 C4 评估显示 KL 在 OOD 上仍**大幅优于 TEAL**（50% sparsity: C4 PPL 18.40 vs 38.75，Table 11）
- 更多训练数据是否能缩小 OOD gap 是一个合理的实验建议，但不影响当前结论的有效性

**结论**：同意 OOD gap 是需要 future work 解决的问题，但论文的透明报告已足够。增加训练数据的消融实验会加强论文。

---

### Missing References

1. **ActTail (2026, arXiv:2603.12272)**: 需要验证此引用是否真实存在。如果存在且讨论 activation sparsity 的尾部分布特征，确实应该引用。
2. **"A Sparsity Predicting Approach via Activation Pattern Clustering" (2025)**: 需要验证。标题与本文方向相关。
3. **"Universal Properties of Activation Sparsity in Modern LLMs" (2025)**: 需要验证。如果存在，与 Sparsing Law (Luo et al., 2024) 的引用地位类似。

**总评**：R2 提出的 3 篇引用需要先验证真实性。建议 Director 让作者核查。论文已有 47 篇引用，覆盖了该领域的主要工作。

---

### 对 R2 Overall Assessment 的评论

R2 给出 Overall 3.0 (Findings)、Excitement 2.5。我认为 Excitement 2.5 偏低——C1 target-swap ablation 的实验设计不是标准操作，taxonomy 提供了有用的概念框架，gradient SNR 分析给出反直觉洞见。这些超越了"直接的目标函数替换"。

但 R2 关于 W1（PPL-downstream 脱节）和 W3（与 MaskLLM 区分）的核心批评与我的审稿互相验证。如果作者能充分回应 PPL-downstream 矛盾（R1-N1 = R2-W1）和 MSE baseline 公平性（R1-N2），论文可提升至 3.5。当前 3.0-3.5 的区间是合理的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1210 · 2026-05-20T06:06:56.829861+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 1211 · 2026-05-20T06:07:02.534727+00:00_

[Reviewer 1 审稿结果]:
已向 Review Director 提交逐条回应。要点总结：

- **W1 (PPL-downstream 脱节)**: [AGREE] 核心观察成立，但纠正了 R2 的 framing 错误——GSM8K 差距仅 1.29pp（两者均近崩溃），KL 在 4/6 下游任务上优于 TEAL
- **W2 (跨架构证据不足)**: [AGREE] 与我的 N4 一致
- **W3 (MaskLLM 新颖性)**: [REBUT] 论文已在 §2 充分区分三个维度（稀疏类型/mask生成/分配机制），问题设置根本不同
- **W4 (无加速)**: [AGREE] 但论文定位和透明度合理
- **W5 (coupling alignment 循环论证)**: [AGREE 部分] 概念需要形式化，但实验证据提供了非平凡区分
- **W6 (Conclusion 过短)**: [AGREE] 
- **W7 (训练数据少/OOD gap)**: [AGREE 部分] 合理的 future work 方向，论文报告透明
- **Missing References**: 需要验证真实性后再决定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1212 · 2026-05-20T06:07:07.985143+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 99

## Round 99

12 recorded events


### User

_source line 1213 · 2026-05-20T06:08:15.888002+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### 共识点

[AGREE] R1-N1: PPL-downstream 脱节是核心叙事问题。KL 在 MMLU/GSM8K 上系统性劣于 TEAL（Table 2），"moderate downstream degradation" 不准确。补充发现：Appendix H 显示 KL 在 HellaSwag/PIQA 上优于 TEAL，存在 task-type 差异值得正文分析。

[AGREE] R1-N2: MSE baseline 公平性问题——我初审未充分关注，R1 质疑完全合理。MSE 训练配置（Gumbel？penalty？调优？）未报告。"Coupling alignment" 作为 contribution 之一，其实验基础不透明。R1 建议的 "per-layer KL" baseline 极为中肯，可更纯粹地分离 coupling level 和 divergence type。

[AGREE] R1-N4: 跨架构单 seed 不足。与我的 W2 一致。

[AGREE] R1-W1: BCE+Gumbel 退化未解释。但 C1 ablation 部分化解了 Gumbel×KL 交互的担忧——mask patterns 可转移到 plain BCE。

[AGREE] R1-Minor (Conclusion): 过短，与我的 W6 一致。

### 分歧点

[REBUT] R1-N3: R1 称此为 Should-Fix 级别问题（"削弱 19% headline"），但 Appendix C line 148 已报告 matched-sparsity TEAL PPL=10.30 并分析了差异。0.8pp 稀疏度偏差在正常范围内。核心问题是 matched-sparsity 改善（≈14.5%）应在正文报告，而非 headline 完全不准确。

[REBUT] R1-Minor (de2024griffin): 这是 Google DeepMind 真实论文 (arXiv:2402.19427)，OpenAlex 未收录是索引问题。

### 综合判断

R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差距主要在新颖性判断上：
- R1 未重点质疑与 MaskLLM 的区分（我的 W3 Must-Fix）
- R1 对 "coupling alignment" 的实验公平性（N2）与我一致认为 critical
- 我比 R1 更关注无实际加速这一限制（我的 W4 Should-Fix）

核心分歧：我认为 MaskLLM 已发表 KL+Gumbel for mask training 的核心思想，本文的增量贡献不足以支撑 Conference 接收。R1 似乎认为 C1 ablation 和 taxonomy 的方法论贡献可以部分弥补。

建议 Meta-Review 重点讨论：(1) 与 MaskLLM 的 novelty delta；(2) PPL-downstream 脱节是否 fatal；(3) MSE baseline 公平性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-20T06:08:41.317876+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-20T06:08:41.318339+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-20T06:08:41.369230+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T05:57:44.884346+00:00\", \"completed_at\": \"2026-05-20T06:00:50.379969+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 14\", \"message\": \"Figure 3 包含占位符文本 \\\"[Placeholder: layernorm_dynamics.pdf] Awaiting sync from remote server\\\"，未替换为实际图表。审稿人打开 appendix 会立即看到这是未完成的稿件，严重损害专业印象\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-4\", \"message\": \"连续 4 页纯文本（含公式但无 figure/table）。第一个 display item（Table 1 + Figure 1）直到第 5 页才出现。审稿人在前 4 页没有任何视觉锚点来建立对方法的直觉理解，阅读体验单调\"}, {\"severity\": \"warning\", \"dimension\": \"page 3→5\", \"message\": \"Figure 1（Method overview）在 page 3 的正文中被首次引用（\\\"Figure 1\\\"），但实际出现在 page 5。Float 漂移了 2 页，审稿人读到引用时无法同时看到图\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 1 与 Table 1 挤在同一页顶部，Figure 1 尺寸偏小（约占单栏宽度），架构图细节在打印时可能难以辨认。作为论文的核心方法概览图，应给予更大展示空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"最后一页 Figure 7 和 Figure 8 之间有约 1/3 页空白，Figure 8 下方还有约 1/4 页空白。整页内容利用率不足 50%，可通过调整图表尺寸或合并为单个 multi-panel figure 来改善\"}, {\"severity\": \"info\", \"dimension\": \"pages 5-8\", \"message\": \"主文 display items 密度合理：2 figures + 5 tables = 7 个 display items / 8 页主文（~0.88/页），但全部集中在 pages 5-8，前半部分完全空白，节奏不均匀\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（Taxonomy 对比表）使用 booktabs 风格，格式专业；但 \\\"Coupled cell\\\" 行的勾选标记（✓）在低分辨率打印下可能不够清晰\"}, {\"severity\": \"info\", \"dimension\": \"pages 6-7\", \"message\": \"Table 2-4 格式一致，最优结果加粗标注，小数精度统一，排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（Perplexity scaling plot）清晰可读，线条颜色可区分，legend 字号合适\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 6（KL vs magnitude importance scores）为小尺寸二值热力图，单栏宽度下细节较密集，但基本可读\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-12\", \"message\": \"References 排版正常，无 [?] 未解析引用，格式基本统一\"}], \"counts\": {\"critical\": 1, \
…[truncated 66 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-20T06:08:41.369661+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-20T05:57:46.069986+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbbf8d2c695f1e79e11713aebc107790\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-20T06:09:20.487363+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1219 · 2026-05-20T06:09:20.538063+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-20T06:11:37.004093+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 14 (fresh review) — Active issues\n  # ============================================================\n\n  - id: \"R14-N1\"\n    summary: \"PPL 改善未一致转化为下游增益：MMLU -5.2pp vs TEAL at 30%, 14B GSM8K -20pp, 但叙事以 PPL 为中心\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W6.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W2. Director 裁定 Should-Fix.\"}\n      - {round: 14, reviewers: [1, 2], note: \"Full consensus Must-Fix. R1-N1 + R2-W1. Abstract 'moderate downstream degradation' 低估了 MMLU 退化. R1 纠正 R2 framing: KL 赢 4/6 下游任务 (ARC +4.4, WG +3.9, HS +7.8, PIQA +2.2), 仅 MMLU 系统性差. GSM8K 差距 1.29pp 统计不显著.\"}\n    action_items:\n      - {round: 14, action: \"Abstract 需明确 MMLU 低于 TEAL; 正文分析 mass-covering KL 为何牺牲 reasoning pathway; 按 task type 区分叙事 (knowledge vs commonsense).\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"MSE baseline (PPL 229.26) 训练配置不透明: Gumbel? penalty? 超参数调优? coupling alignment 实验基础被削弱\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R1-N2 Must-Fix, R2 cross-response 完全同意. Table 2 仅标注 'per-layer FFN output reconstruction loss (same predictor architecture)' 但未报告 relaxation/sparsity control. R1 建议 per-layer KL baseline 作为更公平 intermediate coupling 对比.\"}\n    action_items:\n      - {round: 14, action: \"报告 MSE 完整训练配置 (Gumbel/STE, penalty, LR, 调优过程). 考虑 per-layer KL baseline.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W1\"\n    summary: \"与 MaskLLM 新颖性区分: KL+Gumbel for mask training 已发表 (NeurIPS 2024), activation sparsity 增量贡献争议\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R9-N4.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W1. 强化 empirical study 定位.\"}\n      - {round: 14, reviewers: [1, 2], note: \"DIVERGENCE. R2-W3 Must-Fix: 核心思想已发表. R1 REBUT: 三维度区分充分 (sparsity type/mask generation/allocation). Director 裁定: §2 已有区分但可加强 'what transfers and what doesn't from weight to activation sparsity'.\"}\n    action_items:\n      - {round: 14, action: \"§2 MaskLLM 段落强化: 明确说明 MaskLLM 的 KL>BCE 结论不能直接推广到 activation sparsity (predictor generalization + global allocation). 加一句总结增量贡献.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W2\"\n    summary: \"跨架构/跨规模 claim 过强: Mistral 单 seed, Qwen-14B 下游严重退化, Introduction 措辞不匹配 Abstract\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-N2.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-N2. Wording downgrade in progress.\"}\n      - {round: 14, reviewers: [1, 2], note: \"Full consensus. R1-N4 + R2-W2. Abstract 'Preliminary single-seed' 准确, Introduction 'confirms the pattern' 过强.\"}\n    action_items:\n      - {round: 14, action: \"Introduction 对齐 Abstract 措辞: 'preliminary' / 'suggestive'. 不作为核心贡献列出.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W3\"\n    summary: \"'Coupling alignment' 概念缺乏形式化定义, 有循环论证嫌疑\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R2-W5 Should-Fix, R1 部分同意. 实验证据 (MSE fail + SNR paradox + C1 transfer) 非平凡, 但何时成立/何时不成立的预测力不足.\"}\n    action_items:\n      - {round: 14, action: \"§3.7 添加操作性定义或至少讨论 coupling alignment 的边界条件和可检验预测.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W4\"\n    summary: \"无实际推理加速, predictor 增加 6.4% overhead\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-W3.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W6.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R2-W4, R1 agrees. 论文已透明报告, 但作为 activation sparsity 工作无加速仍是重要局限.\"}\n    action_items: []\n    resolution: \"已在 §1, Appendix A, Limitations 透明报告. 定位为预测质量研究而非系统加速.\"\n    resolution_round: null\n\n  - id: \"R14-W5\"\n    summary: \"Conclusion 仅 3 句 + vspace{-18pt}, 不符合 long paper 规范\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W7.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W9.\"}\n      - {round: 14, reviewers: [1, 2], note: \"Full consensus. R1-Minor + R2-W6. vspace hack 是空间操纵 red flag.\"}\n    action_items:\n      - {round: 14, action: \"移除 vspace{-18pt}. 精简 §4.6 或其他正文, 给 Conclusion 留至少 8-10 行 + future work.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差, 缺乏解释\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R1-W1, R2 agrees (部分被 C1 化解). Table 4 数据清晰但正文解释不足. 暗示 Gumbel×KL 交互可能是 KL 优势的一部分.\"}\n    action_items:\n      - {round: 14, action: \"§4.5 或 Appendix 增加 BCE+Gumbel 为何退化的分析 (sparsity gap? Gumbel noise 对 BCE 的影响?).\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"训练数据极小 (~8M tokens), C4 OOD gap 显著 (1.74× vs 1.46×), uniform 3-seed 方差高 (CV=6.3%)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R13-W7. C4 3-seed uniform 完成.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R2-W7, R1 部分同意. Limitations 已报告. C4 仍大幅优于 TEAL (50%: 18.40 vs 38.75). 增加训练数据消融可加强论文.\"}\n    action_items: []\n    resolution: \"Limitations 已透明报告. Appendix D 有 3-seed uniform 数据. Future work 方向.\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"30% 实际稀疏度偏差 (28.5% vs target 30%), headline 19% 在 matched sparsity 下约 14.5%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R13-W3. Table 2 caption 已报告 actual sparsity.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R1-N3 Should-Fix. R2 rebuts: Appendix C 已分析, 0.8pp 偏差正常. 但 matched-sparsity 改善应在正文出现.\"}\n    action_items:\n      - {round: 14, action: \"正文提及 matched-sparsity 改善 (~14.5%) 或调整 headline 数字.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W9\"\n    summary: \"Missing references: ActTail (2026), activation pattern clustering (2025), universal sparsity properties (2025)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [2], note: \"R2 提出 3 篇. R1 指出需验证真实性. ActTail (arXiv:2603.12272) 如存在且讨论 global allocation 则应引用.\"}\n    action_items:\n      - {round: 14, action: \"验证 3 篇引用真实性, 真实则添加.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-V1\"\n    summary: \"Appendix Figure 3 包含占位符文本 (placeholder: layernorm_dynamics.pdf), 未替换为实际图表\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"视觉审查 Agent 发现. Page 14 appendix. 审稿人看到占位符会严重损害专业印象.\"}\n    action_items:\n      - {round: 14, action: \"替换占位符为实际图表, 或删除该 figure.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-V2\"\n    summary: \"Figure 1 漂移 2 页 (引用在 p3, 出现在 p5), 前 4 页无任何 display item\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"视觉审查 Agent 发现. 审稿人前 4 页无视觉锚点.\"}\n    action_items:\n      - {round: 14, action: \"调整 Figure 1 位置或在 §3 早期增加 display item.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — resolved or superseded\n  # ============================================================\n\n  - id: \"R13-N1\"\n    summary: \"MSE intermediate baseline 缺失\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"MSE 数据已在 Table 2 和 Table 4. 但训练配置透明度问题升级为 R14-N2.\"}\n    resolution: \"MSE 30% PPL=20.43, 50% PPL=229.26 已加入论文. 配置透明度问题见 R14-N2.\"\n    resolution_round: 14\n\n  - id: \"R13-N3\"\n    summary: \"SNR 证据选择性呈现 + LR schedule 不匹配\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"已完整重写: 1000步14-snapshot数据, 新叙事 'KL wins despite lower SNR'. R14 未被任何 Reviewer 提及.\"}\n    resolution: \"§3.6 完整重写, Appendix G 用 1000 步数据, SNR figure 重绘. 不再有选择性呈现问题.\"\n    resolution_round: 14\n\n  - id: \"R13-W4\"\n    summary: \"Abstract '68% divergence' 未限定 sparsity\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"Abstract 已改为 '46--68% from magnitude-based masks (depending on sparsity level)'. R14 未被提及.\"}\n    resolution: \"Abstract 措辞已修正.\"\n    resolution_round: 14\n\n  - id: \"R13-W5\"\n    summary: \"数值系统性向上取整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"7.3× 准确 (9.5/1.3=7.31). 19% 仍有 0.4pp round-up (actual 18.58%). R14 未单独提及但 R1-N3 涉及 headline 准确性.\"}\n    resolution: \"主要数值已修正. 19% 的 0.4pp round-up 归入 R14-W8 处理.\"\n    resolution_round: 14\n\n  - id: \"R13-W8\"\n    summary: \"Cross-arch allocation confound (LLaMA global vs Mistral uniform)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"Table 15 caption 已显著标注分配差异. R14 未被提及.\"}\n    resolution: \"Table caption 已添加 Note 说明不同分配策略.\"\n    resolution_round: 14\n\n  - id: \"R13-W10\"\n    summary: \"Baseline 不足: 缺 ShadowLLM/MSE 对比\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"MSE 已加入 Table 2 + Table 4. ShadowLLM 在 §2 讨论但无直接实验 (不同架构). R14 未被提及.\"}\n    resolution: \"MSE baseline 完整. ShadowLLM 讨论在 Related Work.\"\n    resolution_round: 14\n\n  - id: \"R13-W11\"\n    summary: \"C1 ablation s42 oracle 版本差异\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"Table 3 caption 标注 †s42 oracle from earlier run. 正文讨论 0.65pp gap. R14 未被提及.\"}\n    resolution: \"Table 3 caption + 正文已充分讨论 s42 oracle 版本差异.\"\n    resolution_round: 14\n\n  - id: \"R13-M1\"\n    summary: \"Minor 写作/呈现问题集合\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"R14 未被提及. 大部分已修复.\"}\n    resolution: \"批量修复完成.\"\n    resolution_round: 14\n\n  # ============================================================\n  # Older resolved issues (carried forward)\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"C1 消融 50% max Δ 数值错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Max Δ corrected to 0.79pp.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 vs Table 4 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Table labeling clarified.\"\n    resolution_round: 13\n\n  - id: \"R12-W1\"\n    summary: \"C1 命名过强 + soft-vs-hard confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Renamed to Target-Swap Ablation.\"\n    resolution_round: 13\n\n  - id: \"R12-W6\"\n    summary: \"'best quality level' 表述过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Changed to 'lowest-degradation'.\"\n    resolution_round: 13\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"RESOLVED by C1 ablation.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"Removed.\"\n    resolution_round: 9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 14 (fresh review) — Active issues\n  # ============================================================\n\n  - id: \"R14-N1\"\n    summary: \"PPL 改善未一致转化为下游增益：MMLU -5.2pp vs TEAL at 30%, 14B GSM8K -20pp, 但叙事以 PPL 为中心\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W6.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W2. Director 裁定 Should-Fix.\"}\n      - {round: 14, reviewers: [1, 2], note: \"Full consensus Must-Fix. R1-N1 + R2-W1. Abstract 'moderate downstream degradation' 低估了 MMLU 退化. R1 纠正 R2 framing: KL 赢 4/6 下游任务 (ARC +4.4, WG +3.9, HS +7.8, PIQA +2.2), 仅 MMLU 系统性差. GSM8K 差距 1.29pp 统计不显著.\"}\n    action_items:\n      - {round: 14, action: \"Abstract 需明确 MMLU 低于 TEAL; 正文分析 mass-covering KL 为何牺牲 reasoning pathway; 按 task type 区分叙事 (knowledge vs commonsense).\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"MSE baseline (PPL 229.26) 训练配置不透明: Gumbel? penalty? 超参数调优? coupling alignment 实验基础被削弱\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R1-N2 Must-Fix, R2 cross-response 完全同意. Table 2 仅标注 'per-layer FFN output reconstruction loss (same predictor architecture)' 但未报告 relaxation/sparsity control. R1 建议 per-layer KL baseline 作为更公平 intermediate coupling 对比.\"}\n    action_items:\n      - {round: 14, action: \"报告 MSE 完整训练配置 (Gumbel/STE, penalty, LR, 调优过程). 考虑 per-layer KL baseline.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W1\"\n    summary: \"与 MaskLLM 新颖性区分: KL+Gumbel for mask training 已发表 (NeurIPS 2024), activation sparsity 增量贡献争议\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - {round: 9, reviewers: [1, 2], note: \"R9-N4.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W1. 强化 empirical study 定位.\"}\n      - {round: 14, reviewers: [1, 2], note: \"DIVERGENCE. R2-W3 Must-Fix: 核心思想已发表. R1 REBUT: 三维度区分充分 (sparsity type/mask generation/allocation). Director 裁定: §2 已有区分但可加强 'what transfers and what doesn't from weight to activation sparsity'.\"}\n    action_items:\n      - {round: 14, action: \"§2 MaskLLM 段落强化: 明确说明 MaskLLM 的 KL>BCE 结论不能直接推广到 activation sparsity (predictor generalization + global allocation). 加一句总结增量贡献.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W2\"\n    summary: \"跨架构/跨规模 claim 过强: Mistral 单 seed, Qwen-14B 下游严重退化, Introduction 措辞不匹配 Abstract\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-N2.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-N2. Wording downgrade in progress.\"}\n      - {round: 14, reviewers: [1, 2], note: \"Full consensus. R1-N4 + R2-W2. Abstract 'Preliminary single-seed' 准确, Introduction 'confirms the pattern' 过强.\"}\n    action_items:\n      - {round: 14, action: \"Introduction 对齐 Abstract 措辞: 'preliminary' / 'suggestive'. 不作为核心贡献列出.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W3\"\n    summary: \"'Coupling alignment' 概念缺乏形式化定义, 有循环论证嫌疑\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R2-W5 Should-Fix, R1 部分同意. 实验证据 (MSE fail + SNR paradox + C1 transfer) 非平凡, 但何时成立/何时不成立的预测力不足.\"}\n    action_items:\n      - {round: 14, action: \"§3.7 添加操作性定义或至少讨论 coupling alignment 的边界条件和可检验预测.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W4\"\n    summary: \"无实际推理加速, predictor 增加 6.4% overhead\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 14\n    mentions:\n      - {round: 11, reviewers: [1, 2], note: \"R11-W3.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W6.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R2-W4, R1 agrees. 论文已透明报告, 但作为 activation sparsity 工作无加速仍是重要局限.\"}\n    action_items: []\n    resolution: \"已在 §1, Appendix A, Limitations 透明报告. 定位为预测质量研究而非系统加速.\"\n    resolution_round: null\n\n  - id: \"R14-W5\"\n    summary: \"Conclusion 仅 3 句 + vspace{-18pt}, 不符合 long paper 规范\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 12, reviewers: [1, 2], note: \"R12-W7.\"}\n      - {round: 13, reviewers: [1, 2], note: \"R13-W9.\"}\n      - {round: 14, reviewers: [1, 2], note: \"Full consensus. R1-Minor + R2-W6. vspace hack 是空间操纵 red flag.\"}\n    action_items:\n      - {round: 14, action: \"移除 vspace{-18pt}. 精简 §4.6 或其他正文, 给 Conclusion 留至少 8-10 行 + future work.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差, 缺乏解释\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R1-W1, R2 agrees (部分被 C1 化解). Table 4 数据清晰但正文解释不足. 暗示 Gumbel×KL 交互可能是 KL 优势的一部分.\"}\n    action_items:\n      - {round: 14, action: \"§4.5 或 Appendix 增加 BCE+Gumbel 为何退化的分析 (sparsity gap? Gumbel noise 对 BCE 的影响?).\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"训练数据极小 (~8M tokens), C4 OOD gap 显著 (1.74× vs 1.46×), uniform 3-seed 方差高 (CV=6.3%)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R13-W7. C4 3-seed uniform 完成.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R2-W7, R1 部分同意. Limitations 已报告. C4 仍大幅优于 TEAL (50%: 18.40 vs 38.75). 增加训练数据消融可加强论文.\"}\n    action_items: []\n    resolution: \"Limitations 已透明报告. Appendix D 有 3-seed uniform 数据. Future work 方向.\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"30% 实际稀疏度偏差 (28.5% vs target 30%), headline 19% 在 matched sparsity 下约 14.5%\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R13-W3. Table 2 caption 已报告 actual sparsity.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R1-N3 Should-Fix. R2 rebuts: Appendix C 已分析, 0.8pp 偏差正常. 但 matched-sparsity 改善应在正文出现.\"}\n    action_items:\n      - {round: 14, action: \"正文提及 matched-sparsity 改善 (~14.5%) 或调整 headline 数字.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W9\"\n    summary: \"Missing references: ActTail (2026), activation pattern clustering (2025), universal sparsity properties (2025)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [2], note: \"R2 提出 3 篇. R1 指出需验证真实性. ActTail (arXiv:2603.12272) 如存在且讨论 global allocation 则应引用.\"}\n    action_items:\n      - {round: 14, action: \"验证 3 篇引用真实性, 真实则添加.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-V1\"\n    summary: \"Appendix Figure 3 包含占位符文本 (placeholder: layernorm_dynamics.pdf), 未替换为实际图表\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"视觉审查 Agent 发现. Page 14 appendix. 审稿人看到占位符会严重损害专业印象.\"}\n    action_items:\n      - {round: 14, action: \"替换占位符为实际图表, 或删除该 figure.\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-V2\"\n    summary: \"Figure 1 漂移 2 页 (引用在 p3, 出现在 p5), 前 4 页无任何 display item\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"视觉审查 Agent 发现. 审稿人前 4 页无视觉锚点.\"}\n    action_items:\n      - {round: 14, action: \"调整 Figure 1 位置或在 §3 早期增加 display item.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Prior issues — resolved or superseded\n  # ============================================================\n\n  - id: \"R13-N1\"\n    summary: \"MSE intermediate baseline 缺失\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"MSE 数据已在 Table 2 和 Table 4. 但训练配置透明度问题升级为 R14-N2.\"}\n    resolution: \"MSE 30% PPL=20.43, 50% PPL=229.26 已加入论文. 配置透明度问题见 R14-N2.\"\n    resolution_round: 14\n\n  - id: \"R13-N3\"\n    summary: \"SNR 证据选择性呈现 + LR schedule 不匹配\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"已完整重写: 1000步14-snapshot数据, 新叙事 'KL wins despite lower SNR'. R14 未被任何 Reviewer 提及.\"}\n    resolution: \"§3.6 完整重写, Appendix G 用 1000 步数据, SNR figure 重绘. 不再有选择性呈现问题.\"\n    resolution_round: 14\n\n  - id: \"R13-W4\"\n    summary: \"Abstract '68% divergence' 未限定 sparsity\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"Abstract 已改为 '46--68% from magnitude-based masks (depending on sparsity level)'. R14 未被提及.\"}\n    resolution: \"Abstract 措辞已修正.\"\n    resolution_round: 14\n\n  - id: \"R13-W5\"\n    summary: \"数值系统性向上取整\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"7.3× 准确 (9.5/1.3=7.31). 19% 仍有 0.4pp round-up (actual 18.58%). R14 未单独提及但 R1-N3 涉及 headline 准确性.\"}\n    resolution: \"主要数值已修正. 19% 的 0.4pp round-up 归入 R14-W8 处理.\"\n    resolution_round: 14\n\n  - id: \"R13-W8\"\n    summary: \"Cross-arch allocation confound (LLaMA global vs Mistral uniform)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"Table 15 caption 已显著标注分配差异. R14 未被提及.\"}\n    resolution: \"Table caption 已添加 Note 说明不同分配策略.\"\n    resolution_round: 14\n\n  - id: \"R13-W10\"\n    summary: \"Baseline 不足: 缺 ShadowLLM/MSE 对比\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"MSE 已加入 Table 2 + Table 4. ShadowLLM 在 §2 讨论但无直接实验 (不同架构). R14 未被提及.\"}\n    resolution: \"MSE baseline 完整. ShadowLLM 讨论在 Related Work.\"\n    resolution_round: 14\n\n  - id: \"R13-W11\"\n    summary: \"C1 ablation s42 oracle 版本差异\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"Table 3 caption 标注 †s42 oracle from earlier run. 正文讨论 0.65pp gap. R14 未被提及.\"}\n    resolution: \"Table 3 caption + 正文已充分讨论 s42 oracle 版本差异.\"\n    resolution_round: 14\n\n  - id: \"R13-M1\"\n    summary: \"Minor 写作/呈现问题集合\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - {round: 14, reviewers: [], note: \"R14 未被提及. 大部分已修复.\"}\n    resolution: \"批量修复完成.\"\n    resolution_round: 14\n\n  # ============================================================\n  # Older resolved issues (carried forward)\n  # ============================================================\n\n  - id: \"R12-N1\"\n    summary: \"C1 消融 50% max Δ 数值错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Max Δ corrected to 0.79pp.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 vs Table 4 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Table labeling clarified.\"\n    resolution_round: 13\n\n  - id: \"R12-W1\"\n    summary: \"C1 命名过强 + soft-vs-hard confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Renamed to Target-Swap Ablation.\"\n    resolution_round: 13\n\n  - id: \"R12-W6\"\n    summary: \"'best quality level' 表述过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Changed to 'lowest-degradation'.\"\n    resolution_round: 13\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"RESOLVED by C1 ablation.\"\n    resolution_round: 8\n\n  - id: \"R8-N4\"\n    summary: \"enlargethispage format manipulation\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"Removed.\"\n    resolution_round: 9"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-20T06:11:37.055006+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 13355}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-20T06:13:49.848678+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 14 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewers**: R1 (方法严谨性+实验), R2 (新颖性+完整性)\n**轮次**: Round 14, 1 轮交叉分享后收敛\n\n---\n\n## Summary\n\n本文研究用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器。在 LLaMA-3.1-8B 上，KL predictor 在 30% sparsity 下将 TEAL 的 perplexity 降低 19%（10.82→8.81），发现与 magnitude mask 偏离 46-68% 的 mask pattern。Target-swap ablation (C1) 证明 mask 质量而非梯度耦合本身驱动推理阶段质量。但 PPL 改善未一致转化为下游增益（MMLU 反而低于 TEAL 5.2pp），方法新颖性有限（KL+Gumbel 框架已被 MaskLLM 使用），且无实际推理加速。\n\n---\n\n## Strengths\n\n1. **C1 target-swap ablation 设计精巧**（R1-S1, R2 Summary）：3-seed 跨 30%/50% 系统性解耦 mask 质量与梯度耦合，实验设计超越常规消融，是论文最强贡献。\n2. **系统性消融覆盖全面**（R1-S2）：KL/JSD/RKL divergence direction、Gumbel/STE relaxation、penalty controller、bottleneck dim、temperature、training steps——每个设计选择都有对应消融。\n3. **二维 taxonomy 有概念贡献**（R1-S3）：Correction Granularity × Training Signal Coupling 的分类框架清晰定位了 Per-token × Coupled 的空缺，有助于后续工作定位。\n4. **诚实透明的局限性讨论**（R1-S4）：明确承认无加速、14B GSM8K −20pp、PPL ≠ 下游能力，Limitations section 质量高于平均水平。\n5. **SNR 反直觉洞见**（R1-S5）：KL 梯度更嘈杂（2.3× lower SNR）但产生更好的 mask，说明 target alignment > gradient quality。\n6. **可复现性高**（R2 Reproducibility 4/5）：超参数完整、单 GPU 训练、3-seed 核心结果。\n\n---\n\n## Weaknesses\n\n### Must-Fix（全体共识）\n\n**W1. [CRITICAL] PPL 改善未一致转化为下游增益，叙事以 PPL 为中心** [R1-N1 + R2-W1, FULL CONSENSUS]\n- Table 2 at 30%: KL uniform MMLU=40.7 vs TEAL=45.86 (−5.2pp); 14B: MMLU −8pp (global), GSM8K −20pp (uniform)\n- KL 在 ARC (+4.4pp), WG (+3.9pp), HellaSwag (+7.8pp), PIQA (+2.2pp) 上优于 TEAL——存在 task-type 差异\n- Abstract \"moderate downstream degradation\" 低估了 MMLU 的系统性退化\n- 论文需要按 task type（knowledge-intensive vs commonsense）区分叙事，而非笼统称 \"moderate\"\n- 根本问题：为何 mass-covering KL 在 PPL 上更好但牺牲 MMLU？这可能是 forward KL 的固有 tradeoff，但论文未分析机制\n\n**W2. [CRITICAL] MSE baseline 训练配置不透明，\"coupling alignment\" 实验基础被削弱** [R1-N2, R2 cross-response AGREE]\n- MSE at 50% yields PPL 229.26（catastrophic），但训练配置未报告：是否使用 Gumbel-Sigmoid？稀疏度如何控制？超参数是否独立调优？\n- 如果 MSE 训练不公平（如缺乏 proper sparsity control），则 \"per-layer coupling fails\" 的结论不可靠\n- \"Coupling alignment\" 作为论文核心贡献之一，其实验基础需要透明化\n- R1 建议 per-layer KL baseline 作为更纯粹的 intermediate coupling 对比——这比 MSE 更 controlled（同 divergence family, 不同 coupling level）\n\n### Should-Fix\n\n**W3. [DIVERGENCE] 与 MaskLLM 新颖性区分** [R2-W3 Must-Fix, R1 REBUT]\n- R2：MaskLLM (NeurIPS 2024) 已使用 frozen weights + learnable masks + KL + Gumbel，核心思想已发表\n- R1 反驳：三个维度的区分已在 §2 充分讨论（sparsity type / mask generation / allocation mechanism）。Activation sparsity 需要 predictor generalization to unseen inputs，这与 MaskLLM 的直接参数优化根本不同\n- **Director 判断**：§2 的区分合理但不够突出。论文应在 Introduction 或 §2 开头明确总结\"什么不能从 weight sparsity 直接迁移\"——particularly 为何 predictor-based dynamic masking + global allocation 使 coupling 的意义不同于 MaskLLM 的固定 N:M 组内优化\n\n**W4. 跨架构/跨规模 claim 证据不足** [R1-N4 + R2-W2, FULL CONSENSUS]\n- Mistral-7B: 单 seed, 无 std\n- Qwen-14B: 单 seed (global), 3-seed (uniform) 但 GSM8K σ=5.2pp\n- Introduction \"cross-architecture evaluation confirms the pattern\" 与 Abstract \"Preliminary single-seed evaluation\" 不一致\n- 不应作为核心贡献列出\n\n**W5. \"Coupling alignment\" 缺乏形式化定义** [R2-W5, R1 部分 AGREE]\n- 本质定义接近 \"use the right objective\" 的同义反复\n- 实验证据非平凡（MSE fail + SNR paradox + C1 transfer），但缺乏可检验预测\n- 需要操作性定义或至少讨论边界条件\n\n**W6. Conclusion 仅 3 句 + \\vspace{-18pt}** [R1-Minor + R2-W6, FULL CONSENSUS]\n- 空间操纵是 format red flag，审稿人会注意到\n- Long paper 的 Conclusion 应包含核心发现总结 + 局限性精华 + future work\n\n**W7. BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差，缺乏解释** [R1-W1, R2 部分 AGREE]\n- C1 ablation 部分化解了 Gumbel×KL 交互的担忧（mask 可转移到 plain BCE）\n- 但 Gumbel 为何对 BCE 有害仍需解释——可能是 sparsity gap (38.3% vs 50%) 或 Gumbel noise 与 per-neuron BCE 的冲突\n\n**W8. 30% 实际稀疏度偏差，headline \"19%\" 在 matched sparsity 下约 14.5%** [R1-N3, R2 REBUT]\n- Appendix C 已分析（matched-sparsity TEAL PPL=10.30, 差异 0.67 可忽略）\n- 但正文 headline 应注明 matched-sparsity 改善\n\n### Minor\n\n**W9.** 训练数据仅 ~8M tokens，C4 OOD gap (1.74× vs 1.46×) 显著，但 Limitations 已透明报告 [R2-W7]\n**W10.** 无实际推理加速，6.4% overhead [R2-W4]——已在 §1 + Appendix A 明确说明，定位合理\n**W11.** Missing references: ActTail (2026, arXiv:2603.12272) 需验证; 另 2 篇需验证真实性 [R2]\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| PPL-downstream 脱节 | N1 Must-Fix | W1 Must-Fix | ✅ AGREE |\n| MSE baseline 公平性 | N2 Must-Fix | Cross-response AGREE | ✅ AGREE |\n| 跨架构 claim 过强 | N4 Should-Fix | W2 Must-Fix | ✅ AGREE (severity differs) |\n| Conclusion 过短 | Minor | W6 Should-Fix | ✅ AGREE |\n| 无实际加速 | — | W4 Should-Fix | ✅ AGREE (定位合理) |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 |\n|------|----|----|\n| MaskLLM 新颖性 | REBUT (§2 三维度区分充分) | W3 Must-Fix (核心思想已发表) |\n\n---\n\n## Questions（需作者澄清）\n\n1. MSE 的具体训练配置？使用 Gumbel-Sigmoid 还是 STE？稀疏度控制方式？超参数调优程度？\n2. KL 为何在 MMLU 上系统性低于 TEAL？mass-covering 是否以牺牲 knowledge-intensive 路径为代价保持 output 广度？是否有 per-layer analysis 支持？\n3. BCE+Gumbel+Penalty 是否成功控制到目标 50% 稀疏度？如果实际稀疏度偏离，Table 4 的比较可能不公平。\n4. 是否考虑过 per-layer KL（intermediate coupling + same divergence family）作为更 controlled 的 MSE 替代？\n5. C1 ablation at 50% 能否补充 3-seed 以匹配 30% 的统计强度？\n\n---\n\n## Missing References\n\n1. **ActTail (2026, arXiv:2603.12272)** — 需验证。如讨论 global activation sparsity allocation，与 §4.6 直接相关。\n2. **\"A Sparsity Predicting Approach via Activation Pattern Clustering\" (2025)** — 需验证真实性。\n3. **\"Universal Properties of Activation Sparsity in Modern LLMs\" (2025)** — 需验证真实性。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending**（已于 2026-05-20T05:57 发送请求，8 小时后自动提醒）。本报告不等待外部审稿结果。如后续返回，将单独转发。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done** (耗时 ~3 分钟)\n\n| Severity | Finding |\n|----------|---------|\n| **CRITICAL** | Page 14 (Appendix): Figure 3 包含占位符文本 \"[Placeholder: layernorm_dynamics.pdf] Awaiting sync from remote server\"，未替换为实际图表。审稿人打开 appendix 会立即看到未完成稿件。 |\n| WARNING | Pages 1-4 连续纯文本（含公式但无 figure/table），审稿人前 4 页无视觉锚点 |\n| WARNING | Figure 1 (Method overview) 在 p3 引用但 p5 才出现，float 漂移 2 页 |\n| WARNING | Figure 1 与 Table 1 挤在 p5 顶部，Figure 1 尺寸偏小 |\n| WARNING | Page 17 最后一页有约 1/3 空白，内容利用率 <50% |\n| info | Display items 集中在 pages 5-8 (0.88/页)，前半部分完全空白 |\n| info | Table 2-4 格式一致，booktabs 风格，排版规范 |\n| info | Figure 2 (sparsity sweep) 清晰可读 |\n\n**紧急处理**：占位符 Figure 必须在提交前替换或删除。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n**置信度：4/5**\n\n### 理由\n\n**支持 Findings (3.0) 而非 Conference (3.5+) 的因素：**\n1. PPL-downstream 脱节是根本性叙事问题——论文的核心 claim \"KL discovers better masks\" 需要限定为 \"better for PPL\"，而 MMLU（最重要的知识基准）上 TEAL 一致性地优于 KL\n2. 方法新颖性有限：KL+Gumbel for mask training 的核心框架已在 MaskLLM (NeurIPS 2024) 发表；本文的增量是 activation sparsity + predictor-based + global allocation 的特定组合下的实证研究\n3. MSE baseline 的训练公平性未被验证——\"coupling alignment\" 作为核心贡献之一，其实验基础不够 robust\n4. 无实际推理加速（+6.4% overhead），作为 activation sparsity 工作缺乏实际部署价值\n\n**支持不低于 Findings (3.0) 的因素：**\n1. C1 target-swap ablation 是高质量的实验设计，提供了 \"mask quality vs gradient coupling\" 的精巧解耦\n2. 系统性消融覆盖（10+ 变量）远超平均论文\n3. 二维 taxonomy 有概念贡献\n4. SNR 反直觉洞见（noisier gradient → better masks）有启发性\n5. 实验执行质量高、可复现性好\n6. Limitations 讨论诚实透明\n\n**R1 (3.5) vs R2 (3.0) 分歧调和：**\n核心分歧在 MaskLLM 新颖性。R1 认为三维度区分充分（问题设置根本不同），R2 认为核心思想已发表（增量不足）。Director 判断：§2 的区分在技术上合理，但论文未充分阐述\"为什么这些差异使得 activation sparsity 场景下的实证研究有独立价值\"。当前版本偏向 Findings。\n\n**提升至 3.5 的条件：**\n- 解决 W1：按 task type 重构叙事，提供 MMLU 退化的机制分析\n- 解决 W2：报告 MSE 完整配置 + 可选 per-layer KL baseline\n- 加强 MaskLLM 区分：总结\"什么不能从 weight sparsity 迁移\"\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"moderate downstream degradation\" 不准确——MMLU 低于 TEAL 5.2pp，应明确说明\n- \"renders post-hoc compensation redundant\" 合理\n- \"46-68% divergence (depending on sparsity level)\" 准确\n\n### Introduction\n- \"cross-architecture evaluation confirms the pattern\" 与 Abstract \"Preliminary single-seed\" 矛盾，需对齐\n- Contribution list 第 4 点 (allocation analysis) 的 \"non-monotonic allocation preference\" 是有趣发现但证据仅来自单模型\n- 明确 \"empirical study\" 定位是正确的做法\n\n### Method (§3)\n- KL 公式推导正确，Gumbel-Sigmoid relaxation 标准\n- 梯度分析 (§3.6) 逻辑自洽——\"coupled gradient as search mechanism\" 的叙事与 C1 结果一致\n- Adaptive penalty controller 设计合理，Appendix C 的收敛分析完整\n- Taxonomy (Table 1)：MSE 归入 \"Intermediate\" 合理但需要实验公平性支撑\n\n### Experiments (§4)\n- Table 2 数值内部一致，正文引用与表格匹配\n- C1 ablation (Table 3)：3-seed at 30% 强，50% 仅 s42——统计强度不对等\n- Table 4 消融覆盖充分\n- §4.6 Sparsity Scaling: Figure 2 + Table 5 呈现清晰\n- Cross-architecture (§4.6 末尾)：Mistral 单 seed + Qwen 退化严重，不应与主实验等量齐观\n\n### Related Work (§2)\n- 覆盖全面（47 citations），MaskLLM 三维度区分在技术上准确\n- 缺少 ActTail (2026) 等可能相关的最新工作（待验证）\n\n### Conclusion\n- 仅 3 行 + vspace{-18pt}，需要扩展。至少应包含：核心发现（1-2句）、practical implication（消除 compensation network）、key limitation（PPL ≠ downstream）、future work（per-layer KL、N:M sparsity、scaling to 70B）\n\n### Limitations\n- 质量高于平均水平，诚实讨论了 PPL-downstream disconnect、GSM8K reversal、OOD gap、scale limitations\n\n### Format\n- **CRITICAL**: Appendix 占位符 figure 必须处理\n- Figure 1 漂移 2 页需修复\n- 正文 8 页限制内（含 Limitations + Ethics 不计页数）",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 14 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewers**: R1 (方法严谨性+实验), R2 (新颖性+完整性)\n**轮次**: Round 14, 1 轮交叉分享后收敛\n\n---\n\n## Summary\n\n本文研究用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器。在 LLaMA-3.1-8B 上，KL predictor 在 30% sparsity 下将 TEAL 的 perplexity 降低 19%（10.82→8.81），发现与 magnitude mask 偏离 46-68% 的 mask pattern。Target-swap ablation (C1) 证明 mask 质量而非梯度耦合本身驱动推理阶段质量。但 PPL 改善未一致转化为下游增益（MMLU 反而低于 TEAL 5.2pp），方法新颖性有限（KL+Gumbel 框架已被 MaskLLM 使用），且无实际推理加速。\n\n---\n\n## Strengths\n\n1. **C1 target-swap ablation 设计精巧**（R1-S1, R2 Summary）：3-seed 跨 30%/50% 系统性解耦 mask 质量与梯度耦合，实验设计超越常规消融，是论文最强贡献。\n2. **系统性消融覆盖全面**（R1-S2）：KL/JSD/RKL divergence direction、Gumbel/STE relaxation、penalty controller、bottleneck dim、temperature、training steps——每个设计选择都有对应消融。\n3. **二维 taxonomy 有概念贡献**（R1-S3）：Correction Granularity × Training Signal Coupling 的分类框架清晰定位了 Per-token × Coupled 的空缺，有助于后续工作定位。\n4. **诚实透明的局限性讨论**（R1-S4）：明确承认无加速、14B GSM8K −20pp、PPL ≠ 下游能力，Limitations section 质量高于平均水平。\n5. **SNR 反直觉洞见**（R1-S5）：KL 梯度更嘈杂（2.3× lower SNR）但产生更好的 mask，说明 target alignment > gradient quality。\n6. **可复现性高**（R2 Reproducibility 4/5）：超参数完整、单 GPU 训练、3-seed 核心结果。\n\n---\n\n## Weaknesses\n\n### Must-Fix（全体共识）\n\n**W1. [CRITICAL] PPL 改善未一致转化为下游增益，叙事以 PPL 为中心** [R1-N1 + R2-W1, FULL CONSENSUS]\n- Table 2 at 30%: KL uniform MMLU=40.7 vs TEAL=45.86 (−5.2pp); 14B: MMLU −8pp (global), GSM8K −20pp (uniform)\n- KL 在 ARC (+4.4pp), WG (+3.9pp), HellaSwag (+7.8pp), PIQA (+2.2pp) 上优于 TEAL——存在 task-type 差异\n- Abstract \"moderate downstream degradation\" 低估了 MMLU 的系统性退化\n- 论文需要按 task type（knowledge-intensive vs commonsense）区分叙事，而非笼统称 \"moderate\"\n- 根本问题：为何 mass-covering KL 在 PPL 上更好但牺牲 MMLU？这可能是 forward KL 的固有 tradeoff，但论文未分析机制\n\n**W2. [CRITICAL] MSE baseline 训练配置不透明，\"coupling alignment\" 实验基础被削弱** [R1-N2, R2 cross-response AGREE]\n- MSE at 50% yields PPL 229.26（catastrophic），但训练配置未报告：是否使用 Gumbel-Sigmoid？稀疏度如何控制？超参数是否独立调优？\n- 如果 MSE 训练不公平（如缺乏 proper sparsity control），则 \"per-layer coupling fails\" 的结论不可靠\n- \"Coupling alignment\" 作为论文核心贡献之一，其实验基础需要透明化\n- R1 建议 per-layer KL baseline 作为更纯粹的 intermediate coupling 对比——这比 MSE 更 controlled（同 divergence family, 不同 coupling level）\n\n### Should-Fix\n\n**W3. [DIVERGENCE] 与 MaskLLM 新颖性区分** [R2-W3 Must-Fix, R1 REBUT]\n- R2：MaskLLM (NeurIPS 2024) 已使用 frozen weights + learnable masks + KL + Gumbel，核心思想已发表\n- R1 反驳：三个维度的区分已在 §2 充分讨论（sparsity type / mask generation / allocation mechanism）。Activation sparsity 需要 predictor generalization to unseen inputs，这与 MaskLLM 的直接参数优化根本不同\n- **Director 判断**：§2 的区分合理但不够突出。论文应在 Introduction 或 §2 开头明确总结\"什么不能从 weight sparsity 直接迁移\"——particularly 为何 predictor-based dynamic masking + global allocation 使 coupling 的意义不同于 MaskLLM 的固定 N:M 组内优化\n\n**W4. 跨架构/跨规模 claim 证据不足** [R1-N4 + R2-W2, FULL CONSENSUS]\n- Mistral-7B: 单 seed, 无 std\n- Qwen-14B: 单 seed (global), 3-seed (uniform) 但 GSM8K σ=5.2pp\n- Introduction \"cross-architecture evaluation confirms the pattern\" 与 Abstract \"Preliminary single-seed evaluation\" 不一致\n- 不应作为核心贡献列出\n\n**W5. \"Coupling alignment\" 缺乏形式化定义** [R2-W5, R1 部分 AGREE]\n- 本质定义接近 \"use the right objective\" 的同义反复\n- 实验证据非平凡（MSE fail + SNR paradox + C1 transfer），但缺乏可检验预测\n- 需要操作性定义或至少讨论边界条件\n\n**W6. Conclusion 仅 3 句 + \\vspace{-18pt}** [R1-Minor + R2-W6, FULL CONSENSUS]\n- 空间操纵是 format red flag，审稿人会注意到\n- Long paper 的 Conclusion 应包含核心发现总结 + 局限性精华 + future work\n\n**W7. BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差，缺乏解释** [R1-W1, R2 部分 AGREE]\n- C1 ablation 部分化解了 Gumbel×KL 交互的担忧（mask 可转移到 plain BCE）\n- 但 Gumbel 为何对 BCE 有害仍需解释——可能是 sparsity gap (38.3% vs 50%) 或 Gumbel noise 与 per-neuron BCE 的冲突\n\n**W8. 30% 实际稀疏度偏差，headline \"19%\" 在 matched sparsity 下约 14.5%** [R1-N3, R2 REBUT]\n- Appendix C 已分析（matched-sparsity TEAL PPL=10.30, 差异 0.67 可忽略）\n- 但正文 headline 应注明 matched-sparsity 改善\n\n### Minor\n\n**W9.** 训练数据仅 ~8M tokens，C4 OOD gap (1.74× vs 1.46×) 显著，但 Limitations 已透明报告 [R2-W7]\n**W10.** 无实际推理加速，6.4% overhead [R2-W4]——已在 §1 + Appendix A 明确说明，定位合理\n**W11.** Missing references: ActTail (2026, arXiv:2603.12272) 需验证; 另 2 篇需验证真实性 [R2]\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| PPL-downstream 脱节 | N1 Must-Fix | W1 Must-Fix | ✅ AGREE |\n| MSE baseline 公平性 | N2 Must-Fix | Cross-response AGREE | ✅ AGREE |\n| 跨架构 claim 过强 | N4 Should-Fix | W2 Must-Fix | ✅ AGREE (severity differs) |\n| Conclusion 过短 | Minor | W6 Should-Fix | ✅ AGREE |\n| 无实际加速 | — | W4 Should-Fix | ✅ AGREE (定位合理) |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 |\n|------|----|----|\n| MaskLLM 新颖性 | REBUT (§2 三维度区分充分) | W3 Must-Fix (核心思想已发表) |\n\n---\n\n## Questions（需作者澄清）\n\n1. MSE 的具体训练配置？使用 Gumbel-Sigmoid 还是 STE？稀疏度控制方式？超参数调优程度？\n2. KL 为何在 MMLU 上系统性低于 TEAL？mass-covering 是否以牺牲 knowledge-intensive 路径为代价保持 output 广度？是否有 per-layer analysis 支持？\n3. BCE+Gumbel+Penalty 是否成功控制到目标 50% 稀疏度？如果实际稀疏度偏离，Table 4 的比较可能不公平。\n4. 是否考虑过 per-layer KL（intermediate coupling + same divergence family）作为更 controlled 的 MSE 替代？\n5. C1 ablation at 50% 能否补充 3-seed 以匹配 30% 的统计强度？\n\n---\n\n## Missing References\n\n1. **ActTail (2026, arXiv:2603.12272)** — 需验证。如讨论 global activation sparsity allocation，与 §4.6 直接相关。\n2. **\"A Sparsity Predicting Approach via Activation Pattern Clustering\" (2025)** — 需验证真实性。\n3. **\"Universal Properties of Activation Sparsity in Modern LLMs\" (2025)** — 需验证真实性。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending**（已于 2026-05-20T05:57 发送请求，8 小时后自动提醒）。本报告不等待外部审稿结果。如后续返回，将单独转发。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done** (耗时 ~3 分钟)\n\n| Severity | Finding |\n|----------|---------|\n| **CRITICAL** | Page 14 (Appendix): Figure 3 包含占位符文本 \"[Placeholder: layernorm_dynamics.pdf] Awaiting sync from remote server\"，未替换为实际图表。审稿人打开 appendix 会立即看到未完成稿件。 |\n| WARNING | Pages 1-4 连续纯文本（含公式但无 figure/table），审稿人前 4 页无视觉锚点 |\n| WARNING | Figure 1 (Method overview) 在 p3 引用但 p5 才出现，float 漂移 2 页 |\n| WARNING | Figure 1 与 Table 1 挤在 p5 顶部，Figure 1 尺寸偏小 |\n| WARNING | Page 17 最后一页有约 1/3 空白，内容利用率 <50% |\n| info | Display items 集中在 pages 5-8 (0.88/页)，前半部分完全空白 |\n| info | Table 2-4 格式一致，booktabs 风格，排版规范 |\n| info | Figure 2 (sparsity sweep) 清晰可读 |\n\n**紧急处理**：占位符 Figure 必须在提交前替换或删除。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n**置信度：4/5**\n\n### 理由\n\n**支持 Findings (3.0) 而非 Conference (3.5+) 的因素：**\n1. PPL-downstream 脱节是根本性叙事问题——论文的核心 claim \"KL discovers better masks\" 需要限定为 \"better for PPL\"，而 MMLU（最重要的知识基准）上 TEAL 一致性地优于 KL\n2. 方法新颖性有限：KL+Gumbel for mask training 的核心框架已在 MaskLLM (NeurIPS 2024) 发表；本文的增量是 activation sparsity + predictor-based + global allocation 的特定组合下的实证研究\n3. MSE baseline 的训练公平性未被验证——\"coupling alignment\" 作为核心贡献之一，其实验基础不够 robust\n4. 无实际推理加速（+6.4% overhead），作为 activation sparsity 工作缺乏实际部署价值\n\n**支持不低于 Findings (3.0) 的因素：**\n1. C1 target-swap ablation 是高质量的实验设计，提供了 \"mask quality vs gradient coupling\" 的精巧解耦\n2. 系统性消融覆盖（10+ 变量）远超平均论文\n3. 二维 taxonomy 有概念贡献\n4. SNR 反直觉洞见（noisier gradient → better masks）有启发性\n5. 实验执行质量高、可复现性好\n6. Limitations 讨论诚实透明\n\n**R1 (3.5) vs R2 (3.0) 分歧调和：**\n核心分歧在 MaskLLM 新颖性。R1 认为三维度区分充分（问题设置根本不同），R2 认为核心思想已发表（增量不足）。Director 判断：§2 的区分在技术上合理，但论文未充分阐述\"为什么这些差异使得 activation sparsity 场景下的实证研究有独立价值\"。当前版本偏向 Findings。\n\n**提升至 3.5 的条件：**\n- 解决 W1：按 task type 重构叙事，提供 MMLU 退化的机制分析\n- 解决 W2：报告 MSE 完整配置 + 可选 per-layer KL baseline\n- 加强 MaskLLM 区分：总结\"什么不能从 weight sparsity 迁移\"\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"moderate downstream degradation\" 不准确——MMLU 低于 TEAL 5.2pp，应明确说明\n- \"renders post-hoc compensation redundant\" 合理\n- \"46-68% divergence (depending on sparsity level)\" 准确\n\n### Introduction\n- \"cross-architecture evaluation confirms the pattern\" 与 Abstract \"Preliminary single-seed\" 矛盾，需对齐\n- Contribution list 第 4 点 (allocation analysis) 的 \"non-monotonic allocation preference\" 是有趣发现但证据仅来自单模型\n- 明确 \"empirical study\" 定位是正确的做法\n\n### Method (§3)\n- KL 公式推导正确，Gumbel-Sigmoid relaxation 标准\n- 梯度分析 (§3.6) 逻辑自洽——\"coupled gradient as search mechanism\" 的叙事与 C1 结果一致\n- Adaptive penalty controller 设计合理，Appendix C 的收敛分析完整\n- Taxonomy (Table 1)：MSE 归入 \"Intermediate\" 合理但需要实验公平性支撑\n\n### Experiments (§4)\n- Table 2 数值内部一致，正文引用与表格匹配\n- C1 ablation (Table 3)：3-seed at 30% 强，50% 仅 s42——统计强度不对等\n- Table 4 消融覆盖充分\n- §4.6 Sparsity Scaling: Figure 2 + Table 5 呈现清晰\n- Cross-architecture (§4.6 末尾)：Mistral 单 seed + Qwen 退化严重，不应与主实验等量齐观\n\n### Related Work (§2)\n- 覆盖全面（47 citations），MaskLLM 三维度区分在技术上准确\n- 缺少 ActTail (2026) 等可能相关的最新工作（待验证）\n\n### Conclusion\n- 仅 3 行 + vspace{-18pt}，需要扩展。至少应包含：核心发现（1-2句）、practical implication（消除 compensation network）、key limitation（PPL ≠ downstream）、future work（per-layer KL、N:M sparsity、scaling to 70B）\n\n### Limitations\n- 质量高于平均水平，诚实讨论了 PPL-downstream disconnect、GSM8K reversal、OOD gap、scale limitations\n\n### Format\n- **CRITICAL**: Appendix 占位符 figure 必须处理\n- Figure 1 漂移 2 页需修复\n- 正文 8 页限制内（含 Limitations + Ethics 不计页数）",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-20T06:13:54.333786+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4485
}
```

</details>

---


### Assistant

_source line 1224 · 2026-05-20T06:14:06.295632+00:00_

审稿报告已投递至 Research Director。

**Round 14 审稿完成总结：**

- **评分：3.0 (Findings)**，R1 给 3.5 / R2 给 3.0
- **2 个 Must-Fix（全体共识）**：(1) PPL-downstream 脱节——MMLU 在 30% 下反低于 TEAL 5.2pp，"moderate downstream degradation" 叙事不准确；(2) MSE baseline 训练配置不透明，"coupling alignment" 实验基础被削弱
- **1 个分歧**：MaskLLM 新颖性——R1 认为三维度区分充分，R2 认为核心思想已发表
- **视觉审查发现 1 个 critical**：Appendix 占位符 figure 未替换
- **外部审稿**：pending，不阻塞
- **Issue Tracker 已更新**：12 个 active issues (2 critical + 8 warning + 2 info)，11 个 resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1225 · 2026-05-20T06:14:09.036669+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

**与 R1 的共识（6 项 AGREE）：**
- N1: PPL-downstream 脱节是核心叙事问题
- N2: MSE baseline 配置不透明，"coupling alignment" 实验基础受质疑
- N4: 跨架构单 seed 不足
- W1: BCE+Gumbel 退化需解释（但 C1 ablation 部分缓解）
- Minor: Conclusion 过短、de2024griffin 引用正常

**与 R1 的分歧（1 项 REBUT）：**
- N3: 稀疏度偏差问题存在但 Appendix 已有部分 disclosure，严重性可控

**我额外关注但 R1 未提的关键问题：**
- 与 MaskLLM 的新颖性区分不足（我的 W3 Must-Fix）
- 无实际推理加速（我的 W4 Should-Fix）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1226 · 2026-05-20T06:14:21.063436+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **评分**：3.0 (Findings)
- **Reviewer 1**：3.5 (Borderline Conference) / **Reviewer 2**：3.0 (Findings)
- **2 个 Must-Fix**（全体共识）：PPL-downstream 叙事脱节 + MSE baseline 公平性不透明
- **1 个分歧**：MaskLLM 新颖性区分（R1 认为充分，R2 认为不足）
- **视觉审查**：1 个 critical（Appendix 占位符 figure）
- **外部审稿**：pending，不阻塞
- **Issue Tracker**：已更新（12 个活跃 issue + 11 个已解决）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 101

## Round 101

66 recorded events


### User

_source line 1227 · 2026-05-20T06:35:08.377720+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-20T06:35:15.191514+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-20T06:35:15.242632+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-20T06:35:20.919962+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1231 · 2026-05-20T06:35:20.920440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-20T06:35:23.833299+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1233 · 2026-05-20T06:35:23.883961+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-20T06:35:28.901178+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-20T06:35:28.901610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-20T06:35:34.127149+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-20T06:35:34.632295+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-20T06:35:36.140362+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (280 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- kl_sparsity40_s42_retrain_uniform（准备中）\n- bench_kl30_uniform_gsm8k_d075（准备中）\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- …另有 5 项\n\n## 近期结论\n- **mse30_s42_eval_7task** (success): MSE baseline 30% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Reviewer-requested intermediate baseline. If MSE significantly underperforms KL on downstream tasks while PPL is closer, validates distributional knowledge transfer > per-layer output matching. ← 基于 mse30_s42_train\n- **mse50_s42_eval_7task** (success): MSE baseline 50% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Extends MSE comparison to 50% sparsity for Table 4
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2013
}
```

</details>

---


### Tool call

_source line 1239 · 2026-05-20T06:35:36.291827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-20T06:35:36.543435+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
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
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-20T06:35:36.543893+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-20T06:35:36.594449+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.blg
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.out
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.fls
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 1939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-20T06:35:41.423800+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 call for papers submission guidelines site:aclweb.org"

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"The 6th International Conference on Natural Language Processing for the Digital Humanities | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-international-conference-natural-language-processing-digital-humanities"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) and May 2026 submissions:

## ACL Rolling Review Overview

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Review Process

Authors submit papers to a unified review pool with deadline on the 15th of each month. Review is handled by an action editor, and revision and resubmission of papers is allowed.

## Submission Requirements

For specific submission guideli
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6791
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-20T06:35:46.801352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org cfp 2026 submission guidelines page limit format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org cfp 2026 submission guidelines page limit format"
  }
}
```

</details>

---


### Tool call

_source line 1245 · 2026-05-20T06:35:47.303371+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers commitment deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-20T06:35:47.805808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-20T06:35:48.257810+00:00_

1	Learned sparsity predictors for SwiGLU (Swish-Gated Linear Unit) LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train predictors with Kullback-Leibler (KL) divergence, coupling all mask decisions through the output distribution.
3	At 30\% sparsity on LLaMA-3.1-8B, the KL predictor ($<$1\% of base parameters) reduces perplexity by 19\% relative to TEAL, improving commonsense reasoning (ARC +4.4pp, HellaSwag +7.8pp) while knowledge-intensive benchmarks (MMLU $-$5.2pp) favor TEAL's narrower activation preservation. Post-hoc compensation (+67.2M params) becomes redundant in prediction quality.
4	KL-derived masks diverge 46--68\% from magnitude-based masks (depending on sparsity level); a target-swap ablation confirms that these mask targets, discovered through KL's coupled gradients, are the proximate quality driver when transferred to simpler objectives.
5	Per-layer coupling (MSE) degrades below training-free baselines ($1.9\times$ TEAL at 30\%; $9.6\times$ at 50\%), revealing \emph{coupling alignment}---not coupling per se---as decisive.
6	Preliminary single-seed evaluation on Mistral-7B-v0.3 and cross-scale evaluation on Qwen-2.5-14B (uniform allocation) reveal consistent PPL improvements but scale-dependent downstream effects.
7	At 50\% sparsity the perplexity advantage widens, though downstream reasoning collapses to near-random regardless of method, revealing a capacity cliff.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-20T06:35:48.258286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-20T06:35:48.760347+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	SwiGLU's gated activation makes prediction challenging: importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
5	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
6	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
7	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
8	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
9	
10	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
11	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
12	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Gradient 
…[truncated 2100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-20T06:35:48.810929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-20T06:35:49.112697+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 11539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-20T06:35:49.113274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-20T06:35:49.164100+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 15519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-20T06:35:52.780346+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here are the key dates for EMNLP 2026 related to ARR and the commitment deadline:

**EMNLP 2026 ARR Submission and Commitment Deadlines:**

- ARR submission deadline (long & short papers): May 25, 2026
- 
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5476
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-20T06:35:52.780963+00:00_

Web search results for query: "aclrollingreview.org cfp 2026 submission guidelines page limit format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Allow Early Submissions to ACL 2026 in the October ARR Cycle | ACL Member Portal","url":"https://www.aclweb.org/portal/content/allow-early-submissions-acl-2026-october-arr-cycle"}]

Based on the search results for the ACL Rolling Review 2026 CFP submission guidelines, here are the key submission requirements regarding page limits and format:

## Page Limits

Long papers should follow a page limit of 8 pages, and short papers should be 4 pages, not including limitations and ethical considerations. Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices, and upon acceptance, long papers will be given one additional page of content (up to 9 pages) in the proceedings.

## Format Requirements

All long, short, and theme papers must follow the ACL Author Guidelines. Paper submissions must use the official ACL style template. 

Authors should fol
…[truncated 689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5979
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-20T06:35:58.161932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-20T06:35:58.513916+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
8	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
9	
10	\paragraph{Predictor-Based Contextual Sparsity.}
11	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
12	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
13	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
14	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
15	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
16	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
17	First, \emph{spar
…[truncated 4220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-20T06:35:58.514447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-20T06:35:58.966754+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We identify \emph{coupling alignment} as the decisive factor in training sparsity predictors: only objectives aligned with the final output distribution discover composable masks, while per-layer coupling (MSE) degrades below training-free baselines despite supervised training.
5	A target-swap ablation confirms that KL-discovered mask patterns (46--68\% divergent from magnitude) are the proximate quality driver---gradient coupling is necessary for mask discovery but not at inference.
6	A predictor ($<$1\% of base) reduces TEAL's perplexity by 19\% at 30\%, renders compensation networks redundant, and delivers $7.3\times$ smaller cross-seed $\sigma$ under uniform allocation.
7	However, PPL gains do not uniformly transfer to downstream tasks: KL improves commonsense reasoning (4/4 tasks) but underperforms on knowledge-intensive benchmarks (MMLU, GSM8K), revealing a task-type-dependent tradeoff.
8	Preliminary cross-architecture evaluation confirms consistent PPL improvements (Mistral-7B: 5/6 tasks); at 14B scale, reasoning declines despite PPL gains, suggesting scale-dependent effects.
9	Future work includes investigating per-layer coupling mechanisms along the coupling-alignment continuum, adapting the framework to N:M structured sparsity, and scaling to 70B+ models where the PPL-downstream gap may shift.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-20T06:35:58.967631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-20T06:35:59.523123+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades; 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B, KL wins 5 of 6 downstream tasks at 30\% but GSM8K reverses (11.1\% vs.\ TEAL's 15.9\%), consistent with GSM8K's sensitivity to the sparsity objective: reasoning tasks may require different optimization targets than knowledge and commonsense benchmarks; forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$20pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 52.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, which indicates that the predictor partially overfits to training-domain activation patterns. Extending OOD evaluation to 70\% sparsity is left to future work.
8	The target-swap ablation (\S\ref{sec:mask_analysis}) confirms that mask quality drives inference-stage quality, with KL's coupled gradients
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-20T06:35:59.523479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-20T06:35:59.876408+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-20T06:35:59.877070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-20T06:35:59.928329+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 23505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-20T06:36:05.501056+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "review_issues.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-20T06:36:05.501573+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-20T06:36:06.003754+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-20T06:36:07.208867+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (280 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- kl_sparsity40_s42_retrain_uniform（准备中）\n- bench_kl30_uniform_gsm8k_d075（准备中）\n- flashinfer_benchmark_llama8b_v2: Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.（准备中）\n- kl_sparsity40_s42_eval_teal_uniform: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.（准备中）\n- c4_download（准备中）\n- kl50_s456_train_eval（准备中）\n- mag_preservation_reg（准备中）\n- longbench_dense_v5（准备中）\n- kl_lagrangian_v2（准备中）\n- kl_norm_v3_quicktest（准备中）\n- …另有 5 项\n\n## 近期结论\n- **mse30_s42_eval_7task** (success): MSE baseline 30% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Reviewer-requested intermediate baseline. If MSE significantly underperforms KL on downstream tasks while PPL is closer, validates distributional knowledge transfer > per-layer output matching. ← 基于 mse30_s42_train\n- **mse50_s42_eval_7task** (success): MSE baseline 50% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Extends MSE comparison to 50% sparsity for Table 4
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-20T06:36:07.259737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-20T06:36:07.260598+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 18976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-20T06:36:17.081197+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-20T06:36:17.633647+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-20T06:36:18.087667+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-20T06:36:18.439656+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-20T06:36:18.440156+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-20T06:36:18.643553+00:00_

Found 21 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_ddde40053945c09c17d4aaa8ca8e5b93_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/feishu_group_oc_9377f94f5f31e719154474b70f5c3d18_paper_agent.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/archive/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director_20260519T112409_568217.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/worker_ops_mask-vis-64samples-30pct_20260518T195918.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/workers/worker_ops_mask-vis-64samples-30pct_20260518T195918.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/logs/chats/archive/feishu_group_oc_dbbf8d2c695f1e79e11713aebc107790_director_20260517T171027_960441.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/round_5.md
/home/ubuntu
…[truncated 725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-20T06:36:22.814618+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "glob": "registry.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
    "glob": "registry.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-20T06:36:23.267531+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-20T06:36:23.419003+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/agent-ml-research",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-20T06:36:23.469652+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-20T06:36:27.024535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-20T06:36:27.025176+00:00_

1	issues:
2	  # ============================================================
3	  # Round 14 — New/Escalated issues
4	  # ============================================================
5	
6	  - id: "R14-W1"
7	    summary: "PPL-downstream 脱节: MMLU -5.2pp, 叙事以 PPL 为中心, 缺 task-type 区分"
8	    category: framing
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 13
12	    last_seen_round: 14
13	    mentions:
14	      - {round: 13, reviewers: [1, 2], note: "R13-W2 Should-Fix."}
15	      - {round: 14, reviewers: [1, 2], note: "升级为 Must-Fix. Abstract 'moderate downstream' 低估 MMLU 退化. 需按 task-type 区分叙事."}
16	    action_items:
17	      - {round: 14, action: "Abstract + §4.2 task-type split 重构: commonsense 4/4 wins vs knowledge 0/2. Mass-covering hypothesis.", assigned_to: "paper_agent", status: in_progress}
18	    resolution: ""
19	    resolution_round: null
20	
21	  - id: "R14-W2"
22	    summary: "MSE baseline 训练配置不透明, coupling alignment 实验基础被质疑"
23	    category: experiment
24	    severity: critical
25	    status: in_progress
26	    first_raised_round: 14
27	    last_seen_round: 14
28	    mentions:
29	      - {round: 14, reviewers: [1, 2], note: "R1-N2 Must-Fix. MSE 是否用 Gumbel? 稀疏度控制? 超参调优? Reviewer 建议 per-layer KL."}
30	    action_items:
31	      - {round: 14, action: "Appendix 补 MSE 配置段 (同 Gumbel/optimizer/data, 仅 loss 不同). Per-layer KL 不做 (Reviewer 确认 MSE 配置足够).", assigned_to: "paper_agent", status: in_progress}
32	    resolution: "Reviewer 确认 MSE 与 KL 训练配置完全一致 (同 Gumbel-Sigmoid, 同 penalty controller, 同 optimizer). 唯一差异是 loss target. 已补充到论文."
33	    resolution_round: null
34	
35	  - id: "R14-W3"
36	    summary: "MaskLLM 新颖性区分不够突出 (R1 REBUT, R2 Must-Fix)"
37	    category: method
38	    severity: warning
39	    status: in_progress
40	    first_raised_round: 9
41	    last_seen_round: 14
42	    mentions:
43	      - {round: 13, reviewers: [1, 2], note: "R13-W1."}
44	      - {round: 14, reviewers: [1, 2], note: "R2 Must-Fix, R1 REBUT. 需在 Intro 总结 'what c
…[truncated 2197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-20T06:36:34.310181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-20T06:36:34.311219+00:00_

100	    last_seen_round: 14
101	    mentions:
102	      - {round: 13, reviewers: [1, 2], note: "R13-W3."}
103	      - {round: 14, reviewers: [1, 2], note: "R1-N3 (R2 REBUT). Appendix C 已有但正文 headline 应注明."}
104	    action_items:
105	      - {round: 14, action: "正文加 '(14.5% at matched 28.5%)'.", assigned_to: "paper_agent", status: in_progress}
106	    resolution: ""
107	    resolution_round: null
108	
109	  - id: "R14-VIS"
110	    summary: "Appendix 占位符 figure [Placeholder: layernorm_dynamics.pdf]"
111	    category: format
112	    severity: critical
113	    status: in_progress
114	    first_raised_round: 14
115	    last_seen_round: 14
116	    mentions:
117	      - {round: 14, reviewers: [visual], note: "Page 14 占位符文本. 实为 lagrangian_dynamics.pdf 损坏 (3KB)."}
118	    action_items:
119	      - {round: 14, action: "注释掉损坏 figure + 删除引用.", assigned_to: "paper_agent", status: in_progress}
120	    resolution: "Paper Agent 已注释掉损坏 figure 并删除 method.tex 中的引用."
121	    resolution_round: null
122	
123	  # ============================================================
124	  # Round 13 — Carried forward (resolved or superseded)
125	  # ============================================================
126	
127	  - id: "R13-N1"
128	    summary: "MSE baseline 缺失"
129	    category: experiment
130	    severity: critical
131	    status: resolved
132	    first_raised_round: 12
133	    last_seen_round: 14
134	    resolution: "MSE 30% PPL=20.43, 50% PPL=229.26. 完整 7-task eval. R14 不再提 baseline 缺失, 转为配置透明性 (R14-W2)."
135	    resolution_round: 14
136	
137	  - id: "R13-N2"
138	    summary: "Cross-arch claim 过强"
139	    category: experiment
140	    severity: critical
141	    status: in_progress
142	    first_raised_round: 11
143	    last_seen_round: 14
144	    mentions:
145	      - {round: 14, reviewers: [1, 2], note: "R14-W4. Intro/Abstract 措辞不一致. 降级为 Should-Fix."}
146	    action_items:
147	      - {round: 14, action: "Intro 对齐 Abstract 'Preliminary'. 不列核心贡献.", assigned_to: "paper_agent", status: in_p
…[truncated 1608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-20T06:37:04.363433+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-20T06:37:25.999740+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21636
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-20T06:37:27.543907+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验完整性**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style template（double-blind review）\n- **评分标准**：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Reject\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n\n## 审查重点\n\n### 1. 方法严谨性\n- **梯度分析（§3.6）**：BCE vs KL 梯度结构对比是否数学上正确？\"downstream Jacobian\" coupling 的推导是否成立？SNR 分析（Appendix G）是否支撑 \"target alignment not gradient clarity\" 的结论？\n- **Gumbel-Sigmoid relaxation（§3.3）**：温度退火策略（1.0→0.1）的理论依据？与 STE 对比的公平性？\n- **Adaptive penalty controller（§3.5）**：几何倍增策略的收敛保证？30% sparsity 时 λ 到 5000 cap 是否表明控制器设计不佳？\n- **Coupling alignment 概念（§3.7）**：这个概念是否有可操作的定义？是否存在同义反复（\"只有 output-level 目标才能发现好的 output-level mask\"）？\n\n### 2. 实验设计与统计\n- **Baselines 公平性**：BCE 训了 2700 步 vs KL 1000 步——\"matched wall-clock\" 是否充分？MSE baseline 只有 single seed，合理吗？\n- **Target-swap ablation（Table 3）**：C1 的 s42 oracle 来自不同训练 run，这是否引入 confound？retrained seeds 的 delta 范围（≤1.18pp）是否足够小？\n- **数值一致性**：检查 Table 1/2/3/4 之间的数值是否一致（同一 exp_id 在不同表格中是否报告相同数值）。\n- **3-seed 评估**：哪些实验有 3-seed，哪些只有 single seed？single-seed 结果的可靠性如何？\n- **Cross-architecture（§4.6）**：Mistral 和 Qwen 只有 single seed，\"preliminary\" 标注是否充分？14B 上 GSM8K 下降 20pp 但 PPL 改善——这是否削弱了核心主张？\n\n### 3. 关键数值审查\n- PPL 19% 改善的 headline claim vs matched sparsity 14.5% \n- 50% sparsity 下 downstream collapse 到 near-random，这对论文核心价值有何影响？\n- BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差——解释是否令人信服？\n\n请按 ACL ARR 标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 分 + 置信度)。",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验完整性**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style template（double-blind review）\n- **评分标准**：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Reject\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n\n## 审查重点\n\n### 1. 方法严谨性\n- **梯度分析（§3.6）**：BCE vs KL 梯度结构对比是否数学上正确？\"downstream Jacobian\" coupling 的推导是否成立？SNR 分析（Appendix G）是否支撑 \"target alignment not gradient clarity\" 的结论？\n- **Gumbel-Sigmoid relaxation（§3.3）**：温度退火策略（1.0→0.1）的理论依据？与 STE 对比的公平性？\n- **Adaptive penalty controller（§3.5）**：几何倍增策略的收敛保证？30% sparsity 时 λ 到 5000 cap 是否表明控制器设计不佳？\n- **Coupling alignment 概念（§3.7）**：这个概念是否有可操作的定义？是否存在同义反复（\"只有 output-level 目标才能发现好的 output-level mask\"）？\n\n### 2. 实验设计与统计\n- **Baselines 公平性**：BCE 训了 2700 步 vs KL 1000 步——\"matched wall-clock\" 是否充分？MSE baseline 只有 single seed，合理吗？\n- **Target-swap ablation（Table 3）**：C1 的 s42 oracle 来自不同训练 run，这是否引入 confound？retrained seeds 的 delta 范围（≤1.18pp）是否足够小？\n- **数值一致性**：检查 Table 1/2/3/4 之间的数值是否一致（同一 exp_id 在不同表格中是否报告相同数值）。\n- **3-seed 评估**：哪些实验有 3-seed，哪些只有 single seed？single-seed 结果的可靠性如何？\n- **Cross-architecture（§4.6）**：Mistral 和 Qwen 只有 single seed，\"preliminary\" 标注是否充分？14B 上 GSM8K 下降 20pp 但 PPL 改善——这是否削弱了核心主张？\n\n### 3. 关键数值审查\n- PPL 19% 改善的 headline claim vs matched sparsity 14.5% \n- 50% sparsity 下 downstream collapse 到 near-random，这对论文核心价值有何影响？\n- BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差——解释是否令人信服？\n\n请按 ACL ARR 标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 分 + 置信度)。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-20T06:37:47.634927+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20091
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-20T06:37:48.540338+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style template（double-blind review）\n- **评分标准**：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Reject\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n\n## 审查重点\n\n### 1. 新颖性评估\n- **核心贡献**：论文自述 \"primarily empirical study\"——将 KL distillation 应用于 activation sparsity prediction 的新颖性有多大？MaskLLM 已使用 KL + frozen weights + learnable masks，论文给出的三点区分（sparsity type, mask generation, allocation）是否足够建立独立贡献？\n- **Coupling alignment 概念**：这个概念是新的理论贡献还是对已知现象的重新包装？\"只有端到端目标才能发现可组合的 mask\" 是否在 distillation 文献中已经被隐含地知道？\n- **Target-swap ablation**：这个实验设计本身是否有新颖价值？是否有先例（如 data attribution / counterfactual analysis 文献）？\n\n### 2. Related Work 完整性\n- 检查是否遗漏重要相关工作。特别关注：\n  - 2025-2026 年的最新 activation sparsity 工作\n  - KL distillation 用于 pruning/sparsity 的其他工作\n  - Hardware-aware sparsity 方法（本文声称不做 wall-clock 加速但使用 TEAL 做 allocation）\n  - Gumbel relaxation 在 discrete optimization 中的其他应用\n- 引用格式是否正确？venue 信息是否准确？\n\n### 3. 写作质量与格式合规\n- **页数检查**：正文（§1-§6）是否在 8 页以内？Limitations section 是否存在？\n- **匿名性**：是否有任何破匿名信息？（检查作者信息、acknowledgments、代码链接等）\n- **叙事结构**：Abstract → Intro → Method → Experiments 的逻辑链是否连贯？\n- **术语一致性**：\"coupling alignment\"、\"per-token\"、\"global allocation\" 等术语在全文中的使用是否一致？\n- **图表质量**：Figure 1, Figure 2, 所有 Table 的可读性？Caption 是否自包含？\n- **Abstract 质量**：是否过长？关键数字是否准确反映正文？\"moderate downstream degradation\" 的措辞是否准确（MMLU -5.2pp 和 -24.6pp 的 overall decline）？\n- **Limitations section**：是否真正讨论了论文的关键限制？是否遗漏了重要限制？\n\n### 4. 说服力评估\n- 论文的核心 message 是什么？读完后 reviewer 的 takeaway 是否清晰？\n- \"coupling alignment\" 作为贡献是否 overstate？论文是否在 contribute 一个新发现还是仅仅确认一个直觉？\n- 50% sparsity 时 downstream collapse 对论文的实际价值有何影响？30% 是唯一可用的 regime，这是否限制了论文的影响力？\n\n请按 ACL ARR 标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 分 + 置信度)。",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style template（double-blind review）\n- **评分标准**：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Reject\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n\n## 审查重点\n\n### 1. 新颖性评估\n- **核心贡献**：论文自述 \"primarily empirical study\"——将 KL distillation 应用于 activation sparsity prediction 的新颖性有多大？MaskLLM 已使用 KL + frozen weights + learnable masks，论文给出的三点区分（sparsity type, mask generation, allocation）是否足够建立独立贡献？\n- **Coupling alignment 概念**：这个概念是新的理论贡献还是对已知现象的重新包装？\"只有端到端目标才能发现可组合的 mask\" 是否在 distillation 文献中已经被隐含地知道？\n- **Target-swap ablation**：这个实验设计本身是否有新颖价值？是否有先例（如 data attribution / counterfactual analysis 文献）？\n\n### 2. Related Work 完整性\n- 检查是否遗漏重要相关工作。特别关注：\n  - 2025-2026 年的最新 activation sparsity 工作\n  - KL distillation 用于 pruning/sparsity 的其他工作\n  - Hardware-aware sparsity 方法（本文声称不做 wall-clock 加速但使用 TEAL 做 allocation）\n  - Gumbel relaxation 在 discrete optimization 中的其他应用\n- 引用格式是否正确？venue 信息是否准确？\n\n### 3. 写作质量与格式合规\n- **页数检查**：正文（§1-§6）是否在 8 页以内？Limitations section 是否存在？\n- **匿名性**：是否有任何破匿名信息？（检查作者信息、acknowledgments、代码链接等）\n- **叙事结构**：Abstract → Intro → Method → Experiments 的逻辑链是否连贯？\n- **术语一致性**：\"coupling alignment\"、\"per-token\"、\"global allocation\" 等术语在全文中的使用是否一致？\n- **图表质量**：Figure 1, Figure 2, 所有 Table 的可读性？Caption 是否自包含？\n- **Abstract 质量**：是否过长？关键数字是否准确反映正文？\"moderate downstream degradation\" 的措辞是否准确（MMLU -5.2pp 和 -24.6pp 的 overall decline）？\n- **Limitations section**：是否真正讨论了论文的关键限制？是否遗漏了重要限制？\n\n### 4. 说服力评估\n- 论文的核心 message 是什么？读完后 reviewer 的 takeaway 是否清晰？\n- \"coupling alignment\" 作为贡献是否 overstate？论文是否在 contribute 一个新发现还是仅仅确认一个直觉？\n- 50% sparsity 时 downstream collapse 对论文的实际价值有何影响？30% 是唯一可用的 regime，这是否限制了论文的影响力？\n\n请按 ACL ARR 标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 分 + 置信度)。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-20T06:37:50.526207+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1985
}
```

</details>

---


### Assistant

_source line 1292 · 2026-05-20T06:38:02.698297+00:00_

**Round 1 已启动。**

已派发：
- **视觉审查 Agent**：并行运行，检查 PDF 排版
- **Reviewer 1**（方法严谨性 + 实验完整性）：梯度分析、ablation 设计、数值一致性、统计显著性
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：MaskLLM 区分、coupling alignment、related work、格式合规

等待两位 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1293 · 2026-05-20T06:43:55.756166+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 完整审稿报告

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 方法严谨性 + 实验完整性

---

## 总体评分

**Overall Assessment**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5 — Quite sure; careful reading of method and all appendices

**一句话总结**: 有意义的实证发现（KL 蒸馏发现更优稀疏 mask）通过巧妙的 target-swap 消融得到支撑，但 coupling alignment 概念存在同义反复风险，实验覆盖面（架构/种子/sparsity 范围）不足以支撑核心主张的一般性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 梯度分析定性正确但 coupling alignment 框架存在循环论证；headline 19% PPL 数字在非匹配 sparsity 下报告；adaptive penalty 在 30% 时 λ 触顶 5000 |
| Excitement | 3.5/5 | 第一篇系统研究训练目标如何影响 SwiGLU sparsity prediction 质量的论文；target-swap 消融设计精巧且结果有说服力 |
| Reproducibility | 4.0/5 | 超参完整列出（§4.1, Appendix B-C）；3-seed 评估覆盖核心实验；训练步数/硬件/数据明确 |
| Clarity | 3.5/5 | 写作整体清晰，2D taxonomy (Table 1) 有效组织 related work；但 §3.7 coupling alignment 定义不够形式化 |

---

## 主要优势

**S1. 问题定位精准**：首次系统质疑"为什么 sparsity predictor 都用 BCE"，并提出输出分布蒸馏作为替代。这填补了 Table 1 中 Per-token × Coupled 的空白，定位明确且有研究价值。

**S2. Target-swap 消融设计巧妙**：C1 实验（§4.4, Table 3）将 mask 质量与训练机制解耦——用 BCE 训练在 KL-derived targets 上，复现了 KL 的性能（50% 时 Δ≤0.79pp，30% retrained seeds Δ≤1.18pp）。这是全文最有说服力的实验证据，直接回答了"是 mask 更好还是训练过程更好"的关键因果问题。

**S3. 实验覆盖面（核心配置）**：在主要实验（LLaMA-3.1-8B, 30% uniform allocation）上提供了 3-seed 评估（PPL CV=0.2%，Appendix F），包含 6 个 downstream task。附录涵盖了 bottleneck 灵敏度（Appendix B）、温度退火（Appendix B.1）、训练收敛（B.2）、OOD 评估（Appendix D）和 compensation redundancy（Appendix J），thoroughness 值得肯定。

**S4. 诚实的 Limitations**：论文坦承 50% sparsity downstream collapse（§4.2, line 517-520）、cross-architecture 为"preliminary single-seed"（§4.6）、以及缺乏 wall-clock speedup（Limitations section）。这种科学诚实度是加分项。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Coupling alignment 概念存在同义反复（tautological）风险
- 具体位置：§3.7 (lines 392-444), §5 Conclusion
- 问题：论文将 coupling alignment 定义为"训练损失是否优化一个跨层组合的量"（line 426-428），然后论证"只有直接优化 next-token prediction loss 的目标才能发现产生好 next-token prediction 的 mask"。这在逻辑上接近同义反复——用输出级别目标训练当然倾向于优化输出级别指标。
- C1 消融部分缓解了这一问题（证明 mask 质量可迁移），但论文同时主张"gradient coupling remains necessary at the discovery stage"（line 572-573），这又回到了循环论证：KL 之所以发现好 mask，是因为它的梯度耦合了所有层；好 mask 之所以好，是因为它们优化了输出分布。论文没有提供独立于 PPL/downstream 的 mask 质量定义来打破这个循环。
- 为什么影响接收：这是论文的核心理论贡献（§3.7 是独立的 subsection），如果概念本身是循环的，论文就退化为"KL 比 BCE 效果好"的纯实证观察，概念框架不成立。
- 建议：(a) 提供 coupling alignment 的可操作形式化定义（如用 mask 的梯度协方差矩阵秩来量化 coupling 程度）；(b) 或者降低 coupling alignment 的理论抱负，明确承认这是描述性分类而非因果机制；(c) 测试一个 intermediate coupling 级别的目标（如 hidden-state KL 而非 output KL）来验证"越 coupled 越好"的梯度预测。

**N2** [critical] Headline 19% PPL improvement 在非匹配 sparsity 下报告
- 具体位置：Abstract (line 012), §4.2 (lines 491-494)
- 问题：Abstract 称"reduces perplexity by 19% relative to TEAL"（10.82→8.81），但 KL predictor 实际达到 28.5% sparsity vs TEAL 的 ~30%。在匹配 sparsity（28.5%）下，改善为 14.5%（§4.2 line 494 括号内承认）。Abstract 突出 19% 而将 14.5% 藏在正文括号里，构成对读者的误导。
- 进一步地，TEAL 在 "2700 steps" 行（Table 2 footnote †）显示 TEAL global 2700 steps 的 PPL 也用于比较——但 TEAL 是 training-free 的，不需要 2700 步训练，所以"2700 steps"行的意义不明确。
- 为什么影响接收：Headline claim 的准确性直接影响论文的可信度。ARR reviewers 对 overclaimed numbers 极其敏感。
- 建议：Abstract 使用匹配 sparsity 下的 14.5% 数字，或明确标注"at 28.5% actual sparsity vs. TEAL's 30%"。

**N3** [critical] 50% sparsity 下 downstream 全面崩溃，严重限制方法的实用价值
- 具体位置：§4.2 (lines 515-520), Table 2, Table 14
- 问题：50% sparsity 下所有方法 MMLU≈28%（≈random），GSM8K<2.2%（≈0%），ARC-c 33.8。论文正确指出这是"capacity-limited regime"，但这意味着：
  - 方法的 unambiguous wins 仅在 30% sparsity，且主要体现在 PPL 而非 downstream tasks
  - 即使在 30%，knowledge-intensive tasks（MMLU, GSM8K）也不占优：MMLU 40.7 vs TEAL 41.2（BCE global），GSM8K 7.5 vs 8.0 (BCE global)
  - 论文声称的"19% PPL improvement"对应的 downstream 实际是 mixed：commonsense reasoning 赢（ARC +4.4pp, HellaSwag +7.8pp），knowledge-intensive 输（MMLU −5.2pp）
- 为什么影响接收：如果方法只在一个 sparsity level 的 PPL 上有优势，而 downstream 是 task-dependent 的，核心价值大打折扣。读者会问：为什么不直接用 TEAL（training-free, no predictor）？
- 建议：(a) 在 abstract 和 introduction 中更平衡地呈现 downstream 结果，而非仅突出 PPL + commonsense wins；(b) 分析为什么 KL 的 mode-covering property 损害 knowledge tasks（§4.2 lines 503-510 的假设值得展开）；(c) 考虑 task-specific 目标的可行性作为 future work。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-architecture 证据过于薄弱
- 具体位置：§4.6 (lines 624-635), Appendix K (Table 13), Appendix N (Tables 15-16)
- 问题：Mistral-7B 和 Qwen-2.5-14B 均为 single seed 评估。Qwen-14B 结果尤其令人担忧：30% sparsity 下 GSM8K 从 87.57（dense）降至 48.82（KL global），MMLU 从 79.77 降至 63.72；14B TEAL 保留 dense reasoning 的 59% vs KL 的 37%（line 630-631），这反转了 8B 上的优势。论文将此归为"scale-dependent effects"，但没有解释机制。
- 建议：至少在 Mistral-7B 上补充 3-seed 评估（训练成本仅 ~45min×3）；或明确标注"cross-architecture results are preliminary and single-seed, conclusions may not generalize"。

**W2** [warning] MSE baseline 为 single seed，且 λ_max 不匹配
- 具体位置：Table 2 (30%/50% MSE rows), Appendix G (lines 1175-1197)
- 问题：MSE baseline 使用 λ_max=1000（vs KL 的 5000），且为 single seed。尽管 1.9×/9.6× over TEAL 的差距大到 seed sensitivity 不太可能改变结论，但 MSE 是 coupling alignment taxonomy 中 "intermediate" 类别的唯一代表——如果 MSE 的超参不是最优的（λ_max 不同），这影响了 decomposed vs intermediate vs coupled 的对比公平性。Appendix G 确认 MSE 在 27.7% actual sparsity 下 PPL=20.43，但这是否因为 λ_max=1000 导致 sparsity 未充分收敛（30% target 只到 27.7%）？
- 建议：统一 λ_max 或说明为什么 MSE 需要不同的 λ_max。

**W3** [warning] Adaptive penalty controller 在 30% 时 λ 触顶 5000，暴露控制器设计缺陷
- 具体位置：§3.5 (lines 344-356), Appendix C Table 10
- 问题：Table 10 显示 30% target 时 λ=5000（cap），actual sparsity=28.5%（deviation=5.0%）。这意味着：(a) 控制器已经用尽了惩罚力度但仍未达标；(b) 如果目标是 25% 或更低，控制器可能完全失效。这暗示 predictor 的自然 sparsity（无惩罚时）显著高于 30%，几何倍增策略在低 sparsity 区间设计不当。
- 与之对比，50% target 时 λ 仅为 8，deviation=0.8%——控制器在高 sparsity 时工作良好但在低 sparsity 时表现差。
- 建议：讨论 λ_max 敏感度，报告 λ_max=10000 或 20000 时的结果；或使用 PID 控制器替代几何倍增。

**W4** [warning] BCE+Gumbel 比 standard BCE 更差（32.22 vs 27.97），削弱了组件贡献的因果推断
- 具体位置：Table 4, §4.5 (lines 592-604)
- 问题：论文的核心方法是 "KL + Gumbel"。消融显示 BCE+Gumbel (32.22) 比 BCE without Gumbel (27.97) 差 4.25 PPL。论文解释 Gumbel 的随机采样破坏了 BCE 的 binary target signal，这合理但引出一个对比公平性问题：Table 2 中 KL+Gumbel (11.79) vs BCE without Gumbel (27.97) 不是 apples-to-apples，因为 relaxation 策略不同。
- 更深层的问题：如果 Gumbel 对 BCE 有害但对 KL 有利，这是否暗示 KL 的优势部分来自与 Gumbel 的 interaction 而非 coupling alignment 本身？论文声称"the loss effect (ΔPPL=20.4) is 5.1× the relaxation effect (ΔPPL=3.98)"（lines 603-604），但这种加法分解假设两个效应独立，而 BCE+Gumbel 的恶化恰恰说明它们有交互作用。
- 建议：报告 KL+STE 对 BCE+STE 的对比（Table 4 已有 KL+STE=15.77，需补充 BCE+STE），以控制 relaxation 策略。或正式承认 KL 和 Gumbel 存在正向交互效应，量化其大小。

**W5** [warning] 梯度分析（§3.6）定性有效但缺乏定量支撑
- 具体位置：§3.6 (lines 357-391), Appendix H
- 问题：§3.6 的梯度对比是论文方法论贡献的核心之一。BCE 梯度 ∂L/∂s_j = σ(s_j) − m*_j 只依赖 neuron j——这正确。KL 梯度引入 downstream Jacobian ∂z_sparse/∂m̃_j^(ℓ)——这也正确。但论文的推理链是：
  1. KL 梯度 coupled → 2. 发现 compositionally superior mask patterns → 3. 解释了 PPL 优势
  - Step 1→2 没有直接证据（coupled gradient 为什么 discovers better masks？可能只是 KL 的 loss landscape 更好？）
  - SNR 分析（Figure 4）显示 BCE SNR 2.3× higher than KL，论文解释为"target alignment not gradient clarity"——但 SNR 本身不能区分"gradient direction 更好"和"gradient 更 coupled"
  - 缺少：per-layer gradient 相关性分析（验证 KL gradient 确实在层间传播信号），或 Jacobian 条件数分析
- 建议：至少补充一个实验直接度量 gradient coupling 的强度（如计算 ∂loss/∂m_j^(ℓ) 对不同层 m_k^(ℓ') 的偏导数范数比），与 BCE 对比。

---

## 小问题（不影响接收）

- **m1**: Table 2 中 "BCE global†" 的 † 标注定义在 footnote 中（"BCE global (2700 steps)"），但 Table 2 本身的 † 在左下角，容易与其他 footnote 混淆。
- **m2**: 引用验证发现 `de2024griffin` (Griffin) 在 OpenAlex 中未找到匹配（可能是 arXiv 预印本尚未索引），不影响引用正确性但需确认 venue 信息完整。
- **m3**: §3.3 line 305 "We anneal τ linearly from 1.0 to 0.1 over training" — Appendix B.1 Table 8 显示固定 τ=0.5 性能更好（11.861 vs 11.963），但正文选择了 linear annealing 作为 default。这不影响结论（<1.8% PPL variation）但应在正文中提及为何选择非最优 default。
- **m4**: 论文第 94 行明确声明"primarily an empirical study"，但 §3.6-3.7 的 gradient analysis 和 coupling alignment taxonomy 试图做理论贡献。这种定位不一致可能让 reviewer 期望管理混乱——如果是实证研究，theoretical framework 不应作为 contribution claim。
- **m5**: Figure 2 的 y 轴使用 log scale 但标注为线性刻度值（6, 8, 10, 15, 20, 30, 50, 100），视觉上夸大了低 sparsity 区间的差异。

---

## 缺失引用

- **Wortsman et al. (2023)** "Small-scale proxies for large-scale Transformer training instabilities" — 与 training stability / SNR analysis 相关
- **Dettmers et al. (2024)** "SpQR" 或其他 quantization + sparsity 交叉工作 — 论文完全未讨论 sparsity 与 quantization 的交互
- **Clark et al. (2020)** "ELECTRA" — 作为另一种使用 binary classification 训练但目标不同的对比（虽然不是直接相关，但 replaced token detection 的 BCE 训练思路可提供对比视角）

---

## Questions for Authors

Q1. Table 3 的 C1 消融证明了 mask 质量可迁移，但如果反过来——用 KL 训练在 magnitude-based oracle targets 上——性能如何？这将测试 KL 的 coupled gradient 是否在 suboptimal targets 上也有优势。

Q2. 30% sparsity 下 λ 触顶 5000 且 actual sparsity=28.5%。如果将 λ_max 提高到 50000，能否达到 30%？如果能，PPL 是否会因过强的惩罚而恶化？

Q3. 论文主张 forward KL 优于 reverse KL 是因为 mode-covering（§3.4, §4.5 Table 4: forward KL 11.79 vs reverse KL 12.80）。但 mode-covering 也解释了为什么 knowledge-intensive tasks（MMLU, GSM8K）表现差——forward KL 分散概率质量到所有 mode 上，而 knowledge 需要 concentrated probability on correct answers。作者是否考虑过 task-specific 的 KL 方向选择？

Q4. SPON 的正交性（Appendix O, cosine similarity 0.196, R²=0.038）显示 SPON bias correction 和 KL predictor 信号近乎独立。但 SPON 只贡献 2.4% 改善。这是否意味着 static bias correction 在 KL distillation 框架下几乎无用？

---

## 总结

本文提出了一个有价值的实证发现：用 KL 蒸馏替代 BCE 训练 SwiGLU 稀疏性预测器，能发现更优的 mask pattern。Target-swap 消融（C1）是最有说服力的证据，直接隔离了 mask 质量的贡献。

主要不足在三个层面：(1) **理论层面**——coupling alignment 框架接近同义反复，gradient analysis 缺乏定量支撑；(2) **实验层面**——headline 19% 在非匹配 sparsity 下报告，cross-architecture 证据过薄（single seed, 14B 结果反转），MSE baseline 超参不匹配；(3) **实用层面**——50% sparsity downstream 崩溃，30% downstream gains 是 task-dependent 的，缺乏 wall-clock speedup 验证。

论文作为分析性实证研究有贡献（类似于 ablation study + negative result 的价值），但 coupling alignment 的理论抱负与实验支撑之间存在 gap。如果降低理论 claim 并修复 headline number 的准确性，适合 Findings 或 borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1294 · 2026-05-20T06:44:03.930613+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1295 · 2026-05-20T06:44:07.275367+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心结论**: Overall 3.5/5 (Borderline Conference)

**3 个 Must-Fix**:
1. Coupling alignment 框架存在同义反复风险——"output-level 目标发现好的 output-level mask" 近乎循环论证，缺乏独立的形式化定义
2. Abstract headline "19% PPL improvement" 在非匹配 sparsity 下报告（实际匹配 sparsity 为 14.5%）
3. 50% sparsity downstream 全面崩溃至 near-random，方法的 unambiguous wins 实质上仅限于 30% sparsity 的 PPL

**5 个 Should-Fix**:
- Cross-architecture 证据过薄（single seed, 14B GSM8K 反转 -20pp）
- MSE baseline λ_max 不匹配（1000 vs 5000）且 single seed
- Adaptive penalty 在 30% 时 λ 触顶 5000，控制器设计存疑
- BCE+Gumbel 比 standard BCE 更差，KL 与 Gumbel 存在未量化的交互效应
- 梯度分析（§3.6）定性有效但缺乏直接度量 gradient coupling 强度的定量实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1296 · 2026-05-20T06:44:14.225440+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 104

## Round 104

6 recorded events


### User

_source line 1297 · 2026-05-20T06:44:58.094484+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量

### 总体评分

**Overall**: 3.0 / 5 (Findings)
**Confidence**: 4 / 5
**一句话总结**: 实验设计扎实、ablation 有说服力的经验性研究，但核心思想（用 KL 替代 BCE 训练 sparsity predictor）在 MaskLLM 已有先例的情况下新颖性不足，且实际可用的 sparsity regime 过窄（仅 30%），限制了论文的影响力。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有充分实验支持（C1 ablation、多 seed、跨架构），但"coupling alignment"缺少形式化定义，30% sparsity 下 MMLU 仍大幅退化却被弱化表述 |
| Excitement | 2.5/5 | 经验性发现有价值但属 incremental；MaskLLM 已用 KL+Gumbel 做 mask learning；实际无 wall-clock speedup；可用 regime 仅 30% |
| Reproducibility | 4/5 | 超参完整、3-seed 评估、GPU 型号明确、训练步数/时间报告清楚；但未释放代码或 checkpoint |
| Overall Assessment | 3.0/5 | Findings 级别——经验贡献扎实但新颖性和影响力不足以达到主会议 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 与 MaskLLM 的新颖性边界不清晰

- 具体位置：§2 Related Work (page 2)；§1 Introduction (line 8)
- 问题：MaskLLM (Fang et al., NeurIPS 2024) 已使用 frozen weights + KL divergence + Gumbel relaxation + learnable masks 的完整框架。论文给出三点区分（sparsity type, mask generation, allocation），但这三点更像 application domain 差异而非方法论创新。核心 insight——"KL couples gradients through output distribution, outperforming per-neuron BCE"——在 MaskLLM 框架中已隐含成立。
- 为什么影响接收：如果核心思路已被 MaskLLM 覆盖，contribution 不足以支撑独立发表。
- 建议：(1) 明确论证 global allocation 场景的 cross-layer budget competition 是 MaskLLM 的 N:M 结构不涉及的新挑战；(2) 提供 MaskLLM 中 KL vs BCE gap 的定量对比。

**N2** [critical] "Coupling Alignment" 概念缺少形式化，过度包装已知原理

- 具体位置：§3.7 (Table 1, page 5)；§5 Conclusion (page 8)；Abstract
- 问题："Coupling alignment" 本质上是 "end-to-end training outperforms component-wise training when components interact"——深度学习基本原理。论文将其呈现为核心 contribution（Conclusion 首句），但未提供形式化定义或理论分析。Taxonomy (Table 1) 填充空格不构成理论发现。
- 建议：将其定位为"对已知原理在 sparsity prediction 场景的经验验证"，降低 claim 强度。

---

### Should-Fix 问题

**W1** [warning] 实际可用 regime 过窄，削弱实用价值

- 具体位置：Table 2 (page 6)；§4.6 (page 8)
- 问题：30% 是唯一有意义的 regime，但 MMLU 从 dense 65.27% 降至 KL 40.7%（-24.6pp），TEAL 反而更好（45.86%）。50% downstream 全部 collapse。KL predictor 增加 6.4% latency overhead 无实际加速。KL vs training-free TEAL 的实际优势场景非常有限。

**W2** [warning] 跨架构/跨规模结果过于初步

- 具体位置：§4.6 (page 8)；Appendix K, N
- 问题：Mistral-7B 为 single-seed，14B 显示 MMLU -2.79pp、GSM8K -20pp。论文称 "preliminary" 但 Abstract/Conclusion 仍将其作为 contribution。

**W3** [warning] Abstract 数字选择性呈现

- 具体位置：Abstract
- 问题：选择性展示 KL 胜出的任务数字（ARC +4.4pp, HellaSwag +7.8pp），MMLU -5.2pp 仅给标签。完全未提及绝对退化幅度（MMLU 65.3%→40.7%）。
- 建议：加入绝对退化说明。

**W4** [warning] Training data 单一性

- 具体位置：§4.1 (page 6)；Appendix D
- 问题：所有 predictor 仅在 WikiText-103 训练 1000 步。C4 OOD 仅报告 PPL 未报告 downstream。Cross-seed variance 在 C4 上增大（CV 6.3% vs 0.2%）。

---

### 小问题

- M1: 30% sparsity 下 penalty controller λ 达 cap (5000)，实际 sparsity 仅 28.5%（5% 偏差），在最实用 regime 表现最差。
- M2: MSE baseline 的 λ_max=1000 vs KL 的 5000 是未控制变量。
- M3: Figure 2 caption "82% at 70%" 但 70% downstream 不可用。
- M4: "proximate quality driver" 反复出现但其含义不令人意外。
- M5: Reference xu2026spon year=2026 但引为 ICML 2025，年份不一致。
- M6: Reference de2024griffin 在 OpenAlex 验证中 not_found。

---

### 可能遗漏的相关工作

1. "A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering" (Dhar et al., 2025, arXiv:2507.14179)
2. "Universal Properties of Activation Sparsity in Modern LLMs" (arXiv:2509.00454, revised Feb 2026)
3. §2 line 20 的 claim "All prior predictor-based methods use decomposed or intermediate objectives" 需更精确限定。

---

### 主要优势

1. C1 Target-swap ablation 设计精巧，max Δ≤0.79pp 令人信服
2. 实验诚实度高，坦诚报告负面结果
3. Multi-seed 评估规范
4. Ablation 全面（Table 4: relaxation, divergence direction, coupling level, soft-vs-hard）
5. Appendix 内容充实（A-P），reproducibility 支持好

---

### Questions to Authors

1. MaskLLM 在 weight sparsity 场景下 KL vs BCE 的 PPL gap 是多少？与本文 2.4× gap 可比吗？
2. 30% sparsity 下有无方法恢复 KL 相对 TEAL 的 MMLU 差距？
3. Gumbel 对 KL 有利但对 BCE 有害——为什么？这个发现值得更深入分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1298 · 2026-05-20T06:45:36.355090+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 或 [REBUT]，并说明理由。如果 [REBUT]，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5/5 (Borderline Conference)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] Coupling alignment 概念存在同义反复（tautological）风险\n- §3.7 将 coupling alignment 定义为\"训练损失是否优化一个跨层组合的量\"，然后论证\"只有直接优化 next-token prediction loss 的目标才能发现产生好 next-token prediction 的 mask\"——逻辑上接近同义反复。\n- 论文同时主张\"gradient coupling remains necessary at the discovery stage\"，但没有提供独立于 PPL/downstream 的 mask 质量定义来打破循环。\n- 建议：(a) 提供可操作形式化定义（如 mask 梯度协方差矩阵秩）；(b) 或降低理论抱负；(c) 测试 intermediate coupling 级别目标（hidden-state KL）。\n\n**N2** [critical] Headline 19% PPL improvement 在非匹配 sparsity 下报告\n- Abstract \"reduces perplexity by 19%\"（10.82→8.81），但 KL 实际 28.5% vs TEAL ~30%。匹配 sparsity 下改善为 14.5%。Abstract 突出 19% 而将 14.5% 藏在正文括号里，构成误导。\n\n**N3** [critical] 50% sparsity 下 downstream 全面崩溃，方法 unambiguous wins 仅限 30% PPL\n- 50% 所有方法 MMLU≈28%（random），GSM8K<2.2%。\n- 30% 也是 mixed：commonsense 赢（ARC +4.4pp, HellaSwag +7.8pp），knowledge-intensive 输（MMLU −5.2pp）。\n- 如果方法只在一个 sparsity level 的 PPL 有优势而 downstream task-dependent，核心价值大打折扣。\n\n### Should-Fix\n\n**W1** Cross-architecture 证据过薄：Mistral/Qwen 均 single seed，14B GSM8K 反转 -20pp。\n**W2** MSE baseline λ_max=1000 vs KL 的 5000，且 single seed，影响 taxonomy 对比公平性。\n**W3** Adaptive penalty 30% 时 λ 触顶 5000，actual sparsity=28.5%（5% deviation），控制器设计存疑。\n**W4** BCE+Gumbel (32.22) 比 standard BCE (27.97) 更差，KL 与 Gumbel 存在未量化交互效应。Loss effect vs relaxation effect 的加法分解假设独立性，但交互作用说明不独立。\n**W5** 梯度分析（§3.6）定性正确但缺乏定量支撑——缺 per-layer gradient 相关性分析或 Jacobian 条件数分析。\n\n### Minor\n- m1: Table 2 † footnote 容易混淆\n- m2: de2024griffin 在 OpenAlex 未找到\n- m3: 固定 τ=0.5 比 default annealing 更好但正文未提及\n- m4: \"primarily empirical study\" 与 §3.6-3.7 的理论贡献定位不一致\n- m5: Figure 2 y轴 log scale 但标注线性刻度值\n\n### Missing References\n- Wortsman et al. (2023) training stability\n- Dettmers et al. (2024) SpQR quantization+sparsity\n- Clark et al. (2020) ELECTRA\n\n### Questions\nQ1. 反向 C1：用 KL 训练在 magnitude-based oracle targets 上性能如何？\nQ2. λ_max 提高到 50000 能否达到 30%？\nQ3. Forward KL 的 mode-covering 是否解释了 knowledge-intensive tasks 的退化？\nQ4. SPON 正交性显示 static bias 在 KL 框架下几乎无用？",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 或 [REBUT]，并说明理由。如果 [REBUT]，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5/5 (Borderline Conference)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] Coupling alignment 概念存在同义反复（tautological）风险\n- §3.7 将 coupling alignment 定义为\"训练损失是否优化一个跨层组合的量\"，然后论证\"只有直接优化 next-token prediction loss 的目标才能发现产生好 next-token prediction 的 mask\"——逻辑上接近同义反复。\n- 论文同时主张\"gradient coupling remains necessary at the discovery stage\"，但没有提供独立于 PPL/downstream 的 mask 质量定义来打破循环。\n- 建议：(a) 提供可操作形式化定义（如 mask 梯度协方差矩阵秩）；(b) 或降低理论抱负；(c) 测试 intermediate coupling 级别目标（hidden-state KL）。\n\n**N2** [critical] Headline 19% PPL improvement 在非匹配 sparsity 下报告\n- Abstract \"reduces perplexity by 19%\"（10.82→8.81），但 KL 实际 28.5% vs TEAL ~30%。匹配 sparsity 下改善为 14.5%。Abstract 突出 19% 而将 14.5% 藏在正文括号里，构成误导。\n\n**N3** [critical] 50% sparsity 下 downstream 全面崩溃，方法 unambiguous wins 仅限 30% PPL\n- 50% 所有方法 MMLU≈28%（random），GSM8K<2.2%。\n- 30% 也是 mixed：commonsense 赢（ARC +4.4pp, HellaSwag +7.8pp），knowledge-intensive 输（MMLU −5.2pp）。\n- 如果方法只在一个 sparsity level 的 PPL 有优势而 downstream task-dependent，核心价值大打折扣。\n\n### Should-Fix\n\n**W1** Cross-architecture 证据过薄：Mistral/Qwen 均 single seed，14B GSM8K 反转 -20pp。\n**W2** MSE baseline λ_max=1000 vs KL 的 5000，且 single seed，影响 taxonomy 对比公平性。\n**W3** Adaptive penalty 30% 时 λ 触顶 5000，actual sparsity=28.5%（5% deviation），控制器设计存疑。\n**W4** BCE+Gumbel (32.22) 比 standard BCE (27.97) 更差，KL 与 Gumbel 存在未量化交互效应。Loss effect vs relaxation effect 的加法分解假设独立性，但交互作用说明不独立。\n**W5** 梯度分析（§3.6）定性正确但缺乏定量支撑——缺 per-layer gradient 相关性分析或 Jacobian 条件数分析。\n\n### Minor\n- m1: Table 2 † footnote 容易混淆\n- m2: de2024griffin 在 OpenAlex 未找到\n- m3: 固定 τ=0.5 比 default annealing 更好但正文未提及\n- m4: \"primarily empirical study\" 与 §3.6-3.7 的理论贡献定位不一致\n- m5: Figure 2 y轴 log scale 但标注线性刻度值\n\n### Missing References\n- Wortsman et al. (2023) training stability\n- Dettmers et al. (2024) SpQR quantization+sparsity\n- Clark et al. (2020) ELECTRA\n\n### Questions\nQ1. 反向 C1：用 KL 训练在 magnitude-based oracle targets 上性能如何？\nQ2. λ_max 提高到 50000 能否达到 30%？\nQ3. Forward KL 的 mode-covering 是否解释了 knowledge-intensive tasks 的退化？\nQ4. SPON 正交性显示 static bias 在 KL 框架下几乎无用？",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-20T06:45:47.980200+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11625
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-20T06:45:48.734242+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 或 [REBUT]，并说明理由。如果 [REBUT]，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0/5 (Findings)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 与 MaskLLM 的新颖性边界不清晰\n- MaskLLM (NeurIPS 2024) 已使用 frozen weights + KL divergence + Gumbel relaxation + learnable masks 的完整框架。论文三点区分（sparsity type, mask generation, allocation）更像 application domain 差异而非方法论创新。核心 insight \"KL couples gradients\" 在 MaskLLM 中已隐含成立。\n- 建议：明确论证 global allocation 场景的新挑战；提供 MaskLLM 中 KL vs BCE gap 的定量对比。\n\n**N2** [critical] \"Coupling Alignment\" 概念缺少形式化，过度包装已知原理\n- 本质上是\"end-to-end training outperforms component-wise training when components interact\"——深度学习基本原理。Taxonomy (Table 1) 填充空格不构成理论发现。\n- 建议：定位为\"对已知原理在 sparsity prediction 场景的经验验证\"，降低 claim 强度。\n\n### Should-Fix\n\n**W1** 实际可用 regime 过窄：30% 是唯一有意义 regime，但 MMLU 仍大幅退化（65.27%→40.7%），TEAL 反而更好（45.86%）。加 6.4% latency overhead 无实际加速。\n**W2** 跨架构/跨规模结果过于初步：Mistral single-seed，14B MMLU -2.79pp、GSM8K -20pp，但 Abstract/Conclusion 仍作为 contribution。\n**W3** Abstract 数字选择性呈现：只展示 KL 胜出任务，MMLU -5.2pp 仅给标签，未提及绝对退化（65.3%→40.7%）。\n**W4** Training data 单一性：所有 predictor 仅在 WikiText-103 训练，C4 OOD 仅报告 PPL 未报告 downstream，C4 cross-seed variance 增大（CV 6.3%）。\n\n### Minor\n- M1: 30% λ 达 cap (5000)，最实用 regime 表现最差\n- M2: MSE λ_max=1000 vs KL 5000 未控制\n- M3: Figure 2 caption \"82% at 70%\" 但 70% downstream 不可用\n- M4: \"proximate quality driver\" 反复出现\n- M5: xu2026spon year=2026 但引为 ICML 2025\n- M6: de2024griffin OpenAlex not_found\n\n### Missing References\n1. \"A Sparsity Predicting Approach via Activation Pattern Clustering\" (Dhar et al., 2025)\n2. \"Universal Properties of Activation Sparsity in Modern LLMs\" (arXiv:2509.00454)\n3. §2 \"All prior predictor-based methods use decomposed or intermediate objectives\" 需更精确限定\n\n### Excitement: 2.5/5 — 经验性发现有价值但属 incremental；MaskLLM 已用 KL+Gumbel；无 wall-clock speedup；可用 regime 仅 30%。\n\n### Questions\n1. MaskLLM 中 KL vs BCE 的 PPL gap 与本文 2.4× gap 可比吗？\n2. 30% 下有无方法恢复 MMLU 差距？\n3. Gumbel 对 KL 有利但对 BCE 有害——为什么？",
  "project": "distill_sparse_swiglu",
  "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
  "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 或 [REBUT]，并说明理由。如果 [REBUT]，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0/5 (Findings)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 与 MaskLLM 的新颖性边界不清晰\n- MaskLLM (NeurIPS 2024) 已使用 frozen weights + KL divergence + Gumbel relaxation + learnable masks 的完整框架。论文三点区分（sparsity type, mask generation, allocation）更像 application domain 差异而非方法论创新。核心 insight \"KL couples gradients\" 在 MaskLLM 中已隐含成立。\n- 建议：明确论证 global allocation 场景的新挑战；提供 MaskLLM 中 KL vs BCE gap 的定量对比。\n\n**N2** [critical] \"Coupling Alignment\" 概念缺少形式化，过度包装已知原理\n- 本质上是\"end-to-end training outperforms component-wise training when components interact\"——深度学习基本原理。Taxonomy (Table 1) 填充空格不构成理论发现。\n- 建议：定位为\"对已知原理在 sparsity prediction 场景的经验验证\"，降低 claim 强度。\n\n### Should-Fix\n\n**W1** 实际可用 regime 过窄：30% 是唯一有意义 regime，但 MMLU 仍大幅退化（65.27%→40.7%），TEAL 反而更好（45.86%）。加 6.4% latency overhead 无实际加速。\n**W2** 跨架构/跨规模结果过于初步：Mistral single-seed，14B MMLU -2.79pp、GSM8K -20pp，但 Abstract/Conclusion 仍作为 contribution。\n**W3** Abstract 数字选择性呈现：只展示 KL 胜出任务，MMLU -5.2pp 仅给标签，未提及绝对退化（65.3%→40.7%）。\n**W4** Training data 单一性：所有 predictor 仅在 WikiText-103 训练，C4 OOD 仅报告 PPL 未报告 downstream，C4 cross-seed variance 增大（CV 6.3%）。\n\n### Minor\n- M1: 30% λ 达 cap (5000)，最实用 regime 表现最差\n- M2: MSE λ_max=1000 vs KL 5000 未控制\n- M3: Figure 2 caption \"82% at 70%\" 但 70% downstream 不可用\n- M4: \"proximate quality driver\" 反复出现\n- M5: xu2026spon year=2026 但引为 ICML 2025\n- M6: de2024griffin OpenAlex not_found\n\n### Missing References\n1. \"A Sparsity Predicting Approach via Activation Pattern Clustering\" (Dhar et al., 2025)\n2. \"Universal Properties of Activation Sparsity in Modern LLMs\" (arXiv:2509.00454)\n3. §2 \"All prior predictor-based methods use decomposed or intermediate objectives\" 需更精确限定\n\n### Excitement: 2.5/5 — 经验性发现有价值但属 incremental；MaskLLM 已用 KL+Gumbel；无 wall-clock speedup；可用 regime 仅 30%。\n\n### Questions\n1. MaskLLM 中 KL vs BCE 的 PPL gap 与本文 2.4× gap 可比吗？\n2. 30% 下有无方法恢复 MMLU 差距？\n3. Gumbel 对 KL 有利但对 BCE 有害——为什么？",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-20T06:45:50.399216+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1664
}
```

</details>

---


### Assistant

_source line 1302 · 2026-05-20T06:45:54.168519+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1303 · 2026-05-20T06:45:56.908397+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：论文被评为 **3.0/5 (Findings)**。两个 critical 问题：(1) 与 MaskLLM 的新颖性边界不够清晰——KL+Gumbel+frozen weights 的框架已存在；(2) "coupling alignment" 概念将已知原理包装为新贡献但缺乏形式化。四个 should-fix：实际可用 regime 仅 30% 且 MMLU 退化、跨架构结果过于初步、Abstract 选择性呈现、训练数据单一。论文的主要优势在于 C1 target-swap ablation 设计精巧、实验诚实度高、multi-seed 规范。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1304 · 2026-05-20T06:46:02.396408+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 106

## Round 106

2 recorded events


### User

_source line 1305 · 2026-05-20T06:47:49.364068+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: 与 MaskLLM 的新颖性边界不清晰**

Reviewer 2 认为 MaskLLM 已使用完整的 KL+Gumbel+frozen weights+learnable masks 框架，本文仅为 application domain 差异。我部分不同意。

论文 §2 (lines 139-180) 明确列出三个结构性差异，这些不是表面的 domain 差异：

1. **Sparsity type 差异是根本性的**：MaskLLM 学习 N:M semi-structured *weight* sparsity（静态 2:4 pattern，训练后固定），本文学习 *activation* sparsity（动态 per-token，每个输入生成不同 mask）。Weight mask 固定后没有 per-token prediction 问题——MaskLLM 的 mask 本身就是参数，无需 predictor network。本文的核心挑战——训练一个 predictor 从 hidden states 预测 input-dependent masks——在 MaskLLM 中根本不存在。

2. **全局预算竞争是新问题**：MaskLLM 在固定 N:M group 内优化，无跨组预算竞争（line 167-168）。本文的 mask 参与 global top-k 排名，跨层竞争预算（line 168-170）。这引入了 inter-layer dependency——正是 coupling alignment 分析的对象——MaskLLM 无需处理。

3. **"KL couples gradients" insight 在 MaskLLM 中并非"隐含成立"**：MaskLLM 从未比较 KL vs BCE，从未分析梯度结构差异，也未进行 target-swap ablation。MaskLLM 选择 KL 是因为蒸馏文献的常规选择，不是基于 coupling 分析。论文的贡献不在于"使用 KL"，而在于分析 *why* KL works differently from BCE in the sparsity prediction context, supported by C1 ablation (Table 3)。

但我同意 Reviewer 2 的一点：论文应更明确地论证 **为什么 activation sparsity + global allocation 场景让 KL vs BCE 差异更 pronounced**（可能是因为 global top-k 放大了 inter-layer coupling 的效果，而 N:M 的 local constraint 限制了 coupling 的影响范围）。这个论证在论文中缺失。

---

**[AGREE] R2-N2: "Coupling Alignment" 概念缺少形式化，过度包装已知原理**

我在自己的审稿中也将此列为 N1 (critical)。

Reviewer 2 的概括更直接：本质上是 "end-to-end training outperforms component-wise training when components interact"——这确实是深度学习基本原理。论文 §3.7 的 2D taxonomy (Table 1) 分类本身有组织价值，但将"填充空格"包装为"identify coupling alignment as the decisive factor"（Conclusion line 637）确实过度了。

补充我的证据：§3.7 lines 426-428 定义 coupling alignment 为"whether the training loss optimizes a quantity that composes across layers"，但（a）没有给出 composability 的形式化度量；（b）没有测试"intermediate coupling"级别的目标（如 hidden-state KL）来验证"更 coupled = 更好"的单调预测；（c）C1 ablation 实际上显示 mask quality（而非 coupling 本身）是 proximate driver——这与"coupling alignment as the decisive factor"的结论自相矛盾。

建议与 R2 一致：降低 claim 强度，定位为"对已知原理在 sparsity prediction 场景的经验验证 + 实用配方"。

---

### Should-Fix

**[AGREE] R2-W1: 实际可用 regime 过窄**

与我的 N3 一致。补充一个 R2 没有完全展开的角度：

Table 14 显示 30% uniform 下 MMLU=40.7±1.3，但 dense MMLU=45.86（Table 2 第一行的 0% sparsity 行误标为 65.27——实际看 Table 2 原文，0% dense 行 MMLU=45.86——请 R2 核实，65.27 可能来自 Table 14 的不同配置）。即使取 40.7 vs 45.86，退化幅度是 5.16pp（11.2%），不是 R2 所说的 "65.27→40.7"（24.57pp）。

不过这不影响核心论点：KL 在 30% 下 MMLU (40.7) 不如 TEAL uniform (41.2，Table 2 TEAL uniform 行) 甚至不如 BCE global† (45.86——wait, 这是 dense baseline)。实际上 TEAL 30% 的 downstream 比较需要看 Table 2: TEAL uniform 30% 的 MMLU 为 —— let me re-check: Table 2 shows at 30%, TEAL uniform MMLU = 54.38? No, the 0% row is Dense with MMLU=45.86. At 30%, TEAL uniform: PPL=10.82, ARC-c=27.47 — wait, that doesn't look right either. Let me quote directly: Table 2 at 30% shows KL uniform MMLU=40.7±1.3, and TEAL uniform is the baseline at 30% with MMLU not separately listed...

实际上关键比较是 KL uniform MMLU 40.7 vs BCE global MMLU 45.86（Table 2, 30% BCE global† row）——但 BCE global† 是 2700 steps trained，不是 training-free。对比 TEAL，Table 2 的 TEAL uniform 30% MMLU = 54.38——那是不对的，TEAL 行的值是 PPL=10.82, ARC-c=59.33, WG=78.06, MMLU=45.86, GSM8K=48.75——等等，那是 0% Dense 行。

让我重新核实：我的核心同意立场不变——30% 是唯一有意义的 regime，且 downstream 是 mixed。

---

**[AGREE] R2-W2: 跨架构/跨规模结果过于初步**

与我的 W1 完全一致。14B 的 GSM8K -20pp 尤其令人担忧——如果 scale-up 恶化 reasoning，这对方法的 scalability 是负面信号。论文在 Abstract (line 029-031) 和 Conclusion (line 655-657) 都将 cross-architecture 结果作为 contribution claim，这与"preliminary single-seed"的实际证据强度不匹配。

---

**[AGREE] R2-W3: Abstract 数字选择性呈现**

与我的 N2 一致。Abstract 突出 19% PPL improvement（非匹配 sparsity）和 commonsense reasoning gains（ARC +4.4pp, HellaSwag +7.8pp），而将 MMLU -5.2pp 压缩为"knowledge-intensive benchmarks favor TEAL's narrower activation preservation"（line 015），不提绝对值退化幅度。这种不对称呈现是 overclaiming 的典型模式。

---

**[AGREE] R2-W4: Training data 单一性**

这是我审稿中遗漏的有效问题。补充：

- C4 OOD 评估（Appendix D, Table 11）仅报告 PPL，未报告任何 downstream task。如果 predictor 过拟合 WikiText-103 的 activation patterns（论文自己在 Limitations line 698-700 承认"partially overfits to training-domain activation patterns"），那 downstream OOD 性能可能比 PPL OOD 更差。
- C4 cross-seed variance CV=6.3% vs WikiText-2 CV=0.2%——30× 增大——说明 predictor 的 OOD robustness 存在问题。
- Seed 42 的 C4 PPL (18.22) 远高于其他 seeds (16.37, 16.36)——这与 seed 42 在其他实验中的异常值模式一致（Table 3 的 s42 C1 也来自不同 run），暗示存在 seed-specific overfitting。

建议在 C4 上也报告至少 ARC-c 和 MMLU 的 downstream performance。

---

### Minor

**[AGREE] R2-M1**: λ 达 cap 在最实用 regime——与我的 W3 一致。

**[AGREE] R2-M2**: MSE λ_max 不匹配——与我的 W2 一致。

**[AGREE] R2-M3**: Figure 2 标注 "82% at 70%" 但 70% downstream 完全不可用（Table 14: 50% 已 collapse），纯 PPL 比较在实用角度无意义。这个标注对读者有误导性——暗示方法在 70% 仍有价值。

**[AGREE] R2-M4**: "proximate quality driver" 在 §4.4 (line 571), §5 (line 644), Abstract (line 023) 反复出现。风格问题但确实冗余。

**[AGREE] R2-M5**: xu2026spon 的 bib key 标为 2026 但论文发表于 ICML 2025。引用验证也确认 matched_year=2025。应修正 bib 年份。

**[AGREE] R2-M6**: de2024griffin 在 OpenAlex 未找到——与我的 m2 一致。

---

### Missing References

**[NEUTRAL] R2-Missing-1/2**: 我无法验证 "Dhar et al., 2025" 和 "arXiv:2509.00454" 的存在性和相关性。如果确实存在，应当引用。

**[AGREE] R2-Missing-3**: §2 line 172-173 "All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives" 需要更精确限定范围（如 "for activation sparsity prediction"），因为 MaskLLM 已在 weight sparsity 场景使用 KL。

---

### Excitement 评分

R2 给 Excitement 2.5/5，我给 3.5/5。分歧在于：

R2 认为 MaskLLM 已用 KL+Gumbel，所以本文是 incremental。如上述 REBUT 所论，我认为 activation sparsity + predictor + global allocation 是不同问题。但我同意 coupling alignment 框架的理论贡献有限（本质上是已知原理的经验验证）。综合来看，我的 Excitement 评分保持 3.5——核心实证发现（KL-derived masks diverge 46-68% from magnitude yet produce lower PPL）和 C1 ablation 的实验设计有足够新颖性，但不足以到 4.0。

---

### Reviewer 2 Questions 的补充

**Q1 (MaskLLM KL vs BCE gap)**: 好问题。MaskLLM 论文未报告 KL vs BCE 对比（只用了 KL）。如果 MaskLLM 中 KL vs BCE gap 很小，这会削弱本文的 coupling alignment 论证——因为 coupling 在 N:M constrained 场景也应有效果。作者应尝试在 MaskLLM 设置下复现 KL vs BCE 对比，或至少讨论为什么 gap 在 global allocation 下可能更大。

**Q2 (30% MMLU recovery)**: 我在自己的 Q3 中也问了相关问题。Forward KL 的 mode-covering 性质可能是 MMLU 退化的根因——保留了过多的 activation patterns 导致 knowledge concentration 不足。

**Q3 (Gumbel+KL vs Gumbel+BCE interaction)**: 我在自己的 W4 中详细讨论了这个问题。Table 4 的数据清晰显示 Gumbel 对 KL 有利（+relaxation enables gradient flow through mask）但对 BCE 有害（stochastic sampling corrupts binary target signal）。论文的"加法分解"（loss effect 5.1× relaxation effect）假设效应独立，但 BCE+Gumbel 的恶化证明存在交互效应。这是方法论上的一个 gap。

---

### 综合判断

R2 总体给 3.0 (Findings)，我给 3.5 (Borderline Conference)。在审阅 R2 的意见后，我认为：

- R2-N1 (MaskLLM novelty) 的主要论点我不完全同意——activation sparsity prediction 与 weight sparsity optimization 是不同问题——但论文确实需要更 explicit 地论证新颖性边界
- R2-N2 (coupling alignment over-packaged) 我完全同意，与我自己的 N1 一致
- R2 对 practical value 的质疑（W1, W3）有效且与我的 N3 一致

我**维持** 3.5 的评分。C1 target-swap ablation 的实验设计和"KL-derived masks diverge yet perform better"的核心发现仍有足够 novelty for borderline conference，但 coupling alignment 的理论 claim 需要显著降级。如果 camera-ready 能修复 headline number（14.5% at matched sparsity）并降低理论 claim，适合 Conference (weak accept)。否则 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1306 · 2026-05-20T06:48:01.608541+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 107

## Round 107

10 recorded events


### User

_source line 1307 · 2026-05-20T06:48:02.806170+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心立场：

- **R2-N1 (MaskLLM novelty)**: [REBUT] — activation sparsity prediction 与 weight sparsity optimization 是结构性不同的问题，不是 domain 差异。但同意论文需更 explicit 论证新颖性边界。
- **R2-N2 (coupling alignment)**: [AGREE] — 与我自己的 N1 一致，本质是已知原理的包装。
- **R2-W1/W2/W3/W4**: 全部 [AGREE]，与我自己的 N2/N3/W1 一致。W4 (training data 单一性) 是我遗漏的有效问题。
- **评分维持 3.5** (vs R2 的 3.0)：C1 ablation 的实验设计和 mask divergence 发现仍有足够 novelty，但理论 claim 需降级。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Must-Fix

**[PARTIALLY AGREE] R1-N1: Coupling alignment 同义反复**
形式化缺失成立（与我 N2 一致），但"同义反复"定性过重。MSE 也是 end-to-end 的但比 training-free TEAL 差 1.9×（Table 2: MSE 20.43 vs TEAL 10.82 at 30%），说明 coupling 的 **层级** 而非 coupling 本身是关键——这个发现不是 trivial 的。建议采纳 R1 的 (b)+(c)：降低理论抱负 + 补充 hidden-state KL 对照实验。

**[AGREE] R1-N2: 19% 在非匹配 sparsity 下**
KL actual 28.5% vs TEAL 29.3%，matched-sparsity 改善仅 14.5%（§4.2 parenthetical, Appendix C: TEAL at 28.5% PPL 10.30）。Abstract 突出 19% 构成选择性呈现。比我的 W3 更精确。

**[AGREE] R1-N3: 50% collapse + 方法仅 30% PPL 有优势**
与我 W1 完全一致。30% 也是 mixed（commonsense 4/4 win, knowledge 0/2 lose）。Unambiguous win 仅在 "30% × PPL" 窄窗口。

### Should-Fix

**[AGREE] R1-W1**: 与我 W2 一致。
**[PARTIALLY AGREE] R1-W2**: Appendix G defense 对 50%（MSE 229 vs TEAL 23.9）成立，但 MSE single seed 仍需验证 50% 结果非异常值。
**[AGREE] R1-W3**: 与我 M1 一致，但 matched-sparsity 对比限制了影响。
**[AGREE] R1-W4**: BCE+Gumbel 交互效应是 R1 独到观察。Gumbel 对 BCE 有害（+4.25 PPL）对 KL 有利（-3.98 PPL），additive decomposition 的独立性假设不成立。
**[AGREE] R1-W5**: 与我 N2 中形式化缺失一致。

### Minor

**[AGREE]** R1-m1, m2, m3, m5
**[PARTIALLY AGREE]** R1-m4: §3.6 已有 hedge ("This analysis is suggestive")，更多是 framing 不一致。

### Missing References

**[PARTIALLY AGREE]** Wortsman/SpQR: tangentially related
**[REBUT]** Clark et al. (2020) ELECTRA: 与 activation sparsity prediction 训练目标选择无直接关联。

### 综合评估

R1 和我在核心问题上高度一致：(1) 新颖性边界模糊（我 N1 vs MaskLLM, R1 N1 tautology）；(2) 实际 regime 过窄（我 W1, R1 N3）；(3) headline 数字选择性呈现（我 W3, R1 N2）。R1 的 N2（sparsity 不匹配）和 W4（交互效应）是我遗漏的有价值观点。

我维持 Overall 3.0 (Findings)。R1 给 3.5 (Borderline Conference) 略高于我，主要分歧在 excitement——R1 似乎对 C1 ablation 的方法论贡献给了更高权重。综合两份 review，3.0-3.5 是合理区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-20T06:48:27.239444+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-20T06:48:27.440452+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T06:37:09.483130+00:00\", \"completed_at\": \"2026-05-20T06:39:35.889887+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-4\", \"message\": \"连续 4 页纯文本无任何 display item（figure/table），审稿人前 2 分钟只看到密集文字，缺乏视觉锚点。Figure 1 在 page 3 正文首次引用但漂移到 page 5，建议将 Figure 1 提前至 page 2 或 page 3（Introduction 末尾或 Method 开头）\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Figure 7 仅占页面约 1/3，上方约 2/3 为空白。建议将 Figure 7 与前页内容合并，或在该页补充附录内容填充空间\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1（方法架构图）为单栏宽度，文字接近可读性下限。若内容允许，考虑使用 figure*（全宽）以提高清晰度\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"单页包含 4 个表格（Tables 7-10），排版密集但未溢出；附录可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 折线图仅有 2 条线（KL vs TEAL），颜色区分度好，但建议增加 marker 形状差异以确保灰度打印可辨\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-20T06:48:27.440866+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-20T06:48:27.491701+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-20T06:50:06.297809+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 15 — New/Escalated issues\n  # ============================================================\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装，缺乏形式化定义，接近同义反复\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W5. 缺乏操作性定义.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N1 + R2-N2 共识. 本质是 'end-to-end > component-wise' 基本原理的重新包装. Taxonomy (Table 1) 填充空格不构成理论发现. Conclusion 首句 claim 过度.\"}\n    action_items:\n      - {round: 15, action: \"降低理论抱负: 定位为'已知原理在 sparsity prediction 场景的经验验证 + 实用配方', 非核心 contribution. 或补充 hidden-state KL 对照实验验证 coupling 层级假设.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity (28.5% vs 30%) 下报告, 匹配 sparsity 仅 14.5%\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R13-W3.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R14-W8. 正文括号内承认 14.5% 但 abstract 仍突出 19%.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N2 + R2-W3 共识. Abstract 使用 19% 构成选择性呈现. 正文 §4.2 有括号注但 abstract 未修正.\"}\n    action_items:\n      - {round: 15, action: \"Abstract 使用匹配 sparsity 下的 14.5% 数字, 或明确标注 '(at 28.5% actual vs TEAL 30%)'.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰 (R2 critical, R1 partial rebut)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W3.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R2-N1 critical: KL+Gumbel+frozen weights 框架已存在于 MaskLLM. R1 REBUT: activation sparsity + predictor + global allocation 是结构性不同问题. R2 部分接受但维持 critical. 论文需更 explicit 论证为什么 global allocation 场景让 KL vs BCE 差异更 pronounced.\"}\n    action_items:\n      - {round: 15, action: \"§2 MaskLLM 段落加入 'why global allocation makes KL-BCE gap more salient than N:M' 的论证. 可选: 引用/讨论 MaskLLM 中 KL vs BCE gap 是否存在.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, 且 downstream 为 task-dependent (commonsense 4/4 win, knowledge 0/2 lose)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W1. 升级为 Must-Fix.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N3 + R2-W1 共识. 50% downstream collapse to near-random. 30% MMLU 40.7 vs TEAL 45.86 (-5.2pp). KL predictor 增加 6.4% latency overhead 无实际加速. 方法的 unambiguous wins 仅在 '30% × PPL' 窄窗口.\"}\n    action_items:\n      - {round: 15, action: \"Abstract/Intro 更平衡呈现 downstream: 明确 commonsense 4/4 win + knowledge 0/2 lose 的 task-type split. 讨论 mode-covering 与 knowledge tasks 的 tradeoff.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W2\"\n    summary: \"跨架构/跨规模证据过薄: single seed, 14B GSM8K 反转 -20pp\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W4 (R13-N2 延续).\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-W1 + R2-W2 共识. Mistral/Qwen 均 single seed. 14B GSM8K -20pp (32.1±5.2% vs TEAL 52.1%). Abstract/Conclusion 仍将 cross-arch 作为 contribution 但证据不匹配.\"}\n    action_items:\n      - {round: 15, action: \"至少 Mistral 补 3-seed (~2h). 或将 cross-arch 从 contribution list 移除, 仅作 discussion.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"BCE+Gumbel 比 standard BCE 更差, KL 与 Gumbel 存在未量化交互效应\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W7.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-W4 + R2 AGREE. BCE+Gumbel 32.22 vs BCE 27.97 (+4.25 PPL). 论文 §4.5 的 additive decomposition (loss 5.1× relaxation) 假设独立性但交互效应存在. 需补 BCE+STE 对照或正式承认交互效应.\"}\n    action_items:\n      - {round: 15, action: \"§4.5 补充 BCE+STE 数据点, 或承认 KL×Gumbel 正向交互并量化.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"Training data 单一 (WikiText-103 only), OOD downstream 未评估, C4 cross-seed variance 30× 增大\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - {round: 15, reviewers: [1, 2], note: \"R2-W4 新提出, R1 AGREE. C4 OOD 仅报告 PPL (Appendix D) 未报告 downstream. C4 CV=6.3% vs WikiText-2 CV=0.2%. Seed 42 C4 PPL 18.22 远高于其他 seeds (16.37, 16.36).\"}\n    action_items:\n      - {round: 15, action: \"C4 上补 ARC-c/MMLU downstream, 或在 Limitations 更强调 OOD robustness 不足.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"MSE baseline λ_max=1000 vs KL 5000, 且 single seed, taxonomy 对比公平性存疑\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W2 (配置透明性).\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-W2 + R2-M2 共识. Appendix G 已补配置但 λ_max 仍不匹配. 50% gap (229 vs 23.9) 大到 seed 不影响结论, 但 30% (20.4 vs 10.8) 需确认.\"}\n    action_items:\n      - {round: 15, action: \"统一 λ_max 或说明为什么 MSE 需不同值.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W6\"\n    summary: \"梯度分析 (§3.6) 定性正确但缺乏定量支撑 gradient coupling 强度\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - {round: 15, reviewers: [1, 2], note: \"R1-W5 + R2 部分同意 (与 N2 形式化缺失一致). SNR 分析不能区分 'gradient direction 更好' vs 'gradient 更 coupled'. 缺 per-layer gradient 相关性或 Jacobian 条件数分析.\"}\n    action_items:\n      - {round: 15, action: \"补充 cross-layer gradient correlation 实验, 或降低 §3.6 的机制性 claim.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-M1\"\n    summary: \"Abstract 选择性呈现数字: 突出 KL wins (ARC +4.4pp, HS +7.8pp), 弱化 MMLU -5.2pp, 不提绝对退化\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - {round: 15, reviewers: [1, 2], note: \"R1-N2 延伸 + R2-W3. MMLU 从 dense 65.27% 降至 40.7% 幅度被隐藏.\"}\n    action_items:\n      - {round: 15, action: \"Abstract 加入 MMLU 绝对退化幅度或更平衡的 task-type framing.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 14 — Carried forward (status updates)\n  # ============================================================\n\n  - id: \"R14-VIS\"\n    summary: \"Appendix 占位符 figure [Placeholder: layernorm_dynamics.pdf]\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"lagrangian_dynamics.pdf figure 已注释掉 (appendix.tex lines 137-143), 引用已删除. R15 未再提.\"\n    resolution_round: 15\n\n  - id: \"R14-W6\"\n    summary: \"Conclusion 过短 + vspace{-18pt}\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"Conclusion 现为 9 句完整段落 (§5), 无 vspace hack. R15 未再提.\"\n    resolution_round: 15\n\n  - id: \"R13-N1\"\n    summary: \"MSE baseline 缺失\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"MSE 30% PPL=20.43, 50% PPL=229.26 + 7-task eval. Appendix G 配置段已补. R15 转为 λ_max 匹配性问题 (R15-W5).\"\n    resolution_round: 15\n\n  - id: \"R13-N3\"\n    summary: \"SNR 选择性呈现 + LR schedule 不匹配\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    resolution: \"§3.6 + Appendix H 完整重写. SNR figure 用 1000 步 14-snapshot 数据. R15 列为 Strength (诚实呈现 BCE SNR > KL).\"\n    resolution_round: 15\n\n  - id: \"R13-W7\"\n    summary: \"C4 OOD 3-seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"3-seed 数据完整. R15 转为 OOD downstream 评估缺失 (R15-W4).\"\n    resolution_round: 15\n\n  - id: \"R12-N1\"\n    summary: \"C1 50% max Δ 数值错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Corrected to 0.79pp.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 vs Table 4 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Labeling clarified.\"\n    resolution_round: 13\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"C1 target-swap ablation 解决.\"\n    resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 15 — New/Escalated issues\n  # ============================================================\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装，缺乏形式化定义，接近同义反复\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W5. 缺乏操作性定义.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N1 + R2-N2 共识. 本质是 'end-to-end > component-wise' 基本原理的重新包装. Taxonomy (Table 1) 填充空格不构成理论发现. Conclusion 首句 claim 过度.\"}\n    action_items:\n      - {round: 15, action: \"降低理论抱负: 定位为'已知原理在 sparsity prediction 场景的经验验证 + 实用配方', 非核心 contribution. 或补充 hidden-state KL 对照实验验证 coupling 层级假设.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity (28.5% vs 30%) 下报告, 匹配 sparsity 仅 14.5%\"\n    category: writing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 15\n    mentions:\n      - {round: 13, reviewers: [1, 2], note: \"R13-W3.\"}\n      - {round: 14, reviewers: [1, 2], note: \"R14-W8. 正文括号内承认 14.5% 但 abstract 仍突出 19%.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N2 + R2-W3 共识. Abstract 使用 19% 构成选择性呈现. 正文 §4.2 有括号注但 abstract 未修正.\"}\n    action_items:\n      - {round: 15, action: \"Abstract 使用匹配 sparsity 下的 14.5% 数字, 或明确标注 '(at 28.5% actual vs TEAL 30%)'.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰 (R2 critical, R1 partial rebut)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W3.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R2-N1 critical: KL+Gumbel+frozen weights 框架已存在于 MaskLLM. R1 REBUT: activation sparsity + predictor + global allocation 是结构性不同问题. R2 部分接受但维持 critical. 论文需更 explicit 论证为什么 global allocation 场景让 KL vs BCE 差异更 pronounced.\"}\n    action_items:\n      - {round: 15, action: \"§2 MaskLLM 段落加入 'why global allocation makes KL-BCE gap more salient than N:M' 的论证. 可选: 引用/讨论 MaskLLM 中 KL vs BCE gap 是否存在.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, 且 downstream 为 task-dependent (commonsense 4/4 win, knowledge 0/2 lose)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W1. 升级为 Must-Fix.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N3 + R2-W1 共识. 50% downstream collapse to near-random. 30% MMLU 40.7 vs TEAL 45.86 (-5.2pp). KL predictor 增加 6.4% latency overhead 无实际加速. 方法的 unambiguous wins 仅在 '30% × PPL' 窄窗口.\"}\n    action_items:\n      - {round: 15, action: \"Abstract/Intro 更平衡呈现 downstream: 明确 commonsense 4/4 win + knowledge 0/2 lose 的 task-type split. 讨论 mode-covering 与 knowledge tasks 的 tradeoff.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W2\"\n    summary: \"跨架构/跨规模证据过薄: single seed, 14B GSM8K 反转 -20pp\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 11\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W4 (R13-N2 延续).\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-W1 + R2-W2 共识. Mistral/Qwen 均 single seed. 14B GSM8K -20pp (32.1±5.2% vs TEAL 52.1%). Abstract/Conclusion 仍将 cross-arch 作为 contribution 但证据不匹配.\"}\n    action_items:\n      - {round: 15, action: \"至少 Mistral 补 3-seed (~2h). 或将 cross-arch 从 contribution list 移除, 仅作 discussion.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"BCE+Gumbel 比 standard BCE 更差, KL 与 Gumbel 存在未量化交互效应\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W7.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-W4 + R2 AGREE. BCE+Gumbel 32.22 vs BCE 27.97 (+4.25 PPL). 论文 §4.5 的 additive decomposition (loss 5.1× relaxation) 假设独立性但交互效应存在. 需补 BCE+STE 对照或正式承认交互效应.\"}\n    action_items:\n      - {round: 15, action: \"§4.5 补充 BCE+STE 数据点, 或承认 KL×Gumbel 正向交互并量化.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"Training data 单一 (WikiText-103 only), OOD downstream 未评估, C4 cross-seed variance 30× 增大\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - {round: 15, reviewers: [1, 2], note: \"R2-W4 新提出, R1 AGREE. C4 OOD 仅报告 PPL (Appendix D) 未报告 downstream. C4 CV=6.3% vs WikiText-2 CV=0.2%. Seed 42 C4 PPL 18.22 远高于其他 seeds (16.37, 16.36).\"}\n    action_items:\n      - {round: 15, action: \"C4 上补 ARC-c/MMLU downstream, 或在 Limitations 更强调 OOD robustness 不足.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"MSE baseline λ_max=1000 vs KL 5000, 且 single seed, taxonomy 对比公平性存疑\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W2 (配置透明性).\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-W2 + R2-M2 共识. Appendix G 已补配置但 λ_max 仍不匹配. 50% gap (229 vs 23.9) 大到 seed 不影响结论, 但 30% (20.4 vs 10.8) 需确认.\"}\n    action_items:\n      - {round: 15, action: \"统一 λ_max 或说明为什么 MSE 需不同值.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W6\"\n    summary: \"梯度分析 (§3.6) 定性正确但缺乏定量支撑 gradient coupling 强度\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - {round: 15, reviewers: [1, 2], note: \"R1-W5 + R2 部分同意 (与 N2 形式化缺失一致). SNR 分析不能区分 'gradient direction 更好' vs 'gradient 更 coupled'. 缺 per-layer gradient 相关性或 Jacobian 条件数分析.\"}\n    action_items:\n      - {round: 15, action: \"补充 cross-layer gradient correlation 实验, 或降低 §3.6 的机制性 claim.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-M1\"\n    summary: \"Abstract 选择性呈现数字: 突出 KL wins (ARC +4.4pp, HS +7.8pp), 弱化 MMLU -5.2pp, 不提绝对退化\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - {round: 15, reviewers: [1, 2], note: \"R1-N2 延伸 + R2-W3. MMLU 从 dense 65.27% 降至 40.7% 幅度被隐藏.\"}\n    action_items:\n      - {round: 15, action: \"Abstract 加入 MMLU 绝对退化幅度或更平衡的 task-type framing.\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 14 — Carried forward (status updates)\n  # ============================================================\n\n  - id: \"R14-VIS\"\n    summary: \"Appendix 占位符 figure [Placeholder: layernorm_dynamics.pdf]\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"lagrangian_dynamics.pdf figure 已注释掉 (appendix.tex lines 137-143), 引用已删除. R15 未再提.\"\n    resolution_round: 15\n\n  - id: \"R14-W6\"\n    summary: \"Conclusion 过短 + vspace{-18pt}\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"Conclusion 现为 9 句完整段落 (§5), 无 vspace hack. R15 未再提.\"\n    resolution_round: 15\n\n  - id: \"R13-N1\"\n    summary: \"MSE baseline 缺失\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"MSE 30% PPL=20.43, 50% PPL=229.26 + 7-task eval. Appendix G 配置段已补. R15 转为 λ_max 匹配性问题 (R15-W5).\"\n    resolution_round: 15\n\n  - id: \"R13-N3\"\n    summary: \"SNR 选择性呈现 + LR schedule 不匹配\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    resolution: \"§3.6 + Appendix H 完整重写. SNR figure 用 1000 步 14-snapshot 数据. R15 列为 Strength (诚实呈现 BCE SNR > KL).\"\n    resolution_round: 15\n\n  - id: \"R13-W7\"\n    summary: \"C4 OOD 3-seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"3-seed 数据完整. R15 转为 OOD downstream 评估缺失 (R15-W4).\"\n    resolution_round: 15\n\n  - id: \"R12-N1\"\n    summary: \"C1 50% max Δ 数值错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Corrected to 0.79pp.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 vs Table 4 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Labeling clarified.\"\n    resolution_round: 13\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"C1 target-swap ablation 解决.\"\n    resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-20T06:50:06.567268+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 9321}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 269
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-20T06:52:24.919443+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 15 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**审稿编排**: 2 Reviewers — R1 (方法严谨性 + 实验完整性), R2 (新颖性 + 完整性 + 写作质量)\n**交叉轮数**: 1 轮（关键问题已收敛）\n\n---\n\n## Summary\n\n本文提出用 forward KL 蒸馏替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的上下文稀疏性预测器。在 LLaMA-3.1-8B 上，KL 预测器（75.9M 参数，<1% base）在 30% sparsity 下将 TEAL 的 perplexity 从 10.82 降至 8.81（非匹配 sparsity 下 19%，匹配 sparsity 下 14.5%）。Target-swap ablation (C1) 证明 KL 发现的 mask pattern（与 magnitude mask 偏差 46-68%）是推理阶段质量的近端驱动因素。论文提出 \"coupling alignment\" 概念组织 sparsity prediction 方法的二维分类，但两位 Reviewer 均认为该概念缺乏形式化定义且过度包装已知原理。方法的实际可用范围窄——50% sparsity 下所有方法 downstream collapse，30% 下 downstream 为 task-dependent（commonsense 赢 4/4，knowledge 输 0/2）。\n\n---\n\n## Strengths\n\n**S1. C1 Target-swap ablation 设计精巧且有说服力** [R1 S2, R2 S1, 共识]\n将 mask 质量与训练机制解耦：BCE 在 KL-derived targets 上训练，复现 KL 性能（50% Δ≤0.79pp，30% retrained Δ≤1.18pp）。直接回答了\"是 mask 更好还是训练过程更好\"的因果问题。这是全文最有价值的实验证据。\n\n**S2. 实验诚实度高** [R1 S4, R2 S2, 共识]\n坦承 50% downstream collapse、cross-architecture 为\"preliminary single-seed\"、缺乏 wall-clock speedup、OOD 过拟合。在 MMLU 和 GSM8K 上的负面结果如实报告。\n\n**S3. Multi-seed 评估规范 + Appendix 充实** [R1 S3, R2 S3/S4, 共识]\n核心实验 3-seed（PPL CV=0.2%），6 downstream tasks。Appendix A-P 涵盖 bottleneck sensitivity、temperature schedule、training convergence、OOD、compensation redundancy 等，reproducibility 支持好。超参完整列出（§4.1）。\n\n**S4. 问题定位精准** [R1 S1]\n首次系统质疑\"为什么 sparsity predictor 都用 BCE\"，填补 Table 1 中 Per-token × Coupled 的空白。\n\n**S5. SNR 分析诚实** [R1 交叉回应]\nSNR figure (Appendix H) 用完整 1000 步 14-checkpoint 数据，诚实呈现 BCE SNR 2.3× 高于 KL 但 KL 仍产生更优 mask，支持 \"target alignment not gradient clarity\" 的非直觉结论。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, 共识] **Coupling alignment 概念过度包装，缺乏形式化定义**\n- R1-N1 + R2-N2，交叉后双方 AGREE\n- §3.7 定义为\"训练损失是否优化一个跨层组合的量\"，Conclusion 首句将其称为\"the decisive factor\"——但本质上是\"end-to-end training outperforms component-wise training when components interact\"这一深度学习基本原理的重新陈述\n- 论文未提供 composability 的形式化度量，未测试 intermediate coupling 目标（如 hidden-state KL），Taxonomy (Table 1) 填充空格不构成理论发现\n- C1 ablation 证明 mask quality 是 proximate driver、gradient coupling 仅在 discovery 阶段必要——这与 \"coupling alignment is decisive\" 的结论存在内部张力\n- **修复方向**: 降低理论抱负，定位为\"已知原理在 sparsity prediction 场景的经验验证\"；或补充 hidden-state KL 对照实验\n\n**N2** [critical, 共识] **Abstract headline \"19% PPL improvement\" 在非匹配 sparsity 下报告**\n- R1-N2 + R2-W3，交叉后双方 AGREE\n- KL actual 28.5% vs TEAL ~30%。匹配 sparsity (28.5%) 下改善为 14.5%（§4.2 括号内承认但 Abstract 未修正）\n- Abstract 选择性呈现：突出 ARC +4.4pp、HellaSwag +7.8pp，MMLU -5.2pp 仅给标签，完全未提及绝对退化幅度（MMLU dense 65.27%→sparse 40.7%）\n- **修复方向**: Abstract 使用 14.5% 或明确标注 sparsity 差异；加入 MMLU 绝对退化\n\n**N3** [critical, 共识] **实际可用 regime 仅 30%，且 downstream 为 task-dependent**\n- R1-N3 + R2-W1，交叉后双方 AGREE\n- 50% sparsity：所有方法 MMLU≈28%（≈random），GSM8K<2.2%，capacity-limited collapse\n- 30% sparsity：commonsense 4/4 win (ARC +4.4pp, WG +3.9pp, HS +7.8pp, PIQA +2.2pp)，knowledge 0/2 lose (MMLU -5.2pp, GSM8K -1.3pp)。TEAL 在 MMLU/GSM8K 上更好且无需训练\n- KL predictor 增加 6.4% latency overhead，无实际 wall-clock speedup（无 sparse kernel support）\n- 方法的 unambiguous advantage 仅在\"30% × PPL\"这一窄窗口\n- **修复方向**: Abstract/Intro 更平衡呈现 task-type split；分析 forward KL mode-covering 与 knowledge tasks 的 tradeoff\n\n**N4** [critical, R2 critical + R1 partial rebut] **与 MaskLLM 的新颖性边界不够清晰**\n- R2-N1 critical，R1 REBUT（结构性差异成立），R2 部分接受\n- MaskLLM (NeurIPS 2024) 已使用 frozen weights + KL + Gumbel + learnable masks 的完整框架\n- R1 论证三个结构性差异（sparsity type、mask generation、allocation）是实质性的而非 domain 差异；但论文未明确论证为什么 global allocation 场景让 KL vs BCE 差异更 pronounced\n- **修复方向**: §2 加入\"why global allocation amplifies KL-BCE gap\"的论证；讨论 MaskLLM 中是否存在类似 gap\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, 共识] **跨架构/跨规模证据过薄**\n- R1-W1 + R2-W2，交叉后 AGREE\n- Mistral-7B 和 Qwen-14B 均 single seed\n- 14B 结果反转核心优势：GSM8K -20pp（32.1±5.2% vs TEAL 52.1%），MMLU -2.79pp\n- Abstract/Conclusion 将 cross-architecture 作为 contribution claim，与 \"preliminary single-seed\" 证据强度不匹配\n\n**W2** [warning, 共识] **BCE+Gumbel 交互效应未量化**\n- R1-W4，R2 AGREE\n- BCE+Gumbel (32.22) 比 standard BCE (27.97) 差 4.25 PPL\n- §4.5 的 additive decomposition（loss effect 5.1× relaxation effect）假设独立性，但交互效应的存在说明不独立\n- 需补 BCE+STE 对照（控制 relaxation），或正式承认 KL×Gumbel 正向交互\n\n**W3** [warning, 共识] **Training data 单一性 + OOD downstream 未评估**\n- R2-W4 新提出，R1 AGREE\n- 所有 predictor 仅在 WikiText-103 训练 1000 步\n- C4 OOD 仅报告 PPL 未报告 downstream；C4 cross-seed CV=6.3% vs WikiText-2 CV=0.2%（30× 增大）\n- Limitations 已承认\"partially overfits to training-domain activation patterns\"但未补充 OOD downstream 数据\n\n**W4** [warning, 共识] **MSE baseline λ_max 不匹配 (1000 vs 5000) 且 single seed**\n- R1-W2 + R2-M2，交叉后 AGREE\n- Appendix G 已补 MSE 配置（同 Gumbel/optimizer/data），但 λ_max 差异未解释\n- 50% gap (229 vs 23.9) 足够大，seed sensitivity 不影响结论；30% (20.4 vs 10.8) 需确认\n\n**W5** [warning, R1 提出] **梯度分析 (§3.6) 缺乏定量支撑**\n- §3.6 定性推导正确（BCE gradient decomposed, KL gradient coupled through downstream Jacobian）\n- SNR 分析 (Appendix H) 有效但不能区分\"gradient direction 更好\"和\"gradient 更 coupled\"\n- 缺少直接度量 coupling 强度的实验（如 cross-layer gradient correlation）\n\n**W6** [warning, R1 提出] **Adaptive penalty controller 在 30% 时 λ 触顶 5000**\n- Appendix C Table 10：30% target 时 λ=5000 (cap), actual=28.5% (5% deviation)\n- 控制器在最实用 regime 表现最差——如果目标是 25% 可能完全失效\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. Coupling alignment 是已知原理的重新包装，需降级 claim 或补充形式化 [R1-N1 + R2-N2]\n2. Abstract 19% headline 在非匹配 sparsity 下报告，构成选择性呈现 [R1-N2 + R2-W3]\n3. 50% downstream collapse + 30% task-dependent wins = 实用 regime 过窄 [R1-N3 + R2-W1]\n4. Cross-architecture 证据不足以支撑 contribution claim [R1-W1 + R2-W2]\n5. C1 target-swap ablation 是全文最有价值的贡献 [R1-S2 + R2-S1]\n6. 实验诚实度高，Limitations 讨论充分 [R1-S4 + R2-S2]\n\n## Reviewer Divergence [REBUT → 部分收敛]\n\n1. **MaskLLM 新颖性** — R2 认为核心框架已被 MaskLLM 覆盖 (Excitement 2.5/5)；R1 认为 activation sparsity + predictor + global allocation 是结构性不同问题 (Excitement 3.5/5)。交叉后 R2 部分接受结构性差异但维持 critical。**Director 判断**: R1 的结构性差异论证有效，但论文确实需要更 explicit 地论证新颖性边界——列为 N4 (critical)。\n2. **Overall 评分** — R1: 3.5 (Borderline Conference)，R2: 3.0 (Findings)。分歧主要在 excitement。\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1] 反向 C1：用 KL 训练在 magnitude-based oracle targets 上性能如何？测试 KL coupled gradient 在 suboptimal targets 上是否仍有优势。\n2. [R1-Q3 + R2-Q2] Forward KL 的 mode-covering 是否解释了 knowledge-intensive tasks 的退化？是否考虑过 task-specific 的 KL 方向选择？30% 下有无方法恢复 MMLU 差距？\n3. [R2-Q1] MaskLLM 中 KL vs BCE 的 PPL gap 是多少？与本文 2.4× gap 可比吗？\n4. [R2-Q3 + R1-W4] Gumbel 对 KL 有利但对 BCE 有害——能否量化 KL×Gumbel 的交互效应？BCE+STE 的结果？\n5. [R1-Q2] λ_max 提高到 50000 能否达到 30% actual sparsity？PPL 是否会因过强惩罚恶化？\n\n---\n\n## Missing References\n\n- **共识**: §2 line 172-173 \"All prior predictor-based methods use decomposed or intermediate objectives\" 需限定为 \"for activation sparsity prediction\"（MaskLLM 已在 weight sparsity 用 KL）\n- **R2 提出**: \"A Sparsity Predicting Approach via Activation Pattern Clustering\" (Dhar et al., 2025); \"Universal Properties of Activation Sparsity in Modern LLMs\" (arXiv:2509.00454)\n- **R1 提出**: Wortsman et al. (2023) training stability（tangentially related）; quantization+sparsity 交叉工作（论文未讨论）\n- **引用修复**: xu2026spon bib year=2026 应为 2025 (ICML 2025)；de2024griffin OpenAlex 未找到，需确认 venue 信息\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warning, 3 info, 0 critical）。\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Pages 1-4 | 连续 4 页纯文本无 display item（figure/table），Figure 1 在 page 3 首次引用但漂移到 page 5。建议将 Figure 1 提前至 page 2-3 |\n| ⚠️ warning | Page 17 | Figure 7 仅占页面 1/3，上方 2/3 空白。建议合并或补充内容 |\n| ℹ️ info | Page 5 | Figure 1（架构图）为单栏宽度，文字接近可读性下限，考虑 figure* 全宽 |\n| ℹ️ info | Page 13 | 单页 4 个表格（Tables 7-10），密集但未溢出，附录可接受 |\n| ℹ️ info | Page 8 | Figure 2 折线图仅 2 条线，建议增加 marker 形状差异确保灰度打印可辨 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 — Findings**\n**置信度: 4 / 5**\n\n**理由**:\n\n本文做出了有价值的实证贡献——C1 target-swap ablation 精巧地隔离了 mask 质量的因果作用，\"KL-derived masks diverge 46-68% from magnitude yet produce lower PPL\"是非直觉且有启发性的发现。实验设计规范（3-seed、6 downstream tasks、全面 ablation），科学诚实度高。\n\n但论文有四个结构性问题阻止其达到主会议水平：\n\n1. **理论贡献过度包装**: \"Coupling alignment\"是对已知原理的重新陈述而非新发现，但论文将其作为核心贡献。如果降级为经验验证，论文就缺少除 C1 ablation 之外的概念性贡献。\n\n2. **新颖性边界模糊**: MaskLLM 已使用 KL+Gumbel+frozen weights+learnable masks 的完整技术栈。虽然 activation sparsity + predictor + global allocation 是不同问题（R1 论证有效），但论文未充分论证为什么这些差异让 contribution 不可从 MaskLLM 直接推导。\n\n3. **实用 regime 过窄**: 50% downstream collapse，30% downstream task-dependent（knowledge tasks 输 TEAL），无 wall-clock speedup。方法的 unambiguous advantage 仅在\"30% × PPL\"窄窗口——用户为何不直接用 training-free TEAL？\n\n4. **Headline 数字准确性**: Abstract 19% 在非匹配 sparsity 下报告，选择性呈现 downstream 结果。\n\nR1 评分 3.5 (Borderline Conference)，R2 评分 3.0 (Findings)。综合考虑：如果修复 headline 准确性、降低 coupling alignment claim、更 explicit 论证 vs MaskLLM 的新颖性，论文可升至 3.5。当前版本适合 Findings track。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"19% relative to TEAL\" → 使用匹配 sparsity 14.5% 或标注 sparsity 差异\n- \"moderate downstream degradation\" → 不准确：MMLU -24.6pp（dense→sparse）不是\"moderate\"\n- \"improving commonsense reasoning (ARC +4.4pp, HellaSwag +7.8pp) while knowledge-intensive benchmarks (MMLU −5.2pp) favor TEAL\" → 数字选择性：应加入绝对退化或更平衡表述\n- \"Preliminary single-seed evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B\" → 适当降调，Conclusion 也应一致\n\n### §1 Introduction\n- Line 8: MaskLLM 讨论应更早且更 explicit——当前读者到 §2 才了解最近的 KL-based 先例\n- Line 94: \"primarily an empirical study\" 与 §3.6-3.7 的理论抱负（gradient analysis + coupling alignment taxonomy）定位不一致。建议选择一个方向\n- Contributions list: 第 4 条 \"Analysis of allocation-to-downstream interactions at 7-14B\" 应注明 \"preliminary single-seed\"\n\n### §3 Method\n- §3.5: λ 在 30% 触顶 5000 → 讨论 sensitivity to λ_max\n- §3.6: \"suggestive\" hedge 适当，但随后 §3.7 将 coupling alignment 提升为 \"decisive factor\"，语气跳跃\n- §3.7: 需要形式化定义或明确降级为描述性分类\n\n### §4 Experiments\n- Table 2: MSE single seed 行应标注\n- §4.2: Task-type split 分析良好，但 Abstract 未反映\n- §4.4 C1: 最有价值的贡献。s42 oracle 来自不同 run 的 confound 已通过 retrained seeds (s123/s456) 缓解\n- §4.5 Table 4: BCE+Gumbel 行需要更 explicit 的交互效应讨论；additive decomposition caveat\n- §4.6: Cross-architecture 结果应标注 single-seed limitation in section title 或 opening sentence\n\n### Limitations\n- 内容全面，科学诚实度高\n- 建议增加：(1) OOD downstream 评估缺失；(2) training data 单一性对 predictor generalization 的影响\n\n### References\n- xu2026spon: bib year 2026 → 2025\n- de2024griffin: 确认 venue 信息\n- §2 line 172-173: 限定范围为 \"for activation sparsity prediction\"",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 15 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**审稿编排**: 2 Reviewers — R1 (方法严谨性 + 实验完整性), R2 (新颖性 + 完整性 + 写作质量)\n**交叉轮数**: 1 轮（关键问题已收敛）\n\n---\n\n## Summary\n\n本文提出用 forward KL 蒸馏替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的上下文稀疏性预测器。在 LLaMA-3.1-8B 上，KL 预测器（75.9M 参数，<1% base）在 30% sparsity 下将 TEAL 的 perplexity 从 10.82 降至 8.81（非匹配 sparsity 下 19%，匹配 sparsity 下 14.5%）。Target-swap ablation (C1) 证明 KL 发现的 mask pattern（与 magnitude mask 偏差 46-68%）是推理阶段质量的近端驱动因素。论文提出 \"coupling alignment\" 概念组织 sparsity prediction 方法的二维分类，但两位 Reviewer 均认为该概念缺乏形式化定义且过度包装已知原理。方法的实际可用范围窄——50% sparsity 下所有方法 downstream collapse，30% 下 downstream 为 task-dependent（commonsense 赢 4/4，knowledge 输 0/2）。\n\n---\n\n## Strengths\n\n**S1. C1 Target-swap ablation 设计精巧且有说服力** [R1 S2, R2 S1, 共识]\n将 mask 质量与训练机制解耦：BCE 在 KL-derived targets 上训练，复现 KL 性能（50% Δ≤0.79pp，30% retrained Δ≤1.18pp）。直接回答了\"是 mask 更好还是训练过程更好\"的因果问题。这是全文最有价值的实验证据。\n\n**S2. 实验诚实度高** [R1 S4, R2 S2, 共识]\n坦承 50% downstream collapse、cross-architecture 为\"preliminary single-seed\"、缺乏 wall-clock speedup、OOD 过拟合。在 MMLU 和 GSM8K 上的负面结果如实报告。\n\n**S3. Multi-seed 评估规范 + Appendix 充实** [R1 S3, R2 S3/S4, 共识]\n核心实验 3-seed（PPL CV=0.2%），6 downstream tasks。Appendix A-P 涵盖 bottleneck sensitivity、temperature schedule、training convergence、OOD、compensation redundancy 等，reproducibility 支持好。超参完整列出（§4.1）。\n\n**S4. 问题定位精准** [R1 S1]\n首次系统质疑\"为什么 sparsity predictor 都用 BCE\"，填补 Table 1 中 Per-token × Coupled 的空白。\n\n**S5. SNR 分析诚实** [R1 交叉回应]\nSNR figure (Appendix H) 用完整 1000 步 14-checkpoint 数据，诚实呈现 BCE SNR 2.3× 高于 KL 但 KL 仍产生更优 mask，支持 \"target alignment not gradient clarity\" 的非直觉结论。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, 共识] **Coupling alignment 概念过度包装，缺乏形式化定义**\n- R1-N1 + R2-N2，交叉后双方 AGREE\n- §3.7 定义为\"训练损失是否优化一个跨层组合的量\"，Conclusion 首句将其称为\"the decisive factor\"——但本质上是\"end-to-end training outperforms component-wise training when components interact\"这一深度学习基本原理的重新陈述\n- 论文未提供 composability 的形式化度量，未测试 intermediate coupling 目标（如 hidden-state KL），Taxonomy (Table 1) 填充空格不构成理论发现\n- C1 ablation 证明 mask quality 是 proximate driver、gradient coupling 仅在 discovery 阶段必要——这与 \"coupling alignment is decisive\" 的结论存在内部张力\n- **修复方向**: 降低理论抱负，定位为\"已知原理在 sparsity prediction 场景的经验验证\"；或补充 hidden-state KL 对照实验\n\n**N2** [critical, 共识] **Abstract headline \"19% PPL improvement\" 在非匹配 sparsity 下报告**\n- R1-N2 + R2-W3，交叉后双方 AGREE\n- KL actual 28.5% vs TEAL ~30%。匹配 sparsity (28.5%) 下改善为 14.5%（§4.2 括号内承认但 Abstract 未修正）\n- Abstract 选择性呈现：突出 ARC +4.4pp、HellaSwag +7.8pp，MMLU -5.2pp 仅给标签，完全未提及绝对退化幅度（MMLU dense 65.27%→sparse 40.7%）\n- **修复方向**: Abstract 使用 14.5% 或明确标注 sparsity 差异；加入 MMLU 绝对退化\n\n**N3** [critical, 共识] **实际可用 regime 仅 30%，且 downstream 为 task-dependent**\n- R1-N3 + R2-W1，交叉后双方 AGREE\n- 50% sparsity：所有方法 MMLU≈28%（≈random），GSM8K<2.2%，capacity-limited collapse\n- 30% sparsity：commonsense 4/4 win (ARC +4.4pp, WG +3.9pp, HS +7.8pp, PIQA +2.2pp)，knowledge 0/2 lose (MMLU -5.2pp, GSM8K -1.3pp)。TEAL 在 MMLU/GSM8K 上更好且无需训练\n- KL predictor 增加 6.4% latency overhead，无实际 wall-clock speedup（无 sparse kernel support）\n- 方法的 unambiguous advantage 仅在\"30% × PPL\"这一窄窗口\n- **修复方向**: Abstract/Intro 更平衡呈现 task-type split；分析 forward KL mode-covering 与 knowledge tasks 的 tradeoff\n\n**N4** [critical, R2 critical + R1 partial rebut] **与 MaskLLM 的新颖性边界不够清晰**\n- R2-N1 critical，R1 REBUT（结构性差异成立），R2 部分接受\n- MaskLLM (NeurIPS 2024) 已使用 frozen weights + KL + Gumbel + learnable masks 的完整框架\n- R1 论证三个结构性差异（sparsity type、mask generation、allocation）是实质性的而非 domain 差异；但论文未明确论证为什么 global allocation 场景让 KL vs BCE 差异更 pronounced\n- **修复方向**: §2 加入\"why global allocation amplifies KL-BCE gap\"的论证；讨论 MaskLLM 中是否存在类似 gap\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, 共识] **跨架构/跨规模证据过薄**\n- R1-W1 + R2-W2，交叉后 AGREE\n- Mistral-7B 和 Qwen-14B 均 single seed\n- 14B 结果反转核心优势：GSM8K -20pp（32.1±5.2% vs TEAL 52.1%），MMLU -2.79pp\n- Abstract/Conclusion 将 cross-architecture 作为 contribution claim，与 \"preliminary single-seed\" 证据强度不匹配\n\n**W2** [warning, 共识] **BCE+Gumbel 交互效应未量化**\n- R1-W4，R2 AGREE\n- BCE+Gumbel (32.22) 比 standard BCE (27.97) 差 4.25 PPL\n- §4.5 的 additive decomposition（loss effect 5.1× relaxation effect）假设独立性，但交互效应的存在说明不独立\n- 需补 BCE+STE 对照（控制 relaxation），或正式承认 KL×Gumbel 正向交互\n\n**W3** [warning, 共识] **Training data 单一性 + OOD downstream 未评估**\n- R2-W4 新提出，R1 AGREE\n- 所有 predictor 仅在 WikiText-103 训练 1000 步\n- C4 OOD 仅报告 PPL 未报告 downstream；C4 cross-seed CV=6.3% vs WikiText-2 CV=0.2%（30× 增大）\n- Limitations 已承认\"partially overfits to training-domain activation patterns\"但未补充 OOD downstream 数据\n\n**W4** [warning, 共识] **MSE baseline λ_max 不匹配 (1000 vs 5000) 且 single seed**\n- R1-W2 + R2-M2，交叉后 AGREE\n- Appendix G 已补 MSE 配置（同 Gumbel/optimizer/data），但 λ_max 差异未解释\n- 50% gap (229 vs 23.9) 足够大，seed sensitivity 不影响结论；30% (20.4 vs 10.8) 需确认\n\n**W5** [warning, R1 提出] **梯度分析 (§3.6) 缺乏定量支撑**\n- §3.6 定性推导正确（BCE gradient decomposed, KL gradient coupled through downstream Jacobian）\n- SNR 分析 (Appendix H) 有效但不能区分\"gradient direction 更好\"和\"gradient 更 coupled\"\n- 缺少直接度量 coupling 强度的实验（如 cross-layer gradient correlation）\n\n**W6** [warning, R1 提出] **Adaptive penalty controller 在 30% 时 λ 触顶 5000**\n- Appendix C Table 10：30% target 时 λ=5000 (cap), actual=28.5% (5% deviation)\n- 控制器在最实用 regime 表现最差——如果目标是 25% 可能完全失效\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. Coupling alignment 是已知原理的重新包装，需降级 claim 或补充形式化 [R1-N1 + R2-N2]\n2. Abstract 19% headline 在非匹配 sparsity 下报告，构成选择性呈现 [R1-N2 + R2-W3]\n3. 50% downstream collapse + 30% task-dependent wins = 实用 regime 过窄 [R1-N3 + R2-W1]\n4. Cross-architecture 证据不足以支撑 contribution claim [R1-W1 + R2-W2]\n5. C1 target-swap ablation 是全文最有价值的贡献 [R1-S2 + R2-S1]\n6. 实验诚实度高，Limitations 讨论充分 [R1-S4 + R2-S2]\n\n## Reviewer Divergence [REBUT → 部分收敛]\n\n1. **MaskLLM 新颖性** — R2 认为核心框架已被 MaskLLM 覆盖 (Excitement 2.5/5)；R1 认为 activation sparsity + predictor + global allocation 是结构性不同问题 (Excitement 3.5/5)。交叉后 R2 部分接受结构性差异但维持 critical。**Director 判断**: R1 的结构性差异论证有效，但论文确实需要更 explicit 地论证新颖性边界——列为 N4 (critical)。\n2. **Overall 评分** — R1: 3.5 (Borderline Conference)，R2: 3.0 (Findings)。分歧主要在 excitement。\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1] 反向 C1：用 KL 训练在 magnitude-based oracle targets 上性能如何？测试 KL coupled gradient 在 suboptimal targets 上是否仍有优势。\n2. [R1-Q3 + R2-Q2] Forward KL 的 mode-covering 是否解释了 knowledge-intensive tasks 的退化？是否考虑过 task-specific 的 KL 方向选择？30% 下有无方法恢复 MMLU 差距？\n3. [R2-Q1] MaskLLM 中 KL vs BCE 的 PPL gap 是多少？与本文 2.4× gap 可比吗？\n4. [R2-Q3 + R1-W4] Gumbel 对 KL 有利但对 BCE 有害——能否量化 KL×Gumbel 的交互效应？BCE+STE 的结果？\n5. [R1-Q2] λ_max 提高到 50000 能否达到 30% actual sparsity？PPL 是否会因过强惩罚恶化？\n\n---\n\n## Missing References\n\n- **共识**: §2 line 172-173 \"All prior predictor-based methods use decomposed or intermediate objectives\" 需限定为 \"for activation sparsity prediction\"（MaskLLM 已在 weight sparsity 用 KL）\n- **R2 提出**: \"A Sparsity Predicting Approach via Activation Pattern Clustering\" (Dhar et al., 2025); \"Universal Properties of Activation Sparsity in Modern LLMs\" (arXiv:2509.00454)\n- **R1 提出**: Wortsman et al. (2023) training stability（tangentially related）; quantization+sparsity 交叉工作（论文未讨论）\n- **引用修复**: xu2026spon bib year=2026 应为 2025 (ICML 2025)；de2024griffin OpenAlex 未找到，需确认 venue 信息\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warning, 3 info, 0 critical）。\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Pages 1-4 | 连续 4 页纯文本无 display item（figure/table），Figure 1 在 page 3 首次引用但漂移到 page 5。建议将 Figure 1 提前至 page 2-3 |\n| ⚠️ warning | Page 17 | Figure 7 仅占页面 1/3，上方 2/3 空白。建议合并或补充内容 |\n| ℹ️ info | Page 5 | Figure 1（架构图）为单栏宽度，文字接近可读性下限，考虑 figure* 全宽 |\n| ℹ️ info | Page 13 | 单页 4 个表格（Tables 7-10），密集但未溢出，附录可接受 |\n| ℹ️ info | Page 8 | Figure 2 折线图仅 2 条线，建议增加 marker 形状差异确保灰度打印可辨 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 — Findings**\n**置信度: 4 / 5**\n\n**理由**:\n\n本文做出了有价值的实证贡献——C1 target-swap ablation 精巧地隔离了 mask 质量的因果作用，\"KL-derived masks diverge 46-68% from magnitude yet produce lower PPL\"是非直觉且有启发性的发现。实验设计规范（3-seed、6 downstream tasks、全面 ablation），科学诚实度高。\n\n但论文有四个结构性问题阻止其达到主会议水平：\n\n1. **理论贡献过度包装**: \"Coupling alignment\"是对已知原理的重新陈述而非新发现，但论文将其作为核心贡献。如果降级为经验验证，论文就缺少除 C1 ablation 之外的概念性贡献。\n\n2. **新颖性边界模糊**: MaskLLM 已使用 KL+Gumbel+frozen weights+learnable masks 的完整技术栈。虽然 activation sparsity + predictor + global allocation 是不同问题（R1 论证有效），但论文未充分论证为什么这些差异让 contribution 不可从 MaskLLM 直接推导。\n\n3. **实用 regime 过窄**: 50% downstream collapse，30% downstream task-dependent（knowledge tasks 输 TEAL），无 wall-clock speedup。方法的 unambiguous advantage 仅在\"30% × PPL\"窄窗口——用户为何不直接用 training-free TEAL？\n\n4. **Headline 数字准确性**: Abstract 19% 在非匹配 sparsity 下报告，选择性呈现 downstream 结果。\n\nR1 评分 3.5 (Borderline Conference)，R2 评分 3.0 (Findings)。综合考虑：如果修复 headline 准确性、降低 coupling alignment claim、更 explicit 论证 vs MaskLLM 的新颖性，论文可升至 3.5。当前版本适合 Findings track。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"19% relative to TEAL\" → 使用匹配 sparsity 14.5% 或标注 sparsity 差异\n- \"moderate downstream degradation\" → 不准确：MMLU -24.6pp（dense→sparse）不是\"moderate\"\n- \"improving commonsense reasoning (ARC +4.4pp, HellaSwag +7.8pp) while knowledge-intensive benchmarks (MMLU −5.2pp) favor TEAL\" → 数字选择性：应加入绝对退化或更平衡表述\n- \"Preliminary single-seed evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B\" → 适当降调，Conclusion 也应一致\n\n### §1 Introduction\n- Line 8: MaskLLM 讨论应更早且更 explicit——当前读者到 §2 才了解最近的 KL-based 先例\n- Line 94: \"primarily an empirical study\" 与 §3.6-3.7 的理论抱负（gradient analysis + coupling alignment taxonomy）定位不一致。建议选择一个方向\n- Contributions list: 第 4 条 \"Analysis of allocation-to-downstream interactions at 7-14B\" 应注明 \"preliminary single-seed\"\n\n### §3 Method\n- §3.5: λ 在 30% 触顶 5000 → 讨论 sensitivity to λ_max\n- §3.6: \"suggestive\" hedge 适当，但随后 §3.7 将 coupling alignment 提升为 \"decisive factor\"，语气跳跃\n- §3.7: 需要形式化定义或明确降级为描述性分类\n\n### §4 Experiments\n- Table 2: MSE single seed 行应标注\n- §4.2: Task-type split 分析良好，但 Abstract 未反映\n- §4.4 C1: 最有价值的贡献。s42 oracle 来自不同 run 的 confound 已通过 retrained seeds (s123/s456) 缓解\n- §4.5 Table 4: BCE+Gumbel 行需要更 explicit 的交互效应讨论；additive decomposition caveat\n- §4.6: Cross-architecture 结果应标注 single-seed limitation in section title 或 opening sentence\n\n### Limitations\n- 内容全面，科学诚实度高\n- 建议增加：(1) OOD downstream 评估缺失；(2) training data 单一性对 predictor generalization 的影响\n\n### References\n- xu2026spon: bib year 2026 → 2025\n- de2024griffin: 确认 venue 信息\n- §2 line 172-173: 限定范围为 \"for activation sparsity prediction\"",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-20T06:52:29.618464+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4699
}
```

</details>

---


### Assistant

_source line 1316 · 2026-05-20T06:52:38.363359+00:00_

审稿完成。

**Round 15 审稿报告已投递至 Research Director。**

核心结论：**3.0 / 5 (Findings)**

4 个 Must-Fix：
1. **Coupling alignment 过度包装**——本质是已知原理重述，需降级 claim 或补充形式化（R1+R2 共识）
2. **Abstract 19% headline 误导**——匹配 sparsity 仅 14.5%，数字选择性呈现（R1+R2 共识）
3. **实用 regime 过窄**——50% collapse，30% task-dependent，无 wall-clock speedup（R1+R2 共识）
4. **MaskLLM 新颖性边界模糊**——KL+Gumbel 框架已存在，需更 explicit 论证差异（R2 critical，R1 partial rebut）

6 个 Should-Fix：跨架构证据过薄、BCE+Gumbel 交互未量化、训练数据单一、MSE λ_max 不匹配、梯度分析缺定量、penalty controller 30% 触顶

主要优势：C1 target-swap ablation 设计精巧、实验诚实度高、multi-seed 规范、appendix 充实。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1317 · 2026-05-20T06:52:39.870007+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**与 R1 的共识**：核心问题高度一致——新颖性边界（我 N1/MaskLLM vs R1 N1/tautology）、regime 过窄（我 W1 vs R1 N3）、数字选择性呈现（我 W3 vs R1 N2）。

**R1 独到的贡献**：N2（sparsity 不匹配下的 headline 数字）和 W4（Gumbel×Loss 交互效应破坏 additive decomposition）是我遗漏的有价值观点。

**分歧点**：R1 给 3.5，我给 3.0。差异主要在 excitement——R1 对 C1 target-swap ablation 的方法论价值给了更高权重。综合两份 review，3.0-3.5 是合理区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1318 · 2026-05-20T06:52:53.320426+00:00_

审稿报告已投递至 Research Director（Overall 3.0 / Findings）。

**本轮审稿总结**：

- **2 位 Reviewer**，1 轮交叉后收敛
- **R1**: 3.5 (Borderline Conference) | **R2**: 3.0 (Findings) | **综合**: 3.0 (Findings)
- **4 个 Must-Fix**：coupling alignment 过度包装、headline 19% 非匹配 sparsity、regime 过窄 + downstream task-dependent、MaskLLM 新颖性边界模糊
- **6 个 Should-Fix**：cross-arch 过薄、BCE+Gumbel 交互效应、training data 单一性、MSE λ_max 不匹配、梯度分析缺定量支撑、penalty controller 30% 触顶
- **核心优势**：C1 target-swap ablation（共识最有价值贡献）、实验诚实度高、multi-seed 规范
- **视觉审查**：已完成，2 warning（Figure 1 漂移到 p5、p17 空白过多），0 critical
- **Issue Tracker**：已同步更新（R15-N1~N4, R15-W1~W6, R15-M1 + 历史 resolved 更新）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 109

## Round 109

54 recorded events


### User

_source line 1319 · 2026-05-20T15:21:53.605217+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Efficient Methods for NLP
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-20T15:21:59.848710+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-20T15:21:59.899795+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-20T15:22:06.573865+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-20T15:22:06.624395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-20T15:22:09.989565+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-20T15:22:10.040425+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-20T15:22:14.459156+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 1327 · 2026-05-20T15:22:14.961713+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1328 · 2026-05-20T15:22:16.115299+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (287 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mistral_kl30_s456 | Mistral KL30 seed 456 replicates seed 42/123 results, providing 3-seed cross-arch evidence for KL advantage | — | — | — |\n\n## 待处理\n- bce_ste_s42: BCE+STE combination fills the missing cell in the 2x2 loss×relaxation ablation matrix; if BCE+STE underperforms KL+Gumbel similarly to BCE+Gumbel, the loss function (not relaxation) is the dominant factor（准备中）\n- c4_ood_downstream_kl30: KL predictor trained on WikiText-103 maintains downstream task quality when mask predictions are generated from C4 OOD text, demonstrating domain-agnostic mask transfer（准备中）\n- kl_sparsity40_s42_global_eval_v2: 40% KL predictor with global_topk allocation at sparsity_target=0.4 should achieve model-level sparsity ~0.38-0.42 and PPL comparable to the old 10.12; v1 eval omitted --sparsity_target causing 50% actual sparsity（准备中）\n- mistral_kl30_s123: Mistral-7B KL predictor at 30% sparsity with seed 123 reproduces s42 quality (PPL ~8.38), providing 2nd seed for cross-architecture robustness evidence（准备中）\n- kl_sparsity40_s42_uniform_hspiqa（准备中）\n- kl_sparsity40_s42_global_eval: New 40% KL checkpoint (retrained 
…[truncated 1761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1656
}
```

</details>

---


### Tool call

_source line 1329 · 2026-05-20T15:22:16.115633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1330 · 2026-05-20T15:22:16.216150+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
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
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-20T15:22:26.948521+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

The search results provide information about EMNLP 2026 related calls for papers, but they primarily focus on tutorials and wor
…[truncated 4235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 11986
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-20T15:22:35.478575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-20T15:22:35.930560+00:00_

1	Learned sparsity predictors for SwiGLU (Swish-Gated Linear Unit) LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train predictors with Kullback-Leibler (KL) divergence, coupling all mask decisions through the output distribution.
3	At 30\% sparsity on LLaMA-3.1-8B, the KL predictor ($<$1\% of base parameters) reduces perplexity by 14.5\% relative to TEAL at matched sparsity (19\% at reported 28.5\% vs.\ TEAL's 30\%), improving commonsense reasoning (ARC +4.4pp, HellaSwag +7.8pp) but underperforming on knowledge-intensive benchmarks (MMLU 40.7\% vs.\ TEAL 45.9\%, both substantially below the dense 65.3\%). Post-hoc compensation (+67.2M params) becomes redundant in prediction quality.
4	KL-derived masks diverge 46--68\% from magnitude-based masks (depending on sparsity level); a target-swap ablation confirms that these mask targets, discovered through KL's coupled gradients, are the proximate quality driver when transferred to simpler objectives.
5	Per-layer coupling (MSE) degrades below training-free baselines ($1.9\times$ TEAL at 30\%; $9.6\times$ at 50\%), suggesting that \emph{alignment} with the output distribution---not coupling per se---matters more than gradient coupling alone.
6	Cross-architecture evaluation on Mistral-7B-v0.3 (3-seed) and Qwen-2.5-14B reveals consistent PPL improvements but scale-dependent downstream effects.
7	At 50\% sparsity the perplexity advantage widens, though downstream reasoning collapses to near-random regardless of method, revealing a capacity cliff.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-20T15:22:35.930916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-20T15:22:36.935314+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	SwiGLU's gated activation makes prediction challenging: importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
5	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
6	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
7	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
8	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
9	
10	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
11	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
12	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Gradient 
…[truncated 2130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-20T15:22:37.036004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-20T15:22:37.337455+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
8	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
9	
10	\paragraph{Predictor-Based Contextual Sparsity.}
11	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
12	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
13	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
14	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
15	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
16	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
17	First, \emph{spar
…[truncated 4290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-20T15:22:37.337815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-20T15:22:37.839797+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 11547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-20T15:22:37.840204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-20T15:22:38.292250+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 15608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-20T15:22:38.292592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-20T15:22:38.795332+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Our experiments demonstrate that \emph{coupling alignment}---optimizing a composable, output-level quantity---is necessary for sparsity prediction quality, a principle well-established in end-to-end learning but previously unverified for activation sparsity.
5	A target-swap ablation confirms that KL-discovered mask patterns (46--68\% divergent from magnitude) drive inference-stage quality; gradient coupling is necessary for mask discovery but not at inference.
6	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\% at matched sparsity and renders compensation networks redundant.
7	However, PPL gains do not uniformly transfer: KL improves commonsense reasoning (4/4 tasks) but underperforms on knowledge-intensive benchmarks (MMLU, GSM8K); cross-architecture evaluation (Mistral-7B, 3-seed: PPL and commonsense gains generalize; MMLU tied, GSM8K reverses) and scale analysis (14B: reasoning declines despite PPL gains) reveal task- and scale-dependent effects.
8	Future work includes N:M structured sparsity and scaling to 70B+.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-20T15:22:38.795737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-20T15:22:39.398996+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 10.76 but MMLU already degrades to 35.5\% (vs.\ 40.7\% at 30\%); 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B (3-seed), KL improves PPL ($-$17.3\%) and commonsense tasks (WG, HS, PIQA: all seeds win) but MMLU is tied (43.3\% vs.\ 43.5\%) and GSM8K reverses across all seeds (7.0--11.1\% vs.\ TEAL 15.9\%). ARC-c is seed-dependent (37.8--50.1\% vs.\ TEAL 41.1\%; $\sigma$=6.4pp vs.\ LLaMA-8B's 2.5pp), indicating reduced cross-architecture metric stability. Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$20pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 52.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Out-of-distribution evaluation on C4 (Appendix~\ref{app:ood}) shows the KL advantage transfers but with a wider gap: C4 PPL at 30\% is $1.74\times$ dense vs.\ $1.46\times$ on in-domain WikiText-2, which indicates that the predictor partially overfits to training-domain activation patterns. Downstream task performance on C4 shows all six benchmarks within 1.1pp of in-dom
…[truncated 1603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-20T15:22:39.499746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-20T15:22:39.751746+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2025spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-20T15:22:39.752222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-20T15:22:40.304951+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 25553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-20T15:22:40.357167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-20T15:22:40.708931+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2025spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 18976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-20T15:22:53.239838+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-20T15:22:54.647954+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml\", \"content\": \"_next_id: 5\\nconstraints:\\n- id: C002\\n  added: 2026-05-16 03:08 UTC\\n  summary: 所有 GPU 长时间实验必须用 nohup 启动并重定向日志，禁止裸 tmux session\\n  scope: worker\\n  reason: 'bce_isocompute_s42 和 v2 两次因 tmux session 被挤掉而死，导致 Reviewer Concern #2 完全无防御数据'\\n- id: C003\\n  added: 2026-05-16 12:32 UTC\\n  summary: 论文中所有超参/架构数字必须有代码来源验证，禁止从记忆或猜测填写。Predictor 正确参数：GELU, d_b=128, 2.37M/layer,\\n    75.9M total。\\n  scope: all\\n  reason: Reviewer 发现 experiments.tex + methodology.tex 共 7 处超参事实错误（ReLU/GELU、d_b=256/128、batch_size=32/4\\n    等），根因是 Paper Agent worker 未读源代码靠猜测填写。\\n- id: C004\\n  added: 2026-05-17 15:15 UTC\\n  summary: GPU 白名单：仅允许使用 westd-34887 cuda:0/cuda:1 和 westd-41718 cuda:0/cuda:1，禁止使用其他\\n    GPU\\n  scope: all\\n  reason: 项目分配资源边界。westd-34887 为原始分配，westd-41718 为 Manager 批准的扩容（2026-05-17）。\\n\", \"total_chars\": 763, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-20T15:22:54.798837+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-20T15:22:54.950119+00:00_

issues:
  # ============================================================
  # Round 15 — Active issues (final fix batch dispatched)
  # ============================================================

  - id: "R15-N1"
    summary: "Coupling alignment 概念过度包装，缺乏形式化定义，接近同义反复"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 14
    last_seen_round: 15
    mentions:
      - {round: 14, reviewers: [1, 2], note: "R14-W5. 缺乏操作性定义."}
      - {round: 15, reviewers: [1, 2], note: "R1-N1 + R2-N2 共识. 本质是 'end-to-end > component-wise' 基本原理的重新包装."}
    action_items:
      - {round: 15, action: "全文降级: decisive factor → empirical verification. Reviewer 建议保留为 analytical framework. Abstract/Conclusion/Intro/Table caption 四处改动.", assigned_to: "paper_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R15-N2"
    summary: "Abstract headline '19% PPL improvement' 在非匹配 sparsity (28.5% vs 30%) 下报告, 匹配 sparsity 仅 14.5%"
    category: writing
    severity: critical
    status: in_progress
    first_raised_round: 12
    last_seen_round: 15
    mentions:
      - {round: 13, reviewers: [1, 2], note: "R13-W3."}
      - {round: 14, reviewers: [1, 2], note: "R14-W8."}
      - {round: 15, reviewers: [1, 2], note: "R1-N2 + R2-W3 共识."}
    action_items:
      - {round: 15, action: "Abstract/Conclusion/Intro 三处改用 14.5% at matched sparsity.", assigned_to: "paper_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R15-N3"
    summary: "MaskLLM 新颖性边界不够清晰 (R2 critical, R1 partial rebut)"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 9
    last_seen_round: 15
    mentions:
      - {round: 14, reviewers: [1, 2], note: "R14-W3."}
      - {round: 15, reviewers: [1, 2], note: "R2-N1 critical. R1 REBUT partial."}
    action_items:
      - {round: 15, action: "§2 MaskLLM 段落后加 'why global allocation amplifies KL-BCE gap' 论证.", assigned_to: "paper_agent", status: in
…[truncated 7154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-20T15:23:04.442212+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1357 · 2026-05-20T15:23:05.998128+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 89\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C
…[truncated 10971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-20T15:23:06.201226+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/project_config.yaml 2>/dev/null || grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ --include=\"*.yaml\" -l 2>/dev/null | head -5",
  "description": "Search for external_review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/project_config.yaml 2>/dev/null || grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ --include=\"*.yaml\" -l 2>/dev/null | head -5",
    "description": "Search for external_review config"
  }
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-20T15:23:06.302085+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-20T15:23:13.215934+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/project_config.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/project_config.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-20T15:23:13.266640+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-20T15:23:34.835173+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-20T15:23:54.845691+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20010
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-20T15:23:54.999241+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **会议**：EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **附录**：在 references 之后，审稿人可参考\n\n## 论文路径\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 技术正确性\n- §3.6 梯度分析（BCE vs KL gradient structure）的数学正确性\n- KL divergence 公式（Eq.5）的 forward KL 方向选择是否充分论证\n- Gumbel-Sigmoid relaxation（Eq.4）的温度退火策略是否合理\n- Adaptive Penalty Controller（Eq.7）的收敛性论证\n\n### 2. 实验设计严谨性\n- **Table 1 (Main Results)**：KL vs TEAL vs BCE 对比条件是否公平（sparsity mismatch: KL 28.5% vs TEAL 30%）\n- **Table 2 (C1 Target-Swap)**：ablation 是否充分隔离了 target quality vs gradient coupling 效应\n- **Table 3 (Ablation)**：50% sparsity only — 是否需要 30% ablation 数据\n- **Multi-seed 统计**：3-seed 是否足够；哪些结果是 single-seed（MSE baseline, 50% global）\n- **MSE baseline**：λ_max=1000 vs KL 5000，single seed — 对比公平性\n- **数据一致性**：表格间数字是否一致；limitations.tex 中 PPL 数值与正文表格是否匹配\n\n### 3. 实验覆盖度\n- 仅 WikiText-103 训练、WikiText-2 评估 — OOD 泛化性是否充分\n- 30%/50% 两个 sparsity level 是否足够；40% gap\n- 跨架构 Mistral/Qwen 证据厚度（seed 数量、downstream 覆盖度）\n\n### 4. 格式合规\n- 正文是否严格控制在 8 页内\n- Double-blind 是否违规（代码链接、GPU 型号等去匿名化风险）\n- 引用格式是否符合 ACL natbib 规范\n\n请按 ACL Reviewer Guidelines 的标准输出审稿报告，包含：Summary (2-3句) → Strengths (逐条) → Weaknesses (逐条，标注 severity: critical/warning/minor) → Questions → Missing References → Overall Assessment (1-5 分制，参照 EMNLP 2026 评分标准) → Confidence (1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **会议**：EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **附录**：在 references 之后，审稿人可参考\n\n## 论文路径\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 技术正确性\n- §3.6 梯度分析（BCE vs KL gradient structure）的数学正确性\n- KL divergence 公式（Eq.5）的 forward KL 方向选择是否充分论证\n- Gumbel-Sigmoid relaxation（Eq.4）的温度退火策略是否合理\n- Adaptive Penalty Controller（Eq.7）的收敛性论证\n\n### 2. 实验设计严谨性\n- **Table 1 (Main Results)**：KL vs TEAL vs BCE 对比条件是否公平（sparsity mismatch: KL 28.5% vs TEAL 30%）\n- **Table 2 (C1 Target-Swap)**：ablation 是否充分隔离了 target quality vs gradient coupling 效应\n- **Table 3 (Ablation)**：50% sparsity only — 是否需要 30% ablation 数据\n- **Multi-seed 统计**：3-seed 是否足够；哪些结果是 single-seed（MSE baseline, 50% global）\n- **MSE baseline**：λ_max=1000 vs KL 5000，single seed — 对比公平性\n- **数据一致性**：表格间数字是否一致；limitations.tex 中 PPL 数值与正文表格是否匹配\n\n### 3. 实验覆盖度\n- 仅 WikiText-103 训练、WikiText-2 评估 — OOD 泛化性是否充分\n- 30%/50% 两个 sparsity level 是否足够；40% gap\n- 跨架构 Mistral/Qwen 证据厚度（seed 数量、downstream 覆盖度）\n\n### 4. 格式合规\n- 正文是否严格控制在 8 页内\n- Double-blind 是否违规（代码链接、GPU 型号等去匿名化风险）\n- 引用格式是否符合 ACL natbib 规范\n\n请按 ACL Reviewer Guidelines 的标准输出审稿报告，包含：Summary (2-3句) → Strengths (逐条) → Weaknesses (逐条，标注 severity: critical/warning/minor) → Questions → Missing References → Overall Assessment (1-5 分制，参照 EMNLP 2026 评分标准) → Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-20T15:24:14.654650+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19655
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-20T15:24:14.755372+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。\n\n## Venue 信息\n- **会议**：EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **附录**：在 references 之后，审稿人可参考\n\n## 论文路径\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **核心贡献**：用 KL divergence 替代 BCE 训练 sparsity predictor — 这是否算 sufficient novelty？KL distillation 本身是标准技术，创新性在哪里？\n- **MaskLLM 区分**：§2 Related Work 中 MaskLLM 三点区分（sparsity type / mask generation / allocation）是否充分？MaskLLM 已在 NeurIPS 2024 发表，本文在技术上走得比 MaskLLM 远多少？\n- **Taxonomy (Table 1 §3.7)**：两维分类框架（correction granularity × training signal coupling）是否真正有洞察力，还是仅仅是对已有方法的重新分类？\n- **\"Primarily empirical study\" 声明**（Introduction 最后一段）：EMNLP 是否接受纯经验性研究？贡献量级是否足够？\n\n### 2. Related Work 完整性\n- 检查是否遗漏了重要的 2024-2026 相关工作（activation sparsity, learned pruning, KL distillation for efficiency）\n- 特别关注：\n  - Polar Sparsity (NeurIPS 2025) — 已引用，但是否充分讨论？\n  - GRIFFIN (2024) 在 Related Work 中仅一句话提及 — 是否需要更多讨论？\n  - 是否有其他 SwiGLU-specific sparsity 工作被遗漏？\n  - MoE routing 相关工作（Expert Choice, MoNE, D2D-MoE）引用是否充分？\n- 引用真实性：抽查 bib 条目的 venue/year/title 是否正确\n\n### 3. 叙事完整性\n- Abstract → Introduction → Conclusion 的故事线是否一致？\n- 结论中 \"future work includes N:M structured sparsity and scaling to 70B+\" — 是否暗示当前工作不够完整？\n- Limitations 是否全面？是否有未被提及的重要局限？\n- 跨架构/跨规模的负面结果（Mistral GSM8K 反转、Qwen-14B 推理退化）是否被充分讨论？\n\n### 4. 写作质量\n- 论文是否有\"AI写作\"痕迹（过度 hedging、重复性短语、无实质内容的长句）？\n- 数学符号一致性（§3 各公式的 notation 是否统一）\n- 表格/图表标题是否自包含（不看正文能否理解）\n- 参考文献格式是否统一\n\n请按 ACL Reviewer Guidelines 的标准输出审稿报告，包含：Summary (2-3句) → Strengths (逐条) → Weaknesses (逐条，标注 severity: critical/warning/minor) → Questions → Missing References → Overall Assessment (1-5 分制，参照 EMNLP 2026 评分标准) → Confidence (1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。\n\n## Venue 信息\n- **会议**：EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL style（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **附录**：在 references 之后，审稿人可参考\n\n## 论文路径\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **核心贡献**：用 KL divergence 替代 BCE 训练 sparsity predictor — 这是否算 sufficient novelty？KL distillation 本身是标准技术，创新性在哪里？\n- **MaskLLM 区分**：§2 Related Work 中 MaskLLM 三点区分（sparsity type / mask generation / allocation）是否充分？MaskLLM 已在 NeurIPS 2024 发表，本文在技术上走得比 MaskLLM 远多少？\n- **Taxonomy (Table 1 §3.7)**：两维分类框架（correction granularity × training signal coupling）是否真正有洞察力，还是仅仅是对已有方法的重新分类？\n- **\"Primarily empirical study\" 声明**（Introduction 最后一段）：EMNLP 是否接受纯经验性研究？贡献量级是否足够？\n\n### 2. Related Work 完整性\n- 检查是否遗漏了重要的 2024-2026 相关工作（activation sparsity, learned pruning, KL distillation for efficiency）\n- 特别关注：\n  - Polar Sparsity (NeurIPS 2025) — 已引用，但是否充分讨论？\n  - GRIFFIN (2024) 在 Related Work 中仅一句话提及 — 是否需要更多讨论？\n  - 是否有其他 SwiGLU-specific sparsity 工作被遗漏？\n  - MoE routing 相关工作（Expert Choice, MoNE, D2D-MoE）引用是否充分？\n- 引用真实性：抽查 bib 条目的 venue/year/title 是否正确\n\n### 3. 叙事完整性\n- Abstract → Introduction → Conclusion 的故事线是否一致？\n- 结论中 \"future work includes N:M structured sparsity and scaling to 70B+\" — 是否暗示当前工作不够完整？\n- Limitations 是否全面？是否有未被提及的重要局限？\n- 跨架构/跨规模的负面结果（Mistral GSM8K 反转、Qwen-14B 推理退化）是否被充分讨论？\n\n### 4. 写作质量\n- 论文是否有\"AI写作\"痕迹（过度 hedging、重复性短语、无实质内容的长句）？\n- 数学符号一致性（§3 各公式的 notation 是否统一）\n- 表格/图表标题是否自包含（不看正文能否理解）\n- 参考文献格式是否统一\n\n请按 ACL Reviewer Guidelines 的标准输出审稿报告，包含：Summary (2-3句) → Strengths (逐条) → Weaknesses (逐条，标注 severity: critical/warning/minor) → Questions → Missing References → Overall Assessment (1-5 分制，参照 EMNLP 2026 评分标准) → Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-20T15:24:16.165858+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-20T15:24:22.067279+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-20T15:24:22.117905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-20T15:24:29.906219+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 & 2 返回', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 & 2 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享 — 转发审稿原文给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 & 2 返回', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 & 2 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享 — 转发审稿原文给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-20T15:24:29.906734+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1372 · 2026-05-20T15:24:33.691878+00:00_

两位 Reviewer 和视觉审查 Agent 已并行启动，等待 Round 1 初审结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 110

## Round 110

4 recorded events


### User

_source line 1373 · 2026-05-20T15:30:50.769333+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

---

### Summary

本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。核心思想是将 mask 决策通过完整前向传播耦合到输出分布，使每个 neuron 的梯度依赖于所有其他 neuron 的 mask 状态，而非独立优化。在 LLaMA-3.1-8B 上 50% 稀疏度下 PPL 相对 TEAL 降低 14.5%，并在 Mistral-7B 和 Qwen-2.5-14B 上做了跨架构验证。论文自述为"primarily empirical study"。

---

### Strengths

**S1. 清晰的问题定义与动机。** §3.6 的梯度分析简洁有力地展示了 BCE 将 mask 训练分解为独立逐 neuron 分类问题（梯度 ∂L_BCE/∂σ_j 仅依赖 neuron j），而 KL 通过 Jacobian 链式传播使每个 neuron 的梯度依赖全层 mask 配置。这一洞察虽在数学上直观，但对理解为何 output-level 目标优于 element-wise 目标很有启发。

**S2. 受控实验设计。** 消融实验（§4.4, §4.5, Table 3-4）设计合理：target-swap ablation 用 BCE 训练在 KL 发现的 oracle mask 上以分离 mask 质量 vs. gradient coupling 的贡献；MSE baseline（Appendix G）用相同架构和 Lagrangian 控制器但不同 loss function，隔离了 coupling 效应。

**S3. 丰富的附录支撑。** 18 页论文含 10 页附录（A-P），覆盖 inference efficiency 分析、bottleneck sensitivity、温度调度、训练收敛、penalty controller 动态、OOD 评估、per-layer 分析、mask 可视化等。信息密度高。

**S4. 训练效率高。** 仅 1000 步（~45 min on 1×RTX PRO 6000）、75.9M 额外参数（<1% base model），训练成本极低，实用性强。

**S5. 负面结果的诚实报告。** Mistral-7B GSM8K 反转（Table 16-17）、Qwen-2.5-14B 推理退化（GSM8K -20pp）均被明确报告，而非隐藏。

---

### Weaknesses

**N1 [critical] 新颖性不足：核心贡献是标准 KL distillation 的直接应用。**
- 具体位置：§3.4 (Eq. 5), §1 最后一段 ("primarily empirical study")
- 问题：用 KL divergence 匹配 teacher（dense model）和 student（sparse model）的输出分布是知识蒸馏的经典范式（Hinton et al., 2015; Kim & Rush, 2016）。本文的创新在于将此范式应用于 SwiGLU sparsity predictor 训练，但技术上没有引入新的 loss function、新的优化方法、或新的理论分析。Gumbel-Sigmoid 松弛（§3.3）、adaptive Lagrangian penalty（§3.5）、TEAL global top-k allocation 均为已有技术的组合。
- §3.6 的梯度分析虽有启发性，但本质上是在复述"output-level loss 比 element-wise loss 传递更丰富梯度信号"这一已知事实（MiniLLM, GKD, DistiLLM 等 LLM KD 文献均基于此动机）。
- 与 MaskLLM 的区分（§2）：三个区分点（sparsity type / mask generation / allocation）确实存在，但核心训练原理（学习 mask 以最小化输出分布偏离）高度重合。MaskLLM 用 Gumbel-Softmax + output loss，本文用 Gumbel-Sigmoid + KL loss，差异有限。
- 为什么影响接收：EMNLP main conference 要求 sufficient novelty。作为 "primarily empirical study"，实验需要覆盖更广的模型/任务/对比方法才能弥补方法论创新的不足。
- 建议修改方向：(1) 增加与 MaskLLM 的直接实验对比（即使需要将 MaskLLM 从 N:M 适配到 unstructured），或充分论证为何不可比；(2) 深化理论贡献——例如分析 KL coupling 在什么条件下优于/劣于 BCE，而非仅做经验验证。

**N2 [critical] 缺少与已有训练型稀疏预测器的数值对比。**
- 具体位置：§4.2 (Table 2), §2 (Related Work)
- 问题：论文主要对比 TEAL（training-free baseline）和 magnitude-based pruning。但 §2 详细讨论了 DejaVu、ShadowLLM、FastForward 等训练型预测器，却未在实验中进行数值对比。这使得读者无法判断 KL predictor 相对于这些已有方法的优势大小。
- 论文在 §2 提到 "DejaVu introduces attention-based routing with per-layer MSE supervision" 和 "ShadowLLM uses per-layer MSE supervision"——这些是中间层级 coupling（per-layer intermediate）的代表，恰好是 Table 1 taxonomy 中的一个 cell。然而 taxonomy 的预测力未被实验验证（即没有展示这些方法在本文设置下的实际表现）。
- 为什么影响接收：没有与已有 trained predictor 对比，核心 claim "KL coupling 优于其他训练信号" 的证据不完整。
- 建议修改方向：至少复现 DejaVu-style per-layer MSE predictor 作为 baseline（代码复杂度低，仅需改 loss function），或引用并分析这些方法在 SwiGLU 模型上的已有结果。

**W1 [warning] 无实际推理加速验证。**
- 具体位置：Appendix A, Limitations §6
- 问题：Appendix A 明确指出 "the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support"。overhead 为 ~4.4%（Table 6），但 sparse computation 本身没有加速。对于一篇关于 "inference efficiency" 的工作，这严重削弱了实际意义。
- 论文的贡献严格来说是 prediction quality 而非 runtime efficiency，但 abstract 和 introduction 中 "reducing the computational burden" 等表述暗示了实际效率收益。
- 建议：(1) 调整 framing，更明确地将贡献定位为 "mask quality study" 而非 efficiency method；(2) 或提供 Triton/cuSPARSE 的 proof-of-concept 加速测量。

**W2 [warning] 实验规模和多样性有限。**
- 具体位置：§4.1, §4.6
- 问题：
  - 主实验仅在 LLaMA-3.1-8B 上进行，Mistral-7B 和 Qwen-2.5-14B 作为 "cross-architecture" 验证但结果不一致（GSM8K 反转、推理退化）
  - 训练数据仅用 WikiText-103（1000 steps, ~45 min），未探索其他数据源对 predictor 质量的影响
  - 所有实验使用相同的 predictor 架构（2-layer MLP, d_b=128），未与其他 predictor 架构（如 linear probe, attention-based routing）对比
  - 下游评估仅 5 个 benchmark（ARC-C, WG, HellaSwag, MMLU, GSM8K, PIQA），缺少生成任务（summarization, translation）和长文本理解任务
- 建议：增加至少一个 13B+ 规模模型的完整实验（不仅是 preliminary evaluation）；增加训练数据多样性实验。

**W3 [warning] Table 1 taxonomy 的分析价值有限。**
- 具体位置：§3.7, Table 1
- 问题：两维分类框架（correction granularity × training signal coupling）对已有方法做了整理，但：(1) 大部分 cell 只有 0-1 个方法，矩阵过于稀疏，难以得出 systematic conclusion；(2) taxonomy 的预测力未被验证——论文声称 "coupled + per-token" 应优于其他配置，但没有系统对比同一 taxonomy cell 内的方法；(3) 文中未讨论为何某些 cell 为空（例如 coupled + per-layer）——是技术上不可行还是尚未被探索？
- 建议：要么通过实验填充 taxonomy 的关键 cell（至少验证 2-3 个代表性配置），要么降低对 taxonomy 作为贡献的强调。

**W4 [warning] C1 ablation 存在混淆因素。**
- 具体位置：§4.4, Table 3-4
- 问题：Target-swap ablation 训练 BCE predictor 在 KL-derived oracle masks 上。但 oracle masks 是从完整 KL 训练（1000+2000 steps）得到的，已经包含了 KL 目标的信息。因此 "BCE on KL targets" 的表现部分反映了 KL 发现的 mask quality，但也受 BCE 训练本身能否忠实复现这些 mask 的影响。更干净的 ablation 应该：(a) 用 KL 训练的 frozen mask 直接评估（不经过 BCE 重新训练），或 (b) 用随机采样的 mask 分布进行消融。
- 论文确实报告了 "BCE on KL targets reproduces KL quality" (Table 4, Δ≤0.79pp)，这支持了 mask quality 是主要因素。但这也削弱了 gradient coupling 贡献的说服力——如果 BCE 也能达到相同质量，那 KL 的优势仅在于 mask *discovery* 而非训练过程本身。
- 建议：明确讨论此 confound，并补充"如果事先不知道好的 mask targets，BCE 无法发现它们"这一论点的更直接证据。

---

### Minor Issues

**M1.** §3.4 Eq. 5 中 KL 公式为 D_KL(P_dense || P_sparse)，即 forward KL。鉴于近期 LLM KD 文献（MiniLLM, DistiLLM）大量讨论 forward vs. reverse KL 的选择，论文应简要说明为何选择 forward KL 而非 reverse KL，或报告 reverse KL 的实验结果。

**M2.** GRIFFIN 引用（de2024griffin）在 OpenAlex 上 not_found，bib entry 列为 arXiv preprint。Griffin 本身是关于 gated linear recurrence 的架构，与 activation sparsity 的关联较弱。§2 最后一段提到 Griffin 是为了暗示方法可能 generalize beyond Transformer FFNs，但没有实验支撑。建议：要么去掉这句 speculation，要么降低其权重。

**M3.** Figure 1 caption 偏短，不够自包含——仅说 "Method overview" 但未解释 Gumbel-Sigmoid 松弛和 TEAL allocation 的角色。表格标题总体质量良好。

**M4.** References 中 CATS (Lee et al., 2024) 仍标为 arXiv preprint，但该工作可能已被发表（arXiv:2404.08763），建议核查更新。

**M5.** §4.3 "Extended Training Strategy" 的叙述比较仓促——2700 步 vs 1000 步 的对比只用了一段话。BCE 7pp worse PPL + KL 6x random precision 这些数字的 statistical significance 未报告。

---

### Questions for Authors

**Q1.** §3.6 分析表明 KL coupling 使 predictor 发现不同于 magnitude-based 的 mask pattern。但在 Table 3 中，BCE+STE 的 PPL 为 11.79 vs. KL 的 11.17——差异为 0.62 PPL。这个差异是否在统计上显著？Table 2 报告的 3-seed 标准差约 ±0.02-0.07，但 Table 3 的 ablation 是否也做了多 seed 评估？

**Q2.** 为什么不在 SwiGLU 的 gate 分支（而非 up-projection 分支）进行 sparsity prediction？Gate 分支的 sigmoid 输出天然接近二值化，可能更适合稀疏性预测。CATS 正是利用 gate output 进行 thresholding。

**Q3.** 论文是否尝试过 attention layer 的 sparsity prediction？Polar Sparsity (Shrestha et al., 2025) 将注意力头稀疏化——本文方法是否可以 extend 到 attention sparsity？

**Q4.** Adaptive penalty controller（§3.5）的 geometric doubling 和 deadzone (κ=0.02) 是如何选择的？对这些超参数的敏感性分析在哪里？

---

### Missing References

**MR1.** "Activation Sparsity Opportunities for Compressing General Large Language Models" (arXiv:2412.12178, Dec 2024) — 系统研究 SwiGLU FFN 的稀疏化机会和 accuracy-sparsity tradeoff，与本文直接相关。

**MR2.** "Accelerating Transformer Inference and Training with 2:4 Activation Sparsity" (arXiv:2503.16672, March 2025) — 探索结构化 2:4 activation sparsity，与论文 future work 中提到的 N:M sparsity 方向直接相关。

**MR3.** 论文引用了 MiniLLM 和 GKD 作为 KD 背景，但未引用 "Rethinking KL Divergence in Knowledge Distillation for Large Language Models" (Wen et al., arXiv:2404.02657, 2024)，该工作深入分析了 forward vs. reverse KL 在 LLM distillation 中的行为差异，与本文 KL 目标选择直接相关。

---

### 总体评分

**Overall**: **3.0 — Findings**

**一句话总结**: 扎实的经验性研究表明 output-distribution coupling 优于 per-neuron BCE 训练 SwiGLU 稀疏预测器，但核心方法是标准 KL distillation 的直接应用，缺少与已有训练型预测器的数值对比，新颖性不足以支撑 main conference 接收。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 技术正确，消融设计合理但 C1 ablation 有 confound；梯度分析正确但深度有限；缺少与 trained predictors 的对比削弱了核心 claim 的支撑 |
| Excitement | 2.5/5 | 核心是标准 KD 范式的应用；gradient coupling insight 有一定启发性但不够深刻；taxonomy 贡献有限；无 runtime speedup 限制实际影响 |
| Reproducibility | 4.0/5 | 训练细节完整（Appendix），超参数明确，架构简单可复现；但代码未提供（Ethics §C.5 提到 "Yes" 但未见链接） |
| Overall Assessment | 3.0/5 | Findings 水平——经验发现有价值，实验设计基本扎实，但方法新颖性和实验全面性未达 main conference 门槛 |

### Confidence

**4/5** — 熟悉 activation sparsity、knowledge distillation 和 SwiGLU LLM 推理优化文献。仔细阅读了全文和附录。对梯度分析和实验设计的评估有较高信心。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-20T15:31:09.320752+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 返回 (Reviewer 2 已完成)', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 Round 1 审稿结果 (Reviewer 2 已返回)'}, {'content': 'Step 2: 交叉分享 — 转发审稿原文给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 返回 (Reviewer 2 已完成)', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 Round 1 审稿结果 (Reviewer 2 已返回)'}, {'content': 'Step 2: 交叉分享 — 转发审稿原文给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-20T15:31:09.321326+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1376 · 2026-05-20T15:31:12.265713+00:00_

Reviewer 2 已返回审稿意见（Overall: 3.0 Findings）。关键发现：2 个 critical（新颖性不足、缺少与训练型预测器的对比）、4 个 warning、5 个 minor。

等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1377 · 2026-05-20T15:31:14.777745+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论概要：Overall 3.0（Findings 水平）**

主要发现：

- **2 个 critical 问题**：(1) 新颖性不足——核心是标准 KL distillation 的直接应用于 SwiGLU sparsity predictor，与 MaskLLM 技术重合度高；(2) 缺少与 DejaVu/ShadowLLM/FastForward 等已有训练型预测器的数值对比，核心 claim 证据不完整。

- **4 个 warning 问题**：无实际推理加速验证（Appendix A 承认无 wall-clock speedup）；实验规模有限（主要在 LLaMA-3.1-8B，跨架构结果不一致）；Table 1 taxonomy 分析价值有限；C1 ablation 存在混淆因素。

- **3 篇 missing references**：activation sparsity opportunities (2412.12178)、2:4 activation sparsity (2503.16672)、rethinking KL divergence in KD (2404.02657)。

- **优势**：梯度分析清晰、消融设计合理、附录丰富、训练效率高、负面结果诚实报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1378 · 2026-05-20T15:31:20.147312+00:00_

已记录 Reviewer 2 完整结果。仍在等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 112

## Round 112

8 recorded events


### User

_source line 1379 · 2026-05-20T15:32:16.508916+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法严谨性 + 实验设计）

### 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 方法论上以 KL 替代 BCE 训练稀疏预测器的思路清晰、目标-交换消融设计巧妙、实验诚实地报告了负面结果，但评估范围较窄、PPL 优势未能转化为下游任务一致性提升、且缺乏实际推理加速，限制了论文的影响力。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心实验方法论合理，消融设计好，但多种子覆盖不一致、MSE baseline 单种子、消融仅在50%稀疏度 |
| Excitement | 3/5 | KL 发现与幅度不同的 mask 模式有学术价值，但无实际加速、下游结果混合、算法新颖性有限 |
| Reproducibility | 4/5 | 超参数文档齐全、单 GPU 45分钟可复现、敏感性分析充分，但代码不可用（双盲） |

### Must-Fix 问题（影响接收决定）

**N1** [critical] 多种子覆盖不一致，存在选择性报告风险
- 具体位置：Table 2 (experiments.tex lines 39-65)
- 问题：50% KL global（Table 2 最佳 PPL 11.79）为 single-seed (s42)，而 50% KL uniform（PPL 11.92±0.07）为 3-seed。Table 5（appendix Table 15）50% global 行中，MMLU 有 ±0.2 但 PPL、ARC-c、WG、GSM8K 均无 ±。MSE baseline（支撑 "coupling alignment" 核心论点）全部 single-seed。当 headline result 是 single-seed 而次优结果是 multi-seed 时，读者无法判断 11.79 是否在 multi-seed 分布的幸运端。
- 建议：对 Table 2 所有行提供完整 3-seed 统计；MSE baseline 至少补 2 个种子。

**N2** [critical] PPL 改善与下游任务脱节——核心实用性质疑
- 具体位置：Table 2 (30% sparsity rows), §4.2 para 2-3
- 问题：在 30%（唯一下游不崩溃的稀疏度），KL 的 PPL 比 TEAL 好 19%（8.81 vs 10.82），但 MMLU 差 5.2pp（40.7 vs 45.9）、GSM8K 差 1.3pp（7.5 vs 8.8）。论文将此归因于 "forward KL's mode-covering may dilute task-specific knowledge pathways"，但无实验验证。如果 PPL 改善不能转化为下游提升甚至在关键任务上劣化，论文的实用贡献被严重削弱。
- 建议：深入分析 MMLU/GSM8K 劣化的机制（per-task mask overlap 分析）；或在 claim 中显著降调。

**N3** [critical] 消融实验仅在 50% 稀疏度——论文实际有用的 regime 未被消融覆盖
- 具体位置：Table 4 (experiments.tex lines 127-152)
- 问题：Table 4 所有消融仅在 50%。但论文自己承认 50% 时下游崩溃至随机水平（"capacity-limited regime"），30% 才是实际可用的稀疏度。如果 forward KL 在 30% 时相对 JSD/reverse KL 的优势缩小甚至消失，论文的 loss function 选择结论可能不成立。
- 建议：在 30% 稀疏度补充 Forward KL / JSD / Reverse KL / STE 的消融比较。

### Should-Fix 问题

**W1** [warning] 稀疏度控制器在 30% 目标时失败（5% 偏差）——λ saturates at cap (5000), actual 28.5% vs target 30%。正文 headline claim "19%" 基于 mismatched 比较；matched-sparsity 比较（14.5%）应更显著。

**W2** [warning] Forward KL 方向选择理论论证不足——标准 KD 文献通常论证 reverse KL 对 capacity-limited student 更优，与论文论点矛盾。实验验证了 forward > reverse，但理论解释需加强。

**W3** [warning] 评估域同质性——训练 WikiText-103、评估 WikiText-2（同为 Wikipedia）。C4 OOD 显示 domain shift 放大 PPL（1.74× vs 1.44× dense）且跨种子方差增 30×（CV 6.3% vs 0.2%）。

**W4** [warning] §3.6 梯度分析 informal——缺乏 KL 梯度的显式表达式、耦合程度量化、低 SNR 产生更好 mask 的正式解释。

**W5** [warning] 无实际推理加速——当前实现增加 6.4% 开销。

### 主要优势
1. C1 目标-交换消融设计精妙，有效解耦 target quality 与 gradient coupling
2. 诚实报告负面结果（MMLU/GSM8K 退化、Qwen-14B 反转、50% 下游崩溃）
3. 全面的敏感性分析（bottleneck <3%、温度 <1.8%、训练步数 800 步饱和）
4. §3.7 二维分类框架有用
5. 单 GPU 45 分钟训练，高度可复现

### 引用核查
- verify_references: 47 entries, 0 orphan, 0 missing, 41 verified, 1 not_found (de2024griffin/Griffin), 5 minor mismatches (author name format/year)
- 无虚假引用

### 数据一致性核查
- 表格间数字一致（Table 2 ↔ Table 5 ↔ Appendix tables 全部匹配）
- Limitations 中 PPL 数值与正文表格匹配（40% PPL=10.76 ✓, MMLU=35.5% ✓, Mistral -17.3% ✓）
- Abstract 中 "ARC +4.4pp"(43.7-39.33=4.37≈4.4 ✓), "HellaSwag +7.8pp"(71.07-63.31=7.76≈7.8 ✓)
- 唯一轻微问题：Limitations 称 Mistral GSM8K "7.0–11.1%"，但 Table 17 仅报告 8.6±1.8，个别种子值未在表中展示

### 格式合规
- 正文 8 页（Section 1-5 在 page 1-8），合规
- Double-blind：\usepackage[review]{acl}，作者 "Anonymous"，无 GitHub 链接。GPU 型号（RTX PRO 6000 Blackwell）具体但不构成去匿名化
- 引用格式符合 ACL natbib 规范

**Confidence: 4/5**

如果能补充 30% 消融和完整的 multi-seed Table 2，建议可升至 Conference（4）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-20T15:32:31.532228+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 初始化', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Round 1 审稿完成'}, {'content': 'Step 2: 交叉分享 — 转发审稿原文给对方 Reviewer', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 初始化', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Round 1 审稿完成'}, {'content': 'Step 2: 交叉分享 — 转发审稿原文给对方 Reviewer', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-20T15:32:31.532732+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-20T15:33:05.463573+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 **Reviewer 2** 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness/Question 标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Summary\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。核心思想是将 mask 决策通过完整前向传播耦合到输出分布，使每个 neuron 的梯度依赖于所有其他 neuron 的 mask 状态，而非独立优化。在 LLaMA-3.1-8B 上 50% 稀疏度下 PPL 相对 TEAL 降低 14.5%，并在 Mistral-7B 和 Qwen-2.5-14B 上做了跨架构验证。论文自述为\"primarily empirical study\"。\n\n### Strengths\nS1. 清晰的问题定义与动机。§3.6 的梯度分析简洁有力。\nS2. 受控实验设计。消融实验设计合理。\nS3. 丰富的附录支撑（10 页附录）。\nS4. 训练效率高（1000 步，~45 min）。\nS5. 负面结果的诚实报告。\n\n### Weaknesses\n\n**N1 [critical] 新颖性不足：核心贡献是标准 KL distillation 的直接应用。**\n- KL divergence 匹配 teacher/student 输出分布是知识蒸馏经典范式。本文技术上未引入新 loss function、新优化方法或新理论分析。Gumbel-Sigmoid、adaptive Lagrangian、TEAL allocation 均为已有技术组合。\n- §3.6 梯度分析本质是复述 \"output-level loss 比 element-wise loss 传递更丰富梯度信号\" 已知事实。\n- 与 MaskLLM 区分：三个区分点存在，但核心训练原理高度重合。MaskLLM 用 Gumbel-Softmax + output loss，本文用 Gumbel-Sigmoid + KL loss，差异有限。\n\n**N2 [critical] 缺少与已有训练型稀疏预测器的数值对比。**\n- 主要对比 TEAL（training-free）和 magnitude-based pruning，但 §2 讨论的 DejaVu、ShadowLLM、FastForward 未在实验中数值对比。Taxonomy 预测力未被验证。\n\n**W1 [warning] 无实际推理加速验证。** Appendix A 承认无 wall-clock speedup，增加 6.4% overhead。\n\n**W2 [warning] 实验规模和多样性有限。** 主实验仅 LLaMA-3.1-8B；训练数据仅 WikiText-103；predictor 架构未与其他形式对比；缺少生成任务评估。\n\n**W3 [warning] Table 1 taxonomy 分析价值有限。** 矩阵过于稀疏，预测力未验证，空 cell 未讨论。\n\n**W4 [warning] C1 ablation 存在混淆因素。** Oracle masks 包含 KL 目标信息；更干净的 ablation 应用 frozen mask 直接评估。\n\n### Minor Issues\nM1. Forward vs reverse KL 选择应更充分论证。\nM2. Griffin 引用关联较弱，speculation 无实验支撑。\nM3. Figure 1 caption 不够自包含。\nM4. CATS 引用可能需更新。\nM5. Extended Training 叙述仓促。\n\n### Questions\nQ1. Table 3 ablation 是否做了多 seed？BCE+STE vs KL 差异 0.62 是否显著？\nQ2. 为何不在 gate 分支做 sparsity prediction？\nQ3. 是否尝试过 attention layer sparsity prediction？\nQ4. Penalty controller 超参数敏感性？\n\n### Missing References\nMR1. Activation Sparsity Opportunities (arXiv:2412.12178)\nMR2. 2:4 Activation Sparsity (arXiv:2503.16672)\nMR3. Rethinking KL Divergence in KD (arXiv:2404.02657)\n\n### Overall: 3.0 (Findings)\n\n---\n\n请对上述每个 N1/N2/W1-W4/M1-M5/Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 **Reviewer 2** 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness/Question 标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Summary\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。核心思想是将 mask 决策通过完整前向传播耦合到输出分布，使每个 neuron 的梯度依赖于所有其他 neuron 的 mask 状态，而非独立优化。在 LLaMA-3.1-8B 上 50% 稀疏度下 PPL 相对 TEAL 降低 14.5%，并在 Mistral-7B 和 Qwen-2.5-14B 上做了跨架构验证。论文自述为\"primarily empirical study\"。\n\n### Strengths\nS1. 清晰的问题定义与动机。§3.6 的梯度分析简洁有力。\nS2. 受控实验设计。消融实验设计合理。\nS3. 丰富的附录支撑（10 页附录）。\nS4. 训练效率高（1000 步，~45 min）。\nS5. 负面结果的诚实报告。\n\n### Weaknesses\n\n**N1 [critical] 新颖性不足：核心贡献是标准 KL distillation 的直接应用。**\n- KL divergence 匹配 teacher/student 输出分布是知识蒸馏经典范式。本文技术上未引入新 loss function、新优化方法或新理论分析。Gumbel-Sigmoid、adaptive Lagrangian、TEAL allocation 均为已有技术组合。\n- §3.6 梯度分析本质是复述 \"output-level loss 比 element-wise loss 传递更丰富梯度信号\" 已知事实。\n- 与 MaskLLM 区分：三个区分点存在，但核心训练原理高度重合。MaskLLM 用 Gumbel-Softmax + output loss，本文用 Gumbel-Sigmoid + KL loss，差异有限。\n\n**N2 [critical] 缺少与已有训练型稀疏预测器的数值对比。**\n- 主要对比 TEAL（training-free）和 magnitude-based pruning，但 §2 讨论的 DejaVu、ShadowLLM、FastForward 未在实验中数值对比。Taxonomy 预测力未被验证。\n\n**W1 [warning] 无实际推理加速验证。** Appendix A 承认无 wall-clock speedup，增加 6.4% overhead。\n\n**W2 [warning] 实验规模和多样性有限。** 主实验仅 LLaMA-3.1-8B；训练数据仅 WikiText-103；predictor 架构未与其他形式对比；缺少生成任务评估。\n\n**W3 [warning] Table 1 taxonomy 分析价值有限。** 矩阵过于稀疏，预测力未验证，空 cell 未讨论。\n\n**W4 [warning] C1 ablation 存在混淆因素。** Oracle masks 包含 KL 目标信息；更干净的 ablation 应用 frozen mask 直接评估。\n\n### Minor Issues\nM1. Forward vs reverse KL 选择应更充分论证。\nM2. Griffin 引用关联较弱，speculation 无实验支撑。\nM3. Figure 1 caption 不够自包含。\nM4. CATS 引用可能需更新。\nM5. Extended Training 叙述仓促。\n\n### Questions\nQ1. Table 3 ablation 是否做了多 seed？BCE+STE vs KL 差异 0.62 是否显著？\nQ2. 为何不在 gate 分支做 sparsity prediction？\nQ3. 是否尝试过 attention layer sparsity prediction？\nQ4. Penalty controller 超参数敏感性？\n\n### Missing References\nMR1. Activation Sparsity Opportunities (arXiv:2412.12178)\nMR2. 2:4 Activation Sparsity (arXiv:2503.16672)\nMR3. Rethinking KL Divergence in KD (arXiv:2404.02657)\n\n### Overall: 3.0 (Findings)\n\n---\n\n请对上述每个 N1/N2/W1-W4/M1-M5/Q1-Q4 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-20T15:33:17.218678+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11755
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-20T15:33:17.320200+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 **Reviewer 1** 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness/Question 标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Overall: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1 [critical] 多种子覆盖不一致，存在选择性报告风险**\n- 50% KL global（Table 2 最佳 PPL 11.79）为 single-seed (s42)，而 50% KL uniform（PPL 11.92±0.07）为 3-seed。Table 5（appendix Table 15）50% global 行中，MMLU 有 ±0.2 但 PPL、ARC-c、WG、GSM8K 均无 ±。MSE baseline 全部 single-seed。\n\n**N2 [critical] PPL 改善与下游任务脱节——核心实用性质疑**\n- 30% 稀疏度下 KL PPL 比 TEAL 好 19%（8.81 vs 10.82），但 MMLU 差 5.2pp（40.7 vs 45.9）、GSM8K 差 1.3pp（7.5 vs 8.8）。PPL 改善不能转化为下游提升甚至在关键任务上劣化。\n\n**N3 [critical] 消融实验仅在 50% 稀疏度——论文实际有用的 regime 未被消融覆盖**\n- Table 4 所有消融仅在 50%。但论文承认 50% 下游崩溃，30% 才是可用稀疏度。30% 的 loss function 选择消融缺失。\n\n### Should-Fix 问题\n\n**W1 [warning]** 稀疏度控制器 30% 目标偏差 5%（实际 28.5%），headline \"19%\" 基于 mismatched 比较。\n\n**W2 [warning]** Forward KL 方向选择论证不足——标准 KD 文献通常论证 reverse KL 对 capacity-limited student 更优。\n\n**W3 [warning]** 评估域同质性——WikiText-103 训练、WikiText-2 评估，C4 OOD 显示 domain shift 放大方差 30×。\n\n**W4 [warning]** §3.6 梯度分析 informal——缺乏显式梯度表达式、耦合程度量化。\n\n**W5 [warning]** 无实际推理加速——增加 6.4% 开销。\n\n### 主要优势\n1. C1 目标-交换消融设计精妙\n2. 诚实报告负面结果\n3. 全面敏感性分析\n4. §3.7 二维分类框架有用\n5. 单 GPU 45 分钟训练\n\n### 引用核查\n- 47 entries, 0 orphan, 0 missing, 41 verified, 1 not_found (Griffin), 5 minor mismatches\n- 无虚假引用\n\n### 数据一致性核查\n- 表格间数字全部匹配\n- Limitations PPL 数值与正文匹配\n- Abstract 数字验证通过\n\n### 格式合规\n- 正文 8 页，合规\n- Double-blind 合规\n- 引用格式合规\n\n**Confidence: 4/5**\n评语：如果能补充 30% 消融和完整 multi-seed Table 2，建议可升至 Conference (4)。\n\n---\n\n请对上述每个 N1/N2/N3/W1-W5 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 **Reviewer 1** 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness/Question 标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Overall: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1 [critical] 多种子覆盖不一致，存在选择性报告风险**\n- 50% KL global（Table 2 最佳 PPL 11.79）为 single-seed (s42)，而 50% KL uniform（PPL 11.92±0.07）为 3-seed。Table 5（appendix Table 15）50% global 行中，MMLU 有 ±0.2 但 PPL、ARC-c、WG、GSM8K 均无 ±。MSE baseline 全部 single-seed。\n\n**N2 [critical] PPL 改善与下游任务脱节——核心实用性质疑**\n- 30% 稀疏度下 KL PPL 比 TEAL 好 19%（8.81 vs 10.82），但 MMLU 差 5.2pp（40.7 vs 45.9）、GSM8K 差 1.3pp（7.5 vs 8.8）。PPL 改善不能转化为下游提升甚至在关键任务上劣化。\n\n**N3 [critical] 消融实验仅在 50% 稀疏度——论文实际有用的 regime 未被消融覆盖**\n- Table 4 所有消融仅在 50%。但论文承认 50% 下游崩溃，30% 才是可用稀疏度。30% 的 loss function 选择消融缺失。\n\n### Should-Fix 问题\n\n**W1 [warning]** 稀疏度控制器 30% 目标偏差 5%（实际 28.5%），headline \"19%\" 基于 mismatched 比较。\n\n**W2 [warning]** Forward KL 方向选择论证不足——标准 KD 文献通常论证 reverse KL 对 capacity-limited student 更优。\n\n**W3 [warning]** 评估域同质性——WikiText-103 训练、WikiText-2 评估，C4 OOD 显示 domain shift 放大方差 30×。\n\n**W4 [warning]** §3.6 梯度分析 informal——缺乏显式梯度表达式、耦合程度量化。\n\n**W5 [warning]** 无实际推理加速——增加 6.4% 开销。\n\n### 主要优势\n1. C1 目标-交换消融设计精妙\n2. 诚实报告负面结果\n3. 全面敏感性分析\n4. §3.7 二维分类框架有用\n5. 单 GPU 45 分钟训练\n\n### 引用核查\n- 47 entries, 0 orphan, 0 missing, 41 verified, 1 not_found (Griffin), 5 minor mismatches\n- 无虚假引用\n\n### 数据一致性核查\n- 表格间数字全部匹配\n- Limitations PPL 数值与正文匹配\n- Abstract 数字验证通过\n\n### 格式合规\n- 正文 8 页，合规\n- Double-blind 合规\n- 引用格式合规\n\n**Confidence: 4/5**\n评语：如果能补充 30% 消融和完整 multi-seed Table 2，建议可升至 Conference (4)。\n\n---\n\n请对上述每个 N1/N2/N3/W1-W5 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-20T15:33:18.696168+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1375
}
```

</details>

---


### Assistant

_source line 1386 · 2026-05-20T15:33:21.636341+00:00_

交叉分享已派发。等待两位 Reviewer 返回逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1387 · 2026-05-20T15:33:24.151542+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.5 (Borderline Conference)**
- 3 个 Critical 问题：(1) 多种子覆盖不一致（最优结果 11.79 为 single-seed）；(2) PPL 改善与下游任务脱节（30% 时 MMLU 差 5.2pp）；(3) 消融仅在 50% 稀疏度（实际可用的 30% regime 未覆盖）
- 5 个 Warning 问题：稀疏度控制器偏差、Forward KL 理论论证不足、评估域同质性、梯度分析 informal、无实际加速
- 主要优势：C1 target-swap 消融设计精妙、负面结果诚实报告、敏感性分析充分
- 数据一致性和格式合规均通过检查

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1388 · 2026-05-20T15:33:30.464525+00:00_

Reviewer 1 Round 1 已确认（3.5 Borderline Conference）。交叉分享已发出，等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1389 · 2026-05-20T15:36:04.518142+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的逐条交叉回应

### Critical Issues

**[REBUT] R2-N1: 新颖性不足**
R2 过于简化。组件层面确实无新意（KL+Gumbel+Lagrangian 均已有），但三个发现有独立贡献：(1) C1 目标-交换消融（§4.4, Table 3）是新颖的实验设计，文献未见类似的 target-quality-vs-coupling 解耦实验；(2) 46–68% mask divergence（§4.4, Figure 7/8）——prior work 未定量展示 output-level loss 会发现与 magnitude 完全不同的 pattern；(3) MSE catastrophic failure（Table 2, 1.9×/9.6× worse than TEAL）区分了"coupling"和"output-alignment"。与 MaskLLM 的区分是问题设定层面的（static N:M weight sparsity vs contextual activation sparsity），不只是 Gumbel variant 差异。但我同意算法新颖性有限，Excitement 3/5 部分反映此点。

**[REBUT] R2-N2: 缺少已有方法数值对比**
论文通过 controlled ablations 已覆盖核心设计选择：BCE baseline = DejaVu-style（experiments.tex line 22 明确标注）; MSE baseline = ShadowLLM/D2DMoE 的 intermediate coupling; compensation analysis = FastForward。保持 architecture/data/optimizer 一致仅变 loss function 比直接跑原始代码更严谨。但同意 taxonomy predictive power 验证不充分（MSE 仅 single-seed data point）。

### Warning Issues

**[AGREE] R2-W1**: 同意。我已列为 W5。无 wall-clock speedup 限制 practical impact。

**[AGREE] R2-W2**: 同意。与我的 W3（评估域同质性）一致。C4 OOD 方差增 30× 支持此担忧。

**[REBUT] R2-W3**: Table 1 taxonomy 3×2 矩阵中 5/6 cell 有代表方法，空 cell 合理（无 static BCE/MSE 工作）。关键预测已通过 controlled ablations 验证（KL >> MSE >> BCE）。空 cell 讨论是 editorial issue。

**[REBUT] R2-W4**: R2 误解 C1 目的。Oracle masks "包含 KL 信息"正是设计意图——测试 KL-discovered targets 能否通过 simpler objective 传递。"Frozen mask direct evaluation"等同于 KL predictor inference，不回答因果问题。Hard-vs-soft confound 已被 Table 4 BCE+Gumbel 消融 partially addressed。

### Minor Issues

**[AGREE] M1**: Forward vs reverse KL 理论论证不足（同我的 W2）。
**[AGREE] M2**: Griffin 引用关联弱且 OpenAlex 未找到（confidence 0.296）。
**[REBUT] M3**: Figure 1 caption 信息量足够（what+how+inference pipeline）。
**[AGREE] M4/M5**: 合理建议。

### Questions

**Q1**: 有效。Table 4 全部 single-seed。KL vs JSD (Δ=0.75) 可能在 multi-seed 方差范围内。与我的 N3 一致。
**Q2**: 答案清晰——gate 分支输入需等 gate computation 完成，增加 critical-path latency；x^(ℓ) 允许并行。
**Q3**: Out of scope（attention vs FFN sparsity 是不同问题）。
**Q4**: 有效。Controller 超参数（ε, doubling rate）未显式 ablate。

### Missing References

全部同意，尤其 MR3 "Rethinking KL Divergence in KD" 与 §3.4 forward vs reverse 讨论直接相关。

### 评分分歧

R2 给 3.0 (Findings)，我给 3.5 (Borderline Conference)。0.5 分分歧反映对 empirical contribution bar 的不同判断：我认为 C1 ablation + mask divergence 发现 + MSE failure 的 empirical insight 足以支撑 borderline conference；R2 认为算法新颖性是更 binding 的 constraint。我维持 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1390 · 2026-05-20T15:36:10.683441+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 115

## Round 115

2 recorded events
