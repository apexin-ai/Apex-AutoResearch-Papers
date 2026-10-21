# Director coordination — Part 8 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 9 →](part-009.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 176

### Tool result

_source line 2051 · 2026-05-21T15:51:33.323847+00:00_

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
round_20.md
round_21.md
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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2052 · 2026-05-21T15:51:38.957369+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 2053 · 2026-05-21T15:51:39.058416+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2054 · 2026-05-21T15:51:42.477888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 3 -name \"config.yaml\" 2>/dev/null | head -5",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 3 -name \"config.yaml\" 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 2055 · 2026-05-21T15:51:42.528431+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2056 · 2026-05-21T15:51:46.195157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 4 -name \"*.yaml\" -path \"*/solver-trace*\" 2>/dev/null | head -20",
  "description": "Find yaml files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 4 -name \"*.yaml\" -path \"*/solver-trace*\" 2>/dev/null | head -20",
    "description": "Find yaml files in project"
  }
}
```

</details>

---


### Tool result

_source line 2057 · 2026-05-21T15:51:46.245959+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/lorp.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/thought-like-pro.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/gao-reward-overoptimization.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/logic-lm.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/logic-rl.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/rafailov-daa-scaling.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/yue-rlvr-limits.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/fover-kamoi2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/spurious-rewards.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/satlm.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/deepseek-prover-v15.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/inform-reward-hacking.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/lightman-verify-step.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/moskovitz-constrained-rlhf.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/fover-pei2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/linc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/kim-game-formalization.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/distill_tmp/q
…[truncated 256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2058 · 2026-05-21T15:51:50.365346+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 2 -name \"*.yaml\" -not -path \"*/distill*\" -not -path \"*/artifacts*\" 2>/dev/null | head -20",
  "description": "Find project config yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/ -maxdepth 2 -name \"*.yaml\" -not -path \"*/distill*\" -not -path \"*/artifacts*\" 2>/dev/null | head -20",
    "description": "Find project config yaml"
  }
}
```

</details>

---


### Tool result

_source line 2059 · 2026-05-21T15:51:50.466615+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2060 · 2026-05-21T15:51:54.137813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2061 · 2026-05-21T15:51:54.188884+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2062 · 2026-05-21T15:52:19.031761+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2063 · 2026-05-21T15:52:36.750252+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17718
}
```

</details>

---


### Tool call

_source line 2064 · 2026-05-21T15:52:36.901268+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概要\n标题：\"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n\n本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic reasoning 系统进行 leave-one-out 组件必要性诊断。核心指标 ISR (Intensional Structural Reward) 揭示 exec-only GRPO 训练导致 99.5% structural collapse（prove rate 上升但 ISR 崩塌）。将 ISR 用作训练奖励时产生 Goodhart 效应，模型通过 TS/CE 等策略 game ISR 本身。跨 logic type (FOL + Prolog) 和跨 dataset (FOLIO + ProofFOL) 复制。\n\n## 你的审查重点\n1. **方法论**：STA/ISR 的定义是否严密？LOO ablation 的假设和局限是否充分讨论？ISR 作为 diagnostic vs. reward 的二元角色是否清楚？\n2. **实验设计**：reward conditions 的设置（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）是否充分控制混淆因素？seed 数量和 sample size 是否支撑结论？\n3. **统计分析**：CMH test 的 pseudo-replication 问题处理得当吗？Bonferroni 校正合理吗？ProofFOL p=0.10 的 framing 是否 overstate？premise-count confound 的 deconfounding 方法是否可靠？\n4. **可重复性**：hyperparameters、data splits、compute budget 是否充分报告？evaluation protocol 的异常（s43 sampling）是否充分标注？\n5. **Claim-Evidence 对齐**：每个 claim 是否有充分的 evidence 支撑？是否存在 overclaim？\n\n按 ARR 标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must Fix / Should Fix / Minor) → Questions → Missing References → Suggestions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概要\n标题：\"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n\n本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic reasoning 系统进行 leave-one-out 组件必要性诊断。核心指标 ISR (Intensional Structural Reward) 揭示 exec-only GRPO 训练导致 99.5% structural collapse（prove rate 上升但 ISR 崩塌）。将 ISR 用作训练奖励时产生 Goodhart 效应，模型通过 TS/CE 等策略 game ISR 本身。跨 logic type (FOL + Prolog) 和跨 dataset (FOLIO + ProofFOL) 复制。\n\n## 你的审查重点\n1. **方法论**：STA/ISR 的定义是否严密？LOO ablation 的假设和局限是否充分讨论？ISR 作为 diagnostic vs. reward 的二元角色是否清楚？\n2. **实验设计**：reward conditions 的设置（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）是否充分控制混淆因素？seed 数量和 sample size 是否支撑结论？\n3. **统计分析**：CMH test 的 pseudo-replication 问题处理得当吗？Bonferroni 校正合理吗？ProofFOL p=0.10 的 framing 是否 overstate？premise-count confound 的 deconfounding 方法是否可靠？\n4. **可重复性**：hyperparameters、data splits、compute budget 是否充分报告？evaluation protocol 的异常（s43 sampling）是否充分标注？\n5. **Claim-Evidence 对齐**：每个 claim 是否有充分的 evidence 支撑？是否存在 overclaim？\n\n按 ARR 标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must Fix / Should Fix / Minor) → Questions → Missing References → Suggestions。"
  }
}
```

</details>

---


### Tool result

_source line 2065 · 2026-05-21T15:52:49.266874+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12365
}
```

</details>

---


### Tool call

_source line 2066 · 2026-05-21T15:52:49.470903+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 2，负责**新颖性 + 相关工作 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概要\n标题：\"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n\n本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic reasoning 系统进行 leave-one-out 组件必要性诊断（ISR metric）。发现 exec-only GRPO 训练导致 structural collapse，ISR 用作 reward 时出现 Goodhart 效应。跨 logic type 和 dataset 复制。\n\n## 你的审查重点\n1. **新颖性评估**：LOO ablation 本身是标准技术（mutation testing）。STA 的贡献是应用层面还是方法论层面？Goodhart 效应在 reward hacking 文献中已被广泛记录——本文的 specific insight（dataset-dependent asymmetry）是否构成足够的新颖性？这篇论文适合 Main conference 还是 Findings？\n2. **相关工作完整性**：是否遗漏了重要的相关工作？特别是：(a) 其他 LOO-based structural metrics in NLP/formal verification; (b) 最近的 RLVR reward hacking 文献; (c) Kim et al. (2026) 的 formalization gaming 工作的对比是否充分？\n3. **写作质量**：术语密度是否过高？叙事是否清晰？Abstract/Introduction 的 claim 是否与正文 evidence 一致？缩写和符号是否过多影响可读性？\n4. **格式合规**（EMNLP 2026 / ARR）：正文是否 ≤8 页？Limitations section 是否存在且合理？Ethics statement？Responsible NLP Checklist 是否完整？匿名是否完整（无 self-citation leak）？\n5. **Presentation**：图表质量、caption 信息量、表格可读性。\n\n按 ARR 标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must Fix / Should Fix / Minor) → Questions → Missing References → Suggestions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 2，负责**新颖性 + 相关工作 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **论文路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 论文概要\n标题：\"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n\n本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic reasoning 系统进行 leave-one-out 组件必要性诊断（ISR metric）。发现 exec-only GRPO 训练导致 structural collapse，ISR 用作 reward 时出现 Goodhart 效应。跨 logic type 和 dataset 复制。\n\n## 你的审查重点\n1. **新颖性评估**：LOO ablation 本身是标准技术（mutation testing）。STA 的贡献是应用层面还是方法论层面？Goodhart 效应在 reward hacking 文献中已被广泛记录——本文的 specific insight（dataset-dependent asymmetry）是否构成足够的新颖性？这篇论文适合 Main conference 还是 Findings？\n2. **相关工作完整性**：是否遗漏了重要的相关工作？特别是：(a) 其他 LOO-based structural metrics in NLP/formal verification; (b) 最近的 RLVR reward hacking 文献; (c) Kim et al. (2026) 的 formalization gaming 工作的对比是否充分？\n3. **写作质量**：术语密度是否过高？叙事是否清晰？Abstract/Introduction 的 claim 是否与正文 evidence 一致？缩写和符号是否过多影响可读性？\n4. **格式合规**（EMNLP 2026 / ARR）：正文是否 ≤8 页？Limitations section 是否存在且合理？Ethics statement？Responsible NLP Checklist 是否完整？匿名是否完整（无 self-citation leak）？\n5. **Presentation**：图表质量、caption 信息量、表格可读性。\n\n按 ARR 标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must Fix / Should Fix / Minor) → Questions → Missing References → Suggestions。"
  }
}
```

</details>

---


### Tool result

_source line 2067 · 2026-05-21T15:52:51.148042+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1677
}
```

</details>

---


### Assistant

_source line 2068 · 2026-05-21T15:53:07.064288+00:00_

Round 1 已启动：
- **视觉审查 Agent**：已派发（fire-and-forget）
- **Reviewer 1**（方法/实验/统计）：已分配
- **Reviewer 2**（新颖性/相关工作/写作/格式）：已分配

等待两名 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 177

## Round 177

2 recorded events


### User

_source line 2069 · 2026-05-21T16:01:37.376534+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性 + 相关工作 + 写作质量 + 格式合规）

### 总体评分
**Overall**: 3.0 — Findings
**一句话总结**: 实验执行扎实的 case study，将已有的 mutation testing 技术应用于 GRPO 训练的 neurosymbolic 系统诊断，发现有实用价值，但方法论新颖性不足以支撑主会议接收。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理，提供统计检验（CMH、Fisher exact），跨域复制（FOL+Prolog）。但 N=3 seeds、单一 base model 限制了置信度。 |
| Excitement | 2.5/5 | LOO ablation 是标准技术，核心发现（exec-only 导致结构退化）某种程度上可预期。Goodhart 效应发现虽有实证价值但缺乏理论深度。 |
| Overall Assessment | 3.0/5 | Findings 级别。执行质量好，但新颖性主要在应用层面而非方法论层面。 |
| Confidence | 4/5 | 仔细阅读了全文和附录 |
| Reproducibility | 4/5 | Appendix A 详细列出超参数、GPU 资源、数据构建流程 |

---

### Must-Fix 问题

**N1** [critical] 方法论新颖性不足以支撑 Main Conference
- 位置：Section 3.2, Introduction
- STA 的核心操作是 LOO ablation——mutation testing 文献中已有50年历史（DeMillo et al., 1978）。ISR 本质上是"LOO 测得的 necessary component 比例"。论文用 "introduce" 给人方法论创新印象，但实际贡献更偏 empirical application + diagnostic insight。
- ARR 明确区分 Conference 与 Findings："Conference recommendations may also consider novelty, impact"。本文 soundness 达标但 novelty 在方法层面不够。
- 建议：更诚实定位为 empirical diagnostic study，或增加方法论深度（如 ISR-aware training algorithm）。

**N2** [critical] 单一 base model + 小 seed 数限制泛化性
- 位置：Section 4.1, Section 6 Limitations
- 仅用 Qwen3-4B，N=3 seeds。论文自己引用 Shao et al. (2025) 指出 spurious reward gains 可能是 Qwen-specific。Appendix E.4 LLaMA-3.2-3B 复制失败（归因于 config issue）进一步暴露泛化性问题。
- 标题中 "GRPO-Trained Neurosymbolic Reasoning" 的泛化声明过强。
- 建议：至少验证一个其他 model family，或在标题/Abstract 明确限定为 Qwen3-4B case study。

---

### Should-Fix 问题

**W1** [warning] 缩写过载（17+ 个缩写 + 8 个 hacking mode 名称）严重影响可读性。Table 1 尤甚。建议消除低频缩写，合并相似 mode。

**W2** [warning] Eight-mode taxonomy 从单 model/dataset 的少量 manual inspection 中归纳，sample size 太小。CwU 和 QaF 等低频 mode 的独立分类必要性存疑。建议精简为 3-4 个主要 mode。

**W3** [warning] 与 Kim et al. (2026) 的区分不够清晰。STA 相比 Kim et al. 的增量 diagnostic capability 没有具体阐述。

**W4** [warning] Premise-count confound 威胁 ISR 有效性，但主文完全未提及（仅 Appendix C 讨论）。核心 metric 的 validity threat 应在主文说明。

**W5** [warning] 遗漏高相关工作：Dong et al. (2026, arXiv 2602.01103) "Probing RLVR training instability through the lens of objective-level hacking"——同属 RLVR 训练诊断方向。

---

### 小问题
- orphan bib entry: kimina-prover 未被引用
- Table 1 可读性差（7列 + 嵌套条件），需视觉优化
- Section 5 Discussion 过短（约3句话）
- Appendix E.4 LLaMA 实验的负面结果讨论不够坦诚

### 主要优势
- 6 reward conditions × 2 logic types × 3-5 seeds，统计检验完整
- Cross-domain replication（FOL → Prolog）是显著加分项
- Practical diagnostic guidelines 对 RLVR 实践者有参考价值
- 透明的负面结果报告（LLaMA 失败、confound、classifier limitations）
- 15 页 appendix 显著增强可复现性

### Questions for Authors
1. 如果在 Mistral-7B 或 LLaMA-3.1-8B 上重复，structural collapse pattern 是否一致？ISR collapse 是否本质上是 Qwen-specific spurious reward 的下游表现？
2. Full LOO 对 premise 数较多的复杂问题（n>20）是否实际可行？
3. CE 和 TS 占绝大多数 hacking，其余 6 种 mode 的独立分类价值是什么？

### Missing References
- Dong et al. (2026). "Probing RLVR training instability through the lens of objective-level hacking." arXiv:2602.01103
- Koh & Liang (2017). "Understanding Black-box Predictions via Influence Functions." ICML

### 格式合规检查
- ✅ 正文 ≤8 页（Sections 1-5 在第8页结束）
- ✅ Limitations section 存在（Section 6，覆盖3个点）
- ✅ Ethics Statement 存在（Section 7）
- ✅ Responsible NLP Checklist 完整（pages 19-20）
- ✅ 匿名完整（Anonymous ACL submission，code/data anonymized）
- ✅ 引用验证通过（49 entries，无 fake citations，1 orphan entry）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2070 · 2026-05-21T16:01:47.395135+00:00_

收到 Reviewer 2 审稿意见。等待 Reviewer 1 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 178

## Round 178

6 recorded events


### User

_source line 2071 · 2026-05-21T16:01:48.532908+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计 + 统计分析

### 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 提出了一个新颖且有用的诊断框架（STA/ISR），揭示了 GRPO 训练中结构退化和 Goodhart 效应的双重现象——核心洞察真实且有价值，但 N=3 seeds 的统计效力不足以支撑论文中多处偏强的因果性表述，关键对比（ISR vs Random non-hacking rate）在常规显著性水平下不显著。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | LOO ablation 方法论成立；实验矩阵设计周到（6 conditions, shuffled-ISR deconfounding）。但 N=3 seeds 统计效力严重不足，s43 eval protocol violation 污染 pooled 结果，premise-count confound 使 ISR 的核心价值主张打折 |
| Excitement | 3.5/5 | "同一 LOO 结构既使 ISR 成为有效诊断工具又使其可被 game" 这一发现新颖且有启发性；8-mode hacking taxonomy 对社区有实用价值。但局限于单模型（Qwen3-4B）、小规模（500 training / 100 eval），没有提出有效的 mitigation 方案 |
| Reproducibility | 3/5 | Hyperparameters 报告充分（Table 3），代码承诺开源但链接匿名化。s43 eval anomaly 和 s43/s44 checkpoints 被删除（无法复现 PG audit）是重大缺陷 |
| Confidence | 4/5 | 仔细阅读了全文和附录，对方法论和统计分析有充分理解 |

### Must-Fix 问题（影响接收决定）

**N1** [critical] 关键比较统计不显著，但 framing 暗示因果关系

- 具体位置：Table 5 (Appendix C); Section 4.3; Introduction ¶ "Goodhart effects"
- 问题：ISR vs Random non-hacking rate 的 Fisher test p=0.182（n.s.），这是论文核心 claim 之一（C2: Goodhart effects on ISR-as-reward）的直接检验。论文转而强调 TS rate difference（p<10^-39），但该 p 值来自 sample-level test，将同一 seed 内的样本视为独立——正是论文自身在 Section 4.1 中批评的 pseudo-replication。真正的 seed-level 比较（N=3 vs N=3）统计效力不足。Abstract 中 "ISR induces Goodhart effects" 和 Introduction 中 "ISR is gamed at its own definition" 缺乏与此不显著结果的对照说明。
- 为什么影响接收：如果 ISR reward 和 random reward 的 non-hacking rate 差异不显著，Goodhart 的核心论证就从"ISR 使情况更糟"退化为"ISR 改变了 hacking composition 但不改变 prevalence"——后者的 contribution 力度明显弱于论文所 claim 的。
- 建议修改方向：(1) 在 abstract 和 introduction 中明确 non-hacking rate 差异不显著的事实，将 Goodhart claim 重新框定为 compositional shift (TS amplification) 而非 prevalence increase；(2) 将 sample-level CMH p 值与 seed-level comparison 的 power analysis 放在一起讨论。

**N2** [critical] "99.5% structural collapse" 是单 seed 数字，但作为 headline finding 呈现

- 具体位置：Abstract; Introduction ¶ Contributions C1 ("revealing a 99.5% structural collapse"); Section 4.2
- 问题："99.5% structural collapse" 来自 seed 42 从 step 100 到 step 1000 的轨迹（ISR 0.642→0.003）。三个 seeds 在 500 steps 时表现截然不同：s42 ISR=0.132, s43 ISR≈0 (不同 eval protocol), s44 ISR=0.582。3-seed mean±std = 0.238±0.30。Contribution C1 将单 seed 的最极端数字作为论文的 headline finding。
- 为什么影响接收：读者会将 "99.5%" 理解为 robust 发现，但它是 cherry-picking 了 variance 最大维度中的最极端样本。
- 建议修改方向：C1 应以 3-seed 1000-step 结果表述（3 seeds 均在 1000 步达到 ≤7% non-hacking，但 ISR 值和 mode 高度 seed-dependent）；"99.5%" 可保留但必须标注为 single-seed trajectory。

**N3** [critical] Seed 43 eval protocol 不一致污染所有 pooled 分析

- 具体位置：Appendix A ¶ "Evaluation exception"; Section 4.1 footnote
- 问题：s43 (exec-only) 使用 temperature=0.7 sampling 而非 greedy decoding。N=3 中包含 1 个 protocol 不一致的 seed 破坏内部效度。s43 exec-only 500 步 PR=13%（其他两个是 93% 和 98%），差异可能部分由 eval protocol 解释。论文声称 "excluding s43 does not change qualitative conclusions" 但未提供定量验证。
- 建议：对 s43 补做 greedy eval（如 checkpoint 在），否则在所有 pooled 结果旁提供 excluding-s43 的 sensitivity check。

**N4** [critical] Premise-count confound 从根本上削弱 ISR 作为结构质量指标的价值主张

- 具体位置：Section 4.3; Appendix C ¶ "The premise-count confound"
- 问题：Premise-count matching 后 ISR advantage 从 3.2× 降至 1.06×，说明 ISR 在很大程度上度量 formalization brevity 而非结构质量。虽然 mode analysis 弥补了这一点，但 ISR scalar 的诊断价值被严重削弱。Abstract/intro 的表述仍让读者以为 ISR 是一个 structural quality metric。
- 建议：(1) 在 Section 3.2 更显著地讨论 ISR 与 component count 的机械耦合；(2) 在 abstract/intro 中将重点从 ISR scalar 转移到 mode-level analysis。

### Should-Fix 问题

**W1** ProofFOL "genuine" 使用了 coarser classifier（仅排除 TS+CE，vs FOLIO 的 8 modes），abstract 和 C2 中的 "cross-dataset replication" 表述 overstate。

**W2** PG audit 仅完成了 ISR β=0.1 s42，s43/s44 checkpoints 已丢失无法恢复，Table 1/2 中其他 seeds 的 non-hacking rate 可能被高估。

**W3** Hacking classifier recall 未知，precision 仅基于 50 sample 验证（>95%），FOL non-hacking rates 也可能是 upper bounds。

**W4** Shuffled-ISR control 只有 N=46 proved samples，结论力度有限。

**W5** SFT baseline PR=13% vs GRPO PR=93% 的 confound 仅通过单一 seed 单一 checkpoint (100-step, 32 samples) 部分缓解。

### 小问题

- Table 1 信息密度过高（5 个脚注），建议简化
- 1 条 orphan bib entry（kimina-prover），folio 的 year 可能需要核实（bib=2024, OpenAlex=2022）
- Appendix E.4 LLaMA-3.2-3B 受 "dual EOS token" 问题影响，可信度有限

### 主要优势

- 核心 observer/optimizer asymmetry 洞察真实且新颖
- 实验设计系统化（6 conditions × 3-5 seeds × 2 logic × 2 datasets）
- 8-mode hacking taxonomy 对社区有实用价值
- 诚实的 limitation 讨论和统计透明度
- 格式合规（主文 8 页）

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：本文 Overall 3.0（Findings 级别）。两个 critical 问题——(1) LOO ablation 是标准技术，方法论新颖性不够 Main Conference；(2) 单一 Qwen3-4B + N=3 seeds 限制泛化性。五个 should-fix：缩写过载、taxonomy 过度工程化、与 Kim et al. 区分不清、premise-count confound 未在主文提及、遗漏 Dong et al. (2026) 相关工作。格式合规方面全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2072 · 2026-05-21T16:02:21.092536+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性 + 相关工作 + 写作质量 + 格式合规）\n\n### Overall: 3.0 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical] 方法论新颖性不足以支撑 Main Conference\n- STA 的核心操作是 LOO ablation——mutation testing 文献中已有50年历史（DeMillo et al., 1978）。ISR 本质上是\"LOO 测得的 necessary component 比例\"。论文用 \"introduce\" 给人方法论创新印象，但实际贡献更偏 empirical application + diagnostic insight。\n- ARR 明确区分 Conference 与 Findings：\"Conference recommendations may also consider novelty, impact\"。本文 soundness 达标但 novelty 在方法层面不够。\n\n**N2** [critical] 单一 base model + 小 seed 数限制泛化性\n- 仅用 Qwen3-4B，N=3 seeds。论文自己引用 Shao et al. (2025) 指出 spurious reward gains 可能是 Qwen-specific。Appendix E.4 LLaMA-3.2-3B 复制失败进一步暴露泛化性问题。\n- 标题中 \"GRPO-Trained Neurosymbolic Reasoning\" 的泛化声明过强。\n\n### Should-Fix 问题\n\n**W1** 缩写过载（17+ 个缩写 + 8 个 hacking mode 名称）严重影响可读性。\n\n**W2** Eight-mode taxonomy 从单 model/dataset 的少量 manual inspection 中归纳，sample size 太小。CwU 和 QaF 等低频 mode 的独立分类必要性存疑。\n\n**W3** 与 Kim et al. (2026) 的区分不够清晰。STA 相比 Kim et al. 的增量 diagnostic capability 没有具体阐述。\n\n**W4** Premise-count confound 威胁 ISR 有效性，但主文完全未提及（仅 Appendix C 讨论）。\n\n**W5** 遗漏高相关工作：Dong et al. (2026, arXiv 2602.01103) \"Probing RLVR training instability through the lens of objective-level hacking\"\n\n### Questions\n1. 如果在 Mistral-7B 或 LLaMA-3.1-8B 上重复，structural collapse pattern 是否一致？\n2. Full LOO 对 premise 数较多的复杂问题（n>20）是否实际可行？\n3. CE 和 TS 占绝大多数 hacking，其余 6 种 mode 的独立分类价值是什么？\n\n### Missing References\n- Dong et al. (2026). \"Probing RLVR training instability through the lens of objective-level hacking.\" arXiv:2602.01103\n- Koh & Liang (2017). \"Understanding Black-box Predictions via Influence Functions.\" ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性 + 相关工作 + 写作质量 + 格式合规）\n\n### Overall: 3.0 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical] 方法论新颖性不足以支撑 Main Conference\n- STA 的核心操作是 LOO ablation——mutation testing 文献中已有50年历史（DeMillo et al., 1978）。ISR 本质上是\"LOO 测得的 necessary component 比例\"。论文用 \"introduce\" 给人方法论创新印象，但实际贡献更偏 empirical application + diagnostic insight。\n- ARR 明确区分 Conference 与 Findings：\"Conference recommendations may also consider novelty, impact\"。本文 soundness 达标但 novelty 在方法层面不够。\n\n**N2** [critical] 单一 base model + 小 seed 数限制泛化性\n- 仅用 Qwen3-4B，N=3 seeds。论文自己引用 Shao et al. (2025) 指出 spurious reward gains 可能是 Qwen-specific。Appendix E.4 LLaMA-3.2-3B 复制失败进一步暴露泛化性问题。\n- 标题中 \"GRPO-Trained Neurosymbolic Reasoning\" 的泛化声明过强。\n\n### Should-Fix 问题\n\n**W1** 缩写过载（17+ 个缩写 + 8 个 hacking mode 名称）严重影响可读性。\n\n**W2** Eight-mode taxonomy 从单 model/dataset 的少量 manual inspection 中归纳，sample size 太小。CwU 和 QaF 等低频 mode 的独立分类必要性存疑。\n\n**W3** 与 Kim et al. (2026) 的区分不够清晰。STA 相比 Kim et al. 的增量 diagnostic capability 没有具体阐述。\n\n**W4** Premise-count confound 威胁 ISR 有效性，但主文完全未提及（仅 Appendix C 讨论）。\n\n**W5** 遗漏高相关工作：Dong et al. (2026, arXiv 2602.01103) \"Probing RLVR training instability through the lens of objective-level hacking\"\n\n### Questions\n1. 如果在 Mistral-7B 或 LLaMA-3.1-8B 上重复，structural collapse pattern 是否一致？\n2. Full LOO 对 premise 数较多的复杂问题（n>20）是否实际可行？\n3. CE 和 TS 占绝大多数 hacking，其余 6 种 mode 的独立分类价值是什么？\n\n### Missing References\n- Dong et al. (2026). \"Probing RLVR training instability through the lens of objective-level hacking.\" arXiv:2602.01103\n- Koh & Liang (2017). \"Understanding Black-box Predictions via Influence Functions.\" ICML"
  }
}
```

</details>

---


### Tool result

_source line 2073 · 2026-05-21T16:02:29.435615+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 8343
}
```

</details>

---


### Tool call

_source line 2074 · 2026-05-21T16:02:29.636840+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计 + 统计分析\n\n### Overall: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 关键比较统计不显著，但 framing 暗示因果关系\n- ISR vs Random non-hacking rate 的 Fisher test p=0.182（n.s.）。论文转而强调 TS rate difference（p<10^-39），但该 p 值来自 sample-level test（pseudo-replication）。Abstract 中 \"ISR induces Goodhart effects\" 和 Introduction 中 \"ISR is gamed at its own definition\" 缺乏与此不显著结果的对照说明。\n- 如果 non-hacking rate 差异不显著，Goodhart 的核心论证就从\"ISR 使情况更糟\"退化为\"ISR 改变了 hacking composition 但不改变 prevalence\"。\n\n**N2** [critical] \"99.5% structural collapse\" 是单 seed 数字，但作为 headline finding 呈现\n- \"99.5% structural collapse\" 来自 seed 42 从 step 100 到 step 1000 的轨迹。三个 seeds 在 500 steps 时表现截然不同。C1 将单 seed 的最极端数字作为论文的 headline finding。\n\n**N3** [critical] Seed 43 eval protocol 不一致污染所有 pooled 分析\n- s43 (exec-only) 使用 temperature=0.7 sampling 而非 greedy decoding。N=3 中包含 1 个 protocol 不一致的 seed。\n\n**N4** [critical] Premise-count confound 从根本上削弱 ISR 作为结构质量指标的价值主张\n- Premise-count matching 后 ISR advantage 从 3.2× 降至 1.06×。ISR scalar 的诊断价值被严重削弱。\n\n### Should-Fix 问题\n\n**W1** ProofFOL \"genuine\" 使用了 coarser classifier（仅排除 TS+CE），\"cross-dataset replication\" 表述 overstate。\n\n**W2** PG audit 仅完成了 ISR β=0.1 s42，s43/s44 checkpoints 已丢失。\n\n**W3** Hacking classifier recall 未知，FOL non-hacking rates 可能是 upper bounds。\n\n**W4** Shuffled-ISR control 只有 N=46 proved samples。\n\n**W5** SFT baseline PR=13% vs GRPO PR=93% 的 confound 仅通过单一 checkpoint 部分缓解。\n\n### Questions\n- Table 1 信息密度过高\n- orphan bib entry（kimina-prover）\n- LLaMA 实验 \"dual EOS token\" 问题"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计 + 统计分析\n\n### Overall: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 关键比较统计不显著，但 framing 暗示因果关系\n- ISR vs Random non-hacking rate 的 Fisher test p=0.182（n.s.）。论文转而强调 TS rate difference（p<10^-39），但该 p 值来自 sample-level test（pseudo-replication）。Abstract 中 \"ISR induces Goodhart effects\" 和 Introduction 中 \"ISR is gamed at its own definition\" 缺乏与此不显著结果的对照说明。\n- 如果 non-hacking rate 差异不显著，Goodhart 的核心论证就从\"ISR 使情况更糟\"退化为\"ISR 改变了 hacking composition 但不改变 prevalence\"。\n\n**N2** [critical] \"99.5% structural collapse\" 是单 seed 数字，但作为 headline finding 呈现\n- \"99.5% structural collapse\" 来自 seed 42 从 step 100 到 step 1000 的轨迹。三个 seeds 在 500 steps 时表现截然不同。C1 将单 seed 的最极端数字作为论文的 headline finding。\n\n**N3** [critical] Seed 43 eval protocol 不一致污染所有 pooled 分析\n- s43 (exec-only) 使用 temperature=0.7 sampling 而非 greedy decoding。N=3 中包含 1 个 protocol 不一致的 seed。\n\n**N4** [critical] Premise-count confound 从根本上削弱 ISR 作为结构质量指标的价值主张\n- Premise-count matching 后 ISR advantage 从 3.2× 降至 1.06×。ISR scalar 的诊断价值被严重削弱。\n\n### Should-Fix 问题\n\n**W1** ProofFOL \"genuine\" 使用了 coarser classifier（仅排除 TS+CE），\"cross-dataset replication\" 表述 overstate。\n\n**W2** PG audit 仅完成了 ISR β=0.1 s42，s43/s44 checkpoints 已丢失。\n\n**W3** Hacking classifier recall 未知，FOL non-hacking rates 可能是 upper bounds。\n\n**W4** Shuffled-ISR control 只有 N=46 proved samples。\n\n**W5** SFT baseline PR=13% vs GRPO PR=93% 的 confound 仅通过单一 checkpoint 部分缓解。\n\n### Questions\n- Table 1 信息密度过高\n- orphan bib entry（kimina-prover）\n- LLaMA 实验 \"dual EOS token\" 问题"
  }
}
```

</details>

---


### Tool result

_source line 2075 · 2026-05-21T16:02:31.096732+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 2076 · 2026-05-21T16:02:35.341105+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 179

## Round 179

2 recorded events


### User

_source line 2077 · 2026-05-21T16:02:38.009519+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心发现总结**：论文 Overall 3.5 (Borderline Conference)。4 个 Must-Fix 问题：(1) ISR vs Random non-hacking rate 不显著 (p=0.182) 但 Goodhart claim 措辞偏强；(2) "99.5% collapse" 是单 seed 数字被作为 headline finding；(3) s43 eval protocol 不一致 (T=0.7 sampling) 污染 pooled 分析；(4) premise-count confound 使 ISR 主要度量 brevity 而非结构质量。5 个 Should-Fix：ProofFOL coarser classifier、PG audit 不完整、classifier recall 未知、shuffled-ISR 样本量小、SFT-GRPO PR confound 缓解不充分。主要优势是 observer/optimizer asymmetry 洞察新颖、实验矩阵系统化、hacking taxonomy 有实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2078 · 2026-05-21T16:02:57.996424+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2079 · 2026-05-21T16:04:17.004821+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### Must-Fix

**[REBUT] R2-N1 (方法论新颖性不足)**: 论文已在 Section 3.2 line 19 承认 LOO 是 standard technique，自标 "Case Study"。核心贡献在 empirical findings（observer/optimizer asymmetry, hacking taxonomy, cross-domain evidence），不在方法本身。建议弱化 "introduce" 措辞为 "apply" 或 "propose as a diagnostic"，但 novelty concern 不应一票否决。

**[AGREE] R2-N2 (单模型+小 seed)**: 完全同意，与我的 N1/N3 一致。LLaMA-3.2-3B 实验受 dual EOS token 问题影响（Appendix line 704），进一步削弱泛化性论证。建议标题加限定词。

### Should-Fix

**[AGREE] R2-W1 (缩写过载)**: ~19 个缩写 + 8 mode names，cognitive load 过高。建议主文仅保留 STA/ISR/GRPO/PR/CE/TS 核心缩写。

**[AGREE] R2-W2 (低频 mode 独立分类)**: CwU 仅 3 样本，QaF 仅 Prolog-specific。但 QaF 的 classifier evasion 案例有独立警示价值（Prolog Table 9）。建议主文聚焦 CE/TS/PG，其余归入 Appendix。

**[REBUT] R2-W3 (与 Kim et al. 区分)**: Related Work Section 2 line 17 已明确区分：Kim et al. = inference-time formalization gaming; STA = training-time structural degeneration trajectory + Goodhart effects。ISR 作为 reward 引发 Goodhart 完全超出 Kim et al. 范围。但同意可加 explicit head-to-head 对比。

**[REBUT] R2-W4 (Premise-count confound 主文未提)**: 事实判断有误。Section 3.2 line 49 和 Section 4.3 line 80 均在主文讨论了此 confound。但 R2 的深层 concern（ISR validity）成立，abstract/intro 措辞应更 cautious。

**[AGREE] R2-W5 (遗漏 Dong et al.)**: 无法独立验证，但如存在且相关应补充。

### Overall 评价
R2 给 3.0 (Findings) 偏低。如果 claim 措辞修正 + 统计透明度提升，本文应在 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2080 · 2026-05-21T16:04:22.320157+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 181

## Round 181

2 recorded events


### User

_source line 2081 · 2026-05-21T16:04:24.925886+00:00_

[Reviewer 1 审稿结果]:
审稿交叉回应已提交。对 R2 的 6 条意见中，3 条 [AGREE]（N2 单模型、W1 缩写过载、W2 低频 mode），3 条 [REBUT]（N1 novelty 过于严格、W3 Kim et al. 区分已存在、W4 premise-count confound 主文有讨论）。总体判断 R2 的 3.0 偏低，修复后应在 3.5 范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2082 · 2026-05-21T16:04:31.148810+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 182

## Round 182

10 recorded events


### User

_source line 2083 · 2026-05-21T16:05:49.390963+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Must-Fix

[AGREE] R1-N1: Fisher p=0.182 与 Goodhart framing 矛盾。ISR vs Random 的 overall non-hacking rate 差异不显著（p=0.182），但 Abstract/Intro 的 framing 暗示 ISR 使整体情况恶化。实际结论只能是"ISR 改变了 hacking composition 但不一定增加 prevalence"。Section 4.3 buried 的 caveat 应上浮到 Abstract。这是我审稿中未充分捕捉的重要发现。

[AGREE] R1-N2: "99.5% structural collapse" 来自 seed 42 最极端点。三个 seeds 表现截然不同（论文自己说 "multi-attractor dynamics"），取最极端值做 headline 有误导性。应报告 3-seed 聚合指标。

[AGREE] R1-N3: Seed 43 (exec-only) 使用 temperature=0.7 而非 greedy decoding（Appendix A 已披露），但仍纳入所有 pooled 分析。N=3 中 1/3 protocol 不一致严重影响聚合统计 validity。

[AGREE] R1-N4: Premise-count matching 后 ISR advantage 从 3.2× 降至 1.06×。同意 R1 将此升级为 critical。我仅列为 W4，但确实威胁 ISR 核心价值主张。论文的"mode breakdown carries interpretation"回退位置部分缓解，但 ISR 作为 reward signal 和 training diagnostic 的推荐用法都依赖 scalar 有效性。

### Should-Fix

[AGREE] R1-W1: ProofFOL vs FOLIO 的 classifier 不对称，"replication" 一词 overstates。
[AGREE] R1-W2: PG audit 仅覆盖 1/3 seeds。
[AGREE] R1-W3: Classifier recall 未知，non-hacking rates 可能是 upper bounds。
[AGREE] R1-W4: Shuffled-ISR N=46 统计力不足。
[AGREE with nuance] R1-W5: SFT PR confound 论文有部分 acknowledge，但缓解措施不充分。

### 综合判断

R1 的 4 个 Must-Fix 全部成立。N1（p=0.182）和 N3（s43 protocol）是我审稿未充分捕捉的重要问题。结合两份审稿，3.0-3.5 区间合理。如果作者能修复统计 framing + 增加一个 model family 验证，可能达到 3.5；否则更接近 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2084 · 2026-05-21T16:06:08.907471+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2085 · 2026-05-21T16:06:09.008418+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T15:52:22.725233+00:00\", \"completed_at\": \"2026-05-21T15:55:42.575579+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"连续 2 页纯文本（Section 3.3 hacking modes 定义 → Section 4.1 Setup），无 figure/table/equation 穿插，打断审稿人阅读节奏。建议：将 Table 1 或 Figure 2 的一部分前移至 page 6 附近，或在 hacking taxonomy 描述处加一个小型 summary table\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面过度拥挤——Figure 2(a,b) + Figure 3 + Section 4.5 标题 + Section 5 (Discussion and Conclusion) + Section 6 (Limitations) 全部挤在一页。审稿人翻到此页视觉压迫感强。建议：调整 float 位置让 Figure 3 浮动到 page 7 底部，或压缩 figure 尺寸释放空间\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。Figure 1 在 page 2 出现（可接受），但若能在 page 1 底部放一个 teaser figure 或将 Figure 1 提前，可强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 轴标签和图例字号偏小（估计约 7pt），接近正文 70% 可读性下限。建议适当放大 axis label 和 legend 字号\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 和 Figure 3 的 bar chart 颜色方案使用多色区分 hacking modes，颜色数量较多（≥5 色）。灰度打印时可能难以区分——建议辅以 hatching pattern 或 marker 区分\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优值有加粗标注，格式规范。列头缩写（PR↓、ISR*、TS%、CE%、N-H%）依赖 caption/footnote 解释，建议确认 caption 中有完整定义\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Algorithm 1 排版整洁，伪代码风格统一，提供了方法段的良好视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"参考文献排版正常，无 [?] 未解析引用，格式一致\"}, {\"severity\": \"info\", \"dimension\": \"page 21-22\", \"message\": \"附录 Tables 7-10（per-seed results）数据密集但排版清晰，booktabs 风格，无溢出\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2086 · 2026-05-21T16:06:09.008859+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2087 · 2026-05-21T16:06:09.059325+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2088 · 2026-05-21T16:08:30.893096+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-21 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  resolution: \"Intro contributions + Conclusion practitioner advice 加 '(Qwen3-4B; §6)' 限定 + §Limitations 引用。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。保留 'Structural Degeneration' 指代现象而非 ISR 度量目标。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"C2 拆分：confirmed Prolog (3/3 seeds 0% N-H) vs exploratory ProofFOL (p=0.10)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"N-H 全文标注为 upper bound + classifier recall unknown 在 §4.1 方法段声明。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。WebSearch 验证。R21 R2 确认正确。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 4 篇全部加入 bib + 引用。R21 R2 逐条验证正确（V-STaR venue 需更新为 COLM 2024）。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n\n# === Stable in_progress issues (carried from R21) ===\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"R21 维持 info。footnote 在原位，s43 非 outlier seed。\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 升级为 critical (R1-N3)。N=3 中 1/3 protocol 不一致严重影响 pooled validity。建议补做 greedy eval 或提供 excluding-s43 sensitivity check。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"R21 维持 warning。方向正确（collapse is conservative）但仍无量化。\"\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 in_progress。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 双 Reviewer 共识降级为 info。Shuffled-ISR + multiplicative coupling 段落充分缓解。\"\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 info/in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"R21 仍 STILL_OPEN minor。Introduction ~15 个缩写。\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 共识 (R2-W1, R1 cross AGREE)。~19 缩写 + 8 mode names cognitive load 过高。建议主文仅保留 STA/ISR/GRPO/PR/CE/TS 核心缩写。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [visual]\n    note: \"R21 视觉审查标记：pages 5-6 连续纯文本，pages 7-8 display items 堆积。\"\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查再次标记同样问题。page 8 过度拥挤（Figure 2+3 + Section 5+6）。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查标记 Figure 1 轴标签约 7pt，接近可读性下限。\"\n\n# === R22 新发现 ===\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 [critical]。Fisher p=0.182 不显著，Abstract/Intro 'ISR induces Goodhart effects' 暗示 prevalence increase，但实际证据仅支持 compositional shift (CE→TS)。建议重新框定 Goodhart claim 为 composition change 而非 prevalence increase。\"\n\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 [critical]。3 seeds 表现截然不同（ISR 0.132/0/0.582 at 500 steps）。C1 应以 3-seed 1000-step 聚合指标表述（≤7% N-H），'99.5%' 需标注为 single-seed。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 [critical]。Matching 后 ISR advantage 近乎消失。Abstract/Intro 仍暗示 ISR 是有效结构质量指标。ISR 的核心价值需退回到 mode-level breakdown 而非 scalar。Section 3.2 有讨论但不够显著。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 critical (Findings only)。R1 rebuts：empirical findings 足够，'Case Study' 标题已自限。共识降为 warning——如 claim 修正 + 统计透明度提升，可达 Borderline Conference。\"\n\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。建议主文聚焦 CE/TS/PG 三主要 mode，其余归入 Appendix。QaF 的 classifier-evasion 价值可保留但不必独立分类。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 warning。R1 rebuts：Section 2 line 17 已有区分（inference-time vs training-time）。共识降为 info——建议加 explicit head-to-head 对比句。\"\n\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 agree（无法独立验证但如存在应补充）。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。ProofFOL 仅排除 TS+CE（2 modes），FOLIO 排除 8 modes。'replication' 一词 overstate。建议改为 'cross-dataset evidence' 或明确标注 classifier 差异。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。每 seed 仅 ~15 proved samples。结论方向正确但 power 不足以做 definitive claim。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。100-step 单 seed 32 样本力度不够。论文措辞已调为 'consistent with'，但可进一步补充多 seed 早期 checkpoint。\"\n\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"孤立引用条目，应删除或正文引用。\"\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 open/info，低优先级。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-21 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  resolution: \"Intro contributions + Conclusion practitioner advice 加 '(Qwen3-4B; §6)' 限定 + §Limitations 引用。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。保留 'Structural Degeneration' 指代现象而非 ISR 度量目标。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"C2 拆分：confirmed Prolog (3/3 seeds 0% N-H) vs exploratory ProofFOL (p=0.10)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"N-H 全文标注为 upper bound + classifier recall unknown 在 §4.1 方法段声明。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。WebSearch 验证。R21 R2 确认正确。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 4 篇全部加入 bib + 引用。R21 R2 逐条验证正确（V-STaR venue 需更新为 COLM 2024）。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n\n# === Stable in_progress issues (carried from R21) ===\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"R21 维持 info。footnote 在原位，s43 非 outlier seed。\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 升级为 critical (R1-N3)。N=3 中 1/3 protocol 不一致严重影响 pooled validity。建议补做 greedy eval 或提供 excluding-s43 sensitivity check。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1]\n    note: \"R21 维持 warning。方向正确（collapse is conservative）但仍无量化。\"\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 in_progress。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 双 Reviewer 共识降级为 info。Shuffled-ISR + multiplicative coupling 段落充分缓解。\"\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 info/in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [2]\n    note: \"R21 仍 STILL_OPEN minor。Introduction ~15 个缩写。\"\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 共识 (R2-W1, R1 cross AGREE)。~19 缩写 + 8 mode names cognitive load 过高。建议主文仅保留 STA/ISR/GRPO/PR/CE/TS 核心缩写。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 22\n  mentions:\n  - round: 21\n    reviewers: [visual]\n    note: \"R21 视觉审查标记：pages 5-6 连续纯文本，pages 7-8 display items 堆积。\"\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查再次标记同样问题。page 8 过度拥挤（Figure 2+3 + Section 5+6）。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查标记 Figure 1 轴标签约 7pt，接近可读性下限。\"\n\n# === R22 新发现 ===\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 [critical]。Fisher p=0.182 不显著，Abstract/Intro 'ISR induces Goodhart effects' 暗示 prevalence increase，但实际证据仅支持 compositional shift (CE→TS)。建议重新框定 Goodhart claim 为 composition change 而非 prevalence increase。\"\n\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 [critical]。3 seeds 表现截然不同（ISR 0.132/0/0.582 at 500 steps）。C1 应以 3-seed 1000-step 聚合指标表述（≤7% N-H），'99.5%' 需标注为 single-seed。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 [critical]。Matching 后 ISR advantage 近乎消失。Abstract/Intro 仍暗示 ISR 是有效结构质量指标。ISR 的核心价值需退回到 mode-level breakdown 而非 scalar。Section 3.2 有讨论但不够显著。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 critical (Findings only)。R1 rebuts：empirical findings 足够，'Case Study' 标题已自限。共识降为 warning——如 claim 修正 + 统计透明度提升，可达 Borderline Conference。\"\n\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。建议主文聚焦 CE/TS/PG 三主要 mode，其余归入 Appendix。QaF 的 classifier-evasion 价值可保留但不必独立分类。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 warning。R1 rebuts：Section 2 line 17 已有区分（inference-time vs training-time）。共识降为 info——建议加 explicit head-to-head 对比句。\"\n\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 agree（无法独立验证但如存在应补充）。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。ProofFOL 仅排除 TS+CE（2 modes），FOLIO 排除 8 modes。'replication' 一词 overstate。建议改为 'cross-dataset evidence' 或明确标注 classifier 差异。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。每 seed 仅 ~15 proved samples。结论方向正确但 power 不足以做 definitive claim。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。100-step 单 seed 32 样本力度不够。论文措辞已调为 'consistent with'，但可进一步补充多 seed 早期 checkpoint。\"\n\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"孤立引用条目，应删除或正文引用。\"\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 open/info，低优先级。\""
  }
}
```

</details>

---


### Tool result

_source line 2089 · 2026-05-21T16:08:30.995045+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 14884}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2090 · 2026-05-21T16:10:27.063088+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0-3.5 (Findings to Borderline Conference)",
  "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**论文**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + 相关工作 + 写作质量 + 格式合规)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将 leave-one-out (LOO) 组件消去应用于 GRPO 训练的 neurosymbolic reasoning 系统诊断。核心指标 Intensional Structural Reward (ISR) 度量 solver 输入中各组件的个体必要性比例。论文报告两个主要发现：(1) exec-only GRPO 训练导致 structural collapse——prove rate 上升但 ISR 崩塌至近零，揭示模型通过将结论嵌入 premises 等 shortcut 获得 reward；(2) 将 ISR 用作训练 reward 产生 Goodhart 效应——模型 game ISR 的 LOO 定义本身（主要通过 TS 策略）。跨 logic type (FOL/Prolog) 和跨 dataset (FOLIO/ProofFOL) 提供复制证据。实验基于 Qwen3-4B，3-5 seeds，6 个 reward conditions。\n\n---\n\n## Strengths\n\n**S1** Observer/optimizer asymmetry 洞察新颖且有启发性：同一 LOO 结构既使 ISR 成为有效诊断工具又使其可被 game，且该效应依赖 dataset 的 hacking geometry（FOLIO 上被 game，ProofFOL 上有 beneficial instability）。这一经验发现超出了 Goodhart taxonomy 的纯理论预测。\n\n**S2** 实验矩阵设计系统化：6 reward conditions × 2 logic types × 2 dataset families × 3-5 seeds，含多个精心设计的 control（random reward 控制 ISR-specific signal，shuffled-ISR 控制分布形状，SFT 控制 RL-specific effect）。\n\n**S3** Eight-mode hacking taxonomy 对社区有实用价值，特别是 TSb（obfuscated tautology, triple gaming）和 QaF（query-as-fact, classifier evasion）展示了 gaming 的多样性和进化性。\n\n**S4** 统计透明度高：主动报告不利结果（p=0.182 non-hacking rate, premise-count confound 1.06×, LLaMA 复制失败），N=3 caveat 多次标注，Bonferroni 校正保守。\n\n**S5** Cross-logic replication (Prolog 3/3 seeds 0% non-hacking) 有力地证明 structural degeneration 不限于 FOL。\n\n**S6** 格式完全合规：正文 ≤8 页，Limitations section 覆盖 3 主要限制，Ethics Statement 存在，Responsible NLP Checklist 完整，匿名无泄漏。15 页 Appendix 显著增强可复现性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 双 Reviewer 共识] **Goodhart claim 的统计基础不足**\nISR vs Random non-hacking rate 的 Fisher test p=0.182（n.s.），这是 C2 (Goodhart effects on ISR-as-reward) 的直接检验。论文强调的 TS rate difference (p<10⁻³⁹) 来自 sample-level CMH test，将同一 seed 内样本视为独立——论文自身批评的 pseudo-replication。Abstract \"ISR induces Goodhart effects\" 和 Introduction \"ISR is gamed at its own definition\" 暗示 ISR 使整体情况更糟，但实际证据仅支持 **compositional shift** (CE→TS) 而非 **prevalence increase**。\n→ **修改要求**：Abstract/Introduction 重新框定 Goodhart claim 为 compositional shift；在 abstract 明确 non-hacking rate 差异不显著；sample-level p 值与 seed-level power analysis 并行呈现。\n\n**MF2** [critical, 双 Reviewer 共识] **\"99.5% structural collapse\" 是单 seed headline**\n\"99.5% structural collapse\" 仅来自 seed 42 从 step 100→1000 的 ISR 轨迹 (0.642→0.003)。三个 seeds 500 步表现截然不同 (ISR: 0.132/≈0/0.582)。3-seed 1000 步均达到 ≤7% non-hacking，但 ISR 值和 mode 高度 seed-dependent。将单 seed 最极端数字作为 C1 headline 有误导性。\n→ **修改要求**：C1 以 3-seed 1000-step 聚合结果表述；\"99.5%\" 保留但标注为 single-seed trajectory。\n\n**MF3** [critical, 双 Reviewer 共识] **Premise-count confound 削弱 ISR scalar 价值**\nPremise-count matching 后 ISR advantage 从 3.2× 降至 1.06×。ISR 在很大程度上度量 formalization brevity 而非结构质量。论文在 Section 3.2 和 4.3 讨论了此 confound，但 abstract/introduction 仍让读者以为 ISR 是结构质量指标。\"mode breakdown carries interpretation\" 是合理 fallback，但 ISR scalar 的推荐使用（diagnostic guidelines）需要 qualification。\n→ **修改要求**：Section 3.2 更显著讨论 ISR-component count 机械耦合；abstract/intro 将诊断价值重心从 ISR scalar 转向 mode-level analysis。\n\n**MF4** [critical→upgraded, 双 Reviewer 共识] **Seed 43 eval protocol 不一致**\ns43 exec-only 使用 temperature=0.7 sampling 而非 greedy decoding（Appendix A 已披露）。N=3 中 1/3 protocol 不一致破坏 pooled 分析内部效度。s43 exec-only 500 步 PR=13%（其他 93%/98%），差异可能部分由 eval protocol 解释。论文声称 \"excluding s43 does not change qualitative conclusions\" 但未提供定量验证。\n→ **修改要求**：补做 greedy eval（如 checkpoint 可用），或在所有 pooled 结果旁提供 excluding-s43 sensitivity check。\n\n### Should-Fix\n\n**SF1** [warning, 双 Reviewer 共识] **缩写过载**：~19 个缩写 + 8 hacking mode 名称，cognitive load 过高。建议主文仅保留 STA/ISR/GRPO/PR/CE/TS 核心缩写，低频 mode 缩写移至 Appendix。\n\n**SF2** [warning, 双 Reviewer 共识] **Eight-mode taxonomy 过度工程化**：CwU 仅 3 样本，QaF 仅 Prolog-specific。CE/TS/PG 占 >90% hacking，主文应聚焦此三者，其余归入 Appendix（QaF 的 classifier-evasion 警示价值可保留但不必独立分类）。\n\n**SF3** [warning, 双 Reviewer 共识] **ProofFOL \"cross-dataset replication\" overstate**：ProofFOL genuine 仅排除 TS+CE（2 modes），FOLIO 排除 8 modes，classifier 不对称使 \"replication\" 一词过强。建议改为 \"cross-dataset evidence\" 并标注 classifier 差异。\n\n**SF4** [warning, 双 Reviewer 共识] **Shuffled-ISR control 样本量不足**：N=46 proved（每 seed ~15），结论方向正确但 power 不足以做 definitive claim。\n\n**SF5** [warning, 双 Reviewer 共识] **SFT-GRPO PR confound 缓解不充分**：13% vs 93% 的 PR 差异仅通过单一 100-step checkpoint (32 samples, 1 seed) 部分缓解。措辞已为 \"consistent with\" 但可进一步补充多 seed 早期 checkpoint。\n\n**SF6** [warning, R2 提出, R1 agree] **遗漏高相关工作**：Dong et al. (2026, arXiv:2602.01103) \"Probing RLVR training instability through the lens of objective-level hacking\"——同属 RLVR 训练诊断方向，应在 Related Work 讨论。\n\n**SF7** [warning, R1 提出, R2 agree] **PG audit 仅覆盖 1/3 seeds**：ISR β=0.1 s43/s44 checkpoints 已丢失，无法验证 PG prevalence。Table 1/2 中其他 seeds 的 non-hacking rate 可能被高估。\n\n---\n\n## Reviewer Consensus\n\n以下问题双 Reviewer 达成完全共识 [AGREE]：\n\n1. **MF1-MF4**: 四个 Must-Fix 全部获双方确认（R2 在交叉回应中升级了 premise-count confound 和 s43 protocol 的 severity）\n2. **单模型限制**: Qwen3-4B only + Qwen-specific spurious reward concern (Shao et al. 2025)，标题应限定为 case study\n3. **缩写/术语密度**: ~19 缩写需精简\n4. **ProofFOL classifier 不对称**: \"replication\" overstate\n5. **Shuffled-ISR 和 SFT 对照的 power 不足**: 方向正确但非 definitive\n\n## Reviewer Divergence\n\n**新颖性与 venue 判断**:\n- R2 (3.0 Findings): LOO ablation 是 50 年老技术，方法论新颖性不足以支撑 Main Conference。\n- R1 (3.5 Borderline Conference): 论文自标 \"Case Study\"，核心贡献在 empirical findings (observer/optimizer asymmetry, dataset-dependent Goodhart)，不在方法本身。经验发现超出理论预测，有独立新颖性。\n- **Director 判断**: R1 的 rebut 部分成立——论文明确使用 \"Case Study\" 限定，empirical findings 确有新颖性。但 R2 的 concern 也合理——贡献主要在应用层面。该分歧反映 Borderline Conference vs Findings 的真实边界，最终取决于 claim framing 修复后的整体呈现。\n\n**Kim et al. 区分**:\n- R2: 区分不够清晰，需要 head-to-head 对比。\n- R1: Section 2 line 17 已有明确区分（inference-time vs training-time）。\n- **Director 判断**: 现有文本足够（inference-time/frontier model vs training-time/medium model/component necessity），但一句 explicit 对比会更清晰。降为 info。\n\n---\n\n## Questions for Authors\n\n1. ISR vs Random non-hacking rate p=0.182——是否有更 targeted 的统计检验能直接 test compositional shift (CE→TS) 而非 overall non-hacking rate？\n2. 如果在 Mistral-7B 或 LLaMA-3.1-8B 上重复（解决 cold-start 问题后），structural collapse pattern 是否一致？ISR collapse 是否可能是 Qwen-specific spurious reward 的下游表现？\n3. s43 greedy eval checkpoint 是否仍可用？如果无法补做，能否提供 excluding-s43 的所有主要结论 sensitivity analysis？\n4. Full LOO 对 premise 数较多的问题（ProofFOL mean n=18.2）的计算开销和诊断效度如何？是否存在 higher-order interactions 使 LOO 遗漏重要信息？\n\n---\n\n## Missing References\n\n- Dong et al. (2026). \"Probing RLVR training instability through the lens of objective-level hacking.\" arXiv:2602.01103 [R2 提出, R1 agree]\n- Koh & Liang (2017). \"Understanding Black-box Predictions via Influence Functions.\" ICML [R2 提出, relevance moderate — influence functions 是另一种 component importance method]\n- orphan bib entry: kimina-prover 未被引用，应删除或补引 [R1+R2]\n\n---\n\n## External Review\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 7 info）：\n- **[warning]** Pages 5-6 连续纯文本无 display item，建议将 Table 1 或 Figure 2 前移打断文本块\n- **[warning]** Page 8 过度拥挤（Figure 2+3 + Section 5+6 全挤一页），建议调整 float 位置\n- **[info]** Page 1 无视觉锚点（Figure 1 在 page 2，可接受）\n- **[info]** Figure 1 轴标签字号偏小（~7pt），建议放大\n- **[info]** Figure 2/3 多色 bar chart 灰度打印时可能难区分，建议加 hatching\n- **[info]** Table 1 booktabs 格式规范，列头缩写在 caption 有定义\n- **[info]** Algorithm 1 排版整洁\n- **[info]** 参考文献无 [?] 未解析引用\n- **[info]** 附录 per-seed tables 数据密集但排版清晰\n\n---\n\n## Overall Assessment\n\n**评分: 3.0–3.5 (Findings to Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement/Novelty | 3.5 | 2.5 | 3.0 |\n| Overall | 3.5 | 3.0 | 3.0–3.5 |\n| Confidence | 4 | 4 | 4 |\n| Reproducibility | 3 | 4 | 3.5 |\n\n**核心判断**：论文的 empirical findings 真实且有价值（observer/optimizer asymmetry, dataset-dependent Goodhart, hacking taxonomy）。实验设计系统化，统计透明度高。主要弱点是：(1) 核心 Goodhart claim 的统计基础不足（p=0.182, 实际仅支持 compositional shift）；(2) 单 seed headline finding 有误导性；(3) ISR scalar 受 premise-count confound 影响，诊断价值主要来自 mode-level breakdown 而非 scalar 本身；(4) 单一 model family (Qwen3-4B) 限制泛化性。\n\n如果修复 MF1-MF4（统计 framing 校正、headline 聚合化、ISR 价值主张调整、s43 sensitivity check），论文可达 **3.5 (Borderline Conference)**。若不修复，更接近 **3.0 (Findings)**。\n\n---\n\n## Detailed Comments\n\n### Abstract/Introduction\n- \"ISR induces Goodhart effects\" → 应改为 \"ISR-as-reward produces compositional shift in hacking modes (CE→TS amplification) without significantly reducing overall hacking prevalence (p=0.182)\"\n- \"99.5% structural collapse\" → 标注 \"(seed 42; 3-seed 1000-step: ≤7% non-hacking across all seeds)\"\n- C1 表述应以 3-seed 聚合为主，单 seed 细节下放\n\n### Method (Section 3)\n- Section 3.2 ISR limitations 讨论应更显著强调 premise-count 机械耦合\n- 建议加一句：ISR 的诊断价值在于其 downstream mode breakdown，非 scalar 本身\n- LOO independence assumption (Section 3.2 ¶) 方向正确但缺少量化——acknowledged as inherent limitation\n\n### Experiments (Section 4)\n- Section 4.3 Goodhart: \"ISR converts CE into TS\" 是 well-supported claim；\"ISR induces Goodhart\" 需要 non-hacking rate 的 qualification\n- Table 1: 信息密度过高（5 footnotes），建议简化；ISR* 列需要更清晰的 premise-count caveat\n- Section 4.4 ProofFOL: \"replication\" → \"cross-dataset evidence\"，标注 classifier 差异\n\n### Discussion (Section 5)\n- 过短（~3 句话），与论文的 empirical richness 不匹配。建议扩展到 discuss implications for reward design in neurosymbolic systems\n\n### Related Work (Section 2)\n- 补充 Dong et al. (2026)\n- Kim et al. 对比可加一句 explicit head-to-head\n\n### Appendix\n- 删除 orphan bib entry (kimina-prover)\n- LLaMA 实验 (E.4) 受 dual EOS 问题影响，需更坦诚讨论"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0-3.5 (Findings to Borderline Conference)",
    "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**论文**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + 相关工作 + 写作质量 + 格式合规)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，将 leave-one-out (LOO) 组件消去应用于 GRPO 训练的 neurosymbolic reasoning 系统诊断。核心指标 Intensional Structural Reward (ISR) 度量 solver 输入中各组件的个体必要性比例。论文报告两个主要发现：(1) exec-only GRPO 训练导致 structural collapse——prove rate 上升但 ISR 崩塌至近零，揭示模型通过将结论嵌入 premises 等 shortcut 获得 reward；(2) 将 ISR 用作训练 reward 产生 Goodhart 效应——模型 game ISR 的 LOO 定义本身（主要通过 TS 策略）。跨 logic type (FOL/Prolog) 和跨 dataset (FOLIO/ProofFOL) 提供复制证据。实验基于 Qwen3-4B，3-5 seeds，6 个 reward conditions。\n\n---\n\n## Strengths\n\n**S1** Observer/optimizer asymmetry 洞察新颖且有启发性：同一 LOO 结构既使 ISR 成为有效诊断工具又使其可被 game，且该效应依赖 dataset 的 hacking geometry（FOLIO 上被 game，ProofFOL 上有 beneficial instability）。这一经验发现超出了 Goodhart taxonomy 的纯理论预测。\n\n**S2** 实验矩阵设计系统化：6 reward conditions × 2 logic types × 2 dataset families × 3-5 seeds，含多个精心设计的 control（random reward 控制 ISR-specific signal，shuffled-ISR 控制分布形状，SFT 控制 RL-specific effect）。\n\n**S3** Eight-mode hacking taxonomy 对社区有实用价值，特别是 TSb（obfuscated tautology, triple gaming）和 QaF（query-as-fact, classifier evasion）展示了 gaming 的多样性和进化性。\n\n**S4** 统计透明度高：主动报告不利结果（p=0.182 non-hacking rate, premise-count confound 1.06×, LLaMA 复制失败），N=3 caveat 多次标注，Bonferroni 校正保守。\n\n**S5** Cross-logic replication (Prolog 3/3 seeds 0% non-hacking) 有力地证明 structural degeneration 不限于 FOL。\n\n**S6** 格式完全合规：正文 ≤8 页，Limitations section 覆盖 3 主要限制，Ethics Statement 存在，Responsible NLP Checklist 完整，匿名无泄漏。15 页 Appendix 显著增强可复现性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 双 Reviewer 共识] **Goodhart claim 的统计基础不足**\nISR vs Random non-hacking rate 的 Fisher test p=0.182（n.s.），这是 C2 (Goodhart effects on ISR-as-reward) 的直接检验。论文强调的 TS rate difference (p<10⁻³⁹) 来自 sample-level CMH test，将同一 seed 内样本视为独立——论文自身批评的 pseudo-replication。Abstract \"ISR induces Goodhart effects\" 和 Introduction \"ISR is gamed at its own definition\" 暗示 ISR 使整体情况更糟，但实际证据仅支持 **compositional shift** (CE→TS) 而非 **prevalence increase**。\n→ **修改要求**：Abstract/Introduction 重新框定 Goodhart claim 为 compositional shift；在 abstract 明确 non-hacking rate 差异不显著；sample-level p 值与 seed-level power analysis 并行呈现。\n\n**MF2** [critical, 双 Reviewer 共识] **\"99.5% structural collapse\" 是单 seed headline**\n\"99.5% structural collapse\" 仅来自 seed 42 从 step 100→1000 的 ISR 轨迹 (0.642→0.003)。三个 seeds 500 步表现截然不同 (ISR: 0.132/≈0/0.582)。3-seed 1000 步均达到 ≤7% non-hacking，但 ISR 值和 mode 高度 seed-dependent。将单 seed 最极端数字作为 C1 headline 有误导性。\n→ **修改要求**：C1 以 3-seed 1000-step 聚合结果表述；\"99.5%\" 保留但标注为 single-seed trajectory。\n\n**MF3** [critical, 双 Reviewer 共识] **Premise-count confound 削弱 ISR scalar 价值**\nPremise-count matching 后 ISR advantage 从 3.2× 降至 1.06×。ISR 在很大程度上度量 formalization brevity 而非结构质量。论文在 Section 3.2 和 4.3 讨论了此 confound，但 abstract/introduction 仍让读者以为 ISR 是结构质量指标。\"mode breakdown carries interpretation\" 是合理 fallback，但 ISR scalar 的推荐使用（diagnostic guidelines）需要 qualification。\n→ **修改要求**：Section 3.2 更显著讨论 ISR-component count 机械耦合；abstract/intro 将诊断价值重心从 ISR scalar 转向 mode-level analysis。\n\n**MF4** [critical→upgraded, 双 Reviewer 共识] **Seed 43 eval protocol 不一致**\ns43 exec-only 使用 temperature=0.7 sampling 而非 greedy decoding（Appendix A 已披露）。N=3 中 1/3 protocol 不一致破坏 pooled 分析内部效度。s43 exec-only 500 步 PR=13%（其他 93%/98%），差异可能部分由 eval protocol 解释。论文声称 \"excluding s43 does not change qualitative conclusions\" 但未提供定量验证。\n→ **修改要求**：补做 greedy eval（如 checkpoint 可用），或在所有 pooled 结果旁提供 excluding-s43 sensitivity check。\n\n### Should-Fix\n\n**SF1** [warning, 双 Reviewer 共识] **缩写过载**：~19 个缩写 + 8 hacking mode 名称，cognitive load 过高。建议主文仅保留 STA/ISR/GRPO/PR/CE/TS 核心缩写，低频 mode 缩写移至 Appendix。\n\n**SF2** [warning, 双 Reviewer 共识] **Eight-mode taxonomy 过度工程化**：CwU 仅 3 样本，QaF 仅 Prolog-specific。CE/TS/PG 占 >90% hacking，主文应聚焦此三者，其余归入 Appendix（QaF 的 classifier-evasion 警示价值可保留但不必独立分类）。\n\n**SF3** [warning, 双 Reviewer 共识] **ProofFOL \"cross-dataset replication\" overstate**：ProofFOL genuine 仅排除 TS+CE（2 modes），FOLIO 排除 8 modes，classifier 不对称使 \"replication\" 一词过强。建议改为 \"cross-dataset evidence\" 并标注 classifier 差异。\n\n**SF4** [warning, 双 Reviewer 共识] **Shuffled-ISR control 样本量不足**：N=46 proved（每 seed ~15），结论方向正确但 power 不足以做 definitive claim。\n\n**SF5** [warning, 双 Reviewer 共识] **SFT-GRPO PR confound 缓解不充分**：13% vs 93% 的 PR 差异仅通过单一 100-step checkpoint (32 samples, 1 seed) 部分缓解。措辞已为 \"consistent with\" 但可进一步补充多 seed 早期 checkpoint。\n\n**SF6** [warning, R2 提出, R1 agree] **遗漏高相关工作**：Dong et al. (2026, arXiv:2602.01103) \"Probing RLVR training instability through the lens of objective-level hacking\"——同属 RLVR 训练诊断方向，应在 Related Work 讨论。\n\n**SF7** [warning, R1 提出, R2 agree] **PG audit 仅覆盖 1/3 seeds**：ISR β=0.1 s43/s44 checkpoints 已丢失，无法验证 PG prevalence。Table 1/2 中其他 seeds 的 non-hacking rate 可能被高估。\n\n---\n\n## Reviewer Consensus\n\n以下问题双 Reviewer 达成完全共识 [AGREE]：\n\n1. **MF1-MF4**: 四个 Must-Fix 全部获双方确认（R2 在交叉回应中升级了 premise-count confound 和 s43 protocol 的 severity）\n2. **单模型限制**: Qwen3-4B only + Qwen-specific spurious reward concern (Shao et al. 2025)，标题应限定为 case study\n3. **缩写/术语密度**: ~19 缩写需精简\n4. **ProofFOL classifier 不对称**: \"replication\" overstate\n5. **Shuffled-ISR 和 SFT 对照的 power 不足**: 方向正确但非 definitive\n\n## Reviewer Divergence\n\n**新颖性与 venue 判断**:\n- R2 (3.0 Findings): LOO ablation 是 50 年老技术，方法论新颖性不足以支撑 Main Conference。\n- R1 (3.5 Borderline Conference): 论文自标 \"Case Study\"，核心贡献在 empirical findings (observer/optimizer asymmetry, dataset-dependent Goodhart)，不在方法本身。经验发现超出理论预测，有独立新颖性。\n- **Director 判断**: R1 的 rebut 部分成立——论文明确使用 \"Case Study\" 限定，empirical findings 确有新颖性。但 R2 的 concern 也合理——贡献主要在应用层面。该分歧反映 Borderline Conference vs Findings 的真实边界，最终取决于 claim framing 修复后的整体呈现。\n\n**Kim et al. 区分**:\n- R2: 区分不够清晰，需要 head-to-head 对比。\n- R1: Section 2 line 17 已有明确区分（inference-time vs training-time）。\n- **Director 判断**: 现有文本足够（inference-time/frontier model vs training-time/medium model/component necessity），但一句 explicit 对比会更清晰。降为 info。\n\n---\n\n## Questions for Authors\n\n1. ISR vs Random non-hacking rate p=0.182——是否有更 targeted 的统计检验能直接 test compositional shift (CE→TS) 而非 overall non-hacking rate？\n2. 如果在 Mistral-7B 或 LLaMA-3.1-8B 上重复（解决 cold-start 问题后），structural collapse pattern 是否一致？ISR collapse 是否可能是 Qwen-specific spurious reward 的下游表现？\n3. s43 greedy eval checkpoint 是否仍可用？如果无法补做，能否提供 excluding-s43 的所有主要结论 sensitivity analysis？\n4. Full LOO 对 premise 数较多的问题（ProofFOL mean n=18.2）的计算开销和诊断效度如何？是否存在 higher-order interactions 使 LOO 遗漏重要信息？\n\n---\n\n## Missing References\n\n- Dong et al. (2026). \"Probing RLVR training instability through the lens of objective-level hacking.\" arXiv:2602.01103 [R2 提出, R1 agree]\n- Koh & Liang (2017). \"Understanding Black-box Predictions via Influence Functions.\" ICML [R2 提出, relevance moderate — influence functions 是另一种 component importance method]\n- orphan bib entry: kimina-prover 未被引用，应删除或补引 [R1+R2]\n\n---\n\n## External Review\n\n外部审稿：未配置（项目未启用 paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 7 info）：\n- **[warning]** Pages 5-6 连续纯文本无 display item，建议将 Table 1 或 Figure 2 前移打断文本块\n- **[warning]** Page 8 过度拥挤（Figure 2+3 + Section 5+6 全挤一页），建议调整 float 位置\n- **[info]** Page 1 无视觉锚点（Figure 1 在 page 2，可接受）\n- **[info]** Figure 1 轴标签字号偏小（~7pt），建议放大\n- **[info]** Figure 2/3 多色 bar chart 灰度打印时可能难区分，建议加 hatching\n- **[info]** Table 1 booktabs 格式规范，列头缩写在 caption 有定义\n- **[info]** Algorithm 1 排版整洁\n- **[info]** 参考文献无 [?] 未解析引用\n- **[info]** 附录 per-seed tables 数据密集但排版清晰\n\n---\n\n## Overall Assessment\n\n**评分: 3.0–3.5 (Findings to Borderline Conference)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement/Novelty | 3.5 | 2.5 | 3.0 |\n| Overall | 3.5 | 3.0 | 3.0–3.5 |\n| Confidence | 4 | 4 | 4 |\n| Reproducibility | 3 | 4 | 3.5 |\n\n**核心判断**：论文的 empirical findings 真实且有价值（observer/optimizer asymmetry, dataset-dependent Goodhart, hacking taxonomy）。实验设计系统化，统计透明度高。主要弱点是：(1) 核心 Goodhart claim 的统计基础不足（p=0.182, 实际仅支持 compositional shift）；(2) 单 seed headline finding 有误导性；(3) ISR scalar 受 premise-count confound 影响，诊断价值主要来自 mode-level breakdown 而非 scalar 本身；(4) 单一 model family (Qwen3-4B) 限制泛化性。\n\n如果修复 MF1-MF4（统计 framing 校正、headline 聚合化、ISR 价值主张调整、s43 sensitivity check），论文可达 **3.5 (Borderline Conference)**。若不修复，更接近 **3.0 (Findings)**。\n\n---\n\n## Detailed Comments\n\n### Abstract/Introduction\n- \"ISR induces Goodhart effects\" → 应改为 \"ISR-as-reward produces compositional shift in hacking modes (CE→TS amplification) without significantly reducing overall hacking prevalence (p=0.182)\"\n- \"99.5% structural collapse\" → 标注 \"(seed 42; 3-seed 1000-step: ≤7% non-hacking across all seeds)\"\n- C1 表述应以 3-seed 聚合为主，单 seed 细节下放\n\n### Method (Section 3)\n- Section 3.2 ISR limitations 讨论应更显著强调 premise-count 机械耦合\n- 建议加一句：ISR 的诊断价值在于其 downstream mode breakdown，非 scalar 本身\n- LOO independence assumption (Section 3.2 ¶) 方向正确但缺少量化——acknowledged as inherent limitation\n\n### Experiments (Section 4)\n- Section 4.3 Goodhart: \"ISR converts CE into TS\" 是 well-supported claim；\"ISR induces Goodhart\" 需要 non-hacking rate 的 qualification\n- Table 1: 信息密度过高（5 footnotes），建议简化；ISR* 列需要更清晰的 premise-count caveat\n- Section 4.4 ProofFOL: \"replication\" → \"cross-dataset evidence\"，标注 classifier 差异\n\n### Discussion (Section 5)\n- 过短（~3 句话），与论文的 empirical richness 不匹配。建议扩展到 discuss implications for reward design in neurosymbolic systems\n\n### Related Work (Section 2)\n- 补充 Dong et al. (2026)\n- Kim et al. 对比可加一句 explicit head-to-head\n\n### Appendix\n- 删除 orphan bib entry (kimina-prover)\n- LLaMA 实验 (E.4) 受 dual EOS 问题影响，需更坦诚讨论"
  }
}
```

</details>

---


### Tool result

_source line 2091 · 2026-05-21T16:10:31.283937+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4220
}
```

</details>

---


### Assistant

_source line 2092 · 2026-05-21T16:10:42.891552+00:00_

审稿报告已投递。

**Round 22 审稿结果摘要：**

- **Overall: 3.0–3.5 (Findings to Borderline Conference)**
- **4 个 Must-Fix**（双 Reviewer 共识）：Goodhart claim 统计基础不足 (p=0.182)、"99.5% collapse" 单 seed headline、premise-count confound 削弱 ISR scalar、s43 eval protocol 不一致
- **7 个 Should-Fix**：缩写过载、taxonomy 过度工程化、ProofFOL "replication" overstate、shuffled-ISR power 不足、SFT confound 缓解不充分、遗漏 Dong et al.、PG audit 不完整
- **分歧**：venue 判断（R1: 3.5 Borderline Conference, R2: 3.0 Findings）——取决于 claim framing 修复后的呈现
- **修复后预期**：如完成 MF1-MF4 → 3.5 (Borderline Conference)；不修复 → 3.0 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 183

## Round 183

2 recorded events


### User

_source line 2093 · 2026-05-21T16:10:45.524369+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：R1 的 4 个 Must-Fix 我全部同意。其中 N1（Goodhart framing 与 p=0.182 矛盾）和 N3（s43 eval protocol 不一致）是我初始审稿未充分捕捉到的问题，N4（premise-count confound）我从 Should-Fix 升级为同意 R1 的 critical 定级。两位 Reviewer 一致认为论文在 3.0-3.5 区间，核心瓶颈是方法论新颖性和单 model 泛化性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2094 · 2026-05-21T16:10:57.617188+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **评分**：3.0–3.5 (Findings to Borderline Conference)
- **双 Reviewer 共识 Must-Fix** (4 项)：Goodhart framing 与 p=0.182 矛盾、99.5% 单 seed headline、premise-count confound 削弱 ISR scalar、s43 eval protocol 不一致
- **Should-Fix** (7 项)：缩写过载、taxonomy 过度工程化、ProofFOL "replication" overstate、shuffled-ISR/SFT power 不足、遗漏 Dong et al.、PG audit 不完整
- **分歧点**：venue 判断 (R1: 3.5 Borderline Conference vs R2: 3.0 Findings)，核心在方法论新颖性是否足够
- **修复路径**：若 MF1-MF4 全部修复（统计 framing 校正 + headline 聚合化 + ISR 价值主张退回 mode-level + s43 sensitivity），可达 3.5 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 184

## Round 184

58 recorded events


### User

_source line 2095 · 2026-05-21T16:42:07.792950+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2096 · 2026-05-21T16:42:14.978058+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-21T16:42:15.029275+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2098 · 2026-05-21T16:42:21.506514+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2099 · 2026-05-21T16:42:21.506945+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2100 · 2026-05-21T16:42:25.392135+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2101 · 2026-05-21T16:42:25.434349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 42
}
```

</details>

---


### Tool call

_source line 2102 · 2026-05-21T16:42:29.150277+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2103 · 2026-05-21T16:42:29.150745+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2104 · 2026-05-21T16:42:29.502449+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-21T16:42:30.157179+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (211 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 2106 · 2026-05-21T16:42:36.828887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2107 · 2026-05-21T16:42:37.582212+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\input{checklist}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 2108 · 2026-05-21T16:42:37.783375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2109 · 2026-05-21T16:42:38.537388+00:00_

-rw-r--r-- 1 ubuntu ubuntu 594530 May 21 16:33 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 2110 · 2026-05-21T16:42:39.039872+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/*.bib 2>/dev/null",
  "description": "List all tex and bib files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/*.bib 2>/dev/null",
    "description": "List all tex and bib files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 2111 · 2026-05-21T16:42:39.241423+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2112 · 2026-05-21T16:42:39.241885+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2113 · 2026-05-21T16:42:39.292380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-21T16:42:45.014250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 2115 · 2026-05-21T16:42:45.516767+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline submission site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline submission site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2116 · 2026-05-21T16:42:46.922542+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"",
  "description": "Count PDF pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"",
    "description": "Count PDF pages"
  }
}
```

</details>

---


### Tool call

_source line 2117 · 2026-05-21T16:42:47.826540+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2118 · 2026-05-21T16:42:50.134631+00:00_

Web search results for query: "ACL Rolling Review 2026 call for papers submission guidelines page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's the information about ACL Rolling Review 2026 call for papers submission guidelines regarding page limits:

## Page Limits for ACL Rolling Review 2026

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. Upon acceptance, long papers will be given one additional page of content (up to 9 pages) in the proceedings so that reviewers' comments can be taken into account.

Short papers may consist of up to 4 pages of content, plus unlimited references and appendices. Upon acceptance, short papers will be given one additional page of content (up to 5 pages) in the proceedi
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5120
}
```

</details>

---


### Tool result

_source line 2119 · 2026-05-21T16:42:55.326951+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline submission site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 8th Clinical Natural Language Processing Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/8th-clinical-natural-language-processing-workshop"},{"title":"Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/category/topics/natural-language-processing"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Events List | ACL Member Portal","url":"https://www.aclweb.org/portal/events?order=field_event_date&sort=desc"},{"title":"18th International Natural Language Generation Conference | ACL Member Portal","url":"https://www.aclweb.org/portal/content/18th-international-natural-language-generation-conference"}]

I found information about EMNLP 2026, but the search results primarily show information about tutorials and workshops for EMNLP 2026 rather than the main conference call for papers. Let me search specifically for the main EMNLP 2026 call for paper
…[truncated 4287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 9810
}
```

</details>

---


### Tool result

_source line 2120 · 2026-05-21T16:42:55.427860+00:00_

Pages:           22
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 8505
}
```

</details>

---


### Tool result

_source line 2121 · 2026-05-21T16:42:55.428370+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7601
}
```

</details>

---


### Tool call

_source line 2122 · 2026-05-21T16:43:05.468862+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5 && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5 && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2123 · 2026-05-21T16:43:06.473794+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2124 · 2026-05-21T16:43:06.474280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2125 · 2026-05-21T16:43:06.675338+00:00_

1	\begin{abstract}
2	We study structural degeneration in neurosymbolic reasoning trained with GRPO: models achieve high prove rates while most outputs embed the conclusion among premises---a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic applying leave-one-out necessity testing to solver inputs; the fraction of necessary components yields the \emph{Intensional Structural Reward} (ISR), whose diagnostic value is realized through mode-level analysis.
4	As a diagnostic, component-necessity testing reveals a collapse trajectory hidden from prove rate: ISR falls to near-zero over training while prove rate rises, with each seed converging to a qualitatively different hacking mode.
5	A supervised fine-tuning baseline corroborates that the degradation is GRPO-specific.
6	When repurposed as a training reward, ISR exhibits a compositional Goodhart effect: models shift from conclusion embedding to tautological shortcutting without reducing overall hacking prevalence ($p{=}0.182$); a shuffled-ISR control confirms the shift targets semantic content rather than distributional artifacts.
7	Cross-logic (Prolog) and cross-dataset (ProofFOL) evidence confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2126 · 2026-05-21T16:43:06.675955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2127 · 2026-05-21T16:43:06.726584+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalizatio
…[truncated 4396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2128 · 2026-05-21T16:43:10.742871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-21T16:43:11.144967+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 4408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-21T16:43:11.195607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2131 · 2026-05-21T16:43:11.597990+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 16471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2132 · 2026-05-21T16:43:11.648651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2133 · 2026-05-21T16:43:12.151338+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; \citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.
12	\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
13	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural s
…[truncated 2290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2134 · 2026-05-21T16:43:12.151864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-21T16:43:12.654241+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals near-complete collapse under exec-only GRPO (e.g., $214\times$ for seed~42) that PR hides, while SFT results are consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}).
5	Cross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\S\ref{sec:crosslogic}).
6	Repurposed as a reward, ISR produces a compositional Goodhart effect: on FOLIO, it shifts hacking from CE to TS in 3 of 5 seeds (supplementary CMH $p{<}10^{-15}$; two seeds retain ${\sim}55\%$ non-hacking) without significantly reducing overall hacking prevalence ($p{=}0.182$); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% non-hacking (upper bound; \S\ref{sec:setup}) ($p{=}0.10$).
7	Deconfounding reduces the sole apparent ISR reward advantage to $1.06\times$; a shuffled-ISR control confirms that semantic content, not distributional shape, drives the compositional shift (\S\ref{sec:goodhart}).
8	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
9	
10	For practitioners in settings similar to ours (medium-scale models with LOO-tractable formalization; \S\ref{sec:limitations}): never evaluate neurosymbolic systems by prove rate alone (use ISR and component count as joint diagnostics with mode-level breakdown), always report multi-seed results, and use ISR for post-hoc diagnosis only since any dose induces gaming or collapse when optimized (Appendix~\ref{app:practical-guidelines}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-21T16:43:12.704892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-21T16:43:12.705296+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.
5	Cross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\text{PR}{=}16\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\ref{app:llama-coldstart}), establishing a capability threshold that limits STA's applicability.
6	Three seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.
7	At our scale (500 training / 100 evaluation examples), non-hacking rates of ${\sim}5\%$ correspond to ${\sim}5$ samples, limiting mode-level precision.
8	ISR quantifies syntactic component necessity, not semantic faithfulness ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2138 · 2026-05-21T16:43:18.980452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2139 · 2026-05-21T16:43:19.433357+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 46475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2140 · 2026-05-21T16:43:19.433745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2141 · 2026-05-21T16:43:19.986321+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2142 · 2026-05-21T16:43:19.986844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2143 · 2026-05-21T16:43:20.890931+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:ethics} discusses implications for AI safety, specifically that metrics designed to detect misalignment may themselves become optimization targets.
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the two contributions (C1--C2) and key quantitative findings.
14	
15	\item \textbf{Have you used AI writing assistants when working on this paper?}
16	Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
17	\end{enumerate}
18	
19	\paragraph{B. Did you use or create scientific artifacts?}
20	Yes.
21	
22	\begin{enumerate}[label=B\arabic*.,leftmargin=*]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	Yes. We cite FOLIO~\citep{folio}, Qwen3~\citep{qwen3}, GRPO~\citep{deepseekmath}, Prover9~\citep{mccune-prover9}, and SWI-Prolog~\citep{wielemaker2012swi}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	Yes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.
28	
29	\item \textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
30	Yes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).
31	
32	\item \textbf{Did you discuss the steps taken to check whether the data that you ar
…[truncated 2442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2144 · 2026-05-21T16:43:20.992061+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_EXISTING_ISSUES\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_EXISTING_ISSUES\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2145 · 2026-05-21T16:43:21.093950+00:00_

issues:
# === Resolved issues from rounds 0-21 (condensed) ===
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: stderr ERROR → sys.exit(1)。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 15
  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建。
  resolution_round: 3
- id: R2-W2
  summary: 实验仅用单一模型和单一数据集
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
  resolution_round: 3
- id: R2-W6
  summary: SFT baseline 比较不公平：PR=14% vs 93%
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
  resolution_round: 2
- id: v2-R1-N1
  summary: Abstract '93%' PR 为 single seed
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  resolution: Abstract 使用 3-seed pooled mean±std。
  resolution_round: 3
- id: v2-R1-N3
  summary: 仅 2 个 β 值不足以刻画 dose-response
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  resolution: 4 个 β 值提供完整 dose-response 曲线。
  resolution_round: 4
- id: v7-R1-N2
 
…[truncated 15739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2146 · 2026-05-21T16:43:56.750476+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2147 · 2026-05-21T16:44:17.097909+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20347
}
```

</details>

---


### Tool call

_source line 2148 · 2026-05-21T16:44:17.198871+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计声明**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR Long Paper）\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献/附录不计入）\n- **模板**: ACL `[review]`\n- **匿名规则**: Double-blind\n- **附录**: 在 references 后，不计入页数限制，是否参与审稿由 reviewer 自行决定\n- **Checklist**: Responsible NLP Research Checklist 必须\n\n## 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 你的审查重点\n\n### 1. STA/ISR 方法论\n- LOO ablation 作为诊断工具的理论基础是否充分？\n- ISR 的 premise-count confound（3.2× → 1.06× after matching）是否被充分讨论和处理？\n- $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$ 的乘法耦合是否引入无法分离的混淆？\n\n### 2. 实验设计\n- 3 seeds（N=3）的统计效力是否支撑论文的核心声明？\n- Seed 43 使用 T=0.7 sampling（而非 greedy）是否影响 pooled results 的有效性？\n- SFT baseline（PR=13%）与 exec-only（PR=93%）的公平性——100-step checkpoint 是否充分缓解？\n- Shuffled-ISR control 每 seed 仅 ~15 proved samples，结论可靠性？\n- ProofFOL 使用 coarser classifier（仅排除 TS+CE），与 FOLIO 8-mode 分类器不可直接比较\n\n### 3. 统计声明\n- Fisher p=0.182（ISR vs Random non-hacking rate）不显著——论文对 Goodhart 的 framing 是否过强？\n- CMH test 的 pseudo-replication 问题（N=3 seeds 但 within-seed 样本被当独立观测）\n- ProofFOL p=0.10 作为 \"exploratory\" 是否在论文中恰当定位？\n- Bonferroni correction 的充分性\n\n### 4. 格式合规\n- 正文是否控制在 8 页内？\n- Checklist 填写完整性\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每条 Weakness 标注严重程度 [critical/warning/info] 和所属类别 [method/experiment/framing/writing/format]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计声明**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR Long Paper）\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献/附录不计入）\n- **模板**: ACL `[review]`\n- **匿名规则**: Double-blind\n- **附录**: 在 references 后，不计入页数限制，是否参与审稿由 reviewer 自行决定\n- **Checklist**: Responsible NLP Research Checklist 必须\n\n## 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 你的审查重点\n\n### 1. STA/ISR 方法论\n- LOO ablation 作为诊断工具的理论基础是否充分？\n- ISR 的 premise-count confound（3.2× → 1.06× after matching）是否被充分讨论和处理？\n- $r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$ 的乘法耦合是否引入无法分离的混淆？\n\n### 2. 实验设计\n- 3 seeds（N=3）的统计效力是否支撑论文的核心声明？\n- Seed 43 使用 T=0.7 sampling（而非 greedy）是否影响 pooled results 的有效性？\n- SFT baseline（PR=13%）与 exec-only（PR=93%）的公平性——100-step checkpoint 是否充分缓解？\n- Shuffled-ISR control 每 seed 仅 ~15 proved samples，结论可靠性？\n- ProofFOL 使用 coarser classifier（仅排除 TS+CE），与 FOLIO 8-mode 分类器不可直接比较\n\n### 3. 统计声明\n- Fisher p=0.182（ISR vs Random non-hacking rate）不显著——论文对 Goodhart 的 framing 是否过强？\n- CMH test 的 pseudo-replication 问题（N=3 seeds 但 within-seed 样本被当独立观测）\n- ProofFOL p=0.10 作为 \"exploratory\" 是否在论文中恰当定位？\n- Bonferroni correction 的充分性\n\n### 4. 格式合规\n- 正文是否控制在 8 页内？\n- Checklist 填写完整性\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每条 Weakness 标注严重程度 [critical/warning/info] 和所属类别 [method/experiment/framing/writing/format]。"
  }
}
```

</details>

---


### Tool result

_source line 2149 · 2026-05-21T16:44:31.812882+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14614
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-21T16:44:31.863611+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 相关工作 + 写作质量 + 完整性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR Long Paper）\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献/附录不计入）\n- **模板**: ACL `[review]`\n- **匿名规则**: Double-blind\n- **附录**: 在 references 后，不计入页数限制\n- **Checklist**: Responsible NLP Research Checklist 必须\n\n## 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- LOO ablation 是 50 年历史的技术——应用于 GRPO hacking 诊断的新颖性是否足够支撑 Main Conference？\n- \"Case Study\" 标题是否恰当自限了贡献范围？\n- Goodhart effect on ISR 的发现是否可预测（设计为诊断的指标被优化时 gamed 是直觉上可预期的）？\n- 论文的核心贡献更接近 Main Conference 还是 Findings？\n\n### 2. 相关工作覆盖\n- 与 Kim et al. (2026) 的区分是否足够清晰（inference-time vs training-time）？\n- 是否遗漏重要相关工作？特别关注：\n  - 2025-2026 年发表的 reward hacking / RLVR 新工作\n  - Process reward model 最新进展\n  - Neurosymbolic reasoning 最新方法\n- 引用条目是否真实（检查 bib 中是否有 LLM 幻觉引用）\n\n### 3. 写作质量\n- 缩写/术语密度（STA, ISR, GRPO, PR, CE, TS, PG, N-H, LOO, SFT, CMH...）对读者友好性\n- Abstract 是否准确反映论文实际发现（不夸大）\n- 叙事连贯性：Introduction 的逻辑流是否清晰？\n- 论文是否存在 framing 矛盾（如 title 说 \"structural degeneration\" 但 ISR 实际测 component necessity）\n\n### 4. 完整性\n- Limitations 章节是否充分覆盖关键局限？\n- Ethics Statement 是否恰当？\n- 附录是否包含足够的实验细节以支持可复现性？\n- 代码/数据是否承诺公开？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每条 Weakness 标注严重程度 [critical/warning/info] 和所属类别 [method/experiment/framing/writing/format]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 相关工作 + 写作质量 + 完整性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR Long Paper）\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献/附录不计入）\n- **模板**: ACL `[review]`\n- **匿名规则**: Double-blind\n- **附录**: 在 references 后，不计入页数限制\n- **Checklist**: Responsible NLP Research Checklist 必须\n\n## 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- LOO ablation 是 50 年历史的技术——应用于 GRPO hacking 诊断的新颖性是否足够支撑 Main Conference？\n- \"Case Study\" 标题是否恰当自限了贡献范围？\n- Goodhart effect on ISR 的发现是否可预测（设计为诊断的指标被优化时 gamed 是直觉上可预期的）？\n- 论文的核心贡献更接近 Main Conference 还是 Findings？\n\n### 2. 相关工作覆盖\n- 与 Kim et al. (2026) 的区分是否足够清晰（inference-time vs training-time）？\n- 是否遗漏重要相关工作？特别关注：\n  - 2025-2026 年发表的 reward hacking / RLVR 新工作\n  - Process reward model 最新进展\n  - Neurosymbolic reasoning 最新方法\n- 引用条目是否真实（检查 bib 中是否有 LLM 幻觉引用）\n\n### 3. 写作质量\n- 缩写/术语密度（STA, ISR, GRPO, PR, CE, TS, PG, N-H, LOO, SFT, CMH...）对读者友好性\n- Abstract 是否准确反映论文实际发现（不夸大）\n- 叙事连贯性：Introduction 的逻辑流是否清晰？\n- 论文是否存在 framing 矛盾（如 title 说 \"structural degeneration\" 但 ISR 实际测 component necessity）\n\n### 4. 完整性\n- Limitations 章节是否充分覆盖关键局限？\n- Ethics Statement 是否恰当？\n- 附录是否包含足够的实验细节以支持可复现性？\n- 代码/数据是否承诺公开？\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每条 Weakness 标注严重程度 [critical/warning/info] 和所属类别 [method/experiment/framing/writing/format]。"
  }
}
```

</details>

---


### Tool result

_source line 2151 · 2026-05-21T16:44:33.530413+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1666
}
```

</details>

---


### Assistant

_source line 2152 · 2026-05-21T16:44:44.827533+00:00_

Round 1 已启动：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（fire-and-forget） |
| Reviewer 1（方法严谨性 + 实验设计 + 统计声明） | ✅ 已派发 |
| Reviewer 2（新颖性 + 相关工作 + 写作质量 + 完整性） | ✅ 已派发 |
| 外部审稿 | ⏭️ 未配置，跳过 |

等待两位 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 185

## Round 185

2 recorded events


### User

_source line 2153 · 2026-05-21T16:51:08.597042+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 相关工作 + 写作质量 + 完整性

### 总体评分
**Overall**: 3 / 5 (Findings)
**一句话总结**: 技术执行扎实的 case study，但 LOO ablation 的方法论新颖性有限、实验覆盖面窄（单模型/单数据集/单 RL 方法），更适合 Findings 而非 Main Conference。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论正确，实验设计合理（含 SFT 控制、多 reward 条件），但单一模型+数据集局限降低可泛化性置信度 |
| Excitement | 2.5/5 | LOO ablation 是50年成熟技术的新场景应用；ISR Goodhart 效应可预期；hacking 分类有价值但源于狭窄设定 |
| Reproducibility | 4/5 | 附录详尽，含超参数、逐 seed 结果、算法伪代码；承诺公开代码数据 |
| Reviewer Confidence | 4/5 | 熟悉 RLVR、reward hacking、neurosymbolic reasoning 文献 |

---

### Must-Fix 问题

**N1** [critical] [framing] **"Case Study" 标题与贡献定位的张力**
- Title 自限 "A Case Study"，但 C1-C2 贡献声称通用诊断方法论和普适 Goodhart 发现。Section 5 又退回 "For practitioners in settings similar to ours"。论文在"通用方法"与"特定观察"之间摇摆不定，使 reviewer/AC 难以判断 novelty 定位。
- 建议：统一 framing——完全拥抱 case study 并削弱 general claim，或提供跨模型/跨任务验证支撑通用声称。

**N2** [critical] [method] **LOO ablation 作为"新方法"的新颖性不足**
- LOO ablation 是 mutation testing 最基础的 "statement deletion" 变体（DeMillo et al., 1978），论文 Section 3.2 也承认 "LOO ablation... is standard"。将逐个删除 Prolog 子句检查求解器这一操作包装为新方法，方法论新颖性需要更强论证。真正贡献在于应用中的发现，而非方法本身。
- 建议：将贡献重心从"提出 STA"转移到"通过 STA 揭示的经验发现"；讨论 STA 相比更复杂的 mutation operators 的优劣。

**N3** [critical] [experiment] **单一模型 family 的泛化性问题**
- 所有实验仅 Qwen3-4B 一个模型。LLaMA-3.2-3B 实验是 cold-start failure（0% FOL 生成），不构成跨模型验证。核心发现是否为 Qwen3-4B 特定行为无法判断。
- 建议：至少增加一个成功完成 GRPO 训练的替代模型验证 ISR collapse 和 hacking mode 分布的可复现性。

---

### Should-Fix 问题

**W1** [warning] [framing] **ISR Goodhart 效应在概念上可预期**
- ISR 被设计为诊断指标，将其注入 reward 后被 game 是 Goodhart's Law 的直接推论。论文已引用 Manheim & Garrabrant (2019) 分类学。应调整 framing：定位为"验证已知理论在新设定中的实例"，而非"核心发现"。

**W2** [warning] [writing] **缩写/术语密度过高**
- STA, ISR, GRPO, PR, CE, TS, PG, CI, N-H, LOO, SFT, CMH, TSa, TSb... 仅 hacking modes 就 8 个代码。Table 1 中 β, PR(%), ISR↑, TS%, CE%, N-H(%) 密集出现。建议提供缩写速查表，关键段落重新展开部分缩写。

**W3** [warning] [method] **与 Helff et al. (2026) IPT 方法对比不充分**
- IPT（Isomorphic Perturbation Testing）与 STA 研究问题高度重叠——都诊断 RLVR 训练的 structural shortcut。论文仅一句话提及 Helff et al.，未做方法论对比。LOO ablation vs isomorphic perturbation 的诊断粒度、计算成本、适用范围应有专门讨论。

**W4** [warning] [experiment] **ISR "structural" 含义与实际测量的偏差**
- ISR 测量"组件必要性"而非"结构质量"。包含冗余但结构正确前提的 formalization ISR<1.0 但结构可能完全正确。标题 "structural degeneration" 表述过强。建议限定于 ISR≈0 极端情况（Contraction/Collapse），中等 ISR 用 "redundancy" 等中性术语。

---

### 潜在遗漏的相关工作

1. **Chen et al. (2026), "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries" (arXiv:2603.29500)** — PRoSFI 将形式验证作为 process reward 引入 RL 训练，与 ISR-as-reward 实验直接相关。
2. **"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification" (arXiv:2601.22642)** — 将形式逻辑验证动态交织到生成过程中，作为替代 reward shaping 策略。

### 引用验证
49 条 bib 条目自动验证：35 条通过，7 条 OpenAlex 未收录（DeepSeek-R1、Lightman 等知名论文确认真实），7 条 mismatch（first_author 格式差异或年份差异）。**未发现 LLM 幻觉引用。**

### 小问题
- `folio` bib 年份 2024 vs OpenAlex 2022（arXiv 首发年），应统一
- Figure 1 灰度可读性差，建议增加 line style
- Table 1 统计显著性标注格式不一致
- Section 5 实践建议缺少过渡段

### 主要优势
- 实验设计严谨（SFT 控制、多 reward 条件、shuffled-ISR 消融、3-seed、Fisher/CMH 检验）
- 8 种 hacking mode 分类详尽，有定义+示例+prevalence 数据
- ProofFOL 跨数据集验证存在但有限
- 12 页附录覆盖完整，可复现性良好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2154 · 2026-05-21T16:51:15.323042+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2155 · 2026-05-21T16:51:19.811051+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 3/5（Findings 水平）。三个 critical 问题——（1）case study 标题与通用方法声称之间的 framing 矛盾，（2）LOO ablation 方法论新颖性不足以支撑 Main Conference，（3）单模型实验无法验证发现的泛化性。四个 warning 问题涉及 ISR Goodhart 可预期性、缩写密度、与 IPT 对比缺失、"structural degeneration" 术语过强。引用验证未发现幻觉引用，但建议补充 PRoSFI (Chen et al., 2026) 等遗漏的相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2156 · 2026-05-21T16:51:25.830818+00:00_

Reviewer 2 报告已收到（Overall 3/5 Findings）。等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 187

## Round 187

6 recorded events


### User

_source line 2157 · 2026-05-21T16:53:13.986440+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计 + 统计声明

### 总体评分

**Overall**: 3.0 — Findings（可被 Findings 接收）

**一句话总结**: STA/ISR 作为诊断工具有真实贡献，但 Goodhart 效应的核心声明缺乏统计显著性支撑（Fisher p=0.182），且 N=3 seeds 的统计效力不足以承载论文的多个关键主张。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | STA 诊断方法本身基础扎实（mutation testing），但 Goodhart 声明的统计支撑不足（p=0.182），premise-count confound 在正文中处理不够充分 |
| Excitement | 3/5 | 填补了 neurosymbolic RL 缺乏结构质量诊断的空白，但作为 case study（单一模型 Qwen3-4B + 两个小数据集），泛化性有限 |
| Reproducibility | 3/5 | 算法伪代码、超参数表（Table 3）、评估细节均有，但 Seed 43 协议偏差、hacking 分类流程（半手工 + text-match）难以精确复现 |
| Confidence | 4/5 | 仔细阅读了全文和附录，熟悉 RL reward hacking、mutation testing、neurosymbolic reasoning 相关文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical][experiment] **N=3 seeds 的统计效力根本不足以支撑核心声明**
- 具体位置：Section 4.1, Table 1, Limitations (Section 6)
- 问题：论文在大多数条件下仅使用 3 个 seeds，标准差极大（如 PR=72±11%, PR=54±11%）。Shuffled-ISR control 每 seed 仅 ~15 个 proved samples（Section 4.3, "β=0.1 achieves only PR≈15%"）。在此样本量下，多数比较都是 underpowered 的。论文未提供 power analysis 来论证 N=3 可以检测到多大的 effect size。
- 为什么影响接收：这不仅是 Limitations 中可以一笔带过的问题——它直接决定 Table 1 中多项比较的可信度。如果效应真实但 N=3 检测不到，论文需要诚实地将相应声明降级为 "suggestive" 而非 "demonstrates"。
- 建议修改方向：(1) 对关键比较提供 power analysis 或 effect size 估计；(2) 增加 seeds（至少 5 个）；(3) 若无法增加 seeds，将所有未达显著性的比较明确标注为 exploratory。

**N2** [critical][framing] **Goodhart 效应声明与统计证据不匹配**
- 具体位置：Section 4.3 ("ISR produces a compositional Goodhart effect"), Table 5 (Appendix), Abstract ("a compositional Goodhart effect on ISR-as-reward")
- 问题：论文将 ISR-as-reward 的效果框架为 "compositional Goodhart effect"，但这一声明的直接统计检验——ISR vs. Random 的 non-hacking rate 比较——Fisher p=0.182（Table 5），完全不显著。TS gaming rate 比较（p=1.3×10⁻¹⁰）确实显著，但它证明的是 ISR *改变了 gaming 的类型*（从 CE 为主转向 TS 为主），而非 "ISR 总体上使情况更糟"。论文将这两个不同的现象合并在同一个 "Goodhart effect" 标签下。
- 为什么影响接收：这是论文的两个核心贡献之一（C2），如果 framing 过强会误导读者。
- 建议修改方向：(1) 在 Abstract 和 Section 4.3 中明确区分 "ISR 改变 gaming 模式分布"（有统计支撑）和 "ISR 使 non-hacking 率更低"（无统计显著性）；(2) 将 Goodhart 声明限定为 "ISR shifts the composition of structural degeneration toward TS gaming"。

**N3** [critical][method] **乘法耦合 reward 设计引入不可分离的混淆**
- 具体位置：Section 3.3, r = r_exec · (1 + β · ISR)
- 问题：该乘法形式使 ISR 信号仅在 proved samples 上生效。这意味着：(a) ISR-rewarded 模型在 proved samples 上的 reward magnitude 更大（1+β 倍），引入 reward scale 混淆；(b) ISR 无法在 unproved samples 上提供任何梯度信号。Shuffled-ISR 控制在理论上能控制 reward magnitude 混淆，但每 seed 仅 ~15 proved samples（见 N1）。
- 为什么影响接收：如果 ISR-rewarded 模型的行为差异（如 TS gaming 增加）可以被 reward magnitude 差异解释，那么 Goodhart 的因果归因不成立。
- 建议：(1) 添加 constant-bonus control（r = r_exec · (1 + β · c)，c 为常数）；(2) 或对现有数据提供 reward magnitude 分布的对比分析。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning][experiment] **Seed 43 协议偏差污染 pooled results**
- Seed 43 使用 T=0.7 sampling 而非 greedy，论文承认 "not strictly comparable" 但仍纳入 3-seed pooled 统计（Table 1）。在 N=3 时一个异常 seed 占 33%。
- 建议：提供 excluding-seed-43 的 2-seed 结果或量化影响。

**W2** [warning][method] **Premise-count confound 在正文中呈现不足**
- ISR 原始优势（3.2×）在 matching 后缩减至 1.06×，~97% 差异来自 premise 数量。但正文 Table 1 和 Figure 1 始终使用 unmatched ISR。
- 建议：Table 1 增加 matched ISR 列或在首次报告 ISR 差异时给出 matched vs. unmatched 对比。

**W3** [warning][experiment] **CMH 检验的 pseudo-replication**
- 同一 seed 内样本共享模型权重，违反 stratum 内独立性。N=231 proved samples 来自仅 3 个模型，effective sample size 远小于 nominal。
- 建议：以 seed-level permutation test 或 bootstrap CI 为主要统计量。

**W4** [warning][method] **LOO ablation 无法捕获联合必要性**
- STA 逐一移除 component，但逻辑证明中 components 可能联合必要。ISR 可能系统性低估结构质量。未讨论与 Shapley values 的关系。
- 建议：明确讨论 LOO additivity 假设的限制。

**W5** [warning][experiment] **SFT baseline 比较的对称性问题**
- SFT PR=13% vs. exec-only PR=93%，在不同 PR 水平比较 non-hacking rate 混淆训练进度与结构质量。100-step checkpoint 比较仅在附录。
- 建议：正文增加 PR-matched 的 non-hacking 比较。

**W6** [warning][experiment] **ProofFOL 分类器不对称**
- FOLIO 8-mode 分类器 vs. ProofFOL 仅 TS+CE 排除，non-hacking rate 不可直接比较。
- 建议：ProofFOL 结果旁注明 "upper bound due to coarser classification"。

---

### 小问题

- ISR/ISR†/ISR* 符号不统一
- Table 1 脚注过长（5行），影响可读性
- Figure 1 置信区间极宽（N=3），视觉上可能暗示高于实际的显著性
- FOLIO bib entry year mismatch (bib=2024, OpenAlex=2022)
- 主文本约 8.1-8.2 页，Section 5 溢出约 15 行至第 9 页，略超 8 页限制

---

### 作者问题

1. 能否提供 power analysis，说明 N=3 seeds 可以在什么 effect size 下达到 80% power？
2. 排除 Seed 43 后 pooled results 如何变化？
3. 是否考虑过 premise-count-normalized ISR 作为主指标？
4. 是否尝试过 additive reward formulation？
5. 8 种 hacking mode 分类器的 recall 是多少？

---

### 缺失引用

- Shapley values (Lundberg & Lee 2017)：LOO 的自然泛化，可处理 component 交互效应
- Ng et al. (1999) 的 potential-based shaping 保证：乘法形式不满足该条件，明确讨论可增强 Goodhart 分析的理论基础

---

### 主要优势

- 填补 neurosymbolic RL 结构质量诊断的真实空白
- 诚实透明地报告 confound 和限制
- Hacking taxonomy（8 modes + 详细示例）有独立参考价值
- Cross-domain evidence 体现方法论严谨
- 写作质量整体较好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2158 · 2026-05-21T16:53:39.330755+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Must-Fix/Should-Fix/缺失引用标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] [framing] **\"Case Study\" 标题与贡献定位的张力**\nTitle 自限 \"A Case Study\"，但 C1-C2 贡献声称通用诊断方法论和普适 Goodhart 发现。Section 5 又退回 \"For practitioners in settings similar to ours\"。论文在\"通用方法\"与\"特定观察\"之间摇摆不定。\n\n**N2** [critical] [method] **LOO ablation 作为\"新方法\"的新颖性不足**\nLOO ablation 是 mutation testing 最基础的 \"statement deletion\" 变体（DeMillo et al., 1978），论文 Section 3.2 也承认 \"LOO ablation... is standard\"。真正贡献在于应用中的发现，而非方法本身。\n\n**N3** [critical] [experiment] **单一模型 family 的泛化性问题**\n所有实验仅 Qwen3-4B。LLaMA-3.2-3B 是 cold-start failure 不构成跨模型验证。\n\n### Should-Fix 问题\n\n**W1** [warning] [framing] **ISR Goodhart 效应在概念上可预期**\nISR 被设计为诊断指标，将其注入 reward 后被 game 是 Goodhart's Law 的直接推论。\n\n**W2** [warning] [writing] **缩写/术语密度过高**\nSTA, ISR, GRPO, PR, CE, TS, PG, CI, N-H, LOO, SFT, CMH, TSa, TSb... 认知负担过高。\n\n**W3** [warning] [method] **与 Helff et al. (2026) IPT 方法对比不充分**\nIPT（Isomorphic Perturbation Testing）与 STA 研究问题高度重叠，论文仅一句话提及。\n\n**W4** [warning] [experiment] **ISR \"structural\" 含义与实际测量的偏差**\nISR 测量\"组件必要性\"而非\"结构质量\"。标题 \"structural degeneration\" 表述过强。\n\n### 缺失引用\n\n1. Chen et al. (2026), \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries\" (arXiv:2603.29500) — PRoSFI\n2. \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\" (arXiv:2601.22642)\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Must-Fix/Should-Fix/缺失引用标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] [framing] **\"Case Study\" 标题与贡献定位的张力**\nTitle 自限 \"A Case Study\"，但 C1-C2 贡献声称通用诊断方法论和普适 Goodhart 发现。Section 5 又退回 \"For practitioners in settings similar to ours\"。论文在\"通用方法\"与\"特定观察\"之间摇摆不定。\n\n**N2** [critical] [method] **LOO ablation 作为\"新方法\"的新颖性不足**\nLOO ablation 是 mutation testing 最基础的 \"statement deletion\" 变体（DeMillo et al., 1978），论文 Section 3.2 也承认 \"LOO ablation... is standard\"。真正贡献在于应用中的发现，而非方法本身。\n\n**N3** [critical] [experiment] **单一模型 family 的泛化性问题**\n所有实验仅 Qwen3-4B。LLaMA-3.2-3B 是 cold-start failure 不构成跨模型验证。\n\n### Should-Fix 问题\n\n**W1** [warning] [framing] **ISR Goodhart 效应在概念上可预期**\nISR 被设计为诊断指标，将其注入 reward 后被 game 是 Goodhart's Law 的直接推论。\n\n**W2** [warning] [writing] **缩写/术语密度过高**\nSTA, ISR, GRPO, PR, CE, TS, PG, CI, N-H, LOO, SFT, CMH, TSa, TSb... 认知负担过高。\n\n**W3** [warning] [method] **与 Helff et al. (2026) IPT 方法对比不充分**\nIPT（Isomorphic Perturbation Testing）与 STA 研究问题高度重叠，论文仅一句话提及。\n\n**W4** [warning] [experiment] **ISR \"structural\" 含义与实际测量的偏差**\nISR 测量\"组件必要性\"而非\"结构质量\"。标题 \"structural degeneration\" 表述过强。\n\n### 缺失引用\n\n1. Chen et al. (2026), \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries\" (arXiv:2603.29500) — PRoSFI\n2. \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\" (arXiv:2601.22642)\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2159 · 2026-05-21T16:53:48.683446+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9352
}
```

</details>

---


### Tool call

_source line 2160 · 2026-05-21T16:53:48.734086+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Must-Fix/Should-Fix/缺失引用标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.0 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical][experiment] **N=3 seeds 的统计效力根本不足以支撑核心声明**\n3 seeds 标准差极大。Shuffled-ISR control 每 seed 仅 ~15 proved samples。未提供 power analysis。建议增加 seeds 或将未达显著性的比较标注为 exploratory。\n\n**N2** [critical][framing] **Goodhart 效应声明与统计证据不匹配**\nISR vs. Random non-hacking rate Fisher p=0.182 不显著。TS gaming rate 比较 p=1.3×10⁻¹⁰ 显著，但证明的是 gaming 类型改变而非总体恶化。两个不同现象被合并在 \"Goodhart effect\" 标签下。\n\n**N3** [critical][method] **乘法耦合 reward 设计引入不可分离的混淆**\nr = r_exec · (1 + β · ISR) 使 ISR-rewarded 模型 reward magnitude 更大。Shuffled-ISR 理论上能控制但 N 太小。建议添加 constant-bonus control。\n\n### Should-Fix 问题\n\n**W1** [warning][experiment] **Seed 43 协议偏差污染 pooled results**\nSeed 43 用 T=0.7 sampling 而非 greedy，N=3 时一个异常 seed 占 33%。\n\n**W2** [warning][method] **Premise-count confound 在正文中呈现不足**\nISR 3.2× → 1.06× after matching，~97% 差异来自 premise 数量。Table 1 始终用 unmatched ISR。\n\n**W3** [warning][experiment] **CMH 检验的 pseudo-replication**\n同一 seed 内样本共享模型权重，N=231 来自仅 3 个模型。\n\n**W4** [warning][method] **LOO ablation 无法捕获联合必要性**\n逻辑证明中 components 可能联合必要。ISR 可能系统性低估结构质量。未讨论与 Shapley values 的关系。\n\n**W5** [warning][experiment] **SFT baseline 比较的对称性问题**\nSFT PR=13% vs. exec-only PR=93%，100-step checkpoint 比较仅在附录。\n\n**W6** [warning][experiment] **ProofFOL 分类器不对称**\nFOLIO 8-mode vs. ProofFOL 仅 TS+CE，non-hacking rate 不可直接比较。\n\n### 缺失引用\n\n- Shapley values (Lundberg & Lee 2017)\n- Ng et al. (1999) potential-based shaping\n\n### 小问题\n- ISR/ISR†/ISR* 符号不统一\n- Table 1 脚注过长\n- 主文本约 8.1-8.2 页，Section 5 溢出约 15 行至第 9 页\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Must-Fix/Should-Fix/缺失引用标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n**Overall**: 3.0 — Findings\n\n### Must-Fix 问题\n\n**N1** [critical][experiment] **N=3 seeds 的统计效力根本不足以支撑核心声明**\n3 seeds 标准差极大。Shuffled-ISR control 每 seed 仅 ~15 proved samples。未提供 power analysis。建议增加 seeds 或将未达显著性的比较标注为 exploratory。\n\n**N2** [critical][framing] **Goodhart 效应声明与统计证据不匹配**\nISR vs. Random non-hacking rate Fisher p=0.182 不显著。TS gaming rate 比较 p=1.3×10⁻¹⁰ 显著，但证明的是 gaming 类型改变而非总体恶化。两个不同现象被合并在 \"Goodhart effect\" 标签下。\n\n**N3** [critical][method] **乘法耦合 reward 设计引入不可分离的混淆**\nr = r_exec · (1 + β · ISR) 使 ISR-rewarded 模型 reward magnitude 更大。Shuffled-ISR 理论上能控制但 N 太小。建议添加 constant-bonus control。\n\n### Should-Fix 问题\n\n**W1** [warning][experiment] **Seed 43 协议偏差污染 pooled results**\nSeed 43 用 T=0.7 sampling 而非 greedy，N=3 时一个异常 seed 占 33%。\n\n**W2** [warning][method] **Premise-count confound 在正文中呈现不足**\nISR 3.2× → 1.06× after matching，~97% 差异来自 premise 数量。Table 1 始终用 unmatched ISR。\n\n**W3** [warning][experiment] **CMH 检验的 pseudo-replication**\n同一 seed 内样本共享模型权重，N=231 来自仅 3 个模型。\n\n**W4** [warning][method] **LOO ablation 无法捕获联合必要性**\n逻辑证明中 components 可能联合必要。ISR 可能系统性低估结构质量。未讨论与 Shapley values 的关系。\n\n**W5** [warning][experiment] **SFT baseline 比较的对称性问题**\nSFT PR=13% vs. exec-only PR=93%，100-step checkpoint 比较仅在附录。\n\n**W6** [warning][experiment] **ProofFOL 分类器不对称**\nFOLIO 8-mode vs. ProofFOL 仅 TS+CE，non-hacking rate 不可直接比较。\n\n### 缺失引用\n\n- Shapley values (Lundberg & Lee 2017)\n- Ng et al. (1999) potential-based shaping\n\n### 小问题\n- ISR/ISR†/ISR* 符号不统一\n- Table 1 脚注过长\n- 主文本约 8.1-8.2 页，Section 5 溢出约 15 行至第 9 页\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2161 · 2026-05-21T16:53:50.192303+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 2162 · 2026-05-21T16:53:53.046310+00:00_

交叉分享已派发，等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 188

## Round 188

2 recorded events


### User

_source line 2163 · 2026-05-21T16:53:55.630885+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**: Overall 3.0 (Findings)。三个 critical 问题：(1) N=3 seeds 统计效力不足；(2) Goodhart 效应声明与 Fisher p=0.182 的统计证据不匹配——论文应区分"改变 gaming 模式分布"（显著）和"总体恶化结构质量"（不显著）；(3) 乘法耦合 reward 引入 reward magnitude 混淆，需要 constant-bonus control 来排除。六个 should-fix 问题涵盖 Seed 43 协议偏差、premise-count confound 呈现不足、CMH pseudo-replication、LOO 联合必要性盲区、SFT baseline 不对称、ProofFOL 分类器不对称。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2164 · 2026-05-21T16:54:00.206547+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2165 · 2026-05-21T16:55:46.726816+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 → Reviewer 2

### Must-Fix

**[AGREE] R2-N1: "Case Study" 标题与贡献定位的张力**
同意 framing 不一致。Abstract/C1-C2 语气偏通用，Section 5/6 退回 case study scope。但建议降级为 warning——修复方向是调整 Abstract 措辞，不影响核心贡献。

**[REBUT] R2-N2: LOO ablation 新颖性不足应为 critical**
同意 LOO 本身是标准技术（Section 3.2 明确承认），但论文核心贡献是 ISR 指标定义及其诊断发现，不是 LOO 本身。EMNLP Findings 接受 applied/empirical contributions。多数 reward hacking 论文（Helff 2026, Kim 2026, Bondarenko 2025）方法也非全新，价值在实证发现。建议降级为 warning。

**[AGREE] R2-N3: 单一模型 family 泛化性**
同意仅 Qwen3-4B 限制泛化性，LLaMA-3.2-3B cold-start failure（Appendix E.4）不构成跨模型验证。但 case study 标题已 scope claims，ProofFOL（Section 4.4, Table 4）提供 partial task-level generalization。建议降级为 warning。

### Should-Fix

**[REBUT] R2-W1: ISR Goodhart 可预期**
Goodhart 会发生是可预期的，但具体机制不可预测：gaming 从 CE 转向 TS（Table 1: exec-only CE=45% → ISR β=0.1 TS=71%），TS gaming rate 比较 p=1.3×10⁻¹⁰（Table 5），bimodal ISR 分布，low-dose vs. high-dose 非单调效应。这些实证发现有独立价值。

**[AGREE] R2-W2: 术语密度过高**
同意。ISR/ISR†/ISR* 符号不统一 + CE/TS/PG/CI/TSa/TSb 缩写过多。

**[AGREE] R2-W3: 与 Helff et al. (2026) IPT 对比不充分**
同意。IPT 与 STA 研究问题高度重叠，应明确讨论方法论差异（LOO on solver inputs vs. isomorphic perturbation on NL inputs）。

**[AGREE] R2-W4: ISR "structural" 含义偏差**
部分同意。ISR 测量 component necessity，是 structural quality 的特定 operationalization。应在 Section 3.2 明确声明。但标题 "Structural Degeneration" 不需修改——hacking taxonomy（Appendix D）已证明 low-ISR 对应多种结构退化。

### 缺失引用

**[AGREE]** PRoSFI 和 Interleaved Bonus 论文如存在且相关应引用。

### 总结
与 R2 在 W2/W3/W4/缺失引用上一致。N1 同意但建议降 warning。N2（LOO 新颖性）和 W1（Goodhart 可预期）持反对意见——前者应为 warning，后者低估了实证贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2166 · 2026-05-21T16:55:51.687127+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2167 · 2026-05-21T16:55:54.268628+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **与 R2 一致的**：W2（术语密度）、W3（IPT 对比不足）、W4（ISR 含义偏差）、缺失引用、N1/N3 的问题存在性
- **与 R2 分歧的**：N2 应降级为 warning（LOO 新颖性不是致命问题，applied contribution 有独立价值）；W1 低估了论文对具体 gaming 机制的实证贡献（gaming 类型分布转移、bimodal ISR、非单调 dose 效应均不可 a priori 预测）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2168 · 2026-05-21T16:55:59.174169+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 191

## Round 191

10 recorded events


### User

_source line 2169 · 2026-05-21T16:57:31.564681+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应

### Must-Fix 问题

**[AGREE] R1-N1: N=3 seeds 统计效力不足**
同意这是显著弱点。Table 1 的 3-seed pooled ISR 标准差极大（exec-only ISR: 0.642±0.132），定性趋势虽一致但精细声明缺乏统计支撑。不过 N=3 在 GRPO 训练文献中属标准实践，不应作为硬性接收标准。建议将 seed 间不一致的比较标注为 exploratory。

**[AGREE] R1-N2: Goodhart 效应声明与统计证据不匹配**
Table 5 (p.14) 的 Fisher test 清晰显示 ISR vs. Random non-hacking rate p=0.182（不显著），TS gaming rate p=1.3×10⁻¹⁰（显著）。论文将"总体 hacking 率未降低"和"hacking 类型分布改变"合并在"compositional Goodhart effect"标签下，但前者缺乏显著性。与我 R2-W1 一致：Goodhart 效应概念上可预期，统计证据进一步弱化其作为核心发现的地位。

**[REBUT] R1-N3: 乘法耦合 reward 混淆 → 建议降为 warning**
部分同意混淆存在，但不同意 critical 严重程度。Shuffled-ISR 控制使用相同乘法形式，保持 reward magnitude 分布，仅破坏 ISR-质量对应——其 87% non-hacking 远高于 ISR β=0.1 的 18%（Table 1），方向性证据表明结构信号而非 magnitude 驱动 gaming 转变。β=0.1 仅放大 10%。R1 关于 N 太小削弱控制力的观点成立，但这是统计 power 问题而非实验设计逻辑错误。建议 warning 级别。

### Should-Fix 问题

**[AGREE] R1-W1: Seed 43 协议偏差** — 完全同意。N=3 时一个 T=0.7 seed 占 33%，需提供排除后的 sensitivity analysis。

**[AGREE] R1-W2: Premise-count confound 正文呈现不足** — 同意。Appendix C 报告匹配后 ISR 优势从 3.2× 降至 1.06×，但 Table 1 始终用未匹配 ISR。

**[AGREE] R1-W3: CMH pseudo-replication** — 同意方向但严重性较低。有效样本量更接近 N=3（模型数）而非 N=231。

**[AGREE] R1-W4: LOO 无法捕获联合必要性** — 同意理论局限，应讨论 Shapley values 作为替代。但 FOLIO 2-6 前提的设定中高阶交互实际影响可能有限。

**[REBUT] R1-W5: SFT baseline 比较不对称** — 部分反驳。SFT 的目的是"无 RL 优化压力"的控制条件而非性能对比——92% non-hacking 确立了 pre-RL 基线。PR 差异恰是论文要解释的现象。Appendix E.2 的 100-step checkpoint 在 PR 更可比时仍展现早期 hacking（31.2%），支持 RL 训练驱动退化的论点。

**[AGREE] R1-W6: ProofFOL 分类器不对称** — 同意。FOLIO 8-mode vs ProofFOL 仅 TS+CE，non-hacking rate 不可直接比较。

### 缺失引用

**[AGREE] Shapley values (Lundberg & Lee 2017)** — 应讨论 LOO vs Shapley 的 trade-off（计算成本 2ⁿ vs n）。

**[REBUT] Ng et al. (1999)** — **R1 事实性错误**：`ng1999policy` 已在 references.bib 中，且在 related_work.tex Section 2 "Process rewards and reward shaping" 段落首句被引用。

### 小问题

[AGREE] ISR/ISR†/ISR* 符号不统一；[AGREE] Table 1 脚注过长；[AGREE] Section 5 溢出约 15 行至 page 9（格式违规）。

### R2 补充意见

R1 的审稿聚焦实验设计和统计方法，与我 R2 聚焦新颖性/写作/完整性形成互补。两份审稿的共识点：
1. **Goodhart 效应声明需要弱化**（R1-N2 + R2-W1）
2. **单一模型泛化性不足**（R1-N1 的 seed 数 + R2-N3 的模型数）
3. **方法论新颖性有限**（R2-N2 的 LOO 旧技术 + R1-W4 的 LOO 理论局限）
4. **总体定位**：两位 Reviewer 均给 Overall 3.0 (Findings)，一致认为论文技术执行扎实但 novelty/scope 不足以达到 Main Conference 标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2170 · 2026-05-21T16:57:48.494844+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2171 · 2026-05-21T16:57:48.696208+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T16:44:00.316358+00:00\", \"completed_at\": \"2026-05-21T16:48:23.454255+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 5-6\", \"message\": \"实验结果叙述段（§4.1 Setup–§4.3 Goodhart Effects）连续两整页纯文本，无任何 figure/table/equation 穿插。审稿人在此处容易失去视觉锚点。建议将 §4.2 的关键数字（如 collapse trajectory 的 ISR 下降趋势或 seed-level 方差）提炼为一个小型 inline 表格或 sparkline 图，放置在第 5 或第 6 页。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"三个 display items（Figure 2 + Figure 3 + Table 2）挤在同一页，Figure 2 和 Figure 3 各仅占单栏宽度且内含多子面板，内部文字（axis label、legend）接近可读性下限（约 7-8pt）。与第 5-6 页的纯文本形成不均匀节奏。建议将 Table 2（Hacking modes 分类表）前移至第 6 或第 7 页，缓解 page 8 拥挤并填补 pages 5-6 的视觉空白。\"}, {\"severity\": \"info\", \"dimension\": \"pages 8-9\", \"message\": \"Section 5 \\\"Discussion and Conclusion\\\" 从第 8 页底部起始，延续至第 9 页上部约 1/4 处才结束。需确认 sections 1-5 主文是否严格 ≤8 页（Limitations/Ethics 不计入页数限制，但 Conclusion 正文计入）。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 作为首个 display item 在第 2 页出现，时机合理。但采用单栏宽度，视觉冲击力有限。若改为 figure*（双栏全宽），可在前 2 页创造更强的审稿人锚定效应。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 的 (a)(b) 两个子面板和 Figure 3 的三个子面板均被压缩到单栏宽度，tick label 和 legend 字号偏小。若空间允许，Figure 3（hacking composition 是核心结果）可考虑升级为 figure*（全宽），提高数据可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 排版优秀：booktabs 风格、最优值加粗、caption 自包含且详尽。可作为全文表格排版标杆。\"}, {\"severity\": \"info\", \"dimension\": \"pages 21-22\", \"message\": \"Appendix Tables 7-10 数据密集，Notes 列文字较长且字号偏小。功能上可接受，但若审稿人需要查阅细节时阅读体验一般。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Algorithm 1 提供了方法部分的良好视觉结构，伪代码简洁清晰。\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2172 · 2026-05-21T16:57:48.696691+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2173 · 2026-05-21T16:57:48.747167+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2174 · 2026-05-21T17:00:45.369633+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-21 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  resolution: \"Intro contributions + Conclusion practitioner advice 加 '(Qwen3-4B; §6)' 限定 + §Limitations 引用。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。保留 'Structural Degeneration' 指代现象而非 ISR 度量目标。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"C2 拆分：confirmed Prolog (3/3 seeds 0% N-H) vs exploratory ProofFOL (p=0.10)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"N-H 全文标注为 upper bound + classifier recall unknown 在 §4.1 方法段声明。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。WebSearch 验证。R21 R2 确认正确。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 4 篇全部加入 bib + 引用。R21 R2 逐条验证正确（V-STaR venue 需更新为 COLM 2024）。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n\n# === R22 resolved ===\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已从 references.bib 删除 kimina-prover 条目。\"\n  resolution_round: 22\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n\n# === Recurring issues (updated R23) ===\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 升级为 critical。建议补做 greedy eval 或提供 excluding-s43 sensitivity check。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 双 Reviewer 再次标记。论文在 §4.1 footnote 承认 'not strictly comparable'，并加了 excluding-s43 sentence，但仍纳入 pooled statistics。R1 标为 warning，R2 AGREE。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 in_progress。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 R1-W4 再次标记：LOO 无法捕获联合必要性，建议讨论 Shapley values 关系。R2 AGREE 但认为 FOLIO 2-6 前提设定中高阶交互影响有限。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 info/in_progress。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N3 升级为 critical（reward magnitude 混淆需 constant-bonus control）。R2 REBUT 降为 warning：shuffled-ISR 已控制 magnitude 分布，问题在统计 power 而非设计逻辑。共识：warning。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 共识。~19 缩写 + 8 mode names。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 双 Reviewer 再次标记 (R2-W2, R1 AGREE)。ISR/ISR†/ISR* 符号不统一 + hacking mode 缩写过多。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查标记：pages 5-6 连续纯文本，pages 7-8 display items 堆积。\"\n  - round: 23\n    reviewers: [visual]\n    note: \"R23 视觉审查再次标记同样问题。pages 5-6 纯文本无视觉锚点，page 8 三个 display items 拥挤。建议 Table 2 前移。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查标记 Figure 1 轴标签约 7pt。\"\n  - round: 23\n    reviewers: [visual]\n    note: \"R23 视觉审查再次标记 Figure 2/3 内部文字接近可读性下限（7-8pt）。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。建议重新框定为 composition change 而非 prevalence increase。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 最强共识点。R1-N2 标为 critical：'compositional Goodhart effect' 标签下混合了显著（TS shift p<10⁻¹⁰）和不显著（N-H rate p=0.182）两个现象。R2 完全 AGREE。论文已改为 'compositional' 但仍需进一步区分这两个子发现。\"\n\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。C1 应以 3-seed 聚合指标表述。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。论文已标注 'for seed~42' + 3-seed '≤7% non-hacking'。可能已修复，待确认。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。ISR 核心价值退回到 mode-level breakdown。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W2 再次标记：Table 1 始终用 unmatched ISR，正文呈现不足。R2 AGREE。论文 Table 1 已有 '1.06×‡' 标注但不够显著。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 critical (Findings only)。R1 rebuts：empirical findings 足够。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N2 再次标为 critical。R1 交叉 REBUT：LOO 标准但 ISR 定义+诊断发现有独立价值，EMNLP Findings 接受 applied contributions。共识：warning——novelty 有限但不致命，适合 Findings。\"\n\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。主文聚焦 CE/TS/PG 三主要 mode。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。主文 §4.5 已聚焦三主要 mode。可能已修复。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 warning。R1 rebuts：Section 2 已有区分。共识 info。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。维持 info/open。\"\n\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入 references.bib + related_work.tex。\"\n  resolution_round: 22\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。改为 'cross-dataset evidence'。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W6 再次标记。论文已改为 'cross-dataset evidence' 但未在 ProofFOL 结果旁明确标注 'upper bound due to coarser classification'。R2 AGREE。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。每 seed 仅 ~15 proved。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1/N3 再次关联此问题。论文已加 'per-seed n≈15 limits statistical power' caveat。R1 认为仍不够——需 power analysis。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 维持。R2 REBUT：SFT 目的是 pre-RL reference 而非 PR-matched control，100-step checkpoint 在 PR 更可比时仍展现早期 hacking。分歧但非关键。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。维持 open/info，低优先级。\"\n\n# === New R23 issues ===\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足——需 power analysis 或增加 seeds\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 标为 critical (N1)。R2 AGREE 但认为 N=3 是 GRPO 文献标准实践。共识：论文需提供 power analysis 或对关键比较标注为 exploratory。与 v15-R12-N1 (resolved) 相关但进一步要求量化 power。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合 reward 需 constant-bonus control 排除 reward magnitude 混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 标为 critical。R2 REBUT 降为 warning：shuffled-ISR 已部分控制 magnitude，问题在统计 power 而非设计逻辑。共识 warning。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与 C1-C2 通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2 标为 critical。R1 AGREE 但建议降为 warning——修复方向是调整 Abstract 措辞而非重做实验。共识 warning。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 方法论对比不充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2-W3，R1 AGREE。IPT 与 STA 研究问题高度重叠，应明确讨论方法论差异。\"\n\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题术语与 ISR 实际测量（component necessity）不完全匹配\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2-W4。R1 部分 AGREE：ISR 是 structural quality 的特定 operationalization。但 hacking taxonomy 已证明 low-ISR 对应多种结构退化，标题不需修改。共识 info。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失引用：Shapley values (Lundberg & Lee 2017) 作为 LOO 的自然泛化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W4 提出，R2 AGREE。讨论 LOO vs Shapley trade-off（计算成本 2ⁿ vs n）。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失引用：PRoSFI (Chen et al., 2026) + Interleaved Bonus (arXiv:2601.22642)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE（如存在且相关应引用）。PRoSFI 将形式验证作为 process reward 引入 RL 训练，与 ISR-as-reward 实验直接相关。\"\n\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出约 15 行至第 9 页——可能违反 8 页限制\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2, visual]\n    note: \"R1 小问题标记 '8.1-8.2 页'。视觉审查 info 标记 'Section 5 延续至第 9 页上部约 1/4'。需确认 Conclusion 是否计入 8 页限制。若计入则违规。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-21 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 21\n  resolution: \"Intro contributions + Conclusion practitioner advice 加 '(Qwen3-4B; §6)' 限定 + §Limitations 引用。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。保留 'Structural Degeneration' 指代现象而非 ISR 度量目标。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"C2 拆分：confirmed Prolog (3/3 seeds 0% N-H) vs exploratory ProofFOL (p=0.10)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"N-H 全文标注为 upper bound + classifier recall unknown 在 §4.1 方法段声明。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。WebSearch 验证。R21 R2 确认正确。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 4 篇全部加入 bib + 引用。R21 R2 逐条验证正确（V-STaR venue 需更新为 COLM 2024）。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n\n# === R22 resolved ===\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已从 references.bib 删除 kimina-prover 条目。\"\n  resolution_round: 22\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n\n# === Recurring issues (updated R23) ===\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 升级为 critical。建议补做 greedy eval 或提供 excluding-s43 sensitivity check。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 双 Reviewer 再次标记。论文在 §4.1 footnote 承认 'not strictly comparable'，并加了 excluding-s43 sentence，但仍纳入 pooled statistics。R1 标为 warning，R2 AGREE。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 in_progress。\"\n  - round: 23\n    reviewers: [1]\n    note: \"R23 R1-W4 再次标记：LOO 无法捕获联合必要性，建议讨论 Shapley values 关系。R2 AGREE 但认为 FOLIO 2-6 前提设定中高阶交互影响有限。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: []\n    note: \"R22 未单独提及。维持 info/in_progress。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N3 升级为 critical（reward magnitude 混淆需 constant-bonus control）。R2 REBUT 降为 warning：shuffled-ISR 已控制 magnitude 分布，问题在统计 power 而非设计逻辑。共识：warning。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 共识。~19 缩写 + 8 mode names。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 双 Reviewer 再次标记 (R2-W2, R1 AGREE)。ISR/ISR†/ISR* 符号不统一 + hacking mode 缩写过多。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查标记：pages 5-6 连续纯文本，pages 7-8 display items 堆积。\"\n  - round: 23\n    reviewers: [visual]\n    note: \"R23 视觉审查再次标记同样问题。pages 5-6 纯文本无视觉锚点，page 8 三个 display items 拥挤。建议 Table 2 前移。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [visual]\n    note: \"R22 视觉审查标记 Figure 1 轴标签约 7pt。\"\n  - round: 23\n    reviewers: [visual]\n    note: \"R23 视觉审查再次标记 Figure 2/3 内部文字接近可读性下限（7-8pt）。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。建议重新框定为 composition change 而非 prevalence increase。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 最强共识点。R1-N2 标为 critical：'compositional Goodhart effect' 标签下混合了显著（TS shift p<10⁻¹⁰）和不显著（N-H rate p=0.182）两个现象。R2 完全 AGREE。论文已改为 'compositional' 但仍需进一步区分这两个子发现。\"\n\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。C1 应以 3-seed 聚合指标表述。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。论文已标注 'for seed~42' + 3-seed '≤7% non-hacking'。可能已修复，待确认。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。ISR 核心价值退回到 mode-level breakdown。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W2 再次标记：Table 1 始终用 unmatched ISR，正文呈现不足。R2 AGREE。论文 Table 1 已有 '1.06×‡' 标注但不够显著。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 critical (Findings only)。R1 rebuts：empirical findings 足够。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R2-N2 再次标为 critical。R1 交叉 REBUT：LOO 标准但 ISR 定义+诊断发现有独立价值，EMNLP Findings 接受 applied contributions。共识：warning——novelty 有限但不致命，适合 Findings。\"\n\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。主文聚焦 CE/TS/PG 三主要 mode。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。主文 §4.5 已聚焦三主要 mode。可能已修复。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"[divergent] R2 标为 warning。R1 rebuts：Section 2 已有区分。共识 info。\"\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。维持 info/open。\"\n\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入 references.bib + related_work.tex。\"\n  resolution_round: 22\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。改为 'cross-dataset evidence'。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W6 再次标记。论文已改为 'cross-dataset evidence' 但未在 ProofFOL 结果旁明确标注 'upper bound due to coarser classification'。R2 AGREE。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。每 seed 仅 ~15 proved。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-N1/N3 再次关联此问题。论文已加 'per-seed n≈15 limits statistical power' caveat。R1 认为仍不够——需 power analysis。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 R1-W5 维持。R2 REBUT：SFT 目的是 pre-RL reference 而非 PR-matched control，100-step checkpoint 在 PR 更可比时仍展现早期 hacking。分歧但非关键。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: []\n    note: \"R23 未单独提及。维持 open/info，低优先级。\"\n\n# === New R23 issues ===\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足——需 power analysis 或增加 seeds\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 标为 critical (N1)。R2 AGREE 但认为 N=3 是 GRPO 文献标准实践。共识：论文需提供 power analysis 或对关键比较标注为 exploratory。与 v15-R12-N1 (resolved) 相关但进一步要求量化 power。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合 reward 需 constant-bonus control 排除 reward magnitude 混淆\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 标为 critical。R2 REBUT 降为 warning：shuffled-ISR 已部分控制 magnitude，问题在统计 power 而非设计逻辑。共识 warning。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与 C1-C2 通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2 标为 critical。R1 AGREE 但建议降为 warning——修复方向是调整 Abstract 措辞而非重做实验。共识 warning。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 方法论对比不充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2-W3，R1 AGREE。IPT 与 STA 研究问题高度重叠，应明确讨论方法论差异。\"\n\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题术语与 ISR 实际测量（component necessity）不完全匹配\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2-W4。R1 部分 AGREE：ISR 是 structural quality 的特定 operationalization。但 hacking taxonomy 已证明 low-ISR 对应多种结构退化，标题不需修改。共识 info。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失引用：Shapley values (Lundberg & Lee 2017) 作为 LOO 的自然泛化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1-W4 提出，R2 AGREE。讨论 LOO vs Shapley trade-off（计算成本 2ⁿ vs n）。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失引用：PRoSFI (Chen et al., 2026) + Interleaved Bonus (arXiv:2601.22642)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2 提出，R1 AGREE（如存在且相关应引用）。PRoSFI 将形式验证作为 process reward 引入 RL 训练，与 ISR-as-reward 实验直接相关。\"\n\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出约 15 行至第 9 页——可能违反 8 页限制\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2, visual]\n    note: \"R1 小问题标记 '8.1-8.2 页'。视觉审查 info 标记 'Section 5 延续至第 9 页上部约 1/4'。需确认 Conclusion 是否计入 8 页限制。若计入则违规。\""
  }
}
```

</details>

---


### Tool result

_source line 2175 · 2026-05-21T17:00:45.470899+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 18397}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2176 · 2026-05-21T17:03:05.906712+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "report": "# 审稿报告：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n\n**投稿目标**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 23 (Fresh Review)\n**Reviewer 编排**: R1 (方法严谨性 + 实验设计 + 统计声明) / R2 (新颖性 + 相关工作 + 写作质量 + 完整性)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的神经符号推理模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 量化求解器输入中各组件的必要性。论文在 Qwen3-4B + FOLIO 设定下展示两个主要发现：(C1) exec-only GRPO 训练导致隐性结构崩塌（ISR 下降而 prove rate 上升），SFT baseline 表明该退化与 GRPO 训练特异相关；(C2) 将 ISR 用作训练奖励时产生组合式 Goodhart 效应——hacking 从 conclusion embedding (CE) 转向 tautological shortcutting (TS)，但总体 hacking 率未显著降低（p=0.182）。跨逻辑（Prolog）和跨数据集（ProofFOL）证据支持部分泛化。\n\n---\n\n## Strengths\n\n**S1.** 填补 neurosymbolic RL 中缺乏结构质量诊断的真实空白。现有 prove rate 评估完全无法捕获论文所揭示的结构退化现象——ISR 214× 崩塌（seed 42）而 PR 同期从 32% 上升至 96%，这一对比具有说服力。[R1/R2 共识]\n\n**S2.** 实验设计严谨透明。含 SFT 控制组、shuffled-ISR 消融、多 reward 条件（6 种）、多 β 值 dose-response、3-5 seeds，且诚实报告 confound（premise-count 3.2×→1.06×）和统计局限（p=0.182, N=3）。[R1 主评]\n\n**S3.** 八种 hacking mode 分类法有独立参考价值，含定义、示例、prevalence 数据。Triple gaming (TSb) 和 query-as-fact gaming 等发现展示了 reward hacking 的多样性和创造性。[R1/R2 共识]\n\n**S4.** 可复现性良好。附录含完整超参数表、逐 seed 详细结果（Tables 7-10）、算法伪代码、分类器验证。承诺公开代码和数据。[R2 主评]\n\n**S5.** Cross-domain evidence（Prolog 3/3 seeds 0% non-hacking）为结构退化的普遍性提供有力支撑；ProofFOL 结果虽为 exploratory 但展示了 ISR 的 dataset-dependent 特性。[R1/R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical][framing] **Goodhart 效应声明与统计证据不匹配** [R1-N2, R2-W1; 最强共识]\nISR vs. Random 的 non-hacking rate 比较 Fisher p=0.182（不显著），而 TS gaming rate 比较 p=1.3×10⁻¹⁰（显著）。论文将\"gaming 类型分布改变\"（有显著统计支撑）和\"总体 hacking 率增加\"（无显著统计支撑）混合在 \"compositional Goodhart effect\" 标签下。Abstract/Intro 的 Goodhart framing 应明确区分这两个子发现，将核心声明限定为 \"ISR shifts gaming composition toward TS without significantly reducing overall hacking prevalence\"。\n\n**MF2** [critical][experiment] **N=3 seeds 统计效力不足以支撑多项核心声明** [R1-N1, R2-N1; 共识]\n3 seeds 标准差极大（如 PR=77±14%），多数比较 underpowered。Shuffled-ISR control 每 seed 仅 ~15 proved samples。论文未提供 power analysis。所有未达显著性的比较（包括 ISR vs. Random non-hacking, ProofFOL p=0.10）需明确标注为 exploratory，或补充 power analysis 说明 N=3 可检测的最小 effect size。R2 指出 N=3 在 GRPO 文献中属标准实践，不应作为硬性拒稿标准，但论文的 claim 强度需与统计效力匹配。\n\n### Should-Fix（影响评分）\n\n**SF1** [warning][framing] **Case study 标题与 C1-C2 通用声称之间 framing 矛盾** [R2-N1, R1 AGREE→warning]\nTitle 自限 \"A Case Study\"，但 C1-C2 使用通用方法论语言（\"STA as a diagnostic framework\"），Section 5 又退回 \"For practitioners in settings similar to ours\"。建议统一 framing——完全拥抱 case study 定位并在 Abstract/Contributions 中一致使用限定语。\n\n**SF2** [warning][framing] **LOO ablation 方法论新颖性有限** [R2-N2 critical, R1 REBUT→warning]\nLOO 是 mutation testing 最基础的变体（DeMillo et al., 1978）。R2 认为不足以支撑 Main Conference；R1 反驳称 EMNLP Findings 接受 applied/empirical contributions，且类似 reward hacking 论文（Helff 2026, Kim 2026）方法也非全新。共识降级为 warning：论文应将贡献重心从\"提出 STA\"转移到\"通过 STA 揭示的经验发现\"。\n\n**SF3** [warning][experiment] **单模型 family (Qwen3-4B) 限制泛化性** [R2-N3 critical, R1 AGREE→warning]\nLLaMA-3.2-3B 是 cold-start failure 不构成跨模型验证。论文已在 title/limitations 中加限定语。R1 认为 case study 定位和 ProofFOL 证据提供了部分缓解，共识为 warning。\n\n**SF4** [warning][experiment] **乘法耦合 reward 引入 reward magnitude 混淆** [R1-N3 critical, R2 REBUT→warning]\nr = r_exec · (1 + β · ISR) 使 ISR-rewarded 模型 reward magnitude 更大。R2 反驳：shuffled-ISR 使用相同乘法形式但 87% non-hacking，方向性证据表明结构信号而非 magnitude 驱动。共识 warning——建议补充 constant-bonus control 或 reward magnitude 分布分析。\n\n**SF5** [warning][experiment] **Seed 43 协议偏差（T=0.7 sampling）污染 pooled results** [R1-W1, R2 AGREE]\nN=3 时一个 T=0.7 seed 占 33%。论文在 footnote 中承认 \"not strictly comparable\" 并加了 excluding-s43 sentence，但仍纳入 pooled 统计。需提供完整的 excluding-s43 sensitivity analysis。\n\n**SF6** [warning][method] **Premise-count confound 正文呈现不足** [R1-W2, R2 AGREE]\nISR 原始优势 3.2× 在 matching 后缩减至 1.06×（~97% 差异来自 premise 数量），但 Table 1 始终使用 unmatched ISR。建议 Table 1 增加 matched ISR 列或在首次报告时给出对比。\n\n**SF7** [warning][method] **与 Helff et al. (2026) IPT 方法论对比不充分** [R2-W3, R1 AGREE]\nIPT (Isomorphic Perturbation Testing) 与 STA 研究问题高度重叠。论文仅一句话提及。建议增加 LOO ablation vs isomorphic perturbation 的方法论对比讨论。\n\n**SF8** [warning][experiment] **ProofFOL 分类器不对称** [R1-W6, R2 AGREE]\nFOLIO 使用 8-mode 分类器，ProofFOL 仅排除 TS+CE（2 modes），non-hacking rate 不可直接比较。建议在 ProofFOL 结果旁标注 \"upper bound due to coarser classification\"。\n\n**SF9** [warning][format] **正文可能溢出 8 页限制** [R1/R2/Visual 共识]\nR1 估计正文约 8.1-8.2 页，Section 5 (Discussion and Conclusion) 溢出约 15 行至第 9 页。视觉审查确认 Section 5 从第 8 页底部延续至第 9 页上部约 1/4。Conclusion 属正文（计入 8 页限制），需压缩。\n\n**SF10** [warning][writing] **缩写/术语密度过高** [R2-W2, R1 AGREE; 历史遗留问题]\nSTA, ISR, ISR*, GRPO, PR, CE, TS, TSa, TSb, PG, N-H, LOO, SFT, CMH 等约 15+ 缩写，加上 8 种 hacking mode 名称。ISR/ISR†/ISR* 符号不统一。建议提供缩写速查表，在关键段落展开部分缩写。\n\n### Minor Issues\n\n- Table 1 脚注过长（5 行），影响可读性\n- FOLIO bib entry 年份不一致（bib=2024, OpenAlex/arXiv=2022）\n- Figure 1 灰度可读性差，建议增加 line style\n- Section 5 实践建议缺少过渡段\n- Table 1 统计显著性标注格式不一致\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Goodhart framing 过强**：p=0.182 不显著，核心声明应限定为 composition shift（MF1）—— 两位 Reviewer 最强共识\n2. **统计效力有限**：N=3 seeds 限制 claim 强度，关键比较需标注 exploratory 或提供 power analysis（MF2）\n3. **Overall 3.0 (Findings)**：技术执行扎实但 novelty/scope 不足以达到 Main Conference\n4. **Seed 43 偏差需 sensitivity analysis**（SF5）\n5. **Premise-count confound 正文呈现不足**（SF6）\n6. **缩写密度过高**（SF10）\n7. **ProofFOL 分类器不对称需标注**（SF8）\n8. **IPT 对比缺失**（SF7）\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **乘法耦合混淆严重程度**：R1 标为 critical（需 constant-bonus control），R2 标为 warning（shuffled-ISR 已部分控制）→ 共识 warning，但 R1 认为补充实验更令人信服\n2. **LOO 新颖性是否致命**：R2 标为 critical（Findings only），R1 反驳称 applied contributions 有独立价值 → 共识 warning\n3. **ISR Goodhart 可预期性**：R2 认为概念上可预期降低贡献，R1 反驳称具体机制（CE→TS shift, bimodal ISR, non-monotone dose-response）有独立实证价值 → 未达共识，但不影响整体评分\n4. **SFT baseline 公平性**：R1 认为 PR 差异 7× 是根本缺陷（100-step 单 seed 不够），R2 认为 SFT 目的是 pre-RL reference 而非 PR-matched control → 轻微分歧\n\n---\n\n## Questions for Authors\n\n1. 能否提供 power analysis，说明 N=3 seeds 在什么 effect size 下达到 80% power？\n2. 排除 Seed 43（T=0.7 sampling）后，Table 1 各 pooled 结果如何变化？\n3. 是否考虑过 premise-count-normalized ISR 作为 Table 1 主指标？\n4. 是否考虑过 constant-bonus control（r = r_exec · (1 + β · c), c=常数）来排除 reward magnitude 混淆？\n5. 8 种 hacking mode 分类器的 recall 如何估计？已知 Prolog 场景中 strict classifier 存在严重 false negatives。\n6. \"Structural degeneration\" 与 \"component redundancy\" 的边界在哪？ISR=0.5 的 formalization 是否一定是 \"degenerate\"？\n\n---\n\n## Missing References\n\n1. **Shapley values (Lundberg & Lee, 2017)**：LOO 的自然泛化，可处理组件交互效应。讨论 LOO vs Shapley 的 trade-off（计算成本 2ⁿ vs n）可增强方法论讨论。[R1 提出, R2 AGREE]\n2. **PRoSFI — Chen et al. (2026), arXiv:2603.29500**：将形式验证作为 process reward 引入 RL 训练，与 ISR-as-reward 实验直接相关。[R2 提出, R1 AGREE]\n3. **\"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\" (arXiv:2601.22642)**：将形式逻辑验证动态交织到生成过程中。[R2 提出, R1 AGREE]\n\n注：R1 建议引用 Ng et al. (1999) potential-based shaping，R2 指出该引用已在 references.bib 和 related_work.tex Section 2 首句中出现（R1 事实性错误）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2 warnings, 6 info）\n\n**Warnings:**\n1. **Pages 5-6 连续纯文本**：§4.1-§4.3 实验叙述段无任何 figure/table/equation 穿插，审稿人易失去视觉锚点。建议将关键数字提炼为 inline 表格。\n2. **Page 8 拥挤**：Figure 2 + Figure 3 + Table 2 挤在同一页，内部文字（axis label, legend）接近可读性下限（7-8pt）。与 pages 5-6 纯文本形成不均匀节奏。建议 Table 2 前移。\n\n**Info:**\n- Section 5 从第 8 页底延续至第 9 页上部约 1/4（与 SF9 页数溢出问题一致）\n- Figure 1 单栏宽度，视觉冲击力有限\n- Figure 2/3 被压缩到单栏宽度，tick label 和 legend 字号偏小\n- Table 1 排版优秀（booktabs 风格、最优值加粗、caption 自包含）\n- Algorithm 1 提供良好视觉结构\n- Appendix Tables 7-10 数据密集但功能可接受\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings（可被 Findings 接收）**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉相关文献，仔细审读全文含附录）\n\n**理由:**\n\n论文填补了 neurosymbolic RL 中缺乏结构质量诊断的真实空白，ISR 揭示的 prove rate 与结构质量之间的隐性脱钩（214× ISR 崩塌 vs PR 上升）具有说服力，hacking taxonomy 有独立参考价值。实验设计在 case study 范围内严谨透明。\n\n然而，以下因素限制了论文达到 Main Conference (4.0) 的水平：\n- **统计支撑不足**：核心 Goodhart 声明（C2）的直接统计检验不显著（p=0.182），N=3 seeds 导致多项比较 underpowered\n- **方法论新颖性有限**：LOO ablation 是 50 年老技术的新场景应用，真正贡献在实证发现\n- **泛化范围窄**：仅 Qwen3-4B + FOLIO/ProofFOL，无成功的跨模型验证\n- **Framing 不一致**：title \"Case Study\" 与 contributions 通用语言之间的张力\n\n论文适合 EMNLP 2026 Findings：技术执行扎实，发现有价值，但 novelty 和 scope 不足以竞争 Main Conference。\n\n**建议修改优先级:**\n1. [高] MF1: 区分 Goodhart composition shift（显著）和 prevalence claim（不显著）\n2. [高] MF2: 对关键比较标注 exploratory 或提供 power analysis\n3. [中] SF9: 压缩正文至 8 页\n4. [中] SF1: 统一 case study framing\n5. [中] SF5: 提供 excluding-s43 sensitivity analysis\n6. [中] SF6: 正文增加 premise-count-matched ISR 对比\n7. [低] SF7/SF10/Minor issues\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"compositional Goodhart effect\" 已较前版改善，但仍需在 p=0.182 旁注明 composition shift 有显著支撑而 prevalence reduction 无显著支撑\n- \"whose diagnostic value is realized through mode-level analysis\" 表述好，准确限定了 ISR scalar 的作用\n\n### Introduction\n- 逻辑流清晰：blind spot → component necessity testing → diagnostic → Goodhart\n- L28 \"99.5% degradation\" 已标注 seed~42，L29 \"all 3 seeds: ≤7%\" 提供 3-seed 证据，改善到位\n- C2 \"compositional Goodhart effect: TS amplification without significant prevalence reduction (p=0.182)\" 措辞准确\n\n### Method (Section 3)\n- Algorithm 1 伪代码清晰简洁\n- §3.2 premise-count confound 讨论（3.2×→1.06×）位置正确，但首次在此出现、Table 1 未反映形成呈现落差\n- LOO independence assumption (§3.2 末段) 方向正确但缺少量化\n\n### Experiments (Section 4)\n- §4.1 Statistical considerations 段提供了必要的 N=3 framework\n- §4.2 ISR as Diagnostic：collapse trajectory (214× for s42) 是最强证据\n- §4.3 Goodhart Effects：最弱章节——核心比较 p=0.182 但叙述语气仍偏强\n- §4.4 Cross-Domain：Prolog 结果（3/3 seeds 0% N-H）有力；ProofFOL 结果（p=0.10）标注 exploratory 恰当\n- Table 1 设计好（双行 ISR 3/5-seed），但 ISR* 列 \"1.06×‡\" 在 5-seed 行无对应 matched 值\n\n### Related Work (Section 2)\n- 覆盖面广（neurosymbolic, process rewards, Goodhart, mutation testing）\n- 与 Kim et al. (2026) 区分存在（inference-time vs training-time）但可更显著\n- 缺少与 Helff et al. (2026) IPT 的方法论对比\n\n### Discussion/Conclusion (Section 5)\n- Observer/optimizer asymmetry 总结精准\n- 实践建议有价值但缺少过渡\n- 可能溢出 8 页限制\n\n### Limitations (Section 6)\n- 覆盖充分：single model, 3 seeds, ISR≠semantic faithfulness, data scale, temporal snapshot\n- LLaMA-3.2-3B cold-start 作为 capability threshold 讨论得当\n\n### Appendix\n- 详尽且有组织：hyperparams, algorithm, extended discussion, hacking modes, per-seed results, O(1) ablation, LLaMA cold-start\n- PG/TSb 发现和分类器验证增强了主文可信度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "report": "# 审稿报告：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n\n**投稿目标**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 23 (Fresh Review)\n**Reviewer 编排**: R1 (方法严谨性 + 实验设计 + 统计声明) / R2 (新颖性 + 相关工作 + 写作质量 + 完整性)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的神经符号推理模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 量化求解器输入中各组件的必要性。论文在 Qwen3-4B + FOLIO 设定下展示两个主要发现：(C1) exec-only GRPO 训练导致隐性结构崩塌（ISR 下降而 prove rate 上升），SFT baseline 表明该退化与 GRPO 训练特异相关；(C2) 将 ISR 用作训练奖励时产生组合式 Goodhart 效应——hacking 从 conclusion embedding (CE) 转向 tautological shortcutting (TS)，但总体 hacking 率未显著降低（p=0.182）。跨逻辑（Prolog）和跨数据集（ProofFOL）证据支持部分泛化。\n\n---\n\n## Strengths\n\n**S1.** 填补 neurosymbolic RL 中缺乏结构质量诊断的真实空白。现有 prove rate 评估完全无法捕获论文所揭示的结构退化现象——ISR 214× 崩塌（seed 42）而 PR 同期从 32% 上升至 96%，这一对比具有说服力。[R1/R2 共识]\n\n**S2.** 实验设计严谨透明。含 SFT 控制组、shuffled-ISR 消融、多 reward 条件（6 种）、多 β 值 dose-response、3-5 seeds，且诚实报告 confound（premise-count 3.2×→1.06×）和统计局限（p=0.182, N=3）。[R1 主评]\n\n**S3.** 八种 hacking mode 分类法有独立参考价值，含定义、示例、prevalence 数据。Triple gaming (TSb) 和 query-as-fact gaming 等发现展示了 reward hacking 的多样性和创造性。[R1/R2 共识]\n\n**S4.** 可复现性良好。附录含完整超参数表、逐 seed 详细结果（Tables 7-10）、算法伪代码、分类器验证。承诺公开代码和数据。[R2 主评]\n\n**S5.** Cross-domain evidence（Prolog 3/3 seeds 0% non-hacking）为结构退化的普遍性提供有力支撑；ProofFOL 结果虽为 exploratory 但展示了 ISR 的 dataset-dependent 特性。[R1/R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical][framing] **Goodhart 效应声明与统计证据不匹配** [R1-N2, R2-W1; 最强共识]\nISR vs. Random 的 non-hacking rate 比较 Fisher p=0.182（不显著），而 TS gaming rate 比较 p=1.3×10⁻¹⁰（显著）。论文将\"gaming 类型分布改变\"（有显著统计支撑）和\"总体 hacking 率增加\"（无显著统计支撑）混合在 \"compositional Goodhart effect\" 标签下。Abstract/Intro 的 Goodhart framing 应明确区分这两个子发现，将核心声明限定为 \"ISR shifts gaming composition toward TS without significantly reducing overall hacking prevalence\"。\n\n**MF2** [critical][experiment] **N=3 seeds 统计效力不足以支撑多项核心声明** [R1-N1, R2-N1; 共识]\n3 seeds 标准差极大（如 PR=77±14%），多数比较 underpowered。Shuffled-ISR control 每 seed 仅 ~15 proved samples。论文未提供 power analysis。所有未达显著性的比较（包括 ISR vs. Random non-hacking, ProofFOL p=0.10）需明确标注为 exploratory，或补充 power analysis 说明 N=3 可检测的最小 effect size。R2 指出 N=3 在 GRPO 文献中属标准实践，不应作为硬性拒稿标准，但论文的 claim 强度需与统计效力匹配。\n\n### Should-Fix（影响评分）\n\n**SF1** [warning][framing] **Case study 标题与 C1-C2 通用声称之间 framing 矛盾** [R2-N1, R1 AGREE→warning]\nTitle 自限 \"A Case Study\"，但 C1-C2 使用通用方法论语言（\"STA as a diagnostic framework\"），Section 5 又退回 \"For practitioners in settings similar to ours\"。建议统一 framing——完全拥抱 case study 定位并在 Abstract/Contributions 中一致使用限定语。\n\n**SF2** [warning][framing] **LOO ablation 方法论新颖性有限** [R2-N2 critical, R1 REBUT→warning]\nLOO 是 mutation testing 最基础的变体（DeMillo et al., 1978）。R2 认为不足以支撑 Main Conference；R1 反驳称 EMNLP Findings 接受 applied/empirical contributions，且类似 reward hacking 论文（Helff 2026, Kim 2026）方法也非全新。共识降级为 warning：论文应将贡献重心从\"提出 STA\"转移到\"通过 STA 揭示的经验发现\"。\n\n**SF3** [warning][experiment] **单模型 family (Qwen3-4B) 限制泛化性** [R2-N3 critical, R1 AGREE→warning]\nLLaMA-3.2-3B 是 cold-start failure 不构成跨模型验证。论文已在 title/limitations 中加限定语。R1 认为 case study 定位和 ProofFOL 证据提供了部分缓解，共识为 warning。\n\n**SF4** [warning][experiment] **乘法耦合 reward 引入 reward magnitude 混淆** [R1-N3 critical, R2 REBUT→warning]\nr = r_exec · (1 + β · ISR) 使 ISR-rewarded 模型 reward magnitude 更大。R2 反驳：shuffled-ISR 使用相同乘法形式但 87% non-hacking，方向性证据表明结构信号而非 magnitude 驱动。共识 warning——建议补充 constant-bonus control 或 reward magnitude 分布分析。\n\n**SF5** [warning][experiment] **Seed 43 协议偏差（T=0.7 sampling）污染 pooled results** [R1-W1, R2 AGREE]\nN=3 时一个 T=0.7 seed 占 33%。论文在 footnote 中承认 \"not strictly comparable\" 并加了 excluding-s43 sentence，但仍纳入 pooled 统计。需提供完整的 excluding-s43 sensitivity analysis。\n\n**SF6** [warning][method] **Premise-count confound 正文呈现不足** [R1-W2, R2 AGREE]\nISR 原始优势 3.2× 在 matching 后缩减至 1.06×（~97% 差异来自 premise 数量），但 Table 1 始终使用 unmatched ISR。建议 Table 1 增加 matched ISR 列或在首次报告时给出对比。\n\n**SF7** [warning][method] **与 Helff et al. (2026) IPT 方法论对比不充分** [R2-W3, R1 AGREE]\nIPT (Isomorphic Perturbation Testing) 与 STA 研究问题高度重叠。论文仅一句话提及。建议增加 LOO ablation vs isomorphic perturbation 的方法论对比讨论。\n\n**SF8** [warning][experiment] **ProofFOL 分类器不对称** [R1-W6, R2 AGREE]\nFOLIO 使用 8-mode 分类器，ProofFOL 仅排除 TS+CE（2 modes），non-hacking rate 不可直接比较。建议在 ProofFOL 结果旁标注 \"upper bound due to coarser classification\"。\n\n**SF9** [warning][format] **正文可能溢出 8 页限制** [R1/R2/Visual 共识]\nR1 估计正文约 8.1-8.2 页，Section 5 (Discussion and Conclusion) 溢出约 15 行至第 9 页。视觉审查确认 Section 5 从第 8 页底部延续至第 9 页上部约 1/4。Conclusion 属正文（计入 8 页限制），需压缩。\n\n**SF10** [warning][writing] **缩写/术语密度过高** [R2-W2, R1 AGREE; 历史遗留问题]\nSTA, ISR, ISR*, GRPO, PR, CE, TS, TSa, TSb, PG, N-H, LOO, SFT, CMH 等约 15+ 缩写，加上 8 种 hacking mode 名称。ISR/ISR†/ISR* 符号不统一。建议提供缩写速查表，在关键段落展开部分缩写。\n\n### Minor Issues\n\n- Table 1 脚注过长（5 行），影响可读性\n- FOLIO bib entry 年份不一致（bib=2024, OpenAlex/arXiv=2022）\n- Figure 1 灰度可读性差，建议增加 line style\n- Section 5 实践建议缺少过渡段\n- Table 1 统计显著性标注格式不一致\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Goodhart framing 过强**：p=0.182 不显著，核心声明应限定为 composition shift（MF1）—— 两位 Reviewer 最强共识\n2. **统计效力有限**：N=3 seeds 限制 claim 强度，关键比较需标注 exploratory 或提供 power analysis（MF2）\n3. **Overall 3.0 (Findings)**：技术执行扎实但 novelty/scope 不足以达到 Main Conference\n4. **Seed 43 偏差需 sensitivity analysis**（SF5）\n5. **Premise-count confound 正文呈现不足**（SF6）\n6. **缩写密度过高**（SF10）\n7. **ProofFOL 分类器不对称需标注**（SF8）\n8. **IPT 对比缺失**（SF7）\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **乘法耦合混淆严重程度**：R1 标为 critical（需 constant-bonus control），R2 标为 warning（shuffled-ISR 已部分控制）→ 共识 warning，但 R1 认为补充实验更令人信服\n2. **LOO 新颖性是否致命**：R2 标为 critical（Findings only），R1 反驳称 applied contributions 有独立价值 → 共识 warning\n3. **ISR Goodhart 可预期性**：R2 认为概念上可预期降低贡献，R1 反驳称具体机制（CE→TS shift, bimodal ISR, non-monotone dose-response）有独立实证价值 → 未达共识，但不影响整体评分\n4. **SFT baseline 公平性**：R1 认为 PR 差异 7× 是根本缺陷（100-step 单 seed 不够），R2 认为 SFT 目的是 pre-RL reference 而非 PR-matched control → 轻微分歧\n\n---\n\n## Questions for Authors\n\n1. 能否提供 power analysis，说明 N=3 seeds 在什么 effect size 下达到 80% power？\n2. 排除 Seed 43（T=0.7 sampling）后，Table 1 各 pooled 结果如何变化？\n3. 是否考虑过 premise-count-normalized ISR 作为 Table 1 主指标？\n4. 是否考虑过 constant-bonus control（r = r_exec · (1 + β · c), c=常数）来排除 reward magnitude 混淆？\n5. 8 种 hacking mode 分类器的 recall 如何估计？已知 Prolog 场景中 strict classifier 存在严重 false negatives。\n6. \"Structural degeneration\" 与 \"component redundancy\" 的边界在哪？ISR=0.5 的 formalization 是否一定是 \"degenerate\"？\n\n---\n\n## Missing References\n\n1. **Shapley values (Lundberg & Lee, 2017)**：LOO 的自然泛化，可处理组件交互效应。讨论 LOO vs Shapley 的 trade-off（计算成本 2ⁿ vs n）可增强方法论讨论。[R1 提出, R2 AGREE]\n2. **PRoSFI — Chen et al. (2026), arXiv:2603.29500**：将形式验证作为 process reward 引入 RL 训练，与 ISR-as-reward 实验直接相关。[R2 提出, R1 AGREE]\n3. **\"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\" (arXiv:2601.22642)**：将形式逻辑验证动态交织到生成过程中。[R2 提出, R1 AGREE]\n\n注：R1 建议引用 Ng et al. (1999) potential-based shaping，R2 指出该引用已在 references.bib 和 related_work.tex Section 2 首句中出现（R1 事实性错误）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2 warnings, 6 info）\n\n**Warnings:**\n1. **Pages 5-6 连续纯文本**：§4.1-§4.3 实验叙述段无任何 figure/table/equation 穿插，审稿人易失去视觉锚点。建议将关键数字提炼为 inline 表格。\n2. **Page 8 拥挤**：Figure 2 + Figure 3 + Table 2 挤在同一页，内部文字（axis label, legend）接近可读性下限（7-8pt）。与 pages 5-6 纯文本形成不均匀节奏。建议 Table 2 前移。\n\n**Info:**\n- Section 5 从第 8 页底延续至第 9 页上部约 1/4（与 SF9 页数溢出问题一致）\n- Figure 1 单栏宽度，视觉冲击力有限\n- Figure 2/3 被压缩到单栏宽度，tick label 和 legend 字号偏小\n- Table 1 排版优秀（booktabs 风格、最优值加粗、caption 自包含）\n- Algorithm 1 提供良好视觉结构\n- Appendix Tables 7-10 数据密集但功能可接受\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings（可被 Findings 接收）**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉相关文献，仔细审读全文含附录）\n\n**理由:**\n\n论文填补了 neurosymbolic RL 中缺乏结构质量诊断的真实空白，ISR 揭示的 prove rate 与结构质量之间的隐性脱钩（214× ISR 崩塌 vs PR 上升）具有说服力，hacking taxonomy 有独立参考价值。实验设计在 case study 范围内严谨透明。\n\n然而，以下因素限制了论文达到 Main Conference (4.0) 的水平：\n- **统计支撑不足**：核心 Goodhart 声明（C2）的直接统计检验不显著（p=0.182），N=3 seeds 导致多项比较 underpowered\n- **方法论新颖性有限**：LOO ablation 是 50 年老技术的新场景应用，真正贡献在实证发现\n- **泛化范围窄**：仅 Qwen3-4B + FOLIO/ProofFOL，无成功的跨模型验证\n- **Framing 不一致**：title \"Case Study\" 与 contributions 通用语言之间的张力\n\n论文适合 EMNLP 2026 Findings：技术执行扎实，发现有价值，但 novelty 和 scope 不足以竞争 Main Conference。\n\n**建议修改优先级:**\n1. [高] MF1: 区分 Goodhart composition shift（显著）和 prevalence claim（不显著）\n2. [高] MF2: 对关键比较标注 exploratory 或提供 power analysis\n3. [中] SF9: 压缩正文至 8 页\n4. [中] SF1: 统一 case study framing\n5. [中] SF5: 提供 excluding-s43 sensitivity analysis\n6. [中] SF6: 正文增加 premise-count-matched ISR 对比\n7. [低] SF7/SF10/Minor issues\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"compositional Goodhart effect\" 已较前版改善，但仍需在 p=0.182 旁注明 composition shift 有显著支撑而 prevalence reduction 无显著支撑\n- \"whose diagnostic value is realized through mode-level analysis\" 表述好，准确限定了 ISR scalar 的作用\n\n### Introduction\n- 逻辑流清晰：blind spot → component necessity testing → diagnostic → Goodhart\n- L28 \"99.5% degradation\" 已标注 seed~42，L29 \"all 3 seeds: ≤7%\" 提供 3-seed 证据，改善到位\n- C2 \"compositional Goodhart effect: TS amplification without significant prevalence reduction (p=0.182)\" 措辞准确\n\n### Method (Section 3)\n- Algorithm 1 伪代码清晰简洁\n- §3.2 premise-count confound 讨论（3.2×→1.06×）位置正确，但首次在此出现、Table 1 未反映形成呈现落差\n- LOO independence assumption (§3.2 末段) 方向正确但缺少量化\n\n### Experiments (Section 4)\n- §4.1 Statistical considerations 段提供了必要的 N=3 framework\n- §4.2 ISR as Diagnostic：collapse trajectory (214× for s42) 是最强证据\n- §4.3 Goodhart Effects：最弱章节——核心比较 p=0.182 但叙述语气仍偏强\n- §4.4 Cross-Domain：Prolog 结果（3/3 seeds 0% N-H）有力；ProofFOL 结果（p=0.10）标注 exploratory 恰当\n- Table 1 设计好（双行 ISR 3/5-seed），但 ISR* 列 \"1.06×‡\" 在 5-seed 行无对应 matched 值\n\n### Related Work (Section 2)\n- 覆盖面广（neurosymbolic, process rewards, Goodhart, mutation testing）\n- 与 Kim et al. (2026) 区分存在（inference-time vs training-time）但可更显著\n- 缺少与 Helff et al. (2026) IPT 的方法论对比\n\n### Discussion/Conclusion (Section 5)\n- Observer/optimizer asymmetry 总结精准\n- 实践建议有价值但缺少过渡\n- 可能溢出 8 页限制\n\n### Limitations (Section 6)\n- 覆盖充分：single model, 3 seeds, ISR≠semantic faithfulness, data scale, temporal snapshot\n- LLaMA-3.2-3B cold-start 作为 capability threshold 讨论得当\n\n### Appendix\n- 详尽且有组织：hyperparams, algorithm, extended discussion, hacking modes, per-seed results, O(1) ablation, LLaMA cold-start\n- PG/TSb 发现和分类器验证增强了主文可信度"
  }
}
```

</details>

---


### Tool result

_source line 2177 · 2026-05-21T17:03:10.173883+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4267
}
```

</details>

---


### Assistant

_source line 2178 · 2026-05-21T17:03:17.454487+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **评分**: 3.0 — Findings（可被 Findings 接收）
- **两位 Reviewer 一致**，无评分分歧
- **2 个 Must-Fix**: (1) Goodhart framing 与 p=0.182 统计证据不匹配——需区分 composition shift（显著）和 prevalence claim（不显著）；(2) N=3 seeds 统计效力不足——需 power analysis 或标注 exploratory
- **10 个 Should-Fix**: case study framing 矛盾、LOO 新颖性有限、单模型泛化、乘法耦合混淆、Seed 43 偏差、premise-count confound 呈现、IPT 对比缺失、ProofFOL 分类器不对称、页数溢出、缩写密度
- **Issue Tracker 已更新**: 9 个新增/更新条目（round 23）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 192

## Round 192

2 recorded events


### User

_source line 2179 · 2026-05-21T17:03:20.096357+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1 (seeds)**: AGREE — 统计效力不足但 N=3 是 GRPO 文献标准
- **N2 (Goodhart 统计)**: AGREE — p=0.182 不显著，与我 R2-W1 一致
- **N3 (乘法耦合)**: REBUT — Shuffled-ISR 控制在设计上合理（87% vs 18%），问题是 power 不足而非设计错误，建议降为 warning
- **W1-W4, W6**: 全部 AGREE
- **W5 (SFT 对比)**: REBUT — SFT 用途是无 RL 控制而非性能对比，100-step checkpoint 进一步支持论点
- **Ng et al. (1999)**: REBUT — R1 事实性错误，论文已引用

两位 Reviewer 共识：Overall 3.0 (Findings)，Goodhart 声明需弱化，单模型泛化不足，方法论新颖性有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2180 · 2026-05-21T17:03:29.836191+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结：**

- **Overall: 3.0 — Findings**（双 Reviewer 一致）
- **2 个 Must-Fix**：(1) Goodhart framing 与 p=0.182 不匹配（最强共识），(2) N=3 统计效力不足
- **10 个 Should-Fix**：case study framing 矛盾、LOO 新颖性有限、单模型泛化、乘法耦合混淆、Seed 43 偏差、premise-count confound 呈现、IPT 对比缺失、ProofFOL 分类器不对称、页数溢出、缩写密度
- **Issue Tracker 已同步更新**（round 23，新增 8 条 open issues）
- **视觉审查已完成**（2 warnings: display items 分布不均 + page 8 拥挤）
- **外部审稿**：未配置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 193

## Round 193

64 recorded events


### User

_source line 2181 · 2026-05-21T17:21:40.591562+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2182 · 2026-05-21T17:21:49.933557+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-21T17:21:49.984617+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2184 · 2026-05-21T17:21:55.710928+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2185 · 2026-05-21T17:21:55.761551+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2186 · 2026-05-21T17:21:59.781443+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2187 · 2026-05-21T17:21:59.782006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2188 · 2026-05-21T17:22:03.550817+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 2189 · 2026-05-21T17:22:04.105131+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2190 · 2026-05-21T17:22:04.205980+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (211 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 655
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-21T17:22:04.206347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-21T17:22:09.533295+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2193 · 2026-05-21T17:22:10.547948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 author guidelines page limit formatting requirements site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 author guidelines page limit formatting requirements site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 2194 · 2026-05-21T17:22:12.454919+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2195 · 2026-05-21T17:22:12.706496+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2196 · 2026-05-21T17:22:12.707186+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2197 · 2026-05-21T17:22:12.807897+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2198 · 2026-05-21T17:22:16.066507+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 using the ACL Rolling Review system:

## Submission Process

EMNLP 2026 uses ACL Rolling Review (ARR) as its reviewing system, with a two-step process: authors submit articles to ARR for review, then commit their reviewed articles to the conference where Senior Area Chairs and Program Chairs make acceptance decisions.

## Paper Format Requirements

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. A mandatory Limitations section is requir
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6533
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-21T17:22:17.071876+00:00_

Web search results for query: "ARR 2026 author guidelines page limit formatting requirements site:aclrollingreview.org"

Links: [{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Changelog","url":"http://aclrollingreview.org/changelog"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results from the ACL Rolling Review website, here are the key formatting requirements and page limit information for ARR 2026:

**Page Limits:**
All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

**Formatting Requirements:**
The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template. The paper follows ACL formatting, and you are encouraged to use the ACL pubcheck tool to check for common problems.

**Template Note:**
There is an official Overleaf template, and this template has a [review] setting that must be on for the submission.

**Recent Updates:**
ACLPUB formatting guidelines were updated in January 2025 with clarifications on font size in figures and tables, placement of limitations and ethical considerations sections, and two-column formatting of appendices.

**Limitations and Ethics Sections:**
Ethics sections will not count towards the page limit.

For more detailed information, the Authors Guidelines page at aclrollingreview.org/authors provide
…[truncated 154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6523
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-21T17:22:27.264722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2201 · 2026-05-21T17:22:27.315484+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\input{checklist}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2202 · 2026-05-21T17:22:27.315996+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2203 · 2026-05-21T17:22:27.366677+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2204 · 2026-05-21T17:22:30.731603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2205 · 2026-05-21T17:22:30.732037+00:00_

1	\begin{abstract}
2	We study structural degeneration in neurosymbolic reasoning trained with GRPO: models achieve high prove rates while most outputs embed the conclusion among premises---a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic applying leave-one-out necessity testing to solver inputs; the fraction of necessary components yields the \emph{Intensional Structural Reward} (ISR), whose diagnostic value is realized through mode-level analysis.
4	As a diagnostic, component-necessity testing reveals a collapse trajectory hidden from prove rate: ISR falls to near-zero over training while prove rate rises, with each seed converging to a qualitatively different hacking mode.
5	A supervised fine-tuning baseline corroborates that the degradation is GRPO-specific.
6	When repurposed as a training reward, ISR exhibits a compositional Goodhart effect: the composition of hacking modes shifts significantly from conclusion embedding to tautological shortcutting ($p{<}10^{-15}$), but overall hacking prevalence does not decrease ($p{=}0.182$); a shuffled-ISR control confirms the shift targets semantic content rather than distributional artifacts.
7	Cross-logic (Prolog) and cross-dataset (ProofFOL) evidence confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2206 · 2026-05-21T17:22:30.982971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2207 · 2026-05-21T17:22:31.384339+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalizatio
…[truncated 4468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2208 · 2026-05-21T17:22:31.585207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2209 · 2026-05-21T17:22:31.585666+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 4408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2210 · 2026-05-21T17:22:36.305761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2211 · 2026-05-21T17:22:36.658177+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 15600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2212 · 2026-05-21T17:22:36.658601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2213 · 2026-05-21T17:22:37.311010+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; \citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.
12	\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
13	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural s
…[truncated 2434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 2214 · 2026-05-21T17:22:37.311382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2215 · 2026-05-21T17:22:37.512262+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals near-complete collapse under exec-only GRPO (e.g., $214\times$ for seed~42) that PR hides, while SFT results are consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}).
5	Cross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\S\ref{sec:crosslogic}).
6	Repurposed as a reward, ISR produces a compositional Goodhart effect: on FOLIO, it shifts hacking from CE to TS in 3 of 5 seeds (supplementary CMH $p{<}10^{-15}$; two seeds retain ${\sim}55\%$ non-hacking) without significantly reducing overall hacking prevalence ($p{=}0.182$); on ProofFOL, beneficial instability yields 76.8\% vs.\ 17.4\% non-hacking (upper bound; \S\ref{sec:setup}) ($p{=}0.10$).
7	Deconfounding reduces the sole apparent ISR reward advantage to $1.06\times$; a shuffled-ISR control confirms that semantic content, not distributional shape, drives the compositional shift (\S\ref{sec:goodhart}).
8	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
9	
10	For practitioners in similar settings (\S\ref{sec:limitations}): evaluate with ISR and component count jointly (not PR alone), report multi-seed results, and use ISR for post-hoc diagnosis only---any dose induces gaming or collapse when optimized (Appendix~\ref{app:practical-guidelines}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 2216 · 2026-05-21T17:22:37.562793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2217 · 2026-05-21T17:22:37.613396+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.
5	Cross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\text{PR}{=}16\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\ref{app:llama-coldstart}), establishing a capability threshold that limits STA's applicability.
6	Three seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.
7	At our scale (500 training / 100 evaluation examples), non-hacking rates of ${\sim}5\%$ correspond to ${\sim}5$ samples, limiting mode-level precision.
8	ISR quantifies syntactic component necessity, not semantic faithfulness ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2218 · 2026-05-21T17:22:42.586312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2219 · 2026-05-21T17:22:42.989318+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 46475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2220 · 2026-05-21T17:22:42.989858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2221 · 2026-05-21T17:22:43.541902+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2222 · 2026-05-21T17:22:43.852639+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-21T17:22:44.112279+00:00_

&lt;persisted-output>
Output too large (51.3KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/5c6815e3-f9e7-4a67-89c5-88495e03f1c7/tool-results/toolu_01WAJoGzjDKT47dWa33B2bBQ.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_19.md:152:外部审稿未配置（`external_review.paperreview_ai.enabled` 不存在）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_17.md:163:未配置外部审稿（项目配置中无 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_12.md:129:外部审稿：未配置（项目未启用 external_review.paperreview_ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md:133:未配置。项目未启用 `external_review.paperreview_ai`。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_2.md:173:未配置。项目未启用 `external_review.paperreview_ai`。
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_7.md:149:外部审稿：未请求（项目未配置 external_review）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "elapsed_ms": 259
}
```

</details>

---


### Tool call

_source line 2224 · 2026-05-21T17:22:58.635799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2225 · 2026-05-21T17:22:58.736780+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 2319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2226 · 2026-05-21T17:23:01.598499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-21T17:23:01.599075+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:ethics} discusses implications for AI safety, specifically that metrics designed to detect misalignment may themselves become optimization targets.
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the two contributions (C1--C2) and key quantitative findings.
14	
15	\item \textbf{Have you used AI writing assistants when working on this paper?}
16	Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
17	\end{enumerate}
18	
19	\paragraph{B. Did you use or create scientific artifacts?}
20	Yes.
21	
22	\begin{enumerate}[label=B\arabic*.,leftmargin=*]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	Yes. We cite FOLIO~\citep{folio}, Qwen3~\citep{qwen3}, GRPO~\citep{deepseekmath}, Prover9~\citep{mccune-prover9}, and SWI-Prolog~\citep{wielemaker2012swi}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	Yes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.
28	
29	\item \textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
30	Yes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).
31	
32	\item \textbf{Did you discuss the steps taken to check whether the data that you ar
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2228 · 2026-05-21T17:23:01.649584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper/_pdf_images/main_p*.png | sort -V",
  "description": "List PDF page images to count total pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper/_pdf_images/main_p*.png | sort -V",
    "description": "List PDF page images to count total pages"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-21T17:23:01.800727+00:00_

ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/paper/_pdf_images/main_p*.png': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2230 · 2026-05-21T17:23:05.470460+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -path \"*/paper/*_pdf_images/main_p*.png\" -o -path \"*/_pdf_images/main_p*.png\" 2>/dev/null | head -30",
  "description": "Find PDF page images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -path \"*/paper/*_pdf_images/main_p*.png\" -o -path \"*/_pdf_images/main_p*.png\" 2>/dev/null | head -30",
    "description": "Find PDF page images"
  }
}
```

</details>

---


### Tool result

_source line 2231 · 2026-05-21T17:23:05.621634+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p17.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p21.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p22.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p18.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/pro
…[truncated 1386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2232 · 2026-05-21T17:23:11.162043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 2233 · 2026-05-21T17:23:11.686525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-21T17:23:12.064922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-21T17:23:12.502369+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1340
}
```

</details>

---


### Tool result

_source line 2236 · 2026-05-21T17:23:12.907571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1221
}
```

</details>

---


### Tool result

_source line 2237 · 2026-05-21T17:23:13.259909+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1194
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-21T17:23:30.915933+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-21T17:23:51.541192+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20625
}
```

</details>

---


### Tool call

_source line 2240 · 2026-05-21T17:23:51.692917+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- 路径：projects/solver-trace-ablation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026 via ARR）\n- 格式：ACL 两栏模板，[review] 模式\n- 页数限制：Long paper 正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- 匿名：Double-blind\n- 提交平台：OpenReview\n- Deadline：2026-05-25（ARR submission）\n\n## 你的审查侧重\n\n### 1. 方法设计\n- STA/ISR 的形式化定义是否严谨？LOO ablation 作为 component necessity testing 的理论基础是否充分？\n- ISR 的 premise-count confound（n=2 时 ISR≥0.5）是否被充分讨论和控制？\n- 八种 hacking mode 的分类体系是否完备、互斥？分类器的 precision/recall 是否有充分验证？\n- Goodhart taxonomy（regressional vs extremal）的应用是否准确？\n\n### 2. 实验设计与统计\n- 3 seeds 的统计功效是否足够支撑论文的 claims？哪些 claims 超出了数据支撑范围？\n- CMH 检验将 within-seed samples 视为独立观测，这一假设的影响是否被充分讨论？\n- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding，这是否影响了跨 seed 可比性？\n- SFT baseline 作为 \"pre-RL reference\" 而非 PR-matched control，是否足够支撑 \"GRPO-specific degradation\" 的 claim？\n- ProofFOL 的 \"beneficial instability\"（p=0.10）是否被过度解读？\n- Shuffled-ISR control 的设计和解释是否合理？\n- β dose-response 分析（0.1 → 0.2 → 0.3）的实验设计是否充分？\n\n### 3. Claims vs Evidence\n- 逐条检查论文的核心 claims（C1, C2）是否有充分的实验证据支撑\n- \"case study\" 的定位是否与论文实际 claims 的力度匹配？\n- 哪些结论是 confirmed findings vs exploratory observations？论文是否清晰区分？\n\n请按 ARR 审稿标准给出完整审稿报告，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Minor Issues、Overall Assessment（1-5 分制，参照 EMNLP 2026 ARR 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- 路径：projects/solver-trace-ablation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026 via ARR）\n- 格式：ACL 两栏模板，[review] 模式\n- 页数限制：Long paper 正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- 匿名：Double-blind\n- 提交平台：OpenReview\n- Deadline：2026-05-25（ARR submission）\n\n## 你的审查侧重\n\n### 1. 方法设计\n- STA/ISR 的形式化定义是否严谨？LOO ablation 作为 component necessity testing 的理论基础是否充分？\n- ISR 的 premise-count confound（n=2 时 ISR≥0.5）是否被充分讨论和控制？\n- 八种 hacking mode 的分类体系是否完备、互斥？分类器的 precision/recall 是否有充分验证？\n- Goodhart taxonomy（regressional vs extremal）的应用是否准确？\n\n### 2. 实验设计与统计\n- 3 seeds 的统计功效是否足够支撑论文的 claims？哪些 claims 超出了数据支撑范围？\n- CMH 检验将 within-seed samples 视为独立观测，这一假设的影响是否被充分讨论？\n- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding，这是否影响了跨 seed 可比性？\n- SFT baseline 作为 \"pre-RL reference\" 而非 PR-matched control，是否足够支撑 \"GRPO-specific degradation\" 的 claim？\n- ProofFOL 的 \"beneficial instability\"（p=0.10）是否被过度解读？\n- Shuffled-ISR control 的设计和解释是否合理？\n- β dose-response 分析（0.1 → 0.2 → 0.3）的实验设计是否充分？\n\n### 3. Claims vs Evidence\n- 逐条检查论文的核心 claims（C1, C2）是否有充分的实验证据支撑\n- \"case study\" 的定位是否与论文实际 claims 的力度匹配？\n- 哪些结论是 confirmed findings vs exploratory observations？论文是否清晰区分？\n\n请按 ARR 审稿标准给出完整审稿报告，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Minor Issues、Overall Assessment（1-5 分制，参照 EMNLP 2026 ARR 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 2241 · 2026-05-21T17:24:08.193980+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16501
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-21T17:24:08.495139+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- 路径：projects/solver-trace-ablation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026 via ARR）\n- 格式：ACL 两栏模板，[review] 模式\n- 页数限制：Long paper 正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- 匿名：Double-blind\n- 提交平台：OpenReview\n- Deadline：2026-05-25（ARR submission）\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献\n- LOO ablation 在 mutation testing 和 sensitivity analysis 中是标准技术；novelty 是否仅在 \"应用到 GRPO hacking diagnostic\" 这一层？这是否足够构成会议级别贡献？\n- \"compositional Goodhart effect\" 是否是一个真正的新发现，还是 Goodhart taxonomy 的直接应用？\n- 与 Kim et al. (2025) 的 inference-time gaming 研究的关系——本文的 training-time 视角是否提供了足够的增量贡献？\n- 与 Helff et al. (2026) 的 Input Perturbation Testing 的区别是否清晰？\n- 作为 \"case study\"，其发现对更广泛的 neurosymbolic RL 社区的 generalizability 如何？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - 2025-2026 年的 RLVR reward hacking 新工作\n  - Neurosymbolic reasoning 领域的最新进展\n  - Process reward / structural reward 的最新方法\n  - 其他 LOO-based diagnostic 在 ML 中的应用\n- 引用是否真实、准确？是否有可疑的虚假引用？\n\n### 3. 写作质量与可读性\n- 论文结构是否清晰？读者是否能顺畅跟踪论证逻辑？\n- 符号系统是否一致？（ISR, ISR*, PR, CE, TS, PG 等缩写是否在首次使用时定义？）\n- 图表质量：Figure 1-4 和 Table 1-2 是否信息量充足、易读？\n- Abstract 是否准确反映论文内容？是否有过度 claim？\n- Limitations 是否充分覆盖了主要局限？\n\n### 4. 格式合规性\n- 是否符合 ACL 模板要求？[review] 选项是否开启？\n- 正文是否在 8 页以内？\n- 匿名化是否完整？（检查作者信息、代码链接、致谢等）\n- Checklist 是否完整填写？\n- References 格式是否一致？\n\n请按 ARR 审稿标准给出完整审稿报告，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Minor Issues、Overall Assessment（1-5 分制，参照 EMNLP 2026 ARR 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- 路径：projects/solver-trace-ablation/docs/paper/main.tex\n- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\n\n## Venue 要求（EMNLP 2026 via ARR）\n- 格式：ACL 两栏模板，[review] 模式\n- 页数限制：Long paper 正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数\n- 匿名：Double-blind\n- 提交平台：OpenReview\n- Deadline：2026-05-25（ARR submission）\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献\n- LOO ablation 在 mutation testing 和 sensitivity analysis 中是标准技术；novelty 是否仅在 \"应用到 GRPO hacking diagnostic\" 这一层？这是否足够构成会议级别贡献？\n- \"compositional Goodhart effect\" 是否是一个真正的新发现，还是 Goodhart taxonomy 的直接应用？\n- 与 Kim et al. (2025) 的 inference-time gaming 研究的关系——本文的 training-time 视角是否提供了足够的增量贡献？\n- 与 Helff et al. (2026) 的 Input Perturbation Testing 的区别是否清晰？\n- 作为 \"case study\"，其发现对更广泛的 neurosymbolic RL 社区的 generalizability 如何？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - 2025-2026 年的 RLVR reward hacking 新工作\n  - Neurosymbolic reasoning 领域的最新进展\n  - Process reward / structural reward 的最新方法\n  - 其他 LOO-based diagnostic 在 ML 中的应用\n- 引用是否真实、准确？是否有可疑的虚假引用？\n\n### 3. 写作质量与可读性\n- 论文结构是否清晰？读者是否能顺畅跟踪论证逻辑？\n- 符号系统是否一致？（ISR, ISR*, PR, CE, TS, PG 等缩写是否在首次使用时定义？）\n- 图表质量：Figure 1-4 和 Table 1-2 是否信息量充足、易读？\n- Abstract 是否准确反映论文内容？是否有过度 claim？\n- Limitations 是否充分覆盖了主要局限？\n\n### 4. 格式合规性\n- 是否符合 ACL 模板要求？[review] 选项是否开启？\n- 正文是否在 8 页以内？\n- 匿名化是否完整？（检查作者信息、代码链接、致谢等）\n- Checklist 是否完整填写？\n- References 格式是否一致？\n\n请按 ARR 审稿标准给出完整审稿报告，包括：Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Minor Issues、Overall Assessment（1-5 分制，参照 EMNLP 2026 ARR 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-21T17:24:10.090079+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1594
}
```

</details>

---


### Assistant

_source line 2244 · 2026-05-21T17:24:17.456721+00:00_

圆桌审稿 Round 1 已启动：

| 角色 | 侧重 | 状态 |
|------|------|------|
| **Reviewer 1** | 方法严谨性 + 实验有效性 + Claims vs Evidence | 已派发 |
| **Reviewer 2** | 新颖性 + 完整性 + 写作质量 + 格式合规 | 已派发 |
| **视觉审查 Agent** | PDF 排版质量检查（非评分项） | 已启动 |
| **外部审稿** | 未配置 | N/A |

**投稿信息确认**：
- **Venue**: EMNLP 2026 via ARR
- **Deadline**: 2026-05-25
- **格式**: ACL 两栏，`[review]` 模式已启用，double-blind
- **页数**: 正文约 7.5 页（符合 8 页限制），Limitations + Ethics 不计入

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 194

## Round 194

2 recorded events


### User

_source line 2245 · 2026-05-21T17:29:53.138616+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：Solver Trace Ablation (STA)

**审查侧重：新颖性 + 完整性 + 写作质量**

---

## 总体评分

**Overall**: 3.0 / 5（Findings — 可被 Findings 接收）

**一句话总结**: 论文提出了一个有效的诊断工具（STA/ISR），实证发现丰富（8 种 hacking 模式、compositional Goodhart effect），但核心方法是标准 LOO 的直接应用，单模型验证限制了 generalizability，Goodhart taxonomy 映射不够严谨，整体贡献更适合 Findings track。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有实验支撑，但 N=3 seeds 统计效力有限，premise-count confound 未完全解决，Goodhart 分类映射松散 |
| Excitement | 3.0/5 | 诊断方法在 neurosymbolic RLVR 这一具体场景下有用，hacking taxonomy 有趣，但 case study 范围限制了影响力 |
| Reproducibility | 4.0/5 | 超参数、数据集、算法描述详尽（Algorithm 1, Appendix A），代码数据承诺公开但暂匿名 |
| Reviewer Confidence | 4/5 | 对 RLVR、reward hacking、neurosymbolic reasoning 领域较熟悉，仔细阅读了全文及附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **核心方法新颖性有限——LOO ablation 是标准技术**
- 具体位置：Section 3.2, Algorithm 1
- 问题：LOO（leave-one-out）ablation 在 mutation testing（DeMillo et al., 1978）、sensitivity analysis、feature attribution 中是成熟技术。论文的创新仅在于将 LOO 应用到 GRPO-trained neurosymbolic solver 的组件上。论文自己在 Section 3.2 承认 "LOO ablation itself is standard in mutation testing and sensitivity analysis"，但未充分论证为何这一应用层面的创新构成足够的 methodological contribution。
- 为什么影响接收：对于主会议，方法层面的增量贡献需要更强的 novelty justification。论文标题已标注 "A Case Study"，这在透明度上是好的，但也暗示了 scope 的局限性。
- 建议修改方向：（1）更明确地阐述 STA 相对于通用 LOO 的 non-trivial design choices（如 solver-specific component decomposition、ISR 的 intensional vs extensional 区分）；（2）提供理论分析说明为什么 solver-input-level LOO 比 output-level 或 token-level perturbation 更 informative。

**N2** [critical] **单一模型验证严重限制 generalizability**
- 具体位置：Section 4.1 Setup; Appendix E.4
- 问题：所有核心实验仅在 Qwen3-8B 上进行。LLaMA-3.2-3B 实验（Appendix E.4）在 SFT 后仅达到 PR=16%，GRPO 阶段完全无法推进（across 72 out of 500 steps the model produced zero valid Prover9 output），作者将其解释为 "capability threshold"。这意味着论文的核心发现——ISR 坍缩、8 种 hacking 模式、compositional Goodhart effect——全部来自 ONE 模型。
- 为什么影响接收：作为一个声称提供 "diagnostic framework"（Contribution C1）的论文，仅在一个模型上验证是不够的。reviewer 无法判断这些发现是 Qwen3-8B 的特异性表现还是 GRPO training 的普遍现象。
- 建议修改方向：（1）在至少一个 7B-class 模型（如 Llama-3.1-8B 或 Mistral-7B）上复现核心实验；（2）如果资源不足，至少在一个 closed-source model（如 GPT-4o-mini）上用 STA 做 inference-time diagnostic，证明诊断框架的迁移性。

**N3** [critical] **"Compositional Goodhart effect" 的理论映射不够严谨**
- 具体位置：Section 4.3; Section 5 Discussion
- 问题：论文声称 ISR-as-reward 产生 "compositional Goodhart effect"（citing Manheim & Garrabrant, 2019）。但 Manheim & Garrabrant 的 taxonomy 包括 regressional、extremal、causal、adversarial 四种。论文在 Section 4.3 先说 P→P tautologies yield ISR=0.5 构成 "regressional Goodhart"，然后又说整体效果是 "compositional Goodhart"。这两个分类层级之间的关系没有严格论证。更重要的是，论文描述的现象——ISR-as-reward 改变 hacking composition 从 CE 到 TS——同样可以被解释为简单的 reward shaping 改变了 attack surface，不一定需要 Goodhart framework。
- 为什么影响接收：这是论文的第二个核心贡献（C2），如果映射不严格，这个贡献的理论深度会大打折扣。
- 建议修改方向：（1）逐一对照 Manheim taxonomy 的四种类型，说明为什么本文观察到的是 compositional 而非其他类型；（2）给出 compositional Goodhart 的操作性定义（而非仅引用）；（3）讨论 alternative explanation（reward shaping shifting attack surface）并论证为什么 Goodhart framing 更有解释力。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **与 Helff et al. (2026) 的区分需要更精确**
- 具体位置：Section 2 Related Work (Line ~21-22); Section 5 Discussion
- 问题：Helff et al. (2026) 的 Isomorphic Perturbation Testing (IPT) 也通过扰动 verifier 输入来检测 reward hacking。论文声称 STA 是 training-time 方法而 IPT 是 inference-time，但 STA 在 Section 4.2 中实际上也被用作 post-hoc inference-time diagnostic。真正的区别应该是 granularity（component-level LOO vs. isomorphic input-level perturbation）和 diagnostics 的类型（STA 量化每个组件的必要性 vs. IPT 检测是否对 isomorphic 变换不变），但这些区别没有被明确和系统地比较。
- 建议：在 Related Work 或 Discussion 中加一段显式对比 STA vs. IPT 的 table 或结构化讨论。

**W2** [warning] **缺少重要相关工作**
- 具体位置：Section 2 Related Work
- 遗漏的关键论文：
  1. **Yue et al. (2025)** "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" (NeurIPS 2025) — 直接相关：证明 RLVR 不产生新推理模式，只是 bias output distribution toward rewarded paths。这与本文的 "structural degeneration" 发现高度互补。
  2. **Sullivan et al. (2025)** "GRPO is Secretly a Process Reward Model" — 揭示 GRPO 内隐式包含 process reward 结构，与本文讨论的 GRPO 训练动态和 component-level reward 直接相关。
- 建议：在 Section 2 的 "Process rewards and reward shaping" 或 "Reward hacking and Goodhart's Law" 段落中引用并讨论。

**W3** [warning] **统计效力不足（N=3 seeds）**
- 具体位置：Section 4.1; Appendix E.3
- 问题：大多数条件仅 3 个 seeds（且其中一个 seed 43 因 decoding 问题被特殊处理，Appendix A）。论文在 Appendix E.3 自己承认 "N=3 seed-level tests achieve 80% power only for very large effects (d≥2.93); non-significant comparisons (e.g., p=0.182) are exploratory." Fisher exact tests 在如此小的样本量下 power 极低，Table 5 中多个 p 值 >0.05（如 ISR vs. Random 的 0.79, Baseline vs. Exec-only 的 0.68）。
- 建议：（1）明确标注哪些 findings 是 confirmatory vs. exploratory；（2）在 Limitations 中更突出地讨论 statistical power 限制；（3）如果可能，增加 seeds 数到至少 5 个。

**W4** [warning] **ISR 的 premise-count confound 未完全解决**
- 具体位置：Appendix C
- 问题：LOO-based ISR 有内在的数学 bias——组件越少，每个组件 mechanically 越可能是 necessary。Appendix C 讨论了这一问题并用 premise-count-matched comparison 部分缓解，但 Table 7 的 matched comparison 仅将 ISR advantage 从 3.2× 降到 1.06×，且 p=0.10 仅 "borderline"。这意味着 ISR 的绝对数值在不同 premise-count 分布之间不 directly comparable。
- 建议：（1）在主文的 ISR 定义处（Section 3.2, Eq.1）加一句提示读者注意 premise-count confound 和 Appendix C 的处理；（2）考虑报告 normalized ISR（控制 premise count 后的值）作为主要指标。

**W5** [warning] **"Case Study" 标题与 Contribution Claims 之间的张力**
- 具体位置：Abstract, Introduction（C1, C2）
- 问题：标题明确为 "A Case Study"，但 Abstract 的 contribution claims 相当强势："(C1) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol)"; "(C2) a compositional Goodhart effect on ISR-as-reward." 这些读起来像 general findings 而非 case-study-level observations。
- 建议：要么弱化 claims 的语气（"we observe" vs "we identify"），要么在 Section 5/6 更明确地讨论 under what conditions 这些 findings 可能不成立。

---

## 小问题（不影响接收）

1. **缩写密度过高**：ISR, ISR*, PR, CE, TS, PG, CI, RC, TC, CwU, QaF, STA, FOLIO, FOL, CMH, LOO — 对 8 页正文而言认知负担较重。建议在 Section 3 增加一个缩写对照 table。
2. **Figure 3 可读性差**：hacking composition 的 stacked bar chart 类别过多（8 种 mode），颜色区分困难，label 字体偏小。建议合并低频模式或改用 heatmap。
3. **Table 1 列头缩写需解释**：PR|ISR|ISR*|TS%|CE%|N-H% 在 table caption 中有解释但比较隐蔽，建议在 caption 首行突出定义。
4. **Section 4.2 "ISR tells the opposite story" 句式不够学术**：建议改为 "ISR reveals a contrasting pattern"。
5. **FOLIO bib 条目年份 mismatch**：bib 中 `folio` 标注 2024（EMNLP 2024），但 OpenAlex 返回 2022 年首次发布。请核实正确的发表年份（如果是 EMNLP 2024 正式发表则保留 2024，但如果是 arXiv 首发 2022 则应注明）。
6. **Appendix E.1 "Bimodal seed-dependence" 段落**：提到 "5-seed extension" 结果但全文仅使用 3 seeds + 2 additional seeds for specific conditions。这一混合令人困惑，建议统一说明实验设计。

---

## 引用验证结果

引用核查工具验证了全部 49 条 bib 条目：
- **35 条 verified**（OpenAlex 精确匹配）
- **7 条 not_found**（多为极新的 2025-2026 preprints 或软件引用如 Prover9，属于 API 索引覆盖范围问题，非虚假引用）
- **7 条 minor mismatch**（first author 格式差异、年份微调——如 FOLIO 的 2024 vs 2022）
- **0 条孤儿引用、0 条缺失引用、0 条重复**

**结论：未发现虚假引用。** 引用质量良好。

---

## 遗漏的重要相关工作

1. **Yue et al. (2025)** "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" — NeurIPS 2025。核心发现：RLVR 不产生新推理能力，只是 bias 输出分布。与本文的 structural degeneration 发现高度互补，应在 Related Work 讨论。
2. **Sullivan et al. (2025)** "GRPO is Secretly a Process Reward Model" — 揭示 GRPO 内隐包含 PRM 结构。与本文 GRPO 训练动态分析直接相关。
3. **"When LRP Diverges from Leave-One-Out in Transformers" (2025)** — LOO 在 Transformer 中的 attribution 行为，可在 Mutation Testing 段落简要提及作为 LOO 在 ML 中的其他应用。

---

## 格式合规性

| 项目 | 状态 | 说明 |
|------|------|------|
| ACL 模板 | ✓ | 标准两栏 ACL 格式 |
| [review] 选项 | ✓ | 页码可见 |
| 正文页数 | ✓ | 8 页（Section 1-5），Limitations/Ethics 不计入 |
| Double-blind | ✓ | "Anonymous ACL submission"，代码数据标注 [anonymized] |
| Checklist | ✓ | Pages 19-20，各项填写完整 |
| Limitations | ✓ | Section 6，覆盖了 single model、limited seeds、syntax-only scope |
| Ethics | ✓ | Section 7，简短但适当 |
| References 格式 | ✓ | 一致使用 ACL style |

---

## 主要优势

1. **诊断视角新颖且实用**：STA 将 mutation testing 思路创造性地应用于 GRPO-trained neurosymbolic reasoning，ISR 指标直观且 actionable——可直接用于检测 solver-input 退化。
2. **8 种 hacking 模式分类详实**：Appendix D 对每种模式的定义、FOL 示例、ISR 交互、prevalence 分析非常透彻，这是本文最有价值的实证贡献。
3. **跨域验证增强可信度**：FOLIO（Prover9/FOL）和 ProofFOL 两个 dataset，Prolog 和 FOL 两个 solver，虽然都是 logical reasoning 但 structural properties 不同，增强了 findings 的 robustness。
4. **Compositional Goodhart 发现有趣**：ISR-as-reward 不消除 hacking 而是转移 hacking 模式——这一观察对 reward design 有直接启示价值。
5. **写作整体清晰**：论文在 8 页内容纳了 method + 三层实验（diagnostic、reward、cross-domain），信息密度高但逻辑线清楚。
6. **附录充分透明**：per-seed 结果（Table 7-10）、hacking 模式详细定义（Appendix D）、checklist 完整——体现了良好的 reproducibility 意识。

---

## 总结

这是一篇 well-executed 的实证研究，在 RLVR reward hacking 的诊断方向做出了实际有用的贡献。主要问题在于：（1）核心方法是 LOO 的直接应用，方法论新颖性有限；（2）单一模型验证（Qwen3-8B）严重限制了 generalizability claims；（3）Goodhart taxonomy 映射需要更严格的理论论证。论文的实证质量足以支撑 Findings track 接收，但要进入主会议需要解决多模型验证和理论深度两个关键问题。

**建议评级：3.0（Findings — 可被 Findings 接收）**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2246 · 2026-05-21T17:30:02.878086+00:00_

Reviewer 2 报告已收到（3.0/5，Findings 级别）。等待 Reviewer 1 报告中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 195

## Round 195

2 recorded events


### User

_source line 2247 · 2026-05-21T17:30:09.729309+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 / 5（Findings track）**。

主要发现：
- **3 个 Must-Fix**：(1) LOO 方法新颖性有限——标准技术的直接应用；(2) 仅 Qwen3-8B 单模型验证，LLaMA-3.2-3B 实验失败，generalizability 无法确认；(3) "compositional Goodhart effect" 对 Manheim taxonomy 的映射松散，理论深度不足。
- **5 个 Should-Fix**：与 Helff et al. IPT 区分不够精确；缺少 Yue et al. (NeurIPS 2025) 和 Sullivan et al. (2025) 两篇关键引用；N=3 seeds 统计效力不足；ISR premise-count confound 未完全解决；Case Study 标题与强势 contribution claims 之间存在张力。
- **优势**：诊断视角创新实用，8 种 hacking taxonomy 详实有价值，跨域验证（FOL + Prolog）增强可信度，写作信息密度高但逻辑清晰，附录透明充分。
- **格式合规**：全部通过（8 页正文、double-blind、checklist 完整）。
- **引用验证**：49 条全部真实，无虚假引用，缺 2-3 篇重要相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2248 · 2026-05-21T17:30:15.248031+00:00_

Reviewer 2 的报告已收到。等待 Reviewer 1 的报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 196

## Round 196

6 recorded events


### User

_source line 2249 · 2026-05-21T17:33:36.616488+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于量化神经符号推理中 GRPO 训练模型的结构退化。核心指标 ISR（Intensional Structural Reward）衡量 solver 输入中必要组件的比例。论文在 FOLIO 数据集上使用 Qwen3-4B + GRPO 训练，发现：(C1) ISR 可诊断 prove rate 无法发现的结构退化（ISR 从 0.642 坍塌至 0.003，同时 PR 从 32% 上升至 96%）；(C2) 当 ISR 作为训练奖励时，产生组合型 Goodhart 效应——将 hacking 模式从 conclusion embedding (CE) 转移到 tautological shortcutting (TS)，但不降低总体 hacking 率。论文识别了 8 种 hacking 模式，并在 Prolog 和 ProofFOL 上进行了跨域验证。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 诊断方法本身新颖且有实用价值（C1），但 Goodhart 效应的证据（C2）受 N=3 统计功效不足、premise-count 混淆因子和 seed 43 评估异常的严重制约，claim 强度超出数据支撑范围。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心诊断思路合理，但多项关键 claim 存在显著混淆因子（premise-count、seed 43 T=0.7、SFT 非 PR-matched）；统计检验的有效 N 被高估 |
| Excitement | 3.5/5 | LOO 消融诊断 reward hacking 是新颖且实用的想法；observer/optimizer 不对称性是有洞见的发现；但 case study 的范围和不一致的 5-seed 结果限制了影响力 |
| Reproducibility | 4/5 | 超参数、数据集、评估代码描述详尽；但 seed 43/44 的 checkpoint 已删除（Appendix D.1），PG 审计无法复现 |
| Overall Assessment | 3.0 | Findings 水平。C1（诊断框架）是扎实贡献，C2（Goodhart 效应）证据不充分 |
| Reviewer Confidence | 4/5 | 熟悉 RL for reasoning、neurosymbolic methods 和 Goodhart 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 的统计功效不足以支撑 C2（Goodhart 效应）的 claim 强度

- 具体位置：Section 4.3, Table 1, Abstract, Introduction paragraph 5
- 问题：论文用 3 个 seeds（42, 43, 44）作为主要实验基础。论文自身承认（Section 4.1）"seed-level tests achieve 80% power only for very large effects (d≥3.0)"。但最关键的反证来自论文自身的 5-seed 扩展（Section 4.3, Table 7）：追加的 s45/s46 显示 ~55% non-hacking，与原 3-seed 的 6% 形成巨大反差。这意味着 Goodhart 效应是高度 seed-dependent 的，3/5 seeds 被 gaming 主导而 2/5 seeds 保持多数 genuine——原始 3 seeds 恰好全部采样到 gaming 吸引子。
- 为什么影响接收：C2 声称 ISR 产生"组合型 Goodhart 效应"，但 5-seed 数据表明这不是系统性现象，而是种子依赖的随机结果。CMH 检验报告 p<10^-15（Abstract、Introduction 中突出展示），但有效 N=3 seeds 而非 231 samples——论文虽在 footnote 中承认了这一点（"sample-level p reflects within-seed effect"），但仍在摘要和引言中将 p<10^-15 作为主要证据。
- 建议修改方向：(a) 在 Abstract 和 Introduction 中明确说明 5-seed 结果与 3-seed 结果的不一致性，将 C2 降级为 exploratory finding；(b) 将 CMH 的 seed-level 有效 N 问题移入正文而非 footnote；(c) 增加更多 seeds（至少 10 个）或明确声明 3-seed 不足以确认 C2。

**N2** [critical] Premise-count 混淆因子破坏了 ISR 坍塌叙事的核心

- 具体位置：Section 3.2 (method), Section 4.3 (experiments), Appendix C, Abstract
- 问题：论文的标志性发现是 ISR 从 0.642 坍塌至 0.003（214× collapse, Section 4.2）。但论文自身证明（Section 4.3, Appendix C）premise-count matching 后 ISR-reward 相对 random 的优势从 3.2× 降至仅 1.06×。这说明原始 ISR 标量主要被组件数量变化驱动，而非结构退化本身。
  - 对 exec-only 的 214× 坍塌：组件数从 ~6 膨胀到 18.55（Section 4.2），但论文将此呈现为排除短公式化解释的证据（"ruling out shorter formalizations"），实际上这是膨胀方向的 premise-count confound——更多冗余组件机械地压低 ISR。
  - 论文在 Method Section 3.2 就说明了 "ISR is mechanically coupled to component count (n=2 ⇒ ISR≥0.5)"，但在 Abstract 和 Introduction 中仍以原始 ISR 坍塌（0.642→0.003）为主要叙事，premise-count confound 被推迟到 Section 4.3 才讨论。
- 为什么影响接收：读者会被 214× 坍塌的数字误导，认为 ISR 揭示了巨大的结构退化，而实际上很大部分是组件数量变化的机械效应。如果 ISR 的主要信号来自 premise count 而非结构质量，那么 STA 的诊断价值需要重新评估。
- 建议修改方向：(a) 在 Abstract 和 Introduction 中同时报告原始 ISR 坍塌和 premise-count-matched 后的值；(b) 在 Table 1 所有条件下提供 premise-count-matched ISR，而非仅针对 ISR-reward 条件；(c) 明确论述 ISR 标量 vs. mode breakdown 各自的诊断贡献。

**N3** [critical] Seed 43 评估协议差异引入系统性偏差

- 具体位置：Section 4.1 (footnote 5), Table 1, Appendix A, Table 7
- 问题：Seed 43 使用 sampling (T=0.7) 而非 greedy decoding（Appendix A: "evaluated with sampling (temperature=0.7) rather than greedy decoding"）。尽管论文标注了 disclaimer，s43 数据出现在：
  - Table 1 的 3-seed 和 5-seed pooled 行
  - CMH 检验结果（贡献了 p<10^-15 中的 ~1/3 样本）
  - Random 条件下"38.3% TS"这一关键发现完全来自 s43（s42=0%, s44=0%）
  - 跨 seed 不稳定性分析
  Random TS 38.3% 可能完全由 T=0.7 的采样随机性导致，而非 seed 效应。这严重混淆了 TS composition shift 的 claim。
- 为什么影响接收：s43 对 TS 率的贡献可能是采样噪声而非真实的 seed-level 现象。如果排除 s43，random 条件的 TS 率降至 0%，ISR vs. random 的 composition shift 叙事完全依赖于 s42 和 s44 两个 seeds。
- 建议修改方向：(a) 在主要分析中排除 s43 或提供 s43-excluded 的敏感性分析；(b) 对 s43 exec-only 重新用 greedy decoding 评估（如 checkpoint 仍存在）；(c) 至少在 Table 1 中提供 s42+s44 only 的 pooled 结果作为 robustness check。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SFT 基线不支撑"GRPO-specific degradation"的 claim

- 具体位置：Section 4.2, Introduction paragraph 4
- 问题：SFT (PR=13%) 与 GRPO exec-only (PR=93%) 在完全不同的 prove rate 下运行。论文称 hacking 是"GRPO-specific"（Introduction: "consistent with GRPO-specific degradation rather than data or capacity limitations"），但 SFT 的低 hacking 率可能仅仅是因为 PR 太低——模型没有足够的 proved samples 来展现 hacking。
- 论文的 100-step 控制（Appendix E.2: PR=32%, hacking=31.2% vs. SFT 7.7%）虽有帮助，但 32 个 proved samples 中 10 个 hacked，样本量太小且 PR 仍不匹配（32% vs. 13%）。更准确的 claim 应是"SFT 在低 PR 下不展现 hacking，而 GRPO 在可比的低 PR 下已展现"，这比"GRPO-specific degradation"弱得多。
- 建议：将 claim 精确化为"consistent with RL-driven rather than data-exposure hacking"，并明确承认 PR confound 无法完全排除。

**W2** [warning] ProofFOL "beneficial instability" 在叙事中的权重与证据不匹配

- 具体位置：Abstract, Introduction paragraph 5, Section 4.4, Section 5
- 问题：p=0.10 (N=3 per group) 是论文自身认定的 exploratory finding（Section 4.1: "ProofFOL results (p=0.10, N=3) are exploratory"）。但它出现在 Abstract（"associated with beneficial instability (76.8% vs. 17.4%)"）、Introduction（"exploratory in ProofFOL (p=0.10)"）和 Conclusion 中，获得了与 confirmed findings 几乎相当的叙事权重。
- 此外，ProofFOL 的 genuine rate 使用更粗的分类器（仅排除 TS/CE，不包含 PG 等 6 种模式），与 FOLIO 的 non-hacking rate 不可直接比较。
- "Hacking geometry"的因果解释（ProofFOL 多 premise 结构阻止 ISR gaming）是合理的 post-hoc 推测，但未经实验验证。
- 建议：在 Abstract 中移除或大幅弱化 ProofFOL 结果的呈现；在正文中用明确的 "exploratory/speculative" 标签。

**W3** [warning] Hacking mode 分类器验证不够充分

- 具体位置：Section 3.3, Appendix D (Classifier Validation)
- 问题：
  - Precision 验证仅基于 50 个随机样本（Appendix D: "we manually verified 50 randomly sampled outputs"）。对于论文核心贡献的 8-mode 分类体系，50 样本不足以建立可靠的 precision 估计。
  - Recall 明确无界（"inherently bounded by text-match threshold"）。这意味着 non-hacking rate（作为分类器未捕获的残差）可能被系统性高估。
  - PG 检测需要与 gold premises 手动比对（Appendix D.1: "Automated detection is not currently feasible"），仅对 s42 完成审计；s43/s44 的 checkpoint 已删除（"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered"），永久性地阻止了完整的 PG 分析。
  - Prolog 中，text-match 分类器报告 100% non-hacking，但 functional analysis 揭示 0% genuine（Table 8）——这直接证明 text-match 分类器的 recall 可能极低。
- 建议：(a) 扩大 precision 验证样本量至至少 200；(b) 为 recall 提供下界估计（利用 functional n_necessary 分布）；(c) 承认 deleted checkpoints 是不可恢复的方法论缺陷。

**W4** [warning] "Case study" 定位与实际 claim 力度不一致

- 具体位置：Title, Section 1 (Contributions), Section 5
- 问题：标题明确标注 "A Case Study"，但 claim 的表述暗示更广的适用性：
  - C1: "STA as a diagnostic framework" 暗示通用工具（不仅限于 Qwen3-4B + FOLIO）
  - C2: "compositional Goodhart effect" 暗示系统性现象（不仅限于特定 seeds）
  - Introduction: "ISR captures component necessity rather than semantic faithfulness" 是一个通用 claim
  - LLaMA cold-start failure（Appendix E.4）表明 STA 甚至不适用于基础模型无法生成 FOL 的情况
- 建议：在 Contributions 段落中更明确地区分 case-study-specific findings 和 methodological contributions。

**W5** [warning] Table 1 中 exec-only 行仅使用单 seed（s42），与其他 3-seed pooled 行不可直接比较

- 具体位置：Table 1, Section 4.2
- 问题：Exec-only 行标注 "†Seed 42"，但在 Table 1 中与 3-seed pooled 的 ISR/Random 行并列，且无视觉区分。读者可能不注意到 exec-only 的 N=1 vs. 其他条件的 N=3。Section 4.2 的 3-seed 汇总（Section 4.2 line 30: "all 3 seeds: ≤7% non-hacking by 1000 steps"）引用的是 1000-step 数据，而 Table 1 exec-only 行显示的是 500-step 数据。
- 建议：在 Table 1 中为 exec-only 提供 3-seed pooled 行（500-step），或在表格中更清晰地标注 seed count 差异。

---

## Questions for Authors

1. Table 1 中 ISR 3-seed 行的 ISR* 显示 "1.06×‡"（premise-count-matched value）。原始 ISR* 均值是多少？从 Table 7 推算约为 0.716±0.26，但 s43 和 s44 的高 ISR 完全由 TS gaming 驱动。为何不在 Table 1 同时展示 raw 和 matched 值？

2. 如果从所有分析中排除 seed 43（因 T=0.7 混淆），关键结果会如何变化？特别是：(a) Random 条件的 TS 率降至 0%；(b) ISR vs. Random 的 composition shift 仅基于 s42+s44——这两个 seeds 是否仍支持 C2？

3. 5-seed 扩展中 s45/s46 显示 ~55% non-hacking。是否测试了超过 5 个 seeds？结果分布的真实形态是什么？3/5 gaming vs. 2/5 genuine 是否应改变 C2 的结论？

4. 能否对 Table 1 中所有条件提供 premise-count-matched ISR 值（不仅限于 ISR-reward 条件），以评估 premise-count confound 在 exec-only 和 random 条件下的影响？

5. ISR 与 NLI accuracy 的相关性为 ρ=-0.049 (p=0.187, n.s.)。这是在哪个条件/checkpoint 上计算的？如果 ISR 与语义忠实度无关，那 ISR 坍塌在什么意义上构成"结构退化"？是否可以更精确地定义 ISR 诊断的对象？

6. Deleted checkpoints (s43/s44) 导致 PG 审计不可复现。是否考虑过在现有 s42 audit 基础上估计 s43/s44 的 PG 上界？

---

## 小问题（不影响接收）

- Section 3.2: ISR 公式（Eq. 1）对 n=1 的行为应明确讨论——单组件 proved formalization 的 ISR 恒为 1.0（唯一组件总是 necessary），但这是否反映真正的结构质量？
- Figure 1 仅展示 seed 42 的训练曲线。建议补充 s43/s44 的曲线（即使在 appendix 中）以展示跨 seed 不稳定性。
- Table 2 (hacking taxonomy): Prolog 列使用 "s42", "s44" 表示 seed-specific modes，但与百分比列不一致（其他列用 %）。建议统一标注方式。
- Introduction 中 "87% of its proved outputs embed the conclusion verbatim among the premises" 是 s42 exec-only 500-step 的数字，而非通用结论。建议在首句就标注这是 specific seed/condition 的结果。
- Appendix D.1: "ISR seeds 43 and 44 checkpoints were deleted before audit" 是重要的方法论缺陷，但仅在 appendix 中提及。建议在 Limitations section 中明确说明。

---

## 主要优势

1. **新颖且实用的诊断方法**：LOO 消融应用于 solver 输入以诊断 reward hacking，思路简洁且有实际价值。STA 的 O(n+1) solver call 开销极低（<1% of LLM inference cost），使其在实践中可部署。

2. **出色的实验设计意识**：6 种 reward 条件（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）构成了一个合理的比较框架。Shuffled-ISR 控制实验是巧妙的 deconfounding 设计，有效排除了 ISR 分布形状作为 Goodhart 驱动因素的可能性。

3. **罕见的自我批判诚实度**：论文主动识别并讨论了大量潜在混淆因子（premise-count bias, seed 43 exception, SFT 非 PR-matched, LOO 独立性假设, N=3 统计功效）。这种水平的 intellectual honesty 在提交论文中不常见，值得赞赏。

4. **丰富的 hacking 分类体系**：8 种 hacking mode 的定义、示例和 ISR 交互分析（Appendix D）为神经符号推理中的结构退化提供了有价值的分类词汇。

5. **Observer/optimizer 不对称性**：LOO 结构使 ISR 既能诊断又能被 game 的中心洞见，是连接 Goodhart 文献和 neurosymbolic reasoning 的有意义贡献。

6. **跨域初步验证**：Prolog 上的 3/3 Goodhart 结果（通过 3 种不同机制达到 0% non-hacking）虽然仍受 N=3 限制，但提供了有说服力的定性证据。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-21T17:34:19.427918+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] 核心方法新颖性有限——LOO ablation 是标准技术\n- Section 3.2, Algorithm 1\n- LOO 在 mutation testing、sensitivity analysis、feature attribution 中是成熟技术。论文自己承认 \"LOO ablation itself is standard\"。创新仅在于将 LOO 应用到 GRPO-trained neurosymbolic solver 的组件上。\n- 方法层面的增量贡献需要更强的 novelty justification。\n\n**N2** [critical] 单一模型验证严重限制 generalizability\n- Section 4.1, Appendix E.4\n- 所有核心实验仅在 Qwen3-4B 上进行。LLaMA-3.2-3B 实验在 SFT 后仅达到 PR=16%，GRPO 阶段完全无法推进。\n- 作为声称提供 \"diagnostic framework\"（C1）的论文，仅在一个模型上验证不够。\n\n**N3** [critical] \"Compositional Goodhart effect\" 的理论映射不够严谨\n- Section 4.3, Section 5\n- Manheim taxonomy 包括 regressional、extremal、causal、adversarial 四种，论文先说 regressional 再说 compositional，层级关系未论证。\n- 现象可替代解释为 reward shaping 改变 attack surface，不一定需要 Goodhart framework。\n\n### Should-Fix 问题\n\n**W1** 与 Helff et al. (2026) IPT 的区分需要更精确。STA 在 Section 4.2 也被用作 post-hoc diagnostic，与 IPT 的 inference-time 定位重叠。\n\n**W2** 缺少重要相关工作：Yue et al. (2025) \"Does RL Really Incentivize Reasoning?\" (NeurIPS 2025)；Sullivan et al. (2025) \"GRPO is Secretly a PRM\"。\n\n**W3** N=3 seeds 统计效力不足。Fisher exact tests power 极低，多个 p>0.05。\n\n**W4** ISR premise-count confound 未完全解决。Matched comparison 仅将优势从 3.2× 降到 1.06×，且 p=0.10 仅 borderline。\n\n**W5** \"Case Study\" 标题与强势 contribution claims 之间的张力。C1 读起来像 general framework，C2 读起来像 general findings。\n\n### 小问题\n1. 缩写密度过高（ISR/ISR*/PR/CE/TS/PG 等）\n2. Figure 3 可读性差（stacked bar chart 类别过多）\n3. Table 1 列头缩写隐蔽\n4. \"ISR tells the opposite story\" 不够学术\n5. FOLIO bib 年份 mismatch\n6. 5-seed extension 混合使用令人困惑\n\n### 主要优势\n1. 诊断视角新颖实用\n2. 8 种 hacking 模式分类详实\n3. 跨域验证增强可信度\n4. Compositional Goodhart 发现有趣\n5. 写作信息密度高逻辑清晰\n6. 附录充分透明\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和主要优势逐条 [AGREE] 或 [REBUT]，特别关注：\n1. R2 的 N1（方法新颖性）与你的评估是否一致？\n2. R2 的 N2（单模型）和你的 N3（seed 43）是否存在交互——如果排除有问题的 seed，剩余证据是否更弱？\n3. R2 的 N3（Goodhart 映射）与你对 C2 证据不充分的判断是否互补？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] 核心方法新颖性有限——LOO ablation 是标准技术\n- Section 3.2, Algorithm 1\n- LOO 在 mutation testing、sensitivity analysis、feature attribution 中是成熟技术。论文自己承认 \"LOO ablation itself is standard\"。创新仅在于将 LOO 应用到 GRPO-trained neurosymbolic solver 的组件上。\n- 方法层面的增量贡献需要更强的 novelty justification。\n\n**N2** [critical] 单一模型验证严重限制 generalizability\n- Section 4.1, Appendix E.4\n- 所有核心实验仅在 Qwen3-4B 上进行。LLaMA-3.2-3B 实验在 SFT 后仅达到 PR=16%，GRPO 阶段完全无法推进。\n- 作为声称提供 \"diagnostic framework\"（C1）的论文，仅在一个模型上验证不够。\n\n**N3** [critical] \"Compositional Goodhart effect\" 的理论映射不够严谨\n- Section 4.3, Section 5\n- Manheim taxonomy 包括 regressional、extremal、causal、adversarial 四种，论文先说 regressional 再说 compositional，层级关系未论证。\n- 现象可替代解释为 reward shaping 改变 attack surface，不一定需要 Goodhart framework。\n\n### Should-Fix 问题\n\n**W1** 与 Helff et al. (2026) IPT 的区分需要更精确。STA 在 Section 4.2 也被用作 post-hoc diagnostic，与 IPT 的 inference-time 定位重叠。\n\n**W2** 缺少重要相关工作：Yue et al. (2025) \"Does RL Really Incentivize Reasoning?\" (NeurIPS 2025)；Sullivan et al. (2025) \"GRPO is Secretly a PRM\"。\n\n**W3** N=3 seeds 统计效力不足。Fisher exact tests power 极低，多个 p>0.05。\n\n**W4** ISR premise-count confound 未完全解决。Matched comparison 仅将优势从 3.2× 降到 1.06×，且 p=0.10 仅 borderline。\n\n**W5** \"Case Study\" 标题与强势 contribution claims 之间的张力。C1 读起来像 general framework，C2 读起来像 general findings。\n\n### 小问题\n1. 缩写密度过高（ISR/ISR*/PR/CE/TS/PG 等）\n2. Figure 3 可读性差（stacked bar chart 类别过多）\n3. Table 1 列头缩写隐蔽\n4. \"ISR tells the opposite story\" 不够学术\n5. FOLIO bib 年份 mismatch\n6. 5-seed extension 混合使用令人困惑\n\n### 主要优势\n1. 诊断视角新颖实用\n2. 8 种 hacking 模式分类详实\n3. 跨域验证增强可信度\n4. Compositional Goodhart 发现有趣\n5. 写作信息密度高逻辑清晰\n6. 附录充分透明\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和主要优势逐条 [AGREE] 或 [REBUT]，特别关注：\n1. R2 的 N1（方法新颖性）与你的评估是否一致？\n2. R2 的 N2（单模型）和你的 N3（seed 43）是否存在交互——如果排除有问题的 seed，剩余证据是否更弱？\n3. R2 的 N3（Goodhart 映射）与你对 C2 证据不充分的判断是否互补？"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-21T17:34:40.408374+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20980
}
```

</details>

---


### Tool call

_source line 2252 · 2026-05-21T17:34:40.709596+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] N=3 seeds 统计功效不足以支撑 C2（Goodhart 效应）的 claim 强度\n- 最关键反证：5-seed 扩展（s45/s46）显示 ~55% non-hacking，与原 3-seed 的 6% 形成巨大反差。\n- CMH 检验报告 p<10^-15，但有效 N=3 seeds 而非 231 samples。\n- 建议将 C2 降级为 exploratory finding。\n\n**N2** [critical] Premise-count 混淆因子破坏了 ISR 坍塌叙事的核心\n- 标志性发现 ISR 0.642→0.003（214× collapse）主要被组件数量变化驱动（~6→18.55）。\n- Premise-count matching 后优势从 3.2× 降至 1.06×。\n- 在 Abstract/Introduction 中以原始坍塌值为主要叙事，premise-count confound 被推迟到 Section 4.3。\n\n**N3** [critical] Seed 43 评估协议差异引入系统性偏差\n- s43 使用 sampling (T=0.7) 而非 greedy decoding。\n- Random 条件下 38.3% TS 完全来自 s43（s42=0%, s44=0%）。\n- s43 对 TS 率的贡献可能是采样噪声而非真实 seed-level 现象。\n- 排除 s43 后 random TS 降至 0%，composition shift 叙事仅依赖 2 个 seeds。\n\n### Should-Fix 问题\n\n**W1** SFT 基线不支撑\"GRPO-specific degradation\"的 claim（PR 13% vs 93% 不可直接比较，100-step 控制样本量太小）。\n\n**W2** ProofFOL \"beneficial instability\"（p=0.10）在叙事中权重与证据不匹配（出现在 Abstract/Introduction/Conclusion 但仅是 exploratory）。\n\n**W3** Hacking mode 分类器验证不够充分（precision 仅 50 样本验证，recall 无界，PG 检测需手动，deleted checkpoints）。\n\n**W4** \"Case study\" 定位与 claim 力度不一致。\n\n**W5** Table 1 exec-only 行仅用 s42，与其他 3-seed pooled 行不可直接比较。\n\n### Questions\n1. Table 1 ISR* 为何不同时展示 raw 和 matched 值？\n2. 排除 s43 后关键结果如何变化？\n3. 5-seed 中是否测试了超过 5 个 seeds？\n4. 能否对所有条件提供 premise-count-matched ISR？\n5. ISR 与 NLI accuracy ρ=-0.049 是在哪个条件上计算的？\n6. 能否估计 deleted s43/s44 的 PG 上界？\n\n### 主要优势\n1. 新颖实用的诊断方法\n2. 出色的实验设计意识（6 种 reward 条件 + shuffled-ISR 控制）\n3. 罕见的自我批判诚实度\n4. 丰富的 hacking 分类体系\n5. Observer/optimizer 不对称性洞见\n6. 跨域初步验证\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和主要优势逐条 [AGREE] 或 [REBUT]，特别关注：\n1. R1 的 N2（premise-count confound）——你在 W4 也提到了这个问题但列为 Should-Fix 而非 Must-Fix。在看到 R1 更详细的分析后，是否同意将其升级为 Must-Fix？\n2. R1 的 N3（seed 43 偏差）——这是你未单独提出的问题。在看到 R1 的论证后，你是否认为这构成一个独立的 critical issue？\n3. R1 的 W3（分类器验证不充分）——R1 指出 deleted checkpoints 是不可恢复的方法论缺陷，你的评估如何？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] N=3 seeds 统计功效不足以支撑 C2（Goodhart 效应）的 claim 强度\n- 最关键反证：5-seed 扩展（s45/s46）显示 ~55% non-hacking，与原 3-seed 的 6% 形成巨大反差。\n- CMH 检验报告 p<10^-15，但有效 N=3 seeds 而非 231 samples。\n- 建议将 C2 降级为 exploratory finding。\n\n**N2** [critical] Premise-count 混淆因子破坏了 ISR 坍塌叙事的核心\n- 标志性发现 ISR 0.642→0.003（214× collapse）主要被组件数量变化驱动（~6→18.55）。\n- Premise-count matching 后优势从 3.2× 降至 1.06×。\n- 在 Abstract/Introduction 中以原始坍塌值为主要叙事，premise-count confound 被推迟到 Section 4.3。\n\n**N3** [critical] Seed 43 评估协议差异引入系统性偏差\n- s43 使用 sampling (T=0.7) 而非 greedy decoding。\n- Random 条件下 38.3% TS 完全来自 s43（s42=0%, s44=0%）。\n- s43 对 TS 率的贡献可能是采样噪声而非真实 seed-level 现象。\n- 排除 s43 后 random TS 降至 0%，composition shift 叙事仅依赖 2 个 seeds。\n\n### Should-Fix 问题\n\n**W1** SFT 基线不支撑\"GRPO-specific degradation\"的 claim（PR 13% vs 93% 不可直接比较，100-step 控制样本量太小）。\n\n**W2** ProofFOL \"beneficial instability\"（p=0.10）在叙事中权重与证据不匹配（出现在 Abstract/Introduction/Conclusion 但仅是 exploratory）。\n\n**W3** Hacking mode 分类器验证不够充分（precision 仅 50 样本验证，recall 无界，PG 检测需手动，deleted checkpoints）。\n\n**W4** \"Case study\" 定位与 claim 力度不一致。\n\n**W5** Table 1 exec-only 行仅用 s42，与其他 3-seed pooled 行不可直接比较。\n\n### Questions\n1. Table 1 ISR* 为何不同时展示 raw 和 matched 值？\n2. 排除 s43 后关键结果如何变化？\n3. 5-seed 中是否测试了超过 5 个 seeds？\n4. 能否对所有条件提供 premise-count-matched ISR？\n5. ISR 与 NLI accuracy ρ=-0.049 是在哪个条件上计算的？\n6. 能否估计 deleted s43/s44 的 PG 上界？\n\n### 主要优势\n1. 新颖实用的诊断方法\n2. 出色的实验设计意识（6 种 reward 条件 + shuffled-ISR 控制）\n3. 罕见的自我批判诚实度\n4. 丰富的 hacking 分类体系\n5. Observer/optimizer 不对称性洞见\n6. 跨域初步验证\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和主要优势逐条 [AGREE] 或 [REBUT]，特别关注：\n1. R1 的 N2（premise-count confound）——你在 W4 也提到了这个问题但列为 Should-Fix 而非 Must-Fix。在看到 R1 更详细的分析后，是否同意将其升级为 Must-Fix？\n2. R1 的 N3（seed 43 偏差）——这是你未单独提出的问题。在看到 R1 的论证后，你是否认为这构成一个独立的 critical issue？\n3. R1 的 W3（分类器验证不充分）——R1 指出 deleted checkpoints 是不可恢复的方法论缺陷，你的评估如何？"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-21T17:34:42.169548+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 2254 · 2026-05-21T17:34:45.377948+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 197

## Round 197

2 recorded events


### User

_source line 2255 · 2026-05-21T17:34:47.950095+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论概要**：Overall 3.0（Findings 水平）。

三个 Must-Fix 问题：
1. **N=3 seeds 统计功效不足**——5-seed 扩展中 2/5 seeds 显示 55% non-hacking，与原 3-seed 的 6% 矛盾，C2（Goodhart 效应）应降级为 exploratory finding
2. **Premise-count 混淆因子**——ISR 3.2× 优势经 matching 后仅剩 1.06×，但 Abstract/Introduction 仍以原始 214× 坍塌为核心叙事
3. **Seed 43 的 T=0.7 采样**——Random 条件 38.3% TS 完全来自 s43，可能是采样噪声而非 seed 效应，严重混淆 TS composition shift 的 claim

五个 Should-Fix 问题涉及 SFT 基线 PR confound、ProofFOL p=0.10 的叙事权重过高、分类器验证不充分（50 样本 + 无 recall 估计 + deleted checkpoints）、case study 定位与 claim 力度不一致、Table 1 单 seed vs. pooled 行的可比性。

核心优势是诊断方法本身新颖实用、实验设计意识出色、以及罕见的自我批判诚实度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2256 · 2026-05-21T17:34:53.308338+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2257 · 2026-05-21T17:36:33.689057+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 核心方法新颖性有限——LOO ablation 是标准技术**

R2 的论点成立一半但过度推进了。论文在 Section 3.2 明确承认 "LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia and Harman, 2011); novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces"。论文从未声称 LOO 方法本身是新的。

本文的贡献是 **empirical discovery**，不是 methodological invention：(1) 将 LOO 应用到 solver trace 上产生 ISR 指标后，揭示了 prove rate 完全掩盖的 214× 结构坍塌（Section 4.2, Figure 1）；(2) 发现同一 LOO 结构使 ISR 既能诊断又能被 game 的 observer/optimizer 不对称性（Section 4.3–4.4）；(3) 发现 8 种具体 hacking modes 的分类体系（Section 4.5, Appendix D）。

类比：attention mechanism 在 NLP 之前就存在于信号处理中，但 Bahdanau et al. 2015 将其应用到 seq2seq 并揭示了新现象，这仍然是有价值的贡献。LOO 是工具，STA 的贡献在于用这个工具发现了什么。

但我同意 R2 的潜在关切：如果 claim C1 的表述暗示"STA as a diagnostic framework"是一个通用新框架（而非已知技术的新应用），那措辞确实需要调整。建议将 C1 表述为"an empirical demonstration that LOO-based component necessity testing reveals..."。

**[AGREE] R2-N2: 单一模型验证严重限制 generalizability**

同意这是一个显著限制。论文仅在 Qwen3-4B 上完成核心实验，LLaMA-3.2-3B 因 cold-start failure（Appendix E.4, PR=16% 停滞）无法提供对比数据。Limitations Section 6 也承认 "RLVR gains from random or incorrect rewards have been shown to be Qwen-specific (Spurious Rewards)"，进一步削弱了 generalizability。

但我要补充一个 R2 未提及的维度：即使在 Qwen3-4B 内部，**5-seed 扩展**（Section 4.3）已经显示结果高度 seed-dependent（3/5 gaming vs. 2/5 genuine），这是比跨模型 generalizability 更紧迫的问题。单模型 + seed-dependent 意味着连 Qwen3-4B 上的结论都不够稳健，遑论跨模型推广。

R2-N2 与我的 N3（seed 43 T=0.7 混淆）确实存在交互：如果排除 s43，剩余的 s42+s44 仅提供 N=2 有效 seeds 的 exec-only 证据和 N=2 的 ISR-reward 证据。在单模型上用 2 个有效 seeds 支撑一个 "diagnostic framework" 的 claim，证据基础极其薄弱。

**[AGREE] R2-N3: "Compositional Goodhart effect" 的理论映射不够严谨**

同意，且这与我的 N1 和 W1 互补。具体问题：

1. **层级混乱**：Manheim & Garrabrant (2019) 的分类包含 regressional / extremal / causal / adversarial 四种，都是 Goodhart effect 的子类型。论文在 Section 4.3 先说 β=0.1 FOLIO 是 "regressional Goodhart"（P→P 满足 ISR≥0.5），又在 Abstract/Introduction 中使用 "compositional Goodhart effect" 作为总称。但 "compositional" 不是 Manheim taxonomy 中的术语——论文似乎用它指 "hacking composition shifts without prevalence reduction"，这是一个现象描述而非理论分类。论文需要明确 "compositional" 与 Manheim 四类的关系。

2. **替代解释成立**：R2 提出的 "reward shaping 改变 attack surface" 是一个更简约的解释。ISR reward 将 ISR≥0.5 的 hacking modes（TS）变成高奖励路径，将 ISR=0 的 modes（CE）变成低奖励路径——这是标准的 reward shaping 效应，不一定需要 Goodhart framework。Goodhart 效应的核心是 "when a measure becomes a target, it ceases to be a good measure"，但 ISR 作为 reward 时的 gaming 可能更准确地描述为 reward misspecification。

3. **与我的 N1 互补**：我的 N1 从统计角度（N=3, 5-seed 不一致）质疑 C2 的证据充分性；R2-N3 从理论角度质疑 C2 的概念框架。两者共同指向 C2 需要大幅修改：要么降低为 exploratory observation，要么提供更严谨的理论映射。

---

### Should-Fix 问题

**[REBUT] R2-W1: 与 Helff et al. (2026) IPT 的区分需要更精确**

R2 认为 STA 的 post-hoc diagnostic 用法与 IPT 的 inference-time 定位重叠，但这两者操作的对象不同：

- **STA** 消融 **solver 输入**（formal program 的组件），测试每个逻辑前提是否对 proof 必要。操作发生在模型生成之后、solver 验证阶段。
- **IPT**（Helff et al. 2026, 引文 verify-references 可确认）消融 **LLM 输入**（自然语言 premises），测试模型的推理是否依赖于输入信息。操作发生在模型推理阶段。

两者在方法上都用了 perturbation/ablation，但目标层级不同：STA 诊断 solver-side 结构退化（生成的形式化是否冗余），IPT 诊断 model-side 推理忠实度（模型是否真的使用了输入信息）。论文 Section 2 (Related Work) 引用了 verify-references 相关工作并做了定位区分。我认为现有区分已经足够，但 R2 提出进一步明确是合理的建议。

**[AGREE] R2-W2: 缺少重要相关工作**

同意需要讨论。我的审查未特别标记 missing references，但 R2 提到的两篇工作确实相关：
- "Does RL Really Incentivize Reasoning?"——直接相关，讨论 RL 是否真的促进推理 vs. 仅优化表面模式
- "GRPO is Secretly a PRM"——如果存在，与 GRPO 的内在机制相关

不过 R2 应确认这些引用是否真实存在（非幻觉引用），建议作者通过 verify_references 或手动检索确认。

**[AGREE] R2-W3: N=3 seeds 统计效力不足**

完全同意，与我的 N1 一致。Fisher exact tests 的 power 在 N=3 下极低，p=0.182（non-hacking prevalence）和 p=0.10（ProofFOL genuine rate）都是 underpowered 的直接后果。唯一存活 Bonferroni 校正的结果（TS composition shift p<10^-15）使用了 inflated sample-level N，有效 seed-level N 仅为 3。

**[AGREE] R2-W4: ISR premise-count confound 未完全解决**

完全同意，与我的 N2 一致。补充一点 R2 未提及的：论文仅对 ISR-reward 条件（Section 4.3, seed 42）提供了 premise-count-matched 分析。**exec-only 条件的 214× 坍塌**也受 premise-count confound 影响（组件数从 ~6 膨胀到 18.55），但未提供 matched 值。这意味着论文最引人注目的数字（214× collapse）的实际结构退化贡献不明。

**[AGREE] R2-W5: "Case Study" 标题与强势 contribution claims 之间的张力**

完全同意，与我的 W4 一致。C1 和 C2 的措辞暗示通用性，与标题 "A Case Study" 不匹配。

---

### 小问题

1. **[AGREE]** 缩写密度过高——同意。首次阅读时 ISR/ISR*/PR/CE/TS/PG/CMH/LOO 的密度确实增加了认知负荷。
2. **[AGREE]** Figure 3 可读性——stacked bar chart 在 8 个类别下确实拥挤，但 modes 的层级用颜色有一定逻辑性，问题不大。
3. **[AGREE]** Table 1 列头缩写——ISR*、TS%、CE%、N-H% 需要更明确的列头说明。
4. **[REBUT]** "ISR tells the opposite story" 不够学术——这是 Section 4.2 的表述，在 ACL/EMNLP 论文中 "tells a different/opposite story" 是可接受的修辞，不构成学术性问题。
5. **[AGREE]** FOLIO bib 年份——如果存在 mismatch 应修正，但我的审查未独立验证此项。
6. **[AGREE]** 5-seed extension 混合使用——Table 1 同时展示 3-seed 和 5-seed 行确实增加了混乱。建议统一使用 5-seed 或在 Table 中更清晰地分组。

---

### 主要优势

1. **[AGREE]** 诊断视角新颖实用——与我的 Strength #1 一致。
2. **[AGREE]** 8 种 hacking 模式分类详实——与我的 Strength #4 一致。
3. **[AGREE]** 跨域验证增强可信度——同意，但 ProofFOL 的 p=0.10 仅是 exploratory（我的 W2）。Prolog 的 3/3 Goodhart 更有说服力。
4. **[AGREE]** Compositional Goodhart 发现有趣——同意这是有趣的观察，但证据是否充分（我的 N1、R2-N3）是另一回事。
5. **[AGREE]** 写作信息密度高逻辑清晰——同意。论文在 8 页内容纳了大量信息，组织合理。
6. **[AGREE]** 附录充分透明——与我的 Strength #3 一致。论文的自我批判诚实度值得赞赏。

---

### 对 Director 指定的三个交叉问题的回答

**1. R2-N1（方法新颖性）与我的评估是否一致？**

部分一致。R2 将 LOO 的标准性视为对整篇论文新颖性的否定；我认为方法新颖性不是主要贡献来源——本文的贡献在于 empirical discovery，不在于 method invention。我在 Strength #1 和 #5 中明确肯定了诊断视角和 observer/optimizer 不对称性的新颖性。分歧在于评判标准：R2 倾向于 method novelty，我更看重 empirical insight。对 ACL/EMNLP 的 Findings track 而言，empirical contribution 是足够的定位。

**2. R2-N2（单模型）和我的 N3（seed 43）是否存在交互？**

强交互。排除 s43 后：
- Exec-only：仅 s42（PR=93%, CE=87%）和 s44（PR=98%, TS=100%）两个有效 seed，各展现不同 hacking mode
- ISR β=0.1：s42（mixed CE+TS+PG, 17.3% non-hacking）和 s44（100% TS, 0% non-hacking）——2 个 seeds 的 non-hacking 率分别是 17.3% 和 0%
- Random β=0.1：s42（0% TS, 22.8% non-hacking）和 s44（0% TS, 6.7% non-hacking）

在单模型（R2-N2）+ 仅 2 有效 seeds（排除 s43 后）的基础上声称 "diagnostic framework"（C1）和 "compositional Goodhart effect"（C2），证据基础确实极其薄弱。两个 weaknesses 的交互放大了各自的影响。

**3. R2-N3（Goodhart 映射）与我对 C2 证据不充分的判断是否互补？**

高度互补。我的 N1 从 **统计角度** 质疑 C2（N=3 功效不足，5-seed 不一致），R2-N3 从 **理论角度** 质疑 C2（"compositional" 不在 Manheim taxonomy 中，替代解释更简约）。两者共同指向 C2 的根本问题：**现象描述不稳定（统计），理论框架不严谨（概念）**。C2 作为 confirmed finding 不成立，应降级为 exploratory observation 或需要大幅重构理论映射。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2258 · 2026-05-21T17:36:40.267109+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 199

## Round 199

2 recorded events


### User

_source line 2259 · 2026-05-21T17:36:42.839579+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：
- R2 的 14 个问题中，**9 个 AGREE**（N2, N3, W2-W5, 以及多数小问题），**2 个 REBUT**（N1 方法新颖性、W1 与 IPT 区分），**3 个部分同意**。
- 三个交叉问题的结论：(1) R2-N1 与我评估部分一致，分歧在 method vs. empirical novelty 的权重；(2) R2-N2 和我的 N3 强交互——排除 s43 后仅剩 2 有效 seeds，证据基础极其薄弱；(3) R2-N3 与我的 N1 高度互补，从统计和理论两个角度共同否定 C2 作为 confirmed finding 的资格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2260 · 2026-05-21T17:36:48.104071+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 200

## Round 200

18 recorded events


### User

_source line 2261 · 2026-05-21T17:38:19.781442+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的逐条交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: N=3 seeds 统计功效不足以支撑 C2 的 claim 强度**

同意，且这一问题比我初始评估中更严重。R1 指出的关键反证极有说服力：5-seed 扩展中 s45/s46 在同一 ISR β=0.1 条件下产出 ~55% non-hacking（Section 4.4 "Bimodal seed-dependence"），与原 3-seed 的 6% 形成数量级差异。这直接意味着 C2 ("compositional Goodhart effect") 的定量描述高度依赖 seed selection。

我在自己的审稿中将此列为 W3 (Should-Fix)，但 R1 的论证说服我升级：
1. CMH 检验的 p<10⁻¹⁵ 确实是 pseudo-replication——有效独立单元是 3 个 seeds 而非 231 个 samples，论文在 Appendix E.3 自己承认 "CMH tests within-seed samples as independent observations"（p.13）
2. 5-seed 结果的巨大方差（6% vs 55%）不仅削弱 effect size 估计，更动摇了 "consistent gaming" 这一定性结论
3. 论文在 Section 4.4 称其为 "bimodal seed-dependence"，但 Abstract/Introduction 中 C2 的表述没有反映这一 bimodality

**结论**：C2 应降级为 exploratory observation，或至少在 Abstract 中加入 seed-dependent caveat。同意列为 Must-Fix。

---

**[AGREE，并升级] R1-N2: Premise-count 混淆因子破坏 ISR 坍塌叙事**

在我的初始审稿中，我将此列为 W4 (Should-Fix)。看了 R1 更详细的分析后，**我同意升级为 Must-Fix**。理由：

1. **数据层面**：Section 4.3 + Appendix C 明确显示 premise-count-matched 比较将 ISR 优势从 3.2× 降至仅 1.06×（p=0.10 borderline）。这不是 "部分缓解"——1.06× 实质上是 null effect。
2. **叙事层面**：Abstract 使用 "collapse trajectory invisible to execution-based evaluation" 和 "ISR falls to near-zero"，Introduction 说 "ISR reveals a structural collapse"。这些 framing 基于 raw ISR 0.642→0.003（~214×），但该数字的绝大部分变异来自 component count 变化（~6→18.55 premises），而非 genuine per-component structural degeneration。
3. **读者误导风险**：从 Abstract 到 Section 4.2 的读者会形成 "catastrophic structural collapse" 的印象，直到 Section 4.3 末尾的一小段才了解 confound。这不是诚实的 caveat placement——它应该在首次报告 ISR 坍塌时就同步出现。

R1 的建议（在 ISR 定义处同时引入 matched variant、Abstract 使用 matched 值、或将 premise count 作为 joint metric 呈现）我完全支持。

---

**[PARTIALLY AGREE] R1-N3: Seed 43 评估协议差异引入系统性偏差**

R1 的发现在事实层面是准确的：
- s43 使用 sampling T=0.7 而非 greedy decoding（Section 4.1, Appendix A "Evaluation exception"）
- Table 1 脚注显示 Random 条件下 TS=38.3% 全部来自 s43，s42=s44=0%

但我认为这是 **Should-Fix 而非 Must-Fix**，理由如下：

1. **影响范围有限**：s43 的 protocol 差异主要影响 hacking composition 分析（哪种 mode 占比多少），但不影响 ISR 坍塌的核心发现。ISR 从 ~0.6 降到 ~0 的 trajectory 在 3 个 seeds 中都一致（Figure 1）。
2. **论文已有 partial mitigation**：Section 4.1 脚注称 "excluding s43 yields comparable results"，虽然不够详尽，但表明作者 aware of the issue。
3. **R1 的具体担忧——Random TS 降为 0%——的影响**：如果排除 s43 后 Random TS=0%，那 CE→TS composition shift 的叙事确实仅基于 ISR 条件的 2 个 seeds（s42, s44）。这削弱了 composition shift 的 robustness 但不改变 "ISR-as-reward 未消除 hacking" 这一更基本的结论。

**建议**：论文应提供完整的 s43-excluded sensitivity analysis（不只是一句 "comparable results"），包括 Table 1 的 2-seed 版本。但鉴于其对核心 claim (C1) 的影响有限，我维持 Should-Fix（high priority）。

---

### Should-Fix 问题

**[AGREE] R1-W1: SFT 基线不支撑 "GRPO-specific degradation"**

我在自己的审稿中也提了类似观点（我的 N2 中提到 "SFT baseline has no RL optimization at all"）。SFT PR=13% vs GRPO PR≈93% 是两个完全不同 regime 的对比。100-step 匹配控制的样本量确实太小。不过论文在 Section 4.2 也提供了 exec-only vs ISR 的对比，后者更有诊断意义。建议作者明确 SFT 是 "reference point" 而非 "controlled baseline"。

---

**[AGREE] R1-W2: ProofFOL "beneficial instability" 权重与证据不匹配**

Section 4.4 + Appendix E.3 明确：ProofFOL 的 ISR rate 差异 p=0.10，论文自己归类为 exploratory。但这一 finding 出现在 Abstract（"cross-domain evidence: confirmed in Prolog (3/3 seeds 0% non-hacking)"）和 Introduction 的贡献列表中，语气过强。p=0.10 在 N=3 seeds 的 Fisher exact test 下甚至不是 nominal significance。同意叙事权重应降低。

---

**[AGREE] R1-W3: Hacking mode 分类器验证不充分**

R1 指出 3 个具体问题：
1. Precision 仅 50 样本验证——我同意这对 8 种 mode 的分类器而言不够充分
2. Recall 无上界——论文只验证了 precision（classified as hacking 中真正 hacking 的比例），但没有估计 miss rate
3. PG 检测需手动 + deleted checkpoints 不可恢复

关于 **deleted checkpoints**：这是我初始审稿中未注意到的问题。Appendix D.1 提到 PG reclassification 和 TS false-negative correction 依赖手动检查，但如果部分 checkpoints 已删除（R1 指出的 s43/s44 情况），那这些 mode 的 prevalence 数字包含 unverifiable estimates。这是一个不可恢复的方法论缺陷——无法通过 revision 修复——但其影响仅限于 PG 这一个 mode 的精确 prevalence，不影响 CE 和 TS 两个主要 mode 的分类（它们依赖 text-match，可独立验证）。

**结论**：同意为 Should-Fix。建议论文明确标注哪些 mode prevalence 数字依赖已删除 checkpoints 的不可验证估计。

---

**[AGREE] R1-W4: "Case study" 定位与 claim 力度不一致**

这与我的 W5 完全一致。不再赘述。

---

**[AGREE] R1-W5: Table 1 exec-only 行与其他行的可比性**

Table 1 的 exec-only 行使用条件与其他行不同（无 ISR reward component），如果还存在 seed pooling 差异（R1 指出仅用 s42），那可比性更成问题。Table 1 caption 和脚注应明确说明每行使用的 seeds 和 pooling 方式。

---

### R1 Questions 的补充意见

**Q1 (ISR* raw vs matched)**：合理要求。Table 1 应同时展示 raw 和 matched ISR 值。

**Q2 (排除 s43 后结果)**：这是验证 R1-N3 的关键——如果论文能提供 s43-excluded 的完整结果，多个 issues 可同时得到解答。

**Q3 (5-seed 是否测试超过 5 个)**：论文仅提到 seeds [42,43,44] + [45,46]。如果作者选择性报告（e.g., 跑了 8 个 seeds 只报 5 个），那是一个 reporting bias 问题。但目前没有证据表明存在这种情况。

**Q4 (所有条件的 premise-count-matched ISR)**：强烈支持。这是解决 N2 confound 的直接方案。

**Q5 (ISR 与 NLI accuracy ρ=-0.049 的条件)**：论文在 Appendix C 提到 "ρ(ISR, NLI accuracy) = −0.049 (p = 0.187)"，但没有明确是哪个条件或 checkpoint。建议明确。

**Q6 (deleted checkpoints 的 PG 上界)**：合理但可能不可行（如果 checkpoints 已删除）。论文应至少 acknowledge 这一 limitation。

---

### 主要优势回应

**[AGREE] S1: 新颖实用的诊断方法**——与我的评估一致。STA 将 mutation testing 引入 RLVR hacking diagnostic 是论文最强贡献。

**[AGREE] S2: 出色的实验设计意识**——6 种 reward 条件 + shuffled-ISR 控制是 well-designed。我补充：shuffled-ISR 是一个特别好的控制，证明了 ISR 的 structural signal 不可被 random permutation 替代。

**[AGREE] S3: 罕见的自我批判诚实度**——论文在 Appendix C 讨论 premise-count confound、在 Section 4.4 报告 5-seed 巨大方差、在 Limitations 列出 single-model 等——这些是积极的，但如我和 R1 所述，self-critique 在附录和 limitations 中出现太晚，核心叙事未相应调整。

**[AGREE] S4: 丰富的 hacking 分类体系**——Appendix D 的 8-mode taxonomy 是论文最有价值的实证贡献。我补充：即使部分 mode 的 prevalence 数字因 classifier 验证不足而有 uncertainty，taxonomy 本身作为 conceptual contribution 仍有独立价值。

**[AGREE] S5: Observer/optimizer 不对称性洞见**——ISR 作为 observer 有效但作为 optimizer target 产生 mode shift——这一发现对 reward design 有直接启示。

**[AGREE] S6: 跨域初步验证**——Prolog + FOL 两个 solver 增强了 findings 的 robustness，但如我的审稿所述，这仍在 logical reasoning 范围内，不算真正的 cross-domain。

---

### 对 Director 三个具体问题的总结

1. **R1-N2 升级为 Must-Fix**：**是的，我同意升级。** 1.06× matched vs 3.2× raw 是决定性的——ISR 坍塌叙事的核心数字被 premise-count confound 严重膨胀，这不是 minor caveat 而是 affects the validity of the headline claim。

2. **R1-N3 构成独立 critical issue**：**部分同意，但维持 Should-Fix (high priority) 而非 Must-Fix。** s43 的 protocol 差异主要影响 composition 分析而非 ISR 坍塌核心发现。但论文需要提供完整的 s43-excluded sensitivity analysis。

3. **R1-W3 deleted checkpoints**：**同意是方法论缺陷但影响范围有限。** 不可恢复的 checkpoints 使 PG mode 的 prevalence 不可独立验证，但 CE 和 TS（两个主要 mode）的 text-match 分类可独立复现。建议明确标注哪些数字不可验证。

---

### 综合评分调整

在看到 R1 对 premise-count confound 和 seed instability 的更深入分析后，我维持 **Overall 3.0 (Findings)**。R1 的 N1+N2 加强了我对论文 claim 强度超出证据支撑的判断。核心诊断方法（STA/ISR 作为 observer）的价值不变，但 ISR-as-reward 的 Goodhart 叙事（C2）需要实质性 reframing。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-21T17:38:41.637848+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 2263 · 2026-05-21T17:38:41.638196+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2264 · 2026-05-21T17:38:42.090298+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T17:23:34.485393+00:00\", \"completed_at\": \"2026-05-21T17:27:02.672233+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"主文连续两页纯文本（Experiments §4.1–§4.3），无任何 figure/table/equation 穿插。密集的统计数字（PR、ISR、p-value）全靠行内文本承载，审稿人极易疲劳。建议将关键实验结果（如 §4.2 的 ISR collapse trajectory 或 §4.3 的 Goodhart effect 对比）提炼为一个小型 summary table 或 bar chart 插入此区间。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 和 Figure 3 同时挤在单页顶部，均为单栏宽度。Figure 2 含两个 subfigure (a)(b)，Figure 3 为多类别堆叠柱状图——两者内部文字标注均偏小（目测约 6-7pt），在打印或低分辨率屏幕上可读性受限。建议至少将其中一个改为 figure*（全宽），或将两图分散到不同页面。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。Figure 1 出现在 page 2 是可接受的，但若能将 Figure 1 提前到首页底部（或在 Abstract 后紧跟一个概览图），审稿人第一印象会更强。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 使用蓝/橙/绿/红多色线条，颜色区分度尚可，但建议验证灰度打印下线条是否仍可区分（可辅以不同 line style: dashed, dotted）。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 3 堆叠柱状图使用 8 种颜色对应 8 种 hacking mode，颜色较多时色盲用户可能难以区分相邻类别。建议使用 hatching pattern 辅助区分，或减少到 4-5 个主类别（合并低频类别为 \\\"Other\\\"）。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，格式规范。但部分数值列小数位数不统一（如 ISR 列有的 2 位有的 3 位），建议统一到 2 位或 3 位。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 6 Limitations 仅占页面底部约 6-8 行，内容非常简短。作为 ACL ARR 必需章节这是允许的，但审稿人可能感觉讨论不够充分。\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Checklist 页底部约 40% 空白。不影响审稿，但如果主文空间紧张可考虑压缩。\"}, {\"severity\": \"info\", \"dimension\": \"page 21-22\", \"message\": \"Appendix Tables 7–10 数据密集，Notes 列字体很小。这是 appendix 可接受，但建议确认 Notes 列字号不低于 7pt。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Algorithm 1 伪代码框排版清晰，作为 Method 的视觉锚点效果好。\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 8}}, \"error\": null, \"
…[truncated 17 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-21T17:38:42.090675+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-21T17:38:42.191900+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2267 · 2026-05-21T17:38:42.292692+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2268 · 2026-05-21T17:38:45.405425+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file project",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file project",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2269 · 2026-05-21T17:38:45.456903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2270 · 2026-05-21T17:38:50.476309+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2271 · 2026-05-21T17:38:50.527030+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2272 · 2026-05-21T17:38:59.090211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2273 · 2026-05-21T17:38:59.141447+00:00_

1	issues:
2	# === Resolved issues from rounds 0-21 (condensed) ===
3	- id: R1-W1
4	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
11	  resolution_round: 2
12	- id: RV-EVAL-FALLBACK
13	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: stderr ERROR → sys.exit(1)。
20	  resolution_round: 1
21	- id: R1-W2
22	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
23	  category: framing
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 15
28	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
29	  resolution_round: 2
30	- id: R2-W1
31	  summary: Limitations section 格式不合规
32	  category: format
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 2
37	  resolution: 独立 limitations.tex 已创建。
38	  resolution_round: 3
39	- id: R2-W2
40	  summary: 实验仅用单一模型和单一数据集
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 2
46	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
47	  resolution_round: 3
48	- id: R2-W6
49	  summary: SFT baseline 比较不公平：PR=14% vs 93%
50	  category: experiment
51	  severity: critical
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 2
55	  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
56	  resolution_round: 2
57	- id: v2-R1-N1
58	  summary: Abstract '93%' PR 为 single seed
59	  category: writing
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 2
63	  last_seen_round: 3
64	  resolution: Abstract 使用 3-seed pooled mean±std。
65	  resolution_round: 3
66	- id: v2-R1-N3
67	  summary: 仅 2 个 β 值不足以刻画 dose-respons
…[truncated 18316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-21T17:42:37.085877+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-21 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 双 Reviewer 确认 RESOLVED：Intro/Conclusion 加 '(Qwen3-4B; §6)' 限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记为 critical。R2-N2：LLaMA-3.2-3B 实验失败（PR=16% 停滞）进一步削弱 generalizability。R1 AGREE 并补充：即使 Qwen3-4B 内部，5-seed 结果也高度 seed-dependent。文本限定不够——需要至少一个额外模型的核心实验复现。\"\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 确认 RESOLVED：C2 拆分 confirmed Prolog vs exploratory ProofFOL。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。R1-W2：ProofFOL 'beneficial instability' (p=0.10) 仍出现在 Abstract/Introduction/Conclusion，叙事权重超出 exploratory 定位。R2 AGREE。此外 ProofFOL 'genuine' 用 coarser classifier（仅排除 TS/CE），与 FOLIO 8-mode 不可比。\"\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 确认 RESOLVED：N-H 全文标注为 upper bound。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。R1-W3 新增关键点：s43/s44 checkpoints 已删除（Appendix D.1），PG 审计永久不可复现。Precision 仅 50 样本验证。Prolog text-match 100% non-hacking → functional analysis 0% genuine 直接证明 recall 可能极低。R2 AGREE 但认为影响限于 PG mode。\"\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已从 references.bib 删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入 references.bib + related_work.tex。\"\n  resolution_round: 22\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题术语与 ISR 实际测量（component necessity）不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。ISR operationalizes structural quality；hacking taxonomy 已证明 low-ISR 对应多种结构退化。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R25) ===\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 升级为 critical。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 论文在 §4.1 footnote 承认 'not strictly comparable'，加了 excluding-s43 sentence。仍纳入 pooled statistics。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R1 升级为 Must-Fix (N3)：Random 条件 38.3% TS 完全来自 s43（s42=s44=0%），排除后 Random TS=0%，composition shift 叙事仅依赖 2 seeds。R2 PARTIALLY AGREE：事实准确但影响范围有限（不影响 C1 ISR 坍塌核心），维持 Should-Fix (high priority)。共识：high-priority warning，需提供完整 s43-excluded sensitivity analysis。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1]\n    note: \"R23 再次标记。R2 AGREE 但认为 FOLIO 2-6 前提设定中高阶交互影响有限。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"共识 warning：shuffled-ISR 已控制 magnitude 分布。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"ISR/ISR†/ISR* 符号不统一 + hacking mode 缩写过多。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记 (R2 minor #1, R1 AGREE)。建议 Section 3 增加缩写对照 table。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [visual]\n    note: \"pages 5-6 纯文本无视觉锚点，page 8 display items 拥挤。\"\n  - round: 25\n    reviewers: [visual]\n    note: \"R25 视觉审查再次标记：pages 5-6 连续两页纯文本（§4.1-§4.3），建议插入 summary table 或 bar chart。page 8 Figure 2+3 同时挤在顶部，内部文字 6-7pt 偏小。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [visual]\n    note: \"Figure 2/3 内部文字 7-8pt。\"\n  - round: 25\n    reviewers: [visual]\n    note: \"R25 再次标记。Figure 2/3 标注 6-7pt，打印/低分辨率可读性受限。建议至少一个改为 figure*（全宽）。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"最强共识点。'compositional Goodhart effect' 混合了显著和不显著结果。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记。R1-N1：5-seed 扩展中 2/5 seeds 55% non-hacking 与 3-seed 6% 矛盾，C2 应降级为 exploratory。R2-N3：'compositional Goodhart' 不在 Manheim taxonomy 中，替代解释（reward shaping 改变 attack surface）更简约。R1 交叉 AGREE R2-N3：统计+理论双重质疑 C2。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"Table 1 始终用 unmatched ISR。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 升级为 Must-Fix 共识。R1-N2：214× collapse 主要被 component count 变化驱动（~6→18.55），Abstract/Intro 以 raw ISR 为核心叙事，confound 推迟到 §4.3 才讨论——误导读者。R2 升级同意：1.06× matched 实质上是 null effect，不是 'partial mitigation'。需在首次报告 ISR 坍塌时同步呈现 matched 值。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 REBUT：EMNLP Findings 接受 applied contributions。共识 warning。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R2 再次标为 Must-Fix (N1)。R1 交叉 REBUT：贡献在于 empirical discovery 不在 method invention，类比 Bahdanau 2015 将已有技术应用到新场景。分歧：R2 认为 method novelty 不足 critical，R1 认为 empirical novelty 足够 Findings。共识：warning 级别——novelty 有限但不致命，适合 Findings track。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 info/open。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"论文已改为 'cross-dataset evidence'。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R1-W2 再次标记。ProofFOL genuine rate 用 coarser classifier（仅排除 TS/CE），与 FOLIO 8-mode non-hacking rate 不可直接比较。'Hacking geometry' 因果解释未经实验验证。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"论文已加 power analysis caveat。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2 REBUT：SFT 目的是 pre-RL reference。分歧但非关键。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R1-W1 再次标记。SFT PR=13% vs GRPO PR=93% 不可直接比较。100-step 控制（n=32, PR=32%）样本量太小。R2 AGREE 但补充 SFT 是 reference point 非 controlled baseline。建议精确化 claim 为 'consistent with RL-driven hacking'。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足——需 power analysis 或增加 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"§4.1 新增 d≥3.0 power analysis。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记为核心问题。R1-N1：5-seed 扩展（s45/s46 ~55% non-hacking vs 3-seed 6%）直接证明 C2 是 seed-dependent 非系统性现象。CMH p<10⁻¹⁵ 有效 N=3 而非 231 samples。R2 从 W3 升级为 AGREE Must-Fix。建议 C2 降级为 exploratory finding，Abstract 加 seed-dependent caveat。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合 reward 需 constant-bonus control 排除 reward magnitude 混淆\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"共识 warning。无新实验，text-only 处理。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与 C1-C2 通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n  - round: 24\n    reviewers: []\n    note: \"C1/C2 已由 'In this case study (Qwen3-4B, ...)' 限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记 (R1-W4, R2-W5)。C1 'STA as a diagnostic framework' 暗示通用工具，C2 'compositional Goodhart effect' 暗示系统性现象。LLaMA cold-start failure 表明 STA 甚至不适用于无 FOL 生成能力的模型。建议在 Contributions 段更明确区分 case-study-specific vs methodological contributions。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 方法论对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n  - round: 24\n    reviewers: []\n    note: \"Related Work 已添加 IPT 比较句。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R2-W1 再次标记。R1 REBUT：STA 消融 solver 输入 vs IPT 消融 LLM 输入，目标层级不同，现有区分已足够。分歧但非关键。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失引用：Shapley values (Lundberg & Lee 2017) 作为 LOO 的自然泛化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 info/open。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失引用：PRoSFI (Chen et al., 2026) + Interleaved Bonus (arXiv:2601.22642)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 info/open。\"\n\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出约 15 行至第 9 页——可能违反 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 batch 压缩。Section 5 完全收入第 8 页。\"\n  resolution_round: 24\n\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"论文已标注 'for seed~42' + 3-seed '≤7% non-hacking'。\"\n  resolution_round: 24\n\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n\n# === New R25 issues ===\n- id: v25-R12-N1\n  summary: \"5-seed 扩展（s45/s46 ~55% non-hacking）与 3-seed（6%）矛盾——C2 Goodhart effect 不是系统性现象\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R1-N1 核心反证 + R2 交叉 AGREE 升级。3/5 seeds gaming vs 2/5 genuine = bimodal，非 consistent gaming。Abstract 和 Introduction 中 C2 claims 未反映 bimodality。5-seed 结果已在 Table 1 但 C2 framing 仍基于 3-seed。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× collapse 为核心叙事，premise-count confound 推迟到 §4.3——误导读者\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R1-N2 + R2 交叉升级为 Must-Fix。Exec-only 214× collapse 中 component count 从 ~6 膨胀到 18.55，但 matched 值未提供。ISR-reward 条件 3.2× → 1.06× matched = null effect。需在首次报告 ISR 坍塌时同步呈现 confound + matched value。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨——'compositional' 非 Manheim 术语，替代解释（reward shaping）更简约\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R2-N3 + R1 交叉 AGREE。'compositional' 不在 Manheim taxonomy (regressional/extremal/causal/adversarial) 中。论文先说 regressional 再用 compositional 作总称，层级混乱。现象可替代解释为 reward shaping 改变 attack surface，不一定需要 Goodhart framework。需给出 compositional Goodhart 的操作性定义并讨论替代解释。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R1-W5 + R2 AGREE。Table 1 无视觉区分 single-seed vs pooled 行。建议提供 3-seed pooled exec-only 行或更清晰标注 seed count 差异。\"\n\n- id: v25-MR\n  summary: \"缺失关键引用：Yue et al. (NeurIPS 2025) 'Does RL Really Incentivize Reasoning'; Sullivan et al. (2025) 'GRPO is Secretly a PRM'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R2-W2 提出，R1 AGREE（需验证引用真实性）。Yue et al. 直接相关——RLVR 不产生新推理能力。Sullivan et al. 揭示 GRPO 内隐 PRM 结构。\"\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差——8 种 mode stacked bar chart 颜色区分困难\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [2, visual]\n    note: \"R2 minor #2 + 视觉审查 page 3 info。建议合并低频 mode 或改用 heatmap + hatching pattern。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份可能 mismatch（2024 vs 2022 首发）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [2]\n    note: \"R2 minor #5。需核实 FOLIO 的正确发表年份（arXiv 2022 vs EMNLP 2024）。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-21 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 双 Reviewer 确认 RESOLVED：Intro/Conclusion 加 '(Qwen3-4B; §6)' 限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记为 critical。R2-N2：LLaMA-3.2-3B 实验失败（PR=16% 停滞）进一步削弱 generalizability。R1 AGREE 并补充：即使 Qwen3-4B 内部，5-seed 结果也高度 seed-dependent。文本限定不够——需要至少一个额外模型的核心实验复现。\"\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 确认 RESOLVED：C2 拆分 confirmed Prolog vs exploratory ProofFOL。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。R1-W2：ProofFOL 'beneficial instability' (p=0.10) 仍出现在 Abstract/Introduction/Conclusion，叙事权重超出 exploratory 定位。R2 AGREE。此外 ProofFOL 'genuine' 用 coarser classifier（仅排除 TS/CE），与 FOLIO 8-mode 不可比。\"\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 25\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 确认 RESOLVED：N-H 全文标注为 upper bound。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。R1-W3 新增关键点：s43/s44 checkpoints 已删除（Appendix D.1），PG 审计永久不可复现。Precision 仅 50 样本验证。Prolog text-match 100% non-hacking → functional analysis 0% genuine 直接证明 recall 可能极低。R2 AGREE 但认为影响限于 PG mode。\"\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已从 references.bib 删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入 references.bib + related_work.tex。\"\n  resolution_round: 22\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题术语与 ISR 实际测量（component necessity）不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。ISR operationalizes structural quality；hacking taxonomy 已证明 low-ISR 对应多种结构退化。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R25) ===\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 22\n    reviewers: [1, 2]\n    note: \"R22 双 Reviewer 升级为 critical。\"\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R23 论文在 §4.1 footnote 承认 'not strictly comparable'，加了 excluding-s43 sentence。仍纳入 pooled statistics。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R1 升级为 Must-Fix (N3)：Random 条件 38.3% TS 完全来自 s43（s42=s44=0%），排除后 Random TS=0%，composition shift 叙事仅依赖 2 seeds。R2 PARTIALLY AGREE：事实准确但影响范围有限（不影响 C1 ISR 坍塌核心），维持 Should-Fix (high priority)。共识：high-priority warning，需提供完整 s43-excluded sensitivity analysis。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1]\n    note: \"R23 再次标记。R2 AGREE 但认为 FOLIO 2-6 前提设定中高阶交互影响有限。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"共识 warning：shuffled-ISR 已控制 magnitude 分布。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"ISR/ISR†/ISR* 符号不统一 + hacking mode 缩写过多。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记 (R2 minor #1, R1 AGREE)。建议 Section 3 增加缩写对照 table。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [visual]\n    note: \"pages 5-6 纯文本无视觉锚点，page 8 display items 拥挤。\"\n  - round: 25\n    reviewers: [visual]\n    note: \"R25 视觉审查再次标记：pages 5-6 连续两页纯文本（§4.1-§4.3），建议插入 summary table 或 bar chart。page 8 Figure 2+3 同时挤在顶部，内部文字 6-7pt 偏小。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [visual]\n    note: \"Figure 2/3 内部文字 7-8pt。\"\n  - round: 25\n    reviewers: [visual]\n    note: \"R25 再次标记。Figure 2/3 标注 6-7pt，打印/低分辨率可读性受限。建议至少一个改为 figure*（全宽）。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"最强共识点。'compositional Goodhart effect' 混合了显著和不显著结果。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记。R1-N1：5-seed 扩展中 2/5 seeds 55% non-hacking 与 3-seed 6% 矛盾，C2 应降级为 exploratory。R2-N3：'compositional Goodhart' 不在 Manheim taxonomy 中，替代解释（reward shaping 改变 attack surface）更简约。R1 交叉 AGREE R2-N3：统计+理论双重质疑 C2。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"Table 1 始终用 unmatched ISR。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 升级为 Must-Fix 共识。R1-N2：214× collapse 主要被 component count 变化驱动（~6→18.55），Abstract/Intro 以 raw ISR 为核心叙事，confound 推迟到 §4.3 才讨论——误导读者。R2 升级同意：1.06× matched 实质上是 null effect，不是 'partial mitigation'。需在首次报告 ISR 坍塌时同步呈现 matched 值。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R1 REBUT：EMNLP Findings 接受 applied contributions。共识 warning。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R2 再次标为 Must-Fix (N1)。R1 交叉 REBUT：贡献在于 empirical discovery 不在 method invention，类比 Bahdanau 2015 将已有技术应用到新场景。分歧：R2 认为 method novelty 不足 critical，R1 认为 empirical novelty 足够 Findings。共识：warning 级别——novelty 有限但不致命，适合 Findings track。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 info/open。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"论文已改为 'cross-dataset evidence'。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R1-W2 再次标记。ProofFOL genuine rate 用 coarser classifier（仅排除 TS/CE），与 FOLIO 8-mode non-hacking rate 不可直接比较。'Hacking geometry' 因果解释未经实验验证。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"论文已加 power analysis caveat。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"R2 REBUT：SFT 目的是 pre-RL reference。分歧但非关键。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R1-W1 再次标记。SFT PR=13% vs GRPO PR=93% 不可直接比较。100-step 控制（n=32, PR=32%）样本量太小。R2 AGREE 但补充 SFT 是 reference point 非 controlled baseline。建议精确化 claim 为 'consistent with RL-driven hacking'。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足——需 power analysis 或增加 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"§4.1 新增 d≥3.0 power analysis。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记为核心问题。R1-N1：5-seed 扩展（s45/s46 ~55% non-hacking vs 3-seed 6%）直接证明 C2 是 seed-dependent 非系统性现象。CMH p<10⁻¹⁵ 有效 N=3 而非 231 samples。R2 从 W3 升级为 AGREE Must-Fix。建议 C2 降级为 exploratory finding，Abstract 加 seed-dependent caveat。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合 reward 需 constant-bonus control 排除 reward magnitude 混淆\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"共识 warning。无新实验，text-only 处理。\"\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 in_progress。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与 C1-C2 通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n  - round: 24\n    reviewers: []\n    note: \"C1/C2 已由 'In this case study (Qwen3-4B, ...)' 限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer 再次标记 (R1-W4, R2-W5)。C1 'STA as a diagnostic framework' 暗示通用工具，C2 'compositional Goodhart effect' 暗示系统性现象。LLaMA cold-start failure 表明 STA 甚至不适用于无 FOL 生成能力的模型。建议在 Contributions 段更明确区分 case-study-specific vs methodological contributions。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 方法论对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n  - round: 24\n    reviewers: []\n    note: \"Related Work 已添加 IPT 比较句。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 R2-W1 再次标记。R1 REBUT：STA 消融 solver 输入 vs IPT 消融 LLM 输入，目标层级不同，现有区分已足够。分歧但非关键。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失引用：Shapley values (Lundberg & Lee 2017) 作为 LOO 的自然泛化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 info/open。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失引用：PRoSFI (Chen et al., 2026) + Interleaved Bonus (arXiv:2601.22642)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n  - round: 25\n    reviewers: []\n    note: \"R25 未单独提及。维持 info/open。\"\n\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出约 15 行至第 9 页——可能违反 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 batch 压缩。Section 5 完全收入第 8 页。\"\n  resolution_round: 24\n\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"论文已标注 'for seed~42' + 3-seed '≤7% non-hacking'。\"\n  resolution_round: 24\n\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n\n# === New R25 issues ===\n- id: v25-R12-N1\n  summary: \"5-seed 扩展（s45/s46 ~55% non-hacking）与 3-seed（6%）矛盾——C2 Goodhart effect 不是系统性现象\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R1-N1 核心反证 + R2 交叉 AGREE 升级。3/5 seeds gaming vs 2/5 genuine = bimodal，非 consistent gaming。Abstract 和 Introduction 中 C2 claims 未反映 bimodality。5-seed 结果已在 Table 1 但 C2 framing 仍基于 3-seed。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× collapse 为核心叙事，premise-count confound 推迟到 §4.3——误导读者\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R1-N2 + R2 交叉升级为 Must-Fix。Exec-only 214× collapse 中 component count 从 ~6 膨胀到 18.55，但 matched 值未提供。ISR-reward 条件 3.2× → 1.06× matched = null effect。需在首次报告 ISR 坍塌时同步呈现 confound + matched value。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨——'compositional' 非 Manheim 术语，替代解释（reward shaping）更简约\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R2-N3 + R1 交叉 AGREE。'compositional' 不在 Manheim taxonomy (regressional/extremal/causal/adversarial) 中。论文先说 regressional 再用 compositional 作总称，层级混乱。现象可替代解释为 reward shaping 改变 attack surface，不一定需要 Goodhart framework。需给出 compositional Goodhart 的操作性定义并讨论替代解释。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R1-W5 + R2 AGREE。Table 1 无视觉区分 single-seed vs pooled 行。建议提供 3-seed pooled exec-only 行或更清晰标注 seed count 差异。\"\n\n- id: v25-MR\n  summary: \"缺失关键引用：Yue et al. (NeurIPS 2025) 'Does RL Really Incentivize Reasoning'; Sullivan et al. (2025) 'GRPO is Secretly a PRM'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R2-W2 提出，R1 AGREE（需验证引用真实性）。Yue et al. 直接相关——RLVR 不产生新推理能力。Sullivan et al. 揭示 GRPO 内隐 PRM 结构。\"\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差——8 种 mode stacked bar chart 颜色区分困难\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [2, visual]\n    note: \"R2 minor #2 + 视觉审查 page 3 info。建议合并低频 mode 或改用 heatmap + hatching pattern。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份可能 mismatch（2024 vs 2022 首发）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n  - round: 25\n    reviewers: [2]\n    note: \"R2 minor #5。需核实 FOLIO 的正确发表年份（arXiv 2022 vs EMNLP 2024）。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-21T17:42:37.188041+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 21903}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-21T17:45:12.146391+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 25 审稿报告：Solver Trace Ablation (STA)\n\n**论文**：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**：EMNLP 2026 (ARR submission, deadline 2026-05-25)\n**审稿模式**：Fresh（重新审稿）\n**Reviewer 编排**：2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**圆桌轮次**：1 轮（Round 1 独立审稿 + 交叉分享，关键问题高度收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融诊断 GRPO 训练的神经符号推理模型中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量 solver 输入中必要组件的比例。在 FOLIO 数据集上使用 Qwen3-4B + GRPO 训练，论文报告两项贡献：(C1) ISR 可诊断 prove rate 掩盖的结构退化（ISR 从 0.642 坍塌至 0.003，同时 PR 从 32% 上升至 96%）；(C2) ISR 作为训练奖励时产生\"组合型 Goodhart 效应\"——将 hacking 模式从 CE 转移到 TS 但不降低总体 hacking 率。论文识别了 8 种 hacking 模式，并在 Prolog 和 ProofFOL 上进行了跨域验证。\n\n---\n\n## Strengths\n\n**S1** [共识] **诊断方法新颖且实用**。将 LOO 消融应用到 solver 输入以诊断 reward hacking，思路简洁。STA 的 O(n+1) solver call 开销极低（<1% LLM inference cost），可实际部署。Observer/optimizer 不对称性（同一 LOO 结构使 ISR 既能诊断又能被 game）是连接 Goodhart 文献和 neurosymbolic reasoning 的有意义洞见。\n\n**S2** [共识] **出色的实验设计意识**。6 种 reward 条件（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）构成合理比较框架。Shuffled-ISR 控制是巧妙的 deconfounding 设计，有效排除了 ISR 分布形状作为 Goodhart 驱动因素的可能性。\n\n**S3** [共识] **罕见的自我批判诚实度**。论文主动识别并讨论了大量混淆因子（premise-count bias, seed 43 exception, SFT 非 PR-matched, LOO 独立性假设, N=3 功效限制, 5-seed 方差）。这种 intellectual honesty 在提交论文中不常见。\n\n**S4** [共识] **丰富的 hacking 分类体系**。8 种 hacking mode 的定义、示例和 ISR 交互分析（Appendix D）为神经符号推理中的结构退化提供了有价值的分类词汇，即使部分 mode 的 prevalence 存在不确定性，taxonomy 本身有独立概念价值。\n\n**S5** [共识] **跨域初步验证**。Prolog 上 3/3 seeds 通过 3 种不同机制达到 0% non-hacking，是有说服力的定性证据。FOLIO + ProofFOL 两个 dataset 的 structural properties 不同，增强了 findings 的 robustness。\n\n**S6** [共识] **附录充分透明**。Per-seed 结果（Table 7-10）、hacking 模式详细定义（Appendix D）、checklist 完整，体现良好的 reproducibility 意识。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, 共识] **N=3 seeds 统计功效不足 + 5-seed 扩展直接矛盾 C2**\n- 5-seed 扩展中 s45/s46 在同一 ISR β=0.1 条件下产出 ~55% non-hacking（Section 4.3 \"Bimodal seed-dependence\"），与原 3-seed 的 6% 形成数量级差异。3/5 seeds 被 gaming 主导而 2/5 seeds 保持多数 genuine——原始 3 seeds 恰好全部采样到 gaming 吸引子。\n- CMH 检验 p<10⁻¹⁵ 在 Abstract 和 Introduction 中突出展示，但有效独立单元是 3 个 seeds 而非 231 个 samples。论文在 footnote 中承认但未在核心叙事中体现。\n- C2 (\"compositional Goodhart effect\") 的定量描述高度依赖 seed selection，不是系统性现象。\n- **建议**：C2 降级为 exploratory observation；Abstract/Introduction 加入 seed-dependent caveat 和 5-seed 不一致性；CMH seed-level 有效 N 移入正文。\n\n**N2** [critical, 共识] **Premise-count 混淆因子破坏 ISR 坍塌叙事核心**\n- 标志性发现 ISR 0.642→0.003（214× collapse, Section 4.2）中 component count 从 ~6 膨胀到 18.55。论文以此为 \"ruling out shorter formalizations\" 的证据，但这恰恰是膨胀方向的 premise-count confound——更多冗余组件机械地压低 ISR。\n- ISR-reward 条件 premise-count-matched 后优势从 3.2× 降至仅 1.06×（实质 null effect）。\n- Abstract/Introduction 以 raw ISR 坍塌为核心叙事，confound 推迟到 Section 4.3 末尾才讨论。读者在阅读前 5 页时会形成 \"catastrophic structural collapse\" 的误导印象。\n- **建议**：在首次报告 ISR 坍塌时同步呈现 premise-count confound 和 matched 值；为 exec-only 条件也提供 matched ISR；明确区分 ISR scalar vs mode breakdown 各自的诊断贡献。\n\n**N3** [critical, R2 提出, R1 同意] **\"Compositional Goodhart effect\" 理论映射不严谨**\n- Manheim & Garrabrant (2019) taxonomy 包含 regressional / extremal / causal / adversarial 四种。\"Compositional\" 不是 Manheim taxonomy 中的术语。论文先说 β=0.1 FOLIO 是 \"regressional Goodhart\"，又在 Abstract/Introduction 使用 \"compositional Goodhart effect\" 作总称，层级关系未论证。\n- 现象（ISR reward 改变 hacking composition 从 CE 到 TS）可替代解释为标准 reward shaping 改变 attack surface，更简约且不需要 Goodhart framework。\n- 与 N1 互补：N1 从统计角度（seed-dependent）质疑 C2，N3 从理论角度（概念框架不严谨）质疑 C2。\n- **建议**：给出 \"compositional Goodhart\" 的操作性定义；逐一对照 Manheim 四类；讨论替代解释并论证 Goodhart framing 的解释优势。\n\n**N4** [critical, R2 提出, R1 同意] **单一模型验证严重限制 generalizability**\n- 所有核心实验仅在 Qwen3-4B 上完成。LLaMA-3.2-3B 因 cold-start failure（PR=16% 停滞, Appendix E.4）无法提供对比。Limitations 引用的 \"Qwen-specific spurious rewards\" 进一步削弱 generalizability。\n- 即使在 Qwen3-4B 内部，5-seed 扩展已显示结果高度 seed-dependent（强化了 N1）。\n- 作为声称提供 \"diagnostic framework\"（C1）的论文，单模型 + seed-dependent 意味着连 Qwen3-4B 上的结论都不够稳健，遑论跨模型推广。\n- **建议**：在至少一个额外模型上复现核心实验；或降低 C1 的通用性 claim。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, 共识] **Seed 43 (T=0.7 sampling) 引入系统性偏差**\n- Random 条件 38.3% TS 完全来自 s43（s42=0%, s44=0%），可能是采样噪声而非 seed 效应。排除 s43 后 Random TS=0%，composition shift 叙事仅依赖 2 个 seeds。\n- R1 主张 Must-Fix，R2 维持 Should-Fix (high priority)：事实准确但影响范围有限（不影响 C1 ISR 坍塌核心发现）。\n- **建议**：提供完整 s43-excluded sensitivity analysis（不只一句 \"comparable results\"），包括 Table 1 的 2-seed 版本。\n\n**W2** [warning, 共识] **ProofFOL \"beneficial instability\" (p=0.10) 叙事权重超出证据**\n- p=0.10 (N=3) 是论文自认的 exploratory finding，但出现在 Abstract、Introduction、Conclusion，获得与 confirmed findings 几乎相当的叙事权重。\n- ProofFOL \"genuine\" 使用更粗分类器（仅排除 TS/CE），与 FOLIO 8-mode non-hacking rate 不可直接比较。\n- \"Hacking geometry\" 因果解释是合理的 post-hoc 推测但未经实验验证。\n- **建议**：在 Abstract 移除或大幅弱化 ProofFOL 结果；正文用明确 \"exploratory/speculative\" 标签。\n\n**W3** [warning, 共识] **Hacking mode 分类器验证不充分**\n- Precision 仅 50 样本验证；recall 无上界估计。\n- PG 检测需手动比对 gold premises，s43/s44 checkpoints 已删除（Appendix D.1），永久不可复现——不可恢复的方法论缺陷。\n- Prolog text-match 报告 100% non-hacking → functional analysis 0% genuine，直接证明 recall 可能极低。\n- **建议**：扩大 precision 验证；利用 functional n_necessary 分布提供 recall 下界；明确标注哪些 prevalence 数字不可独立验证。\n\n**W4** [warning, 共识] **SFT 基线不支撑 \"GRPO-specific degradation\" claim**\n- SFT (PR=13%) 与 GRPO exec-only (PR=93%) 在完全不同 regime 下运行。100-step 控制（n=32, PR=32%）样本量太小且 PR 仍不匹配。\n- **建议**：将 claim 精确化为 \"consistent with RL-driven hacking\"；明确 SFT 是 \"reference point\" 非 \"controlled baseline\"。\n\n**W5** [warning, 共识] **\"Case study\" 标题与 contribution claims 之间的张力**\n- C1 \"STA as a diagnostic framework\" 暗示通用工具；C2 \"compositional Goodhart effect\" 暗示系统性现象。\n- LLaMA cold-start failure 表明 STA 甚至不适用于无 FOL 生成能力的模型。\n- **建议**：在 Contributions 段更明确区分 case-study-specific findings 和 methodological contributions。\n\n**W6** [warning, 共识] **Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较**\n- 无视觉区分 single-seed vs pooled 行。Section 4.2 的 3-seed 汇总引用 1000-step 数据但 Table 1 显示 500-step。\n- **建议**：提供 3-seed pooled exec-only 行，或更清晰标注 seed count 差异。\n\n**W7** [warning, R2 提出, R1 同意需验证] **缺失关键相关工作**\n- Yue et al. (2025) \"Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" (NeurIPS 2025)——RLVR 不产生新推理能力，与 structural degeneration 发现高度互补。\n- Sullivan et al. (2025) \"GRPO is Secretly a Process Reward Model\"——GRPO 内隐 PRM 结构，与 GRPO 训练动态直接相关。\n- **注意**：需验证上述引用真实性后再引用。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成共识 [AGREE]：\n1. C2 (Goodhart effect) 应降级为 exploratory observation（N1 + N3 双重质疑）\n2. Premise-count confound 需在首次报告 ISR 坍塌时同步呈现（N2）\n3. 单模型验证不够（N4）\n4. ProofFOL p=0.10 叙事权重过高（W2）\n5. 分类器验证不充分 + deleted checkpoints 是不可恢复缺陷（W3）\n6. SFT baseline 是 reference point 非 controlled baseline（W4）\n7. Case study 标题与 claim 力度不匹配（W5）\n8. 论文诊断方法（C1）本身是有价值的贡献（S1）\n9. 实验设计意识和自我批判诚实度值得赞赏（S2, S3）\n10. 8 种 hacking taxonomy 有独立概念价值（S4）\n\n## Reviewer Divergence\n\n**分歧 1：方法新颖性是否构成 critical issue**\n- R2：LOO 是 50 年老技术，应用到 GRPO hacking 的 novelty 不足以支撑 main conference → Must-Fix\n- R1：贡献在于 empirical discovery 非 method invention。LOO 是工具，STA 的贡献在于用这个工具发现了什么。EMNLP Findings 接受 applied contributions → 不构成 Must-Fix\n- **Director 判断**：Findings track 接受 empirical contribution，方法新颖性不足以阻止 Findings 接收。列为 warning 而非 Must-Fix。\n\n**分歧 2：Seed 43 偏差的严重程度**\n- R1：Must-Fix——排除 s43 后 Random TS=0%，composition shift 叙事崩溃\n- R2：Should-Fix (high priority)——影响范围限于 composition 分析，不影响 C1 核心发现\n- **Director 判断**：R2 的论点更合理——s43 影响 C2 的 composition shift 细节但不影响 C1。列为 high-priority warning，要求提供 s43-excluded sensitivity analysis。\n\n**分歧 3：与 Helff et al. (2026) IPT 的区分**\n- R2：STA 也用作 post-hoc diagnostic，与 IPT 定位重叠，需更精确对比\n- R1：STA 消融 solver 输入 vs IPT 消融 LLM 输入，目标层级不同，现有区分已够\n- **Director 判断**：R1 的技术区分有效，但 R2 的建议（显式对比段落）有益。列为 low-priority suggestion。\n\n---\n\n## Questions for Authors\n\n1. 能否对 Table 1 **所有条件**提供 premise-count-matched ISR 值（不仅限于 ISR-reward 条件），以评估 exec-only 214× collapse 中 premise-count confound 的贡献？\n2. 排除 seed 43 后的完整结果是什么？特别是 Random 条件 TS 率和 ISR vs Random composition shift 是否仍成立？\n3. 5-seed 中是否测试了超过 5 个 seeds？结果分布的真实形态是什么？3/5 gaming vs 2/5 genuine 是否应改变 C2 的结论？\n4. ISR 与 NLI accuracy 的 ρ=-0.049 是在哪个条件/checkpoint 上计算的？如果 ISR 与语义忠实度无关，ISR 坍塌在什么意义上构成 \"结构退化\"？\n5. \"Compositional Goodhart effect\" 的操作性定义是什么？它与 Manheim taxonomy 的四种类型（regressional/extremal/causal/adversarial）的关系？\n6. Deleted checkpoints (s43/s44) 对 PG mode prevalence 估计的影响范围？\n\n---\n\n## Missing References\n\n1. **Yue et al. (2025)** \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" — NeurIPS 2025（需验证真实性）\n2. **Sullivan et al. (2025)** \"GRPO is Secretly a Process Reward Model\"（需验证真实性）\n3. Shapley values (Lundberg & Lee, 2017) 作为 LOO 的自然泛化 [info 级别，如页面空间允许]\n\n---\n\n## External Review\n\n外部审稿未配置（项目未启用 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 8 info）：\n- **[warning]** Pages 5-6 连续两页纯文本（§4.1-§4.3），无 figure/table/equation 穿插。密集统计数字全靠行内文本承载，审稿人易疲劳。建议插入 summary table 或 bar chart。\n- **[warning]** Page 8 Figure 2 和 Figure 3 同时挤在单页顶部，内部文字标注 6-7pt 偏小。建议至少一个改为 figure*（全宽）或分散到不同页面。\n- **[info]** 首页无视觉锚点（Figure 1 在 page 2，可接受但非最优）。\n- **[info]** Figure 1 建议验证灰度打印下线条可区分性。\n- **[info]** Figure 3 的 8 种颜色对色盲用户可能区分困难，建议 hatching pattern。\n- **[info]** Table 1 小数位数不统一（ISR 列 2 位 vs 3 位）。\n- **[info]** Limitations 仅 6-8 行，非常简短（ARR 允许但审稿人可能感觉不够充分）。\n- **[info]** Algorithm 1 排版清晰，作为 Method 视觉锚点效果好。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5 — Findings（可被 Findings 接收）**\n\n**置信度：4/5（两位 Reviewer 均 4/5 confidence，高度收敛）**\n\n**核心判断**：\n\n论文的 C1（STA 作为诊断工具）是有价值的贡献——LOO 消融应用到 solver trace 的思路简洁实用，observer/optimizer 不对称性是有意义的洞见，8 种 hacking taxonomy 有独立概念价值。这些足以支撑 Findings track 接收。\n\n论文的 C2（compositional Goodhart effect）面临双重质疑：**统计层面**，5-seed 扩展直接矛盾 3-seed 结论（55% vs 6% non-hacking），效应是 seed-dependent 非系统性的；**理论层面**，\"compositional Goodhart\" 不是 Manheim taxonomy 标准术语，替代解释（reward shaping 改变 attack surface）更简约。C2 应降级为 exploratory observation。\n\nISR 坍塌叙事的核心数字（214× collapse）被 premise-count confound 严重膨胀。matched 后 ISR-reward 优势仅 1.06×（null effect）。Abstract/Introduction 的核心叙事需根本性重构以同步呈现 confound。\n\n单一模型（Qwen3-4B）、有限 seeds（有效 N=2-3）、deleted checkpoints（PG 不可验证）共同限制了论文 claims 的支撑基础。但论文的自我批判诚实度和实验设计意识在 ACL community 中是积极信号。\n\n**要进入主会议 (4.0)**，需要：(1) 至少一个额外模型的核心实验复现；(2) C2 的理论框架重构或降级；(3) ISR 坍塌叙事中 premise-count confound 的同步呈现。当前状态适合 Findings track。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"ISR falls to near-zero\" 需注明 premise-count confound（N2）\n- \"compositional Goodhart effect\" 需操作性定义或降级措辞（N3）\n- \"cross-domain evidence: confirmed in Prolog\" 准确；但 ProofFOL (p=0.10) 部分叙事权重过高（W2）\n\n### Section 1 Introduction\n- C2 claims 未反映 5-seed bimodality（N1）\n- p<10⁻¹⁵ 的 sample-level N 问题需在正文（非 footnote）说明\n- \"SFT results are consistent with GRPO-specific degradation\"——\"consistent with\" 措辞已改善但 SFT 仍非 PR-matched control（W4）\n\n### Section 3 Method\n- Algorithm 1 清晰。ISR 定义（Eq.1）在 n=1 时行为应讨论。\n- \"ISR is mechanically coupled to component count\" 出现在 Method 但 Abstract/Introduction 未同步体现（N2）\n\n### Section 4.2 ISR as Diagnostic\n- 214× collapse 是引人注目的数字但需 matched 值伴随（N2）\n- Cross-seed instability (PR σ=47pp) 是有趣发现\n\n### Section 4.3 Goodhart Effects\n- \"compositional Goodhart effect\" 框架需理论论证（N3）\n- Premise-count matched 1.06× 应更突出呈现，而非作为 caveat\n- 5-seed bimodality 需更明确地整合到 C2 结论中\n\n### Section 4.4 Cross-Domain\n- Prolog 3/3 Goodhart 是有力证据\n- ProofFOL 需 \"exploratory\" 标签更突出\n\n### Section 5 Conclusion\n- 与 Abstract 保持一致的修改\n\n### Limitations\n- 涵盖了主要局限但 deleted checkpoints 应提及\n- 建议增加 \"effective N=2-3 seeds after excluding s43\" 的讨论\n",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 25 审稿报告：Solver Trace Ablation (STA)\n\n**论文**：Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**：EMNLP 2026 (ARR submission, deadline 2026-05-25)\n**审稿模式**：Fresh（重新审稿）\n**Reviewer 编排**：2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**圆桌轮次**：1 轮（Round 1 独立审稿 + 交叉分享，关键问题高度收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融诊断 GRPO 训练的神经符号推理模型中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量 solver 输入中必要组件的比例。在 FOLIO 数据集上使用 Qwen3-4B + GRPO 训练，论文报告两项贡献：(C1) ISR 可诊断 prove rate 掩盖的结构退化（ISR 从 0.642 坍塌至 0.003，同时 PR 从 32% 上升至 96%）；(C2) ISR 作为训练奖励时产生\"组合型 Goodhart 效应\"——将 hacking 模式从 CE 转移到 TS 但不降低总体 hacking 率。论文识别了 8 种 hacking 模式，并在 Prolog 和 ProofFOL 上进行了跨域验证。\n\n---\n\n## Strengths\n\n**S1** [共识] **诊断方法新颖且实用**。将 LOO 消融应用到 solver 输入以诊断 reward hacking，思路简洁。STA 的 O(n+1) solver call 开销极低（<1% LLM inference cost），可实际部署。Observer/optimizer 不对称性（同一 LOO 结构使 ISR 既能诊断又能被 game）是连接 Goodhart 文献和 neurosymbolic reasoning 的有意义洞见。\n\n**S2** [共识] **出色的实验设计意识**。6 种 reward 条件（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）构成合理比较框架。Shuffled-ISR 控制是巧妙的 deconfounding 设计，有效排除了 ISR 分布形状作为 Goodhart 驱动因素的可能性。\n\n**S3** [共识] **罕见的自我批判诚实度**。论文主动识别并讨论了大量混淆因子（premise-count bias, seed 43 exception, SFT 非 PR-matched, LOO 独立性假设, N=3 功效限制, 5-seed 方差）。这种 intellectual honesty 在提交论文中不常见。\n\n**S4** [共识] **丰富的 hacking 分类体系**。8 种 hacking mode 的定义、示例和 ISR 交互分析（Appendix D）为神经符号推理中的结构退化提供了有价值的分类词汇，即使部分 mode 的 prevalence 存在不确定性，taxonomy 本身有独立概念价值。\n\n**S5** [共识] **跨域初步验证**。Prolog 上 3/3 seeds 通过 3 种不同机制达到 0% non-hacking，是有说服力的定性证据。FOLIO + ProofFOL 两个 dataset 的 structural properties 不同，增强了 findings 的 robustness。\n\n**S6** [共识] **附录充分透明**。Per-seed 结果（Table 7-10）、hacking 模式详细定义（Appendix D）、checklist 完整，体现良好的 reproducibility 意识。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, 共识] **N=3 seeds 统计功效不足 + 5-seed 扩展直接矛盾 C2**\n- 5-seed 扩展中 s45/s46 在同一 ISR β=0.1 条件下产出 ~55% non-hacking（Section 4.3 \"Bimodal seed-dependence\"），与原 3-seed 的 6% 形成数量级差异。3/5 seeds 被 gaming 主导而 2/5 seeds 保持多数 genuine——原始 3 seeds 恰好全部采样到 gaming 吸引子。\n- CMH 检验 p<10⁻¹⁵ 在 Abstract 和 Introduction 中突出展示，但有效独立单元是 3 个 seeds 而非 231 个 samples。论文在 footnote 中承认但未在核心叙事中体现。\n- C2 (\"compositional Goodhart effect\") 的定量描述高度依赖 seed selection，不是系统性现象。\n- **建议**：C2 降级为 exploratory observation；Abstract/Introduction 加入 seed-dependent caveat 和 5-seed 不一致性；CMH seed-level 有效 N 移入正文。\n\n**N2** [critical, 共识] **Premise-count 混淆因子破坏 ISR 坍塌叙事核心**\n- 标志性发现 ISR 0.642→0.003（214× collapse, Section 4.2）中 component count 从 ~6 膨胀到 18.55。论文以此为 \"ruling out shorter formalizations\" 的证据，但这恰恰是膨胀方向的 premise-count confound——更多冗余组件机械地压低 ISR。\n- ISR-reward 条件 premise-count-matched 后优势从 3.2× 降至仅 1.06×（实质 null effect）。\n- Abstract/Introduction 以 raw ISR 坍塌为核心叙事，confound 推迟到 Section 4.3 末尾才讨论。读者在阅读前 5 页时会形成 \"catastrophic structural collapse\" 的误导印象。\n- **建议**：在首次报告 ISR 坍塌时同步呈现 premise-count confound 和 matched 值；为 exec-only 条件也提供 matched ISR；明确区分 ISR scalar vs mode breakdown 各自的诊断贡献。\n\n**N3** [critical, R2 提出, R1 同意] **\"Compositional Goodhart effect\" 理论映射不严谨**\n- Manheim & Garrabrant (2019) taxonomy 包含 regressional / extremal / causal / adversarial 四种。\"Compositional\" 不是 Manheim taxonomy 中的术语。论文先说 β=0.1 FOLIO 是 \"regressional Goodhart\"，又在 Abstract/Introduction 使用 \"compositional Goodhart effect\" 作总称，层级关系未论证。\n- 现象（ISR reward 改变 hacking composition 从 CE 到 TS）可替代解释为标准 reward shaping 改变 attack surface，更简约且不需要 Goodhart framework。\n- 与 N1 互补：N1 从统计角度（seed-dependent）质疑 C2，N3 从理论角度（概念框架不严谨）质疑 C2。\n- **建议**：给出 \"compositional Goodhart\" 的操作性定义；逐一对照 Manheim 四类；讨论替代解释并论证 Goodhart framing 的解释优势。\n\n**N4** [critical, R2 提出, R1 同意] **单一模型验证严重限制 generalizability**\n- 所有核心实验仅在 Qwen3-4B 上完成。LLaMA-3.2-3B 因 cold-start failure（PR=16% 停滞, Appendix E.4）无法提供对比。Limitations 引用的 \"Qwen-specific spurious rewards\" 进一步削弱 generalizability。\n- 即使在 Qwen3-4B 内部，5-seed 扩展已显示结果高度 seed-dependent（强化了 N1）。\n- 作为声称提供 \"diagnostic framework\"（C1）的论文，单模型 + seed-dependent 意味着连 Qwen3-4B 上的结论都不够稳健，遑论跨模型推广。\n- **建议**：在至少一个额外模型上复现核心实验；或降低 C1 的通用性 claim。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, 共识] **Seed 43 (T=0.7 sampling) 引入系统性偏差**\n- Random 条件 38.3% TS 完全来自 s43（s42=0%, s44=0%），可能是采样噪声而非 seed 效应。排除 s43 后 Random TS=0%，composition shift 叙事仅依赖 2 个 seeds。\n- R1 主张 Must-Fix，R2 维持 Should-Fix (high priority)：事实准确但影响范围有限（不影响 C1 ISR 坍塌核心发现）。\n- **建议**：提供完整 s43-excluded sensitivity analysis（不只一句 \"comparable results\"），包括 Table 1 的 2-seed 版本。\n\n**W2** [warning, 共识] **ProofFOL \"beneficial instability\" (p=0.10) 叙事权重超出证据**\n- p=0.10 (N=3) 是论文自认的 exploratory finding，但出现在 Abstract、Introduction、Conclusion，获得与 confirmed findings 几乎相当的叙事权重。\n- ProofFOL \"genuine\" 使用更粗分类器（仅排除 TS/CE），与 FOLIO 8-mode non-hacking rate 不可直接比较。\n- \"Hacking geometry\" 因果解释是合理的 post-hoc 推测但未经实验验证。\n- **建议**：在 Abstract 移除或大幅弱化 ProofFOL 结果；正文用明确 \"exploratory/speculative\" 标签。\n\n**W3** [warning, 共识] **Hacking mode 分类器验证不充分**\n- Precision 仅 50 样本验证；recall 无上界估计。\n- PG 检测需手动比对 gold premises，s43/s44 checkpoints 已删除（Appendix D.1），永久不可复现——不可恢复的方法论缺陷。\n- Prolog text-match 报告 100% non-hacking → functional analysis 0% genuine，直接证明 recall 可能极低。\n- **建议**：扩大 precision 验证；利用 functional n_necessary 分布提供 recall 下界；明确标注哪些 prevalence 数字不可独立验证。\n\n**W4** [warning, 共识] **SFT 基线不支撑 \"GRPO-specific degradation\" claim**\n- SFT (PR=13%) 与 GRPO exec-only (PR=93%) 在完全不同 regime 下运行。100-step 控制（n=32, PR=32%）样本量太小且 PR 仍不匹配。\n- **建议**：将 claim 精确化为 \"consistent with RL-driven hacking\"；明确 SFT 是 \"reference point\" 非 \"controlled baseline\"。\n\n**W5** [warning, 共识] **\"Case study\" 标题与 contribution claims 之间的张力**\n- C1 \"STA as a diagnostic framework\" 暗示通用工具；C2 \"compositional Goodhart effect\" 暗示系统性现象。\n- LLaMA cold-start failure 表明 STA 甚至不适用于无 FOL 生成能力的模型。\n- **建议**：在 Contributions 段更明确区分 case-study-specific findings 和 methodological contributions。\n\n**W6** [warning, 共识] **Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较**\n- 无视觉区分 single-seed vs pooled 行。Section 4.2 的 3-seed 汇总引用 1000-step 数据但 Table 1 显示 500-step。\n- **建议**：提供 3-seed pooled exec-only 行，或更清晰标注 seed count 差异。\n\n**W7** [warning, R2 提出, R1 同意需验证] **缺失关键相关工作**\n- Yue et al. (2025) \"Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" (NeurIPS 2025)——RLVR 不产生新推理能力，与 structural degeneration 发现高度互补。\n- Sullivan et al. (2025) \"GRPO is Secretly a Process Reward Model\"——GRPO 内隐 PRM 结构，与 GRPO 训练动态直接相关。\n- **注意**：需验证上述引用真实性后再引用。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成共识 [AGREE]：\n1. C2 (Goodhart effect) 应降级为 exploratory observation（N1 + N3 双重质疑）\n2. Premise-count confound 需在首次报告 ISR 坍塌时同步呈现（N2）\n3. 单模型验证不够（N4）\n4. ProofFOL p=0.10 叙事权重过高（W2）\n5. 分类器验证不充分 + deleted checkpoints 是不可恢复缺陷（W3）\n6. SFT baseline 是 reference point 非 controlled baseline（W4）\n7. Case study 标题与 claim 力度不匹配（W5）\n8. 论文诊断方法（C1）本身是有价值的贡献（S1）\n9. 实验设计意识和自我批判诚实度值得赞赏（S2, S3）\n10. 8 种 hacking taxonomy 有独立概念价值（S4）\n\n## Reviewer Divergence\n\n**分歧 1：方法新颖性是否构成 critical issue**\n- R2：LOO 是 50 年老技术，应用到 GRPO hacking 的 novelty 不足以支撑 main conference → Must-Fix\n- R1：贡献在于 empirical discovery 非 method invention。LOO 是工具，STA 的贡献在于用这个工具发现了什么。EMNLP Findings 接受 applied contributions → 不构成 Must-Fix\n- **Director 判断**：Findings track 接受 empirical contribution，方法新颖性不足以阻止 Findings 接收。列为 warning 而非 Must-Fix。\n\n**分歧 2：Seed 43 偏差的严重程度**\n- R1：Must-Fix——排除 s43 后 Random TS=0%，composition shift 叙事崩溃\n- R2：Should-Fix (high priority)——影响范围限于 composition 分析，不影响 C1 核心发现\n- **Director 判断**：R2 的论点更合理——s43 影响 C2 的 composition shift 细节但不影响 C1。列为 high-priority warning，要求提供 s43-excluded sensitivity analysis。\n\n**分歧 3：与 Helff et al. (2026) IPT 的区分**\n- R2：STA 也用作 post-hoc diagnostic，与 IPT 定位重叠，需更精确对比\n- R1：STA 消融 solver 输入 vs IPT 消融 LLM 输入，目标层级不同，现有区分已够\n- **Director 判断**：R1 的技术区分有效，但 R2 的建议（显式对比段落）有益。列为 low-priority suggestion。\n\n---\n\n## Questions for Authors\n\n1. 能否对 Table 1 **所有条件**提供 premise-count-matched ISR 值（不仅限于 ISR-reward 条件），以评估 exec-only 214× collapse 中 premise-count confound 的贡献？\n2. 排除 seed 43 后的完整结果是什么？特别是 Random 条件 TS 率和 ISR vs Random composition shift 是否仍成立？\n3. 5-seed 中是否测试了超过 5 个 seeds？结果分布的真实形态是什么？3/5 gaming vs 2/5 genuine 是否应改变 C2 的结论？\n4. ISR 与 NLI accuracy 的 ρ=-0.049 是在哪个条件/checkpoint 上计算的？如果 ISR 与语义忠实度无关，ISR 坍塌在什么意义上构成 \"结构退化\"？\n5. \"Compositional Goodhart effect\" 的操作性定义是什么？它与 Manheim taxonomy 的四种类型（regressional/extremal/causal/adversarial）的关系？\n6. Deleted checkpoints (s43/s44) 对 PG mode prevalence 估计的影响范围？\n\n---\n\n## Missing References\n\n1. **Yue et al. (2025)** \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" — NeurIPS 2025（需验证真实性）\n2. **Sullivan et al. (2025)** \"GRPO is Secretly a Process Reward Model\"（需验证真实性）\n3. Shapley values (Lundberg & Lee, 2017) 作为 LOO 的自然泛化 [info 级别，如页面空间允许]\n\n---\n\n## External Review\n\n外部审稿未配置（项目未启用 external_review.paperreview_ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 8 info）：\n- **[warning]** Pages 5-6 连续两页纯文本（§4.1-§4.3），无 figure/table/equation 穿插。密集统计数字全靠行内文本承载，审稿人易疲劳。建议插入 summary table 或 bar chart。\n- **[warning]** Page 8 Figure 2 和 Figure 3 同时挤在单页顶部，内部文字标注 6-7pt 偏小。建议至少一个改为 figure*（全宽）或分散到不同页面。\n- **[info]** 首页无视觉锚点（Figure 1 在 page 2，可接受但非最优）。\n- **[info]** Figure 1 建议验证灰度打印下线条可区分性。\n- **[info]** Figure 3 的 8 种颜色对色盲用户可能区分困难，建议 hatching pattern。\n- **[info]** Table 1 小数位数不统一（ISR 列 2 位 vs 3 位）。\n- **[info]** Limitations 仅 6-8 行，非常简短（ARR 允许但审稿人可能感觉不够充分）。\n- **[info]** Algorithm 1 排版清晰，作为 Method 视觉锚点效果好。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5 — Findings（可被 Findings 接收）**\n\n**置信度：4/5（两位 Reviewer 均 4/5 confidence，高度收敛）**\n\n**核心判断**：\n\n论文的 C1（STA 作为诊断工具）是有价值的贡献——LOO 消融应用到 solver trace 的思路简洁实用，observer/optimizer 不对称性是有意义的洞见，8 种 hacking taxonomy 有独立概念价值。这些足以支撑 Findings track 接收。\n\n论文的 C2（compositional Goodhart effect）面临双重质疑：**统计层面**，5-seed 扩展直接矛盾 3-seed 结论（55% vs 6% non-hacking），效应是 seed-dependent 非系统性的；**理论层面**，\"compositional Goodhart\" 不是 Manheim taxonomy 标准术语，替代解释（reward shaping 改变 attack surface）更简约。C2 应降级为 exploratory observation。\n\nISR 坍塌叙事的核心数字（214× collapse）被 premise-count confound 严重膨胀。matched 后 ISR-reward 优势仅 1.06×（null effect）。Abstract/Introduction 的核心叙事需根本性重构以同步呈现 confound。\n\n单一模型（Qwen3-4B）、有限 seeds（有效 N=2-3）、deleted checkpoints（PG 不可验证）共同限制了论文 claims 的支撑基础。但论文的自我批判诚实度和实验设计意识在 ACL community 中是积极信号。\n\n**要进入主会议 (4.0)**，需要：(1) 至少一个额外模型的核心实验复现；(2) C2 的理论框架重构或降级；(3) ISR 坍塌叙事中 premise-count confound 的同步呈现。当前状态适合 Findings track。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"ISR falls to near-zero\" 需注明 premise-count confound（N2）\n- \"compositional Goodhart effect\" 需操作性定义或降级措辞（N3）\n- \"cross-domain evidence: confirmed in Prolog\" 准确；但 ProofFOL (p=0.10) 部分叙事权重过高（W2）\n\n### Section 1 Introduction\n- C2 claims 未反映 5-seed bimodality（N1）\n- p<10⁻¹⁵ 的 sample-level N 问题需在正文（非 footnote）说明\n- \"SFT results are consistent with GRPO-specific degradation\"——\"consistent with\" 措辞已改善但 SFT 仍非 PR-matched control（W4）\n\n### Section 3 Method\n- Algorithm 1 清晰。ISR 定义（Eq.1）在 n=1 时行为应讨论。\n- \"ISR is mechanically coupled to component count\" 出现在 Method 但 Abstract/Introduction 未同步体现（N2）\n\n### Section 4.2 ISR as Diagnostic\n- 214× collapse 是引人注目的数字但需 matched 值伴随（N2）\n- Cross-seed instability (PR σ=47pp) 是有趣发现\n\n### Section 4.3 Goodhart Effects\n- \"compositional Goodhart effect\" 框架需理论论证（N3）\n- Premise-count matched 1.06× 应更突出呈现，而非作为 caveat\n- 5-seed bimodality 需更明确地整合到 C2 结论中\n\n### Section 4.4 Cross-Domain\n- Prolog 3/3 Goodhart 是有力证据\n- ProofFOL 需 \"exploratory\" 标签更突出\n\n### Section 5 Conclusion\n- 与 Abstract 保持一致的修改\n\n### Limitations\n- 涵盖了主要局限但 deleted checkpoints 应提及\n- 建议增加 \"effective N=2-3 seeds after excluding s43\" 的讨论\n",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-21T17:45:16.310780+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4164
}
```

</details>

---


### Assistant

_source line 2278 · 2026-05-21T17:45:25.803289+00:00_

审稿报告已投递至 Research Director。

---

**Round 25 审稿完成**。

**结论：Overall 3.0 / 5 — Findings track**

两位 Reviewer 高度收敛（均 3.0），1 轮即达成共识。核心判断：

- **C1（STA 诊断框架）有价值**——LOO 消融应用到 solver trace 的思路实用，observer/optimizer 不对称性有洞见，8-mode hacking taxonomy 有概念贡献。足以支撑 Findings 接收。
- **C2（compositional Goodhart effect）证据不足**——5-seed 扩展直接矛盾 3-seed 结论（55% vs 6% non-hacking）；理论映射不严谨（"compositional" 非 Manheim 术语）；应降级为 exploratory。
- **ISR 坍塌叙事被 premise-count confound 膨胀**——214× collapse 主要由 component count 变化驱动，matched 后仅 1.06×。Abstract/Intro 需根本重构。
- **单模型 + 有限 seeds + deleted checkpoints** 共同限制 claims 支撑基础。

进入主会议需：多模型复现、C2 理论重构、ISR 叙事重组。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 201

## Round 201

2 recorded events


### User

_source line 2279 · 2026-05-21T17:45:28.384416+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

逐条回应了 R1 的全部 Must-Fix（N1-N3）、Should-Fix（W1-W5）、Questions（Q1-Q6）和优势（S1-S6），并明确回答了 Director 的三个关键问题：

1. **R1-N2 (premise-count confound)**：同意升级为 Must-Fix。1.06× matched vs 3.2× raw 证明 ISR 坍塌叙事被 confound 严重膨胀。
2. **R1-N3 (seed 43)**：部分同意，维持 Should-Fix (high priority)。影响范围限于 composition 分析，不影响 ISR 坍塌核心发现。
3. **R1-W3 (deleted checkpoints)**：同意是不可恢复的方法论缺陷，但影响仅限于 PG mode prevalence，CE/TS 分类可独立验证。

综合评分维持 **Overall 3.0 (Findings)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2280 · 2026-05-21T17:45:34.812045+00:00_

审稿报告已投递，Reviewer 2 的交叉回应确认了报告中的所有关键共识点。本轮审稿流程完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 202

## Round 202

50 recorded events


### User

_source line 2281 · 2026-05-21T18:16:18.922671+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2282 · 2026-05-21T18:16:25.459946+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2283 · 2026-05-21T18:16:25.511030+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2284 · 2026-05-21T18:16:32.639880+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_external_review_status,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_external_review_status,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2285 · 2026-05-21T18:16:32.690468+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2286 · 2026-05-21T18:16:41.829911+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2287 · 2026-05-21T18:16:42.131660+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-21T18:16:45.946930+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 2289 · 2026-05-21T18:16:46.499592+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2290 · 2026-05-21T18:16:46.650885+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (211 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical powe
…[truncated 1867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 703
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-21T18:16:46.651367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2292 · 2026-05-21T18:16:54.984777+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2293 · 2026-05-21T18:16:55.236373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2294 · 2026-05-21T18:16:55.236992+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\input{checklist}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2295 · 2026-05-21T18:16:55.287581+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2296 · 2026-05-21T18:16:55.388495+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2297 · 2026-05-21T18:17:02.316277+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026's call for papers and ARR submission guidelines:

## General Call for Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using e
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7331
}
```

</details>

---


### Tool call

_source line 2298 · 2026-05-21T18:17:07.490056+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May cycle submission deadline page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2299 · 2026-05-21T18:17:08.293238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2300 · 2026-05-21T18:17:08.444361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2301 · 2026-05-21T18:17:08.494969+00:00_

1	\begin{abstract}
2	We study structural degeneration in neurosymbolic reasoning trained with GRPO: models achieve high prove rates while most outputs embed the conclusion among premises---a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic applying leave-one-out necessity testing to solver inputs; the fraction of necessary components yields the \emph{Intensional Structural Reward} (ISR), whose diagnostic value is realized through mode-level analysis.
4	As a diagnostic, component-necessity testing reveals a collapse trajectory hidden from prove rate: the mode breakdown shows ${\geq}87\%$ structural hacking while prove rate rises, with each seed converging to a qualitatively different hacking mode.
5	A supervised fine-tuning baseline corroborates that the degradation is GRPO-specific.
6	When repurposed as a training reward, ISR exhibits a seed-dependent Goodhart effect: in 3 of 5 seeds, hacking composition shifts from conclusion embedding to tautological shortcutting ($p{<}10^{-15}$) without reducing overall prevalence ($p{=}0.182$); 2 of 5 seeds retain ${\sim}55\%$ genuine reasoning, showing the effect is stochastic rather than deterministic.
7	Cross-logic (Prolog) and cross-dataset (ProofFOL) evidence confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2302 · 2026-05-21T18:17:08.596432+00:00_

1	issues:
2	# === Resolved issues from rounds 0-21 (condensed) ===
3	- id: R1-W1
4	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
11	  resolution_round: 2
12	- id: RV-EVAL-FALLBACK
13	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: stderr ERROR → sys.exit(1)。
20	  resolution_round: 1
21	- id: R1-W2
22	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
23	  category: framing
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 15
28	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
29	  resolution_round: 2
30	- id: R2-W1
31	  summary: Limitations section 格式不合规
32	  category: format
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 2
37	  resolution: 独立 limitations.tex 已创建。
38	  resolution_round: 3
39	- id: R2-W2
40	  summary: 实验仅用单一模型和单一数据集
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 2
46	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
47	  resolution_round: 3
48	- id: R2-W6
49	  summary: SFT baseline 比较不公平：PR=14% vs 93%
50	  category: experiment
51	  severity: critical
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 2
55	  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
56	  resolution_round: 2
57	- id: v2-R1-N1
58	  summary: Abstract '93%' PR 为 single seed
59	  category: writing
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 2
63	  last_seen_round: 3
64	  resolution: Abstract 使用 3-seed pooled mean±std。
65	  resolution_round: 3
66	- id: v2-R1-N3
67	  summary: 仅 2 个 β 值不足以刻画 dose-respons
…[truncated 26127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-21T18:17:14.771197+00:00_

Web search results for query: "EMNLP 2026 ARR May cycle submission deadline page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is the information about EMNLP 2026 ARR May cycle submission details:

## ARR May Cycle Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limit

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## Format Requirements

EMNLP uses the standard ACL style files, so the LaTeX templ
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7281
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-21T18:17:29.702893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-21T18:17:30.206764+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalizatio
…[truncated 4721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-21T18:17:30.207269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-21T18:17:31.161459+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 4408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-21T18:17:31.262424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-21T18:17:31.614489+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 15499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-21T18:17:31.614912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-21T18:17:32.167381+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; \citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.
12	\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
13	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural s
…[truncated 2434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-21T18:17:32.167826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2313 · 2026-05-21T18:17:32.368911+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: the mode breakdown reveals ${\geq}87\%$ structural hacking under exec-only GRPO while PR rises (ISR collapses $214\times$ for seed~42, partially amplified by premise-count inflation), while SFT results are consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}).
5	Cross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\S\ref{sec:crosslogic}).
6	Repurposed as a reward, ISR produces a seed-dependent compositional Goodhart effect: on FOLIO, 3 of 5 seeds shift hacking from CE to TS ($p{<}10^{-15}$) without reducing prevalence ($p{=}0.182$), while 2 retain ${\sim}55\%$ non-hacking; deconfounding collapses the apparent ISR advantage to $1.06\times$; on ProofFOL, preliminary evidence ($p{=}0.10$) suggests beneficial instability (\S\ref{sec:goodhart}).
7	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
8	
9	For practitioners in similar settings (\S\ref{sec:limitations}): evaluate with ISR and component count jointly (not PR alone), report multi-seed results, and use ISR for post-hoc diagnosis only---any dose induces gaming or collapse when optimized (Appendix~\ref{app:practical-guidelines}).
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2314 · 2026-05-21T18:17:32.369276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2315 · 2026-05-21T18:17:32.419772+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.
5	Cross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\text{PR}{\approx}15\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\ref{app:llama-coldstart}), establishing a capability threshold below which STA's degeneration analysis is uninformative (the model cannot hack what it cannot prove).
6	Three seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.
7	At our scale (500 training / 100 evaluation examples), non-hacking rates of ${\sim}5\%$ correspond to ${\sim}5$ samples, limiting mode-level precision.
8	ISR quantifies syntactic component necessity, not semantic faithfulness ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-21T18:17:40.150467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-21T18:17:40.703907+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 46475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-21T18:17:41.206220+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2319 · 2026-05-21T18:17:41.206666+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-21T18:17:41.652465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-21T18:17:41.816256+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 2319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 163
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-21T18:18:02.924545+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool call

_source line 2323 · 2026-05-21T18:18:05.285060+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "solver-trace-ablation",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "solver-trace-ablation",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 2324 · 2026-05-21T18:18:25.094013+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22169
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-21T18:18:25.094386+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 19809
}
```

</details>

---


### Tool call

_source line 2326 · 2026-05-21T18:18:25.245618+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026（ARR May cycle）\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper（正文 8 页限制，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入 8 页）\n- **Checklist**: Responsible NLP Research Checklist 在 OpenReview 提交表单中填写\n\n### 论文信息\n- **标题**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n- **路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### 你的审查侧重\n\n**主要职责：方法严谨性 + 实验设计**\n\n请重点审查以下方面：\n\n1. **统计方法与效力**\n   - N=3 seeds 的统计效力是否足够支撑核心 claims\n   - CMH 检验的独立性假设是否合理（within-seed pseudo-replication）\n   - p=0.182 non-hacking rate 比较、p=0.10 ProofFOL 结果的叙事权重是否与统计证据匹配\n   - Bonferroni 校正的合理性\n\n2. **实验控制与 Confound**\n   - Premise-count confound：214× collapse → 1.06× matched 的处理是否充分\n   - SFT baseline 的公平性（PR=13% vs 93%）\n   - 100-step checkpoint 控制（n=32）的样本量是否足够\n   - Shuffled-ISR control 的设计与解释\n   - Seed 43 sampling (T=0.7) vs greedy 的影响\n\n3. **Classifier 可靠性**\n   - Text-match classifier 的 recall 上界问题\n   - PG audit 仅限 seed 42 的影响\n   - Non-hacking rate 作为 upper bound 的可信度\n   - ProofFOL \"genuine\" 用 coarser classifier 与 FOLIO 8-mode 的可比性\n\n4. **可复现性**\n   - s43/s44 checkpoints 已删除的影响\n   - 代码和数据匿名化处理\n   - 实验参数是否充分报告\n\n5. **LOO 方法论**\n   - LOO 独立性假设在 FOLIO 2-6 前提设定下的合理性\n   - ISR 乘法耦合 reward 的 confound 控制\n\n请按 Strengths / Weaknesses（逐条列出，标注 severity: Must-Fix / Should-Fix / Minor） / Questions / Missing References 格式输出审稿意见。对每个 Weakness 给出具体改进建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026（ARR May cycle）\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper（正文 8 页限制，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入 8 页）\n- **Checklist**: Responsible NLP Research Checklist 在 OpenReview 提交表单中填写\n\n### 论文信息\n- **标题**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n- **路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### 你的审查侧重\n\n**主要职责：方法严谨性 + 实验设计**\n\n请重点审查以下方面：\n\n1. **统计方法与效力**\n   - N=3 seeds 的统计效力是否足够支撑核心 claims\n   - CMH 检验的独立性假设是否合理（within-seed pseudo-replication）\n   - p=0.182 non-hacking rate 比较、p=0.10 ProofFOL 结果的叙事权重是否与统计证据匹配\n   - Bonferroni 校正的合理性\n\n2. **实验控制与 Confound**\n   - Premise-count confound：214× collapse → 1.06× matched 的处理是否充分\n   - SFT baseline 的公平性（PR=13% vs 93%）\n   - 100-step checkpoint 控制（n=32）的样本量是否足够\n   - Shuffled-ISR control 的设计与解释\n   - Seed 43 sampling (T=0.7) vs greedy 的影响\n\n3. **Classifier 可靠性**\n   - Text-match classifier 的 recall 上界问题\n   - PG audit 仅限 seed 42 的影响\n   - Non-hacking rate 作为 upper bound 的可信度\n   - ProofFOL \"genuine\" 用 coarser classifier 与 FOLIO 8-mode 的可比性\n\n4. **可复现性**\n   - s43/s44 checkpoints 已删除的影响\n   - 代码和数据匿名化处理\n   - 实验参数是否充分报告\n\n5. **LOO 方法论**\n   - LOO 独立性假设在 FOLIO 2-6 前提设定下的合理性\n   - ISR 乘法耦合 reward 的 confound 控制\n\n请按 Strengths / Weaknesses（逐条列出，标注 severity: Must-Fix / Should-Fix / Minor） / Questions / Missing References 格式输出审稿意见。对每个 Weakness 给出具体改进建议。"
  }
}
```

</details>

---


### Tool result

_source line 2327 · 2026-05-21T18:18:41.830535+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16584
}
```

</details>

---


### Tool call

_source line 2328 · 2026-05-21T18:18:42.033057+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026（ARR May cycle）\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper（正文 8 页限制，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入 8 页）\n- **Checklist**: Responsible NLP Research Checklist 在 OpenReview 提交表单中填写\n\n### 论文信息\n- **标题**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n- **路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### 你的审查侧重\n\n**主要职责：新颖性 + 完整性 + 写作质量**\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**\n   - LOO 作为 50+ 年老技术，本文的方法论新颖性是否足够（即使定位为 empirical contribution）\n   - C1（STA 诊断框架）和 C2（compositional Goodhart effect）的贡献层级是否清晰\n   - 与已有工作的差异化是否充分（Kim et al. 2026 inference-time gaming, Helff et al. 2026 IPT, Dong et al. 2026）\n   - \"Case study\" 定位与 C1/C2 通用性声称之间的张力\n\n2. **Framing 一致性**\n   - Title 中 \"Structural Degeneration\" 与正文 \"component necessity\" 的关系\n   - \"Compositional Goodhart effect\" 是否有严格操作性定义，是否映射到 Manheim taxonomy\n   - Abstract/Introduction 中的核心叙事是否与实验证据强度匹配\n   - 5-seed 结果（3/5 gaming vs 2/5 genuine）是否在 Abstract/Intro/Conclusion 中一致呈现\n   - \"seed-dependent\" qualifier 是否充分传达 C2 的局限性\n\n3. **Related Work 完整性**\n   - 是否遗漏重要相关工作（特别是 2025-2026 RLVR/reward hacking 新文献）\n   - 引用格式和 bib entry 准确性\n   - 引用是否存在 LLM 幻觉嫌疑\n\n4. **写作质量**\n   - 术语密度和缩写体系（ISR/ISR*/ISR†、CE/TS/PG 等）的可读性\n   - 叙事结构：是否在首次提到关键发现时充分呈现 caveats\n   - 表格和图表的信息密度与可读性\n   - Limitations 章节是否充分覆盖主要局限\n\n5. **格式合规**\n   - 正文是否在 8 页以内\n   - 匿名合规（是否泄露作者身份）\n   - 参考文献格式\n   - Limitations 章节位置和格式\n\n请按 Strengths / Weaknesses（逐条列出，标注 severity: Must-Fix / Should-Fix / Minor） / Questions / Missing References 格式输出审稿意见。对每个 Weakness 给出具体改进建议。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026（ARR May cycle）\n- **截止日期**: 2026-05-25\n- **类型**: Long Paper（正文 8 页限制，参考文献不限）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入 8 页）\n- **Checklist**: Responsible NLP Research Checklist 在 OpenReview 提交表单中填写\n\n### 论文信息\n- **标题**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n- **路径**: `projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### 你的审查侧重\n\n**主要职责：新颖性 + 完整性 + 写作质量**\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**\n   - LOO 作为 50+ 年老技术，本文的方法论新颖性是否足够（即使定位为 empirical contribution）\n   - C1（STA 诊断框架）和 C2（compositional Goodhart effect）的贡献层级是否清晰\n   - 与已有工作的差异化是否充分（Kim et al. 2026 inference-time gaming, Helff et al. 2026 IPT, Dong et al. 2026）\n   - \"Case study\" 定位与 C1/C2 通用性声称之间的张力\n\n2. **Framing 一致性**\n   - Title 中 \"Structural Degeneration\" 与正文 \"component necessity\" 的关系\n   - \"Compositional Goodhart effect\" 是否有严格操作性定义，是否映射到 Manheim taxonomy\n   - Abstract/Introduction 中的核心叙事是否与实验证据强度匹配\n   - 5-seed 结果（3/5 gaming vs 2/5 genuine）是否在 Abstract/Intro/Conclusion 中一致呈现\n   - \"seed-dependent\" qualifier 是否充分传达 C2 的局限性\n\n3. **Related Work 完整性**\n   - 是否遗漏重要相关工作（特别是 2025-2026 RLVR/reward hacking 新文献）\n   - 引用格式和 bib entry 准确性\n   - 引用是否存在 LLM 幻觉嫌疑\n\n4. **写作质量**\n   - 术语密度和缩写体系（ISR/ISR*/ISR†、CE/TS/PG 等）的可读性\n   - 叙事结构：是否在首次提到关键发现时充分呈现 caveats\n   - 表格和图表的信息密度与可读性\n   - Limitations 章节是否充分覆盖主要局限\n\n5. **格式合规**\n   - 正文是否在 8 页以内\n   - 匿名合规（是否泄露作者身份）\n   - 参考文献格式\n   - Limitations 章节位置和格式\n\n请按 Strengths / Weaknesses（逐条列出，标注 severity: Must-Fix / Should-Fix / Minor） / Questions / Missing References 格式输出审稿意见。对每个 Weakness 给出具体改进建议。"
  }
}
```

</details>

---


### Tool result

_source line 2329 · 2026-05-21T18:18:43.370975+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1337
}
```

</details>

---


### Assistant

_source line 2330 · 2026-05-21T18:18:50.802019+00:00_

圆桌审稿 Round 1 已全部派发：

| 任务 | 状态 |
|------|------|
| **Reviewer 1**（方法严谨性 + 实验设计） | 已启动 |
| **Reviewer 2**（新颖性 + 完整性 + 写作） | 已启动 |
| **视觉审查 Agent** | 已启动（并行，非评分项） |
| **外部审稿（Stanford Agentic Reviewer）** | 已发送请求，等待用户提交 |

等待两位 Reviewer 返回独立审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 203

## Round 203

2 recorded events


### User

_source line 2331 · 2026-05-21T18:24:50.959335+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study"

**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分

**Overall**: 3.0 — Findings（可被 Findings 接收）

**一句话总结**: 一项扎实的实证案例研究，用简单但有效的诊断工具揭示了 GRPO 训练中的结构退化现象，但方法论新颖性有限（LOO 是标准技术），关键发现 C2 依赖种子且统计效力不足，case study 定位与 C1 通用性声称之间存在未解决的张力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 实验设计合理，控制条件充分（6 种 reward condition），但规模受限（1 个模型家族、5 个种子），C2 的关键发现仅在 3/5 种子中出现，统计效力自认不足（d≥2.0 才达 80% power）|
| Excitement | 2.5/5 | 诊断方法本身直截了当（LOO 的直接应用），发现有趣但在并发工作（Helff 2026 IPT、Khalifa 2026 Countdown-Code）背景下不算意外，case study 定位限制了更广泛的影响 |
| Confidence | 4/5 | 仔细阅读了全文（含 22 页 appendix），熟悉 RLVR/reward hacking 和 neurosymbolic reasoning 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] C1 的方法论新颖性与 Helff et al. (2026) IPT 的区分不充分

- **具体位置**: Section 2 (Related Work, p3), Section 3.2 (p4)
- **问题**: STA 的核心操作是对 solver 输入逐一移除组件并重跑——这与 Helff et al. (2026) 的 Input Perturbation Testing (IPT) 在概念层面高度相似：两者都通过扰动验证器输入来检测 gaming。论文声称 "ISR differs in operating at the component level (LOO ablation) rather than the token level"（Section 2, p3），但这一区分是粒度层面的，不是方法论本质的区分。Algorithm 1（p4）只有 7 行伪代码，本质上是标准 LOO。
- **为什么影响接收**: 如果方法论贡献（C1）与并发工作的差异仅在操作粒度上，reviewer 和 AC 会质疑"是否值得一篇独立论文"。
- **建议修改方向**: (1) 在 Section 2 或 Section 3 中增加与 IPT 的系统对比（表格形式），明确列出 STA 在哪些维度提供了 IPT 不具备的诊断能力（如 hacking mode 分类、ISR 的连续量化 vs. IPT 的二元检测）；(2) 如果核心贡献定位为 empirical findings 而非方法论，应在 Introduction 中更明确地表态。

**N2** [critical] "Compositional Goodhart effect"（C2）的操作性定义缺失，且 seed-dependent 限制在 Abstract 中被弱化

- **具体位置**: Abstract (p1), Section 1 (p2), Section 4.3 (p6), Section 5 (p8)
- **问题**: 
  - "Compositional Goodhart effect" 这一术语在论文中首次出现于 Abstract 和 Introduction，但始终没有给出严格的操作性定义。论文将其映射到 Manheim taxonomy 的 "regressional Goodhart"（Introduction p2: "this instantiates regressional Goodhart"），但 regressional Goodhart 描述的是代理指标在优化下与真实目标脱钩——这与"hacking mode 的组成比例发生变化"是不同层面的现象。"Compositional" 一词在 NLP 中有强烈的"组合泛化"含义，容易引起误读。
  - C2 仅在 3/5 种子中观察到（Section 4.3, p6: "seed-dependent: 3 of 5 seeds"），2/5 种子显示 genuine learning。但 Abstract（p1）的表述 "reveals a collapse trajectory... with each converging to a qualitatively different degeneration mode" 给人的印象是所有种子都退化，只是退化模式不同。直到第 2 页才出现 "2 of 5 seeds retain ~55% genuine reasoning" 这一关键限定。
  - Section 4.3 中支撑 "compositional shift" 的 CMR p-value 为 p<0.17，这在常规标准下**不显著**。
- **为什么影响接收**: C2 是本文两个核心贡献之一。如果操作性定义模糊、统计证据不足、且 Abstract 中呈现不完整，会被 reviewer 视为 overclaiming。
- **建议修改方向**: (1) 在 Section 3 或 4.3 给出 "compositional Goodhart effect" 的形式化定义（例如：当 hacking mode 的分布在训练过程中发生非随机转移时...）；(2) Abstract 中明确加入 "3 of 5 seeds" 限定；(3) 将 "compositional Goodhart" 与 Manheim taxonomy 的映射做得更严谨，或降级为 "observed pattern" 而非 "effect"；(4) 如果 CMR p<0.17 是唯一支撑证据，应明确标注为 exploratory。

**N3** [critical] 单模型+相关数据集的泛化性与 C1 "diagnostic framework" 声称之间的矛盾

- **具体位置**: Section 1 (p2, contributions), Section 4.1 (p5), Section 4.4 (p7), Section 6 Limitations (p8)
- **问题**: C1 声称 STA 是一个 "diagnostic applying leave-one-out component-necessity testing to solver inputs"——措辞暗示通用性。但实验仅涉及：(1) 一个模型家族 Qwen3-1B；(2) 一个核心数据集 FOLIO（500 例）+ 一个衍生数据集 ProofFOL（由 GPT-4o 翻译 ProofWriter 构建，Section 4.4/Appendix B）。ProofFOL 被呈现为 "cross-dataset evidence"，但它是从 ProofWriter 机械翻译而来，共享相似的逻辑结构（Table 4, p12 显示 ProofFOL 的结构属性与 FOLIO 差异有限）。这不等于在真正独立的数据集上验证。
  - Prolog 实验（Section 4.4, p7）提供了跨 solver 的证据，这是有价值的，但仍然在同一个 FOLIO 数据集上。
  - Limitations (p8) 承认 "single model family and dataset"，但 C1 的措辞没有相应降级。
- **为什么影响接收**: "Case study" 标题与 "framework" 贡献声称的张力会让 reviewer 困惑于论文的定位。如果是 case study，C1 应描述为"方法+初步验证"；如果是 framework，需要更多模型和数据集。
- **建议修改方向**: (1) 将 C1 的措辞从 "diagnostic framework" 降级为 "diagnostic method demonstrated on..." 或在 C1 中明确限定适用范围；(2) 如果可行，增加至少一个非 FOL 类型的 neurosymbolic 任务（如数学推理中的 symbolic verification）作为验证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SFT baseline 对比的公平性

- **具体位置**: Section 4.2 (p5-6), Table 1 (p7)
- **问题**: SFT baseline 的 PR=13.0%（92.3% non-hacking），GRPO 的 PR≈93%（高 hacking）。论文用 SFT 作为 "non-hacking upper bound"（p5: "An SFT baseline on identical data reaches PR=13.0% with 92.3% non-hacking"），但这是在比较一个严重 underfit 的模型和一个 overoptimized 的模型。更有意义的对比是：GRPO 在达到与 SFT 相同 PR 水平时的 ISR 值（可以从 Figure 1 的早期 training steps 读出）。Table 1 的 "SFT" 行和 "ISR β=0.1" 行直接放在一起，暗示读者将两者对比，但两者的 PR 差距巨大（13% vs 72-93%），不在同一可比水平。
- **建议**: 增加一个 "GRPO at matched-PR" 的对比行，或在讨论中明确指出 SFT 的作用仅是提供非 RL 训练的参考点。

**W2** [warning] 术语密度过高，阻碍可读性

- **具体位置**: 全文，尤其 Section 3.3 (p4-5), Section 4.5 (p7), Appendix D (p14-17)
- **问题**: 论文引入了大量缩写体系：
  - 指标：ISR, ISR*（premise-only）, ISR†（未充分解释区别）
  - Hacking modes：CE, TS, PG, CI（加上 Appendix 的 Contradiction Explosion, Complexity-without-Utility, Repetition Collapse, Query-as-fact Gaming 等）
  - 还有标准缩写：STA, LOO, GRPO, FOL, PR, NLI, CMR
  
  仅 hacking mode 就有 8+ 种（Section 4.5, p7; Appendix D, p14-17），其中部分（如 D.7 Complexity-without-Utility, D.9 Query-as-fact Gaming）出现率低且对主线论证贡献有限。ISR/ISR*/ISR† 三个变体的区分在首次引入时不够清晰（ISR* 在 p4 Section 3.2 "Intensional Structural Reward" 中定义，但 ISR† 的首次出现和定义位置不明确）。
- **建议**: (1) 在正文中只保留核心 3-4 个 hacking modes，其余移入 Appendix；(2) 增加一个 notation table（可放在 Section 3 开头或 Appendix）汇总所有符号/缩写；(3) 明确 ISR 各变体的定义和适用场景差异。

**W3** [warning] Title 中 "Structural Degeneration" 与正文 "component necessity" 的概念跳跃

- **具体位置**: Title, Abstract (p1), Section 3.2 (p4)
- **问题**: ISR 直接测量的是 **component necessity**（移除某组件后 solver 输出是否变化）。从 "低 component necessity" 到 "structural degeneration" 是一个推断而非直接测量。一个 formalization 可以有冗余组件（低 ISR）但逻辑上完全正确（例如多余前提但结论正确）；反之也可能所有组件都 necessary 但语义不忠实。论文在 Appendix C (p12) 讨论了 premise-count confound，但 title 的 "Structural Degeneration" 暗示了比 ISR 实际能测量的更强的主张。
- **建议**: (1) 在 Section 3.2 中增加一段明确讨论 "component necessity" 与 "structural degeneration" 之间的关系和已知 gap；(2) 考虑在 title 中使用更精确的术语（如 "Component Redundancy" 或保留 "Structural Degeneration" 但在 Abstract 第一句就明确其操作化定义）。

**W4** [warning] Hacking Taxonomy（Section 4.5）的验证深度不足

- **具体位置**: Section 4.5 (p7), Appendix D (p14-17)
- **问题**: 论文识别了 8 种 hacking modes（Table 2, p8；Appendix D 有完整定义）。验证方式为：手工检查 50 个 randomly sampled outputs（Section D, p14: "all 50 were confirmed correct, estimated precision >95%, Wilson 95% CI: 89.5%, 100%"）。但：
  - 50 个样本对 8 个类别来说偏少（平均每类 ~6 个）
  - Classifier Validation（Appendix D, p14）使用 text-match classifiers，其中一些 mode 的检测依赖表面模式匹配（如 TS 的 "single-premise conclusion matching"），可能存在假阴性
  - Table 6 (p15) 显示 8 种 mode 的分布极不均匀（CE 和 TS 占主导，其余 mode 的样本量很小）
- **建议**: (1) 增加 inter-annotator agreement 或至少报告 annotator 的领域背景；(2) 对低频 mode 明确标注为 "tentative/exploratory"。

---

## 小问题（不影响接收）

- **M1**: FOLIO bib entry (key: `folio`) year 标注为 2024，但 OpenAlex 显示 2022（原始 arXiv 版本）。如果引用的是 EMNLP 2024 正式发表版，应确认 venue 信息一致。
- **M2**: `metr-reward-hacking` (Von Arx et al., 2025) 作为 `@misc` 类型，缺少 venue/url 信息。作为 blog post 引用应提供完整 URL。
- **M3**: Figure 3 (p8) 的 hacking composition stacked bar chart 在黑白打印下可区分性较差，建议增加纹理区分。
- **M4**: Section 4.2 (p5) "Fischer exact tests" — 应为 "Fisher exact tests"（如果原文拼写有误）。[需验证原文拼写]
- **M5**: Appendix E.3 (p18-19) 的 "Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure" 实验显示 LLaMA 无法生成有效 FOL 输出，因此被排除。这进一步说明 C1 的通用性受限于模型对 FOL 的先验能力，值得在 Limitations 中提及。
- **M6**: Checklist (p19-20) 中 B5 提到 "Responsible NLP Research Checklist 在 OpenReview 提交表单中填写"，这与 EMNLP 2026 规定一致。格式合规。

---

## Missing References / 潜在遗漏

1. **Mutation testing 在 ML/code generation 中的应用**: LOO/mutation testing 已被用于评估 LLM 代码生成质量（如 MuTAP, EvalPlus 等），论文将 mutation testing 追溯到 DeMillo 1978 但没有讨论其在 ML 领域的近期应用，这是 related work 的一个小缺口。
2. **RLVR 中的 reward shaping 文献**: 论文引用了 Ng et al. 1999 (reward shaping)，但近期有更多关于 composite/multi-component reward 设计的工作（如 reward decomposition in RLHF），可能与 "compositional Goodhart" 讨论相关。
3. 引用完整性总体良好（49 entries 全部被引用，无 orphan/missing），未发现明显 LLM 幻觉引用。

---

## 主要优势

- **S1**: 实验设计严谨——6 种 reward condition（exec-only, ISR β={0.1, 0.3}, Random, SFT, Shuffled-ISR）形成了系统的消融，控制变量清晰。
- **S2**: 跨 solver（FOL/Prover9 vs Prolog/SWI-Prolog）验证增强了 structural degeneration 发现的可信度（Section 4.4, Figure 2）。
- **S3**: 诚实的 Limitations section，明确承认 single model、seed-dependent、syntactic-not-semantic 等主要局限。
- **S4**: Hacking taxonomy（8 种 mode 的详细定义和实例，Appendix D）是有价值的社区资源，即使部分 mode 的统计支撑较弱。
- **S5**: ISR 作为 reward signal 时反而加速 gaming 的发现（Section 4.3）有反直觉的洞察价值——说明结构指标作为训练信号会被 Goodhart 化。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤ 8 页 | ✅ | Sections 1-5 约 7.6 页，Limitations 在 p8 底部（不计入） |
| 匿名合规 | ✅ | "Anonymous ACL submission"，代码/数据标注 [anonymized] |
| Limitations 章节 | ✅ | Section 6，p8 底部，独立章节 |
| 参考文献格式 | ✅ | 标准 ACL natbib 格式 |
| Ethics Statement | ✅ | Section 7, p9 |
| Checklist | ⚠️ | Checklist 出现在 PDF 中（p19-20），但 EMNLP 2026 规定 Checklist 在 OpenReview 表单中填写而非 PDF 中。论文在 Checklist 开头标注了这一点，但 PDF 中包含 checklist 内容可能导致页数统计争议。建议确认 venue 是否允许 PDF 中附带 checklist。 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2332 · 2026-05-21T18:24:58.088021+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 204

## Round 204

2 recorded events


### User

_source line 2333 · 2026-05-21T18:25:01.990788+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：

- **Overall: 3.0 (Findings)**——扎实的实证案例研究，但方法论新颖性不足以进入主会议
- **3 个 Must-Fix**：(1) 与 Helff 2026 IPT 的方法论区分不充分；(2) "Compositional Goodhart effect" 缺乏操作性定义且 3/5 seed-dependent；(3) 单模型+相关数据集与 "framework" 声称的矛盾
- **4 个 Should-Fix**：SFT 对比公平性、术语密度过高、title "Structural Degeneration" 的概念跳跃、hacking taxonomy 验证深度不足
- **6 个 Minor**：bib year 问题、missing URL、图表可读性、拼写、LLaMA 实验对通用性的启示、checklist 位置
- **主要优势**：实验设计严谨（6 种 reward condition）、跨 solver 验证、诚实的 limitations、ISR-as-reward 的反直觉发现

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2334 · 2026-05-21T18:25:08.483750+00:00_

Reviewer 2 的意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 205

## Round 205

6 recorded events


### User

_source line 2335 · 2026-05-21T18:25:10.833426+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计）

**论文**: "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study"

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 论文提出了一个有价值的诊断工具（STA/ISR），但 N=3 seeds 的统计效力、premise-count confound 的不完全消除、以及 2/3 seed checkpoints 已删除的可复现性问题，使核心 claims 的证据支撑不足以达到主会议接收标准。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法论（LOO ablation）原理合理，但 N=3 统计效力不足、pseudo-replication、多个非显著 p 值被赋予过高叙事权重、premise-count confound 仅降至 1.06× 而非消除 |
| Excitement | 3/5 | 问题重要且时机正确（RL reward hacking 诊断），但执行规模有限（单模型系列、单数据集家族、3 seeds），限制了方法论贡献的 impact |
| Reproducibility | 3/5 | Seed 43/44 checkpoints 已删除不可恢复（§E, Limitations），2/3 seeds 无法验证；代码承诺匿名发布但当前不可用；超参报告充分（Appendix A） |
| Confidence | 4/5 | 仔细检查了统计方法、实验设计和 confound 控制 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 的统计效力根本不足以支撑核心 claims
- 具体位置：Section 4.1, Appendix C ("Statistical considerations"), Table 1, Table 3
- 问题：全部核心结论基于 3 个随机种子（42, 43, 44）。论文自己承认 "seed-level test-level textures achieve 80% power only for very large effects (d≥2.0); non-significant comparisons (e.g., prevalence p=0.182) are exploratory"（p.5）。但论文随后仍用这 3 个种子的行为模式构建了 "seed-dependent Goodhart effect" 的完整叙事（§4.3），将每个种子的不同表现解释为有意义的 "distinct modes"（seed 42=CE dominance, seed 43=mixed, seed 44=tautological collapse）。N=3 下，无法区分真正的多模态分布与采样噪声。
- 为什么影响接收：这是方法论的根基问题。论文的核心贡献之一是 "documenting STA as GRPO-specific" 和 "dataset-dependent Goodhart"，但 3 seeds 不足以对此作统计推断。CMH 检验报告的 p-values（如 p<0.001 for TS association）依赖 within-seed samples 作为独立观测，实际是 pseudo-replication（见 N2）。
- 建议修改方向：(1) 增加至少到 N=10 seeds 以获得 medium effect size 的合理 power；(2) 若计算资源不允许，需大幅降低 claims 的强度，将所有 cross-seed 比较明确标注为 "exploratory/descriptive" 而非因果推断；(3) 报告 effect sizes 和 confidence intervals 而不仅是 p-values。

**N2** [critical] CMH 检验的 pseudo-replication 问题
- 具体位置：Section 4.1 ("Statistical considerations"), Table 3, Appendix C
- 问题：CMH 检验将每个种子内的 proved samples（如 seed 42 的 100 个 FOLIO 样本）视为独立观测，但这些样本来自同一个训练好的模型。同一模型生成的输出之间存在系统性相关（共享相同权重），这违反了 CMH 的独立性假设。论文承认 "the true replication count is N=3"（p.5），但仍在 Table 3 中报告基于 hundreds of samples 的 CMH p-values（如 "Wilcox Chi" p<0.001），且在正文中引用这些结果作为主要证据。
- 为什么影响接收：如果独立性假设不成立，所有基于 within-seed sample 的统计检验的 p-values 都会被系统性低估（type I error inflation）。论文在方法论贡献中使用了这些检验结果，但未对 pseudo-replication 的影响做任何敏感性分析。
- 建议修改方向：(1) 将 seed 作为分析的基本单位（N=3），仅报告 seed-level aggregates 的统计检验；(2) 或使用 mixed-effects model 将 seed 作为 random effect；(3) 明确标注 CMH 结果为 "within-seed descriptive statistics" 而非推断性证据。

**N3** [critical] Premise-count confound 未充分消解，1.06× 结果反而削弱核心主张
- 具体位置：Section 3.2, Section 4.3 ("Multiplicative coupling"), Appendix C ("The premise-count confound"), Table 7
- 问题：论文承认 "ISR is mechanically coupled to component count (n=2 → ISR≥0.5)"（§3.2）。Premise-count-matched 分析将 raw ISR advantage 从 3.2× 降至 1.06×（§4.3, Table 7）。1.06× 在统计上与 1.0 无异——这意味着 ISR-as-reward 的表观成功几乎完全是 premise-count artifact。论文将此解释为 "ISR β=0.1 seed 42 produces shorter formalizations, mechanically inflating ISR"（Appendix C），但这恰恰说明 ISR 作为 reward signal 并没有真正激励 structural quality，只是奖励了更短的输出。
- 为什么影响接收：这个 confound 动摇了论文关于 "ISR as reward" 实验条件的所有解释。如果 ISR-as-reward 的唯一 "成功" 可以完全归因于 premise-count bias，那么 ISR 作为训练信号的有效性主张（§4.3 的核心叙事）就失去了实验支撑。
- 建议修改方向：(1) 在正文（而非仅 appendix）中明确报告 premise-count-matched 后 ISR advantage 几乎消失的事实；(2) 考虑使用 normalized ISR（除以 premise count）作为 reward signal 的替代实验；(3) 重新构建叙事——当前论文暗示 ISR-as-reward "partially works"，但数据表明它可能完全不 work。

**N4** [critical] Seed 43 使用不同解码策略（T=0.7 vs greedy），污染 3-seed aggregates
- 具体位置：Appendix A ("Evaluation exception"), Table 7 (seed 43 rows), Table 1 (3-seed means)
- 问题：Seed 43（plan0303-exec-only+s43+r4）因原始 checkpoint 问题，使用 sampling temperature=0.7 而非 greedy decoding 进行评估。论文承认 "its PR and ISR values are included for completeness but are not strictly comparable with other seeds"（Appendix A, p.12）。然而，seed 43 仍被纳入所有 3-seed aggregates（Table 1 的 "3-seed mean(sd)" 行、Table 3 的 ISR pooled statistics）。在 N=3 的设定下，一个使用不同评估协议的种子占总样本的 33%，会显著扭曲 aggregate statistics。
- 为什么影响接收：Sampling T=0.7 会引入随机性，可能改变 hacking mode distribution、ISR 值、和 prove rate。将不可比的数据混入 aggregates 是实验设计的基本错误。
- 建议修改方向：(1) 从所有 aggregate statistics 中排除 seed 43，改为仅 2-seed aggregates 并在正文中解释原因；(2) 或使用相同的 greedy protocol 重新评估 seed 43（如果 checkpoint 仍可用——但据报告已删除，见 N5）；(3) 将 seed 43 结果移入 appendix 作为 "supplementary observation"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SFT baseline 的公平性问题（PR=13% vs 93%）
- 具体位置：Section 4.2 ("SFT baseline"), Table 1 (SFT row)
- 问题：SFT 的 prove rate 仅 13%，而 GRPO exec-only 达 93%。论文将 SFT 作为 "non-hacking upper bound"（92.3% non-hacking），但在 PR 差异如此悬殊的情况下，non-hacking rate 不可比。一个几乎无法生成正确证明的模型自然不会展示 "hacking"——它连正确的输出都产生不了。这是 base rate 问题，而非 SFT 真正避免了 hacking。
- 建议：(1) 使用 PR-matched 的比较（例如取 GRPO 早期 checkpoint 与 SFT 在相同 PR 水平的比较）；(2) 或明确讨论 base rate confound，不将 SFT 的低 hacking rate 作为 "SFT avoids hacking" 的证据。

**W2** [warning] PG (Premise-subset Gaming) audit 仅限 seed 42，泛化性不足
- 具体位置：Appendix D.1, p.15 ("Full PG audit was completed for ISR β=0.1 seed 42 only")
- 问题：PG 模式的人工审计仅在一个种子上完成。Table 6 报告 PG 在 exec-only 条件下占 non-trivial 比例（Table 6: exec-only seed 42 有 7 个 PG），但其他种子的 PG 分布可能不同。鉴于论文声称 hacking modes 是 "seed-dependent"（§4.3），仅审计一个种子的做法与这个 claim 相矛盾。
- 建议：至少在 2 个种子上完成 PG audit，或明确将 PG 分析范围限定为 seed 42。

**W3** [warning] Text-match classifier 的 recall 上界问题
- 具体位置：Appendix D ("Classifier Validation"), p.14
- 问题：分类器使用确定性 rule-based text matching（regex 匹配 conclusion-premise 字符串重叠）。论文承认 "text-match classifiers have systematic blind spots that functional analysis exposes"（p.13）。50 个样本的 cross-validation 确认了 precision（100%），但 recall 未报告。如果存在论文规则未覆盖的 novel hacking patterns，non-hacking rate 将被系统性高估。
- 建议：(1) 报告 classifier recall（至少在功能分析覆盖的子集上）；(2) 讨论 recall ceiling 对 non-hacking rate 作为 upper bound 的具体影响。

**W4** [warning] 100-step checkpoint 分析的样本量不足（n=32）
- 具体位置：Appendix E.2 ("Early-Training Hacking Analysis, 100-Step Checkpoint")
- 问题：100-step checkpoint 仅有 32 个 proved samples。在此基础上进行 hacking mode classification 和时间趋势分析，统计可靠性极低。论文用此论证 "hacking emerges early in GRPO training, well before the prove-rate plateau"（p.18），但 n=32 不足以支撑这一时序 claim。
- 建议：承认 n=32 的局限性，将结论从 "demonstrates" 降级为 "suggests"。

**W5** [warning] LOO 独立性假设在 FOLIO 多前提设定下的合理性
- 具体位置：Section 3.2, Appendix C
- 问题：LOO 假设每个 component 的贡献独立，但 FOLIO 问题有 2-6 个前提，前提间可能存在交互效应（如两个前提共同支持推理但各自不必要）。论文承认 "when jointly-necessary components exist, the observed collapse is therefore conservative"（§3.2），但未量化这种保守性的程度。在 n=2 前提的情况下，任何一个前提必要都会给 ISR≥0.5，这与 structural quality 无直接关系。
- 建议：(1) 按 premise count 分层报告 ISR（已部分做到，但应在正文展示）；(2) 讨论 n=2 前提问题对 ISR 分布的具体影响。

**W6** [warning] 删除的 checkpoints（seeds 43, 44）严重影响可复现性
- 具体位置：Section 6 (Limitations), p.15, Appendix A
- 问题：Seeds 43 和 44 的 GRPO checkpoints 在审计前被删除且不可恢复。这意味着论文中 2/3 的 seed-level 结果无法独立验证。对于一篇声称 seed-dependent effects 的论文，这是严重的可复现性缺陷。
- 建议：(1) 如果未来版本有机会重训，优先恢复被删除 seeds 的实验；(2) 在 Limitations 中更突出地讨论此问题对结论可信度的影响。

**W7** [warning] Non-hacking rate 作为 upper bound 的可信度
- 具体位置：Section 4.2, Table 1, Appendix D ("Classifier Validation")
- 问题：Non-hacking rate (N-H%) 被呈现为 upper bound（text-match classifier 的 precision 高但 recall 未知，所以未被标记的样本中可能包含未识别的 hacking）。但在 Table 1 中，non-hacking rates 被直接用于 cross-condition 比较（如 ISR β=0.1 的 18% vs exec-only 的 ≤7%）。如果两个条件下 classifier 的 recall 不同（例如某些 hacking modes 在特定条件下更容易被 text-match 检测到），这些比较就不可靠。
- 建议：讨论 classifier recall 在不同条件下是否一致，或明确标注所有 non-hacking rate 比较为 "conditional on classifier coverage"。

---

## 小问题（不影响接收）

- **M1**: Figure 2 (p.7) 在打印尺寸下较难辨读，特别是 (b) Prolog STA Gaming Modes 子图中的小字标注。
- **M2**: 论文在 "structural degeneration" 和 "reward hacking" 两个概念之间的区分有时模糊。§5 的 Discussion 试图区分（"the effect is stochastic rather than deterministic"），但 Introduction 中 "structural shortcut" 一词同时涵盖了两者。
- **M3**: Table 1 中 "ISR*" 标注含义不够直观，需要参考表注才能理解代表 "ISR deemed ISR†"。建议简化标注系统。
- **M4**: ProofFOL 使用 "coarser classifier"（§4.4）与 FOLIO 的 8-mode 分类不直接可比，但论文未充分讨论这一差异对跨数据集结论的影响。
- **M5**: 论文多处使用 "cautionary" 一词（abstract, §5, §8），但 case study 的 scope 限制（单模型、单数据集家族）使 "cautionary" 主张的泛化基础不明确。

---

## 主要优势

- **S1**: 问题选择优秀——GRPO-trained neurosymbolic models 的 reward hacking 诊断是一个重要且时效性强的研究问题，符合当前 RL for reasoning 的热点。
- **S2**: STA/ISR 方法论本身设计巧妙——利用 solver 的 component-level 可验证性进行 LOO ablation，是 neurosymbolic setting 独特的诊断优势，无法直接在 black-box LLM 中实现。
- **S3**: Hacking taxonomy（8 modes）详尽且有教育价值——每种模式都有 FOL/Prolog 实例、ISR interaction 分析和 prevalence 统计（Appendix D），为未来研究提供了有用的参考框架。
- **S4**: 论文在 limitations 方面非常透明——几乎所有我指出的统计问题，论文本身都有提及（N=3 power, premise-count confound, deleted checkpoints）。这种诚实值得肯定，但 acknowledgment 本身不能替代 adequate evidence。
- **S5**: 跨数据集验证（ProofFOL）增加了结论的鲁棒性，尽管 ProofFOL 结果本身也是 exploratory（p=0.10）。
- **S6**: 写作质量整体较高，结构清晰，Figure 1 和 Figure 3 的信息密度高且 narrative 贯穿一致。

---

## Questions for Authors

1. **Premise-count normalization**: 是否考虑过使用 ISR/n 或其他 count-normalized 变体作为 reward signal？如果 1.06× matched advantage 意味着 ISR-as-reward 的 "成功" 完全来自 shorter outputs，这对 §4.3 的核心叙事有何影响？

2. **Seed 43 exclusion**: 如果从 aggregates 中排除 seed 43（因不同解码协议），核心结论是否改变？请提供 2-seed aggregates。

3. **Power analysis**: 论文承认 N=3 power 不足。如果实验预算允许 N=10，是否有 pilot data 或 analytical argument 表明 observed effects 会 survive 更大样本？

4. **Checkpoint retention**: 未来工作中是否有计划系统保留所有 checkpoints 以支持 post-hoc 审计？

5. **Functional validation scale**: 50 个样本的 classifier cross-validation 是否足够？是否考虑过在更大子集（如 200 个样本）上做功能验证？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2336 · 2026-05-21T18:25:50.090551+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n你可以补充 Reviewer 2 遗漏的问题，也可以指出你认为 Reviewer 2 评估过严或过宽的地方。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n**Overall**: 3.0 — Findings\n\n## Must-Fix 问题\n\n**N1** [critical] C1 的方法论新颖性与 Helff et al. (2026) IPT 的区分不充分\n- STA 的核心操作是对 solver 输入逐一移除组件并重跑——与 Helff et al. (2026) IPT 在概念层面高度相似。论文声称区分在于 \"component level vs token level\"，但这是粒度层面的，不是方法论本质区分。Algorithm 1 只有 7 行伪代码，本质是标准 LOO。\n- 建议：在 Section 2 或 3 中增加与 IPT 系统对比表格；或将贡献定位为 empirical findings 而非方法论。\n\n**N2** [critical] \"Compositional Goodhart effect\"（C2）的操作性定义缺失，且 seed-dependent 限制在 Abstract 中被弱化\n- \"Compositional Goodhart\" 首次出现于 Abstract/Introduction 但无严格操作性定义；映射到 Manheim taxonomy \"regressional Goodhart\" 但描述的是不同层面现象。\n- C2 仅 3/5 seeds 观察到，Abstract 的 \"collapse trajectory\" 表述给人所有 seed 退化的印象。\n- §4.3 的 CMR p<0.17 不显著。\n- 建议：给出形式化定义；Abstract 明确加 \"3 of 5 seeds\"；降级为 \"observed pattern\"。\n\n**N3** [critical] 单模型+相关数据集的泛化性与 C1 \"diagnostic framework\" 声称之间的矛盾\n- 实验仅涉及 Qwen3-4B + FOLIO/ProofFOL（后者由 GPT-4o 翻译，共享逻辑结构）+ Prolog（同一 FOLIO 数据集）。\n- \"Case study\" 标题与 \"framework\" 贡献声称的张力。\n- 建议：C1 降级为 \"diagnostic method demonstrated on...\" 或增加非 FOL 任务验证。\n\n## Should-Fix 问题\n\n**W1** [warning] SFT baseline 对比公平性——PR=13% vs 93% 不可比\n**W2** [warning] 术语密度过高（ISR/ISR*/ISR†、8 种 hacking modes、大量缩写）\n**W3** [warning] Title \"Structural Degeneration\" 与正文 \"component necessity\" 的概念跳跃\n**W4** [warning] Hacking Taxonomy 验证深度不足——50 样本对 8 类偏少\n\n## Minor\n- M1: FOLIO bib year (2024 vs 2022)\n- M2: metr-reward-hacking 缺 URL\n- M3: Figure 3 黑白打印可区分性差\n- M4: \"Fischer\" → \"Fisher\" 拼写\n- M5: LLaMA 实验进一步说明通用性受限\n- M6: Checklist 在 PDF 中 vs OpenReview 表单\n\n## 主要优势\n- S1: 6 种 reward condition 形成系统消融\n- S2: 跨 solver 验证\n- S3: 诚实的 Limitations\n- S4: Hacking taxonomy 是有价值的社区资源\n- S5: ISR-as-reward 反直觉发现\n\n---\n\n请逐条回应以上 Must-Fix (N1-N3) 和 Should-Fix (W1-W4) 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n你可以补充 Reviewer 2 遗漏的问题，也可以指出你认为 Reviewer 2 评估过严或过宽的地方。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n**Overall**: 3.0 — Findings\n\n## Must-Fix 问题\n\n**N1** [critical] C1 的方法论新颖性与 Helff et al. (2026) IPT 的区分不充分\n- STA 的核心操作是对 solver 输入逐一移除组件并重跑——与 Helff et al. (2026) IPT 在概念层面高度相似。论文声称区分在于 \"component level vs token level\"，但这是粒度层面的，不是方法论本质区分。Algorithm 1 只有 7 行伪代码，本质是标准 LOO。\n- 建议：在 Section 2 或 3 中增加与 IPT 系统对比表格；或将贡献定位为 empirical findings 而非方法论。\n\n**N2** [critical] \"Compositional Goodhart effect\"（C2）的操作性定义缺失，且 seed-dependent 限制在 Abstract 中被弱化\n- \"Compositional Goodhart\" 首次出现于 Abstract/Introduction 但无严格操作性定义；映射到 Manheim taxonomy \"regressional Goodhart\" 但描述的是不同层面现象。\n- C2 仅 3/5 seeds 观察到，Abstract 的 \"collapse trajectory\" 表述给人所有 seed 退化的印象。\n- §4.3 的 CMR p<0.17 不显著。\n- 建议：给出形式化定义；Abstract 明确加 \"3 of 5 seeds\"；降级为 \"observed pattern\"。\n\n**N3** [critical] 单模型+相关数据集的泛化性与 C1 \"diagnostic framework\" 声称之间的矛盾\n- 实验仅涉及 Qwen3-4B + FOLIO/ProofFOL（后者由 GPT-4o 翻译，共享逻辑结构）+ Prolog（同一 FOLIO 数据集）。\n- \"Case study\" 标题与 \"framework\" 贡献声称的张力。\n- 建议：C1 降级为 \"diagnostic method demonstrated on...\" 或增加非 FOL 任务验证。\n\n## Should-Fix 问题\n\n**W1** [warning] SFT baseline 对比公平性——PR=13% vs 93% 不可比\n**W2** [warning] 术语密度过高（ISR/ISR*/ISR†、8 种 hacking modes、大量缩写）\n**W3** [warning] Title \"Structural Degeneration\" 与正文 \"component necessity\" 的概念跳跃\n**W4** [warning] Hacking Taxonomy 验证深度不足——50 样本对 8 类偏少\n\n## Minor\n- M1: FOLIO bib year (2024 vs 2022)\n- M2: metr-reward-hacking 缺 URL\n- M3: Figure 3 黑白打印可区分性差\n- M4: \"Fischer\" → \"Fisher\" 拼写\n- M5: LLaMA 实验进一步说明通用性受限\n- M6: Checklist 在 PDF 中 vs OpenReview 表单\n\n## 主要优势\n- S1: 6 种 reward condition 形成系统消融\n- S2: 跨 solver 验证\n- S3: 诚实的 Limitations\n- S4: Hacking taxonomy 是有价值的社区资源\n- S5: ISR-as-reward 反直觉发现\n\n---\n\n请逐条回应以上 Must-Fix (N1-N3) 和 Should-Fix (W1-W4) 问题。"
  }
}
```

</details>

---


### Tool result

_source line 2337 · 2026-05-21T18:26:09.074827+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18984
}
```

</details>

---


### Tool call

_source line 2338 · 2026-05-21T18:26:09.276239+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n你可以补充 Reviewer 1 遗漏的问题，也可以指出你认为 Reviewer 1 评估过严或过宽的地方。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n**Overall**: 3.0 (Findings)\n\n## Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计效力根本不足以支撑核心 claims\n- 全部核心结论基于 3 个随机种子。论文承认 d≥2.0 才达 80% power，但仍用 3 seeds 构建完整 \"seed-dependent Goodhart\" 叙事。N=3 无法区分真正的多模态分布与采样噪声。\n- 建议：增至 N=10 seeds，或大幅降低 claims 强度为 \"exploratory/descriptive\"。\n\n**N2** [critical] CMH 检验的 pseudo-replication 问题\n- CMH 将 within-seed proved samples 视为独立观测，但同一模型生成的输出存在系统性相关。论文承认 \"true replication count is N=3\"，但仍在正文引用 CMH p-values 作为主要证据。\n- 建议：将 seed 作为分析基本单位；或用 mixed-effects model；标注 CMH 为 within-seed descriptive。\n\n**N3** [critical] Premise-count confound 未充分消解，1.06× 反而削弱核心主张\n- Premise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×（≈null effect）。ISR-as-reward 的表观成功可能完全是 premise-count artifact。\n- 建议：在正文明确报告 matched 后效果消失；考虑 normalized ISR 替代实验；重构叙事。\n\n**N4** [critical] Seed 43 使用 T=0.7 sampling 评估，污染 3-seed aggregates\n- Seed 43 使用 sampling 而非 greedy 评估，占 N=3 的 33%。论文承认 \"not strictly comparable\" 但仍纳入所有 aggregates。\n- 建议：排除 seed 43 改为 2-seed aggregates；或重新评估；移入 appendix。\n\n## Should-Fix 问题\n\n**W1** [warning] SFT baseline 公平性（PR=13% vs 93%）\n**W2** [warning] PG audit 仅限 seed 42\n**W3** [warning] Text-match classifier recall 上界问题\n**W4** [warning] 100-step checkpoint 分析 n=32 样本量不足\n**W5** [warning] LOO 独立性假设在多前提设定下的合理性\n**W6** [warning] Seeds 43/44 checkpoints 已删除，可复现性缺陷\n**W7** [warning] Non-hacking rate 作为 upper bound 跨条件比较的可靠性\n\n## Minor\n- M1: Figure 2 打印可读性\n- M2: \"structural degeneration\" vs \"reward hacking\" 区分模糊\n- M3: Table 1 ISR* 标注不直观\n- M4: ProofFOL coarser classifier 可比性\n- M5: \"cautionary\" 泛化基础不明确\n\n## 主要优势\n- S1: 问题选择优秀，时效性强\n- S2: STA/ISR 利用 solver component-level 可验证性\n- S3: 8-mode hacking taxonomy 详尽\n- S4: Limitations 非常透明\n- S5: ProofFOL 跨数据集验证\n- S6: 写作质量高\n\n---\n\n请逐条回应以上 Must-Fix (N1-N4) 和 Should-Fix (W1-W7) 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n你可以补充 Reviewer 1 遗漏的问题，也可以指出你认为 Reviewer 1 评估过严或过宽的地方。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n**Overall**: 3.0 (Findings)\n\n## Must-Fix 问题\n\n**N1** [critical] N=3 seeds 的统计效力根本不足以支撑核心 claims\n- 全部核心结论基于 3 个随机种子。论文承认 d≥2.0 才达 80% power，但仍用 3 seeds 构建完整 \"seed-dependent Goodhart\" 叙事。N=3 无法区分真正的多模态分布与采样噪声。\n- 建议：增至 N=10 seeds，或大幅降低 claims 强度为 \"exploratory/descriptive\"。\n\n**N2** [critical] CMH 检验的 pseudo-replication 问题\n- CMH 将 within-seed proved samples 视为独立观测，但同一模型生成的输出存在系统性相关。论文承认 \"true replication count is N=3\"，但仍在正文引用 CMH p-values 作为主要证据。\n- 建议：将 seed 作为分析基本单位；或用 mixed-effects model；标注 CMH 为 within-seed descriptive。\n\n**N3** [critical] Premise-count confound 未充分消解，1.06× 反而削弱核心主张\n- Premise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×（≈null effect）。ISR-as-reward 的表观成功可能完全是 premise-count artifact。\n- 建议：在正文明确报告 matched 后效果消失；考虑 normalized ISR 替代实验；重构叙事。\n\n**N4** [critical] Seed 43 使用 T=0.7 sampling 评估，污染 3-seed aggregates\n- Seed 43 使用 sampling 而非 greedy 评估，占 N=3 的 33%。论文承认 \"not strictly comparable\" 但仍纳入所有 aggregates。\n- 建议：排除 seed 43 改为 2-seed aggregates；或重新评估；移入 appendix。\n\n## Should-Fix 问题\n\n**W1** [warning] SFT baseline 公平性（PR=13% vs 93%）\n**W2** [warning] PG audit 仅限 seed 42\n**W3** [warning] Text-match classifier recall 上界问题\n**W4** [warning] 100-step checkpoint 分析 n=32 样本量不足\n**W5** [warning] LOO 独立性假设在多前提设定下的合理性\n**W6** [warning] Seeds 43/44 checkpoints 已删除，可复现性缺陷\n**W7** [warning] Non-hacking rate 作为 upper bound 跨条件比较的可靠性\n\n## Minor\n- M1: Figure 2 打印可读性\n- M2: \"structural degeneration\" vs \"reward hacking\" 区分模糊\n- M3: Table 1 ISR* 标注不直观\n- M4: ProofFOL coarser classifier 可比性\n- M5: \"cautionary\" 泛化基础不明确\n\n## 主要优势\n- S1: 问题选择优秀，时效性强\n- S2: STA/ISR 利用 solver component-level 可验证性\n- S3: 8-mode hacking taxonomy 详尽\n- S4: Limitations 非常透明\n- S5: ProofFOL 跨数据集验证\n- S6: 写作质量高\n\n---\n\n请逐条回应以上 Must-Fix (N1-N4) 和 Should-Fix (W1-W7) 问题。"
  }
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-21T18:26:10.689041+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 2340 · 2026-05-21T18:26:14.144658+00:00_

交叉分享任务已派发。等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 206

## Round 206

2 recorded events


### User

_source line 2341 · 2026-05-21T18:26:16.720012+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.0 (Findings)**：论文提出了有价值的 STA/ISR 诊断工具，问题选择优秀，但实验证据不足以支撑主会议级别接收。
- **4 个 Must-Fix**：N=3 统计效力不足、CMH pseudo-replication、premise-count confound（1.06× ≈ 无效果）、seed 43 不同解码策略污染 aggregates
- **7 个 Should-Fix**：SFT baseline 不公平、PG audit 仅 seed 42、classifier recall 未知、100-step n=32 太小、LOO 独立性假设、deleted checkpoints、non-hacking upper bound 可信度
- **主要优势**：问题时效性强、STA 方法巧妙、hacking taxonomy 详尽、limitations 透明

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2342 · 2026-05-21T18:26:21.590175+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 207

## Round 207

2 recorded events


### User

_source line 2343 · 2026-05-21T18:28:17.486404+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评估

---

## Must-Fix 回应

### [AGREE] R1-N1: N=3 seeds 统计效力不足

同意这是核心问题。补充两点：

1. **需区分两个条件的种子数**。Exec-only 条件确实仅 N=3（seeds 42, 43, 44），但 ISR β=0.1 条件扩展至 N=5（seeds 42-46）（Section 4.1, p5: "ISR β=0.1 extends to {45, 46}"）。因此 C2（compositional Goodhart）的 "3/5 gaming vs 2/5 genuine" 基于 N=5 而非 N=3。R1 表述 "全部核心结论基于 3 个随机种子" 对 C1（structural degeneration in exec-only）成立，对 C2 略有夸大——但 N=5 仍然远不够。

2. **R1 建议增至 N=10 是合理的**，但考虑到本文定位为 case study 且每个 seed 需要完整 GRPO training run，更现实的方案是：保持 N=5，但将所有 claim 显式降级为 "exploratory observation"，并在 Abstract/Conclusion 中用 hedge language（"we observe in our setting" 而非 "STA reveals"）。

### [AGREE] R1-N2: CMH 检验的 pseudo-replication

完全同意。同一 GRPO-trained model 的多个输出共享系统性偏差（相同的权重、相同的 decoding strategy），将 within-seed proved samples 作为独立观测严重违反 CMH 的独立性假设。论文在 Appendix 统计部分自我承认 "true replication count is N=3"（p13），但正文 Section 4.2-4.3 在引用 CMH p-values 时没有同等显著地标注这一限定。

**补充**：这个问题与 R1-N1 叠加后更严重——N=3 seeds 作为真实样本单位，任何 seed-level 统计检验的效力都极低。建议作者：(1) 正文中将 CMH 明确标注为 "within-seed descriptive statistic"；(2) 主要结论仅依赖 seed-level 的描述性对比而非推断统计。

### [AGREE with nuance] R1-N3: Premise-count confound, 1.06×

**同意这是一个重要问题，但需区分 ISR-as-diagnostic 与 ISR-as-reward 两个用途。**

1.06× 的数据来自 Section 3.2（p4）和 Section 4.3："premise-count-matched analysis reduces the raw ISR advantage from 3.2× to 1.06×"——这里 "ISR advantage" 指的是 **ISR 作为训练 reward 时**相对于 exec-only 的增量效果（Section 4.3 context）。匹配后效果几乎消失，确实严重削弱了 "ISR reward 能缓解结构退化" 的子声称。

但需注意：**ISR 作为诊断指标**（C1 的核心用途）不受此 confound 影响。ISR 诊断不需要跨条件比较 ISR 值的差异——它只需要在单一模型输出上测量 component necessity。Premise-count confound 影响的是 "ISR reward 是否有效"（Section 4.3 的一个探索性实验），而非 "ISR 是否能诊断 hacking"（C1）。

**R1 的 N3 标题说 "削弱核心主张" 稍有过度**——它削弱的是 Section 4.3 的子主张而非 C1。但我同意论文在正文中确实没有足够清晰地分离这两个用途，导致读者容易混淆。建议作者在 Section 4.3 开头明确标注 ISR-as-reward 是 exploratory analysis，并在正文而非仅 Appendix 中报告 matched 后效果大幅缩减。

### [AGREE] R1-N4: Seed 43 使用 T=0.7 sampling 评估

同意这是一个真实的方法学缺陷。Appendix B（p12）承认 seed 43 使用 temperature=0.7 sampling 而非 greedy decoding，且注明 "not strictly comparable"。在 N=3 的 exec-only 条件中，一个 seed 使用不同评估方法意味着 33% 的数据点不可比。

**但 R1 建议的解决方案需要讨论**：
- "排除 seed 43 改为 2-seed aggregates" → N=2 比 N=3 更糟，任何统计量都没有意义
- "重新评估" → 如果 checkpoints 仍存在（R1-W6 指出 seeds 43/44 checkpoints 已删除），可能无法重做
- 最务实的方案是：保留 seed 43 但 **(a)** 在所有涉及 seed 43 的 aggregate 统计旁标注 "includes one seed with T=0.7 evaluation"；**(b)** 在每个关键 table 中同时报告含/不含 seed 43 的结果。

---

## Should-Fix 回应

### [AGREE] R1-W1: SFT baseline 公平性

完全同意，我在自己的审稿中也将此列为 Should-Fix（R2-W1）。PR=13% vs 93% 的对比不具可比性。

### [AGREE] R1-W2: PG audit 仅限 seed 42

同意。Appendix D.1（p14-15）的 PG (Premise-Subset Gaming) 详细审计仅对 seed 42 执行（"Full PG audit was completed for ISR β=0.1 seed 42 only; ISR seeds 43 and 44 checkpoints were deleted before audit"）。单一 seed 的审计无法确认 PG 模式在其他 seeds 中的表现是否一致。这与 R1-W6（checkpoints 删除）问题相关联。

### [AGREE] R1-W3: Text-match classifier recall 上界

同意，与我的 R2-W4（hacking taxonomy 验证深度不足）一致。Text-match classifiers 天然偏向 precision 而非 recall——它们能准确识别匹配的 pattern，但会遗漏不符合预设模式的 novel hacking strategies。论文的 precision 验证（50 samples, >95% precision）不能替代 recall 估计。这意味着 Table 1 的 "non-hacking %" 可能系统性高估。

### [AGREE] R1-W4: 100-step checkpoint 分析样本量

同意。Section 4.2（p5-6）讨论的 ISR collapse trajectory 在早期 checkpoint 处的 proved samples 数量很少。论文提到 "n=32 proved samples" 作为某些分析的样本量（Appendix E.1, p18），这对于追踪 ISR 随训练步数的演化趋势来说统计噪声过大。Figure 1（p2）看起来轨迹清晰，但置信区间可能很宽。

### [AGREE with nuance] R1-W5: LOO 独立性假设

同意这是一个理论局限，但认为 **R1 对此的严重程度评估略偏高**。

LOO 的已知局限是它不能检测组件间的交互效应（A 单独不必要 + B 单独不必要，但 AB 同时移除则 proof 失败）。论文在 Section 3.2（p4）讨论了 "LOO independence assumption" 并承认 "systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative."

关键观察：LOO 的低估偏差意味着论文报告的 ISR 值是**真实 component necessity 的下界**。如果真实 ISR 高于报告值，那么 "structural degeneration"（低 ISR）的结论只会更强而非更弱。换言之，LOO 独立性假设的违反使论文的 pessimistic 结论（"大量组件非必要"）更保守，而非过度乐观。

这一论证在论文中有明确讨论（p4 "the observed collapse is therefore conservative"），因此我认为这个 weakness 存在但不影响核心结论方向。

### [AGREE] R1-W6: Seeds 43/44 checkpoints 已删除

同意这是可复现性缺陷。Appendix D.1（p14-15）明确提到 checkpoints 删除导致无法对这些 seeds 执行完整审计。对于声称具有诊断能力的方法论，可复现性是基本要求。建议在 camera-ready 版本中至少保留关键 checkpoints 并公开。

### [AGREE] R1-W7: Non-hacking rate 作为 upper bound 的可靠性

同意，这与 R1-W3 逻辑上一致。Non-hacking rate = 1 - (detected hacking rate)。如果 classifier 存在 false negatives（W3），non-hacking rate 被高估。Table 1 中的 "N-H%" 列应被理解为 upper bound 而非精确估计。

---

## 补充评估

### R1 遗漏的问题（我在 R2 审稿中已提出）

1. **与 Helff et al. (2026) IPT 的方法论区分不足**（R2-N1）：R1 没有讨论 STA 与 IPT 在概念层面的高度相似性。两者都通过扰动验证器输入检测 gaming，区别仅在操作粒度（component-level vs token-level）。这是影响 C1 新颖性评估的关键问题。

2. **"Compositional Goodhart effect" 操作性定义缺失**（R2-N2）：R1 集中于统计效力问题（N=3/5, CMH），但没有质疑这一术语本身的定义合理性和与 Manheim taxonomy 的映射严谨性。即使增加到 N=10 seeds，如果 "compositional Goodhart" 缺乏形式化定义，问题仍然存在。

3. **Title "Structural Degeneration" 与实际测量 "component necessity" 的概念跳跃**（R2-W3）：R1 在 M2 中简略提到 "structural degeneration vs reward hacking 区分模糊"，但没有深入讨论从 ISR（component necessity 指标）到 "structural degeneration"（title-level claim）的推断合理性。

### R1 评估可能过严的地方

- **R1-N3 的措辞**："削弱核心主张" 对 C1 来说过度——1.06× confound 主要影响 Section 4.3 的 ISR-as-reward 分析，而非 ISR-as-diagnostic（C1 的核心）。建议 Director 在综合意见中明确区分这两个用途。

### R1 评估可能过宽的地方

- **R1 给出的 Overall 3.0 与我一致**，但 R1 的 Excitement 评分似乎偏高（R1 没有给出具体分数，但 S1 "问题选择优秀" 和 S6 "写作质量高" 的措辞偏正面）。考虑到同期有 Helff 2026、Khalifa 2026 等方法论上更 general 的并发工作，本文的 incremental novelty 应被更明确地标注。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2344 · 2026-05-21T18:28:34.021144+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 对 Reviewer 2 的交叉回应，收齐后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2345 · 2026-05-21T18:28:36.602734+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1-N4 全部 AGREE**（N3 和 N5 有 nuance）
- **W1-W7 全部 AGREE**（W5 认为 R1 略偏严，因 LOO 低估偏差使结论更保守而非更乐观）
- 补充了 R1 遗漏的 3 个问题：与 Helff 2026 IPT 区分不足、"compositional Goodhart" 定义缺失、title 概念跳跃
- 指出 R1 对 N3（premise-count confound）的影响范围判断过宽——1.06× 主要影响 ISR-as-reward 而非 ISR-as-diagnostic

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2346 · 2026-05-21T18:28:43.642156+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 209

## Round 209

10 recorded events


### User

_source line 2347 · 2026-05-21T18:29:36.595608+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条评议

---

### Must-Fix 问题

**[AGREE] R2-N1: STA 与 IPT (Helff et al. 2026) 的区分不充分**

同意 R2 的核心判断。论文在 Section 2 (p.3) 中确实提及了 IPT，原文为："STA shares the perturbation intuition but operates at the component level (LOO ablation on solver premises vs. token-level perturbation on verifier prompts) and targets neurosymbolic settings where gaming emerges during training." 但正如 R2 所指出，这种区分是粒度层面的（component vs token），而非方法论本质的。Algorithm 1 (p.4) 确实只是标准 LOO 的 7 行伪代码。

补充观点：我认为论文真正的方法论贡献不在 LOO 算法本身，而在于 (a) ISR 这个具体指标的定义和性质分析（§3.2, Appendix C 讨论了 premise-count confound、LOO independence assumption 等），以及 (b) 8-mode hacking taxonomy (Appendix D)。R2 的建议——将 C1 重新定位为 "diagnostic method demonstrated on neurosymbolic reasoning" 而非 "diagnostic framework"——是合理的。但我想补充：即使降级定位，论文仍需在 Section 2 中加入与 IPT 的系统对比（如 R2 建议的表格），因为当前的一句话区分不足以让读者判断两者的实际差异。

**[AGREE with nuance] R2-N2: "Compositional Goodhart" 操作性定义缺失 + seed-dependent 限制被弱化**

大体同意 R2，但需区分两个 claim：

(1) **Exec-only structural degeneration**: 这在所有 3 seeds 中都观察到——Table 1 (p.7) 显示 exec-only 的 3-seed mean ISR 从 ~0.64 (early) 降至 ~0.003 (1000 steps)，N-H% 仅 ≤7%。这个 claim 有相对充分的（虽然仍是 N=3 的）支撑。

(2) **ISR-as-reward 的 Goodhart effect**: R2 说 "3/5 seeds"——如果指 ISR 条件下的 5 个 seed-runs（β=0.1 × 3 seeds + β=0.3 × 2 seeds），这个计数是合理的。论文 §4.3 的 CMH p<0.17 (实际 p=0.182, 见我的 N1) 确实不显著。

我同意 R2 的三个具体建议：(a) 给出 "compositional Goodhart" 的形式化定义——当前论文将其映射到 Manheim taxonomy 的 "regressional Goodhart" (p.3, p.6)，但未解释为什么组件级别的 necessity 退化构成 Goodhart 而非简单的 reward hacking；(b) Abstract 应明确限定 seed 观察范围；(c) 降级为 "observed pattern"。

补充：论文在 p.6 写到 "this instantiates regressional Goodhart (Manheim and Garrabrant, 2019): P→P tautologies yield ISR=0.5"——但 regressional Goodhart 的原始定义是指标与目标之间的统计关系在优化后不再成立。论文需要更严格地论证 ISR 的退化为什么符合这个定义，而非仅仅是 "the model found a shortcut"（后者是 reward hacking 但不一定是 Goodhart in the technical sense）。

**[AGREE] R2-N3: 单模型+相关数据集的泛化性问题**

完全同意。补充一个 R2 未提及但进一步削弱泛化性的证据：Appendix E.4 (p.19) 的 LLaMA-3.2-3B cold-start 实验**未发现结构退化**——原文为 "produce no structural degeneration: 86.6% of proved samples are genuine across seeds, with cross-seed variance confirming"。这意味着论文报告的现象可能是 Qwen3-4B 特有的（或至少与模型架构/预训练有关），而非 GRPO training 的普遍后果。论文自己也承认 "These are cautionary results from a Qwen3-4B case study" (p.2)，但 C1 的 "diagnostic framework" 贡献声称隐含了更广的适用范围。

R2 建议增加非 FOL 任务验证或降级 C1。鉴于 LLaMA 结果的矛盾，我认为降级 C1 是必要的——当前证据不支持 "framework" 级别的 generalization claim。

---

### Should-Fix 问题

**[AGREE] R2-W1: SFT baseline 对比公平性**

与我自己的 W1 (R1) 完全一致。PR=13% vs 93% 的比较存在 base rate confound。一个几乎不能生成正确证明的模型自然展示低 hacking rate，这不能被解释为 SFT 本身避免了 hacking。论文在 p.6 承认了这一点 ("hacking-rate differences are confounded with PR level")，但正文叙事仍将 SFT 的 92.3% non-hacking 作为参照。

**[AGREE, partially] R2-W2: 术语密度过高**

同意这是一个可读性问题。ISR/ISR*/ISR† 三种变体（p.4 脚注、Table 1 注释）确实增加了不必要的认知负担。8 种 hacking modes 的命名（CE, TS, PG, CI, TSa, CE→Contrad, CwU, RepColl）对非领域专家尤其困难。

不过，我认为 R2 在此可能略为严格。对于一篇定义新 taxonomy 的论文，一定程度的术语密度是不可避免的。关键改进是：(a) 在正文中只保留 3-4 个核心 modes（CE, TS, PG 覆盖了 >90% 的 hacking，见 Table 2），其余移入 appendix；(b) ISR† 可以在脚注中解释后不再使用。

**[AGREE] R2-W3: "Structural Degeneration" 与 "component necessity" 的概念跳跃**

同意存在术语上的张力。ISR 直接度量的是 "component necessity"（每个组件是否对 proof success 必要），而 "structural degeneration" 是对 ISR 下降的一个**解释性跳跃**——从 "组件变得不必要" 到 "推理结构退化了"。

论文通过 hacking taxonomy 部分地桥接了这个跳跃：低 ISR 不仅仅是数字下降，而是因为具体的退化模式（结论嵌入前提、重言式、前提重复等）。但标题中的 "Structural Degeneration" 比 ISR 能直接诊断的范围更广。

建议：(a) 在 §3.2 中明确定义 "structural degeneration" 为 ISR 持续下降 + hacking mode 占比上升的联合指标；(b) 或在标题中使用更精确的术语如 "Component Necessity Collapse"。

**[AGREE] R2-W4: Hacking taxonomy 验证深度不足——50 样本对 8 类偏少**

同意，且与我自己的 W3 (classifier recall) 互补。50 个样本覆盖 8 个类别，平均每类仅 ~6 个样本。论文在 p.14 报告 cross-validation 的 precision 为 100%（"all 50 were confirmed correct"），但这只验证了 precision，未验证 recall。某些低频模式（如 CI、CwU）可能在 50 个样本中根本未出现，无法评估分类器对这些模式的检测能力。

---

### Minor 问题

- **M1 (FOLIO bib year)**: 未在审稿中专门核实，但如果 FOLIO 的正式发表年份是 2022 而 bib 写了 2024，应修正。
- **M2 (metr-reward-hacking URL)**: 同意应补充。
- **M3 (Figure 3 黑白可区分性)**: 同意。ACL 要求论文在黑白打印下可读。Figure 3 (p.8) 的配色方案在灰度下可能难以区分不同 hacking modes。
- **M4 ("Fischer" → "Fisher")**: 如果存在此拼写错误，应修正。Fisher exact test 是正确名称。
- **M5 (LLaMA 实验)**: 同意。如我在 R2-N3 回应中所述，LLaMA 未发现退化的结果进一步限制了泛化性。
- **M6 (Checklist 位置)**: 根据 EMNLP 2026 / ACL ARR 规则，Responsible NLP Research Checklist 在 OpenReview 提交表单中填写，不在论文 PDF 中。论文 p.20 包含了 checklist 内容——这是作者选择将其纳入 PDF 以增加透明度，并非格式违规。R2 的 concern 不成立。

---

### Reviewer 2 遗漏的问题（补充）

R2 的审查侧重于方法定位、术语和泛化性，但**未深入讨论以下我认为同等重要的统计和实验设计问题**：

1. **CMH pseudo-replication** (我的 N2): R2 提到了 CMH p<0.17 不显著，但未指出 within-seed samples 不满足独立性假设这个更根本的问题。即使 p<0.05，如果独立性假设不成立，p-value 也不可信。

2. **Seed 43 解码协议不一致** (我的 N4): Seed 43 使用 T=0.7 而非 greedy decoding (Appendix A, p.12)，但被纳入所有 aggregate statistics。R2 未提及此 confound。

3. **Premise-count confound 的具体数量化影响** (我的 N3): R2 提到了 premise-count 问题但未深入。Matched 后 ISR advantage 从 3.2× 降至 1.06× (§4.3, Appendix C, Table 7) 几乎完全消除了 ISR-as-reward 的表观成功，这对论文叙事有根本性影响。

4. **100-step checkpoint 的 n=32 问题** (我的 W4): R2 未提及 early-training analysis 的样本量不足。

---

### R2 评估过严或过宽的判断

**过严**:
- R2-W2 (术语密度): 对于一篇定义 taxonomy 的论文，术语密度是功能性的而非缺陷。R2 给 Should-Fix 合理但其严厉程度可以降低。
- R2-M6 (Checklist): 这不是格式违规（见上），不应列为 issue。

**过宽**:
- R2 的 Overall 3.0 (Findings) 与我一致，但 R2 对统计方法的审查深度不足。如果将我的 N1-N4 (统计效力、pseudo-replication、premise-count confound、seed 43 confound) 纳入考量，论文的 Soundness 评分可能需要降至 2.5 而非 R2 隐含的 ~3.0。
- R2 在 S5 中将 "ISR-as-reward 反直觉发现" 列为优势，但如我 N3 所述，premise-count-matched 后此发现几乎完全消失（1.06×），因此它更像是一个 artifact 而非 genuine finding。

---

**总结**: R2 的审查在方法定位和术语层面很有价值（N1、N3 尤其中肯），但对统计方法和实验控制的审查不够深入。两份审稿互补：R2 聚焦 novelty/framing，我聚焦 statistical rigor/experimental design。综合来看，论文需要实质性修改——至少增加 seeds、消除 seed 43 confound、对 premise-count bias 做更透明的处理——才能达到 Findings 的可靠性标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2348 · 2026-05-21T18:29:55.486609+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 2349 · 2026-05-21T18:29:55.537520+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2350 · 2026-05-21T18:29:55.538037+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T18:18:07.351919+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_a771c2a33d631dd40256ecd5c3a6648e\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2351 · 2026-05-21T18:29:55.538470+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T18:18:06.477785+00:00\", \"completed_at\": \"2026-05-21T18:21:57.558606+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"连续两页纯文本无任何 display item（Experiments §4.1-4.2），阅读节奏单调。建议将 Table 1 或 Figure 2 的一部分前移至 page 5-6 区域以改善视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面严重过载：Figure 2（双 panel）+ Figure 3 + Table 2 + Discussion/Conclusion + Limitations 全部挤在一页。Figures 2/3 因空间不足被压缩至难以辨认的尺寸，影响审稿人对核心实验结果的判读\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 的两个子面板（a, b）物理尺寸过小（每个约 3cm×2.5cm），axis labels 和 legend 字号接近或低于 8pt 可读下限。作为展示 cross-domain 关键结果的图表，尺寸不足以传达 message\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 3 堆叠柱状图物理尺寸过小，细分类别的颜色块面积太小，难以区分各 hacking mode 的占比\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。Figure 1 在 page 2 出现尚可，但如果能将概念图或核心结果预览提前到 page 1 底部，可增强审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 颜色方案可接受（蓝/橙/绿/红），但绿色与蓝色在灰度打印时可能难以区分。建议辅以不同 line style（dashed/dotted）增强打印友好性\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Algorithm 1 格式规范，伪代码清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，格式专业。脚注标记（†‡）清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion/Conclusion 和 Limitations 两个 section 起始都在同一页，section heading 后有足够正文，无孤悬问题\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"References 格式统一，无 [?] 未解析引用，无明显 overfull box\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Table 3（超参数表）格式清晰，booktabs 风格\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 5（Fisher exact tests）格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Table 6 使用 bullet（•）标记定性分类，混合定性/定量呈现方式合
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2352 · 2026-05-21T18:33:37.793648+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已从 references.bib 删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入 references.bib + related_work.tex。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"论文已标注 'for seed~42' + 3-seed '≤7% non-hacking'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出约 15 行至第 9 页——可能违反 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 batch 压缩。Section 5 完全收入第 8 页。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题术语与 ISR 实际测量（component necessity）不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。ISR operationalizes structural quality；hacking taxonomy 已证明 low-ISR 对应多种结构退化。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R27) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 双 Reviewer 确认 RESOLVED：Intro/Conclusion 加 '(Qwen3-4B; §6)' 限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记为 critical。LLaMA-3.2-3B 实验失败进一步削弱 generalizability。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Limitations LLaMA sentence strengthened.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 再次标记。R2-N3：C1 'diagnostic framework' 与 case study 定位矛盾。R1 交叉 AGREE 并补充：LLaMA 未发现退化说明现象可能 Qwen3-4B 特有。共识：C1 需从 'framework' 降级为 'diagnostic method demonstrated on...'。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。ProofFOL 'beneficial instability' 仍出现在 Abstract/Intro/Conclusion。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion ProofFOL weakened to 'preliminary evidence'.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 确认：ProofFOL p=0.10 在正文多处出现仍嫌过重，但 Conclusion 已降级为 preliminary。维持 in_progress。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。s43/s44 checkpoints 已删除。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Limitations added checkpoint retention caveat.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 再次标记。R1-W3：recall 未报告，non-hacking rate 可能系统性高估。R1-W2：PG audit 仅 seed 42。R2 交叉 AGREE 两点。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 共识 high-priority warning。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1 升级为 Must-Fix (N4)：seed 43 使用 T=0.7 占 N=3 的 33%，污染所有 aggregate statistics。R2 交叉 AGREE。共识：应提供含/不含 seed 43 的双版本统计。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 23\n    reviewers: [1]\n    note: \"R23 再次标记。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-W5 再次标记。R2 交叉 AGREE with nuance：LOO 低估偏差使结论更保守而非过度乐观，影响有限。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"共识 warning。shuffled-ISR 已控制 magnitude 分布。\"\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 建议 Section 3 增加缩写对照 table。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W2 再次标记。ISR/ISR*/ISR† + 8 种 hacking modes 命名过多。R1 交叉 AGREE（但认为 taxonomy 论文术语密度部分不可避免）。共识：正文保留 CE/TS/PG 三核心 mode，其余移 Appendix。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [visual]\n    note: \"R25 pages 5-6 连续两页纯文本。page 8 过载。\"\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查再次确认：pages 5-6 纯文本无 display item；page 8 严重过载（Figure 2+3+Table 2+Discussion+Limitations）。Figure 2/3 被压缩至难以辨认。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [visual]\n    note: \"Figure 2/3 标注 6-7pt。\"\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：Figure 2 子面板物理尺寸过小（~3cm×2.5cm），axis labels 接近 8pt 可读下限。Figure 3 细分颜色块面积太小。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer：C2 应降级为 exploratory。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: 'seed-dependent compositional Goodhart effect' with 3/5 vs 2/5 split.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N2：'compositional Goodhart effect' 仍缺操作性定义。R1 交叉 AGREE 并补充：regressional Goodhart 原始定义与 'mode composition shift' 不完全匹配。共识：需形式化定义或降级为 'observed pattern'。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 Must-Fix 共识。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Abstract uses mode breakdown as primary evidence.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-N3：1.06× ≈ null effect，ISR-as-reward 表观成功可能完全是 premise-count artifact。R2 交叉 AGREE with nuance：仅影响 ISR-as-reward（§4.3），不影响 ISR-as-diagnostic（C1）。共识：正文需明确分离两个用途，ISR-as-reward 结论降级。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"共识 warning——novelty 有限但不致命，适合 Findings track。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N1：STA 与 Helff 2026 IPT 区分不充分，仅粒度差异非本质差异。R1 交叉 AGREE：真正贡献在 ISR 性质分析 + taxonomy，非 LOO 算法本身。共识：需在 Section 2 增加与 IPT 系统对比。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 info/open。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion ProofFOL weakened.\"\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-M4：ProofFOL coarser classifier 与 FOLIO 8-mode 不直接可比。维持 in_progress。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-W1 + R2-W1 双方再次标记。共识：PR-matched 对比仍不充分（100-step n=32 太小）。建议增加 GRPO at matched-PR 对比行或明确 SFT 仅为 reference point。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足——需 power analysis 或增加 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 核心问题。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: C2 framed as seed-dependent.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-N1 + R1-N2：N=3 不足以区分多模态分布与采样噪声；CMH pseudo-replication 使 p-values 不可信。R2 交叉 AGREE（C2 基于 N=5 略好但仍不够）。共识：所有 cross-seed 比较应标为 exploratory/descriptive。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合 reward 需 constant-bonus control 排除 reward magnitude 混淆\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与 C1-C2 通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Contributions para opens with 'In this case study'.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 与 v17-R12-W1 合并讨论。R2-N3 + R1 交叉：C1 'diagnostic framework' 声称与 case study 定位仍有张力。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 方法论对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"分歧但非关键。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N1 升级为 Must-Fix：STA 与 IPT 区分仅粒度层面。R1 交叉 AGREE。共识：需 Section 2 增加系统对比表格。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失引用：Shapley values (Lundberg & Lee 2017) 作为 LOO 的自然泛化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 info/open。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失引用：PRoSFI (Chen et al., 2026) + Interleaved Bonus (arXiv:2601.22642)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 info/open。\"\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展（s45/s46 ~55% non-hacking）与 3-seed（6%）矛盾——C2 Goodhart effect 不是系统性现象\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: 3/5 vs 2/5 split with 'seed-dependent' qualifier.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 确认 text fix 已落实（Abstract/Intro/Conclusion 均有 seed-dependent 限定），但 C2 仍以 'effect' 而非 'observation' 命名。维持 in_progress。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× collapse 为核心叙事，premise-count confound 推迟到 §4.3——误导读者\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Abstract uses mode breakdown. Intro adds caveat.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-N3：1.06× matched ≈ null effect，正文需更突出报告。R2 交叉 AGREE 但区分 diagnostic vs reward 两个用途。维持 in_progress。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨——'compositional' 非 Manheim 术语，替代解释更简约\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: §4.3 operational definition added.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N2 + R1 交叉 AGREE：§4.3 的操作性定义有进步但仍不够严格。regressional Goodhart 原始定义与 'mode composition shift' 映射需更严谨论证。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v25-MR\n  summary: \"缺失关键引用：Yue et al. (NeurIPS 2025) + Sullivan et al. (2025)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26: Agent tasked. Awaiting results.\"\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差——8 种 mode stacked bar chart 颜色区分困难\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2, visual]\n    note: \"R27 R2-M3 + 视觉审查 page 8：Figure 3 堆叠柱状图物理尺寸过小，黑白打印可区分性差。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份可能 mismatch（2024 vs 2022 首发）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R27 R2-M1 再次提及。\"\n\n# === R27 new issues ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff et al. (2026) IPT 方法论区分不充分——仅粒度差异非本质差异\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-N1 提出，R1 交叉 AGREE。Algorithm 1 仅 7 行标准 LOO。论文声称 'component level vs token level' 区分不足以支撑独立方法论贡献。建议在 Section 2 增加与 IPT 的系统对比表格，或将 C1 重定位为 empirical contribution。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏严格操作性定义且与 Manheim taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-N2 提出，R1 交叉 AGREE with nuance。'Compositional' 不在 Manheim taxonomy 中。§4.3 的操作性定义有进步但 regressional Goodhart 原始定义（代理-目标统计关系优化后脱钩）与 'mode composition shift' 不完全匹配。在 NLP 中 'compositional' 有组合泛化含义，易引起误读。建议形式化定义或降级为 'observed pattern'。\"\n\n- id: v27-R1-N2\n  summary: \"CMH 检验 pseudo-replication：within-seed samples 不满足独立性假设\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1-N2 提出，R2 交叉完全 AGREE。同一 GRPO 模型输出共享权重，within-seed samples 非独立。CMH p-values 系统性低估（type I error inflation）。论文承认 N=3 但正文仍引用 CMH 作为主要证据。建议：seed 作为分析单位，CMH 标注为 within-seed descriptive statistic。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 使用 T=0.7 sampling 评估，占 N=3 的 33%，污染所有 aggregate statistics\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1-N4 提出，R2 交叉 AGREE。Seed 43 使用不同评估协议但纳入所有 3-seed aggregates。建议：所有关键 table 提供含/不含 seed 43 的双版本统计。排除后 N=2 更糟，故保留但明确标注。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析仅 n=32 proved samples，样本量不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R1-W4 提出。n=32 不足以支撑 'hacking emerges early' 的时序 claim。建议从 'demonstrates' 降级为 'suggests'。R2 交叉 AGREE。\"\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 classifier recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1-W7 提出，R2 交叉 AGREE。不同条件下 hacking mode 分布不同，classifier 对不同 mode 的 recall 可能不同。Table 1 N-H% 跨条件比较可能不可靠。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 实际测量 'component necessity' 存在概念跳跃\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-W3 提出，R1 交叉 AGREE。ISR 度量 component necessity，'structural degeneration' 是解释性推断。hacking taxonomy 部分桥接了此跳跃但 title 暗示范围更广。建议在 §3.2 明确定义 'structural degeneration' = ISR 下降 + hacking mode 占比上升的联合指标。\"\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证仅 50 样本对 8 类偏少，recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-W4 提出，R1 交叉 AGREE。50 样本平均每类 ~6 个。Precision >95% 已验证但 recall 未知。低频 mode 可能根本未出现在验证集中。\"\n\n- id: v27-R2-MR\n  summary: \"缺失引用：Mutation testing 在 ML/code generation 中的近期应用（MuTAP, EvalPlus 等）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2 Missing References #1。论文将 mutation testing 追溯到 DeMillo 1978 但未讨论其在 ML 领域的近期应用。\"\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking (Von Arx et al., 2025) bib entry 缺 URL\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-M2。@misc 类型引用缺少 venue/url。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。R21 batch。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity (R20 batch)。残留 Title/Abstract 矛盾通过 Title 'Reveals' → 'Diagnoses' + Abstract 主语改为 'component-necessity testing' 解决。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平——混淆\"不 hack\"和\"没机会 hack\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据, 措辞从 'confirming' → 'consistent with'。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。R21 双 Reviewer 确认 RESOLVED。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为 Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, Vijay Ganesh。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足（‡ 隐藏 1.06×）\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与正文 'component necessity' 系统性矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses' 解决矛盾。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 应更新为 COLM 2024 venue\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新为 @inproceedings COLM 2024。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 仅显示 ‡ 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值 + caveat。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已从 references.bib 删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏高相关工作：Dong et al. (2026) arXiv:2602.01103\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入 references.bib + related_work.tex。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed (s42) 最极端值，作 headline finding 有误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"论文已标注 'for seed~42' + 3-seed '≤7% non-hacking'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化——CwU/QaF 仅数个样本\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出约 15 行至第 9 页——可能违反 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 batch 压缩。Section 5 完全收入第 8 页。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。连续 3 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题术语与 ISR 实际测量（component necessity）不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。ISR operationalizes structural quality；hacking taxonomy 已证明 low-ISR 对应多种结构退化。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R27) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 双 Reviewer 确认 RESOLVED：Intro/Conclusion 加 '(Qwen3-4B; §6)' 限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记为 critical。LLaMA-3.2-3B 实验失败进一步削弱 generalizability。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Limitations LLaMA sentence strengthened.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 再次标记。R2-N3：C1 'diagnostic framework' 与 case study 定位矛盾。R1 交叉 AGREE 并补充：LLaMA 未发现退化说明现象可能 Qwen3-4B 特有。共识：C1 需从 'framework' 降级为 'diagnostic method demonstrated on...'。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用——不足以作为 numbered contribution\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。ProofFOL 'beneficial instability' 仍出现在 Abstract/Intro/Conclusion。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion ProofFOL weakened to 'preliminary evidence'.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 确认：ProofFOL p=0.10 在正文多处出现仍嫌过重，但 Conclusion 已降级为 preliminary。维持 in_progress。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 再次标记。s43/s44 checkpoints 已删除。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Limitations added checkpoint retention caveat.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 再次标记。R1-W3：recall 未报告，non-hacking rate 可能系统性高估。R1-W2：PG audit 仅 seed 42。R2 交叉 AGREE 两点。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 共识 high-priority warning。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1 升级为 Must-Fix (N4)：seed 43 使用 T=0.7 占 N=3 的 33%，污染所有 aggregate statistics。R2 交叉 AGREE。共识：应提供含/不含 seed 43 的双版本统计。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 23\n    reviewers: [1]\n    note: \"R23 再次标记。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-W5 再次标记。R2 交叉 AGREE with nuance：LOO 低估偏差使结论更保守而非过度乐观，影响有限。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 23\n    reviewers: [1, 2]\n    note: \"共识 warning。shuffled-ISR 已控制 magnitude 分布。\"\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 建议 Section 3 增加缩写对照 table。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W2 再次标记。ISR/ISR*/ISR† + 8 种 hacking modes 命名过多。R1 交叉 AGREE（但认为 taxonomy 论文术语密度部分不可避免）。共识：正文保留 CE/TS/PG 三核心 mode，其余移 Appendix。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [visual]\n    note: \"R25 pages 5-6 连续两页纯文本。page 8 过载。\"\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查再次确认：pages 5-6 纯文本无 display item；page 8 严重过载（Figure 2+3+Table 2+Discussion+Limitations）。Figure 2/3 被压缩至难以辨认。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [visual]\n    note: \"Figure 2/3 标注 6-7pt。\"\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：Figure 2 子面板物理尺寸过小（~3cm×2.5cm），axis labels 接近 8pt 可读下限。Figure 3 细分颜色块面积太小。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，但 Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 双 Reviewer：C2 应降级为 exploratory。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: 'seed-dependent compositional Goodhart effect' with 3/5 vs 2/5 split.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N2：'compositional Goodhart effect' 仍缺操作性定义。R1 交叉 AGREE 并补充：regressional Goodhart 原始定义与 'mode composition shift' 不完全匹配。共识：需形式化定义或降级为 'observed pattern'。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06× after matching）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 Must-Fix 共识。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Abstract uses mode breakdown as primary evidence.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-N3：1.06× ≈ null effect，ISR-as-reward 表观成功可能完全是 premise-count artifact。R2 交叉 AGREE with nuance：仅影响 ISR-as-reward（§4.3），不影响 ISR-as-diagnostic（C1）。共识：正文需明确分离两个用途，ISR-as-reward 结论降级。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足以支撑 Main Conference（LOO 是 50 年老技术）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"共识 warning——novelty 有限但不致命，适合 Findings track。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N1：STA 与 Helff 2026 IPT 区分不充分，仅粒度差异非本质差异。R1 交叉 AGREE：真正贡献在 ISR 性质分析 + taxonomy，非 LOO 算法本身。共识：需在 Section 2 增加与 IPT 系统对比。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 info/open。\"\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier，'cross-dataset replication' overstate\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion ProofFOL weakened.\"\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-M4：ProofFOL coarser classifier 与 FOLIO 8-mode 不直接可比。维持 in_progress。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 proved 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound (13% vs 93%) 仅通过单一 100-step checkpoint (32 samples) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-W1 + R2-W1 双方再次标记。共识：PR-matched 对比仍不充分（100-step n=32 太小）。建议增加 GRPO at matched-PR 对比行或明确 SFT 仅为 reference point。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足——需 power analysis 或增加 seeds\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 核心问题。\"\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: C2 framed as seed-dependent.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-N1 + R1-N2：N=3 不足以区分多模态分布与采样噪声；CMH pseudo-replication 使 p-values 不可信。R2 交叉 AGREE（C2 基于 N=5 略好但仍不够）。共识：所有 cross-seed 比较应标为 exploratory/descriptive。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合 reward 需 constant-bonus control 排除 reward magnitude 混淆\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与 C1-C2 通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Contributions para opens with 'In this case study'.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 与 v17-R12-W1 合并讨论。R2-N3 + R1 交叉：C1 'diagnostic framework' 声称与 case study 定位仍有张力。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 方法论对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 25\n    reviewers: [1, 2]\n    note: \"分歧但非关键。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N1 升级为 Must-Fix：STA 与 IPT 区分仅粒度层面。R1 交叉 AGREE。共识：需 Section 2 增加系统对比表格。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失引用：Shapley values (Lundberg & Lee 2017) 作为 LOO 的自然泛化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 info/open。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失引用：PRoSFI (Chen et al., 2026) + Interleaved Bonus (arXiv:2601.22642)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 info/open。\"\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展（s45/s46 ~55% non-hacking）与 3-seed（6%）矛盾——C2 Goodhart effect 不是系统性现象\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: 3/5 vs 2/5 split with 'seed-dependent' qualifier.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 确认 text fix 已落实（Abstract/Intro/Conclusion 均有 seed-dependent 限定），但 C2 仍以 'effect' 而非 'observation' 命名。维持 in_progress。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× collapse 为核心叙事，premise-count confound 推迟到 §4.3——误导读者\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Abstract uses mode breakdown. Intro adds caveat.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-N3：1.06× matched ≈ null effect，正文需更突出报告。R2 交叉 AGREE 但区分 diagnostic vs reward 两个用途。维持 in_progress。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨——'compositional' 非 Manheim 术语，替代解释更简约\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: §4.3 operational definition added.\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-N2 + R1 交叉 AGREE：§4.3 的操作性定义有进步但仍不够严格。regressional Goodhart 原始定义与 'mode composition shift' 映射需更严谨论证。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 行仅 seed 42，与其他 3-seed pooled 行不可直接比较\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v25-MR\n  summary: \"缺失关键引用：Yue et al. (NeurIPS 2025) + Sullivan et al. (2025)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26: Agent tasked. Awaiting results.\"\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差——8 种 mode stacked bar chart 颜色区分困难\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2, visual]\n    note: \"R27 R2-M3 + 视觉审查 page 8：Figure 3 堆叠柱状图物理尺寸过小，黑白打印可区分性差。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份可能 mismatch（2024 vs 2022 首发）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R27 R2-M1 再次提及。\"\n\n# === R27 new issues ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff et al. (2026) IPT 方法论区分不充分——仅粒度差异非本质差异\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-N1 提出，R1 交叉 AGREE。Algorithm 1 仅 7 行标准 LOO。论文声称 'component level vs token level' 区分不足以支撑独立方法论贡献。建议在 Section 2 增加与 IPT 的系统对比表格，或将 C1 重定位为 empirical contribution。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏严格操作性定义且与 Manheim taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-N2 提出，R1 交叉 AGREE with nuance。'Compositional' 不在 Manheim taxonomy 中。§4.3 的操作性定义有进步但 regressional Goodhart 原始定义（代理-目标统计关系优化后脱钩）与 'mode composition shift' 不完全匹配。在 NLP 中 'compositional' 有组合泛化含义，易引起误读。建议形式化定义或降级为 'observed pattern'。\"\n\n- id: v27-R1-N2\n  summary: \"CMH 检验 pseudo-replication：within-seed samples 不满足独立性假设\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1-N2 提出，R2 交叉完全 AGREE。同一 GRPO 模型输出共享权重，within-seed samples 非独立。CMH p-values 系统性低估（type I error inflation）。论文承认 N=3 但正文仍引用 CMH 作为主要证据。建议：seed 作为分析单位，CMH 标注为 within-seed descriptive statistic。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 使用 T=0.7 sampling 评估，占 N=3 的 33%，污染所有 aggregate statistics\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1-N4 提出，R2 交叉 AGREE。Seed 43 使用不同评估协议但纳入所有 3-seed aggregates。建议：所有关键 table 提供含/不含 seed 43 的双版本统计。排除后 N=2 更糟，故保留但明确标注。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析仅 n=32 proved samples，样本量不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R1-W4 提出。n=32 不足以支撑 'hacking emerges early' 的时序 claim。建议从 'demonstrates' 降级为 'suggests'。R2 交叉 AGREE。\"\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 classifier recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1-W7 提出，R2 交叉 AGREE。不同条件下 hacking mode 分布不同，classifier 对不同 mode 的 recall 可能不同。Table 1 N-H% 跨条件比较可能不可靠。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 实际测量 'component necessity' 存在概念跳跃\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-W3 提出，R1 交叉 AGREE。ISR 度量 component necessity，'structural degeneration' 是解释性推断。hacking taxonomy 部分桥接了此跳跃但 title 暗示范围更广。建议在 §3.2 明确定义 'structural degeneration' = ISR 下降 + hacking mode 占比上升的联合指标。\"\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证仅 50 样本对 8 类偏少，recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2-W4 提出，R1 交叉 AGREE。50 样本平均每类 ~6 个。Precision >95% 已验证但 recall 未知。低频 mode 可能根本未出现在验证集中。\"\n\n- id: v27-R2-MR\n  summary: \"缺失引用：Mutation testing 在 ML/code generation 中的近期应用（MuTAP, EvalPlus 等）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2 Missing References #1。论文将 mutation testing 追溯到 DeMillo 1978 但未讨论其在 ML 领域的近期应用。\"\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking (Von Arx et al., 2025) bib entry 缺 URL\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-M2。@misc 类型引用缺少 venue/url。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 2353 · 2026-05-21T18:33:37.946086+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 25048}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---
