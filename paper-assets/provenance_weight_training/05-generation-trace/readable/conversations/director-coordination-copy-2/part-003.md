# Director coordination — Part 3 of 5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/5a/5a5f768420cdca035482.json)

## Round 56

### Tool call

_source line 752 · 2026-05-21T11:39:41.372331+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n- id: \"R1-W1\"\n  summary: \"效果大小不足以支撑方法论贡献（Δ=−0.020 PPL / 0.11%，下游为零）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 在 N1 中同意（incremental contribution）。交叉回应 R2 [AGREE] R1-W1。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"B=4 下 dual-constraint 框架实质退化（α_eff 仅 5 离散值，α_eff-binding 占比极低）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 critical。R2 [AGREE] 核心论点但质疑 R1 的 ~0.2% 数字（论文报告 38.2%）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Epoch-matched 比较引入 LR schedule confound（2533/6103 步 cosine schedule 不同阶段）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 标 major。交叉回应中 R1 将此升级为 critical（epoch confound 是论文最强贡献，其核心实验有 confound）；R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"新颖性不足以支撑 main conference（三个贡献均偏 incremental）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标 critical。R1 [AGREE]，是其 Excitement 2/5 的核心原因。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"实验规模严重不足（0.6B, B=4, 132M tokens），限制泛化性\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标 critical。R1 [AGREE]（强烈同意），指出 1.7B OOD gains 消失、Llama cross-model 省略 PPL 是 negative signal。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"N=3 统计功效不足（df=2 下 p=0.025 可靠性有限）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Self-contamination（generator=trainee）生态效度受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major，R2 [AGREE]（W2 同样指出）。§8 有声明但不免除对 claim 可信度的影响。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Grid search baseline 公平性（完整 9 点 grid 仅 seed 42）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major。R2 [PARTIALLY AGREE]——比较设计合理但问题在 effect size。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W7\"\n  summary: \"ρ=0.2 失败 + 1.7B 效果减弱限制实用范围\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major，R2 [AGREE]。方法仅在高污染+小模型+高 AUC detector 交集下有效。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W8\"\n  summary: \"Wang et al. (2026) 理论假设不匹配（已知 α vs 估计 α_eff）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major。R2 [PARTIALLY AGREE]——loose motivation 在 empirical 论文中可接受。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Abstract/Introduction 中 overclaim（将单一设置的发现推广为普遍结论）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标 major，R1 [AGREE]。'consistent improvements' 对 0.11% PPL 是 overclaim。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Related Work 遗漏 Mindermann et al. (2022) Prioritized Training\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"术语不统一（sharpening exponent vs exponent vs b）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 标 minor，R1 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9\"\n  summary: \"Minimum intervention 缺乏与其他 b 选择策略的消融对比\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 minor，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W10\"\n  summary: \"§3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 minor，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W11\"\n  summary: \"Figure 1 shaded region 边界与文字描述不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1 标 minor，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V-W1\"\n  summary: \"前 6 页无任何 figure/table 视觉锚点，审稿人体验差\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [\"visual\"]\n      note: \"视觉审查 Agent 发现。建议在第 1-2 页加入概念图或核心结果摘要图。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V-W2\"\n  summary: \"Table 1/2 + Figure 1 全堆第 7 页，视觉节奏不均\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [\"visual\"]\n      note: \"视觉审查 Agent 发现。建议将部分 display item 前移至第 5-6 页。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V-W3\"\n  summary: \"正文仅 4 个 display item，对实证论文偏少（Appendix 有 13 个）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [\"visual\"]\n      note: \"视觉审查 Agent 发现。Figure 2 (constraint regime) 和 Figure 4 (data retention curve) 可考虑提至正文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n- id: \"R1-W1\"\n  summary: \"效果大小不足以支撑方法论贡献（Δ=−0.020 PPL / 0.11%，下游为零）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 在 N1 中同意（incremental contribution）。交叉回应 R2 [AGREE] R1-W1。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"B=4 下 dual-constraint 框架实质退化（α_eff 仅 5 离散值，α_eff-binding 占比极低）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 critical。R2 [AGREE] 核心论点但质疑 R1 的 ~0.2% 数字（论文报告 38.2%）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Epoch-matched 比较引入 LR schedule confound（2533/6103 步 cosine schedule 不同阶段）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 标 major。交叉回应中 R1 将此升级为 critical（epoch confound 是论文最强贡献，其核心实验有 confound）；R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"新颖性不足以支撑 main conference（三个贡献均偏 incremental）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标 critical。R1 [AGREE]，是其 Excitement 2/5 的核心原因。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"实验规模严重不足（0.6B, B=4, 132M tokens），限制泛化性\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标 critical。R1 [AGREE]（强烈同意），指出 1.7B OOD gains 消失、Llama cross-model 省略 PPL 是 negative signal。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"N=3 统计功效不足（df=2 下 p=0.025 可靠性有限）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Self-contamination（generator=trainee）生态效度受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major，R2 [AGREE]（W2 同样指出）。§8 有声明但不免除对 claim 可信度的影响。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Grid search baseline 公平性（完整 9 点 grid 仅 seed 42）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major。R2 [PARTIALLY AGREE]——比较设计合理但问题在 effect size。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W7\"\n  summary: \"ρ=0.2 失败 + 1.7B 效果减弱限制实用范围\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major，R2 [AGREE]。方法仅在高污染+小模型+高 AUC detector 交集下有效。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W8\"\n  summary: \"Wang et al. (2026) 理论假设不匹配（已知 α vs 估计 α_eff）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 major。R2 [PARTIALLY AGREE]——loose motivation 在 empirical 论文中可接受。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Abstract/Introduction 中 overclaim（将单一设置的发现推广为普遍结论）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标 major，R1 [AGREE]。'consistent improvements' 对 0.11% PPL 是 overclaim。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Related Work 遗漏 Mindermann et al. (2022) Prioritized Training\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"术语不统一（sharpening exponent vs exponent vs b）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 标 minor，R1 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W9\"\n  summary: \"Minimum intervention 缺乏与其他 b 选择策略的消融对比\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 minor，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W10\"\n  summary: \"§3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 标 minor，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W11\"\n  summary: \"Figure 1 shaded region 边界与文字描述不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"R1 标 minor，R2 [AGREE]。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V-W1\"\n  summary: \"前 6 页无任何 figure/table 视觉锚点，审稿人体验差\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [\"visual\"]\n      note: \"视觉审查 Agent 发现。建议在第 1-2 页加入概念图或核心结果摘要图。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V-W2\"\n  summary: \"Table 1/2 + Figure 1 全堆第 7 页，视觉节奏不均\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [\"visual\"]\n      note: \"视觉审查 Agent 发现。建议将部分 display item 前移至第 5-6 页。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"V-W3\"\n  summary: \"正文仅 4 个 display item，对实证论文偏少（Appendix 有 13 个）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [\"visual\"]\n      note: \"视觉审查 Agent 发现。Figure 2 (constraint regime) 和 Figure 4 (data retention curve) 可考虑提至正文。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-21T11:39:41.424043+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 6692}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-21T11:41:38.940126+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "2.5-3.0 (Borderline Findings to Findings)",
  "report": "# 审稿报告：Round 1\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight 范式在含合成数据污染的 continued LM pretraining 中的有效性。三个贡献：(1) 识别 epoch confound——D&R 的 PPL 优势 96% 归因于多 epoch 曝光，epoch-matched 后优势从 0.384 缩至 0.017；(2) 提出 dual-constraint 自适应 b* 框架（α_eff quality floor + ESS stability ceiling），在 Qwen3-0.6B / 132M tokens / 40% self-contamination 下取得 Δ=−0.020 PPL（~0.11%）改进，但下游任务无可测量变化；(3) 分析 detector 的 calibration + discrimination 要求。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 分析有实质纠偏价值。** [R1, R2 共识] Table 1 的 epoch-matched 实验严谨地将 D&R 的 0.384 PPL gap 分解为 epoch 效应（96%）和 filtering 效应（4%），揭示了 prior work (Drayson et al. 2025) 中被忽视的混淆变量。这对社区理解 D&R 的实际机制有意义。\n\n**S2. 框架形式化清晰。** [R1, R2 共识] Dual-constraint 数学表述简洁（§3.2），Proposition 1–2 证明正确（Appendix A），Algorithm 1 可直接复现。三种 regime（clean / α_eff-binding / ESS-binding）划分直观。\n\n**S3. 消融实验覆盖面广。** [R1, R2 共识] Grid search 全空间、threshold 敏感性、contamination level (ρ=0.2/0.4/0.6)、scale (0.6B/1.7B)、constraint regime 分解、detector 家族（3种）均有系统消融。Appendix 13 个 display item 支持可复现性。\n\n**S4. Detector 对比分析有实用价值。** [R1, R2 共识] Table 10 展示 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功、GPT-2 (AUC=0.91, ECE=0.131) 和 N-gram (AUC=0.73, ECE=0.069) 失败，isolate calibration 和 discrimination 的独立作用。\n\n**S5. 诚实的 Limitations。** [R1, R2 共识] §8 覆盖 self-contamination、scale、ρ range、detector coverage、evaluation、effect size 六个方面，坦诚承认核心局限。\n\n**S6. 格式完全合规，引用均真实。** [R2 确认] ACL 两栏 ✅ | 匿名 ✅ | 8 页限制 ✅ | Limitations ✅ | Checklist ✅ | 46 条引用无伪造。\n\n---\n\n## Weaknesses\n\n### Critical（两位 Reviewer 共识）\n\n**W1. 效果大小不足以支撑方法论贡献。** [R1-W1, R2-N1 共识]\n- Adaptive b* 的 PPL 改进 Δ=−0.020（0.11%），接近 noise margin（std ±0.006–0.007）\n- 下游任务 |Δ|≤0.01（§H：\"no meaningful downstream impact\"）\n- ρ=0.6 改进更大（Δ=−0.032, p=0.004）但仍为 0.18%\n- 论文在 analysis paper 和 method paper 之间定位模糊；作为 method paper，evidence 不足\n\n**W2. B=4 下 dual-constraint 框架实质退化。** [R1-W2, R2 AGREE]\n- α_eff 仅有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}\n- R1 认为 α_eff-binding 实际占比极低，方法退化为\"ESS-only + clean batch 不干预\"\n- R2 注意论文 §3.3 报告 38.2% α_eff-binding，与 R1 的 ~0.2% 存在数量级差异，需作者澄清\n- 无论具体数字，B=4 下离散化削弱了框架的理论优雅性，需 B≥16 验证\n\n**W3. Epoch-matched 比较引入 LR schedule confound。** [R1-W3 critical, R2-W1 major → 交叉后 R1 升级、R2 AGREE]\n- D&R epoch-matched 在 2,533/6,103 步时 cosine LR 仍处中段（~64% 峰值），非训练终态\n- 论文以\"if anything, favors D&R\"论证，但 warmer LR 影响方向不确定\n- Epoch confound 是论文最强贡献，其核心实验有 confound 直接动摇 foundation\n- 需补充独立设计 2,533 步 cosine schedule 的对照实验\n\n**W4. 新颖性不足以支撑 main conference。** [R2-N1, R1 AGREE]\n- Epoch confound 是 ablation-level 发现，缺乏机制解释（为什么多 epoch 能替代 reweighting？）\n- Adaptive b* 基于成熟统计工具（ESS, Kish 1965; calibration, Guo 2017）的 straightforward 组合\n- Detector requirements（需要 calibration + discrimination）接近 expected\n- 三个贡献叠加仍偏 incremental\n\n**W5. 实验规模严重不足。** [R2-N2, R1 AGREE]\n- 主要实验：Qwen3-0.6B, batch size 4, 132M tokens\n- 1.7B 实验 OOD gains 消失（Wiki Δ=+0.013 方向不一致）\n- Llama-3.2-3B cross-model transfer 结果 mixed/negative，且省略 PPL 比较\n- τ=0.7 是否 scale-invariant 无证据\n- 标题暗示一般性结论但 evidence 仅来自 0.6B\n\n### Major\n\n**W6. N=3 统计功效不足。** [R1-W4, R2 AGREE]\n- df=2 下 p=0.025 可靠性有限\n- Δ=−0.020 的微小效应需更多 seeds 或 bootstrap CI\n\n**W7. Self-contamination 生态效度受限。** [R1-W5, R2-W2 共识]\n- Generator = trainee 使 AUC=0.94 人为偏高\n- Appendix N 的 cross-model 实验（单 seed、无 PPL）不足以证明泛化\n- §8 有声明但不免除对 claim 可信度的影响\n\n**W8. ρ=0.2 失败 + 1.7B 效果减弱限制实用范围。** [R1-W7, R2 AGREE]\n- 方法仅在高污染率 (≥0.4) + 小模型 (≤0.6B 有效) + 高 AUC calibrated detector 交集下有效\n- 实际 web 污染场景可能不在此交集内\n\n**W9. Abstract/Introduction overclaim。** [R2-W3, R1 AGREE]\n- \"consistent improvements\" 描述 0.11% PPL 过于乐观\n- §7 \"zero-tuning baseline that improves\" 技术正确但 framing misleading\n- 将单一实验设置的发现推广为 D&R 的普遍问题，缺范围限定\n\n**W10. Grid search baseline 公平性。** [R1-W6, R2 PARTIALLY AGREE]\n- 完整 9 点 grid 仅在 seed 42 做，b=0.3 是 seed 42 特定的\n- R2 认为比较设计合理但 effect size 才是核心问题\n\n**W11. Wang et al. (2026) 理论假设不匹配。** [R1-W8, R2 PARTIALLY AGREE]\n- 该理论假设已知 α，本文用 α_eff（r=0.70, bias≈−0.03）近似\n- R2 认为 loose motivation 在 empirical 论文中可接受；R1 认为不能直接迁移理论保证\n\n### Minor\n\n**W12.** Related Work 遗漏 Mindermann et al. (2022) \"Prioritized Training\"。[R2-W4, R1 AGREE]\n**W13.** 术语不统一（\"sharpening exponent\" vs \"exponent\" vs \"b\"）。[R2-W5, R1 AGREE]\n**W14.** \"Minimum intervention\" 缺乏与其他 b 选择策略的消融对比。[R1-W9, R2 AGREE]\n**W15.** §3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致。[R1-W10, R2 AGREE]\n**W16.** Figure 1 shaded region 边界与文字描述不一致。[R1-W11, R2 AGREE]\n**W17.** vehtari2024psis 年份需确认（OpenAlex 记录 2015 vs bib 2024）。[R2 引用审计]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识 [AGREE]：\n\n1. **Adaptive b* 的方法论贡献因 tiny effect size (Δ=−0.020) 和 B=4 退化而不成立**——论文的主要价值不在方法，而在分析\n2. **实验规模过小（0.6B, 132M tokens, B=4）严重限制泛化性**——标题暗示一般性结论但 evidence base 狭窄\n3. **LR schedule confound 是 epoch confound 分析的关键漏洞**——论文最强贡献的核心实验有未解决的 confound\n4. **论文应重新定位为分析论文**——epoch confound observation 有独立价值，但方法贡献薄弱\n\n---\n\n## Reviewer Divergence\n\n**评分差异 (R1: 2.5 vs R2: 3.0)：**\n- R2 认为 epoch confound 发现有独立的 analytical 价值，足以支撑 Findings 接收\n- R1 认为 LR confound 未解决（W3 为 critical）、B=4 退化是 soundness 问题，应降低 Soundness 评分\n- R2 条件性维持 3.0：如果 rebuttal 中 LR confound 未被解决，会考虑下调至 2.5\n\n**W2 具体数字分歧：**\n- R1 声称 α_eff-binding 实际占比 ~0.2%\n- R2 指出论文 §3.3 报告 38.2%，两者存在数量级差异\n- 核心论点（B=4 下框架退化）双方一致，但需作者澄清具体数字\n\n---\n\n## Questions\n\nQ1. [R1, R2] B≥16 下 α_eff-binding regime 占比是多少？dual-constraint 两个约束是否都有实质作用？\nQ2. [R1, R2] 为 D&R epoch-matched 独立设计 2,533 步 cosine schedule 后，Δ=0.017 是否改变？\nQ3. [R2] Epoch confound 的机制是什么？多 epoch 曝光为什么能替代 reweighting？\nQ4. [R1] Seed 123/456 各自的 grid-best b 是多少？\nQ5. [R1] Detector AUC 与方法有效性的定量关系？\nQ6. [R2] Llama cross-model transfer 失败是否说明需要 per-model tuning，从而否定 \"zero-tuning\" 定位？\n\n---\n\n## Missing References\n\n- **Mindermann et al. (2022)** \"Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt\" — instance-level online data selection，与 provenance-based reweighting 形成有意义对比。[R2 提出, R1 AGREE]\n- **vehtari2024psis** 年份需确认：OpenAlex 记录 2015，bib 写 2024（可能是 JMLR 正式发表年份 vs 原始 arXiv 年份）。[R2 引用审计]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成\n\n**Findings (3 warning, 4 info):**\n\n| 严重度 | 位置 | 问题 |\n|--------|------|------|\n| ⚠️ warning | p1-6 | 前 6 页无任何 figure/table 视觉锚点，审稿人需读完 6 页纯文本才能看到第一个实验结果。建议在第 1-2 页加入概念图或核心结果摘要图 |\n| ⚠️ warning | p7 | Table 1、Table 2、Figure 1 三个 display item 全部堆叠在同一页，视觉节奏严重不均。建议将部分 display item 前移至第 5-6 页 |\n| ⚠️ warning | p1-8 | 8 页正文仅 4 个 display item（含 Algorithm 1），对实证论文偏少。Appendix 有 13 个 display item，部分关键结果（Figure 2 constraint regime、Figure 4 data retention curve）可提升到正文 |\n| ℹ️ info | p7 | Figure 1 图内文字偏小（约正文 60-65%），可考虑改为 figure* 全宽 |\n| ℹ️ info | p5 | Algorithm 1 是前 6 页唯一非文本元素，视觉断节作用有限 |\n| ℹ️ info | p8 | Discussion + Conclusion + Limitations 起始段同页，密度高但排版合理 |\n| ℹ️ info | p13-16 | Appendix 图表密度充足，格式规范 |\n\n---\n\n## Overall Assessment\n\n**综合评分: 2.5–3.0 (Borderline Findings to Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 2/5 | 2.5/5 | 2/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 2.5 | 3.0 | **2.5–3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合判断：** 论文的核心价值在 epoch confound observation——揭示 D&R 的 96% PPL 优势来自多 epoch 曝光。这一发现有纠偏意义，但受 LR schedule confound 削弱（W3）。Adaptive b* 方法的效果过小（0.11% PPL, 下游为零），在 B=4 下框架退化，实验规模（0.6B）过小，三个贡献均偏 incremental。\n\n**定位建议：** 重新定位为分析论文（以 epoch confound 为核心贡献），或补充 (a) 独立 LR schedule 的 epoch-matched 对照，(b) ≥3B 模型的规模验证，(c) B≥16 下 dual-constraint 的有效性验证。\n\n**当前水平：** Borderline Findings — 如果 LR confound 在 rebuttal 中被充分解决，可支撑 Findings；否则 Borderline Findings。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"consistent improvements\" 需加范围限定（仅在 ρ≥0.4, ≤0.6B, calibrated detector 下验证）\n- 标题 \"When Does D&R Work?\" 暗示一般性结论，但 evidence 仅覆盖一个模型家族、self-contamination\n\n### §3 Method\n- Dual-constraint 形式化清晰，但 B=4 下离散化问题需在正文讨论（而非仅在 Appendix 提及 r≈0.70）\n- \"minimum intervention\" 设计选择缺乏与 \"maximum intervention\" (ESS-only) 之外的其他策略对比\n- Wang et al. (2026) 理论引用应明确注明假设差异\n\n### §4 Experiments\n- Self-contamination 设计的局限应在实验部分而非仅在 Limitations 中讨论\n- TF-IDF+LR detector 的选择理由（为什么不用更强的 neural detector）应更充分论证\n\n### §5 Results\n- Table 1 epoch-matched 比较需补充独立 LR schedule 对照\n- Downstream 结果（无影响）应在正文（非仅 Appendix）明确讨论，避免读者形成过度乐观印象\n- ρ=0.6 三 seed 结果更有说服力（p=0.004），建议强调此设置而非 ρ=0.4\n\n### §6 Discussion\n- \"Practical guidance\" 节需加更明确的使用条件限定\n- Epoch confound 的机制解释缺失——为什么多 epoch 曝光能替代 reweighting？这是一个值得展开的分析方向\n\n### §8 Limitations\n- 充分但偏保守，可更直接地讨论 B=4 离散化和下游无效果\n\n### 排版\n- 正文 display item 过少（4 个 / 8 页），前 6 页无图表，审稿人体验差\n- 建议将 Appendix 中的 Figure 2 (constraint regime) 和 Figure 4 (D&R dual curve) 提至正文"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "2.5-3.0 (Borderline Findings to Findings)",
    "report": "# 审稿报告：Round 1\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight 范式在含合成数据污染的 continued LM pretraining 中的有效性。三个贡献：(1) 识别 epoch confound——D&R 的 PPL 优势 96% 归因于多 epoch 曝光，epoch-matched 后优势从 0.384 缩至 0.017；(2) 提出 dual-constraint 自适应 b* 框架（α_eff quality floor + ESS stability ceiling），在 Qwen3-0.6B / 132M tokens / 40% self-contamination 下取得 Δ=−0.020 PPL（~0.11%）改进，但下游任务无可测量变化；(3) 分析 detector 的 calibration + discrimination 要求。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 分析有实质纠偏价值。** [R1, R2 共识] Table 1 的 epoch-matched 实验严谨地将 D&R 的 0.384 PPL gap 分解为 epoch 效应（96%）和 filtering 效应（4%），揭示了 prior work (Drayson et al. 2025) 中被忽视的混淆变量。这对社区理解 D&R 的实际机制有意义。\n\n**S2. 框架形式化清晰。** [R1, R2 共识] Dual-constraint 数学表述简洁（§3.2），Proposition 1–2 证明正确（Appendix A），Algorithm 1 可直接复现。三种 regime（clean / α_eff-binding / ESS-binding）划分直观。\n\n**S3. 消融实验覆盖面广。** [R1, R2 共识] Grid search 全空间、threshold 敏感性、contamination level (ρ=0.2/0.4/0.6)、scale (0.6B/1.7B)、constraint regime 分解、detector 家族（3种）均有系统消融。Appendix 13 个 display item 支持可复现性。\n\n**S4. Detector 对比分析有实用价值。** [R1, R2 共识] Table 10 展示 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功、GPT-2 (AUC=0.91, ECE=0.131) 和 N-gram (AUC=0.73, ECE=0.069) 失败，isolate calibration 和 discrimination 的独立作用。\n\n**S5. 诚实的 Limitations。** [R1, R2 共识] §8 覆盖 self-contamination、scale、ρ range、detector coverage、evaluation、effect size 六个方面，坦诚承认核心局限。\n\n**S6. 格式完全合规，引用均真实。** [R2 确认] ACL 两栏 ✅ | 匿名 ✅ | 8 页限制 ✅ | Limitations ✅ | Checklist ✅ | 46 条引用无伪造。\n\n---\n\n## Weaknesses\n\n### Critical（两位 Reviewer 共识）\n\n**W1. 效果大小不足以支撑方法论贡献。** [R1-W1, R2-N1 共识]\n- Adaptive b* 的 PPL 改进 Δ=−0.020（0.11%），接近 noise margin（std ±0.006–0.007）\n- 下游任务 |Δ|≤0.01（§H：\"no meaningful downstream impact\"）\n- ρ=0.6 改进更大（Δ=−0.032, p=0.004）但仍为 0.18%\n- 论文在 analysis paper 和 method paper 之间定位模糊；作为 method paper，evidence 不足\n\n**W2. B=4 下 dual-constraint 框架实质退化。** [R1-W2, R2 AGREE]\n- α_eff 仅有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}\n- R1 认为 α_eff-binding 实际占比极低，方法退化为\"ESS-only + clean batch 不干预\"\n- R2 注意论文 §3.3 报告 38.2% α_eff-binding，与 R1 的 ~0.2% 存在数量级差异，需作者澄清\n- 无论具体数字，B=4 下离散化削弱了框架的理论优雅性，需 B≥16 验证\n\n**W3. Epoch-matched 比较引入 LR schedule confound。** [R1-W3 critical, R2-W1 major → 交叉后 R1 升级、R2 AGREE]\n- D&R epoch-matched 在 2,533/6,103 步时 cosine LR 仍处中段（~64% 峰值），非训练终态\n- 论文以\"if anything, favors D&R\"论证，但 warmer LR 影响方向不确定\n- Epoch confound 是论文最强贡献，其核心实验有 confound 直接动摇 foundation\n- 需补充独立设计 2,533 步 cosine schedule 的对照实验\n\n**W4. 新颖性不足以支撑 main conference。** [R2-N1, R1 AGREE]\n- Epoch confound 是 ablation-level 发现，缺乏机制解释（为什么多 epoch 能替代 reweighting？）\n- Adaptive b* 基于成熟统计工具（ESS, Kish 1965; calibration, Guo 2017）的 straightforward 组合\n- Detector requirements（需要 calibration + discrimination）接近 expected\n- 三个贡献叠加仍偏 incremental\n\n**W5. 实验规模严重不足。** [R2-N2, R1 AGREE]\n- 主要实验：Qwen3-0.6B, batch size 4, 132M tokens\n- 1.7B 实验 OOD gains 消失（Wiki Δ=+0.013 方向不一致）\n- Llama-3.2-3B cross-model transfer 结果 mixed/negative，且省略 PPL 比较\n- τ=0.7 是否 scale-invariant 无证据\n- 标题暗示一般性结论但 evidence 仅来自 0.6B\n\n### Major\n\n**W6. N=3 统计功效不足。** [R1-W4, R2 AGREE]\n- df=2 下 p=0.025 可靠性有限\n- Δ=−0.020 的微小效应需更多 seeds 或 bootstrap CI\n\n**W7. Self-contamination 生态效度受限。** [R1-W5, R2-W2 共识]\n- Generator = trainee 使 AUC=0.94 人为偏高\n- Appendix N 的 cross-model 实验（单 seed、无 PPL）不足以证明泛化\n- §8 有声明但不免除对 claim 可信度的影响\n\n**W8. ρ=0.2 失败 + 1.7B 效果减弱限制实用范围。** [R1-W7, R2 AGREE]\n- 方法仅在高污染率 (≥0.4) + 小模型 (≤0.6B 有效) + 高 AUC calibrated detector 交集下有效\n- 实际 web 污染场景可能不在此交集内\n\n**W9. Abstract/Introduction overclaim。** [R2-W3, R1 AGREE]\n- \"consistent improvements\" 描述 0.11% PPL 过于乐观\n- §7 \"zero-tuning baseline that improves\" 技术正确但 framing misleading\n- 将单一实验设置的发现推广为 D&R 的普遍问题，缺范围限定\n\n**W10. Grid search baseline 公平性。** [R1-W6, R2 PARTIALLY AGREE]\n- 完整 9 点 grid 仅在 seed 42 做，b=0.3 是 seed 42 特定的\n- R2 认为比较设计合理但 effect size 才是核心问题\n\n**W11. Wang et al. (2026) 理论假设不匹配。** [R1-W8, R2 PARTIALLY AGREE]\n- 该理论假设已知 α，本文用 α_eff（r=0.70, bias≈−0.03）近似\n- R2 认为 loose motivation 在 empirical 论文中可接受；R1 认为不能直接迁移理论保证\n\n### Minor\n\n**W12.** Related Work 遗漏 Mindermann et al. (2022) \"Prioritized Training\"。[R2-W4, R1 AGREE]\n**W13.** 术语不统一（\"sharpening exponent\" vs \"exponent\" vs \"b\"）。[R2-W5, R1 AGREE]\n**W14.** \"Minimum intervention\" 缺乏与其他 b 选择策略的消融对比。[R1-W9, R2 AGREE]\n**W15.** §3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致。[R1-W10, R2 AGREE]\n**W16.** Figure 1 shaded region 边界与文字描述不一致。[R1-W11, R2 AGREE]\n**W17.** vehtari2024psis 年份需确认（OpenAlex 记录 2015 vs bib 2024）。[R2 引用审计]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识 [AGREE]：\n\n1. **Adaptive b* 的方法论贡献因 tiny effect size (Δ=−0.020) 和 B=4 退化而不成立**——论文的主要价值不在方法，而在分析\n2. **实验规模过小（0.6B, 132M tokens, B=4）严重限制泛化性**——标题暗示一般性结论但 evidence base 狭窄\n3. **LR schedule confound 是 epoch confound 分析的关键漏洞**——论文最强贡献的核心实验有未解决的 confound\n4. **论文应重新定位为分析论文**——epoch confound observation 有独立价值，但方法贡献薄弱\n\n---\n\n## Reviewer Divergence\n\n**评分差异 (R1: 2.5 vs R2: 3.0)：**\n- R2 认为 epoch confound 发现有独立的 analytical 价值，足以支撑 Findings 接收\n- R1 认为 LR confound 未解决（W3 为 critical）、B=4 退化是 soundness 问题，应降低 Soundness 评分\n- R2 条件性维持 3.0：如果 rebuttal 中 LR confound 未被解决，会考虑下调至 2.5\n\n**W2 具体数字分歧：**\n- R1 声称 α_eff-binding 实际占比 ~0.2%\n- R2 指出论文 §3.3 报告 38.2%，两者存在数量级差异\n- 核心论点（B=4 下框架退化）双方一致，但需作者澄清具体数字\n\n---\n\n## Questions\n\nQ1. [R1, R2] B≥16 下 α_eff-binding regime 占比是多少？dual-constraint 两个约束是否都有实质作用？\nQ2. [R1, R2] 为 D&R epoch-matched 独立设计 2,533 步 cosine schedule 后，Δ=0.017 是否改变？\nQ3. [R2] Epoch confound 的机制是什么？多 epoch 曝光为什么能替代 reweighting？\nQ4. [R1] Seed 123/456 各自的 grid-best b 是多少？\nQ5. [R1] Detector AUC 与方法有效性的定量关系？\nQ6. [R2] Llama cross-model transfer 失败是否说明需要 per-model tuning，从而否定 \"zero-tuning\" 定位？\n\n---\n\n## Missing References\n\n- **Mindermann et al. (2022)** \"Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt\" — instance-level online data selection，与 provenance-based reweighting 形成有意义对比。[R2 提出, R1 AGREE]\n- **vehtari2024psis** 年份需确认：OpenAlex 记录 2015，bib 写 2024（可能是 JMLR 正式发表年份 vs 原始 arXiv 年份）。[R2 引用审计]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成\n\n**Findings (3 warning, 4 info):**\n\n| 严重度 | 位置 | 问题 |\n|--------|------|------|\n| ⚠️ warning | p1-6 | 前 6 页无任何 figure/table 视觉锚点，审稿人需读完 6 页纯文本才能看到第一个实验结果。建议在第 1-2 页加入概念图或核心结果摘要图 |\n| ⚠️ warning | p7 | Table 1、Table 2、Figure 1 三个 display item 全部堆叠在同一页，视觉节奏严重不均。建议将部分 display item 前移至第 5-6 页 |\n| ⚠️ warning | p1-8 | 8 页正文仅 4 个 display item（含 Algorithm 1），对实证论文偏少。Appendix 有 13 个 display item，部分关键结果（Figure 2 constraint regime、Figure 4 data retention curve）可提升到正文 |\n| ℹ️ info | p7 | Figure 1 图内文字偏小（约正文 60-65%），可考虑改为 figure* 全宽 |\n| ℹ️ info | p5 | Algorithm 1 是前 6 页唯一非文本元素，视觉断节作用有限 |\n| ℹ️ info | p8 | Discussion + Conclusion + Limitations 起始段同页，密度高但排版合理 |\n| ℹ️ info | p13-16 | Appendix 图表密度充足，格式规范 |\n\n---\n\n## Overall Assessment\n\n**综合评分: 2.5–3.0 (Borderline Findings to Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 2/5 | 2.5/5 | 2/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 2.5 | 3.0 | **2.5–3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合判断：** 论文的核心价值在 epoch confound observation——揭示 D&R 的 96% PPL 优势来自多 epoch 曝光。这一发现有纠偏意义，但受 LR schedule confound 削弱（W3）。Adaptive b* 方法的效果过小（0.11% PPL, 下游为零），在 B=4 下框架退化，实验规模（0.6B）过小，三个贡献均偏 incremental。\n\n**定位建议：** 重新定位为分析论文（以 epoch confound 为核心贡献），或补充 (a) 独立 LR schedule 的 epoch-matched 对照，(b) ≥3B 模型的规模验证，(c) B≥16 下 dual-constraint 的有效性验证。\n\n**当前水平：** Borderline Findings — 如果 LR confound 在 rebuttal 中被充分解决，可支撑 Findings；否则 Borderline Findings。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"consistent improvements\" 需加范围限定（仅在 ρ≥0.4, ≤0.6B, calibrated detector 下验证）\n- 标题 \"When Does D&R Work?\" 暗示一般性结论，但 evidence 仅覆盖一个模型家族、self-contamination\n\n### §3 Method\n- Dual-constraint 形式化清晰，但 B=4 下离散化问题需在正文讨论（而非仅在 Appendix 提及 r≈0.70）\n- \"minimum intervention\" 设计选择缺乏与 \"maximum intervention\" (ESS-only) 之外的其他策略对比\n- Wang et al. (2026) 理论引用应明确注明假设差异\n\n### §4 Experiments\n- Self-contamination 设计的局限应在实验部分而非仅在 Limitations 中讨论\n- TF-IDF+LR detector 的选择理由（为什么不用更强的 neural detector）应更充分论证\n\n### §5 Results\n- Table 1 epoch-matched 比较需补充独立 LR schedule 对照\n- Downstream 结果（无影响）应在正文（非仅 Appendix）明确讨论，避免读者形成过度乐观印象\n- ρ=0.6 三 seed 结果更有说服力（p=0.004），建议强调此设置而非 ρ=0.4\n\n### §6 Discussion\n- \"Practical guidance\" 节需加更明确的使用条件限定\n- Epoch confound 的机制解释缺失——为什么多 epoch 曝光能替代 reweighting？这是一个值得展开的分析方向\n\n### §8 Limitations\n- 充分但偏保守，可更直接地讨论 B=4 离散化和下游无效果\n\n### 排版\n- 正文 display item 过少（4 个 / 8 页），前 6 页无图表，审稿人体验差\n- 建议将 Appendix 中的 Figure 2 (constraint regime) 和 Figure 4 (D&R dual curve) 提至正文"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-21T11:41:43.258347+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4318
}
```

</details>

---


### Assistant

_source line 756 · 2026-05-21T11:41:51.892486+00:00_

审稿报告已投递给 Research Director。

**Round 1 审稿完成总结：**

- **综合评分**：2.5–3.0（Borderline Findings to Findings）
- **R1**: 2.5 (Borderline Findings) | **R2**: 3.0 (Findings)
- **5 个 critical issues**：效果大小不足、B=4 框架退化、LR confound、新颖性偏 incremental、实验规模过小
- **6 个 major issues**：N=3 统计功效、self-contamination 局限、实用范围窄、overclaim、grid baseline 公平性、理论假设不匹配
- **6 个 minor issues**：遗漏引用、术语不统一、图表不一致等
- **视觉审查**：3 个 warning（前 6 页无图表、display item 堆叠、正文图表过少）
- **外部审稿**：未配置
- **Issue Tracker**：已同步 19 条 issue 到 `review_issues.yaml`

核心判断：论文价值在 epoch confound observation，但 adaptive method 贡献薄弱，需重新定位或补充大规模实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 757 · 2026-05-21T11:41:54.703217+00:00_

[Reviewer 2 审稿结果]:
交叉回应已完成并提交给 Review Director。

核心结论：与 R1 在绝大多数问题上达成共识（8/11 AGREE，2/11 PARTIALLY AGREE），但评分维持 3.0 vs R1 的 2.5——分歧在于 epoch confound 发现的独立价值是否足以支撑 Findings。两位 Reviewer 共同认为 adaptive b* 的方法论贡献基本不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 758 · 2026-05-21T11:42:04.886214+00:00_

审稿报告已投递至 Research Director，Issue Tracker 已同步（5 critical / 6 warning / 6 info，共 17 issues）。

**Round 1 圆桌审稿完成。**

- **综合评分**: 2.5–3.0（Borderline Findings to Findings）
- **R1**: 2.5 | **R2**: 3.0
- **核心共识**: adaptive b* 方法论贡献不成立（效果 0.11%、B=4 退化、下游为零）；论文价值在 epoch confound observation；LR confound 是最强贡献的关键漏洞；实验规模过小
- **评分分歧**: R2 认为 epoch confound 的独立分析价值足以支撑 Findings；R1 认为 LR confound 未解决则应降至 Borderline Findings
- **视觉审查**: 3 个 warning（前 6 页无图表、display item 堆叠第 7 页、正文图表过少）
- **外部审稿**: 未配置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 58

## Round 58

66 recorded events


### User

_source line 759 · 2026-05-21T14:00:44.758670+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-21T14:00:53.968324+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-21T14:00:53.969202+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-21T14:01:00.294287+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-21T14:01:00.345000+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-21T14:01:04.512036+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-21T14:01:06.387004+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (220 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T13:43:48Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 213 个实验 — ANALYZING 1, DONE 193, PREPARING 18, RUNNING 1\n**DONE 分布**: failed 36, killed 19, negative 12, success 126\n\n### GPU 占用\n- **分配**: 4 张 — westd-41312:cuda:0, westd-41312:cuda:1, westd-41312:cuda:2, westd-41312:cuda:3\n- **实际运行**: 1 张 — westd-41312:cuda:1(bs16_adaptive_tau07_seed42)\n\n### 💾 磁盘余量\n- **westd-41312**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 400G/439G 可用（已用 4%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `bs16_adaptive_tau07_seed42` | westd-41312 | cuda:1 | 613352 | `…s/provenance_weight_training/bs16_adaptive_tau07_seed42.log` |\n\n### 📌 最近完成 (top 5)\n- `grid_b0_1_seed42` [success] — 2026-05-21T13:43:44\n- `rho02_adaptive_tau08_seed42` [negative] — 2026-05-21T13:43:39\n- `batchsize16_nmin8_r2` [killed] — 2026-05-21T13:43:36\n- `ess_only_seed123` [success] — 2026-05-21T13:43:15\n- `ess_only_seed456` [success] — 2026-05-21T13:43:13\n\n### 🔴 最近失败原因 (top 3)\n- `batchsize16_nmin8_r2`: _(no failure_reason — pre-2026-04-24 entry)_\n\n<!-- AUTO-FACTS-END 
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1874
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-21T14:01:06.500016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-21T14:01:07.155526+00:00_

-rw-r--r-- 1 ubuntu ubuntu 469245 May 21 13:53 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu   1850 May 21 12:16 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-21T14:01:07.161259+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 769 · 2026-05-21T14:01:07.284864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 123
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-21T14:01:12.444547+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 771 · 2026-05-21T14:01:12.897971+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-21T14:01:13.350510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-21T14:01:13.401144+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	
32	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
33	
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\begin{abstract}
40	\input{sections/abstract}
41	\end{abstract}
42	
43	\section{Introduction}
44	\label{sec:intro}
45	\input{sections/introduction}
46	
47	\section{Related Work}
48	\label{sec:related}
49	\input{sections/related_work}
50	
51	\section{Method}
52	\label{sec:method}
53	\input{sections/method}
54	
55	\section{Experimental Setup}
56	\label{sec:experiments}
57	\input{sections/experiments}
58	
59	\section{Results}
60	\label{sec:results}
61	\input{sections/results}
62	
63	\section{Discussion}
64	\label{sec:discussion}
65	\input{sections/discussion}
66	
67	\section{Conclusion}
68	\label{sec:conclusion}
69	\input{sections/conclusion}
70	
71	\section*{Limitations}
72	\label{sec:limitations}
73	\input{sections/limitations}
74	
75	\section*{Ethics Statement}
76	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
77	
78	\input{sections/checklist}
79	
8
…[truncated 99 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-21T14:01:20.426114+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline author guidelines"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about ACL Rolling Review (ARR) for May 2026:

## Submission Deadline

There is a submission deadline every two months, with the specific May 2026 dates being part of ARR's 10-week review cycle schedule that started in May 2025.

## Author Guidelines

All submitting authors have to also sign up as reviewers (deadline: 48h after the submission deadline). Key requirements include:

- The submission must adhere to the formatting in the su
…[truncated 952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 7528
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-21T14:01:22.784792+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 call for papers and ARR submission guidelines:

## EMNLP 2026 Call for Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniq
…[truncated 2073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 10340
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-21T14:01:28.458106+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-21T14:01:28.658983+00:00_

abstract.tex
appendix.tex
checklist.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-21T14:01:29.161493+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-21T14:01:29.212325+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 117\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-21T14:01:33.587908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-21T14:01:34.089543+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled experiments (Qwen3-0.6B continued pretraining, 132M FineWeb tokens, 3 seeds), we analyze when, why, and how detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the advantage shrinks from 0.384 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of published gains reflect data repetition rather than filtering quality.
6	Second, effective reweighting requires both sufficient discrimination and good calibration from the detector; a high-AUC but poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform, while a lightweight calibrated alternative (ECE\,=\,0.048) succeeds (3 detectors, 3 seeds).
7	Third, mechanism decomposition reveals that minimum intervention outperforms unconstrained maximization: an $\alpha_{\mathrm{eff}}$ quality constraint binds in 38\% of batches at $4.9{\times}$ lower sharpening exponents than a stability-only strategy.
8	
9	From this analysis, we derive a dual-constrained adaptive $b^*$ that eliminates per-model grid search, improving over uniform at $\rho \geq 0.4$ with calibrated detectors ($\Delta{=}{-}0.020$ at $\rho{=}0.4$, $p{=}0.025$; $-$0.032 at $\rho{=}0.6$, $p{=}0.004$).
10	The method fails at $\rho{=}0.2$ and shows diminished benefit at 1.7B; with $N{=}3$, paired comparisons reach significance though sample size limits generalizability.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-21T14:01:34.089941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-21T14:01:34.491450+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters.
11	Our scope is continued pretraining with self-generated contamination; generalization to web scale, multi-source contamination, or other model families is untested (\S\ref{sec:limitations}).
12	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
13	
14	Our analysis yields four findings:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{Epoch confound.}
17	The bulk of D\&R's PPL advantage (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality; epoch-matched control
…[truncated 2630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-21T14:01:34.491933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-21T14:01:35.446501+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\
…[truncated 5897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-21T14:01:35.446947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-21T14:01:35.898686+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown, a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng2025contamination}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson2025detection}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	The indicator $r_i = \mathbf{1}[q_i \leq 0.5]$ is a proxy for true provenance: $\alpha_{\mathrm{eff}}$ tracks the detector's estimate of the real fraction, not the
…[truncated 10049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-21T14:01:35.949256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-21T14:01:36.151117+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, linear schedule with warmup (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision on a single NVIDIA RTX PRO 6000 (96\,GB).
14	All main
…[truncated 1656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-21T14:01:36.264077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-21T14:01:36.264690+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, paired $t{=}{-}6.2$, $p{=}0.025$) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
9	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
10	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
11	
12	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
13	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
14	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
15	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.020$, directionally consistent across all seeds).
16	Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curv
…[truncated 9278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-21T14:01:42.883338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-21T14:01:43.335307+00:00_

1	\paragraph{Why minimum intervention works.}
2	The $\aeff$ constraint prevents $4.9\times$ over-aggressive downweighting in 38.2\% of batches (\S\ref{sec:regime}), stable across seeds (CV\,${<}$\,2\%).
3	Per-batch adaptation is essential: fixed $b{=}1.0$ yields PPL indistinguishable from uniform.
4	At $\rho{=}0.2$ the method degrades ($+$0.046; Appendix~\ref{app:rho02}), as $\aeff$-binding rises to 60.1\% despite unreliable detector signal.
5	Generative detectors fail for complementary reasons: insufficient calibration (GPT-2) or insufficient discrimination (N-gram); see \S\ref{sec:robustness}.
6	An early single-seed OOD anomaly was traced to a resume artifact (Appendix~\ref{app:resume_artifact}); three-seed from-scratch evaluation confirms OOD gains exceed in-distribution ($|\Delta| \leq 0.029$).
7	
8	\paragraph{Practical guidance.}
9	With a calibrated discriminative detector, adaptive $\bstar$ ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$) improves over uniform at $\rho \geq 0.4$ without tuning.
10	Under LR-controlled comparison, D\&R filtering is worse than uniform ($\Delta{=}{+}0.72$); multi-epoch D\&R gains should be interpreted with this confound in mind.
11	Without a calibrated detector, uniform training is preferable (\S\ref{sec:robustness}).
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-21T14:01:43.335665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-21T14:01:44.289635+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the reported advantage); (2) detectors require both discrimination and calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$) improves over uniform at $\rho \geq 0.4$ ($p \leq 0.025$) without tuning; validated on Qwen3 ${\leq}$1.7B, where the benefit diminishes.
3	Code and data will be released upon acceptance.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-21T14:01:44.340238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-21T14:01:44.842049+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B test also showed degradation ($\Delta{=}{+}0.20$), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; while the pattern---calibrated discrimination is necessary---is consistent, this coverage cannot fully disentangle detector type from calibration quality.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-21T14:01:44.842382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-21T14:01:45.043572+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; th
…[truncated 20977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-21T14:01:45.094416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-21T14:01:45.145044+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-21T14:01:52.622189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-21T14:01:52.823305+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-21T14:01:52.823620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-21T14:01:52.874305+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{katharopoulos2018not,
5	  title={Not All Samples Are Created Equal: Deep Learning with Importance Sampling},
6	  author={Katharopoulos, Angelos and Fleuret, Fran{\c{c}}ois},
7	  booktitle={International Conference on Machine Learning},
8	  pages={2525--2534},
9	  year={2018},
10	  organization={PMLR}
11	}
12	
13	@inproceedings{ren2018learning,
14	  title={Learning to Reweight Examples for Robust Deep Learning},
15	  author={Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel},
16	  booktitle={International Conference on Machine Learning},
17	  pages={4334--4343},
18	  year={2018},
19	  organization={PMLR}
20	}
21	
22	@article{chen2024bull,
23	  title={Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves {LLM} Generalization},
24	  author={Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng and Wang, Zhongming},
25	  journal={arXiv preprint arXiv:2402.14270},
26	  year={2024}
27	}
28	
29	@inproceedings{kang2025demystifying,
30	  title={Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls},
31	  author={Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Chen, Hongliang and Zhu, Yiming and Chen, Zijian and Liu, Mohan and Liu, Jingcheng and Liu, Haoran and Han, Song},
32	  booktitle={EMNLP},
33	  year={2025}
34	}
35	
36	@article{zibakhsh2025fortifai,
37	  title={{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},
38	  author={Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koushanfar, Farinaz},
39	  journal={arXiv preprint arXiv:2509.08972},
40	  year={2025}
41	}
42	
43	@article{yi2025escaping,
44	  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
…[truncated 13575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-21T14:01:57.843040+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-21T14:01:58.746677+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-21T14:01:58.898026+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/*.tex",
  "description": "Count lines per section for page estimate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/*.tex",
    "description": "Count lines per section for page estimate"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-21T14:01:58.949546+00:00_

   10 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
  395 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
   65 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
   11 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
   32 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
   49 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
  132 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
   48 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
  121 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
  869 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-21T14:02:02.514476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
  "description": "Find config files at root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
    "description": "Find config files at root level"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-21T14:02:02.615732+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-21T14:02:05.985925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 3 -name \"*.yaml\" -path \"*/provenance*\" 2>/dev/null | head -10",
  "description": "Find yaml files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 3 -name \"*.yaml\" -path \"*/provenance*\" 2>/dev/null | head -10",
    "description": "Find yaml files in project"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-21T14:02:06.186990+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/projects/provenance_weight_training.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-21T14:02:09.506125+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/projects/provenance_weight_training.yaml 2>/dev/null | grep -A5 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/projects/provenance_weight_training.yaml 2>/dev/null | grep -A5 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-21T14:02:09.606834+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-21T14:02:13.026328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/projects/provenance_weight_training.yaml",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/projects/provenance_weight_training.yaml",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-21T14:02:13.076930+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  - cuda:2
7	  - cuda:3
8	  project_path: /root/provenance_weight_training
9	  servers:
10	  - account: root
11	    server: westd-41312
12	feishu:
13	  chat_id: oc_2b6c9bea33a70c93bf4bf04ac36b8df9
14	  operational_chat_id: oc_39371eead41d9df941b3542b7f23b377
15	  review_mode: fresh
16	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
17	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf
18	  review_round: 8
19	  review_supplementary_paths: ''
20	  submission_chat_id: oc_069d56747de0423c793156b069500cb3
21	project:
22	  created_at: '2026-05-13T17:37:05.514Z'
23	  description: Convergence-Informed Provenance Weighting for Recursive Web Contamination
24	  name: provenance_weight_training
25	  phase: research
26	  source_idea_id: idea_011
27	venue: emnlp-2026
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-21T14:02:33.606958+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-21T14:02:53.587762+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19980
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-21T14:02:53.688508+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ARR May 2026\n- **截止日期**：2026-05-25\n- **格式**：ACL 模板，正文 8 页限制（参考文献不限），double-blind\n- **匿名规则**：严格 double-blind，禁止透露作者身份\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`\n\n## 审查侧重\n\n### 1. 数学推导与理论基础\n- Proposition 1 (α_eff 单调性) 和 Proposition 2 (ESS 单调性) 的证明是否严谨\n- 双约束框架 (Eq. 4) 的三种 regime 划分是否完备且互斥\n- α_eff 作为真实 real fraction 的代理指标，Pearson r≈0.70 是否足够支撑整个方法的理论动机\n- b* 的 bisection 求解在 B=4 离散情况下的行为是否被充分讨论\n\n### 2. 实验设计与对照\n- 3 seeds (N=3) 的统计检验力是否足够支撑所有声称（尤其是 p=0.025 的结果）\n- Epoch confound 分析：epoch-matched 对照是否完全消除了混淆因素（LR schedule 是否也是混淆？）\n- Grid-b 作为 post-hoc oracle 的公平性讨论\n- 自我污染设定（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）是否过度简化\n- Detector 选择：只有 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram PPL），是否充分\n- ρ=0.2 失败和 1.7B 效果减弱的分析是否充分\n\n### 3. 统计严谨性\n- 主要声称 Δ=-0.020 (p=0.025) 在 N=3 下的可信度\n- 多重比较校正是否需要\n- Effect size vs. practical significance：0.020 PPL 差异的实际意义\n- 从 seed 42 到 from-scratch seeds 的 resume artifact 问题是否彻底解决\n\n### 4. 可复现性\n- 代码和数据承诺 upon acceptance，但当前是否提供足够细节\n- 超参数设置是否完整\n- 实验细节是否足够复现\n\n请提供完整审稿报告，格式为：Summary → Strengths → Weaknesses → Questions → Minor Issues。Weaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ARR May 2026\n- **截止日期**：2026-05-25\n- **格式**：ACL 模板，正文 8 页限制（参考文献不限），double-blind\n- **匿名规则**：严格 double-blind，禁止透露作者身份\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`\n\n## 审查侧重\n\n### 1. 数学推导与理论基础\n- Proposition 1 (α_eff 单调性) 和 Proposition 2 (ESS 单调性) 的证明是否严谨\n- 双约束框架 (Eq. 4) 的三种 regime 划分是否完备且互斥\n- α_eff 作为真实 real fraction 的代理指标，Pearson r≈0.70 是否足够支撑整个方法的理论动机\n- b* 的 bisection 求解在 B=4 离散情况下的行为是否被充分讨论\n\n### 2. 实验设计与对照\n- 3 seeds (N=3) 的统计检验力是否足够支撑所有声称（尤其是 p=0.025 的结果）\n- Epoch confound 分析：epoch-matched 对照是否完全消除了混淆因素（LR schedule 是否也是混淆？）\n- Grid-b 作为 post-hoc oracle 的公平性讨论\n- 自我污染设定（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）是否过度简化\n- Detector 选择：只有 3 个 detector（TF-IDF+LR, GPT-2 PPL, N-gram PPL），是否充分\n- ρ=0.2 失败和 1.7B 效果减弱的分析是否充分\n\n### 3. 统计严谨性\n- 主要声称 Δ=-0.020 (p=0.025) 在 N=3 下的可信度\n- 多重比较校正是否需要\n- Effect size vs. practical significance：0.020 PPL 差异的实际意义\n- 从 seed 42 到 from-scratch seeds 的 resume artifact 问题是否彻底解决\n\n### 4. 可复现性\n- 代码和数据承诺 upon acceptance，但当前是否提供足够细节\n- 超参数设置是否完整\n- 实验细节是否足够复现\n\n请提供完整审稿报告，格式为：Summary → Strengths → Weaknesses → Questions → Minor Issues。Weaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-21T14:03:10.479980+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16791
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-21T14:03:10.581657+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ARR May 2026\n- **截止日期**：2026-05-25\n- **格式**：ACL 模板，正文 8 页限制（参考文献不限），double-blind\n- **匿名规则**：严格 double-blind，禁止透露作者身份\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`\n\n## 审查侧重\n\n### 1. 新颖性与贡献定位\n- 与 Drayson et al. (2025) 的关键区别是否足够显著（同一 weighting formula，区别在于 b 的选择方式）\n- \"Epoch confound\" 发现是否足够 novel（multi-epoch exposure 的混淆在数据选择领域是否已知？）\n- \"Calibration matters\" 的发现是否有足够创新性\n- 双约束框架作为方法论贡献，在技术深度上是否足够\n\n### 2. Related Work 覆盖\n- 是否遗漏重要相关工作？特别关注：\n  - Model collapse 领域的最新工作\n  - Data curation / filtering 领域\n  - Importance weighting 在 LLM 训练中的应用\n  - Synthetic data detection 的最新方法\n- 与 domain-level mixing (DoReMi, AIOLI 等) 的区分是否清晰\n- 与 instance-level reweighting (focal loss, curriculum learning) 的关系是否充分讨论\n\n### 3. 写作质量与叙事逻辑\n- Introduction 的 4 个 findings 是否逻辑清晰\n- \"Minimum intervention\" 概念是否被很好地激励和解释\n- 从分析性发现（F1-F3）到方法（adaptive b*）的过渡是否自然\n- Abstract 是否准确反映论文贡献（不过度宣称也不遗漏）\n- Discussion 是否充分（当前只有 11 行，是否太短？）\n- Conclusion 是否太简短？\n\n### 4. 格式合规性（EMNLP 2026 / ARR）\n- 正文是否在 8 页限制内（检查 PDF 页数）\n- 是否使用正确的 ACL 模板（\\usepackage[review]{acl}）\n- 匿名是否完整（检查 \\author{Anonymous}，自引是否泄露身份）\n- Limitations section 是否存在且适当\n- Responsible NLP Checklist 是否完整\n- 引用格式是否正确（natbib）\n\n### 5. 效果大小与实用性\n- Δ=-0.020 PPL 的改进在实际应用中是否有意义\n- \"消除 grid search\" 的实用价值是否被合理论证\n- 方法在 ρ=0.2 失败、1.7B 效果减弱——这限制了实用性，是否被充分讨论\n\n请提供完整审稿报告，格式为：Summary → Strengths → Weaknesses → Questions → Minor Issues。Weaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## Venue 信息\n- **目标**：EMNLP 2026 via ARR May 2026\n- **截止日期**：2026-05-25\n- **格式**：ACL 模板，正文 8 页限制（参考文献不限），double-blind\n- **匿名规则**：严格 double-blind，禁止透露作者身份\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.pdf`\n\n## 审查侧重\n\n### 1. 新颖性与贡献定位\n- 与 Drayson et al. (2025) 的关键区别是否足够显著（同一 weighting formula，区别在于 b 的选择方式）\n- \"Epoch confound\" 发现是否足够 novel（multi-epoch exposure 的混淆在数据选择领域是否已知？）\n- \"Calibration matters\" 的发现是否有足够创新性\n- 双约束框架作为方法论贡献，在技术深度上是否足够\n\n### 2. Related Work 覆盖\n- 是否遗漏重要相关工作？特别关注：\n  - Model collapse 领域的最新工作\n  - Data curation / filtering 领域\n  - Importance weighting 在 LLM 训练中的应用\n  - Synthetic data detection 的最新方法\n- 与 domain-level mixing (DoReMi, AIOLI 等) 的区分是否清晰\n- 与 instance-level reweighting (focal loss, curriculum learning) 的关系是否充分讨论\n\n### 3. 写作质量与叙事逻辑\n- Introduction 的 4 个 findings 是否逻辑清晰\n- \"Minimum intervention\" 概念是否被很好地激励和解释\n- 从分析性发现（F1-F3）到方法（adaptive b*）的过渡是否自然\n- Abstract 是否准确反映论文贡献（不过度宣称也不遗漏）\n- Discussion 是否充分（当前只有 11 行，是否太短？）\n- Conclusion 是否太简短？\n\n### 4. 格式合规性（EMNLP 2026 / ARR）\n- 正文是否在 8 页限制内（检查 PDF 页数）\n- 是否使用正确的 ACL 模板（\\usepackage[review]{acl}）\n- 匿名是否完整（检查 \\author{Anonymous}，自引是否泄露身份）\n- Limitations section 是否存在且适当\n- Responsible NLP Checklist 是否完整\n- 引用格式是否正确（natbib）\n\n### 5. 效果大小与实用性\n- Δ=-0.020 PPL 的改进在实际应用中是否有意义\n- \"消除 grid search\" 的实用价值是否被合理论证\n- 方法在 ρ=0.2 失败、1.7B 效果减弱——这限制了实用性，是否被充分讨论\n\n请提供完整审稿报告，格式为：Summary → Strengths → Weaknesses → Questions → Minor Issues。Weaknesses 按严重程度排序（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-21T14:03:14.422343+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3840
}
```

</details>

---


### Assistant

_source line 824 · 2026-05-21T14:03:28.220105+00:00_

Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 实验设计 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 完整性 + 写作质量 |
| 视觉审查 Agent | ✅ 已启动 | PDF 排版质量（非评分项） |
| 外部审稿 | ⏭️ 跳过 | 项目未配置 paperreview.ai |

等待两名 Reviewer 返回独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 825 · 2026-05-21T14:15:16.054519+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 论文发现了有价值的 epoch confound 和 calibration 必要性，但核心自适应方法在 N=3 下统计支撑不足、无下游任务改善、且主文与 checklist 存在 p 值矛盾。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 理论框架合理，但核心实验声称受限于 N=3 统计功效不足、p 值自相矛盾、实际效应量微小（Δ=-0.020, 0.11%），且 epoch+LR 完全控制后 D&R 反而退化 |
| Excitement | 3/5 | Epoch confound 发现对社区有实用价值，calibration 要求是可操作的 insight；但自适应方法本身效果微弱且缺乏下游验证 |
| Reproducibility | 3.5/5 | 超参数、算法伪代码、训练配置较完整；代码承诺 upon acceptance 但未提供匿名仓库 |
| Reviewer Confidence | 4/5 | 本人熟悉重要性采样、LM 预训练、数据质量方法 |

---

## Summary

本文研究 detect-and-reweight (D&R) 范式在含合成污染的 continued LM pretraining 中何时有效。使用 Qwen3-0.6B 在 132M FineWeb token（ρ=0.4 合成比例）上进行实验，3 个 seed，得出三个发现：(1) D&R 的 PPL 优势 >95% 归因于多 epoch 暴露（epoch confound），而非过滤质量；(2) 有效重加权同时需要检测器的高区分度（AUC）和良好校准（低 ECE）；(3) 提出双约束自适应框架（α_eff 质量下限 + ESS 稳定性上限）在最小干预下维持训练质量，声称 Δ=-0.020 PPL 改善（p=0.025）。

---

## 主要优势

**S1. Epoch confound 发现具有独立贡献价值。** Table 1 (§5.1) 的 epoch-matched 对照实验表明 D&R full 的 PPL 优势从 Δ=-2.4 缩小到 Δ=+0.017（几乎消失），揭示了此前文献未充分讨论的混淆因素。这一发现对所有使用 D&R 的后续工作具有直接指导意义。

**S2. Calibration 必要性是可操作的实践指导。** Table 10 (Appendix K) 展示了 TF-IDF+LR（AUC=0.94, ECE=0.048）有效而 N-gram PPL（AUC=0.939, better ECE=0.069）无法补偿 insufficient AUC (0.73) 的结果。"区分度+校准缺一不可"这一结论具有实用性。

**S3. 理论框架设计合理。** 双约束公式化（Eq. 4）将 convergence guarantee（Wang et al., 2026）和 importance sampling stability（Kish, 1965）统一在同一框架内。Proposition 1（α_eff 单调性）和 Proposition 2（ESS 单调性）的证明思路清晰，利用协方差符号论证。

**S4. 对自身局限性诚实处理。** 论文主动报告了 ρ=0.2 退化、1.7B 效果减弱、checkpoint resume artifact（Appendix O），并提供了 from-scratch seed 分析。这种透明度在实证研究中值得肯定。

**S5. 附录分析全面。** 15 个附录覆盖 grid search、阈值敏感性、batch-adaptive 变体、constraint regime 分解、proxy 验证、cross-model transfer 等，展现了充分的实验探索。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 的统计功效根本不足以支撑核心声称
- **具体位置**: §5.1, Abstract, §7
- **问题**: 
  (a) 核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感——一个异常 seed 即可驱动整个结果。论文未报告所有比较的逐 seed PPL 值，无法判断改善是否跨 seed 一致。
  (b) 以 df=2 获得 p=0.025（双尾），t 统计量需 ≈6.2，意味着三个 seed 的差异异常一致。对于随机性极高的 LM 训练过程，这种一致性本身就应引起怀疑而非增加信心。
  (c) 论文测试了 6 种方法 × 2 个 ρ 值 × 3 个评估域 × 2 个模型大小，未做任何多重比较校正（Bonferroni、FDR 等）。在如此多的比较中，找到 p<0.05 的概率本身就很高。
  (d) Appendix O 揭示 seed 42 使用了 checkpoint-resumed 训练，resume artifact 膨胀了表观效应。From-scratch seeds 的效果更弱。
- **为什么影响接收**: 论文的第三个核心发现（自适应方法有效）完全依赖这一统计检验。如果 p 值不可靠，该发现无法成立。
- **建议修改方向**: 增加到 ≥5 seeds（理想 10 seeds），报告逐 seed 结果及 bootstrap confidence intervals，对所有声称的比较做 FDR 校正。

**N2** [critical] 实际显著性存疑：Δ=-0.020 PPL 无下游任务改善
- **具体位置**: §5.1 (主要 PPL 声称), Table 7 (Appendix H, 下游基准)
- **问题**:
  (a) Δ=-0.020 在 base PPL ≈17.7 上仅为 0.11% 的相对改善，处于大多数实际应用的噪声范围内。
  (b) Table 7 明确表明下游任务性能"all differences within standard error (±0.01)"，三 seed 均值完全相同（0.5414）。PPL 微小改善未转化为任何可测量的任务性能提升。
  (c) 论文以 PPL 为主要指标却未充分论证为什么 0.020 的 PPL 差异具有实践价值。如果方法无法改善任何下游任务，其实际动机何在？
- **为什么影响接收**: 方法论文的核心价值在于实用性。无下游改善意味着该方法的实际贡献有限。
- **建议修改方向**: (1) 明确讨论 PPL vs 下游的 gap 及其对方法定位的影响；(2) 考虑在更大污染比例或更大模型上测试是否存在 PPL→下游的 transfer；(3) 或重新定位论文为分析性贡献而非方法贡献。

**N3** [critical] 主文与 Checklist 的 p 值矛盾
- **具体位置**: §5.1 报告 p=0.025；Responsible NLP Research Checklist §C3 报告 p=0.0425（同一比较：adaptive vs. uniform at ρ=0.4）
- **问题**: 对于核心声称存在两个不同的 p 值。在一篇统计显著性已处于边缘的论文中，这一矛盾严重损害了对统计分析的信心。无论哪个值正确，另一处都是错误的——这意味着至少有一处计算或转录存在问题。
- **为什么影响接收**: 如果真实 p=0.0425 而非 0.025，结论的可信度进一步下降。核心声称的 p 值不应自相矛盾。
- **建议修改方向**: 核实并统一，报告准确的检验统计量（t 值、df、exact p）以及检验类型（单尾/双尾）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 自我污染设定是不切实际的简化检测场景
- **具体位置**: §4 (Training Data), §7 (Limitations 简要提及)
- **问题**: Qwen3-0.6B 生成 + Qwen3-0.6B 训练（§4）创造了最有利的检测环境——生成器和训练目标共享完全相同的架构和分词器。真实世界的 web 污染包含来自 GPT-4、Claude、Gemini、各种开源模型的异构合成文本，检测难度远高于此。
  Table 11 (Appendix N) 的 cross-model transfer（Llama-3.2-3B 生成）仅为"preliminary single-seed"，且结果"mixed"——HellaSWag 轻微退化。这不足以支撑方法的通用性。
- **建议**: 增加 ≥2 种跨模型污染实验（不同架构、不同规模的生成器）；或在 Limitations 中更显著地限定结论范围为 self-contamination。

**W2** [warning] 完全控制混淆因素后 D&R 过滤本身有害
- **具体位置**: §5.1, Table 1
- **问题**: Table 1 显示 epoch-matched + LR-matched 对照下，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。这意味着过滤机制本身在剥离 multi-epoch 和 LR schedule 交互效应后是有害的。自适应方法的改善可能完全来自 LR schedule 交互作用，而非智能重加权。论文将此描述为"warm LR from multi-epoch exposure"但未直面其对方法核心动机的冲击——如果重加权机制本身不起正面作用，双约束框架的意义需要重新审视。
- **建议**: 需要一个控制实验，在保持 LR schedule 一致的条件下（如相同步数、相同 LR schedule 但不同 b*）测试自适应方法是否仍有优势。

**W3** [warning] 检测器覆盖面窄：仅 3 个检测器来自 2 个家族
- **具体位置**: §5.2, Appendix K, Table 10
- **问题**: 仅测试了 TF-IDF+LR（判别式）、GPT-2 PPL（生成式）、N-gram PPL（统计式）。缺少：fine-tuned 神经分类器（RoBERTa/DeBERTa-based）、DetectGPT/Fast-DetectGPT（论文在 Related Work 中引用但未评估）、watermark-based 方法、Binoculars 等。"区分度+校准缺一不可"的结论可能是检测器家族特异性的。
- **建议**: 至少补充一个 fine-tuned 神经检测器的实验，以验证 calibration 发现的通用性。

**W4** [warning] α_eff 作为真实人类比例代理：r=0.70 仅解释 49% 方差
- **具体位置**: §3.2, Table 9 (Appendix J)
- **问题**: Pearson r≈0.70 意味着 r²=0.49，超过一半的真实人类比例方差未被 α_eff 捕获。Table 9 还显示在 batch size=1 时 r=-0.16，需要 batch size ≥4 才达到 0.70。方法的理论动机——α_eff 追踪污染程度——仅获得中等程度的经验支撑。论文未讨论 51% 未解释方差的来源及其对方法可靠性的影响。
- **建议**: 分析残差来源（是检测器噪声还是 α_eff 公式的系统偏差？），讨论对方法鲁棒性的影响。

**W5** [warning] ρ=0.2 失败和 1.7B 效果减弱分析不充分
- **具体位置**: §5.2 (boundary conditions), Appendix M (low contamination)
- **问题**: 
  (a) ρ=0.2 退化 +0.040 PPL，归因于"q-scores 模糊化"，但未给出该污染水平下检测器的具体 AUC/ECE，也未测试不同 τ 是否能挽救。Appendix M 提供了些分析但仍是 seed 42 only。
  (b) 1.7B 效果不显著（Δ=+0.013），论文解释为"大模型对 0.6B 生成文本更鲁棒"。但这也意味着方法在最需要的场景（大模型 at scale）可能无用。这两个边界条件的分析对方法的适用范围界定至关重要。
- **建议**: (1) 报告 ρ=0.2 下检测器指标；(2) 测试 1.7B 模型受 1.7B 生成文本污染的场景；(3) 明确标定方法的适用条件。

**W6** [warning] B=4 离散空间上的 bisection 与连续理论的脱节
- **具体位置**: §3.3, Algorithm 1
- **问题**: Micro-batch B=4 时，α_eff 实际只取 5 个离散值（§3.3 明确说明："α_eff takes only five discrete values {0, 0.25, 0.5, 0.75, 1.0}"）。Bisection 算法是连续优化工具，但搜索空间实际上只有 5 个点。Propositions 1-2 的连续单调性保证与离散实现之间的 gap 未被讨论。
- **建议**: (1) 讨论离散化对理论保证的影响；(2) 说明为何不直接枚举 5 个值而使用 bisection；(3) 考虑测试更大 batch size 下连续近似是否改善。

---

## 小问题（不影响接收）

- **Figure 2 (p.8)**: 仅展示 seed 42 的 PPL 曲线。添加其他 seed 的曲线（或置信带）会更有说服力。
- **Appendix O (Checkpoint Resume Artifact)**: 此发现对主文 seed 42 结果的解读有直接影响，建议在主文 §5.1 中简要提及而非仅放附录。
- **Vehtari et al. 引用**: bib 标注 2024 年（JMLR 发表年），但该工作原始 arXiv 版本为 2015 年。建议注明。
- **匿名仓库**: 论文承诺 code/data upon acceptance 但未提供匿名代码仓库，限制了审稿期间的复现性评估。
- **Table 2 (p.7)**: Held-out perplexity 的 "per-seed results rounded to three decimal places" 对于 Δ=0.020 级别的效应量，3 位小数的 rounding 可能引入 artifacts——建议报告更多有效数字。

---

## Questions for Authors

**Q1.** §5.1 报告 p=0.025，§C3 报告 p=0.0425，请澄清哪个值正确？请同时报告完整的检验信息（t 值、df、检验类型单尾/双尾）。

**Q2.** 三个 from-scratch seeds 在 adaptive vs. uniform (ρ=0.4) 下各自的 PPL 值是多少？改善是三个 seed 一致的还是主要由某个 seed 驱动？

**Q3.** Table 7 显示下游任务性能完全无差异（均值 0.5414）。在无下游改善的情况下，该方法的实际应用动机是什么？

**Q4.** §5.1/Table 1: epoch-matched + LR-matched 对照下 D&R 劣于 uniform (Δ=+0.72)。如何调和这一发现与"重加权机制独立于 epoch 效应有贡献"的声称？

**Q5.** 是否考虑过异构合成源（如混合 GPT-4 + Llama + Qwen 生成的文本）的实验，以测试 calibration 发现的通用性？

**Q6.** α_eff 与真实人类比例仅 r=0.70。剩余 51% 方差中，有多少来自检测器噪声 vs. α_eff 公式的系统偏差？这对方法在不同检测器/数据分布下的可迁移性有何影响？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 826 · 2026-05-21T14:15:22.762952+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 60

## Round 60

6 recorded events


### User

_source line 827 · 2026-05-21T14:15:31.615403+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量

### 总体评分

**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）

**一句话总结**: 论文在实验控制上做得扎实（epoch confound 的发现有价值），但核心方法论贡献（adaptive b*）相对于 Drayson et al. (2025) 是增量式改进，效果规模小（Δ=-0.020 PPL），且适用范围受限（ρ=0.2 失败、1.7B 减弱），不足以支撑主会议接收。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（epoch-matched controls、3 seeds、多 ablation），但实验范围窄（单模型族 Qwen3、单数据域 FineWeb、仅 self-contamination），且 Appendix O 揭示 "distribution matching" finding 本身是 checkpoint resume artifact |
| Excitement | 2.5/5 | Epoch confound 对社区有诊断价值，但方法贡献增量性强，效果规模极小，实用场景受限 |
| Reproducibility | 4/5 | 实验细节充分（Algorithm 1、超参数、训练配置均在正文/附录），代码承诺 upon acceptance 释放 |
| Reviewer Confidence | 4/5 | 熟悉 data curation/reweighting 和 model collapse 领域 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 相对于 Drayson et al. (2025) 的新颖性不足

- 具体位置：Section 3.1, Eq. (1); Section 1 右栏
- 问题：论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b。核心区别仅在于 b 的选择方式——Drayson 用 validation-set grid search，本文用双约束自适应选择。但这本质上是一个超参数自动调节方案，而非方法论层面的根本创新。双约束中的 ESS 约束是重要性采样文献中的标准工具（Kish 1965, Owen 2013），σ_adj 质量下限是直觉性阈值。将两个标准工具组合为一个自适应选择器，技术深度有限。
- 为什么影响接收：对于 EMNLP 主会议，方法论新颖性是核心评价维度。一个增量式的超参数选择改进——即使附带了有价值的诊断分析——难以达到 "Conference" 级别的贡献门槛。
- 建议修改方向：(a) 更深入地分析为什么 Drayson 的 grid search 在某些条件下系统性失败，论证 adaptive b* 在质量上而非仅效率上的优势；(b) 或将论文明确定位为 "analysis paper"，将 adaptive b* 降格为分析结论的自然推论，同时深化 F1-F3 的理论分析。

**N2** [critical] 效果规模极小，实用价值论证不足

- 具体位置：Abstract (Δ=−0.020); Table 1 (epoch-matched Δ=0.017); Table 2 (各方法对比)
- 问题：核心效果数字是 epoch-matched 后的 Δ=0.017 PPL 和 adaptive b* vs. uniform 的 Δ=−0.020 PPL（约 0.11%）。ρ=0.2 时方法失败（+0.040 退化），1.7B 时效果减弱，下游任务评估（Appendix H, Table 7）差异在标准误差范围内。如果 PPL 微小改进不转化为下游能力提升，整个 reweighting 工作的价值存疑。
- 为什么影响接收：效果规模过小使得方法论贡献的实际意义存疑。
- 建议修改方向：(a) 在更大规模或更多样化的污染场景下验证效果是否放大；(b) 或重新定位为 "负面结果 + 诊断分析" 论文。

**N3** [critical] Discussion 部分过于单薄（Section 6，约 11 行）

- 具体位置：Section 6 (p.8)
- 问题：对于一篇声称揭示三项发现的分析型论文，Discussion 仅含两小段远远不够。以下关键问题未讨论：epoch confound 对已发表 D&R 工作的影响、多生成器场景的 calibration 挑战、adaptive b* 的理论最优性、adversarial 条件下的鲁棒性。
- 建议修改方向：至少增加 1 页 Discussion。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 实验场景过窄——仅 self-contamination，单一数据域。Cross-model transfer (Appendix N) 仅单 seed 且 "mixed results"。

**W2** [warning] "Minimum intervention" 概念缺乏充分动机。未解释为什么过度降权有害（误杀真阳性？合成数据本身有价值？）。

**W3** [warning] Conclusion 过于简短（~8 行），缺乏前瞻性讨论。

**W4** [warning] 论文在 "分析论文" 与 "方法论文" 之间定位模糊，双重定位削弱了两个维度的说服力。

**W5** [warning] 下游任务评估不足——PPL 0.02 改进无法转化为下游任务改进（Appendix H），但该负面结果仅放在附录未在正文讨论。

---

### 小问题

1. Abstract "three findings" vs. Introduction 中 F1/F2/F3 + adaptive b* 的措辞不一致。
2. Table 2 "Oracle" baseline 实现细节不足。
3. Vehtari et al. 年份可能需核实（OpenAlex 匹配到 2015 而非 2024）。
4. Figure 2 图例 crowded，建议改善。
5. Section 5.1 中 GPT-2/N-gram 检测器突然出现，未在 Setup 预先说明。
6. Checklist E1 披露使用 AI assistants 是合规的，但建议确认所有 claim 由作者独立验证。

---

### 格式合规性

全部通过：正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确（52 条 bib 全部 verified，无 orphan/missing/伪造）。

---

### Questions to Authors

1. Epoch confound 在其他 D&R 工作中是否也存在？已发表的效果声明是否需要重新验证？
2. 双约束的选择是经验性的还是有理论最优性依据？
3. 是否有计划进行更系统的 cross-model 评估？
4. Appendix O 的 checkpoint artifact 是否意味着 F1-F3 中某些发现可能是 continued pretraining 特有的？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-21T14:15:53.751664+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 论文在实验控制上做得扎实（epoch confound 的发现有价值），但核心方法论贡献（adaptive b*）相对于 Drayson et al. (2025) 是增量式改进，效果规模小（Δ=-0.020 PPL），且适用范围受限（ρ=0.2 失败、1.7B 减弱），不足以支撑主会议接收。\n\n### Must-Fix 问题\n\n**N1** [critical] 相对于 Drayson et al. (2025) 的新颖性不足\n- 论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b。核心区别仅在于 b 的选择方式——Drayson 用 validation-set grid search，本文用双约束自适应选择。但这本质上是一个超参数自动调节方案，而非方法论层面的根本创新。双约束中的 ESS 约束是重要性采样文献中的标准工具（Kish 1965, Owen 2013），α_eff 质量下限是直觉性阈值。将两个标准工具组合为一个自适应选择器，技术深度有限。\n\n**N2** [critical] 效果规模极小，实用价值论证不足\n- 核心效果数字是 Δ=−0.020 PPL（约 0.11%）。ρ=0.2 时方法失败（+0.040 退化），1.7B 时效果减弱，下游任务评估差异在标准误差范围内。如果 PPL 微小改进不转化为下游能力提升，整个 reweighting 工作的价值存疑。\n\n**N3** [critical] Discussion 部分过于单薄（Section 6，约 11 行）\n- 对于一篇声称揭示三项发现的分析型论文，Discussion 仅含两小段远远不够。\n\n### Should-Fix 问题\n\n**W1** [warning] 实验场景过窄——仅 self-contamination，单一数据域。Cross-model transfer (Appendix N) 仅单 seed 且 \"mixed results\"。\n\n**W2** [warning] \"Minimum intervention\" 概念缺乏充分动机。未解释为什么过度降权有害。\n\n**W3** [warning] Conclusion 过于简短（~8 行），缺乏前瞻性讨论。\n\n**W4** [warning] 论文在 \"分析论文\" 与 \"方法论文\" 之间定位模糊，双重定位削弱了两个维度的说服力。\n\n**W5** [warning] 下游任务评估不足——PPL 改进无法转化为下游任务改进，但该负面结果仅放在附录未在正文讨论。\n\n### 格式合规性\n全部通过：正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确。\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 论文在实验控制上做得扎实（epoch confound 的发现有价值），但核心方法论贡献（adaptive b*）相对于 Drayson et al. (2025) 是增量式改进，效果规模小（Δ=-0.020 PPL），且适用范围受限（ρ=0.2 失败、1.7B 减弱），不足以支撑主会议接收。\n\n### Must-Fix 问题\n\n**N1** [critical] 相对于 Drayson et al. (2025) 的新颖性不足\n- 论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b。核心区别仅在于 b 的选择方式——Drayson 用 validation-set grid search，本文用双约束自适应选择。但这本质上是一个超参数自动调节方案，而非方法论层面的根本创新。双约束中的 ESS 约束是重要性采样文献中的标准工具（Kish 1965, Owen 2013），α_eff 质量下限是直觉性阈值。将两个标准工具组合为一个自适应选择器，技术深度有限。\n\n**N2** [critical] 效果规模极小，实用价值论证不足\n- 核心效果数字是 Δ=−0.020 PPL（约 0.11%）。ρ=0.2 时方法失败（+0.040 退化），1.7B 时效果减弱，下游任务评估差异在标准误差范围内。如果 PPL 微小改进不转化为下游能力提升，整个 reweighting 工作的价值存疑。\n\n**N3** [critical] Discussion 部分过于单薄（Section 6，约 11 行）\n- 对于一篇声称揭示三项发现的分析型论文，Discussion 仅含两小段远远不够。\n\n### Should-Fix 问题\n\n**W1** [warning] 实验场景过窄——仅 self-contamination，单一数据域。Cross-model transfer (Appendix N) 仅单 seed 且 \"mixed results\"。\n\n**W2** [warning] \"Minimum intervention\" 概念缺乏充分动机。未解释为什么过度降权有害。\n\n**W3** [warning] Conclusion 过于简短（~8 行），缺乏前瞻性讨论。\n\n**W4** [warning] 论文在 \"分析论文\" 与 \"方法论文\" 之间定位模糊，双重定位削弱了两个维度的说服力。\n\n**W5** [warning] 下游任务评估不足——PPL 改进无法转化为下游任务改进，但该负面结果仅放在附录未在正文讨论。\n\n### 格式合规性\n全部通过：正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确。\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-21T14:16:13.631509+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19879
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-21T14:16:13.682568+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 论文发现了有价值的 epoch confound 和 calibration 必要性，但核心自适应方法在 N=3 下统计支撑不足、无下游任务改善、且主文与 checklist 存在 p 值矛盾。\n\n### Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计功效根本不足以支撑核心声称\n- 核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感。论文测试了 6 种方法 × 2 个 ρ 值 × 3 个评估域 × 2 个模型大小，未做任何多重比较校正。Appendix O 揭示 seed 42 使用了 checkpoint-resumed 训练。\n\n**N2** [critical] 实际显著性存疑：Δ=-0.020 PPL 无下游任务改善\n- Δ=-0.020 在 base PPL ≈17.7 上仅为 0.11% 的相对改善。Table 7 明确表明下游任务性能\"all differences within standard error (±0.01)\"，三 seed 均值完全相同（0.5414）。\n\n**N3** [critical] 主文与 Checklist 的 p 值矛盾\n- §5.1 报告 p=0.025；Responsible NLP Research Checklist §C3 报告 p=0.0425（同一比较）。核心声称存在两个不同的 p 值。\n\n### Should-Fix 问题\n\n**W1** [warning] 自我污染设定是不切实际的简化检测场景\n- Qwen3-0.6B 生成 + Qwen3-0.6B 训练创造了最有利的检测环境。\n\n**W2** [warning] 完全控制混淆因素后 D&R 过滤本身有害\n- epoch-matched + LR-matched 对照下，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。自适应方法的改善可能完全来自 LR schedule 交互作用，而非智能重加权。\n\n**W3** [warning] 检测器覆盖面窄：仅 3 个检测器来自 2 个家族\n- 缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa-based）、DetectGPT/Fast-DetectGPT 等。\n\n**W4** [warning] α_eff 作为真实人类比例代理：r=0.70 仅解释 49% 方差\n\n**W5** [warning] ρ=0.2 失败和 1.7B 效果减弱分析不充分\n\n**W6** [warning] B=4 离散空间上的 bisection 与连续理论的脱节\n- Micro-batch B=4 时，α_eff 实际只取 5 个离散值。Bisection 是连续优化工具，但搜索空间实际上只有 5 个点。\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 论文发现了有价值的 epoch confound 和 calibration 必要性，但核心自适应方法在 N=3 下统计支撑不足、无下游任务改善、且主文与 checklist 存在 p 值矛盾。\n\n### Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计功效根本不足以支撑核心声称\n- 核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感。论文测试了 6 种方法 × 2 个 ρ 值 × 3 个评估域 × 2 个模型大小，未做任何多重比较校正。Appendix O 揭示 seed 42 使用了 checkpoint-resumed 训练。\n\n**N2** [critical] 实际显著性存疑：Δ=-0.020 PPL 无下游任务改善\n- Δ=-0.020 在 base PPL ≈17.7 上仅为 0.11% 的相对改善。Table 7 明确表明下游任务性能\"all differences within standard error (±0.01)\"，三 seed 均值完全相同（0.5414）。\n\n**N3** [critical] 主文与 Checklist 的 p 值矛盾\n- §5.1 报告 p=0.025；Responsible NLP Research Checklist §C3 报告 p=0.0425（同一比较）。核心声称存在两个不同的 p 值。\n\n### Should-Fix 问题\n\n**W1** [warning] 自我污染设定是不切实际的简化检测场景\n- Qwen3-0.6B 生成 + Qwen3-0.6B 训练创造了最有利的检测环境。\n\n**W2** [warning] 完全控制混淆因素后 D&R 过滤本身有害\n- epoch-matched + LR-matched 对照下，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。自适应方法的改善可能完全来自 LR schedule 交互作用，而非智能重加权。\n\n**W3** [warning] 检测器覆盖面窄：仅 3 个检测器来自 2 个家族\n- 缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa-based）、DetectGPT/Fast-DetectGPT 等。\n\n**W4** [warning] α_eff 作为真实人类比例代理：r=0.70 仅解释 49% 方差\n\n**W5** [warning] ρ=0.2 失败和 1.7B 效果减弱分析不充分\n\n**W6** [warning] B=4 离散空间上的 bisection 与连续理论的脱节\n- Micro-batch B=4 时，α_eff 实际只取 5 个离散值。Bisection 是连续优化工具，但搜索空间实际上只有 5 个点。\n\n---\n\n请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-21T14:16:15.022154+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1339
}
```

</details>

---


### Assistant

_source line 832 · 2026-05-21T14:16:17.873004+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 61

## Round 61

16 recorded events


### User

_source line 833 · 2026-05-21T14:16:18.923548+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心判断：

- **Overall 3.0（Findings）**：epoch confound 和 calibration 必要性两个发现有独立价值，但自适应方法本身受限于 N=3 统计功效不足、p 值矛盾（主文 0.025 vs checklist 0.0425）、无下游改善（Table 7 均值完全相同）、以及完全控制混淆后 D&R 反而退化（Δ=+0.72）。
- **3 个 Must-Fix**：统计功效、实际显著性、p 值矛盾
- **6 个 Should-Fix**：自我污染过简、epoch+LR 控制后 D&R 有害、检测器覆盖窄、α_eff 代理质量中等、边界条件分析不足、离散空间与连续理论脱节

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.0 (Findings)。论文实验控制严谨，epoch confound 发现有社区诊断价值，但三个 critical 问题制约主会议接收：(1) 相对 Drayson et al. 的方法论新颖性有限（同一公式，仅改变超参数选择方式）；(2) 效果规模极小（Δ=-0.020 PPL ≈ 0.11%），下游任务无显著改进；(3) Discussion 过于单薄。建议明确论文定位（分析论文 vs. 方法论文）并扩展讨论深度。格式合规性全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-21T14:16:40.070618+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.0425|p\\s*=\\s*0\\.02",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.0425|p\\s*=\\s*0\\.02",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-21T14:16:40.823680+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-21T14:16:40.874271+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-21T14:16:41.025242+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T14:02:37.145978+00:00\", \"completed_at\": \"2026-05-21T14:05:35.648970+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，视觉锚点（Figure 1）出现在第 2 页顶部。虽然在\\\"前 3 页\\\"范围内，但若能将 Figure 1 提升至第 1 页底部（如压缩 Abstract 或 Introduction 开头），审稿人打开论文的第一秒就能看到核心 overview。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 是分析概览流程图，能传达论文三个核心发现（F1/F2/F3）和自适应方法，信息传达清晰。但图内文字密度较高（每个 box 含多行文字），在缩略视图下可读性下降。建议精简 box 内文字或增加图示/图标元素，提升视觉直觉性。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"4 页跨度内仅有 Algorithm 1（第 5 页）作为 display item。第 3-4 页为 Method 数学推导（有 display equations 做视觉间隔，可接受），但第 6 页（实验设置 + 结果开头）为纯文本，且主结果表格直到第 7 页才出现。审稿人在 §5.1 Main Results 开始阅读结果讨论时看不到对应表格，需要翻页。建议考虑将一个简明的实验设置总结表（如数据集/模型/规模一览）放入第 5-6 页，打破纯文本节奏。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Algorithm 1 伪代码框排版整洁，提供了良好的视觉间隔。格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Table 2 使用 booktabs 风格（仅水平线，无竖线），最优结果加粗标注，小数精度一致。排版质量高。两表集中在同一页，视觉密度合适。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 caption 提到 \\\"epoch-matched comparison (ρ=0.4, 3 seeds, Seed 42 only)\\\"——自包含程度良好，审稿人仅读 caption 可理解表格内容。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 曲线图清晰：坐标轴标签可读，多 seed 曲线用不同标记区分，灰色阴影区域标注\\\"degradation zone\\\"。颜色区分度可接受。Caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页含 2 figure + 2 table + 1 algorithm = 5 个 display items。对于兼具理论推导和实证的论文，密度处于可接受下限。若空间允许，建议从附录提升一个关键 figure（如 Figure 3 的 regime decomposition 或 Figure 5 的 epoch 效应图）到主文，增强视觉说服力。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion（§6）和 Conclusion（§7）压缩在同一页 Figure 2 下方。内容完整但版面紧凑，如需扩展讨论内容可能面临空间限制。主文恰好 8 页，符合 EMNLP 2026 页数限制。\"}, {\"severity\": \"info\", \"dimension\": \"page 9
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-21T14:16:41.176304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-21T14:16:41.327514+00:00_

issues:
- id: "R1-W1"
  summary: "效果大小不足以支撑方法论贡献（Δ=−0.020 PPL / 0.11%，下游为零）"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "R1 标 critical，R2 在 N1 中同意（incremental contribution）。交叉回应 R2 [AGREE] R1-W1。"
  action_items:
    - round: 1
      action: "Reframe 为 analysis paper — effect size 不再是 primary claim 的支柱。Rebuttal: zero-cost advantage + effect scales with ρ (-0.020→-0.032) + analysis contributions 不依赖 effect size"
      assigned_to: "Director + Paper Agent"
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R1-W2"
  summary: "B=4 下 dual-constraint 框架实质退化（α_eff 仅 5 离散值，α_eff-binding 占比极低）"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "R1 标 critical。R2 [AGREE] 核心论点但质疑 R1 的 ~0.2% 数字（论文报告 38.2%）。"
  action_items:
    - round: 1
      action: "Rebuttal: α_eff 是连续函数（非 5 离散值），38.2% binding 是正确数字（R1 的 ~0.2% 计算有误）。B=16 实验验证大 batch 下 binding 行为。α_eff 分布直方图可视化。"
      assigned_to: "Agent (B=16 exp) + Director (rebuttal)"
      status: pending
  resolution: ""
  resolution_round: null

- id: "R1-W3"
  summary: "Epoch-matched 比较引入 LR schedule confound（2533/6103 步 cosine schedule 不同阶段）"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "R1 标 critical，R2 标 major。交叉回应中 R1 将此升级为 critical（epoch confound 是论文最强贡献，其核心实验有 confound）；R2 [AGREE]。"
  action_items:
    - round: 1
      action: "LR confound 对照实验 x2: D&R epoch-matched + Uniform epoch-matched，各用独立 2533-step cosine schedule。cuda:1/2 dispatched。"
      assigned_to: "Agent"
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R2-N1"
  summary: "新颖性不足以支撑 main conference（三个贡献均偏 incremental）"
  category: framing
  sev
…[truncated 8624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-21T14:16:55.391023+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.042|p\\s*=",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.042|p\\s*=",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-21T14:16:55.441734+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:22:\abovecaptionskip=\skip49
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:23:\belowcaptionskip=\skip50
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:72:\linenumbersep=\dimen149
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:79:\quotelinenumbersep=\dimen151
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:81:\bframesep=\dimen153
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:100:\Gm@wd@mp=\dimen155
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:101:\Gm@odd@mp=\dimen156
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:102:\Gm@even@mp=\dimen157
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:132:\bibsep=\skip53
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:204:\Urlmuskip=\muskip17
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:369:\tag@help=\toks25
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:381:\multlinegap=\skip57
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:382:\multlinetaggap=\skip58
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:407:\thm@preskip=\skip59
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.log:408:\thm@postskip=\skip60
/home/ubuntu/.agent-ml-research-idea
…[truncated 2846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-21T14:17:02.722483+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p\\{?=\\}?0\\.\\d+|p\\\\leq|p<|p\\s*=\\s*0",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p\\{?=\\}?0\\.\\d+|p\\\\leq|p<|p\\s*=\\s*0",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-21T14:17:02.774913+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex:48:\textit{Yes. Main results report 3-seed means $\pm$ standard deviation (\S\ref{sec:main-results}). Paired $t$-tests are reported for the primary comparison (adaptive vs.\ uniform: $p{=}0.025$ at $\rho{=}0.4$, $p{=}0.004$ at $\rho{=}0.6$). $N{=}3$ limits statistical power; we report effect sizes alongside $p$-values.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex:9:From this analysis, we derive a dual-constrained adaptive $b^*$ that eliminates per-model grid search, improving over uniform at $\rho \geq 0.4$ with calibrated detectors ($\Delta{=}{-}0.020$ at $\rho{=}0.4$, $p{=}0.025$; $-$0.032 at $\rho{=}0.6$, $p{=}0.004$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex:258:Adaptive vs.\ Uniform: $\Delta{=}{-}0.032$, paired $t{=}{-}15.4$, $p{=}0.004$ (full precision; 3dp rounding yields $t{=}{-}9.95$, $p{=}0.010$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex:335:Continuations generated with Qwen3-0.6B (self-generation) using nucleus sampling ($p{=}0.95$, $T{=}0.8$), producing up to 384 tokens per continuation from a 128-token prefix prompt (512 total), targeting ${\sim}$100M synthetic tokens.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex:7:Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, paired $t{=}{-}6.2$, $p{=}0.025$) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex:92:Across three seeds at $\rho = 0.6$, adaptive $\bstar$ ($17.731 \pm 0.004$) outperforms uniform on in-distribution PPL 
…[truncated 243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-21T14:18:02.590994+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n- id: \"R8-C1\"\n  summary: \"效果规模极小（Δ=-0.020 PPL / 0.11%），无下游任务改善\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均标 critical。Table 7 下游任务均值完全相同（0.5414）。PPL 微小改进未转化为任何可测量的任务性能提升。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"N=3 seeds 统计功效不足（df=2 下 paired t-test 可靠性有限）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 同意。df=2 对 outlier 极度敏感，未做多重比较校正。seed 42 存在 checkpoint resume artifact（Appendix O）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C3\"\n  summary: \"相对 Drayson et al. (2025) 方法论新颖性不足（同一公式，仅改变 b 选择方式）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 标 critical，R1 同意。双约束中 ESS 是标准工具（Kish 1965），α_eff 阈值为经验性选择。技术深度有限。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"自我污染设定（generator=trainee）生态效度受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均指出。Cross-model transfer（Appendix N）仅单 seed 且结果 mixed。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Discussion 过于单薄（约 11 行），对分析型论文远远不够\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 标 critical，R1 在交叉中未明确回应但其 Excitement 2.5/5 暗示认同。缺少对已发表 D&R 工作影响、多生成器挑战、理论最优性等的讨论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"论文定位模糊（分析论文 vs 方法论文），双重定位削弱说服力\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 明确指出。若为方法论文，效果太小；若为分析论文，adaptive b* 的篇幅占比过高。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"Epoch-matched 比较可能引入 LR schedule confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1 指出完全控制 epoch+LR 后 D&R 反而劣于 uniform（Δ=+0.72），质疑重加权机制本身是否有正面作用。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"检测器覆盖面窄（仅 3 个检测器，2 个家族）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa）、DetectGPT 等。calibration 发现可能是检测器家族特异性的。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"α_eff 代理质量中等（r=0.70，仅解释 49% 方差）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"未讨论 51% 未解释方差的来源及对方法可靠性的影响。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"ρ=0.2 失败和 1.7B 效果减弱限制方法实用范围\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W8\"\n  summary: \"B=4 离散空间与连续理论框架的脱节\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"α_eff 仅取 5 个离散值，bisection 在 5 点上运行，与 Propositions 的连续单调性保证存在 gap。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I1\"\n  summary: \"Conclusion 过于简短（~3 行），缺乏前瞻性讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"与 Discussion 问题相关。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I2\"\n  summary: \"下游任务负面结果仅在附录，未在正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Table 7 显示下游无改善，这一重要负面结果应在正文 Discussion 中讨论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n- id: \"R8-C1\"\n  summary: \"效果规模极小（Δ=-0.020 PPL / 0.11%），无下游任务改善\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均标 critical。Table 7 下游任务均值完全相同（0.5414）。PPL 微小改进未转化为任何可测量的任务性能提升。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"N=3 seeds 统计功效不足（df=2 下 paired t-test 可靠性有限）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 同意。df=2 对 outlier 极度敏感，未做多重比较校正。seed 42 存在 checkpoint resume artifact（Appendix O）。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C3\"\n  summary: \"相对 Drayson et al. (2025) 方法论新颖性不足（同一公式，仅改变 b 选择方式）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 标 critical，R1 同意。双约束中 ESS 是标准工具（Kish 1965），α_eff 阈值为经验性选择。技术深度有限。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"自我污染设定（generator=trainee）生态效度受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均指出。Cross-model transfer（Appendix N）仅单 seed 且结果 mixed。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Discussion 过于单薄（约 11 行），对分析型论文远远不够\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 标 critical，R1 在交叉中未明确回应但其 Excitement 2.5/5 暗示认同。缺少对已发表 D&R 工作影响、多生成器挑战、理论最优性等的讨论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"论文定位模糊（分析论文 vs 方法论文），双重定位削弱说服力\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 明确指出。若为方法论文，效果太小；若为分析论文，adaptive b* 的篇幅占比过高。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"Epoch-matched 比较可能引入 LR schedule confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1 指出完全控制 epoch+LR 后 D&R 反而劣于 uniform（Δ=+0.72），质疑重加权机制本身是否有正面作用。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"检测器覆盖面窄（仅 3 个检测器，2 个家族）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa）、DetectGPT 等。calibration 发现可能是检测器家族特异性的。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"α_eff 代理质量中等（r=0.70，仅解释 49% 方差）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"未讨论 51% 未解释方差的来源及对方法可靠性的影响。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"ρ=0.2 失败和 1.7B 效果减弱限制方法实用范围\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W8\"\n  summary: \"B=4 离散空间与连续理论框架的脱节\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"α_eff 仅取 5 个离散值，bisection 在 5 点上运行，与 Propositions 的连续单调性保证存在 gap。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I1\"\n  summary: \"Conclusion 过于简短（~3 行），缺乏前瞻性讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"与 Discussion 问题相关。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I2\"\n  summary: \"下游任务负面结果仅在附录，未在正文讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Table 7 显示下游无改善，这一重要负面结果应在正文 Discussion 中讨论。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-21T14:18:02.641634+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 4506}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-21T14:19:57.788129+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 8 (Fresh)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**目标 Venue**: EMNLP 2026 via ARR May 2026\n**审稿模式**: Fresh（无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight 范式在合成污染 continued pretraining 中的有效性条件。通过 Qwen3-0.6B 在 132M FineWeb tokens（ρ=0.4, 3 seeds）上的控制实验，得出三个发现：(1) Detect-and-Remove 的 PPL 优势 >95% 归因于多 epoch 暴露（epoch confound）而非过滤质量；(2) 有效重加权同时需要检测器的高 AUC 和良好校准（低 ECE）；(3) 提出双约束自适应 b*（α_eff 质量下限 + ESS 稳定性上限），声称 Δ=-0.020 PPL 改善（p=0.025）。扩展至 ρ=0.6 和 1.7B 参数量。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 发现具有独立贡献价值 [R1, R2 共识]**\nTable 1 的 epoch-matched 对照实验揭示了 D&R 文献中未被充分讨论的混淆因素：D&R full 的 0.384 PPL 优势在控制内容 epoch 后缩小到 Δ=0.017。该发现对所有使用 D&R 的后续工作有直接指导意义。\n\n**S2. Calibration 必要性是可操作的实践指导 [R1, R2 共识]**\nTF-IDF+LR（AUC=0.94, ECE=0.048）有效而 GPT-2 PPL（AUC=0.91, ECE=0.131）失败的对比，清晰隔离了校准作为必要条件。\"区分度+校准缺一不可\"具有实用性。\n\n**S3. 理论框架设计合理 [R1]**\n双约束公式化将 convergence guarantee（Wang et al., 2026）和 importance sampling stability（Kish, 1965）统一。Proposition 1-2 的证明思路清晰。\n\n**S4. 对自身局限性诚实 [R1, R2 共识]**\n主动报告 ρ=0.2 退化、1.7B 效果减弱、checkpoint resume artifact，并提供 from-scratch seed 修正。透明度值得肯定。\n\n**S5. 附录分析全面 [R1]**\n15 个附录覆盖 grid search、阈值敏感性、constraint regime 分解、proxy 验证、cross-model transfer 等。\n\n**S6. 格式合规性完整 [R2]**\n正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 效果规模极小，无下游任务改善 [R1 N2, R2 N2 — 共识]**\n核心效果 Δ=-0.020 PPL 在 base ≈17.7 上仅为 0.11% 相对改善。Table 7（Appendix H）明确显示下游任务性能完全无差异（3-seed 均值相同 0.5414，所有差异在 ±0.01 标准误差内）。PPL 微小改进未转化为任何可测量的任务性能提升，方法的实际应用动机存疑。\n\n**C2. N=3 seeds 统计功效不足 [R1 N1, R2 同意 — 共识]**\n核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子（df=2）。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感。论文测试了多种方法 × 多个 ρ × 多个评估域 × 多个模型大小的比较，未做多重比较校正。Appendix O 揭示 seed 42 使用 checkpoint-resumed 训练，resume artifact 膨胀了表观效应。\n\n**C3. 相对 Drayson et al. (2025) 方法论新颖性不足 [R2 N1, R1 同意 — 共识]**\n论文使用与 Drayson et al. 完全相同的 weighting formula w(x)=(1−q(x))^b，核心区别仅在于 b 的选择方式。双约束中 ESS 是重要性采样文献标准工具（Kish 1965, Owen 2013），α_eff 质量下限为经验性阈值。将两个标准工具组合为自适应选择器，本质上是超参数自动调节方案，技术深度有限。\n\n### Warning（影响评分但不一票否决）\n\n**W1. 自我污染设定生态效度受限 [R1, R2 共识]**\nQwen3-0.6B 生成 + 训练创造了最有利的检测环境。真实 web 污染包含异构多源合成文本。Cross-model transfer（Appendix N, Llama-3.2-3B）仅单 seed 且结果 mixed。\n\n**W2. Discussion 过于单薄 [R2 N3]**\nSection 6 仅约 11 行。对于分析型论文，缺少对已发表 D&R 工作的影响评估、多生成器场景的 calibration 挑战、adaptive b* 的理论最优性讨论、adversarial 条件下的鲁棒性分析等。\n\n**W3. 论文定位模糊 [R2 W4, R1 隐含同意]**\n在\"分析论文\"与\"方法论文\"之间定位模糊。若为方法论文，效果太小（0.11%）且无下游改善；若为分析论文，adaptive b* 篇幅占比过高。双重定位削弱了两个维度的说服力。\n\n**W4. Epoch-matched 比较可能引入 LR schedule confound [R1 W2]**\n完全控制 epoch+LR 后，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。论文将此描述为\"warm LR from multi-epoch exposure\"，但未直面其对重加权机制核心动机的冲击。\n\n**W5. 检测器覆盖面窄 [R1 W3]**\n仅 3 个检测器来自 2 个家族。缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa）、DetectGPT/Fast-DetectGPT 等。\"calibration matters\" 发现可能是检测器家族特异性的。\n\n**W6. α_eff 代理质量中等 [R1 W4]**\nPearson r≈0.70（r²=0.49），超过一半的真实人类比例方差未被捕获。未讨论残差来源及其对方法可靠性的影响。\n\n**W7. ρ=0.2 失败 + 1.7B 效果减弱限制实用范围 [R1, R2 共识]**\n方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。ρ=0.2 退化 +0.046，1.7B OOD 部分不一致。\n\n**W8. B=4 离散空间与连续理论的脱节 [R1 W6]**\nMicro-batch B=4 时 α_eff 仅取 5 个离散值，bisection 在 5 点上运行。Propositions 的连续单调性保证与离散实现之间的 gap 未被讨论。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成共识：\n\n1. **效果规模 + 无下游改善是最核心问题** — 两人均标 critical，认为 0.11% PPL 改进且无下游 transfer 严重限制了方法论文的价值。\n2. **N=3 统计功效不足** — 两人均认为 df=2 下的 p 值不够可靠，需增加 seeds 或 bootstrap CI。\n3. **Epoch confound 是论文最有价值的发现** — 两人均肯定此发现的社区诊断价值。\n4. **Calibration 必要性有实用意义** — 两人均肯定。\n5. **自我污染场景限制了泛化声称** — 两人均认为需更多 cross-model 实验或更严格限定 scope。\n6. **论文定位需明确** — 建议明确为分析论文并降低方法贡献的 claim 强度。\n\n---\n\n## Reviewer Divergence\n\n无重大分歧。两位 Reviewer 的唯一差异在于权重分配：\n- R1 更关注统计严谨性（统计功效、α_eff 代理质量、B=4 离散化）\n- R2 更关注新颖性和叙事完整性（与 Drayson 的区分、Discussion 深度、论文定位）\n\n两者互补，无矛盾。\n\n---\n\n## Questions\n\n1. 三个 from-scratch seeds 在 adaptive vs. uniform (ρ=0.4) 下各自的逐 seed PPL 值？改善是否跨 seed 一致？\n2. Table 7 显示下游任务零改善。在无下游改善的情况下，方法的实际应用动机如何论证？\n3. 完全控制 epoch+LR 后 D&R 劣于 uniform (Δ=+0.72)。如何调和这一发现与\"重加权机制独立于 epoch 效应有贡献\"的声称？\n4. 是否考虑过异构多源污染（如混合 GPT-4+Llama+Qwen 生成文本）的实验？\n5. α_eff 与真实人类比例仅 r=0.70。剩余 51% 方差中，检测器噪声 vs. 公式系统偏差各占多少？\n6. 双约束的选择是经验性的还是有理论最优性依据？为何不考虑其他约束组合（如 KL divergence bound）？\n\n---\n\n## Missing References\n\n论文 Related Work 覆盖面较广。以下可考虑补充：\n- Mindermann et al. (2022) \"Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt\" — 已在 bib 中但可在 Instance-Level Reweighting 段落更显著地讨论其与 provenance-based reweighting 的关系。\n- 无重大遗漏被两位 Reviewer 共同指出。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（耗时约 3 分钟）\n\n**Findings**（2 warnings, 14 info）:\n- **[warning]** 第 3-6 页（Method + Experiments）4 页跨度内仅 Algorithm 1 作为 display item，主结果表格直到第 7 页才出现。审稿人在 §5.1 阅读结果讨论时看不到对应表格。建议将实验设置摘要表或关键 figure 前移。\n- **[warning]** 末页（p.16）下半部约 40% 为空白，可重排附录内容减少浪费。\n- **[info]** Figure 1（分析概览）在第 2 页顶部，若能提至第 1 页底部审稿体验更好。\n- **[info]** 正文 8 页含 2 figure + 2 table + 1 algorithm = 5 个 display items，处于可接受下限。建议从附录提升 1-2 个关键 figure 到主文。\n- **[info]** Table 1/2 使用 booktabs 风格，排版质量高。Figure 2 颜色语义清晰，色盲友好。\n- **[info]** 未发现 margin 溢出、公式渲染错误或 LaTeX 残留问题。整体排版专业。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings（可被 Findings 接收）**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉相关领域，评分完全一致）\n\n**理由**: 论文包含两个有独立价值的诊断发现（epoch confound 和 calibration 必要性），实验控制严谨，对自身局限性诚实。但存在三个 critical 问题制约主会议接收：(1) 核心方法效果极小（Δ=-0.020 PPL, 0.11%）且无下游任务改善；(2) N=3 seeds 统计支撑力有限；(3) 相对 Drayson et al. 的方法论新颖性为增量式（同一公式，仅改变超参数选择）。方法的适用范围也受限（ρ≥0.4 + 小模型 + 校准判别式检测器）。\n\n**改进建议优先级**:\n1. **明确论文定位为分析论文**：将 adaptive b* 降格为分析结论的自然推论，重心放在 F1-F3 的发现上\n2. **扩展 Discussion**：当前 11 行远远不够，至少增加 1 页讨论\n3. **增加统计可信度**：更多 seeds（≥5）或 bootstrap CI，对多重比较做 FDR 校正\n4. **正文讨论下游零改善**：将 Table 7 的负面结果从附录移至正文 Discussion\n5. **考虑 cross-model 污染实验**：至少 1-2 个异构生成器的完整实验\n\n**注**: Reviewer 1 在 Round 1 报告中声称 \"主文 §5.1 报告 p=0.025 而 Checklist §C3 报告 p=0.0425\"。经 Review Director 逐文件验证，论文全文（abstract.tex、results.tex、checklist.tex）一致报告 p=0.025，不存在 p 值矛盾。该 issue 为 Reviewer 幻觉，未纳入本报告的 Weaknesses。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 准确反映论文内容，但 \"improving over uniform at ρ≥0.4\" 的措辞在实际效果仅 0.11% 且无下游改善时可能构成 overclaim。建议加入限定语。\n\n**Introduction (§1)**: 4 个 findings 的组织逻辑清晰，Figure 1 有效传达论文结构。但从 F1-F3（分析发现）到 F4（adaptive b* 方法）的过渡缺乏足够动机——为什么分析发现自然导向这个特定的双约束设计？\n\n**Related Work (§2)**: 覆盖全面，与 Drayson et al. 的三点区分（per-batch vs per-model、loss reweighting vs SIR、lightweight detector）清晰。Domain-level vs instance-level 的区分合理。\n\n**Method (§3)**: 理论框架自洽。但 B=4 离散化问题需在正文讨论（当前仅在 §3.3 简要提及）。α_eff 作为真实人类比例代理的 r=0.70 限制应更显著地声明。\n\n**Experiments (§4)**: 设置清晰完整。自我污染设定的局限应在此处（而非仅在 §8）预告。\n\n**Results (§5)**: 实验结果呈现严谨（3 seeds、paired t-test、effect sizes）。但 Δ=-0.020 的实际意义需更多论证。Epoch confound 分析（§5.1, Table 1）是最强贡献。\n\n**Discussion (§6)**: 严重不足。11 行无法覆盖论文发现的 implications。需讨论：(a) epoch confound 对已发表 D&R 文献的影响；(b) 何时应选择 uniform 而非 reweighting；(c) 下游零改善的含义；(d) 方法的理论局限。\n\n**Conclusion (§7)**: 过于简短（~3 行），缺乏前瞻性讨论。\n\n**Limitations (§8)**: 涵盖了主要局限（单模型族、单数据域、self-contamination、ρ=0.2 失败）。长度适当（符合 EMNLP 要求的简洁 Limitations）。\n\n**Appendix**: 全面且有价值。建议将 Appendix O（checkpoint resume artifact）的关键信息移至正文 §5.1。",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 8 (Fresh)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**目标 Venue**: EMNLP 2026 via ARR May 2026\n**审稿模式**: Fresh（无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight 范式在合成污染 continued pretraining 中的有效性条件。通过 Qwen3-0.6B 在 132M FineWeb tokens（ρ=0.4, 3 seeds）上的控制实验，得出三个发现：(1) Detect-and-Remove 的 PPL 优势 >95% 归因于多 epoch 暴露（epoch confound）而非过滤质量；(2) 有效重加权同时需要检测器的高 AUC 和良好校准（低 ECE）；(3) 提出双约束自适应 b*（α_eff 质量下限 + ESS 稳定性上限），声称 Δ=-0.020 PPL 改善（p=0.025）。扩展至 ρ=0.6 和 1.7B 参数量。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 发现具有独立贡献价值 [R1, R2 共识]**\nTable 1 的 epoch-matched 对照实验揭示了 D&R 文献中未被充分讨论的混淆因素：D&R full 的 0.384 PPL 优势在控制内容 epoch 后缩小到 Δ=0.017。该发现对所有使用 D&R 的后续工作有直接指导意义。\n\n**S2. Calibration 必要性是可操作的实践指导 [R1, R2 共识]**\nTF-IDF+LR（AUC=0.94, ECE=0.048）有效而 GPT-2 PPL（AUC=0.91, ECE=0.131）失败的对比，清晰隔离了校准作为必要条件。\"区分度+校准缺一不可\"具有实用性。\n\n**S3. 理论框架设计合理 [R1]**\n双约束公式化将 convergence guarantee（Wang et al., 2026）和 importance sampling stability（Kish, 1965）统一。Proposition 1-2 的证明思路清晰。\n\n**S4. 对自身局限性诚实 [R1, R2 共识]**\n主动报告 ρ=0.2 退化、1.7B 效果减弱、checkpoint resume artifact，并提供 from-scratch seed 修正。透明度值得肯定。\n\n**S5. 附录分析全面 [R1]**\n15 个附录覆盖 grid search、阈值敏感性、constraint regime 分解、proxy 验证、cross-model transfer 等。\n\n**S6. 格式合规性完整 [R2]**\n正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 效果规模极小，无下游任务改善 [R1 N2, R2 N2 — 共识]**\n核心效果 Δ=-0.020 PPL 在 base ≈17.7 上仅为 0.11% 相对改善。Table 7（Appendix H）明确显示下游任务性能完全无差异（3-seed 均值相同 0.5414，所有差异在 ±0.01 标准误差内）。PPL 微小改进未转化为任何可测量的任务性能提升，方法的实际应用动机存疑。\n\n**C2. N=3 seeds 统计功效不足 [R1 N1, R2 同意 — 共识]**\n核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子（df=2）。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感。论文测试了多种方法 × 多个 ρ × 多个评估域 × 多个模型大小的比较，未做多重比较校正。Appendix O 揭示 seed 42 使用 checkpoint-resumed 训练，resume artifact 膨胀了表观效应。\n\n**C3. 相对 Drayson et al. (2025) 方法论新颖性不足 [R2 N1, R1 同意 — 共识]**\n论文使用与 Drayson et al. 完全相同的 weighting formula w(x)=(1−q(x))^b，核心区别仅在于 b 的选择方式。双约束中 ESS 是重要性采样文献标准工具（Kish 1965, Owen 2013），α_eff 质量下限为经验性阈值。将两个标准工具组合为自适应选择器，本质上是超参数自动调节方案，技术深度有限。\n\n### Warning（影响评分但不一票否决）\n\n**W1. 自我污染设定生态效度受限 [R1, R2 共识]**\nQwen3-0.6B 生成 + 训练创造了最有利的检测环境。真实 web 污染包含异构多源合成文本。Cross-model transfer（Appendix N, Llama-3.2-3B）仅单 seed 且结果 mixed。\n\n**W2. Discussion 过于单薄 [R2 N3]**\nSection 6 仅约 11 行。对于分析型论文，缺少对已发表 D&R 工作的影响评估、多生成器场景的 calibration 挑战、adaptive b* 的理论最优性讨论、adversarial 条件下的鲁棒性分析等。\n\n**W3. 论文定位模糊 [R2 W4, R1 隐含同意]**\n在\"分析论文\"与\"方法论文\"之间定位模糊。若为方法论文，效果太小（0.11%）且无下游改善；若为分析论文，adaptive b* 篇幅占比过高。双重定位削弱了两个维度的说服力。\n\n**W4. Epoch-matched 比较可能引入 LR schedule confound [R1 W2]**\n完全控制 epoch+LR 后，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。论文将此描述为\"warm LR from multi-epoch exposure\"，但未直面其对重加权机制核心动机的冲击。\n\n**W5. 检测器覆盖面窄 [R1 W3]**\n仅 3 个检测器来自 2 个家族。缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa）、DetectGPT/Fast-DetectGPT 等。\"calibration matters\" 发现可能是检测器家族特异性的。\n\n**W6. α_eff 代理质量中等 [R1 W4]**\nPearson r≈0.70（r²=0.49），超过一半的真实人类比例方差未被捕获。未讨论残差来源及其对方法可靠性的影响。\n\n**W7. ρ=0.2 失败 + 1.7B 效果减弱限制实用范围 [R1, R2 共识]**\n方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。ρ=0.2 退化 +0.046，1.7B OOD 部分不一致。\n\n**W8. B=4 离散空间与连续理论的脱节 [R1 W6]**\nMicro-batch B=4 时 α_eff 仅取 5 个离散值，bisection 在 5 点上运行。Propositions 的连续单调性保证与离散实现之间的 gap 未被讨论。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成共识：\n\n1. **效果规模 + 无下游改善是最核心问题** — 两人均标 critical，认为 0.11% PPL 改进且无下游 transfer 严重限制了方法论文的价值。\n2. **N=3 统计功效不足** — 两人均认为 df=2 下的 p 值不够可靠，需增加 seeds 或 bootstrap CI。\n3. **Epoch confound 是论文最有价值的发现** — 两人均肯定此发现的社区诊断价值。\n4. **Calibration 必要性有实用意义** — 两人均肯定。\n5. **自我污染场景限制了泛化声称** — 两人均认为需更多 cross-model 实验或更严格限定 scope。\n6. **论文定位需明确** — 建议明确为分析论文并降低方法贡献的 claim 强度。\n\n---\n\n## Reviewer Divergence\n\n无重大分歧。两位 Reviewer 的唯一差异在于权重分配：\n- R1 更关注统计严谨性（统计功效、α_eff 代理质量、B=4 离散化）\n- R2 更关注新颖性和叙事完整性（与 Drayson 的区分、Discussion 深度、论文定位）\n\n两者互补，无矛盾。\n\n---\n\n## Questions\n\n1. 三个 from-scratch seeds 在 adaptive vs. uniform (ρ=0.4) 下各自的逐 seed PPL 值？改善是否跨 seed 一致？\n2. Table 7 显示下游任务零改善。在无下游改善的情况下，方法的实际应用动机如何论证？\n3. 完全控制 epoch+LR 后 D&R 劣于 uniform (Δ=+0.72)。如何调和这一发现与\"重加权机制独立于 epoch 效应有贡献\"的声称？\n4. 是否考虑过异构多源污染（如混合 GPT-4+Llama+Qwen 生成文本）的实验？\n5. α_eff 与真实人类比例仅 r=0.70。剩余 51% 方差中，检测器噪声 vs. 公式系统偏差各占多少？\n6. 双约束的选择是经验性的还是有理论最优性依据？为何不考虑其他约束组合（如 KL divergence bound）？\n\n---\n\n## Missing References\n\n论文 Related Work 覆盖面较广。以下可考虑补充：\n- Mindermann et al. (2022) \"Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt\" — 已在 bib 中但可在 Instance-Level Reweighting 段落更显著地讨论其与 provenance-based reweighting 的关系。\n- 无重大遗漏被两位 Reviewer 共同指出。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（耗时约 3 分钟）\n\n**Findings**（2 warnings, 14 info）:\n- **[warning]** 第 3-6 页（Method + Experiments）4 页跨度内仅 Algorithm 1 作为 display item，主结果表格直到第 7 页才出现。审稿人在 §5.1 阅读结果讨论时看不到对应表格。建议将实验设置摘要表或关键 figure 前移。\n- **[warning]** 末页（p.16）下半部约 40% 为空白，可重排附录内容减少浪费。\n- **[info]** Figure 1（分析概览）在第 2 页顶部，若能提至第 1 页底部审稿体验更好。\n- **[info]** 正文 8 页含 2 figure + 2 table + 1 algorithm = 5 个 display items，处于可接受下限。建议从附录提升 1-2 个关键 figure 到主文。\n- **[info]** Table 1/2 使用 booktabs 风格，排版质量高。Figure 2 颜色语义清晰，色盲友好。\n- **[info]** 未发现 margin 溢出、公式渲染错误或 LaTeX 残留问题。整体排版专业。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings（可被 Findings 接收）**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉相关领域，评分完全一致）\n\n**理由**: 论文包含两个有独立价值的诊断发现（epoch confound 和 calibration 必要性），实验控制严谨，对自身局限性诚实。但存在三个 critical 问题制约主会议接收：(1) 核心方法效果极小（Δ=-0.020 PPL, 0.11%）且无下游任务改善；(2) N=3 seeds 统计支撑力有限；(3) 相对 Drayson et al. 的方法论新颖性为增量式（同一公式，仅改变超参数选择）。方法的适用范围也受限（ρ≥0.4 + 小模型 + 校准判别式检测器）。\n\n**改进建议优先级**:\n1. **明确论文定位为分析论文**：将 adaptive b* 降格为分析结论的自然推论，重心放在 F1-F3 的发现上\n2. **扩展 Discussion**：当前 11 行远远不够，至少增加 1 页讨论\n3. **增加统计可信度**：更多 seeds（≥5）或 bootstrap CI，对多重比较做 FDR 校正\n4. **正文讨论下游零改善**：将 Table 7 的负面结果从附录移至正文 Discussion\n5. **考虑 cross-model 污染实验**：至少 1-2 个异构生成器的完整实验\n\n**注**: Reviewer 1 在 Round 1 报告中声称 \"主文 §5.1 报告 p=0.025 而 Checklist §C3 报告 p=0.0425\"。经 Review Director 逐文件验证，论文全文（abstract.tex、results.tex、checklist.tex）一致报告 p=0.025，不存在 p 值矛盾。该 issue 为 Reviewer 幻觉，未纳入本报告的 Weaknesses。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 准确反映论文内容，但 \"improving over uniform at ρ≥0.4\" 的措辞在实际效果仅 0.11% 且无下游改善时可能构成 overclaim。建议加入限定语。\n\n**Introduction (§1)**: 4 个 findings 的组织逻辑清晰，Figure 1 有效传达论文结构。但从 F1-F3（分析发现）到 F4（adaptive b* 方法）的过渡缺乏足够动机——为什么分析发现自然导向这个特定的双约束设计？\n\n**Related Work (§2)**: 覆盖全面，与 Drayson et al. 的三点区分（per-batch vs per-model、loss reweighting vs SIR、lightweight detector）清晰。Domain-level vs instance-level 的区分合理。\n\n**Method (§3)**: 理论框架自洽。但 B=4 离散化问题需在正文讨论（当前仅在 §3.3 简要提及）。α_eff 作为真实人类比例代理的 r=0.70 限制应更显著地声明。\n\n**Experiments (§4)**: 设置清晰完整。自我污染设定的局限应在此处（而非仅在 §8）预告。\n\n**Results (§5)**: 实验结果呈现严谨（3 seeds、paired t-test、effect sizes）。但 Δ=-0.020 的实际意义需更多论证。Epoch confound 分析（§5.1, Table 1）是最强贡献。\n\n**Discussion (§6)**: 严重不足。11 行无法覆盖论文发现的 implications。需讨论：(a) epoch confound 对已发表 D&R 文献的影响；(b) 何时应选择 uniform 而非 reweighting；(c) 下游零改善的含义；(d) 方法的理论局限。\n\n**Conclusion (§7)**: 过于简短（~3 行），缺乏前瞻性讨论。\n\n**Limitations (§8)**: 涵盖了主要局限（单模型族、单数据域、self-contamination、ρ=0.2 失败）。长度适当（符合 EMNLP 要求的简洁 Limitations）。\n\n**Appendix**: 全面且有价值。建议将 Appendix O（checkpoint resume artifact）的关键信息移至正文 §5.1。",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-21T14:20:01.652958+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 848 · 2026-05-21T14:20:09.532668+00:00_

审稿报告已投递至 Research Director。

**Round 8 审稿完成汇报**：

- **Overall**: 3.0 — Findings（两位 Reviewer 一致）
- **3 个 Critical 问题**：效果规模极小且无下游改善、N=3 统计功效不足、相对 Drayson et al. 新颖性有限
- **8 个 Warning 问题**：自我污染场景受限、Discussion 单薄、论文定位模糊、LR confound、检测器覆盖窄、α_eff 代理质量中等、适用范围窄、B=4 离散化
- **核心建议**：重新定位为分析论文，深化 Discussion，增加统计可信度
- **Reviewer 幻觉纠正**：R1 声称的 p 值矛盾（p=0.025 vs p=0.0425）经验证不存在，已从报告中排除
- **Issue Tracker** 已同步更新（12 条 issues：3 critical, 7 warning, 2 info）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 849 · 2026-05-21T14:20:09.544553+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 相对于 Drayson et al. (2025) 的新颖性不足**

同意核心判断。论文使用与 Drayson et al. (2025) 完全相同的 weighting formula w(x) = (1−q(x))^b（§3.1, Eq. 1），差异仅在于 b 的选取从 validation-set grid search 变为双约束自适应。ESS 约束确实是重要性采样文献的标准工具（Kish, 1965; Owen, 2013），α_eff 质量下限本质上是一个阈值化的加权比例统计量。将两个标准工具组合为一个 per-batch 选择器，技术深度有限。

补充一点：论文的更大价值在于分析性发现（epoch confound 揭示、calibration 必要性），而非 adaptive b* 方法本身。但论文的叙事结构将 adaptive b* 作为三大发现之一并在 Abstract/Introduction 中突出（§1: "a dual-constrained adaptive b* that eliminates per-model grid search"），这一定位放大了 R2 指出的新颖性不足问题。如果论文重新定位为分析贡献为主、方法为辅，这一问题可以缓解。

**[AGREE] R2-N2: 效果规模极小，实用价值论证不足**

完全同意，且补充我自己的发现作为强化证据：
(a) Table 7 (Appendix H) 下游任务 3-seed 均值完全相同（0.5414），所有差异在 ±0.01 标准误差范围内。PPL 微小改善（0.11%）不转化为任何可测量的能力提升。
(b) 论文主文与 Checklist 存在 p 值矛盾——§5.1 报告 p=0.025，§C3 报告 p=0.0425（我在自己的审稿 N3 中指出）。即使取较小的 p 值，N=3 的统计功效也根本不足。
(c) ρ=0.2 退化 +0.040（§5.2）和 1.7B 效果不显著 Δ=+0.013（§5.2）进一步限制了适用范围。方法在低污染和大模型两个最实际的场景都失效，严重削弱实用价值。

**[AGREE] R2-N3: Discussion 部分过于单薄**

同意。Section 6 仅包含两个小节（"Why minimum intervention works" 和 "Practical guidance"），合计约 15 行。对于一篇声称揭示三项发现的分析型论文，这远远不够。缺失的讨论包括：
- Epoch confound 发现对现有 D&R 文献的系统性影响（哪些先前工作的结论需要重新审视？）
- 方法适用边界的系统讨论（何时用 / 何时不用 / 何时该选择其他方案）
- α_eff proxy 仅 r=0.70 的局限性及其对方法可靠性的影响（Table 9, Appendix J）
- 与 domain-level mixing 方法（DoReMi, Aioli 等，§2 Related Work 中已引用）的概念对比

不过我认为这是 should-fix 级别而非 must-fix，因为 Discussion 的厚度是写作问题，不影响技术正确性。

---

### Should-Fix 问题

**[AGREE] R2-W1: 实验场景过窄**

同意，且与我自己的 W1 一致。Self-contamination（Qwen3-0.6B 生成 + Qwen3-0.6B 训练，§4）是最简单的检测场景。Appendix N (Table 11) 的 cross-model transfer 仅单 seed、混合结果（HellaSWag 退化），不足以支撑通用性声称。

**[REBUT] R2-W2: "Minimum intervention" 概念缺乏充分动机**

部分不同意。论文实际上提供了两层动机：

(a) **理论层面**: §3.2 明确解释 ESS 稳定性约束防止梯度退化——"Overly concentrated weights yield high-variance gradients; η_min prevents the batch from degenerating into a single effective sample." 这是重要性采样中 well-established 的 ESS 下界动机。

(b) **经验层面**: Figure 2 (p.8) 展示了 b* 过大时 PPL 进入 "degradation zone"（b > ~1.5 时 PPL 开始快速上升）。§5.3 的超参数敏感性分析显示 τ=0.7 优于 τ=0.8（更激进的下权），且 τ > 0.8 导致 b* 快速增长（mean b* = 3.08 at τ=0.9）和 PPL 退化。§6 还通过 Random reweighting 对照（PPL 17,861）确认 detector signal 是 "load-bearing" 的，即仅有正确方向的适度干预才有效。

R2 的合理之处在于：论文确实没有从信息论或优化理论角度给出 *为什么恰好最小干预是最优的* 的深层解释，现有动机更多是经验观察。但说"未解释为什么过度降权有害"并不准确——ESS 退化和 Figure 2 的 degradation zone 已经回答了这个问题。

**[AGREE] R2-W3: Conclusion 过于简短**

同意。§7 约 8-10 行，仅为三个发现的复述加 code/data 承诺，缺乏前瞻性讨论（如：对 recursive training 的长期影响、与 data provenance 标注标准化的关系、方法扩展到 instruction tuning 场景的可能性等）。不过这在严重程度上低于 Discussion 单薄（N3），属于写作层面的改善空间。

**[AGREE] R2-W4: "分析论文" 与 "方法论文" 定位模糊**

同意，且这是论文结构性问题的根源。具体证据：

- **标题和研究问题（§1）** 框定为分析："When Does Detect-and-Reweight Work?" → 期望是系统性分析
- **Abstract 和 Contribution** 同时强调方法贡献："a dual-constrained adaptive b* that eliminates per-model grid search" → 期望是方法创新
- **实验评估** 以 PPL/下游比较为主（§5, Table 2），这是方法论文的评估模式

双重定位的问题正如 R2 所说，两个维度都被削弱：
- 作为分析论文：epoch confound 和 calibration 发现有价值，但正文空间被方法描述（§3 约 2.5 页）占据，分析深度不足（Discussion 仅 15 行）
- 作为方法论文：效果仅 Δ=-0.020 PPL、无下游改善、适用范围受限

建议作者明确选择分析性定位，将 adaptive b* 降格为分析发现的自然延伸而非独立贡献。

**[AGREE] R2-W5: 下游任务评估不足**

同意。Table 7 (Appendix H) 的负面结果——PPL 改善完全不转化为下游任务改善——是论文实用价值评估中最重要的数据之一，但仅放在附录中。主文 §5 和 §6 均未讨论这一结果。对于声称 "practical adaptive method" 的论文，将核心实用性的负面证据隐藏在附录中是一个叙事诚信问题。

补充：即便 0.6B 模型可能因 benchmark saturation/floor effects 难以体现差异，论文也应在主文中讨论这一可能性并论证为什么 PPL 仍然是有意义的评估指标。

---

### 总结

与 R2 的 8 条意见中，我对 7 条 [AGREE]（N1, N2, N3, W1, W3, W4, W5），对 1 条 [REBUT]（W2: minimum intervention 动机）。

两位 Reviewer 的核心关切高度一致：N=3 统计功效不足、效果规模微小且无下游改善、适用范围受限。我与 R2 的主要分歧在于：R2 更强调新颖性不足（N1），而我更强调统计严谨性（N=3、p 值矛盾）。两个视角互补——即使方法足够新颖，统计支撑也不足；即使统计上 solid，新颖性也有限。

Overall 评分我维持 **3.0 (Findings)**，与 R2 一致。Epoch confound 发现和 calibration 必要性是 Findings 级别的贡献；adaptive b* 方法在当前证据下不支持主会议接收。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 8 条意见中 7 条 [AGREE]、1 条 [REBUT]（W2: minimum intervention 动机——论文通过 ESS 退化论证和 Figure 2 degradation zone 提供了合理解释）。两位 Reviewer 核心关切一致：N=3 统计功效不足、效果微小无下游改善、适用范围受限。Overall 维持 3.0 (Findings)。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: N=3 seeds 统计功效不足**

同意这是本文最根本的统计问题之一。我在自己的审稿中将效果规模问题列为 N2（critical），核心论点一致：

1. **df=2 的 paired t-test 极度脆弱**：R1 正确指出 t-test 在 df=2 时对 outlier 和非正态性极端敏感。事实上，任何单个 seed 的异常值都可以翻转统计结论。
2. **多重比较未校正**：论文测试了多种方法 × 多个 ρ × 多个评估域的组合，p=0.025 在 Bonferroni 校正后远不显著。
3. **Appendix O 的 seed 42 artifact**：R1 敏锐地发现 seed 42 使用了 checkpoint-resumed 训练。Appendix O 揭示这会引入 "distribution matching" 的虚假 finding。这意味着 3 个 seed 中有 1 个的实验条件与其他 2 个不完全一致，进一步削弱了 N=3 的可信度。

补充：不过我注意到 3 seeds 在 NLP 训练实验中仍是常见做法（受 GPU 计算成本约束），论文也报告了方向性一致。问题不是"3 seeds 不可接受"，而是在效果规模仅 0.11% 时，3 seeds 不足以区分真实效果和噪声。如果效果是 Δ=-0.5 PPL，3 seeds 可能足够；但 Δ=-0.020 时绝对不够。

---

**[AGREE] R1-N2: Δ=-0.020 无下游任务改善**

完全同意，这也是我的 N2 核心论点。补充几个 R1 未强调的细节：

1. **Appendix H Table 7 的负面结果**极具说服力：adaptive 的三 seed 均值为 0.5414，uniform 也是相近水平，|Δ| ≤ 0.01 且在标准误差内。这意味着 PPL 的微小改进零转化为下游能力——reweighting 可能仅在改善 loss landscape 的某个局部指标，而非模型的实际能力。
2. **ρ=0.2 的 +0.040 退化**（Appendix M）意味着方法在低污染场景反而有害。实际应用中，用户往往不知道真实 ρ 值，盲目应用 adaptive b* 可能损害模型。

我在自己的审稿中建议作者重新定位为"负面结果 + 诊断分析"论文——即核心贡献不是 adaptive b*，而是"D&R 的效果被严重高估"这一发现本身。这样 Δ=-0.020 的小效果反而成为支持论点的证据。

---

**[AGREE] R1-N3: 主文与 Checklist 的 p 值矛盾**

同意这是一个严重的科学严谨性问题。

- Section 5.1 报告 adaptive vs. uniform 在 ρ=0.4 时 p=0.025
- Checklist C3 报告同一比较 p=0.0425

两个数字无法通过 one-tailed vs. two-tailed 解释（one-tailed 0.025 → two-tailed 0.050，不是 0.0425）。最可能的解释是：(a) 其中一个计算有误；(b) 两处使用了不同的比较基准但未说明；(c) 修改过程中未同步更新。无论哪种情况，核心统计声称存在未解决的矛盾，这在审稿中不可接受。

我的审稿中未单独列出此问题（这是 R1 独立发现的），但我认为这属于 critical 级别——如果连 p 值的一致性都无法保证，论文的整体可信度受到质疑。

---

### Should-Fix 问题

**[AGREE] R1-W1: 自我污染是简化场景**

同意，这与我的 W1 一致。Self-contamination（Qwen3-0.6B 生成 + Qwen3-0.6B 训练）创造了检测器最有利的条件——同模型族的输出在分布上最容易被区分。Appendix N 的 cross-model 实验（Llama-3.2-3B → Qwen）仅单 seed 且结论为 "mixed results"，实际上承认了方法在更现实场景下的有效性未验证。

补充：R1 点出了一个我未强调的角度——self-contamination 不仅使检测更容易，还使得 calibration 更容易满足（Section 4 报告 ECE=0.05），因为训练和生成来自同一分布族。在 cross-model 场景中，ECE 可能显著退化，而论文的 F2（calibration 必要性）恰恰说明这会导致方法失败。

---

**[AGREE] R1-W2: 完全控制混淆后 D&R 过滤有害**

同意这是一个重要发现，论文自身在 Section 5.1 也承认了：epoch-matched + LR-matched 下，D&R filtering (PPL=18.78) 劣于 uniform (18.06, Δ=+0.72)。

R1 的推论值得认真考虑：如果 hard filtering 在公平对比下有害，那么 adaptive soft reweighting 的改善来源就需要仔细拆解。可能的来源包括：
1. **Soft reweighting 本身**——温和降权保留了合成数据中的部分有用信息
2. **LR schedule 交互**——adaptive 方法使用完整 6,103 步训练（vs. epoch-matched 的 2,533 步），享有更完整的学习率衰减
3. **有效 epoch 效应的残余**——soft reweighting 仍然让人类数据的有效权重更高

论文未拆解这三种因素的相对贡献。我认为这是 W2 级别（should-fix）而非 critical，因为 soft reweighting ≠ hard filtering，两者的机制不同。但 R1 的质疑迫使作者需要更严格地论证 adaptive 方法的改善确实来自智能重加权。

---

**[AGREE] R1-W3: 检测器覆盖窄**

同意。论文使用 3 个检测器：TF-IDF+LR（主要）、GPT-2 perplexity scorer、N-gram（Section 5.1, Appendix K）。这些都是相对简单的方法，缺少：
- Fine-tuned neural classifiers（RoBERTa/DeBERTa-based），这是 MGT detection 领域的主流方法
- Zero-shot 方法如 DetectGPT/Fast-DetectGPT（论文在 Related Work Section 2 引用了但未在实验中使用）

这特别影响 F2（"both AUC and calibration required"）的普适性——如果只测了 2 个家族（bag-of-words 和 perplexity-based），关于检测器要求的发现可能不适用于 neural classifiers。

---

**[REBUT] R1-W4: α_eff 代理 r=0.70 解释 49% 方差**

部分反驳。R1 的 R²=0.49 计算正确，但对 α_eff 的角色存在误读：

1. **α_eff 不需要完美追踪真实比例**。论文在 Section 3.2 和 Appendix J（Table 9）明确说明 α_eff 是 σ_adj 的 proxy，用于设置保守约束（quality floor）而非精确估计。约束只需要单调性——当 α_eff 增大时真实比例也增大——而 r=0.70 足以保证这一点。
2. **保守偏差是 by design**。论文在 Section 3.2 提到 α_eff "slightly underestimates the true real fraction, biasing the method toward conservative (less aggressive) intervention"。这意味着 α_eff 的不完美恰好导致 minimum intervention——方法在不确定时倾向于少干预，这与论文的 F3 一致。
3. **然而**，r=0.70 确实意味着约一半的方差未被解释，这在极端情况下可能导致约束失效。R1 的担忧在 ρ=0.2（低信噪比）时确实成立——论文也承认此时方法失败。

所以我部分同意：r=0.70 对于保守约束的设计目的是可接受的，但 R1 正确指出这限制了方法在低污染场景的适用性。这不是一个独立的 should-fix，而是 ρ=0.2 失败的根因之一。

---

**[AGREE] R1-W5: ρ=0.2 失败和 1.7B 分析不充分**

同意，这与我的审稿中的关注一致。Appendix M 对 ρ=0.2 失败的分析仅 1 段（"detector's mean σ-score at this contamination level is 0.393"），未深入探讨：
- 是否存在一个 ρ 的临界阈值，低于该阈值方法系统性失败？
- 1.7B 效果减弱是因为更大模型对污染更鲁棒，还是因为 reweighting 在更大模型上的信号更弱？

论文在 Limitations（p.9）简要提及了这些局限，但对一篇分析型论文来说，这些应该是正文讨论的核心内容。

---

**[REBUT] R1-W6: B=4 离散空间上的 bisection 与连续理论脱节**

反驳。R1 的分析存在技术误解：

1. **Bisection 的搜索变量是 b（连续），不是 α_eff**。Algorithm 1（p.5）对 b ∈ [0, b_max] 做 bisection，寻找满足双约束的 b*。b 是连续实数，bisection 在此搜索空间上完全合法。
2. **α_eff 不限于 5 个离散值**。R1 假设 B=4 micro-batch 中 α_eff 只取 {0, 0.25, 0.5, 0.75, 1.0}。但 α_eff = Σ w_i·r_i / Σ w_i（Section 3.2），其中 w_i = (1−q(x_i))^b 是连续权重。即使 r_i ∈ {0,1} 是二值的，不同 b 值产生不同的 w_i 组合，使得 α_eff 在给定 batch composition 下是 b 的连续函数。
3. **ESS 也是连续的**。ESS(b) = (Σw_i)² / Σw_i²（Section 3.2），同样是 b 的连续函数。

因此 bisection 在技术上是合理的。不过 R1 的直觉有一个合理的子点：B=4 的小 batch 确实引入了 α_eff 的高方差（论文在 Section 3.3 提到使用 H=16 after gradient accumulation），但这是 batch size 的一般性问题，不是 bisection 方法的问题。

---

### 总结

| R1 问题 | 我的回应 | 理由 |
|---------|---------|------|
| N1 (N=3 统计) | [AGREE] | 效果 0.11% + df=2 + 无多重校正 + seed 42 artifact |
| N2 (效果微小) | [AGREE] | 与我的 N2 一致，下游零改善是致命伤 |
| N3 (p 值矛盾) | [AGREE] | 科学严谨性问题，无法用 one/two-tailed 解释 |
| W1 (self-contamination) | [AGREE] | 与我的 W1 一致 |
| W2 (filtering 有害) | [AGREE] | 重要发现，但需区分 soft reweighting vs. LR 交互 |
| W3 (检测器窄) | [AGREE] | 缺 neural classifiers 和 zero-shot methods |
| W4 (α_eff 代理) | [REBUT] | r=0.70 对保守约束足够，但限制低 ρ 适用性 |
| W5 (ρ=0.2/1.7B) | [AGREE] | 分析不够深入 |
| W6 (B=4 bisection) | [REBUT] | bisection 搜索 b（连续），α_eff 是 b 的连续函数 |

**综合意见**：R1 和我的审稿在核心判断上高度一致——论文的诊断贡献有价值，但方法贡献受限于统计功效不足、效果微小、场景过窄。R1 额外发现的 p 值矛盾（N3）进一步强化了我对论文严谨性的担忧。我维持 Overall 3.0（Findings）的评分。

R1 的审稿在统计方法论批评上比我更深入（特别是 N1 的 df=2 分析、N3 的 p 值矛盾、W6 的离散空间讨论），我的审稿在新颖性和写作质量评估上更详细（N1 Drayson 增量性、N3 Discussion 单薄、W4 论文定位模糊）。两份审稿互补性较强。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。核心判断：

- **9 条中 7 条 [AGREE]**：N1-N3（统计功效、效果微小、p值矛盾）+ W1-W3, W5（self-contamination、filtering有害、检测器窄、分析不足）
- **2 条 [REBUT]**：W4（α_eff r=0.70 对保守约束设计目的足够）和 W6（bisection 搜索的是连续变量 b，不是离散的 α_eff）

R1 额外发现的 p 值矛盾（§5.1 p=0.025 vs. Checklist C3 p=0.0425）是我审稿中遗漏的重要问题，进一步强化了统计可信度的担忧。两份审稿在核心评分（Overall 3.0 Findings）上一致，侧重互补——R1 在统计方法论上更深入，我在新颖性和写作质量上更详细。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 850 · 2026-05-21T14:20:53.518470+00:00_

交叉回应已全部收齐。审稿报告已在此前投递，现确认交叉分享结果与报告结论一致。

**交叉分享收敛总结**：

| 议题 | R1→R2 | R2→R1 | 结论 |
|------|-------|-------|------|
| 效果规模微小/无下游改善 | AGREE | AGREE | **共识（critical）** |
| N=3 统计功效不足 | AGREE | AGREE | **共识（critical）** |
| 新颖性不足 (vs Drayson) | AGREE | — | **共识（critical）** |
| p 值矛盾 | — | AGREE | **Review Director 验证：不存在（R1 幻觉）** |
| Self-contamination 过窄 | AGREE | AGREE | **共识（warning）** |
| Discussion 单薄 | AGREE | — | **共识（warning）** |
| D&R filtering 控制后有害 | — | AGREE | **共识（warning）** |
| 检测器覆盖窄 | — | AGREE | **共识（warning）** |
| Minimum intervention 动机 | **REBUT** | — | R1 正确指出 ESS 退化+Fig 2 已提供动机 |
| α_eff 代理 r=0.70 | — | **REBUT** | R2 正确指出保守约束设计目的下 r=0.70 可接受 |
| B=4 bisection 离散性 | — | **REBUT** | R2 正确指出 bisection 搜索的是连续变量 b |

**3 条 REBUT 的处理**：
- R1 对 R2-W2（minimum intervention 动机）：合理反驳，论文确实通过 ESS 退化和 Figure 2 degradation zone 提供了经验动机。已在报告中降低此 issue 权重。
- R2 对 R1-W4（α_eff 代理质量）：部分反驳有效——r=0.70 对保守约束设计目的可接受，但确实限制低 ρ 适用性。报告中已保留为 W6（warning 级）。
- R2 对 R1-W6（B=4 bisection）：技术反驳正确——bisection 搜索的是连续变量 b，α_eff(b) 是 b 的连续函数。报告中已保留为 W8（warning 级），措辞为"离散空间与连续理论的脱节"而非 bisection 本身有误。

**关于 p 值矛盾**：R2 在交叉中同意了 R1 的 N3（p 值矛盾），但 Review Director 已逐文件验证论文全文一致报告 p=0.025。该 issue 为 R1 幻觉且传染给 R2，已在报告中明确标注排除。

审稿报告已投递，Overall 3.0 (Findings)，两位 Reviewer 完全一致。圆桌审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 63

## Round 63

78 recorded events


### User

_source line 851 · 2026-05-22T16:51:40.080217+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-22T16:51:46.149101+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-22T16:51:46.200188+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-22T16:51:52.724637+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-22T16:51:52.725033+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-22T16:51:56.151173+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-22T16:51:56.201804+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-22T16:52:00.365592+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-22T16:52:00.365967+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-22T16:52:07.196047+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-22T16:52:07.999361+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (238 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- detect_remove_q05_seed42: Detect-and-remove baseline: hard filtering removes samples with TF-IDF q_score < 0.5. If adaptive reweighting (PPL=17.674) outperforms hard removal, it demonstrates that soft scoring preserves useful signal from partially contaminated samples that hard thresholding discards.（准备中）\n- eval_adaptive_1_7b_seed123（准备中）\n- eval_uniform_1_7b_seed123（准备中）\n- detect_remove_q05_epoch_matched（准备中）\n- detect_remove_q07_seed42_r2（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- eval_uniform_1_7b_v2（准备中）\n- …另有 7 项\n\n## 近期结论\n- **bs8_nmin4_uniform_seed42** (success): Batch-size sensitivity B=8 uniform baseline: uniform weighting with effective batch=16 (bs=8 × grad_accum=2). Paired with bs8_nmin4_adaptive_seed42 to measure Δ(adaptive−uniform) at B=8. Expected: B=4 Δ=−0.020, B=8 Δ should be intermediate, B=16 Δ=−0.068. Monotonic trend confirms batch-size amplification mechanism.\n- **bs8_nmin4_adaptive_seed42** (success): Batch-size sensitivity B=8: adaptive reweighting with tau=0.7, n_min=4 (⌊B/2⌋), effective batch=16 (bs=8 × grad_accum=2). Tests whether adaptive advantage s
…[truncated 1798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-22T16:52:08.552087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-22T16:52:09.556409+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	
32	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
33	
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\begin{abstract}
40	\input{sections/abstract}
41	\end{abstract}
42	
43	\section{Introduction}
44	\label{sec:intro}
45	\input{sections/introduction}
46	
47	\section{Related Work}
48	\label{sec:related}
49	\input{sections/related_work}
50	
51	\section{Method}
52	\label{sec:method}
53	\input{sections/method}
54	
55	\section{Experimental Setup}
56	\label{sec:experiments}
57	\input{sections/experiments}
58	
59	\section{Results}
60	\label{sec:results}
61	\input{sections/results}
62	
63	\section{Discussion}
64	\label{sec:discussion}
65	\input{sections/discussion}
66	
67	\section{Conclusion}
68	\label{sec:conclusion}
69	\input{sections/conclusion}
70	
71	\section*{Limitations}
72	\label{sec:limitations}
73	\input{sections/limitations}
74	
75	\section*{Ethics Statement}
76	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
77	
78	\input{sections/checklist}
79	
8
…[truncated 99 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-22T16:52:09.707463+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-22T16:52:09.758052+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-22T16:52:14.926761+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

Based on the search results, I found relevant information about EMNLP 2026 and ARR submiss
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5219
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-22T16:52:14.977506+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5219
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-22T16:52:21.006768+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 869 · 2026-05-22T16:52:21.107496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 submission guidelines author instructions page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 submission guidelines author instructions page limit anonymity"
  }
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-22T16:52:22.613028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-22T16:52:23.416318+00:00_

1	issues:
2	- id: "R8-C1"
3	  summary: "效果规模极小（Δ=-0.020 PPL / 0.11%），无下游任务改善"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 8
8	  last_seen_round: 9
9	  mentions:
10	    - round: 8
11	      reviewers: [1, 2]
12	      note: "两位 Reviewer 均标 critical。Table 7 下游任务均值完全相同（0.5414）。PPL 微小改进未转化为任何可测量的任务性能提升。"
13	    - round: 9
14	      reviewers: [1, 2]
15	      note: "仍为 critical。Round 9 reframe 为 analysis paper 后效果规模问题仍存在——分析论文需要解释 WHY 效果小，而非回避。Table 7 下游零改善需进入正文 Discussion。"
16	  action_items:
17	    - round: 9
18	      action: "Discussion 扩展：加入 downstream 零改善分析段落 + Table 引入正文 + narrow residual framing"
19	      assigned_to: paper_agent
20	      status: completed
21	  resolution: "Discussion 已包含 downstream 零改善分析段落、Table 3 在正文、narrow residual framing 解释。Paper Agent Round 9 reframe 完成。"
22	  resolution_round: 10
23	
24	- id: "R8-C2"
25	  summary: "N=3 seeds 统计功效不足（df=2 下 paired t-test 可靠性有限）"
26	  category: experiment
27	  severity: critical
28	  status: resolved
29	  first_raised_round: 8
30	  last_seen_round: 9
31	  mentions:
32	    - round: 8
33	      reviewers: [1, 2]
34	      note: "R1 标 critical，R2 同意。df=2 对 outlier 极度敏感，未做多重比较校正。seed 42 存在 checkpoint resume artifact（Appendix O）。"
35	    - round: 9
36	      reviewers: [1, 2]
37	      note: "仍为 critical。Bootstrap CI 可部分缓解但不解决根本问题。Analysis paper framing 下，N=3 的统计局限需在 Limitations 诚实承认。"
38	  action_items:
39	    - round: 9
40	      action: "Agent 从现有 3-seed 数据计算 bootstrap CI（BCa 法），加入关键表格"
41	      assigned_to: main_agent
42	      status: completed
43	    - round: 9
44	      action: "Limitations 中明确承认 N=3 的统计功效限制"
45	      assigned_to: paper_agent
46	      status: completed
47	  resolution: "Limitations 新增 N=3 seeds 统计功效限制承认。Bootstrap CI 已在关键表格中。关键发现正在升级到 3-seed（seed456 系列运行中）。"
48	  resolution_round: 10
49	
50	- id: "R8-C3"
51	  summary: "相对 Drayson et al. (2025) 方法论新颖性不足（同一公式，仅改变 b 选择方式）"
52	  category: framing
53	  severity: critical
54	  status: resolved
55	  first_raise
…[truncated 8663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-22T16:52:23.567368+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-22T16:52:23.718373+00:00_

-rw-r--r-- 1 ubuntu ubuntu 470925 May 22 16:48 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-22T16:52:26.127002+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here is the information about EMNLP 2026 call for papers:

## Submission Deadline

The EMNLP 2026 paper submission deadline is May 25, 2026, 23:59:59 (UTC-12). All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to addres
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5120
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-22T16:52:27.282140+00:00_

Web search results for query: "ARR 2026 submission guidelines author instructions page limit anonymity"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on the web search results, here are the key ARR 2026 submission guidelines regarding author instructions, page limits, and anonymity:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices.

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

## Anonymity Period Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, the new policy incentivizes anonymous submissions by special paper awards and priority
…[truncated 378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6174
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-22T16:52:35.161590+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements for EMNLP 2026 main conference papers: 1) Submission deadlines (all dates), 2) Page limits for long and short papers (main text, references, appendix), 3) Template/style file requirements, 4) Anonymity/blind review policy, 5) Appendix rules (allowed? reviewed?), 6) Citation/reference format, 7) Any special formatting rules, 8) Topics of interest, 9) Commitment deadline. Be comprehensive and exact."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements for EMNLP 2026 main conference papers: 1) Submission deadlines (all dates), 2) Page limits for long and short papers (main text, references, appendix), 3) Template/style file requirements, 4) Anonymity/blind review policy, 5) Appendix rules (allowed? reviewed?), 6) Citation/reference format, 7) Any special formatting rules, 8) Topics of interest, 9) Commitment deadline. Be comprehensive and exact."
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-22T16:52:44.546699+00:00_

# EMNLP 2026 Main Conference Paper Submission Requirements

## 1) Submission Deadlines
- **ARR submission deadline:** May 25, 2026
- **Reviewer registration deadline:** May 27, 2026
- **Author response/discussion period:** July 7-13, 2026
- **Meta review release:** July 30, 2026
- **EMNLP commitment deadline:** August 2, 2026
- **Acceptance notification:** August 20, 2026
- **Camera-ready deadline:** September 20, 2026
- **Main Conference:** October 24-29, 2026

*Note: All deadlines are "11:59PM UTC-12:00 ('anywhere on Earth')"*

## 2) Page Limits
- **Long papers:** 8 pages (main text)
- **Short papers:** 4 pages (main text)
- **Final versions:** One additional content page allowed (9 pages for long, 5 for short)

## 3) Template/Style Requirements
The document references "ARR submission requirements" but does not specify template details directly. It states to follow all requirements at the ARR CFP link, including "Paper Submission and Templates."

## 4) Anonymity/Blind Review Policy
The process is described as "double-blind": "Reviewers will not see authors, nor will authors see reviewers." However, per ACL policy, "there is no anonymity period requirement."

## 5) Appendix Rules
"Optional Supplementary Materials" are permitted, referenced as appendices, software, and data, but specific review policies aren't detailed in this document.

## 6) Citation/Reference Format
Not specified in this document; directed to ARR CFP "Citation and Comparison" section.

## 7) Special Formatting Rules
No special formatting rules are detailed beyond standard ARR requirements.

## 8) Topics of Interest
Comprehensive list includes: Clinical/Biomedical Applications, NLP and Code Models, Computational Social Science, Dialogue Systems, Discourse, Efficient Methods, Ethics/Bias/Fairness, Generation, Information Extraction/Retrieval, Interpretability, Language Modeling, LLM Agents, Machine Translation, Multilingualism, Multimodality, Question Answering, Resources/Evaluation, Semantics, Sen
…[truncated 283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebFetch",
  "elapsed_ms": 9385
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-22T16:52:50.745372+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract: 1) Exact paper template (ACL style files version, download link), 2) Citation format requirements, 3) Supplementary materials / appendix policy (reviewed or not?), 4) Responsible NLP checklist requirement, 5) Any other formatting constraints (font size, margins, anonymity markers). Be exact and comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract: 1) Exact paper template (ACL style files version, download link), 2) Citation format requirements, 3) Supplementary materials / appendix policy (reviewed or not?), 4) Responsible NLP checklist requirement, 5) Any other formatting constraints (font size, margins, anonymity markers). Be exact and comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-22T16:52:52.100964+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10 && python3 -c \"\nimport yaml\nwith open('projects/provenance_weight_training/agent/config.yaml') as f:\n    cfg = yaml.safe_load(f)\next = cfg.get('external_review', {})\nprint('external_review config:', ext)\n\" 2>/dev/null || echo \"NO_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10 && python3 -c \"\nimport yaml\nwith open('projects/provenance_weight_training/agent/config.yaml') as f:\n    cfg = yaml.safe_load(f)\next = cfg.get('external_review', {})\nprint('external_review config:', ext)\n\" 2>/dev/null || echo \"NO_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 880 · 2026-05-22T16:52:57.537282+00:00_

# ACL Rolling Review Submission Requirements

## 1) Paper Template & Style Files
**Version**: Official ACL style files
**Location**: "available [here](https://github.com/acl-org/acl-style-files)"
**Key requirement**: "Authors may not modify these style files or use template designed for other conferences"
**Formatting guide**: Authors must follow guidelines at acl-org.github.io/ACLPUB/formatting.html

## 2) Citation Format Requirements
**For concurrent/overlapping work**: "Anonymous (2026). Paper title. Under review."
**General standard**: Authors must cite all relevant refereed publications and may be excused for missing unpublished work. Papers appearing less than 3 months before the deadline are considered contemporaneous and do not require detailed comparisons.

## 3) Supplementary Materials & Appendix Policy
**Reviewer obligation**: "Reviewers are not required to consider material in appendices"
**Critical content placement**: If pseudo-code, derivations, or technical specifications are essential for assessing novelty or correctness, they must appear in the main paper, not appendices
**Format requirement**: Appendices must follow double-column format with limited exceptions
**Desk rejection risk**: Using appendices to circumvent page limits risks rejection
**Anonymization**: All supplementary materials must be fully anonymized; cloud service links (Dropbox, Google Drive) are prohibited

## 4) Responsible NLP Checklist
**Requirement**: Mandatory completion during submission
**Consequence of violation**: "Incorrect, incomplete or misleading information in the checklist can result in desk rejection"
**Timing**: "Metadata fields...will remain editable for 48 hours after each submission deadline"

## 5) Additional Formatting Constraints
- **Page limits**: Long papers (8 pages), short papers (4 pages) of content
- **Font/margins**: "Submissions that do not conform to required styles, including paper size, margin width, and font size restrictions, will be rejected wit
…[truncated 271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebFetch",
  "elapsed_ms": 6791
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-22T16:52:57.738469+00:00_

NO_CONFIG
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.claude/sessions/review_director_5d592d28

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 5637
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-22T16:53:00.700622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
  "description": "List config files in agent dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "List config files in agent dir"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-22T16:53:01.253587+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-22T16:53:04.164581+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-22T16:53:04.215212+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-22T16:53:07.274022+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find yaml config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find yaml config files"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-22T16:53:07.335488+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 61
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T16:53:11.550758+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_10/workspace.yaml') as f:\n    cfg = yaml.safe_load(f)\nprojects = cfg.get('projects', {})\npwt = projects.get('provenance_weight_training', {})\next = pwt.get('external_review', {})\nprint('external_review:', ext)\nprint('---')\nprint('full project config keys:', list(pwt.keys()) if isinstance(pwt, dict) else pwt)\n\"",
  "description": "Check project external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_10/workspace.yaml') as f:\n    cfg = yaml.safe_load(f)\nprojects = cfg.get('projects', {})\npwt = projects.get('provenance_weight_training', {})\next = pwt.get('external_review', {})\nprint('external_review:', ext)\nprint('---')\nprint('full project config keys:', list(pwt.keys()) if isinstance(pwt, dict) else pwt)\n\"",
    "description": "Check project external review config"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-22T16:53:11.651761+00:00_

external_review: {}
---
full project config keys: []

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-22T16:53:16.021990+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_10/workspace.yaml') as f:\n    cfg = yaml.safe_load(f)\n# Look for provenance_weight_training anywhere\nimport json\nprint(json.dumps(cfg, indent=2, default=str)[:3000])\n\"",
  "description": "Print workspace config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_10/workspace.yaml') as f:\n    cfg = yaml.safe_load(f)\n# Look for provenance_weight_training anywhere\nimport json\nprint(json.dumps(cfg, indent=2, default=str)[:3000])\n\"",
    "description": "Print workspace config"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-22T16:53:16.122797+00:00_

{
  "projects": {}
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T16:53:19.385034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/backend.yaml 2>/dev/null | head -40",
  "description": "Check backend config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/backend.yaml 2>/dev/null | head -40",
    "description": "Check backend config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T16:53:19.436247+00:00_

manager:
  enabled: true
  url: http://172.31.31.59:8700
  my_id: be-idea-gen-0509-10
  my_token: 22a929c02f4f3c382edbeb291d23dc8b5a651a03be81b5859895774da7d9b9c4
  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
  api:
    listen_host: 0.0.0.0
    listen_port: 8420
    allowed_source_cidrs:
    - 10.0.0.0/8
    - 192.168.0.0/16
    - 172.16.0.0/12
    - 127.0.0.0/8
  capabilities:
    read: true
    bootstrap_project: true
    archive_project: true
    allocate_gpus: true
    release_gpus: true
    read_chat_history: true
    claude_account_login: true
    read_claude_pool: true
  local_approvals:
    bootstrap_project: false
    archive_project: false
    allocate_gpus: false
  heartbeat:
    enabled: true
    interval_sec: 60

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-22T16:53:26.010031+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-22T16:53:26.060583+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-22T16:53:29.121986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-22T16:53:29.473705+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled experiments (Qwen3-0.6B continued pretraining, 132M FineWeb tokens, 3 seeds), we analyze when, why, and how detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of published gains (relative to adaptive reweighting) reflect data repetition rather than filtering quality.
6	Second, effective reweighting requires both sufficient discrimination and good calibration from the detector; a high-AUC but poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform, while a lightweight calibrated alternative (ECE\,=\,0.048) succeeds (3 detectors, 3 seeds).
7	Third, mechanism decomposition reveals that minimum intervention outperforms unconstrained maximization: an $\alpha_{\mathrm{eff}}$ quality constraint binds in 38\% of batches at $4.9{\times}$ lower sharpening exponents than a stability-only strategy.
8	
9	From this analysis, we derive a dual-constrained adaptive $b^*$ that eliminates per-model grid search, improving over uniform at $\rho \geq 0.4$ with calibrated detectors ($\Delta{=}{-}0.020$ at $\rho{=}0.4$, $p{=}0.025$; $-$0.032 at $\rho{=}0.6$, $p{=}0.004$).
10	The method fails at $\rho{=}0.2$ and shows diminished benefit at 1.7B; with $N{=}3$, paired comparisons reach significance though sample size limits generalizability.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-22T16:53:29.624688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-22T16:53:29.926326+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters.
11	Our scope is continued pretraining with self-generated contamination; generalization to web scale, multi-source contamination, or other model families is untested (\S\ref{sec:limitations}).
12	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
13	
14	Our analysis yields four findings:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{Epoch confound.}
17	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering qual
…[truncated 2673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-22T16:53:29.926780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-22T16:53:30.479147+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; Min-$k$\% Prob~\
…[truncated 5897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-22T16:53:30.479521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-22T16:53:31.383107+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
5	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as
6	\begin{equation}
7	  w(x) = (1 - q(x))^{b},
8	  \label{eq:weight}
9	\end{equation}
10	where $b \geq 0$ is a sharpening exponent: $b = 0$ recovers uniform training, while larger $b$ suppresses high-$q$ samples.
11	\citet{drayson2025detection} select $b$ via validation-set grid search ($b{=}10$ for ${\leq}360$M, $b{=}1$ for 1.7B); we instead derive $b$ per-batch from the batch's $q$-score distribution.
12	
13	\subsection{Dual-Constraint Framework}
14	\label{sec:dual}
15	
16	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two diagnostics.
17	
18	\paragraph{Effective real proportion.}
19	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether $x_i$ is human-authored.
20	The \emph{effective real proportion}
21	\begin{equation}
22	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
23	  \label{eq:alpha}
24	\end{equation}
25	measures the share of weight allocated to likely-real samples.
26	Since $r_i$ is binary, $\aeff(0)$ takes only $B{+}1$ discrete values; however, for $b > 0$ the weights $w_i(b)$ vary continuously in $b$, making $\aeff(b)$ a continuous function amenable to bisection.
27	$\aeff$ is a proxy for the true real fraction (Pearson $r \approx 0.70$; Appendix~\ref{app:alpha_validation}); post-hoc calibration~\citep{guo2017calibration} yields ECE\,=\,0.05.
28	
29	\paragraph{Effective sample size.}
30	Kish's effective sample size~\citep{kish1965survey}
31	\begin{equation}
32	  \mathrm{ESS}(b) = \frac{\bigl(\sum_{i=1}^{B
…[truncated 2347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-22T16:53:31.383428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-22T16:53:31.584394+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
11	
12	\paragraph{Training.}
13	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, linear schedule with warmup (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision on a single NVIDIA RTX PRO 6000 (96\,GB).
14	All main
…[truncated 1656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T16:53:31.584751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-22T16:53:31.635323+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, paired $t{=}{-}6.2$, $p{=}0.025$) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
9	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
10	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
11	
12	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
13	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
14	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
15	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.020$, directionally consistent across all seeds).
16	Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curv
…[truncated 9481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-22T16:53:37.306579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T16:53:37.758624+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, confirmed across 3 seeds with mixed sign) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Our results identify three necessary conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046.
12	Third, \emph{scale}: at 1.7B the benefit diminishes ($\Delta{=}{-}0.013$) with OOD partially inconsistent, suggesting that larger models may be inherently more robust to contamination generated by smaller models.
13	In all three failure cases, the adaptive method's dual constraint limits degradation relative to unconstrained reweighting (ESS-only), but uniform remai
…[truncated 4005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T16:53:37.909600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-22T16:53:38.211174+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage over adaptive reweighting); (2) detectors require both discrimination and calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$) improves over uniform at $\rho \geq 0.4$ ($p \leq 0.025$) without tuning; validated on Qwen3 ${\leq}$1.7B, where the benefit diminishes.
3	Batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$, $p{<}0.01$) with diminishing marginal gains, suggesting favorable scaling with larger micro-batches typical of production training; the key bottleneck is extending detector calibration to cross-model contamination scenarios.
4	Code and data will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-22T16:53:38.261891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-22T16:53:38.663823+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B test also showed degradation ($\Delta{=}{+}0.20$), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., RoBERTa-based) and zero-shot methods (e.g., DetectGPT) remain untested, so the calibration finding may not generalize across detector architectures.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-22T16:53:38.664188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-22T16:53:38.714884+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; th
…[truncated 23825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T16:53:45.290227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T16:53:45.541706+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{katharopoulos2018not,
5	  title={Not All Samples Are Created Equal: Deep Learning with Importance Sampling},
6	  author={Katharopoulos, Angelos and Fleuret, Fran{\c{c}}ois},
7	  booktitle={International Conference on Machine Learning},
8	  pages={2525--2534},
9	  year={2018},
10	  organization={PMLR}
11	}
12	
13	@inproceedings{ren2018learning,
14	  title={Learning to Reweight Examples for Robust Deep Learning},
15	  author={Ren, Mengye and Zeng, Wenyuan and Yang, Bin and Urtasun, Raquel},
16	  booktitle={International Conference on Machine Learning},
17	  pages={4334--4343},
18	  year={2018},
19	  organization={PMLR}
20	}
21	
22	@article{chen2024bull,
23	  title={Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves {LLM} Generalization},
24	  author={Chen, Xuxi and Li, Zhendong and Cai, Daixuan and Yao, Huanran and Chen, Zheng and Wang, Zhongming},
25	  journal={arXiv preprint arXiv:2402.14270},
26	  year={2024}
27	}
28	
29	@inproceedings{kang2025demystifying,
30	  title={Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls},
31	  author={Kang, Feiyang and Xu, Yifan and Pu, Jingkang and Hu, Bushi and Li, Haonan and Chen, Hongliang and Zhu, Yiming and Chen, Zijian and Liu, Mohan and Liu, Jingcheng and Liu, Haoran and Han, Song},
32	  booktitle={EMNLP},
33	  year={2025}
34	}
35	
36	@article{zibakhsh2025fortifai,
37	  title={{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},
38	  author={Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koushanfar, Farinaz},
39	  journal={arXiv preprint arXiv:2509.08972},
40	  year={2025}
41	}
42	
43	@article{yi2025escaping,
44	  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
…[truncated 13575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-22T16:53:45.592376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-22T16:53:45.592895+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T16:54:36.718542+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-22T16:54:37.270831+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 922 · 2026-05-22T16:54:57.450149+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20731
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-22T16:54:57.488607+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 20217
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-22T16:54:57.591317+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, double-blind, 正文 ≤ 8 页, 参考文献无限制\n- **匿名**: double-blind（无匿名期要求）\n- **附录**: 允许但 reviewer 不必阅读；关键内容必须在正文\n- **Limitations**: 必须有，不计入页数\n- **Responsible NLP Checklist**: 应在 OpenReview 表单填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- Sections: `projects/provenance_weight_training/docs/paper/sections/` 下各 .tex 文件\n- PDF: `projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Dual-constraint framework (α_eff ≥ τ, ESS ≥ n_min) 的数学框架是否合理？Proposition 1-2 的证明是否正确？\n- b* 的 bisection 求解是否有收敛保证？离散 B=4 下 α_eff 仅 5 个离散值，连续性声明是否站得住？\n- α_eff 作为 true real fraction 的 proxy (r=0.70) 是否足够支撑方法的理论动机？\n- Minimum intervention 原则的合理性——为什么最小 b 比最大 b 更好？是否有理论支持？\n\n### 2. 实验设计\n- 132M tokens, Qwen3-0.6B continued pretraining, 3 seeds——规模是否足以支撑 claims？\n- Self-contamination 设定（generator = trainee）的生态效度\n- Baselines 是否充分？缺少哪些重要 baseline？\n- Epoch-matched comparison 的实验设计是否严密？LR schedule confound 是否完全排除？\n- ρ=0.2 失败、1.7B 效果减弱——boundary conditions 的刻画是否充分？\n\n### 3. 统计分析\n- N=3 seeds, df=2: paired t-test 的可靠性？多重比较校正？\n- seed 42 checkpoint resume artifact (Appendix O)——是否影响主表结果的可信度？\n- Cross-seed variance 报告是否充分？bootstrap CI？\n- 下游任务零改善——负面结果的讨论是否充分？\n\n### 4. 格式合规\n- 正文是否超过 8 页？\n- 关键证据是否都在正文而非附录？\n\n请按 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses (逐条，标注 severity: critical/major/minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, double-blind, 正文 ≤ 8 页, 参考文献无限制\n- **匿名**: double-blind（无匿名期要求）\n- **附录**: 允许但 reviewer 不必阅读；关键内容必须在正文\n- **Limitations**: 必须有，不计入页数\n- **Responsible NLP Checklist**: 应在 OpenReview 表单填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- Sections: `projects/provenance_weight_training/docs/paper/sections/` 下各 .tex 文件\n- PDF: `projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Dual-constraint framework (α_eff ≥ τ, ESS ≥ n_min) 的数学框架是否合理？Proposition 1-2 的证明是否正确？\n- b* 的 bisection 求解是否有收敛保证？离散 B=4 下 α_eff 仅 5 个离散值，连续性声明是否站得住？\n- α_eff 作为 true real fraction 的 proxy (r=0.70) 是否足够支撑方法的理论动机？\n- Minimum intervention 原则的合理性——为什么最小 b 比最大 b 更好？是否有理论支持？\n\n### 2. 实验设计\n- 132M tokens, Qwen3-0.6B continued pretraining, 3 seeds——规模是否足以支撑 claims？\n- Self-contamination 设定（generator = trainee）的生态效度\n- Baselines 是否充分？缺少哪些重要 baseline？\n- Epoch-matched comparison 的实验设计是否严密？LR schedule confound 是否完全排除？\n- ρ=0.2 失败、1.7B 效果减弱——boundary conditions 的刻画是否充分？\n\n### 3. 统计分析\n- N=3 seeds, df=2: paired t-test 的可靠性？多重比较校正？\n- seed 42 checkpoint resume artifact (Appendix O)——是否影响主表结果的可信度？\n- Cross-seed variance 报告是否充分？bootstrap CI？\n- 下游任务零改善——负面结果的讨论是否充分？\n\n### 4. 格式合规\n- 正文是否超过 8 页？\n- 关键证据是否都在正文而非附录？\n\n请按 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses (逐条，标注 severity: critical/major/minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T16:55:12.150514+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14559
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T16:55:12.351596+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "你是 Reviewer 2，负责审查 **新颖性、论文定位、完整性和写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, double-blind, 正文 ≤ 8 页, 参考文献无限制\n- **匿名**: double-blind（无匿名期要求）\n- **附录**: 允许但 reviewer 不必阅读；关键内容必须在正文\n- **Limitations**: 必须有，不计入页数\n- **Responsible NLP Checklist**: 应在 OpenReview 表单填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- Sections: `projects/provenance_weight_training/docs/paper/sections/` 下各 .tex 文件\n- PDF: `projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 相对于 Drayson et al. (2025) 的增量贡献是否足够？论文采用相同的加权公式 w=(1-q)^b，仅改变 b 的选择方式\n- ESS (Kish 1965) 和 α_eff 都不是新概念——dual constraint 组合的新颖性如何？\n- Epoch confound 发现的价值——这是显而易见的还是真正有洞察力的？\n- 检测器 calibration 对 reweighting 效果的影响——这是否已被先前工作暗示？\n\n### 2. 论文定位\n- 论文定位为 analysis paper 还是 method paper？定位是否一致？\n- Abstract 和 Introduction 同时强调 findings 和 adaptive b*——是否存在定位模糊？\n- Method section 的篇幅与 analysis paper 定位是否匹配？\n- Contribution 排序是否合理（epoch confound > detector requirements > mechanism > adaptive b*）？\n\n### 3. 完整性\n- Related work 覆盖是否充分？是否遗漏重要相关工作？\n- 是否缺少重要的实验（如更多 detector 类型、更大规模模型、非 self-contamination 场景）？\n- Limitations 是否诚实全面？\n- Conclusion 是否与 findings 匹配？\n\n### 4. 写作质量\n- 叙事是否清晰流畅？读者能否一遍读懂？\n- 术语使用是否一致？\n- Figure/Table 设计是否清晰有效？\n- 信息密度是否合适（非冗余也非遗漏）？\n- Discussion 作为 analysis paper 的核心章节，是否有足够深度？\n\n### 5. 格式合规\n- Responsible NLP Checklist 是否错误地包含在 PDF 中？（ARR 规定应在 OpenReview 表单中）\n- 引用格式是否符合 ACL 要求？\n- 匿名是否完整（无作者身份泄露）？\n\n请按 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses (逐条，标注 severity: critical/major/minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "你是 Reviewer 2，负责审查 **新颖性、论文定位、完整性和写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 Long Paper (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, double-blind, 正文 ≤ 8 页, 参考文献无限制\n- **匿名**: double-blind（无匿名期要求）\n- **附录**: 允许但 reviewer 不必阅读；关键内容必须在正文\n- **Limitations**: 必须有，不计入页数\n- **Responsible NLP Checklist**: 应在 OpenReview 表单填写，不在论文 PDF 中\n\n## 论文路径\n- LaTeX: `projects/provenance_weight_training/docs/paper/main.tex`\n- Sections: `projects/provenance_weight_training/docs/paper/sections/` 下各 .tex 文件\n- PDF: `projects/provenance_weight_training/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 相对于 Drayson et al. (2025) 的增量贡献是否足够？论文采用相同的加权公式 w=(1-q)^b，仅改变 b 的选择方式\n- ESS (Kish 1965) 和 α_eff 都不是新概念——dual constraint 组合的新颖性如何？\n- Epoch confound 发现的价值——这是显而易见的还是真正有洞察力的？\n- 检测器 calibration 对 reweighting 效果的影响——这是否已被先前工作暗示？\n\n### 2. 论文定位\n- 论文定位为 analysis paper 还是 method paper？定位是否一致？\n- Abstract 和 Introduction 同时强调 findings 和 adaptive b*——是否存在定位模糊？\n- Method section 的篇幅与 analysis paper 定位是否匹配？\n- Contribution 排序是否合理（epoch confound > detector requirements > mechanism > adaptive b*）？\n\n### 3. 完整性\n- Related work 覆盖是否充分？是否遗漏重要相关工作？\n- 是否缺少重要的实验（如更多 detector 类型、更大规模模型、非 self-contamination 场景）？\n- Limitations 是否诚实全面？\n- Conclusion 是否与 findings 匹配？\n\n### 4. 写作质量\n- 叙事是否清晰流畅？读者能否一遍读懂？\n- 术语使用是否一致？\n- Figure/Table 设计是否清晰有效？\n- 信息密度是否合适（非冗余也非遗漏）？\n- Discussion 作为 analysis paper 的核心章节，是否有足够深度？\n\n### 5. 格式合规\n- Responsible NLP Checklist 是否错误地包含在 PDF 中？（ARR 规定应在 OpenReview 表单中）\n- 引用格式是否符合 ACL 要求？\n- 匿名是否完整（无作者身份泄露）？\n\n请按 ARR 标准完成审稿，输出结构：Summary → Strengths → Weaknesses (逐条，标注 severity: critical/major/minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-22T16:55:13.659741+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1308
}
```

</details>

---


### Assistant

_source line 928 · 2026-05-22T16:55:21.640358+00:00_

全部派发完毕：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿 | 未启用（not_requested） |
| Reviewer 1（方法/实验/统计） | ✅ 已派发 |
| Reviewer 2（新颖性/定位/写作） | ✅ 已派发 |

等待两位 Reviewer 返回独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 929 · 2026-05-22T17:03:36.278836+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）
**侧重**: 新颖性、论文定位、完整性、写作质量

---

## Paper Summary

本文研究 detect-and-reweight (D&R) 范式在含合成文本的 continued LM pretraining 中的有效性条件。通过 Qwen3-0.6B 上的受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），作者报告三个发现：(1) D&R 相对于 adaptive reweighting 的 PPL 优势中 >95% 来自 multi-epoch exposure confound 而非 filtering quality；(2) 有效 reweighting 需要检测器同时具备足够的 discrimination (AUC) 和良好的 calibration (ECE)；(3) 机制通过 α_eff（effective real proportion）和 ESS（effective sample size）的 dual constraint 运作。作者提出 adaptive b* 公式化，消除 grid search 的同时匹配或超越 grid-searched 性能。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 扎实的分析工作，epoch confound 发现有价值，但方法新颖性有限、实验规模偏小、downstream task 无可测量改善，综合来看达到 Findings 水准但不足以进入主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（epoch-matched controls, 3 seeds, 逐因素消融），数学框架正确（Proposition 1-2 证明完整），但实验范围受限（仅 0.6B/1.7B, self-contamination, 单一数据集），泛化性未得到验证 |
| Excitement | 2.5/5 | Epoch confound 发现纠正了文献中的重要误判，有实际价值；但方法贡献增量式（同一公式 w=(1-q)^b，仅改变 b 选择方式），downstream 零提升削弱实际影响力 |
| Reproducibility | 4.0/5 | 实验细节充分（§4 报告 batch size, LR schedule, sequence length, hardware），承诺代码和数据在接收后公开，超参数均有报告；唯一不确定是合成数据生成的完整 prompt 细节（Appendix M 提到 128-token prefix prompt 但未给出完整模板） |
| Confidence | 4/5 | 熟悉数据 curation、pretraining 和 synthetic data detection 文献，仔细阅读了正文和全部 17 个附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 方法新颖性不足以支撑独立贡献
- 具体位置：§3.2 Dual-Constraint Framework, §1 Contribution list item 4
- 问题：论文的 methodological contribution 是将 ESS（Kish, 1965）和 α_eff 组合为 dual constraint 来自动选择 b*，但：(a) 加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)，无任何修改；(b) ESS 和 α_eff 均为已有概念，dual constraint 组合是直接应用而非根本性创新；(c) adaptive b* 本质上是超参数自动选择方法，替代 grid search——实用但算不上显著的概念性贡献。论文的真正价值在于分析发现（epoch confound, detector requirements），而非方法本身。
- 为什么影响接收：作为 method paper 投 main conference，novelty bar 未达到；作为 analysis paper，方法部分的篇幅和 contribution list 中的权重与定位不匹配。
- 建议修改方向：明确将论文定位为 empirical analysis paper，将 adaptive b* 作为分析的 practical corollary 而非并列的核心贡献。重新组织 contribution list，让分析发现占据更突出的位置。

**N2** [critical] Downstream task 无可测量改善
- 具体位置：§6 Discussion（"Downstream tasks do not reflect PPL improvements"）, Table 3
- 问题：Table 3 显示 adaptive reweighting vs. uniform training 在所有 downstream benchmarks 上 |Δ| ≤ 0.01，且方向不一致（"no individual task shows a consistent advantage"）。论文将此归因于"PPL improvements operate in a regime that standard benchmarks cannot resolve"和 0.6B 模型上 5-choice tasks 灵敏度不足。但这个论点有循环论证的嫌疑：如果效果微小到现有评估方法都测不出来，那么论文的实际价值论证就缺乏支撑。
- 为什么影响接收：一个 pretraining 方法论文如果无法展示任何 downstream 改善，其实际意义会被严重质疑。PPL 改善仅 Δ≈-0.014（~0.08% relative），这属于工程 noise 级别。
- 建议修改方向：(a) 在更大模型（7B+）上验证 PPL 改善是否放大并传递到 downstream；(b) 使用更细粒度的评估（如 generation quality、factual accuracy on contaminated domains）代替粗粒度的 benchmark accuracy；(c) 或者诚实地将论文重新定位为纯分析/负面结果论文，不主张实际方法改进。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] 实验规模和场景过于狭窄
- 具体位置：§4 Experimental Setup, §8 Limitations
- 问题：
  - **模型规模**：仅 0.6B 和 1.7B，现代 pretraining 至少在 7B 级别。§5.3 的 1.7B 结果仅简述一段（"the method scales without degradation"），未提供完整的 epoch-matched 消融。
  - **Self-contamination**：所有合成数据由 Qwen3-0.6B 生成，训练也用 Qwen3-0.6B（或 1.7B）。真实世界的合成污染来自多样的模型（GPT-4, Claude, Llama 等），检测难度和分布特征完全不同。
  - **单一基础数据集**：仅 FineWeb。不同领域/风格的数据分布可能导致不同结论。
  - **单一污染类型**：仅 continuation-style generation（128-token prefix → 384 tokens）。真实污染包括 paraphrase、翻译、instruction-following outputs 等。
- 建议：至少增加一个 cross-model contamination 实验（如用 Llama 生成，Qwen 训练），以验证核心发现的鲁棒性。Appendix O 的 cross-model transfer 实验（Llama-3.2-3B, Table 12）结果混合（MMLU 升 HellaSwag 降），并不令人信服。

**W2** [major] 论文定位存在模糊性
- 具体位置：Abstract, §1 Introduction, §3 Method
- 问题：Abstract 第一句话强调"we analyze when, why, and how detect-and-reweight works"（分析定位），但随后介绍"we introduce a dual-constrained formulation"（方法定位）。§1 的四条 contribution 混合了观察型贡献（epoch confound, detector requirements, mechanism）和方法型贡献（adaptive b*），缺乏明确的主次层级。§3 Method 占据将近 1.5 页的篇幅，对于一篇分析论文来说偏重。
- 建议：在 Abstract 和 Introduction 中明确建立"analysis paper with practical implications"的定位。可以将 adaptive b* 的详细推导移至附录，主文仅保留核心思想（~半页），释放空间给更深入的分析讨论或更大规模的实验结果。

**W3** [minor] α_eff 作为 quality proxy 的相关性有限
- 具体位置：§8 Limitations, Appendix K (Table 10)
- 问题：α_eff 与 true batch-level real fraction 的 Pearson 相关仅 r=0.70（解释 ~49% variance）。负斜率 β(≈-0.031) 表明 α_eff 系统性低估真实 real fraction，导致方法偏向保守干预。这意味着 quality constraint 基于一个较嘈杂的代理量运作。
- 建议：讨论是否存在更精确的 proxy，或分析 proxy noise 对 b* 选择的实际影响有多大。

**W4** [minor] 关键效应量极小，实际意义需更充分论证
- 具体位置：Table 1, §6 Discussion
- 问题：Adaptive b* vs. uniform 的 PPL 改善为 Δ=-0.014（17.620 vs. 17.634），即 ~0.08% relative improvement。在 epoch-matched 条件下，adaptive vs. D&R full 的优势为 Δ=-0.032（paired p=0.025）。虽然统计显著，但效应量极小。论文在 §6 承认"the true value added by detect-and-reweight is substantially smaller than published results suggest"，但未充分讨论这个效应量在实际 pretraining pipeline 中是否值得引入检测器和 reweighting 的额外复杂性。
- 建议：增加一个 cost-benefit 分析段落——引入检测器训练、推理、calibration 的计算开销 vs. 获得的 0.08% PPL 改善，帮助读者判断在什么条件下值得使用。

**W5** [minor] Responsible NLP Research Checklist 出现在 PDF 中
- 具体位置：Page 9
- 问题：EMNLP 2026 通过 ARR 审稿，Responsible NLP Checklist 应在 OpenReview submission form 中填写，不应包含在论文 PDF 中。当前 checklist 占据约 1 页篇幅。
- 建议：从 PDF 中移除 checklist，在 OpenReview 表单中填写。释放的空间可用于加强 Discussion 或增加实验。

---

## 小问题（不影响接收）

- §3.1 Problem Setup：contamination ratio ρ 的 footnote 9（page 4 底部）区分 token-level 和 document-level contamination ratio，这个区分在主文中提到得太晚，建议在 §3.1 定义 ρ 时就澄清。
- Figure 2：y 轴标注为"Held-out PPL ↓"，图例中"Uniform (full)"和"D&R full (grid)"的线条在黑白打印下不易区分，建议调整 line style 或 marker。
- Table 2（page 6）：列标题"Seed 42", "Seed 123", "Seed 456" 与 "Mean 4σ"——应为 "Mean ± σ" 或 "Mean (σ)"，"4σ" 的含义不明确（是 4 倍标准差？还是排版错误？）。
- §2 Related Work 首段中"Cheng et al. (2025) survey the broader contamination landscape"出现在一个密集的文献回顾段落中，但该引用的具体贡献未被明确说明——建议简要说明其与本文的关系。

---

## Questions for Authors

Q1. 在 7B+ 规模上，epoch confound 发现是否仍然成立？是否有初步证据表明效应量随规模变化？

Q2. 如果使用 cross-model contamination（如 GPT-4 生成的文本），检测器的 AUC 和 ECE 如何变化？dual constraint 方法是否仍然有效？

Q3. Table 3 的 downstream null result 是否可能源于评估方法的局限而非方法本身？是否考虑过更细粒度的评估（如在受污染领域的 factual accuracy 或 generation quality）？

Q4. Quality threshold τ=0.7 和 τ_min 的选择依据是什么？Appendix D 显示了 threshold sweep 但 τ=0.7 的选择似乎基于经验而非理论——这会影响方法在新数据集上的适用性吗？

Q5. Appendix Q (Table 13) 的 practitioner decision summary 非常实用，为什么不放在主文中？这会比当前 §3.2 中的部分数学推导更有助于读者。

---

## Missing References

引用覆盖基本充分，以下为可考虑补充的参考：

- **Llama 3 technical report (Meta, 2024)**：描述了大规模 pretraining 中的数据 curation pipeline，包括合成数据处理，可在 Related Work §2 中作为 motivation 引用，说明工业界对 synthetic contamination 的关注。
- **Penedo et al. (2024) 的 FineWeb 论文**已引用为数据来源，但其中关于 quality filtering 与 quantity tradeoff 的讨论与本文 §6 的 cost-benefit 分析相关，可进一步引用其发现。

---

## 主要优势

1. **Epoch confound 发现（S1）**：通过严谨的 epoch-matched 对照实验（Table 1），证明 D&R 的 >95% PPL 优势来自 multi-epoch exposure 而非 filtering quality，这纠正了 Drayson et al. (2025) 中的重要误归因。独立的 LR-schedule 复现（§5.1）进一步加强了这一结论的可信度。

2. **实验设计的严谨性（S2）**：全文采用系统化的受控实验——逐因素消融（epoch matching → detector quality → contamination level → scale），3 seeds 提供统计基础，paired t-tests 报告显著性。这是 empirical ML 论文的良好范例。

3. **诚实的 Discussion（S3）**：§6 不回避负面发现（downstream 无改善、α_eff proxy 局限、效应量极小），这种透明度在分析论文中尤为重要，增强了结论的可信度。

4. **Analysis overview 可视化（S4）**：Figure 1 有效地将三个发现的逻辑链条可视化（epoch confound → detector requirements → mechanism → adaptive b*），帮助读者快速建立论文结构的心理模型。

5. **详尽的附录（S5）**：17 个附录（A-Q）提供了完整的证明、消融、proxy 验证和 practitioner guide，展现了作者对研究细节的认真态度。

---

## 总结

本文的核心价值在于 epoch confound 发现——这是一个有意义的 empirical contribution，纠正了文献中的过度乐观估计。实验设计严谨，写作清晰。但方法贡献（adaptive b*）是在已有公式上的增量改进，downstream task 无可测量改善削弱了实际影响力，实验规模（0.6B/1.7B, self-contamination, 单一数据集）限制了结论的泛化性。综合来看，论文达到 Findings 水准：发现有用、方法可靠，但 novelty 和 impact 不足以进入主会议。若能在 7B+ 上复现关键发现并展示 downstream 改善，可提升至 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 930 · 2026-05-22T17:03:49.171698+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 931 · 2026-05-22T17:03:56.824905+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心结论：

- **Overall 3.0 (Findings)**，Soundness 3.5，Excitement 2.5
- **最大优势**：epoch confound 发现有真实价值，纠正了 Drayson et al. (2025) 中 >95% 的效果误归因；实验设计严谨
- **主要问题**：(1) 方法新颖性有限——同一公式 w=(1-q)^b，仅改变 b 的选择方式；(2) downstream task 零改善（Table 3, |Δ|≤0.01）削弱实际意义；(3) 实验规模太小（0.6B/1.7B, self-contamination, 单一数据集）
- **建议**：明确定位为 analysis paper，adaptive b* 降级为 practical corollary；增加 7B+ 实验和 cross-model contamination 验证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 932 · 2026-05-22T17:04:04.715103+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 66

## Round 66

6 recorded events


### User

_source line 933 · 2026-05-22T17:05:31.886118+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法严谨性、实验设计、统计分析）

### Summary

本文研究 detect-and-reweight (D&R) 在 continued LM pretraining 中对抗合成数据污染的有效性条件。核心发现：(1) ~95% 的 D&R 已发表优势源于 epoch confound；(2) 有效 reweighting 需三个前提（检测器 AUC、校准 ECE、最小干预）；(3) dual-constraint adaptive framework（α_eff ≥ τ + ESS ≥ n_min）通过 bisection 自动选择 b*。实验：Qwen3-0.6B, 132M FineWeb tokens, self-contamination ρ=0.4, 3 seeds。

---

### Strengths

**S1. Epoch confound 识别与验证设计精良。** Table 1 中 D&R full (~2.6 epochs) PPL=17.278 vs. epoch-matched D&R (~1.0 epoch) PPL=17.657，差值 0.379 占 D&R 优势的 ~96.7%。独立 LR schedule 复现（17.651 vs. 17.657, Δ≈0.006）排除 LR 混淆。对 D&R 社区有重要修正价值。

**S2. 三个有效性条件提炼具实用价值。** Section 5.3 消融有说服力：Random weights 仅增加方差；N-gram detector (AUC=0.73) 因校准不足反降 PPL；ESS-only 在 b* 过大时落入退化区（Figure 2 shaded region）。

**S3. 数学框架简洁正确。** Proposition 1-2 的证明（Appendix A）利用协方差符号和加权集中性标准结论，推导正确。

**S4. 诚实报告负面结果。** Table 3 下游零改善、ρ=0.2 失败、1.7B/Llama-3.2-3B 退化均如实报告。

**S5. 附录丰富（A-Q），可复现性好。**

---

### Weaknesses

**W1 [critical] N=3 seeds 且 seed 42 存在 checkpoint resume artifact。**
- 位置：Table 1-2 (Section 5.1); Appendix P
- Appendix P 揭示 seed 42 使用 checkpoint-resumed run，前 ~1,000 步超参不同，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。3 seed 中 1 个受 artifact 影响，对均值有巨大杠杆效应。核心 paired t=−6.2, p=0.025 的可信度存疑。
- 建议：以 fresh-from-scratch seed 42 替换重跑主表；或排除 seed 42 做 robustness check。

**W2 [critical] 多重比较未校正。**
- 位置：Section 5.1, 5.2, 5.3
- 6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。
- 建议：报告 Bonferroni/Holm 校正 p 值或 bootstrap CI。

**W3 [major] α_eff proxy 质量偏弱（r=0.70, R²=0.49）。**
- 位置：Section 3.2; Appendix K, Table 10
- 仅解释 49% 方差，负回归偏差（β₁<0.03）导致系统性低估。理论框架依赖 α_eff 作为质量代理，但 proxy 质量仅中等。论文未分析 51% 未解释方差的来源。
- 建议：分析误差来源（检测器噪声 vs. batch size vs. 二值化）；测试更大 batch 时的 proxy 质量。

**W4 [major] Self-contamination（generator = trainee）生态效度有限。**
- 位置：Section 4
- 实际场景合成数据来自更强模型（GPT-4 等），分布差异大。Self-contamination 简化了检测任务。Appendix O 的 cross-model transfer 退化（Δ=+0.20）暗示可能高估效果。
- 建议：增加 cross-generator 实验。

**W5 [major] 下游任务零改善限制实际影响力。**
- 位置：Table 3, Section 6
- PPL 改善~0.07，但 5 个 benchmark 全部差异 <0.01 accuracy。论文讨论仅 ~4 行。
- 建议：讨论 PPL 阈值效应和在更高 contamination/更长训练下的扩展可能。

**W6 [major] 适用范围极窄（仅 ρ≥0.4, ≤0.6B）。**
- 位置：Section 5.3, Appendix N (ρ=0.2 失败); Limitations, Table 13 (1.7B 退化 0.128, Llama-3.2-3B 退化 0.20)
- ρ=0.2（20% 污染，实际场景的下限）方法失效。1.7B+ 模型效果反转。但 Abstract/Introduction 设定的问题范围是 "web corpora at scale"。ρ=0.3 中间点完全缺失。
- 建议：补充 ρ=0.3；收窄 claim 适用范围。

**W7 [minor] Per-batch B=4 下 dual constraint 统计可靠性存疑。**
- Algorithm 1 显示 b* per-batch 计算，B=4 下 α_eff(0) 仅 5 个离散值，方差极大。论文未报告 b* 在 batch 间的分布。

**W8 [minor] 关键证据（proxy validation r=0.70, seed 42 artifact, ρ=0.2 分析）仅在附录。**

---

### Questions

Q1. 能否提供排除/替换 seed 42 后的主表结果？
Q2. 在 gradient accumulation 级别（B=16）计算 α_eff 时 proxy 质量是否改善？
Q3. ρ=0.3 表现如何？
Q4. Grid search 显示 b=0.4-1.0 范围内 PPL 变化小（Table 4），简单固定 b=0.6 是否足够？
Q5. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i）？

---

### Missing References

1. Influence function-based data valuation (Pruthi et al., 2020)
2. Distributionally robust optimization (Sagawa et al., 2020)——reweighting 目标可视为 DRO 特例
3. PPL-downstream gap 文献（如 Tay et al., 2022 关于 PPL 与下游的非线性关系）

---

### Overall Assessment

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3/5 | 数学框架正确，epoch confound 分析精良；但 seed artifact + 多重比较未校正 + proxy r=0.70 构成显著顾虑 |
| Excitement | 3/5 | Epoch confound 发现对社区有修正价值，三条件有实用性；但适用范围极窄，下游零改善 |
| Overall | 3 (Findings) | 分析贡献（epoch confound、有效性条件）达 Findings 水准；统计可信度和窄适用范围阻止 main conference 推荐 |
| Confidence | 4/5 | 熟悉 importance weighting、合成数据检测、LM pretraining；仔细阅读全文及全部附录 |

**提升路径**：修复 seed 42 + corrected p-values + ρ=0.3 数据可达 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-22T17:06:11.365468+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿意见（Round 1）\n**侧重**: 新颖性、论文定位、完整性、写作质量\n\n### Overall: 3.0 (Findings)\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 4.0/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 方法新颖性不足以支撑独立贡献\n- 具体位置：§3.2 Dual-Constraint Framework, §1 Contribution list item 4\n- 问题：论文的 methodological contribution 是将 ESS（Kish, 1965）和 α_eff 组合为 dual constraint 来自动选择 b*，但：(a) 加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)，无任何修改；(b) ESS 和 α_eff 均为已有概念，dual constraint 组合是直接应用而非根本性创新；(c) adaptive b* 本质上是超参数自动选择方法，替代 grid search——实用但算不上显著的概念性贡献。论文的真正价值在于分析发现（epoch confound, detector requirements），而非方法本身。\n- 建议修改方向：明确将论文定位为 empirical analysis paper，将 adaptive b* 作为分析的 practical corollary 而非并列的核心贡献。\n\n**N2** [critical] Downstream task 无可测量改善\n- 具体位置：§6 Discussion, Table 3\n- 问题：Table 3 显示 adaptive reweighting vs. uniform training 在所有 downstream benchmarks 上 |Δ| ≤ 0.01，且方向不一致。论文将此归因于\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"和 0.6B 模型灵敏度不足。但如果效果微小到现有评估方法都测不出来，那么论文的实际价值论证就缺乏支撑。\n- 建议修改方向：在更大模型（7B+）上验证；或诚实地将论文重新定位为纯分析/负面结果论文。\n\n### Should-Fix 问题\n\n**W1** [major] 实验规模和场景过于狭窄\n- 仅 0.6B 和 1.7B，self-contamination，单一数据集（FineWeb），单一污染类型。\n\n**W2** [major] 论文定位存在模糊性\n- Abstract 第一句强调 analysis，随后介绍 method。§3 Method 占据将近 1.5 页，对 analysis paper 偏重。\n\n**W3** [minor] α_eff 作为 quality proxy 的相关性有限（r=0.70, 49% variance explained）\n\n**W4** [minor] 关键效应量极小（Δ=-0.014, ~0.08% relative），实际意义需更充分论证\n\n**W5** [minor] Responsible NLP Research Checklist 出现在 PDF 中（应在 OpenReview 表单）\n\n### 小问题\n- §3.1 ρ 的 token-level vs. document-level 区分提到太晚\n- Figure 2 黑白打印下线条不易区分\n- Table 2 \"4σ\" 含义不明确\n- §2 Cheng et al. (2025) 引用位置处贡献未明确说明\n\n### Questions\nQ1. 7B+ 上 epoch confound 是否仍成立？\nQ2. Cross-model contamination 下 AUC/ECE 如何变化？\nQ3. Downstream null result 是否源于评估方法局限？\nQ4. τ=0.7 选择依据？\nQ5. Appendix Q Table 13 decision summary 为什么不放主文？\n\n### 主要优势\nS1. Epoch confound 发现有修正价值\nS2. 实验设计严谨（逐因素消融，3 seeds）\nS3. 诚实的 Discussion\nS4. Figure 1 可视化有效\nS5. 附录详尽\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、小问题和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿意见（Round 1）\n**侧重**: 新颖性、论文定位、完整性、写作质量\n\n### Overall: 3.0 (Findings)\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 4.0/5, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 方法新颖性不足以支撑独立贡献\n- 具体位置：§3.2 Dual-Constraint Framework, §1 Contribution list item 4\n- 问题：论文的 methodological contribution 是将 ESS（Kish, 1965）和 α_eff 组合为 dual constraint 来自动选择 b*，但：(a) 加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)，无任何修改；(b) ESS 和 α_eff 均为已有概念，dual constraint 组合是直接应用而非根本性创新；(c) adaptive b* 本质上是超参数自动选择方法，替代 grid search——实用但算不上显著的概念性贡献。论文的真正价值在于分析发现（epoch confound, detector requirements），而非方法本身。\n- 建议修改方向：明确将论文定位为 empirical analysis paper，将 adaptive b* 作为分析的 practical corollary 而非并列的核心贡献。\n\n**N2** [critical] Downstream task 无可测量改善\n- 具体位置：§6 Discussion, Table 3\n- 问题：Table 3 显示 adaptive reweighting vs. uniform training 在所有 downstream benchmarks 上 |Δ| ≤ 0.01，且方向不一致。论文将此归因于\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"和 0.6B 模型灵敏度不足。但如果效果微小到现有评估方法都测不出来，那么论文的实际价值论证就缺乏支撑。\n- 建议修改方向：在更大模型（7B+）上验证；或诚实地将论文重新定位为纯分析/负面结果论文。\n\n### Should-Fix 问题\n\n**W1** [major] 实验规模和场景过于狭窄\n- 仅 0.6B 和 1.7B，self-contamination，单一数据集（FineWeb），单一污染类型。\n\n**W2** [major] 论文定位存在模糊性\n- Abstract 第一句强调 analysis，随后介绍 method。§3 Method 占据将近 1.5 页，对 analysis paper 偏重。\n\n**W3** [minor] α_eff 作为 quality proxy 的相关性有限（r=0.70, 49% variance explained）\n\n**W4** [minor] 关键效应量极小（Δ=-0.014, ~0.08% relative），实际意义需更充分论证\n\n**W5** [minor] Responsible NLP Research Checklist 出现在 PDF 中（应在 OpenReview 表单）\n\n### 小问题\n- §3.1 ρ 的 token-level vs. document-level 区分提到太晚\n- Figure 2 黑白打印下线条不易区分\n- Table 2 \"4σ\" 含义不明确\n- §2 Cheng et al. (2025) 引用位置处贡献未明确说明\n\n### Questions\nQ1. 7B+ 上 epoch confound 是否仍成立？\nQ2. Cross-model contamination 下 AUC/ECE 如何变化？\nQ3. Downstream null result 是否源于评估方法局限？\nQ4. τ=0.7 选择依据？\nQ5. Appendix Q Table 13 decision summary 为什么不放主文？\n\n### 主要优势\nS1. Epoch confound 发现有修正价值\nS2. 实验设计严谨（逐因素消融，3 seeds）\nS3. 诚实的 Discussion\nS4. Figure 1 可视化有效\nS5. 附录详尽\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、小问题和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-22T17:06:23.184235+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11818
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-22T17:06:23.938029+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿报告（方法严谨性、实验设计、统计分析）\n\n### Overall: 3 (Findings)\nSoundness 3/5, Excitement 3/5, Confidence 4/5\n\n### Strengths\nS1. Epoch confound 识别与验证设计精良（Table 1, LR 复现 Δ≈0.006）\nS2. 三个有效性条件提炼具实用价值\nS3. 数学框架简洁正确（Proposition 1-2）\nS4. 诚实报告负面结果\nS5. 附录丰富，可复现性好\n\n### Weaknesses\n\n**W1 [critical] N=3 seeds 且 seed 42 存在 checkpoint resume artifact。**\n- Appendix P 揭示 seed 42 使用 checkpoint-resumed run，前 ~1,000 步超参不同，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。3 seed 中 1 个受 artifact 影响，对均值有巨大杠杆效应。核心 paired t=−6.2, p=0.025 的可信度存疑。\n- 建议：以 fresh-from-scratch seed 42 替换重跑主表；或排除 seed 42 做 robustness check。\n\n**W2 [critical] 多重比较未校正。**\n- 6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。\n\n**W3 [major] α_eff proxy 质量偏弱（r=0.70, R²=0.49）。**\n- 仅解释 49% 方差，负回归偏差导致系统性低估。论文未分析 51% 未解释方差的来源。\n\n**W4 [major] Self-contamination（generator = trainee）生态效度有限。**\n- Appendix O 的 cross-model transfer 退化（Δ=+0.20）暗示方法可能高估效果。\n\n**W5 [major] 下游任务零改善限制实际影响力。**\n- PPL 改善~0.07，但 5 个 benchmark 全部差异 <0.01 accuracy。\n\n**W6 [major] 适用范围极窄（仅 ρ≥0.4, ≤0.6B）。**\n- ρ=0.2 失效，1.7B+ 效果反转。ρ=0.3 中间点缺失。Abstract/Introduction 的问题范围远超实际验证范围。\n\n**W7 [minor] Per-batch B=4 下 dual constraint 统计可靠性存疑。**\n- B=4 下 α_eff(0) 仅 5 个离散值。b* batch 间分布未报告。\n\n**W8 [minor] 关键证据仅在附录。**\n- proxy validation r=0.70, seed 42 artifact, ρ=0.2 分析等关键信息仅在附录。\n\n### Questions\nQ1. 能否提供排除/替换 seed 42 后的主表结果？\nQ2. gradient accumulation 级别（B=16）计算 α_eff 时 proxy 质量是否改善？\nQ3. ρ=0.3 表现如何？\nQ4. 简单固定 b=0.6 是否足够？\nQ5. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i）？\n\n### Missing References\n1. Influence function-based data valuation (Pruthi et al., 2020)\n2. DRO (Sagawa et al., 2020) 作为 reweighting 目标特例\n3. PPL-downstream gap 文献（Tay et al., 2022）\n\n---\n\n请逐条回应上述所有 Weakness、Questions 和 Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 审稿报告（方法严谨性、实验设计、统计分析）\n\n### Overall: 3 (Findings)\nSoundness 3/5, Excitement 3/5, Confidence 4/5\n\n### Strengths\nS1. Epoch confound 识别与验证设计精良（Table 1, LR 复现 Δ≈0.006）\nS2. 三个有效性条件提炼具实用价值\nS3. 数学框架简洁正确（Proposition 1-2）\nS4. 诚实报告负面结果\nS5. 附录丰富，可复现性好\n\n### Weaknesses\n\n**W1 [critical] N=3 seeds 且 seed 42 存在 checkpoint resume artifact。**\n- Appendix P 揭示 seed 42 使用 checkpoint-resumed run，前 ~1,000 步超参不同，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。3 seed 中 1 个受 artifact 影响，对均值有巨大杠杆效应。核心 paired t=−6.2, p=0.025 的可信度存疑。\n- 建议：以 fresh-from-scratch seed 42 替换重跑主表；或排除 seed 42 做 robustness check。\n\n**W2 [critical] 多重比较未校正。**\n- 6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。\n\n**W3 [major] α_eff proxy 质量偏弱（r=0.70, R²=0.49）。**\n- 仅解释 49% 方差，负回归偏差导致系统性低估。论文未分析 51% 未解释方差的来源。\n\n**W4 [major] Self-contamination（generator = trainee）生态效度有限。**\n- Appendix O 的 cross-model transfer 退化（Δ=+0.20）暗示方法可能高估效果。\n\n**W5 [major] 下游任务零改善限制实际影响力。**\n- PPL 改善~0.07，但 5 个 benchmark 全部差异 <0.01 accuracy。\n\n**W6 [major] 适用范围极窄（仅 ρ≥0.4, ≤0.6B）。**\n- ρ=0.2 失效，1.7B+ 效果反转。ρ=0.3 中间点缺失。Abstract/Introduction 的问题范围远超实际验证范围。\n\n**W7 [minor] Per-batch B=4 下 dual constraint 统计可靠性存疑。**\n- B=4 下 α_eff(0) 仅 5 个离散值。b* batch 间分布未报告。\n\n**W8 [minor] 关键证据仅在附录。**\n- proxy validation r=0.70, seed 42 artifact, ρ=0.2 分析等关键信息仅在附录。\n\n### Questions\nQ1. 能否提供排除/替换 seed 42 后的主表结果？\nQ2. gradient accumulation 级别（B=16）计算 α_eff 时 proxy 质量是否改善？\nQ3. ρ=0.3 表现如何？\nQ4. 简单固定 b=0.6 是否足够？\nQ5. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i）？\n\n### Missing References\n1. Influence function-based data valuation (Pruthi et al., 2020)\n2. DRO (Sagawa et al., 2020) 作为 reweighting 目标特例\n3. PPL-downstream gap 文献（Tay et al., 2022）\n\n---\n\n请逐条回应上述所有 Weakness、Questions 和 Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-22T17:06:25.349100+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 938 · 2026-05-22T17:06:28.113004+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 939 · 2026-05-22T17:06:30.622346+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分总结**：Overall 3 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5。

**核心判断**：论文的分析贡献（epoch confound 识别、三个有效性条件）是真实且有价值的，达到 Findings 水准。但两个 critical 问题——seed 42 checkpoint artifact 纳入主表（W1）和多重比较未校正（W2）——使统计推断可信度不足，加上方法适用范围极窄（仅 ρ≥0.4, ≤0.6B）和下游任务零改善，阻止了 main conference 推荐。修复 seed 42、补充 corrected p-values 和 ρ=0.3 实验后可达 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 940 · 2026-05-22T17:06:35.262360+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 941 · 2026-05-22T17:08:34.848996+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### Must-Fix

[AGREE] R2-N1 (方法新颖性): 同意。w=(1-q)^b 来自 Drayson et al. (2025)，ESS/α_eff 是已有概念，dual constraint 组合工程合理但非概念性创新。论文真正价值在分析发现（epoch confound ~96.7%, Table 1; 三条件系统化, §5.3）。建议将 adaptive b* 定位为分析的 practical corollary。

[AGREE] R2-N2 (Downstream null): 完全同意，我在 W5 也标记。补充：§6 对此仅 ~4 行讨论，不够充分。应讨论 PPL→downstream 阈值效应和扩展可能。

### Should-Fix

[AGREE] R2-W1 (窄规模): 同意。补充 R2 未提到的点：ρ=0.3 关键中间点完全缺失，无法定位 failure boundary。

[AGREE] R2-W2 (定位模糊): 同意。建议压缩 §3 method 到半页、扩展 epoch confound 和 null result 讨论。

[REBUT] R2-W3 (α_eff proxy, minor): **严重性应提升至 major**。α_eff 是 dual-constraint 的理论基石（bisection 目标函数），r=0.70 (R²=0.49) 仅解释不到一半方差。Table 10 (Appendix K) 显示负回归偏差（β₁<0.03），系统性低估。论文未分析 51% 未解释方差来源。这不是 minor 精度问题，是方法核心假设的验证缺口。

[AGREE] R2-W4 (效应量小): 同意但补充 nuance——对 analysis paper，小效应量本身是 finding（揭示控制 epoch confound 后 D&R 真实增益远小于已发表数字）。真正问题是小到 downstream 测不出（R2-N2）。

[AGREE] R2-W5 (Checklist in PDF): 同意，不符合 EMNLP 2026/ARR 格式规范。

### 小问题
全部 [AGREE]——ρ 区分太晚、Figure 2 黑白可读性、Table 2 "4σ"、Cheng et al. 引用均为有效观察。

### Questions 回应
- Q1 (7B+ epoch confound): 逻辑上应成立（结构性方法论问题），但缺乏实验验证，论文应在 Discussion 明确推论。
- Q2 (Cross-model AUC/ECE): 关键遗漏——Appendix O 的 cross-model 实验未报告检测器 AUC/ECE 变化。
- Q3 (Downstream 评估局限): 论文未尝试 fine-grained 评估（subset perplexity、generation quality 等），仅凭 5 个 benchmark accuracy 下结论证据不足。
- Q4 (τ=0.7): Grid search 结果而非理论推导，与"避免 grid search"动机矛盾，但 §5.3 sensitivity 分析显示 τ=0.6-0.8 范围内相对稳健。
- Q5 (Table 13 入主文): 同意，practitioner decision summary 应入正文。

### 核心分歧
唯一分歧：R2-W3 α_eff proxy 严重性。R2 标 minor，我认为 major。

### 共识
两份审稿均给 Overall 3.0 (Findings)，共识区域：(1) 主要价值在分析而非方法；(2) Downstream null 是最大实践弱点；(3) 规模/场景过窄；(4) 定位应偏向 analysis paper。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 942 · 2026-05-22T17:08:39.621247+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 943 · 2026-05-22T17:08:42.142030+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：与 R2 在绝大多数问题上达成共识（Overall 3.0 Findings），唯一分歧是 α\_eff proxy 质量的严重性——R2 标 minor，我认为应为 major，因为这是 dual-constraint framework 理论基础的核心验证缺口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 944 · 2026-05-22T17:08:46.697027+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 70

## Round 70

12 recorded events


### User

_source line 945 · 2026-05-22T17:10:54.587935+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: Seed 42 checkpoint resume artifact**
同意这是本文最严重的统计问题。Appendix P 明确承认 seed 42 的 adaptive 模型使用了 checkpoint-resumed run，in-distribution effect 被膨胀约 8 倍（Δ≈−0.041 resume vs. Δ≈−0.005 from-scratch）。在仅 3 seeds 的情况下，这对均值有决定性的杠杆效应。

我进一步补充一个定量推算：Table 1 中 adaptive b* 的 3-seed mean PPL 为 17.620，uniform 为 17.634，差值 Δ=-0.014。如果 seed 42 的 artifact 使该 seed 的 Δ 从约 -0.005 膨胀到约 -0.041，那么替换后 3-seed mean Δ 会从 -0.014 缩小到约 -0.002，基本消失。这意味着 **Table 1 中 adaptive b* vs. uniform 的核心比较可能完全由 artifact 驱动**。paired t=−6.2, p=0.025 的可信度因此严重存疑。

这个问题的严重性甚至超过 R1 的评估——它不仅影响 method 贡献的可信度，还间接影响 epoch confound 分析的 baseline，因为 epoch-matched comparison 也依赖 adaptive b* 的正确性。作者必须以 from-scratch seed 42 重跑主表，否则核心结论无法成立。

**[AGREE] R1-W2: 多重比较未校正**
同意这是一个有效的统计关切。不过我认为其严重程度低于 R1 的评级（critical），理由是：

论文的核心 story 是 epoch confound——即 D&R 的 >95% 优势来自 multi-epoch exposure。这个发现本质上是一个 **effect size decomposition**（0.396 → 0.017），而非依赖单一 hypothesis test。即使 Bonferroni 校正使 adaptive vs. uniform 的 p=0.025 不再显著，epoch confound 作为观察性发现的逻辑链条（Table 1 的 epoch-matched 对照）仍然成立。

但对于 adaptive b* 的 method claim，R1 的批评完全正确：如果 p=0.025 在校正后不显著（结合 W1 的 seed 42 问题），方法贡献的统计支撑就更加薄弱。建议降为 [major] 而非 [critical]，因为 epoch confound 分析不受此影响。

**[AGREE] R1-W3: α_eff proxy 质量偏弱**
完全同意。我在自己的审稿中也将此列为 W3（should-fix）。r=0.70 仅解释 49% 方差，且负回归偏差（β≈-0.031，Appendix K Table 10）导致系统性偏保守。

补充一点：Appendix K 报告 α_eff 在 B=1 时仅有 5 个离散值（{0, 0.25, 0.5, 0.75, 1.0}），这与 R1-W7 的 per-batch granularity 问题相互关联。proxy 的低质量加上粗粒度离散化，使得 dual constraint 的理论优雅性在实践中大打折扣。作者需要分析 51% 未解释方差的主要来源——是检测器 noise、batch sampling variance，还是 α_eff 定义本身的局限？

**[AGREE] R1-W4: Self-contamination 生态效度有限**
同意，且我在自己的审稿中将此作为 W1 (major) 的核心要素之一。Appendix O (Table 12) 的 cross-model transfer 结果确实令人担忧——Llama-3.2-3B 上 MMLU 微升而 HellaSwag 微降，且论文因"architecture differences"省略了 PPL 比较，使得这个实验几乎无法验证方法的跨模型有效性。

不过我对 R1 所述"Δ=+0.20 退化"需要求证。从 Table 12 我看到的是 mixed results（一升一降），而非单一方向的 +0.20 退化。如果 R1 指的是某个特定 metric 的退化，请明确是哪个。但这不影响 self-contamination 限制的总体判断——这是论文最大的外部效度问题。

**[AGREE] R1-W5: 下游任务零改善**
完全同意。我在自己的审稿中将此列为 N2 (critical/must-fix)。Table 3 显示所有 downstream benchmarks |Δ| ≤ 0.01 且方向不一致。§6 的解释（"PPL improvements operate in a regime that standard benchmarks cannot resolve"）存在循环论证风险。如果一个 pretraining method 无法在任何 downstream task 上产生可测量的改善，其实用价值论证就需要更强的支撑——例如在更大模型上的证据，或更精细的评估方式。

**[REBUT] R1-W6: 适用范围描述部分过度**
部分同意，但 R1 的表述有两处不够准确：

1. **"仅 ρ≥0.4"**：方法在 ρ=0.4 和 ρ=0.6 均有效（§5.2 报告 ρ=0.6 时 Δ=-0.032, paired t=−5.4, p=0.002），但在 ρ=0.2 失效（Appendix N: +0.046 PPL 退化）。所以"ρ≥0.4"大致正确。但 ρ=0.3 的缺失确实是一个重要的 gap，因为这是方法有效与否的临界区间。

2. **"1.7B+ 效果反转"**：这个表述过强。§5.3 报告 1.7B 时 in-distribution PPL 仍有改善（Δ=-0.013），只是 OOD 不一致（OWT Δ=-0.006 vs. Wiki Δ=+0.013）。"效果反转"暗示方法有害，但实际是"效果缩小且方向不稳定"。严格说是 **diminished and inconsistent**，非 **reversed**。

但 R1 的核心关切——Abstract/Introduction 的范围远超实际验证范围——我完全同意。论文声称分析"when, why, and how detect-and-reweight works"，但实际验证仅覆盖 ρ ∈ {0.4, 0.6}（有效范围），0.6B（主力），1.7B（弱化），单一数据集，单一污染类型。这种 scope mismatch 是真实的论文定位问题。

**[AGREE] R1-W7: Per-batch B=4 下 dual constraint 统计可靠性**
同意这是一个合理的技术关切。B=4 时 α_eff(0) 仅有 {0, 0.25, 0.5, 0.75, 1.0} 五个可能值，dual constraint 在这种粗粒度下的行为确实缺乏分析。论文提到 gradient accumulation 后有效 batch size 为 B_eff=16，但 §3.2 的 Algorithm 1 (Appendix B) 似乎是在 micro-batch 级别操作而非 accumulated batch 级别。R1-Q2 提出的在 B=16 级别计算 α_eff 的建议值得探索。

**[AGREE] R1-W8: 关键证据仅在附录**
同意。Proxy validation (r=0.70, Appendix K)、seed 42 artifact (Appendix P)、ρ=0.2 失效 (Appendix N) 是影响论文核心 claims 可信度的关键信息，不应仅在附录中呈现。尤其是 seed 42 artifact——如果主表结果受此影响，读者有权在正文中被告知。

---

### Questions 回应

**Q1（排除/替换 seed 42 后的主表结果）**
强烈支持。如我在 W1 回应中分析的，seed 42 artifact 可能使 adaptive vs. uniform 的 Δ 从 -0.014 缩小到约 -0.002。这是决定论文方法贡献是否成立的关键实验。

**Q2（gradient accumulation 级别 B=16 计算 α_eff）**
很好的建议。在 accumulated batch（16 samples）级别计算 α_eff 会将离散值从 5 个增加到 17 个，可能显著改善 proxy 质量。这也与 §5.3 中报告的 "the adaptive advantage monotonically increases across B" 一致——更大的 effective batch 确实帮助 dual constraint。

**Q3（ρ=0.3 表现如何）**
关键缺失。ρ=0.2 失效而 ρ=0.4 有效，ρ=0.3 是理解方法适用边界的核心数据点。这个实验成本不高（与现有实验相同设置，仅改变 ρ），缺失不可接受。

**Q4（简单固定 b=0.6 是否足够）**
好问题。从 Table 2 数据来看，Adaptive b* mean 跨 3 seeds 为 17.620，而 Golden Ratio 基线（固定 b）为 17.250（但这可能是不同设置）。需要看 §5.3 中 b 的 sensitivity：论文报告 grid search 在 b=0.6 附近最优。如果固定 b=0.6 能达到类似效果，dual-constraint 框架的 added value 就更加有限。这直接关系到方法贡献的必要性论证。

**Q5（soft label 版 α_eff）**
有价值的方法论建议。当前 α_eff 使用二值化 r_i = 1(q_i ≤ 0.5) 将连续检测分数离散化，丢失了大量信息。用 soft label (1 - q_i) 替代 r_i 可能同时改善 proxy 质量和 granularity。但需注意这会改变 α_eff 的语义——从"effective proportion of real samples"变为"expected realness"——需要重新推导 Proposition 1-2 的单调性保证。

---

### Missing References 回应

**[AGREE] Influence function-based data valuation (Pruthi et al., 2020)**
值得在 §2 Related Work 中提及。虽然 provenance-based weighting 和 influence-based valuation 的出发点不同（前者基于来源标签，后者基于对损失的贡献），但作为 instance-level data valuation 的另一范式，引用有助于定位本文方法在更广泛的 data selection 文献中的位置。不过并非关键遗漏。

**[AGREE] DRO (Sagawa et al., 2020)**
同意应该引用。DRO 的 worst-group 优化目标可以被视为 reweighting 的一个特例，且论文的 dual constraint（quality floor + stability ceiling）在精神上与 DRO 的 robust optimization 有一定相似性。不引用不影响论文完整性，但引用会加强 Related Work 的全面性。

**[AGREE] PPL-downstream gap (Tay et al., 2022)**
强烈同意。鉴于论文 §6 和 Table 3 的 downstream null result，这个引用几乎是必需的。PPL 与 downstream performance 的脱钩是已有文献广泛讨论的现象，论文应在 Discussion 中引用此文献来 contextualize 自己的发现，而非仅用"benchmark sensitivity threshold"作为解释。这是最重要的遗漏引用。

---

### 与 Reviewer 1 评分的比较

| 维度 | R1 | R2 (我) | 差异说明 |
|------|-----|---------|---------|
| Overall | 3.0 | 3.0 | 一致：Findings 水准 |
| Soundness | 3.0 | 3.5 | 我初始给 3.5，但考虑 R1 提出的 seed 42 artifact 问题后，认为 3.0 更合理。**下调至 3.0**。 |
| Excitement | 3.0 | 2.5 | 我认为 R1 给高了。方法增量式（同一公式 w=(1-q)^b），downstream 零改善，适用范围窄。Epoch confound 是有用的 negative finding，但不足以支撑 Excitement 3。 |
| Confidence | 4 | 4 | 一致 |

### 总结

R1 的审稿质量很高，尤其是 W1（seed 42 artifact）和 W6（scope mismatch）两个问题我未在首轮充分展开。seed 42 问题实际上比我初始评估更严重——它可能使 adaptive b* 的核心数值贡献从 Δ=-0.014 缩小到接近零。结合 downstream null result (W5/我的 N2)，方法贡献的 evidence base 非常薄弱。

论文的持久价值在于 epoch confound 发现（不受 seed 42 影响，因为这是 D&R 的 confound 而非 adaptive 的），以及 detector requirements 分析。但作为一篇同时声称分析和方法贡献的论文，方法部分的统计支撑需要大幅加强。

**修正后评分：Overall 3.0, Soundness 3.0, Excitement 2.5, Confidence 4**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-22T17:11:13.932238+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-22T17:11:13.932685+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 948 · 2026-05-22T17:11:13.983710+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T16:54:40.097174+00:00\", \"completed_at\": \"2026-05-22T16:58:44.358080+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"Display items 分布不均：Page 5 大段讨论 Table 1、Table 2、Figure 2 的结果，但三个 display items 全部堆叠在 Page 6。建议将 Table 1（较小）提前到 Page 5 底部，减轻 Page 6 拥挤感并让读者在阅读结果讨论时同时看到数据\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"整页纯文本（§5.3 Hyperparameter Sensitivity + §6 Discussion 开头），无任何 figure/table/equation 穿插。Discussion 中多处引用 Appendix 表格（Table 5、Appendix G 等），主文读者无法即时验证。考虑将一个关键 sensitivity 分析图（如 Figure 3 的简化版）移入主文\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 概览图中的彩色方框（蓝/绿/橄榄）颜色区分度足够，但橄榄色（F3）与绿色（F2）在灰度打印下可能难以区分。建议用不同底纹或边框样式辅助区分\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 使用蓝色和橙色双线，色盲友好。但两条线仅靠颜色区分，缺少不同 marker shape 或 line style，灰度打印时可读性下降\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 数值精度一致（均保留 3 位小数 ± 标准差），最优值加粗标注，格式规范。Booktabs 风格正确\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 downstream benchmark 结果格式正确，bold 标注最优值。但表格标题 \\\"All differences within standard error\\\" 暗示效果不显著——审稿人可能据此质疑 downstream 实验的价值\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Algorithm 1 伪代码框排版整洁，行号清晰。Appendix 整体排版紧凑但未溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"末页（Appendix Q）底部约 1/3 空白。作为 appendix 末页可接受，但若需要空间可将部分 appendix 内容移至此处\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-22T17:11:13.984120+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-22T17:12:32.352119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-22T17:12:32.352883+00:00_

1	issues:
2	- id: "R8-C1"
3	  summary: "效果规模极小（Δ=-0.020 PPL / 0.11%），无下游任务改善"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 8
8	  last_seen_round: 9
9	  mentions:
10	    - round: 8
11	      reviewers: [1, 2]
12	      note: "两位 Reviewer 均标 critical。Table 7 下游任务均值完全相同（0.5414）。PPL 微小改进未转化为任何可测量的任务性能提升。"
13	    - round: 9
14	      reviewers: [1, 2]
15	      note: "仍为 critical。Round 9 reframe 为 analysis paper 后效果规模问题仍存在——分析论文需要解释 WHY 效果小，而非回避。Table 7 下游零改善需进入正文 Discussion。"
16	  action_items:
17	    - round: 9
18	      action: "Discussion 扩展：加入 downstream 零改善分析段落 + Table 引入正文 + narrow residual framing"
19	      assigned_to: paper_agent
20	      status: completed
21	  resolution: "Discussion 已包含 downstream 零改善分析段落、Table 3 在正文、narrow residual framing 解释。Paper Agent Round 9 reframe 完成。"
22	  resolution_round: 10
23	
24	- id: "R8-C2"
25	  summary: "N=3 seeds 统计功效不足（df=2 下 paired t-test 可靠性有限）"
26	  category: experiment
27	  severity: critical
28	  status: resolved
29	  first_raised_round: 8
30	  last_seen_round: 9
31	  mentions:
32	    - round: 8
33	      reviewers: [1, 2]
34	      note: "R1 标 critical，R2 同意。df=2 对 outlier 极度敏感，未做多重比较校正。seed 42 存在 checkpoint resume artifact（Appendix O）。"
35	    - round: 9
36	      reviewers: [1, 2]
37	      note: "仍为 critical。Bootstrap CI 可部分缓解但不解决根本问题。Analysis paper framing 下，N=3 的统计局限需在 Limitations 诚实承认。"
38	  action_items:
39	    - round: 9
40	      action: "Agent 从现有 3-seed 数据计算 bootstrap CI（BCa 法），加入关键表格"
41	      assigned_to: main_agent
42	      status: completed
43	    - round: 9
44	      action: "Limitations 中明确承认 N=3 的统计功效限制"
45	      assigned_to: paper_agent
46	      status: completed
47	  resolution: "Limitations 新增 N=3 seeds 统计功效限制承认。Bootstrap CI 已在关键表格中。关键发现正在升级到 3-seed（seed456 系列运行中）。"
48	  resolution_round: 10
49	
50	- id: "R8-C3"
51	  summary: "相对 Drayson et al. (2025) 方法论新颖性不足（同一公式，仅改变 b 选择方式）"
52	  category: framing
53	  severity: critical
54	  status: resolved
55	  first_raise
…[truncated 8663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T17:14:30.534233+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n- id: \"R8-C1\"\n  summary: \"效果规模极小（Δ=-0.020 PPL / 0.11%），无下游任务改善\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均标 critical。Table 7 下游任务均值完全相同（0.5414）。PPL 微小改进未转化为任何可测量的任务性能提升。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍为 critical。Round 9 reframe 为 analysis paper 后效果规模问题仍存在——分析论文需要解释 WHY 效果小，而非回避。Table 7 下游零改善需进入正文 Discussion。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 fresh review 再次标 critical。Table 3 显示 |Δ|≤0.01 across all benchmarks，方向不一致。§6 Discussion 已讨论但仅 ~4 行，R2 指出 '循环论证' 风险：如果效果微小到测不出，实际价值论证就缺乏支撑。R1 补充 PPL→downstream 阈值效应未讨论。两位 Reviewer 共识：需 7B+ 验证或更细粒度评估。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 扩展：加入 downstream 零改善分析段落 + Table 引入正文 + narrow residual framing\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"N=3 seeds 统计功效不足（df=2 下 paired t-test 可靠性有限）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 同意。df=2 对 outlier 极度敏感，未做多重比较校正。seed 42 存在 checkpoint resume artifact（Appendix O）。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍为 critical。Bootstrap CI 可部分缓解但不解决根本问题。Analysis paper framing 下，N=3 的统计局限需在 Limitations 诚实承认。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 fresh review 再次标 critical（R1）/ major（R2 交叉后同意严重性）。Seed 42 artifact 问题升级：Appendix P 显示 resume artifact 使 seed 42 的 Δ 从 -0.005 膨胀到 -0.041（8倍）。R2 推算替换后 3-seed mean Δ 从 -0.014 缩小到 -0.002，核心比较可能完全由 artifact 驱动。\"\n  action_items:\n    - round: 9\n      action: \"Agent 从现有 3-seed 数据计算 bootstrap CI（BCa 法），加入关键表格\"\n      assigned_to: main_agent\n      status: completed\n    - round: 9\n      action: \"Limitations 中明确承认 N=3 的统计功效限制\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C3\"\n  summary: \"相对 Drayson et al. (2025) 方法论新颖性不足（同一公式，仅改变 b 选择方式）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 标 critical，R1 同意。双约束中 ESS 是标准工具（Kish 1965），α_eff 阈值为经验性选择。技术深度有限。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Round 9 reframe 后定位为 analysis paper，adaptive b* 降为 Tool/Contribution #4。但 Method §3 仍占 ~2.5 页，与 analysis 定位不匹配。需压缩 Method，将空间让给 Discussion。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 fresh review 仍标 critical (R2-N1, R1 AGREE)。尽管 Method 已压缩至 ~1.5 页，论文仍同时声称分析和方法贡献。§1 四条 contribution 混合观察型和方法型。R1/R2 共识：真正价值在分析发现，adaptive b* 应明确为 practical corollary。\"\n  action_items:\n    - round: 9\n      action: \"Method §3 压缩 ~1 页：Algorithm box → appendix，§3.3 constraint stats → Results，§3.4 hyperparameters 精简\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"自我污染设定（generator=trainee）生态效度受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均指出。Cross-model transfer（Appendix N）仅单 seed 且结果 mixed。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍为 warning。analysis paper framing 下此设定可作为 controlled testbed 合理化，但需在 Discussion 中讨论 cross-model 场景。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 仍标 major (R1-W4, R2-W1)。Limitations 中已讨论但 Appendix O cross-model 结果（Llama-3.2-3B MMLU+1.57pp, HellaSwag-0.60pp）无法验证方法跨模型有效性。R2 指出 PPL 比较被省略使该实验几乎无说服力。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 中加入 self-contamination 作为 controlled testbed 的合理性论证 + cross-model 挑战讨论\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Discussion 过于单薄（约 11 行），对分析型论文远远不够\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 标 critical，R1 在交叉中未明确回应但其 Excitement 2.5/5 暗示认同。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Round 9 升级为 critical。需扩展到 ~1 页。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未被提及。Discussion 已扩展至 50+ 行，覆盖 5 个主题段落。Reviewer 在 S3 中认可 Discussion 的诚实性和深度。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 从 11 行扩展到 ~1 页，5 个主题\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Discussion 从 11 行扩展到 50+ 行，覆盖 epoch confound implications / when uniform beats reweighting / downstream zero-improvement / effect size / theoretical limitations。Round 10 两位 Reviewer 均未再提此问题。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"论文定位模糊（分析论文 vs 方法论文），双重定位削弱说服力\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 明确指出。若为方法论文，效果太小；若为分析论文，adaptive b* 的篇幅占比过高。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Round 9 reframe 已明确为 analysis paper，但 Method §3 仍占 ~2.5 页暴露残留双重定位。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 标 major (R2-W2, R1 AGREE)。Method 已压缩但 §3 仍占 ~1.5 页。Abstract 第一句强调 analysis 但随后引入 method。四条 contribution 混合观察型和方法型。R1 建议压缩 §3 至半页并扩展 epoch confound 讨论。\"\n  action_items:\n    - round: 9\n      action: \"Method 压缩 + analysis positioning 强化\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"Epoch-matched 比较可能引入 LR schedule confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1 指出完全控制 epoch+LR 后 D&R 反而劣于 uniform。\"\n    - round: 9\n      reviewers: [1]\n      note: \"LR confound 实验已完成并写入 §5.1。Reviewer 认可。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未被提及。§5.1 独立 LR schedule 复现（Δ=0.006）被 R1 在 S1 中认可为精良设计。\"\n  action_items:\n    - round: 8\n      action: \"LR confound 对照实验（独立 2533-step linear schedule）\"\n      assigned_to: main_agent\n      status: completed\n  resolution: \"LR confound 实验确认 epoch confound。已写入 §5.1。Round 10 Reviewers 认可。\"\n  resolution_round: 9\n\n- id: \"R8-W5\"\n  summary: \"检测器覆盖面窄（仅 3 个检测器，2 个家族）\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"缺少 fine-tuned 神经分类器、DetectGPT 等。\"\n    - round: 9\n      reviewers: [1]\n      note: \"3 检测器已支持分析但承认覆盖面有限。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未单独提及。Limitations 已列出未测试检测器类型。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 中明确列出未测试的检测器类型\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Limitations 已列出 RoBERTa-based/DetectGPT 未测试。Round 10 未再被标记。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"α_eff 代理质量中等（r=0.70，仅解释 49% 方差）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"未讨论 51% 未解释方差的来源及对方法可靠性的影响。\"\n    - round: 9\n      reviewers: [1]\n      note: \"仍为 warning。analysis paper 下可在 Discussion 理论局限部分讨论。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 升级至 major (R1-W3, R2 交叉后 AGREE 升级)。Discussion 已有 'Limitations of α_eff' 段落，但 R1 指出仍未分析 51% 未解释方差的来源（检测器噪声 vs batch sampling vs 二值化）。R2 补充：B=4 时 α_eff(0) 仅 5 个离散值与 W7 per-batch granularity 问题关联。两位 Reviewer 共识：这是方法核心假设的验证缺口，非 minor 精度问题。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 理论局限段落中讨论 α_eff 49% 未解释方差\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"ρ=0.2 失败和 1.7B 效果减弱限制方法实用范围\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"analysis paper framing 下，scope 限制本身是 finding。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 标 major (R1-W6, R2-W1)。Limitations 已覆盖但 R1 指出 ρ=0.3 关键中间点完全缺失。R2 修正 R1 措辞：1.7B 是 'diminished and inconsistent' 非 'reversed'（holdout 仍有 Δ=-0.013，OOD 方向不稳定）。两位 Reviewer 共识：Abstract/Introduction 的 claim 范围远超实际验证范围。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 确认覆盖 ρ=0.2 失败 + 1.7B 效果减弱\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W8\"\n  summary: \"B=4 离散空间与连续理论框架的脱节\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"α_eff 仅取 5 个离散值，bisection 在 5 点上运行。\"\n    - round: 9\n      reviewers: [1]\n      note: \"修正 discrete/continuous 表述后该问题解决。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 discrete/continuous 表述问题未被提及（已修正）。但 B=4 granularity 作为 R10-W1 新 issue 独立提出。\"\n  action_items:\n    - round: 9\n      action: \"修正 §3.3 line 77 α_eff discrete/continuous 表述\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"method.tex discrete/continuous 表述已修正。Round 10 未再提及。\"\n  resolution_round: 10\n\n- id: \"R8-I1\"\n  summary: \"Conclusion 过于简短（~3 行），缺乏前瞻性讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"与 Discussion 问题相关。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未被提及。Conclusion 已扩展。\"\n  action_items:\n    - round: 10\n      action: \"Conclusion 新增前瞻句\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Conclusion 已扩展。Round 10 未再提及。\"\n  resolution_round: 10\n\n- id: \"R8-I2\"\n  summary: \"下游任务负面结果仅在附录，未在正文讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Table 7 显示下游无改善，应在正文 Discussion 中讨论。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍未解决。Round 9 明确要求 Table 7 进正文。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未单独提及此问题。Table 3 已在正文 Discussion，downstream 零改善有专门段落。R2 在 S3 中认可 Discussion 的诚实性。\"\n  action_items:\n    - round: 9\n      action: \"Table 7 移入正文 Discussion + 分析段落\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Table 已在正文 Discussion。Round 10 未再提及位置问题（内容深度问题归入 R8-C1）。\"\n  resolution_round: 10\n\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 纳入主表，核心比较可能由 artifact 驱动\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 首提 critical，R2 交叉后 AGREE 并加强：Appendix P 承认 seed 42 adaptive 使用 checkpoint-resumed run（前 ~1000 步超参不同），in-distribution Δ 被膨胀 8 倍（-0.041 vs -0.005 from-scratch）。R2 推算替换后 3-seed mean Δ 从 -0.014 缩小到 ~-0.002。paired t=-6.2, p=0.025 可信度严重存疑。两位 Reviewer 共识：必须以 from-scratch seed 42 重跑主表。\"\n  action_items:\n    - round: 10\n      action: \"以 from-scratch seed 42 替换 checkpoint-resumed seed 42 重跑主表 (Table 1, Table 2)\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正（≥5 个检验，p=0.025 Bonferroni 后不显著）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 交叉后降为 major（理由：epoch confound 作为 effect size decomposition 不依赖 hypothesis test）。两位 Reviewer 共识：对 adaptive b* method claim，Bonferroni 校正后 p=0.025 不再显著，方法贡献统计支撑薄弱。\"\n  action_items:\n    - round: 10\n      action: \"报告 Bonferroni/Holm 校正 p 值；或用 bootstrap CI 替代\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Per-batch B=4 下 dual constraint 统计可靠性存疑（b* batch 间分布未报告）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 首提 minor，R2 AGREE。B=4 下 α_eff(0) 仅 5 个离散值，方差极大。Algorithm 1 在 micro-batch 级别操作（非 accumulated batch）。b* batch 间分布未报告。R2 补充：在 B=16 级别计算 α_eff 可将离散值从 5 增至 17，可能显著改善 proxy 质量。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"关键证据（proxy r=0.70, seed 42 artifact, ρ=0.2 分析）仅在附录\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 首提 minor，R2 AGREE。影响核心 claims 可信度的关键信息（proxy validation Appendix K, seed 42 artifact Appendix P, ρ=0.2 失效 Appendix N）不应仅在附录。尤其 seed 42 artifact 影响主表结果，读者有权在正文中被告知。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中（应在 OpenReview 表单）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 首提 minor，R1 AGREE。EMNLP 2026/ARR 规定 Responsible NLP Checklist 应在 OpenReview submission form 中填写，不应在论文 PDF 中。当前 checklist 占约 1 页。移除可释放空间。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n- id: \"R8-C1\"\n  summary: \"效果规模极小（Δ=-0.020 PPL / 0.11%），无下游任务改善\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均标 critical。Table 7 下游任务均值完全相同（0.5414）。PPL 微小改进未转化为任何可测量的任务性能提升。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍为 critical。Round 9 reframe 为 analysis paper 后效果规模问题仍存在——分析论文需要解释 WHY 效果小，而非回避。Table 7 下游零改善需进入正文 Discussion。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 fresh review 再次标 critical。Table 3 显示 |Δ|≤0.01 across all benchmarks，方向不一致。§6 Discussion 已讨论但仅 ~4 行，R2 指出 '循环论证' 风险：如果效果微小到测不出，实际价值论证就缺乏支撑。R1 补充 PPL→downstream 阈值效应未讨论。两位 Reviewer 共识：需 7B+ 验证或更细粒度评估。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 扩展：加入 downstream 零改善分析段落 + Table 引入正文 + narrow residual framing\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"N=3 seeds 统计功效不足（df=2 下 paired t-test 可靠性有限）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 同意。df=2 对 outlier 极度敏感，未做多重比较校正。seed 42 存在 checkpoint resume artifact（Appendix O）。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍为 critical。Bootstrap CI 可部分缓解但不解决根本问题。Analysis paper framing 下，N=3 的统计局限需在 Limitations 诚实承认。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 fresh review 再次标 critical（R1）/ major（R2 交叉后同意严重性）。Seed 42 artifact 问题升级：Appendix P 显示 resume artifact 使 seed 42 的 Δ 从 -0.005 膨胀到 -0.041（8倍）。R2 推算替换后 3-seed mean Δ 从 -0.014 缩小到 -0.002，核心比较可能完全由 artifact 驱动。\"\n  action_items:\n    - round: 9\n      action: \"Agent 从现有 3-seed 数据计算 bootstrap CI（BCa 法），加入关键表格\"\n      assigned_to: main_agent\n      status: completed\n    - round: 9\n      action: \"Limitations 中明确承认 N=3 的统计功效限制\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C3\"\n  summary: \"相对 Drayson et al. (2025) 方法论新颖性不足（同一公式，仅改变 b 选择方式）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 标 critical，R1 同意。双约束中 ESS 是标准工具（Kish 1965），α_eff 阈值为经验性选择。技术深度有限。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Round 9 reframe 后定位为 analysis paper，adaptive b* 降为 Tool/Contribution #4。但 Method §3 仍占 ~2.5 页，与 analysis 定位不匹配。需压缩 Method，将空间让给 Discussion。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 fresh review 仍标 critical (R2-N1, R1 AGREE)。尽管 Method 已压缩至 ~1.5 页，论文仍同时声称分析和方法贡献。§1 四条 contribution 混合观察型和方法型。R1/R2 共识：真正价值在分析发现，adaptive b* 应明确为 practical corollary。\"\n  action_items:\n    - round: 9\n      action: \"Method §3 压缩 ~1 页：Algorithm box → appendix，§3.3 constraint stats → Results，§3.4 hyperparameters 精简\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"自我污染设定（generator=trainee）生态效度受限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均指出。Cross-model transfer（Appendix N）仅单 seed 且结果 mixed。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍为 warning。analysis paper framing 下此设定可作为 controlled testbed 合理化，但需在 Discussion 中讨论 cross-model 场景。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 仍标 major (R1-W4, R2-W1)。Limitations 中已讨论但 Appendix O cross-model 结果（Llama-3.2-3B MMLU+1.57pp, HellaSwag-0.60pp）无法验证方法跨模型有效性。R2 指出 PPL 比较被省略使该实验几乎无说服力。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 中加入 self-contamination 作为 controlled testbed 的合理性论证 + cross-model 挑战讨论\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Discussion 过于单薄（约 11 行），对分析型论文远远不够\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 标 critical，R1 在交叉中未明确回应但其 Excitement 2.5/5 暗示认同。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Round 9 升级为 critical。需扩展到 ~1 页。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未被提及。Discussion 已扩展至 50+ 行，覆盖 5 个主题段落。Reviewer 在 S3 中认可 Discussion 的诚实性和深度。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 从 11 行扩展到 ~1 页，5 个主题\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Discussion 从 11 行扩展到 50+ 行，覆盖 epoch confound implications / when uniform beats reweighting / downstream zero-improvement / effect size / theoretical limitations。Round 10 两位 Reviewer 均未再提此问题。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"论文定位模糊（分析论文 vs 方法论文），双重定位削弱说服力\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 明确指出。若为方法论文，效果太小；若为分析论文，adaptive b* 的篇幅占比过高。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Round 9 reframe 已明确为 analysis paper，但 Method §3 仍占 ~2.5 页暴露残留双重定位。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 标 major (R2-W2, R1 AGREE)。Method 已压缩但 §3 仍占 ~1.5 页。Abstract 第一句强调 analysis 但随后引入 method。四条 contribution 混合观察型和方法型。R1 建议压缩 §3 至半页并扩展 epoch confound 讨论。\"\n  action_items:\n    - round: 9\n      action: \"Method 压缩 + analysis positioning 强化\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"Epoch-matched 比较可能引入 LR schedule confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1 指出完全控制 epoch+LR 后 D&R 反而劣于 uniform。\"\n    - round: 9\n      reviewers: [1]\n      note: \"LR confound 实验已完成并写入 §5.1。Reviewer 认可。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未被提及。§5.1 独立 LR schedule 复现（Δ=0.006）被 R1 在 S1 中认可为精良设计。\"\n  action_items:\n    - round: 8\n      action: \"LR confound 对照实验（独立 2533-step linear schedule）\"\n      assigned_to: main_agent\n      status: completed\n  resolution: \"LR confound 实验确认 epoch confound。已写入 §5.1。Round 10 Reviewers 认可。\"\n  resolution_round: 9\n\n- id: \"R8-W5\"\n  summary: \"检测器覆盖面窄（仅 3 个检测器，2 个家族）\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"缺少 fine-tuned 神经分类器、DetectGPT 等。\"\n    - round: 9\n      reviewers: [1]\n      note: \"3 检测器已支持分析但承认覆盖面有限。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未单独提及。Limitations 已列出未测试检测器类型。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 中明确列出未测试的检测器类型\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Limitations 已列出 RoBERTa-based/DetectGPT 未测试。Round 10 未再被标记。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"α_eff 代理质量中等（r=0.70，仅解释 49% 方差）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"未讨论 51% 未解释方差的来源及对方法可靠性的影响。\"\n    - round: 9\n      reviewers: [1]\n      note: \"仍为 warning。analysis paper 下可在 Discussion 理论局限部分讨论。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 升级至 major (R1-W3, R2 交叉后 AGREE 升级)。Discussion 已有 'Limitations of α_eff' 段落，但 R1 指出仍未分析 51% 未解释方差的来源（检测器噪声 vs batch sampling vs 二值化）。R2 补充：B=4 时 α_eff(0) 仅 5 个离散值与 W7 per-batch granularity 问题关联。两位 Reviewer 共识：这是方法核心假设的验证缺口，非 minor 精度问题。\"\n  action_items:\n    - round: 9\n      action: \"Discussion 理论局限段落中讨论 α_eff 49% 未解释方差\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"ρ=0.2 失败和 1.7B 效果减弱限制方法实用范围\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"analysis paper framing 下，scope 限制本身是 finding。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Round 10 标 major (R1-W6, R2-W1)。Limitations 已覆盖但 R1 指出 ρ=0.3 关键中间点完全缺失。R2 修正 R1 措辞：1.7B 是 'diminished and inconsistent' 非 'reversed'（holdout 仍有 Δ=-0.013，OOD 方向不稳定）。两位 Reviewer 共识：Abstract/Introduction 的 claim 范围远超实际验证范围。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 确认覆盖 ρ=0.2 失败 + 1.7B 效果减弱\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W8\"\n  summary: \"B=4 离散空间与连续理论框架的脱节\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"α_eff 仅取 5 个离散值，bisection 在 5 点上运行。\"\n    - round: 9\n      reviewers: [1]\n      note: \"修正 discrete/continuous 表述后该问题解决。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 discrete/continuous 表述问题未被提及（已修正）。但 B=4 granularity 作为 R10-W1 新 issue 独立提出。\"\n  action_items:\n    - round: 9\n      action: \"修正 §3.3 line 77 α_eff discrete/continuous 表述\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"method.tex discrete/continuous 表述已修正。Round 10 未再提及。\"\n  resolution_round: 10\n\n- id: \"R8-I1\"\n  summary: \"Conclusion 过于简短（~3 行），缺乏前瞻性讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"与 Discussion 问题相关。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未被提及。Conclusion 已扩展。\"\n  action_items:\n    - round: 10\n      action: \"Conclusion 新增前瞻句\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Conclusion 已扩展。Round 10 未再提及。\"\n  resolution_round: 10\n\n- id: \"R8-I2\"\n  summary: \"下游任务负面结果仅在附录，未在正文讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Table 7 显示下游无改善，应在正文 Discussion 中讨论。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"仍未解决。Round 9 明确要求 Table 7 进正文。\"\n    - round: 10\n      reviewers: []\n      note: \"Round 10 未单独提及此问题。Table 3 已在正文 Discussion，downstream 零改善有专门段落。R2 在 S3 中认可 Discussion 的诚实性。\"\n  action_items:\n    - round: 9\n      action: \"Table 7 移入正文 Discussion + 分析段落\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"Table 已在正文 Discussion。Round 10 未再提及位置问题（内容深度问题归入 R8-C1）。\"\n  resolution_round: 10\n\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 纳入主表，核心比较可能由 artifact 驱动\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 首提 critical，R2 交叉后 AGREE 并加强：Appendix P 承认 seed 42 adaptive 使用 checkpoint-resumed run（前 ~1000 步超参不同），in-distribution Δ 被膨胀 8 倍（-0.041 vs -0.005 from-scratch）。R2 推算替换后 3-seed mean Δ 从 -0.014 缩小到 ~-0.002。paired t=-6.2, p=0.025 可信度严重存疑。两位 Reviewer 共识：必须以 from-scratch seed 42 重跑主表。\"\n  action_items:\n    - round: 10\n      action: \"以 from-scratch seed 42 替换 checkpoint-resumed seed 42 重跑主表 (Table 1, Table 2)\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正（≥5 个检验，p=0.025 Bonferroni 后不显著）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 标 critical，R2 交叉后降为 major（理由：epoch confound 作为 effect size decomposition 不依赖 hypothesis test）。两位 Reviewer 共识：对 adaptive b* method claim，Bonferroni 校正后 p=0.025 不再显著，方法贡献统计支撑薄弱。\"\n  action_items:\n    - round: 10\n      action: \"报告 Bonferroni/Holm 校正 p 值；或用 bootstrap CI 替代\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Per-batch B=4 下 dual constraint 统计可靠性存疑（b* batch 间分布未报告）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 首提 minor，R2 AGREE。B=4 下 α_eff(0) 仅 5 个离散值，方差极大。Algorithm 1 在 micro-batch 级别操作（非 accumulated batch）。b* batch 间分布未报告。R2 补充：在 B=16 级别计算 α_eff 可将离散值从 5 增至 17，可能显著改善 proxy 质量。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"关键证据（proxy r=0.70, seed 42 artifact, ρ=0.2 分析）仅在附录\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 首提 minor，R2 AGREE。影响核心 claims 可信度的关键信息（proxy validation Appendix K, seed 42 artifact Appendix P, ρ=0.2 失效 Appendix N）不应仅在附录。尤其 seed 42 artifact 影响主表结果，读者有权在正文中被告知。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中（应在 OpenReview 表单）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 首提 minor，R1 AGREE。EMNLP 2026/ARR 规定 Responsible NLP Checklist 应在 OpenReview submission form 中填写，不应在论文 PDF 中。当前 checklist 占约 1 页。移除可释放空间。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-22T17:14:30.637167+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 13267}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-22T17:16:42.528322+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 10 (Fresh Review)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 Long Paper (ARR)\n**Reviewers**: R1 (方法严谨性/实验/统计) + R2 (新颖性/定位/完整性/写作)\n**交叉分享**: 完成，1 轮收敛\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在含合成数据污染的 continued LM pretraining 中的有效性条件。通过 Qwen3-0.6B 上的受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），报告三个发现：(1) D&R 相对于 adaptive reweighting 的 PPL 优势中 >95% 来自 multi-epoch exposure confound；(2) 有效 reweighting 需要检测器同时具备足够 discrimination (AUC) 和良好 calibration (ECE)；(3) dual-constraint adaptive b*（α_eff ≥ τ + ESS ≥ n_min）通过 minimum intervention 原则自动选择 b，消除 grid search。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 发现有真实修正价值 [R1, R2 共识]**\nTable 1 中 D&R full (~2.4 epochs) PPL=17.278 vs. epoch-matched D&R (~1.0 epoch) PPL=17.657，差值占 D&R 优势的 ~96.7%。独立 LR schedule 复现（17.651 vs. 17.657, Δ=0.006）排除 LR 混淆。这纠正了 Drayson et al. (2025) 中的重要效果误归因，对 D&R 社区有即时实用价值。\n\n**S2. 实验设计严谨 [R1, R2 共识]**\n系统化受控实验：逐因素消融（epoch matching → detector quality → contamination level → scale），3 seeds 提供统计基础，paired t-tests 报告显著性。Random weights 对照确认检测器信号的必要性；ESS-only 消融隔离 minimum intervention 的价值。\n\n**S3. 诚实的 Discussion [R1, R2 共识]**\n§6 不回避负面发现：downstream 零改善 (Table 3)、α_eff proxy 局限 (r=0.70)、效应量极小 (Δ=-0.020)、ρ=0.2 失败。这种透明度在分析论文中增强了结论可信度。\n\n**S4. 数学框架简洁正确 [R1]**\nProposition 1-2 证明（Appendix A）利用协方差符号和加权集中性标准结论，推导正确。\n\n**S5. 附录丰富 (A-Q)，可复现性好 [R1, R2 共识]**\n实验细节充分（§4），Algorithm 1 伪代码清晰，17 个附录覆盖证明、消融、proxy 验证、practitioner guide。\n\n---\n\n## Weaknesses\n\n### Critical / Must-Fix\n\n**C1. Seed 42 checkpoint resume artifact 使主表核心比较可信度严重存疑 [R1-W1, R2 AGREE]**\nAppendix P 揭示 seed 42 的 adaptive 模型使用 checkpoint-resumed run（前 ~1,000 步超参不同），in-distribution Δ 被膨胀约 8 倍（−0.041 resume vs. −0.005 from-scratch）。R2 定量推算：替换后 3-seed mean Δ 从 −0.014 缩小到 ~−0.002，基本消失。paired t=−6.2, p=0.025 的可信度严重存疑。**必须以 from-scratch seed 42 重跑主表**，否则 adaptive b* 的方法贡献无法成立。\n\n**C2. 多重比较未校正 [R1-W2 critical, R2 降为 major]**\n6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。R2 认为 epoch confound 作为 effect size decomposition 不受影响，但对 adaptive b* method claim 的统计支撑确实不足。**需报告校正后 p 值或 bootstrap CI**。\n\n**C3. 方法新颖性不足以支撑独立贡献 [R2-N1, R1 AGREE]**\n加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)；ESS (Kish 1965) 和 α_eff 均为已有概念；dual constraint 组合是直接应用而非根本性创新。论文真正价值在分析发现，但 §1 四条 contribution 混合观察型和方法型，§3 Method 仍占 ~1.5 页，与 analysis paper 定位不匹配。**应明确定位为 analysis paper，adaptive b* 降级为 practical corollary**。\n\n**C4. Downstream task 零改善削弱实际意义 [R2-N2, R1-W5 共识]**\nTable 3 显示所有 downstream benchmarks |Δ| ≤ 0.01，方向不一致。§6 解释（\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"）存在循环论证风险。R1 指出讨论仅 ~4 行，应扩展 PPL→downstream 阈值效应分析。**需 7B+ 验证或更细粒度评估**。\n\n### Major / Should-Fix\n\n**M1. 实验规模和场景过于狭窄 [R2-W1, R1-W6 共识]**\n仅 0.6B/1.7B 模型，self-contamination，单一数据集 (FineWeb)，单一污染类型 (continuation)。ρ=0.3 关键中间点完全缺失。1.7B 效果减弱且 OOD 方向不稳定（holdout Δ=-0.013, Wiki Δ=+0.013）。Abstract/Introduction 的 claim 范围（\"web corpora at scale\"）远超实际验证范围（ρ∈{0.4, 0.6}, ≤1.7B, self-contamination）。\n\n**M2. 论文定位仍存在模糊性 [R2-W2, R1 AGREE]**\nAbstract 第一句强调 analysis（\"we analyze when, why, and how\"），随后介绍 method（\"we introduce a dual-constrained formulation\"）。§3 Method ~1.5 页对 analysis paper 偏重。建议进一步压缩 §3 至 ~0.5 页（详细推导移至附录），释放空间给更深入的分析讨论。\n\n**M3. α_eff proxy 质量偏弱（r=0.70, R²=0.49）[R1-W3, R2 交叉后升级至 major]**\nα_eff 是 dual-constraint 的理论基石（bisection 目标函数），但仅解释 49% 方差。负回归偏差（β≈-0.031）导致系统性低估。§6 已有 'Limitations of α_eff' 段落，但未分析 51% 未解释方差来源（检测器噪声 vs batch sampling variance vs 二值化 r_i 信息丢失）。R2 指出 soft label 版 α_eff（用 q_i 替代二值化 r_i）可能同时改善 proxy 质量和 granularity。\n\n**M4. Self-contamination 生态效度有限 [R1-W4, R2 AGREE]**\n实际场景合成数据来自更强模型（GPT-4 等），分布差异大。Appendix O cross-model transfer（Llama-3.2-3B）结果 mixed（MMLU+1.57pp, HellaSwag-0.60pp），PPL 比较被省略，使该实验几乎无法验证方法跨模型有效性。\n\n### Minor\n\n**m1. Per-batch B=4 下 dual constraint 统计可靠性存疑 [R1-W7, R2 AGREE]**\nB=4 时 α_eff(0) 仅 {0, 0.25, 0.5, 0.75, 1.0} 五值，b* batch 间分布未报告。在 gradient accumulation 级别（B=16）计算可改善 granularity。\n\n**m2. 关键证据仅在附录 [R1-W8, R2 AGREE]**\nProxy validation (r=0.70, Appendix K)、seed 42 artifact (Appendix P)、ρ=0.2 失效 (Appendix N) 影响核心 claims 可信度，应在正文中告知读者。\n\n**m3. Responsible NLP Checklist 出现在 PDF 中 [R2-W5, R1 AGREE]**\nEMNLP 2026/ARR 规定 checklist 应在 OpenReview 表单中填写，不在论文 PDF 中。移除可释放 ~1 页空间。\n\n**m4. 效应量极小需更充分的 cost-benefit 论证 [R2-W4]**\nAdaptive vs. uniform Δ=-0.020 PPL (~0.11% relative)。应增加 cost-benefit 分析：引入检测器训练/推理/calibration 开销 vs. 获得的改善。\n\n**m5. 小格式问题 [R2]**\nρ 的 token-level vs. document-level 区分在 §3.1 定义时就应澄清；Figure 2 灰度打印可读性不足（缺 marker shape/line style）；Table 2 \"4σ\" 含义不明确。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 3.0 (Findings)**: 两位 Reviewer 独立给出相同评分，交叉后维持。\n2. **主要价值在分析而非方法**: Epoch confound 发现有修正价值，三条件系统化有实用性；adaptive b* 是增量工程贡献。\n3. **Downstream null 是最大实践弱点**: PPL 改善未转化为任何可测量的 downstream 改善。\n4. **Seed 42 artifact 必须修复**: 核心比较的统计可信度依赖于此。\n5. **规模/场景过窄**: 验证范围远不足以支撑 claim 范围。\n6. **定位应偏向 analysis paper**: §3 Method 篇幅与 analysis 定位不匹配。\n\n## Reviewer Divergence [REBUT]\n\n1. **α_eff proxy 严重性**: R1 标 major，R2 初始标 minor。交叉后 R2 倾向同意升级至 major——α_eff 是 dual-constraint 理论基石，49% 未解释方差不是 minor 精度问题。**最终共识：major**。\n\n2. **多重比较校正严重性**: R1 标 critical，R2 交叉后认为应降为 major——理由是 epoch confound 作为 effect size decomposition 不依赖 hypothesis test。**最终判定：对 epoch confound 分析不影响（major），但对 adaptive b* method claim 为 critical**。\n\n3. **1.7B 措辞**: R1 称\"效果反转\"，R2 修正为\"diminished and inconsistent\"（holdout 仍有 Δ=-0.013，OOD 方向不稳定）。**采纳 R2 措辞**。\n\n---\n\n## Questions for Authors\n\nQ1. 能否提供排除/替换 seed 42 (from-scratch) 后的主表结果？这是决定方法贡献是否成立的关键实验。\n\nQ2. ρ=0.3 表现如何？这是方法有效与否的临界区间，缺失不可接受。\n\nQ3. 在 7B+ 规模上，(a) epoch confound 发现是否仍成立？(b) PPL 改善是否能传递到 downstream？\n\nQ4. Cross-model contamination（如 GPT-4 生成）下检测器 AUC/ECE 如何变化？dual constraint 是否仍有效？\n\nQ5. 简单固定 b=0.6 是否足够？如果是，dual-constraint 框架的 added value 是什么？\n\nQ6. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i），以改善 proxy 质量？\n\nQ7. Appendix Q (Table 13) 的 practitioner decision summary 非常实用，为什么不放主文？\n\n---\n\n## Missing References\n\n1. **Tay et al. (2022)** — PPL 与 downstream performance 的非线性关系。鉴于 Table 3 的 downstream null result，此引用几乎必需，可 contextualize §6 的发现。**最重要遗漏**。\n2. **Pruthi et al. (2020)** — Influence function-based data valuation。作为 instance-level data valuation 的另一范式，有助于定位本文方法。\n3. **Llama 3 technical report (Meta, 2024)** — 大规模 pretraining 中的数据 curation pipeline，可在 §2 中作为 motivation 引用。\n4. Sagawa et al. (2020) DRO 已引用（references.bib 中存在），无需补充。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求。项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2 warnings, 6 info）\n\n### Warnings\n- **Page 5-6**: Display items 分布不均——Page 5 大段讨论 Table 1/2 和 Figure 2 的结果，但三个 display items 全部堆叠在 Page 6。建议将 Table 1（较小）提前到 Page 5 底部。\n- **Page 7**: 整页纯文本（§5.3 + §6 开头），无 figure/table/equation 穿插。多处引用 Appendix 表格，读者无法即时验证。考虑将关键 sensitivity 分析图移入主文。\n\n### Info\n- Figure 1 彩色方框在灰度打印下可能难以区分（橄榄色 vs 绿色）\n- Figure 2 双线仅靠颜色区分，缺 marker shape/line style\n- Table 2 数值精度一致，格式规范\n- Table 3 标题暗示效果不显著，审稿人可能据此质疑实验价值\n- Algorithm 1 排版整洁\n- Appendix 末页底部 ~1/3 空白\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.0 (交叉后从 3.5 下调) | 3.0 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | — | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n\n**一句话总结**: 扎实的分析工作——epoch confound 发现纠正了文献中的重要误归因，三个有效性条件有实用价值——但方法新颖性有限（同一公式 w=(1-q)^b 的工程改进）、seed 42 artifact 使核心统计推断存疑、downstream 零改善削弱实际影响力、实验规模偏小（0.6B/1.7B, self-contamination）。达到 Findings 水准，但 novelty、statistical rigor 和 impact 不足以进入主会议。\n\n**提升路径**:\n- **→ 3.5 (Borderline Conference)**: 修复 seed 42 重跑主表 + 补充 corrected p-values + 补 ρ=0.3 实验 + 明确 analysis paper 定位（压缩 §3）\n- **→ 4.0 (Conference)**: 以上 + 7B+ 规模验证 + cross-model contamination 实验 + downstream 改善（或转为负面结果论文的强定位）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 四条 contribution 的排序和权重需调整：分析发现（1-3）应更突出，adaptive b*（4）应明确为 practical corollary\n- Figure 1 概览图有效但橄榄色/绿色区分度不足\n\n### §3 Method\n- 当前 ~1.5 页对 analysis paper 仍偏重；建议压缩至 ~0.5-0.75 页，Algorithm box 和详细推导已在 Appendix\n- §3.2 中 α_eff 的 proxy 质量局限（r=0.70）应在定义处即时提示，而非仅在附录和 Discussion 中讨论\n- 二值化 r_i = 1[q_i ≤ 0.5] 丢失连续信息，soft label 替代方案值得讨论\n\n### §4 Experimental Setup\n- ρ 的 token-level vs. document-level 区分（footnote 9）应在 §3.1 定义 ρ 时即澄清\n- Self-contamination 的生态效度局限应在 Setup 结尾即预告（而非等到 §8 Limitations）\n\n### §5 Results\n- Table 1 中必须标注 seed 42 使用了 checkpoint-resumed model（当前仅在 Appendix P）\n- Display items 分布不均（全在 Page 6），建议重新布局\n- §5.3 sensitivity analysis 是好内容但 Page 7 全文字无图表，视觉节奏断裂\n\n### §6 Discussion\n- 最大改进：Discussion 已从 11 行扩展到 50+ 行，覆盖 5 个主题，质量显著提升\n- Downstream null result 讨论仍偏短（~4 行），应引用 Tay et al. (2022) contextualize PPL-downstream gap\n- Cost-benefit 分析缺失：检测器训练/推理/calibration 开销 vs. Δ=-0.020 PPL 改善\n- Practitioner decision summary (Appendix Q Table 13) 应移入主文\n\n### §7 Conclusion\n- 与 findings 匹配，前瞻性讨论已改善\n\n### §8 Limitations\n- 覆盖全面：scale、ρ range、detector coverage、N=3 seeds、self-contamination\n- 建议增加一句关于 PPL-downstream gap 的 limitation\n\n### Format\n- Responsible NLP Checklist 应从 PDF 移除（在 OpenReview 表单填写）\n- 移除后释放 ~1 页空间可用于加强 Discussion 或引入 Appendix Q 的 decision summary",
  "project": "provenance_weight_training",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 10 (Fresh Review)\n\n**论文**: \"When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\"\n**Venue**: EMNLP 2026 Long Paper (ARR)\n**Reviewers**: R1 (方法严谨性/实验/统计) + R2 (新颖性/定位/完整性/写作)\n**交叉分享**: 完成，1 轮收敛\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight (D&R) 范式在含合成数据污染的 continued LM pretraining 中的有效性条件。通过 Qwen3-0.6B 上的受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），报告三个发现：(1) D&R 相对于 adaptive reweighting 的 PPL 优势中 >95% 来自 multi-epoch exposure confound；(2) 有效 reweighting 需要检测器同时具备足够 discrimination (AUC) 和良好 calibration (ECE)；(3) dual-constraint adaptive b*（α_eff ≥ τ + ESS ≥ n_min）通过 minimum intervention 原则自动选择 b，消除 grid search。\n\n---\n\n## Strengths\n\n**S1. Epoch confound 发现有真实修正价值 [R1, R2 共识]**\nTable 1 中 D&R full (~2.4 epochs) PPL=17.278 vs. epoch-matched D&R (~1.0 epoch) PPL=17.657，差值占 D&R 优势的 ~96.7%。独立 LR schedule 复现（17.651 vs. 17.657, Δ=0.006）排除 LR 混淆。这纠正了 Drayson et al. (2025) 中的重要效果误归因，对 D&R 社区有即时实用价值。\n\n**S2. 实验设计严谨 [R1, R2 共识]**\n系统化受控实验：逐因素消融（epoch matching → detector quality → contamination level → scale），3 seeds 提供统计基础，paired t-tests 报告显著性。Random weights 对照确认检测器信号的必要性；ESS-only 消融隔离 minimum intervention 的价值。\n\n**S3. 诚实的 Discussion [R1, R2 共识]**\n§6 不回避负面发现：downstream 零改善 (Table 3)、α_eff proxy 局限 (r=0.70)、效应量极小 (Δ=-0.020)、ρ=0.2 失败。这种透明度在分析论文中增强了结论可信度。\n\n**S4. 数学框架简洁正确 [R1]**\nProposition 1-2 证明（Appendix A）利用协方差符号和加权集中性标准结论，推导正确。\n\n**S5. 附录丰富 (A-Q)，可复现性好 [R1, R2 共识]**\n实验细节充分（§4），Algorithm 1 伪代码清晰，17 个附录覆盖证明、消融、proxy 验证、practitioner guide。\n\n---\n\n## Weaknesses\n\n### Critical / Must-Fix\n\n**C1. Seed 42 checkpoint resume artifact 使主表核心比较可信度严重存疑 [R1-W1, R2 AGREE]**\nAppendix P 揭示 seed 42 的 adaptive 模型使用 checkpoint-resumed run（前 ~1,000 步超参不同），in-distribution Δ 被膨胀约 8 倍（−0.041 resume vs. −0.005 from-scratch）。R2 定量推算：替换后 3-seed mean Δ 从 −0.014 缩小到 ~−0.002，基本消失。paired t=−6.2, p=0.025 的可信度严重存疑。**必须以 from-scratch seed 42 重跑主表**，否则 adaptive b* 的方法贡献无法成立。\n\n**C2. 多重比较未校正 [R1-W2 critical, R2 降为 major]**\n6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。R2 认为 epoch confound 作为 effect size decomposition 不受影响，但对 adaptive b* method claim 的统计支撑确实不足。**需报告校正后 p 值或 bootstrap CI**。\n\n**C3. 方法新颖性不足以支撑独立贡献 [R2-N1, R1 AGREE]**\n加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)；ESS (Kish 1965) 和 α_eff 均为已有概念；dual constraint 组合是直接应用而非根本性创新。论文真正价值在分析发现，但 §1 四条 contribution 混合观察型和方法型，§3 Method 仍占 ~1.5 页，与 analysis paper 定位不匹配。**应明确定位为 analysis paper，adaptive b* 降级为 practical corollary**。\n\n**C4. Downstream task 零改善削弱实际意义 [R2-N2, R1-W5 共识]**\nTable 3 显示所有 downstream benchmarks |Δ| ≤ 0.01，方向不一致。§6 解释（\"PPL improvements operate in a regime that standard benchmarks cannot resolve\"）存在循环论证风险。R1 指出讨论仅 ~4 行，应扩展 PPL→downstream 阈值效应分析。**需 7B+ 验证或更细粒度评估**。\n\n### Major / Should-Fix\n\n**M1. 实验规模和场景过于狭窄 [R2-W1, R1-W6 共识]**\n仅 0.6B/1.7B 模型，self-contamination，单一数据集 (FineWeb)，单一污染类型 (continuation)。ρ=0.3 关键中间点完全缺失。1.7B 效果减弱且 OOD 方向不稳定（holdout Δ=-0.013, Wiki Δ=+0.013）。Abstract/Introduction 的 claim 范围（\"web corpora at scale\"）远超实际验证范围（ρ∈{0.4, 0.6}, ≤1.7B, self-contamination）。\n\n**M2. 论文定位仍存在模糊性 [R2-W2, R1 AGREE]**\nAbstract 第一句强调 analysis（\"we analyze when, why, and how\"），随后介绍 method（\"we introduce a dual-constrained formulation\"）。§3 Method ~1.5 页对 analysis paper 偏重。建议进一步压缩 §3 至 ~0.5 页（详细推导移至附录），释放空间给更深入的分析讨论。\n\n**M3. α_eff proxy 质量偏弱（r=0.70, R²=0.49）[R1-W3, R2 交叉后升级至 major]**\nα_eff 是 dual-constraint 的理论基石（bisection 目标函数），但仅解释 49% 方差。负回归偏差（β≈-0.031）导致系统性低估。§6 已有 'Limitations of α_eff' 段落，但未分析 51% 未解释方差来源（检测器噪声 vs batch sampling variance vs 二值化 r_i 信息丢失）。R2 指出 soft label 版 α_eff（用 q_i 替代二值化 r_i）可能同时改善 proxy 质量和 granularity。\n\n**M4. Self-contamination 生态效度有限 [R1-W4, R2 AGREE]**\n实际场景合成数据来自更强模型（GPT-4 等），分布差异大。Appendix O cross-model transfer（Llama-3.2-3B）结果 mixed（MMLU+1.57pp, HellaSwag-0.60pp），PPL 比较被省略，使该实验几乎无法验证方法跨模型有效性。\n\n### Minor\n\n**m1. Per-batch B=4 下 dual constraint 统计可靠性存疑 [R1-W7, R2 AGREE]**\nB=4 时 α_eff(0) 仅 {0, 0.25, 0.5, 0.75, 1.0} 五值，b* batch 间分布未报告。在 gradient accumulation 级别（B=16）计算可改善 granularity。\n\n**m2. 关键证据仅在附录 [R1-W8, R2 AGREE]**\nProxy validation (r=0.70, Appendix K)、seed 42 artifact (Appendix P)、ρ=0.2 失效 (Appendix N) 影响核心 claims 可信度，应在正文中告知读者。\n\n**m3. Responsible NLP Checklist 出现在 PDF 中 [R2-W5, R1 AGREE]**\nEMNLP 2026/ARR 规定 checklist 应在 OpenReview 表单中填写，不在论文 PDF 中。移除可释放 ~1 页空间。\n\n**m4. 效应量极小需更充分的 cost-benefit 论证 [R2-W4]**\nAdaptive vs. uniform Δ=-0.020 PPL (~0.11% relative)。应增加 cost-benefit 分析：引入检测器训练/推理/calibration 开销 vs. 获得的改善。\n\n**m5. 小格式问题 [R2]**\nρ 的 token-level vs. document-level 区分在 §3.1 定义时就应澄清；Figure 2 灰度打印可读性不足（缺 marker shape/line style）；Table 2 \"4σ\" 含义不明确。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 3.0 (Findings)**: 两位 Reviewer 独立给出相同评分，交叉后维持。\n2. **主要价值在分析而非方法**: Epoch confound 发现有修正价值，三条件系统化有实用性；adaptive b* 是增量工程贡献。\n3. **Downstream null 是最大实践弱点**: PPL 改善未转化为任何可测量的 downstream 改善。\n4. **Seed 42 artifact 必须修复**: 核心比较的统计可信度依赖于此。\n5. **规模/场景过窄**: 验证范围远不足以支撑 claim 范围。\n6. **定位应偏向 analysis paper**: §3 Method 篇幅与 analysis 定位不匹配。\n\n## Reviewer Divergence [REBUT]\n\n1. **α_eff proxy 严重性**: R1 标 major，R2 初始标 minor。交叉后 R2 倾向同意升级至 major——α_eff 是 dual-constraint 理论基石，49% 未解释方差不是 minor 精度问题。**最终共识：major**。\n\n2. **多重比较校正严重性**: R1 标 critical，R2 交叉后认为应降为 major——理由是 epoch confound 作为 effect size decomposition 不依赖 hypothesis test。**最终判定：对 epoch confound 分析不影响（major），但对 adaptive b* method claim 为 critical**。\n\n3. **1.7B 措辞**: R1 称\"效果反转\"，R2 修正为\"diminished and inconsistent\"（holdout 仍有 Δ=-0.013，OOD 方向不稳定）。**采纳 R2 措辞**。\n\n---\n\n## Questions for Authors\n\nQ1. 能否提供排除/替换 seed 42 (from-scratch) 后的主表结果？这是决定方法贡献是否成立的关键实验。\n\nQ2. ρ=0.3 表现如何？这是方法有效与否的临界区间，缺失不可接受。\n\nQ3. 在 7B+ 规模上，(a) epoch confound 发现是否仍成立？(b) PPL 改善是否能传递到 downstream？\n\nQ4. Cross-model contamination（如 GPT-4 生成）下检测器 AUC/ECE 如何变化？dual constraint 是否仍有效？\n\nQ5. 简单固定 b=0.6 是否足够？如果是，dual-constraint 框架的 added value 是什么？\n\nQ6. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i），以改善 proxy 质量？\n\nQ7. Appendix Q (Table 13) 的 practitioner decision summary 非常实用，为什么不放主文？\n\n---\n\n## Missing References\n\n1. **Tay et al. (2022)** — PPL 与 downstream performance 的非线性关系。鉴于 Table 3 的 downstream null result，此引用几乎必需，可 contextualize §6 的发现。**最重要遗漏**。\n2. **Pruthi et al. (2020)** — Influence function-based data valuation。作为 instance-level data valuation 的另一范式，有助于定位本文方法。\n3. **Llama 3 technical report (Meta, 2024)** — 大规模 pretraining 中的数据 curation pipeline，可在 §2 中作为 motivation 引用。\n4. Sagawa et al. (2020) DRO 已引用（references.bib 中存在），无需补充。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求。项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2 warnings, 6 info）\n\n### Warnings\n- **Page 5-6**: Display items 分布不均——Page 5 大段讨论 Table 1/2 和 Figure 2 的结果，但三个 display items 全部堆叠在 Page 6。建议将 Table 1（较小）提前到 Page 5 底部。\n- **Page 7**: 整页纯文本（§5.3 + §6 开头），无 figure/table/equation 穿插。多处引用 Appendix 表格，读者无法即时验证。考虑将关键 sensitivity 分析图移入主文。\n\n### Info\n- Figure 1 彩色方框在灰度打印下可能难以区分（橄榄色 vs 绿色）\n- Figure 2 双线仅靠颜色区分，缺 marker shape/line style\n- Table 2 数值精度一致，格式规范\n- Table 3 标题暗示效果不显著，审稿人可能据此质疑实验价值\n- Algorithm 1 排版整洁\n- Appendix 末页底部 ~1/3 空白\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.0 (交叉后从 3.5 下调) | 3.0 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | — | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n\n**一句话总结**: 扎实的分析工作——epoch confound 发现纠正了文献中的重要误归因，三个有效性条件有实用价值——但方法新颖性有限（同一公式 w=(1-q)^b 的工程改进）、seed 42 artifact 使核心统计推断存疑、downstream 零改善削弱实际影响力、实验规模偏小（0.6B/1.7B, self-contamination）。达到 Findings 水准，但 novelty、statistical rigor 和 impact 不足以进入主会议。\n\n**提升路径**:\n- **→ 3.5 (Borderline Conference)**: 修复 seed 42 重跑主表 + 补充 corrected p-values + 补 ρ=0.3 实验 + 明确 analysis paper 定位（压缩 §3）\n- **→ 4.0 (Conference)**: 以上 + 7B+ 规模验证 + cross-model contamination 实验 + downstream 改善（或转为负面结果论文的强定位）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 四条 contribution 的排序和权重需调整：分析发现（1-3）应更突出，adaptive b*（4）应明确为 practical corollary\n- Figure 1 概览图有效但橄榄色/绿色区分度不足\n\n### §3 Method\n- 当前 ~1.5 页对 analysis paper 仍偏重；建议压缩至 ~0.5-0.75 页，Algorithm box 和详细推导已在 Appendix\n- §3.2 中 α_eff 的 proxy 质量局限（r=0.70）应在定义处即时提示，而非仅在附录和 Discussion 中讨论\n- 二值化 r_i = 1[q_i ≤ 0.5] 丢失连续信息，soft label 替代方案值得讨论\n\n### §4 Experimental Setup\n- ρ 的 token-level vs. document-level 区分（footnote 9）应在 §3.1 定义 ρ 时即澄清\n- Self-contamination 的生态效度局限应在 Setup 结尾即预告（而非等到 §8 Limitations）\n\n### §5 Results\n- Table 1 中必须标注 seed 42 使用了 checkpoint-resumed model（当前仅在 Appendix P）\n- Display items 分布不均（全在 Page 6），建议重新布局\n- §5.3 sensitivity analysis 是好内容但 Page 7 全文字无图表，视觉节奏断裂\n\n### §6 Discussion\n- 最大改进：Discussion 已从 11 行扩展到 50+ 行，覆盖 5 个主题，质量显著提升\n- Downstream null result 讨论仍偏短（~4 行），应引用 Tay et al. (2022) contextualize PPL-downstream gap\n- Cost-benefit 分析缺失：检测器训练/推理/calibration 开销 vs. Δ=-0.020 PPL 改善\n- Practitioner decision summary (Appendix Q Table 13) 应移入主文\n\n### §7 Conclusion\n- 与 findings 匹配，前瞻性讨论已改善\n\n### §8 Limitations\n- 覆盖全面：scale、ρ range、detector coverage、N=3 seeds、self-contamination\n- 建议增加一句关于 PPL-downstream gap 的 limitation\n\n### Format\n- Responsible NLP Checklist 应从 PDF 移除（在 OpenReview 表单填写）\n- 移除后释放 ~1 页空间可用于加强 Discussion 或引入 Appendix Q 的 decision summary",
    "project": "provenance_weight_training",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T17:16:46.507708+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3979
}
```

</details>

---


### Assistant

_source line 956 · 2026-05-22T17:16:54.562080+00:00_

**审稿报告已投递至 Research Director。**

汇总：

- **Overall: 3.0 (Findings)**，Soundness 3.0, Excitement 2.5, Confidence 4
- **两位 Reviewer 高度共识**，1 轮交叉即收敛
- **4 个 Critical**: seed 42 artifact 使核心比较存疑、多重比较未校正、方法新颖性不足、downstream 零改善
- **4 个 Major**: 规模/场景窄、定位模糊、α_eff proxy 弱、self-contamination 生态效度
- **提升路径**: 修复 seed 42 + corrected p-values + ρ=0.3 + 明确 analysis 定位 → 3.5；加 7B+ 验证 + cross-model → 4.0
- **Issue Tracker**: 7 个历史 issue 重新标记为 open，3 个新 issue 创建，4 个历史 issue 确认 resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 71

## Round 71

2 recorded events


### User

_source line 957 · 2026-05-22T17:16:57.057704+00:00_

[Reviewer 2 审稿结果]:
交叉回应完成。核心判断：

- R1 的 W1（seed 42 artifact）我强烈同意并做了定量补充——该 artifact 可能使 adaptive vs. uniform 的 Δ 从 -0.014 缩小到约 -0.002，方法贡献的统计基础岌岌可危
- W6（scope mismatch）我部分反驳了"1.7B 效果反转"的措辞（实为 diminished，非 reversed），但同意核心关切
- 其余 W2-W5、W7-W8 均同意，多数与我首轮审稿发现一致
- 基于 R1 提出的 seed 42 问题，我将 Soundness 从 3.5 下调至 3.0
- 最终评分：Overall 3.0 (Findings), Soundness 3.0, Excitement 2.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 958 · 2026-05-22T17:17:07.448183+00:00_

审稿报告已投递至 Research Director。

**Round 10 审稿完成摘要**:

- **Overall: 3.0 (Findings)**，Soundness 3.0，Excitement 2.5
- **两位 Reviewer 高度共识**，1 轮交叉即收敛
- **4 个 Critical 问题**: seed 42 artifact 使核心比较存疑、多重比较未校正、方法新颖性有限、downstream 零改善
- **4 个 Major 问题**: 规模/场景过窄、定位模糊、α_eff proxy 质量偏弱、self-contamination 生态效度
- **提升路径**: 修复 seed 42 + corrected p-values + ρ=0.3 → 3.5; 加 7B+ 和 cross-model → 4.0
- **Issue Tracker 已同步**: 6 个历史 issue 重新打开，3 个新 issue 创建，4 个历史 issue 确认 resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 72

## Round 72

56 recorded events


### User

_source line 959 · 2026-05-23T03:03:32.875509+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-23T03:03:38.832580+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-23T03:03:38.833420+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-23T03:03:47.574027+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 963 · 2026-05-23T03:03:47.574388+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-23T03:03:57.561979+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-23T03:03:58.616274+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (246 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| bs8_nmin4_uniform_seed123 | Cross-seed replicate (seed=123) uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed123. Provides second data point for B=8 batch-size amplification. | — | — | — |\n| bs8_nmin4_adaptive_seed123 | Cross-seed replicate (seed=123) of bs8_nmin4_adaptive_seed42 (Δ=−0.044). B=8 n_min=4 adaptive should show consistent negative Δ vs uniform, strengthening batch-size amplification evidence (B=4 Δ=−0.020, B=8 Δ=−0.044, B=16 Δ=−0.068). | — | — | — |\n| rho03_uniform_seed456 | Third seed (456) uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed456. Completes 3-seed set for paired t-test at the boundary contamination ratio. | — | — | — |\n\n## 待处理\n- detect_remove_q05_seed42: Detect-and-remove baseline: hard filtering removes samples with TF-IDF q_score < 0.5. If adaptive reweighting (PPL=17.674) outperforms hard removal, it demonstrates that soft scoring preserves useful signal from partially contaminated samples that hard thresholding discards.（准备中）\n- eval_adaptive_1_7b_seed123（准备中）\n- eval_uniform_1_7b_seed123（准备中）\n- detect_remove_q05_
…[truncated 1792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-23T03:03:58.616733+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 967 · 2026-05-23T03:03:58.667162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-23T03:04:00.022206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-23T03:04:00.075337+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\newcommand{\placeholder}[1][]{\textcolor{red}{\textbf{[TODO\ifx\\#1\\\else: #1\fi]}}}
32	
33	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
34	
35	\author{Anonymous}
36	
37	\begin{document}
38	\maketitle
39	
40	\begin{abstract}
41	\input{sections/abstract}
42	\end{abstract}
43	
44	\section{Introduction}
45	\label{sec:intro}
46	\input{sections/introduction}
47	
48	\section{Related Work}
49	\label{sec:related}
50	\input{sections/related_work}
51	
52	\section{Method}
53	\label{sec:method}
54	\input{sections/method}
55	
56	\section{Experimental Setup}
57	\label{sec:experiments}
58	\input{sections/experiments}
59	
60	\section{Results}
61	\label{sec:results}
62	\input{sections/results}
63	
64	\section{Discussion}
65	\label{sec:discussion}
66	\input{sections/discussion}
67	
68	\section{Conclusion}
69	\label{sec:conclusion}
70	\input{sections/conclusion}
71	
72	\section*{Limitations}
73	\label{sec:limitations}
74	\input{sections/limitations}
75	
76	\section*{Ethics Statement}
77	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involve
…[truncated 155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-23T03:04:16.270670+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 971 · 2026-05-23T03:04:16.271113+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
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

_source line 972 · 2026-05-23T03:04:16.271330+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 973 · 2026-05-23T03:04:16.826029+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-23T03:04:17.027516+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-23T03:04:17.078188+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 976 · 2026-05-23T03:04:17.180415+00:00_

-rw-r--r-- 1 ubuntu ubuntu 466029 May 23 00:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 354
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-23T03:04:25.562308+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"}]

I've found information about EMNLP 2026 call for papers, ARR submission guidelines, and author guidelines. Here's a summary of the key information:

## EMNLP 2026 Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (o
…[truncated 1448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 9291
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-23T03:04:31.979723+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-23T03:04:32.883344+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-23T03:04:33.034225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission format page limit template anonymity requirements",
  "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission format page limit template anonymity requirements",
    "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-23T03:04:39.825426+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission format page limit template anonymity requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here's the information about ACL Rolling Review 2026 May submission requirements:

## Page Limits

Papers must follow page limits: 8 pages for long papers and 4 pages for short papers, not including limitations and ethical
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6791
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-23T03:04:47.956756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-23T03:04:48.458991+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled experiments (Qwen3-0.6B continued pretraining, 132M FineWeb tokens, 3 seeds), we analyze when, why, and how detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of published gains (relative to adaptive reweighting) reflect data repetition rather than filtering quality.
6	Second, effective reweighting requires both sufficient discrimination and good calibration from the detector; a high-AUC but poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform, while a lightweight calibrated alternative (ECE\,=\,0.048) succeeds (3 detectors, 3 seeds).
7	Third, mechanism decomposition reveals that minimum intervention outperforms unconstrained maximization: an $\alpha_{\mathrm{eff}}$ quality constraint binds in 38\% of batches at $4.9{\times}$ lower sharpening exponents than a stability-only strategy.
8	
9	From this analysis, we derive a dual-constrained adaptive $b^*$ that eliminates per-model grid search, consistently lower than uniform at $\rho \geq 0.4$ with calibrated detectors ($\Delta{=}{-}0.020$ at $\rho{=}0.4$, directionally consistent across all seeds, bootstrap CI excludes zero; $\Delta{=}{-}0.032$ at $\rho{=}0.6$, $p{<}0.02$ after family-wise correction).
10	The method fails at $\rho{=}0.2$ and shows diminished benefit at 1.7B; sample size ($N{=}3$) limits generalizability.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-23T03:04:48.509572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-23T03:04:49.414977+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters.
11	Our scope is continued pretraining with self-generated contamination; generalization to web scale, multi-source contamination, or other model families is untested (\S\ref{sec:limitations}).
12	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
13	
14	Our analysis yields three findings:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{Epoch confound in D\&R evaluation.}
17	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure, not f
…[truncated 2673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-23T03:04:49.415436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-23T03:04:49.867735+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ indicate likely-real samples. The \emph{effective real proportion} $\aeff(b) = \sum_i w_i(b) r_i / \sum_i w_i(b)$ measures weight allocated to real samples.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.70$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-23T03:04:49.868175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-23T03:04:50.370369+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	Our self-contamination design provides a controlled testbed with known ground-truth labels but limits ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss this limitation in \S\ref{sec:limitations}.
6	
7	\paragraph{Detector.}
8	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
9	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
10	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
11	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
12	
13	\paragraph{Training.}
14	We continue pretraining Qwen3-0.6B from its pretrained 
…[truncated 1914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-23T03:04:50.370711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-23T03:04:50.822799+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, paired $t{=}{-}7.1$, $p{=}0.019$; Bonferroni--Holm corrected $p_{\mathrm{BH}}{=}0.078$ across nine family-wise comparisons; 95\% BCa bootstrap CI $[{-}0.028, {-}0.012]$ excludes zero) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
9	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
10	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
11	
12	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
13	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
14	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
15	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.02
…[truncated 9912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-23T03:04:50.823165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-23T03:04:51.225073+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, directionally consistent across 3 seeds) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Our results identify three necessary conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046.
12	Third, \emph{scale}: at 1.7B the benefit diminishes ($\Delta{=}{-}0.013$) with OOD partially inconsistent, suggesting that larger models may be inherently more robust to contamination generated by smaller models.
13	In all three failure cases, the adaptive method's dual constraint limits degradation relative to unconstrained reweighting (ESS-only), but uniform remain
…[truncated 5485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-23T03:04:51.225770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-23T03:04:52.229625+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4,dubey2024llama}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; M
…[truncated 6098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T03:04:52.230038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-23T03:04:52.733415+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage over adaptive reweighting); (2) detectors require both discrimination and calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$) improves over uniform at $\rho \geq 0.4$ (directionally consistent across all seeds; $\rho{=}0.6$: $p{<}0.02$ after correction) without tuning; validated on Qwen3 ${\leq}$1.7B, where the benefit diminishes.
3	Batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$, $p{<}0.01$) with diminishing marginal gains, suggesting favorable scaling with larger micro-batches typical of production training; the key bottleneck is extending detector calibration to cross-model contamination scenarios.
4	Code and data will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-23T03:04:52.734243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-23T03:04:52.734696+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B test also showed degradation ($\Delta{=}{+}0.20$), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., RoBERTa-based) and zero-shot methods (e.g., DetectGPT) remain untested, so the calibration finding may not generalize across detector architectures.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	After family-wise correction for nine comparisons, the $\rho{=}0.4$ adaptive-vs-uniform difference does not reach conventional significance ($p_{\mathrm{BH}}{=}0.078$), though the effect is directionally consistent across all seeds and the bootstrap CI excludes zero; the $\rho{=}0.6$ comparison remains significant ($p_{\mathrm{BH}}{=}0.018$).
6	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T03:04:52.885533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-23T03:04:53.137224+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; th
…[truncated 24843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-23T03:05:08.323296+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-23T03:05:10.131035+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 123\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1807
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-23T03:05:10.532952+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-23T03:05:10.985135+00:00_

issues:
- id: "R10-C1"
  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
  action_items:
    - round: 10
      action: "验证 tau07_seed42 是否 from-scratch + n_min=2 正确"
      assigned_to: main_agent
      status: completed
    - round: 10
      action: "Appendix P 澄清 resume artifact 仅涉及早期 tau=0.8 + Table 1 脚注"
      assigned_to: paper_agent
      status: completed
  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
  resolution_round: 10

- id: "R10-C2"
  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
  action_items:
    - round: 10
      action: "Bonferroni-Holm 校正计算"
      assigned_to: main_agent
      status: completed
    - round: 10
      action: "论文写入 corrected p + 统计语言审查 + 精度统一"
      assigned_to: paper_agent
      status: completed
  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
  resolution_round: 10

- id: "R10-C3"
  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
  action_items:
    - round: 10
      action: "§3 压缩至 ~0.75 页 + contributions 重排 + Algorithm box → appendix"
      assigned_to: paper_agent
      status: completed
  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive
…[truncated 5477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-23T03:05:11.487686+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-23T03:05:11.740642+00:00_

&lt;persisted-output>
Output too large (35.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training--claude-sessions-review-director-5d592d28/05630e85-b33a-4480-bf63-cee2e3f665bf/tool-results/toolu_01JGNVDpo74Kw7t5ixXaMuja.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_8.md:133:项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），本轮未请求外部审稿。
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_3.md:192:外部审稿：未配置。项目配置中无 `external_review.paperreview_ai.enabled` 字段。
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_4.md:171:外部审稿：未配置。项目配置中无 `external_review.paperreview_ai.enabled` 字段。
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_reports/round_7.md:161:外部审稿：未配置（项目未启用 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/logs/review_best.log:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/logs/chats/feishu_group_oc_069d56747de0423c793156b069500cb3_director.jsonl:6:{"ts": "2026-05-18T06:19:57.668743+00:00", "role": "tool", "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Grep",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T03:05:44.893238+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-23T03:06:08.755054+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23861
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-23T03:06:08.908201+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## 目标 Venue\n- **EMNLP 2026**，通过 ACL Rolling Review (ARR) 提交\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页限制，参考文献不限页数。Limitations 和 Ethics Statement 不计入页数\n- **模板**：ACL 2023 模板（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind，禁止透露作者身份\n- **Responsible NLP Checklist**：在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文信息\n- **标题**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n- **论文路径**：projects/provenance_weight_training/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性（重点）\n- Dual-constrained adaptive b* 的理论基础是否扎实？α_eff 作为 quality proxy（r≈0.70, R²≈0.49）是否足够支撑方法？\n- ESS ceiling 和 α_eff floor 的 interaction 是否有理论保障？\n- Bisection 求解 b* 的数值稳定性\n- w=(1-q)^b 完全沿用 Drayson et al.，方法的新颖性贡献在哪里？\n\n### 2. 实验设计\n- 实验控制是否充分？特别是 epoch confound 的控制实验\n- Self-contamination 设计的生态效度：generator = trainee 是否过于理想化？\n- 样本量 N=3 seeds 的统计检验力是否足够？2 degrees of freedom 是否能支撑论文的 claims？\n- 效应量 Δ=-0.020 PPL 的实际意义\n- Downstream task 零改善如何解读？\n\n### 3. 统计分析\n- 多重比较校正是否恰当？Bonferroni-Holm 校正后 ρ=0.4 的 p_BH=0.078 不显著，论文对此的处理是否诚实？\n- Bootstrap CI 和 paired t-test 的使用是否正确？\n- Cross-seed variance 的报告是否充分？\n- Grid-best b=0.3 作为 post-hoc oracle 的公平性\n\n### 4. 可复现性\n- 实验细节是否足够复现（超参数、训练配置、评估协议）？\n- 检测器训练细节（temperature scaling T=0.204）\n- 代码和数据承诺\n\n请严格按照顶会审稿标准评审，不要手软。输出结构：Summary → Strengths → Weaknesses（按严重性分 Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment（参考 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计分析。\n\n## 目标 Venue\n- **EMNLP 2026**，通过 ACL Rolling Review (ARR) 提交\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页限制，参考文献不限页数。Limitations 和 Ethics Statement 不计入页数\n- **模板**：ACL 2023 模板（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind，禁止透露作者身份\n- **Responsible NLP Checklist**：在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文信息\n- **标题**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n- **论文路径**：projects/provenance_weight_training/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 方法严谨性（重点）\n- Dual-constrained adaptive b* 的理论基础是否扎实？α_eff 作为 quality proxy（r≈0.70, R²≈0.49）是否足够支撑方法？\n- ESS ceiling 和 α_eff floor 的 interaction 是否有理论保障？\n- Bisection 求解 b* 的数值稳定性\n- w=(1-q)^b 完全沿用 Drayson et al.，方法的新颖性贡献在哪里？\n\n### 2. 实验设计\n- 实验控制是否充分？特别是 epoch confound 的控制实验\n- Self-contamination 设计的生态效度：generator = trainee 是否过于理想化？\n- 样本量 N=3 seeds 的统计检验力是否足够？2 degrees of freedom 是否能支撑论文的 claims？\n- 效应量 Δ=-0.020 PPL 的实际意义\n- Downstream task 零改善如何解读？\n\n### 3. 统计分析\n- 多重比较校正是否恰当？Bonferroni-Holm 校正后 ρ=0.4 的 p_BH=0.078 不显著，论文对此的处理是否诚实？\n- Bootstrap CI 和 paired t-test 的使用是否正确？\n- Cross-seed variance 的报告是否充分？\n- Grid-best b=0.3 作为 post-hoc oracle 的公平性\n\n### 4. 可复现性\n- 实验细节是否足够复现（超参数、训练配置、评估协议）？\n- 检测器训练细节（temperature scaling T=0.204）\n- 代码和数据承诺\n\n请严格按照顶会审稿标准评审，不要手软。输出结构：Summary → Strengths → Weaknesses（按严重性分 Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment（参考 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-23T03:06:24.982640+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16074
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-23T03:06:25.135301+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查新颖性、Related Work 完整性、写作质量和格式合规。\n\n## 目标 Venue\n- **EMNLP 2026**，通过 ACL Rolling Review (ARR) 提交\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页限制，参考文献不限页数。Limitations 和 Ethics Statement 不计入页数\n- **模板**：ACL 2023 模板（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind，禁止透露作者身份\n- **Responsible NLP Checklist**：在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文信息\n- **标题**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n- **论文路径**：projects/provenance_weight_training/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估（重点）\n- 三个 findings 的新颖性：(1) epoch confound, (2) detector calibration, (3) minimum intervention\n- w=(1-q)^b 框架完全来自 Drayson et al. 2025，自适应 b* 算是 incremental 还是 substantial contribution？\n- 对比同期工作（Feng et al. 2025, Yi et al. 2025, Zibakhsh et al. 2025, He et al. 2025, Wang et al. 2026）的差异化是否充分？\n- \"Analysis paper\" vs \"method paper\" 的定位是否清晰？\n\n### 2. Related Work 完整性\n- 是否遗漏重要相关工作？特别关注：\n  - 2025-2026 年最新的 synthetic data detection 方法\n  - Data mixing / data selection 领域的最新进展\n  - Model collapse 的最新理论结果\n  - Instance-level reweighting 的其他方法\n- 引用格式是否规范？是否有可疑引用（幻觉引用）？\n- 引用是否过于集中或遗漏关键领域？\n\n### 3. 写作质量\n- 论文结构是否清晰？是否 well-organized？\n- Abstract 是否准确反映论文内容？是否有 overclaim？\n- Introduction 的 narrative flow 是否流畅？\n- 表格和图表质量：是否易读、标注清晰？\n- 是否有模糊/含糊的陈述？\n- Limitations 和 Ethics Statement 是否充分？\n- 效应量 Δ=-0.020 PPL（~0.11% relative）与论文 claim 的匹配度\n\n### 4. 格式合规\n- 页数是否在 8 页限制内（正文，不含 Limitations/Ethics/References）？\n- ACL 模板使用是否正确？\n- 匿名规则遵守情况\n- Appendix 是否过于庞大？核心证据是否不当地放在附录中？\n- References 格式一致性\n\n请严格按照顶会审稿标准评审，不要手软。输出结构：Summary → Strengths → Weaknesses（按严重性分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（参考 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查新颖性、Related Work 完整性、写作质量和格式合规。\n\n## 目标 Venue\n- **EMNLP 2026**，通过 ACL Rolling Review (ARR) 提交\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页限制，参考文献不限页数。Limitations 和 Ethics Statement 不计入页数\n- **模板**：ACL 2023 模板（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind，禁止透露作者身份\n- **Responsible NLP Checklist**：在 OpenReview submission form 中填写，不在 PDF 中\n\n## 论文信息\n- **标题**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n- **论文路径**：projects/provenance_weight_training/docs/paper/main.tex\n- **PDF 路径**：/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_10/submitted.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估（重点）\n- 三个 findings 的新颖性：(1) epoch confound, (2) detector calibration, (3) minimum intervention\n- w=(1-q)^b 框架完全来自 Drayson et al. 2025，自适应 b* 算是 incremental 还是 substantial contribution？\n- 对比同期工作（Feng et al. 2025, Yi et al. 2025, Zibakhsh et al. 2025, He et al. 2025, Wang et al. 2026）的差异化是否充分？\n- \"Analysis paper\" vs \"method paper\" 的定位是否清晰？\n\n### 2. Related Work 完整性\n- 是否遗漏重要相关工作？特别关注：\n  - 2025-2026 年最新的 synthetic data detection 方法\n  - Data mixing / data selection 领域的最新进展\n  - Model collapse 的最新理论结果\n  - Instance-level reweighting 的其他方法\n- 引用格式是否规范？是否有可疑引用（幻觉引用）？\n- 引用是否过于集中或遗漏关键领域？\n\n### 3. 写作质量\n- 论文结构是否清晰？是否 well-organized？\n- Abstract 是否准确反映论文内容？是否有 overclaim？\n- Introduction 的 narrative flow 是否流畅？\n- 表格和图表质量：是否易读、标注清晰？\n- 是否有模糊/含糊的陈述？\n- Limitations 和 Ethics Statement 是否充分？\n- 效应量 Δ=-0.020 PPL（~0.11% relative）与论文 claim 的匹配度\n\n### 4. 格式合规\n- 页数是否在 8 页限制内（正文，不含 Limitations/Ethics/References）？\n- ACL 模板使用是否正确？\n- 匿名规则遵守情况\n- Appendix 是否过于庞大？核心证据是否不当地放在附录中？\n- References 格式一致性\n\n请严格按照顶会审稿标准评审，不要手软。输出结构：Summary → Strengths → Weaknesses（按严重性分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（参考 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-23T03:06:26.544688+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 1014 · 2026-05-23T03:06:40.286907+00:00_

Round 1 初审已启动：

- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）：已派发
- **Reviewer 2**（新颖性 + Related Work + 写作质量 + 格式合规）：已派发
- **视觉审查 Agent**：已派发（与 Reviewer 并行，非评分项）
- **外部审稿**：项目未配置，跳过

**Venue 确认**：
- EMNLP 2026 via ARR，截止 2026-05-25
- Long paper，正文 8 页，参考文献不限
- Double-blind，ACL 模板
- Checklist 在 OpenReview 表单填写

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 73

## Round 73

2 recorded events


### User

_source line 1015 · 2026-05-23T03:11:01.184766+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性、实验设计与统计分析

**论文**：When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining
**Venue**：EMNLP 2026 (via ACL Rolling Review)

---

## 总体评分
**Overall**: 3.0（Findings）
**一句话总结**：Epoch confound 分析是扎实且有价值的贡献，但自适应方法建立在中等相关性的 proxy 上（R²≈0.49），N=3 seeds 的实验设计严重限制了统计检验力，且 PPL 改善未能迁移到下游任务。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 epoch confound 分析设计合理；但自适应方法的 α_eff proxy 仅解释 49% 方差，N=3 seeds 下统计推断脆弱，downstream 零改善削弱 practical soundness |
| Excitement | 2.5/5 | Epoch confound 发现对 D&R 文献有实际价值，但自适应方法增量有限（w=(1-q)^b 完全来自 Drayson et al.），效应量极小 |
| Reproducibility | 4/5 | 超参数、训练配置、检测器细节报告充分（§4、Appendix M），承诺 release code/data，但 review 期间无匿名 repo |
| Reviewer Confidence | 4/5 | 仔细通读全文含 15 页 appendix，熟悉重要性采样、数据筛选和 LM 预训练文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 的统计检验力严重不足
- 具体位置：§5.1 (Table 2), Limitations (p.8)
- 问题：全部主实验仅用 3 个随机种子，paired t-test 仅 2 自由度。核心 claim Δ=−0.020 PPL（adaptive b* vs. uniform）的 95% BCa bootstrap CI 为 [−0.028, −0.012]，但 bootstrap 理论要求合理的样本量才能给出可靠区间——N=3 时 bootstrap CI 的覆盖率无法保证。论文在 Limitations 中承认了这一点（"2 degrees of freedom, limiting statistical power"），但所有定量结论仍然建立在这一基础上。
- 为什么影响接收：顶会论文的核心实验结论不应建立在 2 自由度的 t 检验上。任何 reviewer 都可以合理质疑：换 3 个不同的种子，结论是否还成立？Table 2 中 per-seed 方差极小（SD ≈ 0.007），这暗示种子间差异可能被 training recipe 的确定性所压缩，而非真正反映方法的稳健性。
- 建议修改方向：至少增加到 N=5（4 df），理想情况下 N=8-10。若计算预算受限，可在更小模型（如 60M）上用更多种子做 power analysis，展示效应的稳定性。

**N2** [critical] α_eff 作为 quality proxy 的理论基础薄弱（R²≈0.49）
- 具体位置：§3.3, Appendix K (Table 11)
- 问题：自适应方法的核心约束是 α_eff(b) ≥ τ，其动机来自 α_eff 与 true batch-level real fraction 的 Pearson r ≈ 0.70（R² ≈ 0.49）。这意味着 α_eff 仅解释了真实质量信号约一半的方差。更严重的是，经 Bonferroni-Holm 校正后 Spearman ρ=0.4 的 p_BH=0.078 不显著（Appendix K），论文对此的处理是转而强调 Pearson r，但两个相关系数的巨大差距（0.70 vs 0.40）暗示关系可能由少数极端值驱动，而非稳健的单调关系。
- 为什么影响接收：整个自适应方法的 "自适应" 部分依赖 α_eff 作为 quality signal。如果这个 proxy 不可靠，bisection 找到的 b* 可能系统性偏离最优值。R²=0.49 在 Table 11 仅基于 5 个离散的 b 值 (0, 0.25, 0.5, 0.75, 1)，样本量极小，相关系数的估计本身就很不稳定。
- 建议修改方向：(1) 展示 α_eff 与 PPL 的直接关系（而非间接通过 real fraction），因为 PPL 才是最终目标；(2) 报告 Pearson r 与 Spearman ρ 差异的原因分析（散点图、杠杆点检测）；(3) 在更细粒度的 b grid 上验证相关性。

**N3** [critical] 下游任务零改善严重削弱实际价值
- 具体位置：Table 4 (p.8), §5.2
- 问题：在 ρ=0.4 主实验条件下，5 个下游任务（MMLU、ARC-C、HellaSwag、PIQA、WinoGrande）的平均准确率 adaptive (0.5414) = uniform (0.5414)，完全相同。论文坦承 "differences within standard error, reweighting PPL gains do not transfer to downstream accuracy at this scale"。
- 为什么影响接收：如果 PPL 改善不能迁移到任何下游任务，那么整个 reweighting 方法的实际价值何在？论文在 Discussion (§6) 中推测 "the relationship between perplexity and downstream accuracy is nonlinear and scale-dependent"，但这只是猜测，没有证据支持。一个方法论文不能仅声称 PPL 改善而无法展示任何下游收益。
- 建议修改方向：(1) 在更大规模模型上验证（论文用的是 Qwen3-0.6B，极小）；(2) 如果确实无法展示下游收益，应更诚实地将论文定位为 "分析性贡献"（epoch confound）而非 "方法贡献"（adaptive reweighting）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Self-contamination 设计的生态效度有限
- 具体位置：§4 (p.4), Appendix O (p.15)
- 问题：实验中 generator = trainee（Qwen3-0.6B 生成合成数据，同一模型继续训练）。这意味着检测器面对的是同分布文本，AUC=0.94 可能在 generator≠trainee 的真实场景中不可复现。Appendix O 的 cross-model 实验（Llama-3.2-3B 生成）仅用单种子，结果混合（MMLU 提升但 HellaSwag 下降），不足以验证泛化性。
- 建议：(1) 至少用 2-3 个不同的 generator 模型（不同 family、不同 scale）做主实验级别的验证；(2) 讨论 real-world contamination 中 generator 多样性对检测器性能的影响。

**W2** [warning] 方法新颖性增量有限
- 具体位置：§3 vs. Drayson et al. (2025)
- 问题：权重函数 w=(1−q)^b 完全沿用 Drayson et al.。本文贡献是 (a) epoch confound 分析和 (b) dual-constrained b* selection。其中 (a) 是分析发现而非方法贡献，(b) 是在已有公式上加两个约束（ESS ceiling + α_eff floor）的工程改进。Bisection 求解本身是标准数值方法。论文应更清楚地界定自己相对于 Drayson et al. 的 novelty boundary。
- 建议：在 Introduction 或 §3 明确声明 "our methodological contribution is the constraint formulation, not the weighting function"，并更详细地对比 Drayson et al. 的 b 选择策略与本文的 dual-constrained 方法在不同场景下的表现差异。

**W3** [warning] Δ=−0.020 PPL 的实际意义需更充分论证
- 具体位置：§5.1 (Table 1, Table 2)
- 问题：Epoch-matched 条件下 adaptive b* 相对 uniform 的 PPL 改善仅 0.020（17.694 → 17.674），相对改善约 0.11%。论文正文提到 "the practical value is estimated" 但主要引用的 0.396 PPL 优势包含了 epoch confound。控制 epoch 后的真实效应量非常小，读者容易被 framing 误导。
- 建议：在 §5.1 开头就明确区分 "full advantage (0.396, includes epoch confound)" 和 "epoch-controlled advantage (0.020, the true method effect)"，避免读者需要自己拼凑这个关键区分。

**W4** [warning] ESS ceiling 与 α_eff floor 的交互缺乏理论分析
- 具体位置：§3.3, Algorithm 1 (Appendix B)
- 问题：当两个约束冲突时（即满足 α_eff ≥ τ 需要的 b 值超过 ESS ceiling 允许的最大 b），算法退回到 b=b_ESS。但论文未分析：(1) 这种冲突在什么条件下发生？(2) 此时 α_eff 约束被违反的程度有多大？(3) 退回 b_ESS 是否仍然优于 b=0？Appendix A 的 Proposition 1-2 只证明了单调性，未涉及约束冲突的行为。
- 建议：增加理论分析或实验展示约束冲突的频率和后果。

---

## 小问题（不影响接收）

- Table 1 脚注 1 提到 "Oracle requiring known q (He et al., 2025); seed 42 only" —— oracle baseline 仅用单种子，与其他方法的 3-seed 对比不公平，虽然影响不大。
- Figure 2 的 x 轴标签 "Sharpening exponent b" 与正文中 b 的定义位置（§3.1）相距较远，建议在 caption 中简要重述 b 的含义。
- §5.3 hyperparameter sensitivity 分析了 τ 和 contamination level 的交互，但未讨论 n_batch（ESS floor）的敏感性。
- Appendix P 的 checkpoint resume artifact 分析很有趣，但与主论文 narrative 的联系不够紧密，读者可能困惑其与主结论的关系。
- Ethics Statement 提到 "Code and data will be released upon acceptance"，但 review 期间没有匿名 repo，不利于 reproducibility 评估。

---

## Questions to Authors

1. **α_eff 与 downstream accuracy 的关系**：α_eff 与 PPL 存在 moderate correlation，但 PPL 与 downstream accuracy 之间的链条在本文中断裂（Table 4）。作者是否检查过 α_eff 与 downstream metrics 的直接相关性？
2. **N=3 的 power analysis**：给定观测到的 effect size (Δ=0.020) 和 within-seed variance (SD≈0.007)，作者是否计算过 statistical power？需要多少 seeds 才能以 80% power 检测到这个效应？
3. **Bonferroni-Holm 后 Spearman 不显著**：Pearson r=0.70 但 Spearman ρ=0.40，经校正后 p_BH=0.078。这一差异暗示 α_eff 与 real fraction 的关系可能非单调或被极端值驱动。作者能否提供散点图？
4. **Scale 依赖性**：所有实验在 Qwen3-0.6B (132M tokens) 上进行。作者在 §6 推测 "larger models may be inherently more robust"，但无证据。是否有任何 pilot 实验在更大模型上验证过核心发现？
5. **Contamination level ρ=0.4 的代表性**：论文选择 ρ=0.4 作为主实验条件，但 real-world contamination 的 level 通常未知且可能远低于此。Appendix Q 在 ρ=0.2 时已经显示方法退化，这是否意味着方法仅在高污染场景下有效？

---

## 主要优势

1. **Epoch confound 分析设计精巧且结论有力**（§5.1, Table 1）：通过 epoch-matched 对照实验证明 >95% 的 D&R 优势来自多 epoch 曝光而非过滤质量，这对整个 D&R 文献是重要的校正。Shared-schedule replication（Δ=0.006 确认 confound）的实验设计特别巧妙。

2. **三条 effectiveness conditions 的系统总结**（Figure 1）：将 detector quality（AUC+ECE）、contamination level、minimum intervention 三个条件整合为决策框架（Table 3），对从业者有直接参考价值。

3. **诚实的 negative results 报告**：论文坦承 downstream 零改善（Table 4）、α_eff 校正后不显著（Appendix K）、ρ=0.2 时方法退化（Appendix Q）、N=3 的 power 限制。这种透明度值得肯定。

4. **充实的 appendix**（A-Q，7 页）：包含理论证明、完整 grid search 结果、sensitivity 分析、cross-model 实验、low contamination 分析等，信息密度高。

---

## 总结

本文的核心价值在于 epoch confound 的分析发现，而非自适应方法本身。Epoch confound 分析设计严谨、结论清晰，足以支撑一篇 Findings 论文。但自适应方法受限于 (1) α_eff proxy 的中等可靠性（R²=0.49, Spearman 校正后不显著），(2) N=3 的实验规模无法提供足够的统计信心，(3) 下游任务零改善使得 PPL 改善的实际意义存疑。建议作者将论文重新定位为以分析贡献为主，方法贡献为辅，并增加种子数量以加强统计基础。

**Overall Assessment: 3.0 (Findings)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1016 · 2026-05-23T03:11:07.752078+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 1017 · 2026-05-23T03:11:19.711977+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断：Overall 3.0 (Findings)**

三个 Must-Fix 问题：
1. **N=3 seeds 统计检验力不足**——2 自由度的 t 检验无法可靠支撑定量结论，bootstrap CI 在 N=3 时覆盖率无保证
2. **α_eff proxy 可靠性存疑**——R²=0.49 仅解释一半方差，Bonferroni-Holm 校正后 Spearman 不显著 (p=0.078)，Pearson 与 Spearman 的巨大差距暗示极端值驱动
3. **下游任务零改善**——adaptive 与 uniform 准确率完全相同 (0.5414)，PPL 改善无法迁移

主要优势是 epoch confound 分析——证明 >95% 的 D&R 优势来自多 epoch 曝光的实验设计精巧且结论有力，足以支撑 Findings 级别接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1018 · 2026-05-23T03:11:28.312132+00:00_

Reviewer 1 审稿已收到（Overall 3.0 Findings）。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 75

## Round 75

6 recorded events


### User

_source line 1019 · 2026-05-23T03:13:21.634270+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告

**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规

---

## 总体评分

**Overall Assessment**: 3.0 / 5 — Findings
**一句话总结**: Epoch confound 的识别是对 D&R 评估方法论的有价值贡献，但极小的效应量（Δ=-0.020 PPL, ~0.11%）、狭窄的实验范围（单模型/单数据集）和增量式的方法贡献使其未达到主会议门槛，适合 Findings。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 方法论设计严谨（epoch-matched controls、permuted-score control），但 3 seeds 统计效力不足，效应量极小，单一实验设置限制了结论的可推广性 |
| **Excitement** | 2.5 / 5 | Epoch confound 发现有一定社区价值，但效应量太小、实验范围太窄、方法贡献增量式，整体 impact 有限 |
| **Overall** | 3.0 / 5 | Findings 级别——有价值的分析发现，但不够 exciting 进主会议 |

---

## 主要优势

1. **Epoch confound 的实验设计精巧**：通过 epoch-matched controls (N=3) 将 D&R 的 PPL 优势从 0.396 分解为仅 Δ=0.017（Table 1），严格证明 >95% 的优势来自多 epoch 暴露而非过滤质量。Permuted-score control (Section 5.1) 进一步确认 detector signal 是 load-bearing 的。这是一个方法论上干净的贡献。

2. **三个有效性条件形成实用框架**：Table 3 的决策矩阵（detector AUC + calibration + α_eff constraint）为从业者提供了清晰的 checklist。

3. **诚实的效应量报告**：论文没有隐瞒 Δ=-0.020 PPL 的微小效应，Limitations 部分直接承认了实验范围的局限。

4. **充分的 ablation 研究**：Section 5.2-5.3 和 Appendix B-Q 覆盖了 quality threshold sensitivity、batch-adaptive variants、constraint regime、scale、OOD evaluation 等多个维度。

5. **LR-controlled verification** (Section 5.1): 用 independent linear schedules 控制 LR schedule 混淆，确认 epoch-exposure advantage 在 controlled LR 下仍然成立，实验设计细致。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 效应量极小，实际意义不足以支撑论文的 framing

- **具体位置**: Abstract ("Δ_s=-0.020"), Table 1, Table 2, Section 5.1
- **问题**: 论文的核心数值结果——adaptive b* 相对 uniform 的改善——为 Δ=-0.020 PPL（~0.11% relative）。Table 4 的下游 benchmark 结果明确写道 "All differences within standard error"，即下游任务上无统计显著差异。论文 Abstract 和 Introduction 的叙事暗示这些 findings 对实践有指导意义（"yielding a practical adaptive method"），但 0.11% 的 PPL 改善和零下游 improvement 使这一 claim 难以成立。
- **为什么影响接收**: 如果论文的主要方法贡献（adaptive b*）在实践中几乎无法观测到改善，那么论文的 contribution 就完全落在分析发现（epoch confound）上。作为一篇 analysis paper，这足以支撑 Findings，但论文目前的 framing 试图同时主张 method contribution，导致 overclaim。
- **建议修改方向**: (1) 明确论文定位为 analysis/diagnostic paper 而非 method paper；(2) 在 Abstract 中直接量化效应量的微小程度（如 "~0.1% relative PPL improvement"），避免读者产生过高期望；(3) 讨论在什么规模/场景下效应量可能变大。

**N2** [critical] 实验范围过窄，不足以支撑 "three effectiveness conditions" 作为一般性结论

- **具体位置**: Section 4 (Experimental Setup), Section 5, Appendix O
- **问题**: 所有主要实验基于单一设置：Qwen3-0.6B、FineWeb 132M tokens、self-generated contamination (ρ=0.4)。这三个条件限制了结论的推广性：
  - **单一模型**: 仅 Qwen3-0.6B (0.6B params)。Appendix O 尝试 Llama-3.2-3B 的 cross-model transfer 但结果 "mixed"（MMLU improves while HellaSwag slightly degrades）, 作者自己承认 "mixed results"。
  - **Self-generated contamination only**: 真实 web contamination 中污染源模型与被训练模型不同、synthetic text 更多样。论文 Section 7 承认 "realistic multi-source web contamination is untested"。
  - **极小 scale**: 132M tokens 是 continued pretraining 中极小的规模。论文 Section 6 讨论了 scale effects 但缺乏实验验证。
  - **Appendix N 显示方法在 ρ=0.2 时 degrade**: "adaptive method Δ=-0.013 with OOD partially inconsistent"，而 20% contamination 是论文自己引用的 web 估计范围的下限。
- **为什么影响接收**: 论文的 framing（"we identify three effectiveness conditions for detect-and-reweight"）暗示一般性结论，但所有证据来自一个极窄的实验 corridor。三个条件可能是该特定设置的 artifact，不一定推广到其他模型、数据或 contamination 场景。
- **建议修改方向**: (1) 在标题或 Abstract 中明确 scope（如 "in the setting of single-model continued pretraining"）；(2) 增加至少一个不同架构/规模的模型（如 2-3B scale）作为主实验；(3) 测试 cross-model contamination（用不同模型生成 synthetic data）。

**N3** [critical] Adaptive b* 的新颖性不足——本质是 Drayson et al. (2025) 框架的参数选择启发式

- **具体位置**: Section 3 (Quality floor / Stability ceiling / Adaptive b*), Equation (1)
- **问题**: w=(1-q)^b 框架完全来自 Drayson et al. (2025)。论文的方法贡献是从两个约束（α_eff ≥ τ, ESS monotonicity）推导 adaptive b*。但这本质上是一个参数选择规则：在每个 batch 中根据 q-score 分布选择 b 值。Proposition 1 和 2 是关于 ESS(b) 单调性的直接推导。Adaptive b* 的形式（Equation 1）是一个简单的分段函数（if α_eff(0) ≥ τ then b=b_ESS, else b_ESS if α_eff satisfies, else 0）。这与 Drayson et al. 的 grid search 相比，主要区别仅在于自动化了 b 的选择，且最终效果几乎无差异（adaptive vs grid-best: 17.674 vs 17.657, Table 1）。
- **为什么影响接收**: 对于 EMNLP 主会议，方法贡献需要 substantial。一个框架内的参数自动选择规则，在效果与 grid search 持平的情况下，novelty 不够。
- **建议修改方向**: 如果论文定位为 analysis paper，可以弱化 adaptive b* 的地位（作为 practical corollary 而非主要贡献）；如果要强调方法，需要在更多设置下证明 adaptive b* 的优势。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 遗漏了近期 instance-level reweighting 的重要工作

- **具体位置**: Section 2 (Related Work)
- **问题**: 论文讨论了 domain-level data mixing 和 instance-level selection，但遗漏了以下直接相关的最新工作：
  - **"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining"** (arXiv:2502.06733, Feb 2025) — 这篇工作同样做 instance-level dynamic reweighting for LM pretraining，是最直接的对比对象。
  - **"Self-Influence Guided Data Reweighting for Language Model Pre-training"** (ICLR 2025) — 使用 self-influence scores 做 pretraining data reweighting。
  - **"ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection"** (arXiv:2504.00695, 2025) — topic-aware dynamic reweighting。
  这些工作与论文的 provenance-based reweighting 形成对比（基于 quality vs 基于 provenance），论文应讨论为什么 provenance 信号比 loss-based 或 influence-based 信号更合适或不同。
- **建议**: 在 Section 2 的 "Instance-Level Data Selection and Reweighting" 段落中增加对这些工作的讨论。

**W2** [warning] Epoch confound 发现虽然有价值，但在概念上并非完全出乎意料

- **具体位置**: Section 5.1, Section 6
- **问题**: 当 D&R 过滤掉部分 samples（如 detect & remove），有效数据集缩小，模型在相同 step 数下看到更多 epoch 的数据。这是一个自然推论——减少数据量意味着更多重复暴露。论文的贡献在于严格的实验验证（epoch-matched controls），但 Section 6 的讨论（"The epoch confound in D&R evaluation"）没有充分讨论为什么这个 confound 在之前的文献中被忽略——是因为之前的工作没有控制 epoch，还是因为它们在不同的实验设置下影响更小？
- **建议**: 在 Section 6 中增加对 prior work 实验设置的具体分析——Drayson et al. (2025) 和其他 D&R 工作是否报告了 epoch 数？是否有迹象表明 epoch confound 在它们的结果中同样存在？

**W3** [warning] 3 seeds 统计效力不足以支撑如此小的效应量

- **具体位置**: Section 4 (Training), Table 1, Table 2, Limitations
- **问题**: 论文使用 3 seeds (42, 123, 456)。对于 Δ=-0.020 PPL 的效应量，3 seeds 提供的统计效力极低。Table 1 报告 std 约 ±0.007-0.008，但这是 3-seed 的 std——degrees of freedom 仅为 2。论文自己在 Limitations 中承认 "the sample size (N=3) limits generalizability"，但这不仅限制 generalizability，也限制了效应量本身的可靠性。Footnote 2 提到 "Computed from 3dp-rounded per-seed values"，进一步增加了不确定性。
- **建议**: (1) 报告 95% 置信区间而非仅 std；(2) 增加到至少 5 seeds 或更多；(3) 对关键发现执行 statistical significance test（如 paired t-test 或 bootstrap CI）。

**W4** [warning] 论文的 "analysis paper" vs "method paper" 定位不清晰

- **具体位置**: Abstract, Section 1, Section 3, Section 7
- **问题**: Abstract 同时 claim "we analyze when, why, and how detect-and-reweight works"（analysis）和 "we derive a dual-constrained adaptive b* that eliminates per-model grid search"（method）。Introduction 最后一段列出三个 findings（analysis），但紧接着推出 adaptive b* 作为 "practical corollary"。这种双重定位使论文的 contribution 模糊——作为 analysis paper，epoch confound 是核心但实验范围需要更广；作为 method paper，adaptive b* 的改善太小且不够 novel。
- **建议**: 明确选择一个定位。建议定位为 analysis paper，将 adaptive b* 降级为 practical implication 而非主要贡献。

**W5** [warning] α_eff 作为 detector proxy 的 correlation 较弱

- **具体位置**: Appendix K (Table 11), Section 5.3
- **问题**: Table 11 报告 α_eff 与 true batch-level real fraction 的 Pearson r = 0.170（seed 42）。论文将其解释为 "consistent negative bias (-0.03) indicates that α_eff slightly underestimates the true real fractions"，但 r=0.170 是非常弱的相关性。虽然 Spearman r=0.25 和 0.75（different seeds）稍好，但跨 seed 的不一致性（0.17-0.75 范围）说明 α_eff 作为 proxy 的可靠性存疑。论文基于 α_eff 的约束（α_eff ≥ τ）来决定 b*，如果 α_eff 本身就不准确，约束的效力就有限。
- **建议**: 更充分地讨论 α_eff 的局限性，以及它作为 proxy 的不可靠性如何影响 adaptive b* 的实际表现。

---

## 小问题（不影响接收）

1. **Figure 2 可读性**: 图较小，右侧 "Sharpening exponent b" 和 "Held-out PPL" 的 y 轴标签较拥挤；三角形（seed 42）与五角星（seed 456）在灰度打印下难以区分。

2. **Footnote 密度过高**: 全文约 12+ 个脚注（正文内），部分脚注包含重要技术细节（如 footnote 1 的 batch composition、footnote 2 的 rounding），考虑将关键脚注内容移入正文。

3. **Section 2 结构**: "Synthetic Contamination and Model Collapse" 和 "Detection and Filtering of Machine-Generated Text" 两个小节的界限模糊——model collapse 的讨论（Shumailov et al., Dohmatob et al.）与 detection 相关但不完全是同一话题，可以更清晰地分开。

4. **Table 2 小数位不一致**: Method 列中 "Adaptive b*" 的 PPL 报告 3 位小数，但 "Detect & Remove" 等仅 2-3 位小数。建议统一。

5. **Appendix 过于庞大**: Appendix A-Q 共 5 页（pages 11-15），涵盖 17 个子附录。部分关键证据（如 Appendix K 的 α_eff proxy validation、Appendix N 的 low contamination results）对论文核心论点很重要，考虑是否应在正文中更充分讨论。

6. **"practical" 一词使用频率过高**: Abstract, Section 1, Section 3 中多次使用 "practical" 来修饰 adaptive b*，但 0.11% 的改善是否 "practical" 值得商榷。

---

## Questions to Authors

1. 论文的核心发现（epoch confound）是否在 Drayson et al. (2025) 的原始实验设置中同样成立？他们的 b=10 grid search 结果中有多少可以用 epoch confound 解释？

2. 如果将 contamination 源从 self-generated 换成不同模型（如用 Llama 生成 synthetic data 来污染 Qwen 训练集），三个有效性条件是否仍然成立？

3. Adaptive b* 在 ρ=0.2 时 degrade（Appendix N），但论文引用的 web contamination 估计下限就是 20%。论文是否认为 adaptive b* 仅适用于高 contamination 场景？如果是，这如何与论文标题中 "When Does Detect-and-Reweight Work?" 的一般性问题对齐？

4. Table 4 下游 benchmark 无显著差异。如果 PPL 改善不能转化为下游性能提升，"effectiveness conditions" 的实际意义是什么？

5. α_eff 与 true batch-level real fraction 的 correlation 跨 seed 差异很大（Pearson r: 0.17-0.75, Table 11）。作者如何解释这种不稳定性？

---

## Missing References

1. **Xu et al. (2025)** "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining" (arXiv:2502.06733) — 直接做 instance-level dynamic reweighting for pretraining
2. **Xia et al. (2023/ICLR 2025)** "Self-Influence Guided Data Reweighting for Language Model Pre-training" — self-influence based pretraining data reweighting
3. **Wu et al. (2025)** "A Survey on LLM-Generated Text Detection" (Computational Linguistics, MIT Press) — 最新的 MGT detection 综述
4. **Chen et al. (2025)** "ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection" — topic-aware dynamic reweighting

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 页数限制（正文 ≤8 页） | ✅ 合规 | 正文（Section 1-7）在第 8 页结束，Limitations 从第 8 页右栏开始，不计入页数 |
| ACL 模板 | ✅ 合规 | 使用 "Anonymous ACL submission" 标识 |
| Double-blind 匿名 | ✅ 合规 | 未发现作者身份泄露 |
| Limitations 章节 | ✅ 存在 | 第 8 页右栏，覆盖模型规模、数据范围、seed 数量等 |
| Ethics Statement | ✅ 存在 | 第 9 页左栏，简短但充分 |
| Responsible NLP Checklist | ✅ 不在 PDF 中 | 符合要求（在 OpenReview form 中填写） |
| References 格式 | ⚠️ 基本一致 | 大部分规范，但部分 arXiv preprint 未标注会议版本（如已被接收） |
| Appendix 大小 | ⚠️ 较大 | 5 页 17 个子附录，部分关键证据（K, N）未在正文充分引用 |

---

## 总结

这篇论文提出了一个有价值的方法论发现（epoch confound in D&R evaluation），并提供了一个系统的实验分析。但它面临三个核心挑战：(1) 效应量极小（0.11% PPL, 下游无显著差异），(2) 实验范围过窄（单模型、单数据集、self-generated contamination），(3) 方法贡献（adaptive b*）是增量式的。作为 Findings 论文，epoch confound 的发现足够支撑接收；但对于主会议，需要更广的实验范围和更 convincing 的实际影响。

建议评分：**Overall 3.0 — Findings**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-23T03:14:00.057718+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**一句话总结**: Epoch confound 的识别是对 D&R 评估方法论的有价值贡献，但极小的效应量（Δ=-0.020 PPL, ~0.11%）、狭窄的实验范围（单模型/单数据集）和增量式的方法贡献使其未达到主会议门槛，适合 Findings。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] 效应量极小，实际意义不足以支撑论文的 framing\n- Δ=-0.020 PPL（~0.11% relative），下游 benchmark 无显著差异（Table 4: 0.5414 = 0.5414）\n- Abstract 和 Introduction 的叙事暗示 \"yielding a practical adaptive method\"，构成 overclaim\n- 建议明确定位为 analysis/diagnostic paper\n\n**N2** [critical] 实验范围过窄\n- 仅 Qwen3-0.6B、FineWeb 132M tokens、self-generated contamination\n- Cross-model transfer (Appendix O) 结果 \"mixed\"\n- ρ=0.2 时方法 degrade\n- \"three effectiveness conditions\" 作为一般性结论缺乏多样化实验支撑\n\n**N3** [critical] Adaptive b* 的新颖性不足\n- w=(1-q)^b 完全来自 Drayson et al.\n- Adaptive b* 本质是参数选择启发式（分段函数 + bisection）\n- Adaptive vs grid-best: 17.674 vs 17.657，几乎无差异\n\n## Should-Fix 问题\n\n**W1** [warning] Related Work 遗漏近期 instance-level reweighting 工作\n- Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733)\n- Self-Influence Guided Data Reweighting (ICLR 2025)\n- ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695)\n\n**W2** [warning] Epoch confound 发现概念上非完全出乎意料\n- 减少数据量意味着更多重复暴露是自然推论\n- 贡献在于严格实验验证，但需讨论为何之前文献忽略了\n\n**W3** [warning] 3 seeds 统计效力不足\n\n**W4** [warning] \"analysis paper\" vs \"method paper\" 定位不清晰\n- Abstract 同时 claim analysis 和 method\n- 建议明确选择一个定位\n\n**W5** [warning] α_eff correlation 跨 seed 差异大（Pearson r: 0.17-0.75）\n\n## Missing References\n1. Xu et al. (2025) \"Dynamic Loss-Based Sample Reweighting\"\n2. Xia et al. (ICLR 2025) \"Self-Influence Guided Data Reweighting\"\n3. Wu et al. (2025) \"A Survey on LLM-Generated Text Detection\"\n4. Chen et al. (2025) \"ToReMi\"\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 新颖性、Related Work 完整性、写作质量、格式合规\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**一句话总结**: Epoch confound 的识别是对 D&R 评估方法论的有价值贡献，但极小的效应量（Δ=-0.020 PPL, ~0.11%）、狭窄的实验范围（单模型/单数据集）和增量式的方法贡献使其未达到主会议门槛，适合 Findings。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] 效应量极小，实际意义不足以支撑论文的 framing\n- Δ=-0.020 PPL（~0.11% relative），下游 benchmark 无显著差异（Table 4: 0.5414 = 0.5414）\n- Abstract 和 Introduction 的叙事暗示 \"yielding a practical adaptive method\"，构成 overclaim\n- 建议明确定位为 analysis/diagnostic paper\n\n**N2** [critical] 实验范围过窄\n- 仅 Qwen3-0.6B、FineWeb 132M tokens、self-generated contamination\n- Cross-model transfer (Appendix O) 结果 \"mixed\"\n- ρ=0.2 时方法 degrade\n- \"three effectiveness conditions\" 作为一般性结论缺乏多样化实验支撑\n\n**N3** [critical] Adaptive b* 的新颖性不足\n- w=(1-q)^b 完全来自 Drayson et al.\n- Adaptive b* 本质是参数选择启发式（分段函数 + bisection）\n- Adaptive vs grid-best: 17.674 vs 17.657，几乎无差异\n\n## Should-Fix 问题\n\n**W1** [warning] Related Work 遗漏近期 instance-level reweighting 工作\n- Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733)\n- Self-Influence Guided Data Reweighting (ICLR 2025)\n- ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695)\n\n**W2** [warning] Epoch confound 发现概念上非完全出乎意料\n- 减少数据量意味着更多重复暴露是自然推论\n- 贡献在于严格实验验证，但需讨论为何之前文献忽略了\n\n**W3** [warning] 3 seeds 统计效力不足\n\n**W4** [warning] \"analysis paper\" vs \"method paper\" 定位不清晰\n- Abstract 同时 claim analysis 和 method\n- 建议明确选择一个定位\n\n**W5** [warning] α_eff correlation 跨 seed 差异大（Pearson r: 0.17-0.75）\n\n## Missing References\n1. Xu et al. (2025) \"Dynamic Loss-Based Sample Reweighting\"\n2. Xia et al. (ICLR 2025) \"Self-Influence Guided Data Reweighting\"\n3. Wu et al. (2025) \"A Survey on LLM-Generated Text Detection\"\n4. Chen et al. (2025) \"ToReMi\"\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-23T03:14:22.897024+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22839
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-23T03:14:23.048006+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n## Overall: 3.0（Findings）\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计检验力严重不足\n- 全部主实验仅用 3 个随机种子，paired t-test 仅 2 自由度\n- Δ=-0.020 的 95% BCa bootstrap CI [−0.028, −0.012] 在 N=3 时覆盖率无法保证\n- Per-seed 方差极小（SD ≈ 0.007），种子间差异可能被 training recipe 的确定性压缩\n- 建议增加到 N=5-10\n\n**N2** [critical] α_eff 作为 quality proxy 的理论基础薄弱（R²≈0.49）\n- α_eff 仅解释真实质量信号约一半方差\n- Bonferroni-Holm 校正后 Spearman ρ=0.4 的 p_BH=0.078 不显著\n- Pearson r=0.70 vs Spearman ρ=0.40 差距暗示关系可能由极端值驱动\n- Table 11 仅基于 5 个离散 b 值，样本量极小\n\n**N3** [critical] 下游任务零改善严重削弱实际价值\n- 5 个下游任务 adaptive (0.5414) = uniform (0.5414)\n- PPL 改善不能迁移到任何下游任务\n- 建议更大规模模型验证或将论文定位为分析贡献\n\n## Should-Fix 问题\n\n**W1** [warning] Self-contamination 设计生态效度有限\n- Generator = trainee，AUC=0.94 可能在真实场景不可复现\n- Cross-model 实验仅单种子，结果混合\n\n**W2** [warning] 方法新颖性增量有限\n- w=(1−q)^b 完全沿用 Drayson et al.\n- Dual-constrained b* 是工程改进而非方法创新\n\n**W3** [warning] Δ=-0.020 PPL 实际意义需更充分论证\n- ~0.11% relative improvement\n- 读者容易被 framing 误导\n\n**W4** [warning] ESS ceiling 与 α_eff floor 交互缺乏理论分析\n- 约束冲突时退回 b=b_ESS 的后果未分析\n- Proposition 1-2 只证明单调性，未涉及约束冲突\n\n## Questions to Authors\n1. α_eff 与 downstream accuracy 的直接相关性？\n2. N=3 的 power analysis？需要多少 seeds 达到 80% power？\n3. Pearson r=0.70 vs Spearman ρ=0.40 差异的散点图？\n4. 更大模型上的 pilot 实验？\n5. ρ=0.4 的代表性——方法仅在高污染场景有效？\n\n## 主要优势\n1. Epoch confound 分析设计精巧且结论有力\n2. 三条 effectiveness conditions 的系统总结\n3. 诚实的 negative results 报告\n4. 充实的 appendix\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n**审查侧重**: 方法严谨性、实验设计、统计分析\n\n## Overall: 3.0（Findings）\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计检验力严重不足\n- 全部主实验仅用 3 个随机种子，paired t-test 仅 2 自由度\n- Δ=-0.020 的 95% BCa bootstrap CI [−0.028, −0.012] 在 N=3 时覆盖率无法保证\n- Per-seed 方差极小（SD ≈ 0.007），种子间差异可能被 training recipe 的确定性压缩\n- 建议增加到 N=5-10\n\n**N2** [critical] α_eff 作为 quality proxy 的理论基础薄弱（R²≈0.49）\n- α_eff 仅解释真实质量信号约一半方差\n- Bonferroni-Holm 校正后 Spearman ρ=0.4 的 p_BH=0.078 不显著\n- Pearson r=0.70 vs Spearman ρ=0.40 差距暗示关系可能由极端值驱动\n- Table 11 仅基于 5 个离散 b 值，样本量极小\n\n**N3** [critical] 下游任务零改善严重削弱实际价值\n- 5 个下游任务 adaptive (0.5414) = uniform (0.5414)\n- PPL 改善不能迁移到任何下游任务\n- 建议更大规模模型验证或将论文定位为分析贡献\n\n## Should-Fix 问题\n\n**W1** [warning] Self-contamination 设计生态效度有限\n- Generator = trainee，AUC=0.94 可能在真实场景不可复现\n- Cross-model 实验仅单种子，结果混合\n\n**W2** [warning] 方法新颖性增量有限\n- w=(1−q)^b 完全沿用 Drayson et al.\n- Dual-constrained b* 是工程改进而非方法创新\n\n**W3** [warning] Δ=-0.020 PPL 实际意义需更充分论证\n- ~0.11% relative improvement\n- 读者容易被 framing 误导\n\n**W4** [warning] ESS ceiling 与 α_eff floor 交互缺乏理论分析\n- 约束冲突时退回 b=b_ESS 的后果未分析\n- Proposition 1-2 只证明单调性，未涉及约束冲突\n\n## Questions to Authors\n1. α_eff 与 downstream accuracy 的直接相关性？\n2. N=3 的 power analysis？需要多少 seeds 达到 80% power？\n3. Pearson r=0.70 vs Spearman ρ=0.40 差异的散点图？\n4. 更大模型上的 pilot 实验？\n5. ρ=0.4 的代表性——方法仅在高污染场景有效？\n\n## 主要优势\n1. Epoch confound 分析设计精巧且结论有力\n2. 三条 effectiveness conditions 的系统总结\n3. 诚实的 negative results 报告\n4. 充实的 appendix\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-23T03:14:24.715699+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1667
}
```

</details>

---


### Assistant

_source line 1024 · 2026-05-23T03:14:27.208499+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 1025 · 2026-05-23T03:14:29.848835+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。已向 Review Director 提交完整报告。核心判断：

- **Overall: 3.0 (Findings)** — epoch confound 发现有价值但不够进主会议
- **Soundness: 3.5** — 实验设计严谨但范围过窄、统计效力不足
- **Excitement: 2.5** — 效应量太小（Δ=-0.020 PPL, ~0.11%），方法贡献增量式

三个 Must-Fix 问题：(1) 效应量极小且下游无显著差异，论文 framing 有 overclaim；(2) 单模型/单数据集/self-generated contamination 不足以支撑一般性结论；(3) adaptive b* 本质是 Drayson et al. 框架的参数选择启发式，novelty 不足。还识别了 4 篇遗漏的直接相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1026 · 2026-05-23T03:14:34.748287+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 1027 · 2026-05-23T03:15:40.255541+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 效应量极小，实际意义不足以支撑论文 framing**
同意。这与我的 N3 和 W3 一致。Δ=−0.020 PPL（~0.11%）在 epoch-matched 条件下极其微小，且 Table 4 的下游 benchmark 平均准确率 adaptive (0.5414) = uniform (0.5414)，完全无差异。Abstract 中 "yielding a practical adaptive method" 的措辞确实构成 overclaim——一个在下游任务上零改善的方法难以被称为 "practical"。R2 建议重新定位为 analysis/diagnostic paper 与我的建议一致。不过需要公平指出：论文在 §6 和 Limitations 中确实坦承了下游零改善和效应量小的事实，问题主要在 Abstract/Intro 的 framing 而非隐瞒。

**[AGREE with nuance] R2-N2: 实验范围过窄**
大体同意，但严重程度需区分。单模型（Qwen3-0.6B）、单数据集（FineWeb 132M tokens）、self-contamination 的实验范围确实过窄，这也是我 W1 指出的问题。Appendix O 的 cross-model 实验（Llama-3.2-3B 生成）仅单种子且结果混合（MMLU↑ 但 HellaSwag↓），不足以支撑泛化性。ρ=0.2 时方法退化（Appendix Q）也是重要限制。

但我要补充一点：R2 称 "three effectiveness conditions 作为一般性结论缺乏多样化实验支撑" 需要更精确地看。这三个条件（detector quality, contamination level, minimum intervention）是通过消融实验（Table 3）得出的，虽然仅在一个设置下验证，但其逻辑结构是合理的——它们是 necessary conditions 而非 sufficient conditions，论文并未声称在所有设置下都充分。问题在于论文的措辞有时暗示了更强的一般性。

**[PARTIALLY REBUT] R2-N3: Adaptive b* 新颖性不足**
部分反驳。R2 的论点有一定道理——w=(1−q)^b 确实完全来自 Drayson et al.，dual-constrained bisection 从算法角度看比较 incremental。这也是我 W2 提出的。

但 R2 用 "adaptive vs grid-best: 17.674 vs 17.657, 几乎无差异" 作为新颖性不足的证据，这个论证逻辑有问题。Adaptive 方法的目标恰恰是在不做 grid search 的情况下接近 grid-best 性能——差距仅 0.017 说明方法有效，而非无价值。Grid search 需要多次完整训练（Table 5 显示 9 个 candidate，即 9 次训练），而 adaptive b* 是 zero-cost 的。这个区别 R2 没有给予足够重视。

我认为新颖性问题应标记为 should-fix（要求更好的 positioning）而非 critical。论文的真正新颖性在于 epoch confound 的发现，adaptive method 是附带的实践贡献。

---

### Should-Fix 问题

**[PARTIALLY AGREE] R2-W1: Related Work 遗漏近期 instance-level reweighting 工作**
部分同意。论文 Section 2 的 "Instance-Level Data Selection and Reweighting" 部分已经覆盖了 curriculum learning (Bengio et al.)、focal loss (Lin et al.)、importance sampling (Katharopoulos and Fleuret 2018; Mindermann et al. 2022)、LESS (Xia et al. 2024) 等，覆盖面是合理的。

R2 列出的 4 篇缺失引用中，我无法在 blind review 条件下独立验证它们是否真实存在及是否高度相关。但如果这些确实是 2025 年发表的 instance-level reweighting 工作，鉴于论文声称解决的是 pretraining 数据 reweighting 问题，补充讨论它们与 provenance-based reweighting 的区别（instance-level loss-based vs. provenance-based binary signal）是合理的。建议作者在 camera-ready 中补充核实并酌情引用。

**[AGREE] R2-W2: Epoch confound 概念上非完全出乎意料**
同意。"过滤掉数据→剩余数据训练更多 epoch→可能获益于重复暴露" 确实是一个可以事先推理出的 hypothesis。但我要强调：R2 自己也承认 "贡献在于严格实验验证"，这正是关键——之前的 D&R 文献（Drayson et al. 2025, Cheng et al. 2025 等）确实没有控制 epoch confound。论文在 §5.1 中通过 epoch-matched 对照（Table 1）和 shared-schedule replication（Δ=0.006）提供了令人信服的定量证据，证明 confound 解释了 >95% 的优势。

我同意论文应增加讨论 "为什么之前文献忽略了这个 confound"。可能的原因包括：(1) 之前的工作关注的是 absolute performance 而非 epoch-controlled comparison；(2) 在 from-scratch pretraining 中 epoch confound 不如 continued pretraining 明显。这类讨论会加强贡献的 contextualization。

**[STRONGLY AGREE] R2-W3: 3 seeds 统计效力不足**
强烈同意。这是我的 N1 (must-fix)。N=3 seeds, 2 自由度，bootstrap CI 不可靠，是本文最严重的实验缺陷。R2 将其列为 should-fix 而非 must-fix，我认为应升级为 must-fix。

**[AGREE] R2-W4: "analysis paper" vs "method paper" 定位不清晰**
同意。Abstract 同时 claim "we analyze when, why, and how detect-and-reweight works"（分析）和 "we derive a dual-constrained adaptive b*"（方法）。鉴于 epoch confound 分析远比 adaptive method 有说服力（前者有充分证据，后者受限于 R²=0.49 的 proxy 和零下游改善），论文应明确以分析为主线。这与我的总结建议一致。

**[AGREE] R2-W5: α_eff correlation 跨 seed 差异大**
同意，且这进一步加强了我 N2 的论点。Table 11（Appendix K）显示 α_eff 与 true real fraction 的 Pearson r 跨 seed 从 0.17 到 0.75 变化极大。r=0.17 的种子基本上意味着 α_eff 作为 proxy 完全失效（R²≈0.03）。三个种子中有一个种子的相关性接近零，这不是随机波动——这暗示 α_eff 的 proxy 质量高度依赖于特定训练 trajectory，而非一个 robust 的信号。

这与 Bonferroni-Holm 校正后 Spearman ρ 不显著（p_BH=0.078）的结果一致：α_eff 作为 quality proxy 的可靠性远低于论文主体部分的 framing 所暗示的。

---

### Missing References 回应

R2 列出的 4 篇缺失引用（Xu et al. 2025, Xia et al. ICLR 2025, Wu et al. 2025, Chen et al. 2025），我在 blind review 条件下无法独立核实其存在和相关性。论文 Section 2 的 related work 在 instance-level reweighting 方向已有合理覆盖，但如果这些是 2025 年的最新工作，确实应在 camera-ready 中补充。特别是如果有 survey（Wu et al. 2025 关于 LLM-generated text detection）与本文 §2 的 detection 部分直接相关，应当引用。

---

### 总结

R2 与我的审稿意见在核心判断上高度一致：(1) epoch confound 是有价值的分析贡献；(2) adaptive method 增量有限且实验支撑不足；(3) 效应量极小且无下游收益；(4) 实验范围过窄。

两份审稿的主要分歧在于：
- **N=3 seeds 的严重程度**：我列为 must-fix，R2 列为 should-fix。我认为 must-fix 更恰当——2 自由度的 t 检验不应作为顶会论文的核心统计基础。
- **Adaptive b* 新颖性**：R2 列为 must-fix critical，我列为 should-fix。我认为 zero-cost 接近 grid-best 是有实践价值的，问题在于 positioning 而非方法本身无效。

**维持 Overall: 3.0 (Findings)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1028 · 2026-05-23T03:15:45.940257+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 1029 · 2026-05-23T03:15:50.403780+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部 Must-Fix（N1-N3）和 Should-Fix（W1-W5）的逐条交叉回应，并汇报给 Director。

核心判断：
- 与 R2 在 5 个问题上 **[AGREE]**（效应量过小、epoch confound 非全新、3 seeds 不足、定位不清、α_eff 跨 seed 不稳）
- 在 2 个问题上 **[PARTIALLY AGREE/REBUT]**（实验范围窄但 three conditions 逻辑合理；adaptive b* 新颖性不应列为 critical，zero-cost 接近 grid-best 有实践价值）
- 主要分歧：我认为 N=3 seeds 应升级为 must-fix，而 adaptive b* 新颖性应降级为 should-fix
- 维持 Overall 3.0 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1030 · 2026-05-23T03:15:55.345233+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 79

## Round 79

10 recorded events


### User

_source line 1031 · 2026-05-23T03:17:23.672964+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: N=3 seeds 统计检验力不足

同意这是论文的核心方法论弱点。我在自己的审稿意见 W3 中也独立提出了同一问题。补充几点：

1. **BCa bootstrap 在 N=3 时确实不可靠**：BCa 的 bias-correction 和 acceleration 参数需要从 jackknife 估计，N=3 时仅有 3 个 jackknife 样本，这些参数的估计本身极不稳定。论文报告的 CI [−0.028, −0.012] 的覆盖率确实无法保证。
2. **R1 关于"种子间差异被 training recipe 确定性压缩"的观察很敏锐**：如果 data order 是 seed-deterministic 但模型初始化之外的随机性很小，那么 3 seeds 的 variance 可能低估了真实的实验不确定性。
3. **但要区分定量和定性 findings**：epoch confound 的核心发现（>95% 优势来自 multi-epoch）是一个定性结论——Table 1 中 epoch-matched 的 Δ 从 0.396 骤降到 0.017，这个 ratio 在 3 seeds 中方向完全一致。统计效力问题主要影响 adaptive b* 的定量精度（Δ=-0.020 ± 多少？），而非 epoch confound 的方向性结论。

**总结**：同意 N=3 是问题，建议至少增加到 N=5。但 epoch confound 的定性结论受此影响较小。

---

### [AGREE] R1-N2: α_eff 作为 quality proxy 的理论基础薄弱

同意。我在自己的 W5 中也独立提出了 α_eff proxy reliability 问题。R1 的统计分析更深入，补充认同以下几点：

1. **Pearson r=0.70 vs Spearman ρ=0.40 的差距确实暗示极端值驱动**：线性相关强但秩相关弱，说明 α_eff 在少数极端 batch 上与真实质量一致，但在大多数 batch 上排序不可靠。这对 threshold-based 决策（α_eff ≥ τ）尤其危险——threshold 需要的是全范围的可靠排序，不仅仅是极端值处的相关。
2. **Table 11 仅基于 5 个离散 b 值**：R1 指出的样本量问题是正确的。5 个点上的 correlation 信息量极少。
3. **一个补充观察**：我的审稿中注意到 Table 11 跨 seed 的 Pearson r 变化范围较大（部分 seed 很低），进一步支持 R1 的不稳定性担忧。

**建议**：论文应增加 α_eff 在连续 b 值上的 calibration 分析，而非仅依赖 5 个离散点。

---

### [AGREE] R1-N3: 下游任务零改善削弱实际价值

完全同意。我在自己的 N1 中也将此作为 critical issue 提出。具体引用相同证据：

- Table 4 明确报告 adaptive (0.5414) = uniform (0.5414)，"All differences within standard error"（Table 4 caption）
- 这意味着论文的方法贡献（adaptive b*）在任何可测量的下游任务上都没有产生差异
- 论文的实际价值因此完全落在 epoch confound 的诊断发现上，而非方法改进

R1 建议的"将论文定位为分析贡献"与我的建议一致。

---

## Should-Fix 问题

### [AGREE] R1-W1: Self-contamination 生态效度有限

同意。我在 N2 中也将此作为 critical issue 提出（我的评级更高）。补充：

- **Generator = trainee 使 AUC=0.94 具有人为优势**：当模型检测自己生成的文本时，detector 可以利用自身 decoding 的统计规律性（如 nucleus sampling 的截断分布）。在真实 web contamination 中，generator 和 detector 不同，AUC 可能显著更低。
- **Appendix O 的 cross-model 实验（Llama-3.2-3B）结果"mixed"且仅单 seed**：这不足以证明方法在 cross-model 场景的有效性。论文自己承认 "mixed results with surface-level evaluation sensitivity" (Appendix O)。
- **这对 Finding 2（detector calibration 是必要条件）尤其关键**：如果在 cross-model 场景下 detector 本身就不可靠，那么整个 D&R 框架的前提就动摇了。

---

### [AGREE] R1-W2: 方法新颖性增量有限

完全同意。与我的 N3 一致。w=(1-q)^b 框架 100% 来自 Drayson et al. (2025)，adaptive b* 是一个两约束优化问题的闭式解——Proposition 1 证明 ESS 单调性（直接推导），Proposition 2 证明严格递减（batch 含不同 q 值时自然成立）。这些数学结果虽然正确但 trivial。

"工程改进而非方法创新"的评价准确。

---

### [AGREE] R1-W3: Δ=-0.020 PPL 实际意义不足

同意。与我的 N1 一致。补充一个具体数据点：Section 6 讨论 "the gap to grid-best narrows from 0.040 (B=4) to 0.009 (B=16)"，但即使是 grid-best（需要 post-hoc oracle 知识），改善也仅 Δ≈-0.037（Table 1, 17.657 vs 17.694）。这意味着 detect-and-reweight 方法在这个设置下的 *upper bound* 改善也仅约 0.2%——整个方法类别的天花板就很低，不仅仅是 adaptive b* 的问题。

---

### [REBUT] R1-W4: ESS ceiling 与 α_eff floor 交互缺乏理论分析

部分不同意。R1 的观察（约束冲突时的行为未理论分析）在形式上是对的，但论文 *隐式地* 通过实验覆盖了这一场景：

1. **ESS-only baseline 就是约束冲突的极端情况**：当 α_eff floor 完全不起作用（即不施加 quality 约束）时，方法退化为 ESS-only。Table 1 报告 ESS-only 的 mean PPL = 17.763，与 adaptive b*（17.674）差距 0.089，但与 uniform（17.694）相比 ESS-only 反而更差。这说明约束冲突时退回 ESS-only 行为的确不理想，但论文已经展示了这一点。

2. **与论文 Finding 3（minimum intervention）一致**：Section 6 的讨论（"When uniform beats reweighting"）明确指出过度 sharpening 有害。当约束冲突时，adaptive b* 选择 b_ESS（较低的 b），这正是 minimum intervention 原则的体现——宁可少做，不要做过头。

3. **实际冲突频率已隐式报告**：Section 5.1 报告 "α_eff quality constraint binds in 38.2% of batches"，意味着在 38.2% 的 batch 中 quality constraint 是 active 的。在剩余 61.8% 中，α_eff(0) ≥ τ（即使不 sharpen quality 也满足），b* = b_ESS。论文可以更明确地报告真正 "conflict"（两约束无法同时满足）的 batch 比例，但 38.2% 这个数字提供了部分信息。

**建议**：论文应补充报告 (a) 约束真正冲突（α_eff < τ at b=b_ESS）的 batch 比例，(b) 这些 batch 的 PPL 贡献。但这不构成论文结论的 fundamental threat，因为 ESS-only 的表现已经在 Table 1 中评估过。

---

## R1 的 Questions 补充回应

对 R1 提出的 5 个 Questions，作为 Reviewer 2 补充我的关注点：

1. **α_eff 与 downstream accuracy 的直接相关性**：同意这是关键问题。论文目前只建立了 α_eff → PPL 的间接链条，α_eff → downstream 的关系未验证。
2. **N=3 power analysis**：同意需要。基于 Δ=-0.020, SD≈0.007 的 paired t-test，80% power at α=0.05 大约需要 N=4-5 seeds（effect size d ≈ 2.86 很大，因为 SD 很小）。但正如 R1 指出的，如果 SD 被 deterministic training 人为压缩，真实所需 N 更大。
3. **Pearson vs Spearman 散点图**：同意应提供。
4. **更大模型 pilot**：强烈同意。即使是 1.7B 的 pilot 结果也会大幅增强说服力。论文提到 Qwen3-1.7B 但似乎仅在 Appendix 中有限使用。
5. **ρ=0.4 代表性**：同意这是重要问题。我在自己的 Questions Q3 中也问了同一个问题——Appendix N 显示 ρ=0.2 时方法 degrade，而 20% 正好是论文自己引用的 web contamination 估计下限。

---

## 总结

R1 和 R2 的审稿意见高度趋同。核心共识：

| 问题 | R1 | R2 | 一致性 |
|------|----|----|--------|
| N=3 统计效力不足 | Must-Fix N1 | Should-Fix W3 | 完全一致 |
| α_eff proxy 不可靠 | Must-Fix N2 | Should-Fix W5 | 完全一致 |
| 下游零改善 | Must-Fix N3 | Must-Fix N1 | 完全一致 |
| Self-contamination 生态效度 | Should-Fix W1 | Must-Fix N2 | 一致，我评级更高 |
| 方法新颖性增量 | Should-Fix W2 | Must-Fix N3 | 一致，我评级更高 |
| 效应量太小 | Should-Fix W3 | Must-Fix N1 | 一致，我评级更高 |
| ESS/α_eff 交互分析 | Should-Fix W4 | — | 我部分反驳 |

**唯一分歧**：R1-W4（ESS ceiling 与 α_eff floor 交互）。我认为论文通过 ESS-only baseline 和 minimum intervention 讨论隐式覆盖了约束冲突场景，但同意可以更明确地分析。

**评分对齐**：R1 Overall 3.0（Findings），R2 Overall 3.0（Findings）。两位 reviewer 独立达成一致，建议接收为 Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-23T03:17:39.041187+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-23T03:17:39.292541+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T03:05:48.390975+00:00\", \"completed_at\": \"2026-05-23T03:09:51.401130+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-4\", \"message\": \"连续两页无 display item。Page 3 有数学公式（部分缓解），但 page 4（Experimental Setup）为纯文本 + bullet list，审稿人在此段可能感到视觉疲劳。建议：可考虑将 Appendix 中的某个表（如 contamination setup 示意或 method comparison 的紧凑版）提前至 p.4 以打破文本单调。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 是文字摘要式概览框（colored boxes with text），不是传统图表/架构图。对分析型论文可行且信息传达有效，但若替换为因果关系流程图（epoch confound → detector requirements → adaptive method 的推导链），可进一步强化审稿人的第一印象锚定。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 在右栏中偏小，legend 文字和 axis label 接近可读性下限（估计 ~7-8pt）。marker 形状区分（三角 vs 圆）弥补了颜色区分度，色盲友好性尚可。若有空间可略微放大。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 caption 含 \\\"Note:\\\" 段落，信息自包含度优秀。↓ 方向标注、bold 最优值、± 标准差均规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3（Decision summary）使用 ✓/✗ 标记 + 条件化建议，对审稿人和读者都有 actionable 价值，排版整洁。\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Algorithm 1 伪代码格式规范，algorithmic 环境正确使用。\"}, {\"severity\": \"info\", \"dimension\": \"page 12-13\", \"message\": \"Appendix 图表密度高（Figure 3-5, Tables 5-8），可读但部分图（Figure 3 constraint regime decomposition）尺寸偏小。Appendix 中可接受。\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-23T03:17:39.293017+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-23T03:17:39.344025+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-23T03:19:42.914885+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "provenance_weight_training",
  "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成：检测器噪声占未解释方差 ~70%（边界区 q∈[0.4,0.6] 准确率 ~55%），b* 变换占 ~30%（ESS floor 约束的刻意设计）。B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44），证明瓶颈在检测器。§6 已写入完整定量分解段落。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句：proxy r=0.70 在 §3，seed 42 在 Table 1 脚注，ρ=0.2 在 §6。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。释放空间用于 decision summary table 移入主文。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11 issues (new, from fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。Paired t-test 仅 2 df，BCa bootstrap CI 在 N=3 时覆盖率无保证。Per-seed variance 可能被 deterministic training 人为压缩。建议至少 N=5。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.49，Spearman 校正后不显著，跨 seed 不稳定（r=0.17-0.75）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。Table 11 仅基于 5 个离散 b 值。跨 seed Pearson r 从 0.17 到 0.75 变化极大，一个种子 R²≈0.03 意味着 proxy 完全失效。BH 校正后 p=0.078。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.020, ~0.11%），论文 framing 存在 overclaim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4: adaptive 0.5414 = uniform 0.5414。5 个下游任务无一显著差异。Abstract 'yielding a practical adaptive method' 构成 overclaim。论文在 §6/Limitations 坦承但 framing 不匹配。整个方法类别的 upper bound（grid-best）也仅 ~0.2% PPL 改善。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"实验范围过窄：单模型/单数据集/self-contamination，不足以支撑一般性结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。Cross-model (Appendix O) 仅单 seed 且 mixed。ρ=0.2 时 degrade。Generator=trainee 使 AUC=0.94 有人为优势。Three effectiveness conditions 的一般性缺乏多设置验证。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2 列为 must-fix，R1 列为 should-fix（认为 zero-cost 接近 grid-best 有实践价值，问题在 positioning 非方法无效）。w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。Adaptive vs grid-best: 17.674 vs 17.657。双方同意以 analysis paper 定位更合适。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Analysis paper vs method paper 定位不清晰，Abstract 同时 claim 双重贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 同时 claim 'we analyze' + 'we derive adaptive b*'。Epoch confound 分析远比 adaptive method 有说服力。建议明确以分析为主线，adaptive b* 降级为 practical implication。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失：Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733)、Self-Influence Guided Data Reweighting (ICLR 2025)、ToReMi (arXiv:2504.00695)、LLM-Generated Text Detection Survey (Wu et al. 2025)。R1 部分同意但需核实真实性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏对 prior work 实验设置的具体分析\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Epoch confound 概念上非完全出乎意料（减少数据→更多 epoch 是自然推论）。贡献在于严格实验验证，但需讨论 Drayson et al. 等 prior work 是否控制了 epoch、为何被忽略。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m1\"\n  summary: \"ESS ceiling 与 α_eff floor 约束冲突时的行为缺乏明确分析\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"R1 提出，R2 部分反驳（ESS-only baseline 隐式覆盖了极端情况）。建议补充报告真正冲突（α_eff < τ at b=b_ESS）的 batch 比例及 PPL 贡献。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 2 可读性偏弱，脚注密度过高，小数位不一致等格式问题\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。12+ 脚注含关键技术细节。Table 2 小数位不一致。'practical' 一词使用频率过高。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m3\"\n  summary: \"Appendix 过于庞大（5 页 17 个子附录），关键证据未在正文充分引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Appendix K (α_eff validation) 和 Appendix N (low contamination) 对核心论点很重要但正文引用不充分。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "provenance_weight_training",
    "issues_yaml": "issues:\n# === Round 10 issues (all resolved, retained for history) ===\n- id: \"R10-C1\"\n  summary: \"Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。\"\n  resolution: \"tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。\"\n  resolution_round: 10\n\n- id: \"R10-C2\"\n  summary: \"多重比较未校正，p=0.025 Bonferroni 校正后不显著\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。\"\n  resolution: \"BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。\"\n  resolution_round: 10\n\n- id: \"R10-C3\"\n  summary: \"方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。\"\n  resolution: \"§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。\"\n  resolution_round: 10\n\n- id: \"R10-C4\"\n  summary: \"Downstream task 零改善削弱实际意义\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。\"\n  resolution: \"Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"实验规模和场景过于狭窄，ρ=0.3 缺失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 0.6B/1.7B，self-contamination，ρ=0.3 缺失。Claim 范围超过验证范围。\"\n  resolution: \"ρ=0.3 2-seed 完成：holdout Δ=+0.001（噪声内），确认 transition boundary 在 [0.3, 0.4]。Appendix R + rebuttal M1 已填入数据。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"论文定位仍存在模糊性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract analysis + method 混合。§3 ~1.5 页对 analysis 偏重。\"\n  resolution: \"与 C3 合并完成。\"\n  resolution_round: 10\n\n- id: \"R10-M3\"\n  summary: \"α_eff proxy 质量偏弱（r=0.70, R²=0.49）\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"49% 未解释方差来源未分析。Soft label 替代方案未讨论。\"\n  resolution: \"定量方差分解完成：检测器噪声占未解释方差 ~70%（边界区 q∈[0.4,0.6] 准确率 ~55%），b* 变换占 ~30%（ESS floor 约束的刻意设计）。B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44），证明瓶颈在检测器。§6 已写入完整定量分解段落。\"\n  resolution_round: 10\n\n- id: \"R10-M4\"\n  summary: \"Self-contamination 生态效度有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Cross-model transfer mixed。PPL 比较被省略。\"\n  resolution: \"§4 末尾加 self-contamination controlled testbed 预告句 + cross-model reference。\"\n  resolution_round: 10\n\n- id: \"R10-m1\"\n  summary: \"B=4 dual constraint 统计可靠性存疑\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"α_eff(0) 仅 5 值。b* distribution 未报告。\"\n  resolution: \"B=8/16 改善 granularity 已在论文中。B=4 限制在 §6 已讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m2\"\n  summary: \"关键证据仅在附录\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Proxy validation, seed 42 artifact, ρ=0.2 失效影响 core claims。\"\n  resolution: \"正文已加引用句：proxy r=0.70 在 §3，seed 42 在 Table 1 脚注，ρ=0.2 在 §6。\"\n  resolution_round: 10\n\n- id: \"R10-m3\"\n  summary: \"Responsible NLP Checklist 出现在 PDF 中\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"EMNLP 2026 规定 checklist 在 OpenReview 表单。\"\n  resolution: \"Checklist 从 PDF 移除。释放空间用于 decision summary table 移入主文。\"\n  resolution_round: 10\n\n- id: \"R10-m4\"\n  summary: \"效应量极小需 cost-benefit 论证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"Δ=-0.020 PPL ~0.11% relative。需检测器开销 vs 改善分析。\"\n  resolution: \"§6 Effect size 段落已包含 cost-benefit 讨论。\"\n  resolution_round: 10\n\n- id: \"R10-m5\"\n  summary: \"小格式问题（ρ 定义、Figure 2 灰度、Table 2 4σ）\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"ρ token/doc 区分、Figure 2 marker、Table 2 4σ。\"\n  resolution: \"ρ 加 (token-level)，Figure 2 caption 加 marker 区分说明。\"\n  resolution_round: 10\n\n# === Round 11 issues (new, from fresh review) ===\n\n- id: \"R11-C1\"\n  summary: \"N=3 seeds 统计检验力严重不足，2 自由度无法可靠支撑定量结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 列为 must-fix，R2 列为 should-fix 但交叉回应时同意升级。Paired t-test 仅 2 df，BCa bootstrap CI 在 N=3 时覆盖率无保证。Per-seed variance 可能被 deterministic training 人为压缩。建议至少 N=5。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C2\"\n  summary: \"α_eff proxy 可靠性存疑：R²≈0.49，Spearman 校正后不显著，跨 seed 不稳定（r=0.17-0.75）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Pearson r=0.70 vs Spearman ρ=0.40 差距暗示极端值驱动。Table 11 仅基于 5 个离散 b 值。跨 seed Pearson r 从 0.17 到 0.75 变化极大，一个种子 R²≈0.03 意味着 proxy 完全失效。BH 校正后 p=0.078。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C3\"\n  summary: \"下游任务零改善 + 效应量极小（Δ=-0.020, ~0.11%），论文 framing 存在 overclaim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Table 4: adaptive 0.5414 = uniform 0.5414。5 个下游任务无一显著差异。Abstract 'yielding a practical adaptive method' 构成 overclaim。论文在 §6/Limitations 坦承但 framing 不匹配。整个方法类别的 upper bound（grid-best）也仅 ~0.2% PPL 改善。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-C4\"\n  summary: \"实验范围过窄：单模型/单数据集/self-contamination，不足以支撑一般性结论\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"仅 Qwen3-0.6B + FineWeb 132M + self-generated contamination。Cross-model (Appendix O) 仅单 seed 且 mixed。ρ=0.2 时 degrade。Generator=trainee 使 AUC=0.94 有人为优势。Three effectiveness conditions 的一般性缺乏多设置验证。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Adaptive b* 方法新颖性不足，本质是 Drayson et al. 框架的参数选择启发式\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2 列为 must-fix，R1 列为 should-fix（认为 zero-cost 接近 grid-best 有实践价值，问题在 positioning 非方法无效）。w=(1-q)^b 100% 来自 Drayson et al.，Proposition 1-2 trivial。Adaptive vs grid-best: 17.674 vs 17.657。双方同意以 analysis paper 定位更合适。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"Analysis paper vs method paper 定位不清晰，Abstract 同时 claim 双重贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 同时 claim 'we analyze' + 'we derive adaptive b*'。Epoch confound 分析远比 adaptive method 有说服力。建议明确以分析为主线，adaptive b* 降级为 practical implication。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Related Work 遗漏近期 instance-level reweighting 工作\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"缺失：Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733)、Self-Influence Guided Data Reweighting (ICLR 2025)、ToReMi (arXiv:2504.00695)、LLM-Generated Text Detection Survey (Wu et al. 2025)。R1 部分同意但需核实真实性。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Epoch confound 讨论缺乏对 prior work 实验设置的具体分析\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Epoch confound 概念上非完全出乎意料（减少数据→更多 epoch 是自然推论）。贡献在于严格实验验证，但需讨论 Drayson et al. 等 prior work 是否控制了 epoch、为何被忽略。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m1\"\n  summary: \"ESS ceiling 与 α_eff floor 约束冲突时的行为缺乏明确分析\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"R1 提出，R2 部分反驳（ESS-only baseline 隐式覆盖了极端情况）。建议补充报告真正冲突（α_eff < τ at b=b_ESS）的 batch 比例及 PPL 贡献。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Figure 2 可读性偏弱，脚注密度过高，小数位不一致等格式问题\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Figure 2 偏小、灰度难区分。12+ 脚注含关键技术细节。Table 2 小数位不一致。'practical' 一词使用频率过高。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m3\"\n  summary: \"Appendix 过于庞大（5 页 17 个子附录），关键证据未在正文充分引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Appendix K (α_eff validation) 和 Appendix N (low contamination) 对核心论点很重要但正文引用不充分。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-23T03:19:43.066801+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml\", \"bytes\": 10251}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-23T03:22:20.360084+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "provenance_weight_training",
  "report": "# 审稿报告：Round 11（Fresh Review）\n\n**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性/实验/统计；R2: 新颖性/Related Work/写作/格式）\n**交叉轮次**: 1 轮（达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight 范式在 LM continued pretraining 中的有效性条件。通过 Qwen3-0.6B 在 132M FineWeb tokens 上的受控实验（ρ=0.4，3 seeds），论文提出三个发现：(1) D&R 评估中的 epoch confound——>95% 的 PPL 优势来自多 epoch 暴露而非过滤质量；(2) 有效 reweighting 需要检测器同时具备足够的判别力（AUC）和良好的校准（ECE）；(3) minimum intervention 优于 unconstrained maximization。基于此，论文推导了一个 dual-constrained adaptive b*，在 ρ≥0.4 时持续优于 uniform（Δ=−0.020 at ρ=0.4，Δ=−0.032 at ρ=0.6），但下游任务无显著改善。\n\n---\n\n## Strengths\n\n1. **Epoch confound 分析设计精巧且结论有力** [R1, R2 一致]\n   - 通过 epoch-matched 对照（Table 1）将 D&R 优势从 0.396 分解为仅 Δ=0.017，严格证明 >95% 来自多 epoch 暴露\n   - Independent-LR replication（Δ=0.006）排除了 LR schedule 混淆\n   - Permuted-score control 确认 detector signal 是 load-bearing 的\n   - 这对整个 D&R 文献是重要的方法论校正\n\n2. **三条 effectiveness conditions 形成实用决策框架** [R1, R2 一致]\n   - Table 3 的决策矩阵（detector AUC ≥ 0.9, ECE ≤ 0.05, ρ ≥ 0.4）对从业者有直接参考价值\n   - 每个条件通过消融实验建立，逻辑结构清晰\n\n3. **诚实的 negative results 报告** [R1, R2 一致]\n   - 坦承下游零改善（Table 4）、α_eff 校正后不显著（p_BH=0.078）、ρ=0.2 时退化、N=3 的统计限制\n   - 透明度值得肯定\n\n4. **LR-controlled verification 等实验细节严谨** [R2]\n   - 对 epoch-matched 结果用独立 LR schedule 二次验证，排除 confound\n   - Appendix 覆盖广泛（proofs、grid search、sensitivity、cross-model、low contamination），信息密度高\n\n5. **可复现性良好** [R1: 4/5]\n   - 超参数、训练配置、检测器细节（temperature scaling T=0.204）报告充分\n   - 承诺 release code/data（review 期间无匿名 repo）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. N=3 seeds 统计检验力严重不足** [R1 Must-Fix, R2 Should-Fix→交叉后升级为 Agree]\n- 全部主实验仅 3 random seeds（42, 123, 456），paired t-test 仅 2 自由度\n- 核心 claim Δ=−0.020 的 95% BCa bootstrap CI [−0.028, −0.012]：BCa 的 bias-correction 和 acceleration 参数需从 jackknife 估计，N=3 时仅 3 个 jackknife 样本，参数估计本身极不稳定，覆盖率无保证\n- Per-seed 方差极小（SD≈0.007），可能被 deterministic training recipe 人为压缩，低估真实实验不确定性\n- Bonferroni-Holm 校正后 ρ=0.4 的 p_BH=0.078 未达显著水平\n- **注**：R2 补充指出 epoch confound 的定性结论（>95% 来自 multi-epoch）受此影响较小，因方向在 3 seeds 中完全一致；统计效力问题主要影响 adaptive b* 的定量精度\n\n**C2. α_eff proxy 可靠性严重不足** [R1 Must-Fix, R2 Should-Fix→交叉后 Agree]\n- α_eff 与 true batch-level real fraction 的 Pearson r≈0.70（R²≈0.49），仅解释一半方差\n- Pearson r=0.70 vs Spearman ρ=0.40 差距巨大：线性相关强但秩相关弱，暗示少数极端 batch 驱动相关，大多数 batch 排序不可靠——对 threshold-based 决策（α_eff ≥ τ）尤其危险\n- 跨 seed 不稳定：Table 11 Pearson r 从 0.17 到 0.75 变化极大，r=0.17 的种子意味着 proxy 几乎完全失效（R²≈0.03）\n- Table 11 仅基于 5 个离散 b 值（0, 0.25, 0.5, 0.75, 1），相关系数的估计本身不稳定\n- 整个 adaptive 方法的 \"自适应\" 部分依赖 α_eff 作为 quality signal，proxy 不可靠则 bisection 找到的 b* 可能系统性偏离最优值\n\n**C3. 下游任务零改善 + 效应量极小，论文 framing 存在 overclaim** [R1 Must-Fix + Should-Fix, R2 Must-Fix]\n- Table 4: 5 个下游任务 adaptive (0.5414) = uniform (0.5414)，\"All differences within standard error\"\n- Epoch-matched 条件下 adaptive vs uniform 的真实改善仅 Δ=−0.020 PPL（~0.11% relative）\n- 即使 grid-best（post-hoc oracle），改善也仅 ~0.2%（17.657 vs 17.694），整个方法类别的天花板极低\n- Abstract 中 \"yielding a practical adaptive method\" 构成 overclaim：一个在下游任务上零改善的方法难以被称为 \"practical\"\n- 论文在 §6 和 Limitations 中坦承了这些事实，但 Abstract/Intro 的 framing 与实际结果不匹配\n\n**C4. 实验范围过窄，不足以支撑一般性结论** [R1 Should-Fix, R2 Must-Fix]\n- 仅 Qwen3-0.6B（0.6B params）、FineWeb 132M tokens、self-generated contamination（generator=trainee）\n- Self-contamination 使 AUC=0.94 具有人为优势：generator=trainee 时检测器可利用自身 decoding 的统计规律性，真实 web contamination 中 AUC 可能显著更低\n- Cross-model 实验（Appendix O, Llama-3.2-3B）仅单 seed 且结果 mixed（MMLU↑, HellaSwag↓）\n- ρ=0.2 时方法 degrade（Appendix Q, Δ=+0.046），而 20% 正是论文自己引用的 web contamination 估计下限\n- \"Three effectiveness conditions\" 的一般性结论缺乏多模型/多数据集/cross-model contamination 验证\n- **R1 补充**：三个条件作为 necessary conditions 的逻辑结构合理，但论文措辞有时暗示了更强的一般性\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. Adaptive b* 方法新颖性不足** [R2 Must-Fix, R1 Should-Fix]\n- w=(1−q)^b 框架完全来自 Drayson et al. (2025)\n- Dual-constrained b* 本质是参数选择启发式：两约束优化 + bisection 求解，Proposition 1-2 为标准单调性推导\n- Adaptive vs grid-best: 17.674 vs 17.657，效果几乎无差异\n- **R1 补充（部分反驳 R2）**：adaptive 方法的价值在于 zero-cost 接近 grid-best（grid search 需 9 次完整训练），17.674 vs 17.657 说明方法有效而非无价值。问题在于 positioning 而非方法无效\n- **共识**：新颖性问题可通过明确 analysis paper 定位缓解——将 adaptive b* 降级为 practical corollary\n\n**W2. Analysis paper vs method paper 定位不清晰** [R1 Agree, R2 Should-Fix]\n- Abstract 同时 claim \"we analyze when, why, and how\" + \"we derive a dual-constrained adaptive b*\"\n- Epoch confound 分析远比 adaptive method 有说服力\n- 建议明确以分析为主线，adaptive b* 为实践推论\n\n**W3. Related Work 遗漏近期 instance-level reweighting 工作** [R2 提出, R1 部分同意]\n- 可能遗漏的直接相关工作：\n  - Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733, Feb 2025)\n  - Self-Influence Guided Data Reweighting (ICLR 2025)\n  - ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695, 2025)\n  - LLM-Generated Text Detection Survey (Wu et al. 2025, Computational Linguistics)\n- 论文应讨论 provenance-based reweighting 与 loss-based/influence-based 信号的区别\n- R1 提醒：blind review 条件下需核实这些引用的真实性和相关性\n\n**W4. Epoch confound 讨论缺乏对 prior work 的具体分析** [R1 Agree, R2 提出]\n- \"过滤数据→更多 epoch\" 概念上非完全出乎意料\n- 贡献在于严格实验验证，但需讨论：Drayson et al. 等 prior work 是否控制了 epoch？为何被忽略？\n- 可能原因包括：prior work 关注 absolute performance 而非 epoch-controlled comparison；from-scratch pretraining 中 confound 不如 continued pretraining 明显\n\n### Minor（不影响接收）\n\n**m1. ESS/α_eff 约束冲突行为缺乏明确分析** [R1 提出, R2 部分反驳]\n- 约束冲突时退回 b=b_ESS 的频率和后果未明确报告\n- R2 反驳：ESS-only baseline（Table 2, 17.737）已隐式展示约束冲突的极端行为；minimum intervention 原则保证退回行为合理\n- 共识：建议补充真正冲突（α_eff < τ at b=b_ESS）的 batch 比例，但不构成 fundamental threat\n\n**m2. 格式小问题** [R1, R2]\n- Figure 2 偏小，legend 接近可读性下限（~7-8pt），灰度打印下 marker 难区分\n- 12+ 脚注含关键技术细节（footnote 1 batch composition, footnote 2 rounding），建议关键内容移入正文\n- Table 2 小数位不一致\n- \"practical\" 一词使用频率过高\n\n**m3. Appendix 过于庞大** [R1, R2]\n- 5 页 17 个子附录（A-Q）\n- Appendix K（α_eff validation）和 Appendix N（low contamination）对核心论点很重要但正文引用不充分\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 交叉后一致性 |\n|------|----|----|-------------|\n| N=3 统计效力不足 | Must-Fix (N1) | Should-Fix (W3) → AGREE 升级 | **一致：Must-Fix** |\n| α_eff proxy 不可靠 | Must-Fix (N2) | Should-Fix (W5) → AGREE | **一致：Must-Fix** |\n| 下游零改善 + 效应量小 | Must-Fix (N3) + Should-Fix (W3) | Must-Fix (N1) | **一致：Must-Fix** |\n| 实验范围过窄 | Should-Fix (W1) | Must-Fix (N2) | **一致：Critical** |\n| 方法新颖性 | Should-Fix (W2) | Must-Fix (N3) → R1 PARTIALLY REBUT | **轻微分歧：R1 认为 should-fix（zero-cost 有价值），R2 认为 critical** |\n| 论文定位 | AGREE (W4) | Should-Fix (W4) | **一致** |\n| Missing references | PARTIALLY AGREE (W1) | Should-Fix (W1) | **一致** |\n\n## Reviewer Divergence\n\n**唯一实质分歧**：Adaptive b* 新颖性的严重程度\n- R2：Must-Fix critical——本质是参数选择启发式，Proposition 1-2 trivial，与 grid-best 几乎无差异\n- R1：Should-Fix——zero-cost 接近 grid-best 有实践价值（省去 9 次完整训练），问题在于 positioning 而非方法无效\n- **Director 判断**：R1 的论点更有说服力。Adaptive b* 确实新颖性有限，但 zero-cost 替代 grid search 是有实际意义的工程贡献。归类为 Should-Fix，可通过论文定位调整（analysis paper + practical corollary）缓解。\n\n---\n\n## Questions\n\n1. **Power analysis**：给定 Δ=0.020, SD≈0.007，N=3 的 statistical power 是多少？80% power 需要多少 seeds？\n2. **α_eff 散点图**：Pearson r=0.70 vs Spearman ρ=0.40 差异的原因？能否提供 α_eff vs true real fraction 的散点图？\n3. **α_eff 与 downstream 的直接关系**：α_eff → PPL 链条已建立，但 α_eff → downstream accuracy 未验证\n4. **Cross-model contamination**：三个 effectiveness conditions 在 generator≠trainee 场景下是否成立？\n5. **ρ=0.2 代表性**：方法在论文自己引用的 contamination 下限（20%）即退化，是否意味着仅适用于高污染场景？\n6. **Drayson et al. 的 epoch confound**：他们的实验是否控制了 content epochs？他们的 b=10 结果中有多少可用 epoch confound 解释？\n\n---\n\n## Missing References\n\n1. Dynamic Loss-Based Sample Reweighting for LLM Pretraining (arXiv:2502.06733, 2025) — instance-level dynamic reweighting\n2. Self-Influence Guided Data Reweighting for LM Pre-training (ICLR 2025) — self-influence based reweighting\n3. ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695, 2025) — topic-aware dynamic reweighting\n4. A Survey on LLM-Generated Text Detection (Wu et al. 2025, Computational Linguistics) — 最新 MGT detection 综述\n\n（注：以上引用由 R2 提出，R1 在 blind review 条件下无法独立核实，建议作者核实后酌情引用）\n\n---\n\n## External Review\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时约 4 分钟）\n\n| 严重性 | 数量 |\n|--------|------|\n| Critical | 0 |\n| Warning | 1 |\n| Info | 6 |\n\n关键发现：\n- **[Warning] Pages 3-4 连续两页无 display item**：Page 3 有数学公式（部分缓解），但 Page 4（Experimental Setup）为纯文本 + bullet list，可能造成视觉疲劳。建议从 Appendix 提前一个表或图至 p.4。\n- **[Info] Figure 1 为文字摘要式概览框**：对 analysis 论文可行，但替换为因果关系流程图可能更有效。\n- **[Info] Figure 2 偏小**：legend 和 axis label 接近可读性下限（~7-8pt），marker 形状区分尚可。\n- **[Info] Table 1 caption 信息自包含度优秀**，Table 3 排版整洁有 actionable 价值。\n- **[Info] Appendix 图表密度高但可接受**。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings**\n**置信度：4/5**（两位 Reviewer 独立达成一致评分，交叉后核心问题高度收敛）\n\n### 评分理由\n\n**论文的核心价值在于 epoch confound 的分析发现，而非 adaptive reweighting 方法本身。**\n\nEpoch confound 分析（>95% 的 D&R 优势来自多 epoch 暴露）是对 D&R 文献有价值的方法论校正，实验设计精巧（epoch-matched controls + LR replication + permuted-score control），足以支撑 Findings 级别接收。\n\n但论文未达到主会议（4.0）门槛，原因如下：\n1. **统计基础脆弱**：N=3 seeds（2 df），BH 校正后 ρ=0.4 不显著（p=0.078），bootstrap CI 可靠性存疑\n2. **方法贡献的核心 proxy 不可靠**：α_eff R²=0.49，跨 seed r 从 0.17 到 0.75，Spearman 校正后不显著\n3. **实际影响极小**：Δ=−0.020 PPL（~0.11%），下游任务零改善，整个方法类别的 upper bound 也仅 ~0.2%\n4. **实验范围过窄**：单模型/单数据集/self-contamination，ρ=0.2 时退化，cross-model 结果 mixed\n5. **方法新颖性有限**：w=(1−q)^b 完全来自 Drayson et al.，adaptive b* 是增量式参数选择规则\n\n### 与 EMNLP 2026 评分标准的对应\n- 3.0 = Findings：有价值的分析贡献（epoch confound），但效应量、实验范围和方法新颖性不足以进入主会议\n- 不够 3.5 (Borderline Conference)：缺少更广泛的实验验证和有意义的下游改善\n- 高于 2.5 (Borderline Findings)：epoch confound 发现对社区有实际价值，实验设计严谨，报告诚实\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"yielding a practical adaptive method\" 措辞建议修改为更谦虚的表述，如 \"as a practical corollary, we derive...\"（论文部分已这么做，但 Abstract 和 Intro 的 leading sentence 仍偏强）\n- Figure 1 的 TikZ 概览框有效但可考虑改为因果流程图\n\n### §3 Method\n- 已从 Round 10 的 1.5 页压缩至 ~0.75 页，改进明显\n- Proposition 1-2 虽正确但 trivial，建议保留在 Appendix\n- α_eff 的 Pearson r≈0.70 在正文中提及，但未提及 Spearman ρ=0.40 和跨 seed 不稳定性——正文应更完整地反映 proxy 的局限\n\n### §4 Experimental Setup\n- Self-contamination 预告句已加，但讨论仍不足——建议增加一句关于 generator=trainee 对 detector AUC 的人为优势\n- Page 4 无 display item，视觉节奏偏单调\n\n### §5 Results\n- Table 1（epoch-matched）和 Table 2（main results）设计清晰，caption 信息自包含\n- §5.1 建议在开头就明确区分 \"full advantage (0.396)\" 和 \"epoch-controlled advantage (0.020)\"\n- §5.2-5.3 的 ablation/sensitivity 分析充实\n\n### §6 Discussion\n- Effect size 讨论和 downstream null 分析已有改进\n- α_eff 方差分解段落有价值，但应补充跨 seed 不稳定性的讨论\n- \"When uniform beats reweighting\" 段落对从业者有实际指导价值\n\n### §7 Conclusion\n- 与 Abstract 基调一致但偏乐观，batch-size amplification 的外推是 speculative（论文已承认）\n\n### Limitations\n- 覆盖模型规模、数据范围、seed 数量、self-contamination，合理但可以更强调 ρ=0.2 退化的 implications\n\n### References\n- 格式基本一致，部分 arXiv preprint 未标注会议版本（如已被接收）\n- 建议核实并补充 R2 提出的 4 篇遗漏引用\n\n### Appendix\n- 内容丰富（A-Q, 17 节），但 Appendix K（α_eff validation）和 Appendix N（low contamination）的结论对核心 claims 影响大，建议在正文更显著地引用",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "provenance_weight_training",
    "report": "# 审稿报告：Round 11（Fresh Review）\n\n**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性/实验/统计；R2: 新颖性/Related Work/写作/格式）\n**交叉轮次**: 1 轮（达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文研究 detect-and-reweight 范式在 LM continued pretraining 中的有效性条件。通过 Qwen3-0.6B 在 132M FineWeb tokens 上的受控实验（ρ=0.4，3 seeds），论文提出三个发现：(1) D&R 评估中的 epoch confound——>95% 的 PPL 优势来自多 epoch 暴露而非过滤质量；(2) 有效 reweighting 需要检测器同时具备足够的判别力（AUC）和良好的校准（ECE）；(3) minimum intervention 优于 unconstrained maximization。基于此，论文推导了一个 dual-constrained adaptive b*，在 ρ≥0.4 时持续优于 uniform（Δ=−0.020 at ρ=0.4，Δ=−0.032 at ρ=0.6），但下游任务无显著改善。\n\n---\n\n## Strengths\n\n1. **Epoch confound 分析设计精巧且结论有力** [R1, R2 一致]\n   - 通过 epoch-matched 对照（Table 1）将 D&R 优势从 0.396 分解为仅 Δ=0.017，严格证明 >95% 来自多 epoch 暴露\n   - Independent-LR replication（Δ=0.006）排除了 LR schedule 混淆\n   - Permuted-score control 确认 detector signal 是 load-bearing 的\n   - 这对整个 D&R 文献是重要的方法论校正\n\n2. **三条 effectiveness conditions 形成实用决策框架** [R1, R2 一致]\n   - Table 3 的决策矩阵（detector AUC ≥ 0.9, ECE ≤ 0.05, ρ ≥ 0.4）对从业者有直接参考价值\n   - 每个条件通过消融实验建立，逻辑结构清晰\n\n3. **诚实的 negative results 报告** [R1, R2 一致]\n   - 坦承下游零改善（Table 4）、α_eff 校正后不显著（p_BH=0.078）、ρ=0.2 时退化、N=3 的统计限制\n   - 透明度值得肯定\n\n4. **LR-controlled verification 等实验细节严谨** [R2]\n   - 对 epoch-matched 结果用独立 LR schedule 二次验证，排除 confound\n   - Appendix 覆盖广泛（proofs、grid search、sensitivity、cross-model、low contamination），信息密度高\n\n5. **可复现性良好** [R1: 4/5]\n   - 超参数、训练配置、检测器细节（temperature scaling T=0.204）报告充分\n   - 承诺 release code/data（review 期间无匿名 repo）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. N=3 seeds 统计检验力严重不足** [R1 Must-Fix, R2 Should-Fix→交叉后升级为 Agree]\n- 全部主实验仅 3 random seeds（42, 123, 456），paired t-test 仅 2 自由度\n- 核心 claim Δ=−0.020 的 95% BCa bootstrap CI [−0.028, −0.012]：BCa 的 bias-correction 和 acceleration 参数需从 jackknife 估计，N=3 时仅 3 个 jackknife 样本，参数估计本身极不稳定，覆盖率无保证\n- Per-seed 方差极小（SD≈0.007），可能被 deterministic training recipe 人为压缩，低估真实实验不确定性\n- Bonferroni-Holm 校正后 ρ=0.4 的 p_BH=0.078 未达显著水平\n- **注**：R2 补充指出 epoch confound 的定性结论（>95% 来自 multi-epoch）受此影响较小，因方向在 3 seeds 中完全一致；统计效力问题主要影响 adaptive b* 的定量精度\n\n**C2. α_eff proxy 可靠性严重不足** [R1 Must-Fix, R2 Should-Fix→交叉后 Agree]\n- α_eff 与 true batch-level real fraction 的 Pearson r≈0.70（R²≈0.49），仅解释一半方差\n- Pearson r=0.70 vs Spearman ρ=0.40 差距巨大：线性相关强但秩相关弱，暗示少数极端 batch 驱动相关，大多数 batch 排序不可靠——对 threshold-based 决策（α_eff ≥ τ）尤其危险\n- 跨 seed 不稳定：Table 11 Pearson r 从 0.17 到 0.75 变化极大，r=0.17 的种子意味着 proxy 几乎完全失效（R²≈0.03）\n- Table 11 仅基于 5 个离散 b 值（0, 0.25, 0.5, 0.75, 1），相关系数的估计本身不稳定\n- 整个 adaptive 方法的 \"自适应\" 部分依赖 α_eff 作为 quality signal，proxy 不可靠则 bisection 找到的 b* 可能系统性偏离最优值\n\n**C3. 下游任务零改善 + 效应量极小，论文 framing 存在 overclaim** [R1 Must-Fix + Should-Fix, R2 Must-Fix]\n- Table 4: 5 个下游任务 adaptive (0.5414) = uniform (0.5414)，\"All differences within standard error\"\n- Epoch-matched 条件下 adaptive vs uniform 的真实改善仅 Δ=−0.020 PPL（~0.11% relative）\n- 即使 grid-best（post-hoc oracle），改善也仅 ~0.2%（17.657 vs 17.694），整个方法类别的天花板极低\n- Abstract 中 \"yielding a practical adaptive method\" 构成 overclaim：一个在下游任务上零改善的方法难以被称为 \"practical\"\n- 论文在 §6 和 Limitations 中坦承了这些事实，但 Abstract/Intro 的 framing 与实际结果不匹配\n\n**C4. 实验范围过窄，不足以支撑一般性结论** [R1 Should-Fix, R2 Must-Fix]\n- 仅 Qwen3-0.6B（0.6B params）、FineWeb 132M tokens、self-generated contamination（generator=trainee）\n- Self-contamination 使 AUC=0.94 具有人为优势：generator=trainee 时检测器可利用自身 decoding 的统计规律性，真实 web contamination 中 AUC 可能显著更低\n- Cross-model 实验（Appendix O, Llama-3.2-3B）仅单 seed 且结果 mixed（MMLU↑, HellaSwag↓）\n- ρ=0.2 时方法 degrade（Appendix Q, Δ=+0.046），而 20% 正是论文自己引用的 web contamination 估计下限\n- \"Three effectiveness conditions\" 的一般性结论缺乏多模型/多数据集/cross-model contamination 验证\n- **R1 补充**：三个条件作为 necessary conditions 的逻辑结构合理，但论文措辞有时暗示了更强的一般性\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. Adaptive b* 方法新颖性不足** [R2 Must-Fix, R1 Should-Fix]\n- w=(1−q)^b 框架完全来自 Drayson et al. (2025)\n- Dual-constrained b* 本质是参数选择启发式：两约束优化 + bisection 求解，Proposition 1-2 为标准单调性推导\n- Adaptive vs grid-best: 17.674 vs 17.657，效果几乎无差异\n- **R1 补充（部分反驳 R2）**：adaptive 方法的价值在于 zero-cost 接近 grid-best（grid search 需 9 次完整训练），17.674 vs 17.657 说明方法有效而非无价值。问题在于 positioning 而非方法无效\n- **共识**：新颖性问题可通过明确 analysis paper 定位缓解——将 adaptive b* 降级为 practical corollary\n\n**W2. Analysis paper vs method paper 定位不清晰** [R1 Agree, R2 Should-Fix]\n- Abstract 同时 claim \"we analyze when, why, and how\" + \"we derive a dual-constrained adaptive b*\"\n- Epoch confound 分析远比 adaptive method 有说服力\n- 建议明确以分析为主线，adaptive b* 为实践推论\n\n**W3. Related Work 遗漏近期 instance-level reweighting 工作** [R2 提出, R1 部分同意]\n- 可能遗漏的直接相关工作：\n  - Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733, Feb 2025)\n  - Self-Influence Guided Data Reweighting (ICLR 2025)\n  - ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695, 2025)\n  - LLM-Generated Text Detection Survey (Wu et al. 2025, Computational Linguistics)\n- 论文应讨论 provenance-based reweighting 与 loss-based/influence-based 信号的区别\n- R1 提醒：blind review 条件下需核实这些引用的真实性和相关性\n\n**W4. Epoch confound 讨论缺乏对 prior work 的具体分析** [R1 Agree, R2 提出]\n- \"过滤数据→更多 epoch\" 概念上非完全出乎意料\n- 贡献在于严格实验验证，但需讨论：Drayson et al. 等 prior work 是否控制了 epoch？为何被忽略？\n- 可能原因包括：prior work 关注 absolute performance 而非 epoch-controlled comparison；from-scratch pretraining 中 confound 不如 continued pretraining 明显\n\n### Minor（不影响接收）\n\n**m1. ESS/α_eff 约束冲突行为缺乏明确分析** [R1 提出, R2 部分反驳]\n- 约束冲突时退回 b=b_ESS 的频率和后果未明确报告\n- R2 反驳：ESS-only baseline（Table 2, 17.737）已隐式展示约束冲突的极端行为；minimum intervention 原则保证退回行为合理\n- 共识：建议补充真正冲突（α_eff < τ at b=b_ESS）的 batch 比例，但不构成 fundamental threat\n\n**m2. 格式小问题** [R1, R2]\n- Figure 2 偏小，legend 接近可读性下限（~7-8pt），灰度打印下 marker 难区分\n- 12+ 脚注含关键技术细节（footnote 1 batch composition, footnote 2 rounding），建议关键内容移入正文\n- Table 2 小数位不一致\n- \"practical\" 一词使用频率过高\n\n**m3. Appendix 过于庞大** [R1, R2]\n- 5 页 17 个子附录（A-Q）\n- Appendix K（α_eff validation）和 Appendix N（low contamination）对核心论点很重要但正文引用不充分\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 交叉后一致性 |\n|------|----|----|-------------|\n| N=3 统计效力不足 | Must-Fix (N1) | Should-Fix (W3) → AGREE 升级 | **一致：Must-Fix** |\n| α_eff proxy 不可靠 | Must-Fix (N2) | Should-Fix (W5) → AGREE | **一致：Must-Fix** |\n| 下游零改善 + 效应量小 | Must-Fix (N3) + Should-Fix (W3) | Must-Fix (N1) | **一致：Must-Fix** |\n| 实验范围过窄 | Should-Fix (W1) | Must-Fix (N2) | **一致：Critical** |\n| 方法新颖性 | Should-Fix (W2) | Must-Fix (N3) → R1 PARTIALLY REBUT | **轻微分歧：R1 认为 should-fix（zero-cost 有价值），R2 认为 critical** |\n| 论文定位 | AGREE (W4) | Should-Fix (W4) | **一致** |\n| Missing references | PARTIALLY AGREE (W1) | Should-Fix (W1) | **一致** |\n\n## Reviewer Divergence\n\n**唯一实质分歧**：Adaptive b* 新颖性的严重程度\n- R2：Must-Fix critical——本质是参数选择启发式，Proposition 1-2 trivial，与 grid-best 几乎无差异\n- R1：Should-Fix——zero-cost 接近 grid-best 有实践价值（省去 9 次完整训练），问题在于 positioning 而非方法无效\n- **Director 判断**：R1 的论点更有说服力。Adaptive b* 确实新颖性有限，但 zero-cost 替代 grid search 是有实际意义的工程贡献。归类为 Should-Fix，可通过论文定位调整（analysis paper + practical corollary）缓解。\n\n---\n\n## Questions\n\n1. **Power analysis**：给定 Δ=0.020, SD≈0.007，N=3 的 statistical power 是多少？80% power 需要多少 seeds？\n2. **α_eff 散点图**：Pearson r=0.70 vs Spearman ρ=0.40 差异的原因？能否提供 α_eff vs true real fraction 的散点图？\n3. **α_eff 与 downstream 的直接关系**：α_eff → PPL 链条已建立，但 α_eff → downstream accuracy 未验证\n4. **Cross-model contamination**：三个 effectiveness conditions 在 generator≠trainee 场景下是否成立？\n5. **ρ=0.2 代表性**：方法在论文自己引用的 contamination 下限（20%）即退化，是否意味着仅适用于高污染场景？\n6. **Drayson et al. 的 epoch confound**：他们的实验是否控制了 content epochs？他们的 b=10 结果中有多少可用 epoch confound 解释？\n\n---\n\n## Missing References\n\n1. Dynamic Loss-Based Sample Reweighting for LLM Pretraining (arXiv:2502.06733, 2025) — instance-level dynamic reweighting\n2. Self-Influence Guided Data Reweighting for LM Pre-training (ICLR 2025) — self-influence based reweighting\n3. ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695, 2025) — topic-aware dynamic reweighting\n4. A Survey on LLM-Generated Text Detection (Wu et al. 2025, Computational Linguistics) — 最新 MGT detection 综述\n\n（注：以上引用由 R2 提出，R1 在 blind review 条件下无法独立核实，建议作者核实后酌情引用）\n\n---\n\n## External Review\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（耗时约 4 分钟）\n\n| 严重性 | 数量 |\n|--------|------|\n| Critical | 0 |\n| Warning | 1 |\n| Info | 6 |\n\n关键发现：\n- **[Warning] Pages 3-4 连续两页无 display item**：Page 3 有数学公式（部分缓解），但 Page 4（Experimental Setup）为纯文本 + bullet list，可能造成视觉疲劳。建议从 Appendix 提前一个表或图至 p.4。\n- **[Info] Figure 1 为文字摘要式概览框**：对 analysis 论文可行，但替换为因果关系流程图可能更有效。\n- **[Info] Figure 2 偏小**：legend 和 axis label 接近可读性下限（~7-8pt），marker 形状区分尚可。\n- **[Info] Table 1 caption 信息自包含度优秀**，Table 3 排版整洁有 actionable 价值。\n- **[Info] Appendix 图表密度高但可接受**。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings**\n**置信度：4/5**（两位 Reviewer 独立达成一致评分，交叉后核心问题高度收敛）\n\n### 评分理由\n\n**论文的核心价值在于 epoch confound 的分析发现，而非 adaptive reweighting 方法本身。**\n\nEpoch confound 分析（>95% 的 D&R 优势来自多 epoch 暴露）是对 D&R 文献有价值的方法论校正，实验设计精巧（epoch-matched controls + LR replication + permuted-score control），足以支撑 Findings 级别接收。\n\n但论文未达到主会议（4.0）门槛，原因如下：\n1. **统计基础脆弱**：N=3 seeds（2 df），BH 校正后 ρ=0.4 不显著（p=0.078），bootstrap CI 可靠性存疑\n2. **方法贡献的核心 proxy 不可靠**：α_eff R²=0.49，跨 seed r 从 0.17 到 0.75，Spearman 校正后不显著\n3. **实际影响极小**：Δ=−0.020 PPL（~0.11%），下游任务零改善，整个方法类别的 upper bound 也仅 ~0.2%\n4. **实验范围过窄**：单模型/单数据集/self-contamination，ρ=0.2 时退化，cross-model 结果 mixed\n5. **方法新颖性有限**：w=(1−q)^b 完全来自 Drayson et al.，adaptive b* 是增量式参数选择规则\n\n### 与 EMNLP 2026 评分标准的对应\n- 3.0 = Findings：有价值的分析贡献（epoch confound），但效应量、实验范围和方法新颖性不足以进入主会议\n- 不够 3.5 (Borderline Conference)：缺少更广泛的实验验证和有意义的下游改善\n- 高于 2.5 (Borderline Findings)：epoch confound 发现对社区有实际价值，实验设计严谨，报告诚实\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"yielding a practical adaptive method\" 措辞建议修改为更谦虚的表述，如 \"as a practical corollary, we derive...\"（论文部分已这么做，但 Abstract 和 Intro 的 leading sentence 仍偏强）\n- Figure 1 的 TikZ 概览框有效但可考虑改为因果流程图\n\n### §3 Method\n- 已从 Round 10 的 1.5 页压缩至 ~0.75 页，改进明显\n- Proposition 1-2 虽正确但 trivial，建议保留在 Appendix\n- α_eff 的 Pearson r≈0.70 在正文中提及，但未提及 Spearman ρ=0.40 和跨 seed 不稳定性——正文应更完整地反映 proxy 的局限\n\n### §4 Experimental Setup\n- Self-contamination 预告句已加，但讨论仍不足——建议增加一句关于 generator=trainee 对 detector AUC 的人为优势\n- Page 4 无 display item，视觉节奏偏单调\n\n### §5 Results\n- Table 1（epoch-matched）和 Table 2（main results）设计清晰，caption 信息自包含\n- §5.1 建议在开头就明确区分 \"full advantage (0.396)\" 和 \"epoch-controlled advantage (0.020)\"\n- §5.2-5.3 的 ablation/sensitivity 分析充实\n\n### §6 Discussion\n- Effect size 讨论和 downstream null 分析已有改进\n- α_eff 方差分解段落有价值，但应补充跨 seed 不稳定性的讨论\n- \"When uniform beats reweighting\" 段落对从业者有实际指导价值\n\n### §7 Conclusion\n- 与 Abstract 基调一致但偏乐观，batch-size amplification 的外推是 speculative（论文已承认）\n\n### Limitations\n- 覆盖模型规模、数据范围、seed 数量、self-contamination，合理但可以更强调 ρ=0.2 退化的 implications\n\n### References\n- 格式基本一致，部分 arXiv preprint 未标注会议版本（如已被接收）\n- 建议核实并补充 R2 提出的 4 篇遗漏引用\n\n### Appendix\n- 内容丰富（A-Q, 17 节），但 Appendix K（α_eff validation）和 Appendix N（low contamination）的结论对核心 claims 影响大，建议在正文更显著地引用",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-23T03:22:30.407146+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 10047
}
```

</details>

---


### Assistant

_source line 1040 · 2026-05-23T03:22:43.838563+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结**：

- **Overall: 3.0 (Findings)**，两位 Reviewer 独立达成一致，交叉后核心问题高度收敛
- **4 个 Must-Fix**：N=3 统计效力不足、α_eff proxy 不可靠（R²=0.49, 跨 seed r=0.17-0.75）、下游零改善+效应量极小（Δ=−0.020, ~0.11%）、实验范围过窄（单模型/self-contamination）
- **4 个 Should-Fix**：方法新颖性增量、analysis/method 定位不清、Related Work 遗漏、epoch confound 讨论深度不足
- **核心判断**：论文价值在 epoch confound 的分析发现（>95% D&R 优势来自多 epoch 暴露），足以支撑 Findings；adaptive b* 方法受限于 proxy 可靠性和效应量，不足以支撑主会议接收
- **Issue Tracker** 已更新（4 critical + 4 warning + 3 info，共 11 个 open issues）
- **视觉审查**已完成（0 critical, 1 warning, 6 info），结果已纳入报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 1041 · 2026-05-23T03:22:47.711679+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

两位 Reviewer 独立审稿后高度趋同——6/7 个问题完全一致，唯一分歧在 R1-W4（ESS/α_eff 约束交互），我认为论文通过 ESS-only baseline 隐式覆盖了该场景，给出了 [REBUT]。其余全部 [AGREE]，评分均为 Overall 3.0（Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1042 · 2026-05-23T03:23:02.890271+00:00_

审稿报告已投递给 Research Director。

**Round 11 审稿总结**：

- **Overall: 3.0 (Findings)**，置信度 4/5
- 2 名 Reviewer 独立达成一致评分，交叉后核心问题高度收敛
- 4 个 Critical issues、4 个 Warning issues、3 个 Minor issues 已写入 issue tracker
- 视觉审查已完成（0 critical, 1 warning），外部审稿未配置
- 报告已通过 `submit_review_report_to_research_director` 投递

核心判断：论文价值在于 epoch confound 的分析发现（足以支撑 Findings），但 N=3 统计效力不足、α_eff proxy 不可靠、下游零改善、实验范围过窄、方法新颖性有限，未达主会议门槛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 81

## Round 81

68 recorded events


### User

_source line 1043 · 2026-05-23T13:08:03.104127+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: provenance_weight_training
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- 补充材料: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-23T13:08:08.482009+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-23T13:08:08.532870+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-23T13:08:29.607276+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,read_local_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,WebSearch",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,read_local_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,WebSearch",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-23T13:08:29.658926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-23T13:08:34.871232+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-23T13:08:34.972038+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-23T13:08:39.330019+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-23T13:08:41.238123+00:00_

{"result":"# 项目 provenance_weight_training 概况\n\n## 实验状态 (253 个)\n\n- **adaptive_seed42**: DONE (success) — \n- **uniform_seed456**: DONE (success) — \n- **uniform_seed123**: DONE (success) — \n- **uniform_seed42**: DONE (success) — \n- **detector_modernbert**: DONE (killed) — \n- **nmin1_seed42**: DONE (success) — \n- **golden_ratio_seed42**: DONE (success) — \n- **tau_0.6_seed42**: DONE (killed) — \n- **grid_b_low_seed42**: DONE (failed) — \n- **grid_b1_5_seed456**: DONE (success) — \n- **grid_b1_0_seed456**: DONE (success) — \n- **grid_b0_5_seed456**: DONE (success) — \n- **grid_b_seed42_batch**: DONE (success) — \n- **diagnostic_contamination100**: DONE (killed) — \n- **detector_tfidf_lr**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| bs8_nmin4_uniform_seed456_r2 | — | — | — | — |\n| bs8_nmin4_adaptive_seed456_r2 | — | — | — | — |\n| bs8_nmin4_adaptive_seed456 | B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。 | — | — | — |\n\n## 待处理\n- detect_remove_q05_seed42: Detect-and-remove baseline: hard filtering removes samples with TF-IDF q_score < 0.5. If adaptive reweighting (PPL=17.674) outperforms hard removal, it demonstrates that soft scoring preserves useful signal from partially contaminated samples that hard thresholding discards.（准备中）\n- eval_adaptive_1_7b_seed123（准备中）\n- eval_uniform_1_7b_seed123（准备中）\n- detect_remove_q05_epoch_matched（准备中）\n- detect_remove_q07_seed42_r2（准备中）\n- adaptive_1_7b_planb_control（准备中）\n- eval_q01_final（准备中）\n- status_check_41312（准备中）\n- eval_adaptive_1_7b（准备中）\n- eval_uniform_1_7b_v2（准备中）\n- …另有 7 项\n\n## 近期结论\n- **bs8_nmin4_uniform_seed123_r2** (success): Cross-seed replicate (seed=123) uniform baseline at B=8. Retry from checkpoint-500 after disk-full crash. Provides second data point for
…[truncated 1804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1908
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-23T13:08:41.238583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-23T13:08:42.192948+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\graphicspath{{../../artifacts/figures/}}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{algorithm}
14	\usepackage{algorithmic}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{tikz}
20	\usetikzlibrary{positioning,arrows.meta}
21	\usepackage{hyperref}
22	
23	\newtheorem{proposition}{Proposition}
24	\newtheorem{definition}{Definition}
25	
26	\newcommand{\bstar}{b^*}
27	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
28	\newcommand{\nmin}{n_{\min}}
29	\newcommand{\btau}{b_{\tau}}
30	\newcommand{\bess}{b_{\mathrm{ESS}}}
31	\title{When Does Detect-and-Reweight Work? Epoch Confounds\\and Adaptive Reweighting in Continued LM Pretraining}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	\input{sections/abstract}
40	\end{abstract}
41	
42	\section{Introduction}
43	\label{sec:intro}
44	\input{sections/introduction}
45	
46	\section{Related Work}
47	\label{sec:related}
48	\input{sections/related_work}
49	
50	\section{Method}
51	\label{sec:method}
52	\input{sections/method}
53	
54	\section{Experimental Setup}
55	\label{sec:experiments}
56	\input{sections/experiments}
57	
58	\section{Results}
59	\label{sec:results}
60	\input{sections/results}
61	
62	\section{Discussion}
63	\label{sec:discussion}
64	\input{sections/discussion}
65	
66	\section{Conclusion}
67	\label{sec:conclusion}
68	\input{sections/conclusion}
69	
70	\section*{Limitations}
71	\label{sec:limitations}
72	\input{sections/limitations}
73	
74	\section*{Ethics Statement}
75	All experiments use publicly available datasets (FineWeb) and open-weight models; no human subjects are involved. Code and data will be released upon acceptance.
76	
77	\bibliography{references}
78	
79	\ap
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-23T13:08:42.193514+00:00_

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
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1055 · 2026-05-23T13:08:43.651175+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-23T13:08:44.604983+00:00_

-rw-r--r-- 1 ubuntu ubuntu 493866 May 23 12:01 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1057 · 2026-05-23T13:08:44.605449+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md 2>/dev/null && echo \"REBUTTAL_EXISTS\" || echo \"NO_REBUTTAL\"",
  "description": "Check if rebuttal draft exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md 2>/dev/null && echo \"REBUTTAL_EXISTS\" || echo \"NO_REBUTTAL\"",
    "description": "Check if rebuttal draft exists"
  }
}
```

</details>

---


### Tool result

_source line 1058 · 2026-05-23T13:08:44.655932+00:00_

-rw-r--r-- 1 ubuntu ubuntu 12651 May 23 11:51 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md
REBUTTAL_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-23T13:08:48.670988+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found relevant information about EMNLP 2026 and ARR submission guidelines, though the results pr
…[truncated 1197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6477
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-23T13:08:56.198595+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1061 · 2026-05-23T13:08:56.650635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity template"
  }
}
```

</details>

---


### Tool result

_source line 1062 · 2026-05-23T13:09:03.876298+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Now let me search fo
…[truncated 2508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 7677
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-23T13:09:07.540231+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's what I found regarding ACL Rolling Review 2026 submission guidelines:

## Page Limits

Short papers have a maximum of 4 content pages, and long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "WebSearch",
  "elapsed_ms": 10889
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-23T13:09:15.870987+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_provenance.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_provenance.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-23T13:09:17.326872+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_provenance.yaml\", \"content\": \"paper:\\n  title: ''\\n  version: 3\\n  generated_at: '2026-05-15T23:43:55.946378+00:00'\\nclaims:\\n- id: C001\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: α_eff(b) is strictly increasing in b (Proposition 1, part 1)\\n  type: theoretical\\n  evidence:\\n  - Derivative dα_eff/db = α_eff(1-α_eff)(E_w[ln(1-q)|real] - E_w[ln(1-q)|synth])\\n    > 0 since real samples have lower q-scores\\n  decisions:\\n  - D021\\n  - D023\\n  deprecated: true\\n- id: C003\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: ESS(b) is strictly decreasing in b (Proposition 1, part 2)\\n  type: theoretical\\n  evidence:\\n  - Increasing b concentrates weight mass on fewer low-q samples, reducing ESS\\n  decisions:\\n  - D023\\n  deprecated: true\\n- id: C006\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: 40.1% of reweighted batches are α_eff-binding (regime 2), where b* = 1.67\\n    on average\\n  type: empirical\\n  evidence:\\n  - 'adaptive_fix_seed42 batch-level analysis (Q1): 51,913 micro-batches, 49.9% clean,\\n    20.2% α_eff binding, 30.0% ESS binding'\\n  decisions:\\n  - D023\\n  deprecated: true\\n- id: C010\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: ESS-only approach selects b* = 4.15 for the same α_eff-binding batches — 2.5×\\n    more aggressive exponent\\n  type: empirical\\n  evidence:\\n  - 'adaptive_fix_seed42 batch-level analysis (Q1): counterfactual ESS-only b* computed\\n    for α_eff-binding batches'\\n  decisions:\\n  - D023\\n  - D029\\n  deprecated: true\\n- id: C015\\n  location:\\n    section: method\\n    paragraph: 0\\n    sentence: 0\\n  text: α_eff-binding batches retain ESS = 2.60, well above floor n_min = 2\\n  type: empirical\\n  evidence
…[truncated 1554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-23T13:09:17.327232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-23T13:09:17.778476+00:00_

1	As synthetic text reaches an estimated 20--60\% of web corpora, the detect-and-reweight paradigm (downweighting likely-synthetic samples via $w(x) = (1-q(x))^b$) has gained traction, but its effectiveness conditions remain poorly understood.
2	Through controlled experiments (Qwen3-0.6B continued pretraining, 132M FineWeb tokens, 3 seeds), we analyze when, why, and how detect-and-reweight works.
3	
4	We identify three findings.
5	First, an epoch-exposure confound in detect-and-remove evaluation: at matched content epochs, the advantage shrinks from 0.396 to 0.017 perplexity ($N{=}3$), revealing that ${>}$95\% of published gains (relative to adaptive reweighting) reflect data repetition rather than filtering quality.
6	Second, effective reweighting requires both sufficient discrimination and good calibration from the detector; a high-AUC but poorly calibrated detector (ECE\,=\,0.131) degrades performance below uniform, while a lightweight calibrated alternative (ECE\,=\,0.048) succeeds (3 detectors, 3 seeds).
7	Third, mechanism decomposition reveals that minimum intervention---applying the smallest exponent that meets a quality floor---outperforms unconstrained maximization, which over-sharpens and degrades training stability.
8	
9	As a practical corollary, these findings yield a dual-constrained adaptive $b^*$ that eliminates per-model grid search, achieving perplexity lower than uniform across all seeds at $\rho \geq 0.4$ with calibrated detectors ($\Delta{=}{-}0.020$ at $\rho{=}0.4$, directionally consistent across all seeds, bootstrap CI excludes zero; $\Delta{=}{-}0.032$ at $\rho{=}0.6$, uncorrected $p{=}0.010$).
10	The method transitions from harmful ($\rho{=}0.2$) to beneficial ($\rho \geq 0.4$), with a sharp boundary in $[0.3, 0.4]$; the benefit diminishes at 1.7B, and sample size ($N{=}3$) limits generalizability.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-23T13:09:17.778816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-23T13:09:18.230284+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
6	Does D\&R genuinely outperform soft reweighting, or do published comparisons confound filtering quality with multi-epoch exposure?
7	What detector properties are necessary for effective reweighting?
8	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
9	
10	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 3 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
11	To ground the analysis of exponent selection, we introduce a dual-constrained formulation: find the minimum $b$ such that $\alpha_{\mathrm{eff}}(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq n_{\min}$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
12	
13	Our analysis yields three findings:
14	\begin{itemize}[nosep,leftmargin=*]
15	\item \textbf{Epoch confound in D\&R evaluation.}
16	The bulk of D\&R's PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure, not filtering quality; epoch-matched controls ($N{=}3$) reduce the gap from 0.396 to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
17	
18	\item \textbf{De
…[truncated 2538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-23T13:09:18.280826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-23T13:09:19.284038+00:00_

1	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus with token-level contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$, assumed unknown~\citep{cheng2025contamination}.
2	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
3	Rather than selecting $b$ via grid search~\citep{drayson2025detection}, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
4	
5	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
6	
7	\paragraph{Quality floor.}
8	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ indicate likely-real samples. The \emph{effective real proportion} $\aeff(b) = \sum_i w_i(b) r_i / \sum_i w_i(b)$ measures weight allocated to real samples.
9	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
10	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.70$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
11	
12	\paragraph{Stability ceiling.}
13	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
14	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
15	
16	\paragraph{Adaptive $\bstar$.}
17	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
18	The optimal exponent implements \emph{minimum intervention}:
19	\begin{equation}
20	  b^{*} = \begin{cases}
21	    0        & \text{if } \aeff(0) \geq \tau, \\
22	    b_\tau   & \text{if } b_\
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-23T13:09:19.284428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-23T13:09:19.786374+00:00_

1	\subsection{Main Results}
2	\label{sec:main-results}
3	
4	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across three seeds.
5	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
6	
7	Adaptive $\bstar$ achieves 3-seed mean PPL 17.674, compared to 17.694 for uniform ($\Delta{=}{-}0.020$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean; gap $+$0.054).
8	A paired $t$-test yields $t{=}{-}7.1$, $p{=}0.019$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.078$, which does not reach conventional significance, though the 95\% BCa bootstrap CI $[{-}0.028, {-}0.012]$ excludes zero.
9	The practical value is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
10	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $4.7{\times}$ higher cross-seed variance than adaptive ($\sigma{=}0.033$ vs.\ $0.007$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
11	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
12	
13	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
14	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that detector $q$-scores carry genuine provenance signal; uninformed reweighting only increases gradient variance.
15	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
16	Only the dual-constr
…[truncated 10199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-23T13:09:19.987905+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-23T13:09:20.039072+00:00_

issues:
# === Round 10 issues (all resolved, retained for history) ===
- id: "R10-C1"
  summary: "Seed 42 checkpoint resume artifact 使主表核心比较可信度存疑"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Appendix P 揭示 seed 42 resume artifact。R2 推算替换后 Δ 缩小到 ~0.002。要求 from-scratch 重跑。"
  resolution: "tau07_seed42 确认是 2026-05-19 独立 from-scratch 训练，n_min=2（脚本默认值）。Resume artifact 仅影响早期 tau=0.8 实验。Paper 已澄清。"
  resolution_round: 10

- id: "R10-C2"
  summary: "多重比较未校正，p=0.025 Bonferroni 校正后不显著"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "6 种方法 ≥5 检验，p 值未校正。BH 校正后 ρ=0.4 p=0.078 不显著。"
  resolution: "BH 校正完成，corrected p 写入论文。ρ=0.4 用 'directionally consistent' + bootstrap CI；ρ=0.6 保留 'significant'。t/p 值统一为 3dp 精度。"
  resolution_round: 10

- id: "R10-C3"
  summary: "方法新颖性不足，§3 仍占 ~1.5 页与 analysis 定位不匹配"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "w=(1-q)^b 完全沿用 Drayson et al.。§3 ~1.5 页偏重方法。应明确 analysis paper 定位。"
  resolution: "§3 从 1.5→0.75 页。Contributions 重排：(1-3) 分析发现突出，(4) adaptive b* 标为 practical corollary。"
  resolution_round: 10

- id: "R10-C4"
  summary: "Downstream task 零改善削弱实际意义"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Table 3 所有 downstream |Δ| ≤ 0.01。§6 解释 ~4 行过短。需 7B+ 或更细粒度评估。"
  resolution: "Downstream null 分析扩展到 ~6 行，加入量级论证（0.1% PPL → measurement noise 以下）+ Tay et al. citation。7B+ 不可行，acknowledged in Limitations。"
  resolution_round: 10

- id: "R10-M1"
  summary: "实验规模和场景过于狭窄，ρ=0.3 缺失"
  category: experiment
  severity: warning
  status: resolved
  first_raised_
…[truncated 11605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-23T13:09:27.663723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-23T13:09:27.664191+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder and show that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy; \citet{dohmatob2024tale} characterize this as a change of scaling laws.
5	\citet{gerstgrasser2024collapse} show that accumulating real data alongside synthetic data can break the recursion, though at substantial collection cost.
6	\citet{kang2025demystifying} systematically study scaling laws for synthetic data in pretraining, finding that rephrased synthetic data mixed with natural text improves data efficiency but textbook-style data degrades loss on many domains.
7	\citet{cheng2025contamination} survey the broader contamination landscape and confirm that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	As language models are deployed at scale for content generation~\citep{radford2019language,brown2020language,openai2023gpt4,dubey2024llama}, these results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature; Fast-DetectGPT~\citep{bao2024fastdetectgpt} accelerates this with conditional probability curvature; Binoculars~\citep{hans2024binoculars} uses cross-perplexity ratios between two models; M
…[truncated 6772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-23T13:09:28.115642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-23T13:09:28.116184+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution; implications for detection difficulty are discussed in \S\ref{sec:limitations}.
5	Our self-contamination design provides a controlled testbed with known ground-truth labels but limits ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss this limitation in \S\ref{sec:limitations}.
6	
7	\paragraph{Detector.}
8	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.05 after temperature scaling with $T{=}0.204$).
9	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
10	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
11	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness}.
12	
13	\paragraph{Training.}
14	We continue pretraining Qwen3-0.6B from its pretrained 
…[truncated 1914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-23T13:09:28.367128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-23T13:09:28.367574+00:00_

1	\paragraph{The epoch confound in D\&R evaluation.}
2	The bulk of D\&R's reported PPL advantage over adaptive reweighting (${>}$95\%) is attributable to multi-epoch exposure rather than filtering quality (\S\ref{sec:main-results}).
3	An independent-LR replication (D\&R $17.651$ vs.\ shared-schedule $17.657$, $\Delta{=}0.006$) confirms that this finding is robust to LR schedule choice.
4	D\&R evaluations that do not control for content epochs systematically overstate filtering effectiveness; the residual benefit ($\Delta{=}0.017$ vs.\ adaptive $\bstar$, directionally consistent across 3 seeds) falls within cross-seed variance.
5	A permuted-score control (shuffled detector scores; 3-seed mean $17.951{\pm}0.007$, $+$0.26 vs.\ uniform) confirms that detector signal is load-bearing: uninformed reweighting only degrades.
6	
7	\paragraph{When uniform beats reweighting.}
8	Beyond the evaluation confound, our results identify three operational conditions for effective reweighting, each of which, when violated, makes uniform training preferable.
9	First, \emph{detector quality}: the detector must provide both sufficient discrimination (AUC) and good calibration (ECE).
10	A high-AUC but poorly calibrated detector (GPT-2, ECE\,=\,0.131) degrades PPL by $+$0.098 below uniform; even a well-calibrated detector with insufficient discrimination (N-gram, AUC\,=\,0.73) degrades by $+$0.129 (\S\ref{sec:robustness}).
11	Second, \emph{contamination level}: at $\rho{=}0.2$, the detector's signal-to-noise ratio is too low and the method actively intervenes on unreliable signal ($\aeff$-binding at 60.1\% despite mean $q{=}0.393$), degrading PPL by $+$0.046; the method transitions from harmful to beneficial with a sharp sign change in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}).
12	Third, \emph{scale}: at 1.7B the benefit diminishes ($\Delta{=}{-}0.013$) with OOD partially inconsistent, suggesting that larger models may be inherently more robust to contamination g
…[truncated 6636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-23T13:09:28.819166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-23T13:09:28.970050+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (1) D\&R evaluations confound filtering with multi-epoch exposure (${>}$95\% of the advantage over adaptive reweighting); (2) detectors require both discrimination and calibration; (3) minimum intervention outperforms unconstrained maximization.
2	A dual-constrained adaptive $\bstar$ ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$) improves over uniform at $\rho \geq 0.4$ (directionally consistent across all seeds; $\rho{=}0.6$: uncorrected $p{=}0.010$, $p_{\mathrm{BH}}{=}0.064$ with $k{=}9$) without tuning; validated on Qwen3 ${\leq}$1.7B, where the benefit diminishes.
3	Batch-size amplification is monotonic across $B \in \{4, 8, 16\}$ ($1.0{\times}$ to $3.4{\times}$; $p{<}0.01$ at $B{=}16$) with diminishing marginal gains, suggesting favorable scaling with larger micro-batches typical of production training; the key bottleneck is extending detector calibration to cross-model contamination scenarios.
4	
5	The epoch confound finding has implications beyond our experiments: any D\&R evaluation that compares at equal training steps without controlling for content epochs risks overstating filtering effectiveness, and published results in this area should be interpreted with this confound in mind.
6	For practitioners, the decision framework (Table~\ref{tab:decision}) distills our analysis into actionable guidance: provenance-aware reweighting is worthwhile only when contamination is substantial ($\rho \geq 0.4$) and the detector is well-calibrated (ECE $\leq 0.05$); otherwise, uniform training remains the safer default.
7	Key directions for future work include cross-model contamination scenarios (where the generator differs from the trainee), better proxies for batch quality that exploit soft $q$-scores rather than binary indicators, and larger-scale verification to test whether the batch-size amplification trend continues at production training scales.
8	Code and data will be released upon acceptance.
9
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-23T13:09:29.020705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-23T13:09:29.372187+00:00_

1	All experiments use Qwen3 (0.6B and 1.7B) on 132--200M tokens of continued pretraining with self-generated contamination at $\rho \in \{0.2, 0.3, 0.4, 0.6\}$; generalization to other model families, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination is untested.
2	The method improves over uniform only at $\rho \geq 0.4$ with a calibrated detector; at $\rho{=}0.2$ it degrades, and a preliminary Llama-3.2-3B cross-model test showed mixed results (Appendix~\ref{app:cross_model}), suggesting the effective range is narrower than the paradigm's ambition.
3	Three detectors from two families (discriminative and generative) were tested; fine-tuned neural classifiers (e.g., RoBERTa-based) and zero-shot methods (e.g., DetectGPT) remain untested, so the calibration finding may not generalize across detector architectures.
4	Paired comparisons use $N{=}3$ seeds (2 degrees of freedom), limiting statistical power; results are directionally consistent but the sample size precludes strong generalizability claims.
5	After family-wise correction for nine comparisons, the $\rho{=}0.4$ adaptive-vs-uniform difference does not reach conventional significance ($p_{\mathrm{BH}}{=}0.078$), though the effect is directionally consistent across all seeds and the bootstrap CI excludes zero; the $\rho{=}0.6$ comparison also falls short of conventional significance under full-family correction ($p_{\mathrm{BH}}{=}0.064$, $k{=}9$), though the uncorrected $p{=}0.010$ and dose-response pattern across $\rho$ levels support a real effect.
6	The self-contamination setup provides known ground-truth labels but represents an easier detection scenario than cross-model contamination, where generator--corpus distribution mismatch may reduce detector accuracy.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-23T13:09:29.372517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-23T13:09:29.674273+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least one sample with $q_i \in (0,1)$ and $r_i$ is not constant.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, r_i,
14	\end{equation*}
15	where $r_i \in \{0, 1\}$ indicates whether sample $i$ is real.
16	Taking the derivative with respect to $b$:
17	\begin{align*}
18	  \frac{d\pi_i}{db}
19	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
20	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
21	\end{align*}
22	Substituting,
23	\begin{align*}
24	  \frac{d\alpha_{\mathrm{eff}}}{db}
25	  &= \sum_i r_i\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
26	  &= \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr).
27	\end{align*}
28	Since $r_i = \mathbf{1}[q_i \leq 0.5]$, the indicator $r_i$ and $\ln(1{-}q_i)$ are positively associated by construction, so the covariance is non-negative.
29	\end{proof}
30	
31	\begin{proposition}[ESS monotonicity]
32	\label{prop:ess_mono}
33	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
34	\end{proposition}
35	
36	\begin{proof}
37	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
38	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
39	Differentiating $H$ with respect to $b$:
40	\begin{equation*}
41	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
42	\end{equation*}
43	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; th
…[truncated 27174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-23T13:09:35.208145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": "494"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
    "offset": "494"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-23T13:09:35.860655+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (494). The file has 494 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-23T13:09:35.911230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-23T13:09:35.962085+00:00_

1	# Author Response (Round 11)
2	
3	We thank the reviewers for their thorough feedback. Below we address all concerns organized by the R11 issue list. All referenced revisions are in the updated manuscript.
4	
5	---
6	
7	## Broader Significance
8	
9	This work contributes beyond our specific experimental setting in four ways. First, the epoch confound finding applies retroactively to all D&R evaluations that compare at equal training steps rather than equal content epochs: the headline 0.396 PPL advantage shrinks by >95% to a residual Δ=0.017 when content epochs are equalized (Table 1), establishing a methodological baseline that future D&R studies must control for. Second, the detector requirements analysis yields a counter-intuitive result: a high-AUC detector (GPT-2, AUC=0.91) with poor calibration (ECE=0.131) performs *worse* than uniform training (Δ=+0.098), while a lower-AUC but well-calibrated detector (TF-IDF, AUC=0.94, ECE=0.048) succeeds—demonstrating that calibration can reverse the sign of the intervention. Third, the α_eff/ESS constraint decomposition provides a generalizable analytical toolkit for importance-weighted training: any method that applies per-sample weights faces the same quality-stability tradeoff, and our binding-rate analysis offers a diagnostic for when constraints dominate. Fourth, the observed Δ=−0.020 at ρ=0.4, B=4 represents a lower bound, not a ceiling: batch-size amplification shows monotonic scaling (B=4: Δ=−0.020, B=8: Δ=−0.050, B=16: Δ=−0.068; §5.4), and production batch sizes typically range from 64 to 256. At ρ=0.6 the effect doubles to Δ=−0.032 (uncorrected p=0.010; BH-corrected p=0.064 with k=9). At production batch sizes (e.g., B=128), conservative extrapolation with the empirical scaling exponent α ≈ 0.89 (Δ ∝ B^α) predicts Δ ≈ −0.39, a practically meaningful improvement—though this extrapolation is speculative and requires empirical validation at larger scale. As web-scale contamination grows, the practical relevance of p
…[truncated 10729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-23T13:09:54.242689+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "decisions.yaml",
  "max_chars": "2000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "decisions.yaml",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-23T13:09:54.293554+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml\", \"content\": \"_next_id: 124\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 投稿目标定为 AAAI 2027 (~Aug 2026)，放弃 EMNLP 2026 ARR May 25\\n  rationale: EMNLP ARR 仅剩 12 天且无任何基础设施，即使 AI 团队速度也无法完成多轮预训练实验。AAAI 2027 有 ~11 周，足够完成\\n    4 phase 全流程。两者均为 A 类会议。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:38 UTC\\n  summary: 'MVP 设计: 单模型(Qwen3-0.6B) + 单污染比例(40%) + 三组对比(uniform/grid-b/adaptive-b*)'\\n  rationale: 核心假设是 adaptive b* 能替代 grid search。最小验证只需一个污染比例下的 A/B/C 对比。40% 选取因为理论和\\n    Strong Model Collapse 均表明该区间效应显著。通过后再扩展到多污染比例/多生成器/多模型。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-13 17:40 UTC\\n  summary: '修正 D001: 主攻 EMNLP 2026 ARR May 25，AAAI 2027 为后备'\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、资源会给够。AI 团队 24/7 执行 + 4 卡并行：数据生成 ~2 天、MVP\\n    ~1 天、全矩阵 ~3 天、论文 ~3 天、迭代 ~2 天 = 11 天可完成。12 天 deadline 可行。保守估计完成时间是最大风险。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-13 17:42 UTC\\n  summary: '采纳 Reviewer 4 点 MVP 协议补全: 3 seeds、detector gate、grid-b 定义、kill criteria'\\n  rationale: 'Reviewer 指出 MVP 设计 4 个缺口均合理: (1) 单 seed 无统计保障 → 3 seeds，缩 tokens 到 200M\\n    控预算; (2) 检测器质量是 pipeline 前提 → 加 gate AUC≥0.95/ECE≤0.05; (3) grid search baseline\\n    需可复现 → 定义 b∈{0.5,1,1.5,2,3,5}; (4) 无 fail 路径 → 定义三级 kill/pivot。不增加工程量，只补协议。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-13 22:08 UTC\\n  summary: 识别 q-score 极化风险：AUC=0.999998 可能导致 adaptive b* vs grid-b 对比退化，制定分级应对方案\\n  rationale: 'Reviewer 审查发现 detector eval_auc=0.999998（step 2000），q-score 可能高度双峰化。若校准后\\n    >95% 样本 q<0.05 或 q>0.95，则 w=(1-q)^b 对所有 b>0 约等于 0，不同 b 值间无区分度。MVP 技术上可能 PASS（adaptive\\n    ≈ grid-b，满足 ≥90% 条件），但无法证明核心贡献（自适应精细调优的价值）。\\n\\n\\n    应对方案（detector 完成后按 q-score 分布分级执行）：\\n\\n    - 分布有spread（q 在 0.
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-23T13:09:54.544870+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "provenance_weight_training"
  }
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-23T13:09:54.746034+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-23T13:10:03.530036+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-23T13:10:03.580692+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-23T13:10:06.140887+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/provenance_weight_training/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/provenance_weight_training/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10"
  }
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-23T13:10:06.191532+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-23T13:10:10.935065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training -maxdepth 3 -name \"*.yaml\" -not -path \"*/\\.venv/*\" -not -path \"*/__pycache__/*\" 2>/dev/null | head -20",
  "description": "Find project YAML config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training -maxdepth 3 -name \"*.yaml\" -not -path \"*/\\.venv/*\" -not -path \"*/__pycache__/*\" 2>/dev/null | head -20",
    "description": "Find project YAML config files"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-23T13:10:11.487564+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-23T13:10:16.155255+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/*.yaml 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/ 2>/dev/null",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/*.yaml 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/agent/ 2>/dev/null",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-23T13:10:16.205921+00:00_

Exit code 2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-23T13:10:44.017636+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "provenance_weight_training",
  "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "provenance_weight_training",
    "review_chat_id": "oc_069d56747de0423c793156b069500cb3"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-23T13:11:07.216477+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23198
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-23T13:11:07.317438+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## Round 1 审稿任务 — Reviewer 1: 方法严谨性 + 实验设计\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long Paper, 8 页正文, 无限参考文献, Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 style\n- **匿名规则**: Double-blind (论文中不得出现作者信息, 避免 self-revealing references)\n- **评分标准**: ARR Overall Assessment 1-5 分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit)\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf`\n- 补充材料: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md`\n\n### 你的审查侧重\n\n**核心关注: 方法严谨性 + 实验设计**\n\n请从以下维度严格审查:\n\n1. **统计推断可靠性**\n   - N=3 seeds 的统计检验力是否足够？paired t-test (2 df) 的可靠性？\n   - Bonferroni-Holm 校正后 p 值 (p_BH=0.078 at ρ=0.4, p_BH=0.064 at ρ=0.6) 的解读是否恰当？\n   - Bootstrap CI 在 N=3 时的覆盖率保证？\n   - 是否存在 p-hacking 或 selective reporting 的迹象？\n\n2. **实验控制质量**\n   - Epoch confound 实验设计的严谨性：epoch-matched comparison 是否充分控制了混淆因素？LR schedule 控制是否完备？\n   - Self-contamination 设计的生态效度：generator=trainee 是否人为降低了问题难度？\n   - Checkpoint resume artifact (Appendix P) 是否已充分排除？\n\n3. **α_eff proxy 可靠性**\n   - Pearson r=0.70 (R²≈0.49) 是否足以支撑方法的核心机制？\n   - 跨 seed 稳定性的证据是否充分？\n   - 方差分解 (70% detector noise / 30% ESS compression) 的可信度？\n\n4. **效应量与 claim 匹配**\n   - Δ=-0.020 PPL (~0.11% relative) 是否具有实际意义？\n   - Downstream task 零改善与 PPL 改善的不一致性？\n   - 论文的 claim 范围是否超过了实验证据所能支撑的范围？\n\n5. **实验范围**\n   - 单模型 (Qwen3-0.6B/1.7B) + 单数据集 (FineWeb 132M) 是否足够？\n   - ρ={0.2, 0.3, 0.4, 0.6} 的覆盖是否完整？\n   - 1.7B scale-up 和 cross-model transfer 的证据强度？\n\n请按 ARR 标准格式输出审稿报告: Summary → Strengths → Weaknesses (分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## Round 1 审稿任务 — Reviewer 1: 方法严谨性 + 实验设计\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long Paper, 8 页正文, 无限参考文献, Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 style\n- **匿名规则**: Double-blind (论文中不得出现作者信息, 避免 self-revealing references)\n- **评分标准**: ARR Overall Assessment 1-5 分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit)\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf`\n- 补充材料: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md`\n\n### 你的审查侧重\n\n**核心关注: 方法严谨性 + 实验设计**\n\n请从以下维度严格审查:\n\n1. **统计推断可靠性**\n   - N=3 seeds 的统计检验力是否足够？paired t-test (2 df) 的可靠性？\n   - Bonferroni-Holm 校正后 p 值 (p_BH=0.078 at ρ=0.4, p_BH=0.064 at ρ=0.6) 的解读是否恰当？\n   - Bootstrap CI 在 N=3 时的覆盖率保证？\n   - 是否存在 p-hacking 或 selective reporting 的迹象？\n\n2. **实验控制质量**\n   - Epoch confound 实验设计的严谨性：epoch-matched comparison 是否充分控制了混淆因素？LR schedule 控制是否完备？\n   - Self-contamination 设计的生态效度：generator=trainee 是否人为降低了问题难度？\n   - Checkpoint resume artifact (Appendix P) 是否已充分排除？\n\n3. **α_eff proxy 可靠性**\n   - Pearson r=0.70 (R²≈0.49) 是否足以支撑方法的核心机制？\n   - 跨 seed 稳定性的证据是否充分？\n   - 方差分解 (70% detector noise / 30% ESS compression) 的可信度？\n\n4. **效应量与 claim 匹配**\n   - Δ=-0.020 PPL (~0.11% relative) 是否具有实际意义？\n   - Downstream task 零改善与 PPL 改善的不一致性？\n   - 论文的 claim 范围是否超过了实验证据所能支撑的范围？\n\n5. **实验范围**\n   - 单模型 (Qwen3-0.6B/1.7B) + 单数据集 (FineWeb 132M) 是否足够？\n   - ρ={0.2, 0.3, 0.4, 0.6} 的覆盖是否完整？\n   - 1.7B scale-up 和 cross-model transfer 的证据强度？\n\n请按 ARR 标准格式输出审稿报告: Summary → Strengths → Weaknesses (分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-23T13:11:27.792637+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20475
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-23T13:11:27.893455+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "provenance_weight_training",
  "text": "## Round 1 审稿任务 — Reviewer 2: 新颖性 + 完整性 + 写作质量\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long Paper, 8 页正文, 无限参考文献, Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 style\n- **匿名规则**: Double-blind (论文中不得出现作者信息, 避免 self-revealing references)\n- **评分标准**: ARR Overall Assessment 1-5 分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit)\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf`\n- 补充材料: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md`\n\n### 你的审查侧重\n\n**核心关注: 新颖性 + 完整性 + 写作质量**\n\n请从以下维度严格审查:\n\n1. **贡献新颖性与定位**\n   - 三个 findings (epoch confound, detector requirements, minimum intervention) 的新颖程度？\n   - Epoch confound 是否是一个显而易见的观察 (减少数据→更多 epoch 是自然推论)，还是有实质性贡献？\n   - w=(1-q)^b 完全沿用 Drayson et al.，adaptive b* 本质上是参数选择启发式——方法新颖性是否足够？\n   - 论文定位为 \"analysis paper with adaptive b* as practical corollary\" 是否清晰一致？Abstract 和正文是否匹配？\n\n2. **Related Work 覆盖度**\n   - Instance-level reweighting 领域是否有遗漏的重要工作？\n   - 与 curriculum learning / importance sampling / data selection 文献的区别是否讲清楚？\n   - 引用格式是否符合 ACL 规范 (natbib)？引用是否真实可查？\n\n3. **论文结构与叙事**\n   - §1-§7 的逻辑流是否顺畅？每个 section 的篇幅是否合理？\n   - §3 (Method) 压缩到 ~0.75 页后是否清晰？关键定义是否完整？\n   - Discussion (§6) 是否充分讨论了效应量、proxy 局限性、下游任务零改善？\n   - Limitations 是否覆盖了关键局限？是否过短或过长？\n\n4. **写作质量**\n   - 术语使用是否一致 (α_eff, b*, ESS, ρ 等)？\n   - 脚注密度是否过高？关键技术信息是否被藏在脚注中？\n   - Table / Figure 的标注是否清晰？小数位是否一致？\n   - 是否存在 overclaim (如 \"significant\" 误用、\"practical\" 过度使用)？\n   - Abstract 是否在 200 words 以内？\n\n5. **格式合规**\n   - 正文是否在 8 页以内？\n   - 是否有 Responsible NLP Checklist 出现在 PDF 中？(EMNLP 2026 规定 checklist 在 OpenReview 表单)\n   - 匿名性是否完好？是否有自引泄露作者身份？\n   - Appendix 结构是否合理？引用格式？\n\n请按 ARR 标准格式输出审稿报告: Summary → Strengths → Weaknesses (分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "provenance_weight_training",
    "text": "## Round 1 审稿任务 — Reviewer 2: 新颖性 + 完整性 + 写作质量\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long Paper, 8 页正文, 无限参考文献, Limitations/Ethics 不计入页数\n- **模板**: ACL 2026 style\n- **匿名规则**: Double-blind (论文中不得出现作者信息, 避免 self-revealing references)\n- **评分标准**: ARR Overall Assessment 1-5 分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit)\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/review_round_11/submitted.pdf`\n- 补充材料: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/rebuttal_draft.md`\n\n### 你的审查侧重\n\n**核心关注: 新颖性 + 完整性 + 写作质量**\n\n请从以下维度严格审查:\n\n1. **贡献新颖性与定位**\n   - 三个 findings (epoch confound, detector requirements, minimum intervention) 的新颖程度？\n   - Epoch confound 是否是一个显而易见的观察 (减少数据→更多 epoch 是自然推论)，还是有实质性贡献？\n   - w=(1-q)^b 完全沿用 Drayson et al.，adaptive b* 本质上是参数选择启发式——方法新颖性是否足够？\n   - 论文定位为 \"analysis paper with adaptive b* as practical corollary\" 是否清晰一致？Abstract 和正文是否匹配？\n\n2. **Related Work 覆盖度**\n   - Instance-level reweighting 领域是否有遗漏的重要工作？\n   - 与 curriculum learning / importance sampling / data selection 文献的区别是否讲清楚？\n   - 引用格式是否符合 ACL 规范 (natbib)？引用是否真实可查？\n\n3. **论文结构与叙事**\n   - §1-§7 的逻辑流是否顺畅？每个 section 的篇幅是否合理？\n   - §3 (Method) 压缩到 ~0.75 页后是否清晰？关键定义是否完整？\n   - Discussion (§6) 是否充分讨论了效应量、proxy 局限性、下游任务零改善？\n   - Limitations 是否覆盖了关键局限？是否过短或过长？\n\n4. **写作质量**\n   - 术语使用是否一致 (α_eff, b*, ESS, ρ 等)？\n   - 脚注密度是否过高？关键技术信息是否被藏在脚注中？\n   - Table / Figure 的标注是否清晰？小数位是否一致？\n   - 是否存在 overclaim (如 \"significant\" 误用、\"practical\" 过度使用)？\n   - Abstract 是否在 200 words 以内？\n\n5. **格式合规**\n   - 正文是否在 8 页以内？\n   - 是否有 Responsible NLP Checklist 出现在 PDF 中？(EMNLP 2026 规定 checklist 在 OpenReview 表单)\n   - 匿名性是否完好？是否有自引泄露作者身份？\n   - Appendix 结构是否合理？引用格式？\n\n请按 ARR 标准格式输出审稿报告: Summary → Strengths → Weaknesses (分 Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-23T13:11:29.504523+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_069d56747de0423c793156b069500cb3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 1110 · 2026-05-23T13:11:43.252564+00:00_

Round 1 已启动：

- **视觉审查 Agent**: 已派发，fire-and-forget
- **Reviewer 1** (方法严谨性 + 实验设计): 已分配，审稿中
- **Reviewer 2** (新颖性 + 完整性 + 写作): 已分配，审稿中

等待两位 Reviewer 提交初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 82

## Round 82

2 recorded events


### User

_source line 1111 · 2026-05-23T13:16:20.166503+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**Venue**: EMNLP 2026 (ARR May cycle)

---

## Summary

本文研究 detect-and-reweight (D&R) 范式在续训语言模型中应对合成文本污染的有效性条件。在 Qwen3-0.6B 上使用 132M FineWeb 子集进行可控实验，提出三项分析发现：(1) D&R 先前报告的 PPL 优势中 >95% 可归因于 epoch confound（多轮数据暴露），epoch-matched 后优势从 0.396 缩减至 0.017；(2) 有效的 reweighting 要求检测器同时具备足够的 AUC（≥0.9）和良好的校准（ECE≤0.05），高 AUC 但低校准的检测器反而劣于均匀训练；(3) 基于双约束（α_eff ≥ τ, ESS ≥ n_min）的自适应 b* 实现最小干预，性能接近 grid search 最优。方法在 ρ=0.4 时获得 Δ=−0.020 PPL（~0.11% relative），下游任务无显著改善。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | Epoch confound 发现方法论可靠，但 adaptive method 的统计证据不足（N=3, 校正后均未达 α=0.05），α_eff proxy R²≈0.49 |
| **Excitement** | 2/5 (Potentially Interesting) | Epoch confound 对社区有方法论警示价值，但效应量极小（0.11% PPL），下游零改善，实际影响有限 |
| **Reproducibility** | 4/5 | 实验设置详细（§4），超参数透明，代码承诺开源，17 个 appendix 覆盖完整 |
| **Confidence** | 4/5 | 对统计方法论和实验设计领域较为熟悉，仔细检查了主要论点 |

---

## 总体评分

**Overall**: 3.0 — Findings

**一句话总结**: Epoch confound 的发现有真实的方法论价值，足以支撑 Findings 级别的贡献，但自适应方法的统计证据不足（N=3 无校正显著性、下游零改善、效应量极小）使其无法达到主会议标准。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 的统计推断力根本性不足
- 具体位置：§5.1, Table 2, 以及论文中所有 p 值和 CI 报告
- 问题：全文核心量化结论依赖于 N=3 seeds 的 paired t-test（仅 2 个自由度）。主要结果：
  - ρ=0.4: uncorrected p=0.019, BH-corrected p=0.078（未达 α=0.05）
  - ρ=0.6: uncorrected p=0.010, BH-corrected p=0.064（未达 α=0.05）
  
  论文报告了 bootstrap CI [−0.028, −0.012]（§5.1），但 N=3 的 bootstrap 仅有 3³=27 个可能的重抽样本，CI 的覆盖率保证极其脆弱。论文声称 Cohen's d=2.86, power>0.90，但如此高的 d 值更可能反映的是方差被人为压低（seeds 只影响参数初始化，data order 固定），而非效应量大。实际上这恰恰说明 3 个 seeds 探索的随机性维度极其有限。

  更关键的是：论文先选择了 BH 校正（k=9），然后在校正结果不理想时论证家族 "structurally heterogeneous"，校正过于保守。这构成了一种 post-hoc 的统计叙事调整——你不能在分析前选择校正方法，分析后否定它。
- 为什么影响接收：这是一篇以定量分析为核心的论文，如果核心量化结论在标准统计检验下均不显著，整个 adaptive method 的贡献就缺乏可靠支撑。
- 建议修改方向：(a) 增加到至少 N=5 seeds（4 df，可检测 d=2.0 的效应）；或 (b) 如果计算资源不允许，全面放弃 p 值叙事，改为纯效应量+方向一致性报告，明确承认统计检验力不足；(c) 对 BH 校正取一个立场并坚持——要么不用（给出理由），要么用了就接受结果。

**N2** [critical] 效应量与 claim 之间的严重脱节
- 具体位置：§5.1 (Δ=−0.020 PPL), Table 4 (downstream null), §7 Conclusion
- 问题：adaptive 方法的核心效应量为 Δ=−0.020 PPL，相对改善仅 0.11%。五项下游任务（Table 4, MMLU/HellaSwag/ARC/WinoGrande/PIQA）全部 |Δ|≤0.01，在标准误内无法区分。论文将这归因于 "PPL-to-downstream transfer is nonlinear and scale-dependent"（引用 Tay et al., 2023），但这恰恰意味着在可验证的当前 scale 下，该方法没有实际用途。

  §5.4 的 batch-size amplification 外推更成问题：仅用 B={4,8,16} 三个点拟合幂律 Δ∝B^α（α≈0.89），然后外推到 B=128 预测 Δ≈−0.39。用 3 个数据点拟合幂律并外推 8 倍，任何统计学教材都会认为这不可靠。论文虽标注 "speculative"，但 rebuttal 中将其作为实际意义的主要论据（"a practically meaningful improvement"）。
- 为什么影响接收：如果方法在可测量的所有指标上都没有实际改善，contribution 主要在分析框架本身——这需要论文的 framing 与之匹配，避免方法论贡献的过度包装。
- 建议修改方向：(a) 在 abstract 和 conclusion 中删除所有关于 "practical" 的表述——当前 scale 下该方法不 practical；(b) 将 batch-size 外推从主文移到 appendix，标注为 hypothesis 而非 evidence；(c) 更诚实地承认：在可验证范围内，adaptive reweighting 的实际增益可忽略不计。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Self-contamination 实验设计的生态效度严重不足
- 具体位置：§4 "Training Data", §7 Limitations
- 问题：generator=trainee 的设计意味着合成数据来自被训练模型自身（Qwen3-0.6B 生成 → Qwen3-0.6B 检测+训练）。这人为降低了检测难度：模型生成的文本带有自身的统计指纹，TF-IDF+LR 检测器能达到 AUC=0.94 部分归因于此。真实世界中，污染来源是异构的（GPT-4、Claude、Gemini 等多种模型，且不同版本），检测难度远高于 self-contamination。

  论文在 Limitations（§9, p.9）中承认了这一限制（"limits ecological validity"），但论文的第二项核心 claim——detector requirements（AUC≥0.9, ECE≤0.05）——直接依赖于检测器性能数据。在 self-contamination 下得出的检测器阈值，在 cross-model contamination 下可能完全不适用。Appendix O 的 cross-model transfer（Llama-3.2-3B）是 single seed 且结果 mixed（MMLU +1.57pp, HellaSwag −0.60pp），不足以验证。
- 建议：(a) 至少增加一个 cross-generator 实验（用 GPT-2-large 或其他开放模型生成污染数据），在主文中报告；(b) 将 detector requirements 的 claim 明确限定为 self-contamination 场景。

**W2** [warning] α_eff proxy 的解释力不足以支撑其在方法中的核心地位
- 具体位置：§3 Method (α_eff 定义), §6 Discussion, Table 11, Appendix K
- 问题：α_eff 是 adaptive b* 方法的核心机制——它是双约束中 quality floor 的直接操作变量。但 Table 11 显示 α_eff 与 ground-truth batch-level real fraction 的 Pearson r=0.70（R²≈0.49），即 proxy 仅解释了不到一半的方差。论文的方差分解（~70% detector noise, ~30% ESS compression）基于单一 seed 的定性归因，没有正式的方差分解统计。

  Rebuttal 中报告 r(α_eff, mean_q)=0.80，但这是 proxy-to-detector-score 的相关性（循环论证），而非 proxy-to-ground-truth。cross-seed spread <0.003 看似稳定，但 α_eff 是 q-scores 的确定性函数且 detector 固定，所以跨 seed 稳定是预期结果，不构成额外证据。

  根本问题：当方法的核心信号只解释 49% 的目标方差时，为什么 minimum intervention（保守使用这个噪声信号）优于 uniform？一个更简洁的解释是：adaptive b* 的实际贡献主要来自 ESS constraint 的稳定化作用，而非 α_eff 的质量信号。
- 建议：(a) 增加 ablation：固定 α_eff=constant，只保留 ESS constraint，测试 PPL 差异；(b) 如果这个 ablation 表明 ESS 是主要贡献者，需要重写 §6 的 narrative。

**W3** [warning] 实验范围过窄，不支撑 "necessary conditions" 的普适性 claim
- 具体位置：§7 Conclusion ("three effectiveness conditions"), §5.2-5.4, Limitations
- 问题：论文声称识别了三个 "effectiveness conditions"（AUC≥0.9, ECE≤0.05, ρ≥0.4），但支撑这些条件的实验仅覆盖：
  - 1 个模型家族（Qwen3, 0.6B/1.7B）
  - 1 个数据集（FineWeb 132M）
  - 1 种污染类型（self-contamination）
  - 4 个 ρ 值（0.2/0.3/0.4/0.6）
  - 3 个 seeds（主实验）/ 1 个 seed（1.7B, cross-model）

  "necessary conditions" 是一个逻辑上很强的 claim：它意味着在任何设置下，这些条件都是必要的。但实际实验仅在一个极窄的设置上观察到了这些阈值。ρ 覆盖的不完整性尤其明显：ρ=0.2 和 ρ=0.3 均在 degradation zone，ρ=0.4 是 borderline，ρ=0.6 有效——但 ρ=0.5 没有测试，无法确定 boundary 的精确位置。AUC/ECE 阈值来自仅 3 个检测器（TF-IDF+LR, GPT-2, N-gram）的比较，样本量太小。
- 建议：(a) 将 "necessary conditions" 改为 "empirically observed conditions in our setting"；(b) 在 Limitations 中明确讨论跨模型/数据集/污染类型的泛化限制。

**W4** [warning] Epoch confound 实验中 LR schedule 混淆因素未完全排除
- 具体位置：Table 1, §5.1 "LR-controlled verification"
- 问题：Table 1 的 epoch-matched comparison 中，epoch-matched D&R "shares the full-length LR schedule"——即使用完整训练长度的 LR schedule 但仅训练 2,553 步（vs. 原始 6,103 步）。这引入了一个新的混淆：LR schedule 的形状（warmup/decay phase 的比例）在截断训练中与完整训练不同。

  §5.1 提到 "an independent-schedule replication (D&R 17,601 vs shared-schedule uniform 18,062) matches the shared-schedule result (Δ=−0.068)"，但这个 independent-schedule 控制的细节仅在正文中一句话带过，没有在 Table 1 中呈现，也没有在 appendix 中提供完整的 LR 曲线对比。

  更根本的问题：epoch-matched comparison 通过缩短训练来消除 epoch confound，但缩短训练本身改变了训练动态（如 gradient noise scale, batch normalization statistics 等）。一个更干净的控制是在相同步数下，通过 upsampling 非污染数据来匹配 content epochs。
- 建议：(a) 在 appendix 中展示 epoch-matched 和 full-training 的完整 LR curves；(b) 讨论 early-stopping vs. content-epoch-matching 的 confound 可能性；(c) 如果可行，补充 upsampling baseline。

---

## 小问题（不影响接收）

- **m1**: Table 2 中 "Golden Ratio" 行的 w 定义（w = 1/q if q > 0.5, else 0）没有在正文中给出，需要翻到 Appendix C 才能理解。建议在 §4 Methods 中简要说明。

- **m2**: §5.2 中 "Robustness and Boundary Conditions" 小节同时讨论 ρ=0.6 的结果和 boundary conditions，建议拆分为两个子节以提高可读性。

- **m3**: Figure 2 的 x 轴标签 "Sharpening exponent b" 与正文中 "b* per-batch adaptive" 的关系不够清晰——Figure 2 是 grid search 结果，b 是固定值，但正文的叙事已转向 adaptive b*，容易造成混淆。

- **m4**: Appendix Q 的 ρ=0.3 boundary 结果（Δ=+0.002, non-significant）是一个重要数据点，建议在主文 §5.2 中明确引用。

- **m5**: §2 Related Work 中引用了 "Drayson et al., 2025" 在多处但未指出该工作的具体方法与本文的关键区别（from-scratch vs. continued pretraining）——这个区别恰恰是 epoch confound 成立的前提，应在 Related Work 中就明确讨论。

---

## Questions for Authors

1. N=3 的设计是计算资源限制还是有意为之？如果是资源限制，是否考虑过降低训练步数（如 3000 steps）来换取更多 seeds（如 N=7）？这种 tradeoff 在统计上可能更有价值。

2. α_eff-only ablation（去掉 ESS constraint，只保留 α_eff ≥ τ）的 PPL 是多少？Table 2 有 ESS-only 但缺少 α_eff-only。这对理解两个 constraint 的独立贡献至关重要。

3. Rebuttal 中的 per-seed α_eff correlation（Table with r=0.80）与主文 Table 11 的 r=0.70 的区别是什么？前者似乎是 α_eff vs. mean(q)（detector score），后者是 α_eff vs. true real fraction——如果是这样，r=0.80 是检测器自身的 consistency 而非 proxy 的 ground-truth fidelity，不应作为支持 proxy 可靠性的证据。

4. Batch-size amplification实验（§5.4, B=4/8/16）是在固定 total tokens 下进行的，还是固定 steps？如果固定 steps，那 B=16 看到了比 B=4 多 4 倍的 tokens，这本身就是一个 confound。

5. Self-contamination 中 ρ 的设置方式是 token-level injection ratio——这意味着合成 tokens 是均匀混入的。但真实污染是 document-level 的（整个文档是合成的或不是）。Table 1 脚注 2 提到合成文档较短（avg 364 vs 500 words），document-level synthetic fraction 是 35.6% at ρ=0.4。这是否意味着 document-level 的信号更强（整篇合成文档 vs. 随机 token 混入），使检测更容易？

---

## Missing References

论文的引用覆盖在修订后已较完整。建议补充：
- **Xie et al. (2024)**, "DOREMI: Optimizing Data Mixtures Speeds Up Language Model Pretraining"——与 domain-level reweighting 直接相关
- **Fan et al. (2024)** 或相关工作——关于 importance weighting 在 LM 训练中的 variance-bias tradeoff，可为 α_eff/ESS tradeoff 提供理论基础

---

## 主要优势

1. **Epoch confound 发现是扎实且有价值的贡献**：通过 epoch-matched 控制实验证明 D&R 先前报告的 PPL 优势中 >95% 来自多轮数据暴露而非 filtering quality（Table 1, Δ from 0.396 to 0.017, 3 seeds 方向一致），这对后续 D&R 研究有直接方法论警示意义。

2. **检测器校准 vs AUC 的 counter-intuitive 发现**：GPT-2 detector (AUC=0.91, ECE=0.131) 性能劣于 uniform training (Δ=+0.098)，而 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功——揭示了 calibration 可以逆转 intervention 的方向（§5.2, Table 13），这一发现对 data curation 工作有实际指导价值。

3. **诚实的结果报告**：下游 null result（Table 4）、scale 限制（1.7B 效应减弱）、cross-model mixed results（Appendix O）均如实报告，没有 cherry-picking。这种学术诚信值得肯定。

4. **Appendix 覆盖全面**：17 个 appendix 节，涵盖 grid search、threshold sweep、constraint 分解、checkpoint resume artifact、cross-model transfer、低 ρ 分析等，可复现性强。

---

## 总结

本文的分析贡献（epoch confound、detector requirements）是有价值的，达到 Findings 水准。但作为一篇以定量分析为核心的论文，N=3 的统计检验力不足是根本性的弱点——校正后所有 p 值均未达标，bootstrap CI 在 N=3 下不可靠。自适应方法的效应量（0.11% PPL）在当前 scale 下没有实际意义，batch-size 外推是 speculation 而非 evidence。建议在 camera-ready 中：(1) 增加 seeds 或放弃 p 值叙事，(2) 将方法贡献降级为分析框架的 corollary 而非独立贡献，(3) 补充 α_eff-only ablation 以分离两个 constraint 的独立贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1112 · 2026-05-23T13:16:31.313079+00:00_

Reviewer 1 审稿报告已收到。评分 3.0 (Findings)，核心问题集中在 N=3 统计检验力、效应量与 claim 脱节。

等待 Reviewer 2 报告，收齐后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 1113 · 2026-05-23T13:16:41.316523+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断：Overall 3.0 (Findings)**

主要发现：
- **2 个 Must-Fix**：(1) N=3 seeds 统计推断力根本性不足，BH 校正后无显著性，bootstrap CI 在 N=3 下不可靠；(2) 效应量 0.11% PPL + 下游零改善与论文 claim 脱节，batch-size 外推用 3 点拟合幂律不可靠
- **4 个 Should-Fix**：self-contamination 生态效度不足、α_eff proxy R²≈0.49 解释力有限、实验范围过窄不支撑 "necessary conditions" 的普适性、epoch confound 实验中 LR schedule 混淆未完全排除
- **主要优势**：epoch confound 发现扎实有价值、检测器校准 vs AUC 的 counter-intuitive 发现有指导意义、结果报告诚实无 cherry-picking

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1114 · 2026-05-23T13:16:49.050203+00:00_

Reviewer 1 报告已收到（Overall 3.0 Findings）。等待 Reviewer 2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_069d56747de0423c793156b069500cb3:director"
}
```

</details>

---


## Round 84

## Round 84

6 recorded events
