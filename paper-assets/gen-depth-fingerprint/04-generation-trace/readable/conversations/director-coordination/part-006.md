# Director coordination — Part 6 of 14

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/46/46a4a073b0cc4314da71.json)

## Round 148

### Tool result

_source line 1645 · 2026-05-19T03:18:28.747767+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\\n- Positioning: **Findings paper**（非 main conference long paper）\\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.764. Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\\n\\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while sha
…[truncated 6457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-19T03:18:35.171723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "129",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "129",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-19T03:18:35.674360+00:00_

129	\caption{LOGO binary F1 (gen-1 vs.\ gen-2+, 8-gen pooled) with inference cost. Ensembles achieve marginally higher F1 at 2.4$\times$ inference time and 3.2$\times$ GPU memory; individual detectors vary widely when repurposed for depth.}
130	\label{fig:baseline-ci}
131	\end{figure}
132	\FloatBarrier
133	
134	\input{appendix_feature_correlation}
135	\FloatBarrier
136	
137	\section{Cross-Family Reference Models}
138	\label{app:cross-ref}
139	\input{table4}
140	\FloatBarrier
141	
142	\input{appendix_seed_control}
143	\FloatBarrier
144	
145	\input{appendix_tost}
146	\FloatBarrier
147	
148	\section{DDR Partition Validation}
149	\label{app:ddr-validation}
150	\input{appendix_ddr_validation}
151	\FloatBarrier
152	
153	\section{Generator Subset Summary}
154	\label{app:gen-subsets-section}
155	\input{appendix_generator_subsets}
156	\FloatBarrier
157	
158	\input{appendix_qualitative_examples}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-19T03:18:36.177758+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/gen-depth-fingerprint/artifacts/_project/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/gen-depth-fingerprint/artifacts/_project/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-19T03:18:36.429043+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-19T03:18:36.429350+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/gen-depth-fingerprint/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-19T03:18:36.479712+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-19T03:18:39.284619+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-19T03:18:39.787552+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-19T03:18:40.141161+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper -name \"*.tex\" -type f | sort",
  "description": "List all .tex files in the paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper -name \"*.tex\" -type f | sort",
    "description": "List all .tex files in the paper directory"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-19T03:18:40.242248+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex
/home/ubuntu/.agent-ml-research-idea_gen_051
…[truncated 2501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-19T03:18:45.764257+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-19T03:18:46.518768+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-19T03:18:46.770231+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"File not found\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"File not found\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-19T03:18:46.821049+00:00_

# Round 22→23 Review Issues — Updated after R22 action matrix execution

# ============ CRITICAL (Must-Fix) ============

- id: "R1-N1"
  summary: "DDR tri-partition 阈值统计基础不可靠：异方差下使用 Cohen's d"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 22
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R1首提，R2 AGREE"}
    - {round: 22, reviewers: "R1,R2", note: "需补充 Glass's Δ 或 Cliff's delta 作为 sensitivity check"}
  action_items:
    - {round: 21, action: "appendix_ddr_validation.tex 已有 k-means + TOST + holdout split", assigned_to: "Director", status: "done"}
    - {round: 22, action: "computed Glass's Δ + Cliff's δ for all 7 features; added Table in appendix_ddr_validation.tex §Heteroscedasticity Sensitivity. Gap 9.5× confirmed under Glass's Δ", assigned_to: "Director", status: "done"}
  resolution: ""
  resolution_round: null

- id: "R1-N2"
  summary: "DDR 3/1/3 partition post-hoc 选择，统计证据弱于 2-group structure"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 22
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R1首提，R2 AGREE"}
    - {round: 22, reviewers: "R1,R2", note: "strongest consensus: k=2 silhouette=0.632 > k=3 0.499; holdout 3/2/2"}
  action_items:
    - {round: 21, action: "§4.2 已添加 clustering 引用", assigned_to: "Director", status: "done"}
    - {round: 22, action: "Restructured §4.2 opening + Contribution 2 to lead with '2-group primary structure' then '3/1/3 domain-informed refinement'. Hierarchy now explicit throughout.", assigned_to: "Director", status: "done"}
  resolution: ""
  resolution_round: null

- id: "R2-N1"
  summary: "Framing 矛盾：Introduction 实用动机 vs Discussion 诊断定位"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 22
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R2首提，R1完全同意"}
    - {round: 22, reviewers: "R1,R2", note: "Intro L5 'downstream implications' vs 
…[truncated 10226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-19T03:19:10.163097+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-19T03:19:10.213993+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-19T03:19:14.381815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-19T03:19:14.482689+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-19T03:19:17.897700+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 2 -name \"config.yaml\" -o -name \"project_config.yaml\" 2>/dev/null",
  "description": "Find config files at project root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 2 -name \"config.yaml\" -o -name \"project_config.yaml\" 2>/dev/null",
    "description": "Find config files at project root level"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-19T03:19:17.948452+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1666 · 2026-05-19T03:19:50.678809+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- **标题**: \"Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\"\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper ≤ 8 页正文 + 无限参考文献 + 无限附录\n- ACL 模板，`[review]` 选项\n- Double-blind 匿名\n- 必须包含 Limitations section（conclusion 之后、references 之前，不占页数）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **方法论严谨性**：DDR (Differential Depth Response) 框架的定义是否严格？tri-partition (drifting/stable/shape) 的划分标准是否有充分统计依据？Cohen's d / 效应量的使用是否恰当（注意异方差问题）？\n2. **实验设计**：LOGO (Leave-One-Generator-Out) 评估是否无泄漏？gen-0 seed sharing 是否充分控制？Binary F1 = 0.694 作为 primary metric 是否合理？Cross-model chain 实验设计是否科学？\n3. **统计分析**：Bootstrap CI 计算是否正确？McNemar test 使用是否恰当？TOST 等效性检验的 n=3 统计效力问题？温度消融的统计显著性？\n4. **消融实验完整性**：LOFO, feature ablation, length confound, prompt type 等消融是否覆盖关键变量？是否有遗漏的混淆因素？\n5. **Baseline 公平性**：与 FastDetectGPT, Binoculars 等 baseline 的对比是否公平？是否有更强的 baseline 被忽略？\n\n请阅读全文后，按以下结构输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- Questions (需要作者回答的)\n- Missing References\n- Overall Assessment (评分 + 理由)\n- Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- **标题**: \"Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\"\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper ≤ 8 页正文 + 无限参考文献 + 无限附录\n- ACL 模板，`[review]` 选项\n- Double-blind 匿名\n- 必须包含 Limitations section（conclusion 之后、references 之前，不占页数）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **方法论严谨性**：DDR (Differential Depth Response) 框架的定义是否严格？tri-partition (drifting/stable/shape) 的划分标准是否有充分统计依据？Cohen's d / 效应量的使用是否恰当（注意异方差问题）？\n2. **实验设计**：LOGO (Leave-One-Generator-Out) 评估是否无泄漏？gen-0 seed sharing 是否充分控制？Binary F1 = 0.694 作为 primary metric 是否合理？Cross-model chain 实验设计是否科学？\n3. **统计分析**：Bootstrap CI 计算是否正确？McNemar test 使用是否恰当？TOST 等效性检验的 n=3 统计效力问题？温度消融的统计显著性？\n4. **消融实验完整性**：LOFO, feature ablation, length confound, prompt type 等消融是否覆盖关键变量？是否有遗漏的混淆因素？\n5. **Baseline 公平性**：与 FastDetectGPT, Binoculars 等 baseline 的对比是否公平？是否有更强的 baseline 被忽略？\n\n请阅读全文后，按以下结构输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- Questions (需要作者回答的)\n- Missing References\n- Overall Assessment (评分 + 理由)\n- Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1667 · 2026-05-19T03:20:04.150944+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13472
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-19T03:20:04.301954+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 写作质量 + 完整性**。\n\n## 论文信息\n- **标题**: \"Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\"\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper ≤ 8 页正文 + 无限参考文献 + 无限附录\n- ACL 模板，`[review]` 选项\n- Double-blind 匿名\n- 必须包含 Limitations section（conclusion 之后、references 之前，不占页数）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **新颖性评估**：Generation depth classification 这个任务定义是否有足够新颖性？DDR 框架的理论贡献在哪里？与已有 model collapse / detection 工作的差异是否实质性的？是否有被忽略的并行工作？\n2. **写作质量**：\n   - Abstract 是否在 30 秒内传达论文价值？\n   - Introduction 叙事线是否连贯（问题→缺口→洞察→贡献）？\n   - 全文主线是否统一（Introduction 的 framing 是否与 Discussion/Conclusion 一致）？\n   - 是否有 AI 写作痕迹（em-dash、-ing phrases、过度分段、用词黑名单）？\n   - 专有名词是否首次出现时有定义？\n3. **完整性**：\n   - Related Work 是否充分定位（不是 survey 式罗列）？引用密度是否足够？\n   - Contribution 列表中每条是否有对应 section/table 支撑？\n   - 附录内容是否在正文中有引用且融入叙事？\n   - Limitations section 是否诚实全面？\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 匿名化是否完整（无 author 泄漏）？\n   - 图表字体 ≥ 7pt？Caption 自包含？\n   - 引用格式一致？有无孤立 bib entry？\n\n请阅读全文后，按以下结构输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- Questions (需要作者回答的)\n- Missing References\n- Overall Assessment (评分 + 理由)\n- Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 写作质量 + 完整性**。\n\n## 论文信息\n- **标题**: \"Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\"\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n\n## Venue 格式要求\n- Long paper ≤ 8 页正文 + 无限参考文献 + 无限附录\n- ACL 模板，`[review]` 选项\n- Double-blind 匿名\n- 必须包含 Limitations section（conclusion 之后、references 之前，不占页数）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n1. **新颖性评估**：Generation depth classification 这个任务定义是否有足够新颖性？DDR 框架的理论贡献在哪里？与已有 model collapse / detection 工作的差异是否实质性的？是否有被忽略的并行工作？\n2. **写作质量**：\n   - Abstract 是否在 30 秒内传达论文价值？\n   - Introduction 叙事线是否连贯（问题→缺口→洞察→贡献）？\n   - 全文主线是否统一（Introduction 的 framing 是否与 Discussion/Conclusion 一致）？\n   - 是否有 AI 写作痕迹（em-dash、-ing phrases、过度分段、用词黑名单）？\n   - 专有名词是否首次出现时有定义？\n3. **完整性**：\n   - Related Work 是否充分定位（不是 survey 式罗列）？引用密度是否足够？\n   - Contribution 列表中每条是否有对应 section/table 支撑？\n   - 附录内容是否在正文中有引用且融入叙事？\n   - Limitations section 是否诚实全面？\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 匿名化是否完整（无 author 泄漏）？\n   - 图表字体 ≥ 7pt？Caption 自包含？\n   - 引用格式一致？有无孤立 bib entry？\n\n请阅读全文后，按以下结构输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n- Questions (需要作者回答的)\n- Missing References\n- Overall Assessment (评分 + 理由)\n- Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-19T03:20:06.119341+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1817
}
```

</details>

---


### Assistant

_source line 1670 · 2026-05-19T03:20:09.478642+00:00_

Round 1 任务已分配。Reviewer 1（方法/实验/统计）和 Reviewer 2（新颖性/写作/完整性）正在独立审稿。等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 149

## Round 149

2 recorded events


### User

_source line 1671 · 2026-05-19T03:27:51.582882+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见 — Round 1

**论文**: "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"
**Venue**: EMNLP 2026 (ARR Long Paper)
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## Summary

本文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+（而非传统的二元 real-vs-synthetic），并在 8 个 base model（5 个 family，0.6B–8B 参数）上识别出 differential depth response (DDR) 三分结构：3 个 drifting 特征（entropy mean, TTR, hapax ratio）、1 个 intermediate 特征（entropy std）、3 个 near-stationary 特征（entropy max, tail decay, entropy min）。7 特征集成在 LOGO 评估下获得 leak-free binary F1 = 0.694。论文诚实地承认了 base model 限制和 instruction tuning 下信号退化的问题。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 任务定义新颖、实验控制严谨、DDR 三分结构是有价值的经验性发现，但 base-model-only 限制严重削弱实际意义，primary metric 偏低，且评估设计中 gen-0 seed sharing 使核心三分类任务无法被干净评估。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法论整体合理，DDR tri-partition 有多指标交叉验证支撑。但 Cohen's d 在异方差条件下的使用、tail_decay 仅 4/8 通过 TOST 等效检验、downstream TOST 仅 n=3 seeds 等问题削弱部分 claim 的统计可靠性 |
| Excitement | 2.5/5 | 任务定义新颖（depth classification vs binary detection），DDR 分解提供了有价值的分析框架。但仅限 base model 的结论在 instruct model 主导的真实场景中适用性极低，binary F1=0.694 的实用价值有限 |
| Reproducibility | 4/5 | 实验细节充分（模型、超参数、软件版本、GPU 小时），承诺公开代码和数据。多个 generator subset 虽有解释，但增加了复现复杂度 |
| Overall Assessment | 3.0 | Findings 水平——有真实的科学贡献（DDR 三分结构），但 base-model 限制、中等性能、gen-0 评估污染共同限制了影响力 |
| Confidence | 4/5 | 仔细审阅了全文及所有附录，熟悉 AI-generated text detection 和统计检验方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Gen-0 seed sharing 使核心三分类评估失效，论文的 framing 与实际可靠评估之间存在落差
- 具体位置：§3.2, §4.1, Table 1, Abstract
- 问题：论文将任务定义为 "generation depth classification (gen-0/gen-1/gen-2+)"（Abstract line 2, §1 Contribution 1），但由于 gen-0 seeds 在所有 generators 间共享，LOGO 评估中 gen-0 文本在训练集和测试集中完全相同。论文正确地将 binary F1 (gen-1 vs gen-2+) 作为 primary metric，但这实质上将核心任务降级为二分类。Confusion matrix（Appendix G）显示 gen-0 recall = 99.4%，几乎完全由 seed overlap 驱动。Independent-seed 实验（Appendix T）仅使用 2 个 generator（Pythia-2.8B, OLMo），不足以验证 full 3-class LOGO 的可靠性。
- 为什么影响接收：论文的 Contribution 1 宣称 "formulate generation depth classification...gen-0/gen-1/gen-2+"，但实际上只能可靠评估 gen-1 vs gen-2+ 的二元区分。3-class F1 = 0.762 被标注为 "may carry upward bias"（Table 1 脚注），但仍在 Abstract 中作为结果呈现。这使得论文的核心 framing（三分类 depth profiling）与实际实验支撑之间存在显著落差。
- 建议修改方向：(1) 在 full 8-generator LOGO 设置下进行 independent-seed 实验，为每个 generator 使用不同的 seed pool，报告干净的 3-class LOGO F1；(2) 或者将论文 framing 调整为 "depth profiling 以 binary gen-1 vs gen-2+ 区分为核心"，降低 3-class 叙事的权重；(3) Abstract 应明确说明 3-class metric 受 seed sharing 影响，binary F1 是唯一 leak-free 指标。

**N2** [critical] 仅限 base model 的限制对论文 significance 造成根本性约束
- 具体位置：§5 Discussion, §Limitations, Appendix K (instruct)
- 问题：论文明确限定为 base (pretrained) models，但 web 上绝大多数 LLM 生成文本来自 instruction-tuned / RLHF-aligned 模型。Appendix K 显示 instruct 模型下 entropy mean ρ 翻转符号（−0.60 → +0.48），6/7 特征方向反转（OLMo, Qwen），LOGO F1 从 0.763 暴跌至 0.338（OLMo-Instruct）。这不是一个需要微调的边缘问题——DDR 的核心结构（哪些特征 drift、哪些 stationary）在 instruct model 下被根本性地颠覆。
- 为什么影响接收：如果 DDR 是 base model 独有的现象，其科学价值仍然存在（理解 recursive generation dynamics），但论文多处暗示更广泛的适用性（Introduction: "how language models transform distributions under iterative conditioning"; Related Work 中与 model collapse 的联系），这些 claim 的范围超出了实验支撑。当前 framing 让读者可能高估方法的实际部署价值。
- 建议修改方向：(1) 在 Introduction 和 Abstract 中更显著地标注 base-model-only 限制（不仅在最后一句提及）；(2) 将 instruct model 结果从附录提升到正文 Discussion 中作为核心发现；(3) 讨论 DDR 特征方向反转的理论含义——这是否意味着 instruct model 的 recursive generation 具有质性不同的 dynamics？

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Tail decay 作为 "near-stationary" 特征的分类缺乏充分统计支撑
- 具体位置：§4.2, Table 5 (Appendix R), Table 6 (Appendix S)
- 问题：TOST 等效性检验（ε = 0.20）中，tail decay 仅 4/8 generators 通过，是 near-stationary 组中通过率最低的。Non-passing generators 的 |d| 范围为 0.15–0.22（Table 5），其中 OLMo 的 d=0.22 已超过 TOST bound。Sensitivity analysis 显示需要放松至 ε=0.25 才能达到 7/8 通过（Table 6）。将一个仅半数通过等效性检验的特征归入 "near-stationary" 组，削弱了 DDR 3/1/3 partition 的说服力。
- 建议：(1) 考虑将 tail decay 移至 intermediate 组或标记为 "weakly stationary"；(2) 或在正文中充分讨论其边界地位，而非仅在附录中处理。

**W2** [warning] Downstream utility 实验统计效力极低（n=3 seeds），不足以支撑 "null result" claim
- 具体位置：Appendix M, §5 Discussion
- 问题：Downstream fine-tuning 实验仅用 3 random seeds。Cohen's d 值高达 86.0 和 119.7（论文正确指出这是 artificial inflation），但 TOST 结果的可推广性同样有限。论文承认 "the TOST results have limited generalizability"，但 Discussion 仍将此作为关键结论之一引用："Depth composition does not determine downstream training utility at fixed sample count"（§4.3, §5）。以 n=3 的实验支撑一个跨 Section 反复引用的结论，统计基础过于薄弱。
- 建议：增加 seeds 至至少 10–20，或将该结论降级为 "preliminary observation"，在正文引用时加上 qualification。

**W3** [warning] 4-detector ensemble 的 baseline 结果反过来削弱了 DDR framework 的方法论贡献
- 具体位置：Table 2 (§4.3)
- 问题：4-detector ensemble binary F1 = 0.708 > 7-feature ensemble 0.705，4-det. + surface = 0.708。虽然论文将此定位为 "contextualizing depth discrimination ability rather than claim competitive advantage"，但这个结果意味着：(1) 现有检测方法已隐含深度信息；(2) 简单组合现有检测器就能达到或超过 DDR-based 方法。论文试图用 "inference cost" 差异（2.4×）来区分，但成本差距并不显著。DDR 的真正价值应在于其 interpretability 和分析框架，但论文对此的阐述不够充分。
- 建议：重新组织 baseline 讨论，重点强调 DDR 的分析价值（为什么 tri-partition 重要）而非分类性能竞争力。

**W4** [warning] 多个 generator subset 混用增加了 cross-experiment 比较的复杂性
- 具体位置：Appendix V (Table 9), 全文各处
- 问题：论文在不同实验中使用 5/6/8 generator 子集（cross-model chains: 5-gen, temperature: 4-gen, prompt-type: 1-gen, QLoRA: 6-gen, main LOGO: 8-gen）。虽然 Appendix V 记录了这些差异并解释为 "chronological expansion"，但导致以下问题：(1) Cross-reference 验证（Table 4, 5-gen LOGO）的结果无法直接与 main results（8-gen LOGO）对比；(2) Prompt-type 实验仅用 Pythia-2.8B 一个 generator，cross-prompt generalization 的 claim 缺乏跨模型验证；(3) 审稿人难以判断哪些结论仅基于子集有效。
- 建议：(1) 在核心 claim 上统一使用 8-gen LOGO 评估；(2) 对 prompt-type 实验增加至少 2–3 个 generators。

**W5** [warning] Cross-domain 实验使用 t=1.0（超出可靠范围），domain 和 temperature 效应混淆
- 具体位置：Appendix I
- 问题：Cross-domain 实验使用 t=1.0, top-p=1.0（论文自身在 Appendix H 中确认 t≥0.9 时方法退化 9.3–26.0 pp），导致 domain generalization 与 temperature sensitivity 无法分离。论文诚实地标注了这一 confound，并补充了 t=0.7 结果，但 t=0.7 下 Academic domain binary F1 降至 0.628，反而暗示了 cross-domain 信号可能比 t=1.0 结果所示的更弱。
- 建议：在 Limitations 中更显著地讨论这一混淆。Cross-domain claim 应基于 t=0.7 结果而非 t=1.0。

**W6** [warning] Cohen's d 作为 DDR 分区主要指标存在异方差问题
- 具体位置：§4.2 "Distributional shift quantification"
- 问题：Levene tests 拒绝了 drifting features 的等方差假设（p < 10^−10，方差比 1.86–2.21），但正文在定义 DDR partition 的关键阈值（d > 0.75 vs d < 0.10）时仍然使用 pooled Cohen's d。Heteroscedasticity-robust 指标（Glass's Δ, Cliff's δ）仅在 Appendix S 中报告。虽然 robust 指标确认了 partition（gap ≥ 9.5×），但主要叙事完全依赖的是不满足假设条件的 pooled d。
- 建议：在正文 §4.2 中同时报告 Glass's Δ 或 Cliff's δ，或至少注明 pooled d 在异方差条件下为保守估计。

---

## 小问题（不影响接收）

- **M1**: Abstract 中 "base (pretrained)" 出现 2 次，§3.1–3.2 中再次出现，重复注释显得冗余。保留首次括号解释即可。
- **M2**: Table 1 脚注 "†3-class F1 may carry upward bias from gen-0 seed sharing" 是关键信息，但脚注过于不显眼。应在 caption 主体中说明。
- **M3**: Feature correlation matrix（Appendix P, Table 7）显示 entropy mean 与 TTR/hapax 的 Pearson r = 0.86/0.81。这意味着 3 个 "drifting" features 共享大量方差，DDR 中的 "三个独立 drifting 信号" 实际上可能是同一个 latent factor 的不同投影。论文在 §4.2 提到 TTR-hapax 相关性但未充分讨论 entropy mean 与二者的高相关性对 DDR 解释的影响。
- **M4**: Qualitative example（Appendix X, Table 10）中 gen-2 文本明显退化为简单重复（"the son of the God of the Sky and the Goddess of the Earth" 重复 4 次），这种极端退化在较大模型中可能不常见。建议补充非 Pythia 模型的定性示例。
- **M5**: Ethics Statement 中 "62 GPU-hours on 4× RTX 5090" 合理，但缺少 CO₂ 排放估算（ARR 鼓励但不强制）。
- **M6**: 正文第 8 页 Discussion 中 "gen-1 per-class F1 = 0.63" 引用了 Appendix L 的结果，但 cross-model per-class 表（Appendix N, Table 8）中 gen-1 F1 = 0.768。应明确说明 0.63 指的是哪个评估设置。

---

## Questions（需要作者回答）

**Q1**: Independent-seed 实验（Appendix T）仅用 2 个 generators。能否在 full 8-generator LOGO 设置下报告 independent-seed 3-class F1？这是验证 gen-0 分类是否真正基于 distributional properties（而非 seed identity）的关键实验。

**Q2**: Cross-reference 实验（Table 4）使用 5-gen LOGO。在 full 8-gen 设置下（加入 Llama, Mistral），cross-reference spread 是否仍 ≤ 0.013？考虑到 Mistral-7B 的 binary F1 最低（0.633），reference model 选择可能对困难 generators 更敏感。

**Q3**: DDR tri-partition 中 3 个 drifting features 高度相关（entropy mean–TTR: r=0.86, entropy mean–hapax: r=0.81）。是否考虑过用 PCA 或 factor analysis 验证 drifting group 是否实际上对应单一 latent factor？如果是，DDR 的 "三分" 可能更准确地描述为 "一个 drifting 因子 + 1 intermediate + 3 stationary"。

**Q4**: 论文使用固定 prompt "Continue the following text: {text}"。在 real-world 场景中，递归生成链中的 prompt 可能不同（不同用户使用不同 prompt 风格）。Cross-prompt LOPTO 实验仅用 1 个 generator（Pythia-2.8B）。在多 generator 设置下，cross-prompt transfer 是否同样稳健？

**Q5**: Appendix H 显示 Qwen3-1.7B 在 t=0.5 和 t=0.7 下的 binary F1 完全相同（0.751），95% CI 缺失（"---"）。这是数据问题还是数值巧合？CI 缺失的原因是什么？

**Q6**: Table 2 中 "7-feature (ours)" 的 F1 (0.774/0.705) 与 Table 1 中 8-gen LOGO average (0.762/0.694) 存在差异。Table 2 caption 说明是 "pooled evaluation"。Pooled vs per-generator macro average 的差异从何而来？是否因为 pooled evaluation 在 class distribution 不同的 generator 上加权不同？

---

## Missing References

- 论文引用覆盖度总体充足（68 条引用），related work 的组织合理。以下为可补充方向（非必须）：
  - **Bao et al. (2024)** "On the Reliability of AI Text Detectors" — 关于检测器可靠性的分析，与 baseline comparison 相关
  - 更多关于 ordinal regression 在 NLP 中的应用文献（当前主要引用通用 ML 领域的 ordinal methods）
  - Guo et al. (2023) "How Close is ChatGPT to Human Experts?" — 关于 LLM 生成文本特性的早期分析

---

## 主要优势

1. **任务定义新颖且有意义**: Generation depth classification 将 binary detection 推进到更细粒度的 provenance 分析，是一个自然且重要的 research direction。与 model collapse 文献的联系建立得很好。

2. **实验控制极为严谨**: LOGO + LOFO + seed-level demeaning + independent-seed + length-matched + random-subsample control 构成了多层次的 confound control pipeline，体现了对实验设计的深入思考。很少见到如此完整的 control 链。

3. **DDR tri-partition 的分析框架有价值**: 即使分类性能一般，将特征空间分解为 drifting/intermediate/near-stationary 提供了一个理解 recursive generation dynamics 的有用透镜。多指标交叉验证（ρ, d, KS, Levene, TOST, Glass's Δ, Cliff's δ, clustering）和 holdout split validation 增强了可信度。

4. **诚实的 limitation 讨论**: 论文对 base-model 限制、instruction tuning 退化、temperature sensitivity、3-class metric inflation 等问题的自我批评到位，没有 overclaim。这种透明性值得肯定。

5. **QLoRA upper bound 实验**: 3-class F1 = 0.905（vs 0.789 XGBoost）证实深度信号在 raw token embeddings 中确实存在，同时也说明 7-feature set 是有损压缩。这个对比有助于定位 handcrafted features 的价值。

6. **完整的 ablation 覆盖**: LOFO, feature group ablation, classifier comparison, finer-grained depth, cross-temperature, cross-domain, human editing robustness, error analysis — 附录全面且有组织。

---

## 信心说明

Confidence: 4/5。我仔细审阅了全部正文（8页）和全部 20+ 个附录，对论文涉及的 AI-generated text detection、effect size 统计方法、ordinal classification 均有领域经验。对 tokenizer-level 的 NLL 计算细节关注较少（confidence 扣分点）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1672 · 2026-05-19T03:27:58.692901+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 150

## Round 150

2 recorded events


### User

_source line 1673 · 2026-05-19T03:28:09.793833+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.0 (Findings)** 评分。核心问题有两个 Must-Fix：(1) gen-0 seed sharing 导致三分类评估不可靠，论文 framing（三分类 depth profiling）与实际可靠评估（仅 binary gen-1 vs gen-2+）之间存在落差；(2) base-model-only 限制在 instruct model 主导的真实场景下严重约束论文的实际意义。六个 Should-Fix 涵盖 tail decay 分类统计不充分、downstream TOST 的 n=3 统计效力不足、baseline 反超问题、多 generator subset 混用、cross-domain 温度混淆、以及 Cohen's d 异方差问题。论文的主要优势在于任务定义新颖、实验控制极其严谨、DDR 分析框架有科学价值、limitations 讨论诚实透明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1674 · 2026-05-19T03:28:16.447807+00:00_

收到 Reviewer 1 审稿意见。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 151

## Round 151

6 recorded events


### User

_source line 1675 · 2026-05-19T03:29:45.020858+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Depth Profiling

## Summary (2-3句)

本文提出"生成深度分类"(generation depth classification)这一新任务，将文本按递归生成深度(gen-0/gen-1/gen-2+)进行分类，而非传统的二元真/合成检测。作者设计了7个手工特征并提出 DDR (Differential Depth Response) 三分法框架，在8个 base 模型上用 LOGO 交叉验证进行评估，binary F1=0.694、3-class F1=0.694。实验充分但方法论新颖性有限（特征工程+XGBoost），且实际应用价值尚未得到充分论证——论文自身实验显示 depth-aware curation 对下游 perplexity 无显著改善。

## Strengths

**S1. 任务定义有价值。** 将 AI 文本检测从二元分类扩展到多类深度分类，这一 framing 是新的且有意义的。它与 model collapse 文献的理论关注和数据溯源的实际需求都有自然联系。

**S2. 实验设计严谨。** 8个生成器、5个模型家族、LOGO 交叉验证、Bonferroni 校正、TOST 等价检验——方法论上几乎无可挑剔。控制了 length confound（§4.1, Appendix B）、seed sharing（Appendix R）、prompt type（Appendix C）等多个混淆变量。

**S3. 分析深度突出。** 20个附录（A-T）系统地覆盖了消融、混淆矩阵、特征分布、跨域迁移、跨温度迁移、扰动鲁棒性、下游效用等多个维度。DDR 的 drifting/intermediate/near-stationary 三分法（§4.2, Figure 1）提供了有用的分析视角。

**S4. 写作质量良好。** 无 AI 写作痕迹（无 em-dash、无 -ing phrase 堆砌、无 discourse marker 滥用）。Abstract 信息密度高，行文简洁直接。引用完整（68条，无孤立/缺失），覆盖检测、collapse、数据质量、stylometry 等相关领域。

**S5. 格式合规。** 正文≤8页（Conclusion 在第8页结束），Limitations 在 Conclusion 之后、References 之前，匿名化完整（"Anonymous ACL submission"），ACL 模板 review 选项。

## Weaknesses

### Must-Fix

**N1 [critical] 实际应用动机薄弱——下游效用实验自我否定核心价值。**
- 具体位置：Appendix L (Downstream Utility), Table 16, 以及 §5 Discussion
- 问题：论文 Introduction（§1）将 depth classification 定位为理解 model collapse 和数据溯源的工具。但 Appendix L 的 TOST 等价检验表明 depth-aware curation 与 random subsampling 在下游 perplexity 上"practically indistinguishable"（Δ=0.046/0.770, p=1.1×10⁻¹）。这意味着**知道文本的生成深度对数据筛选没有实际帮助**。§8 Limitations 也承认 "depth does not, by itself, make it more or less useful for training"。
- 为什么影响接收：如果深度分类对下游任务无可衡量的价值，论文的 motivation 从 "this is useful" 退化为 "this is possible but we don't know why it matters"。审稿人会问："So what?"
- 建议：(a) 找到一个 depth classification 确实改变决策/结果的下游应用场景（如检测 data contamination 中的多代累积漂移，或为 model collapse 研究提供精确的 depth labels）；(b) 或者诚实地重新定位论文为 analytical/empirical study，降低 utility claim。

**N2 [critical] 仅限 base models，严重限制实际适用性。**
- 具体位置：§3.2, §8 Limitations（第8-9页）
- 问题：所有实验仅在 pretrained（base）模型上进行。但现实中绝大多数 LLM 生成文本来自 instruction-tuned 或 RLHF 模型。§4.2 和 Contribution 4 提到 "instruction tuning reverses feature drift direction"，但这是从 OLMo-Instruct 一个模型的简单观察（§8, 第8页），而非系统实验。
- 为什么影响接收：如果方法在 instruction-tuned 模型上不工作（或表现完全不同），论文的实际价值大打折扣。审稿人期望至少有一个系统的 instruction-tuned 实验组。
- 建议：增加至少 3-4 个 instruction-tuned 模型的实验（如 Llama-3-Instruct, Qwen-Chat, Mistral-Instruct），即使结果表明方法需要适配，这也是重要的 finding。

**N3 [critical] DDR "框架"的理论贡献被过度包装。**
- 具体位置：§4.2, Abstract ("We identify a differential depth response (DDR)")
- 问题：DDR 本质上是将7个特征按其与 depth 的 Spearman 相关系数分为三组（|ρ|>0.60 = drifting, 0.10<|ρ|<0.55 = intermediate, |ρ|<0.10 = near-stationary）。这是描述性分析（descriptive categorization），不是一个"框架"（framework）。将相关性分组冠以 "Differential Depth Response" 的名称并作为核心贡献之一（Contribution 2），有过度包装之嫌。
- 为什么影响接收：审稿人会质疑这是否构成方法论贡献。将特征按相关性排序是标准 EDA，不需要一个专有名词。
- 建议：将 DDR 降级为分析发现而非框架贡献；或者为 DDR 提供理论基础（如为什么恰好是三组？是否有信息论解释？）。

### Should-Fix

**W1 [warning] 参考模型依赖（Pythia-410M）是未充分讨论的系统性混淆。**
- 具体位置：§3.3 Feature Extraction, §7（第7页 "reference model calibration is critical"）
- 问题：所有 reference-model features（entropy mean/std/min/max, tail decay）依赖于 Pythia-410M 作为参考模型。§7 承认 "reference model calibration is critical for cross-domain deployment"，但没有系统实验评估更换参考模型（如用 Qwen 或 Llama 作为参考）的影响。当生成器与参考模型属于同一家族（如 Pythia-2.8B 作为生成器）时，观测到的 depth signal 可能部分来自模型家族相似性而非真正的 depth effect。
- 建议：(a) 增加 1-2 个备选参考模型的消融；(b) 分析 Pythia 家族生成器的 LOGO 性能是否系统性高于其他家族（从 Table 1 的数据看，Pythia-2.8B 确实是最高的 0.738）。

**W2 [warning] 共享 seed passage 引入的统计依赖未充分处理。**
- 具体位置：§3.2, Appendix R (Independent-Seed Control)
- 问题：所有8个生成器共享同一组 ~1,000 个 Wikipedia seed passages。这意味着不同生成器的输出在 seed 维度上是 paired 的，违反了 independence 假设。Appendix R 用独立 seed 进行了对照实验（binary F1=0.693 vs 共享 seed 的 0.694），差距确实很小。但这个对照只用了6个生成器的 subset，且样本量（500 seeds × 5 depths = 2500 per generator）远小于主实验。
- 建议：在主文中讨论 seed-sharing 的统计影响，并解释为什么 Appendix R 的小规模对照足以排除此混淆。

**W3 [warning] 3-class 分组（gen-0 / gen-1 / gen-2+）的决策缺乏充分论证。**
- 具体位置：§3.1 Task Formulation
- 问题：§3.1 将 depth 2-4 合并为 "gen-2+" 类，理由是 "monotonic feature convergence that compresses inter-class margins beyond depth 2"。但这个决策在 Appendix D（Finer-Grained Depth Classification）的5-class 实验中被详细讨论，5-class F1 仅从 0.694 下降到约 0.50。论文没有清楚解释为什么不选择 4-class 或其他粒度。
- 建议：在 §3.1 或 §4 中加入简要的 granularity 消融（如 2/3/4/5-class 的 F1 曲线），使 3-class 选择有数据支撑。

**W4 [warning] Baseline 对比不完整。**
- 具体位置：§4.3, Table 2
- 问题：Table 2 的 baselines 是4个单特征检测分数（FastDetectGPT, Binoculars, AvgLogProb, FaithfulGPT）+ LD-Score，都不是为 depth classification 设计的。缺少：(a) 简单 n-gram 统计特征 baseline；(b) 除 QLoRA（Appendix E）外的其他 neural classifier（如 RoBERTa finetune）作为上界参考；(c) 直接使用 perplexity 作为 depth classifier 的 baseline。
- 建议：增加至少一个 n-gram/简单统计 baseline 和一个预训练 encoder classifier baseline。

### Minor

**M1 [minor]** §1 Introduction 第一段提到 "model collapse dynamics" 和 "data provenance"，但这两个动机在后文（特别是 §5 Discussion）并未得到均等发展。Discussion 主要聚焦于 DDR 的描述性框架特征，对 model collapse 和 data provenance 的连接偏弱。

**M2 [minor]** Table 1 caption 说 "Binary F1 may carry upward bias from gen-0 seed sharing across generators"，但 Appendix R 已经控制了这个问题。Caption 和正文对这一 limitation 的措辞不一致。

**M3 [minor]** Figure 1（第6页）的 strip plot x 轴标签（hapas ratio, TTR 等）字体偏小，打印后可能低于 7pt。

**M4 [minor]** §2.3 "Vocabulary Diversity and Stylometry" 小节引用密度偏低（4条引用），相比 §2.1 和 §2.2 明显稀疏。可补充 lexical diversity 方法的更多引用（如 MTLD、vocd-D 等已在 §3.3 使用但未在 Related Work 中讨论的工具）。

**M5 [minor]** Appendix T (Illustrative Examples) 中 Table 24-25 展示了生成链示例及对应特征值，但只有1条链。增加 2-3 条不同生成器的链会更有说服力。

## Questions

**Q1.** Contribution 4 称 "Depth composition does not determine downstream training utility"——这是否意味着 depth classification 的主要应用场景不是数据筛选？如果是，作者认为最有价值的应用场景是什么？请给出具体用例。

**Q2.** DDR 的三分法（drifting/intermediate/near-stationary）阈值（|ρ|=0.60, 0.10）是如何确定的？是否存在 sensitivity analysis？如果阈值改为 0.50 和 0.15，分组是否改变？

**Q3.** 为什么不在 Related Work 中讨论 iterative self-training / self-play 文献（如 Constitutional AI、SPIN 等）？这些方法也涉及多代文本生成，且其输出也可能出现在训练数据中。

**Q4.** Pythia-410M 作为参考模型时，Pythia 家族生成器（Pythia-1B, Pythia-2.8B）是否因为架构相似性而获得系统性优势？Table 1 显示 Pythia-2.8B 的 binary F1 最高（0.738），这是否支持这一假设？

**Q5.** 论文提到 instruction tuning "reverses feature drift direction"（§4.2, §8）。这个观察基于多少个 instruction-tuned 模型？如果只有 OLMo-Instruct 一个，这个 claim 的可靠性如何？

## Missing References

1. **Self-training/self-play 文献**：如 Yuan et al., 2024 "Self-Rewarding Language Models"; Chen et al., 2024 "Self-Play Fine-Tuning" (SPIN)——这些涉及多代生成且与 depth profiling 直接相关。
2. **Data attribution 方法**：如 Park et al., 2023 "TRAK: Attributing Model Behavior at Scale"——与数据溯源动机直接相关。
3. **更多 lexical diversity 方法论文**：MTLD (McCarthy & Jarvis, 2010) 和 MATTR (Covington & McFall, 2010) 已在特征设计中使用但未在 §2.3 Related Work 中讨论。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验设计严谨、统计检验充分，但核心 claim（DDR 作为"框架"）的支撑偏弱；下游效用实验否定了实际应用动机；参考模型混淆未系统评估 |
| Excitement | 2/5 | 任务定义有新意，但方法论（特征工程+XGBoost）缺乏 methodological novelty；仅限 base models 限制了实际影响力；未能论证 depth classification 的 killer application |
| Reproducibility | 4/5 | 代码/数据承诺公开，实验细节充分（模型、超参数、评估协议均有明确说明），但参考模型选择的影响未知 |
| Overall Assessment | 3.0 | Findings 水平 |
| Confidence | 4/5 | 熟悉 AI 文本检测和 model collapse 文献，仔细阅读了全文和全部附录 |

## Overall Assessment

**Overall**: 3.0 (Findings)
**一句话总结**: 任务定义有价值且实验充分，但方法论新颖性有限（标准特征+标准分类器），且论文自身实验否定了最直觉的应用场景（数据筛选），使得 "为什么要做 depth classification" 这个问题缺乏令人信服的回答。

论文最大的优势是实验的系统性和分析深度（20个附录覆盖了几乎所有潜在质疑）。最大的弱点是缺乏一个 compelling 的应用场景来证明 depth classification 的价值超越 binary detection。如果作者能 (1) 在 instruction-tuned 模型上验证方法，(2) 找到一个 depth classification 确实改变决策的应用场景，(3) 适当降低 DDR "框架"的包装力度，本文有潜力达到 3.5 (Borderline Conference) 水平。

**Confidence**: 4/5 — 熟悉相关文献，全文细读。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1676 · 2026-05-19T03:30:32.429059+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Summary\n本文提出\"生成深度分类\"(generation depth classification)这一新任务，将文本按递归生成深度(gen-0/gen-1/gen-2+)进行分类，而非传统的二元真/合成检测。作者设计了7个手工特征并提出 DDR (Differential Depth Response) 三分法框架，在8个 base 模型上用 LOGO 交叉验证进行评估，binary F1=0.694、3-class F1=0.694。实验充分但方法论新颖性有限（特征工程+XGBoost），且实际应用价值尚未得到充分论证——论文自身实验显示 depth-aware curation 对下游 perplexity 无显著改善。\n\n## Must-Fix\n\n**N1 [critical] 实际应用动机薄弱——下游效用实验自我否定核心价值。**\n- 论文 Introduction（§1）将 depth classification 定位为理解 model collapse 和数据溯源的工具。但 Appendix L 的 TOST 等价检验表明 depth-aware curation 与 random subsampling 在下游 perplexity 上\"practically indistinguishable\"。这意味着知道文本的生成深度对数据筛选没有实际帮助。如果深度分类对下游任务无可衡量的价值，论文的 motivation 从 \"this is useful\" 退化为 \"this is possible but we don't know why it matters\"。\n\n**N2 [critical] 仅限 base models，严重限制实际适用性。**\n- 所有实验仅在 pretrained（base）模型上进行。现实中绝大多数 LLM 生成文本来自 instruction-tuned 或 RLHF 模型。§4.2 和 Contribution 4 提到 \"instruction tuning reverses feature drift direction\"，但这是从 OLMo-Instruct 一个模型的简单观察，而非系统实验。\n\n**N3 [critical] DDR \"框架\"的理论贡献被过度包装。**\n- DDR 本质上是将7个特征按其与 depth 的 Spearman 相关系数分为三组。这是描述性分析（descriptive categorization），不是一个\"框架\"。将相关性分组冠以 \"Differential Depth Response\" 的名称并作为核心贡献之一，有过度包装之嫌。\n\n## Should-Fix\n\n**W1 [warning] 参考模型依赖（Pythia-410M）是未充分讨论的系统性混淆。**\n- 所有 reference-model features 依赖于 Pythia-410M。当生成器与参考模型属于同一家族时，depth signal 可能部分来自模型家族相似性。Table 1 显示 Pythia-2.8B 的 binary F1 最高（0.738）。\n\n**W2 [warning] 共享 seed passage 引入的统计依赖未充分处理。**\n- 所有8个生成器共享同一组 ~1,000 个 Wikipedia seed passages，违反 independence 假设。Appendix R 对照只用了6个生成器的 subset。\n\n**W3 [warning] 3-class 分组（gen-0 / gen-1 / gen-2+）的决策缺乏充分论证。**\n- §3.1 将 depth 2-4 合并为 \"gen-2+\"，但没有清楚解释为什么不选择 4-class 或其他粒度。\n\n**W4 [warning] Baseline 对比不完整。**\n- 缺少 n-gram 统计特征 baseline、预训练 encoder classifier baseline（如 RoBERTa finetune）、直接使用 perplexity 作为 depth classifier 的 baseline。\n\n## Minor\n- M1: Introduction 的 model collapse 和 data provenance 双动机在 Discussion 中未均等发展\n- M2: Table 1 caption 与 Appendix R 对 seed sharing 的措辞不一致\n- M3: Figure 1 x轴标签字体偏小\n- M4: §2.3 引用密度偏低\n- M5: Appendix T 仅1条链示例\n\n## Questions\n- Q1: 如果 depth classification 对数据筛选无帮助，最有价值的应用场景是什么？\n- Q2: DDR 三分法阈值（|ρ|=0.60, 0.10）如何确定？sensitivity analysis？\n- Q3: 为什么不讨论 iterative self-training / self-play 文献？\n- Q4: Pythia 家族生成器是否因架构相似性获得系统性优势？\n- Q5: instruction tuning \"reverses feature drift direction\" 基于多少个模型？\n\n## Missing References\n- Self-training/self-play: Yuan et al. 2024 \"Self-Rewarding LMs\"; Chen et al. 2024 \"SPIN\"\n- Data attribution: Park et al. 2023 \"TRAK\"\n- Lexical diversity: MTLD (McCarthy & Jarvis 2010), MATTR (Covington & McFall 2010)\n\n## Overall: 3.0 (Findings), Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## Summary\n本文提出\"生成深度分类\"(generation depth classification)这一新任务，将文本按递归生成深度(gen-0/gen-1/gen-2+)进行分类，而非传统的二元真/合成检测。作者设计了7个手工特征并提出 DDR (Differential Depth Response) 三分法框架，在8个 base 模型上用 LOGO 交叉验证进行评估，binary F1=0.694、3-class F1=0.694。实验充分但方法论新颖性有限（特征工程+XGBoost），且实际应用价值尚未得到充分论证——论文自身实验显示 depth-aware curation 对下游 perplexity 无显著改善。\n\n## Must-Fix\n\n**N1 [critical] 实际应用动机薄弱——下游效用实验自我否定核心价值。**\n- 论文 Introduction（§1）将 depth classification 定位为理解 model collapse 和数据溯源的工具。但 Appendix L 的 TOST 等价检验表明 depth-aware curation 与 random subsampling 在下游 perplexity 上\"practically indistinguishable\"。这意味着知道文本的生成深度对数据筛选没有实际帮助。如果深度分类对下游任务无可衡量的价值，论文的 motivation 从 \"this is useful\" 退化为 \"this is possible but we don't know why it matters\"。\n\n**N2 [critical] 仅限 base models，严重限制实际适用性。**\n- 所有实验仅在 pretrained（base）模型上进行。现实中绝大多数 LLM 生成文本来自 instruction-tuned 或 RLHF 模型。§4.2 和 Contribution 4 提到 \"instruction tuning reverses feature drift direction\"，但这是从 OLMo-Instruct 一个模型的简单观察，而非系统实验。\n\n**N3 [critical] DDR \"框架\"的理论贡献被过度包装。**\n- DDR 本质上是将7个特征按其与 depth 的 Spearman 相关系数分为三组。这是描述性分析（descriptive categorization），不是一个\"框架\"。将相关性分组冠以 \"Differential Depth Response\" 的名称并作为核心贡献之一，有过度包装之嫌。\n\n## Should-Fix\n\n**W1 [warning] 参考模型依赖（Pythia-410M）是未充分讨论的系统性混淆。**\n- 所有 reference-model features 依赖于 Pythia-410M。当生成器与参考模型属于同一家族时，depth signal 可能部分来自模型家族相似性。Table 1 显示 Pythia-2.8B 的 binary F1 最高（0.738）。\n\n**W2 [warning] 共享 seed passage 引入的统计依赖未充分处理。**\n- 所有8个生成器共享同一组 ~1,000 个 Wikipedia seed passages，违反 independence 假设。Appendix R 对照只用了6个生成器的 subset。\n\n**W3 [warning] 3-class 分组（gen-0 / gen-1 / gen-2+）的决策缺乏充分论证。**\n- §3.1 将 depth 2-4 合并为 \"gen-2+\"，但没有清楚解释为什么不选择 4-class 或其他粒度。\n\n**W4 [warning] Baseline 对比不完整。**\n- 缺少 n-gram 统计特征 baseline、预训练 encoder classifier baseline（如 RoBERTa finetune）、直接使用 perplexity 作为 depth classifier 的 baseline。\n\n## Minor\n- M1: Introduction 的 model collapse 和 data provenance 双动机在 Discussion 中未均等发展\n- M2: Table 1 caption 与 Appendix R 对 seed sharing 的措辞不一致\n- M3: Figure 1 x轴标签字体偏小\n- M4: §2.3 引用密度偏低\n- M5: Appendix T 仅1条链示例\n\n## Questions\n- Q1: 如果 depth classification 对数据筛选无帮助，最有价值的应用场景是什么？\n- Q2: DDR 三分法阈值（|ρ|=0.60, 0.10）如何确定？sensitivity analysis？\n- Q3: 为什么不讨论 iterative self-training / self-play 文献？\n- Q4: Pythia 家族生成器是否因架构相似性获得系统性优势？\n- Q5: instruction tuning \"reverses feature drift direction\" 基于多少个模型？\n\n## Missing References\n- Self-training/self-play: Yuan et al. 2024 \"Self-Rewarding LMs\"; Chen et al. 2024 \"SPIN\"\n- Data attribution: Park et al. 2023 \"TRAK\"\n- Lexical diversity: MTLD (McCarthy & Jarvis 2010), MATTR (Covington & McFall 2010)\n\n## Overall: 3.0 (Findings), Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-19T03:31:05.893864+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33464
}
```

</details>

---


### Tool call

_source line 1678 · 2026-05-19T03:31:06.094944+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## Summary\n本文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+，并在 8 个 base model（5 个 family，0.6B–8B）上识别出 DDR 三分结构：3 个 drifting 特征、1 个 intermediate 特征、3 个 near-stationary 特征。7 特征集成在 LOGO 评估下获得 leak-free binary F1 = 0.694。\n\n## Must-Fix\n\n**N1 [critical] Gen-0 seed sharing 使核心三分类评估失效。**\n- gen-0 seeds 在所有 generators 间共享，LOGO 中 gen-0 文本训练/测试完全相同。Confusion matrix 显示 gen-0 recall=99.4%。Independent-seed 实验仅 2 generators。论文 framing（三分类 depth profiling）与实际可靠评估（仅 binary）之间存在显著落差。\n\n**N2 [critical] 仅限 base model 的限制对论文 significance 造成根本性约束。**\n- Appendix K 显示 instruct 模型下 entropy mean ρ 翻转（−0.60→+0.48），6/7 特征方向反转，LOGO F1 从 0.763 暴跌至 0.338。DDR 核心结构在 instruct model 下被根本性颠覆。论文多处暗示更广泛适用性，超出实验支撑。\n\n## Should-Fix\n\n**W1 [warning] Tail decay \"near-stationary\" 分类缺乏充分统计支撑。**\n- TOST 仅 4/8 generators 通过，non-passing 的 |d| 范围 0.15–0.22。需放松至 ε=0.25 才达 7/8。\n\n**W2 [warning] Downstream TOST n=3 seeds 统计效力极低。**\n- Cohen's d 值高达 86.0/119.7（artificial inflation），以 n=3 支撑跨 Section 反复引用的结论，统计基础过于薄弱。\n\n**W3 [warning] 4-detector ensemble baseline 反超削弱 DDR 方法论贡献。**\n- 4-det ensemble binary F1=0.708 > 7-feature 0.705。现有检测方法已隐含深度信息，简单组合就能达到或超过 DDR。\n\n**W4 [warning] 多个 generator subset 混用。**\n- 5/6/8-gen subsets，cross-reference 难以直接对比 main results。\n\n**W5 [warning] Cross-domain 实验 t=1.0 超出可靠范围。**\n- 论文自身确认 t≥0.9 退化 9.3-26.0pp，domain 和 temperature 效应混淆。\n\n**W6 [warning] Cohen's d 异方差问题。**\n- Levene tests 拒绝等方差（p<10^-10），但正文仍用 pooled Cohen's d 定义关键阈值。\n\n## Minor\n- M1: \"base (pretrained)\" 重复注释冗余\n- M2: Table 1 脚注关键信息过于不显眼\n- M3: 3 个 drifting features 高度相关（r=0.81-0.86），可能是同一 latent factor\n- M4: Qualitative example 仅 Pythia，退化过于极端\n- M5: Ethics Statement 缺 CO₂ 排放估算\n- M6: Discussion 中 \"gen-1 per-class F1=0.63\" 指代不明\n\n## Questions\n- Q1: 能否在 full 8-gen LOGO 下报告 independent-seed 3-class F1？\n- Q2: 8-gen 设置下 cross-reference spread 是否仍 ≤0.013？\n- Q3: 是否考虑 PCA/factor analysis 验证 drifting group 是否为单一 latent factor？\n- Q4: Cross-prompt transfer 在多 generator 设置下是否稳健？\n- Q5: Qwen3-1.7B t=0.5/0.7 binary F1 完全相同（0.751），CI 缺失原因？\n- Q6: Table 2 pooled vs per-generator macro average 差异从何而来？\n\n## Missing References\n- Bao et al. (2024) \"On the Reliability of AI Text Detectors\"\n- 更多 ordinal regression NLP 文献\n- Guo et al. (2023) \"How Close is ChatGPT to Human Experts?\"\n\n## Overall: 3.0 (Findings), Confidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## Summary\n本文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+，并在 8 个 base model（5 个 family，0.6B–8B）上识别出 DDR 三分结构：3 个 drifting 特征、1 个 intermediate 特征、3 个 near-stationary 特征。7 特征集成在 LOGO 评估下获得 leak-free binary F1 = 0.694。\n\n## Must-Fix\n\n**N1 [critical] Gen-0 seed sharing 使核心三分类评估失效。**\n- gen-0 seeds 在所有 generators 间共享，LOGO 中 gen-0 文本训练/测试完全相同。Confusion matrix 显示 gen-0 recall=99.4%。Independent-seed 实验仅 2 generators。论文 framing（三分类 depth profiling）与实际可靠评估（仅 binary）之间存在显著落差。\n\n**N2 [critical] 仅限 base model 的限制对论文 significance 造成根本性约束。**\n- Appendix K 显示 instruct 模型下 entropy mean ρ 翻转（−0.60→+0.48），6/7 特征方向反转，LOGO F1 从 0.763 暴跌至 0.338。DDR 核心结构在 instruct model 下被根本性颠覆。论文多处暗示更广泛适用性，超出实验支撑。\n\n## Should-Fix\n\n**W1 [warning] Tail decay \"near-stationary\" 分类缺乏充分统计支撑。**\n- TOST 仅 4/8 generators 通过，non-passing 的 |d| 范围 0.15–0.22。需放松至 ε=0.25 才达 7/8。\n\n**W2 [warning] Downstream TOST n=3 seeds 统计效力极低。**\n- Cohen's d 值高达 86.0/119.7（artificial inflation），以 n=3 支撑跨 Section 反复引用的结论，统计基础过于薄弱。\n\n**W3 [warning] 4-detector ensemble baseline 反超削弱 DDR 方法论贡献。**\n- 4-det ensemble binary F1=0.708 > 7-feature 0.705。现有检测方法已隐含深度信息，简单组合就能达到或超过 DDR。\n\n**W4 [warning] 多个 generator subset 混用。**\n- 5/6/8-gen subsets，cross-reference 难以直接对比 main results。\n\n**W5 [warning] Cross-domain 实验 t=1.0 超出可靠范围。**\n- 论文自身确认 t≥0.9 退化 9.3-26.0pp，domain 和 temperature 效应混淆。\n\n**W6 [warning] Cohen's d 异方差问题。**\n- Levene tests 拒绝等方差（p<10^-10），但正文仍用 pooled Cohen's d 定义关键阈值。\n\n## Minor\n- M1: \"base (pretrained)\" 重复注释冗余\n- M2: Table 1 脚注关键信息过于不显眼\n- M3: 3 个 drifting features 高度相关（r=0.81-0.86），可能是同一 latent factor\n- M4: Qualitative example 仅 Pythia，退化过于极端\n- M5: Ethics Statement 缺 CO₂ 排放估算\n- M6: Discussion 中 \"gen-1 per-class F1=0.63\" 指代不明\n\n## Questions\n- Q1: 能否在 full 8-gen LOGO 下报告 independent-seed 3-class F1？\n- Q2: 8-gen 设置下 cross-reference spread 是否仍 ≤0.013？\n- Q3: 是否考虑 PCA/factor analysis 验证 drifting group 是否为单一 latent factor？\n- Q4: Cross-prompt transfer 在多 generator 设置下是否稳健？\n- Q5: Qwen3-1.7B t=0.5/0.7 binary F1 完全相同（0.751），CI 缺失原因？\n- Q6: Table 2 pooled vs per-generator macro average 差异从何而来？\n\n## Missing References\n- Bao et al. (2024) \"On the Reliability of AI Text Detectors\"\n- 更多 ordinal regression NLP 文献\n- Guo et al. (2023) \"How Close is ChatGPT to Human Experts?\"\n\n## Overall: 3.0 (Findings), Confidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-19T03:31:07.803749+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1708
}
```

</details>

---


### Assistant

_source line 1680 · 2026-05-19T03:31:11.054660+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 152

## Round 152

2 recorded events


### User

_source line 1681 · 2026-05-19T03:31:13.890675+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**：Overall 3.0 (Findings)。

3个 Must-Fix 问题：
1. **下游效用实验自我否定动机**——depth-aware curation 与 random subsampling 无差异，"so what" 未回答
2. **仅限 base models**——instruction-tuned 模型完全缺失，实际适用性存疑
3. **DDR "框架"过度包装**——实质是按相关系数对特征分组的描述性分析，不构成方法论贡献

4个 Should-Fix：参考模型混淆、seed sharing 统计依赖、3-class 粒度选择缺论证、baseline 对比不完整。

优点：任务定义新颖、实验极其充分（20个附录）、写作质量好、格式合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1682 · 2026-05-19T03:31:18.083969+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 153

## Round 153

2 recorded events


### User

_source line 1683 · 2026-05-19T03:32:44.919084+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 的逐条回应

---

## Must-Fix

**[REBUT] R2-N1: "下游效用实验自我否定核心价值"**

R2 的前提有误。论文并未将 depth classification 定位为数据筛选工具。§5 Discussion 明确写道："DDR characterizes distributional structure under recursive generation; depth profiling identifies this structure rather than prescribing data-selection actions." Contribution 4（§1）的原文是 "Depth composition does not determine downstream training utility at fixed sample count, consistent with depth profiling serving a **diagnostic** rather than prescriptive role"。下游实验的 null result 不是自我否定，而是论文故意设计来论证 DDR 是分析框架而非工程工具的 supporting evidence。

论文的实际动机在 Introduction 第一段已交代清楚：理解 "how language models transform distributions under iterative conditioning"，以及与 model collapse dynamics 和 data provenance 的联系（§1, line 4–5）。这是一个 scientific characterization 的贡献，类似于 model collapse 文献（Shumailov et al., 2024）记录现象而非提供直接工程方案。

**但我同意 R2 的一个隐含关切**：如果 DDR 仅是 diagnostic，其实际影响力确实受限。论文需要更清楚地阐述：knowing the DDR structure 能 inform 什么后续研究或工程决策。当前 Introduction 的 framing 在 "理解 recursive dynamics" 和 "data provenance" 之间摇摆，如果 provenance 方向的价值（Appendix M 的 downstream 结果）被实验否定了，论文应更坚定地 commit to "scientific understanding" 方向。

---

**[AGREE] R2-N2: "仅限 base models，严重限制适用性"**

同意。我在自己的审稿意见中将此列为 N2 (critical)。补充一点 R2 遗漏的细节：Appendix K (Table 3) 实际上测试了 3 个模型家族（OLMo, Qwen, Llama），而非 R2 所述的 "OLMo-Instruct 一个模型"。但即便 3 个家族，结果仍然一致地灾难性：entropy mean ρ 全部翻转符号（OLMo: −0.64→+0.48, Qwen: −0.60→+0.48, Llama: −0.63→+0.23），6/7 特征方向反转（OLMo, Qwen），LOGO F1 暴跌（OLMo: 0.763→0.338）。这证实了 DDR 的核心结构在 instruct model 下被颠覆——不是 "需要微调" 的问题，而是特征的物理含义改变了。

---

**[REBUT] R2-N3: "DDR 框架被过度包装"**

R2 将 DDR 简化为 "按 Spearman 相关系数分组" 是不准确的。DDR partition 的建立涉及以下多层验证（全部可在 §4.2 和 Appendix R/S 中找到）：

1. **Data-driven clustering**: k-means 在标准化 (|ρ|, d) 空间中确认 k=2 为最强结构（silhouette=0.632），k=4 时 entropy std 自动分离（Appendix S, Table 5）
2. **多指标交叉验证**: pooled Cohen's d, Glass's Δ（异方差校正）, Cliff's δ（非参数）, Levene test, CV shift, KS statistics——六种指标一致收敛（Appendix S, Table 8）
3. **Per-generator TOST 等效性检验**: 逐 generator 验证 near-stationary 分类不是 pooling artifact（Appendix R, Table 5）
4. **TOST bound sensitivity**: ε ∈ {0.15, 0.20, 0.25} 三个阈值下 partition 稳定（Appendix S, Table 6）
5. **Holdout generator split**: 两组 4/4 split，selection 和 validation 子集得到相同分区（Appendix S, Table 7, Figure 5）
6. **Heteroscedasticity robustness**: drifting/near-stationary gap ≥ 9.5× under Glass's Δ（Appendix S, Table 8）

将经过 6 层独立验证的分区结构称为 "描述性分析" 是低估了方法论贡献。DDR 不仅是 "分组"，而是一个关于 recursive generation 中 location 和 shape 如何差异性响应的 empirical decomposition，这在 model collapse 文献中没有类似分析。

当然，R2 指出 "框架" 这一措辞可能过强有一定道理。论文可以更清楚地区分 DDR 作为 "empirical finding"（被充分支撑）和作为 "theoretical framework"（缺少形式化证明）之间的差异。

---

## Should-Fix

**[REBUT] R2-W1: "参考模型依赖是未充分讨论的系统性混淆"**

这个问题在论文中已有充分回应。§4.2 "Cross-family reference models" 段明确报告：使用 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model，LOGO F1 spread ≤ 0.013（Table 4, Appendix U）。三个 reference 的 entropy drift 方向一致（均为负），magnitude 差异反映 capacity 而非 family affinity。

R2 称 "Pythia-2.8B binary F1 最高（0.738）" 暗示 family affinity。但 Table 1 的完整排序为：Pythia-2.8B (0.724) > Pythia-1B (0.718) > Qwen3-1.7B (0.709) > Llama-3.2-3B (0.697) > OLMo-2-1B (0.695) > Qwen3-8B (0.692) > Qwen3-0.6B (0.691) > Mistral-7B (0.633)。Pythia 排名靠前，但 Qwen3-1.7B（非同家族）排第三，且高于同家族的另一个小参数 Qwen3-0.6B。更重要的是，论文在 §4.1 中提出了替代解释："The scale effect...larger models show degradation...partly reflecting same-family affinity with the Pythia-410M reference model (cross-reference spread ≤0.013)"，即 scale 效应和 family affinity 都有贡献，且后者的影响通过 cross-reference 实验被量化为 ≤0.013。

---

**[AGREE] R2-W2: "共享 seed passage 引入统计依赖"**

同意这是一个重要问题，我在自己的 N1 中将其列为 critical。但需要指出论文已做了两层控制：(1) seed-level demeaning (F1=0.701, §4.1)；(2) independent-seed 实验 (F1=0.680, Appendix T)。两者与 shared-seed LOGO (0.694) 的差距均在 CI 内。R2 称 "Appendix R 只用了6个生成器" 可能是指 confusion matrix（Appendix G，确实是 6-gen），但 independent-seed 控制（Appendix T）使用的是 Pythia-2.8B 和 OLMo-2-1B（2 个 generator），这确实不够。我在 Q1 中已要求作者在 full 8-gen 设置下补充 independent-seed 实验。

---

**[REBUT] R2-W3: "3-class 分组缺乏充分论证"**

论文在 §3.1 给出了直接理由："Depths beyond 2 are merged into a single 2+ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2." 更重要的是，Appendix D（Table 2, 3）提供了完整的 5-class 实验：LOGO macro F1 ≈ 0.50，gen-2 和 gen-3 的 F1 分别仅为 0.268 和 0.259，相邻 depth（gen-2↔gen-3, gen-3↔gen-4）贡献了绝大多数错误。四种替代 classifier（HistGradientBoosting, Random Forest, Logistic Regression, Frank-Hall ordinal）均产生相同的 5-class 天花板，排除了 classifier capacity 的因素。这是经过实验验证的分组决策，不是 ad hoc 选择。

---

**[AGREE with nuance] R2-W4: "Baseline 对比不完整"**

部分同意。论文确实缺少以下 baselines：
- **N-gram 统计特征**：合理的 baseline，应该测试（如 character n-gram profile）
- **Pretrained encoder classifier**（如 RoBERTa finetune）：但需注意论文已有 QLoRA end-to-end classifier（Appendix E, 3-class F1=0.905），可视为 neural classifier 的上界

但 R2 提到的 "直接使用 perplexity 作为 depth classifier" 实际上已有：Table 2 中的 Avg-LogProb 就是 reference-model perplexity（binary F1=0.673），FastDetectGPT 也是 perplexity-derived score。这两个 baseline 已包含在对比中。

---

## Minor

**[AGREE] R2-M1**: Introduction 的 model collapse 和 data provenance 双动机确实在 Discussion 中发展不均衡。Provenance 方向在 downstream 实验后基本被放弃，但 Introduction 中仍保留了 provenance 动机。

**[AGREE] R2-M2**: Table 1 caption 与 seed sharing 相关措辞应统一。

**[AGREE] R2-M3**: Figure 1 x轴标签字体偏小。

**[REBUT] R2-M4**: "§2.3 引用密度偏低" 不准确。§2.3 (Vocabulary Diversity and Stylometry) 仅 5 行文本，但引用了 8 篇文献（Stamatatos, Koppel, Neal, McCarthy/MTLD, Covington/MATTR, Uchendu, Holtzman/nucleus sampling, writing_diversity/curious_decline），密度实际上很高。

**[AGREE] R2-M5**: Appendix X 仅有 Pythia-2.8B 的 1 条链示例，补充其他模型的定性示例是合理建议。

---

## Questions

**R2-Q1**: "如果 depth classification 对数据筛选无帮助，最有价值的应用场景是什么？"
→ 合理问题。论文 §5 提到 "corpus-level flagging"（gen-1 per-class F1=0.63）和 model collapse dynamics 理解。但我认为作者需要更具体地阐述：DDR 的 location/shape decomposition 对 model collapse 研究的具体启示是什么？

**R2-Q2**: "DDR 三分法阈值如何确定？"
→ 论文实际上有 sensitivity analysis。§4.2 写道 "shifting thresholds by ±0.10 does not alter grouping"。Appendix S 的 TOST bound sensitivity（Table 6）和 holdout split validation（Table 7）进一步确认 partition 对阈值选择的稳定性。R2 可能遗漏了这些分析。

**R2-Q3**: "为什么不讨论 iterative self-training / self-play 文献？"
→ 合理建议。Self-training/self-play 也涉及 iterative generation，但属于 training-loop setting（模型权重更新），与论文的 inference-chain setting（固定模型参数）有本质区别。§2.2 第一段已明确区分 "training-loop drift" 和 "inference-chain drift"。但简要提及 self-training 文献作为对比仍有价值。

**R2-Q4**: "Pythia 家族是否因架构相似性获得系统性优势？"
→ 见 W1 回应。Cross-reference 实验（Table 4）已回答：换用 OLMo 或 Qwen 作为 reference，spread ≤ 0.013。

**R2-Q5**: "instruction tuning reversal 基于多少个模型？"
→ R2 称 "一个模型"，实际是 3 个模型家族（OLMo, Qwen, Llama），见 Appendix K Table 3。R2 的事实错误。

---

## Missing References

**[AGREE]** Self-training 文献（Yuan et al. 2024, Chen et al. 2024 SPIN）可在 §2.2 简要提及作为 training-loop iterative generation 的一种。

**[REBUT]** TRAK (Park et al. 2023) 是 data attribution（追踪训练样本对预测的影响），与 generation depth provenance 是完全不同的问题。引用价值有限。

**[REBUT]** MTLD 和 MATTR 实际上已被引用。§2.3 原文："more sophisticated alternatives exist (MTLD, HD-D (McCarthy and Jarvis, 2010); MATTR (Covington and McFall, 2010))"。R2 遗漏了论文中已有的引用。

---

## 总结

R2 的 N1 和 N3 存在对论文 framing 的误读：论文明确将 DDR 定位为 diagnostic framework 而非 engineering tool，下游 null result 是 supporting evidence 而非 self-negation；DDR 的建立经过多层验证，不是简单的相关系数分组。N2（base-model 限制）我完全同意且在自己的审稿中同样标记为 critical。W3（3-class 分组）已有 5-class 实验验证。W1（reference model）已有 cross-reference 实验回答。W4（baseline 不完整）部分同意（缺 n-gram baseline），但 R2 遗漏了论文已有的 Avg-LogProb 和 QLoRA 实验。R2 对 instruct model 实验数量和 MTLD/MATTR 引用的事实判断有误。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1684 · 2026-05-19T03:32:49.247951+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 1685 · 2026-05-19T03:32:51.994308+00:00_

[Reviewer 1 审稿结果]:
已提交交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1686 · 2026-05-19T03:32:56.035937+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 155

## Round 155

6 recorded events


### User

_source line 1687 · 2026-05-19T03:35:28.384145+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的交叉回应

---

## Must-Fix

**[AGREE] R1-N1: Gen-0 seed sharing 使三分类评估存在 leakage 风险。**

R1 的核心洞察正确：LOGO 中 held-out generator 的 gen-0 文本与训练集 gen-0 完全相同（同一批 Wikipedia passages），构成 data leakage。Confusion matrix（Figure 5b, p.22）显示 gen-0 recall=99.4%，远高于 gen-1 的 75.0% 和 gen-2+ 的 73.7%，这个不对称性与 leakage 假设一致。

Appendix R（p.28）的独立 seed 对照实验确实缓解了这一问题（binary F1: 0.693 vs. 0.694，差异 <0.001），但有两个重要局限：(1) 仅用了 Pythia-2.8B 和 OLMo-2-1B 两个生成器；(2) 未报告 3-class F1。这正是 R1 Q1 所要求的。

**补充 R1 分析**：不过，我认为此问题的严重程度略低于 R1 的判断。3-class macro F1 对三个类别等权平均，gen-0 recall 从 99.4% 降至（假设无 leakage 下的）~90% 仅导致 macro F1 下降 ~3pp（从 0.694 → ~0.66）。真正的 classification 挑战在 gen-1 vs gen-2+ 边界（recall 分别为 75.0% 和 73.7%），这部分不受 gen-0 seed sharing 影响。因此这更接近 should-fix 而非 critical，但作者确实需要补充 full 8-gen independent-seed 3-class F1。

---

**[AGREE] R1-N2: 仅限 base model 对论文 significance 构成根本性约束。**

完全同意。这也是我的 N2。Appendix K（p.16, Table 10）的数据具有破坏性：OLMo-Instruct LOGO F1 从 base 的 0.763 暴跌至 0.338，entropy mean ρ 从 −0.60 翻转至 +0.48，6/7 特征方向反转。这意味着 DDR 的 drifting/intermediate/near-stationary 三分结构在 instruct 模型下可能完全失效。

§8 Limitations（p.8）承认 "instruction tuning substantially weakens the signal across all three tested families"，但论文多处措辞（如 §1 "how many recursive generation steps a text has undergone"、§6 Conclusion "classifying text by generation depth"）暗示了超出 base-model 范围的一般性。作者应当：(a) 在 title/abstract 中明确限定 "base LLM" 范围；(b) 至少在 3-4 个 instruct 模型上报告系统实验结果（即使结果为负面）。

---

## Should-Fix

**[AGREE] R1-W1: Tail decay "near-stationary" 分类缺乏充分统计支撑。**

§4.2（p.6）明确承认 tail decay 的 TOST 仅 4/8 generators 通过。R1 指出需将 ε 放松至 0.25 才达 7/8，这进一步削弱了 "near-stationary" 标签。从 §4.2 的数据看，tail decay 的 |d| 范围 0.15–0.22 已接近论文自定义的 intermediate 区间（d=0.16 在 §4.2 被标记为 "making it the sole intermediate feature"）。

建议将 tail decay 从 "near-stationary" 重新归类为 "intermediate"，或提供更严格的 per-generator 证据。这也会影响 DDR 三分法的对称性（从 3/1/3 变为 3/2/2），但这是更诚实的分类。

---

**[AGREE] R1-W2: Downstream TOST n=3 统计效力极低。**

同意。n=3 下 Cohen's d=86.0/119.7 显然是 artificial inflation（pooled SD 极小导致 d 值爆炸）。论文在 p.20 承认 "The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences"，但仍在 §5 Discussion（p.7-8）和 Contribution 4 中将此结论作为核心贡献引用。

这与我的 N1 从不同角度指向同一问题：downstream utility 实验既统计效力不足（R1 的 W2），结果本身又否定了 depth classification 的实际价值（我的 N1）。两者叠加使 Contribution 4 ("Depth composition does not determine downstream training utility") 成为全文最薄弱的 claim。

---

**[REBUT] R1-W3: 4-detector ensemble baseline 反超的严重性被夸大。**

R1 的数据引用有偏差。从 Table 2（p.7）看：
- Binary F1: 4-det ensemble = 0.706, 7-feature = 0.705（Δ=0.001，在 noise 范围内）
- 3-class F1: 4-det ensemble = 0.785, 7-feature = 0.714（Δ=0.071，确实显著）

但 §4.3 已明确声明定位："To contextualize depth discrimination ability rather than claim competitive advantage over detection-optimized methods." 论文未声称 7-feature 方法在性能上优于现有检测器，而是强调其可解释性优势——DDR 框架提供了 feature-level decomposition（哪些信号在 drift、哪些 stationary），而 detection scores 是黑盒。

**我部分同意 R1 的隐含结论**：existing detection scores 也能隐含地编码 depth 信息，这确实削弱了 DDR 的 unique methodological contribution。但 R1 将 binary F1 差异 0.001 称为"反超"是不准确的。实际上 7-feature 和 4-det ensemble 在 binary 上 performance-equivalent，而 4-det 在 3-class 上更优。作者应在 §4.3 中更诚实地讨论这一点。

---

**[AGREE] R1-W4: 多个 generator subset 混用造成混乱。**

论文在不同 section/appendix 使用了 5-gen（§3.2, Table 1 footnote 指出原始 6-gen subset）、6-gen（Appendix G/H/I 等）和 8-gen（Table 1 main results）三个 subset，且没有一个统一的对照表说明何时用何 subset 及原因。

Table 1 footnote 指出 "Qwen3-1.7B(0.6B) added later"，但具体哪些实验使用哪个 subset 需要在正文中有清晰的一处说明。这是 presentation 问题，不影响实验有效性，但确实增加了审稿人的认知负担。

---

**[AGREE] R1-W5: Cross-domain 实验 t=1.0 与 main experiment t=0.7 不一致。**

Appendix J（p.18）的 cross-domain 实验使用 t=1.0，而 main experiment（§3.2）使用 t=0.7。Appendix H（p.16, Table 10）显示 t=1.0 vs t=0.7 可导致 F1 差异 ~4-7pp。更关键的是，Appendix J 自身数据显示 "at t=0.7, Academic-domain binary F1 drops to 0.626"（p.18），比 t=1.0 下的 0.739 低了 11.3pp。

这意味着论文报告的 cross-domain robustness（F1>0.73）部分归功于 t=1.0 的高温度而非真正的 domain 迁移能力。在 t=0.7 下 Academic domain 降至 0.626，这实际上削弱了 cross-domain 的 claim。R1 的混淆效应指控成立。

---

**[REBUT] R1-W6: Cohen's d 异方差问题已在论文中被处理。**

§4.2（p.6）明确说明 "This partition is robust under heteroscedasticity-corrected metrics (Glass's Δ, Cliff's δ; Appendix V)"。论文使用 pooled Cohen's d 作为 primary presentation metric（因其更直观），但 DDR 分区在 Glass's Δ 和 Cliff's δ 下保持不变。

R1 的技术观察正确（Levene test 确实拒绝等方差），但结论性 claim 不成立——论文已检验了异方差稳健替代指标并确认结果一致。这是一个 minor presentation issue（应在正文中更显著地提及 Glass's Δ 结果），不是 should-fix。

---

## Minor

**[REBUT] R1-M1: "base (pretrained)" 重复注释**
学术论文中 "base model" 的含义不固定（有些领域指 backbone/foundation model）。"base (pretrained)" 在首次使用时提供明确定义是良好写作实践，符合论文写作规范 §1.3 "首次出现的专有名词必须给出完整定义"。后续使用中仅用 "base" 即可，无需每次重复。

**[AGREE] R1-M2: Table 1 脚注信息过于不显眼。**
Table 1 脚注 "Binary F1 may carry upward bias from gen-0 seed sharing" 涉及核心方法论关切（与 N1 直接相关），不应藏在脚注中。建议提升至正文讨论。

**[AGREE] R1-M3: 3 drifting features 高度相关可能是单一 latent factor。**
Appendix Q（p.27）证实 TTR 和 hapax ratio 的 pairwise correlation r ≈ 0.97，且两者与 entropy mean 的 r ≈ 0.56-0.81。R1 提出的 PCA/factor analysis 建议（Q3）有价值——如果3个 drifting features 确实是一个 latent factor，DDR 的 "3 drifting + 1 intermediate + 3 near-stationary" 结构在维度上被高估了。论文对此有初步讨论（§4.2 "sharing a single latent dimension"），但未做正式验证。

**[AGREE] R1-M4: Qualitative example 仅 Pythia，退化过于极端。**
Appendix T（p.29）的 Table 24 仅展示了一条 Pythia-2.8B 链，且 gen-4 文本退化到近乎无意义的重复。增加来自 Qwen 或 Llama 的链（可能退化更平缓）会提供更有代表性的示例。

**[REBUT] R1-M5: Ethics Statement 缺 CO₂ 排放估算。**
CO₂ 排放估算在 EMNLP/ARR 中非强制要求。论文已报告 compute budget（p.9："4× NVIDIA RTX 5090 GPUs (32GB each), totaling approximately 62 GPU-hours"），这已满足 reproducibility 需求。CO₂ 可在 camera-ready 中补充，不构成审稿问题。

**[AGREE] R1-M6: "gen-1 per-class F1=0.63" 指代不明。**
§5 Discussion 中引用的 0.63 应标注来源（是 Table 1 的哪个指标？是 pooled 还是 per-generator macro？是 binary 还是 3-class per-class？）。缺乏精确引用降低了叙述可信度。

---

## Questions 回应

**Q1: Full 8-gen independent-seed 3-class F1** — [AGREE] 这是对 N1 最直接的回应，应由作者提供。如果 3-class F1 在 independent-seed 下仍接近 0.694，则 N1 的严重性大幅降低。

**Q2: 8-gen cross-reference spread** — [AGREE] Table 22（p.28, Appendix S）报告了 6-gen LOGO 的 cross-reference spread ≤0.013。作者应确认 8-gen 设置下此 spread 是否增大。

**Q3: PCA/factor analysis 验证 drifting group** — [AGREE] 这与 M3 直接相关。TTR/hapax ratio 的 r=0.97（Appendix Q）强烈暗示它们是同一 latent factor 的两个 proxy。正式的 factor analysis 会决定 DDR 的 3-drifting 结构是否成立还是应合并为 1-2 个 factor。

**Q4: Cross-prompt multi-gen 稳健性** — [AGREE] Appendix C（p.14）的 cross-prompt 实验使用 5-gen subset（Pythia-2.8B, continuation only），应扩展到更多 generator 以确认稳健性。

**Q5: Qwen3-1.7B t=0.5/0.7 binary F1 完全相同** — 我在 p.16 Table 10 中确认 Qwen3-1.7B 的两行（t=0.5 和 t=0.7）确实有相同的 binary F1=0.751。虽然可能是数值巧合（bootstrap CI 可能不同但四舍五入后一致），但作者应报告 CI 或至少解释。

**Q6: Table 2 pooled vs per-generator macro average 差异** — [AGREE] Table 2 caption 提到 "slightly higher than per-generator macro average in Table 1"，但没解释差异来源。Pooled evaluation 和 per-generator macro average 在 class imbalance 下可以不同（pooled 对大 generator 加权更多）。作者应明确说明。

---

## Missing References 回应

**Bao et al. (2024)** — 如果该文讨论检测器在不同生成条件下的可靠性，与本文的 cross-generator/cross-domain 分析直接相关。[AGREE] 建议补充。

**Ordinal regression NLP** — [AGREE] 论文在 §3.1 将 depth classification 框架为 "ordinal classification"，但 Related Work（§2）未讨论 ordinal regression 在 NLP 中的应用文献。当前仅在 §7（p.7）提到 CORAL 和 Frank & Hall (2001)。

**Guo et al. (2023) "How Close is ChatGPT to Human Experts?"** — [REBUT] 该文是关于 ChatGPT 在特定任务上的能力评估，与 depth classification 关联性弱。不需要在 Related Work 中讨论。

---

## 总结

R1 的审查质量高，技术分析细致。在 14 个具体 issues 中，我同意 10 个（含 2 个 Must-Fix），反驳 4 个。

**最关键的共识**：
1. Base-model-only limitation（R1-N2 = 我的 N2）是全文最根本的约束
2. Gen-0 seed sharing（R1-N1）需要 independent-seed 3-class F1 来 resolve
3. Downstream utility 的统计基础薄弱（R1-W2 + 我的 N1）

**最关键的分歧**：
1. R1-W3 的 "反超" framing 不准确——binary F1 差异仅 0.001
2. R1-W6 的异方差问题已在论文中被 Glass's Δ/Cliff's δ 检验覆盖
3. R1-M5 的 CO₂ 要求超出 ARR 规范

我维持我的 Overall 3.0 (Findings) 评分不变。R1 的分析强化了我对论文主要弱点的判断（base-model 限制 + 下游 utility 薄弱），但未暴露新的 critical 问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-19T03:37:55.152942+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "\n# Round 23 Review Issues — Fresh review (Round 23)\n# Previous rounds (21-22) issues carried forward with status updates\n\n# ============ CRITICAL (Must-Fix) ============\n\n- id: \"R1-N2\"\n  summary: \"仅限 base model 的限制对论文 significance 造成根本性约束\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"严重性取决于 framing; 科学发现定位使其降为 design scope\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"两位 Reviewer 再次一致标记 critical。Appendix K 3个家族(OLMo/Qwen/Llama)全部显示 DDR 结构颠覆：entropy mean ρ 翻转，6/7 特征方向反转，OLMo LOGO F1 0.763→0.338。论文多处措辞暗示超出 base-model 范围的一般性。\"}\n  action_items:\n    - {round: 21, action: \"Abstract + Contribution 均加 scope limitation\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 22, action: \"No additional change needed — resolved by C2 framing adjustment to scientific characterization\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"Title 已含 'Base LLM'；需检查 Abstract/Intro/Conclusion 中是否仍有超范围表述\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-N1\"\n  summary: \"Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage，论文 framing 与可靠评估之间存在落差\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提 critical，R2 agree 但认为接近 should-fix。gen-0 recall=99.4% vs gen-1 75.0%/gen-2+ 73.7% 不对称性与 leakage 一致。Independent-seed 实验仅 2 generators 不足以验证。需 full 8-gen independent-seed 3-class F1。\"}\n  action_items:\n    - {round: 23, action: \"在 full 8-gen LOGO 设置下进行 independent-seed 实验，报告 3-class F1；或调整论文 framing 以 binary 为核心\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-N2\"\n  summary: \"下游效用实验 n=3 统计效力不足，且结果否定 depth classification 的数据筛选价值\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R2 标记 critical（动机自我否定），R1 标记 warning（统计效力）。n=3 seeds 下 Cohen's d=86.0/119.7 为 artificial inflation。Discussion 和 Contribution 4 仍将此作为核心结论引用。双重问题：统计基础薄弱 + 结果本身削弱论文价值主张。\"}\n  action_items:\n    - {round: 23, action: \"增加 seeds 至 10-20，或将 Contribution 4 降级为 preliminary observation 并在正文引用时加 qualification\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ DIVERGENCE ============\n\n- id: \"R23-D1\"\n  summary: \"DDR '框架' 的理论贡献是否被过度包装\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(rebut),R2(critical)\", note: \"R2 认为 DDR 本质是按相关系数分组的描述性分析。R1 反驳举证 6 层验证（k-means, 多指标交叉, per-gen TOST, sensitivity, holdout, heteroscedasticity robustness）。Director 判断：DDR 验证确实超出简单描述性分析，但 'framework' 措辞可降为 'empirical finding/decomposition'。\"}\n  action_items:\n    - {round: 23, action: \"将 DDR 从 'framework' 调整为 'empirical decomposition/finding'，保留多层验证证据但降低理论贡献的包装力度\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ WARNING (Should-Fix) ============\n\n- id: \"R1-W1\"\n  summary: \"Tail decay 作为 'near-stationary' 特征分类统计支撑不足（TOST 4/8）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 22, reviewers: \"R1,R2\", note: \"建议提升为 Limitations 首条\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提，R2 agree。|d|=0.15-0.22 已接近 intermediate 区间(d=0.16)。建议重新归类为 intermediate 或标记 weakly stationary。\"}\n  action_items:\n    - {round: 23, action: \"考虑将 tail decay 移至 intermediate 组（3/2/2 结构），或在正文充分讨论其边界地位\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W1\"\n  summary: \"多个 generator subset (5/6/8-gen) 混用增加 cross-experiment 比较复杂度\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - {round: 22, reviewers: \"R1,R2\", note: \"Appendix U has subset summary\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"两人均 agree。没有统一对照表说明何时用何 subset。核心 claim 应统一 8-gen LOGO。\"}\n  action_items:\n    - {round: 23, action: \"在正文或附录添加统一的 generator subset 参照表；核心 claim 统一使用 8-gen LOGO\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"Cross-domain 实验 t=1.0 超出可靠范围，domain 和 temperature 效应混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提，R2 agree 并强化。t=0.7 下 Academic domain F1 降至 0.626（vs t=1.0 的 0.739），cross-domain robustness 部分归功于高温度。\"}\n  action_items:\n    - {round: 23, action: \"Cross-domain claim 应基于 t=0.7 结果；Limitations 中更显著讨论此混淆\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W3\"\n  summary: \"Baseline 对比不完整：缺少 n-gram 统计特征 baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"R2首提，R1 部分同意。缺 n-gram 统计特征 baseline。Avg-LogProb 和 QLoRA 已有但 R2 遗漏。RoBERTa finetune 可由 QLoRA 上界替代。\"}\n  action_items:\n    - {round: 23, action: \"增加 character n-gram profile 或类似简单统计 baseline\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"3 个 drifting features 高度相关（r=0.81-0.97），可能是同一 latent factor\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提 minor，R2 agree 并升级。TTR-hapax r=0.97，entropy_mean-TTR r=0.86。需 PCA/factor analysis 验证 DDR 3-drifting 结构是否应合并为 1-2 factors。\"}\n  action_items:\n    - {round: 23, action: \"进行 PCA 或 factor analysis 验证 drifting group 的维度结构\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"Introduction model collapse/provenance 双动机在 Discussion 中发展不均衡\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"Provenance 方向在 downstream 实验后基本被放弃，但 Intro 仍保留此动机。\"}\n  action_items:\n    - {round: 23, action: \"统一 Introduction 和 Discussion 的动机线：坚定 commit 到 scientific characterization 方向\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MINOR / INFO ============\n\n- id: \"R23-M1\"\n  summary: \"Table 1 脚注中 gen-0 seed sharing 信息过于不显眼\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"应提升至 caption 主体或正文讨论\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"Discussion 中 'gen-1 per-class F1=0.63' 指代不明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"应标注来源：哪个评估设置的哪个指标\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"Figure 1 x轴标签字体偏小，打印后可能低于 7pt\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M4\"\n  summary: \"Appendix T 定性示例仅 Pythia-2.8B 一条链，退化过于极端\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"补充 Qwen/Llama 等不同退化模式的链\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M5\"\n  summary: \"缺少 self-training/self-play 文献引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"Yuan et al. 2024 Self-Rewarding LMs, Chen et al. 2024 SPIN 可在 §2.2 简要提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============ PRIOR ROUNDS — STATUS UPDATE ============\n\n- id: \"R1-N1\"\n  summary: \"DDR tri-partition 阈值统计基础不可靠：异方差下使用 Cohen's d\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提，R2 AGREE\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"补充 Glass's Δ + Cliff's δ\"}\n    - {round: 23, reviewers: \"R1(warning),R2(rebut)\", note: \"R1 仍标记正文依赖 pooled d；R2 认为论文已有 robust 指标覆盖，仅为 minor presentation issue。分歧倾向 R2：已有充分 sensitivity check。\"}\n  action_items:\n    - {round: 22, action: \"Glass's Δ + Cliff's δ added to appendix\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"在正文 §4.2 中提及 Glass's Δ 结果（当前仅在附录）\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2-old\"\n  summary: \"DDR 3/1/3 partition post-hoc 选择，统计证据弱于 2-group structure\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提，R2 AGREE\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"restructured to 2-group primary + 3/1/3 refinement\"}\n    - {round: 23, reviewers: \"\", note: \"本轮未被明确提及，可能已通过 restructuring 解决，待确认\"}\n  action_items:\n    - {round: 22, action: \"Restructured §4.2 + Contribution 2\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1-old\"\n  summary: \"Framing 矛盾：Introduction 实用动机 vs Discussion 诊断定位\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"修改了 Intro L5, L9\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1 rebut R2-N1 时指出论文已定位为 diagnostic，但同意 Intro 仍在 provenance/diagnostic 之间摇摆。R2-M1 也指出 model collapse/provenance 双动机不均衡。问题部分残留。\"}\n  action_items:\n    - {round: 22, action: \"L5/L9 revised\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"统一 Intro/Discussion 的动机线（与 R23-W5 合并处理）\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2-old\"\n  summary: \"新颖性受限：三篇并行工作收敛于 ~3 classes\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1 AGREE with nuance\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"novelty 锚定在 DDR 分解\"}\n    - {round: 23, reviewers: \"\", note: \"本轮未被明确重提，R2 转而关注 DDR 包装力度问题（R23-D1），相关但角度不同\"}\n  action_items:\n    - {round: 22, action: \"L9 + Contribution 2 restructured\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"下游 TOST n=3 统计效力严重不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提(warning)，R2同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"升级 critical\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"再次确认。合并至 R23-N2。\"}\n  action_items:\n    - {round: 22, action: \"Discussion restructured to demote downstream evidence\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"见 R23-N2 action items\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N5\"\n  summary: \"QLoRA F1=0.905 是否削弱 DDR 框架贡献\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提(warning)，R2同意\"}\n    - {round: 22, reviewers: \"R1(critical),R2(rebut)\", note: \"分歧未解决\"}\n    - {round: 23, reviewers: \"\", note: \"本轮未被明确重提。R1 在 Strengths 中将 QLoRA 列为优点（upper bound + interpretability tradeoff）。\"}\n  action_items:\n    - {round: 22, action: \"Discussion added explicit ceiling acknowledgment\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ RESOLVED (prior rounds) ============\n\n- id: \"R2-W4\"\n  summary: \"正文可能超8页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"Main content ≤8 pages confirmed\"\n  resolution_round: 21\n\n- id: \"R21-M1\"\n  summary: \"Missing reference: SemEval 2024 Task 8 Subtask B\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"SemEval 已引用\"\n  resolution_round: 21\n\n- id: \"R21-M2\"\n  summary: \"孤立bib entry (radar)未被引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Orphan entry deleted\"\n  resolution_round: 21\n\n- id: \"R22-M1\"\n  summary: \"Orphan bib: self_refine\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Deleted from references.bib\"\n  resolution_round: 22\n\n- id: \"R22-M2\"\n  summary: \"Abstract 中 LLM 缩写未展开\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Changed to 'large language models (LLMs)'\"\n  resolution_round: 22\n\n- id: \"R22-M3\"\n  summary: \"Table 2 baseline ms/text N/A 未解释\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Table 2 caption explanation added\"\n  resolution_round: 22\n\n- id: \"R2-W5-r22\"\n  summary: \"Contribution 3 过于笼统 (catch-all)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Split into Contribution 3 + 4\"\n  resolution_round: 22\n\n- id: \"R2-W2-r22\"\n  summary: \"Table 1 中 3-class F1 列在 Binary F1 之前可能误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Table 1 columns swapped\"\n  resolution_round: 22\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "\n# Round 23 Review Issues — Fresh review (Round 23)\n# Previous rounds (21-22) issues carried forward with status updates\n\n# ============ CRITICAL (Must-Fix) ============\n\n- id: \"R1-N2\"\n  summary: \"仅限 base model 的限制对论文 significance 造成根本性约束\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"严重性取决于 framing; 科学发现定位使其降为 design scope\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"两位 Reviewer 再次一致标记 critical。Appendix K 3个家族(OLMo/Qwen/Llama)全部显示 DDR 结构颠覆：entropy mean ρ 翻转，6/7 特征方向反转，OLMo LOGO F1 0.763→0.338。论文多处措辞暗示超出 base-model 范围的一般性。\"}\n  action_items:\n    - {round: 21, action: \"Abstract + Contribution 均加 scope limitation\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 22, action: \"No additional change needed — resolved by C2 framing adjustment to scientific characterization\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"Title 已含 'Base LLM'；需检查 Abstract/Intro/Conclusion 中是否仍有超范围表述\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-N1\"\n  summary: \"Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage，论文 framing 与可靠评估之间存在落差\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提 critical，R2 agree 但认为接近 should-fix。gen-0 recall=99.4% vs gen-1 75.0%/gen-2+ 73.7% 不对称性与 leakage 一致。Independent-seed 实验仅 2 generators 不足以验证。需 full 8-gen independent-seed 3-class F1。\"}\n  action_items:\n    - {round: 23, action: \"在 full 8-gen LOGO 设置下进行 independent-seed 实验，报告 3-class F1；或调整论文 framing 以 binary 为核心\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-N2\"\n  summary: \"下游效用实验 n=3 统计效力不足，且结果否定 depth classification 的数据筛选价值\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R2 标记 critical（动机自我否定），R1 标记 warning（统计效力）。n=3 seeds 下 Cohen's d=86.0/119.7 为 artificial inflation。Discussion 和 Contribution 4 仍将此作为核心结论引用。双重问题：统计基础薄弱 + 结果本身削弱论文价值主张。\"}\n  action_items:\n    - {round: 23, action: \"增加 seeds 至 10-20，或将 Contribution 4 降级为 preliminary observation 并在正文引用时加 qualification\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ DIVERGENCE ============\n\n- id: \"R23-D1\"\n  summary: \"DDR '框架' 的理论贡献是否被过度包装\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(rebut),R2(critical)\", note: \"R2 认为 DDR 本质是按相关系数分组的描述性分析。R1 反驳举证 6 层验证（k-means, 多指标交叉, per-gen TOST, sensitivity, holdout, heteroscedasticity robustness）。Director 判断：DDR 验证确实超出简单描述性分析，但 'framework' 措辞可降为 'empirical finding/decomposition'。\"}\n  action_items:\n    - {round: 23, action: \"将 DDR 从 'framework' 调整为 'empirical decomposition/finding'，保留多层验证证据但降低理论贡献的包装力度\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ WARNING (Should-Fix) ============\n\n- id: \"R1-W1\"\n  summary: \"Tail decay 作为 'near-stationary' 特征分类统计支撑不足（TOST 4/8）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 22, reviewers: \"R1,R2\", note: \"建议提升为 Limitations 首条\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提，R2 agree。|d|=0.15-0.22 已接近 intermediate 区间(d=0.16)。建议重新归类为 intermediate 或标记 weakly stationary。\"}\n  action_items:\n    - {round: 23, action: \"考虑将 tail decay 移至 intermediate 组（3/2/2 结构），或在正文充分讨论其边界地位\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W1\"\n  summary: \"多个 generator subset (5/6/8-gen) 混用增加 cross-experiment 比较复杂度\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - {round: 22, reviewers: \"R1,R2\", note: \"Appendix U has subset summary\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"两人均 agree。没有统一对照表说明何时用何 subset。核心 claim 应统一 8-gen LOGO。\"}\n  action_items:\n    - {round: 23, action: \"在正文或附录添加统一的 generator subset 参照表；核心 claim 统一使用 8-gen LOGO\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"Cross-domain 实验 t=1.0 超出可靠范围，domain 和 temperature 效应混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提，R2 agree 并强化。t=0.7 下 Academic domain F1 降至 0.626（vs t=1.0 的 0.739），cross-domain robustness 部分归功于高温度。\"}\n  action_items:\n    - {round: 23, action: \"Cross-domain claim 应基于 t=0.7 结果；Limitations 中更显著讨论此混淆\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W3\"\n  summary: \"Baseline 对比不完整：缺少 n-gram 统计特征 baseline\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"R2首提，R1 部分同意。缺 n-gram 统计特征 baseline。Avg-LogProb 和 QLoRA 已有但 R2 遗漏。RoBERTa finetune 可由 QLoRA 上界替代。\"}\n  action_items:\n    - {round: 23, action: \"增加 character n-gram profile 或类似简单统计 baseline\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"3 个 drifting features 高度相关（r=0.81-0.97），可能是同一 latent factor\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提 minor，R2 agree 并升级。TTR-hapax r=0.97，entropy_mean-TTR r=0.86。需 PCA/factor analysis 验证 DDR 3-drifting 结构是否应合并为 1-2 factors。\"}\n  action_items:\n    - {round: 23, action: \"进行 PCA 或 factor analysis 验证 drifting group 的维度结构\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"Introduction model collapse/provenance 双动机在 Discussion 中发展不均衡\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"Provenance 方向在 downstream 实验后基本被放弃，但 Intro 仍保留此动机。\"}\n  action_items:\n    - {round: 23, action: \"统一 Introduction 和 Discussion 的动机线：坚定 commit 到 scientific characterization 方向\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MINOR / INFO ============\n\n- id: \"R23-M1\"\n  summary: \"Table 1 脚注中 gen-0 seed sharing 信息过于不显眼\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"应提升至 caption 主体或正文讨论\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"Discussion 中 'gen-1 per-class F1=0.63' 指代不明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"应标注来源：哪个评估设置的哪个指标\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"Figure 1 x轴标签字体偏小，打印后可能低于 7pt\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M4\"\n  summary: \"Appendix T 定性示例仅 Pythia-2.8B 一条链，退化过于极端\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"补充 Qwen/Llama 等不同退化模式的链\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M5\"\n  summary: \"缺少 self-training/self-play 文献引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"Yuan et al. 2024 Self-Rewarding LMs, Chen et al. 2024 SPIN 可在 §2.2 简要提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============ PRIOR ROUNDS — STATUS UPDATE ============\n\n- id: \"R1-N1\"\n  summary: \"DDR tri-partition 阈值统计基础不可靠：异方差下使用 Cohen's d\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提，R2 AGREE\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"补充 Glass's Δ + Cliff's δ\"}\n    - {round: 23, reviewers: \"R1(warning),R2(rebut)\", note: \"R1 仍标记正文依赖 pooled d；R2 认为论文已有 robust 指标覆盖，仅为 minor presentation issue。分歧倾向 R2：已有充分 sensitivity check。\"}\n  action_items:\n    - {round: 22, action: \"Glass's Δ + Cliff's δ added to appendix\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"在正文 §4.2 中提及 Glass's Δ 结果（当前仅在附录）\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2-old\"\n  summary: \"DDR 3/1/3 partition post-hoc 选择，统计证据弱于 2-group structure\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提，R2 AGREE\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"restructured to 2-group primary + 3/1/3 refinement\"}\n    - {round: 23, reviewers: \"\", note: \"本轮未被明确提及，可能已通过 restructuring 解决，待确认\"}\n  action_items:\n    - {round: 22, action: \"Restructured §4.2 + Contribution 2\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1-old\"\n  summary: \"Framing 矛盾：Introduction 实用动机 vs Discussion 诊断定位\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"修改了 Intro L5, L9\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1 rebut R2-N1 时指出论文已定位为 diagnostic，但同意 Intro 仍在 provenance/diagnostic 之间摇摆。R2-M1 也指出 model collapse/provenance 双动机不均衡。问题部分残留。\"}\n  action_items:\n    - {round: 22, action: \"L5/L9 revised\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"统一 Intro/Discussion 的动机线（与 R23-W5 合并处理）\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2-old\"\n  summary: \"新颖性受限：三篇并行工作收敛于 ~3 classes\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1 AGREE with nuance\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"novelty 锚定在 DDR 分解\"}\n    - {round: 23, reviewers: \"\", note: \"本轮未被明确重提，R2 转而关注 DDR 包装力度问题（R23-D1），相关但角度不同\"}\n  action_items:\n    - {round: 22, action: \"L9 + Contribution 2 restructured\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"下游 TOST n=3 统计效力严重不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提(warning)，R2同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"升级 critical\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"再次确认。合并至 R23-N2。\"}\n  action_items:\n    - {round: 22, action: \"Discussion restructured to demote downstream evidence\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"见 R23-N2 action items\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N5\"\n  summary: \"QLoRA F1=0.905 是否削弱 DDR 框架贡献\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提(warning)，R2同意\"}\n    - {round: 22, reviewers: \"R1(critical),R2(rebut)\", note: \"分歧未解决\"}\n    - {round: 23, reviewers: \"\", note: \"本轮未被明确重提。R1 在 Strengths 中将 QLoRA 列为优点（upper bound + interpretability tradeoff）。\"}\n  action_items:\n    - {round: 22, action: \"Discussion added explicit ceiling acknowledgment\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ RESOLVED (prior rounds) ============\n\n- id: \"R2-W4\"\n  summary: \"正文可能超8页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"Main content ≤8 pages confirmed\"\n  resolution_round: 21\n\n- id: \"R21-M1\"\n  summary: \"Missing reference: SemEval 2024 Task 8 Subtask B\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"SemEval 已引用\"\n  resolution_round: 21\n\n- id: \"R21-M2\"\n  summary: \"孤立bib entry (radar)未被引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Orphan entry deleted\"\n  resolution_round: 21\n\n- id: \"R22-M1\"\n  summary: \"Orphan bib: self_refine\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Deleted from references.bib\"\n  resolution_round: 22\n\n- id: \"R22-M2\"\n  summary: \"Abstract 中 LLM 缩写未展开\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Changed to 'large language models (LLMs)'\"\n  resolution_round: 22\n\n- id: \"R22-M3\"\n  summary: \"Table 2 baseline ms/text N/A 未解释\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Table 2 caption explanation added\"\n  resolution_round: 22\n\n- id: \"R2-W5-r22\"\n  summary: \"Contribution 3 过于笼统 (catch-all)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Split into Contribution 3 + 4\"\n  resolution_round: 22\n\n- id: \"R2-W2-r22\"\n  summary: \"Table 1 中 3-class F1 列在 Binary F1 之前可能误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Table 1 columns swapped\"\n  resolution_round: 22\n"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-19T03:37:55.204752+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 13972}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-19T03:40:22.677908+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "report": "\n# 审稿报告 — Round 23 (Fresh Review)\n\n**论文**: \"Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewers**: R1（方法严谨性+实验设计+统计分析）, R2（新颖性+写作质量+完整性）\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务，将文本按递归生成深度分类为 gen-0/gen-1/gen-2+，并识别出 differential depth response (DDR) 三分结构：3 个 drifting 特征（entropy mean, TTR, hapax ratio）、1 个 intermediate（entropy std）、3 个 near-stationary（entropy max, tail decay, entropy min）。在 8 个 base model（5 个 family，0.6B–8B）上用 LOGO 评估，leak-free binary F1 = 0.694。实验控制极为严谨（20+ 个附录覆盖多层消融），写作质量良好，格式合规。核心局限：仅限 base model（instruct 模型下 DDR 结构被颠覆）、gen-0 seed sharing 导致 3-class 评估存在 leakage、下游效用实验统计效力不足。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有意义。** [R1,R2 共识] Generation depth classification 将二元 real-vs-synthetic 检测推进到更细粒度的 provenance 分析。与 model collapse 文献的联系建立得好。\n\n**S2. 实验控制极其严谨。** [R1,R2 共识] LOGO + LOFO + seed-level demeaning + independent-seed + length-matched + random-subsample control 构成多层次 confound control pipeline。R1 评价\"很少见到如此完整的 control 链\"。\n\n**S3. DDR 三分结构有分析价值。** [R1,R2 共识] 将特征空间分解为 drifting/intermediate/near-stationary 提供了理解 recursive generation dynamics 的有用视角。多指标交叉验证（ρ, d, KS, Levene, TOST, Glass's Δ, Cliff's δ, k-means, holdout split）增强可信度。\n\n**S4. 分析深度突出。** [R1,R2 共识] 20+ 个附录系统覆盖消融、混淆矩阵、特征分布、跨域迁移、跨温度迁移、扰动鲁棒性、下游效用等维度。QLoRA upper bound（3-class F1=0.905）有效定位了 handcrafted features 的价值。\n\n**S5. 写作质量良好。** [R2] 无 AI 写作痕迹，Abstract 信息密度高，引用完整（68 条），格式合规（≤8 页正文，匿名化完整，ACL review 模板）。\n\n**S6. Limitations 讨论诚实透明。** [R1,R2 共识] 对 base-model 限制、instruction tuning 退化、temperature sensitivity、3-class metric inflation 等问题的自我批评到位，没有 overclaim。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [critical] 仅限 base model 的限制对论文 significance 构成根本性约束。** [R1-N2, R2-N2, 完全共识]\n- Appendix K 显示 3 个 instruct 模型家族（OLMo, Qwen, Llama）全部表现灾难性：entropy mean ρ 从 −0.60 翻转至 +0.48，6/7 特征方向反转，OLMo LOGO F1 从 0.763 暴跌至 0.338。DDR 的核心结构在 instruct model 下被根本性颠覆。\n- 论文多处措辞暗示超出 base-model 范围的一般性（§1 \"how language models transform distributions\"、§6 \"classifying text by generation depth\"），超出实验支撑。\n- Title 已含 \"Base LLM\"，但 Abstract/Introduction/Conclusion 中仍需更显著地限定 scope。\n- 建议：(a) 在 Abstract 前几句即明确 base-model scope；(b) 将 instruct 结果从附录提升到正文 Discussion 作为核心发现；(c) 讨论 DDR 特征方向反转的理论含义。\n\n**C2. [critical] Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage。** [R1-N1 critical, R2 agree 但倾向 should-fix]\n- LOGO 中 held-out generator 的 gen-0 文本与训练集 gen-0 完全相同（共享 Wikipedia seed passages），构成 data leakage。Confusion matrix 显示 gen-0 recall=99.4%（vs gen-1: 75.0%, gen-2+: 73.7%），不对称性与 leakage 一致。\n- Binary F1 = 0.694 作为 primary metric 不受影响（排除 gen-0），但论文的 Contribution 1 和 Abstract 同时呈现 3-class F1 = 0.762，后者受 gen-0 leakage 污染。\n- Independent-seed 实验（Appendix T）仅 2 generators（Pythia-2.8B, OLMo），不足以验证 full 3-class LOGO 可靠性。\n- 建议：在 full 8-gen LOGO 下进行 independent-seed 实验并报告 3-class F1；或将论文 framing 调整为以 binary 为核心。\n\n**C3. [critical] 下游效用实验统计效力不足，且结果削弱论文价值主张。** [R1-W2 warning, R2-N1 critical, 共识]\n- Downstream fine-tuning 实验仅 n=3 seeds，Cohen's d 值 86.0/119.7 为 artificial inflation。TOST 结果虽然 \"practically indistinguishable\"，但 n=3 的统计效力极低。\n- 更根本的问题：depth-aware curation 与 random subsampling 无差异，否定了 depth classification 最直觉的应用场景（数据筛选）。论文试图将此定位为 supporting evidence（DDR 是 diagnostic 而非 prescriptive），但 Discussion 和 Contribution 4 仍将此作为核心结论反复引用。\n- 建议：增加 seeds 至 10-20；将 Contribution 4 降级为 preliminary observation；更坚定地 commit 到 \"scientific characterization\" 方向。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [warning] Tail decay 的 \"near-stationary\" 分类统计支撑不足。** [R1-W1, R2 agree]\n- TOST 等效性检验（ε=0.20）仅 4/8 generators 通过，|d| 范围 0.15–0.22 已接近 intermediate 区间（entropy std d=0.16）。需放松至 ε=0.25 才达 7/8。\n- 建议考虑将 tail decay 移至 intermediate 组（3/2/2 结构），或在正文充分讨论其边界地位。\n\n**W2. [warning] Cross-domain 实验使用 t=1.0，与主实验 t=0.7 不一致，domain 和 temperature 效应混淆。** [R1-W5, R2 agree 并强化]\n- t=0.7 下 Academic domain binary F1 降至 0.626（vs t=1.0 的 0.739），cross-domain robustness 部分归功于高温度而非真正的 domain 迁移。\n- 建议 cross-domain claim 基于 t=0.7 结果。\n\n**W3. [warning] 多个 generator subset (5/6/8-gen) 混用增加 cross-experiment 比较复杂度。** [R1-W4, R2 agree]\n- 不同 section/appendix 使用 5/6/8-gen subsets，缺统一对照表。核心 claim 应统一使用 8-gen LOGO。\n\n**W4. [warning] Baseline 对比缺少 n-gram 统计特征 baseline。** [R2-W4, R1 partially agree]\n- 缺少 character n-gram profile 等简单统计 baseline。Avg-LogProb 和 QLoRA 已有但可补充。\n\n**W5. [warning] 3 个 drifting features 高度相关（r=0.81-0.97），DDR 的 \"3-drifting\" 结构可能被维度高估。** [R1-M3, R2 agree]\n- TTR-hapax r=0.97，entropy mean-TTR r=0.86。需 PCA/factor analysis 验证是否为单一 latent factor。\n\n**W6. [warning] Introduction 的 model collapse/data provenance 双动机在 Discussion 中发展不均衡。** [R2-M1, R1 agree]\n- Provenance 方向在 downstream 实验后基本被放弃，但 Introduction 仍保留此动机。论文应坚定 commit 到 scientific characterization 方向。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Base-model-only 是全文最根本的约束**（C1）：DDR 在 instruct 模型下完全失效，论文的实际影响力受限。两位 Reviewer 均标记 critical。\n2. **Gen-0 seed sharing 需要 full 8-gen independent-seed 3-class F1 来 resolve**（C2）：当前 binary F1 不受影响，但 3-class 叙事缺乏干净支撑。\n3. **下游 utility 是最薄弱的 Contribution**（C3）：n=3 统计效力不足 + 结果本身否定数据筛选价值。Contribution 4 需降级或加强。\n4. **实验控制极其严谨**：多层 confound control 是论文最大优势。\n5. **DDR 的分析价值真实**：即使分类性能一般，drifting/stationary 分解提供了有用的科学视角。\n6. **写作质量和格式合规**：无 AI 痕迹，引用充分，满足 ARR 要求。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**D1. DDR \"框架\" 是否被过度包装。** [R2-N3 critical, R1 REBUT]\n- R2 认为 DDR 本质是按相关系数分组的描述性分析，不构成方法论贡献。\n- R1 反驳：DDR 经过 6 层独立验证（k-means clustering, 多指标交叉验证, per-generator TOST, TOST bound sensitivity, holdout generator split, heteroscedasticity robustness），超出简单描述性分析。\n- **Director 判断**：R1 的举证更有说服力——DDR 的验证深度确实超过标准 EDA。但 \"framework\" 措辞可能过强，建议调整为 \"empirical decomposition\" 或 \"empirical finding\"。**总体倾向 R1，但建议适度降低包装力度。**\n\n**D2. Baseline \"反超\" 的严重性。** [R1-W3 warning, R2 REBUT]\n- R1 认为 4-detector ensemble binary F1=0.708 > 7-feature 0.705 构成\"反超\"，削弱 DDR 方法论贡献。\n- R2 反驳：binary F1 差异仅 0.001（noise 范围内）；论文已声明定位为 \"contextualizing\" 而非 \"competitive advantage\"；DDR 价值在可解释性而非性能。\n- **Director 判断**：R2 更准确。Binary F1 差异 0.001 不构成有意义的\"反超\"。3-class 差异 0.071 值得讨论，但论文定位合理。**不构成独立 weakness。**\n\n**D3. Cohen's d 异方差问题的严重性。** [R1-W6 warning, R2 REBUT]\n- R1 认为正文依赖 pooled Cohen's d 而非 heteroscedasticity-robust 指标。\n- R2 反驳：论文已在附录报告 Glass's Δ 和 Cliff's δ，DDR partition 在 robust 指标下保持不变。\n- **Director 判断**：R2 更准确。这是 presentation issue（正文应提及 robust 指标），不是方法论缺陷。**降级为 minor。**\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1,R2 共识] 能否在 full 8-gen LOGO 设置下报告 independent-seed 3-class F1？这是验证 gen-0 分类可靠性的关键实验。\n\n**Q2** [R1] 8-gen 设置下 cross-reference spread 是否仍 ≤ 0.013？\n\n**Q3** [R1,R2 共识] 是否考虑 PCA/factor analysis 验证 3 个 drifting features 是否为单一 latent factor？\n\n**Q4** [R2] 如果 depth classification 对数据筛选无帮助，最有价值的应用场景是什么？请给出具体用例。\n\n**Q5** [R2] DDR 三分法阈值（|ρ|=0.60, 0.10）的 sensitivity analysis？（R1 指出论文已有 ±0.10 分析和 TOST bound sensitivity，但 R2 可能遗漏。）\n\n**Q6** [R1] Qwen3-1.7B 在 t=0.5/0.7 下 binary F1 完全相同（0.751），CI 缺失原因？\n\n**Q7** [R1] Table 2 pooled vs per-generator macro average 差异从何而来？\n\n**Q8** [R2] Instruction tuning \"reverses feature drift direction\" 基于 3 个家族（非 R2 所述的 1 个），但仍需确认：Llama-3.2-3B-Instruct 的 LOGO F1 是多少？\n\n---\n\n## Missing References\n\n**共识推荐**：\n- Self-training/self-play 文献（Yuan et al. 2024 \"Self-Rewarding LMs\"; Chen et al. 2024 \"SPIN\"）—— 在 §2.2 简要提及作为 training-loop iterative generation 的对比\n- Ordinal regression NLP 应用文献 —— 当前主要引用通用 ML 领域\n\n**可选**：\n- Bao et al. (2024) \"On the Reliability of AI Text Detectors\" —— 与 cross-generator 分析相关\n- 更多 lexical diversity 方法论文 —— R2 提到 MTLD/MATTR，但 R1 指出论文已在 §2.3 引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 2.5/5 | 2/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n- 任务定义新颖（generation depth classification vs binary detection），DDR 三分结构是有价值的经验性发现，实验控制极其严谨 —— 这些优势支撑 Findings 级别。\n- 但三个 critical 问题共同限制了论文达到 Conference 水平：(1) base-model-only 限制使论文在 instruct 模型主导的真实场景下适用性极低；(2) gen-0 seed sharing 使核心三分类评估不完整；(3) 下游效用实验统计效力不足且结果否定了最直觉的应用场景。\n- 方法论贡献（特征工程+XGBoost）在 novelty 维度偏弱（Excitement 2.5/5）。DDR 的价值更多在分析框架而非分类性能，但论文对此的 framing 不够坚定。\n- 如果作者能 (a) 补充 instruct 模型的系统实验（即使为负面结果），(b) 提供 full 8-gen independent-seed 3-class F1，(c) 更坚定地定位为 scientific characterization，论文有潜力达到 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度高，四问题均有回答。\n- \"base (pretrained)\" 限定在最后一句出现，位置过靠后。建议在前几句即明确。\n- 3-class F1 受 gen-0 leakage 影响，应标注或移除。\n\n### Introduction (§1)\n- 叙事线基本完整（背景→缺口→洞察→贡献），但 model collapse 和 data provenance 双动机在后文发展不均衡。\n- Contribution 4（downstream null result）以 n=3 实验支撑，统计基础薄弱。\n- \"how language models transform distributions under iterative conditioning\" 措辞暗示超出 base-model scope。\n\n### Related Work (§2)\n- 组织合理，非 survey 式罗列。\n- §2.3 引用密度略低（但 R1 指出实际有 8 篇引用，5 行文本）。\n- 缺少 self-training/self-play 文献和 ordinal regression NLP 应用。\n\n### Method (§3)\n- 实验设计严谨，LOGO + LOFO 评估协议设计合理。\n- 3-class 分组决策有 Appendix D 5-class 实验支撑。\n- 参考模型选择（Pythia-410M）有 cross-reference 消融（spread ≤ 0.013），但应在正文更显著地讨论。\n\n### Results (§4)\n- Table 1 设计合理（binary F1 在前），但 gen-0 seed sharing 脚注信息过于不显眼。\n- §4.2 DDR 分析有价值，多层验证增强可信度。正文应同时报告 Glass's Δ/Cliff's δ 而非仅在附录。\n- §4.3 baseline 对比定位合理（\"contextualizing\" 而非 \"competitive\"），但缺 n-gram baseline。\n\n### Discussion (§5)\n- \"gen-1 per-class F1=0.63\" 指代不明，应标注来源。\n- model collapse/provenance 动机与 diagnostic 定位之间仍有 framing 张力。\n- downstream utility 结论引用力度与 n=3 统计基础不匹配。\n\n### Limitations (§8)\n- 诚实全面，覆盖 base-model、temperature、scale 等。\n- 温度敏感性和 cross-domain 温度混淆可更显著讨论。\n\n### Appendix\n- 体量巨大（20+ 个），系统覆盖各潜在质疑。\n- Independent-seed 控制（Appendix T）仅 2 generators，需扩展。\n- 定性示例（Appendix X）仅 1 条 Pythia 链，建议补充其他模型。\n\n### Format\n- 正文 ≤ 8 页，Limitations 在 Conclusion 后 References 前，匿名化完整。\n- Figure 1 x 轴标签字体偏小（可能 < 7pt）。\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "report": "\n# 审稿报告 — Round 23 (Fresh Review)\n\n**论文**: \"Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewers**: R1（方法严谨性+实验设计+统计分析）, R2（新颖性+写作质量+完整性）\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务，将文本按递归生成深度分类为 gen-0/gen-1/gen-2+，并识别出 differential depth response (DDR) 三分结构：3 个 drifting 特征（entropy mean, TTR, hapax ratio）、1 个 intermediate（entropy std）、3 个 near-stationary（entropy max, tail decay, entropy min）。在 8 个 base model（5 个 family，0.6B–8B）上用 LOGO 评估，leak-free binary F1 = 0.694。实验控制极为严谨（20+ 个附录覆盖多层消融），写作质量良好，格式合规。核心局限：仅限 base model（instruct 模型下 DDR 结构被颠覆）、gen-0 seed sharing 导致 3-class 评估存在 leakage、下游效用实验统计效力不足。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有意义。** [R1,R2 共识] Generation depth classification 将二元 real-vs-synthetic 检测推进到更细粒度的 provenance 分析。与 model collapse 文献的联系建立得好。\n\n**S2. 实验控制极其严谨。** [R1,R2 共识] LOGO + LOFO + seed-level demeaning + independent-seed + length-matched + random-subsample control 构成多层次 confound control pipeline。R1 评价\"很少见到如此完整的 control 链\"。\n\n**S3. DDR 三分结构有分析价值。** [R1,R2 共识] 将特征空间分解为 drifting/intermediate/near-stationary 提供了理解 recursive generation dynamics 的有用视角。多指标交叉验证（ρ, d, KS, Levene, TOST, Glass's Δ, Cliff's δ, k-means, holdout split）增强可信度。\n\n**S4. 分析深度突出。** [R1,R2 共识] 20+ 个附录系统覆盖消融、混淆矩阵、特征分布、跨域迁移、跨温度迁移、扰动鲁棒性、下游效用等维度。QLoRA upper bound（3-class F1=0.905）有效定位了 handcrafted features 的价值。\n\n**S5. 写作质量良好。** [R2] 无 AI 写作痕迹，Abstract 信息密度高，引用完整（68 条），格式合规（≤8 页正文，匿名化完整，ACL review 模板）。\n\n**S6. Limitations 讨论诚实透明。** [R1,R2 共识] 对 base-model 限制、instruction tuning 退化、temperature sensitivity、3-class metric inflation 等问题的自我批评到位，没有 overclaim。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [critical] 仅限 base model 的限制对论文 significance 构成根本性约束。** [R1-N2, R2-N2, 完全共识]\n- Appendix K 显示 3 个 instruct 模型家族（OLMo, Qwen, Llama）全部表现灾难性：entropy mean ρ 从 −0.60 翻转至 +0.48，6/7 特征方向反转，OLMo LOGO F1 从 0.763 暴跌至 0.338。DDR 的核心结构在 instruct model 下被根本性颠覆。\n- 论文多处措辞暗示超出 base-model 范围的一般性（§1 \"how language models transform distributions\"、§6 \"classifying text by generation depth\"），超出实验支撑。\n- Title 已含 \"Base LLM\"，但 Abstract/Introduction/Conclusion 中仍需更显著地限定 scope。\n- 建议：(a) 在 Abstract 前几句即明确 base-model scope；(b) 将 instruct 结果从附录提升到正文 Discussion 作为核心发现；(c) 讨论 DDR 特征方向反转的理论含义。\n\n**C2. [critical] Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage。** [R1-N1 critical, R2 agree 但倾向 should-fix]\n- LOGO 中 held-out generator 的 gen-0 文本与训练集 gen-0 完全相同（共享 Wikipedia seed passages），构成 data leakage。Confusion matrix 显示 gen-0 recall=99.4%（vs gen-1: 75.0%, gen-2+: 73.7%），不对称性与 leakage 一致。\n- Binary F1 = 0.694 作为 primary metric 不受影响（排除 gen-0），但论文的 Contribution 1 和 Abstract 同时呈现 3-class F1 = 0.762，后者受 gen-0 leakage 污染。\n- Independent-seed 实验（Appendix T）仅 2 generators（Pythia-2.8B, OLMo），不足以验证 full 3-class LOGO 可靠性。\n- 建议：在 full 8-gen LOGO 下进行 independent-seed 实验并报告 3-class F1；或将论文 framing 调整为以 binary 为核心。\n\n**C3. [critical] 下游效用实验统计效力不足，且结果削弱论文价值主张。** [R1-W2 warning, R2-N1 critical, 共识]\n- Downstream fine-tuning 实验仅 n=3 seeds，Cohen's d 值 86.0/119.7 为 artificial inflation。TOST 结果虽然 \"practically indistinguishable\"，但 n=3 的统计效力极低。\n- 更根本的问题：depth-aware curation 与 random subsampling 无差异，否定了 depth classification 最直觉的应用场景（数据筛选）。论文试图将此定位为 supporting evidence（DDR 是 diagnostic 而非 prescriptive），但 Discussion 和 Contribution 4 仍将此作为核心结论反复引用。\n- 建议：增加 seeds 至 10-20；将 Contribution 4 降级为 preliminary observation；更坚定地 commit 到 \"scientific characterization\" 方向。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [warning] Tail decay 的 \"near-stationary\" 分类统计支撑不足。** [R1-W1, R2 agree]\n- TOST 等效性检验（ε=0.20）仅 4/8 generators 通过，|d| 范围 0.15–0.22 已接近 intermediate 区间（entropy std d=0.16）。需放松至 ε=0.25 才达 7/8。\n- 建议考虑将 tail decay 移至 intermediate 组（3/2/2 结构），或在正文充分讨论其边界地位。\n\n**W2. [warning] Cross-domain 实验使用 t=1.0，与主实验 t=0.7 不一致，domain 和 temperature 效应混淆。** [R1-W5, R2 agree 并强化]\n- t=0.7 下 Academic domain binary F1 降至 0.626（vs t=1.0 的 0.739），cross-domain robustness 部分归功于高温度而非真正的 domain 迁移。\n- 建议 cross-domain claim 基于 t=0.7 结果。\n\n**W3. [warning] 多个 generator subset (5/6/8-gen) 混用增加 cross-experiment 比较复杂度。** [R1-W4, R2 agree]\n- 不同 section/appendix 使用 5/6/8-gen subsets，缺统一对照表。核心 claim 应统一使用 8-gen LOGO。\n\n**W4. [warning] Baseline 对比缺少 n-gram 统计特征 baseline。** [R2-W4, R1 partially agree]\n- 缺少 character n-gram profile 等简单统计 baseline。Avg-LogProb 和 QLoRA 已有但可补充。\n\n**W5. [warning] 3 个 drifting features 高度相关（r=0.81-0.97），DDR 的 \"3-drifting\" 结构可能被维度高估。** [R1-M3, R2 agree]\n- TTR-hapax r=0.97，entropy mean-TTR r=0.86。需 PCA/factor analysis 验证是否为单一 latent factor。\n\n**W6. [warning] Introduction 的 model collapse/data provenance 双动机在 Discussion 中发展不均衡。** [R2-M1, R1 agree]\n- Provenance 方向在 downstream 实验后基本被放弃，但 Introduction 仍保留此动机。论文应坚定 commit 到 scientific characterization 方向。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Base-model-only 是全文最根本的约束**（C1）：DDR 在 instruct 模型下完全失效，论文的实际影响力受限。两位 Reviewer 均标记 critical。\n2. **Gen-0 seed sharing 需要 full 8-gen independent-seed 3-class F1 来 resolve**（C2）：当前 binary F1 不受影响，但 3-class 叙事缺乏干净支撑。\n3. **下游 utility 是最薄弱的 Contribution**（C3）：n=3 统计效力不足 + 结果本身否定数据筛选价值。Contribution 4 需降级或加强。\n4. **实验控制极其严谨**：多层 confound control 是论文最大优势。\n5. **DDR 的分析价值真实**：即使分类性能一般，drifting/stationary 分解提供了有用的科学视角。\n6. **写作质量和格式合规**：无 AI 痕迹，引用充分，满足 ARR 要求。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n**D1. DDR \"框架\" 是否被过度包装。** [R2-N3 critical, R1 REBUT]\n- R2 认为 DDR 本质是按相关系数分组的描述性分析，不构成方法论贡献。\n- R1 反驳：DDR 经过 6 层独立验证（k-means clustering, 多指标交叉验证, per-generator TOST, TOST bound sensitivity, holdout generator split, heteroscedasticity robustness），超出简单描述性分析。\n- **Director 判断**：R1 的举证更有说服力——DDR 的验证深度确实超过标准 EDA。但 \"framework\" 措辞可能过强，建议调整为 \"empirical decomposition\" 或 \"empirical finding\"。**总体倾向 R1，但建议适度降低包装力度。**\n\n**D2. Baseline \"反超\" 的严重性。** [R1-W3 warning, R2 REBUT]\n- R1 认为 4-detector ensemble binary F1=0.708 > 7-feature 0.705 构成\"反超\"，削弱 DDR 方法论贡献。\n- R2 反驳：binary F1 差异仅 0.001（noise 范围内）；论文已声明定位为 \"contextualizing\" 而非 \"competitive advantage\"；DDR 价值在可解释性而非性能。\n- **Director 判断**：R2 更准确。Binary F1 差异 0.001 不构成有意义的\"反超\"。3-class 差异 0.071 值得讨论，但论文定位合理。**不构成独立 weakness。**\n\n**D3. Cohen's d 异方差问题的严重性。** [R1-W6 warning, R2 REBUT]\n- R1 认为正文依赖 pooled Cohen's d 而非 heteroscedasticity-robust 指标。\n- R2 反驳：论文已在附录报告 Glass's Δ 和 Cliff's δ，DDR partition 在 robust 指标下保持不变。\n- **Director 判断**：R2 更准确。这是 presentation issue（正文应提及 robust 指标），不是方法论缺陷。**降级为 minor。**\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1,R2 共识] 能否在 full 8-gen LOGO 设置下报告 independent-seed 3-class F1？这是验证 gen-0 分类可靠性的关键实验。\n\n**Q2** [R1] 8-gen 设置下 cross-reference spread 是否仍 ≤ 0.013？\n\n**Q3** [R1,R2 共识] 是否考虑 PCA/factor analysis 验证 3 个 drifting features 是否为单一 latent factor？\n\n**Q4** [R2] 如果 depth classification 对数据筛选无帮助，最有价值的应用场景是什么？请给出具体用例。\n\n**Q5** [R2] DDR 三分法阈值（|ρ|=0.60, 0.10）的 sensitivity analysis？（R1 指出论文已有 ±0.10 分析和 TOST bound sensitivity，但 R2 可能遗漏。）\n\n**Q6** [R1] Qwen3-1.7B 在 t=0.5/0.7 下 binary F1 完全相同（0.751），CI 缺失原因？\n\n**Q7** [R1] Table 2 pooled vs per-generator macro average 差异从何而来？\n\n**Q8** [R2] Instruction tuning \"reverses feature drift direction\" 基于 3 个家族（非 R2 所述的 1 个），但仍需确认：Llama-3.2-3B-Instruct 的 LOGO F1 是多少？\n\n---\n\n## Missing References\n\n**共识推荐**：\n- Self-training/self-play 文献（Yuan et al. 2024 \"Self-Rewarding LMs\"; Chen et al. 2024 \"SPIN\"）—— 在 §2.2 简要提及作为 training-loop iterative generation 的对比\n- Ordinal regression NLP 应用文献 —— 当前主要引用通用 ML 领域\n\n**可选**：\n- Bao et al. (2024) \"On the Reliability of AI Text Detectors\" —— 与 cross-generator 分析相关\n- 更多 lexical diversity 方法论文 —— R2 提到 MTLD/MATTR，但 R1 指出论文已在 §2.3 引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 2.5/5 | 2/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.0 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n- 任务定义新颖（generation depth classification vs binary detection），DDR 三分结构是有价值的经验性发现，实验控制极其严谨 —— 这些优势支撑 Findings 级别。\n- 但三个 critical 问题共同限制了论文达到 Conference 水平：(1) base-model-only 限制使论文在 instruct 模型主导的真实场景下适用性极低；(2) gen-0 seed sharing 使核心三分类评估不完整；(3) 下游效用实验统计效力不足且结果否定了最直觉的应用场景。\n- 方法论贡献（特征工程+XGBoost）在 novelty 维度偏弱（Excitement 2.5/5）。DDR 的价值更多在分析框架而非分类性能，但论文对此的 framing 不够坚定。\n- 如果作者能 (a) 补充 instruct 模型的系统实验（即使为负面结果），(b) 提供 full 8-gen independent-seed 3-class F1，(c) 更坚定地定位为 scientific characterization，论文有潜力达到 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度高，四问题均有回答。\n- \"base (pretrained)\" 限定在最后一句出现，位置过靠后。建议在前几句即明确。\n- 3-class F1 受 gen-0 leakage 影响，应标注或移除。\n\n### Introduction (§1)\n- 叙事线基本完整（背景→缺口→洞察→贡献），但 model collapse 和 data provenance 双动机在后文发展不均衡。\n- Contribution 4（downstream null result）以 n=3 实验支撑，统计基础薄弱。\n- \"how language models transform distributions under iterative conditioning\" 措辞暗示超出 base-model scope。\n\n### Related Work (§2)\n- 组织合理，非 survey 式罗列。\n- §2.3 引用密度略低（但 R1 指出实际有 8 篇引用，5 行文本）。\n- 缺少 self-training/self-play 文献和 ordinal regression NLP 应用。\n\n### Method (§3)\n- 实验设计严谨，LOGO + LOFO 评估协议设计合理。\n- 3-class 分组决策有 Appendix D 5-class 实验支撑。\n- 参考模型选择（Pythia-410M）有 cross-reference 消融（spread ≤ 0.013），但应在正文更显著地讨论。\n\n### Results (§4)\n- Table 1 设计合理（binary F1 在前），但 gen-0 seed sharing 脚注信息过于不显眼。\n- §4.2 DDR 分析有价值，多层验证增强可信度。正文应同时报告 Glass's Δ/Cliff's δ 而非仅在附录。\n- §4.3 baseline 对比定位合理（\"contextualizing\" 而非 \"competitive\"），但缺 n-gram baseline。\n\n### Discussion (§5)\n- \"gen-1 per-class F1=0.63\" 指代不明，应标注来源。\n- model collapse/provenance 动机与 diagnostic 定位之间仍有 framing 张力。\n- downstream utility 结论引用力度与 n=3 统计基础不匹配。\n\n### Limitations (§8)\n- 诚实全面，覆盖 base-model、temperature、scale 等。\n- 温度敏感性和 cross-domain 温度混淆可更显著讨论。\n\n### Appendix\n- 体量巨大（20+ 个），系统覆盖各潜在质疑。\n- Independent-seed 控制（Appendix T）仅 2 generators，需扩展。\n- 定性示例（Appendix X）仅 1 条 Pythia 链，建议补充其他模型。\n\n### Format\n- 正文 ≤ 8 页，Limitations 在 Conclusion 后 References 前，匿名化完整。\n- Figure 1 x 轴标签字体偏小（可能 < 7pt）。\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-19T03:40:26.795628+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 1692 · 2026-05-19T03:40:42.057081+00:00_

审稿报告已投递至 Research Director。

**审稿完成总结**：

- **Overall Score: 3.0 (Findings)**
- **R1**: 3.0, **R2**: 3.0, **综合**: 3.0
- **3 个 Must-Fix**：(1) base-model-only 限制是根本性约束——instruct 模型下 DDR 完全失效；(2) gen-0 seed sharing 导致 3-class 评估存在 leakage；(3) 下游效用实验 n=3 统计效力不足且结果否定数据筛选价值
- **6 个 Should-Fix**：tail decay 分类边界、cross-domain 温度混淆、generator subset 混用、缺 n-gram baseline、drifting features 高相关、动机线不均衡
- **1 个分歧**：DDR "框架" 包装力度（R2 认为过度包装，R1 举证 6 层验证反驳，Director 倾向 R1 但建议适度降低措辞）
- **核心共识**：任务定义新颖、实验控制极其严谨、DDR 分析有真实科学价值，但 base-model 限制和中等性能共同限制了论文达到 Conference 水平

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 156

## Round 156

2 recorded events


### User

_source line 1693 · 2026-05-19T03:40:44.765304+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**汇总**：对 R1 的 14 个具体 issue，同意 10 个，反驳 4 个。

核心共识：
- **Base-model-only**（R1-N2 = 我的 N2）是最根本约束，instruct 模型下 DDR 结构崩塌
- **Gen-0 seed sharing**（R1-N1）需补充 independent-seed 3-class F1
- **Downstream utility 统计效力不足**（R1-W2 + 我的 N1）

核心分歧：
- R1-W3 "4-det 反超"：binary F1 差异仅 0.001，不构成反超；3-class 差异 0.071 有意义但论文已明确定位为可解释性而非竞争性能
- R1-W6 异方差：论文已用 Glass's Δ/Cliff's δ 覆盖
- R1-M5 CO₂：超出 ARR 规范要求

维持 Overall 3.0 (Findings) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1694 · 2026-05-19T03:41:01.463805+00:00_

审稿报告已投递至 Research Director。

**Round 23 审稿完成**。汇总如下：

**Overall: 3.0 (Findings)**，两位 Reviewer 一致。

**3 个 Must-Fix**：
1. **Base-model-only 限制**（最根本约束）— instruct 模型下 DDR 结构完全崩塌，论文实际影响力受限
2. **Gen-0 seed sharing leakage** — 3-class 评估不干净，需 full 8-gen independent-seed 实验
3. **下游效用实验** — n=3 统计效力不足 + 结果否定数据筛选价值，Contribution 4 需降级

**6 个 Should-Fix**：tail decay 分类边界、cross-domain 温度混淆、generator subset 混用、n-gram baseline 缺失、drifting features 高相关性、Introduction 动机不均衡

**1 个分歧**（DDR 包装力度）：R2 认为过度包装，R1 举证 6 层验证反驳。Director 判断 R1 更有说服力，但建议从 "framework" 调整为 "empirical decomposition"。

**主要优势**：任务定义新颖、实验控制极其严谨、DDR 分析有科学价值、写作质量好、Limitations 诚实透明。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 157

## Round 157

80 recorded events


### User

_source line 1695 · 2026-05-19T04:01:35.643721+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-19T04:01:41.757768+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-19T04:01:41.758564+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-19T04:01:48.234600+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-19T04:01:48.285228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-19T04:01:54.784204+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-19T04:01:55.286984+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (56 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 提交前最终检查（OpenReview form, AI disclosure）\n\n## 温度扩展实验结果（全部完成，已写入论文）\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\n|-------|------|-----------|--------|-------------|\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\n\n## 其他近期结论\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\n\n## 论文状态\n全部编辑完成，编译 0 errors，27 页。\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\n- appendix_tost.tex（8×7 per-generator TOST table）\n- appendix_classifier.tex OLMo 版本脚
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-19T04:01:56.290995+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-19T04:01:56.392231+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 3977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-19T04:01:56.392662+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 1705 · 2026-05-19T04:01:56.493216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-19T04:02:01.511924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-19T04:02:02.534961+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit template anonymous"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit template anonymous"
  }
}
```

</details>

---


### Tool call

_source line 1708 · 2026-05-19T04:02:05.394986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "description": "Check paper file existence and size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "description": "Check paper file existence and size"
  }
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-19T04:02:06.298772+00:00_

-rw-r--r-- 1 ubuntu ubuntu 3591 May 19 01:51 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
160 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1710 · 2026-05-19T04:02:06.751770+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-19T04:02:07.254431+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml

# Round 23 Review Issues — Updated after R23 Action Matrix execution
# Previous rounds (21-22) issues carried forward with status updates

# ============ CRITICAL (Must-Fix) ============

- id: "R1-N2"
  summary: "仅限 base model 的限制对论文 significance 造成根本性约束"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 23
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R2首提，R1完全同意"}
    - {round: 22, reviewers: "R1,R2", note: "严重性取决于 framing; 科学发现定位使其降为 design scope"}
    - {round: 23, reviewers: "R1,R2", note: "两位 Reviewer 再次一致标记 critical。论文多处措辞暗示超出 base-model 范围的一般性。"}
  action_items:
    - {round: 21, action: "Abstract + Contribution 均加 scope limitation", assigned_to: "Director", status: "done"}
    - {round: 22, action: "No additional change needed — resolved by C2 framing adjustment to scientific characterization", assigned_to: "Director", status: "done"}
    - {round: 23, action: "Abstract 重写前置 base-model scope；Intro L5 'how language models' → 'how base language models'；Intro L5 移除 provenance 引用；Intro L8 移除 provenance 定义", assigned_to: "Director", status: "done"}
  resolution: ""
  resolution_round: null

- id: "R23-N1"
  summary: "Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage，论文 framing 与可靠评估之间存在落差"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 23
  last_seen_round: 23
  mentions:
    - {round: 23, reviewers: "R1,R2", note: "R1首提 critical，R2 agree 但认为接近 should-fix。Independent-seed 实验仅 2 generators 不足以验证。需 full 8-gen independent-seed 3-class F1。"}
  action_items:
    - {round: 23, action: "Text fix: Table 1 caption 重写，显著标注 seed sharing + independent-seed control 引用。Abstract 移除 3-class F1。Binary 为唯一 primary metric。Full 8-gen independent-seed 需 GPU（服务器关机），留作 rebuttal", assigned_to: "Director", status: "done"}
  resolution: "论文 framing 已调整为 binary-primary；full 8-gen i
…[truncated 12845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1712 · 2026-05-19T04:02:07.656732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.pdf 2>/dev/null || echo \"NO_PDF\"",
  "description": "Check for paper PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.pdf 2>/dev/null || echo \"NO_PDF\"",
    "description": "Check for paper PDF"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-19T04:02:07.707384+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig1_differential_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig2_framework.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig3_baseline_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1714 · 2026-05-19T04:02:08.711064+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about EMNLP 2026 ACL Rolling Review submission guidelines:

## Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the conference will be performed via the Open Review platform. Authors follow a two-step process: first submitting articles to ARR where they receive reviews and meta-rev
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7199
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-19T04:02:09.263842+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit template anonymous"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's information about ACL Rolling Review 2026 author guidelines:

**Page Limit:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Template:**
There is an official Overleaf template. Note that this template has a [review] setting that must be on for the submission.

**Anonymity Requirements:**
Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previousl
…[truncated 541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6728
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-19T04:02:33.867114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-19T04:02:34.469744+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{lineno}
12	\usepackage{placeins}
13	\usepackage{multirow}
14	\linenumbers
15	
16	\graphicspath{{../chart/}}
17	
18	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base LLM Text Chains}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{results}
31	
32	\input{discussion}
33	\input{conclusion}
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\appendix
40	
41	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
42	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
43	
44	\input{appendix_dataset_stats}
45	\FloatBarrier
46	
47	\section{Length Confound Analysis}
48	\label{app:length}
49	\input{appendix_length}
50	\FloatBarrier
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	\FloatBarrier
56	
57	\section{Finer-Grained Depth Classification}
58	\label{app:finer-depth}
59	\input{appendix_finer_depth}
60	\FloatBarrier
61	
62	\section{End-to-End Depth Classification (QLoRA)}
63	\label{app:qlora}
64	\input{appendix_qlora}
65	\FloatBarrier
66	
67	\section{Leave-One-Feature-Out Analysis}
68	\label{app:lofo}
69	\input{appendix_lofo}
70	\FloatBarrier
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	\FloatBarrier
76	
77	\section{Classifier Sensitivity}
78	\label{app:classifier}
79	\input{appendix_classifier}
80	\FloatBarrier
81	
82	\section{Robustness to Text Pert
…[truncated 2125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-19T04:02:34.620705+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex | sort",
  "description": "List all tex files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex | sort",
    "description": "List all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-19T04:02:35.424459+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex
/home/ubuntu/.agent-ml-research-idea_gen_051
…[truncated 2501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1720 · 2026-05-19T04:02:36.127684+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review CFP 2026 page limit appendix responsible NLP checklist submission requirements",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review CFP 2026 page limit appendix responsible NLP checklist submission requirements",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool result

_source line 1721 · 2026-05-19T04:02:42.704313+00:00_

Web search results for query: "ACL Rolling Review CFP 2026 page limit appendix responsible NLP checklist submission requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Industry Track - ACL 2026","url":"https://2026.aclweb.org/calls/industry_track/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the ACL Rolling Review CFP information, here are the key submission requirements you asked about:

## Page Limits

The paper follows page limits (8 for long, 4 for short, not including limitations and ethical considerations).

## Appendix

The paper should be readable by itself, and a
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6576
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-19T04:02:47.222467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1723 · 2026-05-19T04:02:47.674658+00:00_

1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	Text generated by large language models (LLMs) increasingly re-enters the web and seeds subsequent generation, producing recursive chains that progressively diverge from human-written text.
4	We study this phenomenon in base (pretrained) models and ask whether the drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Across eight base models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): features partition into drifting (Cohen's $d > 0.75$), intermediate, and near-stationary ($d < 0.10$) groups under standard decoding ($t \leq 0.7$), consistent with recursive generation shifting the NLL location while distributional shape remains stable.
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 (95\% CI [.688, .700]) under leave-one-generator-out evaluation, generalizing across model families.
7	The depth signal degrades substantially under instruction tuning, restricting current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-19T04:02:47.675004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1725 · 2026-05-19T04:02:48.126784+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	Characterizing the structure of this evolution is fundamental to understanding how base language models transform distributions under iterative conditioning, with relevance to understanding model collapse dynamics \cite{curse_of_recursion, self_consuming_mad}.
6	Yet binary detection decisions \cite{fast_detectgpt,binoculars,ld_score,detectgpt} obscure this structure: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and term this \emph{depth profiling}.
9	No existing method provides a feature-level decomposition of depth signal in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR) with a three-way partition: when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, three \emph{drifting} features (reference-model mean entropy, type-token ratio, hapax ratio) shift monotonically (Cohen's $d > 0.75$), one \emph{intermediate} feature (entropy std) shows a non-monotonic level shift ($d{=}0.55$), and three \emph{near-stationary} features (entropy max, tail decay, entropy min) exhibit negligible depth effects ($d < 0.10$).
12	This is consistent with recursive generation shifting the NLL location while distributional shape remains stable under fixed sampling parameters.
13	While distributional drift under recursive generation is documented in the model collapse literature \cite{curse_of_rec
…[truncated 1806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-19T04:02:48.127121+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-19T04:02:48.679446+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers that combine handcrafted features with neural architectures \cite{ghostbuster,feat_aug_transformer,abburi_multifaceted,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{tang2024science}, \citet{wu_survey_2025}, and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent work moves beyond binary detection along several axes.
11	\citet{beyond_binary} classify text into four roles (human-only, LLM-polished, LLM-expanded, LLM-only) via involvement measurement, discriminating production \emph{modes} rather than recursive depth.
12	\citet{two_birds} jointly detect machine-generated text and attribute it to specific LLMs, and \citet{beyond_final_actor} distinguish dual creator-editor roles across four production modes.
13	Multi-generator attribution, including generator-level classification in SemEval 2024 Task 8 Subtask B \cite{semeval2024_task8} and the DeFactify dataset \cite{defactify_dataset}, discriminates among different \emph{sources}.
14	All these approaches classify text by its production process or authorship, while our depth classification tracks how many recursive generation steps a text has undergone, an orthogonal axis.
15	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each capture
…[truncated 5156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-19T04:02:48.679814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-19T04:02:48.730424+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source te
…[truncated 8112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-19T04:02:53.377569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1731 · 2026-05-19T04:02:54.331355+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.764 under 5-fold CV.\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation. Sample-level CV is used because each chain contains multiple generators, making generator-level held-out splits inapplicable.}
14	Leave-one-family-out (LOFO) evaluation yields binary F1\,=\,0.686, confirming cross-family transfer.
15	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference model (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}).
16	Preliminary cross-domain evaluation suggests the signal persists with variation, though a domain$\times$temperature interaction exists (Appendix~\ref{app:domain}).
17	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 ($+$11.6\,pp; Appendix~\ref{app:qlora}), confirming that
…[truncated 10631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-19T04:02:54.331717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-19T04:02:54.482627+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) is consistent with a location/shape decomposition: under fixed temperature $\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration, while iterative conditioning shifts the input distribution's location as text becomes increasingly predictable to the reference model.
5	This interpretation is post-hoc and empirical; formal analysis of softmax output distribution dynamics under recursive conditioning remains an open problem.
6	DDR is an empirical decomposition capturing this dichotomy, not a claimed universal law of recursive generation.
7	DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.
8	Temperature and prompt-type ablations (\S\ref{sec:results-differential}) support this as a tendency rather than a guarantee: all four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp), and the signal varies across prompt types.
9	
10	Instruction tuning substantially weakens the signal across all three tested families (OLMo, Qwen, Llama; Appendix~\ref{app:instruct}).
11	Within-model 3-class F1 drops 3.7--19.9\,pp (OLMo: 0.575 vs.\ 0.754; Qwen: 0.732 vs.\ 0.769; Llama: 0.544 vs.\ 0.742), while binary F1 changes remain small ($\Delta \leq 3.2$\,pp), indicating that instruction tuning primarily disrupts the gen-0/gen-1 boundary.
12	Under cross-generator evaluation, the degradation is larger (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base).
13	Entropy-mean $\rho$ reverses sign consistently ($+0.48$ for OLMo and Qwen, $+0.23$ for Llama; all base models ${\approx}{-}0.6$), and 6 of 7 features reverse direction for OLMo and Qwen, 3 of 7 for Llama, consistent with instruction tuning shifting the generation attractor rather than destroying
…[truncated 1858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-19T04:02:54.884759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1735 · 2026-05-19T04:02:55.086155+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and identified a differential depth response (DDR) tri-partition across eight base-model generators from five families.
5	A 7-feature ensemble exploiting this tri-partition achieves leak-free binary F1\,=\,0.694 (LOGO) and 0.764 (cross-model chains).
6	Current applicability is restricted to base models; instruction tuning and larger scales remain open.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-19T04:02:55.136964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1737 · 2026-05-19T04:02:55.237901+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth profiling to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) and closed-source models remain untested; the consistent scale trend (Mistral-7B binary F1\,=\,0.633, lowest among all generators) suggests depth signal may weaken further at frontier scales, potentially approaching the detection floor.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type binary F1\,=\,0.781) compared to elaboration (0.730) and rewriting (0.737), with within-prompt-type paraphrastic chains showing weaker signal (binary F1\,=\,0.671 vs.\ 0.749 for within-prompt-type continuation).
16	DDR is most reliably detecte
…[truncated 3131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1738 · 2026-05-19T04:03:01.971659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1739 · 2026-05-19T04:03:02.373680+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-19T04:03:02.474464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table1.tex"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-19T04:03:03.328248+00:00_

1	%% NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.
2	\begin{table}[t]
3	\centering
4	\small
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Held-out Generator} & \textbf{Family} & \textbf{Params} & \textbf{Macro-F1} & \textbf{95\% CI} \\
8	\midrule
9	Pythia-2.8B   & Pythia  & 2.8B & ---   & --- \\
10	Pythia-1B     & Pythia  & 1.0B & 0.806 & --- \\
11	Qwen3-1.7B   & Qwen    & 1.7B & ---   & --- \\
12	Llama-3.2-3B & Llama   & 3.2B & ---   & --- \\
13	OLMo-2-1B    & OLMo    & 1.0B & ---   & --- \\
14	Qwen3-8B     & Qwen    & 8.0B & ---   & --- \\
15	Qwen3-0.6B   & Qwen    & 0.6B & ---   & --- \\
16	Mistral-7B   & Mistral & 7.0B & 0.681 & --- \\
17	\midrule
18	\textbf{Average (8-gen)} & & & \textbf{0.762} & [0.758, 0.766] \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-generator-out (LOGO) depth classification results (3-class).
22	Each row holds out one generator for testing and trains on the remaining seven.}
23	\label{tab:logo-results}
24	\end{table}
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-19T04:03:03.378897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table2.tex"
  }
}
```

</details>

---


### Tool result

_source line 1743 · 2026-05-19T04:03:03.830928+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{lp{3.2cm}ccc}
5	\toprule
6	\textbf{Feature Set} & \textbf{Features} & \textbf{LOGO F1} & \textbf{95\% CI} & \textbf{McNemar $p$} \\
7	\midrule
8	Full (7 features) & all & 0.773 & --- & --- \\
9	Surface only (2)  & TTR, hapax\_ratio & 0.688 & --- & $<$ 0.001 \\
10	Reference only (5) & entropy\_mean/std/min/max, tail\_decay & 0.713 & --- & $<$ 0.001 \\
11	\bottomrule
12	\end{tabular}
13	\caption{Feature group ablation and complementarity (8-gen 10-fold CV).
14	Both subsets significantly underperform the full set (+8.5\,pp, +5.9\,pp).
15	Permutation importance: \texttt{hapax\_ratio} (0.269) $>$ \texttt{entropy\_mean} (0.164) $>$ \texttt{ttr} (0.159).}
16	\label{tab:feature-ablation}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1744 · 2026-05-19T04:03:04.283160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "description": "Check references.bib size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
    "description": "Check references.bib size"
  }
}
```

</details>

---


### Tool result

_source line 1745 · 2026-05-19T04:03:04.687441+00:00_

552 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 1746 · 2026-05-19T04:03:04.687794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex"
  }
}
```

</details>

---


### Tool result

_source line 1747 · 2026-05-19T04:03:04.738248+00:00_

1	\section{Independent-Seed Control}
2	\label{app:seed-control}
3	
4	To rule out topic-level leakage from shared seeds across generators, we construct an independent-seed evaluation where Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap).
5	Each generator produces depth-0 through depth-4 chains on its own seed pool; features are extracted with the same Pythia-410M reference model.
6	We then train a 7-feature XGBoost classifier on one generator's data and test on the other, in both directions.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lcc}
12	\toprule
13	\textbf{Setting} & \textbf{Binary F1} & \textbf{95\% CI} \\
14	\midrule
15	Pythia-2.8B $\rightarrow$ OLMo-2-1B & 0.695 & [0.673, 0.717] \\
16	OLMo-2-1B $\rightarrow$ Pythia-2.8B & 0.666 & [0.643, 0.689] \\
17	\midrule
18	Independent-seed average & 0.680 & --- \\
19	Shared-seed LOGO (reference) & 0.694 & [0.688, 0.700] \\
20	\bottomrule
21	\end{tabular}
22	\caption{Independent-seed cross-generator evaluation (binary: gen-1 vs.\ gen-2+). Disjoint seed pools eliminate any possibility of topic-based leakage. The average independent-seed F1 (0.680) is within 1.4\,pp of the shared-seed LOGO baseline (0.694), confirming that the classifier captures generative degradation patterns rather than seed-specific topic content.}
23	\label{tab:seed-control}
24	\end{table}
25	
26	The small gap ($-$1.4\,pp) between independent-seed and shared-seed evaluation falls within bootstrap confidence intervals, and both directions individually exceed 0.66.
27	Combined with the seed-level demeaning control (\S\ref{sec:results-classification}), these results provide converging evidence that depth classification is driven by distributional properties of recursive generation, not topic identity.
28	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1748 · 2026-05-19T04:03:11.362336+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf 2>/dev/null | grep -E \"Pages|Title\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf 2>/dev/null | grep -E \"Pages|Title\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1749 · 2026-05-19T04:03:11.814750+00:00_

Title:           
Pages:           29

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1750 · 2026-05-19T04:03:12.266997+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1751 · 2026-05-19T04:03:13.221668+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1752 · 2026-05-19T04:03:13.975010+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex 2>/dev/null | grep -v \":0$\"",
  "description": "Count em-dash and en-dash occurrences across tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex 2>/dev/null | grep -v \":0$\"",
    "description": "Count em-dash and en-dash occurrences across tex files"
  }
}
```

</details>

---


### Tool result

_source line 1753 · 2026-05-19T04:03:14.025707+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex:1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-19T04:03:17.991921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex 2>/dev/null",
  "description": "Show lines with dash characters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex 2>/dev/null",
    "description": "Show lines with dash characters"
  }
}
```

</details>

---


### Tool result

_source line 1755 · 2026-05-19T04:03:18.846068+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex:1:% Abstract — Depth Profiling of Recursive LLM Generation Chains
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex:1:% Appendix — Length Confound Analysis
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex:1:% EMNLP 2026 ARR Submission — ACL 2023 Template

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-19T04:03:18.846409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
  }
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-19T04:03:19.198354+00:00_

1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{lrc}
8	\toprule
9	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
10	\midrule
11	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
12	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
13	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
14	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
15	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
16	\bottomrule
17	\end{tabular}
18	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
19	\label{tab:downstream}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 
…[truncated 3466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1758 · 2026-05-19T04:03:19.349322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex"
  }
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-19T04:03:19.349699+00:00_

1	\subsection*{Instruction-Tuned Model Results}
2	
3	Table~\ref{tab:instruct} summarizes depth classification under instruction tuning for three model families.
4	All results use within-model 5-fold CV on single-generator chains; LOGO evaluation is available for two models but uses earlier generator subsets (5--6 generators), so cross-model numbers are not directly comparable across rows.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Depth classification: base vs.\ instruction-tuned models (within-model 5-fold CV). $\rho$: Spearman correlation of entropy mean with depth. Rev.: number of features (out of 7) whose $\rho$ reverses sign under instruction tuning.}
10	\label{tab:instruct}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{lcc cc cc c}
13	\toprule
14	& \multicolumn{2}{c}{\textbf{3-class F1}} & \multicolumn{2}{c}{\textbf{Binary F1}} & \multicolumn{2}{c}{$\boldsymbol{\rho}$\textbf{(ent.\ mean)}} & \\
15	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
16	\textbf{Model} & Base & Instruct & Base & Instruct & Base & Instruct & \textbf{Rev.} \\
17	\midrule
18	OLMo-2-1B       & 0.754 & 0.575 & 0.845 & 0.813 & $-$0.64 & $+$0.48 & 6/7 \\
19	Qwen3-1.7B      & 0.769 & 0.732 & 0.861 & 0.875 & $-$0.60 & $+$0.48 & 6/7 \\
20	Llama-3.2-3B    & 0.742 & 0.544 & 0.849 & 0.838 & $-$0.63 & $+$0.23 & 3/7 \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	Instruction tuning degrades 3-class F1 by 3.7--19.9\,pp across all three families, while binary F1 (gen-1 vs.\ gen-2+) changes remain small ($|\Delta| \leq 3.2$\,pp).
26	The asymmetry indicates that instruction tuning primarily disrupts the gen-0/gen-1 boundary (human vs.\ first-generation), consistent with RLHF shifting the output distribution away from human-like text.
27	Entropy-mean $\rho$ reverses sign for all three models ($-0.60$--$-0.64$ base $\rightarrow$ $+0.23$--$+0.48$ instruct), and 6 of 7 features reverse for OLMo and Qwen vs.\ 3 of 7 for Llama.
28	This pattern is consistent with instruction
…[truncated 114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-19T04:03:29.640716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-19T04:03:30.145015+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf (2.7MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1762 · 2026-05-19T04:03:30.309413+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-19T04:03:30.410351+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\\n- Positioning: **Findings paper**（非 main conference long paper）\\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.764. Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\\n\\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while sha
…[truncated 3385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1764 · 2026-05-19T04:03:50.650736+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1765 · 2026-05-19T04:03:52.386731+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 26\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: p
…[truncated 1488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1735
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-19T04:03:52.538060+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/agent/*.yaml 2>/dev/null | head -20",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/agent/*.yaml 2>/dev/null | head -20",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1767 · 2026-05-19T04:03:52.588763+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1768 · 2026-05-19T04:03:58.667868+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
  "description": "Search for external review config across project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -10",
    "description": "Search for external review config across project"
  }
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-19T04:03:58.768604+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-19T04:04:42.907015+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查论文的 **方法严谨性、实验设计与统计推断**。\n\n## 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（PDF: `main.pdf`）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤ 8 页，ACL 模板 `[review]`，double-blind，Limitations 必须有，附录不要求审阅但建议检查\n\n## 你的审查侧重\n\n**重点审查以下方面**：\n\n1. **实验设计**:\n   - Gen-0 seed sharing 跨 generator 的 leakage 问题——论文声称 binary F1 (gen-1 vs gen-2+) 完全规避了此问题，是否成立？\n   - Independent-seed control 仅用 2 个 generator (Pythia-2.8B, OLMo-2-1B)，是否足以支撑泛化声明？\n   - LOGO 评估中同 family 不完全隔离（Pythia-1B held out 但 Pythia-2.8B 留在训练集），对 cross-family 泛化声明的影响\n   - 下游效用实验 n=3 seeds 的统计效力\n\n2. **统计推断**:\n   - DDR tri-partition 的统计基础：Cohen's d 阈值 (0.75, 0.10) 是否 principled？TOST 等价性检验的 margin 选择是否合理？\n   - 异方差条件下使用 pooled Cohen's d 的合理性（论文补充了 Glass's Δ，是否足够？）\n   - Bootstrap CI 方法和 Bonferroni 校正的适当性\n   - 3 个 drifting features 的高度相关性 (r=0.81-0.97)——是否本质上是同一 latent factor？论文的 PCA 分析是否充分回应？\n\n3. **方法论**:\n   - 7 features 的先验选择是否充分 motivated？是否有明显遗漏的特征类型（n-gram、syntactic）？\n   - XGBoost 超参数未调优——\"standard defaults\" 是否为公平比较？\n   - Baseline 对比的公平性：将 detection scores 作为单特征 vs 7-feature ensemble\n   - Reference model (Pythia-410M) 与生成器家族有架构重叠——cross-reference 实验是否充分消除此 confound？\n\n4. **可重复性**:\n   - 代码/数据承诺是否明确？\n   - 关键实验细节是否完整（prompt 模板、生成参数、chain break 处理）？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注严重程度: [Critical] / [Major] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 ARR 评分: 1-5 scale)\n7. **Confidence** (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查论文的 **方法严谨性、实验设计与统计推断**。\n\n## 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（PDF: `main.pdf`）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤ 8 页，ACL 模板 `[review]`，double-blind，Limitations 必须有，附录不要求审阅但建议检查\n\n## 你的审查侧重\n\n**重点审查以下方面**：\n\n1. **实验设计**:\n   - Gen-0 seed sharing 跨 generator 的 leakage 问题——论文声称 binary F1 (gen-1 vs gen-2+) 完全规避了此问题，是否成立？\n   - Independent-seed control 仅用 2 个 generator (Pythia-2.8B, OLMo-2-1B)，是否足以支撑泛化声明？\n   - LOGO 评估中同 family 不完全隔离（Pythia-1B held out 但 Pythia-2.8B 留在训练集），对 cross-family 泛化声明的影响\n   - 下游效用实验 n=3 seeds 的统计效力\n\n2. **统计推断**:\n   - DDR tri-partition 的统计基础：Cohen's d 阈值 (0.75, 0.10) 是否 principled？TOST 等价性检验的 margin 选择是否合理？\n   - 异方差条件下使用 pooled Cohen's d 的合理性（论文补充了 Glass's Δ，是否足够？）\n   - Bootstrap CI 方法和 Bonferroni 校正的适当性\n   - 3 个 drifting features 的高度相关性 (r=0.81-0.97)——是否本质上是同一 latent factor？论文的 PCA 分析是否充分回应？\n\n3. **方法论**:\n   - 7 features 的先验选择是否充分 motivated？是否有明显遗漏的特征类型（n-gram、syntactic）？\n   - XGBoost 超参数未调优——\"standard defaults\" 是否为公平比较？\n   - Baseline 对比的公平性：将 detection scores 作为单特征 vs 7-feature ensemble\n   - Reference model (Pythia-410M) 与生成器家族有架构重叠——cross-reference 实验是否充分消除此 confound？\n\n4. **可重复性**:\n   - 代码/数据承诺是否明确？\n   - 关键实验细节是否完整（prompt 模板、生成参数、chain break 处理）？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注严重程度: [Critical] / [Major] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 ARR 评分: 1-5 scale)\n7. **Confidence** (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-19T04:05:01.972622+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19065
}
```

</details>

---


### Tool call

_source line 1772 · 2026-05-19T04:05:02.140501+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查论文的 **新颖性、完整性、写作质量与格式合规**。\n\n## 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（PDF: `main.pdf`）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤ 8 页，ACL 模板 `[review]`，double-blind，Limitations 必须有，附录不要求审阅但建议检查\n- **ARR 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**重点审查以下方面**：\n\n1. **新颖性与贡献**:\n   - \"Generation depth classification\" 作为新任务的价值——是否真正填补了 gap，还是 niche 问题？\n   - DDR tri-partition 作为 \"empirical rather than methodological\" 贡献的充分性——对 EMNLP 而言是否有足够的 insight？\n   - 与两篇 concurrent works (Broken Telephone, Markovian Chains) 的区分是否有说服力？\n   - 限制在 base models 对 significance 的影响——web text 主要由 instruct models 产生\n\n2. **Related Work 覆盖与定位**:\n   - 引用是否充分（当前 ~40 篇）？\n   - 是否有重要遗漏（特别是 ordinal classification、data contamination detection、self-training 领域）？\n   - Positioning 是否清晰——本文与 AI text detection、model collapse、stylometry 三个领域的关系\n\n3. **写作质量**:\n   - Abstract/Introduction 的故事线是否连贯有吸引力？\n   - 专有名词首次出现是否有定义？\n   - 是否存在 AI 写作风格标志（em-dash、-ing phrases、过度分段、禁用词）？\n   - 段落/句式是否自然流畅？\n   - 主线统一性：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否一致？\n\n4. **格式合规**:\n   - 正文是否 ≤ 8 页？\n   - 模板是否正确（`\\usepackage[review]{acl}`）？\n   - 匿名化是否到位（无作者信息泄露）？\n   - 图表字体是否 ≥ 7pt？信息密度是否足够？\n   - Limitations section 是否充分？\n   - Ethics Statement 是否充分？\n\n5. **叙事结构**:\n   - Contribution list 是否每条都有对应的 section/evidence 支撑？\n   - 附录内容是否在正文中有引用且融入叙事？\n   - 数据是否服务于叙事推进（vs 堆砌）？\n   - Conclusion 是否与 Introduction 的 promise 对应？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注严重程度: [Critical] / [Major] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 ARR 评分: 1-5 scale，参照上述标准)\n7. **Confidence** (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查论文的 **新颖性、完整性、写作质量与格式合规**。\n\n## 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`（PDF: `main.pdf`）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: 正文 ≤ 8 页，ACL 模板 `[review]`，double-blind，Limitations 必须有，附录不要求审阅但建议检查\n- **ARR 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**重点审查以下方面**：\n\n1. **新颖性与贡献**:\n   - \"Generation depth classification\" 作为新任务的价值——是否真正填补了 gap，还是 niche 问题？\n   - DDR tri-partition 作为 \"empirical rather than methodological\" 贡献的充分性——对 EMNLP 而言是否有足够的 insight？\n   - 与两篇 concurrent works (Broken Telephone, Markovian Chains) 的区分是否有说服力？\n   - 限制在 base models 对 significance 的影响——web text 主要由 instruct models 产生\n\n2. **Related Work 覆盖与定位**:\n   - 引用是否充分（当前 ~40 篇）？\n   - 是否有重要遗漏（特别是 ordinal classification、data contamination detection、self-training 领域）？\n   - Positioning 是否清晰——本文与 AI text detection、model collapse、stylometry 三个领域的关系\n\n3. **写作质量**:\n   - Abstract/Introduction 的故事线是否连贯有吸引力？\n   - 专有名词首次出现是否有定义？\n   - 是否存在 AI 写作风格标志（em-dash、-ing phrases、过度分段、禁用词）？\n   - 段落/句式是否自然流畅？\n   - 主线统一性：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否一致？\n\n4. **格式合规**:\n   - 正文是否 ≤ 8 页？\n   - 模板是否正确（`\\usepackage[review]{acl}`）？\n   - 匿名化是否到位（无作者信息泄露）？\n   - 图表字体是否 ≥ 7pt？信息密度是否足够？\n   - Limitations section 是否充分？\n   - Ethics Statement 是否充分？\n\n5. **叙事结构**:\n   - Contribution list 是否每条都有对应的 section/evidence 支撑？\n   - 附录内容是否在正文中有引用且融入叙事？\n   - 数据是否服务于叙事推进（vs 堆砌）？\n   - Conclusion 是否与 Introduction 的 promise 对应？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注严重程度: [Critical] / [Major] / [Minor])\n4. **Questions** (需要作者回答的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (使用 ARR 评分: 1-5 scale，参照上述标准)\n7. **Confidence** (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1773 · 2026-05-19T04:05:03.697789+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1557
}
```

</details>

---


### Assistant

_source line 1774 · 2026-05-19T04:05:14.089738+00:00_

Round 1 审稿任务已分配：
- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计推断
- **Reviewer 2** → 新颖性 + 完整性 + 写作质量 + 格式合规

等待两位 Reviewer 的独立审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 158

## Round 158

2 recorded events


### User

_source line 1775 · 2026-05-19T04:12:21.611083+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 1
### 审查侧重：方法严谨性、实验设计与统计推断

---

## Summary

本文提出 generation depth classification：给定一段文本，判断它经历了多少轮 LLM 递归生成（gen-0 人类 / gen-1 / gen-2+）。作者设计了 7 个手工特征（5 个参考模型特征 + 2 个表面词汇多样性特征），用 XGBoost 在 8 个 base model generator（5 个家族）上进行 LOGO 评估，并提出 Differential Depth Response (DDR) 框架将特征分为 drifting/intermediate/near-stationary 三类。Binary LOGO F1 = 0.694，cross-model F1 = 0.764。任务定义新颖，实验覆盖面广，但 DDR 统计基础和下游实验的统计效力存在显著问题。

---

## Strengths

**S1. 新颖且有实际意义的任务定义。** 超越 binary real-vs-synthetic detection，将生成深度作为分类目标，与 model collapse（Shumailov et al., 2024）、数据溯源（Longpre et al., 2024）有清晰关联。这是一个之前未被正式定义的研究问题。

**S2. 评估协议严谨且透明。** LOGO + LOFO 双重评估，8 个 generator 跨 5 个家族，配套多项控制实验：independent-seed (§S)、length matching (§B)、cross-domain (§J)、cross-temperature (§O)、prompt type sensitivity (§C)。这个实验覆盖度在 EMNLP 投稿中属上乘。

**S3. 可解释的方法设计。** 7 个手工特征完全透明可分析，DDR 框架（尽管有统计问题，见 N2）为理解递归生成下文本属性的演化提供了有用的概念结构。对比 QLora end-to-end 方法 (§E, Table 6) 进一步验证了手工特征的价值。

**S4. 诚实的自我评估。** 论文主动标注 gen-0 seed sharing 问题（§3.2, Table 1 caption）、下游 n=3 的局限（§L）、QLora 天花板与手工特征的 tradeoff (§E)。这种学术诚实度值得肯定。

**S5. 附录消融覆盖全面。** Feature ablation (§P), classifier comparison (§H), perturbation robustness (§I), cross-domain (§J), confusion matrix (§G), error analysis (§K), per-generator TOST equivalence (§T) — 附录的深度和广度远超平均水平。

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] **下游效用实验 (§L/§4.3) n=3 seeds 严重欠缺统计效力**

- **具体位置**: §4.3 (p.8), Appendix L (p.19-20), Table 16
- **问题**: 论文将"depth-aware data curation improves downstream LM quality"列为贡献之一（Abstract, Introduction contribution 3），但训练 OLMo-2-0.425-1B 仅用 3 个随机种子。论文自己承认 pooled SD < 0.001 导致 "artificially inflating d"，Cohen's d 值 "appear large but are unreliable"（p.20）。具体而言：
  - n=3 时 TOST 等价性检验的 power 极低——发现"等价"可能仅因检测不到真实差异
  - 方差估计本身的 95% CI 在 df=2 时极宽，无法可靠估计变异性
  - cross-seed SD < 0.002 这个"可重复性"结论同样不可靠
- **为什么影响接收**: 下游应用是论文三大贡献之一，也是连接学术发现与实际价值的关键桥梁。n=3 无法支撑 "practically indistinguishable downstream quality" 的声明。
- **建议修改方向**: (a) 增加至 ≥20 seeds（如受计算限制可缩短训练或用更小模型），或 (b) 将下游实验降格为 preliminary/pilot evidence，从 contributions 列表移除，并在 Limitations 中明确标注。

**N2** [Critical] **DDR tri-partition 阈值 (§4.2) 缺乏 principled 依据**

- **具体位置**: §4.2 (p.6), Appendix V
- **问题**: DDR 的核心贡献是基于 Cohen's d 的三分法（drifting: d > 0.75; near-stationary: d < 0.10; TOST margin ±2%）。这些阈值直接决定了论文的"key finding"（Abstract），但：
  - 0.75 介于 Cohen 惯例 "medium"（0.5）和 "large"（0.8）之间，未说明为何选此特定值
  - ±2% relative margin 未从领域知识或先验工作推导
  - 敏感性分析（§4.2）仅检验了 near-stationary 边界（0.10-0.16），未检验 drifting 边界——若使用 0.5，entropy_max (d=0.55) 将从 intermediate 重新分类为 drifting，根本性改变 DDR 叙事
  - "Data-driven clustering confirms the primary drifting/non-drifting split" 的表述暗示聚类验证了阈值，但聚类本身也依赖距离度量的选择
- **为什么影响接收**: DDR 是论文的概念核心——如果三分法是阈值选择的 artifact 而非数据的 robust property，框架的贡献就大打折扣。
- **建议修改方向**: (a) 对 drifting 阈值做完整敏感性分析（0.3-1.0 范围），展示哪些分类在不同阈值下保持稳定；(b) 用 data-driven 方法（如 gap statistic, silhouette analysis）取代固定阈值；(c) 如果 entropy_max 在合理阈值范围内不断在 intermediate/drifting 之间切换，诚实报告这一点。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] **三个 "drifting" 特征本质是同一潜在因子**

- **具体位置**: §4.2 (p.6), Appendix Q (p.27)
- **问题**: entropy mean、TTR、hapax ratio 相关性 r=0.81-0.97。PCA 分析（§Q）确认它们形成 "tightly coupled cluster"。LOFO 分析（§F, Table 7）显示移除任何单个 drifting 特征仅造成 0.2-1.5pp 退化，与高冗余一致。但论文叙事反复强调 "three drifting features" 作为 "rich feature drift" 的证据，涵盖 "both semantic and distributional" 维度（§5）。
- **建议**: 更诚实的 framing 应是：一个 latent 词汇多样性/entropy 因子单调漂移，而非三个独立维度。DDR 的 3/1/3 划分在独立信息维度上更接近 1/1/3。

**W2** [Major] **参考模型 confound 部分未解决**

- **具体位置**: §3.3, Appendix R (Table 21), §9 (p.9)
- **问题**: Pythia-410M 与 2 个 generator（Pythia-1B, Pythia-2.8B）同架构。Cross-reference 实验（Table 21）显示 LOGO F1 从 0.694 降至 ~0.613（OLMo/Qwen reference），降幅 8pp (12% relative)。论文承认 "reference model calibration is critical for cross-domain deployment"（p.9），但 §4 主结果和 Table 1 仍全部使用 Pythia-410M。
- **建议**: 在 Table 1 旁边报告 reference-neutral F1（如三个 reference 模型的平均），或在 §4.1 显著标注 0.694 包含 reference-alignment 成分。

**W3** [Major] **Independent-seed 控制覆盖面不足**

- **具体位置**: Appendix S (Table 22)
- **问题**: 仅用 2/8 generators（Pythia-2.8B, OLMo-2-1B）做了 disjoint seed 实验。F1 差距可忽略（0.693 vs 0.694），但这只覆盖 2/5 家族。Qwen（3 个变体）、Llama、Mistral 的 seed sharing 效应未验证。§3.2 中 "seed sharing doesn't affect the evaluation" 的声明建立在 25% generator 样本上。
- **建议**: 至少为每个家族各选一个 generator 做 independent-seed 控制。

**W4** [Major] **LOGO 评估中同家族泄漏未在主表中体现**

- **具体位置**: Table 1 (p.6), §4.1 (p.5)
- **问题**: 8-generator LOGO 中，hold out Pythia-1B 时 Pythia-2.8B 仍在训练集中，Qwen 变体同理。LOFO binary F1 = 0.686 vs LOGO 0.694（§4.1），仅差 0.8pp，说明泄漏不严重。但所有主要声明（Abstract, §4）基于 LOGO 而非 LOFO。
- **建议**: 在 Table 1 中同时报告 LOFO F1，或将 LOFO 作为声明 cross-generator generalization 的主要依据。

---

## 小问题（不影响接收）

**M1** [Minor] **未探索 n-gram 和句法特征。** 7 个特征覆盖参考模型统计量和词汇多样性，但未讨论为何排除 n-gram 重复模式、句法复杂度（依存句法深度、POS 分布）等标准文本分析特征（§3.3）。即使是否定结果也能加强特征选择的 justification。

**M2** [Minor] **Baseline 对比不对称。** Detection scores（FastDetectGPT, Binoculars, LD-Score）作为单特征输入 XGBoost（Table 2），而 proposed method 用 7 特征。4-detector ensemble（"4-det. + surface"）是更公平的对比但仅简短提及。

**M3** [Minor] **Pooled Cohen's d 异方差问题仅在附录讨论。** §4.2 主文仅报告 pooled d，Glass's Δ 分析在 Appendix V。异方差条件下 pooled d 可能偏估，建议在主文添加一句 caveat 并引用附录。

**M4** [Minor] **引用验证结果。** 68 条引用全部匹配（无孤立/缺失），54 条在线验证通过，9 条未找到（含 DetectGPT、Pythia、XGBoost 等知名工作，可能为 OpenAlex 索引问题），5 条轻微 mismatch。引用覆盖基本充分，但缺少关于 stylometric machine text fingerprinting 的工作（如 syntactic complexity 作为 fingerprint）来 contextualize 特征选择。

---

## Questions for Authors

**Q1.** 若将 drifting 阈值从 0.75 降至 Cohen's conventional "medium"（0.5），entropy_max (d=0.55) 是否重新分类为 drifting？这将如何改变 DDR 的三分叙事？

**Q2.** 下游实验为何仅用 3 seeds？是否有计算限制？能否用更小模型或更短训练增加至 ≥20 seeds 以获得足够统计效力？

**Q3.** 跨参考模型 F1 降幅（0.694→0.613）显著。若取三个参考模型（Pythia-410M, OLMo, Qwen）的平均 LOGO F1，"reference-neutral"性能是多少？

**Q4.** 是否考虑将 LOFO 作为主要评估指标？考虑到同家族泄漏，LOFO (F1=0.686) 仅比 LOGO (0.694) 低 0.8pp，且完全避免了 family leakage。

**Q5.** 三个高度相关的 drifting 特征（r=0.81-0.97）：若替换为其第一主成分，分类性能是否变化？这能直接检验它们是否携带独立信息。

---

## Missing References

无关键遗漏。68 条引用覆盖直接竞争方法、基础工作和评估方法论。轻微缺口：缺少 stylometric AI text detection 工作的引用（如从句法复杂度角度的 fingerprinting），可用于 contextualize §3.3 的特征选择。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心分类实验有 LOGO/LOFO 支撑，但 DDR 阈值缺乏 principled 依据（N2），下游 n=3 严重 underpowered（N1），参考模型 confound 8pp 未充分解决（W2） |
| Excitement | 3.5/5 | 任务定义新颖且连接实际问题（model collapse/provenance），但当前 F1=0.694 限制实用性，方法（手工特征+XGBoost）技术新颖性有限 |
| Reproducibility | 4/5 | 实验细节完整（prompt 模板 §3.2, 生成参数, chain break 处理），承诺开源，但代码/数据未随投稿提交 |

---

## Overall Assessment

**Overall**: **3.0 (Findings)**

**一句话总结**: 论文定义了一个新颖且有意义的任务，实验覆盖面广且分析诚实透明，但核心 DDR 框架的统计基础不够严谨（阈值任意性、drifting 特征高共线性），下游实验 n=3 无法支撑贡献声明，参考模型 confound 导致主结果可能高估 ~8pp——整体达到 Findings 水准，修复 N1/N2 后有潜力升至 3.5。

**Confidence**: **4/5** — 对统计方法（效应量、等价性检验、特征相关性分析）和文本分类实验设计有扎实理解；对 base LLM 递归生成链的文献覆盖面略有不确定性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1776 · 2026-05-19T04:12:29.368472+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 159

## Round 159

6 recorded events


### User

_source line 1777 · 2026-05-19T04:12:32.051259+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains

## Summary

本文提出 generation depth classification 任务：将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（递归生成），取代传统的二分类检测。通过 7 个手工特征（5 个参考模型 NLL 统计量 + 2 个表面词汇多样性特征）和 XGBoost 分类器，在 8 个 base model（5 个模型家族，0.6B–8B 参数）上实现 LOGO binary F1=0.694。核心发现是 differential depth response (DDR)：特征自然分为 drifting（entropy mean, TTR, hapax ratio）、intermediate（entropy std）和 near-stationary（entropy max, tail decay, entropy min）三组。作者诚实地定位贡献为"empirical rather than methodological"。

## Strengths

**S1. 任务定义新颖且方向正确。** 从 binary real-vs-synthetic 推进到 ordinal depth classification 是一个有意义的方向扩展，对数据溯源（data provenance）有实际价值。task formulation 清晰，形式化合理（Section 3.1）。

**S2. 实验设计严谨，控制变量充分。** LOGO（leave-one-generator-out）+ LOFO（leave-one-family-out）+ seed-sharing control + length-matched subsampling + independent-seed experiment 构成了非常完善的控制体系。论文系统性地排除了 seed overlap（F1=0.680 independent seed）、length confound（F1=0.724 length-matched）等混淆因素，这在 empirical 论文中是高标准的做法。

**S3. DDR 发现本身有一定洞察价值。** 特征自然分为 drifting/intermediate/near-stationary 三组，且通过多种独立指标（Spearman ρ、Cohen's d、KS statistic、Levene test、CV shift）交叉验证，并用 TOST equivalence testing 和 holdout validation 确认稳定性（Appendix V）。这种 location-shifts-but-shape-persists 的经验观察有助于理解递归生成的分布演化。

**S4. 论文诚实透明。** 作者主动标注贡献为 empirical、明确承认 base model 限制、在 Limitations 中详尽列出 8 项局限（包括 instruct model degradation、scale ceiling、prompt-type dependency 等）。这种诚实的学术态度值得肯定。

**S5. 附录详尽。** 20+ 页附录涵盖 16 个实验板块（dataset stats、confusion matrix、classifier sensitivity、robustness to perturbation、cross-domain、cross-temperature、downstream utility 等），展现了系统性的实验覆盖。

**S6. 与 concurrent work 的定位清晰。** Related Work Section 2.2 对 Broken Telephone 和 Markovian Chains 的区分（paraphrastic vs. continuation chains；三个独立工作收敛于 ~3 class ceiling 的讨论）有说服力。

## Weaknesses

**W1 [Critical] Base model 限制严重削弱论文的 significance 和实际价值。**
- 具体位置：Section 5 (Discussion)、Limitations、Appendix K
- 问题：论文明确承认 instruction tuning 后深度信号"degrades substantially"：OLMo-2-1B-Instruct LOGO F1 从 0.763 暴跌至 0.338（Section 5, line 12），Llama 3-class F1 从 0.742 降至 0.544。现实中 web text 几乎全部由 instruct/RLHF 模型生成，base model 直接生成的文本在实际场景中极为罕见。
- 为什么影响接收：EMNLP 审稿标准强调 "impact" 和 "significance"。一个只在 base model 上有效、面对真实场景（instruct model）性能大幅退化的方法，其研究价值受限于一个实践中几乎不存在的场景。论文在 Introduction（line 14）说"We restrict to base (pretrained) models, since instruction-tuning introduces confounds that obscure this intrinsic mechanism"，但这本质上是将核心限制框架为设计选择。
- 建议：需要更有力地论证 base-model depth profiling 的实际应用场景（不仅是理论兴趣），或者提供 instruct model 上的初步路线图，说明如何克服当前的失效模式（如 entropy mean ρ 反转）。

**W2 [Major] DDR 作为 EMNLP 贡献可能偏薄——本质上是特征分析。**
- 具体位置：Section 4.2, Section 5 (Discussion lines 1-6)
- 问题：DDR tri-partition 的核心发现是"7 个手工特征中，有些随深度漂移，有些不漂移"。这是一个有用的经验观察，但 (1) 作者自己承认 "This interpretation is post-hoc and empirical" (Section 5, line 5)，没有理论解释；(2) 特征集仅 7 个，且 TTR 和 hapax ratio 高度相关（r=0.97, Section 4.2 line 81），实质上是 ~5-6 个独立特征；(3) 对 "为什么 location 漂移而 shape 不漂移" 的解释停留在推测层面（"softmax output distribution dynamics under recursive conditioning remains an open problem", Section 5 line 5）。
- 为什么影响评分：对于 EMNLP main conference 而言，纯 empirical 贡献需要足够令人惊讶或有深度的 insight 来补偿缺乏方法论创新。DDR 发现虽然有趣，但基本上是 "some features are more sensitive to recursive generation than others" 的系统化表述。
- 建议：可以通过 (a) 提供 DDR 的理论推导或至少更严谨的 mechanistic explanation；(b) 展示 DDR 如何 inform 新的方法设计（beyond XGBoost feature selection）；(c) 更深入地分析 DDR 的边界条件，来增强贡献的深度。

**W3 [Major] 主要性能指标 F1=0.694 偏低，限制了 contribution claim 的说服力。**
- 具体位置：Table 1, Section 4.1
- 问题：Leak-free binary F1=0.694 意味着在 gen-1 vs. gen-2+ 的核心判别任务上，分类器的错误率约 30%。per-generator 最低为 Mistral-7B 的 0.633。虽然论文在 Section 4.3 中合理地将 baseline 对比定位为 "contextualize" 而非 "claim advantage"，但 QLoRA 端到端方法在 Appendix E 中达到 3-class F1=0.905（+11.6pp），说明 7 特征集本身远非最优。
- 为什么影响评分：moderate 性能+base-model-only+empirical-only 贡献，三者叠加使得论文的总体 impact 受限。
- 建议：(1) 更明确地讨论 7 特征 vs. QLoRA 的 trade-off（interpretability vs. accuracy）——当前 QLoRA 只在附录中简要提及，给人的印象是将更好的结果"藏"在附录；(2) 考虑将 QLoRA 结果提升到正文讨论的更突出位置。

**W4 [Major] Contribution 列表中第 3 条（parameter dependence）是 negative result，定位不当。**
- 具体位置：Introduction, Contribution #3（line 22）
- 问题：第 3 条贡献写的是 "DDR's parameter dependence: instruction tuning reverses feature drift direction" 和 "depth signal degrades at t=0.9"。这本质上是在说方法在某些条件下失效。将 negative result 列为 contribution 在逻辑上不自洽——它更适合放在 Discussion/Limitations 中（实际上确实也在那里讨论了），而不是作为贡献宣称。
- 建议：重新框架为 "We characterize DDR's boundary conditions, establishing validity within specific parameter regimes" 或类似正面表述；或者减少到 2 条贡献，将参数敏感性分析作为 Discussion 的一部分。

**W5 [Minor] Abstract 中引用了过多具体数字。**
- 具体位置：Abstract（lines 5-7）
- 问题：Abstract 在约 150 词的篇幅内包含了 Cohen's d > 0.75、d < 0.10、t ≤ 0.7、F1=0.694、CI [.688, .700] 等大量数字。根据写作规范，Abstract 最多引用 2-3 个关键数字。当前的数字密度使 Abstract 读起来更像 Results 的压缩版而非独立的叙事单元。
- 建议：保留 F1=0.694 和一个核心效应量（如 "six-fold effect-size gap"），删除其他具体数值，代之以定性描述。

**W6 [Minor] Figure 1 信息密度不足。**
- 具体位置：Figure 1（p.6）
- 问题：Figure 1 展示 7 个特征的 Spearman correlation strip plot，但这些数值在正文（Section 4.2）中已经文字描述了。图本身的附加信息有限——只是将正文数字可视化。对于受限的正文页面空间（8 页），一个仅展示 7 个数字的图占用了约 1/4 页的空间。
- 建议：可以考虑 (a) 将此图合并到更信息密集的组合图中，(b) 改为展示 per-generator 的 DDR 分布（当前在 Appendix N 的 violin plot 中），或 (c) 用 inline table 替代。

**W7 [Minor] Related Work 中 ordinal classification 文献覆盖不足。**
- 具体位置：Section 2.1（line 16）
- 问题：论文将 task 框架为 ordinal classification（Section 3.1, line 10），并在 Related Work 中引用了 3 篇 ordinal classification 方法（CORAL, CORN, Frank-Hall），但没有在 Section 2 设置独立的 ordinal classification 子章节来讨论 ordinal regression/classification 的更广泛文献。既然 ordinal 视角是论文定位的核心要素之一（与 binary detection 的区别），这方面的 positioning 应当更充分。
- 建议：增加简短段落讨论 ordinal classification 的一般框架和在 NLP 中的应用（如 sentiment ordinal classification），说明 depth classification 的 ordinal 性质如何影响方法选择和评估。

**W8 [Minor] 部分附录实验的样本量偏小，统计效力不足。**
- 具体位置：Appendix L (Downstream Utility)
- 问题：下游实验仅 n=3 seeds，Table 16 的 TOST 结果 p=0.020（marginal），且作者自己说 "requires validation at larger scale"（Section 5, line 17）。将此列入附录是合理的，但当前的结论 ("depth composition does not determine training utility") 基于不充分的统计证据，表述应更谨慎。
- 建议：更明确标注为 preliminary/pilot experiment，避免基于 n=3 做定性结论。

## Questions

**Q1.** 请具体描述 base-model depth profiling 的实际部署场景。在什么现实应用中，人们需要判断文本经历了多少代 base model 递归生成？

**Q2.** QLoRA 端到端模型（F1=0.905）在 instruct model 上的表现如何？它是否能部分克服 W1 中描述的 base model 限制？如果是，为什么不将其作为主要方法之一？

**Q3.** DDR 的 "location shifts but shape persists" 解释在直觉上是有意义的，但能否提供更形式化的分析？例如，能否证明在 top-p sampling 下，softmax 分布的高阶矩（方差、峰度）在递归条件化下有界？

**Q4.** Cross-model chains (F1=0.764) 的性能高于 single-generator LOGO (F1=0.694)——这是否说明 depth signal 在 generator 混合时反而更强？如果是，这对 DDR 的解释有什么影响？

**Q5.** Figure 1 中 entropy_min 的 Spearman ρ 较高（看起来约 -0.4），但它被归为 near-stationary。Section 4.2 line 71 解释这是因为变化集中在 gen-0/gen-1 boundary。能否提供 gen-1 vs. gen-2+ 的单独 correlation 来直接支持这一分类？

## Missing References

1. **Ordinal classification in NLP**: 论文引用了 CORAL/CORN/Frank-Hall 三个通用方法，但缺少 ordinal classification 在 NLP 任务中的应用文献（如 sentiment analysis 中的 ordinal approaches）。

2. **Self-training literature**: 仅引用 self-rewarding LMs 和 SPIN 两篇。建议补充 STaR (Zelikman et al., 2022) 等 self-training 方法，因为这些方法也产生迭代生成链。

3. **Distribution shift / domain adaptation**: DDR 本质上是一种 distribution shift 现象，但没有引用 distribution shift detection 的文献（如 dataset shift、covariate shift）。

4. **N-gram based detection methods**: 论文提到 "Simpler features (character or word n-gram frequencies) were not explored"（Limitations line 31），但也没有引用 n-gram 基于的检测方法文献。

## Overall Assessment

**Overall: 3.0 (Findings)**

**一句话总结**: 论文提出了一个新颖且方向正确的 task formulation（depth classification），并以严谨的实验设计支撑了一个有趣的 empirical 发现（DDR），但 base-model-only 限制严重削弱了实际 significance，performance 偏低，且 DDR 作为核心贡献缺乏理论深度。

**打分理由**: 
- 任务定义的新颖性和实验的严谨性使论文达到 Findings 水准
- 但 base-model 限制（W1, Critical）是最大障碍：一个在主要应用场景（instruct models）中失效的方法难以支撑 main conference 接收
- 性能偏低（W3）+ 贡献偏 empirical（W2）进一步削弱了 excitement
- 如果能提供 instruct model 上的可行路线或 DDR 的理论解释，可升至 3.5

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨，控制变量充分（LOGO/LOFO/seed control/length matching），统计方法恰当（bootstrap CI, McNemar, Bonferroni correction, TOST）。无明显方法论缺陷。 |
| Excitement | 2.5/5 | 任务新颖但 niche；base-model 限制使得实际影响有限；DDR 是有趣但非惊人的 empirical 发现。 |
| Reproducibility | 4/5 | 承诺开源代码/数据/模型；实验细节充分（hyperparams, compute budget, software versions）；唯一不确定性是 chain generation 的随机性。 |
| Clarity | 4/5 | 写作清晰专业，叙事连贯；Related Work positioning 好；Limitations 诚实详尽。少数信息密度问题（Abstract 数字过多, Figure 1 不够紧凑）。 |
| Overall | 3.0/5 | Findings 水准。新颖任务 + 严谨实验 + 有趣发现，但 base-model 限制 + 偏低性能 + 缺乏理论深度制约了 excitement。 |

## Confidence

**Confidence: 4/5** — 对 AI-generated text detection、distributional analysis 和 ordinal classification 文献较为熟悉。对 model collapse 和 inference-chain dynamics 的理论基础了解中等。审阅了全文（含 20+ 页附录）并核查了引用。


---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。

两个 Critical 问题：
1. **下游实验 n=3 严重 underpowered** — 论文将 depth-aware curation 列为贡献之一，但 3 个种子无法支撑等价性声明
2. **DDR 阈值缺乏 principled 依据** — drifting/near-stationary 的 Cohen's d 切点（0.75/0.10）未做敏感性分析，entropy_max 在合理阈值范围内分类不稳定

四个 Major 问题涉及 drifting 特征高共线性（r=0.81-0.97 本质是同一 latent factor）、参考模型 confound（cross-reference F1 降 8pp）、independent-seed 仅覆盖 2/8 generator、LOGO 同家族泄漏未在主表体现。

论文优势在于任务定义新颖、评估协议严谨透明、附录消融覆盖全面。修复 N1/N2 后有潜力升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-19T04:13:11.762141+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n### 审查侧重：方法严谨性、实验设计与统计推断\n\n## Summary\n\n本文提出 generation depth classification：给定一段文本，判断它经历了多少轮 LLM 递归生成（gen-0 人类 / gen-1 / gen-2+）。作者设计了 7 个手工特征（5 个参考模型特征 + 2 个表面词汇多样性特征），用 XGBoost 在 8 个 base model generator（5 个家族）上进行 LOGO 评估，并提出 Differential Depth Response (DDR) 框架将特征分为 drifting/intermediate/near-stationary 三类。Binary LOGO F1 = 0.694，cross-model F1 = 0.764。任务定义新颖，实验覆盖面广，但 DDR 统计基础和下游实验的统计效力存在显著问题。\n\n## Strengths\n\n**S1. 新颖且有实际意义的任务定义。**\n**S2. 评估协议严谨且透明。**\n**S3. 可解释的方法设计。**\n**S4. 诚实的自我评估。**\n**S5. 附录消融覆盖全面。**\n\n## Must-Fix 问题\n\n**N1** [Critical] **下游效用实验 (§L/§4.3) n=3 seeds 严重欠缺统计效力**\n- n=3 时 TOST 等价性检验的 power 极低——发现\"等价\"可能仅因检测不到真实差异\n- 方差估计本身的 95% CI 在 df=2 时极宽\n- 建议：增加至 ≥20 seeds 或将下游实验降格为 preliminary evidence，从 contributions 列表移除\n\n**N2** [Critical] **DDR tri-partition 阈值 (§4.2) 缺乏 principled 依据**\n- 0.75 介于 Cohen 惯例 \"medium\"（0.5）和 \"large\"（0.8）之间，未说明为何选此特定值\n- 敏感性分析仅检验 near-stationary 边界，未检验 drifting 边界——若使用 0.5，entropy_std (d=0.55) 将从 intermediate 重新分类为 drifting\n- 建议：对 drifting 阈值做完整敏感性分析（0.3-1.0），或用 data-driven 方法取代固定阈值\n\n## Should-Fix 问题\n\n**W1** [Major] **三个 drifting 特征本质是同一潜在因子**（r=0.81-0.97，PCA 92.3% variance by PC1）\n**W2** [Major] **参考模型 confound 部分未解决**（cross-reference F1 从 0.694 降至 ~0.613，降幅 8pp）\n**W3** [Major] **Independent-seed 控制仅覆盖 2/8 generators**\n**W4** [Major] **LOGO 同家族泄漏未在主表中体现**（LOFO 0.686 vs LOGO 0.694）\n\n## 小问题\n**M1** 未探索 n-gram 和句法特征\n**M2** Baseline 对比不对称（单特征 vs 7 特征）\n**M3** Pooled Cohen's d 异方差问题仅在附录讨论\n**M4** 缺少 stylometric machine text fingerprinting 文献引用\n\n## Questions\n**Q1.** 若 drifting 阈值降至 0.5，entropy_std (d=0.55) 是否重分类？\n**Q2.** 下游实验为何仅 3 seeds？\n**Q3.** 三参考模型平均 \"reference-neutral\" F1 是多少？\n**Q4.** 是否考虑将 LOFO 作为主要指标？\n**Q5.** 三个 drifting 特征替换为 PC1 后性能变化？\n\n## Overall Assessment\n**3.0 (Findings)**，Soundness 3/5，Excitement 3.5/5，Reproducibility 4/5\nConfidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n### 审查侧重：方法严谨性、实验设计与统计推断\n\n## Summary\n\n本文提出 generation depth classification：给定一段文本，判断它经历了多少轮 LLM 递归生成（gen-0 人类 / gen-1 / gen-2+）。作者设计了 7 个手工特征（5 个参考模型特征 + 2 个表面词汇多样性特征），用 XGBoost 在 8 个 base model generator（5 个家族）上进行 LOGO 评估，并提出 Differential Depth Response (DDR) 框架将特征分为 drifting/intermediate/near-stationary 三类。Binary LOGO F1 = 0.694，cross-model F1 = 0.764。任务定义新颖，实验覆盖面广，但 DDR 统计基础和下游实验的统计效力存在显著问题。\n\n## Strengths\n\n**S1. 新颖且有实际意义的任务定义。**\n**S2. 评估协议严谨且透明。**\n**S3. 可解释的方法设计。**\n**S4. 诚实的自我评估。**\n**S5. 附录消融覆盖全面。**\n\n## Must-Fix 问题\n\n**N1** [Critical] **下游效用实验 (§L/§4.3) n=3 seeds 严重欠缺统计效力**\n- n=3 时 TOST 等价性检验的 power 极低——发现\"等价\"可能仅因检测不到真实差异\n- 方差估计本身的 95% CI 在 df=2 时极宽\n- 建议：增加至 ≥20 seeds 或将下游实验降格为 preliminary evidence，从 contributions 列表移除\n\n**N2** [Critical] **DDR tri-partition 阈值 (§4.2) 缺乏 principled 依据**\n- 0.75 介于 Cohen 惯例 \"medium\"（0.5）和 \"large\"（0.8）之间，未说明为何选此特定值\n- 敏感性分析仅检验 near-stationary 边界，未检验 drifting 边界——若使用 0.5，entropy_std (d=0.55) 将从 intermediate 重新分类为 drifting\n- 建议：对 drifting 阈值做完整敏感性分析（0.3-1.0），或用 data-driven 方法取代固定阈值\n\n## Should-Fix 问题\n\n**W1** [Major] **三个 drifting 特征本质是同一潜在因子**（r=0.81-0.97，PCA 92.3% variance by PC1）\n**W2** [Major] **参考模型 confound 部分未解决**（cross-reference F1 从 0.694 降至 ~0.613，降幅 8pp）\n**W3** [Major] **Independent-seed 控制仅覆盖 2/8 generators**\n**W4** [Major] **LOGO 同家族泄漏未在主表中体现**（LOFO 0.686 vs LOGO 0.694）\n\n## 小问题\n**M1** 未探索 n-gram 和句法特征\n**M2** Baseline 对比不对称（单特征 vs 7 特征）\n**M3** Pooled Cohen's d 异方差问题仅在附录讨论\n**M4** 缺少 stylometric machine text fingerprinting 文献引用\n\n## Questions\n**Q1.** 若 drifting 阈值降至 0.5，entropy_std (d=0.55) 是否重分类？\n**Q2.** 下游实验为何仅 3 seeds？\n**Q3.** 三参考模型平均 \"reference-neutral\" F1 是多少？\n**Q4.** 是否考虑将 LOFO 作为主要指标？\n**Q5.** 三个 drifting 特征替换为 PC1 后性能变化？\n\n## Overall Assessment\n**3.0 (Findings)**，Soundness 3/5，Excitement 3.5/5，Reproducibility 4/5\nConfidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-19T04:13:36.583094+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24820
}
```

</details>

---


### Tool call

_source line 1780 · 2026-05-19T04:13:36.734791+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n### 审查侧重：新颖性、完整性、写作质量与格式合规\n\n## Summary\n\n本文提出 generation depth classification 任务：将文本分类为 gen-0 / gen-1 / gen-2+。通过 7 个手工特征和 XGBoost 分类器，在 8 个 base model 上实现 LOGO binary F1=0.694。核心发现是 DDR tri-partition。作者诚实地定位贡献为\"empirical rather than methodological\"。\n\n## Strengths\n\n**S1. 任务定义新颖且方向正确。**\n**S2. 实验设计严谨，控制变量充分。**\n**S3. DDR 发现有一定洞察价值。**\n**S4. 论文诚实透明。**\n**S5. 附录详尽。**\n**S6. 与 concurrent work 的定位清晰。**\n\n## Weaknesses\n\n**W1 [Critical] Base model 限制严重削弱论文的 significance 和实际价值。**\n- OLMo-2-1B-Instruct LOGO F1 从 0.763 暴跌至 0.338\n- 现实中 web text 几乎全部由 instruct/RLHF 模型生成\n- 将核心限制框架为设计选择（\"We restrict to base models, since instruction-tuning introduces confounds\"）\n\n**W2 [Major] DDR 作为 EMNLP 贡献可能偏薄——本质上是特征分析。**\n- \"This interpretation is post-hoc and empirical\"，没有理论解释\n- 7 个特征中 TTR 和 hapax ratio r=0.97，实质 ~5-6 个独立特征\n- 核心发现基本上是 \"some features are more sensitive to recursive generation than others\" 的系统化表述\n\n**W3 [Major] 主要性能指标 F1=0.694 偏低。**\n- 分类器错误率约 30%\n- QLoRA 达到 3-class F1=0.905（+11.6pp），说明 7 特征集远非最优\n- moderate 性能 + base-model-only + empirical-only，三者叠加限制 impact\n\n**W4 [Major] Contribution #3（parameter dependence）本质是 negative result，定位不当。**\n- 将\"方法在某些条件下失效\"列为贡献在逻辑上不自洽\n- 更适合放在 Discussion/Limitations\n\n**W5 [Minor] Abstract 中引用了过多具体数字。**\n**W6 [Minor] Figure 1 信息密度不足。**\n**W7 [Minor] Related Work 中 ordinal classification 文献覆盖不足。**\n**W8 [Minor] 下游实验 n=3 seeds 统计效力不足。**\n\n## Questions\n**Q1.** Base-model depth profiling 的实际部署场景？\n**Q2.** QLoRA 在 instruct model 上的表现？\n**Q3.** 能否对 DDR 的 \"location shifts but shape persists\" 提供更形式化的分析？\n**Q4.** Cross-model chains F1=0.764 高于 LOGO 0.694——depth signal 在混合时更强？\n**Q5.** entropy_min 的 gen-1 vs. gen-2+ 单独 correlation？\n\n## Missing References\n1. Ordinal classification in NLP（sentiment ordinal approaches）\n2. Self-training：STaR (Zelikman et al., 2022) 等\n3. Distribution shift / domain adaptation 文献\n4. N-gram based detection methods\n\n## Overall Assessment\n**3.0 (Findings)**，Soundness 4/5，Excitement 2.5/5，Reproducibility 4/5，Clarity 4/5\nConfidence: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n### 审查侧重：新颖性、完整性、写作质量与格式合规\n\n## Summary\n\n本文提出 generation depth classification 任务：将文本分类为 gen-0 / gen-1 / gen-2+。通过 7 个手工特征和 XGBoost 分类器，在 8 个 base model 上实现 LOGO binary F1=0.694。核心发现是 DDR tri-partition。作者诚实地定位贡献为\"empirical rather than methodological\"。\n\n## Strengths\n\n**S1. 任务定义新颖且方向正确。**\n**S2. 实验设计严谨，控制变量充分。**\n**S3. DDR 发现有一定洞察价值。**\n**S4. 论文诚实透明。**\n**S5. 附录详尽。**\n**S6. 与 concurrent work 的定位清晰。**\n\n## Weaknesses\n\n**W1 [Critical] Base model 限制严重削弱论文的 significance 和实际价值。**\n- OLMo-2-1B-Instruct LOGO F1 从 0.763 暴跌至 0.338\n- 现实中 web text 几乎全部由 instruct/RLHF 模型生成\n- 将核心限制框架为设计选择（\"We restrict to base models, since instruction-tuning introduces confounds\"）\n\n**W2 [Major] DDR 作为 EMNLP 贡献可能偏薄——本质上是特征分析。**\n- \"This interpretation is post-hoc and empirical\"，没有理论解释\n- 7 个特征中 TTR 和 hapax ratio r=0.97，实质 ~5-6 个独立特征\n- 核心发现基本上是 \"some features are more sensitive to recursive generation than others\" 的系统化表述\n\n**W3 [Major] 主要性能指标 F1=0.694 偏低。**\n- 分类器错误率约 30%\n- QLoRA 达到 3-class F1=0.905（+11.6pp），说明 7 特征集远非最优\n- moderate 性能 + base-model-only + empirical-only，三者叠加限制 impact\n\n**W4 [Major] Contribution #3（parameter dependence）本质是 negative result，定位不当。**\n- 将\"方法在某些条件下失效\"列为贡献在逻辑上不自洽\n- 更适合放在 Discussion/Limitations\n\n**W5 [Minor] Abstract 中引用了过多具体数字。**\n**W6 [Minor] Figure 1 信息密度不足。**\n**W7 [Minor] Related Work 中 ordinal classification 文献覆盖不足。**\n**W8 [Minor] 下游实验 n=3 seeds 统计效力不足。**\n\n## Questions\n**Q1.** Base-model depth profiling 的实际部署场景？\n**Q2.** QLoRA 在 instruct model 上的表现？\n**Q3.** 能否对 DDR 的 \"location shifts but shape persists\" 提供更形式化的分析？\n**Q4.** Cross-model chains F1=0.764 高于 LOGO 0.694——depth signal 在混合时更强？\n**Q5.** entropy_min 的 gen-1 vs. gen-2+ 单独 correlation？\n\n## Missing References\n1. Ordinal classification in NLP（sentiment ordinal approaches）\n2. Self-training：STaR (Zelikman et al., 2022) 等\n3. Distribution shift / domain adaptation 文献\n4. N-gram based detection methods\n\n## Overall Assessment\n**3.0 (Findings)**，Soundness 4/5，Excitement 2.5/5，Reproducibility 4/5，Clarity 4/5\nConfidence: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-19T04:13:38.200940+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1466
}
```

</details>

---


### Assistant

_source line 1782 · 2026-05-19T04:13:41.854638+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 1783 · 2026-05-19T04:13:44.467962+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。论文提出了新颖的 depth classification 任务定义，实验设计严谨（LOGO/LOFO/seed control 等），DDR 发现有一定洞察价值。但三个主要问题制约了评分：

1. **[Critical] Base model 限制**：instruct model 上性能严重退化（OLMo LOGO F1: 0.763→0.338），而实际 web text 几乎全部来自 instruct models
2. **[Major] DDR 贡献偏薄**：本质是 7 个特征的敏感度分析，缺乏理论解释，且 TTR/hapax ratio 高度冗余（r=0.97）
3. **[Major] 性能偏低**：leak-free binary F1=0.694，QLoRA 可达 0.905 但被放在附录

写作质量和格式合规方面整体良好，无重大问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1784 · 2026-05-19T04:13:50.266878+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 161

## Round 161

2 recorded events


### User

_source line 1785 · 2026-05-19T04:17:07.590877+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 Round 1 意见的逐条回应

---

## Strengths 回应

**[AGREE] R1-S1 (新颖任务定义):** 同意。任务从 binary 推进到 ordinal depth classification 是有意义的方向扩展，与我的 S1 评价一致。

**[AGREE] R1-S2 (评估协议严谨):** 同意。LOGO + LOFO + seed control + length matching 构成完善的控制体系，是本文最突出的优点之一。

**[AGREE] R1-S3 (可解释方法):** 同意。7 个手工特征的选择使 DDR 分析透明可解释，这是相对 QLoRA 端到端方法的核心 trade-off，论文在 Section 5 (line 19) 明确讨论了此点。

**[AGREE] R1-S4 (诚实自评):** 同意。Limitations section 的详尽程度在 empirical 论文中罕见（34 行，涵盖 8+ 项局限）。

**[AGREE] R1-S5 (附录覆盖):** 同意。16 个附录实验板块覆盖了几乎所有可预见的审稿问题。

---

## Must-Fix 问题回应

**[AGREE] R1-N1: 下游效用 n=3 seeds 统计效力不足**
同意此为真实问题。n=3 时 TOST 的 statistical power 确实极低（df=2），且论文自己在 Appendix L 中承认 "with only n=3 seeds per condition, the TOST results have limited generalizability"。不过需要注意两点：
1. 论文已将此定位为 appendix 中的辅助证据，未列入正文 contribution list（Introduction 的三条 contribution 不包含下游实验）
2. Cross-seed standard deviation < 0.001 说明实验本身可重复，但 R1 指出的 power 问题仍然成立——低方差+低 n 可能导致 false equivalence

建议：将 "depth composition does not determine training utility" 的结论明确降格为 "preliminary evidence suggests..."，并在正文 Discussion (Section 5 line 17) 中更谨慎表述。

**[AGREE] R1-N2: DDR 阈值缺乏 principled 依据**
部分同意。核查发现 R1 的担忧有据：
1. **d=0.75 阈值**确实介于 Cohen 惯例的 medium (0.5) 和 large (0.8) 之间，论文未解释为何选此值而非标准的 0.8
2. **敏感性分析只覆盖了 near-stationary boundary**（通过 TOST 的 ε=0.15/0.20/0.25），但**未对 drifting boundary 本身做敏感性分析**。R1 正确指出，若阈值降至 0.5，entropy_std (d=0.55) 将从 intermediate 变为 drifting，使 tri-partition 变成 4/0/3 bi-partition

但我认为严重程度应从 [Critical] 降为 [Major]，理由：
- 论文在 Section 4.2 (line 66) 指出 "shifting thresholds by ±0.10 does not alter grouping"
- Appendix V 的 data-driven clustering（k=2, silhouette=0.632）提供了独立的分组验证，不依赖 fixed threshold
- 9.5× 的 drifting-to-near-stationary gap（Glass's Δ）意味着即使阈值有所移动，drifting 和 near-stationary 之间的分离仍然稳健
- entropy_std 的边界地位（d=0.55, ρ=0.16）本身就是 DDR 中最有趣的发现之一

建议：补充 drifting 阈值的完整敏感性分析（0.3-1.0），并说明 0.75 的选择理由（或改用 data-driven cutpoint）。

---

## Should-Fix 问题回应

**[AGREE] R1-W1: 三个 drifting 特征本质是同一潜在因子**
强烈同意，与我的 W2 观点一致。r=0.97 (TTR/hapax) 和 PCA 92.3% by PC1 明确表明三个 drifting 特征携带高度冗余信息。论文在 Section 4.2 (line 81) 承认 "permutation importance difference reflects feature masking in tree-based ensembles rather than genuinely distinct signals"，这实际上是在说 TTR 和 hapax ratio 不是独立贡献。"7-feature ensemble" 的表述虽然技术上准确，但可能给读者造成独立特征数量的误导。R1 的 Q5（替换为 PC1）是一个有建设性的验证建议。

**[REBUT] R1-W2: 参考模型 confound (cross-reference F1 从 0.694 降至 ~0.613)**
**R1 的数据引用有误。** 经核查：
- Table 4（Appendix S, Cross-Family Reference Models）显示三个参考模型的 LOGO F1 分别为 Pythia-410M: 0.803, OLMo-2-1B: 0.807, Qwen3-0.6B: 0.816（均为 5-gen LOGO subset 上的 3-class F1）
- 主文 Section 4.2 (line 85) 明确写道 "spread 0.013"
- R1 引用的 "~0.613" 实际上来自 Appendix H（Robustness to Text Perturbation），是 10% random word replacement 条件下的 binary F1=0.614，与参考模型选择无关

因此 R1 关于 "参考模型 confound 部分未解决" 的结论建立在错误的数据引用之上。实际数据（spread=0.013）恰恰支持论文的 claim：depth features are robust to reference model choice。

但需要指出一个**合理的相关担忧**：cross-reference 实验仅使用了 3 个参考模型（均为 <2B 参数），未覆盖更大或架构差异更大的参考模型。spread=0.013 可能低估了 reference model 选择在更广参考集上的影响。

**[AGREE] R1-W3: Independent-seed 控制仅覆盖 2/8 generators**
同意。核查确认 Appendix（seed control）仅使用 Pythia-2.8B 和 OLMo-2-1B 两个 generator（各 500 seeds），覆盖率 2/8 = 25%。虽然结果（F1=0.680 vs. 0.694, Δ=-1.4pp）方向正确，但仅两个 generator 不足以排除其他家族（特别是 Qwen、Llama、Mistral）上 seed sharing 的潜在更大影响。建议至少扩展至每个家族一个 generator。

**[AGREE] R1-W4: LOGO 同家族泄漏**
同意这是一个合理关注，但认为严重程度偏低。LOFO (0.686) vs. LOGO (0.694) 的差距仅 0.8pp，且 95% CI 可能重叠。论文在 Section 3.4 (lines 71-72) 和 Section 4.1 (line 14) 均明确报告了 LOFO 结果并讨论了此问题。将 LOFO 作为 secondary metric（而非替代 LOGO 作为 primary）是合理的，因为 LOGO 是该领域更标准的评估方式。但在 Table 1 中增加 LOFO 行会更透明。

---

## 小问题回应

**[AGREE] R1-M1 (未探索 n-gram/句法特征):** 同意这是一个 gap，但论文在 Limitations (line 31) 已经讨论。这些特征可能提供互补信息但不会贡献于 location/shape decomposition。

**[REBUT] R1-M2 (Baseline 对比不对称):**
对比设计是合理的。Table 2 的目的不是 "公平竞赛"，而是 contextualize depth discrimination ability（Section 4.3 line 96: "rather than claim competitive advantage over detection-optimized methods"）。每个 baseline score 被用作 XGBoost 的单一特征（Section 3.4 line 87），使用完全相同的分类器和 LOGO 协议。这不是"不对称"，而是在回答"单一检测分数是否足够做 depth classification"的问题。且 Table 2 同时报告了 4-detector ensemble (4 features) 和 4-det + surface (6 features) 的结果，提供了 multi-feature baseline。

**[AGREE] R1-M3 (Pooled Cohen's d 异方差):** 同意。论文在正文 Section 4.2 (lines 70-71) 承认 Levene tests reject equal-variance，并使用 CV shift 和 Glass's Δ（Appendix V）作为补充。将 Glass's Δ 结果提升到正文会增强 soundness。

**[AGREE] R1-M4 (缺少 stylometric fingerprinting 文献):** 同意。Related Work Section 2.3 引用了 Stamatatos survey 和 Koppel，但确实缺少更具针对性的 machine text stylometric fingerprinting 文献。

---

## Questions 回应

**[AGREE] R1-Q1 (阈值 0.5 → entropy_std 重分类):**
是的，若 drifting 阈值降至 0.5，entropy_std (d=0.55) 确实会被重分类为 drifting。但我认为这不一定是 DDR 的失败——entropy_std 的 ρ=0.16（远低于 drifting 的 ρ>0.60）说明它即使 effect size 较大（d=0.55），也缺乏 monotonic depth trend，使其行为模式确实不同于三个 drifting 特征。DDR 的 tri-partition 使用了多个指标（ρ, d, CV shift, Levene），不仅仅是 d 一个维度。

**[AGREE] R1-Q2 (下游 n=3 原因):** 论文未解释 n=3 的选择。可能是 compute 限制（每个 variant fine-tune OLMo-2-0425-1B），但应当明确说明。

**[AGREE] R1-Q3 (reference-neutral F1):** 基于论文数据，三个参考模型的平均 LOGO F1 约为 (0.803+0.807+0.816)/3 ≈ 0.809（5-gen 3-class），spread=0.013。但这是 5-gen subset 的结果，不直接对应 8-gen LOGO 的 0.694 binary F1。论文应当在统一的 8-gen LOGO setting 下报告跨参考模型结果。

**[REBUT] R1-Q4 (LOFO 作为主指标):**
LOGO 作为主指标更合理。LOFO 要求按家族 hold out，但不同家族含有不同数量的 generator（Qwen 有 3 个，其他各 1-2 个），导致各 fold 训练集大小不均衡。LOGO 确保每个 fold hold out 恰好一个 generator，产生更均衡的 splits。且 LOFO 0.686 vs. LOGO 0.694 的差距（0.8pp）在 bootstrap CI 范围内，说明 same-family leakage 影响极小。将 LOFO 作为 supplementary metric 报告（当前做法）是适当的。

**[AGREE] R1-Q5 (PC1 替换):** 这是一个有建设性的验证建议。若替换后性能差距 <1pp，则进一步支持三个 drifting 特征冗余的结论。若差距显著，则说明 XGBoost 利用了非线性交互。无论哪种结果都有 informative 价值。

---

## Overall Assessment 回应

**[AGREE] R1 给出 3.0 (Findings)。**

与我的评分一致。我们在以下核心判断上达成共识：
1. 任务定义新颖，实验严谨（→ 达到 Findings 门槛）
2. DDR 贡献偏 empirical，缺乏理论深度（→ 不足以达到 Conference）
3. 性能偏低（binary F1=0.694）且 base-model 限制严重

我与 R1 的主要分歧在于：
- **R1 的 Excitement 3.5 vs. 我的 2.5**：我更重视 base-model 限制对实际 significance 的影响（我的 W1 [Critical]），认为这比 R1 评估的更严重。R1 未将 base-model 限制列为独立的 weakness（仅在 N1/Q2 间接涉及），这可能导致 Excitement 偏高。
- **R1-W2 数据引用错误**：R1 关于 cross-reference F1 降至 ~0.613 的 claim 基于错误的数据来源（实际来自 Appendix H perturbation experiment），实际 spread=0.013，这使得 W2 的严重程度大幅降低。

最终我维持 **Overall 3.0 (Findings)**，Soundness 4/5（比 R1 高 1 分，因为 R1 的 W2 证据不成立）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1786 · 2026-05-19T04:17:12.686747+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 162

## Round 162

6 recorded events


### User

_source line 1787 · 2026-05-19T04:17:15.792137+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应

---

### Strengths

[AGREE] R2-S1 至 R2-S6：全部同意。R2 对论文优势的概括准确，尤其是 S4（诚实透明）和 S6（与 concurrent work 的定位）我在自己的审稿中也作为亮点强调。

---

### Weaknesses

**[AGREE with nuance] R2-W1: Base model 限制严重削弱 significance**

同意这是一个重要限制。OLMo-2-1B-Instruct LOGO F1 暴跌至 0.338（§8 Limitations, Appendix K）确实说明当前方法无法直接应用于 instruct/RLHF 模型，而现实 web text 绝大多数由 instruct 模型生成，这限制了实际部署价值。

但我不同意将其定为 **Critical**，理由如下：
1. 论文标题已明确范围为 "Base LLM Text Chains"，这是一个有意识的范围界定而非疏忽
2. 对于首次定义新任务的 foundational study，在更干净的 base model 设定下建立分析框架是合理的——instruct tuning 引入 RLHF、format constraints、instruction following 等多重 confounds，不利于隔离深度信号
3. 论文诚实报告了 instruct 结果（§8: "Instruction tuning substantially weakens the signal across all three tested families"），包括具体数字（OLMo F1=0.338, Llama F1=0.544），没有回避
4. §8 同时报告 QLoRA 在 instruct model 上 F1=0.338 vs 0.763 base，暗示信号存在但 handcrafted features 无法捕获——这指向未来方向而非根本性缺陷

**建议定级 Major**：是显著的 scope limitation，影响 excitement/impact 评分，但不应一票否决一篇定位为 foundational empirical study 的论文。

---

**[AGREE] R2-W2: DDR 作为 EMNLP 贡献偏薄**

同意。这与我自己的 N2（DDR 阈值缺乏 principled 依据）和 W1（三个 drifting 特征本质是一个潜在因子）高度一致。补充 R2 的论点：

- R2 指出 "本质上是 'some features are more sensitive to recursive generation than others' 的系统化表述"——这个概括基本准确。DDR 的贡献在于将这一观察结构化为 drifting/intermediate/near-stationary 三类，但结构化的依据（Cohen's d 阈值 0.75/0.10）是 arbitrary 的（我的 N2 详细论证了这一点）
- R2 提到 TTR 和 hapax ratio r=0.97——我进一步指出三个 drifting 特征全部高度相关（r=0.81-0.97），PCA 确认形成单一 cluster（Appendix Q），DDR 的 3/1/3 划分在独立信息维度上更接近 1/1/3
- "post-hoc and empirical" 的自我定位（§5）虽然诚实，但也意味着 DDR 缺乏 predictive power——不能预测新特征会落入哪一类

不过，DDR 仍然提供了一个有用的 descriptive framework，只是作为 EMNLP main conference 的核心贡献确实偏薄。**作为 Findings 贡献是合适的。**

---

**[REBUT] R2-W3: F1=0.694 偏低**

部分不同意。R2 的论证需要重要的 context 补充：

1. **指标不可直接对比**：R2 将 LOGO binary F1=0.694（8-gen，gen-1 vs gen-2+）与 QLoRA 3-class F1=0.905（6-gen LOGO，Table 6 脚注明确 "Evaluated on the original 6 generator subset"）对比。这是两个不同的指标（binary vs 3-class）、不同的 generator pool（8 vs 6）。在同一 6-gen 评估下，XGBoost 3-class F1=0.789，QLoRA 0.905，差距是 +11.6pp 而非 R2 暗示的 ~21pp

2. **LOGO 是极其严格的评估**：LOGO hold out 整个未见 generator，classifier 必须泛化到训练时完全未见的模型架构和训练数据分布。在这种条件下 binary F1=0.694 意味着 the signal exists and generalizes，这对于一个**首次定义的新任务**是有价值的基线

3. **QLoRA 的高性能恰恰支持论文论点**：论文在 Appendix E 中定位 QLoRA 为验证 "depth signal extends beyond handcrafted features"（p.15），QLoRA 的高 F1 说明深度信号真实存在且更丰富的表示能捕获更多——这strengthens 而非 weakens 论文的核心发现（深度分类是可行的）

4. **方法贡献的定位**：论文明确将贡献定位为 "empirical rather than methodological"（p.1）。手工特征的价值在于 interpretability 和 DDR 分析的 enablement，而非追求 SOTA——论文清楚说明了这一点（§5: "the handcrafted ensemble trades classification ceiling for interpretability"）

**我的判断**：F1=0.694 对于 EMNLP main 确实略低，但对于 Findings 定位的 foundational study 是可接受的。R2 的 "moderate 性能 + base-model-only + empirical-only 三者叠加" 观察是合理的 impact 评估，但不应基于不可比的指标对比来论证。

---

**[AGREE] R2-W4: Contribution #3（parameter dependence）定位不当**

同意。查看论文 p.1 的贡献列表：

> "3. We establish DDR's parameter dependence: instruction tuning reverses features (fading drift direction across three families (entropy mean μ → −0.60 → +0.48), and depth signal degrades at t=0.1 (−8.3 to −26.0pp) while remaining robust within t ∈ [0.5, 0.7] (§5)."

这本质上是两部分：(a) instruction tuning 使信号失效——这是 limitation；(b) 温度敏感性——这是 robustness/boundary condition 分析。

R2 说得对：将 "方法在某些条件下失效" 框架为 "贡献" 在逻辑上有张力。正常做法是将 (a) 放入 Limitations，(b) 放入 Discussion 或 robustness analysis。

**不过有一个细微的 nuance**：温度敏感性发现（t=0.5-0.7 robust, t=0.1 degradation）对潜在使用者有操作性价值——它告诉你什么条件下可以信任这个方法。这种 "operational envelope" 信息在应用导向的 community 中有时被视为贡献。但我同意 R2 的判断——在 EMNLP 的 framing 中，这更适合放在 Discussion/Limitations。

**建议定级**：同意 R2 的 Major，但建议作者 reframe 而非删除——将其整合到 Discussion 中作为 "boundary conditions" 讨论。

---

**[AGREE] R2-W5: Abstract 数字过多**

同意。Abstract 包含：F1=0.694, CI [0.688, 0.700], 0.764, d ≥ 0.75, d ≤ 0.71, d < 0.10, ≥ 9.5×。CI 和 DDR 阈值细节可以移至 Introduction，Abstract 保留 2-3 个关键数字即可。这符合论文写作规范（§二："最多引用 2-3 个关键数字"）。

---

**[REBUT] R2-W6: Figure 1 信息密度不足**

不同意。Figure 1（strip plot with per-generator variation）在单张图中编码了 7 features × 5 depths × 8 generators 的 DDR pattern，加上 Cohen's d 标注和 tri-partition color coding。这是论文信息密度最高的图之一。

R2 可能关注的是视觉设计（strip plot 的空白区域），但数据密度是充分的——将 DDR 的核心发现浓缩为一张可扫读的图。如果 R2 的意思是"可以更紧凑"（如换用 heatmap），那是设计偏好问题而非信息密度不足。

---

**[AGREE] R2-W7: Ordinal classification 文献覆盖不足**

同意。论文在 §3.4 和 Appendix H 引用了 CORAL 和 Frank-Hall，Appendix H 中也有 Gutierrez et al. ordinal survey。但 Related Work（§2）没有 ordinal classification 的讨论。考虑到 depth classification 天然是 ordinal task（gen-0 < gen-1 < gen-2 < ...），Related Work 中应有一段专门讨论 ordinal classification 在 NLP 中的应用（如 sentiment ordinal regression），以及为什么论文最终选择 nominal 分类（collapsed 3-class）而非 ordinal 方法。

---

**[AGREE but escalate severity] R2-W8: 下游 n=3 seeds**

同意这是一个问题，但**强烈不同意 R2 将其定为 Minor**。

这与我的 N1 [Critical] 完全一致。理由：
- 下游效用是论文三大贡献之一（Abstract, Introduction contribution list）
- n=3 时 TOST 等价性检验的 power 极低，论文自己承认 Cohen's d "unreliable"（p.20）
- "practically indistinguishable downstream quality" 的声明无法由 n=3 支撑
- 如果一个被列为 contribution 的实验无法通过基本的统计效力标准，这影响的是论文 soundness 而非 polish

**建议定级**：从 R2 的 Minor 升级至 Critical/Major。这不是文字措辞问题——是核心声明的证据基础问题。

---

### Questions

**[AGREE] R2-Q1 (Base model 部署场景)**：好问题。论文确实缺少具体的 deployment pipeline 描述。§1 提到 model collapse 和 data provenance，但没有说明"在什么流程中、谁会用 depth profiling 做什么决策"。即使限于 base model，也应描述一个 concrete use case（如 pretraining data filtering pipeline）。

**[AGREE] R2-Q2 (QLoRA on instruct model)**：非常好的问题。如果 QLoRA 能在 instruct model 上恢复 depth signal，就说明 base model 限制是 handcrafted features 的问题而非任务本身的。这对论文的 significance 评估有直接影响。

**[AGREE] R2-Q3 (DDR 形式化分析)**：与我的 N2 一致。DDR 目前是纯 empirical 的，缺乏任何形式化基础。即使是简单的假设检验框架（如基于 effect size 的 decision rule 的 FDR 控制）也能显著加强。

**[AGREE with caveat] R2-Q4 (Cross-model F1=0.764 > LOGO 0.694)**：值得追问。但需注意这两个数字来自不同评估设定——cross-model chains 使用 5-fold CV on single-generator evaluation（§3.4 footnote: "Sample-level CV is used because each chain contains multiple generators, making generator-level held-out splits inapplicable"），而 LOGO 是 hold-out generator。评估协议的差异可能解释部分 gap，不一定说明 "depth signal 在混合时更强"。

**[NO STRONG VIEW] R2-Q5 (entropy_min gen-1 vs gen-2+)**：这是一个有针对性的技术细节问题。Appendix N（Feature Distribution Analysis）的 DDR trend lines 可能已部分回答——entropy_min 在 gen-1 vs gen-2+ 之间的变化是 near-stationary 类别中最大的。但没有单独的 correlation 分析。

---

### Missing References

**[PARTIALLY AGREE] R2-MR1 (Ordinal classification in NLP)**：同意，见 W7 回应。至少应引用 ordinal sentiment classification 的经典工作。

**[REBUT] R2-MR2 (Self-training: STaR)**：不同意。STaR (Zelikman et al., 2022) 是关于 reasoning self-improvement 的方法，其 "iterative" 性质指的是 rationale bootstrapping，与本文的 recursive text generation chains 在机制上不同。本文的 chains 是 LLM 用前一轮输出作为 input 继续生成文本（text re-enters the web），而 STaR 是在自身推理 trace 上自我训练。将两者混同会误导读者。如果 R2 的意图是引用 iterative self-improvement 的广义文献，论文已引用了 self-consuming generative models（Alemohammad et al., 2024）和 model collapse（Shumailov et al., 2024），覆盖了更直接相关的 iterative generation literature。

**[PARTIALLY AGREE] R2-MR3 (Distribution shift / domain adaptation)**：有一定道理。论文的 cross-domain（Appendix J）和 cross-temperature（Appendix O）实验本质上研究 distribution shift 下的 robustness。引用 distribution shift 的经典框架（如 covariate shift, dataset shift）可以帮助 formalize 这些实验的意义。但这不是关键缺口。

**[AGREE] R2-MR4 (N-gram based detection)**：同意，与我的 M1 一致。论文特征集完全不含 n-gram 特征，引用 n-gram based detection methods 可以 contextualize 这一设计选择。

---

### Overall Assessment

R2 给出 **3.0 (Findings)**，与我的评分一致。

我与 R2 的主要分歧：
1. **R2-W1 severity**：R2 标 Critical，我认为 Major——base model scope 是合理的 foundational study 范围界定
2. **R2-W3 论证方式**：R2 将不可比的指标（8-gen binary LOGO vs 6-gen 3-class QLoRA）并列，低估了 F1=0.694 在 LOGO 评估下的合理性
3. **R2-W8 severity**：R2 标 Minor，我认为 Critical——n=3 下游实验是核心声明的证据缺陷，不是 polish 问题

**共识区域**：DDR 贡献偏薄（R2-W2/我的 N2+W1）、Contribution #3 定位不当（R2-W4）、overall 3.0 Findings 定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-19T04:20:11.790187+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "# Round 24 Review Issues — Fresh review (no prior round memory)\n# Updated after R24 cross-sharing convergence\n\n# ============ CRITICAL (Must-Fix) ============\n\n- id: \"R1-N2\"\n  summary: \"仅限 base model 的限制对论文 significance 造成根本性约束\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"严重性取决于 framing; 科学发现定位使其降为 design scope\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"两位 Reviewer 再次一致标记 critical。论文多处措辞暗示超出 base-model 范围的一般性。\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"R2 标 Critical（instruct model 上 OLMo F1=0.338，web text 几乎全部来自 instruct models），R1 降为 Major（foundational study 合理范围界定）。Director 判定 Major-Critical。\"}\n  action_items:\n    - {round: 21, action: \"Abstract + Contribution 均加 scope limitation\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 22, action: \"No additional change needed — resolved by C2 framing adjustment to scientific characterization\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"Abstract 重写前置 base-model scope；Intro L5 'how language models' → 'how base language models'；Intro L5 移除 provenance 引用；Intro L8 移除 provenance 定义\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"论文标题已含 'Base LLM'，Abstract/Intro 已前置 scope。需补充 concrete deployment scenario（如 pretraining data filtering pipeline）。需论证 base-model study 的独立价值\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N1\"\n  summary: \"DDR tri-partition 阈值 (d=0.75/0.10) 缺乏 principled 依据，drifting boundary 未做敏感性分析\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提异方差下 Cohen's d 问题\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"补充 Glass's Δ + Cliff's δ\"}\n    - {round: 23, reviewers: \"R1(warning),R2(rebut)\", note: \"R1 仍标记正文依赖 pooled d\"}\n    - {round: 24, reviewers: \"R1(critical),R2(agree-降级major)\", note: \"R1 标 Critical：0.75 未解释选择理由，敏感性分析仅覆盖 near-stationary boundary。R2 同意问题存在但认为 data-driven clustering (silhouette=0.632) 和 9.5× gap 提供了独立验证，降为 Major。\"}\n  action_items:\n    - {round: 22, action: \"Glass's Δ + Cliff's δ added to appendix\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"§4.2 L54: 加入 Glass's Δ gap ≥9.5× 数字到正文\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"补充 drifting 阈值完整敏感性分析 (d=0.3-1.0)；说明 0.75 选择理由或改用 data-driven cutpoint；展示 entropy_std 在不同阈值下的分类稳定性\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N2\"\n  summary: \"下游效用实验 n=3 seeds 严重 underpowered，不足以支撑等价性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提(warning)，R2同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"升级 critical\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"再次确认。合并至 R23-N2。Contribution 4 已移除\"}\n    - {round: 24, reviewers: \"R1(critical),R2(minor→agree escalate)\", note: \"R1 标 Critical。R2 初始标 Minor，交叉后被 R1 说服——论文虽已从 contribution list 移除 downstream，但 Discussion §5 L17 仍做定性结论。R1 指出 n=3 TOST power 极低，论文自承 Cohen's d unreliable。\"}\n  action_items:\n    - {round: 22, action: \"Discussion restructured to demote downstream evidence\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"Contribution 4 完全移除。downstream 仅保留在 Discussion 作为 preliminary observation\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"Discussion §5 L17 结论措辞改为 'preliminary evidence suggests...'；Appendix L 标注为 pilot experiment\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MAJOR (Should-Fix) ============\n\n- id: \"R24-W1\"\n  summary: \"三个 drifting 特征 (r=0.81-0.97, PCA 92.3%) 本质是同一 latent factor，DDR 3/1/3 在独立信息维度上更接近 1/1/3\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"TTR-hapax r=0.97，entropy_mean-TTR r=0.86。需 PCA/factor analysis。\"}\n    - {round: 24, reviewers: \"R1(major),R2(强烈同意)\", note: \"R1：DDR 3/1/3 在独立信息维度上更接近 1/1/3。R2 强烈同意。论文 §4.2 L81 自承 permutation importance 差异是 feature masking 而非独立信号。PCA 已做 (92.3% by PC1) 但叙事未调整。\"}\n  action_items:\n    - {round: 23, action: \"§4.2 加入 PCA 结论句。Appendix feature correlation 加入详细 PCA 结果。\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"调整叙事：承认三个 drifting 特征共享单一 latent dimension；考虑报告 PC1 替换实验（R1-Q5）；避免将 '3 drifting features' 作为 'rich feature drift' 的证据\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W2\"\n  summary: \"DDR 作为 EMNLP 核心贡献偏薄：本质是特征敏感度分析 + post-hoc empirical 解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"R2：核心是 'some features are more sensitive to recursive generation than others' 的系统化表述。R1 同意并补充：DDR 缺乏 predictive power。作为 Findings 合适，不够 main conference。\"}\n  action_items:\n    - {round: 24, action: \"考虑提供 DDR 的更严谨 mechanistic explanation 或形式化分析；或更明确定位为 descriptive framework\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W3\"\n  summary: \"Contribution #3 (parameter dependence) 本质是 negative result，列为贡献逻辑不自洽\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"R2：将 '方法在某些条件下失效' 列为贡献不自洽。R1 同意但指出温度 boundary condition 有操作价值。共识：reframe 为 Discussion 中的 boundary conditions。\"}\n  action_items:\n    - {round: 24, action: \"Contribution #3 reframe 为 'boundary conditions' 或整合入 Discussion；或改为正面表述 'We characterize DDR's validity regime'\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W4\"\n  summary: \"Independent-seed 控制仅覆盖 2/8 generators (25%)，不足以支撑跨家族泛化声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(major),R2(agree)\", note: \"仅 Pythia-2.8B 和 OLMo-2-1B。Qwen/Llama/Mistral 的 seed sharing 效应未验证。\"}\n  action_items:\n    - {round: 24, action: \"至少为每个家族各选一个 generator 做 independent-seed 控制\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MINOR / INFO ============\n\n- id: \"R24-M1\"\n  summary: \"LOGO 同家族泄漏未在主表 (Table 1) 中体现，LOFO 仅在文中提及\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(major),R2(agree-低严重性)\", note: \"LOFO 0.686 vs LOGO 0.694，差 0.8pp。R2 认为 LOGO 作为主指标合理（LOFO fold 不均衡），在 Table 1 增加 LOFO 行更透明。\"}\n  action_items:\n    - {round: 24, action: \"Table 1 增加 LOFO binary F1 行\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M2\"\n  summary: \"Abstract 数字过多（7+ 个具体数值），超过写作规范建议的 2-3 个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"保留 F1=0.694 和核心效应量描述，移除 CI、DDR 阈值细节。\"}\n  action_items:\n    - {round: 24, action: \"Abstract 精简至 2-3 个关键数字\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"Related Work 缺少 ordinal classification in NLP 的专门讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"论文将 task 框架为 ordinal classification 但 Related Work 无对应子章节。\"}\n  action_items:\n    - {round: 24, action: \"Related Work 增加简短段落讨论 ordinal classification 框架及在 NLP 中的应用\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M4\"\n  summary: \"Pooled Cohen's d 异方差问题仅在附录讨论，正文缺 caveat\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(minor),R2(agree)\", note: \"正文 §4.2 仅报告 pooled d，Glass's Δ 在 Appendix V。\"}\n  action_items:\n    - {round: 24, action: \"§4.2 添加一句 caveat 并引用 Appendix V 的 Glass's Δ 结果\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M5\"\n  summary: \"未探索 n-gram 和句法特征，缺少相关 detection methods 引用\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(minor),R2(agree)\", note: \"Limitations L31 已提及但无引用支撑。\"}\n  action_items:\n    - {round: 24, action: \"引用 n-gram based detection methods；contextualize 特征选择\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ R1-W2 RESOLVED (本轮) ============\n\n- id: \"R24-W2-dismissed\"\n  summary: \"参考模型 confound (R1 声称 cross-reference F1 降至 ~0.613)\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(提出),R2(rebut成功)\", note: \"R2 核查发现 R1 数据引用错误：0.613 来自 Appendix H perturbation experiment，非 cross-reference。实际 cross-reference spread=0.013 (Table 4)。R1 未在交叉回应中反驳。\"}\n  action_items: []\n  resolution: \"R1 数据引用错误。实际 cross-reference LOGO F1 spread=0.013，论文数据支持 reference-robust 声明。\"\n  resolution_round: 24\n\n# ============ PRIOR ROUNDS — STATUS UPDATE ============\n\n- id: \"R1-N1\"\n  summary: \"DDR tri-partition 阈值统计基础不可靠：异方差下使用 Cohen's d\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提，R2 AGREE\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"补充 Glass's Δ + Cliff's δ\"}\n    - {round: 23, reviewers: \"R1(warning),R2(rebut)\", note: \"R1 仍标记正文依赖 pooled d；R2 认为仅为 minor presentation issue。\"}\n    - {round: 24, reviewers: \"\", note: \"本轮合并至 R24-N1（DDR 阈值问题扩展版）。正文已加入 Glass's Δ ≥9.5×，但 drifting boundary 敏感性分析仍缺。\"}\n  action_items:\n    - {round: 22, action: \"Glass's Δ + Cliff's δ added to appendix\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"§4.2 L54: 加入 Glass's Δ gap ≥9.5× 数字到正文\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"部分解决（Glass's Δ 已加入），剩余问题合并至 R24-N1\"\n  resolution_round: null\n\n- id: \"R23-N1\"\n  summary: \"Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage，论文 framing 与可靠评估之间存在落差\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提 critical，R2 agree 但认为接近 should-fix。Independent-seed 实验仅 2 generators 不足以验证。需 full 8-gen independent-seed 3-class F1。\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"论文已采用 binary F1 (gen-1 vs gen-2+) 作为 primary metric 完全规避 gen-0 leakage。Seed sharing 控制得当。但 independent-seed 覆盖率仍不足 (2/8)，见 R24-W4。\"}\n  action_items:\n    - {round: 23, action: \"Text fix: Table 1 caption 重写，显著标注 seed sharing + independent-seed control 引用。Abstract 移除 3-class F1。Binary 为唯一 primary metric。\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"Binary F1 作为 primary metric 解决了 gen-0 leakage 问题。剩余 independent-seed 覆盖率问题见 R24-W4\"\n  resolution_round: null\n\n- id: \"R23-N2\"\n  summary: \"下游效用实验 n=3 统计效力不足，且结果否定 depth classification 的数据筛选价值\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R2 标记 critical（动机自我否定），R1 标记 warning（统计效力）。\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"Contribution 4 已移除，但 Discussion 仍做定性结论。合并至 R24-N2。\"}\n  action_items:\n    - {round: 23, action: \"移除 Contribution 4（downstream null result），从4条变3条。downstream 仅保留在 Discussion L16-17 作为 preliminary observation。\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"Contribution 4 已移除。剩余措辞问题合并至 R24-N2\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"DDR '框架' 的理论贡献是否被过度包装\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1(rebut),R2(critical)\", note: \"Director 判断倾向 R1，但降低包装力度\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"本轮合并至 R24-W2（DDR 贡献偏薄）。'framework' → 'empirical decomposition' 已完成。\"}\n  action_items:\n    - {round: 23, action: \"discussion.tex: 'framework' → 'empirical decomposition'; results.tex: 'DDR framework' → 'DDR decomposition'\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"术语已降级。剩余问题合并至 R24-W2\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Tail decay 作为 'near-stationary' 特征分类统计支撑不足（TOST 4/8）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 22, reviewers: \"R1,R2\", note: \"建议提升为 Limitations 首条\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"|d|=0.15-0.22 已接近 intermediate 区间(d=0.16)。\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未被明确单独提及。合并至 R24-N1 的 drifting boundary 敏感性分析中。\"}\n  action_items:\n    - {round: 23, action: \"§4.2 已有充分讨论 tail decay 边界地位\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"正文讨论已充分，剩余问题合并至 R24-N1\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"Introduction model collapse/provenance 双动机在 Discussion 中发展不均衡\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"Provenance 方向在 downstream 实验后基本被放弃，但 Intro 仍保留此动机。\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未被明确重提。Intro 已移除 provenance 引用/定义（R23 修复），聚焦 model collapse / scientific characterization。\"}\n  action_items:\n    - {round: 23, action: \"Intro L5 移除 provenance 引用。Intro L8 移除 provenance 定义。Contribution 4 (downstream) 移除。\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"Figure 1 x轴标签字体偏小，打印后可能低于 7pt\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未被明确重提，但未确认修复。\"}\n  action_items:\n    - {round: 23, action: \"需检查 Figure 1 生成脚本中字体大小设置\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ RESOLVED (prior rounds) ============\n\n- id: \"R1-N2-old\"\n  summary: \"DDR 3/1/3 partition post-hoc 选择，统计证据弱于 2-group structure\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"§4.2 重构为 2-group primary + 3/1/3 domain-informed refinement。R23 未重提\"\n  resolution_round: 23\n\n- id: \"R2-N1-old\"\n  summary: \"Framing 矛盾：Introduction 实用动机 vs Discussion 诊断定位\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"修改了 Intro L5, L9\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"Intro 仍在 provenance/diagnostic 之间摇摆\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未单独重提。Intro 已聚焦 model collapse / scientific characterization。Related Work §2.4 仍保留 provenance 子章节但定位为 complementary signal。\"}\n  action_items:\n    - {round: 23, action: \"Intro 移除 provenance 引用+定义，单一聚焦 model collapse / scientific characterization\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2-old\"\n  summary: \"新颖性受限：三篇并行工作收敛于 ~3 classes\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Novelty 已锚定在 DDR 分解（非分类任务本身）。R23 未重提\"\n  resolution_round: 23\n\n- id: \"R1-N5\"\n  summary: \"QLoRA F1=0.905 是否削弱 DDR 框架贡献\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1,R2\", note: \"R2 认为 QLoRA 被'藏'在附录。R1 rebut：QLoRA 高 F1 恰恰支持论文论点（depth signal 真实存在），handcrafted features 的价值在 interpretability。\"}\n  resolution: \"QLoRA 定位为验证 depth signal 存在，非竞争方法。R24 R1 在交叉回应中明确辩护。\"\n  resolution_round: 24\n\n- id: \"R2-W4\"\n  summary: \"正文可能超8页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"Main content ≤8 pages confirmed\"\n  resolution_round: 21\n\n- id: \"R22-M2\"\n  summary: \"Abstract 中 LLM 缩写未展开\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Changed to 'large language models (LLMs)'\"\n  resolution_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "# Round 24 Review Issues — Fresh review (no prior round memory)\n# Updated after R24 cross-sharing convergence\n\n# ============ CRITICAL (Must-Fix) ============\n\n- id: \"R1-N2\"\n  summary: \"仅限 base model 的限制对论文 significance 造成根本性约束\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"严重性取决于 framing; 科学发现定位使其降为 design scope\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"两位 Reviewer 再次一致标记 critical。论文多处措辞暗示超出 base-model 范围的一般性。\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"R2 标 Critical（instruct model 上 OLMo F1=0.338，web text 几乎全部来自 instruct models），R1 降为 Major（foundational study 合理范围界定）。Director 判定 Major-Critical。\"}\n  action_items:\n    - {round: 21, action: \"Abstract + Contribution 均加 scope limitation\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 22, action: \"No additional change needed — resolved by C2 framing adjustment to scientific characterization\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"Abstract 重写前置 base-model scope；Intro L5 'how language models' → 'how base language models'；Intro L5 移除 provenance 引用；Intro L8 移除 provenance 定义\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"论文标题已含 'Base LLM'，Abstract/Intro 已前置 scope。需补充 concrete deployment scenario（如 pretraining data filtering pipeline）。需论证 base-model study 的独立价值\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N1\"\n  summary: \"DDR tri-partition 阈值 (d=0.75/0.10) 缺乏 principled 依据，drifting boundary 未做敏感性分析\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提异方差下 Cohen's d 问题\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"补充 Glass's Δ + Cliff's δ\"}\n    - {round: 23, reviewers: \"R1(warning),R2(rebut)\", note: \"R1 仍标记正文依赖 pooled d\"}\n    - {round: 24, reviewers: \"R1(critical),R2(agree-降级major)\", note: \"R1 标 Critical：0.75 未解释选择理由，敏感性分析仅覆盖 near-stationary boundary。R2 同意问题存在但认为 data-driven clustering (silhouette=0.632) 和 9.5× gap 提供了独立验证，降为 Major。\"}\n  action_items:\n    - {round: 22, action: \"Glass's Δ + Cliff's δ added to appendix\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"§4.2 L54: 加入 Glass's Δ gap ≥9.5× 数字到正文\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"补充 drifting 阈值完整敏感性分析 (d=0.3-1.0)；说明 0.75 选择理由或改用 data-driven cutpoint；展示 entropy_std 在不同阈值下的分类稳定性\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N2\"\n  summary: \"下游效用实验 n=3 seeds 严重 underpowered，不足以支撑等价性声明\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提(warning)，R2同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"升级 critical\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"再次确认。合并至 R23-N2。Contribution 4 已移除\"}\n    - {round: 24, reviewers: \"R1(critical),R2(minor→agree escalate)\", note: \"R1 标 Critical。R2 初始标 Minor，交叉后被 R1 说服——论文虽已从 contribution list 移除 downstream，但 Discussion §5 L17 仍做定性结论。R1 指出 n=3 TOST power 极低，论文自承 Cohen's d unreliable。\"}\n  action_items:\n    - {round: 22, action: \"Discussion restructured to demote downstream evidence\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"Contribution 4 完全移除。downstream 仅保留在 Discussion 作为 preliminary observation\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"Discussion §5 L17 结论措辞改为 'preliminary evidence suggests...'；Appendix L 标注为 pilot experiment\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MAJOR (Should-Fix) ============\n\n- id: \"R24-W1\"\n  summary: \"三个 drifting 特征 (r=0.81-0.97, PCA 92.3%) 本质是同一 latent factor，DDR 3/1/3 在独立信息维度上更接近 1/1/3\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"TTR-hapax r=0.97，entropy_mean-TTR r=0.86。需 PCA/factor analysis。\"}\n    - {round: 24, reviewers: \"R1(major),R2(强烈同意)\", note: \"R1：DDR 3/1/3 在独立信息维度上更接近 1/1/3。R2 强烈同意。论文 §4.2 L81 自承 permutation importance 差异是 feature masking 而非独立信号。PCA 已做 (92.3% by PC1) 但叙事未调整。\"}\n  action_items:\n    - {round: 23, action: \"§4.2 加入 PCA 结论句。Appendix feature correlation 加入详细 PCA 结果。\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 24, action: \"调整叙事：承认三个 drifting 特征共享单一 latent dimension；考虑报告 PC1 替换实验（R1-Q5）；避免将 '3 drifting features' 作为 'rich feature drift' 的证据\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W2\"\n  summary: \"DDR 作为 EMNLP 核心贡献偏薄：本质是特征敏感度分析 + post-hoc empirical 解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"R2：核心是 'some features are more sensitive to recursive generation than others' 的系统化表述。R1 同意并补充：DDR 缺乏 predictive power。作为 Findings 合适，不够 main conference。\"}\n  action_items:\n    - {round: 24, action: \"考虑提供 DDR 的更严谨 mechanistic explanation 或形式化分析；或更明确定位为 descriptive framework\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W3\"\n  summary: \"Contribution #3 (parameter dependence) 本质是 negative result，列为贡献逻辑不自洽\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"R2：将 '方法在某些条件下失效' 列为贡献不自洽。R1 同意但指出温度 boundary condition 有操作价值。共识：reframe 为 Discussion 中的 boundary conditions。\"}\n  action_items:\n    - {round: 24, action: \"Contribution #3 reframe 为 'boundary conditions' 或整合入 Discussion；或改为正面表述 'We characterize DDR's validity regime'\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W4\"\n  summary: \"Independent-seed 控制仅覆盖 2/8 generators (25%)，不足以支撑跨家族泛化声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(major),R2(agree)\", note: \"仅 Pythia-2.8B 和 OLMo-2-1B。Qwen/Llama/Mistral 的 seed sharing 效应未验证。\"}\n  action_items:\n    - {round: 24, action: \"至少为每个家族各选一个 generator 做 independent-seed 控制\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MINOR / INFO ============\n\n- id: \"R24-M1\"\n  summary: \"LOGO 同家族泄漏未在主表 (Table 1) 中体现，LOFO 仅在文中提及\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(major),R2(agree-低严重性)\", note: \"LOFO 0.686 vs LOGO 0.694，差 0.8pp。R2 认为 LOGO 作为主指标合理（LOFO fold 不均衡），在 Table 1 增加 LOFO 行更透明。\"}\n  action_items:\n    - {round: 24, action: \"Table 1 增加 LOFO binary F1 行\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M2\"\n  summary: \"Abstract 数字过多（7+ 个具体数值），超过写作规范建议的 2-3 个\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"保留 F1=0.694 和核心效应量描述，移除 CI、DDR 阈值细节。\"}\n  action_items:\n    - {round: 24, action: \"Abstract 精简至 2-3 个关键数字\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"Related Work 缺少 ordinal classification in NLP 的专门讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(agree),R2(提出)\", note: \"论文将 task 框架为 ordinal classification 但 Related Work 无对应子章节。\"}\n  action_items:\n    - {round: 24, action: \"Related Work 增加简短段落讨论 ordinal classification 框架及在 NLP 中的应用\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M4\"\n  summary: \"Pooled Cohen's d 异方差问题仅在附录讨论，正文缺 caveat\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(minor),R2(agree)\", note: \"正文 §4.2 仅报告 pooled d，Glass's Δ 在 Appendix V。\"}\n  action_items:\n    - {round: 24, action: \"§4.2 添加一句 caveat 并引用 Appendix V 的 Glass's Δ 结果\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M5\"\n  summary: \"未探索 n-gram 和句法特征，缺少相关 detection methods 引用\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(minor),R2(agree)\", note: \"Limitations L31 已提及但无引用支撑。\"}\n  action_items:\n    - {round: 24, action: \"引用 n-gram based detection methods；contextualize 特征选择\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ R1-W2 RESOLVED (本轮) ============\n\n- id: \"R24-W2-dismissed\"\n  summary: \"参考模型 confound (R1 声称 cross-reference F1 降至 ~0.613)\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1(提出),R2(rebut成功)\", note: \"R2 核查发现 R1 数据引用错误：0.613 来自 Appendix H perturbation experiment，非 cross-reference。实际 cross-reference spread=0.013 (Table 4)。R1 未在交叉回应中反驳。\"}\n  action_items: []\n  resolution: \"R1 数据引用错误。实际 cross-reference LOGO F1 spread=0.013，论文数据支持 reference-robust 声明。\"\n  resolution_round: 24\n\n# ============ PRIOR ROUNDS — STATUS UPDATE ============\n\n- id: \"R1-N1\"\n  summary: \"DDR tri-partition 阈值统计基础不可靠：异方差下使用 Cohen's d\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R1首提，R2 AGREE\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"补充 Glass's Δ + Cliff's δ\"}\n    - {round: 23, reviewers: \"R1(warning),R2(rebut)\", note: \"R1 仍标记正文依赖 pooled d；R2 认为仅为 minor presentation issue。\"}\n    - {round: 24, reviewers: \"\", note: \"本轮合并至 R24-N1（DDR 阈值问题扩展版）。正文已加入 Glass's Δ ≥9.5×，但 drifting boundary 敏感性分析仍缺。\"}\n  action_items:\n    - {round: 22, action: \"Glass's Δ + Cliff's δ added to appendix\", assigned_to: \"Director\", status: \"done\"}\n    - {round: 23, action: \"§4.2 L54: 加入 Glass's Δ gap ≥9.5× 数字到正文\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"部分解决（Glass's Δ 已加入），剩余问题合并至 R24-N1\"\n  resolution_round: null\n\n- id: \"R23-N1\"\n  summary: \"Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage，论文 framing 与可靠评估之间存在落差\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R1首提 critical，R2 agree 但认为接近 should-fix。Independent-seed 实验仅 2 generators 不足以验证。需 full 8-gen independent-seed 3-class F1。\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"论文已采用 binary F1 (gen-1 vs gen-2+) 作为 primary metric 完全规避 gen-0 leakage。Seed sharing 控制得当。但 independent-seed 覆盖率仍不足 (2/8)，见 R24-W4。\"}\n  action_items:\n    - {round: 23, action: \"Text fix: Table 1 caption 重写，显著标注 seed sharing + independent-seed control 引用。Abstract 移除 3-class F1。Binary 为唯一 primary metric。\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"Binary F1 作为 primary metric 解决了 gen-0 leakage 问题。剩余 independent-seed 覆盖率问题见 R24-W4\"\n  resolution_round: null\n\n- id: \"R23-N2\"\n  summary: \"下游效用实验 n=3 统计效力不足，且结果否定 depth classification 的数据筛选价值\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1,R2\", note: \"R2 标记 critical（动机自我否定），R1 标记 warning（统计效力）。\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"Contribution 4 已移除，但 Discussion 仍做定性结论。合并至 R24-N2。\"}\n  action_items:\n    - {round: 23, action: \"移除 Contribution 4（downstream null result），从4条变3条。downstream 仅保留在 Discussion L16-17 作为 preliminary observation。\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"Contribution 4 已移除。剩余措辞问题合并至 R24-N2\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"DDR '框架' 的理论贡献是否被过度包装\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1(rebut),R2(critical)\", note: \"Director 判断倾向 R1，但降低包装力度\"}\n    - {round: 24, reviewers: \"R1,R2\", note: \"本轮合并至 R24-W2（DDR 贡献偏薄）。'framework' → 'empirical decomposition' 已完成。\"}\n  action_items:\n    - {round: 23, action: \"discussion.tex: 'framework' → 'empirical decomposition'; results.tex: 'DDR framework' → 'DDR decomposition'\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"术语已降级。剩余问题合并至 R24-W2\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Tail decay 作为 'near-stationary' 特征分类统计支撑不足（TOST 4/8）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 22, reviewers: \"R1,R2\", note: \"建议提升为 Limitations 首条\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"|d|=0.15-0.22 已接近 intermediate 区间(d=0.16)。\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未被明确单独提及。合并至 R24-N1 的 drifting boundary 敏感性分析中。\"}\n  action_items:\n    - {round: 23, action: \"§4.2 已有充分讨论 tail decay 边界地位\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"正文讨论已充分，剩余问题合并至 R24-N1\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"Introduction model collapse/provenance 双动机在 Discussion 中发展不均衡\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"Provenance 方向在 downstream 实验后基本被放弃，但 Intro 仍保留此动机。\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未被明确重提。Intro 已移除 provenance 引用/定义（R23 修复），聚焦 model collapse / scientific characterization。\"}\n  action_items:\n    - {round: 23, action: \"Intro L5 移除 provenance 引用。Intro L8 移除 provenance 定义。Contribution 4 (downstream) 移除。\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"Figure 1 x轴标签字体偏小，打印后可能低于 7pt\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: \"R1(agree),R2(提出)\", note: \"\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未被明确重提，但未确认修复。\"}\n  action_items:\n    - {round: 23, action: \"需检查 Figure 1 生成脚本中字体大小设置\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ RESOLVED (prior rounds) ============\n\n- id: \"R1-N2-old\"\n  summary: \"DDR 3/1/3 partition post-hoc 选择，统计证据弱于 2-group structure\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"§4.2 重构为 2-group primary + 3/1/3 domain-informed refinement。R23 未重提\"\n  resolution_round: 23\n\n- id: \"R2-N1-old\"\n  summary: \"Framing 矛盾：Introduction 实用动机 vs Discussion 诊断定位\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 21, reviewers: \"R1,R2\", note: \"R2首提，R1完全同意\"}\n    - {round: 22, reviewers: \"R1,R2\", note: \"修改了 Intro L5, L9\"}\n    - {round: 23, reviewers: \"R1,R2\", note: \"Intro 仍在 provenance/diagnostic 之间摇摆\"}\n    - {round: 24, reviewers: \"\", note: \"本轮未单独重提。Intro 已聚焦 model collapse / scientific characterization。Related Work §2.4 仍保留 provenance 子章节但定位为 complementary signal。\"}\n  action_items:\n    - {round: 23, action: \"Intro 移除 provenance 引用+定义，单一聚焦 model collapse / scientific characterization\", assigned_to: \"Director\", status: \"done\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2-old\"\n  summary: \"新颖性受限：三篇并行工作收敛于 ~3 classes\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Novelty 已锚定在 DDR 分解（非分类任务本身）。R23 未重提\"\n  resolution_round: 23\n\n- id: \"R1-N5\"\n  summary: \"QLoRA F1=0.905 是否削弱 DDR 框架贡献\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: \"R1,R2\", note: \"R2 认为 QLoRA 被'藏'在附录。R1 rebut：QLoRA 高 F1 恰恰支持论文论点（depth signal 真实存在），handcrafted features 的价值在 interpretability。\"}\n  resolution: \"QLoRA 定位为验证 depth signal 存在，非竞争方法。R24 R1 在交叉回应中明确辩护。\"\n  resolution_round: 24\n\n- id: \"R2-W4\"\n  summary: \"正文可能超8页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"Main content ≤8 pages confirmed\"\n  resolution_round: 21\n\n- id: \"R22-M2\"\n  summary: \"Abstract 中 LLM 缩写未展开\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Changed to 'large language models (LLMs)'\"\n  resolution_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-19T04:20:11.891360+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 16532}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-19T04:22:19.581100+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "report": "# Round 24 审稿报告 — gen-depth-fingerprint\n\n**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计推断；R2: 新颖性+完整性+写作质量+格式合规）\n**轮次**: Round 1 + 交叉分享（1 轮收敛）\n**外部审稿**: 未配置\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务——将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（递归生成），取代传统二分类检测。通过 7 个手工特征（5 个参考模型 NLL 统计量 + 2 个表面词汇多样性特征）和 XGBoost 分类器，在 8 个 base model generator（Pythia/OLMo/Qwen/Llama/Mistral，0.6B–8B）上实现 LOGO binary F1=0.694。核心发现是 differential depth response (DDR)：特征分为 drifting（entropy mean, TTR, hapax ratio）、intermediate（entropy std）和 near-stationary（entropy max, tail decay, entropy min）三组，与递归生成下 NLL location shift / shape stability 的解释一致。论文诚实地将贡献定位为 \"empirical rather than methodological\"。\n\n---\n\n## Strengths\n\n**S1. 新颖且有实际意义的任务定义。** [R1,R2 共识] 从 binary real-vs-synthetic 推进到 ordinal depth classification 是有意义的方向扩展，与 model collapse 和数据溯源有清晰关联。这是一个之前未被正式定义的研究问题。\n\n**S2. 评估协议严谨且透明。** [R1,R2 共识] LOGO + LOFO 双重评估，配套 independent-seed、length matching、cross-domain、cross-temperature、prompt type sensitivity 等多项控制实验。覆盖度在 EMNLP 投稿中属上乘。\n\n**S3. 诚实的学术态度。** [R1,R2 共识] 论文主动标注 gen-0 seed sharing 问题、下游 n=3 局限、QLoRA 天花板与手工特征的 tradeoff。Limitations section 详尽（34 行，8+ 项局限）。\n\n**S4. 可解释的方法设计。** [R1,R2 共识] 7 个手工特征完全透明可分析，DDR 框架为理解递归生成下文本属性的演化提供了有用的概念结构。\n\n**S5. 附录覆盖全面。** [R1,R2 共识] 20+ 页附录涵盖 16 个实验板块，覆盖了几乎所有可预见的审稿问题。\n\n**S6. 与 concurrent work 定位清晰。** [R2] 对 Broken Telephone 和 Markovian Chains 的区分有说服力，三个独立工作收敛于 ~3 class ceiling 的讨论增强了可信度。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**N1. Base model 限制严重削弱论文 significance。** [R2 Critical, R1 Major]\n- OLMo-2-1B-Instruct LOGO F1 从 0.763 暴跌至 0.338；Llama 3-class F1 从 0.742 降至 0.544\n- 现实 web text 几乎全部由 instruct/RLHF 模型生成，base model 直接生成的文本在实际场景中极为罕见\n- 论文将此框架为设计选择（\"We restrict to base models, since instruction-tuning introduces confounds\"），但实质是核心限制\n- R1 认为对于 foundational study 此范围界定合理，R2 认为这严重削弱 impact\n- **Director 判定**: Major-Critical。论文标题已含 \"Base LLM\"，scope 透明；但缺少 concrete deployment scenario 论证 base-model study 的独立实际价值\n\n**N2. DDR tri-partition 阈值缺乏 principled 依据。** [R1 Critical, R2 同意降为 Major]\n- Cohen's d 阈值 0.75 介于惯例 medium (0.5) 和 large (0.8) 之间，未说明选择理由\n- 敏感性分析仅覆盖 near-stationary boundary，未检验 drifting boundary\n- 若阈值降至 0.5，entropy_std (d=0.55) 将从 intermediate 重分类为 drifting，改变 DDR 叙事\n- R2 指出 data-driven clustering (silhouette=0.632) 和 9.5× gap 提供了独立验证\n- **Director 判定**: Major。data-driven 验证降低了风险，但阈值选择仍需 justification\n\n**N3. 下游效用实验 n=3 seeds 严重 underpowered。** [R1 Critical, R2 初标 Minor 后同意升级]\n- n=3 时 TOST power 极低，论文自承 Cohen's d \"unreliable\"\n- Discussion §5 L17 仍做定性结论（\"depth composition does not determine training utility\"），该声明无法由 n=3 支撑\n- 虽已从 contribution list 移除，但 Discussion 中的结论措辞需降格为 \"preliminary evidence\"\n\n### Major\n\n**W1. 三个 drifting 特征本质是同一 latent factor。** [R1,R2 强烈共识]\n- entropy mean、TTR、hapax ratio 相关性 r=0.81-0.97，PCA 92.3% by PC1\n- DDR 3/1/3 在独立信息维度上更接近 1/1/3\n- 论文自承 permutation importance 差异反映 feature masking 而非独立信号\n- \"7-feature ensemble\" / \"three drifting features\" 的表述可能误导读者关于独立信息维度数量\n\n**W2. DDR 作为 EMNLP 核心贡献偏薄。** [R1,R2 共识]\n- 核心发现是 \"some features are more sensitive to recursive generation than others\" 的系统化表述\n- 自承 \"post-hoc and empirical\"，无理论解释，缺乏 predictive power\n- 作为 Findings 贡献合适，不够 main conference\n- 需要更严谨的 mechanistic explanation 或形式化分析来增强深度\n\n**W3. Contribution #3 (parameter dependence) 本质是 negative result。** [R1,R2 共识]\n- 将 \"方法在某些条件下失效\"（instruction tuning, t=0.9）列为贡献逻辑不自洽\n- R1 指出温度 boundary condition 有操作价值\n- 建议 reframe 为 Discussion 中的 \"boundary conditions\"\n\n**W4. Independent-seed 控制覆盖率不足。** [R1,R2 共识]\n- 仅 2/8 generators (Pythia-2.8B, OLMo-2-1B)，覆盖 2/5 家族\n- F1 差距可忽略 (0.680 vs 0.694)，但 Qwen/Llama/Mistral 未验证\n\n### Minor\n\n**M1. LOGO 同家族泄漏未在 Table 1 体现。** [R1 Major, R2 降级] LOFO 0.686 vs LOGO 0.694，差 0.8pp。建议 Table 1 增加 LOFO 行。\n\n**M2. Abstract 数字过多。** [R1,R2 共识] 7+ 个具体数值，建议精简至 2-3 个。\n\n**M3. Related Work 缺少 ordinal classification in NLP 讨论。** [R1,R2 共识] 论文将 task 框架为 ordinal classification 但 Related Work 无对应子章节。\n\n**M4. Pooled Cohen's d 异方差问题仅在附录讨论。** [R1,R2 共识] 正文需添加 caveat。\n\n**M5. 未探索 n-gram/句法特征，缺少相关引用。** [R1,R2 共识]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 3.0 (Findings)**: 两位 Reviewer 独立给出相同评分\n2. **任务定义新颖 + 实验严谨 → 达到 Findings 门槛**\n3. **DDR 贡献偏 empirical + base-model 限制 + 性能偏低 → 不够 Conference**\n4. **Contribution #3 定位不当**: 需 reframe\n5. **三个 drifting 特征高度冗余**: 3/1/3 叙事需调整\n6. **下游 n=3 underpowered**: 结论措辞需降格\n7. **附录覆盖和学术诚实度为论文最突出优点**\n\n## Reviewer Divergence [REBUT]\n\n1. **Base model 限制严重程度**: R2=Critical（实际场景失效）vs R1=Major（foundational study 合理范围）。Director 判定 Major-Critical：scope 透明但需补充 deployment scenario 论证。\n\n2. **F1=0.694 是否偏低**: R2=Major（QLoRA 0.905 说明远非最优）vs R1=REBUT（指标不可比：8-gen binary LOGO vs 6-gen 3-class QLoRA；LOGO 是极严格评估；QLoRA 高 F1 恰恰支持 depth signal 存在）。Director 判定：R1 论据更有力——R2 的对比存在指标和评估集不匹配问题。F1=0.694 在 LOGO 下对 foundational study 可接受。\n\n3. **R1-W2 参考模型 confound**: R1 声称 cross-reference F1 降至 ~0.613。R2 核查发现 R1 数据引用错误（0.613 来自 Appendix H perturbation experiment，非 cross-reference；实际 spread=0.013）。**R1 未在交叉回应中反驳此点。Director 判定：R1-W2 dismissed**，参考模型 confound 不构成实质问题。\n\n4. **下游 n=3 严重程度**: R1=Critical vs R2=Minor。R1 在交叉回应中成功说服 R2 升级。Director 判定：论文已将 downstream 从 contribution list 移除，降为 Major-Critical——需修改 Discussion 措辞但不再影响核心评分。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R2, R1 同意] 请具体描述 base-model depth profiling 的实际部署场景。在什么现实应用中需要判断文本经历了多少代 base model 递归生成？\n\n**Q2.** [R1] 若将 drifting 阈值从 0.75 降至 0.5，DDR 的三分叙事如何变化？请提供 drifting boundary 的完整敏感性分析。\n\n**Q3.** [R2] QLoRA 端到端模型在 instruct model 上的表现如何？它是否能部分克服 base model 限制？\n\n**Q4.** [R1] 三个 drifting 特征替换为其第一主成分后，分类性能是否变化？这能直接检验它们是否携带独立信息。\n\n**Q5.** [R2] Cross-model chains F1=0.764 高于 LOGO 0.694——depth signal 在 generator 混合时反而更强？R1 指出评估协议差异（5-fold CV vs LOGO）可能解释部分 gap。\n\n---\n\n## Missing References\n\n- **Ordinal classification in NLP**: 缺少 ordinal classification 在 NLP 任务中的应用文献（如 sentiment ordinal approaches） [R1,R2 共识]\n- **N-gram based detection methods**: 论文特征集不含 n-gram 特征，需引用相关方法 contextualize 特征选择 [R1,R2 共识]\n- **Distribution shift 文献**: DDR 本质是 distribution shift 现象，可引用经典框架（covariate shift, dataset shift）[R2, R1 部分同意]\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Clarity | — | 4/5 | 4/5 |\n\n**ARR 评分**: 3.0 = Findings（可被 Findings 接收）\n\n**综合评价**: 论文定义了一个新颖且有意义的任务（generation depth classification），以高标准的实验设计和学术诚实度支撑了一个有趣的 empirical 发现（DDR tri-partition）。评估协议（LOGO/LOFO + 多项控制实验）和附录覆盖度远超平均水平。然而，三个核心问题制约了评分：(1) base-model-only 限制使得方法在实际场景（instruct models）中性能严重退化，significance 受限；(2) DDR 作为纯 empirical 贡献缺乏理论深度和 predictive power，三个 drifting 特征本质是同一 latent factor，3/1/3 叙事有误导性；(3) 部分声明的统计基础不够稳固（DDR 阈值选择、下游 n=3）。整体达到 Findings 水准——新颖任务定义 + 严谨实验 + 诚实报告构成 solid 但 non-exciting 的贡献。修复阈值敏感性分析、调整 drifting 特征叙事、补充 base-model deployment scenario 后有潜力升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments（按章节）\n\n### Abstract\n- 数字过密（7+ 个具体数值），建议精简至 F1=0.694 和一个核心效应量描述\n- \"instruction tuning\" 限制的提及方式得当\n\n### Introduction\n- Contribution #3 需 reframe：将 parameter dependence 从 \"贡献\" 改为 Discussion 中的 boundary conditions\n- 叙事聚焦 model collapse / scientific characterization 方向正确\n\n### Related Work\n- 缺少 ordinal classification in NLP 子章节\n- 与 concurrent works 的区分清晰有效\n- 需补充 n-gram detection methods 和 distribution shift 文献\n\n### Method\n- 特征选择动机清晰，两组特征（reference-model + surface）的互补性论证充分\n- 需在 §3.3 简要说明为何排除 n-gram/句法特征\n\n### Results\n- Table 1 建议增加 LOFO binary F1 行\n- §4.2 DDR 部分需补充 drifting boundary 敏感性分析\n- §4.2 需在正文添加 pooled Cohen's d 异方差 caveat\n- 三个 drifting 特征的叙事需调整为 \"single latent diversity/entropy factor\"\n\n### Discussion\n- §5 L17 下游结论需降格为 \"preliminary evidence suggests...\"\n- DDR 的 post-hoc / empirical 定位诚实但限制了贡献深度\n\n### Limitations\n- 详尽全面，是论文最佳章节之一\n- 所有关键限制均已覆盖\n\n### Format\n- 正文 8 页，符合 ARR Long Paper 要求\n- 模板 `\\usepackage[review]{acl}` 正确\n- 匿名化到位\n- Figure 1 x 轴标签字体可能低于 7pt（需检查）",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "report": "# Round 24 审稿报告 — gen-depth-fingerprint\n\n**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计推断；R2: 新颖性+完整性+写作质量+格式合规）\n**轮次**: Round 1 + 交叉分享（1 轮收敛）\n**外部审稿**: 未配置\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务——将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（递归生成），取代传统二分类检测。通过 7 个手工特征（5 个参考模型 NLL 统计量 + 2 个表面词汇多样性特征）和 XGBoost 分类器，在 8 个 base model generator（Pythia/OLMo/Qwen/Llama/Mistral，0.6B–8B）上实现 LOGO binary F1=0.694。核心发现是 differential depth response (DDR)：特征分为 drifting（entropy mean, TTR, hapax ratio）、intermediate（entropy std）和 near-stationary（entropy max, tail decay, entropy min）三组，与递归生成下 NLL location shift / shape stability 的解释一致。论文诚实地将贡献定位为 \"empirical rather than methodological\"。\n\n---\n\n## Strengths\n\n**S1. 新颖且有实际意义的任务定义。** [R1,R2 共识] 从 binary real-vs-synthetic 推进到 ordinal depth classification 是有意义的方向扩展，与 model collapse 和数据溯源有清晰关联。这是一个之前未被正式定义的研究问题。\n\n**S2. 评估协议严谨且透明。** [R1,R2 共识] LOGO + LOFO 双重评估，配套 independent-seed、length matching、cross-domain、cross-temperature、prompt type sensitivity 等多项控制实验。覆盖度在 EMNLP 投稿中属上乘。\n\n**S3. 诚实的学术态度。** [R1,R2 共识] 论文主动标注 gen-0 seed sharing 问题、下游 n=3 局限、QLoRA 天花板与手工特征的 tradeoff。Limitations section 详尽（34 行，8+ 项局限）。\n\n**S4. 可解释的方法设计。** [R1,R2 共识] 7 个手工特征完全透明可分析，DDR 框架为理解递归生成下文本属性的演化提供了有用的概念结构。\n\n**S5. 附录覆盖全面。** [R1,R2 共识] 20+ 页附录涵盖 16 个实验板块，覆盖了几乎所有可预见的审稿问题。\n\n**S6. 与 concurrent work 定位清晰。** [R2] 对 Broken Telephone 和 Markovian Chains 的区分有说服力，三个独立工作收敛于 ~3 class ceiling 的讨论增强了可信度。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**N1. Base model 限制严重削弱论文 significance。** [R2 Critical, R1 Major]\n- OLMo-2-1B-Instruct LOGO F1 从 0.763 暴跌至 0.338；Llama 3-class F1 从 0.742 降至 0.544\n- 现实 web text 几乎全部由 instruct/RLHF 模型生成，base model 直接生成的文本在实际场景中极为罕见\n- 论文将此框架为设计选择（\"We restrict to base models, since instruction-tuning introduces confounds\"），但实质是核心限制\n- R1 认为对于 foundational study 此范围界定合理，R2 认为这严重削弱 impact\n- **Director 判定**: Major-Critical。论文标题已含 \"Base LLM\"，scope 透明；但缺少 concrete deployment scenario 论证 base-model study 的独立实际价值\n\n**N2. DDR tri-partition 阈值缺乏 principled 依据。** [R1 Critical, R2 同意降为 Major]\n- Cohen's d 阈值 0.75 介于惯例 medium (0.5) 和 large (0.8) 之间，未说明选择理由\n- 敏感性分析仅覆盖 near-stationary boundary，未检验 drifting boundary\n- 若阈值降至 0.5，entropy_std (d=0.55) 将从 intermediate 重分类为 drifting，改变 DDR 叙事\n- R2 指出 data-driven clustering (silhouette=0.632) 和 9.5× gap 提供了独立验证\n- **Director 判定**: Major。data-driven 验证降低了风险，但阈值选择仍需 justification\n\n**N3. 下游效用实验 n=3 seeds 严重 underpowered。** [R1 Critical, R2 初标 Minor 后同意升级]\n- n=3 时 TOST power 极低，论文自承 Cohen's d \"unreliable\"\n- Discussion §5 L17 仍做定性结论（\"depth composition does not determine training utility\"），该声明无法由 n=3 支撑\n- 虽已从 contribution list 移除，但 Discussion 中的结论措辞需降格为 \"preliminary evidence\"\n\n### Major\n\n**W1. 三个 drifting 特征本质是同一 latent factor。** [R1,R2 强烈共识]\n- entropy mean、TTR、hapax ratio 相关性 r=0.81-0.97，PCA 92.3% by PC1\n- DDR 3/1/3 在独立信息维度上更接近 1/1/3\n- 论文自承 permutation importance 差异反映 feature masking 而非独立信号\n- \"7-feature ensemble\" / \"three drifting features\" 的表述可能误导读者关于独立信息维度数量\n\n**W2. DDR 作为 EMNLP 核心贡献偏薄。** [R1,R2 共识]\n- 核心发现是 \"some features are more sensitive to recursive generation than others\" 的系统化表述\n- 自承 \"post-hoc and empirical\"，无理论解释，缺乏 predictive power\n- 作为 Findings 贡献合适，不够 main conference\n- 需要更严谨的 mechanistic explanation 或形式化分析来增强深度\n\n**W3. Contribution #3 (parameter dependence) 本质是 negative result。** [R1,R2 共识]\n- 将 \"方法在某些条件下失效\"（instruction tuning, t=0.9）列为贡献逻辑不自洽\n- R1 指出温度 boundary condition 有操作价值\n- 建议 reframe 为 Discussion 中的 \"boundary conditions\"\n\n**W4. Independent-seed 控制覆盖率不足。** [R1,R2 共识]\n- 仅 2/8 generators (Pythia-2.8B, OLMo-2-1B)，覆盖 2/5 家族\n- F1 差距可忽略 (0.680 vs 0.694)，但 Qwen/Llama/Mistral 未验证\n\n### Minor\n\n**M1. LOGO 同家族泄漏未在 Table 1 体现。** [R1 Major, R2 降级] LOFO 0.686 vs LOGO 0.694，差 0.8pp。建议 Table 1 增加 LOFO 行。\n\n**M2. Abstract 数字过多。** [R1,R2 共识] 7+ 个具体数值，建议精简至 2-3 个。\n\n**M3. Related Work 缺少 ordinal classification in NLP 讨论。** [R1,R2 共识] 论文将 task 框架为 ordinal classification 但 Related Work 无对应子章节。\n\n**M4. Pooled Cohen's d 异方差问题仅在附录讨论。** [R1,R2 共识] 正文需添加 caveat。\n\n**M5. 未探索 n-gram/句法特征，缺少相关引用。** [R1,R2 共识]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 3.0 (Findings)**: 两位 Reviewer 独立给出相同评分\n2. **任务定义新颖 + 实验严谨 → 达到 Findings 门槛**\n3. **DDR 贡献偏 empirical + base-model 限制 + 性能偏低 → 不够 Conference**\n4. **Contribution #3 定位不当**: 需 reframe\n5. **三个 drifting 特征高度冗余**: 3/1/3 叙事需调整\n6. **下游 n=3 underpowered**: 结论措辞需降格\n7. **附录覆盖和学术诚实度为论文最突出优点**\n\n## Reviewer Divergence [REBUT]\n\n1. **Base model 限制严重程度**: R2=Critical（实际场景失效）vs R1=Major（foundational study 合理范围）。Director 判定 Major-Critical：scope 透明但需补充 deployment scenario 论证。\n\n2. **F1=0.694 是否偏低**: R2=Major（QLoRA 0.905 说明远非最优）vs R1=REBUT（指标不可比：8-gen binary LOGO vs 6-gen 3-class QLoRA；LOGO 是极严格评估；QLoRA 高 F1 恰恰支持 depth signal 存在）。Director 判定：R1 论据更有力——R2 的对比存在指标和评估集不匹配问题。F1=0.694 在 LOGO 下对 foundational study 可接受。\n\n3. **R1-W2 参考模型 confound**: R1 声称 cross-reference F1 降至 ~0.613。R2 核查发现 R1 数据引用错误（0.613 来自 Appendix H perturbation experiment，非 cross-reference；实际 spread=0.013）。**R1 未在交叉回应中反驳此点。Director 判定：R1-W2 dismissed**，参考模型 confound 不构成实质问题。\n\n4. **下游 n=3 严重程度**: R1=Critical vs R2=Minor。R1 在交叉回应中成功说服 R2 升级。Director 判定：论文已将 downstream 从 contribution list 移除，降为 Major-Critical——需修改 Discussion 措辞但不再影响核心评分。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R2, R1 同意] 请具体描述 base-model depth profiling 的实际部署场景。在什么现实应用中需要判断文本经历了多少代 base model 递归生成？\n\n**Q2.** [R1] 若将 drifting 阈值从 0.75 降至 0.5，DDR 的三分叙事如何变化？请提供 drifting boundary 的完整敏感性分析。\n\n**Q3.** [R2] QLoRA 端到端模型在 instruct model 上的表现如何？它是否能部分克服 base model 限制？\n\n**Q4.** [R1] 三个 drifting 特征替换为其第一主成分后，分类性能是否变化？这能直接检验它们是否携带独立信息。\n\n**Q5.** [R2] Cross-model chains F1=0.764 高于 LOGO 0.694——depth signal 在 generator 混合时反而更强？R1 指出评估协议差异（5-fold CV vs LOGO）可能解释部分 gap。\n\n---\n\n## Missing References\n\n- **Ordinal classification in NLP**: 缺少 ordinal classification 在 NLP 任务中的应用文献（如 sentiment ordinal approaches） [R1,R2 共识]\n- **N-gram based detection methods**: 论文特征集不含 n-gram 特征，需引用相关方法 contextualize 特征选择 [R1,R2 共识]\n- **Distribution shift 文献**: DDR 本质是 distribution shift 现象，可引用经典框架（covariate shift, dataset shift）[R2, R1 部分同意]\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Clarity | — | 4/5 | 4/5 |\n\n**ARR 评分**: 3.0 = Findings（可被 Findings 接收）\n\n**综合评价**: 论文定义了一个新颖且有意义的任务（generation depth classification），以高标准的实验设计和学术诚实度支撑了一个有趣的 empirical 发现（DDR tri-partition）。评估协议（LOGO/LOFO + 多项控制实验）和附录覆盖度远超平均水平。然而，三个核心问题制约了评分：(1) base-model-only 限制使得方法在实际场景（instruct models）中性能严重退化，significance 受限；(2) DDR 作为纯 empirical 贡献缺乏理论深度和 predictive power，三个 drifting 特征本质是同一 latent factor，3/1/3 叙事有误导性；(3) 部分声明的统计基础不够稳固（DDR 阈值选择、下游 n=3）。整体达到 Findings 水准——新颖任务定义 + 严谨实验 + 诚实报告构成 solid 但 non-exciting 的贡献。修复阈值敏感性分析、调整 drifting 特征叙事、补充 base-model deployment scenario 后有潜力升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments（按章节）\n\n### Abstract\n- 数字过密（7+ 个具体数值），建议精简至 F1=0.694 和一个核心效应量描述\n- \"instruction tuning\" 限制的提及方式得当\n\n### Introduction\n- Contribution #3 需 reframe：将 parameter dependence 从 \"贡献\" 改为 Discussion 中的 boundary conditions\n- 叙事聚焦 model collapse / scientific characterization 方向正确\n\n### Related Work\n- 缺少 ordinal classification in NLP 子章节\n- 与 concurrent works 的区分清晰有效\n- 需补充 n-gram detection methods 和 distribution shift 文献\n\n### Method\n- 特征选择动机清晰，两组特征（reference-model + surface）的互补性论证充分\n- 需在 §3.3 简要说明为何排除 n-gram/句法特征\n\n### Results\n- Table 1 建议增加 LOFO binary F1 行\n- §4.2 DDR 部分需补充 drifting boundary 敏感性分析\n- §4.2 需在正文添加 pooled Cohen's d 异方差 caveat\n- 三个 drifting 特征的叙事需调整为 \"single latent diversity/entropy factor\"\n\n### Discussion\n- §5 L17 下游结论需降格为 \"preliminary evidence suggests...\"\n- DDR 的 post-hoc / empirical 定位诚实但限制了贡献深度\n\n### Limitations\n- 详尽全面，是论文最佳章节之一\n- 所有关键限制均已覆盖\n\n### Format\n- 正文 8 页，符合 ARR Long Paper 要求\n- 模板 `\\usepackage[review]{acl}` 正确\n- 匿名化到位\n- Figure 1 x 轴标签字体可能低于 7pt（需检查）",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-19T04:22:23.446759+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 1792 · 2026-05-19T04:22:31.123035+00:00_

审稿报告已投递至 Research Director。

**审稿完成摘要**：

- **Overall**: 3.0 (Findings)，两位 Reviewer 一致
- **核心优势**: 新颖任务定义 + 严谨评估协议 + 学术诚实度
- **3 个关键问题**: (1) base-model-only 限制实际 significance；(2) DDR 阈值缺 principled 依据 + drifting 特征高共线性使 3/1/3 叙事有误导性；(3) 下游 n=3 underpowered
- **升至 3.5 的路径**: 补充 DDR drifting boundary 敏感性分析、调整 drifting 特征叙事为 single latent factor、补充 concrete deployment scenario、Discussion 下游结论降格为 preliminary evidence

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 163

## Round 163

2 recorded events


### User

_source line 1793 · 2026-05-19T04:22:32.255893+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：与 R1 在大方向上一致（Overall 3.0 Findings），但有两个关键分歧：

1. **[REBUT] R1-W2**：R1 声称 cross-reference F1 从 0.694 降至 ~0.613（8pp 降幅），经核查这是数据引用错误——0.614 来自 Appendix H 的 perturbation experiment，实际 cross-reference spread 仅 0.013，支持论文的 claim。

2. **Excitement 分歧**：R1 给 3.5/5，我给 2.5/5。我认为 R1 低估了 base-model-only 限制的严重性——这是论文最大的 significance 障碍，但 R1 未将其列为独立 weakness。

其余 Must-Fix（N1 下游 n=3、N2 DDR 阈值）和 Should-Fix（W1 特征冗余、W3 independent-seed 覆盖不足、W4 同家族泄漏）均 [AGREE]。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 的核心分歧在三点：(1) base model scope 的严重程度（我认为 Major 而非 Critical）；(2) F1=0.694 的评价需要考虑 LOGO 评估的严格性，R2 用了不可比的 QLoRA 数字；(3) 下游 n=3 实验 R2 标 Minor 但我认为应是 Critical。在 DDR 贡献偏薄、Contribution #3 定位不当、overall 3.0 Findings 这三点上双方一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1794 · 2026-05-19T04:22:51.264880+00:00_

审稿流程已完成。Round 24 审稿报告已投递至 Research Director。

**最终评分**: 3.0 (Findings)

**核心结论**:
- 任务定义新颖 + 实验严谨 + 学术诚实 → 达到 Findings 门槛
- Base-model-only 限制 + DDR 贡献偏 empirical + 部分统计基础不够稳固 → 不够 Conference

**需修复的关键问题** (3 Critical, 4 Major, 5 Minor):
1. 补充 base-model deployment scenario 论证
2. DDR drifting boundary 完整敏感性分析
3. 下游实验结论措辞降格为 preliminary evidence
4. 调整三个 drifting 特征叙事（承认是单一 latent factor）
5. Contribution #3 reframe 为 boundary conditions
6. Independent-seed 控制扩展至更多家族
7. Abstract 精简数字、Table 1 增加 LOFO 行、Related Work 补充 ordinal classification

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 164

## Round 164

64 recorded events


### User

_source line 1795 · 2026-05-19T04:36:13.543466+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-19T04:36:21.361537+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-19T04:36:21.412630+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-19T04:36:24.925489+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-19T04:36:24.925853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-19T04:36:30.145731+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-19T04:36:30.648157+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (56 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 提交前最终检查（OpenReview form, AI disclosure）\n\n## 温度扩展实验结果（全部完成，已写入论文）\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\n|-------|------|-----------|--------|-------------|\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\n\n## 其他近期结论\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\n\n## 论文状态\n全部编辑完成，编译 0 errors，27 页。\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\n- appendix_tost.tex（8×7 per-generator TOST table）\n- appendix_classifier.tex OLMo 版本脚
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-19T04:36:31.100569+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-19T04:36:32.557355+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml\", \"content\": \"# Literature Map for gen-depth-fingerprint\\n# 递归 LLM 生成链深度指纹识别\\n# Updated: 2026-05-15\\n# Categories: detection, model-collapse, data-quality, stylometry,\\n#             iterative-generation, watermarking, vocabulary-diversity,\\n#             membership-inference, ood-detection, survey\\n# Total: 39 papers\\n\\n##############################################################################\\n# 1. Perplexity-based / Zero-shot Detection\\n##############################################################################\\n\\n- id: detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Mitchell et al.\\\"\\n  year: 2023\\n  venue: \\\"ICML 2023\\\"\\n  arxiv: \\\"2301.11305\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\\\"\\n  key_finding: \\\"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\\\"\\n\\n- id: gltr\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: \\\"Gehrmann et al.\\\"\\n  year: 2019\\n  venue: \\\"ACL 2019\\\"\\n  arxiv: \\\"1906.04043\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\\\"\\n  key_finding: \\\"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\\\"\\n\\n- id: dna_gpt\\n  title: \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\"\\n  authors: \\\"Yang et al.\\\"\\n  year: 2024\\n  venue: \\\"ICLR 2024\\\"\\n  arxiv: \\\"2305.17359\\\"\\n  category: detection\\n  role: background\\n  relevance: \\\"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\\\"\\n  key_finding: \\\"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\\\"\\n\\n- id: binoculars\\n  tit
…[truncated 11985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-19T04:36:32.557896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-19T04:36:33.060131+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{lineno}
12	\usepackage{placeins}
13	\usepackage{multirow}
14	\linenumbers
15	
16	\graphicspath{{../chart/}}
17	
18	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base LLM Text Chains}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{results}
31	
32	\input{discussion}
33	\input{conclusion}
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\appendix
40	
41	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
42	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
43	
44	\input{appendix_dataset_stats}
45	\FloatBarrier
46	
47	\section{Length Confound Analysis}
48	\label{app:length}
49	\input{appendix_length}
50	\FloatBarrier
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	\FloatBarrier
56	
57	\section{Finer-Grained Depth Classification}
58	\label{app:finer-depth}
59	\input{appendix_finer_depth}
60	\FloatBarrier
61	
62	\section{End-to-End Depth Classification (QLoRA)}
63	\label{app:qlora}
64	\input{appendix_qlora}
65	\FloatBarrier
66	
67	\section{Leave-One-Feature-Out Analysis}
68	\label{app:lofo}
69	\input{appendix_lofo}
70	\FloatBarrier
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	\FloatBarrier
76	
77	\section{Classifier Sensitivity}
78	\label{app:classifier}
79	\input{appendix_classifier}
80	\FloatBarrier
81	
82	\section{Robustness to Text Pert
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-19T04:36:33.562867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-19T04:36:33.966244+00:00_

total 3832
drwxr-xr-x  8 ubuntu ubuntu    4096 May 19 04:31 .
drwxr-xr-x 11 ubuntu ubuntu    4096 May 18 15:11 ..
drwxr-xr-x  2 ubuntu ubuntu    4096 May 19 04:05 _pdf_images
drwxr-xr-x  2 ubuntu ubuntu    4096 May 17 12:26 _pdf_images_r8
drwxr-xr-x  2 ubuntu ubuntu    4096 May 17 13:24 _pdf_images_r9
drwxr-xr-x  2 ubuntu ubuntu    4096 May 17 13:28 _pdf_images_r9b
-rw-r--r--  1 ubuntu ubuntu    1163 May 19 04:29 abstract.tex
-rw-r--r--  1 ubuntu ubuntu   11615 May 15 04:58 acl.sty
-rw-r--r--  1 ubuntu ubuntu   45186 May 15 04:58 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu     530 May 17 19:24 appendix_ablation.tex
-rw-r--r--  1 ubuntu ubuntu    5473 May 19 02:29 appendix_classifier.tex
-rw-r--r--  1 ubuntu ubuntu    1987 May 19 02:29 appendix_confusion_matrix.tex
-rw-r--r--  1 ubuntu ubuntu     848 May 17 15:55 appendix_cross_model_detail.tex
-rw-r--r--  1 ubuntu ubuntu    2592 May 19 02:29 appendix_cross_temp.tex
-rw-r--r--  1 ubuntu ubuntu    2285 May 17 15:56 appendix_dataset_stats.tex
-rw-r--r--  1 ubuntu ubuntu    9213 May 19 04:31 appendix_ddr_validation.tex
-rw-r--r--  1 ubuntu ubuntu    3459 May 19 00:53 appendix_domain.tex
-rw-r--r--  1 ubuntu ubuntu    5253 May 19 00:53 appendix_downstream.tex
-rw-r--r--  1 ubuntu ubuntu    3055 May 18 10:46 appendix_error_analysis.tex
-rw-r--r--  1 ubuntu ubuntu    1794 May 19 03:49 appendix_feature_correlation.tex
-rw-r--r--  1 ubuntu ubuntu    1905 May 19 02:29 appendix_feature_distributions.tex
-rw-r--r--  1 ubuntu ubuntu    3748 May 18 10:46 appendix_finer_depth.tex
-rw-r--r--  1 ubuntu ubuntu    1275 May 19 00:58 appendix_generator_subsets.tex
-rw-r--r--  1 ubuntu ubuntu    6578 May 18 10:46 appendix_human_edit.tex
-rw-r--r--  1 ubuntu ubuntu    2036 May 19 01:01 appendix_instruct.tex
-rw-r--r--  1 ubuntu ubuntu    2329 May 17 19:58 appendix_length.tex
-rw-r--r--  1 ubuntu ubuntu    1584 May 17 19:58 appendix_lofo.tex
-rw-r--r--  1 ubuntu ubuntu    1088 May 18 10:45 appendix_prompt_type.tex
-rw-r--r--  1 ubuntu ubunt
…[truncated 2455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-19T04:36:34.067498+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1809 · 2026-05-19T04:36:34.119201+00:00_

# Round 24 Review Issues — Updated after R24 text fixes applied
# Last updated: 2026-05-19 (post R24 action matrix execution)

# ============ CRITICAL (Must-Fix) ============

- id: "R1-N2"
  summary: "仅限 base model 的限制对论文 significance 造成根本性约束"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 24
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R2首提，R1完全同意"}
    - {round: 22, reviewers: "R1,R2", note: "严重性取决于 framing; 科学发现定位使其降为 design scope"}
    - {round: 23, reviewers: "R1,R2", note: "两位 Reviewer 再次一致标记 critical。论文多处措辞暗示超出 base-model 范围的一般性。"}
    - {round: 24, reviewers: "R1,R2", note: "R2 标 Critical（instruct model 上 OLMo F1=0.338，web text 几乎全部来自 instruct models），R1 降为 Major（foundational study 合理范围界定）。Director 判定 Major-Critical。"}
  action_items:
    - {round: 21, action: "Abstract + Contribution 均加 scope limitation", assigned_to: "Director", status: "done"}
    - {round: 22, action: "No additional change needed — resolved by C2 framing adjustment to scientific characterization", assigned_to: "Director", status: "done"}
    - {round: 23, action: "Abstract 重写前置 base-model scope；Intro L5 'how language models' → 'how base language models'；Intro L5 移除 provenance 引用；Intro L8 移除 provenance 定义", assigned_to: "Director", status: "done"}
    - {round: 24, action: "Intro L14 添加 base-model scientific value 句：isolating generation mechanism from instruction-tuning effects provides controlled setting", assigned_to: "Director", status: "done"}
  resolution: ""
  resolution_round: null

- id: "R24-N1"
  summary: "DDR tri-partition 阈值 (d=0.75/0.10) 缺乏 principled 依据，drifting boundary 未做敏感性分析"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 24
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R1首提异方差下 Cohen's d 问题"}
    - {round: 22, reviewers: "R1,R2", note: "补充 Glass's Δ + Cliff's δ"}
    - {round: 23, reviewers: "R1(warning),R2(rebut)", note: "R1 仍标记
…[truncated 15093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-19T04:36:58.874259+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 1811 · 2026-05-19T04:36:58.924765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1812 · 2026-05-19T04:37:02.683652+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1813 · 2026-05-19T04:37:05.595009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1814 · 2026-05-19T04:37:05.595529+00:00_

1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	Text generated by large language models (LLMs) increasingly re-enters the web and seeds subsequent generation, producing recursive chains that progressively diverge from human-written text.
4	We study this phenomenon in base (pretrained) models and ask whether the drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Across eight base models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): features partition into drifting ($d{=}0.76$--$1.17$), intermediate, and near-stationary ($d < 0.10$) groups, consistent with recursive generation shifting the NLL location while distributional shape remains stable.
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, generalizing across model families.
7	The depth signal degrades substantially under instruction tuning, restricting current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1815 · 2026-05-19T04:37:05.796784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1816 · 2026-05-19T04:37:05.797292+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	Characterizing the structure of this evolution is fundamental to understanding how base language models transform distributions under iterative conditioning, with relevance to understanding model collapse dynamics \cite{curse_of_recursion, self_consuming_mad}.
6	Yet binary detection decisions \cite{fast_detectgpt,binoculars,ld_score,detectgpt} obscure this structure: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and term this \emph{depth profiling}.
9	No existing method provides a feature-level decomposition of depth signal in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR) with a three-way partition: when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, three \emph{drifting} features (reference-model mean entropy, type-token ratio, hapax ratio) shift monotonically (Cohen's $d > 0.75$), one \emph{intermediate} feature (entropy std) shows a non-monotonic level shift ($d{=}0.55$), and three \emph{near-stationary} features (entropy max, tail decay, entropy min) exhibit negligible depth effects ($d < 0.10$).
12	This is consistent with recursive generation shifting the NLL location while distributional shape remains stable under fixed sampling parameters.
13	While distributional drift under recursive generation is documented in the model collapse literature \cite{curse_of_rec
…[truncated 2043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1817 · 2026-05-19T04:37:05.917897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1818 · 2026-05-19T04:37:05.919755+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source te
…[truncated 8112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1819 · 2026-05-19T04:37:06.246058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1820 · 2026-05-19T04:37:06.296736+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.764 under 5-fold CV.\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation. Sample-level CV is used because each chain contains multiple generators, making generator-level held-out splits inapplicable.}
14	Leave-one-family-out (LOFO) evaluation yields binary F1\,=\,0.686, confirming cross-family transfer.
15	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference model (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}).
16	Preliminary cross-domain evaluation suggests the signal persists with variation, though a domain$\times$temperature interaction exists (Appendix~\ref{app:domain}).
17	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 ($+$11.6\,pp; Appendix~\ref{app:qlora}), confirming that
…[truncated 11674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1821 · 2026-05-19T04:37:10.913492+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here are the key EMNLP 2026 ARR submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, 
…[truncated 1752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 8229
}
```

</details>

---


### Tool call

_source line 1822 · 2026-05-19T04:37:17.239169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1823 · 2026-05-19T04:37:17.591388+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) is consistent with a location/shape decomposition: under fixed temperature $\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration, while iterative conditioning shifts the input distribution's location as text becomes increasingly predictable to the reference model.
5	This interpretation is post-hoc and empirical; formal analysis of softmax output distribution dynamics under recursive conditioning remains an open problem.
6	DDR is an empirical decomposition capturing this dichotomy, not a claimed universal law of recursive generation.
7	DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.
8	Temperature and prompt-type ablations (\S\ref{sec:results-differential}) support this as a tendency rather than a guarantee: all four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp), and the signal varies across prompt types.
9	
10	Instruction tuning substantially weakens the signal across all three tested families (OLMo, Qwen, Llama; Appendix~\ref{app:instruct}).
11	Within-model 3-class F1 drops 3.7--19.9\,pp (OLMo: 0.575 vs.\ 0.754; Qwen: 0.732 vs.\ 0.769; Llama: 0.544 vs.\ 0.742), while binary F1 changes remain small ($\Delta \leq 3.2$\,pp), indicating that instruction tuning primarily disrupts the gen-0/gen-1 boundary.
12	Under cross-generator evaluation, the degradation is larger (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base).
13	Entropy-mean $\rho$ reverses sign consistently ($+0.48$ for OLMo and Qwen, $+0.23$ for Llama; all base models ${\approx}{-}0.6$), and 6 of 7 features reverse direction for OLMo and Qwen, 3 of 7 for Llama, consistent with instruction tuning shifting the generation attractor rather than destroying
…[truncated 1878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-19T04:37:17.591783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-19T04:37:18.696389+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and identified a differential depth response (DDR) tri-partition across eight base-model generators from five families.
5	A 7-feature ensemble exploiting this tri-partition achieves leak-free binary F1\,=\,0.694 (LOGO) and 0.764 (cross-model chains).
6	Current applicability is restricted to base models; instruction tuning and larger scales remain open.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-19T04:37:20.051419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-19T04:37:20.051876+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers that combine handcrafted features with neural architectures \cite{ghostbuster,feat_aug_transformer,abburi_multifaceted,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{tang2024science}, \citet{wu_survey_2025}, and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent work moves beyond binary detection along several axes.
11	\citet{beyond_binary} classify text into four roles (human-only, LLM-polished, LLM-expanded, LLM-only) via involvement measurement, discriminating production \emph{modes} rather than recursive depth.
12	\citet{two_birds} jointly detect machine-generated text and attribute it to specific LLMs, and \citet{beyond_final_actor} distinguish dual creator-editor roles across four production modes.
13	Multi-generator attribution, including generator-level classification in SemEval 2024 Task 8 Subtask B \cite{semeval2024_task8} and the DeFactify dataset \cite{defactify_dataset}, discriminates among different \emph{sources}.
14	All these approaches classify text by its production process or authorship, while our depth classification tracks how many recursive generation steps a text has undergone, an orthogonal axis.
15	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each capture
…[truncated 5302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1828 · 2026-05-19T04:37:20.252798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1829 · 2026-05-19T04:37:20.253198+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth profiling to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) and closed-source models remain untested; the consistent scale trend (Mistral-7B binary F1\,=\,0.633, lowest among all generators) suggests depth signal may weaken further at frontier scales, potentially approaching the detection floor.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type binary F1\,=\,0.781) compared to elaboration (0.730) and rewriting (0.737), with within-prompt-type paraphrastic chains showing weaker signal (binary F1\,=\,0.671 vs.\ 0.749 for within-prompt-type continuation).
16	DDR is most reliably detecte
…[truncated 3131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-19T04:37:20.303634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-19T04:37:20.304087+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1832 · 2026-05-19T04:37:20.354801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limits long short paper guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limits long short paper guidelines"
  }
}
```

</details>

---


### Tool result

_source line 1833 · 2026-05-19T04:37:27.386863+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limits long short paper guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, here's the information about ACL Rolling Review 2026 submission format, page limits, and guidelines:

## Page Limits

Long papers may have up to eight (8) pages of content plus unlimited pages for references, while short papers may have up to four (4) pages of content, plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page (up
…[truncated 1372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7032
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-19T04:37:43.652451+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-19T04:37:47.467919+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-19T04:37:47.971784+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available, trying alternative\" && python3 -c \"\nimport PyPDF2\nreader = PyPDF2.PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf')\nprint(f'Pages: {len(reader.pages)}')\n\" 2>/dev/null || echo \"Cannot determine page count programmatically\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available, trying alternative\" && python3 -c \"\nimport PyPDF2\nreader = PyPDF2.PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf')\nprint(f'Pages: {len(reader.pages)}')\n\" 2>/dev/null || echo \"Cannot determine page count programmatically\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-19T04:37:48.373507+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 04:32:01 2026 UTC
ModDate:         Tue May 19 04:32:01 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           29
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       2836455 bytes
Optimized:       no
PDF version:     1.7

Cannot determine page count programmatically
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_director_fec00603

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-19T04:37:48.524411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-19T04:37:49.177028+00:00_

100	\FloatBarrier
101	
102	\section{Downstream Utility}
103	\label{app:downstream}
104	\input{appendix_downstream}
105	\FloatBarrier
106	
107	\section{Cross-Model Chain Per-Class Detail}
108	\label{app:cross-model-detail}
109	\input{appendix_cross_model_detail}
110	\FloatBarrier
111	
112	\section{Feature Distribution Analysis}
113	\label{app:feature-distributions}
114	\input{appendix_feature_distributions}
115	\FloatBarrier
116	
117	\section{Cross-Temperature Transfer}
118	\label{app:cross-temp}
119	\input{appendix_cross_temp}
120	\FloatBarrier
121	
122	\section{Feature Ablation}
123	\label{app:ablation-table}
124	\input{appendix_ablation}
125	
126	\begin{figure}[h]
127	\centering
128	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
129	\caption{LOGO binary F1 (gen-1 vs.\ gen-2+, 8-gen pooled) with inference cost. Ensembles achieve marginally higher F1 at 2.4$\times$ inference time and 3.2$\times$ GPU memory; individual detectors vary widely when repurposed for depth.}
130	\label{fig:baseline-ci}
131	\end{figure}
132	\FloatBarrier
133	
134	\input{appendix_feature_correlation}
135	\FloatBarrier
136	
137	\section{Cross-Family Reference Models}
138	\label{app:cross-ref}
139	\input{table4}
140	\FloatBarrier
141	
142	\input{appendix_seed_control}
143	\FloatBarrier
144	
145	\input{appendix_tost}
146	\FloatBarrier
147	
148	\section{DDR Partition Validation}
149	\label{app:ddr-validation}
150	\input{appendix_ddr_validation}
151	\FloatBarrier
152	
153	\section{Generator Subset Summary}
154	\label{app:gen-subsets-section}
155	\input{appendix_generator_subsets}
156	\FloatBarrier
157	
158	\input{appendix_qualitative_examples}
159	
160	\end{document}
161	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-19T04:37:49.327987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-19T04:37:50.583792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-19T04:37:55.803909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1843 · 2026-05-19T04:37:56.513364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-19T04:37:56.717755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1845 · 2026-05-19T04:37:57.672393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1846 · 2026-05-19T04:37:58.430224+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 2626
}
```

</details>

---


### Tool result

_source line 1847 · 2026-05-19T04:38:00.138895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 3625
}
```

</details>

---


### Tool result

_source line 1848 · 2026-05-19T04:38:00.643809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 3926
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-19T04:38:00.795228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 3122
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-19T04:38:07.210273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1851 · 2026-05-19T04:38:08.464967+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1254
}
```

</details>

---


### Tool call

_source line 1852 · 2026-05-19T04:38:28.245871+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"No external_review config found\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"No external_review config found\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1853 · 2026-05-19T04:38:28.296567+00:00_

No external_review config found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1854 · 2026-05-19T04:39:00.598797+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **目标 venue**: EMNLP 2026（via ARR May cycle, deadline 2026-05-25）\n- **格式要求**: Long paper ≤8 页正文 + unlimited references。ACL template, double-blind, [review] 选项, 行号开启。Limitations/Ethics 不计页数。附录允许但审稿人不必审阅。Responsible NLP Checklist 必须。\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **总页数**: 29 页（正文 8 页 + Limitations/Ethics 2 页 + References 3 页 + Appendix 16 页）\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **DDR tri-partition 的统计基础**\n   - Cohen's d 阈值 (0.75/0.10) 的选择是否有 principled 依据\n   - 异方差条件下 pooled Cohen's d 的使用是否合理\n   - Glass's Δ / Cliff's δ 补充分析是否充分\n   - TOST 等价性检验的使用和解释\n   - 3/1/3 partition 的稳健性（holdout validation, threshold sensitivity）\n\n2. **评估协议**\n   - LOGO / LOFO 设计是否合理\n   - Gen-0 seed sharing 对评估的影响及其处理（binary F1 排除 gen-0）\n   - Independent-seed 控制实验的覆盖范围\n   - Length confound 控制\n   - Bootstrap CI 和统计检验的正确性\n\n3. **Baseline 比较**\n   - 将 detection scores 作为 depth predictors 的公平性\n   - 与 QLoRA end-to-end 方法的定位\n   - 推理成本比较的合理性\n\n4. **特征工程**\n   - 7 个特征的选择动机\n   - PCA 92.3% 单维度解释 vs 保留 3 个 drifting 特征的合理性\n   - TTR-hapax 强相关 (r=0.97) 下同时保留的正当性\n   - Reference model (Pythia-410M) 选择的潜在偏差\n\n5. **实验覆盖度**\n   - 8 个 generators 的代表性（0.6B-8B，5 families）\n   - 温度消融实验覆盖范围\n   - Cross-domain 实验的充分性\n   - Instruct model 实验的结论\n\n### 报告格式\n请按以下结构输出：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n- **Questions**（需作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Detailed Comments**（逐节意见）\n\n严格客观，不留情面。像 EMNLP 最严格的审稿人一样评估。",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **目标 venue**: EMNLP 2026（via ARR May cycle, deadline 2026-05-25）\n- **格式要求**: Long paper ≤8 页正文 + unlimited references。ACL template, double-blind, [review] 选项, 行号开启。Limitations/Ethics 不计页数。附录允许但审稿人不必审阅。Responsible NLP Checklist 必须。\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **总页数**: 29 页（正文 8 页 + Limitations/Ethics 2 页 + References 3 页 + Appendix 16 页）\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点审查以下方面：\n\n1. **DDR tri-partition 的统计基础**\n   - Cohen's d 阈值 (0.75/0.10) 的选择是否有 principled 依据\n   - 异方差条件下 pooled Cohen's d 的使用是否合理\n   - Glass's Δ / Cliff's δ 补充分析是否充分\n   - TOST 等价性检验的使用和解释\n   - 3/1/3 partition 的稳健性（holdout validation, threshold sensitivity）\n\n2. **评估协议**\n   - LOGO / LOFO 设计是否合理\n   - Gen-0 seed sharing 对评估的影响及其处理（binary F1 排除 gen-0）\n   - Independent-seed 控制实验的覆盖范围\n   - Length confound 控制\n   - Bootstrap CI 和统计检验的正确性\n\n3. **Baseline 比较**\n   - 将 detection scores 作为 depth predictors 的公平性\n   - 与 QLoRA end-to-end 方法的定位\n   - 推理成本比较的合理性\n\n4. **特征工程**\n   - 7 个特征的选择动机\n   - PCA 92.3% 单维度解释 vs 保留 3 个 drifting 特征的合理性\n   - TTR-hapax 强相关 (r=0.97) 下同时保留的正当性\n   - Reference model (Pythia-410M) 选择的潜在偏差\n\n5. **实验覆盖度**\n   - 8 个 generators 的代表性（0.6B-8B，5 families）\n   - 温度消融实验覆盖范围\n   - Cross-domain 实验的充分性\n   - Instruct model 实验的结论\n\n### 报告格式\n请按以下结构输出：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n- **Questions**（需作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Detailed Comments**（逐节意见）\n\n严格客观，不留情面。像 EMNLP 最严格的审稿人一样评估。",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1855 · 2026-05-19T04:39:18.382660+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17783
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-19T04:39:18.583947+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **目标 venue**: EMNLP 2026（via ARR May cycle, deadline 2026-05-25）\n- **格式要求**: Long paper ≤8 页正文 + unlimited references。ACL template, double-blind, [review] 选项, 行号开启。Limitations/Ethics 不计页数。附录允许但审稿人不必审阅。Responsible NLP Checklist 必须。\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **总页数**: 29 页（正文 8 页 + Limitations/Ethics 2 页 + References 3 页 + Appendix 16 页）\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请重点审查以下方面：\n\n1. **新颖性与贡献充分性**\n   - Generation depth classification 作为任务的新颖性\n   - DDR 作为 EMNLP 核心贡献是否足够（是否仅是 feature sensitivity analysis 的系统化表述）\n   - 与并行工作的区分度（broken_telephone, markovian_chains）\n   - 三条 Contribution 的质量和分量\n   - 整体是否达到 EMNLP Main / Findings 水平\n\n2. **Related Work 覆盖**\n   - 是否遗漏重要相关工作\n   - 与 concurrent work 的对比是否充分\n   - Ordinal classification 文献引用\n   - 引用密度是否达到顶会标准\n\n3. **写作质量（重点检查 AI 痕迹）**\n   - **破折号检查**: em-dash (—) 和解释性 en-dash (–) 必须全部清零（数字范围除外）\n   - **-ing 短语结尾**: \"..., highlighting/demonstrating/indicating...\" 等典型 AI 标志\n   - **过度分段**: 是否每 2-3 句就换段\n   - **过渡词堆叠**: Furthermore/Moreover/Additionally 连续使用\n   - **用词黑名单**: delve into, leverage, utilize, facilitate, a myriad of, in the realm of 等\n   - **代词指代模糊**: this, that, it 是否指代清晰\n   - 专有名词首次出现是否有定义\n\n4. **叙事连贯性**\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 主线是否统一\n   - Introduction 的问题定义与实验结论是否一致\n   - Contribution 列表与正文内容的对应关系\n   - Appendix 内容在正文中是否有引用且融入叙事\n\n5. **格式合规性**\n   - 正文是否 ≤8 页\n   - 匿名化是否完整\n   - 行号是否开启\n   - 表格/图片格式是否规范（字体 ≥7pt，caption 自包含）\n   - ACL template 使用是否正确\n\n### 报告格式\n请按以下结构输出：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n- **Questions**（需作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Detailed Comments**（逐节意见）\n\n严格客观，不留情面。像 EMNLP 最严格的审稿人一样评估。特别注意 AI 写作痕迹——这是论文最容易被审稿人识别的问题。",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **目标 venue**: EMNLP 2026（via ARR May cycle, deadline 2026-05-25）\n- **格式要求**: Long paper ≤8 页正文 + unlimited references。ACL template, double-blind, [review] 选项, 行号开启。Limitations/Ethics 不计页数。附录允许但审稿人不必审阅。Responsible NLP Checklist 必须。\n- **论文路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **总页数**: 29 页（正文 8 页 + Limitations/Ethics 2 页 + References 3 页 + Appendix 16 页）\n\n### 你的审查侧重：新颖性 + 完整性 + 写作质量\n\n请重点审查以下方面：\n\n1. **新颖性与贡献充分性**\n   - Generation depth classification 作为任务的新颖性\n   - DDR 作为 EMNLP 核心贡献是否足够（是否仅是 feature sensitivity analysis 的系统化表述）\n   - 与并行工作的区分度（broken_telephone, markovian_chains）\n   - 三条 Contribution 的质量和分量\n   - 整体是否达到 EMNLP Main / Findings 水平\n\n2. **Related Work 覆盖**\n   - 是否遗漏重要相关工作\n   - 与 concurrent work 的对比是否充分\n   - Ordinal classification 文献引用\n   - 引用密度是否达到顶会标准\n\n3. **写作质量（重点检查 AI 痕迹）**\n   - **破折号检查**: em-dash (—) 和解释性 en-dash (–) 必须全部清零（数字范围除外）\n   - **-ing 短语结尾**: \"..., highlighting/demonstrating/indicating...\" 等典型 AI 标志\n   - **过度分段**: 是否每 2-3 句就换段\n   - **过渡词堆叠**: Furthermore/Moreover/Additionally 连续使用\n   - **用词黑名单**: delve into, leverage, utilize, facilitate, a myriad of, in the realm of 等\n   - **代词指代模糊**: this, that, it 是否指代清晰\n   - 专有名词首次出现是否有定义\n\n4. **叙事连贯性**\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 主线是否统一\n   - Introduction 的问题定义与实验结论是否一致\n   - Contribution 列表与正文内容的对应关系\n   - Appendix 内容在正文中是否有引用且融入叙事\n\n5. **格式合规性**\n   - 正文是否 ≤8 页\n   - 匿名化是否完整\n   - 行号是否开启\n   - 表格/图片格式是否规范（字体 ≥7pt，caption 自包含）\n   - ACL template 使用是否正确\n\n### 报告格式\n请按以下结构输出：\n- **Summary**（2-3 句）\n- **Strengths**（逐条）\n- **Weaknesses**（逐条，标注 severity: Critical / Major / Minor）\n- **Questions**（需作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Detailed Comments**（逐节意见）\n\n严格客观，不留情面。像 EMNLP 最严格的审稿人一样评估。特别注意 AI 写作痕迹——这是论文最容易被审稿人识别的问题。",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1857 · 2026-05-19T04:39:20.097649+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1513
}
```

</details>

---


### Assistant

_source line 1858 · 2026-05-19T04:39:25.296832+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性 + 实验设计）— 已触发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）— 已触发

等待两位 Reviewer 独立初审结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 165

## Round 165

2 recorded events


### User

_source line 1859 · 2026-05-19T04:48:18.258732+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 实验方法论扎实、confound 控制细致的实证研究，但核心贡献 DDR 本质上是已知特征在递归生成下的行为分类，新颖性不足以支撑 Main Conference；限于 base model 的实用性严重制约了 impact。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论审慎（LOGO/LOFO/seed 控制/length confound），但 generator subset 不一致、downstream 实验 underpowered (n=3) |
| Excitement | 2.5/5 | 任务定义有意义但 DDR 发现不令人惊讶；base model 限制 + F1=0.694 + 下游无用途 = 实际 impact 很低 |
| Reproducibility | 4/5 | 超参数完整，statistical testing 规范，承诺开源但 review 阶段无匿名链接 |
| Datasets | 3/5 | 37K 文本、8 generators，有一定规模，但限于 English Wikipedia + base models |
| Confidence | 4/5 | 熟悉该领域，仔细阅读了全文和附录 |

---

## Summary

本文提出 generation depth classification（gen-0/gen-1/gen-2+），将二元检测扩展到深度分类任务。核心发现是 differential depth response (DDR)：7 个特征分为 drifting (3)、intermediate (1)、near-stationary (3) 三组。使用 XGBoost 在 8 个 base model generators 上的 LOGO 评估中达到 binary F1=0.694。信号在 instruction tuning 下严重退化。

---

## Strengths

**S1. 任务定义清晰，填补了 binary detection 与 depth 之间的空白。**
将 "real vs. synthetic" 扩展到 gen-0/gen-1/gen-2+ 的三分类是一个自然且有价值的方向。与 source attribution（识别哪个模型）和 production mode（人机协作模式）形成正交维度。Related Work §2.1 对这些正交关系的讨论清楚到位。

**S2. 实验设计的 confound 控制非常审慎。**
Seed-sharing 问题被主动识别并通过 binary F1（排除 gen-0）+ 独立 seed 实验（F1=0.680, Appendix Q）双重控制。Length confound 通过 matched subsampling 控制（F1=0.724 vs 0.770 unmatched, Appendix B）。Seed-level demeaning (F1=0.701) 进一步排除了 topic leakage。这种对自身 limitations 的预判水平高于多数投稿。

**S3. DDR 分析的统计支撑充分。**
Cohen's d、Glass's Δ、Cliff's δ 三重 effect size 指标，TOST equivalence testing 逐 generator 验证 near-stationary 分类，$k$-means 聚类验证 partition 的数据驱动性（silhouette=0.632），holdout generator split 验证稳定性。这是该领域少见的统计严谨程度。

**S4. 对自身方法局限的透明度。**
Discussion 和 Limitations 对 base model 限制、temperature sensitivity、downstream 无效等问题的讨论诚实而非辩护性质。"DDR is an empirical decomposition, not a claimed universal law" (§5 L6) 这种措辞恰当。

**S5. 写作质量总体良好，AI 痕迹已基本清除。**
无 em-dash（仅 LaTeX 注释中存在），无解释性 en-dash，无 Furthermore/Moreover/Additionally 堆叠，无黑名单用词（delve/leverage/utilize/facilitate 等）。段落长度自然。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DDR 的新颖性作为 EMNLP 核心贡献不够充分
- 具体位置：§4.2 Differential Depth Response; Introduction Contribution #2
- 问题：DDR 本质上是一个 feature sensitivity analysis 的系统化表述。"有些特征随递归深度漂移，有些不变"这一发现在 model collapse 文献（Shumailov et al., 2024; Dohmatob et al., 2025）的背景下是预期之中的——递归生成压缩 vocabulary diversity（TTR/hapax 下降）和 shift NLL 分布是已知现象。DDR 的"命名"（drifting/intermediate/near-stationary）和 3/1/3 partition 增加了术语但未带来概念突破。
- 进一步说，三个 drifting features 共享 92.3% variance（§4.2 PCA），TTR 与 hapax ratio 相关性 r=0.97（Method §3.3），实质上 drifting dimension 是一维的。所谓 "7-feature ensemble" 实际上是一个 ~4 维系统（1 drifting PC + entropy_std + 3 个贡献微弱的 near-stationary features）。
- 为什么影响接收：EMNLP 审稿人会问 "what's the conceptual insight beyond organized feature engineering?"。如果 DDR 仅仅是说 location 特征变、shape 特征不变，这可以用一段话概括而非作为核心贡献。
- 建议修改方向：(a) 提供 DDR 的理论解释（为什么 softmax 在递归条件下 location shift 但 shape 稳定？）而非仅 post-hoc 经验观察；(b) 或者将重心从 DDR 移到 depth classification 的实用性上，但这需要解决 base model 限制。

**N2** [critical] Base model 限制严重削弱了实际 impact
- 具体位置：Discussion §5 L10-14; Limitations L6-9
- 问题：论文明确承认 instruction tuning 导致信号严重退化（OLMo-Instruct LOGO F1=0.338 vs 0.763 base）。然而 web 上绝大多数 LLM 生成文本来自 instruction-tuned/RLHF-aligned models。这意味着 depth profiling 在其最明显的应用场景（web 数据质量控制）中几乎不适用。
- Downstream 实验（Appendix L）进一步表明，即使在 base model 设定下，depth-aware curation 与 random subsampling 在训练效果上统计等价（TOST p=1.1×10⁻⁴），"知道深度没有用"。
- 为什么影响接收：一个既不适用于 real-world 数据（instruction-tuned models）又不改善 downstream task 的方法，其研究价值需要更强的理论支撑来弥补。
- 建议修改方向：(a) 增加 instruction-tuned model 的 depth classification 方法（即使 preliminary）；(b) 或者在 Introduction 中更明确地定位为 "understanding base model generation dynamics" 的理论贡献，降低实用性承诺。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Generator subset 不一致性
- 具体位置：Method §3.4 L1-3; Appendix Q footnote; 正文各表注
- 问题：实验使用三个不同的 generator subset（5-gen for cross-model, 6-gen for appendix analyses, 8-gen for main LOGO），跨表比较时读者必须不断查看 footnote 确认用的是哪个子集。例如 QLoRA 实验用 6-gen（Appendix E footnote: "XGBoost 3-class F1=0.789"），但 main paper 报告的 3-class F1 是 0.762（8-gen）。Temperature ablation 中 Pythia-2.8B 和 Qwen3-1.7B 用 6-gen LOGO，而 OLMo 和 Qwen3-0.6B 用 8-gen LOGO（Appendix G footnote †）。
- 建议：在 Appendix 统一用 8-gen 重跑关键分析；或在 Appendix S（Generator Subset Summary）增加 cross-subset 结果对比表。

**W2** [major] 遗漏重要相关工作
- 具体位置：§2.2 Model Collapse and Iterative Generation
- 问题：(a) "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" (ACL 2025, Varshini et al.) 直接分析了连续 paraphrasing 中的 attractor dynamics，与本文的 "attractor" 叙事高度相关但未被引用。(b) 论文中多次使用 "generation attractor" 概念（Discussion §5 L13; Introduction Contribution #3; Appendix J L28），但未引用该领域的基础动力学分析工作。
- 建议：引用该工作并与 broken_telephone 和 markovian_chains 一起讨论。

**W3** [major] Downstream 实验统计 power 不足
- 具体位置：Appendix L (Downstream Utility)
- 问题：n=3 seeds 是严重不足的。论文自己也承认 "the conclusion generalizes over only three random seeds"（Appendix L 最后一句），Cohen's d 被极小的 pooled std 人为放大到 86.0-119.7 这样无意义的值。这个实验要么不做，要么用 ≥10 seeds 做到有说服力。当前状态下，"depth-aware curation is equivalent to random" 这个结论是 underpowered 的 null result，但 Discussion 中却以此为基础展开叙事（"depth profiling identifies structure rather than prescribing data-selection actions"）。
- 建议：增加 seeds 数量或在正文中更明确地弱化该结论的权重。

**W4** [warning] 引用验证问题
- 具体位置：references.bib
- 问题：OpenAlex 验证显示 9 条 bib entries 未找到（包括 DetectGPT, Pythia, XGBoost 等知名工作），5 条 mismatch。虽然未找到可能是 OpenAlex 收录延迟，但需要人工核查确认所有条目（尤其 author names, venue names, years）准确无误。markovian_chains 标注为 arXiv 2026 preprint，应确认是否已被接收到 peer-reviewed venue。
- 建议：逐条人工核查 14 条问题 bib entries。

**W5** [warning] 三条 Contribution 的分量不均
- 具体位置：Introduction L18-23
- 问题：Contribution 1（task formulation + dataset）和 Contribution 3（boundary conditions mapping）更像是实验设计和消融分析的正常组成部分，而非独立贡献。Contribution 2（DDR）是唯一的实质性发现，但如 N1 所述新颖性有限。三条 contribution 合在一起给人"一个观察被拆成三条来凑分量"的印象。
- 建议：将 Contribution 合并为两条，一条聚焦 task + DDR finding，一条聚焦 cross-generator evaluation 和 boundary conditions。

---

## 小问题（不影响接收）

- **M1** [minor] ", confirming" participial phrase 在全文出现 9+ 次（§3.4 method.tex:72, results.tex:14/17/20/46/84, appendix_feature_correlation.tex:25/27, appendix_ddr_validation.tex:135 等）。这是 AI 写作的轻微标志——真人论文中会用 "which confirms" 或独立句子，不会如此高频地用 ", confirming ..." 结尾。同样 ", enabling" 出现 4 次。
- **M2** [minor] Abstract 中 "LLMs" 首次出现时已展开（L3: "large language models (LLMs)"），合规。但 "DDR" 在 Abstract 中定义（L5: "differential depth response (DDR)"）仍显得术语过密——Abstract 读者尚不知 DDR 是什么概念就看到了缩写定义和 Cohen's d 数值。
- **M3** [minor] Figure 1（strip plot）的标题文字较多但信息密度可接受。不过 per-generator 的彩色点在灰度打印下可能难以区分——建议增加 marker shape 区分。
- **M4** [minor] Table 2 caption 中 "slightly higher than per-generator macro average in Table 1" 的差异原因未解释。Pooled vs per-generator macro 平均的区别应在正文或 footnote 中给出一句解释。
- **M5** [minor] Ethics Statement 中 "All code, data, and trained models will be released upon publication"——review 阶段应提供匿名链接以供 reproducibility 检验。
- **M6** [minor] Responsible NLP Research Checklist 需通过 OpenReview 表单提交，论文中无需嵌入，但建议确认已准备完成。

---

## Questions（需作者澄清）

**Q1.** DDR 的 location/shape decomposition 是否有理论解释？Discussion §5 承认这是 "post-hoc and empirical"。softmax 输出分布在递归条件下为何 shape 不变？是否存在与 temperature 作为 shape 控制参数相关的数学约束？

**Q2.** 为什么不直接将 PC1 score 替换三个 drifting features？论文说 "individual features are retained because they enable the DDR decomposition"（§4.2 L85），但如果 DDR 的解释性价值是唯一保留理由，为什么分类系统中不使用 PC1 来简化？这暗示 DDR 的 decomposition 价值可能被高估了。

**Q3.** Instruction-tuned models 的 entropy mean ρ 反号（-0.60→+0.48）是否意味着 depth signal 仍然存在但方向反转？如果是，为什么不训练一个 instruction-tuned 版本的 classifier？

**Q4.** Cross-model chains（多个 generator 混合）的 binary F1=0.764 高于 single-generator LOGO F1=0.694——这是否意味着 generator heterogeneity 反而增加了 depth signal？这一反直觉结果需要解释。

**Q5.** 论文正文提到 Appendix \ref{app:sampling-sensitivity} 处理 temperature 消融，但该部分实际嵌在 appendix_classifier.tex（§G Classifier Sensitivity）的子节中。这是有意设计还是编排遗漏？

---

## Missing References

1. **Varshini et al., "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" (ACL 2025)** — 直接分析连续 paraphrasing 中的 attractor 周期，与本文的 "generation attractor" 概念直接相关。
2. **"How to Synthesize Text Data without Model Collapse?" (2024)** — 关于如何避免递归生成导致的质量退化，与本文的 data provenance 叙事相关。
3. **VaryBalance / variation-based detection framework (2026)** — 最新的 LLM 检测方法，可能值得在 baseline 讨论中提及。

---

## Detailed Comments（逐节）

### Abstract
- 篇幅适当（~120 words），四个必答问题都有回答。
- "restricting current applicability to base models" 放在 Abstract 最后一句是好的选择，诚实设定期望。
- Cohen's $d$ 数值（$d=0.76$--$1.17$）在 Abstract 中对非专业读者意义不大，考虑用 "large effect sizes" 这样的定性描述替代。

### Introduction
- 叙事线清晰：递归生成→二元检测不够→depth classification→DDR→贡献。
- "No existing method provides a feature-level decomposition of depth signal in non-paraphrastic continuation chains"（L9）这个 claim 较强，需要确认 broken_telephone 和 markovian_chains 确实没有做 feature-level decomposition。
- Contribution #3 过于技术化（temperature ranges, ρ 数值），适合 Results 而非 Introduction。

### Related Work
- 覆盖面广：AI detection、model collapse、stylometry、data provenance 四个方向均有涉及。
- 对 concurrent work（broken_telephone, markovian_chains）的定位合理，三重区分（paraphrastic vs continuation, feature decomposition, convergence mechanism）清晰。
- 但缺少 "Unveiling Attractor Cycles" (ACL 2025) 这个直接相关工作（见 Missing References）。
- 引用密度 70 条，对 EMNLP Long Paper 偏少但可接受。

### Method
- 设计清晰。task formulation、generation chain construction、feature extraction、evaluation protocol 结构合理。
- "entropy" as shorthand for NLL（§3.3 L42）是合理的 convention acknowledgment，但可能让 information-theory 背景的审稿人困惑。
- Feature selection 是 a priori（§3.3 L61），这是合理的决策但也意味着可能遗漏了更有用的特征（syntactic complexity 等），Limitations 中已承认。

### Results
- 数据呈现密集但有组织。binary F1 作为 primary metric（排除 gen-0 leak）的设计是 key methodological contribution。
- Feature complementarity 分析（§4.2 L79-87）清楚展示了 drifting vs near-stationary 的协作。
- Cross-reference experiment（spread ≤0.013）有效排除了 reference model bias。

### Discussion
- "post-hoc and empirical" 的自我定位恰当。
- Instruction tuning 的讨论充分但缺少对策。

### Conclusion
- 过于简短（3 句话），未 highlight future work 方向。

### 叙事连贯性
- Abstract → Introduction → Method → Results → Discussion → Conclusion 主线统一。
- 正文的 framing 在 "empirical contribution" 和 "practical tool" 之间有些模糊：Introduction 暗示实用性（"data provenance signal"），但 downstream 实验和 instruction tuning 限制实质上否定了实用价值。
- 所有 Appendix 内容在正文中都有交叉引用，融入叙事。

### 格式合规性
- ✅ 正文 8 页（p1-p8，Conclusion 在 p8 底部结束）
- ✅ 匿名化完整（"Anonymous ACL submission"）
- ✅ 行号开启
- ✅ ACL template + [review] option
- ✅ Limitations 和 Ethics Statement 存在
- ✅ 表格字体可读，caption 基本自包含
- ⚠️ Responsible NLP Checklist 需通过 OpenReview 提交，确认已准备
- ⚠️ 无匿名代码/数据链接

---

**总结**: 一篇实验方法论扎实的实证论文，DDR tri-partition 是一个有组织的观察但新颖性有限。Base model 限制和 downstream 无效严重制约了 impact。建议作为 Findings 考虑（Overall 3.0），前提是 N1 和 N2 中的 framing 问题得到修正。如果能提供 DDR 的理论解释或 instruction-tuned 模型的初步方案，可考虑提升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1860 · 2026-05-19T04:48:24.862778+00:00_

Reviewer 2 报告已收到（Overall 3.0 Findings）。等待 Reviewer 1 报告完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 166

## Round 166

2 recorded events


### User

_source line 1861 · 2026-05-19T04:48:32.951997+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**: Overall 3.0 (Findings)。

主要问题：
1. **DDR 新颖性不足** — 本质是已知特征（NLL/TTR/hapax）在递归生成下的行为分类，三个 drifting features 共享 92.3% variance，"7-feature ensemble" 实际是 ~4 维系统
2. **Base model 限制严重** — instruction-tuned models 下信号崩溃（F1: 0.763→0.338），web 文本主要来自 instruction-tuned models
3. **Downstream 无用途** — depth-aware curation 与 random subsampling 统计等价（n=3 seeds, underpowered）

优势在于实验设计严谨（LOGO/LOFO/seed 控制/length confound）、写作 AI 痕迹已基本清除、对自身 limitations 的透明度高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1862 · 2026-05-19T04:48:39.310769+00:00_

Reviewer 2 报告已收到（Overall 3.0 Findings）。等待 Reviewer 1 完成初审后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 167

## Round 167

6 recorded events


### User

_source line 1863 · 2026-05-19T04:50:52.582748+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains

## 总体评分

**Overall**: 3.0 / 5 — Findings（可被 Findings 接收）
**一句话总结**: 问题定义新颖、实验设计周密，但 DDR 分区的统计基础存在方法论缺陷，且实际应用场景薄弱，贡献更偏分析性质而非方法创新。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有充分实验支撑，LOGO/LOFO/length-control 设计合理；但 Cohen's d 阈值缺少 principled 推导，异方差下使用 pooled d 有方法论瑕疵，TOST 等价性检验对部分 near-stationary 特征失败 |
| Excitement | 2.5/5 | 问题形式化（depth classification beyond binary）有新意，DDR 分解框架有分析价值；但研究局限于 base models <8B，实际下游应用（Section M）效果微弱，instruct model 退化严重但未深入分析 |
| Reproducibility | 4/5 | 代码和数据承诺公开，实验配置（seed、temperature、prompt）描述详尽，bootstrap CI 报告规范 |
| Confidence | 4/5 | 仔细阅读全文含 29 页附录，对统计方法和实验设计有充分了解 |

---

## Summary

本文提出"generation depth classification"任务，将 LLM 递归生成链的文本按深度分为 gen-0/gen-1/gen-2+，超越传统的 human-vs-machine 二分类。作者在 8 个 base model（0.6B-8B, 5 families）上构建 37,058 个文本的数据集，识别出 differential depth response (DDR) 将 7 个手工特征三分为 drifting/intermediate/near-stationary 三组，并用 XGBoost 集成分类器在 LOGO 评估下达到 leak-free binary F1=0.694。实验设计周密，包含长度控制、独立 seed 验证、cross-domain 和 temperature 消融。但核心 DDR 分区的统计基础（Cohen's d 阈值选择、异方差处理）存在方法论问题，且实际应用场景未充分建立。

---

## Strengths

**S1. 问题形式化有价值。** 将递归生成深度分类（gen-0/gen-1/gen-2+）作为独立任务首次系统性提出，与 model collapse 文献形成互补但不重叠的研究视角。这对理解 LLM 生成链的分布漂移机制有基础科学价值。

**S2. 实验设计严谨。** LOGO（leave-one-generator-out）和 LOFO（leave-one-feature-out）协议设计合理，leak-free 评估意识强。Binary F1 排除 gen-0 以消除 seed sharing 偏差（§3.4），独立 seed 控制实验（Appendix T）确认仅 ~1.4pp 差距，length confound 三重控制（Appendix B）均属高于平均水准的实验规范。

**S3. DDR 分解的分析洞察有趣。** 将特征按效应量系统分为 drifting（location shift）、intermediate、near-stationary（shape stability）三类，并发现 92.3% 方差可被单一主成分解释——这是对递归生成分布漂移的有用刻画。PCA 结果和 per-feature depth trend（Figure 5, Appendix O）给出直观且可验证的 evidence。

**S4. 统计检验覆盖面广。** 论文使用 bootstrap CI (n=1000)、McNemar test、Bonferroni 校正、Levene test、KS test、TOST 等价性检验、Glass's Δ 和 Cliff's δ 等多种统计工具，比该领域大多数论文更为严格。

**S5. 对 detection baseline 的定位诚实。** §4.3 明确将 baseline 比较定位为"contextualize depth discrimination ability rather than claim competitive advantage"，而非过度宣传性能优势。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导**
- 具体位置：Section 4.2, Appendix V
- 问题：DDR tri-partition 是论文的核心分析框架，但分区阈值 |d|>0.75（drifting）和 |d|<0.10（near-stationary）是 empirically chosen，未给出原则性依据。Cohen (1988) 的标准基准是 0.2/0.5/0.8（small/medium/large），论文偏离这些标准却未解释为什么。若阈值改为 0.5/0.15，partition 是否会改变？Appendix V 的 k-means 验证（Table 25）在 k=3 时 entropy_min 从 near-stationary 分离出来，说明分区并非天然稳定。
- 为什么影响接收：DDR tri-partition 是全文核心 claim 之一（Contribution 2），如果阈值选择是 ad hoc 的，则分区的 generality 存疑，下游所有基于分区的 discussion（§4.2, §5）都缺乏根基。
- 建议：(a) 给出阈值选择的 formal criterion（如 ROC-based optimal split、bootstrap stability at varying thresholds）；(b) 报告阈值在合理范围内（如 0.5-1.0 / 0.05-0.20）的分区稳定性图；(c) 或明确承认这是 data-driven choice 并弱化"tri-partition"的理论化表述。

**N2** [critical] **TOST 等价性检验对 "near-stationary" 特征部分失败**
- 具体位置：Appendix U, Table 26
- 问题：Tail decay 在 TOST 检验（ε=0.05 equivalence bound）下仅 4/8 generators 通过等价性，entropy max 仅 6/8 通过。这意味着对一半（或近一半）的 generators，这些特征并不满足 near-stationary 的统计标准，但论文仍将其归入 near-stationary 组。Table 26 在 ε=0.15 时 tail decay 仍仅 6/8 通过。
- 为什么影响接收：如果 near-stationary 分类不可靠，DDR tri-partition 的可信度降低。论文对此的讨论不充分——仅在附录中报告数字，主文中（§4.2）直接使用分区结论。
- 建议：(a) 主文中 acknowledge TOST 部分失败的事实及其含义；(b) 讨论 tail decay 是否应归入 intermediate 而非 near-stationary；(c) 报告移除 tail decay 后分类器性能变化。

**N3** [critical] **异方差条件下使用 pooled Cohen's d 作为主要分区指标**
- 具体位置：Section 4.2 (line ~587), Appendix V (Table 28)
- 问题：Levene tests 明确拒绝等方差假设（方差比 1.86-2.21, p.28），在此条件下 pooled Cohen's d 会系统性偏估效应量。论文虽在 Appendix V 补充了 Glass's Δ 和 Cliff's δ，但主文中的 DDR 分区完全基于 pooled d。Table 28 显示 Glass's Δ amplifies drifting effects（entropy mean 1.054 vs pooled d 约 0.75+），说明 pooled d 低估了真实效应量。
- 为什么影响接收：分析框架的基础指标在已知违反假设的条件下使用，削弱了分区的 statistical rigor。
- 建议：(a) 将 Glass's Δ 或 Cliff's δ 作为主要分区指标，或至少在主文中 jointly report；(b) 重新审视在 Δ/δ 下分区边界是否变化。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **TTR-hapax 近完美相关 (r=0.97) 下同时保留**
- 具体位置：Section 3.3, Appendix R (Table 21)
- 问题：TTR 和 hapax ratio 的 Spearman 相关达 0.97（Table 21），本质上测量同一信号。同时保留两者存在两个问题：(a) 人为膨胀特征集规模（7→实际独立维度 ~5-6）；(b) LOFO 评估（Table 7）中两者互相补偿——drop TTR 时 hapax 接管，反之亦然——导致两者的 individual importance 被系统低估。论文的 justification（"both contribute to LOFO importance"）恰好是这种补偿效应的结果。
- 建议：(a) 报告同时 drop TTR+hapax 的联合消融；(b) 讨论是否应合并为一个 lexical diversity 复合指标。

**W2** [major] **PCA 92.3% 单维解释与保留三特征的分析矛盾**
- 具体位置：Section 4.2, Appendix R
- 问题：论文发现 drifting 特征子集 PCA 的 PC1 解释 92.3% 方差，据此 claim"a single principal component explains 92.3% of their joint variance"，暗示三个 drifting 特征本质上是同一信号。但分类器仍保留全部三个特征。论文的 justification 是"Individual features are retained because they enable the DDR decomposition"（§4.2），但如果三者是同一 latent 的不同表征，DDR 分解本身就不需要区分它们。
- 建议：明确讨论"一个 latent 信号的三个 manifestation" vs. "三个独立信号"的 tension，报告用 PC1 代替三个 drifting 特征后的分类器性能。

**W3** [major] **Reference model (Pythia-410M) 选择的潜在 same-family 偏差**
- 具体位置：Section 3.3, Appendix S (Table 22)
- 问题：Pythia-410M 是 generator family 之一（Pythia-1B, Pythia-2.8B）的小模型。Cross-family reference model validation（Table 22）显示 drift direction 一致但 magnitude varies with spread in LOGO F1 of 0.013。虽然 spread 小，但 Table 22 仅测试了 5 个 reference model（3-gen subset），覆盖不足以排除 family bias。尤其是 Pythia generators 在 Table 1 中 binary F1 最高（0.748 for Pythia-2.8B），可能部分归因于 reference model 亲和性。
- 建议：(a) 在 full 8-gen LOGO 下测试至少一个非 Pythia reference model（如 OLMo-2-1B 或 Qwen-sized model）；(b) 报告 per-generator F1 在不同 reference model 下的方差。

**W4** [major] **温度消融使用不同 OLMo checkpoint**
- 具体位置：Appendix H, footnote on p.18
- 问题：温度实验中 OLMo 使用的是 OLMo-2-0425-1B（April 2025 release），而主实验使用的原始 OLMo-2-1B-1B 权重已不再公开可用。这将 model version 效应与 temperature 效应混淆。论文在脚注中提及，但未讨论其影响。
- 建议：(a) 在主文或附录中 explicitly acknowledge 这一 confound；(b) 讨论是否应将 OLMo 温度结果标记为 preliminary。

**W5** [major] **Instruct model 退化未做 mechanistic 分析**
- 具体位置：Section 5, Appendix K (Table 15)
- 问题：Instruct models 的 F1 下降 3.7-19.9pp，但论文仅描述性地报告"instruction tuning primarily disrupts the gen-0/gen-1 boundary"，未分析 WHY（是特征分布变化？DDR 分区失效？还是 RLHF 改变了递归动态？）。这是论文最大的 practical limitation，但分析最薄弱。
- 建议：(a) 报告 instruct model 下各特征的 DDR 效应量变化；(b) 检查 DDR 分区是否在 instruct model 下仍然成立；(c) 如果分区改变，讨论这对 DDR 作为"fundamental property"的 claim 意味着什么。

**W6** [moderate] **Downstream utility 微弱 (Section M / Appendix M)**
- 具体位置：Appendix M, Table 17
- 问题：Downstream utility 实验显示 depth-aware data selection 的 PPL improvement 仅为 2,367 vs 2,389（depth-filtered vs. random subsample），差异极小（~0.9%）。这削弱了 depth profiling 作为实用工具的 motivation。论文 Introduction 中 motivate depth classification 时暗示实际应用价值，但 Section M 的证据不支持这一 framing。
- 建议：(a) 弱化 Introduction 中对实际应用的 framing，更多强调分析贡献；(b) 或提供更有说服力的 downstream task（如 training data curation 对 model quality 的影响）。

**W7** [moderate] **Cross-domain 覆盖不足**
- 具体位置：Appendix J, Table 14
- 问题：Cross-domain 实验仅覆盖 3 个额外 domain（News, Academic, Code），每个仅 200 seeds、3 generators。鉴于论文 claim "depth signal persists across News, Academic, and Code domains"（Appendix J），这一 evidence base 较薄。Domain×temperature interaction 被提及但样本量太小无法充分 characterize。
- 建议：增加至少 1-2 个 domain（如 social media, creative writing），或 acknowledge cross-domain claim 为 preliminary。

---

## 小问题（不影响接收）

- **M1**: Table 1 (per-generator macro F1=0.694) 与 Table 2 (pooled F1=0.706) 的报告差异未在主文中足够显著地标注，可能引起困惑。建议在 §4.1 首次报告 F1 时 clarify 这是 macro-average。
- **M2**: 主文 §1 中 claim "No existing method provides a feature-level decomposition of depth signal in non-paraphrastic continuation chains"（Abstract, line 007），但未在 Related Work 中 formally survey depth-aware detection 的全部 literature 来支撑这一 claim。
- **M3**: Figure 1 的 strip plot 虽然信息密度高，但三个 DDR zone 的颜色编码（绿/黄/红）与 Figure 2 的 violin plot 颜色方案不一致，增加认知负担。
- **M4**: Table 3 的 "Samples" 列显示各 generator 样本量差异较大（4,535 to 6,569），但未讨论样本量差异对 LOGO 评估的潜在影响。
- **M5**: 论文使用 "near-stationary" 一词描述 shape features 的行为，但严格的 stationarity 定义涉及时间序列的均值/方差恒定——这里的"depth"不是传统意义的时间维度，术语选择可能造成误解。

---

## Questions（需作者澄清）

**Q1.** Cohen's d 阈值 0.75 和 0.10 是在 development set 上 tuned 的还是 pre-specified 的？如果是 data-driven，是否存在 circular reasoning（用 data 定义分区，再用分区指导分类）？

**Q2.** LOFO 实验中，drop entropy_mean 导致最大 F1 下降（-3.70pp），但 drop entropy_min 导致 +0.01pp。如果 entropy_min 对分类毫无贡献，为什么不从 DDR 分析中移除它？保留零贡献特征是否仅为了维持 3/1/3 对称性？

**Q3.** Table 22 (cross-family reference model) 仅测试 3-gen subset。在 full 8-gen 设置下，换用 OLMo 或 Qwen 作为 reference model 是否会改变 LOGO F1 的排序？

**Q4.** 论文 claim DDR 是 "a fundamental property of recursive generation independent of decoding conditions"（§5），但 instruct model 退化 3.7-19.9pp。如何调和 "fundamental property" claim 与 instruct model 下的 breakdown？

**Q5.** Depth classification 的 practical ceiling 是什么？假设有一个 oracle 可以完美提取 depth signal，理论上的最优 F1 是多少？Bayes error rate 在当前特征空间下的估计是多少？

**Q6.** 为什么只测试 gen-0 到 gen-4 的链？更深的链（gen-5+）中 DDR 分区是否仍然成立，还是特征会 saturate？

---

## Missing References

1. **Guo et al. (2023), "How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection"** — 直接相关的 multi-class generation detection work。
2. **Tu et al. (2023), "ChatLog: Carefully Recording the Evolution of ChatGPT"** — 研究 LLM 输出随时间的 distributional drift，与 iterative generation 的 drift 分析高度相关。
3. **Xu et al. (2024), "Earth is Flat because...: Investigating LLMs' Belief towards Misinformation via Persuasive Conversation"** — 涉及 LLM 递归对话中的分布变化，与 recursive chain 的 setting 相关。
4. **Ordinal regression literature**: 论文使用 3-class ordinal 问题但未充分引用 ordinal classification 方法学文献（仅在 Appendix 提到 Frank-Hall reduction）。Gutiérrez et al. 的 ordinal survey 虽已引用，但 CORAL (Cao et al., 2020) 仅在 §4.2 一笔带过。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度合适，四个关键问题回答完整
- "leak-free binary F1=0.694" 作为 headline metric 偏低，可能第一印象不够强

### §1 Introduction
- 故事线清晰：model collapse → inference chain → depth classification
- Contribution list 中 "empirical rather than methodological" 的自我定位是诚实的
- 但 Contribution 3（DDR mechanistic boundary conditions）的表述暗示理论贡献，与 "empirical" 定位有些 tension

### §2 Related Work
- 覆盖面合理，positioning 清晰
- §2.3 (Vocabulary Diversity and Stylometry) 与 §2.4 (Data Quality and Provenance) 的分界不够自然

### §3 Method
- Task formulation 清晰
- Generation chain construction 协议详尽
- Feature extraction 的 motivation 充分（reference-model + surface 两路）

### §4 Results
- §4.1 LOGO 结果呈现清楚，bootstrap CI 规范
- §4.2 DDR 分析是全文亮点但也是最大弱点（见 N1-N3）
- §4.3 Baseline 比较的定位（"contextualize rather than claim advantage"）是正确的策略

### §5 Discussion
- "DDR as an empirical decomposition rather than a theoretical decomposition" 的讨论很好
- 但 "DDR is distinct from model collapse"（§5）的论证过于简短——需要更 formal 的对比

### §6 Conclusion
- 简洁准确

### Limitations
- 覆盖面全面，包含 base model 局限、scale 局限、domain 局限
- 建议增加对 DDR 阈值选择局限性的 acknowledgment

### Appendix
- 共 16 页，内容丰富但部分冗余
- Appendix V (DDR Partition Validation) 应在主文中至少 summarize 一段
- Appendix L (Error Analysis) 中 "gen-2+ samples classified as gen-1 are the primary failure point (40.2%)" 是重要信息，应在主文 §4.1 中提及

---

## 总结

本文提出了一个有价值的新任务（generation depth classification）并给出了系统性的实验分析。DDR 三分区框架是有意义的分析贡献。但核心统计基础（Cohen's d 阈值选择、异方差处理、TOST 部分失败）存在不可忽视的方法论问题，特征工程中的冗余（TTR-hapax r=0.97、PCA 92.3%）未得到充分讨论，且实际应用场景薄弱。论文的强处在于实验设计的严谨性和对 limitation 的诚实态度。修复 N1-N3 中的统计基础问题并加强 DDR 分区的 principled justification 后，本文适合 Findings track 接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1864 · 2026-05-19T04:51:28.440364+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应其 Must-Fix (N1-N3)、Should-Fix (W1-W7) 和 Questions (Q1-Q6) 中的每一条：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题：\n\n**N1** [critical] Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导\n- DDR tri-partition 分区阈值 |d|>0.75（drifting）和 |d|<0.10（near-stationary）是 empirically chosen，未给出原则性依据。Cohen (1988) 的标准基准是 0.2/0.5/0.8，论文偏离这些标准却未解释为什么。若阈值改为 0.5/0.15，partition 是否会改变？Appendix V 的 k-means 验证在 k=3 时 entropy_min 从 near-stationary 分离出来，说明分区并非天然稳定。\n\n**N2** [critical] TOST 等价性检验对 \"near-stationary\" 特征部分失败\n- Tail decay 在 TOST 检验下仅 4/8 generators 通过等价性，entropy max 仅 6/8 通过。论文仍将其归入 near-stationary 组。\n\n**N3** [critical] 异方差条件下使用 pooled Cohen's d 作为主要分区指标\n- Levene tests 明确拒绝等方差假设（方差比 1.86-2.21），pooled Cohen's d 会系统性偏估效应量。主文中 DDR 分区完全基于 pooled d。\n\n### Reviewer 1 的 Should-Fix 问题：\n\n**W1** [major] TTR-hapax 近完美相关 (r=0.97) 下同时保留\n**W2** [major] PCA 92.3% 单维解释与保留三特征的分析矛盾\n**W3** [major] Reference model (Pythia-410M) 选择的潜在 same-family 偏差\n**W4** [major] 温度消融使用不同 OLMo checkpoint\n**W5** [major] Instruct model 退化未做 mechanistic 分析\n**W6** [moderate] Downstream utility 微弱\n**W7** [moderate] Cross-domain 覆盖不足\n\n### Reviewer 1 的 Questions：\n\n**Q1.** Cohen's d 阈值 0.75 和 0.10 是在 development set 上 tuned 的还是 pre-specified 的？\n**Q2.** LOFO 实验中 entropy_min 对分类毫无贡献（+0.01pp），为什么不从 DDR 分析中移除它？\n**Q3.** Table 22 (cross-family reference model) 仅测试 3-gen subset。在 full 8-gen 设置下，换用其他 reference model 是否会改变 LOGO F1 排序？\n**Q4.** 论文是否 claim DDR 是 \"fundamental property\"？instruct model 退化如何调和？\n**Q5.** Depth classification 的 practical ceiling（Bayes error rate）？\n**Q6.** 为什么只测试 gen-0 到 gen-4？更深的链中 DDR 是否仍成立？\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别注意你是否在初审中遗漏了 Reviewer 1 发现的问题，或者 Reviewer 1 的某些批评是否过于严格。",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应其 Must-Fix (N1-N3)、Should-Fix (W1-W7) 和 Questions (Q1-Q6) 中的每一条：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题：\n\n**N1** [critical] Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导\n- DDR tri-partition 分区阈值 |d|>0.75（drifting）和 |d|<0.10（near-stationary）是 empirically chosen，未给出原则性依据。Cohen (1988) 的标准基准是 0.2/0.5/0.8，论文偏离这些标准却未解释为什么。若阈值改为 0.5/0.15，partition 是否会改变？Appendix V 的 k-means 验证在 k=3 时 entropy_min 从 near-stationary 分离出来，说明分区并非天然稳定。\n\n**N2** [critical] TOST 等价性检验对 \"near-stationary\" 特征部分失败\n- Tail decay 在 TOST 检验下仅 4/8 generators 通过等价性，entropy max 仅 6/8 通过。论文仍将其归入 near-stationary 组。\n\n**N3** [critical] 异方差条件下使用 pooled Cohen's d 作为主要分区指标\n- Levene tests 明确拒绝等方差假设（方差比 1.86-2.21），pooled Cohen's d 会系统性偏估效应量。主文中 DDR 分区完全基于 pooled d。\n\n### Reviewer 1 的 Should-Fix 问题：\n\n**W1** [major] TTR-hapax 近完美相关 (r=0.97) 下同时保留\n**W2** [major] PCA 92.3% 单维解释与保留三特征的分析矛盾\n**W3** [major] Reference model (Pythia-410M) 选择的潜在 same-family 偏差\n**W4** [major] 温度消融使用不同 OLMo checkpoint\n**W5** [major] Instruct model 退化未做 mechanistic 分析\n**W6** [moderate] Downstream utility 微弱\n**W7** [moderate] Cross-domain 覆盖不足\n\n### Reviewer 1 的 Questions：\n\n**Q1.** Cohen's d 阈值 0.75 和 0.10 是在 development set 上 tuned 的还是 pre-specified 的？\n**Q2.** LOFO 实验中 entropy_min 对分类毫无贡献（+0.01pp），为什么不从 DDR 分析中移除它？\n**Q3.** Table 22 (cross-family reference model) 仅测试 3-gen subset。在 full 8-gen 设置下，换用其他 reference model 是否会改变 LOGO F1 排序？\n**Q4.** 论文是否 claim DDR 是 \"fundamental property\"？instruct model 退化如何调和？\n**Q5.** Depth classification 的 practical ceiling（Bayes error rate）？\n**Q6.** 为什么只测试 gen-0 到 gen-4？更深的链中 DDR 是否仍成立？\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别注意你是否在初审中遗漏了 Reviewer 1 发现的问题，或者 Reviewer 1 的某些批评是否过于严格。",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1865 · 2026-05-19T04:51:51.046773+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22606
}
```

</details>

---


### Tool call

_source line 1866 · 2026-05-19T04:51:51.348217+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应其 Must-Fix (N1-N2)、Should-Fix (W1-W5) 和 Questions (Q1-Q5) 中的每一条：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题：\n\n**N1** [critical] DDR 的新颖性作为 EMNLP 核心贡献不够充分\n- DDR 本质上是 feature sensitivity analysis 的系统化表述。\"有些特征随递归深度漂移，有些不变\"在 model collapse 文献背景下是预期之中的。三个 drifting features 共享 92.3% variance，实质上 drifting dimension 是一维的。\"7-feature ensemble\" 实际是 ~4 维系统。EMNLP 审稿人会问 \"what's the conceptual insight beyond organized feature engineering?\"\n\n**N2** [critical] Base model 限制严重削弱了实际 impact\n- Instruction-tuned models 下信号崩溃（OLMo-Instruct LOGO F1=0.338 vs 0.763 base）。Web 上绝大多数 LLM 生成文本来自 instruction-tuned/RLHF-aligned models。Downstream 实验进一步表明 depth-aware curation 与 random subsampling 统计等价。\n\n### Reviewer 2 的 Should-Fix 问题：\n\n**W1** [major] Generator subset 不一致性（5-gen / 6-gen / 8-gen 混用）\n**W2** [major] 遗漏重要相关工作：Varshini et al., \"Unveiling Attractor Cycles in LLMs\" (ACL 2025)\n**W3** [major] Downstream 实验 n=3 seeds 统计 power 不足\n**W4** [warning] 引用验证问题（9 条 bib entries 未在 OpenAlex 找到，5 条 mismatch）\n**W5** [warning] 三条 Contribution 的分量不均——Contribution 1 和 3 更像实验设计的正常组成部分\n\n### Reviewer 2 的 Minor 问题：\n\n**M1** \", confirming\" participial phrase 在全文出现 9+ 次——AI 写作的轻微标志\n**M2** Abstract 术语过密（DDR 定义 + Cohen's d 数值）\n**M3** Figure 1 灰度打印下可能难以区分\n**M4** Table 2 pooled vs per-generator macro 差异未解释\n**M5** 无匿名代码/数据链接\n\n### Reviewer 2 的 Questions：\n\n**Q1.** DDR 的 location/shape decomposition 是否有理论解释？\n**Q2.** 为什么不直接将 PC1 score 替换三个 drifting features？\n**Q3.** Instruction-tuned models 的 entropy mean ρ 反号是否意味着 depth signal 仍存在但方向反转？\n**Q4.** Cross-model chains binary F1=0.764 高于 single-generator LOGO F1=0.694——generator heterogeneity 反而增加 depth signal？\n**Q5.** Appendix \\ref{app:sampling-sensitivity} 的编排位置是否正确？\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别注意你是否在初审中遗漏了 Reviewer 2 发现的问题，或者 Reviewer 2 的某些批评是否过于严格。",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应其 Must-Fix (N1-N2)、Should-Fix (W1-W5) 和 Questions (Q1-Q5) 中的每一条：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题：\n\n**N1** [critical] DDR 的新颖性作为 EMNLP 核心贡献不够充分\n- DDR 本质上是 feature sensitivity analysis 的系统化表述。\"有些特征随递归深度漂移，有些不变\"在 model collapse 文献背景下是预期之中的。三个 drifting features 共享 92.3% variance，实质上 drifting dimension 是一维的。\"7-feature ensemble\" 实际是 ~4 维系统。EMNLP 审稿人会问 \"what's the conceptual insight beyond organized feature engineering?\"\n\n**N2** [critical] Base model 限制严重削弱了实际 impact\n- Instruction-tuned models 下信号崩溃（OLMo-Instruct LOGO F1=0.338 vs 0.763 base）。Web 上绝大多数 LLM 生成文本来自 instruction-tuned/RLHF-aligned models。Downstream 实验进一步表明 depth-aware curation 与 random subsampling 统计等价。\n\n### Reviewer 2 的 Should-Fix 问题：\n\n**W1** [major] Generator subset 不一致性（5-gen / 6-gen / 8-gen 混用）\n**W2** [major] 遗漏重要相关工作：Varshini et al., \"Unveiling Attractor Cycles in LLMs\" (ACL 2025)\n**W3** [major] Downstream 实验 n=3 seeds 统计 power 不足\n**W4** [warning] 引用验证问题（9 条 bib entries 未在 OpenAlex 找到，5 条 mismatch）\n**W5** [warning] 三条 Contribution 的分量不均——Contribution 1 和 3 更像实验设计的正常组成部分\n\n### Reviewer 2 的 Minor 问题：\n\n**M1** \", confirming\" participial phrase 在全文出现 9+ 次——AI 写作的轻微标志\n**M2** Abstract 术语过密（DDR 定义 + Cohen's d 数值）\n**M3** Figure 1 灰度打印下可能难以区分\n**M4** Table 2 pooled vs per-generator macro 差异未解释\n**M5** 无匿名代码/数据链接\n\n### Reviewer 2 的 Questions：\n\n**Q1.** DDR 的 location/shape decomposition 是否有理论解释？\n**Q2.** 为什么不直接将 PC1 score 替换三个 drifting features？\n**Q3.** Instruction-tuned models 的 entropy mean ρ 反号是否意味着 depth signal 仍存在但方向反转？\n**Q4.** Cross-model chains binary F1=0.764 高于 single-generator LOGO F1=0.694——generator heterogeneity 反而增加 depth signal？\n**Q5.** Appendix \\ref{app:sampling-sensitivity} 的编排位置是否正确？\n\n---\n\n请对以上每一条给出 [AGREE] 或 [REBUT] 回应，并说明理由。特别注意你是否在初审中遗漏了 Reviewer 2 发现的问题，或者 Reviewer 2 的某些批评是否过于严格。",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-19T04:51:52.762760+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1414
}
```

</details>

---


### Assistant

_source line 1868 · 2026-05-19T04:51:56.096717+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 168

## Round 168

2 recorded events


### User

_source line 1869 · 2026-05-19T04:51:58.695047+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：Overall 3.0 / 5（Findings level）**

核心评价：
- **3 个 Critical 问题**：Cohen's d 阈值缺乏 principled 推导（N1）、TOST 等价性检验对 near-stationary 特征部分失败（N2）、异方差下使用 pooled Cohen's d（N3）
- **7 个 Major/Moderate 问题**：TTR-hapax 冗余（W1）、PCA 与特征保留矛盾（W2）、reference model 偏差（W3）、温度消融 checkpoint 混淆（W4）、instruct 退化未分析（W5）、downstream utility 微弱（W6）、cross-domain 覆盖不足（W7）
- **主要优势**：问题形式化有价值（S1）、实验设计严谨（S2）、DDR 分析洞察有趣（S3）、统计检验覆盖广（S4）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1870 · 2026-05-19T04:52:06.926942+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 1871 · 2026-05-19T04:54:51.793796+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 全部意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Cohen's d 阈值缺乏 principled 推导**

同意这是一个合理的质疑，但严格程度需要校准。

论文在 §4.2 中的实际论证逻辑不是"选了 0.75 和 0.10 作为阈值"，而是"hapax ratio（d=0.76）与 entropy std（d=0.55）之间存在一个自然 gap，partition 在 d∈[0.56, 0.75] 范围内稳定"。这个 gap-based 的论证本身是合理的——它依赖的是特征之间 effect size 的自然分离，而非人为划线。

但 R1 的核心问题仍然成立：(1) 0.10 这个 near-stationary 阈值没有类似的 gap 论证；(2) k=3 clustering 时 entropy_min 自成一类（Table 5, Appendix V），说明纯数据驱动下 3/1/3 并非最自然的分区——论文用 binary-task d 来"修正"聚类结果，这是 domain-informed 但也是 post-hoc 的选择。

建议作者：(a) 明确承认阈值是 gap-driven + domain-informed 而非 principled，(b) 报告在不同阈值下 partition 是否影响分类性能（如果 partition 变化但 F1 不变，说明分类不依赖具体分区方案，反而削弱了 DDR 作为核心贡献的必要性）。

---

**[AGREE] R1-N2: TOST 等价性检验部分失败**

同意。Tail decay 仅 4/8 generators 通过 TOST（ε=0.20），entropy max 6/8。论文在 §4.2 L75-76 和 Appendix V Table 6 中已经坦诚报告了这一点，并指出 non-passing generators 的 d=0.15-0.22 仍远低于 drifting 阈值。

但这恰恰暴露了"near-stationary"这个标签的问题：如果 tail decay 在一半 generators 上不通过等价性检验，称其为"near-stationary"是否 misleading？从诚实性角度，论文处理得不错（数据透明），但从 labeling 角度，R1 的批评有道理。

我在初审中未将此列为 Must-Fix，现在认为 R1 的 severity 评估是合理的——它直接影响 DDR 3/1/3 partition 的可信度。不过我认为这更接近 Major 而非 Critical，因为：(1) drifting/non-drifting 的 primary partition（k=2, silhouette=0.632）不受此影响，(2) 即使将 tail decay 重分类为 intermediate（变成 3/2/2），核心叙事不变。

---

**[REBUT] R1-N3: 异方差条件下使用 pooled Cohen's d**

R1 的技术关切是正确的（Levene 拒绝等方差，方差比 1.86-2.21），但论文已经充分回应了这个问题。

Appendix V §Heteroscedasticity Sensitivity（Table 7）明确提供了 Glass's Δ 和 Cliff's δ 作为 robustness check。关键数据：
- Drifting features: Glass's |Δ| = 0.936-1.410, Cliff's |δ| = 0.510-0.587（"large"）
- Near-stationary: Glass's |Δ| ≤ 0.099, Cliff's |δ| ≤ 0.072（"negligible"）
- 最小 drifting-to-最大 near-stationary gap: 9.5× under Glass's Δ

论文 §4.2 L71 也在正文中提到了 Levene test 结果和 Glass's Δ / Cliff's δ 的 supplement。所以 pooled d 不是"唯一的分区指标"——它是三个互相佐证的指标之一。

R1 说"主文中 DDR 分区完全基于 pooled d"——这并不完全准确。正文同时引用了 Spearman ρ（Figure 1）、KS test、CV shift（<3% vs >15%）、以及 heteroscedasticity-robust metrics（§4.2 倒数第二段）。DDR partition 的论证是 convergence of multiple metrics，不是 solely based on pooled d。

建议：将 N3 降级为 Should-Fix。作者可以在正文中更突出 Glass's Δ 的地位（如在 Figure 1 或 Table 中增加一列），而非仅放在 Appendix 中。

---

### Should-Fix 问题

**[AGREE] R1-W1: TTR-hapax 近完美相关下同时保留**

完全同意。我在初审 N1 中已指出"三个 drifting features 共享 92.3% variance，TTR 与 hapax ratio 相关性 r=0.97"，实质上 drifting dimension 是一维的。论文承认 permutation importance 差异 (0.35 vs 0.18) 反映 tree-based feature masking（§4.2 L86, citing Strobl et al. 2008），这是诚实的，但也等于承认保留两个几乎相同的特征的理由是"marginal LOFO gains"——查 LOFO 表（Appendix F Table 8），hapax_ratio 被移除仅损失 0.42pp，TTR 损失 0.55pp，而如果保留 PC1 替代三者只损失 1.1pp（§4.2 L84）。

---

**[AGREE] R1-W2: PCA 92.3% 单维解释与保留三特征的分析矛盾**

同意，与 W1 密切相关。论文的解释是"individual features are retained because they enable the DDR decomposition"（§4.2 L85），但这是循环论证：DDR decomposition 的价值在于展示三个特征分别如何漂移，但 PCA 已经证明它们漂移的方式几乎相同。保留三个特征对分类贡献微弱（1.1pp），对理解贡献也有限（它们做同一件事）。

---

**[AGREE] R1-W3: Reference model same-family 偏差**

同意，但评估为"partially addressed"。

Cross-reference 实验（Table 22, Appendix R）测试了 Pythia-410M、OLMo-2-1B、Qwen3-0.6B 三个 reference model，LOGO F1 spread 仅 0.013。这在方向上是 reassuring。但 R1 正确指出该实验仅在 5-gen subset 上进行。在 8-gen full set 上，Pythia-410M 与 Pythia-2.8B/1B 的 same-family affinity 是否解释了 Pythia generators 获得最高 F1（Table 1: 0.724, 0.718）的现象？论文 §4.1 L15 提到了这一点但用 "partly reflecting same-family affinity" 一笔带过。

8-gen LOGO 下的 cross-reference 验证是必要的补充实验。

---

**[AGREE] R1-W4: 温度消融使用不同 OLMo checkpoint**

同意这是一个方法论瑕疵。Appendix G 脚注 * 说明 "OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights used in the main experiments are no longer publicly available"。虽然这可能是 forced by circumstances（原 weights 不可用），但引入了一个混淆变量：checkpoint 差异 vs temperature 差异。

建议作者在脚注中增加两个 checkpoint 在 t=0.7 下的 baseline 对比，以 bound checkpoint effect。

---

**[AGREE] R1-W5: Instruct model 退化缺乏 mechanistic 分析**

同意。论文给出了 descriptive 观察（entropy mean ρ 反号，6/7 features reverse for OLMo/Qwen, 3/7 for Llama; Table 9），并解释为"instruction tuning shifting the generation attractor"，但这是 metaphor 而非 mechanism。

我在初审 Q3 中提出了相关问题：如果 depth signal 仍存在但方向反转，为什么不训练一个 instruction-tuned 版本的 classifier？论文未讨论这个自然的 follow-up。cross-generator LOGO F1 从 0.763 降到 0.338（OLMo-Instruct）说明信号不仅仅是反转——它在 cross-generator 泛化上崩溃了，这才是真正需要解释的现象。

---

**[AGREE] R1-W6: Downstream utility 微弱**

完全同意。我在初审中已将此列为 N2（critical）和 W3（major）。n=3 seeds 的 downstream 实验（Appendix L）得出"depth-aware curation 与 random 等价"的结论，同时 Cohen's d 被极小的 pooled std 人为膨胀到 86-120，论文自己也承认这些值"unreliable"（Appendix L L70）。

核心问题：这个 underpowered null result 是否应该放在 Discussion 中作为 narrative support？论文在 §5 中写道"depth profiling identifies structure rather than prescribing data-selection actions"，这依赖于一个 n=3 的 null result 来支撑 framing 转向。如果 downstream 实验用 10+ seeds 后发现 depth-aware curation 有微弱但显著的效果，整个 framing 就需要改变。

---

**[AGREE] R1-W7: Cross-domain 覆盖不足**

同意，但 severity 我认为是 minor 而非 moderate。

Appendix I 测试了 News、Academic、Code 三个域，binary F1 在 0.63-0.75 之间。论文明确注明 cross-domain generation 用了 t=1.0（落在 method 可靠范围 t≤0.7 之外），存在 domain × temperature confound。Supplementary t=0.7 实验显示 Academic domain F1 降至 0.628，但这仍然是有信号的（远高于 chance）。

更重要的域是 social media、dialogue、creative writing 等 real-world 高频场景，但这属于 future work 而非审稿阶段的 must-have。

---

### Questions

**[AGREE] R1-Q1: 阈值是否 pre-specified？**

好问题。论文的措辞暗示 post-hoc: "the drifting boundary reflects the natural gap between hapax ratio (d=0.76) and entropy std (d=0.55)" (§4.2)——这是在看到所有 d 值之后描述 gap，而非 pre-specified。作者应明确承认这一点。

但我补充：即使阈值是 post-hoc 的，如果 partition 在 holdout split 上稳定（Table 6 显示两个 4/4 split 下 zone assignment 一致，max Δ|ρ|=0.05），post-hoc 并不等于 overfit。关键不是阈值是否 pre-specified，而是 partition 是否 robust。

---

**[AGREE] R1-Q2: 为什么不移除 entropy_min？**

同意这是一个尖锐的问题。LOFO 表（Appendix F Table 8）显示 entropy_min 的 Δ=+0.01pp，即移除它反而微幅提升。它在 permutation importance 中也几乎为零（0.015）。保留它的唯一理由是 DDR narrative（作为 near-stationary 组的成员），但如果一个特征对分类完全无贡献，它在 DDR decomposition 中的角色也可质疑——它不提供任何信号来支撑"near-stationary features contribute to ensemble"的说法。

但我也注意到，移除 entropy_min 不会改变 DDR partition 的核心结构（从 3/1/3 变成 3/1/2），且论文的主要 claim 是 drifting features 的行为，不是 near-stationary features 的数量。这是一个 cleanliness 问题而非 validity 问题。

---

**[REBUT] R1-Q3: Cross-ref 仅测试 3-gen subset，是否影响 LOGO F1 排序？**

R1 问的是"在 full 8-gen 下换 reference model 是否改变 LOGO F1 排序"。这是合理的追问，但需要注意 Table 22 的结果：三个不同 family 的 reference models（Pythia-410M、OLMo-2-1B、Qwen3-0.6B）在 5-gen LOGO 下 F1 spread 仅 0.013（0.803-0.816），且 drift direction 一致（全部为负）。

虽然 5-gen 不等于 8-gen，但 0.013 的 spread 意味着 reference model 选择对 LOGO F1 的影响不超过 1.3pp——这小于 Table 1 中 Pythia-2.8B (0.724) 和 Mistral-7B (0.633) 之间 9.1pp 的 generator 间差异。因此 reference model 不太可能改变 per-generator 排序。

不过，我同意 8-gen 下的 cross-ref 验证仍然是一个 valuable supplementary experiment。我将 severity 定位为 minor 而非 major。

---

**[REBUT] R1-Q4: 论文是否 claim DDR 是 "fundamental property"？**

论文明确没有做此 claim。关键文本：
- Discussion §5 L6: "DDR is an empirical decomposition capturing this dichotomy, not a claimed universal law of recursive generation"
- Discussion §5 L7: "DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions"
- §4.2 L90: "confirms the depth features are robust to reference model choice, though it does not alone establish DDR as a fundamental property of recursive generation"

这三处措辞明确将 DDR 定位为 empirical + parameter-dependent，而非 fundamental。R1 的提问可能基于对正文某些段落的印象（如 Introduction 中 "the key finding" 的措辞），但论文在 Discussion 中的 qualification 是充分的。

Instruct model 退化与此定位一致：DDR 在 base models + standard decoding 条件下成立，instruction tuning 改变了条件，信号相应改变。这不是 contradiction，而是 boundary condition mapping（Contribution #3）的一部分。

---

**[AGREE] R1-Q5: Practical ceiling (Bayes error rate) 未报告**

同意这是一个有用的补充。当前 binary F1=0.694 是 achievable performance 而非 ceiling。QLoRA end-to-end classifier（3-class F1=0.905, Appendix E）提供了一个 upper bound，但它的 binary F1 未被报告。知道 Bayes error rate 或至少 QLoRA 的 binary F1 可以帮助判断 7-feature ensemble 距离 ceiling 有多远。

---

**[AGREE] R1-Q6: 为什么只测试 gen-0 到 gen-4？**

同意这是合理的追问。论文的答案隐含在 5-class evaluation（Appendix C）中：gen-2/3/4 已经 mutually indistinguishable（F1≈0.50），这意味着 DDR 的 monotonic drift 在 gen-2 之后趋于饱和。更深的链（gen-5, gen-10）可能会进一步验证这个收敛，但从 practical 角度 gen-4 已经足够。

不过，从理论角度，观察 DDR features 在非常深的链中是否完全 converge（即 inter-class KS→0）可以为 "fixed-point attractor" 的叙事提供更强支撑。

---

### 我的初审中遗漏的 R1 发现

1. **N2 (TOST 部分失败)**: 我初审中未将 TOST 问题列为独立条目——我关注了 DDR 新颖性但忽略了分区 robustness 的技术细节。R1 在这一点上比我更细致。
2. **W4 (不同 OLMo checkpoint)**: 我完全遗漏了这个 appendix 脚注。这是一个值得标记的方法论瑕疵。
3. **Q5 (Bayes error rate)**: 好的补充建议，我未提出。

### R1 过于严格的批评

1. **N3 (pooled d + 异方差)**: R1 将此列为 Critical，但论文在 Appendix V 已提供 Glass's Δ 和 Cliff's δ 的三重验证，partition gap 在所有 metrics 下一致（≥9.5×）。正文 §4.2 也有引用。将其降为 Should-Fix 更合理。
2. **Q3 (cross-ref subset)**: 0.013 spread 的 reference model 效应远小于 9.1pp 的 generator 间差异，8-gen 验证有价值但不是 blocking issue。

---

### 综合评估

R1 的技术审查比我更注重统计方法论细节（effect size metrics, TOST equivalence, heteroscedasticity），我的审查更注重 novelty/impact/writing 层面。两个 review 在核心判断上一致：

**共识点**:
- DDR 新颖性有限（我的 N1 ≈ R1 对 DDR "仅是 feature sensitivity analysis" 的隐含质疑）
- TTR/hapax 冗余（我的 N1 + R1 的 W1/W2）
- Downstream 无效（我的 N2 + R1 的 W6）
- Base model 限制严重（我的 N2 + R1 的 W5）

**R1 独特贡献**: 对 DDR 分区的统计方法论审查（N1 thresholds, N2 TOST, N3 heteroscedasticity）是有价值的补充。

**我的独特贡献**: Missing references（Unveiling Attractor Cycles, ACL 2025）、AI 写作痕迹检查（", confirming" 高频使用）、Responsible NLP Checklist 提醒、叙事连贯性分析。

**Overall 维持 3.0 (Findings)**。R1 的技术问题（N2 TOST, W4 checkpoint）加强了我对论文 methodological cleanness 的轻微担忧，但不改变总体评估——主要限制仍在 novelty 和 impact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1872 · 2026-05-19T04:55:00.337716+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 170

## Round 170

2 recorded events


### User

_source line 1873 · 2026-05-19T04:55:11.872950+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

逐条总结：
- **N1 (阈值)**: [AGREE] — gap-based 论证有合理性但确实是 post-hoc 的
- **N2 (TOST 失败)**: [AGREE] — tail decay 4/8 通过率确实动摇 "near-stationary" 标签
- **N3 (异方差+pooled d)**: [REBUT] — 论文已提供 Glass's Δ + Cliff's δ 三重验证，partition 在所有 metrics 下 gap ≥9.5×，R1 评为 Critical 偏严格
- **W1-W7**: 全部 [AGREE]，W4 (不同 OLMo checkpoint) 是我初审遗漏的
- **Q1-Q2, Q5-Q6**: [AGREE]
- **Q3 (cross-ref subset)**: [REBUT] — 0.013 spread 远小于 generator 间差异
- **Q4 (fundamental claim)**: [REBUT] — 论文三处明确否认 DDR 是 universal/fundamental

Overall 维持 3.0 (Findings)。两位 reviewer 在核心判断上一致：DDR 新颖性有限，base model 限制严重，downstream 无用途。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1874 · 2026-05-19T04:55:18.525686+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 171

## Round 171

8 recorded events


### User

_source line 1875 · 2026-05-19T04:56:46.953911+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 问题

**[AGREE] R2-N1: DDR 新颖性作为 EMNLP 核心贡献不够充分**

同意这是一个实质性问题，但程度上与 R2 有所分歧。

R2 指出 DDR 本质上是 "organized feature engineering"，92.3% PCA 单维度说明 drifting dimension 是一维的——这与我在初审 W2 中的发现一致。论文实际上只有 ~4-5 个独立信息维度（3 drifting → 1 PC，1 intermediate，3 near-stationary → 形态大同小异），"7-feature ensemble" 的表述确实夸大了系统复杂度。

但我认为 R2 略微低估了两点：(a) DDR 的价值不仅在于分区本身，而在于**跨 8 个 generator 的一致性**——7/7 特征在所有 generator 上保持同一分区归属（Appendix V, Table 27），这不是 trivially expected 的；(b) model collapse 文献研究的是**训练时**分布退化，而本文研究的是**推理链**的递归漂移，二者的机制不同——前者涉及梯度更新，后者仅涉及自回归采样。§2.2 (line ~168) 明确做了这一区分。

**结论**：对 Main conference 来说 novelty 确实不足，但 DDR 作为分析框架对 Findings 仍有价值。建议作者弱化 DDR 作为 "novel decomposition" 的表述，改为 "systematic empirical characterization"。

---

**[AGREE] R2-N2: Base model 限制严重削弱实际 impact**

完全同意，这也是我初审的 W5 和 W6。

补充 R2 未完全展开的一个关键细节：Appendix M (Table 17) 的 downstream 实验不仅显示 depth-aware curation 与 random subsampling "统计等价"，实际上 **random subsampling 的 PPL (2,367) 优于 depth-stratified selection (2,387) 和 binary-filtered (2,389)**。也就是说 depth-aware data curation 不是"没用"，而是**轻微有害**。虽然差异很小（~0.9%），但方向是反的。这进一步削弱了 Introduction 中对实际应用的暗示。

Instruct model 方面，我补充一个 R2 提出但未充分利用的发现（见 Q3 回应）：Table 15 (p.21) 显示 entropy mean 的 Spearman ρ 在所有三个 instruct model 上**反号**（base: −0.60~−0.64 → instruct: +0.23~+0.49）。这意味着 depth signal 在 instruct model 中并非消失，而是**方向反转**。如果作者能 exploit 这一反转（如 re-train classifier with instruct data），applicability 可能大幅扩展。这是论文应该深入讨论但完全忽略的方向。

---

## Should-Fix 问题

**[AGREE] R2-W1: Generator subset 不一致性**

我初审未专门标注此问题，R2 的发现是正确的。论文中存在至少 4 种 generator subset 配置：
- 主实验：8-gen（Table 1）
- 温度消融：4-gen（Appendix H, Table 10）
- Cross-domain：3-gen（Appendix J）
- Instruct：3 families（Appendix K）
- Cross-model chains：5-gen（Appendix F, footnote）
- DDR validation holdout：4 subsets 各用 4-gen（Appendix V）

每次 subset 变化都可能引入 selection bias，且跨实验比较变得困难。例如，温度消融的 4-gen 结果能否推广到另外 4 个 generator？论文没有讨论。建议作者至少在 Appendix 中提供一个 unified generator table 列出每个实验使用的 generator 组合。

---

**[AGREE] R2-W2: 遗漏 Varshini et al., "Unveiling Attractor Cycles in LLMs" (ACL 2025)**

我初审未发现此遗漏。§2.2 中 Guo et al. (2020) 的 Markovian attractor dynamics 被讨论为直接相关工作（line ~175），但 Varshini et al. (2025) 的 attractor cycles 研究在时间上更近且更直接相关——如果递归生成链存在 attractor cycle 行为，这对 DDR 的 near-stationary 特征（shape features 趋于稳定）有直接的理论解释。这一遗漏可能被审稿人解读为文献调研不完整。

---

**[AGREE] R2-W3: Downstream 实验 n=3 seeds 统计 power 不足**

同意。Table 17 使用 n=3 seeds 的 mean ± std，但 n=3 几乎无法建立统计显著性。PPL 差异仅 ~20 点（~0.9%），在 n=3 下无法排除随机波动。如果 downstream utility 是论文的一个 contribution point，需要 n≥10 seeds 才能得出可靠结论。若无法增加 seed 数量，应将 downstream 结果明确标记为 "preliminary" 并弱化相关 claim。

---

**[REBUT] R2-W4: 引用验证问题（9 not_found + 5 mismatch）**

R2 对引用问题的关注是合理的，但我认为这些 flag **不构成实质问题**。

我在初审中独立运行了 `verify_references`，9 条 not_found 均为学术界公认的高影响力论文：
- `detectgpt` = Mitchell et al. (2023), ICML，引用量 1000+
- `pythia` = Biderman et al. (2023), ICML
- `xgboost` = Chen & Guestrin (2016), KDD，引用量 15000+
- `aaronson_watermark` = Kirchenbauer et al. (2023)
- `reliable_detection` / `detection_possibilities` / `two_birds` / `beyond_final_actor` / `defactify_dataset` 均为近年 NLP 会议论文

这些全部是 OpenAlex API 的覆盖不足，而非虚构引用。5 条 mismatch（cohen1988statistical, qwen3, llama3, self_consuming_mad, gutierrez_ordinal_survey）同样是 database indexing 差异（如 arXiv preprint vs. conference version），不影响引用准确性。

**建议**：不应在审稿报告中将 OpenAlex 工具的 false negative 转化为对论文引用质量的质疑。

---

**[AGREE] R2-W5: 三条 Contribution 分量不均**

同意。从 §1 (p.2) 的 contribution list 看：
- **Contribution 1**（task formulation + dataset）：这是一个 necessary setup，但 task formulation 本身不是 insight
- **Contribution 2**（DDR tri-partition）：这是唯一的分析贡献
- **Contribution 3**（mechanistic boundary conditions）：这是标准的 robustness/ablation analysis

论文将标准实验设计包装成 "contribution" 的做法在 EMNLP 审稿中确实会被质疑。建议作者将 Contribution 1 和 3 合并为一个 "experimental framework" 贡献点，将 Contribution 2 作为主要贡献，并增加一条关于 instruct model 信号反转的发现（如果展开分析的话）。

---

## 小问题

**[AGREE] R2-M1: ", confirming" participial phrases 9+ 次**

我初审遗漏了此问题。这属于 CLAUDE.md 写作规范中明确禁止的 "-ing 短语结尾"（§5.2: "禁止 -ing 短语结尾：如 '..., highlighting the applicability of...' / '..., demonstrating the effectiveness of...'"）。", confirming" 是完全相同的模式。9+ 次出现是明显的 AI 写作标志，必须修复。

**[AGREE] R2-M2: Abstract 术语过密**

Cohen's d 的具体数值（0.75/0.10）不应出现在 Abstract 中。Abstract 应传达 insight（"drifting features vs. shape-stable features"），不需要 effect size 的数值精度。

**[AGREE] R2-M3: Figure 1 灰度可辨性**

ACL 模板要求 "figures should be legible when printed in grayscale." 颜色编码的 DDR zone 区分在灰度下确实可能失效。

**[AGREE] R2-M4: Table 2 pooled vs per-generator**

与我初审 M1 一致。

**[AGREE] R2-M5: 无匿名代码/数据链接**

§9 (Ethics Statement) 承诺 "All code, data, and trained models will be released upon publication"，但 review 阶段缺少 anonymous link（如 anonymous GitHub 或 supplementary zip）降低了 reproducibility 评估能力。

---

## Questions 回应

**[AGREE] R2-Q1: DDR location/shape decomposition 的理论解释**

这是论文最大的 intellectual gap。DDR 的 location shift（entropy mean, TTR, hapax 单调漂移）vs. shape stability（entropy max/min, tail decay 不变）是一个有趣的经验发现，但论文完全没有解释 **为什么** 会出现这种分离。

可能的理论方向：(a) 自回归采样在有限 vocabulary 上的**信息论收缩**——每次递归生成都在上一次的输出分布上采样，location 向高概率区域收缩（entropy 降低），但 extremal behavior（max/min）由长尾 token 的存在性决定，只要 vocabulary 不变就保持稳定；(b) 这可能与 §2.2 中 Guo et al. (2020) 的 Markov attractor 有关——attractor 保持 shape 但收缩 location。但这需要 formal analysis，不是论文当前版本能覆盖的。

建议作者至少在 Discussion (§5) 中提供一个 informal conjecture。

---

**[AGREE] R2-Q2: 为什么不用 PC1 替代三个 drifting features**

与我初审 W2 一致。论文的 justification（"individual features enable the DDR decomposition"）是循环论证：DDR 分解需要三个特征 → 所以保留三个特征 → 三个特征证明 DDR 分解。如果 PC1 替代后 F1 不下降（论文自己报告仅 -1pp，§4.2 / line ~700），那保留三个特征的唯一理由就是 interpretability。但论文没有 formally demonstrate 三个特征各自提供不同的 interpretable insight——它们都指向同一个 "lexical-distributional convergence" 现象。

---

**[AGREE] R2-Q3: Instruct model entropy mean ρ 反号是否意味着 depth signal 方向反转**

这是 R2 最敏锐的观察，也是我初审中遗漏的关键点。

Table 15 (p.21) 和正文 (p.21) 明确显示：entropy mean 的 Spearman ρ 从 base model 的 −0.60~−0.64 反转为 instruct model 的 +0.23~+0.49。6/7 features 在 OLMo 和 Qwen 上反号，3/7 在 Llama 上反号。

这一发现的含义非常重要：
1. **Depth signal 在 instruct model 中存在，但方向相反** → 当前分类器失败不是因为信号消失，而是因为训练时学到的方向与实际方向相反
2. **如果在 instruct data 上重新训练分类器**，F1 可能恢复甚至提升
3. 这意味着 RLHF/instruction tuning 不是 "破坏" depth signal，而是 "反转" 了递归动态——可能是因为 instruct model 被训练为生成更 "diverse/creative" 的文本，所以递归生成时 entropy 不再单调下降而是上升

论文对此几乎没有讨论，仅在 p.21 用一句话带过："consistent with instruction tuning shifting the generation attractor rather than eliminating iterative dynamics (§5)." 这个发现**本身就可以成为一个独立 contribution**——如果展开分析，可以同时解决 N2（applicability）和 W5（contribution 分量）的问题。

---

**[AGREE] R2-Q4: Cross-model chains F1=0.764 > single-generator LOGO F1=0.694**

这是一个重要的不一致性，我初审未充分关注。两个可能的解释：

(a) **Generator heterogeneity 放大 depth signal**：不同 generator 在链的不同深度引入不同的 stylistic bias，使深度间的分布差异人为增大。如果是这样，0.764 中有一部分信号来自 generator identity 而非 pure depth。
(b) **混合 generator 加速分布漂移**：每个 generator 将前一步的输出向自己的 mode 拉动，如果 modes 不完全重合，累积漂移会比单一 generator 更快。这与 DDR 框架一致但意味着 cross-model F1 不可直接与 single-generator LOGO F1 比较。

论文（§4.1, p.5）将 cross-model 结果呈现为 positive evidence（"confirming cross-family transfer"），但没有讨论为什么比 single-generator 高 7pp。这一差距需要 explicit explanation——如果不能排除 generator identity confound，cross-model 结果的 validity 就存疑。

---

**[AGREE] R2-Q5: Appendix sampling-sensitivity 编排位置**

属于 editorial issue，但如果 cross-reference 链接与实际位置不一致会影响审稿人的阅读体验。建议作者检查所有附录的 \ref 标签是否正确。

---

## 与初审的增量总结

R2 的审稿让我注意到三个我初审遗漏或低估的问题：

1. **Instruct model ρ 反号**（Q3）：这是论文中最有潜力的 unrealized finding，如果展开可以同时解决 applicability 和 novelty 问题
2. **Cross-model F1 > single-generator F1 的不一致性**（Q4）：需要排除 generator identity confound
3. **", confirming" AI 写作标志**（M1）：频繁的 -ing participial phrases 是明显的风格问题

R2 的 N1（novelty）和 N2（base model limitation）与我的评估方向一致，但 R2 的严厉程度更高。我认为对 Findings track 来说，这些问题是可接受的——前提是作者能 (a) 弱化 contribution 表述，(b) 展开 instruct model ρ 反号的分析。

**我维持 Overall 3.0 (Findings) 的评分。**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1876 · 2026-05-19T04:57:16.504759+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null | head -20",
  "description": "Read current review issues header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null | head -20",
    "description": "Read current review issues header"
  }
}
```

</details>

---


### Tool result

_source line 1877 · 2026-05-19T04:57:16.656896+00:00_

# Round 24 Review Issues — Updated after R24 text fixes applied
# Last updated: 2026-05-19 (post R24 action matrix execution)

# ============ CRITICAL (Must-Fix) ============

- id: "R1-N2"
  summary: "仅限 base model 的限制对论文 significance 造成根本性约束"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 24
  mentions:
    - {round: 21, reviewers: "R1,R2", note: "R2首提，R1完全同意"}
    - {round: 22, reviewers: "R1,R2", note: "严重性取决于 framing; 科学发现定位使其降为 design scope"}
    - {round: 23, reviewers: "R1,R2", note: "两位 Reviewer 再次一致标记 critical。论文多处措辞暗示超出 base-model 范围的一般性。"}
    - {round: 24, reviewers: "R1,R2", note: "R2 标 Critical（instruct model 上 OLMo F1=0.338，web text 几乎全部来自 instruct models），R1 降为 Major（foundational study 合理范围界定）。Director 判定 Major-Critical。"}
  action_items:
    - {round: 21, action: "Abstract + Contribution 均加 scope limitation", assigned_to: "Director", status: "done"}
    - {round: 22, action: "No additional change needed — resolved by C2 framing adjustment to scientific characterization", assigned_to: "Director", status: "done"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1878 · 2026-05-19T04:59:06.158837+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "# Round 25 Review Issues (Fresh Review)\n# Last updated: 2026-05-19\n# Reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)\n# Consensus: Both 3.0 (Findings)\n\n# ============ CRITICAL (Must-Fix) ============\n\n- id: \"R25-N1\"\n  summary: \"DDR 新颖性不足以支撑 EMNLP Main Conference 核心贡献\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(critical)，R1同意。DDR 本质是 feature sensitivity analysis 的系统化表述。三个 drifting features 共享 92.3% variance (PCA)，7-feature ensemble 实际 ~4 维。R1 补充：跨 8 generator 一致性有价值，但对 Main 不够。共识：Findings 级别。\"}\n  action_items:\n    - {round: 25, action: \"弱化 DDR 为 'systematic empirical characterization' 而非 'novel decomposition'；或提供理论解释（softmax 递归条件下 location shift 但 shape 稳定的机制）\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"Base model 限制严重削弱实际 impact，instruct model 信号崩溃且 ρ 反转未被利用\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(critical)，R1完全同意并补充：downstream 实验 random subsampling PPL (2367) 优于 depth-aware (2387)，depth-aware 轻微有害。R1 交叉回应中强调 instruct model entropy mean ρ 反号（-0.60→+0.48）是 unrealized finding，展开分析可同时解决 applicability 和 novelty。\"}\n  action_items:\n    - {round: 25, action: \"展开 instruct model ρ 反转分析：重新训练 instruct-specific classifier，讨论 RLHF 是否'反转'而非'破坏'depth signal\", assigned_to: \"pending\", status: \"open\"}\n    - {round: 25, action: \"弱化 Introduction 对实际应用的暗示，更明确定位为 base model generation dynamics 的理论贡献\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N3\"\n  summary: \"Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导，3/1/3 partition 是 post-hoc gap-driven\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1首提(critical)，R2同意。Gap-based 论证有合理性（hapax d=0.76 vs entropy_std d=0.55），但0.10 阈值无 gap 论证。k=3 clustering 时 entropy_min 自成一类，说明 3/1/3 非最自然分区。R2补充：若 partition 变化但 F1 不变，反而削弱 DDR 作为核心贡献的必要性。\"}\n  action_items:\n    - {round: 25, action: \"明确承认阈值是 gap-driven + domain-informed 而非 principled；报告不同阈值下 partition 是否影响分类性能；给出阈值稳定性图\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MAJOR (Should-Fix) ============\n\n- id: \"R25-N4\"\n  summary: \"TOST 等价性检验对 near-stationary 特征部分失败（tail decay 4/8, entropy max 6/8）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1首提(critical)，R2同意但降为 Major——primary partition (k=2) 不受影响，即使 tail decay 重分类为 intermediate (3/2/2) 核心叙事不变。共识：Major。\"}\n  action_items:\n    - {round: 25, action: \"正文 acknowledge TOST 部分失败；讨论 tail decay 是否应归入 intermediate；报告移除 tail decay 后分类器性能\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"异方差条件下 pooled Cohen's d 作为主要分区指标，Glass's Δ/Cliff's δ 仅在附录\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1首提(critical)，R2 rebut 成功：论文已提供 Glass's Δ + Cliff's δ 三重验证，gap ≥9.5× 在所有 metrics 下一致。Director 降为 Major。但 Glass's Δ 应在正文中更突出。\"}\n  action_items:\n    - {round: 25, action: \"正文中 jointly report Glass's Δ 或 Cliff's δ（如在 Figure 1 或 Table 中增加列），不仅放在 Appendix\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"TTR-hapax 近完美相关 (r=0.97) + PCA 92.3% 单维解释，保留三个 drifting 特征的理由是循环论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W1+W2 首提(major)，R2 完全同意。PC1 替代仅损失 1.1pp (§4.2)，'individual features enable DDR decomposition' 是循环论证。联合移除 TTR+hapax 的消融未报告。\"}\n  action_items:\n    - {round: 25, action: \"报告同时 drop TTR+hapax 的联合消融；讨论是否应合并为 lexical diversity 复合指标；明确 '一个 latent 的三个 manifestation' vs '三个独立信号' 的 tension\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"Generator subset 不一致（5/6/8-gen 混用），跨实验比较困难\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(major)，R1同意并列出至少 6 种 subset 配置。温度消融 4-gen 能否推广到另外 4 个 generator 未讨论。\"}\n  action_items:\n    - {round: 25, action: \"在 Appendix 中统一提供 generator subset 对照表；关键分析尽量用 8-gen 重跑或提供 cross-subset 对比\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W4\"\n  summary: \"遗漏重要相关工作：Varshini et al. 'Unveiling Attractor Cycles in LLMs' (ACL 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(major)，R1同意。论文多处使用 'generation attractor' 概念但未引用该领域基础动力学分析工作。\"}\n  action_items:\n    - {round: 25, action: \"引用 Varshini et al. (ACL 2025) 并在 §2.2 讨论 attractor cycle 与 DDR near-stationary 的关系\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W5\"\n  summary: \"Downstream 实验 n=3 seeds 严重 underpowered，null result 不应支撑 framing 叙事\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(major)，R1同意。n=3 下 PPL 差 ~0.9%，random 反而略优。Cohen's d 被极小 pooled std 膨胀到 86-120（论文自承 unreliable）。Discussion §5 L16-17 基于此 null result 转向 'structure identification' framing。\"}\n  action_items:\n    - {round: 25, action: \"增加 seeds 至 ≥10 或将 downstream 结果明确标记为 preliminary 并弱化相关 claim\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W6\"\n  summary: \"Instruct model 退化缺乏 mechanistic 分析，ρ 反转是 unrealized contribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W5 首提(major)，R2同意(初审 Q3)。Entropy mean ρ 从 -0.60 反转为 +0.48，6/7 features 反号(OLMo/Qwen)。R1 交叉回应：这可以成为独立 contribution——若展开分析可同时解决 applicability 和 novelty。\"}\n  action_items:\n    - {round: 25, action: \"报告 instruct model 下 DDR 效应量变化；检查 DDR partition 是否在 instruct 下仍成立；讨论 retrain classifier with instruct data 的可行性\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"三条 Contribution 分量不均，C1 和 C3 更像标准实验设计而非独立贡献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(warning)，R1同意。建议合并为两条：一条 task+DDR，一条 evaluation+boundary conditions。或增加 instruct ρ 反转作为新 contribution。\"}\n  action_items:\n    - {round: 25, action: \"重组 Contribution list\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W8\"\n  summary: \"Reference model (Pythia-410M) same-family 偏差，cross-ref 仅在 5-gen subset 验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W3 首提(major)，R2 partially agree（0.013 spread 远小于 9.1pp generator 间差异）。Pythia generators 获最高 F1 (0.724) 可能部分归因于 reference model 亲和性。\"}\n  action_items:\n    - {round: 25, action: \"在 8-gen LOGO 下测试至少一个非 Pythia reference model\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W9\"\n  summary: \"温度消融使用不同 OLMo checkpoint (OLMo-2-0425-1B vs 原始 OLMo-2-1B)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W4 首提(major)，R2同意（初审遗漏）。原 weights 不再公开可用，checkpoint 差异与 temperature 效应混淆。\"}\n  action_items:\n    - {round: 25, action: \"增加两个 checkpoint 在 t=0.7 下的 baseline 对比以 bound checkpoint effect，或标记 OLMo 温度结果为 preliminary\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W10\"\n  summary: \"Cross-model chains F1=0.764 > single-gen LOGO F1=0.694 的反直觉差异未解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2 Q4 首提，R1同意。可能原因：generator heterogeneity 放大 depth signal（含 generator identity confound）或混合 generator 加速分布漂移。论文呈现为 positive evidence 但未排除 confound。\"}\n  action_items:\n    - {round: 25, action: \"讨论 cross-model vs single-gen F1 差异的原因，排除 generator identity confound\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MINOR / INFO ============\n\n- id: \"R25-M1\"\n  summary: \"', confirming' participial phrase 出现 9+ 次，AI 写作标志\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(minor)，R1同意（写作规范 §5.2 明确禁止 -ing 短语结尾）。', enabling' 也出现 4 次。\"}\n  action_items:\n    - {round: 25, action: \"全文替换 ', confirming/enabling/demonstrating...' 为独立句子或 'which confirms/enables'\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Abstract 术语过密（DDR 定义 + Cohen's d 数值对非专业读者意义不大）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提，R1同意。建议用 'large effect sizes' 定性描述替代具体 d 值。\"}\n  action_items:\n    - {round: 25, action: \"Abstract 中移除 Cohen's d 数值，用定性描述替代\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"Figure 1 灰度打印下 per-generator 彩色点难以区分\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提，R1同意。ACL 要求 figures should be legible in grayscale。\"}\n  action_items:\n    - {round: 25, action: \"增加 marker shape 区分或确保灰度可辨\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Table 2 pooled vs per-generator macro F1 差异 (0.706 vs 0.694) 未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 M1 + R2 M4 均提出。\"}\n  action_items:\n    - {round: 25, action: \"在 §4.1 或 Table 2 caption 中解释 pooled vs per-generator macro 的区别\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M5\"\n  summary: \"无匿名代码/数据链接，降低 reproducibility 评估能力\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2 M5 首提，R1同意。Ethics §9 承诺开源但 review 阶段无匿名链接。\"}\n  action_items:\n    - {round: 25, action: \"提供 anonymous GitHub 或 supplementary zip\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M6\"\n  summary: \"Cross-domain 覆盖不足（仅 3 域，每域 200 seeds/3 generators）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W7 首提(moderate)，R2同意但降为 minor。Social media/dialogue/creative writing 未覆盖。\"}\n  action_items:\n    - {round: 25, action: \"增加 1-2 个 domain 或 acknowledge cross-domain claim 为 preliminary\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M7\"\n  summary: \"entropy_min 对分类零贡献 (LOFO Δ=+0.01pp)，保留仅为维持 3/1/3 对称\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 Q2 首提，R2同意。Permutation importance 仅 0.015。cleanliness 问题非 validity 问题。\"}\n  action_items:\n    - {round: 25, action: \"讨论 entropy_min 的零贡献及其对 DDR narrative 的影响\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "# Round 25 Review Issues (Fresh Review)\n# Last updated: 2026-05-19\n# Reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)\n# Consensus: Both 3.0 (Findings)\n\n# ============ CRITICAL (Must-Fix) ============\n\n- id: \"R25-N1\"\n  summary: \"DDR 新颖性不足以支撑 EMNLP Main Conference 核心贡献\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(critical)，R1同意。DDR 本质是 feature sensitivity analysis 的系统化表述。三个 drifting features 共享 92.3% variance (PCA)，7-feature ensemble 实际 ~4 维。R1 补充：跨 8 generator 一致性有价值，但对 Main 不够。共识：Findings 级别。\"}\n  action_items:\n    - {round: 25, action: \"弱化 DDR 为 'systematic empirical characterization' 而非 'novel decomposition'；或提供理论解释（softmax 递归条件下 location shift 但 shape 稳定的机制）\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"Base model 限制严重削弱实际 impact，instruct model 信号崩溃且 ρ 反转未被利用\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(critical)，R1完全同意并补充：downstream 实验 random subsampling PPL (2367) 优于 depth-aware (2387)，depth-aware 轻微有害。R1 交叉回应中强调 instruct model entropy mean ρ 反号（-0.60→+0.48）是 unrealized finding，展开分析可同时解决 applicability 和 novelty。\"}\n  action_items:\n    - {round: 25, action: \"展开 instruct model ρ 反转分析：重新训练 instruct-specific classifier，讨论 RLHF 是否'反转'而非'破坏'depth signal\", assigned_to: \"pending\", status: \"open\"}\n    - {round: 25, action: \"弱化 Introduction 对实际应用的暗示，更明确定位为 base model generation dynamics 的理论贡献\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N3\"\n  summary: \"Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导，3/1/3 partition 是 post-hoc gap-driven\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1首提(critical)，R2同意。Gap-based 论证有合理性（hapax d=0.76 vs entropy_std d=0.55），但0.10 阈值无 gap 论证。k=3 clustering 时 entropy_min 自成一类，说明 3/1/3 非最自然分区。R2补充：若 partition 变化但 F1 不变，反而削弱 DDR 作为核心贡献的必要性。\"}\n  action_items:\n    - {round: 25, action: \"明确承认阈值是 gap-driven + domain-informed 而非 principled；报告不同阈值下 partition 是否影响分类性能；给出阈值稳定性图\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MAJOR (Should-Fix) ============\n\n- id: \"R25-N4\"\n  summary: \"TOST 等价性检验对 near-stationary 特征部分失败（tail decay 4/8, entropy max 6/8）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1首提(critical)，R2同意但降为 Major——primary partition (k=2) 不受影响，即使 tail decay 重分类为 intermediate (3/2/2) 核心叙事不变。共识：Major。\"}\n  action_items:\n    - {round: 25, action: \"正文 acknowledge TOST 部分失败；讨论 tail decay 是否应归入 intermediate；报告移除 tail decay 后分类器性能\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"异方差条件下 pooled Cohen's d 作为主要分区指标，Glass's Δ/Cliff's δ 仅在附录\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1首提(critical)，R2 rebut 成功：论文已提供 Glass's Δ + Cliff's δ 三重验证，gap ≥9.5× 在所有 metrics 下一致。Director 降为 Major。但 Glass's Δ 应在正文中更突出。\"}\n  action_items:\n    - {round: 25, action: \"正文中 jointly report Glass's Δ 或 Cliff's δ（如在 Figure 1 或 Table 中增加列），不仅放在 Appendix\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"TTR-hapax 近完美相关 (r=0.97) + PCA 92.3% 单维解释，保留三个 drifting 特征的理由是循环论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W1+W2 首提(major)，R2 完全同意。PC1 替代仅损失 1.1pp (§4.2)，'individual features enable DDR decomposition' 是循环论证。联合移除 TTR+hapax 的消融未报告。\"}\n  action_items:\n    - {round: 25, action: \"报告同时 drop TTR+hapax 的联合消融；讨论是否应合并为 lexical diversity 复合指标；明确 '一个 latent 的三个 manifestation' vs '三个独立信号' 的 tension\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"Generator subset 不一致（5/6/8-gen 混用），跨实验比较困难\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(major)，R1同意并列出至少 6 种 subset 配置。温度消融 4-gen 能否推广到另外 4 个 generator 未讨论。\"}\n  action_items:\n    - {round: 25, action: \"在 Appendix 中统一提供 generator subset 对照表；关键分析尽量用 8-gen 重跑或提供 cross-subset 对比\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W4\"\n  summary: \"遗漏重要相关工作：Varshini et al. 'Unveiling Attractor Cycles in LLMs' (ACL 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(major)，R1同意。论文多处使用 'generation attractor' 概念但未引用该领域基础动力学分析工作。\"}\n  action_items:\n    - {round: 25, action: \"引用 Varshini et al. (ACL 2025) 并在 §2.2 讨论 attractor cycle 与 DDR near-stationary 的关系\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W5\"\n  summary: \"Downstream 实验 n=3 seeds 严重 underpowered，null result 不应支撑 framing 叙事\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(major)，R1同意。n=3 下 PPL 差 ~0.9%，random 反而略优。Cohen's d 被极小 pooled std 膨胀到 86-120（论文自承 unreliable）。Discussion §5 L16-17 基于此 null result 转向 'structure identification' framing。\"}\n  action_items:\n    - {round: 25, action: \"增加 seeds 至 ≥10 或将 downstream 结果明确标记为 preliminary 并弱化相关 claim\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W6\"\n  summary: \"Instruct model 退化缺乏 mechanistic 分析，ρ 反转是 unrealized contribution\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W5 首提(major)，R2同意(初审 Q3)。Entropy mean ρ 从 -0.60 反转为 +0.48，6/7 features 反号(OLMo/Qwen)。R1 交叉回应：这可以成为独立 contribution——若展开分析可同时解决 applicability 和 novelty。\"}\n  action_items:\n    - {round: 25, action: \"报告 instruct model 下 DDR 效应量变化；检查 DDR partition 是否在 instruct 下仍成立；讨论 retrain classifier with instruct data 的可行性\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W7\"\n  summary: \"三条 Contribution 分量不均，C1 和 C3 更像标准实验设计而非独立贡献\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(warning)，R1同意。建议合并为两条：一条 task+DDR，一条 evaluation+boundary conditions。或增加 instruct ρ 反转作为新 contribution。\"}\n  action_items:\n    - {round: 25, action: \"重组 Contribution list\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W8\"\n  summary: \"Reference model (Pythia-410M) same-family 偏差，cross-ref 仅在 5-gen subset 验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W3 首提(major)，R2 partially agree（0.013 spread 远小于 9.1pp generator 间差异）。Pythia generators 获最高 F1 (0.724) 可能部分归因于 reference model 亲和性。\"}\n  action_items:\n    - {round: 25, action: \"在 8-gen LOGO 下测试至少一个非 Pythia reference model\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W9\"\n  summary: \"温度消融使用不同 OLMo checkpoint (OLMo-2-0425-1B vs 原始 OLMo-2-1B)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W4 首提(major)，R2同意（初审遗漏）。原 weights 不再公开可用，checkpoint 差异与 temperature 效应混淆。\"}\n  action_items:\n    - {round: 25, action: \"增加两个 checkpoint 在 t=0.7 下的 baseline 对比以 bound checkpoint effect，或标记 OLMo 温度结果为 preliminary\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W10\"\n  summary: \"Cross-model chains F1=0.764 > single-gen LOGO F1=0.694 的反直觉差异未解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2 Q4 首提，R1同意。可能原因：generator heterogeneity 放大 depth signal（含 generator identity confound）或混合 generator 加速分布漂移。论文呈现为 positive evidence 但未排除 confound。\"}\n  action_items:\n    - {round: 25, action: \"讨论 cross-model vs single-gen F1 差异的原因，排除 generator identity confound\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============ MINOR / INFO ============\n\n- id: \"R25-M1\"\n  summary: \"', confirming' participial phrase 出现 9+ 次，AI 写作标志\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提(minor)，R1同意（写作规范 §5.2 明确禁止 -ing 短语结尾）。', enabling' 也出现 4 次。\"}\n  action_items:\n    - {round: 25, action: \"全文替换 ', confirming/enabling/demonstrating...' 为独立句子或 'which confirms/enables'\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"Abstract 术语过密（DDR 定义 + Cohen's d 数值对非专业读者意义不大）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提，R1同意。建议用 'large effect sizes' 定性描述替代具体 d 值。\"}\n  action_items:\n    - {round: 25, action: \"Abstract 中移除 Cohen's d 数值，用定性描述替代\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"Figure 1 灰度打印下 per-generator 彩色点难以区分\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2首提，R1同意。ACL 要求 figures should be legible in grayscale。\"}\n  action_items:\n    - {round: 25, action: \"增加 marker shape 区分或确保灰度可辨\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Table 2 pooled vs per-generator macro F1 差异 (0.706 vs 0.694) 未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 M1 + R2 M4 均提出。\"}\n  action_items:\n    - {round: 25, action: \"在 §4.1 或 Table 2 caption 中解释 pooled vs per-generator macro 的区别\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M5\"\n  summary: \"无匿名代码/数据链接，降低 reproducibility 评估能力\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R2 M5 首提，R1同意。Ethics §9 承诺开源但 review 阶段无匿名链接。\"}\n  action_items:\n    - {round: 25, action: \"提供 anonymous GitHub 或 supplementary zip\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M6\"\n  summary: \"Cross-domain 覆盖不足（仅 3 域，每域 200 seeds/3 generators）\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 W7 首提(moderate)，R2同意但降为 minor。Social media/dialogue/creative writing 未覆盖。\"}\n  action_items:\n    - {round: 25, action: \"增加 1-2 个 domain 或 acknowledge cross-domain claim 为 preliminary\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M7\"\n  summary: \"entropy_min 对分类零贡献 (LOFO Δ=+0.01pp)，保留仅为维持 3/1/3 对称\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: \"R1,R2\", note: \"R1 Q2 首提，R2同意。Permutation importance 仅 0.015。cleanliness 问题非 validity 问题。\"}\n  action_items:\n    - {round: 25, action: \"讨论 entropy_min 的零贡献及其对 DDR narrative 的影响\", assigned_to: \"pending\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1879 · 2026-05-19T04:59:06.259841+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 12043}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1880 · 2026-05-19T05:01:25.908079+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "report": "# Round 25 审稿报告（Fresh Review）\n\n**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: R1（方法严谨性+实验设计）+ R2（新颖性+完整性+写作质量）\n**审稿轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务（gen-0/gen-1/gen-2+），将传统二元检测扩展到递归生成深度分类。核心发现是 differential depth response (DDR)：7 个手工特征在 8 个 base model generators（5 families, 0.6B-8B）上系统分为 drifting (3)、intermediate (1)、near-stationary (3) 三组。XGBoost 集成分类器在 LOGO 评估下达到 leak-free binary F1=0.694。论文实验设计严谨（LOGO/LOFO/seed 控制/length confound），统计检验覆盖面广，但 DDR 的新颖性有限、base model 限制严重削弱 impact、下游应用价值未建立。\n\n---\n\n## Strengths\n\n**S1. 问题形式化有价值且定位清晰。** 将递归生成深度分类作为独立任务首次系统性提出，与 binary detection、source attribution、production mode classification 形成正交维度。与 model collapse 文献互补但不重叠。[R1, R2 共识]\n\n**S2. 实验设计严谨程度高于该领域平均水准。** Binary F1 排除 gen-0 消除 seed sharing 偏差；独立 seed 控制实验（F1=0.680）确认信号非 seed-specific；length-matched subsampling 三重控制 confound。LOGO/LOFO 双协议验证跨 generator/family 泛化。[R1, R2 共识]\n\n**S3. 统计检验规范且多层验证。** Bootstrap CI (n=1000)、McNemar test、Bonferroni 校正、Levene test、KS test、TOST 等价性检验、Glass's Δ、Cliff's δ 等多种工具互相印证。这是该领域少见的严谨程度。[R1, R2 共识]\n\n**S4. 对自身方法局限的透明度高。** \"DDR is an empirical decomposition, not a claimed universal law\"（§5 L6）。Limitations 对 base model 限制、temperature sensitivity、downstream 无效等问题的讨论诚实。论文明确 disclaim DDR 的 universality。[R1, R2 共识]\n\n**S5. Baseline 比较定位诚实。** §4.3 明确将比较定位为 \"contextualize depth discrimination ability rather than claim competitive advantage\"，避免过度宣传。[R1]\n\n**S6. 写作 AI 痕迹已基本清除。** 无 em-dash/en-dash（数字范围除外），无 Furthermore/Moreover/Additionally 堆叠，无黑名单用词。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [Critical, R1+R2 共识] DDR 新颖性不足以支撑 Main Conference 核心贡献。**\nDDR 本质上是已知特征（NLL mean/TTR/hapax）在递归生成下行为差异的系统化表述。三个 drifting features 共享 92.3% variance（PCA），TTR-hapax r=0.97，\"7-feature ensemble\"实际是 ~4 维系统。在 model collapse 文献（vocabulary diversity 下降、NLL 分布 shift）的背景下，\"location 特征漂移、shape 特征不变\"是预期之中的发现。DDR 的\"命名\"（drifting/intermediate/near-stationary）和 3/1/3 partition 增加了术语但未带来概念突破。R1 补充：DDR 跨 8 个 generator 的一致性有价值，但对 Main 不够。\n\n**N2 [Critical, R1+R2 共识] Base model 限制严重削弱实际 impact。**\nInstruction-tuned models 下信号崩溃（OLMo-Instruct LOGO F1=0.338 vs 0.763 base），而 web 文本主要来自 instruction-tuned/RLHF-aligned models。Downstream 实验（n=3 seeds）显示 depth-aware curation 与 random subsampling 统计等价，且 random 反而略优（PPL 2367 vs 2387）。**关键未利用发现**：R1 在交叉回应中指出，instruct model 的 entropy mean ρ 从 -0.60 反转为 +0.48（6/7 features 反号 for OLMo/Qwen），说明 depth signal 存在但方向反转——retrain classifier with instruct data 可能恢复 F1。这一发现本身可成为独立 contribution，但论文仅用一句话带过。\n\n**N3 [Critical, R1 提出 + R2 同意] Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导。**\nDDR tri-partition 的核心分区阈值是 post-hoc 选择的——\"the drifting boundary reflects the natural gap between hapax ratio (d=0.76) and entropy std (d=0.55)\"是在看到所有 d 值后描述 gap，而非 pre-specified。0.10（near-stationary）阈值无类似 gap 论证。k=3 clustering 时 entropy_min 自成一类（Appendix V Table 25），说明 3/1/3 非最自然的数据驱动分区。R2 补充：若 partition 变化但 F1 不变，反而削弱 DDR 作为核心贡献的必要性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [Major, R1 提出 + R2 降级] TOST 等价性检验对 near-stationary 特征部分失败。**\nTail decay 仅 4/8 generators 通过 TOST（ε=0.20），entropy max 6/8。R1 初评 Critical，R2 认为 Major 更合理——primary partition (k=2, silhouette=0.632) 不受影响，即使 tail decay 重分类为 intermediate (3/2/2) 核心叙事不变。**Director 采纳 Major。**\n\n**W2 [Major, R1 提出 + R2 rebut 成功，降级] 异方差下 pooled Cohen's d 作为主要分区指标。**\nLevene tests 拒绝等方差（方差比 1.86-2.21），但论文已在 Appendix V 提供 Glass's Δ + Cliff's δ 三重验证，partition gap ≥9.5× 在所有 metrics 下一致。正文 §4.2 也引用了 heteroscedasticity-robust metrics。R1 初评 Critical，R2 rebut 成功。**Director 降为 Major**——但 Glass's Δ 应在正文中更突出展示，而非仅放 Appendix。\n\n**W3 [Major, R1+R2 共识] TTR-hapax r=0.97 + PCA 92.3%：保留三个 drifting 特征的理由是循环论证。**\n\"Individual features enable DDR decomposition\" → 但 DDR 分解需要三个特征 → 三个特征证明 DDR 分解。PC1 替代仅损失 1.1pp (§4.2)。联合移除 TTR+hapax 的消融未报告。\n\n**W4 [Major, R2 提出 + R1 同意] Generator subset 不一致（5/6/8-gen 混用）。**\n至少 6 种 subset 配置分布于正文和附录。跨实验比较困难——温度消融 4-gen 结果能否推广到另外 4 个 generator 未讨论。\n\n**W5 [Major, R2 提出 + R1 同意] 遗漏重要相关工作。**\nVarshini et al., \"Unveiling Attractor Cycles in Large Language Models\" (ACL 2025) 直接分析连续 paraphrasing 中的 attractor 周期，与论文多处使用的 \"generation attractor\" 概念直接相关但未引用。\n\n**W6 [Major, R1+R2 共识] Downstream 实验 n=3 seeds 严重 underpowered。**\nCohen's d 被极小 pooled std 膨胀到 86-120（论文自承 unreliable）。Discussion §5 基于此 null result 转向 \"structure identification\" framing，但如果 10+ seeds 后发现微弱效果，整个 framing 需要改变。\n\n**W7 [Major, R1+R2 共识] Instruct model 退化缺乏 mechanistic 分析。**\n论文仅描述性报告 F1 下降和 ρ 反号，未分析 WHY（特征分布变化？DDR 分区失效？RLHF 改变递归动态？）。R1 强调这是论文中最有潜力的 unrealized finding。\n\n**W8 [Major, R2 提出 + R1 同意] Contribution 分量不均。**\nC1（task formulation）和 C3（boundary conditions）更像标准实验设计而非独立贡献。DDR（C2）是唯一实质性发现。\"一个观察被拆成三条来凑分量\"的印象。\n\n**W9 [Major, R1 提出 + R2 partially agree] Reference model same-family 偏差。**\nPythia-410M 与 Pythia generators 同家族。Cross-reference 验证仅在 5-gen subset 上（spread 0.013）。Pythia generators 获最高 F1 (0.724) 可能部分归因于亲和性。\n\n**W10 [Major, R1 提出 + R2 同意] 温度消融 OLMo checkpoint 不一致。**\n温度实验用 OLMo-2-0425-1B，主实验用原始 OLMo-2-1B-hf（已不可用）。Checkpoint 差异与 temperature 效应混淆。\n\n**W11 [Major, R2 Q4 提出 + R1 同意] Cross-model chains F1=0.764 > single-gen LOGO F1=0.694 未解释。**\n可能原因：generator heterogeneity 放大 depth signal（含 generator identity confound）。论文呈现为 positive evidence 但未排除 confound。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n1. DDR 新颖性对 Main Conference 不足，Findings 级别合适 [N1]\n2. Base model 限制是论文最大的 practical constraint [N2]\n3. Cohen's d 阈值是 post-hoc gap-driven，非 principled [N3]\n4. TTR-hapax 冗余和 PCA 单维度是实质问题 [W3]\n5. Downstream n=3 underpowered，不足以支撑 framing 转向 [W6]\n6. Instruct model ρ 反转是最有潜力的 unrealized finding [W7]\n7. Contribution 分量不均 [W8]\n8. \", confirming\" 9+ 次是 AI 写作标志 [M1]\n\n## Reviewer Divergence\n\n以下问题经交叉讨论后解决（无遗留分歧）：\n1. **R1-N3 (异方差/pooled d)**: R1 初评 Critical → R2 rebut（三重验证 + ≥9.5× gap）→ **Director 降为 Major** [W2]\n2. **R2-W4 (引用验证)**: R2 初评 warning → R1 rebut（OpenAlex false negatives，非实质问题）→ **Director 采纳 R1 rebut，不列入报告**\n3. **R1-Q3 (cross-ref subset)**: R2 rebut（0.013 spread 远小于 9.1pp generator 间差异）→ 降为 Minor 建议\n4. **R1-Q4 (fundamental claim)**: R2 rebut（论文三处明确否认 DDR 是 universal/fundamental）→ 不构成问题\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** DDR 的 location/shape decomposition 是否有理论解释？为什么 softmax 在递归条件下 location shift 但 shape 稳定？是否与 temperature 作为 shape 控制参数相关？[R1+R2 共识]\n\n**Q2.** 为什么不直接用 PC1 替代三个 drifting features？如果 DDR decomposition 的解释性价值是唯一保留理由，为什么分类系统中不使用 PC1 简化？[R1+R2 共识]\n\n**Q3.** Instruct model 的 entropy mean ρ 反号（-0.60→+0.48）是否意味着 depth signal 仍存在但方向反转？如果在 instruct data 上 retrain classifier，F1 是否恢复？这是论文应该展开的最重要方向。[R1+R2 共识]\n\n**Q4.** Cross-model chains F1=0.764 > single-gen LOGO F1=0.694——是 generator heterogeneity 放大 depth signal，还是存在 generator identity confound？[R2 提出, R1 同意]\n\n**Q5.** Depth classification 的 practical ceiling（Bayes error rate）是多少？QLoRA 的 binary F1 未报告，知道它可以帮助判断 7-feature ensemble 距 ceiling 多远。[R1]\n\n**Q6.** 更深的链（gen-5+）中 DDR 特征是否完全 converge（inter-class KS→0）？这可为 attractor 叙事提供更强支撑。[R1]\n\n---\n\n## Missing References\n\n1. **Varshini et al., \"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\" (ACL 2025)** — 直接分析连续 paraphrasing 中的 attractor 周期，与论文 \"generation attractor\" 概念直接相关。[R1+R2 共识]\n2. **\"How to Synthesize Text Data without Model Collapse?\" (2024)** — 递归生成质量退化与 data provenance 叙事相关。[R2]\n3. **Ordinal classification 方法文献覆盖不足** — CORAL/CORN 仅在 Appendix 一笔带过，正文 task formulation 为 ordinal classification 但无充分引用。[R1]\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer）：**未配置**。项目 config 中未启用 `external_review.paperreview_ai`。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings（可被 Findings 接收）**\n**置信度: 4/5（两位 Reviewer 均仔细阅读全文含 29 页附录）**\n\n### ACL ARR 维度评分（两位 Reviewer 平均）\n\n| 维度 | R1 | R2 | 平均 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 2.5 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n### 判断依据\n\n**支持 Findings（3.0）的理由：**\n- 问题形式化（depth classification beyond binary）有价值\n- 实验设计和统计规范高于该领域平均\n- DDR 三分区作为分析框架有整理价值\n- 对自身 limitations 的透明度是正面信号\n\n**不支持 Main Conference（≥3.5）的理由：**\n- DDR 新颖性有限——本质是已知特征的行为分类，非概念突破\n- Base model 限制严重——web 场景下几乎不适用\n- Downstream 实验否定了实用价值\n- 贡献分量不均，核心 insight 可用一段话概括\n- Feature 冗余严重（7 features → ~4 独立维度）\n\n**提升至 3.5 (Borderline Conference) 的条件：**\n1. 展开 instruct model ρ 反转分析（retrain classifier + mechanistic 解释）——这可同时解决 novelty 和 applicability 问题\n2. 提供 DDR location/shape 分离的理论解释（至少 informal conjecture）\n3. 修复 Cohen's d 阈值的 principled justification\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 四个必答问题回答完整，篇幅适当（~120 words）\n- Cohen's d 数值对非专业读者意义不大，建议用定性描述替代\n- \"restricting current applicability to base models\" 最后一句设定期望是好选择\n\n### Introduction\n- 叙事线清晰：递归生成 → 二元检测不够 → depth classification → DDR → 贡献\n- \"No existing method provides a feature-level decomposition\" 需确认 concurrent work 未做此事\n- Contribution #3 过于技术化（temperature ranges, ρ 数值），适合 Results 而非 Introduction\n- \"empirical rather than methodological\" 的自我定位是诚实的，但与 C3 \"mechanistic boundary conditions\" 有 tension\n\n### Related Work\n- 覆盖面广，positioning 清晰\n- 对 concurrent work (broken_telephone, markovian_chains) 三重区分合理\n- 遗漏 Varshini et al. (ACL 2025) attractor cycles\n- 引用密度 ~70 条，对 EMNLP Long Paper 偏少但可接受\n- §2.3 / §2.4 分界不够自然\n\n### Method\n- Task formulation、generation chain construction、feature extraction、evaluation protocol 结构清晰\n- \"entropy\" as shorthand for NLL 的 convention acknowledgment 合理\n- Feature selection a priori 是合理决策但限制了 feature space 探索\n\n### Results\n- Binary F1 作为 primary metric（排除 gen-0 leak）是 key methodological design\n- DDR 分析是全文亮点也是最大弱点\n- Baseline 比较定位正确（\"contextualize\"而非\"compete\"）\n- gen-2+ 错分为 gen-1 是主要 failure point (40.2%)，应在正文提及\n- Table 1 vs Table 2 的 F1 差异 (0.694 vs 0.706) 应更显著标注\n\n### Discussion\n- Location/shape decomposition 的 post-hoc 定位恰当\n- Instruct model 讨论充分但缺少对策和 mechanistic 分析\n- DDR vs model collapse 区分过于简短\n\n### Conclusion\n- 过于简短（3 句），未 highlight future work 方向\n\n### Limitations\n- 覆盖面全面，应增加 DDR 阈值选择局限性的 acknowledgment\n\n### 格式合规性\n- ✅ 正文 8 页（符合 Long paper 限制）\n- ✅ 匿名化完整（\"Anonymous ACL submission\"）\n- ✅ 行号开启，ACL template + [review] option\n- ✅ Limitations 和 Ethics Statement 存在\n- ⚠️ 无匿名代码/数据链接\n- ⚠️ Responsible NLP Checklist 需确认已通过 OpenReview 提交\n- ⚠️ \", confirming\" 9+ 次 —— 轻微 AI 写作标志，需修复"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "report": "# Round 25 审稿报告（Fresh Review）\n\n**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: R1（方法严谨性+实验设计）+ R2（新颖性+完整性+写作质量）\n**审稿轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文提出 generation depth classification 任务（gen-0/gen-1/gen-2+），将传统二元检测扩展到递归生成深度分类。核心发现是 differential depth response (DDR)：7 个手工特征在 8 个 base model generators（5 families, 0.6B-8B）上系统分为 drifting (3)、intermediate (1)、near-stationary (3) 三组。XGBoost 集成分类器在 LOGO 评估下达到 leak-free binary F1=0.694。论文实验设计严谨（LOGO/LOFO/seed 控制/length confound），统计检验覆盖面广，但 DDR 的新颖性有限、base model 限制严重削弱 impact、下游应用价值未建立。\n\n---\n\n## Strengths\n\n**S1. 问题形式化有价值且定位清晰。** 将递归生成深度分类作为独立任务首次系统性提出，与 binary detection、source attribution、production mode classification 形成正交维度。与 model collapse 文献互补但不重叠。[R1, R2 共识]\n\n**S2. 实验设计严谨程度高于该领域平均水准。** Binary F1 排除 gen-0 消除 seed sharing 偏差；独立 seed 控制实验（F1=0.680）确认信号非 seed-specific；length-matched subsampling 三重控制 confound。LOGO/LOFO 双协议验证跨 generator/family 泛化。[R1, R2 共识]\n\n**S3. 统计检验规范且多层验证。** Bootstrap CI (n=1000)、McNemar test、Bonferroni 校正、Levene test、KS test、TOST 等价性检验、Glass's Δ、Cliff's δ 等多种工具互相印证。这是该领域少见的严谨程度。[R1, R2 共识]\n\n**S4. 对自身方法局限的透明度高。** \"DDR is an empirical decomposition, not a claimed universal law\"（§5 L6）。Limitations 对 base model 限制、temperature sensitivity、downstream 无效等问题的讨论诚实。论文明确 disclaim DDR 的 universality。[R1, R2 共识]\n\n**S5. Baseline 比较定位诚实。** §4.3 明确将比较定位为 \"contextualize depth discrimination ability rather than claim competitive advantage\"，避免过度宣传。[R1]\n\n**S6. 写作 AI 痕迹已基本清除。** 无 em-dash/en-dash（数字范围除外），无 Furthermore/Moreover/Additionally 堆叠，无黑名单用词。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [Critical, R1+R2 共识] DDR 新颖性不足以支撑 Main Conference 核心贡献。**\nDDR 本质上是已知特征（NLL mean/TTR/hapax）在递归生成下行为差异的系统化表述。三个 drifting features 共享 92.3% variance（PCA），TTR-hapax r=0.97，\"7-feature ensemble\"实际是 ~4 维系统。在 model collapse 文献（vocabulary diversity 下降、NLL 分布 shift）的背景下，\"location 特征漂移、shape 特征不变\"是预期之中的发现。DDR 的\"命名\"（drifting/intermediate/near-stationary）和 3/1/3 partition 增加了术语但未带来概念突破。R1 补充：DDR 跨 8 个 generator 的一致性有价值，但对 Main 不够。\n\n**N2 [Critical, R1+R2 共识] Base model 限制严重削弱实际 impact。**\nInstruction-tuned models 下信号崩溃（OLMo-Instruct LOGO F1=0.338 vs 0.763 base），而 web 文本主要来自 instruction-tuned/RLHF-aligned models。Downstream 实验（n=3 seeds）显示 depth-aware curation 与 random subsampling 统计等价，且 random 反而略优（PPL 2367 vs 2387）。**关键未利用发现**：R1 在交叉回应中指出，instruct model 的 entropy mean ρ 从 -0.60 反转为 +0.48（6/7 features 反号 for OLMo/Qwen），说明 depth signal 存在但方向反转——retrain classifier with instruct data 可能恢复 F1。这一发现本身可成为独立 contribution，但论文仅用一句话带过。\n\n**N3 [Critical, R1 提出 + R2 同意] Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导。**\nDDR tri-partition 的核心分区阈值是 post-hoc 选择的——\"the drifting boundary reflects the natural gap between hapax ratio (d=0.76) and entropy std (d=0.55)\"是在看到所有 d 值后描述 gap，而非 pre-specified。0.10（near-stationary）阈值无类似 gap 论证。k=3 clustering 时 entropy_min 自成一类（Appendix V Table 25），说明 3/1/3 非最自然的数据驱动分区。R2 补充：若 partition 变化但 F1 不变，反而削弱 DDR 作为核心贡献的必要性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [Major, R1 提出 + R2 降级] TOST 等价性检验对 near-stationary 特征部分失败。**\nTail decay 仅 4/8 generators 通过 TOST（ε=0.20），entropy max 6/8。R1 初评 Critical，R2 认为 Major 更合理——primary partition (k=2, silhouette=0.632) 不受影响，即使 tail decay 重分类为 intermediate (3/2/2) 核心叙事不变。**Director 采纳 Major。**\n\n**W2 [Major, R1 提出 + R2 rebut 成功，降级] 异方差下 pooled Cohen's d 作为主要分区指标。**\nLevene tests 拒绝等方差（方差比 1.86-2.21），但论文已在 Appendix V 提供 Glass's Δ + Cliff's δ 三重验证，partition gap ≥9.5× 在所有 metrics 下一致。正文 §4.2 也引用了 heteroscedasticity-robust metrics。R1 初评 Critical，R2 rebut 成功。**Director 降为 Major**——但 Glass's Δ 应在正文中更突出展示，而非仅放 Appendix。\n\n**W3 [Major, R1+R2 共识] TTR-hapax r=0.97 + PCA 92.3%：保留三个 drifting 特征的理由是循环论证。**\n\"Individual features enable DDR decomposition\" → 但 DDR 分解需要三个特征 → 三个特征证明 DDR 分解。PC1 替代仅损失 1.1pp (§4.2)。联合移除 TTR+hapax 的消融未报告。\n\n**W4 [Major, R2 提出 + R1 同意] Generator subset 不一致（5/6/8-gen 混用）。**\n至少 6 种 subset 配置分布于正文和附录。跨实验比较困难——温度消融 4-gen 结果能否推广到另外 4 个 generator 未讨论。\n\n**W5 [Major, R2 提出 + R1 同意] 遗漏重要相关工作。**\nVarshini et al., \"Unveiling Attractor Cycles in Large Language Models\" (ACL 2025) 直接分析连续 paraphrasing 中的 attractor 周期，与论文多处使用的 \"generation attractor\" 概念直接相关但未引用。\n\n**W6 [Major, R1+R2 共识] Downstream 实验 n=3 seeds 严重 underpowered。**\nCohen's d 被极小 pooled std 膨胀到 86-120（论文自承 unreliable）。Discussion §5 基于此 null result 转向 \"structure identification\" framing，但如果 10+ seeds 后发现微弱效果，整个 framing 需要改变。\n\n**W7 [Major, R1+R2 共识] Instruct model 退化缺乏 mechanistic 分析。**\n论文仅描述性报告 F1 下降和 ρ 反号，未分析 WHY（特征分布变化？DDR 分区失效？RLHF 改变递归动态？）。R1 强调这是论文中最有潜力的 unrealized finding。\n\n**W8 [Major, R2 提出 + R1 同意] Contribution 分量不均。**\nC1（task formulation）和 C3（boundary conditions）更像标准实验设计而非独立贡献。DDR（C2）是唯一实质性发现。\"一个观察被拆成三条来凑分量\"的印象。\n\n**W9 [Major, R1 提出 + R2 partially agree] Reference model same-family 偏差。**\nPythia-410M 与 Pythia generators 同家族。Cross-reference 验证仅在 5-gen subset 上（spread 0.013）。Pythia generators 获最高 F1 (0.724) 可能部分归因于亲和性。\n\n**W10 [Major, R1 提出 + R2 同意] 温度消融 OLMo checkpoint 不一致。**\n温度实验用 OLMo-2-0425-1B，主实验用原始 OLMo-2-1B-hf（已不可用）。Checkpoint 差异与 temperature 效应混淆。\n\n**W11 [Major, R2 Q4 提出 + R1 同意] Cross-model chains F1=0.764 > single-gen LOGO F1=0.694 未解释。**\n可能原因：generator heterogeneity 放大 depth signal（含 generator identity confound）。论文呈现为 positive evidence 但未排除 confound。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n1. DDR 新颖性对 Main Conference 不足，Findings 级别合适 [N1]\n2. Base model 限制是论文最大的 practical constraint [N2]\n3. Cohen's d 阈值是 post-hoc gap-driven，非 principled [N3]\n4. TTR-hapax 冗余和 PCA 单维度是实质问题 [W3]\n5. Downstream n=3 underpowered，不足以支撑 framing 转向 [W6]\n6. Instruct model ρ 反转是最有潜力的 unrealized finding [W7]\n7. Contribution 分量不均 [W8]\n8. \", confirming\" 9+ 次是 AI 写作标志 [M1]\n\n## Reviewer Divergence\n\n以下问题经交叉讨论后解决（无遗留分歧）：\n1. **R1-N3 (异方差/pooled d)**: R1 初评 Critical → R2 rebut（三重验证 + ≥9.5× gap）→ **Director 降为 Major** [W2]\n2. **R2-W4 (引用验证)**: R2 初评 warning → R1 rebut（OpenAlex false negatives，非实质问题）→ **Director 采纳 R1 rebut，不列入报告**\n3. **R1-Q3 (cross-ref subset)**: R2 rebut（0.013 spread 远小于 9.1pp generator 间差异）→ 降为 Minor 建议\n4. **R1-Q4 (fundamental claim)**: R2 rebut（论文三处明确否认 DDR 是 universal/fundamental）→ 不构成问题\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** DDR 的 location/shape decomposition 是否有理论解释？为什么 softmax 在递归条件下 location shift 但 shape 稳定？是否与 temperature 作为 shape 控制参数相关？[R1+R2 共识]\n\n**Q2.** 为什么不直接用 PC1 替代三个 drifting features？如果 DDR decomposition 的解释性价值是唯一保留理由，为什么分类系统中不使用 PC1 简化？[R1+R2 共识]\n\n**Q3.** Instruct model 的 entropy mean ρ 反号（-0.60→+0.48）是否意味着 depth signal 仍存在但方向反转？如果在 instruct data 上 retrain classifier，F1 是否恢复？这是论文应该展开的最重要方向。[R1+R2 共识]\n\n**Q4.** Cross-model chains F1=0.764 > single-gen LOGO F1=0.694——是 generator heterogeneity 放大 depth signal，还是存在 generator identity confound？[R2 提出, R1 同意]\n\n**Q5.** Depth classification 的 practical ceiling（Bayes error rate）是多少？QLoRA 的 binary F1 未报告，知道它可以帮助判断 7-feature ensemble 距 ceiling 多远。[R1]\n\n**Q6.** 更深的链（gen-5+）中 DDR 特征是否完全 converge（inter-class KS→0）？这可为 attractor 叙事提供更强支撑。[R1]\n\n---\n\n## Missing References\n\n1. **Varshini et al., \"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\" (ACL 2025)** — 直接分析连续 paraphrasing 中的 attractor 周期，与论文 \"generation attractor\" 概念直接相关。[R1+R2 共识]\n2. **\"How to Synthesize Text Data without Model Collapse?\" (2024)** — 递归生成质量退化与 data provenance 叙事相关。[R2]\n3. **Ordinal classification 方法文献覆盖不足** — CORAL/CORN 仅在 Appendix 一笔带过，正文 task formulation 为 ordinal classification 但无充分引用。[R1]\n\n---\n\n## External Review\n\n外部审稿（Stanford Agentic Reviewer）：**未配置**。项目 config 中未启用 `external_review.paperreview_ai`。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings（可被 Findings 接收）**\n**置信度: 4/5（两位 Reviewer 均仔细阅读全文含 29 页附录）**\n\n### ACL ARR 维度评分（两位 Reviewer 平均）\n\n| 维度 | R1 | R2 | 平均 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 2.5 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n### 判断依据\n\n**支持 Findings（3.0）的理由：**\n- 问题形式化（depth classification beyond binary）有价值\n- 实验设计和统计规范高于该领域平均\n- DDR 三分区作为分析框架有整理价值\n- 对自身 limitations 的透明度是正面信号\n\n**不支持 Main Conference（≥3.5）的理由：**\n- DDR 新颖性有限——本质是已知特征的行为分类，非概念突破\n- Base model 限制严重——web 场景下几乎不适用\n- Downstream 实验否定了实用价值\n- 贡献分量不均，核心 insight 可用一段话概括\n- Feature 冗余严重（7 features → ~4 独立维度）\n\n**提升至 3.5 (Borderline Conference) 的条件：**\n1. 展开 instruct model ρ 反转分析（retrain classifier + mechanistic 解释）——这可同时解决 novelty 和 applicability 问题\n2. 提供 DDR location/shape 分离的理论解释（至少 informal conjecture）\n3. 修复 Cohen's d 阈值的 principled justification\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 四个必答问题回答完整，篇幅适当（~120 words）\n- Cohen's d 数值对非专业读者意义不大，建议用定性描述替代\n- \"restricting current applicability to base models\" 最后一句设定期望是好选择\n\n### Introduction\n- 叙事线清晰：递归生成 → 二元检测不够 → depth classification → DDR → 贡献\n- \"No existing method provides a feature-level decomposition\" 需确认 concurrent work 未做此事\n- Contribution #3 过于技术化（temperature ranges, ρ 数值），适合 Results 而非 Introduction\n- \"empirical rather than methodological\" 的自我定位是诚实的，但与 C3 \"mechanistic boundary conditions\" 有 tension\n\n### Related Work\n- 覆盖面广，positioning 清晰\n- 对 concurrent work (broken_telephone, markovian_chains) 三重区分合理\n- 遗漏 Varshini et al. (ACL 2025) attractor cycles\n- 引用密度 ~70 条，对 EMNLP Long Paper 偏少但可接受\n- §2.3 / §2.4 分界不够自然\n\n### Method\n- Task formulation、generation chain construction、feature extraction、evaluation protocol 结构清晰\n- \"entropy\" as shorthand for NLL 的 convention acknowledgment 合理\n- Feature selection a priori 是合理决策但限制了 feature space 探索\n\n### Results\n- Binary F1 作为 primary metric（排除 gen-0 leak）是 key methodological design\n- DDR 分析是全文亮点也是最大弱点\n- Baseline 比较定位正确（\"contextualize\"而非\"compete\"）\n- gen-2+ 错分为 gen-1 是主要 failure point (40.2%)，应在正文提及\n- Table 1 vs Table 2 的 F1 差异 (0.694 vs 0.706) 应更显著标注\n\n### Discussion\n- Location/shape decomposition 的 post-hoc 定位恰当\n- Instruct model 讨论充分但缺少对策和 mechanistic 分析\n- DDR vs model collapse 区分过于简短\n\n### Conclusion\n- 过于简短（3 句），未 highlight future work 方向\n\n### Limitations\n- 覆盖面全面，应增加 DDR 阈值选择局限性的 acknowledgment\n\n### 格式合规性\n- ✅ 正文 8 页（符合 Long paper 限制）\n- ✅ 匿名化完整（\"Anonymous ACL submission\"）\n- ✅ 行号开启，ACL template + [review] option\n- ✅ Limitations 和 Ethics Statement 存在\n- ⚠️ 无匿名代码/数据链接\n- ⚠️ Responsible NLP Checklist 需确认已通过 OpenReview 提交\n- ⚠️ \", confirming\" 9+ 次 —— 轻微 AI 写作标志，需修复"
  }
}
```

</details>

---


### Tool result

_source line 1881 · 2026-05-19T05:01:29.878229+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3970
}
```

</details>

---


### Assistant

_source line 1882 · 2026-05-19T05:01:38.204209+00:00_

审稿报告已投递至 Research Director。

---

**Round 25 审稿完成（Fresh Review）。**

**最终评分：3.0 — Findings**

核心发现：
- **3 个 Critical 问题**：DDR 新颖性不足(N1)、base model 限制(N2)、Cohen's d 阈值非 principled(N3)
- **11 个 Major 问题**：TOST 部分失败、pooled d 异方差、TTR-hapax 冗余、generator subset 混用、遗漏引用、downstream underpowered、instruct 未分析、contribution 不均、reference model 偏差、OLMo checkpoint 混淆、cross-model F1 未解释
- **7 个 Minor 问题**：AI 写作标志(", confirming" 9+次)、Abstract 术语密度、Figure 灰度可辨性等

**最大遗憾**：instruct model entropy mean ρ 反转（-0.60→+0.48）是论文中最有潜力的 unrealized finding。若展开分析可同时解决 novelty 和 applicability 问题，可能提升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 1883 · 2026-05-19T05:01:40.879932+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

**关键判断**：
- R2 的 N1（DDR 新颖性）和 N2（base model 限制）方向正确，但对 Findings 来说严厉度偏高
- R2-Q3（instruct model entropy ρ 反号）是最有价值的发现——信号不是消失而是反转，这本身可以成为独立 contribution
- R2-Q4（cross-model F1 > single-generator F1）暴露了可能的 generator identity confound
- R2-W4（引用验证）我反驳——9 条 not_found 均为 OpenAlex 覆盖不足的知名论文
- 维持 **Overall 3.0 (Findings)** 评分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1884 · 2026-05-19T05:01:54.402941+00:00_

审稿报告已提交至 Research Director。

**Round 25 审稿完成（Fresh Review）。**

**最终评分：Overall 3.0 — Findings**（两位 Reviewer 一致）

**核心问题摘要：**
- **3 个 Critical**：DDR 新颖性不足（N1）、base model 限制（N2）、Cohen's d 阈值缺乏 principled 依据（N3）
- **11 个 Major**：TOST 部分失败、pooled d 异方差、TTR-hapax 冗余/PCA 循环论证、generator subset 不一致、遗漏 attractor cycles 引用、downstream underpowered、instruct ρ 反转未利用、contribution 分量不均、reference model 偏差、OLMo checkpoint 混淆、cross-model F1 confound
- **7 个 Minor**：AI 写作痕迹（", confirming" 9+次）、Abstract 术语密度、Figure 灰度可辨性等

**最重要的 actionable insight**：instruct model 的 entropy mean ρ 从 -0.60 反转为 +0.48——depth signal 不是消失而是方向反转。展开此分析可同时解决 novelty 和 applicability 两个 critical 问题，有望将评分提升至 3.5 (Borderline Conference)。

Issue Tracker 已同步更新（`review_issues.yaml`，20 条 issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 173

## Round 173

72 recorded events


### User

_source line 1885 · 2026-05-19T06:12:33.130510+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1886 · 2026-05-19T06:12:40.451668+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1887 · 2026-05-19T06:12:40.502652+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1888 · 2026-05-19T06:12:43.062351+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1889 · 2026-05-19T06:12:43.113045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1890 · 2026-05-19T06:12:47.339875+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,read_project_file,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,read_project_file,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1891 · 2026-05-19T06:12:47.340273+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1892 · 2026-05-19T06:12:49.700148+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1893 · 2026-05-19T06:12:49.800902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1894 · 2026-05-19T06:12:52.885635+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1895 · 2026-05-19T06:12:52.885979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1896 · 2026-05-19T06:12:53.136700+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "request_external_review",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "request_external_review",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1897 · 2026-05-19T06:12:53.137031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-19T06:12:53.639725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1899 · 2026-05-19T06:12:53.640136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1900 · 2026-05-19T06:12:54.091416+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1901 · 2026-05-19T06:12:54.091768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1902 · 2026-05-19T06:12:54.542973+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1903 · 2026-05-19T06:12:54.543303+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1904 · 2026-05-19T06:12:54.743904+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1905 · 2026-05-19T06:12:54.794454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-19T06:12:59.060718+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 1907 · 2026-05-19T06:12:59.964876+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (56 个)\n\n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 提交前最终检查（OpenReview form, AI disclosure）\n\n## 温度扩展实验结果（全部完成，已写入论文）\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\n|-------|------|-----------|--------|-------------|\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\n\n## 其他近期结论\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\n\n## 论文状态\n全部编辑完成，编译 0 errors，27 页。\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\n- appendix_tost.tex（8×7 per-generator TOST table）\n- appendix_classifier.tex OLMo 版本脚
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-19T06:13:00.015543+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1909 · 2026-05-19T06:13:01.370106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1910 · 2026-05-19T06:13:01.470799+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{lineno}
12	\usepackage{placeins}
13	\usepackage{multirow}
14	\linenumbers
15	
16	\graphicspath{{../chart/}}
17	
18	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base LLM Text Chains}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{results}
31	
32	\input{discussion}
33	\input{conclusion}
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\appendix
40	
41	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
42	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
43	
44	\input{appendix_dataset_stats}
45	\FloatBarrier
46	
47	\section{Length Confound Analysis}
48	\label{app:length}
49	\input{appendix_length}
50	\FloatBarrier
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	\FloatBarrier
56	
57	\section{Finer-Grained Depth Classification}
58	\label{app:finer-depth}
59	\input{appendix_finer_depth}
60	\FloatBarrier
61	
62	\section{End-to-End Depth Classification (QLoRA)}
63	\label{app:qlora}
64	\input{appendix_qlora}
65	\FloatBarrier
66	
67	\section{Leave-One-Feature-Out Analysis}
68	\label{app:lofo}
69	\input{appendix_lofo}
70	\FloatBarrier
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	\FloatBarrier
76	
77	\section{Classifier Sensitivity}
78	\label{app:classifier}
79	\input{appendix_classifier}
80	\FloatBarrier
81	
82	\section{Robustness to Text Pert
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1911 · 2026-05-19T06:13:05.285883+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found search results related to EMNLP 2026 and ARR (ACL Rolling Review), though the results mostly show information about wor
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5270
}
```

</details>

---


### Tool call

_source line 1912 · 2026-05-19T06:13:08.146798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1913 · 2026-05-19T06:13:08.498203+00:00_

100	\FloatBarrier
101	
102	\section{Downstream Utility}
103	\label{app:downstream}
104	\input{appendix_downstream}
105	\FloatBarrier
106	
107	\section{Cross-Model Chain Per-Class Detail}
108	\label{app:cross-model-detail}
109	\input{appendix_cross_model_detail}
110	\FloatBarrier
111	
112	\section{Feature Distribution Analysis}
113	\label{app:feature-distributions}
114	\input{appendix_feature_distributions}
115	\FloatBarrier
116	
117	\section{Cross-Temperature Transfer}
118	\label{app:cross-temp}
119	\input{appendix_cross_temp}
120	\FloatBarrier
121	
122	\section{Feature Ablation}
123	\label{app:ablation-table}
124	\input{appendix_ablation}
125	
126	\begin{figure}[h]
127	\centering
128	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
129	\caption{LOGO binary F1 (gen-1 vs.\ gen-2+, 8-gen pooled) with inference cost. Ensembles achieve marginally higher F1 at 2.4$\times$ inference time and 3.2$\times$ GPU memory; individual detectors vary widely when repurposed for depth.}
130	\label{fig:baseline-ci}
131	\end{figure}
132	\FloatBarrier
133	
134	\input{appendix_feature_correlation}
135	\FloatBarrier
136	
137	\section{Cross-Family Reference Models}
138	\label{app:cross-ref}
139	\input{table4}
140	\FloatBarrier
141	
142	\input{appendix_seed_control}
143	\FloatBarrier
144	
145	\input{appendix_tost}
146	\FloatBarrier
147	
148	\section{DDR Partition Validation}
149	\label{app:ddr-validation}
150	\input{appendix_ddr_validation}
151	\FloatBarrier
152	
153	\section{Generator Subset Summary}
154	\label{app:gen-subsets-section}
155	\input{appendix_generator_subsets}
156	\FloatBarrier
157	
158	\input{appendix_qualitative_examples}
159	
160	\end{document}
161	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-19T06:13:08.498640+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1915 · 2026-05-19T06:13:09.000331+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit template"
  }
}
```

</details>

---


### Tool result

_source line 1916 · 2026-05-19T06:13:13.988503+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the inf
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5489
}
```

</details>

---


### Tool result

_source line 1917 · 2026-05-19T06:13:15.053121+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author instructions page limit template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on my search results, here's what I found about ACL Rolling Review 2026 submission guidelines:

## Key Submission Requirements

All long, short, and theme papers must follow the ACL Author Guidelines. Paper submissions must use the official ACL style template, which is available here.

## Template Information

There is an official Overleaf template that has a [review] setting that must be o
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6052
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-19T06:13:18.415022+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 1919 · 2026-05-19T06:13:18.465693+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1920 · 2026-05-19T06:13:22.787836+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, ethics/limitations section rules, ARR submission deadline, commitment deadline, and any other formatting requirements. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, ethics/limitations section rules, ARR submission deadline, commitment deadline, and any other formatting requirements. Be exhaustive."
  }
}
```

</details>

---


### Tool call

_source line 1921 · 2026-05-19T06:13:23.490439+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract all submission formatting requirements: page limits, template, anonymity rules, appendix rules, responsible NLP checklist, supplementary materials, and any other author requirements. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract all submission formatting requirements: page limits, template, anonymity rules, appendix rules, responsible NLP checklist, supplementary materials, and any other author requirements. Be exhaustive."
  }
}
```

</details>

---


### Tool result

_source line 1922 · 2026-05-19T06:13:28.365930+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Camera-ready versions:** Up to 9 pages (long) and 5 pages (short) to address reviewer feedback

## Template Requirements
Authors must follow "all of the ARR submission requirements" including paper submission templates available on the ARR website. Specific template details are referenced but not detailed in this document.

## Anonymity Rules
The review process maintains double-blind anonymity. "Reviewers will not see authors, nor will authors see reviewers." Reviews on ARR remain non-public, though authors may opt to make anonymized submissions publicly visible. Notably, "there is no anonymity period requirement" following ACL and ARR policies.

## Appendix and Supplementary Materials
Optional supplementary materials, appendices, software, and data are permitted per ARR guidelines.

## Required Sections
- **Limitations section:** Mandatory per ethics policy
- **Responsible NLP Research Checklist:** Required component of ethics compliance

## Key Deadlines
- **ARR Submission:** May 25, 2026
- **Reviewer Registration (all authors):** May 27, 2026
- **EMNLP Commitment:** August 2, 2026
- **Camera-ready Due:** September 20, 2026

## Additional Requirements
- Authors must declare intended conference commitment (EMNLP vs. AACL) at ARR submission
- No dual submissions permitted
- Author list cannot be modified during commitment phase
- All accepted papers require in-person or virtual presentation with registered presenting author

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 5578
}
```

</details>

---


### Tool result

_source line 1923 · 2026-05-19T06:13:32.432911+00:00_

# ACL Rolling Review: Submission Formatting Requirements

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited pages for references
- Unlimited space after conclusion for: limitations section (required) and optional ethical considerations section

**Short Papers:**
- Up to 4 pages of content
- Unlimited pages for references
- Unlimited space after conclusion for: limitations section (required) and optional ethical considerations section

Submissions exceeding length requirements will face desk rejection.

## Template and Style

Papers must use "the official ACL style template, which is available [here](https://github.com/acl-org/acl-style-files)." Authors must follow formatting guidelines at https://acl-org.github.io/ACLPUB/formatting.html and cannot modify style files or use templates from other conferences. Non-conforming submissions face rejection without review.

## Anonymity Requirements

- Author names and affiliations must be omitted
- Self-references revealing identity (e.g., "We previously showed") must be rewritten as third-person citations
- Papers cannot reference documents unavailable to reviewers
- Supplementary materials and repository links must be anonymized
- File-sharing services tracking downloads (Dropbox, Google Drive) are prohibited
- Violations result in desk rejection

## Limitations Section (Required)

All submissions must include a dedicated "Limitations" section at paper's end, before references. This section:
- Does not count toward page limits
- Cannot introduce new methods, analysis, or results
- Should only discuss constraints of presented work
- Omission results in desk rejection

## Responsible NLP Checklist

Authors must complete the checklist during submission. The document states: "incorrect, incomplete or misleading information in the checklist can result in desk rejection." Checklist metadata remains editable for 48 hours post-deadline.

## Supplementary Materials

**Appendices:**
- Placed after references in
…[truncated 1330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebFetch",
  "elapsed_ms": 8942
}
```

</details>

---


### Tool call

_source line 1924 · 2026-05-19T06:13:38.211795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1925 · 2026-05-19T06:13:39.215653+00:00_

1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	Text generated by large language models (LLMs) increasingly re-enters the web and seeds subsequent generation, producing recursive chains that progressively diverge from human-written text.
4	We study this phenomenon in base (pretrained) models and ask whether the drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Across eight base models from five families (0.6B--8B parameters), we identify a \emph{differential depth response} (DDR): features partition into drifting ($d{=}0.76$--$1.17$), intermediate, and near-stationary ($d < 0.10$) groups, consistent with recursive generation shifting the NLL location while distributional shape remains stable.
6	A 7-feature ensemble achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, generalizing across model families.
7	The depth signal degrades substantially under instruction tuning, restricting current applicability to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 1926 · 2026-05-19T06:13:39.215981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1927 · 2026-05-19T06:13:39.667393+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step.
5	Characterizing the structure of this evolution is fundamental to understanding how base language models transform distributions under iterative conditioning, with relevance to understanding model collapse dynamics \cite{curse_of_recursion, self_consuming_mad}.
6	Yet binary detection decisions \cite{fast_detectgpt,binoculars,ld_score,detectgpt} obscure this structure: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and term this \emph{depth profiling}.
9	No existing method provides a feature-level decomposition of depth signal in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR) with a three-way partition: when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, three \emph{drifting} features (reference-model mean entropy, type-token ratio, hapax ratio) shift monotonically (Cohen's $d > 0.75$), one \emph{intermediate} feature (entropy std) shows a non-monotonic level shift ($d{=}0.55$), and three \emph{near-stationary} features (entropy max, tail decay, entropy min) exhibit negligible depth effects ($d < 0.10$).
12	This is consistent with recursive generation shifting the NLL location while distributional shape remains stable under fixed sampling parameters.
13	While distributional drift under recursive generation is documented in the model collapse literature \cite{curse_of_rec
…[truncated 2085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1928 · 2026-05-19T06:13:40.219390+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1929 · 2026-05-19T06:13:40.671475+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1930 · 2026-05-19T06:13:40.772166+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1931 · 2026-05-19T06:13:40.925047+00:00_

# Review Issues — Updated after R25 action matrix execution
# Last updated: 2026-05-19 (post R25 fixes + instruct retrain experiment)

# ============ CRITICAL ============

- id: "R25-N1"
  summary: "DDR 新颖性不足以支撑 Main Conference，Findings 级别合适"
  category: method
  severity: critical
  status: acknowledged
  first_raised_round: 21
  last_seen_round: 25
  mentions:
    - {round: 25, reviewers: "R1,R2", note: "DDR 是已知特征的行为分类，非概念突破。3 drifting features 共享 92.3% variance。命名和 3/1/3 增加术语但未带来概念突破。作为 Findings 合适。"}
  action_items:
    - {round: 25, action: "接受 Findings 定位。通过 instruct retrain 实验增加 excitement（N2）。", assigned_to: "Director", status: "done"}
  resolution: "Findings 定位。instruct retrain 实验已完成，增加了新发现。"
  resolution_round: null

- id: "R25-N2"
  summary: "Base model 限制严重削弱 impact + instruct ρ 反转是 unrealized finding"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 25
  mentions:
    - {round: 25, reviewers: "R1,R2", note: "R1 指出 retrain on instruct data 可能恢复 F1。Web text 主要来自 instruct models。Instruct ρ 反转本身可成 contribution。"}
  action_items:
    - {round: 25, action: "Instruct retrain 实验完成。Within-model recovery +7-27pp。DDR silhouette 0.632→0.338。Cross-condition near chance。Discussion 和 Appendix 已更新。Contribution 3 已升级。", assigned_to: "Director", status: "done"}
  resolution: ""
  resolution_round: null

- id: "R25-N3"
  summary: "Cohen's d 阈值 post-hoc，gap-driven 非 principled"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 21
  last_seen_round: 25
  mentions:
    - {round: 25, reviewers: "R1,R2", note: "0.75 是看到数据后选的。k=3 时 entropy_min 自成一类，非 3/1/3。若 partition 变 F1 不变则削弱 DDR 必要性。"}
  action_items:
    - {round: 24, action: "阈值敏感性 [0.56,0.75] 已加入", assigned_to: "Director", status: "done"}
    - {round: 25, action: "§4.2 改为 continuous gradient + data-driven clustering 叙事，3/1/3 降格为 shorthand", assigned_to: "Director", status: "done"}
  resolution: ""
  resolution_round: null

# ===
…[truncated 7418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1932 · 2026-05-19T06:13:57.898705+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1933 · 2026-05-19T06:13:59.311232+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 26\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: p
…[truncated 3636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 1934 · 2026-05-19T06:13:59.311697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1935 · 2026-05-19T06:13:59.863873+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source te
…[truncated 8107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1936 · 2026-05-19T06:13:59.864302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1937 · 2026-05-19T06:13:59.914959+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.764 under 5-fold CV.\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation. Sample-level CV is used because each chain contains multiple generators, making generator-level held-out splits inapplicable.}
14	The higher cross-model F1 (vs.\ 0.694 single-generator LOGO) may reflect generator heterogeneity amplifying depth-correlated distributional shifts; generator identity information in mixed chains could partially confound the depth signal.
15	Leave-one-family-out (LOFO) evaluation yields binary F1\,=\,0.686, consistent with cross-family transfer.
16	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference model (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}).
17	Preliminary cross-domain evaluation su
…[truncated 12904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1938 · 2026-05-19T06:14:05.135909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1939 · 2026-05-19T06:14:05.637900+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The DDR tri-partition (3 drifting / 1 intermediate / 3 near-stationary) is consistent with a location/shape decomposition: under fixed temperature $\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration, while iterative conditioning shifts the input distribution's location as text becomes increasingly predictable to the reference model.
5	One informal conjecture is that temperature acts as a shape control parameter: at fixed $\tau$, the softmax normalizes token probabilities to a distribution whose entropy spread is bounded, so recursive conditioning can shift the mean but not escape the shape constraint imposed by $\tau$.
6	This would explain why DDR degrades at high temperature (the shape constraint loosens) and why near-stationary features track shape.
7	This interpretation is post-hoc and empirical; formal analysis of softmax output distribution dynamics under recursive conditioning remains an open problem.
8	DDR is an empirical decomposition capturing this dichotomy, not a claimed universal law of recursive generation.
9	DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.
10	Temperature and prompt-type ablations (\S\ref{sec:results-differential}) support this as a tendency rather than a guarantee: all four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp), and the signal varies across prompt types.
11	
12	Instruction tuning fundamentally alters the depth signal across all three tested families (OLMo, Qwen, Llama; Appendix~\ref{app:instruct}).
13	Entropy-mean $\rho$ reverses sign consistently ($+0.48$ for OLMo and Qwen, $+0.23$ for Llama; all base models ${\approx}{-}0.6$), and 6 of 7 features reverse direction for OLMo and Qwen, 3 of 7 for Llama.
14	Retraining the classifier on ins
…[truncated 2391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1940 · 2026-05-19T06:14:05.688482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1941 · 2026-05-19T06:14:06.039683+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers that combine handcrafted features with neural architectures \cite{ghostbuster,feat_aug_transformer,abburi_multifaceted,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{tang2024science}, \citet{wu_survey_2025}, and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent work moves beyond binary detection along several axes.
11	\citet{beyond_binary} classify text into four roles (human-only, LLM-polished, LLM-expanded, LLM-only) via involvement measurement, discriminating production \emph{modes} rather than recursive depth.
12	\citet{two_birds} jointly detect machine-generated text and attribute it to specific LLMs, and \citet{beyond_final_actor} distinguish dual creator-editor roles across four production modes.
13	Multi-generator attribution, including generator-level classification in SemEval 2024 Task 8 Subtask B \cite{semeval2024_task8} and the DeFactify dataset \cite{defactify_dataset}, discriminates among different \emph{sources}.
14	All these approaches classify text by its production process or authorship, while our depth classification tracks how many recursive generation steps a text has undergone, an orthogonal axis.
15	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each capture
…[truncated 5590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1942 · 2026-05-19T06:14:06.090224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1943 · 2026-05-19T06:14:06.643285+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and identified a differential depth response (DDR) tri-partition across eight base-model generators from five families.
5	A 7-feature ensemble exploiting this tri-partition achieves leak-free binary F1\,=\,0.694 (LOGO) and 0.764 (cross-model chains).
6	Current applicability is restricted to base models; instruction tuning and larger scales remain open.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1944 · 2026-05-19T06:14:06.693917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1945 · 2026-05-19T06:14:06.744420+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to 3-class LOGO F1\,=\,0.338 (vs.\ 0.763 base; this is classification F1, distinct from the clustering silhouette of the same value reported in \S\ref{sec:discussion}) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth profiling to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) and closed-source models remain untested; the consistent scale trend (Mistral-7B binary F1\,=\,0.633, lowest among all generators) suggests depth signal may weaken further at frontier scales, potentially approaching the detection floor.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type binary F1\,=\,0.781) compared to elaboration (0.730) and rewriting (0.737), with within-prompt-type paraphrastic c
…[truncated 3260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1946 · 2026-05-19T06:14:10.860380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1947 · 2026-05-19T06:14:12.717780+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 1948 · 2026-05-19T06:14:12.818620+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null; grep \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null; grep \"enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -5",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null; grep \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null; grep \"enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -5",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1949 · 2026-05-19T06:14:12.920282+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1950 · 2026-05-19T06:14:16.030147+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config section"
  }
}
```

</details>

---


### Tool result

_source line 1951 · 2026-05-19T06:14:16.080751+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1952 · 2026-05-19T06:15:00.770184+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: Long paper 8 页正文 + unlimited references/appendix\n- **模板**: Official ACL style template (acl-org/acl-style-files)，必须使用 `[review]` 选项\n- **匿名规则**: Double-blind（作者不可见审稿人，反之亦然）\n- **Limitations section**: 必须有，不计入页数限制\n- **Responsible NLP Checklist**: 必须填写，不完整可能 desk reject\n- **附录**: 放在 references 之后，不计入页数，必须 double-column 格式\n- **Ethics section**: 可选，不计入页数\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **方法论严谨性**：\n   - 7 个特征的选择是否有充分理论依据？是否存在 cherry-picking？\n   - DDR tri-partition（3/1/3 分类）的统计基础是否稳固？阈值选择是否 principled？\n   - Cohen's d、Glass's Δ、TOST 等统计检验的使用是否恰当？\n   - 异方差问题的处理是否充分？\n\n2. **实验设计**：\n   - LOGO 评估是否足以证明跨生成器泛化？gen-0 seed sharing 的影响是否充分控制？\n   - 8 个生成器（0.6B-8B）是否覆盖足够多样性？缺少大规模模型的影响？\n   - Temperature/prompt-type 消融是否充分？\n   - Baseline 比较是否公平？\n   - Generator subset 不一致（5/6/8-gen）是否造成混淆？\n\n3. **结果可信度**：\n   - Binary F1=0.694 是否足以支撑论文 claims？\n   - Cross-model F1 > single-gen F1 的解释是否合理？\n   - QLoRA F1=0.905 与 handcrafted F1=0.694 的差距说明什么？\n   - Instruct model 退化的分析深度是否足够？\n\n4. **统计报告**：\n   - CI 报告是否一致？是否有遗漏？\n   - 多重比较校正是否恰当？\n   - Effect size 报告是否完整？\n\n请按以下格式输出审稿报告：\n```\n## Summary\n[2-3句概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序]\n[每条标注严重级别：[Critical] / [Major] / [Minor]]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n\n## Detailed Comments\n[逐节详细意见]\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: Long paper 8 页正文 + unlimited references/appendix\n- **模板**: Official ACL style template (acl-org/acl-style-files)，必须使用 `[review]` 选项\n- **匿名规则**: Double-blind（作者不可见审稿人，反之亦然）\n- **Limitations section**: 必须有，不计入页数限制\n- **Responsible NLP Checklist**: 必须填写，不完整可能 desk reject\n- **附录**: 放在 references 之后，不计入页数，必须 double-column 格式\n- **Ethics section**: 可选，不计入页数\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **方法论严谨性**：\n   - 7 个特征的选择是否有充分理论依据？是否存在 cherry-picking？\n   - DDR tri-partition（3/1/3 分类）的统计基础是否稳固？阈值选择是否 principled？\n   - Cohen's d、Glass's Δ、TOST 等统计检验的使用是否恰当？\n   - 异方差问题的处理是否充分？\n\n2. **实验设计**：\n   - LOGO 评估是否足以证明跨生成器泛化？gen-0 seed sharing 的影响是否充分控制？\n   - 8 个生成器（0.6B-8B）是否覆盖足够多样性？缺少大规模模型的影响？\n   - Temperature/prompt-type 消融是否充分？\n   - Baseline 比较是否公平？\n   - Generator subset 不一致（5/6/8-gen）是否造成混淆？\n\n3. **结果可信度**：\n   - Binary F1=0.694 是否足以支撑论文 claims？\n   - Cross-model F1 > single-gen F1 的解释是否合理？\n   - QLoRA F1=0.905 与 handcrafted F1=0.694 的差距说明什么？\n   - Instruct model 退化的分析深度是否足够？\n\n4. **统计报告**：\n   - CI 报告是否一致？是否有遗漏？\n   - 多重比较校正是否恰当？\n   - Effect size 报告是否完整？\n\n请按以下格式输出审稿报告：\n```\n## Summary\n[2-3句概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序]\n[每条标注严重级别：[Critical] / [Major] / [Minor]]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n\n## Detailed Comments\n[逐节详细意见]\n```"
  }
}
````

</details>

---


### Tool result

_source line 1953 · 2026-05-19T06:15:20.487707+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19717
}
```

</details>

---


### Tool call

_source line 1954 · 2026-05-19T06:15:20.890290+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: Long paper 8 页正文 + unlimited references/appendix\n- **模板**: Official ACL style template (acl-org/acl-style-files)，必须使用 `[review]` 选项\n- **匿名规则**: Double-blind（作者不可见审稿人，反之亦然）\n- **Limitations section**: 必须有，不计入页数限制\n- **Responsible NLP Checklist**: 必须填写，不完整可能 desk reject\n- **附录**: 放在 references 之后，不计入页数，必须 double-column 格式\n- **Ethics section**: 可选，不计入页数\n- **2025年1月起更新**: 图表字体≥7pt，limitations/ethics 不计入页数，附录必须 double-column\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **新颖性评估**：\n   - \"Generation depth classification\" 作为任务定义的新颖性如何？\n   - DDR（Differential Depth Response）作为 empirical finding 的贡献程度？\n   - 与三篇并行工作（Broken Telephone, Markovian Chains, Attractor Cycles）的区分度？\n   - DDR 是否只是已知 location-shift 现象的重新命名？\n   - 对于 EMNLP Findings 是否有足够的贡献？\n\n2. **论文完整性**：\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 叙事主线是否一致？\n   - Contribution claims 是否都有对应实验支撑？\n   - Related Work 覆盖是否充分？是否有重要遗漏？\n   - Limitations 是否诚实全面？\n   - 附录内容是否在正文中被引用且融入叙事？\n\n3. **写作质量**（按 CLAUDE.md paper-writing-norms 严格审查）：\n   - 是否有 AI 写作痕迹？（em-dash/en-dash、-ing 短语结尾、过度分段、过渡词堆叠）\n   - 专有名词是否首次出现即定义？\n   - Abstract 是否在 150-250 words？四个必答问题是否回答？\n   - Introduction 五段结构是否完整？\n   - 每条 Contribution 是否有对应 section/table 支撑？\n\n4. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 模板是否正确（`\\usepackage[review]{acl}`）？\n   - 匿名化是否完整（作者 \"Anonymous\"，无自引泄露）？\n   - 行号是否开启？\n   - 参考文献格式是否一致？\n   - 图表字体是否 ≥ 7pt？\n   - 附录是否 double-column？\n\n5. **引用充足度**：\n   - 直接相关方法、baseline 论文、评测 benchmark 论文、理论基础是否都有引用？\n   - 引用数量是否与 EMNLP 录用论文量级一致？\n\n请按以下格式输出审稿报告：\n```\n## Summary\n[2-3句概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序]\n[每条标注严重级别：[Critical] / [Major] / [Minor]]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n\n## Detailed Comments\n[逐节详细意见]\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- **路径**: `projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **目标 Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n\n### Venue 格式要求（实时搜索确认）\n- **页数限制**: Long paper 8 页正文 + unlimited references/appendix\n- **模板**: Official ACL style template (acl-org/acl-style-files)，必须使用 `[review]` 选项\n- **匿名规则**: Double-blind（作者不可见审稿人，反之亦然）\n- **Limitations section**: 必须有，不计入页数限制\n- **Responsible NLP Checklist**: 必须填写，不完整可能 desk reject\n- **附录**: 放在 references 之后，不计入页数，必须 double-column 格式\n- **Ethics section**: 可选，不计入页数\n- **2025年1月起更新**: 图表字体≥7pt，limitations/ethics 不计入页数，附录必须 double-column\n\n### EMNLP 2026 评分标准（ARR 统一审稿）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **新颖性评估**：\n   - \"Generation depth classification\" 作为任务定义的新颖性如何？\n   - DDR（Differential Depth Response）作为 empirical finding 的贡献程度？\n   - 与三篇并行工作（Broken Telephone, Markovian Chains, Attractor Cycles）的区分度？\n   - DDR 是否只是已知 location-shift 现象的重新命名？\n   - 对于 EMNLP Findings 是否有足够的贡献？\n\n2. **论文完整性**：\n   - Abstract → Introduction → Method → Results → Discussion → Conclusion 叙事主线是否一致？\n   - Contribution claims 是否都有对应实验支撑？\n   - Related Work 覆盖是否充分？是否有重要遗漏？\n   - Limitations 是否诚实全面？\n   - 附录内容是否在正文中被引用且融入叙事？\n\n3. **写作质量**（按 CLAUDE.md paper-writing-norms 严格审查）：\n   - 是否有 AI 写作痕迹？（em-dash/en-dash、-ing 短语结尾、过度分段、过渡词堆叠）\n   - 专有名词是否首次出现即定义？\n   - Abstract 是否在 150-250 words？四个必答问题是否回答？\n   - Introduction 五段结构是否完整？\n   - 每条 Contribution 是否有对应 section/table 支撑？\n\n4. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 模板是否正确（`\\usepackage[review]{acl}`）？\n   - 匿名化是否完整（作者 \"Anonymous\"，无自引泄露）？\n   - 行号是否开启？\n   - 参考文献格式是否一致？\n   - 图表字体是否 ≥ 7pt？\n   - 附录是否 double-column？\n\n5. **引用充足度**：\n   - 直接相关方法、baseline 论文、评测 benchmark 论文、理论基础是否都有引用？\n   - 引用数量是否与 EMNLP 录用论文量级一致？\n\n请按以下格式输出审稿报告：\n```\n## Summary\n[2-3句概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序]\n[每条标注严重级别：[Critical] / [Major] / [Minor]]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n\n## Detailed Comments\n[逐节详细意见]\n```"
  }
}
````

</details>

---


### Tool result

_source line 1955 · 2026-05-19T06:15:22.527783+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1637
}
```

</details>

---


### Assistant

_source line 1956 · 2026-05-19T06:15:29.044256+00:00_

Round 1 审稿任务已分配：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验设计 + 统计分析 | 已派发 |
| R2 | 新颖性 + 完整性 + 写作质量 + 格式合规 | 已派发 |

**论文概况**：
- 标题：Depth Profiling — 递归生成深度分类
- 核心发现：DDR tri-partition（drifting/intermediate/near-stationary）
- 主要指标：leak-free binary F1=0.694（8-gen LOGO）
- 27 页（正文+附录），8 generators × 5 families，56 个实验
- 外部审稿：未配置，跳过

等待两位 Reviewer 返回初审报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 174

## Round 174

2 recorded events


### User

_source line 1957 · 2026-05-19T06:24:07.624398+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 (ACL Rolling Review)
**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + 格式合规

---

## Summary

本文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+（而非二分类），并在 8 个 base model 上发现了 differential depth response (DDR) 三分现象（drifting/intermediate/near-stationary）。7-feature ensemble 在 LOGO 评估下实现 binary F1=0.694。论文实验设计严谨、统计方法充分、负面结果（downstream utility、instruction tuning degradation）诚实报告。但新颖性在三篇并行工作的背景下显得增量较小，且方法仅适用于 base model，实用价值受限。

---

## Strengths

**S1** [实验设计严谨] 控制变量全面：seed sharing control（independent-seed F1=0.680, Appendix seed-control）、length confound control（length-matched F1=0.724, Appendix A）、cross-reference model validation（spread ≤0.013, §4.2）、LOGO + LOFO 双层 cross-validation。统计方法涵盖 bootstrap CI、McNemar test、KS test、Cohen's d、Glass's Δ、Cliff's δ、TOST equivalence testing，远超同类论文水平。

**S2** [诚实报告负面结果] Downstream utility 实验（Appendix downstream）明确显示 depth-aware curation 不优于 random subsampling；instruction tuning 使 DDR 结构显著退化（silhouette 0.632→0.338, §5）；高温下方法性能大幅下降（-9.3 to -26.0 pp at t=0.9）。这种透明度增强了论文可信度。

**S3** [DDR 分解的分析深度] 从多个角度验证 DDR 三分结构：数据驱动 k-means（silhouette=0.632）、domain-informed 3/1/3 划分、per-generator TOST equivalence testing、holdout generator validation、PCA（92.3% variance explained by PC1 of drifting features）。分析层次从 aggregate 到 per-generator，从 omnibus 到 heteroscedasticity-robust metrics，形成了较完整的证据链。

**S4** [叙事主线一致] Abstract→Introduction→Method→Results→Discussion→Conclusion 形成连贯的故事线：问题（binary detection 不够）→洞察（distributional drift 有结构）→方法（7 features + DDR 分解）→验证（LOGO, controls）→边界条件（temperature, instruction tuning）。每个 contribution claim 都有对应的实验支撑。

**S5** [引用覆盖充分] 71 篇引用，涵盖 detection methods（DetectGPT, Binoculars, FastDetectGPT 等）、model collapse（Shumailov et al., Alemohammad et al.）、三篇并行工作（Broken Telephone, Markovian Chains, Attractor Cycles）、stylometry 基础、ordinal classification 理论。引用验证：57/71 通过 OpenAlex 验证，无虚假引用。

**S6** [写作质量高] 无 AI 写作痕迹（无 em-dash、无 -ing phrase 句尾、无过渡词堆叠），段落结构自然，技术表述精确。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [Critical] 缺少 Responsible NLP Research Checklist
- 具体位置：全文
- 问题：ARR 投稿要求必须包含 Responsible NLP Research Checklist，当前论文中未找到任何 checklist 相关内容。grep "checklist" 和 "Responsible" 在所有 .tex 文件中均无匹配。
- 为什么影响接收：这是 ARR desk reject 的充分条件。根据 ACL 2025+ 规定，checklist 不完整可直接被拒。
- 建议修改方向：立即添加 Responsible NLP Research Checklist，逐项认真填写（不要全写 N/A）。

**N2** [Critical] 正文页数可能超过 8 页限制
- 具体位置：PDF pages 1-9
- 问题：从 PDF 渲染结果看，main body（Abstract 至 §6 Conclusion）延伸到第 9 页左栏约 75% 处。排除 Limitations 和 Ethics 后，主体内容约 8.3-8.4 页，超出 EMNLP long paper 8 页限制约 0.3-0.4 页。
- 为什么影响接收：超页数可能导致 desk reject 或审稿人负面印象。
- 建议修改方向：压缩 Discussion 或 Results 部分约 0.5 页。Discussion §5 中 informal conjecture about temperature as shape control（第 1-7 行）可移至 appendix；Results §4.2 中多处 redundant quantification（同时报告 ρ、d、KS、Glass's Δ、Cliff's δ）可精简。

**N3** [Critical] 新颖性增量在并行工作背景下较有限
- 具体位置：§2.2 (Related Work), §1 (Introduction Contribution 2-3)
- 问题：三篇并行工作（Broken Telephone [ACL 2025], Markovian Chains [arXiv 2026], Attractor Cycles [ACL 2025]）已经独立建立了"iterative generation 约有 ~3 个可区分的深度类别"这一核心发现。论文声称的三点区别（non-paraphrastic chains, handcrafted features enabling DDR, "what converges vs. that convergence occurs"）中：
  - (i) Non-paraphrastic continuation chains 确实是不同的 setting，但用简单 prompt "Continue the following text" 产生的 chains 比 paraphrastic chains 更容易区分（作者自己在 Limitations 中承认 paraphrastic chains F1=0.671 vs. continuation 0.749），这降低了技术贡献。
  - (ii) DDR 三分结构（location shift + shape stability）在固定 temperature 和 nucleus sampling 下是理论可预期的——softmax temperature 控制 shape，iterative conditioning 只能 shift location。论文自己在 §5 Discussion 中承认这是 "post-hoc and empirical" 且 "informal conjecture"。
  - (iii) Markovian Chains (Geng et al., 2026) 已经提供了 Markovian attractor dynamics 的形式化分析，本文的 DDR 作为 empirical 补充，增量较小。
- 为什么影响接收：对于主会议（Overall 4.0），需要 clear novelty contribution。当前定位更适合 Findings。
- 建议修改方向：（a）更清晰地量化 DDR 相对于并行工作的 unique insight（不仅是定性区分）；（b）考虑在 paraphrastic chains 上也验证 DDR 三分结构，以展示 DDR 作为分析框架的通用性；（c）强化 location/shape 分解的理论解释（当前仅为 informal conjecture）。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] DDR 与已知 distributional shift 现象的本质区别不够清晰
- 具体位置：§4.2, §5
- 问题：Model collapse 文献已经记录了 recursive generation 下的 distributional drift（vocabulary diversity 下降、perplexity 压缩）。DDR 的 drifting features（entropy mean, TTR, hapax ratio）本质上就是这些已知现象的具体量化。论文在 §5 和 §2.2 试图区分（"inference-chain drift is fully reversible" vs. training-loop drift），但 drifting/non-drifting partition 本身的科学贡献需要更有力的论证——这是 repackaging 还是 genuine new insight？
- 建议：在 Discussion 中加入更系统的对比表格，列出 DDR 每个组件与已有文献发现的精确对应/区别。

**W2** [Major] Binary F1=0.694 的实用意义有限
- 具体位置：Table 1 (§4.1), Table 2 (§4.3)
- 问题：LOGO binary F1=0.694 意味着每三次预测中约有一次错误（gen-1 vs. gen-2+）。加上 base-model-only 的限制（真实世界 LLM 文本几乎全部来自 instruction-tuned models）和 negative downstream utility result，实际部署场景不明确。论文虽然 framing 为 empirical contribution 而非 practical tool，但 Introduction 第 1 段的动机（"understanding model collapse dynamics"）与实际结果之间有 gap。
- 建议：（a）更明确地将论文定位为 analytical/diagnostic tool 而非 deployment-ready method；（b）在 Conclusion 中讨论 DDR 分析框架如何指导未来 detection 方法设计的 concrete paths。

**W3** [Major] Abstract 低于 150 words（约 132 words），且 "why important" 缺失
- 具体位置：abstract.tex
- 问题：Abstract 约 132 words，低于 ACL/EMNLP 推荐的 150-250 words 范围。更重要的是，Abstract 缺少对 "为什么 depth classification 重要" 的明确阐述——直接从 "text diverges from human-written text" 跳到 "we study this phenomenon"，缺少动机桥梁。四个必答问题中 "为什么重要" 回答不充分。
- 建议：增加 1-2 句话说明 depth classification 对 data provenance / training data curation / detection granularity 的具体意义。

**W4** [Major] NLL 缩写在 Abstract 中未定义
- 具体位置：abstract.tex 第 5 行
- 问题："consistent with recursive generation shifting the NLL location while distributional shape remains stable" —— NLL（negative log-likelihood）在 Abstract 中首次出现但未展开定义。Abstract 应为独立阅读单元。
- 建议：改为 "negative log-likelihood (NLL) location" 或直接用 "perplexity location"。

**W5** [Major] Cross-model chains F1 (0.764) 的 generator identity confound 需更严格处理
- 具体位置：§4.1 第 2 段
- 问题：论文承认 "generator identity information in mixed chains could partially confound the depth signal"，但仍将 0.764 作为重要结果报告（Abstract、Introduction、Conclusion 均引用）。如果 generator heterogeneity 放大了表面差异，这个 F1 可能高估了真实 depth signal。论文仅用 footnote 解释 "Sample-level CV is used because each chain contains multiple generators"，但这恰恰意味着 CV 无法控制 generator identity leakage。
- 建议：（a）在 cross-model 实验中加入 generator-identity ablation（例如，控制每个 depth 使用相同 generator 集合）；（b）或降低 cross-model F1 在叙事中的权重，以 LOGO single-generator F1 (0.694) 为主要 claim。

**W6** [Minor] Introduction 开头过于抽象
- 具体位置：introduction.tex 第 4 行
- 问题："When LLM outputs are fed back as inputs to subsequent generation, the resulting recursive chains form a dynamical system whose distributional properties evolve with each step." 这一开头虽然准确，但不够具体和引人注目。按照 CLAUDE.md paper-writing-norms §3.3，禁止泛泛介绍。
- 建议：从一个更具体的场景或数据切入（例如，web-scale data 中 LLM-generated text 的比例增长及其对 downstream training 的影响）。

**W7** [Minor] Generator subset 不一致增加阅读负担
- 具体位置：main.tex 第 41-43 行（appendix note），§4.1 footnote 1，§4.4 (Evaluation Protocol) 第 69 行
- 问题：论文使用了三个不同的 generator subset（5-gen, 6-gen, 8-gen），虽然在 main.tex appendix 开头和 Appendix generator-subsets 中有说明，但正文中不同实验使用不同 subset，cross-model chains 用 5-gen、appendix 用 6-gen、主实验用 8-gen，增加了理解和比较的难度。
- 建议：在 Method §3.4 中用一个简表清晰列出哪些实验使用哪个 subset 及原因。

---

## Questions

**Q1** DDR 的 drifting/non-drifting partition 是否在 paraphrastic chains 上也成立？如果不成立，DDR 的通用性如何？Related Work §2.2 中声称的 "all three study paraphrastic chains" 区分只有在 DDR 同样适用于 paraphrastic setting 时才有完整说服力。

**Q2** 论文在 §5 Discussion 中提出 "temperature acts as a shape control parameter" 的 informal conjecture。是否可以通过比较不同 temperature 下 near-stationary features 的方差变化来提供初步验证？如果 shape features 在高温下开始 drift，这将直接支持该假说。

**Q3** QLoRA end-to-end classifier（3-class F1=0.905）显著优于 7-feature ensemble（0.789）。是否在 instruction-tuned models 上也测试了 QLoRA？如果 QLoRA 能在 instruct models 上保持高 F1，这将大幅改变论文的实用价值主张。

**Q4** 论文使用单一 prompt template ("Continue the following text: {text}")。在实际 web 生态中，recursive chains 不太可能使用完全相同的 prompt。Cross-prompt-type transfer（LOPTO F1=0.753）使用了哪些 prompt types？是否包含了无 explicit prompt 的 unconditional generation？

**Q5** Appendix downstream 实验仅用 n=3 seeds，论文自己承认 "preliminary observation"。是否计划扩展该实验？如果 depth-aware curation 确实无效，这是否削弱了 depth classification 作为 data provenance signal 的实际价值？

---

## Missing References

1. **Guo et al. (2024)** "Generative AI for Synthetic Data Generation: Methods, Challenges and the Future" — 关于 synthetic data 在 web 上比例增长的综述，与论文动机相关。
2. **Li et al. (2024)** "Synthetic Data (Almost) from Scratch: Generalized Instruction Tuning for Language Models" — 与 instruction-tuned model 下的 synthetic data 质量直接相关。
3. **缺少 ordinal classification 在 NLP 的更多应用引用** — 论文引用了 sentiment analysis 和 essay scoring，但 ordinal regression 在 NLP 中还有更多应用（如 readability assessment、stance detection），可以加强 §2 Related Work 中 ordinal classification 的 positioning。

---

## Overall Assessment

**Overall**: 3.0 (Findings)
**Soundness**: 4/5
**Excitement**: 2.5/5
**Confidence**: 4/5

**一句话总结**: 实验设计和统计分析水准很高，但新颖性在三篇并行工作背景下显得增量较小，base-model-only 限制和 moderate F1 使实用价值受限，适合 Findings 而非主会议。

**评分理由**:
- **Soundness 4/5**: 实验设计严谨，控制变量充分，统计方法规范，负面结果诚实报告。扣分原因：cross-model chain confound 未充分控制；page count 可能超限。
- **Excitement 2.5/5**: DDR 三分结构是有趣的 empirical finding，但（a）三篇并行工作已经独立发现 ~3-class ceiling；（b）location/shape 分解在固定 temperature 下是可预期的；（c）practical utility 受限于 base-model-only restriction 和 moderate F1。
- **Confidence 4/5**: 审阅了全文正文、所有 appendix（16 个附录）、references.bib（71 条引用验证）、PDF 渲染效果，并搜索了 ARR reviewer guidelines。对格式合规和写作质量的判断有较高置信度。

---

## Detailed Comments

### Abstract
- 约 132 words，低于推荐范围（150-250）。
- NLL 在 abstract 中未展开定义。
- "Why important" 环节缺失——从 "diverge from human-written text" 直接跳到 "we study"。
- 最后一句关于 instruction tuning 的限制是好的（诚实），但可以更简洁地为主结论留更多空间。

### Introduction
- 五段结构基本完整，但第 1 段的动机框架偏学术化（"dynamical system"），缺乏具体场景。
- Contribution 3（boundary conditions）的表述过于技术密集，普通 reviewer 可能难以一次理解 "$t \in [0.5, 0.7]$" 和 "silhouette: 0.632→0.338" 的含义。
- 每条 Contribution 都有对应 section 支撑 ✓。

### Related Work
- 结构清晰，分四个子节覆盖主要方向 ✓。
- 与三篇并行工作的对比最为关键（§2.2 最后一段），论文的三点区分论述到位但未完全 convincing（见 N3）。
- §2.1 第一段引用密度高，但分析性 positioning 到位（不是简单堆砌）✓。
- §2.4 Data Quality and Provenance 与主题关联较弱，可以精简以节省页面空间。

### Method
- 任务定义清晰，形式化恰当 ✓。
- Feature extraction 的 motivation 交代充分（两个互补视角）✓。
- §3.3 中 "entropy" 作为 NLL 的简称在此处定义（"We use 'entropy' as shorthand for token-level NLL"），但 Abstract 中已使用 NLL 且未定义。
- Evaluation protocol 详细但 generator subset 的多样性增加复杂度（见 W7）。

### Results
- 结果报告清晰，primary metric（binary F1）和 inflated metric（3-class F1）的区分处理得当 ✓。
- §4.2 DDR 分析是论文的核心贡献，分析深入但存在 over-quantification 风险——同时报告 ρ, d, KS, Glass's Δ, Cliff's δ, CV shift, TOST 等 7+ 种统计量，重复验证同一结论，可能导致信息过载。
- Table 2 baseline comparison 定位准确（"contextualize rather than claim competitive advantage"）✓。

### Discussion
- Location/shape conjecture（§5 第 5-7 行）有趣但过于 speculative——占用宝贵的正文空间且自我标注为 "informal conjecture"。
- Instruction tuning 分析（§5 第 12-17 行）是重要的 boundary condition，报告充分。
- Downstream utility 讨论（§5 第 20-21 行）过于简短，考虑到这是一个 key practical question。

### Limitations
- 极其全面（覆盖 base-model, scale, prompt-type, cross-domain, temperature, tokenizer, feature space, granularity）✓。这是论文的一个显著优势。

### Ethics
- 内容恰当，涵盖 privacy implications、dual use、licenses、compute budget、software versions ✓。

### Format
- `\usepackage[review]{acl}` ✓
- `\author{Anonymous}` ✓
- `\linenumbers` ✓
- References 格式一致 ✓（无 orphan, 无 missing）
- **缺少 Responsible NLP Research Checklist** ✗（见 N1）
- **页数可能超限** ~8.3-8.4 pages（见 N2）
- Figure 1 字体可读，估计 ≥7pt ✓
- 附录 double-column ✓
- Em-dash: 仅出现在 LaTeX 注释中，正文无 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1958 · 2026-05-19T06:24:15.792704+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 175

## Round 175

2 recorded events


### User

_source line 1959 · 2026-05-19T06:24:18.633567+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：Overall 评分 **3.0 (Findings)**。主要发现：

1. **N1 [Critical]** 缺少 Responsible NLP Research Checklist，可能导致 desk reject
2. **N2 [Critical]** 正文约 8.3-8.4 页，可能超出 8 页限制
3. **N3 [Critical]** 三篇并行工作（Broken Telephone, Markovian Chains, Attractor Cycles）已独立发现 ~3-class ceiling，DDR 新颖性增量有限
4. **W1-W5** 包括 DDR 与已知现象的区分不够清晰、binary F1=0.694 实用性有限、Abstract 偏短且缺 "why important"、NLL 未在 Abstract 定义、cross-model chain confound

优点方面，论文实验设计严谨（S1）、诚实报告负面结果（S2）、DDR 分析深入（S3）、叙事主线一致（S4）、引用充分（S5）、写作质量高且无 AI 痕迹（S6）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1960 · 2026-05-19T06:24:28.798633+00:00_

Reviewer 2 报告已收到，记录完毕。

**当前状态**：等待 Reviewer 1（方法严谨性 + 实验设计 + 统计分析）返回初审报告。Reviewer 1 返回后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 176

## Round 176

6 recorded events


### User

_source line 1961 · 2026-05-19T06:26:31.613292+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告 — Round 1

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## Summary

本文提出 "depth profiling"，将 LLM 生成文本的来源判别从二元分类（human vs. machine）扩展为按递归生成深度分类（gen-0 / gen-1 / gen-2+）。作者使用 8 个 base model（0.6B–8B，5 个模型家族），提取 7 个手工特征（3 个 reference-model 特征 + 2 个 surface 特征 + 2 个互补特征），提出 differential depth response (DDR) 三分框架（drifting / intermediate / near-stationary），并用 XGBoost 分类器在 LOGO 评估下达到 3-class macro-F1 = 0.762、binary F1 = 0.694。附录中提供了大量消融实验。QLoRA 端到端分类器达到 F1 = 0.905。

论文问题定义新颖，统计分析较为严谨，附录充实。但核心性能有限、模型规模受限、DDR 阈值缺乏理论基础、跨模型结果存在混淆变量，这些问题影响了整体贡献的说服力。

---

## Strengths

**S1. 问题定义新颖且有实际意义。** 将生成文本检测从二元推广到多级深度分类是一个自然且有价值的扩展。论文在 §1 中清晰阐述了递归生成链的 distributional drift 现象，动机明确，与 model collapse 文献（Shumailov et al., 2024; Alemohammad et al., 2024）建立了有意义的联系。

**S2. 统计方法论严谨。** 在 NLP 论文中达到了较高的统计标准：使用 Bonferroni 校正处理多重比较（§4.2, 21 个分布比较 + 4 个 baseline 比较）；同时报告 Cohen's d、Glass's Δ（处理异方差）和 Cliff's δ（非参数）（Appendix V, Table 28）；TOST 等价性检验在多个 ε 阈值下验证 near-stationary 特征（Appendix U）；bootstrap CI 贯穿全文。

**S3. 消融实验全面。** 附录覆盖了大量潜在混淆变量：长度控制（Appendix B）、种子独立性验证（Appendix T）、温度敏感性（Appendix P）、跨领域泛化（Appendix J）、LOFO 特征消融（Appendix F）、UMAP 可视化（Appendix O）、随机词替换鲁棒性（Appendix I）、LLM 模拟编辑（Appendix I 末尾）。这种覆盖度在同类工作中较为少见。

**S4. DDR 框架具有解释价值。** 将 7 个特征按深度响应模式分为三类（drifting / intermediate / near-stationary）提供了直观的信号分解，有助于理解递归生成的分布漂移机制。Figure 1 和 Figure 5（Appendix O）的可视化有效支撑了叙事。

**S5. 诚实报告局限性。** 论文明确承认了 base model 限制、instruct model 退化（§5）、gen-0 种子共享问题，且将 binary F1（不受种子泄漏影响）作为主要指标。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1 [Critical] DDR 三分阈值缺乏理论基础，entropy mean 恰好位于边界。**
- 具体位置：§4.2 (p6), §1 (p1)
- 问题：DDR 分区使用 |ρ| > 0.60 定义 drifting、|ρ| < 0.10 定义 near-stationary，但这两个阈值的选择没有理论或数据驱动的正式依据。论文在 §4.2 提到 k-means 聚类验证了 drifting/non-drifting 二分（k=2, silhouette=0.632），但从二分进一步细化到 3/1/3 的过程依赖 "domain-informed criteria"，具体标准不够透明。更关键的是，entropy mean 的 ρ = 0.60 恰好处于 drifting 阈值边界上（§4.2: "entropy mean ρ = 0.60"），微小的阈值变动就会改变分区结果。如果 drifting 阈值设为 0.61，entropy mean 就变成 intermediate，DDR 从 3/1/3 变为 2/2/3。
- 为什么影响接收：DDR 是论文的核心概念贡献（Contribution 2），如果分区边界不稳健，整个框架的可信度受损。
- 建议修改方向：(1) 进行阈值敏感性分析，展示在 ρ 阈值 ±0.05 范围内分区和下游分类结果是否稳定；(2) 用更 principled 的方法（如 gap statistic、信息论准则）确定分区边界；(3) 至少承认 entropy mean 的边界状态并讨论其影响。

**W2 [Critical] Cross-model F1 > single-gen F1 的比较存在根本性混淆变量。**
- 具体位置：§4.3 (p5-6), Abstract (p1)
- 问题：论文报告 cross-model binary F1 = 0.764 高于 single-gen LOGO binary F1 = 0.694，并将此作为泛化能力的证据。但 cross-model 链的每一步使用不同生成器，引入了模型切换（model-switching）效应，这本身就是一个额外的分布漂移来源。分类器检测到的可能不是纯粹的 "depth signal"，而是 "depth + model-switching" 的混合信号。论文对此的解释（"generator heterogeneity amplifying depth-correlated distributional shifts"，§4.3）本质上是在承认这一混淆，但没有控制或分离两种效应。此外，cross-model 使用 5-generator subset 而 LOGO 使用 8 generators，实验条件不同使比较更不严谨。
- 为什么影响接收：这影响了论文对 "depth signal" 本质的核心 claim。如果 cross-model 的高 F1 部分来自 model-switching artifact，那么论文关于 "递归生成深度产生可检测信号" 的主张被弱化。
- 建议修改方向：(1) 构造 "same-depth, different-generator" 的对照实验，分离 depth 和 model-switching 效应；(2) 如果无法分离，将 cross-model 结果的解释降级，明确承认 model-switching 混淆；(3) 统一 generator subset 以消除子集差异的影响。

**W3 [Major] Binary F1 = 0.694 支撑力有限，QLoRA 差距（F1 = 0.905）暴露了特征覆盖不足。**
- 具体位置：§4.1 (p5), Appendix E (p16), Abstract (p1)
- 问题：论文的核心分类任务（gen-1 vs. gen-2+）binary F1 = 0.694。虽然高于随机和多数基线，但作为一个实用工具仍然不足。更重要的是，QLoRA 端到端分类器在相同 LOGO 设置下达到 F1 = 0.905，比手工特征高出 21pp。Appendix E 分析认为 "raw token embeddings contain depth signal beyond what summary statistics capture"，这直接表明 7 个手工特征遗漏了大量深度信息。论文将手工方法的优势定位为 "interpretability" 和 "computational efficiency"（§5），但没有给出 interpretability 带来的具体分析洞见来证明 21pp 的代价是值得的。
- 为什么影响接收：如果手工特征只能捕获约 77% 的可达性能（0.694/0.905），作为论文的 primary contribution 说服力不足。
- 建议修改方向：(1) 补充手工特征提供的、QLoRA 无法提供的具体解释性洞见案例；(2) 分析 QLoRA 和手工方法的错误重叠度，展示两者是否互补；(3) 考虑增加特征（如 n-gram divergence、perplexity ratio 等）缩小差距。

### Should-Fix 问题（影响评分但不一票否决）

**W4 [Major] 模型规模限于 0.6B–8B，排除了真实场景。**
- 具体位置：§3.2 (p4), Limitations (p9)
- 问题：所有 8 个生成器均为小型 base model（最大 8B）。现实中的 LLM 生成文本来自更大的 instruct model（70B+, GPT-4 等）。论文将此定位为 "deliberate design choice"（base models 隔离生成机制），但 §5 的 instruct model 分析（p8-9）显示 F1 显著退化，3-class F1 降至 0.338（OLMo-2-1B instruct）。这意味着 DDR 框架和分类方法在实际应用场景中可能不适用。
- 建议：(1) 至少在 1-2 个更大的 base model（如 Llama-3-8B 以上、Qwen-14B）上验证；(2) 深化 instruct model 退化的分析，识别退化是来自 RLHF 对齐还是 SFT 特征压缩。

**W5 [Major] Generator subset 不一致（5/6/8-gen）增加了解释复杂度。**
- 具体位置：Table 1 (p5-6), Table 7 (p17), §4.3 (p6), 各附录
- 问题：不同实验使用不同的 generator 子集：Table 1 主结果用 8-gen，LOFO 消融（Table 7）用 6-gen，cross-model 用 5-gen subset，部分附录实验用 4-gen。虽然每个表格都标注了子集，但跨实验的直接比较变得困难。例如，无法直接比较 6-gen LOFO 的特征消融结果与 8-gen 主表的分类性能。
- 建议：(1) 在主结果中统一使用 8-gen，至少展示 8-gen LOFO 的特征消融结果；(2) 如果子集差异有充分理由（如某些 generator 数据不可用），在一个统一的表格中总结不同子集的影响。

**W6 [Major] Gen-0 种子共享导致 3-class LOGO 评估存在数据泄漏。**
- 具体位置：§3.2 (p4), §3.4 (p5)
- 问题：所有 8 个 generator 共享相同的 ~1,000 个 Wikipedia 种子段落作为 gen-0 数据（§3.2: "The same pool of seed passages serves as gen-0 for all generators"）。在 LOGO 评估中，当某个 generator 被留作测试时，其 gen-0 样本与训练集中其他 generator 的 gen-0 完全相同。这导致 gen-0 分类在 3-class 评估中被人为简化。虽然论文将 binary F1（排除 gen-0）作为主要指标，且 Appendix T 的独立种子实验（Table 23）部分验证了无泄漏情况下的性能（F1 ≈ 0.680），但 3-class F1 = 0.762 仍被突出报告（Abstract、Table 1），可能误导读者。
- 建议：(1) 在报告 3-class 结果时明确注明 gen-0 泄漏风险；(2) 补充一个 gen-0 完全独立的 3-class LOGO 结果。

**W7 [Minor] TOST 等价性检验的等价边界（ε = 0.20）选择缺乏领域特定理由。**
- 具体位置：Appendix U (p26-27)
- 问题：TOST 使用 Cohen's conventional small effect size ε = 0.20 作为等价边界。虽然论文在 Table 26 报告了多个 ε 值（0.15, 0.20, 0.25）的结果，但没有解释为什么 ε = 0.20 在 NLP 文本特征的上下文中是适当的等价标准。Cohen's conventions 是为行为科学设计的，直接移植到文本分布特征可能不恰当。
- 建议：讨论 ε = 0.20 在本研究语境下的含义（对应多大的特征值差异），或基于 pilot data 的效应量分布确定更 principled 的边界。

**W8 [Minor] Instruct model 退化分析深度不足。**
- 具体位置：§5 (p8-9)
- 问题：§5 发现 instruct tuning 将 binary F1 降至 ~0.2–0.5（取决于模型），并推测 "RLHF disrupts the clean location/shape decomposition that underlies DDR"。但分析停留在推测层面，没有进一步验证：是 RLHF 的 reward model 压缩了特征空间，还是 SFT 阶段的格式化输出已经改变了分布？这对评估 DDR 框架的通用性至关重要。
- 建议：如果可以获取 SFT-only 的中间 checkpoint（如某些开源模型提供），对比 SFT vs. RLHF 各阶段的退化程度。

---

## Questions

**Q1.** 如果 DDR drifting 阈值从 |ρ| > 0.60 调整为 |ρ| > 0.55 或 |ρ| > 0.65，分区结果和下游分类性能会如何变化？是否做过敏感性分析？

**Q2.** Cross-model 链中，F1 提升相对于 single-gen 有多少可归因于 depth effect、多少归因于 model-switching artifact？是否可以构造 "fixed-depth, cross-generator" 的对照来分离两种效应？

**Q3.** LOFO 分析（Table 7）中，entropy_max 被分类为 near-stationary（|ρ| = 0.061），但移除它导致最大的 F1 下降（-3.70 pp）。如何解释 near-stationary 特征对分类的高贡献？是否因为 entropy_max 的分布形状（而非位置）在不同深度间有差异？

**Q4.** 7 个特征之间 TTR 和 hapax ratio 高度相关（r = 0.97，Table 21）。是否考虑过移除其中一个或使用 PCA 降维？保留两个近乎完美相关的特征对 XGBoost 是否有实际增益？

**Q5.** Appendix M（Downstream Utility, Table 17）的 perplexity 分析仅用了 OLMo-2-0425-1B。这个结论（depth-aware selection 改善下游 perplexity）是否在其他 reference model 上也成立？

**Q6.** 论文多处提到 "reference model" 固定为 Pythia-410M，且 Appendix S 验证了跨家族一致性（"spread in LOGO F1 is 0.013"）。但 cross-domain 评估（Appendix J, Table 14）显示 Academic domain F1 降至 0.628，这是否表明 reference model 的 domain 校准是必要的？

---

## Missing References

1. **Bao et al. (2024), "Fast-DetectGPT"** — 论文虽已引用并作为 baseline（Table 2），但在 Related Work (§2.1) 中未讨论其与本方法的关系（都使用 probability curvature 的变体）。

2. **Zhu et al. (2023), "Beat LLMs at Their Own Game"** 或其他使用多粒度统计特征做 AI 文本检测的工作 — Related Work 提到了 feature-augmented approaches（Tulchinskii et al., 2023）但覆盖不够完整。

3. **关于 iterative/recursive generation 的 model collapse 理论工作** — 论文引用了 Shumailov et al. (2024) 和 Alemohammad et al. (2024) 的经验性研究，但缺少 Dohmatob et al. (2024) 等关于 model collapse 理论界限的引用（虽然 References 中似乎有 Dohmatob，但在正文 Related Work 中未充分讨论其理论预测与本文经验发现的关系）。

4. **Ordinal classification/regression 方法** — 论文将任务 frame 为 ordinal classification（§3.1: "ordinal classification task"），但 Related Work 缺少对 ordinal classification 方法论的讨论（如 Frank and Hall, 2001 只在 §5 才提到，Gutierrez et al., 2016 也仅出现在 §5）。建议在 Related Work 或 Method 中更早引入 ordinal classification 的方法论背景。

---

## Overall Assessment

**Overall**: 3.0 (Findings)
**Confidence**: 4/5 (Quite sure — 我仔细阅读了论文和全部 29 页附录，熟悉 AI-generated text detection、distributional statistics、ordinal classification 相关文献)

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claims 有支撑，但 DDR 阈值选择、cross-model 混淆变量、binary F1 的充分性存在 gaps |
| Excitement | 3/5 (Interesting) | 问题定义新颖（depth profiling vs. binary detection），DDR 框架提供了解释性分解，但实际应用受限于 base model + 小规模 |
| Reproducibility | 4/5 | 特征定义清晰、评估协议详细、承诺代码开源。Reference model 依赖（Pythia-410M）和 seed 数据来源明确 |
| Overall Assessment | 3.0 (Findings) | 问题新颖、统计严谨、消融充分，但核心性能有限（F1=0.694）、适用范围窄（小型 base model）、DDR 框架稳健性未充分验证。适合 Findings 但不足以进入主会议 |

### 简要理由

论文在一个新颖方向上做了扎实但尚不成熟的探索。核心贡献有两个：(1) depth profiling 问题定义，(2) DDR 三分框架。问题定义本身有价值，但当前的方法实现（7 个手工特征 + XGBoost，binary F1=0.694）远未达到实用水平，且 QLoRA 的 F1=0.905 反过来证明了手工特征覆盖不足。DDR 框架虽然直观，但阈值选择偏 post-hoc，entropy mean 恰在边界上（ρ=0.60），稳健性存疑。最关键的是，所有实验限于 0.6B–8B base model，instruct model 退化严重（§5），这使得论文的发现难以推广到实际 LLM 生成文本检测场景。

论文的统计方法论质量（Bonferroni 校正、多种 effect size、TOST 等价性检验、异方差处理）在 NLP 论文中属于上乘，附录的消融覆盖度也值得肯定。如果能解决 DDR 阈值稳健性、控制 cross-model 混淆变量、并展示在更大/instruct model 上的适用性，有潜力提升至 Conference 水平。

---

## Detailed Comments

### §1 Introduction (p1-2)
- 叙事结构清晰，从 model collapse → distributional drift → depth classification 的逻辑推进合理。
- 但 Contribution 列表中的第 3 条（"We map DDR's boundary conditions"）较为模糊，不清楚 "boundary conditions" 具体指什么——是 DDR 分区的统计边界，还是分类性能的边界条件（temperature、domain 等）？建议明确化。

### §2 Related Work (p2-3)
- §2.1 对 AI text detection 的分类（binary → multi-class → depth）梳理清楚。
- §2.2 (Model Collapse) 讨论与本文的区别（"model collapse studies inference chains... the drifting/intermediate/near-stationary tri-partition central to our analysis has no analogue in model collapse studies"），positioning 合理。
- 但 §2.4 (Data Quality and Provenance) 较短且与核心叙事的连接较弱——depth profiling 如何具体帮助 data provenance？建议简化或整合进 Introduction。

### §3 Method (p3-5)
- §3.1 的 formalization 清晰（generation chain 定义、ordinal classification framing）。
- §3.2 的 generation chain 构造方案（continuation prompt、temperature 0.7、max 256 tokens）设计合理。
- §3.3 的特征选择声称 "a priori from two complementary perspectives"，但 "a priori" 的说法需要谨慎。Features 确实没有在 test data 上调优，但选择这 7 个（而非其他可能的文本统计量）的先验理由并不充分。为什么不包含 perplexity（reference model 已有）或 n-gram diversity 等其他常见指标？
- §3.4 的评估协议设计合理（LOGO + class-balanced subsampling + bootstrap CI）。

### §4 Results (p5-8)
- Table 1 信息密度高，同时报告 3-class 和 binary F1 + 95% CI，有效展示了 per-generator 变异。
- §4.2 的 DDR 描述是论文的亮点，但如 W1 所述，阈值选择的稳健性需要加强。
- §4.3 的 baseline 比较（Table 2）——4 个 detection baselines 在 3-class 和 binary 任务上均低于 7-feature ensemble，说明现有检测方法不能直接用于 depth classification。但 Table 2 中 FastDetectGPT 和 LD-Score 标注 "N/A" 缺少解释——是因为这些方法无法输出 ordinal prediction，还是评估设置不兼容？
- Figure 4（Appendix O, p18）的 per-generator LOGO 可视化有效，但 scale effect（Pythia generators 最高，Mistral 最低）的原因分析不够深入。

### §5 Discussion (p8-9)
- Instruct model 分析是论文最重要的 negative result，但篇幅太短（约 10 行）。§5 给出了 "RLHF disrupts the clean location/shape decomposition" 的推测，但没有验证。这一结果对论文的实用性影响巨大，值得更深入的分析。
- Temperature × prompt-type 交互的讨论（"temperature sensitivity is asymmetric and model-dependent"）是有价值的发现，但在正文中只有 2-3 句，主要细节在附录。建议在正文中给予更多空间。
- §5 最后关于 "cross-model F1 > single-gen F1" 的讨论试图用 LOFO F1=0.686 来支撑 cross-family transfer，但 LOFO 和 LOGO 是不同的评估协议，不能直接用于解释 cross-model 结果。

### Limitations (p9-10)
- 覆盖了主要局限性（base model only、8 generators、single reference model、English only）。
- 但缺少对 "depth > 4 的行为" 的讨论——生成链的深度是否有上限？FeatureDrifting 在 depth 5, 10, 20 时是否继续单调漂移？论文在 Appendix D 提到了 5-class 评估（Table 4, F1 ≈ 0.50），但正文 Limitations 未讨论。

### 附录整体评价
- 附录质量高，覆盖面广（A-X, 约 17 页）。特别是 Appendix I（word replacement robustness）、Appendix T（independent-seed control）和 Appendix V（heteroscedasticity analysis）展示了严谨的实验设计。
- Appendix N（cross-model per-class detail, Table 19）报告了 per-class performance，macro F1 = 0.831 with class balancing——但这个数字高于主文的 cross-model F1=0.764，需要解释两者的评估设置差异。

### 引用完整性
- 71 条引用，无 orphan/missing，9 条在 OpenAlex 中未找到（均为已知论文如 DetectGPT、Pythia、XGBoost，属索引问题非虚假引用），5 条有 minor mismatch。整体引用质量良好。
- Related Work 引用覆盖基本充分，但如 Missing References 所述，ordinal classification 方法论和 model collapse 理论工作可加强。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1962 · 2026-05-19T06:27:14.820567+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n### Summary\n本文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+（而非二分类），并在 8 个 base model 上发现了 differential depth response (DDR) 三分现象（drifting/intermediate/near-stationary）。7-feature ensemble 在 LOGO 评估下实现 binary F1=0.694。论文实验设计严谨、统计方法充分、负面结果（downstream utility、instruction tuning degradation）诚实报告。但新颖性在三篇并行工作的背景下显得增量较小，且方法仅适用于 base model，实用价值受限。\n\n### Strengths\n**S1** [实验设计严谨] 控制变量全面：seed sharing control（independent-seed F1=0.680）、length confound control（length-matched F1=0.724）、cross-reference model validation（spread ≤0.013）、LOGO + LOFO 双层 cross-validation。\n**S2** [诚实报告负面结果] Downstream utility 明确显示 depth-aware curation 不优于 random subsampling；instruction tuning 使 DDR 结构退化；高温下方法性能大幅下降。\n**S3** [DDR 分解的分析深度] 从多角度验证 DDR 三分结构：k-means、TOST、holdout generator validation、PCA。\n**S4** [叙事主线一致] Abstract→Introduction→Method→Results→Discussion→Conclusion 形成连贯故事线。\n**S5** [引用覆盖充分] 71 篇引用，57/71 通过 OpenAlex 验证，无虚假引用。\n**S6** [写作质量高] 无 AI 写作痕迹，段落结构自然，技术表述精确。\n\n### Weaknesses (Must-Fix)\n**N1** [Critical] 缺少 Responsible NLP Research Checklist — ARR 投稿必须包含，缺失可导致 desk reject。\n**N2** [Critical] 正文约 8.3-8.4 页，可能超出 8 页限制。\n**N3** [Critical] 新颖性增量有限 — 三篇并行工作已独立发现 ~3-class ceiling；DDR location/shape 分解在固定 temperature 下可预期；论文自称 \"post-hoc and empirical\"。\n\n### Weaknesses (Should-Fix)\n**W1** [Major] DDR 与已知 distributional shift 现象的本质区别不够清晰。\n**W2** [Major] Binary F1=0.694 实用意义有限。\n**W3** [Major] Abstract 约 132 words，低于 150-250 words 推荐范围，缺少 \"why important\"。\n**W4** [Major] NLL 在 Abstract 中未定义。\n**W5** [Major] Cross-model F1=0.764 存在 generator identity confound。\n**W6** [Minor] Introduction 开头过于抽象。\n**W7** [Minor] Generator subset 不一致增加阅读负担。\n\n### Questions\nQ1: DDR 在 paraphrastic chains 上是否成立？\nQ2: 不同 temperature 下 near-stationary features 的方差变化能否验证 shape control 假说？\nQ3: QLoRA 是否在 instruct models 上也测试了？\nQ4: LOPTO 使用了哪些 prompt types？是否包含 unconditional generation？\nQ5: Downstream utility 实验是否计划扩展？\n\n### Missing References\n1. Guo et al. (2024) synthetic data generation 综述\n2. Li et al. (2024) instruction-tuned model synthetic data 质量\n3. 更多 ordinal classification 在 NLP 的应用引用\n\n### Overall Assessment\nOverall: 3.0 (Findings), Soundness: 4/5, Excitement: 2.5/5, Confidence: 4/5\n\n---\n\n**请对 Reviewer 2 的每条 Weakness（N1-N3, W1-W7）和 Questions（Q1-Q5）逐条回应 [AGREE] 或 [REBUT]。**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重**: 新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n### Summary\n本文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+（而非二分类），并在 8 个 base model 上发现了 differential depth response (DDR) 三分现象（drifting/intermediate/near-stationary）。7-feature ensemble 在 LOGO 评估下实现 binary F1=0.694。论文实验设计严谨、统计方法充分、负面结果（downstream utility、instruction tuning degradation）诚实报告。但新颖性在三篇并行工作的背景下显得增量较小，且方法仅适用于 base model，实用价值受限。\n\n### Strengths\n**S1** [实验设计严谨] 控制变量全面：seed sharing control（independent-seed F1=0.680）、length confound control（length-matched F1=0.724）、cross-reference model validation（spread ≤0.013）、LOGO + LOFO 双层 cross-validation。\n**S2** [诚实报告负面结果] Downstream utility 明确显示 depth-aware curation 不优于 random subsampling；instruction tuning 使 DDR 结构退化；高温下方法性能大幅下降。\n**S3** [DDR 分解的分析深度] 从多角度验证 DDR 三分结构：k-means、TOST、holdout generator validation、PCA。\n**S4** [叙事主线一致] Abstract→Introduction→Method→Results→Discussion→Conclusion 形成连贯故事线。\n**S5** [引用覆盖充分] 71 篇引用，57/71 通过 OpenAlex 验证，无虚假引用。\n**S6** [写作质量高] 无 AI 写作痕迹，段落结构自然，技术表述精确。\n\n### Weaknesses (Must-Fix)\n**N1** [Critical] 缺少 Responsible NLP Research Checklist — ARR 投稿必须包含，缺失可导致 desk reject。\n**N2** [Critical] 正文约 8.3-8.4 页，可能超出 8 页限制。\n**N3** [Critical] 新颖性增量有限 — 三篇并行工作已独立发现 ~3-class ceiling；DDR location/shape 分解在固定 temperature 下可预期；论文自称 \"post-hoc and empirical\"。\n\n### Weaknesses (Should-Fix)\n**W1** [Major] DDR 与已知 distributional shift 现象的本质区别不够清晰。\n**W2** [Major] Binary F1=0.694 实用意义有限。\n**W3** [Major] Abstract 约 132 words，低于 150-250 words 推荐范围，缺少 \"why important\"。\n**W4** [Major] NLL 在 Abstract 中未定义。\n**W5** [Major] Cross-model F1=0.764 存在 generator identity confound。\n**W6** [Minor] Introduction 开头过于抽象。\n**W7** [Minor] Generator subset 不一致增加阅读负担。\n\n### Questions\nQ1: DDR 在 paraphrastic chains 上是否成立？\nQ2: 不同 temperature 下 near-stationary features 的方差变化能否验证 shape control 假说？\nQ3: QLoRA 是否在 instruct models 上也测试了？\nQ4: LOPTO 使用了哪些 prompt types？是否包含 unconditional generation？\nQ5: Downstream utility 实验是否计划扩展？\n\n### Missing References\n1. Guo et al. (2024) synthetic data generation 综述\n2. Li et al. (2024) instruction-tuned model synthetic data 质量\n3. 更多 ordinal classification 在 NLP 的应用引用\n\n### Overall Assessment\nOverall: 3.0 (Findings), Soundness: 4/5, Excitement: 2.5/5, Confidence: 4/5\n\n---\n\n**请对 Reviewer 2 的每条 Weakness（N1-N3, W1-W7）和 Questions（Q1-Q5）逐条回应 [AGREE] 或 [REBUT]。**"
  }
}
```

</details>

---


### Tool result

_source line 1963 · 2026-05-19T06:27:40.527299+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25706
}
```

</details>

---


### Tool call

_source line 1964 · 2026-05-19T06:27:40.880684+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- \n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Summary\n本文提出 \"depth profiling\"，将 LLM 生成文本判别从二元分类扩展为按递归生成深度分类（gen-0/gen-1/gen-2+）。8 个 base model，7 个手工特征，DDR 三分框架，XGBoost LOGO 评估 3-class F1=0.762、binary F1=0.694。QLoRA 端到端 F1=0.905。问题定义新颖，统计分析严谨，附录充实。但核心性能有限、模型规模受限、DDR 阈值缺乏理论基础、跨模型结果存在混淆变量。\n\n### Strengths\n**S1** 问题定义新颖且有实际意义。\n**S2** 统计方法论严谨（Bonferroni、Cohen's d、Glass's Δ、Cliff's δ、TOST、bootstrap CI）。\n**S3** 消融实验全面（长度控制、种子独立性、温度敏感性、跨领域、LOFO、UMAP、词替换鲁棒性）。\n**S4** DDR 框架具有解释价值。\n**S5** 诚实报告局限性。\n\n### Weaknesses (Must-Fix)\n**W1** [Critical] DDR 三分阈值缺乏理论基础 — entropy mean ρ=0.60 恰在 drifting 阈值边界上，微小变动改变分区。若阈值设为 0.61，DDR 从 3/1/3 变为 2/2/3。\n**W2** [Critical] Cross-model F1 > single-gen F1 存在 model-switching 混淆变量 — 分类器可能检测的是 \"depth + model-switching\" 混合信号。且 cross-model 用 5-gen 而 LOGO 用 8-gen，实验条件不同。\n**W3** [Major] Binary F1=0.694 支撑力有限，QLoRA 差距（F1=0.905）暴露特征覆盖不足 — 手工特征只捕获约 77% 可达性能，21pp 差距需要 interpretability 带来的具体洞见来证明。\n\n### Weaknesses (Should-Fix)\n**W4** [Major] 模型规模限于 0.6B–8B，排除真实场景。instruct model F1 降至 0.338。\n**W5** [Major] Generator subset 不一致（5/6/8-gen）增加解释复杂度。\n**W6** [Major] Gen-0 种子共享导致 3-class LOGO 存在数据泄漏，3-class F1=0.762 可能误导。\n**W7** [Minor] TOST ε=0.20 选择缺乏领域特定理由。\n**W8** [Minor] Instruct model 退化分析深度不足——未区分 RLHF vs SFT 的退化来源。\n\n### Questions\nQ1: DDR drifting 阈值在 |ρ| ±0.05 范围内分区和分类结果是否稳定？\nQ2: Cross-model 中 depth effect vs model-switching artifact 能否分离？\nQ3: LOFO 中 entropy_max（near-stationary）移除导致最大 F1 下降（-3.70pp），如何解释？\nQ4: TTR 和 hapax ratio 高度相关（r=0.97），为何保留两个？\nQ5: Downstream utility 结论是否在其他 reference model 上成立？\nQ6: Academic domain F1=0.628，是否表明 reference model domain 校准是必要的？\n\n### Missing References\n1. Fast-DetectGPT 在 Related Work 中未讨论与本方法的关系\n2. 多粒度统计特征做 AI 文本检测的工作\n3. Dohmatob et al. (2024) model collapse 理论界限\n4. Ordinal classification 方法论在 Related Work 中应更早引入\n\n### Overall Assessment\nOverall: 3.0 (Findings), Soundness: 3/5, Excitement: 3/5, Reproducibility: 4/5, Confidence: 4/5\n\n---\n\n**请对 Reviewer 1 的每条 Weakness（W1-W8）和 Questions（Q1-Q6）逐条回应 [AGREE] 或 [REBUT]。**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- \n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Summary\n本文提出 \"depth profiling\"，将 LLM 生成文本判别从二元分类扩展为按递归生成深度分类（gen-0/gen-1/gen-2+）。8 个 base model，7 个手工特征，DDR 三分框架，XGBoost LOGO 评估 3-class F1=0.762、binary F1=0.694。QLoRA 端到端 F1=0.905。问题定义新颖，统计分析严谨，附录充实。但核心性能有限、模型规模受限、DDR 阈值缺乏理论基础、跨模型结果存在混淆变量。\n\n### Strengths\n**S1** 问题定义新颖且有实际意义。\n**S2** 统计方法论严谨（Bonferroni、Cohen's d、Glass's Δ、Cliff's δ、TOST、bootstrap CI）。\n**S3** 消融实验全面（长度控制、种子独立性、温度敏感性、跨领域、LOFO、UMAP、词替换鲁棒性）。\n**S4** DDR 框架具有解释价值。\n**S5** 诚实报告局限性。\n\n### Weaknesses (Must-Fix)\n**W1** [Critical] DDR 三分阈值缺乏理论基础 — entropy mean ρ=0.60 恰在 drifting 阈值边界上，微小变动改变分区。若阈值设为 0.61，DDR 从 3/1/3 变为 2/2/3。\n**W2** [Critical] Cross-model F1 > single-gen F1 存在 model-switching 混淆变量 — 分类器可能检测的是 \"depth + model-switching\" 混合信号。且 cross-model 用 5-gen 而 LOGO 用 8-gen，实验条件不同。\n**W3** [Major] Binary F1=0.694 支撑力有限，QLoRA 差距（F1=0.905）暴露特征覆盖不足 — 手工特征只捕获约 77% 可达性能，21pp 差距需要 interpretability 带来的具体洞见来证明。\n\n### Weaknesses (Should-Fix)\n**W4** [Major] 模型规模限于 0.6B–8B，排除真实场景。instruct model F1 降至 0.338。\n**W5** [Major] Generator subset 不一致（5/6/8-gen）增加解释复杂度。\n**W6** [Major] Gen-0 种子共享导致 3-class LOGO 存在数据泄漏，3-class F1=0.762 可能误导。\n**W7** [Minor] TOST ε=0.20 选择缺乏领域特定理由。\n**W8** [Minor] Instruct model 退化分析深度不足——未区分 RLHF vs SFT 的退化来源。\n\n### Questions\nQ1: DDR drifting 阈值在 |ρ| ±0.05 范围内分区和分类结果是否稳定？\nQ2: Cross-model 中 depth effect vs model-switching artifact 能否分离？\nQ3: LOFO 中 entropy_max（near-stationary）移除导致最大 F1 下降（-3.70pp），如何解释？\nQ4: TTR 和 hapax ratio 高度相关（r=0.97），为何保留两个？\nQ5: Downstream utility 结论是否在其他 reference model 上成立？\nQ6: Academic domain F1=0.628，是否表明 reference model domain 校准是必要的？\n\n### Missing References\n1. Fast-DetectGPT 在 Related Work 中未讨论与本方法的关系\n2. 多粒度统计特征做 AI 文本检测的工作\n3. Dohmatob et al. (2024) model collapse 理论界限\n4. Ordinal classification 方法论在 Related Work 中应更早引入\n\n### Overall Assessment\nOverall: 3.0 (Findings), Soundness: 3/5, Excitement: 3/5, Reproducibility: 4/5, Confidence: 4/5\n\n---\n\n**请对 Reviewer 1 的每条 Weakness（W1-W8）和 Questions（Q1-Q6）逐条回应 [AGREE] 或 [REBUT]。**"
  }
}
```

</details>

---


### Tool result

_source line 1965 · 2026-05-19T06:27:43.493334+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2612
}
```

</details>

---


### Assistant

_source line 1966 · 2026-05-19T06:27:46.192740+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 177

## Round 177

2 recorded events


### User

_source line 1967 · 2026-05-19T06:27:49.247037+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心评估**：Overall 3.0 (Findings)，Soundness 3/5，Excitement 3/5。

**主要发现**：
- 问题定义新颖（depth profiling），统计方法论在 NLP 论文中属上乘
- 三个 Critical/Major 问题：DDR 阈值稳健性存疑（entropy mean ρ=0.60 恰在边界）、cross-model vs single-gen 比较存在 model-switching 混淆变量、binary F1=0.694 相对于 QLoRA F1=0.905 暴露了特征覆盖不足
- 模型规模限于 0.6B-8B 且 instruct model 退化严重，实际适用性受限
- 消融实验覆盖度值得肯定（29 页附录），但 generator subset 不一致（5/6/8-gen）增加了解释复杂度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1968 · 2026-05-19T06:27:53.627899+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events
