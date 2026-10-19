# Director coordination — Part 5 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 115

### User

_source line 1391 · 2026-05-20T15:36:14.498085+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **REBUT 4 条**：N1（新颖性——C1消融和mask divergence发现有独立贡献）、N2（已通过controlled ablations覆盖DejaVu/ShadowLLM/FastForward）、W3（taxonomy有分析价值）、W4（C1设计意图被误解）
- **AGREE 8 条**：W1（无加速）、W2（规模有限）、M1/M2/M4/M5（minor editorial issues）、MR1-3（missing references）
- **评分分歧**：R2=3.0 vs R1=3.5，核心在于对 empirical contribution bar 的判断不同

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

_source line 1392 · 2026-05-20T15:36:19.452782+00:00_

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


## Round 116

## Round 116

14 recorded events


### User

_source line 1393 · 2026-05-20T15:36:49.571926+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 1 意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 多种子覆盖不一致，存在选择性报告风险**

同意这是一个实质性问题。我在 Table 2 和 Table 5 中验证了 R1 的观察：

- Table 2 caption 使用标记约定（†3-seed, unmarked=seed42），50% KL global PPL 11.79 无 ± 号，确认为 single-seed (s42)
- Table 5 中 50% global 行：PPL 11.79（无±）、MMLU 28.1±0.2（有±），种子覆盖在同一行内不一致
- MSE baseline（Appendix G）全部 single-seed

论文确实 disclose 了种子约定，但 headline result（Table 2 的 "best PPL"）基于 single-seed 而非 3-seed mean，这在 empirical study 中构成选择性报告风险。补充完整 3-seed 评估是合理要求。

---

**[REBUT] R1-N2: PPL 改善与下游任务脱节——R1 选择性引用了下游结果**

R1 的论据存在选择性偏差。R1 仅引用 MMLU（-5.2pp）和 GSM8K（-1.3pp）来支撑"PPL 改善不能转化为下游提升"的结论，但**忽略了论文明确报告的 4 项正面结果**。§4.2 原文："KL outperforms TEAL on commonsense reasoning (ARC-C, WG, HellaSwag, PIQA: 4/4 wins at 30% uniform)"。完整图景是：

| 任务类型 | 30% KL vs TEAL | 方向 |
|---------|---------------|------|
| ARC-C | KL 胜 | ↑ |
| WinoGrande | KL 胜 | ↑ |
| HellaSwag | KL 胜 | ↑ |
| PIQA | KL 胜 | ↑ |
| MMLU | TEAL 胜 (-5.2pp) | ↓ |
| GSM8K | TEAL 胜 (-1.3pp) | ↓ |

因此 R1 的结论"PPL 改善不能转化为下游提升"过度概括。更准确的表述应为：**KL 的 PPL 改善一致地转化为 commonsense reasoning 提升，但在 knowledge-intensive 任务上存在 task-type-dependent 退化。**

但我补充一个 R1 未充分强调的担忧：MMLU（-5.2pp）的退化幅度大于 dense→TEAL 30% 的退化，且 MMLU 是 reviewer 和 AC 最常关注的 benchmark。这一 task-type split 模式值得论文在 §5 Conclusion 中更显著地讨论，而非仅在 §4.2 一句话带过。此外，论文将此归因于 "Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways"，但这只是 post-hoc speculation，没有实验验证。

**结论**：R1-N2 的核心观察（PPL-downstream 不一致）有部分合理性，但将其定为 "critical" 并声称 PPL 改善"不能转化为下游提升"与论文实际报告的 4/6 任务正面结果不符。建议降级为 warning。

---

**[AGREE] R1-N3: 消融实验仅在 50% 稀疏度**

完全同意。Table 3（target-swap ablation）和 Table 4（component ablation）均在 50% sparsity 下进行。论文自身在 §4.6 和 §5 中承认 50% 时 "all methods exhibit downstream collapse"，MMLU 崩溃至 near-random（~28%）。在此 regime 下的消融告诉我们 mask quality 差异，但在实际可用的 30% regime 下：

1. BCE vs KL 的 loss function 选择对 downstream 的影响是否相同？未知
2. Gradient coupling 在 30%（激活更多 neurons）时的贡献是否与 50%（大量 pruning）时相同？未知
3. 30% 时 MMLU 退化（-5.2pp vs TEAL）是否可通过消融归因？未知

这是论文的一个真正盲区。作者应补充 30% sparsity 下至少 Table 4 中关键 configurations（Forward KL+Gumbel、BCE+Gumbel、Forward KL+STE）的对比。

---

### Should-Fix 问题

**[REBUT] R1-W1: 稀疏度控制器偏差导致 headline 数字 misleading**

R1 声称 "headline 19% 基于 mismatched 比较"，但论文在 §4.2 **同一段**中已同时报告了两个数字："reducing TEAL's perplexity by 19% (10.82 → 8.81; **14.5% at matched 28.5% sparsity**, Appendix D)"。Table 2 caption 也明确标注 "Actual achieved sparsity: KL 28.5%, TEAL 29.3% at 30% target"。

- 实际偏差：KL 28.5% vs target 30%（差 1.5pp），TEAL 29.3% vs target 30%（差 0.7pp）
- 两者实际稀疏度之差：0.8pp，不是 R1 暗示的 5%

论文的 disclosure 是充分的。19% 是 headline comparison，14.5% 是 matched comparison，两者均被报告。R1 将此定为 warning 偏严。

---

**[AGREE] R1-W2: Forward KL 方向选择论证不足**

完全同意。我在自己的审稿中也提出了相同问题（我的 M1）。§3.4 使用 D_KL(P_dense || P_sparse)（forward KL）但未论证此选择。MiniLLM (Gu et al., 2024) 专门论证了 reverse KL 对 capacity-limited student 的优势；DistiLLM (Ko et al., 2024) 探索了 skewed KL。论文引用了这两个工作但未讨论 KL 方向选择。补充 forward vs. reverse KL 的消融实验或至少理论论证是合理要求。

---

**[AGREE] R1-W3: 评估域同质性**

同意但补充：论文确实在 Appendix D (Table 11) 进行了 C4 OOD 评估，显示 KL predictor achieves 52.5% relative advantage over TEAL。但 R1 正确指出 C4 方差放大（CV=0.3% in-domain vs. 较高 OOD），且只有一个 OOD domain。训练数据也仅 WikiText-103，作为 empirical study 这限制了 generalizability claims 的强度。

---

**[AGREE] R1-W4: §3.6 梯度分析 informal**

同意。§3.6 的分析直觉上有说服力，但缺乏：(1) ∂L_KL/∂σ_j 的显式展开表达式；(2) coupling degree 的量化指标（如 Hessian off-diagonal magnitude）；(3) 与 BCE 梯度在实际训练中 gradient flow 的经验对比。当前分析本质是 "KL 通过 softmax 耦合所有 neuron" 这一已知事实的叙述性重述，未提供定量新洞察。

---

**[AGREE] R1-W5: 无实际推理加速**

同意。这与我的 W1 重合。Appendix A 报告 predictor overhead 4.4%（Table 6），且 unstructured mask 不能被现有 sparse kernel 加速。论文的贡献严格限于 prediction quality，但 framing 时使用了 "reducing computational burden"（Abstract）等暗示实际效率收益的措辞。

---

### 综合评价

R1 的审稿整体质量高，数据核查细致。我的分歧主要在：

1. **N2 应降为 warning**：R1 选择性引用 MMLU/GSM8K 退化而忽略 4 项 commonsense 提升，不应定为 critical。但 task-type split 的成因分析不足确实是问题。

2. **W1 基本不成立**：论文在同一段中同时报告了 matched 和 unmatched comparison，disclosure 充分。

3. **其他 N1/N3/W2-W5 均同意**，尤其 N1（种子覆盖不一致）和 N3（消融缺 30% regime）是需要补充的实质性 gap。

**我维持 Overall 3.0 (Findings) 的评分。** R1 建议 "补充 30% 消融和完整 multi-seed Table 2 可升至 Conference (4)"——我认为这些补充是必要条件但可能不是充分条件，因为 novelty 不足（我的 N1）和缺少与 trained predictor 的对比（我的 N2）是独立于 R1 意见的额外 concerns。

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

_source line 1394 · 2026-05-20T15:37:21.616467+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 初始化', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Round 1 审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '收敛判断完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0-0.7: 初始化', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Round 1 审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '收敛判断完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-20T15:37:21.667219+00:00_

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

_source line 1396 · 2026-05-20T15:37:26.183884+00:00_

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

_source line 1397 · 2026-05-20T15:37:27.942352+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T15:23:38.338977+00:00\", \"completed_at\": \"2026-05-20T15:26:37.871260+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"pages 1-4\", \"message\": \"前4页无任何 display item（figure/table），连续纯文本+公式。第一个 display item（Table 1 Taxonomy）直到第5页才出现，方法概览图（Figure 1）推迟到第6页。审稿人前2分钟只看到密集文字，无视觉锚点，严重影响第一印象。建议将 Figure 1（Method Overview）前移至第2页（Introduction 末尾或 Method 开头），或在 Introduction 中加入一个概念示意图。\"}, {\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主体正文（含 Conclusion）溢出到第9页顶部（约1/4列），超出 EMNLP 2026 的 8 页正文限制。Ethics Statement 从第9页中部才开始。需压缩正文使 Conclusion 在第8页内结束，否则有 desk-reject 风险。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"三张表格（Table 2/3/4）集中在同一页，视觉密度过高。与前面 4 页纯文本形成极端反差——\\\"荒漠-绿洲\\\"节奏感差。建议将 Table 1 或 Table 3 的位置调整以均匀分布 display items。\"}, {\"severity\": \"warning\", \"dimension\": \"page 18\", \"message\": \"最后一页 Figure 8（Binary Mask Comparison）仅占页面约 40%，上方和下方有大面积空白（约 50-55% 空白）。页面利用率不足。建议合并其他 appendix 内容到此页，或缩小 figure 间距。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-4\", \"message\": \"布局节奏失衡：正文前半段（p1-4）无 figure/table，后半段（p5-8）集中了全部 7 个 display items（2 figures + 5 tables）。理想节奏是每 1.5-2 页穿插一个 display item。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1（Method Overview）是全宽 figure*，设计清晰，箱体+箭头架构图，标签可读。Caption 自包含性良好，能独立理解方法流程。质量合格。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（Per-layer scaling plot）尺寸偏小（约占半栏宽），两条线可区分但 legend 字号接近可读下限。建议适当放大或改为全栏宽。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（Main Results）使用 booktabs 风格，最优值加粗标注，精度一致（小数位统一）。表格格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 3（Lagrangian controller dynamics）左图 y 轴 log scale 标注清晰，右图收敛曲线可读。Figure 4（Per-layer retention）dashed baselines 辅助理解，色彩区分度可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"
…[truncated 495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1758
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-20T15:37:27.942714+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null | head -200",
  "description": "Read current review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null | head -200",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-20T15:37:28.094740+00:00_

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
…[truncated 5518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-20T15:39:40.818305+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 16 — Active issues\n  # ============================================================\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致: headline result (50% KL global PPL 11.79) 为 single-seed, MSE baseline 全部 single-seed\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-N1 提出, R2 交叉回应完全同意. Table 2 headline 基于 s42 而非 3-seed mean.\"}\n    action_items:\n      - {round: 16, action: \"Table 2 所有行补充完整 3-seed 统计; MSE baseline 至少补 2 个种子.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N2\"\n    summary: \"消融实验仅在 50% 稀疏度, 论文实际可用的 30% regime 缺消融覆盖\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-N3 提出, R2 完全同意. Table 4 消融全在 50%, 但 50% downstream 崩溃, 30% loss function 选择效果未知.\"}\n    action_items:\n      - {round: 16, action: \"补充 30% 稀疏度下 Forward KL/JSD/Reverse KL/STE 消融对比.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N3\"\n    summary: \"新颖性不足: 核心是标准 KL distillation 直接应用于 SwiGLU sparsity predictor [分歧]\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2-N1 critical. 技术上无新 loss/优化方法/理论; 与 MaskLLM 核心原理高度重合.\"}\n      - {round: 16, reviewers: [1], note: \"[REBUT] C1 target-swap ablation 设计新颖; mask divergence 46-68% 定量发现; MSE failure 区分 coupling vs alignment. 算法新颖性有限但 empirical insight 足够.\"}\n    action_items:\n      - {round: 16, action: \"分歧记录. R2 认为 EMNLP main 要求 sufficient novelty; R1 认为 empirical contribution bar 可达. 无法通过补实验解决.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N4\"\n    summary: \"缺少与已有训练型稀疏预测器 (DejaVu/ShadowLLM/FastForward) 的数值对比 [分歧]\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2-N2 critical. Taxonomy 预测力未被验证.\"}\n      - {round: 16, reviewers: [1], note: \"[REBUT] controlled ablation 已覆盖: BCE=DejaVu-style, MSE=ShadowLLM/D2DMoE, compensation=FastForward. 同架构/数据/优化器仅变 loss 比直接跑原始代码更严谨.\"}\n    action_items:\n      - {round: 16, action: \"降级为 warning (R1 rebut 有理). 但建议至少在 §4 说明 BCE baseline 等价于 DejaVu-style predictor.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W1\"\n    summary: \"PPL 改善与下游任务 task-type-dependent 脱节: commonsense 4/4 win, knowledge 0/2 lose [分歧]\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1-N2 critical. MMLU -5.2pp, GSM8K -1.3pp vs TEAL at 30%.\"}\n      - {round: 16, reviewers: [2], note: \"[REBUT] R1 选择性引用, 忽略 4/6 正面结果. 应降为 warning. 但 MMLU 退化成因分析不足是实质问题.\"}\n    action_items:\n      - {round: 16, action: \"降级为 warning (R2 rebut 有理). §5 Conclusion 中更显著讨论 task-type split 模式.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W2\"\n    summary: \"无实际推理加速: unstructured mask 无 wall-clock speedup, 增加 6.4% overhead\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W5 + R2-W1. Appendix A 承认. Abstract 'reducing computational burden' 措辞暗示实际效率.\"}\n    action_items:\n      - {round: 16, action: \"调整 framing, 明确定位为 mask quality study 而非 efficiency method.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W3\"\n    summary: \"Forward KL 方向选择论证不足, 标准 KD 文献论证 reverse KL 对 capacity-limited student 更优\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W2 + R2-M1. 论文引用 MiniLLM/DistiLLM 但未讨论 KL 方向选择. 缺 Wen et al. 2024 引用.\"}\n    action_items:\n      - {round: 16, action: \"§3.4 补充 forward vs reverse KL 理论论证, 引用 Wen et al. 2024.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W4\"\n    summary: \"评估域同质性: WikiText-103 训练 + WikiText-2 评估, C4 OOD 方差放大 30×\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W3 + R2-W2. 仅一个 OOD domain.\"}\n    action_items:\n      - {round: 16, action: \"Limitations 明确 domain homogeneity 局限; 可行时补充第二个 OOD domain.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W5\"\n    summary: \"§3.6 梯度分析 informal: 缺显式梯度表达式和 coupling 程度量化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W4 + R2 AGREE. 定性正确但缺定量.\"}\n    action_items:\n      - {round: 16, action: \"§3.6 已标注 'suggestive'. 可补充显式 Jacobian 表达式, 但非 must-fix.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M1\"\n    summary: \"Missing references: activation sparsity opportunities (2412.12178), 2:4 activation sparsity (2503.16672), rethinking KL in KD (2404.02657)\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. 三篇均与论文直接相关.\"}\n    action_items:\n      - {round: 16, action: \"补充三篇引用到 §2 Related Work.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M2\"\n    summary: \"Griffin 引用关联弱, OpenAlex not_found, speculation 无实验支撑\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识.\"}\n    action_items:\n      - {round: 16, action: \"去掉 Griffin speculation 或降低权重.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页 (Conclusion 超出 8 页限制), desk-reject 风险\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [\"visual_check\"], note: \"主体正文含 Conclusion 溢出到第9页顶部约1/4列.\"}\n    action_items:\n      - {round: 16, action: \"压缩正文使 Conclusion 在第8页内结束.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-VIS2\"\n    summary: \"前4页无任何 display item, Figure 1 推迟到第6页, 审稿人第一印象差\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [\"visual_check\"], note: \"前4页纯文本+公式, 第一个 display item 到第5页才出现.\"}\n    action_items:\n      - {round: 16, action: \"将 Figure 1 前移至 Introduction 末尾或 Method 开头.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 15 — Status update\n  # ============================================================\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装，缺乏形式化定义，接近同义反复\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W5.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N1 + R2-N2 共识.\"}\n      - {round: 16, reviewers: [1, 2], note: \"本轮未作为独立 issue 提出, §3.7 当前文本有改善但 R2 仍认为分析价值有限 (R2-W3).\"}\n    action_items:\n      - {round: 15, action: \"全文降级 coupling alignment 措辞.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity 下报告\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 数据核查: Abstract 现报告 '14.5% at matched sparsity (19% at reported 28.5% vs TEAL 30%)'. R2 交叉回应确认 disclosure 充分.\"}\n    resolution: \"Abstract 现同时报告 matched (14.5%) 和 unmatched (19%) 数字, R1 确认格式合规.\"\n    resolution_round: 16\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R2-N1 再次提出 (升级为核心新颖性质疑). R1 REBUT (三点区分 + 问题设定差异). 分歧持续. 转为 R16-N3.\"}\n    action_items:\n      - {round: 15, action: \"§2 MaskLLM 论证已加强.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, downstream task-dependent\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"Abstract 现包含 MMLU 绝对退化 (40.7% vs TEAL 45.9%, both below dense 65.3%). R1 核查通过. 转为 R16-W1 讨论.\"}\n    resolution: \"Abstract 和正文已加入 MMLU 绝对退化数字和 task-type split 描述.\"\n    resolution_round: 16\n\n  - id: \"R15-W2\"\n    summary: \"跨架构/跨规模证据过薄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R2-W2 再次提出. Mistral 3-seed 已有但 Qwen-14B 仍 limited.\"}\n    action_items:\n      - {round: 15, action: \"Contribution list 加 Preliminary 标注.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"BCE+Gumbel 比 standard BCE 更差, KL×Gumbel 交互效应\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [], note: \"本轮未被独立提出. §4.5 已有讨论.\"}\n    action_items:\n      - {round: 15, action: \"§4.5 承认交互效应.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"Training data 单一, OOD downstream 未评估\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R1-W3 + R2-W2 再次提出. C4 OOD PPL 评估已有但 downstream 评估仅 single-seed. 转为 R16-W4.\"}\n    action_items:\n      - {round: 15, action: \"Limitations 补充声明.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"MSE baseline λ_max 差异\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 数据核查: Appendix G 现有技术解释 (MSE 梯度量级 5× 大于 KL, 需较小 λ). 本轮未被独立提出.\"}\n    resolution: \"Appendix G 已包含 λ_max 差异的技术解释. 本轮 R1 核查通过.\"\n    resolution_round: 16\n\n  - id: \"R15-W6\"\n    summary: \"梯度分析缺乏定量支撑\"\n    category: method\n    severity: warning\n    status: wont_fix\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R1-W4 + R2 AGREE 再次提出. 转为 R16-W5.\"}\n    action_items:\n      - {round: 15, action: \"§3.6 已有 suggestive hedge.\", assigned_to: \"paper_agent\", status: wont_fix}\n    resolution: \"§3.6 标注为 suggestive. 接受 warning. R16 再次确认.\"\n    resolution_round: 15\n\n  - id: \"R15-M1\"\n    summary: \"Abstract 选择性呈现数字\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 核查: Abstract 现包含 MMLU 绝对退化. R2 确认.\"}\n    resolution: \"Abstract 已包含 MMLU 退化数字和 task-type split.\"\n    resolution_round: 16\n\n  - id: \"R15-DATA1\"\n    summary: \"limitations.tex PPL 数值来自旧实验\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 核查: Limitations 现报 PPL 10.76, MMLU 35.5%. 数值与正文一致.\"}\n    resolution: \"Limitations PPL 和 MMLU 数值已更新, R1 核查通过.\"\n    resolution_round: 16\n\n  - id: \"R15-DATA2\"\n    summary: \"tab:phase_full 40% global 来自旧 checkpoint\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [], note: \"本轮未被独立提出. tab:phase_full 数值未被本轮 Reviewer 质疑.\"}\n    action_items:\n      - {round: 15, action: \"Agent 跑新 checkpoint 40% global eval.\", assigned_to: \"main_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 14 — Resolved (unchanged)\n  # ============================================================\n\n  - id: \"R14-VIS\"\n    summary: \"Appendix 占位符 figure\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"lagrangian_dynamics.pdf 已用真实数据重新生成.\"\n    resolution_round: 15\n\n  - id: \"R14-W6\"\n    summary: \"Conclusion 过短 + vspace{-18pt}\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"Conclusion 现为完整段落, 无 vspace hack.\"\n    resolution_round: 15\n\n  - id: \"R13-N1\"\n    summary: \"MSE baseline 缺失\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"MSE 30% PPL=20.43, 50% PPL=229.26 + 7-task eval.\"\n    resolution_round: 15\n\n  - id: \"R13-N3\"\n    summary: \"SNR 选择性呈现 + LR schedule 不匹配\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    resolution: \"§3.6 + Appendix H 完整重写.\"\n    resolution_round: 15\n\n  - id: \"R13-W7\"\n    summary: \"C4 OOD 3-seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"3-seed 数据完整.\"\n    resolution_round: 15\n\n  - id: \"R12-N1\"\n    summary: \"C1 50% max Δ 数值错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Corrected to 0.79pp.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 vs Table 4 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Labeling clarified.\"\n    resolution_round: 13\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"C1 target-swap ablation 解决.\"\n    resolution_round: 12"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 16 — Active issues\n  # ============================================================\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致: headline result (50% KL global PPL 11.79) 为 single-seed, MSE baseline 全部 single-seed\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-N1 提出, R2 交叉回应完全同意. Table 2 headline 基于 s42 而非 3-seed mean.\"}\n    action_items:\n      - {round: 16, action: \"Table 2 所有行补充完整 3-seed 统计; MSE baseline 至少补 2 个种子.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N2\"\n    summary: \"消融实验仅在 50% 稀疏度, 论文实际可用的 30% regime 缺消融覆盖\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-N3 提出, R2 完全同意. Table 4 消融全在 50%, 但 50% downstream 崩溃, 30% loss function 选择效果未知.\"}\n    action_items:\n      - {round: 16, action: \"补充 30% 稀疏度下 Forward KL/JSD/Reverse KL/STE 消融对比.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N3\"\n    summary: \"新颖性不足: 核心是标准 KL distillation 直接应用于 SwiGLU sparsity predictor [分歧]\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2-N1 critical. 技术上无新 loss/优化方法/理论; 与 MaskLLM 核心原理高度重合.\"}\n      - {round: 16, reviewers: [1], note: \"[REBUT] C1 target-swap ablation 设计新颖; mask divergence 46-68% 定量发现; MSE failure 区分 coupling vs alignment. 算法新颖性有限但 empirical insight 足够.\"}\n    action_items:\n      - {round: 16, action: \"分歧记录. R2 认为 EMNLP main 要求 sufficient novelty; R1 认为 empirical contribution bar 可达. 无法通过补实验解决.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N4\"\n    summary: \"缺少与已有训练型稀疏预测器 (DejaVu/ShadowLLM/FastForward) 的数值对比 [分歧]\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2-N2 critical. Taxonomy 预测力未被验证.\"}\n      - {round: 16, reviewers: [1], note: \"[REBUT] controlled ablation 已覆盖: BCE=DejaVu-style, MSE=ShadowLLM/D2DMoE, compensation=FastForward. 同架构/数据/优化器仅变 loss 比直接跑原始代码更严谨.\"}\n    action_items:\n      - {round: 16, action: \"降级为 warning (R1 rebut 有理). 但建议至少在 §4 说明 BCE baseline 等价于 DejaVu-style predictor.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W1\"\n    summary: \"PPL 改善与下游任务 task-type-dependent 脱节: commonsense 4/4 win, knowledge 0/2 lose [分歧]\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1-N2 critical. MMLU -5.2pp, GSM8K -1.3pp vs TEAL at 30%.\"}\n      - {round: 16, reviewers: [2], note: \"[REBUT] R1 选择性引用, 忽略 4/6 正面结果. 应降为 warning. 但 MMLU 退化成因分析不足是实质问题.\"}\n    action_items:\n      - {round: 16, action: \"降级为 warning (R2 rebut 有理). §5 Conclusion 中更显著讨论 task-type split 模式.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W2\"\n    summary: \"无实际推理加速: unstructured mask 无 wall-clock speedup, 增加 6.4% overhead\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W5 + R2-W1. Appendix A 承认. Abstract 'reducing computational burden' 措辞暗示实际效率.\"}\n    action_items:\n      - {round: 16, action: \"调整 framing, 明确定位为 mask quality study 而非 efficiency method.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W3\"\n    summary: \"Forward KL 方向选择论证不足, 标准 KD 文献论证 reverse KL 对 capacity-limited student 更优\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W2 + R2-M1. 论文引用 MiniLLM/DistiLLM 但未讨论 KL 方向选择. 缺 Wen et al. 2024 引用.\"}\n    action_items:\n      - {round: 16, action: \"§3.4 补充 forward vs reverse KL 理论论证, 引用 Wen et al. 2024.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W4\"\n    summary: \"评估域同质性: WikiText-103 训练 + WikiText-2 评估, C4 OOD 方差放大 30×\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W3 + R2-W2. 仅一个 OOD domain.\"}\n    action_items:\n      - {round: 16, action: \"Limitations 明确 domain homogeneity 局限; 可行时补充第二个 OOD domain.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W5\"\n    summary: \"§3.6 梯度分析 informal: 缺显式梯度表达式和 coupling 程度量化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W4 + R2 AGREE. 定性正确但缺定量.\"}\n    action_items:\n      - {round: 16, action: \"§3.6 已标注 'suggestive'. 可补充显式 Jacobian 表达式, 但非 must-fix.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M1\"\n    summary: \"Missing references: activation sparsity opportunities (2412.12178), 2:4 activation sparsity (2503.16672), rethinking KL in KD (2404.02657)\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. 三篇均与论文直接相关.\"}\n    action_items:\n      - {round: 16, action: \"补充三篇引用到 §2 Related Work.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M2\"\n    summary: \"Griffin 引用关联弱, OpenAlex not_found, speculation 无实验支撑\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识.\"}\n    action_items:\n      - {round: 16, action: \"去掉 Griffin speculation 或降低权重.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页 (Conclusion 超出 8 页限制), desk-reject 风险\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [\"visual_check\"], note: \"主体正文含 Conclusion 溢出到第9页顶部约1/4列.\"}\n    action_items:\n      - {round: 16, action: \"压缩正文使 Conclusion 在第8页内结束.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-VIS2\"\n    summary: \"前4页无任何 display item, Figure 1 推迟到第6页, 审稿人第一印象差\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [\"visual_check\"], note: \"前4页纯文本+公式, 第一个 display item 到第5页才出现.\"}\n    action_items:\n      - {round: 16, action: \"将 Figure 1 前移至 Introduction 末尾或 Method 开头.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 15 — Status update\n  # ============================================================\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装，缺乏形式化定义，接近同义反复\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - {round: 14, reviewers: [1, 2], note: \"R14-W5.\"}\n      - {round: 15, reviewers: [1, 2], note: \"R1-N1 + R2-N2 共识.\"}\n      - {round: 16, reviewers: [1, 2], note: \"本轮未作为独立 issue 提出, §3.7 当前文本有改善但 R2 仍认为分析价值有限 (R2-W3).\"}\n    action_items:\n      - {round: 15, action: \"全文降级 coupling alignment 措辞.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity 下报告\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 数据核查: Abstract 现报告 '14.5% at matched sparsity (19% at reported 28.5% vs TEAL 30%)'. R2 交叉回应确认 disclosure 充分.\"}\n    resolution: \"Abstract 现同时报告 matched (14.5%) 和 unmatched (19%) 数字, R1 确认格式合规.\"\n    resolution_round: 16\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R2-N1 再次提出 (升级为核心新颖性质疑). R1 REBUT (三点区分 + 问题设定差异). 分歧持续. 转为 R16-N3.\"}\n    action_items:\n      - {round: 15, action: \"§2 MaskLLM 论证已加强.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, downstream task-dependent\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"Abstract 现包含 MMLU 绝对退化 (40.7% vs TEAL 45.9%, both below dense 65.3%). R1 核查通过. 转为 R16-W1 讨论.\"}\n    resolution: \"Abstract 和正文已加入 MMLU 绝对退化数字和 task-type split 描述.\"\n    resolution_round: 16\n\n  - id: \"R15-W2\"\n    summary: \"跨架构/跨规模证据过薄\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R2-W2 再次提出. Mistral 3-seed 已有但 Qwen-14B 仍 limited.\"}\n    action_items:\n      - {round: 15, action: \"Contribution list 加 Preliminary 标注.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W3\"\n    summary: \"BCE+Gumbel 比 standard BCE 更差, KL×Gumbel 交互效应\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [], note: \"本轮未被独立提出. §4.5 已有讨论.\"}\n    action_items:\n      - {round: 15, action: \"§4.5 承认交互效应.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W4\"\n    summary: \"Training data 单一, OOD downstream 未评估\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R1-W3 + R2-W2 再次提出. C4 OOD PPL 评估已有但 downstream 评估仅 single-seed. 转为 R16-W4.\"}\n    action_items:\n      - {round: 15, action: \"Limitations 补充声明.\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W5\"\n    summary: \"MSE baseline λ_max 差异\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 数据核查: Appendix G 现有技术解释 (MSE 梯度量级 5× 大于 KL, 需较小 λ). 本轮未被独立提出.\"}\n    resolution: \"Appendix G 已包含 λ_max 差异的技术解释. 本轮 R1 核查通过.\"\n    resolution_round: 16\n\n  - id: \"R15-W6\"\n    summary: \"梯度分析缺乏定量支撑\"\n    category: method\n    severity: warning\n    status: wont_fix\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"R1-W4 + R2 AGREE 再次提出. 转为 R16-W5.\"}\n    action_items:\n      - {round: 15, action: \"§3.6 已有 suggestive hedge.\", assigned_to: \"paper_agent\", status: wont_fix}\n    resolution: \"§3.6 标注为 suggestive. 接受 warning. R16 再次确认.\"\n    resolution_round: 15\n\n  - id: \"R15-M1\"\n    summary: \"Abstract 选择性呈现数字\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 核查: Abstract 现包含 MMLU 绝对退化. R2 确认.\"}\n    resolution: \"Abstract 已包含 MMLU 退化数字和 task-type split.\"\n    resolution_round: 16\n\n  - id: \"R15-DATA1\"\n    summary: \"limitations.tex PPL 数值来自旧实验\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [1], note: \"R1 核查: Limitations 现报 PPL 10.76, MMLU 35.5%. 数值与正文一致.\"}\n    resolution: \"Limitations PPL 和 MMLU 数值已更新, R1 核查通过.\"\n    resolution_round: 16\n\n  - id: \"R15-DATA2\"\n    summary: \"tab:phase_full 40% global 来自旧 checkpoint\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 16\n    mentions:\n      - {round: 16, reviewers: [], note: \"本轮未被独立提出. tab:phase_full 数值未被本轮 Reviewer 质疑.\"}\n    action_items:\n      - {round: 15, action: \"Agent 跑新 checkpoint 40% global eval.\", assigned_to: \"main_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 14 — Resolved (unchanged)\n  # ============================================================\n\n  - id: \"R14-VIS\"\n    summary: \"Appendix 占位符 figure\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"lagrangian_dynamics.pdf 已用真实数据重新生成.\"\n    resolution_round: 15\n\n  - id: \"R14-W6\"\n    summary: \"Conclusion 过短 + vspace{-18pt}\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"Conclusion 现为完整段落, 无 vspace hack.\"\n    resolution_round: 15\n\n  - id: \"R13-N1\"\n    summary: \"MSE baseline 缺失\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"MSE 30% PPL=20.43, 50% PPL=229.26 + 7-task eval.\"\n    resolution_round: 15\n\n  - id: \"R13-N3\"\n    summary: \"SNR 选择性呈现 + LR schedule 不匹配\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 14\n    resolution: \"§3.6 + Appendix H 完整重写.\"\n    resolution_round: 15\n\n  - id: \"R13-W7\"\n    summary: \"C4 OOD 3-seed\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"3-seed 数据完整.\"\n    resolution_round: 15\n\n  - id: \"R12-N1\"\n    summary: \"C1 50% max Δ 数值错误\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Corrected to 0.79pp.\"\n    resolution_round: 13\n\n  - id: \"R12-N2\"\n    summary: \"Table 2 vs Table 4 数值矛盾\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Labeling clarified.\"\n    resolution_round: 13\n\n  - id: \"R8-N1\"\n    summary: \"Coupling vs oracle quality confound\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 12\n    resolution: \"C1 target-swap ablation 解决.\"\n    resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-20T15:39:40.920335+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 15175}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-20T15:41:47.490684+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: 重新审稿 (fresh)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）\n\n---\n\n## Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。轻量级 predictor（75.9M 参数，<1% base model）通过 Gumbel-Sigmoid 松弛和 adaptive penalty controller 实现端到端训练。在 LLaMA-3.1-8B 上 30% 稀疏度下 PPL 相对 TEAL 降低 14.5%（matched sparsity），commonsense reasoning 4/4 任务胜出，但 knowledge-intensive 任务退化（MMLU -5.2pp）。Target-swap ablation 表明 KL 发现的 mask targets（与 magnitude 46-68% 不同）是质量驱动因素。跨架构验证（Mistral-7B 3-seed, Qwen-14B preliminary）显示 PPL 优势泛化但下游结果 task/scale-dependent。论文自述为 \"primarily empirical study\"。\n\n---\n\n## Strengths\n\n**S1. C1 Target-Swap Ablation 设计精妙 [R1, R2 共识]**\n§4.4 的目标-交换消融有效解耦了 mask quality 和 gradient coupling 的贡献——BCE 在 KL-derived targets 上重现 KL 质量（max Δ≤0.79pp at 50%），确认 mask targets 而非 coupling 机制本身驱动 inference-stage 质量。此实验设计在 activation sparsity 文献中未见先例。\n\n**S2. 诚实报告负面结果 [R1, R2 共识]**\nMMLU/GSM8K 退化（30%）、Mistral GSM8K 反转、Qwen-14B 推理崩溃（-20pp）、50% 下游全面崩溃均被明确报告。Limitations 部分全面且自我批评。\n\n**S3. 受控实验设计**\nMSE baseline（Appendix G）保持架构/数据/优化器完全一致仅变 loss function；BCE extended training（2700 steps）控制 compute budget；敏感性分析覆盖 bottleneck/温度/训练步数（均 <3% PPL 变化）。\n\n**S4. 训练效率高**\n1000 步、~45 min、单 GPU (RTX PRO 6000)，75.9M 参数（<1% base）。实用门槛低。\n\n**S5. 丰富的附录支撑**\n10 页附录覆盖 inference latency、bottleneck sensitivity、温度调度、训练收敛、penalty dynamics、OOD 评估、per-layer retention、mask 可视化、cross-architecture 详细结果。\n\n**S6. 数据一致性和格式合规通过核查 [R1 验证]**\n表格间数字全部匹配；Abstract 数字验证通过；引用 47 条无虚假引用；正文 8 页合规；double-blind 合规。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 多种子覆盖不一致，存在选择性报告风险 [R1-N1, R2 AGREE]**\nTable 2 headline result（50% KL global PPL 11.79）为 single-seed (s42)，而次优结果（50% KL uniform 11.92±0.07）为 3-seed。MSE baseline（支撑核心 \"coupling alignment\" 论点）全部 single-seed。当最优结果为 single-seed 时，读者无法判断其是否在 multi-seed 分布的幸运端。\n\n**C2. 消融实验仅在 50% 稀疏度，实际可用的 30% regime 缺失 [R1-N3, R2 AGREE]**\nTable 4 所有消融（Forward KL/JSD/Reverse KL/STE/BCE variants）均在 50%。但论文自身承认 50% downstream 崩溃至随机水平（\"capacity-limited regime\"），30% 才是可用稀疏度。在 30% 下 loss function 选择效果未知——如果 forward KL 相对 JSD/reverse KL 的优势缩小甚至消失，论文的核心结论可能不成立。\n\n**C3. 新颖性不足 [R2-N1 critical, R1 REBUT — 分歧]**\nR2 认为：KL distillation 匹配 teacher/student 输出分布是经典范式；Gumbel-Sigmoid、adaptive Lagrangian、TEAL allocation 均为已有技术组合；与 MaskLLM 核心训练原理高度重合。R1 反驳：C1 ablation 设计新颖、mask divergence 46-68% 是新定量发现、MSE catastrophic failure 区分了 coupling 和 output-alignment。**两位 Reviewer 均同意算法新颖性有限，分歧在于 empirical insights 是否足以弥补。**\n\n### Warning（应修复但不阻挡接收）\n\n**W1. PPL 改善与下游任务 task-type-dependent 脱节 [R1-N2 critical → R2 降级为 warning]**\n30% 稀疏度下 KL vs TEAL：commonsense 4/4 胜（ARC +4.4pp, HS +7.8pp, WG +3.9pp, PIQA +2.2pp），knowledge 0/2 败（MMLU -5.2pp, GSM8K -1.3pp）。R1 认为 critical（PPL 改善未转化为一致的下游提升），R2 指出 R1 选择性引用了负面结果。**综合判断降为 warning**：task-type split 真实存在但论文已报告；MMLU 退化成因（forward KL mode-covering hypothesis）缺实验验证。\n\n**W2. 无实际推理加速 [R1-W5, R2-W1 AGREE]**\nAppendix A 明确承认 unstructured mask 不能被现有 sparse kernel 加速，pipeline 增加 6.4% overhead。论文贡献严格限于 prediction quality，但 framing 暗示效率收益。\n\n**W3. Forward KL 方向选择论证不足 [R1-W2, R2-M1 AGREE]**\n§3.4 使用 forward KL 但未论证选择理由。标准 KD 文献（MiniLLM, DistiLLM）讨论 reverse KL 对 capacity-limited student 的优势。实验（Table 4）验证了 forward > reverse，但理论解释缺失。\n\n**W4. 评估域同质性 [R1-W3, R2-W2 AGREE]**\nWikiText-103 训练 + WikiText-2 评估（同为 Wikipedia）。C4 OOD 评估（Appendix D）显示 cross-seed CV 从 0.2% 增至 6.3%，方差放大 30×。仅一个 OOD domain。\n\n**W5. §3.6 梯度分析 informal [R1-W4, R2 AGREE]**\n分析直觉正确但缺乏：(1) ∂L_KL/∂s_j 的显式展开；(2) coupling degree 量化指标；(3) 低 SNR 产生更好 mask 的正式解释。§3.6 已标注 \"suggestive\"。\n\n**W6. 缺少与已有训练型预测器的直接数值对比 [R2-N2 critical → R1 降级]**\nR2 认为缺 DejaVu/ShadowLLM/FastForward 数值对比。R1 反驳：controlled ablation 已等价覆盖（BCE=DejaVu, MSE=ShadowLLM, compensation=FastForward）。**综合判断降为 warning**：R1 的论点有理，但 §4 应明确标注 baseline 与已有方法的等价关系。\n\n**W7. Taxonomy (Table 1) 分析价值有限 [R2-W3, R1 REBUT]**\n矩阵 5/6 cell 有代表方法（R1 指出），但 taxonomy 的 predictive power 未通过系统对比验证。空 cell 未讨论。降为 minor editorial issue。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **多种子覆盖需补全**（C1）：Table 2 所有行应有 3-seed 统计；MSE 至少 2 额外种子\n2. **30% regime 需消融覆盖**（C2）：Forward KL/JSD/Reverse KL/STE 在 30% 的对比\n3. **无实际加速**（W2）：framing 应调整为 mask quality study\n4. **Forward KL 论证不足**（W3）：需理论或更充分的经验论证\n5. **评估域同质性**（W4）：Limitations 应更明确\n6. **梯度分析 informal**（W5）：已有 suggestive hedge，可接受\n7. **Missing references**：三篇应补充（activation sparsity opportunities, 2:4 activation sparsity, rethinking KL in KD）\n8. **Griffin 引用**：关联弱，应去掉或降权\n\n## Reviewer Divergence [REBUT]\n\n1. **新颖性（C3）**：R2 (3.0) 认为标准 KL 应用 novelty 不足以支撑 main conference；R1 (3.5) 认为 C1 ablation + mask divergence + MSE failure 的 empirical insights 足够 borderline。核心分歧在于 EMNLP main 对 empirical-only contribution 的接收门槛。\n2. **PPL-下游脱节严重性（W1）**：R1 认为 critical（MMLU/GSM8K 退化），R2 认为 warning（4/6 任务正面）。综合为 warning。\n3. **已有方法对比（W6）**：R2 认为 critical（需直接数值对比），R1 认为 controlled ablation 已覆盖。综合为 warning。\n\n---\n\n## Questions\n\n1. Table 4 消融是否做了多种子？BCE+STE vs KL 的 Δ=0.62 PPL 是否统计显著？（R2-Q1, R1 AGREE）\n2. 为何不在 SwiGLU gate 分支做 sparsity prediction？Gate 的 sigmoid 输出天然接近二值化。（R2-Q2）\n3. Adaptive penalty controller 超参数（ε=0.02, doubling rate）的敏感性分析？（R2-Q4, R1 AGREE）\n4. MMLU/GSM8K 退化的 per-task mask overlap 分析？（R1-N2 延伸）\n5. 30% 稀疏度下 forward vs reverse KL 的下游表现差异？（R1-N3 核心）\n\n---\n\n## Missing References\n\n1. \"Activation Sparsity Opportunities for Compressing General Large Language Models\" (arXiv:2412.12178, Dec 2024) — SwiGLU FFN 稀疏化机会的系统研究 [R1, R2 AGREE]\n2. \"Accelerating Transformer Inference and Training with 2:4 Activation Sparsity\" (arXiv:2503.16672, Mar 2025) — 结构化 activation sparsity，与 future work 直接相关 [R1, R2 AGREE]\n3. \"Rethinking KL Divergence in Knowledge Distillation for Large Language Models\" (Wen et al., arXiv:2404.02657, 2024) — forward vs reverse KL 分析，与 §3.4 直接相关 [R1, R2 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（耗时 ~3 min）\n\n**Critical**:\n- **正文溢出第 9 页**：Conclusion 超出 8 页正文限制，Ethics Statement 从第 9 页中部才开始。有 desk-reject 风险。\n- **前 4 页无任何 display item**：Figure 1（Method Overview）直到第 6 页才出现，审稿人前 2 分钟仅看到密集文字，无视觉锚点。\n\n**Warning**:\n- 第 7 页三张表格（Table 2/3/4）集中，与前 4 页纯文本形成极端\"荒漠-绿洲\"反差\n- Appendix 最后一页 Figure 8 仅占 40% 页面，空白过多\n- 布局节奏失衡：前半段无 display item，后半段集中全部 7 个\n\n**Info**: Figure 1 设计清晰；Table 2 booktabs 格式规范；公式渲染正确；参考文献无 [?] 残留。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**评分理由**：\n\n论文在受控实验设计（C1 target-swap ablation）、mask divergence 的定量发现（46-68%）、以及 MSE catastrophic failure 的实证上有价值。敏感性分析全面，负面结果报告诚实，训练成本极低。\n\n但存在三个结构性问题阻碍 main conference 接收：\n1. **消融覆盖缺口**（C2）：核心 loss function 选择消融仅在 50%（downstream 崩溃的 regime），实际可用的 30% 缺消融——这是 empirical study 的根本性 gap\n2. **多种子不一致**（C1）：headline result 为 single-seed，作为 empirical study 统计严谨性不足\n3. **新颖性天花板**（C3）：方法是已有技术的组合应用，贡献主要在 empirical insights 层面；两位 Reviewer 对是否足够存在分歧\n\n如果能补充 30% 消融数据和完整 multi-seed Table 2，论文可升至 Borderline Conference (3.5)。新颖性问题是结构性的，需更深的理论贡献或更广的实验覆盖（多模型、多任务、实际加速）来弥补。\n\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Soundness | 3.5/5 | 技术正确，消融设计好，但多种子覆盖和消融 regime 有 gap |\n| Excitement | 2.5/5 | Empirical insights 有价值但算法无新意，无 runtime speedup |\n| Reproducibility | 4.0/5 | 超参完整，单 GPU 可复现，但代码不可用 |\n| Overall | 3.0/5 | Findings 水平 — empirical 发现有价值但 novelty 和实验全面性未达 main conference |\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"primarily empirical study\" 声明诚实但在 EMNLP submission 中是双刃剑——明确管理了期望但也降低了 perceived contribution\n- Contribution list 第 4 条（allocation-to-downstream interactions）缺 \"preliminary\" 标注\n\n### §2 Related Work\n- MaskLLM 三点区分（sparsity type / mask generation / allocation）是有效的，但 R2 指出核心训练原理重合度高\n- 缺三篇重要引用（见 Missing References）\n- Griffin speculation 无实验支撑，建议去掉\n\n### §3 Method\n- §3.6 梯度分析直觉正确但 informal（缺显式表达式和量化）\n- §3.7 Taxonomy 分析框架有用但 predictive power 未充分验证\n- Forward KL 选择（§3.4）需理论论证\n\n### §4 Experiments\n- Table 2：需完整 3-seed 覆盖\n- Table 4：需 30% regime 消融\n- C1 ablation 设计精妙但 oracle mask 来自 KL 训练的 confound 应被明确讨论\n- BCE baseline 等价于 DejaVu-style predictor 应在文中显式标注\n- MSE baseline single-seed 不够（尽管 1.9×/9.6× gap 使 seed sensitivity 不太可能改变结论）\n\n### §5 Conclusion\n- Task-type split（commonsense vs knowledge）应更显著地讨论，而非仅在 §4.2 一句话\n- \"Future work: N:M sparsity and 70B+\" 暗示当前工作不完整\n\n### Limitations\n- 全面且自我批评，质量高\n- 可补充 \"domain homogeneity\" 和 \"30% 消融缺失\" 的明确声明\n\n### 格式\n- ⚠️ **正文溢出第 9 页** — 需压缩使 Conclusion 在第 8 页内结束（desk-reject 风险）\n- Figure 1 应前移至第 2 页以改善视觉节奏",
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
    "report": "# 审稿报告 — Round 16 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: 重新审稿 (fresh)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）\n\n---\n\n## Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。轻量级 predictor（75.9M 参数，<1% base model）通过 Gumbel-Sigmoid 松弛和 adaptive penalty controller 实现端到端训练。在 LLaMA-3.1-8B 上 30% 稀疏度下 PPL 相对 TEAL 降低 14.5%（matched sparsity），commonsense reasoning 4/4 任务胜出，但 knowledge-intensive 任务退化（MMLU -5.2pp）。Target-swap ablation 表明 KL 发现的 mask targets（与 magnitude 46-68% 不同）是质量驱动因素。跨架构验证（Mistral-7B 3-seed, Qwen-14B preliminary）显示 PPL 优势泛化但下游结果 task/scale-dependent。论文自述为 \"primarily empirical study\"。\n\n---\n\n## Strengths\n\n**S1. C1 Target-Swap Ablation 设计精妙 [R1, R2 共识]**\n§4.4 的目标-交换消融有效解耦了 mask quality 和 gradient coupling 的贡献——BCE 在 KL-derived targets 上重现 KL 质量（max Δ≤0.79pp at 50%），确认 mask targets 而非 coupling 机制本身驱动 inference-stage 质量。此实验设计在 activation sparsity 文献中未见先例。\n\n**S2. 诚实报告负面结果 [R1, R2 共识]**\nMMLU/GSM8K 退化（30%）、Mistral GSM8K 反转、Qwen-14B 推理崩溃（-20pp）、50% 下游全面崩溃均被明确报告。Limitations 部分全面且自我批评。\n\n**S3. 受控实验设计**\nMSE baseline（Appendix G）保持架构/数据/优化器完全一致仅变 loss function；BCE extended training（2700 steps）控制 compute budget；敏感性分析覆盖 bottleneck/温度/训练步数（均 <3% PPL 变化）。\n\n**S4. 训练效率高**\n1000 步、~45 min、单 GPU (RTX PRO 6000)，75.9M 参数（<1% base）。实用门槛低。\n\n**S5. 丰富的附录支撑**\n10 页附录覆盖 inference latency、bottleneck sensitivity、温度调度、训练收敛、penalty dynamics、OOD 评估、per-layer retention、mask 可视化、cross-architecture 详细结果。\n\n**S6. 数据一致性和格式合规通过核查 [R1 验证]**\n表格间数字全部匹配；Abstract 数字验证通过；引用 47 条无虚假引用；正文 8 页合规；double-blind 合规。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. 多种子覆盖不一致，存在选择性报告风险 [R1-N1, R2 AGREE]**\nTable 2 headline result（50% KL global PPL 11.79）为 single-seed (s42)，而次优结果（50% KL uniform 11.92±0.07）为 3-seed。MSE baseline（支撑核心 \"coupling alignment\" 论点）全部 single-seed。当最优结果为 single-seed 时，读者无法判断其是否在 multi-seed 分布的幸运端。\n\n**C2. 消融实验仅在 50% 稀疏度，实际可用的 30% regime 缺失 [R1-N3, R2 AGREE]**\nTable 4 所有消融（Forward KL/JSD/Reverse KL/STE/BCE variants）均在 50%。但论文自身承认 50% downstream 崩溃至随机水平（\"capacity-limited regime\"），30% 才是可用稀疏度。在 30% 下 loss function 选择效果未知——如果 forward KL 相对 JSD/reverse KL 的优势缩小甚至消失，论文的核心结论可能不成立。\n\n**C3. 新颖性不足 [R2-N1 critical, R1 REBUT — 分歧]**\nR2 认为：KL distillation 匹配 teacher/student 输出分布是经典范式；Gumbel-Sigmoid、adaptive Lagrangian、TEAL allocation 均为已有技术组合；与 MaskLLM 核心训练原理高度重合。R1 反驳：C1 ablation 设计新颖、mask divergence 46-68% 是新定量发现、MSE catastrophic failure 区分了 coupling 和 output-alignment。**两位 Reviewer 均同意算法新颖性有限，分歧在于 empirical insights 是否足以弥补。**\n\n### Warning（应修复但不阻挡接收）\n\n**W1. PPL 改善与下游任务 task-type-dependent 脱节 [R1-N2 critical → R2 降级为 warning]**\n30% 稀疏度下 KL vs TEAL：commonsense 4/4 胜（ARC +4.4pp, HS +7.8pp, WG +3.9pp, PIQA +2.2pp），knowledge 0/2 败（MMLU -5.2pp, GSM8K -1.3pp）。R1 认为 critical（PPL 改善未转化为一致的下游提升），R2 指出 R1 选择性引用了负面结果。**综合判断降为 warning**：task-type split 真实存在但论文已报告；MMLU 退化成因（forward KL mode-covering hypothesis）缺实验验证。\n\n**W2. 无实际推理加速 [R1-W5, R2-W1 AGREE]**\nAppendix A 明确承认 unstructured mask 不能被现有 sparse kernel 加速，pipeline 增加 6.4% overhead。论文贡献严格限于 prediction quality，但 framing 暗示效率收益。\n\n**W3. Forward KL 方向选择论证不足 [R1-W2, R2-M1 AGREE]**\n§3.4 使用 forward KL 但未论证选择理由。标准 KD 文献（MiniLLM, DistiLLM）讨论 reverse KL 对 capacity-limited student 的优势。实验（Table 4）验证了 forward > reverse，但理论解释缺失。\n\n**W4. 评估域同质性 [R1-W3, R2-W2 AGREE]**\nWikiText-103 训练 + WikiText-2 评估（同为 Wikipedia）。C4 OOD 评估（Appendix D）显示 cross-seed CV 从 0.2% 增至 6.3%，方差放大 30×。仅一个 OOD domain。\n\n**W5. §3.6 梯度分析 informal [R1-W4, R2 AGREE]**\n分析直觉正确但缺乏：(1) ∂L_KL/∂s_j 的显式展开；(2) coupling degree 量化指标；(3) 低 SNR 产生更好 mask 的正式解释。§3.6 已标注 \"suggestive\"。\n\n**W6. 缺少与已有训练型预测器的直接数值对比 [R2-N2 critical → R1 降级]**\nR2 认为缺 DejaVu/ShadowLLM/FastForward 数值对比。R1 反驳：controlled ablation 已等价覆盖（BCE=DejaVu, MSE=ShadowLLM, compensation=FastForward）。**综合判断降为 warning**：R1 的论点有理，但 §4 应明确标注 baseline 与已有方法的等价关系。\n\n**W7. Taxonomy (Table 1) 分析价值有限 [R2-W3, R1 REBUT]**\n矩阵 5/6 cell 有代表方法（R1 指出），但 taxonomy 的 predictive power 未通过系统对比验证。空 cell 未讨论。降为 minor editorial issue。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **多种子覆盖需补全**（C1）：Table 2 所有行应有 3-seed 统计；MSE 至少 2 额外种子\n2. **30% regime 需消融覆盖**（C2）：Forward KL/JSD/Reverse KL/STE 在 30% 的对比\n3. **无实际加速**（W2）：framing 应调整为 mask quality study\n4. **Forward KL 论证不足**（W3）：需理论或更充分的经验论证\n5. **评估域同质性**（W4）：Limitations 应更明确\n6. **梯度分析 informal**（W5）：已有 suggestive hedge，可接受\n7. **Missing references**：三篇应补充（activation sparsity opportunities, 2:4 activation sparsity, rethinking KL in KD）\n8. **Griffin 引用**：关联弱，应去掉或降权\n\n## Reviewer Divergence [REBUT]\n\n1. **新颖性（C3）**：R2 (3.0) 认为标准 KL 应用 novelty 不足以支撑 main conference；R1 (3.5) 认为 C1 ablation + mask divergence + MSE failure 的 empirical insights 足够 borderline。核心分歧在于 EMNLP main 对 empirical-only contribution 的接收门槛。\n2. **PPL-下游脱节严重性（W1）**：R1 认为 critical（MMLU/GSM8K 退化），R2 认为 warning（4/6 任务正面）。综合为 warning。\n3. **已有方法对比（W6）**：R2 认为 critical（需直接数值对比），R1 认为 controlled ablation 已覆盖。综合为 warning。\n\n---\n\n## Questions\n\n1. Table 4 消融是否做了多种子？BCE+STE vs KL 的 Δ=0.62 PPL 是否统计显著？（R2-Q1, R1 AGREE）\n2. 为何不在 SwiGLU gate 分支做 sparsity prediction？Gate 的 sigmoid 输出天然接近二值化。（R2-Q2）\n3. Adaptive penalty controller 超参数（ε=0.02, doubling rate）的敏感性分析？（R2-Q4, R1 AGREE）\n4. MMLU/GSM8K 退化的 per-task mask overlap 分析？（R1-N2 延伸）\n5. 30% 稀疏度下 forward vs reverse KL 的下游表现差异？（R1-N3 核心）\n\n---\n\n## Missing References\n\n1. \"Activation Sparsity Opportunities for Compressing General Large Language Models\" (arXiv:2412.12178, Dec 2024) — SwiGLU FFN 稀疏化机会的系统研究 [R1, R2 AGREE]\n2. \"Accelerating Transformer Inference and Training with 2:4 Activation Sparsity\" (arXiv:2503.16672, Mar 2025) — 结构化 activation sparsity，与 future work 直接相关 [R1, R2 AGREE]\n3. \"Rethinking KL Divergence in Knowledge Distillation for Large Language Models\" (Wen et al., arXiv:2404.02657, 2024) — forward vs reverse KL 分析，与 §3.4 直接相关 [R1, R2 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（耗时 ~3 min）\n\n**Critical**:\n- **正文溢出第 9 页**：Conclusion 超出 8 页正文限制，Ethics Statement 从第 9 页中部才开始。有 desk-reject 风险。\n- **前 4 页无任何 display item**：Figure 1（Method Overview）直到第 6 页才出现，审稿人前 2 分钟仅看到密集文字，无视觉锚点。\n\n**Warning**:\n- 第 7 页三张表格（Table 2/3/4）集中，与前 4 页纯文本形成极端\"荒漠-绿洲\"反差\n- Appendix 最后一页 Figure 8 仅占 40% 页面，空白过多\n- 布局节奏失衡：前半段无 display item，后半段集中全部 7 个\n\n**Info**: Figure 1 设计清晰；Table 2 booktabs 格式规范；公式渲染正确；参考文献无 [?] 残留。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n**评分理由**：\n\n论文在受控实验设计（C1 target-swap ablation）、mask divergence 的定量发现（46-68%）、以及 MSE catastrophic failure 的实证上有价值。敏感性分析全面，负面结果报告诚实，训练成本极低。\n\n但存在三个结构性问题阻碍 main conference 接收：\n1. **消融覆盖缺口**（C2）：核心 loss function 选择消融仅在 50%（downstream 崩溃的 regime），实际可用的 30% 缺消融——这是 empirical study 的根本性 gap\n2. **多种子不一致**（C1）：headline result 为 single-seed，作为 empirical study 统计严谨性不足\n3. **新颖性天花板**（C3）：方法是已有技术的组合应用，贡献主要在 empirical insights 层面；两位 Reviewer 对是否足够存在分歧\n\n如果能补充 30% 消融数据和完整 multi-seed Table 2，论文可升至 Borderline Conference (3.5)。新颖性问题是结构性的，需更深的理论贡献或更广的实验覆盖（多模型、多任务、实际加速）来弥补。\n\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Soundness | 3.5/5 | 技术正确，消融设计好，但多种子覆盖和消融 regime 有 gap |\n| Excitement | 2.5/5 | Empirical insights 有价值但算法无新意，无 runtime speedup |\n| Reproducibility | 4.0/5 | 超参完整，单 GPU 可复现，但代码不可用 |\n| Overall | 3.0/5 | Findings 水平 — empirical 发现有价值但 novelty 和实验全面性未达 main conference |\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"primarily empirical study\" 声明诚实但在 EMNLP submission 中是双刃剑——明确管理了期望但也降低了 perceived contribution\n- Contribution list 第 4 条（allocation-to-downstream interactions）缺 \"preliminary\" 标注\n\n### §2 Related Work\n- MaskLLM 三点区分（sparsity type / mask generation / allocation）是有效的，但 R2 指出核心训练原理重合度高\n- 缺三篇重要引用（见 Missing References）\n- Griffin speculation 无实验支撑，建议去掉\n\n### §3 Method\n- §3.6 梯度分析直觉正确但 informal（缺显式表达式和量化）\n- §3.7 Taxonomy 分析框架有用但 predictive power 未充分验证\n- Forward KL 选择（§3.4）需理论论证\n\n### §4 Experiments\n- Table 2：需完整 3-seed 覆盖\n- Table 4：需 30% regime 消融\n- C1 ablation 设计精妙但 oracle mask 来自 KL 训练的 confound 应被明确讨论\n- BCE baseline 等价于 DejaVu-style predictor 应在文中显式标注\n- MSE baseline single-seed 不够（尽管 1.9×/9.6× gap 使 seed sensitivity 不太可能改变结论）\n\n### §5 Conclusion\n- Task-type split（commonsense vs knowledge）应更显著地讨论，而非仅在 §4.2 一句话\n- \"Future work: N:M sparsity and 70B+\" 暗示当前工作不完整\n\n### Limitations\n- 全面且自我批评，质量高\n- 可补充 \"domain homogeneity\" 和 \"30% 消融缺失\" 的明确声明\n\n### 格式\n- ⚠️ **正文溢出第 9 页** — 需压缩使 Conclusion 在第 8 页内结束（desk-reject 风险）\n- Figure 1 应前移至第 2 页以改善视觉节奏",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-20T15:41:51.304851+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-20T15:41:59.062880+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 初始化', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Round 1 审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '收敛判断完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
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
    "todos": "[{'content': 'Step 0-0.7: 初始化', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Round 1 审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '收敛判断完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-20T15:41:59.063431+00:00_

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

_source line 1406 · 2026-05-20T15:42:06.329843+00:00_

**Round 16 审稿完成。**

报告已投递至 Research Director。

**最终评分：3.0 (Findings)**

关键行动项（按优先级）：
1. **[desk-reject 风险]** 正文溢出第 9 页，需立即压缩
2. **[C2]** 补充 30% 稀疏度消融（Forward KL/JSD/Reverse KL/STE）
3. **[C1]** Table 2 所有行补 3-seed；MSE 补至少 2 个种子
4. **[W3]** §3.4 补 forward KL 方向选择论证
5. **[布局]** Figure 1 前移至第 2 页

Issue Tracker 已同步更新（Round 16：3 critical, 7 warning, 2 minor 新增；R15 中 5 项已标记 resolved）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1407 · 2026-05-20T15:42:09.129364+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 意见的逐条回应。要点总结：

- **N1（种子不一致）、N3（消融缺 30%）、W2-W5**：全部 AGREE
- **N2（PPL-下游脱节）**：REBUT——R1 选择性引用 MMLU/GSM8K 退化而忽略 4 项 commonsense 提升，建议降为 warning
- **W1（稀疏度偏差）**：REBUT——论文同段已报告 matched comparison（14.5%），disclosure 充分

维持 Overall 3.0 (Findings) 评分不变。

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

_source line 1408 · 2026-05-20T15:42:20.667462+00:00_

审稿流程已全部完成。报告已投递给 Research Director。

**Round 16 审稿结论：Overall 3.0 (Findings)**

关键行动项（按优先级）：

1. **[desk-reject 风险]** 正文溢出第 9 页 → 压缩使 Conclusion 在第 8 页内结束
2. **[C1]** Table 2 所有行补完整 3-seed 统计；MSE baseline 补种子
3. **[C2]** 补充 30% 稀疏度下 Forward KL/JSD/Reverse KL/STE 消融
4. **[C3/分歧]** 新颖性天花板——结构性问题，需更深理论或更广实验覆盖
5. **[W1-W7]** Forward KL 论证、framing 调整、missing references 等

R1 评估：补充 C1+C2 后可升至 3.5 (Borderline Conference)。R2 认为 novelty 问题独立于实验补充，即使补全仍可能停留在 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 118

## Round 118

52 recorded events


### User

_source line 1409 · 2026-05-21T01:17:06.467509+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May cycle)
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

_source line 1410 · 2026-05-21T01:17:21.024790+00:00_

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

_source line 1411 · 2026-05-21T01:17:21.075875+00:00_

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

_source line 1412 · 2026-05-21T01:17:25.752136+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
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
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-21T01:17:25.802871+00:00_



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

_source line 1414 · 2026-05-21T01:17:28.617469+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1415 · 2026-05-21T01:17:28.617829+00:00_

No matching deferred tools found

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

_source line 1416 · 2026-05-21T01:17:34.853517+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1417 · 2026-05-21T01:17:34.853937+00:00_



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

_source line 1418 · 2026-05-21T01:17:39.903316+00:00_

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

_source line 1419 · 2026-05-21T01:17:40.859687+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-21T01:17:42.215079+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (311 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中 (4/4 GPU 满载)\n- bce_iso_v3_s42_30pct_uniform_eval: westd-34887:cuda:0, PID 249865 — 补齐 BCE iso-v3 3-seed (30% uniform)，约 73 分钟\n- jsd_30_s123: westd-34887:cuda:1, PID 250592 — JSD 训练+PPL eval，约 35 分钟\n- jsd_30_s456: westd-41718:cuda:0, PID 292012 — JSD 训练+PPL eval，约 35 分钟\n- revkl_30_s123: westd-41718:cuda:1, PID 292156 — RevKL 训练+PPL eval，约 35 分钟\n\n## 排队\n- revkl_30_s456: 待上述 3 个最先完成的释放 GPU\n\n## 刚完成（本轮）\n- **bce_iso_v3_s123_30pct_uniform_eval** (success): PPL=15.2051\n- **bce_iso_v3_s456_30pct_uniform_eval** (success): PPL=15.1102\n- **teal_30pct_uniform_multiseed_eval** (success): PPL=10.8173 (确定性，1 seed 即可)\n\n## Table 4 30% multi-seed 进度\n| Loss | s42 PPL | s123 PPL | s456 PPL | 状态 |\n|------|---------|----------|----------|------|\n| KL | 8.82 | 8.83 | 8.79 | ✅ 完整 |\n| JSD | 8.88 | ⏳ | ⏳ | 训练中 |\n| RevKL | 9.31 | ⏳ | 📋 | s123 训练中, s456 排队 |\n| BCE iso-v3 | ⏳ | 15.21 | 15.11 | s42 eval 运行中 |\n\n## 趋势\n成功 212 / 负向 23 / 失败 29 / 共 281+\n\n## 下一步\n- 首批训练完成 (~35min) → 提交 revkl_30_s456 + 收集结果\n- bce_iso_v3_s42 eval 完成 (~73min) → 3-seed mean±std → 更新 Table 2\n- 全部完成后 → 汇报 Director 完整 Table 4 multi-seed 数据\n- DDL: 2026-05-25 (4 天)\n\n## 资源状态\nwestd-34887: cuda:0 bce_eval / cuda:1 jsd_t
…[truncated 58 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2311
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-21T01:17:42.417533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "80"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-21T01:17:42.468245+00:00_

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
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-21T01:17:46.493258+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"}]

I performed the web search with your query, but the results returned information about various ACL 2026 conferences and workshops (EACL 2026, ACL 2026, LAW 2026, etc.) rather than specifically for EMN
…[truncated 748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5633
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-21T01:17:49.662231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR cycle"
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
    "query": "EMNLP 2026 call for papers submission deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-21T01:17:50.164660+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 1426 · 2026-05-21T01:17:56.197788+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is the information about EMNLP 2026 call for papers submission deadline for the ARR cycle:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Key ARR C
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6535
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-21T01:17:59.771995+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines for page limit and format requirements:

## Page Limits

Short papers: 4 content pages maximum, Long papers: 8 content pages maximum. Sections on ethical considerations and limitations do not count towards page limit. Additionally, review versions of long papers may have up to eight (8) pages of content plus unlimited pages for ref
…[truncated 837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 9607
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-21T01:18:09.682170+00:00_

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

_source line 1429 · 2026-05-21T01:18:09.682644+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-21T01:18:09.833573+00:00_

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

_source line 1431 · 2026-05-21T01:18:09.834132+00:00_

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
…[truncated 2507 chars]

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

_source line 1432 · 2026-05-21T01:18:09.985211+00:00_

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

_source line 1433 · 2026-05-21T01:18:10.186831+00:00_

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
…[truncated 9558 chars]

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

_source line 1434 · 2026-05-21T01:18:10.188013+00:00_

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

_source line 1435 · 2026-05-21T01:18:10.590996+00:00_

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
…[truncated 17504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-21T01:18:10.591556+00:00_

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

_source line 1437 · 2026-05-21T01:18:11.595838+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
16	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU 
…[truncated 4413 chars]

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

_source line 1438 · 2026-05-21T01:18:11.597226+00:00_

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

_source line 1439 · 2026-05-21T01:18:12.049380+00:00_

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
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-21T01:18:12.200488+00:00_

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

_source line 1441 · 2026-05-21T01:18:12.552605+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 10.76 but MMLU already degrades to 35.5\% (vs.\ 40.7\% at 30\%); 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B (3-seed), KL improves PPL ($-$17.3\%) and commonsense tasks (WG, HS, PIQA: all seeds win) but MMLU is tied (43.3\% vs.\ 43.5\%) and GSM8K reverses across all seeds (7.0--11.1\% vs.\ TEAL 15.9\%). ARC-c is seed-dependent (37.8--50.1\% vs.\ TEAL 41.1\%; $\sigma$=6.4pp vs.\ LLaMA-8B's 2.5pp), indicating reduced cross-architecture metric stability. Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$20pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 52.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Training data is domain-homogeneous: all predictors are trained on WikiText-103 (English Wikipedia), a single-domain corpus.
8	Activation importance patterns may differ on code, multilingual, or dialogue data; the predictor could underperform on domains with substantially different neuron utilization profiles.
9	Out-of-distribution evaluation on C4 (Appendix~\ref{app:oo
…[truncated 1919 chars]

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

_source line 1442 · 2026-05-21T01:18:12.553119+00:00_

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

_source line 1443 · 2026-05-21T01:18:12.754226+00:00_

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
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-21T01:18:12.754684+00:00_

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

_source line 1445 · 2026-05-21T01:18:13.006532+00:00_

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
…[truncated 28698 chars]

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

_source line 1446 · 2026-05-21T01:18:38.641065+00:00_

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

_source line 1447 · 2026-05-21T01:18:40.602667+00:00_

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


### Tool call

_source line 1448 · 2026-05-21T01:18:41.154982+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1449 · 2026-05-21T01:18:42.916191+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4275
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-21T01:18:43.673798+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 3071
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-21T01:18:43.674216+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 2519
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-21T01:18:46.488430+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
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
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-21T01:18:46.539083+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

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

_source line 1454 · 2026-05-21T01:18:48.899962+00:00_

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

_source line 1455 · 2026-05-21T01:18:48.951093+00:00_

1	issues:
2	  # ============================================================
3	  # Round 16 — Active issues
4	  # ============================================================
5	
6	  - id: "R16-N1"
7	    summary: "多种子覆盖不一致: headline result (50% KL global PPL 11.79) 为 single-seed, MSE baseline 全部 single-seed"
8	    category: experiment
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 16
12	    last_seen_round: 16
13	    mentions:
14	      - {round: 16, reviewers: [1, 2], note: "[AGREE] 共识. R1-N1 提出, R2 交叉回应完全同意. Table 2 headline 基于 s42 而非 3-seed mean."}
15	    action_items:
16	      - {round: 16, action: "Table 2 所有行补充完整 3-seed 统计; MSE baseline 至少补 2 个种子.", assigned_to: "research_director", status: in_progress}
17	      - {round: 16, action: "KL50 global 已更新为 3-seed (11.84±0.15). MSE s123 训练失败(D092), appendix 已披露 seed sensitivity.", assigned_to: "main_agent", status: in_progress}
18	    resolution: ""
19	    resolution_round: null
20	
21	  - id: "R16-N2"
22	    summary: "消融实验仅在 50% 稀疏度, 论文实际可用的 30% regime 缺消融覆盖"
23	    category: experiment
24	    severity: critical
25	    status: resolved
26	    first_raised_round: 16
27	    last_seen_round: 16
28	    mentions:
29	      - {round: 16, reviewers: [1, 2], note: "[AGREE] 共识. R1-N3 提出, R2 完全同意. Table 4 消融全在 50%, 但 50% downstream 崩溃, 30% loss function 选择效果未知."}
30	    action_items:
31	      - {round: 16, action: "补充 30% 稀疏度下 Forward KL/JSD/Reverse KL/STE 消融对比.", assigned_to: "research_director", status: resolved}
32	      - {round: 16, action: "30% 数据完整: KL=8.82, JSD=8.88, RevKL=9.31, MSE=20.43, BCE=15.71, STE excluded(D090). Table 4 已更新含双列(30%+50%). §4.5 已更新讨论.", assigned_to: "main_agent", status: resolved}
33	    resolution: "Table 4 现包含 30% 和 50% 双列消融. 所有 coupled losses (KL 8.82, JSD 8.88, RevKL 9.31) 远优于 decomposed losses (BCE 15.71, MSE 20.43), 30% regime 下 loss function 选择效果明确."
34	    resolution_round: 17
35	
36	  - id: "R16-N3"
37	    summary: "新颖性不足: 核心是标准 KL distillation 直接应用于 SwiGLU 
…[truncated 9958 chars]

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

_source line 1456 · 2026-05-21T01:19:38.955893+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的侧重：方法严谨性 + 实验验证\n\n重点审查以下方面：\n1. **Claims vs Evidence 对齐**：论文声称的每个结论是否有充分的实验证据支持？特别关注 abstract 和 conclusion 中的 headline claims。\n2. **实验设计**：baseline 选择是否公平？控制变量是否合理？是否遗漏了关键对比？\n3. **统计严格性**：multi-seed 覆盖是否充分？哪些结果是 single-seed？标准差报告是否完整？\n4. **消融完整性**：每个设计选择是否都有消融支持？是否存在未被消融覆盖的关键决策？\n5. **数据核查**：表格中的数字是否自洽？正文引用与表格数据是否一致？\n6. **方法严谨性**：Gumbel-Sigmoid relaxation、adaptive penalty controller、KL 方向选择的论证是否严密？\n\n### Venue 信息\n- **EMNLP 2026**, ARR May cycle, deadline 2026-05-25\n- Long Paper: 正文 ≤8 页, 参考文献无限制\n- Limitations 和 Ethics 不计入页数\n- ACL 模板, double-blind\n- Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n### 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 论文摘要\n论文提出用 KL divergence（而非 BCE）训练 SwiGLU LLM 的稀疏预测器。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 产生更低的 perplexity。Target-swap ablation (C1) 确认 mask quality 驱动推理阶段质量。评估在 LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B 上进行。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条编号，S1/S2/...）\n3. **Weaknesses**（逐条编号，W1/W2/...，标注严重程度 [Critical/Major/Minor]）\n4. **Questions**（逐条编号，Q1/Q2/...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
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
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的侧重：方法严谨性 + 实验验证\n\n重点审查以下方面：\n1. **Claims vs Evidence 对齐**：论文声称的每个结论是否有充分的实验证据支持？特别关注 abstract 和 conclusion 中的 headline claims。\n2. **实验设计**：baseline 选择是否公平？控制变量是否合理？是否遗漏了关键对比？\n3. **统计严格性**：multi-seed 覆盖是否充分？哪些结果是 single-seed？标准差报告是否完整？\n4. **消融完整性**：每个设计选择是否都有消融支持？是否存在未被消融覆盖的关键决策？\n5. **数据核查**：表格中的数字是否自洽？正文引用与表格数据是否一致？\n6. **方法严谨性**：Gumbel-Sigmoid relaxation、adaptive penalty controller、KL 方向选择的论证是否严密？\n\n### Venue 信息\n- **EMNLP 2026**, ARR May cycle, deadline 2026-05-25\n- Long Paper: 正文 ≤8 页, 参考文献无限制\n- Limitations 和 Ethics 不计入页数\n- ACL 模板, double-blind\n- Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n### 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 论文摘要\n论文提出用 KL divergence（而非 BCE）训练 SwiGLU LLM 的稀疏预测器。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 产生更低的 perplexity。Target-swap ablation (C1) 确认 mask quality 驱动推理阶段质量。评估在 LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B 上进行。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条编号，S1/S2/...）\n3. **Weaknesses**（逐条编号，W1/W2/...，标注严重程度 [Critical/Major/Minor]）\n4. **Questions**（逐条编号，Q1/Q2/...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-21T01:19:50.687605+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11731
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-21T01:19:50.839053+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的侧重：新颖性 + Related Work + 写作质量 + 格式合规\n\n重点审查以下方面：\n1. **新颖性评估**：核心贡献的技术新颖性如何？与 MaskLLM（同为 frozen weights + learnable masks + KL training）的区别是否足够？empirical contribution 是否达到 EMNLP main conference bar？\n2. **Related Work 完整性**：是否遗漏重要相关工作？与已有方法的定位是否准确？Taxonomy (Table 1) 的分类是否合理？\n3. **写作质量**：论文结构是否清晰？核心 narrative 是否有说服力？是否存在过度声称或措辞不当？Abstract/Introduction 的 framing 是否准确反映实验发现？\n4. **格式合规**：是否符合 EMNLP 2026 / ARR 格式要求（8 页正文、ACL 模板、匿名性、引用格式）？\n5. **贡献清晰度**：4 个 contributions 的 claim 是否清晰、可验证、有意义？\n6. **Limitations 和 Ethics**：是否充分讨论？是否遗漏重要 limitations？\n\n### Venue 信息\n- **EMNLP 2026**, ARR May cycle, deadline 2026-05-25\n- Long Paper: 正文 ≤8 页, 参考文献无限制\n- Limitations 和 Ethics 不计入页数\n- ACL 模板, double-blind\n- Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n### 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 论文摘要\n论文提出用 KL divergence（而非 BCE）训练 SwiGLU LLM 的稀疏预测器。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 产生更低的 perplexity。Target-swap ablation (C1) 确认 mask quality 驱动推理阶段质量。评估在 LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B 上进行。论文自定位为 \"primarily empirical study\"。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条编号，S1/S2/...）\n3. **Weaknesses**（逐条编号，W1/W2/...，标注严重程度 [Critical/Major/Minor]）\n4. **Questions**（逐条编号，Q1/Q2/...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
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
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的侧重：新颖性 + Related Work + 写作质量 + 格式合规\n\n重点审查以下方面：\n1. **新颖性评估**：核心贡献的技术新颖性如何？与 MaskLLM（同为 frozen weights + learnable masks + KL training）的区别是否足够？empirical contribution 是否达到 EMNLP main conference bar？\n2. **Related Work 完整性**：是否遗漏重要相关工作？与已有方法的定位是否准确？Taxonomy (Table 1) 的分类是否合理？\n3. **写作质量**：论文结构是否清晰？核心 narrative 是否有说服力？是否存在过度声称或措辞不当？Abstract/Introduction 的 framing 是否准确反映实验发现？\n4. **格式合规**：是否符合 EMNLP 2026 / ARR 格式要求（8 页正文、ACL 模板、匿名性、引用格式）？\n5. **贡献清晰度**：4 个 contributions 的 claim 是否清晰、可验证、有意义？\n6. **Limitations 和 Ethics**：是否充分讨论？是否遗漏重要 limitations？\n\n### Venue 信息\n- **EMNLP 2026**, ARR May cycle, deadline 2026-05-25\n- Long Paper: 正文 ≤8 页, 参考文献无限制\n- Limitations 和 Ethics 不计入页数\n- ACL 模板, double-blind\n- Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n### 论文路径\n- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`\n\n### 论文摘要\n论文提出用 KL divergence（而非 BCE）训练 SwiGLU LLM 的稀疏预测器。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 产生更低的 perplexity。Target-swap ablation (C1) 确认 mask quality 驱动推理阶段质量。评估在 LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B 上进行。论文自定位为 \"primarily empirical study\"。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条编号，S1/S2/...）\n3. **Weaknesses**（逐条编号，W1/W2/...，标注严重程度 [Critical/Major/Minor]）\n4. **Questions**（逐条编号，Q1/Q2/...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-21T01:19:52.460198+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1621
}
```

</details>

---


### Assistant

_source line 1460 · 2026-05-21T01:20:09.571188+00:00_

**Round 1 已启动。** 两位 Reviewer 已收到审稿任务，正在独立审稿中。

当前状态：
- Reviewer 1（方法严谨性 + 实验验证）：审稿中
- Reviewer 2（新颖性 + Related Work + 写作 + 格式）：审稿中
- 视觉审查 Agent：已派发，并行执行中
- 外部审稿（Stanford Agentic Reviewer）：请求已发送，等待用户协助提交

等待 Reviewer 返回审稿意见后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1461 · 2026-05-21T01:25:57.359723+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

### 审稿侧重：方法严谨性 + 实验验证

---

### 1. Summary

本文提出用前向 KL 散度（替代 BCE）训练 SwiGLU LLM 的稀疏性预测器，配合 Gumbel-Sigmoid 松弛和自适应惩罚控制器。核心发现是 KL 的端到端耦合梯度发现了与 magnitude-based masks 偏离 46–68% 的 mask patterns，且这些 patterns 通过 target-swap ablation (C1) 被确认为推理阶段质量的近端驱动因素。实验在 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B 上进行，展示了一致的 PPL 改进但不一致的下游任务表现。

### 2. Strengths

**S1. C1 Target-swap ablation 设计精巧且有说服力。** Table 3 (§4.4) 通过将 KL 发现的 oracle masks 喂给标准 BCE predictor，成功解耦了 mask quality 与 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp（s42），30% 下多 seed 一致性 ≤1.70pp，提供了 mask quality 是推理质量近端驱动因素的有力证据。

**S2. 消融覆盖面广且系统性强。** Table 4 系统对比了 divergence 类型（forward KL vs JSD vs reverse KL）、松弛方法（Gumbel vs STE）、loss function isolation（BCE+Gumbel vs BCE plain），Appendix 补充了 bottleneck sensitivity (Table 7)、temperature schedule (Table 8)、training convergence (Table 9)。

**S3. 诚实的结果报告。** 论文明确报告了 KL 在 knowledge-intensive tasks 上的劣势（MMLU 40.7% vs TEAL 45.9%，Table 2；Qwen-14B GSM8K −20pp），50% 下游的 capacity cliff，以及跨架构的不一致性。

**S4. 二维 taxonomy 有组织价值。** Table 1 沿 correction granularity × training signal coupling 两个轴清晰组织先前工作。

**S5. Multi-seed 评估覆盖了关键结果。** 主要结论均为 3-seed 评估并报告标准差。

### 3. Weaknesses

**W1. [Critical] 无实际推理加速，动机与贡献脱节。** 论文的动机是推理效率，但 Appendix A (Table 6) 显示 KL pipeline 增加 6.4% 延迟开销，实际 wallclock 无加速。论文承认 "net acceleration requires kernel-level sparse computation optimizations...beyond the scope of this work"。在 activation sparsity 领域，若不能展示端到端加速，贡献主要停留在 prediction quality 的学术分析层面。建议至少提供 Triton block-sparse 的 prototype 实测数据，或将 framing 完全转向 "understanding training objectives for sparsity prediction"。

**W2. [Major] MMLU/GSM8K 上的系统性劣势削弱了 "quality improvement" claim 的覆盖面。** Abstract 强调 PPL 和 commonsense reasoning 改进，但 MMLU 从 45.9% 降至 40.7%（−5.2pp），在 Qwen-14B 上 GSM8K −20pp。所有三个模型上，knowledge-intensive tasks 均无改进或退步。论文将 forward KL 的 mode-covering 特性作为假设性解释（§4.2），但缺少实验验证。

**W3. [Major] 主要对比中 actual sparsity 不匹配未被充分解决。** Table 2 中 KL 30% actual=28.5%，TEAL 30% actual=29.3%。0.8pp 差异意味着 KL 保留了更多神经元。虽然正文提供了 matched sparsity 比较（14.5% at 28.5%），但 Table 2 的 headline 比较仍在不同 actual sparsity 下进行。建议在 Table 2 中增加 TEAL at 28.5% 的行。

**W4. [Major] MSE baseline 的单 seed 报告掩盖了高方差。** Appendix G 承认 MSE with seed 123 仅达到 5.1% sparsity（PPL=15,789），是 "failure mode"。但 Table 2/4 中 MSE 均为 seed 42 单 seed。一个 seed 完全失败的情况下，单 seed 报告不能代表 MSE 方法的真实性能分布。

**W5. [Major] "Gradient coupling" vs "objective function" 的因果解释未被完全解耦。** KL 和 BCE 的关键区别不仅是梯度耦合程度，更根本的是 target 定义不同。MSE baseline 使用 L2 on hidden states，而非 per-layer KL on output distributions，因此 MSE 的失败可能源于 L2 loss 不适合而非 per-layer coupling 本身的局限。缺少关键实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence）。

**W6. [Minor] 14B scale 结果有限且令人担忧。** Qwen-14B 仅在 30% sparsity 下评估，KL 的 GSM8K 大幅退步（32.1±5.2% vs 52.1%），方法在 14B+ scale 的适用性存疑。

**W7. [Minor] 训练数据同质性。** 所有 predictor 在 WikiText-103 上训练。OOD 评估显示 C4 上 cross-seed variance 显著增大（CV=6.3% vs in-domain 0.2%）。

### 4. Questions

**Q1.** C1 的 s42 oracle 来自 "an earlier training run"，而 s123/s456 使用 "matched retrained oracles"。统一使用 matched oracles 后 s42 的 gap 是否会缩小？

**Q2.** 是否可以在 reverse KL predictor 上也报告下游 metrics，验证 mode-seeking 是否更好保留 knowledge pathways？

**Q3.** Table 2 没有 BCE 30% uniform 的条目。可否提供？Table 4 的 BCE 30% PPL=15.71 是 uniform 吗？

**Q4.** MSE seed 123 失败是 MSE + Gumbel-Sigmoid + Lagrangian 组合不稳定，还是 MSE 固有缺陷？KL 是否有类似失败？

**Q5.** KL 训练成本约 2.6× BCE，且每个 sparsity target 需单独训练，对实际部署意味着什么？

### 5. Missing References

- CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work 中提及但未实验比较。应与 TEAL 一起在 Table 2 中展示。
- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖。

### 6. Overall Assessment

**Overall: 3.5** (Borderline Conference) | **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**

本文是一篇执行质量较高的实证研究，C1 target-swap ablation 有创意，KL > BCE 的核心发现在 PPL 层面有充分支撑。三个核心短板：(1) 无实际推理加速削弱实用价值；(2) knowledge-intensive tasks 上系统性退步限制 quality improvement 主张覆盖面；(3) gradient coupling 的因果解释缺少 per-layer KL 关键对照实验。方法论新颖性有限，贡献主要在 empirical characterization。建议补充 per-layer KL ablation、MSE multi-seed、和至少一个 kernel-level speedup measurement。

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

_source line 1462 · 2026-05-21T01:26:05.297329+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1463 · 2026-05-21T01:26:08.101791+00:00_

[Reviewer 1 审稿结果]:
审稿意见已发送给 Review Director。

**审稿完成摘要：**

- **Overall: 3.5** (Borderline Conference)
- **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**

主要发现：
- **优势**：C1 target-swap ablation 设计精巧，消融覆盖全面，结果报告诚实
- **关键问题**：无实际推理加速（+6.4% overhead）、knowledge-intensive tasks 系统性退步（MMLU −5.2pp）、gradient coupling 因果解释缺少 per-layer KL 对照实验、MSE baseline 单 seed 掩盖高方差
- **建议补充**：per-layer KL ablation、MSE multi-seed、kernel-level speedup prototype

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

_source line 1464 · 2026-05-21T01:26:22.837553+00:00_

R1 审稿已收到，等待 R2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 121

## Round 121

6 recorded events


### User

_source line 1465 · 2026-05-21T01:26:22.847012+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**Venue**: EMNLP 2026 (ARR May cycle)

---

### 1. Summary

本文提出用 KL divergence（而非传统 BCE）训练轻量 MLP 预测器，为 SwiGLU LLM 的 FFN 层生成 input-dependent activation sparsity masks。核心发现是 KL 的耦合梯度（coupled gradients）发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 在 PPL 指标上持续优于 BCE 和 training-free baselines。通过 target-swap ablation (C1) 确认 mask quality（而非训练 objective 本身）驱动推理质量。评估覆盖 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B，论文自定位为 "primarily empirical study"。

---

### 2. Strengths

**S1. C1 Target-Swap Ablation 设计精巧** — Table 3 (p7) 的 target-swap ablation 是本文最有价值的贡献。通过让 BCE predictor 在推理时使用 KL-derived oracle masks（反之亦然），干净地隔离了 mask quality 与 training objective 的效果。这一实验设计在该领域中较为少见，为 "mask quality drives inference-stage quality" 提供了有说服力的因果证据。

**S2. 实验覆盖全面，附录详尽** — 17 个 Appendix sections 覆盖 bottleneck 敏感性（App B）、OOD 评估（App D）、per-layer retention（App E）、training stability（App F）、MSE baseline（App G）、SNR 分析（App H）等。这种实验透彻度超过了同领域大多数工作，读者能在附录中找到几乎所有合理的 follow-up 问题的回答。

**S3. 诚实的自我定位** — 论文明确声明 "This paper is primarily an empirical study: we do not propose a new architecture or algorithms"（p2），这种诚实的 framing 降低了读者的期望校准成本，也使贡献评估更公正。

**S4. Taxonomy 有组织价值** — Table 1 (p5) 沿 signal coupling（BCE/intermediate/coupled KL）和 granularity（per-token vs per-layer）两个维度组织了现有工作，提供了清晰的定位参照。

**S5. 多架构验证** — 在 3 个模型家族（7B-14B）上评估，包括 cross-architecture 分析（Table 16-17, Appendix N），结论不依赖单一模型。

---

### 3. Weaknesses

**W1 [Major] — 与 MaskLLM 的方法论区分不足，novelty 有限**

核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 Section 2 (p3) 声称三点区别：(1) activation sparsity vs N:M weight sparsity, (2) dynamic per-token masks vs static masks, (3) predictor network vs directly learnable mask parameters。但这三点均为 **application-level differences**（目标不同），而非 **methodological innovation**（训练方法不同）。

关键问题：如果将 MaskLLM 的 KL+Gumbel 训练策略直接迁移到 activation sparsity 场景（只需把 learnable mask parameters 替换为 predictor network 输出），是否就能复现本文的核心结果？论文未讨论这一 counterfactual，这使得"本文的贡献是什么"变得模糊——是发现 KL 对 activation sparsity 也有效（confirmatory），还是提出了新的训练技术（innovative）？

作为 "primarily empirical study"，此 novelty 水平可能达到 Findings bar，但对 main conference 而言，缺乏方法论或理论层面的新颖贡献是主要短板。

**W2 [Major] — Downstream task 结果不一致，削弱核心 claim 的实用价值**

Table 2 (p6) 显示 KL predictor 在 commonsense reasoning (ARC-c, WG, HellaSwag) 上优于 TEAL，但在 knowledge-intensive benchmarks 上表现不佳：
- MMLU: KL 40.73 vs TEAL 45（30% sparsity），差距显著（-4.27pp）
- PIQA: 所有方法均大幅低于 dense baseline

Table 2 同时显示 uniform allocation 在多数下游任务上表现接近 global allocation（有时更好），这暗示 allocation strategy 对下游任务的影响可能被高估。

论文在 Section 4.6 (p8) 承认 "PPL gains reveal task- and scale-dependent effects" 但未充分解释这种不一致性。如果 KL-discovered masks 确实更优，为什么只在 PPL 和部分 reasoning tasks 上体现？这是 mask quality 问题还是 evaluation metric 选择问题？这一 gap 需要更严谨的分析。

**W3 [Major] — "Gradient coupling" narrative 缺乏严格支撑**

Section 3.6 (p5) 的梯度分析是论文的核心叙事支柱，但分析层次停留在直觉性描述：
- "KL introduces a downstream Jacobian ∂P_dense/∂h_l that couples each neuron j's gradient to all other retained neurons in layers l' through L"（p5）— 这个 observation 对任何 output-level loss 都成立（包括 MSE），并非 KL 的独特性质
- Gradient SNR measurements（Figure 5, Appendix H）显示 BCE 在训练早期有更高 SNR，而 KL 后来超越——但这可能是不同 loss landscape 的 artifact，而非 "coupling" 的因果效应
- 论文未提供形式化的理论分析来证明 coupled gradients → better masks 这一因果链条

将这一机制称为 "gradient coupling discovers mask patterns" 是 overclaiming——更准确的描述应该是 "output-level KL optimization empirically finds different masks than per-neuron BCE"。

**W4 [Minor] — Wall-clock speedup 缺失降低实用性论证**

论文在 Limitations (p9) 承认 "actual wall-clock acceleration depends on sparse kernel implementations"，但 Appendix A (p12) 的推理效率分析仅估算 FLOPs 减少（30% sparsity 节省 ~21% latency）。对于声称改进 inference efficiency 的工作，至少应提供 simulated 或 rough wall-clock measurements。特别是论文使用 unstructured element-wise masks (p13)，这在现有硬件上通常无法转化为实际加速。

**W5 [Minor] — Abstract 信息密度过高，关键 claim 的表述需要推敲**

Abstract 在 ~200 词中塞入了过多具体数字（46-68%、14.5%、PPL 数值、5 个 downstream benchmarks 等），反而模糊了核心 message。建议突出 1-2 个最关键的定量发现。

此外，"coupled gradient discovers mask patterns" 和 "mask pattern discovery" 等表述暗示了一种 emergent discovery 的叙事，但实际上这些 patterns 是通过标准优化过程产生的。这种措辞有 overclaiming 之嫌。

**W6 [Minor] — 训练数据单一性**

所有实验仅在 WikiText-103 上训练 1000 steps。虽然 Appendix D (p14) 提供了 C4 上的 OOD 评估，但未探讨在更多样化的训练数据上（如 OpenWebText、RedPajama subsets）mask patterns 是否一致。对于声称发现 "general" mask patterns 的工作，单一训练语料是一个值得注意的局限。

---

### 4. Questions

**Q1**: 如果让 MaskLLM 的训练策略（directly learnable mask parameters + KL + Gumbel-Softmax）直接应用于 per-token activation sparsity prediction（每个 token 有独立 mask），结果是否与本文的 predictor-based 方法可比？这个 baseline 对于确立 predictor architecture 的必要性至关重要。

**Q2**: KL-derived masks 在不同 random seeds 之间的 Jaccard divergence 是多少？如果 seed-to-seed 变异也达到 40-60%，那么 "KL masks diverge 46-68% from magnitude masks" 这个数字的信息量就大打折扣。Appendix F (p14-15) 报告了 PPL 的 seed stability（CV=0.6%），但未报告 mask pattern 的 seed stability。

**Q3**: Section 3.6 (p5) 声称 "coupled gradients discover mask targets that yield lower perplexity, with mask quality driving inference-stage quality"。但 MSE 也是 output-level objective（虽然作用在 hidden states 而非 output distribution），为什么 MSE 的表现反而不如 TEAL（Appendix G, p15）？这似乎与 "output-level coupling is the key" 的叙事矛盾。

**Q4**: Table 4 (p7) 的 ablation 中，"Forward KL + Coupled (ours)" 与 "BCE + STE" 的差距在 50% sparsity 时仅为 PPL 11.79 vs 12.20——这个差距（0.41 PPL points）在 downstream tasks 上是否有统计显著性？

**Q5**: Appendix A (p12) 的 inference 延迟估算基于 RTX PRO 6000 单 GPU。对于 14B 模型（Qwen-2.5-14B），实际部署通常需要多 GPU——predictor overhead 在多 GPU 场景下是否会成为瓶颈？

---

### 5. Missing References

以下工作与本文直接相关但未被讨论：

- **Mixture-of-Channels (MoC)** (arxiv 2511.09323, Nov 2025)：利用 SwiGLU 的 native gating mechanism 进行 Top-K channel selection，与本文在 SwiGLU gate sparsity 的问题域高度重合，应在 Related Work 中讨论。
- **"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering"** (arxiv 2507.14179, Jul 2025)：通过聚类 activation patterns 进行 sparsity prediction，是一种不同于 predictor network 的替代方案。

---

### 6. 格式合规检查

- **页数**: 正文（Abstract 到 Conclusion）8 页，Limitations + Ethics 从 p8 底部开始，References 从 p10 开始。✅ 符合 8 页限制。
- **模板**: ACL 格式，双栏排版。✅
- **匿名性**: "Anonymous ACL submission"。✅ 未发现明显匿名性违规。
- **Limitations**: 有独立 Limitations section (p8-9)，讨论了 model scale 限制、PPL 作为 proxy 的局限、wall-clock speedup 未实现。✅
- **Ethics Statement**: 有独立 Ethics Statement (p9)。✅
- **Responsible NLP Checklist**: 包含完整 checklist (p9-10)。✅
- **引用格式**: 使用 `\cite` 和 `\citealp`，格式一致。✅
- **引用验证**: 50 条引用全部通过 OpenAlex 验证（44 verified, 5 minor mismatches in author name format, 1 orphan bib entry `de2024griffin` not cited）。✅ 无虚假引用。

---

### 7. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 核心 PPL claims 有充分实验支持，C1 ablation 设计严谨。但 gradient coupling 分析缺乏形式化证明，downstream results 不一致性未充分解释。 |
| **Excitement** | 2.5/5 | 方法论 novelty 有限（KL→BCE 替换 + empirical analysis），但 C1 ablation 的实验设计有方法论贡献。对 activation sparsity 社区有参考价值，但不太可能改变该领域的研究方向。 |
| **Reproducibility** | 4/5 | 架构、超参数、训练细节描述详尽（Section 4.1, Appendix B-C）。代码未发布但描述足够重现。唯一扣分：部分 downstream evaluation 细节需参考 TEAL 原文。 |
| **Datasets** | 1/5 | 未发布新数据集。 |
| **Software** | 1/5 | 未发布代码。 |

---

### 8. Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5** — 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文及附录。

**一句话总评**: 一项执行扎实的 empirical study，C1 target-swap ablation 有独立价值，但核心方法论贡献有限（KL 替代 BCE 是增量改进），downstream results 的不一致性和 gradient coupling 叙事缺乏严格支撑使其更适合 Findings 而非 main conference。

**升档路径（→3.5 Borderline Conference）**: (1) 形式化 gradient coupling 分析，提供 KL vs BCE gradient structure 的理论保证；(2) 解释 downstream task inconsistency 的 root cause 并提供额外实验；(3) 提供至少 proof-of-concept 的 wall-clock speedup 数据。

**降档风险（→2.5 Borderline Findings）**: 如果 Q1（MaskLLM 策略直接迁移）的结果表明 predictor architecture 并非必要，或 Q2（seed-level mask divergence）表明 46-68% 的数字不具信息量，则核心 claims 将被显著削弱。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **Overall 3.0 (Findings)**，主要问题：
1. **[Major]** 与 MaskLLM 方法论高度重合，novelty 有限——核心是 "KL 替代 BCE" 的增量改进
2. **[Major]** Downstream task 结果不一致（MMLU 差 4.27pp），削弱实用价值论证
3. **[Major]** "Gradient coupling" 叙事缺乏形式化支撑，存在 overclaiming
4. **[Minor]** 无 wall-clock speedup、训练数据单一、abstract 过度密集

主要优势：C1 target-swap ablation 设计精巧（S1）、实验覆盖极其全面（S2, 17 个 Appendix）、诚实自我定位（S3）。格式完全合规，引用全部验证通过。

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

_source line 1466 · 2026-05-21T01:27:26.921534+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文提出用前向 KL 散度（替代 BCE）训练 SwiGLU LLM 的稀疏性预测器，配合 Gumbel-Sigmoid 松弛和自适应惩罚控制器。核心发现是 KL 的端到端耦合梯度发现了与 magnitude-based masks 偏离 46–68% 的 mask patterns，且这些 patterns 通过 target-swap ablation (C1) 被确认为推理阶段质量的近端驱动因素。实验在 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B 上进行，展示了一致的 PPL 改进但不一致的下游任务表现。\n\n### Strengths\n**S1.** C1 Target-swap ablation 设计精巧且有说服力。\n**S2.** 消融覆盖面广且系统性强。\n**S3.** 诚实的结果报告。\n**S4.** 二维 taxonomy 有组织价值。\n**S5.** Multi-seed 评估覆盖了关键结果。\n\n### Weaknesses\n**W1. [Critical] 无实际推理加速，动机与贡献脱节。** 论文的动机是推理效率，但 Appendix A (Table 6) 显示 KL pipeline 增加 6.4% 延迟开销，实际 wallclock 无加速。论文承认 \"net acceleration requires kernel-level sparse computation optimizations...beyond the scope of this work\"。在 activation sparsity 领域，若不能展示端到端加速，贡献主要停留在 prediction quality 的学术分析层面。建议至少提供 Triton block-sparse 的 prototype 实测数据，或将 framing 完全转向 \"understanding training objectives for sparsity prediction\"。\n\n**W2. [Major] MMLU/GSM8K 上的系统性劣势削弱了 \"quality improvement\" claim 的覆盖面。** Abstract 强调 PPL 和 commonsense reasoning 改进，但 MMLU 从 45.9% 降至 40.7%（−5.2pp），在 Qwen-14B 上 GSM8K −20pp。所有三个模型上，knowledge-intensive tasks 均无改进或退步。论文将 forward KL 的 mode-covering 特性作为假设性解释（§4.2），但缺少实验验证。\n\n**W3. [Major] 主要对比中 actual sparsity 不匹配未被充分解决。** Table 2 中 KL 30% actual=28.5%，TEAL 30% actual=29.3%。0.8pp 差异意味着 KL 保留了更多神经元。虽然正文提供了 matched sparsity 比较（14.5% at 28.5%），但 Table 2 的 headline 比较仍在不同 actual sparsity 下进行。建议在 Table 2 中增加 TEAL at 28.5% 的行。\n\n**W4. [Major] MSE baseline 的单 seed 报告掩盖了高方差。** Appendix G 承认 MSE with seed 123 仅达到 5.1% sparsity（PPL=15,789），是 \"failure mode\"。但 Table 2/4 中 MSE 均为 seed 42 单 seed。一个 seed 完全失败的情况下，单 seed 报告不能代表 MSE 方法的真实性能分布。\n\n**W5. [Major] \"Gradient coupling\" vs \"objective function\" 的因果解释未被完全解耦。** KL 和 BCE 的关键区别不仅是梯度耦合程度，更根本的是 target 定义不同。MSE baseline 使用 L2 on hidden states，而非 per-layer KL on output distributions，因此 MSE 的失败可能源于 L2 loss 不适合而非 per-layer coupling 本身的局限。缺少关键实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence）。\n\n**W6. [Minor] 14B scale 结果有限且令人担忧。** Qwen-14B 仅在 30% sparsity 下评估，KL 的 GSM8K 大幅退步（32.1±5.2% vs 52.1%），方法在 14B+ scale 的适用性存疑。\n\n**W7. [Minor] 训练数据同质性。** 所有 predictor 在 WikiText-103 上训练。OOD 评估显示 C4 上 cross-seed variance 显著增大（CV=6.3% vs in-domain 0.2%）。\n\n### Questions\n**Q1.** C1 的 s42 oracle 来自 \"an earlier training run\"，而 s123/s456 使用 \"matched retrained oracles\"。统一使用 matched oracles 后 s42 的 gap 是否会缩小？\n**Q2.** 是否可以在 reverse KL predictor 上也报告下游 metrics，验证 mode-seeking 是否更好保留 knowledge pathways？\n**Q3.** Table 2 没有 BCE 30% uniform 的条目。可否提供？Table 4 的 BCE 30% PPL=15.71 是 uniform 吗？\n**Q4.** MSE seed 123 失败是 MSE + Gumbel-Sigmoid + Lagrangian 组合不稳定，还是 MSE 固有缺陷？KL 是否有类似失败？\n**Q5.** KL 训练成本约 2.6× BCE，且每个 sparsity target 需单独训练，对实际部署意味着什么？\n\n### Missing References\n- CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work 中提及但未实验比较。\n- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖。\n\n### Overall Assessment\n**Overall: 3.5** (Borderline Conference) | **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**"
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
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文提出用前向 KL 散度（替代 BCE）训练 SwiGLU LLM 的稀疏性预测器，配合 Gumbel-Sigmoid 松弛和自适应惩罚控制器。核心发现是 KL 的端到端耦合梯度发现了与 magnitude-based masks 偏离 46–68% 的 mask patterns，且这些 patterns 通过 target-swap ablation (C1) 被确认为推理阶段质量的近端驱动因素。实验在 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B 上进行，展示了一致的 PPL 改进但不一致的下游任务表现。\n\n### Strengths\n**S1.** C1 Target-swap ablation 设计精巧且有说服力。\n**S2.** 消融覆盖面广且系统性强。\n**S3.** 诚实的结果报告。\n**S4.** 二维 taxonomy 有组织价值。\n**S5.** Multi-seed 评估覆盖了关键结果。\n\n### Weaknesses\n**W1. [Critical] 无实际推理加速，动机与贡献脱节。** 论文的动机是推理效率，但 Appendix A (Table 6) 显示 KL pipeline 增加 6.4% 延迟开销，实际 wallclock 无加速。论文承认 \"net acceleration requires kernel-level sparse computation optimizations...beyond the scope of this work\"。在 activation sparsity 领域，若不能展示端到端加速，贡献主要停留在 prediction quality 的学术分析层面。建议至少提供 Triton block-sparse 的 prototype 实测数据，或将 framing 完全转向 \"understanding training objectives for sparsity prediction\"。\n\n**W2. [Major] MMLU/GSM8K 上的系统性劣势削弱了 \"quality improvement\" claim 的覆盖面。** Abstract 强调 PPL 和 commonsense reasoning 改进，但 MMLU 从 45.9% 降至 40.7%（−5.2pp），在 Qwen-14B 上 GSM8K −20pp。所有三个模型上，knowledge-intensive tasks 均无改进或退步。论文将 forward KL 的 mode-covering 特性作为假设性解释（§4.2），但缺少实验验证。\n\n**W3. [Major] 主要对比中 actual sparsity 不匹配未被充分解决。** Table 2 中 KL 30% actual=28.5%，TEAL 30% actual=29.3%。0.8pp 差异意味着 KL 保留了更多神经元。虽然正文提供了 matched sparsity 比较（14.5% at 28.5%），但 Table 2 的 headline 比较仍在不同 actual sparsity 下进行。建议在 Table 2 中增加 TEAL at 28.5% 的行。\n\n**W4. [Major] MSE baseline 的单 seed 报告掩盖了高方差。** Appendix G 承认 MSE with seed 123 仅达到 5.1% sparsity（PPL=15,789），是 \"failure mode\"。但 Table 2/4 中 MSE 均为 seed 42 单 seed。一个 seed 完全失败的情况下，单 seed 报告不能代表 MSE 方法的真实性能分布。\n\n**W5. [Major] \"Gradient coupling\" vs \"objective function\" 的因果解释未被完全解耦。** KL 和 BCE 的关键区别不仅是梯度耦合程度，更根本的是 target 定义不同。MSE baseline 使用 L2 on hidden states，而非 per-layer KL on output distributions，因此 MSE 的失败可能源于 L2 loss 不适合而非 per-layer coupling 本身的局限。缺少关键实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence）。\n\n**W6. [Minor] 14B scale 结果有限且令人担忧。** Qwen-14B 仅在 30% sparsity 下评估，KL 的 GSM8K 大幅退步（32.1±5.2% vs 52.1%），方法在 14B+ scale 的适用性存疑。\n\n**W7. [Minor] 训练数据同质性。** 所有 predictor 在 WikiText-103 上训练。OOD 评估显示 C4 上 cross-seed variance 显著增大（CV=6.3% vs in-domain 0.2%）。\n\n### Questions\n**Q1.** C1 的 s42 oracle 来自 \"an earlier training run\"，而 s123/s456 使用 \"matched retrained oracles\"。统一使用 matched oracles 后 s42 的 gap 是否会缩小？\n**Q2.** 是否可以在 reverse KL predictor 上也报告下游 metrics，验证 mode-seeking 是否更好保留 knowledge pathways？\n**Q3.** Table 2 没有 BCE 30% uniform 的条目。可否提供？Table 4 的 BCE 30% PPL=15.71 是 uniform 吗？\n**Q4.** MSE seed 123 失败是 MSE + Gumbel-Sigmoid + Lagrangian 组合不稳定，还是 MSE 固有缺陷？KL 是否有类似失败？\n**Q5.** KL 训练成本约 2.6× BCE，且每个 sparsity target 需单独训练，对实际部署意味着什么？\n\n### Missing References\n- CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work 中提及但未实验比较。\n- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖。\n\n### Overall Assessment\n**Overall: 3.5** (Borderline Conference) | **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-21T01:27:58.950221+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32028
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-21T01:27:59.452911+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文提出用 KL divergence（而非传统 BCE）训练轻量 MLP 预测器，为 SwiGLU LLM 的 FFN 层生成 input-dependent activation sparsity masks。核心发现是 KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，在 PPL 指标上持续优于 BCE 和 training-free baselines。通过 target-swap ablation (C1) 确认 mask quality 驱动推理质量。评估覆盖 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B，自定位为 \"primarily empirical study\"。\n\n### Strengths\n**S1.** C1 Target-Swap Ablation 设计精巧。\n**S2.** 实验覆盖全面，附录详尽（17 个 Appendix sections）。\n**S3.** 诚实的自我定位。\n**S4.** Taxonomy 有组织价值。\n**S5.** 多架构验证。\n\n### Weaknesses\n**W1 [Major] — 与 MaskLLM 的方法论区分不足，novelty 有限。** 核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM 高度重合。论文声称三点区别（activation vs weight sparsity, dynamic vs static masks, predictor vs learnable params），但这些均为 application-level differences，非 methodological innovation。作为 empirical study，可能达 Findings bar，但对 main conference 缺乏方法论或理论新颖贡献。\n\n**W2 [Major] — Downstream task 结果不一致，削弱核心 claim 的实用价值。** MMLU: KL 40.73 vs TEAL 45（−4.27pp at 30%）。论文在 §4.6 承认 task/scale-dependent effects 但未充分解释。如果 KL-discovered masks 更优，为何只在 PPL 和部分 reasoning tasks 上体现？\n\n**W3 [Major] — \"Gradient coupling\" narrative 缺乏严格支撑。** §3.6 分析停留在直觉描述。\"KL introduces a downstream Jacobian\" 对任何 output-level loss 都成立，非 KL 独特性质。Gradient SNR 可能是不同 loss landscape 的 artifact。将此称为 \"gradient coupling discovers mask patterns\" 是 overclaiming。\n\n**W4 [Minor] — Wall-clock speedup 缺失降低实用性论证。** 仅有 FLOPs 估算，无实际 wall-clock measurements。Unstructured masks 在现有硬件上通常无法转化为实际加速。\n\n**W5 [Minor] — Abstract 信息密度过高。** ~200 词塞入过多数字，模糊核心 message。\"coupled gradient discovers\" 等措辞有 overclaiming 之嫌。\n\n**W6 [Minor] — 训练数据单一性。** 仅 WikiText-103 训练。OOD C4 上 variance 增大。\n\n### Questions\n**Q1.** MaskLLM 的训练策略（directly learnable mask parameters + KL + Gumbel-Softmax）直接应用于 per-token activation sparsity prediction，结果是否与本文可比？\n**Q2.** KL-derived masks 在不同 random seeds 之间的 Jaccard divergence 是多少？如果 seed-to-seed 变异也达到 40-60%，46-68% 的数字信息量将大打折扣。\n**Q3.** MSE 也是 output-level objective（作用在 hidden states），为什么表现不如 TEAL？这与 \"output-level coupling is the key\" 叙事矛盾。\n**Q4.** Table 4 中 Forward KL+Coupled 与 BCE+STE 差距仅 0.41 PPL，downstream 上是否有统计显著性？\n**Q5.** 14B 模型多 GPU 部署时，predictor overhead 是否成为瓶颈？\n\n### Missing References\n- Mixture-of-Channels (MoC)：SwiGLU native gating + Top-K channel selection\n- \"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\"\n\n### 格式合规\n全部通过（页数✅、模板✅、匿名✅、Limitations✅、Ethics✅、Checklist✅、引用✅）\n\n### Overall Assessment\n**Overall: 3.0 (Findings)** | **Soundness: 3.5/5** | **Excitement: 2.5/5** | **Confidence: 4/5**\n\n升档路径（→3.5）: 形式化 gradient coupling 分析 + 解释 downstream inconsistency + proof-of-concept speedup。\n降档风险（→2.5）: MaskLLM 策略直接迁移可复现结果 或 seed-level mask divergence 高。"
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
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文提出用 KL divergence（而非传统 BCE）训练轻量 MLP 预测器，为 SwiGLU LLM 的 FFN 层生成 input-dependent activation sparsity masks。核心发现是 KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，在 PPL 指标上持续优于 BCE 和 training-free baselines。通过 target-swap ablation (C1) 确认 mask quality 驱动推理质量。评估覆盖 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B，自定位为 \"primarily empirical study\"。\n\n### Strengths\n**S1.** C1 Target-Swap Ablation 设计精巧。\n**S2.** 实验覆盖全面，附录详尽（17 个 Appendix sections）。\n**S3.** 诚实的自我定位。\n**S4.** Taxonomy 有组织价值。\n**S5.** 多架构验证。\n\n### Weaknesses\n**W1 [Major] — 与 MaskLLM 的方法论区分不足，novelty 有限。** 核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM 高度重合。论文声称三点区别（activation vs weight sparsity, dynamic vs static masks, predictor vs learnable params），但这些均为 application-level differences，非 methodological innovation。作为 empirical study，可能达 Findings bar，但对 main conference 缺乏方法论或理论新颖贡献。\n\n**W2 [Major] — Downstream task 结果不一致，削弱核心 claim 的实用价值。** MMLU: KL 40.73 vs TEAL 45（−4.27pp at 30%）。论文在 §4.6 承认 task/scale-dependent effects 但未充分解释。如果 KL-discovered masks 更优，为何只在 PPL 和部分 reasoning tasks 上体现？\n\n**W3 [Major] — \"Gradient coupling\" narrative 缺乏严格支撑。** §3.6 分析停留在直觉描述。\"KL introduces a downstream Jacobian\" 对任何 output-level loss 都成立，非 KL 独特性质。Gradient SNR 可能是不同 loss landscape 的 artifact。将此称为 \"gradient coupling discovers mask patterns\" 是 overclaiming。\n\n**W4 [Minor] — Wall-clock speedup 缺失降低实用性论证。** 仅有 FLOPs 估算，无实际 wall-clock measurements。Unstructured masks 在现有硬件上通常无法转化为实际加速。\n\n**W5 [Minor] — Abstract 信息密度过高。** ~200 词塞入过多数字，模糊核心 message。\"coupled gradient discovers\" 等措辞有 overclaiming 之嫌。\n\n**W6 [Minor] — 训练数据单一性。** 仅 WikiText-103 训练。OOD C4 上 variance 增大。\n\n### Questions\n**Q1.** MaskLLM 的训练策略（directly learnable mask parameters + KL + Gumbel-Softmax）直接应用于 per-token activation sparsity prediction，结果是否与本文可比？\n**Q2.** KL-derived masks 在不同 random seeds 之间的 Jaccard divergence 是多少？如果 seed-to-seed 变异也达到 40-60%，46-68% 的数字信息量将大打折扣。\n**Q3.** MSE 也是 output-level objective（作用在 hidden states），为什么表现不如 TEAL？这与 \"output-level coupling is the key\" 叙事矛盾。\n**Q4.** Table 4 中 Forward KL+Coupled 与 BCE+STE 差距仅 0.41 PPL，downstream 上是否有统计显著性？\n**Q5.** 14B 模型多 GPU 部署时，predictor overhead 是否成为瓶颈？\n\n### Missing References\n- Mixture-of-Channels (MoC)：SwiGLU native gating + Top-K channel selection\n- \"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\"\n\n### 格式合规\n全部通过（页数✅、模板✅、匿名✅、Limitations✅、Ethics✅、Checklist✅、引用✅）\n\n### Overall Assessment\n**Overall: 3.0 (Findings)** | **Soundness: 3.5/5** | **Excitement: 2.5/5** | **Confidence: 4/5**\n\n升档路径（→3.5）: 形式化 gradient coupling 分析 + 解释 downstream inconsistency + proof-of-concept speedup。\n降档风险（→2.5）: MaskLLM 策略直接迁移可复现结果 或 seed-level mask divergence 高。"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-21T01:28:00.963123+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 1470 · 2026-05-21T01:28:05.170366+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1471 · 2026-05-21T01:29:12.795658+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议

---

### Weaknesses 回应

**[AGREE] R1-W1: 无实际推理加速，动机与贡献脱节**

完全同意。这是本文最根本的张力所在。论文 Section 1 (p1) 开篇以 "SwiGLU feed-forward networks... exhibit high contextual sparsity" 和 "a large fraction of FFN neurons contribute negligibly to the output" 建立 efficiency 动机，但 Appendix A (Table 6, p12) 的实测数据显示 KL pipeline 反而增加 6.4% 延迟。更关键的是，论文在 p13 承认 "the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support"——这意味着即使 mask quality 确实更好，在可预见的部署场景中也无法兑现 efficiency 收益。

R1 提出的修复方案合理：要么提供 Triton block-sparse prototype，要么将 framing 完全转向 "understanding training objectives"。我倾向后者，因为这更符合论文的实际贡献。

**[AGREE] R1-W2: MMLU/GSM8K 系统性劣势**

完全同意，这与我的 W2 一致。补充一个额外观察：Table 2 (p6) 中不仅 MMLU 劣化（-5.2pp），且 KL 在 uniform allocation 下的 MMLU（40.7）与 global allocation（40.73）几乎无差异，暗示 allocation strategy 对 knowledge-intensive tasks 的影响远小于论文所强调的。这进一步表明 KL masks 可能系统性地丢失了某些 knowledge pathways，而非简单的 allocation 优化问题。

论文 Section 4.2 (p6) 将此归因于 forward KL 的 mode-covering property "preserves dense activation patterns that benefit broad commonsense inference"，但这只是假设性解释（"this may dilute task-specific knowledge pathways"），无实验验证。一个简单的验证方案：对比 KL vs BCE masks 在 MMLU-relevant layers（通常是中间层）的 retention pattern 差异。

**[AGREE] R1-W3: Actual sparsity 不匹配**

同意这是一个 presentation 问题。KL 30% actual=28.5% vs TEAL 30% actual=29.3% (Table 2, p6)，0.8pp 的差异虽然论文在正文中用 matched 比较进行了控制（"14.5% at 28.5%"），但 Table 2 作为主结果表在不同 actual sparsity 下对比确实容易误导。R1 建议增加 TEAL at 28.5% 行是低成本高收益的改进。

不过我要补充：这个问题对整体结论的影响有限。即使在 matched sparsity 下，KL 的 PPL 优势仍然存在（正文报告 "TEAL at 28.5% actual sparsity yields PPL ≈28.5, comparable to KL"——但这似乎与论文声称的 PPL 14.5% 改进矛盾，需要作者澄清具体数字）。

**[AGREE] R1-W4: MSE single-seed reporting**

强烈同意。这是我在初审中遗漏的重要问题。Appendix G (p15) 明确承认 "MSE with seed 123 only reaches 5.1% sparsity (PPL=15,789), indicating high sensitivity to initialization — a failure mode not observed with KL-based losses"。一个方法如果在 3 个 seed 中有 1 个完全失败（5.1% vs target 30%），那么用另一个 seed 的单次结果来代表该方法的性能是不公正的。

正确的做法应该是：(1) 报告 MSE 的 3-seed 均值和方差，包括 failed seed；(2) 或者明确排除 failed seed 并报告 2-seed 结果，同时将 seed sensitivity 作为 MSE 的 systematic weakness 讨论。当前的处理方式（只报 seed 42）有 cherry-picking 嫌疑，即使是无意的。

**[AGREE with nuance] R1-W5: Gradient coupling vs objective function 因果未解耦**

同意核心观点，但想补充更具体的分析。R1 指出的关键缺失实验 "per-layer KL"（每层独立优化该层 output 对 dense output 的 KL）是一个非常有价值的建议。当前论文的实验设计存在以下混淆变量：

| 方法 | Loss 类型 | 作用范围 | Signal 来源 |
|------|-----------|----------|------------|
| BCE | Per-neuron classification | 单层 | Magnitude-based oracle |
| MSE | L2 on hidden states | 单层 | Dense hidden states |
| KL (ours) | KL on output distribution | 端到端 | Dense output distribution |

三个维度同时变化（loss type × scope × signal source），无法判断哪个因素驱动了性能差异。R1 提出的 per-layer KL 实验可以固定 loss type=KL + signal source=output distribution，只改变 scope（per-layer vs end-to-end），从而真正隔离 "coupling" 的效果。

我在初审 W3 中也指出了类似问题（"gradient coupling 叙事缺乏严格支撑"），但 R1 的实验建议比我的批评更具建设性。

**[AGREE] R1-W6: 14B scale 结果有限**

同意。Qwen-14B 仅在 30% sparsity 下有结果，且 GSM8K 大幅退步（32.1±5.2% vs dense 52.1%，Table 17 推断）。这使得论文 Contribution 4（"Preliminary analysis of allocation-to-downstream interactions at 7-14B"）的 claim 基础薄弱。建议至少补充 50% sparsity 的 14B 结果以验证趋势是否一致。

**[AGREE] R1-W7: 训练数据同质性**

同意，与我的 W6 一致。补充：Appendix D (p14) 的 OOD 评估（C4 上 CV=6.3%）实际上暴露了更大的问题——cross-seed variance 增大 31× (0.2% → 6.3%) 意味着 predictor 对训练分布高度 overfit。论文应该讨论这种 distribution shift sensitivity 对实际部署的影响。

---

### Questions 回应

**[AGREE] R1-Q1: C1 oracle 来源不一致**

合理质疑。如果 s42 使用 "earlier training run" 的 oracle 而 s123/s456 使用 matched retrained oracles，那么 s42 的 gap 可能部分来自 oracle 质量差异而非 mask quality 差异。建议统一为 matched oracles 后重新评估。

**[AGREE] R1-Q2: Reverse KL downstream metrics**

非常好的建议。Table 4 (p7) 显示 Reverse KL + Coupled 在 30% 时 PPL=9.31，优于 BCE 但略逊于 Forward KL (8.82)。如果 reverse KL（mode-seeking）在 MMLU 等 knowledge-intensive tasks 上表现更好，这将支持 "forward KL 的 mode-covering 特性牺牲了 knowledge pathways" 的假设，也为 R1-W2 提供实验验证。

**[AGREE] R1-Q3: BCE 30% uniform 缺失**

Table 2 (p6) 确实缺少 BCE 30% uniform 的条目。Table 4 (p7) 的 "BCE composition" 行有 PPL=15.71，但标注为 "unified benchmark protocol; uniform allocation at 30%"（来自 Table 4 caption），需要作者确认是否一致。这个数据点对于完整对比是必要的。

**[AGREE] R1-Q4: MSE failure mode诊断**

重要问题。如果 MSE 的 seed 123 失败是 Gumbel-Sigmoid + Lagrangian 组合不稳定导致的（而非 MSE 固有缺陷），那么论文对 MSE 的 dismissal 就不成立——可能只需要调整超参数即可修复。KL 是否也有类似失败 seed 需要明确报告。Appendix F (p14-15) 报告 KL 的 3-seed CV=0.6%，看起来稳定，但没有报告是否存在 complete failure 的情况。

**[AGREE] R1-Q5: 训练成本 2.6× BCE**

实用性问题值得关注。每个 sparsity target 需独立训练意味着支持 30%/40%/50% 三个目标需要 3× 训练成本。在 KL 本身已是 BCE 2.6× 的前提下，总成本约 7.8× BCE。论文应讨论是否可以训练单个 predictor 支持多个 sparsity levels（如通过 conditional generation）。

---

### Missing References 回应

**[REBUT] R1-Missing-1: CATS 和 R-Sparse 未实验比较**

CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work (Section 2, p2-3) 中已被讨论并归入 Table 1 taxonomy。CATS 使用 per-layer adaptive thresholding（training-free），R-Sparse 使用 rank-aware selection。两者均为 training-free 方法，与本文的 trained predictor 不在同一 category。论文已将 TEAL 作为 training-free baselines 的代表进行实验比较，因为 TEAL 在该类别中表现最好。要求对每个 taxonomy 条目都进行实验比较会显著增加篇幅，且 TEAL 已经是 sufficient representative。

**[AGREE] R1-Missing-2: D2DMoE 未实验覆盖**

D2DMoE (Szatkowski et al., 2024) 作为 "intermediate (MSE) + per-token" 类别的代表出现在 Table 1 但无实验比较。由于论文的 Appendix G 已经测试了 MSE baseline（同类 loss function），D2DMoE 的缺失可以理解为实验设计选择。但如果 D2DMoE 的 per-token MSE 实现方式与论文的 MSE baseline 有本质差异，这个遗漏就更重要了。

---

### 总体评价差异讨论

R1 给出 **3.5 (Borderline Conference)**，我给出 **3.0 (Findings)**。0.5 分差距主要来自以下分歧：

1. **Novelty 权重**：我对 "KL 替代 BCE" 的增量性质给予更大 penalty（我的 W1），而 R1 更侧重 execution quality 和实用性问题（R1-W1 关注 speedup 缺失而非方法论新颖性）。

2. **C1 ablation 的价值评估**：R1 和我都认可 C1 的设计，但我认为一个 well-designed ablation 不能弥补核心方法论 novelty 的不足，而 R1 可能将其视为独立的方法论贡献。

3. **Downstream inconsistency 的严重性**：我和 R1 都标记了这个问题（我的 W2, R1-W2），但我将其视为对核心 claim 的更根本性威胁——如果 "better masks" 只在 PPL 上体现而不在 downstream 上一致改进，那么 "mask quality drives inference quality" 的 claim 的实用意义就大打折扣。

**结论**：综合 R1 的额外发现（特别是 W4 MSE single-seed、W5 因果未解耦），我维持 **Overall 3.0 (Findings)** 的评分。R1 提出的 W5 per-layer KL 实验如果结果支持 coupling hypothesis，可能将我的评分提升至 3.5。

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

_source line 1472 · 2026-05-21T01:29:18.398524+00:00_

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


## Round 123

## Round 123

2 recorded events


### User

_source line 1473 · 2026-05-21T01:29:21.035353+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。对 Reviewer 1 的 7 个 Weaknesses 全部 AGREE（W5 带 nuance），5 个 Questions 全部 AGREE，Missing References 中 1 个 REBUT（CATS/R-Sparse 已有 TEAL 作为代表）、1 个 AGREE（D2DMoE）。维持 Overall 3.0 (Findings) 评分，与 R1 的 3.5 有 0.5 分差距，主要分歧在方法论 novelty 的权重上。

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

_source line 1474 · 2026-05-21T01:29:28.286879+00:00_

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


## Round 124

## Round 124

10 recorded events


### User

_source line 1475 · 2026-05-21T01:30:30.252578+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Weaknesses 回应

**[AGREE] R2-W1: 与 MaskLLM 方法论区分不足。** 核心训练配方确实与 MaskLLM 高度重合。论文自承 "primarily an empirical study"（Introduction §1）。但 per-token dynamic masks + global top-k allocation 产生的长距离依赖使 C1 ablation 和 allocation analysis 成为可能，application-level differences 不完全 trivial。方法论新颖性有限，empirical contributions 达 Findings bar 无争议，能否达 Conference 取决于评判标准。

**[AGREE] R2-W2: Downstream inconsistency。** 完全同意，与我 R1-W2 一致。三个模型上 knowledge-intensive tasks 均系统性退步（Table 2 MMLU −5.2pp; Table 14 GSM8K −20pp），非边际效应。

**[REBUT] R2-W3: Gradient coupling narrative。** 部分同意 narrative 不够严格，但 R2 说 "任何 output-level loss 都成立" 不构成否定——论文的贡献在于实证量化效果。§3.6 已标注 "suggestive"，因果证据在 C1 ablation。缺少 per-layer KL ablation 是真实 gap（与我 R1-W5 一致），但不应将整个叙事归为 overclaiming。

**[REBUT] R2-W4: R2 称 "仅有 FLOPs 估算，无 wall-clock"——事实性错误。** Appendix A Table 6 有实际 wall-clock 测量（RTX PRO 6000, batch=1, seq=2048, fp16, 100 fwd passes）：Dense 119.11±0.57 ms, KL 126.78±0.31 ms。问题是 +6.4% overhead 而非加速，但数据确实存在。

**[AGREE] R2-W5, W6。** 同意。

### Questions 回应

**[REBUT] R2-Q1:** MaskLLM 的 directly learnable mask parameters 无法泛化到未见过的 input（activation sparsity 的核心要求）。最接近的对照是 Table 4 "BCE + Gumbel"（PPL 32.22 at 50%），远不如 KL (11.79)。

**[AGREE] R2-Q2: Seed-to-seed mask Jaccard 是关键缺口。** 如果 seed 间 mask divergence 也达 40-60%，46-68% 数字的信息量大打折扣。论文仅报告 PPL stability（CV=0.6%），未报告 mask-level 一致性。Appendix P 也承认这是 open question。我 R1 审稿遗漏了此点。

**[REBUT] R2-Q3: MSE 不是 output-level objective。** MSE 作用于 per-layer hidden states，非 model output logits（§3.7 明确说明，Appendix G 确认 loss target 为 per-layer FFN reconstruction）。MSE 是 intermediate-level objective（Table 1 中间列），其失败支持而非矛盾 "output-level coupling is key"。

**[REBUT] R2-Q4: 0.41 PPL 差距无法复现。** Table 4 实际数据：Forward KL 11.79 vs BCE+STE 60.54 (50%)，差距 48.75。30% 无 BCE+STE 数据。Forward KL vs Reverse KL at 30% = 0.49，Forward KL vs JSD at 30% = 0.06——无 0.41 对应。R2 可能存在数据引用错误。

**[AGREE] R2-Q5:** 14B 多 GPU predictor overhead 未讨论，Appendix A 仅覆盖单 GPU。

### 综合

R2 审稿质量较高，W1/W2/Q2 关切有力。但 W4 事实性错误、Q3 前提错误、Q4 数据无法复现。Overall 3.0 可能略低——考虑 C1 ablation 质量和消融覆盖面，维持 3.5 (Borderline Conference)。

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

_source line 1476 · 2026-05-21T01:31:00.923842+00:00_

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

_source line 1477 · 2026-05-21T01:31:01.325896+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T01:18:42.626214+00:00\", \"completed_at\": \"2026-05-21T01:18:47.436566+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets May 22, 6pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-21T01:31:01.326319+00:00_

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

_source line 1479 · 2026-05-21T01:31:01.428662+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T01:18:43.603642+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbbf8d2c695f1e79e11713aebc107790\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-21T01:33:28.705086+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 18 (fresh) — Active issues\n  # ============================================================\n\n  - id: \"R18-W1\"\n    summary: \"方法论新颖性有限: 核心 KL+Gumbel 训练配方与 MaskLLM 高度重合，区别仅在 application level\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2-W1 Major. 核心配方 (frozen backbone + learnable masks + KL + Gumbel) 与 MaskLLM 重合. 三点区别均为 application-level. 作为 empirical study 达 Findings bar, 但 main conference 需更多方法论贡献.\"}\n      - {round: 18, reviewers: [1], note: \"交叉回应: AGREE with nuance. Application differences 非完全 trivial (per-token + global top-k 产生长距离依赖), 但方法论新颖性确实有限.\"}\n    action_items:\n      - {round: 18, action: \"分歧记录. R2 认为 novelty 不足以进 main conference; R1 认为 empirical contributions 可能 borderline. 无法通过补实验解决.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W2\"\n    summary: \"无实际推理加速: pipeline 增加 6.4% 延迟, unstructured masks 无法转化为 wall-clock speedup\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W1 Critical + R2-W4 Minor. Appendix A Table 6 实测 +6.4% overhead. 论文已定位为 empirical study 但 Introduction 开篇仍以 efficiency 动机展开, 存在 framing 张力.\"}\n    action_items:\n      - {round: 18, action: \"检查 Introduction 开篇是否仍暗示 efficiency 收益, 考虑进一步弱化 efficiency framing 或提供 block-sparse prototype.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W3\"\n    summary: \"Knowledge-intensive tasks 系统性退步: MMLU -5.2pp (8B), GSM8K -20pp (14B), 跨三个模型一致\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W2 Major + R2-W2 Major. 论文仅提供 forward KL mode-covering 的假设性解释 (§4.2), 无实验验证. 三个模型 knowledge tasks 均无改进或退步.\"}\n    action_items:\n      - {round: 18, action: \"考虑: (1) reverse KL 下游 metrics 验证 mode-covering 假设; (2) KL vs BCE masks 在 MMLU-relevant layers 的 retention pattern 对比.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W4\"\n    summary: \"Gradient coupling 因果解释不完整: 缺少 per-layer KL 关键对照实验\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W5 Major, R2-W3 Major). BCE/MSE/KL 同时变化 loss type × scope × signal source 三个维度, 无法隔离 coupling 效果. Per-layer KL (固定 loss type + signal source, 仅改变 scope) 是关键缺失实验.\"}\n      - {round: 18, reviewers: [1], note: \"R1 交叉回应部分 REBUT R2-W3: 论文已标注 'suggestive', C1 ablation 提供了 mask quality 的因果证据, 不应将整个叙事归为 overclaiming.\"}\n    action_items:\n      - {round: 18, action: \"补充 per-layer KL ablation 实验, 隔离 coupling scope 的独立效果.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W5\"\n    summary: \"MSE baseline 单 seed 报告掩盖高方差: seed 123 sparsity 仅 5.1% (PPL=15789), 完全失败\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W4 Major, R2 交叉回应强烈同意. Appendix G 承认 seed 123 failure, 但 Table 2/4 仅报 seed 42. 有 cherry-picking 嫌疑.\"}\n    action_items:\n      - {round: 18, action: \"MSE 补充 3-seed 报告 (含 failed seed) 或 2-seed + 明确排除说明. 将 seed sensitivity 作为 MSE systematic weakness 讨论.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W6\"\n    summary: \"Table 2 actual sparsity 不匹配: KL 28.5% vs TEAL 29.3%, headline 比较在不同条件下\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W3 Major. 正文有 matched comparison (14.5% at 28.5%), 但 Table 2 headline 仍在不同 actual sparsity 下. R2 认为影响有限但同意 presentation 需改进.\"}\n    action_items:\n      - {round: 18, action: \"Table 2 增加 TEAL at 28.5% 行, 或在 Table caption 中更显著标注 actual sparsity 差异.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W7\"\n    summary: \"Seed-to-seed mask Jaccard divergence 未报告, 46-68% 数字信息量可能不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2-Q2. 如果不同 seed KL predictor 之间 mask divergence 也达 40-60%, 则 KL-vs-magnitude 的 46-68% divergence 不具备 unique discriminative power.\"}\n      - {round: 18, reviewers: [1], note: \"交叉回应 AGREE. PPL stability (CV=0.6%) 已报告但 mask-level consistency 未报告. 关键缺口.\"}\n    action_items:\n      - {round: 18, action: \"报告 cross-seed mask Jaccard distance (KL seed A vs KL seed B), 作为 46-68% divergence 的 reference baseline.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W8\"\n    summary: \"14B scale 结果有限: 仅 30% sparsity, GSM8K 大幅退步 (32.1±5.2% vs dense 52.1%)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W6 Minor. Contribution 4 ('preliminary analysis at 7-14B') 基础薄弱. 至少补充 50% sparsity 14B 结果.\"}\n    action_items:\n      - {round: 18, action: \"补充 Qwen-14B 50% sparsity 数据, 或降级 Contribution 4 的 claim strength.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W9\"\n    summary: \"训练数据同质性: WikiText-103 训练, C4 OOD 方差增大 31× (CV 0.2%→6.3%)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W7 Minor + R2-W6 Minor. Limitations 已讨论但未探讨多样化训练数据的影响.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"Missing refs: Mixture-of-Channels (MoC, 2511.09323); Sparsity via Activation Pattern Clustering (2507.14179)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2 提出. MoC 与 SwiGLU gate sparsity 问题域高度重合; Clustering 是 predictor network 的替代方案.\"}\n    action_items:\n      - {round: 18, action: \"在 Related Work 中讨论 MoC 和 Activation Pattern Clustering.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 16-17 — Resolved issues (history)\n  # ============================================================\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致: headline result (50% KL global PPL 11.79) 为 single-seed, MSE baseline 全部 single-seed\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. Table 2 headline 基于 s42 而非 3-seed mean.\"}\n      - {round: 18, reviewers: [1, 2], note: \"KL 50% global 已更新为 3-seed (11.84±0.15). MSE 仍为 single-seed (R18-W5). 部分改善但未完全解决.\"}\n    action_items:\n      - {round: 16, action: \"Table 2 所有行补充完整 3-seed 统计; MSE baseline 至少补 2 个种子.\", assigned_to: \"research_director\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N2\"\n    summary: \"消融实验仅在 50% 稀疏度, 论文实际可用的 30% regime 缺消融覆盖\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识.\"}\n      - {round: 18, reviewers: [1, 2], note: \"本轮未再提出. Table 4 现含 30%+50% 双列消融, 问题已解决.\"}\n    resolution: \"Table 4 现包含 30% 和 50% 双列消融.\"\n    resolution_round: 17\n\n  - id: \"R16-N3\"\n    summary: \"新颖性不足: 核心是标准 KL distillation 直接应用于 SwiGLU sparsity predictor\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2-N1 critical.\"}\n      - {round: 16, reviewers: [1], note: \"[REBUT] empirical insight 足够.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 再次出现 (R18-W1). R2 维持 novelty 不足. R1 partial agree. 分歧持续.\"}\n    action_items:\n      - {round: 16, action: \"分歧记录. 无法通过补实验解决.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N4\"\n    summary: \"缺少与已有训练型稀疏预测器的数值对比\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"本轮未再提出. BCE=DejaVu-style, MSE=ShadowLLM/D2DMoE 标注已被接受.\"}\n    resolution: \"experiments.tex 已明确标注 controlled comparison equivalences.\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"PPL 改善与下游任务 task-type-dependent 脱节\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"Abstract 已报告 MMLU 退化.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 再次出现 (R18-W3). 尽管 disclosure 改善, 实质性问题 (MMLU -5.2pp, GSM8K 退步) 仍被两位 reviewer 标记为 Major.\"}\n    action_items:\n      - {round: 18, action: \"需要更深入的因果分析 (reverse KL downstream, per-layer retention analysis).\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W2\"\n    summary: \"无实际推理加速: unstructured mask 无 wall-clock speedup\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"Framing 已调整.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 再次出现 (R18-W2). Introduction 开篇仍以 efficiency 动机展开, 存在 framing 张力. R1 升级为 Critical.\"}\n    action_items:\n      - {round: 18, action: \"Introduction 开篇 framing 需进一步调整.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W3\"\n    summary: \"Forward KL 方向选择论证不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出. §3.4 的 forward vs reverse KL 论证被接受.\"}\n    resolution: \"§3.4 forward KL 论证和 wu2025rethinking 引用已被接受.\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"评估域同质性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"本轮降级为 Minor (R18-W9). Limitations 讨论被接受, 但 C4 variance 增大仍被注意到.\"}\n    resolution: \"Limitations 讨论被接受. 降级为 info.\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"§3.6 梯度分析 informal\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"'suggestive' hedge 可接受.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 升级为 R18-W4 Critical: 不仅是 informal, 更缺少 per-layer KL 关键对照实验来隔离 coupling 效果.\"}\n    action_items:\n      - {round: 18, action: \"Per-layer KL ablation 是新的关键需求.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M1\"\n    summary: \"Missing references: activation sparsity opportunities, 2:4 activation sparsity, rethinking KL in KD\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出. 三篇引用已添加并被接受.\"}\n    resolution: \"三篇引用均已添加.\"\n    resolution_round: 17\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页, desk-reject 风险\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2 格式检查确认: 正文 8 页合规.\"}\n    resolution: \"正文 8 页合规, R18 格式检查通过.\"\n    resolution_round: 17\n\n  - id: \"R16-VIS2\"\n    summary: \"前4页无 display item, Figure 1 推迟到第6页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出.\"}\n    resolution: \"Figure 1 移至 introduction.tex, 渲染在第 2 页.\"\n    resolution_round: 17\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W4 的 gradient coupling narrative 批评与此相关. R2 仍认为措辞有 overclaiming (如 'gradient coupling discovers mask patterns'). R1 认为 'suggestive' 标注足够.\"}\n    action_items:\n      - {round: 18, action: \"继续降级 coupling alignment 措辞, 避免 'discovers' 等暗示 emergent discovery 的表述.\", assigned_to: \"research_director\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity 下报告\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出. Abstract 现报告 matched (14.5%) 和 unmatched (19%) 双数字.\"}\n    resolution: \"Abstract 双数字报告被接受.\"\n    resolution_round: 16\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W1 再次提出. §2 三点区分被 R2 认为仅是 application-level. 分歧持续.\"}\n    action_items:\n      - {round: 18, action: \"持续分歧. 当前区分论证可能是最优解.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, downstream task-dependent\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未作为独立 issue 提出. 已纳入 R18-W3 的 downstream 不一致性讨论.\"}\n    resolution: \"Abstract 和正文已加入 task-type split 描述.\"\n    resolution_round: 16"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 18 (fresh) — Active issues\n  # ============================================================\n\n  - id: \"R18-W1\"\n    summary: \"方法论新颖性有限: 核心 KL+Gumbel 训练配方与 MaskLLM 高度重合，区别仅在 application level\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2-W1 Major. 核心配方 (frozen backbone + learnable masks + KL + Gumbel) 与 MaskLLM 重合. 三点区别均为 application-level. 作为 empirical study 达 Findings bar, 但 main conference 需更多方法论贡献.\"}\n      - {round: 18, reviewers: [1], note: \"交叉回应: AGREE with nuance. Application differences 非完全 trivial (per-token + global top-k 产生长距离依赖), 但方法论新颖性确实有限.\"}\n    action_items:\n      - {round: 18, action: \"分歧记录. R2 认为 novelty 不足以进 main conference; R1 认为 empirical contributions 可能 borderline. 无法通过补实验解决.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W2\"\n    summary: \"无实际推理加速: pipeline 增加 6.4% 延迟, unstructured masks 无法转化为 wall-clock speedup\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W1 Critical + R2-W4 Minor. Appendix A Table 6 实测 +6.4% overhead. 论文已定位为 empirical study 但 Introduction 开篇仍以 efficiency 动机展开, 存在 framing 张力.\"}\n    action_items:\n      - {round: 18, action: \"检查 Introduction 开篇是否仍暗示 efficiency 收益, 考虑进一步弱化 efficiency framing 或提供 block-sparse prototype.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W3\"\n    summary: \"Knowledge-intensive tasks 系统性退步: MMLU -5.2pp (8B), GSM8K -20pp (14B), 跨三个模型一致\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W2 Major + R2-W2 Major. 论文仅提供 forward KL mode-covering 的假设性解释 (§4.2), 无实验验证. 三个模型 knowledge tasks 均无改进或退步.\"}\n    action_items:\n      - {round: 18, action: \"考虑: (1) reverse KL 下游 metrics 验证 mode-covering 假设; (2) KL vs BCE masks 在 MMLU-relevant layers 的 retention pattern 对比.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W4\"\n    summary: \"Gradient coupling 因果解释不完整: 缺少 per-layer KL 关键对照实验\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W5 Major, R2-W3 Major). BCE/MSE/KL 同时变化 loss type × scope × signal source 三个维度, 无法隔离 coupling 效果. Per-layer KL (固定 loss type + signal source, 仅改变 scope) 是关键缺失实验.\"}\n      - {round: 18, reviewers: [1], note: \"R1 交叉回应部分 REBUT R2-W3: 论文已标注 'suggestive', C1 ablation 提供了 mask quality 的因果证据, 不应将整个叙事归为 overclaiming.\"}\n    action_items:\n      - {round: 18, action: \"补充 per-layer KL ablation 实验, 隔离 coupling scope 的独立效果.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W5\"\n    summary: \"MSE baseline 单 seed 报告掩盖高方差: seed 123 sparsity 仅 5.1% (PPL=15789), 完全失败\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W4 Major, R2 交叉回应强烈同意. Appendix G 承认 seed 123 failure, 但 Table 2/4 仅报 seed 42. 有 cherry-picking 嫌疑.\"}\n    action_items:\n      - {round: 18, action: \"MSE 补充 3-seed 报告 (含 failed seed) 或 2-seed + 明确排除说明. 将 seed sensitivity 作为 MSE systematic weakness 讨论.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W6\"\n    summary: \"Table 2 actual sparsity 不匹配: KL 28.5% vs TEAL 29.3%, headline 比较在不同条件下\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W3 Major. 正文有 matched comparison (14.5% at 28.5%), 但 Table 2 headline 仍在不同 actual sparsity 下. R2 认为影响有限但同意 presentation 需改进.\"}\n    action_items:\n      - {round: 18, action: \"Table 2 增加 TEAL at 28.5% 行, 或在 Table caption 中更显著标注 actual sparsity 差异.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W7\"\n    summary: \"Seed-to-seed mask Jaccard divergence 未报告, 46-68% 数字信息量可能不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2-Q2. 如果不同 seed KL predictor 之间 mask divergence 也达 40-60%, 则 KL-vs-magnitude 的 46-68% divergence 不具备 unique discriminative power.\"}\n      - {round: 18, reviewers: [1], note: \"交叉回应 AGREE. PPL stability (CV=0.6%) 已报告但 mask-level consistency 未报告. 关键缺口.\"}\n    action_items:\n      - {round: 18, action: \"报告 cross-seed mask Jaccard distance (KL seed A vs KL seed B), 作为 46-68% divergence 的 reference baseline.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W8\"\n    summary: \"14B scale 结果有限: 仅 30% sparsity, GSM8K 大幅退步 (32.1±5.2% vs dense 52.1%)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W6 Minor. Contribution 4 ('preliminary analysis at 7-14B') 基础薄弱. 至少补充 50% sparsity 14B 结果.\"}\n    action_items:\n      - {round: 18, action: \"补充 Qwen-14B 50% sparsity 数据, 或降级 Contribution 4 的 claim strength.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-W9\"\n    summary: \"训练数据同质性: WikiText-103 训练, C4 OOD 方差增大 31× (CV 0.2%→6.3%)\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识. R1-W7 Minor + R2-W6 Minor. Limitations 已讨论但未探讨多样化训练数据的影响.\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"Missing refs: Mixture-of-Channels (MoC, 2511.09323); Sparsity via Activation Pattern Clustering (2507.14179)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2 提出. MoC 与 SwiGLU gate sparsity 问题域高度重合; Clustering 是 predictor network 的替代方案.\"}\n    action_items:\n      - {round: 18, action: \"在 Related Work 中讨论 MoC 和 Activation Pattern Clustering.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 16-17 — Resolved issues (history)\n  # ============================================================\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致: headline result (50% KL global PPL 11.79) 为 single-seed, MSE baseline 全部 single-seed\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识. Table 2 headline 基于 s42 而非 3-seed mean.\"}\n      - {round: 18, reviewers: [1, 2], note: \"KL 50% global 已更新为 3-seed (11.84±0.15). MSE 仍为 single-seed (R18-W5). 部分改善但未完全解决.\"}\n    action_items:\n      - {round: 16, action: \"Table 2 所有行补充完整 3-seed 统计; MSE baseline 至少补 2 个种子.\", assigned_to: \"research_director\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N2\"\n    summary: \"消融实验仅在 50% 稀疏度, 论文实际可用的 30% regime 缺消融覆盖\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"[AGREE] 共识.\"}\n      - {round: 18, reviewers: [1, 2], note: \"本轮未再提出. Table 4 现含 30%+50% 双列消融, 问题已解决.\"}\n    resolution: \"Table 4 现包含 30% 和 50% 双列消融.\"\n    resolution_round: 17\n\n  - id: \"R16-N3\"\n    summary: \"新颖性不足: 核心是标准 KL distillation 直接应用于 SwiGLU sparsity predictor\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2-N1 critical.\"}\n      - {round: 16, reviewers: [1], note: \"[REBUT] empirical insight 足够.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 再次出现 (R18-W1). R2 维持 novelty 不足. R1 partial agree. 分歧持续.\"}\n    action_items:\n      - {round: 16, action: \"分歧记录. 无法通过补实验解决.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-N4\"\n    summary: \"缺少与已有训练型稀疏预测器的数值对比\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"本轮未再提出. BCE=DejaVu-style, MSE=ShadowLLM/D2DMoE 标注已被接受.\"}\n    resolution: \"experiments.tex 已明确标注 controlled comparison equivalences.\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"PPL 改善与下游任务 task-type-dependent 脱节\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"Abstract 已报告 MMLU 退化.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 再次出现 (R18-W3). 尽管 disclosure 改善, 实质性问题 (MMLU -5.2pp, GSM8K 退步) 仍被两位 reviewer 标记为 Major.\"}\n    action_items:\n      - {round: 18, action: \"需要更深入的因果分析 (reverse KL downstream, per-layer retention analysis).\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W2\"\n    summary: \"无实际推理加速: unstructured mask 无 wall-clock speedup\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"Framing 已调整.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 再次出现 (R18-W2). Introduction 开篇仍以 efficiency 动机展开, 存在 framing 张力. R1 升级为 Critical.\"}\n    action_items:\n      - {round: 18, action: \"Introduction 开篇 framing 需进一步调整.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-W3\"\n    summary: \"Forward KL 方向选择论证不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出. §3.4 的 forward vs reverse KL 论证被接受.\"}\n    resolution: \"§3.4 forward KL 论证和 wu2025rethinking 引用已被接受.\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"评估域同质性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"本轮降级为 Minor (R18-W9). Limitations 讨论被接受, 但 C4 variance 增大仍被注意到.\"}\n    resolution: \"Limitations 讨论被接受. 降级为 info.\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"§3.6 梯度分析 informal\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"'suggestive' hedge 可接受.\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18 升级为 R18-W4 Critical: 不仅是 informal, 更缺少 per-layer KL 关键对照实验来隔离 coupling 效果.\"}\n    action_items:\n      - {round: 18, action: \"Per-layer KL ablation 是新的关键需求.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R16-M1\"\n    summary: \"Missing references: activation sparsity opportunities, 2:4 activation sparsity, rethinking KL in KD\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出. 三篇引用已添加并被接受.\"}\n    resolution: \"三篇引用均已添加.\"\n    resolution_round: 17\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页, desk-reject 风险\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2 格式检查确认: 正文 8 页合规.\"}\n    resolution: \"正文 8 页合规, R18 格式检查通过.\"\n    resolution_round: 17\n\n  - id: \"R16-VIS2\"\n    summary: \"前4页无 display item, Figure 1 推迟到第6页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出.\"}\n    resolution: \"Figure 1 移至 introduction.tex, 渲染在第 2 页.\"\n    resolution_round: 17\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 14\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W4 的 gradient coupling narrative 批评与此相关. R2 仍认为措辞有 overclaiming (如 'gradient coupling discovers mask patterns'). R1 认为 'suggestive' 标注足够.\"}\n    action_items:\n      - {round: 18, action: \"继续降级 coupling alignment 措辞, 避免 'discovers' 等暗示 emergent discovery 的表述.\", assigned_to: \"research_director\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity 下报告\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未再提出. Abstract 现报告 matched (14.5%) 和 unmatched (19%) 双数字.\"}\n    resolution: \"Abstract 双数字报告被接受.\"\n    resolution_round: 16\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W1 再次提出. §2 三点区分被 R2 认为仅是 application-level. 分歧持续.\"}\n    action_items:\n      - {round: 18, action: \"持续分歧. 当前区分论证可能是最优解.\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, downstream task-dependent\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 18\n    mentions:\n      - {round: 18, reviewers: [], note: \"本轮未作为独立 issue 提出. 已纳入 R18-W3 的 downstream 不一致性讨论.\"}\n    resolution: \"Abstract 和正文已加入 task-type split 描述.\"\n    resolution_round: 16"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-21T01:33:28.806229+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 14385}, \"error\": \"\"}"}

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

_source line 1482 · 2026-05-21T01:35:47.255707+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "report": "# 审稿报告 — Round 18 (Fresh Review)\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: R1 (方法严谨性 + 实验验证) + R2 (新颖性 + Related Work + 写作 + 格式)\n\n---\n\n## Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor（75.9M params, &lt;1% base），配合 Gumbel-Sigmoid relaxation 和 adaptive penalty controller。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，在 LLaMA-3.1-8B 上 PPL 减少 14.5%（matched sparsity）。Target-swap ablation (C1) 确认 mask quality 而非 training objective 本身驱动推理质量。跨架构评估覆盖 Mistral-7B 和 Qwen-2.5-14B，论文自定位为 \"primarily empirical study\"。\n\n---\n\n## Strengths\n\n**S1. C1 Target-Swap Ablation 设计精巧 [R1, R2 共识]** — Table 3 通过让 BCE predictor 使用 KL-derived oracle masks，干净地解耦了 mask quality 与 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp (s42)，30% 下 3 seed 一致性 ≤1.70pp。在 activation sparsity 领域中这种实验设计较为少见，为 \"mask quality drives inference quality\" 提供了有说服力的因果证据。\n\n**S2. 消融覆盖面广且系统性强 [R1, R2 共识]** — Table 4 系统对比 divergence 类型（forward KL/JSD/reverse KL）、relaxation 方法（Gumbel vs STE）、loss isolation（BCE+Gumbel vs BCE）。Appendix 17 个 section 覆盖 bottleneck 敏感性、OOD 评估、training stability、SNR 分析等。实验透彻度超过同领域大多数工作。\n\n**S3. 诚实的结果报告与自我定位 [R1, R2 共识]** — 明确报告 MMLU −5.2pp、Qwen-14B GSM8K −20pp、50% 下游 capacity cliff。自承 \"primarily empirical study\"，降低期望校准成本。\n\n**S4. 二维 Taxonomy 有组织价值 [R1, R2 共识]** — Table 1 沿 correction granularity × training signal coupling 组织先前工作，定位清晰。\n\n**S5. Multi-seed 评估 + 多架构验证 [R1, R2 共识]** — 关键结论均 3-seed 评估；覆盖 3 个模型家族 (7B-14B)。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**W1. 方法论新颖性有限，与 MaskLLM 核心配方重合 [R2 主导，R1 partial agree]**\n核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文声称的三点区别——activation vs weight sparsity, dynamic vs static masks, predictor vs learnable parameters——均为 application-level differences 而非 methodological innovation。论文未讨论关键 counterfactual：将 MaskLLM 策略直接迁移到 activation sparsity 是否足以复现核心结果。作为 \"primarily empirical study\"，novelty 可达 Findings bar，但对 main conference 缺乏方法论或理论层面的新贡献。\n\n**W2. 无实际推理加速，Introduction framing 仍存在张力 [R1, R2 共识]**\nAppendix A Table 6 实测显示 KL pipeline 增加 6.4% 延迟（126.78 vs 119.11 ms/fwd）。论文承认 unstructured masks 无 wall-clock speedup，且 Introduction §1 已声明 \"primarily empirical study\" + \"Wall-clock speedup requires sparse kernel support not addressed here\"，但开篇仍以 \"SwiGLU FFNs exhibit high contextual sparsity\" 建立 efficiency 动机，framing 张力尚未完全消解。\n\n**W3. Knowledge-intensive tasks 系统性退步，跨模型一致 [R1, R2 共识]**\nMMLU: KL 40.7% vs TEAL 45.9% (−5.2pp, LLaMA-8B 30%); Qwen-14B: GSM8K 32.1±5.2% vs TEAL 52.1% (−20pp); Mistral-7B: GSM8K reversed across all seeds。三个模型上 knowledge-intensive tasks 均无改进或退步。§4.2 仅提供假设性解释（forward KL mode-covering \"may dilute task-specific knowledge pathways\"），无实验验证。若 \"better masks\" 仅在 PPL 和 commonsense tasks 上体现，\"mask quality drives inference quality\" 的 claim 实用意义受限。\n\n**W4. Gradient coupling 因果解释不完整，缺少 per-layer KL 关键对照 [R1, R2 共识]**\n§3.6 梯度分析停留在直觉描述。当前实验中 BCE/MSE/KL 同时变化 loss type × scope × signal source 三个维度，无法隔离 coupling 的独立效果。关键缺失实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence），可固定 loss type + signal source 仅改变 scope，真正隔离 \"coupling\" 效果。论文已标注 \"suggestive\" 并以 C1 ablation 提供 mask quality 的因果证据，但 \"gradient coupling discovers mask patterns\" 等措辞仍有 overclaiming 之嫌。\n\n### Should-Fix (Major)\n\n**W5. MSE baseline 单 seed 掩盖高方差 [R1 主导，R2 强烈同意]**\nAppendix G 承认 MSE with seed 123 仅达 5.1% sparsity (PPL=15,789)——完全失败。但 Table 2/4 中 MSE 均为 seed 42 单 seed 结果。一个方法 3 seed 中 1 个完全失败，用另一个 seed 代表该方法性能不够公正。应报告 3-seed（含失败 seed）或 2-seed + 明确排除说明。\n\n**W6. Table 2 actual sparsity 不匹配 [R1 主导，R2 同意]**\nKL 30% actual=28.5% vs TEAL 30% actual=29.3%，0.8pp 差异意味着 KL 保留更多神经元。正文提供了 matched comparison (14.5% at 28.5%)，但 Table 2 headline 仍在不同 actual sparsity 下比较。建议增加 TEAL at 28.5% 行或在 caption 中更显著标注。\n\n**W7. Seed-to-seed mask Jaccard divergence 未报告 [R2 主导，R1 强烈同意]**\n论文报告 KL-vs-magnitude mask divergence 46-68%，但未报告 KL seed A vs KL seed B 的 mask divergence。若 seed 间 divergence 也达 40-60%，则 46-68% 的数字不具 unique discriminative power。PPL stability (CV=0.6%) 不等于 mask-level consistency。\n\n### Nice-to-Fix (Minor)\n\n**W8. 14B scale 结果有限 [R1, R2 共识]** — Qwen-14B 仅 30% sparsity，GSM8K 大幅退步，Contribution 4 基础薄弱。\n\n**W9. 训练数据同质性 [R1, R2 共识]** — WikiText-103 单域训练，C4 OOD cross-seed variance 增大 31× (CV 0.2%→6.3%)。\n\n**W10. Abstract 信息密度过高 [R2]** — ~200 词塞入过多具体数字，模糊核心 message。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| C1 ablation 设计优秀 | ✅ S1 | ✅ S1 | **[AGREE]** |\n| 消融全面，实验透彻 | ✅ S2 | ✅ S2 | **[AGREE]** |\n| 无 wall-clock speedup | ✅ W1 Critical | ✅ W4 Minor | **[AGREE]** (严重程度有差异) |\n| Downstream 不一致 | ✅ W2 Major | ✅ W2 Major | **[AGREE]** |\n| Actual sparsity mismatch | ✅ W3 Major | ✅ agree | **[AGREE]** |\n| MSE single-seed | ✅ W4 Major | ✅ agree | **[AGREE]** |\n| Gradient coupling 缺形式化 | ✅ W5 Major | ✅ W3 Major | **[AGREE]** |\n| Seed mask divergence 未报告 | ✅ agree | ✅ Q2 | **[AGREE]** |\n| 14B limited | ✅ W6 Minor | ✅ agree | **[AGREE]** |\n| Training data homogeneity | ✅ W7 Minor | ✅ W6 Minor | **[AGREE]** |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧 |\n|------|----|----|------|\n| **Novelty / MaskLLM** | Application differences 非 trivial，empirical contributions 可能 borderline conference | Novelty 不足 main conference，仅达 Findings bar | R1 更看重 execution quality 和 C1 方法论贡献; R2 更强调方法层面的增量性 |\n| **Gradient coupling overclaiming** | \"Suggestive\" 标注 + C1 evidence 足够，不应归为 overclaiming | \"Discovers\" 等措辞暗示 emergent discovery，是 overclaiming | R1 认为 hedge 到位；R2 认为仍有误导性 |\n\n---\n\n## Questions\n\n**Q1.** C1 s42 oracle 来自 \"earlier training run\"，s123/s456 使用 matched retrained oracles。统一 matched oracles 后 s42 gap 是否缩小？[R1]\n\n**Q2.** Reverse KL predictor 的下游 metrics？若 mode-seeking 更好保留 knowledge pathways (MMLU)，可验证 W3 的假设性解释。[R1, R2 共识]\n\n**Q3.** Table 2 缺 BCE 30% uniform 条目。Table 4 的 BCE 30% PPL=15.71 是否 uniform allocation？[R1]\n\n**Q4.** MSE seed 123 失败是 Gumbel+Lagrangian 组合不稳定还是 MSE 固有缺陷？KL 有无类似 failure seed？[R1, R2 共识]\n\n**Q5.** KL training cost 约 2.6× BCE，每个 sparsity target 需独立训练。是否可训练单个 predictor 支持多 sparsity levels？[R1, R2 共识]\n\n**Q6.** KL seed A vs KL seed B 的 mask Jaccard divergence 是多少？作为 46-68% KL-vs-magnitude divergence 的 reference baseline。[R2, R1 agree]\n\n---\n\n## Missing References\n\n- **Mixture-of-Channels (MoC)** (arXiv 2511.09323, Nov 2025) — SwiGLU native gating + Top-K channel selection，问题域高度重合 [R2]\n- **\"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\"** (arXiv 2507.14179, Jul 2025) — predictor network 的替代方案 [R2]\n- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖 [R1, R2 partial agree]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending** — 外部审稿请求已于 2026-05-21T01:18:43 UTC 发送，尚未返回。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：error** — 视觉审查 Agent 因配额耗尽 (rate limit) 而失败，未能完成 PDF 渲染检查。用户可在配额重置后（2026-05-22 18:00 UTC）重新触发。\n\n**R2 格式合规检查结果（替代）**: 页数 ✅ (8页正文)、模板 ✅ (ACL)、匿名 ✅、Limitations ✅、Ethics ✅、Checklist ✅、引用 ✅ (50条引用全部验证通过，1 orphan bib entry `de2024griffin` 未引用)。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)** | R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)\n**Confidence: 4/5**\n\n本文是一篇执行质量较高的 empirical study，C1 target-swap ablation 有独立方法论价值，消融覆盖极其全面，结果报告诚实。然而存在四个核心短板：\n\n1. **Novelty**: 核心 KL+Gumbel 训练配方与 MaskLLM 高度重合，区别仅在 application level。论文诚实地自定位为 empirical study，但 empirical insights（KL 优于 BCE for activation sparsity）的影响范围有限。\n\n2. **Downstream inconsistency**: Knowledge-intensive tasks 跨三个模型系统性退步（MMLU −5.2pp, GSM8K −20pp at 14B），\"quality improvement\" claim 仅在 PPL + commonsense tasks 上成立，削弱了实用价值。\n\n3. **因果解释不完整**: Gradient coupling 叙事缺少 per-layer KL 关键对照实验，无法隔离 coupling scope 的独立贡献。\n\n4. **No speedup**: Pipeline 增加 6.4% overhead，无实际推理加速。\n\nR1 (3.5) 和 R2 (3.0) 的 0.5 分差距主要源于 novelty 权重：R1 认为 C1 ablation 质量和消融覆盖面可能补偿方法论增量性；R2 认为一个 well-designed ablation 不能弥补核心 novelty 不足。综合两方观点，本文更适合 **Findings** 轨道——execution quality 达标，但 impact 和 novelty 不足以进入 main conference。\n\n**升档路径 (→3.5 Borderline Conference)**:\n- 补充 per-layer KL ablation，若结果支持 coupling hypothesis\n- 提供 reverse KL 下游 metrics，验证 mode-covering 假设\n- MSE 补 multi-seed 或明确排除说明\n- 报告 cross-seed mask Jaccard distance\n\n**降档风险 (→2.5 Borderline Findings)**:\n- MaskLLM 策略直接迁移即可复现结果（Q1 from R2）\n- Seed-level mask divergence 与 KL-vs-magnitude divergence 可比（invalidates §4.4 core finding）\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度过高，建议精简具体数字，突出 1-2 个核心定量发现\n- \"coupled gradient discovers mask patterns\" 措辞有 overclaiming 之嫌，建议改为 \"output-distribution optimization yields different mask patterns\"\n\n### Introduction (§1)\n- 开篇 efficiency 动机与 \"primarily empirical study\" 定位存在张力\n- Contribution 4 (\"preliminary analysis at 7-14B\") 基础薄弱（仅 30% sparsity, GSM8K −20pp）\n\n### Method (§3)\n- §3.4 forward KL 论证清晰，引用充分\n- §3.6 gradient analysis 标注 \"suggestive\" 是合适的 hedge，但 \"coupling\" 措辞在全文中仍被用作因果性表述\n- §3.7 taxonomy 有组织价值但 MSE failure 的解释需要 per-layer KL 实验支持\n\n### Experiments (§4)\n- Table 2: 缺 BCE 30% uniform 条目；actual sparsity mismatch 需更显著标注\n- Table 3 (C1): 设计精巧，是论文最强贡献。s42 oracle provenance 差异需澄清\n- Table 4: 30%+50% 双列消融全面。但 MSE 仅 seed 42\n- §4.4 mask divergence: 缺 cross-seed mask Jaccard 作为 reference baseline\n- §4.6 allocation analysis: non-monotonic 发现有趣但 14B 数据不足\n\n### Related Work (§2)\n- MaskLLM 三点区分描述准确但需强调为 methodological 而非仅 application-level\n- 缺 MoC (2511.09323) 和 Activation Pattern Clustering (2507.14179) 讨论\n- Orphan bib entry: `de2024griffin` 未在正文引用\n\n### Limitations\n- 全面且诚实。训练数据同质性、PPL-downstream gap、scale 限制均已讨论\n\n### Ethics\n- 合规，无 concerns\n\n### Format\n- 8 页正文 ✅，ACL 模板 ✅，匿名 ✅，完整 checklist ✅"
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
    "overall_score": "3.0 (Findings)",
    "report": "# 审稿报告 — Round 18 (Fresh Review)\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: R1 (方法严谨性 + 实验验证) + R2 (新颖性 + Related Work + 写作 + 格式)\n\n---\n\n## Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor（75.9M params, &lt;1% base），配合 Gumbel-Sigmoid relaxation 和 adaptive penalty controller。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，在 LLaMA-3.1-8B 上 PPL 减少 14.5%（matched sparsity）。Target-swap ablation (C1) 确认 mask quality 而非 training objective 本身驱动推理质量。跨架构评估覆盖 Mistral-7B 和 Qwen-2.5-14B，论文自定位为 \"primarily empirical study\"。\n\n---\n\n## Strengths\n\n**S1. C1 Target-Swap Ablation 设计精巧 [R1, R2 共识]** — Table 3 通过让 BCE predictor 使用 KL-derived oracle masks，干净地解耦了 mask quality 与 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp (s42)，30% 下 3 seed 一致性 ≤1.70pp。在 activation sparsity 领域中这种实验设计较为少见，为 \"mask quality drives inference quality\" 提供了有说服力的因果证据。\n\n**S2. 消融覆盖面广且系统性强 [R1, R2 共识]** — Table 4 系统对比 divergence 类型（forward KL/JSD/reverse KL）、relaxation 方法（Gumbel vs STE）、loss isolation（BCE+Gumbel vs BCE）。Appendix 17 个 section 覆盖 bottleneck 敏感性、OOD 评估、training stability、SNR 分析等。实验透彻度超过同领域大多数工作。\n\n**S3. 诚实的结果报告与自我定位 [R1, R2 共识]** — 明确报告 MMLU −5.2pp、Qwen-14B GSM8K −20pp、50% 下游 capacity cliff。自承 \"primarily empirical study\"，降低期望校准成本。\n\n**S4. 二维 Taxonomy 有组织价值 [R1, R2 共识]** — Table 1 沿 correction granularity × training signal coupling 组织先前工作，定位清晰。\n\n**S5. Multi-seed 评估 + 多架构验证 [R1, R2 共识]** — 关键结论均 3-seed 评估；覆盖 3 个模型家族 (7B-14B)。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**W1. 方法论新颖性有限，与 MaskLLM 核心配方重合 [R2 主导，R1 partial agree]**\n核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文声称的三点区别——activation vs weight sparsity, dynamic vs static masks, predictor vs learnable parameters——均为 application-level differences 而非 methodological innovation。论文未讨论关键 counterfactual：将 MaskLLM 策略直接迁移到 activation sparsity 是否足以复现核心结果。作为 \"primarily empirical study\"，novelty 可达 Findings bar，但对 main conference 缺乏方法论或理论层面的新贡献。\n\n**W2. 无实际推理加速，Introduction framing 仍存在张力 [R1, R2 共识]**\nAppendix A Table 6 实测显示 KL pipeline 增加 6.4% 延迟（126.78 vs 119.11 ms/fwd）。论文承认 unstructured masks 无 wall-clock speedup，且 Introduction §1 已声明 \"primarily empirical study\" + \"Wall-clock speedup requires sparse kernel support not addressed here\"，但开篇仍以 \"SwiGLU FFNs exhibit high contextual sparsity\" 建立 efficiency 动机，framing 张力尚未完全消解。\n\n**W3. Knowledge-intensive tasks 系统性退步，跨模型一致 [R1, R2 共识]**\nMMLU: KL 40.7% vs TEAL 45.9% (−5.2pp, LLaMA-8B 30%); Qwen-14B: GSM8K 32.1±5.2% vs TEAL 52.1% (−20pp); Mistral-7B: GSM8K reversed across all seeds。三个模型上 knowledge-intensive tasks 均无改进或退步。§4.2 仅提供假设性解释（forward KL mode-covering \"may dilute task-specific knowledge pathways\"），无实验验证。若 \"better masks\" 仅在 PPL 和 commonsense tasks 上体现，\"mask quality drives inference quality\" 的 claim 实用意义受限。\n\n**W4. Gradient coupling 因果解释不完整，缺少 per-layer KL 关键对照 [R1, R2 共识]**\n§3.6 梯度分析停留在直觉描述。当前实验中 BCE/MSE/KL 同时变化 loss type × scope × signal source 三个维度，无法隔离 coupling 的独立效果。关键缺失实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence），可固定 loss type + signal source 仅改变 scope，真正隔离 \"coupling\" 效果。论文已标注 \"suggestive\" 并以 C1 ablation 提供 mask quality 的因果证据，但 \"gradient coupling discovers mask patterns\" 等措辞仍有 overclaiming 之嫌。\n\n### Should-Fix (Major)\n\n**W5. MSE baseline 单 seed 掩盖高方差 [R1 主导，R2 强烈同意]**\nAppendix G 承认 MSE with seed 123 仅达 5.1% sparsity (PPL=15,789)——完全失败。但 Table 2/4 中 MSE 均为 seed 42 单 seed 结果。一个方法 3 seed 中 1 个完全失败，用另一个 seed 代表该方法性能不够公正。应报告 3-seed（含失败 seed）或 2-seed + 明确排除说明。\n\n**W6. Table 2 actual sparsity 不匹配 [R1 主导，R2 同意]**\nKL 30% actual=28.5% vs TEAL 30% actual=29.3%，0.8pp 差异意味着 KL 保留更多神经元。正文提供了 matched comparison (14.5% at 28.5%)，但 Table 2 headline 仍在不同 actual sparsity 下比较。建议增加 TEAL at 28.5% 行或在 caption 中更显著标注。\n\n**W7. Seed-to-seed mask Jaccard divergence 未报告 [R2 主导，R1 强烈同意]**\n论文报告 KL-vs-magnitude mask divergence 46-68%，但未报告 KL seed A vs KL seed B 的 mask divergence。若 seed 间 divergence 也达 40-60%，则 46-68% 的数字不具 unique discriminative power。PPL stability (CV=0.6%) 不等于 mask-level consistency。\n\n### Nice-to-Fix (Minor)\n\n**W8. 14B scale 结果有限 [R1, R2 共识]** — Qwen-14B 仅 30% sparsity，GSM8K 大幅退步，Contribution 4 基础薄弱。\n\n**W9. 训练数据同质性 [R1, R2 共识]** — WikiText-103 单域训练，C4 OOD cross-seed variance 增大 31× (CV 0.2%→6.3%)。\n\n**W10. Abstract 信息密度过高 [R2]** — ~200 词塞入过多具体数字，模糊核心 message。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| C1 ablation 设计优秀 | ✅ S1 | ✅ S1 | **[AGREE]** |\n| 消融全面，实验透彻 | ✅ S2 | ✅ S2 | **[AGREE]** |\n| 无 wall-clock speedup | ✅ W1 Critical | ✅ W4 Minor | **[AGREE]** (严重程度有差异) |\n| Downstream 不一致 | ✅ W2 Major | ✅ W2 Major | **[AGREE]** |\n| Actual sparsity mismatch | ✅ W3 Major | ✅ agree | **[AGREE]** |\n| MSE single-seed | ✅ W4 Major | ✅ agree | **[AGREE]** |\n| Gradient coupling 缺形式化 | ✅ W5 Major | ✅ W3 Major | **[AGREE]** |\n| Seed mask divergence 未报告 | ✅ agree | ✅ Q2 | **[AGREE]** |\n| 14B limited | ✅ W6 Minor | ✅ agree | **[AGREE]** |\n| Training data homogeneity | ✅ W7 Minor | ✅ W6 Minor | **[AGREE]** |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧 |\n|------|----|----|------|\n| **Novelty / MaskLLM** | Application differences 非 trivial，empirical contributions 可能 borderline conference | Novelty 不足 main conference，仅达 Findings bar | R1 更看重 execution quality 和 C1 方法论贡献; R2 更强调方法层面的增量性 |\n| **Gradient coupling overclaiming** | \"Suggestive\" 标注 + C1 evidence 足够，不应归为 overclaiming | \"Discovers\" 等措辞暗示 emergent discovery，是 overclaiming | R1 认为 hedge 到位；R2 认为仍有误导性 |\n\n---\n\n## Questions\n\n**Q1.** C1 s42 oracle 来自 \"earlier training run\"，s123/s456 使用 matched retrained oracles。统一 matched oracles 后 s42 gap 是否缩小？[R1]\n\n**Q2.** Reverse KL predictor 的下游 metrics？若 mode-seeking 更好保留 knowledge pathways (MMLU)，可验证 W3 的假设性解释。[R1, R2 共识]\n\n**Q3.** Table 2 缺 BCE 30% uniform 条目。Table 4 的 BCE 30% PPL=15.71 是否 uniform allocation？[R1]\n\n**Q4.** MSE seed 123 失败是 Gumbel+Lagrangian 组合不稳定还是 MSE 固有缺陷？KL 有无类似 failure seed？[R1, R2 共识]\n\n**Q5.** KL training cost 约 2.6× BCE，每个 sparsity target 需独立训练。是否可训练单个 predictor 支持多 sparsity levels？[R1, R2 共识]\n\n**Q6.** KL seed A vs KL seed B 的 mask Jaccard divergence 是多少？作为 46-68% KL-vs-magnitude divergence 的 reference baseline。[R2, R1 agree]\n\n---\n\n## Missing References\n\n- **Mixture-of-Channels (MoC)** (arXiv 2511.09323, Nov 2025) — SwiGLU native gating + Top-K channel selection，问题域高度重合 [R2]\n- **\"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\"** (arXiv 2507.14179, Jul 2025) — predictor network 的替代方案 [R2]\n- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖 [R1, R2 partial agree]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending** — 外部审稿请求已于 2026-05-21T01:18:43 UTC 发送，尚未返回。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：error** — 视觉审查 Agent 因配额耗尽 (rate limit) 而失败，未能完成 PDF 渲染检查。用户可在配额重置后（2026-05-22 18:00 UTC）重新触发。\n\n**R2 格式合规检查结果（替代）**: 页数 ✅ (8页正文)、模板 ✅ (ACL)、匿名 ✅、Limitations ✅、Ethics ✅、Checklist ✅、引用 ✅ (50条引用全部验证通过，1 orphan bib entry `de2024griffin` 未引用)。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)** | R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)\n**Confidence: 4/5**\n\n本文是一篇执行质量较高的 empirical study，C1 target-swap ablation 有独立方法论价值，消融覆盖极其全面，结果报告诚实。然而存在四个核心短板：\n\n1. **Novelty**: 核心 KL+Gumbel 训练配方与 MaskLLM 高度重合，区别仅在 application level。论文诚实地自定位为 empirical study，但 empirical insights（KL 优于 BCE for activation sparsity）的影响范围有限。\n\n2. **Downstream inconsistency**: Knowledge-intensive tasks 跨三个模型系统性退步（MMLU −5.2pp, GSM8K −20pp at 14B），\"quality improvement\" claim 仅在 PPL + commonsense tasks 上成立，削弱了实用价值。\n\n3. **因果解释不完整**: Gradient coupling 叙事缺少 per-layer KL 关键对照实验，无法隔离 coupling scope 的独立贡献。\n\n4. **No speedup**: Pipeline 增加 6.4% overhead，无实际推理加速。\n\nR1 (3.5) 和 R2 (3.0) 的 0.5 分差距主要源于 novelty 权重：R1 认为 C1 ablation 质量和消融覆盖面可能补偿方法论增量性；R2 认为一个 well-designed ablation 不能弥补核心 novelty 不足。综合两方观点，本文更适合 **Findings** 轨道——execution quality 达标，但 impact 和 novelty 不足以进入 main conference。\n\n**升档路径 (→3.5 Borderline Conference)**:\n- 补充 per-layer KL ablation，若结果支持 coupling hypothesis\n- 提供 reverse KL 下游 metrics，验证 mode-covering 假设\n- MSE 补 multi-seed 或明确排除说明\n- 报告 cross-seed mask Jaccard distance\n\n**降档风险 (→2.5 Borderline Findings)**:\n- MaskLLM 策略直接迁移即可复现结果（Q1 from R2）\n- Seed-level mask divergence 与 KL-vs-magnitude divergence 可比（invalidates §4.4 core finding）\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度过高，建议精简具体数字，突出 1-2 个核心定量发现\n- \"coupled gradient discovers mask patterns\" 措辞有 overclaiming 之嫌，建议改为 \"output-distribution optimization yields different mask patterns\"\n\n### Introduction (§1)\n- 开篇 efficiency 动机与 \"primarily empirical study\" 定位存在张力\n- Contribution 4 (\"preliminary analysis at 7-14B\") 基础薄弱（仅 30% sparsity, GSM8K −20pp）\n\n### Method (§3)\n- §3.4 forward KL 论证清晰，引用充分\n- §3.6 gradient analysis 标注 \"suggestive\" 是合适的 hedge，但 \"coupling\" 措辞在全文中仍被用作因果性表述\n- §3.7 taxonomy 有组织价值但 MSE failure 的解释需要 per-layer KL 实验支持\n\n### Experiments (§4)\n- Table 2: 缺 BCE 30% uniform 条目；actual sparsity mismatch 需更显著标注\n- Table 3 (C1): 设计精巧，是论文最强贡献。s42 oracle provenance 差异需澄清\n- Table 4: 30%+50% 双列消融全面。但 MSE 仅 seed 42\n- §4.4 mask divergence: 缺 cross-seed mask Jaccard 作为 reference baseline\n- §4.6 allocation analysis: non-monotonic 发现有趣但 14B 数据不足\n\n### Related Work (§2)\n- MaskLLM 三点区分描述准确但需强调为 methodological 而非仅 application-level\n- 缺 MoC (2511.09323) 和 Activation Pattern Clustering (2507.14179) 讨论\n- Orphan bib entry: `de2024griffin` 未在正文引用\n\n### Limitations\n- 全面且诚实。训练数据同质性、PPL-downstream gap、scale 限制均已讨论\n\n### Ethics\n- 合规，无 concerns\n\n### Format\n- 8 页正文 ✅，ACL 模板 ✅，匿名 ✅，完整 checklist ✅"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-21T01:35:51.826763+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4571
}
```

</details>

---


### Assistant

_source line 1484 · 2026-05-21T01:36:07.809324+00:00_

审稿报告已投递至 Research Director。

**Round 18 审稿完成摘要：**

| 维度 | 结果 |
|------|------|
| **Overall** | **3.0 (Findings)** |
| R1 评分 | 3.5 (Borderline Conference) |
| R2 评分 | 3.0 (Findings) |
| 共识点 | 10/12 (83%) |
| 分歧点 | 2 (novelty 权重 + overclaiming 程度) |
| 交叉轮次 | 1 轮 (充分收敛) |

**4 个 Critical Weaknesses：**
1. 方法论新颖性有限 (MaskLLM 重合)
2. 无实际推理加速 (+6.4% overhead)
3. Knowledge-intensive tasks 系统性退步 (MMLU −5.2pp)
4. Gradient coupling 因果解释缺 per-layer KL 对照

**升档关键：** per-layer KL ablation + reverse KL 下游 metrics + cross-seed mask Jaccard + MSE multi-seed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1485 · 2026-05-21T01:36:10.514145+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。总结：

- 对 R2 的 6 个 Weakness 中，4 个 AGREE（W1 novelty, W2 downstream, W5 abstract, W6 data）、2 个 REBUT（W3 部分同意但 C1 ablation 的结论仍成立; W4 事实性错误——论文有 wall-clock 数据）
- 对 R2 的 5 个 Question 中，2 个 AGREE（Q2 seed mask divergence 是关键缺口、Q5 多 GPU overhead）、3 个 REBUT（Q1 MaskLLM 不可直接迁移、Q3 MSE 非 output-level、Q4 数据引用 0.41 无法复现）
- 维持 Overall 3.5 评分，认为 R2 的 3.0 略低

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

_source line 1486 · 2026-05-21T01:36:24.994517+00:00_

审稿报告已投递完成。

**本轮审稿总结：**

- **Overall: 3.0 (Findings)** | R1: 3.5 | R2: 3.0
- 圆桌 1 轮即达成收敛（7/10 共识，2 个 legitimate divergence）
- 4 个 Critical issues: novelty 有限(W1)、无实际加速(W2)、downstream 系统性退步(W3)、gradient coupling 因果不完整(W4)
- 3 个 Major issues: MSE 单 seed(W5)、actual sparsity mismatch(W6)、seed mask divergence 未报告(W7)
- Issue Tracker 已同步更新（R18-W1 至 R18-M1，共 10 条新 issue）
- 外部审稿仍 pending，视觉审查因配额耗尽失败
- 升档路径：per-layer KL ablation + reverse KL downstream + cross-seed mask Jaccard

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 126

## Round 126

56 recorded events


### User

_source line 1487 · 2026-05-22T08:21:36.062856+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

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

_source line 1488 · 2026-05-22T08:21:44.692383+00:00_

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

_source line 1489 · 2026-05-22T08:21:44.843753+00:00_

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
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-22T08:21:46.602623+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1491 · 2026-05-22T08:21:46.602967+00:00_

No matching deferred tools found

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

_source line 1492 · 2026-05-22T08:21:54.334402+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1493 · 2026-05-22T08:21:54.385118+00:00_



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

_source line 1494 · 2026-05-22T08:22:00.563609+00:00_

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

_source line 1495 · 2026-05-22T08:22:01.969569+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (364 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\n\n## 待处理\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\n- perlayer_kl_50_s42_boolq（准备中）\n- perlayer_kl_50_s42_ppl（准备中）\n- qwen14b_kl30_s42_gsm8k_uniform（准备中）\n- revkl_30_s42_boolq_uniform（准备中）\n- diag_eval_env_34887（准备中）\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\n- diag_status_34887（准备中）\n- diag_status_41718（准备中）\n- read_boolq_results（准备中）\n- …另有 41 项\n\n## 近期结论\n- **perlayer_kl_50_s42_downstream** (negative): Per-layer KL distillation at 50% sparsity will produce
…[truncated 1781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-22T08:22:02.472185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "80"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-22T08:22:03.030684+00:00_

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
  "elapsed_ms": 558
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-22T08:22:03.031180+00:00_

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

_source line 1499 · 2026-05-22T08:22:03.031433+00:00_



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

_source line 1500 · 2026-05-22T08:22:04.990827+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-22T08:22:05.193539+00:00_

-rw-r--r-- 1 ubuntu ubuntu 520682 May 22 08:10 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-22T08:22:12.403596+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-22T08:22:13.421812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit format"
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
    "query": "ACL Rolling Review 2026 author guidelines page limit format"
  }
}
```

</details>

---


### Tool call

_source line 1504 · 2026-05-22T08:22:13.893889+00:00_

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

_source line 1505 · 2026-05-22T08:22:14.381105+00:00_

1	Learned sparsity predictors for SwiGLU LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation confirms these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	A coupling alignment hierarchy emerges across five loss configurations; a per-layer KL control decomposes this hierarchy into two dimensions: output-distribution alignment drives PPL (per-layer KL within 3\% of end-to-end at 30\% sparsity), while cross-layer coupling provides additional downstream benefit (3--4\,pp on ARC-Challenge and WinoGrande).
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 487
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-22T08:22:14.381562+00:00_

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

_source line 1507 · 2026-05-22T08:22:15.337745+00:00_

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
12	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Cross-lay
…[truncated 2933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-22T08:22:15.489309+00:00_

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


### Tool call

_source line 1509 · 2026-05-22T08:22:15.489750+00:00_

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

_source line 1510 · 2026-05-22T08:22:15.540499+00:00_

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
…[truncated 9558 chars]

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


### Tool result

_source line 1511 · 2026-05-22T08:22:15.541363+00:00_

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
…[truncated 18174 chars]

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


### Tool result

_source line 1512 · 2026-05-22T08:22:19.957778+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit format"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL Rolling Review 2026 author guidelines:

**Page Limits:**
The search results reference different page limits depending on the paper type. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Format Requirements:**
The paper follows ACL formatting. You are encouraged to use the ACL pubcheck tool to check for common problems. Additionally, there is an official Overleaf template. Note that this template has a [review] setting that must be on for the submissio
…[truncated 773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6535
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-22T08:22:20.560760+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key EMNLP 2026 call for papers submission guidelines related to ARR:

## Paper Types and Scope
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process
Papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.

## Important Dates
Key dates include: ARR submiss
…[truncated 828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 8157
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-22T08:22:28.694760+00:00_

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

_source line 1515 · 2026-05-22T08:22:29.247323+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
16	Dhar et al.~\cite{dhar2025clustering} compress activation patterns via clustering for effici
…[truncated 4852 chars]

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

_source line 1516 · 2026-05-22T08:22:29.247696+00:00_

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

_source line 1517 · 2026-05-22T08:22:29.750131+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Coupling alignment---optimizing through the output distribution---is the dominant design dimension for learned sparsity: signal type accounts for 97.5\% of the PPL gap at 30\% sparsity, while cross-layer coupling contributes downstream fidelity (3--4\,pp on ARC-c, WinoGrande).
5	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\%, with KL-discovered masks (46--68\% divergent from magnitude) driving inference quality; however, downstream transfer is task- and scale-dependent.
6	Future work includes N:M structured sparsity and scaling to 70B+.
7	

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

_source line 1518 · 2026-05-22T08:22:29.750500+00:00_

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

_source line 1519 · 2026-05-22T08:22:30.202522+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 10.76 but MMLU already degrades to 35.5\% (vs.\ 40.7\% at 30\%); 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B (3-seed), KL improves PPL ($-$17.3\%) and commonsense tasks (WG, HS, PIQA: all seeds win) but MMLU is tied (43.3\% vs.\ 43.5\%) and GSM8K reverses across all seeds (7.0--11.1\% vs.\ TEAL 15.9\%). ARC-c is seed-dependent (37.8--50.1\% vs.\ TEAL 41.1\%; $\sigma$=6.4pp vs.\ LLaMA-8B's 2.5pp), indicating reduced cross-architecture metric stability. Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$20pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 52.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Training data is domain-homogeneous: all predictors are trained on WikiText-103 (English Wikipedia), a single-domain corpus.
8	Activation importance patterns may differ on code, multilingual, or dialogue data; the predictor could underperform on domains with substantially different neuron utilization profiles.
9	Out-of-distribution evaluation on C4 (Appendix~\ref{app:oo
…[truncated 1919 chars]

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

_source line 1520 · 2026-05-22T08:22:30.303386+00:00_

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

_source line 1521 · 2026-05-22T08:22:30.705328+00:00_

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
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-22T08:22:30.705735+00:00_

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

_source line 1523 · 2026-05-22T08:22:31.660139+00:00_

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
…[truncated 30676 chars]

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

_source line 1524 · 2026-05-22T08:22:31.861889+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-22T08:22:31.964427+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-22T08:22:39.487810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -5 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ -maxdepth 2 -name \"config*\" 2>/dev/null",
  "description": "Find project config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -5 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ -maxdepth 2 -name \"config*\" 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-22T08:22:40.140961+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/’: No such file or directory
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.git/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/R-Sparse/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-22T08:22:40.393187+00:00_

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

_source line 1529 · 2026-05-22T08:22:40.494542+00:00_

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
…[truncated 20404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-22T08:22:51.793225+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/ -maxdepth 1 -name \"config*\" -o -name \"*.yaml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/constraints.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check for external review config"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/ -maxdepth 1 -name \"config*\" -o -name \"*.yaml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/constraints.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-22T08:22:52.747772+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/workspace.yaml
---
NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-22T08:22:53.300739+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-22T08:22:53.803664+00:00_

issues:
  # ============================================================
  # Round 18 (fresh) — Active issues
  # ============================================================

  - id: "R18-W1"
    summary: "方法论新颖性有限: 核心 KL+Gumbel 训练配方与 MaskLLM 高度重合，区别仅在 application level"
    category: method
    severity: critical
    status: open
    first_raised_round: 18
    last_seen_round: 18
    mentions:
      - {round: 18, reviewers: [2], note: "R2-W1 Major. 核心配方 (frozen backbone + learnable masks + KL + Gumbel) 与 MaskLLM 重合. 三点区别均为 application-level. 作为 empirical study 达 Findings bar, 但 main conference 需更多方法论贡献."}
      - {round: 18, reviewers: [1], note: "交叉回应: AGREE with nuance. Application differences 非完全 trivial (per-token + global top-k 产生长距离依赖), 但方法论新颖性确实有限."}
    action_items:
      - {round: 18, action: "分歧记录. R2 认为 novelty 不足以进 main conference; R1 认为 empirical contributions 可能 borderline. 无法通过补实验解决.", assigned_to: "research_director", status: open}
    resolution: ""
    resolution_round: null

  - id: "R18-W2"
    summary: "无实际推理加速: pipeline 增加 6.4% 延迟, unstructured masks 无法转化为 wall-clock speedup"
    category: experiment
    severity: critical
    status: open
    first_raised_round: 18
    last_seen_round: 18
    mentions:
      - {round: 18, reviewers: [1, 2], note: "[AGREE] 共识. R1-W1 Critical + R2-W4 Minor. Appendix A Table 6 实测 +6.4% overhead. 论文已定位为 empirical study 但 Introduction 开篇仍以 efficiency 动机展开, 存在 framing 张力."}
    action_items:
      - {round: 18, action: "检查 Introduction 开篇是否仍暗示 efficiency 收益, 考虑进一步弱化 efficiency framing 或提供 block-sparse prototype.", assigned_to: "research_director", status: open}
    resolution: ""
    resolution_round: null

  - id: "R18-W3"
    summary: "Knowledge-intensive tasks 系统性退步: MMLU -5.2pp (8B), GSM8K -20pp (14B), 跨三个模型一致"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 18
    last_seen_round: 18
    mentions:
      - {round: 18, reviewers: [1, 2], note: "[AGREE] 共识. R1-W2 
…[truncated 14466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-22T08:22:53.955409+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review reports"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-22T08:22:54.006173+00:00_

round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_14.md
round_15.md
round_16.md
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-22T08:23:26.758859+00:00_

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

_source line 1537 · 2026-05-22T08:23:48.085213+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21326
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-22T08:23:49.741676+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验评估**。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 目标 venue: EMNLP 2026 (Long Paper, ARR May cycle)\n- Deadline: 2026-05-25\n- 格式: ACL review 模板, double-blind, 正文 ≤ 8页, 参考文献不限, Limitations/Ethics 不计入页数\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf\n\n## 你的审查侧重\n\n1. **方法论严谨性**:\n   - KL distillation 框架的数学正确性（§3.4 KL loss, §3.3 Gumbel-Sigmoid, §3.5 Lagrangian）\n   - Gradient analysis (§3.6): BCE vs KL 梯度结构对比是否准确，\"suggestive\" 标注是否足够 hedge overclaiming\n   - Per-layer KL decomposition (§4.5): signal type vs coupling scope 的 2D 分解是否合理，97.5% 归因是否有 confound\n   - Target-swap ablation (C1, §4.4): 是否充分隔离 mask quality vs gradient coupling\n\n2. **实验评估**:\n   - 多种子覆盖: 哪些结果有 3-seed 统计，哪些仅 single seed，是否有 cherry-picking 风险\n   - Baseline 公平性: BCE 2700 steps vs KL 1000 steps 的 isocompute 比较是否合理\n   - Actual sparsity 不匹配: KL 28.5% vs TEAL 29.3% at 30% target，对 headline comparison 的影响\n   - MSE baseline: 3-seed 含 failed seed (PPL=15789) 的报告方式是否恰当\n   - 14B scale 结果: 仅 30% sparsity, GSM8K 大幅退步 (32.1±5.2% vs dense 52.1%)，实验覆盖是否充分\n   - Knowledge-intensive tasks 系统性退步: MMLU -5.2pp (8B), GSM8K -20pp (14B)\n\n3. **技术细节**:\n   - Compensation redundancy claim 是否有充分证据\n   - OOD evaluation: C4 结果和 variance 增大 (CV 0.2%→6.3%)\n   - 延迟分析: +6.4% overhead 但无 wall-clock speedup\n\n请按 ARR reviewer guidelines 输出完整审稿意见，包含: Summary, Strengths (逐条), Weaknesses (逐条, 标注 Critical/Major/Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP guidelines)。",
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验评估**。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 目标 venue: EMNLP 2026 (Long Paper, ARR May cycle)\n- Deadline: 2026-05-25\n- 格式: ACL review 模板, double-blind, 正文 ≤ 8页, 参考文献不限, Limitations/Ethics 不计入页数\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf\n\n## 你的审查侧重\n\n1. **方法论严谨性**:\n   - KL distillation 框架的数学正确性（§3.4 KL loss, §3.3 Gumbel-Sigmoid, §3.5 Lagrangian）\n   - Gradient analysis (§3.6): BCE vs KL 梯度结构对比是否准确，\"suggestive\" 标注是否足够 hedge overclaiming\n   - Per-layer KL decomposition (§4.5): signal type vs coupling scope 的 2D 分解是否合理，97.5% 归因是否有 confound\n   - Target-swap ablation (C1, §4.4): 是否充分隔离 mask quality vs gradient coupling\n\n2. **实验评估**:\n   - 多种子覆盖: 哪些结果有 3-seed 统计，哪些仅 single seed，是否有 cherry-picking 风险\n   - Baseline 公平性: BCE 2700 steps vs KL 1000 steps 的 isocompute 比较是否合理\n   - Actual sparsity 不匹配: KL 28.5% vs TEAL 29.3% at 30% target，对 headline comparison 的影响\n   - MSE baseline: 3-seed 含 failed seed (PPL=15789) 的报告方式是否恰当\n   - 14B scale 结果: 仅 30% sparsity, GSM8K 大幅退步 (32.1±5.2% vs dense 52.1%)，实验覆盖是否充分\n   - Knowledge-intensive tasks 系统性退步: MMLU -5.2pp (8B), GSM8K -20pp (14B)\n\n3. **技术细节**:\n   - Compensation redundancy claim 是否有充分证据\n   - OOD evaluation: C4 结果和 variance 增大 (CV 0.2%→6.3%)\n   - 延迟分析: +6.4% overhead 但无 wall-clock speedup\n\n请按 ARR reviewer guidelines 输出完整审稿意见，包含: Summary, Strengths (逐条), Weaknesses (逐条, 标注 Critical/Major/Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP guidelines)。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-22T08:24:06.371551+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16629
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-22T08:24:07.083244+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 格式合规**。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 目标 venue: EMNLP 2026 (Long Paper, ARR May cycle)\n- Deadline: 2026-05-25\n- 格式: ACL review 模板, double-blind, 正文 ≤ 8页, 参考文献不限, Limitations/Ethics 不计入页数\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf\n\n## 你的审查侧重\n\n1. **新颖性评估**:\n   - 核心配方 (frozen backbone + learnable masks + KL + Gumbel) 与 MaskLLM 的重合度: §2 给出三点区分 (sparsity type, mask generation, allocation)，评估这些区分是否足够构成 novelty\n   - 作为 empirical study 的 contribution 是否达到 EMNLP main conference bar: 2D decomposition (signal type × coupling scope) 是否是 novel insight\n   - Target-swap ablation (C1) 是否足够原创性\n   - 与 ShadowLLM/D2DMoE/FastForward 的定位差异\n\n2. **Related Work 完整性**:\n   - 近期 activation sparsity 文献覆盖: R-Sparse (ICLR 2025), DIP (MLSys 2024), SparseInfer (DATE 2025), Polar Sparsity (NeurIPS 2025), MoNE, Expert Choice, D2D-MoE 等是否已充分讨论\n   - 是否有重要遗漏: 特别关注 2025-2026 新发表的相关工作\n   - 引用格式一致性和完整性\n\n3. **叙事一致性和 Framing**:\n   - Introduction 的 efficiency 动机 vs 实际无 wall-clock speedup 的 framing 张力\n   - \"coupling alignment hierarchy\" / \"2D decomposition\" 叙事是否 overclaim\n   - Abstract 的 headline numbers 是否准确反映实验结果\n   - Contribution list 的 strength 是否与证据匹配\n\n4. **格式合规 (EMNLP 2026)**:\n   - 正文是否 ≤ 8 页（不含 Limitations/Ethics/References/Appendix）\n   - Anonymous 规则: 是否有自引泄露身份\n   - ACL template 格式是否正确\n   - Limitations 和 Ethics 章节是否存在且合理\n   - Responsible NLP Checklist 注意: 这是在 OpenReview submission form 里填写的，不应出现在论文 PDF 中\n\n请按 ARR reviewer guidelines 输出完整审稿意见，包含: Summary, Strengths (逐条), Weaknesses (逐条, 标注 Critical/Major/Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP guidelines)。",
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 格式合规**。\n\n## 论文信息\n- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- 目标 venue: EMNLP 2026 (Long Paper, ARR May cycle)\n- Deadline: 2026-05-25\n- 格式: ACL review 模板, double-blind, 正文 ≤ 8页, 参考文献不限, Limitations/Ethics 不计入页数\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf\n\n## 你的审查侧重\n\n1. **新颖性评估**:\n   - 核心配方 (frozen backbone + learnable masks + KL + Gumbel) 与 MaskLLM 的重合度: §2 给出三点区分 (sparsity type, mask generation, allocation)，评估这些区分是否足够构成 novelty\n   - 作为 empirical study 的 contribution 是否达到 EMNLP main conference bar: 2D decomposition (signal type × coupling scope) 是否是 novel insight\n   - Target-swap ablation (C1) 是否足够原创性\n   - 与 ShadowLLM/D2DMoE/FastForward 的定位差异\n\n2. **Related Work 完整性**:\n   - 近期 activation sparsity 文献覆盖: R-Sparse (ICLR 2025), DIP (MLSys 2024), SparseInfer (DATE 2025), Polar Sparsity (NeurIPS 2025), MoNE, Expert Choice, D2D-MoE 等是否已充分讨论\n   - 是否有重要遗漏: 特别关注 2025-2026 新发表的相关工作\n   - 引用格式一致性和完整性\n\n3. **叙事一致性和 Framing**:\n   - Introduction 的 efficiency 动机 vs 实际无 wall-clock speedup 的 framing 张力\n   - \"coupling alignment hierarchy\" / \"2D decomposition\" 叙事是否 overclaim\n   - Abstract 的 headline numbers 是否准确反映实验结果\n   - Contribution list 的 strength 是否与证据匹配\n\n4. **格式合规 (EMNLP 2026)**:\n   - 正文是否 ≤ 8 页（不含 Limitations/Ethics/References/Appendix）\n   - Anonymous 规则: 是否有自引泄露身份\n   - ACL template 格式是否正确\n   - Limitations 和 Ethics 章节是否存在且合理\n   - Responsible NLP Checklist 注意: 这是在 OpenReview submission form 里填写的，不应出现在论文 PDF 中\n\n请按 ARR reviewer guidelines 输出完整审稿意见，包含: Summary, Strengths (逐条), Weaknesses (逐条, 标注 Critical/Major/Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP guidelines)。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-22T08:24:08.744059+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1660
}
```

</details>

---


### Assistant

_source line 1542 · 2026-05-22T08:24:18.336755+00:00_

已派发:
- **视觉审查 Agent**: 已启动 (fire-and-forget)
- **Reviewer 1** (方法严谨性 + 实验评估): 已分配
- **Reviewer 2** (新颖性 + 完整性 + 格式): 已分配

等待两位 Reviewer 返回独立审稿意见后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1543 · 2026-05-22T08:30:33.041636+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)

---

## Summary

本文提出用 forward KL divergence 替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的上下文稀疏性预测器。核心 insight 是：BCE 将每个神经元的激活视为独立二分类问题，梯度不跨层耦合；而 KL 在输出分布层面优化，通过完整前向传播产生耦合梯度，使预测器发现与 magnitude-based oracle 有 46–68% 差异的 mask patterns。在 LLaMA-3.1-8B 和 Qwen-2.5-14B 上，KL 在 30% 稀疏度下 PPL 优于 TEAL 14.5%（matched sparsity），并在多数下游任务上保持竞争力。论文通过 target-swap ablation (C1)、per-layer KL decomposition 等消融实验分析了 KL 优势的来源。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 KL 框架数学正确；但 97.5% signal-type 归因基于 PPL 而非下游指标，C1 ablation 存在循环论证，削弱了分析叙事的可信度 |
| Excitement | 2.5/5 | 研究问题有意义（BCE 独立性限制），但无实际加速、knowledge-intensive 任务退步显著，实用影响有限 |
| Reproducibility | 4/5 | 超参数详细、主实验有 3-seed 统计、训练细节完整；代码未提供但可根据描述复现 |
| Overall Assessment | **3.0** (Findings) | 实证贡献扎实但分析叙事有关键缺口，且缺乏实际加速验证 |
| Reviewer Confidence | 4/5 | 熟悉 contextual sparsity、知识蒸馏和 SwiGLU 架构相关工作 |

---

## 主要优势

**S1. 研究问题清晰且有意义。** BCE 将每个神经元独立处理的局限性是 contextual sparsity 文献中一个被忽视的问题。用 output-distribution distillation 替代 per-neuron classification 是一个自然且有价值的研究方向。

**S2. 消融设计系统且深入。** C1 target-swap ablation（§4.4）、per-layer KL decomposition（§4.5/§3.7）、4 种 loss 变体对比（Table 4）、relaxation 方法对比（Gumbel vs STE）形成了较完整的消融体系。

**S3. 梯度分析的 hedging 恰当。** §3.6 将 BCE vs KL 梯度结构对比标注为"suggestive"，未过度声称理论因果关系，而是用实验（§4.4）提供支撑证据。这种诚实的表述值得肯定。

**S4. 训练效率优势明确。** KL 在 1000 steps 达到的效果优于 BCE 2700 steps（§4.3, PPL 11.79 vs 28.13），且 wall-clock 时间相当（~45 min），这是一个有实用价值的发现。

**S5. 附录内容充实。** 19 个附录覆盖了 inference latency（App A）、bottleneck sensitivity（App B）、temperature schedule（App B.1）、training convergence（App B.2）、penalty controller dynamics（App C）、OOD evaluation（App D）等，增强了可复现性。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **97.5% signal-type 归因与下游指标矛盾，叙事有误导风险**
- 具体位置：§3.7（page 5）及 §4.5（page 8）
- 问题：论文声称"signal type accounts for 97.5% of the PPL gap"（§3.7），但紧接着承认"cross-layer coupling contributes downstream benefit (1–4pp on ARC-Challenge and WinoGrande)"以及"per-layer KL underperforms end-to-end KL by 5–8pp on commonsense tasks"（§4.5）。这意味着 coupling scope 对下游任务的贡献远超 2.5%，但论文的主叙事（包括 abstract 和 conclusion）反复强调 97.5% 这个数字，可能给读者造成"coupling 不重要"的错误印象。
- 为什么影响接收：论文的核心分析框架（signal type vs coupling scope 的 2D 分解）假设这两个因素可加性分解且 PPL 是充分代理指标。但下游指标显示非加性交互存在。这不是小的表述问题，而是分析叙事的核心主张与自身实验证据之间的不一致。
- 建议修改方向：(1) 在 abstract/conclusion 中明确 97.5% 仅适用于 PPL，下游指标显示 coupling 贡献更大；(2) 补充下游指标的 2D 分解定量结果（不仅是 1–4pp 的定性描述）；(3) 讨论 PPL 作为代理指标的局限性。

**N2** [critical] **C1 target-swap ablation 的循环论证未充分讨论**
- 具体位置：§4.4（page 7）, Table 3
- 问题：C1 将 KL 发现的 masks 交给 BCE 训练，结果 BCE 也能获得接近 KL 的 PPL。论文将此解释为"mask quality is the proximate driver, not gradient coupling"。但这些 masks 恰恰是由 KL 的耦合梯度发现的——如果没有 KL 训练，这些 mask targets 根本不存在。因此 C1 证明的是"KL-derived masks transferable to BCE"，而非"coupling 不重要"。
- 为什么影响接收：这个 ablation 是论文因果分析链的关键环节。如果 C1 的解释存在循环（KL 的贡献被归结为 mask quality，但 mask quality 来自 KL 的 coupling），那么论文关于"what matters"的核心结论需要重新审视。
- 建议修改方向：(1) 明确讨论这个循环性：C1 证明了 mask 的 transferability，但 KL 的 coupling 是发现这些 masks 的必要条件；(2) 补充反向实验——能否用其他方法（如 evolutionary search、random perturbation）找到同等质量的 masks？如果只有 KL 能发现，则 coupling 的贡献不可被 C1 消解。

**N3** [critical] **无实际 wall-clock 加速，实用价值存疑**
- 具体位置：§4.6（page 8）, Appendix A（page 13）, Limitations（page 9）
- 问题：Table 5 显示 KL-sparse pipeline 增加 +6.4% latency overhead，但没有任何 wall-clock speedup 结果。论文承认"wall-clock speedup requires sparse kernel support not yet implemented here"（Limitations, page 9）。对于一篇 contextual sparsity 方法论文，缺乏实际加速验证是重大缺陷。
- 为什么影响接收：Sparsity 的唯一目的是推理加速。即使论文自我定位为"analytical understanding"（Limitations），但 abstract 和 introduction 均以"inference-free activation sparsity"和"lightweight predictor"作为 motivation，暗示实用价值。如果无法展示加速，读者无法判断改进的 mask quality 是否有实际意义。
- 建议修改方向：(1) 至少提供 Triton/cuSPARSE 的概念验证 speedup 数字，即使不完整；(2) 如果无法提供，在 abstract 和 introduction 中显著弱化 practical motivation，明确声明这是一项分析性研究。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **14B 实验覆盖不足，GSM8K 退步严重且缺乏对比**
- 具体位置：Table 13（page 16），§4.6（page 8）
- 问题：14B（Qwen-2.5-14B）仅在 30% sparsity 下有完整下游评估。GSM8K 从 dense 52.1% 降至 32.1±5.2%（−20pp），高 seed variance（±5.2）暗示不稳定性。但论文未给出 TEAL 在 14B 上的 GSM8K 对比，无法判断这是 KL 方法的问题还是 contextual sparsity 的通病。Table 16（page 18）有 cross-architecture 结果但同样仅 30%。
- 建议：(1) 补充 TEAL 在 14B 上的完整下游指标对比；(2) 补充 14B 50% sparsity 的下游结果（HellaSwag/PIQA 已有，缺其他指标）；(3) 讨论 GSM8K 高 variance 的原因。

**W2** [major] **Knowledge-intensive 任务系统性退步缺乏机制解释**
- 具体位置：Table 2（page 6），Limitations（page 9）
- 问题：8B 30% sparsity 下 MMLU −5.2pp（Table 2, KL global vs dense），14B 30% GSM8K −20pp。论文在 Limitations 中承认"KL's mass-covering property may preserve output quality at the expense of reasoning-critical pathways"，但这是推测性的一句话，缺乏任何分析证据。
- 建议：(1) 分析 knowledge-intensive tasks 上 per-layer mask 差异是否与 attention/FFN 的 knowledge storage 层相关；(2) 讨论 forward KL 的 mode-covering 特性是否系统性地牺牲了低频但重要的 knowledge patterns。

**W3** [major] **MSE baseline 的 failed seed 报告方式不透明**
- 具体位置：Table 4（page 7）
- 问题：Per-layer MSE 在 50% sparsity 下达到 PPL 229.26（Table 4），远超正常范围。Appendix G 提到"3-seed, with seed 123, ... random-level, indicating high sensitivity to initialization—a failure mode not observed with KL-based losses"。如果 3 个 seeds 中有一个 catastrophic failure（如 PPL=15789 在某处提到），在 mean±std 中报告会严重扭曲统计。论文应明确每个 seed 的值并讨论 failure mode。
- 建议：(1) Table 4 中标注哪些 entries 包含 failed seeds；(2) 分别报告 median 和 mean，或排除 failed seeds 后单独报告。

**W4** [minor] **OOD variance 增大 (CV 0.2%→6.3%) 需更多讨论**
- 具体位置：Appendix D（page 14）, Limitations（page 9）
- 问题：C4 上 cross-seed PPL variance 的 coefficient of variation 从 in-domain 的 0.2% 增至 6.3%。虽然绝对 PPL（16.03）仍合理，但 30× 的 variance 增幅暗示 KL predictor 可能对 domain shift 敏感。论文仅简单提到"the predictor partially overfits to training-domain activation patterns"但未深入分析。
- 建议：分析哪些层的 mask patterns 在 OOD 时变化最大，以及这是否与 per-layer allocation budget 的 non-monotonic behavior 相关。

**W5** [minor] **Actual sparsity mismatch 的讨论虽在附录但不够显著**
- 具体位置：Table 2 footnote（page 6），Appendix D（page 14）
- 问题：KL 在 30% target 下实际只达到 28.5%（vs TEAL 29.3%）。虽然 Appendix D 有 matched-sparsity 对比，但主表（Table 2）的 headline comparison 使用了不同实际稀疏度下的数字。论文 abstract 的"14.5% over TEAL"使用了 matched-sparsity 数字，这一点没有在 abstract 中说明。
- 建议：在 Table 2 中直接标注各方法的实际稀疏度，而非仅用脚注。

---

## 小问题（不影响接收）

- §3.4 Eq.(5): 符号 $p_{\text{dense}}$ 和 $p_{\text{sparse}}$ 在引入前建议先定义清楚，当前定义在 Eq.(5) 下方的段落中出现，但 Eq.(5) 本身先用了这些符号。
- Figure 2（page 8）: y 轴标签"PPL↓"但图中值越高越差，建议标注为"PPL"（不加箭头）或使用 log scale 让差异更明显。
- Table 1（page 5）: 该 taxonomy table 信息密度高，但"Per-token × Coupled cell"仅由本文占据，可能暗示 positioning 过于强调 novelty 而非实质差异。
- Limitations 中提到"scaling to 70B remains untested"——建议明确这是由于计算资源限制还是方法论障碍。

---

## Questions for Authors

**Q1.** 你们在 §4.5 的 2D 分解中能否提供下游指标（ARC, MMLU, WinoGrande）的定量分解结果？这对于评估 97.5% 归因的适用范围至关重要。

**Q2.** C1 ablation 中，BCE 使用 KL-derived masks 作为 target 训练时，是否也使用了 Gumbel-Sigmoid relaxation？如果 C1 只用了 hard threshold，那么 C1 和 KL 之间的差异可能部分来自 relaxation method 而非 mask quality。

**Q3.** 对于 14B 上 GSM8K 的 −20pp 退步和 ±5.2 的高 seed variance，你们是否分析过是哪些层的 masks 在不同 seeds 间差异最大？这可能揭示 reasoning 能力退化的机制。

**Q4.** 是否有证据表明其他方法（如 evolutionary search 或 gradient-free optimization）能发现与 KL 类似质量的 masks？如果有，则 C1 的"mask quality > coupling"结论更强；如果没有，则说明 coupling 是 mask discovery 的必要条件。

**Q5.** Compensation network 被声称为 redundant（+67.2M params），但在 capacity-limited regime（§4.6 提到的 ≤45% sparsity），compensation 是否可能变得必要？

---

## Missing References

- **PowerInfer** (Song et al., 2024b) 已引用，但 **PowerInfer-2**（Xue et al., 2024）的 on-device sparsity work 可能相关。
- **Wanda** (Sun et al., 2024) 的 structured pruning 方法与本文的 unstructured contextual sparsity 有方法论对比价值。
- **ReLU-fication** literature（如 Mirzadeh et al., 2024 已引用）中关于 SwiGLU 到 ReLU 转换后天然 sparsity 的分析，可与本文"SwiGLU 无天然稀疏性"的假设对比。

---

## Overall Assessment

**Overall: 3.0 (Findings)**

**一句话总结：** 论文提出了一个有价值的研究问题并提供了系统的实证分析，但核心归因框架（97.5% signal-type）与自身下游指标矛盾、C1 ablation 存在循环论证、且完全缺乏实际加速验证，使其分析叙事和实用贡献均有关键缺口。

该论文的实证贡献——KL distillation 系统性优于 BCE 用于 sparsity prediction training——是可靠的，值得发表。但以下因素限制了其达到 Conference 水准：

1. **分析叙事断裂**：97.5% 归因是论文最吸引人的 claim，但仅基于 PPL，与下游指标矛盾（5–8pp coupling 贡献被 97.5% 掩盖）。如果这个 claim 得到修正和扩展（补充下游指标的定量分解），论文会显著更强。

2. **因果推断链有缺口**：C1 ablation 的循环论证（KL 发现的 masks → BCE 也能用 → 所以 mask quality 比 coupling 重要，但忽略了 KL 是发现这些 masks 的唯一途径）使得论文无法清晰回答"what specifically does KL contribute"。

3. **实用价值未验证**：对于 sparsity 方法论文，缺乏任何 speedup 数据是硬伤。即使自我定位为 analytical study，也应至少提供 proof-of-concept。

**推荐：Findings 接收**——实证发现有价值，但分析叙事需要实质性修正才能达到 Conference 水平。

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

_source line 1544 · 2026-05-22T08:30:40.033373+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 128

## Round 128

2 recorded events


### User

_source line 1545 · 2026-05-22T08:30:43.609586+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心评价**：Overall 3.0 (Findings)。

三个 critical issues：
1. **97.5% signal-type 归因与下游指标矛盾** — coupling scope 对下游任务贡献远超 PPL 暗示的 2.5%，但论文叙事反复强调 97.5%
2. **C1 target-swap ablation 循环论证** — KL-derived masks 交给 BCE 也能用 ≠ coupling 不重要，因为这些 masks 只有 KL 的 coupled gradients 才能发现
3. **完全缺乏 wall-clock speedup** — 一篇 sparsity 方法论文没有任何加速数据

三个 major issues：14B 评估不足（GSM8K −20pp 且缺 TEAL 对比）、knowledge-intensive 退步缺机制解释、MSE failed seed 报告不透明。

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

_source line 1546 · 2026-05-22T08:30:48.520284+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 129

## Round 129

6 recorded events


### User

_source line 1547 · 2026-05-22T08:30:50.026805+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## Paper Summary

本文研究将 KL 散度蒸馏（配合 Gumbel-Sigmoid 松弛）应用于训练 SwiGLU LLM 的上下文稀疏性预测器，替代传统的 BCE 损失。在 LLaMA-3.1-8B 上，作者通过大量消融实验建立了"coupling alignment hierarchy"：output-distribution 损失（KL/JSD）在 PPL 上主导，cross-layer coupling 对 downstream task 有额外贡献。KL 预测器在 30% 稀疏度下将 TEAL 的 PPL 降低 14.5%，发现的 mask pattern 与 magnitude-based 方法有 46-68% 的偏离。target-swap ablation (C1) 证明 mask 质量（而非梯度耦合机制本身）是推理质量的近端驱动因素。补偿网络 (+67.2M 参数) 变得冗余。跨架构评估在 Mistral-7B 上 PPL 泛化，但在 Qwen-2.5-14B 上出现 MMLU/GSM8K 下降。

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 扎实的 empirical study，消融设计精巧，但核心方法配方与 MaskLLM 高度重合，缺乏 wall-clock speedup 验证，新颖性不足以支撑主会议接收。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 消融设计合理（C1 target-swap、per-layer KL），实验控制变量严格（同架构/数据/优化器仅改损失），3-seed 评估。但 per-layer KL 实验存在 train-inference distribution shift confound（§4.5 自认），14B 结果与核心叙事矛盾 |
| Excitement | 2.5/5 | 方法配方（frozen backbone + learnable masks + KL + Gumbel）与 MaskLLM 核心相同，应用到 activation sparsity 是增量而非突破。无 wall-clock speedup 削弱实际影响力 |
| Reproducibility | 4/5 | 超参数完整报告，GPU 型号、训练步数、seed、评估协议均明确。但代码和 predictor weights 未发布 |
| Reviewer Confidence | 4/5 | 熟悉 activation sparsity、KL distillation、sparse inference 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] 与 MaskLLM 的新颖性区分不足

- 具体位置：§2 Related Work, ¶"Predictor-Based Contextual Sparsity"
- 问题：核心配方 (frozen weights + learnable masks + KL divergence + Gumbel relaxation) 与 MaskLLM (Fang et al., 2024, NeurIPS) 完全一致。论文给出的三点区分——(1) sparsity type (weight vs activation), (2) mask generation (direct params vs predictor network), (3) allocation (N:M vs global top-k)——都是 application-level adaptation，而非 fundamental methodological contribution。尤其是：
  - KL + Gumbel 用于 mask 优化已被 MaskLLM 建立为已知技术
  - 将其应用到 activation sparsity predictor 是直接的工程迁移
  - 论文最核心的 empirical finding（KL 优于 BCE）在 MaskLLM 已经隐含验证（MaskLLM 用 KL 而非 BCE 训练 mask）
- 为什么影响接收：作为 empirical study，论文需要在 insight 层面提供足够 novelty。但"KL 优于 BCE"这一核心 insight 已被 MaskLLM 的方法选择所暗示。论文的附加贡献（2D taxonomy、C1 ablation、coupling hierarchy）有价值但不足以独立撑起 main conference bar。
- 建议修改方向：(a) 更深入地对比 MaskLLM 的 KL 训练在 activation sparsity 设定下的行为差异，最好有实验对比；(b) 明确论文的贡献是 *理解为什么 KL 有效*（via target-swap ablation），而不是 *提出用 KL*；(c) 考虑与 MaskLLM 在 activation sparsity 设定下的直接实验对比（即使 MaskLLM 设计用于 weight sparsity，也可以适配）。

**N2** [Critical] Efficiency motivation 与实际无 wall-clock speedup 的叙事张力

- 具体位置：§1 Introduction, §A Inference Efficiency (Appendix)
- 问题：Introduction 第一段以 "high contextual sparsity" 和 inference efficiency 为动机引入问题，但：
  - Table 5 (Appendix A) 显示该方法增加了 6.4% 推理延迟（126.78 vs 119.11 ms/forward）
  - 论文明确承认 "unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support"
  - 当前的 activation sparsity 无法实际加速推理，使得整个 efficiency motivation 成为空洞的未来愿景
  - 即使引用了 Triton/cuSPARSE，也没有任何 POC 级别的 sparse kernel 加速数据
- 为什么影响接收：读者期望 efficiency 论文展示 efficiency 提升。论文虽在 §1 和 Limitations 中做了 caveat，但 motivation 和 actual contribution 之间的 gap 太大，削弱了论文的实际意义。
- 建议修改方向：(a) 将 framing 从 efficiency 转向"理解 sparsity prediction 的 training objective design space"，这更准确反映论文的贡献；(b) 提供至少一个 sparse kernel 的 proof-of-concept speedup 数据（即使是 block-sparse with Triton 的简单实现）；(c) 或明确将论文定位为 Findings 级别的 analytical contribution。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] 14B 结果与核心叙事矛盾，但在 framing 中被淡化

- 具体位置：§4.6, Table 13 (Appendix K), Limitations
- 问题：在 Qwen-2.5-14B 上：
  - MMLU: KL 63.55% vs TEAL 66.34% (uniform), -2.79pp
  - GSM8K: KL 32.1±5.2% vs TEAL 52.1% (uniform), -20pp，3-seed 方差极高 (σ=5.2pp)
  - 这些 negative results 与论文的核心 narrative（KL 优于 magnitude-based methods）直接矛盾
  - Limitations 中的解释（"task-and-scale-dependent effects"）过于笼统
- 建议：(a) 在主文 §4.6 中给出更具体的失败模式分析，而不是仅引用 Appendix；(b) 讨论 KL 的 mode-covering 特性是否在 larger model 上反而有害（higher capacity → reasoning pathways more structured → magnitude-based selection more appropriate?）；(c) 考虑这是否表明该方法的 applicability 有根本的 scale limitation。

**W2** [Major] Target-swap ablation (C1) 存在 confound，论文承认但未充分处理

- 具体位置：§4.4, Table 3, Appendix P
- 问题：
  - C1 同时改变了 mask 表征（hard vs soft）和 target（magnitude vs KL-derived），虽然 §4.4 的 "Soft-vs-Hard Confound" 段落用 BCE+Gumbel (PPL 32.22) vs BCE (27.97) 试图排除 softness 的影响，但这只排除了 softness *有利于 BCE* 的可能，没有排除 softness 与 KL targets 之间的 interaction
  - 更关键的是：C1 的 oracle masks 来自特定 KL training trajectory（Appendix P 承认），是否另一个 KL 初始化会发现等效 mask 仍是 open question
  - s42 oracle 来自 "earlier training run"（Table 3 footnote），与其他 seed 的 oracle 不匹配，导致 s42 有 0.65pp gap
- 建议：(a) 明确 state C1 的 conclusion 需要 qualification——它证明了 mask quality 的重要性，但不能完全排除 gradient coupling 的额外贡献；(b) 讨论 oracle mask 的 trajectory dependence 对 C1 结论 robustness 的影响。

**W3** [Major] "2D Taxonomy" / "Coupling Alignment Hierarchy" 叙事有 overclaim 风险

- 具体位置：§3.7, Table 1, §1 Contributions
- 问题：
  - Table 1 的 "2D taxonomy" 实质上是一个 2×3 分类表，将已有方法按两个维度分类。这是 useful organizational tool 但不构成 novel insight——任何熟悉该领域的人都能构建类似分类。称之为 "two-dimensional taxonomy" 和论文的核心贡献之一有 overclaim 风格。
  - "Coupling alignment hierarchy" 本质上是"KL > JSD > Reverse KL > BCE > MSE"的实验排序，使用 "hierarchy" 一词过于宏大
  - Contribution list 第一条 "A coupling alignment hierarchy across five losses, decomposed by a per-layer KL control into signal type and coupling scope" 将这个 empirical finding 包装得过于理论化
- 建议：用更朴素的语言描述：如 "we empirically compare five loss functions and find that output-distribution losses consistently outperform intermediate and decomposed losses"。

**W4** [Minor] 30% sparsity "sweet spot" 限制了实际影响

- 具体位置：§4.2, §4.6, Limitations
- 问题：
  - 在 30% 稀疏度下 KL 方法工作良好（PPL 8.81, MMLU 40.7%），但 40% 时 MMLU 已降至 35.5%，50% 时所有方法的 MMLU 都崩溃到接近随机（~28%）
  - 30% 稀疏度 + 无 wall-clock speedup = 实际部署价值非常有限
  - 在唯一展示大幅 PPL 改善的 50% regime，downstream tasks 已经无法使用
- 建议：Limitations 已部分讨论此问题，但建议在主文中更明确地框定 30% 作为 "最小有意义稀疏度"的意义。

---

## 小问题（不影响接收）

- **格式问题 [Minor]**: 论文 PDF 中包含了 "Responsible NLP Research Checklist"（Ethics Statement 后，§C1-E1），但根据 EMNLP 2026 / ARR 提交指南，该 checklist 应仅在 OpenReview submission form 中填写，不应出现在论文 PDF 中。建议删除 PDF 中的 checklist 部分。

- **引用格式一致性**: `\cite` vs `\citealp` 的使用基本一致，但 §1 中 TEAL 的引用使用了 `\citealp`（括号内）而其他地方使用 `\cite`——这是风格选择不算错误，但建议统一。

- **Table 2 的 footnote 过于密集**: Table 2 的 caption 包含了大量 footnote 标记（†, ‡, *, ±），信息密度过高，降低了可读性。建议将部分解释移到正文或单独的 note。

- **Abstract 中 "post-hoc compensation (+67.2M params) becomes redundant" 可能误导**: 读者可能理解为"其他方法的补偿网络可以去掉"，但实际上论文比较的是自己方法加不加补偿——这个表述需要更清晰。

---

## Questions for Authors

1. **与 MaskLLM 的实验对比**: 是否考虑过将 MaskLLM 的 approach 适配到 activation sparsity setting 进行直接对比？即使 MaskLLM 设计用于 N:M weight sparsity，将其 direct learnable mask + KL 框架应用到 per-token activation selection 应该是 feasible 的。这将更清楚地展示 predictor network 相对于 direct mask parameters 的优势。

2. **14B GSM8K 逆转的根因**: GSM8K 在 14B 上 KL 比 TEAL 差 20pp (32.1% vs 52.1%)。作者假设这是因为 "reasoning-critical pathways that magnitude pruning preserves more robustly"——是否有更具体的 evidence？例如：是否分析了 14B 上 KL-discovered masks 与 magnitude masks 在特定层（如晚期层）的偏离度与 GSM8K 性能的相关性？

3. **Training data diversity**: 所有 predictor 在 WikiText-103 上训练。是否测试过在更多样化的数据（如 C4 子集、code 数据）上训练时，downstream transfer 是否改善？尤其是 MMLU 这种 knowledge-intensive task 可能需要更广泛的 activation pattern 覆盖。

4. **Per-layer KL 的 confound**: §4.5 承认 per-layer KL 实验引入了 train-inference distribution shift（训练时每步仅 mask 一层，推理时同时 mask 32 层）。是否考虑过其他设计来隔离 coupling scope——如训练时 mask K 层（K < 32）的 curriculum？

---

## Missing References

Related work 覆盖较为全面，以下可考虑补充但非必须：

1. **Activation-aware Weight Quantization** (AWQ, Lin et al., 2024, MLSys) — 虽然是量化方法，但其 activation-aware channel selection 与本文的 activation importance scoring 有思路相似性，可在 §2 的 weight pruning 段落中简短提及。

2. 论文已覆盖 R-Sparse, DIP, SparseInfer, Polar Sparsity, MoNE, D2D-MoE, Expert Choice — 所有 Director 指定检查的参考文献均已充分讨论。引用完整性总体良好。

---

## 主要优势

1. **消融设计精巧**: Target-swap ablation (C1) 是 disentangle "what" (mask target quality) vs "how" (gradient coupling mechanism) 的聪明实验设计，即使存在 confound 也提供了有价值的 partial evidence（§4.4, Table 3）。

2. **实验控制严格**: 所有 baseline（KL, BCE, MSE, JSD, RKL）使用相同架构、数据、优化器、Gumbel 松弛参数，仅改变损失函数（§G MSE Baseline Configuration, Appendix），使得 loss function 的效果可以 cleanly 隔离。3-seed 评估贯穿关键实验。

3. **诚实的 negative results 报告**: 14B 的 MMLU/GSM8K 下降、30% 下 global allocation 的高 MMLU 方差（σ=9.5pp）、50% 下 downstream collapse——这些 negative results 在 Limitations 中被充分讨论，展示了学术诚实性（§Limitations, §4.6）。

4. **Per-layer KL control 提供了有价值的分解**: 将 "signal type" 和 "coupling scope" 两个因素分离（97.5% PPL gap 来自 signal type, coupling scope 贡献 downstream fidelity）是有用的 empirical insight（§4.5）。

5. **Related work 覆盖全面**: 对 2024-2026 年的 activation sparsity 文献有广泛覆盖，包括最新的 R-Sparse, DIP, SparseInfer, MoC, SVD-CSP 等（§2）。

---

## 格式合规检查（EMNLP 2026）

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✅ 通过 | §1-5 占 pages 1-8 |
| Anonymous 规则 | ✅ 通过 | Author = "Anonymous ACL submission" |
| ACL template | ✅ 通过 | `\usepackage[review]{acl}` |
| Limitations 章节 | ✅ 通过 | 存在且详细（约 1 页） |
| Ethics Statement | ✅ 通过 | 存在且合理 |
| 无 Responsible NLP Checklist 在 PDF 中 | ❌ 未通过 | Checklist 出现在 PDF §9-10 页，应仅在 OpenReview form 中填写 |
| 自引不泄露身份 | ✅ 通过 | 未发现可识别的自引 |
| 参考文献格式 | ✅ 通过 | 使用 `acl_natbib.bst`，格式一致 |

---

**总结**: 这是一篇执行良好的 empirical study，消融设计值得肯定。但核心方法配方与 MaskLLM 高度重合（KL + Gumbel 用于 mask 优化），无 wall-clock speedup 验证，14B 结果与核心叙事矛盾——这些限制了论文超越 Findings 水平。建议 Overall Assessment = 3.0 (Findings)。


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

_source line 1548 · 2026-05-22T08:31:32.133312+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/小问题，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall Assessment**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [Critical] 与 MaskLLM 的新颖性区分不足\n- 核心配方 (frozen weights + learnable masks + KL divergence + Gumbel relaxation) 与 MaskLLM (Fang et al., 2024, NeurIPS) 完全一致。三点区分——(1) sparsity type (weight vs activation), (2) mask generation (direct params vs predictor network), (3) allocation (N:M vs global top-k)——都是 application-level adaptation。\n- \"KL 优于 BCE\"这一核心 insight 已被 MaskLLM 的方法选择所暗示。论文的附加贡献（2D taxonomy、C1 ablation、coupling hierarchy）有价值但不足以独立撑起 main conference bar。\n\n**N2** [Critical] Efficiency motivation 与实际无 wall-clock speedup 的叙事张力\n- Introduction 第一段以 efficiency 为动机，但 Table 5 显示 +6.4% latency overhead。unstructured masks 无法实际加速推理。motivation 和 actual contribution 之间的 gap 太大。\n\n### Should-Fix 问题\n\n**W1** [Major] 14B 结果与核心叙事矛盾，但在 framing 中被淡化\n- Qwen-2.5-14B: MMLU -2.79pp, GSM8K -20pp (32.1±5.2% vs TEAL 52.1%)。这些 negative results 与论文的核心 narrative（KL 优于 magnitude-based methods）直接矛盾。Limitations 中的解释过于笼统。\n\n**W2** [Major] Target-swap ablation (C1) 存在 confound\n- C1 同时改变了 mask 表征（hard vs soft）和 target（magnitude vs KL-derived）。soft-vs-hard confound 的排除实验只排除了 softness 有利于 BCE 的可能，没有排除 softness 与 KL targets 的 interaction。oracle masks 来自特定 KL training trajectory，trajectory dependence 是 open question。\n\n**W3** [Major] \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" 叙事有 overclaim 风险\n- Table 1 的 \"2D taxonomy\" 实质上是一个 2×3 分类表。称之为论文核心贡献之一有 overclaim。\"Coupling alignment hierarchy\" 本质上是实验排序，使用 \"hierarchy\" 一词过于宏大。\n\n**W4** [Minor] 30% sparsity \"sweet spot\" 限制了实际影响\n- 30% 下 KL 工作良好，但 40% 时 MMLU 降至 35.5%，50% 时 MMLU 崩溃。30% 稀疏度 + 无 speedup = 实际部署价值有限。\n\n### 小问题\n- Responsible NLP Research Checklist 出现在 PDF 中，应仅在 OpenReview form 中填写\n- Table 2 caption footnote 过于密集\n- Abstract 中 \"post-hoc compensation becomes redundant\" 可能误导\n\n### Questions\n1. 是否考虑将 MaskLLM 适配到 activation sparsity setting 直接对比？\n2. 14B GSM8K 逆转的根因有更具体 evidence 吗？\n3. 是否测试过多样化训练数据对 downstream 的影响？\n4. Per-layer KL 的 train-inference distribution shift confound 有其他设计来控制吗？\n\n### Missing References\n- AWQ (Lin et al., 2024, MLSys) 的 activation-aware channel selection 可能相关\n\n### 格式合规\n- Responsible NLP Checklist 在 PDF 中 ❌ 未通过（应仅在 OpenReview form 中填写）\n- 其他所有格式检查均通过\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和小问题逐条给出 [AGREE] 或 [REBUT] 回应。",
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/小问题，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall Assessment**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [Critical] 与 MaskLLM 的新颖性区分不足\n- 核心配方 (frozen weights + learnable masks + KL divergence + Gumbel relaxation) 与 MaskLLM (Fang et al., 2024, NeurIPS) 完全一致。三点区分——(1) sparsity type (weight vs activation), (2) mask generation (direct params vs predictor network), (3) allocation (N:M vs global top-k)——都是 application-level adaptation。\n- \"KL 优于 BCE\"这一核心 insight 已被 MaskLLM 的方法选择所暗示。论文的附加贡献（2D taxonomy、C1 ablation、coupling hierarchy）有价值但不足以独立撑起 main conference bar。\n\n**N2** [Critical] Efficiency motivation 与实际无 wall-clock speedup 的叙事张力\n- Introduction 第一段以 efficiency 为动机，但 Table 5 显示 +6.4% latency overhead。unstructured masks 无法实际加速推理。motivation 和 actual contribution 之间的 gap 太大。\n\n### Should-Fix 问题\n\n**W1** [Major] 14B 结果与核心叙事矛盾，但在 framing 中被淡化\n- Qwen-2.5-14B: MMLU -2.79pp, GSM8K -20pp (32.1±5.2% vs TEAL 52.1%)。这些 negative results 与论文的核心 narrative（KL 优于 magnitude-based methods）直接矛盾。Limitations 中的解释过于笼统。\n\n**W2** [Major] Target-swap ablation (C1) 存在 confound\n- C1 同时改变了 mask 表征（hard vs soft）和 target（magnitude vs KL-derived）。soft-vs-hard confound 的排除实验只排除了 softness 有利于 BCE 的可能，没有排除 softness 与 KL targets 的 interaction。oracle masks 来自特定 KL training trajectory，trajectory dependence 是 open question。\n\n**W3** [Major] \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" 叙事有 overclaim 风险\n- Table 1 的 \"2D taxonomy\" 实质上是一个 2×3 分类表。称之为论文核心贡献之一有 overclaim。\"Coupling alignment hierarchy\" 本质上是实验排序，使用 \"hierarchy\" 一词过于宏大。\n\n**W4** [Minor] 30% sparsity \"sweet spot\" 限制了实际影响\n- 30% 下 KL 工作良好，但 40% 时 MMLU 降至 35.5%，50% 时 MMLU 崩溃。30% 稀疏度 + 无 speedup = 实际部署价值有限。\n\n### 小问题\n- Responsible NLP Research Checklist 出现在 PDF 中，应仅在 OpenReview form 中填写\n- Table 2 caption footnote 过于密集\n- Abstract 中 \"post-hoc compensation becomes redundant\" 可能误导\n\n### Questions\n1. 是否考虑将 MaskLLM 适配到 activation sparsity setting 直接对比？\n2. 14B GSM8K 逆转的根因有更具体 evidence 吗？\n3. 是否测试过多样化训练数据对 downstream 的影响？\n4. Per-layer KL 的 train-inference distribution shift confound 有其他设计来控制吗？\n\n### Missing References\n- AWQ (Lin et al., 2024, MLSys) 的 activation-aware channel selection 可能相关\n\n### 格式合规\n- Responsible NLP Checklist 在 PDF 中 ❌ 未通过（应仅在 OpenReview form 中填写）\n- 其他所有格式检查均通过\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和小问题逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-22T08:32:06.182410+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34049
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-22T08:32:06.836213+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/小问题，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall Assessment**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [Critical] 97.5% signal-type 归因与下游指标矛盾，叙事有误导风险\n- §3.7 和 §4.5 声称\"signal type accounts for 97.5% of the PPL gap\"，但 §4.5 同时承认 per-layer KL underperforms end-to-end KL by 5-8pp on commonsense tasks，BoolQ 差距 9.2pp。这意味着 coupling scope 对下游任务的贡献远超 PPL 暗示的 2.5%。\n- 论文主叙事（abstract, conclusion）反复强调 97.5%，可能给读者\"coupling 不重要\"的错误印象。\n- 建议：在 abstract/conclusion 明确 97.5% 仅适用于 PPL；补充下游指标的 2D 分解定量结果。\n\n**N2** [Critical] C1 target-swap ablation 的循环论证未充分讨论\n- C1 将 KL 发现的 masks 交给 BCE 训练，BCE 也获得接近 KL 的 PPL。论文解释\"mask quality is the proximate driver\"。但这些 masks 恰恰由 KL 的耦合梯度发现——如果没有 KL 训练，这些 mask targets 根本不存在。C1 证明的是 transferability，而非\"coupling 不重要\"。\n- 建议：明确讨论循环性；补充反向实验——能否用其他方法找到同等质量 masks？\n\n**N3** [Critical] 无实际 wall-clock 加速，实用价值存疑\n- Table 5 显示 +6.4% latency overhead。论文承认 \"wall-clock speedup requires sparse kernel support not yet implemented\"。对 sparsity 方法论文缺乏加速验证是重大缺陷。\n- 建议：至少提供 Triton/cuSPARSE POC speedup 数字；或在 abstract/intro 显著弱化 practical motivation。\n\n### Should-Fix 问题\n\n**W1** [Major] 14B 实验覆盖不足，GSM8K 退步严重且缺乏对比\n- 14B 仅 30% sparsity。GSM8K -20pp (32.1±5.2%)，高 seed variance。未给出 TEAL 在 14B 上的 GSM8K 对比。\n- 建议：补 TEAL 14B 完整下游对比；补 14B 50% 结果。\n\n**W2** [Major] Knowledge-intensive 任务系统性退步缺乏机制解释\n- 8B 30% MMLU -5.2pp, 14B GSM8K -20pp。Limitations 中仅一句推测性解释。\n- 建议：分析 per-layer mask 差异与 knowledge storage 层的关系。\n\n**W3** [Major] MSE baseline 的 failed seed 报告方式不透明\n- Per-layer MSE 50% PPL 229.26，3 seeds 中有 catastrophic failure。在 mean±std 中报告会扭曲统计。\n- 建议：标注 failed seeds；分别报告 median 和 mean。\n\n**W4** [Minor] OOD variance 增大 (CV 0.2%→6.3%) 需更多讨论\n\n**W5** [Minor] Actual sparsity mismatch 讨论不够显著\n- KL 28.5% vs TEAL 29.3% at 30% target。主表使用不同实际稀疏度。\n\n### 小问题\n- §3.4 Eq.(5) 符号定义顺序\n- Figure 2 y 轴标签建议\n- Table 1 taxonomy 可能暗示 positioning 过于强调 novelty\n- Limitations 应明确\"scaling to 70B\"未测试原因\n\n### Questions\n1. 能否提供下游指标的 2D 分解定量结果？\n2. C1 中 BCE 是否也使用了 Gumbel-Sigmoid relaxation？\n3. 14B GSM8K -20pp 是否分析过哪些层 masks 差异最大？\n4. 是否有证据其他方法也能发现同等质量 masks？\n5. Compensation network 在 ≤45% sparsity 是否可能变得必要？\n\n### Missing References\n- PowerInfer-2 (Xue et al., 2024)\n- Wanda 的 structured pruning 方法论对比价值\n- ReLU-fication 中关于 SwiGLU→ReLU 后天然 sparsity 的分析\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和小问题逐条给出 [AGREE] 或 [REBUT] 回应。",
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/小问题，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall Assessment**: 3.0 (Findings)\n\n### Must-Fix 问题\n\n**N1** [Critical] 97.5% signal-type 归因与下游指标矛盾，叙事有误导风险\n- §3.7 和 §4.5 声称\"signal type accounts for 97.5% of the PPL gap\"，但 §4.5 同时承认 per-layer KL underperforms end-to-end KL by 5-8pp on commonsense tasks，BoolQ 差距 9.2pp。这意味着 coupling scope 对下游任务的贡献远超 PPL 暗示的 2.5%。\n- 论文主叙事（abstract, conclusion）反复强调 97.5%，可能给读者\"coupling 不重要\"的错误印象。\n- 建议：在 abstract/conclusion 明确 97.5% 仅适用于 PPL；补充下游指标的 2D 分解定量结果。\n\n**N2** [Critical] C1 target-swap ablation 的循环论证未充分讨论\n- C1 将 KL 发现的 masks 交给 BCE 训练，BCE 也获得接近 KL 的 PPL。论文解释\"mask quality is the proximate driver\"。但这些 masks 恰恰由 KL 的耦合梯度发现——如果没有 KL 训练，这些 mask targets 根本不存在。C1 证明的是 transferability，而非\"coupling 不重要\"。\n- 建议：明确讨论循环性；补充反向实验——能否用其他方法找到同等质量 masks？\n\n**N3** [Critical] 无实际 wall-clock 加速，实用价值存疑\n- Table 5 显示 +6.4% latency overhead。论文承认 \"wall-clock speedup requires sparse kernel support not yet implemented\"。对 sparsity 方法论文缺乏加速验证是重大缺陷。\n- 建议：至少提供 Triton/cuSPARSE POC speedup 数字；或在 abstract/intro 显著弱化 practical motivation。\n\n### Should-Fix 问题\n\n**W1** [Major] 14B 实验覆盖不足，GSM8K 退步严重且缺乏对比\n- 14B 仅 30% sparsity。GSM8K -20pp (32.1±5.2%)，高 seed variance。未给出 TEAL 在 14B 上的 GSM8K 对比。\n- 建议：补 TEAL 14B 完整下游对比；补 14B 50% 结果。\n\n**W2** [Major] Knowledge-intensive 任务系统性退步缺乏机制解释\n- 8B 30% MMLU -5.2pp, 14B GSM8K -20pp。Limitations 中仅一句推测性解释。\n- 建议：分析 per-layer mask 差异与 knowledge storage 层的关系。\n\n**W3** [Major] MSE baseline 的 failed seed 报告方式不透明\n- Per-layer MSE 50% PPL 229.26，3 seeds 中有 catastrophic failure。在 mean±std 中报告会扭曲统计。\n- 建议：标注 failed seeds；分别报告 median 和 mean。\n\n**W4** [Minor] OOD variance 增大 (CV 0.2%→6.3%) 需更多讨论\n\n**W5** [Minor] Actual sparsity mismatch 讨论不够显著\n- KL 28.5% vs TEAL 29.3% at 30% target。主表使用不同实际稀疏度。\n\n### 小问题\n- §3.4 Eq.(5) 符号定义顺序\n- Figure 2 y 轴标签建议\n- Table 1 taxonomy 可能暗示 positioning 过于强调 novelty\n- Limitations 应明确\"scaling to 70B\"未测试原因\n\n### Questions\n1. 能否提供下游指标的 2D 分解定量结果？\n2. C1 中 BCE 是否也使用了 Gumbel-Sigmoid relaxation？\n3. 14B GSM8K -20pp 是否分析过哪些层 masks 差异最大？\n4. 是否有证据其他方法也能发现同等质量 masks？\n5. Compensation network 在 ≤45% sparsity 是否可能变得必要？\n\n### Missing References\n- PowerInfer-2 (Xue et al., 2024)\n- Wanda 的 structured pruning 方法论对比价值\n- ReLU-fication 中关于 SwiGLU→ReLU 后天然 sparsity 的分析\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和小问题逐条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "distill_sparse_swiglu",
    "chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93",
    "director_session_key": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-22T08:32:08.548370+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1712
}
```

</details>

---


### Assistant

_source line 1552 · 2026-05-22T08:32:12.847254+00:00_

交叉分享已派发。等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1553 · 2026-05-22T08:32:15.603962+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall Assessment 3.0 (Findings)。主要问题：(1) 核心配方（KL + Gumbel for mask optimization）与 MaskLLM 高度重合，novelty 不足以撑起 main conference；(2) efficiency motivation 与实际增加 6.4% 延迟之间的叙事张力；(3) 14B 上 MMLU/GSM8K 的显著下降与核心叙事矛盾。优势方面：消融设计精巧（C1 target-swap、per-layer KL control），实验控制严格，negative results 报告诚实。格式方面发现一个问题：Responsible NLP Checklist 不应出现在 PDF 中。

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

_source line 1554 · 2026-05-22T08:32:19.567457+00:00_

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


## Round 131

## Round 131

2 recorded events


### User

_source line 1555 · 2026-05-22T08:33:29.733733+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 与 MaskLLM 的新颖性区分不足**

R2 的核心主张——"KL 优于 BCE 已被 MaskLLM 暗示"——过度简化了两者的差异。

1. **问题域本质不同**：MaskLLM 做的是 static weight sparsity（N:M structured，mask 在训练后固定），本文做的是 dynamic activation sparsity（mask 依赖 input，每个 token 不同）。这不是"application-level adaptation"——从 static mask optimization 到 input-conditioned predictor network 是一个非平凡的架构转变。MaskLLM 的直接可学习 mask 参数根本无法处理 unseen inputs，而本文的 predictor 必须泛化到 inference-time 的任意输入（§3.2, Eq. 3）。

2. **核心贡献不是"用 KL"，而是"分析 KL 为何有效"**：MaskLLM 选择 KL 但未分析 BCE 为何不行。本文的贡献在于：(a) §3.6 的梯度结构对比（虽 suggestive）；(b) §4.5 的 signal-type vs coupling-scope 分解；(c) C1 target-swap ablation；(d) per-layer Jaccard divergence 分析（§4.4, Figure 7）。这些是独立的分析性贡献，不依赖于 MaskLLM 的存在。

3. **但 R2 有部分道理**：论文确实应该更早、更显著地与 MaskLLM 对比（当前在 §2 Related Work 中提及但对比不够尖锐），明确说明"MaskLLM 在 weight sparsity 中使用了相似配方，本文的贡献在于将此扩展到 activation sparsity 并提供了系统性的 ablation 分析"。

**总结**：不同意将其标记为 Critical/Must-Fix。新颖性不在配方本身而在分析框架。但同意需要更 sharp 的 MaskLLM 对比。建议降级为 Should-Fix。

---

**[AGREE] R2-N2: Efficiency motivation 与无 speedup 的叙事张力**

完全同意，这与我的 N3 一致。论文 Introduction 第一段以"large fraction of FFN neurons contribute negligibly to the output"开篇暗示 efficiency gain，但全文无 wall-clock speedup 数据。Table 5 的 +6.4% overhead 进一步加剧了 motivation-contribution 的 gap。

补充一点 R2 未提到的：即使 unstructured masks 目前无法用标准 CUDA kernel 加速，近期 Triton block-sparse（已在 Appendix A page 13 提到但未实际测试）和 cuSPARSE 的进展使得 proof-of-concept speedup 并非不可能。论文完全缺乏尝试是一个遗憾。

---

### Should-Fix 问题

**[REBUT] R2-W1: 14B 结果与核心叙事矛盾**

部分反驳 R2 的 framing。

1. **R2 的对比对象有误**："GSM8K -20pp (32.1±5.2% vs TEAL 52.1%)" 中的 52.1% 是 **dense baseline**，不是 TEAL。论文中 TEAL 在 14B 上的 GSM8K 数据实际上缺失（这正是我在 W1 中指出的问题）。如果 TEAL 在 14B GSM8K 上同样退步严重，则不能说 KL "与核心叙事矛盾"——而是说 contextual sparsity 方法在 reasoning tasks 上普遍有限制。

2. **但核心关切成立**：无论 TEAL 表现如何，KL 在 14B 上 GSM8K −20pp、±5.2 高 variance 确实是严重的 negative result。论文将其淡化为 Limitations 中的一句话（"reasoning decline…KL's mass-covering property may preserve output quality at the expense of reasoning-critical pathways"，page 9）是不够的。

3. **建议**：同意需要补充 TEAL 在 14B 上的完整对比，但不同意"与核心叙事矛盾"的 framing——在缺乏 baseline 对比的情况下，这是一个 coverage gap 而非 contradiction。

---

**[AGREE] R2-W2: C1 target-swap ablation 存在 confound**

同意，但我的关切与 R2 不同，两者互补。

- **R2 的关切（soft-vs-hard confound）**：C1 用 hard binary KL-derived masks 训练 BCE，而原始 KL 训练用 Gumbel-Sigmoid soft masks。soft representation 可能与 KL loss 有 interaction（例如 soft masks 允许 gradient flow 更平滑），C1 未控制这个变量。这是有效的方法论关切。

- **我的关切（circularity，R1-N2）**：C1 的 KL-derived mask targets 本身就是 KL 耦合梯度的产物。"mask quality > coupling" 的结论因此有循环性——coupling 是发现这些高质量 masks 的必要条件。

两个 confound 叠加使得 C1 的因果推断力显著减弱。建议作者同时回应两个关切。

---

**[REBUT] R2-W3: "2D Taxonomy" / "Coupling Alignment Hierarchy" overclaim**

部分不同意。

1. **Table 1 的 taxonomy 确实仅是分类表**：同意 R2 指出"2D taxonomy"作为论文贡献之一被高估了。Table 1 本身是一个 2×3 表格，信息量有限。

2. **但 §4.5 的 2D 分解有实质分析价值**：将 signal type 和 coupling scope 正交分解，并用 4 个实验配置定量测量各自贡献（虽然我在 N1 中指出了 PPL vs downstream 的不一致），这不仅仅是命名。它提供了一个可被后续工作使用的分析框架。

3. **"Hierarchy" 一词确实过于宏大**：用"ranking"或"ordering"更准确。

**总结**：同意术语可以更谦逊（Minor 级别修改），但不同意 2D 分解本身缺乏实质——它是论文分析贡献的核心之一。建议从 Major 降级为 Minor。

---

**[AGREE] R2-W4: 30% sparsity "sweet spot" 限制实际影响**

同意。论文在 Limitations（page 9）承认"30% appears to be the lowest-degradation sparsity level for downstream fidelity"。40% 时 MMLU 降至 35.5%（Table 15, page 18），50% 时多数 downstream tasks 大幅退化。结合无 wall-clock speedup，30% 的 sweet spot 确实限制了实用价值。

---

### 小问题

**[AGREE] Responsible NLP Checklist 在 PDF 中**

根据 EMNLP 2026/ARR 规定，Responsible NLP Research Checklist 应仅在 OpenReview submission form 中填写，不应出现在论文 PDF 中。Page 10 的 "Responsible NLP Research Checklist" section（A1–E1 条目）违反此规定。这是一个格式合规问题，应在提交前移除。

**[AGREE] Table 2 caption footnote 过于密集**

同意。Table 2 的 caption 包含多个关键信息（extended training budget、no compensation、actual sparsity mismatch、seed details），密度过高容易遗漏。建议将 actual sparsity 信息移入主表的单独列。

**[REBUT] Abstract 中 "post-hoc compensation becomes redundant" 可能误导**

部分不同意"误导"的判断。Abstract 原文是"post-hoc compensation (+67.2M params) becomes redundant"，这有 Table 4 和 §4.5 的实验支撑——在 KL 训练下移除 compensation 对 PPL 的影响确实很小。但 R2 的关切可能在于：(a) 在 capacity-limited regime（>45% sparsity）compensation 可能重新变得必要（§4.6 暗示了这一点）；(b) "redundant" 一词过于绝对。建议改为"largely unnecessary at moderate sparsity levels"，但不认为当前措辞构成误导。

---

### Questions 回应

**Q1 (MaskLLM 直接适配对比)**: 有价值的实验建议。将 MaskLLM 适配到 activation sparsity（用 per-token learnable masks 替代 predictor network，或用 MaskLLM 的 N:M schedule 替代 global top-k）可以更清晰地隔离 predictor architecture 的贡献。我支持作者考虑此实验。

**Q2 (14B GSM8K 根因)**: 与我的 Q3 一致。需要 per-layer mask stability 分析来定位 reasoning degradation 的来源。

**Q3 (训练数据多样性)**: 有价值。当前仅用 WikiText-103 训练，可能导致 knowledge-intensive tasks 的系统性退步（与我的 W2 相关）。

**Q4 (Per-layer KL train-inference distribution shift)**: 这是一个我未注意到的好问题。Per-layer KL 在训练时逐层优化，但推理时使用 TEAL 的 global allocation。训练和推理的 allocation strategy 不同可能引入 distribution shift confound，特别是对于 §4.5 中 per-layer KL 的实验结果解读。

---

### Missing References

**[AGREE]** AWQ (Lin et al., 2024) 的 activation-aware channel selection 确实与本文的 activation-importance-based mask generation 有方法论联系，值得讨论。

---

### 总体评价

R2 的审稿抓到了一些真问题（efficiency gap、14B coverage、C1 confound），但 N1（MaskLLM novelty）的严重性被高估了——weight sparsity 和 activation sparsity 的问题域差异不是 application-level adaptation，论文的核心贡献在分析框架而非 KL+Gumbel 配方本身。

**我维持 Overall 3.0 (Findings)** 的评分。论文的实证贡献足够支撑 Findings，但 N2/N3（efficiency gap）和 N1（97.5% 归因矛盾）是阻碍 Conference 接收的主要因素。

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

_source line 1556 · 2026-05-22T08:33:38.022476+00:00_

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


## Round 132

## Round 132

2 recorded events


### User

_source line 1557 · 2026-05-22T08:33:40.755717+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应，已提交给 Review Director。

总结：
- **N1 (MaskLLM novelty)**: [REBUT] — weight vs activation sparsity 是本质不同的问题域，核心贡献在分析框架不在配方。但同意需更 sharp 的 MaskLLM 对比。
- **N2 (no speedup)**: [AGREE] — 与我的 N3 一致。
- **W1 (14B contradiction)**: [REBUT framing] — R2 将 dense baseline 误标为 TEAL，但同意 coverage 不足。
- **W2 (C1 confound)**: [AGREE] — soft-vs-hard confound 与我的 circularity 关切互补。
- **W3 (taxonomy overclaim)**: [REBUT severity] — 术语可谦逊，但 2D 分解有实质价值，建议降级为 Minor。
- **W4 (30% sweet spot)**: [AGREE]。
- 小问题：Checklist 格式 [AGREE]，Table 2 density [AGREE]，"redundant" 措辞 [REBUT]。

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

_source line 1558 · 2026-05-22T08:33:49.636262+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 133

## Round 133

12 recorded events


### User

_source line 1559 · 2026-05-22T08:34:43.280474+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

### Must-Fix

**[AGREE] R1-N1: 97.5% signal-type 归因与下游指标矛盾**
同意核心批评。但需澄清：R1 说"abstract/conclusion 反复强调 97.5%"并不完全准确——Abstract 用的是 "within 3%"，97.5% 仅在 §4.5 和 Conclusion 各出现一次。且 Abstract 和 Conclusion 都明确区分了 PPL vs downstream contribution。真正的问题是缺乏 downstream 指标的定量 2D 分解——论文给出了 raw gap (3-5pp commonsense, 9.2pp BoolQ) 但没有像 PPL 那样计算 % 贡献。建议补充而非删除 97.5% 这个数字。

**[AGREE] R1-N2: C1 循环论证**
同意 C1 证明的是 transferability 而非 "coupling 不重要"。论文在 Limitations 和 Appendix P 已承认 trajectory dependence，但 §4.4 主叙事中对此 qualification 不够突出。需补充"但 R1 忽略了 C1 的 diagnostic 价值：它排除了'KL 通过某种推理阶段特性（而非 mask quality）获益'的替代假说。"

**[AGREE] R1-N3: 无 wall-clock 加速**
完全同意。与我的 N2 一致。

### Should-Fix

**[REBUT] R1-W1: "未给出 TEAL 14B GSM8K 对比"**
R1 事实性错误。Table 13 (Appendix K) 明确报告 TEAL 14B uniform GSM8K = 52.1%，Limitations 也引用了 "32.1±5.2% vs. TEAL's 52.1%"。R1 的其他子论点（仅 30%、缺 50%）有效。

**[AGREE] R1-W2: Knowledge-intensive 退步缺机制解释**
同意。论文仅有推测性解释，未利用已有的 per-layer Jaccard divergence 框架 (Figure 7) 与 task-specific 性能关联。

**[AGREE] R1-W3: MSE failed seed 报告透明度**
同意。Appendix G 记录了 50% s123 的 catastrophic failure (PPL=15,789)，但主文 Table 4 仅报告 s42 未标注。30% 的 3-seed 报告是完整的。

**[AGREE] R1-W4: OOD variance** 同意，讨论不充分。
**[AGREE] R1-W5: Actual sparsity mismatch** 同意，应在主表做 matched-sparsity 对比。

### 小问题
全部 [AGREE]。Table 1 taxonomy overclaim 与我的 W3 一致。

### Missing References
PowerInfer-2 [AGREE] 值得补充。Wanda 和 ReLU Strikes Back 已引用但可深入讨论 SwiGLU→ReLU 替代方案。

### 与我评审的一致性
R1 Overall 3.0 (Findings) 与我一致。主要分歧：R1 的 W1 中有事实性错误（TEAL 14B GSM8K 已报告）；R1 对 N1 的 "反复强调" 稍显夸大。核心判断高度一致：方法新颖性有限（KL+Gumbel 来自 MaskLLM）、无 wall-clock speedup、14B 负面结果未充分处理。


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

_source line 1560 · 2026-05-22T08:35:13.131447+00:00_

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

_source line 1561 · 2026-05-22T08:35:13.131889+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:23:30.535958+00:00\", \"completed_at\": \"2026-05-22T08:23:35.370996+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 6pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-22T08:35:13.282776+00:00_

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

_source line 1563 · 2026-05-22T08:35:13.484000+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-22T08:35:52.493599+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1565 · 2026-05-22T08:35:52.544212+00:00_



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

_source line 1566 · 2026-05-22T08:37:53.709535+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 19 (fresh) — Active issues\n  # ============================================================\n\n  - id: \"R19-N1\"\n    summary: \"97.5% signal-type 归因仅适用于 PPL，与下游指标矛盾 (coupling scope 贡献 downstream 3-9pp)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。R1-N1 Critical。R2 同意但 nuance: 建议补充下游 2D 分解而非删除 97.5%。Abstract 用 'within 3%' 而非 97.5%，但 §4.5/Conclusion 各出现一次。核心问题: 缺乏 downstream 指标的定量 % 分解。\"}\n    action_items:\n      - {round: 19, action: \"在 abstract/conclusion 明确 97.5% 仅适用于 PPL；补充下游指标 2D 分解定量结果 (不仅 raw gap)\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 存在循环论证 + soft-vs-hard confound，因果推断力不足\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (互补关切)。R1-N2: 循环论证——KL-derived masks 由 coupling 发现，C1 证明 transferability 不等于 'coupling 不重要'。R2-W2: soft-vs-hard confound——BCE+Gumbel 排除仅 softness 有利 BCE，未排除 softness×KL-targets interaction。两个 confound 叠加显著削弱 C1 因果推断力。\"}\n    action_items:\n      - {round: 19, action: \"§4.4 主叙事需更突出 qualification: C1 证明 mask transferability 和排除'推理阶段特性'假说，但不能完全排除 coupling 的额外贡献。讨论循环性和 confound。\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无法转化为 speedup\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出。Framing 已调整。\"}\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识。R18-W2。Introduction 仍以 efficiency 动机展开。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。R1-N3 + R2-N2。Table 5 实测 +6.4% overhead。Introduction 开篇仍暗示 efficiency gain。R1 补充: Triton block-sparse POC 并非不可能但论文完全缺乏尝试。\"}\n    action_items:\n      - {round: 19, action: \"将 framing 从 efficiency 转向 'understanding training objective design space'；或提供 sparse kernel POC speedup 数据\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分不足: KL+Gumbel 配方高度重合，区别为 application-level\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2 首次提出 novelty 不足。R1 REBUT。\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18-W1。R2 维持 novelty 不足。R1 partial agree。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical: 三点区分均为 application-level。R1 REBUT: weight vs activation sparsity 是本质不同问题域，核心贡献在分析框架而非配方。R1 部分同意需更 sharp 的 MaskLLM 对比。\"}\n    action_items:\n      - {round: 19, action: \"持续分歧。建议: 更早更显著地对比 MaskLLM，明确贡献在于 '理解为什么 KL 有效' 而非 '提出用 KL'\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W2\"\n    summary: \"14B 实验覆盖不足 + GSM8K 大幅退步 (-20pp, σ=5.2pp)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W8。仅 30% sparsity。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W1 Major, R2-W1 Major)。R1 指出缺 TEAL 14B GSM8K 对比，R2 纠正: Table 13 已报告 TEAL 52.1%。核心关切: GSM8K -20pp 且 σ=5.2pp，Limitations 解释过于笼统。缺 50% sparsity 14B 结果。\"}\n    action_items:\n      - {round: 19, action: \"主文 §4.6 给出更具体失败模式分析; 补充 14B 50% sparsity 下游结果; 讨论 scale limitation\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 任务系统性退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W3。论文仅有假设性解释。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W2 Major, R2 agrees)。Per-layer KL §4.5 量化了 PPL-downstream dissociation 但未解释机制。已有 per-layer Jaccard divergence 框架 (Figure 7) 但未与 task-specific 性能关联。\"}\n    action_items:\n      - {round: 19, action: \"利用 per-layer Jaccard divergence 框架分析 knowledge-intensive tasks 退步与特定层 mask 差异的关系\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% sparsity failed seed 报告不透明 (Table 4 仅 s42)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W5。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W3 Major)。30% MSE 已更新为 3-seed (18.52±1.68)。但 50% MSE Table 4 仅报告 s42 (229.26)，Appendix G 提到 s123 failure (PPL=15789) 但主文未标注。\"}\n    action_items:\n      - {round: 19, action: \"Table 4 中标注哪些 entries 包含 failed seeds; 分别报告 median 和 mean，或排除 failed seeds 后单独报告\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"'2D Taxonomy' / 'Coupling Alignment Hierarchy' 术语 overclaim\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[分歧 severity] R2-W3 Major: Table 1 仅 2×3 分类表，'hierarchy' 过于宏大。R1 REBUT severity: 术语可谦逊，但 §4.5 2D 分解有实质分析价值。建议降级为 Minor。Director 判定: 术语修改 (Minor) + 2D 分解本身有效 (非 overclaim)。\"}\n    action_items:\n      - {round: 19, action: \"用更朴素语言: 'ranking/ordering' 替代 'hierarchy'; Table 1 降级为 organizational tool 而非 contribution\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表不够显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W6。Table 2 footnote 标注。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W5 Minor, R2 agrees)。Abstract 14.5% 用 matched sparsity 但未在 abstract 说明。主表使用不同实际稀疏度。\"}\n    action_items:\n      - {round: 19, action: \"Table 2 直接标注各方法实际稀疏度 (非仅脚注)，或增加 matched-sparsity 行\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响 (40% MMLU 降至 35.5%, 50% 崩溃)\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R2-W4 Minor, R1 agrees)。30% + 无 speedup = 部署价值有限。Limitations 已部分讨论。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W8\"\n    summary: \"OOD variance 增大 31× (CV 0.2%→6.3%) 讨论不充分\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W9。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W4 Minor)。Limitations 已提及但未深入分析。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-F1\"\n    summary: \"Responsible NLP Checklist 出现在 PDF 中，应仅在 OpenReview form 填写\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。PDF §9-10 页含 A1-E1 条目，违反 EMNLP 2026/ARR 提交规定。\"}\n    action_items:\n      - {round: 19, action: \"删除 PDF 中的 Responsible NLP Research Checklist section\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 18-19 — Resolved issues\n  # ============================================================\n\n  - id: \"R18-W4\"\n    summary: \"Gradient coupling 因果解释不完整: 缺少 per-layer KL 关键对照实验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识。缺 per-layer KL 实验隔离 coupling scope。\"}\n      - {round: 19, reviewers: [], note: \"Per-layer KL 3-seed 实验完成。§4.5 quantitative 2D decomposition。但 R19 提出新关切: 97.5% 归因仅适用 PPL (R19-N1)。实验本身已解决，衍生问题另行跟踪。\"}\n    action_items:\n      - {round: 18, action: \"补充 per-layer KL ablation\", assigned_to: \"research_director\", status: done}\n    resolution: \"Per-layer KL 3-seed 实验完成并写入 §4.5。衍生归因问题见 R19-N1。\"\n    resolution_round: 19\n\n  - id: \"R18-W7\"\n    summary: \"Seed-to-seed mask Jaccard divergence 未报告\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"需要 cross-seed Jaccard 作为 46-68% divergence 的 reference baseline。\"}\n      - {round: 19, reviewers: [], note: \"Appendix §Cross-Seed Mask Consistency: cross-seed=36.3% < random=46.2% < KL-vs-mag 46-68%。R19 未再提出。\"}\n    resolution: \"数据已补充，未在 R19 被再次提出。\"\n    resolution_round: 19\n\n  - id: \"R18-M1\"\n    summary: \"Missing refs: MoC, Activation Pattern Clustering\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2 提出。\"}\n      - {round: 19, reviewers: [], note: \"§2 Related Work 已包含 MoC (wu2025moc) 和 Clustering (dhar2025clustering)。R19 未再提出。\"}\n    resolution: \"两篇引用均已添加到 §2。\"\n    resolution_round: 19\n\n  - id: \"R18-W5\"\n    summary: \"MSE baseline 单 seed 报告掩盖高方差\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"Table 2/4 仅报 seed 42。\"}\n      - {round: 19, reviewers: [], note: \"Table 4 30% MSE 已更新为 3-seed (18.52±1.68)。50% MSE 透明度问题另见 R19-W4。\"}\n    resolution: \"30% MSE 3-seed 报告完成。50% 透明度问题升级为 R19-W4 独立跟踪。\"\n    resolution_round: 19\n\n  # ============================================================\n  # Earlier rounds — Resolved (history, abbreviated)\n  # ============================================================\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [], note: \"所有关键行均为 3-seed 报告。\"}\n    resolution: \"所有关键行均为 3-seed 报告。MSE 3-seed 含 failed seed。\"\n    resolution_round: 19\n\n  - id: \"R16-N2\"\n    summary: \"消融实验仅在 50% 稀疏度\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"Table 4 现包含 30% 和 50% 双列消融。\"\n    resolution_round: 17\n\n  - id: \"R16-N4\"\n    summary: \"缺少与已有训练型稀疏预测器的数值对比\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"experiments.tex 已明确标注 controlled comparison equivalences。\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Forward KL 方向选择论证不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"§3.4 forward KL 论证和 wu2025rethinking 引用已被接受。\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"评估域同质性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"Limitations 讨论被接受。降级为 info。\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"§3.6 梯度分析 informal → 缺 per-layer KL 对照\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    resolution: \"Per-layer KL 实验完成。§4.5 quantitative decomposition。\"\n    resolution_round: 19\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"正文 8 页合规。\"\n    resolution_round: 17\n\n  - id: \"R16-VIS2\"\n    summary: \"前4页无 display item\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"Figure 1 移至 introduction.tex, 渲染在第 2 页。\"\n    resolution_round: 17\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 19\n    resolution: \"叙事重构为 '2D decomposition'。术语 overclaim 残留问题见 R19-W5。\"\n    resolution_round: 19\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity 下报告\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 18\n    resolution: \"Abstract 双数字报告被接受。\"\n    resolution_round: 16\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-W1 继续跟踪。R2 Critical，R1 REBUT。\"}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, downstream task-dependent\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 18\n    resolution: \"Abstract 和正文已加入 task-type split 描述。\"\n    resolution_round: 16\n\n  - id: \"R16-M1\"\n    summary: \"Missing references: activation sparsity opportunities, 2:4 activation sparsity, rethinking KL\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"三篇引用均已添加。\"\n    resolution_round: 17"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 19 (fresh) — Active issues\n  # ============================================================\n\n  - id: \"R19-N1\"\n    summary: \"97.5% signal-type 归因仅适用于 PPL，与下游指标矛盾 (coupling scope 贡献 downstream 3-9pp)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。R1-N1 Critical。R2 同意但 nuance: 建议补充下游 2D 分解而非删除 97.5%。Abstract 用 'within 3%' 而非 97.5%，但 §4.5/Conclusion 各出现一次。核心问题: 缺乏 downstream 指标的定量 % 分解。\"}\n    action_items:\n      - {round: 19, action: \"在 abstract/conclusion 明确 97.5% 仅适用于 PPL；补充下游指标 2D 分解定量结果 (不仅 raw gap)\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 存在循环论证 + soft-vs-hard confound，因果推断力不足\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (互补关切)。R1-N2: 循环论证——KL-derived masks 由 coupling 发现，C1 证明 transferability 不等于 'coupling 不重要'。R2-W2: soft-vs-hard confound——BCE+Gumbel 排除仅 softness 有利 BCE，未排除 softness×KL-targets interaction。两个 confound 叠加显著削弱 C1 因果推断力。\"}\n    action_items:\n      - {round: 19, action: \"§4.4 主叙事需更突出 qualification: C1 证明 mask transferability 和排除'推理阶段特性'假说，但不能完全排除 coupling 的额外贡献。讨论循环性和 confound。\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无法转化为 speedup\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出。Framing 已调整。\"}\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识。R18-W2。Introduction 仍以 efficiency 动机展开。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。R1-N3 + R2-N2。Table 5 实测 +6.4% overhead。Introduction 开篇仍暗示 efficiency gain。R1 补充: Triton block-sparse POC 并非不可能但论文完全缺乏尝试。\"}\n    action_items:\n      - {round: 19, action: \"将 framing 从 efficiency 转向 'understanding training objective design space'；或提供 sparse kernel POC speedup 数据\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分不足: KL+Gumbel 配方高度重合，区别为 application-level\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - {round: 16, reviewers: [2], note: \"R2 首次提出 novelty 不足。R1 REBUT。\"}\n      - {round: 18, reviewers: [1, 2], note: \"R18-W1。R2 维持 novelty 不足。R1 partial agree。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical: 三点区分均为 application-level。R1 REBUT: weight vs activation sparsity 是本质不同问题域，核心贡献在分析框架而非配方。R1 部分同意需更 sharp 的 MaskLLM 对比。\"}\n    action_items:\n      - {round: 19, action: \"持续分歧。建议: 更早更显著地对比 MaskLLM，明确贡献在于 '理解为什么 KL 有效' 而非 '提出用 KL'\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W2\"\n    summary: \"14B 实验覆盖不足 + GSM8K 大幅退步 (-20pp, σ=5.2pp)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W8。仅 30% sparsity。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W1 Major, R2-W1 Major)。R1 指出缺 TEAL 14B GSM8K 对比，R2 纠正: Table 13 已报告 TEAL 52.1%。核心关切: GSM8K -20pp 且 σ=5.2pp，Limitations 解释过于笼统。缺 50% sparsity 14B 结果。\"}\n    action_items:\n      - {round: 19, action: \"主文 §4.6 给出更具体失败模式分析; 补充 14B 50% sparsity 下游结果; 讨论 scale limitation\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Knowledge-intensive 任务系统性退步缺乏机制解释\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W3。论文仅有假设性解释。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W2 Major, R2 agrees)。Per-layer KL §4.5 量化了 PPL-downstream dissociation 但未解释机制。已有 per-layer Jaccard divergence 框架 (Figure 7) 但未与 task-specific 性能关联。\"}\n    action_items:\n      - {round: 19, action: \"利用 per-layer Jaccard divergence 框架分析 knowledge-intensive tasks 退步与特定层 mask 差异的关系\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"MSE baseline 50% sparsity failed seed 报告不透明 (Table 4 仅 s42)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W5。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W3 Major)。30% MSE 已更新为 3-seed (18.52±1.68)。但 50% MSE Table 4 仅报告 s42 (229.26)，Appendix G 提到 s123 failure (PPL=15789) 但主文未标注。\"}\n    action_items:\n      - {round: 19, action: \"Table 4 中标注哪些 entries 包含 failed seeds; 分别报告 median 和 mean，或排除 failed seeds 后单独报告\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"'2D Taxonomy' / 'Coupling Alignment Hierarchy' 术语 overclaim\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[分歧 severity] R2-W3 Major: Table 1 仅 2×3 分类表，'hierarchy' 过于宏大。R1 REBUT severity: 术语可谦逊，但 §4.5 2D 分解有实质分析价值。建议降级为 Minor。Director 判定: 术语修改 (Minor) + 2D 分解本身有效 (非 overclaim)。\"}\n    action_items:\n      - {round: 19, action: \"用更朴素语言: 'ranking/ordering' 替代 'hierarchy'; Table 1 降级为 organizational tool 而非 contribution\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表不够显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W6。Table 2 footnote 标注。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W5 Minor, R2 agrees)。Abstract 14.5% 用 matched sparsity 但未在 abstract 说明。主表使用不同实际稀疏度。\"}\n    action_items:\n      - {round: 19, action: \"Table 2 直接标注各方法实际稀疏度 (非仅脚注)，或增加 matched-sparsity 行\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响 (40% MMLU 降至 35.5%, 50% 崩溃)\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R2-W4 Minor, R1 agrees)。30% + 无 speedup = 部署价值有限。Limitations 已部分讨论。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W8\"\n    summary: \"OOD variance 增大 31× (CV 0.2%→6.3%) 讨论不充分\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"R18-W9。\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W4 Minor)。Limitations 已提及但未深入分析。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-F1\"\n    summary: \"Responsible NLP Checklist 出现在 PDF 中，应仅在 OpenReview form 填写\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。PDF §9-10 页含 A1-E1 条目，违反 EMNLP 2026/ARR 提交规定。\"}\n    action_items:\n      - {round: 19, action: \"删除 PDF 中的 Responsible NLP Research Checklist section\", assigned_to: \"research_director\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 18-19 — Resolved issues\n  # ============================================================\n\n  - id: \"R18-W4\"\n    summary: \"Gradient coupling 因果解释不完整: 缺少 per-layer KL 关键对照实验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识。缺 per-layer KL 实验隔离 coupling scope。\"}\n      - {round: 19, reviewers: [], note: \"Per-layer KL 3-seed 实验完成。§4.5 quantitative 2D decomposition。但 R19 提出新关切: 97.5% 归因仅适用 PPL (R19-N1)。实验本身已解决，衍生问题另行跟踪。\"}\n    action_items:\n      - {round: 18, action: \"补充 per-layer KL ablation\", assigned_to: \"research_director\", status: done}\n    resolution: \"Per-layer KL 3-seed 实验完成并写入 §4.5。衍生归因问题见 R19-N1。\"\n    resolution_round: 19\n\n  - id: \"R18-W7\"\n    summary: \"Seed-to-seed mask Jaccard divergence 未报告\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"需要 cross-seed Jaccard 作为 46-68% divergence 的 reference baseline。\"}\n      - {round: 19, reviewers: [], note: \"Appendix §Cross-Seed Mask Consistency: cross-seed=36.3% < random=46.2% < KL-vs-mag 46-68%。R19 未再提出。\"}\n    resolution: \"数据已补充，未在 R19 被再次提出。\"\n    resolution_round: 19\n\n  - id: \"R18-M1\"\n    summary: \"Missing refs: MoC, Activation Pattern Clustering\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [2], note: \"R2 提出。\"}\n      - {round: 19, reviewers: [], note: \"§2 Related Work 已包含 MoC (wu2025moc) 和 Clustering (dhar2025clustering)。R19 未再提出。\"}\n    resolution: \"两篇引用均已添加到 §2。\"\n    resolution_round: 19\n\n  - id: \"R18-W5\"\n    summary: \"MSE baseline 单 seed 报告掩盖高方差\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"Table 2/4 仅报 seed 42。\"}\n      - {round: 19, reviewers: [], note: \"Table 4 30% MSE 已更新为 3-seed (18.52±1.68)。50% MSE 透明度问题另见 R19-W4。\"}\n    resolution: \"30% MSE 3-seed 报告完成。50% 透明度问题升级为 R19-W4 独立跟踪。\"\n    resolution_round: 19\n\n  # ============================================================\n  # Earlier rounds — Resolved (history, abbreviated)\n  # ============================================================\n\n  - id: \"R16-N1\"\n    summary: \"多种子覆盖不一致\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [], note: \"所有关键行均为 3-seed 报告。\"}\n    resolution: \"所有关键行均为 3-seed 报告。MSE 3-seed 含 failed seed。\"\n    resolution_round: 19\n\n  - id: \"R16-N2\"\n    summary: \"消融实验仅在 50% 稀疏度\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"Table 4 现包含 30% 和 50% 双列消融。\"\n    resolution_round: 17\n\n  - id: \"R16-N4\"\n    summary: \"缺少与已有训练型稀疏预测器的数值对比\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"experiments.tex 已明确标注 controlled comparison equivalences。\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Forward KL 方向选择论证不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"§3.4 forward KL 论证和 wu2025rethinking 引用已被接受。\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"评估域同质性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"Limitations 讨论被接受。降级为 info。\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"§3.6 梯度分析 informal → 缺 per-layer KL 对照\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    resolution: \"Per-layer KL 实验完成。§4.5 quantitative decomposition。\"\n    resolution_round: 19\n\n  - id: \"R16-VIS1\"\n    summary: \"正文溢出到第9页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"正文 8 页合规。\"\n    resolution_round: 17\n\n  - id: \"R16-VIS2\"\n    summary: \"前4页无 display item\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"Figure 1 移至 introduction.tex, 渲染在第 2 页。\"\n    resolution_round: 17\n\n  - id: \"R15-N1\"\n    summary: \"Coupling alignment 概念过度包装\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 19\n    resolution: \"叙事重构为 '2D decomposition'。术语 overclaim 残留问题见 R19-W5。\"\n    resolution_round: 19\n\n  - id: \"R15-N2\"\n    summary: \"Abstract headline '19% PPL improvement' 在非匹配 sparsity 下报告\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 18\n    resolution: \"Abstract 双数字报告被接受。\"\n    resolution_round: 16\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界不够清晰\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"R19-W1 继续跟踪。R2 Critical，R1 REBUT。\"}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R15-W1\"\n    summary: \"实际可用 regime 仅 30%, downstream task-dependent\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 18\n    resolution: \"Abstract 和正文已加入 task-type split 描述。\"\n    resolution_round: 16\n\n  - id: \"R16-M1\"\n    summary: \"Missing references: activation sparsity opportunities, 2:4 activation sparsity, rethinking KL\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 18\n    resolution: \"三篇引用均已添加。\"\n    resolution_round: 17"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-22T08:37:53.811869+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 13851}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-22T08:40:23.424255+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 19 (Fresh)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**审稿日期**: 2026-05-22\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验评估; R2: 新颖性+完整性+格式合规）\n\n---\n\n## Summary\n\n本文用 forward KL divergence + Gumbel-Sigmoid 松弛替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（75.9M 参数，&lt;1% base）。在 LLaMA-3.1-8B 30% 稀疏度下 PPL 优于 TEAL 14.5%（matched sparsity），发现的 mask pattern 与 magnitude-based 方法有 46-68% Jaccard 偏离。Target-swap ablation (C1) 证明 mask quality 是推理质量的近端驱动因素。Per-layer KL 控制实验将效果分解为 signal type（占 PPL gap 97.5%）和 coupling scope（贡献 downstream 3-9pp）。跨架构评估在 Mistral-7B PPL 泛化，Qwen-2.5-14B 出现 MMLU/GSM8K 下降。\n\n---\n\n## Strengths\n\n**S1. 研究问题有价值** [共识]\nBCE 将每个神经元独立处理的局限性是 contextual sparsity 文献中被忽视的问题。用 output-distribution objective 替代 per-neuron classification 是自然且有意义的研究方向。\n\n**S2. 消融设计系统且精巧** [共识]\nC1 target-swap ablation、per-layer KL decomposition、5 种 loss 变体对比（Table 4）、Gumbel vs STE 对比形成完整消融体系。实验控制严格：所有 baseline 使用相同架构/数据/优化器，仅改变损失函数（Appendix G）。\n\n**S3. 训练效率优势明确** [R1]\nKL 在 1000 steps（~45 min）达到的效果优于 BCE 2700 steps（~46 min），wall-clock 相当但 PPL 差距 2.4×（11.79 vs 28.13）。\n\n**S4. Negative results 报告诚实** [共识]\n14B MMLU/GSM8K 下降、global allocation 高 MMLU variance（σ=9.5pp）、50% downstream collapse 均被充分讨论。\n\n**S5. 附录内容充实** [R1]\n19 个附录覆盖 inference latency、bottleneck sensitivity、temperature schedule、training convergence、penalty controller dynamics、OOD evaluation 等，增强可复现性。\n\n**S6. Related work 覆盖全面** [R2]\n包含 2024-2026 年 activation sparsity 最新文献：R-Sparse、DIP、SparseInfer、MoC、SVD-CSP、Polar Sparsity、MoNE、D2D-MoE 等。\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**C1. 97.5% signal-type 归因与下游指标矛盾** [共识: R1-N1 Critical, R2 AGREE]\n§4.5 和 Conclusion 声称 \"signal type accounts for 97.5% of the PPL gap\"，但同一节承认 per-layer KL（无 cross-layer coupling）在 commonsense tasks 上 underperform 3-5pp，BoolQ 差距 9.2pp。Coupling scope 对下游贡献远超 PPL 暗示的 2.5%。论文主叙事反复使用 97.5% 但未补充下游指标的定量 2D 分解，可能给读者 \"coupling 不重要\" 的错误印象。\n\n**C2. C1 target-swap ablation 因果推断不足** [共识: R1-N2 + R2-W2, 互补关切]\n两个叠加 confound 削弱 C1 的因果推断力：\n- **循环论证** (R1): KL-derived masks 由 coupling 发现 → BCE 用这些 masks 也能达到类似 PPL → 结论 \"mask quality > coupling\"。但如果没有 KL 的 coupled gradients，这些高质量 masks 根本不存在。C1 证明的是 transferability，不是 \"coupling 不重要\"。\n- **Soft-vs-hard confound** (R2): C1 同时改变 mask 表征（hard vs soft）和 target。BCE+Gumbel 排除仅排除了 softness 有利于 BCE 的可能，未排除 softness×KL-targets interaction。\n论文在 Appendix P 承认 trajectory dependence，但 §4.4 主叙事对此 qualification 不够突出。\n\n**C3. 无 wall-clock speedup，efficiency motivation 空洞** [共识: R1-N3 + R2-N2]\nTable 5 实测 +6.4% overhead（126.78 vs 119.11 ms/forward）。Introduction 开篇以 \"high contextual sparsity\" 和 FFN 神经元冗余为动机暗示 efficiency gain，但全文无任何 speedup 结果。Triton block-sparse 在 Appendix A 提到但未实际测试。对于 sparsity 方法论文，motivation-contribution gap 过大。\n\n**C4. 与 MaskLLM 新颖性区分** [分歧: R2 Critical, R1 REBUT → Should-Fix]\n核心配方（frozen backbone + learnable masks + KL + Gumbel relaxation）与 MaskLLM (NeurIPS 2024) 高度重合。§2 的三点区分（sparsity type、mask generation、allocation）被 R2 判定为 application-level adaptation。R1 反驳：weight sparsity → activation sparsity 涉及 predictor network 泛化到 unseen inputs，非 trivial 迁移；核心贡献在分析框架（C1、2D decomposition）而非配方本身。R1 部分同意需更 sharp 的 MaskLLM 对比。\n**Director 判定**: 新颖性确实有限——\"KL 优于 BCE\" 已被 MaskLLM 方法选择隐含验证。但分析贡献（target-swap ablation、signal type vs coupling scope 分解）有独立价值。此 issue 是 Findings vs Conference 的核心分界线。\n\n### Major (Should-Fix)\n\n**M1. 14B 实验覆盖不足 + GSM8K 严重退步** [共识: R1-W1, R2-W1]\nQwen-2.5-14B 仅有 30% sparsity 完整评估。GSM8K 从 dense 87.57% 降至 KL 32.1±5.2%（TEAL 52.1%），−20pp 且高 seed variance。Contribution 4（\"preliminary cross-scale evaluation\"）基础薄弱。缺 50% sparsity 14B 下游结果。Limitations 解释（\"task-and-scale-dependent effects\"）过于笼统。\n（注: R1 声称 TEAL 14B GSM8K 未报告为事实性错误，Table 13 已含此数据。）\n\n**M2. Knowledge-intensive 任务退步缺机制解释** [共识: R1-W2, R2 AGREE]\n8B 30% MMLU −5.2pp, 14B GSM8K −20pp, 跨三个模型一致。Limitations 仅一句推测（\"mass-covering property may preserve output breadth at the expense of reasoning-critical pathways\"），未利用已有的 per-layer Jaccard divergence 框架与 task-specific 性能关联。\n\n**M3. MSE 50% failed seed 报告不透明** [共识: R1-W3, R2 AGREE]\nTable 4 50% MSE 仅报告 s42 (229.26)，Appendix G 提到 s123 failure（PPL=15,789, sparsity 仅 5.1%）但主文未标注。30% MSE 已更新为 3-seed（18.52±1.68），但 50% 的处理方式不一致。\n\n### Minor (Nice-to-Fix)\n\n**m1. \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" 术语** [分歧 severity: R2 Major → R1 Minor]\nTable 1 仅 2×3 分类表，\"hierarchy\" 过于宏大。R1 认为 §4.5 的 2D 分解有实质分析价值，问题仅在术语。Director 判定: 术语需谦逊化（Minor），2D 分解本身有效。\n\n**m2. Actual sparsity mismatch 主表不够显著** [共识: R1-W5, R2 AGREE]\nKL 28.5% vs TEAL 29.3% at 30% target。主表仅 footnote 标注，abstract 14.5% 用 matched-sparsity 但未说明。\n\n**m3. OOD variance 增大 (CV 0.2%→6.3%) 讨论不充分** [共识: R1-W4]\n\n**m4. 30% sparsity sweet spot 限制实际影响** [共识: R2-W4, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| 97.5% 归因 vs 下游矛盾 | Critical | AGREE | **共识** |\n| C1 因果推断不足 | Critical (circularity) | Major (confound) | **共识 (互补)** |\n| 无 wall-clock speedup | Critical | Critical | **共识** |\n| 14B 实验不足 | Major | Major | **共识** |\n| Knowledge-intensive 退步缺解释 | Major | AGREE | **共识** |\n| MSE failed seed 透明度 | Major | AGREE | **共识** |\n| Sparsity mismatch 显示 | Minor | AGREE | **共识** |\n| OOD variance 讨论 | Minor | AGREE | **共识** |\n| Checklist 格式违规 | AGREE | 提出者 | **共识** |\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | Director 判定 |\n|-------|----|----|--------------|\n| MaskLLM novelty 严重性 | REBUT (Should-Fix): 贡献在分析框架 | Critical: 配方重合 | 分歧记录。是 Findings/Conference 分界线 |\n| Taxonomy overclaim 级别 | Minor: 2D 分解有实质价值 | Major: 仅分类表 | 术语 Minor, 分解有效 |\n| \"redundant\" 措辞误导 | REBUT: 有实验支撑 | Minor: 可能误导 | Minor |\n\n---\n\n## Questions for Authors\n\n1. 能否提供下游指标（ARC-c, WG, MMLU, BoolQ）的定量 2D 分解（signal type vs coupling scope 的 % 贡献），而非仅 raw gap？\n2. 是否有证据表明其他方法（evolutionary search、gradient-free optimization）能发现与 KL 类似质量的 masks？这将澄清 coupling 是 mask discovery 的必要条件还是充分条件。\n3. C1 中 BCE 训练是否也使用了 Gumbel-Sigmoid？如果仅用 hard threshold，则 C1 vs KL 的差异可能部分来自 relaxation method。\n4. 14B GSM8K −20pp 且 σ=5.2pp：是否分析过哪些层的 masks 在不同 seeds 间差异最大？\n5. Per-layer KL 的 train-inference distribution shift（训练时 mask 1 层，推理时 mask 32 层）是否可通过 mask-K-layers curriculum 控制？\n6. 是否测试过多样化训练数据（C4 子集、code）对 MMLU 等 knowledge-intensive downstream 的影响？\n\n---\n\n## Missing References\n\n- **PowerInfer-2** (Xue et al., 2024): on-device sparsity work [R1 提出, R2 AGREE]\n- **AWQ** (Lin et al., 2024, MLSys): activation-aware channel selection 与本文 importance scoring 有方法论联系 [R2 提出, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置未开启 paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因 API 限额错误未完成（status: done with error: \"You've hit your limit · resets 6pm (UTC)\"）。无排版审查结果。完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n\n### 评分理由\n\n**达到 Findings bar 的因素：**\n- 研究问题有价值且明确（BCE 独立性 → KL coupled optimization）\n- 消融设计系统：C1 target-swap、per-layer KL decomposition、5 种 loss 对比\n- 3-seed 评估、严格控制变量、充实附录，可复现性强\n- Signal type vs coupling scope 的 2D 分解是有用的分析框架\n- Negative results（14B regression、downstream collapse at 50%）诚实报告\n\n**阻碍 Conference 接收的因素：**\n1. **核心配方新颖性有限**: KL + Gumbel for mask optimization 已被 MaskLLM 建立。论文的贡献在分析框架而非方法创新，但分析叙事本身有关键缺口（97.5% 归因矛盾、C1 循环论证）。\n2. **分析叙事断裂**: 97.5% signal-type 归因是论文最吸引人的 claim，但仅基于 PPL，与下游指标矛盾（coupling scope 贡献 3-9pp）。C1 的因果推断因循环论证和 soft-vs-hard confound 而不足。这两个缺口使论文无法清晰回答 \"what specifically does KL contribute\"。\n3. **实用价值未验证**: +6.4% overhead，无任何 speedup 数据。30% 是唯一可用 regime，40%+ 下游崩溃。Motivation-contribution gap 过大。\n4. **Scale 泛化存疑**: 14B GSM8K −20pp（σ=5.2pp）暗示方法可能有 scale limitation，但缺乏分析。\n\n**推荐**: Findings 接收。实证贡献（KL 系统性优于 BCE for sparsity prediction training, 2D decomposition 框架）有发表价值。但需修正 97.5% 归因叙事（补充下游定量分解）、澄清 C1 的因果推断边界（明确标注循环性）、删除 PDF 中的 Checklist section（格式违规）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第一段以 efficiency 为动机但全文无 speedup——考虑将 opening motivation 调整为 \"understanding how training objective shapes sparsity prediction quality\"，与 p.8 (\"This paper is primarily an empirical study...\") 一致。\n- Contribution 1 (\"coupling alignment hierarchy\") 用 \"hierarchy\" 过于宏大，建议 \"ranking\" 或 \"ordering\"。\n- Contribution 4 (\"preliminary cross-scale evaluation\") 过于薄弱，考虑降级或与 Contribution 1 合并为附加证据。\n\n### §3.6 Gradient Analysis\n- \"suggestive\" 标注恰当，但 §4.5 的 97.5% 归因暗示了更强的因果关系，两者 tension 需解决。\n\n### §3.7 Two-Dimensional Taxonomy\n- Table 1 作为分类工具有用，但作为 contribution 被高估。建议在 Contribution list 中降级。\n\n### §4.4 Target-Swap Ablation (C1)\n- 需在主叙事中更突出讨论：(a) 循环性——KL coupling 是发现高质量 masks 的必要条件；(b) soft-vs-hard confound 未完全排除。当前 qualification 在 Appendix P，对主文读者不够可见。\n\n### §4.5 Per-Layer KL Decomposition\n- 97.5% 数字需限定为 \"PPL-level attribution\"，并补充下游指标的定量分解。\n- 承认的 train-inference distribution shift confound 需要更多讨论——训练时 mask 1 层 vs 推理时 mask 32 层的 gap 可能系统性低估了 coupling scope 的贡献。\n\n### §4.6 Cross-Architecture and Scale\n- 14B 结果需更具体的失败模式分析，尤其 GSM8K 高 seed variance 的来源。TEAL 在 14B GSM8K 为 52.1%，KL 为 32.1±5.2%——这不仅是 \"scale-dependent effect\"，可能是 KL 的 mode-covering 特性在高容量模型上反而有害的证据。\n\n### Table 2\n- Caption footnote 密度过高，建议将 actual sparsity 移入主表单独列。\n- MSE 50% (229.26) 应标注 \"s42 only; s123 failure (PPL=15,789, sparsity 5.1%)\"。\n\n### Table 4\n- 标注 30% MSE 为 3-seed, 50% MSE 为 s42 only with footnote about s123 catastrophic failure。\n\n### Limitations\n- \"Scaling to 70B remains untested\" 应说明原因（计算资源 vs 方法论障碍）。\n- 训练数据同质性的讨论可更深入——C4 OOD variance 增大 31× 暗示 predictor 对 domain 敏感。\n\n### Ethics Statement\n- 合理且完整。\n\n### Format\n- **必须删除** PDF 中的 \"Responsible NLP Research Checklist\" section（A1-E1 条目）。根据 EMNLP 2026/ARR 规定，该 checklist 仅在 OpenReview submission form 中填写，不出现在论文 PDF 中。",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
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
    "report": "# 审稿报告 — Round 19 (Fresh)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**审稿日期**: 2026-05-22\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验评估; R2: 新颖性+完整性+格式合规）\n\n---\n\n## Summary\n\n本文用 forward KL divergence + Gumbel-Sigmoid 松弛替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（75.9M 参数，&lt;1% base）。在 LLaMA-3.1-8B 30% 稀疏度下 PPL 优于 TEAL 14.5%（matched sparsity），发现的 mask pattern 与 magnitude-based 方法有 46-68% Jaccard 偏离。Target-swap ablation (C1) 证明 mask quality 是推理质量的近端驱动因素。Per-layer KL 控制实验将效果分解为 signal type（占 PPL gap 97.5%）和 coupling scope（贡献 downstream 3-9pp）。跨架构评估在 Mistral-7B PPL 泛化，Qwen-2.5-14B 出现 MMLU/GSM8K 下降。\n\n---\n\n## Strengths\n\n**S1. 研究问题有价值** [共识]\nBCE 将每个神经元独立处理的局限性是 contextual sparsity 文献中被忽视的问题。用 output-distribution objective 替代 per-neuron classification 是自然且有意义的研究方向。\n\n**S2. 消融设计系统且精巧** [共识]\nC1 target-swap ablation、per-layer KL decomposition、5 种 loss 变体对比（Table 4）、Gumbel vs STE 对比形成完整消融体系。实验控制严格：所有 baseline 使用相同架构/数据/优化器，仅改变损失函数（Appendix G）。\n\n**S3. 训练效率优势明确** [R1]\nKL 在 1000 steps（~45 min）达到的效果优于 BCE 2700 steps（~46 min），wall-clock 相当但 PPL 差距 2.4×（11.79 vs 28.13）。\n\n**S4. Negative results 报告诚实** [共识]\n14B MMLU/GSM8K 下降、global allocation 高 MMLU variance（σ=9.5pp）、50% downstream collapse 均被充分讨论。\n\n**S5. 附录内容充实** [R1]\n19 个附录覆盖 inference latency、bottleneck sensitivity、temperature schedule、training convergence、penalty controller dynamics、OOD evaluation 等，增强可复现性。\n\n**S6. Related work 覆盖全面** [R2]\n包含 2024-2026 年 activation sparsity 最新文献：R-Sparse、DIP、SparseInfer、MoC、SVD-CSP、Polar Sparsity、MoNE、D2D-MoE 等。\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**C1. 97.5% signal-type 归因与下游指标矛盾** [共识: R1-N1 Critical, R2 AGREE]\n§4.5 和 Conclusion 声称 \"signal type accounts for 97.5% of the PPL gap\"，但同一节承认 per-layer KL（无 cross-layer coupling）在 commonsense tasks 上 underperform 3-5pp，BoolQ 差距 9.2pp。Coupling scope 对下游贡献远超 PPL 暗示的 2.5%。论文主叙事反复使用 97.5% 但未补充下游指标的定量 2D 分解，可能给读者 \"coupling 不重要\" 的错误印象。\n\n**C2. C1 target-swap ablation 因果推断不足** [共识: R1-N2 + R2-W2, 互补关切]\n两个叠加 confound 削弱 C1 的因果推断力：\n- **循环论证** (R1): KL-derived masks 由 coupling 发现 → BCE 用这些 masks 也能达到类似 PPL → 结论 \"mask quality > coupling\"。但如果没有 KL 的 coupled gradients，这些高质量 masks 根本不存在。C1 证明的是 transferability，不是 \"coupling 不重要\"。\n- **Soft-vs-hard confound** (R2): C1 同时改变 mask 表征（hard vs soft）和 target。BCE+Gumbel 排除仅排除了 softness 有利于 BCE 的可能，未排除 softness×KL-targets interaction。\n论文在 Appendix P 承认 trajectory dependence，但 §4.4 主叙事对此 qualification 不够突出。\n\n**C3. 无 wall-clock speedup，efficiency motivation 空洞** [共识: R1-N3 + R2-N2]\nTable 5 实测 +6.4% overhead（126.78 vs 119.11 ms/forward）。Introduction 开篇以 \"high contextual sparsity\" 和 FFN 神经元冗余为动机暗示 efficiency gain，但全文无任何 speedup 结果。Triton block-sparse 在 Appendix A 提到但未实际测试。对于 sparsity 方法论文，motivation-contribution gap 过大。\n\n**C4. 与 MaskLLM 新颖性区分** [分歧: R2 Critical, R1 REBUT → Should-Fix]\n核心配方（frozen backbone + learnable masks + KL + Gumbel relaxation）与 MaskLLM (NeurIPS 2024) 高度重合。§2 的三点区分（sparsity type、mask generation、allocation）被 R2 判定为 application-level adaptation。R1 反驳：weight sparsity → activation sparsity 涉及 predictor network 泛化到 unseen inputs，非 trivial 迁移；核心贡献在分析框架（C1、2D decomposition）而非配方本身。R1 部分同意需更 sharp 的 MaskLLM 对比。\n**Director 判定**: 新颖性确实有限——\"KL 优于 BCE\" 已被 MaskLLM 方法选择隐含验证。但分析贡献（target-swap ablation、signal type vs coupling scope 分解）有独立价值。此 issue 是 Findings vs Conference 的核心分界线。\n\n### Major (Should-Fix)\n\n**M1. 14B 实验覆盖不足 + GSM8K 严重退步** [共识: R1-W1, R2-W1]\nQwen-2.5-14B 仅有 30% sparsity 完整评估。GSM8K 从 dense 87.57% 降至 KL 32.1±5.2%（TEAL 52.1%），−20pp 且高 seed variance。Contribution 4（\"preliminary cross-scale evaluation\"）基础薄弱。缺 50% sparsity 14B 下游结果。Limitations 解释（\"task-and-scale-dependent effects\"）过于笼统。\n（注: R1 声称 TEAL 14B GSM8K 未报告为事实性错误，Table 13 已含此数据。）\n\n**M2. Knowledge-intensive 任务退步缺机制解释** [共识: R1-W2, R2 AGREE]\n8B 30% MMLU −5.2pp, 14B GSM8K −20pp, 跨三个模型一致。Limitations 仅一句推测（\"mass-covering property may preserve output breadth at the expense of reasoning-critical pathways\"），未利用已有的 per-layer Jaccard divergence 框架与 task-specific 性能关联。\n\n**M3. MSE 50% failed seed 报告不透明** [共识: R1-W3, R2 AGREE]\nTable 4 50% MSE 仅报告 s42 (229.26)，Appendix G 提到 s123 failure（PPL=15,789, sparsity 仅 5.1%）但主文未标注。30% MSE 已更新为 3-seed（18.52±1.68），但 50% 的处理方式不一致。\n\n### Minor (Nice-to-Fix)\n\n**m1. \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" 术语** [分歧 severity: R2 Major → R1 Minor]\nTable 1 仅 2×3 分类表，\"hierarchy\" 过于宏大。R1 认为 §4.5 的 2D 分解有实质分析价值，问题仅在术语。Director 判定: 术语需谦逊化（Minor），2D 分解本身有效。\n\n**m2. Actual sparsity mismatch 主表不够显著** [共识: R1-W5, R2 AGREE]\nKL 28.5% vs TEAL 29.3% at 30% target。主表仅 footnote 标注，abstract 14.5% 用 matched-sparsity 但未说明。\n\n**m3. OOD variance 增大 (CV 0.2%→6.3%) 讨论不充分** [共识: R1-W4]\n\n**m4. 30% sparsity sweet spot 限制实际影响** [共识: R2-W4, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识：\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| 97.5% 归因 vs 下游矛盾 | Critical | AGREE | **共识** |\n| C1 因果推断不足 | Critical (circularity) | Major (confound) | **共识 (互补)** |\n| 无 wall-clock speedup | Critical | Critical | **共识** |\n| 14B 实验不足 | Major | Major | **共识** |\n| Knowledge-intensive 退步缺解释 | Major | AGREE | **共识** |\n| MSE failed seed 透明度 | Major | AGREE | **共识** |\n| Sparsity mismatch 显示 | Minor | AGREE | **共识** |\n| OOD variance 讨论 | Minor | AGREE | **共识** |\n| Checklist 格式违规 | AGREE | 提出者 | **共识** |\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | Director 判定 |\n|-------|----|----|--------------|\n| MaskLLM novelty 严重性 | REBUT (Should-Fix): 贡献在分析框架 | Critical: 配方重合 | 分歧记录。是 Findings/Conference 分界线 |\n| Taxonomy overclaim 级别 | Minor: 2D 分解有实质价值 | Major: 仅分类表 | 术语 Minor, 分解有效 |\n| \"redundant\" 措辞误导 | REBUT: 有实验支撑 | Minor: 可能误导 | Minor |\n\n---\n\n## Questions for Authors\n\n1. 能否提供下游指标（ARC-c, WG, MMLU, BoolQ）的定量 2D 分解（signal type vs coupling scope 的 % 贡献），而非仅 raw gap？\n2. 是否有证据表明其他方法（evolutionary search、gradient-free optimization）能发现与 KL 类似质量的 masks？这将澄清 coupling 是 mask discovery 的必要条件还是充分条件。\n3. C1 中 BCE 训练是否也使用了 Gumbel-Sigmoid？如果仅用 hard threshold，则 C1 vs KL 的差异可能部分来自 relaxation method。\n4. 14B GSM8K −20pp 且 σ=5.2pp：是否分析过哪些层的 masks 在不同 seeds 间差异最大？\n5. Per-layer KL 的 train-inference distribution shift（训练时 mask 1 层，推理时 mask 32 层）是否可通过 mask-K-layers curriculum 控制？\n6. 是否测试过多样化训练数据（C4 子集、code）对 MMLU 等 knowledge-intensive downstream 的影响？\n\n---\n\n## Missing References\n\n- **PowerInfer-2** (Xue et al., 2024): on-device sparsity work [R1 提出, R2 AGREE]\n- **AWQ** (Lin et al., 2024, MLSys): activation-aware channel selection 与本文 importance scoring 有方法论联系 [R2 提出, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置未开启 paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因 API 限额错误未完成（status: done with error: \"You've hit your limit · resets 6pm (UTC)\"）。无排版审查结果。完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n\n### 评分理由\n\n**达到 Findings bar 的因素：**\n- 研究问题有价值且明确（BCE 独立性 → KL coupled optimization）\n- 消融设计系统：C1 target-swap、per-layer KL decomposition、5 种 loss 对比\n- 3-seed 评估、严格控制变量、充实附录，可复现性强\n- Signal type vs coupling scope 的 2D 分解是有用的分析框架\n- Negative results（14B regression、downstream collapse at 50%）诚实报告\n\n**阻碍 Conference 接收的因素：**\n1. **核心配方新颖性有限**: KL + Gumbel for mask optimization 已被 MaskLLM 建立。论文的贡献在分析框架而非方法创新，但分析叙事本身有关键缺口（97.5% 归因矛盾、C1 循环论证）。\n2. **分析叙事断裂**: 97.5% signal-type 归因是论文最吸引人的 claim，但仅基于 PPL，与下游指标矛盾（coupling scope 贡献 3-9pp）。C1 的因果推断因循环论证和 soft-vs-hard confound 而不足。这两个缺口使论文无法清晰回答 \"what specifically does KL contribute\"。\n3. **实用价值未验证**: +6.4% overhead，无任何 speedup 数据。30% 是唯一可用 regime，40%+ 下游崩溃。Motivation-contribution gap 过大。\n4. **Scale 泛化存疑**: 14B GSM8K −20pp（σ=5.2pp）暗示方法可能有 scale limitation，但缺乏分析。\n\n**推荐**: Findings 接收。实证贡献（KL 系统性优于 BCE for sparsity prediction training, 2D decomposition 框架）有发表价值。但需修正 97.5% 归因叙事（补充下游定量分解）、澄清 C1 的因果推断边界（明确标注循环性）、删除 PDF 中的 Checklist section（格式违规）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第一段以 efficiency 为动机但全文无 speedup——考虑将 opening motivation 调整为 \"understanding how training objective shapes sparsity prediction quality\"，与 p.8 (\"This paper is primarily an empirical study...\") 一致。\n- Contribution 1 (\"coupling alignment hierarchy\") 用 \"hierarchy\" 过于宏大，建议 \"ranking\" 或 \"ordering\"。\n- Contribution 4 (\"preliminary cross-scale evaluation\") 过于薄弱，考虑降级或与 Contribution 1 合并为附加证据。\n\n### §3.6 Gradient Analysis\n- \"suggestive\" 标注恰当，但 §4.5 的 97.5% 归因暗示了更强的因果关系，两者 tension 需解决。\n\n### §3.7 Two-Dimensional Taxonomy\n- Table 1 作为分类工具有用，但作为 contribution 被高估。建议在 Contribution list 中降级。\n\n### §4.4 Target-Swap Ablation (C1)\n- 需在主叙事中更突出讨论：(a) 循环性——KL coupling 是发现高质量 masks 的必要条件；(b) soft-vs-hard confound 未完全排除。当前 qualification 在 Appendix P，对主文读者不够可见。\n\n### §4.5 Per-Layer KL Decomposition\n- 97.5% 数字需限定为 \"PPL-level attribution\"，并补充下游指标的定量分解。\n- 承认的 train-inference distribution shift confound 需要更多讨论——训练时 mask 1 层 vs 推理时 mask 32 层的 gap 可能系统性低估了 coupling scope 的贡献。\n\n### §4.6 Cross-Architecture and Scale\n- 14B 结果需更具体的失败模式分析，尤其 GSM8K 高 seed variance 的来源。TEAL 在 14B GSM8K 为 52.1%，KL 为 32.1±5.2%——这不仅是 \"scale-dependent effect\"，可能是 KL 的 mode-covering 特性在高容量模型上反而有害的证据。\n\n### Table 2\n- Caption footnote 密度过高，建议将 actual sparsity 移入主表单独列。\n- MSE 50% (229.26) 应标注 \"s42 only; s123 failure (PPL=15,789, sparsity 5.1%)\"。\n\n### Table 4\n- 标注 30% MSE 为 3-seed, 50% MSE 为 s42 only with footnote about s123 catastrophic failure。\n\n### Limitations\n- \"Scaling to 70B remains untested\" 应说明原因（计算资源 vs 方法论障碍）。\n- 训练数据同质性的讨论可更深入——C4 OOD variance 增大 31× 暗示 predictor 对 domain 敏感。\n\n### Ethics Statement\n- 合理且完整。\n\n### Format\n- **必须删除** PDF 中的 \"Responsible NLP Research Checklist\" section（A1-E1 条目）。根据 EMNLP 2026/ARR 规定，该 checklist 仅在 OpenReview submission form 中填写，不出现在论文 PDF 中。",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-22T08:40:27.727812+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4303
}
```

</details>

---


### Assistant

_source line 1570 · 2026-05-22T08:40:37.273886+00:00_

审稿报告已投递。

**Round 19 审稿完成。**

两位 Reviewer 一致给出 **3.0 (Findings)**。

核心问题汇总：
- **4 个 Critical**: (1) 97.5% signal-type 归因与下游指标矛盾；(2) C1 ablation 循环论证 + confound；(3) 无 wall-clock speedup；(4) MaskLLM novelty 区分（分歧，R2 Critical / R1 Should-Fix）
- **3 个 Major**: 14B 覆盖不足（GSM8K −20pp）、knowledge-intensive 退步缺机制解释、MSE failed seed 透明度
- **1 个格式违规**: PDF 中的 Responsible NLP Checklist 需删除

Issue Tracker 已同步更新至 `review_issues.yaml`。视觉审查因 API 限额未完成，完成后会自动补发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1571 · 2026-05-22T08:40:40.030177+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：与 R1 Overall 3.0 (Findings) 高度一致，仅在 W1（TEAL 14B GSM8K 对比确实存在于 Table 13）和 N1（"反复强调"程度）上有事实性修正。

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

_source line 1572 · 2026-05-22T08:40:49.922932+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结**:
- **Overall**: 3.0 (Findings)，两位 Reviewer 完全一致
- **4 个 Critical**: 97.5% 归因与下游矛盾、C1 循环论证+confound、无 wall-clock speedup、MaskLLM novelty 区分（分歧）
- **3 个 Major**: 14B 覆盖不足 (GSM8K −20pp)、knowledge-intensive 退步缺机制解释、MSE failed seed 透明度
- **1 个格式违规**: Responsible NLP Checklist 应从 PDF 中删除
- Issue Tracker 已同步更新（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 135

## Round 135

58 recorded events


### User

_source line 1573 · 2026-05-22T09:32:54.041202+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May cycle)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

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

_source line 1574 · 2026-05-22T09:33:00.696949+00:00_

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

_source line 1575 · 2026-05-22T09:33:00.748085+00:00_

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

_source line 1576 · 2026-05-22T09:33:07.221402+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "11"
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-22T09:33:07.272039+00:00_

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

_source line 1578 · 2026-05-22T09:33:11.195364+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "11"
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
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-22T09:33:11.246072+00:00_



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

_source line 1580 · 2026-05-22T09:33:16.880569+00:00_

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

_source line 1581 · 2026-05-22T09:33:17.884732+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (365 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\n\n## 待处理\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\n- perlayer_kl_50_s42_boolq（准备中）\n- perlayer_kl_50_s42_ppl（准备中）\n- qwen14b_kl30_s42_gsm8k_uniform（准备中）\n- revkl_30_s42_boolq_uniform（准备中）\n- diag_eval_env_34887（准备中）\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\n- diag_status_34887（准备中）\n- diag_status_41718（准备中）\n- read_boolq_results（准备中）\n- …另有 41 项\n\n## 近期结论\n- **mse30_s42_boolq** (success): MSE-distilled predictor at 30% sparsity (s42) preserves BoolQ accurac
…[truncated 1782 chars]

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

_source line 1582 · 2026-05-22T09:33:17.985955+00:00_

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

_source line 1583 · 2026-05-22T09:33:18.338460+00:00_

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
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-22T09:33:18.338993+00:00_

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

_source line 1585 · 2026-05-22T09:33:18.339431+00:00_



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

_source line 1586 · 2026-05-22T09:33:18.792176+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1587 · 2026-05-22T09:33:18.842832+00:00_

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

_source line 1588 · 2026-05-22T09:33:23.713661+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1589 · 2026-05-22T09:33:24.117385+00:00_

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

_source line 1590 · 2026-05-22T09:33:24.117915+00:00_

1	Learned sparsity predictors for SwiGLU LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation confirms these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	A coupling alignment ranking emerges across five loss configurations; a per-layer KL control decomposes this into two dimensions with a task-dependent spectrum: signal type dominates PPL (98\% of the gap at 30\%), while coupling scope contributes 24--35\% on downstream tasks---both dimensions carry independent value.
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	

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

_source line 1591 · 2026-05-22T09:33:24.872001+00:00_

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

_source line 1592 · 2026-05-22T09:33:24.872704+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity---a property exploitable for potential inference acceleration---but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\
…[truncated 2859 chars]

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

_source line 1593 · 2026-05-22T09:33:25.381179+00:00_

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

_source line 1594 · 2026-05-22T09:33:25.836078+00:00_

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
…[truncated 9558 chars]

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

_source line 1595 · 2026-05-22T09:33:25.837771+00:00_

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

_source line 1596 · 2026-05-22T09:33:26.540751+00:00_

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
…[truncated 17686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1597 · 2026-05-22T09:33:26.691792+00:00_

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

_source line 1598 · 2026-05-22T09:33:26.792686+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
16	Dhar et al.~\cite{dhar2025clustering} compress acti
…[truncated 5052 chars]

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


### Tool call

_source line 1599 · 2026-05-22T09:33:26.843337+00:00_

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

_source line 1600 · 2026-05-22T09:33:27.258552+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Coupling alignment---optimizing through the output distribution---is the dominant design dimension for learned sparsity: signal type dominates PPL (98\% of the gap at 30\%), while coupling scope contributes 24--35\% on downstream tasks---a task-dependent spectrum where both dimensions carry independent value.
5	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\%, with KL-discovered masks (46--68\% divergent from magnitude) driving inference quality; however, downstream transfer is task- and scale-dependent. Future work: N:M sparsity and 70B+ scaling.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 415
}
```

</details>

---


### Tool call

_source line 1601 · 2026-05-22T09:33:27.264415+00:00_

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

_source line 1602 · 2026-05-22T09:33:27.785728+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 521
}
```

</details>

---


### Tool call

_source line 1603 · 2026-05-22T09:33:27.786129+00:00_

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

_source line 1604 · 2026-05-22T09:33:28.288517+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

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

_source line 1605 · 2026-05-22T09:33:28.288964+00:00_

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

_source line 1606 · 2026-05-22T09:33:28.691448+00:00_

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
…[truncated 30508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-22T09:33:28.792251+00:00_

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

_source line 1608 · 2026-05-22T09:33:28.943609+00:00_

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
…[truncated 21206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-22T09:33:33.663449+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

I found comprehensive information about the EMNLP 2026 ARR Call for Papers. Here are the key submission guidelines and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers feat
…[truncated 2206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 9949
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-22T09:33:41.705396+00:00_

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

_source line 1611 · 2026-05-22T09:33:41.756104+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

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

_source line 1612 · 2026-05-22T09:33:41.756607+00:00_

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

_source line 1613 · 2026-05-22T09:33:43.364262+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (365 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\n\n## 待处理\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\n- perlayer_kl_50_s42_boolq（准备中）\n- perlayer_kl_50_s42_ppl（准备中）\n- qwen14b_kl30_s42_gsm8k_uniform（准备中）\n- revkl_30_s42_boolq_uniform（准备中）\n- diag_eval_env_34887（准备中）\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\n- diag_status_34887（准备中）\n- diag_status_41718（准备中）\n- read_boolq_results（准备中）\n- …另有 41 项\n\n## 近期结论\n- **mse30_s42_boolq** (success): MSE-distilled predictor at 30% sparsity (s42) preserves BoolQ accurac
…[truncated 1782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1607
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-22T09:33:43.364733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines formatting page limit anonymity requirements",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
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
    "query": "ACL Rolling Review 2026 author guidelines formatting page limit anonymity requirements",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1615 · 2026-05-22T09:33:45.323879+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1616 · 2026-05-22T09:33:46.027651+00:00_

-rw-r--r-- 1 ubuntu ubuntu 515115 May 22 09:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1617 · 2026-05-22T09:33:46.279499+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
  "description": "Check existing review reports"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_reports/ 2>/dev/null || echo \"NO_REPORTS_DIR\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 1618 · 2026-05-22T09:33:46.330157+00:00_

round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_14.md
round_15.md
round_16.md
round_17.md
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-22T09:33:48.789982+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines formatting page limit anonymity requirements"

Links: [{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here are the key ACL Rolling Review (ARR) 2026 author guidelines regarding formatting, page limits, and anonymity requirements:

## Page Limits

The page limit is 4 pages for short papers and 8 pages for long papers, excluding ethical considerations and limitations.

## Formatting

ARR has abandoned the MS Word template for conference submissions, and submissions based on the Word template will be desk-rejected
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5425
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-22T09:33:55.866867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null | head -200 || echo \"NO_FILE\"",
  "description": "Read existing review issues tracker"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null | head -200 || echo \"NO_FILE\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-22T09:33:55.917831+00:00_

issues:
  # ============================================================
  # Round 19 (fresh) — Active issues (all in_progress per Action Matrix)
  # ============================================================

  - id: "R19-N1"
    summary: "97.5% signal-type 归因仅适用于 PPL，与下游指标矛盾 (coupling scope 贡献 downstream 3-9pp)"
    category: framing
    severity: critical
    status: in_progress
    first_raised_round: 19
    last_seen_round: 19
    mentions:
      - {round: 19, reviewers: [1, 2], note: "[AGREE] 共识。R1-N1 Critical。R2 同意但 nuance: 建议补充下游 2D 分解而非删除 97.5%。Abstract 用 'within 3%' 而非 97.5%，但 §4.5/Conclusion 各出现一次。核心问题: 缺乏 downstream 指标的定量 % 分解。"}
    action_items:
      - {round: 19, action: "Paper Agent: abstract/conclusion 明确 97.5% 仅适用于 PPL", assigned_to: "paper_agent", status: in_progress}
      - {round: 19, action: "Agent: 补 MSE 30% downstream eval → 计算 downstream 定量 2D 分解", assigned_to: "main_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R19-N2"
    summary: "C1 target-swap ablation 存在循环论证 + soft-vs-hard confound，因果推断力不足"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 19
    last_seen_round: 19
    mentions:
      - {round: 19, reviewers: [1, 2], note: "[AGREE] 共识 (互补关切)。R1-N2: 循环论证——KL-derived masks 由 coupling 发现，C1 证明 transferability 不等于 'coupling 不重要'。R2-W2: soft-vs-hard confound——BCE+Gumbel 排除仅 softness 有利 BCE，未排除 softness×KL-targets interaction。两个 confound 叠加显著削弱 C1 因果推断力。"}
    action_items:
      - {round: 19, action: "Paper Agent: §4.4 reframe 为 mask transferability + 加 circularity caveat + Appendix P 内容提升到主文", assigned_to: "paper_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R19-N3"
    summary: "无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无法转化为 speedup"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 16
    last_seen_round: 19
    mentions:
      - {round: 16, reviewers: [1, 
…[truncated 6985 chars]

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

_source line 1622 · 2026-05-22T09:35:04.223225+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 (Long Paper, ARR May 2026 cycle)\n- **截止日期**：2026-05-25\n- **格式要求**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL LaTeX template（已使用 `\\usepackage[review]{acl}`）\n- **匿名规则**：双盲审稿，无匿名期限制\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. KL 蒸馏方法严谨性\n- §3.6 的梯度分析（BCE vs KL gradient structure）是否数学正确？推导是否完整？\n- Forward KL vs Reverse KL 的论证（mode-covering vs mode-seeking）是否站得住？\n- Gumbel-Sigmoid relaxation 的使用是否合理？与 STE 的对比是否 fair？\n\n### 2. C1 Target-Swap Ablation（§4.4）\n- 这个 ablation 是否存在循环论证？（KL-derived masks 是由 coupling 发现的，用它们训练 BCE 是否能证明 \"coupling 不重要\"？）\n- Soft-vs-hard confound：论文用 BCE+Gumbel (32.22) vs standard BCE (27.97) 排除 softness 效应，这个对照是否充分？\n- C1 实验的因果推断力有多强？\n\n### 3. Per-Layer KL 2D 分解（§4.5）\n- \"Signal type accounts for 98% of PPL gap\" 这个归因是否方法论正确？\n- Per-layer KL 的 train-inference mismatch（训练 mask 1 layer/step，inference 32 layers 同时）是否被充分讨论？\n- Downstream 分解的定量方法是否 sound？\n\n### 4. 实验方法论\n- 训练仅用 WikiText-103，评估 WikiText-2：同分布问题\n- Multi-seed 覆盖：哪些实验有 3-seed，哪些只有 seed 42？\n- Actual sparsity mismatch（KL 28.5% vs TEAL 29.3% at 30% target）：是否影响公平对比？\n- MSE baseline 在 50% 的 seed 失败（s123 PPL=15789）：是否充分报告？\n- Compensation redundancy 的实验是否 conclusive？\n\n### 5. 统计可靠性\n- 3-seed evaluation 是否足够？领域标准是什么？\n- OOD variance（CV 0.2% → 6.3%）的 implications\n- Global allocation 30% MMLU σ=9.5pp 的极端 variance\n\n请按以下结构输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 Critical/Major/Minor + 置信度）\n4. Questions（需要作者回答的）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 (Long Paper, ARR May 2026 cycle)\n- **截止日期**：2026-05-25\n- **格式要求**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL LaTeX template（已使用 `\\usepackage[review]{acl}`）\n- **匿名规则**：双盲审稿，无匿名期限制\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. KL 蒸馏方法严谨性\n- §3.6 的梯度分析（BCE vs KL gradient structure）是否数学正确？推导是否完整？\n- Forward KL vs Reverse KL 的论证（mode-covering vs mode-seeking）是否站得住？\n- Gumbel-Sigmoid relaxation 的使用是否合理？与 STE 的对比是否 fair？\n\n### 2. C1 Target-Swap Ablation（§4.4）\n- 这个 ablation 是否存在循环论证？（KL-derived masks 是由 coupling 发现的，用它们训练 BCE 是否能证明 \"coupling 不重要\"？）\n- Soft-vs-hard confound：论文用 BCE+Gumbel (32.22) vs standard BCE (27.97) 排除 softness 效应，这个对照是否充分？\n- C1 实验的因果推断力有多强？\n\n### 3. Per-Layer KL 2D 分解（§4.5）\n- \"Signal type accounts for 98% of PPL gap\" 这个归因是否方法论正确？\n- Per-layer KL 的 train-inference mismatch（训练 mask 1 layer/step，inference 32 layers 同时）是否被充分讨论？\n- Downstream 分解的定量方法是否 sound？\n\n### 4. 实验方法论\n- 训练仅用 WikiText-103，评估 WikiText-2：同分布问题\n- Multi-seed 覆盖：哪些实验有 3-seed，哪些只有 seed 42？\n- Actual sparsity mismatch（KL 28.5% vs TEAL 29.3% at 30% target）：是否影响公平对比？\n- MSE baseline 在 50% 的 seed 失败（s123 PPL=15789）：是否充分报告？\n- Compensation redundancy 的实验是否 conclusive？\n\n### 5. 统计可靠性\n- 3-seed evaluation 是否足够？领域标准是什么？\n- OOD variance（CV 0.2% → 6.3%）的 implications\n- Global allocation 30% MMLU σ=9.5pp 的极端 variance\n\n请按以下结构输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 Critical/Major/Minor + 置信度）\n4. Questions（需要作者回答的）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-22T09:35:24.176977+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19953
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-22T09:35:24.428480+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + Related Work**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 (Long Paper, ARR May 2026 cycle)\n- **截止日期**：2026-05-25\n- **格式要求**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL LaTeX template（已使用 `\\usepackage[review]{acl}`）\n- **匿名规则**：双盲审稿，无匿名期限制\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **MaskLLM 区分**：本文使用 KL + Gumbel + frozen weights + learnable masks，MaskLLM 也用这个配方。三点区分（sparsity type / mask generation / allocation）是否足够建立独立贡献？还是仅 application-level 差异？\n- 论文自称 \"primarily an empirical study\"，这个定位下的贡献是否足够 EMNLP main？\n- Target-swap ablation、2D taxonomy、coupling alignment ranking 作为分析框架的新颖性如何？\n\n### 2. 贡献 Framing\n- Abstract/Introduction 的 claims 是否与实验结果匹配？有无 overclaim？\n- \"Coupling alignment is the dominant design dimension\" 这个 claim 的支撑是否充分？\n- 论文标题 \"Output-Distribution Distillation\" 是否准确反映内容？\n- 实用价值：30% sparsity + 6.4% overhead + 无 wall-clock speedup，对社区有什么实际贡献？\n\n### 3. Related Work 完整性\n- 是否遗漏重要相关工作？特别关注：\n  - 2025-2026 年的 activation sparsity 新工作\n  - KL distillation 在其他压缩场景的应用\n  - SwiGLU-specific pruning/sparsity 方法\n- MaskLLM 的对比讨论是否公平、充分？\n- 与 D2D-MoE、ShadowLLM 等 predictor-based 方法的对比是否到位？\n\n### 4. 跨架构 + 跨 scale 证据\n- 3 个模型（LLaMA-8B, Mistral-7B, Qwen-14B）的覆盖是否足够？\n- 14B 的 GSM8K -20pp 退步 + MMLU -2.8pp：这是系统性问题还是偶发？\n- Knowledge-intensive 任务的系统性退步是否得到充分解释？\n- Cross-architecture 能否建立 generality claim？\n\n### 5. 写作质量\n- 论文结构是否清晰？信息密度是否恰当？\n- 术语使用：'coupling alignment ranking', 'signal type × coupling scope', '2D taxonomy' 是否过度创造术语？\n- Figure/Table 质量和信息量\n- 8 页限制内是否包含了足够信息？Appendix 是否包含了应在主文中出现的关键结果？\n\n### 6. 格式合规\n- 页数是否符合 8 页限制？\n- 匿名性检查：是否泄露作者信息？\n- Limitations 和 Ethics 章节是否充分？\n- 引用格式是否正确（natbib）？\n\n请按以下结构输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 Critical/Major/Minor + 置信度）\n4. Questions（需要作者回答的）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + Related Work**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 (Long Paper, ARR May 2026 cycle)\n- **截止日期**：2026-05-25\n- **格式要求**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数\n- **模板**：ACL LaTeX template（已使用 `\\usepackage[review]{acl}`）\n- **匿名规则**：双盲审稿，无匿名期限制\n- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- **MaskLLM 区分**：本文使用 KL + Gumbel + frozen weights + learnable masks，MaskLLM 也用这个配方。三点区分（sparsity type / mask generation / allocation）是否足够建立独立贡献？还是仅 application-level 差异？\n- 论文自称 \"primarily an empirical study\"，这个定位下的贡献是否足够 EMNLP main？\n- Target-swap ablation、2D taxonomy、coupling alignment ranking 作为分析框架的新颖性如何？\n\n### 2. 贡献 Framing\n- Abstract/Introduction 的 claims 是否与实验结果匹配？有无 overclaim？\n- \"Coupling alignment is the dominant design dimension\" 这个 claim 的支撑是否充分？\n- 论文标题 \"Output-Distribution Distillation\" 是否准确反映内容？\n- 实用价值：30% sparsity + 6.4% overhead + 无 wall-clock speedup，对社区有什么实际贡献？\n\n### 3. Related Work 完整性\n- 是否遗漏重要相关工作？特别关注：\n  - 2025-2026 年的 activation sparsity 新工作\n  - KL distillation 在其他压缩场景的应用\n  - SwiGLU-specific pruning/sparsity 方法\n- MaskLLM 的对比讨论是否公平、充分？\n- 与 D2D-MoE、ShadowLLM 等 predictor-based 方法的对比是否到位？\n\n### 4. 跨架构 + 跨 scale 证据\n- 3 个模型（LLaMA-8B, Mistral-7B, Qwen-14B）的覆盖是否足够？\n- 14B 的 GSM8K -20pp 退步 + MMLU -2.8pp：这是系统性问题还是偶发？\n- Knowledge-intensive 任务的系统性退步是否得到充分解释？\n- Cross-architecture 能否建立 generality claim？\n\n### 5. 写作质量\n- 论文结构是否清晰？信息密度是否恰当？\n- 术语使用：'coupling alignment ranking', 'signal type × coupling scope', '2D taxonomy' 是否过度创造术语？\n- Figure/Table 质量和信息量\n- 8 页限制内是否包含了足够信息？Appendix 是否包含了应在主文中出现的关键结果？\n\n### 6. 格式合规\n- 页数是否符合 8 页限制？\n- 匿名性检查：是否泄露作者信息？\n- Limitations 和 Ethics 章节是否充分？\n- 引用格式是否正确（natbib）？\n\n请按以下结构输出审稿报告：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 Critical/Major/Minor + 置信度）\n4. Questions（需要作者回答的）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-22T09:35:25.990970+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-22T09:35:26.041656+00:00_

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

_source line 1627 · 2026-05-22T09:35:26.444392+00:00_

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

_source line 1628 · 2026-05-22T09:35:27.807262+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1765
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-22T09:35:27.861231+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1416
}
```

</details>

---


### Assistant

_source line 1630 · 2026-05-22T09:35:41.636189+00:00_

**Round 1 已派发**：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | 已派发 | 方法严谨性 + 实验设计（梯度分析、C1 ablation、2D 分解、统计可靠性） |
| Reviewer 2 | 已派发 | 新颖性 + 完整性（MaskLLM 区分、贡献 framing、related work、跨架构证据、写作） |
| 视觉审查 Agent | 已启动 | PDF 排版质量（并行，不阻塞） |
| 外部审稿 | 未配置 | — |

等待两位 Reviewer 独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 136

## Round 136

2 recorded events


### User

_source line 1631 · 2026-05-22T09:41:49.259647+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## 总体评分
**Overall**: 3.0 (Findings)
**Confidence**: 4/5 (Quite sure. I tried to check the important points carefully.)
**一句话总结**: 扎实的实证研究，分析框架有价值，但核心配方与 MaskLLM 高度重叠、无实际加速、知识密集型任务系统性退步未解释，整体贡献停留在 Findings 水平。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 claims 有实验支撑但存在显著 caveats：C1 ablation 有 confound（s42 oracle 来自 earlier run）、coupling alignment dominance 可能是 loss function quality 而非 coupling 机制、知识型退步仅有假说无验证 |
| Excitement | 2/5 | 与 MaskLLM 配方重叠度高、仅 30% sparsity sweet spot、6.4% latency overhead 无实际加速、MMLU/GSM8K 系统性退步限制实用价值 |

---

## Summary

本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor，使用 Gumbel-Sigmoid relaxation + frozen weights + learnable masks。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），并通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type 和 coupling scope 两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证。论文自我定位为 "primarily an empirical study"。

---

## Strengths

**S1. 分析框架设计有新意。** Target-swap ablation (C1, Table 3) 是一个巧妙的实验设计——将 KL 训出的 mask targets 喂给 BCE 训练，从而将 "mask quality" 与 "gradient coupling" 效应解耦。这比简单的 loss function 对比更有深度。per-layer KL control 分离 signal type vs. coupling scope 的设计也值得肯定（§4.4, Table 4）。

**S2. 实验覆盖相对全面。** 5 种 loss 配置的 ablation（Table 4）、3-seed evaluation、predictor bottleneck sensitivity（Appendix B）、temperature schedule sensitivity（Appendix B.1）、OOD evaluation on C4（Appendix D）、跨架构 3 模型——整体实验工程量大且有条理。

**S3. 诚实的自我定位。** 论文明确声明 "we do not propose a new architecture or algorithm"（Introduction para 5），且在 Limitations 节坦率承认知识密集型退步、sparsity ceiling、训练数据同质性。这种诚实度在投稿中比较少见。

**S4. Related Work 非常全面。** 覆盖了 training-free methods（TEAL, CATS, R-Sparse, DIP, SparseInfer）、predictor-based methods（DejaVu, ShadowLLM, FastForward, SVD-CSP）、activation function engineering（ReLU Strikes Back, ProSparse, TurboSparse）、MoE routing（D2D-MoE, Expert Choice, MoNE）、weight pruning（Wanda, SparseGPT, SliceGPT）以及 MaskLLM 的三点详细对比。引用量和质量都很好。

**S5. Compensation redundancy 是有实际价值的发现。** 证明 KL predictor 无需 FastForward 式 +67.2M compensation network（Appendix J），简化了 inference pipeline，这对实际部署有意义。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [Critical, Confidence 4/5] **与 MaskLLM 的新颖性区分不足**
- 具体位置：Section 2 (Related Work), para "Predictor-Based Contextual Sparsity", lines on MaskLLM
- 问题：论文核心配方——frozen weights + learnable masks + forward KL + Gumbel relaxation——与 MaskLLM (NeurIPS 2024 Spotlight) 完全一致。论文给出三点区分：(1) sparsity type (weight vs. activation)、(2) mask generation (direct parameters vs. predictor network)、(3) allocation (N:M groups vs. global top-k)。但这三点都是 application-level 差异而非 methodological innovation：将已有方法从 weight sparsity 迁移到 activation sparsity 本身不构成算法贡献。论文自称贡献在于 analysis framework (target-swap ablation, 2D taxonomy)，但 (a) target-swap ablation 是一个实验设计而非方法、(b) 2D taxonomy 是对已有方法的分类而非新框架。在 "primarily empirical study" 定位下，analysis insights 需要足够 surprising 才能撑起贡献——而 "output-distribution loss 比 per-neuron loss 好" 这个结论的 surprise factor 有限。
- 为什么影响接收：如果核心发现可以总结为 "将 MaskLLM 的 KL 配方从 weight sparsity 改到 activation sparsity，效果比 BCE 好"，则增量贡献可能不足以支撑 Main/Findings。
- 建议修改方向：(a) 更深入讨论为什么 activation sparsity 场景下 coupling 效应比 weight sparsity 更重要（比如 global allocation 使得 inter-layer dependency 更关键），(b) 提供与 MaskLLM 的直接实验对比（如在 activation sparsity 场景下让 MaskLLM 的 direct-parameter masks 也用 KL 训练），(c) 或者将 novelty claim 聚焦在分析发现本身（coupling vs. signal type 分解）并强化其 actionable implications。

**N2** [Critical, Confidence 5/5] **无实际推理加速，实用价值存疑**
- 具体位置：Introduction para 5 ("Wall-clock speedup requires sparse kernel support not addressed here"); Appendix A Table 5 (+6.4% overhead)
- 问题：论文全文围绕 "sparsity prediction quality" 展开，但 sparsity 的终极目标是推理加速。当前结果是：30% unstructured sparsity + 6.4% latency overhead = 净减速。论文在 Appendix A 承认 "the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support"。这意味着论文展示的是一种不能加速的 sparsity 方法。对比同期工作：Polar Sparsity (NeurIPS 2025) 实现 2.2× end-to-end speedup，SVD-CSP (2026) 实现 1.8× speedup。
- 为什么影响接收：一篇 sparsity 论文如果不能展示实际加速（哪怕是 wall-clock 持平），其对社区的实际贡献受到严重质疑。"prediction quality" 改进如果不能转化为下游实际收益，则只是学术练习。
- 建议修改方向：(a) 至少用 Triton block-sparse 或 cuSPARSE 做一个 proof-of-concept speedup 实验、(b) 或者明确将论文 reframe 为 "understanding when KL > BCE for mask training"（纯分析贡献），不再以 sparsity/efficiency 为 selling point。

**N3** [Critical, Confidence 4/5] **知识密集型任务系统性退步未解释**
- 具体位置：Section 4.2 "Task-Type Split" para; Table 2; Limitations section; Section 4.5 (Qwen-14B: GSM8K -20pp, MMLU -2.8pp)
- 问题：KL predictor 在 MMLU 和 GSM8K 上系统性地劣于 TEAL magnitude-based method——跨三个架构、多个 sparsity level 一致退步（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp global allocation）。论文给出的解释是 "forward KL's mode-covering property preserves diverse activation patterns that benefit broad commonsense inference; however, this may dilute task-specific knowledge pathways"（§4.2），但这只是一个未经验证的假说（论文自己标注 "hypothesis"）。对于一个声称 "coupling alignment is the dominant design dimension" 的论文，这种 claim 与实际结果的矛盾是严重的：如果 coupling alignment 真的 dominant，为什么在 knowledge tasks 上反而更差？
- 为什么影响接收：这不是 edge case，而是一整类重要任务的系统性退步。如果 KL 在 MMLU/GSM8K 上一致劣于零训练成本的 TEAL，用户为什么要付出训练代价？这动摇了 method 的实用价值定位。
- 建议修改方向：(a) 至少做 probing 实验验证 "mode-covering dilutes knowledge" 假说（如分析 MMLU 各 subject 的退步分布）、(b) 探索 hybrid 策略（如对不同 layer 或不同 task type 用不同 loss）、(c) 或者诚实 reframe contribution：KL predictor 是一种 commonsense-oriented predictor，不适用于 knowledge-intensive scenarios。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [Major, Confidence 3/5] **C1 target-swap ablation 存在 confound**
- 具体位置：Table 3, footnote †; Section 4.3 "Soft-vs-Hard Confound" para
- 问题：C1 ablation 的核心逻辑是：BCE on KL-derived masks ≈ KL → masks are the driver, not gradient coupling。但 (a) s42 oracle 来自 "an earlier training run"（Table 3 footnote），引入 trajectory dependence；(b) oracle masks 本身编码了 KL training 的 specific trajectory（optimizer state, Gumbel noise），所以 BCE 在这些 targets 上训练本质上是在 distill KL 的 training trajectory，而非独立验证 mask quality；(c) soft-vs-hard confound 虽然论文讨论了（BCE+Gumbel 32.22 vs standard BCE 27.97），但这其实说明 representation form 也 matters——不仅是 mask quality。
- 建议：(a) 用 multiple independent KL runs 的 majority-vote masks 作为 targets 消除 trajectory dependence、(b) 设计 reverse direction ablation（KL on magnitude targets）来完善 causal claim。

**W2** [Major, Confidence 4/5] **"Coupling alignment is the dominant design dimension" 可能是 loss quality 而非 coupling 机制**
- 具体位置：Conclusion; Abstract line 5; Section 4.4 per-layer decomposition
- 问题：论文的核心 claim 是 coupling alignment（通过 output distribution 耦合 gradient）是关键设计维度。但 per-layer KL 已经达到 98% 的 PPL gap（9.05 vs 8.81, Table 4），这说明 cross-layer coupling 几乎不重要——真正重要的是 signal type（output distribution vs. intermediate activations）。这与 "coupling alignment" 这个术语暗示的含义不同：coupling 暗示的是 inter-layer gradient interaction，但实际驱动力是 loss function 的 quality（KL on outputs > MSE on intermediate）。Conclusion 中 "coupling alignment—optimizing through the output distribution—is the dominant design dimension" 这句话 conflates 了 signal type 和 coupling，有误导性。
- 建议：区分 "what to optimize"（output distribution vs. intermediate）和 "how gradients flow"（coupled vs. independent），在 Conclusion 中准确归因。

**W3** [Major, Confidence 4/5] **30% sparsity ceiling 过低，实用场景有限**
- 具体位置：Limitations; Table 2; Section 4.5
- 问题：30% sparsity 是 "lowest-degradation level"——但即使在此水平，MMLU 从 65.27%（dense）降至 40.7%（-24.6pp），GSM8K 从 48.75% 降至 7.5%（-41pp）。这意味着即使是 "最佳" sparsity level，模型能力也已大幅衰退。相比之下，同期 Polar Sparsity 在 50% sparsity 下维持 <1% accuracy drop。论文的 sweet spot 分析（Table 14）显示 35% 已经开始 MMLU 退步（40.4% → 35.5% uniform）。
- 建议：讨论为什么 predictor-based 方法在低于 50% sparsity 就开始严重退化，与 training-free methods 的 degradation curve 做直接对比。

**W4** [Minor, Confidence 3/5] **术语过度创造**
- 具体位置：Throughout paper
- 问题："coupling alignment ranking"、"signal type × coupling scope"、"2D taxonomy" 这些术语包装了相对简单的概念。"coupling alignment ranking" 就是 "按 loss function 类型排序"；"signal type × coupling scope" 就是 "loss target × gradient scope"；"2D taxonomy" 就是一张分类表。过度术语化降低了可读性，让读者花时间 decode 术语而非理解核心 insight。
- 建议：简化术语，使用更直觉的描述。

**W5** [Minor, Confidence 3/5] **Batch size 限制未讨论**
- 具体位置：Appendix A; Section 4.5
- 问题：所有实验使用 batch size 1。Polar Sparsity (NeurIPS 2025) 已证明 contextual sparsity 在 batched inference 下效果显著下降（union of active neurons → dense），这是 contextual sparsity 最大的实用障碍之一。论文完全没有讨论这一维度。
- 建议：至少讨论 batched inference 对 contextual sparsity 的影响，评估 predictor overhead amortization 的可能性。

---

## Questions（需要作者回答）

**Q1.** Per-layer KL 已达 98% of PPL gap (9.05 vs 8.81)。如果 cross-layer coupling 只贡献 2% PPL improvement，为什么 "coupling" 是论文的核心 selling point？downstream 上 24-35% 的 coupling scope 贡献是否足够支撑这个 claim？

**Q2.** MaskLLM 在 activation sparsity 场景下的表现如何？如果将 MaskLLM 的 direct-parameter mask 方案直接应用于 activation sparsity（给每个 token 独立的 learnable masks），KL 的优势是否仍然成立？

**Q3.** MMLU/GSM8K 退步在 14B 上放大（GSM8K -20pp）。是否在更大模型（如 70B）上进行过任何 preliminary evaluation？退步趋势是否随 scale 线性增长？

**Q4.** C1 ablation 中 s42 oracle 的 PPL gap (0.65pp) 显著大于 s123/s456 (<0.02pp)。论文将此归因于 "earlier training run"——这是否意味着 C1 的结论对 oracle provenance 高度敏感？

**Q5.** 论文在 Abstract 中 claim "14.5% PPL reduction"，但这是 matched sparsity (28.5% vs 29.3%) 下的数字。在 exact 30% sparsity 下，TEAL PPL 是 10.82 vs KL 8.81 = 18.6% reduction（Table 2）。为什么选择 matched sparsity 的较保守数字而非 nominal comparison？

---

## Missing References

Related work 已非常全面。以下是可考虑补充的近期工作（非 critical）：

1. **SparseInfer** (Shin et al., 2025) — 已引用 ✓
2. **Polar Sparsity** — 已引用 ✓，但建议在 Limitations 中讨论 batched inference 维度
3. **SVD-CSP** (Serbin et al., 2026) — 已引用 ✓
4. **COTS** (Zhang et al., 2025, arXiv:2511.09822) — "Multi-channel Exploiting: Sparse FFNs for Pre-training and Inference" — 可能遗漏，但发表时间与提交时间接近，非 critical
5. **LazyLLM** (Fu et al., 2024) — token-level dynamic pruning for attention + FFN，与 predictor-based 方法互补，可能值得在 routing section 提及

Overall：Related Work 完整度 **8/10**，属于上乘水平。

---

## 小问题（不影响接收）

- Abstract line 1 "universally use binary cross-entropy (BCE)" — FastForward 用的也是 BCE，但 ShadowLLM 用 MSE，此处 "universally" 不准确
- Table 2 footnote ‡ 说明 actual sparsity 不同（KL 28.5% vs TEAL 29.3%），这个差异虽然在 Appendix D 有 matched comparison，但主文 Table 2 是读者第一印象，建议在表格内更显著标注
- Figure 2 (sparsity sweep) y 轴 range 不清，建议标注 dense baseline
- Appendix G (MSE baseline config) 提到 seed 123 出现 catastrophic failure (PPL=15,789, 5.1% sparsity)——这是 MSE 方法的严重 instability，应在主文更显著提及以加强 KL vs MSE 的论点

---

## 主要优势总结

1. 分析框架（C1 + per-layer KL decomposition）在方法论上有贡献
2. 实验覆盖全面，3-seed evaluation + 跨架构验证
3. 论文写作诚实，不 overclaim
4. Related work 非常 thorough
5. Compensation redundancy 发现有实际价值

## 最终判断

论文是一项扎实的实证工作，但面临三个核心问题：(1) 与 MaskLLM 的 methodological overlap 使得 novelty 主要依赖 analysis framework，而 analysis insights 的 surprise factor 有限；(2) 无实际推理加速使得 practical impact 几乎为零；(3) 知识密集型任务的系统性退步是一个未解决的 fundamental limitation。这些问题使论文更适合 Findings track 而非 Main conference。如果作者能在 rebuttal 中提供 wall-clock speedup proof-of-concept + knowledge task 退步的 mechanistic explanation，评分可能提升至 3.5。


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

_source line 1632 · 2026-05-22T09:41:58.960550+00:00_

Reviewer 2 报告已收到。评分 3.0 (Findings)，核心关切：MaskLLM 新颖性区分、无实际加速、知识密集型任务退步。等待 Reviewer 1 报告后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 137

## Round 137

2 recorded events


### User

_source line 1633 · 2026-05-22T09:42:02.119680+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，Soundness 3/5，Excitement 2/5，Confidence 4/5。

三个 Critical 问题：
1. 与 MaskLLM 核心配方高度重叠（frozen weights + KL + Gumbel），三点区分停留在 application-level
2. 无实际 wall-clock speedup（反而 +6.4% overhead），sparsity 论文的根本价值受质疑
3. MMLU/GSM8K 系统性退步跨三个架构一致出现但仅有未验证假说

三个 Major 问题：C1 ablation 有 trajectory confound、"coupling alignment dominance" claim 实际是 loss quality 而非 coupling 机制、30% sparsity ceiling 过低。

Related Work 完整度 8/10，写作诚实度值得肯定，分析框架（C1 + per-layer decomposition）有价值但不足以撑起 Main conference。

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

_source line 1634 · 2026-05-22T09:42:07.927571+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 138

## Round 138

6 recorded events


### User

_source line 1635 · 2026-05-22T09:42:17.580850+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**审查侧重：方法严谨性 + 实验设计**

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 系统性的实证研究揭示了 KL 蒸馏如何发现与 magnitude 显著不同的 mask 模式，但缺乏实际加速效果且下游知识任务一致性退化，限制了实际影响力。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有充分支撑，但 per-layer KL 分解存在训练-推理不匹配混淆变量，"98% signal type" 的归因方法论可商榷 |
| Excitement | 3.0/5 | 对 sparsity prediction 社区有用的实证发现，但无实际加速且 MMLU/GSM8K 一致退化限制了影响力 |
| Reproducibility | 4/5 | 详尽的超参数、多 seed 评估、完整附录；但 per-layer KL downstream 原始数值未在表格中呈现 |
| Confidence | 4/5 | 仔细检查了关键技术点，对主要结论比较确信 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 无实际推理加速——方法增加 6.4% 延迟开销
- 具体位置：Appendix A (Table 5), §5 Conclusion
- 问题：论文动机是 contextual sparsity 的"potential inference acceleration"（§1），但 Table 5 显示完整 pipeline 增加 6.4% 延迟（126.78 vs 119.11 ms/fwd）。论文明确承认"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support"（Appendix A）。这意味着当前工作在实际部署层面不仅没有加速，反而变慢了。
- 为什么影响接收：一篇关于 sparsity prediction 的论文如果无法展示任何加速效果，其实际贡献局限于 analytical insights。论文虽然诚实地 scope out 了这个问题，但 reviewer 和 AC 会质疑：如果 mask 无法转化为加速，发现更好的 mask 的价值有多大？
- 建议修改方向：(a) 至少使用 Triton block-sparse 或 cuSPARSE 展示某个 sparsity level 的端到端加速；或 (b) 明确将论文重新定位为纯分析贡献（analysis paper），弱化 §1 中关于 acceleration 的动机表述。当前的定位介于两者之间，两头不讨好。
- 置信度：高

**N2** [critical] MMLU/GSM8K 在所有 scale 上一致退化——实用性存疑
- 具体位置：Table 2 (30%: MMLU 40.7 vs TEAL 45.86, -5.2pp; GSM8K 7.5 vs 8.79), Table 13 (14B: GSM8K -20pp), Table 17 (Mistral: GSM8K -7.3pp), §Limitations
- 问题：KL 蒸馏在 commonsense reasoning（ARC-c, WG, HellaSwag, PIQA）上一致优于 TEAL，但在 knowledge-intensive 任务（MMLU, GSM8K）上一致劣于 TEAL，且这种退化在 8B、7B、14B 三个 scale 上均成立。论文对此仅给出假设性解释："forward KL's mode-covering property may dilute task-specific knowledge pathways"（§4.2），但未提供任何实验验证。
- 为什么影响接收：这不是一个 edge case，而是系统性的 failure mode。MMLU 和 GSM8K 是 LLM 评估的核心任务。一个 sparsity prediction 方法如果系统性地损害了模型的知识保留和推理能力，其部署价值会受到严重质疑——即使 PPL 更低。
- 建议修改方向：(a) 至少进行一组实验验证 mode-covering 假设（例如，分析 MMLU-relevant 层的 mask 差异）；(b) 设计 hybrid objective（对 knowledge-critical 层用 magnitude，其他层用 KL）并报告 MMLU 是否恢复；(c) 如果无法解决，需在 abstract/conclusion 更显著地标注此限制。
- 置信度：高

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Per-layer KL 的训练-推理不匹配严重混淆了 2D 分解的因果推断
- 具体位置：§4.5 (Per-Layer KL), Table 4
- 问题：Per-layer KL 的设计是"mask one random layer per step and compute KL on the full model output"。但在推理时，所有 32 层同时被 mask。这意味着 per-layer KL 的训练场景与推理场景存在根本性不匹配——训练时每步只有 1 层被稀疏化，其余 31 层保持 dense；推理时 32 层同时稀疏化。
- 论文确实承认了这一点（§4.5 最后一句："A confound: training masks one layer per step while inference applies all 32; the downstream gap may partly reflect this train--inference shift."），但这个 confound 直接影响了论文最核心的定量结论之一。
- 当 per-layer KL 在 30% 时下游任务表现不如 E2E KL，论文将差距归因于"coupling scope contributes 30-35%"。但这个差距的一部分（甚至大部分）可能来自训练-推理不匹配，而非缺乏 cross-layer coupling。
- 50% 时 per-layer KL 退化到 34.85（vs E2E 11.92），退化幅度远超 30%。论文将此解释为"coupling transitions from optional refinement to essential coordination as sparsity increases"。但更 parsimonious 的解释是：50% sparsity 下 train-inference mismatch 更严重（训练时 1/32 层 50% sparse vs 推理时 32/32 层 50% sparse）。
- 建议：(a) 训练 per-layer KL 时逐步增加每步 mask 的层数（如 1→4→16→32），观察性能曲线；(b) 至少讨论这个 confound 的量级估计。
- 置信度：高

**W2** [major] "Signal type accounts for 98% of PPL gap" 的归因方法论不严谨
- 具体位置：§4.5
- 问题：分解公式为 Total gap = (18.52 - 8.81) = 9.71; Signal type = (18.52 - 9.05) = 9.47 (97.5%); Coupling scope = (9.05 - 8.81) = 0.24 (2.5%)。这个分解隐含两个假设：(1) signal type 和 coupling scope 是正交的（无交互效应），(2) 分解是可加的。
- 但实际上，"signal type" 在这里不是一个 clean 的单变量——从 MSE 切换到 KL，不仅改变了 loss target（中间层 vs 输出分布），也改变了 gradient flow 拓扑、优化景观、以及 loss surface 的曲率。论文在脚注中承认了这一点（"this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled"），但 98% 这个数字在正文中被当作主要结论反复引用（Abstract、§1、§4.5、§5），读者很容易将其理解为一个 clean 的因果归因。
- 建议：(a) 在正文中更显著地注明这是 upper bound 估计而非精确归因；(b) 设计一个中间实验（如：per-layer KL on hidden states，即 per-layer scope + KL loss type on intermediate representations）来部分解耦 signal type 和 gradient flow topology。
- 置信度：高

**W3** [major] WikiText-103 训练 → WikiText-2 评估：同分布问题
- 具体位置：§4.1 (Experimental Setup), Appendix D (OOD)
- 问题：WikiText-103 和 WikiText-2 均来自 English Wikipedia 的 Good and Featured articles，本质上是同分布的不同 split。主表（Table 2）的所有 PPL 比较都基于这个 near-identical 分布，严格来说不能称为"评估泛化能力"。
- C4 OOD 评估部分缓解了这个问题，但：(a) 30% 只有 2-seed（global）或 3-seed 但 CV=6.3%（uniform），远高于 in-domain 的 0.2%；(b) C4 PPL 的绝对值（16.03 global / 16.98 uniform）大幅偏离 dense baseline（9.21），说明 predictor 在 OOD 上的质量显著下降；(c) downstream robustness（Table 11）只报告了 seed 42，不是 multi-seed。
- 建议：(a) C4 评估至少做 3-seed 一致性检查；(b) 在主表或 §4.2 中报告 C4 PPL 作为正式 metric，而非仅放在附录。
- 置信度：高

**W4** [major] C1 Target-Swap Ablation 的因果推断存在微妙的循环性
- 具体位置：§4.4 (Table 3)
- 问题：C1 的逻辑是："KL-derived masks 被提取 → BCE 在这些 masks 上训练 → BCE 匹配 KL → 结论：mask 质量驱动推理质量，而非 coupling 机制。" 这个设计巧妙，但存在微妙问题：
  - (a) KL-derived oracle masks 来自特定训练轨迹（optimizer state, data order, Gumbel noise），是一个 point estimate。虽然 3-seed 一致性（≤1.70pp）提供了部分鲁棒性证据，但 oracle mask 的质量仍然依赖于 KL 训练的具体收敛路径。Appendix P 承认了"trajectory-dependent confounds"但未量化。
  - (b) 50% 只有 s42 一个 seed，且 s42 的 oracle 来自"an earlier training run"（Table 3 footnote），与 s123/s456 的 retrained oracles 条件不完全一致。
  - (c) "mask quality" 本身是用 KL 定义的——KL-optimal masks 在 KL 评估下表现好，这有 tautological 成分。更有说服力的证据是 downstream 表现，但 C1 的 downstream 只在 30% 有 3-seed，50% 只有 s42。
- 建议：(a) 50% C1 应补充 s123/s456 结果；(b) 报告 C1 downstream 的 full suite（包括 HellaSwag/PIQA）。
- 置信度：中高

**W5** [minor] MSE baseline 在 50% 的有效性存疑——实质上是 single-seed
- 具体位置：Table 4, Appendix G
- 问题：MSE 50% 的 s123 出现灾难性失败（PPL=15,789, 实际 sparsity 只有 5.1%）。论文在 Table 4 脚注标注了 $^\S$，但主表只报告 s42 的 229.26。这意味着 MSE 在 50% 的对比本质上是 single-seed——这对一个用于支撑论文核心 claim 的 baseline 来说是不够的。
- 此外，s123 的灾难性失败本身就是一个重要的负面结果（MSE 对初始化极其敏感），值得在正文中更显著地讨论，而非仅在附录中提及。
- 建议：(a) 在 Table 4 中注明 MSE 50% 是 s42 only，或报告存活 seed 的均值；(b) 在正文 §4.5 中讨论 MSE 的初始化敏感性。
- 置信度：高

**W6** [minor] Actual sparsity mismatch (KL 28.5% vs TEAL 29.3% at 30% target) 对 downstream 对比的影响未量化
- 具体位置：Table 2 footnote $^\ddagger$, Appendix C, Appendix D
- 问题：论文提供了 matched-sparsity PPL 对比（Appendix D: TEAL at 28.5% = 10.30 vs KL 8.81），但 downstream task 对比（Table 2: MMLU 40.7 vs 45.86）仍然是在不同 actual sparsity 下进行的。0.8pp 的 sparsity 差异在 PPL 上影响不大，但在 MMLU 这类对 capacity 敏感的任务上可能产生非对称影响——TEAL 比 KL 多保留 0.8pp 的神经元可能对 knowledge-intensive 任务更重要。
- 建议：在 Appendix 中补充 TEAL at 28.5% actual sparsity 的 downstream 数字以排除这个 confound。
- 置信度：中

---

## 小问题（不影响接收）

1. **Multi-seed 覆盖不一致**：Table 2 中 KL 30%/50% 有 3-seed，但 TEAL 和 BCE 的部分配置只有 seed 42（尤其是 downstream tasks）。虽然 TEAL 是确定性的（不需要 multi-seed），但 BCE 30% global 只报告了单次结果。建议统一标准。

2. **Per-layer KL downstream 数值缺失**：§4.5 引用了 per-layer KL 的 downstream 分解百分比（30.5% ARC-c, 35.2% WG, 24% MMLU 等），但 per-layer KL 的 downstream 原始数值既不在主表也不在附录表格中（仅在文字中隐含）。读者无法独立验证这些百分比。建议增加一个包含 per-layer KL downstream 数值的表格。

3. **§3.6 梯度分析是定性的**：论文将 §3.6 定位为"suggestive"（合理），但正文和 abstract 中引用时有时暗示更强的因果关系。建议统一用语。

4. **Forward KL vs Reverse KL 论证**：§3.4 中关于 mode-covering 对 sparsity prediction 重要性的论证（"false negatives cascade... false positives merely waste capacity"）是直觉性的但未经形式化证明。这在实证论文中可以接受，但需注意 §4.5 的 reverse KL 结果（30% 3-seed）显示 reverse KL 在 commonsense 任务上也优于 TEAL，削弱了 mode-seeking 的 "missing critical neurons" 论证。

5. **Compensation redundancy**：仅在 30%（s42, s456）和 50%（s42）测试。如果声称 "redundant at both tested sparsity levels"（§1 contributions），至少应在两个 sparsity level 各有 2+ seed。

---

## 需要作者回答的问题

**Q1**：Per-layer KL 在 30% 和 50% 的 downstream 原始数值是多少？请提供 ARC-c, WG, MMLU, GSM8K, HellaSwag, PIQA 的具体数字和 seed 信息（目前只有分解百分比但无法 verify）。

**Q2**：Per-layer KL 训练时如果 mask K>1 层/步（如 K=8 或 K=32），性能如何变化？这能帮助量化训练-推理不匹配的贡献 vs coupling scope 的贡献。

**Q3**：MMLU/GSM8K 退化是否与特定层的 mask divergence 相关？例如，late layers（论文显示 Jaccard divergence 最高的区域）是否恰好是存储 factual knowledge 的层？这可以通过比较 KL/magnitude masks 在 MMLU-relevant prompts 上的 per-layer divergence 来初步检验。

**Q4**：MSE s123 在 50% 的灾难性失败——是 Lagrangian controller 未收敛还是 MSE 本身的优化景观问题？是否有 training curve 可以辅助诊断？

**Q5**：如果用更多样化的训练数据（如 C4 或 RedPajama 的子集替代 WikiText-103），MMLU regression 是否会缓解？

**Q6**：论文使用 $T=1$（无温度缩放）进行 KL 蒸馏，引用了 Hinton et al., 2015。是否尝试过 $T>1$？在标准知识蒸馏中，$T=2$-$4$ 通常优于 $T=1$。

---

## Missing References

未发现关键缺失引用。Related work 覆盖了 training-free sparsity、predictor-based methods、static correction、activation engineering、weight pruning/distillation 和 MoE routing 等主要方向，引用充分。

可考虑补充：
- Alizadeh et al., 2024 ("LLM in a Flash") — 关于 flash memory 上的 sparse inference 部署，与本文的"无加速"讨论互补。
- Wei et al., 2023 (Outlier Suppression+) — activation outlier 分布对 sparsity prediction 的影响。

---

## 主要优势

1. **系统性实证设计**：5 种 loss function（Forward KL, Reverse KL, JSD, BCE, MSE）的完整对比，配合 Gumbel/STE relaxation 的交叉消融，构成了目前该方向最全面的实证研究。

2. **C1 Target-Swap Ablation 设计巧妙**：通过将 KL-derived masks 作为 BCE 训练目标，解耦了"发现 vs 利用"，是一个有创意的因果推断实验。虽然存在 W4 所述的微妙问题，但整体设计思路值得肯定。

3. **诚实的 limitation 报告**：论文没有回避负面结果（MMLU/GSM8K 退化、无加速、OOD variance、MSE seed 失败），均在正文或附录中明确报告。这种透明度值得赞赏。

4. **多架构/多 scale 初步验证**：Mistral-7B（3-seed, Table 16-17）和 Qwen-2.5-14B（Table 13）的跨架构评估，虽然不是深入分析，但增强了结论的初步泛化性。

5. **实用的分类框架**：Correction Granularity × Training Signal Coupling 的 2D taxonomy（Table 1）为后续工作提供了有用的概念工具，尽管部分 cell 为空。

6. **详尽的附录**：18 页中有 10 页附录，涵盖 bottleneck sensitivity、temperature schedule、training convergence、penalty dynamics、OOD evaluation、mask visualization 等，可重现性高。

---

## 总结

论文是一项扎实的实证分析，核心发现（KL 蒸馏发现与 magnitude 显著不同的 mask 模式，signal type 对 PPL 的贡献远大于 coupling scope）对 sparsity prediction 社区有参考价值。C1 ablation 和 5-way loss comparison 是主要亮点。

但三个关键短板限制了论文的 impact：(1) 无实际推理加速（反而增加 6.4% 延迟）；(2) knowledge-intensive 任务一致退化，且缺乏解释；(3) per-layer KL 分解的 train-inference mismatch 混淆了论文最核心的定量结论。这些问题使论文更适合 Findings 而非主会议。


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

_source line 1636 · 2026-05-22T09:43:05.311660+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**Overall**: 3.0 (Findings), Soundness 3/5, Excitement 2/5, Confidence 4/5\n\n## Summary\n本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor，使用 Gumbel-Sigmoid relaxation + frozen weights + learnable masks。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），并通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type 和 coupling scope 两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证。论文自我定位为 \"primarily an empirical study\"。\n\n## Strengths\nS1. 分析框架设计有新意（C1 + per-layer KL decomposition）\nS2. 实验覆盖相对全面（5 loss configs, 3-seed, sensitivity sweeps, OOD, 跨架构）\nS3. 诚实的自我定位（明确声明非 new architecture/algorithm）\nS4. Related Work 非常全面（8/10）\nS5. Compensation redundancy 是有实际价值的发现\n\n## Must-Fix 问题\n\n**N1** [Critical, Confidence 4/5] **与 MaskLLM 的新颖性区分不足**\n核心配方——frozen weights + learnable masks + forward KL + Gumbel relaxation——与 MaskLLM (NeurIPS 2024 Spotlight) 完全一致。三点区分（sparsity type / mask generation / allocation）都是 application-level 差异而非 methodological innovation。论文自称贡献在 analysis framework，但 target-swap ablation 是实验设计而非方法，2D taxonomy 是分类表而非新框架。\"output-distribution loss 比 per-neuron loss 好\" 的 surprise factor 有限。\n\n**N2** [Critical, Confidence 5/5] **无实际推理加速，实用价值存疑**\n30% unstructured sparsity + 6.4% latency overhead = 净减速。对比 Polar Sparsity (NeurIPS 2025) 2.2× speedup, SVD-CSP 1.8× speedup。\"prediction quality\" 改进不能转化为实际收益则只是学术练习。\n\n**N3** [Critical, Confidence 4/5] **知识密集型任务系统性退步未解释**\nKL 在 MMLU/GSM8K 上跨三个架构一致劣于 TEAL（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp）。仅有假设性解释（\"mode-covering may dilute knowledge pathways\"），未验证。如果 coupling alignment 真的 dominant，为什么 knowledge tasks 上反而更差？\n\n## Should-Fix 问题\n\n**W1** [Major, Confidence 3/5] **C1 ablation 存在 confound**\n(a) s42 oracle 来自 earlier training run（trajectory dependence）；(b) oracle masks 编码了 KL specific trajectory；(c) soft-vs-hard confound（BCE+Gumbel 32.22 vs standard BCE 27.97 说明 representation form 也 matters）。\n\n**W2** [Major, Confidence 4/5] **\"Coupling alignment dominance\" 可能是 loss quality 而非 coupling 机制**\nPer-layer KL 达 98% PPL gap → cross-layer coupling 几乎不重要 → 真正重要的是 signal type（output distribution vs intermediate activations）。Conclusion 中 \"coupling alignment\" conflates 了 signal type 和 coupling。\n\n**W3** [Major, Confidence 4/5] **30% sparsity ceiling 过低**\n即使在 30%，MMLU 65.27→40.7（-24.6pp），GSM8K 48.75→7.5（-41pp）。对比 Polar Sparsity 50% sparsity < 1% accuracy drop。\n\n**W4** [Minor] **术语过度创造**\n\"coupling alignment ranking\"、\"signal type × coupling scope\" 包装了相对简单的概念。\n\n**W5** [Minor] **Batch size 限制未讨论**\nPolar Sparsity 已证明 contextual sparsity 在 batched inference 下效果显著下降。\n\n## Questions\nQ1. Per-layer KL 达 98% PPL gap，为什么 \"coupling\" 是核心 selling point？\nQ2. MaskLLM 在 activation sparsity 场景下表现如何？\nQ3. 14B GSM8K -20pp 是否随 scale 增长？\nQ4. C1 s42 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？\nQ5. Abstract \"14.5% PPL reduction\" 是 matched sparsity 数字，为什么不用 nominal 18.6%？\n\n## Missing References\nRelated work 已非常全面（8/10）。可补充 COTS (Zhang et al., 2025) 和 LazyLLM (Fu et al., 2024)。\n\n## 小问题\n- Abstract \"universally use BCE\" 不准确（ShadowLLM 用 MSE）\n- Table 2 actual sparsity 差异应更显著标注\n- MSE s123 catastrophic failure 应在主文更显著提及"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n**Overall**: 3.0 (Findings), Soundness 3/5, Excitement 2/5, Confidence 4/5\n\n## Summary\n本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor，使用 Gumbel-Sigmoid relaxation + frozen weights + learnable masks。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），并通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type 和 coupling scope 两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证。论文自我定位为 \"primarily an empirical study\"。\n\n## Strengths\nS1. 分析框架设计有新意（C1 + per-layer KL decomposition）\nS2. 实验覆盖相对全面（5 loss configs, 3-seed, sensitivity sweeps, OOD, 跨架构）\nS3. 诚实的自我定位（明确声明非 new architecture/algorithm）\nS4. Related Work 非常全面（8/10）\nS5. Compensation redundancy 是有实际价值的发现\n\n## Must-Fix 问题\n\n**N1** [Critical, Confidence 4/5] **与 MaskLLM 的新颖性区分不足**\n核心配方——frozen weights + learnable masks + forward KL + Gumbel relaxation——与 MaskLLM (NeurIPS 2024 Spotlight) 完全一致。三点区分（sparsity type / mask generation / allocation）都是 application-level 差异而非 methodological innovation。论文自称贡献在 analysis framework，但 target-swap ablation 是实验设计而非方法，2D taxonomy 是分类表而非新框架。\"output-distribution loss 比 per-neuron loss 好\" 的 surprise factor 有限。\n\n**N2** [Critical, Confidence 5/5] **无实际推理加速，实用价值存疑**\n30% unstructured sparsity + 6.4% latency overhead = 净减速。对比 Polar Sparsity (NeurIPS 2025) 2.2× speedup, SVD-CSP 1.8× speedup。\"prediction quality\" 改进不能转化为实际收益则只是学术练习。\n\n**N3** [Critical, Confidence 4/5] **知识密集型任务系统性退步未解释**\nKL 在 MMLU/GSM8K 上跨三个架构一致劣于 TEAL（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp）。仅有假设性解释（\"mode-covering may dilute knowledge pathways\"），未验证。如果 coupling alignment 真的 dominant，为什么 knowledge tasks 上反而更差？\n\n## Should-Fix 问题\n\n**W1** [Major, Confidence 3/5] **C1 ablation 存在 confound**\n(a) s42 oracle 来自 earlier training run（trajectory dependence）；(b) oracle masks 编码了 KL specific trajectory；(c) soft-vs-hard confound（BCE+Gumbel 32.22 vs standard BCE 27.97 说明 representation form 也 matters）。\n\n**W2** [Major, Confidence 4/5] **\"Coupling alignment dominance\" 可能是 loss quality 而非 coupling 机制**\nPer-layer KL 达 98% PPL gap → cross-layer coupling 几乎不重要 → 真正重要的是 signal type（output distribution vs intermediate activations）。Conclusion 中 \"coupling alignment\" conflates 了 signal type 和 coupling。\n\n**W3** [Major, Confidence 4/5] **30% sparsity ceiling 过低**\n即使在 30%，MMLU 65.27→40.7（-24.6pp），GSM8K 48.75→7.5（-41pp）。对比 Polar Sparsity 50% sparsity < 1% accuracy drop。\n\n**W4** [Minor] **术语过度创造**\n\"coupling alignment ranking\"、\"signal type × coupling scope\" 包装了相对简单的概念。\n\n**W5** [Minor] **Batch size 限制未讨论**\nPolar Sparsity 已证明 contextual sparsity 在 batched inference 下效果显著下降。\n\n## Questions\nQ1. Per-layer KL 达 98% PPL gap，为什么 \"coupling\" 是核心 selling point？\nQ2. MaskLLM 在 activation sparsity 场景下表现如何？\nQ3. 14B GSM8K -20pp 是否随 scale 增长？\nQ4. C1 s42 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？\nQ5. Abstract \"14.5% PPL reduction\" 是 matched sparsity 数字，为什么不用 nominal 18.6%？\n\n## Missing References\nRelated work 已非常全面（8/10）。可补充 COTS (Zhang et al., 2025) 和 LazyLLM (Fu et al., 2024)。\n\n## 小问题\n- Abstract \"universally use BCE\" 不准确（ShadowLLM 用 MSE）\n- Table 2 actual sparsity 差异应更显著标注\n- MSE s123 catastrophic failure 应在主文更显著提及"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-22T09:43:27.179501+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21867
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-22T09:43:28.234386+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n**Overall**: 3.0 (Findings), Soundness 3.5/5, Excitement 3.0/5, Confidence 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 无实际推理加速——方法增加 6.4% 延迟开销\nTable 5 显示 +6.4% latency（126.78 vs 119.11 ms/fwd）。论文承认 unstructured masks 无法转化为 wall-clock speedup。建议 Triton block-sparse POC 或 reframe 为纯分析论文。\n\n**N2** [critical] MMLU/GSM8K 在所有 scale 上一致退化——实用性存疑\nKL 在 commonsense（ARC-c, WG, HS, PIQA）上优于 TEAL，但 knowledge-intensive（MMLU, GSM8K）上一致劣于 TEAL（8B -5.2pp MMLU; 14B -20pp GSM8K; Mistral -7.3pp GSM8K）。仅有假设性解释。建议验证 mode-covering 假设或设计 hybrid objective。\n\n## Should-Fix 问题\n\n**W1** [major] Per-layer KL 的训练-推理不匹配严重混淆了 2D 分解\nPer-layer KL 训练时 mask 1 layer/step，推理时 32 层同时 mask。30% downstream 差距可能来自 train-inference mismatch 而非缺乏 cross-layer coupling。50% 退化到 34.85（vs E2E 11.92）更可能是 mismatch 放大而非 \"coupling transitions from optional to essential\"。建议训练 per-layer KL 时逐步增加 mask 层数。\n\n**W2** [major] \"Signal type accounts for 98% of PPL gap\" 归因方法论不严谨\n分解假设 signal type 和 coupling scope 正交（无交互效应）。实际上从 MSE→KL 改变了 loss target + gradient flow topology + optimization landscape。论文脚注承认但正文反复引用 98% 作为主结论。建议标注为 upper bound 估计。\n\n**W3** [major] WikiText-103 训练 → WikiText-2 评估：同分布\n两者均来自 English Wikipedia Good/Featured articles，本质同分布。C4 OOD 只有 2-seed（global）或 3-seed 但 CV=6.3%，downstream robustness（Table 11）只有 seed 42。\n\n**W4** [major] C1 Target-Swap Ablation 存在循环性\nKL-derived oracle 来自特定训练轨迹（Gumbel noise, optimizer state），是 point estimate。50% 只有 s42 且 oracle 来自 earlier run。Downstream 50% 也只有 s42。\n\n**W5** [minor] MSE 50% 实质是 single-seed（s123 catastrophic failure, PPL=15789）\n**W6** [minor] Actual sparsity mismatch 对 downstream 影响未量化\n\n## Questions\nQ1. Per-layer KL downstream 原始数值？\nQ2. Per-layer KL mask K>1 layers/step 性能如何？\nQ3. MMLU/GSM8K 退化与特定层 mask divergence 是否相关？\nQ4. MSE s123 50% failure 是 Lagrangian controller 问题还是 MSE 优化景观？\nQ5. 更多样化训练数据是否缓解 MMLU regression？\nQ6. KL 蒸馏 $T>1$ 是否尝试过？\n\n## 主要优势\n1. 5 种 loss function 完整对比，最全面的实证研究\n2. C1 设计巧妙\n3. 诚实的 limitation 报告\n4. 多架构/多 scale 初步验证\n5. 2D taxonomy 有用\n6. 详尽附录，可重现性高\n\n## Missing References\n未发现关键缺失。可补充 LLM in a Flash (Alizadeh et al., 2024), Outlier Suppression+ (Wei et al., 2023)。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n**Overall**: 3.0 (Findings), Soundness 3.5/5, Excitement 3.0/5, Confidence 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 无实际推理加速——方法增加 6.4% 延迟开销\nTable 5 显示 +6.4% latency（126.78 vs 119.11 ms/fwd）。论文承认 unstructured masks 无法转化为 wall-clock speedup。建议 Triton block-sparse POC 或 reframe 为纯分析论文。\n\n**N2** [critical] MMLU/GSM8K 在所有 scale 上一致退化——实用性存疑\nKL 在 commonsense（ARC-c, WG, HS, PIQA）上优于 TEAL，但 knowledge-intensive（MMLU, GSM8K）上一致劣于 TEAL（8B -5.2pp MMLU; 14B -20pp GSM8K; Mistral -7.3pp GSM8K）。仅有假设性解释。建议验证 mode-covering 假设或设计 hybrid objective。\n\n## Should-Fix 问题\n\n**W1** [major] Per-layer KL 的训练-推理不匹配严重混淆了 2D 分解\nPer-layer KL 训练时 mask 1 layer/step，推理时 32 层同时 mask。30% downstream 差距可能来自 train-inference mismatch 而非缺乏 cross-layer coupling。50% 退化到 34.85（vs E2E 11.92）更可能是 mismatch 放大而非 \"coupling transitions from optional to essential\"。建议训练 per-layer KL 时逐步增加 mask 层数。\n\n**W2** [major] \"Signal type accounts for 98% of PPL gap\" 归因方法论不严谨\n分解假设 signal type 和 coupling scope 正交（无交互效应）。实际上从 MSE→KL 改变了 loss target + gradient flow topology + optimization landscape。论文脚注承认但正文反复引用 98% 作为主结论。建议标注为 upper bound 估计。\n\n**W3** [major] WikiText-103 训练 → WikiText-2 评估：同分布\n两者均来自 English Wikipedia Good/Featured articles，本质同分布。C4 OOD 只有 2-seed（global）或 3-seed 但 CV=6.3%，downstream robustness（Table 11）只有 seed 42。\n\n**W4** [major] C1 Target-Swap Ablation 存在循环性\nKL-derived oracle 来自特定训练轨迹（Gumbel noise, optimizer state），是 point estimate。50% 只有 s42 且 oracle 来自 earlier run。Downstream 50% 也只有 s42。\n\n**W5** [minor] MSE 50% 实质是 single-seed（s123 catastrophic failure, PPL=15789）\n**W6** [minor] Actual sparsity mismatch 对 downstream 影响未量化\n\n## Questions\nQ1. Per-layer KL downstream 原始数值？\nQ2. Per-layer KL mask K>1 layers/step 性能如何？\nQ3. MMLU/GSM8K 退化与特定层 mask divergence 是否相关？\nQ4. MSE s123 50% failure 是 Lagrangian controller 问题还是 MSE 优化景观？\nQ5. 更多样化训练数据是否缓解 MMLU regression？\nQ6. KL 蒸馏 $T>1$ 是否尝试过？\n\n## 主要优势\n1. 5 种 loss function 完整对比，最全面的实证研究\n2. C1 设计巧妙\n3. 诚实的 limitation 报告\n4. 多架构/多 scale 初步验证\n5. 2D taxonomy 有用\n6. 详尽附录，可重现性高\n\n## Missing References\n未发现关键缺失。可补充 LLM in a Flash (Alizadeh et al., 2024), Outlier Suppression+ (Wei et al., 2023)。"
  }
}
```

</details>

---


### Tool result

_source line 1639 · 2026-05-22T09:43:29.843457+00:00_

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


### Assistant

_source line 1640 · 2026-05-22T09:43:32.846303+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1641 · 2026-05-22T09:43:35.544134+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论概要：**

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 3.0，Confidence 4/5
- **2 个 Critical 问题**：无实际推理加速（+6.4% overhead）；MMLU/GSM8K 在所有 scale 上一致退化
- **6 个 Major/Minor 问题**：per-layer KL 训练-推理不匹配混淆了 2D 分解；"98% signal type" 归因方法论不严谨；WikiText 同分布评估；C1 ablation 50% 仅 single-seed；MSE 50% 实质 single-seed；sparsity mismatch 对 downstream 影响未量化
- **6 个 Questions**：per-layer KL downstream 原始数值、K>1 层训练、MMLU 退化与层级 mask divergence 的关系、MSE s123 失败诊断、训练数据多样性影响、KL 温度缩放
- **主要优势**：系统性 5-way loss 对比、巧妙的 C1 ablation、诚实的 limitation 报告、详尽附录

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

_source line 1642 · 2026-05-22T09:43:41.408496+00:00_

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


## Round 140

## Round 140

2 recorded events


### User

_source line 1643 · 2026-05-22T09:45:03.519056+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R1-N1: 无实际推理加速**

完全同意。这也是我审稿报告中的 N2（Critical）。Appendix A Table 5 明确显示 +6.4% overhead，论文自己承认 "unstructured element-wise masks do not translate to wall-clock speedup"（Appendix A para 3）。我进一步补充：同期 Polar Sparsity (NeurIPS 2025, 已被论文引用 §2) 实现 2.2× speedup，SVD-CSP (2026, 已引用 §2) 实现 1.8× speedup——本文的 net slowdown 与领域发展方向严重脱节。R1 的两个建议（Triton POC 或 reframe 为分析论文）都是合理的修改方向。

**[AGREE] R1-N2: MMLU/GSM8K 系统性退步**

完全同意。这也是我的 N3（Critical）。补充数据：退步在 Qwen-14B 上更严重——Table 13 (Appendix K) 显示 KL uniform MMLU 63.55% vs TEAL 66.34%（-2.8pp），GSM8K 32.1±5.2% vs TEAL 52.1%（-20pp）。值得注意的是，论文在 §4.2 自己标注了 "hypothesis; mechanistic investigation left to future work"——这表明作者知道没有验证但选择留给未来工作。对于一篇以 "coupling alignment is the dominant design dimension" 为核心 claim 的论文，knowledge tasks 上的系统性劣势是一个严重的 claim-evidence mismatch。

---

## Should-Fix 问题

**[AGREE] R1-W1: Per-layer KL 的训练-推理不匹配混淆了 2D 分解**

同意，且认为这是 R1 最有洞察力的观察。论文自己在 §4.4 末尾也承认了这个 confound："A confound: training masks one layer per step while inference applies all 32; the downstream gap may partly reflect this train-inference shift." 但这个 caveat 只出现在段末一句，而 "coupling scope contributes 24–35% on downstream tasks" 的 claim 却在 Abstract line 5、Conclusion、和 contributions list 中反复出现。

我进一步补充：50% sparsity 下 per-layer KL 退化到 34.85（Table 4）vs E2E 的 11.92——这个 3× gap 更可能是因为训练时只 mask 1/32 层但推理时同时 mask 32 层导致的 distribution shift catastrophe，而非 "coupling transitions from optional refinement to essential coordination"（§4.4）。R1 建议的"逐步增加 mask 层数"实验可以直接验证这个假说。

**[AGREE] R1-W2: 98% 归因方法论不严谨**

同意。这与我的 W2 观点一致。论文脚注（§4.4 footnote on "signal type"）承认 "this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled"——但正文仍然将 98% 作为关键结论反复引用（Abstract, Conclusion, Contributions list）。Signal type 和 coupling scope 之间存在明显的交互效应：改变 loss target 从 MSE 到 KL 同时改变了 (a) 优化目标、(b) gradient flow topology、(c) optimization landscape。98% 这个数字在方法论上是一个 confounded estimate，应标注为 upper bound 而非 point estimate。

**[REBUT] R1-W3: WikiText-103 训练 → WikiText-2 评估：同分布**

部分不同意。R1 说两者"本质同分布"是准确的——都来自 English Wikipedia Good/Featured articles。但论文已经做了 C4 OOD evaluation（Appendix D, Table 10）显示 KL 优势在 OOD 上保持（30%: C4 PPL 16.03±0.01; 50%: 18.40 vs TEAL 38.75, 52.5% relative advantage）。更重要的是，Table 11 (Appendix D) 的 downstream robustness 在 6 个 benchmark 上都显示 Δ≤1.1pp，说明 predictor masks 对 calibration domain shift 是 robust 的。

R1 指出 C4 OOD 只有 2-seed（global）和 downstream 只有 seed 42 是合理的批评——seed 覆盖不足。但 "同分布" 这个批评本身的严重性应该降低，因为 in-domain 和 OOD 的一致性已经得到初步验证。这是一个 **minor** 而非 major 问题。

**[AGREE] R1-W4: C1 Target-Swap Ablation 存在循环性**

同意，这与我的 W1 观点一致。补充证据：Table 3 footnote † 明确说 s42 oracle 来自 "an earlier training run"，且 s42 的 PPL gap（0.65pp）显著大于 retrained seeds s123/s456（<0.02pp）。50% 只有单 seed (s42) 更是明显不足。Appendix P (Oracle Mask Provenance) 也承认 oracle 编码了 "specific training trajectory (optimizer state, data order, Gumbel noise)"。

不过我要补充一个 nuance：s123 和 s456 的 retrained oracles 确实显示了更好的一致性（PPL gap <0.02pp），这在一定程度上缓解了 s42 的 confound。核心问题不是 C1 完全无效，而是其 causal claim 的强度被 confounds 削弱——论文应该将 C1 定位为 "suggestive evidence" 而非 "confirms"（§4.3 用了 "confirms" 三次）。

**[AGREE] R1-W5: MSE 50% 实质是 single-seed**

同意。Appendix G 明确说 seed 123 出现 catastrophic failure（PPL=15,789, 5.1% sparsity）。Table 4 的 MSE 50% 数字（229.26）实际上只代表 seed 42。论文应在主文中更显著标注这一点。不过我要补充：这个 failure 本身也是 MSE 方法 instability 的有力证据——KL 在相同条件下从未出现此类 failure（3-seed CV=0.6%, Appendix F），这反而加强了 KL > MSE 的论点。

**[AGREE] R1-W6: Actual sparsity mismatch 对 downstream 影响未量化**

同意但认为影响有限。Table 2 footnote ‡ 说明 KL 28.5% vs TEAL 29.3%——差 0.8pp。Appendix D (matched sparsity at 28.5%) 显示 PPL 10.30 vs 8.81，KL 优势从 18.6% 缩小到 14.5%，仍然显著。对 downstream 的影响未直接量化，但 0.8pp sparsity 差异不太可能解释 MMLU -5.2pp 或 ARC-c +4pp 的差距。这是一个需要 footnote 但不影响核心结论的 minor 问题。

---

## Questions 回应

**R1-Q1 (Per-layer KL downstream 原始数值)**: 合理问题。§4.4 给出了 coupling scope contribution 的百分比（30–35%）但没有给出 per-layer KL 的原始 downstream 数值，只在 footnote 中说 "E2E KL and per-layer KL are 3-seed means; MSE downstream is seed 42 only"。作者应在 rebuttal 中提供完整数值。

**R1-Q2 (Per-layer KL mask K>1 layers/step)**: 非常好的建议，直接指向 W1 的 train-inference mismatch confound。如果 K=2,4,8,16,32 的 gradual 实验能做出来，可以直接区分 coupling effect 和 mismatch effect。

**R1-Q3 (MMLU/GSM8K 退化与层级 mask divergence 相关性)**: 有价值。Figure 7 (Appendix M) 和 Figure 4 (Appendix E) 提供了 per-layer divergence 数据，但论文没有将其与 per-task performance 关联。这是一个合理的 follow-up 分析。

**R1-Q4 (MSE s123 failure 根因)**: Appendix G 说 "sparsity reaches only 5.1% under the same λ_max cap"——这更可能是 MSE 的 optimization landscape 问题（per-layer gradient 不稳定），而非 Lagrangian controller bug。KL 在相同 controller 下从未出现此 failure。

**R1-Q5 (更多样化训练数据缓解 MMLU regression)**: 有价值但不确定。C4 OOD 的 downstream robustness（Table 11, Δ≤1.1pp）暗示 mask 本身对 domain 不敏感，所以训练数据多样化可能帮助有限。MMLU regression 更可能是 loss function 的固有属性而非训练数据问题。

**R1-Q6 (KL 蒸馏 T>1)**: 有趣的方向。论文 §3.4 提到 "No temperature scaling (T=1) is applied (Hinton et al., 2015)"（Table 4 footnote 引用 Bengio 2013 STE）。T>1 可能 soften output distribution 从而缓解 mode-covering 的过度 diversity。但这改变了 KL 的优化景观，可能需要重新调参。合理的 rebuttal 实验。

---

## Missing References 回应

R1 建议补充 LLM in a Flash (Alizadeh et al., 2024) 和 Outlier Suppression+ (Wei et al., 2023)。

LLM in a Flash 关注的是 flash memory ↔ DRAM 的 data movement optimization 而非 activation sparsity prediction——相关性有限但可在 weight pruning/routing 段提及。Outlier Suppression+ 是量化方法，与本文的 sparsity focus 关系较远。两者都非 critical omission。

---

## 总体评价

R1 和我的评分一致（Overall 3.0 Findings）。我们的核心关切高度重叠：无实际加速 (R1-N1 ↔ 我-N2)、知识型退步 (R1-N2 ↔ 我-N3)、C1 confound (R1-W4 ↔ 我-W1)、98% 归因问题 (R1-W2 ↔ 我-W2)。

R1 独有的最有价值贡献是 **W1 (per-layer KL train-inference mismatch)**——这个观察比我的审稿更深入，指出了 2D 分解的根本方法论缺陷。如果作者不能在 rebuttal 中通过 gradual K 实验回应此点，coupling scope 的整条 contribution line 都会被严重削弱。

我额外强调的 R1 未重点涉及的问题是 **MaskLLM novelty overlap**（我的 N1）——核心配方的重叠使得论文的独立贡献主要依赖 analysis framework，而 analysis insights 的 surprise factor 和 robustness 都受到上述 confounds 的影响。


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

_source line 1644 · 2026-05-22T09:45:16.091298+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 141

## Round 141

10 recorded events


### User

_source line 1645 · 2026-05-22T09:45:17.237602+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。核心结论：

- **6/9 条 [AGREE]**：无加速 (N1)、知识退步 (N2)、per-layer KL mismatch (W1)、98% 归因 (W2)、C1 循环性 (W4)、MSE single-seed (W5)
- **1 条 [REBUT]**：W3 (WikiText 同分布) —— C4 OOD evaluation + downstream robustness (Table 11, Δ≤1.1pp) 提供了初步 OOD 验证，严重性应从 major 降为 minor
- **2 条 nuanced AGREE**：W4 补充了 s123/s456 retrained oracles 的缓解证据；W6 认为 0.8pp sparsity 差异影响有限

特别认同 R1-W1 (per-layer KL train-inference mismatch) 是最深刻的观察——直接动摇了 coupling scope contribution 这条 contribution line。

---

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 与 MaskLLM 的新颖性区分不足**

Reviewer 2 称核心配方与 MaskLLM (NeurIPS 2024) "完全一致"，三点区分只是 "application-level 差异"。我认为这个批评过于简化。

(1) **Mask generation 的差异不是 application-level 的**。MaskLLM 的 masks 是直接可学习参数（one per weight group），训练完成后固定。本文的 masks 由 predictor network 在推理时从 hidden states 生成，每个 token 不同。这是 architecture-level 的差异——前者是参数优化问题，后者是函数逼近问题。predictor 需要从 $\mathbf{x}^{(\ell)}$ 泛化到 unseen inputs（§3.2），MaskLLM 不需要。

(2) **Global top-k allocation 创造了 MaskLLM 不存在的跨层依赖**。MaskLLM 在 fixed N:M groups 内优化（局部独立），本文的 masks 在全模型 global top-k 下竞争（§3.1, Eq. 2）——一个层的 mask 质量直接影响其他层获得的 neuron budget（Appendix E, Figure 4 per-layer retention 分析）。这是 per-layer KL 分解（§4.5）和 allocation strategy 分析（§4.6, Table 14）存在意义的前提。

(3) 不过，我同意 Reviewer 2 关于 **analysis contribution 的定位需要更精确**。C1 target-swap ablation 确实是实验设计而非方法论创新，2D taxonomy 是分类而非理论框架。但 "实验设计创新" 在 empirical study 中是合理的贡献形式——论文明确自我定位为 "primarily an empirical study"（§1 倒数第二段）。

**总结**：方法层面的新颖性确实有限（recipe-level overlap 真实存在），但三点差异中至少两点（predictor network、global allocation）具有非平凡的技术含义。R2 的批评在 "surprise factor 有限" 这一点上是成立的，但 "完全一致" 的措辞过强。

---

**[AGREE] R2-N2: 无实际推理加速**

与我的 R1-N1 一致。论文 Appendix A (Table 5) 明确显示 +6.4% latency overhead。这是一个 critical limitation。不过我要补充一个 nuance：Reviewer 2 引用 Polar Sparsity (2.2× speedup) 和 SVD-CSP (1.8× speedup) 作为对比，但需注意 (a) Polar Sparsity 是 attention head sparsity（结构化），与本文的 FFN neuron sparsity（非结构化）不是同一类问题；(b) SVD-CSP 是 predictor compression 方法，与本文的 training objective 研究不直接可比。直接对比可能误导读者。但核心批评——无加速的 sparsity prediction 实用价值有限——完全成立。

---

**[AGREE] R2-N3: 知识密集型任务系统性退步**

与我的 R1-N2 一致。Table 2（8B MMLU -5.2pp）、Table 13（14B MMLU -8.1pp, GSM8K -20pp）、Table 17（Mistral MMLU tied, GSM8K -7.3pp）构成了跨 scale 的一致证据。论文仅提供假设性解释（§4.2 "mode-covering may dilute task-specific knowledge pathways"），未进行任何验证实验（例如 per-layer mask divergence analysis on MMLU-relevant inputs）。Reviewer 2 提出的反问——"如果 coupling alignment 真的 dominant，为什么 knowledge tasks 反而更差"——有力地指出了论文 narrative 的内在张力。

---

### Should-Fix 问题

**[AGREE] R2-W1: C1 ablation confounds**

与我的 R1-W4 一致。具体补充：

(a) **s42 oracle provenance**: Table 3 footnote 明确标注 s42 oracle 来自 "earlier training run"，而 s123/s456 使用 "matched retrained oracles"。s42 的 0.65pp PPL gap（9.45 vs 8.80）大于 retrained seeds 的 ≤0.02pp gap（如 s123: 8.84 vs 8.83），说明 oracle provenance 确实影响结论。

(b) **soft-vs-hard confound**: BCE+Gumbel (32.22) 实际上比 standard BCE (27.97) 更差，这恰恰说明 Gumbel relaxation 与 BCE 的组合是有害的。但论文用此证明 "softness alone does not explain KL's advantage"（§4.4）——这个推理是正确的（Gumbel 对 BCE 有害但对 KL 有利，说明 loss function 才是关键变量），但需要更清晰地表述。

(c) Reviewer 2 的 "(b) oracle masks 编码了 KL specific trajectory" 与 Appendix P 的承认一致。我认为 3-seed 一致性（≤1.70pp at 30%）提供了 partial 但非 conclusive 的鲁棒性证据。

---

**[AGREE] R2-W2: "Coupling alignment" 术语混淆 signal type 和 coupling**

这是一个比我原始审稿中提出的更精确的批评。论文 §5 Conclusion: "Coupling alignment---optimizing through the output distribution---is the dominant design dimension"——但论文自己的 per-layer KL 实验（§4.5）显示 coupling scope 只贡献 PPL gap 的 2.5%！"Coupling alignment" 这个术语暗示 cross-layer coupling 是核心，但数据说明是 signal type（output distribution vs intermediate representation）才是核心。

Reviewer 2 正确指出了这个 conflation：如果 per-layer KL（无 cross-layer coupling 但有 output-distribution signal）已经达到 E2E KL 98% 的效果，那么 "coupling" 不应该是 selling point。论文应该用 "output-distribution alignment" 而非 "coupling alignment" 作为核心术语。

---

**[REBUT] R2-W3: 30% sparsity ceiling 过低（对比 Polar Sparsity 50% < 1% drop）**

这个对比不公平，原因有三：

(1) **Sparsity 类型不同**。Polar Sparsity 是 attention head sparsity（结构化、粗粒度），本文是 FFN neuron sparsity（非结构化、细粒度）。两者的 capacity-quality tradeoff 完全不同。移除一个 attention head 与移除单个 FFN neuron 的影响不可直接对比。

(2) **模型基线不同**。Polar Sparsity 的 "< 1% drop" 通常报告在特定 benchmark 上的 best-case scenario。本文的 MMLU 65.27→40.7 确实是大幅退化，但这是 FFN activation sparsity 的 *所有* 方法都面临的问题——TEAL 也只有 45.86（-19.4pp），BCE 更差（36.3）。这是问题的固有难度，不是本文方法的特有缺陷。

(3) **Dense baseline 的 capacity utilization 不同**。LLaMA-3.1-8B 在 MMLU 上只有 65.27%（远非完美），说明 FFN 的 capacity 已被高度利用。移除 30% 的 FFN neurons 必然导致显著退化。

我同意 Reviewer 2 指出了 practical utility 的问题，但用 Polar Sparsity 的数字直接对比来论证 "30% ceiling 过低" 是不恰当的。

---

**[AGREE] R2-W4: 术语过度创造**

同意这是一个 minor 但 valid 的风格问题。"coupling alignment ranking" 本质上就是 "loss function comparison"，"signal type × coupling scope" 就是 "loss target × optimization scope"。过度包装简单概念确实增加了阅读负担。但这不影响技术正确性。

---

**[AGREE] R2-W5: Batch size 限制未讨论**

这是一个被论文完全忽略的实际问题。Per-token contextual sparsity 在 batched inference 下会遇到 "mask union" 问题——batch 内不同 token 需要不同 neurons，实际保留的 neuron set 可能接近 dense。Polar Sparsity（§2, Related Work 中已引用）的经验表明这个问题严重。论文应在 Limitations 中讨论 batch size 对 effective sparsity 的影响。

---

### Questions

**R2-Q1: Per-layer KL 达 98% PPL gap，为什么 coupling 是核心 selling point？**

[AGREE] 这与 W2 一致。论文的数据不支持 "coupling" 作为核心 selling point。如果将 framing 改为 "output-distribution signal type 是 dominant dimension"（而非 "coupling alignment"），narrative 会更诚实。

**R2-Q2: MaskLLM 在 activation sparsity 场景下表现如何？**

[AGREE] 这是一个合理的 baseline 请求。论文声称与 MaskLLM 有本质差异（§2），但未提供 MaskLLM 在 activation sparsity 上的实验。即使 MaskLLM 的 static N:M design 无法直接做 per-token activation sparsity，也应讨论为什么不能适配以及性能预期。

**R2-Q3: 14B GSM8K -20pp 是否随 scale 增长？**

[AGREE] 只有两个 scale（8B, 14B）无法确定趋势。但 8B GSM8K -1.3pp（7.5 vs 8.79）到 14B GSM8K -20pp 的跳跃确实令人担忧（Table 2, Table 13）。如果退化随 scale 增长，这会严重限制方法的 scalability。论文应至少讨论这个风险。

**R2-Q4: C1 s42 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？**

[AGREE] 如上 W1(a) 所述。s42 使用 earlier training run 的 oracle，gap 0.65pp；retrained oracles（s123, s456）gap ≤0.02pp。这个差异说明 oracle provenance 确实有影响，尽管影响量级（0.65pp）相对于 KL vs magnitude-BCE 的差距（11.79 vs 28.13）仍然很小。

**R2-Q5: Abstract matched sparsity 数字**

[REBUT] 使用 matched sparsity（14.5%）比 nominal（18.6%）更保守、更诚实。KL actual sparsity 28.5% vs TEAL 29.3% 存在 0.8pp 差异，用 matched sparsity 数字排除了这个 confound。论文在 §1 和 Appendix D 中都注明了这一点。如果用 nominal 18.6%，反而会因为 sparsity mismatch 而膨胀 advantage。Reviewer 2 的问题本身是合理的（读者可能困惑为什么不用更大的数字），但论文的选择是正确的。

---

### Missing References

[AGREE] COTS (Zhang et al., 2025) 和 LazyLLM (Fu et al., 2024) 是合理的补充建议，分别涉及 token-level sparsity 和 lazy token processing，与本文的 contextual sparsity 方向相关。

---

### 小问题

[AGREE] "universally use BCE" 确实不准确——ShadowLLM 用 MSE。建议改为 "primarily rely on decomposed losses (BCE or per-layer MSE)"。

[AGREE] Table 2 actual sparsity 差异应更显著标注。

[AGREE] MSE s123 catastrophic failure 应在正文更显著提及（与我的 R1-W5 一致）。

---

### 综合评价

Reviewer 2 的审稿质量较高，多数批评有据。我与 R2 在以下核心问题上达成共识：
1. **无实际加速** (N2 = 我的 N1)
2. **MMLU/GSM8K 系统退化未解释** (N3 = 我的 N2)
3. **C1 confounds** (W1 ≈ 我的 W4)
4. **术语混淆** (W2，R2 比我更精确地指出了 "coupling alignment" 术语问题)

我与 R2 的主要分歧在：
1. **MaskLLM 新颖性** (N1)：R2 认为 "完全一致"，我认为 predictor network 和 global allocation 是非平凡差异，但同意方法新颖性有限
2. **30% ceiling 对比 Polar Sparsity** (W3)：R2 的对比不公平（不同 sparsity 类型），但指出的 practical utility 问题成立
3. **Abstract matched sparsity 数字** (Q5)：R2 质疑用 14.5% 而非 18.6%，我认为论文选择更保守更正确

Overall 评分，我同意 R2 的 3.0 (Findings)，但 Excitement 我给 3.0 vs R2 的 2.0——论文的 analysis contributions（C1 ablation, 5-way loss comparison）在 empirical study 类别中有中等价值，2.0 偏低。


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

_source line 1646 · 2026-05-22T09:45:40.563652+00:00_

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

_source line 1647 · 2026-05-22T09:45:41.115959+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T09:35:27.393344+00:00\", \"completed_at\": \"2026-05-22T09:35:32.467937+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 6pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-22T09:45:41.166633+00:00_

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

_source line 1649 · 2026-05-22T09:45:41.217214+00:00_

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

_source line 1650 · 2026-05-22T09:47:18.928495+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 20 (fresh) — Issues from roundtable review\n  # ============================================================\n\n  - id: \"R20-N1\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无法转化为 speedup\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 20\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出\"}\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。Introduction 仍暗示 efficiency gain。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-N1 + R2-N2, both Critical)。Table 5 实测 +6.4%。Introduction para 1 仍以 'potential inference acceleration' 为动机。R2 补充: 同期 Polar Sparsity 2.2× speedup, SVD-CSP 1.8× speedup。R1 反驳 Polar Sparsity 对比 (不同 sparsity 类型) 但同意核心批评。\"}\n    action_items:\n      - {round: 19, action: \"Intro 去掉 efficiency motivation\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 在所有 scale (8B/7B/14B) 上系统性退步，仅有未验证假说\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 20\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"首次提出 knowledge-intensive regression\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。假设性解释未验证。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-N2 + R2-N3, both Critical)。8B: MMLU -5.2pp, GSM8K -1.3pp; 14B: MMLU -8.1pp (global), GSM8K -20pp (σ=5.2pp); Mistral: GSM8K -7.3pp。§4.2 标注 'hypothesis; mechanistic investigation left to future work'。R2 指出: 如果 coupling alignment dominant，为何 knowledge tasks 更差？Claim-evidence mismatch。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N3\"\n    summary: \"与 MaskLLM 核心配方高度重叠 (frozen weights + KL + Gumbel)，新颖性依赖 analysis framework\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 20\n    mentions:\n      - {round: 16, reviewers: [2], note: \"首次提出 novelty 不足\"}\n      - {round: 19, reviewers: [1, 2], note: \"[分歧] R2 Critical; R1 REBUT (weight vs activation 是本质不同问题域)\"}\n      - {round: 20, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical: 三点区分均 application-level。R1 REBUT: predictor network (函数逼近 vs 参数优化) 和 global top-k allocation (跨层依赖) 是非平凡差异，但同意方法新颖性有限、'analysis contribution 定位需更精确'。Director 判定: recipe-level overlap 真实存在，predictor+global allocation 有技术差异但不构成 strong novelty。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL 训练-推理不匹配 (1 layer/step vs 32 layers) 混淆了 2D 分解的因果推断\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W1 Major, R2 agrees 且称 'R1 最有洞察力的观察')。§4.5 末尾仅一句 caveat，但 'coupling scope 24-35%' 在 Abstract/Conclusion/Contributions 反复引用。50% per-layer KL 退化到 34.85 (vs E2E 11.92) 更可能是 mismatch catastrophe 而非 coupling 必要性。需 gradual K (1→4→16→32) 实验验证。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"'Coupling alignment' 术语 conflates signal type (what to optimize) 和 coupling mechanism (how gradients flow)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"97.5% 归因仅适用 PPL (R19-N1); 术语 overclaim (R19-W5)\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W2 + R2-W2, both Major → Director escalates to Critical due to pervasive impact on narrative)。98% gap 由 signal type 解释，但正文用 'coupling alignment' 作核心术语——暗示 cross-layer coupling 是关键，与 per-layer KL 数据矛盾。脚注承认 signal type 维度 entails gradient flow topology 差异但未独立控制。98% 应标注为 upper bound 而非 point estimate。建议术语: 'output-distribution alignment' 而非 'coupling alignment'。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"C1 target-swap ablation 存在 trajectory confound + soft-vs-hard confound，因果推断力受限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。循环论证 + confound 叠加。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W4 Major + R2-W1 Major)。s42 oracle from earlier run (0.65pp gap vs retrained ≤0.02pp)。50% 仅 s42。§4.3 用 'confirms' 三次但应降为 'suggestive evidence'。Retrained s123/s456 一致性部分缓解但不消除 confound。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"MSE 50% baseline 实质 single-seed (s123 catastrophic PPL=15789)，主文报告不透明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 20\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"首次提出\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。Table 4 仅 s42。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W5 Minor + R2 agrees)。Table 4 MSE 50% = 229.26 (s42 only)。Appendix G mentions s123 failure but main text 不标注。R2 补充: MSE instability 反而加强 KL>MSE 论点。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W5\"\n    summary: \"WikiText-103 训练 → WikiText-2 评估为同分布；C4 OOD seed 覆盖不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[分歧 severity] R1-W3 Major: 本质同分布，C4 OOD 只 2-seed (global) 且 downstream 只 seed 42。R2 REBUT: C4 OOD + downstream robustness (Table 11, Δ≤1.1pp) 提供初步验证，severity 应为 minor。Director 判定: warning (between major/minor)——同分布主表是合理批评但 C4 data 部分缓解。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表 downstream 对比未控制\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 20\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"首次提出\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W6 Minor + R2 agrees)。PPL 有 matched comparison (Appendix D) 但 downstream 没有。0.8pp 差异对 MMLU -5.2pp 影响可能有限但未排除。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W7\"\n    summary: \"30% sparsity sweet spot 实用价值有限 (MMLU -24.6pp, GSM8K -41pp vs dense)\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。30% + 无 speedup = 部署价值有限。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[分歧对比公平性] R2-W3 Major: 对比 Polar Sparsity 50% <1% drop。R1 REBUT: 不同 sparsity 类型 (attention head vs FFN neuron)，TEAL 也退化 19.4pp。Director 判定: 实用价值问题成立 (info)，但 Polar Sparsity 直接对比不公平。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W8\"\n    summary: \"术语过度创造: 'coupling alignment ranking', 'signal type × coupling scope' 包装简单概念\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"术语 overclaim\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R2-W4 Minor + R1 agrees)。不影响技术正确性但增加阅读负担。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W9\"\n    summary: \"Batched inference 对 contextual sparsity 的影响完全未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R2-W5 Minor + R1 agrees)。Polar Sparsity 已证明 batched inference 下 mask union → near-dense。所有实验 batch=1。Limitations 应讨论。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W10\"\n    summary: \"Abstract 'universally use BCE' 不准确 (ShadowLLM 用 MSE)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识。建议改为 'primarily rely on decomposed losses (BCE or per-layer MSE)'。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 19 — Previously resolved issues (carried forward)\n  # ============================================================\n\n  - id: \"R18-W4\"\n    summary: \"Gradient coupling 因果解释不完整: 缺少 per-layer KL 关键对照实验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识。缺 per-layer KL 实验。\"}\n      - {round: 19, reviewers: [], note: \"Per-layer KL 3-seed 完成。但衍生新问题 (R20-W1 train-inference mismatch, R20-W2 术语 conflation)。\"}\n    action_items:\n      - {round: 18, action: \"补充 per-layer KL ablation\", assigned_to: \"research_director\", status: done}\n    resolution: \"Per-layer KL 实验已完成并写入 §4.5。但暴露了新 confound (R20-W1) 和 framing 问题 (R20-W2)。\"\n    resolution_round: 19\n"
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
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 20 (fresh) — Issues from roundtable review\n  # ============================================================\n\n  - id: \"R20-N1\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无法转化为 speedup\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 20\n    mentions:\n      - {round: 16, reviewers: [1, 2], note: \"首次提出\"}\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。Introduction 仍暗示 efficiency gain。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-N1 + R2-N2, both Critical)。Table 5 实测 +6.4%。Introduction para 1 仍以 'potential inference acceleration' 为动机。R2 补充: 同期 Polar Sparsity 2.2× speedup, SVD-CSP 1.8× speedup。R1 反驳 Polar Sparsity 对比 (不同 sparsity 类型) 但同意核心批评。\"}\n    action_items:\n      - {round: 19, action: \"Intro 去掉 efficiency motivation\", assigned_to: \"paper_agent\", status: in_progress}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 在所有 scale (8B/7B/14B) 上系统性退步，仅有未验证假说\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 20\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"首次提出 knowledge-intensive regression\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。假设性解释未验证。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-N2 + R2-N3, both Critical)。8B: MMLU -5.2pp, GSM8K -1.3pp; 14B: MMLU -8.1pp (global), GSM8K -20pp (σ=5.2pp); Mistral: GSM8K -7.3pp。§4.2 标注 'hypothesis; mechanistic investigation left to future work'。R2 指出: 如果 coupling alignment dominant，为何 knowledge tasks 更差？Claim-evidence mismatch。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N3\"\n    summary: \"与 MaskLLM 核心配方高度重叠 (frozen weights + KL + Gumbel)，新颖性依赖 analysis framework\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 16\n    last_seen_round: 20\n    mentions:\n      - {round: 16, reviewers: [2], note: \"首次提出 novelty 不足\"}\n      - {round: 19, reviewers: [1, 2], note: \"[分歧] R2 Critical; R1 REBUT (weight vs activation 是本质不同问题域)\"}\n      - {round: 20, reviewers: [1, 2], note: \"[分歧] R2-N1 Critical: 三点区分均 application-level。R1 REBUT: predictor network (函数逼近 vs 参数优化) 和 global top-k allocation (跨层依赖) 是非平凡差异，但同意方法新颖性有限、'analysis contribution 定位需更精确'。Director 判定: recipe-level overlap 真实存在，predictor+global allocation 有技术差异但不构成 strong novelty。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL 训练-推理不匹配 (1 layer/step vs 32 layers) 混淆了 2D 分解的因果推断\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W1 Major, R2 agrees 且称 'R1 最有洞察力的观察')。§4.5 末尾仅一句 caveat，但 'coupling scope 24-35%' 在 Abstract/Conclusion/Contributions 反复引用。50% per-layer KL 退化到 34.85 (vs E2E 11.92) 更可能是 mismatch catastrophe 而非 coupling 必要性。需 gradual K (1→4→16→32) 实验验证。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"'Coupling alignment' 术语 conflates signal type (what to optimize) 和 coupling mechanism (how gradients flow)\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"97.5% 归因仅适用 PPL (R19-N1); 术语 overclaim (R19-W5)\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W2 + R2-W2, both Major → Director escalates to Critical due to pervasive impact on narrative)。98% gap 由 signal type 解释，但正文用 'coupling alignment' 作核心术语——暗示 cross-layer coupling 是关键，与 per-layer KL 数据矛盾。脚注承认 signal type 维度 entails gradient flow topology 差异但未独立控制。98% 应标注为 upper bound 而非 point estimate。建议术语: 'output-distribution alignment' 而非 'coupling alignment'。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"C1 target-swap ablation 存在 trajectory confound + soft-vs-hard confound，因果推断力受限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。循环论证 + confound 叠加。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W4 Major + R2-W1 Major)。s42 oracle from earlier run (0.65pp gap vs retrained ≤0.02pp)。50% 仅 s42。§4.3 用 'confirms' 三次但应降为 'suggestive evidence'。Retrained s123/s456 一致性部分缓解但不消除 confound。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W4\"\n    summary: \"MSE 50% baseline 实质 single-seed (s123 catastrophic PPL=15789)，主文报告不透明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 18\n    last_seen_round: 20\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"首次提出\"}\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。Table 4 仅 s42。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W5 Minor + R2 agrees)。Table 4 MSE 50% = 229.26 (s42 only)。Appendix G mentions s123 failure but main text 不标注。R2 补充: MSE instability 反而加强 KL>MSE 论点。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W5\"\n    summary: \"WikiText-103 训练 → WikiText-2 评估为同分布；C4 OOD seed 覆盖不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[分歧 severity] R1-W3 Major: 本质同分布，C4 OOD 只 2-seed (global) 且 downstream 只 seed 42。R2 REBUT: C4 OOD + downstream robustness (Table 11, Δ≤1.1pp) 提供初步验证，severity 应为 minor。Director 判定: warning (between major/minor)——同分布主表是合理批评但 C4 data 部分缓解。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W6\"\n    summary: \"Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在主表 downstream 对比未控制\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 20\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"首次提出\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R1-W6 Minor + R2 agrees)。PPL 有 matched comparison (Appendix D) 但 downstream 没有。0.8pp 差异对 MMLU -5.2pp 影响可能有限但未排除。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W7\"\n    summary: \"30% sparsity sweet spot 实用价值有限 (MMLU -24.6pp, GSM8K -41pp vs dense)\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"[AGREE] 共识。30% + 无 speedup = 部署价值有限。\"}\n      - {round: 20, reviewers: [1, 2], note: \"[分歧对比公平性] R2-W3 Major: 对比 Polar Sparsity 50% <1% drop。R1 REBUT: 不同 sparsity 类型 (attention head vs FFN neuron)，TEAL 也退化 19.4pp。Director 判定: 实用价值问题成立 (info)，但 Polar Sparsity 直接对比不公平。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W8\"\n    summary: \"术语过度创造: 'coupling alignment ranking', 'signal type × coupling scope' 包装简单概念\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - {round: 19, reviewers: [1, 2], note: \"术语 overclaim\"}\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R2-W4 Minor + R1 agrees)。不影响技术正确性但增加阅读负担。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W9\"\n    summary: \"Batched inference 对 contextual sparsity 的影响完全未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识 (R2-W5 Minor + R1 agrees)。Polar Sparsity 已证明 batched inference 下 mask union → near-dense。所有实验 batch=1。Limitations 应讨论。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W10\"\n    summary: \"Abstract 'universally use BCE' 不准确 (ShadowLLM 用 MSE)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - {round: 20, reviewers: [1, 2], note: \"[AGREE] 共识。建议改为 'primarily rely on decomposed losses (BCE or per-layer MSE)'。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 19 — Previously resolved issues (carried forward)\n  # ============================================================\n\n  - id: \"R18-W4\"\n    summary: \"Gradient coupling 因果解释不完整: 缺少 per-layer KL 关键对照实验\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - {round: 18, reviewers: [1, 2], note: \"[AGREE] 共识。缺 per-layer KL 实验。\"}\n      - {round: 19, reviewers: [], note: \"Per-layer KL 3-seed 完成。但衍生新问题 (R20-W1 train-inference mismatch, R20-W2 术语 conflation)。\"}\n    action_items:\n      - {round: 18, action: \"补充 per-layer KL ablation\", assigned_to: \"research_director\", status: done}\n    resolution: \"Per-layer KL 实验已完成并写入 §4.5。但暴露了新 confound (R20-W1) 和 framing 问题 (R20-W2)。\"\n    resolution_round: 19\n"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-22T09:47:18.981422+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 9217}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-22T09:49:45.871195+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "report": "# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**目标 Venue**: EMNLP 2026 (Long Paper, ARR May cycle)\n**截止日期**: 2026-05-25\n**审稿轮次**: Round 20 (fresh)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）\n**评分共识**: 两位 Reviewer 均给出 Overall 3.0 (Findings)\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor（<1% base params），使用 Gumbel-Sigmoid relaxation + frozen weights 框架。在 LLaMA-3.1-8B 30% sparsity 下 PPL 降低 14.5%（matched sparsity），通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type（98% PPL gap）和 coupling scope（24–35% downstream）两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证 PPL generalization。论文自我定位为 \"primarily an empirical study\"。\n\n---\n\n## Strengths\n\n**S1. 系统性的 5-way loss comparison。** 涵盖 Forward KL / Reverse KL / JSD / BCE / MSE 五种 loss 配置，配合 Gumbel/STE relaxation 交叉消融（Table 4），构成该方向目前最全面的实证对比。[R1, R2 共识]\n\n**S2. C1 target-swap ablation 设计有新意。** 将 KL-derived masks 喂给 BCE 训练以解耦 \"mask quality\" 与 \"gradient coupling\"，比简单的 loss comparison 更有深度。尽管存在 confound（见 W3），设计思路值得肯定。[R1, R2 共识]\n\n**S3. 诚实的自我定位和 limitation 报告。** 明确声明 \"we do not propose a new architecture or algorithm\"（§1），坦率承认知识密集型退步、无加速、OOD variance、MSE seed failure。这种透明度在投稿中少见。[R1, R2 共识]\n\n**S4. Compensation redundancy 有实际价值。** 证明 KL predictor 无需 FastForward 式 +67.2M compensation network，简化 inference pipeline。[R2]\n\n**S5. Related Work 覆盖全面。** 覆盖 training-free methods、predictor-based methods、activation engineering、MoE routing、weight pruning 等主要方向，MaskLLM 三点详细对比。引用量和质量均上乘（8/10）。[R2]\n\n**S6. 详尽附录，可重现性高。** 18 页中 ~10 页附录，涵盖 bottleneck sensitivity、temperature schedule、training convergence、penalty dynamics、OOD evaluation、mask visualization 等。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [Critical, 共识]** **无实际 wall-clock 加速，反增 6.4% 延迟**\n- 位置：Appendix A (Table 5), §1 para 5, §5\n- 论文动机围绕 \"potential inference acceleration\"（§1 para 1），但 Table 5 显示 +6.4% latency（126.78 vs 119.11 ms/fwd）。论文承认 \"unstructured element-wise masks do not translate to wall-clock speedup\"（Appendix A）。当前结果是净减速。\n- 影响：一篇 sparsity prediction 论文如果无法展示任何加速效果，其实际贡献局限于 analytical insights。同期工作已实现实际加速（如 Polar Sparsity 2.2× speedup，尽管 R1 指出 sparsity 类型不同不可直接对比）。\n- [R1-N1 Critical + R2-N2 Critical, 完全共识]\n\n**N2 [Critical, 共识]** **MMLU/GSM8K 在所有 scale 上系统性退步，未解释**\n- 位置：Table 2, Table 13 (Appendix K), Table 17 (Appendix L), §4.2, Limitations\n- KL 在 commonsense（ARC-c, WG, HS, PIQA：4/4 wins at 30%）上一致优于 TEAL，但在 knowledge-intensive（MMLU, GSM8K）上一致劣于 TEAL——跨三个架构：8B MMLU -5.2pp; 14B MMLU -8.1pp (global), GSM8K -20pp (σ=5.2pp); Mistral GSM8K -7.3pp。论文仅给出假设性解释（§4.2: \"mode-covering may dilute task-specific knowledge pathways\"），自标 \"hypothesis; mechanistic investigation left to future work\"。\n- 影响：这不是 edge case，而是一整类核心任务的系统性退步。如果 KL 在 MMLU/GSM8K 上一致劣于零训练成本的 TEAL，用户为什么要付出训练代价？R2 进一步指出：如果 \"coupling alignment is the dominant design dimension\"，为什么 knowledge tasks 反而更差？存在 claim-evidence mismatch。\n- [R1-N2 Critical + R2-N3 Critical, 完全共识]\n\n**N3 [Critical, Director 升级]** **\"Coupling alignment\" 核心术语 conflates signal type 和 coupling mechanism；98% 归因方法论不严谨**\n- 位置：Abstract line 5, §1 Contributions, §4.5, §5 Conclusion\n- Per-layer KL（无 cross-layer coupling 但有 output-distribution signal）达到 E2E KL 98% 的 PPL 效果（9.05 vs 8.81, Table 4）→ cross-layer coupling 仅贡献 2.5% PPL gap。但论文用 \"coupling alignment\" 作核心术语（Conclusion: \"Coupling alignment—optimizing through the output distribution—is the dominant design dimension\"），暗示 cross-layer coupling 是关键——这与 per-layer KL 数据矛盾。实际驱动力是 signal type（output distribution vs intermediate activations），而非 inter-layer gradient coupling。\n- 98% 分解假设 signal type 和 coupling scope 正交（无交互效应），但从 MSE→KL 同时改变了 (a) loss target, (b) gradient flow topology, (c) optimization landscape（论文脚注 §4.5 自己承认）。98% 应标注为 upper bound estimate 而非 point estimate，但正文在 Abstract/Contributions/Conclusion 中反复引用。\n- [R1-W2 Major + R2-W2 Major, 完全共识; Director 因对核心 narrative 的全局影响升级为 Critical]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [Major, 共识]** **Per-layer KL 训练-推理不匹配混淆了 2D 分解的因果推断**\n- 位置：§4.5, Table 4\n- Per-layer KL 训练时每步仅 mask 1/32 层，推理时 32 层同时 mask。30% downstream 差距（\"coupling scope 24–35%\"）可能大部分来自 train-inference mismatch 而非缺乏 cross-layer coupling。50% 时 per-layer KL 退化到 34.85（vs E2E 11.92, 3× gap），更可能是 mismatch catastrophe 而非 \"coupling transitions from optional to essential\"（§4.5）。\n- 论文在 §4.5 末尾仅一句 caveat，但 \"coupling scope 24–35%\" 在 Abstract/Conclusion 反复出现。需 gradual K (1→4→16→32 layers/step) 实验才能区分 coupling effect 和 mismatch effect。\n- [R1-W1 Major, R2 agrees 且称\"R1 最有洞察力的观察\"]\n\n**W2 [Major, 分歧]** **与 MaskLLM (NeurIPS 2024) 核心配方高度重叠**\n- 位置：§2 (Related Work), §1 Contributions\n- 核心配方（frozen weights + learnable masks + forward KL + Gumbel relaxation）与 MaskLLM 一致。三点区分（sparsity type / mask generation / allocation）中，R2 认为均为 application-level 差异；R1 认为 predictor network（函数逼近 vs 参数优化）和 global top-k allocation（跨层依赖）是非平凡技术差异，但同意方法新颖性有限。\n- 在 \"primarily empirical study\" 定位下，贡献主要依赖 analysis framework（C1 ablation + 2D decomposition），但这些 insights 受上述 confounds 影响，surprise factor 有限。\n- [R2-N1 Critical; R1 部分 REBUT; Director 判定: Warning — recipe overlap 真实存在，但 predictor+global allocation 有技术差异]\n\n**W3 [Major→Warning, 共识]** **C1 target-swap ablation 存在 trajectory confound**\n- 位置：Table 3, footnote †, Appendix P\n- (a) s42 oracle 来自 \"earlier training run\"（PPL gap 0.65pp vs retrained ≤0.02pp）；(b) oracle masks 编码特定 KL 训练轨迹；(c) 50% 仅 s42 单 seed。§4.3 用 \"confirms\" 三次但应降为 \"suggestive evidence\"。Retrained s123/s456 一致性（≤0.02pp）部分缓解但不消除 confound。\n- [R1-W4 Major + R2-W1 Major, 共识]\n\n**W4 [Warning]** **WikiText 同分布评估 + C4 OOD seed 覆盖不足**\n- WikiText-103 训练 → WikiText-2 评估本质同分布。C4 OOD 提供初步验证（Table 10-11, downstream Δ≤1.1pp），但 30% OOD 仅 2-seed (global)，downstream robustness 仅 seed 42。\n- [R1-W3 Major; R2 REBUT severity→minor; Director 判定: Warning]\n\n**W5 [Warning]** **MSE 50% 实质 single-seed (s123 catastrophic failure)**\n- Table 4 MSE 50% = 229.26 仅 s42。Appendix G 提及 s123 failure (PPL=15789, 5.1% sparsity) 但主文未标注。MSE instability 本身加强 KL>MSE 论点，但 baseline 的有效性受限。\n- [R1-W5 Minor + R2 agrees]\n\n### Minor\n\n**W6 [Info]** Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在 downstream 对比未控制 [R1-W6, R2 agrees]\n**W7 [Info]** 30% sparsity sweet spot 实用价值有限（MMLU -24.6pp, GSM8K -41pp vs dense）[R2-W3, R1 部分 REBUT Polar Sparsity 对比]\n**W8 [Info]** 术语过度创造（\"coupling alignment ranking\" = loss function comparison）[R2-W4, R1 agrees]\n**W9 [Info]** Batched inference 对 contextual sparsity 的影响完全未讨论 [R2-W5, R1 agrees]\n**W10 [Info]** Abstract \"universally use BCE\" 不准确（ShadowLLM 用 MSE）[R2, R1 agrees]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：\n1. **无实际加速** (R1-N1 = R2-N2, both Critical)\n2. **知识密集型任务系统性退步未解释** (R1-N2 = R2-N3, both Critical)\n3. **\"Coupling alignment\" 术语混淆 + 98% 归因不严谨** (R1-W2 = R2-W2, both Major)\n4. **Per-layer KL train-inference mismatch** (R1-W1, R2 fully agrees)\n5. **C1 ablation trajectory confound** (R1-W4 ≈ R2-W1, both Major)\n6. **MSE 50% single-seed** (R1-W5, R2 agrees)\n7. **术语过度创造** (R2-W4, R1 agrees)\n8. **Batched inference 未讨论** (R2-W5, R1 agrees)\n\n---\n\n## Reviewer Divergence\n\n**D1. MaskLLM 新颖性程度**\n- R2: \"完全一致\"，三点区分均 application-level (Critical)\n- R1: predictor network 和 global allocation 是非平凡差异，但同意方法新颖性有限 (REBUT)\n- Director 判定：recipe-level overlap 真实存在。R1 的技术差异论证有道理（predictor 需泛化到 unseen inputs，global allocation 创造跨层依赖），但不足以构成 strong methodological novelty。在 empirical study 定位下，analysis framework 的贡献需要足够 surprising 的 insights 支撑——而当前 insights 受 confounds 影响。\n\n**D2. 30% sparsity ceiling 对比 Polar Sparsity**\n- R2: 对比 Polar Sparsity 50% <1% drop (Major)\n- R1: 不同 sparsity 类型（attention head vs FFN neuron）不可直接对比 (REBUT)\n- Director 判定：R1 的 REBUT 有技术依据。但 practical utility 问题成立：30% FFN sparsity + 无加速 = 部署价值有限。\n\n**D3. WikiText 同分布严重性**\n- R1: Major（本质同分布）\n- R2: Minor（C4 OOD + downstream robustness 部分缓解）\n- Director 判定：Warning。同分布主表是合理批评，但 C4 data (Table 10-11) 提供了初步 OOD 验证。\n\n---\n\n## Questions（需要作者在 rebuttal 中回答）\n\n**Q1.** [关键] Per-layer KL 的 downstream 原始数值（ARC-c, WG, MMLU, GSM8K, HS, PIQA）是多少？目前仅有 coupling scope 百分比但无法 verify。\n\n**Q2.** [关键] Per-layer KL 训练时如果 mask K>1 层/步（如 K=2, 4, 8, 16, 32），性能如何变化？这能直接区分 coupling effect 和 train-inference mismatch effect。\n\n**Q3.** [关键] 如果将论文核心术语从 \"coupling alignment\" 改为 \"output-distribution alignment\"，核心 claims 是否仍然成立？这一修改是否能更准确地反映 per-layer KL 数据？\n\n**Q4.** MMLU/GSM8K 退化是否与特定层的 mask divergence 相关？Per-layer Jaccard divergence（Figure 7, Appendix M）能否与 per-task performance 关联？\n\n**Q5.** MaskLLM 在 activation sparsity 场景下的表现如何？如果将 MaskLLM 的 direct-parameter mask 方案适配到 activation sparsity，KL 优势是否仍成立？\n\n**Q6.** C1 ablation 50% sparsity 是否能补充 s123/s456 结果？s42 oracle 来自 earlier run 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？\n\n**Q7.** 是否尝试过 KL 蒸馏温度 $T>1$？标准知识蒸馏中 $T=2$–$4$ 通常优于 $T=1$。\n\n**Q8.** 更多样化的训练数据（C4 或 RedPajama 子集替代 WikiText-103）是否能缓解 MMLU regression？\n\n---\n\n## Missing References\n\nRelated Work 覆盖全面（R2 评估 8/10）。可考虑补充（均非 critical）：\n- LazyLLM (Fu et al., 2024) — token-level dynamic pruning for attention + FFN\n- COTS (Zhang et al., 2025, arXiv:2511.09822) — multi-channel sparse FFN exploitation\n- LLM in a Flash (Alizadeh et al., 2024) — flash memory 上的 sparse inference 部署\n- Outlier Suppression+ (Wei et al., 2023) — activation outlier 对 sparsity 的影响\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因额度限制报错退出（`agent_error: You've hit your limit · resets 6pm UTC`）。未产生有效的排版审查结果。用户可在额度恢复后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分理由**：\n\n论文是一项扎实的实证研究，5-way loss comparison 和 C1 target-swap ablation 是主要亮点，Related Work 全面，limitation 报告诚实。这些品质使论文达到 Findings 水平。\n\n但三个 Critical 问题阻止 Main conference 接收：\n\n1. **无实际加速**（+6.4% overhead）：一篇 sparsity prediction 论文无法展示任何推理加速，实际贡献局限于 analytical insights。论文需要在 Triton block-sparse POC 或完全 reframe 为纯分析论文之间做出选择。\n\n2. **知识密集型任务系统性退步未解释**：MMLU/GSM8K 跨三个架构一致劣于零训练成本的 TEAL，且仅有未验证假说。这直接动摇了 method 的实用价值和 \"coupling alignment is dominant\" 的核心 claim。\n\n3. **核心 framing 存在问题**：\"coupling alignment\" 术语暗示 cross-layer coupling 是关键，但 per-layer KL 数据显示 signal type（output distribution vs intermediate）才是 PPL 的主要驱动力（98% gap）。加之 per-layer KL 的 train-inference mismatch confound，coupling scope 的 downstream 贡献（24–35%）的可靠性也受到质疑。98% 归因是 confounded estimate 而非 clean causal decomposition。\n\n**提升至 3.5 (Borderline Conference) 的条件**：\n- 在 rebuttal 中提供 Q2（gradual K 实验）的结果，量化 train-inference mismatch vs coupling effect\n- 将核心术语从 \"coupling alignment\" 修正为 \"output-distribution alignment\"\n- 提供 MMLU regression 的初步机制解释（如 per-layer divergence 与 task performance 关联分析）\n- §1 完全去除 efficiency/acceleration 动机\n\n**提升至 4.0 (Conference) 的额外条件**：\n- 展示至少一个 sparsity level 的 wall-clock speedup POC\n- MaskLLM 在 activation sparsity 上的 baseline 对比\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Para 1 \"potential inference acceleration\" 仍以 efficiency 为动机，与 Table 5 (+6.4% overhead) 矛盾。应 reframe 为 understanding training objective design space for sparsity prediction。\n- \"coupling alignment ranking\" (Contributions item 1) 术语需修正为更准确的表述。\n\n### §3 Method\n- §3.4 forward vs reverse KL 论证（mode-covering for sparsity prediction）直觉合理，但 §4.5 reverse KL 30% 3-seed 结果显示 reverse KL 在 commonsense 上也优于 TEAL，部分削弱 \"missing critical neurons\" 论证。\n- §3.6 梯度分析自标 \"suggestive\"（合理），但正文引用时偶尔暗示更强因果关系，需统一用语。\n\n### §4 Experiments\n- Table 2: actual sparsity 差异（KL 28.5% vs TEAL 29.3%）应在表格内更显著标注，而非仅 footnote。\n- §4.2 Task-Type Split: \"hypothesis; mechanistic investigation left to future work\" 的坦率值得肯定，但这个 future work 对于支撑核心 claim 至关重要。\n- §4.4 C1 ablation: \"confirms\" 应改为 \"suggests\" 或 \"provides evidence consistent with\"（出现 3 次）。\n- §4.5 Per-layer KL: \n  - \"coupling scope contributes 24–35%\" 的 claim 需标注 train-inference mismatch caveat（当前仅在段末一句）。\n  - \"signal type accounts for 98%\" 需标注为 upper bound estimate。\n  - Per-layer KL downstream 原始数值应以表格形式呈现，而非仅在文字中给出百分比。\n\n### §5 Conclusion\n- \"Coupling alignment—optimizing through the output distribution—is the dominant design dimension\" 建议修正为 \"Output-distribution alignment—optimizing through the model's final prediction—is the dominant design dimension for PPL; cross-layer coupling provides additional downstream benefits whose magnitude requires further investigation.\"\n\n### Limitations\n- 应补充 batched inference 讨论。\n- 应更显著讨论 knowledge-intensive regression 的 scale-dependent 趋势（8B: -5.2pp MMLU → 14B: -8.1pp MMLU）。\n\n### Appendix\n- MSE s123 50% catastrophic failure (PPL=15,789) 应在主文 §4.5 更显著提及。\n- Per-layer KL downstream 原始数值应出现在某个附录表格中。"
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
    "overall_score": "3.0 (Findings)",
    "report": "# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**目标 Venue**: EMNLP 2026 (Long Paper, ARR May cycle)\n**截止日期**: 2026-05-25\n**审稿轮次**: Round 20 (fresh)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）\n**评分共识**: 两位 Reviewer 均给出 Overall 3.0 (Findings)\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor（<1% base params），使用 Gumbel-Sigmoid relaxation + frozen weights 框架。在 LLaMA-3.1-8B 30% sparsity 下 PPL 降低 14.5%（matched sparsity），通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type（98% PPL gap）和 coupling scope（24–35% downstream）两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证 PPL generalization。论文自我定位为 \"primarily an empirical study\"。\n\n---\n\n## Strengths\n\n**S1. 系统性的 5-way loss comparison。** 涵盖 Forward KL / Reverse KL / JSD / BCE / MSE 五种 loss 配置，配合 Gumbel/STE relaxation 交叉消融（Table 4），构成该方向目前最全面的实证对比。[R1, R2 共识]\n\n**S2. C1 target-swap ablation 设计有新意。** 将 KL-derived masks 喂给 BCE 训练以解耦 \"mask quality\" 与 \"gradient coupling\"，比简单的 loss comparison 更有深度。尽管存在 confound（见 W3），设计思路值得肯定。[R1, R2 共识]\n\n**S3. 诚实的自我定位和 limitation 报告。** 明确声明 \"we do not propose a new architecture or algorithm\"（§1），坦率承认知识密集型退步、无加速、OOD variance、MSE seed failure。这种透明度在投稿中少见。[R1, R2 共识]\n\n**S4. Compensation redundancy 有实际价值。** 证明 KL predictor 无需 FastForward 式 +67.2M compensation network，简化 inference pipeline。[R2]\n\n**S5. Related Work 覆盖全面。** 覆盖 training-free methods、predictor-based methods、activation engineering、MoE routing、weight pruning 等主要方向，MaskLLM 三点详细对比。引用量和质量均上乘（8/10）。[R2]\n\n**S6. 详尽附录，可重现性高。** 18 页中 ~10 页附录，涵盖 bottleneck sensitivity、temperature schedule、training convergence、penalty dynamics、OOD evaluation、mask visualization 等。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [Critical, 共识]** **无实际 wall-clock 加速，反增 6.4% 延迟**\n- 位置：Appendix A (Table 5), §1 para 5, §5\n- 论文动机围绕 \"potential inference acceleration\"（§1 para 1），但 Table 5 显示 +6.4% latency（126.78 vs 119.11 ms/fwd）。论文承认 \"unstructured element-wise masks do not translate to wall-clock speedup\"（Appendix A）。当前结果是净减速。\n- 影响：一篇 sparsity prediction 论文如果无法展示任何加速效果，其实际贡献局限于 analytical insights。同期工作已实现实际加速（如 Polar Sparsity 2.2× speedup，尽管 R1 指出 sparsity 类型不同不可直接对比）。\n- [R1-N1 Critical + R2-N2 Critical, 完全共识]\n\n**N2 [Critical, 共识]** **MMLU/GSM8K 在所有 scale 上系统性退步，未解释**\n- 位置：Table 2, Table 13 (Appendix K), Table 17 (Appendix L), §4.2, Limitations\n- KL 在 commonsense（ARC-c, WG, HS, PIQA：4/4 wins at 30%）上一致优于 TEAL，但在 knowledge-intensive（MMLU, GSM8K）上一致劣于 TEAL——跨三个架构：8B MMLU -5.2pp; 14B MMLU -8.1pp (global), GSM8K -20pp (σ=5.2pp); Mistral GSM8K -7.3pp。论文仅给出假设性解释（§4.2: \"mode-covering may dilute task-specific knowledge pathways\"），自标 \"hypothesis; mechanistic investigation left to future work\"。\n- 影响：这不是 edge case，而是一整类核心任务的系统性退步。如果 KL 在 MMLU/GSM8K 上一致劣于零训练成本的 TEAL，用户为什么要付出训练代价？R2 进一步指出：如果 \"coupling alignment is the dominant design dimension\"，为什么 knowledge tasks 反而更差？存在 claim-evidence mismatch。\n- [R1-N2 Critical + R2-N3 Critical, 完全共识]\n\n**N3 [Critical, Director 升级]** **\"Coupling alignment\" 核心术语 conflates signal type 和 coupling mechanism；98% 归因方法论不严谨**\n- 位置：Abstract line 5, §1 Contributions, §4.5, §5 Conclusion\n- Per-layer KL（无 cross-layer coupling 但有 output-distribution signal）达到 E2E KL 98% 的 PPL 效果（9.05 vs 8.81, Table 4）→ cross-layer coupling 仅贡献 2.5% PPL gap。但论文用 \"coupling alignment\" 作核心术语（Conclusion: \"Coupling alignment—optimizing through the output distribution—is the dominant design dimension\"），暗示 cross-layer coupling 是关键——这与 per-layer KL 数据矛盾。实际驱动力是 signal type（output distribution vs intermediate activations），而非 inter-layer gradient coupling。\n- 98% 分解假设 signal type 和 coupling scope 正交（无交互效应），但从 MSE→KL 同时改变了 (a) loss target, (b) gradient flow topology, (c) optimization landscape（论文脚注 §4.5 自己承认）。98% 应标注为 upper bound estimate 而非 point estimate，但正文在 Abstract/Contributions/Conclusion 中反复引用。\n- [R1-W2 Major + R2-W2 Major, 完全共识; Director 因对核心 narrative 的全局影响升级为 Critical]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [Major, 共识]** **Per-layer KL 训练-推理不匹配混淆了 2D 分解的因果推断**\n- 位置：§4.5, Table 4\n- Per-layer KL 训练时每步仅 mask 1/32 层，推理时 32 层同时 mask。30% downstream 差距（\"coupling scope 24–35%\"）可能大部分来自 train-inference mismatch 而非缺乏 cross-layer coupling。50% 时 per-layer KL 退化到 34.85（vs E2E 11.92, 3× gap），更可能是 mismatch catastrophe 而非 \"coupling transitions from optional to essential\"（§4.5）。\n- 论文在 §4.5 末尾仅一句 caveat，但 \"coupling scope 24–35%\" 在 Abstract/Conclusion 反复出现。需 gradual K (1→4→16→32 layers/step) 实验才能区分 coupling effect 和 mismatch effect。\n- [R1-W1 Major, R2 agrees 且称\"R1 最有洞察力的观察\"]\n\n**W2 [Major, 分歧]** **与 MaskLLM (NeurIPS 2024) 核心配方高度重叠**\n- 位置：§2 (Related Work), §1 Contributions\n- 核心配方（frozen weights + learnable masks + forward KL + Gumbel relaxation）与 MaskLLM 一致。三点区分（sparsity type / mask generation / allocation）中，R2 认为均为 application-level 差异；R1 认为 predictor network（函数逼近 vs 参数优化）和 global top-k allocation（跨层依赖）是非平凡技术差异，但同意方法新颖性有限。\n- 在 \"primarily empirical study\" 定位下，贡献主要依赖 analysis framework（C1 ablation + 2D decomposition），但这些 insights 受上述 confounds 影响，surprise factor 有限。\n- [R2-N1 Critical; R1 部分 REBUT; Director 判定: Warning — recipe overlap 真实存在，但 predictor+global allocation 有技术差异]\n\n**W3 [Major→Warning, 共识]** **C1 target-swap ablation 存在 trajectory confound**\n- 位置：Table 3, footnote †, Appendix P\n- (a) s42 oracle 来自 \"earlier training run\"（PPL gap 0.65pp vs retrained ≤0.02pp）；(b) oracle masks 编码特定 KL 训练轨迹；(c) 50% 仅 s42 单 seed。§4.3 用 \"confirms\" 三次但应降为 \"suggestive evidence\"。Retrained s123/s456 一致性（≤0.02pp）部分缓解但不消除 confound。\n- [R1-W4 Major + R2-W1 Major, 共识]\n\n**W4 [Warning]** **WikiText 同分布评估 + C4 OOD seed 覆盖不足**\n- WikiText-103 训练 → WikiText-2 评估本质同分布。C4 OOD 提供初步验证（Table 10-11, downstream Δ≤1.1pp），但 30% OOD 仅 2-seed (global)，downstream robustness 仅 seed 42。\n- [R1-W3 Major; R2 REBUT severity→minor; Director 判定: Warning]\n\n**W5 [Warning]** **MSE 50% 实质 single-seed (s123 catastrophic failure)**\n- Table 4 MSE 50% = 229.26 仅 s42。Appendix G 提及 s123 failure (PPL=15789, 5.1% sparsity) 但主文未标注。MSE instability 本身加强 KL>MSE 论点，但 baseline 的有效性受限。\n- [R1-W5 Minor + R2 agrees]\n\n### Minor\n\n**W6 [Info]** Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 在 downstream 对比未控制 [R1-W6, R2 agrees]\n**W7 [Info]** 30% sparsity sweet spot 实用价值有限（MMLU -24.6pp, GSM8K -41pp vs dense）[R2-W3, R1 部分 REBUT Polar Sparsity 对比]\n**W8 [Info]** 术语过度创造（\"coupling alignment ranking\" = loss function comparison）[R2-W4, R1 agrees]\n**W9 [Info]** Batched inference 对 contextual sparsity 的影响完全未讨论 [R2-W5, R1 agrees]\n**W10 [Info]** Abstract \"universally use BCE\" 不准确（ShadowLLM 用 MSE）[R2, R1 agrees]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成完全共识 [AGREE]：\n1. **无实际加速** (R1-N1 = R2-N2, both Critical)\n2. **知识密集型任务系统性退步未解释** (R1-N2 = R2-N3, both Critical)\n3. **\"Coupling alignment\" 术语混淆 + 98% 归因不严谨** (R1-W2 = R2-W2, both Major)\n4. **Per-layer KL train-inference mismatch** (R1-W1, R2 fully agrees)\n5. **C1 ablation trajectory confound** (R1-W4 ≈ R2-W1, both Major)\n6. **MSE 50% single-seed** (R1-W5, R2 agrees)\n7. **术语过度创造** (R2-W4, R1 agrees)\n8. **Batched inference 未讨论** (R2-W5, R1 agrees)\n\n---\n\n## Reviewer Divergence\n\n**D1. MaskLLM 新颖性程度**\n- R2: \"完全一致\"，三点区分均 application-level (Critical)\n- R1: predictor network 和 global allocation 是非平凡差异，但同意方法新颖性有限 (REBUT)\n- Director 判定：recipe-level overlap 真实存在。R1 的技术差异论证有道理（predictor 需泛化到 unseen inputs，global allocation 创造跨层依赖），但不足以构成 strong methodological novelty。在 empirical study 定位下，analysis framework 的贡献需要足够 surprising 的 insights 支撑——而当前 insights 受 confounds 影响。\n\n**D2. 30% sparsity ceiling 对比 Polar Sparsity**\n- R2: 对比 Polar Sparsity 50% <1% drop (Major)\n- R1: 不同 sparsity 类型（attention head vs FFN neuron）不可直接对比 (REBUT)\n- Director 判定：R1 的 REBUT 有技术依据。但 practical utility 问题成立：30% FFN sparsity + 无加速 = 部署价值有限。\n\n**D3. WikiText 同分布严重性**\n- R1: Major（本质同分布）\n- R2: Minor（C4 OOD + downstream robustness 部分缓解）\n- Director 判定：Warning。同分布主表是合理批评，但 C4 data (Table 10-11) 提供了初步 OOD 验证。\n\n---\n\n## Questions（需要作者在 rebuttal 中回答）\n\n**Q1.** [关键] Per-layer KL 的 downstream 原始数值（ARC-c, WG, MMLU, GSM8K, HS, PIQA）是多少？目前仅有 coupling scope 百分比但无法 verify。\n\n**Q2.** [关键] Per-layer KL 训练时如果 mask K>1 层/步（如 K=2, 4, 8, 16, 32），性能如何变化？这能直接区分 coupling effect 和 train-inference mismatch effect。\n\n**Q3.** [关键] 如果将论文核心术语从 \"coupling alignment\" 改为 \"output-distribution alignment\"，核心 claims 是否仍然成立？这一修改是否能更准确地反映 per-layer KL 数据？\n\n**Q4.** MMLU/GSM8K 退化是否与特定层的 mask divergence 相关？Per-layer Jaccard divergence（Figure 7, Appendix M）能否与 per-task performance 关联？\n\n**Q5.** MaskLLM 在 activation sparsity 场景下的表现如何？如果将 MaskLLM 的 direct-parameter mask 方案适配到 activation sparsity，KL 优势是否仍成立？\n\n**Q6.** C1 ablation 50% sparsity 是否能补充 s123/s456 结果？s42 oracle 来自 earlier run 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？\n\n**Q7.** 是否尝试过 KL 蒸馏温度 $T>1$？标准知识蒸馏中 $T=2$–$4$ 通常优于 $T=1$。\n\n**Q8.** 更多样化的训练数据（C4 或 RedPajama 子集替代 WikiText-103）是否能缓解 MMLU regression？\n\n---\n\n## Missing References\n\nRelated Work 覆盖全面（R2 评估 8/10）。可考虑补充（均非 critical）：\n- LazyLLM (Fu et al., 2024) — token-level dynamic pruning for attention + FFN\n- COTS (Zhang et al., 2025, arXiv:2511.09822) — multi-channel sparse FFN exploitation\n- LLM in a Flash (Alizadeh et al., 2024) — flash memory 上的 sparse inference 部署\n- Outlier Suppression+ (Wei et al., 2023) — activation outlier 对 sparsity 的影响\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因额度限制报错退出（`agent_error: You've hit your limit · resets 6pm UTC`）。未产生有效的排版审查结果。用户可在额度恢复后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分理由**：\n\n论文是一项扎实的实证研究，5-way loss comparison 和 C1 target-swap ablation 是主要亮点，Related Work 全面，limitation 报告诚实。这些品质使论文达到 Findings 水平。\n\n但三个 Critical 问题阻止 Main conference 接收：\n\n1. **无实际加速**（+6.4% overhead）：一篇 sparsity prediction 论文无法展示任何推理加速，实际贡献局限于 analytical insights。论文需要在 Triton block-sparse POC 或完全 reframe 为纯分析论文之间做出选择。\n\n2. **知识密集型任务系统性退步未解释**：MMLU/GSM8K 跨三个架构一致劣于零训练成本的 TEAL，且仅有未验证假说。这直接动摇了 method 的实用价值和 \"coupling alignment is dominant\" 的核心 claim。\n\n3. **核心 framing 存在问题**：\"coupling alignment\" 术语暗示 cross-layer coupling 是关键，但 per-layer KL 数据显示 signal type（output distribution vs intermediate）才是 PPL 的主要驱动力（98% gap）。加之 per-layer KL 的 train-inference mismatch confound，coupling scope 的 downstream 贡献（24–35%）的可靠性也受到质疑。98% 归因是 confounded estimate 而非 clean causal decomposition。\n\n**提升至 3.5 (Borderline Conference) 的条件**：\n- 在 rebuttal 中提供 Q2（gradual K 实验）的结果，量化 train-inference mismatch vs coupling effect\n- 将核心术语从 \"coupling alignment\" 修正为 \"output-distribution alignment\"\n- 提供 MMLU regression 的初步机制解释（如 per-layer divergence 与 task performance 关联分析）\n- §1 完全去除 efficiency/acceleration 动机\n\n**提升至 4.0 (Conference) 的额外条件**：\n- 展示至少一个 sparsity level 的 wall-clock speedup POC\n- MaskLLM 在 activation sparsity 上的 baseline 对比\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Para 1 \"potential inference acceleration\" 仍以 efficiency 为动机，与 Table 5 (+6.4% overhead) 矛盾。应 reframe 为 understanding training objective design space for sparsity prediction。\n- \"coupling alignment ranking\" (Contributions item 1) 术语需修正为更准确的表述。\n\n### §3 Method\n- §3.4 forward vs reverse KL 论证（mode-covering for sparsity prediction）直觉合理，但 §4.5 reverse KL 30% 3-seed 结果显示 reverse KL 在 commonsense 上也优于 TEAL，部分削弱 \"missing critical neurons\" 论证。\n- §3.6 梯度分析自标 \"suggestive\"（合理），但正文引用时偶尔暗示更强因果关系，需统一用语。\n\n### §4 Experiments\n- Table 2: actual sparsity 差异（KL 28.5% vs TEAL 29.3%）应在表格内更显著标注，而非仅 footnote。\n- §4.2 Task-Type Split: \"hypothesis; mechanistic investigation left to future work\" 的坦率值得肯定，但这个 future work 对于支撑核心 claim 至关重要。\n- §4.4 C1 ablation: \"confirms\" 应改为 \"suggests\" 或 \"provides evidence consistent with\"（出现 3 次）。\n- §4.5 Per-layer KL: \n  - \"coupling scope contributes 24–35%\" 的 claim 需标注 train-inference mismatch caveat（当前仅在段末一句）。\n  - \"signal type accounts for 98%\" 需标注为 upper bound estimate。\n  - Per-layer KL downstream 原始数值应以表格形式呈现，而非仅在文字中给出百分比。\n\n### §5 Conclusion\n- \"Coupling alignment—optimizing through the output distribution—is the dominant design dimension\" 建议修正为 \"Output-distribution alignment—optimizing through the model's final prediction—is the dominant design dimension for PPL; cross-layer coupling provides additional downstream benefits whose magnitude requires further investigation.\"\n\n### Limitations\n- 应补充 batched inference 讨论。\n- 应更显著讨论 knowledge-intensive regression 的 scale-dependent 趋势（8B: -5.2pp MMLU → 14B: -8.1pp MMLU）。\n\n### Appendix\n- MSE s123 50% catastrophic failure (PPL=15,789) 应在主文 §4.5 更显著提及。\n- Per-layer KL downstream 原始数值应出现在某个附录表格中。"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-22T09:49:50.442363+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4571
}
```

</details>

---


### Assistant

_source line 1654 · 2026-05-22T09:49:59.426111+00:00_

审稿报告已投递给 Research Director。

**Round 20 审稿结果摘要**：

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全一致
- **3 个 Critical 问题**：
  1. 无实际加速（+6.4% overhead）
  2. MMLU/GSM8K 跨三架构系统性退步，仅有未验证假说
  3. "Coupling alignment" 核心术语与 per-layer KL 数据矛盾（98% 由 signal type 解释），归因方法论不严谨
- **4 个 Major/Warning**：per-layer KL train-inference mismatch 混淆 2D 分解、MaskLLM 配方重叠、C1 trajectory confound、WikiText 同分布评估
- **5 个 Minor/Info**：MSE single-seed、sparsity mismatch、术语创造、batch size 未讨论、Abstract 表述
- **关键 rebuttal 条件**：gradual K 实验（Q2）、术语修正、MMLU 机制解释、去除 efficiency 动机

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（13 条 issue，5 Critical / 4 Warning / 4 Info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1655 · 2026-05-22T09:50:00.932548+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心共识：无加速(N2)、MMLU退化(N3)、C1 confounds(W1)、术语混淆(W2)。主要分歧：MaskLLM 新颖性(N1)我认为"完全一致"过强，Polar Sparsity 对比(W3)属于不同 sparsity 类型不可直接比较，Abstract matched sparsity 数字(Q5)论文选择更保守正确。

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

_source line 1656 · 2026-05-22T09:50:13.209077+00:00_

审稿报告已投递至 Research Director。

**Round 20 审稿总结**：

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全一致
- **5 个 Critical 问题**：无加速 (+6.4% overhead)、MMLU/GSM8K 系统性退步未解释、"coupling alignment" 术语与数据矛盾 + 98% 归因不严谨、per-layer KL train-inference mismatch、MaskLLM 配方重叠（分歧项）
- **4 个 Warning 问题**：C1 trajectory confound、WikiText 同分布、MSE 50% single-seed、MaskLLM novelty
- **5 个 Info 问题**：sparsity mismatch、30% ceiling、术语创造、batch size、Abstract 措辞
- **8 个 Questions** 需 rebuttal 回答，其中 Q1-Q3 最关键（per-layer KL 原始数值、gradual K 实验、术语修正）
- **Issue Tracker 已更新**（11 个 open issues）
- 视觉审查因额度限制失败，外部审稿未请求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 143

## Round 143

54 recorded events


### User

_source line 1657 · 2026-05-22T13:00:43.227204+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May cycle)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

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

_source line 1658 · 2026-05-22T13:00:49.526182+00:00_

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

_source line 1659 · 2026-05-22T13:00:49.577303+00:00_

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

_source line 1660 · 2026-05-22T13:00:57.151815+00:00_

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

_source line 1661 · 2026-05-22T13:00:57.202407+00:00_



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

_source line 1662 · 2026-05-22T13:01:01.215487+00:00_

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

_source line 1663 · 2026-05-22T13:01:01.215858+00:00_

No matching deferred tools found

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

_source line 1664 · 2026-05-22T13:01:05.982555+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 1665 · 2026-05-22T13:01:06.033130+00:00_



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

_source line 1666 · 2026-05-22T13:01:10.099652+00:00_

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

_source line 1667 · 2026-05-22T13:01:11.053753+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (370 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\n\n## 待处理\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\n- qwen14b_kl30_s42_gsm8k_uniform（准备中）\n- perlayer_kl_50_s42_boolq（准备中）\n- perlayer_kl_50_s42_ppl（准备中）\n- revkl_30_s42_boolq_uniform（准备中）\n- diag_eval_env_34887（准备中）\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\n- diag_status_34887（准备中）\n- diag_status_41718（准备中）\n- read_boolq_results（准备中）\n- …另有 41 项\n\n## 近期结论\n- **perlayer_kl_k4_s42_downstream** (success): Per-layer KL K=4 downstream eval at 30% uniform sparsit
…[truncated 1786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-22T13:01:11.104553+00:00_

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

_source line 1669 · 2026-05-22T13:01:11.807192+00:00_

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
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-22T13:01:11.807527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR May cycle site:aclweb.org"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR May cycle site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1671 · 2026-05-22T13:01:22.475586+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR May cycle site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

The search results provide information about various EMNLP 2026-related submissions, but I didn't find a specific main EMNLP 2026 call for papers with submission guidelines. The results show information about EMNLP
…[truncated 3913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 10668
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-22T13:01:33.917209+00:00_

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

_source line 1673 · 2026-05-22T13:01:34.419567+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	An output-distribution alignment ranking emerges across five loss configurations; a per-layer KL control decomposes this into two dimensions: signal type dominates PPL (up to 97.5\% of the gap at 30\%); a $K{=}4$ mismatch pilot (single seed) reveals task-dependent downstream structure---PPL and BoolQ gaps are predominantly mismatch artifacts, while commonsense retains $\sim$60\% genuine coupling.
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	

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

_source line 1674 · 2026-05-22T13:01:34.470140+00:00_

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

_source line 1675 · 2026-05-22T13:01:34.922124+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20.
…[truncated 2847 chars]

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

_source line 1676 · 2026-05-22T13:01:34.922489+00:00_

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

_source line 1677 · 2026-05-22T13:01:35.374437+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity pred
…[truncated 4835 chars]

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

_source line 1678 · 2026-05-22T13:01:35.425158+00:00_

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

_source line 1679 · 2026-05-22T13:01:35.877249+00:00_

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
…[truncated 9558 chars]

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

_source line 1680 · 2026-05-22T13:01:35.877638+00:00_

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

_source line 1681 · 2026-05-22T13:01:36.329536+00:00_

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
…[truncated 17896 chars]

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

_source line 1682 · 2026-05-22T13:01:36.380439+00:00_

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

_source line 1683 · 2026-05-22T13:01:36.832607+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment---optimizing through the model's final prediction---is the dominant design dimension for PPL (signal type: up to 97.5\% of the gap at 30\%); a $K{=}4$ mismatch pilot (single seed) reveals task-dependent downstream structure: PPL and BoolQ gaps are predominantly mismatch, while commonsense retains $\sim$60\% genuine coupling.
5	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\% via masks 46--68\% divergent from magnitude; downstream transfer is task- and scale-dependent.
6	

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

_source line 1684 · 2026-05-22T13:01:36.833081+00:00_

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

_source line 1685 · 2026-05-22T13:01:37.284860+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

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

_source line 1686 · 2026-05-22T13:01:37.335565+00:00_

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

_source line 1687 · 2026-05-22T13:01:38.239084+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-22T13:01:38.239552+00:00_

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


### Tool call

_source line 1689 · 2026-05-22T13:01:38.390138+00:00_

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

_source line 1690 · 2026-05-22T13:01:38.440887+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@inproceedings{geva2023dissecting,
6	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
7	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
8	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
9	  pages = {12216--12235},
10	  year = {2023},
11	}
12	
13	@article{fu2024lazyllm,
14	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
15	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
16	  year = {2024},
17	  journal = {arXiv preprint arXiv:2407.14057},
18	}
19	
20	@article{zhang2025cots,
21	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
22	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
23	  year = {2025},
24	  journal = {arXiv preprint arXiv:2502.14475},
25	}
26	
27	@inproceedings{alizadeh2024llmflash,
28	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
29	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
30	  year = {2024},
31	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
32	}
33	
34	@article{wei2023outlier,
35	  title = {Outlier Suppression+: Accurate Quantization of Large Language Models by Equivalent and Effective Shifting and Scaling},
36	  author = {Xiuying Wei and Yunchen Zhang and Yuhang Li and Xiangguo Zhang and Ruihao Gong and Jinyang Guo and Xianglong 
…[truncated 23340 chars]

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

_source line 1691 · 2026-05-22T13:01:38.592403+00:00_

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
…[truncated 34205 chars]

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

_source line 1692 · 2026-05-22T13:01:49.513220+00:00_

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

_source line 1693 · 2026-05-22T13:01:51.419721+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (370 个)\n\n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **bce_isocompute_v2_s42**: DONE (success) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\n\n## 待处理\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\n- qwen14b_kl30_s42_gsm8k_uniform（准备中）\n- perlayer_kl_50_s42_boolq（准备中）\n- perlayer_kl_50_s42_ppl（准备中）\n- revkl_30_s42_boolq_uniform（准备中）\n- diag_eval_env_34887（准备中）\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\n- diag_status_34887（准备中）\n- diag_status_41718（准备中）\n- read_boolq_results（准备中）\n- …另有 41 项\n\n## 近期结论\n- **perlayer_kl_k4_s42_downstream** (success): Per-layer KL K=4 downstream eval at 30% uniform sparsit
…[truncated 1786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1906
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-22T13:01:51.420367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-22T13:01:52.324454+00:00_

-rw-r--r-- 1 ubuntu ubuntu 538864 May 22 12:59 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-22T13:01:52.876365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-22T13:01:53.829917+00:00_

-rw-r--r-- 1 ubuntu ubuntu 14583 May 22 12:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml
issues:
  # ============================================================
  # Round 20 — Active issues
  # ============================================================

  - id: "R19-N3"
    summary: "无实际 wall-clock 加速: +6.4% overhead, Intro 仍有 efficiency motivation 残留"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 16
    last_seen_round: 20
    mentions:
      - {round: 16, reviewers: [1, 2], note: "首次提出。"}
      - {round: 18, reviewers: [1, 2], note: "Introduction 仍以 efficiency 动机展开。"}
      - {round: 19, reviewers: [1, 2], note: "Table 5 +6.4% overhead, Intro 暗示 efficiency gain。"}
      - {round: 20, reviewers: [1, 2], note: "[AGREE] R20-N1 Critical。§1 L3 仍有 'potential inference acceleration'。R19 Paper Agent 漏掉此处。"}
    action_items:
      - {round: 19, action: "Paper Agent: Intro 去掉 efficiency motivation", assigned_to: "paper_agent", status: done}
      - {round: 20, action: "Paper Agent: 彻底清除 intro L3 'potential inference acceleration' + 全文搜索残留", assigned_to: "paper_agent", status: done}
    resolution: "Intro L3 efficiency 残留已清除，全文无 efficiency motivation 残留。"
    resolution_round: 21

  - id: "R20-N2"
    summary: "MMLU/GSM8K 跨三个架构系统性退步未解释 (8B -5.2pp, 14B -8.1pp/-20pp, Mistral -7.3pp)"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 18
    last_seen_round: 20
    mentions:
      - {round: 18, reviewers: [1, 2], note: "R18-W8。14B 仅 30% sparsity。"}
      - {round: 19, reviewers: [1, 2], note: "R19-W2/W3。GSM8K -20pp σ=5.2pp。"}
      - {round: 20, reviewers: [1, 2], note: "[AGREE] 升级为 Critical。跨三架构一致。如果 KL 在 MMLU/GSM8K 劣于零训练成本的 TEAL, 实用价值存疑。"}
    action_items:
      - {round: 19, action: "Paper Agent: 14B 失败模式分析, reframe as finding", assigned_to: "paper_agent", status: done}
      - {round: 20, action: "Agent: 提取 per-la
…[truncated 11227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-22T13:01:53.880606+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit format anonymity requirements 2026.emnlp.org"
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
    "query": "EMNLP 2026 author guidelines page limit format anonymity requirements 2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1699 · 2026-05-22T13:01:54.081652+00:00_

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

_source line 1700 · 2026-05-22T13:01:59.851176+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit format anonymity requirements 2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Information For Authors | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/information/authors"}]

Based on the search results from the EMNLP 2026 official website, here are the key author guidelines:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. The mandator
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5970
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-22T13:01:59.851637+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 5769
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-22T13:02:26.588116+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "constraints.yaml",
  "max_chars": "3000"
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
    "file": "constraints.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-22T13:02:26.638760+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml\", \"content\": \"_next_id: 5\\nconstraints:\\n- id: C002\\n  added: 2026-05-16 03:08 UTC\\n  summary: 所有 GPU 长时间实验必须用 nohup 启动并重定向日志，禁止裸 tmux session\\n  scope: worker\\n  reason: 'bce_isocompute_s42 和 v2 两次因 tmux session 被挤掉而死，导致 Reviewer Concern #2 完全无防御数据'\\n- id: C003\\n  added: 2026-05-16 12:32 UTC\\n  summary: 论文中所有超参/架构数字必须有代码来源验证，禁止从记忆或猜测填写。Predictor 正确参数：GELU, d_b=128, 2.37M/layer,\\n    75.9M total。\\n  scope: all\\n  reason: Reviewer 发现 experiments.tex + methodology.tex 共 7 处超参事实错误（ReLU/GELU、d_b=256/128、batch_size=32/4\\n    等），根因是 Paper Agent worker 未读源代码靠猜测填写。\\n- id: C004\\n  added: 2026-05-17 15:15 UTC\\n  summary: GPU 白名单：仅允许使用 westd-34887 cuda:0/cuda:1 和 westd-41718 cuda:0/cuda:1，禁止使用其他\\n    GPU\\n  scope: all\\n  reason: 项目分配资源边界。westd-34887 为原始分配，westd-41718 为 Manager 批准的扩容（2026-05-17）。\\n\", \"total_chars\": 763, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

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

_source line 1704 · 2026-05-22T13:03:01.347170+00:00_

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

_source line 1705 · 2026-05-22T13:03:16.569497+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15222
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-22T13:03:16.721898+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计有效性**。\n\n## Venue 信息\n- **EMNLP 2026** (ARR May cycle)，deadline 2026-05-25\n- Long paper，正文 8 页限制，unlimited references\n- ACL template (`\\usepackage[review]{acl}`)，double-blind\n- Mandatory Limitations section（不计页数）\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf`\n- 标题：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 你的审查侧重\n\n重点审查以下维度，每个维度至少给出具体评价：\n\n1. **方法合理性**：KL distillation + Gumbel-Sigmoid 框架是否 well-motivated？梯度分析（§3.6）是否严谨？自适应惩罚控制器（§3.5）是否有理论/经验支撑？\n2. **实验设计**：对照实验是否充分？控制变量是否干净？baseline 选择是否公平？是否存在未控制的 confound？\n3. **统计有效性**：多种子覆盖是否一致？哪些关键 claim 只有 single-seed 支撑？error bar 报告是否完整？\n4. **Target-swap ablation（C1）**：因果推断链是否严密？是否存在循环论证或 trajectory confound？\n5. **Per-layer KL 分解**：train-inference mismatch (K=1 训练 mask 1 层 / 推理 32 层) 是否 confounds 2D decomposition？K=4 pilot 是否足以解决？\n6. **可复现性**：超参、训练细节、评估协议是否完整可复现？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Critical/Major/Minor/Info) → Questions → Missing References → Overall Assessment (score + confidence)。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计有效性**。\n\n## Venue 信息\n- **EMNLP 2026** (ARR May cycle)，deadline 2026-05-25\n- Long paper，正文 8 页限制，unlimited references\n- ACL template (`\\usepackage[review]{acl}`)，double-blind\n- Mandatory Limitations section（不计页数）\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf`\n- 标题：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 你的审查侧重\n\n重点审查以下维度，每个维度至少给出具体评价：\n\n1. **方法合理性**：KL distillation + Gumbel-Sigmoid 框架是否 well-motivated？梯度分析（§3.6）是否严谨？自适应惩罚控制器（§3.5）是否有理论/经验支撑？\n2. **实验设计**：对照实验是否充分？控制变量是否干净？baseline 选择是否公平？是否存在未控制的 confound？\n3. **统计有效性**：多种子覆盖是否一致？哪些关键 claim 只有 single-seed 支撑？error bar 报告是否完整？\n4. **Target-swap ablation（C1）**：因果推断链是否严密？是否存在循环论证或 trajectory confound？\n5. **Per-layer KL 分解**：train-inference mismatch (K=1 训练 mask 1 层 / 推理 32 层) 是否 confounds 2D decomposition？K=4 pilot 是否足以解决？\n6. **可复现性**：超参、训练细节、评估协议是否完整可复现？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Critical/Major/Minor/Info) → Questions → Missing References → Overall Assessment (score + confidence)。"
  }
}
```

</details>

---


### Tool result

_source line 1707 · 2026-05-22T13:03:28.788705+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12066
}
```

</details>

---


### Tool call

_source line 1708 · 2026-05-22T13:03:28.949336+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **EMNLP 2026** (ARR May cycle)，deadline 2026-05-25\n- Long paper，正文 8 页限制，unlimited references\n- ACL template (`\\usepackage[review]{acl}`)，double-blind\n- Mandatory Limitations section（不计页数）\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf`\n- 标题：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 你的审查侧重\n\n重点审查以下维度，每个维度至少给出具体评价：\n\n1. **新颖性**：与 MaskLLM（KL + Gumbel-Softmax, N:M 权重稀疏）的配方高度重合——本文在 recipe 层面的独立贡献是什么？分析框架（signal type vs coupling scope decomposition）是否足够新颖？\n2. **贡献完整性**：三个 contributions 是否都有充足的实验支撑？是否有 overclaim？Abstract/Intro 的 claim 与实验证据是否对齐？\n3. **相关工作覆盖**：是否遗漏重要的 related work？与 predictor-based sparsity (DejaVu, ShadowLLM, FastForward, R-Sparse, DIP, SparseInfer 等) 的比较是否公平完整？\n4. **写作质量**：行文是否清晰精炼？术语使用是否一致？是否有 AI 写作痕迹？论文叙事（narrative flow）是否连贯？\n5. **格式合规**：正文是否 ≤8 页？匿名是否合规？参考文献格式是否符合 ACL natbib 规范？Table/Figure 编号和引用是否正确？\n6. **Limitations 和 Ethics Statement**：是否充分覆盖论文的局限性？是否存在 ethics concern？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Critical/Major/Minor/Info) → Questions → Missing References → Overall Assessment (score + confidence)。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **EMNLP 2026** (ARR May cycle)，deadline 2026-05-25\n- Long paper，正文 8 页限制，unlimited references\n- ACL template (`\\usepackage[review]{acl}`)，double-blind\n- Mandatory Limitations section（不计页数）\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文信息\n- 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf`\n- 标题：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 你的审查侧重\n\n重点审查以下维度，每个维度至少给出具体评价：\n\n1. **新颖性**：与 MaskLLM（KL + Gumbel-Softmax, N:M 权重稀疏）的配方高度重合——本文在 recipe 层面的独立贡献是什么？分析框架（signal type vs coupling scope decomposition）是否足够新颖？\n2. **贡献完整性**：三个 contributions 是否都有充足的实验支撑？是否有 overclaim？Abstract/Intro 的 claim 与实验证据是否对齐？\n3. **相关工作覆盖**：是否遗漏重要的 related work？与 predictor-based sparsity (DejaVu, ShadowLLM, FastForward, R-Sparse, DIP, SparseInfer 等) 的比较是否公平完整？\n4. **写作质量**：行文是否清晰精炼？术语使用是否一致？是否有 AI 写作痕迹？论文叙事（narrative flow）是否连贯？\n5. **格式合规**：正文是否 ≤8 页？匿名是否合规？参考文献格式是否符合 ACL natbib 规范？Table/Figure 编号和引用是否正确？\n6. **Limitations 和 Ethics Statement**：是否充分覆盖论文的局限性？是否存在 ethics concern？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Critical/Major/Minor/Info) → Questions → Missing References → Overall Assessment (score + confidence)。"
  }
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-22T13:03:30.418358+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1469
}
```

</details>

---


### Assistant

_source line 1710 · 2026-05-22T13:03:38.208561+00:00_

**已派发：**
- 视觉审查 Agent → 已启动（fire-and-forget）
- Reviewer 1（方法 + 实验）→ 已分配
- Reviewer 2（新颖性 + 完整性）→ 已分配

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 144

## Round 144

2 recorded events


### User

_source line 1711 · 2026-05-22T13:08:33.163163+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法严谨性 + 实验设计 + 统计有效性）

### 总体评分

**Overall Assessment**: **3** (Findings)
**Confidence**: 4/5
**一句话总结**: 提出 KL 蒸馏替代 BCE 训练稀疏预测器的新视角，PPL 改进显著且消融充分，但缺乏实际加速收益、下游知识任务系统性退化、以及关键因果分解实验的 confound 削弱了核心 claim 的说服力。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心框架合理但 C1 ablation 有 trajectory confound，per-layer KL 的 97.5% signal-type claim 基于 confounded K=1 设置，K=4 pilot 仅 single-seed |
| Excitement | 2.5/5 | 2D taxonomy 和 coupled-vs-decomposed 视角有学术价值，但无 wall-clock 加速（+6.4% overhead）且下游知识任务系统性退化 |
| Reproducibility | 4/5 | 超参、架构、训练细节充分；单 GPU ~45min 门槛低；缺代码/checkpoint |
| Confidence | 4/5 | 熟悉 contextual sparsity、KD、SwiGLU 相关文献 |

### 主要优势

**S1.** 新颖且 well-motivated 的问题框架——将稀疏预测从 per-neuron BCE 提升到 output-distribution KL，forward KL 的 mode-covering 性质在 false-negative 代价不对称的稀疏场景中有理论基础（§3.4）。2D taxonomy (Table 1) 为组织该领域提供了有用的思维框架。

**S2.** 全面且诚实的消融实验——Table 4 覆盖 8 种配置（divergence × relaxation × coupling），发现不利结果（MMLU/GSM8K 退化）如实报告。

**S3.** C1 target-swap ablation 设计有创意——用 KL-derived masks 作为 BCE 训练目标分离 mask quality 与 gradient coupling（§4.3, Table 3），3 种子覆盖 ≤1.70pp 一致性。

**S4.** 跨架构验证——Mistral-7B（3-seed）和 Qwen-2.5-14B 上 PPL advantage ratio 一致（within 8%, Appendix N）。

**S5.** 训练效率高——单 GPU ~45min，predictor <1% base model 参数。

### Must-Fix 问题

**N1** [Critical] 无 wall-clock 加速收益
- 位置：Appendix A (Table 5), line 32-34
- 论文承认 unstructured element-wise masks "do not translate to wall-clock speedup"，当前实现增加 6.4% 推理延迟。论文定位是 sparsity prediction for efficiency，但无实际加速数据，实践动机被根本削弱。

**N2** [Critical] Per-layer KL 分解的 "97.5% signal type" claim 基于 confounded K=1 设置
- 位置：§4.5 (experiments.tex line 162-163), Table 19
- K=1 训练 mask 1/32 层 vs 推理 mask 32 层，train-inference mismatch 严重。K=4 pilot 仅 single-seed，且 MMLU K=4 超过 E2E KL（43.5 vs 40.7±1.3），GSM8K 负向 gap closure（-6.8%）——反常结果未能排除。

**N3** [Major] 下游知识任务系统性退化，framing 偏重 PPL
- 位置：Table 2, Table 14, Limitations
- MMLU/GSM8K 退化跨 8B/14B 两个 scale，跨 LLaMA/Qwen 两个架构。Abstract/Introduction 以 PPL 改进为主叙事，下游 trade-off 仅在 Conclusion 以 "task- and scale-dependent" 一笔带过。

### Should-Fix 问题

**W1** [Major] C1 的 trajectory confound——oracle masks 从特定 KL trajectory 提取，s42 oracle 来自 earlier training run（Table 3 footnote）。C1 证明 masks 可 transfer，但未证明 KL 是发现好 masks 的唯一/最佳途径。

**W2** [Major] 训练/评估域重叠——WikiText-103 训练 + WikiText-2 评估均来自 Wikipedia。C4 OOD 显示 31× 更高 cross-seed variance。

**W3** [Minor] MSE baseline 可能未被公平调参——seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）表明配置不够稳健。

**W4** [Minor] Global allocation 30% MMLU σ=9.5pp，结果不可解读。

**W5** [Minor] 符号冲突——g^(ℓ) 在 Eq.(1) 为 gate activation，Eq.(4) 中 g1/g2 为 Gumbel noise。

### Questions

Q1. K=4 是否有多种子数据？MMLU 超过 E2E KL 是否为系统性现象？
Q2. 有没有尝试 per-layer sparsity 约束来缓解 L22-L28 过度修剪？
Q3. 补偿对 BCE predictor 的效果如何？"compensation provides no benefit" 可能仅因 KL 自带补偿。
Q4. 更大/更多样训练集是否能缓解 OOD variance？

### Missing References

- Griffin et al., 2024 (Mixture of A Million Experts)
- Mirzadeh et al., 2024 (ReLU-fication of LLMs)
- Wanda (已引未对比讨论互补性)

### 结论

论文有学术价值（新视角、全面消融、诚实 limitation），但三个核心问题阻止 Conference-level：(1) 无实际推理加速；(2) 知识任务系统性退化无解决路径；(3) 核心分析 claim (97.5% signal type) 基于 confounded 实验。适合 Findings track。

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

_source line 1712 · 2026-05-22T13:08:41.175497+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 145

## Round 145

2 recorded events


### User

_source line 1713 · 2026-05-22T13:08:43.727903+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分总结：Overall 3 (Findings)，Confidence 4/5。**

三个核心问题：
1. **无 wall-clock 加速**（+6.4% overhead），实践动机薄弱
2. **Per-layer KL 分解的 97.5% signal-type claim** 基于 confounded K=1 设置，K=4 pilot 仅 single-seed 且有反常结果
3. **MMLU/GSM8K 系统性退化**跨模型跨架构，但论文 framing 偏重 PPL 改进

论文的消融设计和诚实的 limitation 讨论是优点，适合 Findings track。

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

_source line 1714 · 2026-05-22T13:08:51.035171+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 146

## Round 146

6 recorded events


### User

_source line 1715 · 2026-05-22T13:09:44.488941+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 扎实的实证分析——2D taxonomy 和 target-swap ablation 是有价值的方法论贡献，但 recipe 层面对 MaskLLM 的增量有限，且缺乏实际加速，限制了主会议级别的 excitement。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（多 seed、cross-arch），但 97.5% signal type 上界基于非正交分解不可靠；K=4 pilot 单 seed；主表实际 sparsity 不匹配 |
| Excitement | 2.5/5 | KL+Gumbel+frozen model recipe 与 MaskLLM 高度重合；无实际 wall-clock 加速（反增 6.4%）；分析框架有价值但 insights 部分可预期 |
| Reproducibility | 4/5 | 详细的超参数、多 seed 评估、训练步数/温度/bottleneck 灵敏度分析；但未释放代码 |
| Confidence | 4/5 | 熟悉 activation sparsity 和 KL 蒸馏领域 |

---

## 主要优势

**S1. Target-swap ablation (C1) 实验设计精巧。** 通过将 KL 发现的 mask 喂给 BCE predictor 来解耦 mask 质量 vs. 梯度耦合，这是一个genuinely informative 的因果推断实验。Table 3 在 3 个 seed (30%) 和 1 个 seed (50%) 上结果一致（max Δ≤1.70pp），证据充分。(Section 4.4, Table 3)

**S2. 多 seed 评估 + 诚实的混合结果报告。** 3-seed 评估（s42/s123/s456）贯穿全文，cross-seed variance 分析透明（如 30% global MMLU σ=9.5pp vs. uniform σ=1.3pp）。论文坦诚报告 KL 在 MMLU/GSM8K 上的系统性回退（8B -5.2pp, 14B -20pp GSM8K），没有选择性报告。(Table 2, Section 4.2, Limitations)

**S3. 2D taxonomy 提供清晰的组织框架。** signal type × coupling scope 的分解虽然概念上简单，但有效地将 DejaVu/ShadowLLM/FastForward/本文放入统一坐标系。Table 1 + Appendix L 的讨论完整。(Section 3.7, Table 1)

**S4. 跨架构验证有说服力。** 在 Mistral-7B (GQA+sliding window) 和 Qwen-2.5-14B 上验证 PPL 改善的泛化性。Mistral 3-seed 数据（PPL -17.3%）增强结论可信度。(Section 4.6, Tables 12-13)

**S5. 消融实验覆盖全面。** Table 4 覆盖 5 种 loss variant + 2 种 relaxation + 2 种 coupling scope，系统性很强。bottleneck/temperature/training steps 的灵敏度分析也值得赞赏。(Section 4.5, Appendix B)

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **与 MaskLLM 的 recipe 新颖性区分不足**
- 具体位置：Section 2 (Related Work), paragraph "Predictor-Based Contextual Sparsity"
- 问题：MaskLLM (Fang et al., 2024, NeurIPS) 使用 frozen weights + learnable masks + KL divergence + Gumbel-Softmax，与本文的 frozen weights + predictor network + KL divergence + Gumbel-Sigmoid 在 recipe 层面高度重合。论文在 Related Work 中承认 "shares the recipe-level principle" 并指出技术差异（static N:M vs. dynamic per-token），但这一区分未在实验中量化：没有与 MaskLLM 的直接对比（即使是在 activation sparsity 设定下）。论文声称的核心增量是 "analytical"（分析框架），但如果 recipe 本身被视为 known technique 的直接应用，分析框架的新颖性是否足以支撑独立贡献就值得质疑。
- 为什么影响接收：Reviewer 可能将本文视为 "MaskLLM applied to activation sparsity" + 事后分析，而非独立方法论贡献。
- 建议修改方向：(1) 在 Introduction 或 Section 3 中更明确地论证 dynamic activation sparsity 与 static N:M sparsity 的本质差异（generalization to unseen inputs、per-token variability、与 TEAL global allocation 的交互）为什么使得这不是简单的 recipe 迁移；(2) 如果可能，在 activation sparsity 设定下与 MaskLLM 的 learnable-mask variant 做实验对比。

**N2** [critical] **无实际推理加速，实用价值存疑**
- 具体位置：Appendix A (Table 5), Section 4.6 最后一段
- 问题：Predictor pipeline 增加 6.4% latency overhead（126.78 vs. 119.11 ms/fwd），即使在 50% sparsity 下也没有净加速。论文在 Appendix A 中坦承 "unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support"，并明确 "Our contribution is prediction quality and inference simplification, not end-to-end latency reduction"。但这意味着论文的实际应用场景 entirely depends on 未来的 sparse kernel 支持——目前不存在的基础设施。
- 为什么影响接收：对于 efficiency 论文，无法展示实际加速是重大缺陷。论文定位为 "empirical study"，但 Introduction 的 framing（"learned sparsity predictors"、"inference allocates budgets globally"）暗示效率是核心目标。这一 gap 在审稿中很可能被其他 reviewer 重点关注。
- 建议修改方向：(1) 更早、更显著地声明本文是分析/理解导向而非效率导向（目前这一声明藏在 Introduction 倒数第二段和 Appendix A 中）；(2) 提供 Triton block-sparse 或类似方案的 proof-of-concept 加速数据，即使粗糙也能大幅增强实用性论点。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **"97.5% signal type" 声称基于非正交分解**
- 具体位置：Section 4.5 "Per-Layer KL" paragraph, Abstract line 5, Conclusion
- 问题：论文反复引用 "signal type accounts for up to 97.5% of the gap"，但在 Section 4.5 脚注中承认 "signal type and coupling scope are not fully orthogonal"。这个 97.5% 是 (Per-layer KL - MSE) / (E2E KL - MSE) 的比值，但 per-layer KL 同时改变了 signal type AND 引入了部分 end-to-end 信号（通过 full forward pass 计算 KL），所以这两个维度不是独立的。将这个数字放在 Abstract 和 Conclusion 中作为 headline finding 是 overclaim。
- 建议：将 "up to 97.5%" 降级为 "a substantial majority" 或在每次引用时明确标注 "upper bound, dimensions not orthogonal"。目前 Abstract 中没有任何 caveat。

**W2** [major] **K=4 mismatch pilot 仅单 seed，但结论被推广**
- 具体位置：Section 4.5 (最后一段), Appendix R (Table 17)
- 问题：K=4 实验用来分解 mismatch vs. genuine coupling 效应，但只有 seed 42 一个数据点。考虑到 30% global MMLU 的 σ=9.5pp，单 seed 的 K=4 MMLU=43.5 超过 E2E KL 3-seed mean 40.7±1.3 可能完全是随机波动。论文在 Table 17 注释中说 "interpret cautiously"，但 Conclusion 和 Abstract 中直接写 "a K=4 mismatch pilot reveals task-dependent downstream structure"，hedging 不够。
- 建议：在 Abstract/Conclusion 中明确标注 "(single seed, preliminary)"；或增加至少 2 个额外 seed 的 K=4 数据。

**W3** [major] **主表 sparsity 不匹配：KL 28.5% vs. TEAL 29.3%**
- 具体位置：Table 2 footnote ‡, Appendix C
- 问题：Table 2 的 30% 对比中，KL 实际 sparsity 为 28.5% 而 TEAL 为 29.3%。虽然 Appendix C 提供了 matched-sparsity 对比（14.5% improvement at 28.5%），但主表用的是 mismatched 数据（19% improvement），且 Abstract 引用的 "14.5%" 来自 appendix 的 matched 对比而非主表。这种主表/Abstract 数字不一致容易混淆读者。
- 建议：在主表中明确标注实际 sparsity 或使用 matched-sparsity 数字作为 headline claim。

**W4** [minor-to-major] **下游任务回退缺乏深入分析**
- 具体位置：Section 4.2 "Task-Type Split", Section 4.6 最后一段
- 问题：KL 在 MMLU 和 GSM8K 上系统性输给 TEAL 和 magnitude-based 方法（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp）。论文将此归因于 "distribution-matching objectives systematically sacrifice reasoning-critical pathways" 和 late-layer over-pruning (L22-L28 sparsity 48-57%)，但没有验证这一因果链。如果问题确实是 late-layer starvation，是否可以通过 layer-wise sparsity constraint 来缓解？论文未尝试这一自然的 follow-up。
- 建议：增加一个 layer-constrained sparsity 实验（如限制 late-layer sparsity ≤ 35%），验证 late-layer starvation 假说。

**W5** [minor] **Baseline 选择不够全面**
- 具体位置：Section 4.1 "Baselines"
- 问题：实验 baseline 仅包括 TEAL、BCE (DejaVu-style)、MSE (ShadowLLM-style)。缺少与以下方法的对比：(1) R-Sparse（SVD projection-based, 同为 learned predictor）；(2) CATS（per-layer threshold adaptation, training-free 但更 sophisticated than TEAL）；(3) FastForward 的完整 pipeline（论文只测试了 compensation 组件）。这些缺失的 baseline 可能部分解决论文声称的 "所有 prior predictor-based methods 使用 decomposed/intermediate objectives" 这一 gap。
- 建议：至少补充一个 training-free baseline (CATS 或 R-Sparse) 的对比。

---

## 小问题（不影响接收）

- **M1** [minor] Introduction 第 18 行 "Wall-clock speedup requires sparse kernel support not addressed here (Appendix A)" — 这个关键 disclaimer 放在括号里太隐蔽，建议提升到更显眼的位置。
- **M2** [minor] Table 2 注释过长（6 行），信息密度过高，可考虑拆分为正文说明。
- **M3** [minor] Section 3.7 的 taxonomy table（Table 1）中大部分 cell 为空或只有 "---"，作为 "Two-Dimensional Taxonomy" 的 visual representation 信息含量有限。
- **M4** [minor] Figure 2 (PPL scaling) 只展示 global allocation，但主结论在 30% 时推荐 uniform allocation，图表与结论的 allocation 策略不一致。
- **M5** [info] 论文使用 `\usepackage[review]{acl}`、author 为 "Anonymous" — 匿名合规 ✓。正文 Sections 1-5 在 8 页内 ✓。Limitations 和 Ethics Statement 在正文后、不计页数 ✓。References 使用 natbib ✓。

---

## Missing References

以下相关工作可能需要讨论或与之对比：
1. **CATS** (Lee et al., 2024): per-layer threshold adaptation for SiLU/SwiGLU — 已在 Related Work 提及但无实验对比
2. **R-Sparse** (Zhang et al., 2025): rank-aware SVD projection for sparsity prediction — 已提及但无对比
3. **Griffin/Hawk** (De et al., 2024): gated linear recurrence with hardware-efficient sparsity — 未提及
4. **Turbo Sparse** (Song et al., 2024) 的 ReLUfication 后 KL distillation 步骤与本文有方法论重叠 — 已提及但未深入对比

---

## Questions for Authors

1. 如果在 activation sparsity 设定下实现 MaskLLM 的 learnable-mask approach（去掉 predictor network，直接学习 per-layer mask parameters + Gumbel-Softmax），PPL 和下游表现如何？这能直接隔离 "predictor generalization" 的贡献。
2. Late-layer over-pruning (L22-L28 at 48-57%) 是否可以通过 per-layer sparsity constraint 来缓解 MMLU/GSM8K 回退？
3. 为什么没有在 50% sparsity 下进行 3-seed K=4 实验？考虑到 coupling 在 50% 时从 2.5% 升至 10.6%，这一 regime 的 K=4 数据更能支撑 coupling 重要性的 claim。
4. WikiText-103 训练 → WikiText-2 评估存在 domain overlap。C4 OOD 结果显示 cross-seed variance 增大 31×（CV 6.3% vs. 0.2%）。是否尝试过更 diverse 的训练数据（如 C4 subsample）来降低 OOD variance？

---

## 格式合规检查

| 项目 | 状态 |
|------|------|
| 正文 ≤ 8 页 | ✅ Sections 1-5 在 pages 1-8 |
| ACL template [review] | ✅ `\usepackage[review]{acl}` |
| Double-blind (Anonymous) | ✅ Author: "Anonymous ACL submission" |
| Mandatory Limitations | ✅ 1 段，覆盖 3 个点 |
| Ethics Statement | ✅ 存在且合理 |
| References 格式 | ✅ natbib, acl_natbib.bst |
| Table/Figure 编号 | ✅ 连续编号，引用正确 |

---

## Overall Assessment 详细理由

**给分 3.0 (Findings)** — Confidence 4/5

这是一篇质量不错的实证研究，target-swap ablation 和 2D taxonomy 框架提供了有价值的方法论工具。实验执行严谨（多 seed、多架构、全面消融）。但以下因素限制了 main conference 级别的 excitement：

1. **Recipe 新颖性有限**：KL+Gumbel+frozen model 的组合在 MaskLLM 中已建立，本文的增量是将其从 static N:M weight sparsity 迁移到 dynamic activation sparsity。分析框架虽有价值但概念上较直观。
2. **无实际加速**：作为 efficiency-motivated 的工作，增加 6.4% overhead 而无法展示 wall-clock speedup 是重大短板。
3. **下游回退显著**：MMLU/GSM8K 的系统性回退（跨规模一致）意味着 KL predictor 在 knowledge-intensive 场景下不如 training-free baseline，限制了实用价值。
4. **关键 claims 的 evidence 不够 robust**：97.5% 上界基于非正交分解；K=4 pilot 单 seed；主表 sparsity 不匹配。

论文适合 Findings 发表——分析框架对后续 predictor-based sparsity 研究有参考价值，但目前的 novelty 和 practical impact 不足以支撑主会议接收。

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

_source line 1716 · 2026-05-22T13:10:16.289004+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall**: 3.0 (Findings), Confidence 4/5\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（多 seed、cross-arch），但 97.5% signal type 上界基于非正交分解不可靠；K=4 pilot 单 seed；主表实际 sparsity 不匹配 |\n| Excitement | 2.5/5 | KL+Gumbel+frozen model recipe 与 MaskLLM 高度重合；无实际 wall-clock 加速（反增 6.4%）；分析框架有价值但 insights 部分可预期 |\n| Reproducibility | 4/5 | 详细的超参数、多 seed 评估、训练步数/温度/bottleneck 灵敏度分析；但未释放代码 |\n\n### 主要优势\nS1. Target-swap ablation (C1) 实验设计精巧。Table 3 在 3 个 seed (30%) 和 1 个 seed (50%) 上结果一致（max Δ≤1.70pp）。\nS2. 多 seed 评估 + 诚实的混合结果报告。3-seed 贯穿全文，cross-seed variance 分析透明。\nS3. 2D taxonomy 提供清晰的组织框架。\nS4. 跨架构验证有说服力（Mistral-7B 3-seed, Qwen-2.5-14B）。\nS5. 消融实验覆盖全面（Table 4, 8 种配置）。\n\n### Must-Fix 问题\n**N1** [critical] 与 MaskLLM 的 recipe 新颖性区分不足——KL+Gumbel+frozen model 组合在 MaskLLM 已建立，本文增量是从 static N:M weight sparsity 迁移到 dynamic activation sparsity。Related Work 承认 \"shares the recipe-level principle\" 但未实验量化差异。\n**N2** [critical] 无实际推理加速——6.4% overhead，unstructured masks 无 wall-clock speedup。Introduction framing 暗示效率目标但无法兑现。\n\n### Should-Fix 问题\n**W1** [major] \"97.5% signal type\" 基于非正交分解，Abstract/Conclusion 中无 caveat。\n**W2** [major] K=4 pilot 仅单 seed，MMLU 43.5 超过 E2E KL 40.7±1.3 可能为随机波动，但 Abstract/Conclusion hedging 不够。\n**W3** [major] 主表 sparsity 不匹配（KL 28.5% vs TEAL 29.3%），Abstract 引用的 14.5% 来自 appendix matched 对比而非主表 19%。\n**W4** [minor-to-major] 下游知识任务退步归因 late-layer over-pruning 但未验证因果链（如 layer-constrained sparsity 实验）。\n**W5** [minor] Baseline 缺少 R-Sparse/CATS/FastForward 完整 pipeline 对比。\n\n### 小问题\nM1. Introduction disclaimer 放在括号里太隐蔽。\nM2. Table 2 注释过长。\nM3. Taxonomy table 信息含量有限。\nM4. Figure 2 只展示 global allocation 但推荐 uniform。\nM5. 格式合规 ✓。\n\n### Missing References\nCATS (已提及无对比), R-Sparse (已提及无对比), Griffin/Hawk (De et al., 2024), TurboSparse KL distillation 步骤。\n\n### Questions\nQ1. 在 activation sparsity 设定下实现 MaskLLM learnable-mask approach（去掉 predictor），PPL 如何？\nQ2. Late-layer over-pruning 是否可通过 per-layer constraint 缓解？\nQ3. 为什么没有 50% K=4 3-seed 数据？\nQ4. 是否尝试更 diverse 训练数据降低 OOD variance？\n\n---\n\n请对以上每条 N/W/M/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall**: 3.0 (Findings), Confidence 4/5\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（多 seed、cross-arch），但 97.5% signal type 上界基于非正交分解不可靠；K=4 pilot 单 seed；主表实际 sparsity 不匹配 |\n| Excitement | 2.5/5 | KL+Gumbel+frozen model recipe 与 MaskLLM 高度重合；无实际 wall-clock 加速（反增 6.4%）；分析框架有价值但 insights 部分可预期 |\n| Reproducibility | 4/5 | 详细的超参数、多 seed 评估、训练步数/温度/bottleneck 灵敏度分析；但未释放代码 |\n\n### 主要优势\nS1. Target-swap ablation (C1) 实验设计精巧。Table 3 在 3 个 seed (30%) 和 1 个 seed (50%) 上结果一致（max Δ≤1.70pp）。\nS2. 多 seed 评估 + 诚实的混合结果报告。3-seed 贯穿全文，cross-seed variance 分析透明。\nS3. 2D taxonomy 提供清晰的组织框架。\nS4. 跨架构验证有说服力（Mistral-7B 3-seed, Qwen-2.5-14B）。\nS5. 消融实验覆盖全面（Table 4, 8 种配置）。\n\n### Must-Fix 问题\n**N1** [critical] 与 MaskLLM 的 recipe 新颖性区分不足——KL+Gumbel+frozen model 组合在 MaskLLM 已建立，本文增量是从 static N:M weight sparsity 迁移到 dynamic activation sparsity。Related Work 承认 \"shares the recipe-level principle\" 但未实验量化差异。\n**N2** [critical] 无实际推理加速——6.4% overhead，unstructured masks 无 wall-clock speedup。Introduction framing 暗示效率目标但无法兑现。\n\n### Should-Fix 问题\n**W1** [major] \"97.5% signal type\" 基于非正交分解，Abstract/Conclusion 中无 caveat。\n**W2** [major] K=4 pilot 仅单 seed，MMLU 43.5 超过 E2E KL 40.7±1.3 可能为随机波动，但 Abstract/Conclusion hedging 不够。\n**W3** [major] 主表 sparsity 不匹配（KL 28.5% vs TEAL 29.3%），Abstract 引用的 14.5% 来自 appendix matched 对比而非主表 19%。\n**W4** [minor-to-major] 下游知识任务退步归因 late-layer over-pruning 但未验证因果链（如 layer-constrained sparsity 实验）。\n**W5** [minor] Baseline 缺少 R-Sparse/CATS/FastForward 完整 pipeline 对比。\n\n### 小问题\nM1. Introduction disclaimer 放在括号里太隐蔽。\nM2. Table 2 注释过长。\nM3. Taxonomy table 信息含量有限。\nM4. Figure 2 只展示 global allocation 但推荐 uniform。\nM5. 格式合规 ✓。\n\n### Missing References\nCATS (已提及无对比), R-Sparse (已提及无对比), Griffin/Hawk (De et al., 2024), TurboSparse KL distillation 步骤。\n\n### Questions\nQ1. 在 activation sparsity 设定下实现 MaskLLM learnable-mask approach（去掉 predictor），PPL 如何？\nQ2. Late-layer over-pruning 是否可通过 per-layer constraint 缓解？\nQ3. 为什么没有 50% K=4 3-seed 数据？\nQ4. 是否尝试更 diverse 训练数据降低 OOD variance？\n\n---\n\n请对以上每条 N/W/M/Q 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-22T13:10:41.882504+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25593
}
```

</details>

---
