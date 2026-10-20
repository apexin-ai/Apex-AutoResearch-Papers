# Director coordination — Part 6 of 11

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/0e/0e806c5d99edfa05e2ae.json)

## Round 153

### Tool call

_source line 1568 · 2026-05-22T20:58:14.648500+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 18 (fresh review)\n\n# ============================================================\n# R18 ISSUES — NEW OR RECURRING\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 partial ordering 中间层不稳健：cross-judge ρ=0.09 + SESOI margin-dependency 双重不稳定\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"首次发现 cross-judge ρ=0.09\"\n    - round: 16\n      reviewers: []\n      note: \"§5.2 limiting statement added, C2 scoped to robust extremes. Marked resolved.\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位 Reviewer 从不同角度重新发现同一问题。R1: SESOI ±15pp 过大，±10pp 下 mid-tier 仅 3/6 等价，power 降至 0.57。R2: cross-judge ρ=0.09 使 mid-tier ordering judge-dependent。两条独立证据链汇聚。R16 修复被认为不够——C2 仍列为 primary claim (Abstract/Intro)，与 §5.2 末段的 limiting statement 矛盾。\"\n  action_items:\n    - round: 18\n      action: \"将 C2 降级为 secondary/partially-supported claim；Abstract/Introduction 中明确限定为 robust extremes only；Table 2/Figure 2 对 authorization scope 做视觉标注；正文以多 margin 结果为主要呈现\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N2\"\n  summary: \"Judge identity 与 model identity 完全混淆，C4 无法独立解释\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"C1 不受影响（matched-pair），C4 完全混淆\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位 Reviewer 均 AGREE。R1: Figure 3 中 Claude 30.3% 可能部分反映 judge 偏差。R2 补充: C1 在 matched-pair 下不受影响但 C4 完全暴露。建议 §5.4 首段和 Figure 3 caption 明确声明 model-level rates 不可跨 judge 组比较。\"\n  action_items:\n    - round: 18\n      action: \"§5.4 首段和 Figure 3 caption 加 judge-model confound caveat；Limitations 中升级此问题的讨论\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N3\"\n  summary: \"TOST SESOI ±15pp 过大，C2 cluster 结构由 margin 选择决定\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1 首提。perturbation bound >2× 论证不严谨（noise floor ≠ SESOI）。±10pp 下仅 3/6 等价，power 0.57。R2 [AGREE] 并补充 noise floor 与 domain-relevant threshold 是不同概念。两位均认为正文应以多 margin 为主要呈现。\"\n  action_items:\n    - round: 18\n      action: \"正文 §4.6 和 §5.2 以多 margin 结果为主要呈现，不将 ±15pp 作为 primary；补充 domain-grounded SESOI 论证；讨论 ±10pp 下 C2 结构变化\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N4\"\n  summary: \"Taxonomy 增量贡献不足，contribution framing 需调整\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 首提，R1 AGREE with nuance。六类型取自已有工作无新类型，C3 inconclusive 削弱两层结构。incompleteness/cond prec 不是 strict ambiguity。与 DRIP-R 差异化论述过简。R1 认为 'first matched-pair causal study' claim 本身准确但 taxonomy 不应作为独立贡献。\"\n  action_items:\n    - round: 18\n      action: \"将 contribution 重心从 taxonomy 转移到因果方法论 + variance decomposition insight；taxonomy 降格为实验设计工具；§3 更显著讨论操作性定义偏离；§2 加强 DRIP-R 差异化\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N5\"\n  summary: \"'Disambiguation Neglect' 概念新颖性不足，自创术语过多\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 首提，R1 AGREE。本质是 Liu et al. 2023 ambiguity collapse 的 agentic settings 实证确认。4.6% awareness rate 是有价值的数据点但不支撑新术语。systematic nocuity 和 differential nocuity 是已有概念延伸。\"\n  action_items:\n    - round: 18\n      action: \"§6.2 将 Disambiguation Neglect 定位为 ambiguity collapse 的实证确认，减少新概念 framing；考虑减少自创术语数量\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W1\"\n  summary: \"Variance decomposition (Type III SS) 在 binary outcomes 上适用性存疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"R17 修复：permutation test + GLMM ICC 补充。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 仍指出 Tjur's R²=0.175 vs Type III 39.2% explained 差异暗示方法不一致。R2 AGREE 但认为 logistic regression 因子排序一致性是 mitigation factor。\"\n  action_items:\n    - round: 18\n      action: \"正文增加说明 Tjur's R² 与 Type III 度量不同维度，不可直接比较\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W2\"\n  summary: \"60.8% 残差方差未充分讨论对 clause-level auditing 实用性的影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1 首提，R2 AGREE。clause wording 22.4% 是最大可干预因子但 60.8% 残差意味着对话轨迹高度随机。Discussion 应加 perspective。\"\n  action_items:\n    - round: 18\n      action: \"Discussion 加段讨论残差方差对 auditing 实用性的影响，类比可干预风险因子框架\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W3\"\n  summary: \"Incompleteness confound：token-count proxy 粗糙 + Abstract 措辞模糊\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R17 修复：Limitations 加 token count 粗糙性句。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 仍指出。R1: OR=1.022 显著(p<0.001)，p=0.022 接近边界。R2: Abstract 'conditional on' 措辞模糊——读者可能误解为控制后效应仍为 49.2pp，但论文未报告 controlled effect size。R1 交叉回应补充：auth scope 有最大 token delta 但 violation 更低是间接 counter-evidence。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 中 '+49.2pp' 加更明确的 confound 限定；正文（非仅 Appendix）显著讨论此 confound\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W4\"\n  summary: \"Failure mode coding LLM circularity + κ=0.52 仅 moderate\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"Limitations 已有 human validation caveat\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位均 AGREE。MI 不能排除 LLM coder 系统映射。建议 50-100 条 human failure mode annotation。\"\n  action_items:\n    - round: 18\n      action: \"Camera-ready 对 50-100 条 traces 做 human failure mode annotation 作为 calibration\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W5\"\n  summary: \"SOPBench 效应量大幅下降 (+13.8pp vs +34.0pp)，3/5 模型未达个体显著\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R17: SOPBench replication added\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位均 AGREE 效应量下降显著。DeepSeek p=0.119, GPT-5.4 p=0.209 未达 individual significance。'Directional consistency' framing 过于乐观。正文 §5.1 仅一句话提及 SOPBench。\"\n  action_items:\n    - round: 18\n      action: \"正文更坦诚地讨论 SOPBench 效应量下降和个体非显著性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W6\"\n  summary: \"Coreferential 排除出 replication/mitigation 与 confound-free lower bound 地位矛盾\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"Limitations 加了 coreferential caveat\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位 AGREE。+18.7pp 仅基于 primary 5-model，human-LLM κ 最低 (0.479)，不在 7-model replication 中。三点叠加使 coreferential 证据最薄弱——与 confound-free 地位矛盾。\"\n  action_items:\n    - round: 18\n      action: \"Limitations 明确承认 coreferential 证据薄弱与 confound-free 地位的 tension\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W7\"\n  summary: \"Abstract 数字过载 (15+ 数字在 ~200 词中)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2, R1]\n      note: \"R2 首提，R1 部分同意。建议保留 3-5 个关键数字，其余用定性语言。R1 建议保留 C1 核心(34.0pp, OR=15.1)、variance decomposition(22.4% vs 0.4%)、17× ratio。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 精简至 5-7 个关键数字，移除 per-type range 和 awareness rate 细节\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W8\"\n  summary: \"主文超出 8 页限制约 4 行 (Conclusion 在第 9 页)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 14\n      reviewers: [visual_check]\n      note: \"首次发现超页\"\n    - round: 15\n      reviewers: []\n      note: \"修复至 ≤8 页\"\n    - round: 18\n      reviewers: [R2, R1, visual_check]\n      note: \"R18 再次复发。R2 和 visual check 均确认 Conclusion 标题+全文(约 4 行)在第 9 页顶部。R1 验证 PDF 确认。EMNLP 2026 strict 8-page limit，有 desk reject 风险。\"\n  action_items:\n    - round: 18\n      action: \"压缩 §7 Discussion 或 §6 Error Analysis 将 Conclusion 拉回第 8 页\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W9\"\n  summary: \"Conclusion 泛化声明超出证据范围 (仅 customer service 领域)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R17 修复：§7 加了 domain distinction\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Conclusion 仍写 'critical for policy-governed deployments' 未限定领域。SOPBench 效应量降 60% 进一步限制泛化性。\"\n  action_items:\n    - round: 18\n      action: \"Conclusion 限定 claim 领域范围\"\n      assigned_to: agent\n      status: open\n\n# ============================================================\n# R18 MINOR — CAMERA-READY\n# ============================================================\n\n- id: \"R18-M1\"\n  summary: \"17× vs 16.8× NMI ratio 不一致 (Abstract vs Appendix)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n\n- id: \"R18-M2\"\n  summary: \"ICC 双数字 (0.386 vs 0.189) 未充分解释 discrepancy\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n\n- id: \"R18-M3\"\n  summary: \"Bootstrap cluster AU p=0.47 在正文引用时未提及弱确认力\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n\n- id: \"R18-M4\"\n  summary: \"ferrari_defects_2018 bib entry 标 2018 但实际发表 2019\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n- id: \"R18-M5\"\n  summary: \"Mu et al. (2023) 在 bib 中但未在正文引用 (orphan entry)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n- id: \"R18-M6\"\n  summary: \"Pages 4-6 连续纯文本无 figure/table 穿插 (视觉节奏问题)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [visual_check]\n    - round: 18\n      reviewers: [visual_check]\n      note: \"p4-6 连续 3 页纯文本 + p8 又一页纯文本。p4-p8 中 4/5 页纯文本。\"\n\n- id: \"R18-M7\"\n  summary: \"Page 7 三个 display items 堆叠 (Table 2 + Figure 2 + Figure 3)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [visual_check]\n      note: \"Figure 2 和 Figure 3 被压缩。Figure 3 坐标轴标签 6-7pt 接近可读性下限。\"\n\n- id: \"R18-M8\"\n  summary: \"§2 'extends WSD to policy-specific polysemy' 用词不当\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n- id: \"R18-M9\"\n  summary: \"Discussion 仅 3 段，practical implications 讨论不足\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n# ============================================================\n# HISTORICAL — PREVIOUSLY RESOLVED (from R15-R17)\n# ============================================================\n\n- id: \"R15F-N1\"\n  summary: \"'Intervention-design framework' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"全文 → diagnostic taxonomy for failure-mechanism prediction\"\n  resolution_round: 16\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化，夸大约 2 倍\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"7 处替换完成。Appendix S 补充 NMI 说明。\"\n  resolution_round: 17\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test + GLMM ICC 补充。\"\n  resolution_round: 17\n\n- id: \"R17-M1\"\n  summary: \"Systematic nocuity threshold sensitivity\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§6.3 加 ≥2/5, ≥4/5, 5/5 比例。\"\n  resolution_round: 17\n\n- id: \"R17-M6\"\n  summary: \"'Nocuous' 对非母语读者不直观\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Abstract 加 'nocuous (i.e., harmful)'\"\n  resolution_round: 17\n\n- id: \"R11-C1\"\n  summary: \"Type 0.4% variance vs title/narrative tension\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Title refocused on clause-level. Taxonomy → diagnostic tool via MI.\"\n  resolution_round: 16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 18 (fresh review)\n\n# ============================================================\n# R18 ISSUES — NEW OR RECURRING\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 partial ordering 中间层不稳健：cross-judge ρ=0.09 + SESOI margin-dependency 双重不稳定\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"首次发现 cross-judge ρ=0.09\"\n    - round: 16\n      reviewers: []\n      note: \"§5.2 limiting statement added, C2 scoped to robust extremes. Marked resolved.\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位 Reviewer 从不同角度重新发现同一问题。R1: SESOI ±15pp 过大，±10pp 下 mid-tier 仅 3/6 等价，power 降至 0.57。R2: cross-judge ρ=0.09 使 mid-tier ordering judge-dependent。两条独立证据链汇聚。R16 修复被认为不够——C2 仍列为 primary claim (Abstract/Intro)，与 §5.2 末段的 limiting statement 矛盾。\"\n  action_items:\n    - round: 18\n      action: \"将 C2 降级为 secondary/partially-supported claim；Abstract/Introduction 中明确限定为 robust extremes only；Table 2/Figure 2 对 authorization scope 做视觉标注；正文以多 margin 结果为主要呈现\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N2\"\n  summary: \"Judge identity 与 model identity 完全混淆，C4 无法独立解释\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"C1 不受影响（matched-pair），C4 完全混淆\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位 Reviewer 均 AGREE。R1: Figure 3 中 Claude 30.3% 可能部分反映 judge 偏差。R2 补充: C1 在 matched-pair 下不受影响但 C4 完全暴露。建议 §5.4 首段和 Figure 3 caption 明确声明 model-level rates 不可跨 judge 组比较。\"\n  action_items:\n    - round: 18\n      action: \"§5.4 首段和 Figure 3 caption 加 judge-model confound caveat；Limitations 中升级此问题的讨论\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N3\"\n  summary: \"TOST SESOI ±15pp 过大，C2 cluster 结构由 margin 选择决定\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1 首提。perturbation bound >2× 论证不严谨（noise floor ≠ SESOI）。±10pp 下仅 3/6 等价，power 0.57。R2 [AGREE] 并补充 noise floor 与 domain-relevant threshold 是不同概念。两位均认为正文应以多 margin 为主要呈现。\"\n  action_items:\n    - round: 18\n      action: \"正文 §4.6 和 §5.2 以多 margin 结果为主要呈现，不将 ±15pp 作为 primary；补充 domain-grounded SESOI 论证；讨论 ±10pp 下 C2 结构变化\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N4\"\n  summary: \"Taxonomy 增量贡献不足，contribution framing 需调整\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 首提，R1 AGREE with nuance。六类型取自已有工作无新类型，C3 inconclusive 削弱两层结构。incompleteness/cond prec 不是 strict ambiguity。与 DRIP-R 差异化论述过简。R1 认为 'first matched-pair causal study' claim 本身准确但 taxonomy 不应作为独立贡献。\"\n  action_items:\n    - round: 18\n      action: \"将 contribution 重心从 taxonomy 转移到因果方法论 + variance decomposition insight；taxonomy 降格为实验设计工具；§3 更显著讨论操作性定义偏离；§2 加强 DRIP-R 差异化\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-N5\"\n  summary: \"'Disambiguation Neglect' 概念新颖性不足，自创术语过多\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 首提，R1 AGREE。本质是 Liu et al. 2023 ambiguity collapse 的 agentic settings 实证确认。4.6% awareness rate 是有价值的数据点但不支撑新术语。systematic nocuity 和 differential nocuity 是已有概念延伸。\"\n  action_items:\n    - round: 18\n      action: \"§6.2 将 Disambiguation Neglect 定位为 ambiguity collapse 的实证确认，减少新概念 framing；考虑减少自创术语数量\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W1\"\n  summary: \"Variance decomposition (Type III SS) 在 binary outcomes 上适用性存疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"R17 修复：permutation test + GLMM ICC 补充。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 仍指出 Tjur's R²=0.175 vs Type III 39.2% explained 差异暗示方法不一致。R2 AGREE 但认为 logistic regression 因子排序一致性是 mitigation factor。\"\n  action_items:\n    - round: 18\n      action: \"正文增加说明 Tjur's R² 与 Type III 度量不同维度，不可直接比较\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W2\"\n  summary: \"60.8% 残差方差未充分讨论对 clause-level auditing 实用性的影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1 首提，R2 AGREE。clause wording 22.4% 是最大可干预因子但 60.8% 残差意味着对话轨迹高度随机。Discussion 应加 perspective。\"\n  action_items:\n    - round: 18\n      action: \"Discussion 加段讨论残差方差对 auditing 实用性的影响，类比可干预风险因子框架\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W3\"\n  summary: \"Incompleteness confound：token-count proxy 粗糙 + Abstract 措辞模糊\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R17 修复：Limitations 加 token count 粗糙性句。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 仍指出。R1: OR=1.022 显著(p<0.001)，p=0.022 接近边界。R2: Abstract 'conditional on' 措辞模糊——读者可能误解为控制后效应仍为 49.2pp，但论文未报告 controlled effect size。R1 交叉回应补充：auth scope 有最大 token delta 但 violation 更低是间接 counter-evidence。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 中 '+49.2pp' 加更明确的 confound 限定；正文（非仅 Appendix）显著讨论此 confound\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W4\"\n  summary: \"Failure mode coding LLM circularity + κ=0.52 仅 moderate\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"Limitations 已有 human validation caveat\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位均 AGREE。MI 不能排除 LLM coder 系统映射。建议 50-100 条 human failure mode annotation。\"\n  action_items:\n    - round: 18\n      action: \"Camera-ready 对 50-100 条 traces 做 human failure mode annotation 作为 calibration\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W5\"\n  summary: \"SOPBench 效应量大幅下降 (+13.8pp vs +34.0pp)，3/5 模型未达个体显著\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R17: SOPBench replication added\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位均 AGREE 效应量下降显著。DeepSeek p=0.119, GPT-5.4 p=0.209 未达 individual significance。'Directional consistency' framing 过于乐观。正文 §5.1 仅一句话提及 SOPBench。\"\n  action_items:\n    - round: 18\n      action: \"正文更坦诚地讨论 SOPBench 效应量下降和个体非显著性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W6\"\n  summary: \"Coreferential 排除出 replication/mitigation 与 confound-free lower bound 地位矛盾\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1]\n      note: \"Limitations 加了 coreferential caveat\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 两位 AGREE。+18.7pp 仅基于 primary 5-model，human-LLM κ 最低 (0.479)，不在 7-model replication 中。三点叠加使 coreferential 证据最薄弱——与 confound-free 地位矛盾。\"\n  action_items:\n    - round: 18\n      action: \"Limitations 明确承认 coreferential 证据薄弱与 confound-free 地位的 tension\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W7\"\n  summary: \"Abstract 数字过载 (15+ 数字在 ~200 词中)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2, R1]\n      note: \"R2 首提，R1 部分同意。建议保留 3-5 个关键数字，其余用定性语言。R1 建议保留 C1 核心(34.0pp, OR=15.1)、variance decomposition(22.4% vs 0.4%)、17× ratio。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 精简至 5-7 个关键数字，移除 per-type range 和 awareness rate 细节\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W8\"\n  summary: \"主文超出 8 页限制约 4 行 (Conclusion 在第 9 页)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 14\n      reviewers: [visual_check]\n      note: \"首次发现超页\"\n    - round: 15\n      reviewers: []\n      note: \"修复至 ≤8 页\"\n    - round: 18\n      reviewers: [R2, R1, visual_check]\n      note: \"R18 再次复发。R2 和 visual check 均确认 Conclusion 标题+全文(约 4 行)在第 9 页顶部。R1 验证 PDF 确认。EMNLP 2026 strict 8-page limit，有 desk reject 风险。\"\n  action_items:\n    - round: 18\n      action: \"压缩 §7 Discussion 或 §6 Error Analysis 将 Conclusion 拉回第 8 页\"\n      assigned_to: agent\n      status: open\n\n- id: \"R18-W9\"\n  summary: \"Conclusion 泛化声明超出证据范围 (仅 customer service 领域)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R17 修复：§7 加了 domain distinction\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Conclusion 仍写 'critical for policy-governed deployments' 未限定领域。SOPBench 效应量降 60% 进一步限制泛化性。\"\n  action_items:\n    - round: 18\n      action: \"Conclusion 限定 claim 领域范围\"\n      assigned_to: agent\n      status: open\n\n# ============================================================\n# R18 MINOR — CAMERA-READY\n# ============================================================\n\n- id: \"R18-M1\"\n  summary: \"17× vs 16.8× NMI ratio 不一致 (Abstract vs Appendix)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n\n- id: \"R18-M2\"\n  summary: \"ICC 双数字 (0.386 vs 0.189) 未充分解释 discrepancy\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n\n- id: \"R18-M3\"\n  summary: \"Bootstrap cluster AU p=0.47 在正文引用时未提及弱确认力\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n\n- id: \"R18-M4\"\n  summary: \"ferrari_defects_2018 bib entry 标 2018 但实际发表 2019\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n- id: \"R18-M5\"\n  summary: \"Mu et al. (2023) 在 bib 中但未在正文引用 (orphan entry)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n- id: \"R18-M6\"\n  summary: \"Pages 4-6 连续纯文本无 figure/table 穿插 (视觉节奏问题)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [visual_check]\n    - round: 18\n      reviewers: [visual_check]\n      note: \"p4-6 连续 3 页纯文本 + p8 又一页纯文本。p4-p8 中 4/5 页纯文本。\"\n\n- id: \"R18-M7\"\n  summary: \"Page 7 三个 display items 堆叠 (Table 2 + Figure 2 + Figure 3)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [visual_check]\n      note: \"Figure 2 和 Figure 3 被压缩。Figure 3 坐标轴标签 6-7pt 接近可读性下限。\"\n\n- id: \"R18-M8\"\n  summary: \"§2 'extends WSD to policy-specific polysemy' 用词不当\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n- id: \"R18-M9\"\n  summary: \"Discussion 仅 3 段，practical implications 讨论不足\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R2]\n\n# ============================================================\n# HISTORICAL — PREVIOUSLY RESOLVED (from R15-R17)\n# ============================================================\n\n- id: \"R15F-N1\"\n  summary: \"'Intervention-design framework' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 16\n  resolution: \"全文 → diagnostic taxonomy for failure-mechanism prediction\"\n  resolution_round: 16\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化，夸大约 2 倍\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"7 处替换完成。Appendix S 补充 NMI 说明。\"\n  resolution_round: 17\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test + GLMM ICC 补充。\"\n  resolution_round: 17\n\n- id: \"R17-M1\"\n  summary: \"Systematic nocuity threshold sensitivity\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"§6.3 加 ≥2/5, ≥4/5, 5/5 比例。\"\n  resolution_round: 17\n\n- id: \"R17-M6\"\n  summary: \"'Nocuous' 对非母语读者不直观\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Abstract 加 'nocuous (i.e., harmful)'\"\n  resolution_round: 17\n\n- id: \"R11-C1\"\n  summary: \"Type 0.4% variance vs title/narrative tension\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Title refocused on clause-level. Taxonomy → diagnostic tool via MI.\"\n  resolution_round: 16"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-22T20:58:14.750571+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 13276}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-22T21:01:19.446152+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告 — Round 18 (Fresh Review)\n\n**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿，无上轮记忆)\n**Reviewer 编排**: 2 人 — R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量\n**交叉回应**: 完成，所有 critical issues 达成共识\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下因歧义导致安全违规的因果效应。采用匹配对设计在 τ²-bench 上构造 300 对歧义/非歧义 clause pairs，跨 6 种歧义类型和 5 个模型评估 2,997 个 episodes。核心发现：歧义 clause 使违规率增加 34.0pp (conditional OR=15.1)；clause 措辞解释 22.4% 方差远超 type (0.4%) 和 model (1.0%)；type 预测 failure mechanism 比预测 violation rate 强 17×。\n\n---\n\n## Strengths\n\n**S1.** [R1+R2 共识] **匹配对因果设计是方法论亮点**。相比 DRIP-R 的 correlational 设计，本文通过最小编辑配对隔离歧义因果效应，加上扰动控制（Δ_perturb = −0.67pp, CI 含零）确认 specificity to semantic ambiguity。这是 agent policy compliance 领域首个严格的因果推断设计。\n\n**S2.** [R1+R2 共识] **C1 证据极其稳健**。34.0pp 效应在 7 个模型（5+2 replication）、2 个 benchmark（τ²-bench + SOPBench）、多 severity threshold 下方向一致。排除 incompleteness 后 Δ=31.0pp (p<10⁻⁷⁵) 仍然显著，证明效应不依赖任何单一 type。\n\n**S3.** [R1+R2 共识] **Variance decomposition + NMI repositioning 是论文最有价值的原创洞察**。\"Clause wording drives risk (22.4%), type drives mechanism (17× NMI)\" 的发现重新定义了 taxonomy 在 agent safety 中的角色——从 risk predictor 转为 diagnostic tool。这个 framing 有概念新意且有方法论支撑。\n\n**S4.** [R1+R2 共识] **Claims 与 evidence 自觉对齐**。C3 报 inconclusive，C4 标 exploratory，taxonomy 重新定位——论文没有过度声称。18 个附录提供详尽敏感性分析，可审查性高。Limitations 部分对所有已知弱点（cross-judge ρ=0.09, incompleteness confound, ICC OpenAI-only 等）的披露非常坦诚。\n\n**S5.** [R2] **统计分析远超同类实证研究水准**。TOST equivalence testing + bootstrap cluster + permutation tests + Holm-Bonferroni correction + logistic regression confound control + cross-benchmark replication，方法论工具箱完整。\n\n**S6.** [R2] **引用真实性已验证**。所有 2026 年 arXiv preprint 引用均为真实存在的论文。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, R1+R2 共识] **C2 \"partial ordering\" 作为 primary claim 缺乏稳健性——cross-judge 不稳定 + SESOI margin-dependency 双重打击**\n\nC2 被列为两个 primary claims 之一（Abstract, Introduction §1），但存在两条独立的不稳定源：\n\n(a) *Cross-judge instability*（R1-N1, R2-W2 → 交叉后升级为共识 critical）：两个 judge group 的 type ranking Spearman ρ=0.09 (p=0.87, Appendix P)，本质为零。排除 authorization scope 后 ρ=0.90，但 authorization scope 的排除虽有独立方法论理由（κ=0.385 最低, agent composition effect），仍引入 researcher degrees of freedom。C2 的 mid-tier ordering 在不同 judge 组下完全不同。\n\n(b) *SESOI margin-dependency*（R1-N3, R2 交叉回应 AGREE）：±15pp margin 下 6/6 mid-tier pairs 等价，但 ±10pp 下仅 3/6，TOST power 从 0.94 降至 0.57。论文用 \"exceeding perturbation control bound by >2×\" 论证 SESOI——但 perturbation bound 是 noise floor，SESOI 是 domain-relevant threshold，两个概念不可混用。12pp 的 type 差异在 deployment 中已有实际意义，但 ±15pp 会判为\"等价\"。\n\n两条证据链汇聚到同一结论：**C2 作为 primary claim 仅在极端类型上成立（incompleteness 最高、coreferential 最低），mid-tier ordering 不可信。** §5.2 末段已表达了类似限定（\"establishing robust extremes...rather than a complete linear ordering\"），但这与 C2 的 primary claim 地位矛盾。\n\n→ **建议**：将 C2 降级为 secondary/partially-supported；Abstract/Introduction 限定为 robust extremes only；Table 2/Figure 2 对 authorization scope 做视觉标注（如 dagger）；正文以多 margin 结果为主要呈现而非以 ±15pp 为 primary。\n\n---\n\n**N2** [critical, R1+R2 共识] **Judge identity 与 model identity 完全混淆**\n\nGPT-5.4 评判 Claude/GPT-4.1/Qwen3；GPT-4.1 评判 GPT-5.4/DeepSeek。每个 model 只有一个 judge，两个 judge 都是 OpenAI 家族。\n\n- C1 不受此 confound 影响（matched-pair 下 judge bias 在 Δpp 中相消，§4.4 正确指出）\n- C4 完全暴露：Figure 3 中 Claude 最低 30.3% vs DeepSeek 最高 49.7% 的 model main effect 无法与 judge effect 分离。Authorization scope 的 52pp model range（该类型驱动 C4 interaction）可能部分是 judge artifact\n- Same-family leniency/severity 无法排除\n\n这是不可追溯修复的实验设计缺陷（除非追加实验）。\n\n→ **建议**：§5.4 首段和 Figure 3 caption 明确声明 \"model-level absolute violation rates are confounded with judge identity and are not directly comparable across judge groups\"；至少对一个 model 用两个 judge 评判以量化 judge effect。\n\n---\n\n**N3** [critical, R2 首提, R1 AGREE with nuance] **Taxonomy 增量贡献不足，contribution framing 需调整**\n\n六种 type 直接取自 Li et al. (2024) 和 Massey et al. (2014)，无新类型引入。两层结构（linguistic vs. specification）的理论价值被 C3 inconclusive（不过 Holm-Bonferroni，§5.3）削弱。6 种 type 中 2 种（incompleteness, conditional precedence）严格来说不是 linguistic ambiguity——§3 \"Scope of 'ambiguity'\" 承认这一点但辩护不够显著。与 DRIP-R (2026) 的差异化论述（§2 最后一段）过于简略——未论证为什么 safety violations 比 decision quality 是更重要的度量。\n\n→ **建议**：将 contribution 重心从 taxonomy 转移到因果方法论 + variance decomposition insight；taxonomy 降格为实验设计工具而非独立贡献；§3 更显著讨论操作性定义偏离；§2 加强与 DRIP-R 差异化论证。\n\n---\n\n**N4** [critical, R2 首提, R1 AGREE] **\"Disambiguation Neglect\" 概念新颖性不足**\n\nLiu et al. (2023) 已证明 LLMs \"fail to represent ambiguity, collapsing multiple interpretations into a single output\"。Gur-Arieh et al. (2026) 系统化了 \"ambiguity collapse\" 风险分类。本文的 \"Disambiguation Neglect\" 本质是 ambiguity collapse 在 agentic settings 的观测实例，核心区别仅在于不可逆后果（§6.2: \"the result is irreversible policy violation\"）。4.6% awareness rate 是有价值的实证数据点，但 framing 为带专属术语的新概念过度。\"Systematic nocuity\" 和 \"differential nocuity\" 同样是 Berry & Kamsties (2004) / Willis et al. (2008) 概念的直接延伸。\n\n→ **建议**：将 Disambiguation Neglect 定位为 ambiguity collapse 的实证确认而非概念创新；减少自创术语（\"systematic nocuity\" → \"convergent violations\"）；更充分地与 Gur-Arieh et al. (2026) 的 epistemic risk taxonomy 对话。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, R1+R2] **Variance decomposition 在 binary outcomes 上的适用性**：Type III SS 在 binary outcome 上近似 LPM，22.4% 来自 LPM。Tjur's R²=0.175 与 Type III 39.2% explained variance 差异暗示方法不一致。Logistic regression 因子排序一致性（Appendix H）是 mitigation factor，但应在正文说明两者度量不同维度。\n\n**W2** [warning, R1+R2] **60.8% 残差方差未充分讨论**：condition + clause wording 仅解释 ~38% 方差。论文推荐 clause-level auditing（Conclusion）但未讨论 60.8% 随机方差（conversation trajectory, user-simulator stochasticity）对实用性的影响。22.4% 仍是最大可干预因子，但 Discussion 应加入这个 perspective。\n\n**W3** [warning, R1+R2] **Incompleteness confound 需更显著讨论**：49.2pp effect 是 ambiguity resolution + information addition 的混合效应。Token count 作为 information proxy 粗糙（OR=1.022 显著, p<0.001）。Logistic regression 后 p=0.022 接近边界。Abstract \"conditional on an information-addition confound\" 措辞模糊——未报告 controlled effect size。Auth scope 有最大 token delta 但 violation 更低是间接 counter-evidence。正文（非仅 Appendix）应显著讨论。\n\n**W4** [warning, R1+R2] **Failure mode coding LLM circularity**：MI 提供结构性反循环证据，但不能排除 LLM coder 系统映射。κ=0.52 仅 moderate。建议 camera-ready 对 50-100 条 traces 做 human failure mode annotation。\n\n**W5** [warning, R1+R2] **SOPBench 效应量大幅下降**：+13.8pp vs +34.0pp（降 60%），仅 3/5 模型达个体显著性（DeepSeek p=0.119, GPT-5.4 p=0.209）。\"Directional consistency\" framing 可能过于乐观。正文 §5.1 仅一句话提及，应更坦诚讨论。\n\n**W6** [warning, R1+R2] **Coreferential 排除矛盾**：作为唯一 zero-token-delta type，coreferential 是最 clean 的 confound-free evidence (+18.7pp)——但被排除出 mitigation 和 replication。加上 human-LLM κ 最低 (0.479)，三点叠加使其证据最薄弱，与 confound-free 地位矛盾。Limitations 应明确承认此 tension。\n\n**W7** [warning, R2, R1 部分同意] **Abstract 数字过载**：~200 词 abstract 中 15+ 个数字，核心信息被淹没。建议保留 5-7 个关键数字（34.0pp, OR=15.1, 22.4% vs 0.4%, 17×），其余用定性语言。\n\n**W8** [critical/format, R2+R1+visual check] **主文超出 8 页限制约 4 行**：Conclusion (§8) 标题和全文出现在第 9 页顶部。EMNLP 2026 strict 8-page limit，有 desk reject 风险。建议压缩 §7 Discussion 将 Conclusion 拉回第 8 页。\n\n**W9** [warning, R1+R2] **Conclusion 泛化声明超出证据范围**：\"clause-level auditing is critical for policy-governed deployments\" 未限定领域（仅 customer service）。SOPBench 效应量降 60% 进一步限制泛化性。\n\n---\n\n## Reviewer Consensus\n\n以下 issues 两位 Reviewer 在交叉回应中明确达成共识（均 [AGREE]）：\n\n1. **C2 mid-tier ordering 不稳健**：R1 从 SESOI margin-dependency 角度 + R2 从 cross-judge ρ=0.09 角度 → 汇聚同一结论\n2. **Judge-model confound 影响 C4**：R1 首提，R2 完全同意并补充 C1 不受影响的论证\n3. **Incompleteness confound 需更好的 proxy**：R1-W3 ≈ R2-W1，双方一致\n4. **\"Disambiguation Neglect\" 新颖性有限**：R2 首提，R1 完全同意（\"§6.2 自己承认了延伸性质\"）\n5. **SOPBench 效应量下降需更坦诚讨论**：R1-W5 ≈ R2 交叉回应\n6. **主文超页需修复**：R2 首发现，R1 验证 PDF 确认\n\n## Reviewer Divergence\n\n无重大未解决分歧。微小差异：\n\n- R2 将 cross-judge ρ=0.09 列为 Should-Fix (W2)，R1 列为 Must-Fix (N1)。**交叉后 R2 同意升级为 critical**（\"综合来看，应升级为 critical——两个独立的不稳定源叠加使问题更严重\"）。\n- R1 认为 \"first matched-pair causal study\" claim 表述准确，R2 认为需进一步限定（2/6 type 非 strict ambiguity）。分歧已在交叉中收敛——R1 同意 taxonomy framing 应调整但 causal claim 本身准确。\n\n---\n\n## Questions\n\n1. 如果用 Claude 或 Gemini 作为 judge 评判 GPT 模型的 traces，C4 的 model ranking 是否改变？这是检验 judge-model confound 的直接实验。\n2. 在 ±10pp margin 下，C2 的 mid-tier cluster 从 4 types 缩减到 2 pairs——作者如何论证 ±15pp 而非 ±10pp 是\"正确\"的 SESOI？是否有 deployment scenario 可以锚定？\n3. 60.8% 残差方差中，conversation trajectory 和 user-simulator stochasticity 各占多少？是否可以通过固定 user-simulator seed 来分解？\n4. Incompleteness 控制 token delta 后的 controlled effect size 是多少？（Appendix F 仅报告 p=0.022 但未报告 controlled Δpp）\n5. 论文引用了 Mu et al. (2023) \"Can LLMs Follow Simple Rules?\" 在 bib 中但未在正文引用——这篇论文与 policy compliance 直接相关，是有意排除还是遗漏？\n\n---\n\n## Missing References\n\n论文的 related work 覆盖面已相当全面（R2 验证了所有 2026 引用的真实性）。以下供参考：\n\n- **Mu et al. (2023)** \"Can LLMs Follow Simple Rules?\" — 已在 bib 中但未引用，研究 LLM 规则遵循能力，与 policy compliance 直接相关\n- **Structured policy representation / policy formalization** 方向的工作——论文讨论 clause-level auditing 但未讨论 policy formalization 作为替代方案\n- 近期 **constitutional AI / rule-following** 实证研究（2025-2026 如有）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (耗时约 4 分钟)\n\n| 严重度 | 发现 |\n|--------|------|\n| **critical** | 主文本（Section 1-8）超出 8 页限制，Conclusion 完整位于第 9 页顶部，约 8.5 页。存在 desk reject 风险。 |\n| **warning** | Pages 4-6 连续 3 页纯文本（Method + Results 开头），无 figure/table/equation 穿插，审稿人阅读关键技术内容时缺乏视觉休息点。 |\n| **warning** | Page 7 三个 display items（Table 2 + Figure 2 + Figure 3）堆叠，视觉密度过高。Figure 2/3 被压缩。 |\n| **warning** | Page 8 又一个纯文本页（Error Analysis + Discussion），p4-p8 中 4/5 页纯文本。 |\n| **info** | Figure 3 尺寸过小，坐标轴标签 6-7pt 接近可读性下限。 |\n| **info** | Table 1, Table 2 均使用 booktabs 风格，格式规范。 |\n| **info** | 未发现 margin overflow、LaTeX 渲染错误、未解析引用 [?]。参考文献格式统一。 |\n\n建议：将 Table 2 或 Figure 2 前移至 p5-6 以改善视觉节奏，同时压缩 §7 将 Conclusion 收回第 8 页。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n**置信度: 4 / 5**\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**核心判断**：这是一篇方法论严谨的实证研究，C1（歧义因果效应 +34.0pp）在 7 模型和 2 个 benchmark 上的证据非常稳健，matched-pair 设计是真正的方法论贡献。Variance decomposition + NMI repositioning（clause wording drives risk, type drives mechanism）是论文最有价值的原创洞察。\n\n但论文在以下维度不够突出：\n\n1. **C2 mid-tier ordering 不稳健**（cross-judge ρ=0.09 + SESOI margin-dependency），作为 primary claim 证据不足\n2. **Judge-model identity 完全混淆**，C4 的核心发现可能是 artifact\n3. **核心发现（ambiguity → violation）高度直觉**，taxonomic contribution 增量有限\n4. **概念创新有限**——\"Disambiguation Neglect\" 是 ambiguity collapse 的场景迁移，自创术语过多\n\n**如果按建议调整**（C2 降级、taxonomy 降格、术语精简、页面修复），论文的因果方法论 + variance decomposition insight 足以支撑 Conference（4.0）。当前版本处于 Borderline Conference（3.5）。\n\n**格式风险**: 主文超出 8 页限制约 4 行，EMNLP 2026 严格执行，有 desk reject 可能——这是最紧急的修复项。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 开篇的 $200 motivating example 有效且具象\n- 贡献列表中 taxonomy 不应与因果设计和 variance decomposition 并列——后两者的贡献度更高\n- \"first matched-pair causal study\" claim 本身准确，但应明确 2/6 types 采用了 operational definition of ambiguity\n\n### §3 Taxonomy\n- \"Scope of 'ambiguity'\" 段的 principled justification（behaviorally indistinguishable）应更突出\n- 两层结构在 C3 inconclusive 后仅作为\"organizational convenience\"——这个定位是诚实的但可以更早明确\n\n### §4 Method\n- Matched-pair design + perturbation control 是方法论亮点\n- Cross-judge design 的 confound 应在 §4.4 而非仅在 Limitations 中讨论\n- SESOI ±15pp 的论证需要 domain-grounded 锚定而非仅用 perturbation bound >2×\n\n### §5 Results\n- C1 证据链完整且稳健\n- C2 §5.2 最后一段的 limiting statement 与 C2 作为 primary claim 的 framing 矛盾——需要在 Abstract/Intro 中对齐\n- C3 报 inconclusive 是正确的做法\n- C4 需要在 section 内部（不仅在 Limitations）声明 judge-model confound\n\n### §6 Error Analysis\n- Failure mode taxonomy 有价值，但 LLM coding circularity 需要 human calibration\n- \"Disambiguation Neglect\" 应减少新概念 framing，定位为 ambiguity collapse 的 agentic-context 实证确认\n- \"Systematic nocuity\" 的 terminology overhead 超过了概念增量\n\n### §7 Discussion\n- 仅 3 段略显简短\n- Practical implications（clause-level auditing 如何具体操作？与 DRIP-R 方案的互补性？）讨论不足\n- 60.8% 残差方差对 auditing 实用性的影响未讨论\n\n### §8 Conclusion\n- 需拉回第 8 页（format violation）\n- \"critical for policy-governed deployments\" 应限定领域范围\n\n### Appendix\n- 18 个附录的敏感性分析和 robustness checks 可审查性高，值得肯定\n- SOPBench replication 的 individual non-significance（2/5 models）应在正文提及\n\n### 格式与写作\n- Abstract 数字过载需精简\n- 17× vs 16.8× 不一致需统一\n- ICC 双数字需解释\n- ferrari_defects_2018 bib entry 年份需修正\n- Mu et al. (2023) orphan bib entry 需处理"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# 审稿报告 — Round 18 (Fresh Review)\n\n**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿，无上轮记忆)\n**Reviewer 编排**: 2 人 — R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量\n**交叉回应**: 完成，所有 critical issues 达成共识\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下因歧义导致安全违规的因果效应。采用匹配对设计在 τ²-bench 上构造 300 对歧义/非歧义 clause pairs，跨 6 种歧义类型和 5 个模型评估 2,997 个 episodes。核心发现：歧义 clause 使违规率增加 34.0pp (conditional OR=15.1)；clause 措辞解释 22.4% 方差远超 type (0.4%) 和 model (1.0%)；type 预测 failure mechanism 比预测 violation rate 强 17×。\n\n---\n\n## Strengths\n\n**S1.** [R1+R2 共识] **匹配对因果设计是方法论亮点**。相比 DRIP-R 的 correlational 设计，本文通过最小编辑配对隔离歧义因果效应，加上扰动控制（Δ_perturb = −0.67pp, CI 含零）确认 specificity to semantic ambiguity。这是 agent policy compliance 领域首个严格的因果推断设计。\n\n**S2.** [R1+R2 共识] **C1 证据极其稳健**。34.0pp 效应在 7 个模型（5+2 replication）、2 个 benchmark（τ²-bench + SOPBench）、多 severity threshold 下方向一致。排除 incompleteness 后 Δ=31.0pp (p<10⁻⁷⁵) 仍然显著，证明效应不依赖任何单一 type。\n\n**S3.** [R1+R2 共识] **Variance decomposition + NMI repositioning 是论文最有价值的原创洞察**。\"Clause wording drives risk (22.4%), type drives mechanism (17× NMI)\" 的发现重新定义了 taxonomy 在 agent safety 中的角色——从 risk predictor 转为 diagnostic tool。这个 framing 有概念新意且有方法论支撑。\n\n**S4.** [R1+R2 共识] **Claims 与 evidence 自觉对齐**。C3 报 inconclusive，C4 标 exploratory，taxonomy 重新定位——论文没有过度声称。18 个附录提供详尽敏感性分析，可审查性高。Limitations 部分对所有已知弱点（cross-judge ρ=0.09, incompleteness confound, ICC OpenAI-only 等）的披露非常坦诚。\n\n**S5.** [R2] **统计分析远超同类实证研究水准**。TOST equivalence testing + bootstrap cluster + permutation tests + Holm-Bonferroni correction + logistic regression confound control + cross-benchmark replication，方法论工具箱完整。\n\n**S6.** [R2] **引用真实性已验证**。所有 2026 年 arXiv preprint 引用均为真实存在的论文。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, R1+R2 共识] **C2 \"partial ordering\" 作为 primary claim 缺乏稳健性——cross-judge 不稳定 + SESOI margin-dependency 双重打击**\n\nC2 被列为两个 primary claims 之一（Abstract, Introduction §1），但存在两条独立的不稳定源：\n\n(a) *Cross-judge instability*（R1-N1, R2-W2 → 交叉后升级为共识 critical）：两个 judge group 的 type ranking Spearman ρ=0.09 (p=0.87, Appendix P)，本质为零。排除 authorization scope 后 ρ=0.90，但 authorization scope 的排除虽有独立方法论理由（κ=0.385 最低, agent composition effect），仍引入 researcher degrees of freedom。C2 的 mid-tier ordering 在不同 judge 组下完全不同。\n\n(b) *SESOI margin-dependency*（R1-N3, R2 交叉回应 AGREE）：±15pp margin 下 6/6 mid-tier pairs 等价，但 ±10pp 下仅 3/6，TOST power 从 0.94 降至 0.57。论文用 \"exceeding perturbation control bound by >2×\" 论证 SESOI——但 perturbation bound 是 noise floor，SESOI 是 domain-relevant threshold，两个概念不可混用。12pp 的 type 差异在 deployment 中已有实际意义，但 ±15pp 会判为\"等价\"。\n\n两条证据链汇聚到同一结论：**C2 作为 primary claim 仅在极端类型上成立（incompleteness 最高、coreferential 最低），mid-tier ordering 不可信。** §5.2 末段已表达了类似限定（\"establishing robust extremes...rather than a complete linear ordering\"），但这与 C2 的 primary claim 地位矛盾。\n\n→ **建议**：将 C2 降级为 secondary/partially-supported；Abstract/Introduction 限定为 robust extremes only；Table 2/Figure 2 对 authorization scope 做视觉标注（如 dagger）；正文以多 margin 结果为主要呈现而非以 ±15pp 为 primary。\n\n---\n\n**N2** [critical, R1+R2 共识] **Judge identity 与 model identity 完全混淆**\n\nGPT-5.4 评判 Claude/GPT-4.1/Qwen3；GPT-4.1 评判 GPT-5.4/DeepSeek。每个 model 只有一个 judge，两个 judge 都是 OpenAI 家族。\n\n- C1 不受此 confound 影响（matched-pair 下 judge bias 在 Δpp 中相消，§4.4 正确指出）\n- C4 完全暴露：Figure 3 中 Claude 最低 30.3% vs DeepSeek 最高 49.7% 的 model main effect 无法与 judge effect 分离。Authorization scope 的 52pp model range（该类型驱动 C4 interaction）可能部分是 judge artifact\n- Same-family leniency/severity 无法排除\n\n这是不可追溯修复的实验设计缺陷（除非追加实验）。\n\n→ **建议**：§5.4 首段和 Figure 3 caption 明确声明 \"model-level absolute violation rates are confounded with judge identity and are not directly comparable across judge groups\"；至少对一个 model 用两个 judge 评判以量化 judge effect。\n\n---\n\n**N3** [critical, R2 首提, R1 AGREE with nuance] **Taxonomy 增量贡献不足，contribution framing 需调整**\n\n六种 type 直接取自 Li et al. (2024) 和 Massey et al. (2014)，无新类型引入。两层结构（linguistic vs. specification）的理论价值被 C3 inconclusive（不过 Holm-Bonferroni，§5.3）削弱。6 种 type 中 2 种（incompleteness, conditional precedence）严格来说不是 linguistic ambiguity——§3 \"Scope of 'ambiguity'\" 承认这一点但辩护不够显著。与 DRIP-R (2026) 的差异化论述（§2 最后一段）过于简略——未论证为什么 safety violations 比 decision quality 是更重要的度量。\n\n→ **建议**：将 contribution 重心从 taxonomy 转移到因果方法论 + variance decomposition insight；taxonomy 降格为实验设计工具而非独立贡献；§3 更显著讨论操作性定义偏离；§2 加强与 DRIP-R 差异化论证。\n\n---\n\n**N4** [critical, R2 首提, R1 AGREE] **\"Disambiguation Neglect\" 概念新颖性不足**\n\nLiu et al. (2023) 已证明 LLMs \"fail to represent ambiguity, collapsing multiple interpretations into a single output\"。Gur-Arieh et al. (2026) 系统化了 \"ambiguity collapse\" 风险分类。本文的 \"Disambiguation Neglect\" 本质是 ambiguity collapse 在 agentic settings 的观测实例，核心区别仅在于不可逆后果（§6.2: \"the result is irreversible policy violation\"）。4.6% awareness rate 是有价值的实证数据点，但 framing 为带专属术语的新概念过度。\"Systematic nocuity\" 和 \"differential nocuity\" 同样是 Berry & Kamsties (2004) / Willis et al. (2008) 概念的直接延伸。\n\n→ **建议**：将 Disambiguation Neglect 定位为 ambiguity collapse 的实证确认而非概念创新；减少自创术语（\"systematic nocuity\" → \"convergent violations\"）；更充分地与 Gur-Arieh et al. (2026) 的 epistemic risk taxonomy 对话。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, R1+R2] **Variance decomposition 在 binary outcomes 上的适用性**：Type III SS 在 binary outcome 上近似 LPM，22.4% 来自 LPM。Tjur's R²=0.175 与 Type III 39.2% explained variance 差异暗示方法不一致。Logistic regression 因子排序一致性（Appendix H）是 mitigation factor，但应在正文说明两者度量不同维度。\n\n**W2** [warning, R1+R2] **60.8% 残差方差未充分讨论**：condition + clause wording 仅解释 ~38% 方差。论文推荐 clause-level auditing（Conclusion）但未讨论 60.8% 随机方差（conversation trajectory, user-simulator stochasticity）对实用性的影响。22.4% 仍是最大可干预因子，但 Discussion 应加入这个 perspective。\n\n**W3** [warning, R1+R2] **Incompleteness confound 需更显著讨论**：49.2pp effect 是 ambiguity resolution + information addition 的混合效应。Token count 作为 information proxy 粗糙（OR=1.022 显著, p<0.001）。Logistic regression 后 p=0.022 接近边界。Abstract \"conditional on an information-addition confound\" 措辞模糊——未报告 controlled effect size。Auth scope 有最大 token delta 但 violation 更低是间接 counter-evidence。正文（非仅 Appendix）应显著讨论。\n\n**W4** [warning, R1+R2] **Failure mode coding LLM circularity**：MI 提供结构性反循环证据，但不能排除 LLM coder 系统映射。κ=0.52 仅 moderate。建议 camera-ready 对 50-100 条 traces 做 human failure mode annotation。\n\n**W5** [warning, R1+R2] **SOPBench 效应量大幅下降**：+13.8pp vs +34.0pp（降 60%），仅 3/5 模型达个体显著性（DeepSeek p=0.119, GPT-5.4 p=0.209）。\"Directional consistency\" framing 可能过于乐观。正文 §5.1 仅一句话提及，应更坦诚讨论。\n\n**W6** [warning, R1+R2] **Coreferential 排除矛盾**：作为唯一 zero-token-delta type，coreferential 是最 clean 的 confound-free evidence (+18.7pp)——但被排除出 mitigation 和 replication。加上 human-LLM κ 最低 (0.479)，三点叠加使其证据最薄弱，与 confound-free 地位矛盾。Limitations 应明确承认此 tension。\n\n**W7** [warning, R2, R1 部分同意] **Abstract 数字过载**：~200 词 abstract 中 15+ 个数字，核心信息被淹没。建议保留 5-7 个关键数字（34.0pp, OR=15.1, 22.4% vs 0.4%, 17×），其余用定性语言。\n\n**W8** [critical/format, R2+R1+visual check] **主文超出 8 页限制约 4 行**：Conclusion (§8) 标题和全文出现在第 9 页顶部。EMNLP 2026 strict 8-page limit，有 desk reject 风险。建议压缩 §7 Discussion 将 Conclusion 拉回第 8 页。\n\n**W9** [warning, R1+R2] **Conclusion 泛化声明超出证据范围**：\"clause-level auditing is critical for policy-governed deployments\" 未限定领域（仅 customer service）。SOPBench 效应量降 60% 进一步限制泛化性。\n\n---\n\n## Reviewer Consensus\n\n以下 issues 两位 Reviewer 在交叉回应中明确达成共识（均 [AGREE]）：\n\n1. **C2 mid-tier ordering 不稳健**：R1 从 SESOI margin-dependency 角度 + R2 从 cross-judge ρ=0.09 角度 → 汇聚同一结论\n2. **Judge-model confound 影响 C4**：R1 首提，R2 完全同意并补充 C1 不受影响的论证\n3. **Incompleteness confound 需更好的 proxy**：R1-W3 ≈ R2-W1，双方一致\n4. **\"Disambiguation Neglect\" 新颖性有限**：R2 首提，R1 完全同意（\"§6.2 自己承认了延伸性质\"）\n5. **SOPBench 效应量下降需更坦诚讨论**：R1-W5 ≈ R2 交叉回应\n6. **主文超页需修复**：R2 首发现，R1 验证 PDF 确认\n\n## Reviewer Divergence\n\n无重大未解决分歧。微小差异：\n\n- R2 将 cross-judge ρ=0.09 列为 Should-Fix (W2)，R1 列为 Must-Fix (N1)。**交叉后 R2 同意升级为 critical**（\"综合来看，应升级为 critical——两个独立的不稳定源叠加使问题更严重\"）。\n- R1 认为 \"first matched-pair causal study\" claim 表述准确，R2 认为需进一步限定（2/6 type 非 strict ambiguity）。分歧已在交叉中收敛——R1 同意 taxonomy framing 应调整但 causal claim 本身准确。\n\n---\n\n## Questions\n\n1. 如果用 Claude 或 Gemini 作为 judge 评判 GPT 模型的 traces，C4 的 model ranking 是否改变？这是检验 judge-model confound 的直接实验。\n2. 在 ±10pp margin 下，C2 的 mid-tier cluster 从 4 types 缩减到 2 pairs——作者如何论证 ±15pp 而非 ±10pp 是\"正确\"的 SESOI？是否有 deployment scenario 可以锚定？\n3. 60.8% 残差方差中，conversation trajectory 和 user-simulator stochasticity 各占多少？是否可以通过固定 user-simulator seed 来分解？\n4. Incompleteness 控制 token delta 后的 controlled effect size 是多少？（Appendix F 仅报告 p=0.022 但未报告 controlled Δpp）\n5. 论文引用了 Mu et al. (2023) \"Can LLMs Follow Simple Rules?\" 在 bib 中但未在正文引用——这篇论文与 policy compliance 直接相关，是有意排除还是遗漏？\n\n---\n\n## Missing References\n\n论文的 related work 覆盖面已相当全面（R2 验证了所有 2026 引用的真实性）。以下供参考：\n\n- **Mu et al. (2023)** \"Can LLMs Follow Simple Rules?\" — 已在 bib 中但未引用，研究 LLM 规则遵循能力，与 policy compliance 直接相关\n- **Structured policy representation / policy formalization** 方向的工作——论文讨论 clause-level auditing 但未讨论 policy formalization 作为替代方案\n- 近期 **constitutional AI / rule-following** 实证研究（2025-2026 如有）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (耗时约 4 分钟)\n\n| 严重度 | 发现 |\n|--------|------|\n| **critical** | 主文本（Section 1-8）超出 8 页限制，Conclusion 完整位于第 9 页顶部，约 8.5 页。存在 desk reject 风险。 |\n| **warning** | Pages 4-6 连续 3 页纯文本（Method + Results 开头），无 figure/table/equation 穿插，审稿人阅读关键技术内容时缺乏视觉休息点。 |\n| **warning** | Page 7 三个 display items（Table 2 + Figure 2 + Figure 3）堆叠，视觉密度过高。Figure 2/3 被压缩。 |\n| **warning** | Page 8 又一个纯文本页（Error Analysis + Discussion），p4-p8 中 4/5 页纯文本。 |\n| **info** | Figure 3 尺寸过小，坐标轴标签 6-7pt 接近可读性下限。 |\n| **info** | Table 1, Table 2 均使用 booktabs 风格，格式规范。 |\n| **info** | 未发现 margin overflow、LaTeX 渲染错误、未解析引用 [?]。参考文献格式统一。 |\n\n建议：将 Table 2 或 Figure 2 前移至 p5-6 以改善视觉节奏，同时压缩 §7 将 Conclusion 收回第 8 页。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n**置信度: 4 / 5**\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**核心判断**：这是一篇方法论严谨的实证研究，C1（歧义因果效应 +34.0pp）在 7 模型和 2 个 benchmark 上的证据非常稳健，matched-pair 设计是真正的方法论贡献。Variance decomposition + NMI repositioning（clause wording drives risk, type drives mechanism）是论文最有价值的原创洞察。\n\n但论文在以下维度不够突出：\n\n1. **C2 mid-tier ordering 不稳健**（cross-judge ρ=0.09 + SESOI margin-dependency），作为 primary claim 证据不足\n2. **Judge-model identity 完全混淆**，C4 的核心发现可能是 artifact\n3. **核心发现（ambiguity → violation）高度直觉**，taxonomic contribution 增量有限\n4. **概念创新有限**——\"Disambiguation Neglect\" 是 ambiguity collapse 的场景迁移，自创术语过多\n\n**如果按建议调整**（C2 降级、taxonomy 降格、术语精简、页面修复），论文的因果方法论 + variance decomposition insight 足以支撑 Conference（4.0）。当前版本处于 Borderline Conference（3.5）。\n\n**格式风险**: 主文超出 8 页限制约 4 行，EMNLP 2026 严格执行，有 desk reject 可能——这是最紧急的修复项。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 开篇的 $200 motivating example 有效且具象\n- 贡献列表中 taxonomy 不应与因果设计和 variance decomposition 并列——后两者的贡献度更高\n- \"first matched-pair causal study\" claim 本身准确，但应明确 2/6 types 采用了 operational definition of ambiguity\n\n### §3 Taxonomy\n- \"Scope of 'ambiguity'\" 段的 principled justification（behaviorally indistinguishable）应更突出\n- 两层结构在 C3 inconclusive 后仅作为\"organizational convenience\"——这个定位是诚实的但可以更早明确\n\n### §4 Method\n- Matched-pair design + perturbation control 是方法论亮点\n- Cross-judge design 的 confound 应在 §4.4 而非仅在 Limitations 中讨论\n- SESOI ±15pp 的论证需要 domain-grounded 锚定而非仅用 perturbation bound >2×\n\n### §5 Results\n- C1 证据链完整且稳健\n- C2 §5.2 最后一段的 limiting statement 与 C2 作为 primary claim 的 framing 矛盾——需要在 Abstract/Intro 中对齐\n- C3 报 inconclusive 是正确的做法\n- C4 需要在 section 内部（不仅在 Limitations）声明 judge-model confound\n\n### §6 Error Analysis\n- Failure mode taxonomy 有价值，但 LLM coding circularity 需要 human calibration\n- \"Disambiguation Neglect\" 应减少新概念 framing，定位为 ambiguity collapse 的 agentic-context 实证确认\n- \"Systematic nocuity\" 的 terminology overhead 超过了概念增量\n\n### §7 Discussion\n- 仅 3 段略显简短\n- Practical implications（clause-level auditing 如何具体操作？与 DRIP-R 方案的互补性？）讨论不足\n- 60.8% 残差方差对 auditing 实用性的影响未讨论\n\n### §8 Conclusion\n- 需拉回第 8 页（format violation）\n- \"critical for policy-governed deployments\" 应限定领域范围\n\n### Appendix\n- 18 个附录的敏感性分析和 robustness checks 可审查性高，值得肯定\n- SOPBench replication 的 individual non-significance（2/5 models）应在正文提及\n\n### 格式与写作\n- Abstract 数字过载需精简\n- 17× vs 16.8× 不一致需统一\n- ICC 双数字需解释\n- ferrari_defects_2018 bib entry 年份需修正\n- Mu et al. (2023) orphan bib entry 需处理"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-22T21:01:23.464772+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4018
}
```

</details>

---


### Assistant

_source line 1572 · 2026-05-22T21:01:45.523389+00:00_

审稿报告已投递。

---

**Round 18 审稿完成。** 合成报告要点：

**评分：3.5 / 5 — Borderline Conference**

**4 个 Must-Fix：**
1. C2 partial ordering 中间层不稳健（cross-judge ρ=0.09 + SESOI ±15pp margin-dependency）→ 降级为 secondary claim
2. Judge-model identity 完全混淆 → C4 需要 confound caveat
3. Taxonomy 增量贡献不足 → 贡献重心应转移到因果方法论
4. "Disambiguation Neglect" 新颖性有限 → 定位为 ambiguity collapse 的实证确认

**9 个 Should-Fix** 含 1 个格式 critical（主文超 8 页约 4 行，desk reject 风险）。

**核心共识：** C1 因果效应 (+34.0pp) 在 7 模型+2 benchmark 上稳健，matched-pair 设计 + variance decomposition insight 是真正贡献。如果 C2 降级、taxonomy 降格、术语精简、页面修复，可望达到 Conference (4.0)。

Issue tracker 已同步更新（R18-N1~N5 + R18-W1~W9 + R18-M1~M9）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 1573 · 2026-05-22T21:01:47.994347+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 Must-Fix (N1, N2) 和 Should-Fix (W1-W5) 的逐条回应。

核心判断：
- **N1 (taxonomy)**: 同意 taxonomy 自身缺乏增量贡献，但"first causal study"表述准确，不需限定
- **N2 (Disambiguation Neglect)**: 同意术语过度包装，应定位为 ambiguity collapse 的实证确认
- **W1 (incompleteness confound)**: 同意，补充指出 Abstract 中 "conditional on" 措辞模糊
- **W2 (cross-judge ρ=0.09)**: 同意并升级为 Must-Fix，与我 R1-N1 一致
- **W3 (abstract 数字)**: 部分同意，建议保留 5 个关键数字
- **W4 (领域限制)**: 同意 Conclusion 泛化 claim 应限定
- **W5 (页面超限)**: 已验证 PDF 确认 §8 Conclusion 溢出至第 9 页约 4 行，需修复

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1574 · 2026-05-22T21:02:05.203634+00:00_

审稿报告已投递至 Research Director。

**Round 18 审稿总结：**

- **评分**：3.5 / 5（Borderline Conference）
- **两位 Reviewer 评分一致**，交叉回应后所有 critical issues 达成共识

**5 个 Must-Fix：**
1. C2 partial ordering 中间层不稳健（cross-judge ρ=0.09 + SESOI margin-dependency 双重打击）
2. Judge-model identity 完全混淆，C4 可能是 artifact
3. Taxonomy 增量贡献不足，contribution framing 需调整
4. "Disambiguation Neglect" 概念新颖性不足，自创术语过多
5. 主文超出 8 页限制（desk reject 风险，最紧急）

**9 个 Should-Fix：** variance decomposition 适用性、60.8% 残差方差讨论不足、incompleteness confound、failure mode LLM circularity、SOPBench 效应量下降、coreferential 排除矛盾、abstract 数字过载、Conclusion 泛化声明、authorization scope 视觉标注

**核心判断**：C1 因果效应（+34.0pp, 7 模型, 2 benchmark）证据稳健，matched-pair 设计 + variance decomposition insight 是真正贡献。如果按建议调整 C2 降级、taxonomy 降格、术语精简、页面修复，可望达到 Conference（4.0）。

Issue tracker 已同步更新（R18-N1~N5, R18-W1~W9, R18-M1~M9）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 155

## Round 155

62 recorded events


### User

_source line 1575 · 2026-05-23T01:33:36.708299+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May cycle)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-23T01:33:42.685115+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-23T01:33:42.736221+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-23T01:33:51.168850+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1579 · 2026-05-23T01:33:51.219447+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1580 · 2026-05-23T01:33:54.783203+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1581 · 2026-05-23T01:33:54.783698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-23T01:33:59.602377+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-23T01:33:59.853921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-23T01:34:03.167151+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1585 · 2026-05-23T01:34:03.217849+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-23T01:34:14.168903+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-23T01:34:14.219716+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-23T01:34:14.270520+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1589 · 2026-05-23T01:34:14.421696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1590 · 2026-05-23T01:34:14.422064+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1591 · 2026-05-23T01:34:14.523502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1592 · 2026-05-23T01:34:14.624418+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 18 (fresh review, fixes applied)
5	
6	# ============================================================
7	# R18 ISSUES — ALL ADDRESSED
8	# ============================================================
9	
10	- id: "R18-N1"
11	  summary: "C2 mid-tier ordering 不稳健，需降级为 secondary claim"
12	  category: framing
13	  severity: critical
14	  status: resolved
15	  first_raised_round: 18
16	  last_seen_round: 18
17	  action_items:
18	    - round: 18
19	      action: "Abstract/Intro C2 降为 secondary, 保留 robust extremes only"
20	      assigned_to: agent
21	      status: done
22	
23	- id: "R18-N2"
24	  summary: "Judge-model identity 完全混淆影响 C4"
25	  category: method
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 18
29	  last_seen_round: 18
30	  resolution: "Cross-family judge validation (GPT-4.1, Claude Sonnet 4.6, Gemini 2.5 Pro) on 2997 episodes: Fleiss' κ=0.717, model rankings preserved (ρ≥0.70), no same-family leniency. N2 upgraded from caveat to validated."
31	  resolution_round: 18
32	  action_items:
33	    - round: 18
34	      action: "Cross-judge validation experiment + §5.4/Fig3/Limitations upgrade with κ=0.717 evidence"
35	      assigned_to: agent
36	      status: done
37	
38	- id: "R18-N3"
39	  summary: "Taxonomy 增量贡献不足, contribution framing 调整"
40	  category: framing
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 18
44	  last_seen_round: 18
45	  action_items:
46	    - round: 18
47	      action: "Taxonomy 降格为 experimental instrument; contributions 重排"
48	      assigned_to: agent
49	      status: done
50	
51	- id: "R18-N4"
52	  summary: "Disambiguation Neglect 新颖性不足"
53	  category: framing
54	  severity: critical
55	  status: resolved
56	  first_raised_round: 18
57	  last_seen_round: 18
58	  action_items:
59	    - round: 18
60	
…[truncated 4165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-23T01:34:20.798078+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found information related to EMNLP and the ACL Rolling Review (ARR) system, though the search results primarily
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6527
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-23T01:34:27.975332+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1595 · 2026-05-23T01:34:28.477645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR cycle May 2026"
  }
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-23T01:34:30.786844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-23T01:34:30.988050+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points (conditional OR $= 15.1$, matched-pair), with perturbation controls confirming specificity to semantic ambiguity. A variance decomposition reveals that individual clause wording explains 22.4\% of violation variance versus 0.4\% for ambiguity type, establishing clause-level wording as the dominant risk factor. However, a normalized mutual information analysis shows that type membership predicts failure \emph{mechanism} 17$\times$ more strongly than it predicts violation rate, establishing the taxonomy as a diagnostic tool for failure-mechanism prediction rather than risk prediction. Per-type effects range from $+$18.7 to $+$49.2\,pp, with incompleteness as the consistent upper bound. Error analysis reveals disambiguation neglect ($\leq$11\% per-model awareness) and \emph{systematic nocuity}: 41.3\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-23T01:34:31.088934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-23T01:34:31.089419+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1600 · 2026-05-23T01:34:33.770647+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR cycle May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here are the key details about EMNLP 2026 and the ARR May 2026 cycle:

## EMNLP 2026 Commitment Deadline

The EMNLP commitment deadline is August 2, 2026.

## ARR 2026 May Cycle Important Dates

The ARR submission deadline for long and short papers is May 25, 2026, the reviewer registration deadline for all authors is May 27, 2026.

## Special Policy for May 2026 Cycle

There's an important new policy specific to the ARR 2026
…[truncated 657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5293
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-23T01:34:33.871577+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the key ACL Rolling Review (ARR) 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited 
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5896
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-23T01:34:39.493663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-23T01:34:40.447747+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 3480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-23T01:34:40.448112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-23T01:34:40.900339+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and tw
…[truncated 5404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-23T01:34:40.900717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1607 · 2026-05-23T01:34:41.252426+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type partial ordering (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS on binary outcomes approximates a linear probability model; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), though magnitudes differ between linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\,pp is run-to-run stochasticity and $\sim$46\,pp systematic-but-unmeasured factors; ICC replication in Appendix~\ref{app:residual}). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{
…[truncated 8441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-23T01:34:41.252907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-23T01:34:41.303490+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with two achieving unanimity (scopal and authorization scope).
19	
20	\subsection{Disambiguation Neglect}
21	\label{sec:dn}
22	
23	Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} versus \emph{surface adoption} (proceeding with a single interpretation). Overall awareness is 4.6\% ($\leq$11\% per model); Qwen
…[truncated 1136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-23T01:34:48.079889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-23T01:34:48.432290+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on type, safety training, and disambiguation channel availability. The binary effect is domain-robust (interaction $p = 0.187$) but type rankings are not ($\rho = 0.26$), suggesting nocuity is universal while its type-specific profile requires per-domain calibration. Nevertheless, 60.8\% of variance remains unexplained (conversation trajectory, user-simulator stochasticity); clause-level auditing targets the largest controllable factor (22.4\%).
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} 17$\times$ more strongly than violation rate (NMI ratio $\approx 17$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
9	
10	\paragraph{Prompt-based mitigation.}
11	A mitigation study (Appendix~\ref{app:mitigation}) finds prompting effective for authorization scope ($-18.0$\,pp) and lexical ($-8.9$\,pp) but not incompleteness ($-3.3$\,pp), reinforcing policy-design over prompt-level fixes \citep{chantree_2006,ferrari_ambiguity_2019}.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-23T01:34:48.432647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-23T01:34:48.583480+00:00_

1	\section{Conclusion}
2	
3	Policy ambiguity increases agent violations by 34.0\,pp (OR\,$=$\,15.1); clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms 17$\times$ better than violation rate. With $>$89\% disambiguation neglect and 41.3\% convergent violations, clause-level auditing is critical for customer-service and similar policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-23T01:34:48.935255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-23T01:34:49.387505+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested. Cross-domain consistency holds for the overall effect (C1, interaction $p = 0.19$) and model ranking ($\rho = 0.90$, $p = 0.037$), but type rankings vary across domains ($\rho = 0.26$, $p = 0.62$); conditional precedence in particular differs by 22\,pp between retail and airline, further motivating the partial-ordering framing. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}); consequently, the confound-free lower bound ($+$18.7\,pp) rests on the primary five-model study alone.
5	
6	\paragraph{Measurement.} A cross-family judge validation (Appendix~\ref{app:cross_judge}) using GPT-4.1, Claude Sonnet~4.6, and Gemini~2.5~Pro on the same 2,997 episodes achieves Fleiss' $\kappa = 0.717$ (substantial agreement), confirming that C1 and C2 extremes are judge-independent. Model rankings are preserved across all three judge families ($\rho \geq 0.70$), and no same-family leniency is observed (Claude judge rates Claude Sonnet \emph{higher} than GPT judge does). The residual limitation is authorization scope: its within-judge model range is judge-dependent (52\,pp under GPT judge vs.\ 24--30\,pp under Claude/Gemini judges), so absolute C4 magnitudes for this type remain uncertain. Per-type reliability varies---authorization scope has the lowest agreement ($
…[truncated 1671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-23T01:34:49.387905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-23T01:34:49.690880+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 37141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-23T01:34:58.223527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-23T01:34:58.223931+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on frequency in operational policy documents and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by contextual cues within the text.
29	\emph{Scopal} ambiguity involves quantifier, negation, or modal scope interac
…[truncated 2685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-23T01:34:58.675843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-23T01:34:58.726506+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-23T01:35:12.528354+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "experiment_plan.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "experiment_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-23T01:35:12.578924+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-23T01:35:16.644875+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/policy_ambiguity_safety/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/policy_ambiguity_safety/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-23T01:35:16.796778+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/_project/intermediate/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/deprecated/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/v1/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/deprecated/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/v1/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pandas/_config/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pandas/core/
…[truncated 8294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-23T01:35:24.125811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/config.py",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/config.py",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-23T01:35:24.176417+00:00_

1	"""Shared configuration for policy_ambiguity_safety experiment.
2	
3	API models use OpenRouter-compatible endpoint via openai SDK.
4	Claude models may use a separate API key on the same endpoint.
5	"""
6	
7	import os
8	from pathlib import Path
9	
10	# ── Paths ──
11	ARTIFACTS_DIR = Path(__file__).parent
12	DEFAULT_OUTPUT_DIR = ARTIFACTS_DIR / "results"
13	DEFAULT_JUDGMENTS_DIR = ARTIFACTS_DIR / "judgments"
14	DEFAULT_ANALYSIS_DIR = ARTIFACTS_DIR / "analysis"
15	
16	# ── API Endpoints ──
17	OPENROUTER_BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
18	API_KEY_ENV = "OPENROUTER_API_KEY"
19	
20	# ── Models ──
21	# All models via OpenRouter proxy. Non-OpenAI models require provider/ prefix.
22	# Verified 2026-05-20 via openrouter_model_test.json.
23	MODELS = {
24	    "gpt-5.4": {
25	        "model_id": "gpt-5.4",
26	        "max_tokens": 4096,
27	        "api_key_env": API_KEY_ENV,
28	        "base_url": OPENROUTER_BASE_URL,
29	    },
30	    "gpt-4.1": {
31	        "model_id": "gpt-4.1",
32	        "max_tokens": 4096,
33	        "api_key_env": API_KEY_ENV,
34	        "base_url": OPENROUTER_BASE_URL,
35	    },
36	    "claude-sonnet-4-6": {
37	        "model_id": "anthropic/claude-sonnet-4-6",
38	        "max_tokens": 4096,
39	        "api_key_env": API_KEY_ENV,
40	        "base_url": OPENROUTER_BASE_URL,
41	    },
42	    "qwen3-235b": {
43	        "model_id": "qwen/qwen3-235b-a22b",
44	        "max_tokens": 4096,
45	        "api_key_env": API_KEY_ENV,
46	        "base_url": OPENROUTER_BASE_URL,
47	    },
48	    "deepseek-v3": {
49	        "model_id": "deepseek/deepseek-chat-v3-0324",
50	        "max_tokens": 4096,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-23T01:35:43.966623+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool call

_source line 1629 · 2026-05-23T01:35:44.970344+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1630 · 2026-05-23T01:36:10.884980+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26918
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-23T01:36:10.885427+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 25915
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-23T01:36:10.937460+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页, 参考文献无限, Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- 各章节在 `sections/` 子目录下\n\n## 你的审查侧重\n\n重点关注以下维度，逐条给出评价和证据：\n\n### 1. 实验设计\n- Matched-pair design 是否足以建立因果推断？300 clause pairs × 5 models × 2 conditions 的样本量是否充分？\n- 合成 ambiguity clause 的生态效度（ecological validity）——是否代表真实世界的政策歧义？\n- 评审员标注流程（96% initial agreement, 13 disagreements resolved by discussion）是否充分？\n\n### 2. 统计分析\n- McNemar's test、TOST equivalence testing、variance decomposition 的使用是否恰当？\n- ±15pp SESOI 的选择是否有充分理由？sensitivity analysis 是否做得够？\n- Holm-Bonferroni 校正是否覆盖所有需要校正的检验？\n- 60.8% 残差方差是否得到充分讨论？\n- 22.4% clause-level variance 的 permutation test 是否有效地排除了 chance？\n\n### 3. Controls\n- Perturbation control (300 episodes, Δ=-0.67pp) 是否足以排除非歧义因素？\n- Incompleteness confound（information addition）的处理是否充分？token count 作为 proxy 够不够？\n- Cross-judge design 是否有效地控制了 self-evaluation bias？\n\n### 4. Evaluation Pipeline\n- Cross-judge calibration (κ=0.653 binary, κ_w=0.775 severity) 是否达标？\n- Human validation (κ=0.798 inter-annotator, κ=0.733 human-LLM) 是否充分？\n- 100-episode calibration sample 的代表性如何？65% ambiguous stratification 是否引入偏差？\n- Cross-family judge validation (Fleiss' κ=0.717) 的设计和解释是否合理？\n\n### 5. Replication & Generalizability\n- 2 additional models (Gemini, LLaMA) 的 replication 是否充分？\n- SOPBench cross-benchmark replication 的效应量差异（+12.6pp vs +34.0pp）是否合理解释？\n- 仅限 customer service domains 的局限性是否被充分讨论？\n\n### 6. 可复现性\n- API 调用参数（temperature=0, top_p=1）和日期（May 20, 2026）是否足够？\n- ICC=0.919 的 replication 设计是否充分？\n- 数据和代码的可用性声明是否符合要求？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页, 参考文献无限, Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- 各章节在 `sections/` 子目录下\n\n## 你的审查侧重\n\n重点关注以下维度，逐条给出评价和证据：\n\n### 1. 实验设计\n- Matched-pair design 是否足以建立因果推断？300 clause pairs × 5 models × 2 conditions 的样本量是否充分？\n- 合成 ambiguity clause 的生态效度（ecological validity）——是否代表真实世界的政策歧义？\n- 评审员标注流程（96% initial agreement, 13 disagreements resolved by discussion）是否充分？\n\n### 2. 统计分析\n- McNemar's test、TOST equivalence testing、variance decomposition 的使用是否恰当？\n- ±15pp SESOI 的选择是否有充分理由？sensitivity analysis 是否做得够？\n- Holm-Bonferroni 校正是否覆盖所有需要校正的检验？\n- 60.8% 残差方差是否得到充分讨论？\n- 22.4% clause-level variance 的 permutation test 是否有效地排除了 chance？\n\n### 3. Controls\n- Perturbation control (300 episodes, Δ=-0.67pp) 是否足以排除非歧义因素？\n- Incompleteness confound（information addition）的处理是否充分？token count 作为 proxy 够不够？\n- Cross-judge design 是否有效地控制了 self-evaluation bias？\n\n### 4. Evaluation Pipeline\n- Cross-judge calibration (κ=0.653 binary, κ_w=0.775 severity) 是否达标？\n- Human validation (κ=0.798 inter-annotator, κ=0.733 human-LLM) 是否充分？\n- 100-episode calibration sample 的代表性如何？65% ambiguous stratification 是否引入偏差？\n- Cross-family judge validation (Fleiss' κ=0.717) 的设计和解释是否合理？\n\n### 5. Replication & Generalizability\n- 2 additional models (Gemini, LLaMA) 的 replication 是否充分？\n- SOPBench cross-benchmark replication 的效应量差异（+12.6pp vs +34.0pp）是否合理解释？\n- 仅限 customer service domains 的局限性是否被充分讨论？\n\n### 6. 可复现性\n- API 调用参数（temperature=0, top_p=1）和日期（May 20, 2026）是否足够？\n- ICC=0.919 的 replication 设计是否充分？\n- 数据和代码的可用性声明是否符合要求？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-23T01:36:34.103004+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23165
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-23T01:36:34.203875+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页, 参考文献无限, Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- 各章节在 `sections/` 子目录下\n\n## 你的审查侧重\n\n重点关注以下维度，逐条给出评价和证据：\n\n### 1. Contribution 新颖性\n- \"First matched-pair causal study of policy ambiguity's safety impact\" 这一声明是否成立？是否有被遗漏的先行工作？\n- 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等 concurrent work 的区分是否清晰、公正？\n- Variance decomposition (22.4% clause vs 0.4% type) 和 NMI analysis (17× mechanism prediction) 作为 contribution 是否足够新颖？\n- Disambiguation neglect (≤11% awareness) 和 systematic nocuity (41.3% convergent violations) 作为发现是否 incremental？\n\n### 2. Related Work 覆盖\n- Requirements engineering 文献覆盖是否充分？是否遗漏了重要工作？\n- Agent safety evaluation 领域是否有遗漏？特别是 2025-2026 的最新工作？\n- Psycholinguistics 引用是否恰当？ambiguity collapse 相关工作是否覆盖到位？\n- 搜索是否有遗漏的 closely related work（尤其是 policy specification for LLM agents 方向）？\n\n### 3. 写作质量\n- Abstract 是否准确反映论文内容？数字密度是否合适？\n- Introduction 的 narrative arc 是否清晰（问题→gap→方法→发现→贡献）？\n- 各章节的逻辑衔接是否顺畅？\n- 术语一致性（如 nocuous/innocuous、disambiguation neglect、systematic nocuity）\n- Claim hierarchy (C1-C4) 的组织是否清晰？primary vs exploratory 的区分是否恰当？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？（检查 Limitations 是否在正文 8 页之后开始）\n- Limitations section 是否存在、内容是否充分（覆盖 3 个点左右）？\n- 参考文献格式是否符合 ACL/natbib 规范？\n- 匿名性：是否有泄露作者身份的线索（self-citation、acknowledgements、institutional references）？\n- Figure/Table 格式和引用是否规范？\n\n### 5. Taxonomy 定位\n- 将 taxonomy 定位为 \"experimental instrument rather than a proposed classification standard\" 是否有说服力？\n- 将 incompleteness 和 conditional precedence 归入 \"ambiguity\" 的理论依据是否充分？（论文自己承认这两类 \"strictly\" 不算 linguistic ambiguity）\n- 6 type 的选择标准是否透明？为什么是这 6 个而不是更多或更少？\n\n### 6. Discussion & Conclusion\n- \"Differential nocuity\" 假说是否有足够的实验证据支持？\n- Conclusion 中的泛化声明是否被 domain limitation 所限制？\n- 未来工作方向是否有提及？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页, 参考文献无限, Limitations 必须有但不计入页数\n- **模板**: ACL (acl.sty)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- 各章节在 `sections/` 子目录下\n\n## 你的审查侧重\n\n重点关注以下维度，逐条给出评价和证据：\n\n### 1. Contribution 新颖性\n- \"First matched-pair causal study of policy ambiguity's safety impact\" 这一声明是否成立？是否有被遗漏的先行工作？\n- 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等 concurrent work 的区分是否清晰、公正？\n- Variance decomposition (22.4% clause vs 0.4% type) 和 NMI analysis (17× mechanism prediction) 作为 contribution 是否足够新颖？\n- Disambiguation neglect (≤11% awareness) 和 systematic nocuity (41.3% convergent violations) 作为发现是否 incremental？\n\n### 2. Related Work 覆盖\n- Requirements engineering 文献覆盖是否充分？是否遗漏了重要工作？\n- Agent safety evaluation 领域是否有遗漏？特别是 2025-2026 的最新工作？\n- Psycholinguistics 引用是否恰当？ambiguity collapse 相关工作是否覆盖到位？\n- 搜索是否有遗漏的 closely related work（尤其是 policy specification for LLM agents 方向）？\n\n### 3. 写作质量\n- Abstract 是否准确反映论文内容？数字密度是否合适？\n- Introduction 的 narrative arc 是否清晰（问题→gap→方法→发现→贡献）？\n- 各章节的逻辑衔接是否顺畅？\n- 术语一致性（如 nocuous/innocuous、disambiguation neglect、systematic nocuity）\n- Claim hierarchy (C1-C4) 的组织是否清晰？primary vs exploratory 的区分是否恰当？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？（检查 Limitations 是否在正文 8 页之后开始）\n- Limitations section 是否存在、内容是否充分（覆盖 3 个点左右）？\n- 参考文献格式是否符合 ACL/natbib 规范？\n- 匿名性：是否有泄露作者身份的线索（self-citation、acknowledgements、institutional references）？\n- Figure/Table 格式和引用是否规范？\n\n### 5. Taxonomy 定位\n- 将 taxonomy 定位为 \"experimental instrument rather than a proposed classification standard\" 是否有说服力？\n- 将 incompleteness 和 conditional precedence 归入 \"ambiguity\" 的理论依据是否充分？（论文自己承认这两类 \"strictly\" 不算 linguistic ambiguity）\n- 6 type 的选择标准是否透明？为什么是这 6 个而不是更多或更少？\n\n### 6. Discussion & Conclusion\n- \"Differential nocuity\" 假说是否有足够的实验证据支持？\n- Conclusion 中的泛化声明是否被 domain limitation 所限制？\n- 未来工作方向是否有提及？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-23T01:36:35.721339+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1517
}
```

</details>

---


### Assistant

_source line 1636 · 2026-05-23T01:36:46.164850+00:00_

已完成 Step 0-1 的所有并行任务：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性/完整性） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿 | ⏭️ 未启用（项目配置未开启 paperreview.ai） |

等待两位 Reviewer 的独立初审报告返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 156

## Round 156

2 recorded events


### User

_source line 1637 · 2026-05-23T01:43:05.006065+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**投稿**: EMNLP 2026 via ARR May cycle
**审查维度**: 实验设计、统计分析、Controls、Evaluation Pipeline、Replication、可复现性

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计严谨、统计分析全面且诚实，但合成歧义子句的生态效度不足和部分关键度量（authorization scope κ=0.385）的可靠性问题限制了主要发现的泛化性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 匹配对设计合理，统计方法选择恰当，confound 分析全面；主要扣分在 ecological validity 和 auth scope 度量可靠性 |
| Excitement | 3/5 | 研究问题重要（policy ambiguity → agent safety），"type 预测 mechanism 而非 risk" 的洞察有价值，但 ambiguity causes violations 本身不意外，领域限于 customer service |
| Reproducibility | 4/5 | API 参数完整（temperature=0, top_p=1, date），ICC=0.919，承诺释放数据/代码；模型版本漂移是固有限制 |
| Reviewer Confidence | 4/5 | 熟悉实验设计、因果推断、equivalence testing 和 NLP evaluation 方法论 |

---

## Summary

本文研究 LLM agent 在含歧义自然语言政策下的安全行为。在 τ²-bench 上构建 300 matched clause pairs（6 种歧义类型），跨 5 个模型生成 ~3,000 episodes。主要发现：(1) 歧义子句使违规率增加 34.0pp（OR=15.1）；(2) 子句措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型预测失败机制的能力是预测违规率的 17 倍；(3) incompleteness 是持续最高风险类型（46-62%），coreferential 为下界（31.6%）；(4) disambiguation neglect 普遍存在（≤11% awareness）。论文配备了 perturbation control、cross-judge validation、replication models 和 cross-benchmark 验证。

---

## 主要优势 (Strengths)

**S1. 严格的匹配对因果设计 (§4.2)**
匹配对设计是此类研究的 gold standard。在同一 model-judge pairing 内比较每个 clause 的歧义/非歧义变体，有效控制了 judge bias、model baseline 等混淆变量。perturbation control（300 episodes, Δ=-0.67pp）进一步隔离了语义歧义的效应。

**S2. 全面且恰当的统计工具箱 (§4.6, Appendix A-K)**
统计方法选择出色：McNemar's test（匹配对二元结果）、TOST equivalence testing（类型等价性）、Type III SS 方差分解、permutation test（clause-level variance）、bootstrap 聚类分析、logistic regression（confound 控制）、ICC（可复现性）、Holm-Bonferroni 校正、互信息分析。七个 margin 的 sensitivity analysis（Table 3）是特别负责任的做法。

**S3. 多层验证架构**
- Cross-judge: 3 个 judge 家族（GPT, Claude, Gemini），Fleiss' κ=0.717
- Human validation: κ=0.798 inter-annotator, κ=0.733 human-LLM
- Model replication: 7 个模型（+Gemini, LLaMA）跨 6 个 provider
- Cross-benchmark: SOPBench 方向一致性
- Perturbation control: 排除表面文本变化的影响
这种多层验证在 NLP 实证研究中不常见，体现了很高的方法论标准。

**S4. 诚实且精准的 claim calibration**
论文对 claims 的标定非常诚实：C3 (layer effect) 被标记为 inconclusive（不过 Holm-Bonferroni 校正）；authorization scope 的 cross-judge discordance（ρ=0.09）被完整报告；incompleteness 被明确标注为 confounded upper bound；60.8% 残差方差被详细讨论。这种自我约束在投稿论文中难得一见。

**S5. "Type predicts mechanism, not risk" 的核心洞察 (§7)**
这是论文最有价值的贡献。NMI 分析表明 type → mechanism 的预测力是 type → violation rate 的 17 倍（NMI ratio ≈ 17; Appendix S），将 taxonomy 从 risk prediction tool 重新定位为 diagnostic tool。这个 reframing 既诚实（承认 type 对 risk 的解释力很弱）又有实际价值。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 合成歧义子句的生态效度（Ecological Validity）不足
- 具体位置：§4.2, Appendix R (Table 12), Limitations
- 问题：300 clause pairs 通过 "template-based pipeline" 生成。Appendix R 的示例显示部分歧义变体更接近"严重措辞不当"而非真实世界的细微歧义。例如 incompleteness 类型的歧义变体 "Refunds for large orders require appropriate approval and must be processed in a timely manner" 将多个具体参数全部替换为模糊词（"large", "appropriate", "timely"），这种程度的模糊性在实际政策文档中罕见——真实政策更可能在单一参数上存在歧义。Matched-pair 设计建立的因果关系仅在*这组合成子句*的范围内成立。
- 论文提到 "post-hoc realism validation confirms linguistic consistency with original τ²-bench policy text"（§4.2），但：(1) 仅验证了*词汇风格*一致性，未验证歧义的*分布*和*程度*是否匹配真实政策；(2) 未使用外部真实政策文档进行对照；(3) τ²-bench 本身的政策也是合成的。
- 为什么影响接收：这是全文所有 claim 的外部效度基础。如果合成歧义的程度系统性偏高，34.0pp 的效应量可能高估真实场景中的影响。该问题直接影响 Discussion 和 Conclusion 中关于 "policy-governed deployments" 的实践建议的可信度。
- 建议修改方向：(1) 量化合成歧义与真实政策歧义的差异（e.g., 从真实客服政策中采样歧义实例，与合成子句比较歧义程度/类型分布）；(2) 如果无法获取真实数据，至少在 Limitations 中更明确地承认效应量可能被高估，并讨论 effect size 的 transportability；(3) 考虑增加一个 "mild ambiguity" 条件来测试歧义程度的 dose-response 关系。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Authorization scope 度量可靠性不足，但相关 claim 未充分降级
- 具体位置：§4.4 (κ=0.385), §5.4 (C4), Appendix P (judge group ranking ρ=0.09), Appendix W
- 问题：Authorization scope 的 cross-judge binary κ=0.385 低于 "fair" 门槛（0.40），是六种类型中最低的。Per-type human-LLM agreement 也最低（κ=0.644, Table 9）。cross-judge-group ranking discordance（ρ=0.09, p=0.87; Appendix P）完全由 auth scope 的 rank reversal 驱动（GPT-4.1 judged group rank 1 vs GPT-5.4 judged group rank 6）。然而 §5.4 仍然将 auth scope 描述为 "most model-differentiating type"（52pp range）并用于支撑 C4。
- 论文确实在多处提供了 caveats，但这些 caveats 分散在正文（§5.4 末尾）和多个 Appendix（P, W）中。读者容易从 Figure 3 和正文前半部分获得"auth scope 是最有区分度的类型"这一印象，而忽略后续的 qualification。
- 建议：(1) 在 §5.4 正文中更早、更显著地标注 auth scope 的度量不可靠性（不仅仅是结尾的一句 "though its low judge agreement..."）；(2) 考虑在 Figure 3 caption 中直接标注 auth scope 行的 κ 值；(3) 将 "most model-differentiating" 的表述改为条件性的（e.g., "if confirmed by more reliable measurement"）。

**W2** [warning] Incompleteness 的 information-addition confound 虽有控制但 token count proxy 不足
- 具体位置：§5.1, Appendix F, Appendix O (Table 11)
- 问题：Incompleteness 的非歧义变体必然增加政策内容。论文使用 token count 作为信息量的 proxy 进行 logistic regression 控制（Appendix H），发现 token count 系数为正（β=+0.027, p=0.003），即更长的子句预测*更多*违规——看似与 information-addition 假设矛盾。但这个论证有问题：token count 无法区分*信息类型*。Auth scope 的 token delta（+36.1）> incompleteness（+34.6），但两者添加的信息性质完全不同——auth scope 增加的是权限边界细化，incompleteness 增加的是缺失的操作参数。信息类型可能比信息数量更相关。
- Coreferential 作为 confound-free lower bound（18.7pp，information delta=0）是一个巧妙的设计，但它只提供*下界*，不能确定 incompleteness 的 49.2pp 中有多少归因于歧义 vs 信息缺失。
- 建议：(1) 讨论 token count 作为 proxy 的局限性时增加对*信息类型*差异的讨论；(2) 将 "incompleteness is consistently the highest-risk type" 的表述进一步明确为 upper bound；(3) 未来工作中考虑使用语义复杂度/信息论度量替代 token count。

**W3** [warning] SOPBench cross-benchmark replication 的效应量大幅衰减需更审慎讨论
- 具体位置：Appendix V (Table 16)
- 问题：SOPBench replication 效应量（+12.6pp unweighted mean）仅为 τ²-bench 效应（+34.0pp）的 37%。5 个模型中仅 3 个达到 p<0.01，GPT-5.4 borderline（p=0.052），DeepSeek 不显著（p=0.163）。论文将此归因于三个差异：(1) constraint-level vs episode-level measurement, (2) higher baseline, (3) task structure。这些解释合理但未被验证——没有分析证明哪个因素导致了效应衰减。
- "directional consistency across all five models" 的 framing 过于宽泛。Directional consistency 是一个非常弱的标准——即使真实效应为零，在 5 个模型中偶然出现 5/5 正方向的概率为 1/32 ≈ 3%。
- 建议：(1) 报告 SOPBench 的 pooled effect size 和 CI，而非仅报告 unweighted mean；(2) 讨论效应量衰减的量化分析或至少明确承认 generalizability 证据是弱的而非 "confirms"；(3) 将 "confirms directional consistency" 改为更审慎的表述如 "suggests directional consistency, though the substantially smaller effect size warrants caution"。

**W4** [warning] 60.8% 残差方差的实践含义讨论不足
- 具体位置：§5.1, §7 (Discussion), Appendix X
- 问题：方差分解显示 clause identity 22.4%、condition 15.8%、model 1.0%、residual 60.8%。ICC 分析（Appendix X）将残差分解为 ~15pp 随机 + ~46pp systematic-but-unmeasured。后者占总方差的 ~46%，是最大的单一成分，但论文对此的讨论限于 "conversation trajectory, user-simulator stochasticity"。
- 这意味着：即使完全控制了 clause wording、ambiguity type 和 model，仍有 ~46% 的方差来自未测量的系统性因素（对话轨迹、用户模拟器行为等）。这对论文的实践建议（"clause-level auditing"）构成限制——审计 clause 最多解释 22.4% 的方差。
- 建议：在 Discussion 中增加对残差方差实践含义的讨论：(1) 22.4% clause variance 是*可操作的*最大因素，但不是最大因素；(2) 对话轨迹的影响可能意味着相同的歧义子句在不同交互场景下产生不同结果，这对部署建议的含义是什么？

**W5** [warning] Type III SS 在二元结果上的方差分解作为 headline claim 需更多说明
- 具体位置：§5.1 (footnote), Appendix H
- 问题：22.4% clause variance 这个核心数字来自 Type III sum-of-squares 在二元 outcome 上的分解，实质上是线性概率模型的近似。论文在脚注中承认了这一点并引用 logistic regression（Tjur's R²=0.175）作为对照。但 22.4% vs 0.4% 的对比是 abstract 和 introduction 中反复出现的核心 claim，而线性概率模型在极端概率（如 unambiguous 条件下 6.9% violation rate）时的近似质量较差。
- Logistic regression 的 Tjur's R²=0.175 是一个更保守但可能更准确的整体 fit 度量，但它不提供与 Type III SS 直接可比的方差分配。这种方法论选择对核心 claim 的具体数值有影响。
- 建议：(1) 在正文中（而非仅在脚注中）讨论线性近似 vs logistic regression 的差异；(2) 报告 logistic regression 中各预测变量的 partial R² 或 deviance explained，与 Type III SS 的 22.4% 进行对比；(3) 如果两种方法的定性结论一致（clause > type），在正文中明确这一点以增强 claim 的鲁棒性。

---

## Questions for Authors

**Q1.** 生成 clause pairs 的 "template-based pipeline" 具体如何操作？每种类型有多少个 template？是否存在某些 template 贡献了不成比例的违规率？这关系到 22.4% clause variance 是否部分由 template 结构驱动。

**Q2.** 96% initial annotator agreement (287/300) 对应的 chance-corrected κ 是多少？在 6 类分类中，96% raw agreement 的 Cohen's κ 取决于类别基率分布。

**Q3.** Perturbation control 仅包括 synonym substitution 和 clause reordering。是否考虑过包含*结构性*扰动（e.g., 增加不相关的政策内容但不引入歧义）？这将更好地隔离 information-addition 效应。

**Q4.** ICC=0.919 的 replication 仅在 OpenAI family 内进行（30 clause pairs × 2 models × 3 replicates）。cross-provider stability 由 C1 consistency 间接支持，但是否有 cross-provider ICC 数据？

**Q5.** 65% ambiguous stratification in calibration sample（§4.4 footnote）——这个比例高于全数据集的 ~50%。是否检验过在 balanced stratification 下 κ 估计是否发生变化？

---

## 小问题（不影响接收）

- §5.1: "conditional OR = 15.1" 在 abstract 中出现但仅在 §4.6 简要解释了来源（McNemar's discordant pairs）。建议在首次使用时明确注明是 matched-pair OR 还是 marginal OR，因为两者可差异很大。
- §4.3: 模型列表中 "Qwen3-235B" 是 Mixture-of-Experts 架构，但参数量 235B 是否指总参数还是激活参数？这影响与其他模型的可比性。
- Appendix D (detection experiment): 这个实验与主论文的因果分析关系较弱，更像是一个 application spin-off。考虑是否需要在正文中引用。
- Table 2 caption: "All per-type p < 10^{-5} (Fisher's exact)" 但 coreferential 的 p 在正文中报告为 p < 10^{-6}——是否一致？
- §6.1: failure mode coding 的 Gwet's AC₁=0.62, Cohen's κ=0.52。这两个指标的差异通常由 prevalence 不均衡导致。论文应说明选择报告两者的原因。
- Data availability: "https://github.com/anonymous/policy-ambiguity-safety" 是 anonymous placeholder。确认最终版本会替换为真实 URL。

---

## 总体评价

这是一篇方法论标准很高的实证研究。匹配对设计、多层验证、sensitivity analysis 和诚实的 claim calibration 都体现了严谨的科学态度。核心发现（ambiguity causes violations, clause > type for risk, type > clause for mechanism）在其实验范围内是可信的。

主要顾虑集中在外部效度：合成歧义子句的代表性、authorization scope 度量的可靠性、以及 SOPBench replication 效应量的大幅衰减。这些问题不会推翻核心发现，但限制了从 "controlled experiment on synthetic clauses in τ²-bench" 到 "implications for policy-governed deployments" 的推断跨度。

如果能加强 ecological validity 论证（e.g., 真实政策歧义对照或 dose-response 分析）并更审慎地框定 generalizability claims，本文有潜力成为 Conference-level 的贡献。当前版本在 Borderline Conference (3.5) 的高端。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1638 · 2026-05-23T01:43:12.388371+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 157

## Round 157

2 recorded events


### User

_source line 1639 · 2026-05-23T01:43:18.693555+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心结论**：Overall 3.5（Borderline Conference 高端），Soundness 4/5，Excitement 3/5。

**主要发现**：
- 实验设计严谨（matched-pair design + perturbation control + 多层验证），统计方法选择恰当且全面
- 1 个 Must-Fix：合成歧义子句的生态效度不足——template-based 生成的歧义可能系统性偏重，威胁 34.0pp 效应量的外部效度
- 5 个 Should-Fix：authorization scope κ=0.385 度量不可靠但 claim 未充分降级；incompleteness confound 的 token count proxy 不足；SOPBench replication 效应量衰减至 37% 需更审慎讨论；60.8% 残差方差的实践含义讨论不足；Type III SS 在二元结果上的方差分解作为 headline claim 需更多方法论说明

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1640 · 2026-05-23T01:43:23.805377+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 158

## Round 158

6 recorded events


### User

_source line 1641 · 2026-05-23T01:46:29.941617+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计严谨、统计分析全面的因果研究，matched-pair 方法论有贡献；但 taxonomy 将非歧义现象纳入 "ambiguity" 标签下导致核心声明被稀释，且 cross-judge type ranking 不一致（ρ=0.09）削弱了 type-level claims 的稳健性。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Matched-pair 设计严谨，perturbation/replication 控制充分；但 incompleteness 信息添加混淆未完全消除，cross-judge type ranking 不一致（ρ=0.09）削弱 C2 |
| Excitement | 3/5 | 因果设计和 variance decomposition 有方法论贡献，但核心发现（歧义导致违规）较为预期；disambiguation neglect 在先行工作基础上增量有限 |
| Reproducibility | 4/5 | 方法细节充分（模型版本、API 日期、参数、统计检验全部报告），承诺开源，SOPBench 跨基准 replication 增加可信度 |
| Confidence | 4/5 | 认真阅读全文含19页附录，对 RE 和 agent safety 文献有较好了解 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Taxonomy 将非歧义现象纳入 "ambiguity" 标签下，核心声明被稀释**

- 具体位置：§3 "Scope of 'ambiguity'"（"strictly, neither constitutes linguistic ambiguity"）；Title；Abstract
- 问题：论文在 §3 明确承认 incompleteness 和 conditional precedence 不属于 linguistic ambiguity——前者涉及信息缺失（absent information rather than multiple readings），后者涉及规范冲突（normative conflict rather than interpretive uncertainty）。然而标题 "Policy Ambiguity Is Nocuous" 和全文 framing 将它们统一归为 "ambiguity"。这造成三个层级的问题：
  - (a) **效应归因不准**：最强效应 (+49.2 pp) 来自 incompleteness，其 unambiguous variant 通过添加 policy content 而非消除歧义来解决问题。本质上是 "policy underspecification is nocuous" 而非 "policy ambiguity is nocuous"。
  - (b) **标题过度概括**：headline effect (+34.0 pp) 包含 incompleteness 的贡献，而 confound-free range (+18.7 至 +36.0 pp) 虽在 §5.1 末尾报告但并非 primary framing。
  - (c) **理论依据薄弱**：用 "behaviorally indistinguishable"（§3/§5）作为归类依据有实用主义合理性，但不同病因可以产生相同症状不等于它们是同一种病。
- 为什么影响接收：审稿人可能质疑核心声明的准确性。当最强信号来自公认的非歧义类型时，以 "ambiguity" 统一命名的说服力不足。
- 建议修改方向：(a) 标题改为包含 underspecification（如 "Policy Ambiguity and Underspecification Are Nocuous"），或 (b) 将 confound-free range 提升为 primary result，incompleteness 标记为 upper bound supplementary finding，或 (c) 加强 §3 对 inclusive definition 的理论论证——当前 "behaviorally indistinguishable" 一句话不够。

**N2** [critical] **Cross-judge type ranking 严重不一致，C2 partial ordering 的稳健性存疑**

- 具体位置：§5.2（"cross-judge-group type rankings are discordant (ρ = 0.09, p = 0.87)"）；Appendix W
- 问题：两组 judge 对六种 ambiguity type 的 violation rate ranking 本质上无相关性。论文的应对策略是 post-hoc 排除 authorization scope 后获得 ρ = 0.90，以及三家族交叉验证（ρ = 0.71-0.89）。但存在两个问题：
  - (a) **Post-hoc 排除**：从6种 type 中排除表现最异常的一种以获得一致性，方法论上有 cherry-picking 风险。论文虽然提供了排除的技术理由（auth scope κ = 0.385 低 agreement），但这本身就说明 taxonomy 中有一种 type 的测量不可靠。
  - (b) **实际应用限制**：C2 的核心价值在于为 "type-targeted diagnosis" 提供依据（§7），但如果 type ranking 在不同评判者下不稳定，这一应用场景的可行性就存疑。
- 为什么影响接收：C2 是论文三个 primary contribution 之一。如果 type ordering 高度依赖于 judge 选择，contribution 的实际价值被削弱。
- 建议修改方向：(a) 将 C2 的 framing 明确限定为 "robust extremes only"——incompleteness top 和 coreferential bottom 在所有 judge 下一致——而非 partial ordering；(b) 将 auth scope 的 judge sensitivity 从 qualifier 提升为 explicit limitation；(c) 考虑是否需要在主文而非 appendix 中报告三家族 judge 的完整 type ranking

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Incompleteness 信息添加混淆的处理虽合理但展示不足**

- 具体位置：§5.1 末尾、Appendix F/H、Limitations "Confounds"
- 问题：论文提供了三层控制——token count 代理（Appendix F，effect < 0.1 pp）、logistic regression（Appendix H）、confound-free lower bound（coreferential +18.7 pp）。这些措施方法论上合理。但 headline effect (+34.0 pp, OR = 15.1) 出现在 Abstract、Introduction、Results 开头和 Conclusion，而 confound-free range (+18.7 to +36.0 pp) 仅在 §5.1 段落末尾和 Limitations 中提及。读者很可能只记住 +34.0 pp 而忽略 confound caveat。
- 建议：在 Abstract 和 Conclusion 中加入 confound-free range 作为 robustness qualifier

**W2** [warning] **领域泛化性有限且 type-level 结果已显示领域依赖**

- 具体位置：§4.1、Limitations "Scope"、Appendix U
- 问题：τ²-bench 内部 retail vs airline 的 type ranking 已不一致（ρ = 0.26, p = 0.62），conditional precedence 在两个 domain 间差异达 22 pp。SOPBench replication 仍在客服领域。论文在 Limitations 中承认了这一点，但 Discussion 中的 "clause-level auditing is critical for customer-service and similar policy-governed deployments" 暗示了更广泛的适用性。
- 建议：Discussion 应更明确地讨论 C2 的 domain-specificity——当前 "type rankings vary across domains (ρ = 0.26)" 仅在 Limitations 出现一次

**W3** [warning] **Sections 6-8 过度压缩，Error Analysis 和 Discussion 未获得匹配其重要性的篇幅**

- 具体位置：Page 8
- 问题：Error Analysis（§6，3个子节含 disambiguation neglect 和 systematic nocuity 两个关键发现）、Discussion（§7，3段含 differential nocuity 假说和 taxonomy diagnostic tool 论证）和 Conclusion（§8）全部在 page 8 上。其中 Error Analysis 是论文三个 contribution 之一，但压缩程度使得每个 failure mechanism 只有1-2句话描述。相比之下，§5.3 用了整段报告 inconclusive 的 C3，Figures 2-3 占了 page 7 的大部分空间。
- 建议：将 C3（§5.3，inconclusive，4行文字）移至 appendix，释放空间给 §6-7

**W4** [warning] **Disambiguation neglect 的 novelty 需更清晰定位**

- 具体位置：§6.2
- 问题：Liu et al. (2023)、Hu et al. (2025)、Gur-Arieh et al. (2026) 已证明 LLM 将歧义折叠为单一解释。本文扩展至 agentic context 中的不可逆后果，但 §6.2 对 delta 的阐述仅一句："we extend this to agentic contexts where the result is irreversible policy violation"。更关键的贡献——mitigation experiment 证明 disambiguation 可被 prompt 激发（-8.5 pp），暗示 "neglect" 而非 "inability"——被放在了 Appendix B 而非主文。
- 建议：将 "neglect vs. inability" 的区分和 mitigation evidence 作为 §6.2 的核心论点，而非仅引用 appendix

**W5** [warning] **潜在遗漏的相关工作**

- 具体位置：§2 Related Work
- 问题：
  - (a) "Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges" (arxiv 2605.06161, May 2026)：发现 content-preserving policy rewrites 可翻转 9.1% 的 safety verdicts。这直接关系到本文的 cross-judge methodology——如果 policy wording 影响 judge 行为，论文的 cross-judge discordance（特别是 auth scope 的 κ = 0.385）可能部分源于此。
  - (b) "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents" (arxiv 2603.20320, March 2026)：另一个使用 paired evaluation 的因果研究，关注 tool affordance 而非 policy ambiguity，但方法论可比。应在 §2 讨论以更精确定位 "first causal study" 声明的范围。
  - (c) Specification gaming 文献（如 Krakovna et al.）未被引用——agents 在歧义 policy 下的行为可能与 specification gaming 有关联
- 建议：补充上述引用，特别是 (a) 可帮助解释 cross-judge 现象，(b) 可帮助更精确地定位 novelty claim

---

## 小问题（不影响接收）

1. **Abstract 数字密度**：7+ 个具体数值（34.0 pp, OR=15.1, 22.4%, 0.4%, 17×, ≤11%, 41.3%），信息量大但可读性受影响，建议精简至 4 个核心数字
2. **匿名引用**："Anonymous (2025)" 在 references 中出现，如为 self-citation 需确保符合 double-blind 规范
3. **"Nocuous" 术语**：来自 Berry & Kamsties (2004) 的 RE 文献，对 NLP 社区读者可能不直观——建议首次使用时加括号说明 "(i.e., harmful)" ← 实际上论文已这样做了，忽略此条
4. **Figure 3 caption 过长**（5行），可精简并将统计细节移至正文
5. **§5.3 C3 (Layer Effect)**：占用正文空间但结论为 inconclusive，且在 Holm-Bonferroni 校正后不显著——可移至 appendix
6. **Data and Code Availability 的 GitHub URL**：使用 `anonymous` 用户名，格式合规

---

## 主要优势

1. **Matched-pair 因果设计的方法论贡献**：与 DRIP-R（相关性研究）和 PolicyBank（迭代优化）不同，本文通过配对设计建立因果关系。Perturbation control（Δ_perturb = -0.67 pp, CI containing zero）有效排除了表面扰动的干扰，96% 标注者一致率和 100% 讨论后共识保证了 stimulus 质量。

2. **Variance decomposition 视角新颖**：22.4% clause vs 0.4% type 的分解是一个重要的负面结果——它说明 type-level 分类系统（包括本文自己的 taxonomy）不应被用于 risk prediction，风险的真正来源在于 individual clause wording。这个 insight 对实际部署中的 policy auditing 有直接指导意义。

3. **NMI 分析优雅地重新定位了 taxonomy 的价值**：type predicts mechanism 17× better than violation rate 的发现巧妙地将 taxonomy 从 "risk predictor"（variance 解释力仅 0.4%，容易被攻击）转化为 "diagnostic tool"（NMI = 0.23 vs. 0.01），化解了 type-level 解释力不足的问题。

4. **Claim hierarchy 体现学术审慎**：C1-C4 的 primary/exploratory 区分、C3 的 inconclusive 标注、incompleteness confound 的 transparent 处理、authorization scope 的 judge-dependence 披露——论文没有回避自身的弱点。

5. **统计严谨性远超同类工作**：7个模型（5 primary + 2 replication）、3个 judge family、SOPBench 跨基准复制、7个 TOST margin sensitivity（±5 to ±20 pp）、permutation test（n=1000）、bootstrap cluster（B=10000）、Holm-Bonferroni 校正、ICC replication (0.919)——robustness check 的广度和深度令人印象深刻。

6. **Related work 覆盖系统性强**：RE、psycholinguistics、agent safety evaluation、policy specification 四个方向均有系统引用。与 DRIP-R 的三点区别（causal vs. correlational；safety violations vs. decision quality；linguistic+specification layer vs. RE only）论述清晰公允。DRIP-R mapping（Appendix L）进一步增加了可比性。

---

## Questions for Authors

1. 如果完全排除 incompleteness，五种 type 的 pooled effect size 是多少？这能否作为 "genuine ambiguity" 的 primary effect 报告？
2. 实验使用 temperature=0（deterministic），部署环境通常 temperature>0。随机性是否可能改变 disambiguation neglect 的程度或 systematic nocuity 的 convergence rate？
3. Mitigation 对 incompleteness 几乎无效（-3.3 pp vs. auth scope 的 -18.0 pp），这是否构成一个独立证据说明 incompleteness 与 ambiguity 的本质不同——前者需要 policy revision 而后者可被 prompt 解决？
4. Authorization scope 的 cross-judge discordance 的根本原因是什么？是 "authorization violation" 的评判标准模糊（κ=0.385），还是不同 judge model 对 "permission boundary" 的理解不同？
5. 300 clause pairs 均匀分配（每 type 50 pairs）——真实 policy 文档中各 type 的自然分布是什么？均匀设计是否高估了低频 type 的权重？

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤8 页 | ✓ | §1-8 在 pages 1-8 内，Limitations 从 page 8 底部开始（不计入页数）|
| Limitations section | ✓ | 4段，覆盖 Scope、Measurement、Confounds、Disambiguation channel |
| ACL/natbib 格式 | ✓ | 使用 acl.sty + acl_natbib.bst |
| Double-blind | ✓ | "Anonymous ACL submission"；Anonymous (2025) 引用可能是 self-citation 但格式合规 |
| Figure/Table 引用 | ✓ | Figure 1-3, Table 1-2 均在正文中引用 |
| Ethics statement | — | 未见独立 Ethics section，但 Limitations 中涉及 confound 和 evaluation bias 讨论 |

---

## Taxonomy 定位评估（专项）

1. **"Experimental instrument" 定位**：§3 和 §7 将 taxonomy 定位为实验工具而非分类标准，这在 variance decomposition（0.4% type variance）结果下是合理的自我定位。但 §6.1 的 error analysis 又将 taxonomy 用于 "type-specific failure mechanisms" 的组织框架，且 Discussion 提出 "type-targeted diagnosis"——这暗示了 taxonomy 的分类功能，与 "not a classification standard" 的声明有张力。

2. **非歧义类型的归类理论**：§3 的论证链为 "frequently co-occur in RE" → "behaviorally indistinguishable" → "included under ambiguity broadly"。这个论证的第一步（频繁共现）是事实，第二步（行为不可区分）有§6.1 的证据支持（不同 type 确实有不同 failure modes，所以行为其实是可区分的——这反而削弱了 "behaviorally indistinguishable" 的声明）。需要更仔细的论证。

3. **6 types 的选择透明度**：论文引用了 Li et al. (2024b) 的 11-type NLP taxonomy 和 Massey et al. (2014) 的 6-type RE taxonomy，但未解释为什么从 Li 的 11 types 中选了 3 个（lexical, scopal, coreferential），从 RE 中选了 3 个。Appendix L 的 DRIP-R mapping 帮助解释了与 DRIP-R 的关系，但选择标准（"based on frequency in operational policy documents and theoretical distinctiveness"）仅一句话带过。

---

**总结**：这是一篇执行质量很高的实证研究，matched-pair 设计和 variance decomposition 有方法论贡献。主要问题在于：(1) taxonomy 的 "ambiguity" 标签 overreach（N1）和 (2) cross-judge type ranking instability（N2）。若能解决 N1（调整 framing/标题）并在 N2 上更 transparent，整体质量可达 Conference 水平（4.0）。当前评分 3.5 反映了 novelty 的不确定性——core finding "ambiguity is bad" 较为预期，但方法论和分析深度弥补了部分 novelty 不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-23T01:47:11.101510+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1, N2) 和 Should-Fix (W1-W5) 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Taxonomy 将非歧义现象纳入 \"ambiguity\" 标签下，核心声明被稀释\n- §3 承认 incompleteness 和 conditional precedence 不属于 linguistic ambiguity\n- 最强效应 (+49.2 pp) 来自 incompleteness，其 unambiguous variant 通过添加 policy content 而非消除歧义\n- 标题 \"Policy Ambiguity Is Nocuous\" 过度概括\n- \"behaviorally indistinguishable\" 作为归类依据不够——不同病因可产生相同症状不等于同一种病\n- 建议：标题改为包含 underspecification，或将 confound-free range 提升为 primary result\n\n**N2** [critical] Cross-judge type ranking 严重不一致，C2 partial ordering 的稳健性存疑\n- 两组 judge 的 type ranking ρ=0.09 (p=0.87)\n- Post-hoc 排除 auth scope 获得 ρ=0.90 有 cherry-picking 风险\n- C2 作为 primary contribution 之一，如果 type ordering 高度依赖 judge 选择，实际价值被削弱\n- 建议：将 C2 限定为 \"robust extremes only\"\n\n### Should-Fix\n\n**W1** [warning] Incompleteness 信息添加混淆的展示不足\n- Headline effect (+34.0 pp) 在 Abstract/Intro/Conclusion 反复出现，confound-free range (+18.7 to +36.0 pp) 仅在 §5.1 末尾\n- 建议：Abstract 和 Conclusion 中加入 confound-free range\n\n**W2** [warning] 领域泛化性有限且 type-level 结果已显示领域依赖\n- retail vs airline type ranking ρ=0.26，conditional precedence 差异 22pp\n- Discussion 的 policy auditing 建议暗示更广泛适用性\n\n**W3** [warning] Sections 6-8 过度压缩\n- Error Analysis、Discussion、Conclusion 全在 page 8\n- Error Analysis 是三个 contribution 之一但每个 failure mechanism 仅 1-2 句\n\n**W4** [warning] Disambiguation neglect 的 novelty 需更清晰定位\n- 先行工作已证明 LLM 将歧义折叠为单一解释\n- \"neglect vs. inability\" 区分和 mitigation evidence 被放在 Appendix 而非主文\n\n**W5** [warning] 潜在遗漏相关工作\n- \"Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges\" (arxiv 2605.06161)\n- \"The Causal Impact of Tool Affordance on Safety Alignment\" (arxiv 2603.20320)\n- Specification gaming 文献（Krakovna et al.）\n\n### Questions\n1. 排除 incompleteness 后五种 type 的 pooled effect size？\n2. temperature>0 部署环境是否改变 disambiguation neglect？\n3. Mitigation 对 incompleteness 无效是否证明其与 ambiguity 本质不同？\n4. Auth scope cross-judge discordance 的根本原因？\n5. 真实 policy 文档中各 type 的自然分布？\n\n### Taxonomy 定位评估\n- §6.1 的 type-specific failure mechanisms 组织功能与 \"not a classification standard\" 有张力\n- \"behaviorally indistinguishable\" 声明被 §6.1 自身削弱（不同 type 有不同 failure modes）\n- 6 types 选择标准不透明"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1, N2) 和 Should-Fix (W1-W5) 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Taxonomy 将非歧义现象纳入 \"ambiguity\" 标签下，核心声明被稀释\n- §3 承认 incompleteness 和 conditional precedence 不属于 linguistic ambiguity\n- 最强效应 (+49.2 pp) 来自 incompleteness，其 unambiguous variant 通过添加 policy content 而非消除歧义\n- 标题 \"Policy Ambiguity Is Nocuous\" 过度概括\n- \"behaviorally indistinguishable\" 作为归类依据不够——不同病因可产生相同症状不等于同一种病\n- 建议：标题改为包含 underspecification，或将 confound-free range 提升为 primary result\n\n**N2** [critical] Cross-judge type ranking 严重不一致，C2 partial ordering 的稳健性存疑\n- 两组 judge 的 type ranking ρ=0.09 (p=0.87)\n- Post-hoc 排除 auth scope 获得 ρ=0.90 有 cherry-picking 风险\n- C2 作为 primary contribution 之一，如果 type ordering 高度依赖 judge 选择，实际价值被削弱\n- 建议：将 C2 限定为 \"robust extremes only\"\n\n### Should-Fix\n\n**W1** [warning] Incompleteness 信息添加混淆的展示不足\n- Headline effect (+34.0 pp) 在 Abstract/Intro/Conclusion 反复出现，confound-free range (+18.7 to +36.0 pp) 仅在 §5.1 末尾\n- 建议：Abstract 和 Conclusion 中加入 confound-free range\n\n**W2** [warning] 领域泛化性有限且 type-level 结果已显示领域依赖\n- retail vs airline type ranking ρ=0.26，conditional precedence 差异 22pp\n- Discussion 的 policy auditing 建议暗示更广泛适用性\n\n**W3** [warning] Sections 6-8 过度压缩\n- Error Analysis、Discussion、Conclusion 全在 page 8\n- Error Analysis 是三个 contribution 之一但每个 failure mechanism 仅 1-2 句\n\n**W4** [warning] Disambiguation neglect 的 novelty 需更清晰定位\n- 先行工作已证明 LLM 将歧义折叠为单一解释\n- \"neglect vs. inability\" 区分和 mitigation evidence 被放在 Appendix 而非主文\n\n**W5** [warning] 潜在遗漏相关工作\n- \"Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges\" (arxiv 2605.06161)\n- \"The Causal Impact of Tool Affordance on Safety Alignment\" (arxiv 2603.20320)\n- Specification gaming 文献（Krakovna et al.）\n\n### Questions\n1. 排除 incompleteness 后五种 type 的 pooled effect size？\n2. temperature>0 部署环境是否改变 disambiguation neglect？\n3. Mitigation 对 incompleteness 无效是否证明其与 ambiguity 本质不同？\n4. Auth scope cross-judge discordance 的根本原因？\n5. 真实 policy 文档中各 type 的自然分布？\n\n### Taxonomy 定位评估\n- §6.1 的 type-specific failure mechanisms 组织功能与 \"not a classification standard\" 有张力\n- \"behaviorally indistinguishable\" 声明被 §6.1 自身削弱（不同 type 有不同 failure modes）\n- 6 types 选择标准不透明"
  }
}
```

</details>

---


### Tool result

_source line 1643 · 2026-05-23T01:47:38.578952+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27477
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-23T01:47:38.730016+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1) 和 Should-Fix (W1-W5) 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] 合成歧义子句的生态效度（Ecological Validity）不足\n- 300 clause pairs 通过 template-based pipeline 生成\n- Appendix R 示例显示部分歧义变体更接近\"严重措辞不当\"而非真实世界细微歧义\n- Incompleteness 示例将多个具体参数全部替换为模糊词（\"large\", \"appropriate\", \"timely\"），这种程度在实际政策中罕见\n- Post-hoc realism validation 仅验证词汇风格，未验证歧义分布和程度\n- τ²-bench 本身政策也是合成的\n- 建议：量化合成歧义与真实政策歧义差异，或承认效应量可能高估\n\n### Should-Fix\n\n**W1** [warning] Authorization scope 度量可靠性不足但 claim 未充分降级\n- κ=0.385 低于 \"fair\" 门槛\n- Cross-judge-group ranking discordance ρ=0.09 由 auth scope rank reversal 驱动\n- §5.4 仍将 auth scope 描述为 \"most model-differentiating type\"\n- 建议：Figure 3 caption 标注 κ 值，将 \"most model-differentiating\" 改为条件性表述\n\n**W2** [warning] Incompleteness confound 的 token count proxy 不足\n- Token count 无法区分信息类型\n- Auth scope token delta (+36.1) > incompleteness (+34.6) 但添加的信息性质不同\n- Coreferential lower bound 只提供下界，不能确定 49.2pp 中多少归因于歧义 vs 信息缺失\n- 建议：讨论 token count 作为 proxy 的信息类型局限性\n\n**W3** [warning] SOPBench replication 效应量大幅衰减需更审慎讨论\n- 效应量仅为 τ²-bench 的 37%（+12.6pp vs +34.0pp）\n- 5 模型中仅 3 个 p<0.01，GPT-5.4 borderline，DeepSeek 不显著\n- \"directional consistency across all five models\" framing 过于宽泛\n- 建议：报告 pooled effect size 和 CI，改为更审慎表述\n\n**W4** [warning] 60.8% 残差方差的实践含义讨论不足\n- ~46% systematic-but-unmeasured 是最大单一成分\n- 对 \"clause-level auditing\" 建议构成限制——最多解释 22.4%\n- 建议：Discussion 讨论 22.4% 是可操作最大因素但非最大因素\n\n**W5** [warning] Type III SS 在二元结果上的方差分解作为 headline claim 需更多说明\n- 线性概率模型在极端概率时近似质量差\n- Logistic regression Tjur's R²=0.175 不提供直接可比方差分配\n- 建议：正文中讨论线性 vs logistic 差异，报告 logistic regression 的 partial R²\n\n### Questions\n1. Template-based pipeline 操作细节？\n2. 96% annotator agreement 的 chance-corrected κ？\n3. 是否考虑结构性扰动作为控制？\n4. 是否有 cross-provider ICC 数据？\n5. 65% ambiguous stratification 对 κ 估计的影响？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "director_session_key": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1) 和 Should-Fix (W1-W5) 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] 合成歧义子句的生态效度（Ecological Validity）不足\n- 300 clause pairs 通过 template-based pipeline 生成\n- Appendix R 示例显示部分歧义变体更接近\"严重措辞不当\"而非真实世界细微歧义\n- Incompleteness 示例将多个具体参数全部替换为模糊词（\"large\", \"appropriate\", \"timely\"），这种程度在实际政策中罕见\n- Post-hoc realism validation 仅验证词汇风格，未验证歧义分布和程度\n- τ²-bench 本身政策也是合成的\n- 建议：量化合成歧义与真实政策歧义差异，或承认效应量可能高估\n\n### Should-Fix\n\n**W1** [warning] Authorization scope 度量可靠性不足但 claim 未充分降级\n- κ=0.385 低于 \"fair\" 门槛\n- Cross-judge-group ranking discordance ρ=0.09 由 auth scope rank reversal 驱动\n- §5.4 仍将 auth scope 描述为 \"most model-differentiating type\"\n- 建议：Figure 3 caption 标注 κ 值，将 \"most model-differentiating\" 改为条件性表述\n\n**W2** [warning] Incompleteness confound 的 token count proxy 不足\n- Token count 无法区分信息类型\n- Auth scope token delta (+36.1) > incompleteness (+34.6) 但添加的信息性质不同\n- Coreferential lower bound 只提供下界，不能确定 49.2pp 中多少归因于歧义 vs 信息缺失\n- 建议：讨论 token count 作为 proxy 的信息类型局限性\n\n**W3** [warning] SOPBench replication 效应量大幅衰减需更审慎讨论\n- 效应量仅为 τ²-bench 的 37%（+12.6pp vs +34.0pp）\n- 5 模型中仅 3 个 p<0.01，GPT-5.4 borderline，DeepSeek 不显著\n- \"directional consistency across all five models\" framing 过于宽泛\n- 建议：报告 pooled effect size 和 CI，改为更审慎表述\n\n**W4** [warning] 60.8% 残差方差的实践含义讨论不足\n- ~46% systematic-but-unmeasured 是最大单一成分\n- 对 \"clause-level auditing\" 建议构成限制——最多解释 22.4%\n- 建议：Discussion 讨论 22.4% 是可操作最大因素但非最大因素\n\n**W5** [warning] Type III SS 在二元结果上的方差分解作为 headline claim 需更多说明\n- 线性概率模型在极端概率时近似质量差\n- Logistic regression Tjur's R²=0.175 不提供直接可比方差分配\n- 建议：正文中讨论线性 vs logistic 差异，报告 logistic regression 的 partial R²\n\n### Questions\n1. Template-based pipeline 操作细节？\n2. 96% annotator agreement 的 chance-corrected κ？\n3. 是否考虑结构性扰动作为控制？\n4. 是否有 cross-provider ICC 数据？\n5. 65% ambiguous stratification 对 κ 估计的影响？"
  }
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-23T01:47:40.091349+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 1646 · 2026-05-23T01:47:43.394446+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 159

## Round 159

2 recorded events


### User

_source line 1647 · 2026-05-23T01:47:45.972838+00:00_

[Reviewer 2 审稿结果]:
审稿完成。报告已提交至 Review Director，评分 **Overall 3.5 (Borderline Conference)**。

核心问题两个：
1. **N1**：Taxonomy 将 incompleteness/conditional precedence（论文自己承认非 linguistic ambiguity）纳入 "ambiguity" 标签，导致标题声明 "Policy Ambiguity Is Nocuous" 过度概括——最强效应 (+49.2 pp) 来自非歧义类型
2. **N2**：Cross-judge type ranking ρ = 0.09，C2 partial ordering 的稳健性高度依赖 post-hoc 排除 authorization scope

主要优势在于 matched-pair 因果设计的方法论严谨性、variance decomposition（22.4% clause vs 0.4% type）的新颖视角、以及 NMI 分析将 taxonomy 重新定位为 diagnostic tool 的巧妙处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1648 · 2026-05-23T01:47:50.624597+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 1649 · 2026-05-23T01:49:27.945398+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### R2-N1: Taxonomy 将非歧义现象纳入 "ambiguity" 标签，核心声明被稀释

**[AGREE]**（部分同意，同意 framing 问题但不同意 taxonomy 根本无效）

R2 指出的核心问题是成立的：§3 明确承认 "Strictly, neither constitutes linguistic ambiguity: incompleteness involves absent information rather than multiple readings, and conditional precedence involves normative conflict rather than interpretive uncertainty"。论文自己已承认这两种类型不属于语言学意义上的 ambiguity，但仍将它们纳入 "ambiguity taxonomy" 并在标题中使用 "Policy Ambiguity Is Nocuous"——这确实存在术语拉伸。

R2 对 "behaviorally indistinguishable" 论证的反驳（"不同病因产生相同症状不等于同一种病"）很有力，且被论文自身的 §6.1 削弱——§6.1 恰恰展示了不同 type 有*不同的*dominant failure mechanisms（structural misparse vs. gap-filling vs. boundary violation），说明它们在行为层面也并非完全 indistinguishable。

然而，我不同意 R2 认为这完全 invalidates taxonomy 的立场。论文遵循 Berry & Kamsties (2004) 对 nocuous ambiguity 的定义，该定义在 RE 文献中确实涵盖了 specification-level gaps。并且论文已在 §5.1 报告了 confound-free range（+18.7 to +36.0pp），排除 incompleteness 后 pooled effect 仍为 +31.0pp（Appendix Q, p < 10⁻⁷⁵）。

**我的建议**：R2 提出的两个修改方向都是合理的——(1) 标题改为涵盖 underspecification（如 "Policy Ambiguity and Underspecification Are Nocuous"）；(2) 或将 confound-free range 提升为 primary result。我倾向于方案 (2)，因为改标题可能过度缩小论文范围，而提升 confound-free range 的可见度既解决了 framing 问题又保持了论文贡献的完整性。具体来说，Abstract 中应在 "+34.0 percentage points" 之后立即加入 confound-free range（+18.7 to +36.0pp）。

---

### R2-N2: Cross-judge type ranking ρ=0.09，C2 partial ordering 稳健性存疑

**[REBUT]**（部分反驳：post-hoc 排除有合理依据，且三家族验证提供了独立证据）

R2 关于 "post-hoc 排除 auth scope 后 ρ=0.90 有 cherry-picking 风险" 的方法论关切是合理的。但需要考虑以下证据：

1. **排除的因果依据不是统计驱动的，而是构成性的**。Appendix P 详细解释了 ρ=0.09 的来源：两组 judge 评估的模型组成不同（GPT-4.1 judged group 包含 DeepSeek 60% 和 GPT-5.4 64% 这两个 auth scope 最高的模型；GPT-5.4 judged group 包含 Claude 12% 这个最低的）。Rank reversal 由*模型组成差异*而非*judge bias*驱动。这不是 post-hoc data snooping——排除的理由来自设计层面的已知混淆。

2. **三家族 cross-judge validation 提供了独立验证**。Appendix W 用 GPT-4.1、Claude、Gemini 三个 judge 在*相同的* 2,997 episodes 上评估，type ranking pairwise ρ=0.71-0.89，三个 judge 都将 incompleteness 排最高、coreferential/conditional precedence 排最低。这是一个更干净的测试，因为排除了模型组成的混淆。

3. **论文已经在 §5.2 采纳了 R2 建议的 framing**。§5.2 末段明确写道："C2 should be interpreted as establishing robust extremes—incompleteness as upper bound and coreferential as lower bound—rather than a complete linear ordering"。这正是 R2 建议的 "robust extremes only"。

**不过**，我同意这个 framing 在论文中不够突出。Abstract 和 Introduction 中对 C2 的描述（"per-type effects range from +18.7 to +49.2pp"）给人一种 complete ordering 的印象。建议在 Abstract 中明确使用 "partial ordering with robust extremes" 的表述。

---

### R2-W1: Confound-free range 未出现在 Abstract/Conclusion

**[AGREE]**

这与我自己的 W2（incompleteness confound）一致。+34.0pp 包含了 confounded 的 incompleteness，Abstract 中应紧跟 confound-free range（+18.7 to +36.0pp）。Conclusion 中同样应加入此信息。这是一个纯粹的写作/展示问题，不影响数据质量，但对读者理解至关重要。

---

### R2-W2: 领域泛化性有限

**[AGREE]**

Cross-domain type ranking ρ=0.26（Appendix U）与 conditional precedence 跨域差异 22pp 已在论文中报告，但 Discussion §7 中的 "clause-level auditing" 建议确实暗示了超出实际数据支持的泛化范围。

补充我自己的观察：SOPBench replication（Appendix V）效应量仅为 τ²-bench 的 37%（+12.6pp vs +34.0pp），2/5 模型未达显著。这进一步限制了跨 benchmark 泛化的证据强度。建议 Discussion 中明确标注 auditing 建议的适用范围限于 customer service 类似领域。

---

### R2-W3: Sections 6-8 过度压缩

**[REBUT]**（部分反驳：受限于页数约束，且详细内容已在 Appendix 中展开）

R2 指出 Error Analysis（§6）、Discussion（§7）、Conclusion（§8）全在 page 8 是事实。但需要考虑：

1. **8 页硬限制**是投稿格式约束。§1-5 包含了 experimental platform、matched-pair design、5 models、evaluation pipeline、controls、statistical analysis 和四个 claims 的完整结果——这些内容的信息密度很高且不宜删减。

2. **Error Analysis 的详细支撑在 Appendix 中**。Type-mechanism confusion matrix（Appendix S, Table 14）、mutual information analysis（Appendix S, Table 13）、clause-level risk predictors（Appendix T）提供了充分的细节。

3. **三个 failure mechanisms 虽然每个仅 1-2 句，但描述是精确的**。"Structural misparse: the agent constructs an incorrect parse and follows it consistently"——这在 2 句内完成了定义和 dominant type 的关联。

**不过**，我同意 §6.2 (Disambiguation Neglect) 和 §6.3 (Systematic Nocuity) 可以更充分展开。特别是 disambiguation neglect 的 "neglect vs inability" 论证仅在 §6.2 用一句提及（"not inability"），关键支撑证据（mitigation experiment -8.5pp）被引用到 Appendix B 而未给出任何细节。建议在 §6.2 中至少用 2-3 句概述 mitigation 结果来支撑 "neglect" 的定性。

---

### R2-W4: Disambiguation neglect 的 novelty 定位

**[AGREE]**（部分同意）

R2 正确指出 Liu et al. (2023) 和 Hu et al. (2025) 已证明 LLM 将歧义折叠为单一解释。论文声称的增量 novelty 是将此现象扩展到 "agentic contexts where the result is irreversible policy violation"（§6.2）。这个定位是合理的——先行工作研究的是 QA 或 text interpretation 场景，而非 agent 执行不可逆操作的场景。

但我同意 R2 的观点：这一 novelty distinction 在正文中阐述不够清晰。"neglect vs inability" 的区分以及 mitigation 证据（Appendix B: -8.5pp, 其中 auth scope -18.0pp）是支撑这一 claim 的关键证据，不应完全放在 Appendix 中。建议在 §6.2 中增加 2-3 句概述 mitigation 实验设计和主要结果。

---

### R2-W5: 潜在遗漏相关工作

**[AGREE]**（有条件同意——无法完全验证引用的 arxiv 论文，但同意 specification gaming 文献的遗漏）

我无法独立验证 R2 引用的两篇 2026 arxiv 论文（2605.06161 和 2603.20320）的相关性，但从标题判断它们与本文主题高度相关：

- "Policy Invariance as a Reliability Test for LLM Safety Judges" 直接关联 cross-judge evaluation（§4.4, Appendix W）
- "Causal Impact of Tool Affordance on Safety Alignment" 关联 agentic safety 的因果分析框架

Specification gaming 文献（Krakovna et al.）确实是一个值得讨论的对照：agent 利用 policy specification 中的漏洞属于 intentional exploitation，而本文研究的是 unintentional misinterpretation。这种区分在 §7 Discussion 中值得一提。

建议作者检查这三篇文献并在 Related Work 中适当讨论。

---

### R2 提出的 Questions 的补充观察

**Q1 (排除 incompleteness 后 pooled effect)**：论文已在 Appendix Q 报告了答案——Δ=+31.0pp, OR=7.75, p < 10⁻⁷⁵。这个结果应该被提升到正文 §5.1 中。

**Q3 (Mitigation 对 incompleteness 无效是否说明其本质不同于 ambiguity)**：这是一个尖锐的问题。Appendix B Table 4 显示 incompleteness mitigation 仅 -3.4pp（pooled），远低于 auth scope 的 -18.0pp。如果 prompt-based disambiguation 对 incompleteness 无效，这确实暗示 incompleteness 的 failure mechanism 不同于 ambiguity resolution——更多是 information gap 而非 interpretation conflict。这进一步支持了 R2-N1 的论点。

**Q4 (Auth scope discordance 根本原因)**：Appendix P 的解释是模型组成差异而非 judge bias。但 Appendix W 显示即使三个 judge 评估相同 episodes，auth scope 的 within-judge model range 也是 judge-dependent（GPT 52pp, Claude 30pp, Gemini 24pp）。这说明 auth scope 的度量本身就不稳定，不仅仅是模型组成问题。

---

### Taxonomy 定位评估的回应

R2 指出 "behaviorally indistinguishable" 声明被 §6.1 自身削弱——不同 type 有不同 dominant failure modes——这是一个非常精准的内部矛盾。论文不能同时声称：(a) 这些 types 在 behavioral outcome 上 indistinguishable 所以归入同一 taxonomy；(b) 这些 types 有 distinct failure mechanisms 所以 taxonomy 有 diagnostic 价值。

我认为解决方案是：(a) 放弃 "behaviorally indistinguishable" 的归类依据；(b) 改用 "these specification-level phenomena produce comparable safety impact in LLM agents" 的 pragmatic framing，同时明确承认它们与 linguistic ambiguity 的 mechanism-level 区别。这样既保留了 taxonomy 的实用价值，又避免了概念上的自相矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1650 · 2026-05-23T01:49:37.112571+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 161

## Round 161

10 recorded events


### User

_source line 1651 · 2026-05-23T01:49:39.692754+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### R1-N1: 合成歧义子句的生态效度不足

**[AGREE]** 同意这是本文最重要的外部效度威胁之一。

R1 指出的核心问题——template-based pipeline 生成的歧义可能比真实世界更极端——是成立的。几个具体观察：

1. **Incompleteness 的极端程度**：§3 Table 1 中 incompleteness 的示例（将具体参数替换为 "large", "appropriate" 等模糊词）确实接近"严重措辞不当"而非自然产生的细微歧义。这可能部分解释了 incompleteness 的 +49.2 pp 效应为何如此之高。

2. **Realism validation 的局限**：§4.2 的 post-hoc realism validation "confirms linguistic consistency with original τ²-bench policy text" 仅验证词汇风格的一致性，未验证歧义程度的自然性——即合成歧义子句中的歧义"量"是否符合真实 policy 的分布。

3. **效应量高估风险**：SOPBench replication 的效应量衰减至 37%（+12.6 pp vs +34.0 pp，见 §5.1）可能正是因为 SOPBench 使用了不同（可能更自然）的 policy 文档。这一衰减间接支持了 R1 关于 τ²-bench 上效应量可能被高估的判断。

**补充我自己的观察**：尽管生态效度存疑，论文的核心贡献在于建立因果关系（causal mechanism）而非精确量化效应量。即便真实歧义更微妙、效应更小，因果方向仍然成立。但论文应更明确地将 +34.0 pp 定位为 "upper bound under controlled synthetic conditions" 而非部署场景的预期效应量。Limitations 中虽提到 "may not capture the full distribution of naturally occurring ambiguities"（§Limitations "Scope"），但这一 caveat 应更显著地出现在 Abstract 或 Discussion 中。

---

### R1-W1: Authorization scope 度量可靠性不足但 claim 未充分降级

**[AGREE]** 强烈同意。这与我在 N2 中提出的 cross-judge discordance 问题高度一致。

具体补充：
- §5.4 Figure 3 caption 长达 5 行但未标注 auth scope 的 κ = 0.385，读者无法从图中获知这一关键 reliability 信息
- §5.4 使用 "most model-differentiating type (52 pp range; Claude 12% to GPT-5.4 64%)" 的表述时，未同时注明这也是 least reliably measured type
- 我的 N2 中指出 cross-judge-group type ranking ρ = 0.09 本质上无相关性，R1 正确识别了这一不一致性的驱动因素（auth scope rank reversal）

R1 的具体建议——Figure 3 caption 标注 κ 值、将 "most model-differentiating" 改为条件性表述——均合理且容易实施。

---

### R1-W2: Incompleteness confound 的 token count proxy 不足

**[AGREE]** 同意 token count 作为信息量代理变量的局限性。

R1 提出了一个我未充分展开的关键区分：auth scope 的 token delta (+36.1) 与 incompleteness (+34.6) 相近，但信息性质不同——前者是 boundary clarification（细化权限边界），后者是 content addition（补充缺失政策内容）。Token count 等量不等于 information content 等量。

论文在 Limitations 中承认 "token count difference between ambiguous and unambiguous variants is an imperfect proxy for informational asymmetry; future work could employ semantic complexity metrics"，但这一 caveat 的力度不够。更具体地说：

- Appendix F 报告 token count 控制后各 type 的 predicted effect 变化 < 0.1 pp，但这只说明 token count 本身不是 confound 的 effective proxy——而非说明 confound 不存在
- Coreferential lower bound (+18.7 pp) 提供了 confound-free 下界，但 +18.7 到 +49.2 的巨大范围（30.5 pp）暗示 incompleteness 的真实 "ambiguity" 效应可能远低于其 headline 数字

我在 W1 中建议 Abstract 和 Conclusion 更显著报告 confound-free range，R1 的建议（讨论信息类型局限性）是对此的有益补充。

---

### R1-W3: SOPBench replication 效应量大幅衰减需更审慎讨论

**[AGREE]** 同意当前 framing 过于乐观。

§5.1 报告 SOPBench replication 为 "+12.6 pp unweighted mean; three individually significant at p < 0.01"，并称 "directional consistency across all five models"。但：

1. **效应量衰减 63%**（+12.6 vs +34.0 pp）是一个需要解释的实质性差异，不应被 "directional consistency" 一笔带过
2. **2/5 模型不显著**（GPT-5.4 borderline, DeepSeek 不显著）意味着 "across all five models" 的表述有误导性——应为 "in three of five models, with two showing non-significant trends"
3. 论文未报告 SOPBench replication 的 pooled effect size CI，读者无法判断 +12.6 pp 的精度

R1 的建议（报告 pooled CI、改为更审慎表述）合理。衰减可能有多种解释——SOPBench 的 policy 更自然（支持 R1-N1 的生态效度 concern）、benchmark 结构不同、或 ambiguity 类型分布不同——但论文应逐一讨论而非仅报告 directional consistency。

---

### R1-W4: 60.8% 残差方差的实践含义讨论不足

**[AGREE]** 部分同意，但认为论文的 framing 已基本合理。

§7 Discussion 表述为 "60.8% of variance remains unexplained (conversation trajectory, user-simulator stochasticity); clause-level auditing targets the largest controllable factor (22.4%)"。"largest controllable factor" 的限定词是准确的——conversation trajectory 和 user-simulator stochasticity 虽然占比更大但不是 policy 设计者可以控制的。

R1 的要求——更明确讨论 22.4% 是"可操作最大因素但非最大因素"——合理但论文实际上已接近这个表述。建议在 Discussion 中补充一句说明：在 22.4% 之外，15.8% 来自 condition（ambiguous vs. unambiguous，即本研究的 treatment 变量），1.0% 来自 model——这三个可量化因素合计 39.2%，残余 60.8% 来自 conversation dynamics 等不可控因素。这样读者能更清楚地理解 variance landscape。

---

### R1-W5: Type III SS 在二元结果上的方差分解需更多说明

**[AGREE]** 同意这是一个方法论上的合法关切。

线性概率模型（LPM）在极端概率下（如 unambiguous condition 的 6.9% violation rate）的近似质量确实较差。论文在 §5.1 脚注中承认了这一点并引用了 logistic regression 的 concordant factor ordering（Tjur's R² = 0.175），但：

1. **22.4% 作为 headline claim 的风险**：如果 LPM 的方差分解在极端概率下不可靠，那么 22.4% 这个数字的精度就值得怀疑。论文未报告 logistic regression 中 clause identity 的 partial R² 或等效指标，读者无法判断 22.4% 在 logistic framework 下是否保持。
2. **比较基础**：0.4%（type）vs 22.4%（clause）的 relative comparison 可能在 logistic framework 下仍然成立（factor ordering concordant），但绝对值可能不同。

R1 的建议（正文讨论 linear vs logistic 差异，报告 logistic partial R²）合理。即使绝对值变化，clause >> type 的 ordering 若保持一致，核心论点不受影响。建议论文补充 logistic framework 下的等效指标以增强 robustness。

---

### 对 R1 Questions 的补充观察

**Q2（96% agreement 的 chance-corrected κ）**：这是一个重要遗漏。§4.2 报告 "96% initial agreement (287/300)" 但仅给出 raw agreement，未报告 chance-corrected κ。在 6-type 分类任务中，chance agreement 取决于 type prevalence——如果 6 types 均匀分布（各 50 pairs = 16.7%），chance agreement ≈ 16.7%，κ ≈ 0.95，非常高。但如果标注者存在某种系统性偏向特定 type，κ 可能更低。论文应补充报告。

**Q4（cross-provider ICC）**：§4.5 报告 ICC = 0.919 但限于 OpenAI family。Cross-provider ICC 对于 C1 的 robustness 声明至关重要——如果 cross-provider 可重复性显著低于 within-family，C1 的泛化性需要重新评估。

---

## 与我自己审稿意见的交叉总结

R1（方法严谨性）和我（新颖性与完整性）的审稿意见在以下三个核心问题上高度一致：

1. **Incompleteness confound**（R1-W2 ↔ 我的 N1/W1）：均认为 incompleteness 的信息添加混淆未完全解决，且 headline effect 的 framing 不够审慎
2. **Authorization scope measurement reliability**（R1-W1 ↔ 我的 N2）：均认为 κ = 0.385 的低可靠性未在 claims 中得到充分反映
3. **SOPBench replication framing**（R1-W3 ↔ 我的 W2）：均认为 "directional consistency" 的表述过于乐观

R1 独特贡献了两个我未覆盖的重要关切：
- **N1（生态效度）**：合成歧义的极端程度可能导致效应量高估——这是本文最大的外部效度威胁
- **W5（Type III SS 方法论）**：线性概率模型在极端概率下的适用性问题——影响 22.4% headline claim 的精度

两位 Reviewer 的一致评分（3.5 Borderline Conference）反映了共同判断：执行质量高但核心声明需要更审慎的 framing。

---

[Reviewer 1 审稿结果]:
审稿回应已提交给 Review Director。

逐条回应要点概括：
- **N1 (taxonomy 标签)**: 部分同意。承认 "ambiguity" 术语拉伸和 framing 问题，但反对 taxonomy 根本无效——建议提升 confound-free range 可见度而非改标题
- **N2 (C2 robustness)**: 部分反驳。ρ=0.09 的排除有构成性依据（模型组成差异），且三家族验证（Appendix W, ρ=0.71-0.89）提供了独立证据；但同意 "robust extremes" framing 应更突出
- **W1-W5**: 大部分同意，特别是 confound-free range 展示、domain 泛化限制、disambiguation neglect 定位。对 W3 部分反驳（受页数约束但同意 §6.2 需更充分展开）
- 补充指出了 R2 发现的一个精准内部矛盾："behaviorally indistinguishable" 与 §6.1 distinct failure mechanisms 的逻辑冲突

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-23T01:50:11.832239+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-23T01:50:11.983333+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T01:35:47.600884+00:00\", \"completed_at\": \"2026-05-23T01:38:31.976329+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 4-6\", \"message\": \"连续 3 页纯文本（Section 4 Method 到 Section 5.2 Results），无任何 figure/table/equation 穿插，审稿人在此区间缺乏视觉锚点。建议将 Table 2 或 Figure 2/3 中的一个前移至 Results 开头（page 5-6），或在 Method 段增加一个说明实验设计的小图/表\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Table 2 + Figure 2 + Figure 3 三个 display items 挤在同一页，分布极不均匀；Figure 2 和 Figure 3 各占约 1/4 页面，尺寸偏小。建议拆分：将其中一个 figure 移至 page 5-6 的 Results 段落中，缓解 p4-6 的纯文本问题同时释放 page 7 空间\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 axis labels 和 legend 文字字号约为正文 60%，低于推荐的 70% 阈值；Figure 3 同样偏小。如果拆分到不同页面并放大，可读性会显著提升\"}, {\"severity\": \"info\", \"dimension\": \"pages 8-9\", \"message\": \"Error Analysis (§6) 到 Conclusion (§8) 连续 2 页纯文本，虽然讨论/结论章节文字密集属常见，但如果 §6 的 failure mode 分析能配一个小型可视化（如 failure type 分布饼图或混淆矩阵），可同时改善节奏和信息传达\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"主文本仅有 2 个 figure，对于实证为主的论文偏少；variance decomposition (§5.1)、type-specific failure patterns (§6.1)、或 cross-judge agreement (§5) 均有可视化潜力，可增强审稿人的数据感知\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-23T01:50:11.983773+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-23T01:50:12.084508+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-23T01:51:52.024458+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 19 (fresh review)\n\n# ============================================================\n# R19 ISSUES — OPEN\n# ============================================================\n\n- id: \"R19-N1\"\n  summary: \"合成歧义子句的生态效度不足——template-based 生成的歧义可能系统性偏重\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 强烈同意。incompleteness 示例将多个参数替换为模糊词（large/appropriate/timely），程度超出真实政策。SOPBench 效应量衰减至 37% 间接支持此判断。\"\n  action_items:\n    - round: 19\n      action: \"Limitations 中更显著承认效应量可能被高估；或量化合成歧义与真实政策歧义的差异\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-N2\"\n  summary: \"Taxonomy 将非歧义现象（incompleteness/conditional precedence）纳入 ambiguity 标签，标题声明过度概括\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2 首提为 Must-Fix，R1 部分同意 framing 问题但不同意 taxonomy 根本无效。§3 自承 incompleteness/conditional precedence 非 linguistic ambiguity，但标题仍为 Policy Ambiguity Is Nocuous。最强效应 +49.2pp 来自非歧义类型。两人一致指出 behaviorally indistinguishable 与 §6.1 distinct failure mechanisms 存在内部矛盾。\"\n  action_items:\n    - round: 19\n      action: \"方案A：标题改含 underspecification；方案B：confound-free range 提升为 primary result；方案C：加强 §3 inclusive definition 论证并消除与 §6.1 的矛盾\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-N3\"\n  summary: \"Authorization scope κ=0.385 度量不可靠，但相关 claims（C4 most model-differentiating）未充分降级\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 和 R2-N2 均指出。cross-judge-group type ranking ρ=0.09 完全由 auth scope rank reversal 驱动。R1 认为 post-hoc 排除有构成性依据（模型组成差异），R2 认为有 cherry-picking 风险。双方一致认为 Figure 3 caption 和正文 §5.4 应更早标注 auth scope 可靠性问题。\"\n  action_items:\n    - round: 19\n      action: \"Figure 3 caption 标注 auth scope κ 值；§5.4 将 most model-differentiating 改为条件性表述；C2 在 Abstract 中使用 robust extremes 而非 partial ordering\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W1\"\n  summary: \"Confound-free range (+18.7 to +36.0pp) 未出现在 Abstract/Conclusion，headline +34.0pp 包含 confounded incompleteness\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W1 首提，R1 在交叉回应中强烈同意。+34.0pp 在 Abstract/Intro/Conclusion 反复出现但 confound-free range 仅在 §5.1 末尾。\"\n  action_items:\n    - round: 19\n      action: \"Abstract 中 +34.0pp 之后紧跟 confound-free range；Conclusion 同样加入\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W2\"\n  summary: \"SOPBench replication framing 过于乐观——效应量衰减 63%（+12.6 vs +34.0pp），2/5 模型不显著\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W3 首提，R2 同意。directional consistency across all five models 表述有误导性。\"\n  action_items:\n    - round: 19\n      action: \"报告 SOPBench pooled CI；将 confirms directional consistency 改为 suggests；讨论效应量衰减的可能原因\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W3\"\n  summary: \"60.8% 残差方差的实践含义讨论不足——clause-level auditing 仅覆盖 22.4%\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W4 首提，R2 部分同意。论文 largest controllable factor 表述方向正确但不够明确。\"\n  action_items:\n    - round: 19\n      action: \"Discussion 中补充方差分布全景（clause 22.4% + condition 15.8% + model 1.0% vs residual 60.8%），明确 auditing 的上限\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W4\"\n  summary: \"Type III SS 在二元结果上的方差分解（22.4%）作为 headline claim 需方法论补充说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W5 首提，R2 同意。LPM 在极端概率下近似质量差。logistic regression 的 partial R² 未报告。\"\n  action_items:\n    - round: 19\n      action: \"正文中讨论 LPM vs logistic 差异；补充 logistic framework 下 clause identity 的 partial R² 或 deviance explained\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W5\"\n  summary: \"Sections 6-8 过度压缩；disambiguation neglect 的 neglect vs inability 区分和 mitigation 证据在 Appendix 而非主文\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W3/W4 首提，R1 部分反驳（页数约束）但同意 §6.2 需更充分展开。建议将 C3 (inconclusive) 移至 Appendix 释放空间。\"\n  action_items:\n    - round: 19\n      action: \"§6.2 增加 2-3 句概述 mitigation 结果（-8.5pp, auth scope -18.0pp）以支撑 neglect vs inability；考虑将 C3 移至 Appendix\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W6\"\n  summary: \"潜在遗漏相关工作——policy invariance for safety judges、causal impact of tool affordance、specification gaming\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W5 首提，R1 有条件同意。arxiv 2605.06161 关联 cross-judge methodology；arxiv 2603.20320 关联 causal agentic safety；Krakovna et al. specification gaming 与 unintentional misinterpretation 的对比有讨论价值。\"\n  action_items:\n    - round: 19\n      action: \"检查三篇文献并在 Related Work 中适当讨论\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W7\"\n  summary: \"领域泛化性有限——type ranking 跨域不一致（ρ=0.26），auditing 建议适用范围应限定\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W2 首提，R1 同意。Discussion 的 policy auditing 建议暗示超出数据支持的泛化范围。\"\n  action_items:\n    - round: 19\n      action: \"Discussion 中明确 auditing 建议适用于 customer service 及类似领域；C2 type ranking 的 domain-specificity 应在正文而非仅 Limitations 中讨论\"\n      assigned_to: pending\n      status: open\n\n# ============================================================\n# R18 RESOLVED (abbreviated)\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健，需降级为 secondary claim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 完全混淆影响 C4\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"Cross-family judge validation (GPT-4.1, Claude Sonnet 4.6, Gemini 2.5 Pro) on 2997 episodes: Fleiss' κ=0.717\"\n  resolution_round: 18\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足, contribution framing 调整\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n\n- id: \"R18-N4\"\n  summary: \"Disambiguation Neglect 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n\n- id: \"R18-W1\"\n  summary: \"LPM vs logistic specification 说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 再次提出（R19-W4），当前 §5.1 脚注说明不够——需正文级讨论和 logistic partial R²\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页 (~4 行溢出)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"Conclusion on p8, Limitations starts p8 bottom. 18 pages total.\"\n\n# ============================================================\n# HISTORICAL RESOLVED (abbreviated)\n# ============================================================\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"全文 30× → 17× (NMI-based)\"\n  resolution_round: 17\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test (null=8.3%, p<0.001) + GLMM ICC=0.189/0.386\"\n  resolution_round: 17\n\n- id: \"R15F-N1\"\n  summary: \"Intervention-design framework overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"→ diagnostic taxonomy\"\n  resolution_round: 16\n\n- id: \"R15F-N2\"\n  summary: \"Cross-judge ρ=0.09 mid-tier\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"§5.2 limiting statement + partial ordering framing\"\n  resolution_round: 16\n\n- id: \"R14-VC1\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  resolution: \"Maintained ≤8 pages R15-R18\"\n  resolution_round: 18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 19 (fresh review)\n\n# ============================================================\n# R19 ISSUES — OPEN\n# ============================================================\n\n- id: \"R19-N1\"\n  summary: \"合成歧义子句的生态效度不足——template-based 生成的歧义可能系统性偏重\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1 首提，R2 强烈同意。incompleteness 示例将多个参数替换为模糊词（large/appropriate/timely），程度超出真实政策。SOPBench 效应量衰减至 37% 间接支持此判断。\"\n  action_items:\n    - round: 19\n      action: \"Limitations 中更显著承认效应量可能被高估；或量化合成歧义与真实政策歧义的差异\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-N2\"\n  summary: \"Taxonomy 将非歧义现象（incompleteness/conditional precedence）纳入 ambiguity 标签，标题声明过度概括\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2 首提为 Must-Fix，R1 部分同意 framing 问题但不同意 taxonomy 根本无效。§3 自承 incompleteness/conditional precedence 非 linguistic ambiguity，但标题仍为 Policy Ambiguity Is Nocuous。最强效应 +49.2pp 来自非歧义类型。两人一致指出 behaviorally indistinguishable 与 §6.1 distinct failure mechanisms 存在内部矛盾。\"\n  action_items:\n    - round: 19\n      action: \"方案A：标题改含 underspecification；方案B：confound-free range 提升为 primary result；方案C：加强 §3 inclusive definition 论证并消除与 §6.1 的矛盾\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-N3\"\n  summary: \"Authorization scope κ=0.385 度量不可靠，但相关 claims（C4 most model-differentiating）未充分降级\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 和 R2-N2 均指出。cross-judge-group type ranking ρ=0.09 完全由 auth scope rank reversal 驱动。R1 认为 post-hoc 排除有构成性依据（模型组成差异），R2 认为有 cherry-picking 风险。双方一致认为 Figure 3 caption 和正文 §5.4 应更早标注 auth scope 可靠性问题。\"\n  action_items:\n    - round: 19\n      action: \"Figure 3 caption 标注 auth scope κ 值；§5.4 将 most model-differentiating 改为条件性表述；C2 在 Abstract 中使用 robust extremes 而非 partial ordering\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W1\"\n  summary: \"Confound-free range (+18.7 to +36.0pp) 未出现在 Abstract/Conclusion，headline +34.0pp 包含 confounded incompleteness\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W1 首提，R1 在交叉回应中强烈同意。+34.0pp 在 Abstract/Intro/Conclusion 反复出现但 confound-free range 仅在 §5.1 末尾。\"\n  action_items:\n    - round: 19\n      action: \"Abstract 中 +34.0pp 之后紧跟 confound-free range；Conclusion 同样加入\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W2\"\n  summary: \"SOPBench replication framing 过于乐观——效应量衰减 63%（+12.6 vs +34.0pp），2/5 模型不显著\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W3 首提，R2 同意。directional consistency across all five models 表述有误导性。\"\n  action_items:\n    - round: 19\n      action: \"报告 SOPBench pooled CI；将 confirms directional consistency 改为 suggests；讨论效应量衰减的可能原因\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W3\"\n  summary: \"60.8% 残差方差的实践含义讨论不足——clause-level auditing 仅覆盖 22.4%\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W4 首提，R2 部分同意。论文 largest controllable factor 表述方向正确但不够明确。\"\n  action_items:\n    - round: 19\n      action: \"Discussion 中补充方差分布全景（clause 22.4% + condition 15.8% + model 1.0% vs residual 60.8%），明确 auditing 的上限\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W4\"\n  summary: \"Type III SS 在二元结果上的方差分解（22.4%）作为 headline claim 需方法论补充说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W5 首提，R2 同意。LPM 在极端概率下近似质量差。logistic regression 的 partial R² 未报告。\"\n  action_items:\n    - round: 19\n      action: \"正文中讨论 LPM vs logistic 差异；补充 logistic framework 下 clause identity 的 partial R² 或 deviance explained\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W5\"\n  summary: \"Sections 6-8 过度压缩；disambiguation neglect 的 neglect vs inability 区分和 mitigation 证据在 Appendix 而非主文\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W3/W4 首提，R1 部分反驳（页数约束）但同意 §6.2 需更充分展开。建议将 C3 (inconclusive) 移至 Appendix 释放空间。\"\n  action_items:\n    - round: 19\n      action: \"§6.2 增加 2-3 句概述 mitigation 结果（-8.5pp, auth scope -18.0pp）以支撑 neglect vs inability；考虑将 C3 移至 Appendix\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W6\"\n  summary: \"潜在遗漏相关工作——policy invariance for safety judges、causal impact of tool affordance、specification gaming\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W5 首提，R1 有条件同意。arxiv 2605.06161 关联 cross-judge methodology；arxiv 2603.20320 关联 causal agentic safety；Krakovna et al. specification gaming 与 unintentional misinterpretation 的对比有讨论价值。\"\n  action_items:\n    - round: 19\n      action: \"检查三篇文献并在 Related Work 中适当讨论\"\n      assigned_to: pending\n      status: open\n\n- id: \"R19-W7\"\n  summary: \"领域泛化性有限——type ranking 跨域不一致（ρ=0.26），auditing 建议适用范围应限定\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W2 首提，R1 同意。Discussion 的 policy auditing 建议暗示超出数据支持的泛化范围。\"\n  action_items:\n    - round: 19\n      action: \"Discussion 中明确 auditing 建议适用于 customer service 及类似领域；C2 type ranking 的 domain-specificity 应在正文而非仅 Limitations 中讨论\"\n      assigned_to: pending\n      status: open\n\n# ============================================================\n# R18 RESOLVED (abbreviated)\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健，需降级为 secondary claim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 完全混淆影响 C4\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"Cross-family judge validation (GPT-4.1, Claude Sonnet 4.6, Gemini 2.5 Pro) on 2997 episodes: Fleiss' κ=0.717\"\n  resolution_round: 18\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足, contribution framing 调整\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n\n- id: \"R18-N4\"\n  summary: \"Disambiguation Neglect 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n\n- id: \"R18-W1\"\n  summary: \"LPM vs logistic specification 说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19 再次提出（R19-W4），当前 §5.1 脚注说明不够——需正文级讨论和 logistic partial R²\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页 (~4 行溢出)\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"Conclusion on p8, Limitations starts p8 bottom. 18 pages total.\"\n\n# ============================================================\n# HISTORICAL RESOLVED (abbreviated)\n# ============================================================\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"全文 30× → 17× (NMI-based)\"\n  resolution_round: 17\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test (null=8.3%, p<0.001) + GLMM ICC=0.189/0.386\"\n  resolution_round: 17\n\n- id: \"R15F-N1\"\n  summary: \"Intervention-design framework overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"→ diagnostic taxonomy\"\n  resolution_round: 16\n\n- id: \"R15F-N2\"\n  summary: \"Cross-judge ρ=0.09 mid-tier\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"§5.2 limiting statement + partial ordering framing\"\n  resolution_round: 16\n\n- id: \"R14-VC1\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  resolution: \"Maintained ≤8 pages R15-R18\"\n  resolution_round: 18"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-23T01:51:52.075315+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 8797}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-23T01:54:31.898239+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "## 审稿报告 — Round 19 (Fresh Review)\n\n**论文**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**交叉分享**: 完成，关键问题达成共识，无需 Round 2\n\n---\n\n## Summary\n\n本文研究 LLM agent 在含歧义自然语言政策下的安全行为。在 τ²-bench 上构建 300 matched clause pairs（6 种歧义类型），跨 5 个模型生成 ~3,000 episodes。主要发现：(1) 歧义子句使违规率增加 34.0pp（conditional OR=15.1）；(2) 子句措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型预测失败机制的能力是预测违规率的 17 倍（NMI ratio ≈ 17）；(3) incompleteness 是持续最高风险类型（46-62%），coreferential 为下界（31.6%）；(4) disambiguation neglect 普遍存在（≤11% awareness），41.3% 的子句触发跨模型收敛违规。论文配备 perturbation control、cross-judge validation（3 family, Fleiss' κ=0.717）、2 additional replication models 和 SOPBench cross-benchmark 验证。\n\n---\n\n## Strengths\n\n**S1. 严格的匹配对因果设计**\nMatched-pair 设计是建立因果关系的 gold standard。在同一 model-judge pairing 内比较每个 clause 的歧义/非歧义变体，有效控制了 judge bias 和 model baseline。Perturbation control（300 episodes, Δ=-0.67pp, CI containing zero）进一步隔离了语义歧义效应。[R1-S1, R2-S1, 共识]\n\n**S2. 全面且恰当的统计工具箱**\nMcNemar's test、TOST equivalence testing（7 margins sensitivity）、Type III SS 方差分解、permutation test、bootstrap 聚类、logistic regression confound control、ICC replication、Holm-Bonferroni 校正、互信息分析——统计方法选择出色且覆盖全面。[R1-S2, R2-S5, 共识]\n\n**S3. 多层验证架构**\nCross-judge（3 judge 家族, Fleiss' κ=0.717）、human validation（κ=0.798 inter-annotator）、model replication（7 模型跨 6 provider）、cross-benchmark（SOPBench）、perturbation control——多层验证在 NLP 实证研究中不常见。[R1-S3, 共识]\n\n**S4. 诚实且精准的 claim calibration**\nC3 标记为 inconclusive；auth scope cross-judge discordance 完整报告；incompleteness 标注为 confounded upper bound；60.8% 残差方差详细讨论。论文对自身弱点的透明度很高。[R1-S4, R2-S4, 共识]\n\n**S5. \"Type predicts mechanism, not risk\" 的核心洞察**\nNMI 分析（type → mechanism 17× > type → violation rate）将 taxonomy 从 risk predictor 重新定位为 diagnostic tool，既诚实又有实际价值。[R1-S5, R2-S3, 共识]\n\n**S6. Variance decomposition 视角新颖**\n22.4% clause vs 0.4% type 的发现是一个重要的\"负面结果\"——表明 type-level 分类不应用于 risk prediction，真正的风险来源在于 individual clause wording。[R2-S2, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. 合成歧义子句的生态效度不足** [R1-N1, R2 同意]\n300 clause pairs 通过 template-based pipeline 生成。Appendix R 示例显示部分歧义变体更接近\"严重措辞不当\"而非真实世界细微歧义——incompleteness 示例将多个具体参数全部替换为模糊词（\"large\", \"appropriate\", \"timely\"），这种程度在实际政策文档中罕见。Post-hoc realism validation 仅验证词汇风格一致性，未验证歧义程度和分布的自然性；τ²-bench 本身政策也是合成的。SOPBench 效应量衰减至 37%（+12.6 vs +34.0pp）间接支持效应量被高估的判断。这是全文所有 claim 的外部效度基础——如果合成歧义程度系统性偏高，34.0pp 效应量可能高估真实场景影响。\n- **建议**：(1) Limitations 中更显著承认效应量为合成条件下的 upper bound；(2) Discussion/Abstract 中将 +34.0pp 定位为 \"upper bound under controlled synthetic conditions\" 而非部署预期；(3) 未来工作考虑 dose-response 或真实政策对照。\n\n**N2. Taxonomy 将非歧义现象纳入 \"ambiguity\" 标签，标题过度概括** [R2-N1, R1 部分同意]\n§3 明确承认 incompleteness（信息缺失）和 conditional precedence（规范冲突）不属于 linguistic ambiguity，但标题仍为 \"Policy Ambiguity Is Nocuous\"，且最强效应 (+49.2pp) 来自公认的非歧义类型。更关键的是，§3 用 \"behaviorally indistinguishable\" 作为统一归类依据，但 §6.1 恰恰展示了不同 type 有不同 dominant failure mechanisms（structural misparse / gap-filling / boundary violation）——这构成内部矛盾。排除 incompleteness 后 pooled effect 仍为 +31.0pp（Appendix Q），confound-free range 为 +18.7 to +36.0pp，表明 genuine ambiguity 效应仍然显著。\n- **建议**：(1) 标题扩展为包含 underspecification（如 \"Policy Ambiguity and Underspecification...\"）；或 (2) 将 confound-free range 提升为 primary result（R1 倾向此方案）；(3) 消除 \"behaviorally indistinguishable\" 与 §6.1 distinct failure mechanisms 的矛盾——改用 \"produce comparable safety impact\" 的 pragmatic framing。\n\n**N3. Authorization scope 度量不可靠（κ=0.385），但相关 claims 未充分降级** [R1-W1 + R2-N2, 共识]\nAuth scope 的 cross-judge binary κ=0.385 低于 \"fair\" 门槛，是六种类型最低。Cross-judge-group type ranking ρ=0.09（p=0.87）完全由 auth scope rank reversal 驱动。然而 §5.4 仍将其描述为 \"most model-differentiating type (52pp range)\"，Figure 3 caption 未标注可靠性信息。R1 认为 post-hoc 排除 auth scope 有构成性依据（模型组成差异，非 judge bias），且三家族验证（ρ=0.71-0.89）提供独立证据，因此 C2 并非完全不稳健；R2 认为 post-hoc 排除有 cherry-picking 风险。双方一致认为 \"robust extremes only\" 的 framing 应更显著。\n- **建议**：(1) Figure 3 caption 标注 auth scope κ 值；(2) §5.4 \"most model-differentiating\" 改为条件性表述（\"if confirmed by more reliable measurement\"）；(3) Abstract 使用 \"partial ordering with robust extremes\" 而非暗示完整排序。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. Confound-free range 在 Abstract/Conclusion 不可见** [R2-W1 + R1-W2, 共识]\n+34.0pp（含 confounded incompleteness）在 Abstract、Introduction、Conclusion 反复出现，但 confound-free range（+18.7 to +36.0pp）仅在 §5.1 末尾。读者极可能只记住 +34.0pp 而忽略 confound caveat。\n- **建议**：Abstract 中 \"+34.0 percentage points\" 之后立即加入 confound-free range。\n\n**W2. SOPBench replication framing 过于乐观** [R1-W3, R2 同意]\n效应量衰减 63%（+12.6 vs +34.0pp），5 模型中仅 3 个 p<0.01（GPT-5.4 borderline p=0.052, DeepSeek 不显著 p=0.163）。\"Directional consistency across all five models\" 的表述过于宽泛。\n- **建议**：报告 pooled CI；将 \"confirms\" 改为 \"suggests\"；说明 2/5 不显著。\n\n**W3. 60.8% 残差方差的实践含义讨论不足** [R1-W4, R2 部分同意]\n~46% systematic-but-unmeasured 是最大单一方差成分，但 Discussion 对此仅一句带过。Clause-level auditing 仅覆盖 22.4%——是可操作最大因素但非最大因素。\n- **建议**：Discussion 补充方差分布全景图；明确 auditing 的上限。\n\n**W4. Type III SS 方法论需正文级说明** [R1-W5, R2 同意]\n22.4% 来自 Type III SS on binary outcomes（LPM 近似），在 unambiguous 6.9% violation rate 下近似质量较差。Logistic regression Tjur's R²=0.175 作为对照在脚注中提及，但未报告 clause identity 的 partial R²。\n- **建议**：正文讨论 LPM vs logistic 差异；补充 logistic partial R²；确认 clause >> type ordering 在两种 framework 下一致。\n\n**W5. §6 Error Analysis / Disambiguation neglect 的 novelty 未充分展开** [R2-W3+W4, R1 部分同意]\nError Analysis 是三个 contribution 之一但每个 failure mechanism 仅 1-2 句。Disambiguation neglect 的 \"neglect vs inability\" 关键区分仅一句，mitigation 证据（-8.5pp）完全在 Appendix B。Liu et al. (2023) / Hu et al. (2025) 已证明 ambiguity collapse，本文的增量 novelty（agentic context + irreversible consequences）阐述不清。\n- **建议**：§6.2 增加 2-3 句概述 mitigation 结果以支撑 \"neglect\" 定性；考虑将 C3（inconclusive）移至 Appendix 释放空间。\n\n**W6. 潜在遗漏相关工作** [R2-W5, R1 有条件同意]\n(a) \"Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges\" (arxiv 2605.06161) 关联 cross-judge methodology；(b) \"The Causal Impact of Tool Affordance on Safety Alignment\" (arxiv 2603.20320) 关联因果分析框架；(c) Specification gaming 文献（Krakovna et al.）与 unintentional misinterpretation 的对比有讨论价值。\n- **建议**：检查并在 Related Work 中适当讨论。\n\n**W7. 领域泛化性有限但 Discussion 建议暗示更广适用性** [R2-W2, R1 同意]\nRetail vs airline type ranking ρ=0.26，conditional precedence 跨域差异 22pp。Discussion 的 \"clause-level auditing\" 建议暗示超出数据支持的泛化范围。\n- **建议**：Discussion 明确 auditing 建议适用于 customer service 及类似领域。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识 [AGREE]：\n1. **Ecological validity** 是最大外部效度威胁——合成歧义可能系统性偏重，+34.0pp 可能高估真实场景效应\n2. **Confound-free range** 必须在 Abstract/Conclusion 更显著——当前 framing 使读者忽略 incompleteness confound\n3. **Auth scope κ=0.385** 的 claims 需在正文和图表中更早、更显著地降级\n4. **SOPBench \"directional consistency\"** 表述过于宽泛——2/5 模型不显著\n5. **\"Behaviorally indistinguishable\" 与 §6.1 distinct failure mechanisms** 存在内部矛盾——需统一论证\n6. **Type III SS 22.4%** 需要 logistic framework 对照以确认 robustness\n\n## Reviewer Divergence\n\n**N3/R2-N2 (C2 robustness)**：轻度分歧。R1 认为 post-hoc 排除 auth scope 有构成性依据（模型组成差异而非 judge bias），且三家族验证（ρ=0.71-0.89）提供独立证据，因此 C2 \"robust extremes\" 仍有效；R2 认为 post-hoc 排除有 cherry-picking 风险，C2 作为 primary contribution 价值被削弱。双方均同意 \"robust extremes only\" 的 framing 应更突出。分歧在程度而非方向。\n\n---\n\n## Questions for Authors\n\n1. 生成 clause pairs 的 template-based pipeline 具体如何操作？每种类型有多少个 template？是否存在某些 template 贡献了不成比例的违规率？\n2. 96% initial annotator agreement (287/300) 的 chance-corrected Cohen's κ 是多少？\n3. 排除 incompleteness 后五种 type 的 pooled effect size CI？（Appendix Q 报告了 Δ=+31.0pp 但未见 CI）\n4. Mitigation 对 incompleteness 几乎无效（-3.3pp vs auth scope -18.0pp），这是否独立证据说明 incompleteness 与 ambiguity 的本质不同——前者需 policy revision 而非 prompt 可解？\n5. Temperature=0 下的 disambiguation neglect 是否在 temperature>0 部署环境中发生变化？\n6. 是否有 cross-provider ICC 数据？（当前 ICC=0.919 限于 OpenAI family）\n7. 300 clause pairs 均匀分配（每 type 50 pairs）——真实 policy 中各 type 的自然分布？\n\n---\n\n## Missing References\n\n- \"Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges\" (arxiv 2605.06161, May 2026)——关联 cross-judge methodology 和 policy wording 对 judge 行为的影响\n- \"The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents\" (arxiv 2603.20320, March 2026)——方法论可比的因果 agentic safety 研究，需精确定位 \"first causal study\" 声明范围\n- Krakovna et al. specification gaming 文献——与 unintentional misinterpretation 的对比\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warning + 3 info，无 critical）：\n\n- **[Warning] Pages 4-6**：连续 3 页纯文本（§4 Method 到 §5.2 Results），无 figure/table/equation 穿插，审稿人缺乏视觉锚点。建议将 Table 2 或 Figure 2/3 前移至 Results 开头。\n- **[Warning] Page 7**：Table 2 + Figure 2 + Figure 3 三个 display items 挤在同一页，分布极不均匀。建议拆分其中一个 figure 至 page 5-6。\n- **[Info]** Figure 2/3 的 axis labels 和 legend 字号约为正文 60%，低于推荐的 70% 阈值。\n- **[Info]** Pages 8-9 连续纯文本（§6-§8），§6 failure mode 分析可配小型可视化。\n- **[Info]** 主文本仅 2 个 figure，对实证论文偏少；variance decomposition、type-specific failures、cross-judge agreement 均有可视化潜力。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 3.5/5 | 3.5-4/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n\n这是一篇执行质量很高的实证研究。Matched-pair 因果设计、多层验证架构、全面的 sensitivity analysis 和诚实的 claim calibration 体现了很高的方法论标准。核心发现（ambiguity causes violations, clause > type for risk, type > clause for mechanism）在实验范围内可信。\n\n主要顾虑集中在三个方面：(1) **外部效度**——合成歧义的生态效度不足，效应量可能高估真实场景影响；(2) **术语/framing**——将非歧义现象纳入 \"ambiguity\" 标签导致标题和核心声明过度概括，且与 §6.1 的 distinct failure mechanisms 存在内部矛盾；(3) **度量稳健性**——auth scope κ=0.385 和 cross-judge type ranking ρ=0.09 削弱 type-level claims。\n\n如果能解决 N1（加强 ecological validity 论证或更审慎定位效应量）、N2（调整 framing/标题以消除内部矛盾）和 N3（auth scope claims 充分降级），本文有潜力达到 Conference 水平（4.0）。当前版本在 Borderline Conference (3.5) 的高端——方法论贡献突出但 novelty（核心发现 \"ambiguity is bad\" 较为预期）和外部效度不足限制了整体评价。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Opening vignette 有效但 gap statement \"no existing study provides a causal, type-granularity mapping from ambiguity to safety violations\" 需验证是否有 arxiv 2603.20320 等 concurrent causal studies\n- Contribution list 中 \"first matched-pair causal study\" 需限定范围（\"of policy ambiguity's safety impact\"）\n\n### §3 Taxonomy\n- \"Behaviorally indistinguishable\" 需修改为更精确的 pragmatic framing——当前与 §6.1 矛盾\n- 6 type 的选择标准（\"based on frequency in operational policy documents and theoretical distinctiveness\"）过于简略，建议补充每个 type 的选择理由\n\n### §4 Method\n- 96% annotator agreement 应补充 chance-corrected κ\n- Template-based pipeline 细节不足——是否存在 template 效应需要讨论\n\n### §5 Results\n- Abstract 和 §5.1 开头应紧跟 confound-free range\n- C2 在 Abstract 中应使用 \"robust extremes\" 而非暗示完整排序\n- C3 (inconclusive) 可移至 Appendix 释放正文空间\n- SOPBench replication 需更审慎表述\n\n### §6 Error Analysis\n- §6.2 Disambiguation neglect 需增加 mitigation 结果概述以支撑 \"neglect vs inability\"\n- §6.1 failure mechanisms 各仅 1-2 句，信息密度可接受但不充分\n\n### §7 Discussion\n- \"Clause-level auditing targets the largest controllable factor\" 应补充方差全景\n- Auditing 建议应明确限定 domain 范围\n\n### §8 Conclusion\n- 补充 confound-free range\n- 泛化声明已 domain-qualified（\"customer-service and similar\"），这是好的\n\n### Limitations\n- 四段覆盖 Scope、Measurement、Confounds、Disambiguation channel，结构合理\n- 应更显著承认合成歧义的 effect size transportability 问题\n\n### Appendix\n- Appendix R (clause examples) 的极端歧义问题应在正文 Limitations 中讨论\n- Detection experiment (Appendix D) 与主论文因果分析关系较弱，但作为 application spin-off 可保留\n- Appendix Q (sans incompleteness) 的 +31.0pp 结果应在正文 §5.1 中引用",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "## 审稿报告 — Round 19 (Fresh Review)\n\n**论文**: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**交叉分享**: 完成，关键问题达成共识，无需 Round 2\n\n---\n\n## Summary\n\n本文研究 LLM agent 在含歧义自然语言政策下的安全行为。在 τ²-bench 上构建 300 matched clause pairs（6 种歧义类型），跨 5 个模型生成 ~3,000 episodes。主要发现：(1) 歧义子句使违规率增加 34.0pp（conditional OR=15.1）；(2) 子句措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型预测失败机制的能力是预测违规率的 17 倍（NMI ratio ≈ 17）；(3) incompleteness 是持续最高风险类型（46-62%），coreferential 为下界（31.6%）；(4) disambiguation neglect 普遍存在（≤11% awareness），41.3% 的子句触发跨模型收敛违规。论文配备 perturbation control、cross-judge validation（3 family, Fleiss' κ=0.717）、2 additional replication models 和 SOPBench cross-benchmark 验证。\n\n---\n\n## Strengths\n\n**S1. 严格的匹配对因果设计**\nMatched-pair 设计是建立因果关系的 gold standard。在同一 model-judge pairing 内比较每个 clause 的歧义/非歧义变体，有效控制了 judge bias 和 model baseline。Perturbation control（300 episodes, Δ=-0.67pp, CI containing zero）进一步隔离了语义歧义效应。[R1-S1, R2-S1, 共识]\n\n**S2. 全面且恰当的统计工具箱**\nMcNemar's test、TOST equivalence testing（7 margins sensitivity）、Type III SS 方差分解、permutation test、bootstrap 聚类、logistic regression confound control、ICC replication、Holm-Bonferroni 校正、互信息分析——统计方法选择出色且覆盖全面。[R1-S2, R2-S5, 共识]\n\n**S3. 多层验证架构**\nCross-judge（3 judge 家族, Fleiss' κ=0.717）、human validation（κ=0.798 inter-annotator）、model replication（7 模型跨 6 provider）、cross-benchmark（SOPBench）、perturbation control——多层验证在 NLP 实证研究中不常见。[R1-S3, 共识]\n\n**S4. 诚实且精准的 claim calibration**\nC3 标记为 inconclusive；auth scope cross-judge discordance 完整报告；incompleteness 标注为 confounded upper bound；60.8% 残差方差详细讨论。论文对自身弱点的透明度很高。[R1-S4, R2-S4, 共识]\n\n**S5. \"Type predicts mechanism, not risk\" 的核心洞察**\nNMI 分析（type → mechanism 17× > type → violation rate）将 taxonomy 从 risk predictor 重新定位为 diagnostic tool，既诚实又有实际价值。[R1-S5, R2-S3, 共识]\n\n**S6. Variance decomposition 视角新颖**\n22.4% clause vs 0.4% type 的发现是一个重要的\"负面结果\"——表明 type-level 分类不应用于 risk prediction，真正的风险来源在于 individual clause wording。[R2-S2, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. 合成歧义子句的生态效度不足** [R1-N1, R2 同意]\n300 clause pairs 通过 template-based pipeline 生成。Appendix R 示例显示部分歧义变体更接近\"严重措辞不当\"而非真实世界细微歧义——incompleteness 示例将多个具体参数全部替换为模糊词（\"large\", \"appropriate\", \"timely\"），这种程度在实际政策文档中罕见。Post-hoc realism validation 仅验证词汇风格一致性，未验证歧义程度和分布的自然性；τ²-bench 本身政策也是合成的。SOPBench 效应量衰减至 37%（+12.6 vs +34.0pp）间接支持效应量被高估的判断。这是全文所有 claim 的外部效度基础——如果合成歧义程度系统性偏高，34.0pp 效应量可能高估真实场景影响。\n- **建议**：(1) Limitations 中更显著承认效应量为合成条件下的 upper bound；(2) Discussion/Abstract 中将 +34.0pp 定位为 \"upper bound under controlled synthetic conditions\" 而非部署预期；(3) 未来工作考虑 dose-response 或真实政策对照。\n\n**N2. Taxonomy 将非歧义现象纳入 \"ambiguity\" 标签，标题过度概括** [R2-N1, R1 部分同意]\n§3 明确承认 incompleteness（信息缺失）和 conditional precedence（规范冲突）不属于 linguistic ambiguity，但标题仍为 \"Policy Ambiguity Is Nocuous\"，且最强效应 (+49.2pp) 来自公认的非歧义类型。更关键的是，§3 用 \"behaviorally indistinguishable\" 作为统一归类依据，但 §6.1 恰恰展示了不同 type 有不同 dominant failure mechanisms（structural misparse / gap-filling / boundary violation）——这构成内部矛盾。排除 incompleteness 后 pooled effect 仍为 +31.0pp（Appendix Q），confound-free range 为 +18.7 to +36.0pp，表明 genuine ambiguity 效应仍然显著。\n- **建议**：(1) 标题扩展为包含 underspecification（如 \"Policy Ambiguity and Underspecification...\"）；或 (2) 将 confound-free range 提升为 primary result（R1 倾向此方案）；(3) 消除 \"behaviorally indistinguishable\" 与 §6.1 distinct failure mechanisms 的矛盾——改用 \"produce comparable safety impact\" 的 pragmatic framing。\n\n**N3. Authorization scope 度量不可靠（κ=0.385），但相关 claims 未充分降级** [R1-W1 + R2-N2, 共识]\nAuth scope 的 cross-judge binary κ=0.385 低于 \"fair\" 门槛，是六种类型最低。Cross-judge-group type ranking ρ=0.09（p=0.87）完全由 auth scope rank reversal 驱动。然而 §5.4 仍将其描述为 \"most model-differentiating type (52pp range)\"，Figure 3 caption 未标注可靠性信息。R1 认为 post-hoc 排除 auth scope 有构成性依据（模型组成差异，非 judge bias），且三家族验证（ρ=0.71-0.89）提供独立证据，因此 C2 并非完全不稳健；R2 认为 post-hoc 排除有 cherry-picking 风险。双方一致认为 \"robust extremes only\" 的 framing 应更显著。\n- **建议**：(1) Figure 3 caption 标注 auth scope κ 值；(2) §5.4 \"most model-differentiating\" 改为条件性表述（\"if confirmed by more reliable measurement\"）；(3) Abstract 使用 \"partial ordering with robust extremes\" 而非暗示完整排序。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. Confound-free range 在 Abstract/Conclusion 不可见** [R2-W1 + R1-W2, 共识]\n+34.0pp（含 confounded incompleteness）在 Abstract、Introduction、Conclusion 反复出现，但 confound-free range（+18.7 to +36.0pp）仅在 §5.1 末尾。读者极可能只记住 +34.0pp 而忽略 confound caveat。\n- **建议**：Abstract 中 \"+34.0 percentage points\" 之后立即加入 confound-free range。\n\n**W2. SOPBench replication framing 过于乐观** [R1-W3, R2 同意]\n效应量衰减 63%（+12.6 vs +34.0pp），5 模型中仅 3 个 p<0.01（GPT-5.4 borderline p=0.052, DeepSeek 不显著 p=0.163）。\"Directional consistency across all five models\" 的表述过于宽泛。\n- **建议**：报告 pooled CI；将 \"confirms\" 改为 \"suggests\"；说明 2/5 不显著。\n\n**W3. 60.8% 残差方差的实践含义讨论不足** [R1-W4, R2 部分同意]\n~46% systematic-but-unmeasured 是最大单一方差成分，但 Discussion 对此仅一句带过。Clause-level auditing 仅覆盖 22.4%——是可操作最大因素但非最大因素。\n- **建议**：Discussion 补充方差分布全景图；明确 auditing 的上限。\n\n**W4. Type III SS 方法论需正文级说明** [R1-W5, R2 同意]\n22.4% 来自 Type III SS on binary outcomes（LPM 近似），在 unambiguous 6.9% violation rate 下近似质量较差。Logistic regression Tjur's R²=0.175 作为对照在脚注中提及，但未报告 clause identity 的 partial R²。\n- **建议**：正文讨论 LPM vs logistic 差异；补充 logistic partial R²；确认 clause >> type ordering 在两种 framework 下一致。\n\n**W5. §6 Error Analysis / Disambiguation neglect 的 novelty 未充分展开** [R2-W3+W4, R1 部分同意]\nError Analysis 是三个 contribution 之一但每个 failure mechanism 仅 1-2 句。Disambiguation neglect 的 \"neglect vs inability\" 关键区分仅一句，mitigation 证据（-8.5pp）完全在 Appendix B。Liu et al. (2023) / Hu et al. (2025) 已证明 ambiguity collapse，本文的增量 novelty（agentic context + irreversible consequences）阐述不清。\n- **建议**：§6.2 增加 2-3 句概述 mitigation 结果以支撑 \"neglect\" 定性；考虑将 C3（inconclusive）移至 Appendix 释放空间。\n\n**W6. 潜在遗漏相关工作** [R2-W5, R1 有条件同意]\n(a) \"Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges\" (arxiv 2605.06161) 关联 cross-judge methodology；(b) \"The Causal Impact of Tool Affordance on Safety Alignment\" (arxiv 2603.20320) 关联因果分析框架；(c) Specification gaming 文献（Krakovna et al.）与 unintentional misinterpretation 的对比有讨论价值。\n- **建议**：检查并在 Related Work 中适当讨论。\n\n**W7. 领域泛化性有限但 Discussion 建议暗示更广适用性** [R2-W2, R1 同意]\nRetail vs airline type ranking ρ=0.26，conditional precedence 跨域差异 22pp。Discussion 的 \"clause-level auditing\" 建议暗示超出数据支持的泛化范围。\n- **建议**：Discussion 明确 auditing 建议适用于 customer service 及类似领域。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识 [AGREE]：\n1. **Ecological validity** 是最大外部效度威胁——合成歧义可能系统性偏重，+34.0pp 可能高估真实场景效应\n2. **Confound-free range** 必须在 Abstract/Conclusion 更显著——当前 framing 使读者忽略 incompleteness confound\n3. **Auth scope κ=0.385** 的 claims 需在正文和图表中更早、更显著地降级\n4. **SOPBench \"directional consistency\"** 表述过于宽泛——2/5 模型不显著\n5. **\"Behaviorally indistinguishable\" 与 §6.1 distinct failure mechanisms** 存在内部矛盾——需统一论证\n6. **Type III SS 22.4%** 需要 logistic framework 对照以确认 robustness\n\n## Reviewer Divergence\n\n**N3/R2-N2 (C2 robustness)**：轻度分歧。R1 认为 post-hoc 排除 auth scope 有构成性依据（模型组成差异而非 judge bias），且三家族验证（ρ=0.71-0.89）提供独立证据，因此 C2 \"robust extremes\" 仍有效；R2 认为 post-hoc 排除有 cherry-picking 风险，C2 作为 primary contribution 价值被削弱。双方均同意 \"robust extremes only\" 的 framing 应更突出。分歧在程度而非方向。\n\n---\n\n## Questions for Authors\n\n1. 生成 clause pairs 的 template-based pipeline 具体如何操作？每种类型有多少个 template？是否存在某些 template 贡献了不成比例的违规率？\n2. 96% initial annotator agreement (287/300) 的 chance-corrected Cohen's κ 是多少？\n3. 排除 incompleteness 后五种 type 的 pooled effect size CI？（Appendix Q 报告了 Δ=+31.0pp 但未见 CI）\n4. Mitigation 对 incompleteness 几乎无效（-3.3pp vs auth scope -18.0pp），这是否独立证据说明 incompleteness 与 ambiguity 的本质不同——前者需 policy revision 而非 prompt 可解？\n5. Temperature=0 下的 disambiguation neglect 是否在 temperature>0 部署环境中发生变化？\n6. 是否有 cross-provider ICC 数据？（当前 ICC=0.919 限于 OpenAI family）\n7. 300 clause pairs 均匀分配（每 type 50 pairs）——真实 policy 中各 type 的自然分布？\n\n---\n\n## Missing References\n\n- \"Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges\" (arxiv 2605.06161, May 2026)——关联 cross-judge methodology 和 policy wording 对 judge 行为的影响\n- \"The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents\" (arxiv 2603.20320, March 2026)——方法论可比的因果 agentic safety 研究，需精确定位 \"first causal study\" 声明范围\n- Krakovna et al. specification gaming 文献——与 unintentional misinterpretation 的对比\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warning + 3 info，无 critical）：\n\n- **[Warning] Pages 4-6**：连续 3 页纯文本（§4 Method 到 §5.2 Results），无 figure/table/equation 穿插，审稿人缺乏视觉锚点。建议将 Table 2 或 Figure 2/3 前移至 Results 开头。\n- **[Warning] Page 7**：Table 2 + Figure 2 + Figure 3 三个 display items 挤在同一页，分布极不均匀。建议拆分其中一个 figure 至 page 5-6。\n- **[Info]** Figure 2/3 的 axis labels 和 legend 字号约为正文 60%，低于推荐的 70% 阈值。\n- **[Info]** Pages 8-9 连续纯文本（§6-§8），§6 failure mode 分析可配小型可视化。\n- **[Info]** 主文本仅 2 个 figure，对实证论文偏少；variance decomposition、type-specific failures、cross-judge agreement 均有可视化潜力。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 3.5/5 | 3.5-4/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n\n这是一篇执行质量很高的实证研究。Matched-pair 因果设计、多层验证架构、全面的 sensitivity analysis 和诚实的 claim calibration 体现了很高的方法论标准。核心发现（ambiguity causes violations, clause > type for risk, type > clause for mechanism）在实验范围内可信。\n\n主要顾虑集中在三个方面：(1) **外部效度**——合成歧义的生态效度不足，效应量可能高估真实场景影响；(2) **术语/framing**——将非歧义现象纳入 \"ambiguity\" 标签导致标题和核心声明过度概括，且与 §6.1 的 distinct failure mechanisms 存在内部矛盾；(3) **度量稳健性**——auth scope κ=0.385 和 cross-judge type ranking ρ=0.09 削弱 type-level claims。\n\n如果能解决 N1（加强 ecological validity 论证或更审慎定位效应量）、N2（调整 framing/标题以消除内部矛盾）和 N3（auth scope claims 充分降级），本文有潜力达到 Conference 水平（4.0）。当前版本在 Borderline Conference (3.5) 的高端——方法论贡献突出但 novelty（核心发现 \"ambiguity is bad\" 较为预期）和外部效度不足限制了整体评价。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Opening vignette 有效但 gap statement \"no existing study provides a causal, type-granularity mapping from ambiguity to safety violations\" 需验证是否有 arxiv 2603.20320 等 concurrent causal studies\n- Contribution list 中 \"first matched-pair causal study\" 需限定范围（\"of policy ambiguity's safety impact\"）\n\n### §3 Taxonomy\n- \"Behaviorally indistinguishable\" 需修改为更精确的 pragmatic framing——当前与 §6.1 矛盾\n- 6 type 的选择标准（\"based on frequency in operational policy documents and theoretical distinctiveness\"）过于简略，建议补充每个 type 的选择理由\n\n### §4 Method\n- 96% annotator agreement 应补充 chance-corrected κ\n- Template-based pipeline 细节不足——是否存在 template 效应需要讨论\n\n### §5 Results\n- Abstract 和 §5.1 开头应紧跟 confound-free range\n- C2 在 Abstract 中应使用 \"robust extremes\" 而非暗示完整排序\n- C3 (inconclusive) 可移至 Appendix 释放正文空间\n- SOPBench replication 需更审慎表述\n\n### §6 Error Analysis\n- §6.2 Disambiguation neglect 需增加 mitigation 结果概述以支撑 \"neglect vs inability\"\n- §6.1 failure mechanisms 各仅 1-2 句，信息密度可接受但不充分\n\n### §7 Discussion\n- \"Clause-level auditing targets the largest controllable factor\" 应补充方差全景\n- Auditing 建议应明确限定 domain 范围\n\n### §8 Conclusion\n- 补充 confound-free range\n- 泛化声明已 domain-qualified（\"customer-service and similar\"），这是好的\n\n### Limitations\n- 四段覆盖 Scope、Measurement、Confounds、Disambiguation channel，结构合理\n- 应更显著承认合成歧义的 effect size transportability 问题\n\n### Appendix\n- Appendix R (clause examples) 的极端歧义问题应在正文 Limitations 中讨论\n- Detection experiment (Appendix D) 与主论文因果分析关系较弱，但作为 application spin-off 可保留\n- Appendix Q (sans incompleteness) 的 +31.0pp 结果应在正文 §5.1 中引用",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-23T01:54:35.981511+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4083
}
```

</details>

---


### Assistant

_source line 1660 · 2026-05-23T01:54:53.742097+00:00_

**Round 19 审稿完成。**

报告已投递至 Research Director。评分 **3.5 (Borderline Conference)**。

核心发现汇总：

**3 个 Must-Fix：**
- **N1** 合成歧义子句的生态效度不足——template-based 生成的歧义可能系统性偏重，+34.0pp 效应量可能高估真实场景
- **N2** Taxonomy 将 incompleteness/conditional precedence（论文自承非 linguistic ambiguity）纳入 "ambiguity" 标签，标题过度概括，且 "behaviorally indistinguishable" 与 §6.1 distinct failure mechanisms 存在内部矛盾
- **N3** Auth scope κ=0.385 度量不可靠但 C4 claims 未充分降级；cross-judge type ranking ρ=0.09 削弱 C2

**7 个 Should-Fix：** confound-free range 不可见 (W1)、SOPBench framing 过于乐观 (W2)、残差方差讨论不足 (W3)、Type III SS 方法论 (W4)、§6 压缩 / disambiguation neglect 展开 (W5)、遗漏相关工作 (W6)、domain 泛化 (W7)

**共识判断**：执行质量高但核心声明需更审慎 framing。若解决 N1-N3 有潜力达到 Conference (4.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 1661 · 2026-05-23T01:54:56.291153+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 6 个问题全部标注 [AGREE]，核心共识集中在三个问题上：incompleteness confound framing 不够审慎、authorization scope 度量可靠性未充分降级、SOPBench replication 表述过于乐观。R1 额外贡献了生态效度和 Type III SS 方法论两个我未覆盖的重要关切。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1662 · 2026-05-23T01:55:09.635521+00:00_

审稿报告已投递至 Research Director。

**Round 19 审稿总结**：

- **Overall**: 3.5 (Borderline Conference)，R1 和 R2 一致
- **3 个 Must-Fix**：(1) 合成歧义子句生态效度不足，效应量可能高估；(2) Taxonomy 将非歧义现象纳入 "ambiguity" 标签，标题过度概括且与 §6.1 存在内部矛盾；(3) Auth scope κ=0.385 的 claims 未充分降级
- **7 个 Should-Fix**：confound-free range 不可见、SOPBench framing 过于乐观、残差方差实践含义、Type III SS 方法论、§6 压缩、遗漏相关工作、领域泛化
- **视觉审查**：2 warning（pages 4-6 纯文本无视觉锚点、page 7 display items 堆积）
- **外部审稿**：未启用
- **Issue Tracker**：已同步 10 个新 issue（3 critical + 7 warning）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 163

## Round 163

68 recorded events


### User

_source line 1663 · 2026-05-23T02:30:08.328084+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May cycle)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-23T02:30:13.559505+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-23T02:30:13.610702+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1666 · 2026-05-23T02:30:22.595820+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1667 · 2026-05-23T02:30:22.646368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-23T02:30:25.307866+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-23T02:30:27.366874+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2059
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-23T02:30:27.367420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1671 · 2026-05-23T02:30:27.669007+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-23T02:30:27.669396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1673 · 2026-05-23T02:30:33.541760+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found some information about EMNLP 2026, though the search results primarily contain det
…[truncated 1161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5872
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-23T02:30:36.905721+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 1675 · 2026-05-23T02:30:37.057148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR May 2026 cycle submission deadline guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR May 2026 cycle submission deadline guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 1676 · 2026-05-23T02:30:42.147298+00:00_

Web search results for query: "ARR May 2026 cycle submission deadline guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results, here's information about the ARR May 2026 cycle submission deadline and guidelines regarding page limits:

## Submission Deadline

The submission deadline is always the 15th of the month, which means the ARR May 2026 cycle submission deadline would be May 15, 2026.

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## Additional Guidelines

The ARR 2026 May cycle has a new submission policy for EMNLP: authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

After submission, all authors must complete the author registration form within 48h of the deadline.

For more comprehensive guidelines on 
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5090
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-23T02:30:43.202508+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the information about EMNLP 2026 main conference call for papers submission deadline in the ARR cycle:

## Key Submission Deadline

The ARR
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6296
}
```

</details>

---


### Tool call

_source line 1678 · 2026-05-23T02:30:46.465228+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1679 · 2026-05-23T02:30:46.717019+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 author guidelines formatting anonymity requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 author guidelines formatting anonymity requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool result

_source line 1680 · 2026-05-23T02:30:51.083911+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers formatting requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Ten Simple Rules for writing algorithmic bioinformatics conference papers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7117650/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"}]

Based on the search results, I found information about the EMNLP 2026 Call for Main Conference Papers. However, the search results show general information about the conference's paper submission policies rather than specific formatting requirements for the main conference papers.

The search results indicate that manuscripts should be submitted electronically in PDF format and formatted using the templates available on the website, and authors should not modify these style files nor use templates designed for other conferences. Additionally, submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be desk-rejected.

Unfortunately, the specific detailed formatting requirements (such as exact margin widths, font sizes, page limits, etc.) for the main conference papers are not included in these search results. For complete formatting specifications, you would need to visit the actual EMNLP 2026 website at https://2026.emnlp.org/calls/main_conference_papers/ and access the template files and detailed guidelines directly.


REMINDER: Y
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 4618
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-23T02:30:58.010275+00:00_

Web search results for query: "ARR 2026 author guidelines formatting anonymity requirements aclrollingreview.org"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's information about ARR 2026 author guidelines regarding formatting, anonymity requirements, and related policies:

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, the new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.

## Formatting Requirements

Paper submissions must use the official ACL style templates, available as an Overleaf template and downloadable via aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. The paper should be desk-rejected if it does not follow the style guides or goes over the page limit (4 pages for short, 8 for long papers, excluding the ethi
…[truncated 498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 11293
}
```

</details>

---


### Tool call

_source line 1682 · 2026-05-23T02:31:04.391456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-23T02:31:05.094603+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points under controlled synthetic conditions (conditional OR $= 15.1$; $+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of violation variance versus 0.4\% for type; however, type predicts failure \emph{mechanism} 17$\times$ more strongly than violation rate, establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect ($\leq$11\% awareness) and \emph{systematic nocuity}: 41.3\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains under synthetic ambiguity injection, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-23T02:31:05.245787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1685 · 2026-05-23T02:31:05.346705+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1686 · 2026-05-23T02:31:05.397439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1687 · 2026-05-23T02:31:06.351893+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 3835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-23T02:31:06.452826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-23T02:31:07.256526+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on frequency in operational policy documents and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by contextual cues within the text.
29	\emph{Scopal} ambiguity involves quantifier, negation, or modal scope interac
…[truncated 2722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-23T02:31:07.257236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-23T02:31:07.610522+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 5456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-23T02:31:07.610992+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "experiment_plan.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-23T02:31:07.711656+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-23T02:31:11.977816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-23T02:31:12.982218+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary claims; C4 is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{We use Type III SS because factor ordering should not affect attribution in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant factor ordering (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}), with clause and type partial effects directionally consistent across linear and logistic specifications.} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\,pp is run-to-run stochasticity and $\sim$46\,pp systematic-but-unmeasured factors; ICC replication in Appendix~\ref{app:residual}). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness
…[truncated 8493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-23T02:31:12.982662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-23T02:31:13.434625+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with two achieving unanimity (scopal and authorization scope).
19	
20	\subsection{Disambiguation Neglect}
21	\label{sec:dn}
22	
23	Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} versus \emph{surface adoption} (proceeding with a single interpretation). Overall awareness is 4.6\% ($\leq$11\% per model); Qwen
…[truncated 1438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-23T02:31:13.435210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-23T02:31:13.937497+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on type, safety training, and disambiguation channel availability. The binary effect is domain-robust (interaction $p = 0.187$) but type rankings are not ($\rho = 0.26$), suggesting nocuity is universal while its type-specific profile requires per-domain calibration. Nevertheless, 60.8\% of variance remains unexplained; of this, $\sim$15\,pp is run-to-run stochasticity and $\sim$46\,pp systematic-but-unmeasured factors such as conversation trajectory (ICC $= 0.749$; Appendix~\ref{app:residual}). In customer-service and similar task-oriented domains, clause-level auditing thus addresses the largest \emph{actionable} component (22.4\%) but not the majority of outcome variance.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} 17$\times$ more strongly than violation rate (NMI ratio $\approx 17$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
9	
10	\paragraph{Prompt-based mitigation.}
11	A mitigation study (Appendix~\ref{app:mitigation}) finds prompting effective for authorization scope ($-18.0$\,pp) and lexical ($-8.9$\,pp) but not incompleteness ($-3.3$\,pp), reinforcing policy-design over prompt-level fixes \citep{chantree_2006,ferrari_ambiguity_2019}.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-23T02:31:13.937844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-23T02:31:14.389814+00:00_

1	\section{Conclusion}
2	
3	Under controlled synthetic conditions, policy ambiguity increases agent violations by 34.0\,pp (OR\,$=$\,15.1; $+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms 17$\times$ better than violation rate. With $>$89\% disambiguation neglect and 41.3\% convergent violations, clause-level auditing is critical for customer-service and similar policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-23T02:31:14.390185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-23T02:31:14.942587+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Ecological validity.} Our ambiguity pairs are synthetically constructed via templates (\S\ref{sec:method}), so the 34.0\,pp effect is an upper bound under controlled conditions; naturally occurring ambiguity in deployed policies may produce smaller effects. The SOPBench replication ($+$12.6\,pp), while directionally consistent, also uses researcher-constructed benchmarks. Neither study measures ambiguity prevalence in real-world policy documents; a dose-response study varying ambiguity density in production policies would help calibrate practical impact.
5	
6	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested. Cross-domain consistency holds for the overall effect (C1, interaction $p = 0.19$) and model ranking ($\rho = 0.90$, $p = 0.037$), but type rankings vary across domains ($\rho = 0.26$, $p = 0.62$); conditional precedence in particular differs by 22\,pp between retail and airline, further motivating the partial-ordering framing. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}); consequently, the confound-free lower bound ($+$18.7\,pp) rests on the primary five-model study alone.
7	
8	\paragraph{Measurement.} A cross-family judge validation (Appendix~\ref{app:cross_judge}) using GPT-4.1, Claude Sonnet~4.6, and Gemini~2.5~Pro on the same 2,997 episodes achieves Fleiss' $\kappa = 0.71
…[truncated 2250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-23T02:31:14.942978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-23T02:31:15.295273+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 37141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-23T02:31:20.714673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "offset": "474"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "offset": "474"
  }
}
```

</details>

---


### Tool result

_source line 1707 · 2026-05-23T02:31:21.568231+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (474). The file has 474 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1708 · 2026-05-23T02:31:21.719209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-23T02:31:22.472572+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 16843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1710 · 2026-05-23T02:31:22.573943+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-23T02:31:22.725300+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1712 · 2026-05-23T02:31:27.544213+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.*\" -o -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.*\" -o -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-23T02:31:28.548567+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/phantompolicy_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/berry_kamsties_2004.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/policybank_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/agentpex_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/drip_r_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/lhaw_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/shieldagent_2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/li_ambiguity_taxonomy_2024.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/chantree_2006.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/massey_ambiguity_re_2014.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/mantra_2026.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/tau2_bench_2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/distill_tmp/agentauditor_2025.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1714 · 2026-05-23T02:31:28.699530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-23T02:31:28.750257+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-23T02:31:36.884352+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1717 · 2026-05-23T02:31:36.934936+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-23T02:31:39.443058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-23T02:31:40.447480+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 19
5	
6	# ============================================================
7	# R19 ISSUES — ALL RESOLVED
8	# ============================================================
9	
10	- id: "R19-N1"
11	  summary: "合成歧义生态效度不足，+34.0pp 可能高估真实场景"
12	  category: framing
13	  severity: critical
14	  status: resolved
15	  first_raised_round: 19
16	  last_seen_round: 19
17	  resolution: "Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'; Limitations 新增 Ecological validity 段; §4.2 补 Cohen's κ=0.95"
18	  resolution_round: 19
19	
20	- id: "R19-N2"
21	  summary: "非歧义纳入 ambiguity 标签 + behaviorally indistinguishable 与 §6.1 矛盾"
22	  category: framing
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 19
26	  last_seen_round: 19
27	  resolution: "§3 改 'produce comparable safety impact despite distinct underlying mechanisms'; §5.1 加 sans-incompleteness +31.0pp [27.9,34.1]"
28	  resolution_round: 19
29	
30	- id: "R19-N3"
31	  summary: "Auth scope κ=0.385 claims 未充分降级"
32	  category: method
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 18
36	  last_seen_round: 19
37	  resolution: "Figure 3 caption 加 κ=0.385 + 'interpret with caution'; §5.4 'most model-differentiating' → 'largest cross-model range' + caution caveat"
38	  resolution_round: 19
39	
40	- id: "R19-W1"
41	  summary: "Confound-free range 在 Abstract/Conclusion 不可见"
42	  category: writing
43	  severity: warning
44	  status: resolved
45	  first_raised_round: 19
46	  last_seen_round: 19
47	  resolution: "Abstract/Conclusion 加 '+18.7 to +36.0pp excluding confounded incompleteness type'"
48	  resolution_round: 19
49	
50	- id: "R19-W2"
51	  summary: "SOPBench framing 过于乐观 (confirms→suggests, 2/5 不显著)"
52	  category: writing
53	  severity: warning
54	  status: resolved
55	  first_rai
…[truncated 4413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1720 · 2026-05-23T02:31:40.949832+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool call

_source line 1721 · 2026-05-23T02:31:41.703246+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/ 2>/dev/null",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/ 2>/dev/null",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 1722 · 2026-05-23T02:31:41.754030+00:00_

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
round_3.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1723 · 2026-05-23T02:31:41.855075+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-23T02:32:24.121547+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1725 · 2026-05-23T02:32:41.355269+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17233
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-23T02:32:41.506345+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "1",
  "round_number": "20",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations 不计页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: 双盲匿名\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点关注以下方面：\n\n1. **实验设计**：matched-pair design 是否真正建立因果关系？300 clause pairs 的生成流程是否有偏？模板生成 + 标注验证是否充分？\n2. **统计分析**：McNemar's test、TOST equivalence testing、Type III SS variance decomposition、permutation test、bootstrap cluster analysis 使用是否正确？SESOI ±15pp 的选择是否有充分理由？多重比较校正是否充分？\n3. **评估 pipeline**：cross-judge design 是否有效控制 self-evaluation bias？GPT-5.4/GPT-4.1 交叉评判是否引入 confound？κ=0.653 binary agreement 是否足够？human validation (κ=0.798) 的 100 样本量是否充分？\n4. **Controls**：perturbation control (n=300) 是否充分排除 surface-level 干扰？incompleteness confound analysis 是否充分？token count 作为 information delta 的 proxy 是否合理？\n5. **可复现性**：ICC=0.919 的 replication、cross-benchmark (SOPBench) replication 是否可信？model expansion (Gemini/LLaMA) 是否充分？\n6. **Claims 校准**：四个 claims (C1-C4) 的证据强度是否与论文表述匹配？是否有 overclaiming？\n\n请逐项给出评价，标注 Must-Fix / Should-Fix / Minor。最后给出你的独立评分（使用 ARR Overall Assessment 1-5 量表）和置信度（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_id": "1",
    "round_number": "20",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations 不计页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: 双盲匿名\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点关注以下方面：\n\n1. **实验设计**：matched-pair design 是否真正建立因果关系？300 clause pairs 的生成流程是否有偏？模板生成 + 标注验证是否充分？\n2. **统计分析**：McNemar's test、TOST equivalence testing、Type III SS variance decomposition、permutation test、bootstrap cluster analysis 使用是否正确？SESOI ±15pp 的选择是否有充分理由？多重比较校正是否充分？\n3. **评估 pipeline**：cross-judge design 是否有效控制 self-evaluation bias？GPT-5.4/GPT-4.1 交叉评判是否引入 confound？κ=0.653 binary agreement 是否足够？human validation (κ=0.798) 的 100 样本量是否充分？\n4. **Controls**：perturbation control (n=300) 是否充分排除 surface-level 干扰？incompleteness confound analysis 是否充分？token count 作为 information delta 的 proxy 是否合理？\n5. **可复现性**：ICC=0.919 的 replication、cross-benchmark (SOPBench) replication 是否可信？model expansion (Gemini/LLaMA) 是否充分？\n6. **Claims 校准**：四个 claims (C1-C4) 的证据强度是否与论文表述匹配？是否有 overclaiming？\n\n请逐项给出评价，标注 Must-Fix / Should-Fix / Minor。最后给出你的独立评分（使用 ARR Overall Assessment 1-5 量表）和置信度（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-23T02:32:53.869380+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12363
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-23T02:32:54.021372+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_id": "2",
  "round_number": "20",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations 不计页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: 双盲匿名\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**——重点关注以下方面：\n\n1. **Contribution 定位**：三个 contribution（因果研究、方差分解+MI分析、error analysis）的新颖性如何？与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等concurrent work 的差异是否清晰？matched-pair causal design 相比 DRIP-R 的 correlational design 是否构成足够的方法论进步？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注 2025-2026 新发表的 agent safety、policy compliance、ambiguity 文献。引用是否真实、完整？bib 条目格式是否规范？\n3. **Framing 校准**：taxonomy 定位为 \"diagnostic tool\" 而非 \"classification standard\" 是否合理？\"disambiguation neglect\" 作为 descriptive label 而非 novel phenomenon 是否恰当？各 claim 的措辞是否与数据匹配？\n4. **写作质量**：逻辑流是否通顺？Abstract/Intro/Conclusion 是否一致？Limitations 是否充分且真诚？Discussion 是否过度推断？是否有 AI 写作痕迹？\n5. **格式合规**：是否满足 ACL 8 页限制？双盲匿名是否到位？Limitations section 是否存在？Ethics statement 情况？引用格式？\n6. **Missing References**：搜索 2025-2026 文献，识别论文可能遗漏的重要 related work。\n\n请逐项给出评价，标注 Must-Fix / Should-Fix / Minor。最后给出你的独立评分（使用 ARR Overall Assessment 1-5 量表）和置信度（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_id": "2",
    "round_number": "20",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations 不计页数\n- **模板**: ACL (acl.sty)\n- **匿名规则**: 双盲匿名\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**——重点关注以下方面：\n\n1. **Contribution 定位**：三个 contribution（因果研究、方差分解+MI分析、error analysis）的新颖性如何？与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等concurrent work 的差异是否清晰？matched-pair causal design 相比 DRIP-R 的 correlational design 是否构成足够的方法论进步？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注 2025-2026 新发表的 agent safety、policy compliance、ambiguity 文献。引用是否真实、完整？bib 条目格式是否规范？\n3. **Framing 校准**：taxonomy 定位为 \"diagnostic tool\" 而非 \"classification standard\" 是否合理？\"disambiguation neglect\" 作为 descriptive label 而非 novel phenomenon 是否恰当？各 claim 的措辞是否与数据匹配？\n4. **写作质量**：逻辑流是否通顺？Abstract/Intro/Conclusion 是否一致？Limitations 是否充分且真诚？Discussion 是否过度推断？是否有 AI 写作痕迹？\n5. **格式合规**：是否满足 ACL 8 页限制？双盲匿名是否到位？Limitations section 是否存在？Ethics statement 情况？引用格式？\n6. **Missing References**：搜索 2025-2026 文献，识别论文可能遗漏的重要 related work。\n\n请逐项给出评价，标注 Must-Fix / Should-Fix / Minor。最后给出你的独立评分（使用 ARR Overall Assessment 1-5 量表）和置信度（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-23T02:32:55.435487+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1414
}
```

</details>

---


### Assistant

_source line 1730 · 2026-05-23T02:33:04.723511+00:00_

Round 20 审稿已启动：

- **Reviewer 1**（方法严谨性）：已派发 ✅
- **Reviewer 2**（新颖性/完整性）：已派发 ✅
- **视觉审查 Agent**：已启动 ✅
- **外部审稿**：未启用（项目未配置 paperreview.ai）

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 164

## Round 164

4 recorded events


### User

_source line 1731 · 2026-05-23T02:37:54.390502+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5 (Quite sure. I tried to check the important points carefully)
**一句话总结**: 方法论设计扎实、统计分析全面、claims 校准诚实，但 SESOI 选择缺乏外部锚定、生态效度受限于纯合成数据、failure mode 编码存在循环性风险，整体处于可接收边界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 核心 claims (C1, C2) 有充分统计支撑和多层 robustness checks；控制设计到位；但 SESOI 选择和 cross-judge 分配的非随机性留有方法论空间 |
| Excitement | 3/5 | 研究问题实际且及时（LLM agent safety），但结果方向性可预期（ambiguity → more violations），taxonomy 的诊断价值是主要新颖点 |
| Reproducibility | 4/5 | 详细方法描述、计划开源代码/数据、ICC=0.919 的重复实验、跨基准复现；但 annotation 流程细节可更充分 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Failure mode taxonomy 与 ambiguity taxonomy 之间的定义循环性

- 具体位置：§6, §6.1, Appendix S (Table S13)
- 问题：论文声称 "type predicts failure mechanism 17× more strongly than violation rate"（NMI ratio ≈ 16.8×, §7 Discussion）。但三种 failure mechanisms（structural misparse, gap-filling, boundary violation）与 ambiguity types 存在 **定义层面的高度重叠**：authorization scope 的 boundary violation 本质上就是 scope 类歧义的直接后果；incompleteness 的 information gap-filling 就是信息缺失的直接表现。这使得高 mutual information 可能部分反映 **分类学定义的重叠**（tautological association）而非独立的经验发现。此外，failure mode 编码使用 LLM 标注 LLM 的失败模式（§6 承认 "introduces circularity risk"），编码者间一致性仅为 Gwet's AC₁ = 0.62 / κ = 0.52（moderate），进一步削弱了 17× claim 的可信度。
- 为什么影响接收：这是 Discussion 和 Abstract 中的核心贡献之一（"establishing the taxonomy as a diagnostic tool"）。如果 type→mechanism 的高关联部分是定义驱动的 artifact，taxonomy 的 "诊断价值" 论证就被严重削弱。
- 建议修改方向：(1) 明确讨论哪些 type→mechanism 关联是定义驱动 vs. 经验发现的，例如 scopal→structural misparse 和 lexical→gap-filling 的关联并不显然是定义蕴含的，可以分别报告 MI；(2) 对 failure mode 编码进行人工验证（至少 subset），提供 human-LLM 编码一致性；(3) 弱化 "17×" 的表述，承认上界受定义重叠影响。

**N2** [critical] SESOI ±15pp 缺乏外部锚定，显著影响 C2 结论

- 具体位置：§4.6, §5.2, Appendix A (Table 3)
- 问题：C2 的 "mid-tier cluster"（auth scope, lexical, scopal, cond. prec. 四类等价）完全依赖 SESOI = ±15pp。论文承认 "no field-standard SESOI exists"，给出的理由是 (a) 超过测量噪声 2×，(b) 运营上 15pp 会触发不同审计策略。但：
  - 在 ±10pp 下，仅 3/6 mid-tier pairs 等价（Table 3），cluster 结构瓦解
  - TOST power 在 ±10pp 仅 0.57，说明在更严格阈值下检验力不足
  - ±15pp 在实际场景中意味着一个 policy type 可以比另一个多产生 15 个百分点的违规而被视为 "等价"——这个操作定义是否合理取决于应用场景，论文未提供任何来自实际部署的校准数据
  - 论文引用 Anvari & Lakens (2021) 承认 margin dependence，但这恰恰说明 C2 的 "partial ordering" 不是 robust 结论而是 parameter-contingent 的
- 为什么影响接收：C2 是四个 claims 中的 primary claim 之一。如果读者采用更保守的 SESOI，C2 的 mid-tier cluster 不成立，论文的 taxonomy 实用性论证被削弱。
- 建议修改方向：(1) 在正文明确展示 ±10pp 下的等价结构（而非仅在 Appendix）；(2) 考虑将 C2 重新表述为 "incompleteness and coreferential form robust extremes; the four intermediate types are margin-dependent"——实际上论文在 §5.2 末尾已经有类似表述，但 abstract 和 introduction 仍使用更强的 "partial ordering" 语言；(3) 提供来自实际 policy 审计实践的 SESOI 参考（如有的话）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-judge 分配非随机化

- 具体位置：§4.4
- 问题：GPT-5.4 评判 Claude/GPT-4.1/Qwen3，GPT-4.1 评判 GPT-5.4/DeepSeek。论文论证 matched-pair design 使 judge bias 在 Δpp 中抵消，但这仅在 judge bias 是 **加性的**（additive）时成立。如果 GPT-5.4 作为 judge 对 ambiguity-induced errors 的敏感度与 GPT-4.1 不同（即 judge × condition 交互效应），则 matched-pair 差异中仍包含 confound。Appendix W 的三家 judge 验证（Fleiss' κ = 0.717）部分缓解了此问题，但该验证仅在 ambiguous-condition 上进行（2,997 episodes），未覆盖 unambiguous condition 的评判一致性。
- 建议：(1) 在 Appendix W 补充 unambiguous-condition 的三家 judge 验证；(2) 至少在一个 subset 上进行 crossed judge 分配（两个 judge 都评判同一组 episodes 的 ambiguous+unambiguous），直接估计 judge × condition 交互效应。

**W2** [warning] Human validation 的 type-level 检验力不足

- 具体位置：§4.4, Appendix G (Table 9)
- 问题：100 episodes 的 human validation 被描述为 "validating the automated pipeline"（§4.4），但 per-type 样本仅 32-34 episodes。部分 type 的 95% CI 极宽：scopal κ CI = [0.00, 1.00]，coreferential κ CI = [0.00, 0.84]。这些区间对 type-level reliability 几乎没有信息量。论文在 Appendix G 承认 "imprecise due to small cell sizes" 并警告不应用于 type-level inference，但正文 §4.4 的表述（"Per-type estimates validate the pipeline overall but lack power for type-level comparison"）可能给读者过于乐观的印象。
- 建议：正文中更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性（κ = 0.733），不支持任何 type-level 的 reliability claim。对 authorization scope（human κ = 0.644）和 coreferential（human κ = 0.479）这两个 type-level 最低的 κ，应讨论其对 C2 和 C4 结论的潜在影响。

**W3** [warning] Perturbation control 的 construct validity

- 具体位置：§4.5
- 问题：300 个 non-ambiguity perturbation（synonym substitution, clause reordering）用于确认特异性，但这些 perturbation 的性质（surface-level rewording）与 ambiguity manipulation 的性质（semantic-level change）不在同一层面。更相关的 control 是 **添加信息但不消除歧义**（information-addition without disambiguation），这将直接 address incompleteness confound。论文使用 token count logistic regression 作为替代（Appendix F），但承认 token count 是 "coarse proxy"。
- 建议：在 limitations 中增加一句，指出 perturbation control 测试的是 surface-level specificity，而 information-addition control 的缺失是未来工作方向。（实际上论文已在 §4.5 有类似表述，但可以更明确。）

**W4** [warning] Variance decomposition 的解释问题

- 具体位置：§5.1
- 问题：Type III SS 分解中，clause identity 占 22.4%（0.4% between types + 22.0% within types），condition 占 15.8%，model 占 1.0%，residual 60.8%。论文在 §7 讨论 "clause-level auditing addresses the largest actionable component (22.4%)" 但这里有两个问题：
  - (a) 22.4% 的 clause identity effect 包含 within-type 变异（clause wording 本身的特异性），这不是通过 type-level auditing 可 actionable 的；只有 type-level auditing 对应的是 0.4% 的 between-type 变异。clause-level auditing 意味着要逐条检查每个 clause，这在实际中可能不可行，但论文未充分讨论这一点。
  - (b) 60.8% 的 residual 被进一步分解为 ~15pp stochastic + ~46pp systematic-but-unmeasured（Appendix X, ICC=0.749），这意味着 conversation trajectory 是最大的变异来源。这对实际 policy 审计的价值有什么含义？
- 建议：在 Discussion 中更清晰地区分 "clause-level auditing"（逐条检查 300 个 clause）和 "type-level auditing"（基于 6 类分类的策略），讨论各自的 actionability。

**W5** [warning] Cross-benchmark replication (SOPBench) 效力偏弱

- 具体位置：§5.1, Appendix U (Table 16)
- 问题：SOPBench replication 的 pooled effect 为 +12.6pp（vs. τ²-bench 的 +34.0pp），且 5 个模型中仅 3 个达到 individual significance（GPT-5.4 p=0.052, DeepSeek p=0.163）。论文归因于三个系统差异（constraint-level vs episode-level, higher baseline rates, task structure differences），这些解释合理但也意味着 τ²-bench 的效应可能不直接推广到其他 benchmark 设计。特别是 SOPBench 的 unambiguous baseline 高达 22.9%（vs τ²-bench 6.9%），暗示 SOPBench 的 task 本身更难，压缩了 ambiguity 的增量效应。
- 建议：在 Limitations 中补充一句，指出 cross-benchmark replication 的 effect size attenuation 可能反映 benchmark 设计差异，也可能反映 ambiguity effect 的 context-dependence。

---

## 小问题（不影响接收）

- **M1**: Abstract 中 "+18.7 to +36.0pp excluding the confounded incompleteness type"——这是 type-level 的 range，但可能被误读为 model-level。建议澄清为 "type-level Δpp ranges from +18.7 to +36.0pp"。
- **M2**: §4.4 报告 McNemar's test for cross-judge calibration (p=0.606) 基于 9 vs 6 的 discordant pairs（n=100 中）。样本量偏小，McNemar's test 的检验力有限。
- **M3**: §5.1 "Clause wording—not type membership—drives clause-level variance" 后跟 "the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity (χ²=28.02, V=0.137)"——这两句的 juxtaposition 可能让读者困惑。建议明确说明 type 解释的变异虽然 statistically significant 但 effect size 很小（V=0.137, 即 ~1.9% of variance）。
- **M4**: §4.2 提到 annotators "independently verified type assignments with a 96% initial agreement (287/300; Cohen's κ = 0.95)"——但这是同一批 annotators 创建和验证 pairs 的，存在 confirmation bias 风险。是否有第三方独立验证？
- **M5**: Appendix D (Detection Experiment) 中 six-class macro F1 = 0.63，其中 incompleteness F1=0.34——这表明 taxonomy 的自动化应用存在挑战，但论文将其定位为 "proof-of-concept"，表述恰当。
- **M6**: Appendix X 报告 authorization scope 的 per-type ICC ≈ 0，这意味着 auth scope 的违规结果几乎完全由 conversation trajectory 决定而非 clause 本身。这与 auth scope 在 C4 中的 prominent role 形成张力——一个 reproducibility 极低的 type 驱动了唯一显著的交互效应。

---

## 主要优势

1. **Matched-pair 因果设计**：在 agent safety 领域属于方法论创新，300 clause pairs 的规模和匹配质量（κ=0.95）可信。
2. **多层 robustness**：perturbation control、cross-judge validation（3 家 judge, Fleiss' κ=0.717）、cross-benchmark replication、model expansion（7 models, 6 providers）——对 C1 的支撑层层递进。
3. **Claims 校准诚实**：C3 标注为 inconclusive, C4 标注为 exploratory；incompleteness confound 被充分讨论；authorization scope 的 reliability 问题被反复提示。这种自我批判性在投稿中难能可贵。
4. **统计方法选择恰当**：McNemar's test for paired binary data、TOST with sensitivity analysis、Holm-Bonferroni within pre-registered families、bootstrap cluster analysis——方法选择与数据结构匹配。
5. **Appendix 深度可圈可点**：19 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑，显示作者对方法论有深入理解。

---

## 总结性评价

本文在 LLM agent safety 领域提出了一个重要且及时的研究问题，experimental design 和 statistical analysis 的质量在该领域属于上乘。核心发现（C1: ambiguity causally increases violations）有充分的多层证据支持。主要方法论弱点在于：(1) failure mode taxonomy 的诊断价值论证存在定义循环风险（N1），(2) C2 的 partial ordering 高度依赖 SESOI 选择（N2），(3) 纯合成数据限制了生态效度。如果 N1 和 N2 能得到妥善处理（重新表述 17× claim、在正文展示多 margin 下的等价结构），本文可以达到 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-23T02:38:01.075378+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-23T02:38:01.126053+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1734 · 2026-05-23T02:38:33.406825+00:00_

收到 Reviewer 1（方法严谨性）的审稿报告。评分 3.5/5 (Borderline Conference)，提出 2 个 Must-Fix（failure mode 定义循环性 N1、SESOI 外部锚定 N2）和 5 个 Should-Fix。

等待 Reviewer 2（新颖性/完整性）的报告返回后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 165

## Round 165

10 recorded events


### User

_source line 1735 · 2026-05-23T02:38:34.483570+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5（Quite sure — 仔细阅读了论文全文、附录及相关文献）
**一句话总结**: 匹配对因果设计是对 DRIP-R 等关联性研究的真正方法论进步，统计执行严谨，但 taxonomy 本身缺乏原创性，生态效度受限于合成歧义注入和客服场景，整体新颖性处于会议接收门槛。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4.0 / 5 | 匹配对设计、perturbation control、cross-judge 三族验证、七模型复现，统计方法论扎实；incompleteness confound 处理透明但未完全消除 |
| Excitement | 3.0 / 5 | "歧义对 LLM agent 有害"在直觉上不意外；clause vs. type 方差分解和 mechanism 预测是最有新意的发现，但 taxonomy 衍生性和领域局限压低了兴奋度 |
| Reproducibility | 4.0 / 5 | 承诺发布 300 clause pairs、评估 pipeline 和原始 traces；ICC=0.919 可复现性；模型 API 调用日期明确 |
| Overall Assessment | 3.5 / 5 | 方法论贡献过硬，但新颖性和影响力尚不足以确保主会议接收 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 遗漏重要相关工作：Ambig-SWE (ICLR 2026)
- 具体位置：Section 2 (Related Work)，特别是 "Psycholinguistics of ambiguity processing" 段落和 disambiguation neglect 讨论
- 问题：Ambig-SWE (Mou et al., ICLR 2026, arXiv:2502.13069) 直接研究 agent 在 underspecified/ambiguous 指令下的行为，发现交互式 disambiguation 可将性能提升高达 74%。该论文区分了 ambiguity 和 underspecificity——正是本文 taxonomy 中 linguistic layer 和 specification layer 的核心区别。这是 2026 年在 top venue 发表的最直接相关工作，不引用将被 reviewer 视为文献覆盖缺陷。
- 为什么影响接收：ARR 评审标准明确要求 related work 覆盖完整。Ambig-SWE 的交互式 disambiguation 成功率直接挑战本文 "disambiguation neglect" 叙事——如果 agent 被允许交互，neglect 可能是 system prompt 设计问题而非 agent 内在缺陷。不讨论这一对比会削弱 Section 6.2 和 Discussion 的说服力。
- 建议修改方向：在 Related Work 加入 Ambig-SWE 引用，在 Discussion 中讨论 interactive vs. non-interactive 设置下 disambiguation 行为的差异，并在 Limitations 的 "Disambiguation channel" 段落中引用 Ambig-SWE 的发现作为对比证据。

**N2** [critical] Taxonomy 新颖性不足，需更清晰地定位增量贡献
- 具体位置：Section 3 (Ambiguity Taxonomy)，Table 1
- 问题：六类 taxonomy 直接源自 Li et al. (2024) 的 11 类 NLP taxonomy、Massey et al. (2014) 的 6 类 RE taxonomy、以及 DRIP-R (2026) 的 5 类。论文承认"we select types based on frequency"和"our taxonomy serves as an experimental instrument"（Section 2, line 5）。然而，选择标准（"frequency in operational policy documents and theoretical distinctiveness"）未提供量化支撑——频率数据从何而来？为什么正好是这六类？为什么不包括 ellipsis（DRIP-R 的类型之一）或 pragmatic implicature（Li et al. 的类型之一）？
- 为什么影响接收：如果 taxonomy 本身不是贡献，论文需要更加明确地将其定位为"实验工具"而非隐含的贡献项。当前 Introduction 的三点 contribution 声明中，虽未直接列 taxonomy 为贡献，但读者仍可能认为六类 taxonomy 是核心创新。这种定位模糊会在 reviewer 中引发"incremental over DRIP-R"的质疑。
- 建议修改方向：(1) 在 Section 3 增加类型选择的定量依据或操作标准；(2) 明确声明 taxonomy 的功能定位——它是实验独立变量的操作化，而非提议的分类标准；(3) 解释为何排除 ellipsis 和 pragmatic implicature。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Disambiguation neglect" 与已有概念的区分度不够
- 具体位置：Section 6.2
- 问题：Liu et al. (2023) 已证明 LLM 会将歧义"collapse"为单一输出；Gur-Arieh et al. (2026) 将此 taxonomy 化为"ambiguity collapse"的 epistemic risks。本文的 "disambiguation neglect" 在概念上与 "ambiguity collapse" 高度重叠。Section 6.2 确实承认"prior work shows LLMs collapse ambiguity into single interpretations in non-agentic settings"，但其区分论据——"our contribution is demonstrating that this collapse persists in agentic contexts"——更像是对已知现象的场景扩展，而非新发现。
- 建议：更明确地界定 disambiguation neglect 与 ambiguity collapse 的边界。如果差异主要在"agentic context 下产生不可逆后果"，则应强调后果层面的新颖性而非行为层面。

**W2** [warning] 生态效度的量化差距
- 具体位置：Section 9 (Limitations)，以及 Abstract/Conclusion 中的效应量报告
- 问题：合成歧义注入产生的 +34.0 pp 效应是上界；SOPBench 复现为 +12.6 pp（且两个模型未达个体显著性）。论文在 Limitations 中承认这一点，但 Abstract 和 Conclusion 的措辞仍以 34.0 pp 为主要数字。一个真正面向部署的论文需要回答：真实世界策略文档中歧义的 prevalence 是多少？如果自然歧义 prevalence 为 10%，则实际影响为 3.4 pp——这改变了实际意义的判断。
- 建议：(1) 在 Abstract 或 Conclusion 中更突出 SOPBench 的 +12.6 pp 作为更保守的效应量估计；(2) 讨论自然歧义 prevalence 作为实际影响的 moderator。

**W3** [warning] bib 条目问题
- 具体位置：references.bib
- 问题：
  - **重复条目**：`yu_causal_2026`（line 323）和 `yu2026causal`（line 442）指向同一篇论文 (arXiv:2603.20320)。
  - **Anonymous 作者**：`disambiguation_cqa_survey_2025`、`atbench_2026`、`riskybench_2026` 三个条目作者为 "Anonymous"。如果这些是匿名预印本，应注明；如果已有公开作者信息，应更新。Anonymous 作者在审稿中会引发引用真实性疑虑。
  - `tamkin_evaluating_2023` 的 booktitle 字段为 "arXiv preprint"，不应使用 @inproceedings 类型。
- 建议：修复重复条目，核实 Anonymous 作者条目的真实性，统一 bib 条目类型。

**W4** [warning] 其他可能遗漏的相关文献
- 具体位置：Section 2 (Related Work)
- 问题：除 Ambig-SWE 外，以下 2025-2026 文献可能与本文研究直接相关：
  - **Ambig-DS** (arXiv:2605.09698, 2025)：data-science agent 中的 task-framing ambiguity benchmark，与本文的 task-level ambiguity 研究互补
  - **Active Task Disambiguation with LLMs** (arXiv:2502.04485, 2025)：主动 disambiguation 策略，直接关联 disambiguation neglect 发现
  - **CAR-bench** (arXiv:2601.22027, 2026)：评估 agent 在不确定性下的一致性和 limit-awareness
- 建议：至少引用 Ambig-SWE（Must-Fix N1）；其余按作者判断是否纳入。

**W5** [warning] Abstract 信息密度过高
- 具体位置：Abstract（Section 0）
- 问题：Abstract 在 3 个句子内堆叠了 OR=15.1、+18.7 to +36.0 pp、22.4% vs 0.4%、17×、≤11%、41.3% 等 7+ 个数值指标。这超出了大多数读者的工作记忆容量。对比同类论文（如 DRIP-R 或 AgentPex），本文 abstract 的数值密度显著高于行业常规。
- 建议：精简至 3-4 个核心数值（主效应、OR、variance 分解比、awareness rate），将其余移入正文。

---

## 小问题（不影响接收）

- **M1**: "17× more strongly"（Abstract, Introduction, Results, Discussion, Conclusion）在全文出现 5 次。建议在 Abstract 和 Conclusion 各保留一次，正文中可引用 section 而非重复数值。
- **M2**: Table 2 caption 中 "5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla. = Claude, Qw3 = Qwen3, DS = DeepSeek" 可移入 Table 正文的列头注释。
- **M3**: Section 4.6 中 "$n_{\text{disc}} = 580$ of $1{,}497$ pairs" 中 1,497 应为 1,498.5（2,997/2），但实际匹配对数为 floor(2997/2)=1498 或直接 300 clause pairs × 5 models = 1500 减去 3 个 API error = 1497。此处逻辑可再明确一句。
- **M4**: 附录中 Clause Pair Examples（Table 12）的 unambiguous 列被标注为 "Control"，ambiguous 列被标注为 "Treatment"——这是因果推断术语的正确用法，但与正文 Section 4.2 的 "ambiguous variant" 和 "matched unambiguous variant" 措辞不一致（正文未使用 treatment/control 术语）。建议统一。

---

## 主要优势

1. **匹配对因果设计**是本文最强的方法论贡献——相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。perturbation control 排除了表面编辑效应，设计严谨。
2. **"clause wording drives risk, type predicts mechanism" 的双重分解**是真正有洞察力的发现。22.4% vs 0.4% 的方差分解和 NMI 17× 的互信息分析使 taxonomy 从"分类标签"转化为"诊断工具"，这是一个有说服力的 reframing。
3. **统计透明度**极高：margin-dependence 明确展示（Table 3 七个 margin）、confound 分析多层控制、cross-judge 三族验证、七模型跨架构复现。这在 agent safety 文献中罕见。
4. **Limitations 坦诚且具体**：明确承认合成歧义上界、incompleteness confound、authorization scope 低可靠性、severity threshold 未预注册等。这是成熟研究的标志。
5. **Cross-benchmark 复现**（SOPBench）和 **cross-judge 验证**（GPT/Claude/Gemini 三族 Fleiss' κ=0.717）增强了结论的鲁棒性。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤8 页 | ✅ | Sections 1-8 在 pages 1-8，Limitations 从 page 9 开始 |
| 双盲匿名 | ✅ | 作者为 "Anonymous ACL submission"，无自引泄露 |
| Limitations section | ✅ | Page 9，覆盖生态效度、范围、测量、confound、disambiguation channel 五个方面 |
| Ethics statement | ⚠️ | 无独立 Ethics 段落，但 CLAUDE.md 指出 ARR checklist 在 OpenReview form 中填写，论文中不需要 |
| 引用格式 | ⚠️ | 存在 bib 重复条目和 Anonymous 作者问题（见 W3） |
| ACL 模板 | ✅ | 使用 `\usepackage[review]{acl}` |

---

## 独立评分总结

| 指标 | 分数 |
|------|------|
| **Overall Assessment** | **3.5**（Borderline Conference）|
| **Soundness** | **4.0**（Strong）|
| **Excitement** | **3.0**（Interesting）|
| **Confidence** | **4**（Quite sure）|

**核心判断**：这篇论文的方法论执行（causal design, controls, replications）达到了会议接收水平，但新颖性存在两个短板：(1) taxonomy 衍生自已有分类体系，缺乏独立创新；(2) "disambiguation neglect" 在概念上与 ambiguity collapse 重叠度高。如果作者能在 camera-ready 中补充 Ambig-SWE 引用、明确 taxonomy 的工具定位、并在 abstract 中降低数值密度，我倾向于提升至 4.0。当前评分反映的是"方法过硬但新颖性需更清晰界定"的判断。

---

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审查结论**：Overall 3.5 (Borderline Conference), Soundness 4/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5。

识别了 2 个 Must-Fix 问题：
1. **Failure mode taxonomy 与 ambiguity taxonomy 的定义循环性**——"17× diagnostic power" 的核心 claim 部分可能是 tautological artifact（如 auth scope → boundary violation），且 LLM 编码 LLM 失败的循环性风险未通过人工验证消解
2. **SESOI ±15pp 缺乏外部锚定**——C2 的 mid-tier cluster 在 ±10pp 下瓦解（仅 3/6 pairs 等价），partial ordering 是 parameter-contingent 而非 robust 结论

5 个 Should-Fix 问题涉及 cross-judge 分配非随机化、human validation 检验力不足、perturbation control 的 construct validity、variance decomposition 解释、SOPBench replication 效力偏弱。

论文的自我批判性和 appendix 深度值得肯定，C1 的证据链扎实。如能妥善处理 N1（弱化 17× claim）和 N2（正文展示多 margin 等价结构），可达 Conference 水准。

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿摘要**：Overall 3.5（Borderline Conference），Soundness 4.0，Excitement 3.0，Confidence 4。

核心判断：匹配对因果设计和统计执行达到会议水平，但存在两个新颖性短板——taxonomy 衍生自已有分类体系（Li et al. 2024 / Massey et al. 2014 / DRIP-R），"disambiguation neglect" 与 ambiguity collapse 概念重叠度高。提出了 2 个 Must-Fix（遗漏 Ambig-SWE ICLR 2026 引用、taxonomy 新颖性定位需更清晰）和 5 个 Should-Fix（概念区分度、生态效度量化、bib 问题、其他遗漏文献、abstract 信息密度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-23T02:39:16.668630+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n### Must-Fix 问题\n\n**N1** [critical] 遗漏重要相关工作：Ambig-SWE (ICLR 2026)\n- Ambig-SWE (Mou et al., ICLR 2026, arXiv:2502.13069) 直接研究 agent 在 underspecified/ambiguous 指令下的行为，发现交互式 disambiguation 可将性能提升高达 74%。该论文区分了 ambiguity 和 underspecificity——正是本文 taxonomy 中 linguistic layer 和 specification layer 的核心区别。这是 2026 年在 top venue 发表的最直接相关工作，不引用将被 reviewer 视为文献覆盖缺陷。Ambig-SWE 的交互式 disambiguation 成功率直接挑战本文 \"disambiguation neglect\" 叙事——如果 agent 被允许交互，neglect 可能是 system prompt 设计问题而非 agent 内在缺陷。\n\n**N2** [critical] Taxonomy 新颖性不足，需更清晰地定位增量贡献\n- 六类 taxonomy 直接源自 Li et al. (2024)、Massey et al. (2014) 和 DRIP-R (2026)。选择标准（\"frequency in operational policy documents and theoretical distinctiveness\"）未提供量化支撑。为什么不包括 ellipsis（DRIP-R 的类型之一）或 pragmatic implicature（Li et al. 的类型之一）？建议明确声明 taxonomy 是实验独立变量的操作化，而非提议的分类标准。\n\n### Should-Fix 问题\n\n**W1** \"Disambiguation neglect\" 与 ambiguity collapse 概念区分度不够——差异主要在\"agentic context 下产生不可逆后果\"，更像场景扩展而非新发现。\n\n**W2** 生态效度的量化差距——Abstract/Conclusion 以 34.0pp 为主要数字，但 SOPBench 复现仅 +12.6pp；未讨论自然歧义 prevalence 作为实际影响的 moderator。\n\n**W3** bib 条目问题——yu_causal_2026 和 yu2026causal 重复；3 个 Anonymous 作者条目；tamkin_evaluating_2023 类型错误。\n\n**W4** 其他可能遗漏文献——Ambig-DS (arXiv:2605.09698)、Active Task Disambiguation (arXiv:2502.04485)、CAR-bench (arXiv:2601.22027)。\n\n**W5** Abstract 信息密度过高——7+ 个数值指标超出读者工作记忆容量。\n\n### 小问题\n- M1: \"17×\" 全文出现 5 次，建议精简\n- M2: Table 2 caption 缩写可移入列头\n- M3: §4.6 中 1,497 pairs 的计算逻辑可再明确\n- M4: 附录 Table 12 的 treatment/control 术语与正文不一致\n\n### 主要优势\n1. 匹配对因果设计是唯一提供因果证据的工作\n2. \"clause wording drives risk, type predicts mechanism\" 的双重分解有洞察力\n3. 统计透明度极高\n4. Limitations 坦诚且具体\n5. Cross-benchmark 复现和 cross-judge 验证增强鲁棒性\n\n### 总体评分\nOverall 3.5 (Borderline Conference), Soundness 4.0, Excitement 3.0, Confidence 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n### Must-Fix 问题\n\n**N1** [critical] 遗漏重要相关工作：Ambig-SWE (ICLR 2026)\n- Ambig-SWE (Mou et al., ICLR 2026, arXiv:2502.13069) 直接研究 agent 在 underspecified/ambiguous 指令下的行为，发现交互式 disambiguation 可将性能提升高达 74%。该论文区分了 ambiguity 和 underspecificity——正是本文 taxonomy 中 linguistic layer 和 specification layer 的核心区别。这是 2026 年在 top venue 发表的最直接相关工作，不引用将被 reviewer 视为文献覆盖缺陷。Ambig-SWE 的交互式 disambiguation 成功率直接挑战本文 \"disambiguation neglect\" 叙事——如果 agent 被允许交互，neglect 可能是 system prompt 设计问题而非 agent 内在缺陷。\n\n**N2** [critical] Taxonomy 新颖性不足，需更清晰地定位增量贡献\n- 六类 taxonomy 直接源自 Li et al. (2024)、Massey et al. (2014) 和 DRIP-R (2026)。选择标准（\"frequency in operational policy documents and theoretical distinctiveness\"）未提供量化支撑。为什么不包括 ellipsis（DRIP-R 的类型之一）或 pragmatic implicature（Li et al. 的类型之一）？建议明确声明 taxonomy 是实验独立变量的操作化，而非提议的分类标准。\n\n### Should-Fix 问题\n\n**W1** \"Disambiguation neglect\" 与 ambiguity collapse 概念区分度不够——差异主要在\"agentic context 下产生不可逆后果\"，更像场景扩展而非新发现。\n\n**W2** 生态效度的量化差距——Abstract/Conclusion 以 34.0pp 为主要数字，但 SOPBench 复现仅 +12.6pp；未讨论自然歧义 prevalence 作为实际影响的 moderator。\n\n**W3** bib 条目问题——yu_causal_2026 和 yu2026causal 重复；3 个 Anonymous 作者条目；tamkin_evaluating_2023 类型错误。\n\n**W4** 其他可能遗漏文献——Ambig-DS (arXiv:2605.09698)、Active Task Disambiguation (arXiv:2502.04485)、CAR-bench (arXiv:2601.22027)。\n\n**W5** Abstract 信息密度过高——7+ 个数值指标超出读者工作记忆容量。\n\n### 小问题\n- M1: \"17×\" 全文出现 5 次，建议精简\n- M2: Table 2 caption 缩写可移入列头\n- M3: §4.6 中 1,497 pairs 的计算逻辑可再明确\n- M4: 附录 Table 12 的 treatment/control 术语与正文不一致\n\n### 主要优势\n1. 匹配对因果设计是唯一提供因果证据的工作\n2. \"clause wording drives risk, type predicts mechanism\" 的双重分解有洞察力\n3. 统计透明度极高\n4. Limitations 坦诚且具体\n5. Cross-benchmark 复现和 cross-judge 验证增强鲁棒性\n\n### 总体评分\nOverall 3.5 (Borderline Conference), Soundness 4.0, Excitement 3.0, Confidence 4"
  }
}
```

</details>

---


### Tool result

_source line 1737 · 2026-05-23T02:39:48.870889+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32202
}
```

</details>

---


### Tool call

_source line 1738 · 2026-05-23T02:39:49.021837+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性审查\n\n### Must-Fix 问题\n\n**N1** [critical] Failure mode taxonomy 与 ambiguity taxonomy 之间的定义循环性\n- 三种 failure mechanisms（structural misparse, gap-filling, boundary violation）与 ambiguity types 存在定义层面的高度重叠：authorization scope 的 boundary violation 本质上就是 scope 类歧义的直接后果；incompleteness 的 information gap-filling 就是信息缺失的直接表现。这使得高 mutual information 可能部分反映分类学定义的重叠（tautological association）而非独立的经验发现。此外，failure mode 编码使用 LLM 标注 LLM 的失败模式（§6 承认 \"introduces circularity risk\"），编码者间一致性仅为 Gwet's AC₁ = 0.62 / κ = 0.52（moderate）。\n- 这是 Discussion 和 Abstract 中的核心贡献之一（\"establishing the taxonomy as a diagnostic tool\"）。如果 type→mechanism 的高关联部分是定义驱动的 artifact，taxonomy 的 \"诊断价值\" 论证就被严重削弱。\n- 建议：(1) 区分哪些关联是定义驱动 vs. 经验发现的；(2) 对 failure mode 编码进行人工验证；(3) 弱化 \"17×\" 的表述。\n\n**N2** [critical] SESOI ±15pp 缺乏外部锚定，显著影响 C2 结论\n- C2 的 \"mid-tier cluster\" 完全依赖 SESOI = ±15pp。在 ±10pp 下，仅 3/6 mid-tier pairs 等价，cluster 结构瓦解。TOST power 在 ±10pp 仅 0.57。±15pp 在实际场景中是否合理取决于应用场景，论文未提供任何来自实际部署的校准数据。\n- 建议：(1) 正文明确展示 ±10pp 下的等价结构；(2) 将 C2 重新表述为 \"robust extremes with margin-dependent intermediate structure\"；(3) 提供实际 policy 审计实践的 SESOI 参考。\n\n### Should-Fix 问题\n\n**W1** Cross-judge 分配非随机化——matched-pair 差异中 judge bias 抵消仅在 additive bias 时成立。如果 judge × condition 有交互效应，则 confound 仍在。Appendix W 三家 judge 验证仅覆盖 ambiguous condition。\n\n**W2** Human validation per-type 样本仅 32-34 episodes，scopal κ CI = [0.00, 1.00]，对 type-level reliability 几乎无信息量。正文 §4.4 的表述可能过于乐观。\n\n**W3** Perturbation control 的 construct validity——synonym substitution/clause reordering 与 ambiguity manipulation 不在同一层面。更相关的 control 是 information-addition without disambiguation。\n\n**W4** Variance decomposition 解释——22.4% clause identity effect 主要是 within-type 变异（22.0%），clause-level auditing 在实践中可能不可行。Discussion 应区分 clause-level vs. type-level auditing 的 actionability。\n\n**W5** SOPBench replication 效力偏弱——+12.6pp vs τ²-bench +34.0pp，5 个模型中仅 3 个 individual significance。\n\n### 小问题\n- M1: Abstract 中 \"+18.7 to +36.0pp\" 可能被误读为 model-level range\n- M2: §4.4 McNemar's test 基于 9 vs 6 discordant pairs，样本量偏小\n- M3: §5.1 \"clause wording drives variance\" 与 \"significant type heterogeneity\" 的 juxtaposition 可能令读者困惑\n- M4: §4.2 同批 annotators 创建和验证 pairs，存在 confirmation bias 风险\n- M5: Detection F1=0.63 定位为 proof-of-concept 表述恰当\n- M6: Auth scope per-type ICC ≈ 0，reproducibility 极低却驱动唯一显著交互效应，形成张力\n\n### 主要优势\n1. Matched-pair 因果设计在 agent safety 领域属方法论创新\n2. 多层 robustness checks\n3. Claims 校准诚实（C3 inconclusive, C4 exploratory）\n4. 统计方法与数据结构匹配\n5. Appendix 深度可圈可点\n\n### 总体评分\nOverall 3.5 (Borderline Conference), Soundness 4/5, Excitement 3/5, Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性审查\n\n### Must-Fix 问题\n\n**N1** [critical] Failure mode taxonomy 与 ambiguity taxonomy 之间的定义循环性\n- 三种 failure mechanisms（structural misparse, gap-filling, boundary violation）与 ambiguity types 存在定义层面的高度重叠：authorization scope 的 boundary violation 本质上就是 scope 类歧义的直接后果；incompleteness 的 information gap-filling 就是信息缺失的直接表现。这使得高 mutual information 可能部分反映分类学定义的重叠（tautological association）而非独立的经验发现。此外，failure mode 编码使用 LLM 标注 LLM 的失败模式（§6 承认 \"introduces circularity risk\"），编码者间一致性仅为 Gwet's AC₁ = 0.62 / κ = 0.52（moderate）。\n- 这是 Discussion 和 Abstract 中的核心贡献之一（\"establishing the taxonomy as a diagnostic tool\"）。如果 type→mechanism 的高关联部分是定义驱动的 artifact，taxonomy 的 \"诊断价值\" 论证就被严重削弱。\n- 建议：(1) 区分哪些关联是定义驱动 vs. 经验发现的；(2) 对 failure mode 编码进行人工验证；(3) 弱化 \"17×\" 的表述。\n\n**N2** [critical] SESOI ±15pp 缺乏外部锚定，显著影响 C2 结论\n- C2 的 \"mid-tier cluster\" 完全依赖 SESOI = ±15pp。在 ±10pp 下，仅 3/6 mid-tier pairs 等价，cluster 结构瓦解。TOST power 在 ±10pp 仅 0.57。±15pp 在实际场景中是否合理取决于应用场景，论文未提供任何来自实际部署的校准数据。\n- 建议：(1) 正文明确展示 ±10pp 下的等价结构；(2) 将 C2 重新表述为 \"robust extremes with margin-dependent intermediate structure\"；(3) 提供实际 policy 审计实践的 SESOI 参考。\n\n### Should-Fix 问题\n\n**W1** Cross-judge 分配非随机化——matched-pair 差异中 judge bias 抵消仅在 additive bias 时成立。如果 judge × condition 有交互效应，则 confound 仍在。Appendix W 三家 judge 验证仅覆盖 ambiguous condition。\n\n**W2** Human validation per-type 样本仅 32-34 episodes，scopal κ CI = [0.00, 1.00]，对 type-level reliability 几乎无信息量。正文 §4.4 的表述可能过于乐观。\n\n**W3** Perturbation control 的 construct validity——synonym substitution/clause reordering 与 ambiguity manipulation 不在同一层面。更相关的 control 是 information-addition without disambiguation。\n\n**W4** Variance decomposition 解释——22.4% clause identity effect 主要是 within-type 变异（22.0%），clause-level auditing 在实践中可能不可行。Discussion 应区分 clause-level vs. type-level auditing 的 actionability。\n\n**W5** SOPBench replication 效力偏弱——+12.6pp vs τ²-bench +34.0pp，5 个模型中仅 3 个 individual significance。\n\n### 小问题\n- M1: Abstract 中 \"+18.7 to +36.0pp\" 可能被误读为 model-level range\n- M2: §4.4 McNemar's test 基于 9 vs 6 discordant pairs，样本量偏小\n- M3: §5.1 \"clause wording drives variance\" 与 \"significant type heterogeneity\" 的 juxtaposition 可能令读者困惑\n- M4: §4.2 同批 annotators 创建和验证 pairs，存在 confirmation bias 风险\n- M5: Detection F1=0.63 定位为 proof-of-concept 表述恰当\n- M6: Auth scope per-type ICC ≈ 0，reproducibility 极低却驱动唯一显著交互效应，形成张力\n\n### 主要优势\n1. Matched-pair 因果设计在 agent safety 领域属方法论创新\n2. 多层 robustness checks\n3. Claims 校准诚实（C3 inconclusive, C4 exploratory）\n4. 统计方法与数据结构匹配\n5. Appendix 深度可圈可点\n\n### 总体评分\nOverall 3.5 (Borderline Conference), Soundness 4/5, Excitement 3/5, Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1739 · 2026-05-23T02:39:50.379353+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-23T02:39:55.109483+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-23T02:40:01.388781+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 6279
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-23T02:40:01.389238+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1743 · 2026-05-23T02:40:01.439798+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1744 · 2026-05-23T02:40:03.588445+00:00_

视觉审查已启动，外部审稿未启用。等待 Reviewer 交叉回应中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 166

## Round 166

2 recorded events


### User

_source line 1745 · 2026-05-23T02:40:50.468542+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 遗漏 Ambig-SWE (ICLR 2026)**

同意应引用。Ambig-SWE 研究 agent 在 ambiguous 指令下的行为，与本文的 policy ambiguity 研究直接相关。但需要区分两个层面：

1. **相关工作遗漏**：确实应引用并定位差异（Ambig-SWE 研究 task instructions 的 ambiguity，本文研究 policy specifications 的 ambiguity；前者的 disambiguation channel 是 user interaction，后者的 agent 没有 clarification channel）。这是合理的文献补充。

2. **对 "disambiguation neglect" 叙事的挑战**：R2 认为 Ambig-SWE 的交互式 disambiguation 成功率挑战了本文的 neglect 发现。但本文 §6.2 已明确将 neglect 定义为 "absence of disambiguation in default settings, not inability"，且 Limitations 最后一段（§9 "Disambiguation channel"）承认 τ²-bench 的 system prompt 可能抑制 disambiguation 行为。更关键的是，本文 Appendix B 的 mitigation experiment 已经展示了 prompting 可部分 elicit disambiguation（auth scope -18.0pp, lexical -8.9pp），但 incompleteness 不响应（-3.3pp, n.s.）。因此 Ambig-SWE 的发现与本文的 mitigation 结果是互补而非矛盾的。**建议作者引用 Ambig-SWE 并在 §6.2 或 §7 讨论两者的互补关系，而非将其视为对 neglect 发现的根本挑战。**

严重程度同意 R2：确实是必须修复的遗漏。但不同意其影响的方向——这更多是 strengthens the narrative（不同场景下的 converging evidence）而非 undermines it。

---

**[REBUT] R2-N2: Taxonomy 新颖性不足**

部分不同意将此标为 critical。

1. **论文已有定位**：§3 明确说明 taxonomy "draws on Li et al. (2024b)'s NLP taxonomy (11 types), Massey et al. (2014)'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark"。Appendix L（DRIP-R Category Mapping）逐项映射了本 taxonomy 与 DRIP-R 的对应关系，说明 scopal 和 coreferential 直接对应，而其余四类是 policy-specific 的。这已经是对增量贡献的清晰说明。

2. **排除类型的理由**：R2 问为何不包括 ellipsis 和 pragmatic implicature。论文 §3 的选择标准是 "frequency in operational policy documents and theoretical distinctiveness (each type maps to a different resolution mechanism)"。Ellipsis 在 DRIP-R 中被包含但在 policy documents 中不常见；pragmatic implicature 在 Li et al. 的 11-type taxonomy 中是一个类型但其 resolution mechanism 与 lexical ambiguity 重叠。这些理由可以更明确，但并非 critical 缺陷。

3. **核心贡献不是 taxonomy 本身**：论文的核心贡献是 matched-pair causal evidence，taxonomy 是实验设计的 independent variable。§7 的关键洞察——"type predicts mechanism 17× more than violation rate"——是在实验数据上发现的，不是 taxonomy 分类学的贡献。

**建议**：同意 R2 的建议"明确声明 taxonomy 是实验 IV 的操作化"是好的写作改进，但不同意将此标为 critical/must-fix——它是 framing 问题，不影响技术正确性。降级为 should-fix。

---

### Should-Fix 问题

**[AGREE] R2-W1: Disambiguation neglect vs ambiguity collapse 概念区分度**

同意。§6.2 已经承认 "Prior work shows LLMs collapse ambiguity into single interpretations in non-agentic settings; our contribution is demonstrating that this collapse persists in agentic contexts where it produces irreversible policy violations"。这确实更像 context extension 而非新发现。但我认为 context matters：在 agentic settings 中 collapse → irreversible policy violations 的因果链是新的经验证据。建议作者弱化 "disambiguation neglect" 作为独立概念的强调，更多地将其定位为 ambiguity collapse 在 agentic context 下的后果验证。

---

**[AGREE] R2-W2: 生态效度的量化差距**

强烈同意。这也是我在自己审稿中的关注点。34.0pp（τ²-bench）vs 12.6pp（SOPBench）的差距在 abstract 和 conclusion 中未得到充分体现。Abstract 以 34.0pp 为 headline number，但这是合成控制条件下的上界。自然歧义的 prevalence 和 severity 分布是从实验数据推广到实际影响的关键 moderator，但论文未讨论。建议在 abstract 或 conclusion 中明确提及 SOPBench 的 +12.6pp 作为 cross-benchmark reference point，并在 §9 Limitations 讨论 prevalence 作为 effect-to-impact 的 scaling factor。

---

**[AGREE] R2-W3: bib 条目问题**

纯技术问题，应修复。

---

**[AGREE] R2-W4: 其他可能遗漏文献**

未能独立验证这些文献的存在和相关性，但如果它们确实是 2025-2026 年直接相关的工作，应引用。建议作者逐条审查并纳入 §2 Related Work。

---

**[AGREE] R2-W5: Abstract 信息密度过高**

同意。重新阅读 abstract，统计到至少 7 个具体数值：34.0pp, OR=15.1, +18.7 to +36.0pp, 22.4% vs 0.4%, 17×, ≤11%, 41.3%。对于 ~150 词的 abstract 来说确实过密。建议保留 3-4 个最关键的数字（34.0pp, OR, confound-free range, 和 mechanism prediction 的定性描述），其余移至 Introduction。

---

### 小问题

**[AGREE] R2-M1**: "17×" 出现 5 次确实冗余。而且如我在 N1 中指出的，17× 本身存在定义循环风险，频繁重复会放大这个问题。

**[AGREE] R2-M2**: Table 2 caption 缩写问题是排版改进。

**[AGREE] R2-M3**: §4.6 中 1,497 pairs 的计算逻辑：300 pairs × 5 models = 1,500，减去 3 个 API error = 1,497。从上下文可推导但可以写得更清楚。

**[AGREE] R2-M4**: 附录 Table 12 的术语一致性问题应修复。

---

### 对 R2 总体评分的评论

R2 给出 Overall 3.5, Soundness 4.0, Excitement 3.0——与我的评分一致（我也是 Overall 3.5, Soundness 4/5, Excitement 3/5）。两位 reviewer 在以下判断上 converge：

1. **方法论质量高**（both Soundness 4）
2. **新颖性/excitement 一般**（both 3）——方向可预期，taxonomy 是增量贡献
3. **生态效度是主要限制**

两位 reviewer 的 must-fix 问题有交集但不完全重叠：
- R1 关注 failure mode 定义循环和 SESOI 选择（方法层面）
- R2 关注文献遗漏和 taxonomy 定位（贡献层面）

如果作者能同时 address 这两组问题——补充 Ambig-SWE 引用、弱化 17× claim 的定义循环部分、在正文展示多 SESOI 的等价结构、在 abstract 增加 cross-benchmark reference——本文可以达到 Conference 水准（4.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1746 · 2026-05-23T02:40:56.180445+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 167

## Round 167

2 recorded events


### User

_source line 1747 · 2026-05-23T02:40:59.027352+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **5 条 AGREE**（R2-N1 文献遗漏、W1-W5 全部同意），**1 条 REBUT**（R2-N2 taxonomy 新颖性应降级为 should-fix）
- 与 R2 在核心判断上高度一致：Soundness 4、Excitement 3、Overall 3.5
- 两位 reviewer 的 must-fix 互补：我聚焦 failure mode 定义循环 + SESOI 锚定（方法层面），R2 聚焦文献覆盖 + taxonomy 定位（贡献层面）
- 共识：如果作者能同时 address 两组 must-fix，本文可达到 Conference 水准

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1748 · 2026-05-23T02:41:03.332681+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 168

## Round 168

8 recorded events


### User

_source line 1749 · 2026-05-23T02:42:20.649464+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Failure mode taxonomy 与 ambiguity taxonomy 的定义循环性**

同意这是论文中 "17× diagnostic value" 论证的关键弱点。具体来说：

- Authorization scope → boundary violation 近乎定义性映射：如果 authorization boundary 模糊，agent 越权就被编码为 "boundary violation"——这本质上是对同一现象的两种描述。Table 14（Appendix K）的混淆矩阵证实了这一点：authorization scope 的 72/104（69%）traces 编码为 boundary violation，远高于其他类型。
- Incompleteness → gap-filling 同理：信息缺失时 agent 用默认值填充，编码为 "gap-filling"——这是 incompleteness 的直接语义后果。
- 然而，混淆矩阵也显示映射并非完全 tautological：incompleteness 同时有 43 个 structural misparse（vs. 70 gap-filling），coreferential 跨三种机制分布相对均匀（37/29/5）。这说明部分关联是经验性的，但 R1 的核心观点成立——MI 的绝对值被定义重叠抬高了。

补充我自己的观察：failure mode 编码的 inter-rater agreement（Gwet's AC₁ = 0.62, κ = 0.52）仅为 moderate，且使用 LLM 编码 LLM 失败模式的循环性风险论文自身也承认（§6, line 6）。论文提供的反驳证据——"mutual information between type (exogenous) and mechanism labels provides structural anti-circularity evidence"——在 R1 指出的定义重叠问题面前说服力不足：type 标签是 exogenous 的，但 mechanism 标签的定义与 type 语义高度耦合，exogeneity 不能排除 definitional artifact。

**建议**：应要求作者 (1) 对至少一个子集（如 100 traces）进行人工 failure mode 编码验证；(2) 将 "17×" 弱化为 "type predicts mechanism substantially better than violation rate"，不再使用精确倍数作为核心卖点；(3) 在正文中明确区分哪些 type→mechanism 映射是定义驱动的（auth scope→boundary, incompleteness→gap-filling）vs. 经验发现的（scopal→structural misparse）。

---

**[REBUT] R1-N2: SESOI ±15pp 缺乏外部锚定**（部分反驳）

R1 的核心关切——SESOI 缺乏外部校准——是合理的，但论文对此的处理比 R1 描述得更充分：

1. **论文已展示完整 margin 敏感性**：Table 3（Appendix A）报告了从 ±5pp 到 ±20pp 共七个 margin 下的等价结构，§5.2 明确指出 "mid-tier cohesion emerges at ±12 pp and stabilizes at ±15 pp"。读者可在任何偏好阈值下评估 C2。
2. **论文已提供 margin-free 补充**：Bootstrap cluster analysis（Appendix G, B=10,000）不依赖任何 SESOI，其结论与 ±15pp TOST 一致——incompleteness 在 k=2 时形成 singleton，coreferential 在 k=3 时分离。
3. **C2 的表述已经是 "partial ordering"**：§5.2 的结论段明确写道 "C2 should be interpreted as establishing robust extremes—incompleteness as upper bound and coreferential as lower bound—rather than a complete linear ordering"。这与 R1 建议的 "robust extremes with margin-dependent intermediate structure" 实质一致。

但我同意 R1 在以下方面的关切：
- §4.6 对 ±15pp 的操作性论证（"a type producing ≥15 pp more violations warrants distinct policy handling"）未提供部署数据支撑，属于论文作者的主观判断。
- Abstract 中的 "partial ordering" 未附带 margin 条件限定，可能误导快速阅读的读者。

**建议**：(1) 在 Abstract 中限定 "partial ordering (at ±15 pp margin)"；(2) 在 §4.6 增加一句承认 SESOI 无行业标准。不需要全面重写 C2。

---

### Should-Fix 问题

**[AGREE] R1-W1: Cross-judge 分配非随机化**

R1 的技术论点正确：matched-pair 差异中 judge bias 抵消仅在 additive bias 假设下成立。如果 judge 对 ambiguous 和 unambiguous condition 的评判存在交互效应（例如某个 judge 在 ambiguous condition 下系统性地更严格），则 Δpp 受 confound。

Appendix W 的三族 cross-judge 验证（Fleiss' κ=0.717）部分缓解了这一担忧——三个 judge 在同一 episodes 上的 model ranking 一致性高（pairwise ρ ≥ 0.70）。但 R1 指出这仅覆盖了 ambiguous condition（论文原文："we re-evaluate all 2,997 ambiguous-condition episodes"），未验证 unambiguous condition 下的 judge 行为。这意味着 judge × condition 交互无法被排除。

补充：Appendix W 的 Table 17 显示 Gemini judge 系统性地更严格（pooled +8.8pp），但如果这一偏差在 ambiguous 和 unambiguous condition 下一致（additive），则不影响 Δpp。遗憾的是论文未提供数据验证这一假设。

---

**[AGREE] R1-W2: Human validation per-type 样本量不足**

完全同意。Scopal κ CI = [0.00, 1.00]（Table 6, Appendix F）说明估计完全无信息量。论文在 Appendix F 尾段已承认 "Per-type estimates are imprecise due to small cell sizes (n = 32–34); they are descriptive statistics only"，但 §4.4 正文中的表述——"Pooled human–LLM agreement (κ = 0.733, κ_w = 0.807; per-type breakdown in Appendix F) approaches inter-annotator levels, validating the automated pipeline"——没有充分传达 per-type 层面的不确定性。

---

**[REBUT] R1-W3: Perturbation control 的 construct validity**（部分反驳）

R1 认为 synonym substitution/clause reordering 与 ambiguity manipulation 不在同一层面，更好的 control 是 "information-addition without disambiguation"。这个建议有道理，但论文已通过两条路径部分回应了这一关切：

1. **Coreferential 类型提供了天然的信息量控制**：§5.2 和 Appendix D 明确指出 coreferential 的 ambiguous 和 unambiguous variants 是 "lexically identical"（信息量差异=0），其 +18.7pp 效应完全可归因于语义歧义。这比 "information-addition without disambiguation" 控制更强——它是零信息差异下的纯歧义效应。
2. **Logistic regression 控制 token count**（Appendix E, Table 8）：token delta coefficient 为正（β=+0.027），即更长的 clause 预测更多而非更少的 violations——与 information-addition-reduces-violations 假设方向相反。

然而，R1 的建议仍有价值：token count 是信息量的粗糙代理（论文自己承认："Token count is a coarse proxy for information content"，Appendix D 尾段），一个真正的 information-addition-without-disambiguation 控制（例如向 ambiguous clause 添加无关但真实的政策内容）会更具说服力。

---

**[AGREE] R1-W4: Clause-level auditing 的 actionability 讨论不足**

同意。Discussion §7 写道 "clause-level auditing thus addresses the largest actionable component (22.4%)"，但未讨论 clause-level auditing 在实践中的可行性。22.4% 的方差中 22.0% 是 within-type 变异（§5.1），意味着审计者需要逐条评估每个 clause 的歧义风险——这在大规模政策文档中可能不可行。而 type-level auditing（0.4% 方差解释）虽然方差解释低，但可能更可操作（如自动检测器优先标记 incompleteness 和 authorization scope 类型）。论文应在 Discussion 中区分这两种审计策略的成本-收益。

---

**[AGREE] R1-W5: SOPBench replication 效力偏弱**

同意。这也是我在 W2（Should-Fix）中提出的观点。补充一个细节：SOPBench 的 GPT-5.4 和 DeepSeek-V3 使用了 power-expanded 样本（n=374 vs. 其他模型的 n=139），这意味着即使在扩增样本下也未达到个体显著性（GPT-5.4 p=0.052, DeepSeek p=0.163），进一步削弱了 replication 的说服力。论文将 SOPBench 定位为 "directional consistency" 而非 "full replication" 是审慎的，但 Abstract 和 Conclusion 中应更明确地传达效应量差距。

---

### 小问题

**[AGREE] R1-M1**: "+18.7 to +36.0pp" 在 Abstract 中确实可能被误读为 model-level range。实际上这是 type-level range（excluding incompleteness）。应改为 "+18.7 to +36.0 pp across non-confounded types" 或类似限定。

**[AGREE] R1-M2**: McNemar's test 基于 9 vs 6 discordant pairs（§4.4），N=15 过小，p=0.606 的非显著结论缺乏 power。但这仅用于"无系统性检测偏差"的辅助论证，cross-judge 验证（Appendix W）提供了更强的证据。

**[REBUT] R1-M3**: "Clause wording drives variance" 与 "significant type heterogeneity" 的 juxtaposition 并不矛盾。§5.1 清楚地解释了：clause identity 解释 22.4% 方差（其中 0.4% between-type, 22.0% within-type），omnibus χ² 仍然显著因为类型间存在 heterogeneity（V=0.137）。这是方差解释量级（小）vs. 统计显著性（存在）的标准区分——类比 ANOVA 中小 η² 但 significant F。论文的陈述逻辑自洽。

**[AGREE] R1-M4**: 同批 annotators 创建和验证 clause pairs 确实有 confirmation bias 风险。§4.2 提到 "reviewed by two independent annotators" 但未说明这些 annotators 是否也参与了 pair 创建。如果是同一批人，验证的独立性受损。

**[AGREE] R1-M5**: Detection F1=0.63 定位为 proof-of-concept 是恰当的，R1 的肯定我同意。

**[AGREE] R1-M6**: Authorization scope per-type ICC ≈ 0（Appendix X）意味着该类型的观测结果高度依赖具体对话轨迹，但它同时驱动了唯一显著的 model×type 交互效应（C4）。论文在 §5.3 已加了 caution（"interpret with caution"），但这个张力值得在 Discussion 中更明确地指出：C4 的最有趣发现恰好建立在可靠性最低的类型上。

---

### 对 R1 优势评价的回应

完全同意 R1 识别的五项优势。补充强调：R1 提到的 "Claims 校准诚实（C3 inconclusive, C4 exploratory）" 在 agent safety 文献中确实罕见，这是该论文的一个突出优点。

---

### R2 与 R1 评分对齐

| 维度 | R1 | R2 | 一致性 |
|------|-----|-----|--------|
| Overall | 3.5 | 3.5 | ✅ 一致 |
| Soundness | 4/5 | 4/5 | ✅ 一致 |
| Excitement | 3/5 | 3/5 | ✅ 一致 |
| Confidence | 4/5 | 4/5 | ✅ 一致 |

两位 reviewer 在所有维度上完全一致。核心判断相同：方法论执行到位（Soundness 4），但新颖性和影响力处于 borderline（Excitement 3, Overall 3.5）。R1 侧重方法论循环性和统计阈值的外部效度，R2 侧重 taxonomy 原创性和文献覆盖——两个角度互补，共同指向 "执行优于概念" 的整体判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1750 · 2026-05-23T02:42:44.315904+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1751 · 2026-05-23T02:42:44.366517+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"running\", \"started_at\": \"2026-05-23T02:39:56.216053+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1752 · 2026-05-23T02:44:40.678570+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 20\n\n# ============================================================\n# R20 ISSUES — OPEN\n# ============================================================\n\n- id: \"R20-N1\"\n  summary: \"Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"auth scope→boundary violation, incompleteness→gap-filling 是定义驱动映射; LLM 编码 LLM 失败循环性; Gwet AC₁=0.62/κ=0.52 仅 moderate\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"混淆矩阵证实 auth scope 72/104 traces 编码为 boundary violation; 但 incompleteness 也有 43 structural misparse 说明映射非完全 tautological; exogeneity 论证不足以排除 definitional artifact\"\n\n- id: \"R20-N2\"\n  summary: \"遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Ambig-SWE 直接研究 agent 在 ambiguous 指令下行为，交互式 disambiguation 提升高达 74%，挑战 disambiguation neglect 叙事\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意应引用，但认为与 neglect 发现互补而非矛盾——neglect 定义为 default settings 下的行为\"\n\n- id: \"R20-W1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，C2 mid-tier cluster 在 ±10pp 下瓦解\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"±10pp 下仅 3/6 mid-tier pairs 等价; TOST power=0.57; 无行业标准 SESOI; Abstract 'partial ordering' 未附 margin 条件\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-partial-rebut\"\n      note: \"论文已有 Table 3 七 margin 敏感性 + bootstrap cluster (margin-free); C2 表述已为 'robust extremes'; 但同意 §4.6 操作性论证缺部署数据支撑，Abstract 应限定 margin\"\n\n- id: \"R20-W2\"\n  summary: \"Taxonomy 新颖性定位模糊，类型选择缺乏量化依据\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"六类直接源自已有分类; 排除 ellipsis/pragmatic implicature 无量化依据; 可被质疑为 incremental over DRIP-R\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-rebut-downgrade\"\n      note: \"§3 已有定位 + Appendix L 映射; 核心贡献是 matched-pair evidence 非 taxonomy; 降级为 should-fix\"\n\n- id: \"R20-W3\"\n  summary: \"Cross-judge 分配非随机化，judge×condition 交互效应未排除\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"Appendix W 三族验证仅覆盖 ambiguous condition; additive bias 假设未验证\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"Gemini judge 系统性 +8.8pp 但未验证条件间一致性\"\n\n- id: \"R20-W4\"\n  summary: \"Disambiguation neglect 与 ambiguity collapse 概念区分度不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Liu et al. 2023 + Gur-Arieh et al. 2026 已有 ambiguity collapse; 本文差异主要在 agentic context 后果\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"建议弱化独立概念强调，定位为 collapse 在 agentic context 的后果验证\"\n\n- id: \"R20-W5\"\n  summary: \"生态效度量化差距：34.0pp (合成) vs 12.6pp (SOPBench)，Abstract/Conclusion 未充分体现\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"co-originator (W5)\"\n      note: \"SOPBench 5/5 模型仅 3 个 individual significance; GPT-5.4 p=0.052 DeepSeek p=0.163 即使 power-expanded\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"co-originator (W2)\"\n      note: \"Abstract 以 34.0pp 为 headline 但为合成上界; 未讨论自然歧义 prevalence 作为 effect-to-impact scaling factor\"\n\n- id: \"R20-W6\"\n  summary: \"Human validation per-type 检验力不足 (n=32-34, scopal κ CI=[0.00,1.00])\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"正文 §4.4 表述可能给 type-level reliability 过于乐观的印象\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n\n- id: \"R20-W7\"\n  summary: \"Perturbation control 仅测试 surface-level specificity，缺少 information-addition-without-disambiguation 控制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"synonym/reordering 与 semantic ambiguity manipulation 不在同一层面\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-partial-rebut\"\n      note: \"coreferential (lexically identical, Δ=0) 已提供天然信息量控制; token count regression 方向与 information-addition 假设相反; 但同意 token count 是粗糙代理\"\n\n- id: \"R20-W8\"\n  summary: \"Variance decomposition 中 clause-level vs type-level auditing 的 actionability 讨论不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"22.4% clause identity 中 22.0% 是 within-type; clause-level auditing 在大规模文档中可能不可行\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"type-level auditing (0.4% variance) 更可操作但解释力低; 应讨论成本-收益\"\n\n- id: \"R20-W9\"\n  summary: \"Bib 条目问题：重复条目、Anonymous 作者、类型错误\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"yu_causal_2026 与 yu2026causal 重复; 3 条 Anonymous 作者; tamkin_evaluating_2023 @inproceedings 类型错误\"\n\n- id: \"R20-W10\"\n  summary: \"其他可能遗漏文献 (Ambig-DS, Active Task Disambiguation, CAR-bench)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n\n- id: \"R20-W11\"\n  summary: \"Abstract 信息密度过高 (7+ 数值指标)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n\n- id: \"R20-M1\"\n  summary: \"Auth scope ICC≈0 却驱动唯一显著 C4 交互，张力未充分讨论\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator (M6)\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n\n- id: \"R20-M2\"\n  summary: \"§4.2 同批 annotators 创建和验证 pairs 存在 confirmation bias 风险\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator (M4)\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n\n# ============================================================\n# R19 ISSUES — ALL RESOLVED\n# ============================================================\n\n- id: \"R19-N1\"\n  summary: \"合成歧义生态效度不足，+34.0pp 可能高估真实场景\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'; Limitations 新增 Ecological validity 段; §4.2 补 Cohen's κ=0.95\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 继续关注生态效度 (→R20-W5)，但 framing 层面已修复\"\n\n- id: \"R19-N2\"\n  summary: \"非歧义纳入 ambiguity 标签 + behaviorally indistinguishable 与 §6.1 矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"§3 改 'produce comparable safety impact despite distinct underlying mechanisms'; §5.1 加 sans-incompleteness +31.0pp [27.9,34.1]\"\n  resolution_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims 未充分降级\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Figure 3 caption 加 κ=0.385 + 'interpret with caution'; §5.4 改为 'largest cross-model range' + caution caveat\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 未再列为独立 issue，auth scope 可靠性问题已充分降级\"\n\n- id: \"R19-W1\"\n  summary: \"Confound-free range 在 Abstract/Conclusion 不可见\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"Abstract/Conclusion 加 '+18.7 to +36.0pp excluding confounded incompleteness type'\"\n  resolution_round: 19\n\n- id: \"R19-W2\"\n  summary: \"SOPBench framing 过于乐观 (confirms→suggests, 2/5 不显著)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"confirms→suggests; 加 'two not reaching individual significance'\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 继续关注 SOPBench 效力 (→R20-W5)\"\n\n- id: \"R19-W3\"\n  summary: \"60.8% 残差方差实践含义讨论不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Discussion 加方差全景图 + 'addresses largest actionable component but not majority of outcome variance'\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 继续要求区分 clause-level vs type-level auditing actionability (→R20-W8)\"\n\n- id: \"R19-W4\"\n  summary: \"Type III SS 方法论需正文级说明 + logistic partial R²\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"footnote 扩展: Type III SS 理由 + logistic 一致性说明 (Tjur's R²=0.175)\"\n  resolution_round: 19\n\n- id: \"R19-W5\"\n  summary: \"§6 Error Analysis / DN novelty 展开不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"§6.2 加 mitigation 按类型细分 + Liu et al. 区分\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 进一步要求区分 disambiguation neglect vs ambiguity collapse (→R20-W4)\"\n\n- id: \"R19-W6\"\n  summary: \"潜在遗漏相关工作 (3 篇)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"3 篇 BibTeX 加入 + Related Work 引用\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 发现新的遗漏 (→R20-N2 Ambig-SWE, →R20-W10 其他 3 篇)\"\n\n- id: \"R19-W7\"\n  summary: \"领域泛化性有限但 Discussion 暗示更广适用性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"Discussion 加 'In customer-service and similar task-oriented domains'\"\n  resolution_round: 19\n\n# ============================================================\n# R18 RESOLVED\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"C2 降为 secondary claim, robust extremes only.\"\n  resolution_round: 18\n  mentions:\n    - round: 20\n      note: \"R20 继续关注 SESOI margin dependence (→R20-W1)\"\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 完全混淆影响 C4\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Cross-family judge validation κ=0.717, no same-family bias, rankings preserved.\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 关注 cross-judge 仅覆盖 ambiguous condition (→R20-W3)\"\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Taxonomy 降格为 experimental instrument.\"\n  resolution_round: 18\n  mentions:\n    - round: 20\n      note: \"R20 继续要求更清晰定位 (→R20-W2)\"\n\n- id: \"R18-N4\"\n  summary: \"Disambiguation Neglect 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"降级为 descriptive label.\"\n  resolution_round: 18\n  mentions:\n    - round: 20\n      note: \"R20 继续要求与 ambiguity collapse 区分 (→R20-W4)\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"Maintained ≤8 pages.\"\n  resolution_round: 18\n\n# ============================================================\n# R17 RESOLVED\n# ============================================================\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"全文 30× → 17× (NMI-based).\"\n  resolution_round: 17\n  mentions:\n    - round: 20\n      note: \"R20 进一步要求弱化 17× 为定性表述 (→R20-N1)\"\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test (null=8.3%, p<0.001) + GLMM ICC.\"\n  resolution_round: 17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 20\n\n# ============================================================\n# R20 ISSUES — OPEN\n# ============================================================\n\n- id: \"R20-N1\"\n  summary: \"Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"auth scope→boundary violation, incompleteness→gap-filling 是定义驱动映射; LLM 编码 LLM 失败循环性; Gwet AC₁=0.62/κ=0.52 仅 moderate\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"混淆矩阵证实 auth scope 72/104 traces 编码为 boundary violation; 但 incompleteness 也有 43 structural misparse 说明映射非完全 tautological; exogeneity 论证不足以排除 definitional artifact\"\n\n- id: \"R20-N2\"\n  summary: \"遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Ambig-SWE 直接研究 agent 在 ambiguous 指令下行为，交互式 disambiguation 提升高达 74%，挑战 disambiguation neglect 叙事\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意应引用，但认为与 neglect 发现互补而非矛盾——neglect 定义为 default settings 下的行为\"\n\n- id: \"R20-W1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，C2 mid-tier cluster 在 ±10pp 下瓦解\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"±10pp 下仅 3/6 mid-tier pairs 等价; TOST power=0.57; 无行业标准 SESOI; Abstract 'partial ordering' 未附 margin 条件\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-partial-rebut\"\n      note: \"论文已有 Table 3 七 margin 敏感性 + bootstrap cluster (margin-free); C2 表述已为 'robust extremes'; 但同意 §4.6 操作性论证缺部署数据支撑，Abstract 应限定 margin\"\n\n- id: \"R20-W2\"\n  summary: \"Taxonomy 新颖性定位模糊，类型选择缺乏量化依据\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"六类直接源自已有分类; 排除 ellipsis/pragmatic implicature 无量化依据; 可被质疑为 incremental over DRIP-R\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-rebut-downgrade\"\n      note: \"§3 已有定位 + Appendix L 映射; 核心贡献是 matched-pair evidence 非 taxonomy; 降级为 should-fix\"\n\n- id: \"R20-W3\"\n  summary: \"Cross-judge 分配非随机化，judge×condition 交互效应未排除\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"Appendix W 三族验证仅覆盖 ambiguous condition; additive bias 假设未验证\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"Gemini judge 系统性 +8.8pp 但未验证条件间一致性\"\n\n- id: \"R20-W4\"\n  summary: \"Disambiguation neglect 与 ambiguity collapse 概念区分度不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Liu et al. 2023 + Gur-Arieh et al. 2026 已有 ambiguity collapse; 本文差异主要在 agentic context 后果\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"建议弱化独立概念强调，定位为 collapse 在 agentic context 的后果验证\"\n\n- id: \"R20-W5\"\n  summary: \"生态效度量化差距：34.0pp (合成) vs 12.6pp (SOPBench)，Abstract/Conclusion 未充分体现\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"co-originator (W5)\"\n      note: \"SOPBench 5/5 模型仅 3 个 individual significance; GPT-5.4 p=0.052 DeepSeek p=0.163 即使 power-expanded\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"co-originator (W2)\"\n      note: \"Abstract 以 34.0pp 为 headline 但为合成上界; 未讨论自然歧义 prevalence 作为 effect-to-impact scaling factor\"\n\n- id: \"R20-W6\"\n  summary: \"Human validation per-type 检验力不足 (n=32-34, scopal κ CI=[0.00,1.00])\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"正文 §4.4 表述可能给 type-level reliability 过于乐观的印象\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n\n- id: \"R20-W7\"\n  summary: \"Perturbation control 仅测试 surface-level specificity，缺少 information-addition-without-disambiguation 控制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"synonym/reordering 与 semantic ambiguity manipulation 不在同一层面\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-partial-rebut\"\n      note: \"coreferential (lexically identical, Δ=0) 已提供天然信息量控制; token count regression 方向与 information-addition 假设相反; 但同意 token count 是粗糙代理\"\n\n- id: \"R20-W8\"\n  summary: \"Variance decomposition 中 clause-level vs type-level auditing 的 actionability 讨论不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"22.4% clause identity 中 22.0% 是 within-type; clause-level auditing 在大规模文档中可能不可行\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"type-level auditing (0.4% variance) 更可操作但解释力低; 应讨论成本-收益\"\n\n- id: \"R20-W9\"\n  summary: \"Bib 条目问题：重复条目、Anonymous 作者、类型错误\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"yu_causal_2026 与 yu2026causal 重复; 3 条 Anonymous 作者; tamkin_evaluating_2023 @inproceedings 类型错误\"\n\n- id: \"R20-W10\"\n  summary: \"其他可能遗漏文献 (Ambig-DS, Active Task Disambiguation, CAR-bench)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n\n- id: \"R20-W11\"\n  summary: \"Abstract 信息密度过高 (7+ 数值指标)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 20\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n\n- id: \"R20-M1\"\n  summary: \"Auth scope ICC≈0 却驱动唯一显著 C4 交互，张力未充分讨论\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator (M6)\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n\n- id: \"R20-M2\"\n  summary: \"§4.2 同批 annotators 创建和验证 pairs 存在 confirmation bias 风险\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator (M4)\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n\n# ============================================================\n# R19 ISSUES — ALL RESOLVED\n# ============================================================\n\n- id: \"R19-N1\"\n  summary: \"合成歧义生态效度不足，+34.0pp 可能高估真实场景\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'; Limitations 新增 Ecological validity 段; §4.2 补 Cohen's κ=0.95\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 继续关注生态效度 (→R20-W5)，但 framing 层面已修复\"\n\n- id: \"R19-N2\"\n  summary: \"非歧义纳入 ambiguity 标签 + behaviorally indistinguishable 与 §6.1 矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"§3 改 'produce comparable safety impact despite distinct underlying mechanisms'; §5.1 加 sans-incompleteness +31.0pp [27.9,34.1]\"\n  resolution_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims 未充分降级\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Figure 3 caption 加 κ=0.385 + 'interpret with caution'; §5.4 改为 'largest cross-model range' + caution caveat\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 未再列为独立 issue，auth scope 可靠性问题已充分降级\"\n\n- id: \"R19-W1\"\n  summary: \"Confound-free range 在 Abstract/Conclusion 不可见\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"Abstract/Conclusion 加 '+18.7 to +36.0pp excluding confounded incompleteness type'\"\n  resolution_round: 19\n\n- id: \"R19-W2\"\n  summary: \"SOPBench framing 过于乐观 (confirms→suggests, 2/5 不显著)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"confirms→suggests; 加 'two not reaching individual significance'\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 继续关注 SOPBench 效力 (→R20-W5)\"\n\n- id: \"R19-W3\"\n  summary: \"60.8% 残差方差实践含义讨论不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Discussion 加方差全景图 + 'addresses largest actionable component but not majority of outcome variance'\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 继续要求区分 clause-level vs type-level auditing actionability (→R20-W8)\"\n\n- id: \"R19-W4\"\n  summary: \"Type III SS 方法论需正文级说明 + logistic partial R²\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"footnote 扩展: Type III SS 理由 + logistic 一致性说明 (Tjur's R²=0.175)\"\n  resolution_round: 19\n\n- id: \"R19-W5\"\n  summary: \"§6 Error Analysis / DN novelty 展开不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"§6.2 加 mitigation 按类型细分 + Liu et al. 区分\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 进一步要求区分 disambiguation neglect vs ambiguity collapse (→R20-W4)\"\n\n- id: \"R19-W6\"\n  summary: \"潜在遗漏相关工作 (3 篇)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"3 篇 BibTeX 加入 + Related Work 引用\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 发现新的遗漏 (→R20-N2 Ambig-SWE, →R20-W10 其他 3 篇)\"\n\n- id: \"R19-W7\"\n  summary: \"领域泛化性有限但 Discussion 暗示更广适用性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"Discussion 加 'In customer-service and similar task-oriented domains'\"\n  resolution_round: 19\n\n# ============================================================\n# R18 RESOLVED\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"C2 降为 secondary claim, robust extremes only.\"\n  resolution_round: 18\n  mentions:\n    - round: 20\n      note: \"R20 继续关注 SESOI margin dependence (→R20-W1)\"\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 完全混淆影响 C4\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Cross-family judge validation κ=0.717, no same-family bias, rankings preserved.\"\n  resolution_round: 19\n  mentions:\n    - round: 20\n      note: \"R20 关注 cross-judge 仅覆盖 ambiguous condition (→R20-W3)\"\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Taxonomy 降格为 experimental instrument.\"\n  resolution_round: 18\n  mentions:\n    - round: 20\n      note: \"R20 继续要求更清晰定位 (→R20-W2)\"\n\n- id: \"R18-N4\"\n  summary: \"Disambiguation Neglect 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"降级为 descriptive label.\"\n  resolution_round: 18\n  mentions:\n    - round: 20\n      note: \"R20 继续要求与 ambiguity collapse 区分 (→R20-W4)\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"Maintained ≤8 pages.\"\n  resolution_round: 18\n\n# ============================================================\n# R17 RESOLVED\n# ============================================================\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"全文 30× → 17× (NMI-based).\"\n  resolution_round: 17\n  mentions:\n    - round: 20\n      note: \"R20 进一步要求弱化 17× 为定性表述 (→R20-N1)\"\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test (null=8.3%, p<0.001) + GLMM ICC.\"\n  resolution_round: 17"
  }
}
```

</details>

---


### Tool result

_source line 1753 · 2026-05-23T02:44:40.781478+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 13132}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-23T02:47:01.824350+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "report": "# Round 20 审稿报告\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n## 审稿模式: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范中遇到歧义时是否会产生安全违规。作者构建了 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义分类（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes）。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（conditional OR=15.1）；(2) clause wording 解释 22.4% 方差（vs. type 仅 0.4%），但 type 预测 failure mechanism 的能力是预测违规率的 17 倍；(3) agent 对歧义的元认知意识极低（≤11%），41.3% 的歧义 clause 触发多模型趋同违规。\n\n---\n\n## Strengths\n\n**S1 [共识]** 匹配对因果设计在 agent safety 领域属方法论创新——相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的规模和匹配质量（κ=0.95）可信。\n\n**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300, Δ=-0.67pp, CI 含零）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench）、七模型跨架构复现（6 providers）。对 C1 的支撑层层递进。\n\n**S3 [共识]** \"clause wording drives risk, type predicts mechanism\" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解和 NMI 分析将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。\n\n**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive, C4 标注 exploratory；incompleteness confound 被充分讨论；authorization scope 的低可靠性被反复提示。统计方法选择与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster）。\n\n**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑。Limitations 章节覆盖五个方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（两位 Reviewer 共识）\n\n**N1 [critical, 共识]** Failure mode taxonomy 与 ambiguity taxonomy 的定义循环性\n\n\"Type predicts failure mechanism 17× more strongly than violation rate\" 是 Abstract/Discussion/Conclusion 的核心卖点之一。但三种 failure mechanisms 与 ambiguity types 存在定义层面的高度重叠：\n- Authorization scope → boundary violation（72/104 traces, 69%）：如果 authorization boundary 模糊，agent 越权就被编码为 \"boundary violation\"——这是同一现象的两种描述\n- Incompleteness → information gap-filling（70/134 traces）：信息缺失时 agent 用默认值填充，编码为 gap-filling——这是 incompleteness 的直接语义后果\n\n混淆矩阵（Table 14）显示映射并非完全 tautological（如 incompleteness 也有 43 structural misparse），但 MI 的绝对值被定义重叠抬高。此外，failure mode 编码使用 LLM 标注 LLM 失败（§6 自己承认 \"introduces circularity risk\"），编码者间一致性仅 moderate（Gwet's AC₁=0.62, κ=0.52）。论文的反驳——\"MI between exogenous type and mechanism labels provides anti-circularity evidence\"——在定义重叠面前说服力不足。\n\n**要求修改**：(1) 区分哪些 type→mechanism 映射是定义驱动的（auth scope→boundary, incompleteness→gap-filling）vs. 经验发现的（scopal→structural misparse），分别报告 MI；(2) 弱化 \"17×\" 为定性表述（如 \"substantially better\"），不再使用精确倍数作为核心卖点；(3) 对至少 100 traces 进行人工 failure mode 编码验证，或在 Limitations 中明确标注为局限。\n\n**N2 [critical, 共识]** 遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\n\nAmbig-SWE (arXiv:2502.13069) 直接研究 agent 在 underspecified/ambiguous 指令下的行为，发现交互式 disambiguation 可将性能提升高达 74%。该论文区分了 ambiguity 和 underspecificity——与本文 linguistic/specification 两层分类直接对应。这是 2026 年 top venue 发表的最直接相关工作。\n\nR1 补充：Ambig-SWE 的发现与本文 mitigation experiment（Appendix B）互补而非矛盾——本文证明 default settings 下存在 neglect，Ambig-SWE 证明 interactive 设置下可部分恢复。但不讨论这一对比会削弱 §6.2 和 Discussion 的说服力。\n\n**要求修改**：在 §2 Related Work 引用 Ambig-SWE，在 §6.2 或 §7 Discussion 讨论 interactive vs. non-interactive 设置下 disambiguation 行为的差异，在 §9 Limitations \"Disambiguation channel\" 段引用 Ambig-SWE 作为对比证据。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning]** SESOI ±15pp 缺乏外部锚定——C2 mid-tier cluster 在 ±10pp 下瓦解（仅 3/6 pairs 等价，power=0.57）。R2 指出论文已有 Table 3 七 margin 敏感性 + bootstrap cluster analysis 作为 margin-free 补充，C2 表述已为 \"robust extremes\"。但 Abstract 中 \"partial ordering\" 未附 margin 条件，§4.6 操作性论证缺部署数据支撑。**建议**：Abstract 限定 margin 条件；§4.6 承认无行业标准 SESOI。\n\n**W2 [warning]** Taxonomy 新颖性定位模糊——六类直接源自已有分类体系，排除 ellipsis/pragmatic implicature 缺乏量化依据。R1 指出论文已有定位（§3 \"experimental instrument\"、Appendix L DRIP-R 映射），核心贡献是 matched-pair evidence 而非 taxonomy 本身。**建议**：§3 增加类型选择的操作标准；明确声明 taxonomy 是实验 IV 的操作化。\n\n**W3 [warning]** Cross-judge 分配非随机化——matched-pair 差异中 judge bias 抵消仅在 additive bias 假设下成立。Appendix W 三族验证仅覆盖 ambiguous condition，judge×condition 交互效应未排除。**建议**：补充 unambiguous condition 的 cross-judge 验证或在 Limitations 中标注此假设。\n\n**W4 [warning]** Disambiguation neglect 与 ambiguity collapse 概念区分度不足——Liu et al. (2023) 和 Gur-Arieh et al. (2026) 已有 ambiguity collapse 概念。本文差异主要在 agentic context 的后果层面。**建议**：弱化 disambiguation neglect 作为独立概念的强调，定位为 ambiguity collapse 在 agentic context 下的后果验证。\n\n**W5 [warning]** 生态效度量化差距——34.0pp (τ²-bench) vs. 12.6pp (SOPBench)，5 个模型中仅 3 个达到 individual significance。Abstract/Conclusion 以 34.0pp 为 headline，未讨论自然歧义 prevalence 作为 effect-to-impact 的 scaling factor。**建议**：Abstract 或 Conclusion 中提及 SOPBench 的 +12.6pp 作为 cross-benchmark reference；Limitations 讨论 prevalence 对实际影响的调节作用。\n\n**W6 [warning]** Human validation per-type 样本量不足（n=32-34）——scopal κ CI=[0.00, 1.00] 几乎无信息量。正文 §4.4 的表述可能给 type-level reliability 过于乐观的印象。**建议**：正文更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性。\n\n**W7 [warning]** Perturbation control 仅测试 surface-level specificity——R2 指出 coreferential 类型（lexically identical, Δ=0）已提供天然的信息量控制，token count regression 方向与 information-addition 假设相反。但 token count 是粗糙代理。**建议**：Limitations 中明确指出 information-addition control 的缺失。\n\n**W8 [warning]** Variance decomposition 中 clause-level vs. type-level auditing 的 actionability 讨论不足——22.4% clause identity 中 22.0% 是 within-type 变异，clause-level auditing 在大规模文档中可能不可行；type-level auditing 仅 0.4% 方差但更可操作。**建议**：Discussion 中区分两种审计策略的成本-收益。\n\n**W9 [warning]** Bib 条目问题——yu_causal_2026 与 yu2026causal 重复条目；3 条 Anonymous 作者（disambiguation_cqa_survey_2025, atbench_2026, riskybench_2026）；tamkin_evaluating_2023 使用 @inproceedings 但 booktitle 为 arXiv。**要求修复**。\n\n**W10 [warning]** 其他可能遗漏文献——Ambig-DS (arXiv:2605.09698), Active Task Disambiguation (arXiv:2502.04485), CAR-bench (arXiv:2601.22027)。**建议**：逐条审查并按相关性纳入。\n\n**W11 [warning]** Abstract 信息密度过高——7+ 数值指标（34.0pp, OR=15.1, +18.7 to +36.0pp, 22.4% vs 0.4%, 17×, ≤11%, 41.3%）超出工作记忆容量。**建议**：精简至 3-4 个核心数值。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n\n1. **Failure mode 定义循环是核心弱点** (N1)——17× claim 的可信度受定义重叠和 LLM 编码循环性影响\n2. **Ambig-SWE 必须引用** (N2)——ICLR 2026 top venue，直接相关\n3. **方法论质量高** (Soundness 4)——matched-pair 因果设计、多层 robustness、claims 校准诚实\n4. **新颖性处于 borderline** (Excitement 3)——结果方向可预期，taxonomy 增量，disambiguation neglect 与已有概念重叠\n5. **生态效度是主要限制**——合成歧义上界 + SOPBench replication 效力偏弱\n6. **Abstract 数值密度过高**\n\n## Reviewer Divergence\n\n以下问题存在分歧（已在交叉回应中部分收敛）：\n\n1. **R1-N2 → R2 部分反驳 [REBUT]**：R1 认为 SESOI ±15pp 缺乏外部锚定是 critical must-fix；R2 认为论文已有七 margin 敏感性分析 + margin-free bootstrap cluster，处理较充分，建议降级为 should-fix 并在 Abstract 附限定条件。**Director 判断**：采纳 R2 的降级建议，列为 W1 (should-fix)——论文的 Appendix A 和 §5.2 末尾已经提供了读者在任何阈值下评估 C2 的充分信息。\n\n2. **R2-N2 → R1 反驳 [REBUT]**：R2 认为 taxonomy 新颖性不足是 critical must-fix；R1 认为论文已明确定位 taxonomy 为 experimental instrument，核心贡献是 matched-pair evidence。**Director 判断**：采纳 R1 的降级建议，列为 W2 (should-fix)——§3 和 Appendix L 的定位已经清晰，但可进一步明确类型选择的操作标准。\n\n3. **R1-W3 → R2 部分反驳 [REBUT]**：R1 认为 perturbation control 的 construct validity 不足；R2 指出 coreferential 类型和 token count regression 已部分回应。**Director 判断**：列为 W7 (should-fix)，仅需在 Limitations 中补充一句。\n\n---\n\n## Questions\n\n1. Failure mode 编码是否有人工验证子集？如果没有，是否可以在 camera-ready 前完成至少 100 traces 的人工编码？\n2. 同批 annotators 是否既创建又验证了 clause pairs？如果是，如何排除 confirmation bias？\n3. Authorization scope 的 per-type ICC ≈ 0 与其在 C4 中的 prominent role 如何调和？\n\n---\n\n## Missing References\n\n1. **Ambig-SWE** (Mou et al., ICLR 2026, arXiv:2502.13069) — [Must-Fix] agent 在 ambiguous 指令下的行为，交互式 disambiguation\n2. **Ambig-DS** (arXiv:2605.09698, 2025) — data-science agent 的 task-framing ambiguity\n3. **Active Task Disambiguation with LLMs** (arXiv:2502.04485, 2025) — 主动 disambiguation 策略\n4. **CAR-bench** (arXiv:2601.22027, 2026) — agent 不确定性下的一致性和 limit-awareness\n\n---\n\n## External Review\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check\n\n视觉审查：仍在进行中，本报告不等待。完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Overall | 3.5 | 3.5 | **3.5** |\n| Soundness | 4 | 4 | **4** |\n| Excitement | 3 | 3 | **3** |\n| Confidence | 4 | 4 | **4** |\n\n**核心判断**：方法论执行到位（Soundness 4），matched-pair 因果设计、多层 robustness checks、诚实的 claims 校准在 agent safety 文献中属上乘。但存在两个关键弱点：(1) \"17× diagnostic power\" 的核心论证存在定义循环风险，需弱化表述并区分定义驱动 vs. 经验发现的 type→mechanism 映射；(2) 遗漏了 ICLR 2026 的直接相关工作 Ambig-SWE。新颖性处于 borderline——结果方向可预期，taxonomy 增量，disambiguation neglect 与已有概念重叠度高。\n\n**接收条件**：如果作者能 (1) 弱化 17× 为定性表述并讨论定义循环，(2) 补充 Ambig-SWE 引用并讨论 interactive vs. non-interactive disambiguation，(3) 精简 Abstract 数值密度，(4) 修复 bib 条目问题，本文可达 Conference 水准（4.0）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) \"variance decomposition...combined with mutual information analysis showing that type predicts failure mechanism 17× better\" — 17× 需弱化（见 N1）\n- 建议在 contribution 声明中更突出因果设计本身作为方法论贡献\n\n### §2 Related Work\n- 缺少 Ambig-SWE (ICLR 2026) — Must-Fix N2\n- 可能遗漏 Ambig-DS, Active Task Disambiguation, CAR-bench — W10\n- \"Psycholinguistics of ambiguity processing\" 段落可引用 Ambig-SWE 作为 interactive disambiguation evidence\n\n### §3 Ambiguity Taxonomy\n- 类型选择标准 (\"frequency in operational policy documents\") 缺乏量化数据支撑 — W2\n- 建议增加一句明确声明 taxonomy 是实验 IV 的操作化而非分类标准\n\n### §4 Method\n- §4.2 同批 annotators 创建+验证的 confirmation bias 风险未讨论 — M2\n- §4.4 Human validation per-type 不确定性在正文中传达不足 — W6\n- §4.4 McNemar's test (9 vs 6 discordant pairs) 检验力有限\n- §4.5 Perturbation control 测试 surface-level specificity，information-addition control 缺失 — W7\n- §4.6 SESOI ±15pp 操作性论证缺部署数据支撑 — W1\n\n### §5 Results\n- §5.1 \"Clause wording—not type membership—drives variance\" 与 \"significant type heterogeneity (χ²=28.02, V=0.137)\" 的 juxtaposition 可加一句说明 V=0.137 对应 ~1.9% variance\n- §5.2 C2 的 \"partial ordering\" 应在 Abstract 中附 margin 条件 — W1\n- Abstract 中 \"+18.7 to +36.0pp\" 应限定为 type-level range\n\n### §6 Error Analysis\n- §6 Failure mode 定义循环性 — N1\n- §6.2 Disambiguation neglect vs. ambiguity collapse 区分度 — W4\n\n### §7 Discussion\n- \"clause-level auditing addresses the largest actionable component (22.4%)\" — 需区分 clause-level vs. type-level auditing 的可行性 — W8\n- 建议引用 Ambig-SWE 讨论 interactive disambiguation channel\n\n### §9 Limitations\n- \"Disambiguation channel\" 段应引用 Ambig-SWE 的 74% improvement 作为对比\n- Information-addition control 缺失可增加一句\n\n### References\n- 修复重复条目 (yu_causal_2026 / yu2026causal)\n- 核实 Anonymous 作者条目真实性\n- tamkin_evaluating_2023 改为 @article 类型\n\n### Appendix\n- Appendix K (Table 14) 混淆矩阵支持但也暴露定义循环问题 — 建议在正文引用时明确标注哪些映射是 definitional vs. empirical\n- Appendix W cross-judge 验证补充 unambiguous condition 会更完整 — W3",
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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "report": "# Round 20 审稿报告\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)\n## 审稿模式: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范中遇到歧义时是否会产生安全违规。作者构建了 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义分类（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes）。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（conditional OR=15.1）；(2) clause wording 解释 22.4% 方差（vs. type 仅 0.4%），但 type 预测 failure mechanism 的能力是预测违规率的 17 倍；(3) agent 对歧义的元认知意识极低（≤11%），41.3% 的歧义 clause 触发多模型趋同违规。\n\n---\n\n## Strengths\n\n**S1 [共识]** 匹配对因果设计在 agent safety 领域属方法论创新——相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的规模和匹配质量（κ=0.95）可信。\n\n**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300, Δ=-0.67pp, CI 含零）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench）、七模型跨架构复现（6 providers）。对 C1 的支撑层层递进。\n\n**S3 [共识]** \"clause wording drives risk, type predicts mechanism\" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解和 NMI 分析将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。\n\n**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive, C4 标注 exploratory；incompleteness confound 被充分讨论；authorization scope 的低可靠性被反复提示。统计方法选择与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster）。\n\n**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑。Limitations 章节覆盖五个方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（两位 Reviewer 共识）\n\n**N1 [critical, 共识]** Failure mode taxonomy 与 ambiguity taxonomy 的定义循环性\n\n\"Type predicts failure mechanism 17× more strongly than violation rate\" 是 Abstract/Discussion/Conclusion 的核心卖点之一。但三种 failure mechanisms 与 ambiguity types 存在定义层面的高度重叠：\n- Authorization scope → boundary violation（72/104 traces, 69%）：如果 authorization boundary 模糊，agent 越权就被编码为 \"boundary violation\"——这是同一现象的两种描述\n- Incompleteness → information gap-filling（70/134 traces）：信息缺失时 agent 用默认值填充，编码为 gap-filling——这是 incompleteness 的直接语义后果\n\n混淆矩阵（Table 14）显示映射并非完全 tautological（如 incompleteness 也有 43 structural misparse），但 MI 的绝对值被定义重叠抬高。此外，failure mode 编码使用 LLM 标注 LLM 失败（§6 自己承认 \"introduces circularity risk\"），编码者间一致性仅 moderate（Gwet's AC₁=0.62, κ=0.52）。论文的反驳——\"MI between exogenous type and mechanism labels provides anti-circularity evidence\"——在定义重叠面前说服力不足。\n\n**要求修改**：(1) 区分哪些 type→mechanism 映射是定义驱动的（auth scope→boundary, incompleteness→gap-filling）vs. 经验发现的（scopal→structural misparse），分别报告 MI；(2) 弱化 \"17×\" 为定性表述（如 \"substantially better\"），不再使用精确倍数作为核心卖点；(3) 对至少 100 traces 进行人工 failure mode 编码验证，或在 Limitations 中明确标注为局限。\n\n**N2 [critical, 共识]** 遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\n\nAmbig-SWE (arXiv:2502.13069) 直接研究 agent 在 underspecified/ambiguous 指令下的行为，发现交互式 disambiguation 可将性能提升高达 74%。该论文区分了 ambiguity 和 underspecificity——与本文 linguistic/specification 两层分类直接对应。这是 2026 年 top venue 发表的最直接相关工作。\n\nR1 补充：Ambig-SWE 的发现与本文 mitigation experiment（Appendix B）互补而非矛盾——本文证明 default settings 下存在 neglect，Ambig-SWE 证明 interactive 设置下可部分恢复。但不讨论这一对比会削弱 §6.2 和 Discussion 的说服力。\n\n**要求修改**：在 §2 Related Work 引用 Ambig-SWE，在 §6.2 或 §7 Discussion 讨论 interactive vs. non-interactive 设置下 disambiguation 行为的差异，在 §9 Limitations \"Disambiguation channel\" 段引用 Ambig-SWE 作为对比证据。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning]** SESOI ±15pp 缺乏外部锚定——C2 mid-tier cluster 在 ±10pp 下瓦解（仅 3/6 pairs 等价，power=0.57）。R2 指出论文已有 Table 3 七 margin 敏感性 + bootstrap cluster analysis 作为 margin-free 补充，C2 表述已为 \"robust extremes\"。但 Abstract 中 \"partial ordering\" 未附 margin 条件，§4.6 操作性论证缺部署数据支撑。**建议**：Abstract 限定 margin 条件；§4.6 承认无行业标准 SESOI。\n\n**W2 [warning]** Taxonomy 新颖性定位模糊——六类直接源自已有分类体系，排除 ellipsis/pragmatic implicature 缺乏量化依据。R1 指出论文已有定位（§3 \"experimental instrument\"、Appendix L DRIP-R 映射），核心贡献是 matched-pair evidence 而非 taxonomy 本身。**建议**：§3 增加类型选择的操作标准；明确声明 taxonomy 是实验 IV 的操作化。\n\n**W3 [warning]** Cross-judge 分配非随机化——matched-pair 差异中 judge bias 抵消仅在 additive bias 假设下成立。Appendix W 三族验证仅覆盖 ambiguous condition，judge×condition 交互效应未排除。**建议**：补充 unambiguous condition 的 cross-judge 验证或在 Limitations 中标注此假设。\n\n**W4 [warning]** Disambiguation neglect 与 ambiguity collapse 概念区分度不足——Liu et al. (2023) 和 Gur-Arieh et al. (2026) 已有 ambiguity collapse 概念。本文差异主要在 agentic context 的后果层面。**建议**：弱化 disambiguation neglect 作为独立概念的强调，定位为 ambiguity collapse 在 agentic context 下的后果验证。\n\n**W5 [warning]** 生态效度量化差距——34.0pp (τ²-bench) vs. 12.6pp (SOPBench)，5 个模型中仅 3 个达到 individual significance。Abstract/Conclusion 以 34.0pp 为 headline，未讨论自然歧义 prevalence 作为 effect-to-impact 的 scaling factor。**建议**：Abstract 或 Conclusion 中提及 SOPBench 的 +12.6pp 作为 cross-benchmark reference；Limitations 讨论 prevalence 对实际影响的调节作用。\n\n**W6 [warning]** Human validation per-type 样本量不足（n=32-34）——scopal κ CI=[0.00, 1.00] 几乎无信息量。正文 §4.4 的表述可能给 type-level reliability 过于乐观的印象。**建议**：正文更明确指出 human validation 仅支持 pooled 层面的 pipeline 可靠性。\n\n**W7 [warning]** Perturbation control 仅测试 surface-level specificity——R2 指出 coreferential 类型（lexically identical, Δ=0）已提供天然的信息量控制，token count regression 方向与 information-addition 假设相反。但 token count 是粗糙代理。**建议**：Limitations 中明确指出 information-addition control 的缺失。\n\n**W8 [warning]** Variance decomposition 中 clause-level vs. type-level auditing 的 actionability 讨论不足——22.4% clause identity 中 22.0% 是 within-type 变异，clause-level auditing 在大规模文档中可能不可行；type-level auditing 仅 0.4% 方差但更可操作。**建议**：Discussion 中区分两种审计策略的成本-收益。\n\n**W9 [warning]** Bib 条目问题——yu_causal_2026 与 yu2026causal 重复条目；3 条 Anonymous 作者（disambiguation_cqa_survey_2025, atbench_2026, riskybench_2026）；tamkin_evaluating_2023 使用 @inproceedings 但 booktitle 为 arXiv。**要求修复**。\n\n**W10 [warning]** 其他可能遗漏文献——Ambig-DS (arXiv:2605.09698), Active Task Disambiguation (arXiv:2502.04485), CAR-bench (arXiv:2601.22027)。**建议**：逐条审查并按相关性纳入。\n\n**W11 [warning]** Abstract 信息密度过高——7+ 数值指标（34.0pp, OR=15.1, +18.7 to +36.0pp, 22.4% vs 0.4%, 17×, ≤11%, 41.3%）超出工作记忆容量。**建议**：精简至 3-4 个核心数值。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n\n1. **Failure mode 定义循环是核心弱点** (N1)——17× claim 的可信度受定义重叠和 LLM 编码循环性影响\n2. **Ambig-SWE 必须引用** (N2)——ICLR 2026 top venue，直接相关\n3. **方法论质量高** (Soundness 4)——matched-pair 因果设计、多层 robustness、claims 校准诚实\n4. **新颖性处于 borderline** (Excitement 3)——结果方向可预期，taxonomy 增量，disambiguation neglect 与已有概念重叠\n5. **生态效度是主要限制**——合成歧义上界 + SOPBench replication 效力偏弱\n6. **Abstract 数值密度过高**\n\n## Reviewer Divergence\n\n以下问题存在分歧（已在交叉回应中部分收敛）：\n\n1. **R1-N2 → R2 部分反驳 [REBUT]**：R1 认为 SESOI ±15pp 缺乏外部锚定是 critical must-fix；R2 认为论文已有七 margin 敏感性分析 + margin-free bootstrap cluster，处理较充分，建议降级为 should-fix 并在 Abstract 附限定条件。**Director 判断**：采纳 R2 的降级建议，列为 W1 (should-fix)——论文的 Appendix A 和 §5.2 末尾已经提供了读者在任何阈值下评估 C2 的充分信息。\n\n2. **R2-N2 → R1 反驳 [REBUT]**：R2 认为 taxonomy 新颖性不足是 critical must-fix；R1 认为论文已明确定位 taxonomy 为 experimental instrument，核心贡献是 matched-pair evidence。**Director 判断**：采纳 R1 的降级建议，列为 W2 (should-fix)——§3 和 Appendix L 的定位已经清晰，但可进一步明确类型选择的操作标准。\n\n3. **R1-W3 → R2 部分反驳 [REBUT]**：R1 认为 perturbation control 的 construct validity 不足；R2 指出 coreferential 类型和 token count regression 已部分回应。**Director 判断**：列为 W7 (should-fix)，仅需在 Limitations 中补充一句。\n\n---\n\n## Questions\n\n1. Failure mode 编码是否有人工验证子集？如果没有，是否可以在 camera-ready 前完成至少 100 traces 的人工编码？\n2. 同批 annotators 是否既创建又验证了 clause pairs？如果是，如何排除 confirmation bias？\n3. Authorization scope 的 per-type ICC ≈ 0 与其在 C4 中的 prominent role 如何调和？\n\n---\n\n## Missing References\n\n1. **Ambig-SWE** (Mou et al., ICLR 2026, arXiv:2502.13069) — [Must-Fix] agent 在 ambiguous 指令下的行为，交互式 disambiguation\n2. **Ambig-DS** (arXiv:2605.09698, 2025) — data-science agent 的 task-framing ambiguity\n3. **Active Task Disambiguation with LLMs** (arXiv:2502.04485, 2025) — 主动 disambiguation 策略\n4. **CAR-bench** (arXiv:2601.22027, 2026) — agent 不确定性下的一致性和 limit-awareness\n\n---\n\n## External Review\n\n外部审稿：未请求（项目配置未启用）。\n\n---\n\n## Visual Layout Check\n\n视觉审查：仍在进行中，本报告不等待。完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Overall | 3.5 | 3.5 | **3.5** |\n| Soundness | 4 | 4 | **4** |\n| Excitement | 3 | 3 | **3** |\n| Confidence | 4 | 4 | **4** |\n\n**核心判断**：方法论执行到位（Soundness 4），matched-pair 因果设计、多层 robustness checks、诚实的 claims 校准在 agent safety 文献中属上乘。但存在两个关键弱点：(1) \"17× diagnostic power\" 的核心论证存在定义循环风险，需弱化表述并区分定义驱动 vs. 经验发现的 type→mechanism 映射；(2) 遗漏了 ICLR 2026 的直接相关工作 Ambig-SWE。新颖性处于 borderline——结果方向可预期，taxonomy 增量，disambiguation neglect 与已有概念重叠度高。\n\n**接收条件**：如果作者能 (1) 弱化 17× 为定性表述并讨论定义循环，(2) 补充 Ambig-SWE 引用并讨论 interactive vs. non-interactive disambiguation，(3) 精简 Abstract 数值密度，(4) 修复 bib 条目问题，本文可达 Conference 水准（4.0）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (2) \"variance decomposition...combined with mutual information analysis showing that type predicts failure mechanism 17× better\" — 17× 需弱化（见 N1）\n- 建议在 contribution 声明中更突出因果设计本身作为方法论贡献\n\n### §2 Related Work\n- 缺少 Ambig-SWE (ICLR 2026) — Must-Fix N2\n- 可能遗漏 Ambig-DS, Active Task Disambiguation, CAR-bench — W10\n- \"Psycholinguistics of ambiguity processing\" 段落可引用 Ambig-SWE 作为 interactive disambiguation evidence\n\n### §3 Ambiguity Taxonomy\n- 类型选择标准 (\"frequency in operational policy documents\") 缺乏量化数据支撑 — W2\n- 建议增加一句明确声明 taxonomy 是实验 IV 的操作化而非分类标准\n\n### §4 Method\n- §4.2 同批 annotators 创建+验证的 confirmation bias 风险未讨论 — M2\n- §4.4 Human validation per-type 不确定性在正文中传达不足 — W6\n- §4.4 McNemar's test (9 vs 6 discordant pairs) 检验力有限\n- §4.5 Perturbation control 测试 surface-level specificity，information-addition control 缺失 — W7\n- §4.6 SESOI ±15pp 操作性论证缺部署数据支撑 — W1\n\n### §5 Results\n- §5.1 \"Clause wording—not type membership—drives variance\" 与 \"significant type heterogeneity (χ²=28.02, V=0.137)\" 的 juxtaposition 可加一句说明 V=0.137 对应 ~1.9% variance\n- §5.2 C2 的 \"partial ordering\" 应在 Abstract 中附 margin 条件 — W1\n- Abstract 中 \"+18.7 to +36.0pp\" 应限定为 type-level range\n\n### §6 Error Analysis\n- §6 Failure mode 定义循环性 — N1\n- §6.2 Disambiguation neglect vs. ambiguity collapse 区分度 — W4\n\n### §7 Discussion\n- \"clause-level auditing addresses the largest actionable component (22.4%)\" — 需区分 clause-level vs. type-level auditing 的可行性 — W8\n- 建议引用 Ambig-SWE 讨论 interactive disambiguation channel\n\n### §9 Limitations\n- \"Disambiguation channel\" 段应引用 Ambig-SWE 的 74% improvement 作为对比\n- Information-addition control 缺失可增加一句\n\n### References\n- 修复重复条目 (yu_causal_2026 / yu2026causal)\n- 核实 Anonymous 作者条目真实性\n- tamkin_evaluating_2023 改为 @article 类型\n\n### Appendix\n- Appendix K (Table 14) 混淆矩阵支持但也暴露定义循环问题 — 建议在正文引用时明确标注哪些映射是 definitional vs. empirical\n- Appendix W cross-judge 验证补充 unambiguous condition 会更完整 — W3",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 1755 · 2026-05-23T02:47:06.093838+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4269
}
```

</details>

---


### Assistant

_source line 1756 · 2026-05-23T02:47:19.396496+00:00_

Round 20 审稿完成。

**最终评分：3.5 / 5（Borderline Conference）**，Soundness 4, Excitement 3, Confidence 4。两位 Reviewer 在所有维度上完全一致。

**2 个 Must-Fix**：
1. **N1**：Failure mode taxonomy 的定义循环性——"17× diagnostic power" 部分为 tautological artifact（auth scope→boundary violation, incompleteness→gap-filling），需弱化表述并区分定义驱动 vs. 经验发现的映射
2. **N2**：遗漏 Ambig-SWE (ICLR 2026)——直接相关的 top venue 工作，其交互式 disambiguation 发现与本文 neglect 叙事互补

**11 个 Should-Fix**（W1–W11），覆盖 SESOI 锚定、taxonomy 定位、cross-judge 验证、概念区分度、生态效度、human validation、perturbation control、审计 actionability、bib 修复、遗漏文献、Abstract 密度。

**接收条件**：弱化 17× claim + 补充 Ambig-SWE + 精简 Abstract + 修复 bib → 可达 4.0 (Conference)。

审稿报告和 Issue Tracker 已同步更新并投递至 Research Director。视觉审查仍在进行中，完成后会自动发送到本群。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 1757 · 2026-05-23T02:47:22.250520+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 全部问题的逐条回应。总结：

- **Must-Fix N1**（failure mode 循环性）：[AGREE]，MI 的绝对值被定义重叠抬高，建议弱化 "17×" 精确倍数
- **Must-Fix N2**（SESOI ±15pp）：[REBUT] 部分反驳——论文已展示七个 margin 敏感性和 margin-free bootstrap 分析，C2 表述已是 "partial ordering"，但同意缺乏外部锚定
- **W1-W5**：W3 部分反驳（coreferential 提供天然信息量控制），其余四项同意
- **M1-M6**：M3 反驳（方差解释量 vs. 显著性的标准区分），其余同意
- 两位 Reviewer 在 Overall 3.5、Soundness 4、Excitement 3、Confidence 4 上完全一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1758 · 2026-05-23T02:47:35.947696+00:00_

Round 20 审稿完成。

**审稿报告已投递给 Research Director。**

核心结论：

- **Overall 3.5 / 5（Borderline Conference）**，Soundness 4，Excitement 3
- 两位 Reviewer 评分完全一致，交叉回应后在关键问题上达成共识
- **2 个 Must-Fix**：(1) failure mode 定义循环性导致 "17× diagnostic power" 可信度存疑；(2) 遗漏 Ambig-SWE (ICLR 2026)
- **11 个 Should-Fix**：SESOI 外部锚定、taxonomy 定位、cross-judge 非随机化、disambiguation neglect 概念区分、生态效度、human validation 检验力、perturbation control、auditing actionability、bib 问题、遗漏文献、abstract 信息密度
- **接收路径**：弱化 17× 为定性表述 + 补充 Ambig-SWE 引用 + 精简 Abstract + 修复 bib → 可达 Conference 水准（4.0）

视觉审查仍在进行中，完成后会自动发送到本群。Issue tracker 已同步更新至 Round 20。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 170

## Round 170

60 recorded events


### User

_source line 1759 · 2026-05-23T03:20:58.593442+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-23T03:21:04.212946+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-23T03:21:04.364623+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1762 · 2026-05-23T03:21:12.249453+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-23T03:21:12.350413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1764 · 2026-05-23T03:21:18.078490+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1765 · 2026-05-23T03:21:18.179444+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-23T03:21:20.943312+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1767 · 2026-05-23T03:21:21.094364+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1768 · 2026-05-23T03:21:25.915652+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-23T03:21:25.966421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-23T03:21:30.836912+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-23T03:21:31.791285+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1772 · 2026-05-23T03:21:31.942338+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1773 · 2026-05-23T03:21:33.851347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1774 · 2026-05-23T03:21:34.153349+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1775 · 2026-05-23T03:21:34.204031+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1776 · 2026-05-23T03:21:44.308675+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found several results related to EMNLP 2026 and workshops/tutorials, but these are primarily about tutorials and co-located w
…[truncated 4503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 12366
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-23T03:21:44.309345+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/memory.md\", \"content\": \"# Memory — policy_ambiguity_safety\\n\\n## 竞品实验参考\\n（见 literature_map.yaml）\\n\\n## 经验教训\\n\\n### 5-Model Error Analysis 发现 (2026-05-21)\\n- **Layer mechanism 不是 clean dichotomy**：2-model 分析说 spec-layer = guess-and-act, linguistic-layer = misparse-and-apply。但 5-model 数据显示 conditional_precedence (spec-layer) 的 dominant FM 是 scope_misapplication（5/5 unanimous），与 linguistic-layer 一致。Failure mode 是 **type-specific** 而非 layer-specific。\\n- **Disambiguation awareness 有 model family 差异**：Claude 11.0%, GPT-4.1 10.7%（有一定 awareness），Qwen3 0%, DeepSeek 0%（完全 blind）。Overall 4.6%。\\n- **Claude conservative profile**：scope_misapplication dominant (50.5%), conservative_refusal highest (8.8%)，与低 violation rate (30.3%) 一致。\\n- **Inter-coder kappa 下降**：5-model κ=0.517 vs 2-model κ=0.594。新 3 模型的 traces 可能更难分类。\\n\\n### 已验证的模型 ID (OpenRouter proxy)\\n- `gpt-5.4` — 直接用，无 provider prefix\\n- `gpt-4.1` — 直接用\\n- `anthropic/claude-sonnet-4-6` — 需要 provider prefix\\n- `qwen/qwen3-235b-a22b` — 需要 provider prefix\\n- `deepseek/deepseek-chat-v3-0324` — 需要 provider prefix\\n- Base URL: `http://47.94.22.126/v1`\\n\\n### 运行脚本注意事项\\n- 必须用 `.venv/bin/python3` 而非系统 `python3`，因为 `core.crypto` 依赖 `cryptography` 包只在 venv 中\\n- 必须设置 `PYTHONUNBUFFERED=1` 否则 nohup 输出为空（Python stdout buffering）\\n- `core.crypto` 模块在 `/home/ubuntu/agent-ml-research/core/crypto.py`，脚本通过 `sys.path.insert(0, \\\"/home/ubuntu/agent-ml-research\\\")` 加载\\n\", \"total_chars\": 1360, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10105
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-23T03:21:49.954702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-23T03:21:50.809177+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points under controlled synthetic conditions ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of violation variance versus 0.4\% for type; however, type predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$), establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect ($\leq$11\% awareness) and \emph{systematic nocuity}: over 40\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains under synthetic ambiguity injection, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1780 · 2026-05-23T03:21:50.960485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-23T03:21:51.262428+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 1915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1782 · 2026-05-23T03:21:51.262899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-23T03:21:51.765374+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1784 · 2026-05-23T03:21:51.765750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 1785 · 2026-05-23T03:21:52.268044+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on frequency in operational policy documents and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by contextual cues within the text.
29	\emph{Scopal} ambiguity involves quantifier, negation, or modal scope interac
…[truncated 2480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-23T03:21:52.268443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1787 · 2026-05-23T03:21:52.770736+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300; Cohen's $\kappa = 0.95$ on six-type classification); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We
…[truncated 4934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-23T03:21:52.771124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-23T03:21:52.821718+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary claims; C4 is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\,pp is run-to-run stochasticity and $\sim$46\,pp systematic-but-unmeasured factors; ICC replication in Appendix~\ref{app:residual}). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count changes no type's predicted effect by more 
…[truncated 7163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-23T03:21:57.792080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-23T03:21:58.244371+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with two achieving unanimity (scopal and authorization scope).
1
…[truncated 1725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-23T03:21:58.244746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-23T03:21:58.345414+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Our results support a \emph{differential nocuity} hypothesis \citep{berry_kamsties_2004,willis_nocuous_2008}: the binary effect is domain-robust ($p = 0.187$) but type-specific profiles require per-domain calibration ($\rho = 0.26$). Of the 60.8\% unexplained variance, $\sim$15\,pp is stochastic and $\sim$46\,pp systematic (ICC $= 0.749$; Appendix~\ref{app:residual}). In customer-service domains, clause-level auditing addresses the largest \emph{actionable} component (22.4\%) but not the majority of outcome variance.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
9	
10	\paragraph{Prompt-based mitigation.}
11	Prompting is type-dependent: effective for authorization scope ($-18.0$\,pp) and lexical ($-8.9$\,pp) but not incompleteness ($-3.3$\,pp; Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes \citep{chantree_2006,ferrari_ambiguity_2019}.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1794 · 2026-05-23T03:21:58.646931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-23T03:21:59.601130+00:00_

1	\section{Conclusion}
2	
3	Under controlled synthetic conditions, policy ambiguity increases agent violations by 34.0\,pp ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of variance versus 0.4\% for type, while the taxonomy predicts failure mechanisms an order of magnitude better than violation rate. With $>$89\% disambiguation neglect and over 40\% convergent violations, clause-level auditing is critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-23T03:21:59.752053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-23T03:22:00.111275+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Ecological validity.} Our ambiguity pairs are synthetically constructed via templates (\S\ref{sec:method}), so the 34.0\,pp effect is an upper bound under controlled conditions; naturally occurring ambiguity in deployed policies may produce smaller effects. The SOPBench replication ($+$12.6\,pp), while directionally consistent, also uses researcher-constructed benchmarks. Neither study measures ambiguity prevalence in real-world policy documents; a dose-response study varying ambiguity density in production policies would help calibrate practical impact.
5	
6	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested. Cross-domain consistency holds for the overall effect (C1, interaction $p = 0.19$) and model ranking ($\rho = 0.90$, $p = 0.037$), but type rankings vary across domains ($\rho = 0.26$, $p = 0.62$); conditional precedence in particular differs by 22\,pp between retail and airline, further motivating the partial-ordering framing. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}); consequently, the confound-free lower bound ($+$18.7\,pp) rests on the primary five-model study alone.
7	
8	\paragraph{Measurement.} A cross-family judge validation (Appendix~\ref{app:cross_judge}) using GPT-4.1, Claude Sonnet~4.6, and Gemini~2.5~Pro on the same 2,997 episodes achieves Fleiss' $\kappa = 0.71
…[truncated 2443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 359
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-23T03:22:00.111703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-23T03:22:00.566385+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 37141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-23T03:22:00.566849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-23T03:22:00.617420+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 6298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-23T03:22:16.538145+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-23T03:22:18.395378+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-23T03:22:18.445988+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-23T03:22:19.401151+00:00_

## Review Issues Tracker — policy_ambiguity_safety
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle
## Latest Round: 20

# ============================================================
# R20 ISSUES — ALL RESOLVED
# ============================================================

- id: "R20-N1"
  summary: "Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  resolution: "17× → order-of-magnitude (NMI=0.23 vs 0.01 保留); §6.1 区分 2/6 definitional vs 4/6 empirical mappings (scopal→structural_misparse 82.7%)"
  resolution_round: 20
  mentions:
    - round: 20
      reviewer: "R1"
      role: "originator"
      note: "auth scope→boundary violation, incompleteness→gap-filling 是定义驱动映射"
    - round: 20
      reviewer: "R2"
      role: "cross-agree"
      note: "混淆矩阵证实定义重叠但非完全 tautological"

- id: "R20-N2"
  summary: "遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  resolution: "添加 Ambig-SWE bib 条目; §2 Related Work, §6.2, §9 Limitations 三处引用; 定位为 interactive vs default behavior 互补"
  resolution_round: 20
  mentions:
    - round: 20
      reviewer: "R2"
      role: "originator"
    - round: 20
      reviewer: "R1"
      role: "cross-agree"

- id: "R20-W1"
  summary: "SESOI ±15pp 缺乏外部锚定"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  resolution: "R21 已有 Table 3 七 margin 敏感性 + bootstrap cluster + robust extremes 定位"
  resolution_round: 20

- id: "R20-W2"
  summary: "Taxonomy 新颖性定位模糊"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  resolution: "R21 已有 §3 experimental instrument 定位 + Appendix L DRIP-R 映射"
  resolution_round: 20

- id: "R20-W3"
  summa
…[truncated 7240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-23T03:22:19.904010+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-23T03:22:20.758125+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-23T03:22:20.859067+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit format submission requirements ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit format submission requirements ARR"
  }
}
```

</details>

---


### Tool result

_source line 1809 · 2026-05-23T03:22:27.384268+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit format submission requirements ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Information For Authors | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/information/authors"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here is the information about EMNLP 2026 author guidelines:

## Page Limit and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files, and the formatting requirements are the same across all *ACL venues.

## ARR Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Authors follow a two-step process: Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; Auth
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6525
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-23T03:22:54.313446+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool call

_source line 1811 · 2026-05-23T03:22:54.765394+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1812 · 2026-05-23T03:23:14.956853+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20643
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-23T03:23:14.957308+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 20191
}
```

</details>

---


### Tool call

_source line 1814 · 2026-05-23T03:23:15.160348+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 主文 ≤8 页，参考文献不限页数，Limitations 章节必须但不计入页数\n- **审稿制度**: Double-blind\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格审查论文的**方法论严谨性**：\n\n1. **实验设计**：matched-pair design 是否足以建立因果关系？300 clause pairs × 5 models = 2,997 episodes 的统计效力是否充分？clause pair 的生成和验证过程是否可靠？\n2. **统计分析**：McNemar's test、TOST equivalence testing、variance decomposition 的使用是否恰当？多重比较校正是否充分？SESOI ±15pp 的选择是否有充分外部锚定？\n3. **评估流水线**：cross-judge design 的有效性——GPT-5.4 判 Claude/GPT-4.1/Qwen3，GPT-4.1 判 GPT-5.4/DeepSeek 是否引入系统性偏差？human validation 的样本量是否足够？\n4. **控制条件**：perturbation control ($\\Delta_{perturb} = -0.67$ pp) 是否充分？incompleteness 的 information-addition confound 是否被适当控制？\n5. **可重复性**：ICC = 0.919 的 replication 是否跨 provider 充分？温度设置 temperature=0 在不同 API 上是否真正确定性？\n6. **Error analysis 方法学**：用 LLM 编码 LLM 的 failure mode 是否存在循环性？Gwet's AC₁ = 0.62 是否足够？\n7. **Cross-benchmark replication (SOPBench)**：效应量差异（12.6pp vs 34.0pp）的解释是否合理？GPT-5.4 和 DeepSeek 不显著是否削弱泛化性声明？\n\n请按 ARR 审稿标准出具完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 critical/warning/minor 分级）、Questions to Authors、Missing References、Overall Assessment（评分 1-5，参考 EMNLP 2026 评分标准）。\n\n严格、客观、不留情面。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 主文 ≤8 页，参考文献不限页数，Limitations 章节必须但不计入页数\n- **审稿制度**: Double-blind\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格审查论文的**方法论严谨性**：\n\n1. **实验设计**：matched-pair design 是否足以建立因果关系？300 clause pairs × 5 models = 2,997 episodes 的统计效力是否充分？clause pair 的生成和验证过程是否可靠？\n2. **统计分析**：McNemar's test、TOST equivalence testing、variance decomposition 的使用是否恰当？多重比较校正是否充分？SESOI ±15pp 的选择是否有充分外部锚定？\n3. **评估流水线**：cross-judge design 的有效性——GPT-5.4 判 Claude/GPT-4.1/Qwen3，GPT-4.1 判 GPT-5.4/DeepSeek 是否引入系统性偏差？human validation 的样本量是否足够？\n4. **控制条件**：perturbation control ($\\Delta_{perturb} = -0.67$ pp) 是否充分？incompleteness 的 information-addition confound 是否被适当控制？\n5. **可重复性**：ICC = 0.919 的 replication 是否跨 provider 充分？温度设置 temperature=0 在不同 API 上是否真正确定性？\n6. **Error analysis 方法学**：用 LLM 编码 LLM 的 failure mode 是否存在循环性？Gwet's AC₁ = 0.62 是否足够？\n7. **Cross-benchmark replication (SOPBench)**：效应量差异（12.6pp vs 34.0pp）的解释是否合理？GPT-5.4 和 DeepSeek 不显著是否削弱泛化性声明？\n\n请按 ARR 审稿标准出具完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 critical/warning/minor 分级）、Questions to Authors、Missing References、Overall Assessment（评分 1-5，参考 EMNLP 2026 评分标准）。\n\n严格、客观、不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 1815 · 2026-05-23T03:23:33.251358+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18091
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-23T03:23:33.402496+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 主文 ≤8 页，参考文献不限页数，Limitations 章节必须但不计入页数\n- **审稿制度**: Double-blind\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格审查论文的**新颖性与完整性**：\n\n1. **贡献新颖性**：\n   - \"首个 matched-pair causal study of policy ambiguity's safety impact\" 这一声明是否成立？与 DRIP-R (2026) 的区分是否足够清晰？\n   - Taxonomy（6 类型、两层）相比 Li et al. (2024) 的 11 类型 NLP taxonomy 和 Massey et al. (2014) 的 6 类型 RE taxonomy，增量贡献是什么？\n   - \"Disambiguation neglect\" 概念相比 Liu et al. (2023) 的 ambiguity collapse 和 Gur-Arieh et al. (2026) 的分类，新颖性在哪里？\n   - Variance decomposition (22.4% clause vs 0.4% type) 作为 contribution 是否足够 non-trivial？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别检查 2025-2026 年的 agent safety、policy specification、ambiguity 相关论文\n   - 与 PolicyBank (2026)、AgentPex (2026)、MANTRA (2026)、PhantomPolicy (2026) 等的定位区分是否清晰？\n   - Psycholinguistics 的引用是否准确、是否过度引用？\n\n3. **论述逻辑与框架**：\n   - Introduction 的叙事是否从 gap 到 contribution 逻辑流畅？\n   - C1-C4 的 claim 层次是否清晰？primary vs exploratory 的区分是否恰当？\n   - Discussion 是否充分讨论了 implications 和 limitations？\n   - \"Nocuous\" 一词的使用是否恰当？是否与 Berry & Kamsties (2004) 的原意一致？\n\n4. **写作质量**：\n   - Abstract 信息密度是否合适？\n   - 8 页限制下主文信息分布是否合理？是否有内容应移至 appendix？\n   - 图表质量和叙事整合度\n   - 术语一致性（例如 \"nocuous\"、\"disambiguation neglect\"、\"systematic nocuity\"）\n\n5. **Limitations 章节**：\n   - 是否充分覆盖关键限制？\n   - ecological validity、domain scope、measurement 三个维度是否完整？\n\n请按 ARR 审稿标准出具完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 critical/warning/minor 分级）、Questions to Authors、Missing References、Overall Assessment（评分 1-5，参考 EMNLP 2026 评分标准）。\n\n严格、客观、不留情面。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 主文 ≤8 页，参考文献不限页数，Limitations 章节必须但不计入页数\n- **审稿制度**: Double-blind\n- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- **PDF**: `projects/policy_ambiguity_safety/artifacts/review_round_21/submitted.pdf`\n\n## 你的审查侧重\n\n请从以下维度严格审查论文的**新颖性与完整性**：\n\n1. **贡献新颖性**：\n   - \"首个 matched-pair causal study of policy ambiguity's safety impact\" 这一声明是否成立？与 DRIP-R (2026) 的区分是否足够清晰？\n   - Taxonomy（6 类型、两层）相比 Li et al. (2024) 的 11 类型 NLP taxonomy 和 Massey et al. (2014) 的 6 类型 RE taxonomy，增量贡献是什么？\n   - \"Disambiguation neglect\" 概念相比 Liu et al. (2023) 的 ambiguity collapse 和 Gur-Arieh et al. (2026) 的分类，新颖性在哪里？\n   - Variance decomposition (22.4% clause vs 0.4% type) 作为 contribution 是否足够 non-trivial？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别检查 2025-2026 年的 agent safety、policy specification、ambiguity 相关论文\n   - 与 PolicyBank (2026)、AgentPex (2026)、MANTRA (2026)、PhantomPolicy (2026) 等的定位区分是否清晰？\n   - Psycholinguistics 的引用是否准确、是否过度引用？\n\n3. **论述逻辑与框架**：\n   - Introduction 的叙事是否从 gap 到 contribution 逻辑流畅？\n   - C1-C4 的 claim 层次是否清晰？primary vs exploratory 的区分是否恰当？\n   - Discussion 是否充分讨论了 implications 和 limitations？\n   - \"Nocuous\" 一词的使用是否恰当？是否与 Berry & Kamsties (2004) 的原意一致？\n\n4. **写作质量**：\n   - Abstract 信息密度是否合适？\n   - 8 页限制下主文信息分布是否合理？是否有内容应移至 appendix？\n   - 图表质量和叙事整合度\n   - 术语一致性（例如 \"nocuous\"、\"disambiguation neglect\"、\"systematic nocuity\"）\n\n5. **Limitations 章节**：\n   - 是否充分覆盖关键限制？\n   - ecological validity、domain scope、measurement 三个维度是否完整？\n\n请按 ARR 审稿标准出具完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 critical/warning/minor 分级）、Questions to Authors、Missing References、Overall Assessment（评分 1-5，参考 EMNLP 2026 评分标准）。\n\n严格、客观、不留情面。"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-23T03:23:34.917522+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1515
}
```

</details>

---


### Assistant

_source line 1818 · 2026-05-23T03:23:45.473077+00:00_

**Round 21 圆桌审稿已启动**

| 项目 | 状态 |
|------|------|
| Venue 确认 | EMNLP 2026 via ARR May cycle, deadline 5/25, 8页限制, double-blind, ACL 模板 |
| 论文 PDF | ✅ 存在 |
| Reviewer 1（方法严谨性） | ✅ 已派发 |
| Reviewer 2（新颖性/完整性） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已派发（并行执行，不阻塞） |
| 外部审稿 | 未启用（项目配置未开启） |

等待两位 Reviewer 返回初审报告，收齐后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 1819 · 2026-05-23T03:29:39.348831+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性与完整性）

**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性与完整性

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论扎实、分析详尽的实证研究，但核心发现（歧义导致错误）缺乏超出直觉的惊喜感，分类体系为派生性贡献且层级假说未通过检验。

---

## 官方维度打分（ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 匹配对设计 + 扰动控制 + TOST + bootstrap 聚类 + 多法官交叉验证，方法论水准高。Incompleteness confound 和 cross-judge ρ=0.09 是已承认的硬伤但非致命。 |
| Excitement | 3/5 | 核心发现（歧义→违规）在直觉上可预期；方差分解（22.4% clause vs 0.4% type）和 systematic nocuity 是有趣洞察但未开辟全新研究方向。 |
| Reproducibility | 4/5 | ICC=0.919 复现性报告、完整统计规范、承诺代码/数据公开。但 τ²-bench 本身是第三方平台，clause pair 构建流程需公开后验证。 |
| Reviewer Confidence | 4/5 | 熟悉 agent safety、ambiguity processing、因果推断方法论。 |

---

## Summary

本文研究自然语言策略规范中的歧义如何因果性地影响 LLM agent 的安全行为。作者构建 300 对匹配的歧义/非歧义策略子句，注入 τ²-bench，在 5 个模型上生成 2,997 个 episode，用交叉法官评估违规严重度。主要发现：(1) 歧义增加 34.0pp 违规率（C1）；(2) 子句措辞解释 22.4% 方差 vs 类型仅 0.4%，但类型预测失败机制的 NMI 高一个数量级（0.23 vs 0.01）（C2）；(3) agent 几乎不识别歧义（≤11%，"disambiguation neglect"）；(4) 41.3% 的歧义子句触发模型趋同违规（"systematic nocuity"）。

---

## 主要优势

**S1. 严谨的因果设计**: 匹配对 + 扰动控制（Δ_perturb = -0.67pp, CI 含零）+ 复现 ICC=0.919。这是该领域方法论标杆。与 DRIP-R 的相关性设计形成鲜明对比（Section 2, "Policy specification for agents" 段）。

**S2. 统计分析全面且诚实**: TOST 等价检验跨 7 个 margin 的敏感性分析（Appendix A, Table 5）、bootstrap 聚类（Appendix E）、方差分解、Holm-Bonferroni 校正。特别值得肯定的是 C3（层级效应）未通过多重校正后被诚实降级为 "organizational convenience"。

**S3. 方差分解洞察有实践价值**: "clause wording >> type" 的发现（22.4% vs 0.4%）改变了政策审计的焦点——应关注个别子句措辞而非歧义类型分类。这对部署实践有可操作指导。

**S4. Systematic nocuity 概念有价值**: 41.3% 的子句触发 ≥3/5 模型趋同违规（Section 6.3），且 83.9% 共享同一失败模式。这指出基于一致性的评估（如多模型投票）对这类错误盲区明显。

**S5. 透明的局限讨论**: Limitations 段覆盖 ecological validity、scope、measurement、confounds、disambiguation channel 五个维度，每个维度有具体数据支撑，不回避弱点。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Taxonomy 贡献的新颖性不足以支撑其作为独立 contribution 的定位

- 具体位置：Section 3, Table 1; C2/C3 claims
- 问题：分类体系明确派生自 Li et al. (2024) 的 11 类型 NLP taxonomy 和 Massey et al. (2014) 的 6 类型 RE taxonomy（Section 3 第 1 段承认 "drawing on" 二者）。作者声称的增量贡献是 (a) 二层组织（linguistic vs specification）和 (b) 基于操作频率和理论区分度的选型。然而：
  - 层级假说 (C3) 在 Holm-Bonferroni 校正后 **未通过检验**（p=0.017, Section 5.2 末段），作者自己承认 "treated as organizational convenience"。当分类体系的核心理论创新（二层结构映射不同解析通道）无法得到统计支撑时，它退化为从已有分类中挑选 6 个类型——这是选择性重组，不是新分类体系。
  - 6 个类型的选择标准（"frequency in operational policy documents and theoretical distinctiveness"）缺乏定量依据：未报告各类型在真实策略文档中的出现频率，也未定义 "theoretical distinctiveness" 的操作化标准。
- 为什么影响接收：如果 taxonomy 不能作为独立 contribution（C3 失败），论文的 contribution 实际缩减为 (1) 匹配对因果效应的量化和 (2) 方差分解分析。这需要在 Introduction 中更审慎地定位。
- 建议修改方向：(1) 降低 taxonomy 的 contribution 定位，将其明确定位为 "实验工具"（论文 Section 2 末句已暗示这一点: "Our taxonomy serves as an experimental instrument"，但 Introduction 的 C1-C3 框架中它仍占据核心位置）；(2) 补充真实策略文档中各类型出现频率的初步统计；(3) 考虑将 C3 从主文 claim 列表中移除，或明确标注为 exploratory。

**N2** [critical] Cross-judge-group 类型排序近零相关（ρ=0.09）严重削弱 C2 partial ordering 的可信度

- 具体位置：Section 5.2, "An important qualification" 段; Appendix L
- 问题：C2 声称六类型形成 partial ordering（incompleteness > mid-tier cluster > coreferential）。但跨法官组的类型排序 Spearman ρ=0.09（p=0.87），本质上是随机的。作者将其归因于 authorization scope 的 rank reversal（GPT-4.1 组 rank 1 vs GPT-5.4 组 rank 6），排除后 ρ=0.90。但这意味着：
  - 6 类型中有 1 个类型（16.7%）的排序完全依赖法官-模型配对，而非类型本身的固有风险。
  - Authorization scope 的 per-type judge κ=0.385（Table 9），低于通常的 "fair" 标准。在低可靠度下的排序不应纳入 partial ordering 声称。
  - 即使排除 authorization scope，5 类型的 partial ordering 基本退化为 "incompleteness 最高，coreferential 最低，中间三个等价"——这是两个极端点的结论，不是一个有信息量的 ordering。
- 为什么影响接收：C2 是两个 primary claims 之一。如果 partial ordering 仅能可靠地识别两个极端（最高和最低），其实际指导价值有限。
- 建议修改方向：(1) 将 C2 的措辞从 "partial ordering" 降级为 "identifies robust extremes with an equivalent mid-tier"——论文 Section 5.2 末句已接近这一表述（"C2 establishes robust extremes...not a complete linear ordering"），但 Introduction 和 Abstract 中仍以 "partial ordering" 定位；(2) 在 Abstract/Introduction 中前置 ρ=0.09 的限定条件。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Disambiguation neglect" 的术语贡献相对于已有工作（ambiguity collapse）是渐进的

- 具体位置：Section 6.2
- 问题：Liu et al. (2023) 已经证明 LLMs 将歧义坍缩为单一解释（"ambiguity collapse"）；Gur-Arieh et al. (2026) 对此进行了分类。本文的 "disambiguation neglect" 本质上是 "ambiguity collapse in agentic settings"。Section 6.2 的区分论证为 "prior work shows LLMs collapse ambiguity... our contribution is demonstrating that this collapse persists in agentic contexts where it produces irreversible policy violations"——这是一个场景迁移论证而非概念创新。
- 建议：更明确地将 disambiguation neglect 定位为 ambiguity collapse 在 agentic 场景的实证验证（这本身有价值），而非暗示它是一个独立的新概念。

**W2** [warning] "Causal" 一词在标题和摘要中的使用可能过度声称

- 具体位置：标题 "Clause-Level Causal Effects"; Abstract "matched-pair causal study"
- 问题：因果推断的严格标准要求 (a) 随机化或 (b) 自然实验。本文使用的是**合成歧义注入**：通过模板生成歧义变体并注入 benchmark。这是一个精心设计的准实验（quasi-experiment），但不是对真实世界策略歧义的因果研究。Limitations 段（"Ecological validity" 和 "Scope"）正确地承认了合成构造的局限，但标题未反映这一限定。
- 建议：考虑将标题中的 "Causal Effects" 改为 "Controlled Effects" 或 "Experimental Effects"，或在 Abstract 中更明确地限定 "causal" 的适用范围（如 "causal under synthetic manipulation"）。匹配对设计 + 扰动控制确实支持因果推断的**内部效度**，但**外部效度**受限于合成构造。

**W3** [warning] Incompleteness 作为最高风险类型的结论受到不可消除的信息添加混淆

- 具体位置：Table 2 第一行; Section 5.1; Appendix C
- 问题：Incompleteness 的非歧义变体必然**添加策略内容**（而非仅消解歧义），造成 49.2pp 效应中包含信息添加的混淆。论文的逻辑回归控制（token count 系数正向，即更长 = 更多违规，与信息添加假说相反）和 coreferential 下界（18.7pp, 信息差异 = 0）部分缓解了问题。但：
  - Token count 是 "coarse proxy"（论文自认, Appendix C）
  - 逻辑回归的正向系数可能反映的是更长子句 = 更复杂策略 = 更多违规机会，而非否定信息添加假说
  - 排除 incompleteness 后，pooled Δ 从 34.0pp 降至 31.0pp（Section 5.1, Appendix I），主文效应量报告应更突出这一 confound-free 数字
- 建议：在 Abstract 中将核心效应量改为 confound-free range (+18.7 to +36.0pp)，将 34.0pp 降级为包含混淆的 pooled 估计。（论文 Conclusion 已经这样做了——"$+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type"——但 Abstract 仍以 34.0pp 领头。）

**W4** [warning] LLM 编码 LLM 失败模式的循环性风险未被充分缓解

- 具体位置：Section 6 第 1 段
- 问题：用 LLM 对 LLM 的违规 traces 进行失败模式编码存在固有循环性。论文提供的反循环证据是类型（外生）与机制标签的互信息（I=0.41 bits, V=0.45），但这是一个间接论证——高互信息证明的是类型与机制的关联性，不是编码的准确性。Gwet's AC₁=0.62, κ=0.52 的一致性也只是中等水平。
- 建议：补充人工验证失败模式编码的子集分析（即使小样本），或至少在 Limitations 中更明确地承认这是一个未完全解决的效度问题。（当前 Limitations 段 "Measurement" 部分提到 "human validation of a failure-mode subset would further strengthen these findings" 但语气过于轻描淡写。）

**W5** [warning] BibTeX 条目 `mou_ambigswe_2026` 作者字段疑似有误

- 具体位置：references.bib 第 443-448 行
- 问题：BibTeX key 为 `mou_ambigswe_2026`，暗示第一作者为 Mou，但 author 字段为 "Vijayvargiya, Sanidhya and Zhou, Xuhui and Yerukola, Akhila and Sap, Maarten and Neubig, Graham"。同一 bib 中 `vijayvargiya_openagentsafety_2026` 也以 Vijayvargiya 为第一作者。如果 Ambig-SWE 的真实作者确实是 Vijayvargiya 等人，则 bib key 命名有误但渲染正确；如果真实作者应为 Mou 等人，则存在引用错误。无论哪种情况，都需要核实。

---

## 小问题（不影响接收）

**M1.** Abstract 信息密度偏高，包含 5 个具体数字（34.0pp, 18.7-36.0pp, 22.4% vs 0.4%, NMI=0.23 vs 0.01, ≤11%, 40%）。建议精简至 3 个核心数字。

**M2.** 标题中 "Nocuous" 一词对非 RE 背景的读者不透明。虽然 Section 1 第 2 段有定义（引用 Berry & Kamsties 2004），但标题是读者首先看到的——考虑在 abstract 开头更早定义，或使用更通用的表述（如 "Harmful"）。

**M3.** Systematic nocuity（Section 6.3）中的 "nocuity" 与 Berry & Kamsties (2004) 原始定义的微妙偏差：原始定义中 nocuous ambiguity 是指不同利益相关者产生不同解释，而 systematic nocuity 是指模型**趋同**于同一错误解释。这不是矛盾，但值得一句话澄清。

**M4.** Figure 1 过于示意性，未添加超出文字描述的信息。考虑用更信息密集的图替换（如展示匹配对设计的具体例子 + 评估流程）。

**M5.** "Scope of 'ambiguity'" 段（Section 3 末段）承认将 vagueness、information absence 和 normative conflict 统一归入 "ambiguity"，这在语言学上是非标准的。虽然作者给出了实用主义论证（"LLM agents process all six types identically"），但这种合并可能招致语言学背景审稿人的质疑。

**M6.** Section 4.3 提到 "temperature = 0"，这对可复现性有利但不反映部署条件。Limitations 段未讨论温度对结果的影响。

---

## Questions to Authors

**Q1.** C3（层级效应）未通过 Holm-Bonferroni 校正后，你们是否考虑过将分类体系从 "two-layer taxonomy" 重新定位为 "six-type experimental instrument without strong layer claims"？如果层级区分仅是 organizational convenience，是否影响 Section 3 中 "linguistic ambiguity can be partially resolved through tool responses or world knowledge, while specification ambiguity has no external resolution channel" 这一未验证假设的保留？

**Q2.** 方差分解中 60.8% 的残差方差（其中约 46pp 是 systematic-but-unmeasured）——你们是否有假说关于这些 unmeasured factors 是什么？conversation trajectory 和 user-simulator choices 是否可以通过固定对话脚本来控制？

**Q3.** Cross-judge-group ρ=0.09 的发现是否暗示 type-level conclusions 本质上是 judge-model pairing 的 artifact？如果用三组法官（GPT-4.1, Claude, Gemini）分别评估全部 2,997 episodes 的 type rankings（而非 Appendix K 的 pooled analysis），是否能稳定 C2？

**Q4.** 排除 coreferential 后的 mitigation 和 replication 实验——这是否意味着 coreferential 的 confound-free 下界（18.7pp）缺乏跨模型验证？如果是，这是否影响您将 18.7pp 作为 confound-free lower bound 的可靠性？

---

## Missing References

1. **Cui et al. (2024)** "Risk Taxonomy, Mitigation, and Assessment Benchmarks of Large Language Model Systems" — 对 LLM 系统风险的系统性分类，与 agent safety taxonomy 直接相关。
2. **Yao et al. (2025)** "AssistantBench" — 如果存在类似 benchmark 的政策遵从评估工作应考虑引用。
3. 论文引用了 Weng et al. (2026) 关于 policy invariance 的工作，但未讨论其与 systematic nocuity 的概念关系——如果 policy invariance test 可以检测 systematic nocuity，这值得在 Discussion 中提及。

---

## Overall Assessment

**3.5 / 5 — Borderline Conference**

这是一篇方法论扎实、分析全面的实证研究，在 agent safety 领域提供了有价值的定量证据。匹配对设计、多层控制、和透明的局限讨论体现了高水准的实验科学素养。

然而，从 novelty 角度：(1) 核心发现（歧义指令导致 LLM 错误）在直觉上可预期——论文的贡献在于严格量化而非定性突破；(2) 分类体系是派生性的，且其核心理论创新（二层结构）未通过统计检验；(3) "disambiguation neglect" 相对于 "ambiguity collapse" 是场景迁移而非概念创新。

从 completeness 角度：论文覆盖面广，appendix 极为详尽（19 页 PDF 中 11 页为 appendix），展示了出色的 robustness checking 实践。Related work 覆盖面基本完整。

最终定位：methodology 和 thoroughness 达到 Conference 水平（4.0），但 novelty 和 excitement 拉低至 Findings 水平（3.0）。综合为 Borderline Conference（3.5）。若 R1/R3 对 soundness 有更严格的评价，可能降至 Findings；若对 practical impact 有更积极的评价，可能升至 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1820 · 2026-05-23T03:29:47.217499+00:00_

Reviewer 2 报告已收到（3.5/5 Borderline Conference）。等待 Reviewer 1 报告中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 1821 · 2026-05-23T03:29:52.434981+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿核心结论**：Overall 3.5/5（Borderline Conference）。

**关键发现**：
- **Soundness 4/5**：匹配对设计 + 扰动控制 + 交叉法官验证，方法论扎实
- **Excitement 3/5**：核心发现（歧义→违规）直觉可预期，variance decomposition 和 systematic nocuity 是亮点但不够突破性
- **2 个 Must-Fix**：(1) taxonomy 层级假说 C3 未通过检验，派生性分类体系定位需降级；(2) cross-judge-group ρ=0.09 严重削弱 C2 partial ordering 可信度
- **5 个 Should-Fix**：disambiguation neglect 术语新颖性有限、"causal" 可能过度声称、incompleteness confound 未完全消解、LLM 编码循环性风险、bib 条目疑似有误
- **6 个 Minor**：abstract 数字过密、"nocuous" 对非 RE 读者不透明、systematic nocuity 与原始定义微妙偏差等

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1822 · 2026-05-23T03:29:57.294516+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 173

## Round 173

6 recorded events


### User

_source line 1823 · 2026-05-23T03:33:29.899257+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 方法论严谨性（实验设计、统计分析、评估流水线、控制条件、可重复性、Error Analysis、跨基准复制）

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 核心二元效应（C1: 歧义增加违规率）实验设计扎实、统计证据充分，但类型层面claims（C2/C4）受cross-judge不一致性削弱，±15pp SESOI缺乏外部锚定，且46%未解释系统方差未获讨论，需实质修改方可达到主会议标准。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C1二元效应设计严谨（matched-pair + perturbation control + variance decomposition），但C2类型排序被cross-judge discordance（ρ=0.09）严重削弱；SESOI ±15pp无外部锚定；46%未解释系统方差未讨论 |
| Excitement | 3.5/5 | 重要且及时的研究问题（LLM agent安全），matched-pair因果设计在agent safety领域有方法论贡献；但"歧义降低安全性"这一发现本身在直觉上可预期，实际应用受限于模板化刺激的生态效度 |
| Reproducibility | 4/5 | 方法细节充分（API参数、模板构建流程、统计检验规格），承诺代码/数据公开；扣分点：温度=0跨provider的确定性语义未讨论，ICC复制仅限OpenAI系列 |
| Reviewer Confidence | 4/5 | 仔细阅读了全文19页（含附录），核查了统计方法和数值；对matched-pair设计、TOST、McNemar's test、ICC等方法较为熟悉 |
| Overall | 3.5/5 | Borderline Conference——核心因果效应（C1）可信且有贡献，但多个方法论问题（N1-N3）需实质修改；如能解决SESOI锚定和unexplained variance讨论，可达4分 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] SESOI ±15 pp 缺乏外部锚定，对安全评估场景过于宽松

- 具体位置：Section 5.2，Appendix A (Table 3)
- 问题：论文将 ±15 pp 作为 TOST 等价检验的主要 SESOI，但未提供任何外部锚定（如生产环境事故率、监管阈值、或先行研究的效应量基准）来论证为何15个百分点的违规率差异可被视为"实际等价"。在安全关键场景下，±5 pp 甚至 ±3 pp 的差异即可具有操作意义（例如违规率从5%升至10%意味着风险翻倍）。论文自身的 perturbation control 将 Δ_perturb = -0.67 pp 视为"negligible"——若 sub-1pp 即可忽略，为何等价阈值要放宽到 ±15 pp 而非 ±5 pp？
- 从 Appendix A (Table 3) 可见，在 ±5 pp 阈值下，无类型对达到等价；在 ±10 pp 下也极少。这说明论文中"仅incompleteness与其他类型可区分"的结论高度依赖于宽松阈值的选择。
- 为什么影响接收：TOST 是论文 C2（类型偏序）的核心统计工具之一。SESOI 选择直接决定哪些类型"等价"、哪些"可区分"——一个未锚定的 SESOI 使所有等价性结论变得不可靠。这不是分析细节，而是影响论文核心 claim 的方法论根基。
- 建议修改方向：(1) 从外部来源（production incident rates、r²-bench 自身的 baseline violation rate、或 agent safety 文献中的最小实际显著差异）明确锚定 SESOI；(2) 不以单一阈值为主分析，而以 ±5/±10/±15/±20 pp 全谱呈现 TOST 结果，让读者自行判断；(3) 在安全评估语境中论证为何选择的 SESOI 是"实际等价"的合理边界。

**N2** [critical] 46% 未解释系统方差（systematic-but-unmeasured）未获讨论

- 具体位置：Section 5.1，方差分解结果
- 问题：Type III 方差分解显示 residual = 60.8%，其中 "~15 pp 为 run-to-run 随机性，~46 pp 为 systematic-but-unmeasured factors"（论文原文）。也就是说，近一半的违规率方差来自论文既未测量也未讨论的系统性因素。论文重点聚焦 condition 解释的 15.8% 和 clause identity 的 22.4%，但对占比最大的系统性残差完全沉默。
- 这些因素可能是什么？对话轨迹？策略文档整体结构？多轮交互的累积效应？任务复杂度？Agent 的自修正行为？论文未做任何推测或排除。
- 为什么影响接收：论文标题声称歧义是"nocuous"的，但歧义（condition）仅解释 15.8% 的方差——不到六分之一。未知的系统性因素贡献了 3× 于歧义的方差。如果不讨论这些因素，论文给读者的印象是歧义是主要驱动因素，而事实上它是多个驱动因素之一，且可能不是最大的。
- 建议修改方向：(1) 在 Discussion 或 Results 中专门段落讨论 46% 系统性残差的候选解释；(2) 将 "nocuous" 的 claim 置于更平衡的语境中——歧义是显著且可控的驱动因素之一，但非唯一或最大的；(3) 提出后续研究方向以识别这些未测量因素。

**N3** [critical] Cross-judge 类型排序不一致性（ρ = 0.09）动摇 C2 类型偏序的可靠性

- 具体位置：Section 5.2, Appendix P
- 问题：两个 judge group（GPT-5.4 判 Claude/GPT-4.1/Qwen3 vs GPT-4.1 判 GPT-5.4/DeepSeek）对六个歧义类型的严重性排序 Spearman ρ = 0.09 (p = 0.87)，即几乎完全不一致。论文报告排除 authorization scope 后 ρ 大幅提升（≈0.90, p=0.037），但: (a) 排除后仅剩 5 个类型，n=5 的 Spearman 相关本身统计功效极低，ρ 估计值不稳定；(b) 排除一个类型即从 ρ=0.09 跳到 ρ=0.90，表明类型排序对单一 outlier 极其敏感，这本身是稳健性问题；(c) authorization scope 在论文多处分析中承担重要角色（Figure 3 中 cross-model range 最大、驱动 C4 交互效应、Table 2 中关键数据行），因此不能简单排除后继续使用其结果。
- Authorization scope 的 per-type cross-judge 二元一致性仅 κ = 0.385（Section 9），属于"fair"级别；within-judge model range 是 judge-dependent（GPT judge ≤2pp vs Claude/Gemini judges 24-30pp），说明该类型的测量本身不可靠。
- 为什么影响接收：C2（类型偏序）是论文三个 pre-registered claims 之一。如果类型排序随 judge 身份改变，那么 Section 5.2 中呈现的偏序（incompleteness → ... → corefer ential）可能是 judge assignment 的伪影，而非歧义类型的固有属性。论文将此称为"An important qualification"但仍将 C2 作为已建立的发现展示。
- 建议修改方向：(1) 采用完全交叉的 judge 设计（每个模型被两组 judge 分别评估）以分离 judge effect 和 model effect；(2) 或将 C2 明确降级为 exploratory，在 abstract/conclusion 中相应调整措辞；(3) 将 authorization scope 相关的所有 findings 标记为 "unreliable due to low cross-judge agreement"，与其他五类型的结果分开讨论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Error analysis 的 LLM 编码循环性问题（Gwet's AC₁ = 0.62）

- 具体位置：Section 6, Appendix S
- 问题：论文用 LLM 对 LLM 的 failure traces 进行五类 failure mode 编码。Gwet's AC₁ = 0.62 低于通常的"good agreement"阈值（0.80），表明编码存在相当噪声。结构性反循环论证（exogenous type 与 mechanism 的 MI = 0.41 bits）有启发性，但不够充分——LLM 编码器可能存在与 type labels 相关但与真实 failure mechanism 无关的系统性偏差。论文自身承认"human validation of a failure-mode subset would further strengthen these findings"（Section 9），但未执行。
- 建议：对至少 100 条 trace 进行人工 failure mode 编码，报告 human-LLM mechanism coding 的一致性矩阵。

**W2** [warning] SOPBench 跨基准复制：效应量大幅衰减（12.6pp vs 34.0pp），2/5 模型不显著

- 具体位置：Appendix V (Table 16)
- 问题：SOPBench 效应均值仅为主实验的 ~37%。DeepSeek 效应 +5.3pp (p=0.16) 不显著，GPT-5.4 仅边界显著 (p=0.052)。论文的解释（constraint-level vs clause-level measurement、negative task design、task structure differences）虽合理但属 post-hoc。GPT-5.4 是主实验 cross-judge 设计中的核心 judge 之一，其在 SOPBench 上仅边界显著尤其令人担忧。
- 建议：在 Results 中将 34.0pp 和 12.6pp 作为效应量范围并列报告，而非仅突出 34.0pp；讨论效应衰减对实际部署场景的启示。

**W3** [warning] Human validation 样本量不足以支持 per-type claims（n=100, 2 annotators）

- 具体位置：Section 4.4
- 问题：100 个 stratified episodes 分到 6 个类型后 per-type n ≈ 32-34。以 2 名标注员、每类型约 33 个样本计算 per-type κ 的置信区间极宽。论文声称 per-type human validation 支持 pipeline 在类型层面的效度，但 n ≈ 33 远不足以产生可靠的 per-type κ 估计。ACL/EMNLP 社区通常期望 3+ 标注员和更大的 per-category 样本。
- 建议：增加第三名标注员；每类型样本量增至 ≥50；报告 per-type κ 的置信区间。

**W4** [warning] Temperature = 0 跨 provider 的确定性假设未讨论

- 具体位置：Section 4.1
- 问题：论文设置 temperature=0, top_p=1 并隐含假设输出确定性。但不同 API provider 对 temperature=0 的实现不同——有的用 argmax、有的可能因浮点非确定性或基础设施变化引入随机性。ICC = 0.919 的复制仅在 OpenAI 系列内完成（Section 4.4），跨 provider 稳定性仅通过"CI consistency"间接推断，这是远弱于实际跨 provider 复制的证据。
- 建议：明确讨论各 provider 的 temperature=0 语义差异；报告 per-provider 的 run-to-run 方差。

**W5** [warning] Authorization scope 的 cross-judge 二元一致性仅 κ = 0.385，但其结果未被隔离

- 具体位置：Section 9 (Limitations), Figure 3, Table 2
- 问题：Authorization scope 的 cross-judge κ = 0.385 仅为"fair"，within-judge model range judge-dependent（GPT ≤2pp vs Claude/Gemini 24-30pp），但论文在 Figure 3、Table 2、Section 5.2 等处继续将 authorization scope 与其他类型并列分析。所有涉及 authorization scope 的 findings 的可靠性都因此成疑。
- 建议：在所有涉及 authorization scope 的结果旁添加显式 caveat；或在主分析中将其排除，在 Appendix 中单独报告。

---

## 小问题（不影响接收）

**M1.** 可能的数值错误：Section 4.4 报告 ICC = 0.919 with 95% CI [0.892, 0.910]——点估计 (0.919) 看似落在其自身置信区间上界 (0.910) 之外，这在数学上不可能。请核实 CI 上界是否应为 0.940 或类似数值。

**M2.** 标题 "Nocuous" 的力度与证据不完全匹配：歧义（condition）仅解释 15.8% 的方差，而 46% 来自未知系统因素。标题可能给读者过强的印象。

**M3.** NMI = 0.23 vs 0.01 的比较（Section 6）被描述为"an order of magnitude"。虽然 23× 的比值在技术上成立，但 NMI = 0.23 在绝对值上表明 type 仅解释 23% 的 mechanism 信息——这个绝对水平本身是 modest 的，建议同时报告绝对解释力。

**M4.** Section 6 中 five failure modes 的编码基于 614 条 violation traces 分布在 5 个模型 × 6 个类型 = 30 个 cell 中，per-cell 平均仅 ~20 条，部分 cell 可能极少，影响 mechanism 分析的统计稳定性。

**M5.** Tjur's R² = 0.175（Footnote 7）意味着 logistic regression 模型仅解释 ~17.5% 的违规结果方差，与方差分解中 condition (15.8%) + model (1.0%) = 16.8% 一致，但应在正文中明确承认整体预测力有限。

---

## Questions to Authors

**Q1.** 46% systematic-but-unmeasured variance 的候选解释是什么？你们是否调查过对话轨迹、策略文档长度、任务复杂度、或多轮交互深度作为潜在因素？

**Q2.** 能否提供完全交叉的 judge 分析（每个模型被两组 judge 分别评估），以分离 cross-judge type ranking discordance 中的 judge effect 和 model effect？

**Q3.** 如果将 SESOI 收紧到 ±5 pp 或 ±10 pp，TOST 结论会如何改变？哪些类型对仍能达到等价？

**Q4.** SOPBench 效应 (12.6pp) 约为 r²-bench 效应 (34.0pp) 的 1/3。你们预期真实世界效应更接近哪个数字？这对实际策略设计有什么启示？

**Q5.** 对于 Error analysis 循环性：如果换用 GPT-4.1（而非 GPT-5.4）作为 mechanism 编码器，编码结果是否会不同？你们是否测试过编码器身份效应？

---

## Missing References

- Schuirmann (1987): TOST 等价检验的原始方法论文献，论文仅引用 Lakens (2017) 的教程版本
- Riezler & Hagmann (2022): NLP 中统计显著性检验实践的反思——对论文的多重比较策略有直接相关性
- 建议考虑引用 agent safety 中关于 judge LLM 偏差的文献（如 Zheng et al. 2023 MT-Bench 中的 LLM-as-judge 位置偏差分析）

---

## 主要优势

**S1.** 严谨的 matched-pair 因果设计。以受控的单条款操纵建立因果推断，perturbation control（Δ_perturb = -0.67 pp, CI 含零）令人信服地隔离了语义歧义效应。这在 agent safety 领域是方法论贡献。

**S2.** 全面的统计工具箱。McNemar's test、TOST 等价检验（含七个阈值的敏感度分析）、Type III 方差分解、bootstrap 聚类分析、logistic regression 多方法收敛，增强了发现的可信度。

**S3.** 周到的控制条件。Perturbation control (300 episodes)、cross-judge calibration (100 episodes)、human validation (100 episodes, 2 annotators) 展示了对关键效度威胁的系统性关注。

**S4.** 跨基准复制（SOPBench）。虽然效应衰减且部分模型不显著，但主动在 r²-bench 之外的四个领域进行复制表明了对外部效度的重视，值得肯定。

**S5.** 诚实的局限性讨论。论文坦承模板化刺激产生效应上界、SESOI 可能需领域特定校准、error analysis 需人工验证——这种自我意识是积极的。

**S6.** "Type predicts mechanism, not violation rate" 的发现（NMI 0.23 vs 0.01）。这一洞察——分类学对诊断（理解HOW失败）有价值但对预后（预测WHETHER失败）无价值——是一个细致且有意义的贡献，虽然绝对解释力有限。

---

## 格式合规检查

- [x] ACL 模板：符合
- [x] Long paper 主文 ≤ 8 页：符合（Sections 1-8 结束于第 8 页底部，Limitations 不计入页数）
- [x] 参考文献不限页数：符合
- [x] Limitations 章节：存在，覆盖生态效度、测量、混淆变量等
- [x] Double-blind：未发现作者身份泄露

---

*Reviewer 1, 方法严谨性审查完成。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-23T03:34:18.610895+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性与完整性）\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Taxonomy 贡献的新颖性不足以支撑其作为独立 contribution 的定位\n- 分类体系明确派生自 Li et al. (2024) 的 11 类型 NLP taxonomy 和 Massey et al. (2014) 的 6 类型 RE taxonomy\n- 层级假说 (C3) 在 Holm-Bonferroni 校正后未通过检验（p=0.017），作者自己承认 \"treated as organizational convenience\"\n- 6 个类型的选择标准缺乏定量依据：未报告各类型在真实策略文档中的出现频率\n\n**N2** [critical] Cross-judge-group 类型排序近零相关（ρ=0.09）严重削弱 C2 partial ordering 的可信度\n- 6 类型中有 1 个类型（authorization scope, 16.7%）的排序完全依赖法官-模型配对\n- 排除 authorization scope 后 ρ=0.90，但仅剩 5 类型\n- partial ordering 实际退化为 \"incompleteness 最高，coreferential 最低，中间三个等价\"\n\n### Should-Fix 问题\n\n**W1** [warning] \"Disambiguation neglect\" 的术语贡献相对于已有工作（ambiguity collapse）是渐进的——场景迁移论证而非概念创新\n\n**W2** [warning] \"Causal\" 一词在标题和摘要中的使用可能过度声称——合成歧义注入是准实验，建议改为 \"Controlled Effects\" 或 \"Experimental Effects\"\n\n**W3** [warning] Incompleteness 作为最高风险类型的结论受到不可消除的信息添加混淆——Abstract 应以 confound-free range (+18.7 to +36.0pp) 为核心数字\n\n**W4** [warning] LLM 编码 LLM 失败模式的循环性风险未被充分缓解——Gwet's AC₁=0.62, κ=0.52 仅中等水平\n\n**W5** [warning] BibTeX 条目 `mou_ambigswe_2026` 作者字段疑似有误——bib key 暗示第一作者为 Mou，但 author 字段为 Vijayvargiya 等人\n\n### 小问题\n\n**M1.** Abstract 信息密度偏高（5个数字），建议精简至3个\n**M2.** 标题 \"Nocuous\" 对非 RE 读者不透明\n**M3.** Systematic nocuity 与 Berry & Kamsties (2004) 原始定义的微妙偏差需澄清\n**M4.** Figure 1 过于示意性\n**M5.** 将 vagueness/information absence/normative conflict 统一归入 \"ambiguity\" 在语言学上是非标准的\n**M6.** Temperature = 0 不反映部署条件，Limitations 未讨论温度影响\n\n### Missing References\n1. Cui et al. (2024) \"Risk Taxonomy, Mitigation, and Assessment Benchmarks of Large Language Model Systems\"\n2. Yao et al. (2025) \"AssistantBench\"\n3. Weng et al. (2026) 与 systematic nocuity 的概念关系未讨论\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性与完整性）\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Taxonomy 贡献的新颖性不足以支撑其作为独立 contribution 的定位\n- 分类体系明确派生自 Li et al. (2024) 的 11 类型 NLP taxonomy 和 Massey et al. (2014) 的 6 类型 RE taxonomy\n- 层级假说 (C3) 在 Holm-Bonferroni 校正后未通过检验（p=0.017），作者自己承认 \"treated as organizational convenience\"\n- 6 个类型的选择标准缺乏定量依据：未报告各类型在真实策略文档中的出现频率\n\n**N2** [critical] Cross-judge-group 类型排序近零相关（ρ=0.09）严重削弱 C2 partial ordering 的可信度\n- 6 类型中有 1 个类型（authorization scope, 16.7%）的排序完全依赖法官-模型配对\n- 排除 authorization scope 后 ρ=0.90，但仅剩 5 类型\n- partial ordering 实际退化为 \"incompleteness 最高，coreferential 最低，中间三个等价\"\n\n### Should-Fix 问题\n\n**W1** [warning] \"Disambiguation neglect\" 的术语贡献相对于已有工作（ambiguity collapse）是渐进的——场景迁移论证而非概念创新\n\n**W2** [warning] \"Causal\" 一词在标题和摘要中的使用可能过度声称——合成歧义注入是准实验，建议改为 \"Controlled Effects\" 或 \"Experimental Effects\"\n\n**W3** [warning] Incompleteness 作为最高风险类型的结论受到不可消除的信息添加混淆——Abstract 应以 confound-free range (+18.7 to +36.0pp) 为核心数字\n\n**W4** [warning] LLM 编码 LLM 失败模式的循环性风险未被充分缓解——Gwet's AC₁=0.62, κ=0.52 仅中等水平\n\n**W5** [warning] BibTeX 条目 `mou_ambigswe_2026` 作者字段疑似有误——bib key 暗示第一作者为 Mou，但 author 字段为 Vijayvargiya 等人\n\n### 小问题\n\n**M1.** Abstract 信息密度偏高（5个数字），建议精简至3个\n**M2.** 标题 \"Nocuous\" 对非 RE 读者不透明\n**M3.** Systematic nocuity 与 Berry & Kamsties (2004) 原始定义的微妙偏差需澄清\n**M4.** Figure 1 过于示意性\n**M5.** 将 vagueness/information absence/normative conflict 统一归入 \"ambiguity\" 在语言学上是非标准的\n**M6.** Temperature = 0 不反映部署条件，Limitations 未讨论温度影响\n\n### Missing References\n1. Cui et al. (2024) \"Risk Taxonomy, Mitigation, and Assessment Benchmarks of Large Language Model Systems\"\n2. Yao et al. (2025) \"AssistantBench\"\n3. Weng et al. (2026) 与 systematic nocuity 的概念关系未讨论\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-23T03:34:42.711923+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24101
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-23T03:34:43.214671+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（方法严谨性）\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] SESOI ±15 pp 缺乏外部锚定，对安全评估场景过于宽松\n- 未提供外部锚定（生产环境事故率、监管阈值、先行研究效应量基准）\n- perturbation control Δ_perturb = -0.67pp 视为 negligible，但等价阈值放宽到 ±15pp\n- 在 ±5pp 阈值下无类型对达到等价，说明结论高度依赖宽松阈值\n- TOST 是 C2 的核心统计工具，未锚定的 SESOI 使等价性结论不可靠\n\n**N2** [critical] 46% 未解释系统方差（systematic-but-unmeasured）未获讨论\n- Type III 分解 residual = 60.8%，其中约 46pp 为系统性未测量因素\n- 歧义（condition）仅解释 15.8% 方差——不到六分之一\n- 未讨论可能的候选因素（对话轨迹？策略文档整体结构？任务复杂度？）\n- 论文给读者过强印象：歧义是主要驱动因素\n\n**N3** [critical] Cross-judge 类型排序不一致性（ρ = 0.09）动摇 C2 类型偏序的可靠性\n- 排除 authorization scope 后 ρ 从 0.09 跳到 0.90，说明类型排序对单一 outlier 极其敏感\n- Authorization scope per-type κ = 0.385 仅为 \"fair\"\n- C2 是 pre-registered claims 之一，但类型排序可能是 judge assignment 的伪影\n\n### Should-Fix 问题\n\n**W1** [warning] Error analysis LLM 编码循环性（Gwet's AC₁ = 0.62 低于 \"good agreement\" 阈值 0.80），需至少 100 条 trace 人工编码\n\n**W2** [warning] SOPBench 效应量大幅衰减（12.6pp vs 34.0pp），2/5 模型不显著——GPT-5.4 仅边界显著 (p=0.052)\n\n**W3** [warning] Human validation 样本量不足（n=100, 2 annotators, per-type n≈32-34），期望 3+ 标注员\n\n**W4** [warning] Temperature = 0 跨 provider 确定性假设未讨论，ICC 复制仅限 OpenAI 系列\n\n**W5** [warning] Authorization scope κ = 0.385 结果未被隔离，仍与其他类型并列分析\n\n### 小问题\n\n**M1.** ICC CI 数值可能有误：0.919 落在 CI [0.892, 0.910] 之外\n**M2.** \"Nocuous\" 力度与证据不匹配（condition 仅解释 15.8% 方差）\n**M3.** NMI = 0.23 绝对水平 modest，建议同时报告绝对解释力\n**M4.** Failure mode per-cell 平均仅约 20 条，统计稳定性不足\n**M5.** Tjur's R² = 0.175 整体预测力有限，应在正文承认\n\n### Missing References\n- Schuirmann (1987): TOST 原始方法论文献\n- Riezler & Hagmann (2022): NLP 统计显著性检验实践反思\n- Zheng et al. (2023) MT-Bench LLM-as-judge 位置偏差分析\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告（方法严谨性）\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] SESOI ±15 pp 缺乏外部锚定，对安全评估场景过于宽松\n- 未提供外部锚定（生产环境事故率、监管阈值、先行研究效应量基准）\n- perturbation control Δ_perturb = -0.67pp 视为 negligible，但等价阈值放宽到 ±15pp\n- 在 ±5pp 阈值下无类型对达到等价，说明结论高度依赖宽松阈值\n- TOST 是 C2 的核心统计工具，未锚定的 SESOI 使等价性结论不可靠\n\n**N2** [critical] 46% 未解释系统方差（systematic-but-unmeasured）未获讨论\n- Type III 分解 residual = 60.8%，其中约 46pp 为系统性未测量因素\n- 歧义（condition）仅解释 15.8% 方差——不到六分之一\n- 未讨论可能的候选因素（对话轨迹？策略文档整体结构？任务复杂度？）\n- 论文给读者过强印象：歧义是主要驱动因素\n\n**N3** [critical] Cross-judge 类型排序不一致性（ρ = 0.09）动摇 C2 类型偏序的可靠性\n- 排除 authorization scope 后 ρ 从 0.09 跳到 0.90，说明类型排序对单一 outlier 极其敏感\n- Authorization scope per-type κ = 0.385 仅为 \"fair\"\n- C2 是 pre-registered claims 之一，但类型排序可能是 judge assignment 的伪影\n\n### Should-Fix 问题\n\n**W1** [warning] Error analysis LLM 编码循环性（Gwet's AC₁ = 0.62 低于 \"good agreement\" 阈值 0.80），需至少 100 条 trace 人工编码\n\n**W2** [warning] SOPBench 效应量大幅衰减（12.6pp vs 34.0pp），2/5 模型不显著——GPT-5.4 仅边界显著 (p=0.052)\n\n**W3** [warning] Human validation 样本量不足（n=100, 2 annotators, per-type n≈32-34），期望 3+ 标注员\n\n**W4** [warning] Temperature = 0 跨 provider 确定性假设未讨论，ICC 复制仅限 OpenAI 系列\n\n**W5** [warning] Authorization scope κ = 0.385 结果未被隔离，仍与其他类型并列分析\n\n### 小问题\n\n**M1.** ICC CI 数值可能有误：0.919 落在 CI [0.892, 0.910] 之外\n**M2.** \"Nocuous\" 力度与证据不匹配（condition 仅解释 15.8% 方差）\n**M3.** NMI = 0.23 绝对水平 modest，建议同时报告绝对解释力\n**M4.** Failure mode per-cell 平均仅约 20 条，统计稳定性不足\n**M5.** Tjur's R² = 0.175 整体预测力有限，应在正文承认\n\n### Missing References\n- Schuirmann (1987): TOST 原始方法论文献\n- Riezler & Hagmann (2022): NLP 统计显著性检验实践反思\n- Zheng et al. (2023) MT-Bench LLM-as-judge 位置偏差分析\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-23T03:34:44.624715+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 1828 · 2026-05-23T03:34:46.809276+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 174

## Round 174

2 recorded events


### User

_source line 1829 · 2026-05-23T03:34:49.366371+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分**: Overall 3.5/5 (Borderline Conference)

**三个 Must-Fix 问题**:
1. SESOI ±15pp 缺乏外部锚定——安全场景下过于宽松，直接影响 C2 类型等价性结论
2. 46% 未解释系统方差未获讨论——歧义仅解释 15.8%，但论文标题和 framing 暗示其为主要驱动因素
3. Cross-judge 类型排序不一致 (ρ=0.09)——C2 偏序可能是 judge assignment 伪影，authorization scope 的 κ=0.385 尤其不可靠

**五个 Should-Fix**: Error analysis 循环性 (AC₁=0.62)、SOPBench 效应衰减 (12.6pp vs 34.0pp)、human validation 样本量不足、temperature=0 跨 provider 假设、authorization scope 结果未隔离。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1830 · 2026-05-23T03:34:53.476696+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 175

## Round 175

2 recorded events


### User

_source line 1831 · 2026-05-23T03:37:07.520588+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Taxonomy 新颖性不足以支撑独立 contribution**

同意核心判断。分类体系确实明确派生自 Li et al. (2024) 和 Massey et al. (2014)，且 C3 层级假说在 Holm-Bonferroni 校正后仅 p=0.017，论文自身降格为 "organizational convenience"（Section 5.1）。缺乏真实策略文档中各类型出现频率的定量依据也是实质缺陷。

补充两点：(1) 论文的贡献列表（Section 1 尾部）将 taxonomy 嵌入实验设计内（"Using a six-type taxonomy...we construct 300 clause pairs"），并未将其定位为独立 contribution——R2 的批评更多针对 Section 3 的篇幅暗示而非显式 claim；(2) taxonomy 的实证价值体现在 type→mechanism 的预测力（NMI = 0.23 vs 0.01, Section 6），但 NMI = 0.23 在绝对值上仅为 modest（我在 M3 中指出），需要承认这一点。

**[AGREE] R2-N2: Cross-judge 类型排序不一致性（ρ=0.09）**

完全同意，这与我的 N3 一致。补充证据：authorization scope 的 per-type cross-judge κ = 0.385（Section 9, Limitations），within-judge model range 是 judge-dependent（GPT judge ≤2pp vs Claude/Gemini judges 24-30pp）。R2 的总结精准——partial ordering 实际退化为 "incompleteness 最高，coreferential 最低，中间等价"，且即便这一简化版本也仅基于 n=5 类型的 Spearman ρ=0.90 (p=0.037)，统计功效有限。

---

### Should-Fix 问题

**[AGREE] R2-W1: "Disambiguation neglect" 是场景迁移而非概念创新**

同意。论文 Section 6.2 定义 disambiguation neglect 为 "the absence of disambiguation in default settings, not inability"，但 Liu et al. (2023) 和 Hu et al. (2025) 已在非 agentic 场景中证明 LLM 会 collapse ambiguity into single interpretations。论文的增量贡献在于将这一现象置于 agentic context（产生不可逆策略违规），但概念本身确实是渐进的。论文可以更诚实地定位为 "extending X to agentic settings" 而非暗示原创概念。

**[REBUT] R2-W2: "Causal" 用词过度声称**

不同意。论文的 matched-pair 设计是标准的受控实验——研究者直接操纵单一变量（歧义 vs 无歧义），保持其余条款不变（Section 4.2: "minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity"），并通过 perturbation control（Δ_perturb = -0.67 pp, CI 含零, Section 4.5）隔离了语义歧义的特异性效应。

R2 将其定性为 "quasi-experimental" 是不准确的。在社会科学方法论中，quasi-experiment 指缺乏随机分配的设计（如自然实验）。本研究中，歧义操纵是研究者施加的受控 manipulation，且 matched-pair 结构消除了个体差异——这满足 experimental design 的核心要件。

"Causal" 限定于内部效度（within the experimental setting），而非外部效度（real-world generalization）。论文在 Limitations 中明确承认 "the 34.0pp effect is an upper bound under controlled conditions"（Section 8/Limitations），这正是实验因果声称的恰当边界。建议 R2 区分 internal validity（支持 causal language）和 ecological validity（论文已承认局限）。

**[AGREE] R2-W3: Abstract 应以 confound-free range 为核心**

部分同意。Abstract 确实已包含两个数字（"increasing violation rates by 34.0 percentage points...+18.7 pp excluding the confounded incompleteness type"），但 34.0pp 作为首出数字给读者留下的第一印象是含 confound 的效应。鉴于 incompleteness 的 information-addition confound 是论文自身承认的（Appendix F），将 confound-free range (+18.7 to +36.0pp) 或 confound-free lower bound (+18.7pp) 作为主要数字更为审慎。

不过我补充一点：Appendix F 的 logistic regression 表明 token count 的正系数（β = +0.027, p = 0.003）方向与 information-addition confound 预测相反（longer clauses → more violations, 而非 fewer），这意味着 confound 若存在实际上 attenuates 而非 inflates 效应。因此 34.0pp 可能是保守估计而非膨胀估计。论文应在 Abstract 或主文中更清晰地呈现这一反向 confound 论证。

**[AGREE] R2-W4: LLM 编码循环性**

同意，与我的 W1 一致。AC₁ = 0.62 低于 0.80 的 "good agreement" 阈值。结构性反循环论证（MI = 0.41 bits, Section 6）有启发性但不充分。需要人工 validation subset。

**[AGREE] R2-W5: BibTeX 条目可能有误**

同意应核实。从 PDF References（page 11）可见引用 "Vijayvargiya et al., 2026b" 对应论文 "AmbigsWE: Instructive agents to overcome underspecification..."，bib key `mou_ambigswe_2026` 暗示原始第一作者可能是 Mou 而非 Vijayvargiya——可能是引用更新后 key 未同步修改，应修正以避免 camera-ready 阶段的元数据错误。

---

### 小问题

**[AGREE] R2-M1: Abstract 信息密度偏高**

轻微同意。5 个数字（34.0pp, +18.7pp, 22.4%, 0.4%, ≥40%）确实密集，但实证论文的 abstract 承载量化结果是合理的。建议保留 3 个最核心数字（confound-free effect, variance decomposition, convergent violation rate）。

**[AGREE] R2-M2: "Nocuous" 对非 RE 读者不透明**

轻微同意。"Nocuous" 源自 Berry & Kamsties (2004) 的 RE 术语（Section 1），对纯 NLP/AI safety 读者需额外认知负担。但论文在 Introduction 第一页即定义了 nocuous vs innocuous 的区分，且该术语精确传达了论文的核心论点——歧义不是无害的。可在标题或 abstract 添加简短定义性旁注缓解。

**[AGREE] R2-M3: Systematic nocuity 定义偏差**

同意。Berry & Kamsties (2004) 原始定义中 nocuous ambiguity 指不同利益相关者对同一条款产生 divergent interpretations（导致分歧）。论文 Section 6.3 的 "systematic nocuity" 指多个 LLM 模型 convergent 于同一错误解释（41.3% majority-convergent, 13.0% unanimous）——这是相反方向的现象（convergence vs divergence）。论文应明确说明其对该术语的重新定义及与原始含义的关系。

**[REBUT] R2-M4: Figure 1 过于示意性**

部分不同意。Figure 1（page 2）在一张图中展示了完整的实验流水线（Ambiguity Taxonomy → r²-bench Evaluation → Cross-judge Assessment），包括 300 matched pairs、5 models、2,997 episodes、dual-judge pipeline 和 four-tier severity scale——这对 overview figure 而言信息密度已经合适。过度细节化反而会降低可读性。如果 R2 要求的是更具体的 clause pair 示例或 pipeline 细节，这些已在 Section 4.2 文字描述和 Appendix R (Table 12) 的 clause pair examples 中提供。

**[REBUT] R2-M5: 将 vagueness/information absence 归入 "ambiguity" 是非标准的**

不同意这是问题。论文 Section 3 开篇即显式讨论了这一定义选择："We adopt an operational definition of ambiguity following Wasow et al. (2005)"，并援引 Kennedy (2007) 对 gradient boundary（即 vagueness）的处理。对于 incompleteness，论文引用 Dalpez et al. (2018) 证明 ambiguity 和 incompleteness 在 RE 中频繁共现，并给出实证理由："LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty—and the resulting violations produce comparable safety impact despite distinct mechanisms"（Section 3）。

这一 inclusive definition 在 RE 文献中是标准做法（Berry et al., 2004; Massey et al., 2014），论文的定义选择是有意识的、有文献支撑的、有实证理由的。R2 的批评更适用于纯语言学论文，在 NLP/agent safety 场景下，操作性定义比语言学细分更有实际价值。

**[AGREE] R2-M6: Temperature = 0 与部署条件的差距**

同意，与我的 W4 一致。论文 Limitations 未讨论温度对效应量的影响。在真实部署中 temperature > 0 可能放大或缩小歧义效应（更高温度 → 更多采样多样性 → 可能触发更多/更少违规路径），这是一个重要的未探索维度。

---

### Missing References

**Cui et al. (2024)**: 同意应讨论——LLM 系统的 risk taxonomy 与本文的 ambiguity taxonomy 存在交叉，定位两者关系有助于读者理解贡献边界。

**Yao et al. (2025) AssistantBench**: 论文已引用 r²-bench (Barres et al., 2025) 作为主平台，AssistantBench 是另一个 agent benchmark。如果论文声称跨基准泛化性，确实应考虑更多基准。轻微同意。

**Weng et al. (2026)**: 同意应讨论与 systematic nocuity 的概念关系。

---

### 总结

与 R2 在 11/17 条目上达成一致（含部分同意），在 3 条目上反驳：
- **W2**（"Causal" 用词）：matched-pair 受控操纵是标准实验设计，支持因果语言
- **M4**（Figure 1）：作为 overview figure 信息密度已适当
- **M5**（inclusive ambiguity 定义）：Section 3 有显式论证和文献支撑

核心共识点：cross-judge discordance（N2/我的 N3）和 LLM 编码循环性（W4/我的 W1）是两个 Reviewer 共同识别的关键方法论问题，应优先修改。

*Reviewer 1, 交叉回应完成。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1832 · 2026-05-23T03:37:12.632643+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 176

## Round 176

2 recorded events


### User

_source line 1833 · 2026-05-23T03:37:15.161034+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。与 R2 在 11/17 条目上一致，反驳 3 条（"Causal"用词合理、Figure 1 信息密度适当、inclusive ambiguity 定义有文献支撑）。两位 Reviewer 共同识别的优先修改点：cross-judge discordance 和 LLM 编码循环性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1834 · 2026-05-23T03:37:19.618789+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 177

## Round 177

9 recorded events


### User

_source line 1835 · 2026-05-23T03:37:42.485550+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

---

**[AGREE] R1-N1: SESOI ±15pp 缺乏外部锚定**

同意这是方法论弱点。论文仅提供了两个内部锚定：(1) perturbation control bound 6.67pp 的 ">2×"（Section 4.6）；(2) "operationally meaningful: a 15pp violation-rate increase warrants distinct policy handling" 的主观论证。二者均不构成 R1 要求的外部锚定（生产事故率、监管阈值、先行研究效应量）。

但我要补充一个缓解因素：论文提供了 7 个 margin 的 TOST 敏感性分析（Appendix A, Table 5），并辅以 **margin-free 的 bootstrap 聚类分析**（Section 4.6: "We complement TOST with a margin-free bootstrap cluster analysis, Ward's method, B=10,000"）。bootstrap 结果（Appendix E）在 k=2 时 incompleteness 分离为 singleton（34.3% 的 bootstrap 样本），在 k=3 时 coreferential 额外分离——这些结论不依赖 SESOI 选择。因此 C2 的 partial ordering **极端值**（incompleteness 最高、coreferential 最低）并非完全依赖 ±15pp 阈值，但中间四类型的等价结论确实高度 margin-dependent。

总结：R1 对 SESOI 锚定缺失的批评成立，但论文的 margin-free 补充分析部分缓解了结论的 fragility。建议作者补充外部锚定（如引用 Krakovna et al. 2020 关于 specification gaming 的事故率数据），并在主文中更突出 bootstrap 聚类作为 TOST 的独立验证。

---

**[AGREE] R1-N2: 46% 未解释系统方差未获充分讨论**

同意。论文 Discussion 段 "Differential nocuity" 确实提到了这一数据："Of the 60.8% unexplained variance, ~15pp is stochastic and ~46pp systematic (ICC = 0.749; Appendix N)"，以及 "clause-level auditing addresses the largest actionable component (22.4%) but not the majority of outcome variance"——所以 R1 说 "未获讨论" 严格来说不完全准确，论文有提及但**讨论深度不足**。

我与 R1 的核心共识是：论文未列举可能的候选因素。Appendix N 中的 ICC 复制研究识别出 "specific conversation trajectories, user-simulator choices, topic interactions" 作为系统性因素，但这仅是一句话概述。作为审稿人，我期望 Discussion 中有一段专门分析：哪些 unmeasured factors 最有可能解释 46pp 系统方差？τ²-bench 的对话模拟器策略？策略文档整体长度？任务类型（退货 vs 改签）？

但我不完全同意 R1 说 "论文给读者过强印象：歧义是主要驱动因素"。论文明确将歧义的贡献标注为 "the largest actionable component (22.4%)"（Discussion 段），且在 Conclusion 中用的是 "clause-level auditing is critical"，而非 "is the primary driver"。论文的叙事定位是 "actionable"（可干预的最大组分），而非 "dominant"。这个区分是合理的。

---

**[AGREE] R1-N3: Cross-judge ρ=0.09 动摇 C2**

完全同意。这与我的 N2 完全一致。

补充 R1 未提及的一个数据点：Appendix K 的三法官验证中，type ranking 的 pairwise Spearman ρ 为 GPT–Claude=0.71, GPT–Gemini=0.77, Claude–Gemini=0.89——这些是在 **pooled across models** 后的排序，比 R1 讨论的 within-judge-group 排序（ρ=0.09）高得多。这说明 ρ=0.09 的 near-zero 相关主要来自 **judge-model pairing 的组合效应**（GPT-4.1 法官组恰好包含对 authorization scope 最脆弱的两个 agent），而非法官本身的系统性偏差。

这进一步强化了 R1 和我的共同结论：authorization scope 应从 C2 partial ordering 中隔离报告，或至少在主文中以显著的 caveat 标注。当前 Table 2 和 Figure 2 将其与其他类型并列呈现，容易误导读者。

---

### Should-Fix 问题

---

**[AGREE] R1-W1: LLM 编码循环性，需人工编码验证**

同意。这与我的 W4 一致。论文的反循环证据（type-mechanism MI = 0.41 bits）是结构性间接论证，不能替代人工验证。Gwet's AC₁ = 0.62 低于 0.80 的 "good agreement" 阈值。R1 要求 100 条 trace 人工编码是合理的标准。

---

**[REBUT] R1-W2: SOPBench 效应量衰减**

部分反驳。R1 的描述准确（12.6pp vs 34.0pp, 2/5 模型不显著），但对证据的解读过于苛刻。

关键理由：
1. **效应量衰减有系统性解释**：Appendix H 提供了三个结构性差异：(a) SOPBench 使用 constraint-level 而非 episode-level 测量，粒度更细；(b) SOPBench baseline violation rate 高（22.9% vs τ²-bench 6.9%），压缩了 ambiguity-specific delta（天花板效应）；(c) 单轮约束检查 vs 多轮客服对话。这不是效应消失，而是测量刻度不同。
2. **方向一致性是跨 benchmark 复制的核心指标**：5/5 模型方向一致（Δ > 0），3/5 达到 p < 0.01。GPT-5.4 的 p=0.052 虽未达 0.05 显著水平，但经过功率扩展（n=374 vs 原始 139），方向性信号明确。
3. **更重要的是**：R1 未提及论文还有**模型扩展复制**（Appendix D），Gemini-2.5-Flash（Δ=+33.6pp, p<10⁻²¹）和 LLaMA-4-Scout（Δ=+20.0pp, p<10⁻⁶）——这些是在 τ²-bench 内的跨架构复制，效应量完全在主研究范围内。

SOPBench 复制应被视为 "有噪声的方向性支持"，而非完整的定量复制。论文对此的定位（"suggests directional consistency", Section 5.1）是恰当的。

---

**[AGREE] R1-W3: Human validation 样本量不足**

同意。n=100, 2 annotators 是最低标准。论文自身也承认 "Per-type estimates are imprecise due to small cell sizes (n=32-34); they are descriptive statistics only"（Appendix F）。3+ annotators 且更大样本是合理期望。

但要指出：论文的 human validation 目的是验证 LLM 法官管道（pipeline validation），而非作为独立的 ground truth。Pooled κ=0.735（human-LLM）接近 inter-annotator κ=0.798——这在 pipeline validation 框架下是足够的。不足之处是 per-type 可靠性无法评估。

---

**[AGREE] R1-W4: Temperature=0 跨 provider 假设 + ICC 仅限 OpenAI**

同意。这也是我的 M6 关注点。Temperature=0 在不同 provider 实现中行为不一（部分 provider 仍有 nucleus sampling）。ICC=0.919 仅在 OpenAI 家族内计算（Section 4.5: "ICC is computed within the OpenAI family"），跨 provider 的可复现性仅由 C1 一致性间接支持。

建议作者在 Limitations 段补充 temperature=0 跨 provider 不等价性的讨论。

---

**[REBUT] R1-W5: Authorization scope 未被隔离**

部分反驳。论文实际上**已在多处隔离分析** authorization scope：
1. Section 5.3: "Excluding authorization scope, the residual model×type interaction vanishes (p=0.97; Appendix J)"——C4 交互效应已隔离。
2. Appendix L: 排除 authorization scope 后 ρ 从 0.09 升至 0.90——类型排序已隔离分析。
3. Figure 3 caption: "interpret with caution"——有明确 caveat。

R1 的 concern 更准确地说是：authorization scope **在主表（Table 2）和主图（Figure 2）中仍与其他类型并列呈现**，读者可能忽略散布在正文和 appendix 中的 caveats。这是呈现方式的问题（应在 Table 2 中加脚注或视觉标记），而非分析隔离的问题。作者已做了隔离分析，但呈现上不够显著。

---

### 小问题

---

**[REBUT] R1-M1: ICC CI 数值错误**

R1 称 "ICC = 0.919 落在 CI [0.892, 0.910] 之外"。但论文原文（Section 4.5）写的是 "ICC = 0.919 (95% CI **[0.892, 0.940]**)"——上界是 **0.940** 而非 R1 引用的 0.910。0.919 完全在 [0.892, 0.940] 范围内。R1 可能是笔误或误读。此条不成立。

---

**[REBUT] R1-M2: "Nocuous" 力度与 15.8% 方差不匹配**

反驳。"Nocuous" 在 Berry & Kamsties (2004) 中的定义是 "导致不同利益相关者产生不同解释的（因此有害的）歧义"，是一个**定性判断**（harmful vs innocuous），不是一个量化声明。论文标题 "Policy Ambiguity Is Nocuous" 声称的是 "歧义具有有害性"——这被 34.0pp 的效应量、p < 10⁻¹⁰⁵ 强力支持。

R1 的逻辑是：condition 仅解释 15.8% 方差，因此 "nocuous" 力度过强。但这混淆了 **因果效应大小**（34.0pp，巨大）与 **方差解释比例**（15.8%，中等）。一个因素可以产生巨大的因果效应但解释相对较少的总方差——这正好说明还有其他重要因素，不代表该因素本身不 harmful。类比：吸烟导致肺癌的因果效应明确且巨大，但 "是否吸烟" 在所有肺癌方差中的解释比例远低于 100%（遗传、环境等也贡献方差）。这不削弱 "吸烟有害" 的结论。

---

**[AGREE] R1-M3: NMI=0.23 绝对水平 modest**

同意。NMI=0.23 意味着类型仅解释机制标签熵的 23%——"an order of magnitude" 的表述虽然在 **相对** 意义上正确（0.23 vs 0.01 = 23×），但可能给读者留下 type-mechanism 关联很强的印象。建议论文同时报告 Cramér's V=0.45（已在 Appendix M 报告）和绝对 MI=0.41 bits，并在主文中加一句上下文化（如 "moderate but actionable association"）。

---

**[AGREE] R1-M4: Failure mode per-cell 统计稳定性**

同意。614 traces / 30 cells ≈ 20/cell，部分 cell 可能更少（如 authorization scope × structural misparse 仅 4 条，Table 14）。论文报告的 dominant failure mode 使用多数一致标准（≥3/5 models），这在 per-model 层面进一步分割了样本。但鉴于 Section 6 被标记为 "[Exploratory]"，这一局限在当前定位下可以接受。

---

**[AGREE] R1-M5: Tjur's R²=0.175 应在正文承认**

同意。当前 Tjur's R²=0.175 仅出现在 Section 5.1 脚注中，且未做解读。0.175 意味着 logistic 模型仅能解释 17.5% 的预测力——这与方差分解中 residual=60.8% 一致，应在正文中明确承认整体预测力有限。

---

### Missing References

**Schuirmann (1987)**: 引用 Lakens (2017) 已足够——Lakens 是 TOST 在行为科学中的标准现代参考，且 Lakens 本身引用了 Schuirmann。不是必须的遗漏。

**Riezler & Hagmann (2022)**: 如果存在该论文且讨论 NLP 统计实践反思，可能与本文的统计方法选择讨论相关，但不构成核心遗漏。

**Zheng et al. (2023) MT-Bench**: **论文已经引用**（references.bib: `zheng_llm_judge_2024`，即 "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023/2024）。R1 的这条遗漏指控不成立。

---

### 总结

与 R1 的核心共识：**N2（未解释方差讨论不足）和 N3（cross-judge ρ=0.09 动摇 C2）**是最严重的方法论问题。N1（SESOI 锚定）有效但被 bootstrap 补充分析部分缓解。

与 R1 的主要分歧：**W2（SOPBench 衰减）**——R1 对跨 benchmark 复制的期望过于苛刻，未考虑测量刻度差异；**M1（ICC CI 数值）**——R1 引用的 CI 上界有误；**M2（"nocuous" 力度）**——混淆了因果效应大小与方差解释比例。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-23T03:38:16.203347+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-23T03:38:16.304500+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T03:22:57.895997+00:00\", \"completed_at\": \"2026-05-23T03:26:14.339937+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，全为 Title/Abstract/Introduction 文本。Figure 1 出现在第 2 页顶部，作为视觉锚点位置可接受，但若能将 Figure 1 提至第 1 页底部则第一印象更强\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（实验流程总览图）有效传达核心方法论——三阶段 pipeline（Taxonomy → τ²-bench Evaluation → Cross-judge Assessment）。但图内子类别标签（如 Specification Layer 下的 Auth. Scope / Cond. Precedence 等）字号偏小，估计 ≤7pt，低于推荐的 8pt 最低阈值，打印后可能难以辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（六类歧义分类表）排版整洁，使用 booktabs 风格，四列布局合理。作为论文第二个 display item 位置恰当\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Method 4.1–4.4 及 Experiments/Controls 4.5–5.1），无任何 display item 穿插。作为实证型论文，Method 部分缺少方法示意图或 clause pair 构造示例图，审稿人在此段可能失去视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（per-type effect sizes 条形图）使用红蓝双色配合 95% CI error bars，色彩区分度良好，色盲友好（红 vs 蓝非红绿对比）。Caption 自包含，描述了 partial ordering 解读方式\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（violation rates by type and model）使用带色彩渐变的 heatmap 风格单元格，视觉效果好。Figure 3（violation rates heatmap）紧随其下，暖色系（黄→红）色阶清晰，且每个单元格内打印了数值——即使灰度打印仍可读取。本页 display item 密度高（1 表 + 1 图），与前两页纯文本形成对比\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 数值精度一致（1 位小数），最优结果有加粗标注，∆pp 列附 95% CI 和 p 值，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文本末页（Discussion §7 + Conclusion §8 + Limitations 开头），页面利用率 100%，无浪费空间。Limitations 段在右栏底部起始，约 4–5 行后换页，不构成孤悬问题\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 继续 + Data and Code Availability + References 开始。References 从页面中部开始，布局自然\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", \"message\": \"Referenc
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-23T03:38:16.304988+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-23T03:38:16.355491+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-23T03:38:32.318331+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null | head -20",
  "description": "Read first 20 lines of review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null | head -20",
    "description": "Read first 20 lines of review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-23T03:38:32.520537+00:00_

## Review Issues Tracker — policy_ambiguity_safety
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle
## Latest Round: 20

# ============================================================
# R20 ISSUES — ALL RESOLVED
# ============================================================

- id: "R20-N1"
  summary: "Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  resolution: "17× → order-of-magnitude (NMI=0.23 vs 0.01 保留); §6.1 区分 2/6 definitional vs 4/6 empirical mappings (scopal→structural_misparse 82.7%)"
  resolution_round: 20
  mentions:
    - round: 20

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-23T03:40:39.246722+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 21\n\n# ============================================================\n# R21 ISSUES — NEW / REOPENED\n# ============================================================\n\n- id: \"R21-N1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，对安全场景过于宽松\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R20-W1 首次提出，当时标记为 resolved（Table 3 七 margin 敏感性）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"重新提出为 critical：无外部锚定（生产事故率/监管阈值），perturbation Δ=0.67pp 视为 negligible 但 SESOI 放宽到 ±15pp 缺乏理据\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意但指出 bootstrap cluster analysis (margin-free) 部分缓解了 TOST 的 margin 依赖\"\n\n- id: \"R21-N2\"\n  summary: \"46% 未解释系统方差（systematic-but-unmeasured）讨论深度不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"condition 仅解释 15.8% 方差，46pp 系统残差未列举候选因素（对话轨迹？任务复杂度？策略文档结构？）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意讨论深度不足，但指出论文将歧义定位为 'largest actionable component' 而非 'dominant driver'，叙事定位合理\"\n\n- id: \"R21-N3\"\n  summary: \"Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"排除 auth scope 后 ρ 从 0.09 跳到 0.90，n=5 统计功效低；auth scope κ=0.385 不可靠\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"partial ordering 退化为两个极端点（incompleteness 最高，coreferential 最低），中间等价——信息量有限\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-response\"\n      note: \"补充：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，说明问题在 judge-model pairing 而非法官偏差\"\n\n- id: \"R21-N4\"\n  summary: \"Taxonomy 新颖性不足以支撑独立 contribution 定位\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 18\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R18-N3 首次提出\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"R20-W2 标记为 resolved（降格为 experimental instrument）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：C3 层级假说 p=0.017 未通过 Holm-Bonferroni，类型选择标准缺乏定量依据（无真实策略文档频率数据）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意核心判断，但指出 Introduction 的 contribution 列表未将 taxonomy 列为独立贡献\"\n\n- id: \"R21-W1\"\n  summary: \"Error analysis LLM 编码循环性（Gwet's AC₁=0.62），需人工验证子集\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"AC₁=0.62 低于 good agreement 阈值 0.80，需至少 100 条 trace 人工编码\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。MI=0.41 是间接论证，不能替代直接人工验证\"\n\n- id: \"R21-W2\"\n  summary: \"Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W4 首次提出\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：Liu et al. (2023) 已证明 LLM 坍缩歧义，本文在 agentic 场景验证，但暗示独立概念\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意。建议定位为 'extending ambiguity collapse to agentic settings'\"\n\n- id: \"R21-W3\"\n  summary: \"Abstract 应以 confound-free range (+18.7 to +36.0pp) 为核心效应量\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Abstract 以 34.0pp 领头（含 incompleteness confound），应以 confound-free range 为主数字\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"部分同意，但补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating\"\n\n- id: \"R21-W4\"\n  summary: \"Human validation 样本量不足（n=100, 2 annotators, per-type n≈32-34）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"期望 3+ 标注员，per-type ≥50 样本，当前 per-type κ CI 过宽\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意，但指出 pooled κ=0.735 对 pipeline validation 充分，不足在 per-type 层面\"\n\n- id: \"R21-W5\"\n  summary: \"Temperature=0 跨 provider 确定性假设未讨论，ICC 复制仅限 OpenAI\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"不同 provider 对 temperature=0 实现不同（argmax vs 仍有随机性）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。建议 Limitations 补充讨论\"\n\n- id: \"R21-W6\"\n  summary: \"BibTeX key mou_ambigswe_2026 与 author 字段不匹配\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"key 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"可能是引用更新后 key 未同步，应修正\"\n\n- id: \"R21-M1\"\n  summary: \"Abstract 信息密度偏高（5 个数字），建议精简至 3 个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W11 首次提出并标记 resolved\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"仍有 5 个具体数字，建议保留 confound-free effect, variance decomposition, convergent violation rate\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"轻微同意，实证 abstract 承载数字合理但可精简\"\n\n- id: \"R21-M2\"\n  summary: \"Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差需澄清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"原始定义指 divergent interpretations，论文指 convergent errors——方向相反\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意应明确说明术语重新定义\"\n\n- id: \"R21-M3\"\n  summary: \"NMI=0.23 绝对水平 modest，'order of magnitude' 表述需上下文化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"23× 比值成立但 NMI=0.23 绝对值仅为 modest\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"建议同时报告 Cramér's V=0.45 和 'moderate but actionable association'\"\n\n# ============================================================\n# R20 ISSUES — STATUS UPDATES FOR R21\n# ============================================================\n\n- id: \"R20-N1\"\n  summary: \"Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"17× → order-of-magnitude (NMI=0.23 vs 0.01 保留); §6.1 区分 2/6 definitional vs 4/6 empirical mappings\"\n  resolution_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"not re-raised\"\n      note: \"R21 未重新提出 tautological concern，但 R21-W1 提出了相关的 LLM 编码循环性问题\"\n\n- id: \"R20-N2\"\n  summary: \"遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"已添加引用\"\n  resolution_round: 20\n\n- id: \"R20-W1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N1)。七 margin 敏感性和 bootstrap 被视为有帮助但不充分\"\n\n- id: \"R20-W2\"\n  summary: \"Taxonomy 新颖性定位模糊\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N4)。experimental instrument 定位仍不够明确\"\n\n- id: \"R20-W3\"\n  summary: \"Cross-judge 分配非随机化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Cross-judge validation Fleiss κ=0.717 已添加\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"acknowledged\"\n      note: \"R21 承认 cross-judge validation 存在，但提出新问题：within-group type ranking ρ=0.09 (R21-N3)\"\n\n- id: \"R20-W4\"\n  summary: \"Disambiguation neglect 与 ambiguity collapse 概念区分度不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为场景迁移而非概念创新\"\n\n- id: \"R20-W5\"\n  summary: \"生态效度量化差距\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"'under controlled synthetic conditions' 已添加\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Human validation per-type 检验力不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"R21-W4：仍期望 3+ annotators 和更大 per-type 样本\"\n\n- id: \"R20-W7\"\n  summary: \"Perturbation control 缺 information-addition 控制\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"coreferential 天然控制 + token count regression\"\n  resolution_round: 20\n\n- id: \"R20-W8\"\n  summary: \"Clause-level vs type-level auditing actionability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"Discussion 方差全景图覆盖\"\n  resolution_round: 20\n\n- id: \"R20-W9\"\n  summary: \"Bib 条目问题：重复条目、Anonymous 作者、类型错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"主要 bib 问题已修复\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"partial\"\n      note: \"新发现 mou_ambigswe_2026 key 命名问题 (R21-W6)\"\n\n- id: \"R20-W10\"\n  summary: \"其他可能遗漏文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"核实不威胁核心 claim\"\n  resolution_round: 20\n\n- id: \"R20-W11\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-M1：仍有 5 个数字，降级为 info\"\n\n# ============================================================\n# R18-R19 RESOLVED (UNCHANGED)\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"C2 降为 secondary claim, robust extremes only.\"\n  resolution_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Cross-family judge validation κ=0.717\"\n  resolution_round: 19\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"Taxonomy 降格为 experimental instrument\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-N4：降格定位仍不够明确，C3 检验失败未在 Intro 反映\"\n\n- id: \"R18-N4\"\n  summary: \"DN 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"降级为 descriptive label\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为渐进性贡献\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"≤8 pages maintained\"\n  resolution_round: 18\n\n- id: \"R19-N1\"\n  summary: \"合成歧义生态效度不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'\"\n  resolution_round: 19\n\n- id: \"R19-N2\"\n  summary: \"非歧义纳入 ambiguity 标签\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"§3 改 'comparable safety impact despite distinct mechanisms'\"\n  resolution_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims 未充分降级\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Figure 3 caption 加 κ=0.385 + caution\"\n  resolution_round: 19\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"30× → 17× → order-of-magnitude (NMI-based)\"\n  resolution_round: 20\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test + GLMM ICC\"\n  resolution_round: 17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 21\n\n# ============================================================\n# R21 ISSUES — NEW / REOPENED\n# ============================================================\n\n- id: \"R21-N1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，对安全场景过于宽松\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R20-W1 首次提出，当时标记为 resolved（Table 3 七 margin 敏感性）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"重新提出为 critical：无外部锚定（生产事故率/监管阈值），perturbation Δ=0.67pp 视为 negligible 但 SESOI 放宽到 ±15pp 缺乏理据\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意但指出 bootstrap cluster analysis (margin-free) 部分缓解了 TOST 的 margin 依赖\"\n\n- id: \"R21-N2\"\n  summary: \"46% 未解释系统方差（systematic-but-unmeasured）讨论深度不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"condition 仅解释 15.8% 方差，46pp 系统残差未列举候选因素（对话轨迹？任务复杂度？策略文档结构？）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意讨论深度不足，但指出论文将歧义定位为 'largest actionable component' 而非 'dominant driver'，叙事定位合理\"\n\n- id: \"R21-N3\"\n  summary: \"Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"排除 auth scope 后 ρ 从 0.09 跳到 0.90，n=5 统计功效低；auth scope κ=0.385 不可靠\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"partial ordering 退化为两个极端点（incompleteness 最高，coreferential 最低），中间等价——信息量有限\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-response\"\n      note: \"补充：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，说明问题在 judge-model pairing 而非法官偏差\"\n\n- id: \"R21-N4\"\n  summary: \"Taxonomy 新颖性不足以支撑独立 contribution 定位\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 18\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R18-N3 首次提出\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"R20-W2 标记为 resolved（降格为 experimental instrument）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：C3 层级假说 p=0.017 未通过 Holm-Bonferroni，类型选择标准缺乏定量依据（无真实策略文档频率数据）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意核心判断，但指出 Introduction 的 contribution 列表未将 taxonomy 列为独立贡献\"\n\n- id: \"R21-W1\"\n  summary: \"Error analysis LLM 编码循环性（Gwet's AC₁=0.62），需人工验证子集\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"AC₁=0.62 低于 good agreement 阈值 0.80，需至少 100 条 trace 人工编码\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。MI=0.41 是间接论证，不能替代直接人工验证\"\n\n- id: \"R21-W2\"\n  summary: \"Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W4 首次提出\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：Liu et al. (2023) 已证明 LLM 坍缩歧义，本文在 agentic 场景验证，但暗示独立概念\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意。建议定位为 'extending ambiguity collapse to agentic settings'\"\n\n- id: \"R21-W3\"\n  summary: \"Abstract 应以 confound-free range (+18.7 to +36.0pp) 为核心效应量\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Abstract 以 34.0pp 领头（含 incompleteness confound），应以 confound-free range 为主数字\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"部分同意，但补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating\"\n\n- id: \"R21-W4\"\n  summary: \"Human validation 样本量不足（n=100, 2 annotators, per-type n≈32-34）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"期望 3+ 标注员，per-type ≥50 样本，当前 per-type κ CI 过宽\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意，但指出 pooled κ=0.735 对 pipeline validation 充分，不足在 per-type 层面\"\n\n- id: \"R21-W5\"\n  summary: \"Temperature=0 跨 provider 确定性假设未讨论，ICC 复制仅限 OpenAI\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"不同 provider 对 temperature=0 实现不同（argmax vs 仍有随机性）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。建议 Limitations 补充讨论\"\n\n- id: \"R21-W6\"\n  summary: \"BibTeX key mou_ambigswe_2026 与 author 字段不匹配\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"key 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"可能是引用更新后 key 未同步，应修正\"\n\n- id: \"R21-M1\"\n  summary: \"Abstract 信息密度偏高（5 个数字），建议精简至 3 个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W11 首次提出并标记 resolved\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"仍有 5 个具体数字，建议保留 confound-free effect, variance decomposition, convergent violation rate\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"轻微同意，实证 abstract 承载数字合理但可精简\"\n\n- id: \"R21-M2\"\n  summary: \"Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差需澄清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"原始定义指 divergent interpretations，论文指 convergent errors——方向相反\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意应明确说明术语重新定义\"\n\n- id: \"R21-M3\"\n  summary: \"NMI=0.23 绝对水平 modest，'order of magnitude' 表述需上下文化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"23× 比值成立但 NMI=0.23 绝对值仅为 modest\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"建议同时报告 Cramér's V=0.45 和 'moderate but actionable association'\"\n\n# ============================================================\n# R20 ISSUES — STATUS UPDATES FOR R21\n# ============================================================\n\n- id: \"R20-N1\"\n  summary: \"Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"17× → order-of-magnitude (NMI=0.23 vs 0.01 保留); §6.1 区分 2/6 definitional vs 4/6 empirical mappings\"\n  resolution_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"not re-raised\"\n      note: \"R21 未重新提出 tautological concern，但 R21-W1 提出了相关的 LLM 编码循环性问题\"\n\n- id: \"R20-N2\"\n  summary: \"遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"已添加引用\"\n  resolution_round: 20\n\n- id: \"R20-W1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N1)。七 margin 敏感性和 bootstrap 被视为有帮助但不充分\"\n\n- id: \"R20-W2\"\n  summary: \"Taxonomy 新颖性定位模糊\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N4)。experimental instrument 定位仍不够明确\"\n\n- id: \"R20-W3\"\n  summary: \"Cross-judge 分配非随机化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Cross-judge validation Fleiss κ=0.717 已添加\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"acknowledged\"\n      note: \"R21 承认 cross-judge validation 存在，但提出新问题：within-group type ranking ρ=0.09 (R21-N3)\"\n\n- id: \"R20-W4\"\n  summary: \"Disambiguation neglect 与 ambiguity collapse 概念区分度不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为场景迁移而非概念创新\"\n\n- id: \"R20-W5\"\n  summary: \"生态效度量化差距\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"'under controlled synthetic conditions' 已添加\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Human validation per-type 检验力不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"R21-W4：仍期望 3+ annotators 和更大 per-type 样本\"\n\n- id: \"R20-W7\"\n  summary: \"Perturbation control 缺 information-addition 控制\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"coreferential 天然控制 + token count regression\"\n  resolution_round: 20\n\n- id: \"R20-W8\"\n  summary: \"Clause-level vs type-level auditing actionability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"Discussion 方差全景图覆盖\"\n  resolution_round: 20\n\n- id: \"R20-W9\"\n  summary: \"Bib 条目问题：重复条目、Anonymous 作者、类型错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"主要 bib 问题已修复\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"partial\"\n      note: \"新发现 mou_ambigswe_2026 key 命名问题 (R21-W6)\"\n\n- id: \"R20-W10\"\n  summary: \"其他可能遗漏文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"核实不威胁核心 claim\"\n  resolution_round: 20\n\n- id: \"R20-W11\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-M1：仍有 5 个数字，降级为 info\"\n\n# ============================================================\n# R18-R19 RESOLVED (UNCHANGED)\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"C2 降为 secondary claim, robust extremes only.\"\n  resolution_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Cross-family judge validation κ=0.717\"\n  resolution_round: 19\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"Taxonomy 降格为 experimental instrument\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-N4：降格定位仍不够明确，C3 检验失败未在 Intro 反映\"\n\n- id: \"R18-N4\"\n  summary: \"DN 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"降级为 descriptive label\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为渐进性贡献\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"≤8 pages maintained\"\n  resolution_round: 18\n\n- id: \"R19-N1\"\n  summary: \"合成歧义生态效度不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'\"\n  resolution_round: 19\n\n- id: \"R19-N2\"\n  summary: \"非歧义纳入 ambiguity 标签\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"§3 改 'comparable safety impact despite distinct mechanisms'\"\n  resolution_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims 未充分降级\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Figure 3 caption 加 κ=0.385 + caution\"\n  resolution_round: 19\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"30× → 17× → order-of-magnitude (NMI-based)\"\n  resolution_round: 20\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test + GLMM ICC\"\n  resolution_round: 17"
  }
}
```

</details>

---


### Assistant

_source line 1843 · 2026-05-23T03:43:17.889530+00:00_

现在合成最终审稿报告并同步更新 Issue Tracker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 178

## Round 178

42 recorded events


### User

_source line 1844 · 2026-05-23T03:43:25.236073+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 全部 15 条意见的逐条回应。核心立场：

- **同意 N2, N3**（未解释方差讨论不足 + cross-judge ρ=0.09 是最严重的方法论问题）
- **同意 N1** 但指出 bootstrap 聚类分析部分缓解了 SESOI 锚定缺失
- **反驳 W2**（SOPBench 衰减有结构性解释，且模型扩展复制更有力）
- **反驳 M1**（R1 引用的 ICC CI 上界有误，实际为 0.940 非 0.910）
- **反驳 M2**（"nocuous" 是定性判断，因果效应大小 vs 方差解释比例是不同概念）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1845 · 2026-05-23T03:43:50.162856+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,get_visual_check_status,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,get_visual_check_status,get_external_review_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1846 · 2026-05-23T03:43:50.213588+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1847 · 2026-05-23T03:44:02.308875+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1848 · 2026-05-23T03:44:02.309323+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1849 · 2026-05-23T03:44:27.966654+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1850 · 2026-05-23T03:44:28.519353+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T03:22:57.895997+00:00\", \"completed_at\": \"2026-05-23T03:26:14.339937+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，全为 Title/Abstract/Introduction 文本。Figure 1 出现在第 2 页顶部，作为视觉锚点位置可接受，但若能将 Figure 1 提至第 1 页底部则第一印象更强\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（实验流程总览图）有效传达核心方法论——三阶段 pipeline（Taxonomy → τ²-bench Evaluation → Cross-judge Assessment）。但图内子类别标签（如 Specification Layer 下的 Auth. Scope / Cond. Precedence 等）字号偏小，估计 ≤7pt，低于推荐的 8pt 最低阈值，打印后可能难以辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Table 1（六类歧义分类表）排版整洁，使用 booktabs 风格，四列布局合理。作为论文第二个 display item 位置恰当\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Method 4.1–4.4 及 Experiments/Controls 4.5–5.1），无任何 display item 穿插。作为实证型论文，Method 部分缺少方法示意图或 clause pair 构造示例图，审稿人在此段可能失去视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（per-type effect sizes 条形图）使用红蓝双色配合 95% CI error bars，色彩区分度良好，色盲友好（红 vs 蓝非红绿对比）。Caption 自包含，描述了 partial ordering 解读方式\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（violation rates by type and model）使用带色彩渐变的 heatmap 风格单元格，视觉效果好。Figure 3（violation rates heatmap）紧随其下，暖色系（黄→红）色阶清晰，且每个单元格内打印了数值——即使灰度打印仍可读取。本页 display item 密度高（1 表 + 1 图），与前两页纯文本形成对比\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 数值精度一致（1 位小数），最优结果有加粗标注，∆pp 列附 95% CI 和 p 值，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文本末页（Discussion §7 + Conclusion §8 + Limitations 开头），页面利用率 100%，无浪费空间。Limitations 段在右栏底部起始，约 4–5 行后换页，不构成孤悬问题\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 继续 + Data and Code Availability + References 开始。References 从页面中部开始，布局自然\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", \"message\": \"Referenc
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1851 · 2026-05-23T03:44:28.519755+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1852 · 2026-05-23T03:44:29.021292+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1853 · 2026-05-23T03:44:29.121958+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1854 · 2026-05-23T03:44:29.223456+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1855 · 2026-05-23T03:44:32.891466+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 1856 · 2026-05-23T03:44:32.942249+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1857 · 2026-05-23T03:44:37.818351+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1858 · 2026-05-23T03:44:38.420486+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_16.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu
…[truncated 410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1859 · 2026-05-23T03:44:38.521201+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 1860 · 2026-05-23T03:44:38.621966+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1861 · 2026-05-23T03:44:41.383629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1862 · 2026-05-23T03:44:41.535049+00:00_

1	## Review Issues Tracker — policy_ambiguity_safety
2	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Latest Round: 21
5	
6	# ============================================================
7	# R21 ISSUES — NEW / REOPENED
8	# ============================================================
9	
10	- id: "R21-N1"
11	  summary: "SESOI ±15pp 缺乏外部锚定，对安全场景过于宽松"
12	  category: method
13	  severity: critical
14	  status: open
15	  first_raised_round: 20
16	  last_seen_round: 21
17	  resolution: ""
18	  resolution_round: null
19	  mentions:
20	    - round: 20
21	      reviewer: "R1"
22	      role: "originator"
23	      note: "R20-W1 首次提出，当时标记为 resolved（Table 3 七 margin 敏感性）"
24	    - round: 21
25	      reviewer: "R1"
26	      role: "originator"
27	      note: "重新提出为 critical：无外部锚定（生产事故率/监管阈值），perturbation Δ=0.67pp 视为 negligible 但 SESOI 放宽到 ±15pp 缺乏理据"
28	    - round: 21
29	      reviewer: "R2"
30	      role: "cross-agree"
31	      note: "同意但指出 bootstrap cluster analysis (margin-free) 部分缓解了 TOST 的 margin 依赖"
32	
33	- id: "R21-N2"
34	  summary: "46% 未解释系统方差（systematic-but-unmeasured）讨论深度不足"
35	  category: writing
36	  severity: critical
37	  status: open
38	  first_raised_round: 21
39	  last_seen_round: 21
40	  resolution: ""
41	  resolution_round: null
42	  mentions:
43	    - round: 21
44	      reviewer: "R1"
45	      role: "originator"
46	      note: "condition 仅解释 15.8% 方差，46pp 系统残差未列举候选因素（对话轨迹？任务复杂度？策略文档结构？）"
47	    - round: 21
48	      reviewer: "R2"
49	      role: "cross-agree"
50	      note: "同意讨论深度不足，但指出论文将歧义定位为 'largest actionable component' 而非 'dominant driver'，叙事定位合理"
51	
52	- id: "R21-N3"
53	  summary: "Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度"
54	  category: method
55	  severity: critical
56	  status: open
57	  first_raised_round: 21
58	  last_seen_round: 21
59	  resolution: ""
60	  resolution_round: null
61	  mentions:
62	    - round: 21
63	      reviewer: "R1"
64	  
…[truncated 14841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1863 · 2026-05-23T03:44:41.686044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_20.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_reports/round_20.md"
  }
}
```

</details>

---


### Tool result

_source line 1864 · 2026-05-23T03:44:41.686704+00:00_

1	---
2	round: 20
3	review_mode: fresh
4	overall_score: 3.5
5	timestamp: 2026-05-23T02:47:01.848681+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	# Round 20 审稿报告
12	## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
13	## Venue: EMNLP 2026 via ARR May cycle
14	## Reviewers: R1 (方法严谨性), R2 (新颖性与完整性)
15	## 审稿模式: Fresh (重新审稿)
16	
17	---
18	
19	## Summary
20	
21	本文研究 LLM agent 在自然语言策略规范中遇到歧义时是否会产生安全违规。作者构建了 300 对匹配的歧义/非歧义 clause pairs，涵盖六类歧义分类（两层：语言层 + 规范层），在 τ²-bench 上评估五个模型（2,997 episodes）。核心发现：(1) 歧义在合成控制条件下增加 34.0pp 违规率（conditional OR=15.1）；(2) clause wording 解释 22.4% 方差（vs. type 仅 0.4%），但 type 预测 failure mechanism 的能力是预测违规率的 17 倍；(3) agent 对歧义的元认知意识极低（≤11%），41.3% 的歧义 clause 触发多模型趋同违规。
22	
23	---
24	
25	## Strengths
26	
27	**S1 [共识]** 匹配对因果设计在 agent safety 领域属方法论创新——相比 DRIP-R 的关联性设计和 PolicyBank 的迭代优化，这是唯一提供因果证据的工作。300 clause pairs 的规模和匹配质量（κ=0.95）可信。
28	
29	**S2 [共识]** 多层 robustness 堪称全面：perturbation control（n=300, Δ=-0.67pp, CI 含零）、cross-judge 三族验证（Fleiss' κ=0.717）、cross-benchmark 复现（SOPBench）、七模型跨架构复现（6 providers）。对 C1 的支撑层层递进。
30	
31	**S3 [共识]** "clause wording drives risk, type predicts mechanism" 的双重分解是最有洞察力的发现。22.4% vs. 0.4% 的方差分解和 NMI 分析将 taxonomy 从分类标签转化为诊断工具，是有说服力的 reframing。
32	
33	**S4 [共识]** Claims 校准诚实：C3 标注 inconclusive, C4 标注 exploratory；incompleteness confound 被充分讨论；authorization scope 的低可靠性被反复提示。统计方法选择与数据结构匹配（McNemar, TOST, Holm-Bonferroni, bootstrap cluster）。
34	
35	**S5 [共识]** Appendix 深度可圈可点：19 个 appendix sections 覆盖了几乎所有可预见的 reviewer 质疑。Limitations 章节覆盖五个方面（生态效度、范围、测量、confound、disambiguation channel），坦诚且具体。
36	
37	---
38	
39	## Weaknesses
40	
41	### Must-Fix 问题（两位 Reviewer 共识）
42	
43	**N1 [critical, 共识]** Failure mode taxonomy 与 ambiguity taxonomy 的定义循环性
44	
45	"Type predicts failure mechanism 17× more strongly than violation rate" 是 Abstract/Discussion/Conclusion 的核心卖点之一。但三种 failure mechanisms 与 ambiguity types 存在定义层面的高度重叠：
46	- Authorization
…[truncated 9252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1865 · 2026-05-23T03:45:21.146425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1866 · 2026-05-23T03:45:21.598951+00:00_

1	\begin{abstract}
2	LLM-based agents increasingly operate under natural-language policy specifications that inevitably contain ambiguity. We present a matched-pair causal study on $\tau^2$-bench with 300 ambiguous/unambiguous clause pairs spanning a six-type taxonomy, evaluated across five models. Ambiguous clauses are consistently nocuous (i.e., harmful), increasing violation rates by 34.0 percentage points under controlled synthetic conditions ($+$18.7 to $+$36.0\,pp excluding the confounded incompleteness type). Clause wording explains 22.4\% of violation variance versus 0.4\% for type; however, type predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$), establishing the taxonomy as a diagnostic tool. Error analysis reveals disambiguation neglect ($\leq$11\% awareness) and \emph{systematic nocuity}: over 40\% of clauses triggering model-convergent violations. These results, observed in customer-service policy domains under synthetic ambiguity injection, motivate clause-level policy auditing and type-targeted diagnosis for policy-governed deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1867 · 2026-05-23T03:45:21.599434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1868 · 2026-05-23T03:45:21.901028+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 1915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1869 · 2026-05-23T03:45:21.901584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1870 · 2026-05-23T03:45:22.002467+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around three analyses: the binary ambiguity effect (C1), the type partial ordering (C2, including the inconclusive layer effect C3), and the model$\times$type interaction (C4). C1 and C2 are primary claims; C4 is exploratory.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, conditional OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). A Type III sum-of-squares decomposition\footnote{Type III SS avoids ordering dependence in our unbalanced design; logistic regression (Appendix~\ref{app:regression}) confirms concordant results (Tjur's $R^2 = 0.175$; \citealp{tjur_2009}).} partitions variance as: clause identity 22.4\% (0.4\% between types, 22.0\% within), model 1.0\%, condition 15.8\%, residual 60.8\% (of which $\sim$15\,pp is run-to-run stochasticity and $\sim$46\,pp systematic-but-unmeasured factors; ICC replication in Appendix~\ref{app:residual}). A permutation test ($n = 1{,}000$, shuffling within type; Appendix~\ref{app:clause_variance}) confirms the clause effect exceeds chance (null mean $= 8.3\%$, $p < 0.001$); clause-level ICC $= 0.386$ under ambiguous conditions (full-data ICC $= 0.189$). Individual clause wording---not type membership---drives clause-level variance; the omnibus test on ambiguous episodes nonetheless confirms significant type heterogeneity ($\chi^2 = 28.02$, $V = 0.137$; Table~\ref{tab:main_results}). The incompleteness effect ($+$49.2\,pp) is an upper bound that includes information addition; controlling for token count changes no type's predicted effect by more 
…[truncated 7163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1871 · 2026-05-23T03:45:27.540930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1872 · 2026-05-23T03:45:27.892753+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes (Gwet's AC$_1$ $= 0.62$, $\kappa = 0.52$ \citep{gwet_2014,cohen_1960}). Using LLMs to code LLM failures introduces circularity risk; however, mutual information between type (exogenous) and mechanism labels ($I(\text{type}; \text{mechanism}) = 0.41$ bits, $V = 0.45$; Appendix~\ref{app:type_mechanism}) provides structural evidence against this. Two of the six type--mechanism mappings reflect partial definitional affinity (authorization scope$\to$boundary violation, incompleteness$\to$gap-filling); the remaining four (e.g., scopal$\to$structural misparse, 82.7\% cross-model consistency) are empirically derived.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse}: the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral level. Dominates scopal (5/5 models), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling}: the agent fills missing information with plausible but incorrect defaults. Dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation}: the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial). Dominates authorization scope exclusively (5/5).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models), with two achieving unanimity (scopal and authorization scope).
1
…[truncated 1725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1873 · 2026-05-23T03:45:27.893246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1874 · 2026-05-23T03:45:28.245841+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Our results support a \emph{differential nocuity} hypothesis \citep{berry_kamsties_2004,willis_nocuous_2008}: the binary effect is domain-robust ($p = 0.187$) but type-specific profiles require per-domain calibration ($\rho = 0.26$). Of the 60.8\% unexplained variance, $\sim$15\,pp is stochastic and $\sim$46\,pp systematic (ICC $= 0.749$; Appendix~\ref{app:residual}). In customer-service domains, clause-level auditing addresses the largest \emph{actionable} component (22.4\%) but not the majority of outcome variance.
6	
7	\paragraph{Taxonomy as diagnostic tool.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for clause wording; however, it predicts failure \emph{mechanism} an order of magnitude more strongly than violation rate (NMI $= 0.23$ vs.\ $0.01$; Appendix~\ref{app:type_mechanism}), validating the taxonomy as a diagnostic tool: each type maps to a dominant failure mechanism (\S\ref{sec:analysis}).
9	
10	\paragraph{Prompt-based mitigation.}
11	Prompting is type-dependent: effective for authorization scope ($-18.0$\,pp) and lexical ($-8.9$\,pp) but not incompleteness ($-3.3$\,pp; Appendix~\ref{app:mitigation}), reinforcing policy-design over prompt-level fixes \citep{chantree_2006,ferrari_ambiguity_2019}.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1875 · 2026-05-23T03:45:28.246248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1876 · 2026-05-23T03:45:28.296745+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Ecological validity.} Our ambiguity pairs are synthetically constructed via templates (\S\ref{sec:method}), so the 34.0\,pp effect is an upper bound under controlled conditions; naturally occurring ambiguity in deployed policies may produce smaller effects. The SOPBench replication ($+$12.6\,pp), while directionally consistent, also uses researcher-constructed benchmarks. Neither study measures ambiguity prevalence in real-world policy documents; a dose-response study varying ambiguity density in production policies would help calibrate practical impact.
5	
6	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested. Cross-domain consistency holds for the overall effect (C1, interaction $p = 0.19$) and model ranking ($\rho = 0.90$, $p = 0.037$), but type rankings vary across domains ($\rho = 0.26$, $p = 0.62$); conditional precedence in particular differs by 22\,pp between retail and airline, further motivating the partial-ordering framing. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}); consequently, the confound-free lower bound ($+$18.7\,pp) rests on the primary five-model study alone.
7	
8	\paragraph{Measurement.} A cross-family judge validation (Appendix~\ref{app:cross_judge}) using GPT-4.1, Claude Sonnet~4.6, and Gemini~2.5~Pro on the same 2,997 episodes achieves Fleiss' $\kappa = 0.71
…[truncated 2443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1877 · 2026-05-23T03:46:20.980692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1878 · 2026-05-23T03:46:21.332256+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. \citet{kamath_scope_2024} investigate scopal ambiguity in LLMs, finding systematic preferences for surface scope. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous. Our taxonomy serves as an experimental instrument for controlled causal analysis rather than a proposed classification standard.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_l
…[truncated 4039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1879 · 2026-05-23T03:46:21.382859+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1880 · 2026-05-23T03:46:21.484090+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 6685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1881 · 2026-05-23T03:48:48.316573+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 21\n\n# ============================================================\n# R21 ISSUES — FINAL (POST CROSS-RESPONSE)\n# ============================================================\n\n- id: \"R21-N1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，对安全场景过于宽松\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R20-W1 首次提出，当时标记为 resolved（Table 3 七 margin 敏感性）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"重新提出为 critical：无外部锚定（生产事故率/监管阈值），perturbation Δ=0.67pp 视为 negligible 但 SESOI 放宽到 ±15pp 缺乏理据\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意但指出 bootstrap cluster analysis (margin-free) 部分缓解了 TOST 的 margin 依赖\"\n  cross_response_status: \"converged — both agree, R2 notes partial mitigation via bootstrap\"\n\n- id: \"R21-N2\"\n  summary: \"46% 未解释系统方差（systematic-but-unmeasured）讨论深度不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"condition 仅解释 15.8% 方差，46pp 系统残差未列举候选因素（对话轨迹？任务复杂度？策略文档结构？）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意讨论深度不足，但指出论文将歧义定位为 'largest actionable component' 而非 'dominant driver'，叙事定位合理\"\n  cross_response_status: \"converged — both agree on insufficient discussion, R2 endorses narrative framing\"\n\n- id: \"R21-N3\"\n  summary: \"Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"排除 auth scope 后 ρ 从 0.09 跳到 0.90，n=5 统计功效低；auth scope κ=0.385 不可靠\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"partial ordering 退化为两个极端点（incompleteness 最高，coreferential 最低），中间等价——信息量有限\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-response\"\n      note: \"补充：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，说明问题在 judge-model pairing 而非法官偏差\"\n  cross_response_status: \"converged — both agree C2 limited to extremes; R2 adds pooled ρ context\"\n\n- id: \"R21-N4\"\n  summary: \"Taxonomy 新颖性不足以支撑独立 contribution 定位\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 18\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R18-N3 首次提出\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"R20-W2 标记为 resolved（降格为 experimental instrument）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：C3 层级假说 p=0.017 未通过 Holm-Bonferroni，类型选择标准缺乏定量依据（无真实策略文档频率数据）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意核心判断，但指出 Introduction 的 contribution 列表未将 taxonomy 列为独立贡献\"\n  cross_response_status: \"converged — both agree taxonomy not standalone; R1 notes Intro already avoids claiming it\"\n\n- id: \"R21-W1\"\n  summary: \"Error analysis LLM 编码循环性（Gwet's AC₁=0.62），需人工验证子集\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"AC₁=0.62 低于 good agreement 阈值 0.80，需至少 100 条 trace 人工编码\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。MI=0.41 是间接论证，不能替代直接人工验证\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-W2\"\n  summary: \"Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W4 首次提出\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：Liu et al. (2023) 已证明 LLM 坍缩歧义，本文在 agentic 场景验证，但暗示独立概念\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意。建议定位为 'extending ambiguity collapse to agentic settings'\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-W3\"\n  summary: \"Abstract 应以 confound-free range (+18.7 to +36.0pp) 为核心效应量\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Abstract 以 34.0pp 领头（含 incompleteness confound），应以 confound-free range 为主数字\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"部分同意，但补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating\"\n  cross_response_status: \"converged — partial agree, R1 adds attenuating-confound nuance\"\n\n- id: \"R21-W4\"\n  summary: \"Human validation 样本量不足（n=100, 2 annotators, per-type n≈32-34）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"期望 3+ 标注员，per-type ≥50 样本，当前 per-type κ CI 过宽\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意，但指出 pooled κ=0.735 对 pipeline validation 充分，不足在 per-type 层面\"\n  cross_response_status: \"converged — both agree pooled sufficient, per-type insufficient\"\n\n- id: \"R21-W5\"\n  summary: \"Temperature=0 跨 provider 确定性假设未讨论，ICC 复制仅限 OpenAI\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"不同 provider 对 temperature=0 实现不同（argmax vs 仍有随机性）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。建议 Limitations 补充讨论\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-W6\"\n  summary: \"BibTeX key mou_ambigswe_2026 与 author 字段不匹配\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"key 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"可能是引用更新后 key 未同步，应修正\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-M1\"\n  summary: \"Abstract 信息密度偏高（5 个数字），建议精简至 3 个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W11 首次提出并标记 resolved\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"仍有 5 个具体数字，建议保留 confound-free effect, variance decomposition, convergent violation rate\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"轻微同意，实证 abstract 承载数字合理但可精简\"\n  cross_response_status: \"converged — mild agreement\"\n\n- id: \"R21-M2\"\n  summary: \"Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差需澄清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"原始定义指 divergent interpretations，论文指 convergent errors——方向相反\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意应明确说明术语重新定义\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-rebut-partial\"\n      note: \"R2 反驳 R1 对 'nocuous' 一词的延伸质疑：因果效应大小（34pp）与方差解释比例（15.8%）是不同概念，34pp 绝对增幅足以支撑 'nocuous' 定性判断\"\n  cross_response_status: \"converged on direction clarification; diverged on whether 'nocuous' is overstated (resolved: R2's distinction between effect size and variance valid)\"\n\n- id: \"R21-M3\"\n  summary: \"NMI=0.23 绝对水平 modest，'order of magnitude' 表述需上下文化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"23× 比值成立但 NMI=0.23 绝对值仅为 modest\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"建议同时报告 Cramér's V=0.45 和 'moderate but actionable association'\"\n  cross_response_status: \"converged\"\n\n# ============================================================\n# R21 DIVERGENCE RESOLVED IN CROSS-RESPONSE\n# ============================================================\n\n# R2 rebuts R1 on SOPBench decay interpretation:\n# R1 viewed 34pp vs 12.6pp gap as ecological validity concern\n# R2 argues structural explanation (pre-existing policies, different domains) + model scaling replication (+20-33.6pp across 7 models) is stronger evidence\n# Director judgment: R2's rebuttal accepted; SOPBench is secondary, model expansion is primary generalizability evidence. Not elevated to issue.\n\n# R2 corrects R1 on ICC CI upper bound:\n# R1 cited 0.910; actual paper value is 0.940\n# Director judgment: factual correction accepted. No impact on assessment.\n\n# ============================================================\n# R20 ISSUES — STATUS UPDATES FOR R21\n# ============================================================\n\n- id: \"R20-N1\"\n  summary: \"Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"17× → order-of-magnitude (NMI=0.23 vs 0.01 保留); §6.1 区分 2/6 definitional vs 4/6 empirical mappings\"\n  resolution_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"not re-raised\"\n      note: \"R21 未重新提出 tautological concern，但 R21-W1 提出了相关的 LLM 编码循环性问题\"\n\n- id: \"R20-N2\"\n  summary: \"遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"已添加引用并在 §6.2 和 Limitations 讨论\"\n  resolution_round: 20\n\n- id: \"R20-W1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N1)。七 margin 敏感性和 bootstrap 被视为有帮助但不充分\"\n\n- id: \"R20-W2\"\n  summary: \"Taxonomy 新颖性定位模糊\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N4)。experimental instrument 定位仍不够明确\"\n\n- id: \"R20-W3\"\n  summary: \"Cross-judge 分配非随机化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Cross-judge validation Fleiss κ=0.717 已添加\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"acknowledged\"\n      note: \"R21 承认 cross-judge validation 存在，但提出新问题：within-group type ranking ρ=0.09 (R21-N3)\"\n\n- id: \"R20-W4\"\n  summary: \"Disambiguation neglect 与 ambiguity collapse 概念区分度不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为场景迁移而非概念创新\"\n\n- id: \"R20-W5\"\n  summary: \"生态效度量化差距\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"'under controlled synthetic conditions' 已添加\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Human validation per-type 检验力不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"R21-W4：仍期望 3+ annotators 和更大 per-type 样本\"\n\n- id: \"R20-W7\"\n  summary: \"Perturbation control 缺 information-addition 控制\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"coreferential 天然控制 + token count regression\"\n  resolution_round: 20\n\n- id: \"R20-W8\"\n  summary: \"Clause-level vs type-level auditing actionability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"Discussion 方差全景图覆盖\"\n  resolution_round: 20\n\n- id: \"R20-W9\"\n  summary: \"Bib 条目问题：重复条目、Anonymous 作者、类型错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"主要 bib 问题已修复\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"partial\"\n      note: \"新发现 mou_ambigswe_2026 key 命名问题 (R21-W6)\"\n\n- id: \"R20-W10\"\n  summary: \"其他可能遗漏文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"核实不威胁核心 claim\"\n  resolution_round: 20\n\n- id: \"R20-W11\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-M1：仍有 5 个数字，降级为 info\"\n\n# ============================================================\n# R18-R19 RESOLVED (UNCHANGED)\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"C2 降为 secondary claim, robust extremes only.\"\n  resolution_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Cross-family judge validation κ=0.717\"\n  resolution_round: 19\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"Taxonomy 降格为 experimental instrument\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-N4：降格定位仍不够明确，C3 检验失败未在 Intro 反映\"\n\n- id: \"R18-N4\"\n  summary: \"DN 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"降级为 descriptive label\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为渐进性贡献\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"≤8 pages maintained\"\n  resolution_round: 18\n\n- id: \"R19-N1\"\n  summary: \"合成歧义生态效度不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'\"\n  resolution_round: 19\n\n- id: \"R19-N2\"\n  summary: \"非歧义纳入 ambiguity 标签\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"§3 改 'comparable safety impact despite distinct mechanisms'\"\n  resolution_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims 未充分降级\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Figure 3 caption 加 κ=0.385 + caution\"\n  resolution_round: 19\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"30× → 17× → order-of-magnitude (NMI-based)\"\n  resolution_round: 20\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test + GLMM ICC\"\n  resolution_round: 17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Review Issues Tracker — policy_ambiguity_safety\n## Paper: \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Latest Round: 21\n\n# ============================================================\n# R21 ISSUES — FINAL (POST CROSS-RESPONSE)\n# ============================================================\n\n- id: \"R21-N1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，对安全场景过于宽松\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R20-W1 首次提出，当时标记为 resolved（Table 3 七 margin 敏感性）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"重新提出为 critical：无外部锚定（生产事故率/监管阈值），perturbation Δ=0.67pp 视为 negligible 但 SESOI 放宽到 ±15pp 缺乏理据\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意但指出 bootstrap cluster analysis (margin-free) 部分缓解了 TOST 的 margin 依赖\"\n  cross_response_status: \"converged — both agree, R2 notes partial mitigation via bootstrap\"\n\n- id: \"R21-N2\"\n  summary: \"46% 未解释系统方差（systematic-but-unmeasured）讨论深度不足\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"condition 仅解释 15.8% 方差，46pp 系统残差未列举候选因素（对话轨迹？任务复杂度？策略文档结构？）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意讨论深度不足，但指出论文将歧义定位为 'largest actionable component' 而非 'dominant driver'，叙事定位合理\"\n  cross_response_status: \"converged — both agree on insufficient discussion, R2 endorses narrative framing\"\n\n- id: \"R21-N3\"\n  summary: \"Cross-judge-group 类型排序 ρ=0.09 严重削弱 C2 partial ordering 可信度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"排除 auth scope 后 ρ 从 0.09 跳到 0.90，n=5 统计功效低；auth scope κ=0.385 不可靠\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"partial ordering 退化为两个极端点（incompleteness 最高，coreferential 最低），中间等价——信息量有限\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-response\"\n      note: \"补充：Appendix K 三法官 pooled type ranking ρ=0.71-0.89 远高于 within-group 0.09，说明问题在 judge-model pairing 而非法官偏差\"\n  cross_response_status: \"converged — both agree C2 limited to extremes; R2 adds pooled ρ context\"\n\n- id: \"R21-N4\"\n  summary: \"Taxonomy 新颖性不足以支撑独立 contribution 定位\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 18\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"R18-N3 首次提出\"\n    - round: 20\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"R20-W2 标记为 resolved（降格为 experimental instrument）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：C3 层级假说 p=0.017 未通过 Holm-Bonferroni，类型选择标准缺乏定量依据（无真实策略文档频率数据）\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意核心判断，但指出 Introduction 的 contribution 列表未将 taxonomy 列为独立贡献\"\n  cross_response_status: \"converged — both agree taxonomy not standalone; R1 notes Intro already avoids claiming it\"\n\n- id: \"R21-W1\"\n  summary: \"Error analysis LLM 编码循环性（Gwet's AC₁=0.62），需人工验证子集\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"AC₁=0.62 低于 good agreement 阈值 0.80，需至少 100 条 trace 人工编码\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。MI=0.41 是间接论证，不能替代直接人工验证\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-W2\"\n  summary: \"Disambiguation neglect 是 ambiguity collapse 的场景迁移，非概念创新\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W4 首次提出\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"重新提出：Liu et al. (2023) 已证明 LLM 坍缩歧义，本文在 agentic 场景验证，但暗示独立概念\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意。建议定位为 'extending ambiguity collapse to agentic settings'\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-W3\"\n  summary: \"Abstract 应以 confound-free range (+18.7 to +36.0pp) 为核心效应量\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"Abstract 以 34.0pp 领头（含 incompleteness confound），应以 confound-free range 为主数字\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"部分同意，但补充 Appendix F 逻辑回归 token count 正系数暗示 confound 若存在为 attenuating\"\n  cross_response_status: \"converged — partial agree, R1 adds attenuating-confound nuance\"\n\n- id: \"R21-W4\"\n  summary: \"Human validation 样本量不足（n=100, 2 annotators, per-type n≈32-34）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"期望 3+ 标注员，per-type ≥50 样本，当前 per-type κ CI 过宽\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意，但指出 pooled κ=0.735 对 pipeline validation 充分，不足在 per-type 层面\"\n  cross_response_status: \"converged — both agree pooled sufficient, per-type insufficient\"\n\n- id: \"R21-W5\"\n  summary: \"Temperature=0 跨 provider 确定性假设未讨论，ICC 复制仅限 OpenAI\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"不同 provider 对 temperature=0 实现不同（argmax vs 仍有随机性）\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"同意。建议 Limitations 补充讨论\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-W6\"\n  summary: \"BibTeX key mou_ambigswe_2026 与 author 字段不匹配\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"key 暗示第一作者 Mou，但 author 字段为 Vijayvargiya 等人\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"可能是引用更新后 key 未同步，应修正\"\n  cross_response_status: \"converged\"\n\n- id: \"R21-M1\"\n  summary: \"Abstract 信息密度偏高（5 个数字），建议精简至 3 个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"R20-W11 首次提出并标记 resolved\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"仍有 5 个具体数字，建议保留 confound-free effect, variance decomposition, convergent violation rate\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"轻微同意，实证 abstract 承载数字合理但可精简\"\n  cross_response_status: \"converged — mild agreement\"\n\n- id: \"R21-M2\"\n  summary: \"Systematic nocuity 与 Berry & Kamsties (2004) 原始定义方向偏差需澄清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"originator\"\n      note: \"原始定义指 divergent interpretations，论文指 convergent errors——方向相反\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"cross-agree\"\n      note: \"同意应明确说明术语重新定义\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-rebut-partial\"\n      note: \"R2 反驳 R1 对 'nocuous' 一词的延伸质疑：因果效应大小（34pp）与方差解释比例（15.8%）是不同概念，34pp 绝对增幅足以支撑 'nocuous' 定性判断\"\n  cross_response_status: \"converged on direction clarification; diverged on whether 'nocuous' is overstated (resolved: R2's distinction between effect size and variance valid)\"\n\n- id: \"R21-M3\"\n  summary: \"NMI=0.23 绝对水平 modest，'order of magnitude' 表述需上下文化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"originator\"\n      note: \"23× 比值成立但 NMI=0.23 绝对值仅为 modest\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"cross-agree\"\n      note: \"建议同时报告 Cramér's V=0.45 和 'moderate but actionable association'\"\n  cross_response_status: \"converged\"\n\n# ============================================================\n# R21 DIVERGENCE RESOLVED IN CROSS-RESPONSE\n# ============================================================\n\n# R2 rebuts R1 on SOPBench decay interpretation:\n# R1 viewed 34pp vs 12.6pp gap as ecological validity concern\n# R2 argues structural explanation (pre-existing policies, different domains) + model scaling replication (+20-33.6pp across 7 models) is stronger evidence\n# Director judgment: R2's rebuttal accepted; SOPBench is secondary, model expansion is primary generalizability evidence. Not elevated to issue.\n\n# R2 corrects R1 on ICC CI upper bound:\n# R1 cited 0.910; actual paper value is 0.940\n# Director judgment: factual correction accepted. No impact on assessment.\n\n# ============================================================\n# R20 ISSUES — STATUS UPDATES FOR R21\n# ============================================================\n\n- id: \"R20-N1\"\n  summary: \"Failure mode taxonomy 与 ambiguity taxonomy 定义循环性，17× claim 部分为 tautological artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"17× → order-of-magnitude (NMI=0.23 vs 0.01 保留); §6.1 区分 2/6 definitional vs 4/6 empirical mappings\"\n  resolution_round: 20\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"not re-raised\"\n      note: \"R21 未重新提出 tautological concern，但 R21-W1 提出了相关的 LLM 编码循环性问题\"\n\n- id: \"R20-N2\"\n  summary: \"遗漏重要相关工作 Ambig-SWE (Mou et al., ICLR 2026)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"已添加引用并在 §6.2 和 Limitations 讨论\"\n  resolution_round: 20\n\n- id: \"R20-W1\"\n  summary: \"SESOI ±15pp 缺乏外部锚定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R1\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N1)。七 margin 敏感性和 bootstrap 被视为有帮助但不充分\"\n\n- id: \"R20-W2\"\n  summary: \"Taxonomy 新颖性定位模糊\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 20\n      reviewer: \"R2\"\n      role: \"originator\"\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"升级为 critical (R21-N4)。experimental instrument 定位仍不够明确\"\n\n- id: \"R20-W3\"\n  summary: \"Cross-judge 分配非随机化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Cross-judge validation Fleiss κ=0.717 已添加\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R1,R2\"\n      role: \"acknowledged\"\n      note: \"R21 承认 cross-judge validation 存在，但提出新问题：within-group type ranking ρ=0.09 (R21-N3)\"\n\n- id: \"R20-W4\"\n  summary: \"Disambiguation neglect 与 ambiguity collapse 概念区分度不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为场景迁移而非概念创新\"\n\n- id: \"R20-W5\"\n  summary: \"生态效度量化差距\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"'under controlled synthetic conditions' 已添加\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Human validation per-type 检验力不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R1\"\n      role: \"re-raised\"\n      note: \"R21-W4：仍期望 3+ annotators 和更大 per-type 样本\"\n\n- id: \"R20-W7\"\n  summary: \"Perturbation control 缺 information-addition 控制\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"coreferential 天然控制 + token count regression\"\n  resolution_round: 20\n\n- id: \"R20-W8\"\n  summary: \"Clause-level vs type-level auditing actionability\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"Discussion 方差全景图覆盖\"\n  resolution_round: 20\n\n- id: \"R20-W9\"\n  summary: \"Bib 条目问题：重复条目、Anonymous 作者、类型错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"主要 bib 问题已修复\"\n  resolution_round: 20\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"partial\"\n      note: \"新发现 mou_ambigswe_2026 key 命名问题 (R21-W6)\"\n\n- id: \"R20-W10\"\n  summary: \"其他可能遗漏文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"核实不威胁核心 claim\"\n  resolution_round: 20\n\n- id: \"R20-W11\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-M1：仍有 5 个数字，降级为 info\"\n\n# ============================================================\n# R18-R19 RESOLVED (UNCHANGED)\n# ============================================================\n\n- id: \"R18-N1\"\n  summary: \"C2 mid-tier ordering 不稳健\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"C2 降为 secondary claim, robust extremes only.\"\n  resolution_round: 18\n\n- id: \"R18-N2\"\n  summary: \"Judge-model identity 混淆\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Cross-family judge validation κ=0.717\"\n  resolution_round: 19\n\n- id: \"R18-N3\"\n  summary: \"Taxonomy 增量贡献不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"Taxonomy 降格为 experimental instrument\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-N4：降格定位仍不够明确，C3 检验失败未在 Intro 反映\"\n\n- id: \"R18-N4\"\n  summary: \"DN 新颖性不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"降级为 descriptive label\"\n  resolution_round: 18\n  mentions:\n    - round: 21\n      reviewer: \"R2\"\n      role: \"re-raised\"\n      note: \"R21-W2：仍被视为渐进性贡献\"\n\n- id: \"R18-W8\"\n  summary: \"主文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"≤8 pages maintained\"\n  resolution_round: 18\n\n- id: \"R19-N1\"\n  summary: \"合成歧义生态效度不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"Abstract/Intro/Conclusion 加 'under controlled synthetic conditions'\"\n  resolution_round: 19\n\n- id: \"R19-N2\"\n  summary: \"非歧义纳入 ambiguity 标签\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"§3 改 'comparable safety impact despite distinct mechanisms'\"\n  resolution_round: 19\n\n- id: \"R19-N3\"\n  summary: \"Auth scope κ=0.385 claims 未充分降级\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 20\n  resolution: \"Figure 3 caption 加 κ=0.385 + caution\"\n  resolution_round: 19\n\n- id: \"R17-N1\"\n  summary: \"30× MI ratio 未归一化\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"30× → 17× → order-of-magnitude (NMI-based)\"\n  resolution_round: 20\n\n- id: \"R17-N2\"\n  summary: \"22.4% LPM 方差分解 df 膨胀\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 17\n  resolution: \"Permutation test + GLMM ICC\"\n  resolution_round: 17"
  }
}
```

</details>

---


### Tool result

_source line 1882 · 2026-05-23T03:48:48.417837+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 16617}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---
