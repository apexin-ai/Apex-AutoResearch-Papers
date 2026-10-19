# Director coordination — Part 2 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 33

### Tool call

_source line 324 · 2026-05-22T15:06:23.021224+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1 issues — status updates through Round 4 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），Conjecture 1 未证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"一般情形降级为 Empirical Finding，保留比例情形证明。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound；讨论 ASV interpretation under approximate monotonicity。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 CRITICAL: DPI 论证对一般 K 不完整，V_B(δ) 单调性依赖数值验证。R2 AGREE: C(δ) 线性插值族不满足 stochastic degradation。两位建议降级为 Conjecture 或补全直接证明路径。\"\n    action_items:\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"尝试 mediation 单调性证明 (3h time box)；formal ε bound；ASV degradation 讨论\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"补全 Appendix A.4 直接证明路径（不依赖 DPI），或降格 Theorem 1 为 Proposition/Conjecture\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"Abstract 改为 'proven analytically for confounding and collider'。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Abstract 仍用 'establish'，对仅有 empirical verification 的 3 拓扑是 overclaim。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1-W3: 'Empirical Finding 1' 术语误导，应改为 Numerical Observation 或 Conjecture。R2 强烈同意。Abstract 中 'prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door' 的表述已存在但 Introduction 区分不够清晰。\"\n    action_items:\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal'\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Abstract 'establish' → 'prove for confounding and collider, verify numerically for mediation, M-bias, front-door'\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"将 'Empirical Finding 1' 重命名为 'Numerical Finding 1' 或 'Conjecture 2'；确保全文 proved/verified/conjectured 三级层次清晰\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max 约束。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未被提及。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Section 3.3 已引入 δ_max 约束。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称；empirical sign reversal 仅影响 secondary coefficients\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次 CRITICAL。降级 should-fix。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方升级。'catastrophic' 与 Section 4.4 'primary coefficient never reverses' 自相矛盾。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R2 CRITICAL: Abstract alarm tone 与 realistic 2.1% + primary effect 安全的 tension。R1 AGREE 但指出 83.4% 作为 K≥3 vs K=2 结构断裂量化有理论价值，不应移除。共识：两个数字应同等突出，明确区分 primary/secondary coefficient 风险。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 结构性重写：realistic regime 先行，83.4% 作理论语境；删 'catastrophic'；明确 primary coefficient never reverses\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Abstract/Intro 中 realistic 2.1% 应先于或至少与 83.4% 同等突出；明确区分 any-coefficient vs primary-coefficient 的风险；Introduction 早期承认 primary effect 安全性\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 作为不依赖精确条件的替代讨论。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。已扩展至 23 configs 但均为开源 LLM。\"\n    action_items:\n      - round: 2\n        action: \"Limitations 讨论开源 vs 商业 LLM\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Triple verification narrative 已解决。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Appendix B.5 + Section 4.3 已包含 bootstrap ASV 分析。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Appendix B.6 仅 3/7 拓扑。Algorithm 1 未标注 linear-only caveat。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。Appendix 包含 logistic DGP 确认 sign-flip patterns qualitatively preserved。\"\n    action_items:\n      - round: 2\n        action: \"添加 logistic DGP 模拟\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Algorithm 1 加 caveat；扩展 logistic 至全 7 拓扑\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-topology MAPE range 已报告。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"τ 和 β_T 交替使用。Proposition 编号正文-附录不一致。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。\"\n    action_items:\n      - round: 3\n        action: \"统一 τ/β_T；添加 Proposition 交叉引用\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Stress test 已扩展但正文讨论 non-differential 成立条件的 NLP 场景仍不足。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MAJOR (W4): LLM 文本含 A 和 Y 信息可能违反假设。R2 AGREE 并补充两个具体场景：outcome-conditional prompting 和 few-shot ICL 效应。stress test 仅 ε≤0.10 小偏离，且 DGP 限于 exposure topology。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"正文讨论 non-differential 假设的 NLP 场景\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Limitations 明确列举可能违反假设的 NLP 场景（outcome-conditional prompting, ICL bias）；扩大 stress test 到 structured differential misclassification\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"两篇已引用。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"已扩展至 210,000 matrices + adversarial search。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 issues — updates through Round 4 ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制约 0.5 页\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方 critical。Section 5 在第 9 页开始。desk rejection 风险。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及页数问题。需确认当前 PDF 是否已压缩至 8 页。\"\n    action_items:\n      - round: 3\n        action: \"压缩正文至 8 页\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"需要 precise definition + FWL proof sketch + SIMEX 解释。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1-W8: SIMEX FWL 论证不严格。R2 反驳: FWL 不变性对 SIMEX 是结构性推论。R1 认同 FWL invariance 本身有独立价值 (S3)，但 SIMEX 推论链应更明确。Section 4.4 + Appendix B.2 已有实质内容。\"\n    action_items:\n      - round: 3\n        action: \"添加 matrix-based correction precise definition；FWL proof sketch 放 appendix\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"明确陈述 FWL → SIMEX 的推论链（当前让读者自行推断）\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。Limitations 已包含 'when the outcome Y is also LLM-annotated, outcome misclassification introduces additional bias channels not captured by our analysis'。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 outcome misclassification 段落\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（15+ 数字）\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"R2 Presentation Score 3.5/5: 'Abstract 信息过载——8 个具体数字让读者难以抓住核心 message'。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 精简至 3-5 个核心数字\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Abstract 仍含过多数字，需进一步精简\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少多篇相关引用\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Round 3 缺 5 篇。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 和 R2 均建议新增：Imai et al. (2010), Buonaccorsi (2010)。R2 额外建议：Blackwell et al. (2017), Valeri & VanderWeele (2012), Pangakis et al. (2023)。R1 额外建议：Ogburn & VanderWeele (2012)（已在 bib 中）。\"\n    action_items:\n      - round: 4\n        action: \"添加 Imai et al. (2010), Buonaccorsi (2010), Blackwell et al. (2017), Valeri & VanderWeele (2012), Pangakis et al. (2023) 到 bib 并在相关章节引用\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"Conclusion 已承诺 'Code for ASV computation and all experiments will be publicly released'。R1/R2 Reproducibility 均 4/5。\"\n    action_items:\n      - round: 3\n        action: \"论文中承诺公开代码\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"R2 Novelty 3/5: '核心新颖性在于系统性而非方法论突破'。Dosemeci (1990) 已知 polytomous reversal → 本文新贡献的边界需更清晰。\"\n    action_items:\n      - round: 3\n        action: \"Introduction 添加 novelty delineation\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Introduction 中更明确标注 Dosemeci (1990)/Veierød & Laake (2001) 已知 → 本文扩展的 7 拓扑系统化 + ASV + FWL 为新贡献\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。Limitations 已说明 'our empirical validation applies real LLM confusion matrices to simulated linear DGPs, verifying analytical predictions rather than end-to-end practical guidance'。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 simulated DGP caveat\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 新增 issues ===\n\n  - id: R4-NEW-1\n    category: soundness\n    severity: major\n    summary: \"Eq. (3) 中 λ(C) ∈ [0,1] 未被证明，仅数值验证\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MAJOR (W2): 主文声明 λ(C) ∈ [0,1] 暗示已证，附录仅数值验证。R2 AGREE: 应至少提供 sketch proof 或标注为 assumption。\"\n    action_items:\n      - round: 4\n        action: \"证明 λ(C) ∈ [0,1] 或在主文中标注为 numerical observation/assumption\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-NEW-2\n    category: method\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知，未讨论拓扑误指定后果\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MAJOR (W5): Algorithm 1 依赖正确拓扑，错误拓扑导致错误校正。R2 REBUT: 这是因果推断通用 limitation，但同意应在 Limitations 提及。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加一句关于拓扑误指定的讨论\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-NEW-3\n    category: presentation\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MINOR (W7)。R2 AGREE 并给出机制解释：PPI++ 纠正误分类→恢复精确调整→恢复完整 M-bias spurious path→bias 增大。论文未 connect the dots。\"\n    action_items:\n      - round: 4\n        action: \"Section 4.4 添加一句解释 protective topology 下'纠正=恢复 spurious bias'的机制\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，arXiv preprint 状态未确认\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"lee_wood_doughty2024 是 workshop paper 但未标注；baumann2025 和 messing2026 为 arXiv preprints。\"\n    action_items:\n      - round: 4\n        action: \"检查并标注 workshop papers；确认 arXiv preprints 是否已被接收\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1 issues — status updates through Round 4 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），Conjecture 1 未证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"一般情形降级为 Empirical Finding，保留比例情形证明。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound；讨论 ASV interpretation under approximate monotonicity。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 CRITICAL: DPI 论证对一般 K 不完整，V_B(δ) 单调性依赖数值验证。R2 AGREE: C(δ) 线性插值族不满足 stochastic degradation。两位建议降级为 Conjecture 或补全直接证明路径。\"\n    action_items:\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"尝试 mediation 单调性证明 (3h time box)；formal ε bound；ASV degradation 讨论\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"补全 Appendix A.4 直接证明路径（不依赖 DPI），或降格 Theorem 1 为 Proposition/Conjecture\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"Abstract 改为 'proven analytically for confounding and collider'。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Abstract 仍用 'establish'，对仅有 empirical verification 的 3 拓扑是 overclaim。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1-W3: 'Empirical Finding 1' 术语误导，应改为 Numerical Observation 或 Conjecture。R2 强烈同意。Abstract 中 'prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door' 的表述已存在但 Introduction 区分不够清晰。\"\n    action_items:\n      - round: 2\n        action: \"Abstract 'never' → 'show no sign reversal'\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Abstract 'establish' → 'prove for confounding and collider, verify numerically for mediation, M-bias, front-door'\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"将 'Empirical Finding 1' 重命名为 'Numerical Finding 1' 或 'Conjecture 2'；确保全文 proved/verified/conjectured 三级层次清晰\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"δ_max 约束。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未被提及。确认已修复。\"\n    action_items:\n      - round: 1\n        action: \"引入 δ_max 约束\"\n        assigned_to: agent\n        status: resolved\n    resolution: \"Section 3.3 已引入 δ_max 约束。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称；empirical sign reversal 仅影响 secondary coefficients\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"R2 再次 CRITICAL。降级 should-fix。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方升级。'catastrophic' 与 Section 4.4 'primary coefficient never reverses' 自相矛盾。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R2 CRITICAL: Abstract alarm tone 与 realistic 2.1% + primary effect 安全的 tension。R1 AGREE 但指出 83.4% 作为 K≥3 vs K=2 结构断裂量化有理论价值，不应移除。共识：两个数字应同等突出，明确区分 primary/secondary coefficient 风险。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 结构性重写：realistic regime 先行，83.4% 作理论语境；删 'catastrophic'；明确 primary coefficient never reverses\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Abstract/Intro 中 realistic 2.1% 应先于或至少与 83.4% 同等突出；明确区分 any-coefficient vs primary-coefficient 的风险；Introduction 早期承认 primary effect 安全性\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 作为不依赖精确条件的替代讨论。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。已扩展至 23 configs 但均为开源 LLM。\"\n    action_items:\n      - round: 2\n        action: \"Limitations 讨论开源 vs 商业 LLM\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Triple verification narrative 已解决。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Appendix B.5 + Section 4.3 已包含 bootstrap ASV 分析。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Appendix B.6 仅 3/7 拓扑。Algorithm 1 未标注 linear-only caveat。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。Appendix 包含 logistic DGP 确认 sign-flip patterns qualitatively preserved。\"\n    action_items:\n      - round: 2\n        action: \"添加 logistic DGP 模拟\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Algorithm 1 加 caveat；扩展 logistic 至全 7 拓扑\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Per-topology MAPE range 已报告。Round 2-4 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"τ 和 β_T 交替使用。Proposition 编号正文-附录不一致。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。\"\n    action_items:\n      - round: 3\n        action: \"统一 τ/β_T；添加 Proposition 交叉引用\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Stress test 已扩展但正文讨论 non-differential 成立条件的 NLP 场景仍不足。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MAJOR (W4): LLM 文本含 A 和 Y 信息可能违反假设。R2 AGREE 并补充两个具体场景：outcome-conditional prompting 和 few-shot ICL 效应。stress test 仅 ε≤0.10 小偏离，且 DGP 限于 exposure topology。\"\n    action_items:\n      - round: 2\n        action: \"扩展 stress test\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"正文讨论 non-differential 假设的 NLP 场景\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Limitations 明确列举可能违反假设的 NLP 场景（outcome-conditional prompting, ICL bias）；扩大 stress test 到 structured differential misclassification\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"两篇已引用。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"已扩展至 210,000 matrices + adversarial search。Round 3-4 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 issues — updates through Round 4 ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制约 0.5 页\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"双方 critical。Section 5 在第 9 页开始。desk rejection 风险。\"\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及页数问题。需确认当前 PDF 是否已压缩至 8 页。\"\n    action_items:\n      - round: 3\n        action: \"压缩正文至 8 页\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"需要 precise definition + FWL proof sketch + SIMEX 解释。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1-W8: SIMEX FWL 论证不严格。R2 反驳: FWL 不变性对 SIMEX 是结构性推论。R1 认同 FWL invariance 本身有独立价值 (S3)，但 SIMEX 推论链应更明确。Section 4.4 + Appendix B.2 已有实质内容。\"\n    action_items:\n      - round: 3\n        action: \"添加 matrix-based correction precise definition；FWL proof sketch 放 appendix\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"明确陈述 FWL → SIMEX 的推论链（当前让读者自行推断）\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。Limitations 已包含 'when the outcome Y is also LLM-annotated, outcome misclassification introduces additional bias channels not captured by our analysis'。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 outcome misclassification 段落\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（15+ 数字）\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"R2 Presentation Score 3.5/5: 'Abstract 信息过载——8 个具体数字让读者难以抓住核心 message'。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 精简至 3-5 个核心数字\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Abstract 仍含过多数字，需进一步精简\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少多篇相关引用\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Round 3 缺 5 篇。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 和 R2 均建议新增：Imai et al. (2010), Buonaccorsi (2010)。R2 额外建议：Blackwell et al. (2017), Valeri & VanderWeele (2012), Pangakis et al. (2023)。R1 额外建议：Ogburn & VanderWeele (2012)（已在 bib 中）。\"\n    action_items:\n      - round: 4\n        action: \"添加 Imai et al. (2010), Buonaccorsi (2010), Blackwell et al. (2017), Valeri & VanderWeele (2012), Pangakis et al. (2023) 到 bib 并在相关章节引用\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"Conclusion 已承诺 'Code for ASV computation and all experiments will be publicly released'。R1/R2 Reproducibility 均 4/5。\"\n    action_items:\n      - round: 3\n        action: \"论文中承诺公开代码\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"R2 Novelty 3/5: '核心新颖性在于系统性而非方法论突破'。Dosemeci (1990) 已知 polytomous reversal → 本文新贡献的边界需更清晰。\"\n    action_items:\n      - round: 3\n        action: \"Introduction 添加 novelty delineation\"\n        assigned_to: agent\n        status: in_progress\n      - round: 4\n        action: \"Introduction 中更明确标注 Dosemeci (1990)/Veierød & Laake (2001) 已知 → 本文扩展的 7 拓扑系统化 + ASV + FWL 为新贡献\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: []\n        note: \"Round 4 未明确提及。Limitations 已说明 'our empirical validation applies real LLM confusion matrices to simulated linear DGPs, verifying analytical predictions rather than end-to-end practical guidance'。\"\n    action_items:\n      - round: 3\n        action: \"Limitations 添加 simulated DGP caveat\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 4 新增 issues ===\n\n  - id: R4-NEW-1\n    category: soundness\n    severity: major\n    summary: \"Eq. (3) 中 λ(C) ∈ [0,1] 未被证明，仅数值验证\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MAJOR (W2): 主文声明 λ(C) ∈ [0,1] 暗示已证，附录仅数值验证。R2 AGREE: 应至少提供 sketch proof 或标注为 assumption。\"\n    action_items:\n      - round: 4\n        action: \"证明 λ(C) ∈ [0,1] 或在主文中标注为 numerical observation/assumption\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-NEW-2\n    category: method\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知，未讨论拓扑误指定后果\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MAJOR (W5): Algorithm 1 依赖正确拓扑，错误拓扑导致错误校正。R2 REBUT: 这是因果推断通用 limitation，但同意应在 Limitations 提及。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加一句关于拓扑误指定的讨论\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-NEW-3\n    category: presentation\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"R1 MINOR (W7)。R2 AGREE 并给出机制解释：PPI++ 纠正误分类→恢复精确调整→恢复完整 M-bias spurious path→bias 增大。论文未 connect the dots。\"\n    action_items:\n      - round: 4\n        action: \"Section 4.4 添加一句解释 protective topology 下'纠正=恢复 spurious bias'的机制\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-NEW-4\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，arXiv preprint 状态未确认\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"lee_wood_doughty2024 是 workshop paper 但未标注；baumann2025 和 messing2026 为 arXiv preprints。\"\n    action_items:\n      - round: 4\n        action: \"检查并标注 workshop papers；确认 arXiv preprints 是否已被接收\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-22T15:06:23.122454+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 17078}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-22T15:08:40.294492+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR), Long Paper\n**ARR Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性与完整性）\n**圆桌轮次**: 1 轮（Round 1 + 交叉分享后收敛）\n\n---\n\n## Summary\n\n本文推导了七种 DAG 拓扑下 K 类非差异误分类对因果估计的偏差表达式，证明 exposure 和 IV 拓扑可产生符号反转（K≥3 时结构性可能，K=2 时不可能），其余五种拓扑保持符号。提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱程度，揭示 FWL 不变性导致矩阵修正方法对四种 covariate 拓扑无效。经 23 个真实 LLM 配置 × 7 拓扑 = 161 场景验证，理论预测与 Monte Carlo 模拟一致（grand MAPE 2.0%）。\n\n---\n\n## Strengths\n\n**S1. 系统性填补明确文献空白（R1, R2 共识）。** 现有工作限于 binary misclassification（Teblunthuis 2024，4 DAGs）或单拓扑 categorical 扩展（Lee & Wood-Doughty 2024，仅 confounding）。本文首次在 K≥3 条件下系统覆盖七种拓扑——\"first to characterize across seven topologies\" 经核查成立。\n\n**S2. FWL 不变性是干净优雅的 negative result（R1, R2 共识）。** 证明当 A 作为 covariate 进入回归时，任何对 dummy matrix D* 的线性变换不改变 treatment coefficient。这直接否定了四种拓扑下矩阵修正方法的有效性，有实际指导意义。Table 4 中 Naive/MLA 均为 0.0% 数值验证了这一结论。\n\n**S3. Exposure 符号翻转结果是核心亮点（R1）。** Proposition 6（Appendix A.8）显式构造反例证明 K≥3 即使 C_kk > 0.5 也可翻转；Dirichlet(1,1,1) 下 83.4% 翻转率，realistic diagonal ≥ 0.7 时 2.1%。K=2 control 严格为 0%，确认结构性断裂。\n\n**S4. 实证验证规模充足（R1, R2 共识）。** 23 个真实 LLM confusion matrix（4 模型 × 3 数据集 × 多 prompting）× 7 拓扑 = 161 bias scenarios。Figure 3 直观展示 F₁ 不预测因果风险。\n\n**S5. 附录质量高（R2）。** 23 页中 15 页附录，含完整证明、反例构造、robustness checks（非线性 DGP、cross-K、bootstrap ASV），大幅增强可信度。\n\n**S6. 实用工作流（R1）。** Algorithm 1 提供从 DAG 识别→校正方法选择的完整决策指南。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1 [CRITICAL — R1 首发, R2 AGREE] Theorem 1（envelope monotonicity）证明对一般 K 不完整。**\nTheorem 1 声称 proportional effects 下 |B(C(δ))| 单调非递减。证明引用 DPI（data processing inequality），但 C(δ) = (1-δ)I + δC₀ 线性插值族不满足 stochastic degradation 条件（C(δ₂) = M·C(δ₁) for stochastic M）。论文在 Appendix 中承认 \"the exact degradation factorization... is non-trivial\"。标为 Theorem 的结果解析证明仅对 K=2 对称情形完成。Appendix A.4 存在不依赖 DPI 的直接证明路径（V_W(δ) 单调性），但未升级为完整证明。**必须补全证明或降格为 Conjecture/Proposition。**\n\n**W2 [CRITICAL — R2 首发, R1 AGREE] Abstract/Introduction 对 83.4% 符号反转率的 framing 具有误导性。**\n83.4% 来自 uniform Dirichlet(1,1,1) 先验（含大量 realistic 中不可能出现的近置换矩阵）。Realistic accuracy（diagonal ≥ 0.7）下仅 2.1%。更关键：Section 4.3 显示 primary coefficient never reverses，符号反转仅发生在 secondary coefficients with small |β|。但 Abstract 以 alarm tone 将 83.4% 置于最突出位置。R1 指出 83.4% 作为 K≥3 vs K=2 结构断裂量化有理论价值不应移除。**共识：两个数字应同等突出，明确区分 primary/secondary coefficient 风险。**\n\n### Should-Fix\n\n**W3 [MAJOR — R1 首发, R2 AGREE] Eq. (3) 中 λ(C) ∈ [0,1] 未被证明。**\nSection 3.2 Mediation 段声明 λ(C) ∈ [0,1]，但 Appendix A.5 中的推导仅数值验证。如果 λ(C) 可超出 [0,1]，mediation bias 的解释将根本改变。应至少提供 sketch proof 或标注为 assumption。\n\n**W4 [MAJOR — R1 首发, R2 强烈 AGREE] \"Empirical Finding 1\" 术语误导。**\n\"Empirical Finding\" 通常指真实数据发现，而非 Monte Carlo 数值验证。这模糊了已证明结果（Proposition 1: confounding, collider）和未证明结果（mediation, M-bias, front-door）的严格区分。应改为 \"Numerical Finding 1\" 或升级为 Conjecture/Proposition。全文应建立 Proved → Numerically verified → Conjectured 的清晰三级层次。\n\n**W5 [MAJOR — R1 首发, R2 AGREE] Non-differential misclassification 假设讨论不足。**\nLLM 处理的文本可能同时含 A 和 Y 信息。R2 补充两个具体违反场景：(1) outcome-conditional prompting；(2) few-shot ICL 中 demonstration examples 引入的 systematic error。Stress test（Appendix B.5）仅 ε ≤ 0.10 小偏离且限于 exposure topology。应在 Limitations 中明确列举可能违反的 NLP 场景。\n\n**W6 [MAJOR — R2 首发, R1 REBUT] ASV 方法论创新有限——E-value 的直接移植？**\nR2 认为 ASV 核心思路是 E-value 框架的移植（将 unmeasured confounding strength 替换为 misclassification severity δ）。R1 反驳：技术差异实质性——(1) E-value 参数化标量 Γ 天然单调，ASV 将 K×K matrix 映射到 1D 路径需额外证明 monotonicity；(2) 三种 ASV 类型 vs E-value 单类型；(3) topology-dependent ranking 是核心贡献。**分歧未完全解决，但 R1 的技术区分有 merit。建议作者更明确定位 ASV 的贡献边界。**\n\n**W7 [MAJOR — R2 首发, R1 REBUT] 论文广度有余深度不足。**\nR2 认为同时覆盖 bias taxonomy + ASV + correction + empirical validation 导致每个方向偏浅。R1 反驳：系统性比较是核心贡献，sign-flip 二分法、FWL 不变性、ASV vulnerability ranking 均需跨拓扑才能发现。**分歧未完全解决——这是论文定位问题而非技术错误。**\n\n**W8 [MAJOR — R1 首发, R2 REBUT（降级为 Limitation）] DAG 拓扑必须先验已知。**\nAlgorithm 1 依赖正确拓扑输入。R2 认为这是因果推断通用 limitation（E-values 和 robustness values 同样需要），但同意应在 Limitations 中提及。共识：在 Limitations 添加一句 \"our framework assumes the causal DAG is correctly specified\"。\n\n### Minor\n\n**W9 [MINOR — R1 首发, R2 AGREE] Conjecture 1 的 ε < 0.06 bound 可能依赖 DGP 参数。** 当 τ 很小时 6% 相对偏差可能影响推断。建议报告 ε 在多组 DGP 参数下的 sensitivity。\n\n**W10 [MINOR — R1 首发, R2 AGREE] PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释。** R2 给出了推论链（PPI++ 纠正误分类 → 恢复精确调整 → 恢复 M-bias spurious path → bias 增大），论文应 connect the dots。\n\n**W11 [MINOR — R2] Abstract 信息过载——8+ 具体数字让读者难以抓住核心 message。**\n\n**W12 [MINOR — R2] 引用格式：lee_wood_doughty2024 为 workshop paper 未标注；baumann2025/messing2026 为 arXiv preprints 状态未确认。**\n\n---\n\n## Reviewer Consensus\n\n以下问题双方独立达成一致（标注 [AGREE]）：\n\n1. **83.4% framing 的 overclaim 问题**是本文最大的 presentation 缺陷（R1-Q3 = R2-W1 CRITICAL）\n2. **Theorem 1 DPI 论证不完整**（R1-W1 CRITICAL = R2 AGREE）\n3. **三拓扑符号保持无解析证明 + Empirical Finding 术语误导**（R1-W2/W3 = R2-W2）\n4. **λ(C) ∈ [0,1] 未证明**（R1-W2 = R2 AGREE）\n5. **Non-differential assumption 讨论不足**（R1-W4 = R2-W5）\n6. **FWL 不变性和 Exposure 符号翻转是 genuine contributions**（R1-S2/S3 = R2-S1/S2）\n7. **实证验证规模充足，附录质量高**（R1-S5 = R2-S3/S5）\n8. **Overall 3.5 Borderline Conference**\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 评估 |\n|------|-----|-----|------|\n| ASV 创新度 | REBUT: 技术差异实质性 | E-value 直接移植 | R1 论据更强——K×K→1D mapping + topology-dependent ranking 有实质区别 |\n| 广度 vs 深度 | REBUT: 系统性是核心贡献 | Technical report 感 | 论文定位问题，非技术错误 |\n| 拓扑先验假设 | MAJOR weakness | 通用 limitation，非本文特有 | R2 论据更强——但 Limitations 应提及 |\n| SIMEX FWL 严格性 | 不够严格 | 结构性推论，无需额外形式化 | R2 论据更强——FWL 对 SIMEX 的推论是直接的 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Abstract 中 83.4% 与 Section 4.3 \"primary coefficient never reverses\" 如何调和？是否考虑区分 primary/secondary coefficient 风险？\n\n**Q2.** Theorem 1 的 V_B(δ) 单调性：C(δ) 线性插值族是否满足 stochastic degradation 条件？如果不满足，是否有不依赖 DPI 的替代证明路径？\n\n**Q3.** 是否存在使 λ(C) ∉ [0,1] 的 confusion matrix？如果不存在，能否提供 sketch proof？\n\n**Q4.** Empirical Finding 1 是否做过 adversarial search（而非仅 random sampling）寻找违反案例？\n\n**Q5.** Non-differential misclassification 在哪些常见 NLP 标注任务中可能被违反？Stress test 是否覆盖了 structured（非 random）differential misclassification？\n\n**Q6.** ASV linear interpolation C(δ) 在实际非线性错误退化模式下的鲁棒性？\n\n**Q7.** DSL 对 M-bias 的 -267% RMSE 和 PPI++ 的 -88%——能否解释 protective topology 下\"纠正 = 恢复 spurious bias\"的机制？\n\n**Q8.** Multi-LLM ensemble 标注时框架如何扩展？Kim et al. (2025) 发现的 60% 跨模型错误相关性如何影响 non-differential 假设？\n\n---\n\n## Missing References\n\n以下引用由 R1/R2 共同或独立建议：\n\n1. **Imai, Keele & Yamamoto (2010)** \"Identification, Inference and Sensitivity Analysis for Causal Mediation Effects\" — mediation 敏感性分析，与 ASV mediation 直接可比（R1 + R2）\n2. **Buonaccorsi (2010)** \"Measurement Error: Models, Methods, and Applications\" — measurement error 标准教材（R1 + R2）\n3. **Blackwell, Honaker & King (2017)** \"A Unified Approach to Measurement Error and Missing Data\" — 社会科学 measurement error 框架（R2）\n4. **Valeri & VanderWeele (2012)** \"Mediation Analysis Allowing for Exposure-Mediator Interactions\" — mediator misclassification（R2）\n5. **Pangakis, Wolken & Fasching (2023)** \"Automated Annotation with Generative AI Requires Validation\" — LLM 标注验证（R2）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本项目未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：error。** 视觉审查 Agent 因 rate limit 错误退出（\"You've hit your limit · resets May 23, 4pm UTC\"），未能完成 PDF 渲染检查。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5（Borderline Conference）**\n**置信度: 4/5**\n\n| ACL ARR 维度 | R1 | R2 | 综合 |\n|-------------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Presentation | — | 3.5 | 3.5 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**支持接收的理由：**\n- 填补了 K≥3 标注误差 × 多因果拓扑的真实文献空白\n- FWL 不变性和 exposure 符号翻转是 genuine novel contributions\n- 实证验证规模充足（161 scenarios），theory-MC 一致性强\n- 附录质量高，再现性好\n\n**阻碍接收的理由：**\n- Theorem 1 证明不完整——核心理论贡献的 soundness 受损\n- 83.4% framing 与 \"primary coefficient never reverses\" 之间的 tension 是 integrity concern\n- 三拓扑符号保持无解析证明，论文中 proved/verified/conjectured 层次不够清晰\n- ASV 方法论新颖性有争议——系统性扩展 vs 方法论突破\n\n**接收路径（→ 4.0 Conference）：**\n1. 补全 Theorem 1 证明（直接路径，不依赖 DPI）或降格为 Conjecture\n2. 修正 Abstract/Introduction framing：realistic 2.1% 与 83.4% 同等突出，明确区分 primary/secondary coefficient\n3. 建立 Proved → Numerically verified → Conjectured 三级层次\n4. 扩充 non-differential assumption 的 NLP 场景讨论\n5. 补充 5 篇遗漏引用\n\n**当前版本判断：** 介于 Conference 和 Findings 之间。如果 Theorem 1 证明问题和 framing 问题在 camera-ready 中解决，可达 Conference 水平。当前更偏向 Findings track。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息过载：8+ 具体数字。建议保留 3-5 个核心数字。\n- 83.4% 与 2.1% 的顺序和权重需调整——realistic regime 应先行。\n- \"prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door\" 的表述是准确的（已区分 prove/verify），但需确保 Introduction 保持同样清晰。\n\n### Introduction\n- Motivation → gap → contribution 逻辑链基本通顺。\n- 第 2 段 \"83.4% of K=3 confusion matrices cause sign reversal\" 出现太早且太突出——读者尚无上下文判断 Dirichlet(1,1,1) 的实际意义。\n- Contribution 3（correction guidance）的篇幅分配与其在主文中的深度不匹配。\n\n### Related Work\n- 覆盖面良好，三段结构清晰。\n- 缺 5 篇引用（见 Missing References）。\n- lee_wood_doughty2024 应标注为 workshop paper。\n\n### Method (Section 3)\n- Bias expressions 推导结构清晰。\n- Proposition 1 条件 (a)(b) 的充分条件表述需更仔细——collider 条件 |τ| > √(Var(g)Var(h))/E[Var(T|A)] 在实践中是否常满足？\n- \"Empirical Finding 1\" → 改为 \"Numerical Finding 1\"。\n- ASV 的 C(δ) 参数化合理，δ_max 约束正确。但 linear interpolation 的局限性讨论可更深入。\n\n### Experiments (Section 4)\n- Theory-MC agreement（MAPE 2.0%）令人满意。IV 的 5.5% 需解释（论文已提及 Wald estimator variance amplification）。\n- Table 1 和 Figure 2 是论文最有力的展示。\n- Section 4.3 empirical validation 结构良好——\"primary coefficient never reverses\" 是重要发现但在 Abstract 中未体现。\n- Correction guidance（Section 4.4）偏浅——5 种方法一段半，缺乏失败机制的深入解释。\n\n### Conclusion & Limitations\n- Limitations 覆盖了主要 concern（non-differential assumption, linear SEM, single annotator, K=3 derivations）。\n- 应增加：拓扑误指定、outcome misclassification（已有但可强化）、开源 LLM only。\n- 承诺代码公开——好。\n\n### Appendix\n- 质量高。证明基本完整（除 Theorem 1 的 DPI gap）。\n- 反例构造（Proposition 6）严格。\n- Bootstrap ASV、logistic DGP、cross-K robustness 增强可信度。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR), Long Paper\n**ARR Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性与完整性）\n**圆桌轮次**: 1 轮（Round 1 + 交叉分享后收敛）\n\n---\n\n## Summary\n\n本文推导了七种 DAG 拓扑下 K 类非差异误分类对因果估计的偏差表达式，证明 exposure 和 IV 拓扑可产生符号反转（K≥3 时结构性可能，K=2 时不可能），其余五种拓扑保持符号。提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱程度，揭示 FWL 不变性导致矩阵修正方法对四种 covariate 拓扑无效。经 23 个真实 LLM 配置 × 7 拓扑 = 161 场景验证，理论预测与 Monte Carlo 模拟一致（grand MAPE 2.0%）。\n\n---\n\n## Strengths\n\n**S1. 系统性填补明确文献空白（R1, R2 共识）。** 现有工作限于 binary misclassification（Teblunthuis 2024，4 DAGs）或单拓扑 categorical 扩展（Lee & Wood-Doughty 2024，仅 confounding）。本文首次在 K≥3 条件下系统覆盖七种拓扑——\"first to characterize across seven topologies\" 经核查成立。\n\n**S2. FWL 不变性是干净优雅的 negative result（R1, R2 共识）。** 证明当 A 作为 covariate 进入回归时，任何对 dummy matrix D* 的线性变换不改变 treatment coefficient。这直接否定了四种拓扑下矩阵修正方法的有效性，有实际指导意义。Table 4 中 Naive/MLA 均为 0.0% 数值验证了这一结论。\n\n**S3. Exposure 符号翻转结果是核心亮点（R1）。** Proposition 6（Appendix A.8）显式构造反例证明 K≥3 即使 C_kk > 0.5 也可翻转；Dirichlet(1,1,1) 下 83.4% 翻转率，realistic diagonal ≥ 0.7 时 2.1%。K=2 control 严格为 0%，确认结构性断裂。\n\n**S4. 实证验证规模充足（R1, R2 共识）。** 23 个真实 LLM confusion matrix（4 模型 × 3 数据集 × 多 prompting）× 7 拓扑 = 161 bias scenarios。Figure 3 直观展示 F₁ 不预测因果风险。\n\n**S5. 附录质量高（R2）。** 23 页中 15 页附录，含完整证明、反例构造、robustness checks（非线性 DGP、cross-K、bootstrap ASV），大幅增强可信度。\n\n**S6. 实用工作流（R1）。** Algorithm 1 提供从 DAG 识别→校正方法选择的完整决策指南。\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**W1 [CRITICAL — R1 首发, R2 AGREE] Theorem 1（envelope monotonicity）证明对一般 K 不完整。**\nTheorem 1 声称 proportional effects 下 |B(C(δ))| 单调非递减。证明引用 DPI（data processing inequality），但 C(δ) = (1-δ)I + δC₀ 线性插值族不满足 stochastic degradation 条件（C(δ₂) = M·C(δ₁) for stochastic M）。论文在 Appendix 中承认 \"the exact degradation factorization... is non-trivial\"。标为 Theorem 的结果解析证明仅对 K=2 对称情形完成。Appendix A.4 存在不依赖 DPI 的直接证明路径（V_W(δ) 单调性），但未升级为完整证明。**必须补全证明或降格为 Conjecture/Proposition。**\n\n**W2 [CRITICAL — R2 首发, R1 AGREE] Abstract/Introduction 对 83.4% 符号反转率的 framing 具有误导性。**\n83.4% 来自 uniform Dirichlet(1,1,1) 先验（含大量 realistic 中不可能出现的近置换矩阵）。Realistic accuracy（diagonal ≥ 0.7）下仅 2.1%。更关键：Section 4.3 显示 primary coefficient never reverses，符号反转仅发生在 secondary coefficients with small |β|。但 Abstract 以 alarm tone 将 83.4% 置于最突出位置。R1 指出 83.4% 作为 K≥3 vs K=2 结构断裂量化有理论价值不应移除。**共识：两个数字应同等突出，明确区分 primary/secondary coefficient 风险。**\n\n### Should-Fix\n\n**W3 [MAJOR — R1 首发, R2 AGREE] Eq. (3) 中 λ(C) ∈ [0,1] 未被证明。**\nSection 3.2 Mediation 段声明 λ(C) ∈ [0,1]，但 Appendix A.5 中的推导仅数值验证。如果 λ(C) 可超出 [0,1]，mediation bias 的解释将根本改变。应至少提供 sketch proof 或标注为 assumption。\n\n**W4 [MAJOR — R1 首发, R2 强烈 AGREE] \"Empirical Finding 1\" 术语误导。**\n\"Empirical Finding\" 通常指真实数据发现，而非 Monte Carlo 数值验证。这模糊了已证明结果（Proposition 1: confounding, collider）和未证明结果（mediation, M-bias, front-door）的严格区分。应改为 \"Numerical Finding 1\" 或升级为 Conjecture/Proposition。全文应建立 Proved → Numerically verified → Conjectured 的清晰三级层次。\n\n**W5 [MAJOR — R1 首发, R2 AGREE] Non-differential misclassification 假设讨论不足。**\nLLM 处理的文本可能同时含 A 和 Y 信息。R2 补充两个具体违反场景：(1) outcome-conditional prompting；(2) few-shot ICL 中 demonstration examples 引入的 systematic error。Stress test（Appendix B.5）仅 ε ≤ 0.10 小偏离且限于 exposure topology。应在 Limitations 中明确列举可能违反的 NLP 场景。\n\n**W6 [MAJOR — R2 首发, R1 REBUT] ASV 方法论创新有限——E-value 的直接移植？**\nR2 认为 ASV 核心思路是 E-value 框架的移植（将 unmeasured confounding strength 替换为 misclassification severity δ）。R1 反驳：技术差异实质性——(1) E-value 参数化标量 Γ 天然单调，ASV 将 K×K matrix 映射到 1D 路径需额外证明 monotonicity；(2) 三种 ASV 类型 vs E-value 单类型；(3) topology-dependent ranking 是核心贡献。**分歧未完全解决，但 R1 的技术区分有 merit。建议作者更明确定位 ASV 的贡献边界。**\n\n**W7 [MAJOR — R2 首发, R1 REBUT] 论文广度有余深度不足。**\nR2 认为同时覆盖 bias taxonomy + ASV + correction + empirical validation 导致每个方向偏浅。R1 反驳：系统性比较是核心贡献，sign-flip 二分法、FWL 不变性、ASV vulnerability ranking 均需跨拓扑才能发现。**分歧未完全解决——这是论文定位问题而非技术错误。**\n\n**W8 [MAJOR — R1 首发, R2 REBUT（降级为 Limitation）] DAG 拓扑必须先验已知。**\nAlgorithm 1 依赖正确拓扑输入。R2 认为这是因果推断通用 limitation（E-values 和 robustness values 同样需要），但同意应在 Limitations 中提及。共识：在 Limitations 添加一句 \"our framework assumes the causal DAG is correctly specified\"。\n\n### Minor\n\n**W9 [MINOR — R1 首发, R2 AGREE] Conjecture 1 的 ε < 0.06 bound 可能依赖 DGP 参数。** 当 τ 很小时 6% 相对偏差可能影响推断。建议报告 ε 在多组 DGP 参数下的 sensitivity。\n\n**W10 [MINOR — R1 首发, R2 AGREE] PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释。** R2 给出了推论链（PPI++ 纠正误分类 → 恢复精确调整 → 恢复 M-bias spurious path → bias 增大），论文应 connect the dots。\n\n**W11 [MINOR — R2] Abstract 信息过载——8+ 具体数字让读者难以抓住核心 message。**\n\n**W12 [MINOR — R2] 引用格式：lee_wood_doughty2024 为 workshop paper 未标注；baumann2025/messing2026 为 arXiv preprints 状态未确认。**\n\n---\n\n## Reviewer Consensus\n\n以下问题双方独立达成一致（标注 [AGREE]）：\n\n1. **83.4% framing 的 overclaim 问题**是本文最大的 presentation 缺陷（R1-Q3 = R2-W1 CRITICAL）\n2. **Theorem 1 DPI 论证不完整**（R1-W1 CRITICAL = R2 AGREE）\n3. **三拓扑符号保持无解析证明 + Empirical Finding 术语误导**（R1-W2/W3 = R2-W2）\n4. **λ(C) ∈ [0,1] 未证明**（R1-W2 = R2 AGREE）\n5. **Non-differential assumption 讨论不足**（R1-W4 = R2-W5）\n6. **FWL 不变性和 Exposure 符号翻转是 genuine contributions**（R1-S2/S3 = R2-S1/S2）\n7. **实证验证规模充足，附录质量高**（R1-S5 = R2-S3/S5）\n8. **Overall 3.5 Borderline Conference**\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 评估 |\n|------|-----|-----|------|\n| ASV 创新度 | REBUT: 技术差异实质性 | E-value 直接移植 | R1 论据更强——K×K→1D mapping + topology-dependent ranking 有实质区别 |\n| 广度 vs 深度 | REBUT: 系统性是核心贡献 | Technical report 感 | 论文定位问题，非技术错误 |\n| 拓扑先验假设 | MAJOR weakness | 通用 limitation，非本文特有 | R2 论据更强——但 Limitations 应提及 |\n| SIMEX FWL 严格性 | 不够严格 | 结构性推论，无需额外形式化 | R2 论据更强——FWL 对 SIMEX 的推论是直接的 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Abstract 中 83.4% 与 Section 4.3 \"primary coefficient never reverses\" 如何调和？是否考虑区分 primary/secondary coefficient 风险？\n\n**Q2.** Theorem 1 的 V_B(δ) 单调性：C(δ) 线性插值族是否满足 stochastic degradation 条件？如果不满足，是否有不依赖 DPI 的替代证明路径？\n\n**Q3.** 是否存在使 λ(C) ∉ [0,1] 的 confusion matrix？如果不存在，能否提供 sketch proof？\n\n**Q4.** Empirical Finding 1 是否做过 adversarial search（而非仅 random sampling）寻找违反案例？\n\n**Q5.** Non-differential misclassification 在哪些常见 NLP 标注任务中可能被违反？Stress test 是否覆盖了 structured（非 random）differential misclassification？\n\n**Q6.** ASV linear interpolation C(δ) 在实际非线性错误退化模式下的鲁棒性？\n\n**Q7.** DSL 对 M-bias 的 -267% RMSE 和 PPI++ 的 -88%——能否解释 protective topology 下\"纠正 = 恢复 spurious bias\"的机制？\n\n**Q8.** Multi-LLM ensemble 标注时框架如何扩展？Kim et al. (2025) 发现的 60% 跨模型错误相关性如何影响 non-differential 假设？\n\n---\n\n## Missing References\n\n以下引用由 R1/R2 共同或独立建议：\n\n1. **Imai, Keele & Yamamoto (2010)** \"Identification, Inference and Sensitivity Analysis for Causal Mediation Effects\" — mediation 敏感性分析，与 ASV mediation 直接可比（R1 + R2）\n2. **Buonaccorsi (2010)** \"Measurement Error: Models, Methods, and Applications\" — measurement error 标准教材（R1 + R2）\n3. **Blackwell, Honaker & King (2017)** \"A Unified Approach to Measurement Error and Missing Data\" — 社会科学 measurement error 框架（R2）\n4. **Valeri & VanderWeele (2012)** \"Mediation Analysis Allowing for Exposure-Mediator Interactions\" — mediator misclassification（R2）\n5. **Pangakis, Wolken & Fasching (2023)** \"Automated Annotation with Generative AI Requires Validation\" — LLM 标注验证（R2）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本项目未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：error。** 视觉审查 Agent 因 rate limit 错误退出（\"You've hit your limit · resets May 23, 4pm UTC\"），未能完成 PDF 渲染检查。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5（Borderline Conference）**\n**置信度: 4/5**\n\n| ACL ARR 维度 | R1 | R2 | 综合 |\n|-------------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Presentation | — | 3.5 | 3.5 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**支持接收的理由：**\n- 填补了 K≥3 标注误差 × 多因果拓扑的真实文献空白\n- FWL 不变性和 exposure 符号翻转是 genuine novel contributions\n- 实证验证规模充足（161 scenarios），theory-MC 一致性强\n- 附录质量高，再现性好\n\n**阻碍接收的理由：**\n- Theorem 1 证明不完整——核心理论贡献的 soundness 受损\n- 83.4% framing 与 \"primary coefficient never reverses\" 之间的 tension 是 integrity concern\n- 三拓扑符号保持无解析证明，论文中 proved/verified/conjectured 层次不够清晰\n- ASV 方法论新颖性有争议——系统性扩展 vs 方法论突破\n\n**接收路径（→ 4.0 Conference）：**\n1. 补全 Theorem 1 证明（直接路径，不依赖 DPI）或降格为 Conjecture\n2. 修正 Abstract/Introduction framing：realistic 2.1% 与 83.4% 同等突出，明确区分 primary/secondary coefficient\n3. 建立 Proved → Numerically verified → Conjectured 三级层次\n4. 扩充 non-differential assumption 的 NLP 场景讨论\n5. 补充 5 篇遗漏引用\n\n**当前版本判断：** 介于 Conference 和 Findings 之间。如果 Theorem 1 证明问题和 framing 问题在 camera-ready 中解决，可达 Conference 水平。当前更偏向 Findings track。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息过载：8+ 具体数字。建议保留 3-5 个核心数字。\n- 83.4% 与 2.1% 的顺序和权重需调整——realistic regime 应先行。\n- \"prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door\" 的表述是准确的（已区分 prove/verify），但需确保 Introduction 保持同样清晰。\n\n### Introduction\n- Motivation → gap → contribution 逻辑链基本通顺。\n- 第 2 段 \"83.4% of K=3 confusion matrices cause sign reversal\" 出现太早且太突出——读者尚无上下文判断 Dirichlet(1,1,1) 的实际意义。\n- Contribution 3（correction guidance）的篇幅分配与其在主文中的深度不匹配。\n\n### Related Work\n- 覆盖面良好，三段结构清晰。\n- 缺 5 篇引用（见 Missing References）。\n- lee_wood_doughty2024 应标注为 workshop paper。\n\n### Method (Section 3)\n- Bias expressions 推导结构清晰。\n- Proposition 1 条件 (a)(b) 的充分条件表述需更仔细——collider 条件 |τ| > √(Var(g)Var(h))/E[Var(T|A)] 在实践中是否常满足？\n- \"Empirical Finding 1\" → 改为 \"Numerical Finding 1\"。\n- ASV 的 C(δ) 参数化合理，δ_max 约束正确。但 linear interpolation 的局限性讨论可更深入。\n\n### Experiments (Section 4)\n- Theory-MC agreement（MAPE 2.0%）令人满意。IV 的 5.5% 需解释（论文已提及 Wald estimator variance amplification）。\n- Table 1 和 Figure 2 是论文最有力的展示。\n- Section 4.3 empirical validation 结构良好——\"primary coefficient never reverses\" 是重要发现但在 Abstract 中未体现。\n- Correction guidance（Section 4.4）偏浅——5 种方法一段半，缺乏失败机制的深入解释。\n\n### Conclusion & Limitations\n- Limitations 覆盖了主要 concern（non-differential assumption, linear SEM, single annotator, K=3 derivations）。\n- 应增加：拓扑误指定、outcome misclassification（已有但可强化）、开源 LLM only。\n- 承诺代码公开——好。\n\n### Appendix\n- 质量高。证明基本完整（除 Theorem 1 的 DPI gap）。\n- 反例构造（Proposition 6）严格。\n- Bootstrap ASV、logistic DGP、cross-K robustness 增强可信度。\n"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-22T15:08:44.515208+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4220
}
```

</details>

---


### Assistant

_source line 328 · 2026-05-22T15:08:50.787644+00:00_

审稿报告已投递。

**审稿完成总结：**

- **Overall: 3.5（Borderline Conference）**，R1/R2 独立一致
- **2 个 CRITICAL**：Theorem 1 证明不完整 + 83.4% framing overclaim
- **6 个 MAJOR**：λ(C) 未证明、Empirical Finding 术语误导、non-differential 讨论不足、ASV 创新度（有分歧）、广度 vs 深度（有分歧）、拓扑先验假设
- **4 个 MINOR**：ε bound 参数依赖、PPI++ 机制解释、Abstract 信息过载、引用格式
- **接收路径**：补全 Theorem 1 证明 + 修正 framing + 建立 proved/verified/conjectured 三级层次 → 可达 4.0 Conference
- Issue Tracker 已同步更新（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 329 · 2026-05-22T15:08:52.293462+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 的 6 条 Weaknesses 中 4 条 [AGREE]、2 条 [REBUT]：
- **同意**：83.4% framing 需调整（W1）、三拓扑证明缺口（W2）、非差异性讨论不足（W5）、引用格式（W6）
- **反驳**：ASV 相对 E-value 的创新性（W3，技术挑战实质不同）、breadth vs depth 的取舍（W4，系统性比较是核心贡献）

两位 Reviewer 总评均为 3.5 (Borderline Conference)，主要共识集中在 Theorem 1 证明不完整和 proved/verified/conjectured 层次混淆上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 330 · 2026-05-22T15:09:02.678268+00:00_

审稿报告已投递至 Research Director。

**Round 4 审稿结论：Overall 3.5（Borderline Conference）**

两位 Reviewer 独立评分一致，核心共识：
1. **Theorem 1 证明不完整**（CRITICAL）——DPI 论证对一般 K 不成立，需补全或降格
2. **83.4% framing overclaim**（CRITICAL）——与 "primary coefficient never reverses" 存在严重 tension
3. **三拓扑符号保持无解析证明**，proved/verified/conjectured 层次不清晰
4. **Non-differential assumption 讨论不足**
5. **缺 5 篇引用**

分歧点（ASV 创新度、广度 vs 深度）不影响总评收敛。接收路径明确：补全 Theorem 1 证明 + 修正 framing + 建立三级理论层次。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 35

## Round 35

50 recorded events


### User

_source line 331 · 2026-05-22T16:51:29.401693+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-22T16:51:46.313347+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-22T16:51:46.416553+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-22T16:51:52.867056+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 335 · 2026-05-22T16:51:52.917788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-22T16:51:59.230207+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-22T16:52:00.240866+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-22T16:52:00.744488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-22T16:52:00.744960+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 340 · 2026-05-22T16:52:00.850418+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{method}
39	
40	% ── Figures ──
41	
42	\begin{figure*}[t]
43	\centering
44	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
45	\vspace{-6pt}
46	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
47	\label{fig:dag_taxonomy}
48	\end{figure*}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
53	\vspace{-6pt}
54	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
55	\label{fig:bias_distribution}
56	\end{figure*}
57	
58	\input{experiments}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix_proofs}
66	
67	\end{document}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 105
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-22T16:52:00.850910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 105
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-22T16:52:06.445299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-22T16:52:07.910486+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-22T16:52:08.011364+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 345 · 2026-05-22T16:52:08.162334+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-22T16:52:08.821041+00:00_

-rw-r--r-- 1 ubuntu ubuntu 881643 May 22 16:44 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 910
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-22T16:52:15.782477+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on my search results, here's a comprehensive overview of the EMNLP 2026 ARR call for papers submission guidelines and author instructions:

## Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insi
…[truncated 1735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9337
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-22T16:52:19.515350+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit anonymity requirements style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit anonymity requirements style files"
  }
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-22T16:52:20.434369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-22T16:52:20.612239+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), the sign reversal rate is 2.1\%, exclusively in secondary coefficients---the primary treatment effect never reverses in any of 23 empirical LLM configurations. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 177
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-22T16:52:20.678418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-22T16:52:20.679029+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with $C_{kk} {>} 0.5$ to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension, not of a specific error rate~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even when every diagonal entry exceeds $0.5$~\cite{veirod_laake2001}. This structural break is quantifiable: under a uniform Dirichlet$(1,1,1)$ prior spanning the full parameter space, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient (0\%
…[truncated 2387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-22T16:52:26.830462+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit anonymity requirements style files"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results for ACL Rolling Review 2026 submission requirements, here's the information on submission format, page limits, anonymity requirements, and style files:

## Page Limits

Long papers can be up to 8 pages, and short papers up to 4 pages, excluding ethical considerations and limitations. Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7315
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-22T16:52:31.207505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-22T16:52:31.661691+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This assumption is natural when the LLM annotates treatment labels from source documents without access to outcome information, though it may be violated by outcome-conditional prompting or few-shot demonstrations encoding outcome associations (see Limitations).
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
17	
18	\subsection{Multi-Class Bias Expressions}
19	\label{sec:bias_expressions}
20	
21	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
22	
23	\paragraph{Confounding ($A$ = confounder).}
24	
…[truncated 12321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-22T16:52:31.662268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-22T16:52:32.120701+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagona
…[truncated 8742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-22T16:52:32.171482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-22T16:52:32.579950+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose structured approaches to reduce LLM measurement error, and \citet{kim_garg2025} showed 60\% error correlation across models. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the broader landscape. These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal
…[truncated 1123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 408
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-22T16:52:32.580521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-22T16:52:32.684382+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary treatment effect never reverses, but 61\% of exposure configurations reverse a secondary coefficient. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinear models (Appendix~\ref{sec:logistic_dgp}) remain open. We address misclassification of $A$ by a single annotator; outcome misclassification and correlated multi-annotator settings~\cite{kim_garg2025} introduce additional bias channels not captured here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-22T16:52:37.945478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-22T16:52:40.668348+00:00_

File content (31027 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 2722
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-22T16:52:40.922353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-22T16:52:40.973065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-22T16:52:41.077693+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},
31	  volume    = {50},
32	  number    = {1},
33	  pages     = {237--291},
34	  doi       = {10.1162/coli\_a\_00502},
35	}
36	
37	@incollection{bound2001measurement,
38	  author    = {Bound, John and Brown, Charles and Mathiowetz, Nancy},
39	  title     = {Measurement Error in Survey Data},
40	  booktitle = {Handbook of Econometrics},
41	  editor    = {Heckman, James J. and Leamer, Edward E.},
42	  year      = {2001},
43	  volume    = {5},
44	  chapter   = {59},
45	  pages     = {3705--3843},
46	  publisher = {Elsevier},
47	}
48	
49	@article{richardson1993bayesian,
50	  author    = {Richardson, Sylvia and Gilks, Walter R.},
51	  title     = {A {Bayesian} Approach to Measurement Error Problems in Epidemiology Using Conditional Independence Models},
52	  journal   = {Amer
…[truncated 13873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 104
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-22T16:52:44.818628+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf (861KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 3896
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-22T16:53:06.914353+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-22T16:53:06.965060+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-22T16:53:07.926585+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1012
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-22T16:53:08.178344+00:00_

issues:
  # === Round 1 issues ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），证明不完整"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 4
    mentions:
      - round: 1
        reviewers: [R1, R2]
        note: "R1 首发，R2 AGREE。"
      - round: 2
        reviewers: [R1, R2]
        note: "一般情形降级为 Empirical Finding，保留比例情形证明。"
      - round: 3
        reviewers: [R1, R2]
        note: "R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound。"
      - round: 4
        reviewers: [R1, R2]
        note: "W1 CRITICAL。DPI 证明路径不成立（C(δ) 不满足 stochastic degradation）。Appendix A.4 有 V_W(δ) 直接路径但未升级。必须补全或降格。"
    action_items:
      - round: 2
        action: "一般情形降级为 Empirical Finding"
        assigned_to: agent
        status: done
      - round: 3
        action: "Mediation 证明 + ε bound"
        assigned_to: agent
        status: done
      - round: 4
        action: "补全 Theorem 1 直接证明（V_W(δ) 路径，不依赖 DPI）或降格"
        assigned_to: agent
        status: in_progress
    resolution: ""
    resolution_round: null

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    action_items:
      - round: 3
        action: "Abstract 'establish' → 'prove for confounding and collider, verify numerically for mediation, M-bias, front-door'"
        assigned_to: agent
        status: done
    resolution: "Abstract 已准确区分 prove/verify。R4 确认此表述准确。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。Round 2-4 未再提及。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: in_
…[truncated 11730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T16:53:36.456414+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-22T16:53:36.859887+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-22T16:53:55.101496+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18645
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-22T16:53:55.152225+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 18292
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-22T16:53:55.353378+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**审查侧重：方法严谨性 + 实验验证**\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- 正文 ≤ 8 页（不含 references、limitations、ethics）\n- ACL 模板（review 模式）\n- Double-blind 匿名审稿\n- ARR 统一审稿系统\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **理论正确性**：\n   - Proposition 1（sign preservation）的证明是否完整、严谨？条件是否充分？\n   - Theorem 1（envelope monotonicity）的证明是否成立？proof sketch 是否有逻辑漏洞？\n   - Conjecture 1 的数值验证是否充分？ε bound 是否合理？\n   - Eq.(1)-(3) 的推导是否正确？\n\n2. **实验设计**：\n   - 100,000 Dirichlet 矩阵的采样是否充分代表实际场景？\n   - Theory-MC agreement（MAPE 2.0%）的验证方法是否可靠？\n   - 实证验证（23 LLM configurations × 7 topologies）的覆盖是否充分？\n   - Correction methods 比较（210 configurations）是否公平？\n\n3. **FWL invariance 论证**：\n   - 0% bias reduction 的结论是否严格成立？\n   - 证明路径（column space preservation）是否完备？\n\n4. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM 场景下是否合理？\n   - Linear SEM 假设的限制是否充分讨论？\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**审查侧重：方法严谨性 + 实验验证**\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- 正文 ≤ 8 页（不含 references、limitations、ethics）\n- ACL 模板（review 模式）\n- Double-blind 匿名审稿\n- ARR 统一审稿系统\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **理论正确性**：\n   - Proposition 1（sign preservation）的证明是否完整、严谨？条件是否充分？\n   - Theorem 1（envelope monotonicity）的证明是否成立？proof sketch 是否有逻辑漏洞？\n   - Conjecture 1 的数值验证是否充分？ε bound 是否合理？\n   - Eq.(1)-(3) 的推导是否正确？\n\n2. **实验设计**：\n   - 100,000 Dirichlet 矩阵的采样是否充分代表实际场景？\n   - Theory-MC agreement（MAPE 2.0%）的验证方法是否可靠？\n   - 实证验证（23 LLM configurations × 7 topologies）的覆盖是否充分？\n   - Correction methods 比较（210 configurations）是否公平？\n\n3. **FWL invariance 论证**：\n   - 0% bias reduction 的结论是否严格成立？\n   - 证明路径（column space preservation）是否完备？\n\n4. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM 场景下是否合理？\n   - Linear SEM 假设的限制是否充分讨论？\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-22T16:54:08.171769+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12818
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-22T16:54:08.346754+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**审查侧重：新颖性 + 完整性 + 写作质量**\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- 正文 ≤ 8 页（不含 references、limitations、ethics）\n- ACL 模板（review 模式）\n- Double-blind 匿名审稿\n- ARR 统一审稿系统\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 相对于 Brenner(1993)、Dosemeci(1990)、Veierød & Laake(2001)、TeBlunthuis(2024)、Lee & Wood-Doughty(2024) 等已有工作，本文的增量贡献是什么？\n   - \"首次跨 7 种拓扑系统比较\" 的声明是否成立？\n   - ASV framework 相对于 E-values (VanderWeele & Ding 2017) 的方法论创新是否足够？\n   - FWL invariance 结果作为\"负面结果\"的价值是否充分论证？\n\n2. **相关工作覆盖**：\n   - 是否有重要的遗漏引用？特别关注：measurement error in causal inference、LLM annotation quality、sensitivity analysis、correction methods 四个领域\n   - 对已有工作的定位是否准确、公平？\n\n3. **写作质量**：\n   - Abstract 是否准确概括贡献？是否有过度声称？\n   - Introduction 的动机叙事是否有说服力？\n   - 数字密度是否影响可读性？\n   - 符号使用是否一致？\n   - 全文逻辑流是否顺畅？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 是否符合 ACL 模板（字体、边距、引用格式）？\n   - 匿名规则是否遵守？\n   - Limitations 部分是否充分？\n   - 图表质量和可读性\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**审查侧重：新颖性 + 完整性 + 写作质量**\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_5/submitted.pdf`\n- **目标 venue**: EMNLP 2026 (via ARR)\n- **投稿类别**: Long Paper\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- 正文 ≤ 8 页（不含 references、limitations、ethics）\n- ACL 模板（review 模式）\n- Double-blind 匿名审稿\n- ARR 统一审稿系统\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 相对于 Brenner(1993)、Dosemeci(1990)、Veierød & Laake(2001)、TeBlunthuis(2024)、Lee & Wood-Doughty(2024) 等已有工作，本文的增量贡献是什么？\n   - \"首次跨 7 种拓扑系统比较\" 的声明是否成立？\n   - ASV framework 相对于 E-values (VanderWeele & Ding 2017) 的方法论创新是否足够？\n   - FWL invariance 结果作为\"负面结果\"的价值是否充分论证？\n\n2. **相关工作覆盖**：\n   - 是否有重要的遗漏引用？特别关注：measurement error in causal inference、LLM annotation quality、sensitivity analysis、correction methods 四个领域\n   - 对已有工作的定位是否准确、公平？\n\n3. **写作质量**：\n   - Abstract 是否准确概括贡献？是否有过度声称？\n   - Introduction 的动机叙事是否有说服力？\n   - 数字密度是否影响可读性？\n   - 符号使用是否一致？\n   - 全文逻辑流是否顺畅？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 是否符合 ACL 模板（字体、边距、引用格式）？\n   - 匿名规则是否遵守？\n   - Limitations 部分是否充分？\n   - 图表质量和可读性\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 [CRITICAL] / [MAJOR] / [MINOR]）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-22T16:54:12.001916+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3655
}
```

</details>

---


### Assistant

_source line 380 · 2026-05-22T16:54:21.037300+00:00_

**Round 1 已启动。** 当前状态：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验验证） | 审稿中 |
| Reviewer 2（新颖性 + 完整性 + 写作） | 审稿中 |
| 视觉审查 Agent | 已派发，与 Reviewer 并行执行 |
| 外部审稿（Stanford Agentic Reviewer） | 未启用 |

等待两位 Reviewer 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 381 · 2026-05-22T17:01:20.428608+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (via ARR)
**审查侧重**: 方法严谨性 + 实验验证

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 系统性地刻画了 multi-class 标注误差在 7 种 DAG 拓扑下的传播特性，贡献实质性且实用，但 Theorem 1 对 K≥3 的证明依赖数值验证而非解析证明，核心理论主张的严谨性需要加强。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Theorem 1 证明对 K≥3 不完整（仅数值验证）；sign preservation 条件性在 Table 1 中呈现不够透明 |
| Excitement | 3.5/5 | 问题重要且具实践价值，taxonomy 是首创性工作；但与 NLP community 的核心关注点有一定距离（本质上是统计测量误差理论的应用） |
| Reproducibility | 4/5 | 承诺开源代码；DGP 参数、采样策略均有详细说明；Appendix 提供了充分的实验细节 |
| Confidence | 4/5 | 熟悉因果推断和测量误差文献，仔细检查了主要证明 |

---

## 主要优势

**S1. 系统性的拓扑分类学（首创性贡献）。** 现有文献（Teblunthuis 2024 覆盖 4 种二值 DAG；Lee & Wood-Doughty 2024 覆盖 1 种拓扑）均未系统处理 multi-class 情形下 same confusion matrix 在不同 DAG 拓扑下产生质的不同 bias 的问题。本文覆盖 7 种 canonical topology，建立了从 sign-preserving（confounding, collider）到 sign-reversing（exposure, IV）的完整谱系。

**S2. FWL invariance 负结果干净且重要。** 证明 matrix-based corrections 对 4 种 covariate topology 产生 exactly 0% bias reduction（Appendix B.2，基于 column space preservation），这是一个被标注校正文献忽略的重要发现。证明路径（FWL + invertible M preserves column space）简洁完整。

**S3. 三级证据层次结构透明。** 论文诚实地区分了 (i) 解析证明（confounding, collider sign preservation）、(ii) 数值验证零违反（mediation, M-bias, front-door）、(iii) ε-approximate conjecture，这种透明度是值得肯定的。

**S4. 实证验证有说服力。** 23 个真实 LLM configuration × 7 topologies × 3 datasets（HumAID K=10, VAST K=3, CivilComments K=2），覆盖了 frontier 到 7B 模型，结果与理论预测一致。"Primary coefficient never reverses" 的经验发现（Section 4.4）具有实践指导意义。

**S5. ASV 框架具有实践价值。** 将 E-value 的思路扩展到标注误差场景，三种 ASV 类型（magnitude, significance, sign-flip）对应不同拓扑的失败模式，加上 Algorithm 1 的 correction routing，为从业者提供了可操作的指导。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Theorem 1 对 K ≥ 3 缺乏解析证明，不应标为 "Theorem"**
- 具体位置：Section 3.3 Theorem 1; Appendix B.2
- 问题：Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减，但证明的关键步骤——V_B(δ) 关于 δ 单调不增——对 K=2 通过直接求导证明，对 general K 仅通过数值验证（"verified... numerically across all test configurations with zero violations"，Appendix B.2 第 243 行）。论文自身承认 "the exact degradation factorization C(δ₂) = M·C(δ₁) for a stochastic M is non-trivial for the linear interpolation family"，即关键的信息论退化论证不成立。
- 为什么影响接收：标为 "Theorem" 意味着有完整证明。10,000 个随机矩阵零违反是强数值证据，但不构成证明。ASV 框架的有效性建立在此 monotonicity 上——如果它不成立（即使概率极低），ASV 阈值 δ* 可能不正确。
- 建议修改方向：(a) 将 K ≥ 3 的声明降级为 Proposition（numerical evidence）或 Conjecture，保留 K=2 作为 Theorem；(b) 或完成 general K 的证明——考虑对 C(δ) 的 rational function structure 进行 symbolic computation（V_B(δ) 是 δ 的有理函数，可以验证其导数符号）；(c) 至少在证明中明确标注 "For K ≥ 3, this step is verified numerically; a complete analytic proof remains open."

**N2** [critical] **Table 1 的 sign-flip guarantee checkmarks 掩盖了 DGP 条件性**
- 具体位置：Table 1 (Section 4.2); Proposition 1(a) Section 3.2
- 问题：Table 1 对 confounding, mediation, front-door 标注 ✓（"structural sign-flip guarantee holds"），但这些保证都有 DGP 条件：confounding 需要 sign(τ) = sign(τ + B_OV)；mediation 需要 sign(τ_dir) = sign(τ_total)；front-door 需要 sign(λα_U) = sign(λα_U + Cov(T,f(A)))。这些条件在论文的 DGP 参数下成立（Appendix C.1 Table 5），但并非无条件。论文在 Appendix 第 699-703 行讨论了条件失败的情况（"opposing effects"），说明反例是存在的。
- 为什么影响接收：Table 1 是论文最核心的结果汇总表，读者（尤其是 practitioners）会直接查表做决策。✓ 暗示无条件保证，但实际上是有条件的。如果一个 practitioner 的 confounding 场景恰好 sign(τ) ≠ sign(τ + B_OV)（如 suppression 效应），Table 1 的 ✓ 会给出错误的安全感。
- 建议修改方向：(a) 在 Table 1 中用不同符号区分无条件保证（如 collider 在论文参数下是 |τ| > B̄_col，这也是有条件的）和有条件保证，或加脚注标注条件；(b) 在 caption 中明确 "✓ indicates sign preservation under DGP-specific sufficient conditions (Table 5 in Appendix); ✗ indicates no such condition exists."

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **Conjecture 1 的 "ε-approximately monotonic" 表述可能误导**
- 具体位置：Conjecture 1 (Section 3.3); Table 7 (Appendix B.12)
- 问题：Table 7 显示 60-98% 的矩阵存在非单调步骤（如 confounding K=3: 8467/10000，M-bias: 9791/10000）。虽然 worst-case magnitude 很小（非 IV: < 0.056），但 "ε-approximately monotonic" 这个术语可能给读者一种"几乎单调"的印象，而实际上是"几乎处处非单调但偏差量级很小"。此外，Table 8 显示在 τ=0.1（mediation ε=0.130）和 τ=5.0（front-door ε=0.139）时 ε 明显超过 0.06。
- 建议：(a) 明确 ASV 的推荐适用范围（如 |τ| ≥ 0.5 in standardized units），并在 Conjecture 正文中加入 τ 范围限制；(b) 讨论 ε/η 误差对 δ* 的影响——当 ε=0.13, η=0.10 时，δ* 误差可达 1.3 units，这在 ASV 通常为 0-2 的范围内并非 negligible。

**W2** [major] **Non-differential misclassification 假设在 LLM 场景下需要更充分讨论**
- 具体位置：Definition 1 (Section 3.1); Limitations (Section 5)
- 问题：Definition 1 假设 P(A*|A,Y,Z) = P(A*|A)，即 LLM 标注不依赖 outcome。论文在 Limitations 中列举了可能违反的场景（outcome-conditional prompting, few-shot demonstrations encoding outcome associations）。但现代 LLM 标注实践中，prompt 往往包含 context（可能间接包含 Y 信息），RAG 流程可能检索到包含 Y 的文档，chain-of-thought 推理可能利用 Y 相关的先验知识。Appendix B.8 的 stress test 覆盖了 4 topologies 但仅测试 ε ≤ 0.10 的温和违反，且 sign-flip rate 在 ε=0.10 时对 IV（K=3, low-quality CM）达到 7%。
- 建议：(a) 在 Section 3.1 更充分讨论这一假设何时成立/不成立（不仅在 Limitations 中简述）；(b) 提供一个简单的 diagnostic（如检验 C 在 Y 的不同水平上是否一致）帮助 practitioners 验证该假设。

**W3** [major] **线性 SEM 假设对 FWL invariance 结论的影响讨论不足**
- 具体位置：Algorithm 1 caption; Appendix B.9
- 问题：FWL invariance 是论文的核心负结果之一（matrix-based corrections 对 4 种拓扑无效），但它根本性地依赖线性 SEM。在非线性模型（如 logistic regression, probit）中，FWL 不成立，column space argument 失效。Algorithm 1 的 caption 提到 "FWL-based routing may not apply under nonlinear models"，但这个 caveat 在正文中没有讨论。Appendix B.9 的 logistic DGP 检查仅测试 sign-flip pattern 是否 preserved，没有直接测试 FWL invariance 是否在 logistic 下打破。
- 建议：(a) 在 Section 4.5 的 FWL invariance 段落中加入一句话讨论非线性情形；(b) 在 logistic DGP 实验中增加一个 correction experiment，验证 Naive plug-in 在 logistic 下是否仍然 0% reduction。

**W4** [minor] **Exposure topology 的 "primary coefficient never reverses" 缺乏理论保证**
- 具体位置：Section 4.4 第 78 行; Abstract
- 问题：论文反复强调 "the primary treatment effect never reverses" 并在 abstract 中写 "the primary treatment effect never reverses in any of 23 empirical LLM configurations"。这是一个经验发现（23 configurations × exposure topology），但论文未给出理论保证。从 Eq.(2) 看，primary coefficient 的 sign preservation 取决于 weights w_jk 的结构——当 primary category 的 w_jk 不将 opposite-sign categories 的权重超过 primary 自身时成立。论文没有证明在什么条件下这一定成立。
- 建议：(a) 将 abstract 中的措辞改为 conditional（"In our experiments, the primary..."）；(b) 如果可能，给出 primary coefficient sign preservation 的充分条件（如 diagonal dominance + primary category 有最大 prevalence）。

**W5** [minor] **Theory-MC agreement 的 MAPE 2.0% 可能掩盖尾部偏差**
- 具体位置：Section 4.2 第 15 行
- 问题：Grand MAPE 2.0% across 126 scenarios 是 mean；IV topology 的 MAPE 高达 5.5%。MAPE 对真值接近零的情况敏感（小绝对误差 → 大相对误差）。论文未报告 max absolute error 或 coverage（如 95% MC estimate 落在 analytic plim 的 ±x% 内的比例）。
- 建议：补充 absolute error 的 median 和 max，或 coverage 统计，特别是对 IV topology。

---

## 小问题（不影响接收）

1. **Section 3.2 Eq.(1)**: 公式用了 Z'Z 但 Z 的定义依赖 A*（dummies of A*），而目标参数 τ 是 X 的系数。公式和文字的 notation 可以更清晰——Z 是否包含 intercept？
2. **Section 4.2**: "18 LLM configurations × 7 topologies" 但 Section 4.4 说 "23 LLM configurations"。请确认是 18 还是 23（Theory-MC validation 用了 18？Empirical validation 用了 23？需要说明差异）。
3. **Table 2 (Appendix)**: ASV 表的 "Rank" 列将 exposure 列为 "---"，但 exposure 有 sign-flip ASV，在 vulnerability 谱系中应有位置。
4. **Appendix B.8 Table 4**: ε=0.00 baseline 的 sign-flip rate 是 2.0%，但 Section 4.2 报告 diagonal ≥ 0.7 条件下是 2.1%。差异可能源于采样噪声，但应明确说明。
5. **Conjecture 1 排除 IV 的理由**: "the Wald estimator exhibits singularities when the first-stage coefficient passes through zero"——这本身就是 IV 标注误差危害的一部分，将其排除使 Conjecture 回避了最难的情况。建议明确说明 IV 的 ASV 是如何处理 singularity 的（是否在 singular 附近截断？）。
6. **References**: Baumann et al. (2025) 标注为 arXiv preprint。如果有正式发表版本应更新。

---

## Questions（需要作者回答）

**Q1.** Theorem 1 对 K ≥ 3 的证明能否完成？V_B(δ) 作为 δ 的有理函数，其分子分母的 degree 有限——是否尝试过对 K=3 进行 symbolic differentiation 并验证导数符号？

**Q2.** Sign preservation 的 DGP 条件（如 sign(τ) = sign(τ + B_OV) for confounding）在实践中如何验证？Practitioner 不知道真实 τ 和 B_OV。论文建议 "compute ASV under candidate DAGs and report the most conservative"（Limitations），但这不回答条件验证的问题。

**Q3.** 论文提到 "same-sign β_k produce only attenuation" (Section 4.4 第 78 行)。这是否意味着当所有 category 的 treatment effect 同号时，exposure 也有 sign preservation guarantee？如果是，这是一个重要结论，应在正文中 formalize。

**Q4.** PPI++ 需要 gold labels。在 correction experiments 中，gold label 比例是多少？Table 3 报告 47.0% RMSE reduction——这在什么 gold label fraction 下实现？是否有 sensitivity to gold label size 的分析？

**Q5.** FWL invariance 在非线性模型下是否 breakdown？是否可以用 logistic DGP 验证 Naive plug-in 不再是 0% reduction？

**Q6.** Dirichlet(1,1,1) 先验下 83.4% sign reversal 对实际 NLP 研究者意味着什么？如果改用拟合 empirical LLM confusion matrices 的 informative prior（如 Dirichlet(α) with α > 1 集中在 diagonal-dominant 区域），sign reversal rate 会如何变化？

---

## Missing References

1. **Frölich (2007)** "Nonparametric IV estimation in the presence of endogenous regressors" 或 **Mahajan (2006)** "Identification and estimation of regression models with misclassification" — IV with mismeasured instruments 的理论基础，与 Section 3.2 的 IV topology 直接相关。
2. **Kang & Schafer (2007)** "Demystifying Double Robustness" — doubly robust estimators 可能绕过 FWL invariance 限制，值得在 correction guidance 部分讨论。
3. 最近的 **Zhang & Spirtes (2024)** 或 **Zhang et al. (2024)** 关于 causal discovery with measurement error 的工作——虽然论文假设 DAG 已知，但讨论 DAG uncertainty 时应引用。

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**
**置信度: 4/5**

本文对一个实际重要的问题（LLM 标注误差在因果推断中的传播）做出了系统性贡献。7 种拓扑的 bias taxonomy、FWL invariance 负结果、ASV 框架都是 genuine contributions。经验验证覆盖面广、设计合理。

阻止我给出 4.0 的主要原因是 Theorem 1 的证明完整性问题（N1）：一个标为 Theorem 的核心结果不应依赖数值验证。如果作者能 (a) 完成 K≥3 的证明或 (b) 诚实降级为 numerical result + conjecture，我会上调评分。Table 1 的条件性问题（N2）是 presentation 层面的，修改成本低但影响读者理解。

论文的 excitement 对 EMNLP 来说处于边界——核心是统计测量误差理论，NLP-specific 的贡献在于 empirical validation with real LLM configurations 和 practical guidance。但考虑到 LLM-as-annotator 是 NLP 社区的热点话题，实际影响力不低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 382 · 2026-05-22T17:01:39.184070+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），核心问题集中在 Theorem 1 对 K≥3 证明不完整（N1）和 Table 1 条件性标注不透明（N2）。等待 Reviewer 2 意见后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 383 · 2026-05-22T17:01:42.040786+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：
- **Overall 3.5 (Borderline Conference)**，置信度 4/5
- **两个 Critical 问题**：(1) Theorem 1 对 K≥3 仅有数值验证而非解析证明，不应标为 Theorem；(2) Table 1 的 sign-flip guarantee checkmarks 掩盖了 DGP 条件性
- **三个 Major 问题**：Conjecture 1 的 ε 在极端 τ 下超标；non-differential misclassification 假设讨论不足；FWL invariance 的线性 SEM 依赖性未在正文充分讨论
- **主要优势**：7 拓扑 taxonomy 首创、FWL invariance 负结果干净、三级证据层次透明、实证验证充分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-22T17:01:57.576669+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 38

## Round 38

8 recorded events


### User

_source line 385 · 2026-05-22T17:01:59.098630+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**审查侧重**: 新颖性 + 完整性 + 写作质量
**评分标准来源**: [ACL ARR Review Form](https://aclrollingreview.org/reviewform) + [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)

---

### Summary

本文系统研究了 K≥3 类 LLM 标注误差在七种因果 DAG 拓扑下的偏差传播特性，证明二元情形下的 "toward-null" 保证在多类情形下结构性失效（exposure 和 IV 拓扑可产生符号反转）。提出了 Annotation Sensitivity Values (ASV) 敏感性分析框架和基于 FWL 不变性的校正不可行性负面结果，并用 23 个真实 LLM 配置进行了经验验证。

---

### Strengths

**S1. 系统性的跨拓扑分析填补了明确的研究空白。** 先前工作（Brenner 1993; Dosemeci 1990; Veierød & Laake 2001）各自分析单一拓扑；TeBlunthuis (2024) 覆盖 4 个 DAG 但限于 K=2；Lee & Wood-Doughty (2024) 扩展至分类变量但仅覆盖 confounding。本文首次在统一框架下用**同一**混淆矩阵比较七种拓扑的偏差行为，"首次跨 7 种拓扑系统比较"的声明经我核查是成立的（Section 1, para 3; Related Work Section 2）。

**S2. 理论结果的层次化处理体现了学术诚实。** 论文明确区分了三个层次：(i) 解析证明（Proposition 1(a,b), Theorem 1）、(ii) 数值验证且零违反（mediation, M-bias, front-door 的符号保持）、(iii) ε-近似猜想（Conjecture 1）。这种分层比笼统声称"我们证明了"要可信得多（Section 3.2, para "Our theoretical results..."）。

**S3. FWL 不变性的负面结果具有重要实用价值。** 证明矩阵类校正方法（naive plug-in, MLA, SIMEX）对 4 种拓扑的偏差减少率恰好为 0%（Section 4.5; Appendix B.2），这是一个被标注校正文献忽略的结果。FWL 证明本身虽对熟悉该定理的人来说较直接，但其在标注误差场景下的应用是新的，且结论对实践者有直接指导意义。

**S4. 经验验证覆盖面广且设计合理。** 23 个真实 LLM 配置 × 7 拓扑 = 161 个场景（Section 4.4），使用了 HumAID (K=10)、VAST (K=3)、CivilComments (K=2) 三个数据集和四个 LLM，涵盖 zero-shot 和 few-shot。理论-MC 一致性 MAPE 2.0% 表明解析表达式的准确性（Section 4.2）。

**S5. ASV 框架是 E-value 的有意义扩展。** 三个关键差异——(1) 参数化 K×K 矩阵到 1D 路径需要证明近似单调性、(2) 三种 ASV 类型对应不同失效模式、(3) 与 FWL 不变性结合指导校正选择——使其超越了 E-value 的简单迁移（Section 3.3）。

**S6. 论文整体结构清晰，逻辑流畅。** 从动机（LLM annotators + K≥3 的结构性突变）→ 理论（bias expressions + 符号保持）→ 敏感性分析（ASV）→ 校正指导（FWL）→ 经验验证，叙事链条完整。

---

### Weaknesses

**N1 [MAJOR] 非差异性误分类假设在 LLM 场景下的适用性存疑，论文对此的讨论不够充分。**
- 具体位置：Definition 1 (Section 3.1); Limitations (Section 5)
- 问题：论文假设 $P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$（Definition 1），并指出"当 LLM 从源文档标注而不接触结果信息时此假设自然成立"。但在 CSS 的典型应用中，LLM 处理的文本本身同时包含 treatment 和 outcome 相关的信号。例如：对产品评论标注情感（treatment）时，文本中的购买行为描述（outcome proxy）对 LLM 是可见的。Few-shot demonstrations 编码了 treatment-outcome 关联（论文承认），但更根本的是文本作为共同原因导致的结构性差异性。Appendix B.5 的 stress test 仅测试了人为添加的差异参数 ε，并未测试 LLM 诱导的真实差异性模式。
- 建议：在 Limitations 中更明确地讨论"文本作为共同原因"的机制，并提供至少一个定性分析说明差异性对各拓扑结论的影响方向。

**N2 [MAJOR] 线性结构方程的限制性未被充分验证。**
- 具体位置：Section 3 全部 bias expressions; Appendix B.6 (logistic DGP)
- 问题：所有 bias 表达式基于线性 SEM 推导。Appendix B.6 的 logistic DGP 检查仅验证了 sign-flip 模式的一致性（|ΔSFτ| < 0.02），但未验证偏差量级、ASV 排名、或 FWL 不变性在非线性模型下是否成立。具体而言，FWL 定理是线性投影的性质——在非线性模型中，矩阵类校正可能并非无效。论文声称的"matrix-based corrections are provably ineffective for four topologies"严格来说仅在线性框架下成立。
- 建议：明确 FWL 不变性结论的适用范围限于线性模型；考虑在 logistic DGP 下额外验证至少一个拓扑的校正效果。

**N3 [MAJOR] Conjecture 1 在正文中的呈现方式不够审慎。**
- 具体位置：Conjecture 1 (Section 3.3, p.5)
- 问题：Conjecture 1 覆盖了 5 个拓扑的 envelope 单调性，但部分条件下 ε 可达 0.14（front-door, extreme τ）甚至 0.15（exposure, extreme-tail matrices）。在 ASV 的实际使用中，如果单调性不成立，报告的 δ* 可能偏离真实阈值达 ε/η = 0.14/0.10 = 1.4 个 δ 单位——这并非"可忽略"。论文在 p.5 底部承认了这一点但措辞轻描淡写（"negligible at the recommended η = 10%"）。此外，exposure 在 extreme-tail 处 ε≈0.15 的条件写在括号中，容易被忽略。
- 建议：在 Conjecture 1 的表述中更显式地标注 ε 的范围和条件；在讨论 ASV 可靠性时用独立段落说明 ε 对 δ* 精度的影响，而非一句话带过。

**W1 [MINOR] "Primary coefficient never reverses"的声称缺乏理论保证。**
- 具体位置：Abstract ("the primary treatment effect never reverses in any of 23 empirical LLM configurations"); Section 4.4
- 问题：这是一个基于 23 个配置的经验观察，而非结构性证明。论文在 Section 4.4 给出了直觉解释（"Sign reversal requires opposite-sign treatment effects across categories"），但 primary coefficient 不反转取决于混淆矩阵权重与系数的具体关系，并非一个无条件保证。对于 K=10（HumAID）且类别高度不平衡的情况，primary coefficient 的稳健性可能减弱。
- 建议：将 Abstract 的措辞从暗示普遍性改为明确其经验性质，或提供 primary coefficient 保持的充分条件。

**W2 [MINOR] 数字密度较高，影响部分段落的可读性。**
- 具体位置：Section 1 para 2 ("83.4%...2.1%...0%...K=2...K=3"); Section 4.4 ("62.8%...326%...12.2%...32.4%...62-92%")
- 问题：Introduction 第二段在 3 行内出现了 6 个百分比数字；Section 4.4 的 Cross-K comparison 段落密集堆积数字。这些数字各自有意义，但密集呈现降低了阅读体验。
- 建议：在 Introduction 中精简至最关键的 2-3 个数字，其余移至实验部分；Section 4.4 考虑用表格呈现 cross-K 比较。

**W3 [MINOR] 符号使用存在轻微不一致。**
- 具体位置：Section 3.2
- 问题：在 confounding 拓扑中，$\tau$ 是 X 的系数（treatment effect），偏差发生在对 A 的控制不完全上；在 exposure 拓扑中，biased 量是 $\hat{\beta}_j$（A* 本身的系数），$\tau$ 的角色隐含。两种设定下"treatment effect"的含义不同，但论文未显式区分。此外，Eq.(3) 使用 $\lambda(C)$，而 Proposition 4 (Appendix) 重新定义了 $\lambda(C)$ 的含义。
- 建议：在 Section 3.1 添加一句明确 $\tau$ 在不同拓扑下的具体含义。

**W4 [MINOR] ClinicalBERT 案例研究（Appendix B.3）过于简略。**
- 具体位置：Appendix B.3
- 问题：作为唯一的端到端应用案例，该案例仅用一段文字描述了一个回顾性分析，没有提供具体的数值结果（偏差量级、ASV 值等）。这削弱了论文声称的"topology-aware analysis is necessary for valid causal inference"在实际场景中的说服力。
- 建议：扩展案例研究，提供 ASV 诊断输出和校正方法选择的具体示例。

---

### Questions

**Q1.** 对于 CSS 中常见的场景（如 LLM 标注情感作为 confounder），文本同时包含 treatment 和 outcome 信号导致的差异性误分类，会如何影响各拓扑的符号保持结论？是否有方向性的定性分析？

**Q2.** 数值验证使用的 DGP 参数（τ=2.0, α=(1.5,−1.0), β=(1.0,−0.5)）是否代表 CSS 研究中的典型效应量？社会科学中效应通常较小（τ < 0.5），在小效应下 Proposition 2/3 的 sign preservation 条件是否更容易被违反？

**Q3.** ASV 框架假设研究者知道正确的 DAG 拓扑。在实践中拓扑常常不确定，论文建议"compute ASV under candidate DAGs and report the most conservative"（Limitations）。但如果候选拓扑包含 exposure（可能反转）和 confounding（不会反转），如何定义"most conservative"？

**Q4.** FWL 不变性结论在非线性模型（如 logistic regression 控制分类 confounder）下是否成立？如果不成立，matrix-based corrections 在非线性模型下是否可能有效？

**Q5.** 论文使用 Dirichlet(1,1,1) 先验生成随机混淆矩阵。这是均匀分布，包含大量实际中不可能出现的混淆矩阵（如近置换矩阵）。83.4% 的符号反转率是否会在更现实的先验下大幅降低？论文在 realistic subspace（diagonal ≥ 0.7）下报告了 2.1%——这一数字是否更具参考价值？

---

### Missing References

**M1.** Lash, Fox, Fink (2009/2021), *Applying Quantitative Bias Analysis to Epidemiologic Data*, Springer. 这是量化偏差分析（包括误分类偏差）的标准教科书，与 ASV 框架的定位直接相关，应在 Related Work 的 sensitivity analysis 段落中引用。

**M2.** Kuroki & Pearl (2014), "Measurement Bias and Effect Restoration in Causal Inference", *Biometrika*. 从图模型角度分析 measurement bias 和效应恢复，与 starred-node DAG 框架直接相关。

**M3.** Mohan, Pearl, Tian (2013), "Missing Data as a Causal and Probabilistic Problem", *UAI*. 将缺失数据和测量误差统一在图模型框架下，与 Blackwell et al. (2017) 的统一框架互补。

---

### 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤ 8 页 | ✓ | 正文 pp.1-8，Conclusion + Limitations 在 p.8 结束 |
| ACL 模板 | ✓ | `\usepackage[review]{acl}`，双栏，字体/边距正确 |
| 匿名 | ✓ | "Anonymous ACL submission"，正文无自引暴露 |
| Limitations | ✓ | p.8，约 150 词，覆盖 4 个局限点 |
| References | ✓ | pp.9-10，格式一致 |
| 图表质量 | ✓ | Figure 1-3 清晰可读；Table 1-2 格式规范 |

---

### 主要优势总结

- 填补了跨拓扑系统比较的明确空白，claim 有据
- 理论层次分明（证明/验证/猜想），学术诚实
- FWL 不变性负面结果对实践者有直接指导意义
- 经验验证覆盖面广（23 LLM configs × 7 topologies × 3 datasets）
- ASV 框架提供了可操作的敏感性分析工具

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 系统性的跨拓扑分析填补了明确的研究空白，理论层次分明且经验验证充分，但非差异性假设在 LLM 场景下的适用性、线性模型的限制性、以及 Conjecture 1 的 ε 边界使其在主会议接收的边界。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 主要 claims 有充分支撑：Proposition 1、Theorem 1 有完整证明；数值验证覆盖 100K 矩阵且零违反；经验验证 MAPE 2.0%。扣分因素：Conjecture 1 的 ε 在极端条件下较大；部分结果仅在线性 SEM 下成立 |
| Excitement | 3/5 | 问题重要且时机好（LLM annotators 快速普及），但对统计学/流行病学社区是 incremental advancement（各拓扑的单独结果已知），NLP 社区可能对此理论较重的工作兴趣有限 |
| Reproducibility | 4/5 | 提供了完整的 DGP 参数、实验配置说明和 Algorithm 1；承诺代码公开；但当前无代码/数据链接 |
| Overall Assessment | 3.5/5 | Borderline Conference — 贡献明确且执行扎实，但 (1) 非差异性假设限制了对 LLM 场景的适用性，(2) 线性 SEM 限制了通用性，(3) 部分核心结果是 conjecture 而非 theorem |
| Confidence | 4/5 | 我熟悉 measurement error in causal inference 和 sensitivity analysis 文献，仔细检查了主要证明和数值设计 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-22T17:03:00.773076+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（侧重方法严谨性 + 实验验证）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分：3.5 (Borderline Conference)，置信度 4/5\n维度：Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n### Reviewer 1 的 Strengths\n- S1: 系统性的拓扑分类学（首创性贡献）\n- S2: FWL invariance 负结果干净且重要\n- S3: 三级证据层次结构透明\n- S4: 实证验证有说服力（23 LLM configs × 7 topologies × 3 datasets）\n- S5: ASV 框架具有实践价值\n\n### Reviewer 1 的 Must-Fix 问题\n\n**N1 [CRITICAL] Theorem 1 对 K≥3 缺乏解析证明，不应标为 \"Theorem\"**\n- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减\n- 关键步骤 V_B(δ) 对 δ 单调不增：K=2 有解析证明，K≥3 仅有数值验证（10,000 矩阵零违反）\n- R1 认为标为 \"Theorem\" 意味着有完整证明，数值验证不够\n- 建议：降级为 Proposition/Conjecture，或完成 K≥3 的解析证明\n\n**N2 [CRITICAL] Table 1 的 sign-flip guarantee checkmarks 掩盖了 DGP 条件性**\n- Table 1 对 confounding, mediation, front-door 标注 ✓，但这些保证都有 DGP 条件（如 confounding 需要 sign(τ) = sign(τ + B_OV)）\n- Practitioners 可能直接查表做决策，✓ 暗示无条件保证\n- 建议：用不同符号区分有条件/无条件保证，或在 caption 中明确标注\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1 [MAJOR] Conjecture 1 的 \"ε-approximately monotonic\" 可能误导**\n- Table 7 显示 60-98% 的矩阵存在非单调步骤\n- 在 τ=0.1（mediation ε=0.130）和 τ=5.0（front-door ε=0.139）时 ε 明显超过 0.06\n- ε/η 误差对 δ* 的影响在 ASV 0-2 范围内并非 negligible\n- 建议：明确 ASV 推荐适用范围，独立段落讨论 ε 对 δ* 精度的影响\n\n**W2 [MAJOR] Non-differential misclassification 假设需要更充分讨论**\n- LLM 标注实践中 prompt 包含 context（可能间接包含 Y 信息）；RAG 可能检索到包含 Y 的文档\n- Appendix B.8 的 stress test 覆盖 4 topologies 但仅测试 ε ≤ 0.10 的温和违反\n- 建议：在 Section 3.1 更充分讨论何时成立/不成立，提供诊断方法\n\n**W3 [MAJOR] 线性 SEM 假设对 FWL invariance 的影响讨论不足**\n- FWL invariance 根本性依赖线性 SEM，在 logistic/probit 中 FWL 不成立\n- Algorithm 1 的 caveat 仅在 caption 中，正文未讨论\n- Appendix B.9 的 logistic DGP 检查未测试 FWL invariance 是否在 logistic 下打破\n- 建议：在 Section 4.5 讨论非线性情形，在 logistic DGP 中验证 correction\n\n### Reviewer 1 的 Minor 问题\n- W4: \"Primary coefficient never reverses\" 缺乏理论保证\n- W5: Theory-MC MAPE 2.0% 可能掩盖尾部偏差\n\n### Reviewer 1 的 Questions\n- Q1: Theorem 1 K≥3 证明能否通过 symbolic differentiation 完成？\n- Q2: Sign preservation 的 DGP 条件在实践中如何验证？\n- Q3: Same-sign β_k 是否给出 exposure sign preservation guarantee？\n- Q4: PPI++ gold label 比例和 sensitivity 分析？\n- Q5: FWL invariance 在非线性模型下是否 breakdown？\n- Q6: 83.4% 在 informative prior 下会如何变化？\n\n### Reviewer 1 的 Missing References\n1. Frölich (2007) 或 Mahajan (2006) — IV with mismeasured instruments\n2. Kang & Schafer (2007) — doubly robust estimators 可能绕过 FWL\n3. Zhang & Spirtes (2024) 或 Zhang et al. (2024) — causal discovery with measurement error\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix、Should-Fix 和 key Question 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R1-N1：你是否同意 Theorem 1 应降级？\n2. R1-N2：Table 1 条件性问题你如何看？\n3. R1-W3 vs 你的 N2：你们对线性 SEM 限制的看法是否一致？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（侧重方法严谨性 + 实验验证）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 评分：3.5 (Borderline Conference)，置信度 4/5\n维度：Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n### Reviewer 1 的 Strengths\n- S1: 系统性的拓扑分类学（首创性贡献）\n- S2: FWL invariance 负结果干净且重要\n- S3: 三级证据层次结构透明\n- S4: 实证验证有说服力（23 LLM configs × 7 topologies × 3 datasets）\n- S5: ASV 框架具有实践价值\n\n### Reviewer 1 的 Must-Fix 问题\n\n**N1 [CRITICAL] Theorem 1 对 K≥3 缺乏解析证明，不应标为 \"Theorem\"**\n- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减\n- 关键步骤 V_B(δ) 对 δ 单调不增：K=2 有解析证明，K≥3 仅有数值验证（10,000 矩阵零违反）\n- R1 认为标为 \"Theorem\" 意味着有完整证明，数值验证不够\n- 建议：降级为 Proposition/Conjecture，或完成 K≥3 的解析证明\n\n**N2 [CRITICAL] Table 1 的 sign-flip guarantee checkmarks 掩盖了 DGP 条件性**\n- Table 1 对 confounding, mediation, front-door 标注 ✓，但这些保证都有 DGP 条件（如 confounding 需要 sign(τ) = sign(τ + B_OV)）\n- Practitioners 可能直接查表做决策，✓ 暗示无条件保证\n- 建议：用不同符号区分有条件/无条件保证，或在 caption 中明确标注\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1 [MAJOR] Conjecture 1 的 \"ε-approximately monotonic\" 可能误导**\n- Table 7 显示 60-98% 的矩阵存在非单调步骤\n- 在 τ=0.1（mediation ε=0.130）和 τ=5.0（front-door ε=0.139）时 ε 明显超过 0.06\n- ε/η 误差对 δ* 的影响在 ASV 0-2 范围内并非 negligible\n- 建议：明确 ASV 推荐适用范围，独立段落讨论 ε 对 δ* 精度的影响\n\n**W2 [MAJOR] Non-differential misclassification 假设需要更充分讨论**\n- LLM 标注实践中 prompt 包含 context（可能间接包含 Y 信息）；RAG 可能检索到包含 Y 的文档\n- Appendix B.8 的 stress test 覆盖 4 topologies 但仅测试 ε ≤ 0.10 的温和违反\n- 建议：在 Section 3.1 更充分讨论何时成立/不成立，提供诊断方法\n\n**W3 [MAJOR] 线性 SEM 假设对 FWL invariance 的影响讨论不足**\n- FWL invariance 根本性依赖线性 SEM，在 logistic/probit 中 FWL 不成立\n- Algorithm 1 的 caveat 仅在 caption 中，正文未讨论\n- Appendix B.9 的 logistic DGP 检查未测试 FWL invariance 是否在 logistic 下打破\n- 建议：在 Section 4.5 讨论非线性情形，在 logistic DGP 中验证 correction\n\n### Reviewer 1 的 Minor 问题\n- W4: \"Primary coefficient never reverses\" 缺乏理论保证\n- W5: Theory-MC MAPE 2.0% 可能掩盖尾部偏差\n\n### Reviewer 1 的 Questions\n- Q1: Theorem 1 K≥3 证明能否通过 symbolic differentiation 完成？\n- Q2: Sign preservation 的 DGP 条件在实践中如何验证？\n- Q3: Same-sign β_k 是否给出 exposure sign preservation guarantee？\n- Q4: PPI++ gold label 比例和 sensitivity 分析？\n- Q5: FWL invariance 在非线性模型下是否 breakdown？\n- Q6: 83.4% 在 informative prior 下会如何变化？\n\n### Reviewer 1 的 Missing References\n1. Frölich (2007) 或 Mahajan (2006) — IV with mismeasured instruments\n2. Kang & Schafer (2007) — doubly robust estimators 可能绕过 FWL\n3. Zhang & Spirtes (2024) 或 Zhang et al. (2024) — causal discovery with measurement error\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix、Should-Fix 和 key Question 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R1-N1：你是否同意 Theorem 1 应降级？\n2. R1-N2：Table 1 条件性问题你如何看？\n3. R1-W3 vs 你的 N2：你们对线性 SEM 限制的看法是否一致？"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-22T17:03:23.939208+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23166
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-22T17:03:53.023441+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness/Question，使用 [AGREE] 或 [REBUT] 标记，并提供具体理由（引用论文的 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Overall: 3.5 (Borderline Conference)\n\n### Strengths\nS1. 系统性的拓扑分类学（首创性贡献）\nS2. FWL invariance 负结果干净且重要\nS3. 三级证据层次结构透明\nS4. 实证验证有说服力\nS5. ASV 框架具有实践价值\n\n### Must-Fix 问题\n\n**N1 [critical] Theorem 1 对 K ≥ 3 缺乏解析证明，不应标为 \"Theorem\"**\n- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减，但对 general K 仅通过数值验证（10,000 个随机矩阵零违反）。关键步骤 V_B(δ) 单调不增对 K=2 有直接求导证明，K≥3 无解析证明。\n- 建议：降级为 Proposition/Conjecture 或完成 general K 证明。\n\n**N2 [critical] Table 1 的 sign-flip guarantee checkmarks 掩盖了 DGP 条件性**\n- Table 1 对 confounding, mediation, front-door 标注 ✓，但这些保证有 DGP 条件（如 confounding 需 sign(τ) = sign(τ + B_OV)）。✓ 暗示无条件保证，可能误导 practitioners。\n- 建议：用不同符号区分有条件/无条件保证，或在 caption 中明确。\n\n### Should-Fix 问题\n\n**W1 [major] Conjecture 1 的 ε 在极端 τ 下超标（0.13-0.14），ε/η 误差可达 1.3 δ-units，并非 negligible**\n\n**W2 [major] Non-differential misclassification 假设讨论不足——现代 LLM 标注实践中 prompt 可能间接包含 Y 信息**\n\n**W3 [major] FWL invariance 根本性依赖线性 SEM，非线性模型下可能 breakdown，但正文未讨论**\n\n**W4 [minor] \"Primary coefficient never reverses\" 是经验发现，缺乏理论保证**\n\n**W5 [minor] MAPE 2.0% 可能掩盖尾部偏差，未报告 max absolute error**\n\n### Questions\nQ1. Theorem 1 对 K≥3 能否通过 symbolic differentiation 完成？\nQ2. Sign preservation 的 DGP 条件在实践中如何验证？\nQ3. Same-sign β_k 是否保证 exposure sign preservation？\nQ4. PPI++ gold label fraction 和 sensitivity？\nQ5. FWL invariance 在非线性模型下是否 breakdown？\nQ6. Informative prior 下 sign reversal rate 如何变化？\n\n### Missing References\n1. Frölich (2007) / Mahajan (2006) — IV with mismeasured instruments\n2. Kang & Schafer (2007) — doubly robust estimators\n3. Zhang & Spirtes (2024) — causal discovery with measurement error\n\n---\n\n请对以上每个 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness/Question，使用 [AGREE] 或 [REBUT] 标记，并提供具体理由（引用论文的 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Overall: 3.5 (Borderline Conference)\n\n### Strengths\nS1. 系统性的拓扑分类学（首创性贡献）\nS2. FWL invariance 负结果干净且重要\nS3. 三级证据层次结构透明\nS4. 实证验证有说服力\nS5. ASV 框架具有实践价值\n\n### Must-Fix 问题\n\n**N1 [critical] Theorem 1 对 K ≥ 3 缺乏解析证明，不应标为 \"Theorem\"**\n- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减，但对 general K 仅通过数值验证（10,000 个随机矩阵零违反）。关键步骤 V_B(δ) 单调不增对 K=2 有直接求导证明，K≥3 无解析证明。\n- 建议：降级为 Proposition/Conjecture 或完成 general K 证明。\n\n**N2 [critical] Table 1 的 sign-flip guarantee checkmarks 掩盖了 DGP 条件性**\n- Table 1 对 confounding, mediation, front-door 标注 ✓，但这些保证有 DGP 条件（如 confounding 需 sign(τ) = sign(τ + B_OV)）。✓ 暗示无条件保证，可能误导 practitioners。\n- 建议：用不同符号区分有条件/无条件保证，或在 caption 中明确。\n\n### Should-Fix 问题\n\n**W1 [major] Conjecture 1 的 ε 在极端 τ 下超标（0.13-0.14），ε/η 误差可达 1.3 δ-units，并非 negligible**\n\n**W2 [major] Non-differential misclassification 假设讨论不足——现代 LLM 标注实践中 prompt 可能间接包含 Y 信息**\n\n**W3 [major] FWL invariance 根本性依赖线性 SEM，非线性模型下可能 breakdown，但正文未讨论**\n\n**W4 [minor] \"Primary coefficient never reverses\" 是经验发现，缺乏理论保证**\n\n**W5 [minor] MAPE 2.0% 可能掩盖尾部偏差，未报告 max absolute error**\n\n### Questions\nQ1. Theorem 1 对 K≥3 能否通过 symbolic differentiation 完成？\nQ2. Sign preservation 的 DGP 条件在实践中如何验证？\nQ3. Same-sign β_k 是否保证 exposure sign preservation？\nQ4. PPI++ gold label fraction 和 sensitivity？\nQ5. FWL invariance 在非线性模型下是否 breakdown？\nQ6. Informative prior 下 sign reversal rate 如何变化？\n\n### Missing References\n1. Frölich (2007) / Mahajan (2006) — IV with mismeasured instruments\n2. Kang & Schafer (2007) — doubly robust estimators\n3. Zhang & Spirtes (2024) — causal discovery with measurement error\n\n---\n\n请对以上每个 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-22T17:04:09.643335+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16619
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-22T17:04:10.051410+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness/Question，使用 [AGREE] 或 [REBUT] 标记，并提供具体理由（引用论文的 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Overall: 3.5 (Borderline Conference)\n\n### Strengths\nS1. 系统性的跨拓扑分析填补明确研究空白（\"首次跨 7 种拓扑系统比较\"经核查成立）\nS2. 理论结果层次化处理体现学术诚实\nS3. FWL 不变性负面结果具有重要实用价值\nS4. 经验验证覆盖面广且设计合理\nS5. ASV 框架是 E-value 的有意义扩展\nS6. 论文整体结构清晰，逻辑流畅\n\n### Weaknesses\n\n**N1 [MAJOR] 非差异性误分类假设在 LLM 场景下适用性存疑**\n- LLM 处理的文本本身同时包含 treatment 和 outcome 信号（如标注情感时文本中有购买行为描述）。Few-shot demonstrations 编码 treatment-outcome 关联。更根本的是\"文本作为共同原因\"导致结构性差异性。Appendix B.5 的 stress test 仅测试人为添加的 ε 参数，未测试 LLM 诱导的真实差异性模式。\n- 建议：讨论\"文本作为共同原因\"机制，提供定性分析。\n\n**N2 [MAJOR] 线性 SEM 的限制性未被充分验证**\n- 所有 bias 表达式基于线性 SEM。logistic DGP 检查仅验证 sign-flip 一致性，未验证偏差量级、ASV 排名、FWL 不变性。FWL 是线性投影性质，非线性模型中 matrix-based corrections 可能有效。\n- 建议：明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑的校正效果。\n\n**N3 [MAJOR] Conjecture 1 呈现方式不够审慎**\n- ε 可达 0.14（front-door）/0.15（exposure），ε/η = 1.4 δ-units 并非 negligible。论文措辞\"negligible\"轻描淡写。\n- 建议：显式标注 ε 范围和条件；用独立段落讨论 ε 对 δ* 精度影响。\n\n**W1 [MINOR] \"Primary coefficient never reverses\" 缺乏理论保证**\n\n**W2 [MINOR] 数字密度较高影响可读性**\n\n**W3 [MINOR] 符号使用存在轻微不一致（τ 在不同拓扑下含义不同）**\n\n**W4 [MINOR] ClinicalBERT 案例研究（Appendix B.3）过于简略**\n\n### Questions\nQ1. \"文本作为共同原因\"导致的差异性误分类如何影响符号保持结论？\nQ2. DGP 参数（τ=2.0）是否代表 CSS 典型效应量？小效应下条件是否更易违反？\nQ3. 候选拓扑含 exposure 和 confounding 时如何定义\"most conservative\" ASV？\nQ4. FWL 不变性在非线性模型下是否成立？\nQ5. Dirichlet(1,1,1) 的 83.4% sign reversal 在现实先验下是否大幅降低？2.1%（diagonal≥0.7）是否更具参考价值？\n\n### Missing References\nM1. Lash, Fox, Fink (2009/2021) — quantitative bias analysis 教科书\nM2. Kuroki & Pearl (2014) — measurement bias and effect restoration\nM3. Mohan, Pearl, Tian (2013) — missing data as causal problem\n\n### 格式合规检查：全部通过（正文≤8页、ACL模板、匿名、Limitations、图表质量）\n\n---\n\n请对以上每个 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness/Question，使用 [AGREE] 或 [REBUT] 标记，并提供具体理由（引用论文的 Section/Table/Figure 作为证据）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Overall: 3.5 (Borderline Conference)\n\n### Strengths\nS1. 系统性的跨拓扑分析填补明确研究空白（\"首次跨 7 种拓扑系统比较\"经核查成立）\nS2. 理论结果层次化处理体现学术诚实\nS3. FWL 不变性负面结果具有重要实用价值\nS4. 经验验证覆盖面广且设计合理\nS5. ASV 框架是 E-value 的有意义扩展\nS6. 论文整体结构清晰，逻辑流畅\n\n### Weaknesses\n\n**N1 [MAJOR] 非差异性误分类假设在 LLM 场景下适用性存疑**\n- LLM 处理的文本本身同时包含 treatment 和 outcome 信号（如标注情感时文本中有购买行为描述）。Few-shot demonstrations 编码 treatment-outcome 关联。更根本的是\"文本作为共同原因\"导致结构性差异性。Appendix B.5 的 stress test 仅测试人为添加的 ε 参数，未测试 LLM 诱导的真实差异性模式。\n- 建议：讨论\"文本作为共同原因\"机制，提供定性分析。\n\n**N2 [MAJOR] 线性 SEM 的限制性未被充分验证**\n- 所有 bias 表达式基于线性 SEM。logistic DGP 检查仅验证 sign-flip 一致性，未验证偏差量级、ASV 排名、FWL 不变性。FWL 是线性投影性质，非线性模型中 matrix-based corrections 可能有效。\n- 建议：明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑的校正效果。\n\n**N3 [MAJOR] Conjecture 1 呈现方式不够审慎**\n- ε 可达 0.14（front-door）/0.15（exposure），ε/η = 1.4 δ-units 并非 negligible。论文措辞\"negligible\"轻描淡写。\n- 建议：显式标注 ε 范围和条件；用独立段落讨论 ε 对 δ* 精度影响。\n\n**W1 [MINOR] \"Primary coefficient never reverses\" 缺乏理论保证**\n\n**W2 [MINOR] 数字密度较高影响可读性**\n\n**W3 [MINOR] 符号使用存在轻微不一致（τ 在不同拓扑下含义不同）**\n\n**W4 [MINOR] ClinicalBERT 案例研究（Appendix B.3）过于简略**\n\n### Questions\nQ1. \"文本作为共同原因\"导致的差异性误分类如何影响符号保持结论？\nQ2. DGP 参数（τ=2.0）是否代表 CSS 典型效应量？小效应下条件是否更易违反？\nQ3. 候选拓扑含 exposure 和 confounding 时如何定义\"most conservative\" ASV？\nQ4. FWL 不变性在非线性模型下是否成立？\nQ5. Dirichlet(1,1,1) 的 83.4% sign reversal 在现实先验下是否大幅降低？2.1%（diagonal≥0.7）是否更具参考价值？\n\n### Missing References\nM1. Lash, Fox, Fink (2009/2021) — quantitative bias analysis 教科书\nM2. Kuroki & Pearl (2014) — measurement bias and effect restoration\nM3. Mohan, Pearl, Tian (2013) — missing data as causal problem\n\n### 格式合规检查：全部通过（正文≤8页、ACL模板、匿名、Limitations、图表质量）\n\n---\n\n请对以上每个 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T17:04:12.616543+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2565
}
```

</details>

---


### Assistant

_source line 392 · 2026-05-22T17:04:16.720351+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 39

## Round 39

2 recorded events


### User

_source line 393 · 2026-05-22T17:04:19.552308+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5 (Borderline Conference)，Soundness 4/5，Excitement 3/5，Confidence 4/5。

**核心判断**：跨 7 种拓扑的系统比较是明确的新贡献，理论执行扎实（证明/验证/猜想分层诚实），经验验证覆盖面广。三个主要问题拉低评分：(1) 非差异性误分类假设在 LLM 处理文本的场景下适用性受限，(2) 线性 SEM 限制了 FWL 不变性等结论的通用性，(3) Conjecture 1 的 ε 在极端条件下可达 0.14-0.15，对 ASV 精度的影响被轻描淡写。提出了 5 个 Questions 和 3 个 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 394 · 2026-05-22T17:04:37.608240+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 395 · 2026-05-22T17:05:55.578222+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE with nuance] R1-N1: Theorem 1 对 K≥3 缺乏解析证明**

R1 的核心观察是正确的：Theorem 1 的关键步骤——$V_B(\delta)$ 对 $\delta$ 单调不增——在 $K=2$ 有解析证明（直接微分），但对 $K \geq 3$ 仅有数值验证（10,000 矩阵零违反，Appendix A.4 line 241-243）。Proof sketch (Section 3.3) 中的措辞"non-positivity is verified algebraically and numerically"有些含糊——Appendix 实际呈现的是纯数值验证，"algebraically"一词可能误导读者以为存在代数证明。

但我不完全同意降级为 Conjecture 的建议。原因：
1. Theorem 1 的条件已经相当强（proportional effects $f = \lambda g$），这使得 $V_B(\delta)$ 的结构高度受限——它是有理函数，其单调性在 10,000 个随机 $C_0$ 下零违反，这比 Conjecture 1 中 60-98% 矩阵存在非单调步骤的情况有质的区别。
2. 更合理的修改是：(a) 在 proof sketch 中明确承认 $K \geq 3$ 依赖数值验证，删除"algebraically"措辞；(b) 将 Theorem 1 的声明范围缩小为"$K=2$ proved; $K \geq 3$ verified numerically with zero violations"，或改为 Theorem + Remark 的组合。

完全降级为 Conjecture 会模糊 Theorem 1 与 Conjecture 1 之间的本质差异——前者有 zero violations 和结构性约束（proportional effects），后者有 bounded 但 nonzero violations。

**[AGREE] R1-N2: Table 1 的 checkmarks 掩盖了 DGP 条件性**

这是一个重要的实用性问题，我完全同意。核查 Table 1 (Section 4.2, p.7)：
- Confounding ✓：需要 $\operatorname{sign}(\tau) = \operatorname{sign}(\tau + B_{\mathrm{OV}})$（Proposition 1(a)）
- Mediation ✓：需要 $\operatorname{sign}(\tau_{\mathrm{dir}}) = \operatorname{sign}(\tau_{\mathrm{total}})$（Numerical Verification 1）
- Front-door ✓：需要 $\operatorname{sign}(\lambda\alpha_U) = \operatorname{sign}(\lambda\alpha_U + \operatorname{Cov}(T,f(A)))$（同上）
- Collider ✓：需要 $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T|A)]$（Proposition 1(b)）
- M-bias ✓：无条件（唯一真正无条件的）

Table 1 caption 仅说"structural sign-flip guarantee holds (✓) or not (✗)"，未提及条件。实践者确实会直接查表做决策——如果一个 confounding 研究的 treatment effect 很弱（$|\tau|$ 接近 $|B_{\mathrm{OV}}|$），sign preservation 可能不成立，但 Table 1 给出的信号是"安全的"。

R1 的建议合理：用不同符号（如 ✓ vs ✓*）区分无条件保证（M-bias）和有条件保证（其余四个），并在 caption 中列出条件引用。

---

### Should-Fix 问题

**[AGREE] R1-W1: Conjecture 1 的 ε 值在极端条件下可能误导**

R1 对 Conjecture 1 的担忧与我的 N3 高度一致。补充几个具体数据点：
- Front-door $\tau=5.0$ 时 $\varepsilon \approx 0.14$，对应 $\delta^*$ 误差 $\varepsilon/\eta = 0.14/0.10 = 1.4$ 个 $\delta$ 单位——在 ASV 典型范围 0-2 内，这是实质性的误差
- R1 指出 Table 7 显示 60-98% 的矩阵存在非单调步骤——这一数据我在审稿时未充分注意。"ε-approximately monotonic"的措辞与如此高比例的非单调步骤形成了修辞上的紧张关系
- 论文在 p.5 底部用一句话处理此问题（"negligible at the recommended η = 10%"）确实不够

同意 R1 建议：ASV 结果应附带明确的适用范围说明，ε 对 δ* 精度的影响应用独立段落讨论。

**[AGREE] R1-W2: Non-differential misclassification 假设需更充分讨论**

与我的 N1 一致。R1 补充了我未明确提到的两个重要场景：(1) RAG 系统可能检索到包含 Y 的文档；(2) few-shot demonstrations 中隐含的 treatment-outcome 关联。Appendix B.5 的 stress test 确实仅测试了温和违反（$\varepsilon \leq 0.10$），未覆盖 LLM 特有的差异性来源。

R1 关于"提供诊断方法"的建议尤其好——可以建议实践者检查 $P(A^*|A, Y)$ 与 $P(A^*|A)$ 的差异，例如通过在有 gold labels 的子集上测试条件独立性。

**[AGREE] R1-W3: 线性 SEM 假设对 FWL invariance 的影响讨论不足**

与我的 N2 完全一致，R1 的论证更具体：
1. FWL 定理是线性投影的性质，在 logistic/probit 回归中不成立——这意味着 Section 4.5 的核心结论"matrix-based corrections achieve exactly 0% bias reduction for four topologies"严格来说仅在 OLS 下成立
2. Algorithm 1 的 caveat "FWL-based routing may not apply under nonlinear models" 仅在 caption 中，正文 Section 4.5 无任何限定
3. Appendix B.6 的 logistic DGP 检查验证了 sign-flip 模式但**未**验证 correction 效果

R1 的 Q5 进一步追问"FWL invariance 在非线性模型下是否 breakdown"——答案几乎确定是 yes（logistic regression 的 partial 控制不等价于 FWL 投影），但论文回避了这一点。这是一个实质性问题：如果许多 CSS 研究使用 logistic regression，那么"matrix-based corrections are provably ineffective"的结论可能不适用，这削弱了 FWL 负面结果的实践价值。

---

### Minor 问题

**[AGREE] R1-W4: "Primary coefficient never reverses" 缺乏理论保证**

与我的 W1 完全一致。23 个配置的经验观察不构成保证。

**[REBUT partially] R1-W5: Theory-MC MAPE 2.0% 可能掩盖尾部偏差**

R1 担忧 grand MAPE 2.0% 掩盖尾部。论文实际报告了 per-topology 范围（Section 4.2）："Per-topology MAPE ranges from 0.5% (confounding) to 5.5% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification." IV 的 5.5% 已经不低，但论文给出了解释（小分母方差放大）。此外 N=10,000 的 MC 模拟本身有抽样方差，5.5% 的 MAPE 在 IV 拓扑下是合理的。

我认为 2.0% 的 grand MAPE 没有实质性地掩盖问题——论文已提供了分拓扑的分解。如果 R1 希望看到 95th percentile MAPE，这是合理的补充要求，但不影响核心结论。

---

### Key Questions 回应

**[AGREE worth answering] R1-Q1: Theorem 1 K≥3 证明能否通过 symbolic differentiation 完成？**

有意义的问题。$V_B(\delta)$ 是 $\delta$ 的有理函数（分子分母都是 $\delta$ 的多项式），对 general $K$ 进行 symbolic differentiation 是可行的思路。但 $V_B(\delta) = \sum_j q_j(\delta) \cdot [\mathbb{E}[g|A^*_\delta=j]]^2 - [\sum_j q_j(\delta) \cdot \mathbb{E}[g|A^*_\delta=j]]^2$，每项都是 $\delta$ 的有理函数之积/和，展开后的导数表达式对 general $K$ 可能非常复杂。值得尝试但不确定能得到简洁结果。

**[AGREE important] R1-Q2: Sign preservation 的 DGP 条件在实践中如何验证？**

这是 Table 1 条件性问题的自然延伸。例如 confounding 条件 $\operatorname{sign}(\tau) = \operatorname{sign}(\tau + B_{\mathrm{OV}})$ 需要知道 $B_{\mathrm{OV}}$，这依赖于 true DGP parameters——正是因为不知道这些参数才需要做因果推断。论文在 Section 3.2 末尾承认了这一点（"These conditions involve true DGP parameters, which in practice must be estimated. The ASV framework (§3.3) provides a complementary assessment..."），但 ASV 本身也需要 reference confusion matrix $C_0$。这形成了一个循环依赖，值得在论文中更明确讨论。

**[AGREE] R1-Q3: Same-sign β_k 是否给出 exposure sign preservation guarantee？**

从 Equation 2 的结构看，如果所有 $\beta_k$ 同号，那么 $\hat{\beta}_j = \sum_k w_{jk} \beta_k$ 中即使 $w_{jk}$ 为负也不会改变符号（因为没有 opposite-sign 系数可供"借"来反转）。论文在 Section 4.4 提到"Sign reversal requires opposite-sign treatment effects across categories; same-sign βk produce only attenuation"，但这仅作为经验观察而非定理。值得形式化。

**[AGREE] R1-Q6: 83.4% 在 informative prior 下会如何变化？**

与我的 Q5 一致。论文已在 realistic subspace (diagonal ≥ 0.7) 下报告 2.1%，这是更有参考价值的数字。但 Introduction 的 framing 以 83.4% 开头，可能给读者造成过度夸大的印象。

---

### R1 Missing References 回应

**[AGREE] Frölich (2007) 或 Mahajan (2006) — IV with mismeasured instruments**

直接相关。论文的 IV 拓扑分析了 instrument 被误分类的情况，这两篇是该特定问题的经典参考。当前 IV 部分仅引用了 Angrist & Imbens (1995) 的 Wald estimator。

**[REBUT partially] Kang & Schafer (2007) — doubly robust estimators 绕过 FWL**

Doubly robust estimators 确实不受 FWL 约束，但 FWL invariance 结果的关键在于它揭示了**线性回归框架下**矩阵类校正的无效性。Doubly robust 方法需要正确指定 propensity score 或 outcome model，这在 A 被误分类时本身就有问题。可以在讨论中提及但不是核心遗漏。

**[AGREE partially] Zhang & Spirtes (2024) — causal discovery with measurement error**

相关性取决于具体内容。如果该工作从图模型角度处理 measurement error 下的因果发现，与本文的 DAG taxonomy 有交叉。但本文假设 DAG 已知，不做 discovery，因此相关性有限。可以在 Related Work 中简短提及但非必须。

---

### 总结：R2 与 R1 的共识和分歧

**高度共识：**
- 线性 SEM 限制性问题（R1-W3 ≈ R2-N2）
- Non-differential 假设的讨论不足（R1-W2 ≈ R2-N1）
- Primary coefficient 声称缺乏保证（R1-W4 = R2-W1）
- Conjecture 1 的 ε 处理过于轻描淡写（R1-W1 ≈ R2-N3）
- 83.4% vs 2.1% 的 framing 问题（R1-Q6 ≈ R2-Q5）

**主要分歧：**
- R1-N1（Theorem 1 降级）：我认为应修改措辞而非完全降级——Theorem 1 的 zero violations + proportional effects 约束与 Conjecture 1 有质的区别
- 评分：我给 Soundness 4/5（R1 给 3.5/5），差异主要来自我对数值验证作为证据的接受度更高

**评分维持**：Overall 3.5 (Borderline Conference)，与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-22T17:06:15.880285+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 397 · 2026-05-22T17:06:18.614776+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

核心立场：与 R1 在五个关键问题上高度共识（线性 SEM 限制、non-differential 假设、primary coefficient 声称、Conjecture 1 的 ε 处理、83.4% framing），唯一实质分歧在 Theorem 1 是否应降级——我认为修改措辞比完全降级更合理，因为 zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别。

Overall 评分维持 3.5 (Borderline Conference)，与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 398 · 2026-05-22T17:06:33.961004+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 399 · 2026-05-22T17:06:35.487588+00:00_

[Reviewer 2 审稿结果]:
审稿意见已在上一轮交叉回应中完整提交。所有 N/W/Q 均已逐条回应并发送给 Director。无需重复提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 400 · 2026-05-22T17:06:51.139433+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 43

## Round 43

10 recorded events


### User

_source line 401 · 2026-05-22T17:07:03.423837+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

### Weaknesses 逐条回应

**[AGREE] R2-N1: 非差异性误分类假设在 LLM 场景下适用性存疑**

同意这是一个重要问题，且 R2 的 "文本作为共同原因" 框架比我自己的 W2 表述更精确。核心论点：LLM 从同一段文本中同时提取 treatment signal 和（间接的）outcome signal，这在结构上违反 Definition 1 的 P(A*|A,Y,Z) = P(A*|A)，不是简单的 "mild violation" 而是架构性的。

论文在 Section 3.1 第 14 行提到 "natural when the LLM annotates treatment labels from source documents without access to outcome information"，但现代标注场景中文本本身就携带 outcome 信息（如标注政治立场时，文本同时包含投票行为的线索）。Appendix B.8 的 stress test 通过人为添加 ε-perturbation 模拟差异性，但这与 LLM 从文本中提取 outcome-correlated features 的真实模式在结构上不同。

不过我要补充一点 nuance：violation severity 是 topology-dependent 的。Table 4 (Appendix B.8) 显示即使在 ε=0.10 下，exposure sign-flip 仅从 2.0% 升至 4.5%，增幅有限。这说明对大多数 topology，moderate differential misclassification 不会剧烈改变定性结论，虽然 R2 的理论担忧是对的。

**建议给作者的修改优先级：SHOULD-FIX。** 在 Section 3.1 加入 "text as common cause" 讨论，但不必重做全部理论（differential misclassification 的完整理论是另一篇论文的工作量）。

---

**[AGREE] R2-N2: 线性 SEM 的限制性未被充分验证**

与我的 W3 完全一致。关键缺口：Appendix B.9 的 logistic DGP 检查仅验证 sign-flip pattern（SF_τ 和 SF_any），但完全没有验证两个核心 claim 在非线性下是否成立：

1. **FWL invariance 是否打破？** 论文声称 Naive plug-in 对 4 种 covariate topology 产生 0% bias reduction（Section 4.5, Table 3）。这严格依赖线性投影的 column space 性质（Appendix B.2）。在 logistic regression 中 FWL 不成立——如果 matrix-based correction 在 logistic 下确实能降低 bias，这将显著改变 correction guidance。

2. **ASV ranking 是否保持？** 论文未在 logistic DGP 下计算 ASV，topology vulnerability ranking 可能改变。

R2 建议 "明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑的校正效果"，我认为这是 reasonable 且 feasible 的要求。

**建议给作者的修改优先级：SHOULD-FIX。** 至少加一个 logistic correction experiment（如 confounding + Naive plug-in）验证 FWL 是否打破。

---

**[AGREE with nuance] R2-N3: Conjecture 1 呈现方式不够审慎**

核心关切与我的 W1 一致：ε/η 误差在极端情况下可达 1.3-1.4 δ-units，而典型 ASV 范围在 0-2，因此 "negligible" 一词（Section 3.3 第 99 行）确实不准确。

但我要 **部分 rebut R2 的严重性判断**：

1. **Conjecture 自身已有充分限定。** Conjecture 1 正文明确标注了 τ 范围和 ε 上界：front-door "ε < 0.06 for τ ≤ 2.0; at extreme τ, normalization artifacts can increase ε to ≈0.14"；exposure "ε < 0.008 at the 99th percentile, though extreme-tail matrices (<0.02% of Dirichlet draws) can reach ε ≈ 0.15"。这些不是隐藏在 appendix 中的 fine print——它们就在 Conjecture 声明中。

2. **极端 ε 出现在极端参数下。** Table 8 (Appendix B.12) 显示 ε > 0.06 主要发生在 τ=0.1（mediation 0.130, confounding 0.118）和 τ=5.0（front-door 0.139）。在推荐操作范围 τ ∈ [0.5, 2.0] 内，非 IV 拓扑的 ε 均 < 0.06。

3. **ε/η 的实际影响。** ε=0.06, η=0.10 时 δ* 误差 ≤ 0.6 units。在 Table 2 的 ASV 范围内（如 confounding 0.081-0.487），0.6 units 确实不 negligible——但对于 practitioner 的 binary decision（safe vs. unsafe），ASV 排名在所有测试配置中保持不变（Conjecture 1 最后一句）。

**修改建议：** 将 "negligible" 改为 "bounded"，并加入一段明确讨论 ε 对 δ* 精度的定量影响。但我不认为这构成 CRITICAL 问题——Conjecture 的框架本身已足够透明。

---

**[AGREE] R2-W1: "Primary coefficient never reverses" 缺乏理论保证**

与我的 W4 完全一致。论文在 Abstract 和 Section 4.4 中作为 headline finding 呈现 "the primary treatment effect never reverses in any of 23 empirical LLM configurations"，但这只是 23 个经验观察，不是定理。从 Eq.(2) 看，当 primary category 有 largest prevalence 且 diagonal dominance 充分时，sign reversal 确实更难发生——但论文没有 formalize 这个直觉。

R2 将此标为 MINOR 合理——这是一个 framing/presentation 问题，不是方法论缺陷。

---

**[AGREE] R2-W2: 数字密度较高影响可读性**

论文在 8 页内呈现 7 topologies × multiple metrics，数字密度确实高。但考虑到 8-page constraint 和内容的必要性，这更多是 venue limitation 而非论文缺陷。建议作者在 camera-ready 时考虑将部分数字移入 appendix，main text 只保留 key numbers。

---

**[AGREE] R2-W3: 符号使用存在轻微不一致（τ 在不同拓扑下含义不同）**

τ 在 confounding 下是 X→Y 的因果效应，在 mediation 下是直接效应 τ_dir，在 exposure 下是 category-specific β_j，在 IV 下是 LATE。论文 Appendix C 有 notation table（Table 9），但 main text 中 τ 的含义随 topology 切换时没有明确提示。这不影响理解但增加认知负荷。

---

**[AGREE mildly] R2-W4: ClinicalBERT 案例研究过于简略**

Appendix B.7 的案例研究用约半页篇幅做了 retrospective analysis，给出三个具体结论（sign-flip guarantee、FWL warning、correction recommendation）。作为 appendix 的定性说明，深度可以接受。但如果能加上对 ClinicalBERT confusion matrix 的定量 ASV 计算（如 "magnitude ASV for this specific C₀ is δ*=X, indicating the study is robust/fragile"），说服力会显著提升。

---

### Questions 逐条回应

**[AGREE] R2-Q1: "文本作为共同原因" 导致的差异性误分类如何影响符号保持结论？**
有价值的问题。如 N1 中讨论，论文应至少提供定性分析。

**[AGREE] R2-Q2: DGP 参数（τ=2.0）是否代表 CSS 典型效应量？**
重要问题。CSS 中标准化效应量通常在 [0.05, 0.5] 范围，τ=2.0（Appendix A.3 confounding DGP）偏大。Table 8 (Appendix B.12) 显示 τ=0.1 时 confounding 的 ε 升至 0.118——说明在小效应场景下，sign preservation 条件更容易违反（因为 |B_OV| 更可能 overwhelm small |τ|）。论文应明确讨论 DGP 参数选择的 representativeness，并标注 small-τ regime 的额外风险。

**[AGREE] R2-Q3: 候选拓扑含 exposure 和 confounding 时如何定义 "most conservative" ASV？**
有价值。论文 Limitations 说 "compute ASV under candidate DAGs and report the most conservative"，但没有给出操作性定义。当一种 topology 说 safe（如 confounding: sign preserved）而另一种说 dangerous（如 exposure: 83.4% sign reversal）时，"最保守" 意味着采用最悲观的判断，即 exposure 的结论。但这在方法论上等价于 "DAG 不确定则假设最差情况"，可能过于保守。建议论文至少给出一个 decision tree（类似 Algorithm 1 但加入 topology uncertainty 分支）。

**[AGREE] R2-Q4: FWL 不变性在非线性模型下是否成立？**
与 N2 重复。核心观点一致：需要实验验证。

**[REBUT partially] R2-Q5: Dirichlet(1,1,1) 的 83.4% vs. 2.1%（diagonal≥0.7）的呈现**
R2 暗示 83.4% 可能误导。但论文 **已经充分呈现了两个数字**：
- Abstract 第 2 行："Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 2.1%"
- Introduction Section 1 第 6 行："83.4% of K=3 exposure confusion matrices produce sign reversal... under realistic accuracy (diagonal ≥ 0.7), 2.1% do so"
- Section 4.2 第 20 行详细分层报告

两个数字并列呈现，83.4% 用于建立 structural possibility（K≥3 vs K=2），2.1% 用于 practical relevance。我认为 framing 已经足够平衡。不过 R2 提出 "informative prior matching empirical LLM distributions" 的建议是 constructive 的——如果用拟合真实 LLM confusion matrices 的 Dirichlet(α) 做 sensitivity analysis，会更有说服力。

---

### Missing References 回应

**[AGREE] R2-M1: Lash, Fox, Fink (2009/2021)** — quantitative bias analysis 是标注误差校正的标准参考书，论文已引用 Carroll et al. (2006) 和 Gustafson (2004) 但缺少这一本。应在 Related Work 的 measurement error 段落中补充。

**[AGREE] R2-M2: Kuroki & Pearl (2014)** — measurement bias and effect restoration 与论文的 correction guidance（Section 4.5）直接相关。特别是 Kuroki & Pearl 讨论了何时可以从含测量误差的 DAG 中 restore causal effects，这与 FWL invariance 负结果形成对照。

**[AGREE mildly] R2-M3: Mohan, Pearl, Tian (2013)** — 将 missing data 作为 causal problem 处理。论文已引用 Blackwell, Honaker, King (2017) 的 unified framework。Mohan et al. 提供了更基础的 graphical theory，但不是 essential gap——论文不处理 missing data，只处理 misclassification。可以在 Related Work 中以 "related graphical approaches" 简要提及。

---

### 汇总：R1 与 R2 的共识与分歧

**共识点（两位 reviewer 独立提出）：**
1. 线性 SEM / FWL invariance 的非线性 generalization 需要讨论和验证（R1-W3 ↔ R2-N2）
2. Non-differential assumption 在 LLM 场景下需更充分讨论（R1-W2 ↔ R2-N1）
3. Conjecture 1 的 ε 呈现需要更审慎（R1-W1 ↔ R2-N3）
4. "Primary coefficient never reverses" 需要理论支撑或降级表述（R1-W4 ↔ R2-W1）

**R1 独有的关切：**
- **N1 [CRITICAL]: Theorem 1 对 K≥3 的证明不完整** — R2 未提及此问题。我仍认为这是最严重的方法论问题：一个核心 Theorem 依赖数值验证而非解析证明。
- **N2 [CRITICAL]: Table 1 sign-flip guarantee 的条件性呈现不透明** — R2 未单独标记此问题。Table 1 的 ✓ 暗示无条件保证但实际是 DGP-conditional。

**R2 独有的关切：**
- "文本作为共同原因" 的具体机制分析（比我的 W2 更 specific）
- DGP 参数 representativeness（τ=2.0 偏大）
- ClinicalBERT 案例深度不足

**Overall alignment**: 两位 reviewer 评分相同（3.5 Borderline Conference），核心关切高度重叠但侧重略不同。R1 更关注理论证明的严谨性（Theorem 1 proof gap），R2 更关注假设的实际适用性（non-differential assumption, linear SEM）。两组关切互补，共同指向论文需要在理论声明的精确性和实际适用范围的讨论上加强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-22T17:07:33.608903+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-22T17:07:33.964039+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T16:53:52.299817+00:00\", \"completed_at\": \"2026-05-22T16:54:07.801321+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-22T17:07:33.964561+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-22T17:07:34.067560+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T17:10:11.148798+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Carried from Round 1-4, updated in Round 5 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"一般情形降级为 Empirical Finding，保留比例情形证明。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"W1 CRITICAL。DPI 证明路径不成立（C(δ) 不满足 stochastic degradation）。Appendix A.4 有 V_W(δ) 直接路径但未升级。必须补全或降格。\"\n      - round: 5\n        reviewers: [R1]\n        note: \"R1 仍标 CRITICAL：K≥3 仅有数值验证（10,000 矩阵零违反），不应标为 Theorem。R2 AGREE with nuance：建议修改措辞而非完全降级（zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别）。分歧：R1 主张降级为 Conjecture，R2 主张 Theorem + Remark 组合。\"\n    action_items:\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Mediation 证明 + ε bound\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"补全 Theorem 1 直接证明（V_W(δ) 路径，不依赖 DPI）或降格\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"明确 K=2 为 proved、K≥3 为 numerically verified with zero violations；删除 proof sketch 中 'algebraically' 措辞；或完成 K≥3 symbolic differentiation 证明\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。R4 确认此表述准确。R5 未再提及此特定问题。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"'catastrophic' 与 primary coefficient never reverses 矛盾。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"W2 CRITICAL。Abstract 已改善但 Introduction 仍过度突出 83.4%。\"\n      - round: 5\n        reviewers: [R1]\n        note: \"R1 在交叉回应中 partially rebut R2-Q5：认为 Abstract/Intro 已并列呈现 83.4% 和 2.1%，framing 已足够平衡。R2 维持 83.4% 作为 informative prior 下会大幅降低的观点。分歧不大。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 删 83.4%/catastrophic，加 primary never reverses\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Introduction 中 83.4% 从动机降级为参数空间刻画\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。Round 3-5 未再提及。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"Limitations 应提及 open-source only。\"\n      - round: 5\n        reviewers: []\n        note: \"R5 未显式提及，但 Limitations 中仍未见商业 LLM 讨论。可能已修复待确认。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加商业 LLM 限制说明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。Round 3-5 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Algorithm 1 加 caveat；扩展 logistic 至全 7 拓扑\"\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W3 + R2-N2 共同提出。FWL invariance 根本性依赖线性 SEM。Appendix B.9 logistic DGP 仅验证 sign-flip，未验证 FWL breakdown 或 correction 效果。两位 Reviewer 共识：需至少一个 logistic correction experiment。\"\n    action_items:\n      - round: 3\n        action: \"Algorithm 1 加 caveat；扩展 logistic 至全 7 拓扑\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"Section 4.5 明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑（如 confounding）的 Naive plug-in correction 效果\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"统一 τ/β_T；添加 Proposition 交叉引用\"\n      - round: 5\n        reviewers: [R2]\n        note: \"R2-W3：τ 在不同拓扑下含义不同（confounding 是 X→Y 因果效应，exposure 是 category-specific β_j），main text 中切换时无明确提示。\"\n    action_items:\n      - round: 3\n        action: \"统一 τ/β_T；添加 Proposition 交叉引用\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"Section 3.1 添加 τ 在各拓扑下含义的明确说明\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Stress test 已扩展但正文讨论不足。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"W5 MAJOR。已有 outcome-conditional prompting 讨论但缺 few-shot ICL demonstration bias 场景。\"\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W2 + R2-N1 共同提出，均标 MAJOR。R2 引入'文本作为共同原因'框架——LLM 从同一文本同时提取 treatment 和 outcome 信号，这是结构性违反而非 mild violation。R1 补充 RAG 检索和 chain-of-thought 推理渠道。Appendix B.5 stress test 仅测试 ε≤0.10 的人为扰动，未测试 LLM 诱导的真实差异性模式。两位共识：Section 3.1 需加入'text as common cause'讨论 + practitioner diagnostic。\"\n    action_items:\n      - round: 3\n        action: \"正文讨论 non-differential 假设\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Limitations 补充 few-shot ICL demonstration 场景\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"Section 3.1 加入 'text as common cause' 机制讨论；提供 practitioner diagnostic（如在 gold-label 子集上检验 P(A*|A,Y) vs P(A*|A) 的条件独立性）\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"Feder et al. 已引用（Related Work）。Cheng et al. 已引用（Related Work line 164）。R5 未再提及。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。Round 3-5 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 issues ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证（R5 格式检查通过）。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5-R1-S2 确认 FWL 证明'干净且重要'，R2-S3 确认'实用价值'。证明本身不再有问题。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加（'outcome misclassification and correlated multi-annotator settings introduce additional bias channels not captured here'）。R5 未再提及。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"W11 MINOR。\"\n      - round: 5\n        reviewers: [R2]\n        note: \"R2-W2 MINOR：Introduction 第二段 3 行内 6 个百分比数字；Section 4.4 Cross-K 段落数字密集。建议 Introduction 精简至 2-3 个关键数字，Section 4.4 用表格呈现。\"\n    action_items:\n      - round: 5\n        action: \"Introduction 精简数字密度；Section 4.4 Cross-K 比较考虑表格呈现\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。R4-5 未提及。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。R5 Reproducibility 4/5 确认。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5-R2-S1 确认'首次跨 7 种拓扑系统比较经核查成立'。定位问题已解决。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。R4-5 未再提及。\"\n    resolution_round: 4\n\n  # === Round 4 issues ===\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"MAJOR。需 sketch proof 或标注为 assumption。\"\n      - round: 5\n        reviewers: []\n        note: \"R5 未显式提及 λ(C) bound 问题。论文 Eq.(3) 标注'under proportional effects (Appendix A, Proposition 4)'。可能已修复待确认。\"\n    action_items:\n      - round: 4\n        action: \"证明 λ(C) ∈ [0,1] 或标为 assumption\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次：(i) analytically proved (Proposition 1(a,b), Theorem 1), (ii) numerically verified (mediation, M-bias, front-door), (iii) conjectured (Conjecture 1)。R5 R1-S3 和 R2-S2 均确认'三级证据层次结构透明'/'层次化处理体现学术诚实'。'Empirical Finding'术语似已替换为'Numerical Verification'。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"R5-R2-S5 确认'ASV 框架是 E-value 的有意义扩展'，列出三个关键差异（K×K→1D 非平凡、三种 ASV 类型、FWL 结合）。R1-S5 确认'具有实践价值'。ASV 创新性质疑已解决。\"\n    resolution_round: 5\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R2]\n        note: \"R2 Excitement 3/5：'NLP 社区可能对此理论较重的工作兴趣有限'。但 R1 Excitement 3.5/5 更正面。R2-S1 同时确认'填补了明确的研究空白'。分歧在于对 NLP venue 的适配性。\"\n    action_items:\n      - round: 4\n        action: \"通过贡献层级重排（theory-first）自然回应\"\n        assigned_to: director\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加'our framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative'。R5 R2-Q3 提出如何定义'most conservative'的后续问题但不再视为缺失。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"R5 未显式提及。Section 4.5 仍仅报告数字。\"\n    action_items:\n      - round: 4\n        action: \"Section 4.5 添加 PPI++ M-bias 机制解释\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"bib 检查：lee_wood_doughty2024 标注为'AIM-FM Workshop, NeurIPS 2024'（有 note='Workshop paper'）；baumann2025 标注为 arXiv preprint。R5 R1 小问题 #6 提及 Baumann 如有正式版本应更新，降级为建议。\"\n    resolution_round: 5\n\n  - id: R4-MR\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇引用（Round 4 新要求）\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"bib 检查确认：Imai/Keele/Yamamoto(2010) ✓, Buonaccorsi(2010) ✓, Blackwell/Honaker/King(2017) ✓, Valeri/VanderWeele(2013) ✓, Pangakis/Wolken/Fasching(2023) ✓。全部已引用。\"\n    resolution_round: 5\n\n  # === Round 5 新增 issues ===\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性，可能误导 practitioners\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1 标 CRITICAL，R2 AGREE。5/7 拓扑的 ✓ 均有 DGP 条件（仅 M-bias 无条件）。Table 1 caption 未提及条件。Practitioners 可能直接查表做决策获得错误安全感。\"\n    action_items:\n      - round: 5\n        action: \"Table 1 用不同符号区分无条件(M-bias)和有条件保证(其余4个)；caption 明确标注'✓ indicates sign preservation under DGP-specific sufficient conditions (Table 5 in Appendix)'\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15，'negligible' 措辞不当\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W1 MAJOR + R2-N3 MAJOR。ε/η 误差在 ASV 0-2 范围内可达 1.3-1.4 δ-units。Table 7 显示 60-98% 矩阵存在非单调步骤。'ε-approximately monotonic' 与如此高非单调比例的修辞紧张。R1 部分 rebut：extreme ε 仅在 extreme τ 下出现，推荐范围内 ε<0.06。\"\n    action_items:\n      - round: 5\n        action: \"'negligible' → 'bounded'；用独立段落讨论 ε 对 δ* 精度的定量影响；明确 ASV 推荐适用范围（|τ| ≥ 0.5）\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N3\n    category: presentation\n    severity: should-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现（23 configs），缺乏理论保证\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W4 MINOR + R2-W1 MINOR，交叉回应均 AGREE。Abstract 措辞暗示普遍性。Eq.(2) 表明 same-sign β_k 保证 attenuation only——值得 formalize 但论文未做。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 措辞改为 conditional（'In our experiments, the primary...'）；如可能，formalize same-sign β_k → sign preservation 的充分条件\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1: Frölich(2007)/Mahajan(2006) IV mismeasured instruments [AGREE both]; Kang&Schafer(2007) doubly robust [R2 partially rebut]. R2: Lash/Fox/Fink(2009/2021) quantitative bias analysis [R1 AGREE]; Kuroki&Pearl(2014) measurement bias [R1 AGREE]; Mohan/Pearl/Tian(2013) [R1 mildly agree].\"\n    action_items:\n      - round: 5\n        action: \"优先添加：Mahajan(2006) 或 Frölich(2007)（IV）、Lash/Fox/Fink(2009/2021)（QBA）、Kuroki&Pearl(2014)（measurement bias）。可选：Mohan/Pearl/Tian(2013)\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Carried from Round 1-4, updated in Round 5 ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R1 首发，R2 AGREE。\"\n      - round: 2\n        reviewers: [R1, R2]\n        note: \"一般情形降级为 Empirical Finding，保留比例情形证明。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"W1 CRITICAL。DPI 证明路径不成立（C(δ) 不满足 stochastic degradation）。Appendix A.4 有 V_W(δ) 直接路径但未升级。必须补全或降格。\"\n      - round: 5\n        reviewers: [R1]\n        note: \"R1 仍标 CRITICAL：K≥3 仅有数值验证（10,000 矩阵零违反），不应标为 Theorem。R2 AGREE with nuance：建议修改措辞而非完全降级（zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别）。分歧：R1 主张降级为 Conjecture，R2 主张 Theorem + Remark 组合。\"\n    action_items:\n      - round: 2\n        action: \"一般情形降级为 Empirical Finding\"\n        assigned_to: agent\n        status: done\n      - round: 3\n        action: \"Mediation 证明 + ε bound\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"补全 Theorem 1 直接证明（V_W(δ) 路径，不依赖 DPI）或降格\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"明确 K=2 为 proved、K≥3 为 numerically verified with zero violations；删除 proof sketch 中 'algebraically' 措辞；或完成 K≥3 symbolic differentiation 证明\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。R4 确认此表述准确。R5 未再提及此特定问题。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [R1, R2]\n        note: \"R2 首发。\"\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"'catastrophic' 与 primary coefficient never reverses 矛盾。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"W2 CRITICAL。Abstract 已改善但 Introduction 仍过度突出 83.4%。\"\n      - round: 5\n        reviewers: [R1]\n        note: \"R1 在交叉回应中 partially rebut R2-Q5：认为 Abstract/Intro 已并列呈现 83.4% 和 2.1%，framing 已足够平衡。R2 维持 83.4% 作为 informative prior 下会大幅降低的观点。分歧不大。\"\n    action_items:\n      - round: 3\n        action: \"Abstract 删 83.4%/catastrophic，加 primary never reverses\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Introduction 中 83.4% 从动机降级为参数空间刻画\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。Round 3-5 未再提及。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"Limitations 应提及 open-source only。\"\n      - round: 5\n        reviewers: []\n        note: \"R5 未显式提及，但 Limitations 中仍未见商业 LLM 讨论。可能已修复待确认。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加商业 LLM 限制说明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。Round 3-5 未再提及。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: open\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Algorithm 1 加 caveat；扩展 logistic 至全 7 拓扑\"\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W3 + R2-N2 共同提出。FWL invariance 根本性依赖线性 SEM。Appendix B.9 logistic DGP 仅验证 sign-flip，未验证 FWL breakdown 或 correction 效果。两位 Reviewer 共识：需至少一个 logistic correction experiment。\"\n    action_items:\n      - round: 3\n        action: \"Algorithm 1 加 caveat；扩展 logistic 至全 7 拓扑\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"Section 4.5 明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑（如 confounding）的 Naive plug-in correction 效果\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。Round 2-5 未再提及。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"统一 τ/β_T；添加 Proposition 交叉引用\"\n      - round: 5\n        reviewers: [R2]\n        note: \"R2-W3：τ 在不同拓扑下含义不同（confounding 是 X→Y 因果效应，exposure 是 category-specific β_j），main text 中切换时无明确提示。\"\n    action_items:\n      - round: 3\n        action: \"统一 τ/β_T；添加 Proposition 交叉引用\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"Section 3.1 添加 τ 在各拓扑下含义的明确说明\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 2 issues ===\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: open\n    first_raised_round: 2\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [R1, R2]\n        note: \"Stress test 已扩展但正文讨论不足。\"\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"W5 MAJOR。已有 outcome-conditional prompting 讨论但缺 few-shot ICL demonstration bias 场景。\"\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W2 + R2-N1 共同提出，均标 MAJOR。R2 引入'文本作为共同原因'框架——LLM 从同一文本同时提取 treatment 和 outcome 信号，这是结构性违反而非 mild violation。R1 补充 RAG 检索和 chain-of-thought 推理渠道。Appendix B.5 stress test 仅测试 ε≤0.10 的人为扰动，未测试 LLM 诱导的真实差异性模式。两位共识：Section 3.1 需加入'text as common cause'讨论 + practitioner diagnostic。\"\n    action_items:\n      - round: 3\n        action: \"正文讨论 non-differential 假设\"\n        assigned_to: agent\n        status: done\n      - round: 4\n        action: \"Limitations 补充 few-shot ICL demonstration 场景\"\n        assigned_to: agent\n        status: in_progress\n      - round: 5\n        action: \"Section 3.1 加入 'text as common cause' 机制讨论；提供 practitioner diagnostic（如在 gold-label 子集上检验 P(A*|A,Y) vs P(A*|A) 的条件独立性）\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"Feder et al. 已引用（Related Work）。Cheng et al. 已引用（Related Work line 164）。R5 未再提及。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。Round 3-5 未再提及。\"\n    resolution_round: 3\n\n  # === Round 3 issues ===\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证（R5 格式检查通过）。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5-R1-S2 确认 FWL 证明'干净且重要'，R2-S3 确认'实用价值'。证明本身不再有问题。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加（'outcome misclassification and correlated multi-annotator settings introduce additional bias channels not captured here'）。R5 未再提及。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [R2]\n        note: \"W11 MINOR。\"\n      - round: 5\n        reviewers: [R2]\n        note: \"R2-W2 MINOR：Introduction 第二段 3 行内 6 个百分比数字；Section 4.4 Cross-K 段落数字密集。建议 Introduction 精简至 2-3 个关键数字，Section 4.4 用表格呈现。\"\n    action_items:\n      - round: 5\n        action: \"Introduction 精简数字密度；Section 4.4 Cross-K 比较考虑表格呈现\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。R4-5 未提及。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。R5 Reproducibility 4/5 确认。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5-R2-S1 确认'首次跨 7 种拓扑系统比较经核查成立'。定位问题已解决。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。R4-5 未再提及。\"\n    resolution_round: 4\n\n  # === Round 4 issues ===\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [R1, R2]\n        note: \"MAJOR。需 sketch proof 或标注为 assumption。\"\n      - round: 5\n        reviewers: []\n        note: \"R5 未显式提及 λ(C) bound 问题。论文 Eq.(3) 标注'under proportional effects (Appendix A, Proposition 4)'。可能已修复待确认。\"\n    action_items:\n      - round: 4\n        action: \"证明 λ(C) ∈ [0,1] 或标为 assumption\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次：(i) analytically proved (Proposition 1(a,b), Theorem 1), (ii) numerically verified (mediation, M-bias, front-door), (iii) conjectured (Conjecture 1)。R5 R1-S3 和 R2-S2 均确认'三级证据层次结构透明'/'层次化处理体现学术诚实'。'Empirical Finding'术语似已替换为'Numerical Verification'。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"R5-R2-S5 确认'ASV 框架是 E-value 的有意义扩展'，列出三个关键差异（K×K→1D 非平凡、三种 ASV 类型、FWL 结合）。R1-S5 确认'具有实践价值'。ASV 创新性质疑已解决。\"\n    resolution_round: 5\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R2]\n        note: \"R2 Excitement 3/5：'NLP 社区可能对此理论较重的工作兴趣有限'。但 R1 Excitement 3.5/5 更正面。R2-S1 同时确认'填补了明确的研究空白'。分歧在于对 NLP venue 的适配性。\"\n    action_items:\n      - round: 4\n        action: \"通过贡献层级重排（theory-first）自然回应\"\n        assigned_to: director\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加'our framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative'。R5 R2-Q3 提出如何定义'most conservative'的后续问题但不再视为缺失。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"R5 未显式提及。Section 4.5 仍仅报告数字。\"\n    action_items:\n      - round: 4\n        action: \"Section 4.5 添加 PPI++ M-bias 机制解释\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"bib 检查：lee_wood_doughty2024 标注为'AIM-FM Workshop, NeurIPS 2024'（有 note='Workshop paper'）；baumann2025 标注为 arXiv preprint。R5 R1 小问题 #6 提及 Baumann 如有正式版本应更新，降级为建议。\"\n    resolution_round: 5\n\n  - id: R4-MR\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇引用（Round 4 新要求）\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"bib 检查确认：Imai/Keele/Yamamoto(2010) ✓, Buonaccorsi(2010) ✓, Blackwell/Honaker/King(2017) ✓, Valeri/VanderWeele(2013) ✓, Pangakis/Wolken/Fasching(2023) ✓。全部已引用。\"\n    resolution_round: 5\n\n  # === Round 5 新增 issues ===\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性，可能误导 practitioners\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1 标 CRITICAL，R2 AGREE。5/7 拓扑的 ✓ 均有 DGP 条件（仅 M-bias 无条件）。Table 1 caption 未提及条件。Practitioners 可能直接查表做决策获得错误安全感。\"\n    action_items:\n      - round: 5\n        action: \"Table 1 用不同符号区分无条件(M-bias)和有条件保证(其余4个)；caption 明确标注'✓ indicates sign preservation under DGP-specific sufficient conditions (Table 5 in Appendix)'\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15，'negligible' 措辞不当\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W1 MAJOR + R2-N3 MAJOR。ε/η 误差在 ASV 0-2 范围内可达 1.3-1.4 δ-units。Table 7 显示 60-98% 矩阵存在非单调步骤。'ε-approximately monotonic' 与如此高非单调比例的修辞紧张。R1 部分 rebut：extreme ε 仅在 extreme τ 下出现，推荐范围内 ε<0.06。\"\n    action_items:\n      - round: 5\n        action: \"'negligible' → 'bounded'；用独立段落讨论 ε 对 δ* 精度的定量影响；明确 ASV 推荐适用范围（|τ| ≥ 0.5）\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N3\n    category: presentation\n    severity: should-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现（23 configs），缺乏理论保证\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1-W4 MINOR + R2-W1 MINOR，交叉回应均 AGREE。Abstract 措辞暗示普遍性。Eq.(2) 表明 same-sign β_k 保证 attenuation only——值得 formalize 但论文未做。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 措辞改为 conditional（'In our experiments, the primary...'）；如可能，formalize same-sign β_k → sign preservation 的充分条件\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R1: Frölich(2007)/Mahajan(2006) IV mismeasured instruments [AGREE both]; Kang&Schafer(2007) doubly robust [R2 partially rebut]. R2: Lash/Fox/Fink(2009/2021) quantitative bias analysis [R1 AGREE]; Kuroki&Pearl(2014) measurement bias [R1 AGREE]; Mohan/Pearl/Tian(2013) [R1 mildly agree].\"\n    action_items:\n      - round: 5\n        action: \"优先添加：Mahajan(2006) 或 Frölich(2007)（IV）、Lash/Fox/Fink(2009/2021)（QBA）、Kuroki&Pearl(2014)（measurement bias）。可选：Mohan/Pearl/Tian(2013)\"\n        assigned_to: agent\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-22T17:10:11.555771+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 17970}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 406
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-22T17:12:29.394435+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR, Long Paper)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+写作质量）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究了 K≥3 类 LLM 标注误差在七种因果 DAG 拓扑下的偏差传播特性。核心发现包括：(1) 二元情形下的 \"toward-null\" 保证在多类情形下结构性失效——exposure 和 IV 拓扑可产生符号反转，而 confounding、collider、mediation、M-bias、front-door 在特定 DGP 条件下保持符号；(2) 基于 FWL 不变性，矩阵类校正方法对 4 种 covariate 拓扑产生恰好 0% 偏差减少；(3) 提出 Annotation Sensitivity Values (ASV) 框架，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱系。23 个真实 LLM 配置的经验验证与理论预测一致。\n\n---\n\n## Strengths\n\n**S1. 系统性的跨拓扑分析填补了明确的研究空白。** [R1-S1, R2-S1, 共识] 现有文献各自分析单一拓扑或仅覆盖二元情形；本文首次在统一框架下用同一混淆矩阵比较 7 种拓扑的偏差行为。\"首次跨 7 种拓扑系统比较\"的声明经 R2 核查成立。\n\n**S2. FWL 不变性负面结果干净且重要。** [R1-S2, R2-S3, 共识] 证明矩阵类校正方法（Naive plug-in, MLA, SIMEX）对 4 种 covariate 拓扑产生 exactly 0% bias reduction。证明路径（column space preservation）简洁完整，是标注校正文献忽略的重要发现。\n\n**S3. 三级证据层次结构透明、学术诚实。** [R1-S3, R2-S2, 共识] 明确区分 (i) 解析证明（Proposition 1(a,b), Theorem 1）、(ii) 数值验证零违反（mediation, M-bias, front-door）、(iii) ε-近似猜想（Conjecture 1），比笼统声称\"我们证明了\"要可信得多。\n\n**S4. 经验验证覆盖面广且设计合理。** [R1-S4, R2-S4, 共识] 23 个真实 LLM 配置 × 7 拓扑 × 3 数据集（HumAID K=10, VAST K=3, CivilComments K=2），覆盖 frontier 到 7B 模型。Theory-MC 一致性 MAPE 2.0%。\n\n**S5. ASV 框架是 E-value 的有意义扩展。** [R1-S5, R2-S5, 共识] 三个关键技术差异（K×K→1D 参数化需证明近似单调性、三种 ASV 类型对应不同失效模式、与 FWL 结合指导校正选择）使其超越 E-value 的简单迁移。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [CRITICAL/MAJOR — R1 CRITICAL, R2 AGREE with nuance] Theorem 1 对 K≥3 缺乏解析证明**\n- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减。关键步骤 V_B(δ) 单调不增：K=2 有解析证明，K≥3 仅有数值验证（10,000 矩阵零违反）。Proof sketch 中 \"algebraically\" 一词可能误导。\n- **分歧**：R1 主张降级为 Conjecture（\"标为 Theorem 意味着有完整证明\"）；R2 主张修改措辞而非降级（\"zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别\"）。\n- **Director 判断**：R2 的 nuance 有理——Theorem 1（zero violations, 强结构约束）与 Conjecture 1（60-98% 非单调步骤，weak ε bound）确有质的区别。建议采用 R2 方案：Theorem 声明中明确 \"K=2: proved; K≥3: verified numerically with zero violations across 10,000 random C₀\"，删除 \"algebraically\" 措辞。\n- **建议修改方向**：Theorem + Remark 组合，或 Theorem 适用 K=2 + Proposition（numerical evidence）适用 K≥3。\n\n**W2 [CRITICAL — R1 CRITICAL, R2 AGREE] Table 1 的 sign-flip guarantee ✓ 掩盖 DGP 条件性**\n- Table 1 对 5 个拓扑标注 ✓（\"structural sign-flip guarantee holds\"），但仅 M-bias 是无条件的。其余 4 个均有 DGP 条件：confounding 需 sign(τ)=sign(τ+B_OV)，mediation 需 sign(τ_dir)=sign(τ_total)，front-door 和 collider 各有条件。Practitioners 直接查表做决策会获得错误安全感。\n- **建议**：用不同符号区分无条件保证（M-bias: ✓）和有条件保证（其余 4 个: ✓*），caption 中明确列出条件引用。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3 [MAJOR — 双方共识] 非差异性误分类假设在 LLM 场景下的适用性讨论不足**\n- LLM 从同一文本同时提取 treatment 和 outcome 信号（\"文本作为共同原因\"），这是 Definition 1 的结构性违反。Few-shot demonstrations 编码 treatment-outcome 关联。RAG 系统可能检索包含 Y 的文档。Appendix B.5 stress test 仅测试人为 ε-perturbation，未测试 LLM 诱导的真实差异性模式。\n- **建议**：Section 3.1 加入 \"text as common cause\" 机制讨论；提供 practitioner diagnostic（如在 gold-label 子集上检验条件独立性）。\n\n**W4 [MAJOR — 双方共识] 线性 SEM 假设限制 FWL 不变性的通用性**\n- FWL 不变性根本性依赖线性投影，在 logistic/probit 回归中不成立。Section 4.5 声称 \"matrix-based corrections are provably ineffective for four topologies\" 严格来说仅在 OLS 下成立。Algorithm 1 的非线性 caveat 仅在 caption 中，正文未讨论。Appendix B.6 logistic DGP 检查仅验证 sign-flip pattern，未验证 FWL breakdown 或 correction 效果。\n- **建议**：Section 4.5 明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑的 correction 效果。\n\n**W5 [MAJOR — 双方共识] Conjecture 1 的 ε 处理过于轻描淡写**\n- ε 可达 0.14（front-door, extreme τ）和 0.15（exposure, extreme-tail matrices），ε/η 误差在 ASV 0-2 范围内可达 1.3-1.4 δ-units。Table 7 显示 60-98% 矩阵存在非单调步骤。\"negligible\" 一词不准确。\n- **缓解因素**：Conjecture 正文已标注了 τ 范围和 ε 上界（非 hidden fine print）；推荐操作范围 τ ∈ [0.5, 2.0] 内 ε < 0.06。\n- **建议**：将 \"negligible\" 改为 \"bounded\"；用独立段落讨论 ε 对 δ* 精度的定量影响；明确 ASV 推荐适用范围。\n\n**W6 [MINOR — 双方共识] \"Primary coefficient never reverses\" 缺乏理论保证**\n- 基于 23 个配置的经验观察，Abstract 措辞暗示普遍性。从 Eq.(2) 看，same-sign β_k 保证仅 attenuation，值得 formalize 但论文未做。\n- **建议**：Abstract 改为 conditional 表述；如可能，formalize same-sign β_k → sign preservation 的充分条件。\n\n**W7 [MINOR — R2] 数字密度较高影响部分段落可读性**\n- Introduction 第二段 3 行内 6 个百分比；Section 4.4 Cross-K 段落密集堆积数字。\n- **建议**：Introduction 精简至 2-3 个关键数字；Cross-K 比较考虑表格呈现。\n\n**W8 [MINOR — R2, R1 AGREE] 符号 τ 在不同拓扑下含义不同，main text 切换时无明确提示**\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 独立提出并在交叉回应中达成共识：\n\n1. **线性 SEM / FWL 限制**（R1-W3 ↔ R2-N2）：FWL 不变性仅在线性框架下成立，需要明确适用范围并在非线性 DGP 下验证\n2. **Non-differential 假设讨论不足**（R1-W2 ↔ R2-N1）：LLM 场景下文本作为共同原因是结构性违反，需要更充分讨论\n3. **Conjecture 1 ε 处理**（R1-W1 ↔ R2-N3）：\"negligible\" 不准确，需要更审慎的呈现\n4. **Primary coefficient claim**（R1-W4 ↔ R2-W1）：经验发现需要降级表述或 formalize 充分条件\n5. **Table 1 条件性**（R1-N2, R2 AGREE）：✓ 符号应区分有条件/无条件保证\n\n---\n\n## Reviewer Divergence [分歧]\n\n**Theorem 1 处理方式**：\n- R1 [CRITICAL]：应降级为 Conjecture/Proposition，因为\"标为 Theorem 意味着有完整证明\"\n- R2 [AGREE with nuance]：应修改措辞而非降级——zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别。建议 Theorem + Remark 组合。\n- **Director 判断**：R2 的区分有理。建议修改措辞明确 K=2 proved / K≥3 numerically verified，而非完全降级。\n\n**Excitement / Venue 适配性**：\n- R1 (3.5/5)：问题重要且具实践价值，但\"与 NLP community 核心关注点有一定距离\"\n- R2 (3/5)：\"NLP 社区可能对此理论较重的工作兴趣有限\"，但 R2-S1 同时确认\"填补明确研究空白\"\n- **Director 判断**：LLM-as-annotator 是 NLP 热点话题，本文的 practical guidance 对 CSS+NLP 交叉社区有直接价值。Excitement 不应成为 reject 理由。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** [R1-Q1, R2 AGREE] Theorem 1 对 K≥3 能否通过 symbolic differentiation 完成 V_B(δ) 的导数符号验证？\n\n**Q2.** [R1-Q2, R2 AGREE] Sign preservation 的 DGP 条件（如 sign(τ)=sign(τ+B_OV)）在实践中如何验证？ASV 框架是否充分解决了这一循环依赖问题？\n\n**Q3.** [R1-Q3, R2 AGREE] Same-sign β_k 是否给出 exposure sign preservation 的充分条件？如果是，这是一个重要结论应 formalize。\n\n**Q4.** [R1-Q5, R2-Q4, 双方共识] FWL 不变性在 logistic regression 下是否 breakdown？能否用 logistic DGP 验证 Naive plug-in 不再是 0% reduction？\n\n**Q5.** [R2-Q2] DGP 参数（τ=2.0）是否代表 CSS 典型效应量？社会科学中效应通常较小（τ<0.5），在小效应下 sign preservation 条件是否更容易被违反？\n\n**Q6.** [R2-Q3] 当候选拓扑包含 exposure（可能反转）和 confounding（不会反转）时，如何操作性地定义 \"most conservative\" ASV？\n\n**Q7.** [R1-Q4] PPI++ 的 gold label fraction 和 sensitivity 分析？\n\n**Q8.** [R1-Q6, R2-Q5 部分分歧] 83.4% 在 informative prior（拟合真实 LLM confusion matrices 的 Dirichlet(α)）下会如何变化？R1 认为当前 framing 已平衡，R2 认为 2.1%（diagonal≥0.7）更具参考价值。\n\n---\n\n## Missing References\n\n**高优先级（双方共识）：**\n1. Mahajan (2006) 或 Frölich (2007) — IV with mismeasured instruments，与 IV 拓扑分析直接相关\n2. Lash, Fox, Fink (2009/2021) — *Applying Quantitative Bias Analysis to Epidemiologic Data*，QBA 标准教科书，与 ASV 框架定位相关\n3. Kuroki & Pearl (2014) — measurement bias and effect restoration，与 correction guidance 形成对照\n\n**可选（部分共识）：**\n4. Mohan, Pearl, Tian (2013) — missing data as causal problem（R1 mildly agree，相关性有限）\n5. Kang & Schafer (2007) — doubly robust estimators（R2 partially rebut，FWL invariance 的线性框架限制）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：失败。** 视觉审查 Agent 因资源限制（rate limit）未能完成逐页检查。Error: \"You've hit your limit · resets 4pm (UTC)\"。建议用户可在资源恢复后重新触发。\n\n**格式合规（R2 手动检查）：** 全部通过——正文 ≤ 8 页、ACL 模板（`\\usepackage[review]{acl}`）、匿名（\"Anonymous ACL submission\"）、Limitations 覆盖 4 个局限点、References 格式一致、图表清晰可读。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 (Borderline Conference)**\n**置信度：4/5**（两位 Reviewer 均为 4/5）\n\n### 评分理由\n\n**支持接收的因素：**\n- 填补了跨拓扑系统比较的明确研究空白（首创性经核查成立）\n- FWL 不变性负面结果对标注校正文献有重要修正意义\n- 三级证据层次处理体现学术诚实\n- 经验验证覆盖广（23 LLM configs × 7 topologies × 3 datasets, MAPE 2.0%）\n- ASV 框架为从业者提供可操作的敏感性分析工具\n- 格式合规，写作整体清晰\n\n**阻止更高评分的因素：**\n- Theorem 1 对 K≥3 的证明不完整（核心理论结果依赖数值验证）\n- Table 1 的 ✓ 符号掩盖 DGP 条件性，可能误导 practitioners\n- Non-differential misclassification 假设在 LLM 场景下的适用性受限，论文对此讨论不足\n- 线性 SEM 限制了 FWL 不变性等核心结论的通用性，非线性验证缺失\n- Conjecture 1 的 ε 在极端条件下较大，对 ASV 精度的影响被低估\n\n### 接收建议\n\n本文处于 Conference/Findings 边界。如果作者能在 camera-ready 中：\n1. 修改 Theorem 1 措辞明确 K≥3 的数值验证性质（成本低，效果大）\n2. 修改 Table 1 区分有条件/无条件保证（成本低，效果大）\n3. 在 Section 3.1 和 Section 4.5 中分别加强 non-differential 假设和线性 SEM 限制的讨论（成本中等）\n\n则论文可达到 Conference 水平。当前版本更适合 Findings。\n\n### 维度评分汇总\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 整体准确概括了三个贡献\n- \"the primary treatment effect never reverses in any of 23 empirical LLM configurations\" 应改为 conditional 表述\n- 数字密度可控（~5 个核心数字），较前版本已大幅改善\n\n### Section 1 (Introduction)\n- 动机叙事有说服力：LLM annotators 快速普及 + K≥3 结构性突变\n- 83.4% 与 2.1% 的并列呈现已较平衡，但 Introduction 第二段数字密度仍高（3 行 6 个百分比）\n- 三个贡献陈述清晰\n\n### Section 2 (Related Work)\n- 三段结构（measurement error / LLM annotation / sensitivity analysis）覆盖完整\n- 定位准确：\"all analyze a single DAG topology; ours is the first to characterize across seven\"\n- 缺少 Mahajan(2006)/Frölich(2007)（IV mismeasurement）、Lash/Fox/Fink(2009/2021)（QBA）、Kuroki&Pearl(2014)\n\n### Section 3 (Method)\n- Definition 1 需加 \"text as common cause\" 讨论\n- Bias expressions (3.2) 推导清晰，7 个拓扑的处理系统\n- Proposition 1 的条件在正文中呈现较好，但 Table 1 未反映\n- Theorem 1 的 proof sketch 需修改 \"algebraically\" 措辞\n- Conjecture 1 正文已标注 ε 范围（非 hidden fine print），但 \"negligible\" 一词需替换\n- ASV 三种类型的动机和定义清晰\n\n### Section 4 (Experiments)\n- Theory-MC agreement MAPE 2.0% 可靠（R1 建议补充 tail statistics，合理）\n- Exposure sign reversal 分析充分（Dirichlet full + realistic subspace）\n- Empirical validation 23 configs × 7 topologies 覆盖广\n- Correction guidance 的 FWL invariance 需明确线性适用范围\n- Cross-K comparison 数字密度高，建议表格化\n\n### Section 5 (Conclusion + Limitations)\n- Conclusion 简洁到位\n- Limitations 覆盖 4 个点：non-differential assumption, DAG specification, K/nonlinearity extensions, single annotator\n- 建议补充：商业 LLM 缺失、线性 SEM 对 FWL 的限制\n\n### Appendix\n- 证明细节充分（Appendix A）\n- 实验补充完整（Appendix B）\n- ClinicalBERT 案例研究（Appendix B.3）过于简略，建议加定量 ASV 计算\n",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "\n# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (via ARR, Long Paper)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+写作质量）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究了 K≥3 类 LLM 标注误差在七种因果 DAG 拓扑下的偏差传播特性。核心发现包括：(1) 二元情形下的 \"toward-null\" 保证在多类情形下结构性失效——exposure 和 IV 拓扑可产生符号反转，而 confounding、collider、mediation、M-bias、front-door 在特定 DGP 条件下保持符号；(2) 基于 FWL 不变性，矩阵类校正方法对 4 种 covariate 拓扑产生恰好 0% 偏差减少；(3) 提出 Annotation Sensitivity Values (ASV) 框架，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱系。23 个真实 LLM 配置的经验验证与理论预测一致。\n\n---\n\n## Strengths\n\n**S1. 系统性的跨拓扑分析填补了明确的研究空白。** [R1-S1, R2-S1, 共识] 现有文献各自分析单一拓扑或仅覆盖二元情形；本文首次在统一框架下用同一混淆矩阵比较 7 种拓扑的偏差行为。\"首次跨 7 种拓扑系统比较\"的声明经 R2 核查成立。\n\n**S2. FWL 不变性负面结果干净且重要。** [R1-S2, R2-S3, 共识] 证明矩阵类校正方法（Naive plug-in, MLA, SIMEX）对 4 种 covariate 拓扑产生 exactly 0% bias reduction。证明路径（column space preservation）简洁完整，是标注校正文献忽略的重要发现。\n\n**S3. 三级证据层次结构透明、学术诚实。** [R1-S3, R2-S2, 共识] 明确区分 (i) 解析证明（Proposition 1(a,b), Theorem 1）、(ii) 数值验证零违反（mediation, M-bias, front-door）、(iii) ε-近似猜想（Conjecture 1），比笼统声称\"我们证明了\"要可信得多。\n\n**S4. 经验验证覆盖面广且设计合理。** [R1-S4, R2-S4, 共识] 23 个真实 LLM 配置 × 7 拓扑 × 3 数据集（HumAID K=10, VAST K=3, CivilComments K=2），覆盖 frontier 到 7B 模型。Theory-MC 一致性 MAPE 2.0%。\n\n**S5. ASV 框架是 E-value 的有意义扩展。** [R1-S5, R2-S5, 共识] 三个关键技术差异（K×K→1D 参数化需证明近似单调性、三种 ASV 类型对应不同失效模式、与 FWL 结合指导校正选择）使其超越 E-value 的简单迁移。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [CRITICAL/MAJOR — R1 CRITICAL, R2 AGREE with nuance] Theorem 1 对 K≥3 缺乏解析证明**\n- Theorem 1 声称 confounding 和 mediation（proportional effects）下 |B(C(δ))| 关于 δ 单调不减。关键步骤 V_B(δ) 单调不增：K=2 有解析证明，K≥3 仅有数值验证（10,000 矩阵零违反）。Proof sketch 中 \"algebraically\" 一词可能误导。\n- **分歧**：R1 主张降级为 Conjecture（\"标为 Theorem 意味着有完整证明\"）；R2 主张修改措辞而非降级（\"zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别\"）。\n- **Director 判断**：R2 的 nuance 有理——Theorem 1（zero violations, 强结构约束）与 Conjecture 1（60-98% 非单调步骤，weak ε bound）确有质的区别。建议采用 R2 方案：Theorem 声明中明确 \"K=2: proved; K≥3: verified numerically with zero violations across 10,000 random C₀\"，删除 \"algebraically\" 措辞。\n- **建议修改方向**：Theorem + Remark 组合，或 Theorem 适用 K=2 + Proposition（numerical evidence）适用 K≥3。\n\n**W2 [CRITICAL — R1 CRITICAL, R2 AGREE] Table 1 的 sign-flip guarantee ✓ 掩盖 DGP 条件性**\n- Table 1 对 5 个拓扑标注 ✓（\"structural sign-flip guarantee holds\"），但仅 M-bias 是无条件的。其余 4 个均有 DGP 条件：confounding 需 sign(τ)=sign(τ+B_OV)，mediation 需 sign(τ_dir)=sign(τ_total)，front-door 和 collider 各有条件。Practitioners 直接查表做决策会获得错误安全感。\n- **建议**：用不同符号区分无条件保证（M-bias: ✓）和有条件保证（其余 4 个: ✓*），caption 中明确列出条件引用。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3 [MAJOR — 双方共识] 非差异性误分类假设在 LLM 场景下的适用性讨论不足**\n- LLM 从同一文本同时提取 treatment 和 outcome 信号（\"文本作为共同原因\"），这是 Definition 1 的结构性违反。Few-shot demonstrations 编码 treatment-outcome 关联。RAG 系统可能检索包含 Y 的文档。Appendix B.5 stress test 仅测试人为 ε-perturbation，未测试 LLM 诱导的真实差异性模式。\n- **建议**：Section 3.1 加入 \"text as common cause\" 机制讨论；提供 practitioner diagnostic（如在 gold-label 子集上检验条件独立性）。\n\n**W4 [MAJOR — 双方共识] 线性 SEM 假设限制 FWL 不变性的通用性**\n- FWL 不变性根本性依赖线性投影，在 logistic/probit 回归中不成立。Section 4.5 声称 \"matrix-based corrections are provably ineffective for four topologies\" 严格来说仅在 OLS 下成立。Algorithm 1 的非线性 caveat 仅在 caption 中，正文未讨论。Appendix B.6 logistic DGP 检查仅验证 sign-flip pattern，未验证 FWL breakdown 或 correction 效果。\n- **建议**：Section 4.5 明确 FWL 适用范围限于线性模型；logistic DGP 下验证至少一个拓扑的 correction 效果。\n\n**W5 [MAJOR — 双方共识] Conjecture 1 的 ε 处理过于轻描淡写**\n- ε 可达 0.14（front-door, extreme τ）和 0.15（exposure, extreme-tail matrices），ε/η 误差在 ASV 0-2 范围内可达 1.3-1.4 δ-units。Table 7 显示 60-98% 矩阵存在非单调步骤。\"negligible\" 一词不准确。\n- **缓解因素**：Conjecture 正文已标注了 τ 范围和 ε 上界（非 hidden fine print）；推荐操作范围 τ ∈ [0.5, 2.0] 内 ε < 0.06。\n- **建议**：将 \"negligible\" 改为 \"bounded\"；用独立段落讨论 ε 对 δ* 精度的定量影响；明确 ASV 推荐适用范围。\n\n**W6 [MINOR — 双方共识] \"Primary coefficient never reverses\" 缺乏理论保证**\n- 基于 23 个配置的经验观察，Abstract 措辞暗示普遍性。从 Eq.(2) 看，same-sign β_k 保证仅 attenuation，值得 formalize 但论文未做。\n- **建议**：Abstract 改为 conditional 表述；如可能，formalize same-sign β_k → sign preservation 的充分条件。\n\n**W7 [MINOR — R2] 数字密度较高影响部分段落可读性**\n- Introduction 第二段 3 行内 6 个百分比；Section 4.4 Cross-K 段落密集堆积数字。\n- **建议**：Introduction 精简至 2-3 个关键数字；Cross-K 比较考虑表格呈现。\n\n**W8 [MINOR — R2, R1 AGREE] 符号 τ 在不同拓扑下含义不同，main text 切换时无明确提示**\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 独立提出并在交叉回应中达成共识：\n\n1. **线性 SEM / FWL 限制**（R1-W3 ↔ R2-N2）：FWL 不变性仅在线性框架下成立，需要明确适用范围并在非线性 DGP 下验证\n2. **Non-differential 假设讨论不足**（R1-W2 ↔ R2-N1）：LLM 场景下文本作为共同原因是结构性违反，需要更充分讨论\n3. **Conjecture 1 ε 处理**（R1-W1 ↔ R2-N3）：\"negligible\" 不准确，需要更审慎的呈现\n4. **Primary coefficient claim**（R1-W4 ↔ R2-W1）：经验发现需要降级表述或 formalize 充分条件\n5. **Table 1 条件性**（R1-N2, R2 AGREE）：✓ 符号应区分有条件/无条件保证\n\n---\n\n## Reviewer Divergence [分歧]\n\n**Theorem 1 处理方式**：\n- R1 [CRITICAL]：应降级为 Conjecture/Proposition，因为\"标为 Theorem 意味着有完整证明\"\n- R2 [AGREE with nuance]：应修改措辞而非降级——zero violations + proportional effects 约束使其与 Conjecture 1 有质的区别。建议 Theorem + Remark 组合。\n- **Director 判断**：R2 的区分有理。建议修改措辞明确 K=2 proved / K≥3 numerically verified，而非完全降级。\n\n**Excitement / Venue 适配性**：\n- R1 (3.5/5)：问题重要且具实践价值，但\"与 NLP community 核心关注点有一定距离\"\n- R2 (3/5)：\"NLP 社区可能对此理论较重的工作兴趣有限\"，但 R2-S1 同时确认\"填补明确研究空白\"\n- **Director 判断**：LLM-as-annotator 是 NLP 热点话题，本文的 practical guidance 对 CSS+NLP 交叉社区有直接价值。Excitement 不应成为 reject 理由。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** [R1-Q1, R2 AGREE] Theorem 1 对 K≥3 能否通过 symbolic differentiation 完成 V_B(δ) 的导数符号验证？\n\n**Q2.** [R1-Q2, R2 AGREE] Sign preservation 的 DGP 条件（如 sign(τ)=sign(τ+B_OV)）在实践中如何验证？ASV 框架是否充分解决了这一循环依赖问题？\n\n**Q3.** [R1-Q3, R2 AGREE] Same-sign β_k 是否给出 exposure sign preservation 的充分条件？如果是，这是一个重要结论应 formalize。\n\n**Q4.** [R1-Q5, R2-Q4, 双方共识] FWL 不变性在 logistic regression 下是否 breakdown？能否用 logistic DGP 验证 Naive plug-in 不再是 0% reduction？\n\n**Q5.** [R2-Q2] DGP 参数（τ=2.0）是否代表 CSS 典型效应量？社会科学中效应通常较小（τ<0.5），在小效应下 sign preservation 条件是否更容易被违反？\n\n**Q6.** [R2-Q3] 当候选拓扑包含 exposure（可能反转）和 confounding（不会反转）时，如何操作性地定义 \"most conservative\" ASV？\n\n**Q7.** [R1-Q4] PPI++ 的 gold label fraction 和 sensitivity 分析？\n\n**Q8.** [R1-Q6, R2-Q5 部分分歧] 83.4% 在 informative prior（拟合真实 LLM confusion matrices 的 Dirichlet(α)）下会如何变化？R1 认为当前 framing 已平衡，R2 认为 2.1%（diagonal≥0.7）更具参考价值。\n\n---\n\n## Missing References\n\n**高优先级（双方共识）：**\n1. Mahajan (2006) 或 Frölich (2007) — IV with mismeasured instruments，与 IV 拓扑分析直接相关\n2. Lash, Fox, Fink (2009/2021) — *Applying Quantitative Bias Analysis to Epidemiologic Data*，QBA 标准教科书，与 ASV 框架定位相关\n3. Kuroki & Pearl (2014) — measurement bias and effect restoration，与 correction guidance 形成对照\n\n**可选（部分共识）：**\n4. Mohan, Pearl, Tian (2013) — missing data as causal problem（R1 mildly agree，相关性有限）\n5. Kang & Schafer (2007) — doubly robust estimators（R2 partially rebut，FWL invariance 的线性框架限制）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：失败。** 视觉审查 Agent 因资源限制（rate limit）未能完成逐页检查。Error: \"You've hit your limit · resets 4pm (UTC)\"。建议用户可在资源恢复后重新触发。\n\n**格式合规（R2 手动检查）：** 全部通过——正文 ≤ 8 页、ACL 模板（`\\usepackage[review]{acl}`）、匿名（\"Anonymous ACL submission\"）、Limitations 覆盖 4 个局限点、References 格式一致、图表清晰可读。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 (Borderline Conference)**\n**置信度：4/5**（两位 Reviewer 均为 4/5）\n\n### 评分理由\n\n**支持接收的因素：**\n- 填补了跨拓扑系统比较的明确研究空白（首创性经核查成立）\n- FWL 不变性负面结果对标注校正文献有重要修正意义\n- 三级证据层次处理体现学术诚实\n- 经验验证覆盖广（23 LLM configs × 7 topologies × 3 datasets, MAPE 2.0%）\n- ASV 框架为从业者提供可操作的敏感性分析工具\n- 格式合规，写作整体清晰\n\n**阻止更高评分的因素：**\n- Theorem 1 对 K≥3 的证明不完整（核心理论结果依赖数值验证）\n- Table 1 的 ✓ 符号掩盖 DGP 条件性，可能误导 practitioners\n- Non-differential misclassification 假设在 LLM 场景下的适用性受限，论文对此讨论不足\n- 线性 SEM 限制了 FWL 不变性等核心结论的通用性，非线性验证缺失\n- Conjecture 1 的 ε 在极端条件下较大，对 ASV 精度的影响被低估\n\n### 接收建议\n\n本文处于 Conference/Findings 边界。如果作者能在 camera-ready 中：\n1. 修改 Theorem 1 措辞明确 K≥3 的数值验证性质（成本低，效果大）\n2. 修改 Table 1 区分有条件/无条件保证（成本低，效果大）\n3. 在 Section 3.1 和 Section 4.5 中分别加强 non-differential 假设和线性 SEM 限制的讨论（成本中等）\n\n则论文可达到 Conference 水平。当前版本更适合 Findings。\n\n### 维度评分汇总\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 整体准确概括了三个贡献\n- \"the primary treatment effect never reverses in any of 23 empirical LLM configurations\" 应改为 conditional 表述\n- 数字密度可控（~5 个核心数字），较前版本已大幅改善\n\n### Section 1 (Introduction)\n- 动机叙事有说服力：LLM annotators 快速普及 + K≥3 结构性突变\n- 83.4% 与 2.1% 的并列呈现已较平衡，但 Introduction 第二段数字密度仍高（3 行 6 个百分比）\n- 三个贡献陈述清晰\n\n### Section 2 (Related Work)\n- 三段结构（measurement error / LLM annotation / sensitivity analysis）覆盖完整\n- 定位准确：\"all analyze a single DAG topology; ours is the first to characterize across seven\"\n- 缺少 Mahajan(2006)/Frölich(2007)（IV mismeasurement）、Lash/Fox/Fink(2009/2021)（QBA）、Kuroki&Pearl(2014)\n\n### Section 3 (Method)\n- Definition 1 需加 \"text as common cause\" 讨论\n- Bias expressions (3.2) 推导清晰，7 个拓扑的处理系统\n- Proposition 1 的条件在正文中呈现较好，但 Table 1 未反映\n- Theorem 1 的 proof sketch 需修改 \"algebraically\" 措辞\n- Conjecture 1 正文已标注 ε 范围（非 hidden fine print），但 \"negligible\" 一词需替换\n- ASV 三种类型的动机和定义清晰\n\n### Section 4 (Experiments)\n- Theory-MC agreement MAPE 2.0% 可靠（R1 建议补充 tail statistics，合理）\n- Exposure sign reversal 分析充分（Dirichlet full + realistic subspace）\n- Empirical validation 23 configs × 7 topologies 覆盖广\n- Correction guidance 的 FWL invariance 需明确线性适用范围\n- Cross-K comparison 数字密度高，建议表格化\n\n### Section 5 (Conclusion + Limitations)\n- Conclusion 简洁到位\n- Limitations 覆盖 4 个点：non-differential assumption, DAG specification, K/nonlinearity extensions, single annotator\n- 建议补充：商业 LLM 缺失、线性 SEM 对 FWL 的限制\n\n### Appendix\n- 证明细节充分（Appendix A）\n- 实验补充完整（Appendix B）\n- ClinicalBERT 案例研究（Appendix B.3）过于简略，建议加定量 ASV 计算\n",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T17:12:42.564331+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 13169
}
```

</details>

---


### Assistant

_source line 410 · 2026-05-22T17:12:51.062744+00:00_

审稿报告已投递给 Research Director。

---

**Round 5 审稿完成汇总：**

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致
- **2 个 Must-Fix**：Theorem 1 K≥3 证明措辞需修改；Table 1 的 ✓ 需区分有条件/无条件保证
- **3 个 Major Should-Fix**：non-differential 假设讨论不足；线性 SEM 限制 FWL 通用性；Conjecture 1 ε 呈现需更审慎
- **3 个 Minor**：primary coefficient claim、数字密度、符号一致性
- **3 篇高优先级缺失引用**：Mahajan(2006)/Frölich(2007)、Lash/Fox/Fink(2009/2021)、Kuroki&Pearl(2014)
- **接收建议**：当前版本更适合 Findings；若修复 W1-W2（成本低）+ 加强 W3-W5 讨论（成本中等），可达 Conference 水平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 411 · 2026-05-22T17:12:53.822861+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 11 个具体问题（3 MAJOR + 4 MINOR + 5 Questions）逐条给出了 [AGREE]/[REBUT]，并整理了两位 reviewer 的共识与分歧。

核心结论：
- 8/11 项 [AGREE]（含 2 项 "with nuance"）
- 1 项 partial [REBUT]（Q5: 83.4% vs 2.1% 的呈现已足够平衡）
- R1 的两个独有 CRITICAL 关切（Theorem 1 proof gap、Table 1 条件性）R2 未覆盖
- 两位 reviewer 评分一致（3.5），关切互补：R1 侧重理论严谨性，R2 侧重假设适用性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-22T17:13:13.045976+00:00_

审稿报告已投递完毕。

**Round 5 审稿总结：**

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致
- **2 个 Must-Fix**：Theorem 1 的 K≥3 证明不完整（R1 CRITICAL / R2 修改措辞即可）；Table 1 的 ✓ 掩盖 DGP 条件性
- **3 个 Should-Fix（双方共识）**：non-differential 假设讨论不足、线性 SEM 限制 FWL 通用性、Conjecture 1 的 ε 处理轻描淡写
- **接收建议**：当前版本处于 Conference/Findings 边界，修改 Theorem 1 措辞 + Table 1 符号 + 加强假设讨论后可达 Conference 水平

Issue Tracker 已同步更新至 `review_issues.yaml`。视觉审查因资源限制未完成，格式合规由 R2 手动确认全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 45

## Round 45

52 recorded events


### User

_source line 413 · 2026-05-22T17:37:30.611660+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-22T17:37:45.199747+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-22T17:37:45.352759+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-22T17:37:55.970643+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-22T17:37:56.021384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-22T17:38:02.715234+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 419 · 2026-05-22T17:38:02.817359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-22T17:38:06.295766+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 421 · 2026-05-22T17:38:06.346504+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-22T17:38:10.829219+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 423 · 2026-05-22T17:38:10.930079+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-22T17:38:16.701479+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-22T17:38:18.213318+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1511
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-22T17:38:18.213880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-22T17:38:19.125436+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{method}
39	
40	% ── Figures ──
41	
42	\begin{figure*}[t]
43	\centering
44	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
45	\vspace{-6pt}
46	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
47	\label{fig:dag_taxonomy}
48	\end{figure*}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
53	\vspace{-6pt}
54	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
55	\label{fig:bias_distribution}
56	\end{figure*}
57	
58	\input{experiments}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix_proofs}
66	
67	\end{document}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-22T17:38:19.126012+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-22T17:38:19.327021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-22T17:38:19.430918+00:00_

1	issues:
2	  # === Carried from Round 1-4, updated through Round 5 fixes ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 5
11	    mentions:
12	      - round: 1
13	        reviewers: [R1, R2]
14	        note: "R1 首发，R2 AGREE。"
15	      - round: 2
16	        reviewers: [R1, R2]
17	        note: "一般情形降级为 Empirical Finding，保留比例情形证明。"
18	      - round: 3
19	        reviewers: [R1, R2]
20	        note: "R1 critical, R2 should-fix。建议至少证明 mediation；给出 formal ε bound。"
21	      - round: 4
22	        reviewers: [R1, R2]
23	        note: "W1 CRITICAL。DPI 证明路径不成立（C(δ) 不满足 stochastic degradation）。Appendix A.4 有 V_W(δ) 直接路径但未升级。必须补全或降格。"
24	      - round: 5
25	        reviewers: [R1]
26	        note: "R1 仍标 CRITICAL：K≥3 仅有数值验证（10,000 矩阵零违反），不应标为 Theorem。R2 AGREE with nuance：建议修改措辞而非完全降级。"
27	    action_items:
28	      - round: 2
29	        action: "一般情形降级为 Empirical Finding"
30	        assigned_to: agent
31	        status: done
32	      - round: 3
33	        action: "Mediation 证明 + ε bound"
34	        assigned_to: agent
35	        status: done
36	      - round: 4
37	        action: "补全 Theorem 1 直接证明（V_W(δ) 路径，不依赖 DPI）或降格"
38	        assigned_to: agent
39	        status: done
40	      - round: 5
41	        action: "Perspective function + convexity proof：K=2 fully proved，K≥3 worst-case <0.005 deviation across 20,000 random triples。DPI 全部移除。"
42	        assigned_to: agent
43	        status: done
44	    resolution: "Theorem 1 使用 perspective function + convexity 证明路径：K=2 精确证明，K≥3 数值验证 worst-case <0.005。DPI 引用全部移除。proof sketch 无 algebraically 措辞。"
45	    resolution_round: 5
46	
47	  - id: R1-N2
48	    category: soundness
49	    severity: should-fix
50	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
51	    status: resolved
52	    first_raised_round: 1
53	    last_seen_round: 3
54	    resolut
…[truncated 17651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-22T17:38:28.307119+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found some relevant information about EMNLP 2026, though th
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9181
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-22T17:38:34.196036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-22T17:38:34.701023+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Budapest submission deadline commitment deadline"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-22T17:38:39.779628+00:00_

Web search results for query: "EMNLP 2026 Budapest submission deadline commitment deadline"

Links: [{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here are the key deadlines for EMNLP 2026 in Budapest:

**Submission Deadline:**
The EMNLP 2026 paper submission deadline is May 25, 2026, 23:59:59 (UTC-12). This is the ARR (ACL Rolling Review) submission deadline for long and short papers.

**Commitment Deadline:**
The EMNLP commitment deadline is August 2, 2026. This is when authors must commit their papers to EMNLP after receiving their reviews from ARR.

**Other Important Dates:**
- Reviewer registration deadline for
…[truncated 377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5078
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-22T17:38:41.748595+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

I found relevant information about ACL Rolling Review (ARR) submission guidelines. Here's what I found from the search results:

## ARR 2026 Submission Guidelines

**Author Instructions:**
Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template. Authors are encouraged to have a look at the 
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7552
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-22T17:38:52.328226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-22T17:38:52.737001+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), the sign reversal rate is 2.1\%, exclusively in secondary coefficients---in all 23 empirical configurations tested, the primary treatment effect does not reverse---consistent with the largest-magnitude coefficient dominating the misclassification-induced weighted sum. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 408
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-22T17:38:52.737560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-22T17:38:53.291427+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed---a stru
…[truncated 2242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-22T17:38:53.291947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-22T17:38:53.751417+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose structured approaches to reduce LLM measurement error, and \citet{kim_garg2025} showed 60\% error correlation across models. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the broader landscape. These works either restrict to binary labels, cover 
…[truncated 1436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-22T17:38:53.751978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-22T17:38:54.609800+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This assumption is natural when the LLM annotates treatment labels from source documents without access to outcome information. However, in many NLP annotation pipelines, the same text that determines $A$ also carries information about $Y$---a ``text as common cause'' structure that creates a channel for differential misclassification even without explicit access to $Y$. Specific violation pathways include: (i)~outcome-conditional prompting, (ii)~few-shot demonstrations encoding $A$--$Y$ associations, and (iii)~retrieval-augmented pipelines surfacing $Y$-correlated documents. Practitioners can diagnose potential violations by testing $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on a gold-labeled subset (see Limitations).
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship betwee
…[truncated 14093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-22T17:38:54.660544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-22T17:38:54.761546+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate the bias taxonomy and ASV framework through analytical derivations and Monte Carlo simulation across seven DAG topologies under $K{=}3$ non-differential misclassification.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 2.0\% across 126 scenarios (18 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.5\% (confounding) to 5.5\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices produce bias that violates the binary ``toward-null'' guarantee. More critically, 83.4\% of matrices cause \emph{sign reversal} of at least one coefficient. The two failure modes are distinct: for a coefficient with true value $\beta_1{=}1.0$, a near-permutation $C$ produces $\hat{\gamma}_1{=}{-}0.84$ (sign reversal, magnitude $0.84{\times}$); for $\beta_2{=}{-}0.5$, the same $C$ yields $\hat{\gamma}_2{=}{-}1.41$ (same-sign amplification, $2.83{\times}$).
19	
20	This finding persists in practically relevant subspaces. When restricting to confusion matrices with diagonal entries $\geq 0.7$ (typical of current LLM classifiers achieving $F_1 > 0.8$), the violation rate remains 13.7\% with 2.1\% sign reversal and 11.7\% amplification. Even at diagona
…[truncated 9242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-22T17:38:54.762060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-22T17:38:55.271385+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary treatment effect never reverses, but 61\% of exposure configurations reverse a secondary coefficient. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinear models (Appendix~\ref{sec:logistic_dgp}) remain open. We address misclassification of $A$ by a single annotator; outcome misclassification and correlated multi-annotator settings~\cite{kim_garg2025} introduce additional bias channels not captured here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 509
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-22T17:38:55.271902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-22T17:38:55.825474+00:00_

File content (34174 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-22T17:38:55.876140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-22T17:38:55.982707+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},
31	  volume    = {50},
32	  number    = {1},
33	  pages     = {237--291},
34	  doi       = {10.1162/coli\_a\_00502},
35	}
36	
37	@incollection{bound2001measurement,
38	  author    = {Bound, John and Brown, Charles and Mathiowetz, Nancy},
39	  title     = {Measurement Error in Survey Data},
40	  booktitle = {Handbook of Econometrics},
41	  editor    = {Heckman, James J. and Leamer, Edward E.},
42	  year      = {2001},
43	  volume    = {5},
44	  chapter   = {59},
45	  pages     = {3705--3843},
46	  publisher = {Elsevier},
47	}
48	
49	@article{richardson1993bayesian,
50	  author    = {Richardson, Sylvia and Gilks, Walter R.},
51	  title     = {A {Bayesian} Approach to Measurement Error Problems in Epidemiology Using Conditional Independence Models},
52	  journal   = {Amer
…[truncated 14941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 106
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-22T17:39:02.729235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-22T17:39:03.585198+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 8490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-22T17:39:03.791770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-22T17:39:06.516255+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf (880.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 2724
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-22T17:39:58.002195+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-22T17:39:58.505984+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-22T17:40:16.360722+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18358
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-22T17:40:16.413354+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 17907
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-22T17:40:16.464118+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（References 不限；Limitations 不计入页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者标注为 \"Anonymous\"）\n- **附录**: 允许，审稿人可选择性审查\n\n## 你的审查侧重\n\n**方法严谨性**——聚焦以下方面：\n\n1. **数学正确性**：\n   - Proposition 1（sign preservation for confounding/collider）的证明是否完整、正确？\n   - Theorem 1（envelope monotonicity）的证明路径（perspective function + convexity）是否严密？K≥3 的数值验证是否足够？\n   - Conjecture 1（ε-approximate monotonicity）的数值验证规模（30,000 matrices）是否充分？ε bounds 是否合理？\n   - Eq.(3) 中 λ(C) ∈ [0,1] 的条件（proportional effects）是否明确标注？\n\n2. **假设与适用范围**：\n   - Non-differential misclassification 假设的合理性和限制讨论是否充分？\n   - 线性 SEM 假设对结论的限制是否清楚？\n   - \"Primary coefficient never reverses\" 的声称——是理论保证还是经验发现？措辞是否准确？\n\n3. **实验方法论**：\n   - Monte Carlo 验证的设计（N=10,000, 100,000 matrices）是否充分？\n   - 经验验证使用 4 个 LLM × 3 个数据集的覆盖面是否足够？\n   - FWL invariance 的证明和实验验证是否一致？\n   - Correction methods 的评估方法是否公平？\n\n4. **内部一致性**：\n   - Abstract/Introduction 中的声称与 Method/Experiments 中的结果是否一致？\n   - 证明层级（proved/verified/conjectured）是否在全文中一致使用？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（标注 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Detailed Comments → Scores（Soundness, Excitement, Reproducibility, Overall 各 1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（References 不限；Limitations 不计入页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者标注为 \"Anonymous\"）\n- **附录**: 允许，审稿人可选择性审查\n\n## 你的审查侧重\n\n**方法严谨性**——聚焦以下方面：\n\n1. **数学正确性**：\n   - Proposition 1（sign preservation for confounding/collider）的证明是否完整、正确？\n   - Theorem 1（envelope monotonicity）的证明路径（perspective function + convexity）是否严密？K≥3 的数值验证是否足够？\n   - Conjecture 1（ε-approximate monotonicity）的数值验证规模（30,000 matrices）是否充分？ε bounds 是否合理？\n   - Eq.(3) 中 λ(C) ∈ [0,1] 的条件（proportional effects）是否明确标注？\n\n2. **假设与适用范围**：\n   - Non-differential misclassification 假设的合理性和限制讨论是否充分？\n   - 线性 SEM 假设对结论的限制是否清楚？\n   - \"Primary coefficient never reverses\" 的声称——是理论保证还是经验发现？措辞是否准确？\n\n3. **实验方法论**：\n   - Monte Carlo 验证的设计（N=10,000, 100,000 matrices）是否充分？\n   - 经验验证使用 4 个 LLM × 3 个数据集的覆盖面是否足够？\n   - FWL invariance 的证明和实验验证是否一致？\n   - Correction methods 的评估方法是否公平？\n\n4. **内部一致性**：\n   - Abstract/Introduction 中的声称与 Method/Experiments 中的结果是否一致？\n   - 证明层级（proved/verified/conjectured）是否在全文中一致使用？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（标注 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Detailed Comments → Scores（Soundness, Excitement, Reproducibility, Overall 各 1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-22T17:40:32.916357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16452
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-22T17:40:33.020403+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（References 不限；Limitations 不计入页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者标注为 \"Anonymous\"）\n- **附录**: 允许，审稿人可选择性审查\n\n## 你的审查侧重\n\n**新颖性与完整性**——聚焦以下方面：\n\n1. **新颖性与贡献定位**：\n   - 三个贡献（bias taxonomy, correction guidance, ASV）相对于现有工作的增量价值？\n   - \"首次跨 7 种拓扑系统比较\"——这一声称是否准确？是否有先行工作被遗漏？\n   - ASV 相对于 E-value 的创新点是否清晰？是直接移植还是有实质性扩展？\n   - FWL invariance 作为\"negative result\"的价值——是否真的被 annotation correction 文献忽略？\n\n2. **Related Work 覆盖**：\n   - 测量误差文献（epidemiology + econometrics）的覆盖是否完整？\n   - LLM annotation 文献的覆盖是否及时（2024-2025 最新工作）？\n   - 是否有重要的缺失引用？特别关注：\n     - 非线性模型下的 misclassification 文献\n     - Multi-annotator / ensemble 校正方法\n     - Bayesian measurement error 最新进展\n\n3. **Presentation 质量**：\n   - 论文结构是否清晰？信息密度是否合适？\n   - 数学符号是否统一、定义是否清晰？\n   - 图表质量和信息传达效率\n   - Abstract/Introduction 的 framing 是否恰当？是否有过度声称？\n\n4. **实用价值与受众匹配**：\n   - 对 NLP/CSS 社区的实际价值？practitioners 能否直接应用？\n   - EMNLP 受众是否是最佳匹配？（vs. 统计学/流行病学 venue）\n   - Algorithm 1（如有）的可用性和清晰度\n   - 代码公开承诺的可信度\n\n5. **格式合规性**：\n   - 正文是否 ≤ 8 页？\n   - 匿名性是否完整？（无 de-anonymizing 信息）\n   - 引用格式是否符合 ACL 要求？\n   - Limitations 是否覆盖关键限制？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（标注 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Detailed Comments → Scores（Soundness, Excitement, Reproducibility, Overall 各 1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_6/submitted.pdf`\n\n## Venue 要求\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（References 不限；Limitations 不计入页数）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者标注为 \"Anonymous\"）\n- **附录**: 允许，审稿人可选择性审查\n\n## 你的审查侧重\n\n**新颖性与完整性**——聚焦以下方面：\n\n1. **新颖性与贡献定位**：\n   - 三个贡献（bias taxonomy, correction guidance, ASV）相对于现有工作的增量价值？\n   - \"首次跨 7 种拓扑系统比较\"——这一声称是否准确？是否有先行工作被遗漏？\n   - ASV 相对于 E-value 的创新点是否清晰？是直接移植还是有实质性扩展？\n   - FWL invariance 作为\"negative result\"的价值——是否真的被 annotation correction 文献忽略？\n\n2. **Related Work 覆盖**：\n   - 测量误差文献（epidemiology + econometrics）的覆盖是否完整？\n   - LLM annotation 文献的覆盖是否及时（2024-2025 最新工作）？\n   - 是否有重要的缺失引用？特别关注：\n     - 非线性模型下的 misclassification 文献\n     - Multi-annotator / ensemble 校正方法\n     - Bayesian measurement error 最新进展\n\n3. **Presentation 质量**：\n   - 论文结构是否清晰？信息密度是否合适？\n   - 数学符号是否统一、定义是否清晰？\n   - 图表质量和信息传达效率\n   - Abstract/Introduction 的 framing 是否恰当？是否有过度声称？\n\n4. **实用价值与受众匹配**：\n   - 对 NLP/CSS 社区的实际价值？practitioners 能否直接应用？\n   - EMNLP 受众是否是最佳匹配？（vs. 统计学/流行病学 venue）\n   - Algorithm 1（如有）的可用性和清晰度\n   - 代码公开承诺的可信度\n\n5. **格式合规性**：\n   - 正文是否 ≤ 8 页？\n   - 匿名性是否完整？（无 de-anonymizing 信息）\n   - 引用格式是否符合 ACL 要求？\n   - Limitations 是否覆盖关键限制？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（标注 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Detailed Comments → Scores（Soundness, Excitement, Reproducibility, Overall 各 1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-22T17:40:35.336516+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2316
}
```

</details>

---


### Assistant

_source line 464 · 2026-05-22T17:40:51.940084+00:00_

**Round 6 审稿圆桌已启动。**

| 项目 | 状态 |
|------|------|
| **Venue** | EMNLP 2026（ARR，截止 2026-05-25） |
| **论文** | 正文 8 页，格式 ACL review，匿名 |
| **Reviewer 1** | 已分配——方法严谨性（证明、假设、实验方法论） |
| **Reviewer 2** | 已分配——新颖性/完整性（贡献定位、related work、presentation） |
| **视觉审查** | 已派发，后台运行中 |
| **外部审稿** | 未配置，跳过 |

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 465 · 2026-05-22T17:48:38.536906+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — 新颖性与完整性审查

### Paper: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 论文系统性地填补了多类别误分类在因果推断中跨拓扑传播的理论空白，贡献扎实但线性模型限制和部分理论结果仅限 K=3 削弱了其对 NLP 社区的直接适用性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 线性框架内的推导严谨，100K Monte Carlo 验证充分；但多项关键结果限于 K=3，K>3 仅有数值验证；非线性扩展仅附录 B.6 初步测试 |
| Excitement | 3.5/5 | 填补了多类别×多拓扑的真实空白，ASV 框架有实用价值；但线性限制降低了对 NLP practitioners 的直接兴奋度 |
| Reproducibility | 4/5 | DGP 参数完整、算法伪代码清晰、承诺公开代码；实际代码尚未可用 |
| Confidence | 4/5 | 我熟悉测量误差文献和因果推断方法论，仔细阅读了全文含附录 |

---

## Summary

本文研究 LLM 标注产生的多类别（K≥3）误分类如何在 7 种典型因果 DAG 拓扑下传播为下游因果估计偏差。主要贡献：(1) 推导了 7 种拓扑的偏差表达式，揭示二元情况下的"偏向零"保证在 K≥3 时失效且拓扑依赖；(2) 证明 FWL 不变性意味着矩阵校正在 4 种拓扑下无效；(3) 提出 Annotation Sensitivity Values (ASV) 框架量化误分类鲁棒性。论文进一步用真实 LLM 混淆矩阵（HumAID, VAST, CivilComments）进行经验验证。

---

## Strengths

**S1. 真正的理论空白填补。** 现有文献要么处理二元误分类（Brenner 1993; Ogburn & VanderWeele 2012），要么仅覆盖单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下系统比较 K≥3 误分类在 7 种 DAG 拓扑下的行为，核心发现——二元保证在多类别下结构性失效（sign reversal 在 85% 的 K=3 混淆矩阵中出现，Section 4.2）——是非平凡的且有实际意义。

**S2. FWL 不变性作为 negative result 的价值。** Section 4.5 和 Appendix B.2 证明 FWL 投影意味着线性校正在 mediation、collider、M-bias、front-door 四种拓扑下无效。这不是显而易见的结论，能直接帮助 practitioners 避免徒劳的校正尝试。

**S3. ASV 框架的实用性。** 三种互补的 ASV 类型（magnitude、significance、sign-flip）提供了从"多大误差可以容忍"到"何时符号翻转"的完整风险图谱。Algorithm 1（p.26）给出了可操作的拓扑→风险→校正方法选择流程，practitioners 可直接使用。

**S4. 验证的彻底性。** 理论结果经 100,000 个随机混淆矩阵（每个拓扑）验证（Appendix A.9, B.11），经验验证使用 3 个真实 NLP 任务的 LLM 混淆矩阵（23 种配置，Section 4.4），并包含 ClinicalBERT case study（Appendix B.3）。这远超"toy example"水平。

**S5. 时效性与受众匹配。** LLM 标注在 CSS 中的快速采用（Gilardi et al. 2023; Ziems et al. 2024）使得标注误差对因果推断的影响成为紧迫问题。EMNLP 受众中因果推断 + NLP 社区正在增长（Feder et al. 2022 综述），论文定位合适。

---

## Weaknesses

### CRITICAL

**W1. [CRITICAL] 线性模型假设严重限制 NLP 适用性**

- **位置**: Section 3.1 ("Let A denote a true K-class categorical variable... 设 structural equations 为线性"), Limitations (p.9)
- **问题**: 全部 bias 表达式（Section 3.2）、sign preservation 条件（Proposition 1-7）、FWL invariance（Section 4.5）均建立在线性结构方程假设上。然而 NLP/CSS 实践中，研究者几乎不使用线性模型——logistic regression 是最低门槛，更多使用 transformer-based models。Appendix B.6 仅测试了 logistic regression 下"sign-flip rate 为零"这一个声明（Table 7），且只在 exposure 拓扑下做了较完整测试，远未覆盖全部拓扑和偏差方向的结论。
- **影响**: 论文的核心叙事是"指导 NLP 社区在使用 LLM 标注做因果推断时的决策"，但理论工具仅在线性世界成立，造成了 framing 与 scope 的 mismatch。读者无法判断哪些定性结论（如拓扑排序 IV > exposure > front-door...）在非线性下仍然成立。
- **建议**: 至少应在 Appendix B.6 中扩展 logistic DGP 实验到全部 7 个拓扑，并报告 bias direction 和 magnitude 的对比（不仅 sign-flip rate）；在 Introduction 和 Conclusion 中更诚实地 scope 论文的适用范围。

### MAJOR

**W2. [MAJOR] 多项核心理论结果限于 K=3，K>3 一般性不足**

- **位置**: Proposition 1 sign preservation（"proven for K=2"）, Proposition 2-7 多处标注 "proven for K≤3, empirical for K>3", Conjecture 1 (collider/M-bias monotonicity, p.5, 仅数值验证), Table 2 (Appendix A.9, "Not guaranteed for K>3")
- **问题**: K=3 是论文的核心设定，但实际 NLP 任务经常有更多类别（sentiment 5 分、stance detection 4-6 类、NER 十数类）。Conjecture 1 在 Section 5 前以 "our theoretical results establish a three-tier hierarchy" 呈现，但 collider/M-bias 的 monotonicity 仅是 conjecture 而非 theorem。数值验证（10,000 random C_δ matrices，Appendix B.11）提供了证据但非证明。
- **影响**: 读者可能过度泛化 K=3 的结论到更高 K 值。论文在多处使用 "general K" 的语言但实际 guarantee 常限于 K≤3。
- **建议**: 在 Introduction 的 contribution 列表中明确标注每条贡献的 K 范围；Conjecture 1 应在正文（不只是附录注释）中注明其地位是 conjecture 而非 theorem。

**W3. [MAJOR] ASV 与 E-value 的创新边界不够清晰**

- **位置**: Section 3.3, Section 4.3
- **问题**: ASV 框架声称 "building on the E-value framework (VanderWeele and Ding, 2017) but with three key differences"（Section 3.3），然而这三个 difference 是：(1) 从 unmeasured confounding 映射到 misclassification severity——这是应用领域的变换而非方法论创新；(2) 三种 ASV 类型——magnitude 类比 E-value 的 RR 框架，significance 和 sign-flip 是自然延伸；(3) topology-dependent vulnerability spectrum——这本质上是应用 Section 3.2 的 bias 表达式。论文未充分讨论 ASV 与既有的 mediation sensitivity analysis（Imai et al. 2010）和 bias analysis for misclassification（Lash et al. 2009, Fox et al. 2005）的技术区别。
- **建议**: 用一个 Table 或 Figure 直接对比 ASV 与 E-value / mediation sensitivity analysis 的 input、output、assumptions，让读者清楚看到新增的技术内容。

**W4. [MAJOR] Related Work 遗漏重要文献**

- **位置**: Section 2
- **缺失引用**:
  1. **Shu & Yi (2019)** "Weighted causal inference methods with mismeasured covariates and misclassified outcomes" (*Statistics in Medicine*) — 直接处理误分类 outcome 对因果推断的影响，提出校正方法，与本文高度相关但未被引用。
  2. **Shu & Yi (2019)** "Causal inference with measurement error in outcomes" (*Statistical Methods in Medical Research*) — 提供了 outcome 测量误差下 ATE 的 bias 闭式分析，方法论上与本文的 bias taxonomy 相近。
  3. **预测驱动因果推断 (Prediction-Powered Causal Inference)**: Cadei et al. (2025) 将 PPI 框架扩展到因果推断场景，与本文 PPI++ 部分的讨论直接相关，但未被提及。
  4. **Dawid & Skene (1979) / Raykar et al. (2010)** — multi-annotator aggregation 文献作为替代于 confusion-matrix-based 校正的另一范式，至少值得在 Related Work 中提及。
- **影响**: 遗漏 Shu & Yi 的工作尤其显著，因为该系列论文直接在因果推断框架下研究误分类，是最直接的 prior work。

### MINOR

**W5. [MINOR] 非微分误分类假设在 NLP 场景下的脆弱性讨论不足**

- **位置**: Section 3.1 Definition 1, Limitations (p.9)
- **问题**: 非微分假设要求 P(A*|A,Y,Z) = P(A*|A)。论文承认 "which holds when the LLM does not observe Y"。但在许多 NLP pipeline 中，LLM 从同一文本中同时推断 treatment 和 outcome（例如同时标注 stance 和 sentiment），使得误分类可能与 outcome 相关。Appendix B.5 的 stress test（Table 7）仅测试了 exposure 拓扑在 differential departure ε ≤ 0.1 时的鲁棒性，未覆盖其他拓扑。
- **建议**: 在 Limitations 中加入一段具体讨论哪些 NLP 应用场景可能违反此假设，以及违反的后果方向。

**W6. [MINOR] 论文信息密度极高，部分表述可更精炼**

- **位置**: 全文
- **问题**: 8 页正文涵盖 7 种拓扑 × 3 种 ASV × 5 种校正方法 × 理论 + 模拟 + 经验验证，信息密度非常大。Section 3.2 连续给出 7 个拓扑的 bias 分析，每个仅 1-2 段，读者难以消化。Section 4.2-4.3 的多个发现压缩在较小空间内。
- **建议**: 考虑将部分次要拓扑（如 M-bias）的详细分析移入附录，在正文用 Table 汇总关键性质。

**W7. [MINOR] Conjecture 1 的数值验证范围**

- **位置**: Section 3.3, Appendix B.11
- **问题**: Conjecture 1（envelope monotonicity for collider/M-bias）通过 10,000 random C_δ matrices 数值验证。但 C_δ 的参数化（Dirichlet 扰动）可能未覆盖所有 corner case。Appendix B.11 报告 "violation counts are high (60-97% of matrix topologies)" 用语令人困惑——这里的 "violation" 似乎指的是 monotonicity 不严格而非 conjecture 被推翻，需要更清晰的表述。
- **建议**: 明确 Conjecture 1 验证中 "violation" 的定义，并讨论数值验证的边界——什么样的 C 结构可能推翻 conjecture。

---

## Questions for Authors

**Q1.** Appendix B.6 的 logistic regression 测试仅限于 sign-flip rate。你们是否有 bias magnitude 在非线性 DGP 下的完整拓扑比较数据？如果有，拓扑排序是否与线性情况一致？

**Q2.** ASV framework 的实际使用需要知道（或估计）confusion matrix C。在 Section 3.3 的 parameterization 中，C(δ) = (1−δ)I + δC_0，其中 C_0 来自 validation set。当 validation set 很小（如 <100 gold labels）时，C_0 的估计误差如何影响 ASV 的可靠性？

**Q3.** Algorithm 1 中 Step 1 的风险阈值（Magnitude ASV < 0.5, Significance ASV < 0.05 等）是如何确定的？是否有理论依据，还是经验选择？

**Q4.** 关于 "首次跨 7 种拓扑系统比较" 的声称：Hernán and Cole (2009) 已在测量误差框架下讨论了多种 DAG 结构的 bias。你们的工作与其核心区别是什么——仅是 K≥3 的扩展，还是有其他维度？

---

## Missing References

1. Shu, D. & Yi, G.Y. (2019). Weighted causal inference methods with mismeasured covariates and misclassified outcomes. *Statistics in Medicine*, 38(10), 1835-1854.
2. Shu, D. & Yi, G.Y. (2019). Causal inference with measurement error in outcomes: Bias analysis and estimation methods. *Statistical Methods in Medical Research*, 28(7), 2049-2068.
3. Cadei, R. et al. (2025). Prediction-Powered Causal Inferences. *arXiv:2502.06343*.
4. Dawid, A.P. & Skene, A.M. (1979). Maximum likelihood estimation of observer error-rates using the EM algorithm. *Journal of the Royal Statistical Society C*, 28(1), 20-28.（作为 multi-annotator 替代范式的经典参考）
5. Neuhaus, J.M. (1999). Bias and efficiency loss due to misclassified responses in binary regression. *Biometrika*, 86(4), 843-855.

---

## Detailed Comments

**D1.** Abstract 声称 "Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.4%"——这个数字来自 Section 4.2 的 confounding/M-bias 拓扑下的特定条件。但 IV 拓扑在同条件下有 52.6% sign reversal（Section 4.2 末段）。Abstract 应更 nuanced，明确这是哪些拓扑的结果。

**D2.** Figure 2（p.7）展示了 K=3 的 bias 分布，标题说 "Red = sign reversal. Exposure: 83.4% sign reversal; IV: 52.6%"。但图本身很小（半栏宽），6 个子图几乎无法辨认分布细节。建议放大或移至附录给一整页。

**D3.** Table 1（p.7）给出 7 种拓扑的 sign characteristics 汇总，但 "Amplif." 列的含义（amplification factor）在 Table caption 中未解释，需要翻到 Section 4.2 才能理解。Table 应自包含。

**D4.** Section 4.4 的 empirical validation（p.8）检查了 23 个 LLM 配置中 14 个展示 sign reversal "in at least one coefficient"。但未报告哪些拓扑对应哪些任务最脆弱。建议加入 topology × task 的交叉分析。

**D5.** Algorithm 1 的 Step 2（correction method selection）推荐 "PPI++ if gold labels available"，但 Section 4.5 显示 PPI++ 在 M-bias 下表现不佳（"harms M-bias (−88%)"）。Algorithm 1 应加入拓扑相关的 PPI++ 适用条件。

---

## 主要优势

1. 填补了 multi-class misclassification × DAG topology 交叉领域的真正理论空白
2. FWL invariance 作为 negative result 有独立价值
3. 验证规模（100K matrices + 3 真实 NLP 任务）远超同类工作
4. Algorithm 1 给出了从拓扑识别到校正方法选择的完整 actionable pipeline
5. 时效性好，回应了 LLM annotation 在 CSS 中快速扩散的真实需求

---

## 格式合规性

- **正文页数**: ≤ 8 页 ✓（Section 5 Conclusion 在第 8 页结束）
- **匿名性**: "Anonymous ACL submission" ✓；未发现 de-anonymizing 链接或信息
- **Limitations**: 第 9 页，覆盖了线性假设、非微分假设、K 限制、多分类器联合误差等关键限制 ✓
- **引用格式**: 符合 ACL style ✓
- **附录**: 存在（Appendix A-C, pp.11-26），审稿人可选择性审查 ✓


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 466 · 2026-05-22T17:48:55.196569+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 467 · 2026-05-22T17:48:57.879356+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 3.5/5（Borderline Conference）**
- **Soundness 3.5** / **Excitement 3.5** / **Reproducibility 4** / **Confidence 4**

**主要发现**：
- 1 个 CRITICAL 问题：线性模型假设与 NLP 实践的 mismatch，非线性验证严重不足
- 4 个 MAJOR 问题：K=3 理论局限性、ASV 与 E-value 创新边界模糊、Related Work 遗漏 Shu & Yi (2019) 等重要文献、Conjecture 1 未证明
- 3 个 MINOR 问题：非微分假设脆弱性讨论不足、信息密度过高、数值验证边界不清

**核心判断**：论文在线性框架内填补了 multi-class × multi-topology 的真正理论空白，验证规模扎实，Algorithm 1 有实用价值。但线性限制对 NLP 社区的适用性构成根本性问题，多项结果仅限 K=3 削弱了一般性声称。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-22T17:49:12.849798+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 48

## Round 48

6 recorded events


### User

_source line 469 · 2026-05-22T17:50:09.513623+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — 方法严谨性审查

### Paper Summary

本文研究 LLM 多类别（K≥3）标注误差如何沿因果 DAG 拓扑传播至下游因果估计。核心贡献：(1) 7 种典型 DAG 拓扑下非差异误分类的闭合偏差表达式；(2) 符号保持性保证（confounding/collider 解析证明，mediation/M-bias/front-door 数值验证）；(3) Envelope monotonicity 定理（K=2 严格证明）；(4) ASV 敏感性诊断框架；(5) FWL 不变性证明矩阵校正对 4 种拓扑无效；(6) 4 个 LLM × 3 个数据集的经验验证。

---

## 总体评分

**Overall**: 3.5/5（Borderline Conference）

**一句话总结**: 理论贡献扎实（K=2 证明、FWL 不变性、拓扑分类学），但 Theorem 1 对 K≥3 的证明缺口、abstract 中对 primary coefficient 的过度声称、以及 proportional effects 假设的讨论不足，使得当前版本在方法严谨性上存在可修补但不可忽视的问题。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 的证明路径（perspective function + convexity）严密且优雅；但 K≥3 部分仅靠数值验证支撑，Theorem 1 的形式化名称与证明完备性不匹配；abstract 中存在两处 overclaim |
| Excitement | 3.5/5 | LLM 标注 × 因果推断的交叉领域具有实际意义和及时性；ASV 框架有实用价值；但受众相对 niche，核心结果（线性 SEM + 非差异误分类）的适用范围有限 |
| Reproducibility | 4/5 | Monte Carlo 参数完整公开（N, K, Dirichlet prior）；Algorithm 1 可操作；承诺公开代码；LLM 实验使用公开模型和数据集 |
| Overall | 3.5/5 | Borderline Conference — 理论框架系统完整，但关键定理的证明完备性和 claim 的措辞准确性需要修订 |

---

## 主要优势

**S1. 重要且及时的问题定义**：LLM-as-annotator 在 NLP 中日益普及，但多类别标注误差对因果效应估计的系统性影响此前缺少理论刻画。本文填补了从 "标注质量" 到 "因果有效性" 的理论链条。

**S2. 全面的拓扑覆盖**：系统分析 7 种 DAG 拓扑而非仅限于 confounding，揭示偏差的 topology-dependent 性质是核心洞见。Table 1 的比较（如 bias 跨拓扑变化 4.1%–42.1%）直观有力。

**S3. 透明的理论层级**：proved → verified → conjectured 三层体系科学诚实。Proposition 1 对 confounding/collider 的解析证明（Appendix A.3, Cauchy-Schwarz）技术上正确。

**S4. FWL 不变性洞察**：证明矩阵校正对 4 种 A-enters-as-covariate 拓扑无效（col(D*·M) = col(D*) for invertible M）简洁、正确且对实践有非平凡指导意义。Appendix B.2 的证明干净。

**S5. 可操作的 ASV 框架**：将理论结果转化为 practitioners 可用的 sensitivity analysis 工具，Algorithm 1 的决策树结构清晰实用。

**S6. 扎实的经验验证**：4 LLM × 3 数据集 × zero/few-shot = 23 configurations 提供真实世界的 grounding；Monte Carlo 验证规模充分（100,000+ confusion matrices）。

---

## Must-Fix 问题（影响评分但不一票否决）

**M1** [MAJOR] Theorem 1 对 K≥3 未证明，但标记为 "Theorem"

- **具体位置**：Section 3.2 (page 5), Appendix A.4 (page 13-14)
- **问题**：Theorem 1 声称 |B(C(δ))| 在 δ∈[0,1] 上单调不减。对 K=2，证明通过 perspective function + convexity 完成，严格正确。但对 K≥3，论文承认 "worst-case deviations are < 0.003 across 20,000 random (C,p,q) triples"，证明依赖矩阵 M(C_p, C_q) 的负半定性，该条件被承认 "sufficient in practice but not universal"（Appendix A.4, Step 4）。
- **为什么影响评分**：在数学形式化中，"Theorem" 意味着完整证明。用数值验证支撑的 claim 应标记为 "Empirical Result" 或 "Conjecture"。尽管论文在定理陈述中透明地注明了 K≥3 的数值性质，但这在 *ACL 审稿中会引发 soundness 质疑。
- **建议修改方向**：将 Theorem 1 拆分为 (a) Theorem（K=2, exact proof）和 (b) Empirical Proposition 或 Conjecture（K≥3, numerical verification），或在定理陈述中使用 "For K=2, ... is proved; for K≥3, we verify numerically that..." 的显式分层措辞。

**M2** [MAJOR] Abstract 中 "primary coefficient never reverses" 被称为 "structural property"，但仅有经验支撑

- **具体位置**：Abstract (page 1), Footnote 2 (page 4)
- **问题**：Abstract 写道 "the primary treatment coefficient, however, is never reversed—a structural property we explain in Section 3." 但 Footnote 2 明确说这是经验发现："Empirically, the primary coefficient (largest |β_k|) never reverses across our 23 LLM configurations." Section 3 只提供了启发式解释（对角占优 + |β₁| 远大于其他系数），没有形式化条件或证明。
- **为什么影响评分**：在 abstract 中将经验规律称为 "structural property" 可能误导读者，使其认为存在理论保证。这尤其关键，因为 practitioners 可能基于此 claim 做出不检查 primary coefficient 的决定。
- **建议修改方向**：改为 "an empirical regularity we observe and explain heuristically in Section 3"，或提供 formal sufficient conditions（如 diagonal dominance threshold + coefficient magnitude ratio）。

**M3** [MAJOR] Proportional effects 假设 (f = λg) 在 Theorem 1 中是强限制，讨论不足

- **具体位置**：Theorem 1 (page 5), Appendix A.4 (page 13)
- **问题**：Theorem 1 要求 proportional effects（confounding function 与 treatment effect function 成标量倍数关系）。这意味着混杂路径和处理路径的效应结构高度平行，在实际因果推断中未必成立。Appendix A.4 的 "General case (non-proportional effects)" 部分仅提供数值验证（230,000 matrices, worst-case deviation 0.01），但主文未充分讨论何时此假设合理，何时不合理。
- **为什么影响评分**：如果 proportional effects 在实际 LLM 标注场景中不普遍成立，Theorem 1 的实用性会显著降低。读者需要知道这个假设的实际含义和限制。
- **建议修改方向**：在 Section 3.2 主文中增加 1-2 句解释 proportional effects 对应什么现实场景，以及违反时 monotonicity 的近似程度（可引用 Appendix A.4 的 0.01 deviation 结果）。

**M4** [MAJOR] Abstract 中 "1.4%" sign reversal rate 与 Section 4.2 的 "2.1%" 数值不一致

- **具体位置**：Abstract (page 1), Section 4.2 (page 6)
- **问题**：Abstract 称 "Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.4%"，但 Section 4.2 在相同条件（diagonal ≥ 0.7）下报告 "2.1% sign reversal"。如果两个数字来自不同分析（Monte Carlo vs. empirical），abstract 应明确数据来源。如果同一分析产出不同数字，其中一个有误。
- **为什么影响评分**：Abstract 中的核心定量 claim 与正文不一致会削弱整体可信度。
- **建议修改方向**：统一数字来源并在 abstract 中注明分析基础（Monte Carlo / empirical / per-coefficient vs. per-configuration）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Sign preservation conditions（Proposition 1a）涉及不可观测的 population quantities

- **具体位置**：Section 3.2 (page 4), Proposition 1(a)
- **问题**：Confounding 的符号保持条件 sign(τ_obs) = sign(τ·B_{PV}) 涉及真实 A（非 A*）的总体协方差结构。实践者只能观测到 A*，因此条件无法直接验证。虽然 ASV framework（Section 3.3）提供了实用替代，但理论条件与实践可操作性之间的鸿沟应更明确地说明。
- **建议**：在 Proposition 1 后加一句提示此条件在实践中如何 approximate（指向 ASV section）。

**W2** [warning] Dirichlet(1,1) prior 在 Monte Carlo 中可能不反映真实 LLM 误差模式

- **具体位置**：Section 4.1 (page 6), Table 1
- **问题**：Dirichlet(1,...,1) 是 simplex 上的均匀分布，会生成大量极端 confusion matrices（对角线接近 0 或 1），不太反映真实 LLM 分类器的误差分布（通常对角占优且误差集中在语义相近类别）。Table 1 报告的 violation rates 可能因此偏高。
- **建议**：注明 Dirichlet prior 的选择理由，或补充以 concentrated Dirichlet（如 α>1）为先验的 robustness check。

**W3** [warning] Conjecture 1 与 Theorem 1 的覆盖范围关系不清晰

- **具体位置**：Section 3.2 (page 5)
- **问题**：Theorem 1 覆盖 confounding 和 mediation（under proportional effects），Conjecture 1 覆盖 "non-IV topologies"（包括 collider、M-bias 等）。两者之间是否有重叠（confounding/mediation 在 Conjecture 1 的 scope 内吗）？ε-approximate monotonicity 与 exact monotonicity 的关系是什么？
- **建议**：明确说明两个 claim 的非重叠性，或解释为什么 Conjecture 1 对 confounding/mediation 给出更宽松的 bound。

**W4** [warning] ASV 与 E-value 的方法论创新差异化不足

- **具体位置**：Section 3.3 (page 5)
- **问题**：ASV 明确借鉴 E-value framework（VanderWeele and Ding, 2017），但论文未充分说明 ASV 在方法论上超越 "E-value adapted for misclassification" 的创新点。三种 ASV 类型（magnitude, significance, sign-flip）是 E-value 的直接变体还是有独立贡献？
- **建议**：在 Section 3.3 中增加一段明确 ASV 相对 E-value 的 novelty。

---

## 小问题（不影响接收）

- Eq.(2) 中 weights w_{jk} 的完整公式被推迟到附录，主文中读者无法独立理解偏差结构的具体形式。建议在主文给出简化形式或直觉。
- Figure 1 的 7 个 DAG 拓扑在印刷尺寸下较难区分，特别是 M-bias 和 front-door 的边结构。
- Appendix B.6 对 nonlinear DGP 的 robustness check 仅用了 logistic regression 一种非线性形式。如果可能，增加一种（如 probit 或 polynomial）会增强说服力。
- Limitations 部分未提及 ASV 计算在 K 很大时的计算成本。

---

## Questions for Authors

**Q1.** 是否存在 formal sufficient conditions 保证 primary coefficient 不反转？例如，是否可以证明当 C 满足某个 diagonal dominance threshold 且 |β₁|/|β₂| > 某个比值时，β̂₁ 符号必然保持？

**Q2.** Proportional effects 假设 f = λg 在 confounding topology 下对应什么具体的结构方程类？能否给出一个自然语言场景说明何时此假设成立/不成立？

**Q3.** Abstract 中 1.4% sign reversal rate 的精确定义和计算基础是什么（分母是 per-coefficient/per-configuration/per-topology）？与 Section 4.2 的 2.1% 有何关系？

**Q4.** ASV 相对于 E-value 在方法论上的独立贡献是什么？三种 ASV 类型中是否有不能从 E-value 直接类比得到的？

**Q5.** 对于 FWL 不变性使矩阵校正失效的 4 种拓扑，除了 "使用 PPI++ + gold labels" 之外，是否有其他实用的校正策略可以推荐给没有 gold-labeled data 的 practitioners？

---

## Missing References

未发现关键遗漏。Related work 覆盖了因果推断中测量误差的核心文献（Carroll et al., 2006; Gustafson, 2004; Pearl, 2009; VanderWeele and Ding, 2017）和近期 LLM 标注文献。

可选补充：如果 Feder et al. (2022) "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond"（Transactions of ACL）与已引用的 Feder et al. (2024) 不是同一篇，可考虑增加以强化 NLP×因果推断的文献覆盖。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-22T17:50:53.717128+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应，对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供具体证据，cite Section/Table/Figure）。\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**M1 [MAJOR] Theorem 1 对 K≥3 未证明，但标记为 \"Theorem\"**\nTheorem 1 声称 |B(C(δ))| 在 δ∈[0,1] 上单调不减。K=2 通过 perspective function + convexity 严格证明，但 K≥3 仅有数值验证（20,000 random triples, worst-case deviation < 0.005）。建议拆分为 Theorem（K=2）+ Empirical Proposition/Conjecture（K≥3）。\n\n**M2 [MAJOR] Abstract 中 \"primary coefficient never reverses\" 被称为 \"structural property\"，但仅有经验支撑**\nAbstract: \"the primary treatment coefficient, however, is never reversed—a structural property we explain in Section 3.\" 但 Footnote 2 明确说是经验发现（23 LLM configurations），Section 3 只提供启发式解释（magnitude dominance），无 formal proof。建议改为 \"empirical regularity\" 或给出 formal sufficient conditions。\n\n**M3 [MAJOR] Proportional effects 假设 (f = λg) 在 Theorem 1 中是强限制，讨论不足**\n该假设要求混杂路径和处理路径效应结构成标量倍数。实际中未必成立。主文未充分解释何时此假设合理，非比例情形下 monotonicity 的近似程度如何。\n\n**M4 [MAJOR] Abstract 中 \"1.4%\" sign reversal rate 与 Section 4.2 的 \"2.1%\" 不一致**\nAbstract: \"sign reversal rate is 1.4%\"；Section 4.2: \"2.1% sign reversal\"（条件相同：diagonal ≥ 0.7）。如果来自不同分析，应明确。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1** Sign preservation conditions（Proposition 1a）涉及不可观测的 population quantities，实践者无法直接验证。\n**W2** Dirichlet(1,1) prior 生成大量极端 confusion matrices，可能不反映真实 LLM 误差分布，violation rates 可能偏高。\n**W3** Conjecture 1 与 Theorem 1 的覆盖范围关系不清晰——是否重叠？ε-approximate 与 exact monotonicity 的关系？\n**W4** ASV 与 E-value 的方法论差异化不足。\n\n### Reviewer 1 的评分\nSoundness 3.5 / Excitement 3.5 / Reproducibility 4 / Overall 3.5\n\n---\n\n请对每个问题给出 [AGREE] 或 [REBUT] 回应，并说明理由。如果你发现 Reviewer 1 的某个 concern 你在自己的审稿中遗漏了，也请指出。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应，对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供具体证据，cite Section/Table/Figure）。\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**M1 [MAJOR] Theorem 1 对 K≥3 未证明，但标记为 \"Theorem\"**\nTheorem 1 声称 |B(C(δ))| 在 δ∈[0,1] 上单调不减。K=2 通过 perspective function + convexity 严格证明，但 K≥3 仅有数值验证（20,000 random triples, worst-case deviation < 0.005）。建议拆分为 Theorem（K=2）+ Empirical Proposition/Conjecture（K≥3）。\n\n**M2 [MAJOR] Abstract 中 \"primary coefficient never reverses\" 被称为 \"structural property\"，但仅有经验支撑**\nAbstract: \"the primary treatment coefficient, however, is never reversed—a structural property we explain in Section 3.\" 但 Footnote 2 明确说是经验发现（23 LLM configurations），Section 3 只提供启发式解释（magnitude dominance），无 formal proof。建议改为 \"empirical regularity\" 或给出 formal sufficient conditions。\n\n**M3 [MAJOR] Proportional effects 假设 (f = λg) 在 Theorem 1 中是强限制，讨论不足**\n该假设要求混杂路径和处理路径效应结构成标量倍数。实际中未必成立。主文未充分解释何时此假设合理，非比例情形下 monotonicity 的近似程度如何。\n\n**M4 [MAJOR] Abstract 中 \"1.4%\" sign reversal rate 与 Section 4.2 的 \"2.1%\" 不一致**\nAbstract: \"sign reversal rate is 1.4%\"；Section 4.2: \"2.1% sign reversal\"（条件相同：diagonal ≥ 0.7）。如果来自不同分析，应明确。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1** Sign preservation conditions（Proposition 1a）涉及不可观测的 population quantities，实践者无法直接验证。\n**W2** Dirichlet(1,1) prior 生成大量极端 confusion matrices，可能不反映真实 LLM 误差分布，violation rates 可能偏高。\n**W3** Conjecture 1 与 Theorem 1 的覆盖范围关系不清晰——是否重叠？ε-approximate 与 exact monotonicity 的关系？\n**W4** ASV 与 E-value 的方法论差异化不足。\n\n### Reviewer 1 的评分\nSoundness 3.5 / Excitement 3.5 / Reproducibility 4 / Overall 3.5\n\n---\n\n请对每个问题给出 [AGREE] 或 [REBUT] 回应，并说明理由。如果你发现 Reviewer 1 的某个 concern 你在自己的审稿中遗漏了，也请指出。"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-22T17:51:13.830673+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20113
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-22T17:51:15.147999+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应，对每个 CRITICAL/MAJOR/MINOR 问题标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供具体证据，cite Section/Table/Figure）。\n\n---\n\n### Reviewer 2 的 CRITICAL 问题\n\n**W1 [CRITICAL] 线性模型假设严重限制 NLP 适用性**\n全部 bias 表达式、sign preservation、FWL invariance 均建立在线性 SEM 上。NLP/CSS 实践中几乎不用线性模型（logistic 是最低门槛）。Appendix B.6 仅在 exposure 拓扑下测试了 logistic regression 的 sign-flip rate，远未覆盖全部拓扑和偏差方向。论文 framing 是\"指导 NLP 社区\"，但工具仅在线性世界成立，存在 scope mismatch。\n\n### Reviewer 2 的 MAJOR 问题\n\n**W2 [MAJOR] 多项核心理论结果限于 K=3，K>3 一般性不足**\nProposition 1-7 多处标注 \"proven for K≤3, empirical for K>3\"。K=3 是核心设定但 NLP 任务常有更多类别（sentiment 5 分、stance 4-6 类、NER 十数类）。Conjecture 1 仅是 conjecture 但 Section 5 前以 \"our theoretical results establish a three-tier hierarchy\" 呈现。\n\n**W3 [MAJOR] ASV 与 E-value 的创新边界不够清晰**\n三个 claimed differences 可能仅是应用领域变换和自然延伸，而非方法论创新。未充分对比 mediation sensitivity analysis (Imai et al. 2010) 和 QBA framework (Lash et al. 2009)。\n\n**W4 [MAJOR] Related Work 遗漏重要文献**\n缺失：Shu & Yi (2019) 两篇（误分类下的加权因果推断和 outcome 测量误差的 ATE bias 分析）、Cadei et al. (2025) PPI 因果推断扩展、Dawid & Skene (1979) multi-annotator 范式、Neuhaus (1999) binary regression misclassification。\n\n### Reviewer 2 的 MINOR 问题\n\n**W5** 非微分假设在 NLP 场景下的脆弱性讨论不足（stress test 仅覆盖 exposure 拓扑）。\n**W6** 信息密度过高，Section 3.2 连续 7 个拓扑各仅 1-2 段，读者难以消化。\n**W7** Conjecture 1 验证中 \"violation\" 定义不清晰。\n\n### Reviewer 2 的 Detailed Comments\n\n**D1** Abstract \"1.4%\" 与实际报告数字不一致（Section 4.2 报告 2.1%），可能误导。\n**D2** Figure 2 子图过小，分布细节难辨。\n**D3** Table 1 \"Amplif.\" 列含义在 caption 中未解释。\n**D4** Section 4.4 未报告 topology × task 的交叉分析。\n**D5** Algorithm 1 未加入 PPI++ 对 M-bias 有害的条件限制。\n\n### Reviewer 2 的评分\nSoundness 3.5 / Excitement 3.5 / Reproducibility 4 / Overall 3.5\n\n---\n\n请对每个问题给出 [AGREE] 或 [REBUT] 回应，并说明理由。如果你发现 Reviewer 2 的某个 concern 你在自己的审稿中遗漏了，也请指出。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应，对每个 CRITICAL/MAJOR/MINOR 问题标注 [AGREE]（同意并说明理由）或 [REBUT]（反驳并提供具体证据，cite Section/Table/Figure）。\n\n---\n\n### Reviewer 2 的 CRITICAL 问题\n\n**W1 [CRITICAL] 线性模型假设严重限制 NLP 适用性**\n全部 bias 表达式、sign preservation、FWL invariance 均建立在线性 SEM 上。NLP/CSS 实践中几乎不用线性模型（logistic 是最低门槛）。Appendix B.6 仅在 exposure 拓扑下测试了 logistic regression 的 sign-flip rate，远未覆盖全部拓扑和偏差方向。论文 framing 是\"指导 NLP 社区\"，但工具仅在线性世界成立，存在 scope mismatch。\n\n### Reviewer 2 的 MAJOR 问题\n\n**W2 [MAJOR] 多项核心理论结果限于 K=3，K>3 一般性不足**\nProposition 1-7 多处标注 \"proven for K≤3, empirical for K>3\"。K=3 是核心设定但 NLP 任务常有更多类别（sentiment 5 分、stance 4-6 类、NER 十数类）。Conjecture 1 仅是 conjecture 但 Section 5 前以 \"our theoretical results establish a three-tier hierarchy\" 呈现。\n\n**W3 [MAJOR] ASV 与 E-value 的创新边界不够清晰**\n三个 claimed differences 可能仅是应用领域变换和自然延伸，而非方法论创新。未充分对比 mediation sensitivity analysis (Imai et al. 2010) 和 QBA framework (Lash et al. 2009)。\n\n**W4 [MAJOR] Related Work 遗漏重要文献**\n缺失：Shu & Yi (2019) 两篇（误分类下的加权因果推断和 outcome 测量误差的 ATE bias 分析）、Cadei et al. (2025) PPI 因果推断扩展、Dawid & Skene (1979) multi-annotator 范式、Neuhaus (1999) binary regression misclassification。\n\n### Reviewer 2 的 MINOR 问题\n\n**W5** 非微分假设在 NLP 场景下的脆弱性讨论不足（stress test 仅覆盖 exposure 拓扑）。\n**W6** 信息密度过高，Section 3.2 连续 7 个拓扑各仅 1-2 段，读者难以消化。\n**W7** Conjecture 1 验证中 \"violation\" 定义不清晰。\n\n### Reviewer 2 的 Detailed Comments\n\n**D1** Abstract \"1.4%\" 与实际报告数字不一致（Section 4.2 报告 2.1%），可能误导。\n**D2** Figure 2 子图过小，分布细节难辨。\n**D3** Table 1 \"Amplif.\" 列含义在 caption 中未解释。\n**D4** Section 4.4 未报告 topology × task 的交叉分析。\n**D5** Algorithm 1 未加入 PPI++ 对 M-bias 有害的条件限制。\n\n### Reviewer 2 的评分\nSoundness 3.5 / Excitement 3.5 / Reproducibility 4 / Overall 3.5\n\n---\n\n请对每个问题给出 [AGREE] 或 [REBUT] 回应，并说明理由。如果你发现 Reviewer 2 的某个 concern 你在自己的审稿中遗漏了，也请指出。"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-22T17:51:17.416053+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2268
}
```

</details>

---


### Assistant

_source line 474 · 2026-05-22T17:51:20.804991+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 475 · 2026-05-22T17:51:23.560598+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**Overall 3.5/5（Borderline Conference）**。

4 个 MAJOR 问题：
1. **Theorem 1 K≥3 证明缺口** — 数值验证支撑的 claim 标记为 "Theorem" 不妥，应拆分或显式分层
2. **Abstract overclaim** — "primary coefficient never reverses" 被称为 "structural property"，实际仅有经验支撑
3. **Proportional effects 假设讨论不足** — Theorem 1 依赖 f=λg，但主文未说明何时此假设合理
4. **数值不一致** — Abstract 报告 1.4% sign reversal rate vs. Section 4.2 的 2.1%

主要优势：问题定义重要及时、7 拓扑系统覆盖、FWL 不变性洞察干净有力、ASV 框架实用。所有问题均可在 revision 中修补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 476 · 2026-05-22T17:51:37.282104+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 477 · 2026-05-22T17:53:00.143029+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉回应 — 逐条评议 Reviewer 1 意见

---

### Must-Fix 问题

**[AGREE] R1-M1: Theorem 1 对 K≥3 未证明但标记为 "Theorem"**

同意这是一个合理的严谨性关切。从我阅读 Appendix A.4 的情况看，K=2 的证明通过 perspective function 的 convexity 完成，逻辑清晰完整。但 K≥3 的"证明"实质上是数值验证——20,000 random triples 的 worst-case deviation < 0.005。这在数学上不构成 proof。

我在自己的审稿中将此问题归入 W2（K=3 限制），但 R1 的指出更精确：问题不仅是 K>3 的一般性，而是 **Theorem 的命名本身不严谨**。建议拆分为 Theorem 1（K=2, proved）+ Proposition 1'（K≥3, numerically verified）是合理的处理方式。

补充一点：Conjecture 1（Section 3.3, collider/M-bias monotonicity）的命名反而是正确的——作者对此诚实地使用了 "conjecture" 而非 "theorem"。这种不一致性（同类结论在 confounding 称 theorem、在 collider 称 conjecture）更凸显了命名问题。

---

**[AGREE] R1-M2: "primary coefficient never reverses" 被称为 "structural property" 但仅有经验支撑**

同意。我重新检查了 Abstract（p.1）和 Section 3（特别是 Footnote 2）。Abstract 明确说 "a structural property we explain in Section 3"，但 Section 3 的解释是基于 magnitude dominance 的启发式论证（对角项 C_kk 对 plim 的主导贡献），加上 Footnote 2 承认这是 23 个 LLM 配置下的经验观察。

"Structural property" 在学术语境中暗示 mathematical guarantee，而实际支撑仅为 heuristic explanation + empirical regularity。改为 "empirical regularity" 或 "robust empirical pattern" 更准确。或者，如果作者能给出 formal sufficient conditions（例如对角占优度的某个阈值），可以保留更强的措辞。

这个问题我在自己的审稿中未明确指出，R1 的发现有价值。

---

**[AGREE with nuance] R1-M3: Proportional effects 假设 (f = λg) 讨论不足**

同意这是一个值得讨论的假设，但我认为其严重程度介于 MAJOR 和 MINOR 之间，可能更适合归为 Should-Fix 而非 Must-Fix。理由如下：

1. **R1 的关切是合理的**：f = λg 要求混杂路径效应与处理路径效应成比例，这在实际 DGP 中未必成立。论文确实未在主文中充分讨论此假设何时合理。

2. **但论文有部分对冲**：Appendix A.4 在 proportional case 之外还提供了 "general case (non-proportional effects)" 的讨论（我在 p.13-14 看到了 B(δ) 的 general 分析和数值验证），显示即使非比例情形下 monotonicity 也近似成立（worst-case deviation from monotonic bound < 0.005 across 230,000 random C matrices, K ∈ {3,5,7}）。

3. **建议**：在 Section 3.3 或 Appendix A.4 增加 1-2 段明确讨论 (a) f = λg 在什么实际场景下近似成立，(b) 非比例情形的 worst-case 偏离幅度，(c) 何时 practitioners 应特别警惕。这比降级为 conjecture 更有建设性。

这个假设问题我在自己审稿中遗漏了，R1 的指出有贡献。

---

**[AGREE] R1-M4: Abstract "1.4%" 与 Section 4.2 "2.1%" 数值不一致**

这是一个事实性错误，无论原因如何都必须修正。

我重新查看了相关段落：
- Abstract (p.1): "Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.4%, exclusively in secondary coefficients"
- Section 4.2 (p.6): 提到 "2.1% sign reversal" 相关数据

可能的解释：两个数字可能来自不同的拓扑子集或不同的 averaging 方式（across topologies vs. specific topology）。但 Abstract 未做任何限定，读者自然会认为 1.4% 是全局数字。如果 Section 4.2 在相同条件下报告 2.1%，这构成直接矛盾。

**这个数值不一致我在自己审稿中未发现，是 R1 的重要贡献。** 我在 D1 中指出了 Abstract 1.4% 来源不透明的问题（指出 IV 拓扑有 52.6%），但未注意到与 Section 4.2 的具体矛盾。

---

### Should-Fix 问题

**[AGREE] R1-W1: Sign preservation conditions 涉及不可观测量**

同意。Proposition 1(a) 的 sign preservation condition 需要知道 sign(τ_total) 等 population quantities，但 practitioners 在应用误分类校正时恰恰不知道真实值——这就是为什么需要校正的原因。这形成了一种 circularity。

不过，我认为 ASV 框架（Section 3.3）在一定程度上缓解了此问题：ASV 提供的是 "多大的误分类才会改变结论" 的 sensitivity analysis，不要求精确知道 population quantities。论文可以在讨论 sign preservation 条件时更明确地指向 ASV 作为实用替代："当条件无法直接验证时，practitioners 应使用 ASV 评估脆弱性。"

---

**[AGREE] R1-W2: Dirichlet(1,1) prior 生成极端矩阵**

同意 Dirichlet(1,1,...) 生成的 uniform simplex 分布会产生大量对角线很低的极端混淆矩阵，inflate unconditional violation rates。不过论文在 Section 4.2 确实区分了 unconditional 和 conditional (diagonal ≥ 0.7) 结果。

我在自己的审稿中未将此作为独立问题提出，但 R1 的关切合理。建议作者在 Section 4.1 中增加一句说明 Dirichlet(1,1) 的选择理由（coverage of the full parameter space for theoretical verification）以及其在 "realistic" 条件下的含义。

---

**[AGREE] R1-W3: Conjecture 1 与 Theorem 1 的覆盖范围关系**

同意这需要澄清。Theorem 1 覆盖 confounding 和 mediation 拓扑的 envelope monotonicity；Conjecture 1 覆盖 collider 和 M-bias。但论文未明确说：
- 两者覆盖的拓扑是否互斥（是的，根据我的理解）
- Exposure、front-door、IV 的 monotonicity 状态（Table 3 / Appendix B.9 似乎有涉及）
- ε-approximate monotonicity（Conjecture 1 的 "non-increasing" 表述）与 Theorem 1 的 strict monotonicity 在数学上的关系

建议作者在 Section 3.3 末尾加一个 1-2 句的汇总，明确每个拓扑的 monotonicity 状态和证明级别。

---

**[AGREE] R1-W4: ASV 与 E-value 方法论差异化不足**

完全同意——这与我审稿中的 W3 一致。两位 reviewer 独立指出同一问题，说明这是读者共识性困惑。论文需要更清晰地 delineate ASV 的 technical novelty vs. E-value 的 conceptual mapping。

---

### 总结

R1 的审稿质量很高，聚焦方法严谨性的角度与我的新颖性/完整性角度互补。

**R1 发现了我遗漏的问题：**
- M3（proportional effects 假设讨论不足）——我未注意到 f = λg 假设的隐含强度
- M4（1.4% vs 2.1% 数值不一致）——我注意到 Abstract 数字的来源不透明（D1），但未发现与 Section 4.2 的具体矛盾

**我的审稿中 R1 未覆盖的问题：**
- W1（线性假设 vs. NLP 适用性的 mismatch）——R1 未将此列为 concern
- W4（Missing references: Shu & Yi 2019, Cadei et al. 2025 等）——R1 未讨论 related work 完整性
- D5（Algorithm 1 中 PPI++ 对 M-bias 的不适用性未反映）——R1 未涉及校正方法的拓扑适用性

**评分对齐：** R1 给出 Overall 3.5，与我的 3.5 完全一致。两位 reviewer 独立得出相同评分，增强了 Borderline Conference 判断的可信度。核心共识是：理论贡献扎实但有范围限制（K、线性），需要更诚实的 scoping 和几处关键修正。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 478 · 2026-05-22T17:53:15.266610+00:00_

Reviewer 2 对 Reviewer 1 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 479 · 2026-05-22T17:53:17.951606+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。要点总结：

- 对 R1 的 4 个 Must-Fix 全部 **[AGREE]**，其中 M3（proportional effects）认为严重程度可降为 Should-Fix，M4（数值不一致）是我遗漏的重要发现
- 对 R1 的 4 个 Should-Fix 全部 **[AGREE]**，W4（ASV vs E-value）与我的 W3 独立一致
- 指出了我审稿中 R1 未覆盖的问题：线性假设 vs NLP 适用性、缺失引用（Shu & Yi 2019 等）、Algorithm 1 的拓扑适用性缺陷
- 两位 reviewer 独立给出相同评分（Overall 3.5），核心共识：贡献扎实但 scoping 需要更诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 480 · 2026-05-22T17:53:32.265880+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 52

## Round 52

8 recorded events


### User

_source line 481 · 2026-05-22T17:53:40.586105+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### CRITICAL 问题

**[REBUT] R2-W1: 线性模型假设严重限制 NLP 适用性**

R2 的核心论点成立——线性 SEM 确实限制了理论结果的直接适用范围，我在自己的审稿中也将此列为 minor issue（m2）。但我反对将其定为 **CRITICAL**，理由有三：

1. **R2 存在事实性错误**：R2 称 "Appendix B.6 仅在 exposure 拓扑下测试了 logistic regression"，这不准确。Appendix B.6（page 22-23）明确写道 "We replace the linear structural equations with Y ~ Bernoulli(σ(x'β)) and estimate via logistic regression (control function for IV) **for all seven topologies**, using K=3, six real VAST confusion matrices, 500 MC replications, and N=10,000." Table 8（page 23）报告了全部 7 种拓扑的 sign-flip rates 和 DGP 配置结果。B.6 的覆盖面远超 R2 所述。

2. **CSS/NLP 因果推断实践中线性模型仍广泛使用**：线性回归（OLS with controls）在社会科学因果推断中是标准方法之一（Angrist & Pischke, 2009）。论文定位于因果效应估计而非预测，线性模型在此场景下并非边缘选择。

3. **理论先行、扩展跟进是正常研究路径**：测量误差理论的经典文献（Carroll et al., 2006; Gustafson, 2004; Brenner, 1993）同样从线性模型出发。论文在 Limitations 中明确承认了这一限制，并在 B.6 提供了非线性 robustness check。

**建议评级**：MAJOR（不是 CRITICAL）。线性假设是真实限制，但论文的理论贡献在线性框架内是完整的，B.6 提供了非线性方向的初步验证。

---

### MAJOR 问题

**[AGREE] R2-W2: K>3 一般性不足**

同意这是重要问题，与我的 M1（Theorem 1 K≥3 证明缺口）一致。NLP 任务中 K>3 很常见（sentiment 5 分、NER 多类），仅靠数值验证支撑的理论 claim 需要更谨慎的措辞。

但需要**修正 R2 的部分表述**：R2 说 "Proposition 1-7 多处标注 proven for K≤3, empirical for K>3"，这不完全准确。Proposition 1（sign preservation for confounding/collider）的解析证明是 **general K** 的——Appendix A.3 的 Cauchy-Schwarz 论证不依赖 K 的具体值，条件仅要求 C_{kk} > 0 for all k。K 限制主要集中在 Theorem 1（envelope monotonicity, K=2 exact）和 Conjecture 1（numerical for K∈{3,5,7}）。论文的三层体系中，第一层（proved）是 general K 的。

**[AGREE] R2-W3: ASV 与 E-value 的创新边界不够清晰**

完全同意，与我的 W4 一致。论文应更明确地阐述 ASV 相对 E-value 的方法论增量。R2 补充提到的 mediation sensitivity analysis (Imai et al., 2010) 和 QBA framework (Lash et al., 2009) 也是有价值的对比对象——特别是 QBA framework，它同样处理 misclassification bias 的 sensitivity analysis，与 ASV 有直接可比性。这些对比能帮助读者理解 ASV 的独特贡献。

**[REBUT] R2-W4: Related Work 遗漏重要文献（部分反驳）**

R2 列出 5 篇缺失引用，我逐一评估：

- **Shu & Yi (2019) 两篇（误分类下加权因果推断 / outcome 测量误差的 ATE bias）**：[AGREE] 这两篇确实与本文直接相关（多类别误分类 × 因果推断），应当引用。
- **Cadei et al. (2025) PPI 因果推断扩展**：[AGREE] 论文已引用 Angelopoulos et al. (2023) 的 PPI++，但如果 Cadei et al. (2025) 将 PPI 扩展到因果推断设定，属于直接竞争/互补工作，应当引用。
- **Dawid & Skene (1979) multi-annotator 范式**：[REBUT] 这是 multi-annotator agreement 的经典文献，但本文聚焦于单一 annotator（LLM）的 misclassification matrix，不涉及 inter-annotator disagreement 的建模。引用它会是 nice-to-have 但非遗漏。
- **Neuhaus (1999) binary regression misclassification**：[AGREE] 与 Brenner (1993) 互补，本文已引 Brenner 但 Neuhaus 提供了 binary regression 视角，值得补充。

总结：5 篇中 3-4 篇确实应引用，但我不认为这构成 MAJOR 问题。Related Work 的核心覆盖（Carroll et al., Gustafson, Pearl, VanderWeele & Ding, Edwards et al., Lee & Wood-Doughty）已经比较完整。建议降为 **MINOR/should-fix**。

---

### MINOR 问题

**[AGREE] R2-W5: 非微分假设 stress test 仅覆盖 exposure 拓扑**

同意。Appendix B.5（page 22）的 stress test 确实仅在 exposure topology 上进行。虽然 exposure 是最脆弱的拓扑（sign reversal 最严重），但 practitioners 需要知道其他拓扑（特别是 confounding 和 mediation）在非微分条件下的行为。这是我自己审稿中遗漏的一个合理关注点。

**[REBUT] R2-W6: Section 3.2 信息密度过高**

不同意这是问题。Section 3.2 的 7 个拓扑按统一结构呈现（bias expression → sign behavior → key insight），模式一致后读者可以快速扫描。在 8 页限制下，这是系统覆盖与可读性之间的合理权衡。详细推导已在 Appendix A.3-A.8 展开。如果为了"可读性"而砍掉部分拓扑，反而会削弱论文的核心贡献（全面的拓扑分类学）。

**[AGREE] R2-W7: Conjecture 1 验证中 "violation" 定义不清晰**

同意主文中应更明确。Appendix B.11（page 24）定义了 violation 为 "matrices with at least one non-monotone step exceeding tolerance 10^{-12}"，但主文 Section 3.2（page 5）仅说 "worst-case V_p increases"，缺少可操作的定义。建议在主文加一句脚注。

---

### Detailed Comments

**[AGREE] R2-D1: Abstract "1.4%" 与 Section 4.2 "2.1%" 不一致**

完全同意，这与我的 M4 一致。两位 reviewer 独立发现同一问题，进一步说明这个数值不一致需要修正。

**[AGREE] R2-D2: Figure 2 子图过小**

同意，分布细节在当前尺寸下确实难辨。

**[AGREE] R2-D3: Table 1 "Amplif." 列含义未解释**

同意。Table 1 caption 应明确 "Amplif." = amplification（|bias| > |true effect|，即偏差放大了真实效应）。

**[AGREE] R2-D4: Section 4.4 未报告 topology × task 交叉分析**

部分同意。Figure 3 提供了部分交叉信息（topology vs. bias magnitude for HumAID），但缺少跨数据集的 topology × task 完整表格。考虑到篇幅限制，可放在附录。

**[AGREE] R2-D5: Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用**

同意。Algorithm 1（page 26）在 Step 2 中通过 topology-specific 的方法选择隐式避免了 PPI++ 用于 M-bias（选择 MC-SIMEX），但代码逻辑中没有显式的 "if M-bias: exclude PPI++" 条件。考虑到 Section 4.5 明确报告 PPI++ 对 M-bias harmful (−88%)，Algorithm 1 应加入此 guard。

---

### 我自己审稿中遗漏的问题

R2 提出了两个我未充分关注的有效问题：

1. **W5（stress test 覆盖范围）**：我虽然在 W2 中提到了 Dirichlet prior 的代表性问题，但没有具体指出 Appendix B.5 的 stress test 仅限 exposure 拓扑。这是一个合理的覆盖面缺陷。

2. **D5（Algorithm 1 的 PPI++ guard）**：我在审稿中没有仔细检查 Algorithm 1 的内部逻辑与 Section 4.5 报告的 method-topology 交互作用是否一致。R2 的发现是正确的。

---

### 对 R2 整体评分的看法

R2 给出 Soundness 3.5 / Excitement 3.5 / Reproducibility 4 / Overall 3.5，与我的评分完全一致。

关于 W1 的严重程度，我认为 MAJOR 比 CRITICAL 更合适（R2 的事实性错误削弱了 CRITICAL 的论据）。其余评估基本合理，两位 reviewer 在核心问题上高度一致（K≥3 gap、ASV novelty、abstract 数值不一致）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-22T17:54:08.327412+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-22T17:54:08.445486+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T17:40:09.259981+00:00\", \"completed_at\": \"2026-05-22T17:40:21.928401+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 118
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-22T17:56:37.087065+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Carried from Round 1-5 (resolved issues kept as history) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Theorem 1 使用 perspective function + convexity 证明路径：K=2 精确证明，K≥3 数值验证 worst-case <0.005。DPI 引用全部移除。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 再次提出 K≥3 部分仅有数值验证却标为 Theorem 的命名问题（见 R6-M1）。此 issue 的核心关切在 R6 以新 ID R6-M1 重新跟踪。\"\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写：83.4% 作为 K≥3 结构转变呈现，与 2.1% 并列。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未显式提及商业 LLM 缺失。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加商业 LLM 限制说明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。Algorithm 1 caption 已有 'Assumes linear structural equations'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [R2]\n        note: \"R6-R2 再次以 CRITICAL 级别提出线性假设与 NLP 适用性的 mismatch（见 R6-W1）。R1 REBUT 降为 MAJOR。\"\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"method.tex 添加完整的 'text as common cause' 讨论。\"\n    resolution_round: 5\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5 确认 FWL 证明'干净且重要'。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [R2]\n        note: \"R5 确认 ASV 是 E-value 的有意义扩展。\"\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 再次独立提出 ASV vs E-value 差异化不足（R1-W4, R2-W3），交叉回应中 [AGREE]。需更明确 delineate technical novelty。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 增加 ASV vs E-value/QBA 的明确技术对比\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未直接提及，但 R2-W6（信息密度过高）间接相关。R1 REBUT 认为在 8 页限制下是合理权衡。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6-R2-D5 指出 Algorithm 1 未加入 PPI++ 对 M-bias 的排除条件。R1 AGREE。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 加入 if M-bias: exclude PPI++ 的显式 guard\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"bib 检查通过。\"\n    resolution_round: 5\n\n  - id: R4-MR\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇引用（Round 4 新要求）\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 5\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: should-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现（23 configs），缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R5 修复了 same-sign 错误机制解释，替换为 magnitude dominance。\"\n      - round: 6\n        reviewers: [R1]\n        note: \"R6-R1-M2：Abstract 仍将此称为 'structural property'，但仅有 23 configs 的经验支撑。R2 交叉回应 AGREE。见 R6-M2。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 中 'structural property' → 'empirical regularity' 或提供 formal sufficient conditions\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  # === Round 6 新发现 ===\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M1 MAJOR），R2 交叉回应 AGREE 并指出 Conjecture 1 的正确命名与 Theorem 1 的不一致性更凸显问题。继承 R1-N1 的核心关切但聚焦命名而非证明路径。\"\n    action_items:\n      - round: 6\n        action: \"将 Theorem 1 拆分为 Theorem（K=2, exact proof）+ Proposition/Empirical Result（K≥3, numerical verification），或在定理陈述中使用显式分层措辞\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'，实际仅有经验支撑\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M2 MAJOR），R2 交叉回应 AGREE。Footnote 2 承认是 23 configs 经验发现，Section 3 仅提供 magnitude dominance 启发式解释。继承 R5-N3。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 'structural property' → 'empirical regularity' 或 'robust empirical pattern'；或提供 formal sufficient conditions（diagonal dominance threshold + coefficient magnitude ratio）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M3 MAJOR），R2 交叉回应 AGREE with nuance（认为可降为 Should-Fix）。Appendix A.4 有 general case 数值验证（230K matrices, deviation<0.01），但主文未引用此结果。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.2 或 Theorem 1 后增加 1-2 句：(a) proportional effects 对应什么现实场景，(b) 非比例情形的 worst-case deviation（引用 Appendix A.4），(c) 何时 practitioners 应警惕\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract '1.4%' sign reversal rate 与 Section 4.2 '2.1%' 数值不一致\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M4 MAJOR），R2 交叉回应 AGREE（在 D1 中独立发现来源不透明但未发现具体矛盾）。Abstract 条件（diagonal≥0.7）与 Section 4.2 相同但数字不同。\"\n    action_items:\n      - round: 6\n        action: \"统一 Abstract 与 Section 4.2 的 sign reversal rate 数字，明确计算基础（per-coefficient / per-configuration / per-topology）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2 首发为 CRITICAL，R1 REBUT 降为 MAJOR（纠正 R2 事实错误：Appendix B.6 覆盖全部 7 拓扑而非仅 exposure）。R1 论证线性模型在 CSS 因果推断中仍广泛使用。最终共识：MAJOR 级别。继承 R2-W4（R1-5）。\"\n    action_items:\n      - round: 6\n        action: \"Introduction/Conclusion 中更明确地 scope 论文适用范围为线性 SEM；在 Appendix B.6 的非线性结果基础上讨论哪些定性结论（如拓扑排序）可能在非线性下保持\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1-W4 + R2-W3 独立提出，交叉回应中双方 AGREE。继承 R4-W6。需对比 E-value、mediation sensitivity (Imai et al. 2010)、QBA framework (Lash et al. 2009)。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 增加 ASV vs E-value/QBA/mediation sensitivity 的明确技术对比表格或段落\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失 3-4 篇相关引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2 首发（W4 MAJOR，列 5 篇），R1 交叉回应部分 REBUT（3-4 篇应引，Dawid & Skene 1979 非必要，降为 MINOR）。Shu & Yi (2019) 两篇直接处理误分类×因果推断，最为关键。\"\n    action_items:\n      - round: 6\n        action: \"补充引用 Shu & Yi (2019) 两篇 + Cadei et al. (2025) + Neuhaus (1999)\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1-W3 首发，R2 交叉回应 AGREE。两者覆盖的拓扑是否互斥？ε-approximate 与 exact monotonicity 的关系？\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 末尾加 1-2 句汇总每个拓扑的 monotonicity 状态和证明级别\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: minor\n    summary: \"Non-differential stress test 仅覆盖 exposure 拓扑\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2-W5 首发，R1 交叉回应 AGREE。Appendix B.5 仅在 exposure 上测试 differential departure。\"\n    action_items:\n      - round: 6\n        action: \"扩展 Appendix B.5 stress test 到 confounding 和 mediation 拓扑\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2-D3 首发，R1 AGREE。\"\n    action_items:\n      - round: 6\n        action: \"Table 1 caption 明确 'Amplif.' = amplification (|bias| > |true effect| with same sign)\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2-D5 首发，R1 AGREE。Section 4.5 报告 PPI++ 对 M-bias harmful (-88%)，但 Algorithm 1 无显式 guard。继承 R4-W10。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 Step 2 加入 'if M-bias topology: exclude PPI++' 条件\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Carried from Round 1-5 (resolved issues kept as history) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Theorem 1 使用 perspective function + convexity 证明路径：K=2 精确证明，K≥3 数值验证 worst-case <0.005。DPI 引用全部移除。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 再次提出 K≥3 部分仅有数值验证却标为 Theorem 的命名问题（见 R6-M1）。此 issue 的核心关切在 R6 以新 ID R6-M1 重新跟踪。\"\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写：83.4% 作为 K≥3 结构转变呈现，与 2.1% 并列。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未显式提及商业 LLM 缺失。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加商业 LLM 限制说明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。Algorithm 1 caption 已有 'Assumes linear structural equations'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [R2]\n        note: \"R6-R2 再次以 CRITICAL 级别提出线性假设与 NLP 适用性的 mismatch（见 R6-W1）。R1 REBUT 降为 MAJOR。\"\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"method.tex 添加完整的 'text as common cause' 讨论。\"\n    resolution_round: 5\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5 确认 FWL 证明'干净且重要'。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [R2]\n        note: \"R5 确认 ASV 是 E-value 的有意义扩展。\"\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 再次独立提出 ASV vs E-value 差异化不足（R1-W4, R2-W3），交叉回应中 [AGREE]。需更明确 delineate technical novelty。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 增加 ASV vs E-value/QBA 的明确技术对比\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未直接提及，但 R2-W6（信息密度过高）间接相关。R1 REBUT 认为在 8 页限制下是合理权衡。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6-R2-D5 指出 Algorithm 1 未加入 PPI++ 对 M-bias 的排除条件。R1 AGREE。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 加入 if M-bias: exclude PPI++ 的显式 guard\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"bib 检查通过。\"\n    resolution_round: 5\n\n  - id: R4-MR\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇引用（Round 4 新要求）\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 5\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: should-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现（23 configs），缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R5 修复了 same-sign 错误机制解释，替换为 magnitude dominance。\"\n      - round: 6\n        reviewers: [R1]\n        note: \"R6-R1-M2：Abstract 仍将此称为 'structural property'，但仅有 23 configs 的经验支撑。R2 交叉回应 AGREE。见 R6-M2。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 中 'structural property' → 'empirical regularity' 或提供 formal sufficient conditions\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  # === Round 6 新发现 ===\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M1 MAJOR），R2 交叉回应 AGREE 并指出 Conjecture 1 的正确命名与 Theorem 1 的不一致性更凸显问题。继承 R1-N1 的核心关切但聚焦命名而非证明路径。\"\n    action_items:\n      - round: 6\n        action: \"将 Theorem 1 拆分为 Theorem（K=2, exact proof）+ Proposition/Empirical Result（K≥3, numerical verification），或在定理陈述中使用显式分层措辞\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'，实际仅有经验支撑\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M2 MAJOR），R2 交叉回应 AGREE。Footnote 2 承认是 23 configs 经验发现，Section 3 仅提供 magnitude dominance 启发式解释。继承 R5-N3。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 'structural property' → 'empirical regularity' 或 'robust empirical pattern'；或提供 formal sufficient conditions（diagonal dominance threshold + coefficient magnitude ratio）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M3 MAJOR），R2 交叉回应 AGREE with nuance（认为可降为 Should-Fix）。Appendix A.4 有 general case 数值验证（230K matrices, deviation<0.01），但主文未引用此结果。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.2 或 Theorem 1 后增加 1-2 句：(a) proportional effects 对应什么现实场景，(b) 非比例情形的 worst-case deviation（引用 Appendix A.4），(c) 何时 practitioners 应警惕\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract '1.4%' sign reversal rate 与 Section 4.2 '2.1%' 数值不一致\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1 首发（M4 MAJOR），R2 交叉回应 AGREE（在 D1 中独立发现来源不透明但未发现具体矛盾）。Abstract 条件（diagonal≥0.7）与 Section 4.2 相同但数字不同。\"\n    action_items:\n      - round: 6\n        action: \"统一 Abstract 与 Section 4.2 的 sign reversal rate 数字，明确计算基础（per-coefficient / per-configuration / per-topology）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2 首发为 CRITICAL，R1 REBUT 降为 MAJOR（纠正 R2 事实错误：Appendix B.6 覆盖全部 7 拓扑而非仅 exposure）。R1 论证线性模型在 CSS 因果推断中仍广泛使用。最终共识：MAJOR 级别。继承 R2-W4（R1-5）。\"\n    action_items:\n      - round: 6\n        action: \"Introduction/Conclusion 中更明确地 scope 论文适用范围为线性 SEM；在 Appendix B.6 的非线性结果基础上讨论哪些定性结论（如拓扑排序）可能在非线性下保持\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1-W4 + R2-W3 独立提出，交叉回应中双方 AGREE。继承 R4-W6。需对比 E-value、mediation sensitivity (Imai et al. 2010)、QBA framework (Lash et al. 2009)。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 增加 ASV vs E-value/QBA/mediation sensitivity 的明确技术对比表格或段落\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失 3-4 篇相关引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2 首发（W4 MAJOR，列 5 篇），R1 交叉回应部分 REBUT（3-4 篇应引，Dawid & Skene 1979 非必要，降为 MINOR）。Shu & Yi (2019) 两篇直接处理误分类×因果推断，最为关键。\"\n    action_items:\n      - round: 6\n        action: \"补充引用 Shu & Yi (2019) 两篇 + Cadei et al. (2025) + Neuhaus (1999)\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R1-W3 首发，R2 交叉回应 AGREE。两者覆盖的拓扑是否互斥？ε-approximate 与 exact monotonicity 的关系？\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 末尾加 1-2 句汇总每个拓扑的 monotonicity 状态和证明级别\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: minor\n    summary: \"Non-differential stress test 仅覆盖 exposure 拓扑\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2-W5 首发，R1 交叉回应 AGREE。Appendix B.5 仅在 exposure 上测试 differential departure。\"\n    action_items:\n      - round: 6\n        action: \"扩展 Appendix B.5 stress test 到 confounding 和 mediation 拓扑\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2-D3 首发，R1 AGREE。\"\n    action_items:\n      - round: 6\n        action: \"Table 1 caption 明确 'Amplif.' = amplification (|bias| > |true effect| with same sign)\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R2-D5 首发，R1 AGREE。Section 4.5 报告 PPI++ 对 M-bias harmful (-88%)，但 Algorithm 1 无显式 guard。继承 R4-W10。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 Step 2 加入 'if M-bias topology: exclude PPI++' 条件\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-22T17:56:37.694517+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 17602}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-22T17:58:45.984463+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "report": "# 审稿报告 — Round 6（Fresh Review）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026（ACL Rolling Review）\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）\n**交叉分享**: 完成，1 轮收敛\n**Overall**: 3.5/5（Borderline Conference）\n\n---\n\n## Summary\n\n本文研究 LLM 多类别（K≥3）标注误差如何沿 7 种典型因果 DAG 拓扑传播至下游因果估计。主要贡献：(1) 推导 7 种拓扑下非差异误分类的闭合偏差表达式，揭示二元 \"偏向零\" 保证在 K≥3 时结构性失效（83.4% exposure 矩阵产生 sign reversal）；(2) 证明 FWL 不变性使矩阵校正对 4 种 A-as-covariate 拓扑无效——被 annotation correction 文献忽略的 negative result；(3) 提出 ASV（Annotation Sensitivity Values）框架，三种互补类型（magnitude/significance/sign-flip）量化拓扑依赖的脆弱性谱。经验验证使用 4 个 LLM × 3 个 NLP 数据集（23 种配置，161 个 bias 场景）。\n\n---\n\n## Strengths\n\n**S1. 真正的理论空白填补** [R1, R2 共识]\n现有文献要么处理二元误分类（Brenner 1993），要么仅覆盖单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下系统比较 K≥3 误分类在 7 种 DAG 拓扑下的行为。核心发现——topology 而非 annotator quality 决定下游 bias（同一 F₁ 范围内 bias 相差 10×）——非平凡且有实际意义。\n\n**S2. FWL 不变性的独立价值** [R1, R2 共识]\n证明线性校正（C⁻¹ premultiplication, MLA, SIMEX）在 confounding/mediation/collider/M-bias 四种拓扑下 exactly 0% bias reduction。证明简洁（column space preservation under FWL projection, Appendix B.2），结论对 practitioners 有非平凡指导意义。\n\n**S3. 透明的理论层级** [R1]\nproved → verified → conjectured 三层体系科学诚实。Proposition 1 对 confounding/collider 的解析证明（Cauchy-Schwarz, general K）技术正确。\n\n**S4. 扎实的验证规模** [R1, R2 共识]\n100,000 random confusion matrices（每拓扑）+ 4 LLM × 3 真实 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2）= 23 configurations, 161 bias scenarios。远超 \"toy example\" 水平。\n\n**S5. 可操作的 ASV 框架和 Algorithm 1** [R2]\n三种 ASV 类型提供从 \"多大误差可容忍\" 到 \"何时符号翻转\" 的完整风险图谱。Algorithm 1 给出拓扑→风险→校正方法选择的 actionable pipeline。\n\n**S6. 时效性** [R2]\nLLM 标注在 CSS 中的快速采用使标注误差对因果推断的影响成为紧迫问题，论文定位与 EMNLP 受众匹配。\n\n---\n\n## Weaknesses\n\n### Must-Fix（1 项）\n\n**W-MF1. [MUST-FIX] Abstract 与正文数值不一致** [R1-M4, R2-D1; 双方 AGREE]\n- Abstract: \"Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.4%\"\n- Section 4.2: 在相同条件下报告 \"2.1% sign reversal\"\n- 可能原因：不同的 averaging 方式（per-coefficient vs per-configuration vs per-topology），但 Abstract 未做限定\n- **Action**: 统一数字并明确计算基础\n\n### Should-Fix（6 项）\n\n**W-SF1. Theorem 1 对 K≥3 未证明但标记为 \"Theorem\"** [R1-M1, R2-W2; 双方 AGREE]\n- K=2 通过 perspective function + convexity 严格证明——正确且优雅\n- K≥3 仅有数值验证（20,000 random triples, worst-case deviation < 0.005），不构成数学证明\n- Conjecture 1 正确使用了 \"conjecture\" 命名，但 Theorem 1 的不一致命名凸显问题\n- **Action**: 拆分为 Theorem（K=2）+ Proposition/Empirical Result（K≥3），或在陈述中显式分层\n\n**W-SF2. Abstract 将 \"primary coefficient never reverses\" 称为 \"structural property\"，实际仅有经验支撑** [R1-M2; R2 交叉 AGREE]\n- Footnote 2 承认是 23 LLM configurations 的经验观察\n- Section 3 仅提供 magnitude dominance 启发式解释，无 formal proof 或 sufficient conditions\n- \"Structural property\" 在学术语境中暗示数学保证\n- **Action**: 改为 \"empirical regularity\" 或提供 formal sufficient conditions（diagonal dominance threshold + coefficient magnitude ratio）\n\n**W-SF3. Proportional effects 假设 (f=λg) 讨论不足** [R1-M3; R2 交叉 AGREE with nuance]\n- Theorem 1 核心条件，但主文未解释何时此假设合理\n- Appendix A.4 有 general case 数值验证（230K matrices, deviation < 0.01），主文未引用\n- R2 认为可降为 Should-Fix（非 Must-Fix），因附录有对冲\n- **Action**: Section 3.2 增加 1-2 句说明 proportional effects 的现实含义 + 非比例情形的近似程度\n\n**W-SF4. 线性模型假设与 NLP 实践的 scope mismatch** [R2-W1 CRITICAL → R1 REBUT → 共识 MAJOR/Should-Fix]\n- 全部 bias 表达式、sign preservation、FWL invariance 建立在线性 SEM 上\n- **R1 纠正 R2 事实错误**: Appendix B.6 覆盖全部 7 拓扑的 logistic DGP（非仅 exposure），Table 8 报告完整结果\n- R1 论证：线性模型在 CSS 因果推断中仍广泛使用（Angrist & Pischke 2009），经典测量误差文献同样从线性出发\n- 共识：真实限制但非致命——论文在线性框架内的贡献是完整的\n- **Action**: Introduction/Conclusion 更明确 scope 为线性 SEM；讨论 B.6 非线性结果中哪些定性结论（如拓扑排序）保持\n\n**W-SF5. ASV 与 E-value 的方法论创新边界不清晰** [R1-W4, R2-W3; 双方独立提出并交叉 AGREE]\n- 论文声称三个 key differences，但可能仅是应用领域变换 + 自然延伸\n- 未充分对比 mediation sensitivity analysis (Imai et al. 2010) 和 QBA framework (Lash et al. 2009)\n- **Action**: 增加 ASV vs E-value/QBA 的技术对比（table 或 dedicated paragraph）\n\n**W-SF6. Conjecture 1 与 Theorem 1 覆盖范围关系不清晰** [R1-W3; R2 交叉 AGREE]\n- Theorem 1 覆盖 confounding/mediation；Conjecture 1 覆盖 collider/M-bias\n- ε-approximate monotonicity 与 strict monotonicity 的关系未说明\n- Exposure/front-door/IV 的 monotonicity 状态散落各处\n- **Action**: Section 3.3 末尾加汇总句，明确每个拓扑的 monotonicity 状态和证明级别\n\n### Minor（5 项）\n\n**W-M1.** 缺失 3-4 篇引用：Shu & Yi (2019) 两篇（误分类×因果推断，最关键）、Cadei et al. (2025) PPI 因果推断扩展、Neuhaus (1999) [R2-W4; R1 部分 AGREE，降为 MINOR]\n\n**W-M2.** Non-differential stress test (Appendix B.5) 仅覆盖 exposure 拓扑，应扩展到 confounding/mediation [R2-W5; R1 AGREE]\n\n**W-M3.** Table 1 \"Amplif.\" 列含义在 caption 中未解释 [R2-D3; R1 AGREE]\n\n**W-M4.** Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用（Section 4.5 报告 -88% 有害）[R2-D5; R1 AGREE]\n\n**W-M5.** Figure 2 子图过小，6 个分布细节难辨 [R2-D2; R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 的关键共识**（两位 Reviewer 一致）：\n1. Theorem 1 K≥3 命名不严谨——应拆分或显式分层\n2. Abstract \"structural property\" 措辞过度——应降为 \"empirical regularity\"\n3. 1.4% vs 2.1% 数值不一致——必须修正\n4. ASV vs E-value 差异化不足——需要明确技术对比\n5. 论文在线性框架内的贡献是扎实和完整的\n6. FWL 不变性是独立有价值的 negative result\n7. Algorithm 1 需加入 PPI++ M-bias guard\n\n## Reviewer Divergence\n\n**R2-W1 严重程度**：R2 定为 CRITICAL（线性假设根本性限制 NLP 适用性），R1 REBUT 降为 MAJOR。\n\n- R1 纠正了 R2 的事实性错误（Appendix B.6 覆盖全部 7 拓扑，非仅 exposure）\n- R1 论证线性模型在 CSS 因果推断中是标准方法，且经典测量误差文献同样线性起步\n- **Director 判断**: 采纳 R1 的 MAJOR 定级。R2 的核心关切（scope mismatch）成立，但论文已在 B.6 提供非线性 robustness check，且 Limitations 已承认此限制。CRITICAL 意味着不可修补，而此问题可通过更诚实的 scoping 解决。\n\n**R2-W4 严重程度**：R2 定为 MAJOR（遗漏 5 篇引用），R1 部分 REBUT 降为 MINOR。\n\n- R1 同意 3-4 篇应引，但指出 Dawid & Skene (1979) 非必要（本文不涉及 multi-annotator）\n- 核心 Related Work 覆盖已较完整\n- **Director 判断**: 采纳 R1 的 MINOR 定级。引用补充是直接修复，不构成 structural concern。\n\n**R2-W6（信息密度）**：R2 认为 Section 3.2 密度过高，R1 REBUT。\n\n- **Director 判断**: 采纳 R1 的判断。8 页限制下 7 拓扑的系统覆盖是论文核心贡献，统一结构（bias expression → sign behavior → insight）使扫描可行。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R1-Q1] 是否存在 formal sufficient conditions 保证 primary coefficient 不反转（如 diagonal dominance threshold + |β₁|/|β₂| ratio）？\n**Q2.** [R1-Q2] Proportional effects 假设 f=λg 对应什么具体的 DGP 场景？何时不成立？\n**Q3.** [R1-Q3] Abstract 中 1.4% 的精确定义和计算基础？与 Section 4.2 的 2.1% 是什么关系？\n**Q4.** [R1-Q4, R2-Q4] ASV 相对 E-value 在方法论上的独立技术贡献是什么？\n**Q5.** [R2-Q1] 非线性 DGP 下完整拓扑比较数据是否可用？拓扑排序是否与线性一致？\n**Q6.** [R2-Q2] C₀ 估计基于小 validation set (<100 gold labels) 时，ASV 可靠性如何？\n**Q7.** [R1-Q5] 对 FWL invariance 使校正失效的 4 种拓扑，除 PPI++ 外还有什么 gold-free 策略？\n\n---\n\n## Missing References\n\n1. **Shu, D. & Yi, G.Y. (2019).** Weighted causal inference methods with mismeasured covariates and misclassified outcomes. *Statistics in Medicine*, 38(10), 1835-1854. [最关键——直接处理误分类×因果推断]\n2. **Shu, D. & Yi, G.Y. (2019).** Causal inference with measurement error in outcomes. *Statistical Methods in Medical Research*, 28(7), 2049-2068.\n3. **Cadei, R. et al. (2025).** Prediction-Powered Causal Inferences. *arXiv:2502.06343*. [PPI→因果推断扩展，与 Section 4.5 直接相关]\n4. **Neuhaus, J.M. (1999).** Bias and efficiency loss due to misclassified responses in binary regression. *Biometrika*, 86(4), 843-855.\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: error — 视觉审查 Agent 因 API 限额异常退出（\"You've hit your limit · resets 4pm (UTC)\"），未完成页面级排版检查。用户可在限额重置后重新触发 `dispatch_visual_check`。\n\n从 PDF 目视检查（非 Agent 系统化检查）：\n- 正文 8 页，Limitations + References 从第 9 页起，符合 EMNLP 8 页限制\n- Figure 1（DAG taxonomy）清晰可辨，但 Figure 2（bias distributions）6 个子图在半栏宽下细节较难分辨\n- Table 1 结构清晰，但 \"Amplif.\" 列缺 caption 解释\n- 匿名性完整（\"Anonymous ACL submission\"，无 de-anonymizing 信息）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5/5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**置信度**: 4/5（两位 Reviewer 独立收敛到相同评分，交叉回应后核心判断一致）\n\n**核心判断**：\n\n论文在线性 SEM + 非差异误分类框架内填补了 multi-class × multi-topology 的真正理论空白。FWL 不变性是有独立价值的 negative result，ASV 框架对 practitioners 可操作。验证规模（100K matrices + 23 真实 LLM 配置）远超同类工作。\n\n**阻碍更高评分的关键因素**：\n1. **证明完备性**：Theorem 1 对 K≥3 的命名不严谨，\"primary coefficient never reverses\" 被过度声称为 \"structural property\"\n2. **Scope 限制**：线性 SEM 假设在 NLP 实践中适用范围有限，多项结果限于 K=3\n3. **Novelty 定位**：ASV 相对 E-value 的方法论增量需更清晰 delineation\n\n所有问题均可在 ARR revision 中修补。主要修改量集中在措辞调整（Theorem 命名、Abstract 表述、数值统一）和少量补充讨论（proportional effects、ASV 对比、缺失引用），不涉及实验重做或理论推翻。\n\n**建议投递方向**：如果能在 ARR submission deadline (2026-05-25) 前完成 Must-Fix（数值统一）和关键 Should-Fix（Theorem 命名、Abstract 措辞），论文有望在 ARR review 中获得 3.5-4.0 分（Borderline Conference 到 Conference），进入 EMNLP 2026 Main 或 Findings。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 1.4% vs 2.1% 数值不一致 [W-MF1]\n- \"structural property\" → \"empirical regularity\" [W-SF2]\n- R2-D1：未明确 sign reversal 仅限 exposure/IV 拓扑，可能误导\n\n### Section 1 (Introduction)\n- Framing 总体清晰，三个 contribution 明确\n- 数字密度在前 2 轮修改后已改善\n- 可更明确地 scope 为 linear SEM\n\n### Section 2 (Related Work)\n- 核心覆盖完整（Carroll, Gustafson, Pearl, VanderWeele & Ding, Edwards et al.）\n- 补充 Shu & Yi (2019), Cadei et al. (2025), Neuhaus (1999) [W-M1]\n\n### Section 3 (Method)\n- 3.1 Setup: non-differential 定义清晰；\"text as common cause\" 讨论充分\n- 3.2 Bias expressions: 7 拓扑按统一结构呈现，系统完整\n  - Theorem 1 命名需修正 [W-SF1]\n  - Proportional effects 讨论不足 [W-SF3]\n  - Conjecture 1 与 Theorem 1 关系不清 [W-SF6]\n- 3.3 ASV: 框架设计合理\n  - vs E-value 差异化不足 [W-SF5]\n\n### Section 4 (Experiments)\n- 4.1 Setup: Monte Carlo 设计充分\n- 4.2 Taxonomy: 验证扎实，Table 1 \"Amplif.\" 需解释 [W-M3]\n- 4.3 ASV validation: envelope monotonicity 验证充分\n- 4.4 Empirical: 23 configs 提供真实 grounding\n- 4.5 Correction: FWL 证明干净；Algorithm 1 缺 PPI++ M-bias guard [W-M4]\n\n### Section 5 (Conclusion) + Limitations\n- 结论准确反映贡献\n- Limitations 覆盖关键限制（non-differential, linear, K 范围, single annotator）\n- 可扩展：ASV 在大 K 时的计算成本\n\n### Figures and Tables\n- Figure 1: 清晰可辨\n- Figure 2: 子图过小 [W-M5]\n- Figure 3 (F₁ vs bias): 有效传达核心信息\n- Table 1: 结构清晰，caption 需完善 [W-M3]\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "report": "# 审稿报告 — Round 6（Fresh Review）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026（ACL Rolling Review）\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）\n**交叉分享**: 完成，1 轮收敛\n**Overall**: 3.5/5（Borderline Conference）\n\n---\n\n## Summary\n\n本文研究 LLM 多类别（K≥3）标注误差如何沿 7 种典型因果 DAG 拓扑传播至下游因果估计。主要贡献：(1) 推导 7 种拓扑下非差异误分类的闭合偏差表达式，揭示二元 \"偏向零\" 保证在 K≥3 时结构性失效（83.4% exposure 矩阵产生 sign reversal）；(2) 证明 FWL 不变性使矩阵校正对 4 种 A-as-covariate 拓扑无效——被 annotation correction 文献忽略的 negative result；(3) 提出 ASV（Annotation Sensitivity Values）框架，三种互补类型（magnitude/significance/sign-flip）量化拓扑依赖的脆弱性谱。经验验证使用 4 个 LLM × 3 个 NLP 数据集（23 种配置，161 个 bias 场景）。\n\n---\n\n## Strengths\n\n**S1. 真正的理论空白填补** [R1, R2 共识]\n现有文献要么处理二元误分类（Brenner 1993），要么仅覆盖单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下系统比较 K≥3 误分类在 7 种 DAG 拓扑下的行为。核心发现——topology 而非 annotator quality 决定下游 bias（同一 F₁ 范围内 bias 相差 10×）——非平凡且有实际意义。\n\n**S2. FWL 不变性的独立价值** [R1, R2 共识]\n证明线性校正（C⁻¹ premultiplication, MLA, SIMEX）在 confounding/mediation/collider/M-bias 四种拓扑下 exactly 0% bias reduction。证明简洁（column space preservation under FWL projection, Appendix B.2），结论对 practitioners 有非平凡指导意义。\n\n**S3. 透明的理论层级** [R1]\nproved → verified → conjectured 三层体系科学诚实。Proposition 1 对 confounding/collider 的解析证明（Cauchy-Schwarz, general K）技术正确。\n\n**S4. 扎实的验证规模** [R1, R2 共识]\n100,000 random confusion matrices（每拓扑）+ 4 LLM × 3 真实 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2）= 23 configurations, 161 bias scenarios。远超 \"toy example\" 水平。\n\n**S5. 可操作的 ASV 框架和 Algorithm 1** [R2]\n三种 ASV 类型提供从 \"多大误差可容忍\" 到 \"何时符号翻转\" 的完整风险图谱。Algorithm 1 给出拓扑→风险→校正方法选择的 actionable pipeline。\n\n**S6. 时效性** [R2]\nLLM 标注在 CSS 中的快速采用使标注误差对因果推断的影响成为紧迫问题，论文定位与 EMNLP 受众匹配。\n\n---\n\n## Weaknesses\n\n### Must-Fix（1 项）\n\n**W-MF1. [MUST-FIX] Abstract 与正文数值不一致** [R1-M4, R2-D1; 双方 AGREE]\n- Abstract: \"Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.4%\"\n- Section 4.2: 在相同条件下报告 \"2.1% sign reversal\"\n- 可能原因：不同的 averaging 方式（per-coefficient vs per-configuration vs per-topology），但 Abstract 未做限定\n- **Action**: 统一数字并明确计算基础\n\n### Should-Fix（6 项）\n\n**W-SF1. Theorem 1 对 K≥3 未证明但标记为 \"Theorem\"** [R1-M1, R2-W2; 双方 AGREE]\n- K=2 通过 perspective function + convexity 严格证明——正确且优雅\n- K≥3 仅有数值验证（20,000 random triples, worst-case deviation < 0.005），不构成数学证明\n- Conjecture 1 正确使用了 \"conjecture\" 命名，但 Theorem 1 的不一致命名凸显问题\n- **Action**: 拆分为 Theorem（K=2）+ Proposition/Empirical Result（K≥3），或在陈述中显式分层\n\n**W-SF2. Abstract 将 \"primary coefficient never reverses\" 称为 \"structural property\"，实际仅有经验支撑** [R1-M2; R2 交叉 AGREE]\n- Footnote 2 承认是 23 LLM configurations 的经验观察\n- Section 3 仅提供 magnitude dominance 启发式解释，无 formal proof 或 sufficient conditions\n- \"Structural property\" 在学术语境中暗示数学保证\n- **Action**: 改为 \"empirical regularity\" 或提供 formal sufficient conditions（diagonal dominance threshold + coefficient magnitude ratio）\n\n**W-SF3. Proportional effects 假设 (f=λg) 讨论不足** [R1-M3; R2 交叉 AGREE with nuance]\n- Theorem 1 核心条件，但主文未解释何时此假设合理\n- Appendix A.4 有 general case 数值验证（230K matrices, deviation < 0.01），主文未引用\n- R2 认为可降为 Should-Fix（非 Must-Fix），因附录有对冲\n- **Action**: Section 3.2 增加 1-2 句说明 proportional effects 的现实含义 + 非比例情形的近似程度\n\n**W-SF4. 线性模型假设与 NLP 实践的 scope mismatch** [R2-W1 CRITICAL → R1 REBUT → 共识 MAJOR/Should-Fix]\n- 全部 bias 表达式、sign preservation、FWL invariance 建立在线性 SEM 上\n- **R1 纠正 R2 事实错误**: Appendix B.6 覆盖全部 7 拓扑的 logistic DGP（非仅 exposure），Table 8 报告完整结果\n- R1 论证：线性模型在 CSS 因果推断中仍广泛使用（Angrist & Pischke 2009），经典测量误差文献同样从线性出发\n- 共识：真实限制但非致命——论文在线性框架内的贡献是完整的\n- **Action**: Introduction/Conclusion 更明确 scope 为线性 SEM；讨论 B.6 非线性结果中哪些定性结论（如拓扑排序）保持\n\n**W-SF5. ASV 与 E-value 的方法论创新边界不清晰** [R1-W4, R2-W3; 双方独立提出并交叉 AGREE]\n- 论文声称三个 key differences，但可能仅是应用领域变换 + 自然延伸\n- 未充分对比 mediation sensitivity analysis (Imai et al. 2010) 和 QBA framework (Lash et al. 2009)\n- **Action**: 增加 ASV vs E-value/QBA 的技术对比（table 或 dedicated paragraph）\n\n**W-SF6. Conjecture 1 与 Theorem 1 覆盖范围关系不清晰** [R1-W3; R2 交叉 AGREE]\n- Theorem 1 覆盖 confounding/mediation；Conjecture 1 覆盖 collider/M-bias\n- ε-approximate monotonicity 与 strict monotonicity 的关系未说明\n- Exposure/front-door/IV 的 monotonicity 状态散落各处\n- **Action**: Section 3.3 末尾加汇总句，明确每个拓扑的 monotonicity 状态和证明级别\n\n### Minor（5 项）\n\n**W-M1.** 缺失 3-4 篇引用：Shu & Yi (2019) 两篇（误分类×因果推断，最关键）、Cadei et al. (2025) PPI 因果推断扩展、Neuhaus (1999) [R2-W4; R1 部分 AGREE，降为 MINOR]\n\n**W-M2.** Non-differential stress test (Appendix B.5) 仅覆盖 exposure 拓扑，应扩展到 confounding/mediation [R2-W5; R1 AGREE]\n\n**W-M3.** Table 1 \"Amplif.\" 列含义在 caption 中未解释 [R2-D3; R1 AGREE]\n\n**W-M4.** Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用（Section 4.5 报告 -88% 有害）[R2-D5; R1 AGREE]\n\n**W-M5.** Figure 2 子图过小，6 个分布细节难辨 [R2-D2; R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 的关键共识**（两位 Reviewer 一致）：\n1. Theorem 1 K≥3 命名不严谨——应拆分或显式分层\n2. Abstract \"structural property\" 措辞过度——应降为 \"empirical regularity\"\n3. 1.4% vs 2.1% 数值不一致——必须修正\n4. ASV vs E-value 差异化不足——需要明确技术对比\n5. 论文在线性框架内的贡献是扎实和完整的\n6. FWL 不变性是独立有价值的 negative result\n7. Algorithm 1 需加入 PPI++ M-bias guard\n\n## Reviewer Divergence\n\n**R2-W1 严重程度**：R2 定为 CRITICAL（线性假设根本性限制 NLP 适用性），R1 REBUT 降为 MAJOR。\n\n- R1 纠正了 R2 的事实性错误（Appendix B.6 覆盖全部 7 拓扑，非仅 exposure）\n- R1 论证线性模型在 CSS 因果推断中是标准方法，且经典测量误差文献同样线性起步\n- **Director 判断**: 采纳 R1 的 MAJOR 定级。R2 的核心关切（scope mismatch）成立，但论文已在 B.6 提供非线性 robustness check，且 Limitations 已承认此限制。CRITICAL 意味着不可修补，而此问题可通过更诚实的 scoping 解决。\n\n**R2-W4 严重程度**：R2 定为 MAJOR（遗漏 5 篇引用），R1 部分 REBUT 降为 MINOR。\n\n- R1 同意 3-4 篇应引，但指出 Dawid & Skene (1979) 非必要（本文不涉及 multi-annotator）\n- 核心 Related Work 覆盖已较完整\n- **Director 判断**: 采纳 R1 的 MINOR 定级。引用补充是直接修复，不构成 structural concern。\n\n**R2-W6（信息密度）**：R2 认为 Section 3.2 密度过高，R1 REBUT。\n\n- **Director 判断**: 采纳 R1 的判断。8 页限制下 7 拓扑的系统覆盖是论文核心贡献，统一结构（bias expression → sign behavior → insight）使扫描可行。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R1-Q1] 是否存在 formal sufficient conditions 保证 primary coefficient 不反转（如 diagonal dominance threshold + |β₁|/|β₂| ratio）？\n**Q2.** [R1-Q2] Proportional effects 假设 f=λg 对应什么具体的 DGP 场景？何时不成立？\n**Q3.** [R1-Q3] Abstract 中 1.4% 的精确定义和计算基础？与 Section 4.2 的 2.1% 是什么关系？\n**Q4.** [R1-Q4, R2-Q4] ASV 相对 E-value 在方法论上的独立技术贡献是什么？\n**Q5.** [R2-Q1] 非线性 DGP 下完整拓扑比较数据是否可用？拓扑排序是否与线性一致？\n**Q6.** [R2-Q2] C₀ 估计基于小 validation set (<100 gold labels) 时，ASV 可靠性如何？\n**Q7.** [R1-Q5] 对 FWL invariance 使校正失效的 4 种拓扑，除 PPI++ 外还有什么 gold-free 策略？\n\n---\n\n## Missing References\n\n1. **Shu, D. & Yi, G.Y. (2019).** Weighted causal inference methods with mismeasured covariates and misclassified outcomes. *Statistics in Medicine*, 38(10), 1835-1854. [最关键——直接处理误分类×因果推断]\n2. **Shu, D. & Yi, G.Y. (2019).** Causal inference with measurement error in outcomes. *Statistical Methods in Medical Research*, 28(7), 2049-2068.\n3. **Cadei, R. et al. (2025).** Prediction-Powered Causal Inferences. *arXiv:2502.06343*. [PPI→因果推断扩展，与 Section 4.5 直接相关]\n4. **Neuhaus, J.M. (1999).** Bias and efficiency loss due to misclassified responses in binary regression. *Biometrika*, 86(4), 843-855.\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: error — 视觉审查 Agent 因 API 限额异常退出（\"You've hit your limit · resets 4pm (UTC)\"），未完成页面级排版检查。用户可在限额重置后重新触发 `dispatch_visual_check`。\n\n从 PDF 目视检查（非 Agent 系统化检查）：\n- 正文 8 页，Limitations + References 从第 9 页起，符合 EMNLP 8 页限制\n- Figure 1（DAG taxonomy）清晰可辨，但 Figure 2（bias distributions）6 个子图在半栏宽下细节较难分辨\n- Table 1 结构清晰，但 \"Amplif.\" 列缺 caption 解释\n- 匿名性完整（\"Anonymous ACL submission\"，无 de-anonymizing 信息）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5/5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**置信度**: 4/5（两位 Reviewer 独立收敛到相同评分，交叉回应后核心判断一致）\n\n**核心判断**：\n\n论文在线性 SEM + 非差异误分类框架内填补了 multi-class × multi-topology 的真正理论空白。FWL 不变性是有独立价值的 negative result，ASV 框架对 practitioners 可操作。验证规模（100K matrices + 23 真实 LLM 配置）远超同类工作。\n\n**阻碍更高评分的关键因素**：\n1. **证明完备性**：Theorem 1 对 K≥3 的命名不严谨，\"primary coefficient never reverses\" 被过度声称为 \"structural property\"\n2. **Scope 限制**：线性 SEM 假设在 NLP 实践中适用范围有限，多项结果限于 K=3\n3. **Novelty 定位**：ASV 相对 E-value 的方法论增量需更清晰 delineation\n\n所有问题均可在 ARR revision 中修补。主要修改量集中在措辞调整（Theorem 命名、Abstract 表述、数值统一）和少量补充讨论（proportional effects、ASV 对比、缺失引用），不涉及实验重做或理论推翻。\n\n**建议投递方向**：如果能在 ARR submission deadline (2026-05-25) 前完成 Must-Fix（数值统一）和关键 Should-Fix（Theorem 命名、Abstract 措辞），论文有望在 ARR review 中获得 3.5-4.0 分（Borderline Conference 到 Conference），进入 EMNLP 2026 Main 或 Findings。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 1.4% vs 2.1% 数值不一致 [W-MF1]\n- \"structural property\" → \"empirical regularity\" [W-SF2]\n- R2-D1：未明确 sign reversal 仅限 exposure/IV 拓扑，可能误导\n\n### Section 1 (Introduction)\n- Framing 总体清晰，三个 contribution 明确\n- 数字密度在前 2 轮修改后已改善\n- 可更明确地 scope 为 linear SEM\n\n### Section 2 (Related Work)\n- 核心覆盖完整（Carroll, Gustafson, Pearl, VanderWeele & Ding, Edwards et al.）\n- 补充 Shu & Yi (2019), Cadei et al. (2025), Neuhaus (1999) [W-M1]\n\n### Section 3 (Method)\n- 3.1 Setup: non-differential 定义清晰；\"text as common cause\" 讨论充分\n- 3.2 Bias expressions: 7 拓扑按统一结构呈现，系统完整\n  - Theorem 1 命名需修正 [W-SF1]\n  - Proportional effects 讨论不足 [W-SF3]\n  - Conjecture 1 与 Theorem 1 关系不清 [W-SF6]\n- 3.3 ASV: 框架设计合理\n  - vs E-value 差异化不足 [W-SF5]\n\n### Section 4 (Experiments)\n- 4.1 Setup: Monte Carlo 设计充分\n- 4.2 Taxonomy: 验证扎实，Table 1 \"Amplif.\" 需解释 [W-M3]\n- 4.3 ASV validation: envelope monotonicity 验证充分\n- 4.4 Empirical: 23 configs 提供真实 grounding\n- 4.5 Correction: FWL 证明干净；Algorithm 1 缺 PPI++ M-bias guard [W-M4]\n\n### Section 5 (Conclusion) + Limitations\n- 结论准确反映贡献\n- Limitations 覆盖关键限制（non-differential, linear, K 范围, single annotator）\n- 可扩展：ASV 在大 K 时的计算成本\n\n### Figures and Tables\n- Figure 1: 清晰可辨\n- Figure 2: 子图过小 [W-M5]\n- Figure 3 (F₁ vs bias): 有效传达核心信息\n- Table 1: 结构清晰，caption 需完善 [W-M3]\n"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-22T17:58:57.669208+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 11684
}
```

</details>

---


### Assistant

_source line 488 · 2026-05-22T17:59:06.001775+00:00_

审稿报告已投递。

**Round 6 审稿完成**。两位 Reviewer 独立评审 + 交叉分享 + 1 轮收敛，最终报告已提交至 Research Director。

**核心结论**：
- **Overall 3.5/5（Borderline Conference）**，两位 Reviewer 评分完全一致
- **1 项 Must-Fix**：Abstract 1.4% vs Section 4.2 2.1% 数值不一致
- **6 项 Should-Fix**：Theorem 1 K≥3 命名、Abstract "structural property" 措辞、proportional effects 讨论、线性 scope 声明、ASV vs E-value 差异化、Conjecture/Theorem 关系
- **5 项 Minor**：缺失引用 3-4 篇、stress test 覆盖面、Table caption、Algorithm 1 guard、Figure 2 尺寸
- 所有问题均可在 ARR deadline (05-25) 前修补，不涉及实验重做或理论推翻

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 489 · 2026-05-22T17:59:08.743042+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。要点总结：

- **R2-W1 (CRITICAL 线性假设)**：[REBUT] 降为 MAJOR。R2 事实性错误——Appendix B.6 测试了全部 7 种拓扑的 logistic regression，非仅 exposure。线性假设是真实限制但在因果推断文献中是正常起点。
- **R2-W2 (K>3)**：[AGREE]，但修正 R2 的表述——Proposition 1 的解析证明是 general K 的，K 限制主要在 Theorem 1 和 Conjecture 1。
- **R2-W3 (ASV novelty)**：[AGREE]，与我的 W4 一致。
- **R2-W4 (缺失引用)**：部分 [AGREE]（Shu & Yi, Cadei et al., Neuhaus），部分 [REBUT]（Dawid & Skene 与本文主题不直接相关）。建议降为 should-fix。
- **R2-W6 (信息密度)**：[REBUT]——8 页限制下的合理权衡。
- 两位 reviewer 独立发现的共同问题：K≥3 gap、ASV-E-value 创新边界、abstract 1.4% vs 2.1% 不一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 490 · 2026-05-22T17:59:31.321567+00:00_

审稿报告已投递至 Research Director。

**Round 6 审稿完成。** 总结：

- **Overall: 3.5/5（Borderline Conference）**
- **1 项 Must-Fix**: Abstract 与正文 sign reversal rate 数值不一致（1.4% vs 2.1%）
- **6 项 Should-Fix**: Theorem 1 K≥3 命名、Abstract "structural property" overclaim、proportional effects 讨论不足、线性假设 scope mismatch、ASV vs E-value 差异化、Conjecture 1 与 Theorem 1 关系不清
- **5 项 Minor**: 缺失 3-4 篇引用、stress test 覆盖面、Table 1 caption、Algorithm 1 PPI++ guard、Figure 2 尺寸
- **核心共识**: 论文在线性框架内的贡献扎实完整，所有问题均可在 ARR revision 中修补。关键修改集中在措辞调整和少量补充讨论，不涉及实验重做或理论推翻。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 54

## Round 54

52 recorded events


### User

_source line 491 · 2026-05-22T23:35:47.421892+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-22T23:35:53.445106+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-22T23:35:53.496240+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-22T23:36:02.551773+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 495 · 2026-05-22T23:36:02.552559+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-22T23:36:08.626514+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-22T23:36:08.627039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-22T23:36:14.750344+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-22T23:36:15.704453+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-22T23:36:16.206864+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 501 · 2026-05-22T23:36:16.207314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-22T23:36:17.311360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-22T23:36:17.362048+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	
19	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{method}
39	
40	% ── Figures ──
41	
42	\begin{figure*}[t]
43	\centering
44	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
45	\vspace{-6pt}
46	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
47	\label{fig:dag_taxonomy}
48	\end{figure*}
49	
50	\begin{figure*}[t]
51	\centering
52	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
53	\vspace{-6pt}
54	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
55	\label{fig:bias_distribution}
56	\end{figure*}
57	
58	\input{experiments}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix_proofs}
66	
67	\end{document}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-22T23:36:23.585032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author"
  }
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-22T23:36:25.392434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-22T23:36:26.045346+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), the sign reversal rate is 2.1\%, exclusively in secondary coefficients---in all 23 empirical configurations tested, the primary treatment effect does not reverse---consistent with the largest-magnitude coefficient dominating the misclassification-induced weighted sum. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-22T23:36:26.045705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-22T23:36:26.397381+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-22T23:36:26.397886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-22T23:36:26.900300+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This assumption holds when the LLM annotates from source documents without access to outcome information. Violation pathways include outcome-conditional prompting, few-shot demonstrations encoding $A$--$Y$ associations, and retrieval-augmented pipelines surfacing $Y$-correlated documents; practitioners can diagnose violations by testing $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on a gold-labeled subset (see Limitations).
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
17	
18	\subsection{Multi-Class Bias Expressions}
19	\label{sec:bias_expressions}
20	
21	For each topology, we derive the probability limit of the naive estimator that substitutes $A^*$ for $A$. Let $\tau
…[truncated 11829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-22T23:36:26.900691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-22T23:36:27.352793+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause \emph{sign reversal} of at least one coefficient. Restricting to diagonal $\geq 0.7$ (typical LLM accuracy), the violation rate remains 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} b
…[truncated 6846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-22T23:36:27.353151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-22T23:36:28.307402+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 1831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-22T23:36:28.307800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-22T23:36:28.810368+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary treatment effect never reverses across all 23 configurations, but 61\% of exposure configurations reverse a secondary coefficient. Our analytical results assume linear SEMs; Appendix~\ref{sec:logistic_dgp} demonstrates that topology rankings and sign-flip patterns are preserved under logistic DGP ($|\Delta\,\text{SF}_\tau| < 0.02$), though FWL invariance is specific to linear models. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinear models (Appendix~\ref{sec:logistic_dgp}) remain open. We address misclassification of
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-22T23:36:28.811123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-22T23:36:29.062360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-22T23:36:29.113361+00:00_

File content (34174 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-22T23:36:29.113946+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},
31	  volume    = {50},
32	  number    = {1},
33	  pages     = {237--291},
34	  doi       = {10.1162/coli\_a\_00502},
35	}
36	
37	@incollection{bound2001measurement,
38	  author    = {Bound, John and Brown, Charles and Mathiowetz, Nancy},
39	  title     = {Measurement Error in Survey Data},
40	  booktitle = {Handbook of Econometrics},
41	  editor    = {Heckman, James J. and Leamer, Edward E.},
42	  year      = {2001},
43	  volume    = {5},
44	  chapter   = {59},
45	  pages     = {3705--3843},
46	  publisher = {Elsevier},
47	}
48	
49	@article{richardson1993bayesian,
50	  author    = {Richardson, Sylvia and Gilks, Walter R.},
51	  title     = {A {Bayesian} Approach to Measurement Error Problems in Epidemiology Using Conditional Independence Models},
52	  journal   = {Amer
…[truncated 16370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-22T23:36:32.627755+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"}]

Based on the search results, here's information about EMNLP 2026 call for papers with ARR submission guidelines and author requirements:

## Key Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## ARR Submission Guidelines

Papers must be submitted, at latest, by the ARR 2026 May cycle. The ARR submission deadline for long & short papers is May 25, 2026, and all authors must complete the author registration form by May 27, 2026 EoD AoE.

### Special ARR Policy for EMNLP 2026

Given that the ARR 2026 May cycle is aligned with two conference
…[truncated 1468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9042
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-22T23:36:39.204582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-22T23:36:40.158850+00:00_

File content (34174 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-22T23:36:40.661146+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 525 · 2026-05-22T23:36:40.661539+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-22T23:36:42.168090+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-22T23:36:42.624037+00:00_

-rw-r--r-- 1 ubuntu ubuntu 904568 May 22 23:08 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-22T23:36:42.624503+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-22T23:36:42.725182+00:00_

-rw-r--r-- 1 ubuntu ubuntu 20553 May 22 17:56 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-22T23:36:46.891893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-22T23:36:47.243763+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 8490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-22T23:36:47.746275+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "description": "Read review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "description": "Read review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-22T23:36:48.652847+00:00_

issues:
  # === Carried from Round 1-5 (resolved issues kept as history) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Theorem 1 使用 perspective function + convexity 证明路径：K=2 精确证明，K≥3 数值验证 worst-case <0.005。DPI 引用全部移除。"
    resolution_round: 5
    mentions:
      - round: 6
        reviewers: [R1, R2]
        note: "R6 两位 Reviewer 再次提出 K≥3 部分仅有数值验证却标为 Theorem 的命名问题（见 R6-M1）。此 issue 的核心关切在 R6 以新 ID R6-M1 重新跟踪。"

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写：83.4% 作为 K≥3 结构转变呈现，与 2.1% 并列。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
…[truncated 15601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-22T23:36:48.803986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-22T23:36:48.905476+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-22T23:37:23.700288+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-22T23:37:49.962951+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26262
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-22T23:37:50.114138+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "causal_annot_error_attrib",
  "round_number": "1",
  "text": "## 审稿任务：Reviewer 1 — 方法严谨性\n\n### Venue 信息\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL（论文已使用 `\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n### 论文路径\n- TeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf`\n\n### 你的审查侧重：方法严谨性（Soundness）\n\n请重点审查以下方面：\n\n1. **Bias expressions 推导正确性**：7 种 DAG 拓扑下的 bias 公式（Eq. 1-6）是否正确推导？assumptions 是否清晰声明？probability limit 表达式是否有遗漏或错误？\n\n2. **证明层级（Proved/Verified/Conjectured）三级体系**：\n   - Proposition 1(a)(b)(c) 的证明是否完整、条件是否充分？\n   - Theorem 1（envelope monotonicity, K=2）的证明是否严谨？proportional effects 假设 (f=λg) 是否合理？\n   - Proposition 2（K≥3 数值验证）的 20,000 matrices 是否足够？\n   - Conjecture 1（ε-approximate monotonicity）的数值验证（30,000 matrices）是否令人信服？ε<0.06 的 bound 是否稳健？\n   - **关键**：Theorem vs Proposition vs Conjecture 的命名是否与实际证明级别一致？K≥3 结果标为 Theorem 是否恰当？\n\n3. **ASV 框架理论基础**：\n   - C(δ) 参数化是否合理？δ_max 约束是否正确？\n   - 三种 ASV 类型（magnitude/significance/sign-flip）的定义是否严格？\n   - ASV 与 E-value 的技术差异是否足够明确？（这是一个反复被提出的问题）\n   - Envelope monotonicity 作为 ASV well-definedness 的前提条件是否充分论证？\n\n4. **FWL invariance 论证**：\n   - matrix-based corrections 对 4 种拓扑 \"provably ineffective\" 的证明是否完整？\n   - \"exactly 0% bias reduction\" 的声明是否准确？\n   - 线性模型限定是否在正文中清晰标注？\n\n5. **Non-differential misclassification 假设**：\n   - Definition 1 是否足够严格？\n   - 假设违反的讨论（outcome-conditional prompting 等）是否充分？\n   - 对 NLP 实践的适用性讨论是否到位？\n\n6. **数值/经验一致性**：\n   - Abstract 中的数字（sign reversal rate 等）与正文/实验部分是否一致？\n   - 检查所有关键数字的来源和计算基础\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，每条标注严重程度：CRITICAL / MAJOR / MINOR）\n- **Questions**（需要作者澄清的问题，标注 Q1, Q2, ...）\n- **Missing References**（如有遗漏的重要方法论引用）\n- **Detailed Comments**（逐节详细意见）\n- **Overall Assessment**（评分 1-5，按 EMNLP 2026 标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "causal_annot_error_attrib",
    "round_number": "1",
    "text": "## 审稿任务：Reviewer 1 — 方法严谨性\n\n### Venue 信息\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL（论文已使用 `\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n### 论文路径\n- TeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf`\n\n### 你的审查侧重：方法严谨性（Soundness）\n\n请重点审查以下方面：\n\n1. **Bias expressions 推导正确性**：7 种 DAG 拓扑下的 bias 公式（Eq. 1-6）是否正确推导？assumptions 是否清晰声明？probability limit 表达式是否有遗漏或错误？\n\n2. **证明层级（Proved/Verified/Conjectured）三级体系**：\n   - Proposition 1(a)(b)(c) 的证明是否完整、条件是否充分？\n   - Theorem 1（envelope monotonicity, K=2）的证明是否严谨？proportional effects 假设 (f=λg) 是否合理？\n   - Proposition 2（K≥3 数值验证）的 20,000 matrices 是否足够？\n   - Conjecture 1（ε-approximate monotonicity）的数值验证（30,000 matrices）是否令人信服？ε<0.06 的 bound 是否稳健？\n   - **关键**：Theorem vs Proposition vs Conjecture 的命名是否与实际证明级别一致？K≥3 结果标为 Theorem 是否恰当？\n\n3. **ASV 框架理论基础**：\n   - C(δ) 参数化是否合理？δ_max 约束是否正确？\n   - 三种 ASV 类型（magnitude/significance/sign-flip）的定义是否严格？\n   - ASV 与 E-value 的技术差异是否足够明确？（这是一个反复被提出的问题）\n   - Envelope monotonicity 作为 ASV well-definedness 的前提条件是否充分论证？\n\n4. **FWL invariance 论证**：\n   - matrix-based corrections 对 4 种拓扑 \"provably ineffective\" 的证明是否完整？\n   - \"exactly 0% bias reduction\" 的声明是否准确？\n   - 线性模型限定是否在正文中清晰标注？\n\n5. **Non-differential misclassification 假设**：\n   - Definition 1 是否足够严格？\n   - 假设违反的讨论（outcome-conditional prompting 等）是否充分？\n   - 对 NLP 实践的适用性讨论是否到位？\n\n6. **数值/经验一致性**：\n   - Abstract 中的数字（sign reversal rate 等）与正文/实验部分是否一致？\n   - 检查所有关键数字的来源和计算基础\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，每条标注严重程度：CRITICAL / MAJOR / MINOR）\n- **Questions**（需要作者澄清的问题，标注 Q1, Q2, ...）\n- **Missing References**（如有遗漏的重要方法论引用）\n- **Detailed Comments**（逐节详细意见）\n- **Overall Assessment**（评分 1-5，按 EMNLP 2026 标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-22T23:38:17.768740+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27654
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-22T23:38:17.919613+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "causal_annot_error_attrib",
  "round_number": "1",
  "text": "## 审稿任务：Reviewer 2 — 新颖性与完整性\n\n### Venue 信息\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL（论文已使用 `\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n### 论文路径\n- TeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf`\n\n### 你的审查侧重：新颖性与完整性（Novelty + Completeness）\n\n请重点审查以下方面：\n\n1. **贡献新颖性**：\n   - 三个 contributions（bias taxonomy, ASV, correction guidance）的新颖性评估\n   - 与 prior work 的差异是否清晰？特别是：\n     - 相对于 Brenner (1993), Dosemeci (1990), Veierød & Laake (2001) 在 polytomous misclassification 上的已知结果\n     - 相对于 Teblunthuis (2024) 在 classifier error + DAG 上的 binary treatment\n     - 相对于 Lee & Wood-Doughty (2024) 在 LLM + confounding 上的分析\n   - ASV 是否只是 E-value 的直接移植？三种 ASV 类型的方法论创新在哪里？\n   - \"首次跨 7 种拓扑系统比较\" 的声明是否成立？\n\n2. **Related Work 覆盖**：\n   - measurement error in causal inference 文献覆盖是否充分？\n   - LLM annotation 文献是否遗漏重要工作？\n   - sensitivity analysis 和 correction methods 文献是否完整？\n   - 检查是否遗漏任何 2024-2025 年的关键相关工作\n   - 引用格式：workshop paper 是否标注？preprint 状态是否更新？\n\n3. **实验设计与验证**：\n   - Monte Carlo 验证：100,000 matrices × 7 topologies 是否足够？$N=10,000$ 的选择是否合理？\n   - 经验验证：3 个 NLP 任务（HumAID K=10, VAST K=3, CivilComments K=2）是否有代表性？\n   - LLM 选择：4 个模型（Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct）是否足够？缺少商业 LLM（GPT-4, Claude）是否是重大缺陷？\n   - 23 配置 × 7 拓扑 = 161 scenarios：MAPE 1.6% 的声明是否可信？\n   - Cross-K robustness（K=5,7）验证是否充分？\n   - Logistic DGP 验证：是否充分说明定性结论在非线性下的稳健性？\n\n4. **写作质量与信息密度**：\n   - Abstract：是否信息过载？数字密度是否过高？\n   - Introduction：narrative 是否清晰？从 problem → gap → contribution 的逻辑链是否顺畅？\n   - Method section：符号系统是否一致？定义是否清晰？\n   - 整体 framing：83.4% sign reversal 的标题式呈现是否恰当？与 2.1%（realistic accuracy）的关系是否清晰传达？\n   - 论文广度 vs 深度的平衡：在 8 页限制下是否合理？\n\n5. **格式合规性**：\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且内容充分？\n   - 匿名性是否保持？（检查是否有 author-identifying 信息）\n   - 参考文献格式是否符合 ACL 标准？\n\n6. **\"Primary coefficient never reverses\" 声明**：\n   - Abstract 中这一声明的措辞是否准确？（\"structural property\" vs \"empirical regularity\"）\n   - 23 configurations 是否足以支撑这一声明？\n   - 是否有 formal sufficient conditions 或仅是 magnitude dominance 的启发式解释？\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，每条标注严重程度：CRITICAL / MAJOR / MINOR）\n- **Questions**（需要作者澄清的问题，标注 Q1, Q2, ...）\n- **Missing References**（如有遗漏的重要相关工作）\n- **Detailed Comments**（逐节详细意见）\n- **Overall Assessment**（评分 1-5，按 EMNLP 2026 标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "causal_annot_error_attrib",
    "round_number": "1",
    "text": "## 审稿任务：Reviewer 2 — 新颖性与完整性\n\n### Venue 信息\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long Paper），参考文献不限，Limitations 必须有但不计入页数\n- **模板**: ACL（论文已使用 `\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n\n### 论文路径\n- TeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_7/submitted.pdf`\n\n### 你的审查侧重：新颖性与完整性（Novelty + Completeness）\n\n请重点审查以下方面：\n\n1. **贡献新颖性**：\n   - 三个 contributions（bias taxonomy, ASV, correction guidance）的新颖性评估\n   - 与 prior work 的差异是否清晰？特别是：\n     - 相对于 Brenner (1993), Dosemeci (1990), Veierød & Laake (2001) 在 polytomous misclassification 上的已知结果\n     - 相对于 Teblunthuis (2024) 在 classifier error + DAG 上的 binary treatment\n     - 相对于 Lee & Wood-Doughty (2024) 在 LLM + confounding 上的分析\n   - ASV 是否只是 E-value 的直接移植？三种 ASV 类型的方法论创新在哪里？\n   - \"首次跨 7 种拓扑系统比较\" 的声明是否成立？\n\n2. **Related Work 覆盖**：\n   - measurement error in causal inference 文献覆盖是否充分？\n   - LLM annotation 文献是否遗漏重要工作？\n   - sensitivity analysis 和 correction methods 文献是否完整？\n   - 检查是否遗漏任何 2024-2025 年的关键相关工作\n   - 引用格式：workshop paper 是否标注？preprint 状态是否更新？\n\n3. **实验设计与验证**：\n   - Monte Carlo 验证：100,000 matrices × 7 topologies 是否足够？$N=10,000$ 的选择是否合理？\n   - 经验验证：3 个 NLP 任务（HumAID K=10, VAST K=3, CivilComments K=2）是否有代表性？\n   - LLM 选择：4 个模型（Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct）是否足够？缺少商业 LLM（GPT-4, Claude）是否是重大缺陷？\n   - 23 配置 × 7 拓扑 = 161 scenarios：MAPE 1.6% 的声明是否可信？\n   - Cross-K robustness（K=5,7）验证是否充分？\n   - Logistic DGP 验证：是否充分说明定性结论在非线性下的稳健性？\n\n4. **写作质量与信息密度**：\n   - Abstract：是否信息过载？数字密度是否过高？\n   - Introduction：narrative 是否清晰？从 problem → gap → contribution 的逻辑链是否顺畅？\n   - Method section：符号系统是否一致？定义是否清晰？\n   - 整体 framing：83.4% sign reversal 的标题式呈现是否恰当？与 2.1%（realistic accuracy）的关系是否清晰传达？\n   - 论文广度 vs 深度的平衡：在 8 页限制下是否合理？\n\n5. **格式合规性**：\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且内容充分？\n   - 匿名性是否保持？（检查是否有 author-identifying 信息）\n   - 参考文献格式是否符合 ACL 标准？\n\n6. **\"Primary coefficient never reverses\" 声明**：\n   - Abstract 中这一声明的措辞是否准确？（\"structural property\" vs \"empirical regularity\"）\n   - 23 configurations 是否足以支撑这一声明？\n   - 是否有 formal sufficient conditions 或仅是 magnitude dominance 的启发式解释？\n\n### 输出格式\n请按以下结构输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，每条标注严重程度：CRITICAL / MAJOR / MINOR）\n- **Questions**（需要作者澄清的问题，标注 Q1, Q2, ...）\n- **Missing References**（如有遗漏的重要相关工作）\n- **Detailed Comments**（逐节详细意见）\n- **Overall Assessment**（评分 1-5，按 EMNLP 2026 标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-22T23:38:19.484983+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 542 · 2026-05-22T23:38:36.892257+00:00_

圆桌审稿 Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性（bias 推导、证明层级、ASV、FWL） |
| Reviewer 2 | ✅ 已派发 | 新颖性/完整性（贡献定位、related work、实验、写作） |
| 视觉审查 | ✅ 已启动 | PDF 排版质量（非评分项，并行执行） |
| 外部审稿 | ⬜ 未配置 | 项目未启用 paperreview.ai |

**Venue 确认**：EMNLP 2026，ARR May cycle，deadline 2026-05-25（距今 3 天），Long Paper 正文 8 页限制，double-blind，ACL 模板。

等待两位 Reviewer 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 55

## Round 55

2 recorded events


### User

_source line 543 · 2026-05-22T23:44:17.957588+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — 新颖性与完整性

---

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 对一个及时且重要的问题提供了系统性的综合分析，跨7种DAG拓扑的比较具有原创价值，但个别贡献的理论深度有限，且8页限制下广度-深度权衡导致多处论证过于简略。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心claim有支撑但证明层次不齐：confounding/collider有解析证明，mediation/M-bias/front-door仅数值验证，K≥3的monotonicity仅为conjecture。线性SEM范围限制显著。 |
| Excitement | 3.0/5 | 问题timely且实用，跨拓扑系统比较是genuinely novel的综合贡献，但ASV本质是E-value的域迁移，FWL invariance虽有价值但推导直接。 |
| Reproducibility | 4.0/5 | 方法描述清晰，承诺代码开源，100K矩阵+23 LLM配置的实验设置可复现。但附录中部分推导步骤跳跃较大。 |
| Reviewer Confidence | 4/5 | 熟悉measurement error文献、因果推断和NLP annotation质量领域。 |

---

## Strengths

**S1. 系统性跨拓扑比较的原创价值**
在7种canonical DAG拓扑下系统比较同一confusion matrix的bias行为，这确实是prior work未做过的。Teblunthuis (2024)覆盖4种拓扑但限于binary；Lee & Wood-Doughty (2024)只分析confounding。"首次跨7种拓扑系统比较"的声明在我的检索范围内成立。Table 1的taxonomy和Figure 2的bias分布可视化有效传达了核心insight。

**S2. FWL invariance负结果有实用价值**
证明matrix-based correction对4种covariate拓扑无效（Appendix B.2, Table 4），这是一个非平凡的负结果。对该领域的practitioners直接有用：在选择correction方法前必须先识别拓扑。Section 4.5和Algorithm 1（Appendix, p.26）将此转化为actionable guidance。

**S3. 实验验证扎实**
23个真实LLM配置 × 7拓扑 = 161 scenarios，theory-MC agreement MAPE 1.6%（Table未显示但Section 4.2报告），cross-K robustness（K=5,7），logistic DGP验证（Appendix B.6），non-differential stress test（Appendix B.5），bootstrap ASV CI（Appendix B.7）——验证层次丰富，不是单一实验。

**S4. 方法论诚实的三层证据体系**
Section 3.2明确区分"analytically proved"、"numerically verified with zero violations"和"conjectured with ε-approximate bounds"——这种透明度在投稿论文中不常见，值得肯定。

**S5. 实际问题导向**
Figure 3 (F1 vs bias)有效说明了"F1不预测因果风险"的核心论点：在F1=0.614–0.690的窄区间内，bias跨拓扑变化10×。这对CSS实践者有直接的警示价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] ASV框架的方法论新颖性需更清晰阐述

- **具体位置**: Section 3.3, 特别是 "drawing on the E-value framework but parametrising K×K annotation error severity rather than unmeasured confounding strength"
- **问题**: ASV在方法论上与E-value的核心区别不够清晰。论文列举了三个差异：(1) ε-approximate monotonicity proof, (2) three ASV types, (3) FWL combination。但 (1) 是一个验证任务而非方法创新；(2) 本质是同一idea用不同threshold定义（magnitude/significance/sign-flip只是不同的stopping criterion）；(3) 是routing应用而非sensitivity analysis方法本身的创新。基础的参数化方法 C(δ)=(1-δ)I+δC₀ 是标准的单参数插值。
- **为什么影响接收**: Contribution 2是论文三大贡献之一。如果ASV仅是E-value在新domain的direct application，贡献降级为"应用"而非"方法"。审稿人需要理解ASV带来了什么E-value *不能直接提供的* 方法论insight。
- **建议修改方向**: 明确讨论为什么在annotation error domain中sensitivity analysis需要不同于confounding的处理——例如，monotonicity在confounding domain是trivially satisfied的（Cinelli & Hazlett 2020已证明），但在annotation error domain需要非平凡的验证（Theorem 1, Conjecture 1）。这个差异才是真正的方法论贡献，但当前写法将其淹没在了泛泛的"three key differences"中。

**N2** [CRITICAL] "Primary coefficient never reverses"声明的证据不足以支撑其prominence

- **具体位置**: Abstract ("in all 23 empirical configurations tested, the primary treatment effect does not reverse"), Introduction (Section 1, paragraph 2), Section 3.2 footnote 2
- **问题**: 这一声明在abstract和introduction中以近乎structural property的语气呈现，但实际上：
  - 仅基于23个经验配置（Section 4.4）——样本量极小
  - 解释仅为footnote 2中的heuristic（"magnitude dominance: 当|βⱼ|足够大时..."）——"足够大"没有formal bound
  - 论文自身称之为"empirical regularity"（Introduction paragraph 2），但abstract中没有用这个词
  - 未提供formal sufficient condition，也未讨论在什么参数regime下primary coefficient *会* reverse
- **为什么影响接收**: 这是论文最prominent的empirical claim之一（abstract标题位置），如果在更广泛的参数空间中不成立，会严重损害论文的可信度。一个adversarial reviewer可以构造counterexample：当primary和secondary coefficients magnitude接近时，primary也可能reverse。
- **建议修改方向**: (a) 降低claim的prominence——在abstract中明确标注"empirical regularity"而非暗示structural property；(b) 提供primary coefficient sign preservation的sufficient condition（即使是数值验证的）；(c) 讨论在什么β配置下这一regularity会break down（例如当max|βₖ|/min|βₖ|接近1时）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [MAJOR] 线性SEM范围限制对NLP/CSS受众过于显著

- **具体位置**: Section 3 全部推导, Appendix B.6 (logistic DGP)
- **问题**: 所有closed-form结果在linear SEM下推导。对于NLP/CSS目标受众，outcome通常是binary（情感正负）或ordinal——logistic/probit才是自然模型。Appendix B.6的logistic DGP验证仅检查sign-flip rates的stability（|ΔSFτ|<0.02），但：(a) FWL invariance *明确* 在非线性模型下不成立（论文自己在Section 4.5承认）；(b) 仅在confounding DAG下测试了FWL logistic breakdown（Table 5）——其他3个FWL-invariant拓扑未测试。
- **建议**: 在main text中更显著地标注scope restriction；补充其他FWL-invariant拓扑的logistic breakdown数据。

**W2** [MAJOR] 广度-深度权衡导致Method section关键推导过于简略

- **具体位置**: Section 3.2, Collider/M-bias/Front-door段落（各仅2-3句）
- **问题**: 7种拓扑中有3种（collider, M-bias, front-door）在main text中几乎没有数学推导，只有verbal description + 结论。Collider: "misclassification attenuates this spurious association because A* is a noisy proxy for A"——一句直觉解释。M-bias: "Misclassifying A weakens this adjustment, reducing the M-bias"——同样一句。读者必须翻到Appendix A.6–A.7才能看到实际推导。
- **为什么影响评分**: 对于声称"derive bias expressions for seven canonical topologies"的论文，main text应至少给出每个拓扑bias expression的closed-form（即使简化形式），而非仅给verbal summary。
- **建议**: 考虑用一个compact表格在main text中列出所有7个拓扑的bias expression（一行一个公式），目前只有confounding (Eq.1), exposure (Eq.2), mediation (Eq.3)有公式。

**W3** [MAJOR] 83.4% sign reversal数字的framing有误导性

- **具体位置**: Abstract, Figure 2 caption, Section 4.2 paragraph 2
- **问题**: 83.4%是在uniform Dirichlet(1,1,1) prior下得到的——这个prior对realistic confusion matrices极不合理（允许对角线接近0的矩阵）。虽然论文也报告了realistic accuracy (diagonal≥0.7)下的2.1%，但83.4%获得了headline treatment（abstract、figure caption、introduction都首先引用它）。这种framing可能让不细读的读者高估sign reversal的实际风险。
- **建议**: 在abstract和introduction中将realistic accuracy下的数字（2.1%）提前到83.4%之前，或至少同等prominence地呈现。明确标注83.4%是"pathological regime"下的理论上界。

**W4** [MINOR→MAJOR] 缺少商业LLM的实验配置

- **具体位置**: Section 4.4, "Four LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B-Instruct)"
- **问题**: 4个LLM全部是开源模型。在CSS实践中，GPT-4o和Claude是高频使用的annotator。由于论文的analytical结果是关于confusion matrix性质的（与具体LLM无关），这不影响理论贡献。但在empirical validation中，缺少商业LLM的confusion matrix样本可能限制结论的代表性——特别是如果商业LLM的confusion matrix结构与开源模型系统性不同。
- **建议**: 至少讨论为什么未包含商业LLM（是API cost还是reproducibility考虑？），并论证开源模型的confusion matrix结构已足够多样。

**W5** [MINOR] 引用格式问题

- **具体位置**: references.bib
- **问题**: 
  - Pangakis et al. (2023) 标为 "arXiv preprint" 但正文引用时未标注preprint状态
  - Cheng et al. (2024) 同上
  - Cadei et al. (2025) 同上
  - Baumann et al. (2025) 正确标注了"Preprint"（note字段）
  - Lee & Wood-Doughty (2024) 正确标注了"Workshop paper"
- **建议**: 统一标注所有preprint的状态，检查是否有preprint已正式发表。

---

## Questions（需要作者澄清）

**Q1**: Proposition 1(a)给出了confounding sign preservation的sufficient condition（sign(τ) = sign(τ+B_OV)），但这需要知道omitted variable bias B_OV的方向——这在实践中可能不可知。实践者如何在不知道B_OV的情况下判断sign preservation是否成立？

**Q2**: Table 9 (Appendix B.10)显示ASV ranking在不同β配置下会变化。特别是，confounding和front-door的相对fragility似乎依赖于效应量。这是否削弱了"vulnerability spectrum from IV to M-bias"作为universal ranking的声明？

**Q3**: Non-differential misclassification stress test (Appendix B.5, Table 7) 仅测试到r=0.1的departure。在few-shot prompting场景下（demonstrations编码了A-Y关联），differential程度可能远超0.1。是否有更大departure下的结果？

**Q4**: Bootstrap ASV CI (Appendix B.7) 中，IV的95% CI为[0.44, 1.29]——跨越了δ=1的boundary。这是否意味着对IV topology，ASV的point estimate本身就不可靠？

**Q5**: Conjecture 1声称ε<0.06对所有non-IV topologies成立。但ε=0.06对应的δ*误差为ε/η——η是什么量级？如果η很小（例如在weak effect下），ε/η可以很大，使ASV的实际精度远低于0.06。

**Q6**: Algorithm 1 (p.26) 在Step 1中使用"ASV exceeds 0.1"作为risk level threshold。这个0.1的选择依据是什么？是否对不同application domain应该使用不同的threshold？

---

## Missing References

1. **Wei, He, Li & Geng (2025)** "Multiply robust causal inference in the presence of an error-prone treatment" — Statistical Methods in Medical Research. 直接处理misclassified treatment的因果推断，与exposure topology相关。

2. 论文引用的 **Cheng, Mayya & Sedoc (2024)** 即 SILICON 论文，但其2025年2月有更新版本，应检查是否已正式发表。

3. **Demirel et al. (2024)** "Prediction-powered Generalization of Causal Inferences" (ICML 2024) — 虽然Cadei et al. 2025已引用，但Demirel et al.的generalization framework与PPI在causal setting的应用更直接相关。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高：包含至少8个specific数字（83.4%, 2.1%, 1.6%, 47.0%, -88%, 52.6%, ∞, 0%）。建议删减到3-4个最关键的数字。
- "structural possibility of sign reversal absent in the binary case"表述准确。
- "the primary treatment effect does not reverse"——如N2所述，措辞过于绝对。

### Introduction
- Paragraph 1的叙事逻辑清晰：LLM annotation普及 → multi-class是主流 → error propagation依赖structure和topology。
- Paragraph 2的K≥3 structural break论述有效，但83.4%的framing问题同W3。
- Contribution列表清晰，但Contribution 2的novel性需加强（同N1）。
- "154× across topologies"的binarization结果很striking，但仅出现在contribution列表中一句话，在experiments中未充分展开。

### Related Work
- 覆盖面广泛且组织合理（3个paragraph分别覆盖measurement error、LLM annotation、sensitivity analysis/correction）。
- 与prior work的差异化表述清晰："All analyze a single DAG topology; ours is the first to characterize how the same confusion matrix produces qualitatively different bias across seven topologies."
- 对Teblunthuis (2024)的定位准确（"most complete binary treatment, K=2, four DAGs"）。
- 遗漏：measurement error在non-parametric/semiparametric causal inference中的处理（如multiply robust estimation）。

### Method (Section 3)
- 符号系统基本一致（C_jk定义、starred-node notation）。
- Definition 1 (non-differential misclassification)清晰，violation pathways的讨论（outcome-conditional prompting, few-shot demonstrations, RAG）对NLP受众有价值。
- Proposition 1的条件分(a)(b)(c)结构清晰，但(a)的条件"sign(τ)=sign(τ+B_OV)"实际上是一个tautology（如果B_OV足够大可以reverse sign）——这是一个sufficient condition而非一个checkable condition（参见Q1）。
- Theorem 1 (K=2 monotonicity)的"proportional effects"条件（f=λg）限制了适用范围——论文称"the general case deviates by <0.02"，但这是empirical bound，对K≥3且non-proportional effects可能不成立。

### Experiments (Section 4)
- Theory-MC agreement (1.6% MAPE)很好，但这本质上是验证probability limit推导的正确性（large-N regime下应该趋近），不是验证finite-sample performance。
- Figure 3 (F1 vs bias) 是论文中最effective的可视化——直观说明了"topology matters more than accuracy"。
- Table 1格式清晰。但"Violation"列的定义需在caption或文中更清晰地解释——violation of what？（violation of the binary toward-null guarantee）
- Correction guidance (Section 4.5): "No single method dominates"的结论有价值，PPI++ -88% on M-bias是一个重要的warning。

### Conclusion & Limitations
- Limitations覆盖了主要的scope restrictions（non-differential assumption, correctly specified DAG, linear SEM, single annotator）。
- "Code for ASV computation and all experiments will be publicly released"——期待。

### Appendix
- 附录质量高，特别是Appendix A (proofs for Propositions 1-7)和Appendix B.3 (ClinicalBERT case study)。
- Appendix B.10 (ASV stability across DGP)是一个重要的robustness check，但结果（Table 9）显示ranking并非完全universal——值得在main text中提及。

---

## 主要优势总结
- 系统性是核心价值：7种拓扑的统一分析框架是genuinely novel的综合贡献
- FWL invariance负结果有immediate practical value
- 实验验证层次丰富（analytical → MC → empirical → logistic DGP → stress test → bootstrap）
- 问题高度timely：LLM annotation在CSS中的快速采用使得这一分析urgent
- 方法论诚实度高（三层证据体系、明确的scope restrictions）

---

**最终评分**: 3.5 (Borderline Conference)

**推荐理由**: 论文提出了一个timely且well-executed的系统性分析，跨拓扑比较有原创价值，实验验证扎实。主要concern是：(1) ASV的方法论新颖性需更convincing地与E-value区分；(2) "primary coefficient never reverses"的claim需与evidence强度匹配；(3) linear SEM scope restriction对NLP受众是一个non-trivial limitation。如果N1和N2能adequately address，评分可提升至4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 544 · 2026-05-22T23:44:27.486478+00:00_

Reviewer 2 审稿意见已收到，等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 545 · 2026-05-22T23:44:32.583133+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成概要**：

- **Overall**: 3.5/5 (Borderline Conference)
- **2个Must-Fix问题**：(1) ASV与E-value的方法论区分不足——论文需更清晰阐述annotation error domain中sensitivity analysis的非平凡挑战（如monotonicity不自动成立）；(2) "primary coefficient never reverses"的prominence与evidence强度不匹配——仅23个配置不足以支撑abstract级别的claim
- **5个Should-Fix问题**：线性SEM范围限制、Method section关键拓扑推导过于简略、83.4%数字的misleading framing、缺少商业LLM实验、部分preprint引用未标注状态
- **6个Questions**：涉及Proposition 1的实用性、ASV ranking的stability、non-differential stress test的departure range、bootstrap CI跨boundary问题、ε-approximate误差的实际精度、Algorithm 1 threshold选择依据
- **核心判断**：系统性跨拓扑比较有genuinely novel的综合价值，FWL invariance负结果有实用价值，实验验证扎实——若N1/N2能adequately address，评分可提升至4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 546 · 2026-05-22T23:44:37.947477+00:00_

收到 Reviewer 2 的审稿意见。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 57

## Round 57

6 recorded events


### User

_source line 547 · 2026-05-22T23:50:55.447514+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告 — 方法严谨性（Soundness）

**论文**: "Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction"
**Venue**: EMNLP 2026 (ACL ARR)
**审查侧重**: 方法严谨性

---

## Summary

本文针对 K-class 非差异性错分类（non-differential misclassification）在 7 种经典 DAG 拓扑下的偏差传播进行了系统性理论分析，推导了各拓扑的 probability limit 表达式，建立了 Annotation Sensitivity Values (ASV) 敏感性分析框架，并证明了 FWL 不变性导致矩阵校正方法在 4 种拓扑下完全无效。论文构建了三级证明层级（proved/verified/conjectured），并通过真实 LLM 混淆矩阵进行了经验验证。理论贡献扎实且框架新颖，但 K≥3 的关键结果依赖数值验证而非解析证明，proportional effects 假设限制了 Theorem 1 的适用范围，非差异性假设在 LLM 实践中的成立性需要更充分的讨论。

---

## Strengths

**S1. 系统性的 7 拓扑偏差分类体系（Section 3.2, Eqs. 1-6）**
先前工作（Brenner 1993; Vierod and Laake 2001）仅覆盖 1-2 种拓扑。本文首次在统一的线性 SEM 框架下推导全部 7 种拓扑的 bias 表达式，揭示了同一混淆矩阵在不同拓扑下产生质量上不同的偏差（attenuating vs. amplifying vs. sign-reversing）。这是一个重要的理论贡献。

**S2. 透明的三级证明层级**
论文明确区分了 analytically proved（Proposition 1, Theorem 1）、numerically verified（Proposition 2）和 conjectured（Conjecture 1）三个层次。这种学术诚实性在理论论文中值得肯定，避免了对未完全证明的结果做过度声称。

**S3. FWL 不变性结果（Section 4.5, Appendix B.2）**
证明矩阵校正方法（Naive/MLA 等）在 4 种协变量拓扑下完全无效（0% bias reduction），因为校正后的 D*M 与原始 D* 具有相同的列空间。这是一个优雅且实用的理论结果，对实践者选择校正方法有直接指导意义。该证明基于 FWL 定理的代数性质，论证完整。

**S4. ASV 框架设计合理**
将 E-value 的思路从 unmeasured confounding 推广到 annotation error 领域，C(δ)=(1-δ)I+δC₀ 的参数化提供了一个从完美分类到现实错分类的自然插值路径。三种 ASV 类型（magnitude/significance/sign-flip）覆盖了实践中最关心的三类脆弱性。

**S5. 经验验证充分**
使用 3 个真实 NLP 任务（HumAID K=10, VAST K=3, CivilComments K=2）× 4 个 LLM 的 23 种配置，得到 161 个 bias 场景，grand MAPE 1.65%。理论预测与 Monte Carlo 模拟的一致性令人信服。ClinicalBERT 案例研究（Appendix B.3）展示了端到端应用。

---

## Weaknesses

**W1. [MAJOR] Proposition 2 的命名与其证明级别不匹配**
- **具体位置**: Section 3.2 (page 5), Appendix B.11 (Tables 10-11)
- **问题**: 在数学惯例中，"Proposition" 指已有完整证明的命题。但 Proposition 2 的 "证明" 实质是对 20,000 组随机矩阵的数值验证（"numerical verification across 20,000 random (C₀, p, g) triples per K"）。论文虽在正文中标注了 "(Numerically verified)" 并在第三级层次中解释了差异，但 formal name 仍为 "Proposition"，可能误导读者认为 K≥3 的 envelope monotonicity 已被证明。
- **建议**: 将 "Proposition 2" 改为 "Numerical Finding 1" 或 "Empirical Proposition 2 (numerically verified)"，或在命题名称中明确标注未经解析证明。

**W2. [MAJOR] Theorem 1 的 proportional effects 假设 (f=λg) 过于严格**
- **具体位置**: Theorem 1 (page 5), Appendix A.4 (page 13)
- **问题**: Theorem 1 证明 K=2 时 envelope monotonicity 成立，但要求 "proportional effects"：f=λg，即混杂变量 A 对 T 和 Y 的效应函数线性成比例。这意味着 A 的各类别对治疗和结局的影响必须按同一比例缩放。在实际 NLP 应用中（如政治立场 5 分类作为混杂变量），不同立场对治疗的影响和对结局的影响很可能不成比例关系。论文在 "General case (non-proportional effects)" 段落（Appendix A.4, page 14）提供了数值验证，但承认 "strict monotonicity proof for the general case remains open"。
- **为什么影响接收**: Theorem 1 是 ASV well-definedness 的理论基础。如果 proportional effects 不成立，monotonicity 可能不保证，ASV 的路径依赖解释就可能失效。
- **建议**: (1) 讨论 proportional effects 在 NLP 实际场景中的合理性，给出哪些场景近似成立、哪些不成立的具体例子；(2) 量化 general case 中偏离 monotonicity 的程度（不仅是 "数值验证成立"，而是 worst-case deviation 的统计量）。

**W3. [MAJOR] ASV 对 C₀ 选择的敏感性未充分讨论**
- **具体位置**: Section 3.3 (page 5), Appendix B.7 (page 23)
- **问题**: ASV 值取决于参考混淆矩阵 C₀ 的选择。不同的 C₀ 估计方法（validation set, cross-validation, 人工标注子集）会产生不同的 ASV 排名。论文推荐了 bootstrap CI（B=1,000, Appendix B.7），但仅报告了点估计的 95% CI，未分析 C₀ 估计误差如何传播到 ASV 排名。如果 C₀ 的小幅扰动导致 ASV 拓扑排名翻转（如 exposure 和 IV 的相对脆弱性互换），ASV 作为实践指导工具的可靠性就会受损。
- **建议**: 增加 C₀ 扰动分析（perturbation analysis），展示在 C₀ 估计误差范围内 ASV 排名的稳定性。

**W4. [MAJOR] 非差异性错分类假设的压力测试覆盖不足**
- **具体位置**: Definition 1 (page 3), Limitations (page 8), Appendix B.5 (page 22)
- **问题**: 整个框架的理论有效性依赖于 P(A*|A,Y,Z)=P(A*|A)（Definition 1）。Appendix B.5 的压力测试仅覆盖了 mild violations（differential parameter r ≤ 0.1），在 r=0.1 时最大 sign-flip rate 为 7%（IV, K=3, low-quality C_kk=0.4）。但实际 LLM 标注中的差异性错分类可能远大于 r=0.1：
  - 当 prompt 中包含结局相关信息时（如文本同时提到 stance 和 engagement）
  - 当 LLM 的训练数据中 A-Y 关联被编码时
  - 当 retrieval-augmented 标注引入了 outcome-correlated documents 时
  论文在 Limitations 中定性讨论了这些场景，但缺乏对更大 r 值（如 r=0.3-0.5）的系统评估。
- **建议**: 扩展压力测试到 r ∈ {0.1, 0.2, 0.3, 0.5}，评估在强差异性错分类下框架结论（尤其是 sign preservation 和 ASV 排名）的退化程度。

**W5. [MINOR] 20,000 矩阵对 K≥3 参数空间的覆盖充分性**
- **具体位置**: Proposition 2 (page 5), Tables 10-11 (pages 25)
- **问题**: K=3 的列随机矩阵有 6 个自由参数（9 个元素减 3 个列和约束），K=5 有 20 个，K=7 有 42 个。每个 K 仅用 20,000 组随机矩阵验证，在高维参数空间的尾部区域覆盖可能不足。Table 10 显示 exposure 在 K=3 时有 485 次违反（约 4.85%），K=5 时降至 205，但 worst-case magnitude 为 0.009。虽然 worst-case 数值小，但能否保证没有遗漏更极端的违反点？
- **建议**: 补充覆盖性论证（如对比理论自由度与采样密度），或使用 adversarial search 寻找最大违反点。

**W6. [MINOR] Abstract 中 "154×" 倍数的来源不透明**
- **具体位置**: Abstract (page 1)
- **问题**: Abstract 声称 "K≥3 introduces a structural possibility of sign reversal varying 154× across topologies"。正文 Table 1 (page 7) 显示各拓扑 sign-flip rate：Exposure 83.4%, M-bias 53.2%, IV 52.6%，其余 0%。83.4%/0% 是无穷大而非 154×；如果取 non-zero 拓扑的比值 83.4/0.54（假设某拓扑有极小概率），可能得到 154×，但论文未在正文中给出该计算的明确来源。
- **建议**: 在正文中给出 154× 的具体计算基础（哪两个拓扑、哪个指标的比值），或修改 abstract 措辞。

**W7. [MINOR] 线性模型限定在正文中标注不够显著**
- **具体位置**: Section 3.1 (page 3), Section 4.5 (page 8), Appendix B.6 (page 23)
- **问题**: 整个理论框架限定于线性 SEM（Y 和 T 关于 A 的线性回归）。虽然 Appendix B.6 在 logistic DGP 下验证了主要模式保持（sign-flip rates 在线性和 logistic 下均为 0 对 5 个拓扑；IV 的差异 < 0.02），但正文 Section 3.1 仅在一句话中提到 "linear structural equations"。FWL invariance 结果（Section 4.5）和 "exactly 0% bias reduction" 声称严格依赖线性假设。
- **建议**: 在 Section 3.1 的 setup 中添加显著标注（如 bold 或 dedicated remark）说明线性模型限定，并在 Section 4.5 的 FWL 结果中重申。

---

## Questions

**Q1.** Theorem 1 证明的 Step 4 (Appendix A.4, page 13) 依赖 (C₀)_jj ≥ 1/2 的条件。这个条件在论文中如何确保？是否所有实际 LLM 混淆矩阵都满足此条件？当 K 较大时（如 K=10），对角元素可能低于 0.5——此时 Theorem 1 是否仍然适用？

**Q2.** ASV 的 C(δ) = (1-δ)I + δC₀ 采用线性插值。是否考虑过其他插值路径（如 matrix geometric interpolation 或 log-linear interpolation on the Simplex）？不同插值路径下 monotonicity 是否仍然成立？选择线性插值的理论或实践理由是什么？

**Q3.** Conjecture 1 排除了 IV 拓扑。Table 10 显示 IV 的 worst-case magnitude > 10^7（远超其他拓扑的 0.001-0.107）。能否解释 IV 拓扑 monotonicity 失败的根本原因？是否与 Wald estimator 的分母接近零有关？如果是，是否可以通过 regularized IV estimators 缓解？

**Q4.** 论文声称 "exclusively in secondary coefficients"（Abstract, page 1; Section 4.4, page 7）出现 sign reversal。这个 "exclusively" 声称是解析结果还是经验观察？如果是经验观察（仅基于 23 个配置），这个声称的泛化性如何保证？

**Q5.** FWL invariance 证明（Appendix B.2, page 20）假设校正矩阵 M 是可逆的（col(D*M) = col(D*) for invertible M）。当 C₀ 接近奇异时（某些类别几乎不被预测），M 可能接近奇异。此时 FWL invariance 是否仍然精确成立？

---

## Missing References

未发现重要遗漏引用。论文在测量误差理论（Carroll et al., 2006; Buonaccorsi, 2010; Gustafson, 2004）、NLP 标注（Gilardi et al., 2023; Baumann et al., 2025）、敏感性分析（VanderWeele and Ding, 2017; Cinelli and Hazlett, 2020）三个核心领域的引用覆盖充分。

可选补充：Fong, Hazlett, and Imai (2018) "Covariate balancing propensity score for a continuous treatment" 中的敏感性分析方法可能与 ASV 框架有方法论对话空间，但非必需。

---

## Detailed Comments

### Section 3.1 (Setup and Notation, page 3)
- Definition 1（非差异性错分类）的表述清晰严格。但 "for all j,k" 应注意：当 A 是有序分类变量时，non-differential 的含义可能需要额外讨论。论文隐含假设 A 是 nominal（非 ordinal），应明确。

### Section 3.2 (Multi-Class Bias Expressions, pages 3-5)
- **Confounding (Eq. 1)**: FWL 推导正确。Appendix A.3 给出了完整的 closed-form bias decomposition via group covariances，步骤清晰。
- **Exposure (Eq. 2)**: K=2 case 中 2×2 stochastic matrix with positive diagonal 不允许 sign reversal 的论证正确。K≥3 case 的 counterexample (Appendix A.8) 构造合理——对角占优的 3×3 列随机矩阵确实可以产生负权重。
- **Mediation (Eq. 3)**: M(C) 函数的构造和 indirect effect leakage 的分析完整。Appendix A.5 中关于 mediation leakage coefficient 的推导正确。
- **Proposition 1(a)(b)(c)**: (a) confounding sign preservation 的条件（C_kk > 0 for all k + proportional effects）是充分条件，证明正确。(b) collider sign preservation 的条件涉及 |B(C)| ≤ |τ_ind|（Appendix A.6, Propositions 6-7），推导合理但条件较强。(c) exposure sign reversal 的 counterexample 构造有效。

### Section 3.2 (Theorem 1 & Proposition 2, page 5)
- **Theorem 1** 的 proportional effects 证明（Appendix A.4）结构清晰：
  - Step 1: V_0(δ) 凸性 ✓
  - Step 2: 导数公式 ✓
  - Step 3: V₀''(0) ≤ 0 无条件成立 ✓
  - Step 4: (C₀)_jj ≥ 1/2 条件下 closed form monotonicity ✓
  - Step 5: 从凸性推导 monotonicity ✓
  
  但 Step 4 对 (C₀)_jj ≥ 1/2 的依赖需要讨论（见 Q1）。

### Section 3.3 (Annotation Sensitivity Values, page 5)
- C(δ) 参数化合理：δ=0 对应完美分类，δ=1 对应 C₀，单调增加的 δ 对应递增的错分类严重度。
- 三种 ASV 类型的定义严格。但 δ_mag 的定义中 threshold ε 的选择缺乏讨论——不同 ε 值会给出不同的 ASV 排名。
- ASV 与 E-value 的类比基本到位，但核心技术差异可更清晰：E-value 具有 causal bound interpretation（multiplier on unmeasured confounding），而 ASV 的 δ 是插值参数，不具有同等的因果解释。这不一定是缺点，但应明确讨论。

### Section 4 (Experiments, pages 5-8)
- Monte Carlo 验证（Section 4.1-4.2）规模合理（N=10,000, 100,000 random matrices）。
- 经验验证（Section 4.4）中 MAPE 1.65% 的理论-实证一致性令人信服。
- 校正方法比较（Section 4.5, Table 3）清晰展示了拓扑依赖的校正有效性。PPI++ 在 exposure/front-door 上表现优异符合理论预期。
- Figure 3 (page 8) 中 "Topology Determines Downstream Causal Bias" 的可视化有效支持了 core claim。

### Appendix B.2 (FWL Invariance, page 20)
- col(D*M) = col(D*) for invertible M 的论证代数上正确。
- 对 SIMEX 的处理：SIMEX 通过外推而非直接矩阵替换来校正偏差，论文声称 "SIMEX provides gold-free correction"（Table 3），但 SIMEX 在 FWL-invariant 拓扑上是否同样无效？Table 4 (page 21) 显示 MC-SIMEX 在 confounding 上仍有 0% bias reduction，确认 SIMEX 也受 FWL 限制。但 SIMEX 在 exposure 上达到 best performance，这与 FWL 不矛盾（exposure 是 treatment 拓扑，不受 FWL 限制）。

### Appendix B.5 (Non-Differential Assumption Stress Test, page 22)
- 测试设计合理（differential parameter r 控制 Y-conditional 偏移），但 r ≤ 0.1 的范围过窄（见 W4）。

### Appendix B.11 (Extended Conjecture Verification, pages 24-25)
- Table 10 的结果整体支持 Conjecture 1（非 IV 拓扑 worst-case magnitude 0.001-0.107）。
- 但 exposure 在 K=3 时 485/10,000 = 4.85% 的违反率并非可忽略——虽然 magnitude 小（0.009），但频率不低。这与 "ε-approximately monotonic" 的声称一致（违反存在但幅度小），但建议在正文中讨论这一频率。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 核心理论结果（Proposition 1, Theorem 1, FWL invariance）证明完整；K≥3 gap 透明标注但未解决；proportional effects 假设限制泛化性 |
| Excitement | 3.5/5 | 首次在统一框架下分析 LLM 标注误差×因果推断×DAG 拓扑的交叉问题，ASV 工具有实用价值；但线性 SEM 限定和 non-differential 假设限制了影响范围 |
| Reproducibility | 4/5 | 提供了清晰的数学推导、实验参数和算法伪代码（Algorithm 1），承诺公开代码；但部分数值验证的种子/精确实现细节可加强 |
| Reviewer Confidence | 4/5 | 仔细审查了所有 bias 表达式推导、Theorem 1 证明、FWL invariance 论证和数值验证方法论 |

## Overall Assessment

**Overall**: 3.5/5 — Borderline Conference

**一句话总结**: 理论框架新颖且核心证明扎实，但 K≥3 monotonicity 的解析证明缺失、proportional effects 假设的实用性论证不足、以及非差异性假设的压力测试范围过窄，使得最强声称的支撑尚不充分，建议补充后可达到 Conference 水准。

### 关键修改路径（从 3.5 到 4.0）：
1. 将 Proposition 2 重新命名以反映其数值验证性质
2. 增加 proportional effects 假设在 NLP 场景中合理性的实证讨论
3. 扩展非差异性假设压力测试到 r=0.3+
4. 补充 ASV 对 C₀ 扰动的敏感性分析


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-22T23:51:41.430628+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "causal_annot_error_attrib",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question。对每条使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Strengths\n- S1. 系统性的 7 拓扑偏差分类体系（Section 3.2, Eqs. 1-6）——首次在统一线性 SEM 框架下推导全部 7 种拓扑的 bias 表达式\n- S2. 透明的三级证明层级（proved/verified/conjectured）\n- S3. FWL 不变性结果（Section 4.5, Appendix B.2）——证明矩阵校正方法在 4 种协变量拓扑下完全无效\n- S4. ASV 框架设计合理——C(δ) 参数化提供自然插值路径\n- S5. 经验验证充分——23 种配置 × 7 拓扑 = 161 scenarios，MAPE 1.65%\n\n### Weaknesses\n\n**W1. [MAJOR] Proposition 2 的命名与其证明级别不匹配**\nProposition 2 的\"证明\"实质是 20,000 组随机矩阵的数值验证，但 formal name 为\"Proposition\"，可能误导读者认为 K≥3 envelope monotonicity 已被证明。建议改为\"Numerical Finding 1\"或\"Empirical Proposition 2\"。\n\n**W2. [MAJOR] Theorem 1 的 proportional effects 假设 (f=λg) 过于严格**\nTheorem 1 要求 f=λg（混杂变量 A 对 T 和 Y 的效应函数线性成比例），在实际 NLP 应用中（如政治立场 5 分类）不太可能严格成立。Appendix A.4 的 general case 数值验证承认 \"strict monotonicity proof for the general case remains open\"。如果 proportional effects 不成立，monotonicity 可能不保证，ASV 的路径依赖解释就可能失效。\n\n**W3. [MAJOR] ASV 对 C₀ 选择的敏感性未充分讨论**\n不同 C₀ 估计方法（validation set, cross-validation, 人工标注子集）会产生不同的 ASV 排名。论文推荐 bootstrap CI（B=1,000, Appendix B.7），但未分析 C₀ 估计误差如何传播到 ASV 排名。需增加 C₀ 扰动分析。\n\n**W4. [MAJOR] 非差异性错分类假设的压力测试覆盖不足**\nAppendix B.5 的压力测试仅覆盖 r ≤ 0.1 的 mild violations。实际 LLM 标注中差异性错分类可能远大于 r=0.1（如 prompt 包含结局相关信息、LLM 训练数据编码 A-Y 关联等）。建议扩展到 r ∈ {0.1, 0.2, 0.3, 0.5}。\n\n**W5. [MINOR] 20,000 矩阵对 K≥3 参数空间的覆盖充分性**\nK=3 有 6 个自由参数，K=7 有 42 个。每个 K 仅 20,000 组随机矩阵，高维参数空间尾部覆盖可能不足。\n\n**W6. [MINOR] Abstract 中 \"154×\" 倍数的来源不透明**\nAbstract 声称 binarization bias 变化 154×，但正文未给出具体计算基础。\n\n**W7. [MINOR] 线性模型限定在正文中标注不够显著**\nSection 3.1 仅一句话提到 \"linear structural equations\"，FWL invariance 严格依赖线性假设但标注不够突出。\n\n### Questions\n- Q1. Theorem 1 的 (C₀)_jj ≥ 1/2 条件在 K=10 时是否满足？\n- Q2. ASV 的 C(δ) 线性插值 vs. 其他插值路径（geometric/log-linear），monotonicity 是否仍成立？\n- Q3. IV 拓扑 monotonicity 失败的根本原因？是否与 Wald estimator 分母接近零有关？\n- Q4. \"exclusively in secondary coefficients\" sign reversal 是解析结果还是经验观察？泛化性如何？\n- Q5. FWL invariance 当 C₀ 接近奇异时是否精确成立？\n\n### Missing References\n未发现重要遗漏。可选补充 Fong, Hazlett, and Imai (2018)。\n\n### Overall: 3.5/5 (Borderline Conference)\n\n---\n\n请对以上每个 W1-W7 和 Q1-Q5 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "causal_annot_error_attrib",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question。对每条使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Strengths\n- S1. 系统性的 7 拓扑偏差分类体系（Section 3.2, Eqs. 1-6）——首次在统一线性 SEM 框架下推导全部 7 种拓扑的 bias 表达式\n- S2. 透明的三级证明层级（proved/verified/conjectured）\n- S3. FWL 不变性结果（Section 4.5, Appendix B.2）——证明矩阵校正方法在 4 种协变量拓扑下完全无效\n- S4. ASV 框架设计合理——C(δ) 参数化提供自然插值路径\n- S5. 经验验证充分——23 种配置 × 7 拓扑 = 161 scenarios，MAPE 1.65%\n\n### Weaknesses\n\n**W1. [MAJOR] Proposition 2 的命名与其证明级别不匹配**\nProposition 2 的\"证明\"实质是 20,000 组随机矩阵的数值验证，但 formal name 为\"Proposition\"，可能误导读者认为 K≥3 envelope monotonicity 已被证明。建议改为\"Numerical Finding 1\"或\"Empirical Proposition 2\"。\n\n**W2. [MAJOR] Theorem 1 的 proportional effects 假设 (f=λg) 过于严格**\nTheorem 1 要求 f=λg（混杂变量 A 对 T 和 Y 的效应函数线性成比例），在实际 NLP 应用中（如政治立场 5 分类）不太可能严格成立。Appendix A.4 的 general case 数值验证承认 \"strict monotonicity proof for the general case remains open\"。如果 proportional effects 不成立，monotonicity 可能不保证，ASV 的路径依赖解释就可能失效。\n\n**W3. [MAJOR] ASV 对 C₀ 选择的敏感性未充分讨论**\n不同 C₀ 估计方法（validation set, cross-validation, 人工标注子集）会产生不同的 ASV 排名。论文推荐 bootstrap CI（B=1,000, Appendix B.7），但未分析 C₀ 估计误差如何传播到 ASV 排名。需增加 C₀ 扰动分析。\n\n**W4. [MAJOR] 非差异性错分类假设的压力测试覆盖不足**\nAppendix B.5 的压力测试仅覆盖 r ≤ 0.1 的 mild violations。实际 LLM 标注中差异性错分类可能远大于 r=0.1（如 prompt 包含结局相关信息、LLM 训练数据编码 A-Y 关联等）。建议扩展到 r ∈ {0.1, 0.2, 0.3, 0.5}。\n\n**W5. [MINOR] 20,000 矩阵对 K≥3 参数空间的覆盖充分性**\nK=3 有 6 个自由参数，K=7 有 42 个。每个 K 仅 20,000 组随机矩阵，高维参数空间尾部覆盖可能不足。\n\n**W6. [MINOR] Abstract 中 \"154×\" 倍数的来源不透明**\nAbstract 声称 binarization bias 变化 154×，但正文未给出具体计算基础。\n\n**W7. [MINOR] 线性模型限定在正文中标注不够显著**\nSection 3.1 仅一句话提到 \"linear structural equations\"，FWL invariance 严格依赖线性假设但标注不够突出。\n\n### Questions\n- Q1. Theorem 1 的 (C₀)_jj ≥ 1/2 条件在 K=10 时是否满足？\n- Q2. ASV 的 C(δ) 线性插值 vs. 其他插值路径（geometric/log-linear），monotonicity 是否仍成立？\n- Q3. IV 拓扑 monotonicity 失败的根本原因？是否与 Wald estimator 分母接近零有关？\n- Q4. \"exclusively in secondary coefficients\" sign reversal 是解析结果还是经验观察？泛化性如何？\n- Q5. FWL invariance 当 C₀ 接近奇异时是否精确成立？\n\n### Missing References\n未发现重要遗漏。可选补充 Fong, Hazlett, and Imai (2018)。\n\n### Overall: 3.5/5 (Borderline Conference)\n\n---\n\n请对以上每个 W1-W7 和 Q1-Q5 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-22T23:52:21.826844+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 40396
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-22T23:52:22.028561+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "causal_annot_error_attrib",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix、Question。对每条使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Strengths\n- S1. 系统性跨拓扑比较的原创价值——\"首次跨7种拓扑系统比较\"成立\n- S2. FWL invariance 负结果有实用价值\n- S3. 实验验证扎实（23 LLM配置 × 7拓扑 = 161 scenarios，MAPE 1.6%）\n- S4. 方法论诚实的三层证据体系\n- S5. 实际问题导向——Figure 3 (F1 vs bias) 有效说明 \"F1不预测因果风险\"\n\n### Must-Fix 问题\n\n**N1 [CRITICAL] ASV 框架的方法论新颖性需更清晰阐述**\nASV 与 E-value 的核心区别不够清晰。论文列举的三个差异中：(1) ε-approximate monotonicity proof 是验证任务非方法创新；(2) three ASV types 本质是同一 idea 用不同 threshold；(3) FWL combination 是 routing 应用。基础参数化 C(δ)=(1-δ)I+δC₀ 是标准单参数插值。如果 ASV 仅是 E-value 在新 domain 的 direct application，贡献降级为\"应用\"而非\"方法\"。建议明确讨论为什么在 annotation error domain 中 sensitivity analysis 需要不同于 confounding 的处理——monotonicity 在 confounding domain 是 trivially satisfied（Cinelli & Hazlett 2020 已证明），但在 annotation error domain 需要 Theorem 1 + Conjecture 1。\n\n**N2 [CRITICAL] \"Primary coefficient never reverses\" 声明的 evidence 不足以支撑其 prominence**\n仅基于 23 个经验配置，解释仅为 footnote 2 的 heuristic（\"magnitude dominance\"），无 formal sufficient condition。Abstract 中以近乎 structural property 语气呈现但实际是 empirical regularity。建议：(a) 降低 claim prominence，明确标注\"empirical regularity\"；(b) 提供 sufficient condition；(c) 讨论 break-down regime。\n\n### Should-Fix 问题\n\n**W1 [MAJOR] 线性 SEM 范围限制对 NLP/CSS 受众过于显著**\nFWL invariance 明确在非线性下不成立（论文自己承认）；Appendix B.6 logistic DGP 验证仅检查 sign-flip rates stability 但其他 3 个 FWL-invariant 拓扑未测试 logistic breakdown。\n\n**W2 [MAJOR] 广度-深度权衡导致 Method section 关键推导过于简略**\n7 种拓扑中 3 种（collider, M-bias, front-door）在 main text 中几乎没有数学推导，只有 verbal description。论文声称 \"derive bias expressions for seven canonical topologies\" 但 main text 仅给出 confounding/exposure/mediation 的公式。\n\n**W3 [MAJOR] 83.4% sign reversal 数字的 framing 有误导性**\n83.4% 在 uniform Dirichlet(1,1,1) prior 下得到——对 realistic confusion matrices 极不合理。论文给了 headline treatment（abstract/figure caption/introduction 首先引用），而 realistic accuracy 下 2.1% 获得较低 prominence。\n\n**W4 [MINOR→MAJOR] 缺少商业 LLM 的实验配置**\n4 个 LLM 全部开源。CSS 实践中 GPT-4o/Claude 高频使用。缺少商业 LLM 可能限制结论代表性。\n\n**W5 [MINOR] 引用格式问题**\nPangakis et al. (2023)、Cheng et al. (2024)、Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态。\n\n### Questions\n- Q1. Proposition 1(a) 的 sufficient condition 需要知道 B_OV 方向——实践中如何判断？\n- Q2. Table 9 (Appendix B.10) 显示 ASV ranking 依赖 β 配置，是否削弱 \"universal ranking\" 声明？\n- Q3. Non-differential stress test 仅 r=0.1，few-shot prompting 下 differential 程度可能远超。\n- Q4. Bootstrap ASV CI for IV 跨越 δ=1 boundary——ASV point estimate 是否不可靠？\n- Q5. Conjecture 1 的 ε/η 实际精度——η 小时 δ* 误差可以很大。\n- Q6. Algorithm 1 的 0.1 threshold 选择依据？\n\n### Missing References\n- Wei, He, Li & Geng (2025) \"Multiply robust causal inference in the presence of an error-prone treatment\"\n- Demirel et al. (2024) \"Prediction-powered Generalization of Causal Inferences\" (ICML 2024)\n- Cheng et al. (2024) 2025年2月更新版本\n\n### Overall: 3.5/5 (Borderline Conference)\n\n---\n\n请对以上 N1, N2, W1-W5, Q1-Q6 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "causal_annot_error_attrib",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix、Question。对每条使用 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供证据，cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Strengths\n- S1. 系统性跨拓扑比较的原创价值——\"首次跨7种拓扑系统比较\"成立\n- S2. FWL invariance 负结果有实用价值\n- S3. 实验验证扎实（23 LLM配置 × 7拓扑 = 161 scenarios，MAPE 1.6%）\n- S4. 方法论诚实的三层证据体系\n- S5. 实际问题导向——Figure 3 (F1 vs bias) 有效说明 \"F1不预测因果风险\"\n\n### Must-Fix 问题\n\n**N1 [CRITICAL] ASV 框架的方法论新颖性需更清晰阐述**\nASV 与 E-value 的核心区别不够清晰。论文列举的三个差异中：(1) ε-approximate monotonicity proof 是验证任务非方法创新；(2) three ASV types 本质是同一 idea 用不同 threshold；(3) FWL combination 是 routing 应用。基础参数化 C(δ)=(1-δ)I+δC₀ 是标准单参数插值。如果 ASV 仅是 E-value 在新 domain 的 direct application，贡献降级为\"应用\"而非\"方法\"。建议明确讨论为什么在 annotation error domain 中 sensitivity analysis 需要不同于 confounding 的处理——monotonicity 在 confounding domain 是 trivially satisfied（Cinelli & Hazlett 2020 已证明），但在 annotation error domain 需要 Theorem 1 + Conjecture 1。\n\n**N2 [CRITICAL] \"Primary coefficient never reverses\" 声明的 evidence 不足以支撑其 prominence**\n仅基于 23 个经验配置，解释仅为 footnote 2 的 heuristic（\"magnitude dominance\"），无 formal sufficient condition。Abstract 中以近乎 structural property 语气呈现但实际是 empirical regularity。建议：(a) 降低 claim prominence，明确标注\"empirical regularity\"；(b) 提供 sufficient condition；(c) 讨论 break-down regime。\n\n### Should-Fix 问题\n\n**W1 [MAJOR] 线性 SEM 范围限制对 NLP/CSS 受众过于显著**\nFWL invariance 明确在非线性下不成立（论文自己承认）；Appendix B.6 logistic DGP 验证仅检查 sign-flip rates stability 但其他 3 个 FWL-invariant 拓扑未测试 logistic breakdown。\n\n**W2 [MAJOR] 广度-深度权衡导致 Method section 关键推导过于简略**\n7 种拓扑中 3 种（collider, M-bias, front-door）在 main text 中几乎没有数学推导，只有 verbal description。论文声称 \"derive bias expressions for seven canonical topologies\" 但 main text 仅给出 confounding/exposure/mediation 的公式。\n\n**W3 [MAJOR] 83.4% sign reversal 数字的 framing 有误导性**\n83.4% 在 uniform Dirichlet(1,1,1) prior 下得到——对 realistic confusion matrices 极不合理。论文给了 headline treatment（abstract/figure caption/introduction 首先引用），而 realistic accuracy 下 2.1% 获得较低 prominence。\n\n**W4 [MINOR→MAJOR] 缺少商业 LLM 的实验配置**\n4 个 LLM 全部开源。CSS 实践中 GPT-4o/Claude 高频使用。缺少商业 LLM 可能限制结论代表性。\n\n**W5 [MINOR] 引用格式问题**\nPangakis et al. (2023)、Cheng et al. (2024)、Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态。\n\n### Questions\n- Q1. Proposition 1(a) 的 sufficient condition 需要知道 B_OV 方向——实践中如何判断？\n- Q2. Table 9 (Appendix B.10) 显示 ASV ranking 依赖 β 配置，是否削弱 \"universal ranking\" 声明？\n- Q3. Non-differential stress test 仅 r=0.1，few-shot prompting 下 differential 程度可能远超。\n- Q4. Bootstrap ASV CI for IV 跨越 δ=1 boundary——ASV point estimate 是否不可靠？\n- Q5. Conjecture 1 的 ε/η 实际精度——η 小时 δ* 误差可以很大。\n- Q6. Algorithm 1 的 0.1 threshold 选择依据？\n\n### Missing References\n- Wei, He, Li & Geng (2025) \"Multiply robust causal inference in the presence of an error-prone treatment\"\n- Demirel et al. (2024) \"Prediction-powered Generalization of Causal Inferences\" (ICML 2024)\n- Cheng et al. (2024) 2025年2月更新版本\n\n### Overall: 3.5/5 (Borderline Conference)\n\n---\n\n请对以上 N1, N2, W1-W5, Q1-Q6 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-22T23:52:23.540047+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1511
}
```

</details>

---


### Assistant

_source line 552 · 2026-05-22T23:52:26.023033+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 553 · 2026-05-22T23:52:28.631425+00:00_

[Reviewer 1 审稿结果]:
Reviewer 1 审稿完成。核心发现：

- **Soundness 4/5** — Proposition 1、Theorem 1、FWL invariance 的证明完整正确；K≥3 monotonicity gap 透明但未解决
- **Excitement 3.5/5** — 首次统一分析 7 种 DAG 拓扑下 LLM 标注误差传播，ASV 框架有实用价值
- **Overall 3.5/5 (Borderline Conference)**

4 个 MAJOR 问题：(1) Proposition 2 命名与数值验证性质不匹配；(2) Theorem 1 的 proportional effects 假设过强且缺乏 NLP 场景合理性论证；(3) ASV 对 C₀ 选择的敏感性未分析；(4) 非差异性假设压力测试仅覆盖 r≤0.1，范围过窄。5 个 Questions 要求作者澄清。已提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 554 · 2026-05-22T23:52:33.791566+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 555 · 2026-05-22T23:54:23.388113+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Weaknesses 逐条回应

**[AGREE] R1-W1: Proposition 2 的命名与证明级别不匹配**

同意。Proposition 2（Section 3.3, p.5）的完整文本是 "For K≥3 under the same conditions, numerical verification across 20,000 random (C₀,p,g) triples per K shows worst-case deviations < 0.005 from strict monotonicity"——这明确是数值验证，不是解析证明。在数学文献中 "Proposition" 意味着已证结果。论文自身在 Section 3.2 末尾其实已建立了清晰的三层体系（proved / numerically verified / conjectured），Proposition 2 应归入第二层而非第一层。

补充发现：Conjecture 1（同在 Section 3.3）的命名反而是恰当的——同样基于数值验证但正确使用了 "Conjecture"。这种命名不一致使 Proposition 2 的问题更加突出。建议改为 "Numerical Result 1" 或在 Proposition 2 正文中显式标注 "supported by numerical evidence; analytic proof remains open"（类似 Section 3.2 对 mediation/M-bias/front-door 的处理方式）。

---

**[AGREE with nuance] R1-W2: Theorem 1 的 proportional effects 假设 (f=λg) 过于严格**

基本同意 concern 的方向，但程度判断略有不同。

同意点：f=λg 要求 A 对 T 和 Y 的类别效应严格线性成比例，在实际 NLP 场景（如政治立场 K=5）中确实不太可能精确成立。Appendix A.4 承认 "strict monotonicity proof for the general case remains open"。

补充视角：论文实际上已做了 general case 的数值验证——Appendix A.4 中用 20,000 组 random (C₀,p,g) 测试了 non-proportional effects，报告 worst-case deviation < 0.005。更重要的是，Proposition 2 声称的正是 general K≥3 case 的数值验证结果。所以 R1 的 concern 和我的回应是：proportional effects 是 *Theorem 1* 的限制（K=2 的解析证明需要它），但 ASV 的路径解释不完全依赖 Theorem 1——Proposition 2 和 Conjecture 1 提供了 general case 的数值支撑。

真正的风险不是"monotonicity 完全失效"而是"monotonicity 存在小的 deviation，导致 ASV 的 δ* 有 bounded error"——论文在 Conjecture 1 后已讨论这一点（"δ* may differ from the true threshold by at most ε/η"）。但 R1 的关键追问是合理的：ε/η 在 weak effect 下可以很大（参见我的 Q5）。

---

**[AGREE] R1-W3: ASV 对 C₀ 选择的敏感性未充分讨论**

同意。Appendix B.7 的 bootstrap CI 分析（δ* = 0.94 [0.60, 1.36] for exposure; 0.75 [0.44, 1.29] for IV）回答了 "给定 C₀ 估计方法，sampling uncertainty 有多大"，但没有回答 "不同 C₀ 估计方法（validation set vs. cross-validation vs. few-shot gold subset）是否产生系统性不同的 ASV"。

补充观察：IV 的 95% CI [0.44, 1.29] 跨越 δ=1 boundary——这意味着在 IV 拓扑下，ASV 的 point estimate 已经不可靠，bootstrap CI 的宽度反映了 Wald estimator 的 ratio instability。这进一步说明了 C₀ uncertainty 对 fragile topologies 的影响被低估。论文应至少讨论 C₀ 估计方法选择对 ranking stability 的影响——即使不做完整的 sensitivity analysis，至少应说明在什么条件下 ranking 是 robust to C₀ estimation method。

---

**[AGREE] R1-W4: 非差异性错分类压力测试覆盖不足**

强烈同意。这与我在 Round 1 审稿中提出的 Q3 一致。

Appendix B.5 (Table 7) 仅测试 r ∈ {0, 0.05, 0.1}，最大 departure 为 r=0.1。Table 7 显示在 r=0.1 时 sign-flip rate 仅从 0% 增加到约 5-18%（依拓扑而定），violation rate 增加约 7 个百分点。但 r=0.1 是 mild violation——在实际场景中：

- Few-shot demonstrations 编码了 outcome-treatment 关联 → differential misclassification 可能 substantial
- LLM 训练数据（如 RLHF reward models）编码了 implicit A-Y correlations
- RAG 管道中检索到的文档可能包含 outcome signal

扩展到 r ∈ {0.2, 0.3, 0.5} 是最低要求。此外，当前 stress test 的 r 定义（Section B.5 "differential misclassification parameter r"）是均匀扰动所有 off-diagonal entries——实际 violation 可能是 structured（某些类别的 differential 更大），需要更 realistic 的 violation 模型。

---

**[REBUT] R1-W5: 20,000 矩阵对 K≥3 参数空间的覆盖充分性**

部分不同意。R1 的计算是正确的——K=3 有 6 free params，K=7 有 42 free params——但覆盖充分性的判断需要考虑：

1. **验证目标是 monotonicity violation 的存在性，不是 distribution estimation。** 如果 20,000 样本中 zero violations（worst-case deviation < 0.005），这提供了 ≥ 1 - (1-p)^20000 的 confidence——对 p=0.001（0.1% violation rate），confidence > 99.99%。问题只在于 violation 集中在 Dirichlet 无法覆盖的参数空间角落。

2. **Conjecture 1 使用了 30,000 matrices per topology，且 K ∈ {3,5,7}，τ ∈ {0.1, 0.5, 1.0, 2.0, 5.0}**——这是 30,000 × 3 × 5 = 450,000 configurations per topology，覆盖度远超 R1 引用的 20,000。

3. **Appendix B.8 (Cross-K Robustness)** 额外用 100,000 matrices 验证了 K=5,7 的 structural patterns。

4. **尾部覆盖的真正 concern** 是极端 C₀（如近排列矩阵），但这些正是 realistic accuracy (diagonal ≥ 0.7) 过滤排除的区域。

综上，20,000 对 Proposition 2 的验证目标是 adequate 的。R1 的 concern 更适合作为 caveat 而非 weakness。

---

**[AGREE] R1-W6: "154×" 倍数的来源不透明**

同意。Introduction (Contribution 1) 中 "Binarization amplifies the gap: collapsing K=3 to binary introduces additional bias varying 154× across topologies" 是一个 striking claim，但：

- 正文 Section 4 没有 binarization 实验的结果展示
- Appendix B.1 讨论了 binarization collapse 并有 Figure 6 (p.21)，但我在 Figure 6 的 caption 和周围文本中未找到 "154×" 这个具体数字的明确计算基础
- 读者无法从 main text verify 这个数字

建议至少在 Appendix B.1 中给出 154× 的具体计算（哪两个拓扑的 binarization bias 之比产生了 154×？最大 vs 最小 bias 的具体值是多少？），并在 main text 中 cite appendix reference。

---

**[AGREE] R1-W7: 线性模型限定在正文中标注不够显著**

同意，与我在 Round 1 中提出的 W1 (MAJOR) 一致。Section 3.1 在 "linear structural equation models" 上仅一句话带过。对于面向 NLP/CSS 受众的论文，应在以下位置显著标注 scope：
- Section 3 开头（当前只在 Introduction Contribution 1 中提到 "linear structural equation models"）
- FWL invariance 结果旁（Section 4.5 确实说了 "Under linear OLS"，但可以更强调这是一个 strict requirement）
- Section 5 (Conclusion) 的第二句话提到了 "linear SEMs"，这是好的，但来得太晚

---

### Questions 逐条回应

**[AGREE] R1-Q1: Theorem 1 的 (C₀)_jj ≥ 1/2 条件在 K=10 时是否满足？**

好问题。对 K=10 (HumAID)，如果 LLM 对某些 rare classes 的 per-class accuracy 低于 50%（这在 10 分类中完全可能），Theorem 1 的前提条件就不满足。论文应该报告 HumAID confusion matrices 中 (C₀)_jj 的 per-class 分布，验证条件是否对所有 j 成立。

补充：从 Appendix B.9 (ASV Diagnostic Results) 可以间接推断——如果 55.4% 的 HumAID scenarios 被标记为 magnitude-unsafe，说明部分 confusion matrices 确实有低 diagonal entries。但这不直接回答 Theorem 1 的条件是否满足。

---

**[REBUT] R1-Q2: C(δ) 线性插值 vs. 其他插值路径的 monotonicity**

这个问题虽然在数学上有趣，但在实践中 relevance 有限。理由：

1. C(δ) = (1-δ)I + δC₀ 的线性插值有明确的物理解释：δ=0 是 perfect classification，δ=1 是 observed accuracy C₀，δ>1 是 worse-than-observed（如果 non-negativity 允许）。这条路径是 severity axis 上的自然选择。

2. Geometric interpolation (C(δ) = C₀^δ) 在 matrix space 中不保证 column-stochastic 性质（除非 C₀ 本身是 doubly stochastic），所以物理上不可行。

3. Log-linear interpolation 虽然可行，但引入额外的非线性，对 monotonicity 的 verification 更困难，且没有 clear practical advantage。

4. E-value 文献（VanderWeele & Ding 2017）也使用单参数路径，未讨论 path sensitivity——ASV 遵循同样的 convention 是合理的。

但我同意，如果论文声称 ASV 是 "path-independent" 的 sensitivity measure，那就需要验证多条路径。论文目前没有做这个 claim——ASV 明确绑定于 C(δ) 路径。

---

**[AGREE] R1-Q3: IV 拓扑 monotonicity 失败的根本原因**

R1 的猜测是正确的——IV 的 Wald estimator τ̂_IV = cov(A*,Y) / cov(A*,X) 是 ratio estimator，分母 cov(A*,X) 可以在 misclassification 下趋近零或变号。Section 3.2 (IV paragraph) 已陈述 "Misclassification can drive first-stage coefficients toward zero or reverse their sign, causing the ratio estimator to diverge or flip"。

补充：Appendix B.4 (IV Wald Estimator) 详细分析了 diagonal-dominance subspaces，Table 8 显示即使 diagonal ≥ 0.9，IV violation 仍为 100%。这是因为 ratio estimator 的 denominator 对 off-diagonal entries 的 *sign structure* 敏感，而非仅对 magnitude 敏感。这与 2SLS 的 weak instrument 问题本质相同——misclassification 制造了 "artificial weak instrument"。论文已有这个分析，R1 的追问可以指向 Appendix B.4 获得解答。

---

**[AGREE] R1-Q4: "exclusively in secondary coefficients" 是解析结果还是经验观察？**

与我在 Round 1 中提出的 N2 (CRITICAL) 完全一致。这是纯经验观察，基于 23 个 LLM 配置。Section 3.2 footnote 2 给出的 "magnitude dominance" 是 heuristic 解释，不是 formal proof。

论文需要：(a) 明确标注为 empirical observation；(b) 提供 formal sufficient condition（例如当 |β_primary| / |β_secondary| > some threshold 时 sign preservation 成立）；(c) 讨论当多个 coefficients magnitude 接近时，primary coefficient 也可能 reverse。这与我的 N2 concern 是同一问题。

---

**[REBUT] R1-Q5: FWL invariance 当 C₀ 接近奇异时是否精确成立？**

FWL invariance 是一个关于 column space 的代数恒等式，不依赖于 C₀ 的 invertibility。具体来说（Appendix B.2）：对于 A 作为 covariate 的 4 种拓扑，treatment coefficient τ̂ 仅依赖于 T 对 D*（dummy encoding of A*）的残差投影。任何对 D* 列的线性变换（包括 matrix correction M·D*）不改变 D* 的 column space，因此 FWL 定理保证 τ̂ 不变。

这是精确成立的——不存在 "C₀ 接近奇异时 breakdown" 的情形，因为：
1. FWL 操作的是 projection matrix M_D* = I - D*(D*'D*)⁻¹D*'
2. M·D* 和 D* 的 column space 相同当且仅当 M 可逆——但即使 M 不可逆（C₀ 奇异），只要 correction 后的变量仍 span 相同空间，FWL 成立
3. 唯一例外是 M 将 D* 的某些列映射为零——这要求 C₀ 的某行全为零（不是 column-stochastic matrix 的合法状态）

所以 R1-Q5 的答案是：FWL invariance 在所有 column-stochastic C₀ 下精确成立，包括近奇异情形。数值精度问题（condition number 很大时浮点误差）不影响理论结果。

---

### Missing References 回应

**[AGREE]** Fong, Hazlett, and Imai (2018) "Covariate Balancing Propensity Score for a Continuous Treatment" 确实与 sensitivity analysis 方法论相关，但与本文的 annotation error 焦点距离稍远。作为 optional reference 合理。

---

### 总结

与 Reviewer 1 在大方向上高度一致（均评 3.5 Borderline Conference）。核心共识：
- **W1/Proposition 2 命名**：同意需修正
- **W4/Stress test 覆盖**：同意需扩展（与我的 Q3 一致）
- **Q4/Primary coefficient claim**：同意需降级为 empirical observation（与我的 N2 一致）
- **W7/Linear scope annotation**：同意需更显著标注（与我的 W1 一致）

主要分歧：
- **W5/矩阵覆盖**：我认为 20,000 对存在性验证目标是 adequate 的
- **Q2/路径选择**：我认为 C(δ) 线性插值是自然且合理的选择，path sensitivity 不是 critical concern
- **Q5/FWL near-singular**：FWL invariance 是代数恒等式，不受 C₀ 条件数影响

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 556 · 2026-05-22T23:54:38.831711+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 557 · 2026-05-22T23:54:41.388477+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

与 Reviewer 1 在 7 个 weakness 中 5 个 AGREE（W1-W4, W6-W7），1 个 REBUT（W5 矩阵覆盖充分性）；在 5 个 question 中 3 个 AGREE（Q1, Q3, Q4），2 个 REBUT（Q2 路径选择、Q5 FWL near-singular）。两位 reviewer 的核心共识集中在：Proposition 2 命名不当、stress test 覆盖不足、primary coefficient claim 过强、linear scope 标注不够显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 558 · 2026-05-22T23:54:49.460580+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 61

## Round 61

10 recorded events


### User

_source line 559 · 2026-05-22T23:55:27.970844+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: ASV 框架与 E-value 的方法论新颖性**

同意论文当前对 ASV vs E-value 的区分不够深入，列举的三个差异确实偏表面。但不同意 ASV 仅是 "E-value 在新 domain 的 direct application" 的结论，理由如下：

R2 自己实际上已经点出了核心差异：E-value 的 confounding 参数 Γ 的 monotonicity 是 trivially satisfied（Cinelli & Hazlett 2020），而 annotation error domain 中 monotonicity 需要 Theorem 1 + Conjecture 1 来证明/验证。这不仅是"验证任务"——这是 ASV well-definedness 的前提条件，而且它不是自动成立的（IV 拓扑就不满足严格 monotonicity，见 Table 10, Appendix B.11）。E-value 不需要证明 monotonicity 因为它的参数化天然保证了单调性；ASV 需要证明是因为 K×K 混淆矩阵的参数化使得 bias 可以非单调（如 collider/M-bias 方向相反）。

此外，C(δ)=(1-δ)I+δC₀ 虽然形式简单，但它在 K×K 列随机矩阵空间上的行为远比标量插值复杂——不同拓扑下 bias 关于 δ 的方向不同（confounding 递增，collider 递减），这种拓扑依赖性是 E-value 框架中不存在的。

**建议**：论文应将 "monotonicity is non-trivial and topology-dependent" 作为 ASV 的核心方法论贡献来阐述，而非仅列举三个表面差异。这实际上会strengthes 而非 weakens 论文的贡献叙事。

---

**[AGREE] R2-N2: "Primary coefficient never reverses" 声明的 evidence 不足**

完全同意。我在自己的 Q4 中也提出了相同问题。23 个经验配置不足以支撑 abstract 中 "exclusively in secondary coefficients" 的声称——这只是 23 个数据点上的经验规律，不是结构性保证。

补充证据支持 R2 的判断：
- Section 4.4 (page 7) 提到 "never reversed in any tested configuration—an empirical regularity we discuss in Section 4"，论文自身已使用 "empirical regularity" 一词，但 abstract 的措辞未反映这一谨慎性
- Footnote 2 的 "magnitude dominance" 解释是 heuristic，依赖于 primary coefficient 在所有合理 DGP 下恒占主导地位的假设，但未给出 breakdown 条件
- 论文在 K≥3 binarization collapse 分析中（Appendix B.1）实际上展示了 binarization 可以导致 primary coefficient reversal（"sign flip during binarization" 见 page 19 底部），这暗示在某些 K≥3 结构下 primary reversal 是可能的

**建议**：将 abstract 中 "exclusively" 改为 "in all tested configurations, only secondary coefficients reversed"，并在 Section 4.4 补充 sufficient condition 或至少讨论何种条件下 primary reversal 可能发生。

---

### Should-Fix 问题

**[AGREE partially] R2-W1: 线性 SEM 范围限制**

同意线性限制对 NLP/CSS 受众是显著的，这与我的 W7 一致（我标为 MINOR，R2 标为 MAJOR）。

但需要纠正 R2 一处事实性判断：R2 声称 "其他 3 个 FWL-invariant 拓扑未测试 logistic breakdown"——实际上 Appendix B.6 (page 23) 明确测试了全部 7 种拓扑的 logistic DGP，表中显示 "Treatment-effect sign-flip rates (SF_e) are zero for all five guaranteed topologies under both linear and logistic DGPs"。所以 logistic 验证是完整的，不仅限于某几个拓扑。

不过，R2 的核心论点仍然成立：sign-flip rate stability ≠ FWL invariance preservation。在 logistic 模型下，矩阵校正方法可能不再完全无效（因为 FWL 不再精确成立），但论文没有测试这一点。建议补充 logistic DGP 下矩阵校正方法的 RMSE reduction 数据。

---

**[REBUT partially] R2-W2: 主文关键推导过于简略**

R2 的事实描述准确：main text 仅给出 confounding (Eq.1), exposure (Eq.2), mediation (Eq.3) 的公式，collider/M-bias/front-door/IV 在 main text 中仅有文字描述。

但这是 8 页限制下的合理权衡，而非疏忽：
- 7 种拓扑的完整推导在 Appendix A.3-A.8 中均有提供（共 10 页证明），每种拓扑包含 data-generating process、bias decomposition、closed-form plim、endpoint analysis 和数值验证
- Main text 优先展示的 3 种拓扑（confounding/exposure/mediation）是 NLP/CSS 中最常见的因果结构
- Section 3.2 在 "Structural sign-flip guarantee" 段落（page 4 底部）对所有 7 种拓扑的 sign preservation 条件做了统一摘要

建议论文在 Section 3.2 开头添加一句明确声明："Full derivations for all seven topologies appear in Appendix A.3-A.8; we present the three most common topologies in the main text." 这比重新安排 main text 结构更实际。

---

**[AGREE partially] R2-W3: 83.4% sign reversal framing**

R2 的核心批评——Dirichlet(1,1,1) prior 对 realistic confusion matrices 不合理——是正确的。uniform Dirichlet 生成的矩阵对角元素期望仅为 1/K（K=3 时约 0.33），远低于任何合理分类器。

但需要注意：
1. Abstract（page 1）实际上已使用 realistic 数字："Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.1%"——这是 abstract 中的 headline 数字，不是 83.4%
2. 83.4% 出现在 Section 4.2 (page 6) 和 Figure 2 caption (page 6) 中，用于论证"结构可能性"（structural possibility），即 K≥3 的混淆矩阵空间在理论上允许 sign reversal——这是一个数学事实，不依赖于 prior 的 realism
3. Introduction (page 1) 提到的 "50% for smaller models" 引用的是 Baumann et al. (2025) 的结果，不是本文的 83.4%

所以 R2 关于 "abstract 首先引用 83.4%" 的说法不准确——abstract 用的是 1.1%。但同意 Figure 2 caption 和 Section 4.2 的呈现顺序可以改进：应先报告 realistic rate（diagonal ≥ 0.7 下的 1.1%），再以 Dirichlet 分析作为理论极端情况。

---

**[AGREE partially] R2-W4: 缺少商业 LLM**

同意从经验代表性角度看，GPT-4o/Claude 的混淆矩阵数据会加强实验部分。

但理论贡献完全不依赖于具体 LLM：bias 表达式、ASV 框架、FWL invariance 均以混淆矩阵 C 为输入，与产生 C 的具体模型无关。加入商业 LLM 数据只影响 Section 4.4 的经验验证广度，不影响方法论贡献。

此外，R2 将此项从 MINOR 升级到 MAJOR 过于激进。商业 LLM API 的可及性、成本和 reproducibility（closed-source API 版本可能变化）都是合理的不纳入理由。建议论文在 Limitations 中提及这一点即可。

---

**[AGREE] R2-W5: 引用格式**

同意。arXiv preprint 应标注 "preprint" 或在参考文献中注明状态。纯格式问题，不影响实质评估。

---

### Questions

**[AGREE] R2-Q1: Proposition 1(a) 的 B_OV 方向**

正确指出了实践困难。Proposition 1(a) 的 sign preservation 条件需要知道 omitted variable bias 的方向（即 Cov(g(A), f(A)) / Var(f(A)) 的符号），这在实践中通常需要领域知识或 sensitivity analysis 来判断。论文应讨论如何在实践中评估此条件——例如通过 ASV 框架本身提供的 sign-flip ASV 来间接回答。

---

**[AGREE] R2-Q2: Table 9 ASV ranking 依赖 β 配置**

有效质疑。Table 9 (Appendix B.10) 显示 exposure 的 ASV 依赖于 coefficient ratio structure。论文声称 "vulnerability spectrum from IV (maximally fragile) to M-bias (immune)" 但如果中间拓扑的排名随 β 变化，这个 "spectrum" 不是 universal 的。

不过需要区分两个层面：
1. **端点稳定**：IV 最脆弱、M-bias 最稳健——这在所有测试配置下一致（Table 9 confirms "IV magnitude ASV is identical across all three DGPs"）
2. **中间排名可变**：exposure/confounding/mediation 的相对顺序可能随 β 变化

论文应明确："IV-fragile, M-bias-immune" 的极端排名是稳健的，但中间拓扑的精确排名依赖于 DGP 参数。

---

**[AGREE] R2-Q3: Non-differential stress test 范围**

与我的 W4 一致。r=0.1 的测试范围不足以覆盖 few-shot prompting 或 retrieval-augmented 标注中可能出现的强差异性错分类。论文应扩展到 r ∈ {0.2, 0.3, 0.5}。

---

**[AGREE] R2-Q4: Bootstrap ASV CI for IV**

有效关注。Appendix B.7 (page 23) 显示 IV 的 95% CI "spans a 3× range"，论文自身建议 "practitioners should bootstrap C₀ rather than rely on a point estimate when ASV is near the decision boundary." 但这实际上意味着对 IV 拓扑，ASV 的实践指导价值有限——CI 过宽时 point estimate 不可靠。论文应在 main text 中（而非仅在 appendix）提及这一限制。

---

**[REBUT] R2-Q5: Conjecture 1 的 ε/η 精度问题**

R2 的数学直觉是正确的（η 小时 ε/η 可以很大），但这个担忧在实践中不构成问题：

1. ASV 的计算不依赖于 Conjecture 1 的 ε 精度——ASV 直接在 C(δ) 路径上计算 bias，然后检查 threshold crossing。Monotonicity 仅用于保证 crossing point 的唯一性（如果 bias 非单调，可能有多个 crossing，ASV 定义需要取 infimum）
2. 即使 ε=0.06，Table 10 (page 25) 显示实际 worst-case deviation 远小于 ε bound（confounding 0.011, exposure 0.009, mediation 0.013 等）
3. 对于 ε-approximate monotonicity 下的 ASV 计算，论文推荐 bootstrapping（Appendix B.7），这自动处理了非精确 monotonicity 下的不确定性

所以 ε/η 的理论放大问题在实践中被 bootstrapping 和实际 deviation 远小于 bound 两个因素缓解。但建议论文添加一段简短讨论，解释为什么 ε < 0.06 在实践中足够（因为它远小于 ASV 的 typical step size η）。

---

**[AGREE] R2-Q6: Algorithm 1 的 0.1 threshold**

合理问题。Algorithm 1 (page 26) 中的 RMSE threshold 0.1 和 bias reduction 0.05 等数字缺乏系统的 sensitivity analysis 或理论推导。这些是工程化选择，应在论文中讨论其依据（如来自 Monte Carlo 实验中的 elbow analysis）或至少进行 threshold sensitivity 测试。

---

### Missing References

**[AGREE partially]**

- Wei, He, Li & Geng (2025) "Multiply robust causal inference in the presence of an error-prone treatment" — 同意应引用，直接相关于 error-prone treatment 的因果推断
- Demirel et al. (2024) "Prediction-powered Generalization of Causal Inferences" (ICML 2024) — 同意，与 PPI++ 方法论相关
- Cheng et al. (2024) 更新版本 — 如有 venue publication 版本应更新引用

---

### 综合评价

R2 的审稿整体质量高，多数批评有据。两个 CRITICAL 中：
- **N1 (ASV novelty)**: 诊断正确但结论过重。ASV 不是 E-value 的简单搬运——monotonicity 非平凡性本身就是方法论贡献。但论文确实需要更好地阐述这一点。建议 severity: **MAJOR** 而非 CRITICAL。
- **N2 (primary coefficient claim)**: 完全同意，这是 abstract 中最需要修改的声称。severity: **CRITICAL** 合理。

R2 的 Overall 3.5 与我的评分一致。论文核心贡献扎实但存在可修复的表述和验证范围问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-22T23:55:53.780183+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-22T23:55:53.881107+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T23:37:27.288465+00:00\", \"completed_at\": \"2026-05-22T23:37:30.853030+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-22T23:55:53.931749+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-22T23:55:53.982654+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-23T00:02:18.217672+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Carried from Round 1-5 (resolved issues kept as history) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 6\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Proposition 2（数值验证）和 Conjecture 1 覆盖。R6-M1 的拆分已完成。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1]\n        note: \"R7-R1 确认 Theorem 1 (K=2) 证明完整正确。新 concern 转移到 Proposition 2 的命名问题（见 R7-SF1）。\"\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写：83.4% 作为 K≥3 结构转变呈现，与 2.1% 并列。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未显式提及商业 LLM 缺失。\"\n      - round: 7\n        reviewers: [R2]\n        note: \"R7-R2 再次提出（W4 MINOR→MAJOR）。R1 REBUT partially：理论贡献不依赖具体 LLM，API 成本和 reproducibility 是合理不纳入理由。共识降为 MINOR——在 Limitations 中讨论即可。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加商业 LLM 限制说明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。Algorithm 1 caption 已有 'Assumes linear structural equations'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [R2]\n        note: \"R6-R2 再次以 CRITICAL 级别提出线性假设与 NLP 适用性的 mismatch（见 R6-W1）。R1 REBUT 降为 MAJOR。\"\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"method.tex 添加完整的 'text as common cause' 讨论。\"\n    resolution_round: 5\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5 确认 FWL 证明'干净且重要'。R7 两位 Reviewer 均肯定 FWL invariance 论证完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。R7 两位 Reviewer 均肯定三级体系（R1-S2, R2-S4）。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 5\n        reviewers: [R2]\n        note: \"R5 确认 ASV 是 E-value 的有意义扩展。\"\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 再次独立提出 ASV vs E-value 差异化不足。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7-R2 首发 CRITICAL，R7-R1 AGREE with nuance 降为 MAJOR。共识：论文应聚焦 monotonicity 非平凡性（confounding 域 trivially satisfied, annotation error 域需 Theorem 1 + Conjecture 1）作为核心方法论贡献。当前列举的三个差异偏表面。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 增加 ASV vs E-value/QBA 的明确技术对比\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"重构 ASV novelty 叙事——将 'monotonicity is non-trivial and topology-dependent' 作为核心方法论贡献阐述，而非仅列举三个表面差异\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未直接提及。\"\n      - round: 7\n        reviewers: [R2]\n        note: \"R7-R2 提出 Method section collider/M-bias/front-door 推导过于简略（W2 MAJOR）。R7-R1 REBUT partially：8 页限制下合理权衡，完整推导在 Appendix A.3-A.8。共识降为 MINOR——添加一句指向 appendix 的声明即可。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6-R2-D5 指出 Algorithm 1 未加入 PPI++ 对 M-bias 的排除条件。R1 AGREE。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及 PPI++ M-bias guard。R7-R2 提出 Algorithm 1 threshold 问题（Q6），但未单独提 M-bias 排除条件。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 加入 if M-bias: exclude PPI++ 的显式 guard\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"R5 bib 检查通过。\"\n      - round: 7\n        reviewers: [R2]\n        note: \"R7-R2 再次发现：Pangakis et al. (2023), Cheng et al. (2024), Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态。R1 AGREE。\"\n    action_items:\n      - round: 7\n        action: \"统一标注所有 preprint 状态，检查是否有 preprint 已正式发表\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-MR\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇引用（Round 4 新要求）\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 5\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: should-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现（23 configs），缺乏理论保证\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 7\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R5 修复了 same-sign 错误机制解释，替换为 magnitude dominance。\"\n      - round: 6\n        reviewers: [R1]\n        note: \"R6-R1-M2：Abstract 仍将此称为 'structural property'，但仅有 23 configs 的经验支撑。R2 交叉回应 AGREE。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7 两位 Reviewer 一致评为 CRITICAL——本轮最需修改的声称。R2-N2 首发，R1 完全 AGREE。R1 补充：Appendix B.1 binarization 分析暗示某些 K≥3 下 primary reversal 可能发生。要求：(a) Abstract 标注 'empirical regularity'；(b) 提供 sufficient condition 或讨论 breakdown regime；(c) 降低 claim prominence。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 'structural property' → 'empirical regularity'\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"降低 claim prominence + 提供 sufficient condition（如 diagonal dominance threshold + coefficient magnitude ratio）或讨论 breakdown regime（当 max|βₖ|/min|βₖ| 接近 1 时）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  # === Round 6 issues ===\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2（proof via perspective function convexity）。K≥3 由 Proposition 2（数值验证）覆盖。R7-R1 确认 Theorem 1 证明完整正确。但 Proposition 2 的命名引发新 concern（见 R7-SF1）。\"\n    resolution_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 提出。\"\n      - round: 7\n        reviewers: [R1]\n        note: \"R7-R1 确认 Theorem 1 (K=2) 证明正确。新 concern 转移到 Proposition 2（R7-SF1）。\"\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'，实际仅有经验支撑\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"与 R5-N3 合并跟踪。R7 两位 Reviewer 一致升为 CRITICAL。详见 R5-N3 条目。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7-R1 首发 W2 MAJOR。R7-R2 AGREE with nuance：Proposition 2 + Conjecture 1 为 general case 提供数值支撑，但 ε/η 在 weak effect 下可能放大误差。要求：(a) 讨论 NLP 场景合理性；(b) 主文引用 Appendix A.4 general case 数值验证（worst-case deviation < 0.005）。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.2 增加 proportional effects 的现实场景讨论和 Appendix A.4 引用\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"补充 NLP 场景中 proportional effects 的合理性讨论 + 引用 Appendix A.4 worst-case deviation\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%（diagonal≥0.7 条件下），数值一致。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7 未再发现 Abstract 与 Section 4.2 的数值不一致。但 R7-R1 在交叉回应中误读 Abstract 为 1.1%（实际为 2.1%），此为 Reviewer 笔误非论文问题。\"\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。共识 MAJOR。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7-R2 首发 W1 MAJOR。R7-R1 AGREE partially（纠正事实错误：Appendix B.6 实际测试了全部 7 种拓扑）。共识：Section 3.1 仅一句话提到 linear SEM，FWL invariance 标注不够显著。要求：Section 3 开头和 Section 4.5 显著标注 linear scope。\"\n    action_items:\n      - round: 6\n        action: \"Introduction/Conclusion 更明确 scope 为线性 SEM\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"Section 3 开头添加显著 linear scope 标注 + Section 4.5 FWL 结果旁重申 linear requirement\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。继承 R4-W6。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并跟踪。详见 R4-W6 条目。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失 3-4 篇相关引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Shu & Yi (2019a, 2019b), Cadei et al. (2025), Neuhaus (1999) 均已在 Related Work 中引用。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1]\n        note: \"R7-R1 确认引用覆盖充分（'未发现重要遗漏引用'）。R7-R2 发现新缺失引用（见 R7-MR1）。\"\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及。论文当前结构已较清晰：Theorem 1 (K=2 exact) → Proposition 2 (K≥3 numerical) → Conjecture 1 (ε-approximate all non-IV)。但 Proposition 2 命名问题（R7-SF1）间接影响此关系的清晰度。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: minor\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发：仅覆盖 exposure 拓扑。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7 将 concern 升级并转向 r 范围：R1-W4 MAJOR 指出 r≤0.1 过窄，R2 强烈 AGREE。R2 补充：当前均匀扰动不反映实际 structured violation。要求扩展到 r ∈ {0.2, 0.3, 0.5}。severity 从 MINOR 升为 MAJOR。\"\n    action_items:\n      - round: 6\n        action: \"扩展 stress test 到 confounding 和 mediation 拓扑\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"扩展 r 范围到 {0.2, 0.3, 0.5}，评估强差异性下 sign preservation 和 ASV ranking 的退化\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及。R7-R2 在 Detailed Comments 中注意到 'Violation 列定义需更清晰'，间接相关。\"\n    action_items:\n      - round: 6\n        action: \"Table 1 caption 明确 'Amplif.' 定义\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及 PPI++ M-bias guard。R7-R2-Q6 提出 Algorithm 1 threshold 问题但未单独提 M-bias 排除。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 加入 M-bias exclude PPI++ guard\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 7 新发现 ===\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名与数值验证性质不匹配——应反映非解析证明的性质\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R1-W1 首发 MAJOR，R2 AGREE。Proposition 2 文本明确是数值验证（20,000 random triples），但 formal name 暗示已证结果。与 Conjecture 1 正确使用 'Conjecture' 形成对比，命名不一致。建议改为 'Numerical Result 1' 或显式标注 'supported by numerical evidence'。\"\n    action_items:\n      - round: 7\n        action: \"Proposition 2 重命名或在正文中显式标注数值验证性质\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 选择的敏感性未充分分析——不同估计方法可能产生不同 ASV ranking\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R1-W3 首发 MAJOR，R2 AGREE。Bootstrap CI 回答了 sampling uncertainty，但未回答不同 C₀ 估计方法（validation set vs cross-validation vs few-shot gold subset）的系统性差异。IV 的 95% CI [0.44, 1.29] 跨越 δ=1——point estimate 不可靠。需增加 C₀ 扰动分析或讨论 ranking robustness。\"\n    action_items:\n      - round: 7\n        action: \"增加 C₀ 扰动分析，或至少讨论 ASV ranking 对 C₀ 估计方法的 robustness 条件\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 和 Figure 2 中 83.4% sign reversal 的呈现顺序有误导性\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R2-W3 首发 MAJOR，R1 AGREE partially。Dirichlet(1,1,1) prior 生成的矩阵对角元素期望仅 1/K≈0.33，对 realistic classifiers 不合理。R1 纠正：Abstract 实际首先使用 realistic number (2.1%)，83.4% 主要出现在 Section 4.2 和 Figure 2 caption。共识：Section 4.2 应先报告 realistic rate，再以 Dirichlet 分析作为理论极端。\"\n    action_items:\n      - round: 7\n        action: \"Section 4.2 重排呈现顺序——先 realistic accuracy (diagonal≥0.7) 下的 2.1%，再 Dirichlet(1,1,1) 的 83.4% 作为理论上界\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"Introduction '154×' binarization bias 倍数来源不透明\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R1-W6 首发 MINOR，R2 AGREE。Introduction Contribution 1 中 '154×' 未在正文给出计算基础。Appendix B.1 讨论 binarization 但未明确此数字的来源。\"\n    action_items:\n      - round: 7\n        action: \"在 Appendix B.1 或正文中给出 154× 的具体计算（哪两个拓扑、哪个指标的比值）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 2-3 篇相关引用（Wei et al. 2025, Demirel et al. 2024）\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"R2 发现 3 篇潜在遗漏。R1 AGREE partially。(1) Wei, He, Li & Geng (2025) 'Multiply robust causal inference in the presence of an error-prone treatment'——直接相关；(2) Demirel et al. (2024) 'Prediction-powered Generalization of Causal Inferences' (ICML 2024)——与 PPI 方法论相关；(3) Cheng et al. (2024) 应检查是否已正式发表。R1 另建议可选补充 Fong, Hazlett & Imai (2018)。\"\n    action_items:\n      - round: 7\n        action: \"补充 Wei et al. (2025) 和 Demirel et al. (2024)；检查 Cheng et al. (2024) 发表状态\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 的 risk threshold (0.1) 缺乏选择依据和 sensitivity analysis\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R2-Q6 首发，R1 AGREE。Algorithm 1 (p.26) 的 RMSE threshold 0.1 和 bias reduction 0.05 等数字缺乏理论推导或 sensitivity analysis。\"\n    action_items:\n      - round: 7\n        action: \"讨论 threshold 选择依据或进行 threshold sensitivity 测试\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Carried from Round 1-5 (resolved issues kept as history) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 6\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Proposition 2（数值验证）和 Conjecture 1 覆盖。R6-M1 的拆分已完成。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1]\n        note: \"R7-R1 确认 Theorem 1 (K=2) 证明完整正确。新 concern 转移到 Proposition 2 的命名问题（见 R7-SF1）。\"\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写：83.4% 作为 K≥3 结构转变呈现，与 2.1% 并列。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未显式提及商业 LLM 缺失。\"\n      - round: 7\n        reviewers: [R2]\n        note: \"R7-R2 再次提出（W4 MINOR→MAJOR）。R1 REBUT partially：理论贡献不依赖具体 LLM，API 成本和 reproducibility 是合理不纳入理由。共识降为 MINOR——在 Limitations 中讨论即可。\"\n    action_items:\n      - round: 4\n        action: \"Limitations 添加商业 LLM 限制说明\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。Algorithm 1 caption 已有 'Assumes linear structural equations'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [R2]\n        note: \"R6-R2 再次以 CRITICAL 级别提出线性假设与 NLP 适用性的 mismatch（见 R6-W1）。R1 REBUT 降为 MAJOR。\"\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"method.tex 添加完整的 'text as common cause' 讨论。\"\n    resolution_round: 5\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"R5 确认 FWL 证明'干净且重要'。R7 两位 Reviewer 均肯定 FWL invariance 论证完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。R7 两位 Reviewer 均肯定三级体系（R1-S2, R2-S4）。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 5\n        reviewers: [R2]\n        note: \"R5 确认 ASV 是 E-value 的有意义扩展。\"\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 再次独立提出 ASV vs E-value 差异化不足。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7-R2 首发 CRITICAL，R7-R1 AGREE with nuance 降为 MAJOR。共识：论文应聚焦 monotonicity 非平凡性（confounding 域 trivially satisfied, annotation error 域需 Theorem 1 + Conjecture 1）作为核心方法论贡献。当前列举的三个差异偏表面。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.3 增加 ASV vs E-value/QBA 的明确技术对比\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"重构 ASV novelty 叙事——将 'monotonicity is non-trivial and topology-dependent' 作为核心方法论贡献阐述，而非仅列举三个表面差异\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: []\n        note: \"R6 未直接提及。\"\n      - round: 7\n        reviewers: [R2]\n        note: \"R7-R2 提出 Method section collider/M-bias/front-door 推导过于简略（W2 MAJOR）。R7-R1 REBUT partially：8 页限制下合理权衡，完整推导在 Appendix A.3-A.8。共识降为 MINOR——添加一句指向 appendix 的声明即可。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6-R2-D5 指出 Algorithm 1 未加入 PPI++ 对 M-bias 的排除条件。R1 AGREE。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及 PPI++ M-bias guard。R7-R2 提出 Algorithm 1 threshold 问题（Q6），但未单独提 M-bias 排除条件。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 加入 if M-bias: exclude PPI++ 的显式 guard\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: open\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"R5 bib 检查通过。\"\n      - round: 7\n        reviewers: [R2]\n        note: \"R7-R2 再次发现：Pangakis et al. (2023), Cheng et al. (2024), Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态。R1 AGREE。\"\n    action_items:\n      - round: 7\n        action: \"统一标注所有 preprint 状态，检查是否有 preprint 已正式发表\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-MR\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇引用（Round 4 新要求）\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 5\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: should-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现（23 configs），缺乏理论保证\"\n    status: open\n    first_raised_round: 5\n    last_seen_round: 7\n    mentions:\n      - round: 5\n        reviewers: [R1, R2]\n        note: \"R5 修复了 same-sign 错误机制解释，替换为 magnitude dominance。\"\n      - round: 6\n        reviewers: [R1]\n        note: \"R6-R1-M2：Abstract 仍将此称为 'structural property'，但仅有 23 configs 的经验支撑。R2 交叉回应 AGREE。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7 两位 Reviewer 一致评为 CRITICAL——本轮最需修改的声称。R2-N2 首发，R1 完全 AGREE。R1 补充：Appendix B.1 binarization 分析暗示某些 K≥3 下 primary reversal 可能发生。要求：(a) Abstract 标注 'empirical regularity'；(b) 提供 sufficient condition 或讨论 breakdown regime；(c) 降低 claim prominence。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 'structural property' → 'empirical regularity'\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"降低 claim prominence + 提供 sufficient condition（如 diagonal dominance threshold + coefficient magnitude ratio）或讨论 breakdown regime（当 max|βₖ|/min|βₖ| 接近 1 时）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  # === Round 6 issues ===\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2（proof via perspective function convexity）。K≥3 由 Proposition 2（数值验证）覆盖。R7-R1 确认 Theorem 1 证明完整正确。但 Proposition 2 的命名引发新 concern（见 R7-SF1）。\"\n    resolution_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 两位 Reviewer 提出。\"\n      - round: 7\n        reviewers: [R1]\n        note: \"R7-R1 确认 Theorem 1 (K=2) 证明正确。新 concern 转移到 Proposition 2（R7-SF1）。\"\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'，实际仅有经验支撑\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"与 R5-N3 合并跟踪。R7 两位 Reviewer 一致升为 CRITICAL。详见 R5-N3 条目。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7-R1 首发 W2 MAJOR。R7-R2 AGREE with nuance：Proposition 2 + Conjecture 1 为 general case 提供数值支撑，但 ε/η 在 weak effect 下可能放大误差。要求：(a) 讨论 NLP 场景合理性；(b) 主文引用 Appendix A.4 general case 数值验证（worst-case deviation < 0.005）。\"\n    action_items:\n      - round: 6\n        action: \"Section 3.2 增加 proportional effects 的现实场景讨论和 Appendix A.4 引用\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"补充 NLP 场景中 proportional effects 的合理性讨论 + 引用 Appendix A.4 worst-case deviation\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%（diagonal≥0.7 条件下），数值一致。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7 未再发现 Abstract 与 Section 4.2 的数值不一致。但 R7-R1 在交叉回应中误读 Abstract 为 1.1%（实际为 2.1%），此为 Reviewer 笔误非论文问题。\"\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。共识 MAJOR。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7-R2 首发 W1 MAJOR。R7-R1 AGREE partially（纠正事实错误：Appendix B.6 实际测试了全部 7 种拓扑）。共识：Section 3.1 仅一句话提到 linear SEM，FWL invariance 标注不够显著。要求：Section 3 开头和 Section 4.5 显著标注 linear scope。\"\n    action_items:\n      - round: 6\n        action: \"Introduction/Conclusion 更明确 scope 为线性 SEM\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"Section 3 开头添加显著 linear scope 标注 + Section 4.5 FWL 结果旁重申 linear requirement\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。继承 R4-W6。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并跟踪。详见 R4-W6 条目。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失 3-4 篇相关引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Shu & Yi (2019a, 2019b), Cadei et al. (2025), Neuhaus (1999) 均已在 Related Work 中引用。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1]\n        note: \"R7-R1 确认引用覆盖充分（'未发现重要遗漏引用'）。R7-R2 发现新缺失引用（见 R7-MR1）。\"\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及。论文当前结构已较清晰：Theorem 1 (K=2 exact) → Proposition 2 (K≥3 numerical) → Conjecture 1 (ε-approximate all non-IV)。但 Proposition 2 命名问题（R7-SF1）间接影响此关系的清晰度。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: minor\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发：仅覆盖 exposure 拓扑。\"\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R7 将 concern 升级并转向 r 范围：R1-W4 MAJOR 指出 r≤0.1 过窄，R2 强烈 AGREE。R2 补充：当前均匀扰动不反映实际 structured violation。要求扩展到 r ∈ {0.2, 0.3, 0.5}。severity 从 MINOR 升为 MAJOR。\"\n    action_items:\n      - round: 6\n        action: \"扩展 stress test 到 confounding 和 mediation 拓扑\"\n        assigned_to: director\n        status: open\n      - round: 7\n        action: \"扩展 r 范围到 {0.2, 0.3, 0.5}，评估强差异性下 sign preservation 和 ASV ranking 的退化\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及。R7-R2 在 Detailed Comments 中注意到 'Violation 列定义需更清晰'，间接相关。\"\n    action_items:\n      - round: 6\n        action: \"Table 1 caption 明确 'Amplif.' 定义\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [R1, R2]\n        note: \"R6 首发。\"\n      - round: 7\n        reviewers: []\n        note: \"R7 未显式提及 PPI++ M-bias guard。R7-R2-Q6 提出 Algorithm 1 threshold 问题但未单独提 M-bias 排除。\"\n    action_items:\n      - round: 6\n        action: \"Algorithm 1 加入 M-bias exclude PPI++ guard\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 7 新发现 ===\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名与数值验证性质不匹配——应反映非解析证明的性质\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R1-W1 首发 MAJOR，R2 AGREE。Proposition 2 文本明确是数值验证（20,000 random triples），但 formal name 暗示已证结果。与 Conjecture 1 正确使用 'Conjecture' 形成对比，命名不一致。建议改为 'Numerical Result 1' 或显式标注 'supported by numerical evidence'。\"\n    action_items:\n      - round: 7\n        action: \"Proposition 2 重命名或在正文中显式标注数值验证性质\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 选择的敏感性未充分分析——不同估计方法可能产生不同 ASV ranking\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R1-W3 首发 MAJOR，R2 AGREE。Bootstrap CI 回答了 sampling uncertainty，但未回答不同 C₀ 估计方法（validation set vs cross-validation vs few-shot gold subset）的系统性差异。IV 的 95% CI [0.44, 1.29] 跨越 δ=1——point estimate 不可靠。需增加 C₀ 扰动分析或讨论 ranking robustness。\"\n    action_items:\n      - round: 7\n        action: \"增加 C₀ 扰动分析，或至少讨论 ASV ranking 对 C₀ 估计方法的 robustness 条件\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 和 Figure 2 中 83.4% sign reversal 的呈现顺序有误导性\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R2-W3 首发 MAJOR，R1 AGREE partially。Dirichlet(1,1,1) prior 生成的矩阵对角元素期望仅 1/K≈0.33，对 realistic classifiers 不合理。R1 纠正：Abstract 实际首先使用 realistic number (2.1%)，83.4% 主要出现在 Section 4.2 和 Figure 2 caption。共识：Section 4.2 应先报告 realistic rate，再以 Dirichlet 分析作为理论极端。\"\n    action_items:\n      - round: 7\n        action: \"Section 4.2 重排呈现顺序——先 realistic accuracy (diagonal≥0.7) 下的 2.1%，再 Dirichlet(1,1,1) 的 83.4% 作为理论上界\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"Introduction '154×' binarization bias 倍数来源不透明\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R1-W6 首发 MINOR，R2 AGREE。Introduction Contribution 1 中 '154×' 未在正文给出计算基础。Appendix B.1 讨论 binarization 但未明确此数字的来源。\"\n    action_items:\n      - round: 7\n        action: \"在 Appendix B.1 或正文中给出 154× 的具体计算（哪两个拓扑、哪个指标的比值）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 2-3 篇相关引用（Wei et al. 2025, Demirel et al. 2024）\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"R2 发现 3 篇潜在遗漏。R1 AGREE partially。(1) Wei, He, Li & Geng (2025) 'Multiply robust causal inference in the presence of an error-prone treatment'——直接相关；(2) Demirel et al. (2024) 'Prediction-powered Generalization of Causal Inferences' (ICML 2024)——与 PPI 方法论相关；(3) Cheng et al. (2024) 应检查是否已正式发表。R1 另建议可选补充 Fong, Hazlett & Imai (2018)。\"\n    action_items:\n      - round: 7\n        action: \"补充 Wei et al. (2025) 和 Demirel et al. (2024)；检查 Cheng et al. (2024) 发表状态\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 的 risk threshold (0.1) 缺乏选择依据和 sensitivity analysis\"\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"R2-Q6 首发，R1 AGREE。Algorithm 1 (p.26) 的 RMSE threshold 0.1 和 bias reduction 0.05 等数字缺乏理论推导或 sensitivity analysis。\"\n    action_items:\n      - round: 7\n        action: \"讨论 threshold 选择依据或进行 threshold sensitivity 测试\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-23T00:02:18.319056+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 23506}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-23T00:05:07.586469+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# Consolidated Review Report — Round 7\n\n**论文**: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n**Venue**: EMNLP 2026 (ACL ARR, Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**轮次**: Round 1（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文针对 K-class 非差异性错分类在 7 种经典 DAG 拓扑下的偏差传播进行系统性理论分析，推导 probability limit 表达式，建立 Annotation Sensitivity Values (ASV) 敏感性分析框架，并证明 FWL 不变性导致矩阵校正方法在 4 种拓扑下完全无效。论文通过 23 个真实 LLM 配置 × 7 拓扑 = 161 个场景的经验验证（MAPE 1.6%），确认理论预测。贡献扎实且问题 timely，但存在可修复的命名不当、声称过强和验证范围不足问题。\n\n---\n\n## Strengths\n\n**S1. 系统性跨拓扑比较的原创价值** [R1-S1, R2-S1, 双方一致]\n首次在统一线性 SEM 框架下推导全部 7 种拓扑的 bias 表达式，揭示同一混淆矩阵在不同拓扑下产生质量上不同的偏差（attenuating vs. amplifying vs. sign-reversing）。Teblunthuis (2024) 覆盖 4 种拓扑但限于 binary；Lee & Wood-Doughty (2024) 只分析 confounding。\"首次跨 7 种拓扑系统比较\"的声明在两位 Reviewer 的检索范围内成立。\n\n**S2. FWL 不变性负结果有实用价值** [R1-S3, R2-S2, 双方一致]\n证明 matrix-based correction 对 4 种 covariate 拓扑下完全无效（0% bias reduction）——基于 FWL 定理的代数性质，论证完整且优雅。对 practitioners 选择校正方法有直接指导意义。R1 仔细审查了 Appendix B.2 的推导，确认代数正确。\n\n**S3. 透明的三级证明层级** [R1-S2, R2-S4, 双方一致]\n明确区分 analytically proved（Proposition 1, Theorem 1）、numerically verified（Proposition 2, 100K+ matrices）和 conjectured（Conjecture 1, ε-approximate bounds）三个层次。这种方法论诚实度在投稿论文中不常见。\n\n**S4. 实验验证层次丰富** [R1-S5, R2-S3, 双方一致]\n23 LLM 配置 × 7 拓扑 = 161 scenarios，grand MAPE 1.6%。包含 cross-K robustness (K=5,7)、logistic DGP 验证、non-differential stress test、bootstrap ASV CI——不是单一实验而是多层验证体系。ClinicalBERT case study (Appendix B.3) 展示端到端应用。\n\n**S5. 实际问题导向** [R2-S5]\nFigure 3 (F1 vs bias) 有效说明\"F1 不预测因果风险\"：在 F1=0.614–0.690 窄区间内 bias 跨拓扑变化 10×。对 CSS 实践者有直接警示价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. [CRITICAL] \"Primary coefficient never reverses\" 声明的 evidence 不足以支撑其 prominence**\n[R2-N2 首发 CRITICAL, R1 完全 AGREE CRITICAL]\n\n- **位置**: Abstract (\"in all 23 empirical configurations tested, the primary treatment effect does not reverse\"), Section 3.2 footnote 2, Introduction paragraph 2\n- **问题**: 该声明在 abstract 和 introduction 中以近乎 structural property 的语气呈现，但：(a) 仅基于 23 个经验配置——样本量极小；(b) 解释仅为 footnote 2 的 heuristic（\"magnitude dominance\"）——无 formal sufficient condition；(c) 论文自身在 Section 3.2 已使用 \"empirical regularity\"，但 abstract 措辞未反映这一谨慎性；(d) 未讨论 breakdown regime（如多个 coefficient magnitude 接近时）\n- **R1 补充证据**: Appendix B.1 binarization 分析暗示在某些 K≥3 结构下 primary reversal 可能发生\n- **要求**: (a) Abstract 中明确标注 \"empirical regularity\"；(b) 提供 formal sufficient condition（如 diagonal dominance threshold + coefficient magnitude ratio）或讨论 breakdown regime；(c) 降低 claim prominence\n\n**MF-2. [MAJOR] ASV 框架与 E-value 的方法论差异需更清晰阐述**\n[R2-N1 首发 CRITICAL, R1 AGREE with nuance 降为 MAJOR]\n\n- **位置**: Section 3.3\n- **问题**: 论文列举的三个 ASV vs E-value 差异偏表面：(1) ε-approximate monotonicity proof 是验证任务非方法创新；(2) three ASV types 本质是同一 idea 用不同 threshold；(3) FWL combination 是 routing 应用\n- **R1 关键洞察**: 真正的方法论贡献被淹没——E-value 的 confounding 参数 Γ 的 monotonicity 是 trivially satisfied（Cinelli & Hazlett 2020 已证明），但 annotation error domain 中 monotonicity 非平凡（需 Theorem 1 + Conjecture 1），且拓扑依赖（confounding 递增, collider 递减）。这种 non-trivial topology-dependent monotonicity 是 E-value 框架中不存在的\n- **R1 降级理由**: ASV 不是 E-value 的简单搬运——monotonicity 非平凡性本身就是方法论贡献，只是论文未凸显\n- **要求**: 重构 ASV novelty 叙事——将 \"monotonicity is non-trivial and topology-dependent\" 作为核心方法论贡献阐述\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. [MAJOR] Proposition 2 命名与数值验证性质不匹配**\n[R1-W1 首发 MAJOR, R2 AGREE]\n\n- **位置**: Section 3.3 (page 5)\n- **问题**: Proposition 2 的 \"证明\" 实质是 20,000 组随机矩阵的数值验证；在数学惯例中 \"Proposition\" 意味已证结果。Conjecture 1 正确使用 \"Conjecture\"，命名不一致更凸显问题\n- **要求**: 改为 \"Numerical Result 1\" 或显式标注 \"supported by numerical evidence; analytic proof remains open\"\n\n**SF-2. [MAJOR] Theorem 1 的 proportional effects 假设 (f=λg) 讨论不足**\n[R1-W2 首发 MAJOR, R2 AGREE with nuance]\n\n- **位置**: Theorem 1 (page 5), Appendix A.4 (page 13)\n- **问题**: f=λg 在实际 NLP 场景（如政治立场 K=5）中不太可能严格成立。Appendix A.4 有 general case 数值验证（worst-case deviation < 0.005）但主文未充分引用\n- **R2 补充**: Proposition 2 + Conjecture 1 为 general case 提供数值支撑；但 ε/η 在 weak effect 下可能放大误差\n- **要求**: (a) 讨论 proportional effects 在 NLP 场景的合理性；(b) 主文引用 Appendix A.4 general case 数值验证\n\n**SF-3. [MAJOR] 非差异性错分类压力测试覆盖不足**\n[R1-W4 首发 MAJOR, R2 强烈 AGREE]\n\n- **位置**: Appendix B.5 (Table 7)\n- **问题**: 仅覆盖 r ∈ {0, 0.05, 0.1} 的 mild violations。实际场景（few-shot demonstrations 编码 outcome-treatment 关联, RLHF implicit correlations, RAG outcome signal）可能远超 r=0.1\n- **R2 补充**: 当前 r 定义是均匀扰动所有 off-diagonal entries——实际 violation 可能是 structured\n- **要求**: 扩展到 r ∈ {0.2, 0.3, 0.5}\n\n**SF-4. [MAJOR] 线性 SEM 范围限制标注不够显著**\n[R1-W7 首发 MINOR, R2-W1 首发 MAJOR, 交叉后共识 MAJOR]\n\n- **位置**: Section 3.1, Section 4.5\n- **问题**: Section 3.1 仅一句话提到 \"linear structural equations\"；FWL invariance 严格依赖线性假设但标注不突出\n- **R1 纠正 R2 事实错误**: Appendix B.6 实际测试了全部 7 种拓扑（非仅 exposure）。但 R2 核心论点成立：sign-flip rate stability ≠ FWL invariance preservation\n- **要求**: Section 3 开头和 Section 4.5 显著标注 linear scope\n\n**SF-5. [MAJOR] ASV 对 C₀ 选择的敏感性未充分分析**\n[R1-W3 首发 MAJOR, R2 AGREE]\n\n- **位置**: Section 3.3, Appendix B.7\n- **问题**: Bootstrap CI 回答了 sampling uncertainty，未回答不同 C₀ 估计方法的系统性差异。IV 的 95% CI [0.44, 1.29] 跨越 δ=1——point estimate 不可靠\n- **要求**: 增加 C₀ 扰动分析或讨论 ranking robustness 条件\n\n**SF-6. [MAJOR] 83.4% sign reversal 在 Section 4.2/Figure 2 中的呈现顺序有误导性**\n[R2-W3 首发 MAJOR, R1 AGREE partially]\n\n- **位置**: Section 4.2 paragraph 2, Figure 2 caption\n- **问题**: Dirichlet(1,1,1) prior 对角元素期望仅 1/K≈0.33，对 realistic classifiers 不合理\n- **R1 纠正**: Abstract 实际首先使用 realistic number (2.1%)；83.4% 主要出现在 Section 4.2 和 Figure 2\n- **要求**: Section 4.2 重排呈现顺序——先 realistic rate (2.1%)，再 Dirichlet 分析作为理论极端\n\n**SF-7. [MINOR] Method section 关键拓扑推导过于简略**\n[R2-W2 首发 MAJOR, R1 REBUT partially 降为 MINOR]\n\n- **问题**: Main text 仅给出 confounding/exposure/mediation 的公式，collider/M-bias/front-door/IV 仅有文字描述\n- **R1 论证**: 8 页限制下合理权衡，完整推导在 Appendix A.3-A.8（共 10 页证明）\n- **要求**: 添加一句声明指向 appendix\n\n**SF-8. [MINOR] \"154×\" binarization bias 倍数来源不透明**\n[R1-W6 首发 MINOR, R2 AGREE]\n\n- **位置**: Introduction Contribution 1\n- **要求**: 在 Appendix B.1 或正文中给出 154× 的具体计算基础\n\n**SF-9. [MINOR] 缺少商业 LLM 实验配置**\n[R2-W4 首发 MINOR→MAJOR, R1 REBUT partially 维持 MINOR]\n\n- **问题**: 4 个 LLM 全部开源。R1 论证：理论贡献不依赖具体 LLM，API 成本和 reproducibility 是合理理由\n- **要求**: Limitations 中讨论即可\n\n**SF-10. [MINOR] 引用格式不统一**\n[R2-W5 首发 MINOR, R1 AGREE]\n\n- **问题**: Pangakis et al. (2023), Cheng et al. (2024), Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态\n- **要求**: 统一标注 preprint 状态，检查是否已正式发表\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Primary coefficient claim 过强** (MF-1)：两位 Reviewer 均评为 CRITICAL——本轮最需修改的声称\n2. **ASV novelty 需更好阐述** (MF-2)：聚焦 monotonicity 非平凡性和拓扑依赖性\n3. **Proposition 2 命名不当** (SF-1)：应反映数值验证性质\n4. **Stress test 范围过窄** (SF-3)：r≤0.1 不足，需扩展到 r≥0.3\n5. **Linear scope 标注不足** (SF-4)：对 NLP/CSS 受众需更显著标注\n6. **核心理论贡献扎实**：7 拓扑 taxonomy、FWL invariance、三级证明体系均获双方肯定\n\n## Reviewer Divergence [REBUT]\n\n1. **ASV novelty severity**：R2 评 CRITICAL，R1 降为 MAJOR（R1 认为 monotonicity 非平凡性本身就是方法论贡献，只是论文未凸显）→ 最终采纳 **MAJOR**\n2. **Method section brevity** (SF-7)：R2 评 MAJOR，R1 REBUT 为 MINOR（8 页限制下合理权衡）→ 最终采纳 **MINOR**\n3. **83.4% framing** (SF-6)：R2 评 MAJOR，R1 partially AGREE 但纠正 Abstract 实际首先使用 realistic number → 最终维持 **MAJOR**（Section 4.2/Figure 2 仍需改进）\n4. **Commercial LLM** (SF-9)：R2 升为 MAJOR，R1 REBUT 维持 MINOR → 最终采纳 **MINOR**\n5. **矩阵覆盖充分性** (R1-W5)：R2 REBUT——20,000 对存在性验证目标 adequate（confidence > 99.99% for p=0.001 violation rate）→ 最终不列为 weakness\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Proposition 1(a) 的 sufficient condition (sign(τ)=sign(τ+B_OV)) 需要知道 B_OV 方向——实践者如何在不知道 B_OV 的情况下判断 sign preservation？ASV 框架能否间接回答此问题？ [R2-Q1, R1 AGREE]\n\n**Q2.** Table 9 (Appendix B.10) 显示 ASV ranking 依赖 β 配置。\"Vulnerability spectrum from IV to M-bias\" 是否仅端点（IV 最脆弱, M-bias 最稳健）稳定而中间排名可变？ [R2-Q2, R1 AGREE — 端点稳定，中间排名可变]\n\n**Q3.** Theorem 1 的 (C₀)_jj ≥ 1/2 条件在 K=10 (HumAID) 时是否对所有 j 成立？论文应报告 HumAID confusion matrices 的 per-class diagonal 分布。 [R1-Q1, R2 AGREE]\n\n**Q4.** Non-differential stress test 仅测试到 r=0.1。在 few-shot prompting 下 differential 程度可能远超——是否有更大 r 下的结果？ [R2-Q3, R1-W4 共同提出]\n\n**Q5.** IV 的 bootstrap ASV CI [0.44, 1.29] 跨越 δ=1 boundary。对 IV 拓扑，ASV point estimate 是否不可靠？论文应在 main text 提及此限制。 [R2-Q4, R1 AGREE]\n\n**Q6.** Conjecture 1 的 ε/η 精度：η 小时 ε/η 可以很大。R1 REBUT 认为 bootstrapping 缓解此问题（practical worst-case deviation 远小于 ε bound），但建议论文添加解释。 [R2-Q5, R1 REBUT with suggested addition]\n\n**Q7.** Algorithm 1 (p.26) 的 risk threshold 0.1 选择依据？不同 application domain 是否应使用不同 threshold？ [R2-Q6, R1 AGREE]\n\n---\n\n## Missing References\n\n**R2 建议（R1 AGREE partially）:**\n1. Wei, He, Li & Geng (2025) \"Multiply robust causal inference in the presence of an error-prone treatment\" — Statistical Methods in Medical Research. 直接处理 error-prone treatment 因果推断\n2. Demirel et al. (2024) \"Prediction-powered Generalization of Causal Inferences\" (ICML 2024) — PPI 在 causal setting 的 generalization\n3. Cheng et al. (2024) → 检查 2025 年 2 月更新版本是否已正式发表\n\n**R1 可选补充:**\n4. Fong, Hazlett, and Imai (2018) \"Covariate Balancing Propensity Score for a Continuous Treatment\" — 与 ASV 方法论有对话空间（非必需）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态: error**\n视觉审查 Agent 因 API 限额耗尽退出（\"You've hit your limit · resets 4pm (UTC)\"）。无排版审查结果可用。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4.0 | 3.5 | 3.75 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**置信度**: 4/5（两位 Reviewer 均有相关领域经验，仔细审查了推导和实验）\n\n**判断依据**:\n- 论文解决了一个 timely 且重要的问题（LLM annotation error × causal inference），跨 7 种 DAG 拓扑的系统比较是 genuinely novel 的综合贡献\n- 理论核心（FWL invariance、sign preservation proofs for confounding/collider）扎实\n- 实验验证多层次且 MAPE 1.6% 的 theory-MC agreement 令人信服\n- 但存在两类可修复问题阻碍达到 Conference 水准：\n  - (1) **声称与证据的匹配性**：primary coefficient claim 过强、ASV novelty 阐述不足\n  - (2) **验证范围的完整性**：stress test r 范围过窄、C₀ sensitivity 未分析、proportional effects 讨论不足\n\n**从 3.5 到 4.0 的路径**（两位 Reviewer 共识）:\n1. **MF-1**: 将 \"primary coefficient never reverses\" 降级为 empirical regularity，提供 sufficient condition 或讨论 breakdown regime\n2. **MF-2**: 重构 ASV novelty 叙事——聚焦 monotonicity 非平凡性和拓扑依赖性作为核心贡献\n3. **SF-1**: Proposition 2 命名反映数值验证性质\n4. **SF-3**: 扩展 non-differential stress test 到 r ≥ 0.3\n5. **SF-4**: 在 Section 3 开头和 Section 4.5 显著标注 linear scope\n\n如果 MF-1 和 MF-2 能 adequately address，加上 SF-1/SF-3/SF-4 的修改，论文可达到 **4.0 (Conference)** 水准。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度仍偏高（至少 8 个 specific 数字），但整体可读\n- \"the primary treatment effect does not reverse\" → 需降级为 empirical regularity (MF-1)\n- 数值（2.1% sign reversal under realistic accuracy）与 Section 4.2 一致\n\n### Introduction\n- Paragraph 1 的叙事逻辑清晰：LLM annotation 普及 → multi-class 是主流 → error propagation 依赖 structure 和 topology\n- Contribution 2 (ASV) 的 novelty 需加强阐述 (MF-2)\n- \"154×\" binarization claim 来源不透明 (SF-8)\n\n### Related Work\n- 覆盖面广泛且组织合理（measurement error / LLM annotation / sensitivity analysis 三条线）\n- 与 prior work 的差异化表述清晰\n- R1 确认引用覆盖充分；R2 建议补充 2-3 篇新引用\n\n### Method (Section 3)\n- Definition 1 (non-differential misclassification) 清晰严格\n- Confounding (Eq.1), Exposure (Eq.2), Mediation (Eq.3) 推导正确\n- Collider/M-bias/Front-door/IV 在 main text 仅有文字描述——8 页限制下可接受但应明确指向 appendix (SF-7)\n- Proposition 1(a)(b)(c) 证明正确；(a) 的 sufficient condition 需实践指导 (Q1)\n- Theorem 1 证明完整但 proportional effects 限制需讨论 (SF-2)\n- Proposition 2 命名需修正 (SF-1)\n- ASV 三种类型定义严格，但 ε threshold 选择缺乏讨论\n\n### Experiments (Section 4)\n- Theory-MC agreement MAPE 1.6% 令人信服\n- Figure 3 (F1 vs bias) 是论文中最 effective 的可视化\n- Table 1 格式清晰但 \"Violation\"/\"Amplif.\" 列需在 caption 中定义\n- Correction guidance (Section 4.5) \"no single method dominates\" 有实用价值\n- Section 4.2 呈现顺序应改进 (SF-6)\n\n### Conclusion & Limitations\n- Limitations 覆盖了主要 scope restrictions\n- 应补充商业 LLM 限制说明 (SF-9)\n\n### Appendix\n- 附录质量高，推导完整（Appendix A 共 10 页 proofs）\n- Appendix B.5 stress test r 范围过窄 (SF-3)\n- Appendix B.7 bootstrap CI 结果对 IV 的 implication 应在 main text 提及 (Q5)\n- Appendix B.10 ASV stability 显示中间拓扑排名可变——值得在 main text 提及 (Q2)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# Consolidated Review Report — Round 7\n\n**论文**: \"Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\"\n**Venue**: EMNLP 2026 (ACL ARR, Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**轮次**: Round 1（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文针对 K-class 非差异性错分类在 7 种经典 DAG 拓扑下的偏差传播进行系统性理论分析，推导 probability limit 表达式，建立 Annotation Sensitivity Values (ASV) 敏感性分析框架，并证明 FWL 不变性导致矩阵校正方法在 4 种拓扑下完全无效。论文通过 23 个真实 LLM 配置 × 7 拓扑 = 161 个场景的经验验证（MAPE 1.6%），确认理论预测。贡献扎实且问题 timely，但存在可修复的命名不当、声称过强和验证范围不足问题。\n\n---\n\n## Strengths\n\n**S1. 系统性跨拓扑比较的原创价值** [R1-S1, R2-S1, 双方一致]\n首次在统一线性 SEM 框架下推导全部 7 种拓扑的 bias 表达式，揭示同一混淆矩阵在不同拓扑下产生质量上不同的偏差（attenuating vs. amplifying vs. sign-reversing）。Teblunthuis (2024) 覆盖 4 种拓扑但限于 binary；Lee & Wood-Doughty (2024) 只分析 confounding。\"首次跨 7 种拓扑系统比较\"的声明在两位 Reviewer 的检索范围内成立。\n\n**S2. FWL 不变性负结果有实用价值** [R1-S3, R2-S2, 双方一致]\n证明 matrix-based correction 对 4 种 covariate 拓扑下完全无效（0% bias reduction）——基于 FWL 定理的代数性质，论证完整且优雅。对 practitioners 选择校正方法有直接指导意义。R1 仔细审查了 Appendix B.2 的推导，确认代数正确。\n\n**S3. 透明的三级证明层级** [R1-S2, R2-S4, 双方一致]\n明确区分 analytically proved（Proposition 1, Theorem 1）、numerically verified（Proposition 2, 100K+ matrices）和 conjectured（Conjecture 1, ε-approximate bounds）三个层次。这种方法论诚实度在投稿论文中不常见。\n\n**S4. 实验验证层次丰富** [R1-S5, R2-S3, 双方一致]\n23 LLM 配置 × 7 拓扑 = 161 scenarios，grand MAPE 1.6%。包含 cross-K robustness (K=5,7)、logistic DGP 验证、non-differential stress test、bootstrap ASV CI——不是单一实验而是多层验证体系。ClinicalBERT case study (Appendix B.3) 展示端到端应用。\n\n**S5. 实际问题导向** [R2-S5]\nFigure 3 (F1 vs bias) 有效说明\"F1 不预测因果风险\"：在 F1=0.614–0.690 窄区间内 bias 跨拓扑变化 10×。对 CSS 实践者有直接警示价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. [CRITICAL] \"Primary coefficient never reverses\" 声明的 evidence 不足以支撑其 prominence**\n[R2-N2 首发 CRITICAL, R1 完全 AGREE CRITICAL]\n\n- **位置**: Abstract (\"in all 23 empirical configurations tested, the primary treatment effect does not reverse\"), Section 3.2 footnote 2, Introduction paragraph 2\n- **问题**: 该声明在 abstract 和 introduction 中以近乎 structural property 的语气呈现，但：(a) 仅基于 23 个经验配置——样本量极小；(b) 解释仅为 footnote 2 的 heuristic（\"magnitude dominance\"）——无 formal sufficient condition；(c) 论文自身在 Section 3.2 已使用 \"empirical regularity\"，但 abstract 措辞未反映这一谨慎性；(d) 未讨论 breakdown regime（如多个 coefficient magnitude 接近时）\n- **R1 补充证据**: Appendix B.1 binarization 分析暗示在某些 K≥3 结构下 primary reversal 可能发生\n- **要求**: (a) Abstract 中明确标注 \"empirical regularity\"；(b) 提供 formal sufficient condition（如 diagonal dominance threshold + coefficient magnitude ratio）或讨论 breakdown regime；(c) 降低 claim prominence\n\n**MF-2. [MAJOR] ASV 框架与 E-value 的方法论差异需更清晰阐述**\n[R2-N1 首发 CRITICAL, R1 AGREE with nuance 降为 MAJOR]\n\n- **位置**: Section 3.3\n- **问题**: 论文列举的三个 ASV vs E-value 差异偏表面：(1) ε-approximate monotonicity proof 是验证任务非方法创新；(2) three ASV types 本质是同一 idea 用不同 threshold；(3) FWL combination 是 routing 应用\n- **R1 关键洞察**: 真正的方法论贡献被淹没——E-value 的 confounding 参数 Γ 的 monotonicity 是 trivially satisfied（Cinelli & Hazlett 2020 已证明），但 annotation error domain 中 monotonicity 非平凡（需 Theorem 1 + Conjecture 1），且拓扑依赖（confounding 递增, collider 递减）。这种 non-trivial topology-dependent monotonicity 是 E-value 框架中不存在的\n- **R1 降级理由**: ASV 不是 E-value 的简单搬运——monotonicity 非平凡性本身就是方法论贡献，只是论文未凸显\n- **要求**: 重构 ASV novelty 叙事——将 \"monotonicity is non-trivial and topology-dependent\" 作为核心方法论贡献阐述\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. [MAJOR] Proposition 2 命名与数值验证性质不匹配**\n[R1-W1 首发 MAJOR, R2 AGREE]\n\n- **位置**: Section 3.3 (page 5)\n- **问题**: Proposition 2 的 \"证明\" 实质是 20,000 组随机矩阵的数值验证；在数学惯例中 \"Proposition\" 意味已证结果。Conjecture 1 正确使用 \"Conjecture\"，命名不一致更凸显问题\n- **要求**: 改为 \"Numerical Result 1\" 或显式标注 \"supported by numerical evidence; analytic proof remains open\"\n\n**SF-2. [MAJOR] Theorem 1 的 proportional effects 假设 (f=λg) 讨论不足**\n[R1-W2 首发 MAJOR, R2 AGREE with nuance]\n\n- **位置**: Theorem 1 (page 5), Appendix A.4 (page 13)\n- **问题**: f=λg 在实际 NLP 场景（如政治立场 K=5）中不太可能严格成立。Appendix A.4 有 general case 数值验证（worst-case deviation < 0.005）但主文未充分引用\n- **R2 补充**: Proposition 2 + Conjecture 1 为 general case 提供数值支撑；但 ε/η 在 weak effect 下可能放大误差\n- **要求**: (a) 讨论 proportional effects 在 NLP 场景的合理性；(b) 主文引用 Appendix A.4 general case 数值验证\n\n**SF-3. [MAJOR] 非差异性错分类压力测试覆盖不足**\n[R1-W4 首发 MAJOR, R2 强烈 AGREE]\n\n- **位置**: Appendix B.5 (Table 7)\n- **问题**: 仅覆盖 r ∈ {0, 0.05, 0.1} 的 mild violations。实际场景（few-shot demonstrations 编码 outcome-treatment 关联, RLHF implicit correlations, RAG outcome signal）可能远超 r=0.1\n- **R2 补充**: 当前 r 定义是均匀扰动所有 off-diagonal entries——实际 violation 可能是 structured\n- **要求**: 扩展到 r ∈ {0.2, 0.3, 0.5}\n\n**SF-4. [MAJOR] 线性 SEM 范围限制标注不够显著**\n[R1-W7 首发 MINOR, R2-W1 首发 MAJOR, 交叉后共识 MAJOR]\n\n- **位置**: Section 3.1, Section 4.5\n- **问题**: Section 3.1 仅一句话提到 \"linear structural equations\"；FWL invariance 严格依赖线性假设但标注不突出\n- **R1 纠正 R2 事实错误**: Appendix B.6 实际测试了全部 7 种拓扑（非仅 exposure）。但 R2 核心论点成立：sign-flip rate stability ≠ FWL invariance preservation\n- **要求**: Section 3 开头和 Section 4.5 显著标注 linear scope\n\n**SF-5. [MAJOR] ASV 对 C₀ 选择的敏感性未充分分析**\n[R1-W3 首发 MAJOR, R2 AGREE]\n\n- **位置**: Section 3.3, Appendix B.7\n- **问题**: Bootstrap CI 回答了 sampling uncertainty，未回答不同 C₀ 估计方法的系统性差异。IV 的 95% CI [0.44, 1.29] 跨越 δ=1——point estimate 不可靠\n- **要求**: 增加 C₀ 扰动分析或讨论 ranking robustness 条件\n\n**SF-6. [MAJOR] 83.4% sign reversal 在 Section 4.2/Figure 2 中的呈现顺序有误导性**\n[R2-W3 首发 MAJOR, R1 AGREE partially]\n\n- **位置**: Section 4.2 paragraph 2, Figure 2 caption\n- **问题**: Dirichlet(1,1,1) prior 对角元素期望仅 1/K≈0.33，对 realistic classifiers 不合理\n- **R1 纠正**: Abstract 实际首先使用 realistic number (2.1%)；83.4% 主要出现在 Section 4.2 和 Figure 2\n- **要求**: Section 4.2 重排呈现顺序——先 realistic rate (2.1%)，再 Dirichlet 分析作为理论极端\n\n**SF-7. [MINOR] Method section 关键拓扑推导过于简略**\n[R2-W2 首发 MAJOR, R1 REBUT partially 降为 MINOR]\n\n- **问题**: Main text 仅给出 confounding/exposure/mediation 的公式，collider/M-bias/front-door/IV 仅有文字描述\n- **R1 论证**: 8 页限制下合理权衡，完整推导在 Appendix A.3-A.8（共 10 页证明）\n- **要求**: 添加一句声明指向 appendix\n\n**SF-8. [MINOR] \"154×\" binarization bias 倍数来源不透明**\n[R1-W6 首发 MINOR, R2 AGREE]\n\n- **位置**: Introduction Contribution 1\n- **要求**: 在 Appendix B.1 或正文中给出 154× 的具体计算基础\n\n**SF-9. [MINOR] 缺少商业 LLM 实验配置**\n[R2-W4 首发 MINOR→MAJOR, R1 REBUT partially 维持 MINOR]\n\n- **问题**: 4 个 LLM 全部开源。R1 论证：理论贡献不依赖具体 LLM，API 成本和 reproducibility 是合理理由\n- **要求**: Limitations 中讨论即可\n\n**SF-10. [MINOR] 引用格式不统一**\n[R2-W5 首发 MINOR, R1 AGREE]\n\n- **问题**: Pangakis et al. (2023), Cheng et al. (2024), Cadei et al. (2025) 标为 arXiv preprint 但正文未标注状态\n- **要求**: 统一标注 preprint 状态，检查是否已正式发表\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Primary coefficient claim 过强** (MF-1)：两位 Reviewer 均评为 CRITICAL——本轮最需修改的声称\n2. **ASV novelty 需更好阐述** (MF-2)：聚焦 monotonicity 非平凡性和拓扑依赖性\n3. **Proposition 2 命名不当** (SF-1)：应反映数值验证性质\n4. **Stress test 范围过窄** (SF-3)：r≤0.1 不足，需扩展到 r≥0.3\n5. **Linear scope 标注不足** (SF-4)：对 NLP/CSS 受众需更显著标注\n6. **核心理论贡献扎实**：7 拓扑 taxonomy、FWL invariance、三级证明体系均获双方肯定\n\n## Reviewer Divergence [REBUT]\n\n1. **ASV novelty severity**：R2 评 CRITICAL，R1 降为 MAJOR（R1 认为 monotonicity 非平凡性本身就是方法论贡献，只是论文未凸显）→ 最终采纳 **MAJOR**\n2. **Method section brevity** (SF-7)：R2 评 MAJOR，R1 REBUT 为 MINOR（8 页限制下合理权衡）→ 最终采纳 **MINOR**\n3. **83.4% framing** (SF-6)：R2 评 MAJOR，R1 partially AGREE 但纠正 Abstract 实际首先使用 realistic number → 最终维持 **MAJOR**（Section 4.2/Figure 2 仍需改进）\n4. **Commercial LLM** (SF-9)：R2 升为 MAJOR，R1 REBUT 维持 MINOR → 最终采纳 **MINOR**\n5. **矩阵覆盖充分性** (R1-W5)：R2 REBUT——20,000 对存在性验证目标 adequate（confidence > 99.99% for p=0.001 violation rate）→ 最终不列为 weakness\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Proposition 1(a) 的 sufficient condition (sign(τ)=sign(τ+B_OV)) 需要知道 B_OV 方向——实践者如何在不知道 B_OV 的情况下判断 sign preservation？ASV 框架能否间接回答此问题？ [R2-Q1, R1 AGREE]\n\n**Q2.** Table 9 (Appendix B.10) 显示 ASV ranking 依赖 β 配置。\"Vulnerability spectrum from IV to M-bias\" 是否仅端点（IV 最脆弱, M-bias 最稳健）稳定而中间排名可变？ [R2-Q2, R1 AGREE — 端点稳定，中间排名可变]\n\n**Q3.** Theorem 1 的 (C₀)_jj ≥ 1/2 条件在 K=10 (HumAID) 时是否对所有 j 成立？论文应报告 HumAID confusion matrices 的 per-class diagonal 分布。 [R1-Q1, R2 AGREE]\n\n**Q4.** Non-differential stress test 仅测试到 r=0.1。在 few-shot prompting 下 differential 程度可能远超——是否有更大 r 下的结果？ [R2-Q3, R1-W4 共同提出]\n\n**Q5.** IV 的 bootstrap ASV CI [0.44, 1.29] 跨越 δ=1 boundary。对 IV 拓扑，ASV point estimate 是否不可靠？论文应在 main text 提及此限制。 [R2-Q4, R1 AGREE]\n\n**Q6.** Conjecture 1 的 ε/η 精度：η 小时 ε/η 可以很大。R1 REBUT 认为 bootstrapping 缓解此问题（practical worst-case deviation 远小于 ε bound），但建议论文添加解释。 [R2-Q5, R1 REBUT with suggested addition]\n\n**Q7.** Algorithm 1 (p.26) 的 risk threshold 0.1 选择依据？不同 application domain 是否应使用不同 threshold？ [R2-Q6, R1 AGREE]\n\n---\n\n## Missing References\n\n**R2 建议（R1 AGREE partially）:**\n1. Wei, He, Li & Geng (2025) \"Multiply robust causal inference in the presence of an error-prone treatment\" — Statistical Methods in Medical Research. 直接处理 error-prone treatment 因果推断\n2. Demirel et al. (2024) \"Prediction-powered Generalization of Causal Inferences\" (ICML 2024) — PPI 在 causal setting 的 generalization\n3. Cheng et al. (2024) → 检查 2025 年 2 月更新版本是否已正式发表\n\n**R1 可选补充:**\n4. Fong, Hazlett, and Imai (2018) \"Covariate Balancing Propensity Score for a Continuous Treatment\" — 与 ASV 方法论有对话空间（非必需）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态: error**\n视觉审查 Agent 因 API 限额耗尽退出（\"You've hit your limit · resets 4pm (UTC)\"）。无排版审查结果可用。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4.0 | 3.5 | 3.75 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n**置信度**: 4/5（两位 Reviewer 均有相关领域经验，仔细审查了推导和实验）\n\n**判断依据**:\n- 论文解决了一个 timely 且重要的问题（LLM annotation error × causal inference），跨 7 种 DAG 拓扑的系统比较是 genuinely novel 的综合贡献\n- 理论核心（FWL invariance、sign preservation proofs for confounding/collider）扎实\n- 实验验证多层次且 MAPE 1.6% 的 theory-MC agreement 令人信服\n- 但存在两类可修复问题阻碍达到 Conference 水准：\n  - (1) **声称与证据的匹配性**：primary coefficient claim 过强、ASV novelty 阐述不足\n  - (2) **验证范围的完整性**：stress test r 范围过窄、C₀ sensitivity 未分析、proportional effects 讨论不足\n\n**从 3.5 到 4.0 的路径**（两位 Reviewer 共识）:\n1. **MF-1**: 将 \"primary coefficient never reverses\" 降级为 empirical regularity，提供 sufficient condition 或讨论 breakdown regime\n2. **MF-2**: 重构 ASV novelty 叙事——聚焦 monotonicity 非平凡性和拓扑依赖性作为核心贡献\n3. **SF-1**: Proposition 2 命名反映数值验证性质\n4. **SF-3**: 扩展 non-differential stress test 到 r ≥ 0.3\n5. **SF-4**: 在 Section 3 开头和 Section 4.5 显著标注 linear scope\n\n如果 MF-1 和 MF-2 能 adequately address，加上 SF-1/SF-3/SF-4 的修改，论文可达到 **4.0 (Conference)** 水准。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度仍偏高（至少 8 个 specific 数字），但整体可读\n- \"the primary treatment effect does not reverse\" → 需降级为 empirical regularity (MF-1)\n- 数值（2.1% sign reversal under realistic accuracy）与 Section 4.2 一致\n\n### Introduction\n- Paragraph 1 的叙事逻辑清晰：LLM annotation 普及 → multi-class 是主流 → error propagation 依赖 structure 和 topology\n- Contribution 2 (ASV) 的 novelty 需加强阐述 (MF-2)\n- \"154×\" binarization claim 来源不透明 (SF-8)\n\n### Related Work\n- 覆盖面广泛且组织合理（measurement error / LLM annotation / sensitivity analysis 三条线）\n- 与 prior work 的差异化表述清晰\n- R1 确认引用覆盖充分；R2 建议补充 2-3 篇新引用\n\n### Method (Section 3)\n- Definition 1 (non-differential misclassification) 清晰严格\n- Confounding (Eq.1), Exposure (Eq.2), Mediation (Eq.3) 推导正确\n- Collider/M-bias/Front-door/IV 在 main text 仅有文字描述——8 页限制下可接受但应明确指向 appendix (SF-7)\n- Proposition 1(a)(b)(c) 证明正确；(a) 的 sufficient condition 需实践指导 (Q1)\n- Theorem 1 证明完整但 proportional effects 限制需讨论 (SF-2)\n- Proposition 2 命名需修正 (SF-1)\n- ASV 三种类型定义严格，但 ε threshold 选择缺乏讨论\n\n### Experiments (Section 4)\n- Theory-MC agreement MAPE 1.6% 令人信服\n- Figure 3 (F1 vs bias) 是论文中最 effective 的可视化\n- Table 1 格式清晰但 \"Violation\"/\"Amplif.\" 列需在 caption 中定义\n- Correction guidance (Section 4.5) \"no single method dominates\" 有实用价值\n- Section 4.2 呈现顺序应改进 (SF-6)\n\n### Conclusion & Limitations\n- Limitations 覆盖了主要 scope restrictions\n- 应补充商业 LLM 限制说明 (SF-9)\n\n### Appendix\n- 附录质量高，推导完整（Appendix A 共 10 页 proofs）\n- Appendix B.5 stress test r 范围过窄 (SF-3)\n- Appendix B.7 bootstrap CI 结果对 IV 的 implication 应在 main text 提及 (Q5)\n- Appendix B.10 ASV stability 显示中间拓扑排名可变——值得在 main text 提及 (Q2)"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-23T00:05:11.854883+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4268
}
```

</details>

---


### Assistant

_source line 568 · 2026-05-23T00:05:24.955572+00:00_

审稿报告已投递。

**Round 7 审稿完成摘要**：

- **Overall: 3.5/5 (Borderline Conference)**，两位 Reviewer 评分一致
- **1 个 CRITICAL**：Abstract 中 "primary coefficient never reverses" 的 prominence 与 evidence 不匹配（仅 23 configs 经验观察）
- **1 个 MAJOR Must-Fix**：ASV vs E-value 方法论差异需重构——聚焦 monotonicity 非平凡性
- **6 个 MAJOR Should-Fix**：Proposition 2 命名、proportional effects 讨论、stress test r 范围、linear scope 标注、C₀ sensitivity、83.4% framing
- **从 3.5→4.0 路径明确**：MF-1/MF-2 + SF-1/SF-3/SF-4 修复后可达 Conference 水准
- **Issue Tracker 已同步**（R6-M1/M4/W3 标记 resolved，新增 7 条 R7 issues）
- **视觉审查**：Agent 因 API 限额退出，无结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 569 · 2026-05-23T00:05:27.874210+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R2 的 17 个观点，我给出了 **11 个 [AGREE]（含 6 个 partial agree）、1 个 [REBUT]（Q5 ε/η 精度问题）、1 个 partial REBUT（W2 推导简略）**。核心共识集中在：N2（primary coefficient claim prominence 过高）、Q3/W4（非差异性假设和商业 LLM 覆盖不足）。主要分歧在 N1——R2 认为 ASV 是 E-value 的简单应用，我认为 monotonicity 非平凡性本身构成方法论贡献，但论文确实需要更好地阐述这一区分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 570 · 2026-05-23T00:05:44.870704+00:00_

审稿报告已投递。

**Round 7 审稿完成摘要**：

- **Overall: 3.5 / 5 (Borderline Conference)**
- **1 轮收敛**，两位 Reviewer 在关键问题上达成共识
- **1 个 CRITICAL**：Abstract 中 "primary coefficient never reverses" 仅有 23 配置经验支撑，需降级为 empirical regularity 并提供 breakdown 条件
- **1 个 MAJOR Must-Fix**：ASV vs E-value 的核心方法论差异（monotonicity 非平凡性）被表面差异列举淹没，需重构叙事
- **6 个 MAJOR Should-Fix**：Proposition 2 命名、proportional effects 讨论、stress test r 范围、linear scope 标注、C₀ sensitivity、83.4% framing
- **从 3.5→4.0 路径明确**：MF-1/MF-2 + SF-1/SF-3/SF-4 修改后可达 Conference 水准
- Issue Tracker 已同步更新（R6-M1/R6-M4/R6-W3 标记为 resolved，新增 R7-SF1/R7-SF5/R7-SF6/R7-SF8/R7-MR1/R7-Q7）
- 视觉审查因 API 限额未完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 63

## Round 63

48 recorded events


### User

_source line 571 · 2026-05-23T01:24:25.326428+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-23T01:24:31.201632+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-23T01:24:31.302772+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-23T01:24:38.496642+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 575 · 2026-05-23T01:24:38.547252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-23T01:24:41.157686+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-23T01:24:41.860798+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-23T01:24:41.861295+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 579 · 2026-05-23T01:24:41.911753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-23T01:24:46.178343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-23T01:24:48.438340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-23T01:24:49.342211+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\input{related_work}
38	
39	\input{method}
40	
41	% ── Figures ──
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
46	\vspace{-6pt}
47	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
48	\label{fig:dag_taxonomy}
49	\end{figure*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-23T01:24:49.593734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-23T01:24:49.744945+00:00_

-rw-r--r-- 1 ubuntu ubuntu 897145 May 23 00:29 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-23T01:24:56.169985+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the web search results, here are the key submission guidelines and author instructions for EMNLP 2026 ARR (ACL Rolling Review):

## Key Submission Requirements

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the conference will be perfo
…[truncated 2098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 9991
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-23T01:25:03.800314+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 formatting guidelines page limit long paper short paper template",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 formatting guidelines page limit long paper short paper template",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-23T01:25:04.152140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-23T01:25:04.604547+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), the sign reversal rate is 2.1\%, exclusively in secondary coefficients---across all 23 empirical configurations tested, the primary coefficient does not reverse, an empirical regularity consistent with magnitude dominance in the misclassification-induced weighted sum rather than an algebraic guarantee. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-23T01:25:04.604899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-23T01:25:04.655427+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-23T01:25:09.123274+00:00_

Web search results for query: "ACL Rolling Review 2026 formatting guidelines page limit long paper short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Style Files and Formatting - ACL 2023","url":"https://2023.aclweb.org/calls/style_and_formatting/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Student Research Workshop - ACL 2026","url":"https://2026.aclweb.org/calls/student_research_workshop/"}]

Based on the search results for ACL Rolling Review 2026, here are the formatting guidelines for page limits:

## Page Limits

**Long Papers:** Long papers may consist of up to eight (8) pages of content, plus unlimited pages of references.

**Short Papers:** Short papers may consist of up to four (4) pages of content, plus unlimited pages of re
…[truncated 852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 5322
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-23T01:25:13.240387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-23T01:25:13.693466+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 1919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-23T01:25:13.744278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-23T01:25:14.296926+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This holds when the LLM annotates from source documents without access to outcome information. Violations arise from outcome-conditional prompting, few-shot demonstrations encoding $A$--$Y$ associations, or retrieval-augmented pipelines surfacing $Y$-correlated documents; practitioners can diagnose violations by testing $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on a gold-labeled subset (see Limitations).
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Throughout, we derive probability limits under \emph{linear} structural equation models; each role induces a different functional relationship between $C$ and the probability limit of the standard causal estimator, yielding topology-dependent bias.
17	
18	\subsection{Multi-Class Bias Expressions}
19	\label{sec:bias_expressions}
20	
21	For each topology, we derive the probabilit
…[truncated 11930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-23T01:25:14.347557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---
