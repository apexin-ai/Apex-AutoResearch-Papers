# Director coordination — Part 6 of 7

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/3d/3daf92a3dbeb151a5ec1.json)

## Round 139

### Tool call

_source line 1421 · 2026-05-23T09:27:49.626675+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 15 issues ===\n\n  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1]\n        note: \"R1-N1 升级为 Must-Fix。论文已有 DEFF simulation (App I) 和 size-stratified table (App D)，但正文仍以 simple-mean 为主报告值而未在正文充分论证选择。Cluster bootstrap CI [26.7%, 53.2%] 极宽未讨论。\"\n    action_items:\n      - round: 15\n        action: \"正文 §4.2 需并列呈现两种估计并解释选择理由；讨论 cluster bootstrap CI 宽度的驱动因素\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定外部效度受限\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W3: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3: 标题改为 Detection Power under Controlled Injection\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 + R2-W2 共识升级。两位 reviewer 一致认为 uniform flipping 不能被称为 worst-case，可能是 easiest-to-detect。要求增加更现实的注入模型或更准确描述其性质。\"\n    action_items:\n      - round: 15\n        action: \"将 'worst-case' 改为 'stylized/simplified'；在正文讨论 uniform flipping 对 TPR 标定的影响方向；考虑增加 difficulty-dependent 注入对比\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N3\"\n    summary: \"框架贡献被过度声称（Contribution 3 vs Section 2 自述矛盾）\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W6: 方法论新颖性有限\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7: 建议升级 highlight LLM-specific innovations\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 升级为 Must-Fix，R1 AGREE with nuance。Introduction Contribution 3 列 'framework' 与 Section 2 'We do not modify the MH procedure' 矛盾。R1 认为 cross-subject matching 有实质适配但不构成方法创新。\"\n    action_items:\n      - round: 15\n        action: \"Contribution 3 重述为 'methodological adaptations enabling valid DIF in LLM setting' 而非独立框架贡献；消除与 Section 2 的措辞矛盾\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W1。阈值源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity (App A.2) 有用但不等于论证适切性。\"\n    action_items:\n      - round: 15\n        action: \"增加一段讨论 ETS 阈值在 LLM 语境下的适切性，或用 permutation-based null 确定 LLM-specific 阈值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W2。BH-FDR 仅移除 3/3918 items 恰恰说明 p-value 已无区分力。论文已有 DEFF 校正恢复 p-value selectivity，但正文未充分讨论。\"\n    action_items:\n      - round: 15\n        action: \"§3.2 或 §4.2 讨论 N=5227 下 p-value 行为；说明 DEFF 校正如何恢复 p-value 的区分作用\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"Within-family DIF（Llama-2 vs 3, C%=59.2%）与架构/能力代际差异混淆\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W3。App N 将 within-family 定位为 'confirming temporal DIF not artifact of architecture'，但逻辑可能相反。\"\n    action_items:\n      - round: 15\n        action: \"重新框架化 within-family 分析的解释——说明 C% 更高可能因架构差异叠加时间效应\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"GSM1K 相关性（r=-0.478, N=33）正文用 'confirms' 语气但应保持 exploratory 定位\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W4。Figure 5 caption 标 exploratory 但正文用 confirming 语气。R20-N1 曾标 resolved 但本轮再次提出。\"\n    action_items:\n      - round: 15\n        action: \"统一 exploratory 定位，正文避免 confirms/confirming；报告 r 的 CI；讨论样本代表性\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"Local independence 违反（Yen's Q3）的定量影响未与 DIF detection rate 关联——DEFF 处理 family-level，Q3 是 item-level\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W5。两个层面的非独立性（model-level clustering vs item-level local dependence）需分别处理。\"\n    action_items:\n      - round: 15\n        action: \"量化 item-level LD 对 MH-DIF false detection rate 的贡献，或讨论为何 DEFF 足以处理两层面\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W6\"\n    summary: \"遗漏 concurrent work：CoDeC（ICLR 2026）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W1 提出，R1 AGREE（需核实时间线）。CoDeC 使用 in-context learning 检测污染，属 global exposure 范畴。\"\n    action_items:\n      - round: 15\n        action: \"核实 CoDeC 发表时间线；如在本文投稿前公开则加入 §2\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W7\"\n    summary: \"可操作性缺口：DIF 是 mechanism-agnostic 但推荐 mechanism-conditional responses，缺判断标准\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W3 提出，R1 AGREE with nuance。R1 建议增加简要决策启发式而非完整框架。\"\n    action_items:\n      - round: 15\n        action: \"§5.2 增加 1-2 句决策启发式（如 |Δ_MH|>2.0 + web-overlap → prioritize removal）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-I1\"\n    summary: \"'两维度正交'作为 Contribution 1 的新颖性存疑——从构念定义可预期\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2: 建议调整为 empirical confirmation\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N2 升级为 Must-Fix，R1 REBUT（NLP 社区未量化验证，Figure 1 有独立价值）。存在分歧：R2 认为定义可预期，R1 认为实证量化有价值。\"\n    action_items:\n      - round: 15\n        action: \"将 Contribution 1 从 'discovery' 调整为 'empirical quantification of a theoretically expected but previously unverified distinction'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-I2\"\n    summary: \"视觉节奏不均：p3-6 连续 4 页无 figure/table，p7 堆积 3 个 display items\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"视觉审查 Agent 发现。建议将 Table 1 或 Figure 2 提前至 §3-4 附近。\"\n    action_items:\n      - round: 15\n        action: \"调整 figure/table placement 平衡视觉节奏\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 14 issues（状态更新） ===\n\n  - id: \"R14-W1\"\n    summary: \"Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷，但 DIF 无法区分 contamination / capability evolution / composition shift\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M1 + R2-W-F1 + R2-W-F2 共识。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"本轮未作为独立 issue 提出，但 R15-N3 (overclaiming) 和 R15-I1 (两维度) 涉及相同 framing 层面。论文已引入 Camilli impact-vs-bias、composition control (Δ=1.08pp)、within-arch DIF。部分改善但 R15 仍有 framing 问题。\"\n    action_items:\n      - round: 14\n        action: \"综合重写 framing\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W2\"\n    summary: \"DEFF 估计范围过宽\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2\"\n      - round: 15\n        reviewers: [1]\n        note: \"Merged into R15-N1, 升级为 critical\"\n    action_items: []\n    resolution: \"Superseded by R15-N1\"\n    resolution_round: null\n\n  - id: \"R14-W3\"\n    summary: \"Semi-synthetic 注入模型生态效度有限\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-N2, 升级为 critical\"\n    action_items: []\n    resolution: \"Superseded by R15-N2\"\n    resolution_round: null\n\n  - id: \"R14-W4\"\n    summary: \"缺少 base/instruct composition shift 的直接控制\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W4\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未被单独提出。论文已增加 App O composition control (Δ=1.08pp) 和 §5.1 讨论。可能已部分修复。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W5\"\n    summary: \"\\\\enlargethispage 使用激进\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W5\"\n      - round: 15\n        reviewers: [2]\n        note: \"R2 小问题中提到 discussion.tex 中有 \\\\enlargethispage*{4\\\\baselineskip}。较 R14 的 6\\\\baselineskip 有改善。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W6\"\n      - round: 15\n        reviewers: [2]\n        note: \"R2 小问题中提到 measurement invariance / temporal score incomparability 仍有混用。有改善但未完全统一。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-N3, 升级为 critical\"\n    action_items: []\n    resolution: \"Superseded by R15-N3\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"Conclusion 仅 4 句话\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W8\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未被单独提出。可能已改善。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N1\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N1\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未被单独提出。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"'两个维度'框架正交性可能是概念上预期的结果\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-I1, R2 升级为 Must-Fix, R1 REBUT. 存在分歧。\"\n    action_items: []\n    resolution: \"Superseded by R15-I1\"\n    resolution_round: null\n\n  # === Round 13 issues（状态更新） ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W1\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W1\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未作为独立 issue 提出。论文已大幅改善 framing（引入 mechanism-agnostic diagnostic 定位、exclusion arguments、base-vs-instruct decomposition）。但 R15-N3 和 R15-W7 仍涉及相关层面。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定条件\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2\"\n      - round: 14\n        reviewers: []\n        note: \"已有 k≤5 限定\"\n    action_items: []\n    resolution: \"Contribution 2 已写为 'ΔFPR = 0 under single-subject contamination, k ≤ 5'。R14/R15 未再提出。\"\n    resolution_round: 14\n\n  # === 历史 issues（已 resolved，保留追踪） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Size-stratified DEFF table added. Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法未定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Formal definition in app:dedup_k.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Reframed as 'Orthogonal constructs'.\"\n    resolution_round: 19\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Difficulty-dependent injection results written to paper.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as exploratory. R15 再次提出正文仍用 confirms 语气 (R15-W4)。\"\n    resolution_round: 20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 15 issues ===\n\n  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1]\n        note: \"R1-N1 升级为 Must-Fix。论文已有 DEFF simulation (App I) 和 size-stratified table (App D)，但正文仍以 simple-mean 为主报告值而未在正文充分论证选择。Cluster bootstrap CI [26.7%, 53.2%] 极宽未讨论。\"\n    action_items:\n      - round: 15\n        action: \"正文 §4.2 需并列呈现两种估计并解释选择理由；讨论 cluster bootstrap CI 宽度的驱动因素\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定外部效度受限\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W3: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3: 标题改为 Detection Power under Controlled Injection\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N2 + R2-W2 共识升级。两位 reviewer 一致认为 uniform flipping 不能被称为 worst-case，可能是 easiest-to-detect。要求增加更现实的注入模型或更准确描述其性质。\"\n    action_items:\n      - round: 15\n        action: \"将 'worst-case' 改为 'stylized/simplified'；在正文讨论 uniform flipping 对 TPR 标定的影响方向；考虑增加 difficulty-dependent 注入对比\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N3\"\n    summary: \"框架贡献被过度声称（Contribution 3 vs Section 2 自述矛盾）\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W6: 方法论新颖性有限\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7: 建议升级 highlight LLM-specific innovations\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N1 升级为 Must-Fix，R1 AGREE with nuance。Introduction Contribution 3 列 'framework' 与 Section 2 'We do not modify the MH procedure' 矛盾。R1 认为 cross-subject matching 有实质适配但不构成方法创新。\"\n    action_items:\n      - round: 15\n        action: \"Contribution 3 重述为 'methodological adaptations enabling valid DIF in LLM setting' 而非独立框架贡献；消除与 Section 2 的措辞矛盾\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W1。阈值源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity (App A.2) 有用但不等于论证适切性。\"\n    action_items:\n      - round: 15\n        action: \"增加一段讨论 ETS 阈值在 LLM 语境下的适切性，或用 permutation-based null 确定 LLM-specific 阈值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W2。BH-FDR 仅移除 3/3918 items 恰恰说明 p-value 已无区分力。论文已有 DEFF 校正恢复 p-value selectivity，但正文未充分讨论。\"\n    action_items:\n      - round: 15\n        action: \"§3.2 或 §4.2 讨论 N=5227 下 p-value 行为；说明 DEFF 校正如何恢复 p-value 的区分作用\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"Within-family DIF（Llama-2 vs 3, C%=59.2%）与架构/能力代际差异混淆\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W3。App N 将 within-family 定位为 'confirming temporal DIF not artifact of architecture'，但逻辑可能相反。\"\n    action_items:\n      - round: 15\n        action: \"重新框架化 within-family 分析的解释——说明 C% 更高可能因架构差异叠加时间效应\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"GSM1K 相关性（r=-0.478, N=33）正文用 'confirms' 语气但应保持 exploratory 定位\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W4。Figure 5 caption 标 exploratory 但正文用 confirming 语气。R20-N1 曾标 resolved 但本轮再次提出。\"\n    action_items:\n      - round: 15\n        action: \"统一 exploratory 定位，正文避免 confirms/confirming；报告 r 的 CI；讨论样本代表性\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"Local independence 违反（Yen's Q3）的定量影响未与 DIF detection rate 关联——DEFF 处理 family-level，Q3 是 item-level\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W5。两个层面的非独立性（model-level clustering vs item-level local dependence）需分别处理。\"\n    action_items:\n      - round: 15\n        action: \"量化 item-level LD 对 MH-DIF false detection rate 的贡献，或讨论为何 DEFF 足以处理两层面\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W6\"\n    summary: \"遗漏 concurrent work：CoDeC（ICLR 2026）\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W1 提出，R1 AGREE（需核实时间线）。CoDeC 使用 in-context learning 检测污染，属 global exposure 范畴。\"\n    action_items:\n      - round: 15\n        action: \"核实 CoDeC 发表时间线；如在本文投稿前公开则加入 §2\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W7\"\n    summary: \"可操作性缺口：DIF 是 mechanism-agnostic 但推荐 mechanism-conditional responses，缺判断标准\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-W3 提出，R1 AGREE with nuance。R1 建议增加简要决策启发式而非完整框架。\"\n    action_items:\n      - round: 15\n        action: \"§5.2 增加 1-2 句决策启发式（如 |Δ_MH|>2.0 + web-overlap → prioritize removal）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-I1\"\n    summary: \"'两维度正交'作为 Contribution 1 的新颖性存疑——从构念定义可预期\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2: 建议调整为 empirical confirmation\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2-N2 升级为 Must-Fix，R1 REBUT（NLP 社区未量化验证，Figure 1 有独立价值）。存在分歧：R2 认为定义可预期，R1 认为实证量化有价值。\"\n    action_items:\n      - round: 15\n        action: \"将 Contribution 1 从 'discovery' 调整为 'empirical quantification of a theoretically expected but previously unverified distinction'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-I2\"\n    summary: \"视觉节奏不均：p3-6 连续 4 页无 figure/table，p7 堆积 3 个 display items\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"视觉审查 Agent 发现。建议将 Table 1 或 Figure 2 提前至 §3-4 附近。\"\n    action_items:\n      - round: 15\n        action: \"调整 figure/table placement 平衡视觉节奏\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 14 issues（状态更新） ===\n\n  - id: \"R14-W1\"\n    summary: \"Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷，但 DIF 无法区分 contamination / capability evolution / composition shift\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M1 + R2-W-F1 + R2-W-F2 共识。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"本轮未作为独立 issue 提出，但 R15-N3 (overclaiming) 和 R15-I1 (两维度) 涉及相同 framing 层面。论文已引入 Camilli impact-vs-bias、composition control (Δ=1.08pp)、within-arch DIF。部分改善但 R15 仍有 framing 问题。\"\n    action_items:\n      - round: 14\n        action: \"综合重写 framing\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W2\"\n    summary: \"DEFF 估计范围过宽\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2\"\n      - round: 15\n        reviewers: [1]\n        note: \"Merged into R15-N1, 升级为 critical\"\n    action_items: []\n    resolution: \"Superseded by R15-N1\"\n    resolution_round: null\n\n  - id: \"R14-W3\"\n    summary: \"Semi-synthetic 注入模型生态效度有限\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-N2, 升级为 critical\"\n    action_items: []\n    resolution: \"Superseded by R15-N2\"\n    resolution_round: null\n\n  - id: \"R14-W4\"\n    summary: \"缺少 base/instruct composition shift 的直接控制\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W4\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未被单独提出。论文已增加 App O composition control (Δ=1.08pp) 和 §5.1 讨论。可能已部分修复。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W5\"\n    summary: \"\\\\enlargethispage 使用激进\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W5\"\n      - round: 15\n        reviewers: [2]\n        note: \"R2 小问题中提到 discussion.tex 中有 \\\\enlargethispage*{4\\\\baselineskip}。较 R14 的 6\\\\baselineskip 有改善。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W6\"\n      - round: 15\n        reviewers: [2]\n        note: \"R2 小问题中提到 measurement invariance / temporal score incomparability 仍有混用。有改善但未完全统一。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-N3, 升级为 critical\"\n    action_items: []\n    resolution: \"Superseded by R15-N3\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"Conclusion 仅 4 句话\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W8\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未被单独提出。可能已改善。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N1\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N1\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未被单独提出。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"'两个维度'框架正交性可能是概念上预期的结果\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 15\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-I1, R2 升级为 Must-Fix, R1 REBUT. 存在分歧。\"\n    action_items: []\n    resolution: \"Superseded by R15-I1\"\n    resolution_round: null\n\n  # === Round 13 issues（状态更新） ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W1\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W1\"\n      - round: 15\n        reviewers: []\n        note: \"本轮未作为独立 issue 提出。论文已大幅改善 framing（引入 mechanism-agnostic diagnostic 定位、exclusion arguments、base-vs-instruct decomposition）。但 R15-N3 和 R15-W7 仍涉及相关层面。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定条件\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2\"\n      - round: 14\n        reviewers: []\n        note: \"已有 k≤5 限定\"\n    action_items: []\n    resolution: \"Contribution 2 已写为 'ΔFPR = 0 under single-subject contamination, k ≤ 5'。R14/R15 未再提出。\"\n    resolution_round: 14\n\n  # === 历史 issues（已 resolved，保留追踪） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Size-stratified DEFF table added. Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法未定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Formal definition in app:dedup_k.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Reframed as 'Orthogonal constructs'.\"\n    resolution_round: 19\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Difficulty-dependent injection results written to paper.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as exploratory. R15 再次提出正文仍用 confirms 语气 (R15-W4)。\"\n    resolution_round: 20"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-23T09:27:49.727869+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 15341}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1423 · 2026-05-23T09:30:39.395393+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# Round 15 审稿报告\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 via ARR (Long paper, 8-page limit)\n**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + Related Work）\n**轮次**: Round 1（Fresh 模式，无历史上下文）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）进行大规模时序审计。核心发现：2023 与 2024 模型队列间约 27–31% 的 MMLU 题目表现出时序 DIF，且此信号与 web-overlap 污染标签经验上正交（Jaccard ≈ 0.206）。论文提出 cross-subject matching 策略处理多学科污染，用 semi-synthetic injection 验证检测能力，在 6 个 benchmark 上做了交叉验证，并发现 base 和 instruct 模型呈现相反 DIF 模式（χ² = 562.7）。\n\n---\n\n## Strengths\n\n**S1** [共识] **问题的重要性和规模**：LLM benchmark 分数的跨时间可比性被广泛假设但很少被系统验证。5,227 模型 × 12,508 题目的审计规模在 DIF 文献中前所未有，6 个 benchmark 的交叉验证增强了发现的普遍性。\n\n**S2** [共识] **实验控制链的完整性**：随机分割对照（C%=0.18%）、能力匹配控制（C%=28.9%±0.1%）、LOFO 家族稳健性（|ΔC%|≤2.93pp）、DEFF 非独立性修正、graduated de-duplication、cluster bootstrap——每个潜在混淆因素都有对应的控制实验。\n\n**S3** [共识] **Base-vs-instruct 反转模式**：χ²=562.7 的方向反转是论文最有洞见的发现。Base 模型 60.1% reference-favoring（ρ=-0.570），instruct 模型 65.6% focal-favoring（ρ=-0.079），表明 DIF 信号具有结构性，与训练方法论差异关联。\n\n**S4** [R1] **Cross-subject matching 的实质性适配**：识别出 LLM multi-domain benchmark 中 matching variable 被污染的问题，提出用其他学科总分隔离单学科污染，并提供 ΔFPR=0 的结构性保证（k≤5）。\n\n**S5** [共识] **与 Growing Pains 的互补定位**：\"诊断先于等值校准\"的定位合理，论文的 stable-item set 可直接作为 anchor item candidates。\n\n**S6** [共识] **写作质量与可复现性**：8 页内清晰呈现复杂方法论框架，提供匿名代码仓库，使用公开数据集，附录组织有序。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [共识] **DEFF 校正两种估计量差异 2 倍，选择理由不充分**\n- Simple-mean DEFF: adjusted C% = 29.2%; weighted-mean DEFF: adjusted C% = 13.5%\n- Cluster bootstrap 95% CI [26.7%, 53.2%] 跨度 26.5pp\n- 论文以 simple-mean 为主报告值（\"≈27–29%\"），但 weighted-mean 是统计学中更标准的处理方式\n- App I 的 DEFF simulation 支持 simple-mean 但论证链未在正文展开\n- **核心影响**：论文的 headline claim（\"≈27–29% of MMLU items exhibit temporal DIF\"）直接依赖此选择。如果 weighted-mean 更合理，核心数字缩减至 13.5%——仍有意义但 narrative 需调整\n- **历史追踪**：R13-W2 → R14-W2 → R15-N1，连续 3 轮被提出\n\n**MF2** [共识] **Semi-synthetic 验证使用 uniform binary flipping，检测力标定外部效度受限**\n- Uniform flipping 产生均匀信号，可能是 easiest-to-detect case 而非 worst-case\n- 真实污染涉及部分记忆、格式特定优势、能力依赖效应——效应大小因题目难度和模型能力而异\n- 论文将其定位为\"upper-bound estimate\"不完全准确：uniform flipping 可能高估 TPR\n- ΔTPR=+0.508 at p=0.5（Figure 2）是核心检测力证据，但在真实污染下可能显著更低\n- **核心影响**：如果检测力在真实场景下大幅下降，\"500 模型即可审计\"的实用建议可能不成立\n- **历史追踪**：R13-W3 → R14-W3 → R15-N2，连续 3 轮被提出\n\n**MF3** [R2 提出, R1 AGREE with nuance] **框架贡献被过度声称**\n- Introduction Contribution 3 列\"Temporal DIF audit framework\"为独立贡献\n- 但 Section 2 写道\"We do not modify the MH procedure; our contribution is the application context\"——两处措辞矛盾\n- 三项技术组件逐项审视：cross-subject matching = purified subtest matching 适配；DEFF = 调查方法学标准技术；semi-synthetic = 最简二值翻转注入\n- R1 认为 cross-subject matching 在 LLM 语境下有实质性考量（ΔFPR=0 保证），但不构成方法创新\n- **建议**：重述为\"methodological adaptations enabling valid DIF in LLM setting\"\n- **历史追踪**：R13-W6 → R14-W7 → R15-N3，连续 3 轮\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [R1] **ETS 阈值移植合理性未论证**：|Δ_MH| ≥ 1.5 源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity 分析有用但不等于论证适切性。\n\n**SF2** [R1] **N=5,227 下 p-value 失去区分力**：BH-FDR 仅移除 3/3918 items 说明几乎所有 p-value 极小。ETS C 的 p<0.05 条件在此规模下自动满足，等同于仅用效应量筛选。论文已有 DEFF 恢复 p-value selectivity（269 items 失显著性），但正文讨论不足。\n\n**SF3** [R1] **Within-family DIF 解释有误**：Llama-2 vs Llama-3（C%=59.2%）中架构/规模/训练数据差异与时间效应完全混淆。App N 的解释逻辑（\"confirming temporal DIF not artifact of architecture\"）可能相反——C% 更高可能因架构差异叠加时间效应。\n\n**SF4** [R1] **GSM1K 相关性过度解读**：r=-0.478, N=33，Figure 5 caption 标 exploratory 但正文用 \"confirms\" 语气。应统一 exploratory 定位，报告 CI。\n\n**SF5** [R1] **Local independence 违反定量影响缺失**：DEFF 处理 family-level clustering（模型间），Yen's Q3 反映 item-level local dependence（题目间）——两个不同层面的非独立性。论文未量化 item-level LD 对 DIF detection rate 的具体贡献。\n\n**SF6** [共识] **遗漏 concurrent work CoDeC（ICLR 2026）**：使用 in-context learning 检测污染，属 global exposure 范畴，与本文 DIF 方法形成有趣对比。\n\n**SF7** [R2 提出, R1 AGREE with nuance] **可操作性缺口**：DIF 是 mechanism-agnostic 的（Section 5.1 反复强调），但 Section 5.2 推荐 \"mechanism-conditional responses\"——实践者缺乏判断标准。建议增加简要决策启发式。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n\n1. **[AGREE] Semi-synthetic 验证生态效度不足**：两位独立识别 uniform binary flipping 的局限性。R1 列为 Must-Fix (N2)，R2 列为 Should-Fix (W2)，R1 交叉回应 AGREE。取共识严重度：Must-Fix。\n\n2. **[AGREE] 框架贡献需降调**：R2 列为 Must-Fix (N1)，R1 AGREE with nuance——承认技术组件非原创，但认为 cross-subject matching 的 LLM 适配有实质考量。共识：重述 framing 但保留应用贡献。\n\n3. **[AGREE] 遗漏 CoDeC**：R2 提出，R1 同意（需核实时间线）。\n\n4. **[AGREE] 可操作性缺口可通过简要启发式解决**：R2 提出缺口，R1 同意但认为 DIF 本质是诊断工具，不必须解决所有下游问题。\n\n5. **[AGREE] 实验控制链完整、base-vs-instruct 反转模式是核心亮点**：两位在优势评估上高度一致。\n\n---\n\n## Reviewer Divergence\n\n以下问题两位 Reviewer 存在分歧：\n\n1. **[DIVERGE] \"两维度正交\"的新颖性**\n   - R2 (N2, Must-Fix)：Global exposure 和 differential functioning 在定义层面就是不同维度，低相关是预期结果，不构成 surprising finding。\n   - R1 (REBUT)：概念区分在心理测量学中不新，但在 NLP 社区中未被量化验证。现有 contamination detection 文献隐含假设\"暴露=失真\"，论文用大规模数据量化了这一假设的不成立。Figure 1 的经验证据有独立价值。\n   - **Director 判断**：R1 的反驳有说服力——NLP 社区确实未系统区分这两个概念。但 R2 的批评也合理——从心理测量学视角这不意外。建议折中：将 Contribution 1 从\"discovery\"调整为\"empirical quantification of a theoretically expected but previously unverified distinction\"。降级为 info 而非 Must-Fix。\n\n2. **[DIVERGE] 非 MMLU 基准分析深度**\n   - R2 (W4)：标题说 \"Psychometric Audit\"，但 5 个非 MMLU 基准仅各占 Table 3 一行，无结构分析。\n   - R1 (REBUT)：MMLU 是 primary analysis，cross-benchmark 是 replication check。8 页限制下深度优于广度。\n   - **Director 判断**：R1 的论点更有说服力。Cross-benchmark 作为 replication 已足够，不必每个 benchmark 都做完整分析。记录为 info。\n\n3. **[DIVERGE] 标题 \"5,227 Models\"**\n   - R2 (W5)：核心时序分析仅用 1,887 模型。\n   - R1 (REBUT)：5,227 描述审计范围（response matrix 规模），各 cohort N 值在 Section 3.3 清楚列出。\n   - **Director 判断**：R1 的反驳成立。5,227 是数据集规模，不同分析使用不同子集在论文中已明确交代。不构成问题。\n\n---\n\n## Questions\n\n1. [R2] 如果仅对 base 模型或仅对 instruct 模型做时序 DIF 分析，C% 分别是多少？这能否分离 temporal 和 training methodology 成分？\n2. [R2] Aggregate ranking ρ≈0.997 意味着对排名用途 DIF 影响可忽略。DIF 监测的实际应用场景是分数校准还是科学理解？如果主要是后者，\"practical audit protocol\"的定位是否需要调整？\n3. [R2] 按季度或模型发布时间做更细粒度分割，DIF 率如何演变？\n4. [R1] 为什么不使用 data-driven 方法（如 permutation-based null）确定 LLM-specific 的 DIF 阈值？\n5. [R1] Item-level local dependence（Q3 > 0.20 的 11.3% within-subject pairs）对 MH-DIF false detection rate 的定量贡献是多少？\n\n---\n\n## Missing References\n\n1. **CoDeC** (ICLR 2026) — Detecting Data Contamination in LLMs via In-Context Learning。重要的最新污染检测方法，属 global exposure 范畴。[R2 提出, R1 AGREE]\n2. **JE-IRT** (arXiv 2509.22888) — Joint Embedding Item Response Theory。将 IRT 与表示学习结合。[R2]\n3. **PaCoST** (arXiv 2406.18326) — Paired Confidence Significance Testing。另一种污染检测方法。[R2]\n4. 引用格式问题：`suk2026causal` 标注 \"Forthcoming\" in Psychometrika，审稿人无法验证。建议提供 preprint 链接。[R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-23 09:10 → 09:13，耗时 ~3 分钟）\n\n**Findings（2 warning, 12 info）**:\n\n- ⚠️ **视觉节奏不均**：p3-6 连续 4 页无 figure/table（Method §3 和 Experiments 开头全为纯文本），p7 堆积 3 个 display items（Table 1 + Figure 2 + Table 2）。建议将至少 1 个 table 提前至 §3-4 附近。\n- ⚠️ **Display item 分布极端**：正文 8 页仅 5 个 display items（密度 0.625/页），实证为主的论文偏低但因兼有方法论贡献尚可接受。\n- ℹ️ Figure 1（p2 顶部）位置合理，ICC 曲线图清晰传达核心区别。\n- ℹ️ Figure 2 剂量-反应曲线带置信区间，清晰可读。\n- ℹ️ Tables 使用 booktabs 风格，格式规范。\n- ℹ️ Limitations 在 p8 底部开始，符合 EMNLP 要求。\n- ℹ️ References 无 [?] 未解析引用，无 overfull。\n- ℹ️ Appendix Figures 3-4 尺寸偏小，轴标签勉强可读。\n- ℹ️ 无 margin 溢出、公式渲染错误或 section heading 孤悬。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference（适合 Findings 或 Borderline Main Conference）\n\n**置信度**: 4 / 5（两位 Reviewer 均熟悉 DIF/IRT 方法论和 LLM 评估文献）\n\n**详细评判**:\n\n这是一篇有实质贡献的大规模实证研究。核心发现（31% temporal DIF rate, web-overlap 正交性, base-vs-instruct 反转模式 χ²=562.7）在多重控制下成立，对 LLM 评估社区有实用价值。实验控制链的完整性是论文的突出优势——几乎每个潜在混淆因素都有对应的控制实验。\n\n主要弱点集中在三个层面：\n\n1. **统计选择的透明度**（MF1）：DEFF 校正的两种估计量导致核心数字存在 2 倍分歧（13.5% vs 29.2%），这一选择直接决定论文的 headline claim 强度。论文倾向 simple-mean 但论证不充分，且此问题已连续 3 轮被提出。\n\n2. **验证框架的生态效度**（MF2）：Semi-synthetic injection 的 uniform binary flipping 可能高估而非保守估计检测力。两位 Reviewer 一致认为这削弱了检测能力标定的可信度。同样连续 3 轮被提出。\n\n3. **贡献声称的校准**（MF3）：方法论贡献（Contribution 3）与论文自身在 Section 2 的定位存在张力。建议降调为\"领域适配\"而非\"框架创新\"。\n\n这三个问题均可在修订中解决，不构成根本性缺陷。如果作者能在修订中（1）并列呈现 DEFF 两种估计并充分论证选择、（2）增加更现实的注入模型或更准确描述 uniform flipping 的性质、（3）调整 Contribution 3 的声称力度，论文可达到 Conference 水准。\n\n**ARR 评分对照**：3.5 = Borderline Conference。Excitement 3-4/5（问题重要但方法论创新有限），Soundness 3.5-4/5（实验严谨但统计选择需进一步论证）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 3 与 Section 2 \"We do not modify the MH procedure\" 矛盾。建议重述为 \"methodological adaptations\" 而非 \"framework\"。[MF3]\n- Contribution 1 \"two dimensions\" 在心理测量学中不新，但在 NLP 社区中有实证量化价值。建议调整为 \"empirical quantification of a theoretically expected distinction\"。[R2-N2 vs R1 REBUT，分歧降级为建议]\n\n### Section 3.2 (MH-DIF and ETS Classification)\n- ETS 阈值 |Δ_MH| ≥ 1.5 从人类考生直接移植，未论证在 LLM 语境下的适切性。[SF1]\n- 在 N=5,227 下 p < 0.05 条件几乎自动满足（仅 3/3,918 items 未通过 BH-FDR），应讨论 p-value 在此规模下的实际角色。论文已有 DEFF 恢复 p-value selectivity 的证据（269 items 失显著性），但正文讨论不足。[SF2]\n\n### Section 3.4 (Semi-Synthetic Injection)\n- \"worst-case uniform injection pattern\" 描述不准确。Uniform flipping 可能是 easiest-to-detect 而非 worst-case。建议改为 \"stylized\" 或 \"simplified\"。[MF2]\n- ΔFPR=0 的结构性保证（k≤5）已正确限定条件。\n\n### Section 4.2 (Temporal DIF)\n- 正文以 \"≈27–29%\" 为主报告值，但 weighted-mean DEFF 给出 13.5%。建议并列呈现两种估计并解释差异原因（mega-family 低 ICC 导致 weighted-mean 过度校正）。[MF1]\n- Cluster bootstrap CI [26.7%, 53.2%] 极宽，应讨论驱动因素（bootstrap resample 中 Mistral/Llama-3 过度代表）。[MF1]\n\n### Section 4.3 (Ground Truth Mismatch)\n- 两维度正交性的呈现可调整为\"empirical confirmation\"而非\"discovery\"。[R2-N2, 分歧降级]\n\n### Section 4.7 (Cross-Benchmark)\n- GSM1K 相关性（r=-0.478, N=33）在 Figure 5 caption 标 exploratory 但正文用 \"confirms\" 语气，应统一。[SF4]\n- 非 MMLU 基准仅 Table 3 一行——作为 replication check 足够，但可考虑增加 1 个基准的简要结构分析。[R2-W4, R1 REBUT, 分歧降级为建议]\n\n### Section 5.1 (Discussion)\n- Base-vs-instruct 反转模式讨论充分。Camilli impact-vs-bias framework 引入恰当。\n- Composition control (Δ=1.08pp) 结果有效排除了 confound。\n\n### Section 5.2 (Audit Protocol)\n- \"Mechanism-conditional responses\" 缺乏判断标准。建议增加 1-2 句决策启发式。[SF7]\n\n### Appendix\n- Within-family DIF (App N): Llama-2 vs 3 的 C%=59.2% 不能解释为 \"confirming temporal DIF not artifact of architecture\"——逻辑可能相反。建议重新框架化。[SF3]\n- Local independence (App A.1): Q3 诊断发现 11.3% within-subject pairs 超阈值，但未量化其对 DIF detection rate 的贡献。DEFF 处理 family-level 而非 item-level 非独立性。[SF5]\n- Appendix Figures 3-4 尺寸偏小，建议放大或使用 figure* 全宽展示。[Visual Check]\n\n### 格式\n- `\\enlargethispage*{4\\baselineskip}` 在 discussion.tex 中仍存在，较 R14 的 6\\baselineskip 有改善。\n- 正文 8 页，符合 EMNLP 限制。Limitations 在正文中，符合要求。\n- 术语 \"measurement invariance\" / \"temporal score incomparability\" 仍有少量混用，建议进一步统一。\n- 匿名性：脚注 1 提供匿名代码链接，满足 double-blind。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# Round 15 审稿报告\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 via ARR (Long paper, 8-page limit)\n**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + Related Work）\n**轮次**: Round 1（Fresh 模式，无历史上下文）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）进行大规模时序审计。核心发现：2023 与 2024 模型队列间约 27–31% 的 MMLU 题目表现出时序 DIF，且此信号与 web-overlap 污染标签经验上正交（Jaccard ≈ 0.206）。论文提出 cross-subject matching 策略处理多学科污染，用 semi-synthetic injection 验证检测能力，在 6 个 benchmark 上做了交叉验证，并发现 base 和 instruct 模型呈现相反 DIF 模式（χ² = 562.7）。\n\n---\n\n## Strengths\n\n**S1** [共识] **问题的重要性和规模**：LLM benchmark 分数的跨时间可比性被广泛假设但很少被系统验证。5,227 模型 × 12,508 题目的审计规模在 DIF 文献中前所未有，6 个 benchmark 的交叉验证增强了发现的普遍性。\n\n**S2** [共识] **实验控制链的完整性**：随机分割对照（C%=0.18%）、能力匹配控制（C%=28.9%±0.1%）、LOFO 家族稳健性（|ΔC%|≤2.93pp）、DEFF 非独立性修正、graduated de-duplication、cluster bootstrap——每个潜在混淆因素都有对应的控制实验。\n\n**S3** [共识] **Base-vs-instruct 反转模式**：χ²=562.7 的方向反转是论文最有洞见的发现。Base 模型 60.1% reference-favoring（ρ=-0.570），instruct 模型 65.6% focal-favoring（ρ=-0.079），表明 DIF 信号具有结构性，与训练方法论差异关联。\n\n**S4** [R1] **Cross-subject matching 的实质性适配**：识别出 LLM multi-domain benchmark 中 matching variable 被污染的问题，提出用其他学科总分隔离单学科污染，并提供 ΔFPR=0 的结构性保证（k≤5）。\n\n**S5** [共识] **与 Growing Pains 的互补定位**：\"诊断先于等值校准\"的定位合理，论文的 stable-item set 可直接作为 anchor item candidates。\n\n**S6** [共识] **写作质量与可复现性**：8 页内清晰呈现复杂方法论框架，提供匿名代码仓库，使用公开数据集，附录组织有序。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [共识] **DEFF 校正两种估计量差异 2 倍，选择理由不充分**\n- Simple-mean DEFF: adjusted C% = 29.2%; weighted-mean DEFF: adjusted C% = 13.5%\n- Cluster bootstrap 95% CI [26.7%, 53.2%] 跨度 26.5pp\n- 论文以 simple-mean 为主报告值（\"≈27–29%\"），但 weighted-mean 是统计学中更标准的处理方式\n- App I 的 DEFF simulation 支持 simple-mean 但论证链未在正文展开\n- **核心影响**：论文的 headline claim（\"≈27–29% of MMLU items exhibit temporal DIF\"）直接依赖此选择。如果 weighted-mean 更合理，核心数字缩减至 13.5%——仍有意义但 narrative 需调整\n- **历史追踪**：R13-W2 → R14-W2 → R15-N1，连续 3 轮被提出\n\n**MF2** [共识] **Semi-synthetic 验证使用 uniform binary flipping，检测力标定外部效度受限**\n- Uniform flipping 产生均匀信号，可能是 easiest-to-detect case 而非 worst-case\n- 真实污染涉及部分记忆、格式特定优势、能力依赖效应——效应大小因题目难度和模型能力而异\n- 论文将其定位为\"upper-bound estimate\"不完全准确：uniform flipping 可能高估 TPR\n- ΔTPR=+0.508 at p=0.5（Figure 2）是核心检测力证据，但在真实污染下可能显著更低\n- **核心影响**：如果检测力在真实场景下大幅下降，\"500 模型即可审计\"的实用建议可能不成立\n- **历史追踪**：R13-W3 → R14-W3 → R15-N2，连续 3 轮被提出\n\n**MF3** [R2 提出, R1 AGREE with nuance] **框架贡献被过度声称**\n- Introduction Contribution 3 列\"Temporal DIF audit framework\"为独立贡献\n- 但 Section 2 写道\"We do not modify the MH procedure; our contribution is the application context\"——两处措辞矛盾\n- 三项技术组件逐项审视：cross-subject matching = purified subtest matching 适配；DEFF = 调查方法学标准技术；semi-synthetic = 最简二值翻转注入\n- R1 认为 cross-subject matching 在 LLM 语境下有实质性考量（ΔFPR=0 保证），但不构成方法创新\n- **建议**：重述为\"methodological adaptations enabling valid DIF in LLM setting\"\n- **历史追踪**：R13-W6 → R14-W7 → R15-N3，连续 3 轮\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [R1] **ETS 阈值移植合理性未论证**：|Δ_MH| ≥ 1.5 源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity 分析有用但不等于论证适切性。\n\n**SF2** [R1] **N=5,227 下 p-value 失去区分力**：BH-FDR 仅移除 3/3918 items 说明几乎所有 p-value 极小。ETS C 的 p<0.05 条件在此规模下自动满足，等同于仅用效应量筛选。论文已有 DEFF 恢复 p-value selectivity（269 items 失显著性），但正文讨论不足。\n\n**SF3** [R1] **Within-family DIF 解释有误**：Llama-2 vs Llama-3（C%=59.2%）中架构/规模/训练数据差异与时间效应完全混淆。App N 的解释逻辑（\"confirming temporal DIF not artifact of architecture\"）可能相反——C% 更高可能因架构差异叠加时间效应。\n\n**SF4** [R1] **GSM1K 相关性过度解读**：r=-0.478, N=33，Figure 5 caption 标 exploratory 但正文用 \"confirms\" 语气。应统一 exploratory 定位，报告 CI。\n\n**SF5** [R1] **Local independence 违反定量影响缺失**：DEFF 处理 family-level clustering（模型间），Yen's Q3 反映 item-level local dependence（题目间）——两个不同层面的非独立性。论文未量化 item-level LD 对 DIF detection rate 的具体贡献。\n\n**SF6** [共识] **遗漏 concurrent work CoDeC（ICLR 2026）**：使用 in-context learning 检测污染，属 global exposure 范畴，与本文 DIF 方法形成有趣对比。\n\n**SF7** [R2 提出, R1 AGREE with nuance] **可操作性缺口**：DIF 是 mechanism-agnostic 的（Section 5.1 反复强调），但 Section 5.2 推荐 \"mechanism-conditional responses\"——实践者缺乏判断标准。建议增加简要决策启发式。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n\n1. **[AGREE] Semi-synthetic 验证生态效度不足**：两位独立识别 uniform binary flipping 的局限性。R1 列为 Must-Fix (N2)，R2 列为 Should-Fix (W2)，R1 交叉回应 AGREE。取共识严重度：Must-Fix。\n\n2. **[AGREE] 框架贡献需降调**：R2 列为 Must-Fix (N1)，R1 AGREE with nuance——承认技术组件非原创，但认为 cross-subject matching 的 LLM 适配有实质考量。共识：重述 framing 但保留应用贡献。\n\n3. **[AGREE] 遗漏 CoDeC**：R2 提出，R1 同意（需核实时间线）。\n\n4. **[AGREE] 可操作性缺口可通过简要启发式解决**：R2 提出缺口，R1 同意但认为 DIF 本质是诊断工具，不必须解决所有下游问题。\n\n5. **[AGREE] 实验控制链完整、base-vs-instruct 反转模式是核心亮点**：两位在优势评估上高度一致。\n\n---\n\n## Reviewer Divergence\n\n以下问题两位 Reviewer 存在分歧：\n\n1. **[DIVERGE] \"两维度正交\"的新颖性**\n   - R2 (N2, Must-Fix)：Global exposure 和 differential functioning 在定义层面就是不同维度，低相关是预期结果，不构成 surprising finding。\n   - R1 (REBUT)：概念区分在心理测量学中不新，但在 NLP 社区中未被量化验证。现有 contamination detection 文献隐含假设\"暴露=失真\"，论文用大规模数据量化了这一假设的不成立。Figure 1 的经验证据有独立价值。\n   - **Director 判断**：R1 的反驳有说服力——NLP 社区确实未系统区分这两个概念。但 R2 的批评也合理——从心理测量学视角这不意外。建议折中：将 Contribution 1 从\"discovery\"调整为\"empirical quantification of a theoretically expected but previously unverified distinction\"。降级为 info 而非 Must-Fix。\n\n2. **[DIVERGE] 非 MMLU 基准分析深度**\n   - R2 (W4)：标题说 \"Psychometric Audit\"，但 5 个非 MMLU 基准仅各占 Table 3 一行，无结构分析。\n   - R1 (REBUT)：MMLU 是 primary analysis，cross-benchmark 是 replication check。8 页限制下深度优于广度。\n   - **Director 判断**：R1 的论点更有说服力。Cross-benchmark 作为 replication 已足够，不必每个 benchmark 都做完整分析。记录为 info。\n\n3. **[DIVERGE] 标题 \"5,227 Models\"**\n   - R2 (W5)：核心时序分析仅用 1,887 模型。\n   - R1 (REBUT)：5,227 描述审计范围（response matrix 规模），各 cohort N 值在 Section 3.3 清楚列出。\n   - **Director 判断**：R1 的反驳成立。5,227 是数据集规模，不同分析使用不同子集在论文中已明确交代。不构成问题。\n\n---\n\n## Questions\n\n1. [R2] 如果仅对 base 模型或仅对 instruct 模型做时序 DIF 分析，C% 分别是多少？这能否分离 temporal 和 training methodology 成分？\n2. [R2] Aggregate ranking ρ≈0.997 意味着对排名用途 DIF 影响可忽略。DIF 监测的实际应用场景是分数校准还是科学理解？如果主要是后者，\"practical audit protocol\"的定位是否需要调整？\n3. [R2] 按季度或模型发布时间做更细粒度分割，DIF 率如何演变？\n4. [R1] 为什么不使用 data-driven 方法（如 permutation-based null）确定 LLM-specific 的 DIF 阈值？\n5. [R1] Item-level local dependence（Q3 > 0.20 的 11.3% within-subject pairs）对 MH-DIF false detection rate 的定量贡献是多少？\n\n---\n\n## Missing References\n\n1. **CoDeC** (ICLR 2026) — Detecting Data Contamination in LLMs via In-Context Learning。重要的最新污染检测方法，属 global exposure 范畴。[R2 提出, R1 AGREE]\n2. **JE-IRT** (arXiv 2509.22888) — Joint Embedding Item Response Theory。将 IRT 与表示学习结合。[R2]\n3. **PaCoST** (arXiv 2406.18326) — Paired Confidence Significance Testing。另一种污染检测方法。[R2]\n4. 引用格式问题：`suk2026causal` 标注 \"Forthcoming\" in Psychometrika，审稿人无法验证。建议提供 preprint 链接。[R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-23 09:10 → 09:13，耗时 ~3 分钟）\n\n**Findings（2 warning, 12 info）**:\n\n- ⚠️ **视觉节奏不均**：p3-6 连续 4 页无 figure/table（Method §3 和 Experiments 开头全为纯文本），p7 堆积 3 个 display items（Table 1 + Figure 2 + Table 2）。建议将至少 1 个 table 提前至 §3-4 附近。\n- ⚠️ **Display item 分布极端**：正文 8 页仅 5 个 display items（密度 0.625/页），实证为主的论文偏低但因兼有方法论贡献尚可接受。\n- ℹ️ Figure 1（p2 顶部）位置合理，ICC 曲线图清晰传达核心区别。\n- ℹ️ Figure 2 剂量-反应曲线带置信区间，清晰可读。\n- ℹ️ Tables 使用 booktabs 风格，格式规范。\n- ℹ️ Limitations 在 p8 底部开始，符合 EMNLP 要求。\n- ℹ️ References 无 [?] 未解析引用，无 overfull。\n- ℹ️ Appendix Figures 3-4 尺寸偏小，轴标签勉强可读。\n- ℹ️ 无 margin 溢出、公式渲染错误或 section heading 孤悬。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference（适合 Findings 或 Borderline Main Conference）\n\n**置信度**: 4 / 5（两位 Reviewer 均熟悉 DIF/IRT 方法论和 LLM 评估文献）\n\n**详细评判**:\n\n这是一篇有实质贡献的大规模实证研究。核心发现（31% temporal DIF rate, web-overlap 正交性, base-vs-instruct 反转模式 χ²=562.7）在多重控制下成立，对 LLM 评估社区有实用价值。实验控制链的完整性是论文的突出优势——几乎每个潜在混淆因素都有对应的控制实验。\n\n主要弱点集中在三个层面：\n\n1. **统计选择的透明度**（MF1）：DEFF 校正的两种估计量导致核心数字存在 2 倍分歧（13.5% vs 29.2%），这一选择直接决定论文的 headline claim 强度。论文倾向 simple-mean 但论证不充分，且此问题已连续 3 轮被提出。\n\n2. **验证框架的生态效度**（MF2）：Semi-synthetic injection 的 uniform binary flipping 可能高估而非保守估计检测力。两位 Reviewer 一致认为这削弱了检测能力标定的可信度。同样连续 3 轮被提出。\n\n3. **贡献声称的校准**（MF3）：方法论贡献（Contribution 3）与论文自身在 Section 2 的定位存在张力。建议降调为\"领域适配\"而非\"框架创新\"。\n\n这三个问题均可在修订中解决，不构成根本性缺陷。如果作者能在修订中（1）并列呈现 DEFF 两种估计并充分论证选择、（2）增加更现实的注入模型或更准确描述 uniform flipping 的性质、（3）调整 Contribution 3 的声称力度，论文可达到 Conference 水准。\n\n**ARR 评分对照**：3.5 = Borderline Conference。Excitement 3-4/5（问题重要但方法论创新有限），Soundness 3.5-4/5（实验严谨但统计选择需进一步论证）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 3 与 Section 2 \"We do not modify the MH procedure\" 矛盾。建议重述为 \"methodological adaptations\" 而非 \"framework\"。[MF3]\n- Contribution 1 \"two dimensions\" 在心理测量学中不新，但在 NLP 社区中有实证量化价值。建议调整为 \"empirical quantification of a theoretically expected distinction\"。[R2-N2 vs R1 REBUT，分歧降级为建议]\n\n### Section 3.2 (MH-DIF and ETS Classification)\n- ETS 阈值 |Δ_MH| ≥ 1.5 从人类考生直接移植，未论证在 LLM 语境下的适切性。[SF1]\n- 在 N=5,227 下 p < 0.05 条件几乎自动满足（仅 3/3,918 items 未通过 BH-FDR），应讨论 p-value 在此规模下的实际角色。论文已有 DEFF 恢复 p-value selectivity 的证据（269 items 失显著性），但正文讨论不足。[SF2]\n\n### Section 3.4 (Semi-Synthetic Injection)\n- \"worst-case uniform injection pattern\" 描述不准确。Uniform flipping 可能是 easiest-to-detect 而非 worst-case。建议改为 \"stylized\" 或 \"simplified\"。[MF2]\n- ΔFPR=0 的结构性保证（k≤5）已正确限定条件。\n\n### Section 4.2 (Temporal DIF)\n- 正文以 \"≈27–29%\" 为主报告值，但 weighted-mean DEFF 给出 13.5%。建议并列呈现两种估计并解释差异原因（mega-family 低 ICC 导致 weighted-mean 过度校正）。[MF1]\n- Cluster bootstrap CI [26.7%, 53.2%] 极宽，应讨论驱动因素（bootstrap resample 中 Mistral/Llama-3 过度代表）。[MF1]\n\n### Section 4.3 (Ground Truth Mismatch)\n- 两维度正交性的呈现可调整为\"empirical confirmation\"而非\"discovery\"。[R2-N2, 分歧降级]\n\n### Section 4.7 (Cross-Benchmark)\n- GSM1K 相关性（r=-0.478, N=33）在 Figure 5 caption 标 exploratory 但正文用 \"confirms\" 语气，应统一。[SF4]\n- 非 MMLU 基准仅 Table 3 一行——作为 replication check 足够，但可考虑增加 1 个基准的简要结构分析。[R2-W4, R1 REBUT, 分歧降级为建议]\n\n### Section 5.1 (Discussion)\n- Base-vs-instruct 反转模式讨论充分。Camilli impact-vs-bias framework 引入恰当。\n- Composition control (Δ=1.08pp) 结果有效排除了 confound。\n\n### Section 5.2 (Audit Protocol)\n- \"Mechanism-conditional responses\" 缺乏判断标准。建议增加 1-2 句决策启发式。[SF7]\n\n### Appendix\n- Within-family DIF (App N): Llama-2 vs 3 的 C%=59.2% 不能解释为 \"confirming temporal DIF not artifact of architecture\"——逻辑可能相反。建议重新框架化。[SF3]\n- Local independence (App A.1): Q3 诊断发现 11.3% within-subject pairs 超阈值，但未量化其对 DIF detection rate 的贡献。DEFF 处理 family-level 而非 item-level 非独立性。[SF5]\n- Appendix Figures 3-4 尺寸偏小，建议放大或使用 figure* 全宽展示。[Visual Check]\n\n### 格式\n- `\\enlargethispage*{4\\baselineskip}` 在 discussion.tex 中仍存在，较 R14 的 6\\baselineskip 有改善。\n- 正文 8 页，符合 EMNLP 限制。Limitations 在正文中，符合要求。\n- 术语 \"measurement invariance\" / \"temporal score incomparability\" 仍有少量混用，建议进一步统一。\n- 匿名性：脚注 1 提供匿名代码链接，满足 double-blind。"
  }
}
```

</details>

---


### Tool result

_source line 1424 · 2026-05-23T09:30:43.564303+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 1425 · 2026-05-23T09:30:54.855912+00:00_

审稿报告已投递。

**Round 15 审稿结果概要**：

- **Overall**: 3.5/5（Borderline Conference）
- **R1**: 3.5（Soundness 3.5, Excitement 4）
- **R2**: 3.5（Soundness 4, Excitement 3）

**3 个 Must-Fix**（均为历史反复问题，连续 3 轮被提出）：
1. DEFF 校正 2 倍估计分歧（29.2% vs 13.5%）未在正文充分论证
2. Semi-synthetic uniform flipping 可能高估检测力，生态效度不足
3. 框架贡献过度声称，与正文自述矛盾

**7 个 Should-Fix**：ETS 阈值移植、p-value 失效、within-family 解释逻辑、GSM1K 过度解读、local independence 定量缺失、遗漏 CoDeC、可操作性缺口

**核心共识**：实证贡献扎实（规模、控制链、base-vs-instruct 反转模式），方法论新颖性有限但应用价值明确。三个 Must-Fix 均可在修订中解决，不构成根本性缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 140

## Round 140

14 recorded events


### User

_source line 1426 · 2026-05-23T09:30:54.859026+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: DEFF 两种估计量差异悬殊**

同意这是一个实质性问题。Simple-mean DEFF（Adj. C%=29.2%）与 weighted-mean DEFF（Adj. C%=13.5%）之间 2 倍以上的差距确实使读者难以判断真实 C% 水平。

补充我自己的观察：
- Appendix D Table 9（size-stratified DEFF）显示 13.5% 的保守值完全由两个 mega-family（Mistral n=547, Llama-3 n=315）驱动——它们的 tier（>200 成员）DEFF=36.11，而小家族（2-10 成员）的 DEFF 仅 2.07，对应 Adj. C%=31.3%。这说明 weighted-mean 给了 mega-family 不成比例的影响力。
- Table 10（Uncertainty Quantification Comparison, Appendix E）汇总了五种方法，其中 cluster bootstrap 下界 26.7% 与 simple-mean DEFF 29.2% 确实收敛于 ~27-29%，graduated de-duplication（K=20）给出 19.7%±0.9%——落在两个 DEFF 估计之间。
- 即便取保守值 13.5%，仍是随机基线（0.18%）的 75 倍，论文的定性结论（存在大量时序 DIF）依然成立。

但 R1 的核心关切是对的：论文以 simple-mean 作为主要报告值，却没有充分论证为什么 simple-mean 比教科书推荐的 weighted-mean 更合适。Appendix D 最后一段虽有解释（"weighted-mean overcorrects by assigning excessive weight to mega-families whose low ICC does not warrant large DEFF adjustments"），但这一判断嵌入在附录深处，主文中未呈现。**建议作者在主文 Section 4.2 中明确说明选择理由，或报告一个范围（13.5%–29.2%）而非单一点估计。**

---

**[AGREE] R1-N2: Uniform flipping 可能是 easiest-to-detect 而非 worst-case**

这是 R1 最精彩的观察之一。论文在 Section 3.4 称 uniform binary flipping 为"worst-case uniform injection pattern"，但 R1 指出这里的"worst-case"是从信号强度角度说的，而非从可检测性角度。

R1 的论证逻辑是正确的：MH 统计量计算的是跨 strata 的**公共优势比**（common odds ratio, Eq. 1）。Uniform flipping 在每个 stratum 中产生方向一致、幅度相近的 odds ratio 偏移，这恰好是 MH 最擅长检测的信号结构。而真实污染可能高度非均匀——例如：
- 只在特定能力水平（如中等能力模型）上有效，在高能力模型上无效（天花板效应）
- 只在特定提示格式下有效
- 产生 non-uniform DIF（ability×group 交互），这类信号需要 logistic regression DIF 才能捕获

论文在 Appendix B 讨论了 difficulty-dependent injection（ρ≈+0.77 vs uniform 的 ρ≈-0.52），但这仍然是对所有被注入项目的均匀翻转，只是选择哪些项目注入时有了难度偏好。真正的异质性注入（不同项目不同翻转概率）未被测试。

因此，Section 3.4 的表述应当修正：ΔTPR 是在"信号结构最适配 MH 检测特性"条件下的上界估计，而非泛化意义上的 worst-case。**这实质性地影响了论文对 semi-synthetic validation 的解释力度。**

---

### Should-Fix 问题

**[AGREE] R1-W1: ETS 阈值直接移植到 LLM 的合理性未论证**

同意，但程度有限。|Δ_MH| ≥ 1.5 是 ETS 为人类考试设计的"大效应"阈值，其含义是 log odds ratio 偏移约 0.64（≈ 1.5/2.35）。对 LLM 基准来说，"大"DIF 的实际含义是什么？论文没有讨论。

不过，论文在 Section 4.2 提供了阈值敏感性分析（|Δ_MH| ≥ 2.0 时 C%=18.3%，≥ 2.5 时 C%=10.2%），证明定性结论不依赖于特定阈值。此外，论文的 random-split baseline（0.18%）提供了内部锚点：不论阈值选择如何，时序 C% 都远超随机预期。这在一定程度上缓解了阈值合理性的担忧。

**建议作者在 Section 3.2 增加一段简短讨论**：为什么在 LLM 场景下继续使用 ETS 阈值是合理的（或至少是保守的），并引用其效应量的实际含义。

---

**[REBUT] R1-W2: N=5,227 导致 p-value 自动显著**

R1 的观察虽然正确，但论文**已经显式处理了这个问题**。Section 3.2 明确写道：

> "At N=5,227, significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5: only 3 of 3,918 C items lack significance, so the dual criterion effectively reduces to a single effect-size threshold; per-item DEFF correction (Appendix D) restores p-value selectivity by reducing effective N: under simple-mean DEFF, 269 items (6.9%) lose significance while retaining |Δ_MH| ≥ 1.5."

论文不仅承认了这个问题，还通过 DEFF 修正将 effective N 降低，使得 p-value 条件重新具有筛选力（6.9% 的项目因此失去 C 分类）。这正是 DEFF 校正的设计目的。R1 在 N1 中批评 DEFF 选择，在 W2 中又批评 p-value 不起作用——但 DEFF 正是解决 W2 的工具，两者不能同时成为独立的 critical issue。

此外，论文的核心论证本来就以**效应量**（|Δ_MH| ≥ 1.5）为主，p-value 是辅助条件。在大样本 DIF 研究中，这是标准做法（Zumbo, 1999）。

---

**[AGREE] R1-W3: Within-family DIF（Llama-2 vs Llama-3）可比性存疑**

同意。Llama-2 和 Llama-3 在架构（grouped-query attention）、规模（7B-70B vs 8B-70B，新增 405B）、训练数据（2T vs 15T tokens）、以及训练方法论上都有根本性差异。将此称为"within-family"容易给读者造成误解，暗示变化只来自同一产品线的迭代，而实际上几乎等同于全新模型。

论文在 Section 5.1 用这个比较来论证"signal persists within individual lineages"（C%=59.2%）。但 59.2% 的高 DIF 率更可能反映的是两代模型间的**全面能力跃迁**（capability evolution），而非项目层面的差异化功能。Table 1 中 within-family 的 N 也相对小（161 vs 308），统计功效差异也可能贡献。

**建议作者将此比较明确标注为"cross-generation"而非"within-family"**，并降低其在论证链中的权重。

---

**[AGREE] R1-W4: GSM1K 相关性分析偏弱**

同意。r=-0.478, N=33 的相关性在统计上虽然显著（p=0.005），但：
- 33 个数据点的相关性估计极不稳定，置信区间很宽
- 论文自己也在 Section 4.7 注明"the small sample requires replication"
- 更关键的是，这个相关性的因果方向不清楚：是 contamination gap 导致 DIF，还是共同的第三变量（如模型能力水平）同时驱动两者？

论文将此结果定性为"exploratory"是恰当的。R1 的担忧在于：尽管标注了探索性，这个 r 值仍然被放在主文 Section 4.7 中作为 cross-benchmark validation 的一部分呈现，给人以比实际更强的印证感。**建议将此分析移至附录，或在主文中更明确地隔离其证据等级。**

---

**[AGREE] R1-W5: Item-level 与 family-level 非独立性是不同层面的问题**

同意这是一个概念清晰度问题。R1 正确指出：

1. **Family-level clustering**（同一模型家族内的模型高度相关）→ 用 DEFF 修正 MH χ² 的有效样本量
2. **Item-level local dependence**（同一科目内的项目共享方差）→ 用 Q3 诊断，cross-subject matching 缓解

这两者是不同维度的非独立性，可能产生不同的膨胀效应。论文分别处理了每一种，但没有讨论它们的**交互效应**。例如：如果某个模型家族在特定科目上有系统性优势（family × subject 交互），则 family-level DEFF 和 item-level Q3 会同时被触发，但各自的修正可能低估了联合效应。

Appendix C 报告了 Q3 结果（11.3% within-subject item pairs 超过 |Q3|>0.20），并声称"cross-subject matching protocol addresses this bias"。但这只处理了 matching variable 层面的 LD，没有处理 DIF 统计量本身可能因 item-level LD 而膨胀的问题。

**建议作者在 Appendix 中增加一个联合分析**：在已做 DEFF 修正的基础上，检查残差中是否仍存在 item-level LD 的系统性模式。

---

### 总结

R1 的审稿意见整体质量很高，特别是 N2（uniform flipping 的可检测性论证）和 W5（两种非独立性的区分）是精确且有建设性的技术观察。我同意 R1 的 7 条中的 6 条（程度不一），仅在 W2 上持不同意见——论文已在 Section 3.2 显式处理了大样本 p-value 问题。

两位 Reviewer 的共识问题：
1. **Semi-synthetic validation 的生态效度**（R1-N2 + R2-W2）：uniform flipping 既是上界也可能是 easiest case，这严重限制了检测力标定的可信度
2. **DEFF 估计的不确定性**（R1-N1 + R2 我也注意到了宽 CI）：13.5%–29.2% 的范围需要在主文中更透明地呈现
3. **可操作性缺口**（R2-W3 + R1 未直接提及但 N2 隐含）：如果检测力在真实场景下不确定，那么 Section 5.2 的审计协议建议也相应不确定

我维持 Overall 3.5（Borderline Conference）的评分不变。

---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

要点总结：
- R1 的 7 条意见中，我同意 6 条（N1、N2、W1、W3、W4、W5），仅在 W2（p-value 自动显著）上反驳——论文 Section 3.2 已显式处理此问题并提供 DEFF 修正
- R1-N2（uniform flipping 是 easiest-to-detect 而非 worst-case）是最精彩的观察，与我的 W2 形成共振
- 两位 Reviewer 在 semi-synthetic 生态效度、DEFF 不确定性、可操作性缺口三个问题上形成共识
- 维持 Overall 3.5 不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1427 · 2026-05-23T09:31:22.448914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
  "offset": "0",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
    "offset": "0",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1428 · 2026-05-23T09:31:22.600083+00:00_

0	issues:
1	  # === Round 15 issues ===
2	
3	  - id: "R15-N1"
4	    summary: "DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分"
5	    category: method
6	    severity: critical
7	    status: open
8	    first_raised_round: 13
9	    last_seen_round: 15
10	    mentions:
11	      - round: 13
12	        reviewers: [1, 2]
13	        note: "R13-W2: 首次提出"
14	      - round: 14
15	        reviewers: [1, 2]
16	        note: "R14-W2: 再次独立提出"
17	      - round: 15
18	        reviewers: [1]
19	        note: "R1-N1 升级为 Must-Fix。论文已有 DEFF simulation (App I) 和 size-stratified table (App D)，但正文仍以 simple-mean 为主报告值而未在正文充分论证选择。Cluster bootstrap CI [26.7%, 53.2%] 极宽未讨论。"
20	    action_items:
21	      - round: 15
22	        action: "正文 §4.2 需并列呈现两种估计并解释选择理由；讨论 cluster bootstrap CI 宽度的驱动因素"
23	        assigned_to: paper_agent
24	        status: open
25	    resolution: ""
26	    resolution_round: null
27	
28	  - id: "R15-N2"
29	    summary: "Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定外部效度受限"
30	    category: method
31	    severity: critical
32	    status: open
33	    first_raised_round: 13
34	    last_seen_round: 15
35	    mentions:
36	      - round: 13
37	        reviewers: [1, 2]
38	        note: "R13-W3: 首次提出"
39	      - round: 14
40	        reviewers: [1, 2]
41	        note: "R14-W3: 标题改为 Detection Power under Controlled Injection"
42	      - round: 15
43	        reviewers: [1, 2]
44	        note: "R1-N2 + R2-W2 共识升级。两位 reviewer 一致认为 uniform flipping 不能被称为 worst-case，可能是 easiest-to-detect。要求增加更现实的注入模型或更准确描述其性质。"
45	    action_items:
46	      - round: 15
47	        action: "将 'worst-case' 改为 'stylized/simplified'；在正文讨论 uniform flipping 对 TPR 标定的影响方向；考虑增加 difficulty-dependent 注入对比"
48	        assigned_to: paper_agent
49	        status: open

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1429 · 2026-05-23T09:31:31.086349+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
  "old_string": "  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1]\n        note: \"R1-N1 升级为 Must-Fix。论文已有 DEFF simulation (App I) 和 size-stratified table (App D)，但正文仍以 simple-mean 为主报告值而未在正文充分论证选择。Cluster bootstrap CI [26.7%, 53.2%] 极宽未讨论。\"",
  "new_string": "  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 升级为 Must-Fix。R2 交叉回应 AGREE，补充: 13.5% 完全由两个 mega-family 驱动（tier >200 DEFF=36.11 vs 小家族 2.07）。建议主文报告范围而非点估计。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
    "old_string": "  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1]\n        note: \"R1-N1 升级为 Must-Fix。论文已有 DEFF simulation (App I) 和 size-stratified table (App D)，但正文仍以 simple-mean 为主报告值而未在正文充分论证选择。Cluster bootstrap CI [26.7%, 53.2%] 极宽未讨论。\"",
    "new_string": "  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 15\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 升级为 Must-Fix。R2 交叉回应 AGREE，补充: 13.5% 完全由两个 mega-family 驱动（tier >200 DEFF=36.11 vs 小家族 2.07）。建议主文报告范围而非点估计。\""
  }
}
```

</details>

---


### Tool result

_source line 1430 · 2026-05-23T09:31:31.137313+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Edit",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1431 · 2026-05-23T09:31:37.663231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
  "offset": "65",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
    "offset": "65",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1432 · 2026-05-23T09:31:37.713991+00:00_

65	      - round: 14
66	        reviewers: [1, 2]
67	        note: "R14-W7: 建议升级 highlight LLM-specific innovations"
68	      - round: 15
69	        reviewers: [1, 2]
70	        note: "R2-N1 升级为 Must-Fix，R1 AGREE with nuance。Introduction Contribution 3 列 'framework' 与 Section 2 'We do not modify the MH procedure' 矛盾。R1 认为 cross-subject matching 有实质适配但不构成方法创新。"
71	    action_items:
72	      - round: 15
73	        action: "Contribution 3 重述为 'methodological adaptations enabling valid DIF in LLM setting' 而非独立框架贡献；消除与 Section 2 的措辞矛盾"
74	        assigned_to: paper_agent
75	        status: open
76	    resolution: ""
77	    resolution_round: null
78	
79	  - id: "R15-W1"
80	    summary: "ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证"
81	    category: method
82	    severity: warning
83	    status: open
84	    first_raised_round: 15
85	    last_seen_round: 15
86	    mentions:
87	      - round: 15
88	        reviewers: [1]
89	        note: "R1-W1。阈值源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity (App A.2) 有用但不等于论证适切性。"
90	    action_items:
91	      - round: 15
92	        action: "增加一段讨论 ETS 阈值在 LLM 语境下的适切性，或用 permutation-based null 确定 LLM-specific 阈值"
93	        assigned_to: paper_agent
94	        status: open

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1433 · 2026-05-23T09:31:45.242088+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
  "old_string": "  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W1。阈值源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity (App A.2) 有用但不等于论证适切性。\"",
  "new_string": "  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W1 提出，R2 交叉回应 AGREE（程度有限）。R2 补充: threshold sensitivity 和 random-split baseline (0.18%) 在一定程度上缓解担忧，但仍建议增加简短讨论。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
    "old_string": "  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W1。阈值源自教育测试经验校准，LLM 群体方差结构不同。Threshold sensitivity (App A.2) 有用但不等于论证适切性。\"",
    "new_string": "  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-W1 提出，R2 交叉回应 AGREE（程度有限）。R2 补充: threshold sensitivity 和 random-split baseline (0.18%) 在一定程度上缓解担忧，但仍建议增加简短讨论。\""
  }
}
```

</details>

---


### Tool result

_source line 1434 · 2026-05-23T09:31:45.292830+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Edit",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1435 · 2026-05-23T09:31:48.855602+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "R15-W2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
  "output_mode": "content",
  "-A": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "R15-W2",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
    "output_mode": "content",
    "-A": "8"
  }
}
```

</details>

---


### Tool result

_source line 1436 · 2026-05-23T09:31:48.906410+00:00_

98:  - id: "R15-W2"
99-    summary: "N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力"
100-    category: method
101-    severity: warning
102-    status: open
103-    first_raised_round: 15
104-    last_seen_round: 15
105-    mentions:
106-      - round: 15

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-23T09:31:59.549519+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
  "old_string": "  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W2。BH-FDR 仅移除 3/3918 items 恰恰说明 p-value 已无区分力。论文已有 DEFF 校正恢复 p-value selectivity，但正文未充分讨论。\"",
  "new_string": "  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W2 提出。R2 交叉回应 REBUT：论文 §3.2 已显式处理此问题，DEFF 校正恢复 p-value selectivity（269 items 失显著性）。R2 认为不能与 R15-N1 (DEFF 选择) 同时作为独立 critical issue。降级为 info。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml",
    "old_string": "  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W2。BH-FDR 仅移除 3/3918 items 恰恰说明 p-value 已无区分力。论文已有 DEFF 校正恢复 p-value selectivity，但正文未充分讨论。\"",
    "new_string": "  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 15\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"R1-W2 提出。R2 交叉回应 REBUT：论文 §3.2 已显式处理此问题，DEFF 校正恢复 p-value selectivity（269 items 失显著性）。R2 认为不能与 R15-N1 (DEFF 选择) 同时作为独立 critical issue。降级为 info。\""
  }
}
```

</details>

---


### Tool result

_source line 1438 · 2026-05-23T09:31:59.601137+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Edit",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 1439 · 2026-05-23T09:32:06.566797+00:00_

Issue tracker 已更新，反映 R2 交叉回应的三个关键修正：
- R15-N1 (DEFF)：R2 AGREE，补充 mega-family 驱动因素
- R15-W1 (ETS 阈值)：R2 AGREE（程度有限）
- R15-W2 (p-value)：R2 REBUT，降级为 info——论文 §3.2 已处理，DEFF 是解决方案

审稿报告已提交，整体评分 **3.5/5 Borderline Conference**。R2 的迟到交叉回应与已提交报告结论一致，无需重投。圆桌审稿 Round 15 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 141

## Round 141

66 recorded events


### User

_source line 1440 · 2026-05-23T10:15:31.155479+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1441 · 2026-05-23T10:15:37.636171+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-23T10:15:37.687141+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1443 · 2026-05-23T10:15:46.122419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1444 · 2026-05-23T10:15:46.273459+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1445 · 2026-05-23T10:15:50.994326+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1446 · 2026-05-23T10:15:51.045020+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1447 · 2026-05-23T10:15:55.161872+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1448 · 2026-05-23T10:15:56.316914+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-23T10:15:56.317297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-23T10:15:56.468203+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Score Incomparability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1451 · 2026-05-23T10:16:04.098993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1452 · 2026-05-23T10:16:04.601461+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 MMLU models, 27,125 items across all six), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (${\approx}$27--29\% for MMLU after non-independence corrections; conservative bound 13.5\%; random-split baseline 0.18\%). Web-overlap contamination labels are near-independent of DIF flags (Jaccard $= 0.206$): global exposure and differential functioning are complementary diagnostic dimensions. Temporal DIF does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals structured item-level change---base and instruct models exhibit opposite DIF patterns ($\chi^2 = 562.7$)---and shifts DIF-corrected scores by ${+}2.12$\,pp on average. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1453 · 2026-05-23T10:16:04.601881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-23T10:16:04.602142+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} as the empirical phenomenon when DIF is detected across time-defined cohorts---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 849 rank positions. The incomparability is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items appear in training corpora---through membership inference~\citep{shi2024mink} and performance-based detection~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}, validated a
…[truncated 3739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1455 · 2026-05-23T10:16:05.003949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1456 · 2026-05-23T10:16:06.059024+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating} or in-context learning effects~\citep{zawalski2026codec}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discrim
…[truncated 4977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-23T10:16:06.059507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-23T10:16:06.562028+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 8972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-23T10:16:06.562410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1460 · 2026-05-23T10:16:07.014641+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: 31\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two DEFF estimators bound the non-independence effect in parallel: simple-mean DEFF (29.2\%) and cluster bootstrap (26.7\%) converge on ${\approx}$27--29\%, while the conservative weighted-mean DEFF yields 13.5\%---still $75\times$ the random baseline (\Cref{app:deff,app:deff_simulation}). No single family drives the signal (LOFO $|\Delta\mathrm{C\%}| \leq 2.93$\,pp); graduated de-duplication confirms C\% scales with power, not redundancy (\Cref{app:dedup_k}).
17	
18	\looseness=-1
19	Three controls confirm genuine temporal change (\Cref{tab:temporal_landscape}
…[truncated 10173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1461 · 2026-05-23T10:16:07.015096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1462 · 2026-05-23T10:16:07.517230+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{4\baselineskip}
4	
5	\subsection{Temporal DIF as Structured Signal}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design. Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
10	
11	\looseness=-1
12	The two temporal cohorts differ in base/instruct composition (2023: 79.7\% vs.\ 2024: 67.9\% base). Downsampling to match ratios yields C\% $= 30.25\% \pm 1.32\%$ ($\Delta = 1.08$\,pp; \Cref{app:composition_control}); base-only (32.1\%) and instruct-only (36.5\%) temporal analyses independently confirm substantial DIF (\Cref{app:baseinst_temporal}). Within-architecture Llama-2-vs-3 C\% $= 59.2\%$ drops to ${\sim}$28--29\% after ability matching, isolating the temporal component (\Cref{app:within_arch}).
13	
14	\looseness=-1
15	Three features distinguish LLM temporal DIF from educational settings: (1)~the observed C\% (${\approx}$27--29\%) substantially exceeds typical educational DIF rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$), unlike educational settings where DIF correlates with construct-irrelevant variance; (3)~model families introduce non-independence (design effect) absent in human testing, necessitating DEFF correction (\Cref{app:deff}).
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$
…[truncated 609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1463 · 2026-05-23T10:16:07.517621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1464 · 2026-05-23T10:16:07.969655+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (${\approx}$27--29\% for MMLU; conservative bound: 13.5\%), while aggregate rankings remain preserved ($\rho \approx 0.997$). Global exposure and differential functioning are complementary diagnostic dimensions (Jaccard $= 0.206$), confirmed by opposite base-vs-instruct DIF patterns ($\chi^2 = 562.7$). DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with rank displacements exceeding ${\pm}500$. Mechanism-conditional DIF audit should complement contamination screening as standard practice~\citep{habba2026growingpains}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1465 · 2026-05-23T10:16:07.970053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1466 · 2026-05-23T10:16:09.024781+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\Delta\mathrm{TPR}$ values may overestimate detection power, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. The framework detects \emph{that} items function differently but not \emph{why}---a deliberate design choice that limits immediate actionability; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1467 · 2026-05-23T10:16:09.025281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1468 · 2026-05-23T10:16:09.478135+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 30317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1469 · 2026-05-23T10:16:09.529142+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1470 · 2026-05-23T10:16:09.529516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1471 · 2026-05-23T10:16:10.232454+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1472 · 2026-05-23T10:16:10.333264+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1473 · 2026-05-23T10:16:21.528630+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1474 · 2026-05-23T10:16:23.647974+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-23T10:16:25.004348+00:00_

-rw-r--r-- 1 ubuntu ubuntu 18062 May 23 09:47 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-23T10:16:25.456660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-23T10:16:25.758295+00:00_

-rw-r--r-- 1 ubuntu ubuntu 662469 May 23 10:11 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-23T10:16:25.758759+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-23T10:16:28.720634+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines and ARR:

## Paper Types and Submission Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Policies

Following the ACL and ARR policies, there is no anonymity period requirement.

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## ARR-Specific Guidelines for EMNLP 2026

Given that 
…[truncated 783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7192
}
```

</details>

---


### Tool result

_source line 1480 · 2026-05-23T10:16:28.771382+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3012
}
```

</details>

---


### Tool call

_source line 1481 · 2026-05-23T10:16:37.506875+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit format template double blind ARR May cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline page limit format template double blind ARR May cycle"
  }
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-23T10:16:37.858782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-23T10:16:37.909866+00:00_

1	issues:
2	  # === Round 15 issues (Action Matrix locked, dispatched to Paper Agent) ===
3	
4	  - id: "R15-N1"
5	    summary: "DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分"
6	    category: method
7	    severity: critical
8	    status: in_progress
9	    first_raised_round: 13
10	    last_seen_round: 15
11	    mentions:
12	      - round: 13
13	        reviewers: [1, 2]
14	        note: "R13-W2: 首次提出"
15	      - round: 14
16	        reviewers: [1, 2]
17	        note: "R14-W2: 再次独立提出"
18	      - round: 15
19	        reviewers: [1, 2]
20	        note: "R1-N1 升级为 Must-Fix。mega-family size-dependent ICC 导致 weighted-mean over-correct。"
21	    action_items:
22	      - round: 15
23	        action: "§4.2 并列呈现两种估计 + 解释 size-dependent ICC 导致 weighted-mean over-correct + 引用 App I simulation + 强调 13.5% 仍是 75× baseline。Abstract/Intro/Conclusion 加 conservative bound。[复发×3轮，之前只做 writing hedge → 本轮 surfacing evidence to 正文]"
24	        assigned_to: paper_agent
25	        status: in_progress
26	    resolution: ""
27	    resolution_round: null
28	
29	  - id: "R15-N2"
30	    summary: "Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定外部效度受限"
31	    category: method
32	    severity: critical
33	    status: in_progress
34	    first_raised_round: 13
35	    last_seen_round: 15
36	    mentions:
37	      - round: 13
38	        reviewers: [1, 2]
39	        note: "R13-W3: 首次提出"
40	      - round: 14
41	        reviewers: [1, 2]
42	        note: "R14-W3: 标题改为 Detection Power under Controlled Injection"
43	      - round: 15
44	        reviewers: [1, 2]
45	        note: "共识 Must-Fix。uniform flipping 不是 worst-case，可能是 easiest-to-detect。"
46	    action_items:
47	      - round: 15
48	        action: "术语 worst-case→stylized; upper-bound→may overestimate; 加入 R19 difficulty-dependent ΔTPR≈0.41 vs uniform 0.51（~20% reduction）+ ρ signatures（+0.77/-0.52/+0.39）。[复发×3轮，之前只改术语 → 本轮加 evidence]"
49	        assigned_to: paper_agent
50	        status: in_pr
…[truncated 16454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1484 · 2026-05-23T10:16:45.841508+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit format template double blind ARR May cycle"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"}]

Based on the search results, here's what I found about EMNLP 2026:

**Submission Deadline:** The EMNLP 2026 paper submission deadline is May 25, 2026, 23:59:59 (UTC-12).

**Page Limits:** The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**Format and Template:** Manuscripts should be submitted electronically, in PDF format and formatted using the templates available here. Authors should not modify the style files, nor use templates designed for other conferences, as submissions
…[truncated 747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 8334
}
```

</details>

---


### Tool call

_source line 1485 · 2026-05-23T10:17:06.923375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1486 · 2026-05-23T10:17:07.375356+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 10:11:24 2026 UTC
ModDate:         Sat May 23 10:11:24 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           18
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       662469 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1487 · 2026-05-23T10:17:07.779148+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "paper_framing.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1488 · 2026-05-23T10:17:07.879960+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\\n\\n## Paper Type\\nEmpirical analysis + methodological framework. Discovery paper with substantive LLM-specific methodological adaptations. \\\"DIF audit framework reveals and quantifies temporal score incomparability.\\\" NOT \\\"just applied standard MH-DIF\\\" — three LLM-specific adaptations address challenges absent in educational testing, with cross-subject matching as a genuine innovation.\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-st
…[truncated 1344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1489 · 2026-05-23T10:18:09.489896+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1490 · 2026-05-23T10:18:09.590894+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1491 · 2026-05-23T10:18:14.060769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 1492 · 2026-05-23T10:18:14.161561+00:00_

This PDF has 18 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1493 · 2026-05-23T10:18:22.396079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1494 · 2026-05-23T10:18:23.111216+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf (646.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 715
}
```

</details>

---


### Tool call

_source line 1495 · 2026-05-23T10:18:55.199855+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1496 · 2026-05-23T10:19:18.597104+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23397
}
```

</details>

---


### Tool call

_source line 1497 · 2026-05-23T10:19:19.551699+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查方法严谨性和统计有效性。\n\n## 审稿任务\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf`\n**目标 Venue**: EMNLP 2026 (via ARR)\n**格式要求**: Long paper, 8 页正文限制, ACL 模板, double-blind, mandatory Limitations section（不计入页数）, 无限引用\n\n## 你的审查侧重\n\n**方法严谨性 + 统计有效性**，重点关注：\n\n1. **MH-DIF 方法论适用性**: MH-DIF 从教育测量迁移到 LLM 评估的统计假设是否成立？ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性。N=5,227 下 p-value 的统计功效和区分力。\n2. **DEFF 校正**: simple-mean (29.2%) vs weighted-mean (13.5%) 两种估计量差异 2 倍，论文是否充分解释了选择偏好和偏差来源？Simulation study (App I) 是否足够有说服力？\n3. **Semi-synthetic 验证框架**: uniform binary flipping 是否是 easiest-to-detect 而非 worst-case？ΔTPR 的外部效度。difficulty-dependent injection 是否充分缓解了这个concern？\n4. **Cross-subject matching**: ΔFPR=0 guarantee 的条件和限制。k≤5 限制在实践中的合理性。matching variable contamination 在多域污染场景下的表现。\n5. **控制实验充分性**: random split、ability-quintile、nearest-neighbor matching、composition control 是否完全排除了混淆因素？base/instruct composition shift (11.8pp gap) 的 residual confound。\n6. **Local independence**: Yen's Q3 显示 11.3% item pairs 存在局部依赖，permutation simulation 的 FPR 膨胀估计 (<0.001pp) 是否可信？\n7. **Multiple testing**: 论文声称 ETS C 的双重阈值提供了隐式控制，BH-FDR 仅移除 3/3,918 items。这个论证在 N=5,227 的超大样本下是否成立？\n\n请按 ARR 标准输出完整审稿报告，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查方法严谨性和统计有效性。\n\n## 审稿任务\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf`\n**目标 Venue**: EMNLP 2026 (via ARR)\n**格式要求**: Long paper, 8 页正文限制, ACL 模板, double-blind, mandatory Limitations section（不计入页数）, 无限引用\n\n## 你的审查侧重\n\n**方法严谨性 + 统计有效性**，重点关注：\n\n1. **MH-DIF 方法论适用性**: MH-DIF 从教育测量迁移到 LLM 评估的统计假设是否成立？ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 的合理性。N=5,227 下 p-value 的统计功效和区分力。\n2. **DEFF 校正**: simple-mean (29.2%) vs weighted-mean (13.5%) 两种估计量差异 2 倍，论文是否充分解释了选择偏好和偏差来源？Simulation study (App I) 是否足够有说服力？\n3. **Semi-synthetic 验证框架**: uniform binary flipping 是否是 easiest-to-detect 而非 worst-case？ΔTPR 的外部效度。difficulty-dependent injection 是否充分缓解了这个concern？\n4. **Cross-subject matching**: ΔFPR=0 guarantee 的条件和限制。k≤5 限制在实践中的合理性。matching variable contamination 在多域污染场景下的表现。\n5. **控制实验充分性**: random split、ability-quintile、nearest-neighbor matching、composition control 是否完全排除了混淆因素？base/instruct composition shift (11.8pp gap) 的 residual confound。\n6. **Local independence**: Yen's Q3 显示 11.3% item pairs 存在局部依赖，permutation simulation 的 FPR 膨胀估计 (<0.001pp) 是否可信？\n7. **Multiple testing**: 论文声称 ETS C 的双重阈值提供了隐式控制，BH-FDR 仅移除 3/3,918 items。这个论证在 N=5,227 的超大样本下是否成立？\n\n请按 ARR 标准输出完整审稿报告，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1498 · 2026-05-23T10:19:38.303577+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18751
}
```

</details>

---


### Tool call

_source line 1499 · 2026-05-23T10:19:38.554993+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查新颖性/贡献声称和论文完整性。\n\n## 审稿任务\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf`\n**目标 Venue**: EMNLP 2026 (via ARR)\n**格式要求**: Long paper, 8 页正文限制, ACL 模板, double-blind, mandatory Limitations section（不计入页数）, 无限引用\n\n## 你的审查侧重\n\n**新颖性/贡献 + 完整性 + 写作质量**，重点关注：\n\n1. **贡献声称的合理性**:\n   - Contribution 1 (\"两维度正交\") 是概念上预期的结果 (global exposure vs differential functioning 定义上就是不同构念) 还是有实质性新发现？\"empirically quantify a theoretically expected but previously unverified distinction\" 这个框架是否足够？\n   - Contribution 3 (\"three methodological adaptations\") vs Related Work §2 中 \"We do not modify the core MH statistic\" 之间是否存在矛盾？方法论新颖性是否被过度声称？\n   - 论文整体是 \"成熟工具的领域迁移\" 还是有实质性方法论创新？对 EMNLP 受众的价值定位。\n\n2. **Related Work 覆盖**:\n   - 是否遗漏了重要的 concurrent work？特别关注 2025-2026 年发表的 LLM evaluation 和 contamination 相关工作。\n   - 与 Growing Pains (Habba et al., 2026) 的对比是否准确和公平？\n   - 搜索是否有遗漏的相关 DIF/IRT 在 NLP 中的应用。\n\n3. **叙事结构和可读性**:\n   - Abstract 信息密度是否过高（大量数字堆砌）？\n   - Introduction 的 story arc 是否清晰有说服力？\n   - Discussion 是否提供了足够的 insight 超越实验结果的重述？\n   - \"temporal score incomparability\" vs \"measurement invariance\" 术语是否一致？\n\n4. **可操作性**:\n   - §5.2 Recommended DIF Audit Protocol 的决策启发式是否足够具体？\"mechanism-conditional responses\" 在 DIF 本身是 mechanism-agnostic 的前提下如何操作？\n   - 对 benchmark 维护者的实际建议是否清晰？\n\n5. **格式和规范**:\n   - 8 页正文限制合规性（注意 `\\enlargethispage*{4\\baselineskip}` 的使用）\n   - Limitations section 是否充分覆盖关键限制？\n   - 匿名规则遵守情况\n\n请按 ARR 标准输出完整审稿报告，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。",
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查新颖性/贡献声称和论文完整性。\n\n## 审稿任务\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_16/submitted.pdf`\n**目标 Venue**: EMNLP 2026 (via ARR)\n**格式要求**: Long paper, 8 页正文限制, ACL 模板, double-blind, mandatory Limitations section（不计入页数）, 无限引用\n\n## 你的审查侧重\n\n**新颖性/贡献 + 完整性 + 写作质量**，重点关注：\n\n1. **贡献声称的合理性**:\n   - Contribution 1 (\"两维度正交\") 是概念上预期的结果 (global exposure vs differential functioning 定义上就是不同构念) 还是有实质性新发现？\"empirically quantify a theoretically expected but previously unverified distinction\" 这个框架是否足够？\n   - Contribution 3 (\"three methodological adaptations\") vs Related Work §2 中 \"We do not modify the core MH statistic\" 之间是否存在矛盾？方法论新颖性是否被过度声称？\n   - 论文整体是 \"成熟工具的领域迁移\" 还是有实质性方法论创新？对 EMNLP 受众的价值定位。\n\n2. **Related Work 覆盖**:\n   - 是否遗漏了重要的 concurrent work？特别关注 2025-2026 年发表的 LLM evaluation 和 contamination 相关工作。\n   - 与 Growing Pains (Habba et al., 2026) 的对比是否准确和公平？\n   - 搜索是否有遗漏的相关 DIF/IRT 在 NLP 中的应用。\n\n3. **叙事结构和可读性**:\n   - Abstract 信息密度是否过高（大量数字堆砌）？\n   - Introduction 的 story arc 是否清晰有说服力？\n   - Discussion 是否提供了足够的 insight 超越实验结果的重述？\n   - \"temporal score incomparability\" vs \"measurement invariance\" 术语是否一致？\n\n4. **可操作性**:\n   - §5.2 Recommended DIF Audit Protocol 的决策启发式是否足够具体？\"mechanism-conditional responses\" 在 DIF 本身是 mechanism-agnostic 的前提下如何操作？\n   - 对 benchmark 维护者的实际建议是否清晰？\n\n5. **格式和规范**:\n   - 8 页正文限制合规性（注意 `\\enlargethispage*{4\\baselineskip}` 的使用）\n   - Limitations section 是否充分覆盖关键限制？\n   - 匿名规则遵守情况\n\n请按 ARR 标准输出完整审稿报告，包含 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。",
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1500 · 2026-05-23T10:19:39.964911+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 1501 · 2026-05-23T10:19:53.936443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/registry.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"No external_review config found\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/registry.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"No external_review config found\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1502 · 2026-05-23T10:19:54.039206+00:00_

No external_review config found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-23T10:19:58.469911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"*.yaml\" -o -name \"*.yml\" | head -20 && echo \"---\" && grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/ 2>/dev/null || echo \"No external review config\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"*.yaml\" -o -name \"*.yml\" | head -20 && echo \"---\" && grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/ 2>/dev/null || echo \"No external review config\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-23T10:19:58.620979+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/hendrycks2021mmlu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/liang2026dvd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/shi2024mink.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/balloccu2024leak.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/lalor2019irt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/zhou2026psnirt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/dekoninck2024constat.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/chen2025irtnet.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/li2024latesteval.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/white2025livebench.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/chang2024survey.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/li2025atlas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/tao2026selfcritique.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/golchin2024timetravel.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/habba2026growingpains.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/li2024contamination.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/chiang2024chatbot.yaml
/home/ubuntu/.agent-ml-research-idea_gen_052
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 1505 · 2026-05-23T10:20:13.849100+00:00_

外部审稿未在项目中配置，跳过。

当前状态：
- ✅ 视觉审查已派发（并行运行中）
- ✅ Reviewer 1（方法严谨性）已派发
- ✅ Reviewer 2（新颖性/完整性）已派发
- ⏳ 等待两位 Reviewer 返回初审结果

等待 Reviewer 回复中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1506 · 2026-05-23T10:27:24.957873+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

**论文**: "Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
**Venue**: EMNLP 2026 (via ARR)

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 扎实的大规模经验研究，将教育测量中的 MH-DIF 方法应用于 LLM 基准评测，发现 ~27-29% 的题目存在时间性 DIF，实用价值高，但方法论新颖性有限——核心贡献更接近"成熟工具的领域迁移"而非"实质性方法论创新"。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法正确应用，结构性控制充分（Table 2），但 Contribution 1 概念深度不足，§5.2 的机制推断超出 DIF 方法论所能支撑的范围 |
| Excitement | 3/5 | 解决了一个及时且实用的问题（基准分数的时间可比性），规模令人印象深刻，但核心方法是已有心理测量方法的应用，发现基本符合理论预期 |
| Reproducibility | 4/5 | 标准 MH-DIF 方法，METABENCH 公开可用，匿名 URL 承诺提供代码，半合成验证框架描述清晰 |
| Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评测文献，技术评估有把握，新颖性判断涉及一定主观性 |

---

## Paper Summary

本文对 5,227 个 LLM 在 METABENCH 的 12,508 道 MMLU 题目上进行大规模的 Mantel-Haenszel 差异项目功能（DIF）分析，检测 2023 与 2024 模型群组之间的时间性分数不可比性。主要发现：(1) 17.9-31.5% 的题目表现出时间性 DIF；(2) 全局暴露（web-overlap 标签）与差异功能在经验上正交（Jaccard ≈ 0.206）；(3) DIF 校正后分数平均偏移 ±2.12pp。论文在 6 个基准上进行了交叉验证，并提供了半合成注入框架来验证 MH-DIF 的灵敏度。

---

## 主要优势

**S1. 规模与经验严谨性**
5,227 个模型 × 12,508 道题目，是迄今最大规模的 LLM 基准 DIF 分析。Table 2 中的多重结构性控制（能力匹配分层、交叉学科匹配、DEFF 校正、随机分割基线）展现了对方法的审慎态度。五个 cohort design（Section 3.3）涵盖了时间、能力、家族内和随机对照，分析全面。

**S2. 实用价值明确**
~27-29% 的题目存在时间性 DIF，DIF 校正后的排名位移平均达到 ±2.12pp（Section 4.6），对排行榜维护者和基准开发者有直接的可操作意义。Table 3 的 6 基准交叉验证（C% 从 17.9% 到 33.3%）增强了泛化性。

**S3. 正交性发现具有实践价值**
虽然全局暴露与差异功能在概念上属于不同构念，但量化其独立性（Jaccard ≈ 0.206, ρ = 0.012；Section 4.3）为实践提供了具体证据：现有的污染检测方法不足以保证分数可比性。Figure 1 的 ICC 可视化对直觉理解有效。

**S4. 验证框架完备**
半合成注入框架（Section 3.4）以可控的污染率验证 MH-DIF 灵敏度（Figure 2, Table 11），cross-subject matching 与 within-subject matching 的对比实验（Section 4.5）提供了匹配策略选择的经验依据。

**S5. 附录深度出色**
Appendix A-P（Section A 的诊断、Section B 的机制分析、Section C 的结构控制细节、Section D 的 DEFF 估计、Section J 的去重灵敏度等）为 thorough reader 提供了完整的技术链条。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution 1 的贡献度声称需要重新校准

- **具体位置**: Section 1 Contribution 1 (page 2): "We empirically quantify a theoretically expected but previously unverified distinction"
- **问题**: 全局暴露（global exposure）和差异功能（differential functioning）在定义上就是不同的构念——web-overlap 标签测量的是数据存在性，MH-DIF 测量的是在控制总分后的条件性响应模式差异。这两者的低相关性（Jaccard ≈ 0.206）是方法论层面的结构性预期，而非经验上的惊人发现。将其提升为三大贡献之首（"Two dimensions of benchmark behavior"）存在过度声称风险。
- **为什么影响接收**: EMNLP reviewer 可能将此视为"在大规模数据上确认了显而易见的事实"，而非提供新的 insight。这会直接影响 Excitement 评分。
- **建议修改方向**: 将 Contribution 1 重新定位为支撑性经验观察而非独立贡献，或者强化其实践后果的论证——例如展示在不做 DIF 审计的情况下排名会如何被误导（即 contamination filter 通过但 DIF 未通过的具体案例分析）。目前 Section 4.3 只报告了统计量，缺乏对"这意味着什么"的深入讨论。

**N2** [critical] Contribution 3 ("three methodological adaptations") 与 "We do not modify the core MH statistic" 之间的张力

- **具体位置**: Section 1 Contribution 3 (page 2) vs. Section 2 Related Work (page 3): "We do not modify the core MH statistic; our adaptations address challenges specific to the LLM evaluation setting"
- **问题**: 论文在 Contribution 3 中声称 "three methodological adaptations for LLM evaluation"，但同时在 Related Work 中明确承认不修改核心统计量。逐条审视这三个 "adaptations"：
  - (a) Cross-subject matching: 是匹配变量的选择（使用另一个 benchmark 的总分作为匹配变量），属于标准实践中的实施决策，而非方法论创新
  - (b) Family-level DEFF correction: 直接借用自 survey methodology (Rao and Scott, 1992)，论文自己也承认 "adapted from survey methodology"（Section 1）
  - (c) Semi-synthetic validation: 这是验证策略，不是方法论贡献
  - 这三者是将 MH-DIF 应用于 LLM 评测时的合理工程决策，但称之为 "methodological adaptations" 过度拉升了新颖性。
- **为什么影响接收**: 方法论新颖性是 EMNLP 评审的重要维度。如果三大贡献中有两个（C1 的概念深度不足、C3 的新颖性虚高）存在问题，论文的整体贡献叙事会被显著削弱。
- **建议修改方向**: 将 Contribution 3 重新表述为 "practical considerations for deploying MH-DIF at scale in the LLM setting"，诚实地定位为工程贡献而非方法论创新。或者，如果希望强调方法论贡献，需要更有力地论证为什么这些 adaptations 是 non-trivial 的——例如展示 naive matching 与 cross-subject matching 的结果差异有多大。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] §5.2 审计协议中的机制推断超出方法能力

- **具体位置**: Section 5.2 "Recommended DIF Audit Protocol" (page 8)
- **问题**: 协议建议 "mechanism-conditional responses: DIF + web-overlap co-occurrence warrants removal, DIF on web-clean items suggests capability shift immunity"。但 DIF 本质上是 mechanism-agnostic 的——它检测到题目功能差异（*that*），但不能告诉我们为什么（*why*）。将 DIF 结果与 web-overlap 标签交叉后做因果性解读（"suggests capability shift"）是一种 ad hoc 的推断，缺乏方法论支撑。
- DIF 可能由多种因素引起：训练方法学变化、tokenizer 差异、prompt format 敏感性、数据配比变化等。论文没有讨论这些替代解释。
- **建议**: 明确承认 mechanism inference 的局限性，将协议定位为 heuristic 而非 principled decision framework。可以添加一个 caveat 段落讨论"DIF alone cannot determine causation"。

**W2** [warning] Discussion (Section 5) 停留在结果层面，缺乏深层 insight

- **具体位置**: Section 5.1-5.2 (pages 7-8)
- **问题**: Section 5.1 本质上是额外的实验结果（模型类型分层分析），而非对发现的反思性讨论。Section 5.2 提供了操作建议但没有讨论更深层的问题：
  - 为什么题目会随时间发展出 DIF？是训练数据分布的变化？能力天花板效应？还是评测方法论本身的问题？
  - 时间性分数不可比性对整个 LLM 领域依赖排行榜排名意味着什么？
  - 是否应该将 DIF 校正作为标准实践？其治理含义是什么？
- **建议**: 增加一段讨论 temporal DIF 的成因假说和对 LLM 评测生态的系统性影响。

**W3** [warning] Abstract 信息密度过高

- **具体位置**: Abstract (page 1)
- **问题**: 单段内包含 15+ 个数值（5,227 models, 27,125 items, 17.9-31.5%, χ²=27-295, p < 0.05, 0.16%, 13.5%, ρ ≈ 0.997, Jaccard = 0.206, ρ = 0.012, χ² = 562.7, ±2.12pp, 0.18%）。对不熟悉 DIF 术语的 NLP 读者来说，这严重影响可读性。
- **建议**: 保留核心数字（规模、DIF 率、分数位移幅度），将统计检验细节移至 Introduction。

**W4** [warning] Limitations section 覆盖面偏窄

- **具体位置**: Section 7 Limitations (page 8)
- **问题**: 仅覆盖半合成框架的三个方法论限制。以下重要限制未讨论：
  - (a) 对 MMLU 式多选题以外的基准（代码、数学、开放生成）的泛化性
  - (b) 模型发布日期与训练数据截止时间不一定对齐的假设
  - (c) 依赖 Li et al. 的 web-overlap 标签作为正交性分析的准 ground truth——这些标签本身有已知局限性
- **建议**: 补充上述三点限制。

---

## 小问题（不影响接收）

**M1** [minor] 术语不一致: 标题使用 "temporal score incomparability"，但论文框架检测的是 measurement non-invariance (via DIF)。这是相关但不同的概念——measurement non-invariance 是机制，score incomparability 是后果。应在 Section 1 明确这一区分。

**M2** [minor] 潜在的格式合规问题: 审稿任务指出论文使用了 `\enlargethispage*{4\baselineskip}`。如果此命令应用于正文页面（Sections 1-6），可能构成格式违规（扩展了模板指定的文本区域边距）。4\baselineskip ≈ 0.67 英寸的扩展量不算小。建议在 camera-ready 阶段移除此命令并确保正文自然适配 8 页限制。

**M3** [minor] Section 4.6 (Downstream Impact) 的排名影响分析基于 stable-item ranking，但未讨论 DIF 校正对模型间差异的统计显著性——±2.12pp 的偏移在排名差异的置信区间内还是外？

**M4** [minor] Figure 1 的 ICC 图（左 vs 右）有效传达了直觉，但 y 轴标签 ("P(correct)") 在右图中应标注为条件概率以明确是在控制总分后的结果。

---

## 遗漏的相关工作

以下近期工作应在 Related Work §2 中被引用或讨论：

1. **"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"** (arxiv 2511.04689, Nov 2025) — 使用 IRT 的 Fisher information 进行自适应 LLM 评测，与本文的 IRT 应用形成互补视角
2. **"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory"** (arxiv 2509.22888, Sep 2025) — 提出 joint embedding 方式的 IRT，代表了 IRT 在 LLM 评测中的另一个创新方向
3. **"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores"** (arxiv 2601.13885, Jan 2026) — 扩展了 IRT 自适应测试到连续分数
4. **"When Benchmarks Leak: Inference-Time Decontamination for LLMs"** (arxiv 2601.19334, Jan 2026) — 从推理时去污染角度处理基准泄露，与本文的 audit 视角互补

与 Growing Pains (Habba et al., 2026) 的对比（Section 2, page 3）基本准确——论文正确区分了 anchor-item calibration（Growing Pains 的目标）和 DIF detection（本文的目标）。但可以更明确地讨论两者的互补关系：DIF 发现的不稳定题目是否应从 Growing Pains 的 anchor set 中排除？

---

## 问题（Questions for Authors）

**Q1**. Table 1 中不同学科的 DIF enrichment ratio 差异较大（Humanities 0.45 vs STEM 0.86），这一跨领域差异的驱动因素是什么？是差异化的污染率还是题目本身的结构特性？

**Q2**. DEFF 校正（Appendix D）使用 family-level ICC 来处理家族内依赖。如果以更粗粒度定义 "family"（例如组织而非模型系列），C% 会如何变化？

**Q3**. 半合成注入框架（Section 3.4）以固定概率 p 翻转响应。实践中，污染可能表现为对特定难度或类型题目的选择性提升。是否考虑过与题目难度相关的注入方案？

**Q4**. Growing Pains (Habba et al., 2026) 用 anchor items 做 IRT calibration，本文用 MH-DIF 做时间可比性检测。两者天然互补——是否考虑过 DIF-flagged items 应被排除出 anchor sets？

---

## 总结判断

本文在一个重要且及时的问题上做了大量认真细致的经验工作，规模和严谨性令人印象深刻。核心发现（~27-29% temporal DIF, ±2.12pp 分数偏移）对 LLM 评测实践有直接价值。

主要顾虑在于贡献的新颖性定位：论文本质上是将教育测量中的标准 MH-DIF 方法迁移到 LLM 评测领域，三个 contributions 中有两个存在过度声称的风险（C1 确认理论预期，C3 声称的 "methodological adaptations" 实为工程决策）。Discussion 的深度不足以弥补方法论新颖性的不足。

如果作者能够：(1) 更诚实地定位贡献层次（强调经验发现的实践价值而非方法论创新），(2) 深化 Discussion 的反思性分析，(3) 解决 §5.2 的 mechanism inference 问题，论文有潜力达到 Conference 水平。当前状态更适合 Findings。

**Overall: 3.5 (Borderline Conference)**
**Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1507 · 2026-05-23T10:27:33.492851+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1508 · 2026-05-23T10:27:38.026529+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。论文规模和严谨性出色（5,227 模型 × 12,508 题目的 MH-DIF 审计），发现 ~27-29% 的题目存在时间性 DIF，实用价值高。但两个核心问题拉低评分：

1. **贡献声称偏高**——Contribution 1（正交性）是概念上预期的结构性结果而非新发现；Contribution 3（三个方法论适配）与"我们不修改核心 MH 统计量"自相矛盾，本质是工程决策而非方法创新
2. **Discussion 深度不足**——§5.1 实质是更多结果，§5.2 的审计协议从 mechanism-agnostic 的 DIF 推断因果机制，缺乏方法论支撑

同时标注了 4 项 Should-Fix（审计协议的机制推断、Discussion 深度、Abstract 信息密度、Limitations 覆盖面）和 4 篇遗漏的近期 IRT-for-LLM 工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1509 · 2026-05-23T10:27:44.208144+00:00_

Reviewer 2 已返回，等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 144

## Round 144

6 recorded events


### User

_source line 1510 · 2026-05-23T10:28:27.675435+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告

**论文**: "Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
**审查侧重**: 方法严谨性 + 统计有效性
**Venue**: EMNLP 2026 (via ARR)

---

## Paper Summary

本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能分析 (MH-DIF) 迁移至 LLM benchmark 评估领域，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items）审计 2023 与 2024 模型队列间的分数可比性。核心发现：17.9–31.5% 的 items 在 ETS Category C 阈值（|Δ_MH| ≥ 1.5）下展现 temporal DIF。论文提出三项方法学适配：(a) cross-subject matching 防止 contamination 污染 matching variable；(b) DEFF 校正处理模型家族内非独立性；(c) semi-synthetic injection 验证框架。主要结论：DIF flags 与 global exposure labels 近似独立（Jaccard ≈ 0.206），DIF-corrected scores 平均偏移 ±2.12pp，raw benchmark scores 跨时间队列不可直接比较。

---

## 总体评分

**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论框架扎实、实证规模空前，但 ETS 阈值从人类考试直接移植到 LLM 缺乏领域内标定、DEFF 两种估计量 2 倍差距削弱了定量结论的精度，综合来看是一篇有实质贡献但关键校准环节需要补强的工作。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 方法论框架从教育测量迁移整体合理，5 种 cohort 设计提供三角验证，但 ETS 阈值缺乏 LLM 领域特定标定，DEFF 估计量不确定性大，multiple testing 论证在超大样本下有循环论证问题 |
| Excitement | 3.5 / 5 | 重要且及时的问题——benchmark 分数跨时间可比性直接影响社区对模型进步的理解；cross-subject matching 是真正的方法学贡献；但 "分数不可比" 这一定性结论对实践者而言可能并不意外 |
| Reproducibility | 4 / 5 | 代码可用，数据公开（METABENCH），方法描述详尽含参数（K=5 strata、ETS 阈值、bootstrap 细节）；Appendix 覆盖了绝大多数实现细节 |
| Overall Assessment | 3.5 / 5 | Borderline Conference——定性发现稳健、方法学有贡献，但定量精度（阈值校准、DEFF 不确定性）需加强方可达到 Conference 水准 |

**Reviewer Confidence**: 4 / 5（统计方法论和心理测量领域有充分经验，仔细阅读了全文含全部 Appendix）

---

## Strengths

**S1. 重要且及时的研究问题。** LLM benchmark 分数跨时间可比性是社区追踪模型进步的基础假设。本文以实证而非轶事方式证明 ~27–29% 的 items 存在 temporal DIF，直接影响 leaderboard 解读。这不是 "contamination detection"——而是一个更根本的 measurement invariance 问题。

**S2. 原则性的方法论框架。** MH-DIF 是教育测量中最成熟的 DIF 检测方法之一，其非参数特性（仅需二值响应和分组标签，无需模型内部信息）恰好适配 LLM 评估场景。方法选择有充分理论依据，不是简单的工具套用。

**S3. 空前的实证规模与系统性控制。** 5,227 模型 × 12,508 items 是目前同类研究中最大规模的审计。五种 cohort 设计（temporal, ability-quintile, within-family, within-subject, random split）提供了真正的三角验证。Random split 基线 C% = 0.18%（Section 4.1）确认方法在零假设下几乎无 false positive，为后续结论提供了坚实的参照基准。

**S4. Cross-subject matching 是实质性的方法学贡献。** 单域 contamination 下 ΔFPR = 0 的理论保证（Section 3.4）推导清晰且正确：将被测 subject 排除出 matching variable，从构造上阻断了 contamination 信号泄漏。这解决了将 DIF 应用于 LLM benchmark 时一个真实且此前未被解决的方法学难题。实证验证（Table 7）也支持这一保证在小 k 下成立。

**S5. 对估计量不确定性的透明度。** 论文诚实报告了 simple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）之间 ~2.2× 的差距（Section 4.2），而非 cherry-pick 一个。Appendix I 的 simulation study 为偏好 simple-mean 提供了有原则的依据，同时承认不确定性。

**S6. 实用价值。** Section 5.2 提供了具体可操作的审计协议（MH-DIF pre-screening, N ≥ 500, cross-subject matching, k ≤ 5 阈值），直接可被 benchmark 维护者采用。

**S7. 跨 benchmark 复制。** 分析扩展到全部 6 个 METABENCH benchmarks（Table 3）并在 GSM8K 上复制（Section 4.7），增强了泛化性声称。所有 6 个 benchmark 的 C% 均高于随机基线（Table 3 shows 20.7%–48.4%），定性结论一致。

---

## Must-Fix 问题（影响接收决定）

**N1 [critical] ETS 阈值从人类考试直接移植到 LLM 缺乏领域内校准**
- 具体位置：Section 3.2, Appendix A.2
- 问题：论文直接采用 ETS Category C 阈值（|Δ_MH| ≥ 1.5）并引用其在教育测试中的标准地位。然而在教育场景中，DIF 率通常为 5–15%（Clauser and Mazor, 1998）；本文发现 17.9–31.5%，高出 2–6 倍。这一显著差异可能意味着：(a) LLM benchmark 确实存在严重的 measurement instability，或 (b) 该阈值对 LLM 领域过于宽松，因为 LLM 的 item-response 模式与人类考生在结构上不同。
  
  Appendix A.2 的阈值敏感性分析（|Δ_MH| ∈ {1.0, 1.5, 2.0, 2.5}）显示定性稳健性，这有帮助。但论文始终未建立：在 LLM 评估中，|Δ_MH| = 1.5 对应的 odds ratio (~2.7:1) 是否构成"实质性显著"的 measurement difference。当"考生"是 LLM 而非人类学生时，同一 effect size 可能有完全不同的实际含义。

- 为什么影响接收：论文的核心量化声称（"17.9–31.5% items exhibit temporal DIF"）完全依赖于这个阈值。如果阈值不恰当，所有下游分析（DEFF 校正、cross-benchmark 比较、审计协议建议）的数值精度都受影响。
- 建议修改方向：提供 LLM 领域内的实证锚定——例如，展示 |Δ_MH| ≥ 1.5 的 items 与 |Δ_MH| < 1.5 的 items 在模型排名上产生显著不同的结果（rank displacement analysis）。或者，使用数据驱动方法（如 random split 下 |Δ_MH| 分布的 95th percentile）建立 LLM-specific threshold，与 ETS 1.5 比较。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] DEFF 校正的 2× 不确定性削弱了 headline 定量精度**
- 具体位置：Section 4.2, Appendix I
- 问题：Simple-mean DEFF（29.2%，cluster bootstrap CI 26.7%）与 weighted-mean DEFF（13.5%）相差 ~2.2 倍。论文通过 Appendix I 的 simulation 论证了 simple-mean 的偏好，但该 simulation 仅测试了 4 种特定的 family-structure 场景，且 simple-mean 的优势依赖于 ICC 与 family size 的负相关关系——这一经验关系可能随 benchmark 和时间变化。
  
  论文 headline claim "17.9–31.5% of items exhibit temporal DIF" 横跨了这个范围。读者无法区分 "~18% items have DIF" 和 "~31% items have DIF"——二者的实践含义差异巨大。

- 建议：(1) 在 abstract 和 introduction 中更突出地报告校正后范围，而非仅在 Section 4.2 讨论；(2) 给出在什么条件下（family 数量、size 分布、ICC 范围）应使用哪种估计量的指导；(3) 考虑报告一个 conservative "robust" 估计，如两种估计量的区间并集。

**W2 [warning] Multiple testing 论证在超大样本下存在循环逻辑**
- 具体位置：Section 3.2, Appendix A
- 问题：论文声称 ETS C 的双重阈值（|Δ_MH| ≥ 1.5 AND p < 0.05）提供了"隐式"多重检验控制，并以 BH-FDR 仅移除 3/3,918 items 为证。但论文自身承认："At N ≥ 5,227, significance (p ≈ 0.03) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5"（Section 3.2）。这意味着：
  (a) p-value 阈值是空洞的——它从不 bind；
  (b) 分类完全由 effect size 决定；
  (c) 对本身已极小的 p-values 施加 BH-FDR 自然几乎无变化。
  
  论证是循环的：展示一个校正在未校正值已极端时没有效果，不能证明分类是良好校准的。

- 建议：明确承认在此 N 下分类本质上是纯 effect-size 准则，并在实质性而非统计性基础上论证 effect-size 阈值的合理性（与 N1 建议联动）。

**W3 [warning] Semi-synthetic validation 使用 stylized injection 可能高估检测能力**
- 具体位置：Section 3.4, Figure 2, Appendix G
- 问题：主要验证（Section 3.4）使用 uniform binary flipping：选择 ETS A items 并以均匀概率 p 将 incorrect 翻转为 correct。这是检测的"最佳情况"——真实 contamination 产生渐变的、difficulty-dependent 的、部分的效应。
  
  Appendix G 的 difficulty-dependent injection 部分缓解了这一顾虑，但揭示了一个重要缺口：injection 无法匹配 instruct 模型观察到的 near-zero direction-reversal pattern（残差 gap 13×）。论文将此解读为 "instruct-model DIF 至少部分由非 contamination 机制驱动"——这是合理的解读，但同时意味着 semi-synthetic 框架无法完整复制真实 DIF 模式。

- 建议：在 main text 中更明确地说明 ΔTPR 应被解读为检测能力的 upper bound 而非 point estimate。考虑增加更具挑战性的 injection scheme（如 graded injection with noise, model-capability-dependent injection rates）以测试 robustness。

**W4 [warning] Base/instruct composition confound 未完全排除**
- 具体位置：Section 5.1, Appendix O, Appendix P
- 问题：论文报告 11.8pp 的 composition gap。Appendix O 显示 base 和 instruct 模型各自独立展现 DIF（Table 15），但方向分布差异大（base: 61.1% reference-favoring, ρ = −0.528; instruct: 65.6% focal-favoring, ρ = −0.079）。这意味着 temporal DIF profile 是两种不同模式的加权混合，且混合权重在队列间发生了偏移。虽然各子群 DIF 幅度可能持续，但聚合 C% 仍可能被 composition shift 部分膨胀。
  
  Section C（Appendix）的 composition control 显示仅 −1.0pp 的 residual shift，令人安心但基于有限协变量的 matching。

- 建议：报告 composition-matched temporal C%（在 base/instruct 比例对齐后的 DIF 率），并讨论 residual confounding 的 magnitude bound。

---

## 小问题（不影响接收）

**M1.** Local dependence 影响可能被低估。Yen's Q3 显示 11.3% within-subject item pairs |Q3| > 0.20（Section A.1），但 permutation simulation 估计 FPR inflation < 0.001pp。这一估计在直觉上偏低：虽然 permutation test 在零假设（无 DIF）下有效，但在备择假设下（真实 DIF 存在），LD 可能导致 subject 内 DIF 信号相关，使表面独立的 DIF-flagged items 数量高估。建议报告 within-subject DIF clustering 程度或讨论有效独立 DIF 信号数。

**M2.** Cross-benchmark 分析较薄。Table 3 报告了 6 个 benchmarks 的 C% 和相关性，但缺少深度分析——例如，是否同一 model families 在所有 benchmarks 上驱动 DIF？Item-level DIF profiles 是否跨 benchmark 相关？

**M3.** GSM8K 复制（Section 4.7）描述过于简略。应报告使用了多少 items/models，以及 GSM8K 的 DIF 模式与 MMLU 的异同。

**M4.** 论文在 Section 3.2 提到 "At N ≥ 5,227"，但 temporal comparison 实际使用 N_ref = 1,080, N_focal = 807（Section 3.3），总计 1,887 而非 5,227。应澄清 MH test 中使用的有效 N。

**M5.** Figure 1 的 "left" vs "right" 两个子图区分需要更清晰的标注——当前 caption 中"Left: global contamination produces no DIF" 和 "Right: differential contamination produces DIF" 在小字体下不够醒目。

---

## Questions for Authors

**Q1.** 能否提供证据表明 |Δ_MH| = 1.5 在 LLM 场景下产生有意义的不同的模型排名？例如，仅移除 |Δ_MH| ≥ 1.5 items vs. |Δ_MH| ≥ 1.0 或 ≥ 2.0 后，平均 rank displacement 分别是多少？

**Q2.** DEFF simulation（Appendix I）假设了特定的 ICC-family-size 关系。如果 within-family ICC 在不同 family size 间大致恒定（而非负相关），simple-mean 的偏好是否仍然成立？

**Q3.** Permutation simulation 报告 LD 导致 FPR inflation < 0.001pp。运行了多少 permutations？该估计的 standard error 是多少？鉴于 11.3% item pairs 显示 |Q3| > 0.20，能否提供直觉解释为何 FPR 影响如此之小？

**Q4.** Difficulty-direction interaction（Appendix B）显示显著的 difficulty × model-type interaction（t = 1.56, OR = 4.75, p < 10⁻⁸）。仅此 interaction 能解释多大比例的 observed temporal DIF？是否存在这样的可能：difficulty-dependent capability improvements（无需任何 contamination）即可产生类似幅度的 DIF？

**Q5.** K=5 strata 的选择依据 ETS 推荐实践。是否测试了 K=3 或 K=10 对 DIF 检测率的影响？Appendix J 提到了 K=3 和 K=5 的比较，但 main text 中未讨论。

---

## Missing References

- Martinková, P., & Drabinová, A. (2018). "ShinyItemAnalysis for teaching psychometrics and to enforce routine analysis of educational tests." *The R Journal* — 提供了替代 DIF 检测工具，与本文方法可作比较。
- Chalmers, R.P. (2012). "mirt: A multidimensional item response theory package for the R environment." *Journal of Statistical Software* — 论文提到 multidimensionality 但未引用主要 MIRT 软件/方法论文献。
- 论文引用了 Polo et al. (2024) tinyBenchmarks，但可进一步讨论 IRT-based benchmark compression 与 DIF-aware item selection 的关系。

---

## 总结

本文在一个重要问题上做出了实质性贡献：通过大规模心理测量审计揭示 LLM benchmark 分数的 temporal incomparability。方法论框架从教育测量迁移整体合理，cross-subject matching 是真正的创新，实证规模空前。主要不足集中在校准层面：ETS 阈值的 LLM 适用性缺乏领域内验证（N1），DEFF 校正的不确定性范围过大（W1），multiple testing 论证在大样本下需要重新框定（W2）。这些问题影响定量精度但不动摇定性结论（temporal DIF 以非平凡比例存在）。如果作者能补充 threshold 的 LLM-specific 校准，论文可上升到 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1511 · 2026-05-23T10:29:04.141925+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Contribution 1 的贡献度声称需要重新校准\n- 全局暴露（global exposure）和差异功能（differential functioning）在定义上就是不同的构念。将其低相关性（Jaccard ≈ 0.206）提升为三大贡献之首存在过度声称风险。EMNLP reviewer 可能将此视为\"在大规模数据上确认了显而易见的事实\"。\n\n**N2** [critical] Contribution 3 (\"three methodological adaptations\") 与 \"We do not modify the core MH statistic\" 之间的张力\n- (a) Cross-subject matching 属于标准实践中的实施决策；(b) DEFF correction 直接借用自 survey methodology；(c) Semi-synthetic validation 是验证策略，不是方法论贡献。称之为 \"methodological adaptations\" 过度拉升了新颖性。\n\n### Should-Fix\n\n**W1** [warning] §5.2 审计协议中的机制推断超出方法能力\n- DIF 本身是 mechanism-agnostic 的，但 §5.2 建议 \"DIF on web-clean items suggests capability shift\"——这是 ad hoc 推断。\n\n**W2** [warning] Discussion 停留在结果层面，缺乏深层 insight\n- §5.1 本质上是额外实验结果；§5.2 缺乏对 temporal DIF 成因和对 LLM 评测生态系统性影响的讨论。\n\n**W3** [warning] Abstract 信息密度过高\n- 单段内包含 15+ 个数值，影响可读性。\n\n**W4** [warning] Limitations section 覆盖面偏窄\n- 未讨论对 MMLU 式多选题以外基准的泛化性、模型发布日期与训练数据截止时间不对齐、Li et al. web-overlap 标签本身的局限性。\n\n### Minor\n\n**M1** 术语不一致: \"temporal score incomparability\" vs measurement non-invariance\n**M2** `\\enlargethispage*{4\\baselineskip}` 潜在格式违规\n**M3** ±2.12pp 偏移在排名差异置信区间内还是外？\n**M4** Figure 1 右图 y 轴应标注条件概率\n\n### Missing References\n1. Adaptive Testing for LLM Evaluation (arxiv 2511.04689)\n2. JE-IRT (arxiv 2509.22888)\n3. Confident Rankings with Fewer Items (arxiv 2601.13885)\n4. When Benchmarks Leak: Inference-Time Decontamination (arxiv 2601.19334)\n\n### Questions\nQ1. 不同学科的 DIF enrichment ratio 差异的驱动因素？\nQ2. 更粗粒度定义 \"family\" 后 C% 如何变化？\nQ3. 是否考虑过与题目难度相关的注入方案？\nQ4. DIF-flagged items 是否应被排除出 Growing Pains 的 anchor sets？",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Contribution 1 的贡献度声称需要重新校准\n- 全局暴露（global exposure）和差异功能（differential functioning）在定义上就是不同的构念。将其低相关性（Jaccard ≈ 0.206）提升为三大贡献之首存在过度声称风险。EMNLP reviewer 可能将此视为\"在大规模数据上确认了显而易见的事实\"。\n\n**N2** [critical] Contribution 3 (\"three methodological adaptations\") 与 \"We do not modify the core MH statistic\" 之间的张力\n- (a) Cross-subject matching 属于标准实践中的实施决策；(b) DEFF correction 直接借用自 survey methodology；(c) Semi-synthetic validation 是验证策略，不是方法论贡献。称之为 \"methodological adaptations\" 过度拉升了新颖性。\n\n### Should-Fix\n\n**W1** [warning] §5.2 审计协议中的机制推断超出方法能力\n- DIF 本身是 mechanism-agnostic 的，但 §5.2 建议 \"DIF on web-clean items suggests capability shift\"——这是 ad hoc 推断。\n\n**W2** [warning] Discussion 停留在结果层面，缺乏深层 insight\n- §5.1 本质上是额外实验结果；§5.2 缺乏对 temporal DIF 成因和对 LLM 评测生态系统性影响的讨论。\n\n**W3** [warning] Abstract 信息密度过高\n- 单段内包含 15+ 个数值，影响可读性。\n\n**W4** [warning] Limitations section 覆盖面偏窄\n- 未讨论对 MMLU 式多选题以外基准的泛化性、模型发布日期与训练数据截止时间不对齐、Li et al. web-overlap 标签本身的局限性。\n\n### Minor\n\n**M1** 术语不一致: \"temporal score incomparability\" vs measurement non-invariance\n**M2** `\\enlargethispage*{4\\baselineskip}` 潜在格式违规\n**M3** ±2.12pp 偏移在排名差异置信区间内还是外？\n**M4** Figure 1 右图 y 轴应标注条件概率\n\n### Missing References\n1. Adaptive Testing for LLM Evaluation (arxiv 2511.04689)\n2. JE-IRT (arxiv 2509.22888)\n3. Confident Rankings with Fewer Items (arxiv 2601.13885)\n4. When Benchmarks Leak: Inference-Time Decontamination (arxiv 2601.19334)\n\n### Questions\nQ1. 不同学科的 DIF enrichment ratio 差异的驱动因素？\nQ2. 更粗粒度定义 \"family\" 后 C% 如何变化？\nQ3. 是否考虑过与题目难度相关的注入方案？\nQ4. DIF-flagged items 是否应被排除出 Growing Pains 的 anchor sets？",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1512 · 2026-05-23T10:29:21.976267+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17834
}
```

</details>

---


### Tool call

_source line 1513 · 2026-05-23T10:29:22.127398+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] ETS 阈值从人类考试直接移植到 LLM 缺乏领域内校准\n- |Δ_MH| ≥ 1.5 对应的 odds ratio (~2.7:1) 在 LLM 评估中是否构成\"实质性显著\"未论证。教育 DIF 率 5-15%，本文 17.9-31.5%——差异可能因阈值不恰当。\n\n### Should-Fix\n\n**W1** [warning] DEFF 校正的 2× 不确定性削弱 headline 定量精度\n- Simple-mean (29.2%) vs weighted-mean (13.5%) 差距 ~2.2×。读者无法区分实践含义。Appendix I simulation 仅 4 种场景。\n\n**W2** [warning] Multiple testing 论证在超大样本下存在循环逻辑\n- N=5,227 下 p<0.05 几乎自动满足，BH-FDR 几乎无变化。论证是循环的。\n\n**W3** [warning] Semi-synthetic validation 使用 stylized injection 可能高估检测能力\n- Uniform binary flipping 是检测的\"最佳情况\"。difficulty-dependent injection 部分缓解但揭示了 instruct 模型的残差 gap (13×)。\n\n**W4** [warning] Base/instruct composition confound 未完全排除\n- 11.8pp composition gap，方向分布差异大。聚合 C% 仍可能被 composition shift 部分膨胀。\n\n### Minor\n\n**M1** LD 影响可能被低估\n**M2** Cross-benchmark 分析较薄\n**M3** GSM8K 复制描述过于简略\n**M4** Section 3.2 的有效 N 应澄清（实际 1,887 而非 5,227）\n**M5** Figure 1 子图标注不够醒目\n\n### Missing References\n- Martinková & Drabinová (2018) ShinyItemAnalysis\n- Chalmers (2012) mirt package\n- IRT-based benchmark compression 与 DIF-aware item selection 的关系\n\n### Questions\nQ1. |Δ_MH| = 1.5 在 LLM 场景下是否产生有意义的不同排名？\nQ2. ICC-family-size 若恒定（非负相关），simple-mean 是否仍优？\nQ3. Permutation simulation 的 SE 和直觉解释？\nQ4. Difficulty × model-type interaction 能解释多大比例的 DIF？\nQ5. K=3 vs K=5 vs K=10 对 DIF 检测率的影响？",
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] ETS 阈值从人类考试直接移植到 LLM 缺乏领域内校准\n- |Δ_MH| ≥ 1.5 对应的 odds ratio (~2.7:1) 在 LLM 评估中是否构成\"实质性显著\"未论证。教育 DIF 率 5-15%，本文 17.9-31.5%——差异可能因阈值不恰当。\n\n### Should-Fix\n\n**W1** [warning] DEFF 校正的 2× 不确定性削弱 headline 定量精度\n- Simple-mean (29.2%) vs weighted-mean (13.5%) 差距 ~2.2×。读者无法区分实践含义。Appendix I simulation 仅 4 种场景。\n\n**W2** [warning] Multiple testing 论证在超大样本下存在循环逻辑\n- N=5,227 下 p<0.05 几乎自动满足，BH-FDR 几乎无变化。论证是循环的。\n\n**W3** [warning] Semi-synthetic validation 使用 stylized injection 可能高估检测能力\n- Uniform binary flipping 是检测的\"最佳情况\"。difficulty-dependent injection 部分缓解但揭示了 instruct 模型的残差 gap (13×)。\n\n**W4** [warning] Base/instruct composition confound 未完全排除\n- 11.8pp composition gap，方向分布差异大。聚合 C% 仍可能被 composition shift 部分膨胀。\n\n### Minor\n\n**M1** LD 影响可能被低估\n**M2** Cross-benchmark 分析较薄\n**M3** GSM8K 复制描述过于简略\n**M4** Section 3.2 的有效 N 应澄清（实际 1,887 而非 5,227）\n**M5** Figure 1 子图标注不够醒目\n\n### Missing References\n- Martinková & Drabinová (2018) ShinyItemAnalysis\n- Chalmers (2012) mirt package\n- IRT-based benchmark compression 与 DIF-aware item selection 的关系\n\n### Questions\nQ1. |Δ_MH| = 1.5 在 LLM 场景下是否产生有意义的不同排名？\nQ2. ICC-family-size 若恒定（非负相关），simple-mean 是否仍优？\nQ3. Permutation simulation 的 SE 和直觉解释？\nQ4. Difficulty × model-type interaction 能解释多大比例的 DIF？\nQ5. K=3 vs K=5 vs K=10 对 DIF 检测率的影响？",
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1514 · 2026-05-23T10:29:23.591934+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1464
}
```

</details>

---


### Assistant

_source line 1515 · 2026-05-23T10:29:28.801099+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 145

## Round 145

2 recorded events


### User

_source line 1516 · 2026-05-23T10:29:31.469164+00:00_

[Reviewer 1 审稿结果]:
Reviewer 1 审稿完成。

**评分**: Overall 3.5/5 (Borderline Conference), Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5。

**核心判断**: 定性结论稳健（temporal DIF 以非平凡比例存在），方法学有实质贡献（cross-subject matching），但定量精度受三个关键校准问题制约：

1. **N1 [Must-Fix]**: ETS |Δ_MH| ≥ 1.5 阈值从人类考试直接移植到 LLM，缺乏领域内标定——教育测试 DIF 率 5–15%，本文 17.9–31.5%，差异 2–6×，未排除阈值过于宽松的可能
2. **W1–W4 [Should-Fix]**: DEFF 两种估计量差 2.2×（29.2% vs 13.5%）；multiple testing 论证在 N≈5,227 下本质循环；semi-synthetic validation 用最易检测的 uniform flipping；base/instruct composition confound 未完全排除
3. **M1–M5 [Minor]**: local dependence FPR inflation 估计 <0.001pp 偏低、cross-benchmark 分析较薄等

报告已通过 `review_reviewer_post_to_director` 提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1517 · 2026-05-23T10:29:37.322185+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 146

## Round 146

2 recorded events


### User

_source line 1518 · 2026-05-23T10:32:09.155754+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R1-N1: ETS 阈值缺乏 LLM 领域内校准**

同意这是论文的核心方法论盲点之一。|Δ_MH| ≥ 1.5 的 ETS Category C 阈值源自教育测量（Holland and Thayer, 1988），其含义是 odds ratio ≈ 2.7:1——在人类考生群体中构成"大效应"。但 LLM 不是人类考生：模型间的能力分布、响应机制、群体异质性都根本不同。

论文在 Section 3.2（page 4）将 ETS 阈值作为"standardized reference points and verify robustness across stricter cutoffs"，并在 Appendix A.1 提供了阈值灵敏度分析。但这只是展示了"换阈值结果如何变化"，没有回答"对 LLM 来说多大的 |Δ_MH| 构成实质性问题"——后者才是核心问题。

补充我自己的观察：论文报告的 DIF 率（17.9-31.5%）远高于教育测试文献中的典型值（5-15%），这一差距恰好可能反映阈值未经 domain-specific 校准。如果 LLM 响应模式的自然变异更大（例如因为模型架构差异远大于人类个体差异），|Δ_MH| ≥ 1.5 可能标记了大量实际无关紧要的差异。

**这与我的 N1（Contribution 1 概念深度不足）和 N2（methodological adaptations 过度声称）形成叠加：论文声称 "three methodological adaptations for LLM evaluation"，但最根本的 adaptation——阈值校准——恰好缺失。**

---

### Should-Fix

**[AGREE] R1-W1: DEFF 校正的 2× 不确定性**

同意。Simple-mean DEFF 给出 C% ≈ 29.2%，weighted-mean DEFF 给出 C% ≈ 13.5%（Appendix D, page 15），差距达 2.2×。论文在 Appendix I 的 DEFF simulation 仅覆盖 4 种家族结构场景，不足以让读者判断哪个估计更可靠。

论文的辩护——"even the conservative 13.5% exceeds the baseline by 75%+"（page 15）——在定性层面成立，但对于 headline finding 的定量精度是个问题。读者面对 "17.9-31.5%" 的 C% 范围，再叠加 DEFF 的 2× 不确定性，实际上不知道真实的 DIF 率是多少。

不过，我也注意到论文在 page 6 提供了 cluster bootstrap（26.7%）作为第三个参考点，与 simple-mean（29.2%）较接近，这暗示 weighted-mean 可能过于保守。但论文没有明确推荐使用哪个估计，这是需要修复的。

**[REBUT] R1-W2: Multiple testing 循环逻辑**

部分不同意。R1 的核心论点是"N=5,227 下 p<0.05 几乎自动满足，BH-FDR 几乎无变化，论证是循环的"。

确实，论文在 page 4 承认 "applying BH-FDR at q = 0.05 reclassifies only 3 of 3,918 C items"——FDR 几乎不起作用。但这并不构成循环逻辑，因为：

1. **ETS C 分类的约束性条件是 effect size（|Δ_MH| ≥ 1.5），不是 p-value。** p < 0.05 只是 AND 条件之一。在大 N 下 p-value 确实近乎退化，但 effect size 阈值仍在执行实质性过滤。这是 ETS 系统设计的一部分——大样本下转向 effect size 驱动的分类。
2. 论文的 Table 2 sensitivity check（page 7）展示了 ability-matched quintiles 和 cross-subject matching 下 C% 的稳健性，这些控制独立于 p-value 校正。
3. 实际有效比较的 N 是 1,080 vs 807（Section 4.2, page 6），不是 5,227——每个 item 的 contingency table 只用这些 model 数。

但我同意论文应该更明确地承认 p-value 在大样本下的退化性，并强调 ETS C 分类本质上是 effect-size 驱动的。当前表述给人一种 p-value 和 effect size "双重保障"的印象，实际上只有 effect size 在起作用。

**[AGREE] R1-W3: Semi-synthetic validation 的 stylized injection 局限**

同意。Uniform binary flipping 确实是检测的"最佳情况"（best-case scenario）：信号均匀、清晰、无混淆。实际的 contamination 效应可能是 difficulty-dependent、domain-specific、甚至 item-format-specific 的。

论文在 Appendix B（page 14）提供了 difficulty-dependent injection 分析，显示 instruct 模型的残差 gap 达 13×（"the observed difficulty–direction correlation (ρ = −0.597)"），这实际上是 R1 关切的有力证据——difficulty-dependent 效应确实存在。论文的 Limitations section（page 8）也承认 "a stylized injection model; reported ΔTPR values may overestimate detection power"。

但我认为这一局限不完全是 Must-Fix 级别。原因：(1) 半合成框架的目的是验证 MH-DIF 的灵敏度下界（"can it detect DIF when present"），而非声称完美模拟真实污染；(2) 论文提供了 TPR 和 FPR 的定量报告（Figure 2, Table 4），读者可以自行评估。需要改进的是更明确地声明这是 sensitivity analysis 而非 power estimation。

**[REBUT] R1-W4: Base/instruct composition confound**

不完全同意。R1 担心 "聚合 C% 仍可能被 composition shift 部分膨胀"。但论文在多处提供了直接的反驳证据：

1. **Appendix O（page 18, Table 15）**: Base-only temporal DIF C% = 32.1%，instruct-only temporal DIF C% = 36.5%——两个纯子群独立展现了高 DIF 率，消除了 composition confound 作为主因的可能性。
2. **Section 5.1（page 7-8）**: "Training methodology modulates DIF direction...rather than DIF magnitude, providing direct evidence against composition shift as the primary driver."
3. **Appendix N（page 18）**: Within-architecture 分析（Llama-2 vs Llama-3）显示 C% ≈ 28-29%，控制了架构差异。
4. **Table 2（page 7）**: ability-matched quintiles 下 C% 仍为 17.9-31.5%。

R1 说 "11.8pp composition gap" 是一个 confound——但论文的 base-only/instruct-only 分析正是为了排除这个 confound，且两个子群的 C% 都在 30%+ 水平。聚合 C% 的方向分布差异确实存在（base 偏 reference-favoring，instruct 偏 focal-favoring），但这说明 composition 影响的是 DIF 方向而非检出率。

不过，论文可以更清楚地在 main text（而非只在 Appendix O）展示这一 decomposition 结果。

---

### Minor

**[AGREE] R1-M1: LD 影响可能被低估**
同意这值得关注。论文使用 Yen's Q3 诊断局部依赖（Appendix A.1），但 MMLU 的题目按学科分组，可能存在 testlet 效应。不过，cross-subject matching 策略（Section 3.2）在一定程度上缓解了这个问题，因为匹配变量来自不同基准。

**[AGREE] R1-M2: Cross-benchmark 分析较薄**
同意。Table 3 展示了 6 个基准的 C%（17.9% 到 33.3%），但没有深入分析跨基准差异的原因。例如，为什么 knowledge/reasoning 基准的 C% 更高？是因为这些基准更容易被污染，还是因为能力维度更容易随时间变化？这种分析会增加论文的 insight。

**[AGREE] R1-M3: GSM8K 复制描述过于简略**
同意。GSM8K 作为 cross-benchmark validation 的一个关键点（Section 1, page 2 提到 "Replicated on GSM8K"），但正文中的描述不够详细。应至少在附录中提供 GSM8K 的完整 DIF 分析结果。

**[AGREE] R1-M4: 有效 N 应澄清**
同意。Section 3.1 提到 5,227 models，但实际 temporal comparison 使用的是 2023 (N=1,080) vs 2024 (N=807)，有效 N=1,887（Section 4.2, page 6）。5,227 是全部模型数（含 5 个 cohort design），应在 Section 3.1 明确区分。这避免了读者误以为每个 item 的 contingency table 有 5,227 个观测。

**[AGREE] R1-M5: Figure 1 子图标注**
同意，minor visual issue。左图 "Global Contamination" 和右图 "Differential Contamination" 的标注可以更醒目。

---

### Missing References

**[AGREE] R1-Missing: Martinková & Drabinová (2018) ShinyItemAnalysis**
合理建议。ShinyItemAnalysis 是 DIF 分析的常用工具，对想复现结果的读者有参考价值。

**[AGREE] R1-Missing: Chalmers (2012) mirt**
合理建议。mirt 是 R 语言中最主要的 IRT/DIF 包之一。即使论文没有使用它，作为方法论文献引用是合适的。

**[REBUT] R1-Missing: IRT-based benchmark compression 与 DIF-aware item selection 的关系**
这更像是 future work 的方向而非 missing reference。论文的 scope 是 DIF 检测和审计，不是 item selection 或 benchmark compression。不过可以在 Discussion 中简要提及这一连接点。

---

### Questions

**[AGREE] R1-Q1 值得回答**: |Δ_MH| = 1.5 在 LLM 排名中的实际影响。论文报告了 ±2.12pp 的平均校正位移（Section 4.6），但没有直接展示阈值处的排名变化。一个 case study 会很有说服力。

**[AGREE] R1-Q2 值得回答**: ICC-family-size 相关性对 DEFF 估计方法选择的影响。当前论文报告两个 bound 但不做推荐，读者需要明确指导。

**[AGREE] R1-Q3 值得回答**: Permutation simulation 的 SE 会帮助读者理解 Section 4.1 的 Monte Carlo power analysis 的稳定性。

**[AGREE] R1-Q4 重要**: Difficulty × model-type interaction 能解释多大比例的 DIF 是一个关键的 decomposition 问题。Appendix B 的 difficulty-direction correlation（ρ = −0.597）和 Appendix O 的 model-type 分析提供了部分答案，但没有联合分析。

**[AGREE] R1-Q5 值得回答**: K 的选择（quintile binning）对 C% 的灵敏度。论文使用 K=5（Section 3.2），Appendix H 报告 K=3 vs K=5 结果相近，但 K=10 未测试。

---

### 总结

R1 的审稿整体质量高，关注点与我的审稿存在显著重叠但侧重不同：

**重叠共识**:
- 我们都认为论文的经验工作扎实（scale + controls），但贡献新颖性定位存在问题
- 我们都给出 3.5 (Borderline Conference)
- ETS 阈值校准问题（R1-N1）与我的 N1/N2（贡献声称过度）共同指向同一个根源：论文声称 "methodological adaptations for LLM evaluation" 但最关键的 adaptation（阈值校准）恰好缺失

**互补视角**:
- R1 侧重方法论的技术细节（DEFF 不确定性、multiple testing、K 值选择）
- 我侧重贡献框架和叙事（Contribution 1/3 的过度声称、Discussion 深度、mechanism inference）
- 两者结合给出了完整画面：论文的经验发现有价值，但方法论新颖性和贡献叙事都需要校准

**对最终评分的影响**: R1 的 N1（ETS 阈值）如果与我的 N2（methodological adaptations 过度声称）叠加考虑，论文的方法论贡献会进一步被削弱。但即使在保守阈值（|Δ_MH| ≥ 2.0）下，论文报告 C% 仍为 17.9%+ (Table 2 sensitivity)，核心发现不会被推翻。我维持 3.5 的评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1519 · 2026-05-23T10:32:21.368179+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 147

## Round 147

2 recorded events


### User

_source line 1520 · 2026-05-23T10:32:23.994367+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **7 条 AGREE**（N1 阈值校准、W1 DEFF 不确定性、W3 注入模型局限、M1-M5 小问题）
- **2 条 REBUT**（W2 multiple testing 并非循环逻辑——effect size 是约束性条件；W4 composition confound 已被 Appendix O 的 base-only/instruct-only 分析充分排除）
- **1 条部分 REBUT**（missing ref 中 IRT-based benchmark compression 属于 future work 而非 missing reference）

R1 和我的审稿在评分（均为 3.5）和核心判断（经验工作扎实但新颖性定位有问题）上高度一致。R1 的 N1（ETS 阈值未校准）与我的 N2（"three methodological adaptations" 过度声称）形成叠加效应——论文声称为 LLM 做了方法论适配，但最关键的适配（阈值重新校准）恰好缺失。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1521 · 2026-05-23T10:32:38.447606+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 148

## Round 148

12 recorded events


### User

_source line 1522 · 2026-05-23T10:32:39.951742+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: Contribution 1（global exposure vs. DIF 独立性）的贡献度**

R2 认为 global exposure 和 differential functioning"定义上就是不同构念"，因此低 Jaccard（≈ 0.206）只是在"确认显而易见的事实"。我不完全同意。

**证据与理由：**
1. 定义上不同 ≠ 经验上必然独立。contamination detection 文献的隐含假设恰恰是：global exposure（item 出现在训练数据中）会导致 differential functioning（模型在该 item 上表现异常）。MinK++ (Shi et al., 2024)、Time Travel (Golchin and Surdescu, 2024) 等方法正是基于这一假设运作的。如果二者真的"显而易见地独立"，这些方法的理论基础就需要重新审视。
2. 论文提供了具体的定量证据：Jaccard ≈ 0.206, Enrichment ratio ≈ 1.0（Section 4.3, Figure 1），permutation null (Jaccard = 0.206, p = 0.88)。这不是重述定义，而是对一个被广泛默认成立的假设的实证否证。
3. 同时，Abstract 明确指出 "aggregate rankings are robust (ρ ≈ 0.997), but absolute scores are not directly comparable"——即 global exposure 不影响排名但 DIF 影响绝对分数。这一区分在先前文献中没有被系统建立。

**部分同意点：** 我同意将此作为"三大贡献之首"的位置可以商榷——它更适合作为背景性的 empirical observation 来激发后续方法学贡献，而非独立的 headline contribution。建议作者调整 Introduction 中三个 contribution 的排序和权重表述。

---

**[REBUT] R2-N2: "Three methodological adaptations" 的新颖性**

R2 认为三项适配均不构成方法论贡献：(a) cross-subject matching 是"实施决策"，(b) DEFF 借用 survey methodology，(c) semi-synthetic validation 是验证策略。我对 (a) 强烈反驳，对 (b)(c) 部分同意。

**对 (a) Cross-subject matching 的反驳：**
- 这不是标准实施决策。教育测量中 MH-DIF 的标准做法是使用 within-test total score 作为 matching variable（Holland and Thayer, 1988; Donoghue and Allen, 1993）。论文的创新在于：当 matching variable 本身可能被 contamination 污染时（benchmark 的 total score 包含了被 contaminate 的 items），使用 cross-subject total score 排除被测 subject，从构造上保证 ΔFPR = 0（Section 3.4，含形式化推导）。
- 这一保证是 formal result，不是 engineering choice。Section 3.4 给出了严格证明：single-subject injection 下，被测 subject 的 items 不进入 matching variable，因此注入不影响 matching，ΔFPR = 0 by construction。
- Table 7（Section 4.5）的实证验证进一步支持：single-subject injection 下 ΔFPR = 0.000（所有 MMLU subjects），而 within-subject matching 下 ΔFPR 则显著膨胀（+0.186）。这不是"显然的实施选择"——它解决了将 DIF 应用到 contaminated benchmarks 时一个此前未被形式化的 matching variable corruption 问题。

**对 (b) DEFF correction 的部分同意：**
- R2 说得对，DEFF 概念源自 survey methodology（Kish, 1965）。但将其适配到 LLM model-family 结构需要非平凡的工作：计算 family-level ICC、处理 heterogeneous family sizes、在 Appendix I 中通过 simulation 比较 simple-mean vs. weighted-mean 估计量。称之为"adaptation"而非"original contribution"更准确。

**对 (c) Semi-synthetic validation 的同意：**
- 我同意 semi-synthetic injection 更接近 validation strategy 而非 methodological contribution。论文用 "validation" 一词本身是准确的，但将其列为三大"methodological adaptations"之一确实拉升了新颖性声称。

**建议：** 论文可将 (a) cross-subject matching 单独突出为主要方法学贡献（含 formal guarantee），将 (b)(c) 降级为"supporting methodological choices"或"complementary validation"。

---

### Should-Fix

**[AGREE] R2-W1: §5.2 审计协议中的 mechanism inference**

R2 指出"DIF on web-clean items suggests capability shift"超出了 DIF 方法的能力边界。我同意这一批评。

DIF by design 是 mechanism-agnostic 的（论文自身在 Limitations 中承认这一点）。虽然 §5.2 使用了 "suggests" 而非 "proves" 的措辞，但在审计协议这种规范性建议中，即便是"suggests"也可能被误读为因果推断。

**补充意见：** 论文可改为更保守的表述，如："DIF on web-clean items is inconsistent with contamination as the sole mechanism"——这是 MH-DIF 结合 web-overlap labels 可以支持的排除性推理，不需要正面声称是"capability shift"。

---

**[AGREE] R2-W2: Discussion 缺乏深层 insight（部分同意）**

§5.1 确实更像是附加的实验分析（base/instruct 分层、model family profiles、difficulty-direction interaction）而非对 temporal DIF 成因的深层讨论。我部分同意。

**但有两点需要补充：**
1. 论文的核心贡献是 empirical audit 而非 mechanistic explanation。在 8 页限制下，合理的选择是将 Discussion 聚焦在最直接可操作的内容（审计协议），而非对缺乏数据支撑的因果机制进行推测。
2. §5.1 中 base/instruct 方向差异（base: 61.1% reference-favoring, ρ = −0.528; instruct: 65.6% focal-favoring, ρ = −0.079, Section 5.1/Appendix O）不仅是结果报告——它提供了 structured signal 的证据，表明 DIF 不是随机噪声而是与训练方法论相关的系统性模式。这超越了简单的结果重述。

---

**[AGREE] R2-W3: Abstract 信息密度过高**

同意。15+ 个数值在单段 abstract 中确实影响可读性。这是可以在 revision 中轻松改善的表达问题。

---

**[REBUT] R2-W4: Limitations 覆盖面偏窄（部分反驳）**

R2 认为应补充：(1) 对 MMLU 式 MCQ 以外基准的泛化性，(2) 模型发布日期与训练数据截止不对齐，(3) Li et al. web-overlap 标签自身局限性。

**反驳理由：**
1. 关于泛化性：论文在 Section 4.7 已在 GSM8K（数学问题，非传统 MCQ）上完成了 cross-benchmark 复制，且 Table 3 报告了 6 个 METABENCH benchmarks 的 DIF 率（20.7%–48.4%），涵盖了不同题型。Limitations 中不需要重复讨论已有实证覆盖的问题。
2. 关于 web-overlap 标签局限性：论文的核心发现恰恰是 DIF flags 与 web-overlap labels 近似独立（Jaccard ≈ 0.206），因此 web-overlap labels 的局限性主要影响 Section 4.3 的 ground truth comparison，而不影响论文的主要 DIF 分析。

**同意点：** 模型发布日期与训练数据截止不对齐是一个值得在 Limitations 中提及的有效关切——temporal cohort 按 release date 划分，但模型的训练数据可能跨越了这些边界。

---

### Minor

**[AGREE] R2-M1:** 术语一致性是合理的要求。"temporal score incomparability" 和 "measurement non-invariance" 应在首次出现时明确对应关系。

**[AGREE] R2-M2:** `\enlargethispage*{4\baselineskip}` 确实是潜在的格式风险。虽然 ACL 模板没有明确禁止此命令，但如果它导致正文页面实际内容超出标准行数，可能被 reviewer/AC 标记。我在首轮审稿中未检查 LaTeX 源码层面的格式合规性，这是一个有价值的补充。

**[AGREE] R2-M3:** ±2.12pp 偏移是否在排名差异的置信区间内——这是一个好问题。论文报告了 DIF-corrected scores 的 rank displacement（Section 4.6: "Among the 200 most displaced models (top 3.8%), 33.6% of pairwise rankings reverse"），但未将 ±2.12pp 与排名不确定性的 baseline（如 bootstrap confidence interval of rank）进行比较。如果 ±2.12pp 落在 typical ranking noise 范围内，DIF correction 的实际价值会被削弱。

**[AGREE] R2-M4:** Figure 1 右图 y 轴标注条件概率是合理的改进建议。

---

### Missing References

R2 提出的 4 篇论文（Adaptive Testing for LLM Evaluation, JE-IRT, Confident Rankings with Fewer Items, When Benchmarks Leak）如果确实存在且相关，是合理的补充。但我无法当场验证这些 arXiv ID 的真实性——建议 Director 确认后转达给作者。其中 "Adaptive Testing for LLM Evaluation" 和 "JE-IRT" 可能与论文的 IRT 方法论直接相关，值得优先考虑。

---

### Questions

**[对 R2-Q1 的回应]** Subject-level DIF enrichment ratio 差异：Table 6（Domain-level Cohen's d）和 Table 1 提供了部分 subject-level 数据。论文指出 knowledge-grounding benchmarks 的 C% 高于 procedural ones（Table 3: HellaSwag 17.9% vs. MMLU 31.5%），暗示知识密集型 items 更易受 temporal DIF 影响。但详细的 subject-level 驱动因素分析确实缺失。

**[对 R2-Q2 的回应]** 更粗粒度的 family 定义：Appendix D（Size-stratified DEFF）和 Appendix H（LOFO robustness）提供了相关信息。Table 9 按 tier（<10, 10-50, 50-200, >200 members）分析了 ICC 和 DEFF。粗粒度 family 定义可能降低 ICC（因家族内异质性增加），进而减小 DEFF correction，但论文没有直接测试这一变体。这是一个有价值的 robustness check。

**[对 R2-Q3 的回应]** Difficulty-dependent injection：已在 Appendix G 中覆盖（mixed-mechanism injection, Scheme D and E）。论文发现 difficulty-dependent injection 能复制 overall DIF direction gradient 但不能复制 instruct-model 的 near-zero reversal。这部分回答了 Q3。

**[对 R2-Q4 的回应]** DIF-flagged items 与 Growing Pains anchor sets：这是一个好的应用建议，值得在 Discussion 中提及。Growing Pains（Habba et al., 2026）使用 IRT calibration 建立 anchor items for equating——如果这些 anchor items 存在 temporal DIF，equating 的有效性会受影响。

---

### 总结

R2 的审稿侧重 novelty framing 和 presentation，与我（R1）侧重 statistical methodology 形成互补。我在 N2(a) 上强烈反驳——cross-subject matching 是 formal contribution 而非 implementation decision。在 N1 上部分反驳——global-vs-differential independence 不是定义上显然的。在 W1-W3 上基本同意。我认为 R2 的 overall 3.5 评分合理，但 N2 中对 cross-subject matching 新颖性的低估可能导致了过于保守的评价。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1523 · 2026-05-23T10:33:25.605107+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1524 · 2026-05-23T10:33:25.706623+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T10:18:58.814659+00:00\", \"completed_at\": \"2026-05-23T10:23:26.705379+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主文超页：Section 5 Discussion 从 page 8 下半开始，Section 6 Conclusion 位于 page 9 右栏中部。主文（Sections 1-6）约占 8.3-8.5 页，超出 EMNLP 2026 的 8 页限制。Limitations 和 References 虽不计入，但 Conclusion 仍在第 9 页。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页无 figure/table：Related Work（pp.3-4）+ Method（pp.4-5）纯文本段。Page 4 有公式穿插稍微缓解，但 Section 3 Method 缺少流程/框架概览图，审稿人需要纯靠阅读理解 DIF audit pipeline。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点：Title + Abstract + Intro 全文本。Figure 1 在 page 2 出现已算较早，但如果能将 Figure 1 提升到 page 1（或在 page 1 加一个小型概念图），可强化审稿人第一印象。\"}, {\"severity\": \"info\", \"dimension\": \"pages 16-17\", \"message\": \"附录 Figures 3-6 尺寸偏小，axis label 字号接近可读性下限（约 6-7pt），打印场景下可能模糊。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 使用红/蓝配色，线型（实线 vs 虚线）提供冗余编码，色盲安全性可接受但非最优（建议 Okabe-Ito 或 blue+orange）。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 全宽表格列数较多（6 个 benchmark + 多个 metric），信息密度高但可读。最优值已加粗。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-11\", \"message\": \"参考文献格式统一，无 [?] 未解析引用，排版正常。\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"无 margin 溢出、无公式渲染错误、无 section heading 孤悬页底、所有表格均使用 booktabs 风格。\"}], \"counts\": {\"critical\": 1, \"warning\": 2, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1525 · 2026-05-23T10:33:25.707183+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1526 · 2026-05-23T10:33:25.757748+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1527 · 2026-05-23T10:34:08.641807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1528 · 2026-05-23T10:34:08.793418+00:00_

1	issues:
2	  # === Round 15 issues (Action Matrix locked, dispatched to Paper Agent) ===
3	
4	  - id: "R15-N1"
5	    summary: "DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分"
6	    category: method
7	    severity: critical
8	    status: in_progress
9	    first_raised_round: 13
10	    last_seen_round: 15
11	    mentions:
12	      - round: 13
13	        reviewers: [1, 2]
14	        note: "R13-W2: 首次提出"
15	      - round: 14
16	        reviewers: [1, 2]
17	        note: "R14-W2: 再次独立提出"
18	      - round: 15
19	        reviewers: [1, 2]
20	        note: "R1-N1 升级为 Must-Fix。mega-family size-dependent ICC 导致 weighted-mean over-correct。"
21	    action_items:
22	      - round: 15
23	        action: "§4.2 并列呈现两种估计 + 解释 size-dependent ICC 导致 weighted-mean over-correct + 引用 App I simulation + 强调 13.5% 仍是 75× baseline。Abstract/Intro/Conclusion 加 conservative bound。[复发×3轮，之前只做 writing hedge → 本轮 surfacing evidence to 正文]"
24	        assigned_to: paper_agent
25	        status: in_progress
26	    resolution: ""
27	    resolution_round: null
28	
29	  - id: "R15-N2"
30	    summary: "Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定外部效度受限"
31	    category: method
32	    severity: critical
33	    status: in_progress
34	    first_raised_round: 13
35	    last_seen_round: 15
36	    mentions:
37	      - round: 13
38	        reviewers: [1, 2]
39	        note: "R13-W3: 首次提出"
40	      - round: 14
41	        reviewers: [1, 2]
42	        note: "R14-W3: 标题改为 Detection Power under Controlled Injection"
43	      - round: 15
44	        reviewers: [1, 2]
45	        note: "共识 Must-Fix。uniform flipping 不是 worst-case，可能是 easiest-to-detect。"
46	    action_items:
47	      - round: 15
48	        action: "术语 worst-case→stylized; upper-bound→may overestimate; 加入 R19 difficulty-dependent ΔTPR≈0.41 vs uniform 0.51（~20% reduction）+ ρ signatures（+0.77/-0.52/+0.39）。[复发×3轮，之前只改术语 → 本轮加 evidence]"
49	        assigned_to: paper_agent
50	        status: in_pr
…[truncated 16454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1529 · 2026-05-23T10:38:37.490612+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 16 issues ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准——核心定量声称的基础\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-W1: warning 级别，threshold sensitivity + random baseline 部分缓解\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix (N1)。R2 交叉回应 AGREE 并叠加：'论文声称 methodological adaptations for LLM 但最关键的 adaptation（阈值校准）恰好缺失'。论文已加 sensitivity analysis (18.3% at ≥2.0, 10.2% at ≥2.5) 和 'standardized reference points' 措辞，但未做 LLM-specific calibration（如 random-split null 分布的 percentile、rank displacement per threshold）。共识 Must-Fix。\"\n    action_items:\n      - round: 16\n        action: \"提供 LLM-specific 实证锚定：(1) random-split |Δ_MH| 分布的 95th percentile 作为 empirical null; (2) rank displacement 随阈值变化的分析; (3) 明确承认 ETS 分类在 LLM 中是 effect-size 驱动的标准化参考点而非经过领域校准的阈值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 1（global-vs-differential 正交性）和 Contribution 3（three methodological adaptations）的贡献声称均存在过度定位\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W6: 方法论新颖性有限\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7/N2: innovations→adaptations; 正交性可能是概念预期\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N3/I1: framework→adaptations 改善但 Related Work 自矛盾；正交性降级为 info\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2 升级 C1 为 Must-Fix (N1)：'确认显而易见的事实'。R1 REBUT C1：contamination 文献隐含假设 exposure→DIF，实证否证有价值，但同意不应是 #1 贡献。R2 升级 C3 为 Must-Fix (N2)：DEFF 借用、semi-synthetic 是验证策略。R1 强力辩护 cross-subject matching（formal ΔFPR=0 guarantee，非 implementation decision），同意 DEFF/semi-synthetic 定位偏高。【分歧】：cross-subject matching 的新颖性——R1 认为是 formal contribution，R2 认为是 engineering choice。\"\n    action_items:\n      - round: 16\n        action: \"重构三项贡献：(1) C1 降级为 motivating empirical observation 或合并入 C2; (2) C3 突出 cross-subject matching 的 formal guarantee 为主要方法学贡献，DEFF/semi-synthetic 降为 supporting choices; (3) 消除 Related Work 中任何自矛盾措辞\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 校正两种估计量差异 2× 削弱 headline 定量精度\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次提出\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N1 升级为 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2 AGREE。论文已加 simulation (App I) + size-stratified DEFF (Table 8) + cluster bootstrap 26.7% 作为第三参考点。改善明显但仍缺推荐估计量。R2 指出 cluster bootstrap 与 simple-mean 接近暗示 weighted-mean 过保守，但论文未明确推荐。降级为 Should-Fix（已有证据链，缺明确推荐）。\"\n    action_items:\n      - round: 16\n        action: \"在 §4.2 或 Discussion 中明确推荐 simple-mean DEFF 作为 primary estimate（基于 simulation evidence + cluster bootstrap convergence），将 weighted-mean 定位为 conservative bound\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W2\"\n    summary: \"§5.2 审计协议从 mechanism-agnostic 的 DIF 推断因果机制，措辞超出方法能力\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-W7: 增加决策启发式\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1 AGREE。论文加了 3 条 heuristic 但 'suggests capability shift' 仍是正面因果声称。R1 建议改为排除性推理：'inconsistent with contamination as sole mechanism'。共识 Should-Fix。\"\n    action_items:\n      - round: 16\n        action: \"§5.2 将 'suggests capability shift' 改为排除性推理措辞（如 'inconsistent with contamination as sole mechanism'）; 加 caveat 'DIF alone cannot determine causation'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W3\"\n    summary: \"Discussion (§5) 缺乏深层 insight，§5.1 本质是附加实验结果\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W2 新提出。R1 部分同意但指出 8 页限制制约 + §5.1 base/instruct 分层是 structured signal 证据而非简单重述。R1 认为 audit paper 合理聚焦操作建议而非未经数据支撑的因果推测。分歧程度低。\"\n    action_items:\n      - round: 16\n        action: \"在 §5 增加 1-2 段讨论 temporal DIF 对 LLM 评测生态的系统性影响（排行榜解读、benchmark 维护策略），超越结果重述\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高（15+ 数值堆砌），影响可读性\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N1: info 级别\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W3 重新提出为 Should-Fix + R1 AGREE。论文 abstract 仍含 15+ 数值。共识应精简。\"\n    action_items:\n      - round: 16\n        action: \"Abstract 保留核心数字（规模、DIF 率、分数位移），统计检验细节移至 Introduction\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W5\"\n    summary: \"主文超页：Conclusion 位于 page 9，\\\\enlargethispage 导致 page overflow\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W5: enlargethispage 使用激进\"\n      - round: 15\n        reviewers: [2]\n        note: \"改善至 4\\\\baselineskip\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-M2 标记格式风险。视觉审查 critical finding：Sections 1-6 约占 8.3-8.5 页，Conclusion 位于 page 9。EMNLP 2026 strict 8-page limit。\"\n    action_items:\n      - round: 16\n        action: \"压缩正文至 strict 8 页：移除 \\\\enlargethispage；压缩 §2 Related Work 或 §5 Discussion 约 0.3-0.5 页\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W6\"\n    summary: \"Semi-synthetic validation 的 uniform flipping 是 upper bound，ΔTPR 应标为检测力上界\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W3\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N2 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W3 + R2 AGREE。论文已加 difficulty-dependent injection (App G) + 'stylized/may overestimate' 措辞。改善明显。R2 认为不完全是 Must-Fix（框架目的是 sensitivity analysis 非 power estimation）。降级为 Should-Fix。残余问题：instruct 模型残差 gap 13×。\"\n    action_items:\n      - round: 16\n        action: \"正文中明确 ΔTPR 是 upper bound 而非 point estimate；考虑更具挑战性的 injection scheme（如 graded injection with noise）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致：temporal score incomparability vs measurement non-invariance\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W6\"\n      - round: 15\n        reviewers: [2]\n        note: \"仍有少量混用\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-M1 + R1 AGREE。需在 §1 明确 measurement non-invariance（机制）vs temporal score incomparability（后果）的对应关系。\"\n    action_items:\n      - round: 16\n        action: \"§1 首次出现时明确对应关系\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M2\"\n    summary: \"有效 N=1,887（temporal cohort）vs 总 N=5,227 需要在 §3.1 澄清\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [1]\n        note: \"R1-M4。§3.2 提到 'At N=5,227' 但 temporal comparison 实际使用 N_ref=1,080, N_focal=807。R2 AGREE。\"\n    action_items:\n      - round: 16\n        action: \"§3.1 明确区分全量模型数与 temporal cohort 有效 N\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M3\"\n    summary: \"遗漏近期 IRT-for-LLM 相关工作（4 篇）和 DIF 工具文献（2 篇）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2 建议 4 篇（Adaptive Testing arxiv 2511.04689, JE-IRT arxiv 2509.22888, Confident Rankings arxiv 2601.13885, Benchmarks Leak arxiv 2601.19334）。R1 建议 2 篇（ShinyItemAnalysis Martinková 2018, mirt Chalmers 2012）。R1 提醒需先验证 R2 建议的 arXiv ID 真实性。\"\n    action_items:\n      - round: 16\n        action: \"WebSearch 核实 6 篇引用真实性后择优加入 §2\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 15 issues with R16 status updates ===\n\n  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 升级为 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"论文已加 simulation (App I) + stratified DEFF + cluster bootstrap 26.7%。改善明显。R16 降级为 Should-Fix (R16-W1)。残余：缺明确推荐哪个估计量。\"\n    action_items:\n      - round: 15\n        action: \"§4.2 并列呈现两种估计 + 解释 size-dependent ICC 导致 weighted-mean over-correct + 引用 App I simulation + 强调 13.5% 仍是 75× baseline\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Simulation + stratified DEFF + cluster bootstrap added. Downgraded to Should-Fix in R16 (R16-W1). Remaining: explicit recommendation needed.\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W3\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N2 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"论文加了 difficulty-dependent injection + 'stylized/may overestimate' 措辞。改善明显。R16 降级为 Should-Fix (R16-W6)。\"\n    action_items:\n      - round: 15\n        action: \"术语 worst-case→stylized; upper-bound→may overestimate; 加 difficulty-dependent injection\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Terminology fixed + difficulty-dependent injection added. Downgraded to Should-Fix in R16 (R16-W6).\"\n    resolution_round: null\n\n  - id: \"R15-N3\"\n    summary: \"框架贡献被过度声称（Contribution 3 vs Section 2 自述矛盾）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W6\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N3\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"论文改 framework→adaptations，统一了两处。但 R2 仍认为 overclaimed（N2），R1 辩护 cross-subject matching 的 formal contribution。合并入 R16-N2。\"\n    action_items:\n      - round: 15\n        action: \"Contribution 3: framework→adaptations; related_work: 消除自矛盾\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Terminology unified. Merged into R16-N2 for further refinement.\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"threshold sensitivity + random baseline 部分缓解\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix。合并入 R16-N1。\"\n    action_items:\n      - round: 15\n        action: \"§3.2 加 ETS 阈值适切性讨论\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Escalated to Must-Fix in R16. Merged into R16-N1.\"\n    resolution_round: null\n\n  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"已在 method.tex §3.2 处理\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W2 再提。R2 REBUT：effect size 是约束性条件，非循环逻辑。论文 §3.2 已有详细讨论（DEFF restores p-value selectivity）。分歧解决：R2 的 rebuttal 更有说服力。残余：应更明确承认 p-value 在大样本下退化。\"\n    action_items:\n      - round: 15\n        action: \"确认 §3.2 现有讨论充分\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Mostly addressed. §3.2 discusses DEFF restoring p-value selectivity. R2 rebuttal convincing. Minor wording improvement needed.\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"Within-family DIF（Llama-2 vs 3, C%=59.2%）与架构/能力代际差异混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"App N 逻辑可能相反\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。论文 §5.1 + App N 已重新框架化：raw 59.2% → ability-matched ~28-29%。\"\n    action_items:\n      - round: 15\n        action: \"App N + §5.1 重新框架化\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Likely addressed. R16 did not re-raise. Paper now shows ability-matched convergence.\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"GSM1K 相关性正文用 'confirms' 语气但应保持 exploratory 定位\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"Figure 5 caption 标 exploratory 但正文 confirming 语气\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。论文 §4.7 现用 'exploratory cross-benchmark signal' + 'small sample requires replication'。\"\n    action_items:\n      - round: 15\n        action: \"正文 confirms→suggests\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Likely addressed. R16 did not re-raise. Current language uses 'exploratory' and 'requires replication'.\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"Local independence 违反（Yen's Q3）的定量影响未与 DIF detection rate 关联\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"DEFF 处理 model-level，Q3 是 item-level\"\n      - round: 16\n        reviewers: [1]\n        note: \"R1-M1 简要提及。论文已加 permutation simulation <0.001pp (§3.2 LLM-specific challenges)。R2 AGREE 值得关注但 cross-subject matching 部分缓解。\"\n    action_items:\n      - round: 15\n        action: \"引用 plan_035 结果\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Permutation simulation result now in paper. Minor residual concern.\"\n    resolution_round: null\n\n  - id: \"R15-W6\"\n    summary: \"遗漏 concurrent work：CoDeC（ICLR 2026）\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"CoDeC in-context learning 污染检测\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。论文 §2 now includes Zawalski et al. (2026) CoDeC。\"\n    action_items: []\n    resolution: \"CoDeC now cited in §2 Related Work (Zawalski et al., 2026). R16 did not re-raise.\"\n    resolution_round: 16\n\n  - id: \"R15-W7\"\n    summary: \"可操作性缺口：DIF 是 mechanism-agnostic 但推荐 mechanism-conditional responses\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"增加决策启发式\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1 AGREE。论文加了 heuristics 但 'suggests capability shift' 措辞仍超出方法能力。合并入 R16-W2。\"\n    action_items:\n      - round: 15\n        action: \"§5.2 加决策启发式\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Heuristics added but mechanism inference language persists. Merged into R16-W2.\"\n    resolution_round: null\n\n  - id: \"R15-I1\"\n    summary: \"'两维度正交'作为 Contribution 1 的新颖性存疑\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2 Must-Fix vs R1 REBUT 降级为 info\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2 再次升级为 Must-Fix (N1)。R1 REBUT：contamination 文献隐含假设 exposure→DIF，实证否证有价值。但同意不应是 #1 贡献。分歧存在但方向一致（需重新定位）。合并入 R16-N2。\"\n    action_items:\n      - round: 15\n        action: \"Contribution 1 调整为 empirical quantification\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed by reframing. Merged into R16-N2 for further restructuring.\"\n    resolution_round: null\n\n  - id: \"R15-I2\"\n    summary: \"视觉节奏不均：连续多页无 figure/table\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"视觉审查\"\n      - round: 16\n        reviewers: []\n        note: \"R16 视觉审查确认 pages 3-5 连续 3 页无 figure/table。建议 Method section 加框架概览图。\"\n    action_items:\n      - round: 16\n        action: \"如空间允许，在 §3 加 DIF audit pipeline 概览图\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-NEW1\"\n    summary: \"Discussion 加 Contrasts with Educational DIF 段\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"列出 LLM DIF 与教育 DIF 的质的差异\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。论文 §5.1 现含 3 个 LLM-education 对比。\"\n    action_items: []\n    resolution: \"Addressed. §5.1 now includes three contrasts with educational DIF settings.\"\n    resolution_round: 16\n\n  - id: \"R15-Q1\"\n    summary: \"Base-only 和 instruct-only 分别做 temporal DIF 的 C%\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [2]\n        note: \"分离 temporal 和 training methodology 贡献\"\n      - round: 16\n        reviewers: []\n        note: \"论文 Appendix O (Table 15) 现有完整结果：base-only C%=32.1%, instruct-only C%=36.5%。R16 R2 在交叉回应中引用此数据反驳 R1-W4。\"\n    action_items: []\n    resolution: \"Fully addressed. Appendix O Table 15 provides base-only and instruct-only temporal DIF results.\"\n    resolution_round: 16\n\n  # === Round 14 issues（R16 状态更新） ===\n\n  - id: \"R14-W1\"\n    summary: \"Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W1\"\n      - round: 15\n        reviewers: []\n        note: \"已引入 temporal score incomparability + mechanism-agnostic\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。标题和全文统一使用 'temporal score incomparability'，mechanism-agnostic 定位贯穿。\"\n    action_items: []\n    resolution: \"Addressed. Terminology changed to 'temporal score incomparability' throughout. Mechanism-agnostic positioning established. Not raised in R15 or R16.\"\n    resolution_round: 16\n\n  - id: \"R14-W4\"\n    summary: \"缺少 base/instruct composition shift 的直接控制\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W4\"\n      - round: 15\n        reviewers: []\n        note: \"App O composition control\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W4 再提 composition confound。R2 REBUT 引用 App O (Δ=1.08pp) + App P (base-only/instruct-only 独立验证)。充分排除。\"\n    action_items: []\n    resolution: \"Fully addressed. Appendix O composition control (Δ=1.08pp) + Appendix P base/instruct decomposition. R2 rebuttal convincing.\"\n    resolution_round: 16\n\n  - id: \"R14-W5\"\n    summary: \"\\\\enlargethispage 使用激进\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W5\"\n      - round: 15\n        reviewers: [2]\n        note: \"改善至 4\\\\baselineskip\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"视觉审查 critical：主文 ~8.3-8.5 页。合并入 R16-W5。\"\n    action_items: []\n    resolution: \"Worsened. Merged into R16-W5 (page overflow).\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W6\"\n      - round: 15\n        reviewers: [2]\n        note: \"仍有混用\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-M1 + R1 AGREE。合并入 R16-M1。\"\n    action_items: []\n    resolution: \"Merged into R16-M1.\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-N3\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Merged into R16-N2\"\n    action_items: []\n    resolution: \"Superseded by R16-N2\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"Conclusion 仅 4 句话\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W8\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。Conclusion 现为 5 句（§6, page 8），简洁但完整。\"\n    action_items: []\n    resolution: \"Not re-raised in R15 or R16. Conclusion now 5 sentences covering key findings.\"\n    resolution_round: 16\n\n  - id: \"R14-N1\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N1\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W3 重新提出。合并入 R16-W4。\"\n    action_items: []\n    resolution: \"Re-raised in R16. Merged into R16-W4.\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"'两个维度'框架正交性可能是概念上预期的结果\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-I1\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Merged into R16-N2\"\n    action_items: []\n    resolution: \"Superseded by R16-N2\"\n    resolution_round: null\n\n  # === Round 13 issues ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W1\"\n      - round: 15\n        reviewers: []\n        note: \"mechanism-agnostic 定位已建立\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。论文全文统一 mechanism-agnostic 定位 + 4 exclusion arguments (App B)。§5.2 的 mechanism-conditional 建议是残余问题（R16-W2）。\"\n    action_items: []\n    resolution: \"Core concern addressed by mechanism-agnostic positioning. Residual mechanism inference issue in §5.2 tracked as R16-W2.\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定条件\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2\"\n      - round: 14\n        reviewers: []\n        note: \"已有 k≤5 限定\"\n    action_items: []\n    resolution: \"Contribution 2 已写为 'ΔFPR = 0 under single-subject contamination, k ≤ 5'。R14/R15/R16 未再提出。\"\n    resolution_round: 14\n\n  # === Historical resolved issues ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Size-stratified DEFF table added.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法未定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Formal definition in app:dedup_k.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Reframed as 'Orthogonal constructs'.\"\n    resolution_round: 19\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Difficulty-dependent injection results written to paper.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as exploratory. R15 re-raised as R15-W4.\"\n    resolution_round: 20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 16 issues ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准——核心定量声称的基础\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-W1: warning 级别，threshold sensitivity + random baseline 部分缓解\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix (N1)。R2 交叉回应 AGREE 并叠加：'论文声称 methodological adaptations for LLM 但最关键的 adaptation（阈值校准）恰好缺失'。论文已加 sensitivity analysis (18.3% at ≥2.0, 10.2% at ≥2.5) 和 'standardized reference points' 措辞，但未做 LLM-specific calibration（如 random-split null 分布的 percentile、rank displacement per threshold）。共识 Must-Fix。\"\n    action_items:\n      - round: 16\n        action: \"提供 LLM-specific 实证锚定：(1) random-split |Δ_MH| 分布的 95th percentile 作为 empirical null; (2) rank displacement 随阈值变化的分析; (3) 明确承认 ETS 分类在 LLM 中是 effect-size 驱动的标准化参考点而非经过领域校准的阈值\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 1（global-vs-differential 正交性）和 Contribution 3（three methodological adaptations）的贡献声称均存在过度定位\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W6: 方法论新颖性有限\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7/N2: innovations→adaptations; 正交性可能是概念预期\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N3/I1: framework→adaptations 改善但 Related Work 自矛盾；正交性降级为 info\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2 升级 C1 为 Must-Fix (N1)：'确认显而易见的事实'。R1 REBUT C1：contamination 文献隐含假设 exposure→DIF，实证否证有价值，但同意不应是 #1 贡献。R2 升级 C3 为 Must-Fix (N2)：DEFF 借用、semi-synthetic 是验证策略。R1 强力辩护 cross-subject matching（formal ΔFPR=0 guarantee，非 implementation decision），同意 DEFF/semi-synthetic 定位偏高。【分歧】：cross-subject matching 的新颖性——R1 认为是 formal contribution，R2 认为是 engineering choice。\"\n    action_items:\n      - round: 16\n        action: \"重构三项贡献：(1) C1 降级为 motivating empirical observation 或合并入 C2; (2) C3 突出 cross-subject matching 的 formal guarantee 为主要方法学贡献，DEFF/semi-synthetic 降为 supporting choices; (3) 消除 Related Work 中任何自矛盾措辞\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 校正两种估计量差异 2× 削弱 headline 定量精度\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次提出\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N1 升级为 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2 AGREE。论文已加 simulation (App I) + size-stratified DEFF (Table 8) + cluster bootstrap 26.7% 作为第三参考点。改善明显但仍缺推荐估计量。R2 指出 cluster bootstrap 与 simple-mean 接近暗示 weighted-mean 过保守，但论文未明确推荐。降级为 Should-Fix（已有证据链，缺明确推荐）。\"\n    action_items:\n      - round: 16\n        action: \"在 §4.2 或 Discussion 中明确推荐 simple-mean DEFF 作为 primary estimate（基于 simulation evidence + cluster bootstrap convergence），将 weighted-mean 定位为 conservative bound\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W2\"\n    summary: \"§5.2 审计协议从 mechanism-agnostic 的 DIF 推断因果机制，措辞超出方法能力\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-W7: 增加决策启发式\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1 AGREE。论文加了 3 条 heuristic 但 'suggests capability shift' 仍是正面因果声称。R1 建议改为排除性推理：'inconsistent with contamination as sole mechanism'。共识 Should-Fix。\"\n    action_items:\n      - round: 16\n        action: \"§5.2 将 'suggests capability shift' 改为排除性推理措辞（如 'inconsistent with contamination as sole mechanism'）; 加 caveat 'DIF alone cannot determine causation'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W3\"\n    summary: \"Discussion (§5) 缺乏深层 insight，§5.1 本质是附加实验结果\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W2 新提出。R1 部分同意但指出 8 页限制制约 + §5.1 base/instruct 分层是 structured signal 证据而非简单重述。R1 认为 audit paper 合理聚焦操作建议而非未经数据支撑的因果推测。分歧程度低。\"\n    action_items:\n      - round: 16\n        action: \"在 §5 增加 1-2 段讨论 temporal DIF 对 LLM 评测生态的系统性影响（排行榜解读、benchmark 维护策略），超越结果重述\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高（15+ 数值堆砌），影响可读性\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N1: info 级别\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W3 重新提出为 Should-Fix + R1 AGREE。论文 abstract 仍含 15+ 数值。共识应精简。\"\n    action_items:\n      - round: 16\n        action: \"Abstract 保留核心数字（规模、DIF 率、分数位移），统计检验细节移至 Introduction\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W5\"\n    summary: \"主文超页：Conclusion 位于 page 9，\\\\enlargethispage 导致 page overflow\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W5: enlargethispage 使用激进\"\n      - round: 15\n        reviewers: [2]\n        note: \"改善至 4\\\\baselineskip\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-M2 标记格式风险。视觉审查 critical finding：Sections 1-6 约占 8.3-8.5 页，Conclusion 位于 page 9。EMNLP 2026 strict 8-page limit。\"\n    action_items:\n      - round: 16\n        action: \"压缩正文至 strict 8 页：移除 \\\\enlargethispage；压缩 §2 Related Work 或 §5 Discussion 约 0.3-0.5 页\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W6\"\n    summary: \"Semi-synthetic validation 的 uniform flipping 是 upper bound，ΔTPR 应标为检测力上界\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W3\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N2 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W3 + R2 AGREE。论文已加 difficulty-dependent injection (App G) + 'stylized/may overestimate' 措辞。改善明显。R2 认为不完全是 Must-Fix（框架目的是 sensitivity analysis 非 power estimation）。降级为 Should-Fix。残余问题：instruct 模型残差 gap 13×。\"\n    action_items:\n      - round: 16\n        action: \"正文中明确 ΔTPR 是 upper bound 而非 point estimate；考虑更具挑战性的 injection scheme（如 graded injection with noise）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致：temporal score incomparability vs measurement non-invariance\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W6\"\n      - round: 15\n        reviewers: [2]\n        note: \"仍有少量混用\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-M1 + R1 AGREE。需在 §1 明确 measurement non-invariance（机制）vs temporal score incomparability（后果）的对应关系。\"\n    action_items:\n      - round: 16\n        action: \"§1 首次出现时明确对应关系\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M2\"\n    summary: \"有效 N=1,887（temporal cohort）vs 总 N=5,227 需要在 §3.1 澄清\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [1]\n        note: \"R1-M4。§3.2 提到 'At N=5,227' 但 temporal comparison 实际使用 N_ref=1,080, N_focal=807。R2 AGREE。\"\n    action_items:\n      - round: 16\n        action: \"§3.1 明确区分全量模型数与 temporal cohort 有效 N\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M3\"\n    summary: \"遗漏近期 IRT-for-LLM 相关工作（4 篇）和 DIF 工具文献（2 篇）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2 建议 4 篇（Adaptive Testing arxiv 2511.04689, JE-IRT arxiv 2509.22888, Confident Rankings arxiv 2601.13885, Benchmarks Leak arxiv 2601.19334）。R1 建议 2 篇（ShinyItemAnalysis Martinková 2018, mirt Chalmers 2012）。R1 提醒需先验证 R2 建议的 arXiv ID 真实性。\"\n    action_items:\n      - round: 16\n        action: \"WebSearch 核实 6 篇引用真实性后择优加入 §2\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 15 issues with R16 status updates ===\n\n  - id: \"R15-N1\"\n    summary: \"DEFF 校正两种估计量差异 2 倍（simple-mean 29.2% vs weighted-mean 13.5%），选择理由仍不充分\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W2: 首次提出\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W2: 再次独立提出\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R1-N1 升级为 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"论文已加 simulation (App I) + stratified DEFF + cluster bootstrap 26.7%。改善明显。R16 降级为 Should-Fix (R16-W1)。残余：缺明确推荐哪个估计量。\"\n    action_items:\n      - round: 15\n        action: \"§4.2 并列呈现两种估计 + 解释 size-dependent ICC 导致 weighted-mean over-correct + 引用 App I simulation + 强调 13.5% 仍是 75× baseline\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Simulation + stratified DEFF + cluster bootstrap added. Downgraded to Should-Fix in R16 (R16-W1). Remaining: explicit recommendation needed.\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Semi-synthetic 验证 uniform binary flipping 可能是 easiest-to-detect 而非 worst-case\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W3\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W3\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N2 Must-Fix\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"论文加了 difficulty-dependent injection + 'stylized/may overestimate' 措辞。改善明显。R16 降级为 Should-Fix (R16-W6)。\"\n    action_items:\n      - round: 15\n        action: \"术语 worst-case→stylized; upper-bound→may overestimate; 加 difficulty-dependent injection\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Terminology fixed + difficulty-dependent injection added. Downgraded to Should-Fix in R16 (R16-W6).\"\n    resolution_round: null\n\n  - id: \"R15-N3\"\n    summary: \"框架贡献被过度声称（Contribution 3 vs Section 2 自述矛盾）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W6\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R15-N3\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"论文改 framework→adaptations，统一了两处。但 R2 仍认为 overclaimed（N2），R1 辩护 cross-subject matching 的 formal contribution。合并入 R16-N2。\"\n    action_items:\n      - round: 15\n        action: \"Contribution 3: framework→adaptations; related_work: 消除自矛盾\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Terminology unified. Merged into R16-N2 for further refinement.\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"ETS 效应量阈值从人类考生直接移植到 LLM 的合理性未论证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"threshold sensitivity + random baseline 部分缓解\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix。合并入 R16-N1。\"\n    action_items:\n      - round: 15\n        action: \"§3.2 加 ETS 阈值适切性讨论\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Escalated to Must-Fix in R16. Merged into R16-N1.\"\n    resolution_round: null\n\n  - id: \"R15-W2\"\n    summary: \"N=5,227 下 MH chi-squared p-value 近乎全显著，ETS C 的 p<0.05 条件失去区分力\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"已在 method.tex §3.2 处理\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W2 再提。R2 REBUT：effect size 是约束性条件，非循环逻辑。论文 §3.2 已有详细讨论（DEFF restores p-value selectivity）。分歧解决：R2 的 rebuttal 更有说服力。残余：应更明确承认 p-value 在大样本下退化。\"\n    action_items:\n      - round: 15\n        action: \"确认 §3.2 现有讨论充分\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Mostly addressed. §3.2 discusses DEFF restoring p-value selectivity. R2 rebuttal convincing. Minor wording improvement needed.\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"Within-family DIF（Llama-2 vs 3, C%=59.2%）与架构/能力代际差异混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"App N 逻辑可能相反\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。论文 §5.1 + App N 已重新框架化：raw 59.2% → ability-matched ~28-29%。\"\n    action_items:\n      - round: 15\n        action: \"App N + §5.1 重新框架化\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Likely addressed. R16 did not re-raise. Paper now shows ability-matched convergence.\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"GSM1K 相关性正文用 'confirms' 语气但应保持 exploratory 定位\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"Figure 5 caption 标 exploratory 但正文 confirming 语气\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。论文 §4.7 现用 'exploratory cross-benchmark signal' + 'small sample requires replication'。\"\n    action_items:\n      - round: 15\n        action: \"正文 confirms→suggests\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Likely addressed. R16 did not re-raise. Current language uses 'exploratory' and 'requires replication'.\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"Local independence 违反（Yen's Q3）的定量影响未与 DIF detection rate 关联\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1]\n        note: \"DEFF 处理 model-level，Q3 是 item-level\"\n      - round: 16\n        reviewers: [1]\n        note: \"R1-M1 简要提及。论文已加 permutation simulation <0.001pp (§3.2 LLM-specific challenges)。R2 AGREE 值得关注但 cross-subject matching 部分缓解。\"\n    action_items:\n      - round: 15\n        action: \"引用 plan_035 结果\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Permutation simulation result now in paper. Minor residual concern.\"\n    resolution_round: null\n\n  - id: \"R15-W6\"\n    summary: \"遗漏 concurrent work：CoDeC（ICLR 2026）\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"CoDeC in-context learning 污染检测\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。论文 §2 now includes Zawalski et al. (2026) CoDeC。\"\n    action_items: []\n    resolution: \"CoDeC now cited in §2 Related Work (Zawalski et al., 2026). R16 did not re-raise.\"\n    resolution_round: 16\n\n  - id: \"R15-W7\"\n    summary: \"可操作性缺口：DIF 是 mechanism-agnostic 但推荐 mechanism-conditional responses\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"增加决策启发式\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W1 + R1 AGREE。论文加了 heuristics 但 'suggests capability shift' 措辞仍超出方法能力。合并入 R16-W2。\"\n    action_items:\n      - round: 15\n        action: \"§5.2 加决策启发式\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed. Heuristics added but mechanism inference language persists. Merged into R16-W2.\"\n    resolution_round: null\n\n  - id: \"R15-I1\"\n    summary: \"'两维度正交'作为 Contribution 1 的新颖性存疑\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"R2 Must-Fix vs R1 REBUT 降级为 info\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2 再次升级为 Must-Fix (N1)。R1 REBUT：contamination 文献隐含假设 exposure→DIF，实证否证有价值。但同意不应是 #1 贡献。分歧存在但方向一致（需重新定位）。合并入 R16-N2。\"\n    action_items:\n      - round: 15\n        action: \"Contribution 1 调整为 empirical quantification\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"Partially addressed by reframing. Merged into R16-N2 for further restructuring.\"\n    resolution_round: null\n\n  - id: \"R15-I2\"\n    summary: \"视觉节奏不均：连续多页无 figure/table\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"视觉审查\"\n      - round: 16\n        reviewers: []\n        note: \"R16 视觉审查确认 pages 3-5 连续 3 页无 figure/table。建议 Method section 加框架概览图。\"\n    action_items:\n      - round: 16\n        action: \"如空间允许，在 §3 加 DIF audit pipeline 概览图\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-NEW1\"\n    summary: \"Discussion 加 Contrasts with Educational DIF 段\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [1, 2]\n        note: \"列出 LLM DIF 与教育 DIF 的质的差异\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。论文 §5.1 现含 3 个 LLM-education 对比。\"\n    action_items: []\n    resolution: \"Addressed. §5.1 now includes three contrasts with educational DIF settings.\"\n    resolution_round: 16\n\n  - id: \"R15-Q1\"\n    summary: \"Base-only 和 instruct-only 分别做 temporal DIF 的 C%\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [2]\n        note: \"分离 temporal 和 training methodology 贡献\"\n      - round: 16\n        reviewers: []\n        note: \"论文 Appendix O (Table 15) 现有完整结果：base-only C%=32.1%, instruct-only C%=36.5%。R16 R2 在交叉回应中引用此数据反驳 R1-W4。\"\n    action_items: []\n    resolution: \"Fully addressed. Appendix O Table 15 provides base-only and instruct-only temporal DIF results.\"\n    resolution_round: 16\n\n  # === Round 14 issues（R16 状态更新） ===\n\n  - id: \"R14-W1\"\n    summary: \"Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W1\"\n      - round: 15\n        reviewers: []\n        note: \"已引入 temporal score incomparability + mechanism-agnostic\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。标题和全文统一使用 'temporal score incomparability'，mechanism-agnostic 定位贯穿。\"\n    action_items: []\n    resolution: \"Addressed. Terminology changed to 'temporal score incomparability' throughout. Mechanism-agnostic positioning established. Not raised in R15 or R16.\"\n    resolution_round: 16\n\n  - id: \"R14-W4\"\n    summary: \"缺少 base/instruct composition shift 的直接控制\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W4\"\n      - round: 15\n        reviewers: []\n        note: \"App O composition control\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R1-W4 再提 composition confound。R2 REBUT 引用 App O (Δ=1.08pp) + App P (base-only/instruct-only 独立验证)。充分排除。\"\n    action_items: []\n    resolution: \"Fully addressed. Appendix O composition control (Δ=1.08pp) + Appendix P base/instruct decomposition. R2 rebuttal convincing.\"\n    resolution_round: 16\n\n  - id: \"R14-W5\"\n    summary: \"\\\\enlargethispage 使用激进\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W5\"\n      - round: 15\n        reviewers: [2]\n        note: \"改善至 4\\\\baselineskip\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"视觉审查 critical：主文 ~8.3-8.5 页。合并入 R16-W5。\"\n    action_items: []\n    resolution: \"Worsened. Merged into R16-W5 (page overflow).\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W6\"\n      - round: 15\n        reviewers: [2]\n        note: \"仍有混用\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-M1 + R1 AGREE。合并入 R16-M1。\"\n    action_items: []\n    resolution: \"Merged into R16-M1.\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"方法论新颖性有限\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W7\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-N3\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Merged into R16-N2\"\n    action_items: []\n    resolution: \"Superseded by R16-N2\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"Conclusion 仅 4 句话\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-W8\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未提出。Conclusion 现为 5 句（§6, page 8），简洁但完整。\"\n    action_items: []\n    resolution: \"Not re-raised in R15 or R16. Conclusion now 5 sentences covering key findings.\"\n    resolution_round: 16\n\n  - id: \"R14-N1\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N1\"\n      - round: 15\n        reviewers: []\n        note: \"R15 未提出\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"R2-W3 重新提出。合并入 R16-W4。\"\n    action_items: []\n    resolution: \"Re-raised in R16. Merged into R16-W4.\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"'两个维度'框架正交性可能是概念上预期的结果\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14-N2\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Merged into R15-I1\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"Merged into R16-N2\"\n    action_items: []\n    resolution: \"Superseded by R16-N2\"\n    resolution_round: null\n\n  # === Round 13 issues ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-W1\"\n      - round: 15\n        reviewers: []\n        note: \"mechanism-agnostic 定位已建立\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。论文全文统一 mechanism-agnostic 定位 + 4 exclusion arguments (App B)。§5.2 的 mechanism-conditional 建议是残余问题（R16-W2）。\"\n    action_items: []\n    resolution: \"Core concern addressed by mechanism-agnostic positioning. Residual mechanism inference issue in §5.2 tracked as R16-W2.\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定条件\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2\"\n      - round: 14\n        reviewers: []\n        note: \"已有 k≤5 限定\"\n    action_items: []\n    resolution: \"Contribution 2 已写为 'ΔFPR = 0 under single-subject contamination, k ≤ 5'。R14/R15/R16 未再提出。\"\n    resolution_round: 14\n\n  # === Historical resolved issues ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Size-stratified DEFF table added.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法未定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Formal definition in app:dedup_k.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    resolution: \"Reframed as 'Orthogonal constructs'.\"\n    resolution_round: 19\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    resolution: \"Difficulty-dependent injection results written to paper.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as exploratory. R15 re-raised as R15-W4.\"\n    resolution_round: 20"
  }
}
```

</details>

---


### Tool result

_source line 1530 · 2026-05-23T10:38:37.642122+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 26988}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1531 · 2026-05-23T10:41:35.646737+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 16 审稿报告\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (via ARR, Long Paper)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer**: R1（方法严谨性+统计有效性）、R2（新颖性/贡献+完整性+写作）\n**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items）进行大规模时间性测量不变性审计。核心发现：2023-2024 模型队列间 17.9–31.3% 的 items 展现 temporal DIF（DEFF 校正后 ~27–29%，保守下界 13.5%）；DIF flags 与 web-overlap contamination labels 近似独立（Jaccard ≈ 0.206）；DIF-corrected scoring 平均偏移 +2.12pp。论文提出三项 LLM-specific 适配：cross-subject matching（ΔFPR=0 guarantee）、DEFF 校正和 semi-synthetic 验证框架，在 6 个 METABENCH benchmarks 上复制。\n\n---\n\n## Strengths\n\n**S1. 空前的实证规模与系统性控制。** 5,227 模型 × 12,508 items，五种 cohort 设计（temporal, ability-quintile, within-family, within-subject, random split）提供三角验证。Random split 基线 C% = 0.18% 确认方法在零假设下几乎无 false positive。[R1, R2 共识]\n\n**S2. Cross-subject matching 是实质性方法学贡献。** 单域 contamination 下 ΔFPR = 0 的 formal guarantee（Section 3.4），从构造上阻断 contamination 信号泄漏到 matching variable。Table 7 实证验证：ΔFPR = 0.000 vs within-subject matching 膨胀 +0.186。解决了将 DIF 应用于可能被 contaminate 的 benchmarks 时一个此前未被形式化的方法学难题。[R1 强调；R2 承认技术贡献但认为定位可调]\n\n**S3. 重要且及时的研究问题。** Benchmark 分数跨时间可比性是 LLM 社区追踪模型进步的基础假设，本文以定量方式首次系统性检验该假设。~27–29% 的 items 存在 temporal DIF，DIF 校正后排名位移达 ±800+，对排行榜维护者有直接可操作价值。[R1, R2 共识]\n\n**S4. 对估计量不确定性的透明度。** 诚实报告 simple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）的 2.2× 差距，Appendix I simulation 提供有原则的比较，cluster bootstrap（26.7%）作为第三参考点。[R1 特别肯定]\n\n**S5. 跨 benchmark 复制。** 6 个 METABENCH benchmarks 均展现显著 temporal DIF（C% 17.9–31.3%，45–174× 随机基线），增强泛化性。知识/推理类 benchmark C% 高于程序类。[R1, R2 共识]\n\n**S6. 附录深度出色。** Sections A-P 提供完整技术链条：诊断（Q3, domain-specificity）、机制分析、结构控制细节、DEFF 估计、去重灵敏度、跨架构验证等。[R1, R2 共识]\n\n---\n\n## Weaknesses — Must-Fix（影响接收决定）\n\n**N1 [critical, 共识] ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准**\n\n论文直接采用 ETS Category C 阈值（odds ratio ≈ 2.7:1），引用其在教育测试中的标准地位。但 LLM 不是人类考生——模型间的能力分布、响应机制、群体异质性根本不同。教育测试 DIF 率通常 5–15%，本文 17.9–31.3%（高 2–6×），差异可能反映阈值在 LLM 域内过于宽松。\n\n论文提供了阈值灵敏度分析（18.3% at ≥2.0, 10.2% at ≥2.5; Section 4.2），展示了定性稳健性。但这只回答了\"换阈值结果如何变化\"，没有回答\"对 LLM 来说 |Δ_MH| = 1.5 构成什么级别的实质性差异\"。论文声称做了 \"three methodological adaptations for LLM evaluation\"，但最关键的 adaptation——阈值校准——恰好缺失。\n\n**所需修改**: (1) 提供 LLM-specific 实证锚定（如 random-split |Δ_MH| 分布的 95th percentile 作为 empirical null）；(2) 展示不同阈值下 rank displacement 的差异；(3) 明确承认 ETS 分类在当前 N 下本质是 effect-size 驱动的标准化参考点。\n\n**N2 [critical, 分歧存在] 贡献声称定位偏高——Contribution 1 和 Contribution 3 均存在过度声称**\n\n- **Contribution 1**（\"Two dimensions of benchmark behavior\"）: R2 认为 global exposure 与 differential functioning 定义上就是不同构念，低 Jaccard 是结构性预期而非新发现。R1 反驳：contamination 文献隐含假设 exposure→DIF（MinK++, Time Travel 等方法基于此），实证否证有价值。**两位 Reviewer 均同意**不应作为 #1 贡献，建议重新定位为 motivating empirical observation。\n\n- **Contribution 3**（\"Three methodological adaptations\"）: R2 认为 (a) cross-subject matching 是实施决策，(b) DEFF 借用 survey methodology，(c) semi-synthetic 是验证策略——不构成方法论贡献。**R1 强烈反驳 (a)**：cross-subject matching 有 formal ΔFPR=0 guarantee，解决了此前未被形式化的 matching variable corruption 问题，非标准实施选择。R1 同意 (b)(c) 定位偏高。\n\n**所需修改**: (1) C1 降级为 motivating observation 或合并入 C2；(2) C3 突出 cross-subject matching 的 formal guarantee 为主要方法学贡献，DEFF/semi-synthetic 降为 supporting choices；(3) 消除 Related Work 中任何自矛盾措辞。\n\n---\n\n## Weaknesses — Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] DEFF 校正的 2× 不确定性削弱 headline 定量精度**\n\nSimple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）差距 2.2×。论文通过 Appendix I simulation 和 cluster bootstrap（26.7%）提供了有力证据链，但未明确推荐使用哪个估计量。Cluster bootstrap 与 simple-mean 接近，暗示 weighted-mean 过保守。读者面对宽范围不知如何解读。\n\n*进展*: 相比 R15，论文已加 simulation + stratified DEFF + cluster bootstrap，改善明显。从 R15 的 Must-Fix 降级。\n\n**所需修改**: 明确推荐 simple-mean DEFF 作为 primary estimate，weighted-mean 定位为 conservative bound，附理由。\n\n**W2 [warning, 共识] §5.2 审计协议从 mechanism-agnostic 的 DIF 推断因果机制**\n\n\"DIF on web-clean items suggests capability shift\" 超出了 DIF 方法的能力边界。DIF 检测 *that* items function differently，但不能告诉 *why*。在审计协议这种规范性建议中，正面因果声称可能被误读。\n\n**所需修改**: 改为排除性推理（\"inconsistent with contamination as sole mechanism\"），加 caveat \"DIF alone cannot determine causation\"。\n\n**W3 [warning, 共识] Discussion (§5) 缺乏深层 insight**\n\n§5.1 本质是附加实验结果（base/instruct 分层），§5.2 提供操作建议但缺乏对 temporal DIF 成因假说和对 LLM 评测生态系统性影响的讨论。R1 指出 8 页限制的合理约束，且 §5.1 的 base/instruct 方向差异提供了 structured signal 证据，超越简单重述。\n\n**所需修改**: 增加 1-2 段对 temporal DIF 系统性影响的讨论（排行榜解读、benchmark 生命周期管理）。\n\n**W4 [warning, 共识] Abstract 信息密度过高**\n\n单段 Abstract 含 15+ 数值（5,227 models, 27,125 items, 17.9–31.3%, Jaccard = 0.206, χ² = 562.7, ±2.12pp 等），影响不熟悉 DIF 术语的 NLP 读者的可读性。\n\n**所需修改**: 保留核心数字（规模、DIF 率、分数位移），统计检验细节移至 Introduction。\n\n**W5 [warning, 视觉审查] 主文超页——Conclusion 位于 page 9**\n\n视觉审查发现 Sections 1-6 约占 8.3–8.5 页，Conclusion 位于 page 9 右栏。`\\enlargethispage*{4\\baselineskip}` 扩展了 Discussion 页面但仍超出 EMNLP 2026 strict 8-page limit。\n\n**所需修改**: 压缩正文至 strict 8 页：移除 `\\enlargethispage`，压缩 §2 或 §5 约 0.3–0.5 页。\n\n**W6 [warning, 共识] Semi-synthetic ΔTPR 应标为检测力上界而非 point estimate**\n\nUniform binary flipping 是检测的 best-case scenario。论文已加 difficulty-dependent injection（ΔTPR ≈ 0.41 vs 0.51 uniform, ~20% reduction）和 \"stylized/may overestimate\" 措辞，改善明显。残余问题：instruct 模型残差 gap 13×（无法复制 near-zero direction reversal）。\n\n*进展*: 相比 R15 的 Must-Fix，显著改善，降级。\n\n**所需修改**: 正文明确 ΔTPR 是 upper bound 而非 point estimate。\n\n---\n\n## Reviewer Consensus（交叉分享后共识）\n\n1. **[AGREE]** ETS 阈值缺乏 LLM-specific 校准是论文最大方法论盲点（N1）\n2. **[AGREE]** DEFF 2× 不确定性影响定量精度但证据链已改善（W1）\n3. **[AGREE]** Semi-synthetic injection 是 upper bound，不是 power estimation（W6）\n4. **[AGREE]** §5.2 mechanism inference 超出方法能力（W2）\n5. **[AGREE]** Abstract 信息密度过高（W4）\n6. **[AGREE]** 定性结论稳健：temporal DIF 以非平凡比例存在（~27–29%），远超随机基线\n7. **[AGREE]** Cross-subject matching 提供了实质性的 LLM-specific 方法学贡献\n8. **[AGREE]** 论文的经验工作（规模 + 控制）处于高水平\n\n## Reviewer Divergence（交叉分享后分歧）\n\n1. **Contribution 1 的贡献深度**: R2 认为 global-vs-differential 独立性是定义上预期的结果；R1 认为 contamination 文献的隐含假设使实证否证有价值。**双方均同意应降低其贡献层级**。\n\n2. **Cross-subject matching 的新颖性定位**: R2 认为是 \"engineering choice\"；R1 认为是 \"formal contribution with ΔFPR=0 guarantee\"（含 Section 3.4 的严格推导 + Table 7 的实证验证）。**R1 的论证更有力**——该保证是 formal result 且此前在 LLM 评测中未被形式化。\n\n3. **Multiple testing 循环论证**: R1 认为 BH-FDR 在大 N 下的无效性构成循环逻辑；R2 反驳 ETS C 分类的约束性条件是 effect size 而非 p-value，大样本下转向 effect-size 驱动是系统设计的一部分。**R2 的论证更有说服力**——论文已在 §3.2 讨论了 DEFF 如何恢复 p-value 选择性。\n\n4. **Composition confound**: R1 认为 11.8pp composition gap 仍可能膨胀聚合 C%；R2 引用 Appendix O base-only (32.1%) / instruct-only (36.5%) 分析，认为已充分排除。**R2 的数据反驳有力**——两个纯子群独立展现高 DIF 率，composition 影响方向而非检出率。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** |Δ_MH| = 1.5 在 LLM 排名中的实际影响？不同阈值（1.0, 1.5, 2.0, 2.5）下的 average rank displacement 分别是多少？\n\n**Q2.** Random-split 下 |Δ_MH| 分布的 95th percentile 是多少？可否作为 LLM-specific empirical null 与 ETS 1.5 比较？\n\n**Q3.** DEFF simulation 中如果 ICC 与 family size 不呈负相关，simple-mean 估计量是否仍然优于 weighted-mean？\n\n**Q4.** Difficulty × model-type interaction 能解释多大比例的 observed temporal DIF？是否存在 difficulty-dependent capability improvements（无 contamination）即可产生类似幅度 DIF 的可能性？\n\n**Q5.** 不同学科的 DIF enrichment ratio 差异（如 Humanities vs STEM）的驱动因素——差异化污染率还是题目结构特性？\n\n**Q6.** DIF-flagged items 是否应被排除出 Growing Pains (Habba et al., 2026) 的 anchor sets？两个框架的互补关系可否更明确地讨论？\n\n---\n\n## Missing References\n\n**R2 建议（需验证 arXiv ID 真实性）:**\n1. Adaptive Testing for LLM Evaluation (arxiv 2511.04689) — IRT Fisher information 自适应评测\n2. JE-IRT: Joint Embedding IRT (arxiv 2509.22888) — geometric lens on LLM abilities\n3. Confident Rankings with Fewer Items (arxiv 2601.13885) — 连续分数自适应测试\n4. When Benchmarks Leak: Inference-Time Decontamination (arxiv 2601.19334)\n\n**R1 建议:**\n5. Martinková & Drabinová (2018) ShinyItemAnalysis — DIF 分析替代工具\n6. Chalmers (2012) mirt — 主要 MIRT 软件文献\n\n---\n\n## External Review\n\n外部审稿：未配置（`external_review.paperreview_ai.enabled` 未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4.5 分钟）。\n\n| Severity | Finding |\n|----------|---------|\n| **critical** | 主文超页：Sections 1-6 约占 8.3-8.5 页，Conclusion 位于 page 9。违反 EMNLP 2026 strict 8-page limit。 |\n| **warning** | Pages 3-5 连续 3 页无 figure/table（Related Work + Method 纯文本），§3 缺少 DIF audit pipeline 概览图。 |\n| **warning** | 首页无视觉锚点（Title + Abstract + Intro 全文本），Figure 1 在 page 2。 |\n| info | 附录 Figures 3-6 axis label 约 6-7pt，接近可读性下限。 |\n| info | Figure 1 红/蓝配色有冗余线型编码，色盲安全可接受但非最优。 |\n| info | Table 3 信息密度高但可读，最优值加粗。 |\n| info | 引用格式统一，无未解析引用，无 margin 溢出。 |\n| info | 全文无公式渲染错误、无 section heading 孤悬页底，表格统一 booktabs 风格。 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 (Borderline Conference)**\n\n**R1**: 3.5 (Borderline Conference), Confidence 4/5\n**R2**: 3.5 (Borderline Conference), Confidence 4/5\n\n**综合判断**: 论文在一个重要且及时的问题上做了大规模、严谨的经验工作。Cross-subject matching 提供了实质性的方法学贡献（formal ΔFPR=0 guarantee）。核心定性结论稳健：temporal DIF 以 ~27–29% 的非平凡比例存在，远超随机基线 170×+，且不受 family structure、ability mismatch 或 composition shift 的混淆。\n\n主要不足集中在两个层面：\n\n1. **方法论校准缺口**（N1）：ETS 阈值未经 LLM 领域特定校准——这是论文声称做了 \"methodological adaptations for LLM evaluation\" 但实际遗漏的最关键适配。DEFF 2× 不确定性进一步影响定量精度。\n\n2. **贡献叙事偏高**（N2）：Contribution 1（正交性）和 Contribution 3 中的 DEFF/semi-synthetic 部分存在过度声称。Cross-subject matching 的新颖性被 Reviewer 间的分歧暴露——需要更清晰的 positioning 来让其方法学价值被充分认可。\n\n如果作者能：(1) 提供 LLM-specific 阈值锚定（random-split empirical null + rank displacement per threshold），(2) 重构贡献层级（突出 cross-subject matching 的 formal guarantee，降低 C1 和 C3 其余部分），(3) 解决页数超限和 Abstract 可读性问题——论文有潜力上升到 Conference 水平（4.0）。当前状态位于 Borderline Conference 与 Findings 之间的上端。\n\n**使用 EMNLP 2026 ARR 评分标准**: 3.5 = Borderline Conference\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 三个 contributions 的排序和权重需要重构。当前 C1 占据首位但贡献深度最浅。建议：C2（temporal DIF at scale）→ C1（cross-subject matching formal guarantee）→ C3（empirical independence of global/differential signals as motivating observation）。\n- \"to our knowledge the largest-scale DIF analysis on LLM benchmarks\" 声称合理但应注明 scale 的具体维度（models × items × benchmarks）。\n\n### Section 2 (Related Work)\n- \"We do not modify the core MH statistic\" 这句在交叉回应中被 R1 标记为不应删除（它是诚实的），但也不应与 \"three methodological adaptations\" 构成矛盾。建议重写为：\"We retain the standard MH statistic and develop three LLM-specific adaptations around it\"。\n- 6 篇遗漏引用需核实后择优补充（见 Missing References）。\n\n### Section 3 (Method)\n- §3.2: 应明确承认 ETS 阈值在当前 N 下本质是 effect-size 准则（p-value 近乎退化），并讨论该 effect size 在 LLM 评估中的实质意义。\n- §3.2: \"At N = 5,227\" 应改为实际 temporal cohort 的有效 N（1,887）。5,227 是全部模型数。\n- §3.4: Cross-subject matching 的 ΔFPR=0 guarantee 是论文最强的方法学贡献，应在 Introduction 中给予更突出的位置。\n\n### Section 4 (Experiments)\n- §4.2: DEFF 讨论已大幅改善，但应明确推荐 simple-mean 为 primary estimate。\n- §4.7: GSM8K 复制描述过于简略（仅 1 段），应至少报告 items/models 数量和与 MMLU 的模式异同。\n\n### Section 5 (Discussion)\n- §5.1: Base/instruct 方向差异（χ² = 562.7）是有价值的 structured signal，但应更明确讨论其对 LLM 评测实践的 implications。\n- §5.2: \"suggests capability shift\" → \"inconsistent with contamination as sole mechanism\"。\n- `\\enlargethispage*{4\\baselineskip}` 应移除。\n\n### Section 6 (Conclusion)\n- 当前 5 句简洁有效，但因页数超限可能需要进一步压缩或将部分内容移入 Discussion。\n\n### Limitations\n- 应补充：(1) 模型发布日期与训练数据截止时间不一定对齐；(2) 对 MMLU 式 MCQ 以外题型的泛化性仍需更多验证（虽有 GSM8K 但仅 1 段描述）。\n\n### Appendix\n- 深度出色，但 Figures 3-6 的 axis label 应增大至 ≥8pt。\n- Appendix I (DEFF Simulation) 的 4 种场景可考虑增加 1-2 种额外场景以增强说服力。",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 16 审稿报告\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (via ARR, Long Paper)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer**: R1（方法严谨性+统计有效性）、R2（新颖性/贡献+完整性+写作）\n**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items）进行大规模时间性测量不变性审计。核心发现：2023-2024 模型队列间 17.9–31.3% 的 items 展现 temporal DIF（DEFF 校正后 ~27–29%，保守下界 13.5%）；DIF flags 与 web-overlap contamination labels 近似独立（Jaccard ≈ 0.206）；DIF-corrected scoring 平均偏移 +2.12pp。论文提出三项 LLM-specific 适配：cross-subject matching（ΔFPR=0 guarantee）、DEFF 校正和 semi-synthetic 验证框架，在 6 个 METABENCH benchmarks 上复制。\n\n---\n\n## Strengths\n\n**S1. 空前的实证规模与系统性控制。** 5,227 模型 × 12,508 items，五种 cohort 设计（temporal, ability-quintile, within-family, within-subject, random split）提供三角验证。Random split 基线 C% = 0.18% 确认方法在零假设下几乎无 false positive。[R1, R2 共识]\n\n**S2. Cross-subject matching 是实质性方法学贡献。** 单域 contamination 下 ΔFPR = 0 的 formal guarantee（Section 3.4），从构造上阻断 contamination 信号泄漏到 matching variable。Table 7 实证验证：ΔFPR = 0.000 vs within-subject matching 膨胀 +0.186。解决了将 DIF 应用于可能被 contaminate 的 benchmarks 时一个此前未被形式化的方法学难题。[R1 强调；R2 承认技术贡献但认为定位可调]\n\n**S3. 重要且及时的研究问题。** Benchmark 分数跨时间可比性是 LLM 社区追踪模型进步的基础假设，本文以定量方式首次系统性检验该假设。~27–29% 的 items 存在 temporal DIF，DIF 校正后排名位移达 ±800+，对排行榜维护者有直接可操作价值。[R1, R2 共识]\n\n**S4. 对估计量不确定性的透明度。** 诚实报告 simple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）的 2.2× 差距，Appendix I simulation 提供有原则的比较，cluster bootstrap（26.7%）作为第三参考点。[R1 特别肯定]\n\n**S5. 跨 benchmark 复制。** 6 个 METABENCH benchmarks 均展现显著 temporal DIF（C% 17.9–31.3%，45–174× 随机基线），增强泛化性。知识/推理类 benchmark C% 高于程序类。[R1, R2 共识]\n\n**S6. 附录深度出色。** Sections A-P 提供完整技术链条：诊断（Q3, domain-specificity）、机制分析、结构控制细节、DEFF 估计、去重灵敏度、跨架构验证等。[R1, R2 共识]\n\n---\n\n## Weaknesses — Must-Fix（影响接收决定）\n\n**N1 [critical, 共识] ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准**\n\n论文直接采用 ETS Category C 阈值（odds ratio ≈ 2.7:1），引用其在教育测试中的标准地位。但 LLM 不是人类考生——模型间的能力分布、响应机制、群体异质性根本不同。教育测试 DIF 率通常 5–15%，本文 17.9–31.3%（高 2–6×），差异可能反映阈值在 LLM 域内过于宽松。\n\n论文提供了阈值灵敏度分析（18.3% at ≥2.0, 10.2% at ≥2.5; Section 4.2），展示了定性稳健性。但这只回答了\"换阈值结果如何变化\"，没有回答\"对 LLM 来说 |Δ_MH| = 1.5 构成什么级别的实质性差异\"。论文声称做了 \"three methodological adaptations for LLM evaluation\"，但最关键的 adaptation——阈值校准——恰好缺失。\n\n**所需修改**: (1) 提供 LLM-specific 实证锚定（如 random-split |Δ_MH| 分布的 95th percentile 作为 empirical null）；(2) 展示不同阈值下 rank displacement 的差异；(3) 明确承认 ETS 分类在当前 N 下本质是 effect-size 驱动的标准化参考点。\n\n**N2 [critical, 分歧存在] 贡献声称定位偏高——Contribution 1 和 Contribution 3 均存在过度声称**\n\n- **Contribution 1**（\"Two dimensions of benchmark behavior\"）: R2 认为 global exposure 与 differential functioning 定义上就是不同构念，低 Jaccard 是结构性预期而非新发现。R1 反驳：contamination 文献隐含假设 exposure→DIF（MinK++, Time Travel 等方法基于此），实证否证有价值。**两位 Reviewer 均同意**不应作为 #1 贡献，建议重新定位为 motivating empirical observation。\n\n- **Contribution 3**（\"Three methodological adaptations\"）: R2 认为 (a) cross-subject matching 是实施决策，(b) DEFF 借用 survey methodology，(c) semi-synthetic 是验证策略——不构成方法论贡献。**R1 强烈反驳 (a)**：cross-subject matching 有 formal ΔFPR=0 guarantee，解决了此前未被形式化的 matching variable corruption 问题，非标准实施选择。R1 同意 (b)(c) 定位偏高。\n\n**所需修改**: (1) C1 降级为 motivating observation 或合并入 C2；(2) C3 突出 cross-subject matching 的 formal guarantee 为主要方法学贡献，DEFF/semi-synthetic 降为 supporting choices；(3) 消除 Related Work 中任何自矛盾措辞。\n\n---\n\n## Weaknesses — Should-Fix（影响评分但不一票否决）\n\n**W1 [warning, 共识] DEFF 校正的 2× 不确定性削弱 headline 定量精度**\n\nSimple-mean DEFF（29.2%）与 weighted-mean DEFF（13.5%）差距 2.2×。论文通过 Appendix I simulation 和 cluster bootstrap（26.7%）提供了有力证据链，但未明确推荐使用哪个估计量。Cluster bootstrap 与 simple-mean 接近，暗示 weighted-mean 过保守。读者面对宽范围不知如何解读。\n\n*进展*: 相比 R15，论文已加 simulation + stratified DEFF + cluster bootstrap，改善明显。从 R15 的 Must-Fix 降级。\n\n**所需修改**: 明确推荐 simple-mean DEFF 作为 primary estimate，weighted-mean 定位为 conservative bound，附理由。\n\n**W2 [warning, 共识] §5.2 审计协议从 mechanism-agnostic 的 DIF 推断因果机制**\n\n\"DIF on web-clean items suggests capability shift\" 超出了 DIF 方法的能力边界。DIF 检测 *that* items function differently，但不能告诉 *why*。在审计协议这种规范性建议中，正面因果声称可能被误读。\n\n**所需修改**: 改为排除性推理（\"inconsistent with contamination as sole mechanism\"），加 caveat \"DIF alone cannot determine causation\"。\n\n**W3 [warning, 共识] Discussion (§5) 缺乏深层 insight**\n\n§5.1 本质是附加实验结果（base/instruct 分层），§5.2 提供操作建议但缺乏对 temporal DIF 成因假说和对 LLM 评测生态系统性影响的讨论。R1 指出 8 页限制的合理约束，且 §5.1 的 base/instruct 方向差异提供了 structured signal 证据，超越简单重述。\n\n**所需修改**: 增加 1-2 段对 temporal DIF 系统性影响的讨论（排行榜解读、benchmark 生命周期管理）。\n\n**W4 [warning, 共识] Abstract 信息密度过高**\n\n单段 Abstract 含 15+ 数值（5,227 models, 27,125 items, 17.9–31.3%, Jaccard = 0.206, χ² = 562.7, ±2.12pp 等），影响不熟悉 DIF 术语的 NLP 读者的可读性。\n\n**所需修改**: 保留核心数字（规模、DIF 率、分数位移），统计检验细节移至 Introduction。\n\n**W5 [warning, 视觉审查] 主文超页——Conclusion 位于 page 9**\n\n视觉审查发现 Sections 1-6 约占 8.3–8.5 页，Conclusion 位于 page 9 右栏。`\\enlargethispage*{4\\baselineskip}` 扩展了 Discussion 页面但仍超出 EMNLP 2026 strict 8-page limit。\n\n**所需修改**: 压缩正文至 strict 8 页：移除 `\\enlargethispage`，压缩 §2 或 §5 约 0.3–0.5 页。\n\n**W6 [warning, 共识] Semi-synthetic ΔTPR 应标为检测力上界而非 point estimate**\n\nUniform binary flipping 是检测的 best-case scenario。论文已加 difficulty-dependent injection（ΔTPR ≈ 0.41 vs 0.51 uniform, ~20% reduction）和 \"stylized/may overestimate\" 措辞，改善明显。残余问题：instruct 模型残差 gap 13×（无法复制 near-zero direction reversal）。\n\n*进展*: 相比 R15 的 Must-Fix，显著改善，降级。\n\n**所需修改**: 正文明确 ΔTPR 是 upper bound 而非 point estimate。\n\n---\n\n## Reviewer Consensus（交叉分享后共识）\n\n1. **[AGREE]** ETS 阈值缺乏 LLM-specific 校准是论文最大方法论盲点（N1）\n2. **[AGREE]** DEFF 2× 不确定性影响定量精度但证据链已改善（W1）\n3. **[AGREE]** Semi-synthetic injection 是 upper bound，不是 power estimation（W6）\n4. **[AGREE]** §5.2 mechanism inference 超出方法能力（W2）\n5. **[AGREE]** Abstract 信息密度过高（W4）\n6. **[AGREE]** 定性结论稳健：temporal DIF 以非平凡比例存在（~27–29%），远超随机基线\n7. **[AGREE]** Cross-subject matching 提供了实质性的 LLM-specific 方法学贡献\n8. **[AGREE]** 论文的经验工作（规模 + 控制）处于高水平\n\n## Reviewer Divergence（交叉分享后分歧）\n\n1. **Contribution 1 的贡献深度**: R2 认为 global-vs-differential 独立性是定义上预期的结果；R1 认为 contamination 文献的隐含假设使实证否证有价值。**双方均同意应降低其贡献层级**。\n\n2. **Cross-subject matching 的新颖性定位**: R2 认为是 \"engineering choice\"；R1 认为是 \"formal contribution with ΔFPR=0 guarantee\"（含 Section 3.4 的严格推导 + Table 7 的实证验证）。**R1 的论证更有力**——该保证是 formal result 且此前在 LLM 评测中未被形式化。\n\n3. **Multiple testing 循环论证**: R1 认为 BH-FDR 在大 N 下的无效性构成循环逻辑；R2 反驳 ETS C 分类的约束性条件是 effect size 而非 p-value，大样本下转向 effect-size 驱动是系统设计的一部分。**R2 的论证更有说服力**——论文已在 §3.2 讨论了 DEFF 如何恢复 p-value 选择性。\n\n4. **Composition confound**: R1 认为 11.8pp composition gap 仍可能膨胀聚合 C%；R2 引用 Appendix O base-only (32.1%) / instruct-only (36.5%) 分析，认为已充分排除。**R2 的数据反驳有力**——两个纯子群独立展现高 DIF 率，composition 影响方向而非检出率。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** |Δ_MH| = 1.5 在 LLM 排名中的实际影响？不同阈值（1.0, 1.5, 2.0, 2.5）下的 average rank displacement 分别是多少？\n\n**Q2.** Random-split 下 |Δ_MH| 分布的 95th percentile 是多少？可否作为 LLM-specific empirical null 与 ETS 1.5 比较？\n\n**Q3.** DEFF simulation 中如果 ICC 与 family size 不呈负相关，simple-mean 估计量是否仍然优于 weighted-mean？\n\n**Q4.** Difficulty × model-type interaction 能解释多大比例的 observed temporal DIF？是否存在 difficulty-dependent capability improvements（无 contamination）即可产生类似幅度 DIF 的可能性？\n\n**Q5.** 不同学科的 DIF enrichment ratio 差异（如 Humanities vs STEM）的驱动因素——差异化污染率还是题目结构特性？\n\n**Q6.** DIF-flagged items 是否应被排除出 Growing Pains (Habba et al., 2026) 的 anchor sets？两个框架的互补关系可否更明确地讨论？\n\n---\n\n## Missing References\n\n**R2 建议（需验证 arXiv ID 真实性）:**\n1. Adaptive Testing for LLM Evaluation (arxiv 2511.04689) — IRT Fisher information 自适应评测\n2. JE-IRT: Joint Embedding IRT (arxiv 2509.22888) — geometric lens on LLM abilities\n3. Confident Rankings with Fewer Items (arxiv 2601.13885) — 连续分数自适应测试\n4. When Benchmarks Leak: Inference-Time Decontamination (arxiv 2601.19334)\n\n**R1 建议:**\n5. Martinková & Drabinová (2018) ShinyItemAnalysis — DIF 分析替代工具\n6. Chalmers (2012) mirt — 主要 MIRT 软件文献\n\n---\n\n## External Review\n\n外部审稿：未配置（`external_review.paperreview_ai.enabled` 未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4.5 分钟）。\n\n| Severity | Finding |\n|----------|---------|\n| **critical** | 主文超页：Sections 1-6 约占 8.3-8.5 页，Conclusion 位于 page 9。违反 EMNLP 2026 strict 8-page limit。 |\n| **warning** | Pages 3-5 连续 3 页无 figure/table（Related Work + Method 纯文本），§3 缺少 DIF audit pipeline 概览图。 |\n| **warning** | 首页无视觉锚点（Title + Abstract + Intro 全文本），Figure 1 在 page 2。 |\n| info | 附录 Figures 3-6 axis label 约 6-7pt，接近可读性下限。 |\n| info | Figure 1 红/蓝配色有冗余线型编码，色盲安全可接受但非最优。 |\n| info | Table 3 信息密度高但可读，最优值加粗。 |\n| info | 引用格式统一，无未解析引用，无 margin 溢出。 |\n| info | 全文无公式渲染错误、无 section heading 孤悬页底，表格统一 booktabs 风格。 |\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 (Borderline Conference)**\n\n**R1**: 3.5 (Borderline Conference), Confidence 4/5\n**R2**: 3.5 (Borderline Conference), Confidence 4/5\n\n**综合判断**: 论文在一个重要且及时的问题上做了大规模、严谨的经验工作。Cross-subject matching 提供了实质性的方法学贡献（formal ΔFPR=0 guarantee）。核心定性结论稳健：temporal DIF 以 ~27–29% 的非平凡比例存在，远超随机基线 170×+，且不受 family structure、ability mismatch 或 composition shift 的混淆。\n\n主要不足集中在两个层面：\n\n1. **方法论校准缺口**（N1）：ETS 阈值未经 LLM 领域特定校准——这是论文声称做了 \"methodological adaptations for LLM evaluation\" 但实际遗漏的最关键适配。DEFF 2× 不确定性进一步影响定量精度。\n\n2. **贡献叙事偏高**（N2）：Contribution 1（正交性）和 Contribution 3 中的 DEFF/semi-synthetic 部分存在过度声称。Cross-subject matching 的新颖性被 Reviewer 间的分歧暴露——需要更清晰的 positioning 来让其方法学价值被充分认可。\n\n如果作者能：(1) 提供 LLM-specific 阈值锚定（random-split empirical null + rank displacement per threshold），(2) 重构贡献层级（突出 cross-subject matching 的 formal guarantee，降低 C1 和 C3 其余部分），(3) 解决页数超限和 Abstract 可读性问题——论文有潜力上升到 Conference 水平（4.0）。当前状态位于 Borderline Conference 与 Findings 之间的上端。\n\n**使用 EMNLP 2026 ARR 评分标准**: 3.5 = Borderline Conference\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 三个 contributions 的排序和权重需要重构。当前 C1 占据首位但贡献深度最浅。建议：C2（temporal DIF at scale）→ C1（cross-subject matching formal guarantee）→ C3（empirical independence of global/differential signals as motivating observation）。\n- \"to our knowledge the largest-scale DIF analysis on LLM benchmarks\" 声称合理但应注明 scale 的具体维度（models × items × benchmarks）。\n\n### Section 2 (Related Work)\n- \"We do not modify the core MH statistic\" 这句在交叉回应中被 R1 标记为不应删除（它是诚实的），但也不应与 \"three methodological adaptations\" 构成矛盾。建议重写为：\"We retain the standard MH statistic and develop three LLM-specific adaptations around it\"。\n- 6 篇遗漏引用需核实后择优补充（见 Missing References）。\n\n### Section 3 (Method)\n- §3.2: 应明确承认 ETS 阈值在当前 N 下本质是 effect-size 准则（p-value 近乎退化），并讨论该 effect size 在 LLM 评估中的实质意义。\n- §3.2: \"At N = 5,227\" 应改为实际 temporal cohort 的有效 N（1,887）。5,227 是全部模型数。\n- §3.4: Cross-subject matching 的 ΔFPR=0 guarantee 是论文最强的方法学贡献，应在 Introduction 中给予更突出的位置。\n\n### Section 4 (Experiments)\n- §4.2: DEFF 讨论已大幅改善，但应明确推荐 simple-mean 为 primary estimate。\n- §4.7: GSM8K 复制描述过于简略（仅 1 段），应至少报告 items/models 数量和与 MMLU 的模式异同。\n\n### Section 5 (Discussion)\n- §5.1: Base/instruct 方向差异（χ² = 562.7）是有价值的 structured signal，但应更明确讨论其对 LLM 评测实践的 implications。\n- §5.2: \"suggests capability shift\" → \"inconsistent with contamination as sole mechanism\"。\n- `\\enlargethispage*{4\\baselineskip}` 应移除。\n\n### Section 6 (Conclusion)\n- 当前 5 句简洁有效，但因页数超限可能需要进一步压缩或将部分内容移入 Discussion。\n\n### Limitations\n- 应补充：(1) 模型发布日期与训练数据截止时间不一定对齐；(2) 对 MMLU 式 MCQ 以外题型的泛化性仍需更多验证（虽有 GSM8K 但仅 1 段描述）。\n\n### Appendix\n- 深度出色，但 Figures 3-6 的 axis label 应增大至 ≥8pt。\n- Appendix I (DEFF Simulation) 的 4 种场景可考虑增加 1-2 种额外场景以增强说服力。",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1532 · 2026-05-23T10:41:39.813607+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4166
}
```

</details>

---


### Assistant

_source line 1533 · 2026-05-23T10:41:50.996170+00:00_

---

**Round 16 审稿完成。**

审稿报告已投递至 Research Director。

**最终评分: 3.5 / 5 (Borderline Conference)**，R1 和 R2 评分一致。

**关键发现汇总:**

| 类型 | 数量 | 核心问题 |
|------|------|----------|
| Must-Fix | 2 | N1: ETS 阈值缺 LLM 校准; N2: 贡献声称偏高 |
| Should-Fix | 6 | DEFF 推荐、mechanism inference、Discussion 深度、Abstract 密度、页数超限、semi-synthetic upper bound |
| Minor | 3 | 术语一致性、有效 N 澄清、遗漏引用 |
| 视觉 | 1 critical + 2 warning | 主文超 8 页（Conclusion 在 page 9） |

**升级路径**: 补充 LLM-specific 阈值锚定 + 重构贡献层级 + 解决页数超限 → 有潜力达到 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 149

## Round 149

2 recorded events


### User

_source line 1534 · 2026-05-23T10:41:53.654121+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1**（global vs. DIF 独立性）：[REBUT] — 定义上不同≠经验上独立，contamination 文献隐含了二者相关的假设，实证否证不是"显而易见"。但同意其作为 Contribution #1 的位置可调整。
- **N2**（三项适配新颖性）：对 (a) cross-subject matching [REBUT]——有 formal ΔFPR=0 guarantee，不是 implementation decision；对 (b) DEFF 和 (c) semi-synthetic 部分 [AGREE]。
- **W1–W3**：基本 [AGREE]，§5.2 的 mechanism inference 超出 DIF 能力、Discussion 可更深、Abstract 过密。
- **W4**（Limitations 窄）：部分 [REBUT]——GSM8K 复制和 Table 3 已覆盖泛化性，但 release date vs. training cutoff 不对齐值得补充。
- **Minor M1–M4**：全部 [AGREE]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1535 · 2026-05-23T10:42:08.355772+00:00_

审稿报告已投递至 Research Director。

**Round 16 审稿完成。**

- **评分**: 3.5 / 5 (Borderline Conference)，R1 和 R2 一致
- **2 项 Must-Fix**: (1) ETS 阈值缺乏 LLM-specific 校准——核心定量声称的基础；(2) Contribution 1 和 3 的贡献声称偏高需重构
- **6 项 Should-Fix**: DEFF 推荐估计量、§5.2 mechanism inference 措辞、Discussion 深度、Abstract 信息密度、主文超页（Conclusion 在 page 9）、ΔTPR 标为 upper bound
- **3 项 Info**: 术语一致性、有效 N 澄清、6 篇遗漏引用
- **视觉审查**: 1 critical（超页）+ 2 warning（pages 3-5 无图表、首页无视觉锚点）
- **Issue Tracker**: 已同步更新，13 项 open issues（2 critical, 6 warning, 3 info, 2 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 150

## Round 150

52 recorded events


### User

_source line 1536 · 2026-05-23T11:23:22.625333+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1537 · 2026-05-23T11:23:28.453006+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1538 · 2026-05-23T11:23:28.453828+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1539 · 2026-05-23T11:23:34.054249+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1540 · 2026-05-23T11:23:34.105909+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1541 · 2026-05-23T11:23:38.072353+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1542 · 2026-05-23T11:23:38.123884+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1543 · 2026-05-23T11:23:40.383834+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1544 · 2026-05-23T11:23:41.187635+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1545 · 2026-05-23T11:23:41.188037+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1546 · 2026-05-23T11:23:41.288682+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1547 · 2026-05-23T11:23:45.506458+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-23T11:23:47.364338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-23T11:23:48.218237+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Score Incomparability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-23T11:23:48.218581+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1551 · 2026-05-23T11:23:48.269041+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1552 · 2026-05-23T11:23:50.930422+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

Based on the search results, I found information about EMNLP 2026, but the specific page limit details for ARR submissions are not explicitly stated in the EMNLP 2026 Call for Main Conference Papers page. EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both sub
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5423
}
```

</details>

---


### Tool call

_source line 1553 · 2026-05-23T11:23:56.100226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-23T11:23:58.410200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-23T11:23:59.113455+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 models), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (${\approx}$27--29\% for MMLU after non-independence corrections; conservative bound 13.5\%; random-split baseline 0.62\%). Web-overlap contamination labels are near-independent of DIF flags: global exposure and differential functioning are complementary diagnostic dimensions. Temporal DIF does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals structured item-level change---base and instruct models exhibit opposite DIF patterns---and shifts DIF-corrected scores by ${+}2.12$\,pp on average. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-23T11:23:59.214296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1557 · 2026-05-23T11:23:59.365369+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} (measurement non-invariance across temporal cohorts, manifesting as score incomparability) as the empirical phenomenon when DIF is detected---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.62\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 849 rank positions. The incomparability is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items appear in training corpora---through membership inference~\citep{shi2024mink} and performance-based detection~\citep{deko
…[truncated 3074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-23T11:23:59.365893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-23T11:23:59.767872+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating} in-context learning effects~\citep{zawalski2026codec}, or inference-time decontamination~\citep{chai2026benchmarksleak}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introd
…[truncated 4571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-23T11:23:59.818562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-23T11:24:00.823199+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-23T11:24:00.823568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-23T11:24:01.275916+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: 31\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two DEFF estimators bound the non-independence effect in parallel: simple-mean DEFF (29.2\%) and cluster bootstrap (26.7\%) converge on ${\approx}$27--29\%, while the conservative weighted-mean DEFF yields 13.5\%---still ${\approx}22\times$ the random baseline (\Cref{app:deff,app:deff_simulation}). We recommend simple-mean DEFF as the primary estimate: it converges with the cluster bootstrap and DEFF simulation, while weighted-mean DEFF over-corrects by down-weighting large families with systematically lower ICC. Under 100 random permutations within the 2023 c
…[truncated 10755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-23T11:24:01.276393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-23T11:24:01.778675+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Temporal DIF as Structured Signal}
5	\label{sec:disc_temporal}
6	
7	\looseness=-1
8	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design. Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
9	
10	\looseness=-1
11	Composition downsampling ($\Delta = 1.08$\,pp), base-only (32.1\%), and instruct-only (36.5\%) temporal analyses independently confirm DIF is not an artifact of cohort structure (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}). These findings have immediate implications for leaderboard maintenance: temporal DIF means the same score carries different meaning across model generations, motivating periodic psychometric audits alongside score reporting.
12	
13	\looseness=-1
14	Three features distinguish LLM temporal DIF from educational settings: (1)~the observed C\% (${\approx}$27--29\%) substantially exceeds typical educational DIF rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$), unlike educational settings where DIF correlates with construct-irrelevant variance; (3)~model families introduce non-independence (design effect) absent in human testing, necessitating DEFF correction (\Cref{app:deff}).
15	
16	\subsection{Recommended DIF Audit Protocol}
17	\label{sec:disc_protocol}
18	
19	\looseness=-1
20	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend MH-DIF
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-23T11:24:01.779226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-23T11:24:02.231860+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (${\approx}$27--29\% for MMLU; conservative bound: 13.5\%), while aggregate rankings remain preserved ($\rho \approx 0.997$). Global exposure and differential functioning are complementary diagnostic dimensions (Jaccard $= 0.206$), confirmed by opposite base-vs-instruct DIF patterns ($\chi^2 = 562.7$). DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with rank displacements exceeding ${\pm}500$. Mechanism-conditional DIF audit should complement contamination screening as standard practice~\citep{habba2026growingpains}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-23T11:24:02.232393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-23T11:24:03.187034+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not cou
…[truncated 1244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7086
}
```

</details>

---


### Tool result

_source line 1570 · 2026-05-23T11:24:03.187598+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\Delta\mathrm{TPR}$ values may overestimate detection power, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. The framework detects \emph{that} items function differently but not \emph{why}---a deliberate design choice that limits immediate actionability; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric. Additionally, model release dates need not align with training-data cu
…[truncated 144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1571 · 2026-05-23T11:24:03.187920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1572 · 2026-05-23T11:24:03.640868+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 30324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1573 · 2026-05-23T11:24:03.943518+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1574 · 2026-05-23T11:24:04.096586+00:00_

issues:
  # === Round 16 issues (all resolved, Reviewer-verified R17) ===

  - id: "R16-N1"
    summary: "ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准——核心定量声称的基础"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 15
    last_seen_round: 16
    mentions:
      - round: 15
        reviewers: [1, 2]
        note: "R15-W1: warning 级别，threshold sensitivity + random baseline 部分缓解"
      - round: 16
        reviewers: [1, 2]
        note: "升级为 Must-Fix。需 LLM-specific empirical null + rank displacement per threshold。"
    action_items:
      - round: 16
        action: "Random-split null distribution (100 permutations): P99=1.45. 写入 §4.1. 0.18%→0.62% 全文统一。"
        assigned_to: paper_agent
        status: done
    resolution: "§4.1 插入 empirical null (P99=1.45 ≈ ETS C 1.5). 0.18→0.62 全文 12 处修正. Reviewer 验证 PASS."
    resolution_round: 17

  - id: "R16-N2"
    summary: "Contribution 1（global-vs-differential 正交性）和 Contribution 3（three methodological adaptations）的贡献声称均存在过度定位"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 13
    last_seen_round: 16
    mentions:
      - round: 13
        reviewers: [1, 2]
        note: "R13-W6: 方法论新颖性有限"
      - round: 14
        reviewers: [1, 2]
        note: "R14-W7/N2: innovations→adaptations"
      - round: 15
        reviewers: [1, 2]
        note: "R15-N3/I1: framework→adaptations 改善但自矛盾"
      - round: 16
        reviewers: [1, 2]
        note: "复发 ×4 轮。C1 降级为 motivating observation 合并入 C2; C3 聚焦 cross-subject matching formal guarantee。"
    action_items:
      - round: 16
        action: "结构性重构三项贡献为两项"
        assigned_to: paper_agent
        status: done
    resolution: "3→2 contributions. C1=temporal DIF at scale + orthogonality; C2=cross-subject matching ΔFPR=0 + supporting choices. Reviewer 验证 PASS."
    resolution_round: 17

  - id: "R16-W1"
    summary: "DEFF 校正两种估计量差异 2× 削弱 headline 定量精度"
    category: method
    severity: warning
    status: resolve
…[truncated 9902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1575 · 2026-05-23T11:24:23.082144+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 1576 · 2026-05-23T11:24:23.586075+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\\n\\n## Paper Type\\nEmpirical analysis + methodological framework. Discovery paper with substantive LLM-specific methodological adaptations. \\\"DIF audit framework reveals and quantifies temporal score incomparability.\\\" NOT \\\"just applied standard MH-DIF\\\" — three LLM-specific adaptations address challenges absent in educational testing, with cross-subject matching as a genuine innovation.\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-st
…[truncated 4376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1577 · 2026-05-23T11:24:23.586572+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1578 · 2026-05-23T11:24:24.842145+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 1579 · 2026-05-23T11:24:24.993236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1580 · 2026-05-23T11:24:24.993826+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{zawalski2026codec,
6	  title     = {Detecting Data Contamination in {LLM}s via In-Context Learning},
7	  author    = {Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
8	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
9	  year      = {2026},
10	  url       = {https://arxiv.org/abs/2510.27055}
11	}
12	
13	@inproceedings{balloccu2024leak,
14	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
15	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
16	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
17	  year      = {2024},
18	  doi       = {10.18653/v1/2024.eacl-long.5},
19	  url       = {https://arxiv.org/abs/2402.03927}
20	}
21	
22	@inproceedings{dekoninck2024constat,
23	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
24	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2405.16281}
28	}
29	
30	@inproceedings{golchin2024timetravel,
31	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
32	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
33	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
34	  year      = {2024},
35	  url       = {https://arxiv.org/abs/2308.08493}
36	}
37	
38	@inproceedings{li2024contamination,
39	  title     = {An Open-Source Data Contamination Report for Large Language Models},

…[truncated 3249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1581 · 2026-05-23T11:24:47.144946+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1582 · 2026-05-23T11:25:07.089149+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19944
}
```

</details>

---


### Tool call

_source line 1583 · 2026-05-23T11:25:09.149796+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **EMNLP 2026** Long Paper via ACL Rolling Review (ARR)\n- 正文 8 页限制，参考文献无限制\n- Limitations 章节必须有，不计页数\n- ACL 模板，double-blind\n- Deadline: 2026-05-25\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文文件\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各章节在 `sections/` 目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **DIF 方法论适用性**：MH-DIF 从教育测量迁移到 LLM 评估的合理性。ETS 阈值（|Δ_MH| ≥ 1.5）的 LLM 适切性——论文是否提供了充分的 empirical calibration？随机分割基线是否足以建立 null distribution？\n2. **统计控制充分性**：DEFF 校正两种估计量（simple-mean 29.2% vs weighted-mean 13.5%）的选择是否合理？推荐 simple-mean 作为 primary estimate 的论证是否充分？非独立性处理是否到位？\n3. **Semi-synthetic validation**：uniform binary flipping 的 ecological validity。ΔTPR 标为 detection-power upper bound 是否充分？difficulty-dependent injection 是否弥补了 uniform 的局限？\n4. **Cross-subject matching**：ΔFPR=0 的 formal guarantee 在什么条件下成立？k≤5 的限定是否充分讨论？当 k>5 时 graceful degradation 的论证是否严谨？\n5. **实验设计**：temporal cohort 划分（2023 vs 2024）的合理性；ability confound 的控制（matched-ability quintile, NN matching）；cross-benchmark replication 的说服力\n6. **Ground truth analysis**：DIF 与 web-overlap labels 的正交性论证逻辑是否自洽？enrichment≈1.0 的解释是否 convincing？\n7. **Downstream impact**：ρ≈0.997 的 ranking preservation 与 ±800 rank displacement 的张力如何解读？DIF-corrected scoring 的实际意义\n\n请按 ARR 审稿标准出具完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **EMNLP 2026** Long Paper via ACL Rolling Review (ARR)\n- 正文 8 页限制，参考文献无限制\n- Limitations 章节必须有，不计页数\n- ACL 模板，double-blind\n- Deadline: 2026-05-25\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文文件\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各章节在 `sections/` 目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **DIF 方法论适用性**：MH-DIF 从教育测量迁移到 LLM 评估的合理性。ETS 阈值（|Δ_MH| ≥ 1.5）的 LLM 适切性——论文是否提供了充分的 empirical calibration？随机分割基线是否足以建立 null distribution？\n2. **统计控制充分性**：DEFF 校正两种估计量（simple-mean 29.2% vs weighted-mean 13.5%）的选择是否合理？推荐 simple-mean 作为 primary estimate 的论证是否充分？非独立性处理是否到位？\n3. **Semi-synthetic validation**：uniform binary flipping 的 ecological validity。ΔTPR 标为 detection-power upper bound 是否充分？difficulty-dependent injection 是否弥补了 uniform 的局限？\n4. **Cross-subject matching**：ΔFPR=0 的 formal guarantee 在什么条件下成立？k≤5 的限定是否充分讨论？当 k>5 时 graceful degradation 的论证是否严谨？\n5. **实验设计**：temporal cohort 划分（2023 vs 2024）的合理性；ability confound 的控制（matched-ability quintile, NN matching）；cross-benchmark replication 的说服力\n6. **Ground truth analysis**：DIF 与 web-overlap labels 的正交性论证逻辑是否自洽？enrichment≈1.0 的解释是否 convincing？\n7. **Downstream impact**：ρ≈0.997 的 ranking preservation 与 ±800 rank displacement 的张力如何解读？DIF-corrected scoring 的实际意义\n\n请按 ARR 审稿标准出具完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1584 · 2026-05-23T11:25:22.221549+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13071
}
```

</details>

---


### Tool call

_source line 1585 · 2026-05-23T11:25:26.502075+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **EMNLP 2026** Long Paper via ACL Rolling Review (ARR)\n- 正文 8 页限制，参考文献无限制\n- Limitations 章节必须有，不计页数\n- ACL 模板，double-blind\n- Deadline: 2026-05-25\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文文件\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各章节在 `sections/` 目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **新颖性与贡献定位**：将 DIF 应用于 LLM benchmarks 的新颖性如何？两项贡献（temporal DIF at scale + cross-subject matching ΔFPR=0）的定位是否恰当？与 Growing Pains (Habba et al., 2026) 的关系是否充分区分？与 contamination detection 文献的对话是否到位？\n2. **Related Work 覆盖度**：是否遗漏重要相关工作？IRT-for-LLM 领域的最新文献是否充分覆盖？DIF 方法论文献（MH 之外的替代方法）是否充分讨论？benchmark quality / dynamic benchmark 文献是否恰当定位？\n3. **叙事结构与可读性**：Abstract 信息密度是否合适？Introduction 的叙事逻辑是否清晰？\"temporal score incomparability\" vs \"measurement non-invariance\" 的术语使用是否一致？各章节之间的逻辑衔接是否流畅？\n4. **贡献与声称匹配**：论文声称的贡献是否与实验结果匹配？是否有过度声称或声称不足？mechanism-agnostic 的立场是否始终一致？\n5. **格式与规范**：是否严格遵守 8 页限制？表格/图表质量、编号、引用格式是否规范？double-blind 匿名性是否保持？Limitations 章节是否充分但不冗余？\n6. **整体影响力**：这篇论文对 LLM evaluation 社区的实际影响？审计协议的可操作性？发现对 leaderboard 维护者的启示？\n7. **写作风格**：是否存在 AI 风格痕迹？措辞是否精确？是否存在不必要的重复或冗余？\n\n请按 ARR 审稿标准出具完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **EMNLP 2026** Long Paper via ACL Rolling Review (ARR)\n- 正文 8 页限制，参考文献无限制\n- Limitations 章节必须有，不计页数\n- ACL 模板，double-blind\n- Deadline: 2026-05-25\n- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文文件\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各章节在 `sections/` 目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_17/submitted.pdf`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **新颖性与贡献定位**：将 DIF 应用于 LLM benchmarks 的新颖性如何？两项贡献（temporal DIF at scale + cross-subject matching ΔFPR=0）的定位是否恰当？与 Growing Pains (Habba et al., 2026) 的关系是否充分区分？与 contamination detection 文献的对话是否到位？\n2. **Related Work 覆盖度**：是否遗漏重要相关工作？IRT-for-LLM 领域的最新文献是否充分覆盖？DIF 方法论文献（MH 之外的替代方法）是否充分讨论？benchmark quality / dynamic benchmark 文献是否恰当定位？\n3. **叙事结构与可读性**：Abstract 信息密度是否合适？Introduction 的叙事逻辑是否清晰？\"temporal score incomparability\" vs \"measurement non-invariance\" 的术语使用是否一致？各章节之间的逻辑衔接是否流畅？\n4. **贡献与声称匹配**：论文声称的贡献是否与实验结果匹配？是否有过度声称或声称不足？mechanism-agnostic 的立场是否始终一致？\n5. **格式与规范**：是否严格遵守 8 页限制？表格/图表质量、编号、引用格式是否规范？double-blind 匿名性是否保持？Limitations 章节是否充分但不冗余？\n6. **整体影响力**：这篇论文对 LLM evaluation 社区的实际影响？审计协议的可操作性？发现对 leaderboard 维护者的启示？\n7. **写作风格**：是否存在 AI 风格痕迹？措辞是否精确？是否存在不必要的重复或冗余？\n\n请按 ARR 审稿标准出具完整审稿意见，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（含评分和置信度）。",
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1586 · 2026-05-23T11:25:28.178321+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1676
}
```

</details>

---


### Assistant

_source line 1587 · 2026-05-23T11:25:38.784457+00:00_

已并行派发：
- **视觉审查 Agent**: 已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）: 已分配
- **Reviewer 2**（新颖性/完整性）: 已分配

等待两位 Reviewer 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 151

## Round 151

2 recorded events


### User

_source line 1588 · 2026-05-23T11:31:11.218356+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：方法严谨性 + 实验有效性

---

## Summary

本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析迁移到 LLM 基准评测领域，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现 2023 与 2024 模型群组之间约 27–29% 的题目存在显著时序 DIF（保守下界 13.5%），远超随机基线（0.62%）。论文提出跨学科匹配（cross-subject matching）策略并给出 ΔFPR=0 的形式化保证，通过半合成注入框架验证检测能力，并在六个 METABENCH 基准上复现。核心发现是 DIF 标记与 web-overlap 污染标签近乎正交（Jaccard=0.206），base 与 instruct 模型呈现相反的 DIF 方向模式。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 将 DIF 引入 LLM 评测是新颖且及时的贡献，实验控制详尽，但 DEFF 估计量选择的论证不够严密、半合成验证的生态效度有限、以及"检测到 DIF 之后怎么办"的可操作性不足，使本文处于 Conference 与 Findings 的边界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论总体严谨，多重控制（随机分割、能力匹配、LOFO、跨基准复现）令人信服；但 DEFF 双估计量差距达 2× 且选择论证有循环性，k>5 时 ΔFPR 保证退化，半合成注入生态效度有限 |
| Excitement | 3.5/5 | 将心理测量学的 DIF 方法引入 LLM 评测是新颖的跨学科贡献，正交性发现有理论价值；但 DIF 只能检测"what"不能回答"why"，实际可操作性受限，ρ≈0.997 削弱了实践紧迫性 |
| Overall Assessment | 3.5/5 | Borderline Conference — 贡献真实但关键方法选择需要更严谨的论证 |

**Confidence**: 4/5 — 对 DIF 方法论和 IRT 在 NLP 中的应用有深入了解，仔细核查了统计论证。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DEFF 估计量选择的论证存在循环性，且对核心结论影响巨大

- 具体位置：§4.2、§D (App DEFF)、Table 12 (App L: DEFF Simulation)
- 问题：论文给出两种 DEFF 估计量——simple-mean（C%=29.2%）和 weighted-mean（C%=13.5%），差距达 2.16×。论文推荐 simple-mean 为 primary estimate，理由是"它与 cluster bootstrap 和 DEFF simulation 收敛"。但 DEFF simulation（Table 12）的模拟场景本身使用了"size-dependent ICC matching empirical observations"——即用观测到的 ICC-size 反相关模式来构造模拟，再用模拟结果论证 simple-mean 更好，形成循环论证。此外，weighted-mean DEFF（Kish, 1965）是 survey sampling 文献中处理不等概率抽样的标准方法，论文将其降格为"conservative extreme"但未充分讨论在什么样本结构下 weighted-mean 是更合适的选择。13.5% 仍远超基线，但如果 weighted-mean 是正确的估计量，论文的 headline number（~27-29%）将被大幅下修，叙事的 framing 需要重新调整。
- 为什么影响接收：论文的核心 claim 是"~27-29% of items exhibit temporal DIF"。如果 DEFF 选择改变，这个 headline number 可能需要修改为"13.5-29.2%"的区间表述，而非将 simple-mean 作为点估计推荐。
- 建议修改方向：(1) 明确区分模拟研究的设计假设与待验证的假设，打破循环性；(2) 考虑采用区间表述（如"13.5-29.2%, with convergent evidence supporting the upper range"）而非推荐单一估计量；(3) 补充分析：如果使用 weighted-mean DEFF，论文的所有下游分析（排名影响、分数修正）如何变化。

**N2** [critical] 半合成验证框架的生态效度不足，ΔTPR 作为"detection-power upper bound"的声称不严密

- 具体位置：§3.4、§4.5、Limitations §(1)
- 问题：半合成注入使用 uniform binary flipping（将 focal group 的错误回答以固定概率翻转为正确），论文将报告的 ΔTPR 标记为"detection-power upper bound"。但这个上界声称缺乏严格论证：(a) 如果真实污染集中在特定难度范围的题目上（如只影响中等难度题目），DIF 信号可能比 uniform flipping 更强而非更弱；(b) difficulty-dependent injection（§4.5）确实产生了较低的 ΔTPR（0.41 vs 0.51），但这只验证了一种特定的非均匀模式，不能穷举所有可能的注入模式；(c) 论文未讨论 partial memorization（模型只记住答案的关键线索而非完整内容）会产生什么样的 DIF 信号——这是现实中最常见的"污染"模式。
- 为什么影响接收：半合成验证是论文方法有效性的关键支撑。如果 ΔTPR 不是真正的上界，那么论文对检测能力的表述需要降级，这影响读者对方法可靠性的判断。
- 建议修改方向：(1) 将"upper bound"改为"reference point under stylized uniform injection"；(2) 补充至少一种更接近现实的注入模式（如 partial-credit flipping：只将 focal group 的回答从最不可能的错误选项翻转到正确答案，模拟部分记忆）；(3) 讨论在什么条件下真实污染可能产生比 uniform flipping 更强的 DIF 信号。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] k>5 时 ΔFPR 保证退化的影响未被充分量化

- 具体位置：§3.4 Remark、§4.5、Table 7
- 问题：跨学科匹配的 ΔFPR=0 保证仅对 single-subject contamination（k≤5）成立。当 k=20（18% of domains）时 ΔFPR 上升至 0.069±0.018。论文在 §4.5 最后一句提到"worst-case ΔFPR at k=20 (0.069) represents up to 50% of the 13.5% lower bound"，这意味着如果污染广泛分布且 weighted-mean DEFF 是正确估计，FPR 通胀可能吃掉保守估计的近一半。但论文未系统讨论：在现实场景中，MMLU 57 个学科中有多少可能同时受到污染？如果模型在预训练中接触了大量公开数据，污染可能同时影响多数学科。
- 建议：(1) 提供关于"现实中 k 的合理范围"的论证——例如从 web-overlap 标签分布推断跨学科污染的经验分布；(2) 给出 ΔFPR 对 C% 估计的敏感性分析（如果 7pp 的 FPR 通胀全部转化为 false C flags，adjusted C% 从 X 降至 Y）。

**W2** [warning] DIF 与 web-overlap 正交性的解读存在替代解释

- 具体位置：§4.3、§5.1、Figure 1
- 问题：enrichment≈1.0（DIF-C 在 web-contaminated 和 web-clean 题目中的比率几乎相同）被解读为"两个诊断维度互补"。但还有一个更简单的替代解释：DIF 可能根本不在测量任何与污染相关的东西。如果 DIF 主要反映的是能力演化（capability evolution）或训练方法差异（RLHF/instruction tuning），那么与污染标签正交是自然的——但这削弱了论文将 DIF 定位为"complementary contamination diagnostic"的叙事。论文在 §5.1 和 Appendix B 提供了 base/instruct 方向反转和难度-方向交互作为机制证据，但 Appendix B 的 mixed-mechanism injection 未能匹配 instruct 模型的 ρ（模拟 -0.302 vs 观测 -0.079），作者自己也承认"instruct-model DIF is at least partially driven by non-contamination mechanisms"。
- 建议：(1) 更明确地将 DIF 定位为"measurement instability diagnostic"而非暗示它与污染互补——正交性发现说明它们是不同的东西，而非互补的工具；(2) 在 Discussion 中更充分地讨论"DIF 主要反映能力演化而非污染"这一可能性的含义。

**W3** [warning] ρ≈0.997 的排名保持与 ±800 rank displacement 之间的张力未充分解析

- 具体位置：§4.6、Appendix K
- 问题：论文同时报告了 ρ≈0.997（几乎完美的排名相关）和 ±800 的极端位移。Appendix K 的分析表明 reversal 集中在 Δrank<50 的"统计平局"模型对中（reversal rate 35.2%），>1000 时为 0%。但这个模式是任何噪声源（包括随机移除 31% 的题目）都会产生的。论文报告了 DIF-ordered removal 比 random removal 更快降低 ρ（Figure 6, z=-8 to -49），但未直接报告：随机移除同等数量题目后的 rank displacement 分布是什么？如果随机移除 31% 的题目也产生 ±500 的位移，那么 DIF-specific 的 downstream impact 就大幅缩水。
- 建议：补充随机移除 31% 题目后的 rank displacement 分布作为基线对比（mean Δ、99th percentile、±800 对应的百分位数），以量化 DIF-specific 的增量影响。

**W4** [warning] 时序群组定义的粒度问题

- 具体位置：§3.3、Limitations
- 问题：以日历年（2023 vs 2024）划分群组是粗粒度的。模型发布日期 ≠ 训练数据截止日期。2024 年初发布的模型很可能主要使用 2023 年之前的数据训练。论文在 Appendix E 报告了半年度粒度（C%=34.4%），但这进一步模糊而非澄清了信号的时间结构。更重要的是，如果 DIF 主要由训练方法的代际变化（如 RLHF 的普及）驱动，那么"时序"标签可能是误导性的——本质上是方法论差异而非时间差异。
- 建议：(1) 在正文中更明确地讨论 release date vs training cutoff 的混淆；(2) 考虑按训练方法论（base/instruct/RLHF）而非时间划分群组作为补充分析——论文已在 Appendix O-P 提供了 base-only 和 instruct-only 的时序 DIF，这些结果（均 >32%）支持 DIF 不完全由 composition shift 驱动，应在正文中更突出地呈现。

---

## 小问题（不影响接收）

- §3.2 中 ΔFPR=0 的陈述格式为"Remark"而非正式的 Proposition/Theorem，但论文在多处将其称为"formal guarantee"。建议统一：要么升级为 Proposition 并给出完整证明，要么降低"formal guarantee"的措辞。
- Figure 1 的 ICC 示意图（global vs differential contamination）概念清晰，但右图假设"only that cohort was disproportionately exposed"——这是 differential contamination 的定义而非经验发现，存在循环性。Caption 应更明确地标注这是 schematic/definitional illustration。
- Table 1 的 Within-family (Llama-2 vs 3) C%=61.3% 在能力匹配后收敛到 ~28-29%（Appendix C），这个信息很重要但在正文中不够突出。未经匹配的 61.3% 可能误导读者以为 within-family DIF 远高于 temporal DIF。
- §4.7 GSM1K 相关性分析（r=-0.478, N=33）过于初步，作为正式结果放在正文中分量不足。建议移至 Appendix 或更明确地标记为 exploratory。
- Limitations 中提到"generalizability to open-ended or partial-credit benchmarks is untested"，但 GSM8K（open-ended）已在 §4.7 中测试且结果一致（C%=18.9%）。这里的表述需要修正——应更精确地说"partial-credit and free-form generation benchmarks are untested"。

---

## 主要优势

1. **跨学科方法创新**: 首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型），填补了教育测量和 LLM 评测之间的方法论空白。
2. **实验控制的深度和广度**: 随机分割基线、能力匹配（NN matching）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control、跨基准复现——每一个潜在混淆变量都被系统地检验和排除。这种控制水平在 LLM 评测领域罕见。
3. **跨学科匹配的创新**: 将教育测量中的 purified subtest matching 改造为 LLM 多学科设置的 cross-subject matching，并提供形式化的 ΔFPR=0 保证（在 k≤5 条件下），是对方法论的实质性贡献。
4. **正交性发现的理论价值**: DIF 与 web-overlap 标签的近乎独立性（Jaccard=0.206, φ=0.012）是一个非平凡的经验发现，表明现有的全局污染检测和项目功能差异是不同的维度，具有重要的概念意义。
5. **Base/instruct 方向反转**: χ²=562.7 的 base/instruct 方向反转提供了强有力的机制分离证据，表明 DIF 反映的是结构化的项目级变化而非均匀的群组效应。
6. **写作质量**: 论文组织清晰，术语定义严谨（measurement invariance / DIF / temporal score incomparability 的三重区分），附录详实。

---

## Missing References

- Embretson, S.E. & Reise, S.P. (2000). *Item Response Theory for Psychologists*. 作为 IRT 基础参考，论文大量使用 IRT 概念但未引用此经典教材。
- Suk, Y. & Ryu, W. (2026). *Rethinking differential item functioning from a causal inference perspective*. 论文在 Appendix B 引用了此文（bibkey: suk2026rethinking），但在正文 Discussion 中讨论 DIF 的因果解释局限时未引用——考虑到 DIF"测 what 不测 why"是论文的核心局限之一，这篇因果推断视角的 DIF 文献应在正文中讨论。
- Martinková, P. & Drabinová, A. (2018). *ShinyItemAnalysis for teaching psychometrics and to enforce routine analysis of educational tests*. 作为 DIF 分析的实用工具参考。

---

## Questions for Authors

1. 如果使用 weighted-mean DEFF（C%=13.5%）重新计算所有下游分析（排名影响、分数修正、rank displacement），结果会发生什么定性变化？
2. 在 web-overlap 标签覆盖的 9,229 个题目中，跨学科的污染分布是什么样的？有多少学科有 >50% 的题目被标记为 web-contaminated？这能帮助约束"现实中 k 的合理范围"。
3. 论文是否考虑过使用 confirmatory DIF 方法（如 IRT-LR 或 MIMIC 模型）作为 MH-DIF 的交叉验证？非均匀 DIF 检测（§4.4: 17.7% additional items）暗示 MH 可能遗漏了重要信号。
4. Base-only temporal DIF（32.1%）和 instruct-only temporal DIF（36.5%）之间的差异是否在统计上显著？如果 instruct 模型的 DIF 率更高，这对"DIF 反映能力演化 vs 污染"的机制讨论有什么含义？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1589 · 2026-05-23T11:31:17.445666+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 152

## Round 152

2 recorded events


### User

_source line 1590 · 2026-05-23T11:31:24.839191+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**:
- **Overall**: 3.5 (Borderline Conference)
- **Soundness**: 3.5/5
- **Excitement**: 3.5/5
- **Confidence**: 4/5

**2 个 Must-Fix 问题**:
1. DEFF 估计量选择（simple-mean vs weighted-mean，差距 2×）的论证存在循环性——DEFF simulation 用观测到的 ICC-size 模式构造模拟，再用模拟结果论证 simple-mean 更好
2. 半合成验证的 ΔTPR "upper bound" 声称不严密——uniform flipping 不是检测能力的真正上界

**4 个 Should-Fix 问题**:
1. k>5 时 ΔFPR 保证退化的实际影响未量化
2. DIF-contamination 正交性有替代解释（DIF 可能根本不测量污染相关的东西）
3. ρ≈0.997 与 ±800 rank displacement 的张力需要随机移除基线对比
4. 日历年群组定义的粒度和"时序"标签可能是误导性的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1591 · 2026-05-23T11:31:33.252373+00:00_

Reviewer 1 已提交（3.5 Borderline Conference）。等待 Reviewer 2 完成初审后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 153

## Round 153

6 recorded events


### User

_source line 1592 · 2026-05-23T11:31:40.738768+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见：Temporal Score Incomparability in LLM Benchmarks

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 大规模 MH-DIF 审计方法论扎实、实证充分，但核心叙事存在 mechanism-agnostic 与 contamination-centric 的内在矛盾，新颖性主要在应用层面而非方法层面，与 Growing Pains 的差异化不够清晰。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | MH-DIF 方法正确应用，结构性控制充分（random split baseline、sensitivity check、cross-benchmark validation），semi-synthetic 验证框架设计合理但覆盖面窄 |
| Excitement | 3 / 5 | 核心贡献是将成熟心理测量方法应用于新领域，发现本身（DIF ≠ contamination, Jaccard ≈ 0.206）有价值，但方法论创新有限 |
| Reproducibility | 4 / 5 | 匿名代码链接已提供，METABENCH 数据公开，IRT 参数来自公开工具 PSN-IRT，实验设置描述详细 |
| Overall Assessment | 3.5 / 5 | Borderline Conference |
| Confidence | 4 / 5 | 熟悉 DIF 方法论和 LLM evaluation 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Mechanism-agnostic 定位与实验设计存在系统性矛盾
- 具体位置：Abstract ("without implying degradation or attributing cause")、Section 1 贡献列表、Section 3.4、Section 4.3、Section 4.5、Section 5.1、Appendix B
- 问题：论文反复声称采取 mechanism-agnostic 立场，但实验设计大量围绕 contamination 展开：
  - Section 3.4 的 Semi-Synthetic Injection Framework 明确注入 contamination
  - Section 4.3 "Ground Truth Mismatch" 直接对比 web-overlap contamination labels
  - Section 4.5 标题即为 "Detection Power under Controlled Injection"
  - Appendix B 标题为 "Mechanism Analysis"，讨论 contamination 机制
  - Section 3.4 的 Remark (Zero FPR) 中 "contamination" 一词出现多次
  
  这构成叙事上的自我矛盾：一方面声称不归因，另一方面整个验证体系都建立在 contamination 假设之上。
- 为什么影响接收：这不是措辞问题，而是论文核心定位的连贯性问题。Reviewer 和读者无法判断论文的真正立场——是一个通用的 measurement invariance 工具，还是一个 contamination detection 方法。这直接影响对贡献的评估。
- 建议修改方向：两条路选一条——（1）明确定位为 "contamination-induced DIF detection"，放弃 mechanism-agnostic 声称；或（2）保持 mechanism-agnostic，但将 contamination 相关实验重新定位为 "case study of one DIF-inducing mechanism"，在 framing 中明确 DIF 可能由多种原因引起（training methodology shifts、RLHF、format-specific advantages），contamination 只是其中之一，且实验设计的局限性在于仅验证了这一种。

**N2** [critical] Semi-synthetic validation 仅覆盖 uniform injection，与真实 contamination 模式脱节
- 具体位置：Section 3.4（"For each contaminated item, we flip incorrect responses..."）、Section 4.5、Limitations 第(1)点
- 问题：注入模型是 uniform binary response flipping——所有被注入的 item 以相同概率翻转。但论文自身在 Appendix B 和 Appendix C (Scheme D) 承认真实 contamination 是 difficulty-dependent 的。Section 4.5 末尾也提到 "Difficulty-dependent injection ... yields ΔTPR = 0.41 at p = 0.1"，显著低于 uniform injection 的 ΔTPR。这意味着：
  - 主文中报告的 detection power 数字（Section 4.1: TPR of 0.68–0.94, AUC of 0.93–0.94）基于 uniform injection，可能高估了真实场景下的检测能力
  - ΔFPR = 0 的形式证明依赖于特定注入结构，但在 difficulty-dependent injection 下 ΔFPR 的表现未在主文充分讨论
- 为什么影响接收：detection power 是论文的核心卖点之一（贡献列表第2条）。如果 power 估计基于过度简化的注入模型，读者无法信任这些数字在实际应用中的有效性。
- 建议修改方向：将 Scheme D (mixed injection) 的结果提升到主文 Section 4.5，与 uniform injection 并列报告。明确说明 uniform injection 是 upper bound，difficulty-dependent injection 更接近真实场景但 power 显著降低。调整 abstract 和 contributions 中的 power 声称。

**N3** [critical] 与 Growing Pains (Habba et al., 2026) 的差异化不充分
- 具体位置：Section 2 第3段末尾（"The closest concurrent work is Growing Pains..."）、Section 1 贡献列表
- 问题：论文声称 "to our knowledge, no prior work applies DIF to benchmark temporal comparability"（Section 2 末尾）。但 Growing Pains 执行的 anchor item selection for equating 本质上包含 DIF 筛选——识别跨时间功能不同的 items 以排除其作为 anchor。论文仅用一句话区分（"uses IRT calibration to establish anchor items for cross-temporal score equating via fixed-parameter calibration"），未深入讨论两者在方法论层面的本质差异和互补性。
- 为什么影响接收：如果 Growing Pains 已经在做类似的事（识别 temporally non-invariant items），本文的 novelty 声称需要更精确的 scoping。否则可能被 reviewer 认为是 incremental contribution。
- 建议修改方向：在 Section 2 或 Section 5 中增加一段专门对比：（1）Growing Pains 的 anchor selection 是 equating 的前置步骤，目标是建立可比分数；本文的 DIF 分析是诊断工具，目标是量化 non-invariance 的 pattern 和 magnitude。（2）MH-DIF 提供 effect size 分类（ETS A/B/C），Growing Pains 的 FPC 不提供。（3）本文的 cross-subject matching 是 Growing Pains 没有的方法论贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] MH 方法选择缺乏与替代方法的充分比较
- 具体位置：Section 2 DIF Methodology 段落、Section 3.2
- 问题：论文提及 logistic regression DIF、SIBTEST、Lord's F test、Raju area method（Section 2），但未解释为何选择 MH。鉴于 MMLU 的多维性（57 subjects）和论文自身承认的 2PL 模型拟合不佳（Section A.1: "2PL fit is poor for MMLU's multidimensional structure"），IRT-based DIF 方法（如 logistic regression DIF with ability-by-group interaction）可能更适合。"most widely used method" 不构成在新应用领域的充分理由。
- 建议：增加 1-2 句解释 MH 的优势（如不依赖参数模型、对 multidimensionality 的 robustness、computational scalability for 12,508 items），或在 Section A 中增加与 logistic regression DIF 的对比实验。

**W2** [warning] 时间粒度选择（年度 cohort）未经论证
- 具体位置：Section 3.3（"We construct five cohort comparisons: (1) Temporal: 2023 vs 2024"）
- 问题：选择年度 cohort 但未讨论为何此粒度合适。如果 contamination 或 training data 更新发生在更短时间尺度，年度分组可能掩盖 within-year 变化。论文有 5,227 个模型，sample size 允许更细粒度（如季度）。Appendix E 的 half-year granularity 分析（"splitting at the 6-month boundary yields C% = 34.4%"）暗示年度 vs 半年度结果差异不大，但这本身值得在主文讨论。
- 建议：在 Section 3.3 或 Section 5 中增加对 temporal granularity 选择的讨论。

**W3** [warning] Abstract 信息过载
- 具体位置：Abstract
- 问题：Abstract 包含至少 8 个独立的定量发现（17.9–31.3%、≤27.29%、13.5%、0.62%、Jaccard = 0.206、ΔFPR = 0、≈2.12 pp、≥500 rank positions）。这使读者难以在首次阅读时抓住核心信息。
- 建议：保留 2-3 个最重要的发现（如 DIF prevalence、DIF ≠ contamination、score incomparability magnitude），其余移至 Introduction。

**W4** [warning] Jaccard ≈ 0.206 被表述为 "near-independent" 不够精确
- 具体位置：Abstract ("web-overlap contamination labels are near-independent of DIF flags")、Section 1
- 问题：Jaccard = 0.206 意味着约 21% 的重叠，这是 low 但非 trivial。"near-independent" 暗示接近 0，但 0.206 在统计意义上并不接近独立。论文后续使用的 "complementary diagnostic dimensions" 更准确。
- 建议：将 "near-independent" 改为 "largely non-overlapping" 或 "weakly associated"，与后文 "complementary" 措辞保持一致。

**W5** [warning] DEFF 校正依赖 IRT 参数但模型拟合不佳
- 具体位置：Section 4.4、Appendix D、Section A.1
- 问题：Section A.1 承认 "2PL fit is poor for MMLU's multidimensional structure"，但 DEFF 校正（Section D）使用 IRT discrimination parameters。如果 IRT 模型拟合差，这些参数可能不可靠，进而使 DEFF 校正结果不可靠。论文未量化 DEFF 对 IRT 模型规范的敏感性。
- 建议：在 Appendix D 中增加 sensitivity analysis，测试 DEFF 在不同 IRT 模型（如 1PL vs 2PL vs 多维 IRT）下的稳定性，或明确说明 DEFF 校正仅作为 robustness check 而非核心结果。

---

## 小问题（不影响接收）

- Section 1 脚注1：匿名 GitHub 链接是否对 reviewer 可访问应确认
- Figure 1 caption 提及 "Left" 和 "Right"，但 Section 1 正文未显式引导读者逐步理解该图
- Table 3 列标题 "ρ" 和 "Ratio" 需要在 caption 中增加说明
- Equation 1 使用 α_MH 标记，后续公式中下标 MH 被省略，应保持一致
- 论文交替使用 "test-takers" 和 "examinees" 作为 LLM 类比，应统一术语
- Table 1 字体较小，打印阅读可能有困难
- Section 5.1 首段 "Temporal DIF detects that items function differently across cohorts, not why" 与后文立刻讨论 mechanism 的段落存在微妙张力

---

## 主要优势

1. **规模与严谨性**：5,227 个模型、6 个 benchmark、12,508 items 的大规模审计，配合充分的结构性控制（random split baseline C% 13.5%、sensitivity check、cross-benchmark validation across all 6 METABENCH benchmarks）——这是目前对 LLM benchmark temporal comparability 最全面的心理测量审计。

2. **Cross-subject matching 的 ΔFPR = 0 保证**：Section 3.4 的形式论证和实证验证表明 cross-subject matching 消除了 matching variable 导致的 false positives，这是将 DIF 应用于 LLM 评估的genuine 方法论贡献（不仅仅是套用现有方法）。

3. **DIF ≠ contamination 的实证发现**：DIF flags 与 web-overlap labels 的 Jaccard ≈ 0.206（Section 4.3）是genuinely surprising 且重要的发现。这表明 temporal measurement non-invariance 不能简单等同于 contamination，对评估社区的思维框架有实质推进。

4. **实际影响力**：DIF-corrected scores shift ≈2.12 pp、rank displacements ≥500（Section 4.6）直接说明 temporal score incomparability 的实际后果。Section 5.2 的审计协议具有可操作性。

5. **详实的 Appendix**：Sections A-L 提供了 sensitivity analysis (A.2)、mechanism analysis (B)、structural analysis (C)、design effect estimation (D)、uncertainty quantification (E)、cross-benchmark comparison (F)、item-level predictive analysis (G) 等全面的补充分析。

---

## Questions for Authors

1. Growing Pains 的 anchor item selection 过程中是否包含了类似 MH-DIF 的统计检验？如果是，本文的 novelty 相对于 Growing Pains 具体在哪里？

2. 如果将 temporal granularity 从年度改为季度，DIF prevalence (C%) 的变化趋势如何？是否有 preliminary 结果？

3. Logistic regression DIF（可以同时检验 uniform 和 non-uniform DIF）是否曾被考虑作为主要方法？如果考虑过但放弃了，原因是什么？

4. DEFF 校正在 1PL（不使用 discrimination parameter）下的结果是否与 2PL 下一致？

---

## Missing References

- Magis et al. (2010) "A general framework and an R package for the detection of dichotomous differential item functioning" — 已引用，但论文未讨论该 R 包中实现的多种 DIF 方法的比较
- 未见引用任何关于 **multidimensional DIF** 的文献（如 Shealy & Stout, 1993 的 multidimensional model-based DIF），考虑到 MMLU 的多维性这是一个值得讨论的方向
- 关于 **dynamic benchmarks** 的文献可以更全面：如 Kiela et al. (2021) "Dynabench" 提出的动态评估范式与本文发现的 temporal non-invariance 有直接关联



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1593 · 2026-05-23T11:32:09.468568+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] Mechanism-agnostic 定位与实验设计存在系统性矛盾\n- 论文反复声称采取 mechanism-agnostic 立场（Abstract: \"without implying degradation or attributing cause\"），但实验设计大量围绕 contamination 展开：Section 3.4 注入 contamination、Section 4.3 对比 web-overlap labels、Section 4.5 标题 \"Detection Power under Controlled Injection\"、Appendix B \"Mechanism Analysis\"。\n- 构成叙事上的自我矛盾：一方面声称不归因，另一方面整个验证体系建立在 contamination 假设之上。\n\n**N2** [critical] Semi-synthetic validation 仅覆盖 uniform injection，与真实 contamination 模式脱节\n- 主文的 detection power 数字（TPR 0.68-0.94, AUC 0.93-0.94）基于 uniform injection，可能高估真实场景。\n- Difficulty-dependent injection (ΔTPR=0.41 vs uniform 0.51) 在 Appendix B，未在主文充分呈现。\n\n**N3** [critical] 与 Growing Pains (Habba et al., 2026) 的差异化不充分\n- Growing Pains 的 anchor item selection 本质上包含 DIF 筛选。论文仅一句话区分，未深入讨论方法论层面差异。\n- \"to our knowledge, no prior work applies DIF to benchmark temporal comparability\" 可能不成立。\n\n### Should-Fix 问题\n\n**W1** MH 方法选择缺乏与替代方法的充分比较（SIBTEST、logistic regression DIF 等）\n**W2** 时间粒度选择（年度 cohort）未经论证\n**W3** Abstract 信息过载（≥8 个定量发现）\n**W4** Jaccard ≈ 0.206 被表述为 \"near-independent\" 不够精确\n**W5** DEFF 校正依赖 IRT 参数但模型拟合不佳\n\n### Overall: 3.5 (Borderline Conference)\n### Soundness: 4/5, Excitement: 3/5\n\n---\n\n请逐条回应上述问题。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] Mechanism-agnostic 定位与实验设计存在系统性矛盾\n- 论文反复声称采取 mechanism-agnostic 立场（Abstract: \"without implying degradation or attributing cause\"），但实验设计大量围绕 contamination 展开：Section 3.4 注入 contamination、Section 4.3 对比 web-overlap labels、Section 4.5 标题 \"Detection Power under Controlled Injection\"、Appendix B \"Mechanism Analysis\"。\n- 构成叙事上的自我矛盾：一方面声称不归因，另一方面整个验证体系建立在 contamination 假设之上。\n\n**N2** [critical] Semi-synthetic validation 仅覆盖 uniform injection，与真实 contamination 模式脱节\n- 主文的 detection power 数字（TPR 0.68-0.94, AUC 0.93-0.94）基于 uniform injection，可能高估真实场景。\n- Difficulty-dependent injection (ΔTPR=0.41 vs uniform 0.51) 在 Appendix B，未在主文充分呈现。\n\n**N3** [critical] 与 Growing Pains (Habba et al., 2026) 的差异化不充分\n- Growing Pains 的 anchor item selection 本质上包含 DIF 筛选。论文仅一句话区分，未深入讨论方法论层面差异。\n- \"to our knowledge, no prior work applies DIF to benchmark temporal comparability\" 可能不成立。\n\n### Should-Fix 问题\n\n**W1** MH 方法选择缺乏与替代方法的充分比较（SIBTEST、logistic regression DIF 等）\n**W2** 时间粒度选择（年度 cohort）未经论证\n**W3** Abstract 信息过载（≥8 个定量发现）\n**W4** Jaccard ≈ 0.206 被表述为 \"near-independent\" 不够精确\n**W5** DEFF 校正依赖 IRT 参数但模型拟合不佳\n\n### Overall: 3.5 (Borderline Conference)\n### Soundness: 4/5, Excitement: 3/5\n\n---\n\n请逐条回应上述问题。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1594 · 2026-05-23T11:32:25.296087+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15827
}
```

</details>

---


### Tool call

_source line 1595 · 2026-05-23T11:32:25.648050+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] DEFF 估计量选择的论证存在循环性，且对核心结论影响巨大\n- Simple-mean (C%=29.2%) vs weighted-mean (C%=13.5%) 差距 2.16×。\n- DEFF simulation (Table 12) 用观测到的 ICC-size 反相关模式构造模拟，再用模拟结果论证 simple-mean 更好——循环论证。\n- Weighted-mean DEFF (Kish, 1965) 是 survey sampling 标准方法，被降格为 \"conservative extreme\" 但未充分讨论何时 weighted-mean 更合适。\n- 如果 weighted-mean 正确，headline number 需下修为 13.5-29.2% 区间。\n\n**N2** [critical] 半合成验证框架的 ΔTPR \"upper bound\" 声称不严密\n- Uniform binary flipping 不是真正的上界：集中在特定难度范围的污染可能产生更强 DIF 信号。\n- Difficulty-dependent injection (ΔTPR=0.41 vs 0.51) 只验证一种非均匀模式。\n- 未讨论 partial memorization 会产生什么 DIF 信号。\n\n### Should-Fix 问题\n\n**W1** k>5 时 ΔFPR 保证退化的影响未充分量化（k=20 时 0.069 可能吃掉保守估计近一半）\n**W2** DIF-contamination 正交性有替代解释——DIF 可能根本不测量污染相关的东西\n**W3** ρ≈0.997 与 ±800 rank displacement 的张力需要随机移除基线对比\n**W4** 日历年群组定义的粒度和\"时序\"标签可能误导\n\n### Overall: 3.5 (Borderline Conference)\n### Soundness: 3.5/5, Excitement: 3.5/5\n\n---\n\n请逐条回应上述问题。",
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（引用具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] DEFF 估计量选择的论证存在循环性，且对核心结论影响巨大\n- Simple-mean (C%=29.2%) vs weighted-mean (C%=13.5%) 差距 2.16×。\n- DEFF simulation (Table 12) 用观测到的 ICC-size 反相关模式构造模拟，再用模拟结果论证 simple-mean 更好——循环论证。\n- Weighted-mean DEFF (Kish, 1965) 是 survey sampling 标准方法，被降格为 \"conservative extreme\" 但未充分讨论何时 weighted-mean 更合适。\n- 如果 weighted-mean 正确，headline number 需下修为 13.5-29.2% 区间。\n\n**N2** [critical] 半合成验证框架的 ΔTPR \"upper bound\" 声称不严密\n- Uniform binary flipping 不是真正的上界：集中在特定难度范围的污染可能产生更强 DIF 信号。\n- Difficulty-dependent injection (ΔTPR=0.41 vs 0.51) 只验证一种非均匀模式。\n- 未讨论 partial memorization 会产生什么 DIF 信号。\n\n### Should-Fix 问题\n\n**W1** k>5 时 ΔFPR 保证退化的影响未充分量化（k=20 时 0.069 可能吃掉保守估计近一半）\n**W2** DIF-contamination 正交性有替代解释——DIF 可能根本不测量污染相关的东西\n**W3** ρ≈0.997 与 ±800 rank displacement 的张力需要随机移除基线对比\n**W4** 日历年群组定义的粒度和\"时序\"标签可能误导\n\n### Overall: 3.5 (Borderline Conference)\n### Soundness: 3.5/5, Excitement: 3.5/5\n\n---\n\n请逐条回应上述问题。",
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1596 · 2026-05-23T11:32:27.060902+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 1597 · 2026-05-23T11:32:35.684027+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 1598 · 2026-05-23T11:32:38.315941+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5（Borderline Conference），Soundness 4/5，Excitement 3/5。

**三个 Must-Fix 问题**：
1. Mechanism-agnostic 定位与实验设计（大量围绕 contamination）存在系统性矛盾
2. Semi-synthetic validation 仅覆盖 uniform injection，高估了真实场景下的检测能力
3. 与 Growing Pains 的差异化不够清晰，novelty claim 需要更精确 scoping

**五个 Should-Fix 问题**：MH 方法选择理由不足、时间粒度未论证、Abstract 信息过载、"near-independent" 措辞不精确、DEFF 校正依赖拟合不佳的 IRT 参数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1599 · 2026-05-23T11:32:44.290215+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 155

## Round 155

2 recorded events


### User

_source line 1600 · 2026-05-23T11:33:52.469463+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: Mechanism-agnostic 定位与实验设计的"系统性矛盾"**

R2 的观察有一定表面合理性，但将其定性为"系统性矛盾"过重。论文的逻辑结构是：

1. **核心 DIF 分析本身是 mechanism-agnostic 的**：MH-DIF 仅测试"题目在两个群组间的功能是否不同"，不假设任何特定机制。§3.2 的定义、§4.2 的时序 DIF 结果、§4.4 的结构分析——这些核心结果完全不依赖于 contamination 假设。

2. **Semi-synthetic injection 使用 contamination 作为验证工具，而非作为理论前提**：任何检测方法都需要 ground truth 来校准检测能力。Contamination injection 提供了一个可控的、有明确 ground truth 的测试环境。论文在 §3.4 明确说明"To evaluate whether MH-DIF can detect differential contamination *when it is present*"——这是验证条件句，不是因果归因。

3. **§4.3 的正交性分析恰恰支持 mechanism-agnostic 立场**：如果论文的叙事建立在 contamination 假设之上，那么与 web-overlap 标签的正交性（enrichment≈1.0）将是负面结果。但论文将其解读为正面发现——DIF 和 contamination labels 是"complementary diagnostic dimensions"——这正说明 DIF 不预设 contamination 作为唯一或主要机制。

4. **Appendix B "Mechanism Analysis"** 标题确实可能引起误解，但内容是 *exclusion arguments*（排除能力混淆、domain-level improvement、item quality defects 等替代解释），这是标准的科学推理，不构成因果归因。

真正的问题不在于"矛盾"，而在于 **叙事框架需要更清晰**：论文应更明确地区分"DIF 作为诊断工具"和"contamination 作为验证手段"。但这是 framing 问题，不是方法论缺陷。

---

**[AGREE] R2-N2: Semi-synthetic validation 的生态效度有限**

同意。我在自己的审稿意见 N2 中提出了几乎完全一致的关切。补充两点：

1. 论文确实在 Appendix B 提供了 difficulty-dependent injection（ΔTPR=0.41 vs uniform 0.51），但这一更接近现实的结果被放在附录中，主文的检测能力数字（TPR 0.68-0.94）基于 uniform injection，可能给读者造成过于乐观的印象。

2. 更重要的是，如我在 N2 中指出的，"upper bound"声称缺乏严格论证——存在特定注入模式（如集中在中等难度题目）可能产生比 uniform 更强 DIF 信号的情况。

建议作者将 difficulty-dependent injection 的结果提升到主文，并将 ΔTPR 标记为"reference point"而非"upper bound"。

---

**[REBUT] R2-N3: 与 Growing Pains 的差异化不充分**

R2 声称"Growing Pains 的 anchor item selection 本质上包含 DIF 筛选"且论文的 novelty claim "可能不成立"，但这混淆了两个层面的区别：

1. **方法论差异**：Growing Pains 使用 IRT fixed-parameter calibration（FPC），通过参数化模型（2PL/3PL）检测参数漂移。MH-DIF 是非参数方法，不假设特定 IRT 模型形式。论文在 Appendix A 明确报告"MMLU response matrix shows poor fit to a unidimensional 2PL model"——这意味着 FPC 的参数化假设在 MMLU 上可能不成立，而 MH-DIF 不受此限制。这是实质性的方法论差异，不是表面区分。

2. **诊断 vs 矫正的功能定位**：Growing Pains 的目标是 *equating*（跨时间的分数可比性校正），其 anchor item selection 是达成 equating 的工具性步骤。本文的目标是 *diagnosis*（识别哪些题目、多大比例、什么模式出现功能差异），并提供定量严重程度分级（ETS A/B/C）。论文在 §2 Related Work 中明确指出："While Growing Pains prescribes how to equate scores after instability is detected, our work diagnoses *which* items exhibit instability and quantifies its magnitude."

3. **"no prior work applies DIF to benchmark temporal comparability"**：这里的关键词是"DIF"——一个有明确定义的心理测量学程序（MH 统计量 + ETS 分类）。FPC 中的参数漂移检测虽然在广义上也检测"项目不稳定性"，但它不是 DIF 分析。这个 novelty claim 在严格意义上是成立的。

建议作者在正文中补充 1-2 句话明确对比方法论差异（非参数 vs 参数化、诊断 vs 矫正），但不需要大幅改写。

---

### Should-Fix 问题

**[REBUT] R2-W1: MH 方法选择缺乏与替代方法的比较**

论文实际上已提供了多个层面的方法比较：

- §4.4 使用 logistic regression DIF 检测非均匀 DIF，发现额外 17.7% 的题目（union 47%）——这既是对 MH 的补充，也证明了 MH 的保守性（仅检测 uniform DIF）。
- §4.4 的 IRT θ-conditioning 作为 sensitivity check（r(θ, total score)=0.9986, C%=0.312），验证了 total-score matching 的充分性。
- §2 Related Work 系统列举了 SIBTEST、Lord's χ²、Raju area method 等替代方法。

MH 是教育测量中使用最广泛的 DIF 方法（论文引用了 Clauser and Mazor 1998 的综述），其选择不需要额外论证。大规模比较所有 DIF 方法超出了本文的范围——本文的贡献是将 DIF 引入 LLM 评测，而非开发新的 DIF 方法。

---

**[AGREE] R2-W2: 时间粒度选择未经论证**

同意，我在 W4 中提出了类似关切。补充：Appendix E 的半年度分析（C%=34.4%）和 Appendix P 的 base-only/instruct-only 分析都提供了有价值的粒度信息，但正文未充分整合。建议作者在 §3.3 或 §5.1 中增加一段讨论 release date vs training cutoff 的混淆以及粒度选择的依据。

---

**[AGREE] R2-W3: Abstract 信息过载**

同意这是一个 presentation issue。Abstract 确实压缩了过多定量发现（C% 范围、DEFF 校正值、Jaccard、φ、ρ、pp 偏移等）。建议精简到 4-5 个核心数字。但这不影响技术评估。

---

**[REBUT] R2-W4: Jaccard≈0.206 作为 "near-independent" 不精确**

R2 的关切源于对 Jaccard 指标的误读。论文的"near-independence"声称并非仅基于 Jaccard，而是基于一组互补的统计量：

- **φ = 0.012**：Phi 系数是二元变量间关联性的标准度量，0.012 在任何标准下都是 negligible association。
- **OR = 1.05 [0.96, 1.15]**：95% CI 包含 1.0，无法拒绝独立性。
- **Permutation null for Jaccard: [0.203, 0.222]**，观测值 0.206 落在 null distribution 内（§4.3: "within permutation null"）。
- **p = 0.88**：关联性检验的 p 值远高于任何显著性阈值。

Jaccard=0.206 反映的是两组标记各自覆盖率的 base rate，不是关联强度。给定 ~31% 的 DIF-C rate 和 ~X% 的 web-contamination rate，即使两个标记完全独立，Jaccard 也不会为零。论文提供的 permutation null 正是控制了这一点。"Near-independent"在 φ=0.012 + OR CI 包含 1.0 + permutation test 的支持下是充分合理的。

---

**[REBUT] R2-W5: DEFF 校正依赖 IRT 参数但模型拟合不佳**

这是一个事实性错误。DEFF 校正与 IRT 模型参数无关：

- DEFF 使用的是 **ICC（intra-class correlation）**，即组内相关系数——这是一个从原始响应矩阵直接计算的非参数统计量，与 IRT 的 Item Characteristic Curve (ICC) 是完全不同的概念。
- §D (Appendix DEFF) 定义：DEFF_i = 1 + (m̄ - 1) · ICC_i，其中 ICC_i 是 item i 在 30 个家族上的 one-way random-effects ICC。
- 论文在 Limitations 中明确指出："IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric."

R2 可能混淆了 ICC (intra-class correlation) 和 ICC (Item Characteristic Curve)。DEFF 校正完全是非参数的，不受 IRT 模型拟合质量的影响。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1601 · 2026-05-23T11:34:07.529120+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 156

## Round 156

2 recorded events


### User

_source line 1602 · 2026-05-23T11:34:10.149805+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。

总结：
- **R2-N1**（mechanism-agnostic 矛盾）：[REBUT]——contamination 是验证工具而非理论前提，正交性发现恰好支持 mechanism-agnostic 立场，但 framing 可更清晰
- **R2-N2**（semi-synthetic 生态效度）：[AGREE]——与我自己的 N2 一致
- **R2-N3**（Growing Pains 差异化）：[REBUT]——非参数 vs 参数化、诊断 vs 矫正是实质性差异，novelty claim 成立
- **R2-W1**（方法比较）：[REBUT]——论文已含 logistic regression DIF 和 θ-conditioning
- **R2-W2**（时间粒度）：[AGREE]——与我的 W4 一致
- **R2-W3**（Abstract 过载）：[AGREE]——presentation issue
- **R2-W4**（Jaccard 解读）：[REBUT]——φ=0.012 + OR CI 含 1.0 + permutation test 充分支持 near-independence
- **R2-W5**（DEFF 依赖 IRT）：[REBUT]——事实性错误，ICC (intra-class correlation) ≠ ICC (Item Characteristic Curve)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1603 · 2026-05-23T11:34:14.269333+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 157

## Round 157

10 recorded events


### User

_source line 1604 · 2026-05-23T11:34:38.611287+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: DEFF 估计量选择的循环性与对 headline number 的影响**

同意这是一个影响接收决定的重要问题。

理由：
1. **2.16× 的差距是实质性的**。Simple-mean C% ≈ 29.2% vs weighted-mean C% ≈ 13.5%——论文选择 simple-mean 作为 headline number，但如果 weighted-mean 更合适，核心发现的量级需下修近一半。论文在 Appendix L (Table 12) 用模拟论证 simple-mean 更优，但模拟构造基于观测到的 ICC-size 反相关模式（Appendix I），确实存在 R1 指出的 "用结论构造前提" 的嫌疑。
2. **补充 R1 的论点**：即使接受 ICC-size 反相关是真实的经验事实（非循环产物），论文也未讨论 weighted-mean DEFF 在什么条件下更合适。Kish (1965) 的 weighted-mean 是 cluster sampling 标准方法，在 equal-ICC 假设成立时无偏。论文应至少讨论：如果 ICC-size 反相关是 sampling artifact（如大 family 内部 heterogeneity 更大导致 ICC 偏低），weighted-mean 可能才是正确的校正。
3. **建议**：论文应同时报告两个估计量的结果范围（如 "C% 在 13.5%–29.2% 之间，取决于 family-size 校正方法"），而非单方面选择 simple-mean。这样读者可以自行判断。

**[AGREE] R1-N2: Semi-synthetic ΔTPR "upper bound" 声称不严密**

完全同意，且这与我自己的 N2 一致。

理由：
1. **Uniform flipping 不是理论上界**：R1 正确指出，如果 contamination 集中在特定难度范围（如接近 ability threshold 的 items），DIF 信号可能被放大而非减弱。MH 检验的 power 取决于 item difficulty 与 ability distribution 的交互，uniform flipping 实际上在高/低难度 items 上浪费了 "污染预算"（这些 items 的 baseline 正确率已经接近 0 或 1，翻转影响小），而集中在 medium-difficulty items 可能产生更强的 DIF。
2. **Partial memorization 的遗漏**：R1 提出的 partial memorization 场景很重要——模型可能 "部分记住" 题目（如记住关键词但不完全记住答案），这会产生与 binary flipping 完全不同的 DIF 模式（可能表现为 discrimination parameter 变化而非 difficulty shift）。论文未讨论这种场景。
3. **与我的 N2 的互补**：我的 N2 侧重于 "uniform injection 高估 detection power"，R1 的 N2 更进一步质疑 "upper bound" 标签本身。两个角度互补，共同说明 semi-synthetic 验证的局限性比论文所承认的更大。

---

### Should-Fix 问题

**[AGREE] R1-W1: k>5 时 ΔFPR 退化需要更充分量化**

同意。

理由：Table 7 (Appendix C) 显示 k=20 时 ΔFPR = 0.069，k=10 时 ΔFPR = 0.047。论文在 Abstract 中声称 "cross-subject matching with formal FPR guarantee: ΔFPR = 0"，但这仅在 single-subject contamination (k=1) 下严格成立。对于 multi-domain contamination（k > 5），ΔFPR 可以达到 ~7%，这在 weighted-mean C% ≈ 13.5% 的语境下确实非 trivial（约占一半）。建议 abstract 中的 ΔFPR = 0 声称应附加限定条件，如 "ΔFPR = 0 under single-subject contamination; ≤0.02 for k ≤ 5"。

**[AGREE] R1-W2: DIF-contamination 正交性存在替代解释**

同意这是一个需要讨论的替代假设。

理由：论文将 Jaccard ≈ 0.206 解读为 "DIF 捕获了 contamination 之外的东西"（即 DIF 是一个更广的工具，contamination 只是其中一个来源）。但 R1 提出的替代解释同样合理：DIF 可能测量的是与 contamination 基本无关的东西（如 training methodology shifts、architecture-specific biases），那么低 Jaccard 并不 surprising，只是说明两个指标测量不同的构念。这两种解释对论文定位有不同含义——前者支持 "DIF 是比 contamination detection 更通用的工具"，后者则意味着 "DIF 和 contamination detection 是平行的、不可替代的"。论文应在 Discussion 中明确讨论这两种解释。

补充我自己的观点：Appendix B (Mechanism Analysis) 中 logistic regression 发现 model-type interaction 是 DIF 的独立 predictor (OR = 4.75, p < 10^−188)，这部分支持 R1 的替代解释——DIF 确实在很大程度上捕获了 architecture/training methodology 差异而非 contamination。

**[REBUT] R1-W3: ρ ≈ 0.997 与 ≥500 rank displacement 的张力**

部分反驳。论文已提供随机移除基线，但主文对张力的解释不足。

理由：
1. **Figure 6 (Appendix K) 已包含随机基线**：论文在 Figure 6 中明确对比了 DIF-ordered removal 和 random removal（"blue band = mean ± 1 SD; 20 seeds"），显示 DIF-ordered removal 的 ρ 下降速度显著快于随机移除。这直接回应了 R1 要求的随机移除基线。
2. **ρ = 0.997 与 ≥500 displacement 在统计上并不矛盾**：N = 5,227 模型时，ρ = 0.997 允许部分模型有较大位移，只要大多数模型位移很小。≥500 位移约为总排名范围的 ~10%，在密集排名的中间区域（模型间 accuracy 差异极小），微小的分数变化就能产生大的 rank 位移。
3. **但 R1 有一个合理的 concern**：论文未在主文中解释这种"大 ρ + 大 displacement"的共存机制。读者可能误以为这是矛盾的。建议在 Section 4.6 增加 1-2 句解释（如 "The high ρ reflects stability for the majority; large displacements concentrate among closely-ranked models in the middle of the distribution"）。

结论：R1 的 concern 在数据层面已被 Figure 6 回应，但在叙事层面论文确实应改进。建议降级为 minor issue。

**[AGREE] R1-W4: 日历年 cohort 粒度与 "时序" 标签**

同意，与我的 W2 一致。

理由：年度 cohort 是一个粗粒度的选择，论文未论证为何此粒度最合适。Appendix E 的半年度分析（C% = 34.4%）暗示更细粒度可能揭示不同模式。此外，R1 正确指出 "temporal" 标签可能误导——日历年分组不纯粹反映时间效应，还混淆了 training data cutoff、model architecture evolution、RLHF 方法变化等因素。论文应在 Section 3.3 明确讨论这一 confound。

---

### 对 R1 整体评分的评价

R1 给出 Soundness 3.5/5、Excitement 3.5/5、Overall 3.5。我的评分为 Soundness 4/5、Excitement 3/5、Overall 3.5。

**分歧点**：
- Soundness：R1 因 DEFF 循环性和 semi-synthetic upper bound 给 3.5，我给 4。我认为 MH-DIF 方法本身的应用是 sound 的，DEFF 和 semi-synthetic 是附属分析而非核心方法。但 R1 的论点有说服力——如果 headline number 依赖 DEFF 选择，这确实影响 soundness。若要调和，我倾向 3.5-4 之间。
- Excitement：R1 给 3.5 比我高（我给 3）。我认为核心贡献主要是应用层面（将现有心理测量方法移植到 LLM 评估），方法论创新有限。但 R1 可能更看重实证发现本身的价值。

**一致点**：Overall 3.5 (Borderline Conference)——我们都认为论文方法论扎实、实证充分、有实际影响力，但新颖性和叙事连贯性存在可改进空间。



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1605 · 2026-05-23T11:35:19.494060+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1606 · 2026-05-23T11:35:19.544902+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T11:24:50.905305+00:00\", \"completed_at\": \"2026-05-23T11:27:32.490984+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本（Method 章节），无 figure/table/diagram 穿插。页 4 的两个公式部分缓解，但审稿人在此区间可能失去视觉锚点。考虑将 Method 中的 pipeline 或 DIF 分类标准以小型示意图或流程图可视化。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-5\", \"message\": \"Display item 分布前重后轻倒置：前 5 页仅 Figure 1，页 6-8 集中 4 个 display item。审稿人翻过 3 页纯文本后才看到第一个数据表格。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 y 轴标签 \\\"True Positive Rate (TPR)\\\" 字号偏小但仍可读。legend 字号约为正文 70%，处于下限。\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 6（六面板 benchmark 对比图）面板内 axis label 和 legend 文字较小，打印时可能接近可读性下限。建议略增字号或减少面板数。\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 5 标注 N=33 小样本，caption 已注明\\\"results should be interpreted cautiously\\\"，处理得当。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，格式整洁。但表中 \\\"Dagger †\\\" 符号含义需读者参照 caption 才能理解——caption 已解释，合格。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 格式良好，数值精度一致（2 位小数），最优值加粗标注。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 跨 6 个 benchmark 的对比表，列数适中（~8 列），使用全宽排版合理。精度统一，关键数值加粗。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 颜色方案使用蓝/橙/绿区分不同 ICC 曲线，色盲友好，线型也有区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 8-9\", \"message\": \"Limitations 段落简短（约 8 行），覆盖 3 个关键局限点，符合 EMNLP 要求。References 从页 9 开始，约 2.5 页，格式统一，未见 [?] 未解析引用。\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-23T11:35:19.645897+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1608 · 2026-05-23T11:35:19.646254+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1609 · 2026-05-23T11:36:59.160045+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 17 new issues ===\n\n  - id: \"R17-N1\"\n    summary: \"DEFF 估计量选择论证存在循环性——simulation 用观测 ICC-size 模式构造前提，再论证 simple-mean 更优\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%，差距 2.16×。论文推荐 simple-mean 为 primary estimate，但 DEFF simulation (Table 12) 的模拟场景本身使用观测到的 ICC-size 反相关模式——循环论证。建议改为区间表述 (13.5-29.2%) 或打破循环性。\"\n    action_items:\n      - round: 17\n        action: \"改为区间表述 '13.5-29.2%, with convergent evidence supporting the upper range'，或补充独立论证打破循环性\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-N2\"\n    summary: \"Semi-synthetic ΔTPR 'upper bound' 声称不严密——uniform flipping 非理论上界，difficulty-dependent 结果应进主文\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (N2)，R2 独立提出 (N2) 并 AGREE。集中在 medium-difficulty items 的污染可能产生比 uniform 更强的 DIF 信号，故 uniform 非真正上界。Difficulty-dependent injection (ΔTPR=0.41) 仅在 Appendix B，主文数字 (TPR 0.68-0.94) 基于 uniform injection 可能过于乐观。\"\n    action_items:\n      - round: 17\n        action: \"将 'upper bound' 改为 'reference point under stylized uniform injection'；将 difficulty-dependent injection 结果提升到主文 §4.5 并列报告\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W1\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力需要更清晰的 framing\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 提出为 Must-Fix (N1)，R1 REBUT——contamination 是验证工具而非理论前提，正交性发现支持 mechanism-agnostic。R2 未再反驳。降级为 Should-Fix：framing 需更清晰区分'DIF 作为诊断工具'和'contamination 作为验证手段'。\"\n    action_items:\n      - round: 17\n        action: \"在 §3.4 或 §5 中明确：contamination injection 是验证 DIF 检测能力的 case study，DIF 本身是 mechanism-agnostic 的诊断工具\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"与 Growing Pains 的差异化需补充 1-2 句方法论对比（非参数 vs 参数化、诊断 vs 矫正）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 提出为 Must-Fix (N3)，R1 REBUT——MH-DIF 非参数 vs FPC 参数化、诊断 vs equating 是实质性差异。R2 未再反驳。降级为 Should-Fix：§2 已有一句区分，建议补充方法论差异（MH 非参数不受 2PL misfit 影响 vs FPC 依赖参数化模型）。\"\n    action_items:\n      - round: 17\n        action: \"§2 Growing Pains 段落补充 1-2 句：方法论差异（非参数 vs 参数化）、功能定位（诊断+量化 vs equating）、ETS severity classification\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W3\"\n    summary: \"k>5 时 ΔFPR 保证退化的实际影响未充分量化，Abstract 中 ΔFPR=0 需附加限定\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W1)，R2 AGREE。k=20 时 ΔFPR=0.069 在 weighted-mean C%=13.5% 语境下占约一半。Abstract 'ΔFPR=0' 需限定条件。建议提供现实中 k 的合理范围论证。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 中 ΔFPR=0 附加条件 (k≤5)；§4.5 增加 ΔFPR 对 C% 估计的敏感性分析\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W4\"\n    summary: \"DIF-contamination 正交性需讨论替代解释：DIF 可能主要测量 capability evolution 而非污染\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W2)，R2 AGREE 并补充 Appendix B model-type interaction (OR=4.75) 证据。两种解释：(1) DIF 是比 contamination detection 更通用的工具；(2) DIF 和 contamination detection 测量不同构念。论文应在 Discussion 明确讨论。\"\n    action_items:\n      - round: 17\n        action: \"§5.1 或 §5.2 增加 1 段讨论正交性的两种解释及其含义\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W5\"\n    summary: \"时间粒度选择（年度 cohort）未经论证，release date vs training cutoff 混淆未充分讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W4)，R2 独立提出 (W2)，均 AGREE。年度粒度是粗粒度选择，Appendix E 半年度 C%=34.4% 和 Appendix O-P base-only/instruct-only 分析提供有价值信息但正文未充分整合。\"\n    action_items:\n      - round: 17\n        action: \"§3.3 或 §5.1 增加 temporal granularity 讨论，包括 release date vs training cutoff 的 confound\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W6\"\n    summary: \"Abstract 信息过载（≥8 个定量发现），建议精简到 4-5 个核心数字\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 提出 (W3)，R1 AGREE。Abstract 包含 C% 范围、DEFF 校正值、Jaccard、ρ、pp 偏移等过多定量发现。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 精简到 4-5 个核心数字，其余移至 Introduction\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-M1\"\n    summary: \"ρ≈0.997 与 ±800 rank displacement 共存的机制需在主文解释\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W3)，R2 partial REBUT——Figure 6 已含随机基线，但主文叙事需改进。降级为 info。建议 §4.6 增加 1-2 句解释。\"\n    action_items:\n      - round: 17\n        action: \"§4.6 增加 1-2 句解释大 ρ + 大 displacement 共存机制\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 16 issues (all resolved) ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未重新提出。§4.1 的 empirical null (P99=1.45) 被 R17 Reviewers 接受为充分校准。\"\n    resolution: \"§4.1 插入 empirical null (P99=1.45 ≈ ETS C 1.5). Reviewer 验证 PASS.\"\n    resolution_round: 17\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 声称过度定位\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未重新提出。3→2 contributions 结构被接受。\"\n    resolution: \"3→2 contributions. Reviewer 验证 PASS.\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 校正两种估计量差异 2× 削弱 headline 定量精度\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 以新形式复发为 R17-N1（循环性论证）。推荐 simple-mean 的论证被质疑。\"\n    resolution: \"§4.1 推荐 simple-mean 为 primary estimate. R17 指出循环性，升级为 R17-N1.\"\n    resolution_round: 17\n\n  - id: \"R16-W2\"\n    summary: \"§5.2 审计协议措辞超出方法能力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"§5.2 含 'DIF alone cannot determine causation'. R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Discussion 缺乏深层 insight\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§5.1 三个 LLM-vs-educational 区分已加入。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 以新形式复发为 R17-W6。当前约 8 个数字，仍偏多。\"\n    resolution: \"R16 精简到约 7-8 个数字。R17 指出仍偏多，复发为 R17-W6。\"\n    resolution_round: 17\n\n  - id: \"R16-W5\"\n    summary: \"主文超页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"0 \\\\enlargethispage. Main text strict 8 页. R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-W6\"\n    summary: \"Semi-synthetic ΔTPR 应标为检测力上界\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 以新形式复发为 R17-N2。'upper bound' 声称本身被质疑——uniform flipping 不是理论上界。\"\n    resolution: \"§4.5 标为 'detection-power upper bounds'. R17 指出 upper bound 不严密，复发为 R17-N2。\"\n    resolution_round: 17\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"§1 parenthetical 定义。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-M2\"\n    summary: \"有效 N=1,887 vs 总 N=5,227 澄清\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§3.2 已修正。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-M3\"\n    summary: \"遗漏近期相关工作\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"4 篇新引用已加入 §2。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-DATA1\"\n    summary: \"论文 random-split baseline 0.18% 来自单次运行\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"全文 12 处修正 0.18→0.62。R17 未重新提出。\"\n    resolution_round: 17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 17 new issues ===\n\n  - id: \"R17-N1\"\n    summary: \"DEFF 估计量选择论证存在循环性——simulation 用观测 ICC-size 模式构造前提，再论证 simple-mean 更优\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%，差距 2.16×。论文推荐 simple-mean 为 primary estimate，但 DEFF simulation (Table 12) 的模拟场景本身使用观测到的 ICC-size 反相关模式——循环论证。建议改为区间表述 (13.5-29.2%) 或打破循环性。\"\n    action_items:\n      - round: 17\n        action: \"改为区间表述 '13.5-29.2%, with convergent evidence supporting the upper range'，或补充独立论证打破循环性\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-N2\"\n    summary: \"Semi-synthetic ΔTPR 'upper bound' 声称不严密——uniform flipping 非理论上界，difficulty-dependent 结果应进主文\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (N2)，R2 独立提出 (N2) 并 AGREE。集中在 medium-difficulty items 的污染可能产生比 uniform 更强的 DIF 信号，故 uniform 非真正上界。Difficulty-dependent injection (ΔTPR=0.41) 仅在 Appendix B，主文数字 (TPR 0.68-0.94) 基于 uniform injection 可能过于乐观。\"\n    action_items:\n      - round: 17\n        action: \"将 'upper bound' 改为 'reference point under stylized uniform injection'；将 difficulty-dependent injection 结果提升到主文 §4.5 并列报告\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W1\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力需要更清晰的 framing\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 提出为 Must-Fix (N1)，R1 REBUT——contamination 是验证工具而非理论前提，正交性发现支持 mechanism-agnostic。R2 未再反驳。降级为 Should-Fix：framing 需更清晰区分'DIF 作为诊断工具'和'contamination 作为验证手段'。\"\n    action_items:\n      - round: 17\n        action: \"在 §3.4 或 §5 中明确：contamination injection 是验证 DIF 检测能力的 case study，DIF 本身是 mechanism-agnostic 的诊断工具\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"与 Growing Pains 的差异化需补充 1-2 句方法论对比（非参数 vs 参数化、诊断 vs 矫正）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 提出为 Must-Fix (N3)，R1 REBUT——MH-DIF 非参数 vs FPC 参数化、诊断 vs equating 是实质性差异。R2 未再反驳。降级为 Should-Fix：§2 已有一句区分，建议补充方法论差异（MH 非参数不受 2PL misfit 影响 vs FPC 依赖参数化模型）。\"\n    action_items:\n      - round: 17\n        action: \"§2 Growing Pains 段落补充 1-2 句：方法论差异（非参数 vs 参数化）、功能定位（诊断+量化 vs equating）、ETS severity classification\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W3\"\n    summary: \"k>5 时 ΔFPR 保证退化的实际影响未充分量化，Abstract 中 ΔFPR=0 需附加限定\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W1)，R2 AGREE。k=20 时 ΔFPR=0.069 在 weighted-mean C%=13.5% 语境下占约一半。Abstract 'ΔFPR=0' 需限定条件。建议提供现实中 k 的合理范围论证。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 中 ΔFPR=0 附加条件 (k≤5)；§4.5 增加 ΔFPR 对 C% 估计的敏感性分析\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W4\"\n    summary: \"DIF-contamination 正交性需讨论替代解释：DIF 可能主要测量 capability evolution 而非污染\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W2)，R2 AGREE 并补充 Appendix B model-type interaction (OR=4.75) 证据。两种解释：(1) DIF 是比 contamination detection 更通用的工具；(2) DIF 和 contamination detection 测量不同构念。论文应在 Discussion 明确讨论。\"\n    action_items:\n      - round: 17\n        action: \"§5.1 或 §5.2 增加 1 段讨论正交性的两种解释及其含义\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W5\"\n    summary: \"时间粒度选择（年度 cohort）未经论证，release date vs training cutoff 混淆未充分讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W4)，R2 独立提出 (W2)，均 AGREE。年度粒度是粗粒度选择，Appendix E 半年度 C%=34.4% 和 Appendix O-P base-only/instruct-only 分析提供有价值信息但正文未充分整合。\"\n    action_items:\n      - round: 17\n        action: \"§3.3 或 §5.1 增加 temporal granularity 讨论，包括 release date vs training cutoff 的 confound\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W6\"\n    summary: \"Abstract 信息过载（≥8 个定量发现），建议精简到 4-5 个核心数字\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R2 提出 (W3)，R1 AGREE。Abstract 包含 C% 范围、DEFF 校正值、Jaccard、ρ、pp 偏移等过多定量发现。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 精简到 4-5 个核心数字，其余移至 Introduction\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-M1\"\n    summary: \"ρ≈0.997 与 ±800 rank displacement 共存的机制需在主文解释\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出 (W3)，R2 partial REBUT——Figure 6 已含随机基线，但主文叙事需改进。降级为 info。建议 §4.6 增加 1-2 句解释。\"\n    action_items:\n      - round: 17\n        action: \"§4.6 增加 1-2 句解释大 ρ + 大 displacement 共存机制\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 16 issues (all resolved) ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值（|Δ_MH| ≥ 1.5）从人类考生直接移植到 LLM 缺乏领域内校准\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未重新提出。§4.1 的 empirical null (P99=1.45) 被 R17 Reviewers 接受为充分校准。\"\n    resolution: \"§4.1 插入 empirical null (P99=1.45 ≈ ETS C 1.5). Reviewer 验证 PASS.\"\n    resolution_round: 17\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 声称过度定位\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未重新提出。3→2 contributions 结构被接受。\"\n    resolution: \"3→2 contributions. Reviewer 验证 PASS.\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 校正两种估计量差异 2× 削弱 headline 定量精度\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 以新形式复发为 R17-N1（循环性论证）。推荐 simple-mean 的论证被质疑。\"\n    resolution: \"§4.1 推荐 simple-mean 为 primary estimate. R17 指出循环性，升级为 R17-N1.\"\n    resolution_round: 17\n\n  - id: \"R16-W2\"\n    summary: \"§5.2 审计协议措辞超出方法能力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"§5.2 含 'DIF alone cannot determine causation'. R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Discussion 缺乏深层 insight\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§5.1 三个 LLM-vs-educational 区分已加入。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 以新形式复发为 R17-W6。当前约 8 个数字，仍偏多。\"\n    resolution: \"R16 精简到约 7-8 个数字。R17 指出仍偏多，复发为 R17-W6。\"\n    resolution_round: 17\n\n  - id: \"R16-W5\"\n    summary: \"主文超页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"0 \\\\enlargethispage. Main text strict 8 页. R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-W6\"\n    summary: \"Semi-synthetic ΔTPR 应标为检测力上界\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R17 以新形式复发为 R17-N2。'upper bound' 声称本身被质疑——uniform flipping 不是理论上界。\"\n    resolution: \"§4.5 标为 'detection-power upper bounds'. R17 指出 upper bound 不严密，复发为 R17-N2。\"\n    resolution_round: 17\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"§1 parenthetical 定义。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-M2\"\n    summary: \"有效 N=1,887 vs 总 N=5,227 澄清\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§3.2 已修正。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-M3\"\n    summary: \"遗漏近期相关工作\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"4 篇新引用已加入 §2。R17 未重新提出。\"\n    resolution_round: 17\n\n  - id: \"R16-DATA1\"\n    summary: \"论文 random-split baseline 0.18% 来自单次运行\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"全文 12 处修正 0.18→0.62。R17 未重新提出。\"\n    resolution_round: 17"
  }
}
```

</details>

---


### Tool result

_source line 1610 · 2026-05-23T11:36:59.261171+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 9665}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1611 · 2026-05-23T11:39:40.543051+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 17 审稿报告：Temporal Score Incomparability in LLM Benchmarks\n\n**论文**: Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 Long Paper (via ARR)\n**Reviewers**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作）\n**模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析迁移到 LLM 基准评测领域，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现 2023 与 2024 模型群组之间约 27–29% 的题目存在显著时序 DIF（保守下界 13.5%），远超随机基线（0.62%）。论文提出跨学科匹配（cross-subject matching）策略并给出 ΔFPR=0 的形式化保证（k≤5 条件下），通过半合成注入框架验证检测能力，并在六个 METABENCH 基准上复现。核心发现是 DIF 标记与 web-overlap 污染标签近乎正交（φ=0.012），base 与 instruct 模型呈现相反的 DIF 方向模式（χ²=562.7）。\n\n---\n\n## Strengths\n\n1. **跨学科方法创新**：首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型、6 个 benchmark），填补了教育测量和 LLM 评测之间的方法论空白。\n\n2. **实验控制的深度与广度**：随机分割基线、能力匹配（NN matching, Cohen's d=-0.17）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control（Δ=1.08pp）、跨基准复现——每一个潜在混淆变量都被系统检验。这种控制水平在 LLM 评测领域罕见。[R1/R2 共识]\n\n3. **Cross-subject matching 的创新**：将 purified subtest matching 改造为 LLM 多学科设置的 cross-subject matching，提供 ΔFPR=0 的形式化保证（k≤5），是对方法论的实质性贡献。[R1/R2 共识]\n\n4. **DIF ≠ contamination 的实证发现**：DIF 与 web-overlap 标签的近乎独立性（φ=0.012, OR=1.05 [0.96,1.15], permutation test p=0.88）是非平凡的经验发现，表明全局污染检测和项目功能差异是不同的维度。[R1/R2 共识]\n\n5. **Base/instruct 方向反转**：χ²=562.7 提供了强有力的机制分离证据，表明 DIF 反映的是结构化的项目级变化而非均匀群组效应。[R1 Strength]\n\n6. **详实的附录体系**：Appendix A-L 提供了 sensitivity analysis、mechanism analysis、structural analysis、DEFF estimation、uncertainty quantification 等全面补充分析，增强了可重复性。[R2 Strength]\n\n---\n\n## Weaknesses\n\n### Must-Fix（2 项，Reviewer 共识）\n\n**N1 [critical]** DEFF 估计量选择的论证存在循环性，对核心结论影响巨大\n- Simple-mean DEFF（C%=29.2%）vs weighted-mean DEFF（C%=13.5%），差距 2.16×。论文推荐 simple-mean 为 primary estimate，理由是\"与 cluster bootstrap 和 DEFF simulation 收敛\"。但 DEFF simulation（Table 12）的模拟场景使用观测到的 ICC-size 反相关模式构造——用结论构造前提，循环论证。Weighted-mean DEFF（Kish, 1965）是 survey sampling 标准方法，被降格为\"conservative extreme\"但未讨论其适用条件。若 weighted-mean 正确，headline number 需下修近一半。\n- **建议**：(1) 采用区间表述（如\"13.5–29.2%, with convergent evidence supporting the upper range\"）而非推荐单一估计量；(2) 补充独立论证打破循环性；(3) 报告 weighted-mean DEFF 下的下游分析（排名影响、分数修正）。\n- **[R1 提出, R2 AGREE]**\n\n**N2 [critical]** Semi-synthetic ΔTPR \"upper bound\" 声称不严密\n- Uniform binary flipping 不是检测能力的理论上界：集中在 medium-difficulty items 的污染可能产生比 uniform 更强的 DIF 信号（MH power 取决于 item difficulty 与 ability distribution 的交互，uniform flipping 在高/低难度 items 上浪费\"污染预算\"）。Difficulty-dependent injection（ΔTPR=0.41 vs uniform 0.51）仅在 Appendix B，主文检测能力数字（TPR 0.68–0.94）基于 uniform injection 可能过于乐观。Partial memorization 场景（模型部分记住题目线索）会产生与 binary flipping 不同的 DIF 模式，未被讨论。\n- **建议**：(1) 将\"upper bound\"改为\"reference point under stylized uniform injection\"；(2) 将 difficulty-dependent injection 结果提升到主文 §4.5 并列报告；(3) 讨论 partial memorization 场景。\n- **[R1 提出 (N2), R2 独立提出 (N2), 完全共识]**\n\n### Should-Fix（6 项）\n\n**W1 [warning]** Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力\n- 论文声称 mechanism-agnostic 立场，但 §3.4（Semi-Synthetic Injection Framework）、§4.3（Ground Truth Mismatch）、§4.5（Detection Power under Controlled Injection）、Appendix B（Mechanism Analysis）大量围绕 contamination 展开。R1 指出 contamination 是\"验证工具而非理论前提\"、正交性发现支持 mechanism-agnostic 立场，该反驳有说服力，因此从 R2 的 Must-Fix 降级为 Should-Fix。但叙事框架确实需要更清晰地区分\"DIF 作为诊断工具\"和\"contamination 作为验证手段\"。\n- **建议**：§3.4 或 §5 中明确：contamination injection 是验证 DIF 检测能力的 case study，DIF 本身是 mechanism-agnostic 的诊断工具，可由多种原因引起。\n- **[R2 提出为 Must-Fix, R1 REBUT, 降级为 Should-Fix]**\n\n**W2 [warning]** 与 Growing Pains 的差异化需补充方法论对比\n- R2 认为\"to our knowledge, no prior work applies DIF to benchmark temporal comparability\"可能不成立。R1 反驳指出：(1) FPC 是参数化方法（依赖 2PL/3PL），MH-DIF 是非参数方法，且论文已报告 2PL fit poor for MMLU；(2) Growing Pains 目标是 equating，本文目标是 diagnosis + severity grading (ETS A/B/C)。R1 反驳有力，novelty claim 在严格意义上成立。但 §2 仅一句话区分，建议补充方法论差异。\n- **建议**：§2 Growing Pains 段落补充 1-2 句方法论对比。\n- **[R2 提出为 Must-Fix, R1 REBUT, 降级为 Should-Fix]**\n\n**W3 [warning]** k>5 时 ΔFPR 保证退化的实际影响未充分量化\n- k=20 时 ΔFPR=0.069，在 weighted-mean C%=13.5% 语境下占约一半。Abstract 中\"ΔFPR=0\"未附加限定条件。论文未论证现实中 k 的合理范围。\n- **建议**：(1) Abstract 中 ΔFPR=0 附加条件（k≤5）；(2) 从 web-overlap 标签分布推断跨学科污染的经验分布以约束 k；(3) 给出 ΔFPR 对 C% 估计的敏感性分析。\n- **[R1 提出, R2 AGREE]**\n\n**W4 [warning]** DIF-contamination 正交性需讨论替代解释\n- 低 Jaccard 有两种解释：(1) DIF 是比 contamination detection 更通用的工具（论文的解读）；(2) DIF 主要测量 capability evolution/training methodology shifts，与 contamination 基本无关。Appendix B model-type interaction (OR=4.75) 部分支持后者。论文应在 Discussion 中明确讨论两种解释及其含义。\n- **[R1 提出, R2 AGREE 并补充证据]**\n\n**W5 [warning]** 时间粒度选择（年度 cohort）未经论证\n- 年度 cohort 是粗粒度选择，release date ≠ training cutoff。Appendix E 半年度分析（C%=34.4%）和 Appendix O-P base-only/instruct-only 分析提供有价值信息但正文未充分整合。\"Temporal\" 标签可能误导——可能本质上是方法论差异（RLHF 普及等）而非时间差异。\n- **建议**：§3.3 或 §5.1 增加 temporal granularity 讨论，包括 release date vs training cutoff confound。\n- **[R1 提出 (W4), R2 独立提出 (W2), 完全共识]**\n\n**W6 [warning]** Abstract 信息过载\n- Abstract 包含 ≥8 个独立定量发现（C% 范围、DEFF 校正值、conservative bound、random baseline、Jaccard、ΔFPR、pp 偏移、rank displacement）。建议精简到 4-5 个核心数字。\n- **[R2 提出, R1 AGREE]**\n\n### Minor Issues（不影响接收）\n\n- **M1**：ρ≈0.997 与 ±800 rank displacement 共存的机制需在 §4.6 增加 1-2 句解释（大 ρ 反映多数模型稳定，大位移集中在密集排名区域的统计平局模型对中）。[R1 W3, R2 partial REBUT → 降级为 info]\n- **M2**：§3.4 ΔFPR=0 的陈述格式为 \"Remark\" 但多处称 \"formal guarantee\"，建议统一（升级为 Proposition 或降低措辞）。[R1 minor]\n- **M3**：Table 1 Within-family C%=61.3% 能力匹配后收敛到 ~28-29%（Appendix C），这个信息应在正文更突出，避免误导。[R1 minor]\n- **M4**：§4.7 GSM1K 相关性分析（r=-0.478, N=33）过于初步，建议移至 Appendix 或更明确标记为 exploratory。[R1 minor]\n- **M5**：Limitations 中\"generalizability to open-ended benchmarks is untested\"与 GSM8K（open-ended, C%=18.9%）已测试矛盾，应修正为\"partial-credit and free-form generation benchmarks\"。[R1 minor]\n- **M6**：Figure 1 caption \"assuming no ceiling effect\" 是 definitional illustration，应更明确标注为 schematic。[R1 minor]\n\n### Dismissed Issues（交叉讨论后排除）\n\n- **R2-W4**（Jaccard≈0.206 作为 \"near-independent\" 不精确）：R1 反驳成立——φ=0.012、OR CI 包含 1.0、permutation test 充分支持 near-independence。Jaccard 0.206 反映 base rate，非关联强度。**排除。**\n- **R2-W5**（DEFF 校正依赖 IRT 参数）：R1 指出事实性错误——DEFF 使用 ICC（intra-class correlation），非 IRT 的 Item Characteristic Curve，完全非参数。**排除。**\n- **R2-W1**（MH 方法选择缺乏与替代方法比较）：论文已在 §4.4 使用 logistic regression DIF 检测非均匀 DIF（17.7% additional, union 47%），且 θ-conditioning 作为 sensitivity check。MH 是 DIF 文献标准方法，不需额外论证。**排除。**\n\n---\n\n## Reviewer Consensus\n\n**[AGREE]** 以下问题两位 Reviewer 完全一致：\n1. DEFF 估计量的循环论证需要打破或改为区间表述 (N1)\n2. Semi-synthetic ΔTPR \"upper bound\" 不严密，difficulty-dependent 结果应进主文 (N2)\n3. k>5 ΔFPR 退化需更充分量化 (W3)\n4. 时间粒度选择需论证 (W5)\n5. Abstract 信息过载 (W6)\n\n## Reviewer Divergence\n\n**[REBUT resolved]** 以下问题经交叉讨论后达成一致：\n1. R2-N1（mechanism-agnostic 矛盾）→ R1 反驳有力（contamination 是验证工具非理论前提），降级为 Should-Fix (W1)\n2. R2-N3（Growing Pains 差异化）→ R1 反驳有力（非参数 vs 参数化是实质性差异），降级为 Should-Fix (W2)\n3. R2-W4（Jaccard 解读）→ R1 反驳成立（φ=0.012 充分），排除\n4. R2-W5（DEFF 依赖 IRT）→ R1 指出事实性错误，排除\n5. R1-W3（ρ vs displacement 张力）→ R2 partial REBUT（Figure 6 已含基线），降级为 minor\n\n**评分分歧**：\n- Soundness: R1 给 3.5（因 DEFF 循环性和 upper bound 问题），R2 给 4（认为这些是附属分析非核心方法）。取 3.5——DEFF 选择直接影响 headline number。\n- Excitement: R1 给 3.5（看重实证发现本身的价值），R2 给 3（认为方法论创新有限）。取 3。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 weighted-mean DEFF（C%=13.5%）重新计算所有下游分析（排名影响、分数修正、rank displacement），结果发生什么定性变化？\n2. 在 web-overlap 标签覆盖的 9,229 个题目中，跨学科的污染分布是什么样的？有多少学科有 >50% 的题目被标记为 web-contaminated？这能帮助约束 k 的合理范围。\n3. 是否考虑过 partial-credit flipping（模拟部分记忆）或 targeted difficulty-range injection 作为更现实的注入模式？\n4. Base-only temporal DIF（32.1%）和 instruct-only temporal DIF（36.5%）之间的差异是否在统计上显著？\n\n---\n\n## Missing References\n\n- Embretson, S.E. & Reise, S.P. (2000). *Item Response Theory for Psychologists*. IRT 基础教材参考。[R1]\n- Suk & Ryu (2026). *Rethinking DIF from a causal inference perspective*. 已在 Appendix B 引用（suk2026rethinking），但正文 Discussion 讨论 DIF 因果局限时应引用。[R1]\n- Shealy & Stout (1993). Multidimensional DIF 文献，考虑到 MMLU 的多维性值得讨论。[R2]\n- Kiela et al. (2021). Dynabench 动态评估范式——论文已引用但可更充分讨论与 temporal non-invariance 的关联。[R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 ~2.5 分钟）\n\n**Findings**:\n- **[warning]** 连续 3 页纯文本（Method 章节 pp.3-5），无 figure/table 穿插。审稿人可能在此区间失去视觉锚点。考虑将 DIF 流程或分类标准以小型示意图可视化。\n- **[warning]** Display item 分布前重后轻倒置：前 5 页仅 Figure 1，pp.6-8 集中 4 个 display item。\n- **[info]** Figure 2 y 轴标签和 legend 字号偏小但可读。Figure 6 六面板图 axis label 接近可读性下限。\n- **[info]** Tables 1-3 格式整洁，booktabs 风格，精度一致。\n- **[info]** Limitations ~8 行覆盖 3 个关键点，符合 EMNLP 要求。References ~2.5 页，格式统一，无未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 — Borderline Conference\n\n**置信度**: 4/5\n\n**评审共识总结**：\n\n论文将 MH-DIF 引入 LLM 评测是新颖且及时的贡献，实验控制深度在该领域罕见，cross-subject matching 的 ΔFPR=0 保证和 DIF ≠ contamination 的正交性发现具有实质价值。但两个关键方法论问题需要解决：(1) DEFF 估计量选择的循环论证直接影响 headline number（29.2% vs 13.5%），需改为区间表述或补充独立论证；(2) semi-synthetic ΔTPR 的 \"upper bound\" 标签不成立，主文应并列报告 difficulty-dependent injection 结果。此外，mechanism-agnostic 定位与 contamination-centric 实验设计之间的叙事张力、时间粒度选择的论证不足、Abstract 信息过载等写作层面问题也需改进。\n\n**接收建议**：如果 N1（DEFF 区间表述）和 N2（semi-synthetic terminology + 主文补充）被充分修改，论文有望升至 Conference 水平。当前状态处于 Borderline Conference / Findings 交界。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 两项贡献定位基本清晰，但 Contribution 1 中\"orthogonal to contamination labels\"的表述暗示了与 contamination 的关系，与 mechanism-agnostic 立场存在微妙张力（W1）。\n- 脚注 1 的匿名代码链接应确认对 reviewer 可访问。\n\n### §2 Related Work\n- IRT-for-LLM 文献覆盖充分（ATLAS、JE-IRT、Confident Rankings、When Benchmarks Leak 均已引用）。\n- Growing Pains 的对比需补充方法论差异（W2）。\n- 考虑补充 Suk & Ryu (2026) 在正文中的引用。\n\n### §3 Method\n- MH-DIF 定义和 ETS 分类描述清晰严谨。\n- Cross-subject matching 的 ΔFPR=0 Remark 需决定统一称谓（Proposition vs Remark, M2）。\n- Semi-synthetic injection framework 需在 framing 中明确定位为\"验证 case study\"（W1）。\n- 时间粒度选择需论证（W5）。\n\n### §4 Experiments\n- §4.2 temporal DIF 结果：DEFF 需改为区间表述或打破循环论证（N1）。\n- §4.3 ground truth mismatch：正交性解释需补充替代假设讨论（W4）。\n- §4.5 detection power：difficulty-dependent injection 结果应进主文，ΔTPR 标签修改（N2）。\n- §4.6 downstream impact：ρ vs displacement 的共存机制需 1-2 句解释（M1）。\n- §4.7 GSM1K 分析（N=33）建议移至 Appendix（M4）。\n\n### §5 Discussion\n- §5.1 temporal DIF 讨论质量较好，三个 LLM-vs-educational 区分有价值。\n- §5.2 审计协议可操作性良好，\"DIF alone cannot determine causation\" caveat 到位。\n- 需增加正交性替代解释讨论（W4）。\n\n### §6 Conclusion\n- 简洁，5 句话覆盖核心发现。无重大问题。\n\n### Limitations\n- 覆盖 3 个关键局限点，长度适当。\n- \"open-ended benchmarks untested\"与 GSM8K 结果矛盾，需修正（M5）。\n\n### Appendix\n- 详实且有组织。Appendix B Mechanism Analysis 标题建议改为更中性的措辞（如\"Exclusion Analysis\"）以与 mechanism-agnostic 定位一致。",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 17 审稿报告：Temporal Score Incomparability in LLM Benchmarks\n\n**论文**: Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 Long Paper (via ARR)\n**Reviewers**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作）\n**模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析迁移到 LLM 基准评测领域，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现 2023 与 2024 模型群组之间约 27–29% 的题目存在显著时序 DIF（保守下界 13.5%），远超随机基线（0.62%）。论文提出跨学科匹配（cross-subject matching）策略并给出 ΔFPR=0 的形式化保证（k≤5 条件下），通过半合成注入框架验证检测能力，并在六个 METABENCH 基准上复现。核心发现是 DIF 标记与 web-overlap 污染标签近乎正交（φ=0.012），base 与 instruct 模型呈现相反的 DIF 方向模式（χ²=562.7）。\n\n---\n\n## Strengths\n\n1. **跨学科方法创新**：首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型、6 个 benchmark），填补了教育测量和 LLM 评测之间的方法论空白。\n\n2. **实验控制的深度与广度**：随机分割基线、能力匹配（NN matching, Cohen's d=-0.17）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control（Δ=1.08pp）、跨基准复现——每一个潜在混淆变量都被系统检验。这种控制水平在 LLM 评测领域罕见。[R1/R2 共识]\n\n3. **Cross-subject matching 的创新**：将 purified subtest matching 改造为 LLM 多学科设置的 cross-subject matching，提供 ΔFPR=0 的形式化保证（k≤5），是对方法论的实质性贡献。[R1/R2 共识]\n\n4. **DIF ≠ contamination 的实证发现**：DIF 与 web-overlap 标签的近乎独立性（φ=0.012, OR=1.05 [0.96,1.15], permutation test p=0.88）是非平凡的经验发现，表明全局污染检测和项目功能差异是不同的维度。[R1/R2 共识]\n\n5. **Base/instruct 方向反转**：χ²=562.7 提供了强有力的机制分离证据，表明 DIF 反映的是结构化的项目级变化而非均匀群组效应。[R1 Strength]\n\n6. **详实的附录体系**：Appendix A-L 提供了 sensitivity analysis、mechanism analysis、structural analysis、DEFF estimation、uncertainty quantification 等全面补充分析，增强了可重复性。[R2 Strength]\n\n---\n\n## Weaknesses\n\n### Must-Fix（2 项，Reviewer 共识）\n\n**N1 [critical]** DEFF 估计量选择的论证存在循环性，对核心结论影响巨大\n- Simple-mean DEFF（C%=29.2%）vs weighted-mean DEFF（C%=13.5%），差距 2.16×。论文推荐 simple-mean 为 primary estimate，理由是\"与 cluster bootstrap 和 DEFF simulation 收敛\"。但 DEFF simulation（Table 12）的模拟场景使用观测到的 ICC-size 反相关模式构造——用结论构造前提，循环论证。Weighted-mean DEFF（Kish, 1965）是 survey sampling 标准方法，被降格为\"conservative extreme\"但未讨论其适用条件。若 weighted-mean 正确，headline number 需下修近一半。\n- **建议**：(1) 采用区间表述（如\"13.5–29.2%, with convergent evidence supporting the upper range\"）而非推荐单一估计量；(2) 补充独立论证打破循环性；(3) 报告 weighted-mean DEFF 下的下游分析（排名影响、分数修正）。\n- **[R1 提出, R2 AGREE]**\n\n**N2 [critical]** Semi-synthetic ΔTPR \"upper bound\" 声称不严密\n- Uniform binary flipping 不是检测能力的理论上界：集中在 medium-difficulty items 的污染可能产生比 uniform 更强的 DIF 信号（MH power 取决于 item difficulty 与 ability distribution 的交互，uniform flipping 在高/低难度 items 上浪费\"污染预算\"）。Difficulty-dependent injection（ΔTPR=0.41 vs uniform 0.51）仅在 Appendix B，主文检测能力数字（TPR 0.68–0.94）基于 uniform injection 可能过于乐观。Partial memorization 场景（模型部分记住题目线索）会产生与 binary flipping 不同的 DIF 模式，未被讨论。\n- **建议**：(1) 将\"upper bound\"改为\"reference point under stylized uniform injection\"；(2) 将 difficulty-dependent injection 结果提升到主文 §4.5 并列报告；(3) 讨论 partial memorization 场景。\n- **[R1 提出 (N2), R2 独立提出 (N2), 完全共识]**\n\n### Should-Fix（6 项）\n\n**W1 [warning]** Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力\n- 论文声称 mechanism-agnostic 立场，但 §3.4（Semi-Synthetic Injection Framework）、§4.3（Ground Truth Mismatch）、§4.5（Detection Power under Controlled Injection）、Appendix B（Mechanism Analysis）大量围绕 contamination 展开。R1 指出 contamination 是\"验证工具而非理论前提\"、正交性发现支持 mechanism-agnostic 立场，该反驳有说服力，因此从 R2 的 Must-Fix 降级为 Should-Fix。但叙事框架确实需要更清晰地区分\"DIF 作为诊断工具\"和\"contamination 作为验证手段\"。\n- **建议**：§3.4 或 §5 中明确：contamination injection 是验证 DIF 检测能力的 case study，DIF 本身是 mechanism-agnostic 的诊断工具，可由多种原因引起。\n- **[R2 提出为 Must-Fix, R1 REBUT, 降级为 Should-Fix]**\n\n**W2 [warning]** 与 Growing Pains 的差异化需补充方法论对比\n- R2 认为\"to our knowledge, no prior work applies DIF to benchmark temporal comparability\"可能不成立。R1 反驳指出：(1) FPC 是参数化方法（依赖 2PL/3PL），MH-DIF 是非参数方法，且论文已报告 2PL fit poor for MMLU；(2) Growing Pains 目标是 equating，本文目标是 diagnosis + severity grading (ETS A/B/C)。R1 反驳有力，novelty claim 在严格意义上成立。但 §2 仅一句话区分，建议补充方法论差异。\n- **建议**：§2 Growing Pains 段落补充 1-2 句方法论对比。\n- **[R2 提出为 Must-Fix, R1 REBUT, 降级为 Should-Fix]**\n\n**W3 [warning]** k>5 时 ΔFPR 保证退化的实际影响未充分量化\n- k=20 时 ΔFPR=0.069，在 weighted-mean C%=13.5% 语境下占约一半。Abstract 中\"ΔFPR=0\"未附加限定条件。论文未论证现实中 k 的合理范围。\n- **建议**：(1) Abstract 中 ΔFPR=0 附加条件（k≤5）；(2) 从 web-overlap 标签分布推断跨学科污染的经验分布以约束 k；(3) 给出 ΔFPR 对 C% 估计的敏感性分析。\n- **[R1 提出, R2 AGREE]**\n\n**W4 [warning]** DIF-contamination 正交性需讨论替代解释\n- 低 Jaccard 有两种解释：(1) DIF 是比 contamination detection 更通用的工具（论文的解读）；(2) DIF 主要测量 capability evolution/training methodology shifts，与 contamination 基本无关。Appendix B model-type interaction (OR=4.75) 部分支持后者。论文应在 Discussion 中明确讨论两种解释及其含义。\n- **[R1 提出, R2 AGREE 并补充证据]**\n\n**W5 [warning]** 时间粒度选择（年度 cohort）未经论证\n- 年度 cohort 是粗粒度选择，release date ≠ training cutoff。Appendix E 半年度分析（C%=34.4%）和 Appendix O-P base-only/instruct-only 分析提供有价值信息但正文未充分整合。\"Temporal\" 标签可能误导——可能本质上是方法论差异（RLHF 普及等）而非时间差异。\n- **建议**：§3.3 或 §5.1 增加 temporal granularity 讨论，包括 release date vs training cutoff confound。\n- **[R1 提出 (W4), R2 独立提出 (W2), 完全共识]**\n\n**W6 [warning]** Abstract 信息过载\n- Abstract 包含 ≥8 个独立定量发现（C% 范围、DEFF 校正值、conservative bound、random baseline、Jaccard、ΔFPR、pp 偏移、rank displacement）。建议精简到 4-5 个核心数字。\n- **[R2 提出, R1 AGREE]**\n\n### Minor Issues（不影响接收）\n\n- **M1**：ρ≈0.997 与 ±800 rank displacement 共存的机制需在 §4.6 增加 1-2 句解释（大 ρ 反映多数模型稳定，大位移集中在密集排名区域的统计平局模型对中）。[R1 W3, R2 partial REBUT → 降级为 info]\n- **M2**：§3.4 ΔFPR=0 的陈述格式为 \"Remark\" 但多处称 \"formal guarantee\"，建议统一（升级为 Proposition 或降低措辞）。[R1 minor]\n- **M3**：Table 1 Within-family C%=61.3% 能力匹配后收敛到 ~28-29%（Appendix C），这个信息应在正文更突出，避免误导。[R1 minor]\n- **M4**：§4.7 GSM1K 相关性分析（r=-0.478, N=33）过于初步，建议移至 Appendix 或更明确标记为 exploratory。[R1 minor]\n- **M5**：Limitations 中\"generalizability to open-ended benchmarks is untested\"与 GSM8K（open-ended, C%=18.9%）已测试矛盾，应修正为\"partial-credit and free-form generation benchmarks\"。[R1 minor]\n- **M6**：Figure 1 caption \"assuming no ceiling effect\" 是 definitional illustration，应更明确标注为 schematic。[R1 minor]\n\n### Dismissed Issues（交叉讨论后排除）\n\n- **R2-W4**（Jaccard≈0.206 作为 \"near-independent\" 不精确）：R1 反驳成立——φ=0.012、OR CI 包含 1.0、permutation test 充分支持 near-independence。Jaccard 0.206 反映 base rate，非关联强度。**排除。**\n- **R2-W5**（DEFF 校正依赖 IRT 参数）：R1 指出事实性错误——DEFF 使用 ICC（intra-class correlation），非 IRT 的 Item Characteristic Curve，完全非参数。**排除。**\n- **R2-W1**（MH 方法选择缺乏与替代方法比较）：论文已在 §4.4 使用 logistic regression DIF 检测非均匀 DIF（17.7% additional, union 47%），且 θ-conditioning 作为 sensitivity check。MH 是 DIF 文献标准方法，不需额外论证。**排除。**\n\n---\n\n## Reviewer Consensus\n\n**[AGREE]** 以下问题两位 Reviewer 完全一致：\n1. DEFF 估计量的循环论证需要打破或改为区间表述 (N1)\n2. Semi-synthetic ΔTPR \"upper bound\" 不严密，difficulty-dependent 结果应进主文 (N2)\n3. k>5 ΔFPR 退化需更充分量化 (W3)\n4. 时间粒度选择需论证 (W5)\n5. Abstract 信息过载 (W6)\n\n## Reviewer Divergence\n\n**[REBUT resolved]** 以下问题经交叉讨论后达成一致：\n1. R2-N1（mechanism-agnostic 矛盾）→ R1 反驳有力（contamination 是验证工具非理论前提），降级为 Should-Fix (W1)\n2. R2-N3（Growing Pains 差异化）→ R1 反驳有力（非参数 vs 参数化是实质性差异），降级为 Should-Fix (W2)\n3. R2-W4（Jaccard 解读）→ R1 反驳成立（φ=0.012 充分），排除\n4. R2-W5（DEFF 依赖 IRT）→ R1 指出事实性错误，排除\n5. R1-W3（ρ vs displacement 张力）→ R2 partial REBUT（Figure 6 已含基线），降级为 minor\n\n**评分分歧**：\n- Soundness: R1 给 3.5（因 DEFF 循环性和 upper bound 问题），R2 给 4（认为这些是附属分析非核心方法）。取 3.5——DEFF 选择直接影响 headline number。\n- Excitement: R1 给 3.5（看重实证发现本身的价值），R2 给 3（认为方法论创新有限）。取 3。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 weighted-mean DEFF（C%=13.5%）重新计算所有下游分析（排名影响、分数修正、rank displacement），结果发生什么定性变化？\n2. 在 web-overlap 标签覆盖的 9,229 个题目中，跨学科的污染分布是什么样的？有多少学科有 >50% 的题目被标记为 web-contaminated？这能帮助约束 k 的合理范围。\n3. 是否考虑过 partial-credit flipping（模拟部分记忆）或 targeted difficulty-range injection 作为更现实的注入模式？\n4. Base-only temporal DIF（32.1%）和 instruct-only temporal DIF（36.5%）之间的差异是否在统计上显著？\n\n---\n\n## Missing References\n\n- Embretson, S.E. & Reise, S.P. (2000). *Item Response Theory for Psychologists*. IRT 基础教材参考。[R1]\n- Suk & Ryu (2026). *Rethinking DIF from a causal inference perspective*. 已在 Appendix B 引用（suk2026rethinking），但正文 Discussion 讨论 DIF 因果局限时应引用。[R1]\n- Shealy & Stout (1993). Multidimensional DIF 文献，考虑到 MMLU 的多维性值得讨论。[R2]\n- Kiela et al. (2021). Dynabench 动态评估范式——论文已引用但可更充分讨论与 temporal non-invariance 的关联。[R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时 ~2.5 分钟）\n\n**Findings**:\n- **[warning]** 连续 3 页纯文本（Method 章节 pp.3-5），无 figure/table 穿插。审稿人可能在此区间失去视觉锚点。考虑将 DIF 流程或分类标准以小型示意图可视化。\n- **[warning]** Display item 分布前重后轻倒置：前 5 页仅 Figure 1，pp.6-8 集中 4 个 display item。\n- **[info]** Figure 2 y 轴标签和 legend 字号偏小但可读。Figure 6 六面板图 axis label 接近可读性下限。\n- **[info]** Tables 1-3 格式整洁，booktabs 风格，精度一致。\n- **[info]** Limitations ~8 行覆盖 3 个关键点，符合 EMNLP 要求。References ~2.5 页，格式统一，无未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 — Borderline Conference\n\n**置信度**: 4/5\n\n**评审共识总结**：\n\n论文将 MH-DIF 引入 LLM 评测是新颖且及时的贡献，实验控制深度在该领域罕见，cross-subject matching 的 ΔFPR=0 保证和 DIF ≠ contamination 的正交性发现具有实质价值。但两个关键方法论问题需要解决：(1) DEFF 估计量选择的循环论证直接影响 headline number（29.2% vs 13.5%），需改为区间表述或补充独立论证；(2) semi-synthetic ΔTPR 的 \"upper bound\" 标签不成立，主文应并列报告 difficulty-dependent injection 结果。此外，mechanism-agnostic 定位与 contamination-centric 实验设计之间的叙事张力、时间粒度选择的论证不足、Abstract 信息过载等写作层面问题也需改进。\n\n**接收建议**：如果 N1（DEFF 区间表述）和 N2（semi-synthetic terminology + 主文补充）被充分修改，论文有望升至 Conference 水平。当前状态处于 Borderline Conference / Findings 交界。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 两项贡献定位基本清晰，但 Contribution 1 中\"orthogonal to contamination labels\"的表述暗示了与 contamination 的关系，与 mechanism-agnostic 立场存在微妙张力（W1）。\n- 脚注 1 的匿名代码链接应确认对 reviewer 可访问。\n\n### §2 Related Work\n- IRT-for-LLM 文献覆盖充分（ATLAS、JE-IRT、Confident Rankings、When Benchmarks Leak 均已引用）。\n- Growing Pains 的对比需补充方法论差异（W2）。\n- 考虑补充 Suk & Ryu (2026) 在正文中的引用。\n\n### §3 Method\n- MH-DIF 定义和 ETS 分类描述清晰严谨。\n- Cross-subject matching 的 ΔFPR=0 Remark 需决定统一称谓（Proposition vs Remark, M2）。\n- Semi-synthetic injection framework 需在 framing 中明确定位为\"验证 case study\"（W1）。\n- 时间粒度选择需论证（W5）。\n\n### §4 Experiments\n- §4.2 temporal DIF 结果：DEFF 需改为区间表述或打破循环论证（N1）。\n- §4.3 ground truth mismatch：正交性解释需补充替代假设讨论（W4）。\n- §4.5 detection power：difficulty-dependent injection 结果应进主文，ΔTPR 标签修改（N2）。\n- §4.6 downstream impact：ρ vs displacement 的共存机制需 1-2 句解释（M1）。\n- §4.7 GSM1K 分析（N=33）建议移至 Appendix（M4）。\n\n### §5 Discussion\n- §5.1 temporal DIF 讨论质量较好，三个 LLM-vs-educational 区分有价值。\n- §5.2 审计协议可操作性良好，\"DIF alone cannot determine causation\" caveat 到位。\n- 需增加正交性替代解释讨论（W4）。\n\n### §6 Conclusion\n- 简洁，5 句话覆盖核心发现。无重大问题。\n\n### Limitations\n- 覆盖 3 个关键局限点，长度适当。\n- \"open-ended benchmarks untested\"与 GSM8K 结果矛盾，需修正（M5）。\n\n### Appendix\n- 详实且有组织。Appendix B Mechanism Analysis 标题建议改为更中性的措辞（如\"Exclusion Analysis\"）以与 mechanism-agnostic 定位一致。",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1612 · 2026-05-23T11:39:44.711970+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 1613 · 2026-05-23T11:39:59.014929+00:00_

**Round 17 审稿完成，报告已投递。**

汇总：
- **Overall**: 3.5（Borderline Conference），置信度 4/5
- **2 个 Must-Fix**：(1) DEFF 估计量选择循环论证，需改为区间表述或独立论证；(2) semi-synthetic ΔTPR "upper bound" 不成立，difficulty-dependent 结果应进主文
- **6 个 Should-Fix**：mechanism-agnostic 叙事张力、Growing Pains 差异化、k>5 ΔFPR 量化、正交性替代解释、时间粒度论证、Abstract 精简
- **6 个 Minor**：ρ vs displacement 解释、Remark 术语统一、Table 1 上下文等
- **3 个 Dismissed**：R2 的 Jaccard 解读（φ=0.012 充分）、DEFF 依赖 IRT（事实性错误）、MH 方法比较（论文已含）

Issue Tracker 已同步更新（9 个新 open issue + 12 个历史 resolved issue）。视觉审查结果已纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 158

## Round 158

2 recorded events


### User

_source line 1614 · 2026-05-23T11:40:01.631110+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 6 个问题逐条回应：

- **N1 (DEFF 循环性)**: [AGREE] — 2.16× 差距是实质性的，建议同时报告两个估计量
- **N2 (upper bound 不严密)**: [AGREE] — 与我的 N2 互补，uniform flipping 确实不是理论上界
- **W1 (ΔFPR 退化)**: [AGREE] — k=20 时 ΔFPR=0.069 在保守估计下非 trivial
- **W2 (正交性替代解释)**: [AGREE] — DIF 可能测量 architecture/methodology 差异而非 contamination
- **W3 (ρ vs displacement 张力)**: [REBUT] — Figure 6 已提供随机基线，但主文确需改进解释
- **W4 (时间粒度)**: [AGREE] — 与我的 W2 一致

两位 reviewer 在 Overall 3.5 上达成一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1615 · 2026-05-23T11:40:13.518193+00:00_

Round 17 审稿报告已提交至 Research Director。

**评分**: 3.5 — Borderline Conference（R1/R2 一致）

**核心结论**:
- 2 个 Must-Fix（DEFF 循环论证 + semi-synthetic "upper bound" 不严密）
- 6 个 Should-Fix（mechanism-agnostic 叙事张力、Growing Pains 对比、ΔFPR 退化量化、正交性替代解释、时间粒度论证、Abstract 过载）
- 6 个 Minor
- 3 个 Dismissed（R2-W4/W5/W1 经交叉讨论后排除）

两个 Must-Fix 均可在修订中解决：N1 改为区间表述或补充独立论证，N2 将 difficulty-dependent injection 提升到主文并修改术语。充分修改后有望升至 Conference 水平。

Issue Tracker 已同步更新（9 个新 open issue + 12 个 R16 resolved issue 状态确认）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 159

## Round 159

56 recorded events


### User

_source line 1616 · 2026-05-23T13:56:58.856190+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1617 · 2026-05-23T13:57:05.044741+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1618 · 2026-05-23T13:57:05.095940+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1619 · 2026-05-23T13:57:12.983913+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1620 · 2026-05-23T13:57:12.984461+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1621 · 2026-05-23T13:57:23.132559+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1622 · 2026-05-23T13:57:24.037055+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1623 · 2026-05-23T13:57:24.037535+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1624 · 2026-05-23T13:57:24.088894+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1625 · 2026-05-23T13:57:29.915652+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1626 · 2026-05-23T13:57:31.824931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-23T13:57:31.976076+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Score Incomparability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-23T13:57:32.528683+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1629 · 2026-05-23T13:57:32.579307+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1630 · 2026-05-23T13:57:36.872887+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## Paper Types and Scope
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Presentation Requirements
All accepted papers must be presented at the conference to appear in the proceedings. The conference will include both in-person and virtual presentation options. Papers without at least one presenting author registered by the 
…[truncated 708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6957
}
```

</details>

---


### Tool call

_source line 1631 · 2026-05-23T13:57:43.300361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1632 · 2026-05-23T13:57:43.652173+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 models), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (13.5--29.2\% for MMLU after non-independence corrections; ${\geq}22\times$ random baseline). Web-overlap contamination labels are near-independent of DIF flags: global exposure and differential functioning are complementary diagnostic dimensions. Temporal DIF does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals structured item-level change---base and instruct models exhibit opposite DIF patterns ($\chi^2 = 562.7$), evidence that DIF captures capability shifts beyond contamination---and shifts DIF-corrected scores by ${+}2.12$\,pp on average. We propose a three-step audit protocol (Monitor/Triage/Correct) with empirically grounded thresholds for benchmark maintainers. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1633 · 2026-05-23T13:57:43.652526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1634 · 2026-05-23T13:57:44.204919+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} (measurement non-invariance across temporal cohorts, manifesting as score incomparability) as the empirical phenomenon when DIF is detected---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://github.com/anonymous-nlp-2026-2/irt_equated_bench_regen}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.62\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 849 rank positions. This instability does not invalidate the benchmark---aggregate rankings are massively redundant---but it is diagnostic, revealing which capability dimensions shift across model generations.
6	
7	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items 
…[truncated 3405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1635 · 2026-05-23T13:57:44.205289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1636 · 2026-05-23T13:57:45.109200+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating} in-context learning effects~\citep{zawalski2026codec}, or inference-time decontamination~\citep{chai2026benchmarksleak}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introd
…[truncated 4849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1637 · 2026-05-23T13:57:45.109579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1638 · 2026-05-23T13:57:45.611994+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1639 · 2026-05-23T13:57:45.612651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1640 · 2026-05-23T13:57:45.763852+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: 31\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift $= {+}1
…[truncated 9862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1641 · 2026-05-23T13:57:46.115890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1642 · 2026-05-23T13:57:46.568322+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Temporal DIF as Structured Signal}
5	\label{sec:disc_temporal}
6	
7	\looseness=-1
8	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design. Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
9	
10	\looseness=-1
11	Composition downsampling ($\Delta = 1.08$\,pp), base-only, and instruct-only temporal analyses independently confirm DIF is not an artifact of cohort structure (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}), motivating periodic psychometric audits alongside score reporting.
12	
13	\looseness=-2
14	Three features distinguish LLM temporal DIF from educational settings: (1)~the observed C\% (13.5--29.2\%) substantially exceeds typical educational DIF rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$), unlike educational settings where DIF correlates with construct-irrelevant variance; (3)~the near-independence admits two interpretations: DIF captures a broader signal---including capability evolution and training methodology shifts---of which contamination is one component, or DIF and contamination detection measure distinct constructs. The base/instruct direction reversal and model-type interaction (OR $= 4.75$; \Cref{app:mechanism_discussion}) favor the former, as contamination alone cannot explain opposing DIF patterns. Either interpretation supports periodic DIF audits.
15	
16	\subsection{Recommended DIF Audit Protocol}
17	\label{sec:di
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1643 · 2026-05-23T13:57:46.568852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1644 · 2026-05-23T13:57:47.071224+00:00_

1	\enlargethispage{2\baselineskip}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	\looseness=-2
6	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (13.5--29.2\% for MMLU after non-independence corrections), while aggregate rankings remain preserved ($\rho \approx 0.997$). Global exposure and differential functioning are complementary diagnostic dimensions (Jaccard $= 0.206$), confirmed by opposite base-vs-instruct DIF patterns ($\chi^2 = 562.7$). Mechanism-conditional DIF audit---including DIF-corrected score reporting---should complement contamination screening as standard practice~\citep{habba2026growingpains}. Connecting temporal DIF to specific training factors remains open; tracking DIF across model generations with known data composition could test the contamination-versus-capability hypothesis.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1645 · 2026-05-23T13:57:47.222228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1646 · 2026-05-23T13:57:47.975766+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\Delta\mathrm{TPR}$ values may overestimate detection power. Partial memorization scenarios---where models recall item cues without deterministic answer flipping---would produce weaker and qualitatively different DIF patterns than our binary injection model. The framework detects \emph{that} items function differently but not \emph{why}---a deliberate design choice that limits immediate actionability; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Two DEFF estimators (13.5--29.2\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to partial-credit and free-form generation benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric. 
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1647 · 2026-05-23T13:57:47.976262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1648 · 2026-05-23T13:57:48.780330+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 30347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1649 · 2026-05-23T13:57:48.932879+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1650 · 2026-05-23T13:57:49.135461+00:00_

issues:
  # === Round 17 issues (all resolved by R18 verification) ===

  - id: "R17-N1"
    summary: "DEFF 估计量选择论证存在循环性——simulation 用观测 ICC-size 模式构造前提，再论证 simple-mean 更优"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 17
    last_seen_round: 17
    mentions:
      - round: 17
        reviewers: [1, 2]
        note: "R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%，差距 2.16×。"
      - round: 18
        reviewers: []
        note: "Reviewer 验证 PASS。区间表述 13.5-29.2% 全文 8 处同步；cluster bootstrap 独立证据；weighted-mean downstream 分析确认结论稳健。"
    action_items:
      - round: 17
        action: "改为区间表述 13.5-29.2%，cluster bootstrap CI 作为独立证据，weighted-mean downstream 分析"
        assigned_to: paper_agent
        status: done
    resolution: "区间表述 13.5-29.2% 替代 simple-mean 推荐；cluster bootstrap CI 排除 weighted-mean 13.5%，提供模型无关证据；weighted-mean downstream (ρ=0.999, +1.77pp) 确认结论稳健。Reviewer 验证 PASS。"
    resolution_round: 18

  - id: "R17-N2"
    summary: "Semi-synthetic ΔTPR 'upper bound' 声称不严密——uniform flipping 非理论上界，difficulty-dependent 结果应进主文"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 17
    last_seen_round: 17
    mentions:
      - round: 17
        reviewers: [1, 2]
        note: "uniform 非真正上界；difficulty-dependent injection 仅在 Appendix。"
      - round: 18
        reviewers: []
        note: "Reviewer 验证 PASS。'reference-case detection power' 替换完成；difficulty-dependent 进入主文 §4.5。"
    action_items:
      - round: 17
        action: "'upper bound' → 'reference-case detection power'; difficulty-dependent 进主文"
        assigned_to: paper_agent
        status: done
    resolution: "'upper bound' → 'reference-case detection power under stylized uniform injection'；ΔTPR≈0.41 vs 0.51 (20% reduction) 进入主文 §4.5；Limitations 加 partial memorization caveat。Reviewer 验证 PASS。"
    resolution_round: 18

  - id: "R17-W1"
    summary: "Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力"
    category
…[truncated 6161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1651 · 2026-05-23T13:58:03.095308+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-23T13:58:03.095784+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-23T13:58:04.402415+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool result

_source line 1654 · 2026-05-23T13:58:04.402850+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool call

_source line 1655 · 2026-05-23T13:58:04.403072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1656 · 2026-05-23T13:58:04.755394+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{zawalski2026codec,
6	  title     = {Detecting Data Contamination in {LLM}s via In-Context Learning},
7	  author    = {Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
8	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
9	  year      = {2026},
10	  url       = {https://arxiv.org/abs/2510.27055}
11	}
12	
13	@inproceedings{balloccu2024leak,
14	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
15	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
16	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
17	  year      = {2024},
18	  doi       = {10.18653/v1/2024.eacl-long.5},
19	  url       = {https://arxiv.org/abs/2402.03927}
20	}
21	
22	@inproceedings{dekoninck2024constat,
23	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
24	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2405.16281}
28	}
29	
30	@inproceedings{golchin2024timetravel,
31	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
32	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
33	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
34	  year      = {2024},
35	  url       = {https://arxiv.org/abs/2308.08493}
36	}
37	
38	@inproceedings{li2024contamination,
39	  title     = {An Open-Source Data Contamination Report for Large Language Models},

…[truncated 29968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1657 · 2026-05-23T13:58:32.993951+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1658 · 2026-05-23T13:58:59.192607+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26198
}
```

</details>

---


### Tool call

_source line 1659 · 2026-05-23T13:58:59.845427+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf`\n\n## 论文概述\n\"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"——将教育测量中的 DIF (Differential Item Functioning) 分析应用于 METABENCH 的 5,227 个 LLM 模型，发现 17.9-31.3% 的 benchmark items 在 2023-2024 cohort 之间表现出 temporal DIF，而 DIF 信号与 web-overlap contamination labels 近乎独立 (Jaccard=0.206)。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法的统计严谨性**\n   - ETS 阈值（从人类考生校准）直接用于 LLM 是否合理？论文用 random-split P99=1.45 做了经验校准，是否充分？\n   - K=5 quintile stratification 的选择是否有充分论证？\n   - 多重检验问题：12,508 items 的 multiple testing，ETS dual threshold 是否足够控制 FPR？\n\n2. **DEFF 校正的有效性**\n   - Simple-mean vs weighted-mean DEFF 差距 2.16×（29.2% vs 13.5%）。论文给出区间表述，但区间本身是否可靠？\n   - Cluster bootstrap CI [26.7%, 53.2%] 排除了 13.5%，论证是否循环？\n   - ICC 估计依赖 family 定义，family 边界的敏感性分析是否充分？\n\n3. **Semi-synthetic 注入框架**\n   - Uniform binary flipping 的 ecological validity——partial memorization 场景下检测力是否被高估？\n   - Cross-subject matching ΔFPR=0 保证在 k≤5 时成立，但 k>5 退化的实际影响？\n   - Difficulty-dependent injection (ΔTPR≈0.41 vs 0.51) 是否充分表征了真实场景？\n\n4. **因果推断的边界**\n   - Mechanism-agnostic 定位是否一致贯穿全文？有无地方暗示因果关系？\n   - Base/instruct direction reversal (χ²=562.7) 的解释力——是否排除了 cohort composition confound？\n   - DIF-contamination orthogonality 的两种解释是否平衡呈现？\n\n5. **实验设计与数据**\n   - METABENCH 数据集的代表性——全部来自 Open LLM Leaderboard，是否存在 selection bias？\n   - Calendar-year cohort boundary 的粗糙性——release date ≠ training cutoff\n   - 99.98% decoder-only 的 architecture homogeneity 是否限制了 generalizability？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (按 severity 排序) → Questions → Missing References → Overall Assessment (含置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf`\n\n## 论文概述\n\"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"——将教育测量中的 DIF (Differential Item Functioning) 分析应用于 METABENCH 的 5,227 个 LLM 模型，发现 17.9-31.3% 的 benchmark items 在 2023-2024 cohort 之间表现出 temporal DIF，而 DIF 信号与 web-overlap contamination labels 近乎独立 (Jaccard=0.206)。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法的统计严谨性**\n   - ETS 阈值（从人类考生校准）直接用于 LLM 是否合理？论文用 random-split P99=1.45 做了经验校准，是否充分？\n   - K=5 quintile stratification 的选择是否有充分论证？\n   - 多重检验问题：12,508 items 的 multiple testing，ETS dual threshold 是否足够控制 FPR？\n\n2. **DEFF 校正的有效性**\n   - Simple-mean vs weighted-mean DEFF 差距 2.16×（29.2% vs 13.5%）。论文给出区间表述，但区间本身是否可靠？\n   - Cluster bootstrap CI [26.7%, 53.2%] 排除了 13.5%，论证是否循环？\n   - ICC 估计依赖 family 定义，family 边界的敏感性分析是否充分？\n\n3. **Semi-synthetic 注入框架**\n   - Uniform binary flipping 的 ecological validity——partial memorization 场景下检测力是否被高估？\n   - Cross-subject matching ΔFPR=0 保证在 k≤5 时成立，但 k>5 退化的实际影响？\n   - Difficulty-dependent injection (ΔTPR≈0.41 vs 0.51) 是否充分表征了真实场景？\n\n4. **因果推断的边界**\n   - Mechanism-agnostic 定位是否一致贯穿全文？有无地方暗示因果关系？\n   - Base/instruct direction reversal (χ²=562.7) 的解释力——是否排除了 cohort composition confound？\n   - DIF-contamination orthogonality 的两种解释是否平衡呈现？\n\n5. **实验设计与数据**\n   - METABENCH 数据集的代表性——全部来自 Open LLM Leaderboard，是否存在 selection bias？\n   - Calendar-year cohort boundary 的粗糙性——release date ≠ training cutoff\n   - 99.98% decoder-only 的 architecture homogeneity 是否限制了 generalizability？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (按 severity 排序) → Questions → Missing References → Overall Assessment (含置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1660 · 2026-05-23T13:59:16.194497+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16349
}
```

</details>

---


### Tool call

_source line 1661 · 2026-05-23T13:59:16.345516+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf`\n\n## 论文概述\n\"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"——将教育测量中的 DIF 分析应用于 METABENCH 的 5,227 个 LLM 模型，发现 17.9-31.3% 的 items 在 2023-2024 cohort 间表现出 temporal DIF，且与 web-overlap contamination labels 近乎独立。提出三步 Monitor/Triage/Correct 审计协议。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - DIF 应用于 LLM benchmark 的 novelty 是否足够？与 Growing Pains (Habba et al., 2026) 的差异化是否清晰？\n   - Cross-subject matching 作为方法贡献的 novelty——是否仅为 purified subtest matching 的直接应用？\n   - 三步审计协议的实用性——threshold 选择是否有足够经验支撑？\n\n2. **Related Work 覆盖**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 近期 benchmark contamination 领域的新方法\n     - IRT-for-LLM 领域的其他工作\n     - Measurement invariance 在 NLP 以外领域的应用经验\n   - 与 concurrent work 的定位是否公平？\n\n3. **叙事连贯性与 Framing**\n   - Title \"Temporal Score Incomparability\" 是否准确反映论文内容？\n   - Abstract 信息密度是否合适？（当前约 122 words，~6 核心数字）\n   - Introduction 的 contribution 声称（3 点）是否与实验结果匹配？\n   - \"measurement instability\" vs \"contamination\" 的叙事平衡\n\n4. **Presentation 质量**\n   - Figure 1 (ICC schematic) 是否有效传达核心信息？\n   - 表格设计（6 个表格）是否清晰、信息密度适当？\n   - Appendix 与主文的内容分配是否合理？\n   - 术语一致性（temporal DIF / score incomparability / measurement invariance）\n\n5. **格式合规**\n   - 正文是否在 8 页内？注意 `\\enlargethispage{2\\baselineskip}` 的使用\n   - Limitations 节是否在正文中（不在 appendix）？\n   - 匿名性——是否有 deanonymization risk（GitHub URL、数据集引用等）？\n   - 参考文献格式是否一致？\n\n6. **Completeness**\n   - 是否有未兑现的实验承诺？\n   - Limitations 覆盖是否充分？\n   - Ethical considerations 是否需要？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (按 severity 排序) → Questions → Missing References → Overall Assessment (含置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (Long Paper, via ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_18/submitted.pdf`\n\n## 论文概述\n\"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"——将教育测量中的 DIF 分析应用于 METABENCH 的 5,227 个 LLM 模型，发现 17.9-31.3% 的 items 在 2023-2024 cohort 间表现出 temporal DIF，且与 web-overlap contamination labels 近乎独立。提出三步 Monitor/Triage/Correct 审计协议。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - DIF 应用于 LLM benchmark 的 novelty 是否足够？与 Growing Pains (Habba et al., 2026) 的差异化是否清晰？\n   - Cross-subject matching 作为方法贡献的 novelty——是否仅为 purified subtest matching 的直接应用？\n   - 三步审计协议的实用性——threshold 选择是否有足够经验支撑？\n\n2. **Related Work 覆盖**\n   - 是否遗漏了重要的相关工作？特别是：\n     - 近期 benchmark contamination 领域的新方法\n     - IRT-for-LLM 领域的其他工作\n     - Measurement invariance 在 NLP 以外领域的应用经验\n   - 与 concurrent work 的定位是否公平？\n\n3. **叙事连贯性与 Framing**\n   - Title \"Temporal Score Incomparability\" 是否准确反映论文内容？\n   - Abstract 信息密度是否合适？（当前约 122 words，~6 核心数字）\n   - Introduction 的 contribution 声称（3 点）是否与实验结果匹配？\n   - \"measurement instability\" vs \"contamination\" 的叙事平衡\n\n4. **Presentation 质量**\n   - Figure 1 (ICC schematic) 是否有效传达核心信息？\n   - 表格设计（6 个表格）是否清晰、信息密度适当？\n   - Appendix 与主文的内容分配是否合理？\n   - 术语一致性（temporal DIF / score incomparability / measurement invariance）\n\n5. **格式合规**\n   - 正文是否在 8 页内？注意 `\\enlargethispage{2\\baselineskip}` 的使用\n   - Limitations 节是否在正文中（不在 appendix）？\n   - 匿名性——是否有 deanonymization risk（GitHub URL、数据集引用等）？\n   - 参考文献格式是否一致？\n\n6. **Completeness**\n   - 是否有未兑现的实验承诺？\n   - Limitations 覆盖是否充分？\n   - Ethical considerations 是否需要？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (按 severity 排序) → Questions → Missing References → Overall Assessment (含置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1662 · 2026-05-23T13:59:17.859945+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1514
}
```

</details>

---


### Tool call

_source line 1663 · 2026-05-23T13:59:24.052881+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "config",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "config",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1664 · 2026-05-23T13:59:24.153769+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1665 · 2026-05-23T13:59:27.723443+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/irt_equated_bench_regen/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/irt_equated_bench_regen/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
  }
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-23T13:59:28.577101+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-23T13:59:31.489954+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/irt_equated_bench_regen/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/irt_equated_bench_regen/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
  }
}
```

</details>

---


### Tool result

_source line 1668 · 2026-05-23T13:59:31.590732+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.git/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1669 · 2026-05-23T13:59:35.623603+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1670 · 2026-05-23T13:59:35.774689+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 1671 · 2026-05-23T13:59:44.451819+00:00_

外部审稿未配置（`external_review.paperreview_ai.enabled` 未找到），跳过外部审稿线。

**当前状态**：
- 视觉审查：已派发（running）
- Reviewer 1（方法严谨性）：已派发，等待回复
- Reviewer 2（新颖性/完整性）：已派发，等待回复

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 1672 · 2026-05-23T14:05:15.329349+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）

**论文**: "Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
**Venue**: EMNLP 2026 (Long Paper, via ARR)

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 大规模实证发现有价值（temporal DIF 与 contamination 近乎正交），但核心方法是 off-the-shelf MH-DIF 的直接搬运，方法论创新不足以稳进主会。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法本身正确，但因果推断过度（DIF 是关联而非因果）；contamination independence claim 依赖质量存疑的 web-overlap proxy |
| Excitement | 3/5 | 实证发现（31% items exhibit DIF, 且与 contamination 正交）有趣但 insight 深度有限；方法论贡献偏增量 |
| Reproducibility | 4/5 | 数据来自公开 METABENCH，方法细节充分，有 semi-synthetic validation；但脚注 URL 可能涉及匿名性问题 |
| Confidence | 4/5 | 熟悉 IRT/DIF 方法论和 LLM evaluation 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心方法论新颖性不足——MH-DIF 是 40 年前的标准方法的直接应用
- 具体位置：Section 3.2, Section 3 全节
- 问题：Mantel-Haenszel DIF 检测（Holland & Thayer, 1988）+ ETS severity 分类是教育测量领域的标准流程，论文将其直接搬运到 LLM benchmark 场景。Section 3.2 的方法描述本质上是教科书内容——K=5 等频分层、对数 odds ratio、ETS A/B/C 分类标准均原封不动。论文声称的三点贡献中（Section 1），第一点（temporal DIF at scale）是实证发现而非方法创新；第二点（cross-subject matching）是 purified subtest matching (Donoghue and Allen, 1993) 的直接推广；第三点（audit protocol）是组合既有步骤。对于 EMNLP main conference，需要论证为什么这不仅仅是"在新数据集上跑老方法"。
- 为什么影响接收：ARR review form 的 Excitement 维度要求论文提供 "new insights or methods"。如果 reviewer 判断方法论贡献为纯应用型，可能被归类为 Findings 而非 Conference。
- 建议修改方向：(a) 更清晰地论证 LLM 多学科结构（57 subjects）带来的 cross-subject matching 的技术挑战和理论保证（ΔFPR=0 的证明可以更突出）；(b) 讨论为什么 MH-DIF 在 LLM 场景下的 4 个 LLM-specific challenges（Section 3.2 末尾提到但未充分展开）构成真正的方法适配贡献；(c) 考虑增加与参数化 DIF 方法（如 logistic regression DIF）的比较，展示方法选择的合理性。

**N2** [critical] "DIF 与 contamination 近乎独立"的核心发现依赖质量存疑的 proxy
- 具体位置：Section 4.3, Table 1 (Enrichment column)
- 问题：论文最引人注目的发现是 DIF flags 与 web-overlap contamination labels 的 Jaccard ≈ 0.20（Section 4.3: "near-independence"）。但 web-overlap labels 来自 Li et al. (2024b)，仅检测 benchmark items 是否在公开网络语料中出现——这是一个非常粗糙的 contamination proxy。(1) Web-overlap ≠ 实际训练数据包含；(2) 许多 contamination 来源（如 synthetic data augmentation、instruction tuning 数据）不会被 web-overlap 捕获；(3) Li et al. 自己的 labels 覆盖率仅 73.8%（9,229/12,508），剩余 items 标记为 dash (—)。因此 Jaccard ≈ 0.20 可能仅反映 web-overlap labels 的低质量，而非 DIF 与 "真正的" contamination 的独立性。
- 为什么影响接收：这是论文的 headline finding，直接支撑 "DIF captures a broader signal" 的核心叙事（Section 5.1）。如果这个发现的基础不牢，整篇论文的叙事逻辑都会受影响。
- 建议修改方向：(a) 明确讨论 web-overlap 作为 contamination proxy 的局限性；(b) 使用多种 contamination 指标（如 Time Travel scores、memorization scores from Dekoninck et al.）进行交叉验证；(c) 将结论从 "DIF is independent of contamination" 软化为 "DIF is independent of web-overlap based contamination labels"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证
- 具体位置：Section 3.2, Section 5.2
- 问题：ETS Category A/B/C 阈值（|Δ_MH| < 1.0, 1.0–1.5, ≥ 1.5）是为人类考生群体标定的。论文在 Section 3.2 承认 "these thresholds were calibrated for human test-taker populations" 并声称 "retain them as standardized reference points"。但 LLM 的能力分布、作答模式与人类根本不同——例如 LLM 没有 guessing behavior（或有不同的 guessing pattern），能力维度可能是高度多维的。Section 5.2 的 Monitor/Triage/Correct 审计协议直接依赖这些阈值，如果阈值不适用于 LLM，整个协议的实用性都成问题。
- 建议：(a) 通过 simulation 研究验证 ETS 阈值在 LLM response matrix 下的 Type I error 和 power；(b) 或者提出 data-driven 的阈值选择方法（如 bootstrap percentile）。

**W2** [warning] 与 Growing Pains (Habba et al., 2026) 的差异化论证不够深入
- 具体位置：Section 2 (Related Work, 最后一段), Section 1 (Introduction, footnote)
- 问题：论文在 Section 2 末尾花了一段讨论与 Growing Pains 的关系，定位为 "complementary"。但差异化主要停留在方法层面（MH-DIF vs. fixed-parameter calibration），缺少在相同数据/相同 items 上的直接比较。读者无法判断两种方法是否会 flag 相同的 items、是否给出一致的结论。论文声称 "our DIF analysis identifies which items should not serve as anchors"，暗示 Growing Pains 的 anchor selection 可能有问题，但没有实证支撑。
- 建议：如果可能，在附录中加入与 Growing Pains 方法在相同 items 上的交叉比较；否则至少明确讨论两种方法在理论上会在哪些情况下 diverge。

**W3** [warning] "Temporal" framing 可能过窄——实际检测到的是 cohort-based DIF
- 具体位置：Title, Abstract, Section 5.1
- 问题：论文标题 "Temporal Score Incomparability" 暗示时间是唯一变量。但 2023 vs. 2024 cohorts 不仅在时间上不同，还在模型架构、训练数据规模、训练方法（RLHF 频率增加等）上系统性不同。Section 5.1 承认 "three non-exclusive mechanisms may drive the observed DIF rate"（Appendix B），包括 differential contamination、capability evolution、training methodology shifts。既然如此，称之为 "temporal" DIF 实际上是把所有 cohort 间差异都归到时间维度上，而更准确的说法是 "cohort-based" DIF。这不是措辞问题——它影响 DIF 发现的可解释性。
- 建议：在 Discussion 中更明确地讨论 temporal confounding，考虑至少在一个控制实验中分离出纯时间效应（如同一 model family 在不同时间点的版本）。

**W4** [warning] 因果性过度暗示
- 具体位置：Section 5.1 ("DIF captures a broader signal—including capability evolution and training methodology shifts"), Abstract ("scores are not directly comparable across cohorts because item measurement properties differ systematically")
- 问题：DIF 是一个统计关联——在控制 matching variable 后，item response 与 group membership 的关联。它不能区分 (a) 真正的测量不变性违反（items 在不同 cohort 测的不是同一 construct），(b) 与 cohort 相关的多维性，(c) matching variable 未能完全捕获的系统性能力差异。Abstract 中 "because item measurement properties differ systematically" 隐含因果判断，但实际上 DIF 只能说明 "items function differently after conditioning on total score"。Section 5.1 的 "DIF captures a broader signal" 进一步加强了因果暗示。
- 建议：使用更谨慎的语言，如 "items exhibit differential functioning" 而非 "measurement properties differ"；增加对 DIF 统计本质（关联非因果）的明确说明。

**W5** [warning] Score correction 的实际影响展示不充分
- 具体位置：Section 4.6 (Downstream Impact)
- 问题：Section 4.6 提到 DIF-corrected scores shift accuracy by ±2.12pp 且 33.6% of pairwise rankings reverse，但仅占半页篇幅。作为 audit protocol 最终要落地的环节，这个分析太薄——(a) 没有展示具体哪些模型的排名发生了显著变化；(b) 没有区分 ranking reversal 发生在 top-10 还是 mid-tier（影响完全不同）；(c) 没有与其他 score correction 方法比较。
- 建议：扩展 Section 4.6 或在 Appendix 中加入 case study，展示 DIF correction 如何具体影响 leaderboard 的 top-k 排名。

---

## 小问题（不影响接收）

- **术语不一致**：论文交替使用 "temporal DIF"、"score incomparability"、"measurement invariance" 三个术语。虽然相关但含义不同：DIF 是统计检验，score incomparability 是后果，measurement invariance 是更广义的框架。建议在 Section 3 开头明确定义并统一使用。

- **Figure 1 (ICC schematic)**：概念图清晰有效，但左右面板的 y 轴标注 "Test-Taker Ability" 用于 LLM 场景可能不恰当。建议改为 "Model Ability" 或 "Latent Trait Score"。

- **匿名性风险**：Page 1 脚注包含一个 URL（指向代码仓库）。在 double-blind review 下，如果这是一个非匿名化的 GitHub URL，构成 deanonymization risk。建议使用 anonymous.4open.science 或类似匿名提交服务。

- **Limitations 节内容适当**（3 点，约半页），但第 3 点 "follow-up expert review is needed to determine whether flagged items should be retired or retained" 作为 limitation 偏弱——这更像是 future work 而非当前工作的局限。

- **Table 3 格式**：跨 6 个 benchmark 的 C% 比较表很有用，但 "knowledge/reasoning benchmarks" 一列的 footnote 标记 (†) 在表中不明显。

---

## 主要优势

1. **规模与覆盖度出色**：5,227 models × 12,508 items 的分析规模在 IRT-for-LLM 领域最大，且扩展到 6 个 METABENCH benchmark 的交叉验证（Table 3）增强了 generalizability。

2. **Semi-synthetic validation 设计精巧**：Section 3.4 的注入框架提供了 controlled ground truth 来验证 DIF 检测的 sensitivity 和 specificity。Figure 2 的 dose-response curve 清晰展示了 detection power 与 contamination 程度的关系。ΔFPR = 0 的理论保证（cross-subject matching）是一个干净的分析贡献。

3. **多层验证架构可信**：Monte Carlo power analysis (Section 4.1) → temporal DIF detection (4.2) → contamination independence (4.3) → structural controls (4.4) → detection power validation (4.5) → downstream impact (4.6) → cross-benchmark validation (4.7)——实验设计系统性强。

4. **DEFF correction 处理 family dependence 问题得当**：论文明确识别了 LLM model families 的非独立性问题（Section 4.1），引入 design-effect estimators 修正非独立性，这是将 DIF 方法适配到 LLM 场景的正确处理。

5. **附录内容丰富**：18 页论文中 7 页附录覆盖了 method details (A)、mechanism analysis (B)、structural analysis (C)、DEFF estimation (D)、uncertainty quantification (E)，满足 reproducibility 要求。

---

## 缺失的重要参考文献

1. **Test security / item exposure 文献**：教育测量中关于 item exposure control 的文献（如 Hau & Chang, 2001; Way, 1998）直接相关——items "被曝光"到训练数据的概念与 test security 中的 item exposure 高度类似。这类文献可以为 audit protocol 提供更成熟的理论基础。

2. **Polytomous DIF 方法**：论文仅使用 binary DIF (correct/incorrect)。但 MMLU 是 4-choice MCQ，distractor-level analysis 可能揭示更细粒度的 DIF patterns。相关方法如 ordinal logistic regression DIF（French & Miller, 1996）或 Lord's chi-square for polytomous items 值得讨论。

3. **Benchmark dynamics 文献**：Xu et al. (2024, "Benchmark self-evolving") 已被引用，但 benchmark design 领域关于 item banking 和 equating 的文献（如 Kolen & Brennan, 2014, "Test Equating, Scaling, and Linking"——已引用但可以更深入讨论其 equating 方法论对 LLM benchmarks 的适用性）可以强化 Section 5.2 的 audit protocol。

4. **Multi-group CFA / MIMIC models for MI testing**：论文引用了 Meredith (1993) 但只讨论了 DIF 检测。Measurement invariance 检验在 SEM 框架下有更完整的理论体系（configural → metric → scalar invariance），讨论这些会让 Section 2 的 related work 在 MI 维度上更完整。

---

## Questions for Authors

1. 如果使用 Time Travel (Golchin & Surdeanu, 2024) 或 LLM memorization scores (Dekoninck et al., 2024) 作为替代 contamination proxy，DIF flags 与这些 labels 的 Jaccard 是否仍然 ~0.20？这对 "near-independence" claim 至关重要。

2. 论文在 Appendix A.2 提到 1PL model 对 MMLU response matrix poor fit。是否尝试过 2PL model？如果 item discrimination 参数变异很大，MH-DIF 的 uniform DIF 假设可能不成立，这会影响 power 和 Type I error。

3. Section 5.2 的 audit protocol 建议 "periodic psychometric audits alongside score reporting"。是否有关于审计频率的具体建议？每隔多少新模型加入后应触发审计？

4. Cross-subject matching 的 ΔFPR=0 保证依赖于 "contamination 仅影响单一 subject"（k ≤ 5）的假设。在实际场景中，training data contamination 可能影响多个 subjects（如 internet-scale pre-training），Table 7 的 multi-subject injection robustness 分析在 k=20 时 ΔFPR 升至 0.018——如何判断现实中 contamination 的跨 subject spread 程度？

---

**总结**：论文在规模、实验系统性和 semi-synthetic validation 上表现优秀，核心实证发现（temporal DIF 大量存在且与 web-overlap 标签正交）对社区有价值。主要短板是方法论创新有限（MH-DIF 直接搬运）和 contamination independence claim 的 proxy 质量问题。如果作者能更好地论证 LLM-specific methodological adaptations 的非平凡性，并对 contamination proxy 的局限性做坦诚讨论，论文有潜力达到 Conference 水平；否则 Findings 是更合适的归宿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1673 · 2026-05-23T14:05:29.685135+00:00_

Reviewer 2 报告已收到（3.5 分，Borderline Conference）。等待 Reviewer 1 报告中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 161

## Round 161

2 recorded events


### User

_source line 1674 · 2026-05-23T14:05:38.558451+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

**核心判断**：Overall 3.5 (Borderline Conference)。

两个 Must-Fix：
1. 方法论新颖性不足——MH-DIF 是 40 年前标准方法的直接搬运，cross-subject matching 是 purified subtest matching 的直接推广
2. "DIF 与 contamination 正交"的 headline finding 依赖质量存疑的 web-overlap proxy（Li et al. 2024b），Jaccard ≈ 0.20 可能反映 proxy 低质量而非真正的独立性

五个 Should-Fix：ETS 阈值未经 LLM 校准验证、与 Growing Pains 差异化不足、temporal framing 过窄（实为 cohort-based DIF）、因果性暗示过度、score correction 展示太薄。

主要优势：5,227 模型的分析规模出色、semi-synthetic validation 设计精巧、DEFF correction 处理 family dependence 得当、7 页附录覆盖充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1675 · 2026-05-23T14:05:44.602281+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 162

## Round 162

6 recorded events


### User

_source line 1676 · 2026-05-23T14:08:01.151771+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查报告

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 将 MH-DIF 应用于 5,227 LLMs 的大规模 psychometric audit 方法论基本可靠，cross-subject matching 是有价值的方法论贡献，但 DEFF 校正的 2.16× 不确定性范围、半合成注入框架的生态效度不足、以及缺少 DIF 文献中 impact/bias 关键区分是三个影响接收决定的方法论缺陷。

## 官方维度打分（ACL ARR review form, Feb 2025+）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | MH-DIF 应用正确，cross-subject matching 有方法论贡献，但 DEFF 估计范围过宽（13.5%–29.2%）且半合成验证生态效度不足 |
| Excitement | 3.5/5 | DIF 与 contamination 近正交（Jaccard=0.206）的发现有重要意义，但实践可操作性尚需更多论证 |
| Reproducibility | 4/5 | 使用公开数据集 METABENCH，方法描述详尽，代码脚本声明可用 |
| Confidence | 4/5 | 对统计方法论和 psychometrics 有充分了解，仔细阅读了正文和全部 18 页附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DEFF 校正产生 2.16× 估计范围，论文未提供充分的分辨依据
- 具体位置：Section D (Appendix, p.15)；正文 Section 4.2 (p.6) 报告 "13.5–29.2%"
- 问题：Simple-mean DEFF (3.58) 给出 C% = 29.2%，weighted-mean DEFF (12.29) 给出 C% = 13.5%——差距超过 2 倍。论文将两者作为 "bracket" 呈现，但未提供在此区间内定位的原则性依据。Cluster bootstrap 95% CI [26.7%, 53.2%] 被用来排除 13.5% 下界，但 bootstrap 仅对约 30 个 family 重采样（其中 Mistral n=547、Llama-3 n=315 占据主导），有效独立重采样单元极少。论文自己也承认 "extreme bootstrap upper bound (53.2%) is driven by extreme bootstrap resamples that over-represent Mistral or Llama-3"（p.16），这意味着 bootstrap 分布受少数 mega-family 驱动，推断可靠性存疑。
- 为什么影响接收：论文核心定量发现是 "17.9–31.3% of items exhibit temporal DIF"（Abstract, Conclusion 均引用此数字）。如果实际值接近 13.5%（weighted-mean），DIF 的规模和实践影响将大幅缩水，"Correct" 步骤移除的 item 数量和 rescoring 幅度也会显著不同。
- 建议修改方向：(1) 对 family 定义进行 sensitivity analysis——用更细粒度的分组（如 fine-tune chain、base model version）和更粗粒度的分组分别估计 DEFF，展示 C% 对 family 粒度的敏感性曲线；(2) 报告 block bootstrap with varying block size 或 jackknife-after-bootstrap 结果，评估 cluster bootstrap CI 本身的稳定性；(3) 如果无法缩窄区间，至少应在正文 Discussion 中充分讨论这一不确定性的实践含义，而非仅在 Appendix D 中处理。

**N2** [critical] 半合成注入框架使用 uniform binary flipping，检测力估计可能被系统性高估
- 具体位置：Section 3.4 (p.5)；Section 4.5 (p.7)；Limitations (p.9)
- 问题：注入框架将 "contamination" 操作化为二元翻转（incorrect → correct），产生最大化的 per-item DIF effect size。现实中 contamination 更可能表现为 graded probability shift（partial memorization：模型对见过的题目正确率从 0.4 提高到 0.7，而非从 0 跳到 1）。论文报告的 ΔTPR = 0.371（MMLU，Section 4.5）代表 binary-flip 下的 best-case 检测力。虽然 Scheme D（difficulty-dependent injection）展示了 ΔTPR 从 0.51 降至约 0.41，但这仍是 binary flipping 的变体（仅 injection rate 随 difficulty 变化），未测试 graded probability shift 场景。Limitations（p.9）正确承认了这一点但未量化影响。
- 为什么影响接收：论文第二个核心贡献（cross-subject matching with constructive ΔFPR=0 guarantee）和实践建议（Section 5.2 Monitor/Triage/Correct 协议）的可行性都取决于有足够的检测力。如果 graded injection 下 ΔTPR 降至 0.1–0.2 级别，审计框架的实际可用性将大打折扣。
- 建议修改方向：(1) 增加 graded injection scheme：将 p(correct) 从 baseline 提升 Δp ∈ {0.1, 0.2, 0.3}，而非 binary flip，报告不同 Δp 下的 ΔTPR 曲线和 "minimum detectable probability shift"；(2) 若实验资源不足，至少用数学推导估计 graded shift 对 MH odds ratio 的影响幅度，提供 analytical bound。

**N3** [critical] 缺少 DIF 文献中的 "impact vs. bias" 关键区分，威胁 "Correct" 步骤的方法论基础
- 具体位置：Section 5.2 (p.8)；Section M (p.18, score inflation analysis)
- 问题：DIF 文献（Camilli & Shepard, 1994; Zumbo, 1999; Penfield & Camilli, 2007）明确区分 DIF（统计发现：能力匹配后 item 在组间表现不同）和 item bias（实质性判断：差异由 construct-irrelevant 因素导致）。DIF 是 bias 的必要但非充分条件。如果 2024 models 在特定推理能力上有真实进步，导致特定 items 上的 performance shift，这属于 "impact"（construct-relevant differential functioning），移除这些 items 反而会降低 benchmark 对真实能力差异的敏感度。论文的 "Correct" 步骤（Section 5.2）直接建议 "removing ETS C items and rescoring"，Section M 报告 "+2.12 pp" score shift，但未区分 impact-driven vs. bias-driven DIF items。论文自己在 Section B (Appendix) 承认 "capability evolution" 是三个可能机制之一——如果部分 DIF 确实由 capability evolution 驱动，indiscriminate removal 在方法论上不成立。
- 为什么影响接收：这不仅是讨论层面的缺失，而是论文方法论框架的内在一致性问题。一方面声称 "mechanism-agnostic"，另一方面建议无差别移除 DIF items——两者逻辑冲突。
- 建议修改方向：(1) 在 Section 5.2 引入 impact/bias 区分，讨论 Triage 步骤应如何 operationalize（例如：DIF 方向与 domain-specific ability gain 一致时可能是 impact，与 web-overlap 一致时更可能是 bias）；(2) 在 Section M 中分别报告 impact-candidate 和 bias-candidate items 的 rescoring 效应；(3) 引用 DIF 文献中的标准做法：DIF detection → expert content review → bias determination → removal decision，而非跳过中间步骤。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Calendar-year cohort boundary 过于粗糙
- 具体位置：Section 3.3 (p.5)；Limitations (p.9)
- 问题：以 calendar year（2023 vs 2024）划分 cohort，但 release date ≠ training data cutoff。2024 年初发布的模型可能使用 2022 年的训练数据。Appendix（p.16）的 half-year granularity 分析（31.3% annual vs 34.1% half-year）仅提供了有限额外信息。
- 建议：(1) 对有 training cutoff 元数据的子集进行 sensitivity analysis；(2) 报告 quarterly cohort 的 C% 趋势以验证 temporal monotonicity。

**W2** [warning] Cross-subject matching ΔFPR=0 保证在高覆盖率 contamination 下的退化未充分讨论
- 具体位置：Section 4.5 (p.7)；Table 7
- 问题：ΔFPR=0 保证仅在 k≤5 科目同时被 contaminate 时严格成立。k=10 时 ΔFPR=0.012–0.018，k=20 时 ΔFPR=0.062。论文正文称 "worst-case multi-subject inflation (~7 pp) cannot account for the observed 31% C% rate"，但此论证将 worst-case per-item FPR 与 aggregate C% 对比，未考虑在 "realistic web contamination coverage"（可能影响 30+ 科目）下的累积效应。
- 建议：模拟在 k=30（~53% 科目）甚至 k=50 时的 ΔFPR，并讨论是否改变定性结论。

**W3** [warning] Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力
- 具体位置：Section 1 (p.1-2)；Section 4.3 (p.6-7)；Section 5.1 (p.8)；Figure 1
- 问题：论文明确宣称 "mechanism-agnostic"（Section 5.1: "Temporal DIF detects that items function differently across cohorts, not why"），但叙事结构大量围绕 contamination 展开：Related Work 以 "Contamination Detection" 开篇，Figure 1 左图标注 "global contamination"，Section 4.3 整节做 DIF-contamination 对比。这种张力可能让读者误读为 "DIF 是更好的 contamination detector"，与论文实际贡献（measurement invariance diagnostic）不一致。
- 建议：将 contamination 对比重新框定为 "discriminant validity evidence"（证明 DIF 度量的构念不同于 contamination），而非暗示两者在同一维度上竞争。

**W4** [warning] METABENCH 数据的 selection bias 未充分讨论
- 具体位置：Section 3.1 (p.4)
- 问题：所有 5,227 模型来自 Open LLM Leaderboard，存在自选择偏差（只有主动提交的模型被收录）、teaching-to-the-test 效应（Leaderboard 公开后可能诱导针对性训练）、以及 family-level over-representation（某些 family 大量提交微调变体）。DEFF 校正处理了非独立性，但 selection bias 本身未讨论。
- 建议：在 Limitations 中讨论 Leaderboard selection bias 的方向和预期影响。

---

## 小问题（不影响接收）
- Abstract "≤22% benchmarks show above-baseline DIF flags" 表述模糊，建议用 "5 of 6 benchmarks" 或具体比例
- Table 3 (p.8) HellaSwag 的 Enrichment 标 "–"，原因是 Li et al. (2024b) 未覆盖——建议脚注说明
- Figure 2 (p.7) y 轴标签 "True Positive Rate (Power)" 建议统一用 "Detection Power (TPR)" 以匹配正文术语

---

## Questions for Authors
1. 如果用 graded probability injection（Δp=0.2 而非 binary flip），ΔTPR 预期会下降到什么水平？是否做过任何 pilot 实验或 analytical estimation？
2. DEFF 的 family 定义是如何确定的？是否考虑过用 model card 中的 base model 字段构建更细粒度的 fine-tune chain 谱系？如果用 50 个 sub-family 而非 30 个 family，DEFF 会如何变化？
3. Section M 中移除 DIF-C items 后 score shift = +2.12 pp——这意味着 2024 cohort 在 DIF-corrected 后得分更高。但如果 contamination 是主要机制，我们预期移除 contaminated items 后 2024 得分应该下降。论文如何调和这一方向性矛盾？
4. 论文是否能区分 "legitimately harder items for 2024 models"（因为 training methodology shift 导致某些能力退化）和 "construct-irrelevant DIF"？如果不能，"Correct" 步骤的实践建议是否过于简化？

---

## Missing References
- Camilli, G. & Shepard, L. A. (1994). *Methods for Identifying Biased Test Items*. Sage. ——DIF 与 item bias 的经典区分框架
- Penfield, R. D. & Camilli, G. (2007). Differential item functioning and item bias. In *Handbook of Statistics* (Vol. 26). ——impact vs. bias 的方法论框架
- （论文已引用 Millsap 2011、Zumbo 1999，但未利用其中的 impact/bias 区分来支撑 Section 5.2 的实践建议）

---

## 主要优势
- **S1 规模与系统性**：5,227 模型 × 12,508 items 的全量 psychometric audit，据我所知是 LLM 评估领域最大规模的此类分析
- **S2 Cross-subject matching 是真正的方法论贡献**：ΔFPR=0 的构造性保证（k≤5）为 DIF 在多科目 benchmark 上的应用提供了可靠的 FPR 控制，这是对标准 MH-DIF 流程的有价值扩展
- **S3 DIF ⊥ contamination 的发现有重要理论意义**：Jaccard=0.206 表明这两种 diagnostic 维度近正交，挑战了将 item-level anomaly 简单归因于 contamination 的普遍直觉
- **S4 内部一致性控制设计得当**：random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control（Appendix P：30.25% vs 31.3%，仅 1.08 pp 差异）构成多层次 null-hypothesis 校验
- **S5 Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 的强证据**：base models 60.1% reference-favoring vs instruct models 69.6% focal-favoring，有效排除了 DIF 纯粹由单一机制驱动的假设

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1677 · 2026-05-23T14:08:53.955617+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 大规模实证发现有价值（temporal DIF 与 contamination 近乎正交），但核心方法是 off-the-shelf MH-DIF 的直接搬运，方法论创新不足以稳进主会。\n\n## Must-Fix 问题\n\n**N1** [critical] 核心方法论新颖性不足——MH-DIF 是 40 年前的标准方法的直接应用\n- Section 3.2 的方法描述本质上是教科书内容——K=5 等频分层、对数 odds ratio、ETS A/B/C 分类标准均原封不动。\n- 第一点贡献（temporal DIF at scale）是实证发现而非方法创新；第二点（cross-subject matching）是 purified subtest matching 的直接推广；第三点（audit protocol）是组合既有步骤。\n- 建议：(a) 更清晰论证 ΔFPR=0 的技术挑战和理论保证；(b) 讨论 4 个 LLM-specific challenges 构成真正的方法适配贡献；(c) 增加与 logistic regression DIF 的比较。\n\n**N2** [critical] \"DIF 与 contamination 近乎独立\"的核心发现依赖质量存疑的 proxy\n- Web-overlap labels 来自 Li et al. (2024b)，仅检测 items 是否在公开网络语料中出现——非常粗糙的 contamination proxy。\n- (1) Web-overlap ≠ 实际训练数据包含；(2) 许多 contamination 来源不会被 web-overlap 捕获；(3) Li et al. labels 覆盖率仅 73.8%。\n- Jaccard ≈ 0.20 可能仅反映 web-overlap labels 的低质量，而非 DIF 与真正 contamination 的独立性。\n- 建议：使用多种 contamination 指标交叉验证；将结论软化为 \"DIF is independent of web-overlap based contamination labels\"。\n\n## Should-Fix 问题\n\n**W1** [warning] ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证\n- LLM 没有 guessing behavior，能力维度可能高度多维。\n- 建议通过 simulation 验证 ETS 阈值在 LLM response matrix 下的 Type I error 和 power。\n\n**W2** [warning] 与 Growing Pains (Habba et al., 2026) 的差异化论证不够深入\n- 差异化主要停留在方法层面（MH-DIF vs. fixed-parameter calibration），缺少在相同数据/相同 items 上的直接比较。\n- 建议在附录中加入交叉比较。\n\n**W3** [warning] \"Temporal\" framing 可能过窄——实际检测到的是 cohort-based DIF\n- 2023 vs. 2024 cohorts 不仅在时间上不同，还在架构、数据规模、训练方法上系统性不同。\n- 建议在 Discussion 中更明确讨论 temporal confounding。\n\n**W4** [warning] 因果性过度暗示\n- Abstract \"because item measurement properties differ systematically\" 隐含因果判断。\n- DIF 只能说明 \"items function differently after conditioning on total score\"。\n\n**W5** [warning] Score correction 的实际影响展示不充分\n- Section 4.6 仅半页篇幅，未区分 ranking reversal 发生在 top-10 还是 mid-tier。\n- 建议扩展或加入 case study。\n\n## 主要优势\n1. 规模与覆盖度出色（5,227 models × 12,508 items）\n2. Semi-synthetic validation 设计精巧\n3. 多层验证架构可信\n4. DEFF correction 处理 family dependence 得当\n5. 附录内容丰富\n\n## 缺失的重要参考文献\n1. Test security / item exposure 文献（Hau & Chang, 2001; Way, 1998）\n2. Polytomous DIF 方法（French & Miller, 1996）\n3. Benchmark dynamics 中 item banking 和 equating 的文献\n4. Multi-group CFA / MIMIC models for MI testing\n\n---\n\n请逐条回应 R2 的每个 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 大规模实证发现有价值（temporal DIF 与 contamination 近乎正交），但核心方法是 off-the-shelf MH-DIF 的直接搬运，方法论创新不足以稳进主会。\n\n## Must-Fix 问题\n\n**N1** [critical] 核心方法论新颖性不足——MH-DIF 是 40 年前的标准方法的直接应用\n- Section 3.2 的方法描述本质上是教科书内容——K=5 等频分层、对数 odds ratio、ETS A/B/C 分类标准均原封不动。\n- 第一点贡献（temporal DIF at scale）是实证发现而非方法创新；第二点（cross-subject matching）是 purified subtest matching 的直接推广；第三点（audit protocol）是组合既有步骤。\n- 建议：(a) 更清晰论证 ΔFPR=0 的技术挑战和理论保证；(b) 讨论 4 个 LLM-specific challenges 构成真正的方法适配贡献；(c) 增加与 logistic regression DIF 的比较。\n\n**N2** [critical] \"DIF 与 contamination 近乎独立\"的核心发现依赖质量存疑的 proxy\n- Web-overlap labels 来自 Li et al. (2024b)，仅检测 items 是否在公开网络语料中出现——非常粗糙的 contamination proxy。\n- (1) Web-overlap ≠ 实际训练数据包含；(2) 许多 contamination 来源不会被 web-overlap 捕获；(3) Li et al. labels 覆盖率仅 73.8%。\n- Jaccard ≈ 0.20 可能仅反映 web-overlap labels 的低质量，而非 DIF 与真正 contamination 的独立性。\n- 建议：使用多种 contamination 指标交叉验证；将结论软化为 \"DIF is independent of web-overlap based contamination labels\"。\n\n## Should-Fix 问题\n\n**W1** [warning] ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证\n- LLM 没有 guessing behavior，能力维度可能高度多维。\n- 建议通过 simulation 验证 ETS 阈值在 LLM response matrix 下的 Type I error 和 power。\n\n**W2** [warning] 与 Growing Pains (Habba et al., 2026) 的差异化论证不够深入\n- 差异化主要停留在方法层面（MH-DIF vs. fixed-parameter calibration），缺少在相同数据/相同 items 上的直接比较。\n- 建议在附录中加入交叉比较。\n\n**W3** [warning] \"Temporal\" framing 可能过窄——实际检测到的是 cohort-based DIF\n- 2023 vs. 2024 cohorts 不仅在时间上不同，还在架构、数据规模、训练方法上系统性不同。\n- 建议在 Discussion 中更明确讨论 temporal confounding。\n\n**W4** [warning] 因果性过度暗示\n- Abstract \"because item measurement properties differ systematically\" 隐含因果判断。\n- DIF 只能说明 \"items function differently after conditioning on total score\"。\n\n**W5** [warning] Score correction 的实际影响展示不充分\n- Section 4.6 仅半页篇幅，未区分 ranking reversal 发生在 top-10 还是 mid-tier。\n- 建议扩展或加入 case study。\n\n## 主要优势\n1. 规模与覆盖度出色（5,227 models × 12,508 items）\n2. Semi-synthetic validation 设计精巧\n3. 多层验证架构可信\n4. DEFF correction 处理 family dependence 得当\n5. 附录内容丰富\n\n## 缺失的重要参考文献\n1. Test security / item exposure 文献（Hau & Chang, 2001; Way, 1998）\n2. Polytomous DIF 方法（French & Miller, 1996）\n3. Benchmark dynamics 中 item banking 和 equating 的文献\n4. Multi-group CFA / MIMIC models for MI testing\n\n---\n\n请逐条回应 R2 的每个 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1678 · 2026-05-23T14:09:21.023848+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27068
}
```

</details>

---


### Tool call

_source line 1679 · 2026-05-23T14:09:21.226127+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查报告\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: MH-DIF 应用方法论基本可靠，cross-subject matching 是有价值的方法论贡献，但 DEFF 校正的 2.16× 不确定性范围、半合成注入框架的生态效度不足、以及缺少 DIF 文献中 impact/bias 关键区分是三个影响接收决定的方法论缺陷。\n\n## Must-Fix 问题\n\n**N1** [critical] DEFF 校正产生 2.16× 估计范围，论文未提供充分的分辨依据\n- Simple-mean DEFF (3.58) → C% = 29.2%；weighted-mean DEFF (12.29) → C% = 13.5%\n- Cluster bootstrap 95% CI [26.7%, 53.2%] 被用来排除 13.5%，但 bootstrap 仅对约 30 个 family 重采样，有效独立重采样单元极少\n- 建议：family 定义 sensitivity analysis；block bootstrap with varying block size；正文 Discussion 中充分讨论不确定性的实践含义\n\n**N2** [critical] 半合成注入框架使用 uniform binary flipping，检测力估计可能被系统性高估\n- 现实中 contamination 更可能表现为 graded probability shift（partial memorization）\n- 虽有 Scheme D（difficulty-dependent injection）但仍是 binary flipping 的变体\n- 建议：增加 graded injection scheme（Δp ∈ {0.1, 0.2, 0.3}），报告 minimum detectable probability shift\n\n**N3** [critical] 缺少 DIF 文献中的 \"impact vs. bias\" 关键区分\n- DIF 是 bias 的必要但非充分条件\n- 如果 2024 models 在推理能力上有真实进步导致 performance shift，这属于 \"impact\"（construct-relevant），移除会降低 benchmark 敏感度\n- \"Correct\" 步骤直接建议移除 ETS C items，但未区分 impact-driven vs. bias-driven\n- 一方面声称 \"mechanism-agnostic\"，另一方面建议无差别移除——逻辑冲突\n- 建议：引入 impact/bias 区分；分别报告 impact-candidate 和 bias-candidate 的 rescoring 效应；引用 DIF → expert review → bias determination → removal 的标准做法\n\n## Should-Fix 问题\n\n**W1** [warning] Calendar-year cohort boundary 过于粗糙\n- Release date ≠ training data cutoff。建议对有 training cutoff 元数据的子集做 sensitivity analysis。\n\n**W2** [warning] Cross-subject matching ΔFPR=0 保证在高覆盖率 contamination 下的退化未充分讨论\n- k=10 时 ΔFPR=0.012–0.018，k=20 时 ΔFPR=0.062。未模拟 k=30 或 k=50 场景。\n\n**W3** [warning] Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力\n- Related Work 以 \"Contamination Detection\" 开篇，Figure 1 标注 \"global contamination\"，Section 4.3 整节做 DIF-contamination 对比。\n- 建议将 contamination 对比重新框定为 \"discriminant validity evidence\"。\n\n**W4** [warning] METABENCH 数据的 selection bias 未充分讨论\n- 所有模型来自 Open LLM Leaderboard，存在自选择偏差。\n\n## 主要优势\n- S1: 5,227 模型的大规模 psychometric audit\n- S2: Cross-subject matching ΔFPR=0 是真正的方法论贡献\n- S3: DIF ⊥ contamination 的发现有重要理论意义\n- S4: 多层 null-hypothesis 校验设计得当\n- S5: Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 强证据\n\n## Missing References\n- Camilli & Shepard (1994) — DIF 与 item bias 的经典区分\n- Penfield & Camilli (2007) — impact vs. bias 方法论框架\n\n---\n\n请逐条回应 R1 的每个 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查报告\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: MH-DIF 应用方法论基本可靠，cross-subject matching 是有价值的方法论贡献，但 DEFF 校正的 2.16× 不确定性范围、半合成注入框架的生态效度不足、以及缺少 DIF 文献中 impact/bias 关键区分是三个影响接收决定的方法论缺陷。\n\n## Must-Fix 问题\n\n**N1** [critical] DEFF 校正产生 2.16× 估计范围，论文未提供充分的分辨依据\n- Simple-mean DEFF (3.58) → C% = 29.2%；weighted-mean DEFF (12.29) → C% = 13.5%\n- Cluster bootstrap 95% CI [26.7%, 53.2%] 被用来排除 13.5%，但 bootstrap 仅对约 30 个 family 重采样，有效独立重采样单元极少\n- 建议：family 定义 sensitivity analysis；block bootstrap with varying block size；正文 Discussion 中充分讨论不确定性的实践含义\n\n**N2** [critical] 半合成注入框架使用 uniform binary flipping，检测力估计可能被系统性高估\n- 现实中 contamination 更可能表现为 graded probability shift（partial memorization）\n- 虽有 Scheme D（difficulty-dependent injection）但仍是 binary flipping 的变体\n- 建议：增加 graded injection scheme（Δp ∈ {0.1, 0.2, 0.3}），报告 minimum detectable probability shift\n\n**N3** [critical] 缺少 DIF 文献中的 \"impact vs. bias\" 关键区分\n- DIF 是 bias 的必要但非充分条件\n- 如果 2024 models 在推理能力上有真实进步导致 performance shift，这属于 \"impact\"（construct-relevant），移除会降低 benchmark 敏感度\n- \"Correct\" 步骤直接建议移除 ETS C items，但未区分 impact-driven vs. bias-driven\n- 一方面声称 \"mechanism-agnostic\"，另一方面建议无差别移除——逻辑冲突\n- 建议：引入 impact/bias 区分；分别报告 impact-candidate 和 bias-candidate 的 rescoring 效应；引用 DIF → expert review → bias determination → removal 的标准做法\n\n## Should-Fix 问题\n\n**W1** [warning] Calendar-year cohort boundary 过于粗糙\n- Release date ≠ training data cutoff。建议对有 training cutoff 元数据的子集做 sensitivity analysis。\n\n**W2** [warning] Cross-subject matching ΔFPR=0 保证在高覆盖率 contamination 下的退化未充分讨论\n- k=10 时 ΔFPR=0.012–0.018，k=20 时 ΔFPR=0.062。未模拟 k=30 或 k=50 场景。\n\n**W3** [warning] Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力\n- Related Work 以 \"Contamination Detection\" 开篇，Figure 1 标注 \"global contamination\"，Section 4.3 整节做 DIF-contamination 对比。\n- 建议将 contamination 对比重新框定为 \"discriminant validity evidence\"。\n\n**W4** [warning] METABENCH 数据的 selection bias 未充分讨论\n- 所有模型来自 Open LLM Leaderboard，存在自选择偏差。\n\n## 主要优势\n- S1: 5,227 模型的大规模 psychometric audit\n- S2: Cross-subject matching ΔFPR=0 是真正的方法论贡献\n- S3: DIF ⊥ contamination 的发现有重要理论意义\n- S4: 多层 null-hypothesis 校验设计得当\n- S5: Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 强证据\n\n## Missing References\n- Camilli & Shepard (1994) — DIF 与 item bias 的经典区分\n- Penfield & Camilli (2007) — impact vs. bias 方法论框架\n\n---\n\n请逐条回应 R1 的每个 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1680 · 2026-05-23T14:09:22.697938+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1471
}
```

</details>

---


### Assistant

_source line 1681 · 2026-05-23T14:09:27.209913+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 163

## Round 163

2 recorded events


### User

_source line 1682 · 2026-05-23T14:09:29.818861+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.5 (Borderline Conference)**。三个 Must-Fix 问题：(1) DEFF 校正的 2.16× 估计范围（13.5% vs 29.2%）缺乏分辨依据；(2) 半合成注入用 binary flipping 而非 graded probability shift，检测力估计可能被系统性高估；(3) 缺少 DIF 文献中 impact/bias 的经典区分，导致 "Correct" 步骤（无差别移除 DIF items）与 mechanism-agnostic 定位之间存在逻辑冲突。四个 Should-Fix：calendar-year cohort 粒度粗糙、cross-subject matching 在高覆盖率下退化、contamination-heavy 叙事与 mechanism-agnostic 定位的张力、METABENCH selection bias 未讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1683 · 2026-05-23T14:09:40.294931+00:00_

等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 164

## Round 164

2 recorded events


### User

_source line 1684 · 2026-05-23T14:10:44.281176+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: 核心方法论新颖性不足——MH-DIF 是 off-the-shelf 的直接搬运**

R2 的批评部分成立但整体过度。需要区分三个层次：

(1) MH-DIF 本身确实是标准方法——这点没有争议。但论文的方法论贡献不在于 MH-DIF 本身，而在于**将其适配到 LLM evaluation 的特殊结构**。Section 3.2（p.4-5）明确列出 4 个 LLM-specific challenges：local independence violation（模型不是独立考生）、permutation simulation 验证（1,000 replications, Section 4.1）、fine-tuned variants within model families 造成 family structure、MMLU 57-subject 多维结构。这些不是教科书内容——教科书处理的是人类考生的 i.i.d. 假设，不涉及 family-level DEFF 校正（Section D）。

(2) Cross-subject matching 不是 purified subtest matching 的"直接推广"。标准 purified subtest matching（Swaminathan & Rogers, 1990）从同一测试中剔除 DIF 嫌疑 items 后用剩余 items 做 matching variable。论文的 cross-subject matching（Section 3.4, p.5）完全使用**不同科目**的总分做 matching variable，并给出了 **constructive ΔFPR=0 guarantee**（单科目 contamination 下 matching variable 不包含任何 contaminated item 的信号）。这一保证的证明（p.5 "Remark"段落）依赖于 LLM benchmark 的 multi-subject 结构——这是人类教育测试中没有对应物的特殊构造。

(3) 我同意 R2 关于增加 logistic regression DIF 比较的建议——这确实能强化方法论贡献。但**缺少比较不等于 MH-DIF 应用无新颖性**。

**结论**：R2 的新颖性批评适用于 Section 3.2 的 MH-DIF 核心步骤描述，但不适用于 cross-subject matching、DEFF 校正、和 LLM-specific 适配工作。建议作者在 Introduction 中更清晰地区分"borrowed methodology"和"novel adaptations"，但不应要求以此为由拒稿。

---

**[AGREE] R2-N2: "DIF 与 contamination 近乎独立"依赖质量存疑的 proxy**

这是 R2 最有力的批评，我完全同意。

Web-overlap labels（Li et al., 2024b）检测的是 items 是否在公开网络语料中出现——这与"模型训练数据是否包含该 item"之间存在大量 gap。论文 Section 4.3（p.6-7）自己报告覆盖率为 73.8%（9,229 of 12,508 items），且 web-overlap 只是 contamination 的一个 noisy proxy。Jaccard = 0.206 可能反映的是：(a) DIF 与真实 contamination 确实独立（论文的解释），或 (b) web-overlap labels 噪声太大导致与任何信号的关联都很低。论文未排除解释 (b)。

Section 5.1（p.8）呈现了两种解释（"DIF captures a broader signal" vs. "DIF and contamination detection measure distinct constructs"），但在 Abstract 和 Conclusion 中的措辞更接近单一解释。Abstract 的 "Web-overlap contamination labels are near-independent of DIF flags" 虽然事实正确，但暗示的含义（DIF 检测的不是 contamination）取决于 labels 的质量。

R2 建议将结论软化为 "DIF is independent of web-overlap based contamination labels" 是合理的。我进一步建议：**应在 Section 4.3 中报告 web-overlap labels 自身的 test-retest reliability 或与其他 contamination 指标的交叉验证**，否则读者无法判断低 Jaccard 是信号还是噪声。

---

### Should-Fix

**[AGREE] R2-W1: ETS 阈值从人类测试群体直接迁移到 LLM，缺乏校准验证**

同意。我在自己的审查中也关注了这一问题。论文的 random-split P99=1.45（Section A.2, p.12-13）提供了 empirical calibration——在 2023 cohort 内部随机分割时，99th percentile of |Δ_MH| 恰好略低于 ETS C threshold 1.5，说明阈值在 LLM response matrix 下近似合理。但这只是 necessary condition（null distribution 下不超过阈值），不是 sufficient condition（阈值在 LLM-specific effect size 分布下是否提供 optimal sensitivity-specificity tradeoff）。

R2 建议通过 simulation 验证 Type I error 和 power 是合理的——论文 Section 4.1 的 Monte Carlo power analysis（Table 4-5）已部分完成了这一工作，但未将其明确框定为"ETS 阈值在 LLM 下的校准验证"。建议作者在正文中更明确地连接 Section 4.1 的 power 结果与 ETS 阈值的适用性论证。

---

**[AGREE] R2-W2: 与 Growing Pains 的差异化论证不够深入**

同意，但优先级不高。Growing Pains（Habba et al., 2026）使用 fixed-parameter IRT calibration 检测 temporal instability，与 MH-DIF 是不同的技术路径。Section 2（p.3）提到两者的方法差异，但缺乏在相同 data slice 上的直接比较。作为一个 should-fix 合理，但在 8 页正文空间限制下，附录中的交叉比较可能更可行。

---

**[AGREE] R2-W3: "Temporal" framing 可能过窄——实际是 cohort-based DIF**

同意。我在自己的 W1 中提出了相同的关切。2023 vs 2024 cohorts 在时间、架构偏好、训练方法、数据规模等维度上同时变化，"temporal" 标签暗示时间是主要变量，但实际驱动 DIF 的可能是 cohort composition（例如 2024 instruct models 比例更高）。论文 Appendix P（p.18）的 composition control 分析（balanced C%=30.25% vs raw 31.3%）部分回应了这一关切，但仅控制了 base/instruct 比例，未控制其他 cohort 差异（如平均模型大小、主流架构从 Llama-2 到 Llama-3 的迁移）。

建议作者在 Section 5.1 讨论中明确承认 "temporal" 是 "cohort-based" 的简写，并讨论未控制的 confounders。

---

**[REBUT] R2-W4: Abstract 中 "because" 构成因果性过度暗示**

R2 引用的具体句子是 Abstract 中的 "scores are not directly comparable across cohorts because item measurement properties differ systematically"。我认为这**不构成因果过度暗示**。

这里的 "because" 解释的是**为什么 scores 不可比**（因为 item properties 不同），而非**为什么 item properties 不同**（因为 contamination / capability evolution / methodology shift）。DIF 的存在**在定义上**意味着 measurement properties 在组间不同——这是 DIF 的 definition，不是因果推断。说 "scores are incomparable because items function differently" 等价于说 "measurement invariance is violated, therefore scores are not on a common scale"——这是 psychometrics 中的标准推论链，不涉及 DIF 成因的因果判断。

我在自己的 W3 中确实指出论文在 mechanism-agnostic 定位和 contamination-heavy 叙事之间存在张力，但 R2 所 cite 的这个具体句子不是 problematic 的例子。

---

**[AGREE] R2-W5: Score correction 的实际影响展示不充分**

部分同意，但我认为问题比 R2 描述的更深。R2 关注的是展示不充分（未区分 ranking reversal 的位置），这确实是一个 presentation issue。但更根本的问题是我在 N3 中指出的：**Score correction 缺少 impact/bias 区分作为方法论基础**。在没有区分 impact-driven 和 bias-driven DIF items 的情况下，即使展示了更详细的 ranking reversal，也无法判断 correction 是改善了还是损害了 benchmark 的测量质量。

建议将 R2 的 "展示不足" 和我的 "impact/bias 缺失" 合并处理：先建立 conceptual foundation（哪些 DIF items 应该被移除），再展示移除后的实际影响。

---

### 缺失参考文献

**[REBUT] Polytomous DIF 方法（French & Miller, 1996）**：MMLU 是 4 选 1 多选题，论文使用 binary scoring（correct=1, incorrect=0），polytomous DIF 方法不适用。这不是缺失。

**[AGREE] Test security / item exposure 文献**：Hau & Chang (2001) 等 item exposure control 文献与 benchmark maintenance 高度相关，建议在 Section 5.2 audit protocol 讨论中引用。

**[REBUT] Multi-group CFA / MIMIC models**：论文 Section 2（p.3）已引用 MIMIC models 文献并解释了选择 MH-DIF 而非 parametric MI testing 的理由（MH-DIF 是非参数方法，不依赖 IRT model fit，而 MMLU response matrix 对 uni-dimensional 2PL fit 较差——Section A.1, p.13）。multi-group CFA 要求可接受的 model fit 作为前提，在 57-subject MMLU 上不现实。这个选择有充分的方法论理由。

**[AGREE] Benchmark dynamics 中的 item banking/equating 文献**：这与 Section 5.2 的 audit protocol 直接相关——DIF detection → item banking → equated scoring 是教育测量的标准流程。引用 equating 文献能强化 Section 5.2 的实践建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1685 · 2026-05-23T14:10:49.084463+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 165

## Round 165

2 recorded events


### User

_source line 1686 · 2026-05-23T14:10:57.290630+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (新颖性不足)**：[REBUT] — cross-subject matching 的 ΔFPR=0 保证和 DEFF 校正是 LLM-specific 的真正方法论贡献，不是教科书内容的直接搬运
- **N2 (contamination proxy 质量)**：[AGREE] — web-overlap labels 噪声可能解释低 Jaccard，论文需软化结论
- **W1 (ETS 阈值迁移)**：[AGREE] — random-split P99 是必要但非充分的校准
- **W2 (Growing Pains 对比)**：[AGREE] — 但优先级不高
- **W3 (temporal vs cohort-based)**：[AGREE] — 与我的 W1 一致
- **W4 (因果暗示)**：[REBUT] — Abstract 中的 "because" 解释的是不可比性的原因（DIF 的定义），非 DIF 成因的因果判断
- **W5 (score correction 展示)**：[AGREE] — 但更根本的问题是缺少 impact/bias 区分（我的 N3）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1687 · 2026-05-23T14:11:01.845195+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 166

## Round 166

10 recorded events


### User

_source line 1688 · 2026-05-23T14:11:28.441749+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: DEFF 校正 2.16× 估计范围**
同意这是一个实质性问题。论文 Section 4.1 给出 simple-mean DEFF (C%=29.2%) 和 weighted-mean DEFF (C%=13.5%) 两个估计，差距确实达到 2.16 倍。论文选择 weighted-mean 作为保守下界并声称 "all downstream conclusions hold"（p6），但 bootstrap 仅对 ~30 个 families 重采样，有效独立单元极少，CI [26.7%, 53.2%] 的精度存疑。

补充我的发现：这个问题还与论文的 headline number "17.9–31.3%" 相互作用——如果用 weighted-mean DEFF 校正后 C% 低至 13.5%，那么主文反复强调的 "31% items exhibit DIF" 实际上可能被高估了一倍以上。论文在 Abstract 中使用的 "13.5–29.2%" 是 DEFF 校正后的范围，但在多处讨论中倾向于引用未校正或仅 simple-mean 校正后的上界。建议作者在正文中更一致地使用 bracketed range 而非 point estimate。

R1 建议的 family 定义 sensitivity analysis 和 block bootstrap with varying block size 都是合理的改进方向。

---

**[AGREE] R1-N2: Semi-synthetic injection 的 binary flipping 局限性**
同意。论文 Section 3.4 的注入框架（包括 Scheme D difficulty-dependent injection）本质上都是 binary flipping——一个 item 要么被完全"解决"（flip 0→1），要么不受影响。现实中的 contamination/memorization 更可能表现为概率偏移——模型因接触过相似训练数据而有更高（但非 100%）的正确概率。

补充：这个问题直接影响论文 Figure 2 dose-response curve 的可信度。如果实际效应是 graded shift (Δp=0.1–0.3) 而非 binary flip，MH-DIF 的 detection power 可能显著低于论文报告的 TPR。论文 Limitations 第 1 点提到 "binary response framework" 和 "stylized injection model"，但将其影响方向简化为 "ΔTPR values may overestimate detection power"——考虑到 graded shift 在小效应量下可能完全无法被 MH 捕获，这个局限可能比论文承认的更严重。

R1 建议的 graded injection scheme (Δp ∈ {0.1, 0.2, 0.3}) 和 minimum detectable probability shift 报告是切实可行的补充实验。

---

**[AGREE] R1-N3: 缺少 impact vs. bias 关键区分**
强烈同意，这是 R1 提出的最有力的批评。DIF 文献中 impact/bias 区分是核心概念（Camilli & Shepard, 1994）：DIF 是 bias 的必要但非充分条件。如果 2024 cohort 模型在某些能力维度上有真实进步（如数学推理），那些 items 上的 DIF 是 construct-relevant 的 "impact"，移除它们反而会降低 benchmark 的区分度。

论文的逻辑确实存在 R1 指出的矛盾：
- Section 5.1 声称 "mechanism-agnostic"（"DIF detects that items function differently…not why"）
- 但 Section 5.2 的 "Correct" 步骤建议直接移除 ETS C items
- Limitations 第 3 点又承认 "follow-up expert review is needed to determine whether flagged items should be retired or retained"

这三处形成了一个内部张力：如果 mechanism-agnostic 是设计选择，那么 audit protocol 不应包含无差别移除步骤；如果需要 expert review 才能决定是否移除，那么 "Correct" 步骤的 framing 就过于 prescriptive。

R1 建议的引用 DIF → expert review → bias determination → removal 的标准流程，以及分别报告 impact-candidate 和 bias-candidate 的 rescoring 效应，都会显著提升论文的方法论严谨性。这与我在 W4 中提出的因果性过度暗示问题一脉相承。

R1 推荐的 Camilli & Shepard (1994) 和 Penfield & Camilli (2007) 确实是该领域的关键参考文献，论文应当引用。

---

### Should-Fix 问题

**[AGREE] R1-W1: Calendar-year cohort boundary 过于粗糙**
同意。这与我在 W3 中提出的问题高度重合——"temporal" 实际上是 cohort-based，而 cohort 的定义（calendar-year release date）与 training data cutoff 可能存在系统性偏差。论文 Section 3.3 列出了 5 种 cohort design（temporal, ability-quintile, generational, within-family, random split），但所有非 random 的 cohort design 都基于 release date。

补充：2024 年发布的模型可能使用 2022–2023 年的 training data cutoff，而 2023 年发布的模型可能使用 2021–2022 年的数据。这意味着论文检测到的 "temporal DIF" 部分反映的是 training data vintage 的差异而非时间本身的效应。R1 建议的对有 training cutoff 元数据的子集做 sensitivity analysis 是可行且必要的。

---

**[AGREE] R1-W2: Cross-subject matching ΔFPR 在高 k 下的退化**
同意。Table 7 显示 k=20 时 ΔFPR 已达 0.062，但论文未模拟更极端的 k=30 或 k=50 场景。我在 Q4 中也提出了类似问题——在 internet-scale pre-training 下，contamination 可能同时影响大量 subjects。

补充：MMLU 有 57 个 subjects。如果 contamination 覆盖 30+ subjects（对于大规模预训练语料并非不可能），cross-subject matching 的理论保证实际上已经失效。论文应明确给出 ΔFPR=0 保证成立的 k 上界的实际含义，以及在超出该范围时推荐的替代策略。

---

**[AGREE] R1-W3: Mechanism-agnostic 与 contamination-heavy 叙事的张力**
同意。论文在叙事上的双重定位确实造成混乱：
- Related Work（Section 2）以 "Contamination Detection" 开篇
- Figure 1 标注 "global contamination" vs "differential contamination"
- Section 4.3 专门做 DIF-contamination 对比
- 但同时声称 DIF 是 mechanism-agnostic 的

R1 建议将 contamination 对比重新框定为 "discriminant validity evidence" 是精准的：论文不是在说 DIF 能检测 contamination，而是在说 DIF 检测到的信号与 contamination proxy 是不同的东西——这恰恰是 discriminant validity 的定义。这个 reframing 同时解决了我在 N2（contamination proxy 质量）和 W4（因果暗示）中的部分担忧。

---

**[REBUT] R1-W4: METABENCH selection bias**
部分不同意 R1 对这个问题严重性的评估。

R1 指出所有模型来自 Open LLM Leaderboard 存在 self-selection bias——表现差的模型可能不被提交。这个观察本身正确，但对 DIF 分析的影响取决于一个关键问题：selection bias 是否在 2023 和 2024 cohorts 之间存在差异？

DIF 分析的核心是比较两个 groups 在 matching variable conditioning 后的 item response。如果 self-selection bias 在两个 cohorts 中大致相同（即两个时期的模型开发者都有类似的 "只提交表现好的模型" 倾向），那么 selection bias 是一个 common factor，不会产生 artifactual DIF。

论文 Section 4.4 的 structural controls 和 Table 2（θ-conditioning 作为 sensitivity check）实际上部分回应了这个问题——通过 ability matching 控制后的 DIF 结果保持稳健。此外，5,227 个模型的样本量已经覆盖了 Leaderboard 上的大部分提交（不仅仅是 top-performing 模型），selection bias 的实际影响可能有限。

不过我同意论文应在 Limitations 或 Section 3.1 中简要讨论这一点。

---

### 关于 R1 推荐的缺失参考文献

**[AGREE]** Camilli & Shepard (1994) 和 Penfield & Camilli (2007) 确实是 DIF 领域的核心文献，特别是 impact/bias 区分。论文引用了大量 DIF 方法论文献（Holland & Thayer, 1988; Donoghue & Allen, 1993; Swaminathan & Rogers, 1990 等），但恰恰遗漏了这两部讨论 DIF 解释框架的关键著作，导致 N3 中 impact/bias 区分的缺失。

---

### 与 R2 自身审稿意见的交叉总结

R1 和 R2 的审稿意见在以下关键点上高度一致：
1. **方法论新颖性有限**（R2-N1 + R1 整体评价）
2. **Contamination proxy 质量问题**（R2-N2 ↔ R1-N3 的 impact/bias 讨论相互补充）
3. **Temporal framing 过窄**（R2-W3 ≈ R1-W1）
4. **叙事定位的内部张力**（R2-W4 ≈ R1-W3）
5. **Cross-subject matching 在高 contamination 下的退化**（R2-Q4 ≈ R1-W2）

R1 独特贡献了三个 R2 未覆盖的重要问题：
- DEFF 校正的不确定性范围（N1）——这是一个我在审查中未充分关注的统计严谨性问题
- Impact vs. bias 区分（N3）——这是最有力的批评，直接影响 audit protocol 的逻辑完整性
- Binary flipping vs. graded injection 的生态效度（N2）——补充了我对 semi-synthetic framework 的评价

**综合两位 Reviewer 意见后的评分调整**：维持 Overall 3.5 (Borderline Conference)。R1 的 N3 (impact/bias) 加强了我对论文审计协议逻辑完整性的担忧，但论文的规模、实验系统性和 cross-subject matching 贡献仍然是实质性的优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1689 · 2026-05-23T14:11:57.784768+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1690 · 2026-05-23T14:11:57.986071+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:58:36.746681+00:00\", \"completed_at\": \"2026-05-23T14:02:01.711581+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页无任何 figure/table（仅 p4 有 2 个公式），整个 Method 章节（§3）缺乏视觉锚点，审稿人在此区间容易产生阅读疲劳。建议在 §3 中加入一个方法流程概览图（pipeline/framework diagram）打破文字单调感\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 2 + Table 1 + Table 2 三个 display items 堆积在同一页，与前 4 页的纯文本形成强烈节奏失衡。建议将 Table 1 或 Table 2 前移至 §3 末尾或 §4 开头（如果 LaTeX float 允许），分散视觉密度\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 部分单元格文字偏小（Cohort Definition 列），边界可读但在打印时可能吃力。考虑缩减列宽或将次要列移入附录\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 x 轴标签 \\\"Exploitation Rate (p)\\\" 字号偏小，建议适当放大\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 5 个 display items / 8 页 = 0.625/页，对实证为主的论文偏少。附录有 12+ 表 + 4 图，部分关键结果（如 Table 4 的 power sensitivity 或 Figure 4 的 ranking impact）可考虑提升到主文以增强说服力\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 作为视觉锚点效果优秀——ICC 示意图直观传达核心概念，caption 自包含，审稿人第一印象正面\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1691 · 2026-05-23T14:11:57.986459+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1692 · 2026-05-23T14:11:57.986864+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1693 · 2026-05-23T14:14:28.521556+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 19 issues (current round, fresh review) ===\n\n  - id: \"R19-N1\"\n    summary: \"DEFF 校正产生 2.16× 估计范围（13.5% vs 29.2%），论文未提供充分的分辨依据\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。Cluster bootstrap CI [26.7%, 53.2%] 仅 ~30 families 重采样，有效独立单元极少。论文 headline '17.9-31.3%' 可能因 DEFF 选择被高估一倍。\"\n    action_items:\n      - round: 19\n        action: \"Family 定义 sensitivity analysis；block bootstrap with varying block size；正文 Discussion 中充分讨论不确定性的实践含义\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"Semi-synthetic 注入用 uniform binary flipping，检测力估计可能被系统性高估——缺少 graded probability shift 验证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Scheme D (difficulty-dependent) 仍是 binary flipping 变体。Graded shift (Δp=0.1-0.3) 下 MH-DIF 检测力可能远低于报告的 ΔTPR=0.371。\"\n    action_items:\n      - round: 19\n        action: \"增加 graded injection scheme (Δp ∈ {0.1, 0.2, 0.3})；报告 minimum detectable probability shift；或提供 analytical bound\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"缺少 DIF 文献中 impact/bias 关键区分——'Correct' 步骤无差别移除 DIF items 与 mechanism-agnostic 定位逻辑冲突\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈 AGREE。DIF 是 bias 的必要非充分条件。如果部分 DIF 由 capability evolution 驱动（impact），无差别移除会降低 benchmark 敏感度。§5.1 mechanism-agnostic ↔ §5.2 Correct 步骤 ↔ Limitations expert review 三处逻辑冲突。\"\n    action_items:\n      - round: 19\n        action: \"§5.2 引入 impact/bias 区分；分别报告 impact-candidate 和 bias-candidate 的 rescoring 效应；引用 DIF→expert review→bias determination→removal 标准流程；引用 Camilli & Shepard (1994), Penfield & Camilli (2007)\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N4\"\n    summary: \"DIF-contamination 正交性的 headline finding 依赖质量存疑的 web-overlap proxy\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。Web-overlap labels (Li et al. 2024b) 覆盖率仅 73.8%，是 contamination 的 noisy proxy。Jaccard≈0.20 可能反映 proxy 低质量而非真正独立性。论文未排除此替代解释。\"\n    action_items:\n      - round: 19\n        action: \"将结论软化为 'DIF is independent of web-overlap based contamination labels'；讨论 proxy 局限性；如可能用其他 contamination 指标交叉验证\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"Calendar-year cohort boundary 粗糙——temporal framing 过窄，实为 cohort-based DIF\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2-W3 高度重合。Release date ≠ training cutoff。'Temporal' 标签暗示时间是主变量，但 cohort 在架构、数据规模、训练方法上同时变化。Composition control 仅控制 base/instruct 比例。\"\n    action_items:\n      - round: 19\n        action: \"§5.1 明确 'temporal' 是 'cohort-based' 简写；讨论未控制 confounders；如有 training cutoff 元数据做 sensitivity analysis\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W2\"\n    summary: \"Cross-subject matching ΔFPR=0 在高覆盖率 contamination (k>5) 下退化未充分讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W2, R2 AGREE。k=20 ΔFPR=0.062。Internet-scale 预训练可能覆盖 30+ subjects，但论文未模拟 k=30/50 且未给出超出保证范围时的替代策略。\"\n    action_items:\n      - round: 19\n        action: \"模拟 k=30/50 的 ΔFPR；讨论高 contamination 覆盖率下的替代策略\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W3, R2 AGREE。Related Work 以 Contamination Detection 开篇，Figure 1 标注 global contamination，§4.3 整节做 DIF-contamination 对比——但同时声称 mechanism-agnostic。R1 建议将 contamination 对比重新框定为 discriminant validity evidence。\"\n    action_items:\n      - round: 19\n        action: \"将 contamination 对比重新框定为 discriminant validity evidence；调整 Related Work 开篇和 Figure 1 标注\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"ETS 阈值从人类考生迁移到 LLM 缺乏充分校准验证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W1, R1 AGREE。Random-split P99=1.45 是 necessary 但非 sufficient condition。§4.1 Monte Carlo power analysis 未被明确框定为 ETS 阈值校准验证。\"\n    action_items:\n      - round: 19\n        action: \"在正文中明确连接 §4.1 power 分析与 ETS 阈值在 LLM 下的适用性论证\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"与 Growing Pains (Habba et al., 2026) 差异化论证不够深入\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W2, R1 AGREE（优先级不高）。缺少在相同 data/items 上的直接比较。\"\n    action_items:\n      - round: 19\n        action: \"附录中加入与 Growing Pains 在相同 items 上的交叉比较；或明确讨论两方法在理论上何时 diverge\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Score correction 展示不充分且缺乏 impact/bias 区分作为方法论基础\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W5, R1 AGREE（更根本问题是 N3 的 impact/bias）。§4.6 仅半页，未区分 ranking reversal 位置（top-10 vs mid-tier），未与其他 correction 方法比较。\"\n    action_items:\n      - round: 19\n        action: \"扩展 §4.6 或附录 case study；结合 N3 建立 impact/bias conceptual foundation 后再展示影响\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-D1\"\n    summary: \"[分歧] 方法论新颖性是否足够——MH-DIF 直接搬运 vs LLM-specific adaptations\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-N1 认为 MH-DIF 是 40 年标准方法的直接搬运，novelty 不足。R1 REBUT：cross-subject matching ΔFPR=0、DEFF 校正、4 个 LLM-specific challenges 是真正贡献，不是教科书内容。分歧未解决。\"\n    action_items:\n      - round: 19\n        action: \"Introduction 中更清晰区分 'borrowed methodology' 和 'novel adaptations'；考虑增加 logistic regression DIF 比较\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 17 issues (all resolved by R18 verification) ===\n\n  - id: \"R17-N1\"\n    summary: \"DEFF 估计量选择论证存在循环性——simulation 用观测 ICC-size 模式构造前提，再论证 simple-mean 更优\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%，差距 2.16×。\"\n      - round: 18\n        reviewers: []\n        note: \"Reviewer 验证 PASS。区间表述 13.5-29.2% 全文 8 处同步；cluster bootstrap 独立证据；weighted-mean downstream 分析确认结论稳健。\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R19 fresh review 再次提出 DEFF 不确定性范围问题（R19-N1），关注点从循环性转移到区间本身过宽和 bootstrap 可靠性。\"\n    action_items:\n      - round: 17\n        action: \"改为区间表述 13.5-29.2%，cluster bootstrap CI 作为独立证据，weighted-mean downstream 分析\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"区间表述 13.5-29.2% 替代 simple-mean 推荐；cluster bootstrap CI 排除 weighted-mean 13.5%，提供模型无关证据；weighted-mean downstream (ρ=0.999, +1.77pp) 确认结论稳健。Reviewer 验证 PASS。但 R19 fresh review 认为区间仍过宽（R19-N1）。\"\n    resolution_round: 18\n\n  - id: \"R17-N2\"\n    summary: \"Semi-synthetic ΔTPR 'upper bound' 声称不严密——uniform flipping 非理论上界，difficulty-dependent 结果应进主文\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"uniform 非真正上界；difficulty-dependent injection 仅在 Appendix。\"\n      - round: 18\n        reviewers: []\n        note: \"Reviewer 验证 PASS。'reference-case detection power' 替换完成；difficulty-dependent 进入主文 §4.5。\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R19 fresh review 进一步要求 graded probability shift 验证（R19-N2），超出 R17 的修改范围。\"\n    action_items:\n      - round: 17\n        action: \"'upper bound' → 'reference-case detection power'; difficulty-dependent 进主文\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"'upper bound' → 'reference-case detection power under stylized uniform injection'；ΔTPR≈0.41 vs 0.51 (20% reduction) 进入主文 §4.5。但 R19 要求更进一步的 graded injection 验证（R19-N2）。\"\n    resolution_round: 18\n\n  - id: \"R17-W1\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§3.4 + §5.1 明确 mechanism-agnostic diagnostic\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§3.4 + §5.1 双处标记 mechanism-agnostic + impact-bias framework citation。但 R19 再次提出此张力（R19-W3），要求更彻底的 reframing。\"\n    resolution_round: 18\n\n  - id: \"R17-W2\"\n    summary: \"与 Growing Pains 的差异化需补充方法论对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§2 补充 parametric vs nonparametric + equating vs diagnosis\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Related Work 两点区分。但 R19 仍要求更深入对比（R19-W5）。\"\n    resolution_round: 18\n\n  - id: \"R17-W3\"\n    summary: \"k>5 时 ΔFPR 保证退化的实际影响未充分量化\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"Abstract 移除 ΔFPR=0; Intro C2 附 k≤5; §4.5 量化影响\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已修改。R19 进一步要求模拟 k=30/50（R19-W2）。\"\n    resolution_round: 18\n\n  - id: \"R17-W4\"\n    summary: \"DIF-contamination 正交性需讨论替代解释\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§5.1 两种解释 + OR=4.75 证据\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已修改。R19 进一步要求讨论 proxy 质量（R19-N4）。\"\n    resolution_round: 18\n\n  - id: \"R17-W5\"\n    summary: \"时间粒度选择（年度 cohort）未经论证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§3.3 半年粒度 + Limitations release date confound\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已修改。R19 仍指出 temporal framing 过窄（R19-W1）。\"\n    resolution_round: 18\n\n  - id: \"R17-W6\"\n    summary: \"Abstract 信息过载（≥8 个定量发现）\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"Abstract 精简到 ~5 个核心数字\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"~122 words, ~6 核心数字。R19 未复发。\"\n    resolution_round: 18\n\n  - id: \"R17-M1\"\n    summary: \"ρ≈0.997 与 ±800 rank displacement 共存的机制需在主文解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§4.6 解释 closely-ranked pairs 集中\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§4.6 '35.2% at Δrank < 50 vs. 0.0% above 1000'。R19 未复发。\"\n    resolution_round: 18\n\n  # === Round 16 issues (all resolved) ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值从人类考生直接移植到 LLM 缺乏领域内校准\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"§4.1 empirical null (P99=1.45 ≈ ETS C 1.5). R17 未复发。R19 再次提出但降级为 warning（R19-W4）。\"\n    resolution_round: 17\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 声称过度定位\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"3→2 contributions. R17 未复发。R19 novelty 分歧（R19-D1）部分相关。\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 校正两种估计量差异 2× 削弱 headline 定量精度\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"R16 推荐 simple-mean → R17-N1 循环性 → R18 区间表述解决。R19 再次提出（R19-N1）。\"\n    resolution_round: 18\n\n  - id: \"R16-W2\"\n    summary: \"§5.2 审计协议措辞超出方法能力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"§5.2 含 'DIF alone cannot determine causation'. R17 未复发。R19 impact/bias 问题（R19-N3）进一步深化。\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Discussion 缺乏深层 insight\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§5.1 三个 LLM-vs-educational 区分。\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"精简到 ~122 words, 6 数字。\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"主文超页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"0 \\\\enlargethispage. Conclusion 在 page 8 内。R17/R18 均通过。但 R19 注意到 \\\\enlargethispage{2\\\\baselineskip} 仍在使用。\"\n    resolution_round: 17\n\n  - id: \"R16-W6\"\n    summary: \"Semi-synthetic ΔTPR 应标为检测力上界\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"'reference-case detection power' 替换完成。R19 进一步要求 graded injection（R19-N2）。\"\n    resolution_round: 18\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"§1 parenthetical 定义。R19 仍有小问题提及但不影响接收。\"\n    resolution_round: 17\n\n  - id: \"R16-M2\"\n    summary: \"有效 N=1,887 vs 总 N=5,227 澄清\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§3.2 已修正。\"\n    resolution_round: 17\n\n  - id: \"R16-M3\"\n    summary: \"遗漏近期相关工作\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"新引用已加入 §2。\"\n    resolution_round: 17\n\n  - id: \"R16-DATA1\"\n    summary: \"论文 random-split baseline 0.18% 来自单次运行\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"全文修正 0.18→0.62。\"\n    resolution_round: 17\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 19 issues (current round, fresh review) ===\n\n  - id: \"R19-N1\"\n    summary: \"DEFF 校正产生 2.16× 估计范围（13.5% vs 29.2%），论文未提供充分的分辨依据\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。Cluster bootstrap CI [26.7%, 53.2%] 仅 ~30 families 重采样，有效独立单元极少。论文 headline '17.9-31.3%' 可能因 DEFF 选择被高估一倍。\"\n    action_items:\n      - round: 19\n        action: \"Family 定义 sensitivity analysis；block bootstrap with varying block size；正文 Discussion 中充分讨论不确定性的实践含义\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"Semi-synthetic 注入用 uniform binary flipping，检测力估计可能被系统性高估——缺少 graded probability shift 验证\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Scheme D (difficulty-dependent) 仍是 binary flipping 变体。Graded shift (Δp=0.1-0.3) 下 MH-DIF 检测力可能远低于报告的 ΔTPR=0.371。\"\n    action_items:\n      - round: 19\n        action: \"增加 graded injection scheme (Δp ∈ {0.1, 0.2, 0.3})；报告 minimum detectable probability shift；或提供 analytical bound\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"缺少 DIF 文献中 impact/bias 关键区分——'Correct' 步骤无差别移除 DIF items 与 mechanism-agnostic 定位逻辑冲突\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈 AGREE。DIF 是 bias 的必要非充分条件。如果部分 DIF 由 capability evolution 驱动（impact），无差别移除会降低 benchmark 敏感度。§5.1 mechanism-agnostic ↔ §5.2 Correct 步骤 ↔ Limitations expert review 三处逻辑冲突。\"\n    action_items:\n      - round: 19\n        action: \"§5.2 引入 impact/bias 区分；分别报告 impact-candidate 和 bias-candidate 的 rescoring 效应；引用 DIF→expert review→bias determination→removal 标准流程；引用 Camilli & Shepard (1994), Penfield & Camilli (2007)\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N4\"\n    summary: \"DIF-contamination 正交性的 headline finding 依赖质量存疑的 web-overlap proxy\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。Web-overlap labels (Li et al. 2024b) 覆盖率仅 73.8%，是 contamination 的 noisy proxy。Jaccard≈0.20 可能反映 proxy 低质量而非真正独立性。论文未排除此替代解释。\"\n    action_items:\n      - round: 19\n        action: \"将结论软化为 'DIF is independent of web-overlap based contamination labels'；讨论 proxy 局限性；如可能用其他 contamination 指标交叉验证\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"Calendar-year cohort boundary 粗糙——temporal framing 过窄，实为 cohort-based DIF\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2-W3 高度重合。Release date ≠ training cutoff。'Temporal' 标签暗示时间是主变量，但 cohort 在架构、数据规模、训练方法上同时变化。Composition control 仅控制 base/instruct 比例。\"\n    action_items:\n      - round: 19\n        action: \"§5.1 明确 'temporal' 是 'cohort-based' 简写；讨论未控制 confounders；如有 training cutoff 元数据做 sensitivity analysis\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W2\"\n    summary: \"Cross-subject matching ΔFPR=0 在高覆盖率 contamination (k>5) 下退化未充分讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W2, R2 AGREE。k=20 ΔFPR=0.062。Internet-scale 预训练可能覆盖 30+ subjects，但论文未模拟 k=30/50 且未给出超出保证范围时的替代策略。\"\n    action_items:\n      - round: 19\n        action: \"模拟 k=30/50 的 ΔFPR；讨论高 contamination 覆盖率下的替代策略\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Mechanism-agnostic 定位与 contamination-heavy 叙事存在张力\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W3, R2 AGREE。Related Work 以 Contamination Detection 开篇，Figure 1 标注 global contamination，§4.3 整节做 DIF-contamination 对比——但同时声称 mechanism-agnostic。R1 建议将 contamination 对比重新框定为 discriminant validity evidence。\"\n    action_items:\n      - round: 19\n        action: \"将 contamination 对比重新框定为 discriminant validity evidence；调整 Related Work 开篇和 Figure 1 标注\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"ETS 阈值从人类考生迁移到 LLM 缺乏充分校准验证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W1, R1 AGREE。Random-split P99=1.45 是 necessary 但非 sufficient condition。§4.1 Monte Carlo power analysis 未被明确框定为 ETS 阈值校准验证。\"\n    action_items:\n      - round: 19\n        action: \"在正文中明确连接 §4.1 power 分析与 ETS 阈值在 LLM 下的适用性论证\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"与 Growing Pains (Habba et al., 2026) 差异化论证不够深入\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W2, R1 AGREE（优先级不高）。缺少在相同 data/items 上的直接比较。\"\n    action_items:\n      - round: 19\n        action: \"附录中加入与 Growing Pains 在相同 items 上的交叉比较；或明确讨论两方法在理论上何时 diverge\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Score correction 展示不充分且缺乏 impact/bias 区分作为方法论基础\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W5, R1 AGREE（更根本问题是 N3 的 impact/bias）。§4.6 仅半页，未区分 ranking reversal 位置（top-10 vs mid-tier），未与其他 correction 方法比较。\"\n    action_items:\n      - round: 19\n        action: \"扩展 §4.6 或附录 case study；结合 N3 建立 impact/bias conceptual foundation 后再展示影响\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-D1\"\n    summary: \"[分歧] 方法论新颖性是否足够——MH-DIF 直接搬运 vs LLM-specific adaptations\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-N1 认为 MH-DIF 是 40 年标准方法的直接搬运，novelty 不足。R1 REBUT：cross-subject matching ΔFPR=0、DEFF 校正、4 个 LLM-specific challenges 是真正贡献，不是教科书内容。分歧未解决。\"\n    action_items:\n      - round: 19\n        action: \"Introduction 中更清晰区分 'borrowed methodology' 和 'novel adaptations'；考虑增加 logistic regression DIF 比较\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 17 issues (all resolved by R18 verification) ===\n\n  - id: \"R17-N1\"\n    summary: \"DEFF 估计量选择论证存在循环性——simulation 用观测 ICC-size 模式构造前提，再论证 simple-mean 更优\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%，差距 2.16×。\"\n      - round: 18\n        reviewers: []\n        note: \"Reviewer 验证 PASS。区间表述 13.5-29.2% 全文 8 处同步；cluster bootstrap 独立证据；weighted-mean downstream 分析确认结论稳健。\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R19 fresh review 再次提出 DEFF 不确定性范围问题（R19-N1），关注点从循环性转移到区间本身过宽和 bootstrap 可靠性。\"\n    action_items:\n      - round: 17\n        action: \"改为区间表述 13.5-29.2%，cluster bootstrap CI 作为独立证据，weighted-mean downstream 分析\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"区间表述 13.5-29.2% 替代 simple-mean 推荐；cluster bootstrap CI 排除 weighted-mean 13.5%，提供模型无关证据；weighted-mean downstream (ρ=0.999, +1.77pp) 确认结论稳健。Reviewer 验证 PASS。但 R19 fresh review 认为区间仍过宽（R19-N1）。\"\n    resolution_round: 18\n\n  - id: \"R17-N2\"\n    summary: \"Semi-synthetic ΔTPR 'upper bound' 声称不严密——uniform flipping 非理论上界，difficulty-dependent 结果应进主文\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"uniform 非真正上界；difficulty-dependent injection 仅在 Appendix。\"\n      - round: 18\n        reviewers: []\n        note: \"Reviewer 验证 PASS。'reference-case detection power' 替换完成；difficulty-dependent 进入主文 §4.5。\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R19 fresh review 进一步要求 graded probability shift 验证（R19-N2），超出 R17 的修改范围。\"\n    action_items:\n      - round: 17\n        action: \"'upper bound' → 'reference-case detection power'; difficulty-dependent 进主文\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"'upper bound' → 'reference-case detection power under stylized uniform injection'；ΔTPR≈0.41 vs 0.51 (20% reduction) 进入主文 §4.5。但 R19 要求更进一步的 graded injection 验证（R19-N2）。\"\n    resolution_round: 18\n\n  - id: \"R17-W1\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 实验设计的叙事张力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§3.4 + §5.1 明确 mechanism-agnostic diagnostic\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§3.4 + §5.1 双处标记 mechanism-agnostic + impact-bias framework citation。但 R19 再次提出此张力（R19-W3），要求更彻底的 reframing。\"\n    resolution_round: 18\n\n  - id: \"R17-W2\"\n    summary: \"与 Growing Pains 的差异化需补充方法论对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§2 补充 parametric vs nonparametric + equating vs diagnosis\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Related Work 两点区分。但 R19 仍要求更深入对比（R19-W5）。\"\n    resolution_round: 18\n\n  - id: \"R17-W3\"\n    summary: \"k>5 时 ΔFPR 保证退化的实际影响未充分量化\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"Abstract 移除 ΔFPR=0; Intro C2 附 k≤5; §4.5 量化影响\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已修改。R19 进一步要求模拟 k=30/50（R19-W2）。\"\n    resolution_round: 18\n\n  - id: \"R17-W4\"\n    summary: \"DIF-contamination 正交性需讨论替代解释\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§5.1 两种解释 + OR=4.75 证据\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已修改。R19 进一步要求讨论 proxy 质量（R19-N4）。\"\n    resolution_round: 18\n\n  - id: \"R17-W5\"\n    summary: \"时间粒度选择（年度 cohort）未经论证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§3.3 半年粒度 + Limitations release date confound\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"已修改。R19 仍指出 temporal framing 过窄（R19-W1）。\"\n    resolution_round: 18\n\n  - id: \"R17-W6\"\n    summary: \"Abstract 信息过载（≥8 个定量发现）\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"Abstract 精简到 ~5 个核心数字\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"~122 words, ~6 核心数字。R19 未复发。\"\n    resolution_round: 18\n\n  - id: \"R17-M1\"\n    summary: \"ρ≈0.997 与 ±800 rank displacement 共存的机制需在主文解释\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    action_items:\n      - round: 17\n        action: \"§4.6 解释 closely-ranked pairs 集中\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§4.6 '35.2% at Δrank < 50 vs. 0.0% above 1000'。R19 未复发。\"\n    resolution_round: 18\n\n  # === Round 16 issues (all resolved) ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值从人类考生直接移植到 LLM 缺乏领域内校准\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"§4.1 empirical null (P99=1.45 ≈ ETS C 1.5). R17 未复发。R19 再次提出但降级为 warning（R19-W4）。\"\n    resolution_round: 17\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 声称过度定位\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"3→2 contributions. R17 未复发。R19 novelty 分歧（R19-D1）部分相关。\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 校正两种估计量差异 2× 削弱 headline 定量精度\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"R16 推荐 simple-mean → R17-N1 循环性 → R18 区间表述解决。R19 再次提出（R19-N1）。\"\n    resolution_round: 18\n\n  - id: \"R16-W2\"\n    summary: \"§5.2 审计协议措辞超出方法能力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"§5.2 含 'DIF alone cannot determine causation'. R17 未复发。R19 impact/bias 问题（R19-N3）进一步深化。\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Discussion 缺乏深层 insight\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§5.1 三个 LLM-vs-educational 区分。\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"精简到 ~122 words, 6 数字。\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"主文超页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"0 \\\\enlargethispage. Conclusion 在 page 8 内。R17/R18 均通过。但 R19 注意到 \\\\enlargethispage{2\\\\baselineskip} 仍在使用。\"\n    resolution_round: 17\n\n  - id: \"R16-W6\"\n    summary: \"Semi-synthetic ΔTPR 应标为检测力上界\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"'reference-case detection power' 替换完成。R19 进一步要求 graded injection（R19-N2）。\"\n    resolution_round: 18\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"§1 parenthetical 定义。R19 仍有小问题提及但不影响接收。\"\n    resolution_round: 17\n\n  - id: \"R16-M2\"\n    summary: \"有效 N=1,887 vs 总 N=5,227 澄清\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§3.2 已修正。\"\n    resolution_round: 17\n\n  - id: \"R16-M3\"\n    summary: \"遗漏近期相关工作\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"新引用已加入 §2。\"\n    resolution_round: 17\n\n  - id: \"R16-DATA1\"\n    summary: \"论文 random-split baseline 0.18% 来自单次运行\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"全文修正 0.18→0.62。\"\n    resolution_round: 17\n"
  }
}
```

</details>

---


### Tool result

_source line 1694 · 2026-05-23T14:14:28.572603+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 15656}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1695 · 2026-05-23T14:17:05.562029+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "report": "# 审稿报告 — Round 19 (Fresh Review)\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (Long Paper, via ARR)\n**审稿模式**: Fresh（独立初审，无历史记忆）\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n\n---\n\n## Summary\n\n论文将教育测量中的 Mantel-Haenszel DIF (Differential Item Functioning) 分析应用于 METABENCH 的 5,227 个 LLM 模型在 MMLU 12,508 道题目上的二元响应矩阵，发现 2023–2024 模型 cohort 之间 13.5–29.2%（DEFF 校正后）的题目表现出显著 temporal DIF（ETS Category C），且 DIF 信号与 web-overlap contamination labels 近乎独立（Jaccard=0.206）。论文提出 cross-subject matching 策略（在单科目 contamination 下提供构造性 ΔFPR=0 保证）和三步 Monitor/Triage/Correct 审计协议。Semi-synthetic 注入框架验证了检测力，6 个 METABENCH benchmark 的交叉验证确认了结果的泛化性。\n\n---\n\n## Strengths\n\n**S1 [共识]** 规模与系统性出色——5,227 models × 12,508 items 是 IRT-for-LLM 领域最大规模的 DIF 分析，且扩展到 6 个 benchmark 交叉验证（Table 3），增强了 generalizability。\n\n**S2 [共识]** Cross-subject matching 是真正的方法论贡献——ΔFPR=0 的构造性保证（k≤5 subjects）为 DIF 在多科目 benchmark 上的应用提供了可靠 FPR 控制。R1 特别指出这不是 purified subtest matching 的直接推广，而是利用 LLM benchmark 的 multi-subject 结构给出了在教育测试中无对应物的理论保证。\n\n**S3 [共识]** DIF ⊥ contamination labels 的发现有重要理论意义——Jaccard=0.206 表明两种 diagnostic 维度近正交，挑战了将 item-level anomaly 简单归因于 contamination 的直觉（尽管此发现的解释力受限于 proxy 质量，见 N4）。\n\n**S4 [共识]** 多层验证架构设计得当——random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control (Δ=1.08pp)、LOFO robustness、graduated de-duplication 构成系统性 null-hypothesis 校验。\n\n**S5 [共识]** Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 强证据——base 60.1% reference-favoring vs instruct 65.6% focal-favoring，有效排除单一机制驱动假设。\n\n**S6 [共识]** 附录内容丰富（~10 页），覆盖 method details、mechanism analysis、structural controls、DEFF estimation、uncertainty quantification，满足 reproducibility 要求。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [共识: R1提出, R2 AGREE]** DEFF 校正产生 2.16× 估计范围（C%=29.2% vs 13.5%），论文未提供充分分辨依据\n- Simple-mean DEFF (3.87) 和 weighted-mean DEFF (12.79) 给出的 C% 差距超过 2 倍\n- Cluster bootstrap 95% CI [26.7%, 53.2%] 仅对 ~30 个 families 重采样，有效独立单元极少，上界被 Mistral (n=547)/Llama-3 (n=315) 驱动\n- 论文 headline \"17.9–31.3%\" 在多处讨论中倾向引用上界，而 weighted-mean 下界 13.5% 意味着 DIF 规模可能被高估一倍\n- **修改建议**: family 定义 sensitivity analysis（不同粒度分组）；block bootstrap with varying block size 评估 CI 稳定性；正文 Discussion 充分讨论不确定性的实践含义\n\n**N2 [共识: R1提出, R2 AGREE]** Semi-synthetic 注入框架使用 uniform binary flipping，检测力估计可能被系统性高估\n- 所有注入方案（包括 Scheme D difficulty-dependent）均为 binary flipping 变体（0→1），未测试 graded probability shift\n- 现实 contamination 更可能表现为概率偏移（Δp=0.1–0.3），此场景下 MH-DIF 检测力可能远低于报告的 ΔTPR=0.371\n- Limitations 承认 \"ΔTPR values may overestimate detection power\" 但未量化影响\n- **修改建议**: 增加 graded injection scheme (Δp ∈ {0.1, 0.2, 0.3})，报告 minimum detectable probability shift；或提供 analytical bound\n\n**N3 [共识: R1提出, R2 强烈 AGREE]** 缺少 DIF 文献中 impact/bias 关键区分，\"Correct\" 步骤与 mechanism-agnostic 定位逻辑冲突\n- DIF 是 item bias 的必要但非充分条件（Camilli & Shepard, 1994）。如果部分 DIF 由 capability evolution 驱动（construct-relevant \"impact\"），无差别移除会降低 benchmark 敏感度\n- 论文存在内部逻辑冲突：§5.1 声称 mechanism-agnostic → §5.2 建议无差别移除 ETS C items → Limitations 又承认需 expert review\n- Score correction (+2.12pp) 未区分 impact-driven vs bias-driven DIF items 的贡献\n- **修改建议**: §5.2 引入 impact/bias 区分；DIF → expert review → bias determination → removal 标准流程；分别报告 impact/bias candidate 的 rescoring 效应；引用 Camilli & Shepard (1994), Penfield & Camilli (2007)\n\n**N4 [共识: R2提出, R1 AGREE]** DIF-contamination 正交性的 headline finding 依赖质量存疑的 web-overlap proxy\n- Li et al. (2024b) web-overlap labels 是粗糙的 contamination proxy：(1) web-overlap ≠ 实际训练数据包含；(2) synthetic data/instruction tuning 不被捕获；(3) 覆盖率仅 73.8%\n- Jaccard ≈ 0.206 存在两种解释：(a) DIF 与真实 contamination 确实独立（论文解释），(b) proxy 噪声太大导致与任何信号关联都低。论文未排除解释 (b)\n- Abstract/Conclusion 措辞倾向解释 (a)，但 §5.1 呈现了两种解释——措辞不一致\n- **修改建议**: 结论软化为 \"DIF is independent of web-overlap based contamination labels\"；讨论 proxy 局限性；如可能用 Time Travel/memorization scores 交叉验证\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [共识: R1-W1 + R2-W3]** Calendar-year cohort boundary 粗糙，\"temporal\" framing 过窄\n- Release date ≠ training data cutoff；2023 vs 2024 cohorts 在架构、数据规模、训练方法上同时变化\n- Composition control 仅控制 base/instruct 比例，未控制其他 cohort 差异\n- **建议**: §5.1 明确 \"temporal\" 是 \"cohort-based\" 简写；讨论未控制 confounders\n\n**W2 [共识: R1-W2, R2 AGREE]** Cross-subject matching ΔFPR=0 在高覆盖率 contamination (k>5) 下的退化未充分讨论\n- k=20 时 ΔFPR=0.069；internet-scale 预训练可能覆盖 30+ subjects\n- **建议**: 模拟 k=30/50 的 ΔFPR；讨论超出保证范围时的替代策略\n\n**W3 [共识: R1-W3 + R2相关]** Mechanism-agnostic 定位与 contamination-heavy 叙事张力\n- Related Work 以 Contamination Detection 开篇，Figure 1 标注 \"global contamination\"，§4.3 整节做 DIF-contamination 对比\n- **建议**: 将 contamination 对比重新框定为 discriminant validity evidence\n\n**W4 [共识: R2-W1, R1 AGREE]** ETS 阈值从人类考生迁移到 LLM 缺乏充分校准\n- Random-split P99=1.45 是 necessary 但非 sufficient condition\n- **建议**: 明确连接 §4.1 power 分析与 ETS 阈值适用性论证\n\n**W5 [共识: R2-W2, R1 AGREE]** 与 Growing Pains 差异化论证不够深入\n- 缺少在相同 data/items 上的直接比较（优先级较低）\n\n**W6 [共识: R2-W5, R1 AGREE]** Score correction (§4.6) 展示不充分\n- 仅半页篇幅，未区分 ranking reversal 位置（top-10 vs mid-tier）\n- 更根本问题是缺少 impact/bias 区分作为方法论基础（与 N3 关联）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全一致** [AGREE]：\n1. DEFF 2.16× 不确定性范围是实质性方法论缺陷（N1）\n2. Binary flipping 高估检测力，需 graded injection 验证（N2）\n3. Impact/bias 区分缺失是最严重的方法论问题，导致 \"Correct\" 步骤逻辑不自洽（N3）\n4. Web-overlap proxy 质量问题削弱 headline finding（N4）\n5. Calendar-year / temporal framing 过窄（W1）\n6. Cross-subject matching 高 k 退化需进一步量化（W2）\n7. Mechanism-agnostic 与 contamination-heavy 叙事张力需重新框定（W3）\n\n---\n\n## Reviewer Divergence\n\n**D1: 方法论新颖性是否足够**\n- R2 认为 MH-DIF 是 40 年标准方法的直接搬运，novelty 不足以进 Conference\n- R1 反驳：cross-subject matching ΔFPR=0 保证和 DEFF 校正是 LLM-specific 的非平凡贡献；但同意应更清晰区分 \"borrowed methodology\" 和 \"novel adaptations\"\n- **结论**: 方法论贡献介于 \"纯应用\" 和 \"有实质创新\" 之间，取决于 reviewer 对 application novelty 的标准\n\n**D2: Abstract \"because\" 因果暗示**\n- R2 认为 \"scores are not directly comparable because item measurement properties differ systematically\" 隐含因果判断\n- R1 反驳：此处 \"because\" 解释的是不可比性的原因（DIF 的定义），非 DIF 成因的因果推断；\"measurement properties differ\" 在 DIF 框架下是统计事实而非因果声称\n- **结论**: R1 的反驳有力——此处措辞在 psychometrics 框架下是标准用法，不构成因果过度暗示\n\n**D3: METABENCH selection bias 的严重性**\n- R1 指出 Open LLM Leaderboard 存在自选择偏差\n- R2 反驳：关键问题是 bias 是否跨 cohort 差异性存在，若两个时期的 bias 相似则不产生 artifactual DIF；5,227 模型已覆盖大部分提交\n- **结论**: R2 的反驳合理——selection bias 是一般性局限，但对 DIF 结果的特异性影响有限。建议在 Limitations 简要讨论\n\n---\n\n## Questions\n\n1. 如果用 graded probability injection (Δp=0.2) 而非 binary flip，ΔTPR 预期下降到什么水平？是否做过 pilot 或 analytical estimation？\n2. DEFF 的 family 定义是如何确定的？用 50 个 sub-family 而非 30 个 family 时，DEFF 如何变化？\n3. 移除 DIF-C items 后 score shift = +2.12pp（2024 cohort 得分上升）——如果 contamination 是主要机制，预期 2024 得分应下降。如何调和这一方向性矛盾？\n4. 如果使用 Time Travel 或 memorization scores 替代 web-overlap labels，Jaccard 是否仍 ~0.20？\n5. 论文能否区分 \"legitimately harder items for 2024 models\"（capability regression）和 \"construct-irrelevant DIF\"？若不能，\"Correct\" 步骤是否过于简化？\n\n---\n\n## Missing References\n\n**两位 Reviewer 一致推荐**:\n- Camilli, G. & Shepard, L. A. (1994). *Methods for Identifying Biased Test Items*. Sage. — DIF 与 item bias 的经典区分框架\n- Penfield, R. D. & Camilli, G. (2007). Differential item functioning and item bias. In *Handbook of Statistics* (Vol. 26). — impact vs. bias 方法论框架\n\n**R2 推荐（R1 部分同意）**:\n- Test security / item exposure control 文献 (Hau & Chang, 2001; Way, 1998) — 与 benchmark item exposure 概念相关\n- Item banking/equating 在 benchmark 维护中的应用 — 可强化 §5.2 audit protocol\n\n**R2 推荐但 R1 反驳**:\n- Polytomous DIF 方法 (French & Miller, 1996) — R1 指出 MMLU 使用 binary scoring，polytomous DIF 不适用\n- Multi-group CFA / MIMIC models — R1 指出论文已解释选择 MH-DIF 而非 parametric MI 的理由（MMLU 2PL fit 差），CFA 前提不满足\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer）：**未请求**（项目配置未启用）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 4 info）。主要发现：\n\n- **[warning]** Pages 3-6（Method §3 全节）连续 4 页无任何 figure/table，缺乏视觉锚点，易产生阅读疲劳。建议加入方法流程概览图\n- **[warning]** Page 7 三个 display items (Figure 2 + Table 1 + Table 2) 堆积，与前 4 页纯文本形成强烈节奏失衡。建议分散部分 display items\n- **[info]** 主文 5 个 display items / 8 页 = 0.625/页，对实证论文偏少。附录有 12+ 表 + 4 图，部分关键结果可考虑提升到主文\n- **[info]** Figure 1 (ICC schematic) 作为视觉锚点效果优秀\n- **[info]** Table 1 部分单元格文字偏小；Figure 2 x 轴标签字号偏小\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度: 4/5**（两位 Reviewer 均具备 DIF/psychometrics 和 LLM evaluation 领域专业知识）\n\n**评分理由**:\n\n论文在规模（5,227 models × 12,508 items）、实验系统性（7 层验证架构）和 cross-subject matching 方法论贡献上表现出色。DIF ⊥ contamination labels 的发现对社区有价值，base/instruct 方向反转提供了令人信服的 mechanism separation 证据。\n\n但四个 Must-Fix 问题阻止更高评分：(1) DEFF 2.16× 不确定性范围削弱核心定量发现的精度；(2) binary flipping 可能系统性高估检测力；(3) impact/bias 区分的缺失导致审计协议的逻辑不自洽——这是两位 Reviewer 的最强共识；(4) headline finding（DIF-contamination 正交）依赖质量存疑的 proxy。方法论新颖性存在分歧——cross-subject matching 是实质贡献，但整体框架仍以标准 MH-DIF 为核心。\n\n如果作者能：(a) 引入 impact/bias 区分重构审计协议逻辑，(b) 坦诚讨论 web-overlap proxy 局限性并软化正交性声称，(c) 提供 graded injection 的检测力估计，论文有潜力达到 Conference (4.0) 水平。否则 Findings (3.0) 是更合适的归宿。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2（cross-subject matching ΔFPR=0）是最有说服力的方法论贡献，但叙事中被 Contribution 1（规模与实证发现）抢占了焦点。考虑在 framing 上更突出方法论适配的非平凡性\n- \"temporal score incomparability\" 这一术语在 Introduction 的 parenthetical 定义清晰，但后续混用 \"temporal DIF\" / \"measurement invariance\" / \"score incomparability\" 造成术语分散\n\n### §2 Related Work\n- 以 \"Contamination Detection\" 开篇强化了论文的 contamination framing，与 mechanism-agnostic 定位矛盾。建议以 \"Measurement Invariance in LLM Evaluation\" 或 \"Psychometric Approaches to Benchmark Quality\" 开篇\n- 与 Growing Pains 的对比是充分的，但缺少在相同 items 上的实证比较\n\n### §3 Method\n- §3.2 的 MH-DIF 描述清晰完整，但 LLM-specific challenges（末段 4 点）可以更展开\n- §3.4 Semi-synthetic framework: \"Remark (Zero FPR)\" 的证明干净简洁，是论文的 highlight\n- 视觉审查指出 §3 全节（pages 3-6）无任何 figure/table，建议加入方法流程图\n\n### §4 Experiments\n- §4.2 的多层控制（random split, ability quintile, nearest-neighbor matching）设计严谨\n- §4.3 Ground Truth Mismatch: 标题 \"Ground Truth Mismatch\" 暗示 web-overlap labels 是 ground truth——但论文自己论证了它们不是。建议改为 \"Relationship to Web-Overlap Labels\" 或 \"Discriminant Validity\"\n- §4.5 的 ΔFPR=0 结果是重要发现，但 k>5 退化部分需扩展\n- §4.6 Downstream Impact 偏薄，需补充 top-k ranking 影响和 impact/bias 分析\n\n### §5 Discussion\n- §5.1 的三个 LLM-vs-educational 区分和两种解释框架是好的讨论内容\n- §5.2 Monitor/Triage/Correct 协议的 \"Correct\" 步骤需根本性修改——引入 DIF→expert review→bias determination→removal 流程\n\n### Limitations\n- 3 点覆盖了主要局限，但第 1 点关于 binary injection 的承认太轻描淡写——应量化 graded shift 的预期影响\n- 缺少对 METABENCH selection bias 和 \"temporal\" = \"cohort-based\" 的讨论\n\n### 格式\n- `\\enlargethispage{2\\baselineskip}` 在 Conclusion 页使用，需验证正文确在 8 页内\n- Page 1 脚注 URL 在 double-blind review 下存在 deanonymization risk（应使用 anonymous submission service）\n- 参考文献格式整体一致，个别 arXiv preprint 缺少 eprint 字段标记",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "report": "# 审稿报告 — Round 19 (Fresh Review)\n\n**论文**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (Long Paper, via ARR)\n**审稿模式**: Fresh（独立初审，无历史记忆）\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n\n---\n\n## Summary\n\n论文将教育测量中的 Mantel-Haenszel DIF (Differential Item Functioning) 分析应用于 METABENCH 的 5,227 个 LLM 模型在 MMLU 12,508 道题目上的二元响应矩阵，发现 2023–2024 模型 cohort 之间 13.5–29.2%（DEFF 校正后）的题目表现出显著 temporal DIF（ETS Category C），且 DIF 信号与 web-overlap contamination labels 近乎独立（Jaccard=0.206）。论文提出 cross-subject matching 策略（在单科目 contamination 下提供构造性 ΔFPR=0 保证）和三步 Monitor/Triage/Correct 审计协议。Semi-synthetic 注入框架验证了检测力，6 个 METABENCH benchmark 的交叉验证确认了结果的泛化性。\n\n---\n\n## Strengths\n\n**S1 [共识]** 规模与系统性出色——5,227 models × 12,508 items 是 IRT-for-LLM 领域最大规模的 DIF 分析，且扩展到 6 个 benchmark 交叉验证（Table 3），增强了 generalizability。\n\n**S2 [共识]** Cross-subject matching 是真正的方法论贡献——ΔFPR=0 的构造性保证（k≤5 subjects）为 DIF 在多科目 benchmark 上的应用提供了可靠 FPR 控制。R1 特别指出这不是 purified subtest matching 的直接推广，而是利用 LLM benchmark 的 multi-subject 结构给出了在教育测试中无对应物的理论保证。\n\n**S3 [共识]** DIF ⊥ contamination labels 的发现有重要理论意义——Jaccard=0.206 表明两种 diagnostic 维度近正交，挑战了将 item-level anomaly 简单归因于 contamination 的直觉（尽管此发现的解释力受限于 proxy 质量，见 N4）。\n\n**S4 [共识]** 多层验证架构设计得当——random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control (Δ=1.08pp)、LOFO robustness、graduated de-duplication 构成系统性 null-hypothesis 校验。\n\n**S5 [共识]** Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 强证据——base 60.1% reference-favoring vs instruct 65.6% focal-favoring，有效排除单一机制驱动假设。\n\n**S6 [共识]** 附录内容丰富（~10 页），覆盖 method details、mechanism analysis、structural controls、DEFF estimation、uncertainty quantification，满足 reproducibility 要求。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [共识: R1提出, R2 AGREE]** DEFF 校正产生 2.16× 估计范围（C%=29.2% vs 13.5%），论文未提供充分分辨依据\n- Simple-mean DEFF (3.87) 和 weighted-mean DEFF (12.79) 给出的 C% 差距超过 2 倍\n- Cluster bootstrap 95% CI [26.7%, 53.2%] 仅对 ~30 个 families 重采样，有效独立单元极少，上界被 Mistral (n=547)/Llama-3 (n=315) 驱动\n- 论文 headline \"17.9–31.3%\" 在多处讨论中倾向引用上界，而 weighted-mean 下界 13.5% 意味着 DIF 规模可能被高估一倍\n- **修改建议**: family 定义 sensitivity analysis（不同粒度分组）；block bootstrap with varying block size 评估 CI 稳定性；正文 Discussion 充分讨论不确定性的实践含义\n\n**N2 [共识: R1提出, R2 AGREE]** Semi-synthetic 注入框架使用 uniform binary flipping，检测力估计可能被系统性高估\n- 所有注入方案（包括 Scheme D difficulty-dependent）均为 binary flipping 变体（0→1），未测试 graded probability shift\n- 现实 contamination 更可能表现为概率偏移（Δp=0.1–0.3），此场景下 MH-DIF 检测力可能远低于报告的 ΔTPR=0.371\n- Limitations 承认 \"ΔTPR values may overestimate detection power\" 但未量化影响\n- **修改建议**: 增加 graded injection scheme (Δp ∈ {0.1, 0.2, 0.3})，报告 minimum detectable probability shift；或提供 analytical bound\n\n**N3 [共识: R1提出, R2 强烈 AGREE]** 缺少 DIF 文献中 impact/bias 关键区分，\"Correct\" 步骤与 mechanism-agnostic 定位逻辑冲突\n- DIF 是 item bias 的必要但非充分条件（Camilli & Shepard, 1994）。如果部分 DIF 由 capability evolution 驱动（construct-relevant \"impact\"），无差别移除会降低 benchmark 敏感度\n- 论文存在内部逻辑冲突：§5.1 声称 mechanism-agnostic → §5.2 建议无差别移除 ETS C items → Limitations 又承认需 expert review\n- Score correction (+2.12pp) 未区分 impact-driven vs bias-driven DIF items 的贡献\n- **修改建议**: §5.2 引入 impact/bias 区分；DIF → expert review → bias determination → removal 标准流程；分别报告 impact/bias candidate 的 rescoring 效应；引用 Camilli & Shepard (1994), Penfield & Camilli (2007)\n\n**N4 [共识: R2提出, R1 AGREE]** DIF-contamination 正交性的 headline finding 依赖质量存疑的 web-overlap proxy\n- Li et al. (2024b) web-overlap labels 是粗糙的 contamination proxy：(1) web-overlap ≠ 实际训练数据包含；(2) synthetic data/instruction tuning 不被捕获；(3) 覆盖率仅 73.8%\n- Jaccard ≈ 0.206 存在两种解释：(a) DIF 与真实 contamination 确实独立（论文解释），(b) proxy 噪声太大导致与任何信号关联都低。论文未排除解释 (b)\n- Abstract/Conclusion 措辞倾向解释 (a)，但 §5.1 呈现了两种解释——措辞不一致\n- **修改建议**: 结论软化为 \"DIF is independent of web-overlap based contamination labels\"；讨论 proxy 局限性；如可能用 Time Travel/memorization scores 交叉验证\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [共识: R1-W1 + R2-W3]** Calendar-year cohort boundary 粗糙，\"temporal\" framing 过窄\n- Release date ≠ training data cutoff；2023 vs 2024 cohorts 在架构、数据规模、训练方法上同时变化\n- Composition control 仅控制 base/instruct 比例，未控制其他 cohort 差异\n- **建议**: §5.1 明确 \"temporal\" 是 \"cohort-based\" 简写；讨论未控制 confounders\n\n**W2 [共识: R1-W2, R2 AGREE]** Cross-subject matching ΔFPR=0 在高覆盖率 contamination (k>5) 下的退化未充分讨论\n- k=20 时 ΔFPR=0.069；internet-scale 预训练可能覆盖 30+ subjects\n- **建议**: 模拟 k=30/50 的 ΔFPR；讨论超出保证范围时的替代策略\n\n**W3 [共识: R1-W3 + R2相关]** Mechanism-agnostic 定位与 contamination-heavy 叙事张力\n- Related Work 以 Contamination Detection 开篇，Figure 1 标注 \"global contamination\"，§4.3 整节做 DIF-contamination 对比\n- **建议**: 将 contamination 对比重新框定为 discriminant validity evidence\n\n**W4 [共识: R2-W1, R1 AGREE]** ETS 阈值从人类考生迁移到 LLM 缺乏充分校准\n- Random-split P99=1.45 是 necessary 但非 sufficient condition\n- **建议**: 明确连接 §4.1 power 分析与 ETS 阈值适用性论证\n\n**W5 [共识: R2-W2, R1 AGREE]** 与 Growing Pains 差异化论证不够深入\n- 缺少在相同 data/items 上的直接比较（优先级较低）\n\n**W6 [共识: R2-W5, R1 AGREE]** Score correction (§4.6) 展示不充分\n- 仅半页篇幅，未区分 ranking reversal 位置（top-10 vs mid-tier）\n- 更根本问题是缺少 impact/bias 区分作为方法论基础（与 N3 关联）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全一致** [AGREE]：\n1. DEFF 2.16× 不确定性范围是实质性方法论缺陷（N1）\n2. Binary flipping 高估检测力，需 graded injection 验证（N2）\n3. Impact/bias 区分缺失是最严重的方法论问题，导致 \"Correct\" 步骤逻辑不自洽（N3）\n4. Web-overlap proxy 质量问题削弱 headline finding（N4）\n5. Calendar-year / temporal framing 过窄（W1）\n6. Cross-subject matching 高 k 退化需进一步量化（W2）\n7. Mechanism-agnostic 与 contamination-heavy 叙事张力需重新框定（W3）\n\n---\n\n## Reviewer Divergence\n\n**D1: 方法论新颖性是否足够**\n- R2 认为 MH-DIF 是 40 年标准方法的直接搬运，novelty 不足以进 Conference\n- R1 反驳：cross-subject matching ΔFPR=0 保证和 DEFF 校正是 LLM-specific 的非平凡贡献；但同意应更清晰区分 \"borrowed methodology\" 和 \"novel adaptations\"\n- **结论**: 方法论贡献介于 \"纯应用\" 和 \"有实质创新\" 之间，取决于 reviewer 对 application novelty 的标准\n\n**D2: Abstract \"because\" 因果暗示**\n- R2 认为 \"scores are not directly comparable because item measurement properties differ systematically\" 隐含因果判断\n- R1 反驳：此处 \"because\" 解释的是不可比性的原因（DIF 的定义），非 DIF 成因的因果推断；\"measurement properties differ\" 在 DIF 框架下是统计事实而非因果声称\n- **结论**: R1 的反驳有力——此处措辞在 psychometrics 框架下是标准用法，不构成因果过度暗示\n\n**D3: METABENCH selection bias 的严重性**\n- R1 指出 Open LLM Leaderboard 存在自选择偏差\n- R2 反驳：关键问题是 bias 是否跨 cohort 差异性存在，若两个时期的 bias 相似则不产生 artifactual DIF；5,227 模型已覆盖大部分提交\n- **结论**: R2 的反驳合理——selection bias 是一般性局限，但对 DIF 结果的特异性影响有限。建议在 Limitations 简要讨论\n\n---\n\n## Questions\n\n1. 如果用 graded probability injection (Δp=0.2) 而非 binary flip，ΔTPR 预期下降到什么水平？是否做过 pilot 或 analytical estimation？\n2. DEFF 的 family 定义是如何确定的？用 50 个 sub-family 而非 30 个 family 时，DEFF 如何变化？\n3. 移除 DIF-C items 后 score shift = +2.12pp（2024 cohort 得分上升）——如果 contamination 是主要机制，预期 2024 得分应下降。如何调和这一方向性矛盾？\n4. 如果使用 Time Travel 或 memorization scores 替代 web-overlap labels，Jaccard 是否仍 ~0.20？\n5. 论文能否区分 \"legitimately harder items for 2024 models\"（capability regression）和 \"construct-irrelevant DIF\"？若不能，\"Correct\" 步骤是否过于简化？\n\n---\n\n## Missing References\n\n**两位 Reviewer 一致推荐**:\n- Camilli, G. & Shepard, L. A. (1994). *Methods for Identifying Biased Test Items*. Sage. — DIF 与 item bias 的经典区分框架\n- Penfield, R. D. & Camilli, G. (2007). Differential item functioning and item bias. In *Handbook of Statistics* (Vol. 26). — impact vs. bias 方法论框架\n\n**R2 推荐（R1 部分同意）**:\n- Test security / item exposure control 文献 (Hau & Chang, 2001; Way, 1998) — 与 benchmark item exposure 概念相关\n- Item banking/equating 在 benchmark 维护中的应用 — 可强化 §5.2 audit protocol\n\n**R2 推荐但 R1 反驳**:\n- Polytomous DIF 方法 (French & Miller, 1996) — R1 指出 MMLU 使用 binary scoring，polytomous DIF 不适用\n- Multi-group CFA / MIMIC models — R1 指出论文已解释选择 MH-DIF 而非 parametric MI 的理由（MMLU 2PL fit 差），CFA 前提不满足\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer）：**未请求**（项目配置未启用）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 4 info）。主要发现：\n\n- **[warning]** Pages 3-6（Method §3 全节）连续 4 页无任何 figure/table，缺乏视觉锚点，易产生阅读疲劳。建议加入方法流程概览图\n- **[warning]** Page 7 三个 display items (Figure 2 + Table 1 + Table 2) 堆积，与前 4 页纯文本形成强烈节奏失衡。建议分散部分 display items\n- **[info]** 主文 5 个 display items / 8 页 = 0.625/页，对实证论文偏少。附录有 12+ 表 + 4 图，部分关键结果可考虑提升到主文\n- **[info]** Figure 1 (ICC schematic) 作为视觉锚点效果优秀\n- **[info]** Table 1 部分单元格文字偏小；Figure 2 x 轴标签字号偏小\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度: 4/5**（两位 Reviewer 均具备 DIF/psychometrics 和 LLM evaluation 领域专业知识）\n\n**评分理由**:\n\n论文在规模（5,227 models × 12,508 items）、实验系统性（7 层验证架构）和 cross-subject matching 方法论贡献上表现出色。DIF ⊥ contamination labels 的发现对社区有价值，base/instruct 方向反转提供了令人信服的 mechanism separation 证据。\n\n但四个 Must-Fix 问题阻止更高评分：(1) DEFF 2.16× 不确定性范围削弱核心定量发现的精度；(2) binary flipping 可能系统性高估检测力；(3) impact/bias 区分的缺失导致审计协议的逻辑不自洽——这是两位 Reviewer 的最强共识；(4) headline finding（DIF-contamination 正交）依赖质量存疑的 proxy。方法论新颖性存在分歧——cross-subject matching 是实质贡献，但整体框架仍以标准 MH-DIF 为核心。\n\n如果作者能：(a) 引入 impact/bias 区分重构审计协议逻辑，(b) 坦诚讨论 web-overlap proxy 局限性并软化正交性声称，(c) 提供 graded injection 的检测力估计，论文有潜力达到 Conference (4.0) 水平。否则 Findings (3.0) 是更合适的归宿。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 2（cross-subject matching ΔFPR=0）是最有说服力的方法论贡献，但叙事中被 Contribution 1（规模与实证发现）抢占了焦点。考虑在 framing 上更突出方法论适配的非平凡性\n- \"temporal score incomparability\" 这一术语在 Introduction 的 parenthetical 定义清晰，但后续混用 \"temporal DIF\" / \"measurement invariance\" / \"score incomparability\" 造成术语分散\n\n### §2 Related Work\n- 以 \"Contamination Detection\" 开篇强化了论文的 contamination framing，与 mechanism-agnostic 定位矛盾。建议以 \"Measurement Invariance in LLM Evaluation\" 或 \"Psychometric Approaches to Benchmark Quality\" 开篇\n- 与 Growing Pains 的对比是充分的，但缺少在相同 items 上的实证比较\n\n### §3 Method\n- §3.2 的 MH-DIF 描述清晰完整，但 LLM-specific challenges（末段 4 点）可以更展开\n- §3.4 Semi-synthetic framework: \"Remark (Zero FPR)\" 的证明干净简洁，是论文的 highlight\n- 视觉审查指出 §3 全节（pages 3-6）无任何 figure/table，建议加入方法流程图\n\n### §4 Experiments\n- §4.2 的多层控制（random split, ability quintile, nearest-neighbor matching）设计严谨\n- §4.3 Ground Truth Mismatch: 标题 \"Ground Truth Mismatch\" 暗示 web-overlap labels 是 ground truth——但论文自己论证了它们不是。建议改为 \"Relationship to Web-Overlap Labels\" 或 \"Discriminant Validity\"\n- §4.5 的 ΔFPR=0 结果是重要发现，但 k>5 退化部分需扩展\n- §4.6 Downstream Impact 偏薄，需补充 top-k ranking 影响和 impact/bias 分析\n\n### §5 Discussion\n- §5.1 的三个 LLM-vs-educational 区分和两种解释框架是好的讨论内容\n- §5.2 Monitor/Triage/Correct 协议的 \"Correct\" 步骤需根本性修改——引入 DIF→expert review→bias determination→removal 流程\n\n### Limitations\n- 3 点覆盖了主要局限，但第 1 点关于 binary injection 的承认太轻描淡写——应量化 graded shift 的预期影响\n- 缺少对 METABENCH selection bias 和 \"temporal\" = \"cohort-based\" 的讨论\n\n### 格式\n- `\\enlargethispage{2\\baselineskip}` 在 Conclusion 页使用，需验证正文确在 8 页内\n- Page 1 脚注 URL 在 double-blind review 下存在 deanonymization risk（应使用 anonymous submission service）\n- 参考文献格式整体一致，个别 arXiv preprint 缺少 eprint 字段标记",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1696 · 2026-05-23T14:17:09.931086+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4369
}
```

</details>

---


### Assistant

_source line 1697 · 2026-05-23T14:17:18.771631+00:00_

审稿报告已投递至 Research Director。

**Round 19 审稿完成**。总结：

**Overall: 3.5 (Borderline Conference)**

4 个 Must-Fix（全部共识）：
1. **DEFF 2.16× 不确定性**——核心定量发现精度不足
2. **Binary flipping 高估检测力**——需 graded injection 验证
3. **Impact/bias 区分缺失**——审计协议逻辑不自洽（最强共识）
4. **Web-overlap proxy 质量**——headline finding 基础不牢

6 个 Should-Fix + 1 个分歧点（新颖性）。Issue Tracker 已同步更新 11 条新 issue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 167

## Round 167

2 recorded events


### User

_source line 1698 · 2026-05-23T14:17:21.542432+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部 Must-Fix (N1–N3) 和 Should-Fix (W1–W4) 的逐条回应，并提交给 Review Director。

核心判断：
- **N1 (DEFF)、N2 (binary flipping)、N3 (impact/bias)**：全部 AGREE，其中 N3 是 R1 最有力的批评
- **W1–W3**：全部 AGREE，与我自己的 W3/W4 高度重合
- **W4 (selection bias)**：唯一 REBUT——DIF 分析对 cohort-constant 的 selection bias 具有天然鲁棒性，R1 高估了其严重性

两位 Reviewer 在 5 个关键点上高度一致，维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1699 · 2026-05-23T14:17:33.506225+00:00_

Round 19 审稿已完成。

**最终结果**: Overall 3.5 (Borderline Conference)

审稿报告已投递给 Research Director。两位 Reviewer 在所有关键问题上达成强共识：

- **4 个 Must-Fix**: DEFF 2.16× 不确定性、binary flipping 高估检测力、impact/bias 区分缺失（最强共识）、web-overlap proxy 质量
- **6 个 Should-Fix**: temporal framing 过窄、cross-subject matching 高 k 退化、mechanism-agnostic 叙事张力、ETS 阈值校准、Growing Pains 对比、score correction 展示
- **1 个分歧**: 方法论新颖性——R1 认为 cross-subject matching 是实质贡献，R2 认为整体仍是标准方法搬运

Issue Tracker 已同步更新（11 个新 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 168

## Round 168

62 recorded events


### User

_source line 1700 · 2026-05-25T21:13:06.535285+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1701 · 2026-05-25T21:13:20.917455+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1702 · 2026-05-25T21:13:20.918436+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1703 · 2026-05-25T21:13:34.775983+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1704 · 2026-05-25T21:13:34.776382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1705 · 2026-05-25T21:13:38.039356+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1706 · 2026-05-25T21:13:38.190295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-25T21:13:43.562007+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-25T21:13:44.064579+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1709 · 2026-05-25T21:13:44.065123+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1710 · 2026-05-25T21:13:45.975886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-25T21:13:46.428144+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	% inconsolata is recommended by the official ACL template for typewriter font
11	% aesthetics, but is not strictly necessary. Omitted here as it is not
12	% installed on the build system.
13	% \usepackage{inconsolata}
14	
15	\usepackage{amsmath}
16	\usepackage{booktabs}
17	\usepackage{graphicx}
18	\usepackage{multirow}
19	\usepackage{subcaption}
20	\usepackage{pifont}
21	\usepackage{enumitem}
22	
23	\usepackage{cleveref}
24	
25	\graphicspath{{../figures/paper/}}
26	
27	\setlength{\dbltextfloatsep}{6pt plus 2pt minus 2pt}
28	\setlength{\textfloatsep}{6pt plus 2pt minus 2pt}
29	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
30	\setlength{\intextsep}{4pt plus 2pt minus 2pt}
31	\setlength{\abovecaptionskip}{4pt}
32	\setlength{\belowcaptionskip}{0pt}
33	
34	\title{Temporal Score Incomparability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
35	
36	\begin{document}
37	
38	\maketitle
39	
40	\input{sections/abstract}
41	\input{sections/introduction}
42	\input{sections/related_work}
43	\input{sections/method}
44	\input{sections/experiments}
45	\input{sections/discussion}
46	\input{sections/conclusion}
47	\input{sections/limitations}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---
