# Director coordination — Part 4 of 6

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/3d/3da1d06caead0f03c51d.json)

## Round 95

### User

_source line 917 · 2026-05-19T03:08:54.852508+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 对 Reviewer 1 的交叉回应

### 逐条回应

**[AGREE] R1-W1 (生态效度)**: 与我的 W2 一致。full-replacement chain 与 accumulation setting 的结构性差距是核心问题。补充：domain bias 分析（Appendix D.2）只排除了 seed 文章 confound，没有回答 accumulation 问题。

**[AGREE] R1-W2 (Cross-strategy failure)**: d1-d3 balanced accuracy 45.9% 加上 d1/d2 boundary inversion 意味着策略未知时部署价值很低。回顾后认为 R1 将此列为 Must-Fix 比我原始审稿更准确。

**[AGREE] R1-W3 (d0 膨胀)**: 与我的 W6 一致。cross-model 66.4% 被 d0 (99.3% recall) 抬升约 11pp。

**[AGREE] R1-W4 (Cross-scale 证据不足)**: 仅 3 个 7-14B 模型且轨迹完全不同（Llama monotonic vs Qwen U-shaped）不足以建立 general pattern。我补充：这个问题比 R1 评估的更严重，因为 14B 的 EDD=0 关系到整个 research program 的可行性。

**[AGREE] R1-W5 (Curation PoC)**: 与我的 W7 一致。补充 Bonferroni 校正后 rf_moderate vs random_moderate (p=0.020) 变为 borderline non-significant。

**[PARTIALLY AGREE] R1-W6 (多重共线性)**: 技术观点正确，但论文已有三重验证缓解（Kendall's W=0.90）。问题在 framing（individual rank vs group-level dominance），非 validity。

**[PARTIALLY AGREE] R1-W7 (EDD threshold)**: T=0.70 无独立依据，但论文报告了 T∈{0.65-0.80} 敏感性。Minor 级别合适。

**[REBUT] R1-W8 (RF ordinal claim)**: 98.2% adjacent errors, QWK=0.89, CORAL 仅 +0.6pp，加上 Janitza (2016) 理论和 feature monotonicity (ρ=-1.0) 构成充分证据。建议添加条件 caveat 即可。

**[PARTIALLY AGREE] R1-W9 (Reference model ablation)**: 只在 Pythia 数据上做的不够完整，但 Limitations 中已承认且核心 finding 不依赖特定 reference。

### 对 R1 Questions 的回应

- Q1 (Accumulation): AGREE，论文未回答，应在 Discussion 讨论
- Q2 (Architecture signal): AGREE，reverse-chain 提供间接证据但不够
- Q3 (d3>d2 recall): AGREE with nuance，d2 被两边夹击 + 多类分类器利用非相邻对比
- Q4 (GPU claim): AGREE，"requires no GPU" 几乎肯定不准确（1.4B 模型 CPU 推理 5000×512 tokens 需数十小时非 2 分钟）
- Q5 (CV independence): PARTIALLY AGREE，distributional dependency 不违反 CV 假设，但 pattern inheritance 可能导致 CV 轻微高估

### 共识与分歧总结

**高度共识**: 生态效度、d0 通胀、Curation PoC 不显著、Overall 3.0 (Findings)

**互补**: R1 侧重统计方法论（VIF、EDD threshold、多重比较），我侧重新颖性（算法贡献不足 W3）和写作质量（Abstract 过载 W4、Discussion 缺失 W5）

**轻微分歧**: R1-W8 (RF ordinal claim) 我倾向 REBUT；规模瓶颈严重性我评估高于 R1（Must-Fix vs Should-Fix）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-19T03:09:24.983719+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 初始化 + 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成初始化和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排并派发任务', 'status': 'completed', 'activeForm': '完成 Reviewer 编排和任务派发'}, {'content': 'Step 1: 等待 Reviewer 1 和 Reviewer 2 独立审稿返回', 'status': 'completed', 'activeForm': '两位 Reviewer 审稿已返回'}, {'content': 'Step 2: 交叉分享 — 将每位 Reviewer 原文转发给对方', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': 'Step 3: 收敛判断 — 检查共识与分歧', 'status': 'in_progress', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 初始化 + 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成初始化和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排并派发任务', 'status': 'completed', 'activeForm': '完成 Reviewer 编排和任务派发'}, {'content': 'Step 1: 等待 Reviewer 1 和 Reviewer 2 独立审稿返回', 'status': 'completed', 'activeForm': '两位 Reviewer 审稿已返回'}, {'content': 'Step 2: 交叉分享 — 将每位 Reviewer 原文转发给对方', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': 'Step 3: 收敛判断 — 检查共识与分歧', 'status': 'in_progress', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-19T03:09:25.084778+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-19T03:09:44.325646+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 初始化 + 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成初始化和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排并派发任务', 'status': 'completed', 'activeForm': '完成 Reviewer 编排和任务派发'}, {'content': 'Step 1: 等待 Reviewer 1 和 Reviewer 2 独立审稿返回', 'status': 'completed', 'activeForm': '两位 Reviewer 审稿已返回'}, {'content': 'Step 2: 交叉分享 — 将每位 Reviewer 原文转发给对方', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': 'Step 3: 收敛判断 — 检查共识与分歧', 'status': 'completed', 'activeForm': '审稿意见已收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 初始化 + 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成初始化和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排并派发任务', 'status': 'completed', 'activeForm': '完成 Reviewer 编排和任务派发'}, {'content': 'Step 1: 等待 Reviewer 1 和 Reviewer 2 独立审稿返回', 'status': 'completed', 'activeForm': '两位 Reviewer 审稿已返回'}, {'content': 'Step 2: 交叉分享 — 将每位 Reviewer 原文转发给对方', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': 'Step 3: 收敛判断 — 检查共识与分歧', 'status': 'completed', 'activeForm': '审稿意见已收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-19T03:09:44.376384+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-19T03:11:03.011710+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 12 Issues\n  # ============================================================\n\n  - id: R12-W1\n    summary: \"生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异，需更清晰的 scope 声明\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。论文 Limitations 中有承认但 framing 不够突出。需要在 Abstract/Introduction 明确 scope 限制，Discussion 讨论 accumulation setting。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 讨论段落\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W2\n    summary: \"Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion，策略未知场景下部署价值极低\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix，R2 交叉回应中升级认同。Abstract 中的 cross-model 66.4% 有 d0 膨胀（d1-d3 仅 55.4%），cross-strategy 更差。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 补充 d1-d3 balanced accuracy 到同等显著位置；将 cross-strategy bottleneck 从 limitation 提升为独立贡献点\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W3\n    summary: \"d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 和 R2-W6 完全一致。cross-model 66.4% 被 d0 从 55.4% 抬升 11pp。\"\n    action_items:\n      - round: 12\n        action: \"所有 headline 数字旁系统性并列 d1-d3 balanced accuracy\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"Cross-scale 实验仅 3 个模型、5 个混杂因素，不足以支撑 scale-dependent attenuation 结论；14B 自参考混杂使数据点不可靠\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 列 Should-Fix，R2 列 Must-Fix（'致命瓶颈'）。分歧点：R1 认为 14B 自参考混杂使数据不可靠，scale 结论本身 weak；R2 视 14B EDD=0 为 face value 推断路线天花板。Director 裁定 Should-Fix：14B confound 确实存在，证据不足以支撑强结论。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Contributions 降调 cross-scale claim；明确声明 cross-scale results are confounded；若可能用 Pythia-1.4B 作为 14B reference 补充实验\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W5\n    summary: \"Curation PoC 主比较不显著（RF vs unfiltered p=0.407），RF vs random 多重比较未校正\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W5 和 R2-W7 完全一致。Bonferroni 校正后 rf_moderate vs random_moderate borderline non-significant。\"\n    action_items:\n      - round: 12\n        action: \"明确将 curation PoC 标记为 inconclusive；对 RF vs random 应用 Bonferroni 校正；Discussion 中不以 feasible 描述 depth-graduated filtering\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W6\n    summary: \"Abstract 信息过载：200 词中 20+ 数字，嵌套括号，一次阅读几乎无法消化\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Detailed Comments 和 R2-W4 一致。建议重构为 3 个清晰 claim 层级。\"\n    action_items:\n      - round: 12\n        action: \"重写 Abstract：保留 2-3 个关键数字，分为 problem-method-result 三层叙事\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W7\n    summary: \"Discussion 仅一段约 80 词，核心讨论被放逐到 Appendix\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 和 R2-W5 一致。建议扩展：(1) accumulation setting (2) model collapse mitigation 交互 (3) 部署 roadmap。\"\n    action_items:\n      - round: 12\n        action: \"扩展 Discussion 至 3-4 段，将 Appendix Extended Discussion 核心内容移入正文\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W8\n    summary: \"多重共线性（VIF>10, 14-16/19 features）下 individual feature importance 不可靠，正文以单特征 rank 为核心叙事\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W6 提出，R2 交叉回应 partially agree（三重验证缓解，framing 问题非 validity）。\"\n    action_items:\n      - round: 12\n        action: \"主表格改以 feature group 为分析单位；正文强调 group-level dominance 而非 individual rank\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W9\n    summary: \"算法贡献不足：标准 RF + 标准特征，RF/XGB/LightGBM 0.4pp 内收敛\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W3 列 Must-Fix，R1 REBUT（定位问题非缺陷，benchmark paper 先例）。Director 裁定 Should-Fix：论文明确自我定位为 empirical study，但 framing 可更明确。classifier convergence 恰恰证明 feature 的价值。\"\n    action_items:\n      - round: 12\n        action: \"Introduction 强化 empirical study + problem formalization 定位；强调 feature design 和 task formalization 为核心贡献而非 classifier\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M1\n    summary: \"EDD threshold T=0.70 选择缺乏独立理论/实证依据，存在循环论证风险\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W7 提出，R2 partially agree（sensitivity analysis 缓解，Minor 合适）。\"\n    action_items:\n      - round: 12\n        action: \"添加 T=0.70 在 AUC 文献中的含义讨论\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M2\n    summary: \"RF ordinal claim 过强：adjacent error 集中可能仅反映 feature overlap 而非 RF 内在序数归纳偏置\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W8 提出，R2 REBUT（98.2% + QWK=0.89 + CORAL +0.6pp + Janitza 2016 构成充分证据，添加 caveat 即可）。\"\n    action_items:\n      - round: 12\n        action: \"弱化表述为 'RF produces ordinally consistent predictions'，避免暗示 RF 有内在序数偏置\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M3\n    summary: \"Reference model (Pythia-1.4B) 与 generator 重叠，ablation 仅在 Pythia 数据上做\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W9 提出，R2 partially agree。Limitations 已承认但可补充非 Pythia cell ablation。\"\n    action_items:\n      - round: 12\n        action: \"在至少一个非 Pythia cell 上补充 reference model ablation\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M4\n    summary: \"Prompted generation 验证仅覆盖 1/9 cells (GPT-2 XL nucleus)，推广性未建立\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。Limitations 有 caveat 但 Abstract/正文中不够突出。\"\n    action_items:\n      - round: 12\n        action: \"Limitations 加强 caveat；Abstract 中 prompted generation 结果添加 single-cell qualifier\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M5\n    summary: \"Feature trajectory 图 (fig_feature_trajectory) 被移入 Appendix，应保留正文\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W9 提出，R1 交叉回应 AGREE。\"\n    action_items:\n      - round: 12\n        action: \"将 feature trajectory 图移回正文（可缩小尺寸）\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M6\n    summary: \"孤立 bib entry c2pa2024 未在正文引用；5 条引用 mismatch（作者名/年份差异）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均指出。\"\n    action_items:\n      - round: 12\n        action: \"删除或引用 c2pa2024；核实 5 条 mismatch 条目\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M7\n    summary: \"Feature extraction 'requires no GPU' 声明可能不准确（Pythia-1.4B forward pass on CPU for 5000×512 tokens）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1-Q4 提出，R2 交叉回应 AGREE（CPU 推理 1.4B 模型 5000 样本需数十小时非 2 分钟）。\"\n    action_items:\n      - round: 12\n        action: \"核实 inference 硬件需求并修正 Appendix 声明\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M8\n    summary: \"遗漏相关工作：Muennighoff et al. (2024), Ilyas et al. (2022) Datamodels\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 交叉回应部分同意。\"\n    action_items:\n      - round: 12\n        action: \"补充引用 Muennighoff et al. 和 Ilyas et al.\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 12 Issues\n  # ============================================================\n\n  - id: R12-W1\n    summary: \"生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异，需更清晰的 scope 声明\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。论文 Limitations 中有承认但 framing 不够突出。需要在 Abstract/Introduction 明确 scope 限制，Discussion 讨论 accumulation setting。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 讨论段落\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W2\n    summary: \"Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion，策略未知场景下部署价值极低\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix，R2 交叉回应中升级认同。Abstract 中的 cross-model 66.4% 有 d0 膨胀（d1-d3 仅 55.4%），cross-strategy 更差。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 补充 d1-d3 balanced accuracy 到同等显著位置；将 cross-strategy bottleneck 从 limitation 提升为独立贡献点\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W3\n    summary: \"d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 和 R2-W6 完全一致。cross-model 66.4% 被 d0 从 55.4% 抬升 11pp。\"\n    action_items:\n      - round: 12\n        action: \"所有 headline 数字旁系统性并列 d1-d3 balanced accuracy\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"Cross-scale 实验仅 3 个模型、5 个混杂因素，不足以支撑 scale-dependent attenuation 结论；14B 自参考混杂使数据点不可靠\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 列 Should-Fix，R2 列 Must-Fix（'致命瓶颈'）。分歧点：R1 认为 14B 自参考混杂使数据不可靠，scale 结论本身 weak；R2 视 14B EDD=0 为 face value 推断路线天花板。Director 裁定 Should-Fix：14B confound 确实存在，证据不足以支撑强结论。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Contributions 降调 cross-scale claim；明确声明 cross-scale results are confounded；若可能用 Pythia-1.4B 作为 14B reference 补充实验\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W5\n    summary: \"Curation PoC 主比较不显著（RF vs unfiltered p=0.407），RF vs random 多重比较未校正\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W5 和 R2-W7 完全一致。Bonferroni 校正后 rf_moderate vs random_moderate borderline non-significant。\"\n    action_items:\n      - round: 12\n        action: \"明确将 curation PoC 标记为 inconclusive；对 RF vs random 应用 Bonferroni 校正；Discussion 中不以 feasible 描述 depth-graduated filtering\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W6\n    summary: \"Abstract 信息过载：200 词中 20+ 数字，嵌套括号，一次阅读几乎无法消化\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Detailed Comments 和 R2-W4 一致。建议重构为 3 个清晰 claim 层级。\"\n    action_items:\n      - round: 12\n        action: \"重写 Abstract：保留 2-3 个关键数字，分为 problem-method-result 三层叙事\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W7\n    summary: \"Discussion 仅一段约 80 词，核心讨论被放逐到 Appendix\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 和 R2-W5 一致。建议扩展：(1) accumulation setting (2) model collapse mitigation 交互 (3) 部署 roadmap。\"\n    action_items:\n      - round: 12\n        action: \"扩展 Discussion 至 3-4 段，将 Appendix Extended Discussion 核心内容移入正文\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W8\n    summary: \"多重共线性（VIF>10, 14-16/19 features）下 individual feature importance 不可靠，正文以单特征 rank 为核心叙事\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W6 提出，R2 交叉回应 partially agree（三重验证缓解，framing 问题非 validity）。\"\n    action_items:\n      - round: 12\n        action: \"主表格改以 feature group 为分析单位；正文强调 group-level dominance 而非 individual rank\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W9\n    summary: \"算法贡献不足：标准 RF + 标准特征，RF/XGB/LightGBM 0.4pp 内收敛\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W3 列 Must-Fix，R1 REBUT（定位问题非缺陷，benchmark paper 先例）。Director 裁定 Should-Fix：论文明确自我定位为 empirical study，但 framing 可更明确。classifier convergence 恰恰证明 feature 的价值。\"\n    action_items:\n      - round: 12\n        action: \"Introduction 强化 empirical study + problem formalization 定位；强调 feature design 和 task formalization 为核心贡献而非 classifier\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M1\n    summary: \"EDD threshold T=0.70 选择缺乏独立理论/实证依据，存在循环论证风险\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W7 提出，R2 partially agree（sensitivity analysis 缓解，Minor 合适）。\"\n    action_items:\n      - round: 12\n        action: \"添加 T=0.70 在 AUC 文献中的含义讨论\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M2\n    summary: \"RF ordinal claim 过强：adjacent error 集中可能仅反映 feature overlap 而非 RF 内在序数归纳偏置\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W8 提出，R2 REBUT（98.2% + QWK=0.89 + CORAL +0.6pp + Janitza 2016 构成充分证据，添加 caveat 即可）。\"\n    action_items:\n      - round: 12\n        action: \"弱化表述为 'RF produces ordinally consistent predictions'，避免暗示 RF 有内在序数偏置\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M3\n    summary: \"Reference model (Pythia-1.4B) 与 generator 重叠，ablation 仅在 Pythia 数据上做\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W9 提出，R2 partially agree。Limitations 已承认但可补充非 Pythia cell ablation。\"\n    action_items:\n      - round: 12\n        action: \"在至少一个非 Pythia cell 上补充 reference model ablation\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M4\n    summary: \"Prompted generation 验证仅覆盖 1/9 cells (GPT-2 XL nucleus)，推广性未建立\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均同意。Limitations 有 caveat 但 Abstract/正文中不够突出。\"\n    action_items:\n      - round: 12\n        action: \"Limitations 加强 caveat；Abstract 中 prompted generation 结果添加 single-cell qualifier\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M5\n    summary: \"Feature trajectory 图 (fig_feature_trajectory) 被移入 Appendix，应保留正文\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2-W9 提出，R1 交叉回应 AGREE。\"\n    action_items:\n      - round: 12\n        action: \"将 feature trajectory 图移回正文（可缩小尺寸）\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M6\n    summary: \"孤立 bib entry c2pa2024 未在正文引用；5 条引用 mismatch（作者名/年份差异）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均指出。\"\n    action_items:\n      - round: 12\n        action: \"删除或引用 c2pa2024；核实 5 条 mismatch 条目\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M7\n    summary: \"Feature extraction 'requires no GPU' 声明可能不准确（Pythia-1.4B forward pass on CPU for 5000×512 tokens）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"R1-Q4 提出，R2 交叉回应 AGREE（CPU 推理 1.4B 模型 5000 样本需数十小时非 2 分钟）。\"\n    action_items:\n      - round: 12\n        action: \"核实 inference 硬件需求并修正 Appendix 声明\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M8\n    summary: \"遗漏相关工作：Muennighoff et al. (2024), Ilyas et al. (2022) Datamodels\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 交叉回应部分同意。\"\n    action_items:\n      - round: 12\n        action: \"补充引用 Muennighoff et al. 和 Ilyas et al.\"\n        assigned_to: research_director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-19T03:11:03.112774+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 10209}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-19T03:13:18.129186+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了一个 180K 样本基准（3 模型族 × 3 解码策略 × 4 深度），用 Random Forest 在 19 个统计特征上实现 69-86% 四分类准确率（chance=25%）。论文定义了 Effective Discriminable Depth (EDD) 度量，构建了 Depth Degradation Atlas，并在 8 个泛化维度上进行系统评估。这是一项问题定义新颖、实验执行严谨、报告透明诚实的实证研究，但在生态效度、跨策略部署和规模可扩展性方面存在结构性限制。\n\n---\n\n## Strengths\n\n**S1. 任务定义的原创性 [R1, R2 一致]。** 递归生成深度估计是一个真正未被研究过的问题，填补了 model collapse 理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。EDD 度量的形式化（Definition 1, Eq. 1）数学自洽且有概念价值。\n\n**S2. 系统性实验设计 [R1, R2 一致]。** 3×3 model-strategy grid × 4 depths = 180K 样本，加上 8 个泛化轴（cross-model, cross-strategy, cross-scale, cross-domain, cross-model chains, prompted generation, seed replication, depth extension），构成了非常全面的实验矩阵。基线覆盖四类方法且对比公平。\n\n**S3. 统计实践透明 [R1 主导, R2 认同]。** Bootstrap 95% CI 贯穿主要结果；domain bias 分析的三子实验设计严谨；初始 bug 透明报告并修复；RF seed robustness 验证（std=0.06pp）。\n\n**S4. 诚实的局限性讨论 [R1, R2 一致]。** d0 膨胀、cross-strategy 失败、14B EDD=0、5 个 cross-scale 混杂因素、单 LoRA 种子不确定性、curation PoC 非显著——均被如实报告。Limitations 覆盖 12+ 个具体限制。\n\n**S5. 理论-实证对应 [R1 主导]。** tail erosion 理论预测与 9/9 cells 的 p90_ppl top-2 ranking 对应；temperature d1 median p90_ppl (92.2) 与 nucleus d2 median (92.3) 的精确匹配验证了 strategy-dependent convergence 理论。\n\n**S6. 特征重要性三重验证 [R1 主导]。** Gini/SHAP/permutation 三种方法的一致性（Kendall's W=0.90, p<0.005）增强了核心发现的可信度。\n\n**S7. Related Work 覆盖充分 [R2 主导]。** 67 条引用覆盖 model collapse、AI text detection、membership inference、ordinal classification、decoding strategies 五个维度，达到 EMNLP 标准。\n\n---\n\n## Weaknesses\n\n### Must-Fix (2 项)\n\n**W1. 生态效度差距过大，需更清晰的 scope 声明 [R1-W1, R2-W2; AGREE]。**\n基准使用 Wikipedia 种子 + LoRA fine-tune 的 full-replacement recursive chain（每步完全替换训练数据）。真实世界的递归污染涉及 accumulation（混合真实+合成数据）、全量微调、混合语料、未知比例。论文 Limitations 有承认但 framing 不够突出。\n- **要求**: Abstract/Introduction 明确声明 full-replacement chain 的 scope 限制；Discussion 增加 accumulation setting 讨论。\n\n**W2. Cross-strategy transfer 在部署场景下近乎失败 [R1-W2; R2 交叉升级认同]。**\nd1-d3 balanced accuracy 仅 45.9%（chance=33%），出现 d1/d2 boundary inversion（d1v2 AUC < 0.5）。在实际部署中解码策略几乎总是未知的。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。论文标题以 \"estimating recursive generation depth\" 为核心 claim，但在最常见场景下该 claim 实质不成立。\n- **要求**: Abstract 补充 d1-d3 balanced accuracy 到同等显著位置；将 cross-strategy bottleneck 从 limitation 提升为独立贡献/发现。\n\n### Should-Fix (7 项)\n\n**W3. d0 膨胀导致 headline metrics 误导 [R1-W3, R2-W6; AGREE]。**\nd0 recall >97% 使 4-class accuracy 和 cross-model transfer 66.4% 被系统性抬升。d1-d3 balanced accuracy（within-distribution 71.6%, cross-model 55.4%, cross-strategy 45.9%）才是评估实际能力的关键数字。\n- **要求**: 所有 headline 数字旁系统性并列 d1-d3 balanced accuracy。\n\n**W4. Cross-scale 证据不足 [R1-W4 Should-Fix, R2-W1 Must-Fix; Director 裁定 Should-Fix]。**\n仅 3 个 7-14B 模型，5 个混杂因素同时存在（QLoRA、样本量、仅 nucleus、vocabulary mismatch、14B 自参考）。两个 7-8B 模型 AUC 轨迹完全不同（Llama monotonic vs Qwen U-shaped），无法确定主流 pattern。14B 的 EDD=0 因自参考混杂不可直接与 1-1.5B 比较。\n- **Director 裁定理由**: R2 将 14B EDD=0 视为 \"致命瓶颈\" 并推断 70B+ 必然失效，但 R1 正确指出 14B 自参考混杂使该数据点不可靠，scale effect 和 reference model effect 未被分离。在混杂未分离前，两种推断均缺乏充分依据。论文已标记为 \"Preliminary\"，应进一步降调。\n- **要求**: Abstract/Contributions 降调 cross-scale claim；声明 \"cross-scale results are confounded and should be interpreted as existence proofs\"；若可能用 Pythia-1.4B 作为 14B reference 补充实验。\n\n**W5. Curation PoC 主比较不显著 [R1-W5, R2-W7; AGREE]。**\nRF vs unfiltered p=0.407, d_z=0.41。RF vs random 的 3 个比较未做多重校正（Bonferroni 后 borderline non-significant）。\n- **要求**: 标记为 inconclusive；应用 Bonferroni 校正；Discussion 中不以 \"feasible\" 描述 depth-graduated filtering。\n\n**W6. Abstract 信息过载 [R1-Detailed, R2-W4; AGREE]。**\n约 200 词塞入 20+ 数字和多层嵌套括号。\n- **要求**: 重写 Abstract，保留 2-3 个关键数字，分为 problem-method-result 三层叙事。\n\n**W7. Discussion 实质缺失 [R1-Detailed, R2-W5; AGREE]。**\nSection 7 仅一段约 80 词，核心讨论被放逐到 Appendix Extended Discussion。\n- **要求**: 扩展至 3-4 段，涵盖 accumulation setting、model collapse mitigation 交互、部署 roadmap。\n\n**W8. 多重共线性下 feature importance framing 不当 [R1-W6; R2 partially agree]。**\nVIF>10 的 14-16/19 features 使 individual Gini importance 不可靠，但正文以 \"p90_ppl ranks top-2 in 9/9 cells\" 为核心叙事。三重验证（Kendall's W=0.90）缓解了 validity 问题，但 framing 应以 feature group 而非 individual feature 为分析单位。\n\n**W9. 算法贡献定位需强化 [R2-W3 Must-Fix; R1 REBUT; Director 裁定 Should-Fix]。**\nRF/XGBoost/LightGBM 在 0.4pp 内收敛，说明分类器选择不构成贡献。\n- **Director 裁定理由**: R1 的反驳有理——论文明确自我定位为 \"empirical study and problem formalization\"，*ACL 有 benchmark/analysis paper 先例（RAID, M4-SemEval）。Classifier convergence 恰恰证明核心贡献在 feature design + task formalization。这是 positioning 问题而非缺陷，不应列为 Must-Fix。\n- **要求**: Introduction 强化 empirical study + problem formalization 定位。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **生态效度差距是最核心的结构性问题**（R1-W1 ≡ R2-W2）\n2. **d0 通胀系统性抬升 headline metrics**（R1-W3 ≡ R2-W6）\n3. **Cross-strategy 在 d1-d3 近乎失败（45.9%）是部署的根本障碍**\n4. **Curation PoC 统计不显著（p>0.4）**（R1-W5 ≡ R2-W7）\n5. **Abstract 过载 + Discussion 缺失是写作层面最大问题**\n6. **Prompted generation 验证仅 1/9 cells 不足**\n7. **Overall 3.0 (Findings) — 两位 Reviewer 评分完全一致**\n\n## Reviewer Divergence [REBUT]\n\n1. **算法贡献是否构成 Must-Fix**: R2 认为 Must-Fix（\"方法论贡献几乎为零\"），R1 REBUT（benchmark paper 有先例，classifier convergence 证明 feature value）。**Director 采纳 R1 立场**——降级为 Should-Fix (W9)。\n\n2. **14B scale 瓶颈的严重程度**: R2 列 Must-Fix（\"致命\"，推断 70B+ 必然失效），R1 列 Should-Fix（自参考混杂使数据不可靠）。**Director 采纳折中立场**——Should-Fix (W4)，14B 数据因混杂不可直接推断。\n\n3. **AI 写作痕迹 (R2-W8)**: R1 REBUT（无具体例子，作者已声明使用 AI 辅助）。**Director 采纳 R1 立场**——不列入 weakness，但建议作者自查 dash 和 -ing phrases。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1 [R1].** Accumulation setting（混合真实+合成数据训练）下深度信号预期如何变化？\n\n**Q2 [R1].** Cross-model chain 的 84.75% 中有多少来自 depth signal vs architecture shift？能否通过与 single-model chain 对比做定量分解？\n\n**Q3 [R1].** 为什么 d3 recall 一致高于 d2？是否因为 d3 有更多独特退化信号？\n\n**Q4 [R1].** Feature extraction \"requires no GPU\" 的声明是否准确？Pythia-1.4B forward pass for 5000×512 tokens 在 CPU 上是否真的只需 2 分钟？\n\n**Q5 [R1].** 不同深度数据间的间接统计依赖关系对 CV 独立性假设有何影响？\n\n**Q6 [R2].** 14B 的 higher-order moments 成为 top features 是否暗示了 feature adaptation 策略？\n\n**Q7 [R2].** τ=1.1 时 depth signal 消失——高 temperature 能否有效规避 depth estimation？代价是什么？\n\n---\n\n## Missing References\n\n1. **Muennighoff et al. (2024)** \"Scaling Data-Constrained Language Models\" — data mixing 与 scale-dependent attenuation 相关 [R2]\n2. **Ilyas et al. (2022)** \"Datamodels\" — data attribution 与 provenance toolkit 相关 [R2]\n3. **孤立 bib entry**: c2pa2024 在 bib 中但未在正文引用 [R1, R2 一致]\n4. **5 条引用 mismatch**: alemohammad2024_mad, garces_arias2025_decoding_decoded, he2021_deberta_v3 (year mismatch), llama3, guo2024_biscope [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**综合评价**: 问题定义新颖且 timely，实验执行严谨，统计实践透明，局限性报告诚实——这些是论文的核心优势。但两个结构性限制压制了评分：(1) 生态效度差距（controlled full-replacement chain vs real-world accumulation）使方法的实际适用性存疑；(2) 跨策略迁移在 d1-d3 仅 45.9%，在最常见的部署场景（策略未知）下深度估计接近随机。方法上无算法创新（标准 RF + 标准特征），核心贡献在 task formalization + systematic empirical analysis 层面。适合 Findings 发表，距 Main Conference 需要：(a) 缩小生态效度差距（accumulation setting 实验），或 (b) 解决 cross-strategy 瓶颈（robust strategy-invariant features），或 (c) 提出有算法新颖性的 depth estimation 方法。\n\n---\n\n## Detailed Comments (逐 Section)\n\n### Abstract\n- 信息密度过高，20+ 数字塞入约 200 词。建议重构为 3 层叙事（problem → method → key findings），保留 2-3 个关键数字。\n- \"69-86% four-class accuracy\" 应伴随 d1-d3 balanced accuracy 作为等权修正。\n- \"cross-model transfer reaches 66.4% (2.7× chance)\" 中 d1-d3 (55.4%) 应提升到同等位置。\n\n### Introduction (§1)\n- 叙事线清晰：递归循环 → 工具空白 → fingerprint 发现 → 贡献。\n- \"empirical study and problem formalization rather than an algorithmic contribution\" 的自我定位恰当且诚实。\n- Contribution 列表第 3 点过于冗长，数字细节应移至正文。\n\n### Related Work (§2)\n- 覆盖全面（67 references），positioning 准确。\n- 补充引用 Muennighoff et al. (2024) 和 Ilyas et al. (2022)。\n\n### Method (§2)\n- Problem definition 形式化清晰。建议增加 full-replacement vs accumulation 区分。\n- EDD 定义数学自洽。T=0.70 选择应添加独立依据讨论。\n- 19 features 的 effective dimensionality ~4-5 是重要发现，应更突出。\n\n### Theory (§3.1)\n- Temperature d1 ≈ nucleus d2 (92.2 vs 92.3) 的验证有力但为 cherry-picked 单一比较。\n\n### Atlas (§4)\n- Strategy effect (9.3pp) > model effect (7.2pp) 是有趣发现。\n- Feature importance 应以 group 而非 individual 为核心叙事。\n- Feature trajectory 图应从 Appendix 移回正文。\n\n### Generalization (§5)\n- Baseline comparison 全面公平。Classifier convergence 证明 feature-determined ceiling。\n- Cross-model d2 recall (26.8-52.6%) 是最大弱点。\n- Cross-strategy failure 是论文最重要的负面结果，framing 应更突出。\n- Cross-scale 标记 \"Preliminary\" 恰当，应进一步降调。\n\n### Discussion (§7)\n- 仅一段约 80 词，远不够。需扩展至 3-4 段。\n\n### Limitations\n- 覆盖广泛且诚实，特别是 domain-dependent FPR 和 adversarial robustness 的承认。\n- 建议增加 full-replacement vs accumulation 作为 top-level limitation。\n\n### Appendix\n- 信息量极大。Temperature robustness 中 \"memorization as prerequisite\" (τ=1.1) 是重要机制洞察。\n- Domain bias analysis 是亮点。\n- Feature extraction GPU/CPU 声明需核实。\n\n### 格式合规\n- ACL review template ✓, double-blind ✓, Anonymous ✓\n- 清理孤立 bib entry c2pa2024；核实 5 条引用 mismatch。\n",
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 12 (Fresh Review)\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 Main Conference (ARR May cycle)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了一个 180K 样本基准（3 模型族 × 3 解码策略 × 4 深度），用 Random Forest 在 19 个统计特征上实现 69-86% 四分类准确率（chance=25%）。论文定义了 Effective Discriminable Depth (EDD) 度量，构建了 Depth Degradation Atlas，并在 8 个泛化维度上进行系统评估。这是一项问题定义新颖、实验执行严谨、报告透明诚实的实证研究，但在生态效度、跨策略部署和规模可扩展性方面存在结构性限制。\n\n---\n\n## Strengths\n\n**S1. 任务定义的原创性 [R1, R2 一致]。** 递归生成深度估计是一个真正未被研究过的问题，填补了 model collapse 理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。EDD 度量的形式化（Definition 1, Eq. 1）数学自洽且有概念价值。\n\n**S2. 系统性实验设计 [R1, R2 一致]。** 3×3 model-strategy grid × 4 depths = 180K 样本，加上 8 个泛化轴（cross-model, cross-strategy, cross-scale, cross-domain, cross-model chains, prompted generation, seed replication, depth extension），构成了非常全面的实验矩阵。基线覆盖四类方法且对比公平。\n\n**S3. 统计实践透明 [R1 主导, R2 认同]。** Bootstrap 95% CI 贯穿主要结果；domain bias 分析的三子实验设计严谨；初始 bug 透明报告并修复；RF seed robustness 验证（std=0.06pp）。\n\n**S4. 诚实的局限性讨论 [R1, R2 一致]。** d0 膨胀、cross-strategy 失败、14B EDD=0、5 个 cross-scale 混杂因素、单 LoRA 种子不确定性、curation PoC 非显著——均被如实报告。Limitations 覆盖 12+ 个具体限制。\n\n**S5. 理论-实证对应 [R1 主导]。** tail erosion 理论预测与 9/9 cells 的 p90_ppl top-2 ranking 对应；temperature d1 median p90_ppl (92.2) 与 nucleus d2 median (92.3) 的精确匹配验证了 strategy-dependent convergence 理论。\n\n**S6. 特征重要性三重验证 [R1 主导]。** Gini/SHAP/permutation 三种方法的一致性（Kendall's W=0.90, p<0.005）增强了核心发现的可信度。\n\n**S7. Related Work 覆盖充分 [R2 主导]。** 67 条引用覆盖 model collapse、AI text detection、membership inference、ordinal classification、decoding strategies 五个维度，达到 EMNLP 标准。\n\n---\n\n## Weaknesses\n\n### Must-Fix (2 项)\n\n**W1. 生态效度差距过大，需更清晰的 scope 声明 [R1-W1, R2-W2; AGREE]。**\n基准使用 Wikipedia 种子 + LoRA fine-tune 的 full-replacement recursive chain（每步完全替换训练数据）。真实世界的递归污染涉及 accumulation（混合真实+合成数据）、全量微调、混合语料、未知比例。论文 Limitations 有承认但 framing 不够突出。\n- **要求**: Abstract/Introduction 明确声明 full-replacement chain 的 scope 限制；Discussion 增加 accumulation setting 讨论。\n\n**W2. Cross-strategy transfer 在部署场景下近乎失败 [R1-W2; R2 交叉升级认同]。**\nd1-d3 balanced accuracy 仅 45.9%（chance=33%），出现 d1/d2 boundary inversion（d1v2 AUC < 0.5）。在实际部署中解码策略几乎总是未知的。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。论文标题以 \"estimating recursive generation depth\" 为核心 claim，但在最常见场景下该 claim 实质不成立。\n- **要求**: Abstract 补充 d1-d3 balanced accuracy 到同等显著位置；将 cross-strategy bottleneck 从 limitation 提升为独立贡献/发现。\n\n### Should-Fix (7 项)\n\n**W3. d0 膨胀导致 headline metrics 误导 [R1-W3, R2-W6; AGREE]。**\nd0 recall >97% 使 4-class accuracy 和 cross-model transfer 66.4% 被系统性抬升。d1-d3 balanced accuracy（within-distribution 71.6%, cross-model 55.4%, cross-strategy 45.9%）才是评估实际能力的关键数字。\n- **要求**: 所有 headline 数字旁系统性并列 d1-d3 balanced accuracy。\n\n**W4. Cross-scale 证据不足 [R1-W4 Should-Fix, R2-W1 Must-Fix; Director 裁定 Should-Fix]。**\n仅 3 个 7-14B 模型，5 个混杂因素同时存在（QLoRA、样本量、仅 nucleus、vocabulary mismatch、14B 自参考）。两个 7-8B 模型 AUC 轨迹完全不同（Llama monotonic vs Qwen U-shaped），无法确定主流 pattern。14B 的 EDD=0 因自参考混杂不可直接与 1-1.5B 比较。\n- **Director 裁定理由**: R2 将 14B EDD=0 视为 \"致命瓶颈\" 并推断 70B+ 必然失效，但 R1 正确指出 14B 自参考混杂使该数据点不可靠，scale effect 和 reference model effect 未被分离。在混杂未分离前，两种推断均缺乏充分依据。论文已标记为 \"Preliminary\"，应进一步降调。\n- **要求**: Abstract/Contributions 降调 cross-scale claim；声明 \"cross-scale results are confounded and should be interpreted as existence proofs\"；若可能用 Pythia-1.4B 作为 14B reference 补充实验。\n\n**W5. Curation PoC 主比较不显著 [R1-W5, R2-W7; AGREE]。**\nRF vs unfiltered p=0.407, d_z=0.41。RF vs random 的 3 个比较未做多重校正（Bonferroni 后 borderline non-significant）。\n- **要求**: 标记为 inconclusive；应用 Bonferroni 校正；Discussion 中不以 \"feasible\" 描述 depth-graduated filtering。\n\n**W6. Abstract 信息过载 [R1-Detailed, R2-W4; AGREE]。**\n约 200 词塞入 20+ 数字和多层嵌套括号。\n- **要求**: 重写 Abstract，保留 2-3 个关键数字，分为 problem-method-result 三层叙事。\n\n**W7. Discussion 实质缺失 [R1-Detailed, R2-W5; AGREE]。**\nSection 7 仅一段约 80 词，核心讨论被放逐到 Appendix Extended Discussion。\n- **要求**: 扩展至 3-4 段，涵盖 accumulation setting、model collapse mitigation 交互、部署 roadmap。\n\n**W8. 多重共线性下 feature importance framing 不当 [R1-W6; R2 partially agree]。**\nVIF>10 的 14-16/19 features 使 individual Gini importance 不可靠，但正文以 \"p90_ppl ranks top-2 in 9/9 cells\" 为核心叙事。三重验证（Kendall's W=0.90）缓解了 validity 问题，但 framing 应以 feature group 而非 individual feature 为分析单位。\n\n**W9. 算法贡献定位需强化 [R2-W3 Must-Fix; R1 REBUT; Director 裁定 Should-Fix]。**\nRF/XGBoost/LightGBM 在 0.4pp 内收敛，说明分类器选择不构成贡献。\n- **Director 裁定理由**: R1 的反驳有理——论文明确自我定位为 \"empirical study and problem formalization\"，*ACL 有 benchmark/analysis paper 先例（RAID, M4-SemEval）。Classifier convergence 恰恰证明核心贡献在 feature design + task formalization。这是 positioning 问题而非缺陷，不应列为 Must-Fix。\n- **要求**: Introduction 强化 empirical study + problem formalization 定位。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **生态效度差距是最核心的结构性问题**（R1-W1 ≡ R2-W2）\n2. **d0 通胀系统性抬升 headline metrics**（R1-W3 ≡ R2-W6）\n3. **Cross-strategy 在 d1-d3 近乎失败（45.9%）是部署的根本障碍**\n4. **Curation PoC 统计不显著（p>0.4）**（R1-W5 ≡ R2-W7）\n5. **Abstract 过载 + Discussion 缺失是写作层面最大问题**\n6. **Prompted generation 验证仅 1/9 cells 不足**\n7. **Overall 3.0 (Findings) — 两位 Reviewer 评分完全一致**\n\n## Reviewer Divergence [REBUT]\n\n1. **算法贡献是否构成 Must-Fix**: R2 认为 Must-Fix（\"方法论贡献几乎为零\"），R1 REBUT（benchmark paper 有先例，classifier convergence 证明 feature value）。**Director 采纳 R1 立场**——降级为 Should-Fix (W9)。\n\n2. **14B scale 瓶颈的严重程度**: R2 列 Must-Fix（\"致命\"，推断 70B+ 必然失效），R1 列 Should-Fix（自参考混杂使数据不可靠）。**Director 采纳折中立场**——Should-Fix (W4)，14B 数据因混杂不可直接推断。\n\n3. **AI 写作痕迹 (R2-W8)**: R1 REBUT（无具体例子，作者已声明使用 AI 辅助）。**Director 采纳 R1 立场**——不列入 weakness，但建议作者自查 dash 和 -ing phrases。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1 [R1].** Accumulation setting（混合真实+合成数据训练）下深度信号预期如何变化？\n\n**Q2 [R1].** Cross-model chain 的 84.75% 中有多少来自 depth signal vs architecture shift？能否通过与 single-model chain 对比做定量分解？\n\n**Q3 [R1].** 为什么 d3 recall 一致高于 d2？是否因为 d3 有更多独特退化信号？\n\n**Q4 [R1].** Feature extraction \"requires no GPU\" 的声明是否准确？Pythia-1.4B forward pass for 5000×512 tokens 在 CPU 上是否真的只需 2 分钟？\n\n**Q5 [R1].** 不同深度数据间的间接统计依赖关系对 CV 独立性假设有何影响？\n\n**Q6 [R2].** 14B 的 higher-order moments 成为 top features 是否暗示了 feature adaptation 策略？\n\n**Q7 [R2].** τ=1.1 时 depth signal 消失——高 temperature 能否有效规避 depth estimation？代价是什么？\n\n---\n\n## Missing References\n\n1. **Muennighoff et al. (2024)** \"Scaling Data-Constrained Language Models\" — data mixing 与 scale-dependent attenuation 相关 [R2]\n2. **Ilyas et al. (2022)** \"Datamodels\" — data attribution 与 provenance toolkit 相关 [R2]\n3. **孤立 bib entry**: c2pa2024 在 bib 中但未在正文引用 [R1, R2 一致]\n4. **5 条引用 mismatch**: alemohammad2024_mad, garces_arias2025_decoding_decoded, he2021_deberta_v3 (year mismatch), llama3, guo2024_biscope [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**综合评价**: 问题定义新颖且 timely，实验执行严谨，统计实践透明，局限性报告诚实——这些是论文的核心优势。但两个结构性限制压制了评分：(1) 生态效度差距（controlled full-replacement chain vs real-world accumulation）使方法的实际适用性存疑；(2) 跨策略迁移在 d1-d3 仅 45.9%，在最常见的部署场景（策略未知）下深度估计接近随机。方法上无算法创新（标准 RF + 标准特征），核心贡献在 task formalization + systematic empirical analysis 层面。适合 Findings 发表，距 Main Conference 需要：(a) 缩小生态效度差距（accumulation setting 实验），或 (b) 解决 cross-strategy 瓶颈（robust strategy-invariant features），或 (c) 提出有算法新颖性的 depth estimation 方法。\n\n---\n\n## Detailed Comments (逐 Section)\n\n### Abstract\n- 信息密度过高，20+ 数字塞入约 200 词。建议重构为 3 层叙事（problem → method → key findings），保留 2-3 个关键数字。\n- \"69-86% four-class accuracy\" 应伴随 d1-d3 balanced accuracy 作为等权修正。\n- \"cross-model transfer reaches 66.4% (2.7× chance)\" 中 d1-d3 (55.4%) 应提升到同等位置。\n\n### Introduction (§1)\n- 叙事线清晰：递归循环 → 工具空白 → fingerprint 发现 → 贡献。\n- \"empirical study and problem formalization rather than an algorithmic contribution\" 的自我定位恰当且诚实。\n- Contribution 列表第 3 点过于冗长，数字细节应移至正文。\n\n### Related Work (§2)\n- 覆盖全面（67 references），positioning 准确。\n- 补充引用 Muennighoff et al. (2024) 和 Ilyas et al. (2022)。\n\n### Method (§2)\n- Problem definition 形式化清晰。建议增加 full-replacement vs accumulation 区分。\n- EDD 定义数学自洽。T=0.70 选择应添加独立依据讨论。\n- 19 features 的 effective dimensionality ~4-5 是重要发现，应更突出。\n\n### Theory (§3.1)\n- Temperature d1 ≈ nucleus d2 (92.2 vs 92.3) 的验证有力但为 cherry-picked 单一比较。\n\n### Atlas (§4)\n- Strategy effect (9.3pp) > model effect (7.2pp) 是有趣发现。\n- Feature importance 应以 group 而非 individual 为核心叙事。\n- Feature trajectory 图应从 Appendix 移回正文。\n\n### Generalization (§5)\n- Baseline comparison 全面公平。Classifier convergence 证明 feature-determined ceiling。\n- Cross-model d2 recall (26.8-52.6%) 是最大弱点。\n- Cross-strategy failure 是论文最重要的负面结果，framing 应更突出。\n- Cross-scale 标记 \"Preliminary\" 恰当，应进一步降调。\n\n### Discussion (§7)\n- 仅一段约 80 词，远不够。需扩展至 3-4 段。\n\n### Limitations\n- 覆盖广泛且诚实，特别是 domain-dependent FPR 和 adversarial robustness 的承认。\n- 建议增加 full-replacement vs accumulation 作为 top-level limitation。\n\n### Appendix\n- 信息量极大。Temperature robustness 中 \"memorization as prerequisite\" (τ=1.1) 是重要机制洞察。\n- Domain bias analysis 是亮点。\n- Feature extraction GPU/CPU 声明需核实。\n\n### 格式合规\n- ACL review template ✓, double-blind ✓, Anonymous ✓\n- 清理孤立 bib entry c2pa2024；核实 5 条引用 mismatch。\n",
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-19T03:13:22.648370+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4519
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-19T03:13:32.697114+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 初始化 + 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成初始化和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排并派发任务', 'status': 'completed', 'activeForm': '完成 Reviewer 编排和任务派发'}, {'content': 'Step 1: 等待 Reviewer 1 和 Reviewer 2 独立审稿返回', 'status': 'completed', 'activeForm': '两位 Reviewer 审稿已返回'}, {'content': 'Step 2: 交叉分享 — 将每位 Reviewer 原文转发给对方', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': 'Step 3: 收敛判断 — 检查共识与分歧', 'status': 'completed', 'activeForm': '审稿意见已收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 初始化 + 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成初始化和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排并派发任务', 'status': 'completed', 'activeForm': '完成 Reviewer 编排和任务派发'}, {'content': 'Step 1: 等待 Reviewer 1 和 Reviewer 2 独立审稿返回', 'status': 'completed', 'activeForm': '两位 Reviewer 审稿已返回'}, {'content': 'Step 2: 交叉分享 — 将每位 Reviewer 原文转发给对方', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': 'Step 3: 收敛判断 — 检查共识与分歧', 'status': 'completed', 'activeForm': '审稿意见已收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-19T03:13:32.697647+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 928 · 2026-05-19T03:13:45.169372+00:00_

**Round 12 审稿完成。**

审稿报告已投递给 Research Director。

**结果摘要**：
- **Overall**: 3.0 (Findings)，两位 Reviewer 评分一致
- **Must-Fix (2)**：生态效度 scope 声明 + cross-strategy 部署障碍的 framing
- **Should-Fix (7)**：d0 膨胀、cross-scale 证据不足、curation PoC 不显著、Abstract 过载、Discussion 缺失、multicollinearity framing、算法贡献定位
- **Minor (8)**：EDD threshold 依据、RF ordinal claim、reference model ablation、prompted validation 覆盖、feature trajectory 图位置、孤立引用、GPU 声明、遗漏文献
- **Director 裁定 3 项分歧**：算法贡献降级 Should-Fix（定位问题非缺陷）；14B scale 裁定 Should-Fix（自参考混杂使数据不可靠）；AI 写作痕迹不列入 weakness
- **Issue Tracker**: 18 条 issue 已写入 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 929 · 2026-05-19T03:13:47.896537+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。两位 Reviewer 在生态效度、d0 通胀、Curation PoC 不显著性和 Overall 3.0 (Findings) 上高度一致。主要分歧在 RF ordinal claim（我倾向 REBUT）和规模瓶颈严重性（我评估更高）。互补方面，R1 补充了统计方法论细节（VIF、EDD threshold），我补充了新颖性和写作质量评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 930 · 2026-05-19T03:13:57.699342+00:00_

审稿流程已全部完成。

**Round 12 审稿结果汇总**：

- **Overall**: 3.0 (Findings)，两位 Reviewer 评分完全一致
- **Must-Fix**: 2 项（生态效度 scope 声明、cross-strategy 部署障碍的 framing）
- **Should-Fix**: 7 项（d0 膨胀、cross-scale 证据、curation PoC、Abstract 过载、Discussion 缺失、多重共线性 framing、算法贡献定位）
- **Minor**: 8 项
- **Issue Tracker**: 18 条 issue 已写入 `review_issues.yaml`
- **审稿报告**: 已投递至 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 97

## Round 97

62 recorded events


### User

_source line 931 · 2026-05-19T06:32:02.009574+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-19T06:32:10.999911+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-19T06:32:11.000555+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-19T06:32:14.866310+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-19T06:32:14.866673+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-19T06:32:15.168045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-19T06:32:15.218672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-19T06:32:20.492048+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-19T06:32:21.897963+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (118 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| qwen25_14b_temp09 | Recursive generation depth signal persists at 14B scale under temperature sampling (τ=0.9), achieving RF 4-class accuracy above 25% baseline and comparable to scale_002 nucleus (54.05%). Validates Claim 2: Atlas spans 3 strategies at 14B. Directly addresses Dream worst review M3 \"14B too narrow\". | — | — | — |\n| qwen25_14b_topk50 | Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **lr_zscore_cross_strategy_001** (negative): LR cross-strategy LOO + z-score: 验证 paper_framing 声称的 z-score 恢复 LR d1v2 AUC（GPT-2 XL 0.13→0.68, OLMo 0.25→0.83）。论文 claim 硬依赖。 ← 基于 cross_strategy_loo_zscore_001\n  [lr_zscore_cross_strategy_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/lr_zscore_cross_strategy_001/data/lr_zscore_cross_strategy_point
…[truncated 1832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-19T06:32:22.049066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-19T06:32:22.853374+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-19T06:32:22.853726+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 943 · 2026-05-19T06:32:23.255687+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 944 · 2026-05-19T06:32:28.276698+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 submission guidelines and ARR-related deadlines. Here's what 
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5422
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-19T06:32:28.277672+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml\", \"content\": \"# Literature Map — recursive_gen_depth_est\\n# Last updated: 2026-05-15\\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\\n#\\n# Tags used for cite_in: introduction, related-work, background, method,\\n#   experiments, discussion, limitations, dcol-section\\n\\n# =============================================================\\n# MODEL COLLAPSE — foundational theory & recursive generation\\n# =============================================================\\n\\nshumailov2024_nature:\\n  title: \\\"AI models collapse when trained on recursively generated data\\\"\\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\\n  venue: Nature\\n  year: 2024\\n  doi: \\\"10.1038/s41586-024-07566-y\\\"\\n  tags: [model-collapse, recursive-generation, tail-erosion]\\n  relevance: direct\\n  cite_in: [introduction, related-work, background]\\n  notes: >\\n    Foundational model collapse paper. Tail erosion across recursive generations.\\n    Perplexity monotonically increases over 40 generations. Does NOT compare\\n    sampling strategies—uses standard sampling (T=1).\\n\\nmarchi2024_heat_death:\\n  title: \\\"Heat Death of Generative Models in Closed-Loop Learning\\\"\\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\\n  venue: ICASSP 2025\\n  year: 2024\\n  arxiv: \\\"2404.02325\\\"\\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\\n  relevance: direct\\n  cite_in: [discussion]\\n  notes: >\\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\\n    support for our tau=0.9 accelerated convergence finding.\\n\\ndohmatob2024_tale_of_tails:\\n  title: \\\"A Tale of Tails: Model Collapse as a Cha
…[truncated 11201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5021
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-19T06:32:35.145146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limits author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limits author instructions"
  }
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-19T06:32:35.547149+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference dates commitment deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference dates commitment deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-19T06:32:37.555222+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-19T06:32:37.555595+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 950 · 2026-05-19T06:32:41.722731+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limits author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found information about the ACL Rolling Review submission guidelines. Here are the key points regarding submission requirements for 2026:

## Key Submission Guidelines

**Page Limits:**
The search results reference that submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected. However, the specific p
…[truncated 1055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6577
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-19T06:32:42.326165+00:00_

Web search results for query: "EMNLP 2026 conference dates commitment deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the information about EMNLP 2026 conference dates, commitment deadline, and ARR cycle:

## Conference Dates
EMNLP 2026 will be held October 24-29, 2026 in Budapest, Hungary.

## Key Deadlines

**ARR Submission:**
The ARR submission deadline for long and short papers is May 25, 2026.

**Commitment Deadline:**
The EMNLP commitme
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6779
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-19T06:32:48.755032+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines: page limits for long papers and short papers (main text, references, appendix), formatting template requirements, anonymity rules, limitations section requirement, ethics statement requirement, responsible NLP checklist requirement, and any other mandatory requirements. Be specific about page numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines: page limits for long papers and short papers (main text, references, appendix), formatting template requirements, anonymity rules, limitations section requirement, ethics statement requirement, responsible NLP checklist requirement, and any other mandatory requirements. Be specific about page numbers."
  }
}
```

</details>

---


### Tool call

_source line 953 · 2026-05-19T06:32:50.012471+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements for EMNLP 2026 main conference: page limits, formatting, commitment deadline, ARR cycle deadline, anonymous requirements, topics, and any special rules. Include all dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements for EMNLP 2026 main conference: page limits, formatting, commitment deadline, ARR cycle deadline, anonymous requirements, topics, and any special rules. Include all dates."
  }
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-19T06:32:50.916755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-19T06:32:51.067827+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning 3 model families, 3 decoding strategies, and 4 depths under controlled full-replacement recursive chains at the 1--1.5B scale.
4	A Random Forest over 19 statistical features, dominated by the perplexity tail family (\texttt{p90\_ppl}, \texttt{var\_surprisal}), achieves 69--86\% four-class accuracy (d1--d3 balanced: 59--82\%; chance = 25\%/33\%); the convergence of RF, XGBoost, and LightGBM within 0.4\,pp confirms that discriminative signal resides in feature design, not classifier choice.
5	Cross-model transfer reaches 66.4\% four-class (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, and a single-cell prompted-generation test 69.5\%.
6	Cross-strategy transfer (59.1\%, d1--d3: 45.9\%) reveals that decoding strategies induce structurally distinct degradation trajectories, a finding we formalize via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families).
7	Preliminary cross-scale experiments (7--14B, 54--70\%) provide an existence proof that depth signal persists at larger scales, though confounded by five factors including quantization and vocabulary mismatch.
8	Binary detectors and membership inference baselines (30--35\%) fall ${>}$43\,pp below our pipeline, confirming that ordinal depth estimation requires distributional statistics inaccessible from surface text.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-19T06:32:51.118563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-19T06:32:51.169292+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We study this question under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
11	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
12	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
13	No exi
…[truncated 3395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 958 · 2026-05-19T06:32:54.834301+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- Main text: "up to eight (8) pages of content"
- References: unlimited pages
- Limitations section: unlimited, placed after conclusion (required, does not count toward limit)
- Ethical considerations section: unlimited, optional (does not count toward limit)
- Total: 8 pages of content maximum

**Short Papers:**
- Main text: "up to four (4) pages of content"
- References: unlimited pages
- Limitations section: unlimited, placed after conclusion (required, does not count toward limit)
- Ethical considerations section: unlimited, optional (does not count toward limit)
- Total: 4 pages of content maximum

## Formatting Requirements

Papers must use "the official ACL style template" available on GitHub and follow ACL author guidelines. No modifications to style files or alternative templates are permitted. Submissions failing to meet formatting standards face rejection without review.

## Anonymity Rules

Papers must exclude author names and affiliations. Self-references revealing identity (e.g., "We previously showed") should be rewritten as third-person citations. Supplementary materials must be anonymized, with cloud services (Dropbox, Google Drive) prohibited due to download tracking.

## Mandatory Sections

**Limitations Section:** Required for both long and short papers. Must discuss work constraints in a dedicated section at paper's end, before references. Papers lacking this section receive desk rejection.

**Responsible NLP Checklist:** Authors must complete this mandatory checklist during submission. Incorrect, incomplete, or misleading responses result in desk rejection.

**Ethics Statement:** Encouraged but optional section discussing ethical impacts and broader implications of the work.

## Other Mandatory Requirements

- Two-way anonymized review compliance
- No concurrent submissions to other venues
- Original, unpublished work with no more than 10% text overlap with prior publi
…[truncated 120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 6079
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-19T06:32:55.989254+00:00_

# EMNLP 2026 Main Conference Submission Requirements

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Camera-ready versions:** +1 additional page allowed (9 pages for long, 5 pages for short)

## Key Deadlines
- **ARR Submission:** May 25, 2026 (11:59 PM UTC-12:00)
- **Reviewer Registration:** May 27, 2026
- **Author Response Period:** July 7-13, 2026
- **Meta-review Release:** July 30, 2026
- **EMNLP Commitment:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-ready Due:** September 20, 2026
- **Conference Dates:** October 24-29, 2026

## Anonymity Requirements
The review process maintains "double-blind" standards where "reviewers will not see authors, nor will authors see reviewers." No anonymity period is required following ACL and ARR policies.

## Major Topic Areas
The conference welcomes work across diverse NLP domains including machine translation, dialogue systems, information extraction, language modeling, LLM agents, multilingual NLP, and multimodality.

## Special Theme Track
"New Missions for NLP Research" emphasizing rethinking evaluation methodologies, moving from models to systems, scientific understanding of language and cognition, data governance, and LLMs as research tools.

## Critical Rules
- Dual submissions are prohibited
- Author lists cannot be modified during commitment (reordering only)
- Papers must address responsible NLP research and publication ethics standards
- At least one presenting author must register by early registration deadline

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5976
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-19T06:33:01.410526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-19T06:33:01.862767+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt
…[truncated 2904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-19T06:33:01.913471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-19T06:33:02.365597+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 5915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-19T06:33:02.366046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-19T06:33:02.617429+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-19T06:33:02.668069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-19T06:33:02.718826+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$).}
22	\label{tab:main_matrix}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
27	\midrule
28	Pythia-1.4B  & 78.7{\scriptsize$\pm$0.6}\,(
…[truncated 8458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-19T06:33:07.548667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-19T06:33:07.851079+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
10	RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell, confirming a feature-determined ceiling; on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).
11	
12	\paragraph{Binary detectors and membership inference.}
13	Four binary detection/membership inference methods, calibrated for ordinal depth, all fall 43--48\,pp below RF (Table~\ref{tab:baselines}).
14	Min-K\% Prob \cite{shi2024_minkprob} (33.2\%) outperforms DetectGPT \cite{mitchell2023_detectgpt} (30.7\%), but CORAL ordinal calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%), confirming the bottleneck is input signal, not calibration (Appendix~\ref{app:detector_baselines}).
15	Adding Min-K\% as a 20th RF feature yields only +0.48\,pp (78.4\%$\to$78.9\%); the 19 statistical features already capture the dominant ordinal signal.
16	
17	\paragraph{Surface-text ablation.}
18	Single-feature regression on mean perplexity performs at chance (25.1\%); zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%) also fail (43\,pp below the best RF cell; Appendix~\ref{app:zeroshot_prompt}); depth signal resides in distributional statistics inaccessible from surface text.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\caption{Ordinal depth estimation: method comparison (mean across 9 atlas cells; DetectGPT: 8 of 9, Pythia nucleus excluded due to scoring instability). Chance = 25\% (4-class) / 33.3\% (d1--d3). Min-K\%: $K{=}20$, CORAL calibration. D
…[truncated 5079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-19T06:33:07.851462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-19T06:33:08.353581+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
5	The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families (confirmed by 5-class extension, 71--80\%; Appendix~\ref{app:depth4_ext}); cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while binary detectors and membership inference methods achieve only 30--35\%.
6	
7	\paragraph{Accumulation settings.}
8	Our benchmark uses full-replacement chains; in practice, model training involves accumulation, mixing human data with synthetic outputs at unknown proportions \cite{gerstgrasser2024_accumulate}.
9	Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties, slowing tail erosion.
10	The 66.4\% cross-model and 59.1\% cross-strategy transfer should be interpreted as ceiling estimates for the mixed-data regime.
11	Extending the framework to accumulation, where depth becomes a continuous mixing parameter, is a priority for future work.
12	
13	\paragraph{Scale and deployment implications.}
14	The depth signal attenuates with model scale: at 14B, d0/d1 separability drops sharply ($\mathrm{EDD}_{0.70}{=}0$), though d1--d3 discrimination persists above chance.
15	This suggests that depth estimation complements rather than replaces binary detection for practical data auditing: binary detectors handle the human-vs-machine boundary where depth estimation is redundant ($>$97\% d0 recall), while depth estimation provides the finer ordinal resolution that binary methods cannot.
16	A practical deployment path proceeds from controlled settings, where model and strategy are known, to partially known settings via strategy-identification routing, to fully unknown settings requiring strategy-invariant features (Appen
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-19T06:33:08.504682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-19T06:33:08.806423+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus. Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions across iterations \cite{gerstgrasser2024_accumulate}. Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties. Our results therefore represent an upper bound on feature separability; extending the framework to accumulation settings, where depth becomes a continuous mixing parameter, is a priority for future work.
6	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}), as our framework assumes uniform depth per passage.
7	
8	\paragraph{Controlled experimental setting.}
9	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination.
10	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
11	Cross-scale experiments (7--14B, \S\ref{sec:gen:crossscale}) show signal that attenuates with scale; at 14B, d0/d1 separability nearly vanishes ($\mathrm{EDD}_{0.70}{=}0$) while d1--d3 discrimination persists; this constitutes a boundary condition for the current feature set (confounded by five factors; Appendix~\ref{app:cross_scale_confounds}).
12	
13	\paragraph{Cross-strategy deployment constraint.}
14	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
15	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random 
…[truncated 6195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-19T06:33:08.806915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-19T06:33:09.209341+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 57037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-19T06:33:16.750273+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 977 · 2026-05-19T06:33:16.750718+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 978 · 2026-05-19T06:33:16.851503+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml\", \"content\": \"_next_id: 44\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 14:03 UTC\\n  summary: MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase\\n  rationale: Pythia-1.4B 4-depth pipeline 验证核心假设：4-class acc 78.2% (>>40% threshold),\\n    d1v2 AUC 0.861 (>>0.6 threshold)。控制实验排除域混淆（过滤代码后 acc 提升至 81.6%）。Top 特征为 surprisal\\n    variance 和 perplexity percentiles，说明信号来自分布窄化而非内容差异。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_pythia_002\\n    role: primary\\n    result: 4-class acc 78.2%, d1v2 AUC 0.861, content-type control 81.6%\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:01 UTC\\n  summary: Dream 三档分析完成：6项结构性必修+framing重心从DCOL转向Atlas/EDD\\n  rationale: Dream dream_20260514T140607 full review 完成。三档(best=borderline accept\\n    3.0, median=Findings 3.0, worst=borderline Findings 2.5)一致指出6项结构性问题：(1)DCOL loss\\n    Eq.1缺repulsive term不可复现 (2)Atlas论文零图不可接受 (3)bibliography严重不足(3-10 refs,需25+) (4)d0\\n    confound膨胀headline metrics,需报d1-d5 acc (5)EDD threshold无sensitivity analysis (6)surprisal\\n    reference model未指定有circularity风险。三档均认为Atlas/EDD是primary contribution,DCOL incremental\\n    over CLOC——与我们的contingency plan方向一致。worst case下DCOL不显著(p=0.12),EDD=2,但任务formalization+Atlas仍可支撑Findings。关键风险：cross-model\\n    transfer在worst case降到33%。\\n  related_experiments:\\n  - exp_id: dream_20260514T140607\\n    role: dream_simulation\\n    result: best=3.0 median=3.0 worst=2.5\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 19:45 UTC\\n  summary: 要求 baselines 统一使用 DeBERTa-v3-large，消除与 DCOL 的模型规模混淆变量\\n  rationale: Reviewer 发现 DCOL 用 DeBERTa-v3-large (435M) 而 CE/CORAL baselines 用 DeBERTa-v3-base\\n    (184M)，参数量差 2.4×，审稿人必问改进来源。修改 baseline 脚本支持 large 版本实验成本极低（模型已在服务器上），可彻底解耦方法贡献与模型容量。\\n  related_experiments:\\n  - exp_id: dcol_deberta_001\\n    role: target\\n    result: pending\\n  depends_on: []\\n- id: D00
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-19T06:33:16.852008+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-19T06:33:18.258032+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-19T06:33:18.911462+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-19T06:33:19.062503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-19T06:33:19.063003+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},

…[truncated 2604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-19T06:33:25.287362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-19T06:33:25.841338+00:00_

1	issues:
2	  # ============================================================
3	  # Round 12 Issues — D043 Action Matrix locked in
4	  # ============================================================
5	
6	  - id: R12-W1
7	    summary: "生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异，需更清晰的 scope 声明"
8	    category: framing
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 12
12	    last_seen_round: 12
13	    mentions:
14	      - round: 12
15	        reviewers: [1, 2]
16	        note: "R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。"
17	    action_items:
18	      - round: 12
19	        action: "Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 段落；Limitations 提升为第一条"
20	        assigned_to: paper_agent
21	        status: in_progress
22	    resolution: ""
23	    resolution_round: null
24	
25	  - id: R12-W2
26	    summary: "Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion，策略未知场景下部署价值极低"
27	    category: experiment
28	    severity: critical
29	    status: in_progress
30	    first_raised_round: 12
31	    last_seen_round: 12
32	    mentions:
33	      - round: 12
34	        reviewers: [1, 2]
35	        note: "R1 列为 Must-Fix，R2 交叉回应中升级认同。"
36	    action_items:
37	      - round: 12
38	        action: "Abstract 并列 d1-d3 45.9%；cross-strategy bottleneck 重定位为 key empirical finding；Claim 3 措辞修改"
39	        assigned_to: paper_agent
40	        status: in_progress
41	    resolution: ""
42	    resolution_round: null
43	
44	  - id: R12-W3
45	    summary: "d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没"
46	    category: writing
47	    severity: warning
48	    status: in_progress
49	    first_raised_round: 12
50	    last_seen_round: 12
51	    mentions:
52	      - round: 12
53	        reviewers: [1, 2]
54	        note: "R1-W3 和 R2-W6 完全一致。"
55	    action_items:
56	      - round: 12
57	        action: "所有 headline 数字旁系统性并列 d1-d3 balanced accuracy"
58	        assign
…[truncated 8148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-19T06:33:25.891975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-19T06:33:25.943033+00:00_

100	}
101	
102	@inproceedings{shi2025_closer_look,
103	  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
104	  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},
105	  booktitle = {Proceedings of NeurIPS},
106	  year      = {2025},
107	  note      = {Spotlight},
108	}
109	
110	@inproceedings{yi2026_escaping_collapse,
111	  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
112	  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},
113	  booktitle = {3rd DATA-FM Workshop at ICLR 2026},
114	  year      = {2026},
115	}
116	
117	@inproceedings{muennighoff2023scaling,
118	  author    = {Muennighoff, Niklas and Rush, Alexander and Barak, Boaz and Le Scao, Teven and Piktus, Aleksandra and Tazi, Nouamane and Pyysalo, Sampo and Wolf, Thomas and Raffel, Colin},
119	  title     = {{Scaling Data-Constrained Language Models}},
120	  booktitle = {Proceedings of NeurIPS},
121	  year      = {2023},
122	}
123	
124	% --- Model collapse: collapse-can-be-avoided / contamination ---
125	
126	@inproceedings{drayson2025_detection_prevents_collapse,
127	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
128	  title     = {{Machine-generated text detection prevents language model collapse}},
129	  booktitle = {Findings of EMNLP},
130	  year      = {2025},
131	  note      = {arXiv:2502.15654},
132	  url       = {https://arxiv.org/abs/2502.15654},
133	}
134	
135	@misc{bakshi2026_collapse_improvement,
136	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
137	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
138	  year      = {2026},
139	  howpublished = {arXiv:2602.10531},
140	  url       = {https://arxiv.org/abs/2602.10531},
141	}
142	
143	@misc{wang2026_contamination,
144	
…[truncated 22878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-19T06:34:27.218928+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计声明）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数**: Long paper, 8 页正文 + 无限引用/附录\n- **模板**: ACL style template (review mode, double-blind)\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n`projects/recursive_gen_depth_est/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估论文的方法严谨性、实验设计质量和统计声明的可靠性。\n\n请重点审查以下方面：\n\n1. **实验设计**\n   - Benchmark 构建（180K 样本, 3×3 grid, d0-d3）是否存在数据泄露或系统性偏差\n   - Full-replacement chain 的 scope 声明是否充分，与 accumulation setting 的差距讨论是否到位\n   - Cross-validation 设计是否合理（5-fold stratified CV）\n   - LoRA finetuning 配置的合理性（单一超参、fresh adapter）\n\n2. **统计声明的可靠性**\n   - 所有 accuracy/AUC 数字是否有充分的置信区间和统计检验\n   - d0 recall >97% 对 headline metrics 的膨胀问题：d1-d3 balanced accuracy 是否被系统性地并列报告\n   - Cross-scale 实验（7-14B）的 5 个混杂因素是否被充分讨论\n   - Curation PoC（Appendix）主比较 p>0.4 不显著，多重比较是否校正\n   - Cross-seed replication 仅覆盖 3/9 cells，single-seed uncertainty 估计\n\n3. **方法**\n   - EDD 定义的严谨性：contiguous prefix 要求在非单调情况下是否过于保守\n   - Reference model (Pythia-1.4B) 与 generator 重叠的 circularity 风险\n   - RF ordinal claim 的强度是否与 CORAL baseline 对比证据匹配\n   - 19 features 中 14-16 个 VIF>10 高共线性下的 feature importance 解释\n\n4. **可复现性**\n   - 超参细节是否充足\n   - 代码/数据承诺（upon acceptance）\n   - 计算资源报告\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），每条标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 1-2 句总结\n- **Detailed Comments**: 按 section 逐节详细评论"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计声明）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数**: Long paper, 8 页正文 + 无限引用/附录\n- **模板**: ACL style template (review mode, double-blind)\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n`projects/recursive_gen_depth_est/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估论文的方法严谨性、实验设计质量和统计声明的可靠性。\n\n请重点审查以下方面：\n\n1. **实验设计**\n   - Benchmark 构建（180K 样本, 3×3 grid, d0-d3）是否存在数据泄露或系统性偏差\n   - Full-replacement chain 的 scope 声明是否充分，与 accumulation setting 的差距讨论是否到位\n   - Cross-validation 设计是否合理（5-fold stratified CV）\n   - LoRA finetuning 配置的合理性（单一超参、fresh adapter）\n\n2. **统计声明的可靠性**\n   - 所有 accuracy/AUC 数字是否有充分的置信区间和统计检验\n   - d0 recall >97% 对 headline metrics 的膨胀问题：d1-d3 balanced accuracy 是否被系统性地并列报告\n   - Cross-scale 实验（7-14B）的 5 个混杂因素是否被充分讨论\n   - Curation PoC（Appendix）主比较 p>0.4 不显著，多重比较是否校正\n   - Cross-seed replication 仅覆盖 3/9 cells，single-seed uncertainty 估计\n\n3. **方法**\n   - EDD 定义的严谨性：contiguous prefix 要求在非单调情况下是否过于保守\n   - Reference model (Pythia-1.4B) 与 generator 重叠的 circularity 风险\n   - RF ordinal claim 的强度是否与 CORAL baseline 对比证据匹配\n   - 19 features 中 14-16 个 VIF>10 高共线性下的 feature importance 解释\n\n4. **可复现性**\n   - 超参细节是否充足\n   - 代码/数据承诺（upon acceptance）\n   - 计算资源报告\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），每条标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 1-2 句总结\n- **Detailed Comments**: 按 section 逐节详细评论"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-19T06:34:45.740715+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18521
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-19T06:34:45.891853+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 写作完整性 + Related Work 覆盖度）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数**: Long paper, 8 页正文 + 无限引用/附录\n- **模板**: ACL style template (review mode, double-blind)\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n`projects/recursive_gen_depth_est/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估论文的新颖性、写作质量和相关工作覆盖度。\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - \"Recursive generation depth estimation\" 作为新任务的价值和动机是否充分\n   - EDD metric 的创新程度\n   - 方法层面（标准 RF + 标准统计特征）的算法贡献是否足够撑起 EMNLP Main\n   - 论文的 positioning：benchmark-driven empirical study 的定位是否清晰且有说服力\n   - 与 EditLens (ICLR 2026), DivEye (TMLR 2026) 等最新工作的区分度\n\n2. **写作质量**\n   - Abstract 是否简洁有力（150-250 words），数字堆砌问题\n   - Introduction 叙事线是否清晰（问题→洞察→方法→验证）\n   - Discussion 是否充实（不是 1 段 80 词的 stub）\n   - 专有名词首次出现是否定义\n   - AI 写作痕迹检查：em-dash/en-dash 滥用、-ing 短语结尾、过度分段、过渡词堆积\n   - 主线统一性：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否一条线\n\n3. **Related Work 覆盖度**\n   - Model collapse 理论文献是否完整（Shumailov, Dohmatob, Alemohammad 等）\n   - AI text detection 文献是否 up-to-date（2025-2026 最新检测器）\n   - Ordinal classification 基础文献是否充分\n   - 是否有重要遗漏（特别是 2025-2026 的新工作）\n   - 引用密度是否匹配 EMNLP 长文水准（通常 40+ 引用）\n\n4. **图表质量**\n   - Figure/Table 信息密度是否高\n   - Caption 是否自包含\n   - 图中字体是否可读（>=7pt）\n   - 空间效率（在 8 页限制下）\n\n5. **格式与合规**\n   - 匿名性：是否泄露作者信息\n   - Limitations 节是否实质性\n   - Ethics Statement 是否充分\n   - 页数是否在 8 页正文内\n   - 引用格式是否一致\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），每条标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 1-2 句总结\n- **Detailed Comments**: 按 section 逐节详细评论"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 写作完整性 + Related Work 覆盖度）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **页数**: Long paper, 8 页正文 + 无限引用/附录\n- **模板**: ACL style template (review mode, double-blind)\n- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n`projects/recursive_gen_depth_est/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）\n\n### 你的审查侧重\n\n**核心任务**：评估论文的新颖性、写作质量和相关工作覆盖度。\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**\n   - \"Recursive generation depth estimation\" 作为新任务的价值和动机是否充分\n   - EDD metric 的创新程度\n   - 方法层面（标准 RF + 标准统计特征）的算法贡献是否足够撑起 EMNLP Main\n   - 论文的 positioning：benchmark-driven empirical study 的定位是否清晰且有说服力\n   - 与 EditLens (ICLR 2026), DivEye (TMLR 2026) 等最新工作的区分度\n\n2. **写作质量**\n   - Abstract 是否简洁有力（150-250 words），数字堆砌问题\n   - Introduction 叙事线是否清晰（问题→洞察→方法→验证）\n   - Discussion 是否充实（不是 1 段 80 词的 stub）\n   - 专有名词首次出现是否定义\n   - AI 写作痕迹检查：em-dash/en-dash 滥用、-ing 短语结尾、过度分段、过渡词堆积\n   - 主线统一性：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否一条线\n\n3. **Related Work 覆盖度**\n   - Model collapse 理论文献是否完整（Shumailov, Dohmatob, Alemohammad 等）\n   - AI text detection 文献是否 up-to-date（2025-2026 最新检测器）\n   - Ordinal classification 基础文献是否充分\n   - 是否有重要遗漏（特别是 2025-2026 的新工作）\n   - 引用密度是否匹配 EMNLP 长文水准（通常 40+ 引用）\n\n4. **图表质量**\n   - Figure/Table 信息密度是否高\n   - Caption 是否自包含\n   - 图中字体是否可读（>=7pt）\n   - 空间效率（在 8 页限制下）\n\n5. **格式与合规**\n   - 匿名性：是否泄露作者信息\n   - Limitations 节是否实质性\n   - Ethics Statement 是否充分\n   - 页数是否在 8 页正文内\n   - 引用格式是否一致\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句论文概述\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），每条标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]\n- **Questions**: 需要作者回答的问题\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 1-2 句总结\n- **Detailed Comments**: 按 section 逐节详细评论"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-19T06:34:47.401062+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1509
}
```

</details>

---


### Assistant

_source line 992 · 2026-05-19T06:34:56.788605+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性 + 实验设计 + 统计声明）— 已发送
- **Reviewer 2**（新颖性 + 写作完整性 + Related Work 覆盖度）— 已发送

等待两位 Reviewer 完成独立初审，收到后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 993 · 2026-05-19T06:40:08.441268+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

### Summary

本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类任务，构建了一个 180K 样本的基准测试集（3 个模型族 × 3 种解码策略 × 4 个深度等级），并使用基于 19 个统计特征的 Random Forest 进行分类。论文提出了 Effective Discriminable Depth（EDD）指标来量化相邻深度的可区分性极限，并在多个泛化轴（跨模型、跨策略、跨域、跨尺度）上进行了系统实验。核心发现是困惑度尾部特征族（p90_ppl、var_surprisal）在所有 9 个 cell 中主导深度判别。

---

### Strengths

**S1: 任务形式化填补了真实空白。** 在二元检测（human vs. machine）和模型坍塌理论（假定深度已知）之间，序数深度估计是一个未被研究的新维度。EDD 指标提供了一个有操作意义的量化手段来衡量递归链上的可区分极限。这一贡献在概念层面是扎实的。

**S2: 基准设计系统且全面。** 3×3 grid（模型族 × 解码策略）覆盖了合理的变异来源，180K 样本规模充足。每个 cell 独立评估，避免了将异质信号混为一体。Depth extension 到 d5 的设计也合理。

**S3: 控制实验设计良好。** Domain bias analysis（§App F）中的 LOGO 评估和 seed-group negative control 是方法论亮点——LOGO accuracy（72.1%）与标准 CV（72.0%）匹配，seed-group 预测在 chance level（10.2%），有效排除了 topic leakage。修正 bug 后如实报告修正前后的数据（64.0% → 72.1%），体现了研究诚信。

**S4: 分类器收敛验证了特征为核心。** RF、XGBoost、LightGBM 在 0.4pp 内收敛（§5.1），加上 CORAL/DivEye 在 0.6pp 内匹配（p>0.05），有力地论证了分类信号来自特征设计而非分类器架构。

**S5: Limitations 章节异常诚实。** 论文主动讨论了 full-replacement vs. accumulation、d0 inflation、cross-strategy boundary inversion、reference model dependency、single LoRA instance、adversarial robustness 等。这种透明度在提交稿中并不常见。

**S6: 跨模型递归链实验（App J）是有价值的补充。** 异构链（Pythia→OLMo→GPT-2 XL）达到 84.75%，反向链（GPT-2 XL→OLMo→Pythia）达到 85.75%，有效排除了架构指纹假说。

---

### Weaknesses

**W1 [Must-Fix]: Reference model circularity claim 与消融数据自相矛盾。**
- 具体位置：§3.4（"confers no systematic advantage"）vs. Table 8 / Appendix H
- 问题：§3.4 声称 Pythia-1.4B 同时作为 generator 和 reference model "不带来系统性优势"，论据是 Pythia 数据（78.7%）低于 GPT-2 XL 数据（85.9%）。但这是**跨 generator 的混淆比较**——GPT-2 XL 数据准确率更高可能是因为 GPT-2 XL 产生了更强的深度信号，而非 self-reference 不帮助 Pythia。Appendix H（Table 8）的**公平消融**显示：在 Pythia 生成的数据上，self-reference（78.6%）> OLMo 参考（74.5%）> GPT-2 XL 参考（67.3%），self-reference 带来 4.1-11.3pp 的优势。Limitations 中也承认 "same-family references yield optimal performance"。
- 影响：这意味着 Pythia cell 的 78.7% 准确率可能部分来自 self-reference 的系统性优势，而非纯粹的深度信号。OLMo 和 GPT-2 XL cell 使用的是 cross-reference（Pythia-1.4B），其准确率反而可能被低估。这使得 9 个 cell 之间的横向比较不公平。
- 建议：(1) 修正 §3.4 的 claim，承认 self-reference 带来可测量的优势；(2) 在 Table 2 的 Pythia 行旁注明 self-reference；(3) 讨论使用统一 cross-reference 时所有 cell 准确率的预期变化。

**W2 [Must-Fix]: 跨尺度实验的 5 个混淆因素使其结论不可靠。**
- 具体位置：§5.4, Appendix I
- 问题：7-14B 实验引入了 5 个混淆因素（QLoRA 4-bit 量化 / 样本量 500 vs 5000 / 仅 nucleus 策略 / 词表不匹配 / 14B 使用 self-reference），且论文承认"infeasible to attribute the observed accuracy gap to any single factor"。在这种条件下：
  - 仅 2 个 7-8B 模型（Llama-3.1-8B 和 Qwen2.5-7B）给出了方向相反的 AUC 轨迹（单调 vs U 型），无法判断哪种是主流模式
  - 14B 的 EDD=0 可能完全是 self-reference + quantization 的产物，而非真正的 scale effect
  - 500 samples/depth 的 CI 宽度为 ±2pp（Table 9），Cross-scale 的准确率差异（54-70%）可能部分在噪声范围内
- 主文 §5.4 使用 "existence proof" 是恰当的，但 abstract 中 "Preliminary cross-scale experiments (7-14B, 54-70%) provide an existence proof that depth signal persists at larger scales" 的表述过于乐观——"persists" 对 14B（EDD=0, d0v1 AUC=0.643）来说言过其实
- 建议：(1) 在 abstract 中将 14B 的结果明确标记为 boundary condition 而非 "persists"；(2) 讨论 QLoRA quantization 对 perplexity distribution 的独立影响——是否有消融可以分离量化效应？(3) 增加至少一个不使用量化的 7-8B 实验作为 control

**W3 [Must-Fix]: d0 recall >97% 系统性膨胀 headline metrics，且 d1-d3 balanced accuracy 未被充分前置。**
- 具体位置：Abstract, Table 2, §4.1, §5.1-5.3
- 问题：Abstract 首句报告 "69-86% four-class accuracy"，括号内的 "d1-d3 balanced: 59-82%" 是补充说明。但 d0 recall >97% 本质上是二元检测的成功（已被 Binoculars 等工具解决），不是本文的核心贡献。核心贡献是区分 d1/d2/d3——而 d1-d3 balanced accuracy 在跨模型迁移中仅 55.4%（chance=33%），跨策略迁移中仅 45.9%。
  - Cross-model transfer: 66.4% headline → 55.4% d1-d3（下降 11pp）
  - Cross-strategy transfer: 59.1% headline → 45.9% d1-d3（下降 13.2pp）
  - 更极端的是 Pythia holdout 的 d2 recall 仅 26.8%（Table 4）
- 论文在 Limitations 中承认了 d0 inflation，但 abstract 和 contribution 列表中仍以四类准确率为主导叙事
- 建议：(1) Abstract 和 Contribution 列表中应以 d1-d3 balanced accuracy 为主指标，四类准确率作为补充；(2) Table 2 增加一列专门报告 d1-d3 balanced accuracy 的 CI；(3) 明确讨论：在 d2 recall=26.8% 的 worst case 下，深度估计的实际部署意义

**W4 [Should-Fix]: Curation PoC（Appendix K）的主要比较不显著，多重比较未充分校正。**
- 具体位置：Table 13, Table 14, Appendix K, Extended Discussion（Appendix N）
- 问题：
  - 核心比较（RF-filtered vs unfiltered）：p=0.407（rf_soft）、p=0.492（rf_moderate）、p=0.607（rf_strict），全部不显著
  - RF vs random 的 3 个 pairwise 比较（p=0.002, 0.020, <0.001）未进行 Bonferroni 校正；Appendix N 声称 "2 of 3 comparisons surviving" Bonferroni（α=0.05/3=0.017），但 rf_moderate vs random_moderate 的 p=0.020 不通过
  - 效应量微小：rf_soft vs unfiltered 的 Δ=+0.043 PPL（<0.3% relative）
  - 仅 5 seeds，power 极低
- 论文诚实地报告了 p 值并承认 "inconclusive"，但 Appendix N 的 framing（"2 of 3 surviving Bonferroni"）给读者留下了部分显著的印象
- 建议：(1) 统一使用 Bonferroni-corrected p 值，明确标注 rf_moderate vs random_moderate 不通过；(2) 在 Discussion 中将 curation 描述为 "negative result" 而非 "inconclusive preliminary evidence"；(3) 删除或大幅缩减 curation PoC 篇幅，避免读者产生误导性的实用价值预期

**W5 [Should-Fix]: VIF>10 for 14-16/19 features 下的 feature importance 解释过度。**
- 具体位置：§4.2, Table 3, footnote 3
- 问题：当 VIF>10 时，Gini importance 在高共线性特征间分配不稳定。论文的脚注承认 "individual rankings should be interpreted cautiously given high multicollinearity"，但紧接着在 Table 3 中详细报告了每个 cell 的逐个特征排名和精确 importance 值（如 .17、.15、.11）。§4.2 声称 "p90_ppl ranks top-2 by Gini importance in all 9 cells" 和 "var_surprisal in 8/9 under SHAP"——在 effective dimensionality 仅 4-5 的情况下，这些个体排名的稳定性存疑。
- group-level dominance 的 claim（perplexity tail family 主导）有 Kendall's W=0.90 支持，是可靠的
- 但 Table 3 的呈现方式暗示了比数据支持的更高的特征级别精度
- 建议：(1) 明确区分 group-level claim（可靠）和 individual feature claim（不可靠）；(2) 报告 bootstrap stability 的特征排名（重采样 1000 次后 p90_ppl 排名 top-2 的概率）；(3) 考虑使用 PCA 或 elastic net 来处理共线性后再解释 importance

**W6 [Should-Fix]: EDD 定义的 contiguous prefix 要求在非单调场景下过于保守，且无替代方案。**
- 具体位置：Definition 1（§3.5），Limitations
- 问题：EDD 要求从 (0,1) 到 (d*,d*+1) 的所有 pairwise AUC 都超过阈值 T。当 AUC profile 非单调时（如 Qwen2.5-7B 的 U 型，Limitations 中提到的 cross-strategy inversion 导致 d1v2 AUC 低至 0.129），EDD 会大幅低估真实的可区分范围。
- 对 1-1.5B 基模型，AUC 严格单调递减，EDD 表现良好。但论文将 EDD 作为通用指标推广，在 7B+ 和 cross-strategy 场景下它的保守性成为系统性偏差
- 论文在 Limitations 中承认了这一点（"extending EDD to handle non-contiguous discriminable regions is future work"），但没有提供任何替代定义或敏感性分析
- 建议：(1) 提供一个补充指标（如 "Maximum Discriminable Depth" = max{d : AUC(d,d+1) ≥ T}）来覆盖非单调场景；(2) 在 §3.5 中明确 EDD 的适用条件（monotonic AUC decay）而非仅在脚注中提及

**W7 [Should-Fix]: Cross-seed replication 覆盖不足（3/9 cells），且方向一致的 seed=43 优势未被解释。**
- 具体位置：Appendix M, Limitations
- 问题：
  - 仅 3 个 cell（Pythia/OLMo/GPT-2 XL nucleus）有 cross-seed replication；其余 6 个 cell（所有 temperature 和 top-k 配置）均为 single-seed
  - seed=43 在所有 3 个 cell 中均优于 seed=42（+0.14 到 +3.17pp），且 2/3 差异统计显著（CI 不重叠）。方向一致的偏差暗示 seed=42 可能系统性偏低，而非 seed=43 偏高
  - single-seed 不确定性为 ~1-3pp，这意味着 Table 2 中跨 cell 的许多差异（如 Pythia nucleus 78.7% vs OLMo nucleus 78.9% 仅差 0.2pp）可能完全在 seed noise 范围内
- 建议：(1) 至少对 3 个 temperature cells 补充 seed=43 replication；(2) 讨论 seed=43 系统性偏高的可能原因；(3) 在 Table 2 的 caption 中注明 single-seed uncertainty ~1-3pp

**W8 [Should-Fix]: Full-replacement scope 声明在 Introduction/Abstract 中不够前置。**
- 具体位置：Abstract（第 2 句）、Introduction §1 段 2
- 问题：Abstract 第 2 句提到 "controlled full-replacement recursive chains"，但对不熟悉模型坍塌文献的读者来说，"full-replacement" 的含义及其对实际场景的限制不明显。Introduction 在第 2 段才解释这一点，并指出 "real-world contamination typically involves partial mixing (accumulation)"。
- 论文在 Discussion 中声称 cross-model/cross-strategy transfer 应被视为 "ceiling estimates for the mixed-data regime"，但这一 claim 未经任何实验验证——accumulation 设置下的特征行为可能完全不同（不仅仅是 "attenuated"）
- "upper bound on depth signal strength" 的论证是直觉性的（full-replacement 最大化深度信号），但缺乏理论或实验支持
- 建议：(1) 在 Abstract 中明确说明这是 full-replacement 的 upper bound 结果；(2) 至少做一个 toy-scale accumulation 实验来验证 "upper bound" 假设

**W9 [Minor]: 单一 LoRA 超参数配置。**
- 具体位置：§3.2, Table 5
- 所有 9 个 cell 使用完全相同的 LoRA 配置（r=16, α=32, lr=2e-4, 3 epochs）。不同的 LoRA rank 或学习率可能改变递归链的衰退速度，从而影响深度信号强度。缺少对 rank r（如 r=4, 8, 32）或 learning rate 的敏感性分析。

**W10 [Minor]: Prompted generation 验证仅覆盖 1/9 cell。**
- 具体位置：§5.3, Appendix O
- 仅 GPT-2 XL nucleus 一个 cell 验证了 prompted generation（69.5%，-13.8pp）。13.8pp 的下降幅度不小；在 top-k 或 temperature 配置下（本已准确率较低），prompted generation 可能将准确率推向 chance level。

---

### Questions

**Q1:** Table 8（Appendix H）显示 self-reference 在 Pythia 数据上提供 4.1-11.3pp 优势。§3.4 如何将此与 "no systematic advantage" 的 claim 调和？

**Q2:** Curation PoC 中 rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正（α=0.017）下不通过，但 Appendix N 声称 "2 of 3 comparisons surviving"。请澄清具体哪两个通过了？

**Q3:** 论文声称 full-replacement 结果是 accumulation 设置的 "upper bound"。是否有任何实验或理论依据支持这一单调性假设？是否存在 accumulation 反而增强某些深度信号的可能？

**Q4:** seed=43 在所有 3 个 cell 中系统性优于 seed=42。是否检查了 seed=42 的 LoRA 训练是否有异常（如训练不收敛、outlier 比例异常）？Appendix M 提到 seed=42 下 d3 outlier 比例为 0.56%，seed=43 为 12.8%——但 seed=43 反而准确率更高，这似乎矛盾。

**Q5:** 对于 cross-strategy transfer 中 d1/d2 boundary inversion（d1v2 AUC < 0.5），两阶段 pipeline 仅恢复了 11.5pp。在策略未知的实际部署中（d1-d3: 45.9%），这一准确率是否足以支持 "data auditing" 的实用 claim？

---

### Missing References

未发现重大遗漏。Related Work 覆盖了 model collapse theory、AI text detection、membership inference、ordinal classification 和 decoding strategy effects 的主要工作。建议补充：
- 关于 synthetic data contamination in the wild 的实证研究（如果有 2025-2026 的新工作）
- 关于 LoRA 微调与模型坍塌交互的工作（如果存在）

---

### 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 1-1.5B full-replacement 范围内的实验设计扎实（LOGO control、多 baseline、多泛化轴），但 reference model circularity claim 与消融数据矛盾（W1），cross-scale 结论受 5 个混淆因素限制（W2），curation PoC 主比较不显著且多重比较校正有误（W4）。Feature importance 在高共线性下的解释超出了数据支持的范围（W5）。 |
| **Excitement** | 3.5/5 | 任务形式化是真正的新贡献，EDD 指标有操作价值。但 full-replacement 限制降低了生态效度；cross-strategy barrier（d1-d3: 45.9%）和 scale attenuation（14B EDD=0）使得从实验室到部署的路径不清晰。 |
| **Reproducibility** | 3/5 | LoRA 超参（Table 5）、RF 配置、软件版本和硬件均已报告。但：(1) 代码/数据 "upon acceptance" 未提供匿名链接；(2) Wikipedia subset 的选择方法未说明；(3) 仅 3/9 cells 有 cross-seed replication。 |
| **Confidence** | 4/5 | 我仔细阅读了论文全文和附录，熟悉 model collapse 和 AI text detection 文献。不太确定的点是 accumulation 设置下的理论预期。 |

### Overall Assessment

**Overall: 3.5 — Borderline Conference**

**一句话总结：** 任务形式化有价值且实验系统全面，但 reference model circularity 的误导性 claim、cross-scale 结论的不可靠性、以及 d0 inflation 对核心 d1-d3 性能的掩盖，使论文在方法严谨性上存在需要修复的问题。

本文的核心贡献——将递归生成深度估计形式化为序数分类并构建系统性基准——是有意义的。在 1-1.5B full-replacement 范围内的实验设计是审慎的，控制实验（LOGO、negative control、reverse chain）是亮点。但论文在几个关键点上的 claim 强度超过了数据支持：(1) reference model "no systematic advantage" 与 Table 8 矛盾；(2) cross-scale "depth signal persists" 对 14B（EDD=0）不成立；(3) d1-d3 balanced accuracy（核心指标）在跨模型/跨策略迁移中仅 55.4%/45.9%，显著低于 headline 四类准确率。修复 W1-W3 后，论文有望达到 Conference 水准。

---

### Detailed Comments（按 Section）

**Abstract:** "69-86% four-class accuracy" 应明确标注包含 d0 inflation。建议改为以 d1-d3 balanced accuracy 为主指标。"depth signal persists at larger scales" 对 14B（EDD=0）不准确。

**§1 Introduction:** 第 2 段对 full-replacement scope 的说明是必要的，但应更前置（移到第 1 段末尾或与任务定义一起出现）。Contribution 列表中的 "EDD_{0.70}=4 for all three families" 需注明这是 1-1.5B 的结果。

**§3.4 Reference model:** "confers no systematic advantage" 需要修正为 "confers a measurable advantage on same-family data (4-11pp; Appendix H) but does not drive the cross-generator accuracy ranking"。当前表述具有误导性。

**§3.5 EDD:** Definition 1 的适用条件（monotonic AUC decay）应在定义而非脚注中明确。当前脚注提到 Qwen2.5-7B 的非单调性，但读者在阅读 Definition 1 时不一定注意到这个限制。

**§4.1 In-Distribution Performance:** Table 2 的 caption 已提到 "Depth-0 recall exceeds 97%"，但建议增加 d1-d3 balanced accuracy 列以便读者直接比较。

**§4.2 Feature Consistency:** 建议将 footnote 3（multicollinearity caveat）提升为正文段落，并在 Table 3 的 caption 中明确注明 "individual feature rankings are unstable under VIF>10; group-level dominance is robust"。

**§5.1 Classifier Comparison:** "within 0.4pp" 的收敛 claim 是否经过等价性检验（如 TOST）？如果仅是 observed difference，应说明 "observed difference ≤ 0.4pp" 而非暗示统计等价。

**§5.4 Cross-Scale:** 建议将 "existence proof" 的 claim 限制为 7-8B（signal above chance），14B 明确标记为 boundary condition。当前表述 "depth signal persists at larger scales" 对 14B 不成立。

**Appendix K Curation PoC:** 建议大幅压缩或移至补充材料的 "inconclusive results" 部分。当前篇幅和位置可能给读者造成 "curation 有效" 的印象。

**Limitations:** 质量很高，建议将 reference model circularity 的更诚实表述（self-reference 4-11pp advantage）从 Limitations 提前到 §3.4 正文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 994 · 2026-05-19T06:40:16.484496+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 995 · 2026-05-19T06:40:28.444747+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心评分：**Overall 3.5（Borderline Conference）**，Soundness 3.5/5，Excitement 3.5/5，Reproducibility 3/5，Confidence 4/5。

主要发现：
- **3 个 Must-Fix**：reference model circularity claim 与 Appendix H 消融数据矛盾（self-reference 实际带来 4-11pp 优势）；cross-scale 的 5 个混淆因素使 14B 结论不可靠；d0 >97% recall 系统性膨胀 headline metrics
- **5 个 Should-Fix**：curation PoC 主比较不显著且多重比较校正有误；VIF>10 下 feature importance 解释过度；EDD contiguous prefix 在非单调场景下过于保守；cross-seed replication 仅覆盖 3/9 cells 且 seed=43 系统性偏高；full-replacement scope 在 abstract 中不够前置
- **2 个 Minor**：单一 LoRA 配置、prompted generation 仅验证 1/9 cell

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 996 · 2026-05-19T06:40:35.621264+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 100

## Round 100

6 recorded events


### User

_source line 997 · 2026-05-19T06:41:51.574025+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿完成

**Overall Assessment: 3.0 (Findings)**
**Confidence: 4/5**

### 一句话总结
论文提出了新颖且有价值的 recursive depth estimation 任务，实验全面且 reporting 诚实，但方法创新不足（标准 RF + 标准特征）、Discussion 过薄、full-replacement-only 设置限制实用性，达到 Findings 水平。

### 核心优势
- S1: 新颖且及时的任务形式化，填补 data provenance 工具链空白
- S2: 3×3×4 atlas + 8 个泛化轴的系统实验设计
- S3: 高度诚实的 reporting（d1-d3 balanced acc alongside headline, 详尽 Limitations）
- S4: Feature consistency 发现有理论意义（验证 tail erosion 预测）
- S5: Related Work 覆盖全面，69 引用

### Must-Fix 问题
- W1: Abstract 数字堆砌（20+ 数字），缺乏叙事吸引力和动机
- W2: Discussion 仅 ~200 words，无法承载 empirical study 的 insight 深度（应提升 Appendix A.17 的 provenance toolkit 讨论到正文，新增 cross-strategy barrier 和 collapse phase transition 分析）

### Should-Fix 问题
- W3: 方法层面无算法贡献（RF + 已知特征），classifier convergence (0.4pp) 证明了 ceiling
- W4: Full-replacement only，缺乏 accumulation 实验（哪怕 pilot）
- W5: "confirming that..." -ing 短语模式全文出现 9+ 次，AI 写作痕迹明显
- W6: EDD 创新程度有限（本质是 pairwise AUC + threshold + contiguous prefix）
- W7: 14B 实验 5 个 confounds，Abstract 中的描述可能误导读者

### Minor 问题
- W8: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007）
- W9: Curation PoC 未做 multiple comparison correction

### 关键问题
- Q1: 与 Mohamed et al. (2025) "Broken Telephone" 的精确区分
- Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 定义的 strategy-invariance
- Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count 效应
- Q4: EDD=4 跨三个 family 一致性有无理论基础

### 建议改进路径
若充实 Discussion（0.75-1 页）+ 补充 accumulation pilot + 消除 AI 写作痕迹，可提升至 3.5 (Borderline Conference)。

完整审稿意见已在 session 中输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-19T06:42:17.021381+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall Assessment: 3.0 (Findings), Confidence 4/5**\n\n**一句话总结:** 论文提出了新颖且有价值的 recursive depth estimation 任务，实验全面且 reporting 诚实，但方法创新不足（标准 RF + 标准特征）、Discussion 过薄、full-replacement-only 设置限制实用性，达到 Findings 水平。\n\n**Strengths:**\n- S1: 新颖且及时的任务形式化，填补 data provenance 工具链空白\n- S2: 3×3×4 atlas + 8 个泛化轴的系统实验设计\n- S3: 高度诚实的 reporting（d1-d3 balanced acc alongside headline, 详尽 Limitations）\n- S4: Feature consistency 发现有理论意义（验证 tail erosion 预测）\n- S5: Related Work 覆盖全面，69 引用\n\n**Must-Fix:**\n- W1: Abstract 数字堆砌（20+ 数字），缺乏叙事吸引力和动机\n- W2: Discussion 仅 ~200 words，无法承载 empirical study 的 insight 深度（应提升 Appendix A.17 的 provenance toolkit 讨论到正文，新增 cross-strategy barrier 和 collapse phase transition 分析）\n\n**Should-Fix:**\n- W3: 方法层面无算法贡献（RF + 已知特征），classifier convergence (0.4pp) 证明了 ceiling\n- W4: Full-replacement only，缺乏 accumulation 实验（哪怕 pilot）\n- W5: \"confirming that...\" -ing 短语模式全文出现 9+ 次，AI 写作痕迹明显\n- W6: EDD 创新程度有限（本质是 pairwise AUC + threshold + contiguous prefix）\n- W7: 14B 实验 5 个 confounds，Abstract 中的描述可能误导读者\n\n**Minor:**\n- W8: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007）\n- W9: Curation PoC 未做 multiple comparison correction\n\n**Questions:**\n- Q1: 与 Mohamed et al. (2025) \"Broken Telephone\" 的精确区分\n- Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 定义的 strategy-invariance\n- Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count 效应\n- Q4: EDD=4 跨三个 family 一致性有无理论基础\n\n---\n\n请对 R2 的每个 Weakness (W1-W9)、每个 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别关注：你是否认同 R2 将 overall 降至 3.0 (Findings) 的判断？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall Assessment: 3.0 (Findings), Confidence 4/5**\n\n**一句话总结:** 论文提出了新颖且有价值的 recursive depth estimation 任务，实验全面且 reporting 诚实，但方法创新不足（标准 RF + 标准特征）、Discussion 过薄、full-replacement-only 设置限制实用性，达到 Findings 水平。\n\n**Strengths:**\n- S1: 新颖且及时的任务形式化，填补 data provenance 工具链空白\n- S2: 3×3×4 atlas + 8 个泛化轴的系统实验设计\n- S3: 高度诚实的 reporting（d1-d3 balanced acc alongside headline, 详尽 Limitations）\n- S4: Feature consistency 发现有理论意义（验证 tail erosion 预测）\n- S5: Related Work 覆盖全面，69 引用\n\n**Must-Fix:**\n- W1: Abstract 数字堆砌（20+ 数字），缺乏叙事吸引力和动机\n- W2: Discussion 仅 ~200 words，无法承载 empirical study 的 insight 深度（应提升 Appendix A.17 的 provenance toolkit 讨论到正文，新增 cross-strategy barrier 和 collapse phase transition 分析）\n\n**Should-Fix:**\n- W3: 方法层面无算法贡献（RF + 已知特征），classifier convergence (0.4pp) 证明了 ceiling\n- W4: Full-replacement only，缺乏 accumulation 实验（哪怕 pilot）\n- W5: \"confirming that...\" -ing 短语模式全文出现 9+ 次，AI 写作痕迹明显\n- W6: EDD 创新程度有限（本质是 pairwise AUC + threshold + contiguous prefix）\n- W7: 14B 实验 5 个 confounds，Abstract 中的描述可能误导读者\n\n**Minor:**\n- W8: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007）\n- W9: Curation PoC 未做 multiple comparison correction\n\n**Questions:**\n- Q1: 与 Mohamed et al. (2025) \"Broken Telephone\" 的精确区分\n- Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 定义的 strategy-invariance\n- Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count 效应\n- Q4: EDD=4 跨三个 family 一致性有无理论基础\n\n---\n\n请对 R2 的每个 Weakness (W1-W9)、每个 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别关注：你是否认同 R2 将 overall 降至 3.0 (Findings) 的判断？"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-19T06:42:39.891224+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22869
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-19T06:42:40.343482+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall Assessment: 3.5 (Borderline Conference), Confidence 4/5**\n\n**Strengths:**\n- S1: 任务形式化填补真实空白\n- S2: 基准设计系统且全面（3×3 grid, 180K 样本）\n- S3: 控制实验设计良好（LOGO、seed-group negative control、bug修正后如实报告）\n- S4: 分类器收敛验证了特征为核心（0.4pp）\n- S5: Limitations 章节异常诚实\n- S6: 跨模型递归链实验（正向+反向链 84.75%/85.75%）\n\n**Must-Fix:**\n- W1: Reference model circularity claim 与 Appendix H 消融数据矛盾——§3.4 称 \"no systematic advantage\"，但 Table 8 显示 self-reference 在 Pythia 数据上比 cross-reference 高 4.1-11.3pp。这使得 9 个 cell 的横向比较不公平。\n- W2: 跨尺度实验的 5 个混淆因素使 14B 结论不可靠——仅 2 个 7-8B 模型给出方向相反的 AUC 轨迹；14B 的 EDD=0 可能是 self-reference + quantization 的产物。Abstract \"depth signal persists\" 对 14B（EDD=0, d0v1 AUC=0.643）言过其实。\n- W3: d0 recall >97% 系统性膨胀 headline metrics——Cross-model transfer 66.4% headline → 55.4% d1-d3；Cross-strategy 59.1% → 45.9% d1-d3。Pythia holdout d2 recall 仅 26.8%。\n\n**Should-Fix:**\n- W4: Curation PoC 主比较不显著（p>0.4），RF vs random 多重比较 Bonferroni 校正后 2/3 通过但 rf_moderate vs random_moderate 的 p=0.020 不通过。\n- W5: VIF>10 for 14-16/19 features 下 feature importance 解释过度——Table 3 的逐特征精确 importance 值在高共线性下不稳定，但 group-level claim（Kendall's W=0.90）可靠。\n- W6: EDD contiguous prefix 要求在非单调场景下过于保守，缺乏替代方案。\n- W7: Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高（+0.14 到 +3.17pp），Table 2 中许多跨 cell 差异可能在 seed noise 范围内。\n- W8: Full-replacement scope 在 Abstract/Introduction 中不够前置，\"upper bound\" 假设缺乏实验验证。\n\n**Minor:**\n- W9: 单一 LoRA 超参配置\n- W10: Prompted generation 仅验证 1/9 cell\n\n**Questions:**\n- Q1: Table 8 self-reference 4-11pp 优势如何与 §3.4 \"no systematic advantage\" 调和？\n- Q2: Curation PoC Bonferroni 校正后具体哪两个比较通过了？\n- Q3: Full-replacement \"upper bound\" 假设有何实验/理论依据？\n- Q4: seed=43 系统性偏高的原因？d3 outlier 比例 0.56% vs 12.8% 但 seed=43 准确率更高的矛盾？\n- Q5: Cross-strategy transfer d1-d3: 45.9% 是否足以支持 \"data auditing\" 实用 claim？\n\n**官方维度打分:** Soundness 3.5/5, Excitement 3.5/5, Reproducibility 3/5\n\n---\n\n请对 R1 的每个 Weakness (W1-W10)、每个 Question (Q1-Q5) 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别关注：你是否认同 R1 给出 3.5 (Borderline Conference) 的判断？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall Assessment: 3.5 (Borderline Conference), Confidence 4/5**\n\n**Strengths:**\n- S1: 任务形式化填补真实空白\n- S2: 基准设计系统且全面（3×3 grid, 180K 样本）\n- S3: 控制实验设计良好（LOGO、seed-group negative control、bug修正后如实报告）\n- S4: 分类器收敛验证了特征为核心（0.4pp）\n- S5: Limitations 章节异常诚实\n- S6: 跨模型递归链实验（正向+反向链 84.75%/85.75%）\n\n**Must-Fix:**\n- W1: Reference model circularity claim 与 Appendix H 消融数据矛盾——§3.4 称 \"no systematic advantage\"，但 Table 8 显示 self-reference 在 Pythia 数据上比 cross-reference 高 4.1-11.3pp。这使得 9 个 cell 的横向比较不公平。\n- W2: 跨尺度实验的 5 个混淆因素使 14B 结论不可靠——仅 2 个 7-8B 模型给出方向相反的 AUC 轨迹；14B 的 EDD=0 可能是 self-reference + quantization 的产物。Abstract \"depth signal persists\" 对 14B（EDD=0, d0v1 AUC=0.643）言过其实。\n- W3: d0 recall >97% 系统性膨胀 headline metrics——Cross-model transfer 66.4% headline → 55.4% d1-d3；Cross-strategy 59.1% → 45.9% d1-d3。Pythia holdout d2 recall 仅 26.8%。\n\n**Should-Fix:**\n- W4: Curation PoC 主比较不显著（p>0.4），RF vs random 多重比较 Bonferroni 校正后 2/3 通过但 rf_moderate vs random_moderate 的 p=0.020 不通过。\n- W5: VIF>10 for 14-16/19 features 下 feature importance 解释过度——Table 3 的逐特征精确 importance 值在高共线性下不稳定，但 group-level claim（Kendall's W=0.90）可靠。\n- W6: EDD contiguous prefix 要求在非单调场景下过于保守，缺乏替代方案。\n- W7: Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高（+0.14 到 +3.17pp），Table 2 中许多跨 cell 差异可能在 seed noise 范围内。\n- W8: Full-replacement scope 在 Abstract/Introduction 中不够前置，\"upper bound\" 假设缺乏实验验证。\n\n**Minor:**\n- W9: 单一 LoRA 超参配置\n- W10: Prompted generation 仅验证 1/9 cell\n\n**Questions:**\n- Q1: Table 8 self-reference 4-11pp 优势如何与 §3.4 \"no systematic advantage\" 调和？\n- Q2: Curation PoC Bonferroni 校正后具体哪两个比较通过了？\n- Q3: Full-replacement \"upper bound\" 假设有何实验/理论依据？\n- Q4: seed=43 系统性偏高的原因？d3 outlier 比例 0.56% vs 12.8% 但 seed=43 准确率更高的矛盾？\n- Q5: Cross-strategy transfer d1-d3: 45.9% 是否足以支持 \"data auditing\" 实用 claim？\n\n**官方维度打分:** Soundness 3.5/5, Excitement 3.5/5, Reproducibility 3/5\n\n---\n\n请对 R1 的每个 Weakness (W1-W10)、每个 Question (Q1-Q5) 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别关注：你是否认同 R1 给出 3.5 (Borderline Conference) 的判断？"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-19T06:42:41.901324+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1557
}
```

</details>

---


### Assistant

_source line 1002 · 2026-05-19T06:42:44.903369+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1003 · 2026-05-19T06:42:47.646385+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 (Findings)** 评分。主要问题集中在三方面：(1) Abstract 数字堆砌 + Discussion 过薄（两个 Must-Fix），(2) 方法创新不足 + full-replacement only 的生态有效性限制（Should-Fix），(3) AI 写作痕迹（"confirming that..." 模式 9+ 次）。核心优势是任务新颖性、实验系统性和 reporting 诚实度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1004 · 2026-05-19T06:42:52.624026+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1005 · 2026-05-19T06:45:24.710585+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 完成

### 回应摘要

**AGREE (完全同意): W1, W4, W5, W6, W7, W9, W10, Q1, Q2, Q3, Q5**
**PARTIALLY AGREE: W2, W8**
**PARTIALLY REBUT: W3, Q4**

### 核心分歧

1. **W3 (d0 inflation) 应降级为 Should-Fix**: 论文已在每个 table/headline 旁报告 d1-d3 balanced accuracy，Limitations 专门讨论了此问题。R1 将已被论文处理好的 transparency issue 标为 Must-Fix 过重。

2. **W2 (14B) 部分同意**: 14B 不可解读（同意），但 7-8B 的 d0v1 AUC=0.949/0.969 不是 noise，两个模型 AUC 轨迹方向相反本身是有价值的发现。

3. **Q4 (seed=43 outlier 矛盾)**: clipping 机制可以解释 d3 高 outlier 比例 + 高准确率的共存，但论文缺乏直接证据。

### 对 R1 分数的评价

R1: 3.5 (Borderline Conference), R2: 3.0 (Findings)
差异主要在 Excitement。我认为标准 RF + 已知特征的方法 + ~200 words Discussion 不足以支撑 Conference level 的 intellectual contribution。区间 3.0-3.5 合理，充实 Discussion + accumulation pilot 可上调至 3.5。

### 两位 Reviewer 的共识区域
- Full-replacement scope 是核心限制，缺乏 accumulation 实验
- 14B 实验 confounds 过多
- Reference model circularity 措辞需修正
- EDD contiguous prefix 在非单调下过于保守
- Cross-seed replication 不足
- Curation PoC 统计分析需要 correction

完整逐条回应已在 session 中输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1006 · 2026-05-19T06:45:31.490158+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1007 · 2026-05-19T06:45:34.146111+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。与 R1 在大多数问题上达成共识（11/15 完全同意），核心分歧在 d0 inflation 是否构成 Must-Fix（我认为论文已处理好）和 Overall Assessment（我给 3.0 vs R1 的 3.5，差异来自方法贡献和 Discussion 深度的权重不同）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1008 · 2026-05-19T06:45:42.145442+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 104

## Round 104

8 recorded events


### User

_source line 1009 · 2026-05-19T06:45:54.432333+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Weaknesses 逐条回应

**[AGREE] R2-W1: Abstract 数字堆砌**
同意。我逐一计数，abstract 9 句话中包含 20+ 个数值（180K、3×3、d0-d3、19、69-86%、59-82%、25%/33%、0.4pp、66.4%、55.4%、74.1%、69.5%、59.1%、45.9%、EDD_{0.70}=4、7-14B、54-70%、30-35%、43pp）。这确实读起来像 results summary 而非有吸引力的叙事。我的审稿（R1-W3）也指出 d0 inflation 的叙事问题，但未单独将 abstract 写作风格列为独立问题——R2 的诊断更精确。建议：减少到 8-10 个关键数字，将叙事主线放在 "深度信号存在于困惑度尾部统计中" 这一洞察上，而非罗列所有泛化实验。不过我认为这是 Should-Fix 而非 Must-Fix，因为 abstract 的信息完整性没有问题，只是叙事吸引力不足。

**[AGREE] R2-W2: Discussion 过薄（~250 words）**
同意 concern，但对严重程度的判断有分歧。Discussion+Conclusion（§6）约 250 words，3 个 paragraph，确实无法承载 9 个 cell + 8 个泛化轴的 insight 深度。Appendix N（Extended Discussion）的 provenance toolkit 讨论和 cross-strategy conditional decomposition 分析是有价值的材料，提升到正文会显著改善论文。然而，我认为这是 **Should-Fix** 而非 Must-Fix：Discussion 的薄弱影响的是论文的 impact/excitement 感知，而非 soundness 或核心 claims 的可靠性。正文 8 页的空间约束下，Discussion 被压缩是可以理解的。

**[REBUT] R2-W3: 方法层面无算法贡献**
不同意将此作为显著扣分项。理由：
1. 论文在 §1 明确声明 "our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty"——这是自觉的 empirical contribution 定位。
2. ARR reviewer guidelines 列出了 17 个 common review issues，其中 H2 明确警告不要 "demanding state-of-the-art results or novel algorithms when the paper's contribution is elsewhere"。
3. Classifier convergence（RF/XGBoost/LightGBM 在 0.4pp 内收敛，§5.1）本身是一个有价值的 empirical finding：它证明了信号瓶颈在特征设计而非分类器——这一结论指导了未来研究方向（改进特征而非改进分类器）。
4. 类比：许多被广泛引用的 NLP benchmark 论文（如 GLUE、SuperGLUE、MMLU）的方法贡献也是 "standard model + standard protocol"，其价值在于 task formalization 和 systematic evaluation。
5. R2 自己也在 S1 中认可了 "novel and timely task formalization"——如果任务形式化是核心贡献，那么用标准方法证明信号存在性正是合适的方法论选择。

**[AGREE] R2-W4: Full-replacement only，缺乏 accumulation 实验**
完全同意。我的审稿（R1-W8）也将此列为 Should-Fix。论文在 Discussion 中声称 full-replacement 结果是 accumulation 的 "ceiling estimate"（§6, para 2），但这一单调性假设缺乏理论或实验支持。即使是一个 toy-scale 实验（如 50% human + 50% synthetic 的 2-depth 混合链）也会大幅增强论文的生态效度。

**[AGREE] R2-W5: -ing 短语 AI 写作痕迹**
事实确认：我 grep 了全文，", confirming/demonstrating/suggesting/indicating/revealing/establishing " 模式在正文+附录中出现 **20 次**（仅 "confirming that" 就有 8 次），R2 的 "9+ 次" 是保守估计。这确实是显著的 AI 写作标志。但我将此列为 **Minor** 而非 Should-Fix：ARR guidelines 强调 "assess substance over style"，这些模式不影响论文的技术内容或可读性。修复也很简单（将 -ing 分词短语改写为独立句子）。

**[REBUT] R2-W6: EDD 创新程度有限**
部分不同意。R2 将 EDD 描述为 "pairwise AUC + threshold + contiguous prefix"，这在技术组件层面是准确的，但低估了其概念贡献：
1. EDD 的价值不在于组件的技术新颖性，而在于**将 model collapse 理论的定性预测转化为可操作的定量指标**。这类 operationalization 在 NLP 中有悠久传统（BLEU = n-gram precision + brevity penalty；ROUGE = recall-based overlap；BERTScore = contextual embedding similarity——组件都不新，但组合后的 operationalization 有独立价值）。
2. contiguous prefix 要求使 EDD 具有可解释的语义："前 d 个深度都可以可靠区分"，比简单的 "最大可区分对" 更有实际部署意义。
3. 不过，我在 R1-W6 中指出了 EDD 在非单调场景下的过度保守性（如 Qwen2.5-7B 的 U 型 AUC），论文没有提供替代指标。这是 EDD 定义的一个真实局限，但不等于 "创新不足"。

**[AGREE] R2-W7: 14B 实验 5 个 confounds 在 Abstract 中的描述可能误导**
强烈同意。我的审稿（R1-W2）将此列为 Must-Fix。Abstract 中 "depth signal persists at larger scales" 对 14B（EDD=0, d0v1 AUC=0.643）不成立。5 个混淆因素（QLoRA量化 / 500 samples / 单策略 / 词表不匹配 / self-reference）使 cross-scale 结论不可靠。R2 和我在这一点上完全一致。

**[AGREE] R2-W8: 3 条孤儿引用**
已验证：`llama3`、`qwen2.5`、`sugiyama2007_importance_weighting` 存在于 references.bib 中，但在实际提交的 tex 文件中**均未被 \cite**（仅出现在 drafts/ 目录的未使用草稿中）。这是提交前清理的遗漏，属于 Minor 但应修复。

**[AGREE] R2-W9: Curation PoC 未做 multiple comparison correction**
同意，且我的审稿（R1-W4）对此有更详细的分析：rf_moderate vs random_moderate 的 p=0.020 在 Bonferroni 校正（α=0.017）下不通过，但 Appendix N 声称 "2 of 3 surviving"。R2 的 concern 与我一致。

---

### Questions 逐条回应

**[REBUT] R2-Q1: 与 Mohamed et al. (2025) "Broken Telephone" 的区分**
Related Work §2（Adjacent Tasks 段）已明确区分："Mohamed et al. (2025) characterize *how* text degrades under iterative generation without classifying which iteration a passage comes from. Our task performs the inverse: ordinal depth estimation from text alone." 区分是清晰的：Mohamed et al. 分析退化现象（descriptive），本文估计迭代次数（predictive/classificatory）。不过，可以建议作者补充一句说明为什么 "Broken Telephone" 的 degradation characterization 不能直接用于深度分类（如：是否因为其特征不具有序数单调性？）。

**[AGREE] R2-Q2: Cross-strategy d1/d2 inversion 是否质疑 depth 的 strategy-invariance**
这是一个有深度的概念问题。我的回答是：它质疑的不是 **depth 定义的 strategy-invariance**（depth 是过程定义，策略无关），而是**基于当前特征集的 depth estimation 的 strategy-invariance**。温度采样加速收敛（§3.6），使得 temp d1 的统计特征类似于 nucleus d2——这是特征空间的对齐问题，不是深度定义的问题。但 R2 提出这个问题的价值在于：论文应更明确地区分 "depth as a process property"（strategy-invariant）和 "depth estimation via perplexity features"（strategy-dependent）。当前的 Discussion 没有充分展开这一区分，这也印证了 R2-W2（Discussion 过薄）的 concern。

**[REBUT] R2-Q3: GPT-2 XL 最高准确率是 architecture 还是 parameter count**
参数量不能解释准确率排序。OLMo-1B（1B 参数）在 temperature 策略下达到 82.3%，超过 Pythia-1.4B（1.4B）的 76.8%——如果参数量是主导因素，这一反转不应出现。更可能的解释是训练数据差异：GPT-2 XL（WebText）的训练数据与 Wikipedia seed 的分布差异可能产生了更强的深度信号（cross-distribution feature extraction）。这一点可以通过 Table 8（Appendix H）的 reference model ablation 间接验证：当 Pythia 数据使用 GPT-2 XL 作为参考模型时准确率**最低**（67.3%），而 GPT-2 XL 数据使用 Pythia 作为参考模型时准确率**最高**（85.9%）——这暗示 generator 与 reference 的分布差异本身可能放大了深度信号，值得进一步调查。

**[AGREE] R2-Q4: EDD=4 跨三个 family 的一致性有无理论基础**
§3.6 提供了部分理论基础（tail mass 以 α^k 收缩，α 为 contraction factor），如果三个模型的 α 在 1-1.5B 尺度下相近，EDD 收敛是可预期的。但仅 3 个模型族构不成统计意义上的 "一致性"——这可能是 scale 约束下的巧合。论文将 "EDD_{0.70}=4 for all three families" 写入 abstract 和 contribution 列表，但没有提供理论预测或 bootstrap 检验来支持这一一致性的显著性。R2 的质疑合理。

---

### 对 R2 Overall Assessment (3.0, Findings) 的评价

**我不完全认同将 overall 降至 3.0。** 我的评分为 3.5（Borderline Conference），与 R2 的核心分歧在 W3（方法无算法贡献）和 W6（EDD 创新有限）：

1. **W3 的权重分歧**：R2 将 "RF + 已知特征" 视为 Should-Fix 级别的弱点，但 ARR guidelines 明确警告不要惩罚 empirical contribution 论文缺乏算法创新。论文的价值在于：(a) 定义了一个被忽视但重要的新任务；(b) 通过系统实验证明了信号的存在性和特征结构；(c) 证明了分类器不是瓶颈。这种 "task + benchmark + systematic empirical characterization" 的贡献模式在 *ACL venues 中有清晰的先例。

2. **W6 与 W3 的耦合**：如果因为 RF 不新（W3）又因为 EDD 不新（W6），论文的方法贡献就被双重折扣了。但 EDD 的贡献是 operationalization 而非 algorithmic novelty，与 W3 属于不同维度。

3. **R2 与 R1 的共识区域**：我们在以下问题上完全一致——full-replacement scope limitation（R2-W4 / R1-W8）、cross-scale confounds（R2-W7 / R1-W2）、curation PoC 不显著（R2-W9 / R1-W4）、Abstract 需要改善（R2-W1 / R1-W3 部分重叠）。这些问题是 **可修复的**，不构成 fundamental flaw。

4. **R2 比 R1 更敏感的区域**：Discussion 厚度（W2）和 AI 写作痕迹（W5）。这些是合理的关注，但它们的修复成本低（增写 Discussion + 改写 -ing 短语），不应将论文从 Conference 边缘推到 Findings。

5. **R1 比 R2 更敏感的区域**：Reference model circularity（R1-W1）、feature importance 在高共线性下的过度解释（R1-W5）、cross-seed 覆盖不足（R1-W7）。这些是 R2 未覆盖的方法严谨性问题，但同样可修复。

**综合判断**：论文的 Must-Fix 问题（reference model claim 矛盾、cross-scale claim 校准、d0 inflation 前置）是 claim-strength 校准问题，而非 fundamental methodological flaw。在 claim 校准后，任务形式化 + 系统实验 + EDD 指标 + 特征一致性发现的组合贡献足以支撑 Borderline Conference（3.5），前提是作者在 rebuttal 中充分回应 W1-W3 的修复方案。如果 rebuttal 不能令人信服地回应 reference model circularity 和 cross-scale confounds，我会降至 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-19T06:47:12.364974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-19T06:47:12.365565+00:00_

1	issues:
2	  # ============================================================
3	  # Round 12 Issues — D043 Action Matrix locked in
4	  # ============================================================
5	
6	  - id: R12-W1
7	    summary: "生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异，需更清晰的 scope 声明"
8	    category: framing
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 12
12	    last_seen_round: 12
13	    mentions:
14	      - round: 12
15	        reviewers: [1, 2]
16	        note: "R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。"
17	    action_items:
18	      - round: 12
19	        action: "Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 段落；Limitations 提升为第一条"
20	        assigned_to: paper_agent
21	        status: in_progress
22	    resolution: ""
23	    resolution_round: null
24	
25	  - id: R12-W2
26	    summary: "Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion，策略未知场景下部署价值极低"
27	    category: experiment
28	    severity: critical
29	    status: in_progress
30	    first_raised_round: 12
31	    last_seen_round: 12
32	    mentions:
33	      - round: 12
34	        reviewers: [1, 2]
35	        note: "R1 列为 Must-Fix，R2 交叉回应中升级认同。"
36	    action_items:
37	      - round: 12
38	        action: "Abstract 并列 d1-d3 45.9%；cross-strategy bottleneck 重定位为 key empirical finding；Claim 3 措辞修改"
39	        assigned_to: paper_agent
40	        status: in_progress
41	    resolution: ""
42	    resolution_round: null
43	
44	  - id: R12-W3
45	    summary: "d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没"
46	    category: writing
47	    severity: warning
48	    status: in_progress
49	    first_raised_round: 12
50	    last_seen_round: 12
51	    mentions:
52	      - round: 12
53	        reviewers: [1, 2]
54	        note: "R1-W3 和 R2-W6 完全一致。"
55	    action_items:
56	      - round: 12
57	        action: "所有 headline 数字旁系统性并列 d1-d3 balanced accuracy"
58	        assign
…[truncated 8148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-19T06:49:14.521315+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 12 Issues — status updated based on Round 13 fresh review\n  # ============================================================\n\n  - id: R12-W1\n    summary: \"生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-R1-W8 和 R13-R2-W4 再次提出。论文已在 Introduction §2 和 Discussion 中添加了 scope 声明和 accumulation 段落，Limitations 已提为第一条。但仍缺乏任何 accumulation 实验验证 'upper bound' 假设。部分改善但核心问题未解决。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 段落；Limitations 提升为第一条\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"补充至少一个 toy-scale accumulation 实验（如 50% human + 50% synthetic 混合链）验证 upper bound 假设\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W2\n    summary: \"Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix，R2 交叉回应中升级认同。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已将 cross-strategy bottleneck 重新定位为 key empirical finding（§5.3），Abstract 并列了 d1-d3 45.9%，Claim 3 措辞已修改。R13-R1-Q5 质疑 45.9% 是否足以支持 data auditing claim。两阶段 pipeline 仅恢复 11.5pp。改善明显但部署价值仍受限。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 并列 d1-d3 45.9%；cross-strategy bottleneck 重定位为 key empirical finding\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W3\n    summary: \"d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 和 R2-W6 完全一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已在每个 table/headline 旁系统性并列 d1-d3 balanced accuracy。R13-R1 仍将此列为 Must-Fix（应以 d1-d3 为主指标），R13-R2 认为已充分处理（降为 Should-Fix）。Director 裁定 Should-Fix：transparency 已改善，但 Abstract 仍以四类准确率为主导叙事。\"\n    action_items:\n      - round: 12\n        action: \"所有 headline 数字旁系统性并列 d1-d3 balanced accuracy\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Abstract 和 Contribution 列表中以 d1-d3 balanced accuracy 为主指标，四类准确率作为补充\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"Cross-scale 实验仅少数模型、5+ 个混杂因素，不足以支撑 scale-dependent attenuation 结论\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 双方均列为 Must-Fix 并完全一致。论文已将 §5.4 标题改为 'Preliminary Cross-Scale Observations'，使用 'existence proof' 措辞，但 Abstract 中 'depth signal persists at larger scales' 对 14B（EDD=0, d0v1 AUC=0.643）仍言过其实。14B 多策略实验（temp09+topk50）正在运行但结果未纳入。升级为 critical。\"\n    action_items:\n      - round: 12\n        action: \"降调 cross-scale 为 existence proof；14B 多策略实验补充\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Abstract 中将 14B 明确标记为 boundary condition 而非 persists；限制 existence proof claim 为 7-8B\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W5\n    summary: \"Curation PoC 主比较不显著（RF vs unfiltered p>0.4），RF vs random 多重比较校正不完整\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W5 和 R2-W7 完全一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已标记为 'inconclusive'，Appendix N 提及 Bonferroni 但声称 '2 of 3 surviving' 不准确（rf_moderate vs random_moderate p=0.020 > α=0.017 不通过）。部分改善但校正仍有误。\"\n    action_items:\n      - round: 12\n        action: \"标记为 inconclusive；应用 Bonferroni 校正\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"修正 Appendix N 的 Bonferroni 表述：明确仅 1/3 通过（rf_strict vs random_strict p=0.002 < 0.017），另两个不通过\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W6\n    summary: \"Abstract 信息过载：20+ 数字堆砌\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 和 R2-W4 一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"未修复。R13-R2 列为 Must-Fix，R13-R1 AGREE 但降为 Should-Fix。当前 abstract 9 句话仍含 20+ 数值。Director 裁定 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"完全重写 Abstract：150-180 词，problem-method-result 三层叙事，2-3 关键数字\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"同上，未执行。减少到 8-10 个关键数字，叙事主线放在困惑度尾部统计洞察上\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W7\n    summary: \"Discussion 过薄，核心讨论被放逐到 Appendix\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 和 R2-W5 一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"部分改善：从 R12 的 ~80 词扩展到 ~250 词（3 段），但 R13-R2 仍列为 Must-Fix（不足以承载 empirical study 的 insight 深度），R13-R1 AGREE 但降为 Should-Fix。Appendix N 的 provenance toolkit 讨论和 cross-strategy decomposition 分析仍在附录。Director 裁定 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"扩展至 3-4 段：accumulation setting、scale attenuation、部署 roadmap\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"将 Appendix N 的 provenance toolkit 讨论提升到正文；新增 cross-strategy barrier 和 depth-as-process vs depth-estimation 的区分讨论\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W8\n    summary: \"多重共线性下 individual feature importance 不可靠\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W6 提出，R2 partially agree。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"部分改善：添加了脚注 caveat（VIF>10 for 14-16/19 features），group-level claim 有 Kendall's W=0.90 支持。但 Table 3 仍展示逐特征精确 importance 值（.17, .15 等），R13-R1-W5 指出在 effective dimensionality 4-5 下个体排名不稳定。\"\n    action_items:\n      - round: 12\n        action: \"Atlas §4 改为 feature group 级别叙事\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"将脚注 caveat 提升为正文段落；Table 3 caption 注明 individual rankings unstable under VIF>10；考虑报告 bootstrap stability\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W9\n    summary: \"算法贡献不足：标准 RF + 标准特征\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Must-Fix, R1 REBUT. Director 裁定 Should-Fix.\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已在 Introduction 明确声明 empirical contribution 定位。R13-R2-W3 仍列为 Should-Fix，R13-R1 REBUT（引用 ARR guidelines H2 保护 empirical contribution）。分歧未解决但双方论据均有效。Director 维持 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"Introduction 强化 empirical study + problem formalization 定位\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M1\n    summary: \"EDD threshold T=0.70 选择缺乏独立依据\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Minor issue.\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出此问题。论文已添加 T∈{0.65,0.70,0.75,0.80} 敏感性分析（§4.4），并在 §3.5 报告 T=0.70 对应 adequate discrimination。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 12\n        action: \"加 1 句 AUC 文献含义\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M2\n    summary: \"RF ordinal claim 过强\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Minor issue.\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。论文已弱化为 'ordinally consistent predictions'（§3.5 末段）并添加 CORAL 匹配数据。可能已修复，待确认。\"\n    action_items:\n      - round: 12\n        action: \"弱化为 ordinally consistent predictions\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M3\n    summary: \"Reference model (Pythia-1.4B) 与 generator 重叠——circularity risk\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Defer to rebuttal. Appendix 已有 3 种 reference 消融数据。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"恶化。§3.4 新增了 'confers no systematic advantage' 声明，与 Appendix H（Table 8）self-reference 带来 4.1-11.3pp 优势的数据直接矛盾。R13-R1-W1 列为 Must-Fix，R13-R2 完全同意。从 info 升级为 critical。\"\n    action_items:\n      - round: 12\n        action: \"DEFER to rebuttal\"\n        assigned_to: research_director\n        status: open\n      - round: 13\n        action: \"修正 §3.4 claim：承认 self-reference 带来可测量优势（4-11pp）；Table 2 Pythia 行注明 self-reference；讨论统一 cross-reference 时准确率预期变化\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M4\n    summary: \"Prompted generation 验证仅 1/9 cells\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Minor.\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已在 §5.3 和 Limitations 中添加 single-cell qualifier。R13-R1-W10 和 R13-R2 均确认但维持 Minor。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 加 single-cell qualifier\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M5\n    summary: \"Feature trajectory 图应从 Appendix 移回正文\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"REJECTED by Director — 页数限制不允许\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未提出此问题。\"\n    action_items:\n      - round: 12\n        action: \"REJECT — 页数约束，保持 appendix + 正文前向引用\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Won't fix — page budget allocated to Discussion expansion instead\"\n    resolution_round: 12\n\n  - id: R12-M6\n    summary: \"孤立 bib entries + 引用 mismatch\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"c2pa2024 孤立 + 5 条 mismatch。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"c2pa2024 已删除，但 R13-R2-W8 发现 3 条新孤儿引用（llama3, qwen2.5, sugiyama2007_importance_weighting），R13-R1 确认均在 bib 中但未被 cite。部分修复但问题复发。\"\n    action_items:\n      - round: 12\n        action: \"删除 c2pa2024；修正 mismatch\"\n        assigned_to: main_agent\n        status: in_progress\n      - round: 13\n        action: \"删除或 cite llama3, qwen2.5, sugiyama2007_importance_weighting\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M7\n    summary: \"Feature extraction 'requires no GPU' 声明可能不准确\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"Agent 核实中。\"\n      - round: 13\n        reviewers: []\n        note: \"论文现在报告 'approximately 2 minutes on a single GPU' 和 'approximately 50 minutes on server-grade hardware' for CPU（Appendix P）。可能已修复，待确认。\"\n    action_items:\n      - round: 12\n        action: \"Agent benchmark CPU inference 并修正声明\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M8\n    summary: \"遗漏引用 Muennighoff et al. (2024) + Ilyas et al. (2022)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Agent 验证 bib 条目中。\"\n      - round: 13\n        reviewers: []\n        note: \"两条引用现已出现在 references.bib 中（muennighoff2023scaling, ilyas2022datamodels），且在正文 Related Work §2 中被 cite。可能已修复，待确认。\"\n    action_items:\n      - round: 12\n        action: \"Agent 提供验证后 bib 条目\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 13 New Issues\n  # ============================================================\n\n  - id: R13-W1\n    summary: \"Reference model circularity: §3.4 'no systematic advantage' claim 与 Appendix H self-reference 4-11pp 优势数据直接矛盾\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W1 Must-Fix，R2 完全 AGREE。§3.4 的 claim 使用跨 generator 的混淆比较论证 self-reference 无优势，但 Table 8 的公平消融显示 self-reference 在 Pythia 数据上比 cross-reference 高 4.1-11.3pp。这使 9 cell 横向比较不公平。从 R12-M3（info）升级而来。\"\n    action_items:\n      - round: 13\n        action: \"修正 §3.4 claim；Table 2 Pythia 行注明 self-reference；讨论统一 cross-reference 时准确率预期\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W2\n    summary: \"EDD contiguous prefix 在非单调 AUC 场景下过于保守，缺乏替代指标\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W6 Should-Fix，R2 AGREE。Qwen2.5-7B U 型 AUC、cross-strategy d1v2 AUC 低至 0.129 均触发 EDD 的保守性问题。Limitations 承认但无替代方案。\"\n    action_items:\n      - round: 13\n        action: \"在 §3.5 提供补充指标（如 Maximum Discriminable Depth）；明确 EDD 适用条件\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W3\n    summary: \"Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高 +0.14~+3.17pp\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W7 Should-Fix，R2 AGREE。seed=43 在所有 3 cell 中均优于 seed=42 且 2/3 统计显著。Table 2 中多个跨 cell 差异（如 Pythia 78.7% vs OLMo 78.9%）可能在 seed noise 范围内。\"\n    action_items:\n      - round: 13\n        action: \"至少对 3 个 temperature cells 补充 seed=43 replication；Table 2 caption 注明 single-seed uncertainty ~1-3pp\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W4\n    summary: \"AI 写作痕迹：-ing 短语（confirming/demonstrating/suggesting...）全文 20+ 次\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W5 Should-Fix，R1 AGREE 但降为 Minor。R1 grep 确认正文+附录共 20 次（'confirming that' 8 次）。不影响技术内容但是 AI 写作标志。Director 裁定 Minor。\"\n    action_items:\n      - round: 13\n        action: \"将 -ing 分词短语改写为独立句子；grep 'confirming|demonstrating|suggesting|indicating|revealing|establishing' 并逐一修正\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W5\n    summary: \"单一 LoRA 超参配置（r=16, α=32），缺乏 rank/lr 敏感性分析\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1]\n        note: \"R1-W9 Minor。不同 LoRA rank 可能改变递归链衰退速度。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 12 Issues — status updated based on Round 13 fresh review\n  # ============================================================\n\n  - id: R12-W1\n    summary: \"生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13-R1-W8 和 R13-R2-W4 再次提出。论文已在 Introduction §2 和 Discussion 中添加了 scope 声明和 accumulation 段落，Limitations 已提为第一条。但仍缺乏任何 accumulation 实验验证 'upper bound' 假设。部分改善但核心问题未解决。\"\n    action_items:\n      - round: 12\n        action: \"Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 段落；Limitations 提升为第一条\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"补充至少一个 toy-scale accumulation 实验（如 50% human + 50% synthetic 混合链）验证 upper bound 假设\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W2\n    summary: \"Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix，R2 交叉回应中升级认同。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已将 cross-strategy bottleneck 重新定位为 key empirical finding（§5.3），Abstract 并列了 d1-d3 45.9%，Claim 3 措辞已修改。R13-R1-Q5 质疑 45.9% 是否足以支持 data auditing claim。两阶段 pipeline 仅恢复 11.5pp。改善明显但部署价值仍受限。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 并列 d1-d3 45.9%；cross-strategy bottleneck 重定位为 key empirical finding\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W3\n    summary: \"d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W3 和 R2-W6 完全一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已在每个 table/headline 旁系统性并列 d1-d3 balanced accuracy。R13-R1 仍将此列为 Must-Fix（应以 d1-d3 为主指标），R13-R2 认为已充分处理（降为 Should-Fix）。Director 裁定 Should-Fix：transparency 已改善，但 Abstract 仍以四类准确率为主导叙事。\"\n    action_items:\n      - round: 12\n        action: \"所有 headline 数字旁系统性并列 d1-d3 balanced accuracy\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Abstract 和 Contribution 列表中以 d1-d3 balanced accuracy 为主指标，四类准确率作为补充\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"Cross-scale 实验仅少数模型、5+ 个混杂因素，不足以支撑 scale-dependent attenuation 结论\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13 双方均列为 Must-Fix 并完全一致。论文已将 §5.4 标题改为 'Preliminary Cross-Scale Observations'，使用 'existence proof' 措辞，但 Abstract 中 'depth signal persists at larger scales' 对 14B（EDD=0, d0v1 AUC=0.643）仍言过其实。14B 多策略实验（temp09+topk50）正在运行但结果未纳入。升级为 critical。\"\n    action_items:\n      - round: 12\n        action: \"降调 cross-scale 为 existence proof；14B 多策略实验补充\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"Abstract 中将 14B 明确标记为 boundary condition 而非 persists；限制 existence proof claim 为 7-8B\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W5\n    summary: \"Curation PoC 主比较不显著（RF vs unfiltered p>0.4），RF vs random 多重比较校正不完整\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W5 和 R2-W7 完全一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已标记为 'inconclusive'，Appendix N 提及 Bonferroni 但声称 '2 of 3 surviving' 不准确（rf_moderate vs random_moderate p=0.020 > α=0.017 不通过）。部分改善但校正仍有误。\"\n    action_items:\n      - round: 12\n        action: \"标记为 inconclusive；应用 Bonferroni 校正\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"修正 Appendix N 的 Bonferroni 表述：明确仅 1/3 通过（rf_strict vs random_strict p=0.002 < 0.017），另两个不通过\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W6\n    summary: \"Abstract 信息过载：20+ 数字堆砌\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 和 R2-W4 一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"未修复。R13-R2 列为 Must-Fix，R13-R1 AGREE 但降为 Should-Fix。当前 abstract 9 句话仍含 20+ 数值。Director 裁定 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"完全重写 Abstract：150-180 词，problem-method-result 三层叙事，2-3 关键数字\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"同上，未执行。减少到 8-10 个关键数字，叙事主线放在困惑度尾部统计洞察上\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W7\n    summary: \"Discussion 过薄，核心讨论被放逐到 Appendix\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 和 R2-W5 一致。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"部分改善：从 R12 的 ~80 词扩展到 ~250 词（3 段），但 R13-R2 仍列为 Must-Fix（不足以承载 empirical study 的 insight 深度），R13-R1 AGREE 但降为 Should-Fix。Appendix N 的 provenance toolkit 讨论和 cross-strategy decomposition 分析仍在附录。Director 裁定 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"扩展至 3-4 段：accumulation setting、scale attenuation、部署 roadmap\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"将 Appendix N 的 provenance toolkit 讨论提升到正文；新增 cross-strategy barrier 和 depth-as-process vs depth-estimation 的区分讨论\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W8\n    summary: \"多重共线性下 individual feature importance 不可靠\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W6 提出，R2 partially agree。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"部分改善：添加了脚注 caveat（VIF>10 for 14-16/19 features），group-level claim 有 Kendall's W=0.90 支持。但 Table 3 仍展示逐特征精确 importance 值（.17, .15 等），R13-R1-W5 指出在 effective dimensionality 4-5 下个体排名不稳定。\"\n    action_items:\n      - round: 12\n        action: \"Atlas §4 改为 feature group 级别叙事\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 13\n        action: \"将脚注 caveat 提升为正文段落；Table 3 caption 注明 individual rankings unstable under VIF>10；考虑报告 bootstrap stability\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W9\n    summary: \"算法贡献不足：标准 RF + 标准特征\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Must-Fix, R1 REBUT. Director 裁定 Should-Fix.\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已在 Introduction 明确声明 empirical contribution 定位。R13-R2-W3 仍列为 Should-Fix，R13-R1 REBUT（引用 ARR guidelines H2 保护 empirical contribution）。分歧未解决但双方论据均有效。Director 维持 Should-Fix。\"\n    action_items:\n      - round: 12\n        action: \"Introduction 强化 empirical study + problem formalization 定位\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M1\n    summary: \"EDD threshold T=0.70 选择缺乏独立依据\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Minor issue.\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出此问题。论文已添加 T∈{0.65,0.70,0.75,0.80} 敏感性分析（§4.4），并在 §3.5 报告 T=0.70 对应 adequate discrimination。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 12\n        action: \"加 1 句 AUC 文献含义\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M2\n    summary: \"RF ordinal claim 过强\"\n    category: method\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Minor issue.\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未单独提出。论文已弱化为 'ordinally consistent predictions'（§3.5 末段）并添加 CORAL 匹配数据。可能已修复，待确认。\"\n    action_items:\n      - round: 12\n        action: \"弱化为 ordinally consistent predictions\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M3\n    summary: \"Reference model (Pythia-1.4B) 与 generator 重叠——circularity risk\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Defer to rebuttal. Appendix 已有 3 种 reference 消融数据。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"恶化。§3.4 新增了 'confers no systematic advantage' 声明，与 Appendix H（Table 8）self-reference 带来 4.1-11.3pp 优势的数据直接矛盾。R13-R1-W1 列为 Must-Fix，R13-R2 完全同意。从 info 升级为 critical。\"\n    action_items:\n      - round: 12\n        action: \"DEFER to rebuttal\"\n        assigned_to: research_director\n        status: open\n      - round: 13\n        action: \"修正 §3.4 claim：承认 self-reference 带来可测量优势（4-11pp）；Table 2 Pythia 行注明 self-reference；讨论统一 cross-reference 时准确率预期变化\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M4\n    summary: \"Prompted generation 验证仅 1/9 cells\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Minor.\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"论文已在 §5.3 和 Limitations 中添加 single-cell qualifier。R13-R1-W10 和 R13-R2 均确认但维持 Minor。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 加 single-cell qualifier\"\n        assigned_to: paper_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M5\n    summary: \"Feature trajectory 图应从 Appendix 移回正文\"\n    category: writing\n    severity: info\n    status: wont_fix\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"REJECTED by Director — 页数限制不允许\"\n      - round: 13\n        reviewers: []\n        note: \"R13 未提出此问题。\"\n    action_items:\n      - round: 12\n        action: \"REJECT — 页数约束，保持 appendix + 正文前向引用\"\n        assigned_to: research_director\n        status: open\n    resolution: \"Won't fix — page budget allocated to Discussion expansion instead\"\n    resolution_round: 12\n\n  - id: R12-M6\n    summary: \"孤立 bib entries + 引用 mismatch\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"c2pa2024 孤立 + 5 条 mismatch。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"c2pa2024 已删除，但 R13-R2-W8 发现 3 条新孤儿引用（llama3, qwen2.5, sugiyama2007_importance_weighting），R13-R1 确认均在 bib 中但未被 cite。部分修复但问题复发。\"\n    action_items:\n      - round: 12\n        action: \"删除 c2pa2024；修正 mismatch\"\n        assigned_to: main_agent\n        status: in_progress\n      - round: 13\n        action: \"删除或 cite llama3, qwen2.5, sugiyama2007_importance_weighting\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M7\n    summary: \"Feature extraction 'requires no GPU' 声明可能不准确\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1]\n        note: \"Agent 核实中。\"\n      - round: 13\n        reviewers: []\n        note: \"论文现在报告 'approximately 2 minutes on a single GPU' 和 'approximately 50 minutes on server-grade hardware' for CPU（Appendix P）。可能已修复，待确认。\"\n    action_items:\n      - round: 12\n        action: \"Agent benchmark CPU inference 并修正声明\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-M8\n    summary: \"遗漏引用 Muennighoff et al. (2024) + Ilyas et al. (2022)\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Agent 验证 bib 条目中。\"\n      - round: 13\n        reviewers: []\n        note: \"两条引用现已出现在 references.bib 中（muennighoff2023scaling, ilyas2022datamodels），且在正文 Related Work §2 中被 cite。可能已修复，待确认。\"\n    action_items:\n      - round: 12\n        action: \"Agent 提供验证后 bib 条目\"\n        assigned_to: main_agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 13 New Issues\n  # ============================================================\n\n  - id: R13-W1\n    summary: \"Reference model circularity: §3.4 'no systematic advantage' claim 与 Appendix H self-reference 4-11pp 优势数据直接矛盾\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W1 Must-Fix，R2 完全 AGREE。§3.4 的 claim 使用跨 generator 的混淆比较论证 self-reference 无优势，但 Table 8 的公平消融显示 self-reference 在 Pythia 数据上比 cross-reference 高 4.1-11.3pp。这使 9 cell 横向比较不公平。从 R12-M3（info）升级而来。\"\n    action_items:\n      - round: 13\n        action: \"修正 §3.4 claim；Table 2 Pythia 行注明 self-reference；讨论统一 cross-reference 时准确率预期\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W2\n    summary: \"EDD contiguous prefix 在非单调 AUC 场景下过于保守，缺乏替代指标\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W6 Should-Fix，R2 AGREE。Qwen2.5-7B U 型 AUC、cross-strategy d1v2 AUC 低至 0.129 均触发 EDD 的保守性问题。Limitations 承认但无替代方案。\"\n    action_items:\n      - round: 13\n        action: \"在 §3.5 提供补充指标（如 Maximum Discriminable Depth）；明确 EDD 适用条件\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W3\n    summary: \"Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高 +0.14~+3.17pp\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W7 Should-Fix，R2 AGREE。seed=43 在所有 3 cell 中均优于 seed=42 且 2/3 统计显著。Table 2 中多个跨 cell 差异（如 Pythia 78.7% vs OLMo 78.9%）可能在 seed noise 范围内。\"\n    action_items:\n      - round: 13\n        action: \"至少对 3 个 temperature cells 补充 seed=43 replication；Table 2 caption 注明 single-seed uncertainty ~1-3pp\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W4\n    summary: \"AI 写作痕迹：-ing 短语（confirming/demonstrating/suggesting...）全文 20+ 次\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W5 Should-Fix，R1 AGREE 但降为 Minor。R1 grep 确认正文+附录共 20 次（'confirming that' 8 次）。不影响技术内容但是 AI 写作标志。Director 裁定 Minor。\"\n    action_items:\n      - round: 13\n        action: \"将 -ing 分词短语改写为独立句子；grep 'confirming|demonstrating|suggesting|indicating|revealing|establishing' 并逐一修正\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-W5\n    summary: \"单一 LoRA 超参配置（r=16, α=32），缺乏 rank/lr 敏感性分析\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1]\n        note: \"R1-W9 Minor。不同 LoRA rank 可能改变递归链衰退速度。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-19T06:49:14.623232+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 16929}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-19T06:52:00.310356+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**目标 Venue**: EMNLP 2026 (ARR May cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+写作完整性+Related Work）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类任务，构建了 180K 样本的基准测试集（3 个模型族 × 3 种解码策略 × 4 个深度等级），使用基于 19 个统计特征的 Random Forest 进行分类，并提出 Effective Discriminable Depth (EDD) 指标量化相邻深度的可区分极限。论文在多个泛化轴（跨模型、跨策略、跨域、跨尺度）上进行了系统实验，核心发现是困惑度尾部特征族（p90_ppl、var_surprisal）在所有 9 个 model-strategy cell 中主导深度判别，EDD_{0.70}=4 for all three model families at 1-1.5B scale。\n\n---\n\n## Strengths\n\n**S1: 任务形式化填补真实空白。** 在二元检测（human vs. machine）和模型坍塌理论（假定深度已知）之间，序数深度估计是一个未被研究的新维度。EDD 指标将 model collapse 理论的定性预测转化为可操作的定量指标。两位 Reviewer 一致认可这是论文最重要的贡献。\n\n**S2: 基准设计系统且全面。** 3×3 grid（模型族 × 解码策略）覆盖了合理的变异来源，180K 样本规模充足，8 个泛化轴的测试体系（跨模型、跨策略、跨域、跨尺度、prompted generation、跨模型链、深度扩展、温度鲁棒性）在 empirical study 中罕见地系统。\n\n**S3: 控制实验和报告诚信度高。** Domain bias analysis 中的 LOGO 评估（72.1% 匹配标准 CV 72.0%）和 seed-group negative control（10.2%, chance level）有效排除了 topic leakage。修正 bug 后如实报告修正前后数据体现研究诚信。Limitations 章节主动讨论了 full-replacement vs. accumulation、d0 inflation、cross-strategy boundary inversion、reference model dependency 等多个 limitation，透明度在提交稿中罕见。\n\n**S4: 分类器收敛验证了特征为核心。** RF、XGBoost、LightGBM 在 0.4pp 内收敛（§5.1），CORAL/DivEye 在 0.6pp 内匹配（p>0.05），有力论证信号来自特征设计而非分类器架构。这本身是一个有价值的 empirical finding。\n\n**S5: Related Work 覆盖全面。** 69 条引用，覆盖 model collapse theory、AI text detection、membership inference、ordinal classification、decoding strategy effects 等主要领域，2025-2026 最新工作均已纳入。\n\n**S6: 跨模型递归链实验有说服力。** 异构链（Pythia→OLMo→GPT-2 XL, 84.75%）和反向链（GPT-2 XL→OLMo→Pythia, 85.75%）有效排除了架构指纹假说，为 process-level depth signal 提供了初步证据。\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识）\n\n**W1 [Must-Fix, consensus]: Reference model circularity claim 与消融数据直接矛盾。**\n- §3.4 声称 Pythia-1.4B 同时作为 generator 和 reference model \"confers no systematic advantage\"，论据是 Pythia 数据（78.7%）低于 GPT-2 XL 数据（85.9%）。\n- 但这是跨 generator 的混淆比较。Appendix H（Table 8）的公平消融显示：在 Pythia 生成的数据上，self-reference（78.6%）> OLMo 参考（74.5%）> GPT-2 XL 参考（67.3%），self-reference 带来 4.1-11.3pp 优势。\n- Limitations 也承认 \"same-family references yield optimal performance\"。\n- 这使得 9 个 cell 的横向比较不公平：Pythia cell 可能因 self-reference 被高估，OLMo/GPT-2 XL cell 因 cross-reference 被低估。\n- **修复**: 修正 §3.4 claim，承认 self-reference 带来可测量优势；Table 2 Pythia 行注明 self-reference。\n\n**W2 [Must-Fix, consensus]: Cross-scale 实验的 5 个混淆因素使结论不可靠，Abstract 表述过度乐观。**\n- 7-14B 实验受 5 个混淆因素限制（QLoRA 4-bit 量化 / 500 vs 5000 samples / 仅 nucleus 策略 / 词表不匹配 / 14B self-reference）。\n- 仅 2 个 7-8B 模型给出方向相反的 AUC 轨迹（Llama-3.1 单调 vs Qwen2.5 U型），无法判断哪种是主流模式。\n- 14B 的 EDD=0（d0v1 AUC=0.643）可能是 self-reference + quantization 的产物。\n- Abstract \"depth signal persists at larger scales\" 对 14B 不成立。\n- **修复**: Abstract 中 14B 标记为 boundary condition；限制 \"existence proof\" claim 为 7-8B。\n\n### Should-Fix（共识或 Director 裁定）\n\n**W3 [Should-Fix, R1 Must-Fix / R2 Should-Fix, Director 裁定 Should-Fix]: d0 recall >97% 膨胀 headline metrics。**\n- Abstract 和 Contribution 列表仍以四类准确率为主导叙事。Cross-model transfer 66.4% headline → 55.4% d1-d3；Cross-strategy 59.1% → 45.9% d1-d3。Pythia holdout d2 recall 仅 26.8%。\n- 论文已在每个 table 旁系统性并列 d1-d3 balanced accuracy（相比 Round 12 有改善），但 Abstract 仍以四类准确率领头。\n- **修复**: Abstract 和 Contribution 列表以 d1-d3 balanced accuracy 为主指标。\n\n**W4 [Should-Fix, R2 Must-Fix / R1 Should-Fix, Director 裁定 Should-Fix]: Abstract 数字堆砌。**\n- Abstract 9 句话包含 20+ 个数值，读起来像 results summary 而非叙事。信息完整但缺乏吸引力。Round 12 已提出但未修复。\n- **修复**: 减少到 8-10 个关键数字，叙事主线放在困惑度尾部统计洞察上。\n\n**W5 [Should-Fix, R2 Must-Fix / R1 Should-Fix, Director 裁定 Should-Fix]: Discussion 过薄。**\n- 从 Round 12 的 ~80 词扩展到 ~250 词（3 段），有改善但仍不足以承载 9 cell + 8 泛化轴的 empirical study insight。Appendix N 的 provenance toolkit 讨论和 cross-strategy conditional decomposition 是有价值的材料但被放逐到附录。\n- **修复**: 将 provenance toolkit 讨论提升到正文；新增 cross-strategy barrier 作为 empirical contribution 的分析和 depth-as-process vs depth-estimation 的概念区分。\n\n**W6 [Should-Fix, consensus]: Full-replacement only 缺乏 accumulation 实验。**\n- 所有实验使用 full-replacement chains。Discussion 声称这是 accumulation 的 \"ceiling estimate\"，但缺乏理论或实验支持。Accumulation 设置下特征行为可能完全不同。Round 12 至今未补充任何 accumulation 实验。\n- **修复**: 至少做一个 toy-scale accumulation 实验验证 upper bound 假设。\n\n**W7 [Should-Fix, consensus]: Curation PoC 统计分析有误。**\n- 核心比较（RF-filtered vs unfiltered）全部不显著（p>0.4）。RF vs random 的 Bonferroni 校正后，Appendix N 声称 \"2 of 3 surviving\" 不准确（rf_moderate vs random_moderate p=0.020 > α=0.017）。\n- **修复**: 修正 Bonferroni 表述；将 curation 描述为 negative/inconclusive result。\n\n**W8 [Should-Fix, consensus]: VIF>10 下 feature importance 解释过度。**\n- 14-16/19 features VIF>10，脚注承认 multicollinearity caveat，但 Table 3 仍展示逐特征精确 importance 值。Group-level claim（Kendall's W=0.90）可靠，但 individual feature rankings 不稳定。\n- **修复**: 将脚注 caveat 提升为正文段落；Table 3 caption 明确注明 individual rankings unstable。\n\n**W9 [Should-Fix, consensus]: EDD contiguous prefix 在非单调场景下过于保守。**\n- EDD 要求所有 pairwise AUC 从 (0,1) 到 (d*,d*+1) 均超过 T。非单调 AUC（Qwen2.5-7B U型, cross-strategy d1v2 AUC 低至 0.129）下 EDD 大幅低估真实可区分范围。Limitations 承认但无替代方案。\n- **修复**: 提供补充指标（如 Maximum Discriminable Depth）；§3.5 明确适用条件。\n\n**W10 [Should-Fix, consensus]: Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高。**\n- seed=43 在所有 3 cell 中均优于 seed=42（+0.14 到 +3.17pp），2/3 统计显著。Table 2 中多个跨 cell 差异可能在 seed noise 范围内（~1-3pp）。\n\n### Minor\n\n**W11 [Minor, divergence]: 方法层面无算法贡献。** R2 列为 Should-Fix，R1 REBUT（ARR guidelines H2 保护 empirical contribution）。论文已在 Introduction 明确声明 empirical contribution 定位，classifier convergence 本身是有价值的 empirical finding。Director 裁定：这是论文 excitement 的主要限制因素，但不构成 soundness 问题。\n\n**W12 [Minor, consensus]: AI 写作痕迹。** -ing 短语（confirming/demonstrating/suggesting...）正文+附录共 20 次。不影响技术内容但为审稿人可见的 AI 写作标志。\n\n**W13 [Minor]: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007_importance_weighting）在 bib 中但未被 cite。**\n\n**W14 [Minor]: 单一 LoRA 超参配置，缺乏 rank/lr 敏感性分析。**\n\n**W15 [Minor]: Prompted generation 验证仅 1/9 cell（GPT-2 XL nucleus），-13.8pp 下降幅度下 top-k 配置可能逼近 chance。**\n\n---\n\n## Reviewer Consensus\n\n**完全一致 [AGREE] 的问题:**\n1. Reference model circularity claim 需修正（R1-W1 / R2 AGREE）\n2. Cross-scale 14B 结论不可靠，Abstract 表述需校准（R1-W2 / R2-W7 / 双方 AGREE）\n3. Full-replacement scope 是核心限制，缺乏 accumulation 实验（R1-W8 / R2-W4 / 双方 AGREE）\n4. Curation PoC 统计分析需修正（R1-W4 / R2-W9 / 双方 AGREE）\n5. VIF>10 下 feature importance 解释过度（R1-W5 / R2 AGREE）\n6. EDD contiguous prefix 在非单调下过于保守（R1-W6 / R2 AGREE）\n7. Cross-seed replication 不足（R1-W7 / R2 AGREE）\n8. 孤儿引用需清理（R2-W8 / R1 AGREE）\n9. Curation PoC 需 multiple comparison correction（R2-W9 / R1-W4 AGREE）\n10. 任务形式化是真正的新贡献（S1 双方一致）\n11. 实验设计系统全面（S2 双方一致）\n\n## Reviewer Divergence\n\n**R1 Must-Fix / R2 Should-Fix:**\n- d0 inflation: R1 认为 Abstract 应以 d1-d3 为主指标（Must-Fix），R2 认为论文已通过并列 d1-d3 balanced accuracy 充分处理（Should-Fix）。**Director 裁定 Should-Fix**：transparency 已改善，但 Abstract 叙事仍需调整。\n\n**R2 Must-Fix / R1 Should-Fix:**\n- Abstract 数字堆砌: R2 列为 Must-Fix，R1 AGREE 但降为 Should-Fix（信息完整性无问题）。**Director 裁定 Should-Fix**。\n- Discussion 过薄: R2 列为 Must-Fix，R1 AGREE 但降为 Should-Fix（影响 excitement 而非 soundness）。**Director 裁定 Should-Fix**。\n\n**R2 Should-Fix / R1 REBUT:**\n- 方法无算法贡献: R2 认为 RF + 已知特征不足以支撑 Conference（Should-Fix），R1 引用 ARR guidelines H2 和 empirical contribution 先例 REBUT。**Director 裁定**：合理的审美分歧，记录但不作为降分依据。\n- EDD 创新有限: R2 认为本质是 pairwise AUC + threshold，R1 REBUT（operationalization 有独立价值，类比 BLEU/ROUGE）。**Director 裁定**：R1 论据更有说服力。\n\n---\n\n## Questions（需要作者在 Rebuttal 中回答）\n\n**Q1 [R1]:** Table 8 self-reference 带来 4-11pp 优势，§3.4 如何与 \"no systematic advantage\" 调和？\n\n**Q2 [R1]:** Full-replacement \"upper bound\" 假设有何实验或理论依据？是否存在 accumulation 反而增强某些深度信号的可能？\n\n**Q3 [R1]:** seed=43 系统性偏高的原因？d3 outlier 比例 0.56% vs 12.8% 但 seed=43 准确率更高——clipping 机制是否为完整解释？\n\n**Q4 [R1]:** Cross-strategy transfer d1-d3: 45.9% 是否足以支持 \"data auditing\" 实用 claim？\n\n**Q5 [R2]:** Cross-strategy d1/d2 inversion 是否意味着 depth 作为统计量的 strategy-invariance 不成立？depth-as-process 和 depth-as-estimable-quantity 的边界在哪里？\n\n**Q6 [R2]:** GPT-2 XL 始终最高准确率：是 architecture effect 还是 reference model 分布差异效应？\n\n**Q7 [R2]:** EDD=4 跨三个 family 一致性有无超出经验观察的理论基础？\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大引用遗漏。Related Work 覆盖全面（69 引用），model collapse theory、AI text detection、membership inference、ordinal classification、decoding strategy effects 主要工作均已纳入。\n\n建议关注：\n- Synthetic data contamination in the wild 的实证研究（2025-2026 新工作）\n- LoRA 微调与模型坍塌交互的工作\n\n3 条孤儿引用需删除或添加 cite（llama3, qwen2.5, sugiyama2007_importance_weighting）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分区间**: R1 给 3.5 (Borderline Conference), R2 给 3.0 (Findings)。\n\n**Director 裁定 3.0 (Findings) 的理由:**\n\n论文的核心贡献——将递归生成深度估计形式化为序数分类并构建系统性基准——是有意义且及时的。在 1-1.5B full-replacement 范围内的实验设计审慎，控制实验（LOGO、negative control、reverse chain）是亮点，reporting 诚信度高。\n\n但以下问题的组合将论文限制在 Findings 水平：\n\n1. **Claim 校准问题**（W1, W2）：reference model circularity 的误导性 claim 和 cross-scale 的过度乐观表述是方法严谨性缺陷，需要实质性修正。\n\n2. **生态效度不足**（W6）：full-replacement only 且无任何 accumulation 实验，\"upper bound\" 假设未经验证。这限制了论文从实验室到部署的路径说服力。\n\n3. **写作深度不足**（W4, W5）：Abstract 数字堆砌缺乏叙事吸引力，Discussion ~250 词无法承载 empirical study 的 insight 深度。这些是 impression management 问题，但在审稿人快速判断价值时影响显著。\n\n4. **方法层面无算法贡献**（W11）：虽然 ARR guidelines 保护 empirical contribution，标准 RF + 标准特征的组合在 excitement 维度上是限制因素。classifier convergence 证明了特征为瓶颈，但也意味着当前 pipeline 已触及 ceiling。\n\n**从 3.0 提升到 3.5 的路径：**\n- 修复 W1（reference model claim）和 W2（cross-scale claim 校准）→ 消除 soundness concerns\n- 充实 Discussion（W5）+ 重写 Abstract（W4）→ 提升 excitement/impression\n- 补充 accumulation pilot（W6）→ 提升生态效度\n\n这些修改在 rebuttal + revision cycle 内是可行的。\n\n---\n\n## Detailed Comments（按 Section）\n\n### Abstract\n- 20+ 数字堆砌，缺乏叙事吸引力（W4）。应以 d1-d3 balanced accuracy 为主指标（W3）。\n- \"depth signal persists at larger scales\" 对 14B（EDD=0）不准确（W2）。\n- \"Preliminary cross-scale experiments (7-14B, 54-70%)\" 应将 14B 明确标记为 boundary condition。\n- \"a single-cell prompted-generation test 69.5%\" 的 qualifier 是诚实的，保持。\n\n### §1 Introduction\n- Full-replacement scope 说明在第 2 段出现，位置合理但可更前置。\n- Contribution 列表中 \"EDD_{0.70}=4 for all three families\" 需注明这是 1-1.5B 结果。\n- Empirical contribution 定位声明是恰当的。\n\n### §2 Related Work\n- 覆盖全面，69 引用，结构清晰（6 个 paragraph 按主题分组）。\n- 与 Mohamed et al. (2025) \"Broken Telephone\" 的区分清晰但可补充为何其 degradation characterization 不能直接用于深度分类。\n\n### §3 Method\n- §3.4: \"confers no systematic advantage\" 必须修正（W1）。建议改为 \"confers a measurable advantage on same-family data (4-11pp; Appendix H) but does not drive the cross-generator accuracy ranking\"。\n- §3.5 EDD: Definition 1 的适用条件（monotonic AUC decay）应在定义正文而非脚注中明确（W9）。\n- §3.6 Theoretical Grounding: 简洁有效，strategy-dependent convergence 的论述有理论支持。\n\n### §4 Atlas\n- §4.1: Table 2 建议增加 d1-d3 balanced accuracy 列。Pythia 行应标注 self-reference。\n- §4.2: Footnote 3 的 multicollinearity caveat 应提升为正文段落（W8）。Table 3 caption 应注明 individual rankings unstable under VIF>10。\n- §4.3: Monotonicity analysis 简洁有效。\n- §4.4: EDD analysis 是论文亮点。AUC decay curves (Figure 2) 信息密度高。\n\n### §5 Generalization\n- §5.1: \"within 0.4pp\" 收敛 claim 是否经过等价性检验（如 TOST）？\n- §5.3: Cross-strategy transfer 的 boundary inversion 分析是有价值的 empirical finding，但 Discussion 中应更深入地讨论 depth-as-process vs depth-estimation 的概念区分。\n- §5.4: \"existence proof\" 措辞合适，但需限制为 7-8B。14B 应明确标记为 boundary condition。\n\n### §6 Discussion\n- ~250 词 3 段，有改善但仍不足。建议提升 Appendix N 内容到正文，新增 cross-strategy barrier 分析和 feature adaptation 讨论。\n\n### Limitations\n- 质量很高，主动覆盖了 9 个 limitation。Reference model circularity 的更诚实表述应从 Limitations 前移到 §3.4。\n\n### Ethics Statement\n- 简洁充分，覆盖了公开模型/数据使用、无人类受试者、潜在误用风险。\n\n### Appendix\n- 全面且有价值（16 个 subsection）。Appendix K（Curation PoC）的 Bonferroni 校正需修正（W7）。建议 Appendix N（Extended Discussion）中最重要的内容移回正文。\n\n### 格式合规\n- 模板: ACL style (review mode) ✓\n- 匿名: \"Anonymous\" author ✓，未发现作者信息泄露\n- Limitations: 存在且实质性 ✓\n- Ethics Statement: 存在 ✓\n- 引用格式: natbib, 基本一致 ✓\n- 3 条孤儿引用需清理（W13）\n\n---\n\n## 与 Round 12 问题对照\n\n| Round 12 Issue | R13 状态 | 备注 |\n|---|---|---|\n| R12-W1 生态效度/scope | 部分改善 | 添加了 scope 声明和 Discussion 段落，但仍缺 accumulation 实验 |\n| R12-W2 Cross-strategy 45.9% | 改善 | 重定位为 key empirical finding，措辞修改 |\n| R12-W3 d0 inflation | 改善 | d1-d3 balanced acc 系统性并列，但 Abstract 仍以四类为主 |\n| R12-W4 Cross-scale confounds | 部分改善 | 标题改为 Preliminary，但 Abstract 表述仍过度乐观 |\n| R12-W5 Curation PoC | 部分改善 | 标记 inconclusive 但 Bonferroni 表述仍有误 |\n| R12-W6 Abstract 数字堆砌 | 未修复 | 仍 20+ 数字 |\n| R12-W7 Discussion 过薄 | 部分改善 | 从 ~80 词扩展到 ~250 词，但仍不足 |\n| R12-W8 Feature importance 共线性 | 部分改善 | 添加脚注 caveat 但 Table 3 仍展示个体 importance |\n| R12-W9 算法贡献不足 | 改善 | Introduction 明确 empirical contribution 定位 |\n| R12-M1 EDD threshold | 可能已修复 | 添加 T 敏感性分析 |\n| R12-M2 RF ordinal claim | 可能已修复 | 弱化为 ordinally consistent predictions |\n| R12-M3 Reference model 重叠 | 恶化 | 新增误导性 \"no systematic advantage\" claim，与 Table 8 矛盾 |\n| R12-M4 Prompted gen 1/9 | 部分改善 | 添加 single-cell qualifier |\n| R12-M6 孤儿 bib | 复发 | c2pa2024 删除但新增 3 条孤儿 |\n| R12-M7 GPU claim | 可能已修复 | 修正为 CPU ~50 min |\n| R12-M8 遗漏引用 | 可能已修复 | muennighoff + ilyas 已入 bib |",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "report": "# 审稿报告 — Round 13 (Fresh Review)\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**目标 Venue**: EMNLP 2026 (ARR May cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+写作完整性+Related Work）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文将递归生成深度估计（recursive generation depth estimation）形式化为序数分类任务，构建了 180K 样本的基准测试集（3 个模型族 × 3 种解码策略 × 4 个深度等级），使用基于 19 个统计特征的 Random Forest 进行分类，并提出 Effective Discriminable Depth (EDD) 指标量化相邻深度的可区分极限。论文在多个泛化轴（跨模型、跨策略、跨域、跨尺度）上进行了系统实验，核心发现是困惑度尾部特征族（p90_ppl、var_surprisal）在所有 9 个 model-strategy cell 中主导深度判别，EDD_{0.70}=4 for all three model families at 1-1.5B scale。\n\n---\n\n## Strengths\n\n**S1: 任务形式化填补真实空白。** 在二元检测（human vs. machine）和模型坍塌理论（假定深度已知）之间，序数深度估计是一个未被研究的新维度。EDD 指标将 model collapse 理论的定性预测转化为可操作的定量指标。两位 Reviewer 一致认可这是论文最重要的贡献。\n\n**S2: 基准设计系统且全面。** 3×3 grid（模型族 × 解码策略）覆盖了合理的变异来源，180K 样本规模充足，8 个泛化轴的测试体系（跨模型、跨策略、跨域、跨尺度、prompted generation、跨模型链、深度扩展、温度鲁棒性）在 empirical study 中罕见地系统。\n\n**S3: 控制实验和报告诚信度高。** Domain bias analysis 中的 LOGO 评估（72.1% 匹配标准 CV 72.0%）和 seed-group negative control（10.2%, chance level）有效排除了 topic leakage。修正 bug 后如实报告修正前后数据体现研究诚信。Limitations 章节主动讨论了 full-replacement vs. accumulation、d0 inflation、cross-strategy boundary inversion、reference model dependency 等多个 limitation，透明度在提交稿中罕见。\n\n**S4: 分类器收敛验证了特征为核心。** RF、XGBoost、LightGBM 在 0.4pp 内收敛（§5.1），CORAL/DivEye 在 0.6pp 内匹配（p>0.05），有力论证信号来自特征设计而非分类器架构。这本身是一个有价值的 empirical finding。\n\n**S5: Related Work 覆盖全面。** 69 条引用，覆盖 model collapse theory、AI text detection、membership inference、ordinal classification、decoding strategy effects 等主要领域，2025-2026 最新工作均已纳入。\n\n**S6: 跨模型递归链实验有说服力。** 异构链（Pythia→OLMo→GPT-2 XL, 84.75%）和反向链（GPT-2 XL→OLMo→Pythia, 85.75%）有效排除了架构指纹假说，为 process-level depth signal 提供了初步证据。\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识）\n\n**W1 [Must-Fix, consensus]: Reference model circularity claim 与消融数据直接矛盾。**\n- §3.4 声称 Pythia-1.4B 同时作为 generator 和 reference model \"confers no systematic advantage\"，论据是 Pythia 数据（78.7%）低于 GPT-2 XL 数据（85.9%）。\n- 但这是跨 generator 的混淆比较。Appendix H（Table 8）的公平消融显示：在 Pythia 生成的数据上，self-reference（78.6%）> OLMo 参考（74.5%）> GPT-2 XL 参考（67.3%），self-reference 带来 4.1-11.3pp 优势。\n- Limitations 也承认 \"same-family references yield optimal performance\"。\n- 这使得 9 个 cell 的横向比较不公平：Pythia cell 可能因 self-reference 被高估，OLMo/GPT-2 XL cell 因 cross-reference 被低估。\n- **修复**: 修正 §3.4 claim，承认 self-reference 带来可测量优势；Table 2 Pythia 行注明 self-reference。\n\n**W2 [Must-Fix, consensus]: Cross-scale 实验的 5 个混淆因素使结论不可靠，Abstract 表述过度乐观。**\n- 7-14B 实验受 5 个混淆因素限制（QLoRA 4-bit 量化 / 500 vs 5000 samples / 仅 nucleus 策略 / 词表不匹配 / 14B self-reference）。\n- 仅 2 个 7-8B 模型给出方向相反的 AUC 轨迹（Llama-3.1 单调 vs Qwen2.5 U型），无法判断哪种是主流模式。\n- 14B 的 EDD=0（d0v1 AUC=0.643）可能是 self-reference + quantization 的产物。\n- Abstract \"depth signal persists at larger scales\" 对 14B 不成立。\n- **修复**: Abstract 中 14B 标记为 boundary condition；限制 \"existence proof\" claim 为 7-8B。\n\n### Should-Fix（共识或 Director 裁定）\n\n**W3 [Should-Fix, R1 Must-Fix / R2 Should-Fix, Director 裁定 Should-Fix]: d0 recall >97% 膨胀 headline metrics。**\n- Abstract 和 Contribution 列表仍以四类准确率为主导叙事。Cross-model transfer 66.4% headline → 55.4% d1-d3；Cross-strategy 59.1% → 45.9% d1-d3。Pythia holdout d2 recall 仅 26.8%。\n- 论文已在每个 table 旁系统性并列 d1-d3 balanced accuracy（相比 Round 12 有改善），但 Abstract 仍以四类准确率领头。\n- **修复**: Abstract 和 Contribution 列表以 d1-d3 balanced accuracy 为主指标。\n\n**W4 [Should-Fix, R2 Must-Fix / R1 Should-Fix, Director 裁定 Should-Fix]: Abstract 数字堆砌。**\n- Abstract 9 句话包含 20+ 个数值，读起来像 results summary 而非叙事。信息完整但缺乏吸引力。Round 12 已提出但未修复。\n- **修复**: 减少到 8-10 个关键数字，叙事主线放在困惑度尾部统计洞察上。\n\n**W5 [Should-Fix, R2 Must-Fix / R1 Should-Fix, Director 裁定 Should-Fix]: Discussion 过薄。**\n- 从 Round 12 的 ~80 词扩展到 ~250 词（3 段），有改善但仍不足以承载 9 cell + 8 泛化轴的 empirical study insight。Appendix N 的 provenance toolkit 讨论和 cross-strategy conditional decomposition 是有价值的材料但被放逐到附录。\n- **修复**: 将 provenance toolkit 讨论提升到正文；新增 cross-strategy barrier 作为 empirical contribution 的分析和 depth-as-process vs depth-estimation 的概念区分。\n\n**W6 [Should-Fix, consensus]: Full-replacement only 缺乏 accumulation 实验。**\n- 所有实验使用 full-replacement chains。Discussion 声称这是 accumulation 的 \"ceiling estimate\"，但缺乏理论或实验支持。Accumulation 设置下特征行为可能完全不同。Round 12 至今未补充任何 accumulation 实验。\n- **修复**: 至少做一个 toy-scale accumulation 实验验证 upper bound 假设。\n\n**W7 [Should-Fix, consensus]: Curation PoC 统计分析有误。**\n- 核心比较（RF-filtered vs unfiltered）全部不显著（p>0.4）。RF vs random 的 Bonferroni 校正后，Appendix N 声称 \"2 of 3 surviving\" 不准确（rf_moderate vs random_moderate p=0.020 > α=0.017）。\n- **修复**: 修正 Bonferroni 表述；将 curation 描述为 negative/inconclusive result。\n\n**W8 [Should-Fix, consensus]: VIF>10 下 feature importance 解释过度。**\n- 14-16/19 features VIF>10，脚注承认 multicollinearity caveat，但 Table 3 仍展示逐特征精确 importance 值。Group-level claim（Kendall's W=0.90）可靠，但 individual feature rankings 不稳定。\n- **修复**: 将脚注 caveat 提升为正文段落；Table 3 caption 明确注明 individual rankings unstable。\n\n**W9 [Should-Fix, consensus]: EDD contiguous prefix 在非单调场景下过于保守。**\n- EDD 要求所有 pairwise AUC 从 (0,1) 到 (d*,d*+1) 均超过 T。非单调 AUC（Qwen2.5-7B U型, cross-strategy d1v2 AUC 低至 0.129）下 EDD 大幅低估真实可区分范围。Limitations 承认但无替代方案。\n- **修复**: 提供补充指标（如 Maximum Discriminable Depth）；§3.5 明确适用条件。\n\n**W10 [Should-Fix, consensus]: Cross-seed replication 仅 3/9 cells，seed=43 系统性偏高。**\n- seed=43 在所有 3 cell 中均优于 seed=42（+0.14 到 +3.17pp），2/3 统计显著。Table 2 中多个跨 cell 差异可能在 seed noise 范围内（~1-3pp）。\n\n### Minor\n\n**W11 [Minor, divergence]: 方法层面无算法贡献。** R2 列为 Should-Fix，R1 REBUT（ARR guidelines H2 保护 empirical contribution）。论文已在 Introduction 明确声明 empirical contribution 定位，classifier convergence 本身是有价值的 empirical finding。Director 裁定：这是论文 excitement 的主要限制因素，但不构成 soundness 问题。\n\n**W12 [Minor, consensus]: AI 写作痕迹。** -ing 短语（confirming/demonstrating/suggesting...）正文+附录共 20 次。不影响技术内容但为审稿人可见的 AI 写作标志。\n\n**W13 [Minor]: 3 条孤儿引用（llama3, qwen2.5, sugiyama2007_importance_weighting）在 bib 中但未被 cite。**\n\n**W14 [Minor]: 单一 LoRA 超参配置，缺乏 rank/lr 敏感性分析。**\n\n**W15 [Minor]: Prompted generation 验证仅 1/9 cell（GPT-2 XL nucleus），-13.8pp 下降幅度下 top-k 配置可能逼近 chance。**\n\n---\n\n## Reviewer Consensus\n\n**完全一致 [AGREE] 的问题:**\n1. Reference model circularity claim 需修正（R1-W1 / R2 AGREE）\n2. Cross-scale 14B 结论不可靠，Abstract 表述需校准（R1-W2 / R2-W7 / 双方 AGREE）\n3. Full-replacement scope 是核心限制，缺乏 accumulation 实验（R1-W8 / R2-W4 / 双方 AGREE）\n4. Curation PoC 统计分析需修正（R1-W4 / R2-W9 / 双方 AGREE）\n5. VIF>10 下 feature importance 解释过度（R1-W5 / R2 AGREE）\n6. EDD contiguous prefix 在非单调下过于保守（R1-W6 / R2 AGREE）\n7. Cross-seed replication 不足（R1-W7 / R2 AGREE）\n8. 孤儿引用需清理（R2-W8 / R1 AGREE）\n9. Curation PoC 需 multiple comparison correction（R2-W9 / R1-W4 AGREE）\n10. 任务形式化是真正的新贡献（S1 双方一致）\n11. 实验设计系统全面（S2 双方一致）\n\n## Reviewer Divergence\n\n**R1 Must-Fix / R2 Should-Fix:**\n- d0 inflation: R1 认为 Abstract 应以 d1-d3 为主指标（Must-Fix），R2 认为论文已通过并列 d1-d3 balanced accuracy 充分处理（Should-Fix）。**Director 裁定 Should-Fix**：transparency 已改善，但 Abstract 叙事仍需调整。\n\n**R2 Must-Fix / R1 Should-Fix:**\n- Abstract 数字堆砌: R2 列为 Must-Fix，R1 AGREE 但降为 Should-Fix（信息完整性无问题）。**Director 裁定 Should-Fix**。\n- Discussion 过薄: R2 列为 Must-Fix，R1 AGREE 但降为 Should-Fix（影响 excitement 而非 soundness）。**Director 裁定 Should-Fix**。\n\n**R2 Should-Fix / R1 REBUT:**\n- 方法无算法贡献: R2 认为 RF + 已知特征不足以支撑 Conference（Should-Fix），R1 引用 ARR guidelines H2 和 empirical contribution 先例 REBUT。**Director 裁定**：合理的审美分歧，记录但不作为降分依据。\n- EDD 创新有限: R2 认为本质是 pairwise AUC + threshold，R1 REBUT（operationalization 有独立价值，类比 BLEU/ROUGE）。**Director 裁定**：R1 论据更有说服力。\n\n---\n\n## Questions（需要作者在 Rebuttal 中回答）\n\n**Q1 [R1]:** Table 8 self-reference 带来 4-11pp 优势，§3.4 如何与 \"no systematic advantage\" 调和？\n\n**Q2 [R1]:** Full-replacement \"upper bound\" 假设有何实验或理论依据？是否存在 accumulation 反而增强某些深度信号的可能？\n\n**Q3 [R1]:** seed=43 系统性偏高的原因？d3 outlier 比例 0.56% vs 12.8% 但 seed=43 准确率更高——clipping 机制是否为完整解释？\n\n**Q4 [R1]:** Cross-strategy transfer d1-d3: 45.9% 是否足以支持 \"data auditing\" 实用 claim？\n\n**Q5 [R2]:** Cross-strategy d1/d2 inversion 是否意味着 depth 作为统计量的 strategy-invariance 不成立？depth-as-process 和 depth-as-estimable-quantity 的边界在哪里？\n\n**Q6 [R2]:** GPT-2 XL 始终最高准确率：是 architecture effect 还是 reference model 分布差异效应？\n\n**Q7 [R2]:** EDD=4 跨三个 family 一致性有无超出经验观察的理论基础？\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大引用遗漏。Related Work 覆盖全面（69 引用），model collapse theory、AI text detection、membership inference、ordinal classification、decoding strategy effects 主要工作均已纳入。\n\n建议关注：\n- Synthetic data contamination in the wild 的实证研究（2025-2026 新工作）\n- LoRA 微调与模型坍塌交互的工作\n\n3 条孤儿引用需删除或添加 cite（llama3, qwen2.5, sugiyama2007_importance_weighting）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分区间**: R1 给 3.5 (Borderline Conference), R2 给 3.0 (Findings)。\n\n**Director 裁定 3.0 (Findings) 的理由:**\n\n论文的核心贡献——将递归生成深度估计形式化为序数分类并构建系统性基准——是有意义且及时的。在 1-1.5B full-replacement 范围内的实验设计审慎，控制实验（LOGO、negative control、reverse chain）是亮点，reporting 诚信度高。\n\n但以下问题的组合将论文限制在 Findings 水平：\n\n1. **Claim 校准问题**（W1, W2）：reference model circularity 的误导性 claim 和 cross-scale 的过度乐观表述是方法严谨性缺陷，需要实质性修正。\n\n2. **生态效度不足**（W6）：full-replacement only 且无任何 accumulation 实验，\"upper bound\" 假设未经验证。这限制了论文从实验室到部署的路径说服力。\n\n3. **写作深度不足**（W4, W5）：Abstract 数字堆砌缺乏叙事吸引力，Discussion ~250 词无法承载 empirical study 的 insight 深度。这些是 impression management 问题，但在审稿人快速判断价值时影响显著。\n\n4. **方法层面无算法贡献**（W11）：虽然 ARR guidelines 保护 empirical contribution，标准 RF + 标准特征的组合在 excitement 维度上是限制因素。classifier convergence 证明了特征为瓶颈，但也意味着当前 pipeline 已触及 ceiling。\n\n**从 3.0 提升到 3.5 的路径：**\n- 修复 W1（reference model claim）和 W2（cross-scale claim 校准）→ 消除 soundness concerns\n- 充实 Discussion（W5）+ 重写 Abstract（W4）→ 提升 excitement/impression\n- 补充 accumulation pilot（W6）→ 提升生态效度\n\n这些修改在 rebuttal + revision cycle 内是可行的。\n\n---\n\n## Detailed Comments（按 Section）\n\n### Abstract\n- 20+ 数字堆砌，缺乏叙事吸引力（W4）。应以 d1-d3 balanced accuracy 为主指标（W3）。\n- \"depth signal persists at larger scales\" 对 14B（EDD=0）不准确（W2）。\n- \"Preliminary cross-scale experiments (7-14B, 54-70%)\" 应将 14B 明确标记为 boundary condition。\n- \"a single-cell prompted-generation test 69.5%\" 的 qualifier 是诚实的，保持。\n\n### §1 Introduction\n- Full-replacement scope 说明在第 2 段出现，位置合理但可更前置。\n- Contribution 列表中 \"EDD_{0.70}=4 for all three families\" 需注明这是 1-1.5B 结果。\n- Empirical contribution 定位声明是恰当的。\n\n### §2 Related Work\n- 覆盖全面，69 引用，结构清晰（6 个 paragraph 按主题分组）。\n- 与 Mohamed et al. (2025) \"Broken Telephone\" 的区分清晰但可补充为何其 degradation characterization 不能直接用于深度分类。\n\n### §3 Method\n- §3.4: \"confers no systematic advantage\" 必须修正（W1）。建议改为 \"confers a measurable advantage on same-family data (4-11pp; Appendix H) but does not drive the cross-generator accuracy ranking\"。\n- §3.5 EDD: Definition 1 的适用条件（monotonic AUC decay）应在定义正文而非脚注中明确（W9）。\n- §3.6 Theoretical Grounding: 简洁有效，strategy-dependent convergence 的论述有理论支持。\n\n### §4 Atlas\n- §4.1: Table 2 建议增加 d1-d3 balanced accuracy 列。Pythia 行应标注 self-reference。\n- §4.2: Footnote 3 的 multicollinearity caveat 应提升为正文段落（W8）。Table 3 caption 应注明 individual rankings unstable under VIF>10。\n- §4.3: Monotonicity analysis 简洁有效。\n- §4.4: EDD analysis 是论文亮点。AUC decay curves (Figure 2) 信息密度高。\n\n### §5 Generalization\n- §5.1: \"within 0.4pp\" 收敛 claim 是否经过等价性检验（如 TOST）？\n- §5.3: Cross-strategy transfer 的 boundary inversion 分析是有价值的 empirical finding，但 Discussion 中应更深入地讨论 depth-as-process vs depth-estimation 的概念区分。\n- §5.4: \"existence proof\" 措辞合适，但需限制为 7-8B。14B 应明确标记为 boundary condition。\n\n### §6 Discussion\n- ~250 词 3 段，有改善但仍不足。建议提升 Appendix N 内容到正文，新增 cross-strategy barrier 分析和 feature adaptation 讨论。\n\n### Limitations\n- 质量很高，主动覆盖了 9 个 limitation。Reference model circularity 的更诚实表述应从 Limitations 前移到 §3.4。\n\n### Ethics Statement\n- 简洁充分，覆盖了公开模型/数据使用、无人类受试者、潜在误用风险。\n\n### Appendix\n- 全面且有价值（16 个 subsection）。Appendix K（Curation PoC）的 Bonferroni 校正需修正（W7）。建议 Appendix N（Extended Discussion）中最重要的内容移回正文。\n\n### 格式合规\n- 模板: ACL style (review mode) ✓\n- 匿名: \"Anonymous\" author ✓，未发现作者信息泄露\n- Limitations: 存在且实质性 ✓\n- Ethics Statement: 存在 ✓\n- 引用格式: natbib, 基本一致 ✓\n- 3 条孤儿引用需清理（W13）\n\n---\n\n## 与 Round 12 问题对照\n\n| Round 12 Issue | R13 状态 | 备注 |\n|---|---|---|\n| R12-W1 生态效度/scope | 部分改善 | 添加了 scope 声明和 Discussion 段落，但仍缺 accumulation 实验 |\n| R12-W2 Cross-strategy 45.9% | 改善 | 重定位为 key empirical finding，措辞修改 |\n| R12-W3 d0 inflation | 改善 | d1-d3 balanced acc 系统性并列，但 Abstract 仍以四类为主 |\n| R12-W4 Cross-scale confounds | 部分改善 | 标题改为 Preliminary，但 Abstract 表述仍过度乐观 |\n| R12-W5 Curation PoC | 部分改善 | 标记 inconclusive 但 Bonferroni 表述仍有误 |\n| R12-W6 Abstract 数字堆砌 | 未修复 | 仍 20+ 数字 |\n| R12-W7 Discussion 过薄 | 部分改善 | 从 ~80 词扩展到 ~250 词，但仍不足 |\n| R12-W8 Feature importance 共线性 | 部分改善 | 添加脚注 caveat 但 Table 3 仍展示个体 importance |\n| R12-W9 算法贡献不足 | 改善 | Introduction 明确 empirical contribution 定位 |\n| R12-M1 EDD threshold | 可能已修复 | 添加 T 敏感性分析 |\n| R12-M2 RF ordinal claim | 可能已修复 | 弱化为 ordinally consistent predictions |\n| R12-M3 Reference model 重叠 | 恶化 | 新增误导性 \"no systematic advantage\" claim，与 Table 8 矛盾 |\n| R12-M4 Prompted gen 1/9 | 部分改善 | 添加 single-cell qualifier |\n| R12-M6 孤儿 bib | 复发 | c2pa2024 删除但新增 3 条孤儿 |\n| R12-M7 GPU claim | 可能已修复 | 修正为 CPU ~50 min |\n| R12-M8 遗漏引用 | 可能已修复 | muennighoff + ilyas 已入 bib |",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-19T06:52:04.781342+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4470
}
```

</details>

---


### Assistant

_source line 1016 · 2026-05-19T06:52:15.996324+00:00_

审稿报告已投递。

---

**Round 13 审稿完成总结：**

| 项目 | 内容 |
|------|------|
| **Overall** | **3.0 (Findings)** |
| **R1 评分** | 3.5 (Borderline Conference) |
| **R2 评分** | 3.0 (Findings) |
| **Must-Fix** | 2 项（reference model circularity claim 矛盾、cross-scale 14B claim 过度乐观） |
| **Should-Fix** | 8 项（d0 inflation 叙事、Abstract 数字堆砌、Discussion 过薄、缺 accumulation 实验、curation PoC 统计错误、feature importance 过度解释、EDD 保守性、cross-seed 不足） |
| **Minor** | 5 项（算法贡献不足[分歧]、AI 写作痕迹、孤儿引用、单一 LoRA 配置、prompted gen 1/9 cell） |
| **交叉共识** | 11/15 点完全一致 |
| **与 R12 对照** | 多数问题部分改善，R12-M3 恶化（新增误导性 claim），R12-W6 未修复 |
| **提升路径** | 修复 W1-W2 + 充实 Discussion + 重写 Abstract + accumulation pilot → 可达 3.5 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1017 · 2026-05-19T06:52:18.655464+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

要点总结：
- 与 R2 在 **7 个 Weakness 上一致**（W1/W2/W4/W5/W7/W8/W9），但对 W1 和 W2 的严重程度判断不同（我认为是 Should-Fix，R2 认为 Must-Fix）
- **反驳了 2 个 Weakness**：W3（方法无算法贡献——ARR guidelines 明确不应惩罚 empirical contribution 论文）和 W6（EDD 创新有限——operationalization 有独立价值）
- **不认同降至 3.0**：核心分歧在于 W3/W6 的权重。问题是 claim-strength 校准而非 fundamental flaw，修复后足以支撑 3.5（Borderline Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1018 · 2026-05-19T06:52:24.241430+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 106

## Round 106

178 recorded events


### User

_source line 1019 · 2026-05-20T06:23:04.181998+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-20T06:23:10.282402+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-20T06:23:10.333490+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-20T06:23:15.968230+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-20T06:23:15.968600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-20T06:23:20.135370+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-20T06:23:21.492034+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (139 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **binoculars_14b_topk50** (success): Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy. ← 基于 qwen25_14b_topk50\n  [binoculars_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/binoculars_14b_topk50/report/binoculars_14b_topk50_results.md)\n- **qwen25_14b_topk50** (success): Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\n  [qwen25_14b_topk50_analysis](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report/qwen25_14b_topk50_analysis_b7a903.md) | [qwen25_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-20T06:23:21.994490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-20T06:23:22.547109+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-20T06:23:22.547470+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1029 · 2026-05-20T06:23:22.547652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-20T06:23:22.698553+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1031 · 2026-05-20T06:23:22.749233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-20T06:23:28.071609+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-20T06:23:29.025734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-20T06:23:29.176748+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-20T06:23:36.477943+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results, here's comprehensive information about EMNLP 2026's call for papers, ARR submission, and author guidelines:

## Key Submission Deadlines

The ARR submission deadline for both long and short papers is May 25, 2026, with a reviewer registration deadline for ALL authors of May 27, 2026. The EMNLP commitment deadline is August 2, 2026, with notification of acceptance coming on August 20, 2026.

## Submission Process

EMNLP 2026 uses ACL Rolling Review (ARR) as its reviewing system with final decisions made by the conference. Submissions and commitment of re
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 8406
}
```

</details>

---


### Tool result

_source line 1036 · 2026-05-20T06:23:36.528758+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission deadline page limit"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, I found information about the ACL Rolling Review 2026 May cycle. However, the search results don't contain specific page limit information for the May 2026 cycle. Let me search for more specific details about page limits.

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","u
…[truncated 1937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7503
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-20T06:23:36.579486+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7402
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-20T06:24:04.841047+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" \"May 2026\" submission deadline site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" \"May 2026\" submission deadline site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-20T06:24:09.107976+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read project config for external review",
  "subagent_type": "Explore",
  "prompt": "Search for the project configuration file for \"recursive_gen_depth_est\" in the directory /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/. I need to find settings related to \"external_review\" and \"paperreview_ai\" - whether it's enabled or not. Check files like config.yaml, settings.yaml, project.yaml, or any yaml/json config files in the project root and agent/ subdirectory. Report the exact content of the external_review section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Read project config for external review",
    "subagent_type": "Explore",
    "prompt": "Search for the project configuration file for \"recursive_gen_depth_est\" in the directory /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/. I need to find settings related to \"external_review\" and \"paperreview_ai\" - whether it's enabled or not. Check files like config.yaml, settings.yaml, project.yaml, or any yaml/json config files in the project root and agent/ subdirectory. Report the exact content of the external_review section."
  }
}
```

</details>

---


### Tool result

_source line 1040 · 2026-05-20T06:24:09.409545+00:00_

Web search results for query: ""ACL Rolling Review" "May 2026" submission deadline site:aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – An initiative of the Association for Computational Linguistics","url":"https://aclrollingreview.org/page8/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the search results from the ACL Rolling Review website, I found information about the submission deadlines, though the specific May 2026 deadline details are not explicitly listed in these 
…[truncated 819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4568
}
```

</details>

---


### Tool call

_source line 1041 · 2026-05-20T06:24:14.180189+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/**/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/**/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-20T06:24:14.180774+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_data_seed-prep_20260514T095557_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_code_recursive-gen-chain_20260514T095847_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_code_fix-scripts_20260514T100522_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_code_fix-and-launch-pipeline_20260514T100803_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_QUEUED_20260514T102444.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_ALLOCATED_20260514T102448.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_RUNNING_20260514T102454.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_infra_env-setup_20260514T095535_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_check_status-urgent_20260514T105857_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_RUNNING_20260514T110519.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_004_DONE_20260514T110526.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_infra_kill-instruct-download-base-restart_20260514T110510_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_pipeline_base_003_QUEUED_20260514T112425.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/mvp_
…[truncated 12794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-20T06:24:14.181130+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-20T06:24:14.181414+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/_last_visual_review.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/cross_model_olmo_temp09_001_PENDING_20260514T203413.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/dcol_deberta_005_DONE_20260515T034641.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/depth_extension_pythia_d4d5_001_RUNNING_20260515T040232.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/cross_model_olmo_002_DONE_20260514T170202.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/accum_v3_mix25_QUEUED_20260519T081744.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/w2_domain_bias_001_RUNNING_20260515T192901.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/deberta_pilot_gpt2xl_temp09_ANALYZING_20260519T172116.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/olmo_temp09_002_PENDING_20260515T045918.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/checkpoints/bootstrap_ci_table1_001_RUNNING_20260517T150108.json
/hom
…[truncated 560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1045 · 2026-05-20T06:24:14.181715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1046 · 2026-05-20T06:24:14.181982+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1047 · 2026-05-20T06:24:14.182226+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ | grep -E \"\\.(yaml|yml|json)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ | grep -E \"\\.(yaml|yml|json)$\""
  }
}
```

</details>

---


### Tool result

_source line 1048 · 2026-05-20T06:24:14.182570+00:00_

-rw-r--r--  1 ubuntu ubuntu     90 May 20 06:01 _last_visual_review.json
-rw-------  1 ubuntu ubuntu   1880 May 17 17:30 constraints.yaml
-rw-------  1 ubuntu ubuntu  46604 May 20 05:33 decisions.yaml
-rw-------  1 ubuntu ubuntu   5342 May 18 17:16 dream_registry.yaml
-rw-------  1 ubuntu ubuntu  13493 May 17 17:02 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  26438 May 15 23:57 literature_map.yaml
-rw-------  1 ubuntu ubuntu  11093 May 19 15:06 mistakes.yaml
-rw-------  1 ubuntu ubuntu  55785 May 19 17:33 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 265000 May 20 05:50 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  22442 May 15 10:21 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1049 · 2026-05-20T06:24:14.182820+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent/ 2>/dev/null || echo \"agent directory not found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/agent/ 2>/dev/null || echo \"agent directory not found\""
  }
}
```

</details>

---


### Tool result

_source line 1050 · 2026-05-20T06:24:14.183060+00:00_

agent directory not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1051 · 2026-05-20T06:24:14.333872+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper content thoroughly",
  "subagent_type": "Explore",
  "prompt": "Read the full content of the paper at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/. The main file is main.tex which includes these files via \\input: abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix, and references.bib. \n\nRead ALL of these .tex files completely (use max_chars=0 or read without limits). I need the FULL content of every section. Report back the complete text of each file. This is for a paper review, so every detail matters. The files should be in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ directory. Try abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex, references.bib."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper content thoroughly",
    "subagent_type": "Explore",
    "prompt": "Read the full content of the paper at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/. The main file is main.tex which includes these files via \\input: abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix, and references.bib. \n\nRead ALL of these .tex files completely (use max_chars=0 or read without limits). I need the FULL content of every section. Report back the complete text of each file. This is for a paper review, so every detail matters. The files should be in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ directory. Try abstract.tex, introduction.tex, related_work.tex, method.tex, theory.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex, references.bib."
  }
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-20T06:24:14.686337+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-20T06:24:14.737171+00:00_

issues:
- id: R12-W1
  summary: 生态效度差距过大：full-replacement recursive chain 与真实 accumulation setting 存在结构性差异
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 12
  last_seen_round: 13
  mentions:
  - round: 12
    reviewers:
    - 1
    - 2
    note: R1-W1 和 R2-W2 均列为 Must-Fix。交叉回应中双方完全一致。
  - round: 13
    reviewers:
    - 1
    - 2
    note: R13-R1-W8 和 R13-R2-W4 再次提出。论文已在 Introduction §2 和 Discussion 中添加了 scope 声明和 accumulation 段落，Limitations 已提为第一条。但仍缺乏任何
      accumulation 实验验证 'upper bound' 假设。部分改善但核心问题未解决。
  action_items:
  - round: 12
    action: Abstract/Introduction 添加 full-replacement chain scope 限制声明；Discussion 增加 accumulation setting 段落；Limitations 提升为第一条
    assigned_to: paper_agent
    status: in_progress
  - round: 13
    action: 补充至少一个 toy-scale accumulation 实验（如 50% human + 50% synthetic 混合链）验证 upper bound 假设
    assigned_to: paper_agent
    status: open
  resolution: ''
  resolution_round: null
- id: R12-W2
  summary: Cross-strategy transfer 在 d1-d3 仅 45.9%（chance=33%），d1/d2 boundary inversion
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 12
  last_seen_round: 13
  mentions:
  - round: 12
    reviewers:
    - 1
    - 2
    note: R1 列为 Must-Fix，R2 交叉回应中升级认同。
  - round: 13
    reviewers:
    - 1
    - 2
    note: 论文已将 cross-strategy bottleneck 重新定位为 key empirical finding（§5.3），Abstract 并列了 d1-d3 45.9%，Claim 3 措辞已修改。R13-R1-Q5
      质疑 45.9% 是否足以支持 data auditing claim。两阶段 pipeline 仅恢复 11.5pp。改善明显但部署价值仍受限。
  action_items:
  - round: 12
    action: Abstract 并列 d1-d3 45.9%；cross-strategy bottleneck 重定位为 key empirical finding
    assigned_to: paper_agent
    status: in_progress
  resolution: ''
  resolution_round: null
- id: R12-W3
  summary: d0 recall >97% 膨胀 headline metrics，Abstract 中 d1-d3 数字被淹没
  category: writing
  severity: warning
  status: in_progress
  first_raised_round: 12
  last_seen_round: 13
  mentions:
  - round: 12
    reviewers:
    - 1
    - 2
    note: R1-W3 和 R
…[truncated 13523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-20T06:24:15.289801+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---


### Tool call

_source line 1055 · 2026-05-20T06:24:15.480239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/constraints.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-20T06:24:15.589610+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-20T06:24:15.640460+00:00_

&lt;persisted-output>
Output too large (60.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-director-79bccd15/8bf580e8-c42e-4d63-9a7a-90b8486e70c5/tool-results/toolu_014fmDYWAx4ALeaR7YW1AK74.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-133-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-134----
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-135-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-136-## External Review (Stanford Agentic Reviewer)
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-137-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md:138:外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-139-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-140----
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-141-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-142-## Overall Assessment
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_9.md-143-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/round_3.md-142-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recurs
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 350
}
```

</details>

---


### Tool result

_source line 1058 · 2026-05-20T06:24:15.640987+00:00_

1	_next_id: 5
2	constraints:
3	- id: C001
4	  added: 2026-05-15 02:50 UTC
5	  summary: 提交同系列实验（如 DCOL v5/v6）前必须先 read_registry 检查该系列所有历史实验的失败原因和参数约束，确认新 spec
6	    不重复已知错误
7	  scope: all
8	  reason: DCOL 系列 4 次失败，v4 重复了 v1 完全相同的错误（margin_lr=1e-3 导致 embedding collapse）。Worker
9	    写 spec 时未查阅同系列历史教训。
10	- id: C002
11	  added: 2026-05-15 02:50 UTC
12	  summary: 提交 DCOL 系列新实验前必须先 read_registry 检查同系列所有历史实验的失败原因和参数约束
13	  scope: all
14	  reason: DCOL v4 重复了 v1 完全相同的错误（margin_lr=1e-3 导致 embedding collapse），系列已连续 4 次失败。Worker
15	    未查阅历史教训直接提交。
16	- id: C003
17	  added: 2026-05-17 14:36 UTC
18	  summary: 'plan_023 理论分析质量门控: EDD 上界推导必须 mathematically rigorous (Fisher information
19	    / KL chain rule 级别)。如果只能做 informal argument，写入 Discussion 一段即可，不单开 Theory section。写入论文前必须
20	    post_to_reviewer 审查。'
21	  scope: all
22	  reason: 'Reviewer warning: 浅层理论反而招攻击，worse than no theory section。D038。'
23	  decision_id: D038
24	- id: C004
25	  added: 2026-05-17 17:30 UTC
26	  summary: wild_data_features 结果禁止解释为"AI生成内容占比"。C4 34% d1+ 是 OOD 假阳性率（C4 来自 2019 年，几乎无
27	    LLM 内容）。论文中必须 frame 为 FPR baseline / method limitation，不是正面 claim。
28	  scope: all
29	  reason: RF 训练数据的 d0 是模型 BOS-seeded 生成文本，不是真实人类文本。分类器从未见过 human web text 分布，在已知人类语料上的
30	    d1+ 预测是 distribution shift 导致的假阳性。正确叙事角色：Limitation + Future Work (需 human-text
31	    calibration)。
32	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 160
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-20T06:24:15.691632+00:00_

total 1124
drwxr-xr-x 3 ubuntu ubuntu   4096 May 20 06:02 .
drwxr-xr-x 4 ubuntu ubuntu   4096 May 15 05:24 ..
-rw-r--r-- 1 ubuntu ubuntu   1617 May 20 05:56 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu  11615 May 15 09:45 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  45186 May 15 09:45 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu  10448 May 19 09:09 atlas.tex
-rw-r--r-- 1 ubuntu ubuntu   8052 May 19 07:04 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu   1442 May 20 05:58 discussion.tex
drwxr-xr-x 2 ubuntu ubuntu   4096 May 19 09:10 drafts
lrwxrwxrwx 1 ubuntu ubuntu     94 May 15 16:32 figures -> /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper
-rw-r--r-- 1 ubuntu ubuntu   7419 May 20 05:58 generalization.tex
-rw-r--r-- 1 ubuntu ubuntu   5608 May 20 05:57 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  77659 May 20 06:03 main.aux
-rw-r--r-- 1 ubuntu ubuntu  25124 May 20 06:02 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   1302 May 20 06:02 main.blg
-rw-r--r-- 1 ubuntu ubuntu  20852 May 20 06:02 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu  23909 May 20 06:02 main.fls
-rw-r--r-- 1 ubuntu ubuntu  37755 May 20 06:03 main.log
-rw-r--r-- 1 ubuntu ubuntu   9710 May 20 06:03 main.out
-rw-r--r-- 1 ubuntu ubuntu 515534 May 20 06:03 main.pdf
-rw-r--r-- 1 ubuntu ubuntu    959 May 18 17:34 main.tex
-rw-r--r-- 1 ubuntu ubuntu 179080 May 18 14:50 main.txt
-rw-r--r-- 1 ubuntu ubuntu   7835 May 19 07:14 method.tex
-rw-r--r-- 1 ubuntu ubuntu  26662 May 19 07:10 references.bib
-rw-r--r-- 1 ubuntu ubuntu   4822 May 19 07:08 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  62313 May 20 06:01 section_appendix.tex
-rw-r--r-- 1 ubuntu ubuntu   2224 May 19 03:28 theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-20T06:24:15.742505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-20T06:24:15.743108+00:00_

1	_next_id: 51
2	decisions:
3	- id: D001
4	  date: 2026-05-14 14:03 UTC
5	  summary: MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase
6	  rationale: Pythia-1.4B 4-depth pipeline 验证核心假设：4-class acc 78.2% (>>40% threshold),
7	    d1v2 AUC 0.861 (>>0.6 threshold)。控制实验排除域混淆（过滤代码后 acc 提升至 81.6%）。Top 特征为 surprisal
8	    variance 和 perplexity percentiles，说明信号来自分布窄化而非内容差异。
9	  related_experiments:
10	  - exp_id: mvp_pipeline_pythia_002
11	    role: primary
12	    result: 4-class acc 78.2%, d1v2 AUC 0.861, content-type control 81.6%
13	  depends_on: []
14	- id: D002
15	  date: 2026-05-14 16:01 UTC
16	  summary: Dream 三档分析完成：6项结构性必修+framing重心从DCOL转向Atlas/EDD
17	  rationale: Dream dream_20260514T140607 full review 完成。三档(best=borderline accept
18	    3.0, median=Findings 3.0, worst=borderline Findings 2.5)一致指出6项结构性问题：(1)DCOL loss
19	    Eq.1缺repulsive term不可复现 (2)Atlas论文零图不可接受 (3)bibliography严重不足(3-10 refs,需25+) (4)d0
20	    confound膨胀headline metrics,需报d1-d5 acc (5)EDD threshold无sensitivity analysis (6)surprisal
21	    reference model未指定有circularity风险。三档均认为Atlas/EDD是primary contribution,DCOL incremental
22	    over CLOC——与我们的contingency plan方向一致。worst case下DCOL不显著(p=0.12),EDD=2,但任务formalization+Atlas仍可支撑Findings。关键风险：cross-model
23	    transfer在worst case降到33%。
24	  related_experiments:
25	  - exp_id: dream_20260514T140607
26	    role: dream_simulation
27	    result: best=3.0 median=3.0 worst=2.5
28	  depends_on: []
29	- id: D003
30	  date: 2026-05-14 19:45 UTC
31	  summary: 要求 baselines 统一使用 DeBERTa-v3-large，消除与 DCOL 的模型规模混淆变量
32	  rationale: Reviewer 发现 DCOL 用 DeBERTa-v3-large (435M) 而 CE/CORAL baselines 用 DeBERTa-v3-base
33	    (184M)，参数量差 2.4×，审稿人必问改进来源。修改 baseline 脚本支持 large 版本实验成本极低（模型已在服务器上），可彻底解耦方法贡献与模型容量。
34	  related_experiments:
35	  - exp_id: dcol_deberta_001
36	    role: target
37	    result: pending
38	  depends_on: []
39	- id: D004
40	  date: 2026-05-14 20:34 UTC
41	  summary: 跨策略泛化 claim 从 "strategy-agnostic" 降级为 "strategy-dependent signal attenuation"
42	  ratio
…[truncated 2701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-20T06:24:18.002643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-20T06:24:18.003106+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-20T06:24:18.053598+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 3 -name \"config.yaml\" -o -name \"settings.yaml\" -o -name \"project.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 3 -name \"config.yaml\" -o -name \"settings.yaml\" -o -name \"project.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-20T06:24:18.206238+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-20T06:24:18.307395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-20T06:24:18.307788+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-20T06:24:18.609301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-20T06:24:18.609669+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-20T06:24:18.710498+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml",
  "output_mode": "content",
  "context": "10",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/registry.yaml",
    "output_mode": "content",
    "context": "10",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-20T06:24:18.761189+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-20T06:24:18.811797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-20T06:24:18.812181+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-20T06:24:19.214010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-20T06:24:19.214463+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-20T06:24:19.465656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-20T06:24:19.466387+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-20T06:24:19.667406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-20T06:24:19.667765+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-20T06:24:20.069951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-20T06:24:20.070374+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-20T06:24:20.372005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | grep -E \"(config|settings|project|init)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | grep -E \"(config|settings|project|init)\" | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-20T06:24:20.373118+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/"
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-20T06:24:20.423626+00:00_

total 44
drwxrwxr-x  9 ubuntu ubuntu 4096 May 14 03:43 .
drwxr-x--- 16 ubuntu ubuntu 4096 May 20 05:41 ..
drwxr-xr-x  3 ubuntu ubuntu 4096 May 14 03:43 .claude
-rw-r--r--  1 ubuntu ubuntu  355 May 20 06:23 AGENTS.md
drwxrwxr-x  5 ubuntu ubuntu 4096 May 20 05:52 config
drwxr-xr-x  4 ubuntu ubuntu 4096 May 20 06:23 global
drwxr-xr-x  2 ubuntu ubuntu 4096 May 14 09:35 idea_generator
drwxrwxr-x  7 ubuntu ubuntu 4096 May 14 09:51 projects
drwxr-xr-x  3 ubuntu ubuntu 4096 May 13 11:23 skills
drwxr-xr-x  2 ubuntu ubuntu 4096 May 20 06:24 state
-rw-r--r--  1 ubuntu ubuntu   13 May 13 11:23 workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-20T06:24:20.424155+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_6683f1795256b05035b138360f193731.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_70ebd22373d3a7c470648796de71dbbf.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_a1b70f6b4ad915d47dbcc2043d3e9229.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_review_reviewer_1.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_09731295942d3269e0517509703bed15.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_f265de7a9796688b878083fef59f9d4c.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_4117895cca10a53e32a904aa47517ffe.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_paper_agent.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_dc55567f3c41939c4158a0a3c8e6e960.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_worker_23395dfac19840f2566efcf2b6c04201.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-20T06:24:20.474726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-20T06:24:20.475108+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-20T06:24:20.826706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-20T06:24:20.827264+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-20T06:24:20.927990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-20T06:24:20.928338+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-20T06:24:21.279803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-20T06:24:21.280200+00:00_

&lt;tool_use_error>InputValidationError: Read failed due to the following issue:
An unexpected parameter `max_chars` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-20T06:24:21.883076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-20T06:24:22.485836+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0513-2
5	  my_token: 88df7b82fe89666837a7c394be40395b99611bbf40aa913dc676879bf0a5cc0e
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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-20T06:24:22.539185+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -name \".clauderc\" -o -name \"config.yaml\" -o -name \"*.local.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 2 -name \".clauderc\" -o -name \"config.yaml\" -o -name \"*.local.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-20T06:24:22.840999+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-20T06:24:22.893070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/ 2>/dev/null || echo \"No .claude directory\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/ 2>/dev/null || echo \"No .claude directory\""
  }
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-20T06:24:22.893456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-20T06:24:22.943922+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-20T06:24:22.944300+00:00_

total 28
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 09:51 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 20 05:50 ..
-rw-r--r--  1 ubuntu ubuntu 14179 May 20 06:23 CLAUDE.md
drwxr-xr-x 44 ubuntu ubuntu  4096 May 20 05:31 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-20T06:24:22.994807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-20T06:24:22.995282+00:00_

1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification, constructing a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement recursive chains at the 1--1.5B scale.
4	A Random Forest over statistical features dominated by the perplexity tail family achieves d1--d3 balanced accuracy of 59--82\% (four-class: 69--86\%) across nine model--strategy cells; convergence of RF, XGBoost, and LightGBM confirms that discriminative signal resides in feature design, not classifier choice.
5	Cross-model transfer reaches 66.4\%, cross-domain arXiv 74.1\%, and cross-strategy transfer 59.1\%; the gap reveals that decoding strategies induce structurally distinct degradation trajectories, formalized via the \emph{Effective Discriminable Depth} (EDD) metric ($\mathrm{EDD}_{0.70}{=}4$ for all three families); preliminary cross-scale experiments at 14B confirm signal persistence across all three strategies (mean 50.8\%, $2{\times}$ chance).
6	Perturbation-based and membership inference baselines (29--33\%) fall far below our pipeline; cross-perplexity features (Binoculars) converge to matching performance (78.1\% vs.\ 78.4\%), and merging both feature sets yields 82.6\%, decomposing the depth signal into perplexity displacement, distributional shape, and cross-model divergence channels.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-20T06:24:23.698664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-20T06:24:23.699122+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We study this question under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions; the full-replacement setting provides an upper bound on depth signal strength, and we discuss implications for accumulation settings in \S\ref{sec:discussion}.
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
11	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
12	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
13	No exi
…[truncated 3698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-20T06:24:23.850119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-20T06:24:23.900868+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, data scaling under constraint \cite{muennighoff2023scaling}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026} are active areas.
8	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectg
…[truncated 2906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-20T06:24:24.102197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-20T06:24:24.153082+00:00_

1	## 当前项目
2	当前绑定项目：**recursive_gen_depth_est**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("recursive_gen_depth_est")` 或 `load_project_config("recursive_gen_depth_est", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## 用户自定义规则（必须遵守）
11	### 审稿规则
12	
13	- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
14	- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.
15	
16	> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
17	
18	## Worker 操作规范
19	
20	### ssh-env-setup
21	
22	# 远程服务器环境搭建规范
23	
24	## 核心原则
25	
26	**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。
27	
28	**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。
29	
30	**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**
31	
32	## Phase 1: 环境探测（用 ssh_read_only）
33	
34	连接到服务器后，第一步永远是收集信息，不要直接装东西：
35	
36	```bash
37	# 1. Python 环境
38	which python3 && python3 --version
39	pip3 --version 2>/dev/null || echo "NO_PIP"
40	
41	# 2. CUDA 环境
42	nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || ec
…[truncated 8941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-20T06:24:26.161909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global -type f -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global -type f -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-20T06:24:26.213086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-20T06:24:26.264531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/state/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/state/"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-20T06:24:26.265126+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-20T06:24:26.265498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-20T06:24:26.265728+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/pending_queue/178a3f157153.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/feat_ablation_v1_RUNNING_20260515T193532.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_scale_llama3_base_001_PREPARING_20260516T130123.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_scale_qwen7b_001_QUEUED_20260516T045352.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_model_reverse_chain_001_RUNNING_20260516T142420.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_scale_qwen7b_001_RUNNING_20260516T045401.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/feat_ablation_v1_RUNNING_20260515T193522.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_model_gpt2xl_001_RUNNING_20260514T182850.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_scale_qwen7b_001_PENDING_20260516T045349.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_model_gpt2xl_001_RUNNING_20260514T182853.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_model_reverse_chain_001_QUEUED_20260516T142415.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/feat_ablation_v1_DONE_20260515T193535.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_model_olmo_002_RUNNING_20260514T181922.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/cross_scale_qwen7b_001_RUNNING_20260516T114826.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/checkpoints/olmo_temp09_001_RUNNING_20260514T225720.json
/home/ubuntu/.agent-ml-research-
…[truncated 203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-20T06:24:26.317072+00:00_

total 12
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 06:24 .
drwxrwxr-x 9 ubuntu ubuntu 4096 May 14 03:43 ..
-rw-r--r-- 1 ubuntu ubuntu 1650 May 20 06:24 pool_state_last.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-20T06:24:26.518240+00:00_

1	\subsection{Theoretical Grounding}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed by its dominance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--80\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
15	Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-20T06:24:26.518744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-20T06:24:26.770080+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: MAE\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}).}
22	\label{tab:main_matrix}
23	\resizebox
…[truncated 8856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-20T06:24:26.770640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-20T06:24:26.821153+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares ordinal depth estimation methods across all 9 atlas cells.
10	RF, XGBoost, and LightGBM on the same 19 features converge within 0.4\,pp per cell (a feature-determined ceiling); on Pythia nucleus, CORAL \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match RF within 0.6\,pp ($p>0.05$).
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA) trained end-to-end on raw text underperforms RF by 16--32\,pp across three cells (Table~\ref{tab:baselines}); the gap is largest on GPT-2~XL temp09 (53.1\% vs.\ 85.9\%), where RF signal is strongest.
14	Depth-2 recall collapses to 8.4\% under DeBERTa, indicating that intermediate-depth distributional shifts---captured by perplexity tail statistics---are invisible to token-level neural encoders without explicit feature engineering.
15	RoBERTa-DCOL (ordinal contrastive; 64.5\%) narrows the gap but remains 14\,pp below RF.
16	
17	\paragraph{Binary detectors and membership inference.}
18	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); CORAL calibration does not close the gap (d1--d3: 40.4\% vs.\ RF 71.6\%).
19	Binoculars \cite{binoculars2024}, calibrated with an 11-feature RF on per-token cross-perplexity scores, matches our pipeline within 0.3\,pp (78.1\% vs.\ 78.4\%, $p{>}0.05$); 6 of 11 Binoculars features overlap with 6 of our 19 (both capture mean-level perplexity displacement), and merging all 30 features yields 82.6\% (+4.2\,pp; Appendix~\ref{app:feature_ablation_bino}).
20	
21	\paragraph{
…[truncated 5787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-20T06:24:27.878679+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/ 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-20T06:24:28.079922+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-15 10:39:08 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-15 16:03:49 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 12:01:54 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 17:13:34 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 19:27:28 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 20:03:20 INFO     [EXTERN] [external_review] reset state for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-16 20:03:21 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-17 06:17:59 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-18 14:07:05 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-19 02:55:38 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log:2026-05-19 06:32:00 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth
…[truncated 187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-20T06:24:28.130676+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2 --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2 --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-20T06:24:28.232296+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1126 · 2026-05-20T06:24:28.834968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-20T06:24:28.935729+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	This paper formalizes recursive generation depth estimation as ordinal classification under controlled full-replacement chains.
5	The perplexity tail feature family dominates depth discrimination across all nine cells, with $\mathrm{EDD}_{0.70}{=}4$ for all three families; cross-model transfer reaches 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, while perturbation-based and membership-inference detectors achieve only 30--35\%.
6	Under accumulation (GPT-2~XL, nucleus), accuracy drops to ${\sim}$69--70\% ($-$15\,pp, $2.8{\times}$ chance); at 14B (mean 50.8\% across three strategies, $2{\times}$ chance), $\mathrm{EDD}_{0.70}{=}0$ but d1--d3 discrimination persists with strategy-specific AUC patterns (Appendix~\ref{app:cross_scale_full}).
7	
8	\paragraph{Multi-channel depth encoding.}
9	Feature ablation (Appendix~\ref{app:feature_ablation_bino}) decomposes the depth signal into perplexity displacement (6 core features, 75.9\%, 97\% of pipeline accuracy), distributional shape (+2.5\,pp), and cross-model divergence (+4.2\,pp, merged 82.6\%); the gain is strategy-dependent (nucleus/temperature +4.7\,pp vs.\ top-k +3.2\,pp).
10	That two independent pipelines converge to within 0.3\,pp validates depth as a genuine distributional property; at 14B, merging still yields +3.6--3.7\,pp despite a 10$\times$ observer--generator scale gap (Appendix~\ref{app:feature_ablation_bino}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-20T06:24:28.936167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-20T06:24:28.986665+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	All experiments use full-replacement recursive chains, where each depth fully replaces the prior training corpus. Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions across iterations \cite{gerstgrasser2024_accumulate}. Under accumulation, depth signal should attenuate because each generation retains human-originated distributional properties. Our results therefore represent an upper bound on feature separability; extending the framework to accumulation settings, where depth becomes a continuous mixing parameter, is a priority for future work.
6	Segment-level estimation in mixed-depth documents remains open (Appendix~\ref{app:mixed_depth}), as our framework assumes uniform depth per passage.
7	
8	\paragraph{Controlled experimental setting.}
9	The primary benchmark uses Wikipedia seed text with controlled LoRA fine-tuning (1--1.5B models), a design that isolates the depth variable but diverges from wild contamination.
10	Domain bias controls confirm depth as the dominant factor: LOGO accuracy (72.1\%) matches standard CV (72.0\%), seed-group prediction is at chance (10.2\%; Appendix~\ref{app:domain_bias}).
11	Cross-scale experiments (7--14B, \S\ref{sec:gen:crossscale}) show signal that attenuates with scale; at 14B, d0/d1 separability nearly vanishes ($\mathrm{EDD}_{0.70}{=}0$) while d1--d3 discrimination persists; this constitutes a boundary condition for the current feature set (confounded by five factors; Appendix~\ref{app:cross_scale_confounds}).
12	
13	\paragraph{Cross-strategy deployment constraint.}
14	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
15	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random 
…[truncated 6238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-20T06:24:29.188116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-20T06:24:29.440099+00:00_

1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\t
…[truncated 63837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-20T06:24:29.842103+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -name \"projects.yaml\" -o -name \"projects.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2 -name \"projects.yaml\" -o -name \"projects.json\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-20T06:24:30.295058+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-20T06:24:30.295520+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/ 2>/dev/null"
  }
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-20T06:24:30.346153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/state/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/state/"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-20T06:24:30.396927+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-20T06:24:30.397270+00:00_

total 12
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 06:24 .
drwxrwxr-x 9 ubuntu ubuntu 4096 May 14 03:43 ..
-rw-r--r-- 1 ubuntu ubuntu 1650 May 20 06:24 pool_state_last.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-20T06:24:31.755708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool call

_source line 1139 · 2026-05-20T06:24:31.806589+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -maxdepth 3 -name \"*projects*\" -type f 2>/dev/null | grep -E \"\\.(yaml|json)$\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -maxdepth 3 -name \"*projects*\" -type f 2>/dev/null | grep -E \"\\.(yaml|json)$\" | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1140 · 2026-05-20T06:24:32.109049+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-20T06:24:32.109476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-20T06:24:32.160198+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},

…[truncated 27098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-20T06:24:32.210839+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-20T06:24:33.717446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-20T06:24:33.868455+00:00_

1	baseline: null
2	experiments:
3	  cross_model_olmo_002:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T18:19:10.507Z'
7	    updated_at: '2026-05-14T18:19:32.370Z'
8	    spec:
9	      command: bash scripts/run_pipeline_olmo.sh
10	      server: gpu-6000pro-2
11	      data_path: data/olmo/
12	      data_count: 20000
13	      model_name: olmo-1b-hf
14	      seed: 42
15	      checkpoint_path: checkpoints/olmo/
16	      log_path: /root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_olmo_002.log
17	    conclusion: success
18	    metrics:
19	      rf_4class_acc: 0.7877
20	      rf_4class_acc_ci:
21	      - 0.7758
22	      - 0.8003
23	      lr_4class_acc: 0.7508
24	      rf_auc_0v1: 0.9834
25	      rf_auc_0v2: 0.9949
26	      rf_auc_0v3: 0.9989
27	      rf_auc_1v2: 0.8673
28	      rf_auc_1v3: 0.9806
29	      rf_auc_2v3: 0.8124
30	      train_loss_depth0: 2.269
31	      train_loss_depth1: 1.65
32	      train_loss_depth2: 1.226
33	      top_features:
34	      - p90_ppl
35	      - var_surprisal
36	      - p75_ppl
37	      - mean_surprisal
38	      - type_token_ratio
39	    completed_at: '2026-05-14T18:19:32.370Z'
40	  cross_model_gpt2xl_001:
41	    status: DONE
42	    retry_count: 0
43	    created_at: '2026-05-14T18:28:37.468Z'
44	    updated_at: '2026-05-14T18:29:09.370Z'
45	    spec:
46	      command: scripts/run_pipeline_gpt2xl.sh + manual eval (filter_code, extract_features,
47	        train_classifier)
48	      server: gpu-6000pro-2
49	      data_path: data/gpt2xl/
50	      data_count: 20000
51	      model_name: gpt2-xl
52	      seed: 42
53	      checkpoint_source: checkpoints/gpt2xl/
54	      checkpoint_path: checkpoints/gpt2xl/
55	      log_path: results/gpt2xl/
56	    conclusion: success
57	    metrics:
58	      four_class_rf_acc: 0.8333
59	      four_class_rf_ci:
60	      - 0.8227
61	      - 0.8445
62	      four_class_lr_acc: 0.8127
63	      four_class_lr_ci:
64	      - 0.8013
65	      - 0.8257
66	      pairwise_auc_rf:
67	        d0v1: 0.994
…[truncated 3433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-20T06:24:33.919099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml | tail -150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/registry.yaml | tail -150"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-20T06:24:33.969763+00:00_

      model_name: gpt2-xl
      seed: 42
      checkpoint_source: checkpoints/gpt2xl/
      checkpoint_path: checkpoints/gpt2xl/
      log_path: results/gpt2xl/
    conclusion: success
    metrics:
      four_class_rf_acc: 0.8333
      four_class_rf_ci:
      - 0.8227
      - 0.8445
      four_class_lr_acc: 0.8127
      four_class_lr_ci:
      - 0.8013
      - 0.8257
      pairwise_auc_rf:
        d0v1: 0.9941
        d0v2: 0.9965
        d0v3: 0.9988
        d1v2: 0.9131
        d1v3: 0.9857
        d2v3: 0.8829
      pairwise_auc_lr:
        d0v1: 0.9808
        d0v2: 0.9941
        d0v3: 0.9937
        d1v2: 0.8469
        d1v3: 0.9686
        d2v3: 0.8651
      three_class_rf_acc: 0.7927
      three_class_rf_ci:
      - 0.7783
      - 0.806
      three_class_auc:
        d1v2: 0.9109
        d1v3: 0.989
        d2v3: 0.8885
      top_features:
        p90_ppl: 0.2082
        var_surprisal: 0.2079
        p75_ppl: 0.1034
        mean_surprisal: 0.0821
        mean_ppl: 0.0645
      code_contamination_broad:
        depth_0: 0.005
        depth_1: 0.005
        depth_2: 0.013
        depth_3: 0.007
      code_contamination_narrow:
        depth_0: 0.004
        depth_1: 0.005
        depth_2: 0.009
        depth_3: 0.037
    notes: 'GPT-2 XL (1.5B) significantly outperforms both Pythia-1.4B and OLMo-1B
      baselines across all metrics. 4-class acc: GPT2XL 83.3% vs Pythia 78.2% vs OLMo
      78.8% (+5.1/+4.5pp). AUC d1v2: 0.9131 vs 0.8607 vs 0.8673 (+0.052/+0.046). AUC
      d2v3: 0.8829 vs 0.8005 vs 0.8124 (+0.082/+0.071). Code contamination very low
      (broad: 0.5-1.3%, narrow: 0.4-3.7%). Top features same pattern: p90_ppl and
      var_surprisal dominate. The stronger signal suggests GPT-2 XL''s recursive generations
      diverge more from the reference model (Pythia-1.4B surprisal), making depth
      discrimination easier.'
    completed_at: '2026-05-14T18:29:09.370Z'
  olmo_temp09_001:
    status: DONE
    retry_count: 0
    created_at: '2026-05-14T22:5
…[truncated 3697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-20T06:24:36.330488+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "tail -100 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | grep -A 3 \"external_review\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "tail -100 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | grep -A 3 \"external_review\" | head -30"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-20T06:24:36.633621+00:00_

2026-05-20 06:23:02 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
2026-05-20 06:23:02 INFO     [HOOKS] [review] kick-off message length=346 has_ext=False
2026-05-20 06:23:02 INFO     [SESSION] [feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director] QUEUED | project=recursive_gen_depth_est | depth=0 | text='系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: /home/ubuntu/.'
2026-05-20 06:23:03 INFO     [HOOKS] [review] Group C=oc_db3bd143165620ee6950e6ef0826eec8 project=recursive_gen_depth_est venue=EMNLP 2026 mode=fresh round=11

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-20T06:24:36.634143+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -path \"*/recursive_gen_depth_est/*\" -name \"project*.yaml\" -o -path \"*/recursive_gen_depth_est/*\" -name \"config*.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -path \"*/recursive_gen_depth_est/*\" -name \"project*.yaml\" -o -path \"*/recursive_gen_depth_est/*\" -name \"config*.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-20T06:24:36.985861+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-20T06:24:38.592710+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -type f -name \"*metadata*\" 2>/dev/null | grep recursive_gen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -type f -name \"*metadata*\" 2>/dev/null | grep recursive_gen"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-20T06:24:38.944242+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_ops_fix_gpt2xl_json_metadata_20260515T225200.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_ops_fix_gpt2xl_json_metadata_20260515T225200_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ops_fix_gpt2xl_json_metadata_20260515T225200.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ops_fix_gpt2xl_json_metadata_20260515T225200.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-20T06:24:38.995026+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B 5 -A 5 \"external_review_enabled=False\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B 5 -A 5 \"external_review_enabled=False\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/logs/system.log | head -40"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-20T06:24:39.045896+00:00_

2026-05-15 10:39:07 INFO     [MANAGE] [approval:apr_20260515T103851_pcew] approved by feishu:ou_ec5e2f7a132fba5220486d5a53c3c45a
2026-05-15 10:39:07 INFO     [HOOKS] [review] reusing existing Group C: oc_db3bd143165620ee6950e6ef0826eec8
2026-05-15 10:39:07 INFO     [FEISHU] Unified approval action: approve approval_id=apr_20260515T103851_pcew by=feishu:ou_ec5e2f7a132fba5220486d5a53c3c45a
2026-05-15 10:39:07 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director
2026-05-15 10:39:07 INFO     [HOOKS] [review] reset all review sessions for chat_id=oc_db3bd143165620ee6950e6ef0826eec8
2026-05-15 10:39:08 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
2026-05-15 10:39:08 INFO     [HOOKS] [review] kick-off message length=293 has_ext=False
2026-05-15 10:39:08 INFO     [SESSION] [feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director] QUEUED | project=recursive_gen_depth_est | depth=0 | text='系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: recursive_gen_depth_est\n- 论文路径: projects/recur'
2026-05-15 10:39:09 INFO     [HOOKS] [review] Group C=oc_db3bd143165620ee6950e6ef0826eec8 project=recursive_gen_depth_est venue=EMNLP 2026 mode=fresh round=1
2026-05-15 10:39:10 INFO     [SESSION] [session_server] wrote /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/mcp_config_review_director.json
2026-05-15 10:39:10 INFO     [SESSION] [session_server] pool account selected: account-3 (/home/ubuntu/.claude-account-3)
--
2026-05-15 16:03:49 INFO     [HOOKS] [review] reusing existing Group C: oc_db3bd143165620ee6950e6ef0826eec8
2026-05-15 16:03:49 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director
2026-05-15 16:03:49 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1
2026-05-15 16:03:49 INFO     [SESSION] [session_server] invalidated sessio
…[truncated 3167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-20T06:24:41.154901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -maxdepth 2 -type f \\( -name \"projects.yaml\" -o -name \"projects.json\" -o -name \".projects.yaml\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -maxdepth 2 -type f \\( -name \"projects.yaml\" -o -name \"projects.json\" -o -name \".projects.yaml\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-20T06:24:41.607351+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-20T06:24:41.607839+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-20T06:24:41.660052+00:00_

-rw------- 1 ubuntu ubuntu 27012 May 20 06:23 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-20T06:24:43.015850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/global/approvals.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-20T06:24:43.016419+00:00_

1	approvals:
2	  apr_20260515T052615_yo5c:
3	    approval_id: apr_20260515T052615_yo5c
4	    context:
5	      file_scope: 0
6	      task_type: experiment:depth_extension_binary_pairwise_001
7	    created_at: '2026-05-15T05:26:15.131Z'
8	    feishu_card_message_id: om_x100b6f5ea953989cc450e6ed97925de
9	    project: recursive_gen_depth_est
10	    reject_reason: 审批超时（24h）
11	    resolved_at: '2026-05-16T05:26:32.125737+00:00'
12	    resolved_by: null
13	    risk_score:
14	      auto_approve: false
15	      dimensions:
16	      - label: 任务类型
17	        level: medium
18	        name: task_type
19	        value: experiment:depth_extension_binary_pairwise_001
20	      - label: 涉及文件数
21	        level: low
22	        name: file_scope
23	        value: 0
24	      overall: medium
25	      reason: 需要人工审批。维度：任务类型=experiment:depth_extension_binary_pairwise_001(medium),
26	        涉及文件数=0(low)
27	    status: expired
28	    subject_id: worker_experiment_depth_extension_binary_pairwise_001_20260515T052615
29	    type: worker
30	  apr_20260515T103851_pcew:
31	    approval_id: apr_20260515T103851_pcew
32	    context:
33	      chat_id: oc_5d269fdb74af3f4ab8d78b82a993f5cf
34	      deadline: ''
35	      has_prior_review: true
36	      mode_reason: 距上轮审稿有大量修改（z-score claim 整段重写、新增粒度消融段落、多处数字修正），fresh review 能更好评估整体论文质量。
37	      paper_path: projects/recursive_gen_depth_est/paper/main.tex
38	      paper_title: EMNLP 2026
39	      reason: Round 1 Reviewer 所有 CRITICAL/WARNING 修复完成：z-score LR claim 修正(D021)、DeepSeek
40	        40.0%、LoRA targets 三模型分列、粒度消融结果加入正文、EDD binary classifier 方法学澄清、confusion
41	        matrix caption 同步、atlas "comparably" 措辞修正。编译通过，主文 8 页。
42	      recommended_review_mode: fresh
43	      review_chat_id: oc_db3bd143165620ee6950e6ef0826eec8
44	      review_mode: fresh
45	      review_round: 0
46	      supplementary_paths: ''
47	      track: main conference
48	      venue: EMNLP 2026
49	    created_at: '2026-05-15T10:38:51.676Z'
50	    feishu_card_message_id: om_x100b6f5
…[truncated 6358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-20T06:24:45.601121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 3 -name \"*config*\" -o -name \"*metadata*\" -o -name \"*settings*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -maxdepth 3 -name \"*config*\" -o -name \"*metadata*\" -o -name \"*settings*\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-20T06:24:45.896833+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_ops_fix_gpt2xl_json_metadata_20260515T225200.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/workers/worker_ops_fix_gpt2xl_json_metadata_20260515T225200_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ops_fix_gpt2xl_json_metadata_20260515T225200.lock
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/logs/chats/worker_ops_fix_gpt2xl_json_metadata_20260515T225200.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 295
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-20T06:24:45.948276+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/agent-ml-research --include=\"*.py\" --include=\"*.yaml\" 2>/dev/null | grep -v \".pyc\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/agent-ml-research --include=\"*.py\" --include=\"*.yaml\" 2>/dev/null | grep -v \".pyc\" | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-20T06:24:47.155191+00:00_

/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:  2. fresh mode wipes `external_review_state.json` so prior-round pending /
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:# Fix 2: external_review.reset_state
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        from core.tools.external_review import _save_state, reset_state, _load_state
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        state_file = _paths.project_dir(project) / "external_review_state.json"
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        from core.tools.external_review import reset_state
/home/ubuntu/agent-ml-research/tests/test_paper_review_handoff.py:            "core.tools.external_review.reset_state",
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        # External review (paperreview.ai) — too slow for Dream.
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        assert "request_external_review" not in tools
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        assert "get_external_review_status" not in tools
/home/ubuntu/agent-ml-research/tests/test_dream_review_simple.py:        assert "request_external_review" in prompt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-20T06:24:49.967043+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -name \"external_review*.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est -name \"external_review*.json\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-20T06:24:50.268960+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-20T06:24:50.269482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review.paperreview_ai.enabled\\|external_review:\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review.paperreview_ai.enabled\\|external_review:\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -15"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-20T06:24:50.570990+00:00_

/home/ubuntu/agent-ml-research/core/tools/project_config.py:    Reads ``external_review.paperreview_ai.enabled`` from project config.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-20T06:24:52.027528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-20T06:24:52.330069+00:00_

1	"""Project configuration loader — reads config/projects/{name}.yaml.
2	
3	Each project config declares server, codebase paths, evaluation metrics,
4	and W&B settings. The orchestrator injects this into the system prompt
5	and MCP tool defaults at session startup.
6	"""
7	
8	from __future__ import annotations
9	
10	from pathlib import Path
11	
12	import yaml
13	
14	from core.tools.result import ToolResult
15	
16	# ---------------------------------------------------------------------------
17	# Paths
18	# ---------------------------------------------------------------------------
19	
20	from core import paths as _paths
21	
22	
23	# ---------------------------------------------------------------------------
24	# Path expansion — resolve ~ in config values so non-interactive shells work
25	# ---------------------------------------------------------------------------
26	
27	# Top-level keys whose string values may contain ~
28	_PATH_KEYS = {"root", "project_path", "log_dir"}
29	
30	
31	def _expand_paths(config: dict) -> None:
32	    """In-place expand ~ in known path fields using the remote account's home.
33	
34	    These paths refer to remote servers, NOT the local machine.
35	    ``~`` is resolved to ``/home/{account}`` (standard Linux layout)
36	    using the account from ``execution.servers[0].account`` or
37	    ``execution.account``.
38	    """
39	    # Determine remote account for ~ expansion
40	    exec_cfg = config.get("execution", {})
41	    account = exec_cfg.get("account", "")
42	    if not account:
43	        servers = exec_cfg.get("servers")
44	        if isinstance(servers, list) and servers:
45	            first = servers[0]
46	            if isinstance(first, dict):
47	                account = first.get("account", "")
48	    # Fallback: extract account from resources.yaml server host (user@ip)
49	    if not account:
50	        server_name = exec_cfg.get("server", "")
51	        if server_name:
52	            try:
53	                resources_path = _
…[truncated 42481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-20T06:24:54.993145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -path \"*/config/projects*\" -type d 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -path \"*/config/projects*\" -type d 2>/dev/null"
  }
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-20T06:24:55.195110+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/agent-ml-research/config/projects/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/agent-ml-research/config/projects/ 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-20T06:24:55.296076+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-20T06:24:55.396961+00:00_

/home/ubuntu/agent-ml-research/workspace/config/projects
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-20T06:24:56.756244+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-20T06:24:56.907328+00:00_

total 20
drwxrwxr-x 2 ubuntu ubuntu 4096 May 14 17:07 .
drwxrwxr-x 5 ubuntu ubuntu 4096 May 20 05:52 ..
-rw-r--r-- 1 ubuntu ubuntu  636 May 14 09:34 distill_kv_rag_cache.yaml
-rw-r--r-- 1 ubuntu ubuntu  506 May 14 09:45 error_type_pref_optim.yaml
-rw-r--r-- 1 ubuntu ubuntu  940 May 20 06:23 recursive_gen_depth_est.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-20T06:24:56.907776+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-20T06:24:56.958392+00:00_

total 12
drwxrwxr-x 2 ubuntu ubuntu 4096 May  9 09:00 .
drwxrwxr-x 3 ubuntu ubuntu 4096 May 13 11:22 ..
-rw-rw-r-- 1 ubuntu ubuntu  337 May  9 09:00 LLM-Calibration.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-20T06:24:58.866513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-20T06:24:58.967370+00:00_

1	execution:
2	  project_path: /root/autodl-tmp/recursive_gen_depth_est
3	  servers:
4	  - gpu_ids:
5	    - 0
6	    - 1
7	    server: gpu-6000pro-2
8	  - gpu_ids:
9	    - 0
10	    - 1
11	    server: westd-48862
12	feishu:
13	  chat_id: oc_5d269fdb74af3f4ab8d78b82a993f5cf
14	  operational_chat_id: oc_5434474971bcc3bc52c4774796ba7f3d
15	  review_mode: fresh
16	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
17	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf
18	  review_round: 11
19	  review_supplementary_paths: ''
20	  submission_chat_id: oc_db3bd143165620ee6950e6ef0826eec8
21	project:
22	  created_at: '2026-05-14T09:51:34.204Z'
23	  description: How Deep Is Your Data? Estimating Recursive Generation Depth for Synthetic
24	    Text Quality Scoring
25	  name: recursive_gen_depth_est
26	  phase: research
27	  source_idea_id: idea_008
28	venue: emnlp-2026
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-20T06:25:01.127924+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"external_review:\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"external_review:\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-20T06:25:01.338111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"paperreview_ai\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"paperreview_ai\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1184 · 2026-05-20T06:25:01.553498+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 425
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-20T06:25:01.906069+00:00_

/home/ubuntu/agent-ml-research/core/tools/project_config.py:462:    Reads ``external_review.paperreview_ai.enabled`` from project config.
/home/ubuntu/agent-ml-research/core/tools/project_config.py:469:    return bool(ext.get("paperreview_ai", {}).get("enabled", False))
/home/ubuntu/agent-ml-research/core/api/routers/projects.py:112:        if "paperreview_ai" in body["external_review"]:
/home/ubuntu/agent-ml-research/core/api/routers/projects.py:113:            ext.setdefault("paperreview_ai", {}).update(body["external_review"]["paperreview_ai"])

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 567
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-20T06:25:03.161531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/api/routers/projects.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/api/routers/projects.py",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-20T06:25:03.212241+00:00_

1	"""Projects API — workspace project listing + architecture docs."""
2	
3	from pathlib import Path
4	from typing import List
5	
6	import yaml
7	from fastapi import APIRouter, HTTPException
8	from fastapi.responses import PlainTextResponse
9	
10	from core import paths as _paths
11	from core.api.schemas import CreateProjectIn, ProjectOut
12	
13	router = APIRouter(tags=["projects"])
14	
15	
16	@router.get("/projects", response_model=List[ProjectOut])
17	def list_projects():
18	    from core.tools.workspace import list_workspace_projects
19	
20	    result = list_workspace_projects()
21	    if not result.success:
22	        raise HTTPException(500, detail=result.error)
23	
24	    return [ProjectOut(**p) for p in result.data.get("projects", [])]
25	
26	
27	@router.post("/projects", response_model=ProjectOut, status_code=201)
28	def create_project(body: CreateProjectIn):
29	    from core.tools.workspace import create_project as _create, list_workspace_projects
30	
31	    result = _create(name=body.name, description=body.description, repo=body.repo)
32	    if not result.success:
33	        raise HTTPException(400, detail=result.error)
34	
35	    ws_result = list_workspace_projects()
36	    for p in ws_result.data.get("projects", []):
37	        if p["name"] == body.name:
38	            return ProjectOut(**p)
39	
40	    return ProjectOut(name=body.name, description=body.description or body.name)
41	
42	
43	@router.delete("/projects/{name}", status_code=200)
44	def delete_project_endpoint(name: str, remove_files: bool = False):
45	    from core.tools.workspace import delete_project as _delete
46	
47	    result = _delete(name=name, remove_files=remove_files)
48	    if not result.success:
49	        raise HTTPException(400, detail=result.error)
50	    return result.data
51	
52	
53	@router.get("/projects/{name}", response_model=ProjectOut)
54	def get_project(name: str):
55	    from core.tools.workspace import list_workspace_projects
56	
57	    result = list_workspace_projects()
…[truncated 3809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1188 · 2026-05-20T06:25:09.287557+00:00_

Good! Now I have a full picture. The configuration shows that the `external_review` section is not present in the current project config YAML file. Let me verify this is indeed the case and provide the final report:

Based on my comprehensive search of the project configuration files and system logs, here are my findings:

## Project Configuration File Location
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/config/projects/recursive_gen_depth_est.yaml`

## External Review Configuration Status

**Current Status:** The `external_review` section is **NOT configured** in the project configuration file.

## Exact Configuration Content

The project configuration file contains the following sections:
- `execution` (servers and project paths)
- `feishu` (Feishu chat group IDs and review settings)
- `project` (project metadata)
- `venue` (submission venue)

**The `external_review` section is absent entirely.**

## Evidence from System Logs

Multiple system log entries confirm that external review is disabled:

```
2026-05-20 06:23:02 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
2026-05-15 10:39:08 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
2026-05-16 12:01:54 INFO     [HOOKS] [review] external_review_enabled=False for project=recursive_gen_depth_est
```

All log entries consistently show `external_review_enabled=False`.

## Configuration Structure (if it were enabled)

Based on the `is_external_review_enabled()` function in `/home/ubuntu/agent-ml-research/core/tools/project_config.py` (lines 459-469), the configuration structure should be:

```yaml
external_review:
  paperreview_ai:
    enabled: true  # or false
```

However, this section does not exist in the current project configuration, causing the default behavior to be `enabled: False`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Agent",
  "elapsed_ms": 60179
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-20T06:25:50.707107+00:00_

Perfect! I have successfully read all the paper files. Let me provide you with a comprehensive summary of the complete paper contents:

## Complete Paper Contents: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"

### **Main File Structure**
The paper is organized with a main.tex file that inputs 11 sections plus references, targeting EMNLP 2026 (ARR May cycle).

---

## **ABSTRACT**
The paper formalizes recursive generation depth estimation as ordinal classification. Key findings:
- 180K-passage benchmark spanning 3 model families (Pythia-1.4B, OLMo-1B, GPT-2 XL), 3 decoding strategies, and 4 depths under full-replacement recursive chains
- Random Forest over statistical features (dominated by perplexity tail: p90_ppl, p75_ppl, kurtosis_ppl) achieves 59-82% d1-d3 balanced accuracy (69-86% four-class)
- Cross-model transfer: 66.4%, cross-domain arXiv: 74.1%, cross-strategy: 59.1%
- Introduces Effective Discriminable Depth (EDD) metric: EDD_0.70=4 for all three families
- Perturbation-based and membership inference baselines (29-33%) underperform; Binoculars reaches 78.1% vs 78.4% for the pipeline
- Merged feature sets (perplexity + Binoculars) yield 82.6%

---

## **INTRODUCTION**
- Addresses the novel problem: no existing method estimates ordinal recursive generation depth from text alone
- Existing tools handle adjacent problems (binary detection via Binoculars, watermarking, model collapse assuming known depth)
- Key finding: Recursive generation leaves **consistent but scale-dependent** statistical fingerprints
- Perplexity tail features (p90_ppl, p75_ppl, kurtosis_ppl) and surprisal variance are dominant depth indicators
- Formalized as ordinal classification with 19 reference-model statistical features and Random Forest classifier
- Introduces Depth Degradation Atlas (3×3 grid of models × strategies, 4 depths)
- Key contributions: task formalization, atlas, EDD metric, generalization analysis, feature convergence

---
…[truncated 15953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Agent",
  "elapsed_ms": 96373
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-20T06:26:36.994119+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-20T06:27:01.703937+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24709
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-20T06:27:02.157620+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review）\n- **ARR May cycle 截止**: 2026-05-25\n- **EMNLP commitment deadline**: 2026-08-02\n- **格式**: Long paper，正文 8 页限制，参考文献不限，ACL 模板，double-blind\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n### 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- main.tex 通过 \\input 引入：abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下维度，给出 Strengths / Weaknesses / Questions / Missing References：\n\n1. **实验设计与统计分析**\n   - 180K benchmark 构建是否合理？LoRA fine-tuning 链的 hyperparameter 选择（r=16, α=32）是否充分论证？\n   - Random Forest 作为主分类器，与 CORAL / XGBoost 等的比较是否充分？\n   - Cross-validation 设计是否有 data leakage 风险？\n   - 统计检验（bootstrap CI, p-value）使用是否恰当？多重比较校正是否完整？\n\n2. **Cross-transfer 有效性**\n   - Cross-model transfer（66.4%）、cross-strategy（59.1%, d1-d3: 45.9%）、cross-domain（74.1%）的实验设计和结论是否匹配？\n   - Cross-strategy d1/d2 boundary inversion 是否被充分分析和解释？\n   - Two-stage pipeline 是否是合理的解决方案？\n\n3. **EDD 指标**\n   - Effective Discriminable Depth 的定义是否严谨？T=0.70 的阈值选择是否有充分依据？\n   - 非单调 AUC 场景下 EDD 的适用性？\n   - Contiguous prefix 要求是否过于保守？\n\n4. **Baseline 比较**\n   - Binoculars（78.1%）vs 本方法（78.4%）差异不显著，如何定位本方法的附加价值？\n   - Perturbation-based baselines（DetectGPT 28.8%, Min-K% Prob 33.2%）是否为公平比较（binary → ordinal 适配）？\n   - Zero-shot LLM baselines 的设计是否充分？\n\n5. **Reference Model 自引用问题**\n   - Pythia-1.4B 同时作为 reference model 和 generator，Table 中是否充分标注？\n   - Self-reference 带来的 4-11pp 优势是否影响 cross-model 比较的公平性？\n\n6. **Cross-scale 实验**\n   - 7-8B 和 14B 实验的结论强度是否与证据匹配？\n   - 14B EDD=0 但 claim \"signal persists\" 是否言过其实？\n   - Mixed confounders（model family, tokenizer, training data 均不同）是否被充分讨论？\n\n7. **Reproducibility**\n   - Cross-seed replication 仅 3/9 cells，是否足够？\n   - 单一 LoRA 超参配置是否影响结论普适性？\n\n请以 EMNLP 2026 顶会标准严格审稿。每个 Weakness 标注 **[Must-Fix]** / **[Should-Fix]** / **[Minor]**。最后给出独立评分建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review）\n- **ARR May cycle 截止**: 2026-05-25\n- **EMNLP commitment deadline**: 2026-08-02\n- **格式**: Long paper，正文 8 页限制，参考文献不限，ACL 模板，double-blind\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n### 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- main.tex 通过 \\input 引入：abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下维度，给出 Strengths / Weaknesses / Questions / Missing References：\n\n1. **实验设计与统计分析**\n   - 180K benchmark 构建是否合理？LoRA fine-tuning 链的 hyperparameter 选择（r=16, α=32）是否充分论证？\n   - Random Forest 作为主分类器，与 CORAL / XGBoost 等的比较是否充分？\n   - Cross-validation 设计是否有 data leakage 风险？\n   - 统计检验（bootstrap CI, p-value）使用是否恰当？多重比较校正是否完整？\n\n2. **Cross-transfer 有效性**\n   - Cross-model transfer（66.4%）、cross-strategy（59.1%, d1-d3: 45.9%）、cross-domain（74.1%）的实验设计和结论是否匹配？\n   - Cross-strategy d1/d2 boundary inversion 是否被充分分析和解释？\n   - Two-stage pipeline 是否是合理的解决方案？\n\n3. **EDD 指标**\n   - Effective Discriminable Depth 的定义是否严谨？T=0.70 的阈值选择是否有充分依据？\n   - 非单调 AUC 场景下 EDD 的适用性？\n   - Contiguous prefix 要求是否过于保守？\n\n4. **Baseline 比较**\n   - Binoculars（78.1%）vs 本方法（78.4%）差异不显著，如何定位本方法的附加价值？\n   - Perturbation-based baselines（DetectGPT 28.8%, Min-K% Prob 33.2%）是否为公平比较（binary → ordinal 适配）？\n   - Zero-shot LLM baselines 的设计是否充分？\n\n5. **Reference Model 自引用问题**\n   - Pythia-1.4B 同时作为 reference model 和 generator，Table 中是否充分标注？\n   - Self-reference 带来的 4-11pp 优势是否影响 cross-model 比较的公平性？\n\n6. **Cross-scale 实验**\n   - 7-8B 和 14B 实验的结论强度是否与证据匹配？\n   - 14B EDD=0 但 claim \"signal persists\" 是否言过其实？\n   - Mixed confounders（model family, tokenizer, training data 均不同）是否被充分讨论？\n\n7. **Reproducibility**\n   - Cross-seed replication 仅 3/9 cells，是否足够？\n   - 单一 LoRA 超参配置是否影响结论普适性？\n\n请以 EMNLP 2026 顶会标准严格审稿。每个 Weakness 标注 **[Must-Fix]** / **[Should-Fix]** / **[Minor]**。最后给出独立评分建议。"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-20T06:27:22.382532+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20224
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-20T06:27:22.734707+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review）\n- **ARR May cycle 截止**: 2026-05-25\n- **EMNLP commitment deadline**: 2026-08-02\n- **格式**: Long paper，正文 8 页限制，参考文献不限，ACL 模板，double-blind\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n### 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- main.tex 通过 \\input 引入：abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix\n\n### 你的审查侧重：新颖性与完整性\n\n请重点审查以下维度，给出 Strengths / Weaknesses / Questions / Missing References：\n\n1. **Problem Framing 与 Novelty**\n   - \"Recursive generation depth estimation\" 作为新任务的 formalization 是否有意义？是否有先前工作已隐式或显式处理此问题？\n   - 从 binary AI text detection → ordinal depth classification 的推进是否足够 novel？\n   - Depth Degradation Atlas 和 EDD 作为 conceptual contribution 是否有足够价值？\n   - 论文使用标准 RF + 标准统计特征，算法贡献如何？论文是否恰当定位为 empirical study？\n\n2. **Related Work 覆盖与定位**\n   - Model collapse 文献（Shumailov et al. Nature, MAD framework）覆盖是否完整？\n   - AI text detection 文献（Binoculars, DetectGPT, watermarking）是否遗漏重要工作？\n   - Data provenance / membership inference 领域的定位是否准确？\n   - 是否有近期（2025-2026）的重要 related work 被遗漏？请搜索确认。\n\n3. **写作质量**\n   - Abstract 是否清晰传达核心贡献？数字是否过多导致信息过载？\n   - Introduction 的叙事结构是否有效（problem → gap → contribution）？\n   - Discussion 部分是否足够深入？核心洞察是否被放逐到 Appendix？\n   - Limitations 是否全面、诚实？是否隐瞒了重要局限？\n   - 是否存在 AI 写作痕迹（如过度使用 -ing 分词短语 \"confirming/demonstrating/suggesting\"）？\n\n4. **格式合规**\n   - 正文是否控制在 8 页内？\n   - 是否使用正确的 ACL 模板？（检查 \\usepackage[review]{acl}）\n   - 匿名化是否彻底？是否有 self-citation 泄露身份？\n   - 参考文献格式是否一致？是否有孤立（未引用）的 bib entries？\n   - 表格和图表编号是否连续？Caption 是否自包含？\n\n5. **Claim-Evidence 匹配**\n   - Abstract 和 Introduction 中的核心 claims 是否都有充分实验支撑？\n   - \"Full-replacement\" vs \"accumulation\" 的 scope 限制是否在论文中充分声明？\n   - Cross-scale \"signal persists at larger scales\" 的 claim 是否与 14B EDD=0 的数据匹配？\n   - Curation PoC（RF vs unfiltered p>0.4）是否被适当定调为 inconclusive？\n\n6. **引用完整性**\n   - 搜索 2025-2026 年发表的关于 model collapse、AI text detection、data provenance 的新论文\n   - 检查所有 bib entries 是否真实存在（无幻觉引用）\n   - 检查是否有 bib entries 存在但未被正文 cite\n\n请以 EMNLP 2026 顶会标准严格审稿。每个 Weakness 标注 **[Must-Fix]** / **[Should-Fix]** / **[Minor]**。最后给出独立评分建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review）\n- **ARR May cycle 截止**: 2026-05-25\n- **EMNLP commitment deadline**: 2026-08-02\n- **格式**: Long paper，正文 8 页限制，参考文献不限，ACL 模板，double-blind\n- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n### 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n- main.tex 通过 \\input 引入：abstract, introduction, related_work, method, theory, atlas, generalization, discussion, conclusion, section_appendix\n\n### 你的审查侧重：新颖性与完整性\n\n请重点审查以下维度，给出 Strengths / Weaknesses / Questions / Missing References：\n\n1. **Problem Framing 与 Novelty**\n   - \"Recursive generation depth estimation\" 作为新任务的 formalization 是否有意义？是否有先前工作已隐式或显式处理此问题？\n   - 从 binary AI text detection → ordinal depth classification 的推进是否足够 novel？\n   - Depth Degradation Atlas 和 EDD 作为 conceptual contribution 是否有足够价值？\n   - 论文使用标准 RF + 标准统计特征，算法贡献如何？论文是否恰当定位为 empirical study？\n\n2. **Related Work 覆盖与定位**\n   - Model collapse 文献（Shumailov et al. Nature, MAD framework）覆盖是否完整？\n   - AI text detection 文献（Binoculars, DetectGPT, watermarking）是否遗漏重要工作？\n   - Data provenance / membership inference 领域的定位是否准确？\n   - 是否有近期（2025-2026）的重要 related work 被遗漏？请搜索确认。\n\n3. **写作质量**\n   - Abstract 是否清晰传达核心贡献？数字是否过多导致信息过载？\n   - Introduction 的叙事结构是否有效（problem → gap → contribution）？\n   - Discussion 部分是否足够深入？核心洞察是否被放逐到 Appendix？\n   - Limitations 是否全面、诚实？是否隐瞒了重要局限？\n   - 是否存在 AI 写作痕迹（如过度使用 -ing 分词短语 \"confirming/demonstrating/suggesting\"）？\n\n4. **格式合规**\n   - 正文是否控制在 8 页内？\n   - 是否使用正确的 ACL 模板？（检查 \\usepackage[review]{acl}）\n   - 匿名化是否彻底？是否有 self-citation 泄露身份？\n   - 参考文献格式是否一致？是否有孤立（未引用）的 bib entries？\n   - 表格和图表编号是否连续？Caption 是否自包含？\n\n5. **Claim-Evidence 匹配**\n   - Abstract 和 Introduction 中的核心 claims 是否都有充分实验支撑？\n   - \"Full-replacement\" vs \"accumulation\" 的 scope 限制是否在论文中充分声明？\n   - Cross-scale \"signal persists at larger scales\" 的 claim 是否与 14B EDD=0 的数据匹配？\n   - Curation PoC（RF vs unfiltered p>0.4）是否被适当定调为 inconclusive？\n\n6. **引用完整性**\n   - 搜索 2025-2026 年发表的关于 model collapse、AI text detection、data provenance 的新论文\n   - 检查所有 bib entries 是否真实存在（无幻觉引用）\n   - 检查是否有 bib entries 存在但未被正文 cite\n\n请以 EMNLP 2026 顶会标准严格审稿。每个 Weakness 标注 **[Must-Fix]** / **[Should-Fix]** / **[Minor]**。最后给出独立评分建议。"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-20T06:27:24.548065+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1813
}
```

</details>

---


### Assistant

_source line 1196 · 2026-05-20T06:27:32.969969+00:00_

**Step 0-1 完成，当前状态：**

| 任务 | 状态 |
|------|------|
| Venue 调研（EMNLP 2026 / ARR May cycle） | 已确认：截止 2026-05-25，距今 5 天 |
| 视觉审查 Agent | 已派发，后台执行中 |
| Reviewer 1（方法严谨性） | Round 1 任务已下发 |
| Reviewer 2（新颖性与完整性） | Round 1 任务已下发 |
| 外部审稿（Stanford Agentic Reviewer） | 项目未启用，跳过 |

等待两名 Reviewer 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1197 · 2026-05-20T06:37:13.040276+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查（Round 1）

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 问题定义新颖、benchmark 构建系统，但 headline metrics 被 d0 系统性膨胀、与 Binoculars 无显著差异、cross-transfer 实用性不足、14B 实验严重混淆，作为主会议论文方法严谨性未达标，作为 Findings 论文贡献足够。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心 in-distribution 实验严谨；cross-transfer 和 cross-scale 的 claim 超出证据支撑；自引用混淆未充分隔离 |
| Excitement | 3.5/5 | 问题本身新颖有价值（递归生成深度估计是新方向）；EDD 指标有概念贡献；但方法简单（RF + 手工特征），增量性较强 |
| Reproducibility | 4.0/5 | 超参详尽（Appendix A），代码承诺开源；但 cross-seed 仅覆盖 3/9 cells，单一 LoRA 配置 |
| Overall Assessment | 3.0 | Findings 水平——贡献真实但主会议接收需解决 d0 膨胀表述、baseline 差距不显著、cross-scale 混淆等关键问题 |
| Confidence | 4/5 | 仔细阅读了全文和全部 25 页附录，核验了统计检验和引用 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Headline metrics 被 d0 召回率系统性膨胀，误导读者对方法实用性的判断
- 具体位置：Abstract（"accuracy of 59–82%"）, Section 4.1 Table 2, Section 5.2 Table 5（"66.4%"）, Section 6
- 问题：d0（human-written）召回率 >97%（Table 2 脚注），four-class accuracy 被 d0 严重拉高。Cross-model transfer 的 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 作为主指标，d1-d3 balanced accuracy 虽有报告但始终处于括号内或脚注位置。这在实际应用中会误导用户：一个能以 97% 识别人类文本但只有 26.8% 识别 d2 的系统，其实用价值与 "66.4% accuracy" 给人的印象截然不同。
- 为什么影响接收：ACL ARR soundness 要求 claims 与 evidence 匹配。当前表述方式让读者高估了方法在真正困难（d1-d3 discriminability）场景下的能力。
- 建议修改方向：(1) Abstract 和 Introduction 同时并列报告 four-class accuracy 和 d1-d3 balanced accuracy；(2) 在 Section 6 Discussion 中明确承认 d0 膨胀效应并量化其影响；(3) 考虑以 d1-d3 balanced accuracy 作为主指标。

**N2** [critical] 与 Binoculars baseline 无显著差异（78.4% vs 78.1%, p>0.05），论文未充分定位自身方法的附加价值
- 具体位置：Section 5.1 Table 4, Section 5.1 正文第 3 段, Appendix B.17 Table B.17
- 问题：论文 19-feature RF（78.4%）与 Binoculars 11-feature RF calibration（78.1%）在 9-cell mean 上无统计显著差异。Table 4 中 Binoculars 行列出的是 threshold（69.8%）和 RF (1 feat)（63.7%）两个较弱配置，78.1% 的完整 11-feature 配置仅在正文中一句话提及。这种呈现方式不透明。Merged 30-feature 达到 82.6%（+4.2pp），说明两个管线的信号部分互补——但互补性本身暗示 19-feature pipeline 并未完全覆盖 Binoculars 的信号，反之亦然。
- 为什么影响接收：如果一个已有方法（Binoculars + RF calibration）已经达到相同性能，那么本文的方法论贡献（19-feature pipeline）需要通过其他维度（如 interpretability、deployment cost、无需 performer model）来论证，而非仅以 accuracy 定位。
- 建议修改方向：(1) Table 4 中加入 Binoculars 11-feat RF 行并标注 p-value；(2) 明确论证本文管线相对 Binoculars 的优势（如单一 reference model 即可、无需 observer-performer pair、特征可解释性、merged system 的增益来源）；(3) 将 merged 82.6% 作为推荐配置而非附录内容。

**N3** [critical] 14B 实验严重混淆，"signal persists" claim 言过其实
- 具体位置：Section 5.4, Section 6 第 1 段, Appendix B.12 Table B.6 及 §Confounds
- 问题：14B 实验（Qwen2.5-14B, mean 50.8%, EDD=0）同时改变了 5 个变量：(a) model family（Qwen vs Pythia/OLMo/GPT-2）, (b) tokenizer, (c) training data, (d) reference model（self-reference vs cross-reference Pythia-1.4B）, (e) model scale（14B vs 1-1.5B）。Appendix B.12 §Confounds 承认 "it is therefore infeasible to attribute the observed accuracy gap to any single factor"，但 Section 5.4 和 Section 6 仍声称 "signal persists at 14B"。当 EDD=0（no adjacent-depth pair exceeds T=0.70）时，声称 "d1-d3 discrimination persists" 与 EDD 指标的定义矛盾——EDD 正是为了衡量这种 discrimination，而它报告为 0。50.8% 仅为 2× chance，在高方差小样本下可能不稳定。
- 为什么影响接收：这是 overclaiming。作者自己的 EDD 指标说 0，但结论说 "persists"，这是内部不一致。多重混淆使得无法将 50.8% 归因于 depth signal vs 其他因素。
- 建议修改方向：(1) 将 Section 5.4 标题从 "Preliminary Cross-Scale Observations" 改为更明确的 caveat（如 "Inconclusive Cross-Scale Observations"）；(2) Section 6 中不应使用 "persists"，改为 "above-chance accuracy is observed but cannot be attributed to depth signal due to multiple confounds"；(3) 在 14B 实验中加入 Qwen2.5-14B 的 Pythia-referenced pipeline（而非 self-reference）以隔离 reference model 混淆。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Should-Fix] Self-reference 混淆使 3×3 atlas 内部不可比
- 具体位置：Section 3.2 §Reference model, Table 2（†标注）, Appendix B.11 Table B.11
- 问题：Pythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp（Table B.11: self 78.6% vs cross-OLMo 74.5% vs cross-GPT2 67.3%）。这意味着 Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%，与 OLMo 和 GPT-2 XL 的表观优势关系反转。虽然论文用 † 标注并在 Limitations 中讨论，但 atlas 分析（Section 4）中的所有 cross-cell 比较（如 "GPT-2 XL achieves the highest accuracy under every strategy"）均基于这个不公平基础。
- 建议：在 Table 2 中增加一列 cross-reference accuracy（OLMo-1B 或 GPT-2 XL 作为 reference），使 atlas 内部比较基于相同条件。或者至少在 Section 4.1 的 axis effect 分析中明确说明 Pythia 行的可比性受限。

**W2** [Should-Fix] Cross-strategy transfer d1-d3 仅 45.9%（1.38× chance），实用性存疑
- 具体位置：Section 5.3 Table 6, Appendix B.23 §Cross-strategy conditional decomposition
- 问题：d1-d3 balanced accuracy 45.9%（chance 33.3%）意味着在 decoding strategy 未知时，系统对 generated text 的深度估计几乎没有实用价值。d1/d2 boundary inversion（AUC<0.5）意味着系统在某些 strategy 下会系统性地反转深度判断。Two-stage pipeline 回收 11.5pp，但前提是 strategy space 已知且 strategy classifier 准确——论文未报告 strategy classifier 本身的准确率。
- 建议：(1) 报告 two-stage pipeline 中 strategy classifier 的独立准确率；(2) 在 Section 6 中明确将 "decoding strategy must be known or identifiable" 列为部署前提条件，而非仅在 Limitations 中提及。

**W3** [Should-Fix] 单一 LoRA 超参配置（r=16, α=32）无 sensitivity analysis
- 具体位置：Section 3.2 §Generation pipeline, Appendix A Table A.1
- 问题：所有 180K 样本和全部实验使用相同 LoRA 配置。不同 LoRA rank（r=4, 8, 32, 64）和 learning rate 可能产生不同的 distributional shift patterns。如果 depth signal 部分来源于特定 LoRA rank 的 underfitting/overfitting 特征（r=16 可能比 full fine-tuning 产生更大的 distributional gap），那么结论的普适性受限。论文在 Limitations 中承认 "single LoRA instance" 但未提供任何 sensitivity analysis。
- 建议：至少在一个 model-strategy cell 上提供 r∈{4, 8, 16, 32} 的 sensitivity analysis，或与 full fine-tuning 对比一个 cell 的深度估计准确率。

**W4** [Should-Fix] Cross-seed replication 不充分（3/9 cells），OLMo +3.17pp 非重叠 CI 表明 benchmark 不稳定
- 具体位置：Appendix B.16 Table B.9
- 问题：仅 Pythia/OLMo/GPT-2 XL 的 nucleus cell 有 2-seed replication（3/9 cells）。OLMo seed=42 78.94% → seed=43 82.11%（+3.17pp），CI 不重叠。这意味着 Table 2 中的 OLMo nucleus accuracy 有 ~3pp 不确定性。温度和 top-k cells 完全未复制。更严重的是，feature rankings 的 seed stability 虽被声称 "identical top-3"，但未报告跨 seed 的 importance 值变化幅度。
- 建议：(1) 在所有 9 cells 上提供 cross-seed replication；(2) 报告 importance 值的 seed-wise 标准差。

**W5** [Should-Fix] EDD T=0.70 阈值选择缺乏充分依据
- 具体位置：Section 3.4, Section 4.3
- 问题：T=0.70 被选为 primary threshold，理由是 "corresponding to adequate discrimination in ROC analysis (8/9 cells achieve EDD ≥ 3)"。这是循环论证——选择一个让大多数 cells 看起来好的阈值。T=0.75 时只有 7/9 cells 达到 EDD≥3，T=0.80 时只有 5/9。论文确实报告了 sensitivity analysis（Section 4.3），但 T=0.70 的 "primary" 地位未基于外部标准（如 classification error rate bound, information-theoretic argument）论证。
- 建议：(1) 提供 T 选择的 principled justification（如与 downstream task performance 的关联，或与 classification error rate 的对应关系）；(2) 如无法提供，则在正文中将 T=0.70 定位为 "illustrative" 而非 "primary"。

**W6** [Should-Fix] Perturbation-based baselines 从 binary → ordinal 的适配不充分
- 具体位置：Section 5.1 Table 4, Appendix B.19
- 问题：DetectGPT（28.8%）和 Min-K% Prob（33.2%）是二分类方法，被改造为序数分类 baselines。DetectGPT 使用 "best-of-3" calibration，Min-K% 使用 CORAL calibration。但这些方法从未被设计用于序数深度估计——它们的 score 空间（perturbation discrepancy, token-level log-probability）不一定具有序数结构。28-33% 的性能接近 chance（25%），这可能反映适配方法的局限而非方法本身的局限。Appendix B.19 中 augmented feature set（19 + Min-K%）提升 +0.48pp 并 Min-K% 排名 #3，说明 Min-K% 确实携带互补信号——当配合合适的特征工程时可以工作。
- 建议：(1) 在 Table 4 中注明 "adapted from binary detection; comparison reflects ordinal adaptation rather than original method"；(2) 加入 min-K% 和 DetectGPT 的 binary d0-vs-d1+ 性能作为 sanity check。

**W7** [Should-Fix] Curation PoC（Appendix B.10）主结论非显著（p>0.4），存在多重比较问题
- 具体位置：Appendix B.10 Tables B.7 & B.8, Appendix B.23
- 问题：RF-filtered vs unfiltered（p=0.407）——主假设不成立。RF-vs-random 的 3 个 pairwise comparison（p<0.02 before Bonferroni）在 Bonferroni 校正后仅 1/3 存活（p<0.003 vs threshold 0.017）。论文在 Appendix B.23 中部分承认（"1 of 3 comparisons surviving"），但 Appendix B.10 的呈现未充分强调非显著的主结论。
- 建议：(1) 将 Appendix B.10 标题改为 "Curation PoC (Inconclusive)"；(2) 在正文中提及 curation 时使用 "inconclusive" 而非暗示有效。

---

## 小问题（不影响接收）

- **[Minor]** Table 4 中 Binoculars 的 calibration 列写 "threshold" 和 "RF (1 feat)"，但 78.1% 的 11-feat RF 配置未出现在 table 中。建议补充。
- **[Minor]** 引用验证：7 条在 OpenAlex 未找到（knowledge_collapse2025, falahati2026_curated, mitchell2023_detectgpt 等），多为 2025-2026 新论文或索引问题，非虚构。4 条有年份/first-author 微小 mismatch（he2021_deberta_v3 bib 标 2023 vs 实际 2021; alemohammad2024_mad first author mismatch）。建议修正 bib 年份。
- **[Minor]** Appendix B.12 中 7-8B 实验使用 4-bit NF4 QLoRA（与 1-1.5B 的 bf16 LoRA 不同），这一差异在 Table B.6 中未标注。
- **[Minor]** Section 5.1: "Single-feature regression on mean perplexity performs at chance (25.1%)" — 但 Table B.20 显示 p90_ppl alone 达到 58.3%。Mean perplexity 是最弱的 perplexity 特征，以它代表 "surface-text ablation" 可能低估了简单 baselines。
- **[Minor]** Cross-boundary generalization（Appendix B.15）：heterogeneous chain 的 confound（architecture identity ≡ depth）虽有 reverse-chain control，但 reverse chain 也只是将另一组 architecture 映射到 depth，无法完全排除 architecture fingerprint 的贡献。

---

## 主要优势

1. **问题定义新颖且有价值**：将递归生成深度估计形式化为序数分类问题，区别于现有的 binary human/machine detection，具有理论清晰性和实际意义。在 model collapse 文献中这是一个被忽视的逆问题。

2. **Benchmark 设计系统**：180K 样本覆盖 3 model families × 3 decoding strategies × 4 depths 的完整网格，控制变量严格（固定 LoRA 配置、固定 reference model、固定 seed text）。Domain bias analysis（Appendix B.8, Sub-A/B/C）包括 bug 修复透明披露，体现了实验诚信。

3. **EDD 指标有概念贡献**：将聚合准确率分解为逐深度边界的可判别性，提供了比单一准确率更有信息量的评估框架。虽然具体实现（contiguous prefix + fixed threshold）有改进空间，但概念方向正确。

4. **Feature analysis 深入且一致**：三种 importance measures（Gini, SHAP, permutation）的高一致性（Kendall's W=0.90, p<0.005），perplexity tail 特征在 9/9 cells 中的统治性，以及理论 grounding（tail erosion → decreasing p90_ppl）形成了完整的叙事。

5. **Limitations 异常全面**：论文用整整一页讨论了 10+ 个 limitations，包括 d0 inflation、FPR、self-reference confound、cross-strategy constraint 等。多数问题是作者自己识别并讨论的。这在 submission 中较为少见。

6. **Appendix 丰富**（15页附录，含 23 个子实验）：包括 domain bias 修正、calibration、feature overlap、end-to-end comparison、depth-4/5 extension、prompted generation、instruction-tuned model、cross-boundary chain 等。

---

## Missing References / Related Work

- **Recursive text generation detection**: 论文未引用 EditLens 之外的 partial-generation / mixed-origin detection 方法。虽然 depth estimation 是更窄的问题定义，但 sentence-level attribution 方法（如 SeqXGPT）与论文的 passage-level 假设形成对比，值得讨论。
- **Ordinal classification baselines**: 论文在 Appendix B.19 中比较了 CORAL、Frank & Hall、Rennie & Srebro 等 ordinal methods，但主文 Table 4 仅列 RF。建议在 Table 4 中加入 XGBoost（67.2%）和 Ordinal MLP（66.7%）的 cross-model transfer 结果以完整呈现 classifier 比较。

---

## Reviewer Confidence
4/5: 仔细阅读了 10 页正文 + 15 页附录的全部内容，核验了 EDD 定义的数学一致性、Table 2/4/5/6 的数值与 appendix 的对应关系、statistical tests 的使用（bootstrap CI, Wilson CI, paired t-test, Bonferroni correction）、以及 68 条引用的在线验证。对 model collapse 理论和 AI text detection 文献有一般性了解，但非该子领域核心研究者。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1198 · 2026-05-20T06:37:26.187684+00:00_

Reviewer 1 审稿意见已收到。评分 3.0（Findings），核心问题：d0 膨胀 headline metrics、与 Binoculars 无显著差异、14B overclaiming。

等待 Reviewer 2 返回后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1199 · 2026-05-20T06:37:46.551218+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.0（Findings），Soundness 3.0/5，Excitement 3.5/5，Reproducibility 4.0/5。

**3 个 Must-Fix 问题**：
1. Headline metrics 被 d0 召回率系统性膨胀（d1-d3 balanced accuracy 才是真正指标，但被 bracket 化处理）
2. 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%, p>0.05），方法附加价值定位不清
3. 14B 实验 5 重混淆下 EDD=0，"signal persists" 与自定义 EDD 指标矛盾

**7 个 Should-Fix 问题**：self-reference 混淆使 atlas 不可比、cross-strategy d1-d3 仅 1.38× chance、单一 LoRA 配置无 sensitivity analysis、cross-seed 仅 3/9 cells、EDD T=0.70 循环论证、perturbation baseline 适配不充分、curation PoC 非显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1200 · 2026-05-20T06:37:52.273201+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 109

## Round 109

6 recorded events


### User

_source line 1201 · 2026-05-20T06:37:58.589772+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿报告（新颖性与完整性）

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 (ACL Rolling Review May cycle)

---

## 总体评分

**Overall**: 3.0 / 5（Findings 级别）
**一句话总结**: 任务定义新颖且实验设计系统，但方法贡献有限（标准 RF + 标准特征），scale generalization 在 14B 时崩塌（EDD=0），full-replacement 假设严重限制生态效度，综合来看达到 Findings 标准但不足以被主会议接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论严谨（5-fold CV, 多 seed, bootstrap CI），但 full-replacement 假设与 real-world accumulation 场景差距过大，14B 结果（EDD=0）与 "signal persists" 叙事存在张力 |
| Excitement | 2.5/5 | 任务定义有意义且时机恰当（model collapse 话题热度高），但执行层面无算法创新，RF+统计特征是成熟方法的直接应用；cross-transfer 性能较弱限制实用价值 |
| Reproducibility | 4.0/5 | LoRA 训练协议（Appendix A）、特征定义（Table 1）、超参数均有详细记录；承诺释放代码和数据；随机种子有报告（Appendix B.24） |
| Overall Assessment | 3.0/5 | Findings 可接收：新颖任务形式化 + 系统实证分析，但缺乏方法论贡献、scale 受限、实用性存疑 |
| Confidence | 4/5 | 熟悉 AI text detection 和 model collapse 文献，仔细检查了实验设计和数据 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Scale generalization 的叙事与证据之间存在系统性张力

- 具体位置：Abstract（"scale-dependent in magnitude"）、§5.4（p.8）、Appendix B.14（p.18-19）
- 问题：Abstract 声称 fingerprints "are consistent in direction but scale-dependent in magnitude across the three model families"，Introduction 称 "the perplexity tail feature family (p90_ppl, kurtosis_ppl) and surprisal variance emerge as dominant depth indicators"。但 14B 结果（Appendix B.14, Table 17）显示 EDD₁₄B = 0（所有三种解码策略下无相邻深度对 AUC 超过 0.70 阈值），4-class 准确率仅 50.8%（2× chance，但远低于 1.5B 的 59-82%）。7-8B 结果虽优于 chance（Llama-3.1-8B: 70.2%, Qwen2.5-7B: 60.1%），但 cross-scale 实验仅验证了 Pythia-1.4B 特征在更大模型上的迁移，未重新训练分类器。
- 这意味着：在实际关心的模型规模（≥14B，现代 LLM 普遍 >70B）上，该方法的实用性未经验证。14B EDD=0 是一个根本性的 negative result，论文需要更突出地呈现。
- 为什么影响接收：如果方法无法 scale 到实际使用的模型大小，论文的实用价值大幅缩水，读者可能得出 "仅在 toy-scale 有效" 的结论。
- 建议修改方向：(1) 在 Abstract 和 Introduction 中明确声明 14B EDD=0 的结果及其对实用性的影响；(2) 将 §5.4 的 cross-scale 分析扩展到主体正文而非仅 1 段话；(3) 讨论 14B EDD=0 可能的原因（LoRA 微调在 14B 上的效果更弱？特征空间在大模型上变化？）及未来缓解方向。

**N2** [critical] Full-replacement 假设严重限制生态效度，论文未充分论证其合理性

- 具体位置：§3.2（p.3）、Limitations（p.9）、Appendix B.22（p.22）
- 问题：所有实验使用 full-replacement 递归链（每一代完全替换上一代训练数据）。论文 Limitations 正确指出 "Real-world contamination typically involves partial mixing (accumulation), where synthetic and human data co-exist at unknown proportions"，但未量化这一 gap 的影响。Appendix B.22 的 Curation PoC 是唯一尝试验证下游价值的实验，但结果 inconclusive：(1) d0-only data 并非最低 perplexity（d1-only 和 mixed 更低），(2) "single sample is insufficient for statistical significance"，(3) 训练 loss 随深度单调下降但这可能仅反映信息量减少而非质量下降。
- 为什么影响接收：full-replacement 是 model collapse 理论中的 worst case（Gerstgrasser et al., 2024 已证明 accumulation 可避免 collapse）。如果深度信号仅在 replacement 场景下明显，而 real-world 是 accumulation，那么整个方法的应用前景不明。
- 建议修改方向：(1) 至少增加一组 partial-mixing 实验（如 50% synthetic + 50% real 混合），验证深度信号是否存在；(2) 如果无法实验，应在 Discussion 中进行更深入的分析讨论，明确这是一个 open question 而非 minor caveat。

**N3** [critical] 算法贡献有限，论文定位需要更谨慎

- 具体位置：§3.3-3.4（p.4）、Table 1（p.4）、Table 4（p.7）
- 问题：核心方法是标准 Random Forest（200 棵树，5-fold CV）+ 19 个标准统计特征（perplexity 统计量、surprisal 统计量、词汇多样性、重复模式）。所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等均使用类似统计量）。DeBERTa-v3 端到端基线反而低于 RF（Table 4: RF 78.1% vs DeBERTa-v3+LoRA 53.1%），这说明是特征工程在发力，但这些特征并非论文的创新。论文在 p.2 称 "our contribution centers on task formalization and systematic empirical characterization rather than algorithmic novelty"，这个定位是诚实的，但 Findings 级别的 empirical study 也需要至少一些技术 insight 超越 "将已有方法应用到新任务"。
- 为什么影响接收：方法论贡献的缺失是限制论文从 Findings 上升到 Conference 的主要因素。审稿人（和 AC）会问：除了任务定义，读者能从这篇论文中学到什么 non-trivial 的方法论 insight？
- 建议修改方向：(1) 深入分析为什么 RF 大幅优于 neural 方法（Appendix B.9 有初步讨论但不够深入——"PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties" 值得展开）；(2) 考虑是否有 feature engineering 上的创新空间（如深度感知的特征组合）；(3) 加强 EDD 的 formalization，使其成为一个更有理论深度的贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 信息过载，核心信息被淹没

- 具体位置：Abstract（p.1）
- 问题：Abstract 包含过多具体数字——"180K-passage benchmark", "three model families", "three decoding strategies", "four depths", "1–5B scale", "59–82% (four-class; 68–86%)", "19 statistical features", "EDD_top-k=1", "p90_ppl, kurtosis_ppl"——导致核心贡献和关键发现被稀释。对比顶会 best paper 的 abstract，通常聚焦 1-2 个最 striking 的数字。
- 建议：精简数字，突出 (1) 任务新颖性、(2) 一个 headline accuracy number、(3) 核心 insight（perplexity tail fingerprint），将实验细节留给正文。

**W2** [warning] Discussion 过于单薄，核心洞察被放逐到 Appendix

- 具体位置：§6（p.8，约 1 页）
- 问题：Section 6 "Discussion and Conclusion" 篇幅有限，混合了讨论和结论。关键分析——multi-channel depth encoding（Appendix B.26）、cross-scale behavior（Appendix B.14）、curation PoC（Appendix B.22）、RF vs neural divergence（Appendix B.9）、downstream fine-tuning probe（Appendix B.22）——全部在 Appendix 中。主体 Discussion 仅有 "multi-channel depth encoding" 和 "prompted generation" 两段概述，深度不足。
- 为什么影响评分：读者（和审稿人）主要阅读主体 8 页，如果关键洞察在 Appendix 中，容易被忽略，也使主体显得缺乏分析深度。
- 建议：将 Appendix B.9（RF vs neural 的 feature space divergence 分析）和 B.22 的核心结论提升到主体 Discussion 中，即使以压缩形式呈现。

**W3** [warning] "Depth Degradation Atlas" 作为概念贡献被过度包装

- 具体位置：§4（p.5-6）、Contributions list（p.2）
- 问题："Atlas" 一词暗示一份全面的参考地图，但实际上是一个 3×3 grid（3 model families × 3 decoding strategies）的 RF 分类结果 + 特征重要性分析 + EDD 评估。这是一个系统的 empirical evaluation，但 "atlas" 这个术语让贡献显得比实际更大。
- 建议：使用更准确的术语，如 "systematic empirical analysis" 或 "benchmark evaluation"，或在正文中更清楚地界定 atlas 的含义和范围。

**W4** [warning] Cross-model 和 cross-strategy transfer 性能较弱但讨论不足

- 具体位置：Table 5（p.8）、Table 6（p.8）、§5.2-5.3（p.8）
- 问题：Cross-model transfer 最高 66.4%（vs in-distribution 59-82%）；cross-strategy transfer（Table 6）d1-d3 balanced accuracy 45.9%，mean d1-d3 accuracy 仅 45.9%。论文承认 "a two-stage pipeline is needed for reliable cross-strategy deployment"（p.9），但未充分讨论这对实际部署意味着什么——用户需要先知道是哪个模型、哪种解码策略，才能选择正确的分类器，这大大限制了 blind deployment 场景的实用性。
- 建议：在 Discussion 中增加一段关于 practical deployment constraints 的分析，明确需要哪些先验知识。

**W5** [warning] Curation PoC（Appendix B.22）结果 inconclusive 但论文仍将其列为 contribution

- 具体位置：Contributions list（p.2 未明确列出但 §6 提及 "practical curation"）、Appendix B.22（p.22）
- 问题：Downstream fine-tuning probe 结果显示 d0-only 并非最优（PPL 5.55 vs d1-only 更低），单次实验缺乏统计显著性，"single sample is insufficient for statistical significance"。训练 loss 随深度单调下降可能反映信息量减少而非质量变差。但 §6 Discussion 仍称 "depth estimation offers a practical signal for data curation"，语气偏乐观。
- 建议：明确将 curation 定调为 preliminary/inconclusive，不要在 contribution 级别上暗示它是一个 validated 应用。

---

## 小问题（不影响接收）

**M1** [minor] 部分 bib entry 年份不匹配
- `he2021_deberta_v3`: bib 记为 2023，OpenAlex 返回 2021（原始 arXiv 时间）
- `alemohammad2024_mad`: first author 不匹配（bib=Alemohammad vs API=Casco-Rodriguez）
- `guo2024_biscope`: first author 不匹配（bib=Guo vs API=Cheng）
- 建议核实并统一。

**M2** [minor] 引用一致性问题
- `gerstgrasser2024_accumulate` 类型为 `misc`（无 venue），但该论文已被 NeurIPS 2024 接收，应更新为 `inproceedings`
- `briesch2024selfconsuming` 同样为 `misc`，如已发表应更新

**M3** [minor] 个别 AI 写作痕迹
- "confirming its dominance across all 9 cells"（p.5）、"suggesting cross-model divergence features contribute more"（p.7）——-ing 分词短语作为独立分句的模式在论文中多处出现，虽不影响可读性但在 double-blind 中可能被注意到。

**M4** [minor] Figure 1（p.6）heatmap 色彩对比度有限
- 浅色单元格的数值难以直接从图中读取，建议增加数值标注或调整色板。

**M5** [minor] 脚注 1（p.4）细节
- "EDD binary classifiers use 500 trees; the main 4-class RF uses 200 trees" — 应解释为什么 binary 用更多树但 multi-class 用更少。

---

## 主要优势

1. **任务定义的新颖性和时效性**：将 recursive generation depth estimation 形式化为 ordinal classification 是一个有意义的概念贡献。在 model collapse 受到广泛关注的背景下，"how deep is your data?" 是一个自然且重要的问题。据搜索确认，目前无其他工作显式处理这个问题。

2. **实验设计的系统性**：3 model families × 3 decoding strategies × 4 depths 的 full grid 设计，配合 5-fold CV + bootstrap CI + 多 seed 验证，展示了 rigorous empirical methodology。Appendix 提供了 17 页的补充分析（ablation, robustness, cross-validation, domain bias, LoRA protocol），透明度很高。

3. **Perplexity tail insight 的理论连接**：将 model collapse 理论（tail distribution collapse）与检测特征（perplexity tail statistics）连接起来，§3.5 的 theoretical grounding 虽不完整但方向正确。EDD 上界与 contraction factor 的关系（§3.5）提供了有用的理论框架。

4. **诚实的局限性声明**：Limitations section（p.9）涵盖了 full-replacement vs accumulation、controlled setting vs wild deployment、cross-strategy constraint、EDD monotonicity assumption 等关键局限，态度坦诚。

5. **相关工作覆盖全面**：68 篇引用涵盖 model collapse 理论、AI text detection、data provenance、ordinal classification、decoding strategies 五个领域，包含 2025-2026 最新工作。verify_references 确认 0 orphan / 0 missing bib entries。

6. **Strategy-dependent trajectory** 的发现（§4.5, Figure 2）：不同解码策略产生质量不同的退化轨迹是一个有价值的 empirical insight，对理解 model collapse 的机制有帮助。

---

## 引用完整性审查

### 自动化检查结果（verify_references）
- 68 bib entries, 107 citations, 68 unique cited keys
- **0 orphan bib entries**（全部 bib entries 均被 cite）
- **0 missing bib entries**（所有 cite 的 key 均在 bib 中找到）
- 57/68 online verified, 7 not_found（多为 OpenAlex 索引问题，非幻觉引用——DetectGPT ICML'23、RoBERTa、Qwen2.5 tech report、Rennie 2005 workshop paper、Datamodels ICML'22、Knowledge Collapse NeurIPS-WS'25 均为真实论文，已通过 web search 确认）
- 4 mismatch（year/author 小问题，见 M1）

### 可能遗漏的相关工作

1. **PAN 2026 Shared Task**（Generative Plagiarism Detection, Voight-Kampff Generative AI Detection）—— 2026 年的 shared task 直接涉及 AI 生成文本的 fine-grained 检测和归属，与本文高度相关。
2. **TROVE** (NAACL 2025?) 和 **GenProve** (2026) —— fine-grained text provenance 方向的新工作，与 §2 Related Work 的 "Membership Inference and Data Provenance" 子节相关。
3. **"Collapse or Thrive? Perils and Promises of Synthetic Data in the Era of Generative AI"** (arXiv:2410.16713, 2024) —— 一篇较全面的 synthetic data survey，可作为 model collapse 文献的补充引用。
4. **Rate of Model Collapse in Recursive Training** (arXiv:2412.17646, 2024) —— 直接量化 recursive training 中 collapse 速率的理论工作，与 EDD 的 contraction factor 分析（§3.5）相关。

以上均为 suggestions，并非 must-cite，但引用它们可以加强论文的文献覆盖。

---

## Claim-Evidence 匹配分析

| Claim（位置） | 证据 | 评估 |
|-------------|------|------|
| "59–82% four-class accuracy"（Abstract） | Table 2（p.5） | ✅ 匹配 |
| "perplexity tail family dominates"（Abstract, §4.2） | Table 3, Figure 1（p.6）, Appendix B.2 | ✅ 匹配 |
| "fingerprints are consistent in direction but scale-dependent"（Abstract） | 1.5B results + 7-8B results（§5.4, Appendix B.14） | ⚠️ 部分匹配：14B EDD=0 使 "consistent in direction" 的表述存疑 |
| "signal persists at larger scales"（§5.4, p.8） | Appendix B.14: 14B accuracy 50.8%（2× chance）, 但 EDD=0 | ⚠️ "persists" 一词偏乐观，50.8% 仅 2× chance，实用性有限 |
| "cross-model transfer reaches 66.4%"（§5.2, p.8） | Table 5 | ✅ 匹配，但应更突出这是 best case，worst case 显著更低 |
| "curation PoC"（§6, Appendix B.22） | Appendix B.22: d0 非最低 PPL，单样本无统计显著性 | ⚠️ 结论 inconclusive，但 §6 语气偏乐观 |
| "full-replacement" scope（Limitations, p.9） | 明确声明 | ✅ 诚实声明 |

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| ACL 模板 | ✅ | `\usepackage[review]{acl}` |
| 正文 ≤ 8 页 | ✅ | §6 结束于 p.8 底部 |
| 匿名化 | ✅ | `\author{Anonymous}`，未发现 self-citation 泄露 |
| 参考文献格式 | ✅ | 基本一致，minor year mismatch 见 M1 |
| 图表编号连续 | ✅ | Figure 1-4, Table 1-29 连续 |
| Caption 自包含 | ✅ | 主要图表 caption 包含足够信息 |
| Limitations section | ✅ | p.9, 在 conclusion 之后、references 之前 |
| Ethics Statement | ✅ | p.9-10 |

---

## 独立评分建议

**Overall: 3.0（Findings）**

理由：论文在任务定义上有明确的新颖性贡献，实验设计系统且透明度高。但三个核心限制阻止其达到 Conference 级别：(1) 算法贡献缺失（标准 RF + 已有特征），(2) scale generalization 在 14B 时失效（EDD=0），(3) full-replacement 假设与 real-world 场景差距过大。如果作者能在 revision 中增加 partial-mixing 实验并更深入地分析 scale 限制，评分可能提升至 3.5。

当前评分区间：**2.5-3.0**，倾向 3.0，取决于 AC 如何权衡 "novel task formulation + thorough empirical work" vs "no method novelty + scale limitation"。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-20T06:39:21.673372+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — 方法严谨性审查（Round 1）\n\n### 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 问题定义新颖、benchmark 构建系统，但 headline metrics 被 d0 系统性膨胀、与 Binoculars 无显著差异、cross-transfer 实用性不足、14B 实验严重混淆，作为主会议论文方法严谨性未达标，作为 Findings 论文贡献足够。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 in-distribution 实验严谨；cross-transfer 和 cross-scale 的 claim 超出证据支撑；自引用混淆未充分隔离 |\n| Excitement | 3.5/5 | 问题本身新颖有价值（递归生成深度估计是新方向）；EDD 指标有概念贡献；但方法简单（RF + 手工特征），增量性较强 |\n| Reproducibility | 4.0/5 | 超参详尽（Appendix A），代码承诺开源；但 cross-seed 仅覆盖 3/9 cells，单一 LoRA 配置 |\n| Overall Assessment | 3.0 | Findings 水平——贡献真实但主会议接收需解决 d0 膨胀表述、baseline 差距不显著、cross-scale 混淆等关键问题 |\n| Confidence | 4/5 | 仔细阅读了全文和全部 25 页附录，核验了统计检验和引用 |\n\n### Must-Fix 问题\n\n**N1** [critical] Headline metrics 被 d0 召回率系统性膨胀，误导读者对方法实用性的判断\n- 具体位置：Abstract（\"accuracy of 59–82%\"）, Section 4.1 Table 2, Section 5.2 Table 5（\"66.4%\"）, Section 6\n- 问题：d0（human-written）召回率 >97%（Table 2 脚注），four-class accuracy 被 d0 严重拉高。Cross-model transfer 的 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 作为主指标，d1-d3 balanced accuracy 虽有报告但始终处于括号内或脚注位置。\n- 为什么影响接收：ACL ARR soundness 要求 claims 与 evidence 匹配。当前表述方式让读者高估了方法在真正困难（d1-d3 discriminability）场景下的能力。\n- 建议修改方向：(1) Abstract 和 Introduction 同时并列报告 four-class accuracy 和 d1-d3 balanced accuracy；(2) 在 Section 6 Discussion 中明确承认 d0 膨胀效应并量化其影响；(3) 考虑以 d1-d3 balanced accuracy 作为主指标。\n\n**N2** [critical] 与 Binoculars baseline 无显著差异（78.4% vs 78.1%, p>0.05），论文未充分定位自身方法的附加价值\n- 具体位置：Section 5.1 Table 4, Section 5.1 正文第 3 段, Appendix B.17 Table B.17\n- 问题：论文 19-feature RF（78.4%）与 Binoculars 11-feature RF calibration（78.1%）在 9-cell mean 上无统计显著差异。Table 4 中 Binoculars 行列出的是 threshold（69.8%）和 RF (1 feat)（63.7%）两个较弱配置，78.1% 的完整 11-feature 配置仅在正文中一句话提及。Merged 30-feature 达到 82.6%（+4.2pp），说明两个管线的信号部分互补。\n- 为什么影响接收：如果一个已有方法已经达到相同性能，那么本文的方法论贡献需要通过其他维度来论证。\n- 建议修改方向：(1) Table 4 中加入 Binoculars 11-feat RF 行并标注 p-value；(2) 明确论证本文管线相对 Binoculars 的优势（如单一 reference model、无需 observer-performer pair、特征可解释性）；(3) 将 merged 82.6% 作为推荐配置。\n\n**N3** [critical] 14B 实验严重混淆，\"signal persists\" claim 言过其实\n- 具体位置：Section 5.4, Section 6 第 1 段, Appendix B.12 Table B.6 及 §Confounds\n- 问题：14B 实验同时改变了 5 个变量：model family, tokenizer, training data, reference model, model scale。Appendix B.12 §Confounds 承认 \"infeasible to attribute the observed accuracy gap to any single factor\"，但 Section 5.4 和 Section 6 仍声称 \"signal persists at 14B\"。当 EDD=0 时，声称 \"d1-d3 discrimination persists\" 与 EDD 指标的定义矛盾。\n- 建议修改方向：(1) 将标题改为更明确的 caveat；(2) Section 6 中不应使用 \"persists\"；(3) 加入 Pythia-referenced pipeline 以隔离混淆。\n\n### Should-Fix 问题\n\n**W1** Self-reference 混淆使 3×3 atlas 内部不可比\n- Pythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp。Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%。\n- 建议：增加 cross-reference accuracy 列，或明确声明 Pythia 行可比性受限。\n\n**W2** Cross-strategy transfer d1-d3 仅 45.9%（1.38× chance），实用性存疑\n- d1/d2 boundary inversion（AUC<0.5）意味着系统在某些 strategy 下会系统性地反转深度判断。Two-stage pipeline 回收 11.5pp 但未报告 strategy classifier 准确率。\n- 建议：报告 strategy classifier 准确率；在 Discussion 中列为部署前提条件。\n\n**W3** 单一 LoRA 超参配置无 sensitivity analysis\n- 不同 LoRA rank 可能产生不同的 distributional shift patterns。论文在 Limitations 中承认但未提供 sensitivity analysis。\n- 建议：至少一个 cell 提供 r∈{4,8,16,32} 的 sensitivity analysis。\n\n**W4** Cross-seed replication 不充分（3/9 cells），OLMo +3.17pp 非重叠 CI\n- 仅 nucleus cells 有 2-seed replication。OLMo CI 不重叠（+3.17pp）。温度和 top-k 完全未复制。\n- 建议：所有 9 cells 提供 cross-seed replication。\n\n**W5** EDD T=0.70 阈值选择缺乏充分依据\n- \"选择一个让大多数 cells 看起来好的阈值\" 是循环论证。\n- 建议：提供 principled justification 或定位为 \"illustrative\"。\n\n**W6** Perturbation-based baselines 从 binary → ordinal 的适配不充分\n- DetectGPT 和 Min-K% Prob 从未被设计用于序数深度估计，28-33% 可能反映适配方法的局限。\n- 建议：注明适配来源，加入 binary d0-vs-d1+ 性能作为 sanity check。\n\n**W7** Curation PoC 主结论非显著（p>0.4），存在多重比较问题\n- RF-filtered vs unfiltered 主假设不成立。Bonferroni 校正后仅 1/3 存活。\n- 建议：标题改为 \"Curation PoC (Inconclusive)\"。\n\n### Minor 问题\n- Table 4 中 Binoculars 78.1% 的 11-feat 配置未出现在 table 中\n- 7 条引用在 OpenAlex 未找到（索引问题，非虚构）；4 条 year/author mismatch\n- Appendix B.12 中 7-8B 使用 QLoRA 但未标注\n- Mean perplexity 代表 \"surface-text ablation\" 低估了简单 baselines（p90_ppl alone 58.3%）\n- Heterogeneous chain 的 confound（architecture identity ≡ depth）未完全排除\n\n### 主要优势\n1. 问题定义新颖且有价值\n2. Benchmark 设计系统（180K 样本，domain bias 修复透明披露）\n3. EDD 指标有概念贡献\n4. Feature analysis 深入且一致（Kendall's W=0.90）\n5. Limitations 异常全面（10+ 个 limitations）\n6. Appendix 丰富（15 页，23 个子实验）\n\n### Missing References\n- SeqXGPT（sentence-level attribution）\n- Table 4 中应加入 XGBoost 和 Ordinal MLP 的 cross-model transfer 结果\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和 Minor 问题。对每条明确标注 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — 方法严谨性审查（Round 1）\n\n### 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 问题定义新颖、benchmark 构建系统，但 headline metrics 被 d0 系统性膨胀、与 Binoculars 无显著差异、cross-transfer 实用性不足、14B 实验严重混淆，作为主会议论文方法严谨性未达标，作为 Findings 论文贡献足够。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 in-distribution 实验严谨；cross-transfer 和 cross-scale 的 claim 超出证据支撑；自引用混淆未充分隔离 |\n| Excitement | 3.5/5 | 问题本身新颖有价值（递归生成深度估计是新方向）；EDD 指标有概念贡献；但方法简单（RF + 手工特征），增量性较强 |\n| Reproducibility | 4.0/5 | 超参详尽（Appendix A），代码承诺开源；但 cross-seed 仅覆盖 3/9 cells，单一 LoRA 配置 |\n| Overall Assessment | 3.0 | Findings 水平——贡献真实但主会议接收需解决 d0 膨胀表述、baseline 差距不显著、cross-scale 混淆等关键问题 |\n| Confidence | 4/5 | 仔细阅读了全文和全部 25 页附录，核验了统计检验和引用 |\n\n### Must-Fix 问题\n\n**N1** [critical] Headline metrics 被 d0 召回率系统性膨胀，误导读者对方法实用性的判断\n- 具体位置：Abstract（\"accuracy of 59–82%\"）, Section 4.1 Table 2, Section 5.2 Table 5（\"66.4%\"）, Section 6\n- 问题：d0（human-written）召回率 >97%（Table 2 脚注），four-class accuracy 被 d0 严重拉高。Cross-model transfer 的 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 作为主指标，d1-d3 balanced accuracy 虽有报告但始终处于括号内或脚注位置。\n- 为什么影响接收：ACL ARR soundness 要求 claims 与 evidence 匹配。当前表述方式让读者高估了方法在真正困难（d1-d3 discriminability）场景下的能力。\n- 建议修改方向：(1) Abstract 和 Introduction 同时并列报告 four-class accuracy 和 d1-d3 balanced accuracy；(2) 在 Section 6 Discussion 中明确承认 d0 膨胀效应并量化其影响；(3) 考虑以 d1-d3 balanced accuracy 作为主指标。\n\n**N2** [critical] 与 Binoculars baseline 无显著差异（78.4% vs 78.1%, p>0.05），论文未充分定位自身方法的附加价值\n- 具体位置：Section 5.1 Table 4, Section 5.1 正文第 3 段, Appendix B.17 Table B.17\n- 问题：论文 19-feature RF（78.4%）与 Binoculars 11-feature RF calibration（78.1%）在 9-cell mean 上无统计显著差异。Table 4 中 Binoculars 行列出的是 threshold（69.8%）和 RF (1 feat)（63.7%）两个较弱配置，78.1% 的完整 11-feature 配置仅在正文中一句话提及。Merged 30-feature 达到 82.6%（+4.2pp），说明两个管线的信号部分互补。\n- 为什么影响接收：如果一个已有方法已经达到相同性能，那么本文的方法论贡献需要通过其他维度来论证。\n- 建议修改方向：(1) Table 4 中加入 Binoculars 11-feat RF 行并标注 p-value；(2) 明确论证本文管线相对 Binoculars 的优势（如单一 reference model、无需 observer-performer pair、特征可解释性）；(3) 将 merged 82.6% 作为推荐配置。\n\n**N3** [critical] 14B 实验严重混淆，\"signal persists\" claim 言过其实\n- 具体位置：Section 5.4, Section 6 第 1 段, Appendix B.12 Table B.6 及 §Confounds\n- 问题：14B 实验同时改变了 5 个变量：model family, tokenizer, training data, reference model, model scale。Appendix B.12 §Confounds 承认 \"infeasible to attribute the observed accuracy gap to any single factor\"，但 Section 5.4 和 Section 6 仍声称 \"signal persists at 14B\"。当 EDD=0 时，声称 \"d1-d3 discrimination persists\" 与 EDD 指标的定义矛盾。\n- 建议修改方向：(1) 将标题改为更明确的 caveat；(2) Section 6 中不应使用 \"persists\"；(3) 加入 Pythia-referenced pipeline 以隔离混淆。\n\n### Should-Fix 问题\n\n**W1** Self-reference 混淆使 3×3 atlas 内部不可比\n- Pythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp。Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%。\n- 建议：增加 cross-reference accuracy 列，或明确声明 Pythia 行可比性受限。\n\n**W2** Cross-strategy transfer d1-d3 仅 45.9%（1.38× chance），实用性存疑\n- d1/d2 boundary inversion（AUC<0.5）意味着系统在某些 strategy 下会系统性地反转深度判断。Two-stage pipeline 回收 11.5pp 但未报告 strategy classifier 准确率。\n- 建议：报告 strategy classifier 准确率；在 Discussion 中列为部署前提条件。\n\n**W3** 单一 LoRA 超参配置无 sensitivity analysis\n- 不同 LoRA rank 可能产生不同的 distributional shift patterns。论文在 Limitations 中承认但未提供 sensitivity analysis。\n- 建议：至少一个 cell 提供 r∈{4,8,16,32} 的 sensitivity analysis。\n\n**W4** Cross-seed replication 不充分（3/9 cells），OLMo +3.17pp 非重叠 CI\n- 仅 nucleus cells 有 2-seed replication。OLMo CI 不重叠（+3.17pp）。温度和 top-k 完全未复制。\n- 建议：所有 9 cells 提供 cross-seed replication。\n\n**W5** EDD T=0.70 阈值选择缺乏充分依据\n- \"选择一个让大多数 cells 看起来好的阈值\" 是循环论证。\n- 建议：提供 principled justification 或定位为 \"illustrative\"。\n\n**W6** Perturbation-based baselines 从 binary → ordinal 的适配不充分\n- DetectGPT 和 Min-K% Prob 从未被设计用于序数深度估计，28-33% 可能反映适配方法的局限。\n- 建议：注明适配来源，加入 binary d0-vs-d1+ 性能作为 sanity check。\n\n**W7** Curation PoC 主结论非显著（p>0.4），存在多重比较问题\n- RF-filtered vs unfiltered 主假设不成立。Bonferroni 校正后仅 1/3 存活。\n- 建议：标题改为 \"Curation PoC (Inconclusive)\"。\n\n### Minor 问题\n- Table 4 中 Binoculars 78.1% 的 11-feat 配置未出现在 table 中\n- 7 条引用在 OpenAlex 未找到（索引问题，非虚构）；4 条 year/author mismatch\n- Appendix B.12 中 7-8B 使用 QLoRA 但未标注\n- Mean perplexity 代表 \"surface-text ablation\" 低估了简单 baselines（p90_ppl alone 58.3%）\n- Heterogeneous chain 的 confound（architecture identity ≡ depth）未完全排除\n\n### 主要优势\n1. 问题定义新颖且有价值\n2. Benchmark 设计系统（180K 样本，domain bias 修复透明披露）\n3. EDD 指标有概念贡献\n4. Feature analysis 深入且一致（Kendall's W=0.90）\n5. Limitations 异常全面（10+ 个 limitations）\n6. Appendix 丰富（15 页，23 个子实验）\n\n### Missing References\n- SeqXGPT（sentence-level attribution）\n- Table 4 中应加入 XGBoost 和 Ordinal MLP 的 cross-model transfer 结果\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和 Minor 问题。对每条明确标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-20T06:40:06.254654+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 44581
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-20T06:40:06.658123+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与完整性）的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）\n\n### 总体评分\n**Overall**: 3.0 / 5（Findings 级别）\n**一句话总结**: 任务定义新颖且实验设计系统，但方法贡献有限（标准 RF + 标准特征），scale generalization 在 14B 时崩塌（EDD=0），full-replacement 假设严重限制生态效度，综合来看达到 Findings 标准但不足以被主会议接收。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论严谨（5-fold CV, 多 seed, bootstrap CI），但 full-replacement 假设与 real-world accumulation 场景差距过大，14B 结果（EDD=0）与 \"signal persists\" 叙事存在张力 |\n| Excitement | 2.5/5 | 任务定义有意义且时机恰当（model collapse 话题热度高），但执行层面无算法创新，RF+统计特征是成熟方法的直接应用；cross-transfer 性能较弱限制实用价值 |\n| Reproducibility | 4.0/5 | LoRA 训练协议（Appendix A）、特征定义（Table 1）、超参数均有详细记录；承诺释放代码和数据；随机种子有报告 |\n| Overall Assessment | 3.0/5 | Findings 可接收：新颖任务形式化 + 系统实证分析，但缺乏方法论贡献、scale 受限、实用性存疑 |\n| Confidence | 4/5 | 熟悉 AI text detection 和 model collapse 文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] Scale generalization 的叙事与证据之间存在系统性张力\n- Abstract 声称 fingerprints \"are consistent in direction but scale-dependent in magnitude\"，但 14B 结果 EDD=0，4-class 准确率仅 50.8%（2× chance）。7-8B 优于 chance 但未重新训练分类器。在实际关心的模型规模（≥14B）上方法实用性未经验证。\n- 建议：(1) Abstract 和 Introduction 中明确声明 14B EDD=0；(2) §5.4 扩展到主体正文；(3) 讨论 14B EDD=0 的可能原因及缓解方向。\n\n**N2** [critical] Full-replacement 假设严重限制生态效度\n- 所有实验使用 full-replacement 递归链。Gerstgrasser et al. (2024) 已证明 accumulation 可避免 collapse。如果深度信号仅在 replacement 场景下明显，整个方法的应用前景不明。Curation PoC（Appendix B.22）结果 inconclusive。\n- 建议：(1) 增加 partial-mixing 实验（50% synthetic + 50% real）；(2) 如无法实验，在 Discussion 中深入分析。\n\n**N3** [critical] 算法贡献有限，论文定位需要更谨慎\n- 核心方法是标准 RF + 19 个标准统计特征。所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等）。DeBERTa-v3 端到端基线反而低于 RF。论文在 p.2 称 \"our contribution centers on task formalization and systematic empirical characterization\"，定位诚实，但 Findings 级别也需要 non-trivial 的方法论 insight。\n- 建议：(1) 深入分析为什么 RF 大幅优于 neural 方法；(2) 加强 EDD 的 formalization 使其成为更有理论深度的贡献。\n\n### Should-Fix 问题\n\n**W1** Abstract 信息过载，核心信息被淹没\n- Abstract 包含过多具体数字（\"180K-passage\", \"three model families\", \"19 statistical features\", 多个百分比），核心贡献被稀释。\n- 建议：精简到 1-2 个 headline 数字。\n\n**W2** Discussion 过于单薄，核心洞察被放逐到 Appendix\n- §6 约 1 页，混合讨论和结论。关键分析（multi-channel encoding, RF vs neural, curation PoC, cross-scale）全在 Appendix。\n- 建议：将 Appendix B.9 和 B.22 核心结论提升到主体。\n\n**W3** \"Depth Degradation Atlas\" 作为概念贡献被过度包装\n- \"Atlas\" 暗示全面参考地图，但实际是 3×3 grid 的 empirical evaluation。\n- 建议：使用更准确术语如 \"systematic empirical analysis\"。\n\n**W4** Cross-model 和 cross-strategy transfer 性能较弱但讨论不足\n- 用户需要先知道是哪个模型、哪种解码策略才能选择正确分类器，限制 blind deployment 实用性。\n- 建议：Discussion 增加 practical deployment constraints 分析。\n\n**W5** Curation PoC 结果 inconclusive 但论文仍暗示为 contribution\n- d0-only 非最低 PPL，单次实验缺乏统计显著性，但 §6 语气偏乐观。\n- 建议：明确定调为 preliminary/inconclusive。\n\n### Minor 问题\n- M1: 部分 bib entry 年份不匹配（he2021_deberta_v3, alemohammad2024_mad, guo2024_biscope）\n- M2: gerstgrasser2024_accumulate 和 briesch2024selfconsuming 应更新为 inproceedings\n- M3: AI 写作痕迹（-ing 分词短语多处出现）\n- M4: Figure 1 heatmap 色彩对比度有限\n- M5: 脚注 1 中 binary EDD 500 trees vs multi-class 200 trees 未解释\n\n### 主要优势\n1. 任务定义的新颖性和时效性\n2. 实验设计的系统性（3×3×4 full grid + thorough appendix）\n3. Perplexity tail insight 的理论连接\n4. 诚实的局限性声明\n5. 相关工作覆盖全面（68 篇引用，0 orphan/0 missing）\n6. Strategy-dependent trajectory 的发现\n\n### Claim-Evidence 匹配分析\n- \"59–82% four-class accuracy\" ✅ 匹配\n- \"perplexity tail family dominates\" ✅ 匹配\n- \"consistent in direction but scale-dependent\" ⚠️ 14B EDD=0 使表述存疑\n- \"signal persists at larger scales\" ⚠️ 50.8% 仅 2× chance\n- \"cross-model transfer 66.4%\" ✅ 匹配但应突出 worst case\n- \"curation PoC\" ⚠️ inconclusive 但语气偏乐观\n\n### 可能遗漏的相关工作\n1. PAN 2026 Shared Task（Generative Plagiarism Detection）\n2. TROVE (NAACL 2025?) 和 GenProve (2026) — fine-grained text provenance\n3. \"Collapse or Thrive?\" (arXiv:2410.16713, 2024) — synthetic data survey\n4. \"Rate of Model Collapse in Recursive Training\" (arXiv:2412.17646, 2024) — collapse 速率理论\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和 Minor 问题。对每条明确标注 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性与完整性）的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告（新颖性与完整性）\n\n### 总体评分\n**Overall**: 3.0 / 5（Findings 级别）\n**一句话总结**: 任务定义新颖且实验设计系统，但方法贡献有限（标准 RF + 标准特征），scale generalization 在 14B 时崩塌（EDD=0），full-replacement 假设严重限制生态效度，综合来看达到 Findings 标准但不足以被主会议接收。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论严谨（5-fold CV, 多 seed, bootstrap CI），但 full-replacement 假设与 real-world accumulation 场景差距过大，14B 结果（EDD=0）与 \"signal persists\" 叙事存在张力 |\n| Excitement | 2.5/5 | 任务定义有意义且时机恰当（model collapse 话题热度高），但执行层面无算法创新，RF+统计特征是成熟方法的直接应用；cross-transfer 性能较弱限制实用价值 |\n| Reproducibility | 4.0/5 | LoRA 训练协议（Appendix A）、特征定义（Table 1）、超参数均有详细记录；承诺释放代码和数据；随机种子有报告 |\n| Overall Assessment | 3.0/5 | Findings 可接收：新颖任务形式化 + 系统实证分析，但缺乏方法论贡献、scale 受限、实用性存疑 |\n| Confidence | 4/5 | 熟悉 AI text detection 和 model collapse 文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] Scale generalization 的叙事与证据之间存在系统性张力\n- Abstract 声称 fingerprints \"are consistent in direction but scale-dependent in magnitude\"，但 14B 结果 EDD=0，4-class 准确率仅 50.8%（2× chance）。7-8B 优于 chance 但未重新训练分类器。在实际关心的模型规模（≥14B）上方法实用性未经验证。\n- 建议：(1) Abstract 和 Introduction 中明确声明 14B EDD=0；(2) §5.4 扩展到主体正文；(3) 讨论 14B EDD=0 的可能原因及缓解方向。\n\n**N2** [critical] Full-replacement 假设严重限制生态效度\n- 所有实验使用 full-replacement 递归链。Gerstgrasser et al. (2024) 已证明 accumulation 可避免 collapse。如果深度信号仅在 replacement 场景下明显，整个方法的应用前景不明。Curation PoC（Appendix B.22）结果 inconclusive。\n- 建议：(1) 增加 partial-mixing 实验（50% synthetic + 50% real）；(2) 如无法实验，在 Discussion 中深入分析。\n\n**N3** [critical] 算法贡献有限，论文定位需要更谨慎\n- 核心方法是标准 RF + 19 个标准统计特征。所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等）。DeBERTa-v3 端到端基线反而低于 RF。论文在 p.2 称 \"our contribution centers on task formalization and systematic empirical characterization\"，定位诚实，但 Findings 级别也需要 non-trivial 的方法论 insight。\n- 建议：(1) 深入分析为什么 RF 大幅优于 neural 方法；(2) 加强 EDD 的 formalization 使其成为更有理论深度的贡献。\n\n### Should-Fix 问题\n\n**W1** Abstract 信息过载，核心信息被淹没\n- Abstract 包含过多具体数字（\"180K-passage\", \"three model families\", \"19 statistical features\", 多个百分比），核心贡献被稀释。\n- 建议：精简到 1-2 个 headline 数字。\n\n**W2** Discussion 过于单薄，核心洞察被放逐到 Appendix\n- §6 约 1 页，混合讨论和结论。关键分析（multi-channel encoding, RF vs neural, curation PoC, cross-scale）全在 Appendix。\n- 建议：将 Appendix B.9 和 B.22 核心结论提升到主体。\n\n**W3** \"Depth Degradation Atlas\" 作为概念贡献被过度包装\n- \"Atlas\" 暗示全面参考地图，但实际是 3×3 grid 的 empirical evaluation。\n- 建议：使用更准确术语如 \"systematic empirical analysis\"。\n\n**W4** Cross-model 和 cross-strategy transfer 性能较弱但讨论不足\n- 用户需要先知道是哪个模型、哪种解码策略才能选择正确分类器，限制 blind deployment 实用性。\n- 建议：Discussion 增加 practical deployment constraints 分析。\n\n**W5** Curation PoC 结果 inconclusive 但论文仍暗示为 contribution\n- d0-only 非最低 PPL，单次实验缺乏统计显著性，但 §6 语气偏乐观。\n- 建议：明确定调为 preliminary/inconclusive。\n\n### Minor 问题\n- M1: 部分 bib entry 年份不匹配（he2021_deberta_v3, alemohammad2024_mad, guo2024_biscope）\n- M2: gerstgrasser2024_accumulate 和 briesch2024selfconsuming 应更新为 inproceedings\n- M3: AI 写作痕迹（-ing 分词短语多处出现）\n- M4: Figure 1 heatmap 色彩对比度有限\n- M5: 脚注 1 中 binary EDD 500 trees vs multi-class 200 trees 未解释\n\n### 主要优势\n1. 任务定义的新颖性和时效性\n2. 实验设计的系统性（3×3×4 full grid + thorough appendix）\n3. Perplexity tail insight 的理论连接\n4. 诚实的局限性声明\n5. 相关工作覆盖全面（68 篇引用，0 orphan/0 missing）\n6. Strategy-dependent trajectory 的发现\n\n### Claim-Evidence 匹配分析\n- \"59–82% four-class accuracy\" ✅ 匹配\n- \"perplexity tail family dominates\" ✅ 匹配\n- \"consistent in direction but scale-dependent\" ⚠️ 14B EDD=0 使表述存疑\n- \"signal persists at larger scales\" ⚠️ 50.8% 仅 2× chance\n- \"cross-model transfer 66.4%\" ✅ 匹配但应突出 worst case\n- \"curation PoC\" ⚠️ inconclusive 但语气偏乐观\n\n### 可能遗漏的相关工作\n1. PAN 2026 Shared Task（Generative Plagiarism Detection）\n2. TROVE (NAACL 2025?) 和 GenProve (2026) — fine-grained text provenance\n3. \"Collapse or Thrive?\" (arXiv:2410.16713, 2024) — synthetic data survey\n4. \"Rate of Model Collapse in Recursive Training\" (arXiv:2412.17646, 2024) — collapse 速率理论\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和 Minor 问题。对每条明确标注 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-20T06:40:08.322904+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1664
}
```

</details>

---


### Assistant

_source line 1206 · 2026-05-20T06:40:11.121517+00:00_

交叉分享已分发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1207 · 2026-05-20T06:40:14.141265+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

**审稿结论**：Overall 3.0（Findings 级别）。

三个 Must-Fix 问题：
1. **Scale generalization 叙事与证据张力**：14B EDD=0，方法在大模型上实用性未验证，但论文叙事偏乐观
2. **Full-replacement 假设限制生态效度**：与 real-world accumulation 场景差距过大，curation PoC inconclusive
3. **算法贡献有限**：标准 RF + 已有统计特征，无方法论创新

四个 Should-Fix 问题涉及 Abstract 信息过载、Discussion 单薄、"Atlas" 命名过度包装、cross-transfer 性能弱但讨论不足。

引用完整性方面，68 篇引用全部真实存在（0 orphan / 0 missing），建议补充 PAN 2026 shared task、TROVE/GenProve 等近期 provenance 工作。格式合规无问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1208 · 2026-05-20T06:40:18.712014+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1209 · 2026-05-20T06:42:22.657902+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2（新颖性与完整性）审稿意见的逐条回应

---

### 总体评分
[AGREE] R2 的 Overall 3.0 (Findings) 评分。我给出了相同分数，理由高度重叠：任务定义新颖、benchmark 系统，但方法贡献有限、scale generalization 不足、cross-transfer 实用性存疑。

---

### Must-Fix 问题

**[AGREE] R2-N1: Scale generalization 叙事与证据的系统性张力**

完全同意。我在自己的 N3 中提出了本质相同的问题。补充两点 R2 未明确提到的证据：

(1) 14B 实验的内部不一致更深层：论文自己定义的 EDD 指标（Section 3.4 Definition 1）在 14B 上报告 EDD=0，这意味着按照论文自己的度量标准，14B 文本的相邻深度不可判别。但 Section 6 第 1 段仍写 "d1-d3 discrimination persists with strategy-specific AUC patterns"——这与 EDD=0 的定义矛盾。

(2) Table B.6 中 14B 的 d0v1 AUC（0.561-0.643）远低于 1-1.5B 的 >0.99。考虑到 d0/d1 boundary 是整个框架中最容易的判别（human vs first-gen），这个 boundary 的崩塌比 d1-d3 的困难更值得关注——它暗示 14B 的 depth signal 可能根本是不同性质的，而非同一信号的 scale-dependent attenuation。

**[REBUT] R2-N2: Full-replacement 假设严重限制生态效度 → 不同意 "critical" 严重度**

R2 将此标为 critical，我认为应降为 Should-Fix，理由如下：

(1) Full-replacement 是研究递归生成深度的 *必要起点*。正如 controlled experiment 需要隔离变量，full-replacement 消除了 mixing ratio 这个连续混淆变量，使 depth 成为唯一自变量。论文明确声明 "Our results therefore represent an upper bound on feature separability"（Limitations §1），定位为 upper bound 而非 real-world deployment 方案。

(2) Gerstgrasser et al. (2024) 证明 accumulation 可避免 collapse，但这恰恰说明 full-replacement 场景下 depth signal 更强——论文选择 signal 最强的设定来建立 feasibility，再逐步推广，是合理的研究策略。

(3) 论文已有 partial evidence：prompted generation（Appendix B.22, Table B.15: 69.5%, -13.8pp）和 mixed-depth corpus（Appendix B.14: macro-recall Δ=-1.62pp）提供了部分 relaxation。完整的 accumulation 实验确实重要，但其缺失不构成对当前贡献的否定——它是 future work，不是 fatal flaw。

(4) 作为 Findings 论文，在 controlled setting 下建立 feasibility + 系统实证分析已足够。要求 accumulation 实验等同于要求一篇论文同时解决 controlled 和 wild 场景。

建议维持 Should-Fix：在 Discussion 中加深 accumulation 场景的分析，但不需要新实验。

**[AGREE with nuance] R2-N3: 算法贡献有限**

同意 R2 的判断，但有细微差异：

(1) 同意 "RF + 19 标准特征" 本身无算法创新。但 R2 声称 "所有特征在 detection 文献中已有广泛使用（GLTR, Ghostbuster 等）" 不完全准确。GLTR 和 Ghostbuster 使用的是 token-level log-probability 和 per-token rank 特征，而本文的 *passage-level distributional statistics*（p90_ppl, var_surprisal, kurtosis_ppl）是对 token-level 信号的 distributional aggregation——这是一个非 trivial 的特征工程选择，并且论文展示了为什么这种 aggregation 有效（tail erosion 理论，Section 3.5）而 token-level 方法（DetectGPT 28.8%, Min-K% 33.2%）失败。

(2) 同意 EDD 的 formalization 有改进空间。当前定义（Definition 1, Section 3.4）的 contiguous prefix 要求在 non-monotonic 场景下过于保守（如论文自己在 Limitations 中承认）。如果 EDD 能处理 non-contiguous discriminable regions，将显著增强理论贡献。

(3) R2 建议 "深入分析为什么 RF 大幅优于 neural 方法" ——我强烈支持。论文有 partial 分析（Appendix B.7 feature overlap analysis: PLM [CLS] representations yield negative R² for var_surprisal and p90_ppl），但这个结果非常有趣且未在主文中充分展开。如果加强为 "perplexity tail statistics are not linearly accessible in pretrained representation space"，这可以成为一个有价值的 insight。

---

### Should-Fix 问题

**[REBUT] R2-W1: Abstract 信息过载**

不同意。ACL/EMNLP 的 abstract 惯例允许甚至鼓励包含具体数字以便检索和快速评估。我审查的 abstract 中的 key numbers（180K, 3 model families, 59-82%, 9-cell grid）每个都 serve a specific purpose：benchmark scale, generalization scope, performance range, experimental design。问题不在于数字过多，而在于 *which* numbers are highlighted——正如我在 N1 中指出，d1-d3 balanced accuracy 应与 four-class accuracy 并列呈现，而非用 four-class 单独 headline。

**[AGREE] R2-W2: Discussion 过于单薄**

同意。Section 6 约 1 页，混合了 summary 和 discussion。关键分析（multi-channel encoding 分解、RF vs neural 的 representational gap、cross-scale 趋势的 theoretical implications）全在 Appendix。建议将 Appendix B.7（feature overlap analysis）和 B.17（Binoculars signal decomposition）的核心结论提升到 Section 6，使 discussion 更有理论深度。

**[REBUT] R2-W3: "Depth Degradation Atlas" 过度包装**

不完全同意。"Atlas" 在计量学和系统生物学中指 systematic empirical map across a parameter grid——论文的 3 model families × 3 strategies × 4 depths × 19 features 的系统性评估，加上跨维度的 consistency analysis（feature rank correlation ρ̄=0.868, Table 3）和 sensitivity analysis（EDD at multiple thresholds），符合 "atlas" 的使用惯例。如果只是单一模型的 accuracy table，称 "atlas" 确实过度；但 9 cells 的完整交叉分析 + feature trajectory + EDD decay curve + importance heatmap（Figure 1）构成了一个有参考价值的 empirical map。

不过 R2 说 "暗示全面参考地图" 有道理——3×3 grid 的覆盖范围确实有限（3 个 model families 均为 1-1.5B，且仅 nucleus/temp/top-k 三种 strategy）。建议折中：保留 "atlas" 但在首次使用时加注 scope（"a 3×3 atlas at the 1-1.5B scale"）。

**[AGREE] R2-W4: Cross-model 和 cross-strategy transfer 性能较弱但讨论不足**

同意。我在 W2 中提出了类似问题。补充一个 R2 未明确提到的点：two-stage pipeline（strategy identification + depth classification）回收 11.5pp，但论文未报告 strategy classifier 本身的准确率。如果 strategy identification 本身不可靠，two-stage pipeline 的实际增益会打折扣。这是 deployment feasibility 的关键缺失。

**[AGREE] R2-W5: Curation PoC 结果 inconclusive 但论文仍暗示为 contribution**

完全同意。我在 W7 中提出了相同问题。RF-vs-unfiltered p=0.407，主假设不成立。Bonferroni 校正后仅 1/3 RF-vs-random comparisons 存活（Appendix B.23 自己承认）。Section 6 和 Appendix B.23 的措辞（"inconclusive preliminary evidence"）已比早期版本改善，但 Appendix B.10 的标题（"Downstream Curation PoC"）和呈现方式仍可能给 skimming reader 留下 positive 印象。

---

### Minor 问题

**[AGREE] R2-M1**: bib 年份不匹配。我在引用验证中也发现了相同问题（he2021_deberta_v3: bib=2023 vs actual=2021; alemohammad2024_mad: first author mismatch; guo2024_biscope: first author mismatch）。

**[AGREE] R2-M2**: gerstgrasser2024_accumulate 等应从 misc 更新为 inproceedings（如已被会议接收）。

**[REBUT] R2-M3: AI 写作痕迹（-ing 分词短语）**

不同意将此列为问题。-ing participial phrases 是学术英语中的标准构造（如 "confirming that...", "suggesting that...", "indicating that..."），在 NLP/ML 论文中普遍使用。Ethics Statement 透明披露了 "This research used AI coding assistants for experiment implementation and writing drafts"（p.10）。除非 R2 能指出具体的不自然表述，仅以 -ing 频率为由标记 "AI 写作痕迹" 缺乏依据，且与 double-blind review 的精神相悖（不应基于写作风格推断作者身份或工具使用）。

**[AGREE] R2-M4**: Figure 1 heatmap 对比度有限。从 PDF 视觉检查来看，低 importance 值之间的颜色区分确实不够明显。

**[AGREE] R2-M5**: 脚注 1 中 EDD binary classifier 使用 500 trees vs main 4-class RF 200 trees，未解释原因。这是一个合理的实验设计问题——不同 tree 数量可能影响 AUC 估计，且 EDD 的 AUC 阈值判定对 classifier capacity 敏感。

---

### Claim-Evidence 匹配分析

[AGREE] R2 的所有 6 条 claim-evidence 匹配判断。特别强调：

- "signal persists at larger scales" ⚠️：这与我的 N3 一致。50.8% (2× chance) 在 5 个混淆变量下不能归因于 depth signal。
- "curation PoC" ⚠️：p>0.4 的主假设检验不成立，应明确标记为 inconclusive。

---

### 可能遗漏的相关工作

**[AGREE]** R2 建议补充的 4 篇参考文献均有道理：
1. PAN 2026 (Generative Plagiarism Detection) — 如果确实存在该 shared task，直接相关
2. TROVE / GenProve — fine-grained text provenance，与论文的 depth estimation 互补
3. "Collapse or Thrive?" — synthetic data survey，可丰富 Related Work
4. "Rate of Model Collapse in Recursive Training" — collapse 速率理论，可能与 EDD upper bound 分析（Section 3.5）直接相关

建议作者核实这些参考文献的可用性并酌情补充。

---

### 与我审稿的一致性和差异

**高度一致的判断**：
- 14B "signal persists" overclaiming（R2-N1 ≈ 我的 N3）
- d0 inflation（R2 在 claim-evidence 中提及，我的 N1 更详细）
- Curation PoC inconclusive（R2-W5 ≈ 我的 W7）
- Cross-transfer 实用性不足（R2-W4 ≈ 我的 W2）
- 最终评分完全一致（3.0 Findings）

**R2 强调而我未充分覆盖的**：
- Full-replacement 生态效度（R2-N2）——我认为严重度应低于 R2 的判定
- Discussion 单薄 / Appendix-heavy 结构（R2-W2）——我同意但在我的审稿中未单独列出

**我强调而 R2 未充分覆盖的**：
- Binoculars parity（我的 N2）：78.4% vs 78.1% (p>0.05) 是方法论贡献的核心挑战，R2 未提及
- Self-reference confound（我的 W1）：Pythia-1.4B 同时作为 reference 和 generator，4-11pp 优势使 atlas 内部不可比
- EDD T=0.70 阈值选择缺乏依据（我的 W5）
- 单一 LoRA 配置无 sensitivity（我的 W3）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1210 · 2026-05-20T06:42:29.162406+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1211 · 2026-05-20T06:42:31.992747+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。

核心判断：与 R2 在 Overall 评分（3.0 Findings）和多数问题上高度一致，尤其是 14B overclaiming、curation PoC inconclusive、cross-transfer 实用性不足。主要分歧在两点：(1) full-replacement 假设我认为应降为 Should-Fix 而非 critical——作为 controlled study 的起点合理；(2) abstract 信息量我认为是风格偏好而非缺陷。另外我补充了 R2 未覆盖的 Binoculars parity（78.4% vs 78.1%）和 self-reference confound 两个问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1212 · 2026-05-20T06:42:36.882384+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 113

## Round 113

12 recorded events


### User

_source line 1213 · 2026-05-20T06:42:48.943376+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 逐条回应

**[AGREE] R1-N1: Headline metrics 被 d0 召回率系统性膨胀**

同意这是一个重要的 presentation 问题。d0（人类文本）召回率 >97%（Table 2）使得 4-class accuracy 的下限被系统性拉高。在 balanced 4-class 设定下，d0 贡献约 24.25%（0.25×97%）到总 accuracy，意味着最低 cell 的 d1-d3 平均准确率仅约 49%（(60.95−24.25)/0.75），与 33.3% chance 的差距远小于 headline 60.95% 暗示的效果。

但我补充一点：d0 IS 任务的合法类别——"估计递归生成深度"本身包含 d0 判定。问题不在于 metric 本身，而在于 **emphasis**。建议作者在 Abstract 和 §6 同时报告 4-class 和 d1-d3 balanced accuracy，使读者自行判断。R1 建议以 d1-d3 作为主指标偏激进——排除 d0 会人为重新定义任务。更合理的方案是**双指标并列**。

---

**[AGREE] R1-N2: 与 Binoculars 11-feature RF 无显著差异（78.4% vs 78.1%, p>0.05）**

同意这是一个严肃的 positioning 问题。我在审稿中注意到 Table 4 的 Binoculars 行仅列出了较弱配置（threshold 69.8%, RF 1-feat 63.7%），而 78.1% 的 11-feature RF 配置仅在 §5.1 正文中一句话提及（"Binoculars...calibrated with an 11-feature RF on per-token cross-perplexity scores, matches our pipeline within 0.3 pp (78.1% vs. 78.4%, p>0.05)"）。这种 presentation 策略——在 table 中放弱版本、在文本中轻描淡写强版本——降低了论文的透明度。

不过我对此的严重程度判断比 R1 略低。原因：(1) 论文的核心贡献是 task formulation 而非 beat SOTA；(2) 本文管线仅需单一 reference model（Pythia-1.4B），而 Binoculars 需要 observer-performer pair（两个模型），部署成本不同；(3) merged 30 features 达 82.6% 表明两个管线信号互补，本文特征捕获的是 distributional tail properties，Binoculars 捕获的是 cross-model divergence。但 R1 关于 Table 4 透明度的修改建议完全合理——应在表中加入 Binoculars 11-feat RF 行。

---

**[AGREE] R1-N3: 14B 实验严重混淆，"signal persists" claim 言过其实**

强烈同意，这与我 review 中 N1 的核心关切一致。我在审稿中指出 14B EDD=0 与 "signal persists" 叙事存在张力；R1 更进一步识别了混淆变量问题——14B 实验同时改变了 model family（Qwen vs Pythia/OLMo/GPT-2）、tokenizer、training data、reference model、model scale 五个变量。Appendix B.14 §Confounds 自己承认 "Four confounds limit the 7-8B results: (1) 4-bit NF4 QLoRA quantization (absent at 1-1.5B)" 和 "infeasible to attribute the observed accuracy gap to any single factor"，但 §5.4（p.8）和 §6 仍使用 "Depth signal persists at 14B" 的措辞，这在 Appendix 自己排除了因果推断能力的情况下是不恰当的。

R1 的建议——将 "persists" 改为更审慎的表述，并加入 Pythia-referenced pipeline 以隔离混淆——是完全合理且可操作的。

---

## Should-Fix 逐条回应

**[AGREE] R1-W1: Self-reference 混淆使 3×3 atlas 内部不可比**

同意。Pythia-1.4B 同时作为 generator 和 reference model（self-reference），而 OLMo 和 GPT-2 XL 使用 Pythia 作为 cross-reference。这引入了系统性偏差。论文在 p.10 确实提到了这一点（"For the Pythia pipeline this constitutes self-model feature extraction"），但未量化 self-reference advantage 的幅度。R1 估计 4-11pp 的差异是合理的推断（基于 §5.1 中 "same-family references yield optimal performance" 的讨论）。

建议在 Table 2 中标注哪些 cell 使用 self-reference vs cross-reference，或增加一列 cross-reference accuracy 用于公平对比。

---

**[AGREE] R1-W2: Cross-strategy transfer d1-d3 仅 45.9%（1.38× chance）**

同意。我在 review W4 中提出了同样的关切。d1-d3 balanced accuracy 45.9% 意味着在实际部署（不知道解码策略）场景下，方法几乎无法有效区分生成深度。R1 补充的 AUC<0.5（boundary inversion）问题更严重——系统会在某些策略下系统性地反转深度判断，这比随机猜测更危险。

对 R1 的补充建议：论文声称需要 two-stage pipeline（先识别策略再估计深度），但未报告 strategy classifier 的准确率。如果 strategy classification 本身不可靠，整个 two-stage 方案就不成立。

---

**[REBUT] R1-W3: 单一 LoRA 超参配置无 sensitivity analysis**

部分反驳。R1 的关切有道理——不同 LoRA rank 确实可能产生不同的 distributional shift patterns。但 LoRA 在这里的角色是 **benchmark 构建工具**（用于创建递归训练链），而非核心方法的一部分。论文的方法是分类器（RF + features），LoRA 只是用来制造不同深度的训练数据。Appendix A（p.13）记录了完整的 LoRA 配置（r=16, α=32, target modules, learning rate 等），Table 7 确认三个模型家族的超参一致。

更重要的是，如果 LoRA 配置改变导致深度信号消失，那说明的是信号对训练过程敏感，而非方法有缺陷。LoRA sensitivity analysis 属于 "nice to have" 而非 "must fix"——它回答的是 benchmark robustness 问题，不影响论文的核心 claim（"在给定 benchmark 上，深度信号存在且可被统计特征捕获"）。

但我同意至少应在 Limitations 中更明确地声明这一局限。

---

**[AGREE] R1-W4: Cross-seed replication 不充分（3/9 cells）**

同意。只有 nucleus 策略的 3 个 cell 有 2-seed replication（Appendix B.24），temperature 和 top-k 完全未复制。OLMo nucleus 的 CI 不重叠（+3.17pp）更令人担忧——这意味着在至少一个配置下，种子选择对结果有显著影响。对于一篇以系统性 benchmark 为核心贡献的论文，9/9 cells 都应有 cross-seed replication。

---

**[REBUT] R1-W5: EDD T=0.70 阈值选择缺乏充分依据**

部分反驳。R1 称这是 "循环论证"，但论文确实提供了 sensitivity analysis——§4.4（p.6）报告了 T ∈ {0.65, 0.70, 0.75, 0.80} 下的 EDD 变化，Appendix 提供了更详细的分析。此外，T=0.70 对应 AUC=0.70，这是 ROC 分析中 "adequate discrimination" 的常用经验阈值（AUC 0.7-0.8 = "acceptable"），并非凭空选择。

R1 的 concern 更准确地说是：论文没有显式引用这个经验标准的来源，也没有讨论不同应用场景下 T 的选择逻辑。建议在 §3.4 中增加一句引用 ROC 解释标准的文献（如 Hosmer & Lemeshow），并声明 T 的选择可按应用需求调整。

---

**[AGREE] R1-W6: Perturbation-based baselines 适配不充分**

同意。DetectGPT（28.8%）和 Min-K% Prob（33.2%）的低性能可能部分反映适配方法的局限而非方法本身的能力。论文将这些连续分数直接 bin 成 4 个深度类别，但最优 binning 策略不明。R1 建议增加 binary d0-vs-d1+ 性能作为 sanity check 是合理的——如果 DetectGPT 在 binary setting 下表现良好但 ordinal 下崩溃，说明适配方法有问题；如果 binary 下也差，说明这些方法确实不捕获深度信号。

---

**[AGREE] R1-W7: Curation PoC 主结论非显著（p>0.4）**

强烈同意。我在 review W5 中提出了同样的关切。RF-filtered vs unfiltered 的主假设不成立，单次实验无统计显著性。R1 进一步指出的 Bonferroni 校正问题加强了这一判断——多重比较使本已微弱的信号更不可靠。建议标题改为 "Curation PoC (Preliminary/Inconclusive)"，并在 §6 Discussion 中降低对 curation 应用的信心级别。

---

## Minor 逐条回应

**[AGREE] R1-Minor-1: Table 4 中 Binoculars 78.1% 的 11-feat 配置未出现**
与 N2 一致。Table 4 应包含这一配置。

**[AGREE] R1-Minor-2: 引用 year/author mismatch**
我在 review M1 中独立发现了同样的问题。

**[AGREE] R1-Minor-3: Appendix B.14 中 7-8B 使用 QLoRA 但未标注**
有效关切——QLoRA 量化会引入额外的 distributional shift，应在实验设置中明确标注。

**[AGREE] R1-Minor-4: Surface-text ablation 低估了简单 baselines**
R1 指出 p90_ppl 单特征达 58.3%，而论文用 mean perplexity（25.1%，等于 chance）作为 "surface-text ablation" 的代表。mean perplexity 是最弱的单特征，用它代表 surface-text baseline 确实低估了简单方法的能力。更公平的 ablation 应使用 best single feature（p90_ppl, 58.3%）作为下限。

**[REBUT] R1-Minor-5: Heterogeneous chain 的 architecture identity ≡ depth 混淆**
部分反驳。R1 担心异构链中 architecture identity 和 depth 混淆。但 Appendix B.15（p.19-20）的 heterogeneous chain 实验明确讨论了这一点——"depth ordering is preserved in every configuration" 且 "architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2 XL)"。论文 **确实承认了这个混淆**（p.19: "if the classifier exploited architecture fingerprints rather than depth signal..."），并通过反向链控制（reverse chain）验证了 85.7%的准确率，统计上与正向链不可区分（[81.0, 88.25]）。这不是完美的去混淆（因为样本量有限），但论文的处理比 R1 暗示的更充分。

---

## Missing References 回应

**[AGREE] R1-Missing-1: SeqXGPT（sentence-level attribution）**
合理建议。SeqXGPT 是 sentence-level 的 AI 文本检测方法，与 passage-level ordinal depth 任务相关但不直接竞争。应在 §2 Related Work 的 detection 子节中引用。

**[REBUT] R1-Missing-2: Table 4 中应加入 XGBoost 和 Ordinal MLP 的 cross-model transfer 结果**
理解意图但认为优先级不高。Table 4 的目的是对比不同 **方法类型**（RF vs neural vs perturbation-based vs membership inference）在 in-distribution 设定下的性能。Cross-model transfer 是独立维度，在 Table 5 中已有报告（虽然仅限 RF）。在 Table 4 中为每种方法加入 cross-model 列会使表格过于复杂。如果空间允许，可以在 Appendix 中增加。

---

## 总结

R1 的审稿整体质量很高，绝大多数 concerns 有据可查且可操作。我与 R1 在以下关键判断上 **高度一致**：

1. **d0 膨胀问题**（N1）——需要双指标并列报告
2. **Binoculars 对比透明度**（N2）——Table 4 应包含完整配置
3. **14B 混淆**（N3）——"persists" 措辞不当
4. **Curation PoC inconclusive**（W7）——需降调
5. **Cross-seed replication 不充分**（W4）——9/9 cells 均需覆盖

两处分歧：
- **LoRA sensitivity**（W3）：R1 将其列为 should-fix，我认为是 nice-to-have，因 LoRA 是 benchmark 构建工具而非方法的一部分
- **EDD 阈值**（W5）：T=0.70 有 ROC 经验标准支撑，但需要更明确的引用

**最终评分维持 Overall 3.0（Findings）**，与 R1 一致。核心限制是算法贡献缺失 + scale 受限 + 生态效度不足。如果 revision 能解决 d0 reporting、Binoculars transparency、14B caveat，可考虑 3.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-20T06:43:14.389721+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-20T06:43:14.542204+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T06:26:41.177490+00:00\", \"completed_at\": \"2026-05-20T06:30:18.480019+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主文（Sections 1–6）超出 8 页限制：Section 6 Discussion and Conclusion 从 page 8 底部延伸至 page 9 上半部（约半栏至一栏），Limitations 才在 page 9 中部开始。需压缩正文约 0.3–0.5 页以符合 EMNLP 2026 的 8-page limit。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1–3\", \"message\": \"连续 3 页纯文本，无任何 display item（figure/table/equation）。审稿人前 2 分钟看到的全是文字，缺乏视觉锚点，第一印象较弱。建议在 page 2 之前引入一张方法概览图或核心结果预览图。\"}, {\"severity\": \"warning\", \"dimension\": \"global\", \"message\": \"全文缺少方法 pipeline/概念图。论文提出 statistical fingerprint → RF classifier → EDD 的多阶段 framework，但无一张图展示端到端流程。审稿人需从纯文字中拼凑方法全貌，增加认知负担。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 3（3 个 confusion matrix）内部单元格数字字号偏小，在打印或低分辨率屏幕上可能难以辨认。建议增大 annotation 字号或简化为 heatmap 形式。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1（heatmap）Y 轴和 X 轴标签字号较小（约正文 60%），色彩梯度在灰度打印下区分度有限。建议加大 axis label 字号，或在 cell 内标注数值辅助阅读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（AUC decay curves）legend 字号偏小；三条线仅靠颜色区分，未使用不同 line style（dash/dot）。灰度打印或色盲场景下区分困难。建议添加 marker shape 或 line style 差异。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 4（appendix, feature trajectories）同样仅靠颜色区分多条线，建议补充 line style。\"}, {\"severity\": \"info\", \"dimension\": \"page 25\", \"message\": \"末页（Appendix B.29）内容仅占页面约 40%，大面积空白。Appendix 末页无硬性要求，但可考虑合并内容以节省页数。\"}, {\"severity\": \"info\", \"dimension\": \"pages 4–8\", \"message\": \"所有表格均使用 booktabs 风格（toprule/midrule/bottomrule），无竖线，最优值加粗标注——排版规范，符合顶会标准。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10–12\", \"message\": \"References 格式统一，无可见 [?] 未解析引用，编号连续，排版正常。\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-20T06:43:14.593090+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-20T06:43:14.643772+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-20T06:44:21.119672+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1219 · 2026-05-20T06:44:21.120150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-20T06:50:21.062317+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "issues_yaml": "issues:\n# ============================================================\n# CRITICAL ISSUES (影响接收决定)\n# ============================================================\n\n- id: R12-W4\n  summary: Cross-scale 14B 实验 5 重混淆，EDD=0 与 \"signal persists\" claim 矛盾\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.\n  - round: 13\n    reviewers: [1, 2]\n    note: 升级为 critical。论文已将标题改为 Preliminary，但 Abstract 仍言过其实。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14-R1-N3 和 R14-R2-N1 均列为 Must-Fix 且交叉完全一致。EDD=0 与 'persists' 措辞矛盾——论文自己的指标否定了自己的 claim。R1 补充: d0v1 AUC 降至 0.56-0.64 暗示 14B 信号可能是不同性质而非同一信号的 attenuation。§5.4 和 §6 仍使用 'persists'，Appendix §Confounds 承认无法归因但 headline 忽略限定。\"\n  action_items:\n  - round: 12\n    action: 降调 cross-scale 为 existence proof\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 13\n    action: Abstract 中将 14B 明确标记为 boundary condition\n    assigned_to: paper_agent\n    status: open\n  - round: 14\n    action: \"(1) §5.4 标题加强 caveat；(2) §6 用 'above-chance but cannot be attributed to depth signal due to multiple confounds' 替换 'persists'；(3) Abstract 明确声明 14B EDD=0\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W3\n  summary: Headline metrics 被 d0 召回率（>97%）系统性膨胀，d1-d3 balanced accuracy 被 bracket 化\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1-W3 和 R2-W6 完全一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善，已并列 d1-d3。R13-R1 仍列为 Must-Fix，R13-R2 降为 Should-Fix。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14-R1-N1 升为 Must-Fix，R2 AGREE。d0 贡献约 24.25% 到 4-class accuracy，最低 cell d1-d3 实际约 49%。Cross-model 66.4% 中 d1-d3 仅 55.4%（1.66x chance）。Pythia holdout d2 recall 仅 26.8%。Abstract/Introduction 仍以 4-class 为主指标。R2 补充: d0 是合法类别，问题在 emphasis 而非 metric 定义——应双指标并列而非以 d1-d3 为唯一主指标。从 warning 升级为 critical。\"\n  action_items:\n  - round: 12\n    action: 所有 headline 并列 d1-d3 balanced accuracy\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 13\n    action: Abstract 以 d1-d3 为主指标\n    assigned_to: paper_agent\n    status: resolved\n  - round: 14\n    action: \"Abstract 和所有 headline 处双指标并列（4-class + d1-d3 balanced accuracy），不排除 d0 但不让其膨胀印象\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-C1\n  summary: 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%, p>0.05），Table 4 呈现不透明\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-N2 Must-Fix，R2 AGREE（严重度略低但同意透明度修改）。Table 4 仅列 Binoculars 弱配置（threshold 69.8%, RF 1-feat 63.7%），78.1% 的 11-feat RF 仅在正文一句话中提及。Merged 30-feat 达 82.6%（+4.2pp）表明信号互补。R2 补充: 论文管线仅需单一 reference model（vs Binoculars observer-performer pair），这种部署优势应被明确论证。\"\n  action_items:\n  - round: 14\n    action: \"(1) Table 4 加入 Binoculars 11-feat RF 行并标注 p-value；(2) 正文论证部署优势（单一 reference model、可解释性）；(3) 将 merged 82.6% 作为推荐配置\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-C2\n  summary: 主文（§1-6）超出 8 页限制，§6 延伸至 page 9（约 0.3-0.5 页溢出）\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现。§6 Discussion and Conclusion 从 p.8 底部延伸至 p.9 上半部。Limitations 在 p.9 中部开始。EMNLP 2026 规定 long paper 正文严格 8 页，Limitations/Ethics 不计入但 Discussion 属正文。R2 格式检查误判为合规。\"\n  action_items:\n  - round: 14\n    action: 压缩正文约 0.3-0.5 页以符合 8-page limit\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# SHOULD-FIX ISSUES (影响评分但不一票否决)\n# ============================================================\n\n- id: R12-W1\n  summary: Full-replacement recursive chain 与真实 accumulation setting 存在结构性差异\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1-W1 和 R2-W2 均列为 Must-Fix。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善但核心问题未解决。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N2 列为 critical，R1 REBUT 降为 Should-Fix。R1 论证: full-replacement 是 controlled study 必要起点，upper bound 定位合理，prompted generation（69.5%）和 mixed-depth corpus 提供 partial relaxation。Director 裁定 Should-Fix——controlled study 起点选择合理，Findings 论文在 controlled setting 下建立 feasibility 已足够。\"\n  action_items:\n  - round: 12\n    action: Abstract/Introduction 添加 scope 限制声明\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 13\n    action: 补充 toy-scale accumulation 实验\n    assigned_to: paper_agent\n    status: open\n  - round: 14\n    action: Discussion 中加深 accumulation 场景分析（可无新实验但需更深入讨论）\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W9\n  summary: 算法贡献不足：标准 RF + 标准特征，论文定位需更谨慎\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R2 Must-Fix, R1 REBUT. Director 裁定 Should-Fix.\n  - round: 13\n    reviewers: [1, 2]\n    note: 论文已声明 empirical contribution 定位。分歧未解决。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N3 列为 critical，R1 AGREE with nuance。R1 指出 passage-level distributional aggregation（p90_ppl, var_surprisal）区别于 token-level 方法（GLTR/DetectGPT），是非 trivial 的特征工程选择。RF 大幅优于 neural（Appendix B.7: PLM representations yield negative R² for p90_ppl）值得在主文展开——'perplexity tail statistics not linearly accessible in pretrained representation space' 可成为有价值 insight。Director 维持 Should-Fix。\"\n  action_items:\n  - round: 12\n    action: Introduction 强化 empirical study 定位\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: 深入分析 RF vs neural representational gap（将 Appendix B.7 核心结论提升到主文）\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M3\n  summary: Reference model (Pythia-1.4B) 与 generator 重叠，self-reference 4-11pp 优势使 atlas 不可比\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Defer to rebuttal.\n  - round: 13\n    reviewers: [1, 2]\n    note: \"§3.4 'no systematic advantage' claim 与 Table 8 数据矛盾。升级为 critical。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W1 Should-Fix，R2 AGREE。§3.4 contradiction 已修复（R13-W1 resolved），但 atlas 内部不可比问题仍在: Table 2 Pythia 行 78.7% 在 cross-reference 下可能降至 68-75%。所有 cross-cell 比较基于不公平基础。降回 warning（§3.4 claim 已修复，剩余是 atlas 可比性问题）。\"\n  action_items:\n  - round: 12\n    action: DEFER to rebuttal\n    assigned_to: research_director\n    status: open\n  - round: 13\n    action: 修正 §3.4 claim\n    assigned_to: paper_agent\n    status: resolved\n  - round: 14\n    action: \"Table 2 增加 cross-reference accuracy 列或明确标注 Pythia 行可比性受限\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W2\n  summary: Cross-strategy transfer d1-d3 仅 45.9%（1.38x chance），d1/d2 boundary inversion\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 列为 Must-Fix。\n  - round: 13\n    reviewers: [1, 2]\n    note: 改善明显但部署价值仍受限。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W2 和 R2-W4 交叉一致。d1/d2 AUC<0.5 比随机猜测更危险。Two-stage pipeline 回收 11.5pp 但未报告 strategy classifier 准确率——如 strategy identification 不可靠则 two-stage 方案不成立。\"\n  action_items:\n  - round: 12\n    action: Abstract 并列 d1-d3 45.9%\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: \"(1) 报告 strategy classifier 独立准确率；(2) Discussion 中明确 'decoding strategy must be known or identifiable' 为部署前提\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells，OLMo +3.17pp 非重叠 CI\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R1-W7 Should-Fix，R2 AGREE。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W4 Should-Fix，R2 AGREE。仍仅 3/9 cells（nucleus only），temperature 和 top-k 完全未复制。OLMo CI 不重叠暗示种子选择对结果有显著影响。\"\n  action_items:\n  - round: 13\n    action: 至少对 3 个 temperature cells 补充 seed=43 replication\n    assigned_to: paper_agent\n    status: open\n  - round: 14\n    action: 所有 9 cells 提供 cross-seed replication；报告 importance 值的 seed-wise 标准差\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W7\n  summary: Discussion 过薄，核心洞察被放逐到 Appendix\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 从 ~80 词扩展到 ~250 词，部分改善。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-W2 warning，R1 AGREE。§6 约 1 页混合 discussion 和 conclusion。核心分析（multi-channel encoding, RF vs neural, cross-scale, curation）全在 Appendix。\"\n  action_items:\n  - round: 12\n    action: 扩展至 3-4 段\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: 将 Appendix B.7（RF vs neural feature overlap）和 B.17（Binoculars signal decomposition）核心结论提升到主文 Discussion\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W5\n  summary: Curation PoC 主比较不显著（p>0.4），但论文语气偏乐观\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 已标记 inconclusive，Bonferroni 表述部分修正。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W7 和 R2-W5 交叉一致。RF-vs-unfiltered p=0.407 主假设不成立。Bonferroni 后仅 1/3 存活。§6 仍称 'practical signal for data curation'，语气偏乐观。\"\n  action_items:\n  - round: 12\n    action: 标记为 inconclusive\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: \"Appendix B.10 标题改为 'Curation PoC (Inconclusive)'；§6 降低对 curation 应用的信心级别\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# MINOR / INFO ISSUES\n# ============================================================\n\n- id: R12-W6\n  summary: Abstract 信息过载（20+ 数字）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 未修复。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-W1 warning，R1 REBUT（ACL 惯例允许数字，问题在 which numbers 而非数量）。Director 降为 info——与 R12-W3（d0 inflation）合并处理即可。\"\n  action_items:\n  - round: 14\n    action: 与 d0 inflation 修改合并处理，无需单独精简数字\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M1\n  summary: EDD threshold T=0.70 选择需引用经验标准\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Minor issue.\n  - round: 13\n    reviewers: []\n    note: R13 未单独提出。已添加 sensitivity analysis。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W5 Should-Fix（循环论证），R2 partial REBUT（AUC=0.70 是 ROC 'adequate discrimination' 常用经验阈值）。Director 裁定 info——需引用文献（如 Hosmer & Lemeshow）但非循环论证。\"\n  action_items:\n  - round: 14\n    action: \"§3.4 增加一句引用 ROC 解释标准文献，声明 T 可按应用需求调整\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W5\n  summary: 单一 LoRA 超参配置（r=16, alpha=32），缺乏 sensitivity analysis\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1]\n    note: R1-W9 Minor。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W3 Should-Fix，R2 REBUT（LoRA 是 benchmark 构建工具非核心方法）。Director 裁定 info——在 Limitations 中更明确声明即可。\"\n  action_items:\n  - round: 14\n    action: Limitations 中更明确声明 single LoRA config 局限\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-W1\n  summary: Perturbation-based baselines（DetectGPT/Min-K%）从 binary 到 ordinal 适配不充分\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W6 Should-Fix，R2 AGREE。28-33% 可能反映适配方法局限而非方法本身。Min-K% augmented feature set +0.48pp 且排名 #3 说明确实携带互补信号。\"\n  action_items:\n  - round: 14\n    action: \"Table 4 注明 'adapted from binary detection'；增加 binary d0-vs-d1+ sanity check\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M6\n  summary: Bib entries 年份/作者 mismatch\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: c2pa2024 孤立 + 5 条 mismatch。\n  - round: 13\n    reviewers: [1, 2]\n    note: c2pa2024 已删除，但新发现 3 条孤儿引用。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1 和 R2 独立发现: he2021_deberta_v3 (bib=2023 vs actual=2021), alemohammad2024_mad (first author mismatch), guo2024_biscope (first author mismatch)。gerstgrasser2024_accumulate 和 briesch2024selfconsuming 应从 misc 更新为 inproceedings。\"\n  action_items:\n  - round: 14\n    action: 修正 3 条 year/author mismatch；更新 2 条 bib entry type\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-M1\n  summary: Surface-text ablation 用 mean perplexity（25.1%）代表低估简单 baselines（p90_ppl alone 58.3%）\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"Mean perplexity 是最弱单特征，用它代表 surface-text baseline 低估了简单方法。更公平的 ablation 应使用 best single feature。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R14-M2\n  summary: Figure 可读性问题（heatmap 灰度、线条仅靠颜色、confusion matrix 字号）\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [2]\n    note: \"R2-M4 + 视觉审查。Figure 1 灰度区分度有限；Figure 2/4 无 line style 差异；Figure 3 字号偏小。\"\n  action_items:\n  - round: 14\n    action: \"增加 line style（dash/dot）、加大 annotation 字号、考虑在 heatmap cell 内标注数值\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-M3\n  summary: 前 3 页无 display item + 缺少方法 pipeline 概念图\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现。pp.1-3 连续纯文本无视觉锚点。Statistical fingerprint -> RF -> EDD 的多阶段框架无图示。\"\n  action_items:\n  - round: 14\n    action: \"在 page 2 前引入方法概览图或核心结果预览图\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# RESOLVED / WONT_FIX (保留追踪)\n# ============================================================\n\n- id: R13-W1\n  summary: \"Reference model circularity: §3.4 'no systematic advantage' claim 与 Appendix H 数据矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R1-W1 Must-Fix，R2 完全 AGREE。\n  - round: 14\n    reviewers: []\n    note: \"R14 未重新提出 §3.4 specific claim 问题（R14 关注 atlas 可比性而非 §3.4 声明）。视为已修复。\"\n  action_items:\n  - round: 13\n    action: 修正 §3.4 claim\n    assigned_to: paper_agent\n    status: resolved\n  resolution: Fixed in D044 writing patch, verified by Reviewer\n  resolution_round: 13\n\n- id: R13-W2\n  summary: EDD contiguous prefix 在非单调 AUC 场景下过于保守\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R1-W6 Should-Fix，R2 AGREE。\n  action_items:\n  - round: 13\n    action: 提供补充指标（Maximum Discriminable Depth）\n    assigned_to: paper_agent\n    status: resolved\n  resolution: Fixed in D044 writing patch, verified by Reviewer\n  resolution_round: 13\n\n- id: R13-W4\n  summary: AI 写作痕迹（-ing 分词短语 20+ 次）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R2-W5 Should-Fix，R1 降为 Minor。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-M3 提及，R1 REBUT——标准学术英语，不应基于 -ing 频率标记 AI 写作。Director 不列入问题。维持 resolved。\"\n  action_items:\n  - round: 13\n    action: 改写 -ing 分词短语\n    assigned_to: paper_agent\n    status: resolved\n  resolution: Fixed in D044 writing patch, verified by Reviewer\n  resolution_round: 13\n\n- id: R12-M5\n  summary: Feature trajectory 图应从 Appendix 移回正文\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: REJECTED by Director — 页数限制不允许\n  action_items:\n  - round: 12\n    action: REJECT — 页数约束\n    assigned_to: research_director\n    status: open\n  resolution: Won't fix — page budget allocated to Discussion expansion instead\n  resolution_round: 12\n\n- id: R12-W8\n  summary: 多重共线性下 individual feature importance 不可靠\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1-W6 提出。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善，添加脚注 caveat 和 Kendall W 支持。\n  - round: 14\n    reviewers: []\n    note: \"R14 未单独提出此问题。可能已通过 R13 的修改充分解决，待 Research Director 确认。\"\n  action_items:\n  - round: 13\n    action: 将脚注 caveat 提升为正文段落\n    assigned_to: paper_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M2\n  summary: RF ordinal claim 过强\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Minor issue.\n  - round: 13\n    reviewers: []\n    note: 弱化为 ordinally consistent predictions + CORAL 匹配数据。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已修复，待确认。\"\n  action_items:\n  - round: 12\n    action: 弱化为 ordinally consistent predictions\n    assigned_to: paper_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M4\n  summary: Prompted generation 验证仅 1/9 cells\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Minor.\n  - round: 13\n    reviewers: [1, 2]\n    note: 已添加 single-cell qualifier。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已通过 qualifier 修复，待确认。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M7\n  summary: Feature extraction 'requires no GPU' 声明可能不准确\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1]\n    note: Agent 核实中。\n  - round: 13\n    reviewers: []\n    note: 已改为 '~2 min GPU, ~50 min CPU'。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已修复，待确认。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M8\n  summary: 遗漏引用 Muennighoff et al. (2024) + Ilyas et al. (2022)\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Agent 验证中。\n  - round: 13\n    reviewers: []\n    note: 两条引用已出现在 bib 和正文中。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已修复，待确认。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "issues_yaml": "issues:\n# ============================================================\n# CRITICAL ISSUES (影响接收决定)\n# ============================================================\n\n- id: R12-W4\n  summary: Cross-scale 14B 实验 5 重混淆，EDD=0 与 \"signal persists\" claim 矛盾\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.\n  - round: 13\n    reviewers: [1, 2]\n    note: 升级为 critical。论文已将标题改为 Preliminary，但 Abstract 仍言过其实。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14-R1-N3 和 R14-R2-N1 均列为 Must-Fix 且交叉完全一致。EDD=0 与 'persists' 措辞矛盾——论文自己的指标否定了自己的 claim。R1 补充: d0v1 AUC 降至 0.56-0.64 暗示 14B 信号可能是不同性质而非同一信号的 attenuation。§5.4 和 §6 仍使用 'persists'，Appendix §Confounds 承认无法归因但 headline 忽略限定。\"\n  action_items:\n  - round: 12\n    action: 降调 cross-scale 为 existence proof\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 13\n    action: Abstract 中将 14B 明确标记为 boundary condition\n    assigned_to: paper_agent\n    status: open\n  - round: 14\n    action: \"(1) §5.4 标题加强 caveat；(2) §6 用 'above-chance but cannot be attributed to depth signal due to multiple confounds' 替换 'persists'；(3) Abstract 明确声明 14B EDD=0\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W3\n  summary: Headline metrics 被 d0 召回率（>97%）系统性膨胀，d1-d3 balanced accuracy 被 bracket 化\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1-W3 和 R2-W6 完全一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善，已并列 d1-d3。R13-R1 仍列为 Must-Fix，R13-R2 降为 Should-Fix。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14-R1-N1 升为 Must-Fix，R2 AGREE。d0 贡献约 24.25% 到 4-class accuracy，最低 cell d1-d3 实际约 49%。Cross-model 66.4% 中 d1-d3 仅 55.4%（1.66x chance）。Pythia holdout d2 recall 仅 26.8%。Abstract/Introduction 仍以 4-class 为主指标。R2 补充: d0 是合法类别，问题在 emphasis 而非 metric 定义——应双指标并列而非以 d1-d3 为唯一主指标。从 warning 升级为 critical。\"\n  action_items:\n  - round: 12\n    action: 所有 headline 并列 d1-d3 balanced accuracy\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 13\n    action: Abstract 以 d1-d3 为主指标\n    assigned_to: paper_agent\n    status: resolved\n  - round: 14\n    action: \"Abstract 和所有 headline 处双指标并列（4-class + d1-d3 balanced accuracy），不排除 d0 但不让其膨胀印象\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-C1\n  summary: 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%, p>0.05），Table 4 呈现不透明\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-N2 Must-Fix，R2 AGREE（严重度略低但同意透明度修改）。Table 4 仅列 Binoculars 弱配置（threshold 69.8%, RF 1-feat 63.7%），78.1% 的 11-feat RF 仅在正文一句话中提及。Merged 30-feat 达 82.6%（+4.2pp）表明信号互补。R2 补充: 论文管线仅需单一 reference model（vs Binoculars observer-performer pair），这种部署优势应被明确论证。\"\n  action_items:\n  - round: 14\n    action: \"(1) Table 4 加入 Binoculars 11-feat RF 行并标注 p-value；(2) 正文论证部署优势（单一 reference model、可解释性）；(3) 将 merged 82.6% 作为推荐配置\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-C2\n  summary: 主文（§1-6）超出 8 页限制，§6 延伸至 page 9（约 0.3-0.5 页溢出）\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现。§6 Discussion and Conclusion 从 p.8 底部延伸至 p.9 上半部。Limitations 在 p.9 中部开始。EMNLP 2026 规定 long paper 正文严格 8 页，Limitations/Ethics 不计入但 Discussion 属正文。R2 格式检查误判为合规。\"\n  action_items:\n  - round: 14\n    action: 压缩正文约 0.3-0.5 页以符合 8-page limit\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# SHOULD-FIX ISSUES (影响评分但不一票否决)\n# ============================================================\n\n- id: R12-W1\n  summary: Full-replacement recursive chain 与真实 accumulation setting 存在结构性差异\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1-W1 和 R2-W2 均列为 Must-Fix。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善但核心问题未解决。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N2 列为 critical，R1 REBUT 降为 Should-Fix。R1 论证: full-replacement 是 controlled study 必要起点，upper bound 定位合理，prompted generation（69.5%）和 mixed-depth corpus 提供 partial relaxation。Director 裁定 Should-Fix——controlled study 起点选择合理，Findings 论文在 controlled setting 下建立 feasibility 已足够。\"\n  action_items:\n  - round: 12\n    action: Abstract/Introduction 添加 scope 限制声明\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 13\n    action: 补充 toy-scale accumulation 实验\n    assigned_to: paper_agent\n    status: open\n  - round: 14\n    action: Discussion 中加深 accumulation 场景分析（可无新实验但需更深入讨论）\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W9\n  summary: 算法贡献不足：标准 RF + 标准特征，论文定位需更谨慎\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R2 Must-Fix, R1 REBUT. Director 裁定 Should-Fix.\n  - round: 13\n    reviewers: [1, 2]\n    note: 论文已声明 empirical contribution 定位。分歧未解决。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N3 列为 critical，R1 AGREE with nuance。R1 指出 passage-level distributional aggregation（p90_ppl, var_surprisal）区别于 token-level 方法（GLTR/DetectGPT），是非 trivial 的特征工程选择。RF 大幅优于 neural（Appendix B.7: PLM representations yield negative R² for p90_ppl）值得在主文展开——'perplexity tail statistics not linearly accessible in pretrained representation space' 可成为有价值 insight。Director 维持 Should-Fix。\"\n  action_items:\n  - round: 12\n    action: Introduction 强化 empirical study 定位\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: 深入分析 RF vs neural representational gap（将 Appendix B.7 核心结论提升到主文）\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M3\n  summary: Reference model (Pythia-1.4B) 与 generator 重叠，self-reference 4-11pp 优势使 atlas 不可比\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Defer to rebuttal.\n  - round: 13\n    reviewers: [1, 2]\n    note: \"§3.4 'no systematic advantage' claim 与 Table 8 数据矛盾。升级为 critical。\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W1 Should-Fix，R2 AGREE。§3.4 contradiction 已修复（R13-W1 resolved），但 atlas 内部不可比问题仍在: Table 2 Pythia 行 78.7% 在 cross-reference 下可能降至 68-75%。所有 cross-cell 比较基于不公平基础。降回 warning（§3.4 claim 已修复，剩余是 atlas 可比性问题）。\"\n  action_items:\n  - round: 12\n    action: DEFER to rebuttal\n    assigned_to: research_director\n    status: open\n  - round: 13\n    action: 修正 §3.4 claim\n    assigned_to: paper_agent\n    status: resolved\n  - round: 14\n    action: \"Table 2 增加 cross-reference accuracy 列或明确标注 Pythia 行可比性受限\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W2\n  summary: Cross-strategy transfer d1-d3 仅 45.9%（1.38x chance），d1/d2 boundary inversion\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1 列为 Must-Fix。\n  - round: 13\n    reviewers: [1, 2]\n    note: 改善明显但部署价值仍受限。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W2 和 R2-W4 交叉一致。d1/d2 AUC<0.5 比随机猜测更危险。Two-stage pipeline 回收 11.5pp 但未报告 strategy classifier 准确率——如 strategy identification 不可靠则 two-stage 方案不成立。\"\n  action_items:\n  - round: 12\n    action: Abstract 并列 d1-d3 45.9%\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: \"(1) 报告 strategy classifier 独立准确率；(2) Discussion 中明确 'decoding strategy must be known or identifiable' 为部署前提\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W3\n  summary: Cross-seed replication 仅 3/9 cells，OLMo +3.17pp 非重叠 CI\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R1-W7 Should-Fix，R2 AGREE。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W4 Should-Fix，R2 AGREE。仍仅 3/9 cells（nucleus only），temperature 和 top-k 完全未复制。OLMo CI 不重叠暗示种子选择对结果有显著影响。\"\n  action_items:\n  - round: 13\n    action: 至少对 3 个 temperature cells 补充 seed=43 replication\n    assigned_to: paper_agent\n    status: open\n  - round: 14\n    action: 所有 9 cells 提供 cross-seed replication；报告 importance 值的 seed-wise 标准差\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W7\n  summary: Discussion 过薄，核心洞察被放逐到 Appendix\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 从 ~80 词扩展到 ~250 词，部分改善。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-W2 warning，R1 AGREE。§6 约 1 页混合 discussion 和 conclusion。核心分析（multi-channel encoding, RF vs neural, cross-scale, curation）全在 Appendix。\"\n  action_items:\n  - round: 12\n    action: 扩展至 3-4 段\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: 将 Appendix B.7（RF vs neural feature overlap）和 B.17（Binoculars signal decomposition）核心结论提升到主文 Discussion\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-W5\n  summary: Curation PoC 主比较不显著（p>0.4），但论文语气偏乐观\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 已标记 inconclusive，Bonferroni 表述部分修正。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W7 和 R2-W5 交叉一致。RF-vs-unfiltered p=0.407 主假设不成立。Bonferroni 后仅 1/3 存活。§6 仍称 'practical signal for data curation'，语气偏乐观。\"\n  action_items:\n  - round: 12\n    action: 标记为 inconclusive\n    assigned_to: paper_agent\n    status: in_progress\n  - round: 14\n    action: \"Appendix B.10 标题改为 'Curation PoC (Inconclusive)'；§6 降低对 curation 应用的信心级别\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# MINOR / INFO ISSUES\n# ============================================================\n\n- id: R12-W6\n  summary: Abstract 信息过载（20+ 数字）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: 一致。\n  - round: 13\n    reviewers: [1, 2]\n    note: 未修复。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-W1 warning，R1 REBUT（ACL 惯例允许数字，问题在 which numbers 而非数量）。Director 降为 info——与 R12-W3（d0 inflation）合并处理即可。\"\n  action_items:\n  - round: 14\n    action: 与 d0 inflation 修改合并处理，无需单独精简数字\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M1\n  summary: EDD threshold T=0.70 选择需引用经验标准\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Minor issue.\n  - round: 13\n    reviewers: []\n    note: R13 未单独提出。已添加 sensitivity analysis。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W5 Should-Fix（循环论证），R2 partial REBUT（AUC=0.70 是 ROC 'adequate discrimination' 常用经验阈值）。Director 裁定 info——需引用文献（如 Hosmer & Lemeshow）但非循环论证。\"\n  action_items:\n  - round: 14\n    action: \"§3.4 增加一句引用 ROC 解释标准文献，声明 T 可按应用需求调整\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R13-W5\n  summary: 单一 LoRA 超参配置（r=16, alpha=32），缺乏 sensitivity analysis\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1]\n    note: R1-W9 Minor。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W3 Should-Fix，R2 REBUT（LoRA 是 benchmark 构建工具非核心方法）。Director 裁定 info——在 Limitations 中更明确声明即可。\"\n  action_items:\n  - round: 14\n    action: Limitations 中更明确声明 single LoRA config 局限\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-W1\n  summary: Perturbation-based baselines（DetectGPT/Min-K%）从 binary 到 ordinal 适配不充分\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W6 Should-Fix，R2 AGREE。28-33% 可能反映适配方法局限而非方法本身。Min-K% augmented feature set +0.48pp 且排名 #3 说明确实携带互补信号。\"\n  action_items:\n  - round: 14\n    action: \"Table 4 注明 'adapted from binary detection'；增加 binary d0-vs-d1+ sanity check\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M6\n  summary: Bib entries 年份/作者 mismatch\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: c2pa2024 孤立 + 5 条 mismatch。\n  - round: 13\n    reviewers: [1, 2]\n    note: c2pa2024 已删除，但新发现 3 条孤儿引用。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1 和 R2 独立发现: he2021_deberta_v3 (bib=2023 vs actual=2021), alemohammad2024_mad (first author mismatch), guo2024_biscope (first author mismatch)。gerstgrasser2024_accumulate 和 briesch2024selfconsuming 应从 misc 更新为 inproceedings。\"\n  action_items:\n  - round: 14\n    action: 修正 3 条 year/author mismatch；更新 2 条 bib entry type\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-M1\n  summary: Surface-text ablation 用 mean perplexity（25.1%）代表低估简单 baselines（p90_ppl alone 58.3%）\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"Mean perplexity 是最弱单特征，用它代表 surface-text baseline 低估了简单方法。更公平的 ablation 应使用 best single feature。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R14-M2\n  summary: Figure 可读性问题（heatmap 灰度、线条仅靠颜色、confusion matrix 字号）\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [2]\n    note: \"R2-M4 + 视觉审查。Figure 1 灰度区分度有限；Figure 2/4 无 line style 差异；Figure 3 字号偏小。\"\n  action_items:\n  - round: 14\n    action: \"增加 line style（dash/dot）、加大 annotation 字号、考虑在 heatmap cell 内标注数值\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n- id: R14-M3\n  summary: 前 3 页无 display item + 缺少方法 pipeline 概念图\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"视觉审查发现。pp.1-3 连续纯文本无视觉锚点。Statistical fingerprint -> RF -> EDD 的多阶段框架无图示。\"\n  action_items:\n  - round: 14\n    action: \"在 page 2 前引入方法概览图或核心结果预览图\"\n    assigned_to: paper_agent\n    status: open\n  resolution: ''\n  resolution_round: null\n\n# ============================================================\n# RESOLVED / WONT_FIX (保留追踪)\n# ============================================================\n\n- id: R13-W1\n  summary: \"Reference model circularity: §3.4 'no systematic advantage' claim 与 Appendix H 数据矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R1-W1 Must-Fix，R2 完全 AGREE。\n  - round: 14\n    reviewers: []\n    note: \"R14 未重新提出 §3.4 specific claim 问题（R14 关注 atlas 可比性而非 §3.4 声明）。视为已修复。\"\n  action_items:\n  - round: 13\n    action: 修正 §3.4 claim\n    assigned_to: paper_agent\n    status: resolved\n  resolution: Fixed in D044 writing patch, verified by Reviewer\n  resolution_round: 13\n\n- id: R13-W2\n  summary: EDD contiguous prefix 在非单调 AUC 场景下过于保守\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R1-W6 Should-Fix，R2 AGREE。\n  action_items:\n  - round: 13\n    action: 提供补充指标（Maximum Discriminable Depth）\n    assigned_to: paper_agent\n    status: resolved\n  resolution: Fixed in D044 writing patch, verified by Reviewer\n  resolution_round: 13\n\n- id: R13-W4\n  summary: AI 写作痕迹（-ing 分词短语 20+ 次）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: R2-W5 Should-Fix，R1 降为 Minor。\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-M3 提及，R1 REBUT——标准学术英语，不应基于 -ing 频率标记 AI 写作。Director 不列入问题。维持 resolved。\"\n  action_items:\n  - round: 13\n    action: 改写 -ing 分词短语\n    assigned_to: paper_agent\n    status: resolved\n  resolution: Fixed in D044 writing patch, verified by Reviewer\n  resolution_round: 13\n\n- id: R12-M5\n  summary: Feature trajectory 图应从 Appendix 移回正文\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: REJECTED by Director — 页数限制不允许\n  action_items:\n  - round: 12\n    action: REJECT — 页数约束\n    assigned_to: research_director\n    status: open\n  resolution: Won't fix — page budget allocated to Discussion expansion instead\n  resolution_round: 12\n\n- id: R12-W8\n  summary: 多重共线性下 individual feature importance 不可靠\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: R1-W6 提出。\n  - round: 13\n    reviewers: [1, 2]\n    note: 部分改善，添加脚注 caveat 和 Kendall W 支持。\n  - round: 14\n    reviewers: []\n    note: \"R14 未单独提出此问题。可能已通过 R13 的修改充分解决，待 Research Director 确认。\"\n  action_items:\n  - round: 13\n    action: 将脚注 caveat 提升为正文段落\n    assigned_to: paper_agent\n    status: resolved\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M2\n  summary: RF ordinal claim 过强\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Minor issue.\n  - round: 13\n    reviewers: []\n    note: 弱化为 ordinally consistent predictions + CORAL 匹配数据。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已修复，待确认。\"\n  action_items:\n  - round: 12\n    action: 弱化为 ordinally consistent predictions\n    assigned_to: paper_agent\n    status: in_progress\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M4\n  summary: Prompted generation 验证仅 1/9 cells\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Minor.\n  - round: 13\n    reviewers: [1, 2]\n    note: 已添加 single-cell qualifier。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已通过 qualifier 修复，待确认。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M7\n  summary: Feature extraction 'requires no GPU' 声明可能不准确\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1]\n    note: Agent 核实中。\n  - round: 13\n    reviewers: []\n    note: 已改为 '~2 min GPU, ~50 min CPU'。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已修复，待确认。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null\n\n- id: R12-M8\n  summary: 遗漏引用 Muennighoff et al. (2024) + Ilyas et al. (2022)\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: Agent 验证中。\n  - round: 13\n    reviewers: []\n    note: 两条引用已出现在 bib 和正文中。\n  - round: 14\n    reviewers: []\n    note: \"R14 未提出。可能已修复，待确认。\"\n  action_items: []\n  resolution: ''\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-20T06:50:21.515055+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml\", \"bytes\": 19687}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-20T06:53:51.165633+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
  "report": "# 审稿报告 — recursive_gen_depth_est (Round 14, Fresh)\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**目标 Venue**: EMNLP 2026 (ACL Rolling Review May cycle)\n**投稿类别**: Long Paper (ARR)\n**审稿团队**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性与完整性）\n**审稿模式**: Fresh（重新审稿）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了涵盖 3 个模型家族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略 × 4 个深度的 180K 样本 benchmark。基于 19 个统计特征的 Random Forest 分类器在 in-distribution 设定下达到 59–82% 四类准确率（d1-d3 balanced: 58.9–81.5%），并提出 Effective Discriminable Depth (EDD) 指标量化相邻深度的可判别性。论文系统分析了跨模型（66.4%, d1-d3: 55.4%）、跨策略（59.1%, d1-d3: 45.9%）和跨规模（7-14B）的泛化性能，发现 perplexity tail 特征族（p90_ppl, kurtosis_ppl）和 surprisal variance 在所有 9 个实验单元中占主导地位。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有价值** [R1, R2 一致]\n将递归生成深度估计从 binary human/machine detection 推进到 ordinal depth classification，是 model collapse 文献中被忽视的逆问题。经搜索确认无先前工作显式处理此问题。问题定义清晰（Definition 1），具有理论意义和实际价值。\n\n**S2. Benchmark 设计系统** [R1, R2 一致]\n180K 样本覆盖 3×3×4 完整网格，控制变量严格（固定 LoRA 配置、固定 reference model、固定 seed text）。Domain bias analysis（Appendix B.8）包括 bug 修复的透明披露，体现了实验诚信。15 页附录含 23 个子实验，透明度很高。\n\n**S3. Perplexity tail insight 有理论连接** [R1, R2 一致]\n将 model collapse 理论（tail distribution collapse）与检测特征（perplexity tail statistics）连接。三种 importance measures（Gini, SHAP, permutation）高度一致（Kendall's W=0.90, p<0.005），perplexity tail 在 9/9 cells 中占主导地位。§3.5 的 theoretical grounding 虽非完整证明但方向正确。\n\n**S4. EDD 指标有概念贡献** [R1]\n将聚合准确率分解为逐深度边界的可判别性，提供了比单一准确率更有信息量的评估框架。EDD 上界与 contraction factor 的关系（§3.5）提供了有用的理论框架。\n\n**S5. Limitations 异常全面** [R1, R2 一致]\n整页讨论 10+ 个 limitations，包括 d0 inflation、FPR、self-reference confound、cross-strategy constraint 等。多数问题是作者自己识别并讨论的，态度坦诚。这在 submission 中较为少见。\n\n**S6. 相关工作覆盖全面** [R2]\n68 篇引用涵盖 model collapse 理论、AI text detection、data provenance、ordinal classification、decoding strategies 五个领域。引用完整性检查：0 orphan / 0 missing bib entries，57/68 online verified。\n\n**S7. Strategy-dependent trajectory 发现** [R2]\n不同解码策略产生质量不同的退化轨迹是有价值的 empirical insight，对理解 model collapse 的机制有帮助。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] 14B \"signal persists\" claim 与自定义 EDD 指标矛盾** [R1-N3, R2-N1, 交叉一致 AGREE]\n\n14B 实验（Qwen2.5-14B）EDD=0（所有三种解码策略下无相邻深度对 AUC 超过 0.70 阈值），4-class 准确率仅 50.8%（2× chance）。但 §5.4 和 §6 声称 \"signal persists at 14B\"——这与论文自己的 EDD 定义直接矛盾。实验同时改变 5 个变量（model family, tokenizer, training data, reference model, model scale），Appendix B.14 §Confounds 承认 \"infeasible to attribute the observed accuracy gap to any single factor\"，但 headline claim 忽略了这一限定。\n\nR1 补充关键观察：d0v1 AUC 在 14B 上降至 0.561-0.643（vs 1-1.5B >0.99）。d0/d1 boundary 是整个框架中最容易的判别（human vs first-gen），这个 boundary 的崩塌暗示 14B 的信号可能根本是不同性质的，而非同一信号的 scale-dependent attenuation。\n\n**修改要求**：(1) §5.4 标题加强 caveat（如 \"Inconclusive Cross-Scale Observations\"）；(2) §6 用 \"above-chance accuracy is observed but cannot be attributed to depth signal due to multiple confounds\" 替换 \"persists\"；(3) Abstract 明确声明 14B EDD=0 及其意义。\n\n**C2. [Critical] Headline metrics 被 d0 召回率（>97%）系统性膨胀** [R1-N1, R2 AGREE]\n\nd0（human-written）召回率 >97%（Table 2），four-class accuracy 被系统性拉高。定量分析：d0 贡献约 24.25%（0.25×97%）到总 accuracy，最低 cell 的 d1-d3 实际准确率仅约 49%（vs headline ~61%）。Cross-model transfer 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 为主指标，d1-d3 balanced accuracy 虽有报告但处于括号或脚注位置。\n\nR2 补充：d0 是任务的合法类别——问题在于 emphasis 而非 metric 定义。应双指标并列而非以 d1-d3 为唯一主指标。\n\n**修改要求**：Abstract 和所有 headline 处双指标并列报告（4-class accuracy + d1-d3 balanced accuracy），使读者自行判断实用性。\n\n**C3. [Critical] 与 Binoculars 11-feature RF 无显著差异（78.4% vs 78.1%, p>0.05），Table 4 呈现不透明** [R1-N2, R2 AGREE]\n\nTable 4 仅列出 Binoculars 的较弱配置（threshold 69.8%, RF 1-feat 63.7%），78.1% 的完整 11-feature RF 配置仅在 §5.1 正文中一句话提及（\"matches our pipeline within 0.3 pp\"）。这种呈现方式——在 table 中放弱版本、在文本中轻描淡写强版本——降低了论文的透明度。\n\nMerged 30-feature 达到 82.6%（+4.2pp）表明两个管线信号互补——但互补性本身暗示 19-feature pipeline 未完全覆盖 Binoculars 信号。R2 指出论文管线仅需单一 reference model（vs Binoculars 的 observer-performer pair），这种部署优势应被明确论证。\n\n**修改要求**：(1) Table 4 加入 Binoculars 11-feat RF 行并标注 p-value；(2) 正文明确论证相对优势（单一 reference model、无需 observer-performer pair、特征可解释性）；(3) 将 merged 82.6% 作为推荐配置而非附录内容。\n\n**C4. [Critical] 主文超出 8 页限制** [视觉审查]\n\n视觉审查发现 Section 6 (Discussion and Conclusion) 从 page 8 底部延伸至 page 9 上半部（约 0.3-0.5 页溢出）。Limitations 在 page 9 中部开始。EMNLP 2026 规定 long paper 正文严格限制 8 页（Limitations 和 Ethics 不计入页数），Discussion/Conclusion 属正文，这是格式违规。注：R2 格式检查误判为合规。\n\n**修改要求**：压缩正文约 0.3-0.5 页以符合 8-page limit。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. Full-replacement 假设限制生态效度** [R2: critical, R1 REBUT → Director 裁定: Should-Fix]\n\n所有实验使用 full-replacement 递归链。Real-world contamination 是 accumulation（partial mixing）。Gerstgrasser et al. (2024) 已证明 accumulation 可避免 collapse。Curation PoC（Appendix B.22）结果 inconclusive（p>0.4）。\n\nR1 反驳（Director 采纳）：full-replacement 是 controlled study 的必要起点——消除 mixing ratio 连续混淆变量，使 depth 成为唯一自变量。论文定位为 upper bound 合理。Prompted generation（69.5%, -13.8pp）和 mixed-depth corpus 提供了 partial relaxation。作为 Findings 论文在 controlled setting 下建立 feasibility 已足够。完整 accumulation 实验是重要的 future work，但其缺失不否定当前贡献。\n\n**修改建议**：Discussion 中加深 accumulation 场景分析。\n\n**W2. 算法贡献有限** [R2: critical, R1 AGREE with nuance → Director 裁定: Should-Fix]\n\n核心方法是标准 RF（200 trees, 5-fold CV）+ 19 个标准统计特征。论文诚实定位为 \"task formalization and systematic empirical characterization\"。R1 指出 passage-level distributional aggregation（p90_ppl, var_surprisal, kurtosis_ppl）区别于 token-level 方法（GLTR, DetectGPT），是非 trivial 的特征工程选择。更关键的是，RF 大幅优于 neural 方法（Appendix B.7: PLM [CLS] representations yield negative R² for var_surprisal and p90_ppl）——\"perplexity tail statistics are not linearly accessible in pretrained representation space\" 可成为有价值的 insight，但未在主文充分展开。\n\n**修改建议**：深入分析 RF vs neural 的 representational gap（将 Appendix B.7 核心结论提升到主文）；加强 EDD formalization 使其成为更有理论深度的贡献。\n\n**W3. Self-reference 混淆使 3×3 atlas 内部不可比** [R1-W1, R2 AGREE]\n\nPythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp（Appendix B.11: self 78.6% vs cross-OLMo 74.5% vs cross-GPT2 67.3%）。Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%，与 OLMo 和 GPT-2 XL 的表观优势关系可能反转。Atlas 分析（§4）中所有 cross-cell 比较（如 \"GPT-2 XL achieves highest accuracy\"）基于不公平基础。\n\n**修改建议**：Table 2 增加 cross-reference accuracy 列，或在 §4.1 axis effect 分析中明确声明 Pythia 行可比性受限。\n\n**W4. Cross-strategy d1-d3 仅 45.9%（1.38× chance），实用性存疑** [R1-W2, R2-W4, 交叉一致]\n\nd1/d2 boundary inversion（AUC<0.5）意味着某些策略下系统会系统性地反转深度判断——比随机猜测更危险。Two-stage pipeline 回收 11.5pp，但未报告 strategy classifier 本身的准确率。如果 strategy identification 不可靠，two-stage 方案的实际增益会打折扣。\n\n**修改建议**：(1) 报告 strategy classifier 独立准确率；(2) Discussion 中明确 \"decoding strategy must be known or identifiable\" 为部署前提条件。\n\n**W5. Cross-seed replication 不充分（3/9 cells）** [R1-W4, R2 AGREE]\n\n仅 nucleus 策略 3 cells 有 2-seed replication（Appendix B.24）。OLMo seed=42 78.94% → seed=43 82.11%（+3.17pp, CI 不重叠）。Temperature 和 top-k 完全未复制。对于以系统性 benchmark 为核心贡献的论文，9/9 cells 均应有 cross-seed replication。\n\n**修改建议**：所有 9 cells 提供 cross-seed replication。\n\n**W6. Discussion 过于单薄** [R2-W2, R1 AGREE]\n\n§6 约 1 页，混合讨论和结论。核心分析——multi-channel depth encoding（Appendix B.26）、RF vs neural divergence（Appendix B.9/B.7）、Binoculars signal decomposition（Appendix B.17）、cross-scale behavior（Appendix B.14）——全在 Appendix。主体 Discussion 深度不足，审稿人主要阅读 8 页正文，关键洞察在 Appendix 中容易被忽略。\n\n**修改建议**：将 Appendix B.7（feature overlap analysis）和 B.17（Binoculars signal decomposition）核心结论提升到主文。\n\n**W7. Curation PoC inconclusive 但语气偏乐观** [R1-W7, R2-W5, 交叉一致]\n\nRF-filtered vs unfiltered p=0.407——主假设不成立。RF-vs-random 的 3 个 pairwise comparisons 在 Bonferroni 校正后仅 1/3 存活（rf_strict vs random_strict p=0.002 < α=0.017，另两个不通过）。§6 Discussion 仍称 \"practical signal for data curation\"，语气偏乐观。\n\n**修改建议**：(1) Appendix B.10 标题改为 \"Curation PoC (Inconclusive)\"；(2) §6 中降低对 curation 应用的信心级别。\n\n---\n\n### Minor\n\n**M1. EDD T=0.70 阈值需引用文献** [R1-W5, R2 partial REBUT]\nR2 指出 AUC=0.70 对应 ROC \"adequate discrimination\" 的常用经验阈值（Hosmer & Lemeshow 分类标准），非凭空选择。但论文未显式引用。建议 §3.4 增加一句引用 ROC 解释标准文献。\n\n**M2. LoRA sensitivity analysis 缺失** [R1-W3, R2 REBUT]\nR2 反驳：LoRA 是 benchmark 构建工具而非核心方法，sensitivity analysis 属于 benchmark robustness 问题。Director 裁定 Minor——在 Limitations 中更明确声明此局限即可。\n\n**M3. Perturbation-based baselines 适配不充分** [R1-W6, R2 AGREE]\nDetectGPT（28.8%）和 Min-K% Prob（33.2%）从 binary 改造为 ordinal，低性能可能反映适配方法局限。Min-K% augmented feature set +0.48pp 且排名 #3 说明确实携带互补信号。建议 Table 4 注明 \"adapted from binary detection\"，增加 binary d0-vs-d1+ sanity check。\n\n**M4. Bib entries 年份/作者 mismatch** [R1, R2 独立发现]\n- he2021_deberta_v3: bib=2023, actual=2021\n- alemohammad2024_mad: first author mismatch\n- guo2024_biscope: first author mismatch\n- gerstgrasser2024_accumulate, briesch2024selfconsuming: 应从 misc 更新为 inproceedings（已被会议接收）\n\n**M5. Surface-text ablation 低估简单 baselines** [R1]\nMean perplexity（25.1%, chance level）被用作 \"surface-text ablation\" 代表，但 p90_ppl 单特征达 58.3%。更公平的 ablation 应使用 best single feature。\n\n**M6. Abstract 信息过载** [R2-W1, R1 REBUT]\nR1 反驳：ACL/EMNLP 惯例允许具体数字，问题在于 which numbers are highlighted 而非数量。Director 裁定与 C2（d0 inflation）合并处理——修正 emphasis 即可。\n\n**M7. \"Depth Degradation Atlas\" 命名** [R2-W3, R1 partial REBUT]\nR1 认为 3×3 grid + feature trajectory + EDD decay + importance heatmap 符合 atlas 使用惯例。建议折中：保留 \"atlas\" 但首次使用时加注 scope（\"a 3×3 atlas at the 1-1.5B scale\"）。\n\n**M8. Figure 可读性** [视觉审查, R2-M4]\nFigure 1 heatmap 灰度打印下区分度有限（axis labels 约正文 60%）；Figure 2/4 仅靠颜色区分线条，无 line style 差异，灰度/色盲不友好；Figure 3 confusion matrix 字号偏小。\n\n**M9. 前 3 页无 display item + 缺少方法 pipeline 概念图** [视觉审查]\npp.1-3 连续纯文本无视觉锚点。Statistical fingerprint → RF → EDD 的多阶段框架无图示，增加审稿人认知负担。建议在 page 2 前引入方法概览图。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 通过交叉回应达成一致：\n\n| # | 问题 | 严重度 | 共识内容 |\n|---|------|--------|----------|\n| 1 | 14B \"signal persists\" overclaiming (C1) | Critical | EDD=0 与 \"persists\" 矛盾；5 重混淆无法归因 → 必须修正措辞 |\n| 2 | d0 inflation (C2) | Critical | 双指标并列报告；d0 是合法类别但不应膨胀印象 |\n| 3 | Binoculars parity (C3) | Critical | Table 4 应包含 11-feat RF；方法优势需通过其他维度论证 |\n| 4 | Cross-strategy 实用性 (W4) | Warning | d1-d3 45.9% + boundary inversion → 需报告 strategy classifier 准确率 |\n| 5 | Cross-seed 不充分 (W5) | Warning | 3/9 cells + CI 不重叠 → 9/9 均需覆盖 |\n| 6 | Discussion 单薄 (W6) | Warning | 核心洞察在 Appendix → 提升到主文 |\n| 7 | Curation PoC inconclusive (W7) | Warning | p>0.4 主假设不成立 → 降调 |\n| 8 | 评分一致 | — | Overall 3.0 (Findings) |\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 问题 | R1 立场 | R2 立场 | Director 裁定 |\n|------|---------|---------|---------------|\n| Full-replacement 生态效度 | Should-Fix（controlled study 合理起点，upper bound 定位有效） | Critical（限制应用前景，需 accumulation 实验） | **Should-Fix** — controlled study 起点选择合理；Findings 论文建立 feasibility 已足够 |\n| Abstract 信息量 | Fine（ACL 惯例允许数字） | Warning（信息过载） | **Minor** — 与 C2 合并处理 |\n| LoRA sensitivity | Should-Fix（不同 rank 可能改变 shift 特征） | Nice-to-have（LoRA 是 benchmark 工具非方法） | **Minor** — Limitations 中声明即可 |\n| EDD T=0.70 | Should-Fix（循环论证） | 有 ROC 经验标准支撑 | **Minor** — 需引用文献但非循环论证 |\n| Atlas 命名 | 符合使用惯例（3×3 + full analysis） | 过度包装 | **Minor** — 加注 scope 即可 |\n| AI 写作痕迹 | 标准学术英语，不应标记 | 可被注意到 | **不列入** — R1 反驳有效；Ethics Statement 已透明披露 |\n\n---\n\n## Questions（需作者澄清）\n\n1. **Strategy classifier 准确率**：Two-stage pipeline（§5.3）中 strategy identification 模块的独立准确率是多少？如不可靠，two-stage 方案的实际增益如何？\n2. **14B Pythia-referenced pipeline**：是否有使用 Pythia-1.4B（而非 self-reference）作为 14B 实验 reference model 的消融结果？这可隔离 reference model 混淆。\n3. **Binoculars 部署成本**：论文管线（单一 Pythia-1.4B, 1.4B params）vs Binoculars（observer-performer pair）的实际推理时间/成本对比？\n4. **d0 FPR calibration**：C4 FPR 4.7-22.4%，阈值 P(d0)≥0.15 降至 2.8%——这个阈值是在 held-out data 上选择的吗？\n5. **14B feature hierarchy shift**：14B top-k 下 TTR/hapax 替代 p90_ppl/var_surprisal（Appendix B.14）——这是否暗示 14B 的 depth signal 来源不同（lexical diversity vs distributional tail）？\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 建议（非 must-cite，但可加强文献覆盖）：\n\n1. **SeqXGPT**（sentence-level AI text attribution）— 与 passage-level depth estimation 形成方法论对比 [R1]\n2. **PAN 2026 Shared Task**（Generative Plagiarism Detection / Voight-Kampff）— 2026 直接相关的 shared task [R2]\n3. **TROVE / GenProve**（fine-grained text provenance, NAACL 2025/2026）— §2 Data Provenance 子节相关 [R2]\n4. **\"Collapse or Thrive? Perils and Promises of Synthetic Data in the Era of Generative AI\"** (arXiv:2410.16713, 2024) — model collapse 综述补充 [R2]\n5. **\"Rate of Model Collapse in Recursive Training\"** (arXiv:2412.17646, 2024) — collapse 速率理论，与 EDD contraction factor 分析（§3.5）相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未启用外部审稿 `external_review.paperreview_ai.enabled = false`）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-20 06:26–06:30 UTC）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | p.8-9 | 主文（§1-6）超出 8 页限制：§6 从 p.8 底部延伸至 p.9 上半部（约 0.3-0.5 页溢出）。Limitations 在 p.9 中部开始。需压缩正文。 |\n| Warning | pp.1-3 | 连续 3 页纯文本，无 display item（figure/table/equation），缺乏视觉锚点。建议在 p.2 前引入方法概览图。 |\n| Warning | global | 全文缺少方法 pipeline 概念图。Statistical fingerprint → RF → EDD 的多阶段框架无图示。 |\n| Warning | p.8 | Figure 3（confusion matrices）单元格数字字号偏小，打印或低分辨率下难以辨认。 |\n| Info | p.6 | Figure 1 heatmap Y/X 轴标签约正文 60%，灰度打印区分度有限。建议加大字号或在 cell 内标注数值。 |\n| Info | p.7 | Figure 2 legend 字号偏小；三条线仅靠颜色区分，未使用 line style。灰度/色盲不友好。 |\n| Info | p.14 | Figure 4（appendix, feature trajectories）同样仅靠颜色区分。 |\n| Info | pp.4-8 | 所有表格使用 booktabs 风格，排版规范，符合顶会标准。✓ |\n| Info | pp.10-12 | References 格式统一，无未解析引用。✓ |\n\n---\n\n## Overall Assessment\n\n### Overall Score: 3.0 — Findings（可被 Findings 接收）\n\n**EMNLP 2026 评分标准**：3 = Findings, 3.5 = Borderline Conference, 4 = Conference\n\n**维度汇总**：\n\n| 维度 | R1 | R2 | 均值 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | 3.25/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n| Overall | 3.0/5 | 3.0/5 | 3.0/5 |\n\n**Confidence**: 4/5（两位 Reviewer 均仔细阅读全文 + 15 页附录，核验统计检验和引用）\n\n### 核心限制（阻止从 Findings 上升到 Conference）\n\n1. **算法贡献缺失**：标准 RF + 已有统计特征，无方法论创新 → Excitement 低（均值 3.0）\n2. **Scale 受限**：14B EDD=0（50.8%, 2× chance），在实际关心的模型规模（≥14B）上实用性未验证\n3. **Cross-transfer 实用性不足**：cross-strategy d1-d3 仅 45.9%（1.38× chance），需已知策略信息\n4. **与 Binoculars 无显著差异**：78.4% vs 78.1% (p>0.05)，方法附加价值需重新论证\n5. **格式违规**：主文超出 8 页限制\n\n### 升级路径（如修复以下问题，可考虑 3.5 Borderline Conference）\n\n- 修正 14B overclaiming、d0 inflation 报告、Binoculars Table 4 透明度\n- 修复页数超限\n- 深化 RF vs neural 的 representational gap 分析（从 Appendix 提升到主文）\n- 增加 accumulation 场景的至少一组 pilot 实验\n- 完成 9/9 cells cross-seed replication\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 以 4-class accuracy 为主导叙事，d1-d3 balanced accuracy 未并列 → **C2**\n- \"scale-dependent in magnitude\" 对 14B EDD=0 不够审慎 → **C1**\n- 数字偏多但 ACL 惯例可接受 → **M6**\n\n### §1 Introduction\n- 问题定义清晰，gap 识别准确 → **S1**\n- \"empirical contribution\" 定位诚实\n- 未提及 Binoculars 已达 78.1% 的上下文 → **C3**\n\n### §2 Related Work\n- 覆盖全面（model collapse, detection, provenance, ordinal, decoding）→ **S6**\n- 建议补充 SeqXGPT, PAN 2026, TROVE/GenProve → Missing References\n\n### §3 Method\n- Benchmark 构建系统（180K, 3×3×4 grid）→ **S2**\n- Self-reference 混淆（Pythia 同时为 generator 和 reference）未在本节充分讨论 → **W3**\n- EDD Definition 1 的 contiguous prefix 要求在 non-monotonic 场景下过于保守 → **M1**\n- Feature design 19 个特征有据，perplexity tail 理论连接良好 → **S3**\n\n### §4 Depth Degradation Atlas\n- Feature analysis 深入一致（Kendall's W=0.90）→ **S3**\n- Atlas 内部比较受 self-reference 影响：所有 cross-cell 比较（如 \"GPT-2 XL achieves highest accuracy\"）基于不公平基础 → **W3**\n- Strategy-dependent trajectory 是有价值的发现 → **S7**\n- EDD threshold sensitivity analysis 存在但缺乏文献引用 → **M1**\n\n### §5 Generalization and Robustness\n- Cross-model 66.4%（d1-d3: 55.4%）实验设计合理 → 但 d2 worst case 26.8% 应更突出\n- Cross-strategy 45.9%（d1-d3）+ boundary inversion 讨论不足 → **W4**\n- §5.4 14B \"signal persists\" overclaiming → **C1**\n- Binoculars comparison Table 4 呈现不透明 → **C3**\n- RF vs neural 差距（78.4% vs 53.1%）的分析在 Appendix 而非主文 → **W2**\n\n### §6 Discussion and Conclusion\n- 过于单薄（约 1 页），核心洞察在 Appendix → **W6**\n- Curation 语气偏乐观（p>0.4 的主比较） → **W7**\n- 超出 8 页限制 → **C4**\n\n### Limitations\n- 异常全面和诚实 → **S5**\n- Full-replacement scope 声明合理 → **W1** 裁定依据\n\n### Appendix\n- 丰富（15 页，23 子实验）→ **S2**\n- B.7（RF vs neural）、B.17（Binoculars decomposition）应提升到主文 → **W2, W6**\n- B.22（Curation PoC）应标记为 Inconclusive → **W7**\n- B.24（cross-seed）仅 3/9 cells → **W5**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8",
    "report": "# 审稿报告 — recursive_gen_depth_est (Round 14, Fresh)\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**目标 Venue**: EMNLP 2026 (ACL Rolling Review May cycle)\n**投稿类别**: Long Paper (ARR)\n**审稿团队**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性与完整性）\n**审稿模式**: Fresh（重新审稿）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文将递归生成深度估计形式化为序数分类任务，构建了涵盖 3 个模型家族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略 × 4 个深度的 180K 样本 benchmark。基于 19 个统计特征的 Random Forest 分类器在 in-distribution 设定下达到 59–82% 四类准确率（d1-d3 balanced: 58.9–81.5%），并提出 Effective Discriminable Depth (EDD) 指标量化相邻深度的可判别性。论文系统分析了跨模型（66.4%, d1-d3: 55.4%）、跨策略（59.1%, d1-d3: 45.9%）和跨规模（7-14B）的泛化性能，发现 perplexity tail 特征族（p90_ppl, kurtosis_ppl）和 surprisal variance 在所有 9 个实验单元中占主导地位。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有价值** [R1, R2 一致]\n将递归生成深度估计从 binary human/machine detection 推进到 ordinal depth classification，是 model collapse 文献中被忽视的逆问题。经搜索确认无先前工作显式处理此问题。问题定义清晰（Definition 1），具有理论意义和实际价值。\n\n**S2. Benchmark 设计系统** [R1, R2 一致]\n180K 样本覆盖 3×3×4 完整网格，控制变量严格（固定 LoRA 配置、固定 reference model、固定 seed text）。Domain bias analysis（Appendix B.8）包括 bug 修复的透明披露，体现了实验诚信。15 页附录含 23 个子实验，透明度很高。\n\n**S3. Perplexity tail insight 有理论连接** [R1, R2 一致]\n将 model collapse 理论（tail distribution collapse）与检测特征（perplexity tail statistics）连接。三种 importance measures（Gini, SHAP, permutation）高度一致（Kendall's W=0.90, p<0.005），perplexity tail 在 9/9 cells 中占主导地位。§3.5 的 theoretical grounding 虽非完整证明但方向正确。\n\n**S4. EDD 指标有概念贡献** [R1]\n将聚合准确率分解为逐深度边界的可判别性，提供了比单一准确率更有信息量的评估框架。EDD 上界与 contraction factor 的关系（§3.5）提供了有用的理论框架。\n\n**S5. Limitations 异常全面** [R1, R2 一致]\n整页讨论 10+ 个 limitations，包括 d0 inflation、FPR、self-reference confound、cross-strategy constraint 等。多数问题是作者自己识别并讨论的，态度坦诚。这在 submission 中较为少见。\n\n**S6. 相关工作覆盖全面** [R2]\n68 篇引用涵盖 model collapse 理论、AI text detection、data provenance、ordinal classification、decoding strategies 五个领域。引用完整性检查：0 orphan / 0 missing bib entries，57/68 online verified。\n\n**S7. Strategy-dependent trajectory 发现** [R2]\n不同解码策略产生质量不同的退化轨迹是有价值的 empirical insight，对理解 model collapse 的机制有帮助。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] 14B \"signal persists\" claim 与自定义 EDD 指标矛盾** [R1-N3, R2-N1, 交叉一致 AGREE]\n\n14B 实验（Qwen2.5-14B）EDD=0（所有三种解码策略下无相邻深度对 AUC 超过 0.70 阈值），4-class 准确率仅 50.8%（2× chance）。但 §5.4 和 §6 声称 \"signal persists at 14B\"——这与论文自己的 EDD 定义直接矛盾。实验同时改变 5 个变量（model family, tokenizer, training data, reference model, model scale），Appendix B.14 §Confounds 承认 \"infeasible to attribute the observed accuracy gap to any single factor\"，但 headline claim 忽略了这一限定。\n\nR1 补充关键观察：d0v1 AUC 在 14B 上降至 0.561-0.643（vs 1-1.5B >0.99）。d0/d1 boundary 是整个框架中最容易的判别（human vs first-gen），这个 boundary 的崩塌暗示 14B 的信号可能根本是不同性质的，而非同一信号的 scale-dependent attenuation。\n\n**修改要求**：(1) §5.4 标题加强 caveat（如 \"Inconclusive Cross-Scale Observations\"）；(2) §6 用 \"above-chance accuracy is observed but cannot be attributed to depth signal due to multiple confounds\" 替换 \"persists\"；(3) Abstract 明确声明 14B EDD=0 及其意义。\n\n**C2. [Critical] Headline metrics 被 d0 召回率（>97%）系统性膨胀** [R1-N1, R2 AGREE]\n\nd0（human-written）召回率 >97%（Table 2），four-class accuracy 被系统性拉高。定量分析：d0 贡献约 24.25%（0.25×97%）到总 accuracy，最低 cell 的 d1-d3 实际准确率仅约 49%（vs headline ~61%）。Cross-model transfer 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 为主指标，d1-d3 balanced accuracy 虽有报告但处于括号或脚注位置。\n\nR2 补充：d0 是任务的合法类别——问题在于 emphasis 而非 metric 定义。应双指标并列而非以 d1-d3 为唯一主指标。\n\n**修改要求**：Abstract 和所有 headline 处双指标并列报告（4-class accuracy + d1-d3 balanced accuracy），使读者自行判断实用性。\n\n**C3. [Critical] 与 Binoculars 11-feature RF 无显著差异（78.4% vs 78.1%, p>0.05），Table 4 呈现不透明** [R1-N2, R2 AGREE]\n\nTable 4 仅列出 Binoculars 的较弱配置（threshold 69.8%, RF 1-feat 63.7%），78.1% 的完整 11-feature RF 配置仅在 §5.1 正文中一句话提及（\"matches our pipeline within 0.3 pp\"）。这种呈现方式——在 table 中放弱版本、在文本中轻描淡写强版本——降低了论文的透明度。\n\nMerged 30-feature 达到 82.6%（+4.2pp）表明两个管线信号互补——但互补性本身暗示 19-feature pipeline 未完全覆盖 Binoculars 信号。R2 指出论文管线仅需单一 reference model（vs Binoculars 的 observer-performer pair），这种部署优势应被明确论证。\n\n**修改要求**：(1) Table 4 加入 Binoculars 11-feat RF 行并标注 p-value；(2) 正文明确论证相对优势（单一 reference model、无需 observer-performer pair、特征可解释性）；(3) 将 merged 82.6% 作为推荐配置而非附录内容。\n\n**C4. [Critical] 主文超出 8 页限制** [视觉审查]\n\n视觉审查发现 Section 6 (Discussion and Conclusion) 从 page 8 底部延伸至 page 9 上半部（约 0.3-0.5 页溢出）。Limitations 在 page 9 中部开始。EMNLP 2026 规定 long paper 正文严格限制 8 页（Limitations 和 Ethics 不计入页数），Discussion/Conclusion 属正文，这是格式违规。注：R2 格式检查误判为合规。\n\n**修改要求**：压缩正文约 0.3-0.5 页以符合 8-page limit。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. Full-replacement 假设限制生态效度** [R2: critical, R1 REBUT → Director 裁定: Should-Fix]\n\n所有实验使用 full-replacement 递归链。Real-world contamination 是 accumulation（partial mixing）。Gerstgrasser et al. (2024) 已证明 accumulation 可避免 collapse。Curation PoC（Appendix B.22）结果 inconclusive（p>0.4）。\n\nR1 反驳（Director 采纳）：full-replacement 是 controlled study 的必要起点——消除 mixing ratio 连续混淆变量，使 depth 成为唯一自变量。论文定位为 upper bound 合理。Prompted generation（69.5%, -13.8pp）和 mixed-depth corpus 提供了 partial relaxation。作为 Findings 论文在 controlled setting 下建立 feasibility 已足够。完整 accumulation 实验是重要的 future work，但其缺失不否定当前贡献。\n\n**修改建议**：Discussion 中加深 accumulation 场景分析。\n\n**W2. 算法贡献有限** [R2: critical, R1 AGREE with nuance → Director 裁定: Should-Fix]\n\n核心方法是标准 RF（200 trees, 5-fold CV）+ 19 个标准统计特征。论文诚实定位为 \"task formalization and systematic empirical characterization\"。R1 指出 passage-level distributional aggregation（p90_ppl, var_surprisal, kurtosis_ppl）区别于 token-level 方法（GLTR, DetectGPT），是非 trivial 的特征工程选择。更关键的是，RF 大幅优于 neural 方法（Appendix B.7: PLM [CLS] representations yield negative R² for var_surprisal and p90_ppl）——\"perplexity tail statistics are not linearly accessible in pretrained representation space\" 可成为有价值的 insight，但未在主文充分展开。\n\n**修改建议**：深入分析 RF vs neural 的 representational gap（将 Appendix B.7 核心结论提升到主文）；加强 EDD formalization 使其成为更有理论深度的贡献。\n\n**W3. Self-reference 混淆使 3×3 atlas 内部不可比** [R1-W1, R2 AGREE]\n\nPythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp（Appendix B.11: self 78.6% vs cross-OLMo 74.5% vs cross-GPT2 67.3%）。Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%，与 OLMo 和 GPT-2 XL 的表观优势关系可能反转。Atlas 分析（§4）中所有 cross-cell 比较（如 \"GPT-2 XL achieves highest accuracy\"）基于不公平基础。\n\n**修改建议**：Table 2 增加 cross-reference accuracy 列，或在 §4.1 axis effect 分析中明确声明 Pythia 行可比性受限。\n\n**W4. Cross-strategy d1-d3 仅 45.9%（1.38× chance），实用性存疑** [R1-W2, R2-W4, 交叉一致]\n\nd1/d2 boundary inversion（AUC<0.5）意味着某些策略下系统会系统性地反转深度判断——比随机猜测更危险。Two-stage pipeline 回收 11.5pp，但未报告 strategy classifier 本身的准确率。如果 strategy identification 不可靠，two-stage 方案的实际增益会打折扣。\n\n**修改建议**：(1) 报告 strategy classifier 独立准确率；(2) Discussion 中明确 \"decoding strategy must be known or identifiable\" 为部署前提条件。\n\n**W5. Cross-seed replication 不充分（3/9 cells）** [R1-W4, R2 AGREE]\n\n仅 nucleus 策略 3 cells 有 2-seed replication（Appendix B.24）。OLMo seed=42 78.94% → seed=43 82.11%（+3.17pp, CI 不重叠）。Temperature 和 top-k 完全未复制。对于以系统性 benchmark 为核心贡献的论文，9/9 cells 均应有 cross-seed replication。\n\n**修改建议**：所有 9 cells 提供 cross-seed replication。\n\n**W6. Discussion 过于单薄** [R2-W2, R1 AGREE]\n\n§6 约 1 页，混合讨论和结论。核心分析——multi-channel depth encoding（Appendix B.26）、RF vs neural divergence（Appendix B.9/B.7）、Binoculars signal decomposition（Appendix B.17）、cross-scale behavior（Appendix B.14）——全在 Appendix。主体 Discussion 深度不足，审稿人主要阅读 8 页正文，关键洞察在 Appendix 中容易被忽略。\n\n**修改建议**：将 Appendix B.7（feature overlap analysis）和 B.17（Binoculars signal decomposition）核心结论提升到主文。\n\n**W7. Curation PoC inconclusive 但语气偏乐观** [R1-W7, R2-W5, 交叉一致]\n\nRF-filtered vs unfiltered p=0.407——主假设不成立。RF-vs-random 的 3 个 pairwise comparisons 在 Bonferroni 校正后仅 1/3 存活（rf_strict vs random_strict p=0.002 < α=0.017，另两个不通过）。§6 Discussion 仍称 \"practical signal for data curation\"，语气偏乐观。\n\n**修改建议**：(1) Appendix B.10 标题改为 \"Curation PoC (Inconclusive)\"；(2) §6 中降低对 curation 应用的信心级别。\n\n---\n\n### Minor\n\n**M1. EDD T=0.70 阈值需引用文献** [R1-W5, R2 partial REBUT]\nR2 指出 AUC=0.70 对应 ROC \"adequate discrimination\" 的常用经验阈值（Hosmer & Lemeshow 分类标准），非凭空选择。但论文未显式引用。建议 §3.4 增加一句引用 ROC 解释标准文献。\n\n**M2. LoRA sensitivity analysis 缺失** [R1-W3, R2 REBUT]\nR2 反驳：LoRA 是 benchmark 构建工具而非核心方法，sensitivity analysis 属于 benchmark robustness 问题。Director 裁定 Minor——在 Limitations 中更明确声明此局限即可。\n\n**M3. Perturbation-based baselines 适配不充分** [R1-W6, R2 AGREE]\nDetectGPT（28.8%）和 Min-K% Prob（33.2%）从 binary 改造为 ordinal，低性能可能反映适配方法局限。Min-K% augmented feature set +0.48pp 且排名 #3 说明确实携带互补信号。建议 Table 4 注明 \"adapted from binary detection\"，增加 binary d0-vs-d1+ sanity check。\n\n**M4. Bib entries 年份/作者 mismatch** [R1, R2 独立发现]\n- he2021_deberta_v3: bib=2023, actual=2021\n- alemohammad2024_mad: first author mismatch\n- guo2024_biscope: first author mismatch\n- gerstgrasser2024_accumulate, briesch2024selfconsuming: 应从 misc 更新为 inproceedings（已被会议接收）\n\n**M5. Surface-text ablation 低估简单 baselines** [R1]\nMean perplexity（25.1%, chance level）被用作 \"surface-text ablation\" 代表，但 p90_ppl 单特征达 58.3%。更公平的 ablation 应使用 best single feature。\n\n**M6. Abstract 信息过载** [R2-W1, R1 REBUT]\nR1 反驳：ACL/EMNLP 惯例允许具体数字，问题在于 which numbers are highlighted 而非数量。Director 裁定与 C2（d0 inflation）合并处理——修正 emphasis 即可。\n\n**M7. \"Depth Degradation Atlas\" 命名** [R2-W3, R1 partial REBUT]\nR1 认为 3×3 grid + feature trajectory + EDD decay + importance heatmap 符合 atlas 使用惯例。建议折中：保留 \"atlas\" 但首次使用时加注 scope（\"a 3×3 atlas at the 1-1.5B scale\"）。\n\n**M8. Figure 可读性** [视觉审查, R2-M4]\nFigure 1 heatmap 灰度打印下区分度有限（axis labels 约正文 60%）；Figure 2/4 仅靠颜色区分线条，无 line style 差异，灰度/色盲不友好；Figure 3 confusion matrix 字号偏小。\n\n**M9. 前 3 页无 display item + 缺少方法 pipeline 概念图** [视觉审查]\npp.1-3 连续纯文本无视觉锚点。Statistical fingerprint → RF → EDD 的多阶段框架无图示，增加审稿人认知负担。建议在 page 2 前引入方法概览图。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 通过交叉回应达成一致：\n\n| # | 问题 | 严重度 | 共识内容 |\n|---|------|--------|----------|\n| 1 | 14B \"signal persists\" overclaiming (C1) | Critical | EDD=0 与 \"persists\" 矛盾；5 重混淆无法归因 → 必须修正措辞 |\n| 2 | d0 inflation (C2) | Critical | 双指标并列报告；d0 是合法类别但不应膨胀印象 |\n| 3 | Binoculars parity (C3) | Critical | Table 4 应包含 11-feat RF；方法优势需通过其他维度论证 |\n| 4 | Cross-strategy 实用性 (W4) | Warning | d1-d3 45.9% + boundary inversion → 需报告 strategy classifier 准确率 |\n| 5 | Cross-seed 不充分 (W5) | Warning | 3/9 cells + CI 不重叠 → 9/9 均需覆盖 |\n| 6 | Discussion 单薄 (W6) | Warning | 核心洞察在 Appendix → 提升到主文 |\n| 7 | Curation PoC inconclusive (W7) | Warning | p>0.4 主假设不成立 → 降调 |\n| 8 | 评分一致 | — | Overall 3.0 (Findings) |\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 问题 | R1 立场 | R2 立场 | Director 裁定 |\n|------|---------|---------|---------------|\n| Full-replacement 生态效度 | Should-Fix（controlled study 合理起点，upper bound 定位有效） | Critical（限制应用前景，需 accumulation 实验） | **Should-Fix** — controlled study 起点选择合理；Findings 论文建立 feasibility 已足够 |\n| Abstract 信息量 | Fine（ACL 惯例允许数字） | Warning（信息过载） | **Minor** — 与 C2 合并处理 |\n| LoRA sensitivity | Should-Fix（不同 rank 可能改变 shift 特征） | Nice-to-have（LoRA 是 benchmark 工具非方法） | **Minor** — Limitations 中声明即可 |\n| EDD T=0.70 | Should-Fix（循环论证） | 有 ROC 经验标准支撑 | **Minor** — 需引用文献但非循环论证 |\n| Atlas 命名 | 符合使用惯例（3×3 + full analysis） | 过度包装 | **Minor** — 加注 scope 即可 |\n| AI 写作痕迹 | 标准学术英语，不应标记 | 可被注意到 | **不列入** — R1 反驳有效；Ethics Statement 已透明披露 |\n\n---\n\n## Questions（需作者澄清）\n\n1. **Strategy classifier 准确率**：Two-stage pipeline（§5.3）中 strategy identification 模块的独立准确率是多少？如不可靠，two-stage 方案的实际增益如何？\n2. **14B Pythia-referenced pipeline**：是否有使用 Pythia-1.4B（而非 self-reference）作为 14B 实验 reference model 的消融结果？这可隔离 reference model 混淆。\n3. **Binoculars 部署成本**：论文管线（单一 Pythia-1.4B, 1.4B params）vs Binoculars（observer-performer pair）的实际推理时间/成本对比？\n4. **d0 FPR calibration**：C4 FPR 4.7-22.4%，阈值 P(d0)≥0.15 降至 2.8%——这个阈值是在 held-out data 上选择的吗？\n5. **14B feature hierarchy shift**：14B top-k 下 TTR/hapax 替代 p90_ppl/var_surprisal（Appendix B.14）——这是否暗示 14B 的 depth signal 来源不同（lexical diversity vs distributional tail）？\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 建议（非 must-cite，但可加强文献覆盖）：\n\n1. **SeqXGPT**（sentence-level AI text attribution）— 与 passage-level depth estimation 形成方法论对比 [R1]\n2. **PAN 2026 Shared Task**（Generative Plagiarism Detection / Voight-Kampff）— 2026 直接相关的 shared task [R2]\n3. **TROVE / GenProve**（fine-grained text provenance, NAACL 2025/2026）— §2 Data Provenance 子节相关 [R2]\n4. **\"Collapse or Thrive? Perils and Promises of Synthetic Data in the Era of Generative AI\"** (arXiv:2410.16713, 2024) — model collapse 综述补充 [R2]\n5. **\"Rate of Model Collapse in Recursive Training\"** (arXiv:2412.17646, 2024) — collapse 速率理论，与 EDD contraction factor 分析（§3.5）相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未启用外部审稿 `external_review.paperreview_ai.enabled = false`）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-20 06:26–06:30 UTC）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | p.8-9 | 主文（§1-6）超出 8 页限制：§6 从 p.8 底部延伸至 p.9 上半部（约 0.3-0.5 页溢出）。Limitations 在 p.9 中部开始。需压缩正文。 |\n| Warning | pp.1-3 | 连续 3 页纯文本，无 display item（figure/table/equation），缺乏视觉锚点。建议在 p.2 前引入方法概览图。 |\n| Warning | global | 全文缺少方法 pipeline 概念图。Statistical fingerprint → RF → EDD 的多阶段框架无图示。 |\n| Warning | p.8 | Figure 3（confusion matrices）单元格数字字号偏小，打印或低分辨率下难以辨认。 |\n| Info | p.6 | Figure 1 heatmap Y/X 轴标签约正文 60%，灰度打印区分度有限。建议加大字号或在 cell 内标注数值。 |\n| Info | p.7 | Figure 2 legend 字号偏小；三条线仅靠颜色区分，未使用 line style。灰度/色盲不友好。 |\n| Info | p.14 | Figure 4（appendix, feature trajectories）同样仅靠颜色区分。 |\n| Info | pp.4-8 | 所有表格使用 booktabs 风格，排版规范，符合顶会标准。✓ |\n| Info | pp.10-12 | References 格式统一，无未解析引用。✓ |\n\n---\n\n## Overall Assessment\n\n### Overall Score: 3.0 — Findings（可被 Findings 接收）\n\n**EMNLP 2026 评分标准**：3 = Findings, 3.5 = Borderline Conference, 4 = Conference\n\n**维度汇总**：\n\n| 维度 | R1 | R2 | 均值 |\n|------|----|----|------|\n| Soundness | 3.0/5 | 3.5/5 | 3.25/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n| Overall | 3.0/5 | 3.0/5 | 3.0/5 |\n\n**Confidence**: 4/5（两位 Reviewer 均仔细阅读全文 + 15 页附录，核验统计检验和引用）\n\n### 核心限制（阻止从 Findings 上升到 Conference）\n\n1. **算法贡献缺失**：标准 RF + 已有统计特征，无方法论创新 → Excitement 低（均值 3.0）\n2. **Scale 受限**：14B EDD=0（50.8%, 2× chance），在实际关心的模型规模（≥14B）上实用性未验证\n3. **Cross-transfer 实用性不足**：cross-strategy d1-d3 仅 45.9%（1.38× chance），需已知策略信息\n4. **与 Binoculars 无显著差异**：78.4% vs 78.1% (p>0.05)，方法附加价值需重新论证\n5. **格式违规**：主文超出 8 页限制\n\n### 升级路径（如修复以下问题，可考虑 3.5 Borderline Conference）\n\n- 修正 14B overclaiming、d0 inflation 报告、Binoculars Table 4 透明度\n- 修复页数超限\n- 深化 RF vs neural 的 representational gap 分析（从 Appendix 提升到主文）\n- 增加 accumulation 场景的至少一组 pilot 实验\n- 完成 9/9 cells cross-seed replication\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 以 4-class accuracy 为主导叙事，d1-d3 balanced accuracy 未并列 → **C2**\n- \"scale-dependent in magnitude\" 对 14B EDD=0 不够审慎 → **C1**\n- 数字偏多但 ACL 惯例可接受 → **M6**\n\n### §1 Introduction\n- 问题定义清晰，gap 识别准确 → **S1**\n- \"empirical contribution\" 定位诚实\n- 未提及 Binoculars 已达 78.1% 的上下文 → **C3**\n\n### §2 Related Work\n- 覆盖全面（model collapse, detection, provenance, ordinal, decoding）→ **S6**\n- 建议补充 SeqXGPT, PAN 2026, TROVE/GenProve → Missing References\n\n### §3 Method\n- Benchmark 构建系统（180K, 3×3×4 grid）→ **S2**\n- Self-reference 混淆（Pythia 同时为 generator 和 reference）未在本节充分讨论 → **W3**\n- EDD Definition 1 的 contiguous prefix 要求在 non-monotonic 场景下过于保守 → **M1**\n- Feature design 19 个特征有据，perplexity tail 理论连接良好 → **S3**\n\n### §4 Depth Degradation Atlas\n- Feature analysis 深入一致（Kendall's W=0.90）→ **S3**\n- Atlas 内部比较受 self-reference 影响：所有 cross-cell 比较（如 \"GPT-2 XL achieves highest accuracy\"）基于不公平基础 → **W3**\n- Strategy-dependent trajectory 是有价值的发现 → **S7**\n- EDD threshold sensitivity analysis 存在但缺乏文献引用 → **M1**\n\n### §5 Generalization and Robustness\n- Cross-model 66.4%（d1-d3: 55.4%）实验设计合理 → 但 d2 worst case 26.8% 应更突出\n- Cross-strategy 45.9%（d1-d3）+ boundary inversion 讨论不足 → **W4**\n- §5.4 14B \"signal persists\" overclaiming → **C1**\n- Binoculars comparison Table 4 呈现不透明 → **C3**\n- RF vs neural 差距（78.4% vs 53.1%）的分析在 Appendix 而非主文 → **W2**\n\n### §6 Discussion and Conclusion\n- 过于单薄（约 1 页），核心洞察在 Appendix → **W6**\n- Curation 语气偏乐观（p>0.4 的主比较） → **W7**\n- 超出 8 页限制 → **C4**\n\n### Limitations\n- 异常全面和诚实 → **S5**\n- Full-replacement scope 声明合理 → **W1** 裁定依据\n\n### Appendix\n- 丰富（15 页，23 子实验）→ **S2**\n- B.7（RF vs neural）、B.17（Binoculars decomposition）应提升到主文 → **W2, W6**\n- B.22（Curation PoC）应标记为 Inconclusive → **W7**\n- B.24（cross-seed）仅 3/9 cells → **W5**"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-20T06:53:55.719809+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d269fdb74af3f4ab8d78b82a993f5cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4554
}
```

</details>

---


### Assistant

_source line 1224 · 2026-05-20T06:54:03.941192+00:00_

审稿报告已投递，Issue Tracker 已更新。

---

**审稿完成摘要**：

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

**4 个 Critical 问题**：
1. 14B EDD=0 与 "signal persists" 矛盾（5 重混淆无法归因）
2. Headline metrics 被 d0 召回率（>97%）系统性膨胀
3. 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%），Table 4 呈现不透明
4. 主文超出 8 页限制（视觉审查发现，§6 溢出约 0.3-0.5 页）

**7 个 Should-Fix**：full-replacement 生态效度（R1 论证降级）、算法贡献有限、self-reference atlas 不可比、cross-strategy 实用性、cross-seed 3/9 cells、Discussion 单薄、curation PoC inconclusive

**升级路径**：修复 Critical + 深化 RF vs neural 分析 + 补充 accumulation pilot → 可达 3.5 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1225 · 2026-05-20T06:54:06.866188+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

对 R1 的 13 条具体意见（3 Must-Fix + 7 Should-Fix + 3 Minor + 2 Missing Ref），我给出了 10 条 [AGREE]、3 条 [REBUT]（LoRA sensitivity / EDD 阈值 / heterogeneous chain confound）。与 R1 在 Overall 3.0（Findings）的评分上完全一致，核心分歧集中在 LoRA sensitivity 的优先级和 EDD 阈值的合理性上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1226 · 2026-05-20T06:54:18.603196+00:00_

审稿报告已投递完成。R2 的交叉回应确认了与 R1 的高度一致性（10/13 AGREE），3 条分歧均为严重度级别而非根本分歧，已在报告中裁定。

**本轮审稿总结**：

- **Overall Score**: 3.0 — Findings（可被 Findings 接收）
- **4 个 Critical Must-Fix**：14B overclaiming（EDD=0 vs "persists"）、d0 inflation 报告、Binoculars Table 4 透明度、主文超 8 页
- **7 个 Should-Fix**：full-replacement 生态效度、算法贡献有限、self-reference atlas 不可比、cross-strategy 实用性、cross-seed 不充分、Discussion 单薄、curation PoC inconclusive
- **10 个 Minor**：EDD 阈值引用、LoRA sensitivity 声明、perturbation baseline 适配、bib mismatch、figure 可读性等
- **Issue Tracker 已同步更新**（review_issues.yaml，28 条 issue）
- **审稿报告已投递** → Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 115

## Round 115

50 recorded events


### User

_source line 1227 · 2026-05-20T08:30:32.829628+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: recursive_gen_depth_est
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 未提供，请自行调研

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-20T08:30:39.784815+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-20T08:30:39.836212+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-20T08:30:46.884383+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1231 · 2026-05-20T08:30:46.935005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-20T08:30:54.724893+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-20T08:30:56.082055+00:00_

{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (139 个)\n\n- **cross_model_olmo_temp09_001**: DONE (killed) — \n- **pythia_topk50_001**: DONE (success) — \n- **cross_model_gpt2xl_001**: DONE (success) — \n- **cross_model_olmo_002**: DONE (success) — \n- **pythia_temp09_001**: DONE (success) — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **cross_model_olmo_001**: DONE (failed) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- accum_v2_mix25（准备中）\n- accum_v2_mix50（准备中）\n\n## 近期结论\n- **binoculars_14b_topk50** (success): Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy. ← 基于 qwen25_14b_topk50\n  [binoculars_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/binoculars_14b_topk50/report/binoculars_14b_topk50_results.md)\n- **qwen25_14b_topk50** (success): Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\n  [qwen25_14b_topk50_analysis](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report/qwen25_14b_topk50_analysis_b7a903.md) | [qwen25_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-20T08:30:56.688630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-20T08:30:57.141311+00:00_

-rw-r--r-- 1 ubuntu ubuntu 509457 May 20 07:57 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    959 May 18 17:34 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-20T08:30:57.593593+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "report.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "report.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-20T08:30:57.695969+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- accum_v2_mix25（准备中）\\n- accum_v2_mix50（准备中）\\n\\n## 近期结论\\n- **binoculars_14b_topk50** (success): Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy. ← 基于 qwen25_14b_topk50\\n  [binoculars_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/binoculars_14b_topk50/report/binoculars_14b_topk50_results.md)\\n- **qwen25_14b_topk50** (success): Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\\n  [qwen25_14b_topk50_analysis](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report/qwen25_14b_topk50_analysis_b7a903.md) | [qwen25_14b_topk50_results](/api/workspace-files/projects/recursive_gen_depth_est/artifacts/qwen25_14b_topk50/report/qwen25_14b_topk50_results.md)\\n- **binoculars_14b_temp09** (success): Binoculars cross-perplexity features provide complementary signal at 14B scale when merged with 19 statistical features, yielding accuracy above stat-only baseline. Tests whether cross-model divergence channel persists at larger scale. ← 基于 qwen25_14b_temp09\\n\\n## 趋势\\n成功 84 / 负向 13 / 失败 16 / 共 137\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ngpu-6000pro-2: 无 GPU 信息\\nwestd-48862: 无 GPU 信息\\n\\n## 告警\\n- mvp_pipeline_001: 已被终止 — unknown\\n- mvp_pipeline_002: 已被终止 — unknown\\n- mvp_pipeline_003: 已被终止 — un
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-20T08:30:57.697058+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1239 · 2026-05-20T08:30:57.798298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-20T08:31:04.807645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-20T08:31:06.213593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit author guidelines",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author guidelines",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-20T08:31:06.665810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-20T08:31:06.967579+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{theory}
39	
40	\input{atlas}
41	
42	\input{generalization}
43	
44	\input{discussion}
45	
46	\input{conclusion}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{section_appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-20T08:31:07.018405+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1245 · 2026-05-20T08:31:07.069061+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-20T08:31:11.287508+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, here's the information about EMNLP 2026 call for papers submission deadline related to ARR:

Papers must be submitted, at latest, by the ARR 2026 May cycle. 

The ARR 2026 May submission policy for EMNLP requires that authors explicitly declare which conference they intend to commit 
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6479
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-20T08:31:13.749204+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author guidelines"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authorship Changes Policy for ACL Venue Papers - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/Authorship_Changes_Policy_for_ACL_Venue_Papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I found information about ACL Rolling Review submission guidelines. Based on the search results, here are the key findings regarding page limits and author guidelines:

## Page Limits

For ACL 2026, final versions of accepted papers will be given one additional page of content (up to 9 pages
…[truncated 1359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7535
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-20T08:31:21.636065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-20T08:31:22.543105+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf (497.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-20T08:31:23.063283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers page limit anonymity template ARR May cycle deadline",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers page limit anonymity template ARR May cycle deadline",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1251 · 2026-05-20T08:31:23.917713+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>&1; ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/ 2>&1",
  "description": "Check existing review artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml 2>&1; ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_reports/ 2>&1",
    "description": "Check existing review artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1252 · 2026-05-20T08:31:24.018588+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml
round_1.md
round_10.md
round_11.md
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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-20T08:31:28.888316+00:00_

Web search results for query: "EMNLP 2026 call for papers page limit anonymity template ARR May cycle deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"}]

Based on the search results, here's what I found regarding EMNLP 2026 submission requirements:

## Anonymity
Following the ACL and ARR policies, there is no anonymity period requirement. However, Industry Track submissions must neither include the authors' names nor their affiliations, indicating that double-blind review is still in effect during the review process.

## ARR May Cycle and Deadline
Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. Papers must be submitted, at latest, by the ARR 2026 May cycle. Additionally, all deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Template
The search results mention templates are available. For tutorials, authors can download the LaTeX template or use 
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5825
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-20T08:31:58.324558+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "decisions.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "decisions.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-20T08:31:59.630326+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml\", \"content\": \"_next_id: 51\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 14:03 UTC\\n  summary: MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase\\n  rationale: Pythia-1.4B 4-depth pipeline 验证核心假设：4-class acc 78.2% (>>40% threshold),\\n    d1v2 AUC 0.861 (>>0.6 threshold)。控制实验排除域混淆（过滤代码后 acc 提升至 81.6%）。Top 特征为 surprisal\\n    variance 和 perplexity percentiles，说明信号来自分布窄化而非内容差异。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_pythia_002\\n    role: primary\\n    result: 4-class acc 78.2%, d1v2 AUC 0.861, content-type control 81.6%\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:01 UTC\\n  summary: Dream 三档分析完成：6项结构性必修+framing重心从DCOL转向Atlas/EDD\\n  rationale: Dream dream_20260514T140607 full review 完成。三档(best=borderline accept\\n    3.0, median=Findings 3.0, worst=borderline Findings 2.5)一致指出6项结构性问题：(1)DCOL loss\\n    Eq.1缺repulsive term不可复现 (2)Atlas论文零图不可接受 (3)bibliography严重不足(3-10 refs,需25+) (4)d0\\n    confound膨胀headline metrics,需报d1-d5 acc (5)EDD threshold无sensitivity analysis (6)surprisal\\n    reference model未指定有circularity风险。三档均认为Atlas/EDD是primary contribution,DCOL incremental\\n    over CLOC——与我们的contingency plan方向一致。worst case下DCOL不显著(p=0.12),EDD=2,但任务formalization+Atlas仍可支撑Findings。关键风险：cross-model\\n    transfer在worst case降到33%。\\n  related_experiments:\\n  - exp_id: dream_20260514T140607\\n    role: dream_simulation\\n    result: best=3.0 median=3.0 worst=2.5\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 19:45 UTC\\n  summary: 要求 baselines 统一使用 DeBERTa-v3-large，消除与 DCOL 的模型规模混淆变量\\n  rationale: Reviewer 发现 DCOL 用 DeBERTa-v3-large (435M) 而 CE/CORAL baselines 用 DeBERTa-v3-base\\n    (184M)，参数量差 2.4×，审稿人必问改进来源。修改 baseline 脚本支持 large 版本实验成本极低（模型已在服务器上），可彻底解耦方法贡献与模型容量。\\n  related_experiments:\\n  - exp_id: dcol_deberta_001\\n    role: target\\n    result: pending\\n  depends_on: []\\n- id: D00
…[truncated 4618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-20T08:32:00.186071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-20T08:32:00.688605+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-20T08:32:00.689012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-20T08:32:01.492563+00:00_

1	issues:
2	# ============================================================
3	# CRITICAL ISSUES
4	# ============================================================
5	
6	- id: R12-W4
7	  summary: Cross-scale 14B 实验 5 重混淆，EDD=0 与 "signal persists" claim 矛盾
8	  category: experiment
9	  severity: critical
10	  status: resolved
11	  first_raised_round: 12
12	  last_seen_round: 14
13	  mentions:
14	  - round: 12
15	    reviewers: [1, 2]
16	    note: R1 Should-Fix, R2 Must-Fix. Director 裁定 Should-Fix.
17	  - round: 13
18	    reviewers: [1, 2]
19	    note: 升级为 critical。论文已将标题改为 Preliminary，但 Abstract 仍言过其实。
20	  - round: 14
21	    reviewers: [1, 2]
22	    note: "Must-Fix. EDD=0 与 'persists' 矛盾。"
23	  action_items:
24	  - round: 14
25	    action: "§5.4 标题改 Preliminary; Abstract/§6 删除 persists; 加 EDD=0 + confound disclaimer"
26	    assigned_to: paper_agent
27	    status: resolved
28	  resolution: "§5.4 标题改为 'Preliminary Cross-Scale Observations (14B)', Abstract/§6 全面降调, §6 'persists' 改为 'residual discrimination above chance'. Reviewer R14 验收 PASS."
29	  resolution_round: 14
30	
31	- id: R12-W3
32	  summary: Headline metrics 被 d0 召回率（>97%）系统性膨胀
33	  category: writing
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 12
37	  last_seen_round: 14
38	  mentions:
39	  - round: 12
40	    reviewers: [1, 2]
41	    note: 一致。
42	  - round: 13
43	    reviewers: [1, 2]
44	    note: 部分改善。
45	  - round: 14
46	    reviewers: [1, 2]
47	    note: "Must-Fix. Abstract/Intro 以 4-class 为主指标."
48	  action_items:
49	  - round: 14
50	    action: "所有 headline 双指标并列 X% (d1-d3: Y%)"
51	    assigned_to: paper_agent
52	    status: resolved
53	  resolution: "Abstract/Intro/§4/§5 全部改为双指标格式. Reviewer R14 验收 PASS."
54	  resolution_round: 14
55	
56	- id: R14-C1
57	  summary: 与 Binoculars 11-feat RF 无显著差异（78.4% vs 78.1%），Table 4 呈现不透明
58	  category: method
59	  severity: critical
60	  status: resolved
61	  first_raised_round: 14
62	  last_seen_round: 14
63	  mentions:
64	  - round: 14
65	    re
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-20T08:32:01.543454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 submission deadline date",
  "allowed_domains": "['aclrollingreview.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 submission deadline date",
    "allowed_domains": "['aclrollingreview.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-20T08:32:06.744150+00:00_

Web search results for query: "ACL Rolling Review May 2026 submission deadline date"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, the submission deadline is always the 15th of the month for ACL Rolling Review cycles. Therefore, the submission deadline for the May 2026 ARR cycle would be **May 15, 2026**.

The search results indicate that the ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025, which replaced the previous 8-week cycle
…[truncated 158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5200
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-20T08:32:12.526976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-20T08:32:12.879034+00:00_

100	  category: framing
101	  severity: warning
102	  status: resolved
103	  first_raised_round: 12
104	  last_seen_round: 14
105	  mentions:
106	  - round: 14
107	    reviewers: [1, 2]
108	    note: "R2 critical, R1 REBUT. Director 裁定 Should-Fix."
109	  action_items:
110	  - round: 14
111	    action: "引用 accum_v3 实验数据 (70.1%/69.1% vs 84.2%)"
112	    assigned_to: paper_agent
113	    status: resolved
114	  resolution: "§6 引用 accum_v3 具体数字 70.1%/69.1% vs 84.2%. Reviewer R14 验收 soft FAIL 后补充具体数字修复."
115	  resolution_round: 14
116	
117	- id: R12-W9
118	  summary: 算法贡献不足：标准 RF + 标准特征
119	  category: framing
120	  severity: warning
121	  status: resolved
122	  first_raised_round: 12
123	  last_seen_round: 14
124	  mentions:
125	  - round: 14
126	    reviewers: [1, 2]
127	    note: "Should-Fix. PLM R²<0 insight 应提升到主文."
128	  action_items:
129	  - round: 14
130	    action: "将 Appendix B.7 核心结论 (PLM R²<0) 提升到主文"
131	    assigned_to: paper_agent
132	    status: resolved
133	  resolution: "§6 加入 PLM R²<0 结论. Reviewer R14 验收 PASS."
134	  resolution_round: 14
135	
136	- id: R12-M3
137	  summary: Self-reference confound 使 atlas 不可比
138	  category: experiment
139	  severity: warning
140	  status: resolved
141	  first_raised_round: 12
142	  last_seen_round: 14
143	  mentions:
144	  - round: 14
145	    reviewers: [1, 2]
146	    note: "Should-Fix. Table 2 需 caveat."
147	  action_items:
148	  - round: 14
149	    action: "Table 2 caption 加 Pythia self-reference caveat"
150	    assigned_to: paper_agent
151	    status: resolved
152	  resolution: "Table 1 caption 加 '†Self-reference scoring...4-11pp advantage'. Reviewer R14 验收 PASS."
153	  resolution_round: 14
154	
155	- id: R12-W2
156	  summary: Cross-strategy d1-d3 仅 45.9%, boundary inversion
157	  category: experiment
158	  severity: warning
159	  status: resolved
160	  first_raised_round: 12
161	  last_seen_round: 14
162	  mentions:
163	  - round: 14
164	    reviewers: [1, 2]
165	    note: "Should-Fix. 需报告 strategy classifier 准确率."
16
…[truncated 2524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-20T08:32:12.879422+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
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

_source line 1265 · 2026-05-20T08:32:12.929832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-20T08:32:20.209258+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the following information: 1) ARR submission deadline for EMNLP 2026 (which ARR cycle is the last one accepted), 2) commitment deadline, 3) page limits for long and short papers, 4) template requirements, 5) anonymity/double-blind rules, 6) appendix rules, 7) any other format requirements. Be precise with dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the following information: 1) ARR submission deadline for EMNLP 2026 (which ARR cycle is the last one accepted), 2) commitment deadline, 3) page limits for long and short papers, 4) template requirements, 5) anonymity/double-blind rules, 6) appendix rules, 7) any other format requirements. Be precise with dates."
  }
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-20T08:32:20.611088+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract the ARR 2026 May cycle submission deadline date. List all 2026 cycle dates if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract the ARR 2026 May cycle submission deadline date. List all 2026 cycle dates if available."
  }
}
```

</details>

---


### Tool result

_source line 1268 · 2026-05-20T08:32:23.623535+00:00_

# ARR 2026 May Cycle Submission Deadline

The May 2026 cycle submission deadline is **May 25, 2026**.

## All May 2026 Cycle Dates

According to the scheduling table provided:

| Key Milestone | Date |
|---|---|
| Submission | May 25, 2026 |
| Reviewer registration | May 27, 2026 |
| Reviews due | June 29, 2026 |
| Author Response | July 7-July 13, 2026 |
| Meta-reviews release | July 30, 2026 |
| Cycle End | August 2, 2026 |

The page notes that "the new schedule will be in action, starting in May 2025 cycle," implementing 10-week review cycles instead of the previous 8-week schedule.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 3012
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-20T08:32:24.829598+00:00_

# EMNLP 2026 Paper Submission Guidelines

**1) ARR Submission Deadline & Last Accepted Cycle:**
The ARR submission deadline is "May 25, 2026." Papers must be submitted to the "ARR 2026 May cycle" at the latest to be eligible for EMNLP commitment.

**2) Commitment Deadline:**
The commitment deadline to EMNLP is "August 2, 2026."

**3) Page Limits:**
- Long papers: 8 pages
- Short papers: 4 pages
- Camera-ready versions receive one additional page (9 pages for long papers, 5 pages for short papers)

**4) Template Requirements:**
The document references "Paper Submission and Templates" but directs readers to the ARR CFP page for specific template details without providing the actual templates here.

**5) Anonymity/Double-Blind Rules:**
The review process follows "double-blind" standards where "Reviewers will not see authors, nor will authors see reviewers." However, "there is no anonymity period requirement" after the ACL policy change.

**6) Appendix Rules:**
Materials are "Optional" and the document specifies "Optional Supplementary Materials (appendices, software, and data)" without detailing specific restrictions.

**7) Other Format Requirements:**
Authors must follow all "ARR submission requirements" and comply with the "Publication Ethics Policy," "Ethics Policy," and include a "responsible NLP research checklist."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "WebFetch",
  "elapsed_ms": 4620
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-20T08:34:03.126091+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "# Round 1 审稿任务 — Reviewer 1\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25 (ARR submission); 2026-08-02 (commitment)\n- **类型**: Long Paper\n- **正文页数限制**: 8 页（不含 Limitations、Ethics、References）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求）\n- **附录**: 可选补充材料\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下维度：\n\n1. **方法论严谨性**\n   - 问题形式化（ordinal classification for depth estimation）是否合理？定义是否清晰无歧义？\n   - 19 个统计特征的设计是否有充分理论/实证依据？特征间多重共线性（VIF>10 for 14-16/19 features）是否影响结论可靠性？\n   - EDD 指标定义（Eq. 1）是否严密？阈值 T=0.70 的选择是否充分论证？monotonicity assumption 的局限性讨论是否充分？\n   - Random Forest 作为主分类器的选择是否充分论证？与 XGBoost/LightGBM 收敛到 0.4pp 内是否真能说明\"信号在特征不在分类器\"？\n\n2. **实验设计与 Benchmark**\n   - Benchmark 构建（3 families × 3 strategies × 4 depths × 5000 samples）是否合理？为何选这3个模型（1-1.5B）？\n   - LoRA finetuning pipeline（r=16, α=32, lr=2e-4, 3 epochs）的超参选择是否有依据？\n   - BOS-seeded vs prompted generation：论文报告 −13.8pp 差异，是否充分讨论了影响？\n   - 评估方案（5-fold stratified CV, 200 trees）是否恰当？是否有数据泄漏风险？\n   - Reference model (Pythia-1.4B) 与 Pythia generator 重叠的 self-reference confound：4-11pp advantage 是否使 Pythia 结果不可比？Table 2 中 Pythia 标 † 是否足够？\n\n3. **泛化实验严谨性**\n   - Cross-model LOO transfer (mean 66.4%, d1-d3: 55.4%)：设计是否合理？d0 recall >98% 膨胀 headline 的问题？\n   - Cross-strategy transfer (59.1%, d1-d3: 45.9%)：d1/d2 boundary inversion 问题是否说明方法有根本局限？z-score normalization 修复只改善 logistic regression 不改善 RF 的含义？\n   - Cross-domain arXiv (74.1%)：仅一个域是否足够？C4/FineWeb FPR 34%/17% 说明什么？\n   - 14B cross-scale (mean 50.8%, EDD₀.₇₀=0)：5 重混淆因素下的结论表述是否审慎？\n\n4. **Baseline 比较公平性**\n   - Binoculars 11-feat RF (78.1%) vs 本文 19-feat RF (78.4%)：p>0.05，无显著差异。Merged 30-feat (82.6%) 的讨论是否充分？部署优势论证是否成立（1 reference model vs observer-performer pair）？\n   - DeBERTa-v3 end-to-end baseline 下降 16-32pp：是否因为 ordinal classification 对 neural encoder 本身就难？\n   - DetectGPT (28.8%), Min-K% Prob (33.2%)：这些 binary detector 用 CORAL calibration 后仍只 40.4%，比较框架是否公平（它们并非为 ordinal 设计）？\n\n5. **统计严谨性**\n   - Bootstrap CI (B=1000) 和 permutation test 的使用是否正确？\n   - 多重比较（9 cells × 多个 metrics）是否需要校正？\n   - 效应量报告是否充分？MAE=0.23, QWK=0.89 等指标选择是否恰当？\n\n请按以下结构输出审稿意见：\n- **Strengths**（逐条）\n- **Weaknesses**（分 Must-Fix / Should-Fix / Minor，每条说明理由并 cite 具体 Section/Table/Figure）\n- **Questions**（需作者澄清的技术问题）\n- **Missing References**（遗漏的重要相关工作）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "# Round 1 审稿任务 — Reviewer 1\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25 (ARR submission); 2026-08-02 (commitment)\n- **类型**: Long Paper\n- **正文页数限制**: 8 页（不含 Limitations、Ethics、References）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求）\n- **附录**: 可选补充材料\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下维度：\n\n1. **方法论严谨性**\n   - 问题形式化（ordinal classification for depth estimation）是否合理？定义是否清晰无歧义？\n   - 19 个统计特征的设计是否有充分理论/实证依据？特征间多重共线性（VIF>10 for 14-16/19 features）是否影响结论可靠性？\n   - EDD 指标定义（Eq. 1）是否严密？阈值 T=0.70 的选择是否充分论证？monotonicity assumption 的局限性讨论是否充分？\n   - Random Forest 作为主分类器的选择是否充分论证？与 XGBoost/LightGBM 收敛到 0.4pp 内是否真能说明\"信号在特征不在分类器\"？\n\n2. **实验设计与 Benchmark**\n   - Benchmark 构建（3 families × 3 strategies × 4 depths × 5000 samples）是否合理？为何选这3个模型（1-1.5B）？\n   - LoRA finetuning pipeline（r=16, α=32, lr=2e-4, 3 epochs）的超参选择是否有依据？\n   - BOS-seeded vs prompted generation：论文报告 −13.8pp 差异，是否充分讨论了影响？\n   - 评估方案（5-fold stratified CV, 200 trees）是否恰当？是否有数据泄漏风险？\n   - Reference model (Pythia-1.4B) 与 Pythia generator 重叠的 self-reference confound：4-11pp advantage 是否使 Pythia 结果不可比？Table 2 中 Pythia 标 † 是否足够？\n\n3. **泛化实验严谨性**\n   - Cross-model LOO transfer (mean 66.4%, d1-d3: 55.4%)：设计是否合理？d0 recall >98% 膨胀 headline 的问题？\n   - Cross-strategy transfer (59.1%, d1-d3: 45.9%)：d1/d2 boundary inversion 问题是否说明方法有根本局限？z-score normalization 修复只改善 logistic regression 不改善 RF 的含义？\n   - Cross-domain arXiv (74.1%)：仅一个域是否足够？C4/FineWeb FPR 34%/17% 说明什么？\n   - 14B cross-scale (mean 50.8%, EDD₀.₇₀=0)：5 重混淆因素下的结论表述是否审慎？\n\n4. **Baseline 比较公平性**\n   - Binoculars 11-feat RF (78.1%) vs 本文 19-feat RF (78.4%)：p>0.05，无显著差异。Merged 30-feat (82.6%) 的讨论是否充分？部署优势论证是否成立（1 reference model vs observer-performer pair）？\n   - DeBERTa-v3 end-to-end baseline 下降 16-32pp：是否因为 ordinal classification 对 neural encoder 本身就难？\n   - DetectGPT (28.8%), Min-K% Prob (33.2%)：这些 binary detector 用 CORAL calibration 后仍只 40.4%，比较框架是否公平（它们并非为 ordinal 设计）？\n\n5. **统计严谨性**\n   - Bootstrap CI (B=1000) 和 permutation test 的使用是否正确？\n   - 多重比较（9 cells × 多个 metrics）是否需要校正？\n   - 效应量报告是否充分？MAE=0.23, QWK=0.89 等指标选择是否恰当？\n\n请按以下结构输出审稿意见：\n- **Strengths**（逐条）\n- **Weaknesses**（分 Must-Fix / Should-Fix / Minor，每条说明理由并 cite 具体 Section/Table/Figure）\n- **Questions**（需作者澄清的技术问题）\n- **Missing References**（遗漏的重要相关工作）"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-20T08:34:30.144190+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27018
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-20T08:34:30.345419+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "# Round 1 审稿任务 — Reviewer 2\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25 (ARR submission); 2026-08-02 (commitment)\n- **类型**: Long Paper\n- **正文页数限制**: 8 页（不含 Limitations、Ethics、References）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求）\n- **附录**: 可选补充材料\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请重点审查以下维度：\n\n1. **新颖性与贡献度**\n   - Recursive generation depth estimation as ordinal classification：这个任务形式化在 NLP 社区的新颖度如何？是否有先前工作做过类似的深度区分（而非仅 human vs machine）？\n   - EDD 指标：是否是一个有意义的新指标？还是仅仅将 pairwise AUC 打包成一个数字？其理论意义和实用价值各如何？\n   - Depth Degradation Atlas（3×3 grid of model × strategy）：系统性实证 mapping 是否构成独立贡献？在缺少算法创新的情况下，这种 benchmark-driven 贡献对 EMNLP 是否足够？\n   - 标准 RF + 标准统计特征：pipeline 无算法创新，贡献主要在 task formalization + empirical characterization。这在 EMNLP 的接受标准下是否足够？\n   - 与 Binoculars 无显著差异（78.1% vs 78.4%）是否削弱了方法贡献？\n\n2. **Related Work 完整性**\n   - Model collapse theory 覆盖：Shumailov 2024, Dohmatob 2024b, Alemohammad 2024, Bertrand 2024, Seddik 2024, Gerstgrasser 2024 等是否覆盖了主要线索？是否遗漏 2025-2026 年重要工作？\n   - AI text detection：DetectGPT, Binoculars, Fast-DetectGPT, DivEye, GLTR, DNA-GPT 等覆盖是否全面？M4-SemEval 和 PAN 2026 shared task 是否应更详细讨论？\n   - Data provenance / membership inference：TROVE (Zhu et al., 2025), EditLens (Thai et al., 2026) 的定位区分是否清晰？\n   - Ordinal classification：CORAL, CLOC 作为 baseline 是否足够？是否遗漏了更强的 ordinal methods？\n   - 是否遗漏了与 recursive/iterative generation 直接相关的 depth estimation 工作？\n\n3. **写作质量与 Narrative**\n   - Abstract：信息密度极高（数字密集），是否过载？读者能否在首次阅读时把握核心贡献？\n   - Introduction narrative flow：问题（recursive loop）→ 动机（depth matters for collapse）→ gap（no ordinal estimation）→ approach（statistical fingerprints + RF）→ contributions 是否清晰连贯？\n   - Headline metrics 呈现：是否始终并列 4-class accuracy 和 d1-d3 balanced accuracy 以避免 d0 膨胀？检查 Abstract、§4.1、§5、§6 中的数字呈现。\n   - Limitations section：是否诚实全面？检查是否覆盖了 full-replacement vs accumulation、scale limitation、BOS vs prompted、reference model dependency、single seed、cross-strategy deployment constraint。\n   - 术语一致性：全文是否统一使用同一套术语？\n\n4. **格式合规（严格检查）**\n   - 主文（Abstract → §6 Discussion and Conclusion）是否在 8 页以内？Limitations 从第几页开始？\n   - `\\usepackage[review]{acl}` 模板是否正确使用？\n   - 匿名性检查：`\\author{Anonymous}` 是否正确？正文中是否有自引泄露身份的句子？（检查 \"we previously\" / \"our prior work\" / GitHub links 等）\n   - 参考文献格式：是否一致？arXiv preprint 是否有已发表版本可替换？\n   - Ethics Statement 是否存在且内容充分？\n\n5. **EMNLP 2026 适合度**\n   - 论文整体水平评估：Main Conference / Findings / Borderline？\n   - 贡献量是否支撑 Long Paper？还是 Short Paper 更合适？\n   - 对 NLP 社区的影响力和受众范围预估\n\n请按以下结构输出审稿意见：\n- **Strengths**（逐条）\n- **Weaknesses**（分 Must-Fix / Should-Fix / Minor，每条说明理由并 cite 具体 Section/Table/Figure）\n- **Questions**（需作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作，需 web search 确认）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "# Round 1 审稿任务 — Reviewer 2\n\n## 论文信息\n- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25 (ARR submission); 2026-08-02 (commitment)\n- **类型**: Long Paper\n- **正文页数限制**: 8 页（不含 Limitations、Ethics、References）\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无匿名期要求）\n- **附录**: 可选补充材料\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请重点审查以下维度：\n\n1. **新颖性与贡献度**\n   - Recursive generation depth estimation as ordinal classification：这个任务形式化在 NLP 社区的新颖度如何？是否有先前工作做过类似的深度区分（而非仅 human vs machine）？\n   - EDD 指标：是否是一个有意义的新指标？还是仅仅将 pairwise AUC 打包成一个数字？其理论意义和实用价值各如何？\n   - Depth Degradation Atlas（3×3 grid of model × strategy）：系统性实证 mapping 是否构成独立贡献？在缺少算法创新的情况下，这种 benchmark-driven 贡献对 EMNLP 是否足够？\n   - 标准 RF + 标准统计特征：pipeline 无算法创新，贡献主要在 task formalization + empirical characterization。这在 EMNLP 的接受标准下是否足够？\n   - 与 Binoculars 无显著差异（78.1% vs 78.4%）是否削弱了方法贡献？\n\n2. **Related Work 完整性**\n   - Model collapse theory 覆盖：Shumailov 2024, Dohmatob 2024b, Alemohammad 2024, Bertrand 2024, Seddik 2024, Gerstgrasser 2024 等是否覆盖了主要线索？是否遗漏 2025-2026 年重要工作？\n   - AI text detection：DetectGPT, Binoculars, Fast-DetectGPT, DivEye, GLTR, DNA-GPT 等覆盖是否全面？M4-SemEval 和 PAN 2026 shared task 是否应更详细讨论？\n   - Data provenance / membership inference：TROVE (Zhu et al., 2025), EditLens (Thai et al., 2026) 的定位区分是否清晰？\n   - Ordinal classification：CORAL, CLOC 作为 baseline 是否足够？是否遗漏了更强的 ordinal methods？\n   - 是否遗漏了与 recursive/iterative generation 直接相关的 depth estimation 工作？\n\n3. **写作质量与 Narrative**\n   - Abstract：信息密度极高（数字密集），是否过载？读者能否在首次阅读时把握核心贡献？\n   - Introduction narrative flow：问题（recursive loop）→ 动机（depth matters for collapse）→ gap（no ordinal estimation）→ approach（statistical fingerprints + RF）→ contributions 是否清晰连贯？\n   - Headline metrics 呈现：是否始终并列 4-class accuracy 和 d1-d3 balanced accuracy 以避免 d0 膨胀？检查 Abstract、§4.1、§5、§6 中的数字呈现。\n   - Limitations section：是否诚实全面？检查是否覆盖了 full-replacement vs accumulation、scale limitation、BOS vs prompted、reference model dependency、single seed、cross-strategy deployment constraint。\n   - 术语一致性：全文是否统一使用同一套术语？\n\n4. **格式合规（严格检查）**\n   - 主文（Abstract → §6 Discussion and Conclusion）是否在 8 页以内？Limitations 从第几页开始？\n   - `\\usepackage[review]{acl}` 模板是否正确使用？\n   - 匿名性检查：`\\author{Anonymous}` 是否正确？正文中是否有自引泄露身份的句子？（检查 \"we previously\" / \"our prior work\" / GitHub links 等）\n   - 参考文献格式：是否一致？arXiv preprint 是否有已发表版本可替换？\n   - Ethics Statement 是否存在且内容充分？\n\n5. **EMNLP 2026 适合度**\n   - 论文整体水平评估：Main Conference / Findings / Borderline？\n   - 贡献量是否支撑 Long Paper？还是 Short Paper 更合适？\n   - 对 NLP 社区的影响力和受众范围预估\n\n请按以下结构输出审稿意见：\n- **Strengths**（逐条）\n- **Weaknesses**（分 Must-Fix / Should-Fix / Minor，每条说明理由并 cite 具体 Section/Table/Figure）\n- **Questions**（需作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作，需 web search 确认）"
  }
}
```

</details>

---


### Tool call

_source line 1273 · 2026-05-20T08:34:31.654057+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "review_chat_id": "oc_db3bd143165620ee6950e6ef0826eec8"
  }
}
```

</details>

---


### Tool result

_source line 1274 · 2026-05-20T08:34:32.070890+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1725
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-20T08:34:33.733188+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2079
}
```

</details>

---


### Assistant

_source line 1276 · 2026-05-20T08:34:43.828755+00:00_

已派发完毕：

- **Reviewer 1** (方法严谨性 + 实验设计) → 已启动
- **Reviewer 2** (新颖性 + 完整性 + 写作质量) → 已启动
- **视觉审查 Agent** → 已启动

三线并行执行，等待 Reviewer 返回初审意见后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1277 · 2026-05-20T08:39:55.137228+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

## 论文信息
**标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## 总体评分

**Overall**: 3.0 — Findings
**一句话总结**: 问题定义新颖、实验体量充足，但核心方法在 in-distribution 上与已有 Binoculars 特征持平（p>0.05），在 cross-strategy/cross-scale 上大幅退化，headline 数字被 d0 近完美可分性膨胀，实际深层区分能力（d1-d3）远低于报告值。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心 claim 有部分实验支撑，但 self-reference confound、Binoculars 平局、cross-strategy/scale 失败构成重大方法论缺口 |
| Excitement | 3.0/5 | 问题定义（ordinal depth estimation）有新意，Degradation Atlas 有系统价值，但方法性能未超越现有 binary detector 特征的简单重用 |
| Reproducibility | 4/5 | 附录细节充分（超参、硬件、种子），承诺代码/数据公开，但 LoRA pipeline 缺少超参敏感性分析 |
| Confidence | 4/5 | 熟悉 model collapse、AI text detection、ordinal classification 相关文献 |

---

## 主要优势

**S1. 问题定义新颖且有实际价值。** 将递归生成深度估计形式化为 ordinal classification（Section 3.1），区别于 binary human-vs-machine detection，是一个自然且未被充分探索的方向。这对理解训练数据污染程度有直接意义。

**S2. Degradation Atlas 系统性强。** Section 4 的 atlas（3 families × 3 strategies × 4 depths）提供了关于递归生成如何改变文本统计特性的系统实证图景。Feature consistency 分析（Section 4.2）、monotonicity 分析（Section 4.3）、EDD 分析（Section 4.4）构成了一个有价值的 empirical contribution，独立于分类器性能。

**S3. 评估方案设计合理。** 使用 ordinal-specific metrics（QWK=0.89, MAE=0.23），5-fold stratified CV，bootstrap CI (B=1000)，permutation test，体现了统计素养。CORAL ordinal regression 对照也是恰当的。

**S4. 消融实验覆盖面广。** 附录 B.1-B.29 涵盖了 permutation importance、feature trajectories、per-class recall、DCOL iteration、temperature robustness、generation length、feature group ablation、Binoculars decomposition、domain bias、wild-data calibration、reference model ablation、cross-scale 等多个角度，展现了严肃的实验态度。

**S5. 引用质量高。** 74 篇引用中 63 篇 OpenAlex 验证通过，7 篇 not_found 均为真实论文（OpenAlex 覆盖缺口），无伪造引用。cross-check 显示 0 missing_bib（所有 \cite 都有对应 bib 条目）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Binoculars 特征平局严重削弱方法论贡献**
- 具体位置：Section 5.1, Table 4
- 问题：论文的 19-feature RF 达到 78.4%，而 Binoculars 的 11 features 用相同 RF 达到 78.1%，p>0.05 无显著差异。Merged 30-feature 达到 82.6%，但这说明信息是互补的、而非本文特征优于已有特征。论文声称的部署优势（"1 reference model vs observer-performer pair"，Section 5.1）是工程论证而非科学贡献。
- 为什么影响接收：如果现有 binary detector 的特征简单重新标定（CORAL calibration）就能达到相同 ordinal 性能，则本文 19 个统计特征的设计贡献被大幅稀释。论文的核心 claim "discriminative signal resides in feature design"（Section 5.1）恰好被 Binoculars 平局所反驳——信号不在*这些*特征，而在*任何*能捕获分布偏移的特征。
- 建议修改方向：(1) 在 abstract/intro 诚实报告 Binoculars 平局；(2) 将 contribution 重新定位为"问题定义 + atlas + benchmark"而非"特征设计"；(3) 分析为何 merged 30-feature 提升 4.2pp——互补信息来自哪里？

**N2** [critical] **Self-reference confound 使 Pythia 结果不可比，膨胀 headline 数字**
- 具体位置：Section 3.3（reference model = Pythia-1.4B），Table 2（Pythia 行标 †），Appendix B.13（Table 16）
- 问题：Pythia-1.4B 同时是 generator（3 个 family 之一）和 reference model（特征提取的唯一模型）。Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 的 reference model ablation 显示换用 GPT-2 XL 作 reference 时 accuracy 降至 67.3%（−11pp）。这意味着 headline "78.4%" 中 Pythia 行的贡献包含了 self-reference 优势。
- 为什么影响接收：1/3 的 in-distribution 结果存在系统性偏差。cross-model transfer（Table 5）中 Pythia holdout 行（62.4%）低于 OLMo（69.2%）反映了这一 confound 的传递。如果排除 Pythia 或使用 non-Pythia reference，headline 数字会下降。
- 建议修改方向：(1) 主实验增加一个 non-overlapping reference model 的全量结果（如 GPT-NeoX）；(2) 报告 "excluding Pythia" 的 mean accuracy 作为 conservative estimate；(3) 将 † caveat 从脚注提升到正文讨论。

**N3** [critical] **d0 膨胀 headline 数字，d1-d3 实际性能远低于报告值**
- 具体位置：Abstract（"68.9-85.9% accuracy"），Section 4.1（"Depth-0 recall exceeds 97%"），Table 5（cross-model mean 66.4%），Table 6（cross-strategy 59.1%）
- 问题：d0（人类文本）与 d1+ 的区分本质上是 binary human-vs-machine detection，已被大量现有工作解决。真正有价值的是 d1-d2-d3 的细粒度区分。但 cross-model d1-d3 仅 55.4%（chance 33%），cross-strategy d1-d3 仅 45.9%。Abstract 报告 "68.9-85.9%" 和 "cross-model transfer reaches 66.4%" 时没有突出 d1-d3 的大幅下降。
- 为什么影响接收：这是一种 overclaiming——论文标题和 framing 围绕 "depth estimation"，但实际方法的深层区分能力接近 chance。读者会被 headline 数字误导。
- 建议修改方向：(1) Abstract 和 Introduction 必须报告 d1-d3 准确率；(2) 正文中将 d0 结果与 d1-d3 结果明确分开讨论；(3) 承认深层区分是当前方法的主要瓶颈。

**N4** [critical] **Cross-strategy 和 cross-scale 失败动摇方法的泛化 claim**
- 具体位置：Section 5.3（Table 6, 59.1%），Section 5.4（14B: 50.8%, EDD₀.₇₀=0），Limitations（p.9）
- 问题：Cross-strategy transfer d1-d3 仅 45.9%（接近 chance 33%），且出现 d1/d2 boundary inversion。z-score normalization 只修复 logistic regression 不修复 RF（Section 5.3），说明不同策略产生了根本不同的深度信号。14B cross-scale mean 50.8%、EDD₀.₇₀=0 意味着方法在更大模型上完全失效。论文在 Limitations 中承认了这些，但 abstract/introduction 的 framing 仍然偏乐观。
- 为什么影响接收：一个 depth estimation 方法如果只在训练时见过的 strategy 上工作、且无法推广到实际部署的模型规模（7B/14B），其实际应用价值有限。这些不仅是 limitations，而是对核心 claim 的根本质疑。
- 建议修改方向：(1) Abstract/intro 中对泛化限制进行显著标注，而非仅在 Limitations 提及；(2) 分析 cross-strategy 失败的根本原因——是特征空间不重叠还是 ordinal 结构消失？(3) 为 14B 实验分离至少一个 confound（如用 14B reference model）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **多重共线性与可解释性 claim 的矛盾**
- 具体位置：Section 3.3（"VIF>10 for 14-16/19 features"），Section 4.2（feature importance via Gini/SHAP）
- 问题：14-16/19 个特征 VIF>10 意味着严重的多重共线性。虽然 RF 对共线性相对鲁棒（就预测而言），但 Gini importance 和 SHAP 在共线性下不稳定——重要性会在相关特征间随机分配。Section 4.2 基于 Gini 和 SHAP 的特征重要性排序在这种共线性下是不可靠的。
- 建议：(1) 使用 permutation importance（已在 Appendix B.2 做了，结论一致则强化论证）；(2) 对 SHAP 结果增加 caveat；(3) 或者使用降维后的特征子集做可解释性分析。

**W2** [warning] **LoRA 微调超参无 ablation**
- 具体位置：Section 3.2（"LoRA (r=16, α=32, lr=2e-4, 3 epochs)"），Appendix A（Table 7）
- 问题：LoRA rank、learning rate、epoch 数直接影响生成文本的质量和多样性，进而影响 depth signatures。r=16 是一个特定选择——更高的 rank 产生更接近 full fine-tuning 的效果，可能产生不同的退化模式。论文未提供任何超参敏感性分析。
- 建议：至少做一个 LoRA rank ablation（r=4, 8, 16, 32），验证 depth signatures 对微调强度的鲁棒性。

**W3** [warning] **BOS-seeded generation 限制生态效度**
- 具体位置：Section 3.2（generation pipeline），Appendix B.27（Table 29, −13.8pp for prompted generation）
- 问题：主实验全部使用 BOS-seeded generation（从 BOS token 开始自由生成 512 tokens）。但现实中的递归生成（如 synthetic data pipeline、LLM 辅助写作）几乎都是 prompted generation。Appendix B.27 承认 prompted generation accuracy 下降 13.8pp。这不是边缘问题，而是核心 validity concern。
- 建议：(1) 将 prompted generation 结果从附录提升到正文；(2) 讨论 BOS-seeded 与 prompted 在什么条件下等价/不等价；(3) 考虑混合 BOS/prompted 的训练数据。

**W4** [warning] **单域 cross-domain 测试不够充分**
- 具体位置：Section 5.4（"cross-domain arXiv 74.1%"），Appendix B.11（Table 13, C4 FPR 34%, FineWeb FPR 17%）
- 问题：cross-domain 仅测试 arXiv（学术文本，本身有特定的文本统计特征）。WikiText-103 虽然用于 wild-data calibration（B.11），但不是 cross-domain 泛化测试。C4 上 34% 的 FPR 和 FineWeb 上 17% 的 FPR（Table 13）表明方法在非学术 web 文本上产生大量误报。
- 建议：增加至少 2-3 个域（如 news、social media、code）的 cross-domain 评估，或者将 C4/FineWeb FPR 数据在正文中讨论而非藏在附录。

**W5** [warning] **多重比较未校正**
- 具体位置：Appendix B.2（"multiple pairwise comparisons that were not corrected for multiplicity"），Table 15（paired t-tests）
- 问题：全文进行了大量统计检验（9 cells 的准确率比较、Table 15 的 pairwise comparisons、各种 ablation 中的 p 值），但均未做 Bonferroni/FDR 校正。Appendix B.2 中论文自己承认了这一点。Table 15 有 6 个 pairwise comparisons，p<0.05 可能仅因多重比较。
- 建议：对所有包含多组比较的结果应用 Holm-Bonferroni 或 BH-FDR 校正，或者在正文中标注 adjusted p-values。

**W6** [warning] **EDD 阈值 T=0.70 的论证依据不够充分**
- 具体位置：Section 3.4（Eq. 1），引用 Hosmer & Lemeshow (2000)
- 问题：T=0.70 引自 Hosmer & Lemeshow 的 AUC discrimination standard，但该标准是为 binary logistic regression 的 c-statistic 设计的，直接迁移到 multi-class ordinal 的 pairwise AUC 缺乏理论依据。虽然 Section 3.4 提供了 T∈{0.65,0.70,0.75,0.80} 的 sensitivity analysis，但没有解释为何 0.70 是 "natural" 的。
- 建议：(1) 讨论为何 binary AUC 的 discrimination 标准可迁移到 ordinal pairwise AUC；(2) 或者提出一个 data-driven 的阈值选择方法。

---

## 小问题（不影响接收）

- **M1**: Orphan bib entries: `dsir2023` 和 `qurating2024` 在 .bib 中定义但未在正文 \cite，应清理。
- **M2**: Table 2 脚注 1（"RF binary classifiers use 500 trees; the main 4-class RF uses 200 trees"）——为何 binary 和 4-class 用不同数量的树？未见讨论。
- **M3**: Section 4.3 "all 12 AUC profiles in our benchmark decay monotonically" 与 Appendix B.14 中 GPT-2 XL 14B d4→d5 non-monotonic 的发现有 tension——应在正文中注明 monotonicity 仅在 1-1.5B 范围内成立。
- **M4**: Figure 1 的 atlas heatmap 中颜色强度编码 RF Gini importance，但 W1 中指出的共线性问题意味着这些重要性值不稳定。
- **M5**: Appendix B.28 "Cross-strategy conditional decomposition" 中 naïve pooled classifier 的讨论（"the two-stage pipeline... yields 11.5pp gain"）应考虑提到正文，因为它直接说明了 cross-strategy 失败的解决方向。

---

## Questions（需作者澄清）

**Q1**: 如果使用完全不同架构的 reference model（如 Mamba/RWKV 而非 Transformer），特征提取的结果会如何？当前 reference model ablation（B.13）仅在 Transformer LM 内部换模型。

**Q2**: Perplexity tail features 真正捕获的是 "depth-specific signature" 还是仅仅是文本质量的代理（quality proxy）？一段由 depth-1 生成但碰巧质量较差的文本，与一段 depth-2 的 "正常" 文本，特征能否区分？

**Q3**: Cross-strategy 中 z-score normalization 修复 logistic regression 但不修复 RF 的原因是什么？这是否说明 RF 学到了 strategy-specific 的非线性决策边界，而这些边界在 strategy 间不可迁移？

**Q4**: DCOL iteration（Appendix B.5）中 convergence vs failure 的决定因素是什么？有没有可靠的 stopping criterion？

**Q5**: 14B 实验中 5 个 confounders（Section 5.4）能否通过实验设计分离？例如用 14B 模型做 reference model 提取特征，是否能消除 scale mismatch confound？

---

## Missing References

1. **Min-K%++ (Zhang et al., 2024)**: Min-K% Prob 的改进版本，在 membership inference 上有更好的性能，应作为 baseline 考虑。
2. **Ordinal classification 综述**: 论文引用了 Frank (2001), McCullagh (1980), Rennie (2005) 等经典工作，但缺少对近年 ordinal classification 在 NLP 中的应用的系统综述引用。
3. **RAID benchmark (Dugan et al., 2024)**: 虽然已引用，但未在实验中使用其数据或评估框架进行比较——考虑到 RAID 专门为 robustly evaluating detection 设计，解释为何不采用会更好。

---

## 格式合规检查

- **页数**: 正文 8 页（pp.1-8），Limitations 在 p.9 开头，References 从 p.10 开始。符合 EMNLP 2026 的 8 页限制。
- **匿名**: 使用 `\usepackage[review]{acl}`，标题页为 "Anonymous ACL submission"，正文未见去匿名化内容。符合 double-blind 要求。
- **Limitations section**: 存在（p.9），覆盖了 full-replacement vs accumulation、experimental setting、cross-strategy、controlled setting 等主要限制。
- **Ethics statement**: 存在（p.10），讨论了潜在滥用风险。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1278 · 2026-05-20T08:40:06.121740+00:00_

Reviewer 1 审稿意见已收到。Overall 3.0 (Findings)，4 个 critical issues（Binoculars 平局、self-reference confound、d0 膨胀、泛化失败）。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1279 · 2026-05-20T08:40:14.623902+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成，已提交给 Review Director。

**核心判断**: Overall 3.0（Findings）。问题定义新颖、实验体量大，但四个 critical 问题影响接收决定：

1. **Binoculars 平局**（78.1% vs 78.4%, p>0.05）——19-feature 设计的增量贡献不成立
2. **Self-reference confound**——Pythia 同时做 generator 和 reference model，1/3 结果存在系统偏差
3. **d0 膨胀 headline**——cross-model d1-d3 仅 55.4%（报告 66.4%），cross-strategy d1-d3 仅 45.9%（报告 59.1%）
4. **Cross-strategy/scale 泛化失败**——14B EDD₀.₇₀=0，方法在实际模型规模上完全失效

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1280 · 2026-05-20T08:40:20.304127+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director"
}
```

</details>

---


## Round 118

## Round 118

6 recorded events


### User

_source line 1281 · 2026-05-20T08:41:59.732630+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper

---

## 总体评分

**Overall**: 3.0 — Findings
**一句话总结**: 论文提出了一个新颖且有意义的任务形式化（递归生成深度的序数分类），实验设计系统全面，但 pipeline 缺乏算法创新（标准 RF + 标准统计特征），模型规模受限于 ≤1.5B，且未能显著超越现有 Binoculars 方法，整体贡献更适合 Findings 而非主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计系统（3×3 grid, 5-fold CV, cross-validation），但单 seed 主实验、≤1.5B 规模、仅 full-replacement 设置限制了结论的普适性 |
| **Excitement** | 2.5/5 | 问题本身及时且重要（递归污染是真实威胁），但方法是标准 RF 无创新，且与 Binoculars 无显著差异，降低了兴奋度 |
| **Reproducibility** | 4/5 | 附录极其详尽（29 个子节），超参数、特征列表、生成协议均有完整描述，复现门槛低 |
| **Datasets** | 4/5 | 180K benchmark 涵盖 3 模型×3 策略×4 深度，是一个有价值的资源贡献 |
| **Software** | 2/5 | 未见软件/代码发布承诺（Ethics Statement 提到"code and data will be released upon acceptance"但细节不清） |
| **Reviewer Confidence** | 4/5 | 仔细阅读全文及全部附录，核查了引用，搜索了 related work |

---

## 主要优势

**S1. 新颖且有意义的任务形式化。** 将递归生成深度估计从二元检测（human vs. machine）扩展为序数分类（d0–d3）是一个有价值的概念贡献。在 model collapse 理论日益成熟的背景下（Shumailov et al., 2024; Dohmatob et al., 2024），区分"生成了几轮"比仅区分"是否生成"具有更强的实用价值。§1 的动机论证清晰：depth matters for collapse severity。

**S2. 系统的实验设计和全面的泛化分析。** 3×3 model-strategy grid（§3.2）、cross-model transfer（§5.2, Table 5）、cross-strategy transfer（§5.3, Table 6）、cross-domain 评估（§5.4, Appendix B.11）、7–14B 规模探索（Appendix B.14）、d0–d5 深度扩展（Appendix B.17）、种子稳健性（Appendix B.24）——分析轴覆盖广泛，论文在经验层面是扎实的。

**S3. Depth Degradation Atlas 的系统映射。** §4 对 3×3 grid 中每个 cell 的特征行为进行了系统描述，发现了解码策略诱导的质变差异（§4.5）：nucleus 保持单调衰减、temperature scaling 引入 d1/d2 boundary inversion、top-k truncation 移除 depth-discriminative 的 low-probability tokens。这些发现对理解递归生成的统计机制有参考价值。

**S4. EDD 指标作为操作化工具。** 虽然 EDD 本质是 pairwise AUC 的聚合（Definition 1, §3.4），但它提供了一个单一数字来回答"深度信号能传多远"的问题，实用价值明确。12 个 AUC profile 全部单调递减（§3.4）从经验上验证了单调性假设。

**S5. Limitations 部分诚实全面。** 覆盖了 full-replacement vs. accumulation、scale limitation、BOS vs. prompted、reference model dependency、single seed、cross-strategy deployment constraint 等核心局限（pp. 9–10）。这是值得肯定的学术诚实度。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Pipeline 缺乏算法创新，贡献主要在 task formalization + empirical characterization**
- 具体位置：§3.3（Feature Design）、§3.4（Classifiers）
- 问题：核心 pipeline 是 19 个标准统计特征（perplexity moments/quantiles、surprisal statistics、lexical diversity、n-gram repetition）+ 标准 Random Forest（200 trees, uncontrained depth, 5-fold CV）。特征和分类器均为已有方法的直接应用，无任何算法层面的创新。论文自己也承认"discriminative signal resides in feature design, not classifier choice"（Abstract），但 feature design 本身也是标准统计量的组合。
- 为什么影响接收：EMNLP 主会议期望至少在方法或理论层面有所推进。纯 benchmark-driven + empirical characterization 的贡献更适合 Findings track。论文对 NLP 社区的方法论贡献有限——后续研究者不会从中学到新的技术手段。
- 建议修改方向：(a) 引入针对序数结构设计的特征或损失函数；(b) 探索利用 LLM 内部表示（hidden states, attention patterns）的方法；(c) 至少在一个维度上展示超越现有 baseline 的显著优势。

**N2** [critical] **与 Binoculars 无显著差异（78.1% vs. 78.4%），削弱方法贡献**
- 具体位置：§5.1, Table 4, Appendix B.25
- 问题：论文承认"Binoculars 11 features" 和 "Our 19 features" 在 cross-model transfer 上几乎持平（Table 4: RF 78.1% vs. Binoculars 78.4%，差异 −0.3pp）。Appendix B.25 中，Binoculars 在 cross-perplexity calibration（11 cross-configurations）上达到 69.8%，与 19-feature pipeline 的 cross-model mean 接近。Appendix B.26 的 feature ablation decomposition 也显示 Binoculars 的 6 个 cross-perplexity 特征单独就能达到 75.9%（Table 26），仅比完整 pipeline 低 2.2pp。
- 为什么影响接收：如果一个已有方法（Binoculars, 2024）能达到同等性能，论文的 pipeline 贡献就大打折扣。论文试图以"可解释性"和"多特征互补"来辩护，但 Binoculars 本身也基于可解释的 perplexity 对比。这使得论文的核心方法论贡献变得模糊——读者会合理地问：为什么不直接用 Binoculars？
- 建议修改方向：(a) 展示在 Binoculars 失败的场景中 pipeline 的独特优势；(b) 将 Binoculars 特征纳入 pipeline 并展示互补增益；(c) 更诚实地定位贡献为"empirical study of depth estimation"而非"novel pipeline"。

**N3** [critical] **模型规模严重受限（≤1.5B），2026 年的实用性存疑**
- 具体位置：§3.2（Model families）、Appendix B.14（7–14B）、Limitations
- 问题：主实验仅涵盖 Pythia-1.4B、OLMo-1B、GPT-2 XL（1.5B）三个 ≤1.5B 的模型。Appendix B.14 的 14B 扩展实验显示 EDD_{τ=0.70} 仅为 d1（即相邻深度区分在 d2 处已失效），4-class accuracy 61%（仅略高于 4× chance=25%）。这表明 depth signal 随模型规模增大而迅速衰减。
- 在 2026 年，主流模型为 7B–70B+（Llama-3, Qwen2.5 等），≤1.5B 的结论对社区的实用参考价值有限。14B 结果不仅不支持 scalability，反而提供了"scaling 可能破坏 depth signal"的证据。
- 为什么影响接收：这不仅是 limitation，而是动摇了论文核心 claim 的根基。如果 depth signal 在实用规模上消失，那么"depth estimation via statistical fingerprints"这一方法论的价值就大打折扣。
- 建议修改方向：(a) 至少在 7B 规模上提供完整的 3×3 grid 实验；(b) 如果 signal 确实随 scale 衰减，应将其作为论文的核心发现之一进行深入分析，而非放在附录。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Abstract 信息密度过载**
- 具体位置：Abstract（p.1）
- 问题：Abstract 中至少包含 10+ 个具体数字（68.9%、39-45%、0.6pp、68.4%、55.4%、69.5%、50.8%、2×、EDD_{τ=0.70}、14B 等），读者首次阅读很难提取核心信息。关键信息被数字洪流淹没。
- 建议：精简到 3-4 个最关键的数字，将其余移至 Introduction 或 Results。Abstract 应让读者 30 秒内理解：(1) 问题是什么，(2) 方法是什么，(3) 最重要的发现是什么。

**W2** [warning] **d0 膨胀导致 headline metrics 误导性**
- 具体位置：Abstract、§4.1、§5、§6
- 问题：d0（human text）recall >97%（Table 8, Appendix B.4），几乎完美可分。这使得 4-class accuracy（68.9%）显著高估了 depth estimation 的真实难度。论文在大多数地方确实并列报告了 d1-d3 balanced accuracy（39-45%），但 Abstract 和 §6 的标题数字仍以 4-class accuracy 为主打。§8 Table 5 中 cross-model transfer 的 66.4% 也包含 d0 膨胀。
- 建议：在所有 headline 位置（Abstract、Conclusion 的首句）优先报告 d1-d3 balanced accuracy，将 4-class accuracy 作为补充。这样更诚实地反映 depth estimation 的真实性能。

**W3** [warning] **Full-replacement 设置与现实场景脱节**
- 具体位置：§3.2（Generation pipeline）、Limitations
- 问题：Benchmark 中每个深度完全替换上一代文本（full-replacement recursive chain），但现实中的递归污染是 accumulation 模式——真实数据与合成数据按未知比例混合（Gerstgrasser et al., 2024）。论文在 Limitations 中承认了这一点，但 accumulation 设置的缺失使论文的"practical implications"主张（§6 第2段提到的 data curation 应用）缺乏实验支撑。
- 建议：至少提供一个 accumulation 设置的 pilot 实验，或更明确地将论文定位为"controlled laboratory study"而非面向部署的方法。

**W4** [warning] **EDD 指标的理论动机薄弱**
- 具体位置：§3.4, Definition 1
- 问题：EDD 本质上是"所有连续 pair AUC 超过阈值 τ 的最大深度"。这是一个操作化便利，而非有理论深度的指标。τ=0.70 的选择借用了 Hosmer & Lemeshow (2000) 的 AUC 分类标准（"acceptable discrimination"），但 (a) 该标准来自医学统计的二元分类场景，移植到多深度 ordinal 问题是否合适未被论证；(b) τ 的选择对 EDD 值极为敏感——§5.4 提到 τ=0.80 时"several cells lose one depth level"。如果核心指标的值因阈值选择而大幅变化，其作为稳健衡量工具的价值就减弱了。
- 建议：(a) 报告 EDD 在 τ∈{0.60, 0.65, 0.70, 0.75, 0.80} 范围内的完整 sensitivity 分析（而非仅在 Limitations 中提及）；(b) 考虑一个不依赖硬阈值的连续版 EDD，如 AUC-under-the-AUC-curve。

**W5** [warning] **Depth Degradation Atlas 的贡献独立性存疑**
- 具体位置：§4
- 问题：Atlas 的核心发现是"不同解码策略诱导不同的退化轨迹"（§4.5），但这些发现的 evidence 基本来自论文自己设计的 19 个特征的行为模式（perplexity compression、tail erosion、distributional shift 等）。换言之，Atlas 是用设计来捕捉 depth signal 的特征来描述 depth signal 的变化——这存在一定的循环性。Atlas 缺乏独立于 pipeline 的分析维度（如 semantic coherence、factual accuracy、human evaluation）来验证其发现。
- 建议：引入至少一个与 pipeline 特征正交的分析维度，或更明确地将 Atlas 定位为"pipeline 特征的可视化和解读"而非独立贡献。

**W6** [warning] **Cross-strategy transfer 严重不足（59.1%），部署前景堪忧**
- 具体位置：§5.3, Table 6
- 问题：Cross-strategy transfer accuracy 仅 59.1%（d1-d3: 45.9%），比 in-distribution 低约 10pp，比 cross-model 低约 7pp。论文承认"structurally distinct degradation trajectories"是原因，并提出 two-stage pipeline（先识别策略再分类深度），但 strategy identification 本身仅 57.8%（3-class）。这意味着在 deployment 中，如果目标文本的解码策略未知（这是最常见的情况），pipeline 性能会严重退化。
- 建议：(a) 讨论是否存在 strategy-agnostic 特征子集；(b) 将 cross-strategy 结果提升到主文而非仅作为一个小节；(c) 坦诚讨论这对实际部署的影响。

---

## 小问题（不影响接收）

**M1.** 2 个 orphan bib 条目（dsir2023, qurating2024）：已定义但全文未引用，应清理。

**M2.** 引用 author 顺序 mismatch：alemohammad2024_mad（bib 首作者 Alemohammad vs. OpenAlex 首作者 Casco-Rodriguez）、guo2024_biscope（bib 首作者 Guo vs. 实际首作者 Cheng）、hosmer2000（bib 年份 2000 vs. 可能指第 1 版 1989 或第 2 版 2000，OpenAlex 匹配到 1990）。建议核实。

**M3.** 主文频繁引用附录：§4–§6 中几乎每段都有"(Appendix B.X)"引用，阅读体验碎片化。建议将最关键的 appendix 内容（如 per-class recall Table 8、feature importance Figure 1）提升到主文。

**M4.** 术语"depth"在不同语境中的含义：§1 引入时指 recursive generation depth（生成迭代次数），但 §3.5 的 Theoretical Grounding 中引用 model collapse 理论的"depth"指 training iterations。两者相关但不完全等价，建议在首次出现时明确区分。

**M5.** Table 1（p.4）的 feature 命名需要更好的说明：如 `p90_ppl`, `p75_ppl` 等缩写对首次阅读者不友好，建议在正文中提供至少 2-3 个关键特征的直觉解释。

---

## Questions（需作者澄清）

**Q1.** 14B 实验（Appendix B.14）中 EDD 降至 d1 是否意味着在 7B+ 规模下，depth estimation via statistical fingerprints 从根本上不可行？如果是，论文的核心方法论前提是否需要重新审视？

**Q2.** Table 4 中 Binoculars 11-feature 和 19-feature pipeline 的差异仅 −0.3pp，但 Binoculars 无需 reference model 的 perplexity 计算（使用 observer-performer 架构自包含）。在计算效率和 reference-model-free 的优势下，19-feature pipeline 的实际优势是什么？

**Q3.** §4.5 报告 temperature 策略在 d1/d2 boundary 出现 inversion。这是否意味着在 temperature sampling 下 depth estimation 本质上是不可靠的？还是 pipeline 能通过其他特征补偿这一 inversion？

**Q4.** Cross-seed replication（Appendix B.24）仅用 3 个 seed 在 cross-model LOO 设置下测试，std=0.06pp。但主 benchmark 的 in-distribution 实验仅用 seed=42。能否提供 in-distribution 设置下的 multi-seed 结果？

**Q5.** 论文声称"perplexity tail family dominates"（§4.2），但 SHAP 分析（Appendix B.2）显示 `var_surprisal` 也在 top-2 features 中。surprisal variance 和 perplexity tail（如 p90_ppl）在信息论上有何区别？它们是否只是同一信号的不同视角？

---

## Missing References（遗漏的重要相关工作）

**MR1. [critical]** **Markovian Generation Chains in Large Language Models** (arxiv:2603.11228, ICLR 2026). 该论文直接研究文本被 LLM 迭代处理时的 Markov 链动态——包括 convergence to fixed points、cycle behavior、decoding strategy 的影响等。这与本文的 recursive generation setup 和 Depth Degradation Atlas 的 strategy-dependent trajectory 发现高度相关。该论文已被 ICLR 2026 接收，应被引用和讨论。

**MR2. [minor]** Ordinal regression 文献中是否遗漏了更强的 neural ordinal methods？论文仅用 CORAL 和 CLOC 作为 ordinal baselines（§5.1），但 ordinal classification 文献丰富。Kasa et al. (2024)（已引用）的 survey 列出了多种方法，但论文未解释为何仅选择了 CORAL 和 CLOC，也未讨论 proportional odds model 等经典方法在此任务上的表现。Appendix B.20 提供了 ordinal MLP 结果，但主文中缺乏讨论。

**MR3. [minor]** PAN 2026 shared task（已引用 Bevendorff et al., 2026）和 M4-SemEval（已引用 Wang et al., 2024）的讨论过于简略。论文仅在 Related Work 中列出了这些 shared tasks，但未讨论它们的评估协议或发现与本文的关系——特别是 PAN 2026 引入的 obfuscation scenarios 是否与 recursive depth estimation 问题有交叉。

---

## EMNLP 2026 适合度评估

**Main Conference vs. Findings：** 论文的核心贡献是 (1) 任务形式化和 (2) 系统经验研究。方法上无算法创新，规模受限于 ≤1.5B，且未能超越已有方法。这种 "benchmark paper + empirical characterization" 的贡献 profile 更符合 Findings 的定位（soundness + reproducibility 为主要标准）。要达到 Conference 水平，至少需要在方法或理论上有实质性推进，或在更大规模上展示 convincing results。

**Long vs. Short Paper：** 内容量（180K benchmark、3×3 grid、8 个 generalization 维度、29 个附录实验）支撑 Long Paper format。如果精简为 Short Paper，需要大幅削减实验覆盖面，反而削弱论文的主要优势（系统性）。

**受众范围：** 对 model collapse、data provenance、AI text detection 社区有参考价值，但方法论影响面有限。预估引用: 中等（benchmark 数据集可能被后续工作使用）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-20T08:42:51.699103+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "recursive_gen_depth_est",
  "text": "# 交叉审稿 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，请标注：\n- **[AGREE]** 同意并简要说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 — Findings\n\n## Must-Fix 问题\n\n**N1** [critical] **Binoculars 特征平局严重削弱方法论贡献**\n- 19-feature RF 78.4% vs Binoculars 11-feat RF 78.1%，p>0.05 无显著差异。Merged 30-feature 82.6% 说明信息互补而非本文特征优于已有特征。论文声称\"discriminative signal resides in feature design\"恰好被 Binoculars 平局所反驳——信号不在*这些*特征，而在*任何*能捕获分布偏移的特征。\n\n**N2** [critical] **Self-reference confound 使 Pythia 结果不可比，膨胀 headline 数字**\n- Pythia-1.4B 同时是 generator 和 reference model。Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 换用 GPT-2 XL 作 reference 时 accuracy 降至 67.3%（−11pp）。1/3 的 in-distribution 结果存在系统性偏差。cross-model transfer 中 Pythia holdout 行 62.4% 低于 OLMo 69.2% 反映了 confound 的传递。\n\n**N3** [critical] **d0 膨胀 headline 数字，d1-d3 实际性能远低于报告值**\n- d0 recall >97%（本质是 binary human-vs-machine）。Cross-model d1-d3 仅 55.4%（报告 66.4%），cross-strategy d1-d3 仅 45.9%（报告 59.1%）。Abstract 报告时未突出 d1-d3 的大幅下降。\n\n**N4** [critical] **Cross-strategy 和 cross-scale 失败动摇方法的泛化 claim**\n- Cross-strategy d1-d3 仅 45.9%（接近 chance 33%）。14B mean 50.8%、EDD₀.₇₀=0。z-score normalization 只修复 logistic regression 不修复 RF。方法在实际部署规模上完全失效。\n\n## Should-Fix 问题\n\n**W1** 多重共线性（VIF>10 for 14-16/19）与 Gini/SHAP 可解释性 claim 矛盾\n**W2** LoRA 微调超参（r=16, α=32, lr=2e-4）无 ablation\n**W3** BOS-seeded generation vs prompted generation（−13.8pp）限制生态效度\n**W4** 单域 cross-domain（仅 arXiv），C4 FPR 34%/FineWeb 17% 说明 web 文本泛化差\n**W5** 多重比较未校正（Bonferroni/FDR）\n**W6** EDD 阈值 T=0.70 从 binary logistic regression 标准迁移到 ordinal pairwise AUC 缺乏理论依据\n\n## Minor\n- M1: 2 个 orphan bib entries\n- M2: Binary RF 500 trees vs 4-class RF 200 trees 未解释\n- M3: §4.3 monotonicity claim 与 14B non-monotonic 发现有 tension\n- M4: Figure 1 heatmap 共线性下 Gini importance 不稳定\n- M5: Appendix B.28 two-stage pipeline 应提到正文\n\n## Questions\n- Q1: 非 Transformer reference model（如 Mamba/RWKV）的表现？\n- Q2: Perplexity tail features 是 depth-specific 还是 quality proxy？\n- Q3: z-score 修复 LR 不修复 RF 的原因？\n- Q4: DCOL iteration 的 convergence 条件？\n- Q5: 14B 实验能否分离 5 个 confounders？\n\n## Missing References\n1. Min-K%++ (Zhang et al., 2024)\n2. 近年 ordinal classification in NLP 综述\n3. RAID benchmark 为何不采用\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "recursive_gen_depth_est",
    "text": "# 交叉审稿 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，请标注：\n- **[AGREE]** 同意并简要说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 — Findings\n\n## Must-Fix 问题\n\n**N1** [critical] **Binoculars 特征平局严重削弱方法论贡献**\n- 19-feature RF 78.4% vs Binoculars 11-feat RF 78.1%，p>0.05 无显著差异。Merged 30-feature 82.6% 说明信息互补而非本文特征优于已有特征。论文声称\"discriminative signal resides in feature design\"恰好被 Binoculars 平局所反驳——信号不在*这些*特征，而在*任何*能捕获分布偏移的特征。\n\n**N2** [critical] **Self-reference confound 使 Pythia 结果不可比，膨胀 headline 数字**\n- Pythia-1.4B 同时是 generator 和 reference model。Table 2 显示 Pythia 比 OLMo/GPT-2 XL 高 4-11pp。Appendix B.13 换用 GPT-2 XL 作 reference 时 accuracy 降至 67.3%（−11pp）。1/3 的 in-distribution 结果存在系统性偏差。cross-model transfer 中 Pythia holdout 行 62.4% 低于 OLMo 69.2% 反映了 confound 的传递。\n\n**N3** [critical] **d0 膨胀 headline 数字，d1-d3 实际性能远低于报告值**\n- d0 recall >97%（本质是 binary human-vs-machine）。Cross-model d1-d3 仅 55.4%（报告 66.4%），cross-strategy d1-d3 仅 45.9%（报告 59.1%）。Abstract 报告时未突出 d1-d3 的大幅下降。\n\n**N4** [critical] **Cross-strategy 和 cross-scale 失败动摇方法的泛化 claim**\n- Cross-strategy d1-d3 仅 45.9%（接近 chance 33%）。14B mean 50.8%、EDD₀.₇₀=0。z-score normalization 只修复 logistic regression 不修复 RF。方法在实际部署规模上完全失效。\n\n## Should-Fix 问题\n\n**W1** 多重共线性（VIF>10 for 14-16/19）与 Gini/SHAP 可解释性 claim 矛盾\n**W2** LoRA 微调超参（r=16, α=32, lr=2e-4）无 ablation\n**W3** BOS-seeded generation vs prompted generation（−13.8pp）限制生态效度\n**W4** 单域 cross-domain（仅 arXiv），C4 FPR 34%/FineWeb 17% 说明 web 文本泛化差\n**W5** 多重比较未校正（Bonferroni/FDR）\n**W6** EDD 阈值 T=0.70 从 binary logistic regression 标准迁移到 ordinal pairwise AUC 缺乏理论依据\n\n## Minor\n- M1: 2 个 orphan bib entries\n- M2: Binary RF 500 trees vs 4-class RF 200 trees 未解释\n- M3: §4.3 monotonicity claim 与 14B non-monotonic 发现有 tension\n- M4: Figure 1 heatmap 共线性下 Gini importance 不稳定\n- M5: Appendix B.28 two-stage pipeline 应提到正文\n\n## Questions\n- Q1: 非 Transformer reference model（如 Mamba/RWKV）的表现？\n- Q2: Perplexity tail features 是 depth-specific 还是 quality proxy？\n- Q3: z-score 修复 LR 不修复 RF 的原因？\n- Q4: DCOL iteration 的 convergence 条件？\n- Q5: 14B 实验能否分离 5 个 confounders？\n\n## Missing References\n1. Min-K%++ (Zhang et al., 2024)\n2. 近年 ordinal classification in NLP 综述\n3. RAID benchmark 为何不采用\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-20T08:43:14.289564+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22590
}
```

</details>

---
