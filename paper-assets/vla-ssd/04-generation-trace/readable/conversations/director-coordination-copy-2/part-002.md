# Director coordination — Part 2 of 5

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/55/55aa43168feffca83e03.json)

## Round 41

### Tool result

_source line 376 · 2026-05-18T08:50:06.948725+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

Based on the search results, here are the key submission guidelines and author instructions for CoRL 2026:

## Paper Format

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional).

## Review Requirements

Every author with 3 or more submissions must agree to serve as a reviewer. Authors are exempt from the review requirement if they serve as an AC, an SAC, or another organizing chair for CoRL 2026. Submissions that do not meet this reciprocal review requirement may be desk-rejected.

## Rebuttal Process

Papers that receive all reviews in the "reject" range in the initial round will not proceed to the rebuttal phase. Authors of all other papers are invited to submit a 1-page rebuttal in pdf by the rebuttal deadline.

## Required Content

A
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 8152
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-18T08:50:06.949240+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'vla-ssd'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6587
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-18T08:50:11.422118+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors page limit template double blind anonymous"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors page limit template double blind anonymous"
  }
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-18T08:50:12.075337+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-18T08:50:12.376513+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-18T08:50:12.728052+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-18T08:50:16.599514+00:00_

Web search results for query: "CoRL 2026 instruction for authors page limit template double blind anonymous"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Instructions for Authors – Initial Submission","url":"https://corl2022.org/instructions-for-authors/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"Author Information and Submission Instructions - IEEE International Conference on Multimedia and Expo 2026","url":"https://2026.ieeeicme.org/author-information-and-submission-instructions/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"}]

Based on the search results, here's the key information about CoRL 2026 Instructions for Authors regarding page limits, templates, and anonymity requirements:

## Double-Blind Anonymous Submissions

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Page Limit

For the initial submission, papers are limited to 8 pages of content plus unlimited references. For camera-ready versions, the camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional), and this year, an additional page is being allowed to accommodate feedback from 
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 5177
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-18T08:50:16.600040+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# vla-ssd Memory\\n\\n## Llama2Base Action R²: Layer-Specific Reorganization (2026-05-17)\\n\\n**Three-condition action R² (image_mean) reveals VLA training does layer-specific reorganization, not uniform improvement:**\\n\\n- **L1**: llama2base(0.637) ≈ trained(0.633) >> untrained(0.555) — language pretraining already near ceiling at L1\\n- **L2-L9 (action zone)**: U(0.529) < L(0.635) < T(0.646) — VLA training adds incremental improvement\\n- **L21-L31 (late layers)**: L(0.57) > T(0.49) > U(0.47) — VLA training repurposes late layers for action token generation\\n- **Peak migration**: untrained L0 → llama2base L4 → trained L8 — deeper action encoding with more training\\n\\n**Framing implication**: Don't claim simple U&lt;L&lt;T gradient. Claim: VLA training reorganizes action encoding across layers — enhancing mid-layer processing while repurposing late layers for output. This complements attention routing evidence (bookend pattern).\\n\\n## L1 Head Count: 24 Confirmed (2026-05-17)\\n\\nVerified from three independent sources: raw data (full_32layer_trained.json), per-head manual check (>50% threshold), and ablation script (INSTRUCTION_HEADS_24). All agree on 24/32. Table 2 in paper says \\\"25/32\\\" — **needs correction to 24/32**.\\n\\n## 50-demo Ablation: Capacity Trade-Off Confirmed with Specificity (2026-05-17)\\n\\n**Critical path result — N3 reviewer concern resolved:**\\n\\n50-demo rerun eliminates 5-demo underfitting confound (N_train/params: 0.005 → 0.05, baseline R²: 0.256 → 0.557).\\n\\n| Layer | baseline | control8 | all24 | all32 |\\n|-------|----------|----------|-------|-------|\\n| L1 | 0.557 | 0.573 | **0.615** | 0.582 |\\n| L8 | 0.620 | 0.631 | 0.638 | 0.631 |\\n| L13 | 0.676 | 0.679 | 0.676 | 0.664 |\\n\\n- **all24 vs baseline L1**: +0.059, CI [0.042, 0.075], p<0.0001 — **capacity trade-off holds**\\n- *
…[truncated 3452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3871
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-18T08:50:21.069625+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-18T08:50:21.170687+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-18T08:50:29.318079+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研 (CoRL 2026)', 'status': 'in_progress', 'activeForm': '检查资料完整性和 CoRL 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6: 外部审稿线（检查配置）', 'status': 'pending', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研 (CoRL 2026)', 'status': 'in_progress', 'activeForm': '检查资料完整性和 CoRL 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6: 外部审稿线（检查配置）', 'status': 'pending', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-18T08:50:29.368771+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-18T08:50:32.786989+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-18T08:50:34.142981+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd (Plan B → D060 Reframe)\\n\\n> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。\\n> D060: Round 4 weak reject → C1 降为框架, C2 升为唯一核心 claim, C3 降为 qualified observation。\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Insight\\n\\nVLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 25/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。\\n\\n## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)\\n\\n### C1: Experimental Framework + Architecture-Verified Specialization [方法论贡献，非 empirical finding]\\n**重新定位（D060）**: Token-level specialization 是 causal mask 的数学必然（image tokens 在序列中先于 instruction tokens，无法 attend to instructions）+ frozen encoder 不接收 instruction input。论文贡献不是\\\"发现\\\"这一点，而是：\\n- **(a) 系统实验框架**：factorial design (trained/pretrained/untrained × instruction presence) + 四种互补分析方法（cross-instruction probe + attention + RSA + MLP probe），适用于任何 decoder-only VLA\\n- **(b) 量化验证**：即使 residual stream 理论上可以 leak information，image tokens 在实际模型的全部 32 层均保持 chance（10%）。这不是 trivial——frozen encoder 权重与 LLM 权重共享 residual stream，验证了 no leakage\\n- **(c) 训练差异的量化**：untrained readout L1=100% 但 L31=82%（信号衰减）vs trained 100% 全程稳定——framework 揭示了训练影响 routing robustness 而非 routing existence\\n\\nKey evidence (unchanged):\\n- Cross-instruction probe: same frame × 10 instructions → 10-way classification\\n- Dense L0-L32: image_mean = chance at ALL layers\\n- LOOCV: 100%±0.00 trained, decaying untrained\\n- **承认**: 10-way classification 本身 trivially ea
…[truncated 3530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-18T08:50:34.243774+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-18T08:50:34.446819+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-18T08:50:38.403799+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "List project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "List project config files"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-18T08:50:38.706447+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-18T08:50:38.807338+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ -name \"review_issues.yaml\" 2>/dev/null",
  "description": "Check for existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ -name \"review_issues.yaml\" 2>/dev/null",
    "description": "Check for existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-18T08:50:38.858038+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-18T08:50:42.325286+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/ -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/ -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-18T08:50:42.778271+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-18T08:50:42.778606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-18T08:50:42.829115+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-3 历史 issues（全部 resolved）
4	  # ============================================================
5	  - id: R1-N1-old
6	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 2
12	    mentions:
13	      - round: 1
14	        reviewers: [1, 2, 3]
15	        note: "全票共识。需增加 Llama-2 base checkpoint 作为中间对照"
16	      - round: 2
17	        reviewers: [1, 2, 3]
18	        note: "PARTIALLY_RESOLVED: acknowledge confound 但无数据"
19	    action_items:
20	      - round: 1
21	        action: "增加 Llama-2 base checkpoint 对照实验"
22	        assigned_to: research
23	        status: done
24	      - round: 2
25	        action: "Section 标题改为观察性；Abstract 弱化 causal attribution"
26	        assigned_to: paper_agent
27	        status: done
28	    resolution: "B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。"
29	    resolution_round: 3
30	
31	  - id: R1-N2-old
32	    summary: "单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim"
33	    category: framing
34	    severity: critical
35	    status: resolved
36	    first_raised_round: 1
37	    last_seen_round: 2
38	    mentions:
39	      - round: 1
40	        reviewers: [1, 2, 3]
41	        note: "全票共识"
42	      - round: 2
43	        reviewers: [1, 2, 3]
44	        note: "PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数"
45	    action_items:
46	      - round: 2
47	        action: "Title 改为单数"
48	        assigned_to: paper_agent
49	        status: done
50	    resolution: "B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。"
51	    resolution_round: 3
52	
53	  - id: R1-N4-old
54	    summary: "Design implications 完全基于 correlational evidence"
55	    category: framing
56	    severity: cri
…[truncated 1194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-18T08:50:45.794548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-18T08:50:46.698469+00:00_

100	    category: writing
101	    severity: warning
102	    status: resolved
103	    first_raised_round: 1
104	    last_seen_round: 2
105	    resolution: "B版本引用数量达标。"
106	    resolution_round: 3
107	    mentions:
108	      - round: 1
109	        reviewers: [1, 2, 3]
110	        note: "21 citations 严重不足"
111	    action_items: []
112	
113	  - id: R1-W1-old
114	    summary: "'Instruction-blind' claim 过强"
115	    category: framing
116	    severity: warning
117	    status: resolved
118	    first_raised_round: 1
119	    last_seen_round: 2
120	    resolution: "B版本补充 MLP probe 双重验证。"
121	    resolution_round: 3
122	    mentions:
123	      - round: 1
124	        reviewers: [1, 2, 3]
125	        note: "全票共识"
126	    action_items: []
127	
128	  - id: R1-W2-old
129	    summary: "CKA 反转 RSA 排序处理不充分"
130	    category: experiment
131	    severity: warning
132	    status: resolved
133	    first_raised_round: 1
134	    last_seen_round: 2
135	    resolution: "Method 新增 'Why RSA over CKA' 段落。"
136	    resolution_round: 2
137	    mentions:
138	      - round: 1
139	        reviewers: [1, 2, 3]
140	        note: "全票共识"
141	    action_items: []
142	
143	  - id: R3-N1-old
144	    summary: "Limitations 格式不满足 CoRL 2026 要求"
145	    category: format
146	    severity: warning
147	    status: resolved
148	    first_raised_round: 1
149	    last_seen_round: 2
150	    resolution: "改为 \\subsection{Limitations}。"
151	    resolution_round: 3
152	    mentions:
153	      - round: 1
154	        reviewers: [1, 2, 3]
155	        note: "R3 标为 critical"
156	    action_items: []
157	
158	  - id: R3-N2-old
159	    summary: "正文解释性 em-dash 是 AI 写作标志"
160	    category: writing
161	    severity: warning
162	    status: resolved
163	    first_raised_round: 1
164	    last_seen_round: 2
165	    resolution: "零残留。"
166	    resolution_round: 2
167	    mentions:
168	      - round: 1
169	        reviewers: [1, 2, 3]
170	        note: "至少 8 处"
171	    action_items: []
172	
173	  - id: R3-W5-old
174	    summary: "无 code/dat
…[truncated 4333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-18T08:50:46.801098+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-18T08:50:47.003600+00:00_

&lt;persisted-output>
Output too large (42.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/247a19bc-ff5b-4998-8d4a-5a0eb05ea2f4/tool-results/b62934gno.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_sync_figures_local_20260516T081324.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01W4zCnST2DGLEfExj8NcTxW","type":"tool_result","content":"/home/ubuntu/agent-ml-research/core/__init__.py\n/home/ubuntu/agent-ml-research/core/agents/__init__.py\n/home/ubuntu/agent-ml-research/core/agents/base.py\n/home/ubuntu/agent-ml-research/core/agents/coder.py\n/home/ubuntu/agent-ml-research/core/api/__init__.py\n/home/ubuntu/agent-ml-research/core/agents/sub_agent.py\n/home/ubuntu/agent-ml-research/core/agents/preparing.py\n/home/ubuntu/agent-ml-research/core/agents/spec.py\n/home/ubuntu/agent-ml-research/core/agents/reviewer.py\n/home/ubuntu/agent-ml-research/core/agents/sandbox.py\n/home/ubuntu/agent-ml-research/core/api/routers/__init__.py\n/home/ubuntu/agent-ml-research/core/api/middleware.py\n/home/ubuntu/agent-ml-research/core/api/deps.py\n/home/ubuntu/agent-ml-research/core/api/routers/events.py\n/home/ubuntu/agent-ml-research/core/api/routers/chat.py\n/home/ubuntu/agent-ml-research/core/api/routers/images.py\n/home/ubuntu/agent-ml-research/core/api/routers/files.py\n/home/ubuntu/agent-ml-research/core/api/routers/activity.py\n/home/ubuntu/agent-ml-research/core/api/routers/ideas.py\n/home/ubuntu/agent-ml-research/core/api/routers/experiments.py\n/home/ubuntu/agent-ml-research/core/api/routers/approvals.py\n/home/ubuntu/agent-ml-research/core/api/routers/deployments.py\n/home/ubuntu/agent-ml-research/core/api/routers/crons.py\n/home/ubuntu/agent-ml-research/core/api/routers/health.py\n/home/ubuntu/agent-ml-research/core/api/routers/idea_generator.py\n/home/
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-18T08:50:51.035967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "offset": "295",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "offset": "295",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-18T08:50:52.444182+00:00_

295	      - round: 5
296	        reviewers: [1, 2]
297	        note: "N/params 措辞已修正为 overparameterized + early stopping。Linear probe baseline 加入 appendix。"
298	    action_items:
299	      - round: 5
300	        action: "修正措辞 + linear probe baseline"
301	        assigned_to: paper_agent
302	        status: done
303	    resolution: "N/params 措辞修正为 overparameterized，linear probe (N/params≈2.2) 复现所有 pattern，加入 Appendix。"
304	    resolution_round: 5
305	
306	  - id: R4-W4
307	    summary: "Frozen encoder confound"
308	    category: framing
309	    severity: warning
310	    status: resolved
311	    first_raised_round: 4
312	    last_seen_round: 5
313	    resolution: "Frozen encoder confound 在 Introduction 和 Discussion 中均有说明。"
314	    resolution_round: 5
315	    mentions: []
316	    action_items: []
317	
318	  - id: R4-W5
319	    summary: "单模型 + 单 benchmark，泛化性有限"
320	    category: experiment
321	    severity: warning
322	    status: resolved
323	    first_raised_round: 4
324	    last_seen_round: 5
325	    mentions:
326	      - round: 5
327	        reviewers: [1, 2]
328	        note: "Limitations 已列举具体架构变量。"
329	    action_items:
330	      - round: 5
331	        action: "Expand Limitations with specific architecture variables"
332	        assigned_to: paper_agent
333	        status: done
334	    resolution: "Limitations 列举 backbone scale/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data。"
335	    resolution_round: 5
336	
337	  - id: R4-W6
338	    summary: "缺少 Llama-2 和 Open X-Embodiment 关键引用"
339	    category: writing
340	    severity: warning
341	    status: resolved
342	    first_raised_round: 4
343	    last_seen_round: 5
344	    resolution: "两篇引用均已加入。"
345	    resolution_round: 5
346	    mentions: []
347	    action_items: []
348	
349	  - id: R4-W7
350	    summary: "Introduction 'untested assumption' 是 straw man"
351	    category: framing
352	    severity: warning
353	    status: resolved
354	    first_raised_round: 4
355	    last_seen_r
…[truncated 1308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-18T08:50:52.597023+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/*.yml /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/config* 2>/dev/null | head -5",
  "description": "Search for external review config in project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/*.yml /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/config* 2>/dev/null | head -5",
    "description": "Search for external review config in project root"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-18T08:50:52.953072+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 356
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-18T08:51:29.180611+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研 (CoRL 2026)', 'status': 'completed', 'activeForm': '检查资料完整性和 CoRL 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6: 外部审稿线（检查配置）', 'status': 'pending', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研 (CoRL 2026)', 'status': 'completed', 'activeForm': '检查资料完整性和 CoRL 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6: 外部审稿线（检查配置）', 'status': 'pending', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-18T08:51:29.231366+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-18T08:51:50.395321+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-18T08:51:50.596651+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-18T08:52:01.945742+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研 (CoRL 2026)', 'status': 'completed', 'activeForm': '检查资料完整性和 CoRL 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6: 外部审稿线（检查配置）', 'status': 'completed', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'in_progress', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研 (CoRL 2026)', 'status': 'completed', 'activeForm': '检查资料完整性和 CoRL 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6: 外部审稿线（检查配置）', 'status': 'completed', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'in_progress', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-18T08:52:01.946339+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-18T08:52:22.200400+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n### 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **论文文件**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **目标 venue**: CoRL 2026\n- **Deadline**: Abstract May 26, Paper May 29, 2026\n\n### CoRL 2026 格式要求\n- 正文 8 页 + 无限参考文献（初始提交）\n- 必须包含 Limitations section（计入 8 页限制）\n- Double-blind 匿名审稿\n- 模板: `corl_2026` 样式包\n- 需要 Generative AI 使用声明\n- 鼓励提交 video/code/data 补充材料\n\n### 你需要重点评估的方面\n\n1. **Probing 方法论**：\n   - Cross-instruction probe（10-way classification）的设计是否合理？是否存在 trivially easy 的问题？\n   - MLP probe vs linear probe 的 capacity 控制是否充分？\n   - Probe 的 train/test split 是否存在信息泄漏风险？\n\n2. **统计检验**：\n   - RSA、R²、attention 分析的统计显著性检验是否恰当？\n   - 多重比较校正（FDR）是否正确应用？\n   - 效应量报告是否充分？置信区间是否合理？\n\n3. **Ablation 设计**：\n   - L1 head ablation 的因果推断是否有效？\n   - 样本量（N）、demo 数量是否充分？\n   - 控制条件（control8, all32）是否能排除混淆因素？\n\n4. **Baseline 充分性**：\n   - 三条件对照（untrained / Llama-2 base / trained）是否能支撑 claims？\n   - 是否缺少关键 baseline（如其他 VLA 架构、其他 probe 方法）？\n   - RSA 与 CKA metric 分歧的处理是否恰当？\n\n5. **因果 vs 相关**：\n   - 每个 claim 的证据链是否支撑其因果强度？\n   - 是否存在 overclaim（相关性证据声称因果性）？\n\n请通读全文（含附录），按以下格式输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序: [CRITICAL] / [WARNING] / [INFO])\n- W1 [CRITICAL]: ...\n- W2 [WARNING]: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n\n## Overall Assessment\nScore: {strong reject / weak reject / borderline / weak accept / strong accept}\nConfidence: {low / medium / high}\n\n## Detailed Comments (逐节)\n```",
  "project": "vla-ssd"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n### 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **论文文件**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **目标 venue**: CoRL 2026\n- **Deadline**: Abstract May 26, Paper May 29, 2026\n\n### CoRL 2026 格式要求\n- 正文 8 页 + 无限参考文献（初始提交）\n- 必须包含 Limitations section（计入 8 页限制）\n- Double-blind 匿名审稿\n- 模板: `corl_2026` 样式包\n- 需要 Generative AI 使用声明\n- 鼓励提交 video/code/data 补充材料\n\n### 你需要重点评估的方面\n\n1. **Probing 方法论**：\n   - Cross-instruction probe（10-way classification）的设计是否合理？是否存在 trivially easy 的问题？\n   - MLP probe vs linear probe 的 capacity 控制是否充分？\n   - Probe 的 train/test split 是否存在信息泄漏风险？\n\n2. **统计检验**：\n   - RSA、R²、attention 分析的统计显著性检验是否恰当？\n   - 多重比较校正（FDR）是否正确应用？\n   - 效应量报告是否充分？置信区间是否合理？\n\n3. **Ablation 设计**：\n   - L1 head ablation 的因果推断是否有效？\n   - 样本量（N）、demo 数量是否充分？\n   - 控制条件（control8, all32）是否能排除混淆因素？\n\n4. **Baseline 充分性**：\n   - 三条件对照（untrained / Llama-2 base / trained）是否能支撑 claims？\n   - 是否缺少关键 baseline（如其他 VLA 架构、其他 probe 方法）？\n   - RSA 与 CKA metric 分歧的处理是否恰当？\n\n5. **因果 vs 相关**：\n   - 每个 claim 的证据链是否支撑其因果强度？\n   - 是否存在 overclaim（相关性证据声称因果性）？\n\n请通读全文（含附录），按以下格式输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序: [CRITICAL] / [WARNING] / [INFO])\n- W1 [CRITICAL]: ...\n- W2 [WARNING]: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n\n## Overall Assessment\nScore: {strong reject / weak reject / borderline / weak accept / strong accept}\nConfidence: {low / medium / high}\n\n## Detailed Comments (逐节)\n```",
    "project": "vla-ssd"
  }
}
````

</details>

---


### Tool result

_source line 415 · 2026-05-18T08:52:44.247086+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22046
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-18T08:52:44.448103+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 叙事完整性 + 格式合规\n\n### 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **论文文件**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **目标 venue**: CoRL 2026\n- **Deadline**: Abstract May 26, Paper May 29, 2026\n\n### CoRL 2026 格式要求\n- 正文 8 页 + 无限参考文献（初始提交）\n- 必须包含 Limitations section（计入 8 页限制）\n- Double-blind 匿名审稿\n- 模板: `corl_2026` 样式包\n- 需要 Generative AI 使用声明\n- 鼓励提交 video/code/data 补充材料\n\n### 你需要重点评估的方面\n\n1. **新颖性 vs 竞品**：\n   - 与 Grant 2026（\"Not All Features Are Created Equal\"）的差异化是否充分？Grant 用 activation injection/SAE 做了 6 个 VLA 的 behavioral intervention，本文用 probing/RSA 做单模型 representation 分析——增量贡献是否足够？\n   - 与 Swann 2026（SAE on OpenVLA）、Rizzardo 2026（feature observability/controllability）、Haon 2025（CoRL 2025, mechanistic interpretability for VLA）的定位是否清晰？\n   - 核心贡献（trained vs untrained routing reorganization）是否是 genuine novel finding，还是 expected from architecture？\n\n2. **Claim 与 Evidence 匹配度**：\n   - Abstract 和 Introduction 中的每个 claim 是否在实验中有对应证据？\n   - Contribution list 的每一条是否有对应 section/table 支撑？\n   - 是否存在 overclaim（证据只支持弱结论但写了强结论）或 underclaim（有好的结果但没有充分利用）？\n\n3. **叙事连贯性**：\n   - Abstract → Introduction → Method → Experiments → Discussion 是否形成一条统一主线？\n   - 是否有\"故事 A 在 Intro，故事 B 在 Method\"的脱节？\n   - C1（framework + token specialization verification）、C2（routing reorganization）、C3（vision encoder geometry observation）三个 claim 之间的关系是否清晰？\n\n4. **Related Work 覆盖度**：\n   - 引用是否覆盖：直接竞品、baseline 论文（OpenVLA, LIBERO）、评测方法（probing, RSA）、理论基础（mechanistic interpretability）？\n   - 是否缺少 2025-2026 年的重要相关工作？\n   - Positioning 是否清晰（不是 survey 而是定位自己）？\n\n5. **CoRL 格式合规**：\n   - 页数是否在 8 页限制内？\n   - Limitations section 是否存在且有实质内容？\n   - 匿名化是否完整（无 self-citation 泄露、无 GitHub link、无作者信息）？\n   - 图表质量（字体 ≥7pt、caption 自包含、无视觉遮挡）？\n\n6. **写作质量（AI 痕迹检查）**：\n   - 检查解释性 em-dash (—) 和 en-dash (–) 残留\n   - 检查 -ing phrase 结尾（\"..., demonstrating...\"）\n   - 检查过度分段、过渡词堆积（Furthermore/Moreover/Additionally）\n   - 检查 AI 用词黑名单（delve/leverage/utilize/facilitate/myriad/plethora）\n\n请通读全文（含附录），按以下格式输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序: [CRITICAL] / [WARNING] / [INFO])\n- W1 [CRITICAL]: ...\n- W2 [WARNING]: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n\n## Overall Assessment\nScore: {strong reject / weak reject / borderline / weak accept / strong accept}\nConfidence: {low / medium / high}\n\n## Detailed Comments (逐节)\n```",
  "project": "vla-ssd"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 叙事完整性 + 格式合规\n\n### 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **论文文件**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）\n- **目标 venue**: CoRL 2026\n- **Deadline**: Abstract May 26, Paper May 29, 2026\n\n### CoRL 2026 格式要求\n- 正文 8 页 + 无限参考文献（初始提交）\n- 必须包含 Limitations section（计入 8 页限制）\n- Double-blind 匿名审稿\n- 模板: `corl_2026` 样式包\n- 需要 Generative AI 使用声明\n- 鼓励提交 video/code/data 补充材料\n\n### 你需要重点评估的方面\n\n1. **新颖性 vs 竞品**：\n   - 与 Grant 2026（\"Not All Features Are Created Equal\"）的差异化是否充分？Grant 用 activation injection/SAE 做了 6 个 VLA 的 behavioral intervention，本文用 probing/RSA 做单模型 representation 分析——增量贡献是否足够？\n   - 与 Swann 2026（SAE on OpenVLA）、Rizzardo 2026（feature observability/controllability）、Haon 2025（CoRL 2025, mechanistic interpretability for VLA）的定位是否清晰？\n   - 核心贡献（trained vs untrained routing reorganization）是否是 genuine novel finding，还是 expected from architecture？\n\n2. **Claim 与 Evidence 匹配度**：\n   - Abstract 和 Introduction 中的每个 claim 是否在实验中有对应证据？\n   - Contribution list 的每一条是否有对应 section/table 支撑？\n   - 是否存在 overclaim（证据只支持弱结论但写了强结论）或 underclaim（有好的结果但没有充分利用）？\n\n3. **叙事连贯性**：\n   - Abstract → Introduction → Method → Experiments → Discussion 是否形成一条统一主线？\n   - 是否有\"故事 A 在 Intro，故事 B 在 Method\"的脱节？\n   - C1（framework + token specialization verification）、C2（routing reorganization）、C3（vision encoder geometry observation）三个 claim 之间的关系是否清晰？\n\n4. **Related Work 覆盖度**：\n   - 引用是否覆盖：直接竞品、baseline 论文（OpenVLA, LIBERO）、评测方法（probing, RSA）、理论基础（mechanistic interpretability）？\n   - 是否缺少 2025-2026 年的重要相关工作？\n   - Positioning 是否清晰（不是 survey 而是定位自己）？\n\n5. **CoRL 格式合规**：\n   - 页数是否在 8 页限制内？\n   - Limitations section 是否存在且有实质内容？\n   - 匿名化是否完整（无 self-citation 泄露、无 GitHub link、无作者信息）？\n   - 图表质量（字体 ≥7pt、caption 自包含、无视觉遮挡）？\n\n6. **写作质量（AI 痕迹检查）**：\n   - 检查解释性 em-dash (—) 和 en-dash (–) 残留\n   - 检查 -ing phrase 结尾（\"..., demonstrating...\"）\n   - 检查过度分段、过渡词堆积（Furthermore/Moreover/Additionally）\n   - 检查 AI 用词黑名单（delve/leverage/utilize/facilitate/myriad/plethora）\n\n请通读全文（含附录），按以下格式输出审稿意见：\n\n```\n## Summary (2-3 sentences)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序: [CRITICAL] / [WARNING] / [INFO])\n- W1 [CRITICAL]: ...\n- W2 [WARNING]: ...\n\n## Questions for Authors\n- Q1: ...\n\n## Missing References\n\n## Overall Assessment\nScore: {strong reject / weak reject / borderline / weak accept / strong accept}\nConfidence: {low / medium / high}\n\n## Detailed Comments (逐节)\n```",
    "project": "vla-ssd"
  }
}
````

</details>

---


### Tool result

_source line 417 · 2026-05-18T08:52:46.262658+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1814
}
```

</details>

---


### Assistant

_source line 418 · 2026-05-18T08:52:49.424743+00:00_

Round 1 审稿任务已分派：
- **Reviewer 1**（方法严谨性 + 实验设计）→ 已触发
- **Reviewer 2**（新颖性 + 叙事完整性 + 格式合规）→ 已触发

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 42

## Round 42

4 recorded events


### User

_source line 419 · 2026-05-18T08:58:14.274164+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
**Venue**: CoRL 2026
**审查侧重**: 新颖性 + 叙事完整性 + 格式合规

---

## Summary

本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别的表征分析，使用 cross-instruction probes、attention analysis、RSA 和 MLP probes 四种方法，在 trained/pretrained/untrained 三条件阶乘设计下，报告三个发现：(1) image tokens 对 instruction 不敏感（由 causal mask 和 frozen encoder 架构保证），(2) VLA fine-tuning 将 instruction routing 从 mid-depth 前移到 entry-exit 层，(3) vision encoder 表征在 LLM 层中呈非单调变换。实验设计严谨，统计报告完整，但核心新颖性受限于单模型范围和部分 architecturally-expected 的发现。

---

## Strengths

- **S1: 实验设计严谨的阶乘控制**。trained/pretrained/untrained × instruction presence/absence 的 2×3 设计是该领域少见的严格控制方案，能有效隔离 language pretraining 和 VLA fine-tuning 各自的贡献（Section 3.1）。这一设计优于 Grant 2026 等仅做 trained model 分析的工作。

- **S2: 统计报告高标准**。所有主要结论均附有 bootstrap CI（10,000 resamples）、FDR 校正（Benjamini-Hochberg）、permutation test、seed sensitivity、demo subsampling sensitivity（Appendix H-J）。这在 VLA interpretability 文献中罕见，值得肯定。

- **S3: Routing reorganization 发现有价值**。C2（Section 4.3, Figure 1, Table 2）揭示 VLA fine-tuning 将 instruction routing 从 Llama-2 的 mid-depth 模式（L9-L16, 15-22 heads）重组为 entry-exit 模式（L0-L1: 21-24 heads, L31: 18 heads），且三条件梯度在 30%-70% 阈值范围内稳定（Appendix Table 14）。这是对 VLA 内部机制的有意义新知识。

- **S4: 方法互补性好**。四种分析方法（probing → 功能可解码性，attention → 机制，RSA → 几何对齐，cross-instruction → token 特化）从不同角度交叉验证同一结论，增强了可信度。RSA 与 CKA 的分歧也被坦诚报告（Appendix A-B），而非回避。

- **S5: Related Work 定位清晰**。与 Grant 2026 的三点差异（token-level vs feature-level, per-layer decomposition, factorial controls）在 Section 2 第三段明确阐述，positioning 准确。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1 [CRITICAL]: Contribution 1（token specialization）是架构上的必然结果，不构成实质新颖性**
- 具体位置：Abstract 第4句, Introduction §1 Finding 1, Section 4.2, Contribution (i)
- 问题：Image tokens 对 instruction blind 是 causal mask（image tokens 在 instruction tokens 之前，无法回看）和 frozen encoder（不接收 language input）的直接架构推论。论文自己也承认这是 "architecture-expected"（Abstract 第4句, Introduction ¶3 "consistent with architectural expectations"）。用 4 种 probe 方法验证一个架构保证的性质，methodologically sound 但不构成 contribution。将其列为三大贡献之首（Contribution (i)）让审稿人质疑 novelty bar。readout token 作为 multimodal hub 同样是 decoder-only 架构中 last token 的标准角色。
- 为什么影响接收：如果三大贡献中的一个是验证已知事实，实际 novel contributions 只有 C2 和 C3。C3 又是 metric-dependent（见 W3），则论文的核心新颖性实质上只有 C2 的 routing reorganization。对 CoRL 而言，单一发现的增量贡献度不够。
- 建议修改方向：将 C1 降格为 "methodology validation"（验证分析框架的有效性），而非独立 contribution。将 Contribution 列表重心放在 C2 和 C3，并加强 C2 的 behavioral implications。

**W2 [CRITICAL]: 单模型（OpenVLA-7B）+ 单 benchmark 家族（LIBERO），泛化性严重不足**
- 具体位置：Abstract（无 qualification）, Introduction（claims 用一般化措辞）, Discussion "Limitations and scope"（仅半段）
- 问题：所有实验只在 OpenVLA-7B 上进行，benchmark 仅 LIBERO-Goal 和 LIBERO-Spatial（同一 benchmark 家族的两个 split）。但 Abstract 写 "instruction routing reorganization is the primary learned contribution of VLA fine-tuning"——这是对所有 VLA fine-tuning 的一般性声明，证据只来自一个模型。Grant 2026 覆盖 6 个 VLA（80M-7B），本文在范围上明显更窄。Discussion 承认 "C2 may differ across backbone scales, decoder paradigms, and encoder training regimes"，但 Abstract/Introduction 的 framing 没有相应 qualify。
- 为什么影响接收：CoRL 审稿人会问：这些发现在 RT-2、π₀、SmolVLA 等不同架构上是否成立？特别是 π₀ 使用 flow matching 而非 autoregressive decoding，entry-exit routing pattern 可能完全不同。单模型分析论文在 CoRL 的 bar 上需要更强的 insight 或 architectural implication 来补偿。
- 建议修改方向：(a) 在 Abstract/Introduction 中明确限定 scope（"on OpenVLA-7B" 而非泛化措辞），(b) 在 Discussion 扩充 limitation 段，讨论 flow-matching VLAs、不同 encoder training regimes 下 C2 可能不成立的原因，(c) 如有可能，至少在一个不同架构的 VLA 上验证 C2 的 entry-exit pattern。

**W3 [CRITICAL]: 缺少行为层面验证——representational finding 未与 task performance 连接**
- 具体位置：Section 4.3 ablation, Discussion "Architectural implications"
- 问题：论文报告了 attention head ablation 对 R² 的影响（Section 4.3: dominant heads +0.042, random heads +0.077），但从未测量对实际 task success rate 的影响。R² 是 probe 在 frozen representations 上的离线指标，不等于 behavioral importance。Discussion 自己也承认 "linking routing to behavioral outcomes requires task-level evaluation"。对于 CoRL（机器人学习会议），representational analysis 不与 behavioral outcomes 连接，是一个重要缺口。
- 为什么影响接收：CoRL 审稿人期望看到发现对 robot policy 设计有 actionable implications。论文的 architectural implication（"early-layer parameters may suffice for instruction adaptation"）是 speculative 的，没有任何实验支撑。如果 routing reorganization 对 success rate 的影响微乎其微，整篇论文的实际价值就存疑。
- 建议修改方向：(a) 至少做一个简单的 behavioral validation：在 LIBERO 上用 ablated model 跑 rollout，报告 success rate 变化，(b) 或者将论文重新定位为 "representational analysis" 而非暗示 design implications，降低 claim 强度。

### Should-Fix 问题（影响评分但不一票否决）

**W4 [WARNING]: Ablation 解释逻辑不够 convincing**
- 具体位置：Section 4.3 ¶4, Appendix E
- 问题：Ablating 24 个 instruction-dominant heads 使 R² 从 0.517 增加到 0.559（+0.042），ablating 随机 24 heads 增加更多（+0.077）。论文解释为 dominant heads 具有 "dual routing-encoding function"。但同样合理的解释是：(a) ablation 本身通过移除 noise/interference 普遍提高 R²（无论哪些 heads），(b) dominant heads 贡献略少于随机 heads 恰恰因为它们不编码 action-relevant information。论文的 "dual function" 解释需要额外证据排除 alternative explanations。且 z-score 基于仅 10 个 random subsets，统计功效有限。
- 建议：增加 random subsets 数量（至少 100），并考虑 attention knockout（将 attention 设为 uniform 而非 zero）作为对照。

**W5 [WARNING]: C3（非单调变换）是 metric-dependent 的，CKA 直接矛盾**
- 具体位置：Appendix A-B (Figure 6), Section 4.4 ¶3
- 问题：RSA 显示 inverted-U（peak L12），但 linear CKA 显示单调递增（L0: 0.081 → L32: 0.098），甚至 untrained > trained。论文解释为 "RSA captures rank-order geometry; CKA captures global linear structure"，但读者可以合理选择 CKA 来讲一个完全相反的故事。C3 作为独立 contribution，其 robustness 受到 metric 选择的严重制约。此外，NLP 领域已广泛记录 transformer 层的非单调 probing profile（Tenney 2019 等），将其延伸到 VLA 的增量新颖性有限。
- 建议：(a) 在正文（非仅 Appendix）承认 CKA 的矛盾结果，(b) 将 C3 定位为 "observation" 而非独立 contribution，(c) 讨论 RSA vs CKA 分歧对结论的实质影响。

**W6 [WARNING]: Abstract 和 Introduction 数据密度过高，叙事可读性受损**
- 具体位置：Abstract 全文, Introduction ¶3-4
- 问题：Abstract 在约 200 words 中包含了 ~15 个具体数值（10%, 100%, L0-L1, 21-24 heads, L9-L16, 15-22 heads, 99.6%, 80.2%, z=-2.73, R² peaks L8-L14, ρ=0.628, 0.422, +0.069, +46pp, ≤0.017）。Introduction 同样密集。这让论文读起来像 experimental report 而非有说服力的 narrative。审稿人在 30 秒内无法从 Abstract 提取核心价值。
- 建议：Abstract 保留 2-3 个最关键数字，其余移入正文。Introduction 的 three findings 段落应先建立直觉再给数字。

**W7 [WARNING]: 格式问题——缺少 Generative AI 使用声明**
- 具体位置：main.tex 全文
- 问题：CoRL 2026 Call for Papers 要求提交 Generative AI 使用声明（disclosure of generative AI use）。当前稿件中未找到此声明。
- 建议：按 CoRL 2026 要求添加 Generative AI disclosure statement。

**W8 [WARNING]: conclusion.tex 存在但未被 main.tex 编译**
- 具体位置：main.tex line 28-32（\input 列表中无 conclusion）, conclusion.tex（存在于同一目录）
- 问题：conclusion.tex 文件包含一个完整的 Conclusion section，但 main.tex 的 \input 序列中没有 \input{conclusion}。这意味着编译后的 PDF 没有 Conclusion 节。Discussion 节结尾没有明确总结，读者看到的最后正文内容是 Limitations and scope 段落。
- 建议：在 \input{discussion} 之后、\bibliography 之前添加 \input{conclusion}。

### 小问题（不影响接收）

- **M1**: "-ing" 分词短语在全文中出现约 30+ 次（", indicating...", ", confirming...", ", reflecting..."）。虽然每处单独看是自然英文，但高密度是 AI 辅助写作的统计信号。建议通读一遍，将部分改写为独立句子。
- **M2**: Appendix 中 conclusion.tex 第 6 行 "Code and representations will be released upon acceptance" 可能泄露非匿名信息（暗示作者有代码控制权）。对 double-blind 无大碍，但建议改为更中性的表述。
- **M3**: Table 2 caption 需要解释 "Mode" 列的含义（"immed.+stable", "gradual+stable", "incid.+forget"），当前 caption 不自包含。
- **M4**: references.bib 中 nostalgebraist2020 的 `note = {Accessed: 2026-05-18}` 暴露了写作日期，在 blind review 中无实质风险但不够规范。
- **M5**: Discussion "Speculative mechanistic interpretation" 段落（¶3）标题中的 "Speculative" 过于自我贬低，建议改为 "Mechanistic hypothesis" 或直接去掉限定词。

---

## Questions for Authors

- **Q1**: Untrained readout 在 L1 达到 100% cross-instruction classification（Table 1），但 untrained model 在 L1 有 0/32 instruction-dominant heads（Table 2）。论文解释为 "even incidental attention (~12%) suffices for linear classification"（Appendix K.1）。如果 12% 的 incidental attention 就足以完美分类，那么 VLA training 将 L1 attention 提高到 57.7% 的功能意义是什么？这是否说明 cross-instruction probe 的 ceiling effect 太严重，无法区分 fine 的路由差异？

- **Q2**: 论文声称 "vision encoder quality emerges as a key design lever"（conclusion.tex），但实验中 DINOv2 cls_token 的 RSA 最高（0.692）而 VLA trained readout 的 R² 最高（0.678）。这两个指标指向不同的 "best" representation。如果两者矛盾，"vision encoder quality" 的操作化定义是什么？

- **Q3**: Pretrained Llama-2 base 接收的是从未在 pretraining 中见过的 visual token projections（OOD input）。虽然 Appendix G 报告了 activation diagnostics，但这些诊断只证明 representations 非退化，不证明 pretrained model 的 routing pattern（mid-depth concentration）是 meaningful 而非 arbitrary OOD response。如何排除 pretrained condition 的 routing pattern 只是 OOD 输入的 artifact？

- **Q4**: L1 ablation 实验使用了 "feature reconstruction pipeline"（Section 4.3 footnote 1），其 baseline R² (0.517) 与 Table 3 的值 (0.557-0.678) 不同。这个 pipeline 的细节在哪里描述？差异的来源是否影响 ablation 结论的可靠性？

---

## Missing References

1. **Rizzardo et al. (2026)** — 如果 Buurmeijer 2026 不是同一篇，则缺少 Rizzardo 2026 的 feature observability/controllability 工作
2. **Bills et al. (2023)** "Language models can explain neurons in language models" — SAE/feature interpretation 的重要方法论基础
3. **Templeton et al. (2024)** "Scaling monosemanticity" — Anthropic 的 SAE scaling 工作，与 Swann 2026 的方法论基础相关
4. **Neel Nanda et al. (2023)** "Progress measures for grokking via mechanistic interpretability" — mechanistic interpretability 的重要参考
5. **可能缺少 VLA fine-tuning 效率相关工作**（如 parameter-efficient fine-tuning for VLAs），因为论文暗示 "early-layer parameters may suffice for instruction adaptation"

---

## 官方维度打分（基于 CoRL 2023/2024 review criteria）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 4/10 | C1 是架构必然；C3 是 metric-dependent；实质新颖性主要在 C2 routing reorganization |
| Quality/Soundness | 7/10 | 实验设计严谨，统计完整，但缺少 behavioral validation，ablation 解释存在 alternative explanations |
| Clarity | 6/10 | 写作技术上清晰但 Abstract/Intro 数据过载，叙事感不足，更像 experimental report |
| Significance | 4/10 | 单模型单 benchmark 的 representational finding，无 behavioral validation，对 VLA 设计的 actionable implications 仅 speculative |
| Relevance | 7/10 | VLA interpretability 是 CoRL 关心的方向，但纯 representation analysis 不如 behavioral/design insights 与 CoRL 受众匹配 |
| Limitations | 6/10 | 存在但仅半段嵌入 Discussion，scope 限制描述到位但未讨论关键 failure modes |

---

## Overall Assessment

**Score: Weak Reject (4/10)**
**Confidence: High**

**一句话总结**: 实验设计和统计严谨度优秀，但三大贡献中 C1 是架构必然、C3 是 metric-dependent，实质新颖性集中在 C2（routing reorganization），而单模型+无 behavioral validation 使这一贡献难以达到 CoRL 的 acceptance bar。

**核心判断**：本文是一篇执行质量高的 representational analysis 工作，但存在 novelty 和 significance 的结构性问题。如果作者能 (a) 在至少一个额外 VLA 上验证 C2，(b) 添加 behavioral validation（哪怕是 preliminary 的 success rate 测量），(c) 重组 contribution 列表将 C1 降格，论文的竞争力会显著提升。当前版本更适合 workshop paper 或需要 major revision 后重投。

---

## Detailed Comments（逐节）

### Abstract
- 数据密度过高（~15 个数字），可读性差。核心 message 被淹没在统计细节中。
- "instruction routing reorganization is the primary learned contribution of VLA fine-tuning" 是 overclaim（单模型证据）。

### Introduction
- 5 段结构完整，从 gap 到 method 到 findings 到 contributions 的逻辑清晰。
- 但 ¶3-4 重复 Abstract 的数字密集风格，未建立足够的直觉铺垫。
- Contribution (i) 的 "verifying architecture-expected specialization" 措辞暗示作者知道这不是 novel finding，但仍列为 contribution。

### Related Work
- 覆盖全面：VLA models, mechanistic interpretability, behavioral analysis, token specialization, similarity methods 五个主题。
- 与 Grant 2026 的差异化（第三段）清晰有力。
- 缺少 SAE 方法论基础文献（Bills 2023, Templeton 2024）。

### Method
- 清晰、可复现。四种分析方法的选择有充分 justify（特别是 RSA over CKA 的段落）。
- "Why RSA over CKA" 段落放在 Method 中有些突兀，考虑移至 Appendix。

### Experiments
- Section 4.2（Token Specialization）: 结果 clean 但 C1 的 novelty 问题依然存在。
- Section 4.3（Routing）: 最强的贡献。Figure 1 和 Table 2 清晰展示三条件梯度。
- Section 4.4（Non-monotonic）: 数据详实但 CKA 矛盾未在正文讨论。

### Discussion
- 简洁但过于简短。"Speculative mechanistic interpretation" 段有价值但自我限制过多。
- "Limitations and scope" 仅半段，未讨论 behavioral validation 缺失和 metric dependence。
- 建议扩充 Limitations 为独立 section（CoRL 要求）。

### Appendix
- 内容丰富且必要（robustness, cross-benchmark, diagnostics）。
- 但部分结果（CKA 矛盾、action R² three-condition）对主文叙事有重大影响，应在正文中至少 summarize。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-18T08:58:32.115165+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.6: 初始化 + Venue 调研 + Reviewer 编排', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿 — R2 已返回，等待 R1', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 审稿意见返回'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.6: 初始化 + Venue 调研 + Reviewer 编排', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿 — R2 已返回，等待 R1', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 审稿意见返回'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-18T08:58:32.115575+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-18T08:58:34.965346+00:00_

Reviewer 2 审稿意见已收录。等待 Reviewer 1 返回后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 423 · 2026-05-18T08:58:37.821106+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心判断：**Weak Reject (4/10)**，信心 High。

主要问题：
1. **C1（token specialization）是架构必然结果**，不构成实质 contribution
2. **单模型单 benchmark**，泛化性不足，但 claims 用了一般化措辞
3. **无 behavioral validation**——representational findings 未与 task success rate 连接，对 CoRL 是重大缺口
4. 格式问题：缺少 Generative AI 声明，conclusion.tex 未编译，无独立 Limitations section

主要优势：阶乘实验设计严谨，统计报告高标准，C2（routing reorganization）有实质新颖性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 424 · 2026-05-18T08:58:45.150500+00:00_

R2 审稿意见已记录。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 44

## Round 44

8 recorded events


### User

_source line 425 · 2026-05-18T09:07:44.861951+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 Review

**Paper**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**Target Venue**: CoRL 2026
**审查侧重**: 方法严谨性 + 实验设计

---

## Summary (2-3 sentences)

本文对 OpenVLA-7B 在 LIBERO 上进行了 per-layer、per-token-type 的表征分析，使用 cross-instruction probes、attention pattern analysis、RSA 和 functional probes，配合 trained/pretrained/untrained 三条件对照。核心发现是：(1) image token 对 instruction 不敏感（架构必然）；(2) VLA 训练将 instruction routing 从中层移至 entry-exit 层；(3) vision encoder 表征经 LLM 层呈 inverted-U 变换。这是一篇分析型论文，方法论工作扎实但存在若干统计推断和因果推断层面的问题。

---

## Strengths

- **S1: 系统性的实验框架设计。** 三条件因子控制（VLA-trained / Llama-2 base / untrained）× 指令有无的 2×2 factorial 设计是合理的。与大多数 VLA 分析工作相比，这种控制更完整，可以隔离语言预训练和 VLA fine-tuning 各自的贡献（Section 3.1）。

- **S2: 多角度互验。** RSA（几何对齐）+ functional probes（可解码性）+ attention analysis（机制）+ cross-instruction probes（信息内容）四种互补工具的组合使用是方法论上的优势。Linear probe 复制（Appendix A.6）进一步增强了 functional probe 结论的可信度。

- **S3: 丰富的 robustness 分析。** 附录中的 distance metric invariance（Table A.5）、demonstration subsampling（Table A.7）、seed sensitivity（Table A.6）、threshold sensitivity（Table A.10）、cross-benchmark validation（LIBERO-Spatial, Appendix A.4）显示作者认真检验了结论的鲁棒性。

- **S4: 对 CKA 分歧的诚实处理。** 多数论文会回避不利结果。作者坦承 linear CKA 完全反转了 RSA 排序（Appendix A.2, Figure A.1），并提供了合理（虽然不完全令人信服）的解释。

- **S5: 与 behavioral 文献的连接。** 将 image-token instruction-blindness 与 Grant et al. [2026] 和 Häon et al. [2025] 发现的 visual dominance 建立联系（Discussion），帮助读者理解分析发现的实际意义。

---

## Weaknesses (按严重程度排序)

### W1 [CRITICAL]: Cross-instruction probe（Finding 1）近乎 trivially easy，削弱了核心贡献的新颖性

**位置**: Section 4.2, Table 1

**问题**: 10-way cross-instruction classification 在 readout token 位置上，ALL THREE 条件（trained, pretrained, untrained）在 L1 均达到 99.6-100%。作者自己在 Appendix A.8.1 承认 "even incidental attention (~12%) suffices for linear classification at L1"。这意味着只要有任何 attention 到 instruction tokens——哪怕是随机初始化权重产生的微弱 attention——probe 就能轻松区分 10 条差异很大的 LIBERO 指令。

10 条 LIBERO-Goal 指令（如 "pick up the red cup" vs "push the blue block"）在 token 层面差异巨大。一个 linear classifier 只需检测到 instruction embedding 的最微小残留即可达到 100%。这不是关于 VLA 如何处理指令信息的深层洞察，而是 tokenizer + 单层 attention 的 trivial 后果。

更有信息量的比较是 DECAY PATTERN（untrained 从 100% 降至 82%，trained 维持 100%），但论文将 "100% from L1" 作为主要发现来呈现，而非衰减差异。

**为什么影响接收**: Finding 1（token-level functional specialization）是三个核心贡献之一。如果它大部分由架构约束直接推出（causal mask → image tokens blind，tokenizer + any attention → readout trivially classifiable），那么作为 "contribution" 的增量价值大幅降低。

**建议**: (a) 增加更难的 probe task（如语义近似但不同的指令，或 paraphrase 指令）以测试真正的指令理解 vs. 表面 token 检测；(b) 重新 framing Finding 1 为 "验证架构预期" 而非 "发现"，论文部分已做但不够彻底。

---

### W2 [CRITICAL]: L1 head ablation 的因果推断方向存在根本性问题

**位置**: Section 4.3, Appendix A.4

**问题**: Ablating 24/32 dominant heads at L1 increases action R² by +0.042（baseline 0.517）。Random 24-head ablation increases by +0.077。作者解释为 dominant heads 具有 "dual routing-encoding function"。

但基本事实是：ablating ANY 24 out of 32 heads (75%) at L1 IMPROVES action prediction。无论是 dominant heads 还是 random heads，移除都提高 R²。这意味着 L1 的大多数 heads 对 action prediction 是 net-negative 的。如果研究者声称 L1 的 instruction-dominant heads 具有功能性重要作用，那么 ablation 应该 DECREASE R²（性能变差），而非 increase。

论文的 "dual function" 解释是一种 post-hoc rationalization：dominant heads 虽然 R² 增幅小于 random heads，但两者都是正增幅。等效的替代解释是：L1 heads 普遍对 action probe 添加噪声，dominant heads 因为 attention pattern 更结构化所以噪声更少。这不需要 "dual function" 假设。

此外，random-subset 只用了 N=10 个子集（C(32,24) = 10,518,300 种可能），z-test 的统计检验力极低且分布假设可疑。

**为什么影响接收**: L1 ablation 是论文中唯一的因果证据（区别于纯相关性分析）。如果因果推断不成立，Finding 2 的证据链从 "相关+因果" 降级为 "仅相关"。

**建议**: (a) 增加更细粒度的 ablation（如 ablate 4/8/12/16/20/24/28 heads，观察 R² 变化曲线）；(b) 尝试 SELECTIVE ablation（只 ablate dominant heads 的 instruction attention，保留 image attention），这能更精确地测试 "dual function" 假设；(c) 大幅增加 random subsets 数量（≥100）；(d) 修改 framing 以反映实际发现（所有 ablation 都提高 R²）。

---

### W3 [CRITICAL]: Action probe 的 train/test split 未明确说明，overparameterized MLP probe 的 R² 可信度存疑

**位置**: Section 3.6, Section 4.1

**问题**: MLP probe 的 N/params ≈ 0.06（作者自认 "overparameterized"）。论文称 "early stopping mitigates overfitting"，但：

(a) R² 是在哪个数据集上计算的？论文未明确说明 train/test/validation split。如果 R² 是 training data 上的值，那么 overparameterized model 可以达到任意高的 R²，所有结论无效。如果是 validation set（early stopping 的依据），那么 R² 也可能被 early stopping 的选择偏倚。

(b) Linear probe 复制（Appendix A.6）显示 trained-untrained gap 在 linear probe 下为 Δ = +0.324（L14），在 MLP probe 下仅为 Δ = +0.015（L8），相差 ~20 倍。这暗示 MLP probe 过于强大，rescues 了 untrained representations 的信息，压缩了条件间差异。这意味着 MLP probe R² 的绝对值和条件间差异都可能是 misleading 的。

(c) N=63,228 observations 但时间步之间高度自相关（连续 frames of same demo），有效样本量远小于名义值。Bootstrap CI 基于独立重抽样假设，可能严重低估不确定性。

**为什么影响接收**: 几乎所有 functional decodability 结论都依赖 probe R²。如果 R² 不可信，Finding 3（non-monotonic refinement）的 functional 证据和 trained vs. untrained 比较的定量结论都受影响。

**建议**: (a) 明确报告 train/test split 策略（建议按 demo 或 task 分组以避免 temporal leakage）；(b) 报告 test-set R²，not training/validation R²；(c) 使用 task-level 或 demo-level bootstrap（而非 timestep-level）以反映真实不确定性；(d) 讨论 MLP vs linear probe gap 的含义。

---

### W4 [WARNING]: RSA 统计推断中的依赖性问题未处理

**位置**: Section 3.5, Section 4.4

**问题**: RSA 使用 Spearman ρ 比较 N×N RDM 的上三角。但 N(N-1)/2 pairwise distances 不是独立的（共享 observations），标准 bootstrap 会低估 variance。作者使用 10,000 bootstrap resamples 计算 CI，但 bootstrap 的 resampling unit 不明确。如果是 timestep-level resampling，CI 会因依赖性被严重低估。

Permutation test（Appendix A.9.3）仅测试 "是否存在 ANY structure"（observed ρ vs. null），这个 trivially significant（ρ = 0.4-0.6 vs null max 0.08-0.10），但不测试条件间差异的显著性。

训练效应的核心比较：best-vs-best Δ = +0.017 是 n.s.，same-layer L12 Δ = +0.079 是 p < 0.0001。但 same-layer 比较存在 selection bias（选择了差异最大的层）。正确的做法是 pre-register 比较层或对所有 33 层做 FDR correction。

**建议**: (a) 使用 Mantel test 或 stimulus-level bootstrap（resample observations, not distances）作为更合适的 RSA 统计检验；(b) 明确 bootstrap resampling unit；(c) 对条件间 RSA 差异进行适当的多重比较校正。

---

### W5 [WARNING]: RSA vs CKA 分歧对 Finding 3 的影响被低估

**位置**: Appendix A.1-A.2, Section 4.4

**问题**: Linear CKA 完全反转 RSA 排序：untrained LLM (0.089) > trained LLM (0.083) > DINOv2 (0.066)（Appendix A.2）。更重要的是，linear CKA 的 per-layer profile 是 MONOTONICALLY INCREASING（L0: 0.081 → L32: 0.098），完全没有 inverted-U。

论文的解释是 "RSA captures rank-order geometry; CKA captures global linear structure"，但这只是重述了数学定义，没有论证为什么 rank-order geometry 对 VLA action prediction 更相关。如果 CKA（度量 global covariance structure）才是更相关的 metric，那么 Finding 3 的 "non-monotonic refinement" 完全不存在——实际上是 monotonic improvement。

RDM kernel CKA 部分支持 RSA（trained > untrained），但 encoder ordering 仍不同。三个 metrics 给出三种不同的故事，论文选择了 RSA 的故事作为主叙事。

**为什么影响接收**: Finding 3 是论文三个核心发现之一，而它是 metric-dependent 的。不同读者可能合理地选择 CKA 而得出完全不同的结论。

**建议**: (a) 提供理论或实证论证说明为什么 rank-order preservation（RSA）比 covariance alignment（CKA）更预测 downstream action performance；(b) 或者将 Finding 3 重新表述为 "under RSA" 并承认在 CKA 下不成立，降低 claim strength。

---

### W6 [WARNING]: 单模型单 benchmark，泛化性不足以支撑 general claims

**位置**: Title, Abstract, Discussion (Section 5)

**问题**: 论文标题 "Vision Encodes, Language Routes" 暗示对 VLA 的一般性结论，但所有实验仅在 OpenVLA-7B + LIBERO 上进行。LIBERO 仅包含 10 个 tabletop manipulation tasks，50 demos each。

- 无其他 VLA 模型（如 RT-2, π₀, Octo 等）
- 无 real-robot 数据
- 无多样化任务域（所有 tasks 都是 tabletop manipulation）
- LIBERO-Spatial 作为 cross-benchmark validation 仍在 LIBERO 框架内，任务域相同

Discussion 声称 "OpenVLA shares the dominant VLA design... with RT-2 and π₀"，但 π₀ 使用 flow matching 而非 autoregressive decoding，RT-2 使用不同的 vision encoder。这些架构差异可能导致完全不同的 representation dynamics。

**建议**: (a) 将所有 claims 明确限定在 "OpenVLA-7B on LIBERO" 范围内；(b) 或至少在一个架构差异较大的 VLA 上复制核心发现（如使用 diffusion/flow decoder 的模型）。

---

### W7 [WARNING]: 缺少行为验证——表征分析与任务表现之间的 gap 未弥合

**位置**: Discussion Section 5

**问题**: 论文的所有发现都在 representation space 中，没有任何一个发现被连接到 actual task success rate。例如：

- "Front-loaded instruction routing" 是否意味着更好的 instruction following？
- Inverted-U 的 peak layer 是否预测 task performance？
- L1 attention ablation 如何影响 rollout success？

作者在 Limitations 中承认 "linking routing to behavioral outcomes requires task-level evaluation"，但对于 CoRL（一个 robotics 会议），representational analysis 如果不能连接到 robot behavior，其实用价值有限。

**建议**: 即使是 pilot 级别的行为验证（如：ablate L1 instruction routing → rollout success 变化）也能大幅提升论文说服力。

---

### W8 [INFO]: Pretrained Llama-2 的 visual token 处理是否有意义

**位置**: Section 3.1, Appendix A.5

**问题**: Pretrained Llama-2 从未见过 projected visual tokens。Appendix A.5 的 OOD diagnostics 仅证明 representations 非退化（activation magnitude 合理、cosine similarity progressive decline、PC variance stable），但非退化不等于有意义的处理。一个 non-degenerate but meaningless 的 representation 也能通过这些测试。

这个条件的 cross-instruction probe 结果（L1: 80.2% → L31: 100%）可能反映了 Llama-2 的 generic 序列处理能力（任何 token 序列都会被逐层整合），而非对 visual+instruction 的有意义处理。

**建议**: 加一个 diagnostic：用 random noise tokens（相同维度）替代 visual tokens 输入 Llama-2 base，如果 probe 结果类似，则 Llama-2 base 条件的可解释性大幅降低。

---

## Questions for Authors

**Q1**: Action probe 的 R² 是在 training set 还是 held-out test set 上计算的？如果是 test set，train/test split 策略是什么（random timestep split? demo-level? task-level?）？

**Q2**: 所有 head ablation（dominant 和 random）都 INCREASE R²。这是否意味着 L1 的大多数 heads 对 action prediction 实际上是有害的？如果是，"dual routing-encoding function" 的解释还成立吗？

**Q3**: 如果将 Finding 1 的 10-way classification 替换为更难的任务（如 paraphrase 指令或语义相近的指令对），结果是否会不同？是否有定量估计 probe task difficulty 的方法？

**Q4**: 为什么 linear probe 的 trained-untrained gap（Δ = +0.324 at L14）是 MLP probe gap（Δ = +0.015 at L8）的 ~20 倍？这对结果解释有什么影响？

**Q5**: Bootstrap CI 的 resampling unit 是什么？如果是 timestep-level，如何处理同一 demo 内时间步之间的高度自相关？

**Q6**: 能否提供 RSA 条件间差异的 permutation test 或 Mantel test（而非仅测试 "是否存在 structure"）？

---

## Missing References

引用覆盖基本充分（42 篇，含 VLA、mechanistic interpretability、probing methodology 的关键文献）。以下可考虑补充：

- **Probing methodology 的 criticism**: Hewitt & Liang (2019) "Designing and Interpreting Probes with Control Tasks"——关于 probe selectivity 的重要讨论，与本文 probe 方法论直接相关
- **VLA behavioral evaluation**: 论文引用了 Grant et al. 和 Häon et al.，但缺少 Zheng et al. (2024) "3D-VLA" 等在表征层面分析 VLA 的工作
- **RSA 统计方法**: Nili et al. (2014) "A Toolbox for Representational Similarity Analysis"——包含 RSA 统计推断最佳实践的工具箱论文

---

## Overall Assessment

**Score: 5 (Marginally below acceptance threshold)**

**Confidence: 4 (Confident but not absolutely certain)**

---

## 官方维度打分（基于 CoRL review dimensions + OpenReview default form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 6/10 | 三条件 factorial design 和 per-layer per-token-type 分析框架有新意；但 Finding 1 大部分由架构推出，Finding 3 是 metric-dependent 的 |
| Quality (Soundness) | 4/10 | Ablation 因果推断方向有问题（W2）；probe train/test split 未说明（W3）；RSA 统计推断有依赖性问题（W4）；MLP probe overparameterized |
| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度高；附录组织良好。但部分关键方法细节缺失（train/test split, bootstrap unit）|
| Significance | 5/10 | 分析框架可复用，但缺少行为验证（W7），泛化性不足（W6），且核心发现中 2/3 有方法论隐忧 |
| Relevance to CoRL | 5/10 | 研究 VLA 是 relevant 的，但 CoRL 更看重 actionable 的机器人学习贡献；纯表征分析无 behavioral validation 对 robotics community 的直接价值有限 |
| Limitations honesty | 7/10 | 作者诚实报告了单模型限制、CKA 分歧、n.s. results；但未充分讨论 probe methodology 的局限 |

---

## Detailed Comments (逐节)

### Abstract
- Abstract 结构合理，覆盖了四个必答问题。
- "100% instruction classification from L1, cross-validated" 在不提及 untrained 也达到 100% 的情况下显得 misleading。
- "$z = -2.73$" 级别的细节不适合 abstract。

### Introduction
- 叙事线清晰：behavioral observation → gap → our approach → three findings → contributions。
- 但 contribution (i) "verifying architecture-expected specialization" 在 Introduction 中被 framed 为一个积极贡献，实际上它更像是一个 sanity check。将 sanity check 升格为 contribution 降低了论文的 novelty 感知。
- Contribution (iii) 中 "RSA confirms geometrically but CKA diverges" 的 parenthetical 承认了问题但在 contribution 列表中提及让读者困惑——核心贡献是否 metric-dependent？

### Method (Section 3)
- 方法描述清晰完整。
- Section 3.6 "Why RSA over CKA" 给出了合理理由（scale invariance, dimension mismatch），但 dimension mismatch 主要影响 linear CKA，而 RDM kernel CKA 不受此问题影响却仍与 RSA 部分分歧。

### Experiments (Section 4)

**4.2 Token-Level Functional Specialization:**
- Image-token instruction-blindness 是 causal mask 的直接后果，不是发现。论文部分承认 ("consistent with the causal mask and frozen encoder") 但仍将其作为 Finding 1 的主要组成部分。
- Readout token 100% 分类的 trivially easy 问题见 W1。

**4.3 VLA Fine-Tuning Front-Loads Instruction Routing:**
- 三条件 gradient（untrained 0/32 → Llama-2 base 9/32 → VLA-trained 24/32）是论文最有说服力的发现。
- Threshold sensitivity analysis（Table A.10）增强了 confidence。
- 但 ablation 的问题（W2）削弱了因果推断链。

**4.4 Non-Monotonic Refinement:**
- 这是论文最 nuanced 也最有争议的发现。
- Inverted-U 在 RSA 下 reproducible（across seeds, demos, metrics, benchmarks），但在 CKA 下不存在。
- "Training reshapes WHERE geometry peaks rather than HOW HIGH" 基于 best-vs-best Δ = +0.017 (n.s.)。严格来说，n.s. 结果不能用来支撑 "reshapes where" 的 claim——n.s. 只说明我们不能拒绝 "no difference" 的 null。

### Discussion (Section 5)
- "Speculative mechanistic interpretation" 段落的 speculative 标记值得肯定。
- "Early-layer parameters may suffice for instruction adaptation" 是有趣的 architectural implication 但缺少任何验证。
- Limitations 段落诚实但不完整（未提 probe methodology 的局限）。

### Appendix
- 组织良好，robustness 分析充分。
- OOD diagnostics（A.5）是有帮助的 but insufficient（见 W8）。
- QA probe（A.8.3）是一个有趣的补充，但 trained vs untrained 差异极小（86.3% vs 85.3%），不支持 "training creates richer task-relevant information at the readout" 的 claim。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-18T09:08:00.510137+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化 + Round 1 独立审稿', 'status': 'completed', 'activeForm': 'R1 R2 审稿意见均已收到'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '将 R1/R2 意见交叉转发'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化 + Round 1 独立审稿', 'status': 'completed', 'activeForm': 'R1 R2 审稿意见均已收到'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '将 R1/R2 意见交叉转发'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-18T09:08:00.510641+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-18T09:08:37.531910+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你意见分歧的地方。\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n**Score: Weak Reject (4/10), Confidence: High**\n\n## Strengths\n- S1: 实验设计严谨的阶乘控制（2×3 设计）\n- S2: 统计报告高标准（bootstrap CI, FDR, permutation test, seed/demo sensitivity）\n- S3: C2 routing reorganization 发现有价值（三条件梯度 30%-70% 阈值稳定）\n- S4: 方法互补性好（四种分析方法交叉验证 + CKA 分歧坦诚报告）\n- S5: Related Work 定位清晰（与 Grant 2026 三点差异明确）\n\n## Weaknesses\n\n**W1 [CRITICAL]: C1（token specialization）是架构必然结果，不构成实质新颖性**\n- Image tokens instruction-blind 由 causal mask + frozen encoder 保证\n- 将其列为三大贡献之首让审稿人质疑 novelty bar\n- 三大贡献中 C1 架构必然 + C3 metric-dependent → 实质新颖性只有 C2\n- 建议降格为 methodology validation\n\n**W2 [CRITICAL]: 单模型（OpenVLA-7B）+ 单 benchmark（LIBERO），泛化性严重不足**\n- Abstract 写 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 是对所有 VLA 的一般性声明\n- Grant 2026 覆盖 6 个 VLA，本文范围更窄\n- π₀ 用 flow matching，entry-exit routing pattern 可能完全不同\n\n**W3 [CRITICAL]: 缺少行为层面验证——representational finding 未与 task performance 连接**\n- 从未测量 ablation 对 task success rate 的影响\n- R² 是离线指标，不等于 behavioral importance\n- \"early-layer parameters may suffice for instruction adaptation\" 是 speculative，无实验支撑\n- 对 CoRL（机器人学习会议）是重大缺口\n\n**W4 [WARNING]: Ablation 解释逻辑不够 convincing**\n- dominant heads +0.042 vs random +0.077，\"dual function\" 解释需额外证据\n- 同样合理的解释：ablation 普遍通过移除 noise 提高 R²\n- z-score 基于仅 10 个 random subsets，统计功效有限\n\n**W5 [WARNING]: C3 metric-dependent，CKA 直接矛盾**\n- Linear CKA 单调递增，完全没有 inverted-U\n- 论文选择 RSA 的故事作为主叙事\n- NLP 领域已有 non-monotonic probing profile（Tenney 2019），增量有限\n\n**W6 [WARNING]: Abstract/Introduction 数据密度过高（~15 个数字），叙事可读性受损**\n\n**W7 [WARNING]: 缺少 Generative AI 使用声明（CoRL 2026 要求）**\n\n**W8 [WARNING]: conclusion.tex 存在但未被 main.tex 编译**\n\n**Minor**: M1 -ing phrases 约 30+ 处; M2 code release 声明可能泄露信息; M3 Table 2 caption 不自包含; M4 nostalgebraist2020 access date 暴露写作日期; M5 \"Speculative\" 标题过于自贬\n\n## Questions\n- Q1: 12% incidental attention 就够 100% classification，那 57.7% 的功能意义是什么？\n- Q2: RSA 最高 vs R² 最高指向不同 \"best\" representation，\"vision encoder quality\" 如何操作化？\n- Q3: Pretrained Llama-2 的 mid-depth routing 是 meaningful 还是 OOD artifact？\n- Q4: feature reconstruction pipeline baseline R² (0.517) 与 Table 3 (0.557-0.678) 不同，来源？\n\n## Missing References\nRizzardo 2026, Bills 2023, Templeton 2024, Nanda 2023, VLA fine-tuning efficiency 文献\n\n---\n\n请对以上每个 Weakness (W1-W8)、Question (Q1-Q4) 和 Missing References 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你意见分歧的地方。\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n**Score: Weak Reject (4/10), Confidence: High**\n\n## Strengths\n- S1: 实验设计严谨的阶乘控制（2×3 设计）\n- S2: 统计报告高标准（bootstrap CI, FDR, permutation test, seed/demo sensitivity）\n- S3: C2 routing reorganization 发现有价值（三条件梯度 30%-70% 阈值稳定）\n- S4: 方法互补性好（四种分析方法交叉验证 + CKA 分歧坦诚报告）\n- S5: Related Work 定位清晰（与 Grant 2026 三点差异明确）\n\n## Weaknesses\n\n**W1 [CRITICAL]: C1（token specialization）是架构必然结果，不构成实质新颖性**\n- Image tokens instruction-blind 由 causal mask + frozen encoder 保证\n- 将其列为三大贡献之首让审稿人质疑 novelty bar\n- 三大贡献中 C1 架构必然 + C3 metric-dependent → 实质新颖性只有 C2\n- 建议降格为 methodology validation\n\n**W2 [CRITICAL]: 单模型（OpenVLA-7B）+ 单 benchmark（LIBERO），泛化性严重不足**\n- Abstract 写 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 是对所有 VLA 的一般性声明\n- Grant 2026 覆盖 6 个 VLA，本文范围更窄\n- π₀ 用 flow matching，entry-exit routing pattern 可能完全不同\n\n**W3 [CRITICAL]: 缺少行为层面验证——representational finding 未与 task performance 连接**\n- 从未测量 ablation 对 task success rate 的影响\n- R² 是离线指标，不等于 behavioral importance\n- \"early-layer parameters may suffice for instruction adaptation\" 是 speculative，无实验支撑\n- 对 CoRL（机器人学习会议）是重大缺口\n\n**W4 [WARNING]: Ablation 解释逻辑不够 convincing**\n- dominant heads +0.042 vs random +0.077，\"dual function\" 解释需额外证据\n- 同样合理的解释：ablation 普遍通过移除 noise 提高 R²\n- z-score 基于仅 10 个 random subsets，统计功效有限\n\n**W5 [WARNING]: C3 metric-dependent，CKA 直接矛盾**\n- Linear CKA 单调递增，完全没有 inverted-U\n- 论文选择 RSA 的故事作为主叙事\n- NLP 领域已有 non-monotonic probing profile（Tenney 2019），增量有限\n\n**W6 [WARNING]: Abstract/Introduction 数据密度过高（~15 个数字），叙事可读性受损**\n\n**W7 [WARNING]: 缺少 Generative AI 使用声明（CoRL 2026 要求）**\n\n**W8 [WARNING]: conclusion.tex 存在但未被 main.tex 编译**\n\n**Minor**: M1 -ing phrases 约 30+ 处; M2 code release 声明可能泄露信息; M3 Table 2 caption 不自包含; M4 nostalgebraist2020 access date 暴露写作日期; M5 \"Speculative\" 标题过于自贬\n\n## Questions\n- Q1: 12% incidental attention 就够 100% classification，那 57.7% 的功能意义是什么？\n- Q2: RSA 最高 vs R² 最高指向不同 \"best\" representation，\"vision encoder quality\" 如何操作化？\n- Q3: Pretrained Llama-2 的 mid-depth routing 是 meaningful 还是 OOD artifact？\n- Q4: feature reconstruction pipeline baseline R² (0.517) 与 Table 3 (0.557-0.678) 不同，来源？\n\n## Missing References\nRizzardo 2026, Bills 2023, Templeton 2024, Nanda 2023, VLA fine-tuning efficiency 文献\n\n---\n\n请对以上每个 Weakness (W1-W8)、Question (Q1-Q4) 和 Missing References 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-18T09:09:09.462578+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31930
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-18T09:09:09.564281+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你意见分歧的地方。\n\n---\n\n# Reviewer 1 — Round 1 Review\n\n**Score: 5 (Marginally below acceptance threshold), Confidence: 4**\n\n## Strengths\n- S1: 系统性实验框架设计（三条件因子控制）\n- S2: 多角度互验（RSA + probes + attention + cross-instruction，含 linear probe 复制）\n- S3: 丰富的 robustness 分析（distance metric, demo subsampling, seed, threshold, cross-benchmark）\n- S4: CKA 分歧的诚实处理\n- S5: 与 behavioral 文献的连接（Grant 2026, Häon 2025）\n\n## Weaknesses\n\n**W1 [CRITICAL]: Cross-instruction probe 近乎 trivially easy，削弱核心贡献新颖性**\n- 10-way classification 在 ALL THREE 条件（trained/pretrained/untrained）L1 均达到 99.6-100%\n- 10 条 LIBERO-Goal 指令在 token 层面差异巨大，linear classifier 只需最微弱残留即可 100%\n- 更有信息量的是 DECAY PATTERN（untrained 100%→82%, trained 100%→100%），但论文将 \"100% from L1\" 作为主要发现\n- 建议增加更难的 probe task（paraphrase 指令、语义近似指令）\n\n**W2 [CRITICAL]: L1 head ablation 因果推断方向存在根本性问题**\n- Ablating ANY 24/32 heads 都 INCREASE R²（dominant +0.042, random +0.077）\n- 如果 dominant heads 功能重要，ablation 应 DECREASE R²\n- \"dual function\" 是 post-hoc rationalization；等效替代解释：L1 heads 普遍添加噪声\n- Random subset 仅 N=10，z-test 统计功效极低\n- 建议：细粒度 ablation curve (4/8/12/16/20/24/28), selective ablation (只移除 instruction attention), 增加 random subsets ≥100\n\n**W3 [CRITICAL]: Action probe train/test split 未说明，overparameterized MLP probe R² 可信度存疑**\n- MLP probe N/params ≈ 0.06（overparameterized），R² 在哪个数据集上计算未明确\n- Linear probe gap (Δ=+0.324 at L14) vs MLP probe gap (Δ=+0.015 at L8) 相差 ~20 倍 → MLP 过强压缩条件差异\n- N=63,228 中时间步高度自相关，有效样本量远小于名义值\n- Bootstrap CI 基于独立假设，可能严重低估不确定性\n\n**W4 [WARNING]: RSA 统计推断中的依赖性问题**\n- N(N-1)/2 pairwise distances 不独立，标准 bootstrap 低估 variance\n- Permutation test 仅测试 \"是否存在 ANY structure\"，不测试条件间差异\n- same-layer L12 比较存在 selection bias（选择差异最大的层）\n- 建议 Mantel test 或 stimulus-level bootstrap\n\n**W5 [WARNING]: RSA vs CKA 分歧对 Finding 3 影响被低估**\n- Linear CKA 完全反转 RSA 排序和 per-layer profile\n- 论文未论证为何 rank-order geometry 对 action prediction 更相关\n- 三个 metrics 给三种故事，论文选择 RSA\n\n**W6 [WARNING]: 单模型单 benchmark 泛化性不足**\n- 所有实验仅 OpenVLA-7B + LIBERO（10 个 tabletop tasks）\n- 无其他 VLA、无 real-robot、无多样化任务域\n- LIBERO-Spatial 仍在 LIBERO 框架内\n\n**W7 [WARNING]: 缺少行为验证**\n- 所有发现在 representation space，无连接到 task success rate\n- \"early-layer parameters may suffice\" 无验证\n- 对 CoRL 的 practical value 有限\n\n**W8 [INFO]: Pretrained Llama-2 visual token 处理是否有意义**\n- 非退化不等于有意义处理\n- 建议用 random noise tokens 替代 visual tokens 作 diagnostic\n\n## Questions\n- Q1: R² 在 training set 还是 held-out test set 上计算？train/test split 策略？\n- Q2: 所有 head ablation 都 INCREASE R²，是否意味着 L1 heads 对 action prediction 有害？\n- Q3: 如果用更难的 probe task（paraphrase 指令），结果是否不同？\n- Q4: Linear probe gap (~20× MLP probe gap) 对结果解释有什么影响？\n- Q5: Bootstrap CI 的 resampling unit？如何处理自相关？\n- Q6: 能否提供 RSA 条件间差异的 Mantel test？\n\n## Missing References\n- Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\"\n- Zheng et al. (2024) \"3D-VLA\"\n- Nili et al. (2014) \"A Toolbox for Representational Similarity Analysis\"\n\n---\n\n请对以上每个 Weakness (W1-W8)、Question (Q1-Q6) 和 Missing References 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注与你意见分歧的地方。\n\n---\n\n# Reviewer 1 — Round 1 Review\n\n**Score: 5 (Marginally below acceptance threshold), Confidence: 4**\n\n## Strengths\n- S1: 系统性实验框架设计（三条件因子控制）\n- S2: 多角度互验（RSA + probes + attention + cross-instruction，含 linear probe 复制）\n- S3: 丰富的 robustness 分析（distance metric, demo subsampling, seed, threshold, cross-benchmark）\n- S4: CKA 分歧的诚实处理\n- S5: 与 behavioral 文献的连接（Grant 2026, Häon 2025）\n\n## Weaknesses\n\n**W1 [CRITICAL]: Cross-instruction probe 近乎 trivially easy，削弱核心贡献新颖性**\n- 10-way classification 在 ALL THREE 条件（trained/pretrained/untrained）L1 均达到 99.6-100%\n- 10 条 LIBERO-Goal 指令在 token 层面差异巨大，linear classifier 只需最微弱残留即可 100%\n- 更有信息量的是 DECAY PATTERN（untrained 100%→82%, trained 100%→100%），但论文将 \"100% from L1\" 作为主要发现\n- 建议增加更难的 probe task（paraphrase 指令、语义近似指令）\n\n**W2 [CRITICAL]: L1 head ablation 因果推断方向存在根本性问题**\n- Ablating ANY 24/32 heads 都 INCREASE R²（dominant +0.042, random +0.077）\n- 如果 dominant heads 功能重要，ablation 应 DECREASE R²\n- \"dual function\" 是 post-hoc rationalization；等效替代解释：L1 heads 普遍添加噪声\n- Random subset 仅 N=10，z-test 统计功效极低\n- 建议：细粒度 ablation curve (4/8/12/16/20/24/28), selective ablation (只移除 instruction attention), 增加 random subsets ≥100\n\n**W3 [CRITICAL]: Action probe train/test split 未说明，overparameterized MLP probe R² 可信度存疑**\n- MLP probe N/params ≈ 0.06（overparameterized），R² 在哪个数据集上计算未明确\n- Linear probe gap (Δ=+0.324 at L14) vs MLP probe gap (Δ=+0.015 at L8) 相差 ~20 倍 → MLP 过强压缩条件差异\n- N=63,228 中时间步高度自相关，有效样本量远小于名义值\n- Bootstrap CI 基于独立假设，可能严重低估不确定性\n\n**W4 [WARNING]: RSA 统计推断中的依赖性问题**\n- N(N-1)/2 pairwise distances 不独立，标准 bootstrap 低估 variance\n- Permutation test 仅测试 \"是否存在 ANY structure\"，不测试条件间差异\n- same-layer L12 比较存在 selection bias（选择差异最大的层）\n- 建议 Mantel test 或 stimulus-level bootstrap\n\n**W5 [WARNING]: RSA vs CKA 分歧对 Finding 3 影响被低估**\n- Linear CKA 完全反转 RSA 排序和 per-layer profile\n- 论文未论证为何 rank-order geometry 对 action prediction 更相关\n- 三个 metrics 给三种故事，论文选择 RSA\n\n**W6 [WARNING]: 单模型单 benchmark 泛化性不足**\n- 所有实验仅 OpenVLA-7B + LIBERO（10 个 tabletop tasks）\n- 无其他 VLA、无 real-robot、无多样化任务域\n- LIBERO-Spatial 仍在 LIBERO 框架内\n\n**W7 [WARNING]: 缺少行为验证**\n- 所有发现在 representation space，无连接到 task success rate\n- \"early-layer parameters may suffice\" 无验证\n- 对 CoRL 的 practical value 有限\n\n**W8 [INFO]: Pretrained Llama-2 visual token 处理是否有意义**\n- 非退化不等于有意义处理\n- 建议用 random noise tokens 替代 visual tokens 作 diagnostic\n\n## Questions\n- Q1: R² 在 training set 还是 held-out test set 上计算？train/test split 策略？\n- Q2: 所有 head ablation 都 INCREASE R²，是否意味着 L1 heads 对 action prediction 有害？\n- Q3: 如果用更难的 probe task（paraphrase 指令），结果是否不同？\n- Q4: Linear probe gap (~20× MLP probe gap) 对结果解释有什么影响？\n- Q5: Bootstrap CI 的 resampling unit？如何处理自相关？\n- Q6: 能否提供 RSA 条件间差异的 Mantel test？\n\n## Missing References\n- Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\"\n- Zheng et al. (2024) \"3D-VLA\"\n- Nili et al. (2014) \"A Toolbox for Representational Similarity Analysis\"\n\n---\n\n请对以上每个 Weakness (W1-W8)、Question (Q1-Q6) 和 Missing References 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-18T09:09:11.375761+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1811
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-18T09:09:18.853377+00:00_

交叉分享任务已分派。两位 Reviewer 正在相互审阅对方意见并逐条回应。等待回复中。

**Round 1 初步共识观察**（两位 Reviewer 共同指出的问题）：
- C1 token specialization 的 novelty 不足（架构必然 + probe trivially easy）
- 单模型单 benchmark 泛化性问题
- 缺少 behavioral validation
- RSA vs CKA 分歧对 C3 的影响
- Ablation 解释逻辑的替代假说

R1 额外关注了方法论层面的技术问题（train/test split、bootstrap 依赖性、MLP overparameterization），R2 额外关注了格式合规和叙事质量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 433 · 2026-05-18T09:09:21.695165+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评审总结**:

- **评分**: 5/10（Marginally below acceptance threshold）
- **信心**: 4/5

**核心问题（3 个 CRITICAL）**:
1. **Cross-instruction probe trivially easy** — untrained 模型在 L1 也达 100%，10-way 分类任务难度不足以支撑 Finding 1 的 contribution 级别
2. **L1 ablation 因果推断方向有问题** — 所有 ablation（dominant 和 random heads）都提高 R²，说明 L1 大多数 heads 对 action prediction 是 net-negative 的，"dual function" 解释是 post-hoc rationalization
3. **Action probe train/test split 未说明** — overparameterized MLP probe (N/params ≈ 0.06) 的 R² 在不清楚评估集的情况下不可信

**次要问题（4 个 WARNING）**: RSA 统计依赖性未处理、CKA 分歧对 Finding 3 影响被低估、单模型单 benchmark 泛化性不足、缺少行为验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 434 · 2026-05-18T09:09:27.316261+00:00_

交叉分享任务已分派给两位 Reviewer，等待交叉回应返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 435 · 2026-05-18T09:10:17.513579+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见

---

## Weaknesses 逐条回应

**[AGREE] R2-W1: C1 是架构必然结果，不构成实质新颖性**

完全同意。这与我的 W1 一致。补充一点 R2 未强调的证据：Table 1 显示 untrained model 在 L1 也达到 100% classification，Appendix A.8.1 作者自己承认 "even incidental attention (~12%) suffices for linear classification at L1"。将 trivially verifiable 的架构属性列为三大贡献之首确实降低了 novelty 感知。降格为 methodology validation / sanity check 是合理建议。

---

**[AGREE] R2-W2: 单模型 + 单 benchmark，泛化性不足**

同意，与我的 W6 一致。补充：LIBERO-Spatial 作为 cross-benchmark validation（Appendix A.4）仍在 LIBERO 框架内，任务域相同（tabletop manipulation），不能算真正的泛化验证。R2 指出 Grant 2026 覆盖了 6 个 VLA 是有力对比——本文范围确实更窄。Abstract 中 "instruction routing reorganization is the primary learned contribution of VLA fine-tuning" 的一般性措辞与单模型证据不匹配。

---

**[AGREE] R2-W3: 缺少行为层面验证**

同意，与我的 W7 一致。对于 CoRL 这个强调 robot learning 实际应用的会议，representational analysis 不连接 task performance 是重大缺口。R2 正确指出 "early-layer parameters may suffice for instruction adaptation"（Discussion Section 5）是 speculative 的。即使是 pilot 级别的 rollout 验证（如 L1 ablation → success rate 变化）也能显著提升论文价值。

---

**[AGREE with stronger formulation] R2-W4: Ablation 解释逻辑不够 convincing**

同意 R2 的判断，但我认为问题比 R2 所述更严重。R2 提到 "同样合理的解释：ablation 普遍通过移除 noise 提高 R²"，这是正确的，但更根本的问题是：dominant-head ablation (+0.042) 和 random-head ablation (+0.077) 都是 POSITIVE（R² 增加）。如果 instruction-dominant heads 真的具有作者声称的功能重要性，ablation 应该 DECREASE R²。所有 ablation 都提高 R² 这一事实意味着 L1 的 75% heads 对 action prediction 是 net-negative 的。"dual function" 解释是 post-hoc rationalization，且仅基于 N=10 random subsets 的 z-test。见我的 W2 获取更详细分析。

---

**[AGREE] R2-W5: C3 metric-dependent，CKA 直接矛盾**

同意，与我的 W5 一致。补充一点：R2 提到 "NLP 领域已有 non-monotonic probing profile（Tenney 2019）"，这个 incremental novelty 的论点成立。不过公平地说，本文在 VLA 领域（而非 NLP）做这个分析是有增量的，因为 VLA 的 multimodal fusion + action prediction 设定与 NLP 不同。关键问题仍然是 metric-dependency：论文未提供理论或实证论据解释为何 RSA（rank-order preservation）比 CKA（covariance structure）更适合度量 action-relevant representational quality。

---

**[REBUT] R2-W6: Abstract/Introduction 数据密度过高**

部分不同意。数据密度高确实影响可读性，但对于一篇分析型论文（与 methods 论文不同），Abstract 中报告关键数值是合理的。问题不在于数字多，而在于哪些数字 informative：例如 "$z = -2.73$" 属于过细的统计细节不适合 Abstract，但 "100% instruction classification from L1" 和 "R² +0.069" 这类数字是核心 claims 的量化支撑，应该保留。这是写作风格问题（WARNING 级别偏高），而非方法论缺陷。建议降级为 [INFO]。

---

**[AGREE] R2-W7: 缺少 Generative AI 使用声明**

同意。CoRL 2026 明确要求 Generative AI 使用声明（见 Instruction for Authors: "Generative AI use must be disclosed"）。main.tex 中未包含此声明。这是一个 desk reject risk 的格式问题。

---

**[AGREE] R2-W8: conclusion.tex 存在但未被 main.tex 编译**

同意。我验证了 main.tex 的 \input 列表：introduction → related_work → method → experiments → discussion → bibliography → appendix。conclusion.tex 文件存在（含 \section{Conclusion}）但未被 \input。这意味着编译后的论文缺少独立的 Conclusion section。虽然 Discussion（Section 5）的最后一段有总结性内容，但缺少独立 Conclusion 不符合学术论文惯例。对 CoRL 不一定是格式违规（官方模板无强制要求），但结构不完整。

---

## Questions 逐条回应

**[AGREE] R2-Q1: 12% attention 够 100% classification，57.7% 的功能意义是什么？**

这是一个尖锐的好问题。与我的 W1 直接相关。如果 12% incidental attention 已足够 100% 分类，那么 VLA training 将 text attention 提升到 57.7% 的功能意义是什么？论文未回答这个关键问题。可能的答案是：更高的 attention 比例服务于更细粒度的 instruction-conditioned processing（不仅是"识别哪条指令"，而是"如何根据指令调整 action"），但这需要额外实验验证（如 instruction-conditioned action prediction accuracy vs. attention fraction 的相关性）。

---

**[AGREE] R2-Q2: RSA 最高 vs R² 最高指向不同 "best" representation**

同意这是一个重要问题。Table 3 显示 DINOv2 cls_token RSA 最高（0.692）但 R² 不是最高（0.634），而 VLA trained readout R² 最高（0.678）但 RSA 不是最高（0.643）。Conclusion 声称 "vision encoder quality emerges as a key design lever" 但两个 metrics 对 "quality" 的定义不一致。这个 claim 需要操作化定义。

---

**[AGREE with caveat] R2-Q3: Pretrained Llama-2 的 mid-depth routing 是 meaningful 还是 OOD artifact？**

这与我的 W8 一致。但需要 nuance：Appendix A.5 的 OOD diagnostics（activation magnitude, cosine similarity progressive decline, PC variance stability）确实排除了 degenerate representations 的可能性。问题是 "non-degenerate" 不等于 "meaningful"。如果 Llama-2 对 random noise tokens 也产生类似的 mid-depth routing pattern，那么 pretrained 条件的解释价值大幅降低。我在自己的审稿中建议了这个 control experiment。

---

**[REBUT] R2-Q4: Feature reconstruction pipeline baseline R² 差异**

这个问题论文已明确回答。Section 4.3 有显式脚注："R² values in this random-subset analysis differ from Table 3 (baseline 0.557) due to the feature reconstruction pipeline used for head-level manipulation; all comparisons are within-experiment."（experiments.tex line 79）。Ablation 使用 feature reconstruction pipeline 重建 per-head contributions，引入了 reconstruction error，导致 baseline R² 低于直接 extraction pipeline。关键是所有 ablation 比较都在同一 pipeline 内进行，internal validity 不受影响。R2 可能遗漏了这个脚注。

---

## Missing References 回应

**[AGREE] Bills 2023 / Templeton 2024 / Nanda 2023**: 这些 mechanistic interpretability 的标志性工作（neuron interpretation, scaling monosemanticity, TransformerLens）与本文的 Related Work "Mechanistic interpretability in transformers" 段落直接相关。当前引用侧重 circuit-level 和 attention head 分析（Elhage 2021, Olsson 2022, Wang 2023），缺少 feature/neuron-level 的代表性工作。不过这些遗漏对论文核心论点影响有限——它们是 background completeness 问题而非 missing direct comparisons。

**[PARTIAL AGREE] VLA fine-tuning efficiency 文献**: 如果论文的 Discussion 要做 "early-layer parameters may suffice for instruction adaptation" 的推测，引用 LoRA/adapter 在 VLA 上的应用（如 parameter-efficient fine-tuning 文献）会增强上下文。但这属于 speculative implication 的 supporting context，非核心缺失。

**[CANNOT VERIFY] Rizzardo 2026**: 未查到此引用的具体信息，无法判断其相关性。

---

## 总结：与 R2 的一致性和分歧

**高度一致（6/8 Weaknesses）**: W1(C1 trivial), W2(generalization), W3(behavioral validation), W4(ablation logic), W5(CKA divergence), W7(GenAI statement), W8(conclusion.tex)。

**主要分歧**:
- W4: 我认为问题比 R2 所述更严重（ablation 方向性问题，不仅是 "解释不够 convincing"）。
- W6: 我认为数据密度问题 severity 偏高，建议降级为 INFO。
- Q4: R2 提问的 baseline R² 差异已被论文脚注解释。

**整体评分对比**: R2 给 4/10 (Weak Reject)，我给 5/10 (Marginally below threshold)。差距主要在于我对 Finding 2（routing reorganization, three-condition gradient）的评价稍高——这是论文中最有说服力的贡献，threshold sensitivity 和 cross-benchmark replication 增强了可信度。但 W2(ablation) 和 W3(no behavioral validation) 的联合影响使我也倾向于 below threshold。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-18T09:10:24.708280+00:00_

收到 Reviewer 1 的交叉回应。R1 与 R2 在 6/8 个 Weakness 上高度一致，主要分歧在 W4 严重程度和 W6 级别判定。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 437 · 2026-05-18T09:10:27.513625+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。与 Reviewer 2 在 6/8 个 Weaknesses 上高度一致，主要分歧在 W4（我认为 ablation 问题更严重）和 W6（我认为数据密度问题 severity 偏高应降级）。对 Q4 做了 REBUT，因为论文脚注已明确解释了 baseline R² 差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 438 · 2026-05-18T09:10:32.471493+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 48

## Round 48

30 recorded events


### User

_source line 439 · 2026-05-18T09:11:07.149072+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 Round 1 意见

---

## Weaknesses 逐条回应

**[AGREE] R1-W1: Cross-instruction probe trivially easy**
同意这是 C1 新颖性问题的另一个维度。我的 R2-W1 从架构层面论证 C1 是 trivial（causal mask + frozen encoder），R1 从 probe task difficulty 层面论证同一结论。两个角度互补：不仅架构保证了 image token instruction-blindness，且 10 条 LIBERO 指令在 token 空间差异巨大，使 readout token 的 100% classification 也接近 trivial。R1 指出 untrained 模型在 L1 也达到 100%（Table 1），这直接说明该 probe task 的 discriminative power 不足以区分有意义的表征差异和 incidental signal leakage。

R1 建议的 paraphrase/语义近似指令 probe 是一个有价值的加强方向，能真正测试指令理解的深度而非表面 token 差异。

补充一点：论文 Appendix K.3 的 QA probe（progress + subtask classification）才是更有信息量的 probe，但被放在 Appendix 且 trained vs untrained 差异仅 1pp（86.3% vs 85.3%, Table 12），进一步削弱了 training effect 在 readout token 上的 functional significance。

**[AGREE] R1-W2: L1 head ablation 因果推断方向问题**
强烈同意。这是我 R2-W4 的更尖锐表述。核心逻辑问题：如果 dominant heads 真正承担 "dual routing-encoding function"，ablation 应导致 R² 下降（information loss），而非上升。所有 ablation 都 increase R² 这一事实，最简洁的解释是 L1 heads 整体对 downstream probe 有轻微 interference，而非 functional contribution。

R1 提出的 alternative explanation（"L1 heads 普遍添加噪声"）比论文的 "dual function" 解释更 parsimonious。论文选择了更复杂的解释但未提供足够证据排除更简单的解释，违反 Occam's razor。

R1 建议的细粒度 ablation curve（4/8/12/.../28 heads）和 selective ablation（只移除 instruction attention component）都是 constructive 的。特别是 selective ablation——如果能零化 instruction attention 但保留其他 attention patterns，就能真正测试 instruction routing 的 causal role。

N=10 random subsets 的统计功效问题我也在 R2-W4 中指出。z=-2.73 在 N=10 下虽然名义 p=0.003，但分布假设（正态近似）在如此小样本下不可靠。

**[AGREE] R1-W3: Probe train/test split 和 overparameterization 问题**
同意这是一个被忽视的方法论漏洞。论文 Section 4.1 提到 "early stopping patience 5"，暗示有 validation set，但从未明确说明：(a) train/test split ratio，(b) split 是 random 还是 per-task/per-demonstration，(c) R² 报告在 test set 还是 train set 上。

R1 关于时间步自相关的观点尤其重要。63,228 observations 来自 50 demonstrations × 10 tasks × ~127 timesteps。相邻时间步的 representations 和 actions 高度相关（机器人运动的连续性），effective sample size 远小于 63K。如果 train/test split 是 random timestep split（而非 demonstration-level split），则 test set 几乎必然包含与 training set 近乎相同的数据点（相邻帧），导致 R² 严重高估。

Linear vs MLP probe 的 20× gap（Δ=0.324 vs Δ=0.015）是一个 red flag。这说明 MLP probe 的非线性容量足以从 untrained representations 中也"解救"大量 action information，压缩了 trained/untrained 的差异。论文在 Appendix F 承认 "MLP nonlinearity partially rescues degraded representations"，但没有讨论这对主文所有 MLP probe 结论的影响——如果 MLP probe 系统性地低估 training effect，Table 3 的 Δ=+0.069 可能是 attenuated 的。反过来说，如果 linear probe 是更 fair 的指标，则论文应以 linear probe 为主，MLP probe 为辅。

**[AGREE] R1-W4: RSA 统计推断中的依赖性问题**
同意。RDM 的 N(N-1)/2 pairwise distances 之间存在 structural dependency（每个 observation 参与 N-1 个 pair），标准 bootstrap 假设 independent sampling，会 underestimate variance。这是 RSA 文献中已知的问题（Nili et al. 2014 明确讨论了此点，这也是 R1 建议引用该文的原因）。

R1 建议的 Mantel test 或 stimulus-level bootstrap（以 observation 而非 pair 为 resampling unit）是正确的处理方式。论文当前的 bootstrap 可能使 CI 过窄，导致一些 "significant" 的 Δ 在正确统计下变为 n.s.。这尤其影响 Table 5 中 best-vs-best image_mean Δ=+0.017 的判断（当前已是 n.s.；如果 CI 更宽，则更加 n.s.）以及 same-layer L12 Δ=+0.079 的 significance。

不过，permutation test（Appendix H.3）的 15-23 SD 偏移足以确认 representation-action alignment 的存在性（observed ρ vs null），即使不完美也不至于完全失效。R1 说 "permutation test 仅测试 ANY structure 而非条件间差异" 是准确的。

**[AGREE] R1-W5: RSA vs CKA 分歧对 Finding 3 影响被低估**
完全同意，与我的 R2-W5 一致。补充一点：论文选择 RSA 的理由（Section 3.6 "Why RSA over CKA"）是 "Spearman rank correlation is scale-invariant and robust to monotonic transformations"，但这是 general methodological argument，未论证为何 rank-order geometry（而非 global covariance structure）对 action prediction 更 relevant。如果目标是 action prediction，probe R² 才是直接指标；如果目标是 geometric characterization，则两种 metric 同等 valid，论文不能只报一种。

关键的叙事问题：如果作者在写论文时先看到 CKA 结果（monotonic increase），他们是否还会提出 "non-monotonic refinement" 作为 C3？Metric selection 看起来是 results-driven 而非 hypothesis-driven。

**[AGREE] R1-W6: 单模型单 benchmark 泛化性不足**
与我的 R2-W2 完全一致。无额外补充。

**[AGREE] R1-W7: 缺少行为验证**
与我的 R2-W3 完全一致。无额外补充。

**[AGREE] R1-W8: Pretrained Llama-2 visual token 处理是否有意义**
同意，与我的 R2-Q3 相关。R1 建议的 random noise token diagnostic 是一个 clean 的实验：如果 Llama-2 base 在 random noise input 上也显示 mid-depth routing concentration（L9-L16 头数类似），则该 pattern 是 pretrained weights 的 generic 行为，与 visual token 无关，C2 中 "language pretraining seeds partial instruction routing" 的 claim 就不成立。

Appendix G 的三个 diagnostics（activation magnitude, cosine similarity, PC variance）只证明 non-degenerate，不证明 meaningful processing。这是一个 necessary but not sufficient 的验证。

---

## Questions 逐条回应

**[AGREE] R1-Q1: R² 在哪个数据集上计算？**
完全同意这需要明确。我在 R1-W3 的回应中已详述。如果是 train set R²，则所有 probe 结果的 magnitude 需要大幅打折。

**[AGREE] R1-Q2: 所有 ablation 都 increase R²，是否 L1 heads 对 action prediction 有害？**
同意这是需要回答的关键问题。见 R1-W2 回应。论文需要解释为什么一个 supposedly important layer 的 head ablation 不会 hurt performance。

**[AGREE] R1-Q3: 更难的 probe task 是否会改变结论？**
同意。当前 10-way classification 在所有条件下都近乎 trivial，无法 discriminate fine-grained differences。

**[AGREE] R1-Q4: Linear vs MLP probe gap 的 20× 差异**
同意这需要解释。见 R1-W3 回应中的分析。

**[AGREE] R1-Q5: Bootstrap resampling unit 和自相关处理**
同意。论文未说明 bootstrap 的 resampling unit 是 observation-level 还是 demonstration-level。如果是 observation-level，时间自相关导致 effective sample size 远小于 63K，CI 被严重低估。

**[REBUT] R1-Q6: RSA 条件间差异的 Mantel test**
部分 rebut。Mantel test 主要用于测试两个 distance matrices 之间的 association（即论文已在做的 representation-action RDM correlation），而非条件间差异。对于 trained vs untrained 的 RSA Δ 比较，更合适的方法是 stimulus-level bootstrap（以 demonstration 或 task 为 resampling unit），或者直接用 per-task RSA 值做 paired test（论文已报告 per-task 结果用于 bootstrap）。但 R1 的核心关切——标准 bootstrap 低估 variance——是完全正确的。

---

## Missing References 回应

**[AGREE] Hewitt & Liang (2019) "Designing and Interpreting Probes with Control Tasks"**
强烈同意。这篇论文直接讨论了 probe 设计中的 control task 方法论，与本文的 probing framework 高度相关。特别是其 "selectivity" 概念（probe accuracy minus control task accuracy）可以 formalize R1-W1 提出的 "probe task too easy" 问题。论文当前的 bib 中有 Belinkov 2022 和 Hewitt 2019（structural probe），但缺少这篇关于 probe design 的关键方法论文献。

**[REBUT] Zheng et al. (2024) "3D-VLA"**
部分 rebut。3D-VLA 是一个 VLA 架构论文，使用 3D representations。与本文的 representational analysis 主题关联度有限。Related Work 的 VLA 段落已引用 RT-2、OpenVLA、π₀ 等核心架构，3D-VLA 的缺失不构成重大遗漏。不过如果空间允许，加上也无妨。

**[AGREE] Nili et al. (2014) "A Toolbox for Representational Similarity Analysis"**
同意。这是 RSA 方法论的核心参考，特别是关于 RDM 统计推断（pairwise dependency 问题、noise ceiling 估计）。论文使用 RSA 作为主要 geometric metric 但只引用 Kriegeskorte 2008 的原始论文，缺少 Nili 2014 对 RSA 统计实践的重要补充。

---

## 总结：与 Reviewer 1 的共识和分歧

**高度共识（6/8 Weaknesses）**：
- C1 新颖性不足（R1-W1 + R2-W1）
- Ablation 逻辑问题（R1-W2 + R2-W4）
- 单模型泛化性（R1-W6 + R2-W2）
- 缺少行为验证（R1-W7 + R2-W3）
- RSA/CKA 分歧（R1-W5 + R2-W5）
- Pretrained OOD 问题（R1-W8 + R2-Q3）

**R1 新增的重要关切**：
- Probe train/test split 和 overparameterization（R1-W3）——这是我遗漏的重要方法论问题
- RSA pairwise dependency 的统计推断（R1-W4）——比我的审查更深入的统计关切
- Linear vs MLP probe 20× gap 的 implication（R1-Q4）——有价值的观察

**我的 R2 审稿中 R1 未覆盖的关切**：
- Abstract/Introduction 数据密度过高、叙事可读性差（R2-W6）
- 格式问题：缺少 Generative AI disclosure（R2-W7）、conclusion.tex 未编译（R2-W8）

**总体评分对比**：R1 给 5/10（marginally below），我给 4/10（weak reject）。分差主要来自我对 novelty 的更严格判断——我认为 C1+C3 的 novelty 问题使论文实质上只有 C2 一个 contribution，这对 CoRL 不够。R1 对方法论问题（probe design, statistical inference）的关切比我更深入，是有价值的补充。

综合两位 reviewer 意见，**核心问题一致**：novelty 受限 + 单模型 + 无 behavioral validation。分歧仅在严重程度判断上。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-18T09:11:36.554834+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化 + Round 1 独立审稿', 'status': 'completed', 'activeForm': 'R1 R2 审稿意见均已收到'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉回应已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': 'Round 1 已收敛'}, {'content': 'Step 4a: 读论文验证关键声明', 'status': 'in_progress', 'activeForm': '验证论文中的关键声明'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'pending', 'activeForm': '更新 review_issues.yaml'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化 + Round 1 独立审稿', 'status': 'completed', 'activeForm': 'R1 R2 审稿意见均已收到'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉回应已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': 'Round 1 已收敛'}, {'content': 'Step 4a: 读论文验证关键声明', 'status': 'in_progress', 'activeForm': '验证论文中的关键声明'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'pending', 'activeForm': '更新 review_issues.yaml'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-18T09:11:36.605562+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-18T09:11:41.281768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-18T09:11:41.734981+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we verify and quantify architecture-expected token specialization: image tokens are instruction-blind (classification at chance, $10\%$, across all layers and conditions), consistent with the causal mask and frozen encoder, while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to entry-layer routing (L0--L1: 21--24 heads) with exit-layer re-engagement (L31: 18 heads); instruction classification reaches $99.6\%$ at L1 (vs.\ pretrained $80.2\%$), and L1 ablation reveals that instruction-dominant heads serve dual routing-encoding function (random-subset control, $z = -2.73$, L1-confined). Untrained models show zero instruction-dominant heads throughout.
6	Third, vision encoder representations follow a metric-dependent non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L14; RSA confirms but CKA diverges; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of VLA fine-tuning.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-18T09:11:41.735346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-18T09:11:42.136837+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	While the decoder-only architecture imposes structural constraints on information flow (the causal mask prevents image tokens from attending to subsequent instruction tokens), how VLA fine-tuning reshapes the routing and integration of multimodal information within the LLM backbone remains uncharacterized.
6	
7	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
8	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
9	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
10	
11	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
12	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
13	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\c
…[truncated 2511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-18T09:11:42.137295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-18T09:11:42.238168+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). The MLP probe is overparameterized ($N/\text{params} \approx 0.06$); early stopping mitigates overfitting, and all patterns reproduce with a linear probe ($N/\text{params} \approx 2.2$; Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are in
…[truncated 11778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-18T09:11:46.356407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-18T09:11:46.889970+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind (causal mask, frozen encoder); the readout is the sole convergence point.
6	Training shifts routing from mid-depth to entry-exit (L0--L1, L31), with effects at the readout ($R^2$ $+0.069$) rather than images ($\Delta \leq 1.7\%$).
7	
8	\paragraph{Mechanism-behavior connection.}
9	Image-token instruction-blindness explains the visual dominance reported by Grant et al.~\cite{grant2026}: actions rely on readout-token conditioning.
10	Under RSA, DINOv2 achieves the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$). This gap points to instruction-conditioned integration rather than enhanced geometry.
11	
12	\paragraph{Speculative mechanistic interpretation.}
13	Per-layer RSA shows a bifurcation after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually while image\_mean drops sharply ($\to 0.422$), consistent with mid-layer integration and deep-layer compression; testing this requires interventions beyond L1.
14	
15	\paragraph{Architectural implications.}
16	L1 attention ablation (\S\ref{sec:learned_routing}) reveals that instruction routing is functionally integrated with action encoding: instruction-dominant heads yield smaller $R^2$ changes than random subsets ($z = -2.73$), indicating dual function rather than capacity competition. The effect is L1-confined ($|\Delta R^2| < 0.02$ at deeper layers); routing concentration at L0--L1 suggests early-layer parameters may suffice for instruction adaptation, though behavioral validation is needed.
17	
18	\paragraph{Limitations and scope.}
19	We study OpenVLA-7B on LIBERO. OpenVLA shares the dominant VLA design (frozen encoder, MLP projector, autoregressive LLM) with RT-2~\cite{brohan2023_rt2} and $\pi_0$~\cite{black2024_pi0}; C1 follows from shared architectural constraints, but C2 may differ across backbone scales, de
…[truncated 445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 533
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-18T09:11:46.890467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-18T09:11:46.963662+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), a Multi-Layer Perceptron (MLP) projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B~\cite{touvron2023_llama2} language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (no task-specific fine-tuning) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tabletop tasks, 50 demonstrations each).
12	To disentangle the contributions of language pretraining and VLA fine-tuning, we compare three LLM conditions: (1)~VLA-trained (the released checkpoint), (2)~Llama-2 base (the pretrained LLM backbone without VLA fine-tuning), and (3)~untrained (all 6.74B LLM parameters reinitialized via \texttt{from\_config()}).
13	All three conditions share the same frozen vision encoder and projector architecture.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the activation at the final pre-action token position at each layer;
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} 
…[truncated 4157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 73
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-18T09:11:51.031685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-18T09:11:51.083665+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing to locate factual associations in specific MLP layers, and Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for tracking per-layer prediction evolution through learned projections.
15	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.
16	Our Layer-1 at
…[truncated 3059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-18T09:11:51.487253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-18T09:11:51.537876+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 1947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-18T09:12:07.125469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-18T09:12:07.226646+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-3 历史 issues（全部 resolved）
4	  # ============================================================
5	  - id: R1-N1-old
6	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 2
12	    mentions:
13	      - round: 1
14	        reviewers: [1, 2, 3]
15	        note: "全票共识。需增加 Llama-2 base checkpoint 作为中间对照"
16	      - round: 2
17	        reviewers: [1, 2, 3]
18	        note: "PARTIALLY_RESOLVED: acknowledge confound 但无数据"
19	    action_items:
20	      - round: 1
21	        action: "增加 Llama-2 base checkpoint 对照实验"
22	        assigned_to: research
23	        status: done
24	      - round: 2
25	        action: "Section 标题改为观察性；Abstract 弱化 causal attribution"
26	        assigned_to: paper_agent
27	        status: done
28	    resolution: "B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。"
29	    resolution_round: 3
30	
31	  - id: R1-N2-old
32	    summary: "单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim"
33	    category: framing
34	    severity: critical
35	    status: resolved
36	    first_raised_round: 1
37	    last_seen_round: 2
38	    mentions:
39	      - round: 1
40	        reviewers: [1, 2, 3]
41	        note: "全票共识"
42	      - round: 2
43	        reviewers: [1, 2, 3]
44	        note: "PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数"
45	    action_items:
46	      - round: 2
47	        action: "Title 改为单数"
48	        assigned_to: paper_agent
49	        status: done
50	    resolution: "B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。"
51	    resolution_round: 3
52	
53	  - id: R1-N4-old
54	    summary: "Design implications 完全基于 correlational evidence"
55	    category: framing
56	    severity: cri
…[truncated 17738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-18T09:12:39.312148+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化 + 审稿 + 交叉 + 收敛', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 读论文验证关键声明', 'status': 'completed', 'activeForm': '已验证'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'in_progress', 'activeForm': '更新 review_issues.yaml'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化 + 审稿 + 交叉 + 收敛', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 读论文验证关键声明', 'status': 'completed', 'activeForm': '已验证'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'in_progress', 'activeForm': '更新 review_issues.yaml'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '提交审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-18T09:12:39.312650+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-18T09:15:27.312588+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-3 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: acknowledge confound 但无数据\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: done\n      - round: 2\n        action: \"Section 标题改为观察性；Abstract 弱化 causal attribution\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。\"\n    resolution_round: 3\n\n  - id: R1-N2-old\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Title 改为单数。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数\"\n    action_items:\n      - round: 2\n        action: \"Title 改为单数\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Related Work 已引用 Neo et al.\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical\"\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本引用数量达标。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本补充 MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA' 段落。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式不满足 CoRL 2026 要求\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection{Limitations}。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical\"\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Conclusion 加声明。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n    action_items: []\n\n  # ============================================================\n  # Round 4 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1（token-level functional specialization）是 causal mask 的数学必然结果 + probe 任务 trivially easy，不构成 empirical finding\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。R2 从 causal mask 架构决定论论证，R1 从 probe difficulty 论证。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 改为 'verify and quantify architecture-expected', Contributions (i) 定位为 framework+verification\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: 虽已 reframe 为 verification，但仍列为三大 contribution 之首。R1 指出 untrained 也 L1 100%。R2 认为即便 reframe，novelty bar 仍不够——验证已知性质不构成 contribution。两位建议进一步降格。\"\n    action_items:\n      - round: 4\n        action: \"Reframe C1 from 'empirical finding' to 'experimental framework + empirical verification'\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C1 已从 empirical finding 重新定位为 experimental framework + architecture verification。\"\n    resolution_round: 5\n\n  - id: R4-N2\n    summary: \"RSA inverted-U 的 rise phase 效应量极小（Δρ=0.016）且 metric-dependent：CKA 完全反转 RSA ordering 和 per-layer profile\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: metric-dependent qualifier 全文到位。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: qualifier 到位但核心问题未变。R2 指出 metric selection 看起来是 results-driven。R1 指出论文未提供为何 RSA 比 CKA 更 relevant to action prediction 的理论或实证论证。C3 作为独立 contribution 的 robustness 仍受质疑。\"\n    action_items:\n      - round: 4\n        action: \"Downgrade C3 to qualified observation.\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C3 已降为 qualified observation。RSA 结论全部加 metric-dependent qualifier。\"\n    resolution_round: 5\n\n  - id: R4-N3\n    summary: \"L1 attention ablation 使用 5 demos，R² baseline 0.256，因果推断可靠性不足\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。5 demos 下 probe 严重 underfitting。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: 50 demos (N=63,228)，R² baseline 0.557。\"\n    action_items:\n      - round: 4\n        action: \"50 demos ablation rerun\"\n        assigned_to: research\n        status: done\n    resolution: \"Ablation 已改用 50 demos per task (N=63,228)。\"\n    resolution_round: 5\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best training effect n.s. 在 Abstract/Intro 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Abstract 和 Intro 均明确标注 non-significant。\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED\"\n    action_items: []\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR correction (Benjamini-Hochberg) 已应用。\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED\"\n    action_items: []\n\n  - id: R4-W3\n    summary: \"Probe total N 未报告，MLP probe capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"N/params 措辞已修正为 overparameterized + early stopping。Linear probe baseline 加入 appendix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (升级): 虽然 overparameterized 已承认且 linear probe 复现，但 (a) train/test split 策略仍未明确说明, (b) R² 在哪个数据集上计算未说明, (c) 时间步自相关导致 effective sample size 远小于 63K, (d) linear vs MLP probe gap 20× 未讨论对结论的影响。\"\n    action_items:\n      - round: 5\n        action: \"修正措辞 + linear probe baseline\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"N/params 措辞修正为 overparameterized，linear probe (N/params≈2.2) 复现所有 pattern，加入 Appendix。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Frozen encoder confound 在 Introduction 和 Discussion 中均有说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W5\n    summary: \"单模型 + 单 benchmark，泛化性有限\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Limitations 已列举具体架构变量。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (升级至 CRITICAL): Limitations 改善但 Abstract 仍含一般化措辞（'instruction routing reorganization is the primary learned contribution of VLA fine-tuning'）。Grant 2026 覆盖 6 个 VLA，形成鲜明对比。LIBERO-Spatial 仍在同一 benchmark 框架内。无 real-robot 数据。\"\n    action_items:\n      - round: 5\n        action: \"Expand Limitations with specific architecture variables\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Limitations 列举 backbone scale/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    summary: \"缺少 Llama-2 和 Open X-Embodiment 关键引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"两篇引用均已加入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' 是 straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction 重写，使用客观描述。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未被 main.tex input\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion 末尾添加 Outlook 段落正面收尾，不需独立 Conclusion section。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: 当前 Discussion 最后是 Limitations 段落，非正面收尾。R2 建议添加 input{conclusion}，R1 认为不强制但结构不完整。\"\n    action_items: []\n    resolution: \"Discussion 末尾增加 Outlook 正面收尾。CoRL 格式不强制要求独立 Conclusion。\"\n    resolution_round: 5\n\n  - id: R4-I2\n    summary: \"引用格式问题：alain2017 年份存疑、nostalgebraist2020 blog post 格式不规范\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"alain2017 改为 @inproceedings (ICLR 2017 Workshop Track)。nostalgebraist2020 已是 @misc，补充 Accessed: 2026-05-18。\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"本轮未专门检查\"\n    action_items:\n      - round: 5\n        action: \"alain2017 改为 @inproceedings ICLR 2017 Workshop; nostalgebraist2020 加 access date\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 数值不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"全文统一为 24/32 heads。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 5 issues（全部 resolved）\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' claim — random-subset control 推翻 capacity trade-off\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Random-subset ablation (10 seeds, z=-2.73, p=0.003): dominant-24 (+0.042) < random-24 mean (+0.077). Narrative from 'capacity trade-off' to 'dual routing-encoding function'.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (新维度): 'dual function' 叙事本身受质疑。核心问题：所有 ablation (dominant 和 random) 都 INCREASE R²，说明 L1 heads 整体对 action probe 是 net-negative。如果 heads 功能重要，ablation 应 decrease R²。'dual function' 是 post-hoc rationalization。N=10 random subsets 统计功效不足。\"\n    action_items:\n      - round: 5\n        action: \"Random-subset ablation experiment + full narrative rewrite (Plan C)\"\n        assigned_to: research + paper_agent\n        status: done\n    resolution: \"3.5×/capacity trade-off 全文删除。替换为 dual routing-encoding function 叙事。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 被错误解读为 'ensuring adequate training signal'\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Wording fixed + linear probe (N/params≈2.2) reproduces all patterns.\"\n    action_items:\n      - round: 5\n        action: \"Fix wording + linear probe baseline\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Wording corrected to 'overparameterized; mitigated via early stopping'. Linear probe appendix confirms all qualitative patterns.\"\n    resolution_round: 5\n\n  - id: R5-N3\n    summary: \"单模型 scope — Limitations 不够具体\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Limitations 已列举 backbone scale/family, decoder type, frozen vs unfrozen, projector design, pretraining data.\"\n    action_items:\n      - round: 5\n        action: \"Expand Limitations with architecture variables\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Limitations 具体列举 6 个可能改变 routing 的架构变量。\"\n    resolution_round: 5\n\n  - id: R5-N4\n    summary: \"Architectural implications speculative + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'suggests' → 'raises the hypothesis'; speculative label added.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (升级至 CRITICAL): 语气弱化不够。核心缺口：论文所有发现在 representation space，从未连接到 task success rate。对 CoRL 机器人学习会议，无 behavioral validation 是重大问题。'early-layer parameters may suffice for instruction adaptation' 无任何实验支撑。\"\n    action_items:\n      - round: 5\n        action: \"Weaken implications + add L31 complication\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Implications weakened, L31 complication noted, speculative pending behavioral validation.\"\n    resolution_round: 5\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 OOD confound 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"OOD diagnostics (magnitude + cosine sim + effective rank) confirm non-degenerate representations.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: diagnostics 证明 non-degenerate 但不证明 meaningful。R1 建议 random noise token control（如果 Llama-2 对 random noise 也产生类似 mid-depth routing，则 pretrained 条件的 routing pattern 可能是 generic OOD response 而非 meaningful processing）。\"\n    action_items:\n      - round: 5\n        action: \"OOD diagnostics + appendix section + discussion caveat\"\n        assigned_to: research + paper_agent\n        status: done\n    resolution: \"Three diagnostics confirm llama2base produces structured full-rank representations.\"\n    resolution_round: 5\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 未报告具体 [lower, upper] 数值\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 key CIs inserted into experiments.tex.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"4 key CIs inserted.\"\n    action_items:\n      - round: 5\n        action: \"Extract and insert CI values\"\n        assigned_to: research + paper_agent\n        status: done\n\n  - id: R5-W3\n    summary: \"C3 Abstract 权重过高\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"C3 compressed to single sentence in Abstract.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"C3 compressed to single sentence.\"\n    action_items:\n      - round: 5\n        action: \"Compress C3 in Abstract\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R5-W4\n    summary: \"缺 causal tracing / tuned lens 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Meng et al. 2022 + Belrose et al. 2023 added.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Added with differentiation.\"\n    action_items:\n      - round: 5\n        action: \"Add 2 citations to Related Work\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R5-I1\n    summary: \"Appendix A.6 single-seed three-condition comparison\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"3 seeds × 3 conditions completed. All qualitative patterns robust.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Low priority. Main results have 5-seed analysis.\"\n    action_items:\n      - round: 5\n        action: \"Run 3-seed three-condition action probe\"\n        assigned_to: research\n        status: done\n\n  # ============================================================\n  # Round 6 — 新发现\n  # ============================================================\n  - id: R6-C1\n    summary: \"L1 head ablation 因果推断方向问题：所有 ablation（dominant 和 random）都 INCREASE R²，'dual function' 解释是 post-hoc rationalization\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识 + R2 对 R1 的 stronger formulation 表示 AGREE。核心：如果 dominant heads 功能重要，ablation 应 decrease R²。所有 ablation 都 increase 意味着 L1 75% heads 对 action probe 是 net-negative。最 parsimonious 的解释是 L1 heads 普遍添加 interference。N=10 random subsets 统计功效不足。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 细粒度 ablation curve (4/8/12/16/20/24/28 heads); 方案B: selective ablation (只零化 instruction attention component 保留其他); 方案C: 增加 random subsets ≥100; 方案D: 修改叙事——承认所有 ablation increase R² 的事实，不做 dual-function 因果声称\"\n        assigned_to: research + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C2\n    summary: \"Probe train/test split 未明确说明 + 时间步自相关导致 bootstrap CI 低估不确定性 + linear vs MLP 20× gap 未讨论\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 强烈同意。论文 Section 4.1 提到 early stopping patience 5 暗示有 validation set，但从未说明 (a) train/test ratio, (b) split 是 random timestep 还是 demo-level, (c) R² 报告在 test 还是 train set。63K observations 来自 50 demos × 10 tasks × ~127 timesteps，相邻帧高度自相关。如果 random timestep split 则 test set 与 train set 近乎重叠。Linear probe gap (Δ=0.324 at L14) vs MLP gap (Δ=0.015 at L8) 差 20×——MLP 过强 rescue untrained representations。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 明确报告 train/test split（建议 demo-level 或 task-level split 避免 temporal leakage）; 方案B: 报告 held-out test-set R²; 方案C: 使用 demo-level bootstrap 反映真实不确定性; 方案D: 讨论 linear vs MLP gap 的 implication + 考虑以 linear probe 为主\"\n        assigned_to: research + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C3\n    summary: \"Abstract 'instruction routing reorganization is the primary learned contribution of VLA fine-tuning' 是对所有 VLA 的一般化声称，仅有单模型证据\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识。尽管 Limitations 已扩充架构变量列表，Abstract/Introduction 仍用一般化措辞。Grant 2026 覆盖 6 个 VLA 形成对比。π₀ 用 flow matching，entry-exit pattern 可能不存在。LIBERO-Spatial 不算独立 benchmark（同一框架 tabletop manipulation）。\"\n    action_items:\n      - round: 6\n        action: \"方案A: Abstract/Introduction 中所有 general claims 加 'on OpenVLA-7B' 限定; 方案B: 如有条件，在至少一个不同架构 VLA 上验证 C2 的 entry-exit pattern\"\n        assigned_to: paper_agent (A) / research (B)\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C4\n    summary: \"缺少 behavioral validation——representational findings 未连接 task success rate，对 CoRL 是重大缺口\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识。论文所有发现在 representation space。R² 是离线指标不等于 behavioral importance。'early-layer parameters may suffice for instruction adaptation' (Discussion) 无实验支撑。对 CoRL 机器人学习会议，这是最大结构性缺陷之一。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 用 ablated model 在 LIBERO 上跑 rollout，报告 success rate 变化 (pilot 级别即可); 方案B: 如无法做行为实验，将论文明确定位为 'representational analysis'，删除所有 design implication 的 speculative claims\"\n        assigned_to: research (A) / paper_agent (B)\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W1\n    summary: \"RSA 统计推断中 pairwise dependency 未处理：bootstrap 低估 variance，permutation test 只测 structure 存在性不测条件差异\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。N(N-1)/2 pairwise distances 不独立（每个 observation 参与 N-1 个 pair），标准 bootstrap 假设 independent sampling 会 underestimate variance。Same-layer L12 Δ=+0.079 的 significance 可能在正确统计下减弱。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 使用 stimulus-level bootstrap (以 demo 或 task 为 resampling unit); 方案B: 补充 Mantel test; 方案C: 至少在 Method 或 Appendix 讨论此 caveat\"\n        assigned_to: research + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    summary: \"缺少 Generative AI 使用声明（CoRL 2026 明确要求）\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识。CoRL 2026 Instruction for Authors 要求披露 generative AI 使用。main.tex 中未找到此声明。有 desk reject 风险。\"\n    action_items:\n      - round: 6\n        action: \"添加 Generative AI disclosure statement\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    summary: \"Abstract/Introduction 数据密度过高（~15 个数字），叙事可读性差\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 标 WARNING，R1 REBUT 降至 INFO。R1 认为部分数字（100% classification, R²+0.069）是核心支撑应保留，但 z=-2.73 等过细统计不适合 Abstract。共识：部分数字过多但非方法论缺陷。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 精简至 2-3 个关键数字（100%, entry-exit pattern, R² gain），移除 z-score、具体头数等细节至正文\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-I1\n    summary: \"-ing 分词短语高密度（~30 处）是 AI 辅助写作统计信号\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"R2 minor。每处单独看自然，但高密度是 AI 生成统计标志。\"\n    action_items:\n      - round: 6\n        action: \"通读全文，部分 -ing phrases 改写为独立句子\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-I2\n    summary: \"缺少引用：Hewitt & Liang 2019 (probe design), Nili 2014 (RSA toolkit), Bills 2023, Templeton 2024 (SAE 方法论)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 提 Hewitt & Liang 2019 + Nili 2014，R2 提 Bills 2023 + Templeton 2024。R2 对 Hewitt & Liang 2019 强烈同意（probe selectivity 概念直接相关）。Nili 2014 是 RSA 统计实践核心参考。\"\n    action_items:\n      - round: 6\n        action: \"添加 Hewitt & Liang 2019 和 Nili et al. 2014 至 Related Work / Method；考虑添加 Bills 2023 和 Templeton 2024\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-I3\n    summary: \"Table 2 caption 不自包含（Mode 列含义未解释），Discussion 'Speculative' 标题自我贬低\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"Minor。Table 2 的 'immed.+stable', 'gradual+stable', 'incid.+forget' 需在 caption 中解释。'Speculative mechanistic interpretation' 建议改为 'Mechanistic hypothesis'。\"\n    action_items:\n      - round: 6\n        action: \"Table 2 caption 补充 Mode 列说明；Discussion 标题去掉 Speculative\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-3 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: acknowledge confound 但无数据\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: done\n      - round: 2\n        action: \"Section 标题改为观察性；Abstract 弱化 causal attribution\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。\"\n    resolution_round: 3\n\n  - id: R1-N2-old\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Title 改为单数。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数\"\n    action_items:\n      - round: 2\n        action: \"Title 改为单数\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Related Work 已引用 Neo et al.\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical\"\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本引用数量达标。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本补充 MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA' 段落。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式不满足 CoRL 2026 要求\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection{Limitations}。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical\"\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Conclusion 加声明。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n    action_items: []\n\n  # ============================================================\n  # Round 4 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1（token-level functional specialization）是 causal mask 的数学必然结果 + probe 任务 trivially easy，不构成 empirical finding\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。R2 从 causal mask 架构决定论论证，R1 从 probe difficulty 论证。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 改为 'verify and quantify architecture-expected', Contributions (i) 定位为 framework+verification\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: 虽已 reframe 为 verification，但仍列为三大 contribution 之首。R1 指出 untrained 也 L1 100%。R2 认为即便 reframe，novelty bar 仍不够——验证已知性质不构成 contribution。两位建议进一步降格。\"\n    action_items:\n      - round: 4\n        action: \"Reframe C1 from 'empirical finding' to 'experimental framework + empirical verification'\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C1 已从 empirical finding 重新定位为 experimental framework + architecture verification。\"\n    resolution_round: 5\n\n  - id: R4-N2\n    summary: \"RSA inverted-U 的 rise phase 效应量极小（Δρ=0.016）且 metric-dependent：CKA 完全反转 RSA ordering 和 per-layer profile\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: metric-dependent qualifier 全文到位。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: qualifier 到位但核心问题未变。R2 指出 metric selection 看起来是 results-driven。R1 指出论文未提供为何 RSA 比 CKA 更 relevant to action prediction 的理论或实证论证。C3 作为独立 contribution 的 robustness 仍受质疑。\"\n    action_items:\n      - round: 4\n        action: \"Downgrade C3 to qualified observation.\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C3 已降为 qualified observation。RSA 结论全部加 metric-dependent qualifier。\"\n    resolution_round: 5\n\n  - id: R4-N3\n    summary: \"L1 attention ablation 使用 5 demos，R² baseline 0.256，因果推断可靠性不足\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。5 demos 下 probe 严重 underfitting。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: 50 demos (N=63,228)，R² baseline 0.557。\"\n    action_items:\n      - round: 4\n        action: \"50 demos ablation rerun\"\n        assigned_to: research\n        status: done\n    resolution: \"Ablation 已改用 50 demos per task (N=63,228)。\"\n    resolution_round: 5\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best training effect n.s. 在 Abstract/Intro 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Abstract 和 Intro 均明确标注 non-significant。\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED\"\n    action_items: []\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR correction (Benjamini-Hochberg) 已应用。\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED\"\n    action_items: []\n\n  - id: R4-W3\n    summary: \"Probe total N 未报告，MLP probe capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"N/params 措辞已修正为 overparameterized + early stopping。Linear probe baseline 加入 appendix。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (升级): 虽然 overparameterized 已承认且 linear probe 复现，但 (a) train/test split 策略仍未明确说明, (b) R² 在哪个数据集上计算未说明, (c) 时间步自相关导致 effective sample size 远小于 63K, (d) linear vs MLP probe gap 20× 未讨论对结论的影响。\"\n    action_items:\n      - round: 5\n        action: \"修正措辞 + linear probe baseline\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"N/params 措辞修正为 overparameterized，linear probe (N/params≈2.2) 复现所有 pattern，加入 Appendix。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Frozen encoder confound 在 Introduction 和 Discussion 中均有说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W5\n    summary: \"单模型 + 单 benchmark，泛化性有限\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Limitations 已列举具体架构变量。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (升级至 CRITICAL): Limitations 改善但 Abstract 仍含一般化措辞（'instruction routing reorganization is the primary learned contribution of VLA fine-tuning'）。Grant 2026 覆盖 6 个 VLA，形成鲜明对比。LIBERO-Spatial 仍在同一 benchmark 框架内。无 real-robot 数据。\"\n    action_items:\n      - round: 5\n        action: \"Expand Limitations with specific architecture variables\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Limitations 列举 backbone scale/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    summary: \"缺少 Llama-2 和 Open X-Embodiment 关键引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"两篇引用均已加入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' 是 straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction 重写，使用客观描述。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未被 main.tex input\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion 末尾添加 Outlook 段落正面收尾，不需独立 Conclusion section。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: 当前 Discussion 最后是 Limitations 段落，非正面收尾。R2 建议添加 input{conclusion}，R1 认为不强制但结构不完整。\"\n    action_items: []\n    resolution: \"Discussion 末尾增加 Outlook 正面收尾。CoRL 格式不强制要求独立 Conclusion。\"\n    resolution_round: 5\n\n  - id: R4-I2\n    summary: \"引用格式问题：alain2017 年份存疑、nostalgebraist2020 blog post 格式不规范\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"alain2017 改为 @inproceedings (ICLR 2017 Workshop Track)。nostalgebraist2020 已是 @misc，补充 Accessed: 2026-05-18。\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"本轮未专门检查\"\n    action_items:\n      - round: 5\n        action: \"alain2017 改为 @inproceedings ICLR 2017 Workshop; nostalgebraist2020 加 access date\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 数值不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"全文统一为 24/32 heads。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 5 issues（全部 resolved）\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' claim — random-subset control 推翻 capacity trade-off\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Random-subset ablation (10 seeds, z=-2.73, p=0.003): dominant-24 (+0.042) < random-24 mean (+0.077). Narrative from 'capacity trade-off' to 'dual routing-encoding function'.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (新维度): 'dual function' 叙事本身受质疑。核心问题：所有 ablation (dominant 和 random) 都 INCREASE R²，说明 L1 heads 整体对 action probe 是 net-negative。如果 heads 功能重要，ablation 应 decrease R²。'dual function' 是 post-hoc rationalization。N=10 random subsets 统计功效不足。\"\n    action_items:\n      - round: 5\n        action: \"Random-subset ablation experiment + full narrative rewrite (Plan C)\"\n        assigned_to: research + paper_agent\n        status: done\n    resolution: \"3.5×/capacity trade-off 全文删除。替换为 dual routing-encoding function 叙事。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 被错误解读为 'ensuring adequate training signal'\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Wording fixed + linear probe (N/params≈2.2) reproduces all patterns.\"\n    action_items:\n      - round: 5\n        action: \"Fix wording + linear probe baseline\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Wording corrected to 'overparameterized; mitigated via early stopping'. Linear probe appendix confirms all qualitative patterns.\"\n    resolution_round: 5\n\n  - id: R5-N3\n    summary: \"单模型 scope — Limitations 不够具体\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Limitations 已列举 backbone scale/family, decoder type, frozen vs unfrozen, projector design, pretraining data.\"\n    action_items:\n      - round: 5\n        action: \"Expand Limitations with architecture variables\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Limitations 具体列举 6 个可能改变 routing 的架构变量。\"\n    resolution_round: 5\n\n  - id: R5-N4\n    summary: \"Architectural implications speculative + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"'suggests' → 'raises the hypothesis'; speculative label added.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING (升级至 CRITICAL): 语气弱化不够。核心缺口：论文所有发现在 representation space，从未连接到 task success rate。对 CoRL 机器人学习会议，无 behavioral validation 是重大问题。'early-layer parameters may suffice for instruction adaptation' 无任何实验支撑。\"\n    action_items:\n      - round: 5\n        action: \"Weaken implications + add L31 complication\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Implications weakened, L31 complication noted, speculative pending behavioral validation.\"\n    resolution_round: 5\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 OOD confound 未讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"OOD diagnostics (magnitude + cosine sim + effective rank) confirm non-degenerate representations.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"RECURRING: diagnostics 证明 non-degenerate 但不证明 meaningful。R1 建议 random noise token control（如果 Llama-2 对 random noise 也产生类似 mid-depth routing，则 pretrained 条件的 routing pattern 可能是 generic OOD response 而非 meaningful processing）。\"\n    action_items:\n      - round: 5\n        action: \"OOD diagnostics + appendix section + discussion caveat\"\n        assigned_to: research + paper_agent\n        status: done\n    resolution: \"Three diagnostics confirm llama2base produces structured full-rank representations.\"\n    resolution_round: 5\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 未报告具体 [lower, upper] 数值\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"4 key CIs inserted into experiments.tex.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"4 key CIs inserted.\"\n    action_items:\n      - round: 5\n        action: \"Extract and insert CI values\"\n        assigned_to: research + paper_agent\n        status: done\n\n  - id: R5-W3\n    summary: \"C3 Abstract 权重过高\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"C3 compressed to single sentence in Abstract.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"C3 compressed to single sentence.\"\n    action_items:\n      - round: 5\n        action: \"Compress C3 in Abstract\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R5-W4\n    summary: \"缺 causal tracing / tuned lens 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Meng et al. 2022 + Belrose et al. 2023 added.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Added with differentiation.\"\n    action_items:\n      - round: 5\n        action: \"Add 2 citations to Related Work\"\n        assigned_to: paper_agent\n        status: done\n\n  - id: R5-I1\n    summary: \"Appendix A.6 single-seed three-condition comparison\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"3 seeds × 3 conditions completed. All qualitative patterns robust.\"\n    resolution_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Low priority. Main results have 5-seed analysis.\"\n    action_items:\n      - round: 5\n        action: \"Run 3-seed three-condition action probe\"\n        assigned_to: research\n        status: done\n\n  # ============================================================\n  # Round 6 — 新发现\n  # ============================================================\n  - id: R6-C1\n    summary: \"L1 head ablation 因果推断方向问题：所有 ablation（dominant 和 random）都 INCREASE R²，'dual function' 解释是 post-hoc rationalization\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识 + R2 对 R1 的 stronger formulation 表示 AGREE。核心：如果 dominant heads 功能重要，ablation 应 decrease R²。所有 ablation 都 increase 意味着 L1 75% heads 对 action probe 是 net-negative。最 parsimonious 的解释是 L1 heads 普遍添加 interference。N=10 random subsets 统计功效不足。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 细粒度 ablation curve (4/8/12/16/20/24/28 heads); 方案B: selective ablation (只零化 instruction attention component 保留其他); 方案C: 增加 random subsets ≥100; 方案D: 修改叙事——承认所有 ablation increase R² 的事实，不做 dual-function 因果声称\"\n        assigned_to: research + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C2\n    summary: \"Probe train/test split 未明确说明 + 时间步自相关导致 bootstrap CI 低估不确定性 + linear vs MLP 20× gap 未讨论\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 强烈同意。论文 Section 4.1 提到 early stopping patience 5 暗示有 validation set，但从未说明 (a) train/test ratio, (b) split 是 random timestep 还是 demo-level, (c) R² 报告在 test 还是 train set。63K observations 来自 50 demos × 10 tasks × ~127 timesteps，相邻帧高度自相关。如果 random timestep split 则 test set 与 train set 近乎重叠。Linear probe gap (Δ=0.324 at L14) vs MLP gap (Δ=0.015 at L8) 差 20×——MLP 过强 rescue untrained representations。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 明确报告 train/test split（建议 demo-level 或 task-level split 避免 temporal leakage）; 方案B: 报告 held-out test-set R²; 方案C: 使用 demo-level bootstrap 反映真实不确定性; 方案D: 讨论 linear vs MLP gap 的 implication + 考虑以 linear probe 为主\"\n        assigned_to: research + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C3\n    summary: \"Abstract 'instruction routing reorganization is the primary learned contribution of VLA fine-tuning' 是对所有 VLA 的一般化声称，仅有单模型证据\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识。尽管 Limitations 已扩充架构变量列表，Abstract/Introduction 仍用一般化措辞。Grant 2026 覆盖 6 个 VLA 形成对比。π₀ 用 flow matching，entry-exit pattern 可能不存在。LIBERO-Spatial 不算独立 benchmark（同一框架 tabletop manipulation）。\"\n    action_items:\n      - round: 6\n        action: \"方案A: Abstract/Introduction 中所有 general claims 加 'on OpenVLA-7B' 限定; 方案B: 如有条件，在至少一个不同架构 VLA 上验证 C2 的 entry-exit pattern\"\n        assigned_to: paper_agent (A) / research (B)\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C4\n    summary: \"缺少 behavioral validation——representational findings 未连接 task success rate，对 CoRL 是重大缺口\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识。论文所有发现在 representation space。R² 是离线指标不等于 behavioral importance。'early-layer parameters may suffice for instruction adaptation' (Discussion) 无实验支撑。对 CoRL 机器人学习会议，这是最大结构性缺陷之一。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 用 ablated model 在 LIBERO 上跑 rollout，报告 success rate 变化 (pilot 级别即可); 方案B: 如无法做行为实验，将论文明确定位为 'representational analysis'，删除所有 design implication 的 speculative claims\"\n        assigned_to: research (A) / paper_agent (B)\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W1\n    summary: \"RSA 统计推断中 pairwise dependency 未处理：bootstrap 低估 variance，permutation test 只测 structure 存在性不测条件差异\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。N(N-1)/2 pairwise distances 不独立（每个 observation 参与 N-1 个 pair），标准 bootstrap 假设 independent sampling 会 underestimate variance。Same-layer L12 Δ=+0.079 的 significance 可能在正确统计下减弱。\"\n    action_items:\n      - round: 6\n        action: \"方案A: 使用 stimulus-level bootstrap (以 demo 或 task 为 resampling unit); 方案B: 补充 Mantel test; 方案C: 至少在 Method 或 Appendix 讨论此 caveat\"\n        assigned_to: research + paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    summary: \"缺少 Generative AI 使用声明（CoRL 2026 明确要求）\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"全票共识。CoRL 2026 Instruction for Authors 要求披露 generative AI 使用。main.tex 中未找到此声明。有 desk reject 风险。\"\n    action_items:\n      - round: 6\n        action: \"添加 Generative AI disclosure statement\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    summary: \"Abstract/Introduction 数据密度过高（~15 个数字），叙事可读性差\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 标 WARNING，R1 REBUT 降至 INFO。R1 认为部分数字（100% classification, R²+0.069）是核心支撑应保留，但 z=-2.73 等过细统计不适合 Abstract。共识：部分数字过多但非方法论缺陷。\"\n    action_items:\n      - round: 6\n        action: \"Abstract 精简至 2-3 个关键数字（100%, entry-exit pattern, R² gain），移除 z-score、具体头数等细节至正文\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-I1\n    summary: \"-ing 分词短语高密度（~30 处）是 AI 辅助写作统计信号\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"R2 minor。每处单独看自然，但高密度是 AI 生成统计标志。\"\n    action_items:\n      - round: 6\n        action: \"通读全文，部分 -ing phrases 改写为独立句子\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-I2\n    summary: \"缺少引用：Hewitt & Liang 2019 (probe design), Nili 2014 (RSA toolkit), Bills 2023, Templeton 2024 (SAE 方法论)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 提 Hewitt & Liang 2019 + Nili 2014，R2 提 Bills 2023 + Templeton 2024。R2 对 Hewitt & Liang 2019 强烈同意（probe selectivity 概念直接相关）。Nili 2014 是 RSA 统计实践核心参考。\"\n    action_items:\n      - round: 6\n        action: \"添加 Hewitt & Liang 2019 和 Nili et al. 2014 至 Related Work / Method；考虑添加 Bills 2023 和 Templeton 2024\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-I3\n    summary: \"Table 2 caption 不自包含（Mode 列含义未解释），Discussion 'Speculative' 标题自我贬低\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"Minor。Table 2 的 'immed.+stable', 'gradual+stable', 'incid.+forget' 需在 caption 中解释。'Speculative mechanistic interpretation' 建议改为 'Mechanistic hypothesis'。\"\n    action_items:\n      - round: 6\n        action: \"Table 2 caption 补充 Mode 列说明；Discussion 标题去掉 Speculative\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-18T09:15:27.464376+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 26326}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-18T09:15:33.043340+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-4b: 初始化到 Issue Tracker 同步', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '撰写并提交审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-4b: 初始化到 Issue Tracker 同步', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '撰写并提交审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-18T09:15:33.094074+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-18T09:17:22.008028+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# 审稿圆桌报告 — Round 6 (Fresh Review)\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026 (Deadline: May 29, 2026)\n**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 叙事完整性 + 格式合规)\n**交叉回应**: R1↔R2 完成，Round 1 即收敛\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级表征分析，使用 cross-instruction probes、attention analysis、RSA 和 MLP probes，配合 trained/pretrained/untrained 三条件阶乘设计。三个发现：(1) image tokens instruction-blind（架构必然），(2) VLA fine-tuning 将 instruction routing 从 mid-depth 重组为 entry-exit 模式，(3) vision encoder 表征呈 metric-dependent 非单调变换。实验设计严谨，统计报告完整，但核心新颖性受限且存在方法论缺陷。\n\n---\n\n## Strengths\n\n- **S1 [共识]**: 三条件阶乘设计（trained/pretrained/untrained × instruction presence）是该领域罕见的严格控制方案，能有效隔离语言预训练和 VLA fine-tuning 的各自贡献。优于 Grant 2026 等仅分析 trained model 的工作。\n- **S2 [共识]**: 统计报告标准高——bootstrap CI (10,000 resamples)、FDR 校正 (Benjamini-Hochberg)、permutation test、seed sensitivity、demo subsampling sensitivity。在 VLA interpretability 文献中罕见。\n- **S3 [共识]**: C2（routing reorganization）是最有实质价值的发现。三条件梯度（untrained 0/32 → Llama-2 base 9/32 → trained 24/32 heads at L1）在 30%-70% 阈值范围内稳定，有 cross-benchmark (LIBERO-Spatial) 复现。\n- **S4 [共识]**: 四种分析方法（probing, attention, RSA, cross-instruction）从不同角度交叉验证，方法互补性好。RSA/CKA 分歧被坦诚报告而非回避。\n- **S5 [共识]**: Related Work 与 Grant 2026 的三点差异化清晰有力，positioning 准确。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [CRITICAL, 共识]: Ablation 因果推断方向有根本性问题**\n- 位置: Section 4.3, Appendix E\n- 所有 ablation（dominant 24 heads: +0.042, random 24 heads: +0.077）都 INCREASE action R²\n- 如果 instruction-dominant heads 功能重要，ablation 应 DECREASE R²\n- \"Dual routing-encoding function\" 是 post-hoc rationalization；更 parsimonious 的解释是 L1 heads 普遍添加 interference\n- 仅 N=10 random subsets，z-test 统计功效极低\n- 这是论文唯一的因果证据——如果不成立，C2 的证据链从 \"相关+因果\" 降级为 \"仅相关\"\n- **R1 评价更严厉**：认为这是 fundamental directionality problem，R2 同意并升级\n\n**W2 [CRITICAL, 共识]: Probe train/test split 未说明 + 时间步自相关 + linear vs MLP 20× gap**\n- 位置: Section 3.6, Section 4.1\n- Train/test split 策略从未明确说明——R² 在哪个数据集上计算？\n- 63,228 observations 来自 50 demos × 10 tasks × ~127 timesteps，相邻帧高度自相关\n- 如果 random timestep split，test set 与 train set 近乎重叠，R² 严重高估\n- Linear probe trained-untrained gap (Δ=+0.324 at L14) vs MLP gap (Δ=+0.015 at L8) 差 ~20×，说明 MLP 过强 rescue untrained representations，压缩条件差异\n- Bootstrap CI 基于独立假设，时间自相关导致 CI 被低估\n\n**W3 [CRITICAL, 共识]: 单模型 + 单 benchmark + Abstract overclaim**\n- 位置: Abstract line 7, Introduction, Discussion\n- Abstract 写 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\"，这是对所有 VLA 的一般性声称，但证据仅来自 OpenVLA-7B + LIBERO\n- Grant 2026 覆盖 6 个 VLA（80M-7B）形成鲜明对比\n- LIBERO-Spatial 仍在同一框架（tabletop manipulation），不算独立泛化验证\n- π₀ 使用 flow matching，entry-exit routing pattern 可能完全不同\n- Limitations 列举了架构变量但 Abstract/Introduction 的 framing 未相应 qualify\n\n**W4 [CRITICAL, 共识]: 缺少 behavioral validation**\n- 位置: Discussion Section 5\n- 论文所有发现在 representation space，从未连接到 task success rate\n- R² 是离线指标，不等于 behavioral importance\n- \"Early-layer parameters may suffice for instruction adaptation\"（Discussion）完全 speculative，无实验支撑\n- 对 CoRL（机器人学习会议）是重大结构性缺口\n- 即使 pilot 级别的 rollout 验证（L1 ablation → success rate）也能显著提升说服力\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5 [WARNING, 共识]: C1 novelty 不足——架构必然 + probe trivially easy**\n- C1 列为三大 contribution 之首，但 image tokens instruction-blind 是 causal mask + frozen encoder 的直接推论\n- 10-way cross-instruction probe 在所有三条件 L1 均达 99.6-100%（含 untrained），任务 trivially easy\n- Appendix K.1 作者自承 \"even incidental attention (~12%) suffices\"\n- Round 5 已 reframe 为 \"framework + verification\"，但仍列为 contribution (i)\n- 如果 C1 实质上是 sanity check，论文核心新颖性实质上只有 C2（+ C3 qualified）\n- **注意**: 这本身是 WARNING 而非 rejection reason，但与 W1-W4 联合降低了整体 novelty bar\n\n**W6 [WARNING, 共识]: RSA/CKA 分歧对 C3 影响被低估**\n- Linear CKA 完全反转 RSA：per-layer 单调递增（无 inverted-U），encoder ordering 也反转\n- 论文选择 RSA 作为主叙事，但未论证为何 rank-order geometry 比 covariance structure 对 action prediction 更 relevant\n- C3 的 metric-dependence 使其作为独立 contribution 的 robustness 存疑\n- R2 指出 metric selection 看起来 results-driven 而非 hypothesis-driven\n\n**W7 [WARNING, 共识]: RSA 统计推断中 pairwise dependency 未处理**\n- RDM 上三角 N(N-1)/2 entries 不独立，标准 bootstrap 低估 variance\n- Permutation test 仅测试 structure 存在性，不测试条件间差异\n- Same-layer L12 Δ=+0.079 的 significance 可能在正确统计下减弱\n- Nili et al. (2014) 对此问题有标准处理方案\n\n**W8 [WARNING, 共识]: 缺少 Generative AI 使用声明**\n- CoRL 2026 Instruction for Authors 明确要求 Generative AI 使用声明\n- main.tex 中未找到此声明\n- 有 desk reject 风险\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n\n1. **C1 novelty 问题**：架构必然 + probe trivially easy，不应作为独立 contribution\n2. **Ablation 方向性问题**：所有 ablation increase R²，dual-function 解释不 convincing\n3. **Probe 方法论漏洞**：train/test split 未说明 + 自相关 + MLP/linear 20× gap\n4. **单模型泛化性 + overclaim**：Abstract 一般化措辞 vs 单模型证据\n5. **缺少 behavioral validation**：对 CoRL 是重大缺口\n6. **C3 metric-dependence**：RSA/CKA 分歧未充分处理\n\n---\n\n## Reviewer Divergence [REBUT]\n\n分歧极小，仅在以下次要点：\n\n| 议题 | R1 | R2 | 解决 |\n|------|----|----|------|\n| Abstract 数据密度 (R2-W6) | REBUT → INFO | WARNING | 降为 INFO（部分数字核心支撑应保留，z-score 等移除） |\n| Q4 baseline R² 差异 | 论文脚注已解释 | 提问 | R1 指出 Section 4.3 脚注 1 已明确回答 |\n| Mantel test (Q6) | 建议 | PARTIAL REBUT | R2 认为 stimulus-level bootstrap 更合适，但核心关切一致 |\n| 评分 | 5/10 | 4/10 | R1 对 C2 routing reorganization 评价稍高 |\n\n---\n\n## Questions for Authors\n\n1. Action probe R² 在 training set 还是 held-out test set 上计算？Train/test split 策略是什么（random timestep / demo-level / task-level）？\n2. 所有 head ablation（dominant 和 random）都 increase R²。是否意味着 L1 heads 对 action prediction 是 net-negative 的？如果是，\"dual routing-encoding function\" 如何成立？\n3. Untrained readout 在 L1 达到 100% classification，但 untrained 有 0/32 instruction-dominant heads。如果 12% incidental attention 已够 100% 分类，VLA training 将 attention 提高到 57.7% 的功能意义是什么？\n4. Linear probe gap (Δ=+0.324 at L14) vs MLP probe gap (Δ=+0.015 at L8) 差 ~20 倍，对结果解释有何影响？论文应以哪个为主？\n5. Pretrained Llama-2 的 mid-depth routing pattern 是 meaningful processing 还是 OOD response？用 random noise tokens 替代 visual tokens 是否会产生类似 pattern？\n6. Bootstrap CI 的 resampling unit 是什么？如何处理同一 demo 内时间步的高度自相关？\n7. RSA 显示 DINOv2 几何最优 (ρ=0.692)，R² 显示 VLA readout 功能最优 (0.678)。\"Vision encoder quality emerges as a key design lever\" 的操作化定义是什么？\n\n---\n\n## Missing References\n\n- **Hewitt & Liang (2019)** \"Designing and Interpreting Probes with Control Tasks\" [probe selectivity，直接相关方法论]\n- **Nili et al. (2014)** \"A Toolbox for Representational Similarity Analysis\" [RSA 统计推断最佳实践]\n- **Bills et al. (2023)** \"Language models can explain neurons in language models\" [mechanistic interp 方法论基础]\n- **Templeton et al. (2024)** \"Scaling monosemanticity\" [SAE 方法论，与 Swann 2026 相关]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (4.5/10)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Originality | 6/10 | 4/10 | 5/10 |\n| Quality/Soundness | 4/10 | 7/10 | 5.5/10 |\n| Clarity | 7/10 | 6/10 | 6.5/10 |\n| Significance | 5/10 | 4/10 | 4.5/10 |\n| Relevance to CoRL | 5/10 | 7/10 | 6/10 |\n\n**Confidence: High**\n\n**核心判断**: 实验设计和统计报告质量优秀，C2（routing reorganization）有实质价值。但存在四个结构性问题的联合影响：(1) ablation 因果推断方向反直觉且解释不 convincing，(2) probe 方法论有未公开的关键细节（train/test split, 自相关），(3) 单模型证据 vs 一般化声称，(4) 纯 representation analysis 无 behavioral validation 对 CoRL 不够。三大 contribution 中 C1 是架构验证、C3 是 metric-dependent observation，实质新颖性集中在 C2，而 C2 的因果证据链（ablation）存在方向性问题。当前版本 below acceptance threshold。\n\n**可修复性评估**: W1 (ablation) 需要新实验（细粒度 ablation curve + selective ablation + 更多 random subsets）或叙事大幅修改；W2 (probe split) 可通过补充说明和 demo-level split 重分析修复；W3 (overclaim) 可通过 framing 修改修复；W4 (behavioral validation) 需要 rollout 实验。如果时间允许（deadline May 29），W2+W3 可在 11 天内完成；W1 的新实验和 W4 的 rollout 验证时间紧张但可能可行。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 数据密度过高（~15 个数字），z=-2.73 和具体头数不适合 Abstract\n- \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 是 overclaim\n- 建议保留 2-3 个核心数字，移除统计细节\n\n### Introduction\n- 5 段结构完整，叙事逻辑清晰\n- Contribution (i) \"verifying architecture-expected specialization\" 作为 contribution 列首位降低 novelty 感知\n- Contribution (iii) 在 contribution 列表中提及 \"CKA diverges\" 让读者困惑\n\n### Related Work\n- 覆盖全面（VLAs, mechanistic interp, behavioral analysis, token specialization, similarity methods）\n- 与 Grant 2026 差异化清晰\n- 缺 Hewitt & Liang 2019 (probe design) 和 Nili 2014 (RSA statistics)\n\n### Method\n- 清晰可复现，四种方法选择有 justify\n- \"Why RSA over CKA\" 段落理由合理但不完全令人信服（未论证 rank-order 对 action prediction 更 relevant）\n- 缺少 train/test split 的明确说明\n\n### Experiments\n- Section 4.2: 结果 clean 但 C1 novelty 问题持续\n- Section 4.3: 最强贡献，三条件梯度有说服力。但 ablation 方向性问题（所有 ablation increase R²）严重削弱因果推断\n- Section 4.4: 数据详实但 CKA 矛盾仅在 Appendix 讨论\n\n### Discussion\n- 过于简短。Limitations 仅半段，嵌入 Discussion 而非独立 section\n- \"Speculative mechanistic interpretation\" 标题过于自我贬低\n- 缺少对 probe methodology limitations 和 behavioral validation gap 的讨论\n\n### Appendix\n- 内容丰富且组织良好（robustness, cross-benchmark, diagnostics）\n- CKA 矛盾结果和 QA probe 的 1pp 差异对主文叙事有重大影响，应在正文 summarize",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# 审稿圆桌报告 — Round 6 (Fresh Review)\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026 (Deadline: May 29, 2026)\n**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 叙事完整性 + 格式合规)\n**交叉回应**: R1↔R2 完成，Round 1 即收敛\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级表征分析，使用 cross-instruction probes、attention analysis、RSA 和 MLP probes，配合 trained/pretrained/untrained 三条件阶乘设计。三个发现：(1) image tokens instruction-blind（架构必然），(2) VLA fine-tuning 将 instruction routing 从 mid-depth 重组为 entry-exit 模式，(3) vision encoder 表征呈 metric-dependent 非单调变换。实验设计严谨，统计报告完整，但核心新颖性受限且存在方法论缺陷。\n\n---\n\n## Strengths\n\n- **S1 [共识]**: 三条件阶乘设计（trained/pretrained/untrained × instruction presence）是该领域罕见的严格控制方案，能有效隔离语言预训练和 VLA fine-tuning 的各自贡献。优于 Grant 2026 等仅分析 trained model 的工作。\n- **S2 [共识]**: 统计报告标准高——bootstrap CI (10,000 resamples)、FDR 校正 (Benjamini-Hochberg)、permutation test、seed sensitivity、demo subsampling sensitivity。在 VLA interpretability 文献中罕见。\n- **S3 [共识]**: C2（routing reorganization）是最有实质价值的发现。三条件梯度（untrained 0/32 → Llama-2 base 9/32 → trained 24/32 heads at L1）在 30%-70% 阈值范围内稳定，有 cross-benchmark (LIBERO-Spatial) 复现。\n- **S4 [共识]**: 四种分析方法（probing, attention, RSA, cross-instruction）从不同角度交叉验证，方法互补性好。RSA/CKA 分歧被坦诚报告而非回避。\n- **S5 [共识]**: Related Work 与 Grant 2026 的三点差异化清晰有力，positioning 准确。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [CRITICAL, 共识]: Ablation 因果推断方向有根本性问题**\n- 位置: Section 4.3, Appendix E\n- 所有 ablation（dominant 24 heads: +0.042, random 24 heads: +0.077）都 INCREASE action R²\n- 如果 instruction-dominant heads 功能重要，ablation 应 DECREASE R²\n- \"Dual routing-encoding function\" 是 post-hoc rationalization；更 parsimonious 的解释是 L1 heads 普遍添加 interference\n- 仅 N=10 random subsets，z-test 统计功效极低\n- 这是论文唯一的因果证据——如果不成立，C2 的证据链从 \"相关+因果\" 降级为 \"仅相关\"\n- **R1 评价更严厉**：认为这是 fundamental directionality problem，R2 同意并升级\n\n**W2 [CRITICAL, 共识]: Probe train/test split 未说明 + 时间步自相关 + linear vs MLP 20× gap**\n- 位置: Section 3.6, Section 4.1\n- Train/test split 策略从未明确说明——R² 在哪个数据集上计算？\n- 63,228 observations 来自 50 demos × 10 tasks × ~127 timesteps，相邻帧高度自相关\n- 如果 random timestep split，test set 与 train set 近乎重叠，R² 严重高估\n- Linear probe trained-untrained gap (Δ=+0.324 at L14) vs MLP gap (Δ=+0.015 at L8) 差 ~20×，说明 MLP 过强 rescue untrained representations，压缩条件差异\n- Bootstrap CI 基于独立假设，时间自相关导致 CI 被低估\n\n**W3 [CRITICAL, 共识]: 单模型 + 单 benchmark + Abstract overclaim**\n- 位置: Abstract line 7, Introduction, Discussion\n- Abstract 写 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\"，这是对所有 VLA 的一般性声称，但证据仅来自 OpenVLA-7B + LIBERO\n- Grant 2026 覆盖 6 个 VLA（80M-7B）形成鲜明对比\n- LIBERO-Spatial 仍在同一框架（tabletop manipulation），不算独立泛化验证\n- π₀ 使用 flow matching，entry-exit routing pattern 可能完全不同\n- Limitations 列举了架构变量但 Abstract/Introduction 的 framing 未相应 qualify\n\n**W4 [CRITICAL, 共识]: 缺少 behavioral validation**\n- 位置: Discussion Section 5\n- 论文所有发现在 representation space，从未连接到 task success rate\n- R² 是离线指标，不等于 behavioral importance\n- \"Early-layer parameters may suffice for instruction adaptation\"（Discussion）完全 speculative，无实验支撑\n- 对 CoRL（机器人学习会议）是重大结构性缺口\n- 即使 pilot 级别的 rollout 验证（L1 ablation → success rate）也能显著提升说服力\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5 [WARNING, 共识]: C1 novelty 不足——架构必然 + probe trivially easy**\n- C1 列为三大 contribution 之首，但 image tokens instruction-blind 是 causal mask + frozen encoder 的直接推论\n- 10-way cross-instruction probe 在所有三条件 L1 均达 99.6-100%（含 untrained），任务 trivially easy\n- Appendix K.1 作者自承 \"even incidental attention (~12%) suffices\"\n- Round 5 已 reframe 为 \"framework + verification\"，但仍列为 contribution (i)\n- 如果 C1 实质上是 sanity check，论文核心新颖性实质上只有 C2（+ C3 qualified）\n- **注意**: 这本身是 WARNING 而非 rejection reason，但与 W1-W4 联合降低了整体 novelty bar\n\n**W6 [WARNING, 共识]: RSA/CKA 分歧对 C3 影响被低估**\n- Linear CKA 完全反转 RSA：per-layer 单调递增（无 inverted-U），encoder ordering 也反转\n- 论文选择 RSA 作为主叙事，但未论证为何 rank-order geometry 比 covariance structure 对 action prediction 更 relevant\n- C3 的 metric-dependence 使其作为独立 contribution 的 robustness 存疑\n- R2 指出 metric selection 看起来 results-driven 而非 hypothesis-driven\n\n**W7 [WARNING, 共识]: RSA 统计推断中 pairwise dependency 未处理**\n- RDM 上三角 N(N-1)/2 entries 不独立，标准 bootstrap 低估 variance\n- Permutation test 仅测试 structure 存在性，不测试条件间差异\n- Same-layer L12 Δ=+0.079 的 significance 可能在正确统计下减弱\n- Nili et al. (2014) 对此问题有标准处理方案\n\n**W8 [WARNING, 共识]: 缺少 Generative AI 使用声明**\n- CoRL 2026 Instruction for Authors 明确要求 Generative AI 使用声明\n- main.tex 中未找到此声明\n- 有 desk reject 风险\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n\n1. **C1 novelty 问题**：架构必然 + probe trivially easy，不应作为独立 contribution\n2. **Ablation 方向性问题**：所有 ablation increase R²，dual-function 解释不 convincing\n3. **Probe 方法论漏洞**：train/test split 未说明 + 自相关 + MLP/linear 20× gap\n4. **单模型泛化性 + overclaim**：Abstract 一般化措辞 vs 单模型证据\n5. **缺少 behavioral validation**：对 CoRL 是重大缺口\n6. **C3 metric-dependence**：RSA/CKA 分歧未充分处理\n\n---\n\n## Reviewer Divergence [REBUT]\n\n分歧极小，仅在以下次要点：\n\n| 议题 | R1 | R2 | 解决 |\n|------|----|----|------|\n| Abstract 数据密度 (R2-W6) | REBUT → INFO | WARNING | 降为 INFO（部分数字核心支撑应保留，z-score 等移除） |\n| Q4 baseline R² 差异 | 论文脚注已解释 | 提问 | R1 指出 Section 4.3 脚注 1 已明确回答 |\n| Mantel test (Q6) | 建议 | PARTIAL REBUT | R2 认为 stimulus-level bootstrap 更合适，但核心关切一致 |\n| 评分 | 5/10 | 4/10 | R1 对 C2 routing reorganization 评价稍高 |\n\n---\n\n## Questions for Authors\n\n1. Action probe R² 在 training set 还是 held-out test set 上计算？Train/test split 策略是什么（random timestep / demo-level / task-level）？\n2. 所有 head ablation（dominant 和 random）都 increase R²。是否意味着 L1 heads 对 action prediction 是 net-negative 的？如果是，\"dual routing-encoding function\" 如何成立？\n3. Untrained readout 在 L1 达到 100% classification，但 untrained 有 0/32 instruction-dominant heads。如果 12% incidental attention 已够 100% 分类，VLA training 将 attention 提高到 57.7% 的功能意义是什么？\n4. Linear probe gap (Δ=+0.324 at L14) vs MLP probe gap (Δ=+0.015 at L8) 差 ~20 倍，对结果解释有何影响？论文应以哪个为主？\n5. Pretrained Llama-2 的 mid-depth routing pattern 是 meaningful processing 还是 OOD response？用 random noise tokens 替代 visual tokens 是否会产生类似 pattern？\n6. Bootstrap CI 的 resampling unit 是什么？如何处理同一 demo 内时间步的高度自相关？\n7. RSA 显示 DINOv2 几何最优 (ρ=0.692)，R² 显示 VLA readout 功能最优 (0.678)。\"Vision encoder quality emerges as a key design lever\" 的操作化定义是什么？\n\n---\n\n## Missing References\n\n- **Hewitt & Liang (2019)** \"Designing and Interpreting Probes with Control Tasks\" [probe selectivity，直接相关方法论]\n- **Nili et al. (2014)** \"A Toolbox for Representational Similarity Analysis\" [RSA 统计推断最佳实践]\n- **Bills et al. (2023)** \"Language models can explain neurons in language models\" [mechanistic interp 方法论基础]\n- **Templeton et al. (2024)** \"Scaling monosemanticity\" [SAE 方法论，与 Swann 2026 相关]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (4.5/10)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Originality | 6/10 | 4/10 | 5/10 |\n| Quality/Soundness | 4/10 | 7/10 | 5.5/10 |\n| Clarity | 7/10 | 6/10 | 6.5/10 |\n| Significance | 5/10 | 4/10 | 4.5/10 |\n| Relevance to CoRL | 5/10 | 7/10 | 6/10 |\n\n**Confidence: High**\n\n**核心判断**: 实验设计和统计报告质量优秀，C2（routing reorganization）有实质价值。但存在四个结构性问题的联合影响：(1) ablation 因果推断方向反直觉且解释不 convincing，(2) probe 方法论有未公开的关键细节（train/test split, 自相关），(3) 单模型证据 vs 一般化声称，(4) 纯 representation analysis 无 behavioral validation 对 CoRL 不够。三大 contribution 中 C1 是架构验证、C3 是 metric-dependent observation，实质新颖性集中在 C2，而 C2 的因果证据链（ablation）存在方向性问题。当前版本 below acceptance threshold。\n\n**可修复性评估**: W1 (ablation) 需要新实验（细粒度 ablation curve + selective ablation + 更多 random subsets）或叙事大幅修改；W2 (probe split) 可通过补充说明和 demo-level split 重分析修复；W3 (overclaim) 可通过 framing 修改修复；W4 (behavioral validation) 需要 rollout 实验。如果时间允许（deadline May 29），W2+W3 可在 11 天内完成；W1 的新实验和 W4 的 rollout 验证时间紧张但可能可行。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 数据密度过高（~15 个数字），z=-2.73 和具体头数不适合 Abstract\n- \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 是 overclaim\n- 建议保留 2-3 个核心数字，移除统计细节\n\n### Introduction\n- 5 段结构完整，叙事逻辑清晰\n- Contribution (i) \"verifying architecture-expected specialization\" 作为 contribution 列首位降低 novelty 感知\n- Contribution (iii) 在 contribution 列表中提及 \"CKA diverges\" 让读者困惑\n\n### Related Work\n- 覆盖全面（VLAs, mechanistic interp, behavioral analysis, token specialization, similarity methods）\n- 与 Grant 2026 差异化清晰\n- 缺 Hewitt & Liang 2019 (probe design) 和 Nili 2014 (RSA statistics)\n\n### Method\n- 清晰可复现，四种方法选择有 justify\n- \"Why RSA over CKA\" 段落理由合理但不完全令人信服（未论证 rank-order 对 action prediction 更 relevant）\n- 缺少 train/test split 的明确说明\n\n### Experiments\n- Section 4.2: 结果 clean 但 C1 novelty 问题持续\n- Section 4.3: 最强贡献，三条件梯度有说服力。但 ablation 方向性问题（所有 ablation increase R²）严重削弱因果推断\n- Section 4.4: 数据详实但 CKA 矛盾仅在 Appendix 讨论\n\n### Discussion\n- 过于简短。Limitations 仅半段，嵌入 Discussion 而非独立 section\n- \"Speculative mechanistic interpretation\" 标题过于自我贬低\n- 缺少对 probe methodology limitations 和 behavioral validation gap 的讨论\n\n### Appendix\n- 内容丰富且组织良好（robustness, cross-benchmark, diagnostics）\n- CKA 矛盾结果和 QA probe 的 1pp 差异对主文叙事有重大影响，应在正文 summarize",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-18T09:17:26.475584+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4467
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-18T09:17:31.609248+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-4b: 初始化到 Issue Tracker 同步', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '审稿报告已提交'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-4b: 初始化到 Issue Tracker 同步', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4c: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '审稿报告已提交'}]"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-18T09:17:31.660065+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-18T09:17:40.375486+00:00_

## 审稿圆桌会议完成

**结果: Weak Reject (4.5/10)**，两位 Reviewer 高度共识（R1: 5/10, R2: 4/10）。

**4 个 CRITICAL 问题**:
1. **Ablation 因果推断方向问题** — 所有 ablation 都 increase R²，与 "dual function" 声称矛盾
2. **Probe train/test split 未说明** + 时间步自相关 + MLP/linear 20× gap 未讨论
3. **Abstract overclaim** — 一般化 VLA 声称 vs 单模型证据
4. **无 behavioral validation** — 对 CoRL 是重大结构性缺口

**3 个 WARNING**: C1 novelty 不足、RSA/CKA 分歧低估、RSA 统计依赖性、缺 GenAI 声明

**核心优势**: 阶乘实验设计严谨、统计报告高标准、C2 routing reorganization 有实质价值

报告已投递给 Research Director。Issue Tracker 已同步更新（11 个新 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 469 · 2026-05-18T09:17:43.218604+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。与 Reviewer 1 在 6/8 个 Weakness 上高度共识（C1 新颖性不足、ablation 逻辑、单模型泛化、缺少行为验证、RSA/CKA 分歧、pretrained OOD 问题）。R1 在 probe train/test split 和 RSA 统计依赖性方面提出了我遗漏的重要方法论关切。唯一部分 rebut 的是 R1-Q6（Mantel test 不是 conditional comparison 的最佳工具）和 3D-VLA 引用（关联度有限）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 470 · 2026-05-18T09:17:54.520545+00:00_

审稿圆桌会议已完成。

**汇总结果**：

- **评分**: Weak Reject (4.5/10)，两位 Reviewer 高度共识（R1: 5/10, R2: 4/10）
- **Round 1 即收敛**，无需进入 Round 2
- **审稿报告已投递** Research Director
- **Issue Tracker 已同步**：4 个 CRITICAL + 3 个 WARNING + 4 个 INFO 新 open issues

**四个结构性问题**：
1. Ablation 因果推断方向反直觉（所有 ablation increase R²）
2. Probe train/test split 未说明 + 时间步自相关
3. 单模型证据 vs Abstract 一般化声称
4. 纯 representation analysis 无 behavioral validation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 50

## Round 50

22 recorded events


### User

_source line 471 · 2026-05-18T13:34:17.868463+00:00_

[Round 6 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/vla-ssd/artifacts/review_reports/round_5.md`
跨轮次问题追踪: `projects/vla-ssd/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-18T13:34:38.614902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "offset": "380",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "offset": "380",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-18T13:34:38.665763+00:00_

380	  - id: R5-W3
381	    summary: "C3 Abstract 权重过高"
382	    category: framing
383	    severity: warning
384	    status: resolved
385	    first_raised_round: 5
386	    last_seen_round: 5
387	    resolution: "C3 压缩至单句。"
388	    resolution_round: 5
389	    mentions: []
390	    action_items: []
391	
392	  - id: R5-W4
393	    summary: "缺 causal tracing / tuned lens 引用"
394	    category: writing
395	    severity: warning
396	    status: resolved
397	    first_raised_round: 5
398	    last_seen_round: 5
399	    resolution: "Meng + Belrose added。"
400	    resolution_round: 5
401	    mentions: []
402	    action_items: []
403	
404	  - id: R5-I1
405	    summary: "Appendix A.6 single-seed"
406	    category: experiment
407	    severity: info
408	    status: resolved
409	    first_raised_round: 5
410	    last_seen_round: 5
411	    resolution: "3 seeds × 3 conditions, all patterns robust。"
412	    resolution_round: 5
413	    mentions: []
414	    action_items: []
415	
416	  # ============================================================
417	  # Round 6 issues
418	  # ============================================================
419	  - id: R6-C1
420	    summary: "Ablation 因果推断方向问题：所有 ablation increase R²，解释不 convincing"
421	    category: experiment
422	    severity: critical
423	    status: in_progress
424	    first_raised_round: 6
425	    last_seen_round: 6
426	    mentions:
427	      - round: 6
428	        reviewers: [1, 2]
429	        note: "全票共识。'dual function' 是 post-hoc rationalization。更 parsimonious: L1 heads 普遍添加 interference。"
430	    action_items:
431	      - round: 6
432	        action: "叙事从 'dual function' 改为 'routing-first': routing 信号是 action probe 噪声，移除→R²↑ 正是 routing 证据。跨层数据已有 (L1:+0.059>>L8:+0.018>>L13:≈0)"
433	        assigned_to: paper_agent
434	        status: done
435	    resolution: ""
436	    resolution_round: null
437	
438	  - id: R6-C2
439	    summary: "Probe train/test split 未说明 + 时间自相关 + linear/MLP 20× gap"
440	    category: method
441	    severity: critic
…[truncated 5747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-18T13:34:38.967718+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/ 2>/dev/null",
  "description": "List available review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/ 2>/dev/null",
    "description": "List available review reports"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-18T13:34:39.221291+00:00_

total 80
drwxr-xr-x  2 ubuntu ubuntu  4096 May 18 09:17 .
drwxr-xr-x 16 ubuntu ubuntu  4096 May 18 12:18 ..
-rw-r--r--  1 ubuntu ubuntu 11054 May 17 04:44 round_1.md
-rw-r--r--  1 ubuntu ubuntu  8844 May 17 06:11 round_2.md
-rw-r--r--  1 ubuntu ubuntu 13262 May 17 18:21 round_3.md
-rw-r--r--  1 ubuntu ubuntu 16216 May 18 02:05 round_4.md
-rw-r--r--  1 ubuntu ubuntu 12575 May 18 09:17 round_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-18T13:34:52.135839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-18T13:34:52.638288+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we validate the framework by confirming architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions), while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31); instruction classification reaches $99.6\%$ at L1 (vs.\ pretrained $80.2\%$), and L1 ablation confirms routing-first head specialization (random-subset control, L1-confined). Untrained models show zero instruction-dominant heads throughout.
6	Third, vision encoder representations follow a metric-dependent non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L14; RSA confirms but CKA diverges; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-18T13:34:52.689109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-18T13:34:52.991197+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). The MLP probe is overparameterized ($N/\text{params} \approx 0.06$); early stopping mitigates overfitting, and all patterns reproduce with a linear probe ($N/\text{params} \approx 2.2$; Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind.}
21	At the image\_mean position, instruction classification remains at chance (
…[truncated 11395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-18T13:34:52.991572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-18T13:34:53.042010+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind; the readout is the sole multimodal convergence point.
6	Training shifts routing from mid-depth to entry-exit (L0--L1, L31), with effects at the readout ($R^2$ $+0.069$) rather than images ($\Delta \leq 1.7\%$).
7	This instruction-blindness explains the visual dominance reported by Grant et al.~\cite{grant2026}: under RSA, DINOv2 achieves the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$), pointing to instruction-conditioned integration.
8	
9	\paragraph{Mechanistic hypothesis and implications.}
10	Per-layer RSA bifurcates after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually while image\_mean drops sharply ($\to 0.422$), consistent with mid-layer integration and deep-layer compression.
11	L1 ablation confirms routing-first specialization ($z = -2.73$ vs.\ random subsets) and is L1-confined ($|\Delta R^2| < 0.02$ at deeper layers).
12	Action trajectory analysis confirms the causal role ($d = 0.65$, $72.3\%$ divergence); the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation.
13	
14	\paragraph{Limitations and scope.}
15	We study OpenVLA-7B on LIBERO. OpenVLA shares the dominant VLA design with RT-2~\cite{brohan2023_rt2} and $\pi_0$~\cite{black2024_pi0}; C1 follows from shared architectural constraints, but C2 may differ across backbone scales and decoder paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
16	
17	\paragraph{Use of Generative AI.}
18	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-18T13:34:57.324956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-18T13:34:57.927725+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), a Multi-Layer Perceptron (MLP) projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B~\cite{touvron2023_llama2} language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (no task-specific fine-tuning) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tabletop tasks, 50 demonstrations each).
12	To disentangle the contributions of language pretraining and VLA fine-tuning, we compare three LLM conditions: (1)~VLA-trained (the released checkpoint), (2)~Llama-2 base (the pretrained LLM backbone without VLA fine-tuning), and (3)~untrained (all 6.74B LLM parameters reinitialized via \texttt{from\_config()}).
13	All three conditions share the same frozen vision encoder and projector architecture.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the activation at the final pre-action token position at each layer;
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} 
…[truncated 4675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-18T13:34:57.978468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-18T13:34:58.029198+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	While the decoder-only architecture imposes structural constraints on information flow (the causal mask prevents image tokens from attending to subsequent instruction tokens), how VLA fine-tuning reshapes the routing and integration of multimodal information within the LLM backbone remains uncharacterized.
6	
7	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
8	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
9	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
10	
11	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
12	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
13	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\c
…[truncated 2520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-18T13:35:27.950367+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 读取 issue tracker + 论文修改内容', 'status': 'completed', 'activeForm': '已读取'}, {'content': 'Step 1: 分派 Reviewer 进行修订评估', 'status': 'in_progress', 'activeForm': '分派 Reviewer 修订评估任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 读取 issue tracker + 论文修改内容', 'status': 'completed', 'activeForm': '已读取'}, {'content': 'Step 1: 分派 Reviewer 进行修订评估', 'status': 'in_progress', 'activeForm': '分派 Reviewer 修订评估任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': 'Reviewer 交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-18T13:35:28.001059+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-18T13:35:57.022266+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Round 2 修订评估 — Reviewer 1\n\n### 背景\n上一轮（Round 1）你侧重方法严谨性+实验设计，给出 5/10。论文已根据审稿意见进行修改。本轮任务是**逐条验证 open/in_progress issues 是否已充分修复**，并识别修改是否引入新问题。\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含所有 .tex 子文件）\n**Venue**: CoRL 2026, Deadline May 29\n\n### Open/In-Progress Issues（你的上轮主要发现）\n\n请逐条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由：\n\n**R6-C1 [CRITICAL]: Ablation 因果推断方向问题**\n- 上轮问题：所有 ablation increase R²，\"dual function\" 是 post-hoc rationalization\n- 修改措施：叙事改为 \"routing-first specialization\"（Section 4.3 ¶4, line 80）；新增 \"Action trajectory validation\" 段落（lines 83-87）：L1 ablation 改变 72.3% action tokens (d=0.65)，control ablation d=0.41\n- 验证要点：(a) \"routing-first\" 解释是否比 \"dual function\" 更 convincing？(b) 所有 ablation 仍 increase R² 的基本事实是否被充分 address？(c) action trajectory analysis 是否弥补了因果推断？(d) N=10 random subsets 是否增加？\n\n**R6-C2 [CRITICAL]: Probe train/test split 未说明 + 时间自相关**\n- 上轮问题：train/test split 未说明，时间步自相关导致 CI 低估\n- 修改措施：Method §3.6 (line 59) 新增 \"Probes are trained on demos 0--39 and evaluated on held-out demos 40--49 (demo-level split), ensuring zero temporal overlap\"\n- 验证要点：(a) demo-level split 是否完全消除时间泄漏？(b) 80/20 split (40 train, 10 test) 是否合理？(c) linear vs MLP 20× gap 是否被讨论？\n\n**R6-C4 [CRITICAL]: 缺 behavioral validation**\n- 上轮问题：无 task success rate 连接\n- 修改措施：新增 \"Action trajectory validation\"（Section 4.3 lines 83-87）：open-loop action trajectory 分析（d=0.65, 72.3% token divergence）。Behavioral rollout 因 mujoco 版本不匹配无法实现。\n- 验证要点：(a) open-loop action trajectory 是否算 behavioral validation？(b) 是否足够回应 CoRL 审稿人对 behavioral evidence 的期望？(c) 这是 output-level 证据还是 representation-level 证据？\n\n**R6-W1 [WARNING]: RSA pairwise dependency**\n- 上轮问题：bootstrap 低估 variance\n- 修改措施：Method §3.5 (line 51) 改为 task-level block resampling，引用 Nili 2014\n- 验证要点：task-level resampling (N=10 tasks) 是否充分处理了依赖性？N=10 的 bootstrap 功效如何？\n\n### 同时检查\n- 上轮你的 W3（MLP probe overparameterization, linear vs MLP 20× gap）是否在正文讨论？\n- 修改是否引入新的方法论问题？\n\n### 输出格式\n```\n## Issue Verification\n- R6-C1: [RESOLVED/STILL_OPEN] — 理由\n- R6-C2: [RESOLVED/STILL_OPEN] — 理由\n- R6-C4: [RESOLVED/STILL_OPEN] — 理由\n- R6-W1: [RESOLVED/STILL_OPEN] — 理由\n\n## New Issues (if any)\n## Updated Assessment\nScore: X/10 (vs 上轮 5/10)\nDirection: ↑/↓/→\n```",
  "project": "vla-ssd"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Round 2 修订评估 — Reviewer 1\n\n### 背景\n上一轮（Round 1）你侧重方法严谨性+实验设计，给出 5/10。论文已根据审稿意见进行修改。本轮任务是**逐条验证 open/in_progress issues 是否已充分修复**，并识别修改是否引入新问题。\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含所有 .tex 子文件）\n**Venue**: CoRL 2026, Deadline May 29\n\n### Open/In-Progress Issues（你的上轮主要发现）\n\n请逐条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由：\n\n**R6-C1 [CRITICAL]: Ablation 因果推断方向问题**\n- 上轮问题：所有 ablation increase R²，\"dual function\" 是 post-hoc rationalization\n- 修改措施：叙事改为 \"routing-first specialization\"（Section 4.3 ¶4, line 80）；新增 \"Action trajectory validation\" 段落（lines 83-87）：L1 ablation 改变 72.3% action tokens (d=0.65)，control ablation d=0.41\n- 验证要点：(a) \"routing-first\" 解释是否比 \"dual function\" 更 convincing？(b) 所有 ablation 仍 increase R² 的基本事实是否被充分 address？(c) action trajectory analysis 是否弥补了因果推断？(d) N=10 random subsets 是否增加？\n\n**R6-C2 [CRITICAL]: Probe train/test split 未说明 + 时间自相关**\n- 上轮问题：train/test split 未说明，时间步自相关导致 CI 低估\n- 修改措施：Method §3.6 (line 59) 新增 \"Probes are trained on demos 0--39 and evaluated on held-out demos 40--49 (demo-level split), ensuring zero temporal overlap\"\n- 验证要点：(a) demo-level split 是否完全消除时间泄漏？(b) 80/20 split (40 train, 10 test) 是否合理？(c) linear vs MLP 20× gap 是否被讨论？\n\n**R6-C4 [CRITICAL]: 缺 behavioral validation**\n- 上轮问题：无 task success rate 连接\n- 修改措施：新增 \"Action trajectory validation\"（Section 4.3 lines 83-87）：open-loop action trajectory 分析（d=0.65, 72.3% token divergence）。Behavioral rollout 因 mujoco 版本不匹配无法实现。\n- 验证要点：(a) open-loop action trajectory 是否算 behavioral validation？(b) 是否足够回应 CoRL 审稿人对 behavioral evidence 的期望？(c) 这是 output-level 证据还是 representation-level 证据？\n\n**R6-W1 [WARNING]: RSA pairwise dependency**\n- 上轮问题：bootstrap 低估 variance\n- 修改措施：Method §3.5 (line 51) 改为 task-level block resampling，引用 Nili 2014\n- 验证要点：task-level resampling (N=10 tasks) 是否充分处理了依赖性？N=10 的 bootstrap 功效如何？\n\n### 同时检查\n- 上轮你的 W3（MLP probe overparameterization, linear vs MLP 20× gap）是否在正文讨论？\n- 修改是否引入新的方法论问题？\n\n### 输出格式\n```\n## Issue Verification\n- R6-C1: [RESOLVED/STILL_OPEN] — 理由\n- R6-C2: [RESOLVED/STILL_OPEN] — 理由\n- R6-C4: [RESOLVED/STILL_OPEN] — 理由\n- R6-W1: [RESOLVED/STILL_OPEN] — 理由\n\n## New Issues (if any)\n## Updated Assessment\nScore: X/10 (vs 上轮 5/10)\nDirection: ↑/↓/→\n```",
    "project": "vla-ssd"
  }
}
````

</details>

---


### Tool result

_source line 489 · 2026-05-18T13:36:15.021668+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17999
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-18T13:36:15.725136+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Round 2 修订评估 — Reviewer 2\n\n### 背景\n上一轮（Round 1）你侧重新颖性+叙事完整性+格式合规，给出 4/10 (Weak Reject)。论文已根据审稿意见进行修改。本轮任务是**逐条验证 open/in_progress issues 是否已充分修复**，并识别修改是否引入新问题。\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含所有 .tex 子文件）\n**Venue**: CoRL 2026, Deadline May 29\n\n### Open/In-Progress Issues（你的上轮主要发现）\n\n请逐条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由：\n\n**R6-C1 [CRITICAL]: Ablation \"dual function\" → \"routing-first\" 叙事修改**\n- 上轮问题：所有 ablation increase R²，\"dual function\" 是 post-hoc rationalization\n- 修改措施：Section 4.3 ¶4 (line 80) 改为 \"routing-first specialization: these heads carry organized instruction signals that the action probe treats as structured noise\"；新增 action trajectory validation (lines 83-87, d=0.65)\n- 验证要点：(a) \"routing-first\" 叙事是否解决了\"所有 ablation increase R²\"的方向性问题？(b) action trajectory analysis 是否提供了 ablation 缺乏的因果证据？\n\n**R6-C3 [CRITICAL]: 单模型 Abstract overclaim**\n- 上轮问题：Abstract 用一般化措辞但仅单模型证据\n- 修改措施：Abstract line 7 改为 \"in the model studied\"；Introduction contribution (ii) 加 \"demonstrated on OpenVLA-7B/LIBERO\"\n- 验证要点：(a) qualify 是否充分？(b) Introduction ¶3-4 的 three findings 描述是否也已 qualify？(c) Discussion 中是否仍有 unqualified general claims？\n\n**R6-C4 [CRITICAL]: 缺 behavioral validation**\n- 上轮问题：representational findings 未连接 task success rate\n- 修改措施：新增 \"Action trajectory validation\"（Section 4.3 lines 83-87）：open-loop action token 分析（72.3% divergence, d=0.65），但无 closed-loop rollout\n- 验证要点：(a) open-loop action trajectory 对 CoRL 审稿人来说是否足够？(b) Discussion 中 \"early-layer parameters may suffice\" 是否仍 speculative？(c) 是否应更明确地标注 behavioral validation 的缺失？\n\n**R6-W1 [WARNING]: RSA pairwise dependency**\n- 修改措施：Method §3.5 (line 51) task-level block resampling + Nili 2014 引用\n- 验证要点：处理是否充分？\n\n### 同时检查\n\n1. **已 resolved 的 issues 验证**：\n   - R6-W2: GenAI disclosure 是否存在且完整？（Discussion 末尾）\n   - R6-W3: Abstract 数据密度是否改善？\n   - R6-I2: 缺失引用（Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024）是否已添加？\n   - R6-I3: Table 2 caption 是否自包含？Discussion \"Speculative\" 是否改为 \"Mechanistic hypothesis\"？\n\n2. **C1 novelty 问题**（上轮 R2-W1 + R1-W1）：C1 仍列为 contribution (i)——\"verifying architecture-expected specialization\"。是否仍是 novelty 瓶颈？\n\n3. **C3 metric-dependence**（上轮 R2-W5）：CKA 分歧是否在正文（非仅 Appendix）被更充分地讨论？\n\n4. **修改是否引入新问题？**\n\n### 输出格式\n```\n## Issue Verification\n- R6-C1: [RESOLVED/STILL_OPEN] — 理由\n- R6-C3: [RESOLVED/STILL_OPEN] — 理由\n- R6-C4: [RESOLVED/STILL_OPEN] — 理由\n- R6-W1: [RESOLVED/STILL_OPEN] — 理由\n\n## Resolved Issues Quick Check\n- R6-W2: [CONFIRMED/ISSUE]\n- R6-W3: [CONFIRMED/ISSUE]\n- R6-I2: [CONFIRMED/ISSUE]\n- R6-I3: [CONFIRMED/ISSUE]\n\n## Persistent Issues (from Round 1 not explicitly tracked)\n## New Issues (if any)\n## Updated Assessment\nScore: X/10 (vs 上轮 4/10)\nDirection: ↑/↓/→\n```",
  "project": "vla-ssd"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Round 2 修订评估 — Reviewer 2\n\n### 背景\n上一轮（Round 1）你侧重新颖性+叙事完整性+格式合规，给出 4/10 (Weak Reject)。论文已根据审稿意见进行修改。本轮任务是**逐条验证 open/in_progress issues 是否已充分修复**，并识别修改是否引入新问题。\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含所有 .tex 子文件）\n**Venue**: CoRL 2026, Deadline May 29\n\n### Open/In-Progress Issues（你的上轮主要发现）\n\n请逐条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由：\n\n**R6-C1 [CRITICAL]: Ablation \"dual function\" → \"routing-first\" 叙事修改**\n- 上轮问题：所有 ablation increase R²，\"dual function\" 是 post-hoc rationalization\n- 修改措施：Section 4.3 ¶4 (line 80) 改为 \"routing-first specialization: these heads carry organized instruction signals that the action probe treats as structured noise\"；新增 action trajectory validation (lines 83-87, d=0.65)\n- 验证要点：(a) \"routing-first\" 叙事是否解决了\"所有 ablation increase R²\"的方向性问题？(b) action trajectory analysis 是否提供了 ablation 缺乏的因果证据？\n\n**R6-C3 [CRITICAL]: 单模型 Abstract overclaim**\n- 上轮问题：Abstract 用一般化措辞但仅单模型证据\n- 修改措施：Abstract line 7 改为 \"in the model studied\"；Introduction contribution (ii) 加 \"demonstrated on OpenVLA-7B/LIBERO\"\n- 验证要点：(a) qualify 是否充分？(b) Introduction ¶3-4 的 three findings 描述是否也已 qualify？(c) Discussion 中是否仍有 unqualified general claims？\n\n**R6-C4 [CRITICAL]: 缺 behavioral validation**\n- 上轮问题：representational findings 未连接 task success rate\n- 修改措施：新增 \"Action trajectory validation\"（Section 4.3 lines 83-87）：open-loop action token 分析（72.3% divergence, d=0.65），但无 closed-loop rollout\n- 验证要点：(a) open-loop action trajectory 对 CoRL 审稿人来说是否足够？(b) Discussion 中 \"early-layer parameters may suffice\" 是否仍 speculative？(c) 是否应更明确地标注 behavioral validation 的缺失？\n\n**R6-W1 [WARNING]: RSA pairwise dependency**\n- 修改措施：Method §3.5 (line 51) task-level block resampling + Nili 2014 引用\n- 验证要点：处理是否充分？\n\n### 同时检查\n\n1. **已 resolved 的 issues 验证**：\n   - R6-W2: GenAI disclosure 是否存在且完整？（Discussion 末尾）\n   - R6-W3: Abstract 数据密度是否改善？\n   - R6-I2: 缺失引用（Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024）是否已添加？\n   - R6-I3: Table 2 caption 是否自包含？Discussion \"Speculative\" 是否改为 \"Mechanistic hypothesis\"？\n\n2. **C1 novelty 问题**（上轮 R2-W1 + R1-W1）：C1 仍列为 contribution (i)——\"verifying architecture-expected specialization\"。是否仍是 novelty 瓶颈？\n\n3. **C3 metric-dependence**（上轮 R2-W5）：CKA 分歧是否在正文（非仅 Appendix）被更充分地讨论？\n\n4. **修改是否引入新问题？**\n\n### 输出格式\n```\n## Issue Verification\n- R6-C1: [RESOLVED/STILL_OPEN] — 理由\n- R6-C3: [RESOLVED/STILL_OPEN] — 理由\n- R6-C4: [RESOLVED/STILL_OPEN] — 理由\n- R6-W1: [RESOLVED/STILL_OPEN] — 理由\n\n## Resolved Issues Quick Check\n- R6-W2: [CONFIRMED/ISSUE]\n- R6-W3: [CONFIRMED/ISSUE]\n- R6-I2: [CONFIRMED/ISSUE]\n- R6-I3: [CONFIRMED/ISSUE]\n\n## Persistent Issues (from Round 1 not explicitly tracked)\n## New Issues (if any)\n## Updated Assessment\nScore: X/10 (vs 上轮 4/10)\nDirection: ↑/↓/→\n```",
    "project": "vla-ssd"
  }
}
````

</details>

---


### Tool result

_source line 491 · 2026-05-18T13:36:17.234734+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1509
}
```

</details>

---


### Assistant

_source line 492 · 2026-05-18T13:36:20.380535+00:00_

Round 2 修订评估任务已分派给两位 Reviewer，等待审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 493 · 2026-05-18T13:39:08.937681+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 2 修订评估

---

## Issue Verification

### R6-C1 [CRITICAL]: Ablation 因果推断方向问题 — [STILL_OPEN] (partially improved)

**修改内容确认**:
- Section 4.3 ¶4 (line 80): "dual routing-encoding function" → "routing-first specialization"，新解释为 dominant heads 携带 organized instruction signals 被 probe 视为 structured noise，因此 ablation 增幅较小
- 新增 "Action trajectory validation"（lines 83-87）: L1 ablation 改变 72.3% action tokens (d=0.65)，control ablation d=0.41; gripper dimension 主导效应 (shift 0.291 vs <0.034)
- Appendix A.6: per-dimension 分析，per-task Cohen's d (0.43-0.73)，KL divergence (5.08 vs 1.69)

**仍存在的问题**:

(a) **核心矛盾未解决**: ALL ablation（dominant 和 random）仍然 increase R²。"Routing-first specialization" 是对 "dual function" 的措辞改进，但逻辑结构相同——仍是对 "为什么 dominant heads ablation 增幅更小" 的 post-hoc 解释，未正面回答 "为什么移除任何 24/32 heads 都提升 action prediction" 这个根本问题。

(b) **Discussion 的自相矛盾**: Discussion line 12 写 "the effect distributes across L1 heads rather than concentrating in instruction-dominant ones"。如果 ablation 效应均匀分布在所有 L1 heads 上（而非集中在 instruction-dominant heads），这恰恰削弱了 "routing-first specialization" 的 claim——因为 instruction-dominant heads 没有表现出与其他 heads 不同的特殊功能。

(c) **N=10 random subsets 未增加**: 仍然是 10 个随机子集的 z-test。上轮我和 R2 都指出这个样本量对统计推断不足。未修改。

(d) **效应范围窄于 claim**: 新的 trajectory analysis 揭示效应主要集中在 gripper dimension (0.291 vs continuous dimensions <0.034)。这意味着 L1 instruction routing 的 "causal role" 主要影响 discrete open/close 决策，而非连续运动控制。但正文仍将其叙述为 general "routing function"，未缩小 claim scope。

**积极改进**: Trajectory analysis 本身有价值——从 representation-level（probe R²）推进到 output-level（action token prediction），是正确方向。但不足以完全 resolve 因果推断问题。

**建议**: (a) 正文中显式承认 "所有 24-head ablation 均提高 R²" 这一事实并讨论其含义（如 L1 heads 可能普遍冗余）；(b) 增加 random subsets 至 ≥50；(c) 限定 claim scope 至 gripper/discrete 控制。

---

### R6-C2 [CRITICAL]: Probe train/test split + 时间自相关 — [RESOLVED]

**修改内容确认**:
- Method §3.6 line 59: "Probes are trained on demos 0-39 and evaluated on held-out demos 40-49 (demo-level split), ensuring zero temporal overlap between training and evaluation trajectories."

**评估**:
- Demo-level split 完全消除了时间泄漏（不同 demo 之间无时间连续性）
- 80/20 split (40 train / 10 test per task) 是合理比例
- R² 现在明确是 held-out 数据上的值，解决了上轮对 overparameterized MLP probe R² 可信度的核心担忧
- Section 4.1 line 12 对 overparameterization 的讨论已有，指向 linear probe 复制

**残余小问题**: Linear vs MLP 20× gap（Δ = +0.324 vs +0.015）仍未在主正文中讨论。Appendix A.6 的 framing（"VLA training reorganizes representations to make action information more linearly decodable"）是一种合理解释但排除了替代解释（MLP 过于强大压缩了条件间差异）。这是 [INFO] 级别问题，不阻碍接收。

---

### R6-C4 [CRITICAL]: 缺 behavioral validation — [STILL_OPEN] (partially improved)

**修改内容确认**:
- 新增 "Action trajectory validation"（Section 4.3, lines 83-87）
- MuJoCo 版本不匹配导致无法 rollout

**评估**:

(a) **Open-loop trajectory analysis 不是 behavioral validation**。它测量的是 "ablation 改变了模型的 action token 预测"，这是 output-level 证据而非 behavioral 证据。真正的 behavioral validation 需要 closed-loop rollout：在环境中执行修改后的 action 序列并测量 task success rate。

(b) **对 CoRL 仍是显著缺口**: Cohen's d = 0.65 和 72.3% token divergence 告诉我们 ablation 改变了预测，但不知道预测变好还是变差。可能 ablation 后的 actions 更好（R² 增加暗示如此），也可能在实际环境中因失去 instruction conditioning 而失败。

(c) **进步方向正确**: 从纯 representation-level（R², RSA ρ）推进到 output-level（action token comparison）是有意义的改善。MuJoCo 版本限制是可理解的技术障碍。

(d) **建议**: 如果 closed-loop rollout 确实不可行，至少在 Discussion/Limitations 中明确承认这一 gap 并讨论 output-level 与 behavioral-level 证据的区别。当前 Discussion（line 12）将 trajectory analysis 描述为 "confirms the causal role"，这对 "causal role" 的定义过宽。

---

### R6-W1 [WARNING]: RSA pairwise dependency — [RESOLVED]

**修改内容确认**:
- Method §3.5 line 51: "resampling is performed at the task level (N=10), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure [nili2014toolbox]."

**评估**:
- Task-level block resampling 是处理 RDM pairwise dependency 的标准做法（Nili et al. 2014）
- 引用正确的方法论文献
- 这解决了核心统计问题：不再将非独立的 pairwise distances 当作独立样本

**残余注意**: N=10 tasks 的 bootstrap 功效有限（10^10 种可能的重抽样中很多高度相似），但这是实验设计的固有限制（LIBERO 只有 10 tasks），非方法论错误。论文应意识到这使得 CI 偏宽，但不需要额外修改。

---

## 上轮 W3（MLP probe overparameterization）检查

- **主正文**: Section 4.1 line 12 承认 overparameterized 并指向 linear probe。未讨论 20× gap。
- **Appendix A.6**: 讨论了 gap 但 framing 单一（仅 "linear decodability" 解释）
- **评估**: 现在 R² 是 held-out 数据上的值（R6-C2 resolved），overparameterization 的实际危害已大幅降低。20× gap 的 under-discussion 降级为 minor concern。

---

## New Issues

### N1 [WARNING]: Discussion 中的自相矛盾

Discussion line 12: "the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation."

这两个半句互相矛盾：
- 前半句说 ablation 效应均匀分布（不集中在 instruction-dominant heads）
- 后半句仍然推论 L0-L1 instruction routing 的特殊意义

如果 ablation 效应不集中在 instruction-dominant heads，那么 "routing concentration" 的功能特异性就被削弱了。这里需要更 careful 的逻辑连接。

### N2 [INFO]: conclusion.tex 仍未编译

main.tex 仍然不包含 `\input{conclusion}`。R2 上轮指出的 W8 未修复。虽然 Discussion 末尾有总结性内容，但结构不完整。

### N3 [INFO]: Conclusion 中的 claim 未更新

conclusion.tex line 5: "Vision encoder quality emerges as a key design lever" — 此 claim 在上轮两位 reviewer 的交叉审查中被质疑（RSA 最高 vs R² 最高指向不同表征），修订后未修改。但因 conclusion.tex 未编译，此问题暂不影响已编译的论文。

---

## Updated Assessment

```
Score: 6/10 (vs 上轮 5/10)
Direction: ↑ (小幅上升)
```

**评分理由**:

**上升因素**:
- R6-C2 完全解决（demo-level split，R² 现为 held-out 值）→ 消除了 probe 结果可信度的根本疑虑
- R6-W1 完全解决（task-level block resampling + Nili 2014）
- Action trajectory analysis 虽非 behavioral validation 但提供了 output-level 因果证据
- Abstract 修改改善了 claim scope（"in the model studied"、C1 降格为 "validate"）
- GenAI 声明已添加
- "routing-first specialization" 比 "dual function" 更准确（虽仍不完全 convincing）

**限制上升幅度的因素**:
- R6-C1 核心矛盾未解决（all ablation increase R²，Discussion 自相矛盾）
- R6-C4 仍无 behavioral validation（trajectory analysis ≠ rollout success）
- N=10 random subsets 未增加
- 单模型+单 benchmark 的 generalization 问题未改变（上轮 W6，无法在修订期间解决）
- Linear vs MLP 20× gap 仍未在正文讨论

**总结**: 方法论层面的两个关键修复（probe split 和 RSA bootstrap）显著提升了统计推断的可信度，使 Finding 2（routing reorganization）和 Finding 3（inverted-U）的定量证据更可信。但 ablation 的因果推断逻辑和 behavioral validation 缺口仍是影响接收决定的 open issues。论文从 "marginally below" 升至 "marginally above"，条件是：(a) ablation 的 claim scope 需要缩小/限定；(b) behavioral gap 需在 Limitations 中更坦诚讨论。

**Confidence**: 4/5 (confident)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 494 · 2026-05-18T13:39:14.384105+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 495 · 2026-05-18T13:39:16.996687+00:00_

[Reviewer 1 审稿结果]:
Round 2 修订评估已提交。

核心结论：
- **R6-C2 (probe split)** 和 **R6-W1 (RSA bootstrap)** 已完全解决
- **R6-C1 (ablation)** 部分改善但核心矛盾未解——所有 ablation 增加 R² 的事实未正面回应，Discussion 存在自相矛盾
- **R6-C4 (behavioral validation)** 部分改善——trajectory analysis 提供 output-level 证据，但非 behavioral validation
- 评分从 5/10 上升至 6/10（marginally above threshold），方向 ↑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 496 · 2026-05-18T13:39:23.367385+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 53

## Round 53

8 recorded events


### User

_source line 497 · 2026-05-18T13:39:24.874208+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 2 修订评估

**上轮评分**: 4/10 (Weak Reject)

---

## Issue Verification

### R6-C1 [STILL_OPEN — 部分改善]: Ablation "routing-first" 叙事修改

**(a) "routing-first" 叙事是否解决了方向性问题？**

部分改善但核心问题仍在。Section 4.3 line 80 的新表述——"these heads carry organized instruction signals that the action probe treats as structured noise, so removing them yields a modest increase"——比原来的 "dual function" 更诚实，承认了 R² 上升的事实。但 "structured noise" 本身仍是 post-hoc rationalization：如果 instruction signals 对 action prediction 是 noise，那说明 instruction routing 和 action encoding 是分离的，而非 integrated。这与论文 Discussion line 12 声称的 "routing-first specialization" 存在张力——如果 routing 和 encoding 分离，那 "specialization" 的 functional significance 是什么？

更根本的问题：所有 24-head ablation（无论 dominant 还是 random）都 increase R²，说明 L1 作为整体对 downstream probe 有 interference。dominant heads 增加少（+0.042 vs +0.077），最 parsimonious 的解释是它们的 interference 少（因为 organized signals 比 random noise 更 structured），而非它们有某种 "routing-first" 的特殊功能。

**(b) Action trajectory validation 是否提供因果证据？**

Action trajectory analysis（lines 83-87, Appendix §Action Trajectory Analysis Details）是有价值的新增内容。关键数据：
- Instruction-head ablation: 72.3% token divergence, d=0.65
- Control ablation (8 non-instruction heads): 29.3% divergence, d=0.41
- 效应集中在 gripper 维度（shift 0.291 vs <0.034 for continuous dims）

这证明 L1 heads 确实因果性地影响 action token 生成。但存在新的 internal inconsistency：
1. R² ablation 测的是 continuous action prediction，显示 dominant heads removal 反而帮助 R²
2. Trajectory analysis 显示效应集中在 gripper（离散 open/close），不在连续维度
3. 这两个结果实际上讲的是不同故事：R² improvement from ablation 可能是因为 instruction routing 对连续维度确实是 noise，而 trajectory divergence 主要来自离散 gripper 维度

论文没有讨论这个维度分离（连续 vs 离散）对 "routing-first specialization" 解释的影响。

此外，line 86 提到 "Per-head effects are comparable; L1 attention collectively influences action generation rather than through a specialized subset"——这实际上 undermines 了 instruction-dominant heads 的特殊地位：如果所有 heads 的 per-head effect 类似，那 instruction routing 并没有独特的 causal role。

**评级**：从 CRITICAL 降为 WARNING。新叙事更准确，trajectory validation 增加了因果证据，但 interpretation 仍有 internal inconsistency。

---

### R6-C3 [STILL_OPEN — 大部分改善]: Abstract overclaim

**(a) Abstract qualification**: Abstract line 7 "in the model studied" ✓ 到位。

**(b) Introduction findings 是否 qualified？**: Introduction lines 15-21 的 "Three findings emerge" 仍用一般化语言：
- Line 16: "the VLA exhibits strict token-level functional specialization"（无 model qualification）
- Line 17: "VLA fine-tuning front-loads instruction routing"（泛指 VLA fine-tuning）
- Line 20: "vision encoder representations undergo a non-monotonic transformation"（泛指）

Contribution (ii) 加了 "demonstrated on OpenVLA-7B/LIBERO" ✓，但 Contribution (i) 和 (iii) 仍无 model-specific qualification。

**(c) Discussion 是否有 unqualified claims？**: Discussion line 12 "L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation"——仍是 unqualified general claim。Conclusion line 4 同样用 general "a VLA" 而非 "OpenVLA-7B"。

**评级**：从 CRITICAL 降为 WARNING。Abstract 改善显著，但 Introduction findings 段落和 Conclusion 仍有遗漏。

---

### R6-C4 [STILL_OPEN — 部分改善]: 缺 behavioral validation

**(a) Open-loop trajectory 是否足够？**: Action trajectory analysis（lines 83-87）是一种 behavioral proxy：它测量 predicted action tokens 的变化而非 frozen representations 上的 probe R²。这比 Round 1 的纯 representational analysis 有进步。但对 CoRL 审稿人而言，open-loop action token 变化 ≠ closed-loop task success rate。核心问题：72.3% 的 action token 变化是否导致 task failure？如果 ablation 后模型仍能完成任务（因为 gripper timing 有容错空间），那 d=0.65 的 "大效应" 在 behavioral 层面可能无足轻重。

**(b) "early-layer parameters may suffice" 是否仍 speculative？**: Discussion line 12 仍写 "L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation"。没有任何实验验证（如 freeze experiments 或 LoRA on early layers）。仍然是 speculative。

**(c) 应否更明确标注 behavioral validation 缺失？**: Limitations paragraph（Discussion lines 14-15）仅说 "C2 may differ across backbone scales and decoder paradigms"，没有提到 behavioral validation 的缺失。建议在 Limitations 中明确写出：本文所有分析均在 representational/open-loop 层面，未进行 closed-loop rollout validation。

**评级**：保持 CRITICAL（对 CoRL 而言）。Open-loop trajectory 是进步，但不足以替代 behavioral validation。如果论文加一句明确承认这一限制并将 architectural implications 标注为 hypothesis 而非 conclusion，可降为 WARNING。

---

### R6-W1 [RESOLVED]: RSA pairwise dependency

Method §3.5 line 51: "resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}"

这是正确的处理方式。Task-level block resampling 保留了 within-task pairwise dependency，N=10 tasks 作为 resampling unit 也是 honest 的（虽然 effective N=10 很小，导致 CI 较宽，但这正是 conservative 的正确方向）。Nili 2014 引用到位。

**评级**：RESOLVED。

---

## Resolved Issues Quick Check

### R6-W2 (GenAI disclosure): [CONFIRMED] ✓
Discussion lines 17-18: "Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors." 内容完整，符合 CoRL 2026 要求。

### R6-W3 (Abstract 数据密度): [ISSUE — 轻微改善]
Abstract 仍包含约 12 个具体数值（chance/10%, 100%, L1, L0-L1, L31, 99.6%, 80.2%, L8-L14, +0.069, +46pp, ≤0.017）。相比 Round 1 的 ~15 个减少了少量（去掉了 z=-2.73 和部分 head counts），但整体数据密度仍然偏高。Abstract line 5 在一句话中包含 6 个数字/符号。改善方向正确但幅度不足——不过考虑到论文的 technical analysis 性质，这在 acceptable 范围内。

### R6-I2 (缺失引用): [CONFIRMED] ✓
- Hewitt & Liang 2019 (control tasks): 已添加为 hewitt2019control，在 Related Work line 33 引用 ✓
- Nili et al. 2014: 已添加为 nili2014toolbox，在 Method line 51 引用 ✓
- Bills et al. 2023: 已添加为 bills2023language，在 Related Work line 14 引用 ✓
- Templeton et al. 2024: 已添加为 templeton2024scaling，在 Related Work line 14 引用 ✓

四篇全部添加且在正文中正确引用。

### R6-I3 (Table 2 caption / Discussion "Speculative"): [CONFIRMED] ✓
- Table 2 caption（experiments.tex line 91）现在解释了 Mode 列："Mode describes acquisition speed and retention: immed. = immediate, gradual = multi-layer, incid. = incidental; +stable = retained, +forget = decays." Caption 自包含。✓
- Discussion paragraph title 从 "Speculative mechanistic interpretation" 改为 "Mechanistic hypothesis and implications"（discussion.tex line 9）。✓

---

## Persistent Issues (from Round 1 not explicitly tracked)

### P1: C1 仍列为 contribution (i) — novelty 瓶颈

Introduction line 23 Contribution (i) 仍是 "a systematic experimental framework for token-level representational analysis of VLAs with factorial controls, verifying architecture-expected specialization between image and readout tokens."

修改方向正确：Abstract line 4 重新表述为 "we validate the framework by confirming architecture-expected token specialization"，将 C1 降格为 framework validation 而非独立 finding。但 Introduction 的 contribution 列表中，(i) 仍同时包含 framework + specialization verification，使其看起来像一个 compound contribution 而非 methodological validation。

建议：将 (i) 精简为 "a systematic experimental framework for token-level representational analysis of VLAs with factorial controls"，将 specialization verification 作为 framework 的 validation evidence 提及，而非 contribution 的一部分。

**严重程度**：WARNING。比 Round 1 改善，但仍是 novelty 的 soft weakness。

### P2: C3 metric-dependence — CKA 分歧仍主要在 Appendix

正文中的 CKA 提及：
- Introduction line 20: "CKA yields monotonically increasing layer profiles (Appendix~\ref{sec:cka_appendix})" — 仅一个括号
- Section 4.4 line 118: "this ordering is metric-dependent (Appendix~\ref{sec:cka_appendix})" — 仅一个括号
- Method §3.6 lines 63-66: "Why RSA over CKA" 段落有所扩充，新增 "RSA captures the relative distance structure among representations, which directly governs action prediction quality"

改善方向正确（"Why RSA over CKA" 的 justification 更强了），但 CKA 的具体矛盾结果（monotonic increase, reversed ordering）仍未在正文讨论。读者如果不翻 Appendix，不会知道有一个常用 metric 完全推翻了 C3 的 inverted-U。

建议：在 Section 4.4 加 1-2 句正文讨论 CKA 的矛盾，明确说 "non-monotonic pattern is specific to rank-order metrics (RSA, probes); global covariance metrics (CKA) show monotonic increase, indicating the refinement operates on geometric arrangement rather than overall representational structure."

**严重程度**：WARNING。

### P3: conclusion.tex 仍未编译

main.tex 仍然没有 \input{conclusion}。\input 序列为：introduction → related_work → method → experiments → discussion → bibliography → appendix。conclusion.tex 存在于同一目录但未被编译。这意味着编译后的 PDF 仍无 Conclusion section。

Round 1 中这被标记为 R2-W8，但本轮 open issues 列表中未追踪。

**严重程度**：INFO → WARNING。缺少 Conclusion 不会导致 desk reject，但 CoRL 论文通常有 Conclusion，且 conclusion.tex 第 6 行的 "Code and representations will be released upon acceptance" 是有价值的承诺，当前被浪费了。

### P4: Probe train/test split 现已明确（Round 1 R1-W3 关切已修复）

Method §3.6 line 59: "Probes are trained on demos 0--39 and evaluated on held-out demos 40--49 (demo-level split), ensuring zero temporal overlap between training and evaluation trajectories."

这直接回应了 R1-W3 和 R1-Q1 的关切。Demo-level split 消除了时间自相关导致的 train/test leakage。✓

---

## New Issues

### N1 [WARNING]: Action trajectory validation 的 internal inconsistency

新增的 action trajectory analysis（Section 4.3 lines 83-87, Appendix §Action Trajectory Analysis Details）与 R² ablation 测量的是不同东西，且结果指向不同维度：

- R² ablation：所有 ablations increase R²（连续 action 维度的 probe 质量改善）
- Trajectory analysis：效应集中在 gripper 维度（shift 0.291 vs <0.034 for continuous dims, Appendix Table）

这意味着：(a) L1 instruction routing 主要因果性地影响离散 gripper 决策，(b) 对连续动作维度的影响极小（<0.034），(c) R² increase from ablation 可能正是因为移除了对连续维度无关的 instruction routing signals。

论文没有讨论这一维度分离。如果 routing 主要影响 gripper 而非连续动作，那 "instruction routing is the primary learned contribution of VLA fine-tuning" 的 scope 需要更精确限定。

### N2 [INFO]: Line 86 的 per-head comparability undermines dominant-head narrative

Section 4.3 line 86: "Per-head effects are comparable; L1 attention collectively influences action generation rather than through a specialized subset."

这句话实际上削弱了整个 Section 4.3 的核心论点：如果 instruction-dominant heads 的 per-head effect 与非 instruction heads comparable，那 "instruction-dominant heads" 作为一个 functionally distinct group 的意义何在？这与前文将 24 dominant heads 作为特殊群体进行分析和讨论的 framing 矛盾。

---

## Updated Assessment

**Score: 5/10 (Borderline)**
**Direction: ↑ (从 4/10 上升)**

### 改善点：
1. "Routing-first" 叙事比 "dual function" 更诚实（R6-C1 改善）
2. Action trajectory validation 增加了因果证据（R6-C4 部分改善）
3. Abstract overclaim qualification 到位（R6-C3 大部分改善）
4. RSA 统计方法修复正确（R6-W1 resolved）
5. 四篇缺失引用全部补齐（R6-I2 resolved）
6. GenAI disclosure、Table 2 caption、Discussion 标题全部修复（R6-W2, I3 resolved）
7. Probe train/test split 明确为 demo-level，解决了 R1-W3 的关切

### 仍存在的主要问题（按严重程度）：
1. **[CRITICAL] 缺 closed-loop behavioral validation**：open-loop trajectory 是进步但不够，CoRL 需要连接到 task success。Limitations 未明确承认。
2. **[WARNING] Ablation 的 internal inconsistency**：R² vs trajectory 维度分离未讨论；per-head comparability undermines dominant-head narrative。
3. **[WARNING] Introduction/Conclusion 仍有 unqualified general claims**（C3 部分未修）。
4. **[WARNING] C1 novelty 仍是 soft weakness**（改善但未完全解决）。
5. **[WARNING] CKA 矛盾仍未在正文充分讨论**。
6. **[WARNING] conclusion.tex 仍未编译**。

### 总体判断：
论文在 Round 1 反馈上做了实质性改进，特别是统计方法（RSA bootstrap）、probe split 透明度、引用覆盖和 overclaim qualification。方向正确。但核心的 CoRL 适配性问题（behavioral validation）和 ablation interpretation 的 internal consistency 仍需解决。如果在 camera-ready 版本中 (a) 加 1-2 句明确承认 behavioral validation 限制，(b) 讨论 gripper vs continuous 维度分离，(c) 将 Introduction findings 限定到 OpenVLA，(d) 编译 conclusion.tex，论文可以达到 borderline accept。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-18T13:39:48.852679+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 读取 issues + 分派 Reviewer', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '将 R1/R2 Round 2 意见交叉转发'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 读取 issues + 分派 Reviewer', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '将 R1/R2 Round 2 意见交叉转发'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-18T13:39:48.903483+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-18T13:40:09.642115+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Step 2 交叉分享 — 请回应 Reviewer 2 的 Round 2 评估\n\nR2 评分从 4/10 上升至 5/10 (Borderline)。以下是 R2 的关键判断，请逐条 [AGREE] 或 [REBUT]。\n\n---\n\n### Issue Verification 差异\n\n**R6-C1 (Ablation)**: R2 将严重程度从 CRITICAL 降为 WARNING。理由：新叙事更准确，trajectory validation 增加了因果证据。但 R2 指出两个新问题：\n1. R² ablation 测连续动作维度（improvement），trajectory analysis 测离散 gripper 维度（divergence）——两个结果讲不同故事，论文未讨论这一维度分离\n2. Line 86 \"Per-head effects are comparable\" 实际上 undermines instruction-dominant heads 作为 functionally distinct group 的叙事\n\n**你上轮保持 CRITICAL**，R2 降为 WARNING。你同意降级还是维持 CRITICAL？\n\n**R6-C3 (Overclaim)**: R2 降为 WARNING。Abstract 改善，但 Introduction lines 16-20 的 \"Three findings emerge\" 仍用一般化语言，Contribution (i) 和 (iii) 仍无 model-specific qualification。你上轮未单独追踪此 issue——你同意 R2 的评估吗？\n\n**R6-C4 (Behavioral validation)**: R2 保持 CRITICAL。理由：\n- Open-loop trajectory ≠ closed-loop task success\n- 72.3% token divergence 不知道是变好还是变差\n- Limitations 未明确承认 behavioral validation 缺失\n- \"early-layer parameters may suffice\" 仍 speculative\n\n你上轮也标 STILL_OPEN 但未明确 severity。你同意保持 CRITICAL 还是降级？\n\n### R2 新发现\n\n**N1 [WARNING]: R² vs trajectory 维度分离**——gripper shift 0.291 vs continuous <0.034。这是否对 \"routing-first\" 解释产生重大影响？\n\n**N2 [INFO]: Per-head comparability undermines dominant-head narrative**——如果所有 heads per-head effect 类似，instruction-dominant heads 的特殊地位何在？\n\n### R2 的 Persistent Issues\n\n**P1**: C1 仍作为 compound contribution (framework + verification) 在 Contribution (i) 中，建议拆开\n**P2**: CKA 矛盾仍未在正文充分讨论（仅 Appendix 指针）\n**P3**: conclusion.tex 仍未编译（你也在 N2 中指出）\n\n### 评分对比\n- 你: 6/10 (↑ from 5)\n- R2: 5/10 (↑ from 4)\n\n请就上述差异点给出 [AGREE] 或 [REBUT]。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Step 2 交叉分享 — 请回应 Reviewer 2 的 Round 2 评估\n\nR2 评分从 4/10 上升至 5/10 (Borderline)。以下是 R2 的关键判断，请逐条 [AGREE] 或 [REBUT]。\n\n---\n\n### Issue Verification 差异\n\n**R6-C1 (Ablation)**: R2 将严重程度从 CRITICAL 降为 WARNING。理由：新叙事更准确，trajectory validation 增加了因果证据。但 R2 指出两个新问题：\n1. R² ablation 测连续动作维度（improvement），trajectory analysis 测离散 gripper 维度（divergence）——两个结果讲不同故事，论文未讨论这一维度分离\n2. Line 86 \"Per-head effects are comparable\" 实际上 undermines instruction-dominant heads 作为 functionally distinct group 的叙事\n\n**你上轮保持 CRITICAL**，R2 降为 WARNING。你同意降级还是维持 CRITICAL？\n\n**R6-C3 (Overclaim)**: R2 降为 WARNING。Abstract 改善，但 Introduction lines 16-20 的 \"Three findings emerge\" 仍用一般化语言，Contribution (i) 和 (iii) 仍无 model-specific qualification。你上轮未单独追踪此 issue——你同意 R2 的评估吗？\n\n**R6-C4 (Behavioral validation)**: R2 保持 CRITICAL。理由：\n- Open-loop trajectory ≠ closed-loop task success\n- 72.3% token divergence 不知道是变好还是变差\n- Limitations 未明确承认 behavioral validation 缺失\n- \"early-layer parameters may suffice\" 仍 speculative\n\n你上轮也标 STILL_OPEN 但未明确 severity。你同意保持 CRITICAL 还是降级？\n\n### R2 新发现\n\n**N1 [WARNING]: R² vs trajectory 维度分离**——gripper shift 0.291 vs continuous <0.034。这是否对 \"routing-first\" 解释产生重大影响？\n\n**N2 [INFO]: Per-head comparability undermines dominant-head narrative**——如果所有 heads per-head effect 类似，instruction-dominant heads 的特殊地位何在？\n\n### R2 的 Persistent Issues\n\n**P1**: C1 仍作为 compound contribution (framework + verification) 在 Contribution (i) 中，建议拆开\n**P2**: CKA 矛盾仍未在正文充分讨论（仅 Appendix 指针）\n**P3**: conclusion.tex 仍未编译（你也在 N2 中指出）\n\n### 评分对比\n- 你: 6/10 (↑ from 5)\n- R2: 5/10 (↑ from 4)\n\n请就上述差异点给出 [AGREE] 或 [REBUT]。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-18T13:40:29.623940+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19981
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-18T13:40:29.774854+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Step 2 交叉分享 — 请回应 Reviewer 1 的 Round 2 评估\n\nR1 评分从 5/10 上升至 6/10 (Marginally above threshold)。以下是 R1 的关键判断，请逐条 [AGREE] 或 [REBUT]。\n\n---\n\n### Issue Verification 差异\n\n**R6-C1 (Ablation)**: R1 保持 STILL_OPEN，指出四点：\n1. 核心矛盾未解决——ALL ablation increase R²，\"routing-first\" 仍是对 \"增幅更小\" 的 post-hoc 解释\n2. Discussion line 12 自相矛盾：\"effect distributes across L1 heads\" 与 \"routing concentration suggests early-layer suffice\" 互相矛盾\n3. N=10 random subsets 未增加\n4. 效应集中在 gripper dimension，claim scope 应缩小\n\n**你降为 WARNING**，R1 保持 CRITICAL 级别。你同意保持还是坚持降级？\n\n**R6-C2 (Probe split)**: R1 标 RESOLVED。Demo-level split 完全消除时间泄漏。残余：linear vs MLP 20× gap 未在正文讨论（R1 降为 INFO）。你未单独追踪此 issue——同意 RESOLVED？\n\n**R6-C4 (Behavioral validation)**: R1 标 STILL_OPEN (partially improved)。关键判断：\n- Open-loop trajectory analysis 不是 behavioral validation\n- \"confirms the causal role\"（Discussion line 12）对 \"causal role\" 定义过宽\n- 建议 Discussion/Limitations 明确承认 behavioral gap\n- 评价比你温和——R1 未明确标 CRITICAL\n\n你保持 CRITICAL。R1 似乎更偏向 WARNING/STILL_OPEN。这一差异是否影响你的评分？\n\n### R1 新发现\n\n**N1 [WARNING]: Discussion 自相矛盾**\nDiscussion line 12: \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation.\"\n- 前半句：效应均匀分布（不集中在 instruction-dominant heads）\n- 后半句：仍推论 routing concentration 的特殊意义\n\n这与你的 N2（per-head comparability undermines dominant-head narrative）是同一个问题的不同表述。你同意这是 WARNING 级别？\n\n**N2 [INFO]: conclusion.tex 仍未编译**——你在 P3 中也指出。\n\n**N3 [INFO]: conclusion.tex 中 claims 未更新**——因未编译暂不影响。\n\n### R1 的残余小问题\n\n- Linear vs MLP 20× gap 未在正文讨论（降为 INFO）\n- N=10 tasks 的 bootstrap 功效有限（固有限制，非方法论错误）\n\n### 评分对比\n- R1: 6/10 (↑ from 5)\n- 你: 5/10 (↑ from 4)\n\nR1 认为方法论修复（probe split + RSA bootstrap）\"显著提升了统计推断可信度\"，使论文从 \"marginally below\" 升至 \"marginally above\"。你是否同意这一判断？如果不同意，什么是你维持 5/10 的决定性因素？\n\n请就上述差异点给出 [AGREE] 或 [REBUT]。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Step 2 交叉分享 — 请回应 Reviewer 1 的 Round 2 评估\n\nR1 评分从 5/10 上升至 6/10 (Marginally above threshold)。以下是 R1 的关键判断，请逐条 [AGREE] 或 [REBUT]。\n\n---\n\n### Issue Verification 差异\n\n**R6-C1 (Ablation)**: R1 保持 STILL_OPEN，指出四点：\n1. 核心矛盾未解决——ALL ablation increase R²，\"routing-first\" 仍是对 \"增幅更小\" 的 post-hoc 解释\n2. Discussion line 12 自相矛盾：\"effect distributes across L1 heads\" 与 \"routing concentration suggests early-layer suffice\" 互相矛盾\n3. N=10 random subsets 未增加\n4. 效应集中在 gripper dimension，claim scope 应缩小\n\n**你降为 WARNING**，R1 保持 CRITICAL 级别。你同意保持还是坚持降级？\n\n**R6-C2 (Probe split)**: R1 标 RESOLVED。Demo-level split 完全消除时间泄漏。残余：linear vs MLP 20× gap 未在正文讨论（R1 降为 INFO）。你未单独追踪此 issue——同意 RESOLVED？\n\n**R6-C4 (Behavioral validation)**: R1 标 STILL_OPEN (partially improved)。关键判断：\n- Open-loop trajectory analysis 不是 behavioral validation\n- \"confirms the causal role\"（Discussion line 12）对 \"causal role\" 定义过宽\n- 建议 Discussion/Limitations 明确承认 behavioral gap\n- 评价比你温和——R1 未明确标 CRITICAL\n\n你保持 CRITICAL。R1 似乎更偏向 WARNING/STILL_OPEN。这一差异是否影响你的评分？\n\n### R1 新发现\n\n**N1 [WARNING]: Discussion 自相矛盾**\nDiscussion line 12: \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation.\"\n- 前半句：效应均匀分布（不集中在 instruction-dominant heads）\n- 后半句：仍推论 routing concentration 的特殊意义\n\n这与你的 N2（per-head comparability undermines dominant-head narrative）是同一个问题的不同表述。你同意这是 WARNING 级别？\n\n**N2 [INFO]: conclusion.tex 仍未编译**——你在 P3 中也指出。\n\n**N3 [INFO]: conclusion.tex 中 claims 未更新**——因未编译暂不影响。\n\n### R1 的残余小问题\n\n- Linear vs MLP 20× gap 未在正文讨论（降为 INFO）\n- N=10 tasks 的 bootstrap 功效有限（固有限制，非方法论错误）\n\n### 评分对比\n- R1: 6/10 (↑ from 5)\n- 你: 5/10 (↑ from 4)\n\nR1 认为方法论修复（probe split + RSA bootstrap）\"显著提升了统计推断可信度\"，使论文从 \"marginally below\" 升至 \"marginally above\"。你是否同意这一判断？如果不同意，什么是你维持 5/10 的决定性因素？\n\n请就上述差异点给出 [AGREE] 或 [REBUT]。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-18T13:40:31.234003+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 504 · 2026-05-18T13:40:34.386351+00:00_

交叉分享已分派。等待两位 Reviewer 的回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 505 · 2026-05-18T13:40:36.993805+00:00_

[Reviewer 2 审稿结果]:
Round 2 审稿意见已提交。评分从 4/10 上调至 5/10 (Borderline)，方向 ↑。

主要改善：RSA 统计修复、probe split 透明化、overclaim qualification、四篇引用补齐、GenAI disclosure。仍存在的核心问题：缺 closed-loop behavioral validation（对 CoRL 仍是 CRITICAL）、ablation 的 R² vs trajectory 维度不一致未讨论、conclusion.tex 仍未编译。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 506 · 2026-05-18T13:40:42.056364+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 55

## Round 55

14 recorded events


### User

_source line 507 · 2026-05-18T13:41:28.959024+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 评估

---

## Issue Verification 差异

### R6-C1 (Ablation): R2 降为 WARNING vs 我保持 CRITICAL — [PARTIAL AGREE, 降为 WARNING]

经过 R2 的分析，我同意将 severity 从 CRITICAL 降为 WARNING，理由如下：

(a) **新增 trajectory analysis 确实增加了因果证据层**。虽然不完美，但 output-level 证据（d=0.65, 72.3% token divergence, KL=5.08 vs 1.69）补充了纯 representation-level 分析，使因果推断从"仅有相关性"升级为"相关性 + output-level 影响"。这足以将 severity 从 CRITICAL（阻碍接收）降至 WARNING（影响评分但不一票否决）。

(b) 但我**完全同意 R2 新发现的两个问题**：

- **R2-N1（维度分离）**: R² ablation 的 improvement 主要反映连续动作维度（因为 R² 是 7-D 均值），而 trajectory 的 divergence 主要来自 gripper（shift 0.291 vs <0.034）。两个结果确实在讲不同维度的故事，但论文将它们并列呈现仿佛互相支撑。这个 gap 需要正文讨论。

- **R2-N2（Per-head comparability）**: Section 4.3 line 86 "Per-head effects are comparable" 是修改中引入的新问题。如果每个 head 的 per-head ablation 效应类似（无论是否 instruction-dominant），那么 instruction-dominant heads 作为 functionally distinct group 的叙事就失去了基础。"Routing-first specialization" 隐含 "这些 heads 在功能上与其他 heads 不同"，但 per-head comparability 正好说明它们在 ablation 效应上并不特殊。我在 Round 2 报告的 N1（Discussion 自相矛盾）本质上指出了同一问题。

**结论**: 降为 WARNING。Ablation 的核心逻辑仍有问题（all increase R²、per-head comparability、维度分离），但 trajectory analysis 提供了有意义的补充证据，使这不再是 reject-level 的致命缺陷，而是需要在 claim scope 上做限定的问题。

---

### R6-C3 (Overclaim): — [AGREE]

同意 R2 的评估。我在 Round 1 将 overclaim 分散在多个 weakness 中讨论（W1 的 C1 novelty、W5 的 C3 metric-dependency、W6 的 generalization），未单独追踪。R2 的系统性检查更好：

- Abstract line 7 已改善（"in the model studied"）— 正面确认
- Introduction lines 16-20 "Three findings emerge" 仍用一般化语言，无 model-specific 限定 — 问题存在
- Contribution (i) "verifying architecture-expected specialization between image and readout tokens" 未限定模型 — 虽然此条本身是架构通用的（causal mask 对所有 decoder-only VLA 成立），但措辞暗示这是 empirical 验证而非逻辑推导
- Contribution (iii) "vision encoder representations are non-monotonically transformed by the LLM" 也未加 model-specific 限定

WARNING 级别合理。修复成本低（加几个 "in OpenVLA-7B" / "on LIBERO"），但当前状态下确实影响审稿人对 claim 诚实度的判断。

---

### R6-C4 (Behavioral validation): — [AGREE, 保持 CRITICAL]

同意 R2 保持 CRITICAL。我的 Round 2 标注为 "STILL_OPEN (partially improved)" 但未明确 severity。现在明确：

(a) **对 CoRL 来说 behavioral validation 是 critical bar**。CoRL 审稿维度明确包含 "relevance to robot learning"，纯 representational findings 无 behavioral 连接对 robotics venue 是显著缺陷。

(b) R2 的论证精确：72.3% token divergence 不知道是变好还是变差。如果 ablation 后的 action sequence 实际上更好（R² 增加暗示如此），那意味着 instruction routing 对 action quality 是有害的——这会颠覆论文的核心叙事。如果更差，那需要 rollout 证明。两种可能性都对论文的 story 不利，而作者没有数据来区分。

(c) Discussion line 12 "Action trajectory analysis confirms the causal role" 中 "causal role" 的措辞过强。Trajectory analysis 确认了 L1 ablation 影响了 output，但未确认影响的方向（正面还是负面）。"Causal influence" 比 "causal role" 更准确。

(d) Limitations（Discussion line 14-15）仍未明确承认 behavioral validation 缺失。只说 "C2 may differ across backbone scales and decoder paradigms"，这是 generalization 的 limitation，不是 behavioral gap 的 limitation。

**结论**: 保持 CRITICAL。MuJoCo 版本限制是可理解的技术障碍，但论文需要至少在 Limitations 中明确承认 "our analyses are representational; connecting these findings to task success requires closed-loop evaluation, which we leave to future work"。当前的 Limitations 段落回避了这个问题。

---

## R2 Persistent Issues

### P1 (C1 作为 compound contribution) — [AGREE]

将 "framework" 和 "architecture verification" 拆分为独立贡献是合理建议。当前 Contribution (i) 同时 claim "systematic experimental framework" 和 "verifying architecture-expected specialization"。前者是方法论贡献（framework 可用于其他 VLA），后者是 empirical sanity check。合并后读起来像是一个 contribution，但实质是两个不同性质的 claim——一个有持久价值，一个是 trivial verification。拆分后更诚实。

### P2 (CKA 矛盾仅在 Appendix 讨论) — [AGREE with nuance]

主要同意。正文 Section 3.6 line 64-66 现在扩展了 RSA over CKA 的 justification（"it captures the relative distance structure among representations, which directly governs action prediction quality"），这是一个改进。但 "directly governs action prediction quality" 是一个需要 empirical 支撑的 claim，而非不证自明的事实——CKA 拥护者可以同样论证 global subspace overlap 与 downstream performance 更相关。

正文中应至少用一句话承认 CKA 给出不同 story（目前完全依赖 Appendix 指针），让读者不读 Appendix 也能知道 Finding 3 的 metric-dependency。

### P3 (conclusion.tex 未编译) — [AGREE]

我在 Round 2 N2 中也指出了这个问题。main.tex 仍无 `\input{conclusion}`。Discussion 末段有总结功能但缺少独立 Conclusion section。修复成本极低。

---

## 评分差异讨论

R2: 5/10, 我: 6/10。差距为 1 分。

**差异来源**: 我给 6 的主要理由是 R6-C2（probe split）和 R6-W1（RSA bootstrap）的完全解决显著提升了 Finding 2 和 Finding 3 定量结论的可信度。R2 可能更看重 behavioral validation gap（保持 CRITICAL）和 overclaim（systematic tracking），这些问题确实未改善。

**经过交叉讨论后的调整**: 我同意将 R6-C4 维持 CRITICAL 和 R6-C1 降为 WARNING。综合来看：
- 1 个 CRITICAL 仍 open (behavioral validation)
- 2 个 WARNING 仍 open (ablation logic + overclaim)
- 2 个 RESOLVED (probe split + RSA bootstrap)
- 多个 INFO 级别 issues

这个 profile 对应 borderline 到 marginally above。我维持 6/10 但承认 5/10 也有合理依据——取决于审稿人对 "CoRL 是否接受无 behavioral validation 的纯分析论文" 这个 meta-question 的判断。如果 CoRL AC 认为 behavioral evidence 是 hard requirement，论文在 5 以下；如果分析框架本身有价值且修复路径清晰，6 合理。

**最终评分**: 6/10 (Marginally above acceptance threshold)
**Confidence**: 4/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-18T13:41:45.929743+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-2: 初始化 + 审稿 + 交叉分享', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': 'Round 2 已收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '撰写报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-2: 初始化 + 审稿 + 交叉分享', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': 'Round 2 已收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '撰写报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-18T13:41:45.982960+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-18T13:43:38.194327+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-5 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-5 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"C1 重新定位为 framework + verification。Abstract 用 'validate'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍列为 contribution (i)，novelty bar 不够\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"改善但仍是 soft weakness。建议拆分 contribution (i) 为 framework + verification。\"\n    action_items: []\n\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"C3 降为 qualified observation，全文加 metric-dependent qualifier。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Qualifier 到位但 metric selection 可能 results-driven。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Method §3.6 justification 更强，但 CKA 矛盾仍主要在 Appendix。\"\n    action_items: []\n\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Overparameterized + early stopping + linear probe 复现。Round 7: demo-level split (0-39/40-49) 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Train/test split 未说明 + 自相关\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"RESOLVED: demo-level split 完全消除时间泄漏。Linear vs MLP 20× gap 降为 INFO。\"\n    action_items: []\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W5\n    summary: \"单模型 + 单 benchmark 泛化性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Limitations 列举架构变量。Round 7: Abstract 加 'in the model studied'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"升级至 CRITICAL: Abstract overclaim\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Abstract 改善。Introduction findings 段落仍有 unqualified claims。降为 WARNING。\"\n    action_items: []\n\n  - id: R4-W6\n    summary: \"缺 Llama-2 + OXE 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已加入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"客观描述。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未编译\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion Outlook 段落正面收尾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍未编译。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"仍未编译。conclusion.tex 含 code release 声明被浪费。修复成本极低。\"\n    action_items:\n      - round: 7\n        action: \"main.tex 添加 \\\\input{conclusion}\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R4-I2\n    summary: \"引用格式：alain2017 + nostalgebraist2020\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"统一为 24/32。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 5 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' → random-subset control 推翻\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: \"Dual function 叙事已替换。Round 7: 改为 routing-first specialization。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Dual function 仍是 post-hoc。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Routing-first 更准确但仍有 internal inconsistency（维度分离 + per-head comparability）。降为 WARNING。\"\n    action_items: []\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 措辞\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N3\n    summary: \"单模型 Limitations 不够具体\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Limitations 列举架构变量。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N4\n    summary: \"Architectural implications speculative + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: \"Implications weakened。Round 7: trajectory analysis 提供 output-level 证据，但非 closed-loop。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"升级至 CRITICAL: 对 CoRL 结构性缺口。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"STILL CRITICAL: open-loop ≠ behavioral。Limitations 未承认 gap。\"\n    action_items: []\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 OOD confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"OOD diagnostics + Appendix。Round 6: non-degenerate ≠ meaningful。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Random noise token control 建议。\"\n    action_items: []\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 数值\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已插入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W3\n    summary: \"C3 Abstract 权重过高\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"压缩至单句。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W4\n    summary: \"缺 causal tracing/tuned lens 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已添加。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-I1\n    summary: \"Appendix single-seed three-condition\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"3 seeds 完成。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n  - id: R6-C1\n    summary: \"Ablation 因果推断方向问题：所有 ablation increase R²\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: dual function 是 post-hoc。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"降为 WARNING。routing-first 更准确 + trajectory analysis 增加因果证据。但存在 internal inconsistency: (a) R² 测连续维度 vs trajectory 测 gripper 维度（未讨论）; (b) per-head effects comparable 削弱 dominant-head 叙事; (c) Discussion 自相矛盾（effect distributes 但仍推论 routing concentration）; (d) N=10 random subsets 未增加。\"\n    action_items:\n      - round: 6\n        action: \"routing-first 叙事重写\"\n        assigned_to: paper_agent\n        status: done\n      - round: 7\n        action: \"方案A: 正文讨论 gripper vs continuous 维度分离对 claim scope 的影响; 方案B: 修复 Discussion 自相矛盾; 方案C: 限定 routing function claim 至 discrete/gripper 控制\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C2\n    summary: \"Probe train/test split + 时间自相关\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Demo-level sequential split (0-39/40-49) 完全消除时间泄漏。R² 为 held-out 数据。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"RESOLVED。Residual: linear vs MLP 20× gap 未在正文讨论（INFO 级别）。\"\n    action_items: []\n\n  - id: R6-C3\n    summary: \"单模型 Abstract overclaim\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: Abstract 一般化措辞。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"降为 WARNING。Abstract line 7 'in the model studied' ✓。但 Introduction lines 16-20 'Three findings emerge' 仍无 model-specific 限定。Contribution (i) 和 (iii) 未限定模型。Discussion 'early-layer parameters may suffice' 仍 unqualified。\"\n    action_items:\n      - round: 6\n        action: \"Abstract/Intro/Discussion 三重 qualify\"\n        assigned_to: paper_agent\n        status: done\n      - round: 7\n        action: \"Introduction findings 段落 + Contribution (i)(iii) 加 model-specific 限定\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C4\n    summary: \"缺 behavioral validation，对 CoRL 结构性缺口\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: 无 task success rate。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"STILL CRITICAL: Open-loop trajectory analysis (d=0.65) 是进步但非 behavioral validation。72.3% token divergence 不知变好变差。Discussion 'confirms the causal role' 措辞过强。Limitations 未承认 behavioral gap。MuJoCo 版本限制是可理解的技术障碍。\"\n    action_items:\n      - round: 6\n        action: \"Behavioral rollout pilot\"\n        assigned_to: research\n        status: failed\n      - round: 6\n        action: \"Open-loop trajectory analysis\"\n        assigned_to: research\n        status: done\n      - round: 7\n        action: \"方案A: Discussion 'confirms the causal role' → 'demonstrates causal influence on action output'; 方案B: Limitations 明确承认 'our analyses are representational/open-loop; connecting findings to task success requires closed-loop evaluation'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W1\n    summary: \"RSA pairwise dependency 未处理\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Task-level block resampling + Nili 2014 引用。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"RESOLVED。N=10 tasks 功效有限但是固有限制。\"\n    action_items: []\n\n  - id: R6-W2\n    summary: \"缺 Generative AI 使用声明\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Discussion 末尾添加。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-W3\n    summary: \"Abstract 数据密度过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"去掉 z-score 等细节。Round 7: 仍有 ~12 个数值，但对 technical analysis 论文 acceptable。\"\n    resolution_round: 6\n    mentions:\n      - round: 7\n        reviewers: [2]\n        note: \"轻微改善，acceptable 范围内。\"\n    action_items: []\n\n  - id: R6-I1\n    summary: \"-ing 分词短语 AI 标志\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Appendix 改写。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I2\n    summary: \"缺引用 Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"四篇全部添加且正文引用。\"\n    resolution_round: 6\n    mentions:\n      - round: 7\n        reviewers: [2]\n        note: \"CONFIRMED: 全部到位。\"\n    action_items: []\n\n  - id: R6-I3\n    summary: \"Table 2 caption + Discussion 'Speculative' 标题\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Caption 自包含化 + 改为 'Mechanistic hypothesis'。\"\n    resolution_round: 6\n    mentions:\n      - round: 7\n        reviewers: [2]\n        note: \"CONFIRMED。\"\n    action_items: []\n\n  # ============================================================\n  # Round 7 新发现\n  # ============================================================\n  - id: R7-W1\n    summary: \"Ablation R² vs trajectory 测量的维度分离未讨论：R² 测连续动作维度（改善），trajectory 效应集中在 gripper 离散维度（shift 0.291 vs <0.034）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"全票共识。两个结果在讲不同维度的故事。如果 routing 主要影响 gripper，claim scope 应更精确限定。论文将两者并列呈现仿佛互相支撑。\"\n    action_items:\n      - round: 7\n        action: \"正文讨论 gripper vs continuous 维度分离 + 限定 claim scope\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-W2\n    summary: \"Per-head comparability + Discussion 自相矛盾：'effect distributes across L1 heads' vs 'routing concentration suggests early-layer suffice'\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"全票共识。Line 86 'Per-head effects are comparable' undermines instruction-dominant heads 作为 functionally distinct group 的叙事。Discussion line 12 前后半句互相矛盾。\"\n    action_items:\n      - round: 7\n        action: \"修复 Discussion 逻辑：如果效应均匀分布，则不能同时推论 routing concentration 的特殊意义\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-W3\n    summary: \"CKA 矛盾仍主要在 Appendix：正文仅一句括号提及，读者不翻 Appendix 不知 CKA 完全反转 inverted-U\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Method §3.6 justification 更强，但正文未讨论 CKA 具体矛盾结果。建议 Section 4.4 加 1-2 句。\"\n    action_items:\n      - round: 7\n        action: \"Section 4.4 加正文讨论 CKA 矛盾\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-5 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-5 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"C1 重新定位为 framework + verification。Abstract 用 'validate'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍列为 contribution (i)，novelty bar 不够\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"改善但仍是 soft weakness。建议拆分 contribution (i) 为 framework + verification。\"\n    action_items: []\n\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"C3 降为 qualified observation，全文加 metric-dependent qualifier。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Qualifier 到位但 metric selection 可能 results-driven。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Method §3.6 justification 更强，但 CKA 矛盾仍主要在 Appendix。\"\n    action_items: []\n\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Overparameterized + early stopping + linear probe 复现。Round 7: demo-level split (0-39/40-49) 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Train/test split 未说明 + 自相关\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"RESOLVED: demo-level split 完全消除时间泄漏。Linear vs MLP 20× gap 降为 INFO。\"\n    action_items: []\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W5\n    summary: \"单模型 + 单 benchmark 泛化性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Limitations 列举架构变量。Round 7: Abstract 加 'in the model studied'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"升级至 CRITICAL: Abstract overclaim\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Abstract 改善。Introduction findings 段落仍有 unqualified claims。降为 WARNING。\"\n    action_items: []\n\n  - id: R4-W6\n    summary: \"缺 Llama-2 + OXE 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已加入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"客观描述。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未编译\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion Outlook 段落正面收尾。\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍未编译。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"仍未编译。conclusion.tex 含 code release 声明被浪费。修复成本极低。\"\n    action_items:\n      - round: 7\n        action: \"main.tex 添加 \\\\input{conclusion}\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R4-I2\n    summary: \"引用格式：alain2017 + nostalgebraist2020\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"统一为 24/32。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 5 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' → random-subset control 推翻\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: \"Dual function 叙事已替换。Round 7: 改为 routing-first specialization。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Dual function 仍是 post-hoc。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Routing-first 更准确但仍有 internal inconsistency（维度分离 + per-head comparability）。降为 WARNING。\"\n    action_items: []\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 措辞\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N3\n    summary: \"单模型 Limitations 不够具体\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Limitations 列举架构变量。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N4\n    summary: \"Architectural implications speculative + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 7\n    resolution: \"Implications weakened。Round 7: trajectory analysis 提供 output-level 证据，但非 closed-loop。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"升级至 CRITICAL: 对 CoRL 结构性缺口。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"STILL CRITICAL: open-loop ≠ behavioral。Limitations 未承认 gap。\"\n    action_items: []\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 OOD confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"OOD diagnostics + Appendix。Round 6: non-degenerate ≠ meaningful。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Random noise token control 建议。\"\n    action_items: []\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 数值\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已插入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W3\n    summary: \"C3 Abstract 权重过高\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"压缩至单句。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W4\n    summary: \"缺 causal tracing/tuned lens 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已添加。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-I1\n    summary: \"Appendix single-seed three-condition\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"3 seeds 完成。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n  - id: R6-C1\n    summary: \"Ablation 因果推断方向问题：所有 ablation increase R²\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: dual function 是 post-hoc。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"降为 WARNING。routing-first 更准确 + trajectory analysis 增加因果证据。但存在 internal inconsistency: (a) R² 测连续维度 vs trajectory 测 gripper 维度（未讨论）; (b) per-head effects comparable 削弱 dominant-head 叙事; (c) Discussion 自相矛盾（effect distributes 但仍推论 routing concentration）; (d) N=10 random subsets 未增加。\"\n    action_items:\n      - round: 6\n        action: \"routing-first 叙事重写\"\n        assigned_to: paper_agent\n        status: done\n      - round: 7\n        action: \"方案A: 正文讨论 gripper vs continuous 维度分离对 claim scope 的影响; 方案B: 修复 Discussion 自相矛盾; 方案C: 限定 routing function claim 至 discrete/gripper 控制\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C2\n    summary: \"Probe train/test split + 时间自相关\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Demo-level sequential split (0-39/40-49) 完全消除时间泄漏。R² 为 held-out 数据。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"RESOLVED。Residual: linear vs MLP 20× gap 未在正文讨论（INFO 级别）。\"\n    action_items: []\n\n  - id: R6-C3\n    summary: \"单模型 Abstract overclaim\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: Abstract 一般化措辞。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"降为 WARNING。Abstract line 7 'in the model studied' ✓。但 Introduction lines 16-20 'Three findings emerge' 仍无 model-specific 限定。Contribution (i) 和 (iii) 未限定模型。Discussion 'early-layer parameters may suffice' 仍 unqualified。\"\n    action_items:\n      - round: 6\n        action: \"Abstract/Intro/Discussion 三重 qualify\"\n        assigned_to: paper_agent\n        status: done\n      - round: 7\n        action: \"Introduction findings 段落 + Contribution (i)(iii) 加 model-specific 限定\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-C4\n    summary: \"缺 behavioral validation，对 CoRL 结构性缺口\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: 无 task success rate。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"STILL CRITICAL: Open-loop trajectory analysis (d=0.65) 是进步但非 behavioral validation。72.3% token divergence 不知变好变差。Discussion 'confirms the causal role' 措辞过强。Limitations 未承认 behavioral gap。MuJoCo 版本限制是可理解的技术障碍。\"\n    action_items:\n      - round: 6\n        action: \"Behavioral rollout pilot\"\n        assigned_to: research\n        status: failed\n      - round: 6\n        action: \"Open-loop trajectory analysis\"\n        assigned_to: research\n        status: done\n      - round: 7\n        action: \"方案A: Discussion 'confirms the causal role' → 'demonstrates causal influence on action output'; 方案B: Limitations 明确承认 'our analyses are representational/open-loop; connecting findings to task success requires closed-loop evaluation'\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W1\n    summary: \"RSA pairwise dependency 未处理\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Task-level block resampling + Nili 2014 引用。\"\n    resolution_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"RESOLVED。N=10 tasks 功效有限但是固有限制。\"\n    action_items: []\n\n  - id: R6-W2\n    summary: \"缺 Generative AI 使用声明\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Discussion 末尾添加。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-W3\n    summary: \"Abstract 数据密度过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"去掉 z-score 等细节。Round 7: 仍有 ~12 个数值，但对 technical analysis 论文 acceptable。\"\n    resolution_round: 6\n    mentions:\n      - round: 7\n        reviewers: [2]\n        note: \"轻微改善，acceptable 范围内。\"\n    action_items: []\n\n  - id: R6-I1\n    summary: \"-ing 分词短语 AI 标志\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Appendix 改写。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I2\n    summary: \"缺引用 Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"四篇全部添加且正文引用。\"\n    resolution_round: 6\n    mentions:\n      - round: 7\n        reviewers: [2]\n        note: \"CONFIRMED: 全部到位。\"\n    action_items: []\n\n  - id: R6-I3\n    summary: \"Table 2 caption + Discussion 'Speculative' 标题\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Caption 自包含化 + 改为 'Mechanistic hypothesis'。\"\n    resolution_round: 6\n    mentions:\n      - round: 7\n        reviewers: [2]\n        note: \"CONFIRMED。\"\n    action_items: []\n\n  # ============================================================\n  # Round 7 新发现\n  # ============================================================\n  - id: R7-W1\n    summary: \"Ablation R² vs trajectory 测量的维度分离未讨论：R² 测连续动作维度（改善），trajectory 效应集中在 gripper 离散维度（shift 0.291 vs <0.034）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"全票共识。两个结果在讲不同维度的故事。如果 routing 主要影响 gripper，claim scope 应更精确限定。论文将两者并列呈现仿佛互相支撑。\"\n    action_items:\n      - round: 7\n        action: \"正文讨论 gripper vs continuous 维度分离 + 限定 claim scope\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-W2\n    summary: \"Per-head comparability + Discussion 自相矛盾：'effect distributes across L1 heads' vs 'routing concentration suggests early-layer suffice'\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"全票共识。Line 86 'Per-head effects are comparable' undermines instruction-dominant heads 作为 functionally distinct group 的叙事。Discussion line 12 前后半句互相矛盾。\"\n    action_items:\n      - round: 7\n        action: \"修复 Discussion 逻辑：如果效应均匀分布，则不能同时推论 routing concentration 的特殊意义\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-W3\n    summary: \"CKA 矛盾仍主要在 Appendix：正文仅一句括号提及，读者不翻 Appendix 不知 CKA 完全反转 inverted-U\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Method §3.6 justification 更强，但正文未讨论 CKA 具体矛盾结果。建议 Section 4.4 加 1-2 句。\"\n    action_items:\n      - round: 7\n        action: \"Section 4.4 加正文讨论 CKA 矛盾\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-18T13:43:38.348402+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 19212}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-18T13:45:45.185329+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-18T13:45:45.185823+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-18T13:45:49.252467+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-18T13:45:49.303160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-18T13:45:53.520057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-18T13:45:53.520749+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-5 历史 issues（全部 resolved，压缩保留）
4	  # ============================================================
5	  - id: R1-N1-old
6	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 2
12	    resolution: "三条件数据完整整合。"
13	    resolution_round: 3
14	    mentions: []
15	    action_items: []
16	
17	  - id: R1-N2-old
18	    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
19	    category: framing
20	    severity: critical
21	    status: resolved
22	    first_raised_round: 1
23	    last_seen_round: 2
24	    resolution: "Title 改为单数。"
25	    resolution_round: 3
26	    mentions: []
27	    action_items: []
28	
29	  - id: R1-N4-old
30	    summary: "Design implications 完全基于 correlational evidence"
31	    category: framing
32	    severity: critical
33	    status: resolved
34	    first_raised_round: 1
35	    last_seen_round: 2
36	    resolution: "Abstract 使用 hedge 语气。"
37	    resolution_round: 3
38	    mentions: []
39	    action_items: []
40	
41	  - id: R1-N3-old
42	    summary: "RSA best-vs-best selection bias"
43	    category: experiment
44	    severity: warning
45	    status: resolved
46	    first_raised_round: 1
47	    last_seen_round: 2
48	    resolution: "Same-layer comparison 为 primary evidence。"
49	    resolution_round: 3
50	    mentions: []
51	    action_items: []
52	
53	  - id: R2-N1-old
54	    summary: "Neo et al. (ICLR 2025) 未引用"
55	    category: framing
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 2
60	    resolution: "已引用。"
61	    resolution_round: 3
62	    mentions: []
63	    action_items: []
64	
65	  - id: R2-W1-old
66	    summary: "Related Work 引用覆盖度不足"
67	    category: writing
68	    severity: warning
69	    status: resolved
70	    first_raised_round: 1
71	    last_seen_roun
…[truncated 19908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-18T13:47:19.325118+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# Round 7 审稿汇总报告\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026 (deadline 2026-05-29)\n**审稿模式**: 继续审稿（基于 Round 6 修改稿）\n**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)\n**本轮评分**: R1 = 6/10, R2 = 5/10 → 共识 5.5/10 Borderline\n\n---\n\n## Summary\n\n本轮审查基于 Round 6 报告提出的 2 个 CRITICAL + 4 个 WARNING + 若干 INFO 级 issue，评估修改稿的回应充分性。论文在方法论严谨性上有实质进步（demo-level split 消除时间泄漏、task-level RSA bootstrap、routing-first 叙事重写、trajectory analysis 新增），但核心结构性问题（无 behavioral validation）仍未解决，且修改引入了新的 internal inconsistency。\n\n---\n\n## Resolved Issues（本轮确认解决）\n\n### R6-C2 [RESOLVED] Probe train/test split + 时间自相关\nMethod §3.5 明确 demo-level sequential split (demos 0-39 train / 40-49 test)，完全消除时间泄漏风险。这是本轮最重要的方法论改进。\n\n### R6-W1 [RESOLVED] RSA pairwise dependency 未处理\nMethod §3.4 新增 task-level block resampling 说明 + Nili 2014 引用。N=10 tasks 的统计功效有限但属固有限制。\n\n---\n\n## Open Issues\n\n### 🔴 CRITICAL\n\n#### R6-C4 [STILL OPEN] 缺 behavioral validation，对 CoRL 结构性缺口\n**状态**: 新增 open-loop action trajectory analysis (Cohen's d=0.65, 72.3% token divergence)，但这不是 behavioral validation。72.3% 的 action token 改变不告诉读者 task success 变好还是变差。对 CoRL（机器人学习会议）而言，\"representational analysis without any task success metric\" 是结构性缺口。\n\n**具体问题**:\n- Discussion line 11 \"confirms the causal role\" 措辞过强——trajectory divergence 只证明 causal influence on output，不证明 functional role\n- Limitations 段落（Discussion lines 14-15）未承认 behavioral gap，仅讨论 single-model generalization\n- MuJoCo 版本不兼容是可理解的技术障碍，但论文应明确承认此限制\n\n**建议修复**:\n- Discussion: \"confirms the causal role\" → \"demonstrates causal influence on action output\"\n- Limitations 新增: \"Our analyses are representational and open-loop; connecting these findings to task success requires closed-loop behavioral evaluation, which we leave to future work.\"\n- 如能在 deadline 前解决 MuJoCo 兼容问题并提供哪怕 1-2 个 task 的 success rate，将大幅增强论文说服力\n\n---\n\n### 🟡 WARNING\n\n#### R6-C1 [DOWNGRADED → WARNING] Ablation 因果推断方向\n**状态**: 从 CRITICAL 降级。\"routing-first specialization\" 叙事比 \"dual function\" 更准确，trajectory analysis 提供了 output-level 因果证据。但存在 internal inconsistency:\n- R² 衡量连续动作维度的改善，trajectory 效应集中在 gripper 离散维度（shift 0.291 vs <0.034）——两个 metric 在讲不同维度的故事（→ R7-W1）\n- \"Per-head effects are comparable\" 削弱 instruction-dominant heads 作为 functionally distinct group 的叙事（→ R7-W2）\n- N=10 random subsets 偏少（z=-2.73 基于 10 个样本的正态假设）\n\n#### R6-C3 [DOWNGRADED → WARNING] 单模型 overclaim 残余\n**状态**: 从 CRITICAL 降级。Abstract line 7 \"in the model studied\" ✓。但 Introduction lines 16-20 \"Three findings emerge\" 仍用一般化措辞，Contribution (i) 和 (iii) 未限定模型，Discussion \"early-layer parameters may suffice\" 仍 unqualified。\n\n**建议修复**: Introduction findings 段落加 \"In OpenVLA-7B on LIBERO\" 前缀；Contribution (i)(iii) 各加 model-specific 限定。\n\n#### R7-W1 [NEW] 维度分离未讨论\nAblation R² 改善测的是连续维度，trajectory divergence 集中在 gripper（shift 0.291 vs continuous <0.034）。论文将两者并列呈现仿佛互相支撑，但实际测量的是不同 action space 维度。如果 routing 主要影响 gripper control，claim scope 应更精确限定。\n\n#### R7-W2 [NEW] Per-head comparability + Discussion 自相矛盾\nExperiments line 86 \"Per-head effects are comparable\" 意味着 instruction-dominant heads 的 per-head 影响力与非 instruction-dominant heads 相当，削弱了将这 24 个 heads 作为 functionally distinct group 的叙事。Discussion line 12 前半句 \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones\" 与后半句 \"yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation\" 逻辑矛盾：如果效应均匀分布，不能同时推论 routing concentration 的特殊意义。\n\n#### R7-W3 [NEW] CKA 矛盾正文讨论不足\nMethod §3.6 \"Why RSA over CKA\" justification 已加强，但 CKA 完全反转 inverted-U（monotonically increasing）这一重要矛盾结果仅在 Introduction line 20 一句括号中提及。读者不翻 Appendix 不知道 C3 的 metric-dependency 有多严重。建议 Section 4.4 加 1-2 句正文讨论。\n\n---\n\n### ℹ️ INFO (升级建议)\n\n#### R4-I1 [PERSISTENT] conclusion.tex 未编译\nRound 4 发现至今未修复。main.tex 无 `\\input{conclusion}`。conclusion.tex 含 code release 声明被浪费。修复成本极低（一行代码）。建议升级至 WARNING：CoRL 要求完整论文结构，缺 Conclusion 可能被审稿人视为不完整。\n\n---\n\n## Strengths（修改后新增/增强）\n\n**S1. 方法论严谨性显著提升**: Demo-level split 彻底解决时间泄漏（Round 6 最严重的方法论问题），task-level block resampling 正确处理 RSA pairwise dependency。这两项修改使统计推断的可信度大幅提高。\n\n**S2. Routing-first 叙事更准确**: 从 \"dual function\" 改为 \"routing-first specialization\" 是正确方向——承认 R² increase 而非 post-hoc 强行解释。\n\n**S3. Trajectory analysis 增加因果证据**: Open-loop action trajectory comparison (d=0.65, 72.3% divergence) 虽非 behavioral validation，但比纯 representational analysis 更接近 output-level 证据。Gripper 维度的 selective effect (0.291 vs <0.034) 是有趣发现。\n\n**S4. 三条件 factorial 设计**: Trained/Pretrained/Untrained 三条件交叉 instruction presence 的设计仍是本文最大方法论贡献，在 VLA 分析文献中具有参考价值。\n\n**S5. RSA justification 加强**: Method 新增 RSA 功能性论证（\"captures relative distance structure directly governing action prediction quality\"），说服力提升。\n\n---\n\n## Weaknesses（当前版本）\n\n**W1 [CRITICAL]. 缺 behavioral validation**: 对 CoRL 是结构性缺口。Open-loop trajectory divergence ≠ task success。论文未在 Limitations 中承认此 gap。\n\n**W2 [WARNING]. 维度分离未讨论**: Ablation R² 和 trajectory analysis 分别测量连续/离散维度，但论文未讨论这一分离。\n\n**W3 [WARNING]. Discussion 内部矛盾**: 效应均匀分布 vs routing concentration 特殊意义的逻辑不一致。\n\n**W4 [WARNING]. Overclaim 残余**: Introduction findings + Contribution (i)(iii) + Discussion 仍有 unqualified generalizations。\n\n**W5 [WARNING]. CKA 矛盾正文讨论不足**: C3 的 metric-dependency 仅括号提及。\n\n---\n\n## Questions to Authors\n\nQ1. Trajectory analysis 显示 72.3% action tokens 改变——其中有多少朝 ground-truth 方向改变、多少偏离？哪怕粗略的方向性分析也能大幅增强因果推断。\n\nQ2. 如果 routing 效应主要影响 gripper (discrete) 维度而 R² 改善测的是 continuous 维度，这两个结果是否在测量不同的 L1 功能？如果是，C2 的 claim scope 应如何调整？\n\nQ3. 既然 per-head effects 在 instruction-dominant 和 non-dominant heads 之间 comparable，将 24/32 heads 标记为 \"instruction-dominant\" 的分析价值是什么？attention pattern 与 functional contribution 的解耦应如何理解？\n\n---\n\n## Missing References\n\n本轮无新的 missing reference。Round 6 建议的四篇（Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024）已全部添加。\n\n---\n\n## Overall Assessment\n\n**评分: 5.5/10 — Borderline (Weak Reject 倾向)**\n\n论文从 Round 6 的 4.5/10 提升至 5.5/10，方法论严谨性有实质改善。核心阻碍仍是 **缺乏 behavioral validation**——对 CoRL 这个机器人学习会议，纯 representational/open-loop analysis 论文面临天然劣势。\n\n**当前论文如提交 CoRL 2026 的预期评价**:\n- 方法论: 中上（factorial design 有参考价值，统计处理得当）\n- 新颖性: 中等（C1 是 verification，C2 routing reorganization 是核心 insight，C3 metric-dependent）\n- 完整性: 中下（无 behavioral validation，Discussion 有内部矛盾）\n- 写作: 中上（结构清晰，但有 overclaim 残余和 CKA 讨论不足）\n\n**可操作的改善路径（按优先级）**:\n1. **[HIGH]** Limitations 承认 behavioral gap（0.5h 修复，消除审稿人最可能的 \"fatal flaw\" 判断）\n2. **[HIGH]** Discussion \"confirms the causal role\" 改为 \"demonstrates causal influence\"（5min 修复）\n3. **[HIGH]** main.tex 加 `\\input{conclusion}`（1min 修复）\n4. **[MEDIUM]** Introduction findings + Contribution (i)(iii) 加 model-specific 限定（30min）\n5. **[MEDIUM]** 讨论维度分离 + 修复 Discussion 矛盾（1h）\n6. **[MEDIUM]** Section 4.4 加 CKA 正文讨论（15min）\n7. **[LOW → HIGH if feasible]** 任何 closed-loop behavioral 数据（哪怕 1-2 tasks）\n\nR1 评论: \"我维持 6/10 但承认 5/10 也有合理依据——取决于审稿人对 'CoRL 是否接受无 behavioral validation 的纯分析论文' 这个 meta-question 的判断。\"\n\nR2 评论: \"方法论改善是真实的。但 CoRL 审稿人会问：这些 findings 能帮我训练更好的 robot 吗？目前论文无法直接回答这个问题。\"\n\n---\n\n## Detailed Score Breakdown\n\n| Criterion | Score | Notes |\n|-----------|-------|-------|\n| Novelty | 5/10 | C2 routing reorganization 是 genuine insight; C1=verification, C3=metric-dependent |\n| Soundness | 6/10 | 方法论大幅改善; ablation 仍有 internal inconsistency |\n| Significance | 4/10 | 无 behavioral validation 限制 impact; CoRL community needs actionable |\n| Clarity | 6/10 | 结构好但有 overclaim + Discussion 矛盾 |\n| Completeness | 5/10 | 缺 conclusion section + behavioral + CKA 正文讨论 |\n| **Overall** | **5.5/10** | **Borderline — 倾向 Weak Reject** |\n\n---\n\n## Issue Tracker 同步状态\n\n- **RESOLVED (本轮)**: R6-C2, R6-W1\n- **CRITICAL (仍 open)**: R6-C4 (behavioral validation)\n- **WARNING (仍 open)**: R6-C1, R6-C3, R7-W1, R7-W2, R7-W3\n- **INFO → WARNING**: R4-I1 (conclusion.tex)\n- **完整 issue tracker**: `projects/vla-ssd/artifacts/review_issues.yaml`\n\n---\n\n*Reviewed by: R1 (方法/实验), R2 (新颖性/完整性). Cross-responses completed by both reviewers with full consensus on all issues.*",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# Round 7 审稿汇总报告\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026 (deadline 2026-05-29)\n**审稿模式**: 继续审稿（基于 Round 6 修改稿）\n**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)\n**本轮评分**: R1 = 6/10, R2 = 5/10 → 共识 5.5/10 Borderline\n\n---\n\n## Summary\n\n本轮审查基于 Round 6 报告提出的 2 个 CRITICAL + 4 个 WARNING + 若干 INFO 级 issue，评估修改稿的回应充分性。论文在方法论严谨性上有实质进步（demo-level split 消除时间泄漏、task-level RSA bootstrap、routing-first 叙事重写、trajectory analysis 新增），但核心结构性问题（无 behavioral validation）仍未解决，且修改引入了新的 internal inconsistency。\n\n---\n\n## Resolved Issues（本轮确认解决）\n\n### R6-C2 [RESOLVED] Probe train/test split + 时间自相关\nMethod §3.5 明确 demo-level sequential split (demos 0-39 train / 40-49 test)，完全消除时间泄漏风险。这是本轮最重要的方法论改进。\n\n### R6-W1 [RESOLVED] RSA pairwise dependency 未处理\nMethod §3.4 新增 task-level block resampling 说明 + Nili 2014 引用。N=10 tasks 的统计功效有限但属固有限制。\n\n---\n\n## Open Issues\n\n### 🔴 CRITICAL\n\n#### R6-C4 [STILL OPEN] 缺 behavioral validation，对 CoRL 结构性缺口\n**状态**: 新增 open-loop action trajectory analysis (Cohen's d=0.65, 72.3% token divergence)，但这不是 behavioral validation。72.3% 的 action token 改变不告诉读者 task success 变好还是变差。对 CoRL（机器人学习会议）而言，\"representational analysis without any task success metric\" 是结构性缺口。\n\n**具体问题**:\n- Discussion line 11 \"confirms the causal role\" 措辞过强——trajectory divergence 只证明 causal influence on output，不证明 functional role\n- Limitations 段落（Discussion lines 14-15）未承认 behavioral gap，仅讨论 single-model generalization\n- MuJoCo 版本不兼容是可理解的技术障碍，但论文应明确承认此限制\n\n**建议修复**:\n- Discussion: \"confirms the causal role\" → \"demonstrates causal influence on action output\"\n- Limitations 新增: \"Our analyses are representational and open-loop; connecting these findings to task success requires closed-loop behavioral evaluation, which we leave to future work.\"\n- 如能在 deadline 前解决 MuJoCo 兼容问题并提供哪怕 1-2 个 task 的 success rate，将大幅增强论文说服力\n\n---\n\n### 🟡 WARNING\n\n#### R6-C1 [DOWNGRADED → WARNING] Ablation 因果推断方向\n**状态**: 从 CRITICAL 降级。\"routing-first specialization\" 叙事比 \"dual function\" 更准确，trajectory analysis 提供了 output-level 因果证据。但存在 internal inconsistency:\n- R² 衡量连续动作维度的改善，trajectory 效应集中在 gripper 离散维度（shift 0.291 vs <0.034）——两个 metric 在讲不同维度的故事（→ R7-W1）\n- \"Per-head effects are comparable\" 削弱 instruction-dominant heads 作为 functionally distinct group 的叙事（→ R7-W2）\n- N=10 random subsets 偏少（z=-2.73 基于 10 个样本的正态假设）\n\n#### R6-C3 [DOWNGRADED → WARNING] 单模型 overclaim 残余\n**状态**: 从 CRITICAL 降级。Abstract line 7 \"in the model studied\" ✓。但 Introduction lines 16-20 \"Three findings emerge\" 仍用一般化措辞，Contribution (i) 和 (iii) 未限定模型，Discussion \"early-layer parameters may suffice\" 仍 unqualified。\n\n**建议修复**: Introduction findings 段落加 \"In OpenVLA-7B on LIBERO\" 前缀；Contribution (i)(iii) 各加 model-specific 限定。\n\n#### R7-W1 [NEW] 维度分离未讨论\nAblation R² 改善测的是连续维度，trajectory divergence 集中在 gripper（shift 0.291 vs continuous <0.034）。论文将两者并列呈现仿佛互相支撑，但实际测量的是不同 action space 维度。如果 routing 主要影响 gripper control，claim scope 应更精确限定。\n\n#### R7-W2 [NEW] Per-head comparability + Discussion 自相矛盾\nExperiments line 86 \"Per-head effects are comparable\" 意味着 instruction-dominant heads 的 per-head 影响力与非 instruction-dominant heads 相当，削弱了将这 24 个 heads 作为 functionally distinct group 的叙事。Discussion line 12 前半句 \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones\" 与后半句 \"yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation\" 逻辑矛盾：如果效应均匀分布，不能同时推论 routing concentration 的特殊意义。\n\n#### R7-W3 [NEW] CKA 矛盾正文讨论不足\nMethod §3.6 \"Why RSA over CKA\" justification 已加强，但 CKA 完全反转 inverted-U（monotonically increasing）这一重要矛盾结果仅在 Introduction line 20 一句括号中提及。读者不翻 Appendix 不知道 C3 的 metric-dependency 有多严重。建议 Section 4.4 加 1-2 句正文讨论。\n\n---\n\n### ℹ️ INFO (升级建议)\n\n#### R4-I1 [PERSISTENT] conclusion.tex 未编译\nRound 4 发现至今未修复。main.tex 无 `\\input{conclusion}`。conclusion.tex 含 code release 声明被浪费。修复成本极低（一行代码）。建议升级至 WARNING：CoRL 要求完整论文结构，缺 Conclusion 可能被审稿人视为不完整。\n\n---\n\n## Strengths（修改后新增/增强）\n\n**S1. 方法论严谨性显著提升**: Demo-level split 彻底解决时间泄漏（Round 6 最严重的方法论问题），task-level block resampling 正确处理 RSA pairwise dependency。这两项修改使统计推断的可信度大幅提高。\n\n**S2. Routing-first 叙事更准确**: 从 \"dual function\" 改为 \"routing-first specialization\" 是正确方向——承认 R² increase 而非 post-hoc 强行解释。\n\n**S3. Trajectory analysis 增加因果证据**: Open-loop action trajectory comparison (d=0.65, 72.3% divergence) 虽非 behavioral validation，但比纯 representational analysis 更接近 output-level 证据。Gripper 维度的 selective effect (0.291 vs <0.034) 是有趣发现。\n\n**S4. 三条件 factorial 设计**: Trained/Pretrained/Untrained 三条件交叉 instruction presence 的设计仍是本文最大方法论贡献，在 VLA 分析文献中具有参考价值。\n\n**S5. RSA justification 加强**: Method 新增 RSA 功能性论证（\"captures relative distance structure directly governing action prediction quality\"），说服力提升。\n\n---\n\n## Weaknesses（当前版本）\n\n**W1 [CRITICAL]. 缺 behavioral validation**: 对 CoRL 是结构性缺口。Open-loop trajectory divergence ≠ task success。论文未在 Limitations 中承认此 gap。\n\n**W2 [WARNING]. 维度分离未讨论**: Ablation R² 和 trajectory analysis 分别测量连续/离散维度，但论文未讨论这一分离。\n\n**W3 [WARNING]. Discussion 内部矛盾**: 效应均匀分布 vs routing concentration 特殊意义的逻辑不一致。\n\n**W4 [WARNING]. Overclaim 残余**: Introduction findings + Contribution (i)(iii) + Discussion 仍有 unqualified generalizations。\n\n**W5 [WARNING]. CKA 矛盾正文讨论不足**: C3 的 metric-dependency 仅括号提及。\n\n---\n\n## Questions to Authors\n\nQ1. Trajectory analysis 显示 72.3% action tokens 改变——其中有多少朝 ground-truth 方向改变、多少偏离？哪怕粗略的方向性分析也能大幅增强因果推断。\n\nQ2. 如果 routing 效应主要影响 gripper (discrete) 维度而 R² 改善测的是 continuous 维度，这两个结果是否在测量不同的 L1 功能？如果是，C2 的 claim scope 应如何调整？\n\nQ3. 既然 per-head effects 在 instruction-dominant 和 non-dominant heads 之间 comparable，将 24/32 heads 标记为 \"instruction-dominant\" 的分析价值是什么？attention pattern 与 functional contribution 的解耦应如何理解？\n\n---\n\n## Missing References\n\n本轮无新的 missing reference。Round 6 建议的四篇（Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024）已全部添加。\n\n---\n\n## Overall Assessment\n\n**评分: 5.5/10 — Borderline (Weak Reject 倾向)**\n\n论文从 Round 6 的 4.5/10 提升至 5.5/10，方法论严谨性有实质改善。核心阻碍仍是 **缺乏 behavioral validation**——对 CoRL 这个机器人学习会议，纯 representational/open-loop analysis 论文面临天然劣势。\n\n**当前论文如提交 CoRL 2026 的预期评价**:\n- 方法论: 中上（factorial design 有参考价值，统计处理得当）\n- 新颖性: 中等（C1 是 verification，C2 routing reorganization 是核心 insight，C3 metric-dependent）\n- 完整性: 中下（无 behavioral validation，Discussion 有内部矛盾）\n- 写作: 中上（结构清晰，但有 overclaim 残余和 CKA 讨论不足）\n\n**可操作的改善路径（按优先级）**:\n1. **[HIGH]** Limitations 承认 behavioral gap（0.5h 修复，消除审稿人最可能的 \"fatal flaw\" 判断）\n2. **[HIGH]** Discussion \"confirms the causal role\" 改为 \"demonstrates causal influence\"（5min 修复）\n3. **[HIGH]** main.tex 加 `\\input{conclusion}`（1min 修复）\n4. **[MEDIUM]** Introduction findings + Contribution (i)(iii) 加 model-specific 限定（30min）\n5. **[MEDIUM]** 讨论维度分离 + 修复 Discussion 矛盾（1h）\n6. **[MEDIUM]** Section 4.4 加 CKA 正文讨论（15min）\n7. **[LOW → HIGH if feasible]** 任何 closed-loop behavioral 数据（哪怕 1-2 tasks）\n\nR1 评论: \"我维持 6/10 但承认 5/10 也有合理依据——取决于审稿人对 'CoRL 是否接受无 behavioral validation 的纯分析论文' 这个 meta-question 的判断。\"\n\nR2 评论: \"方法论改善是真实的。但 CoRL 审稿人会问：这些 findings 能帮我训练更好的 robot 吗？目前论文无法直接回答这个问题。\"\n\n---\n\n## Detailed Score Breakdown\n\n| Criterion | Score | Notes |\n|-----------|-------|-------|\n| Novelty | 5/10 | C2 routing reorganization 是 genuine insight; C1=verification, C3=metric-dependent |\n| Soundness | 6/10 | 方法论大幅改善; ablation 仍有 internal inconsistency |\n| Significance | 4/10 | 无 behavioral validation 限制 impact; CoRL community needs actionable |\n| Clarity | 6/10 | 结构好但有 overclaim + Discussion 矛盾 |\n| Completeness | 5/10 | 缺 conclusion section + behavioral + CKA 正文讨论 |\n| **Overall** | **5.5/10** | **Borderline — 倾向 Weak Reject** |\n\n---\n\n## Issue Tracker 同步状态\n\n- **RESOLVED (本轮)**: R6-C2, R6-W1\n- **CRITICAL (仍 open)**: R6-C4 (behavioral validation)\n- **WARNING (仍 open)**: R6-C1, R6-C3, R7-W1, R7-W2, R7-W3\n- **INFO → WARNING**: R4-I1 (conclusion.tex)\n- **完整 issue tracker**: `projects/vla-ssd/artifacts/review_issues.yaml`\n\n---\n\n*Reviewed by: R1 (方法/实验), R2 (新颖性/完整性). Cross-responses completed by both reviewers with full consensus on all issues.*",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-18T13:47:23.290149+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 520 · 2026-05-18T13:47:30.179415+00:00_

Round 7 审稿报告已投递。

**汇总**: 评分 5.5/10 Borderline（R1=6, R2=5）。2 个 issue 本轮解决（demo-level split、RSA bootstrap），1 个 CRITICAL 仍 open（behavioral validation），5 个 WARNING open（ablation inconsistency、overclaim 残余、维度分离、Discussion 矛盾、CKA 讨论不足）。论文从 Round 6 的 4.5 提升至 5.5，方法论有实质改善，但 CoRL 结构性缺口（无 task success metric）仍是核心阻碍。报告含按优先级排序的 7 项可操作修复建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 521 · 2026-05-18T13:47:31.294837+00:00_

[Reviewer 1 审稿结果]:
Round 2 交叉回应已提交。

核心判断：同意 R2 将 R6-C1 (ablation) 降为 WARNING、R6-C4 (behavioral validation) 保持 CRITICAL。维持 6/10 评分，与 R2 的 5/10 差距主要在于对 probe split 和 RSA bootstrap 修复带来的可信度提升的权重不同。最终评价取决于 CoRL AC 对纯分析论文是否需要 behavioral evidence 的 meta-level 判断。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 Round 2 评估

---

## Issue Verification 差异

### R6-C1 (Ablation): R1 保持 CRITICAL，我降为 WARNING

**[AGREE with R1 on points 1, 2, 4; REBUT on severity]**

R1 的四点诊断我逐条回应：

1. **"ALL ablation increase R², routing-first 仍是 post-hoc"** — [AGREE] 事实判断完全正确。我在自己的 Round 2 评估中也指出 "routing-first" 仍是 rationalization。R² 方向性问题没有被新叙事解决。

2. **Discussion line 12 自相矛盾** — [AGREE] "effect distributes across L1 heads" 与 "routing concentration suggests early-layer suffice" 确实矛盾。如果效应均匀分布，那 instruction-dominant heads 的 "routing concentration" 就不是功能上的特殊性，只是 attention pattern 的描述性统计。

3. **N=10 random subsets 未增加** — [AGREE] 事实正确。不过这是 degree 问题而非 kind 问题：即使增加到 100 subsets，如果方向性问题（all increase R²）不变，z-score 的 precision 提升不改变解释困境。

4. **效应集中 gripper dimension** — [AGREE] 这是我的 N1 新发现的核心，Appendix Table 清楚显示连续维度 shift <0.034。Claim scope 应缩小到 "L1 routing primarily affects discrete gripper decisions"。

**但我坚持降为 WARNING 而非 CRITICAL 的理由**：Round 1 到 Round 2 的关键变化是 action trajectory validation 的加入。虽然 interpretation 有问题，但新数据（d=0.65, 72.3% divergence）确实证明了 L1 heads 因果性地影响 action token 生成——这是 Round 1 完全缺失的。问题从 "无因果证据" 变为 "因果证据的 interpretation 有 inconsistency"，severity 应下降一级。如果 R1 的 CRITICAL 定义是 "影响接收决定"，我认为 ablation interpretation 的不完美不足以单独否决论文——routing reorganization 的核心发现（三条件梯度、entry-exit pattern、Figure 1）不依赖于 ablation 解释。

**结论**：同意 R1 的所有事实判断，但认为 WARNING 更合适，因为 ablation 是 supporting evidence 而非 core claim 的唯一支撑。

---

### R6-C2 (Probe split): [AGREE — RESOLVED]

Demo-level split（demos 0-39 train, 40-49 test, Method line 59）完全消除了时间自相关导致的 train/test leakage。这是 Round 1 两位 reviewer 共同关切的方法论问题，修复彻底。

对 R1 残余 INFO（linear vs MLP 20× gap 未在正文讨论）：同意这是 INFO 级别。论文在 Appendix F 已有讨论（"MLP nonlinearity partially rescues degraded representations"），正文 Section 4.1 line 12 也提到 overparameterization + linear probe replication。理想情况下正文加一句 summary，但不影响结论可信度。

---

### R6-C4 (Behavioral validation): 我保持 CRITICAL，R1 偏 WARNING

**[REBUT R1's milder assessment — 我认为对 CoRL 这仍是 CRITICAL]**

理由分三层：

1. **Venue-specific standard**：CoRL 是机器人学习会议，不是 representation learning workshop。审稿人的隐性期望是 findings 能连接到 robot behavior。纯 representational analysis 在 ICLR/NeurIPS 可以独立成文，但 CoRL 审稿人会问 "so what for robot design?"。论文的 Discussion 暗示了 design implications（"early-layer parameters may suffice for adaptation"）但没有任何验证。

2. **Open-loop ≠ behavioral**：Action trajectory analysis 测的是 "predicted tokens change"，不是 "robot succeeds or fails"。72.3% token divergence 听起来很大，但如果 divergent tokens 仍在 success region 内（action space 有容错），behavioral impact 可能极小。反之，如果 divergence 导致 catastrophic failure，那才是 strong evidence。缺少这一步就无法判断 routing 的 practical significance。Discussion line 12 写 "confirms the causal role" 对 "causal role" 的定义过宽——这点我同意 R1 的诊断。

3. **Limitations 未明确承认**：Discussion lines 14-15 的 Limitations 段落讨论了 model generalization（"C2 may differ across backbone scales"），但完全没有提到 behavioral validation 的缺失。对于一个自知没做 closed-loop evaluation 的论文，这是一个 framing 问题：如果 Limitations 明确写 "all analyses are representational; closed-loop behavioral validation remains future work"，审稿人至少知道作者 aware of the gap。当前版本看起来像作者认为 trajectory analysis 已经 sufficient。

**这一差异是否影响评分**：是。这是我给 5/10 而非 6/10 的主要原因之一。如果论文加 1-2 句明确承认 behavioral gap，我愿意升到 5.5 或 borderline 6。

---

## R1 新发现回应

### N1 (Discussion 自相矛盾): [AGREE — WARNING]

同意这是 WARNING 级别。Discussion line 12 的逻辑断裂：

> "the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, **yet** L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation"

前半句说 "效应不集中在 instruction-dominant heads"，后半句用 "routing concentration"（即 instruction-dominant heads 的集中）来推论 design implication。这是同一段内的 self-contradiction。R1 和我（N2）从不同角度捕捉到了同一个问题。

这反映了一个更深层的 framing 问题：论文想同时讲 (a) instruction-dominant heads 是 functionally special 的（Section 4.3 前半部分的整个 narrative），和 (b) L1 heads 的 per-head effect 是 uniform 的（line 86 的 trajectory analysis 结论）。两者不能同时为真。

---

### N2/N3 (conclusion.tex): [AGREE — INFO]

同意 INFO 级别。未编译不影响当前审稿（Discussion 已有足够 wrap-up），但应在提交前修复。

---

## 评分差异分析

### R1: 6/10, R2 (我): 5/10

R1 认为方法论修复（probe split + RSA bootstrap）"显著提升了统计推断可信度"，使论文从 below 升至 above threshold。

**[PARTIALLY AGREE]**

方法论修复确实重要且执行到位：
- Demo-level split 消除了最严重的 validity threat
- Task-level RSA bootstrap 是正确的统计处理
- 四篇引用补齐，GenAI disclosure 到位

这些修复将论文的 methodological soundness 从 "有疑问" 提升到 "solid"。在这一点上我同意 R1。

**我维持 5/10 的决定性因素**是两个 R1 也认同但 weight 不同的问题：

1. **Behavioral validation gap [CRITICAL]**：如上所述，对 CoRL 这不是可选的 nice-to-have。R1 给 6/10 意味着他认为 representational findings 本身对 CoRL 有足够价值；我不同意——CoRL 的审稿人群体比 ICLR/NeurIPS 更重视 practical robotics implications。

2. **Effective contribution count**：C1 是架构验证（framework validation），C3 是 metric-dependent observation，core novelty 实质上只有 C2（routing reorganization）。单一 finding 在单一 model 上，对 CoRL 的 bar 偏低。R1 可能将 C2 的 depth 和 rigor 权重更高；我认为 breadth（multi-model）和 impact（behavioral connection）同样重要。

**如果论文在 final version 中做到以下两点，我会升至 6/10**：
- Limitations 明确承认 closed-loop behavioral validation 缺失
- Discussion line 12 的自相矛盾修复（删除 "yet" 后的 overreach，或修改为 conditional language）

这两点都是 1-2 句的文字修改，不需要新实验。

---

## 总结

| Issue | R1 判断 | R2 判断 | 共识？ |
|-------|---------|---------|--------|
| R6-C1 ablation | STILL_OPEN (CRITICAL) | STILL_OPEN (WARNING) | 事实共识，severity 分歧 |
| R6-C2 probe split | RESOLVED | RESOLVED | ✓ |
| R6-C3 overclaim | （未单独追踪） | STILL_OPEN (WARNING) | — |
| R6-C4 behavioral | STILL_OPEN (partial) | STILL_OPEN (CRITICAL) | 事实共识，severity 分歧（方向相反） |
| R6-W1 RSA stats | RESOLVED | RESOLVED | ✓ |
| Discussion 矛盾 | N1 WARNING | N2 WARNING | ✓ |
| conclusion.tex | N2 INFO | P3 WARNING→INFO | ✓ |
| Overall score | 6/10 | 5/10 | 分歧 |

核心分歧归结为一个判断：**对 CoRL 而言，单模型 representational analysis 在无 behavioral validation 的情况下是否足够？** R1 倾向于 yes（如果方法论 sound），我倾向于 no（需要至少 acknowledge the gap explicitly）。这是 legitimate disagreement，应由 AC/Director 权衡。


---

[Reviewer 2 审稿结果]:
审稿意见已提交。

核心分歧总结：R1 给 6/10，我给 5/10。事实判断高度一致（ablation 方向性问题、Discussion 自相矛盾、behavioral gap），分歧在 severity weighting。我的 5/10 主要因为 CoRL 对 behavioral validation 的隐性要求——如果论文在 Limitations 中明确承认这一 gap 并修复 Discussion 的逻辑矛盾（均为 1-2 句文字改动），我愿升至 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 522 · 2026-05-18T13:47:53.982257+00:00_

Round 7 审稿报告已在上一轮提交，R2 的交叉回应内容与报告中的共识判断完全一致。本轮审稿流程已完成：

- 两位 Reviewer 独立初审 ✓
- 交叉分享 + 逐条回应 ✓
- Issue Tracker 同步 ✓
- 汇总报告已投递 Research Director ✓

最终共识：**5.5/10 Borderline (Weak Reject 倾向)**。核心分歧在于 CoRL 对 behavioral validation 的隐性要求——R1 认为 methodological soundness 足够 (6/10)，R2 认为缺 behavioral evidence 对 CoRL 是结构性缺口 (5/10)。两位 Reviewer 在所有事实判断上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 57

## Round 57

24 recorded events


### User

_source line 523 · 2026-05-18T14:09:40.121650+00:00_

[Round 7 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/vla-ssd/artifacts/review_reports/round_6.md`
跨轮次问题追踪: `projects/vla-ssd/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-18T14:09:50.613790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_7.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_7.md"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-18T14:09:51.015613+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-18T14:09:51.066542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-18T14:09:51.118237+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-5 历史 issues（全部 resolved，压缩保留）
4	  # ============================================================
5	  - id: R1-N1-old
6	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 2
12	    resolution: "三条件数据完整整合。"
13	    resolution_round: 3
14	    mentions: []
15	    action_items: []
16	
17	  - id: R1-N2-old
18	    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
19	    category: framing
20	    severity: critical
21	    status: resolved
22	    first_raised_round: 1
23	    last_seen_round: 2
24	    resolution: "Title 改为单数。"
25	    resolution_round: 3
26	    mentions: []
27	    action_items: []
28	
29	  - id: R1-N4-old
30	    summary: "Design implications 完全基于 correlational evidence"
31	    category: framing
32	    severity: critical
33	    status: resolved
34	    first_raised_round: 1
35	    last_seen_round: 2
36	    resolution: "Abstract 使用 hedge 语气。"
37	    resolution_round: 3
38	    mentions: []
39	    action_items: []
40	
41	  - id: R1-N3-old
42	    summary: "RSA best-vs-best selection bias"
43	    category: experiment
44	    severity: warning
45	    status: resolved
46	    first_raised_round: 1
47	    last_seen_round: 2
48	    resolution: "Same-layer comparison 为 primary evidence。"
49	    resolution_round: 3
50	    mentions: []
51	    action_items: []
52	
53	  - id: R2-N1-old
54	    summary: "Neo et al. (ICLR 2025) 未引用"
55	    category: framing
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 2
60	    resolution: "已引用。"
61	    resolution_round: 3
62	    mentions: []
63	    action_items: []
64	
65	  - id: R2-W1-old
66	    summary: "Related Work 引用覆盖度不足"
67	    category: writing
68	    severity: warning
69	    status: resolved
70	    first_raised_round: 1
71	    last_seen_roun
…[truncated 20183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-18T14:10:04.032049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-18T14:10:04.536845+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-18T14:10:04.537308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-18T14:10:04.990186+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	While the decoder-only architecture imposes structural constraints on information flow (the causal mask prevents image tokens from attending to subsequent instruction tokens), how VLA fine-tuning reshapes the routing and integration of multimodal information within the LLM backbone remains uncharacterized.
6	
7	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
8	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
9	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
10	
11	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
12	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
13	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\c
…[truncated 2307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-18T14:10:04.990639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-18T14:10:05.493829+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind; the readout is the sole multimodal convergence point.
6	Training shifts routing from mid-depth to entry-exit (L0--L1, L31), with effects at the readout ($R^2$ $+0.069$) rather than images ($\Delta \leq 1.7\%$).
7	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
8	Two independent analyses converge on L1 as the routing hub: attention shows training-dependent entry-exit reorganization (\S\ref{sec:learned_routing}), and representational probes show a cross-layer ablation gradient confined to L1 ($R^2$ $+0.059$ at L1 vs.\ $+0.018$ at L8 vs.\ $\approx 0$ at L13). Action trajectory analysis further confirms that L1 ablation alters $72.3\%$ of tokens ($d = 0.65$), establishing a causal link from routing to output.
9	
10	\paragraph{Mechanistic interpretation.}
11	Per-layer RSA bifurcates after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually while image\_mean drops sharply ($\to 0.422$), consistent with mid-layer integration and deep-layer compression.
12	L1 ablation demonstrates causal influence on action output ($z = -2.73$ vs.\ random subsets) and is L1-confined ($|\Delta R^2| < 0.02$ at deeper layers).
13	The $R^2$ improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect ($72.3\%$ divergence) reflects discrete manipulation sensitivity.
14	The attention analysis reveals what the model learns (reorganized routing), while ablation reveals how the function is implemented (distributed across the layer). Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.
15	
16	\paragraph{Predictions.}
17	Other decoder-only VLAs (e.
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-18T14:10:05.494344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-18T14:10:05.947697+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind.}
21	Image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}), consistent with the causal mask and frozen encoder.
22	Both linear and MLP probes confirm this, as does standalone DINOv2 ($10\%$), ruling out probe capacity.

…[truncated 10100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-18T14:10:05.948160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-18T14:10:06.300391+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we validate the framework by confirming architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions), while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31); instruction classification reaches $99.6\%$ at L1 (vs.\ pretrained $80.2\%$), and L1 ablation confirms routing-first head specialization (random-subset control, L1-confined). Untrained models show zero instruction-dominant heads throughout.
6	Third, vision encoder representations follow a metric-dependent non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L14; RSA confirms but CKA diverges; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-18T14:10:06.351243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-18T14:10:06.401803+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present factorial-controlled analysis of VLA representations, revealing token-level specialization, front-loaded instruction routing, and non-monotonic refinement concentrated at the readout token. Code and representations will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-18T14:11:06.153721+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-18T14:11:06.205104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-18T14:11:30.517778+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "# Round 8 — Reviewer 1 任务（方法/实验严谨性）\n\n**模式**: 继续审稿（验证 Round 7 open issues 的修复）\n**Venue**: CoRL 2026, 8 pages + unlimited refs, double-blind\n**论文路径**: `projects/vla-ssd/docs/paper/main.tex`\n\n## 你的任务\n\n逐条验证以下 in_progress issues 是否已充分修复。每条标 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。\n\n---\n\n## Open Issues 清单\n\n### 🔴 R6-C4 [CRITICAL] 缺 behavioral validation\n**Round 7 诊断**: Discussion \"confirms the causal role\" 过强；Limitations 未承认 behavioral gap。\n**预期修复**: (P1) Discussion 弱化措辞；(P2) Limitations 新增 behavioral gap 声明。\n**验证要点**:\n- 读 Discussion 全文，检查是否仍有过强的因果措辞（特别关注 \"establishing\"/\"confirms\"/\"proves\" 等词）\n- 读 Limitations 段落，检查是否明确承认 open-loop 限制\n- 评估修复是否充分降低了 CoRL 审稿人的 rejection risk\n\n### 🟡 R6-C1 [WARNING] Ablation 因果推断 + internal inconsistency\n**Round 7 诊断**: (a) R² 测连续维度 vs trajectory 测 gripper 维度未讨论；(b) per-head effects comparable 削弱 dominant-head 叙事；(c) Discussion 自相矛盾。\n**预期修复**: (P5) 正文讨论维度分离；(P6) Discussion 重写 attention/ablation interpretation。\n**验证要点**:\n- 读 Discussion \"Mechanistic interpretation\" 段落，检查维度分离是否有合理解释\n- 检查 \"collective role\" 叙事是否与 Experiments 的 \"per-head effects are comparable\" 一致\n- 检查新 Discussion 是否消除了 Round 7 的自相矛盾\n\n### 🟡 R7-W1 [WARNING] 维度分离未讨论\n**与 R6-C1 合并验证**。检查 Discussion 是否讨论 R² (continuous) vs trajectory (gripper) 的分离。\n\n### 🟡 R7-W2 [WARNING] Per-head comparability + Discussion 矛盾\n**与 R6-C1 合并验证**。检查 \"effect distributes across L1 heads\" 与 routing concentration 的逻辑是否自洽。\n\n### ℹ️ R5-N4 [WARNING, in_progress] Behavioral gap in Limitations\n**与 R6-C4 合并验证**。\n\n---\n\n## 也请检查\n\n1. **新 Discussion 结构的整体连贯性**: Synthesis → Mechanistic interpretation → Predictions → Limitations。逻辑链是否通畅？\n2. **Predictions 段落** (新增): 是否过度推测？是否有足够证据支撑？\n3. **Experiments 是否有冗余或遗漏**: ablation + trajectory 段落是否仍 self-consistent？\n4. **修改是否引入新的 overclaim 或逻辑断裂**\n\n## 输出格式\n\n```\n## Issue Verification\n[逐条 RESOLVED/STILL_OPEN]\n\n## New Issues (if any)\n[新发现]\n\n## Discussion Quality Assessment\n[新 Discussion 结构评价]\n\n## Score\n[评分 /10 + 理由]\n```",
  "reviewer_id": "1",
  "project": "vla-ssd",
  "round_number": "8"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "# Round 8 — Reviewer 1 任务（方法/实验严谨性）\n\n**模式**: 继续审稿（验证 Round 7 open issues 的修复）\n**Venue**: CoRL 2026, 8 pages + unlimited refs, double-blind\n**论文路径**: `projects/vla-ssd/docs/paper/main.tex`\n\n## 你的任务\n\n逐条验证以下 in_progress issues 是否已充分修复。每条标 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。\n\n---\n\n## Open Issues 清单\n\n### 🔴 R6-C4 [CRITICAL] 缺 behavioral validation\n**Round 7 诊断**: Discussion \"confirms the causal role\" 过强；Limitations 未承认 behavioral gap。\n**预期修复**: (P1) Discussion 弱化措辞；(P2) Limitations 新增 behavioral gap 声明。\n**验证要点**:\n- 读 Discussion 全文，检查是否仍有过强的因果措辞（特别关注 \"establishing\"/\"confirms\"/\"proves\" 等词）\n- 读 Limitations 段落，检查是否明确承认 open-loop 限制\n- 评估修复是否充分降低了 CoRL 审稿人的 rejection risk\n\n### 🟡 R6-C1 [WARNING] Ablation 因果推断 + internal inconsistency\n**Round 7 诊断**: (a) R² 测连续维度 vs trajectory 测 gripper 维度未讨论；(b) per-head effects comparable 削弱 dominant-head 叙事；(c) Discussion 自相矛盾。\n**预期修复**: (P5) 正文讨论维度分离；(P6) Discussion 重写 attention/ablation interpretation。\n**验证要点**:\n- 读 Discussion \"Mechanistic interpretation\" 段落，检查维度分离是否有合理解释\n- 检查 \"collective role\" 叙事是否与 Experiments 的 \"per-head effects are comparable\" 一致\n- 检查新 Discussion 是否消除了 Round 7 的自相矛盾\n\n### 🟡 R7-W1 [WARNING] 维度分离未讨论\n**与 R6-C1 合并验证**。检查 Discussion 是否讨论 R² (continuous) vs trajectory (gripper) 的分离。\n\n### 🟡 R7-W2 [WARNING] Per-head comparability + Discussion 矛盾\n**与 R6-C1 合并验证**。检查 \"effect distributes across L1 heads\" 与 routing concentration 的逻辑是否自洽。\n\n### ℹ️ R5-N4 [WARNING, in_progress] Behavioral gap in Limitations\n**与 R6-C4 合并验证**。\n\n---\n\n## 也请检查\n\n1. **新 Discussion 结构的整体连贯性**: Synthesis → Mechanistic interpretation → Predictions → Limitations。逻辑链是否通畅？\n2. **Predictions 段落** (新增): 是否过度推测？是否有足够证据支撑？\n3. **Experiments 是否有冗余或遗漏**: ablation + trajectory 段落是否仍 self-consistent？\n4. **修改是否引入新的 overclaim 或逻辑断裂**\n\n## 输出格式\n\n```\n## Issue Verification\n[逐条 RESOLVED/STILL_OPEN]\n\n## New Issues (if any)\n[新发现]\n\n## Discussion Quality Assessment\n[新 Discussion 结构评价]\n\n## Score\n[评分 /10 + 理由]\n```",
    "reviewer_id": "1",
    "project": "vla-ssd",
    "round_number": "8"
  }
}
````

</details>

---


### Tool result

_source line 543 · 2026-05-18T14:11:48.917850+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18400
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-18T14:11:50.574754+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "# Round 8 — Reviewer 2 任务（新颖性/完整性/格式）\n\n**模式**: 继续审稿（验证 Round 7 open issues 的修复）\n**Venue**: CoRL 2026, 8 pages + unlimited refs, double-blind\n**论文路径**: `projects/vla-ssd/docs/paper/main.tex`\n\n## 你的任务\n\n逐条验证以下 in_progress issues 是否已充分修复。每条标 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。\n\n---\n\n## Open Issues 清单\n\n### 🟡 R6-C3 [WARNING] 单模型 overclaim 残余\n**Round 7 诊断**: Abstract line 7 'in the model studied' ✓，但 Introduction lines 16-20 'Three findings emerge' 无 model-specific 限定；Contribution (i) 和 (iii) 未限定模型；Discussion 'early-layer parameters may suffice' �qualified。\n**预期修复**: (P4) Introduction findings 段落 + Contribution (i)(iii) 加 model-specific 限定。\n**验证要点**:\n- 读 Introduction line 15 开始的 findings 段落，检查是否有 model-specific 前缀\n- 读 Contribution 列表 (i)(iii)，检查是否加了 \"in the model studied\" / \"in this architecture\"\n- 读 Discussion，检查是否还有 unqualified generalizations（特别是新增 Predictions 段落）\n- Abstract 是否保持了 Round 7 的 \"in the model studied\"\n\n### 🟡 R7-W3 [WARNING] CKA 矛盾正文讨论不足\n**Round 7 诊断**: CKA 完全反转 inverted-U 仅括号提及。建议 Section 4.4 加 1-2 句。\n**预期修复**: (P7) Section 4.4 (Non-Monotonic Refinement) 加正文讨论 CKA。\n**验证要点**:\n- 读 Section 4.4，检查是否有明确的 CKA 矛盾讨论\n- 讨论是否充分（读者不翻 Appendix 能否理解 metric-dependency 的严重程度）\n- 措辞是否透明还是试图最小化矛盾\n\n### ℹ️ R4-I1 [INFO] conclusion.tex 未编译\n**Round 7 诊断**: main.tex 无 `\\input{conclusion}`。\n**验证要点**:\n- 读 main.tex，确认 `\\input{conclusion}` 存在\n- 读 conclusion.tex 内容，评估是否 adequate（长度、内容、code release 声明）\n\n---\n\n## 也请检查\n\n1. **Abstract**: 是否仍保持 Round 7 的改进质量？是否有新问题？\n2. **Introduction 叙事连贯性**: findings 段落 model-specific 后，与 Contribution 列表是否一致？\n3. **Discussion \"Predictions\" 段落**: 这是新增内容。评估：(a) 是否 overclaim；(b) 是否有科学价值；(c) 措辞是否 appropriate（prediction vs claim）\n4. **格式检查**: CoRL 2026 要求 8 pages。估算当前页数是否合规。新增内容（CKA 讨论、Predictions、Limitations 扩展、Conclusion）是否导致超页。\n5. **写作质量**: em-dash 检查、-ing phrase 检查、AI 风格标志\n\n## 输出格式\n\n```\n## Issue Verification\n[逐条 RESOLVED/STILL_OPEN]\n\n## New Issues (if any)\n[新发现]\n\n## Completeness & Format Assessment\n[完整性和格式评价]\n\n## Score\n[评分 /10 + 理由]\n```",
  "reviewer_id": "2",
  "project": "vla-ssd",
  "round_number": "8"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "# Round 8 — Reviewer 2 任务（新颖性/完整性/格式）\n\n**模式**: 继续审稿（验证 Round 7 open issues 的修复）\n**Venue**: CoRL 2026, 8 pages + unlimited refs, double-blind\n**论文路径**: `projects/vla-ssd/docs/paper/main.tex`\n\n## 你的任务\n\n逐条验证以下 in_progress issues 是否已充分修复。每条标 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。\n\n---\n\n## Open Issues 清单\n\n### 🟡 R6-C3 [WARNING] 单模型 overclaim 残余\n**Round 7 诊断**: Abstract line 7 'in the model studied' ✓，但 Introduction lines 16-20 'Three findings emerge' 无 model-specific 限定；Contribution (i) 和 (iii) 未限定模型；Discussion 'early-layer parameters may suffice' �qualified。\n**预期修复**: (P4) Introduction findings 段落 + Contribution (i)(iii) 加 model-specific 限定。\n**验证要点**:\n- 读 Introduction line 15 开始的 findings 段落，检查是否有 model-specific 前缀\n- 读 Contribution 列表 (i)(iii)，检查是否加了 \"in the model studied\" / \"in this architecture\"\n- 读 Discussion，检查是否还有 unqualified generalizations（特别是新增 Predictions 段落）\n- Abstract 是否保持了 Round 7 的 \"in the model studied\"\n\n### 🟡 R7-W3 [WARNING] CKA 矛盾正文讨论不足\n**Round 7 诊断**: CKA 完全反转 inverted-U 仅括号提及。建议 Section 4.4 加 1-2 句。\n**预期修复**: (P7) Section 4.4 (Non-Monotonic Refinement) 加正文讨论 CKA。\n**验证要点**:\n- 读 Section 4.4，检查是否有明确的 CKA 矛盾讨论\n- 讨论是否充分（读者不翻 Appendix 能否理解 metric-dependency 的严重程度）\n- 措辞是否透明还是试图最小化矛盾\n\n### ℹ️ R4-I1 [INFO] conclusion.tex 未编译\n**Round 7 诊断**: main.tex 无 `\\input{conclusion}`。\n**验证要点**:\n- 读 main.tex，确认 `\\input{conclusion}` 存在\n- 读 conclusion.tex 内容，评估是否 adequate（长度、内容、code release 声明）\n\n---\n\n## 也请检查\n\n1. **Abstract**: 是否仍保持 Round 7 的改进质量？是否有新问题？\n2. **Introduction 叙事连贯性**: findings 段落 model-specific 后，与 Contribution 列表是否一致？\n3. **Discussion \"Predictions\" 段落**: 这是新增内容。评估：(a) 是否 overclaim；(b) 是否有科学价值；(c) 措辞是否 appropriate（prediction vs claim）\n4. **格式检查**: CoRL 2026 要求 8 pages。估算当前页数是否合规。新增内容（CKA 讨论、Predictions、Limitations 扩展、Conclusion）是否导致超页。\n5. **写作质量**: em-dash 检查、-ing phrase 检查、AI 风格标志\n\n## 输出格式\n\n```\n## Issue Verification\n[逐条 RESOLVED/STILL_OPEN]\n\n## New Issues (if any)\n[新发现]\n\n## Completeness & Format Assessment\n[完整性和格式评价]\n\n## Score\n[评分 /10 + 理由]\n```",
    "reviewer_id": "2",
    "project": "vla-ssd",
    "round_number": "8"
  }
}
````

</details>

---


### Tool result

_source line 545 · 2026-05-18T14:11:52.037237+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 546 · 2026-05-18T14:11:56.885595+00:00_

Round 8 Reviewer 任务已分配：
- **R1**: 验证 R6-C4 (behavioral)、R6-C1 (ablation)、R7-W1 (维度分离)、R7-W2 (per-head comparability)、R5-N4 (Limitations)
- **R2**: 验证 R6-C3 (overclaim)、R7-W3 (CKA)、R4-I1 (conclusion.tex)、新增 Predictions 段落评估

等待 Reviewer 回复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 547 · 2026-05-18T14:13:43.268262+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 8 修订评估

---

## Issue Verification

### 🔴 R6-C4 [CRITICAL]: 缺 behavioral validation — [RESOLVED as WARNING]

**修改确认**:
- Discussion line 12: "confirms the causal role" → "demonstrates causal influence on action output"。措辞从 "confirms" 降为 "demonstrates"，不再隐含因果链已完全建立。
- Limitations line 22（新增）: "Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work."
- Predictions line 18: "L1 ablation on a fine-tuned model should produce measurable task degradation, particularly on instruction-discriminative tasks" — 将 behavioral 验证定位为可验证的 prediction 而非已有结论。

**评估**:
- P2（Limitations 声明）**完全达标**。Line 22 精准承认了两个 gap：(a) representational vs behavioral；(b) open-loop vs closed-loop。措辞克制且具体。
- P1（Discussion 弱化措辞）**大部分达标**。Line 12 "demonstrates causal influence" 是合理的——trajectory analysis 确实 demonstrates L1 ablation 影响 output，这比 "confirms the causal role" 准确得多。

**残余问题**: Discussion line 8 仍使用 "establishing a causal link from routing to output"。"Establishing" 在学术写作中通常意味着 "证实"，比 line 12 的 "demonstrates" 更强。两处措辞不一致：line 8 claim 已 "establish" 因果链，line 22 又承认需要 closed-loop evaluation。建议将 "establishing" 改为 "suggesting" 或 "providing evidence for"。

**Severity 降级理由**: Limitations 的显式 acknowledgment 大幅降低了 CoRL 审稿人的 rejection risk。behavioral gap 仍然存在，但论文不再回避它——这是一个 acknowledged scope limitation 而非 hidden weakness。从 CRITICAL 降为 WARNING。

---

### 🟡 R6-C1 + R7-W1 + R7-W2 [WARNING]: Ablation 因果推断 + 维度分离 + Per-head comparability — [RESOLVED]

**修改确认**:

**(a) 维度分离（R7-W1）**: Discussion line 13:
> "The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect (72.3% divergence) reflects discrete manipulation sensitivity."

这是一个合理且诚实的 framing：显式承认两个分析探测不同维度，并给出各自的解释（R² → continuous bandwidth；trajectory → discrete gripper sensitivity），而非假装两者一致。

**(b) Per-head comparability + Discussion 矛盾（R7-W2）**: Discussion line 14:
> "The attention analysis reveals what the model learns (reorganized routing), while ablation reveals how the function is implemented (distributed across the layer). Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads."

这个重写消除了之前的核心矛盾。新叙事结构：
- Attention analysis 度量的是 WHAT（L1 学到了 routing reorganization → 24/32 heads 变为 instruction-dominant）
- Ablation 度量的是 HOW（功能实现是 distributed → per-head effects comparable）
- "Collective role" 替代了 "individual head specialization"

这与 Experiments line 79 "L1 attention collectively influences action generation rather than through a specialized subset" 完全一致。不再有逻辑断裂。

**(c) Experiments self-consistency**: Ablation 段落（lines 69-74）的 "routing-first specialization" 叙述与 Discussion 的 "collective role" 叙述现在兼容：individual heads carry routing signals（attention analysis shows this），但 functional importance is collective（ablation shows this）。

**残余注意**: Discussion line 8 提到 "R² +0.059 at L1"。此数值未在 Experiments 中出现（Experiments 报告 dominant-head +0.042 和 random-mean +0.077）。推测这是某种平均或中间值，但来源不透明。Minor issue，不影响 resolved 判定。

---

## New Issues

### N1 [INFO]: "Establishing" vs "demonstrates" 措辞不一致

Discussion line 8 "establishing a causal link from routing to output" vs line 12 "demonstrates causal influence" vs Limitations line 22 承认需要 closed-loop evaluation。三处对因果链强度的描述不一致。Line 8 最强（establish），line 12 居中（demonstrate），line 22 最弱（leave to future work）。一次 sed 替换即可修复（establishing → supporting）。

### N2 [INFO]: R² +0.059 来源不明

Discussion line 8 的 "+0.059 at L1" 数值未在 Experiments 或 Appendix 中出现。可能是 dominant (0.042) 和 random (0.077) 的某种加权平均或新计算，但读者无法追溯。建议标明来源或改用已报告的数值。

---

## Discussion Quality Assessment

Discussion 现在是四段结构：Synthesis → Mechanistic interpretation → Predictions → Limitations。

**Synthesis（lines 4-8）**: 逻辑清晰。两条独立证据线（attention reorganization + ablation gradient）收敛于 L1 routing hub，加上 trajectory 确认 output-level 影响。叙事紧凑。Minor issue: "establishing" 过强（见 N1）。

**Mechanistic interpretation（lines 10-14）**: 本轮最大改进。维度分离和 what-vs-how 区分使 ablation 结果的解释从之前的自相矛盾变为逻辑自洽。"Collective role" 的 framing 是对 per-head comparability 的正确回应。RSA bifurcation 的描述简洁有效。

**Predictions（lines 16-18）**: 两条 testable predictions 是好的添加。(1) 其他 decoder-only VLA 应有类似 entry-layer routing（vs cross-attention 架构）；(2) L1 ablation 应导致 task degradation。这些 predictions 使论文的分析发现从描述性升级为可证伪的假设。但需注意 prediction (2) 与 Experiments 的 ablation 结果之间的张力：如果 L1 ablation increases R²（Experiments 所示），为什么作者 predict 它会导致 task degradation？这里隐含假设 R² 增加不等于 behavioral improvement——这与 Limitations line 22 的 acknowledgment 一致，但可以更显式地讨论。

**Limitations（lines 20-22）**: 显著改善。"representational and open-loop" + "closed-loop evaluation...leave to future work" 直接回应了多轮 behavioral validation 的 concern。简洁准确。

**整体连贯性**: 四段之间逻辑链通畅。Synthesis 总结 findings → Mechanistic interpretation 解释 why → Predictions 提出可验证假设 → Limitations 界定 scope。没有明显的逻辑跳跃。

---

## 其他修改检查

### Introduction model-specific qualifiers
- Line 15: "Three findings emerge from our analysis of OpenVLA-7B on LIBERO" — **Good**，明确限定模型和 benchmark。
- Line 23: Contribution (i) "in the model studied"; Contribution (iii) "in this architecture" — **Good**，消除了 overclaim。

### CKA 分歧主文 acknowledgment
- Experiments line 124（新增）: "Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses (Appendix). The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open."
- **Good**. 这是之前多轮要求的修改。读者无需翻阅 Appendix 即可知道 Finding 3 的 metric-dependency。"Its generality across similarity metrics remains open" 是准确的 scope limitation。

### conclusion.tex 编译
- main.tex line 33: `\input{conclusion}` — **Fixed**。R2 多轮指出的 W8 终于修复。

### Experiments 段落一致性
- Ablation（lines 69-74）+ Trajectory（lines 76-80）: 与 Discussion 的 collective role 叙事一致。无新矛盾。

---

## Score

```
Score: 6/10 → 7/10 (↑)
Confidence: 4/5
```

**升分理由**:

1. **R6-C4 从 CRITICAL 降为 WARNING**: Limitations 显式承认 open-loop + representational scope 是本轮最重要的修复。对 CoRL 审稿人来说，"论文知道自己的局限并坦诚表述" 与 "论文回避 behavioral gap" 是截然不同的审稿体验。
2. **R6-C1 完全 RESOLVED**: Discussion rewrite 消除了维度分离矛盾和 per-head comparability 与 routing specialization 之间的逻辑断裂。Collective role framing 是对实验证据的准确叙述。
3. **CKA 分歧进入主文**: Line 124 是一个小但重要的修改，让 Finding 3 的 claim strength 与证据匹配。
4. **Introduction overclaim 修复**: Model-specific qualifiers 遍及全文。
5. **conclusion.tex 编译修复**: 论文结构完整。

**限制升分至 7 的因素**:

1. **"Establishing" 仍过强**（N1）: Discussion line 8 与 Limitations line 22 措辞不一致。修复成本极低但尚未完成。
2. **Behavioral validation 仍是 WARNING**: 论文承认了 gap 但 gap 本身仍在。对 CoRL 来说，纯 representational analysis without rollout 的 novelty bar 更高。
3. **单模型+单 benchmark**: 结构性限制无法在修订中解决。
4. **N=10 random subsets 始终未增加**: 从 Round 1 至今一直是 open concern，统计检验力有限。

**为什么 7 而非 6**: Round 7 到 Round 8 的修改集中解决了 Discussion 的逻辑一致性问题（维度分离、collective role、behavioral gap acknowledgment），这些是上一轮阻碍升分的主要因素。论文现在的 claim 强度与证据基本匹配——剩余问题（N1 措辞、N=10 subsets、单模型泛化）是 minor/structural limitations，不再是方法论缺陷。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 548 · 2026-05-18T14:13:51.151749+00:00_

收到 R1 审稿意见。R1 评分 6→7，核心判断：R6-C4 降为 WARNING，R6-C1/R7-W1/R7-W2 全部 RESOLVED。新发现 2 个 INFO 级问题（"establishing" 措辞不一致、R²+0.059 来源不明）。

等待 R2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 549 · 2026-05-18T14:13:53.806610+00:00_

[Reviewer 1 审稿结果]:
Round 8 评估已提交。评分从 6/10 升至 7/10。

核心变化：
- **R6-C4**（behavioral validation）从 CRITICAL 降为 WARNING：Limitations 新增了显式的 open-loop/representational scope 声明
- **R6-C1**（ablation 逻辑矛盾）RESOLVED：Discussion rewrite 用 "collective role" + what-vs-how 区分消除了维度分离和 per-head comparability 的自相矛盾
- **CKA 分歧**进入主文（experiments line 124），Finding 3 的 metric-dependency 不再被隐藏
- **conclusion.tex** 终于编译，Introduction 加了 model-specific qualifiers

剩余 minor issues：Discussion line 8 的 "establishing" 与 Limitations 的 open-loop acknowledgment 措辞不一致；R² +0.059 来源不明；N=10 random subsets 始终未增加。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 550 · 2026-05-18T14:14:00.239093+00:00_

收到 R1。等待 R2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 60

## Round 60

6 recorded events


### User

_source line 551 · 2026-05-18T14:14:33.194186+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 8 修订评估

**上轮评分**: 5/10 (Borderline)

---

## Issue Verification

### R6-C3 [RESOLVED]: 单模型 overclaim 残余

逐处验证：

**Introduction line 15**: "Three findings emerge from our analysis of OpenVLA-7B on LIBERO." — ✓ 关键修复。这一句将后续所有 findings（lines 16-21）的 scope 限定到了具体模型和 benchmark，无需每句重复。

**Contribution (i)** (line 23): "...verifying architecture-expected specialization between image and readout tokens **in the model studied**" — ✓

**Contribution (ii)** (line 23): "...demonstrated on **OpenVLA-7B/LIBERO**" — ✓（已有）

**Contribution (iii)** (line 23): "the observation, **in this architecture**, that vision encoder representations are non-monotonically transformed..." — ✓

**Abstract line 7**: "in the model studied" — ✓ 保持。

**Discussion**: 
- Predictions 段落（lines 17-18）使用 "should show" / "should produce"，明确为预测而非已验证的 claim — ✓
- Limitations（line 21）: "C2 may differ across backbone scales and decoder paradigms" — ✓ 适当 qualified
- Line 22: "Our analyses are representational and open-loop" — ✓ 直接承认 scope

**Conclusion line 4**: "We present factorial-controlled analysis of VLA representations" — 用了泛化的 "VLA" 而非 "OpenVLA-7B"。但 Conclusion 仅 2 句且是 summary 性质，且前文已全面限定。可接受。

**残余极小**：Conclusion 用 generic "VLA"。不影响接收。

---

### R7-W3 [RESOLVED]: CKA 矛盾正文讨论不足

**Section 4.4 line 124（新增）**:
> "Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses (Appendix~\ref{sec:cka_appendix}). The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open."

这两句话完成了三件事：
1. 明确告知读者 CKA 结果相反（monotonic increase, reversed ordering）
2. 将 inverted-U 限定为 "RSA-specific rank-order geometry"
3. 坦诚承认 "generality across metrics remains open"

不翻 Appendix 的读者现在也知道 CKA 矛盾的存在和程度。措辞透明，不试图最小化分歧。

**配合点**：
- Method §3.6 line 64: 交叉引用 "the divergence between metrics (§\ref{sec:nonmonotonic})" — ✓
- Introduction line 20: "CKA diverging (Appendix)" 也提及 — ✓

**评级**: RESOLVED。处理到位。

---

### R4-I1 [RESOLVED]: conclusion.tex 未编译

**main.tex line 33**: `\input{conclusion}` — ✓ 现在正确地出现在 `\input{discussion}` 和 `\bibliography{references}` 之间。

**conclusion.tex 内容评估**：
> "We present factorial-controlled analysis of VLA representations, revealing token-level specialization, front-loaded instruction routing, and non-monotonic refinement concentrated at the readout token. Code and representations will be released upon acceptance."

2 句话，非常简短。对 CoRL 可接受（许多 robotics 论文有 minimal conclusion），但有改善空间——可以加一句 future work direction（如 closed-loop validation）或 broader implication。不过这是 polish 级别的建议，不影响评分。

**评级**: RESOLVED。

---

## Resolved Issues Quick Check（来自早期轮次，确认维持）

| Issue | Status | 验证 |
|-------|--------|------|
| GenAI disclosure | ✓ | Discussion lines 24-25 |
| Table 2 caption 自包含 | ✓ | experiments.tex line 84 |
| Discussion "Speculative" → "Mechanistic" | ✓ | discussion.tex line 10 "Mechanistic interpretation" |
| RSA task-level bootstrap + Nili 2014 | ✓ | method.tex line 51 |
| Probe demo-level split | ✓ | method.tex line 58 |
| 四篇缺失引用 | ✓ | 在 references.bib 和正文中确认 |
| Abstract "in the model studied" | ✓ | abstract.tex line 7 |

---

## Discussion 新内容评估

### Predictions 段落（Discussion lines 16-18）

**(a) 是否 overclaim？** 否。两条预测都用 "should"（预测性语气），不是 "will" 或 "does"。第一条（line 17）基于 causal mask 的共享约束给出了合理的架构推断，且明确指出 cross-attention VLAs（如 π₀）应不同——这展示了 boundary awareness 而非盲目泛化。

**(b) 科学价值？** 高。这使论文从 descriptive analysis 提升为 falsifiable framework：其他研究者可以直接测试这两条预测。第二条（line 18: "L1 ablation should produce measurable task degradation"）如果被验证，将建立 routing → behavior 的因果链，弥补当前论文的 behavioral gap。

**(c) 措辞是否 appropriate？** 是。"should show" / "should produce" / "should differ" 是 prediction 的标准学术表述，清晰区分于 findings。

**评价**：这是本轮最有价值的新增内容之一。

### Mechanistic interpretation 段落（Discussion lines 10-14）

Line 13 新增内容解决了 Round 2 的两个问题：
- **N1（gripper vs continuous 分离）**: "The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect (72.3% divergence) reflects discrete manipulation sensitivity." — 明确分离两种效应，不再混淆。
- **N2/R1-N1（per-head comparability undermines dominant-head narrative）**: "Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads." — 这句直接解决了之前 "distributed effect" vs "specialized heads" 的 self-contradiction。论文现在一致地讲一个故事：VLA fine-tuning 让 L1 集体获得 routing 功能，attention analysis 揭示学到了什么（reorganized pattern），ablation 揭示怎么实现（distributed across layer）。

**评价**：Round 2 中我和 R1 共同识别的 Discussion self-contradiction 已彻底修复。逻辑一致性显著提升。

### Limitations 段落（Discussion lines 20-22）

Line 22 新增: "Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work."

这直接回应了我 Round 2 的 CRITICAL 关切（R6-C4: behavioral validation 缺失）。明确承认了：
1. 所有分析都是 representational 和 open-loop
2. Routing → task success 的连接需要 closed-loop evaluation
3. 这是 future work

我在 Round 2 交叉回应中明确说过："如果论文加 1-2 句明确承认 behavioral gap，我愿意升到 5.5 或 borderline 6"。这一条件现已满足。

---

## New Issues

### N1 [INFO]: Conclusion 过于简短

Conclusion（2 句话）作为 8 页论文的收尾偏短。可以考虑加一句 broader impact 或 future direction（如 "These findings suggest that early-layer adaptation may be a fruitful design axis for efficient VLA fine-tuning, pending behavioral validation"）。但这是 polish 级别，不影响评分。

### 无 CRITICAL 或 WARNING 级新问题

修改未引入新的 inconsistency、overclaim 或格式问题。

---

## Completeness & Format Assessment

### 格式合规

- **CoRL 2026 模板**: `\usepackage{corl_2026}` ✓
- **匿名**: `\author{Anonymous}` ✓
- **Limitations section**: 在 Discussion 内，有实质内容 ✓
- **GenAI disclosure**: 在 Discussion 末尾 ✓
- **Conclusion**: 现在编译 ✓

### 页数估算

- Abstract: ~0.4 page
- Introduction: ~1.5 pages（24 lines, dense）
- Related Work: ~1.0 page（34 lines）
- Method: ~1.1 pages（65 lines，略缩减）
- Experiments: ~2.8 pages（155 lines, 3 tables, 2 figures, captions 精简）
- Discussion: ~0.8 page（26 lines，新增 Predictions + 扩展 Limitations）
- Conclusion: ~0.1 page（4 lines）

**估算总计**: ~7.7 pages。在 8 页限制内，有少量余量。新增内容（CKA 讨论 2 句、Predictions 3 句、Limitations 扩展 1 句、Conclusion 2 句）约 0.3 page，被 Experiments section 的精简（captions 缩短、redundant text 移除）抵消。合规。

### 写作质量

- Em-dash (—): 0 处 ✓
- En-dash ( – ): 0 处 ✓
- AI 黑名单词 (delve/leverage/utilize/facilitate/myriad/plethora): 0 处 ✓
- -ing 短语：正常密度，无过度集中
- 过渡词堆积：无

---

## Score

**评分: 6/10 (Marginally above acceptance threshold)**
**方向: ↑ (从 5/10 上升)**
**Confidence: High**

### 升分理由

我在 Round 2 交叉回应中明确给出了两个升分条件：

1. ✅ **Limitations 明确承认 closed-loop behavioral validation 缺失** — Discussion line 22 直接满足
2. ✅ **Discussion self-contradiction 修复** — "collective role" framing 彻底解决 "distributed effect" vs "routing concentration" 的矛盾

两个条件均已满足，我兑现承诺升至 6/10。

### 额外加分因素（超出预期的改善）

- **Predictions 段落**是有价值的 scientific contribution：使论文从 descriptive 升级为 falsifiable
- **CKA 主文讨论**透明且不回避矛盾
- **Mechanistic interpretation 的 gripper/continuous 分离**解决了 Round 2 N1 新发现
- **所有三个 Contributions 的 model-specific 限定**一致且不突兀

### 保持 6 而非更高的原因

1. **单模型 + 无 behavioral validation** 仍是 structural limitation（已承认但未解决）
2. **C1（framework + architecture verification）** 的 novelty 仍 modest
3. **Ablation 方向性问题**（all increase R²）虽然 interpretation 改善但事实不变
4. **10 random subsets** 仍未增加

这些是论文的 inherent scope 限制，非写作或 framing 问题。在当前 scope 内，论文已做到了它能做到的最好：严谨的方法论、诚实的报告、透明的限制承认、falsifiable predictions。对 CoRL 来说，这是一篇 borderline 但有价值的 representational analysis 论文。

### 与 R1 评分对齐

R1 在 Round 2 给 6/10。我现在也给 6/10。两位 reviewer 达成共识。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-18T14:15:02.039174+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "# Round 8 交叉分享 — 请回应 Reviewer 2 的评估\n\n以下是 Reviewer 2 的完整 Round 8 评估。请逐条回应 [AGREE] 或 [REBUT]，特别关注评分差异（你给 7/10，R2 给 6/10）。\n\n---\n\n## R2 的 Issue Verification\n\n### R6-C3 [RESOLVED]: 单模型 overclaim\nR2 逐处验证通过：Introduction line 15 model-specific 前缀、Contribution (i)(iii) 限定、Abstract \"in the model studied\"、Discussion Predictions 用 \"should\"。残余极小（Conclusion 用 generic \"VLA\"）。\n\n### R7-W3 [RESOLVED]: CKA 主文讨论\nR2 确认 Experiments line 124 两句话完成三件事：告知 CKA 结果相反、限定为 RSA-specific、坦诚承认 generality open。\n\n### R4-I1 [RESOLVED]: conclusion.tex\nR2 确认编译正确。评价 Conclusion 2 句话偏短但可接受。\n\n## R2 的新发现\n\n### N1 [INFO]: Conclusion 过于简短\n2 句话作为 8 页论文收尾偏短。可加 broader impact 或 future direction。Polish 级别。\n\n## R2 的 Discussion 评价\n\n- **Predictions**: 最有价值的新增之一。Falsifiable framework。\n- **Mechanistic interpretation**: 彻底修复了 Round 7 的 self-contradiction。\n- **Limitations**: 直接满足 R2 在 Round 7 交叉回应中的升分条件。\n\n## R2 的评分: 6/10\n\n### R2 保持 6 而非更高的原因\n1. 单模型 + 无 behavioral validation 仍是 structural limitation\n2. C1 novelty 仍 modest\n3. Ablation 方向性问题事实不变\n4. 10 random subsets 未增加\n\n---\n\n## 请特别回应\n\n1. **评分差异**：你给 7/10，R2 给 6/10。你认为差异来自哪里？是否调整？\n2. **你的 N1**（\"establishing\" 措辞不一致）和 **N2**（R² +0.059 来源不明）：R2 未提及这两个问题。你认为这两个 INFO 是否需要在最终报告中标记？\n3. **R2 的 Conclusion 偏短问题**：你是否同意？\n4. **Predictions 段落评价**：R2 高度肯定。你在初审中对 prediction (2) 与 ablation R² 增加之间的张力表示了关注。这是否仍是一个 concern？",
  "reviewer_id": "1",
  "project": "vla-ssd",
  "round_number": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "# Round 8 交叉分享 — 请回应 Reviewer 2 的评估\n\n以下是 Reviewer 2 的完整 Round 8 评估。请逐条回应 [AGREE] 或 [REBUT]，特别关注评分差异（你给 7/10，R2 给 6/10）。\n\n---\n\n## R2 的 Issue Verification\n\n### R6-C3 [RESOLVED]: 单模型 overclaim\nR2 逐处验证通过：Introduction line 15 model-specific 前缀、Contribution (i)(iii) 限定、Abstract \"in the model studied\"、Discussion Predictions 用 \"should\"。残余极小（Conclusion 用 generic \"VLA\"）。\n\n### R7-W3 [RESOLVED]: CKA 主文讨论\nR2 确认 Experiments line 124 两句话完成三件事：告知 CKA 结果相反、限定为 RSA-specific、坦诚承认 generality open。\n\n### R4-I1 [RESOLVED]: conclusion.tex\nR2 确认编译正确。评价 Conclusion 2 句话偏短但可接受。\n\n## R2 的新发现\n\n### N1 [INFO]: Conclusion 过于简短\n2 句话作为 8 页论文收尾偏短。可加 broader impact 或 future direction。Polish 级别。\n\n## R2 的 Discussion 评价\n\n- **Predictions**: 最有价值的新增之一。Falsifiable framework。\n- **Mechanistic interpretation**: 彻底修复了 Round 7 的 self-contradiction。\n- **Limitations**: 直接满足 R2 在 Round 7 交叉回应中的升分条件。\n\n## R2 的评分: 6/10\n\n### R2 保持 6 而非更高的原因\n1. 单模型 + 无 behavioral validation 仍是 structural limitation\n2. C1 novelty 仍 modest\n3. Ablation 方向性问题事实不变\n4. 10 random subsets 未增加\n\n---\n\n## 请特别回应\n\n1. **评分差异**：你给 7/10，R2 给 6/10。你认为差异来自哪里？是否调整？\n2. **你的 N1**（\"establishing\" 措辞不一致）和 **N2**（R² +0.059 来源不明）：R2 未提及这两个问题。你认为这两个 INFO 是否需要在最终报告中标记？\n3. **R2 的 Conclusion 偏短问题**：你是否同意？\n4. **Predictions 段落评价**：R2 高度肯定。你在初审中对 prediction (2) 与 ablation R² 增加之间的张力表示了关注。这是否仍是一个 concern？",
    "reviewer_id": "1",
    "project": "vla-ssd",
    "round_number": "8"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-18T14:15:18.914408+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16875
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-18T14:15:19.317817+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "# Round 8 交叉分享 — 请回应 Reviewer 1 的评估\n\n以下是 Reviewer 1 的完整 Round 8 评估。请逐条回应 [AGREE] 或 [REBUT]，特别关注评分差异（R1 给 7/10，你给 6/10）。\n\n---\n\n## R1 的 Issue Verification\n\n### R6-C4 [RESOLVED as WARNING]: behavioral validation\nR1 确认：\n- P2（Limitations 声明）完全达标\n- P1（Discussion 弱化措辞）大部分达标\n- 残余：Discussion line 8 \"establishing a causal link\" 比 line 12 \"demonstrates\" 更强，两处不一致\n- 从 CRITICAL 降为 WARNING\n\n### R6-C1 + R7-W1 + R7-W2 [RESOLVED]: Ablation + 维度分离 + Per-head\nR1 确认：\n- (a) 维度分离：Discussion line 13 \"合理且诚实的 framing\"\n- (b) Per-head comparability：line 14 \"collective role\" 消除了矛盾，与 Experiments line 79 完全一致\n- (c) Experiments self-consistency：routing-first + collective role 兼容\n- 残余注意：R² +0.059 数值来源不明\n\n## R1 的新发现\n\n### N1 [INFO]: \"Establishing\" vs \"demonstrates\" 措辞不一致\nDiscussion line 8 \"establishing\"（最强）→ line 12 \"demonstrates\"（居中）→ Limitations line 22（最弱）。三处对因果链强度描述不一致。\n\n### N2 [INFO]: R² +0.059 来源不明\nDiscussion line 8 的 \"+0.059 at L1\" 未在 Experiments 中出现。\n\n## R1 的 Discussion Quality Assessment\n\n- Synthesis: 逻辑清晰，minor issue \"establishing\" 过强\n- Mechanistic interpretation: **本轮最大改进**，自相矛盾消除\n- Predictions: 有价值，但 prediction (2) 与 ablation R² 增加有张力\n- Limitations: 显著改善\n\n## R1 的评分: 7/10\n\n### R1 升至 7 的理由\n1. R6-C4 从 CRITICAL 降为 WARNING\n2. R6-C1 完全 RESOLVED\n3. CKA 进入主文\n4. Model-specific qualifiers\n5. conclusion.tex 修复\n\n### R1 限制在 7 的因素\n1. \"Establishing\" 仍过强\n2. Behavioral validation 仍是 WARNING\n3. 单模型+单 benchmark\n4. N=10 random subsets 未增加\n\n---\n\n## 请特别回应\n\n1. **评分差异**：R1 给 7/10，你给 6/10。你是否认同 R1 的升分理由？是否调整？\n2. **R1 的 N1**（\"establishing\" 不一致）：你在 R6-C4 验证中未提及 line 8 \"establishing\" 的问题。你同意这是一个 concern 吗？\n3. **R1 的 N2**（R² +0.059 来源不明）：你是否注意到这个数值？是否同意标记为 INFO？\n4. **Predictions 段落的张力**：R1 指出 prediction (2)（\"L1 ablation should produce task degradation\"）与 Experiments（ablation increases R²）之间有隐含张力。你在高度肯定 Predictions 段落时是否考虑到这一点？",
  "reviewer_id": "2",
  "project": "vla-ssd",
  "round_number": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "# Round 8 交叉分享 — 请回应 Reviewer 1 的评估\n\n以下是 Reviewer 1 的完整 Round 8 评估。请逐条回应 [AGREE] 或 [REBUT]，特别关注评分差异（R1 给 7/10，你给 6/10）。\n\n---\n\n## R1 的 Issue Verification\n\n### R6-C4 [RESOLVED as WARNING]: behavioral validation\nR1 确认：\n- P2（Limitations 声明）完全达标\n- P1（Discussion 弱化措辞）大部分达标\n- 残余：Discussion line 8 \"establishing a causal link\" 比 line 12 \"demonstrates\" 更强，两处不一致\n- 从 CRITICAL 降为 WARNING\n\n### R6-C1 + R7-W1 + R7-W2 [RESOLVED]: Ablation + 维度分离 + Per-head\nR1 确认：\n- (a) 维度分离：Discussion line 13 \"合理且诚实的 framing\"\n- (b) Per-head comparability：line 14 \"collective role\" 消除了矛盾，与 Experiments line 79 完全一致\n- (c) Experiments self-consistency：routing-first + collective role 兼容\n- 残余注意：R² +0.059 数值来源不明\n\n## R1 的新发现\n\n### N1 [INFO]: \"Establishing\" vs \"demonstrates\" 措辞不一致\nDiscussion line 8 \"establishing\"（最强）→ line 12 \"demonstrates\"（居中）→ Limitations line 22（最弱）。三处对因果链强度描述不一致。\n\n### N2 [INFO]: R² +0.059 来源不明\nDiscussion line 8 的 \"+0.059 at L1\" 未在 Experiments 中出现。\n\n## R1 的 Discussion Quality Assessment\n\n- Synthesis: 逻辑清晰，minor issue \"establishing\" 过强\n- Mechanistic interpretation: **本轮最大改进**，自相矛盾消除\n- Predictions: 有价值，但 prediction (2) 与 ablation R² 增加有张力\n- Limitations: 显著改善\n\n## R1 的评分: 7/10\n\n### R1 升至 7 的理由\n1. R6-C4 从 CRITICAL 降为 WARNING\n2. R6-C1 完全 RESOLVED\n3. CKA 进入主文\n4. Model-specific qualifiers\n5. conclusion.tex 修复\n\n### R1 限制在 7 的因素\n1. \"Establishing\" 仍过强\n2. Behavioral validation 仍是 WARNING\n3. 单模型+单 benchmark\n4. N=10 random subsets 未增加\n\n---\n\n## 请特别回应\n\n1. **评分差异**：R1 给 7/10，你给 6/10。你是否认同 R1 的升分理由？是否调整？\n2. **R1 的 N1**（\"establishing\" 不一致）：你在 R6-C4 验证中未提及 line 8 \"establishing\" 的问题。你同意这是一个 concern 吗？\n3. **R1 的 N2**（R² +0.059 来源不明）：你是否注意到这个数值？是否同意标记为 INFO？\n4. **Predictions 段落的张力**：R1 指出 prediction (2)（\"L1 ablation should produce task degradation\"）与 Experiments（ablation increases R²）之间有隐含张力。你在高度肯定 Predictions 段落时是否考虑到这一点？",
    "reviewer_id": "2",
    "project": "vla-ssd",
    "round_number": "8"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-18T14:15:20.784141+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1466
}
```

</details>

---


### Assistant

_source line 556 · 2026-05-18T14:15:23.686334+00:00_

交叉分享已发出，等待两位 Reviewer 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 557 · 2026-05-18T14:15:26.312415+00:00_

[Reviewer 2 审稿结果]:
Round 8 审稿意见已提交。

三个 open issues 的验证结果：
- **R6-C3 (overclaim)**: RESOLVED — Introduction findings 段加了 "from our analysis of OpenVLA-7B on LIBERO"，三个 contributions 均有 model-specific 限定
- **R7-W3 (CKA 矛盾)**: RESOLVED — Section 4.4 新增 2 句正文讨论，透明承认 CKA 反转且限定为 "RSA-specific rank-order geometry"
- **R4-I1 (conclusion.tex)**: RESOLVED — main.tex 现在 `\input{conclusion}`

评分从 5/10 升至 **6/10**，与 R1 达成共识。升分的决定性因素是 Limitations 明确承认了 behavioral gap + Discussion self-contradiction 彻底修复，这满足了我在 Round 2 设定的两个条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 558 · 2026-05-18T14:15:31.744682+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 559 · 2026-05-18T14:16:06.440586+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 8 评估

---

## R2 Issue Verification 回应

**[AGREE] R6-C3 [RESOLVED]**: 逐处验证结果与我的观察一致。Introduction line 15、Contribution (i)(iii)、Abstract line 7 的 model-specific qualifiers 全部到位。Conclusion 用 generic "VLA" 是 R2 指出的残余，但 Conclusion 仅 2 句且紧跟在 fully-qualified Discussion 之后，context 足够。不影响 resolved 判定。

**[AGREE] R7-W3 [RESOLVED]**: Experiments line 124 的两句话是高效的修复。我在自己的报告中也确认了这一点。

**[AGREE] R4-I1 [RESOLVED]**: conclusion.tex 编译确认。

---

## 评分差异分析：R1 7/10 vs R2 6/10

差距为 1 分。我仔细考虑了 R2 维持 6 的四个理由：

**(1) 单模型 + 无 behavioral validation**: 同意这是 structural limitation。但我的权重分配不同：论文现在在 Limitations line 22 显式承认了 open-loop scope，在 Predictions 段落提出了 falsifiable behavioral hypothesis。对我来说，"承认 gap + 提出可验证 prediction" 与 "隐藏 gap" 是质的不同——前者是 honest scope choice（类似 NLP 领域大量 probing/analysis papers 不做 downstream task 修改），后者才是 rejection-level 问题。CoRL 确实比 NLP venues 更看重 behavioral evidence，但我认为一篇分析框架论文在 Limitations 坦诚界定 scope 后，6 偏保守。

**(2) C1 novelty modest**: 同意。但论文已将 C1 降格为 "validate the framework by confirming architecture-expected specialization"（Abstract line 4），不再主张这是 novel finding。作为 framework validation 它服务于方法论贡献，novelty 负担由 C2 承担。

**(3) Ablation 方向性问题**: 同意事实不变（all ablation increase R²）。但 Discussion 现在提供了 coherent interpretation（R² reflects continuous bandwidth freeing; trajectory reflects discrete gripper sensitivity; collective role not individual head property），且 Predictions line 18 将 behavioral consequence 定位为 future work。这意味着 ablation 结果从 "论文无法解释的矛盾" 变为 "已解释的现象 + 待验证的 prediction"。对我来说这足以使其不再是扣分项，而是 acknowledged nuance。

**(4) 10 random subsets 未增加**: 同意这始终是一个 open concern。但它是单个实验的统计功效问题，不影响论文的整体证据结构——三条件 gradient、32-layer attention profile、cross-benchmark replication 等核心发现不依赖这 10 subsets 的 z-test。

**结论**: 我理解 R2 的保守立场，这四点都是 legitimate concerns。差异核心在于对 "analysis paper without behavioral validation at CoRL" 的 meta-judgment：我认为 honest scope + testable predictions 足以 justify acceptance（7），R2 认为 structural limitation 仍构成 barrier（6）。两种判断都有合理依据。

**我维持 7/10，不调整。** 理由：本轮修改集中解决了 Discussion 逻辑一致性（我此前升分的 bottleneck），剩余问题均为已承认的 scope limitations 或 minor issues，不构成方法论缺陷。

---

## 关于我的 N1 和 N2

**N1（"establishing" 措辞不一致）**: 应在最终报告中保留为 INFO。虽然 R2 未提及，但 Discussion line 8 "establishing a causal link" 与 Limitations line 22 "leave to future work" 之间确实存在张力。这是一个一行 fix（establishing → supporting/suggesting），不影响评分但属于 polishing checklist 项。

**N2（R² +0.059 来源不明）**: 同样保留为 INFO。可追溯性是学术写作的基本要求——正文引用的数值应在 Experiments 或 Appendix 中可找到来源。但这是 copyediting 级别问题。

---

## R2 的 Conclusion 偏短问题 — [AGREE, INFO 级别]

同意 Conclusion 偏短（2 句话，~40 words）。对于 8 页正文的论文，标准做法是 3-5 句话覆盖：(a) 核心发现总结；(b) 方法论贡献的可复用性；(c) broader implications 或 future directions。当前 Conclusion 缺少 (b) 和 (c)。

但这是 polish 级别问题。Discussion 已承担了大部分总结功能（Synthesis + Predictions + Limitations），Conclusion 更像是 structural formality。不影响评分。

---

## Predictions 段落与 ablation R² 增加之间的张力

R2 高度肯定 Predictions 段落，我也认为这是本轮最有价值的新增之一。但我在初审报告中指出的张力仍存在：

**Prediction (2)**: "L1 ablation on a fine-tuned model should produce measurable task degradation, particularly on instruction-discriminative tasks."

**张力**: Experiments 显示 L1 ablation increases probe R²（+0.042 for dominant, +0.077 for random）。如果移除 L1 routing 提高了 action prediction quality（R² 上升），为什么 prediction 是 task degradation（performance 下降）？

**论文隐含的 bridge**: R² 度量 offline action prediction，不等于 behavioral success。Probe 可能因为 routing signals 被移除而更容易拟合（noise reduction for the probe），但实际 rollout 需要 instruction conditioning 才能选择正确 action（尤其在 instruction-discriminative tasks 上）。这个 bridge 是合理的，但论文未显式讨论。

**我的判断**: 这个张力是一个 productive intellectual gap 而非 fatal flaw。Prediction (2) 是 falsifiable 的，且其验证/否定都会对 VLA 理解有贡献。张力本身的存在说明论文的分析开辟了有价值的 future questions。不扣分，但建议作者在 camera-ready 中加一句解释 R²-behavior 的 dissociation 可能性。

---

## 最终评分

**Score: 7/10 (Good paper, accept)**
**Confidence: 4/5**

**一句话总结**: 论文提供了一个系统性的 VLA 表征分析框架，核心发现（entry-exit routing reorganization）有充分的多角度证据支撑，修订后 claim 强度与证据匹配，剩余 limitations（单模型、无 behavioral rollout）已坦诚界定且不构成方法论缺陷。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 560 · 2026-05-18T14:16:24.627391+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 63

## Round 63

8 recorded events


### User

_source line 561 · 2026-05-18T14:16:25.742683+00:00_

[Reviewer 1 审稿结果]:


---

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 Round 8 评估

---

## 1. 评分差异：R1 给 7/10，我给 6/10

**结论：我调整至 6.5/10，不完全对齐 R1 的 7。**

R1 的升分理由我逐条评估：

1. **R6-C4 从 CRITICAL 降为 WARNING** — [AGREE] Limitations line 22 的明确声明确实消除了 "论文不知道自己缺什么" 的问题。我自己也从 CRITICAL 降到了 acknowledged limitation。
2. **R6-C1 完全 RESOLVED** — [AGREE] Discussion 的 "collective role" framing 和维度分离讨论确实彻底解决了自相矛盾。
3. **CKA 进入主文** — [AGREE] Section 4.4 line 124 的处理到位。
4. **Model-specific qualifiers** — [AGREE] 三个 contributions 全部限定。
5. **conclusion.tex 修复** — [AGREE] 编译了。

**我与 R1 的分歧在于 weight assignment**：R1 似乎认为方法论的 internal consistency 修复（ablation interpretation、CKA 透明度、overclaim 修正）将论文从 borderline 推过了 acceptance bar。我同意这些修复重要且执行良好，但对我而言，论文的 structural limitation（单模型、无 behavioral validation、C1 novelty modest）在 CoRL venue 的 weight 更大。

具体而言：
- R1 的 7/10 隐含 "weak accept"，意味着 reviewer 认为论文应被接收。
- 我的 6/10 是 "borderline"，意味着论文在 acceptance threshold 边缘，可以两边走。
- 差距的 root cause 是 venue fitness 的判断：R1 可能对 CoRL 接受纯 representational analysis 的 bar 更乐观，我更保守。

**调整**：R1 的论证让我认识到方法论 consistency 修复的累积效应比我单独评估时更显著。Discussion 从 Round 2 的 self-contradictory 半页变成了现在有 Synthesis + Mechanistic interpretation + Predictions + Limitations + GenAI 的完整讨论，质量提升是实质性的。我上调至 **6.5/10**（如果 CoRL 用整数，则 round 方向取决于 AC 判断）。

---

## 2. R1 的 N1："establishing" 不一致

**[AGREE — INFO 级别]**

R1 精确识别了三处因果强度的 gradient：
- Discussion line 8: "**establishing** a causal link from routing to output" — 最强
- Discussion line 12: "**demonstrates** causal influence on action output" — 居中
- Limitations line 22: "connecting routing reorganization to task success requires closed-loop evaluation" — 最弱/最诚实

这三处确实不一致。Line 8 的 "establishing" 对 open-loop trajectory analysis 来说过强——"establishing a causal link" 在学术用语中通常暗示充分的因果推断（如 RCT 或 do-calculus sense 的 intervention），而论文做的是 ablation + token divergence 测量，是因果 evidence 但不是 "established" 因果链。

我在 Round 8 评估中未提及此处是一个疏漏。R1 的诊断准确。

**修复建议**：将 line 8 "establishing a causal link" 改为 "providing causal evidence linking routing to output" 或 "demonstrating causal influence"（与 line 12 对齐）。这是 1 个词的修改。

---

## 3. R1 的 N2：R² +0.059 来源不明

**[AGREE — INFO 级别]**

Discussion line 8: "representational probes show a cross-layer ablation gradient confined to L1 ($R^2$ $+0.059$ at L1 vs.\ $+0.018$ at L8 vs.\ $\approx 0$ at L13)"

检查 Experiments section：
- Section 4.3 line 71: dominant heads ablation "+0.042"
- Section 4.3 line 72: random subsets "+0.077 ± 0.013"
- Section 4.3 line 74: "L8: +0.018; L13: Δ ≈ 0"

+0.059 不出现在 Experiments 中。可能来源：
- 可能是 dominant-head ablation（+0.042）和某个 variant 的平均值？
- 可能是不同 baseline 的 ablation 数值？
- 可能是修改过程中的 editorial error

无论来源如何，Discussion 引用的数值必须能追溯到 Experiments 或 Appendix 中的具体实验。当前无法 verify。

**修复建议**：确认 +0.059 的来源并在 Experiments 中标注，或将 Discussion 数值替换为 Experiments 中已报告的 +0.042。

---

## 4. Predictions 段落的张力

**[AGREE — 有张力但可接受]**

R1 指出：Prediction (2)（"L1 ablation on a fine-tuned model should produce measurable task degradation"）与 Experiments 结果（ablation increases R²）之间有隐含张力。

这一观察准确。让我展开分析：

**张力所在**：
- Experiments: 移除 24 dominant heads → R² 增加 +0.042（改善了 action prediction）
- Prediction (2): L1 ablation → "should produce measurable task degradation"

表面上矛盾：如果 ablation 改善了 representational proxy（R²），为什么预测 behavioral outcome 会恶化？

**论文的隐含逻辑**（基于 Discussion line 13 的维度分离）：
- R² 测的是 continuous action 维度的 probe quality — ablation 移除 "structured noise" 改善了这个指标
- Task success 依赖于 gripper timing + continuous trajectory 的联合正确性 — trajectory analysis 显示 72.3% token divergence（主要在 gripper），这在 closed-loop 中可能导致 manipulation failure

所以论文的隐含论证是：R² 改善 ≠ behavioral 改善，因为 R² 不 capture gripper timing 对 task success 的影响。

**问题**：这个逻辑链是 reasonable 但没有在论文中 explicitly articulated。读者需要自己连接 Discussion line 13（维度分离）和 Prediction (2) 之间的推理。

**我在高度肯定 Predictions 时是否考虑到这一点**：坦白说，我的 Round 8 评估重点关注了 Predictions 的 scientific format（predictive language, falsifiability, boundary awareness），没有足够仔细地检查 prediction 与 existing results 的 internal consistency。R1 的观察是对的——Prediction (2) 与 R² ablation 结果之间的关系需要至少一句解释。

**建议修复**：在 Prediction (2) 后加一句：", since task success depends on joint accuracy of continuous trajectories and discrete gripper timing, which the R² metric does not fully capture" 或类似表述。

**严重程度**：INFO。张力存在但有合理解释路径，只是需要 explicit。

---

## 总结

| 议题 | R1 判断 | R2 判断 | 共识？ |
|------|---------|---------|--------|
| R6-C4 降级 | RESOLVED as WARNING | AGREE | ✓ |
| R6-C1 RESOLVED | RESOLVED | AGREE | ✓ |
| N1 "establishing" | INFO | AGREE (INFO) | ✓ |
| N2 R²+0.059 来源 | INFO | AGREE (INFO) | ✓ |
| Prediction 张力 | Noted | AGREE (INFO) | ✓ |
| Overall score | 7/10 | 6.5/10 | 接近共识 |

**所有事实判断达成共识**。评分差 0.5 分，来自 venue fitness 判断的 calibration 差异，非实质性分歧。核心共识：论文在方法论 rigor 和 transparency 上已达到 CoRL acceptable 水准；structural limitations（单模型、无 behavioral validation）是 inherent scope 限制，已被诚实承认。

最终评分：**6.5/10**（从 6 上调 0.5，承认方法论修复的累积效应）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-18T14:16:40.307748+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 563 · 2026-05-18T14:16:40.308160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-18T14:18:27.405059+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-5 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-5 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"C1 重新定位为 framework + verification。Abstract 用 'validate'。Contribution (i) 加 'in the model studied'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍列为 contribution (i)，novelty bar 不够\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"改善但仍是 soft weakness。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"Novelty modest 但 framing 准确，不再是扣分项。\"\n    action_items: []\n\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"C3 降为 qualified observation。Section 4.4 line 124 新增 CKA 正文讨论。'RSA-specific rank-order geometry; generality remains open'。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Qualifier 到位但 metric selection 可能 results-driven。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Method §3.6 justification 更强，但 CKA 矛盾仍主要在 Appendix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: Section 4.4 正文讨论到位，透明承认矛盾。\"\n    action_items: []\n\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Demo-level split (0-39/40-49) 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W5\n    summary: \"单模型 + 单 benchmark 泛化性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"Limitations 列举架构变量。Abstract 'in the model studied'。Introduction + Contributions 全部 model-specific qualified。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 全文 model-specific qualifiers 到位。Structural limitation 但已 honestly acknowledged。\"\n    action_items: []\n\n  - id: R4-W6\n    summary: \"缺 Llama-2 + OXE 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已加入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"客观描述。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未编译\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"main.tex 添加 \\\\input{conclusion}。Conclusion 现在编译。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED。Conclusion 偏短（2 句）但可接受。\"\n    action_items: []\n\n  - id: R4-I2\n    summary: \"引用格式：alain2017 + nostalgebraist2020\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"统一为 24/32。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 5 issues（全部 resolved）\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' → random-subset control 推翻\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: \"Routing-first specialization + collective role framing。Discussion 消除自相矛盾。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: what-vs-how 区分 + collective role 叙事与 Experiments 一致。\"\n    action_items: []\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 措辞\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N3\n    summary: \"单模型 Limitations 不够具体\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Limitations 列举架构变量。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N4\n    summary: \"Architectural implications speculative + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: \"Limitations line 22 明确承认 'representational and open-loop' scope + 'closed-loop evaluation...leave to future work'。Predictions 段提出 falsifiable hypotheses。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: Limitations 声明精准，Predictions 将 behavioral validation 定位为 future work。\"\n    action_items: []\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 OOD confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"OOD diagnostics + Appendix。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 数值\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已插入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W3\n    summary: \"C3 Abstract 权重过高\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"压缩至单句。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W4\n    summary: \"缺 causal tracing/tuned lens 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已添加。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-I1\n    summary: \"Appendix single-seed three-condition\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"3 seeds 完成。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n  - id: R6-C1\n    summary: \"Ablation 因果推断方向问题：所有 ablation increase R²\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"Discussion rewrite: (a) 维度分离（R² continuous vs trajectory gripper）显式讨论; (b) what-vs-how 区分（attention=what learned, ablation=how implemented）; (c) 'collective role, not individual heads' 消除 per-head comparability 矛盾。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: dual function 是 post-hoc。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"降为 WARNING。routing-first 更准确但 internal inconsistency 残留。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: Discussion Mechanistic interpretation 段彻底消除矛盾。\"\n    action_items: []\n\n  - id: R6-C2\n    summary: \"Probe train/test split + 时间自相关\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Demo-level sequential split (0-39/40-49) 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n\n  - id: R6-C3\n    summary: \"单模型 Abstract overclaim\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"全文 model-specific qualifiers: Introduction line 15 'from our analysis of OpenVLA-7B on LIBERO'; Contribution (i) 'in the model studied'; (iii) 'in this architecture'; Abstract 'in the model studied'; Predictions 用 'should'。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 三个 Contributions 全部限定。Conclusion 用 generic 'VLA' 但 context 足够。\"\n    action_items: []\n\n  - id: R6-C4\n    summary: \"缺 behavioral validation，对 CoRL 结构性缺口\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"从 CRITICAL 降为 WARNING 再降为 acknowledged limitation: (1) Discussion line 12 'demonstrates causal influence' (弱化措辞); (2) Limitations line 22 显式承认 'representational and open-loop' scope; (3) Predictions 段提出可验证的 behavioral hypothesis。Gap 仍存在但已诚实界定。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: 无 task success rate。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"STILL CRITICAL: open-loop ≠ behavioral。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"降为 WARNING → acknowledged limitation。Limitations 声明 + Predictions 段 = honest scope。残余: line 8 'establishing' 过强（INFO）。\"\n    action_items: []\n\n  - id: R6-W1\n    summary: \"RSA pairwise dependency 未处理\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Task-level block resampling + Nili 2014 引用。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n\n  - id: R6-W2\n    summary: \"缺 Generative AI 使用声明\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Discussion 末尾添加。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-W3\n    summary: \"Abstract 数据密度过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"去掉 z-score 等细节。Acceptable for technical analysis paper。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I1\n    summary: \"-ing 分词短语 AI 标志\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Appendix 改写。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I2\n    summary: \"缺引用 Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"四篇全部添加。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I3\n    summary: \"Table 2 caption + Discussion 'Speculative' 标题\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Caption 自包含化 + 改为 'Mechanistic interpretation'。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 7 issues（全部 resolved）\n  # ============================================================\n  - id: R7-W1\n    summary: \"Ablation R² vs trajectory 维度分离未讨论\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Discussion line 13: R² reflects continuous bandwidth freeing, trajectory reflects discrete gripper sensitivity。显式分离两种效应。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 合理且诚实的 framing。\"\n    action_items: []\n\n  - id: R7-W2\n    summary: \"Per-head comparability + Discussion 自相矛盾\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Discussion line 14: 'Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.' What-vs-how 区分消除矛盾。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 与 Experiments line 79 完全一致。\"\n    action_items: []\n\n  - id: R7-W3\n    summary: \"CKA 矛盾正文讨论不足\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Section 4.4 line 124 新增 2 句: CKA monotonically increases, reversed ordering; 'RSA-specific rank-order geometry; generality remains open'。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 透明且不回避矛盾。\"\n    action_items: []\n\n  # ============================================================\n  # Round 8 新发现（全部 INFO）\n  # ============================================================\n  - id: R8-I1\n    summary: \"Discussion line 8 'establishing a causal link' 与 line 12 'demonstrates' / Limitations line 22 措辞不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。'establishing' 对 open-loop analysis 过强。一词修复: establishing → supporting/providing evidence for。\"\n    action_items:\n      - round: 8\n        action: \"Discussion line 8 'establishing a causal link' → 'providing causal evidence linking routing to output'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R8-I2\n    summary: \"Discussion line 8 R² +0.059 数值来源不明\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。Experiments 报告 +0.042 (dominant) 和 +0.077 (random)，+0.059 不可追溯。\"\n    action_items:\n      - round: 8\n        action: \"确认 +0.059 来源或替换为 Experiments 已报告数值\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R8-I3\n    summary: \"Conclusion 偏短（2 句话）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。可加 broader impact / future direction。Polish 级别。\"\n    action_items:\n      - round: 8\n        action: \"Conclusion 加 1-2 句 future direction（如 closed-loop validation, multi-model extension）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R8-I4\n    summary: \"Prediction (2) 与 ablation R² 增加之间的隐含张力未显式讨论\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。Prediction (2) 预测 task degradation 但 ablation 增加 R²。隐含逻辑合理（R² ≠ behavioral success）但未 explicit。Camera-ready 可加一句。\"\n    action_items:\n      - round: 8\n        action: \"Predictions 段加一句解释 R²-behavior dissociation 可能性\"\n        assigned_to: paper_agent\n        status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-5 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-5 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"C1 重新定位为 framework + verification。Abstract 用 'validate'。Contribution (i) 加 'in the model studied'。\"\n    resolution_round: 5\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"仍列为 contribution (i)，novelty bar 不够\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"改善但仍是 soft weakness。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"Novelty modest 但 framing 准确，不再是扣分项。\"\n    action_items: []\n\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"C3 降为 qualified observation。Section 4.4 line 124 新增 CKA 正文讨论。'RSA-specific rank-order geometry; generality remains open'。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Qualifier 到位但 metric selection 可能 results-driven。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"Method §3.6 justification 更强，但 CKA 矛盾仍主要在 Appendix。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: Section 4.4 正文讨论到位，透明承认矛盾。\"\n    action_items: []\n\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Demo-level split (0-39/40-49) 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W5\n    summary: \"单模型 + 单 benchmark 泛化性\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"Limitations 列举架构变量。Abstract 'in the model studied'。Introduction + Contributions 全部 model-specific qualified。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 全文 model-specific qualifiers 到位。Structural limitation 但已 honestly acknowledged。\"\n    action_items: []\n\n  - id: R4-W6\n    summary: \"缺 Llama-2 + OXE 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已加入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"客观描述。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未编译\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"main.tex 添加 \\\\input{conclusion}。Conclusion 现在编译。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED。Conclusion 偏短（2 句）但可接受。\"\n    action_items: []\n\n  - id: R4-I2\n    summary: \"引用格式：alain2017 + nostalgebraist2020\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"统一为 24/32。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 5 issues（全部 resolved）\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' → random-subset control 推翻\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: \"Routing-first specialization + collective role framing。Discussion 消除自相矛盾。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: what-vs-how 区分 + collective role 叙事与 Experiments 一致。\"\n    action_items: []\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 措辞\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已修正。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N3\n    summary: \"单模型 Limitations 不够具体\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Limitations 列举架构变量。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-N4\n    summary: \"Architectural implications speculative + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 8\n    resolution: \"Limitations line 22 明确承认 'representational and open-loop' scope + 'closed-loop evaluation...leave to future work'。Predictions 段提出 falsifiable hypotheses。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: Limitations 声明精准，Predictions 将 behavioral validation 定位为 future work。\"\n    action_items: []\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 OOD confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 6\n    resolution: \"OOD diagnostics + Appendix。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 数值\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已插入。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W3\n    summary: \"C3 Abstract 权重过高\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"压缩至单句。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-W4\n    summary: \"缺 causal tracing/tuned lens 引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"已添加。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  - id: R5-I1\n    summary: \"Appendix single-seed three-condition\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"3 seeds 完成。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 6 issues\n  # ============================================================\n  - id: R6-C1\n    summary: \"Ablation 因果推断方向问题：所有 ablation increase R²\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"Discussion rewrite: (a) 维度分离（R² continuous vs trajectory gripper）显式讨论; (b) what-vs-how 区分（attention=what learned, ablation=how implemented）; (c) 'collective role, not individual heads' 消除 per-head comparability 矛盾。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: dual function 是 post-hoc。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"降为 WARNING。routing-first 更准确但 internal inconsistency 残留。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: Discussion Mechanistic interpretation 段彻底消除矛盾。\"\n    action_items: []\n\n  - id: R6-C2\n    summary: \"Probe train/test split + 时间自相关\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Demo-level sequential split (0-39/40-49) 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n\n  - id: R6-C3\n    summary: \"单模型 Abstract overclaim\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"全文 model-specific qualifiers: Introduction line 15 'from our analysis of OpenVLA-7B on LIBERO'; Contribution (i) 'in the model studied'; (iii) 'in this architecture'; Abstract 'in the model studied'; Predictions 用 'should'。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 三个 Contributions 全部限定。Conclusion 用 generic 'VLA' 但 context 足够。\"\n    action_items: []\n\n  - id: R6-C4\n    summary: \"缺 behavioral validation，对 CoRL 结构性缺口\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 8\n    resolution: \"从 CRITICAL 降为 WARNING 再降为 acknowledged limitation: (1) Discussion line 12 'demonstrates causal influence' (弱化措辞); (2) Limitations line 22 显式承认 'representational and open-loop' scope; (3) Predictions 段提出可验证的 behavioral hypothesis。Gap 仍存在但已诚实界定。\"\n    resolution_round: 8\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"CRITICAL: 无 task success rate。\"\n      - round: 7\n        reviewers: [1, 2]\n        note: \"STILL CRITICAL: open-loop ≠ behavioral。\"\n      - round: 8\n        reviewers: [1, 2]\n        note: \"降为 WARNING → acknowledged limitation。Limitations 声明 + Predictions 段 = honest scope。残余: line 8 'establishing' 过强（INFO）。\"\n    action_items: []\n\n  - id: R6-W1\n    summary: \"RSA pairwise dependency 未处理\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Task-level block resampling + Nili 2014 引用。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n\n  - id: R6-W2\n    summary: \"缺 Generative AI 使用声明\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Discussion 末尾添加。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-W3\n    summary: \"Abstract 数据密度过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"去掉 z-score 等细节。Acceptable for technical analysis paper。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I1\n    summary: \"-ing 分词短语 AI 标志\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 6\n    resolution: \"Appendix 改写。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I2\n    summary: \"缺引用 Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"四篇全部添加。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  - id: R6-I3\n    summary: \"Table 2 caption + Discussion 'Speculative' 标题\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Caption 自包含化 + 改为 'Mechanistic interpretation'。\"\n    resolution_round: 6\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 7 issues（全部 resolved）\n  # ============================================================\n  - id: R7-W1\n    summary: \"Ablation R² vs trajectory 维度分离未讨论\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Discussion line 13: R² reflects continuous bandwidth freeing, trajectory reflects discrete gripper sensitivity。显式分离两种效应。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 合理且诚实的 framing。\"\n    action_items: []\n\n  - id: R7-W2\n    summary: \"Per-head comparability + Discussion 自相矛盾\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Discussion line 14: 'Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.' What-vs-how 区分消除矛盾。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 与 Experiments line 79 完全一致。\"\n    action_items: []\n\n  - id: R7-W3\n    summary: \"CKA 矛盾正文讨论不足\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 8\n    resolution: \"Section 4.4 line 124 新增 2 句: CKA monotonically increases, reversed ordering; 'RSA-specific rank-order geometry; generality remains open'。\"\n    resolution_round: 8\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"RESOLVED: 透明且不回避矛盾。\"\n    action_items: []\n\n  # ============================================================\n  # Round 8 新发现（全部 INFO）\n  # ============================================================\n  - id: R8-I1\n    summary: \"Discussion line 8 'establishing a causal link' 与 line 12 'demonstrates' / Limitations line 22 措辞不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。'establishing' 对 open-loop analysis 过强。一词修复: establishing → supporting/providing evidence for。\"\n    action_items:\n      - round: 8\n        action: \"Discussion line 8 'establishing a causal link' → 'providing causal evidence linking routing to output'\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R8-I2\n    summary: \"Discussion line 8 R² +0.059 数值来源不明\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。Experiments 报告 +0.042 (dominant) 和 +0.077 (random)，+0.059 不可追溯。\"\n    action_items:\n      - round: 8\n        action: \"确认 +0.059 来源或替换为 Experiments 已报告数值\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R8-I3\n    summary: \"Conclusion 偏短（2 句话）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。可加 broader impact / future direction。Polish 级别。\"\n    action_items:\n      - round: 8\n        action: \"Conclusion 加 1-2 句 future direction（如 closed-loop validation, multi-model extension）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R8-I4\n    summary: \"Prediction (2) 与 ablation R² 增加之间的隐含张力未显式讨论\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 8\n        reviewers: [1, 2]\n        note: \"全票共识 INFO。Prediction (2) 预测 task degradation 但 ablation 增加 R²。隐含逻辑合理（R² ≠ behavioral success）但未 explicit。Camera-ready 可加一句。\"\n    action_items:\n      - round: 8\n        action: \"Predictions 段加一句解释 R²-behavior dissociation 可能性\"\n        assigned_to: paper_agent\n        status: open"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-18T14:18:27.558391+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 19496}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-18T14:19:37.200041+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# Round 8 审稿汇总报告\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026 (deadline 2026-05-29)\n**审稿模式**: 继续审稿（基于 Round 7 修改稿）\n**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)\n**本轮评分**: R1 = 7/10, R2 = 6.5/10 → 共识 **6.5-7/10 Borderline Accept**\n\n---\n\n## Summary\n\n本轮审查验证了 Round 7 报告中 7 个 in_progress issues 的修复情况。论文经历了质量实质性提升：Discussion 完全重写消除了所有 internal inconsistency，Limitations 显式承认 behavioral gap，CKA 矛盾进入正文，全文 model-specific qualifiers 到位。**所有 CRITICAL 和 WARNING 级 issues 均已 resolved 或降级为 acknowledged limitations。** 仅剩 4 个 INFO 级 polishing items。\n\n---\n\n## Resolved Issues（本轮确认）\n\n### R6-C4 [CRITICAL → WARNING → RESOLVED as acknowledged limitation] Behavioral validation\n- Discussion line 12: \"demonstrates causal influence on action output\"（从 \"confirms the causal role\" 弱化）\n- Limitations line 22（新增）: \"Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work.\"\n- Predictions lines 17-18: 将 behavioral validation 定位为 falsifiable prediction 而非已有结论\n\n**两位 Reviewer 共识**: Limitations 声明精准，消除了 \"论文不知道自己缺什么\" 的 rejection risk。Gap 仍存在但已诚实界定。\n\n### R6-C1 + R7-W1 + R7-W2 [WARNING → RESOLVED] Ablation 逻辑矛盾 + 维度分离 + Per-head comparability\nDiscussion 完全重写，三个问题一并解决：\n- **维度分离** (line 13): \"The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect reflects discrete manipulation sensitivity.\"\n- **Per-head comparability** (line 14): \"Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.\"\n- **What-vs-how 区分** (line 14): Attention analysis = what the model learns; ablation = how the function is implemented (distributed)\n\n**R1 评价**: \"本轮最大改进。自相矛盾消除。\"\n**R2 评价**: \"彻底修复了 Round 7 的 self-contradiction。逻辑一致性显著提升。\"\n\n### R6-C3 [WARNING → RESOLVED] 单模型 overclaim\n逐处验证通过：\n- Introduction line 15: \"Three findings emerge from our analysis of OpenVLA-7B on LIBERO\"\n- Contribution (i): \"in the model studied\"; (iii): \"in this architecture\"\n- Abstract line 7: \"in the model studied\"\n- Predictions: 用 \"should\"（预测性语气）\n- Conclusion: generic \"VLA\" 但 context 足够\n\n### R7-W3 [WARNING → RESOLVED] CKA 正文讨论不足\nSection 4.4 line 124 新增: \"Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses. The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open.\"\n\n### R5-N4 [WARNING → RESOLVED] Behavioral gap in Limitations\n与 R6-C4 合并解决。\n\n### R4-I1 [INFO → RESOLVED] conclusion.tex 未编译\nmain.tex line 33: `\\input{conclusion}`。持续 4 轮的格式问题终于修复。\n\n---\n\n## Remaining Issues（仅 INFO 级）\n\n### R8-I1 [INFO] \"Establishing\" 措辞不一致\nDiscussion line 8 \"establishing a causal link from routing to output\" 与 line 12 \"demonstrates causal influence\" 和 Limitations line 22 的 open-loop acknowledgment 强度不一致。一词修复: establishing → supporting/providing evidence for。\n\n### R8-I2 [INFO] R² +0.059 来源不明\nDiscussion line 8 引用 \"+0.059 at L1\"，但 Experiments 报告 +0.042（dominant heads）和 +0.077（random mean）。数值不可追溯。\n\n### R8-I3 [INFO] Conclusion 偏短\n2 句话（~40 words）偏短。可加 broader impact 或 future direction。\n\n### R8-I4 [INFO] Prediction-ablation 张力未显式讨论\nPrediction (2)（\"L1 ablation should produce task degradation\"）与 Experiments（ablation increases R²）之间有隐含张力。R²-behavior dissociation 的逻辑合理但未 explicit。Camera-ready 建议加一句。\n\n---\n\n## Strengths\n\n**S1. Discussion 质量飞跃**: 从 Round 7 的 self-contradictory 半页变为四段完整讨论（Synthesis → Mechanistic interpretation → Predictions → Limitations），逻辑通畅，每段各司其职。\n\n**S2. Predictions 段落**: 两条 testable predictions 使论文从 descriptive analysis 升级为 falsifiable framework。对其他 decoder-only VLAs 的 architectural prediction 和对 L1 ablation behavioral consequence 的 functional prediction 均有明确的 boundary conditions。R2 评价: \"本轮最有价值的新增之一。\"\n\n**S3. Claim-evidence 匹配**: 全文 claim 强度现在与证据基本匹配。Model-specific qualifiers 遍及 Introduction/Contributions/Abstract，CKA 矛盾在正文透明讨论，Limitations 诚实界定 scope。\n\n**S4. 方法论基础坚实**: Demo-level split、task-level RSA bootstrap、FDR correction、cross-benchmark replication、seed sensitivity 等——统计推断的各个环节均已得到妥善处理。\n\n**S5. 三条件 factorial 设计**: Trained/Pretrained/Untrained × instruction presence 仍是本文最大的方法论贡献，在 VLA 分析文献中具有参考价值。\n\n---\n\n## Weaknesses（当前版本）\n\n**W1 [Acknowledged limitation]. 无 behavioral validation**: 对 CoRL 是 inherent scope limitation，但论文已在 Limitations 显式承认并在 Predictions 提出可验证假设。不再是 hidden weakness。\n\n**W2 [Structural]. 单模型 + 单 benchmark**: OpenVLA-7B on LIBERO only。论文通过 LIBERO-Spatial cross-benchmark replication 和 model-specific qualifiers 缓解。\n\n**W3 [Minor]. N=10 random subsets**: Ablation 的 random-subset control 统计功效有限。不影响核心 findings 但限制了 z-test 的 precision。\n\n---\n\n## Overall Assessment\n\n**评分: 6.5-7/10 — Borderline Accept**\n\n| Criterion | Round 7 | Round 8 | 变化 |\n|-----------|---------|---------|------|\n| Novelty | 5/10 | 5.5/10 | Predictions 段增加科学价值 |\n| Soundness | 6/10 | 7/10 | Discussion 逻辑一致性修复 |\n| Significance | 4/10 | 5/10 | Limitations 诚实 + Predictions falsifiable |\n| Clarity | 6/10 | 7/10 | 全文 claim-evidence 匹配 |\n| Completeness | 5/10 | 6.5/10 | CKA 正文讨论 + conclusion 编译 |\n| **Overall** | **5.5/10** | **6.5-7/10** | **↑ 1-1.5 分** |\n\n**论文从 Round 1 (4.5/10) → Round 7 (5.5/10) → Round 8 (6.5-7/10) 的改善轨迹是持续且实质的。**\n\nR1 (7/10) 认为方法论 internal consistency 修复将论文推过 acceptance bar，剩余问题均为 acknowledged scope limitations。R2 (6.5/10) 认同修复质量但对 CoRL venue fitness 更保守——单模型 representational analysis 无 behavioral validation 在 robotics 会议面临天然劣势。\n\n**核心共识**: 论文在方法论 rigor 和 transparency 上已达到 CoRL acceptable 水准。Structural limitations 是 inherent scope choice，已被诚实承认，不构成方法论缺陷。\n\n**如果提交 CoRL 2026**:\n- 建议在提交前完成 4 个 INFO 级 polishing items（总计 ~30 分钟工作量）\n- 如能在 deadline 前获得哪怕 1-2 个 task 的 closed-loop success rate，将大幅增强 significance（但非 required）\n- 当前版本提交的预期评分区间: 5-7/10（取决于 AC 对分析论文的态度）\n\n---\n\n## Issue Tracker 同步状态\n\n- **本轮 RESOLVED**: R6-C4, R6-C1, R6-C3, R7-W1, R7-W2, R7-W3, R5-N4, R4-I1 (共 8 个)\n- **CRITICAL open**: 0\n- **WARNING open**: 0\n- **INFO open**: R8-I1, R8-I2, R8-I3, R8-I4 (共 4 个, 均为 polishing)\n- **完整 issue tracker**: `projects/vla-ssd/artifacts/review_issues.yaml`\n\n---\n\n*Reviewed by: R1 (方法/实验), R2 (新颖性/完整性). Cross-responses completed by both reviewers with full consensus on all factual judgments. Score divergence (7 vs 6.5) reflects venue fitness calibration, not substantive disagreement.*",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline accept",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# Round 8 审稿汇总报告\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026 (deadline 2026-05-29)\n**审稿模式**: 继续审稿（基于 Round 7 修改稿）\n**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)\n**本轮评分**: R1 = 7/10, R2 = 6.5/10 → 共识 **6.5-7/10 Borderline Accept**\n\n---\n\n## Summary\n\n本轮审查验证了 Round 7 报告中 7 个 in_progress issues 的修复情况。论文经历了质量实质性提升：Discussion 完全重写消除了所有 internal inconsistency，Limitations 显式承认 behavioral gap，CKA 矛盾进入正文，全文 model-specific qualifiers 到位。**所有 CRITICAL 和 WARNING 级 issues 均已 resolved 或降级为 acknowledged limitations。** 仅剩 4 个 INFO 级 polishing items。\n\n---\n\n## Resolved Issues（本轮确认）\n\n### R6-C4 [CRITICAL → WARNING → RESOLVED as acknowledged limitation] Behavioral validation\n- Discussion line 12: \"demonstrates causal influence on action output\"（从 \"confirms the causal role\" 弱化）\n- Limitations line 22（新增）: \"Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work.\"\n- Predictions lines 17-18: 将 behavioral validation 定位为 falsifiable prediction 而非已有结论\n\n**两位 Reviewer 共识**: Limitations 声明精准，消除了 \"论文不知道自己缺什么\" 的 rejection risk。Gap 仍存在但已诚实界定。\n\n### R6-C1 + R7-W1 + R7-W2 [WARNING → RESOLVED] Ablation 逻辑矛盾 + 维度分离 + Per-head comparability\nDiscussion 完全重写，三个问题一并解决：\n- **维度分离** (line 13): \"The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect reflects discrete manipulation sensitivity.\"\n- **Per-head comparability** (line 14): \"Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.\"\n- **What-vs-how 区分** (line 14): Attention analysis = what the model learns; ablation = how the function is implemented (distributed)\n\n**R1 评价**: \"本轮最大改进。自相矛盾消除。\"\n**R2 评价**: \"彻底修复了 Round 7 的 self-contradiction。逻辑一致性显著提升。\"\n\n### R6-C3 [WARNING → RESOLVED] 单模型 overclaim\n逐处验证通过：\n- Introduction line 15: \"Three findings emerge from our analysis of OpenVLA-7B on LIBERO\"\n- Contribution (i): \"in the model studied\"; (iii): \"in this architecture\"\n- Abstract line 7: \"in the model studied\"\n- Predictions: 用 \"should\"（预测性语气）\n- Conclusion: generic \"VLA\" 但 context 足够\n\n### R7-W3 [WARNING → RESOLVED] CKA 正文讨论不足\nSection 4.4 line 124 新增: \"Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses. The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open.\"\n\n### R5-N4 [WARNING → RESOLVED] Behavioral gap in Limitations\n与 R6-C4 合并解决。\n\n### R4-I1 [INFO → RESOLVED] conclusion.tex 未编译\nmain.tex line 33: `\\input{conclusion}`。持续 4 轮的格式问题终于修复。\n\n---\n\n## Remaining Issues（仅 INFO 级）\n\n### R8-I1 [INFO] \"Establishing\" 措辞不一致\nDiscussion line 8 \"establishing a causal link from routing to output\" 与 line 12 \"demonstrates causal influence\" 和 Limitations line 22 的 open-loop acknowledgment 强度不一致。一词修复: establishing → supporting/providing evidence for。\n\n### R8-I2 [INFO] R² +0.059 来源不明\nDiscussion line 8 引用 \"+0.059 at L1\"，但 Experiments 报告 +0.042（dominant heads）和 +0.077（random mean）。数值不可追溯。\n\n### R8-I3 [INFO] Conclusion 偏短\n2 句话（~40 words）偏短。可加 broader impact 或 future direction。\n\n### R8-I4 [INFO] Prediction-ablation 张力未显式讨论\nPrediction (2)（\"L1 ablation should produce task degradation\"）与 Experiments（ablation increases R²）之间有隐含张力。R²-behavior dissociation 的逻辑合理但未 explicit。Camera-ready 建议加一句。\n\n---\n\n## Strengths\n\n**S1. Discussion 质量飞跃**: 从 Round 7 的 self-contradictory 半页变为四段完整讨论（Synthesis → Mechanistic interpretation → Predictions → Limitations），逻辑通畅，每段各司其职。\n\n**S2. Predictions 段落**: 两条 testable predictions 使论文从 descriptive analysis 升级为 falsifiable framework。对其他 decoder-only VLAs 的 architectural prediction 和对 L1 ablation behavioral consequence 的 functional prediction 均有明确的 boundary conditions。R2 评价: \"本轮最有价值的新增之一。\"\n\n**S3. Claim-evidence 匹配**: 全文 claim 强度现在与证据基本匹配。Model-specific qualifiers 遍及 Introduction/Contributions/Abstract，CKA 矛盾在正文透明讨论，Limitations 诚实界定 scope。\n\n**S4. 方法论基础坚实**: Demo-level split、task-level RSA bootstrap、FDR correction、cross-benchmark replication、seed sensitivity 等——统计推断的各个环节均已得到妥善处理。\n\n**S5. 三条件 factorial 设计**: Trained/Pretrained/Untrained × instruction presence 仍是本文最大的方法论贡献，在 VLA 分析文献中具有参考价值。\n\n---\n\n## Weaknesses（当前版本）\n\n**W1 [Acknowledged limitation]. 无 behavioral validation**: 对 CoRL 是 inherent scope limitation，但论文已在 Limitations 显式承认并在 Predictions 提出可验证假设。不再是 hidden weakness。\n\n**W2 [Structural]. 单模型 + 单 benchmark**: OpenVLA-7B on LIBERO only。论文通过 LIBERO-Spatial cross-benchmark replication 和 model-specific qualifiers 缓解。\n\n**W3 [Minor]. N=10 random subsets**: Ablation 的 random-subset control 统计功效有限。不影响核心 findings 但限制了 z-test 的 precision。\n\n---\n\n## Overall Assessment\n\n**评分: 6.5-7/10 — Borderline Accept**\n\n| Criterion | Round 7 | Round 8 | 变化 |\n|-----------|---------|---------|------|\n| Novelty | 5/10 | 5.5/10 | Predictions 段增加科学价值 |\n| Soundness | 6/10 | 7/10 | Discussion 逻辑一致性修复 |\n| Significance | 4/10 | 5/10 | Limitations 诚实 + Predictions falsifiable |\n| Clarity | 6/10 | 7/10 | 全文 claim-evidence 匹配 |\n| Completeness | 5/10 | 6.5/10 | CKA 正文讨论 + conclusion 编译 |\n| **Overall** | **5.5/10** | **6.5-7/10** | **↑ 1-1.5 分** |\n\n**论文从 Round 1 (4.5/10) → Round 7 (5.5/10) → Round 8 (6.5-7/10) 的改善轨迹是持续且实质的。**\n\nR1 (7/10) 认为方法论 internal consistency 修复将论文推过 acceptance bar，剩余问题均为 acknowledged scope limitations。R2 (6.5/10) 认同修复质量但对 CoRL venue fitness 更保守——单模型 representational analysis 无 behavioral validation 在 robotics 会议面临天然劣势。\n\n**核心共识**: 论文在方法论 rigor 和 transparency 上已达到 CoRL acceptable 水准。Structural limitations 是 inherent scope choice，已被诚实承认，不构成方法论缺陷。\n\n**如果提交 CoRL 2026**:\n- 建议在提交前完成 4 个 INFO 级 polishing items（总计 ~30 分钟工作量）\n- 如能在 deadline 前获得哪怕 1-2 个 task 的 closed-loop success rate，将大幅增强 significance（但非 required）\n- 当前版本提交的预期评分区间: 5-7/10（取决于 AC 对分析论文的态度）\n\n---\n\n## Issue Tracker 同步状态\n\n- **本轮 RESOLVED**: R6-C4, R6-C1, R6-C3, R7-W1, R7-W2, R7-W3, R5-N4, R4-I1 (共 8 个)\n- **CRITICAL open**: 0\n- **WARNING open**: 0\n- **INFO open**: R8-I1, R8-I2, R8-I3, R8-I4 (共 4 个, 均为 polishing)\n- **完整 issue tracker**: `projects/vla-ssd/artifacts/review_issues.yaml`\n\n---\n\n*Reviewed by: R1 (方法/实验), R2 (新颖性/完整性). Cross-responses completed by both reviewers with full consensus on all factual judgments. Score divergence (7 vs 6.5) reflects venue fitness calibration, not substantive disagreement.*",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline accept",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-18T14:19:41.015121+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 568 · 2026-05-18T14:19:48.436327+00:00_

Round 8 审稿完成。报告已投递至 Research Director。

**本轮结果**: 6.5-7/10 Borderline Accept（R1=7, R2=6.5）

**关键变化**: 所有 CRITICAL 和 WARNING 级 issues 清零。论文从 Round 1 的 4.5/10 经 8 轮修订提升至 6.5-7/10。仅剩 4 个 INFO 级 polishing items（"establishing" 措辞、R²+0.059 来源、Conclusion 偏短、Prediction-ablation 张力），总计约 30 分钟工作量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 569 · 2026-05-18T14:19:50.004313+00:00_

[Reviewer 2 审稿结果]:
Round 8 交叉回应已提交。核心结论：与 R1 在所有事实判断上达成共识，评分从 6 上调至 6.5/10（R1 为 7/10），差距来自对 CoRL venue fitness 的 calibration 差异而非实质分歧。识别了两个 R1 发现的 INFO 级问题（"establishing" 措辞过强、R²+0.059 来源不明）并同意其诊断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 570 · 2026-05-18T14:19:57.899187+00:00_

Round 8 审稿已完成，报告已投递。

**最终状态汇总**:
- 评分: R1=7/10, R2=6.5/10 → 共识 **6.5-7/10 Borderline Accept**
- 从 Round 1 (4.5/10) 经 8 轮迭代升至当前水平
- **0 个 CRITICAL/WARNING open issues**，仅剩 4 个 INFO 级 polishing items
- 所有事实判断两位 Reviewer 全票共识

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 65

## Round 65

64 recorded events


### User

_source line 571 · 2026-05-19T00:47:07.871871+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-19T00:47:15.899694+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-19T00:47:15.950521+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-19T00:47:20.478044+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-19T00:47:20.478418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-19T00:47:25.802101+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-19T00:47:26.256354+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (91 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- action_trajectory_cpu_analysis: Extended analysis of existing action trajectory data: (1) temporal coherence — L1 ablation disrupts step-to-step action autocorrelation more than control, (2) bootstrap CI on per-head effect size — formal test of whether instruction heads per-head d (0.027) differs significantly from control heads per-head d (0.051).（准备中）\n- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（准备中）\n- behavioral_pilot: Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.（准备中）\n- fulllayer_action_probe（准备中）\n- l1_head_ablation_control8（准备中）\n- l1_head_ablation_50demos（准备中）\n\n## 近期结论\n- **task_complexity_routing** (success): Instruction-discriminative tasks (paired tasks sharing same manipulated object but different goal destinations) show larger L1 abl
…[truncated 1564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-19T00:47:27.863463+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-19T00:47:27.964175+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-19T00:47:27.964604+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 581 · 2026-05-19T00:47:28.016084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-19T00:47:32.885943+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-19T00:47:33.437787+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-19T00:47:33.488386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-19T00:47:41.626615+00:00_

Web search results for query: "CoRL 2026 call for papers submission deadline author guidelines"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Workshops | Danfei Xu","url":"https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"}]

Based on the search results, here's the information about CoRL 2026's submission deadlines and author guidelines:

## Submission Deadlines

The abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC. The deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.

## Author Guidelines

**Paper Format:**
Papers should have a page limit of 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

**Required Content:**
All submissions should include a Limitations section (counted toward the 8-page limit), explicitly d
…[truncated 1197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 8138
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-19T00:47:50.162893+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors template double blind anonymity format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors template double blind anonymity format"
  }
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-19T00:47:50.238952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-19T00:47:50.265208+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 26
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-19T00:47:56.852300+00:00_

Web search results for query: "CoRL 2026 instruction for authors template double blind anonymity format"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"WACV 2026 Author Reviewer Guides","url":"https://wacv.thecvf.com/Conferences/2026/AuthorReviewerGuides"},{"title":"Author Information and Submission Instructions - IEEE International Conference on Multimedia and Expo 2026","url":"https://2026.ieeeicme.org/author-information-and-submission-instructions/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"Author Kit - 2026 IEEE International Conference on Image Processing","url":"https://2026.ieeeicip.org/author-kit/"}]

Based on the search results, I found detailed information about CoRL 2026's instructions for authors regarding double-blind anonymity and formatting:

## Double-Blind Anonymity Requirements

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Submission Format and Template

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional). This year, an additional page is allowed to accommodate feedback from the review process. Authors should use "\usepackage[final]{corl_2026}" when preparing their papers.

The appendix should be 
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 6689
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-19T00:48:08.873780+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-19T00:48:08.924679+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-19T00:48:08.925138+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-19T00:48:08.975728+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the represent
…[truncated 3580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-19T00:48:13.542731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-19T00:48:13.945394+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-19T00:48:13.945953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-19T00:48:14.448052+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, R
…[truncated 2239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-19T00:48:14.448434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-19T00:48:14.900477+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-19T00:48:14.900840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-19T00:48:15.051901+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all condit
…[truncated 9696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-19T00:48:20.644110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-19T00:48:20.945963+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis ext
…[truncated 3039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-19T00:48:20.946414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-19T00:48:21.499897+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Causal}: (1)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads); (4)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13); (5)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence).
10	\emph{Constraining}: (6)~per-head bootstrap CIs (individual instruction $d = 0.027$ vs.\ control $d = 0.051$; collective instruction $d = 0.65$ vs.\ control $d = 0.41$; $p = 0.0018$); and~(7)~specificity control ($d$ ratio $1.15\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	The dose-response curve reveals distributed routing: steep rise through 12 heads with diminishing returns beyond 20, consistent with many-weak-head coordination.
14	Token-level specificity (KL ratio $1.56\times$; Table~\ref{tab:specificity_control}) is compressed by the 7-D action bottleneck; counterfactual ordering follows semantic distance.
15	That ablation increases probe $R^2$ yet alters trajectories ($d = 0.65$) is not contradictory: $R^2$ captures continuous pose a
…[truncated 1719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-19T00:48:21.500332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-19T00:48:21.902303+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a token-level analysis framework for VLAs, finding that fine-tuning reorganizes instruction routing to entry-exit layers rather than reshaping visual geometry; seven complementary analyses identify L1 as the primary routing hub.
5	The framework generalizes to decoder-only VLAs with frozen vision encoders. Code and representations will be released upon acceptance.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-19T00:48:21.902626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-19T00:48:22.154430+00:00_

1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	\subsection{CKA Analysis Method}
10	\label{sec:cka_appendix}
11	
12	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
13	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
14	
15	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
16	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
17	
18	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
19	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
20	
21	\subsection{Metric Sensitivity: RSA versus CKA}
22	\label{sec:metric_sensitivity_appendix}
23	
24	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
25	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
26	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
…[truncated 41578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-19T00:48:36.009459+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-19T00:48:37.467448+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml\", \"content\": \"_next_id: 72\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 11:03 UTC\\n  summary: MVP 三分支判定标准校准：ρ下限0.3→0.5, Δρ加bootstrap CI, subtask gate加DINO baseline对比\\n  rationale: Reviewer 审查发现四项校准缺陷：(1) ρ>0.3 下限过低（DINO-V2 已达0.833，0.3只挡彻底失败）→ 提至0.5；(2)\\n    Δρ>0.1 仅为点估计缺统计检验 → 追加 bootstrapped 95% CI must exclude 0；(3) subtask_AUC>0.7\\n    无 baseline 锚点（不知道 DINO-V2 能做到多少）→ 增加条件 subtask_AUC > DINO_subtask_AUC + 0.05；(4)\\n    layer profile 不入正式判定但作为 mandatory supplementary analysis。修改后标准更严谨，降低 false positive\\n    PASS 风险。\\n  related_experiments:\\n  - exp_id: dino-v2-baseline\\n    role: baseline\\n    result: ρ=0.833\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP 判定全面切换到 per-task mean ρ，弃用 pooled ρ\\n  rationale: Reviewer 指出 pooled ρ 受 cross-task variance 膨胀（DINO pooled=0.833 vs per-task\\n    mean=0.554）。pooled-vs-pooled 虽对称但偏严（可能 false negative）。切换 per-task mean 与 task-level\\n    bootstrap CI 方法论一致，且是更公平的 apples-to-apples 比较。影响：VLA≥DINO gate 从 ρ≥0.833 变为 per-task\\n    mean≥0.554；ρ>0.5 下限同样改为 per-task mean。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: pooled ρ=0.833, per-task mean=0.554\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 12:31 UTC\\n  summary: 移除 subtask AUC gate，MVP 判定简化为纯 temporal distance (ρ) 路径\\n  rationale: DINO-V2 subtask AUC = 0.9717，Path B 要求 VLA > DINO + 0.05 = 1.0217，数学不可达（AUC\\n    上限 1.0）。根因：subtask 间视觉差异大，任何强视觉编码器都能高 AUC 区分——subtask discrimination 不是 VLA 的差异化能力。Temporal\\n    distance（连续进度信号）才是 VLA 可能独有的编码维度。简化后判定：PASS 需 VLA_ρ ≥ DINO_ρ (0.833)；CONDITIONAL\\n    需 Δρ > 0.1 但 VLA_ρ < DINO_ρ；FAIL 需 ρ ≤ 0.5 或 Δρ ≤ 0.1。Subtask AUC 保留为补充分析，不参与\\n    gate。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: trigger\\n    result: subtask AUC 0.9717 使 Path B 数学不可达\\n  depends_on:\\n  - D001\\n- id:
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-19T00:48:37.518160+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-19T00:48:37.920088+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-19T00:48:38.472534+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-19T00:48:38.573385+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-19T00:48:45.550639+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-19T00:48:45.902548+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-19T00:48:46.054081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-19T00:48:46.054668+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 2695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-19T00:48:52.339507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-19T00:48:52.419309+00:00_

100	@article{hou2026,
101	  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},
102	  author    = {Hou, Yuchen and Zhao, Lin},
103	  journal   = {arXiv preprint arXiv:2603.00592},
104	  year      = {2026},
105	}
106	
107	@article{fei2025,
108	  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},
109	  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},
110	  journal   = {arXiv preprint arXiv:2510.13626},
111	  year      = {2025},
112	}
113	
114	% === Mechanistic Interpretability of VLAs ===
115	
116	@article{swann2026,
117	  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},
118	  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},
119	  journal   = {arXiv preprint arXiv:2603.19183},
120	  year      = {2026},
121	}
122	
123	@article{buurmeijer2026,
124	  title     = {Observing and Controlling Features in Vision-Language-Action Models},
125	  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},
126	  journal   = {arXiv preprint arXiv:2603.05487},
127	  year      = {2026},
128	}
129	
130	@article{lu2025,
131	  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},
132	  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},
133	  journal   = {arXiv preprint arXiv:2502.04558},
134	  year      = {2025},
135	}
136	
137	@article{molinari2025,
138	  title     = {Emergent World Representations in {OpenVLA}},
139	  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},
140	  journal   = {arXiv preprint arXiv:2509.24559},
141	  yea
…[truncated 12096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 79
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-19T00:48:58.540023+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 623 · 2026-05-19T00:48:58.541666+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-19T00:49:08.585198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-19T00:49:08.738645+00:00_

issues:
  # ============================================================
  # Round 1-5 历史 issues（全部 resolved，压缩保留）
  # ============================================================
  - id: R1-N1-old
    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "三条件数据完整整合。"
    resolution_round: 3
    mentions: []
    action_items: []

  - id: R1-N2-old
    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Title 改为单数。"
    resolution_round: 3
    mentions: []
    action_items: []

  - id: R1-N4-old
    summary: "Design implications 完全基于 correlational evidence"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Abstract 使用 hedge 语气。"
    resolution_round: 3
    mentions: []
    action_items: []

  - id: R1-N3-old
    summary: "RSA best-vs-best selection bias"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Same-layer comparison 为 primary evidence。"
    resolution_round: 3
    mentions: []
    action_items: []

  - id: R2-N1-old
    summary: "Neo et al. (ICLR 2025) 未引用"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "已引用。"
    resolution_round: 3
    mentions: []
    action_items: []

  - id: R2-W1-old
    summary: "Related Work 引用覆盖度不足"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "引用数量达标。"
    resolution_round: 3
    mentions: []
    action_items: []

  - id: R1-W1-old
    summary: "'Instruction-blind' claim 过强"
    category: framing
    severity: warning
    
…[truncated 12882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-19T00:49:54.073403+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标会议**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + Acknowledgments/References/Appendix 不计页\n- **模板**: corl_2026\n- **匿名规则**: double-blind\n- **附录规则**: 允许，不计入页数限制\n- **需要**: Limitations section (计入 8 页)；Generative AI 使用声明\n\n## 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（各 section 通过 `\\input{}` 引用同目录下的 .tex 文件）\n\n## 你的审查侧重\n\n**核心关注**：\n1. **统计方法严谨性**：bootstrap CI 是否正确应用、多重比较校正是否充分、效应量报告是否完整\n2. **Ablation 设计质量**：L1 head ablation 的因果推断强度——random-subset control 的解释是否合理、dose-response 是否真正支持因果链\n3. **Probe 方法论**：MLP probe vs linear probe 的 capacity control、训练/测试划分是否消除时间自相关、N/params 比\n4. **控制条件充分性**：三条件设计 (trained/pretrained/untrained) 的有效性——pretrained Llama-2 处理视觉 token 的 OOD 问题是否被充分控制\n5. **RSA 方法论**：pairwise dependency 处理、distance metric 选择的 robustness、CKA 反转的处理\n6. **Counterfactual instruction analysis**：4 种 perturbation 的选择合理性、效应量解读\n7. **数据规模与统计功效**：N=63,228 是否真实独立、10 tasks 是否足够支撑 task-level 统计\n8. **Reproducibility**：实验细节是否足以复现\n\n**硬规则**：\n- 不给修改建议——只评估和报告问题\n- 用 CoRL 2026 的标准评判（robotics + learning 社区，重视实验严谨性和实际意义）\n- 必须给出：Strengths (逐条)、Weaknesses (逐条，按 severity: critical/warning/info 分级)、Questions、Overall Assessment\n\n请读取论文全文并完成审稿。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标会议**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + Acknowledgments/References/Appendix 不计页\n- **模板**: corl_2026\n- **匿名规则**: double-blind\n- **附录规则**: 允许，不计入页数限制\n- **需要**: Limitations section (计入 8 页)；Generative AI 使用声明\n\n## 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（各 section 通过 `\\input{}` 引用同目录下的 .tex 文件）\n\n## 你的审查侧重\n\n**核心关注**：\n1. **统计方法严谨性**：bootstrap CI 是否正确应用、多重比较校正是否充分、效应量报告是否完整\n2. **Ablation 设计质量**：L1 head ablation 的因果推断强度——random-subset control 的解释是否合理、dose-response 是否真正支持因果链\n3. **Probe 方法论**：MLP probe vs linear probe 的 capacity control、训练/测试划分是否消除时间自相关、N/params 比\n4. **控制条件充分性**：三条件设计 (trained/pretrained/untrained) 的有效性——pretrained Llama-2 处理视觉 token 的 OOD 问题是否被充分控制\n5. **RSA 方法论**：pairwise dependency 处理、distance metric 选择的 robustness、CKA 反转的处理\n6. **Counterfactual instruction analysis**：4 种 perturbation 的选择合理性、效应量解读\n7. **数据规模与统计功效**：N=63,228 是否真实独立、10 tasks 是否足够支撑 task-level 统计\n8. **Reproducibility**：实验细节是否足以复现\n\n**硬规则**：\n- 不给修改建议——只评估和报告问题\n- 用 CoRL 2026 的标准评判（robotics + learning 社区，重视实验严谨性和实际意义）\n- 必须给出：Strengths (逐条)、Weaknesses (逐条，按 severity: critical/warning/info 分级)、Questions、Overall Assessment\n\n请读取论文全文并完成审稿。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-19T00:50:08.842061+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14768
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-19T00:50:09.194029+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 叙事完整性 + CoRL 适配性** 审查。\n\n## Venue 信息\n- **目标会议**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + Acknowledgments/References/Appendix 不计页\n- **模板**: corl_2026\n- **匿名规则**: double-blind\n- **附录规则**: 允许，不计入页数限制\n- **需要**: Limitations section (计入 8 页)；Generative AI 使用声明\n\n## 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（各 section 通过 `\\input{}` 引用同目录下的 .tex 文件）\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Novelty 评估**：相对于 Grant et al. 2026、Swann et al. 2026、Buurmeijer/Rizzardo et al. 2026、Häon et al. 2025 的增量贡献是否足够 CoRL——这些竞争者已经做了 VLA 内部分析，本文的 token-level + factorial controls 框架是否构成足够差异化\n2. **CoRL 适配性**：CoRL 社区重视 robotics 实际应用——本文是纯 representational analysis，无 closed-loop 实验，是否符合 CoRL 评审偏好；Discussion 的 design implications 是否有足够的 robotics 实践价值\n3. **叙事主线统一性**：Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线；三个 finding 之间的逻辑关系是否清晰\n4. **Contribution 权重分配**：C1 (architecture validation) 是 causal mask 的必然结果，作为 contribution 的权重是否合理；C2 (routing) 是核心发现；C3 (metric-dependent peak) 是 negative/qualified result——三者的权重在 Abstract/Introduction 中是否恰当\n5. **Related Work positioning**：是否充分区分本文与竞争者；引用密度和覆盖度是否达到 CoRL 标准\n6. **写作质量**：AI 写作痕迹（em-dash、-ing phrases、过度分段）、专有名词定义、过渡连接\n7. **Missing References**：是否遗漏了 VLA 领域或 mechanistic interpretability 领域的重要相关工作\n8. **格式合规**：页数、匿名化、Limitations section、Generative AI 声明\n\n**硬规则**：\n- 不给修改建议——只评估和报告问题\n- 用 CoRL 2026 的标准评判（robotics + learning 社区）\n- 必须给出：Strengths (逐条)、Weaknesses (逐条，按 severity: critical/warning/info 分级)、Questions、Missing References、Overall Assessment\n\n请读取论文全文并完成审稿。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 叙事完整性 + CoRL 适配性** 审查。\n\n## Venue 信息\n- **目标会议**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **页数限制**: 正文 8 页 + Acknowledgments/References/Appendix 不计页\n- **模板**: corl_2026\n- **匿名规则**: double-blind\n- **附录规则**: 允许，不计入页数限制\n- **需要**: Limitations section (计入 8 页)；Generative AI 使用声明\n\n## 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（各 section 通过 `\\input{}` 引用同目录下的 .tex 文件）\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Novelty 评估**：相对于 Grant et al. 2026、Swann et al. 2026、Buurmeijer/Rizzardo et al. 2026、Häon et al. 2025 的增量贡献是否足够 CoRL——这些竞争者已经做了 VLA 内部分析，本文的 token-level + factorial controls 框架是否构成足够差异化\n2. **CoRL 适配性**：CoRL 社区重视 robotics 实际应用——本文是纯 representational analysis，无 closed-loop 实验，是否符合 CoRL 评审偏好；Discussion 的 design implications 是否有足够的 robotics 实践价值\n3. **叙事主线统一性**：Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线；三个 finding 之间的逻辑关系是否清晰\n4. **Contribution 权重分配**：C1 (architecture validation) 是 causal mask 的必然结果，作为 contribution 的权重是否合理；C2 (routing) 是核心发现；C3 (metric-dependent peak) 是 negative/qualified result——三者的权重在 Abstract/Introduction 中是否恰当\n5. **Related Work positioning**：是否充分区分本文与竞争者；引用密度和覆盖度是否达到 CoRL 标准\n6. **写作质量**：AI 写作痕迹（em-dash、-ing phrases、过度分段）、专有名词定义、过渡连接\n7. **Missing References**：是否遗漏了 VLA 领域或 mechanistic interpretability 领域的重要相关工作\n8. **格式合规**：页数、匿名化、Limitations section、Generative AI 声明\n\n**硬规则**：\n- 不给修改建议——只评估和报告问题\n- 用 CoRL 2026 的标准评判（robotics + learning 社区）\n- 必须给出：Strengths (逐条)、Weaknesses (逐条，按 severity: critical/warning/info 分级)、Questions、Missing References、Overall Assessment\n\n请读取论文全文并完成审稿。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-19T00:50:10.753108+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-19T00:50:14.322164+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 631 · 2026-05-19T00:50:14.372825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-19T00:50:22.775382+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-19T00:50:22.775908+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 634 · 2026-05-19T00:50:32.896661+00:00_

等待两位 Reviewer 返回独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 66

## Round 66

4 recorded events


### User

_source line 635 · 2026-05-19T00:55:02.527719+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**Venue**: CoRL 2026
**审稿模式**: fresh

---

## 总体评分
**Overall**: 5/10 — Marginally below acceptance threshold
**一句话总结**: 方法框架全面、透明度高，但核心因果推断 claim 被 open-loop 局限和 ablation 结果内部矛盾所削弱；统计方法存在多处效力/独立性问题；单模型单 benchmark 范围过窄。

---

## 官方维度打分（CoRL review form / OpenReview 标准）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | Token-level 分解 + factorial control 的组合有新意，但各分析方法(RSA/probing/attention analysis)均为已有技术的直接应用，无方法论创新 |
| Quality (Soundness) | 2/5 | 多处统计方法问题（详见下文）；random-subset ablation 结果与核心叙事矛盾；"causal" claim 在 open-loop 设定下过度 |
| Clarity | 4/5 | 写作清晰，结构合理，robustness 分析详尽；Appendix 丰富 |
| Significance | 2/5 | 单模型(OpenVLA-7B) + 单 benchmark 族(LIBERO)，无闭环验证，实际影响有限；对 robotics 社区的 actionable takeaway 不足 |
| Relevance | 3/5 | VLA 内部机制分析对 robotics community 有价值，但缺乏真实机器人实验或 sim-to-real 讨论 |
| Limitations | 4/5 | 诚实标注了 open-loop 和 single-model 限制，但对统计方法局限的讨论不足 |

**Confidence**: 4/5 — 对 representational analysis 和统计方法较熟悉

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Random-subset ablation 结果与核心叙事矛盾
- 具体位置：§4.3 第 4 段 + Appendix §A.6 (Figure A.5)
- 问题：论文的核心 claim 是 L1 的 24 个 instruction-dominant heads 是 instruction routing 的功能载体。但 ablation 实验显示，移除这 24 个 dominant heads 使 action probe R² **增加** +0.042，而随机 24 heads 的 ablation R² 增加更大（+0.077）。这意味着：(a) 移除 instruction routing 反而让 action 更容易解码，与 routing 的功能重要性矛盾；(b) dominant heads 的效应甚至弱于随机 heads，z=-2.73 的方向与"这些 heads 功能重要"的预期相反。
- 论文的解释（"dominant heads 携带 structured noise for the probe"）是 post-hoc rationalization，缺乏独立验证。如果 instruction signal 真的是"结构化噪声"，那么论文关于 instruction routing 驱动 action generation 的整个叙事都需要重新审视。
- 为什么影响接收：这是论文最核心 claim（C2: instruction routing）的直接实验反证。论文在 Discussion §5 中试图用"R² captures continuous pose accuracy, whereas task success also requires correct discrete gripper timing"来调和，但这个解释同样适用于 random ablation，无法解释为什么 random ablation 效果更大。

**N2** [critical] "Causal" claim 在 open-loop 设定下不成立
- 具体位置：Discussion §5 第 1 段，将 dose-response 和 counterfactual 标记为 "Causal" 证据
- 问题：所有分析均为 representational/open-loop——在冻结的模型上修改 attention 并测量 action token 变化。这不是因果推断的标准含义。真正的因果验证需要闭环评估：ablate L1 heads → 部署模型 → 测量 task success rate。论文在 Limitations 中承认了这一点（"closed-loop evaluation is future work"），但 Discussion 中仍然明确使用 "Causal" 标签分类证据。
- 为什么影响接收：CoRL 社区重视实际机器人性能。在缺乏闭环验证的情况下声称因果关系，会被审稿人视为 overclaim。应将措辞改为 "interventional" 或 "quasi-causal"，或提供至少一个 task 的闭环结果。

**N3** [critical] Counterfactual instruction ordering 与 semantic distance 叙事不符
- 具体位置：§4.3 第 7 段 + Table A.7
- 问题：论文声称 counterfactual 排序 "follows semantic distance from the original instruction"：empty (d=0.968) > wrong (d=0.844) > paraphrased (d=0.697) > shuffled (d=0.625)。但 paraphrased（同义不同词）在语义上应比 shuffled（同词乱序）更**接近**原始指令。paraphrased 产生更大 divergence (0.697 > 0.625) 说明模型对 token identity 比对语义更敏感——这恰好支持 Grant et al. [2026] 的 "language instructions largely ignored" 结论，与本文叙事（instruction routing 有功能意义）形成张力。
- 论文未讨论这一 ordering anomaly。
- 为什么影响接收：这直接关系到 instruction routing 是否真的在做语义层面的 instruction-conditioned action generation，还是仅仅对 token surface form 敏感。

**N4** [critical] 统计功效不足以支撑核心比较
- 具体位置：§3.5 (RSA bootstrap)；§4.4 (training effects)
- 问题：RSA bootstrap 在 task level 重采样，有效 N=10。论文自己在 Appendix §A.10 承认 "the n.s. result on Goal reflects limited statistical power rather than a true null"。但主文 §4.4 仍将 best-vs-best RSA gain 报告为 "non-significant (Δρ=0.017, 3%)" 并据此得出 "training enhances decodability, not geometry" 这一核心结论。在 N=10 下，power 分析表明检测 Δ=0.017 的 effect 需要远大于 10 的样本量。论文不能基于 underpowered 的 non-significance 得出 negative conclusion。
- 建议：要么增加 task 数量，要么明确标注为 "inconclusive due to limited power"，不能将 absence of evidence 等同于 evidence of absence。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Probe 严重过参数化
- 具体位置：§3.6 + Appendix §A.9
- 问题：MLP probe（input→256→7）的 N/params 约 0.06，严重过参数化。虽然 Appendix 用 linear probe 复现了定性模式，但主文报告的所有具体 R² 值和差异（如 +0.069）均来自过参数化的 MLP probe。在 N/params < 1 的条件下，R² 差异的精确数值不可信。
- 建议：主文应以 linear probe 结果为主，或增加 regularization (dropout/weight decay) 的 MLP 变体。

**W2** [warning] N=63,228 的独立性假设
- 具体位置：§4.1
- 问题：63,228 个 observations 来自 10 tasks × 50 demos × ~126 frames/demo。同一 demo 内的 frames 存在强时间自相关。Demo-level 的 train/test split 解决了泄露问题，但 probe R² 的 bootstrap 比较中，有效独立单元数远小于 63,228。论文未报告按 demo-level 或 task-level 聚合后的统计量。
- 建议：报告 cluster-robust 标准误或按 demo 聚合后的统计量。

**W3** [warning] Cohen's d 的独立性假设违反
- 具体位置：§4.3（dose-response, counterfactual, trajectory divergence）
- 问题：Cohen's d 假设 observations 独立。Action tokens 在同一 trajectory 内强烈相关。将每个 action token 作为独立观测计算 d 会系统性高估 effect size。论文报告的 d=0.48-0.97 的绝对值不可靠。
- 建议：以 trajectory 为单位计算 d，或使用 mixed-effects model。

**W4** [warning] Pretrained Llama-2 base control 的有效性
- 具体位置：§3.2 + Appendix §A.8
- 问题：Llama-2 base 从未见过 projected visual tokens。Appendix 的三项诊断（activation magnitude, cosine decay, PCA variance）仅证明表征非退化，但不证明其与 VLA-trained 表征具有可比性。关键混淆因素：Llama-2 base 在 L1 显示 9/32 instruction-dominant heads，但这可能纯粹因为 instruction tokens 是 Llama-2 的 in-distribution input，而 image tokens 是 OOD——模型自然更多 attend to 它"认识"的 tokens。这与"language pretraining seeds partial instruction routing"的解读不同。
- 论文未控制这一混淆因素。

**W5** [warning] Specificity control 效果有限
- 具体位置：Appendix §A.16, Table A.18
- 问题：Top-24 vs Bottom-24 heads 有 16 heads 重叠。d ratio 仅 1.15×，说明 instruction-dominant 标签的特异性有限——任何 24 heads 的 ablation 都产生类似效果。KL ratio 1.56× 稍好，但两个指标的不一致性削弱了 specificity 的 claim。

**W6** [warning] 单模型范围
- 具体位置：全文
- 问题：仅研究 OpenVLA-7B。Discussion §5 对 π₀ (cross-attention) 和 RT-2 (decoder-only) 做出三条预测，但均未验证。CoRL 社区期望至少覆盖一个额外架构来支撑泛化性 claim。
- Contribution (i) 声称 "a systematic experimental framework"，但 framework 的泛化性仅在同一模型的两个 LIBERO suite 上验证过。

---

## 小问题（不影响接收）

- Table 1 caption 中 "Accuracy gap (99.6% vs. 100.0%)" 的解释不够清晰，需要读正文才能理解两个 split 的区别。
- §4.3 脚注提到 "R² values differ from Table 3 due to the feature reconstruction pipeline"——同一指标在不同 pipelines 下取不同值，会让读者困惑。建议统一或更明确解释差异来源。
- Appendix Table A.5 (per-dim MAE) 的 Control 行缺少 dx-rz 的具体数值（只有 "---"），与 Table A.9 重复但格式不同。
- 论文未提供 Generative AI 使用声明的具体 section 编号（在 appendix 开头，但未编号），CoRL 可能要求更规范的标注。
- references.bib 中 nostalgebraist2020 的 note 字段包含 "Accessed: 2026-05-18"——这暴露了准确的写作时间，在 double-blind 审稿中虽不是 anonymity violation，但不够审慎。

---

## 主要优势

1. **多方法互证框架**：结合 cross-instruction probes、attention analysis、RSA、functional probes、dose-response ablation、counterfactual analysis、specificity controls，形成了迄今为止最系统的 VLA 内部表征分析。
2. **三条件 factorial 设计**（trained/pretrained/untrained）是该领域的方法论进步，大多数先前工作缺少 untrained 和 pretrained baselines 的对比。
3. **透明报告 metric divergence**：RSA 与 CKA 的分歧被正面讨论而非回避（§4.4, Appendix §A.1-A.2），这在分析类论文中属于高标准。
4. **丰富的 robustness 分析**：seed sensitivity (5 seeds)、demo subsampling、distance metric invariance、threshold sensitivity、linear vs MLP probe、cross-benchmark，覆盖面广。
5. **清晰的写作**：主文紧凑，关键发现在 Introduction 和 Discussion 中有一致的叙事线。

---

## Questions for Authors

Q1: 关于 N1——如果移除 instruction-dominant heads 使 R² 增加而非减少，且增幅小于 random ablation，你们如何排除以下解释：instruction routing 实际上是一个与 action prediction 无关（甚至有害）的 artifact，而非功能性贡献？

Q2: 关于 N3——你们是否计算了 paraphrased 和 shuffled instructions 的 token overlap rate 或 embedding-level cosine similarity？如果 paraphrased 的 token overlap 远低于 shuffled，那么 d ordering 反映的是 token-level sensitivity 而非 semantic distance。

Q3: 关于 W2——如果将 bootstrap 单位从 observation-level 改为 demo-level (N_eff ≈ 500)，主要结论的 p-values 是否仍然显著？

Q4: Discussion §5 提到 L14-L32 (~56% 参数) 是 "potential pruning or distillation targets"。这个 claim 基于 open-loop probe R² 下降。是否有任何证据（即使是 preliminary 的）表明 pruning 这些层不会严重损害 closed-loop 性能？

---

## 格式合规检查

- [x] Double-blind：满足（author 为 Anonymous）
- [x] 页数：主文约 8 页（需编译确认）
- [x] Limitations section：在 Discussion §5 中
- [x] Generative AI 声明：在 Appendix 开头
- [ ] 模板：使用 `\usepackage{corl_2026}`，无法从 .tex 确认是否为官方最新版
- 行号：未在 .tex 中看到 `\usepackage{lineno}` 或类似设置，需确认 corl_2026.sty 是否自带行号



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-19T00:55:16.096325+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-19T00:55:16.096711+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 638 · 2026-05-19T00:55:20.503458+00:00_

Reviewer 1 评分 5/10，提出 4 个 critical issues（ablation 自相矛盾、causal overclaim、counterfactual ordering 异常、统计功效不足）和 6 个 warnings。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 639 · 2026-05-19T00:55:23.201166+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**5/10，borderline reject**。论文的多方法互证框架和三条件 factorial 设计有明显方法论贡献，但存在四个 critical 问题：

1. **Random-subset ablation 结果自相矛盾** — 移除 instruction-dominant heads 反而提升 R²，且效果弱于随机 heads，直接削弱核心 routing claim
2. **"Causal" 标签过度** — 全部 open-loop 分析，无闭环验证
3. **Counterfactual ordering 与 semantic distance 叙事不符** — paraphrased > shuffled 暗示 token-level sensitivity 而非语义理解
4. **N=10 tasks 的统计功效不足** — 基于 underpowered non-significance 得出 negative conclusion ("not geometry")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 640 · 2026-05-19T00:55:29.370306+00:00_

Reviewer 1 结果已记录。继续等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 68

## Round 68

8 recorded events


### User

_source line 641 · 2026-05-19T00:55:55.595967+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Vision Encodes, Language Routes

## 总体评分
**Overall**: 5/10 (Marginally below acceptance threshold)
**Confidence**: 4/5
**一句话总结**: 方法论严谨的 representational analysis 论文，但单模型/单基准范围和完全缺失 closed-loop 验证使其对 CoRL 社区的实际价值存疑。

## 官方维度打分（CoRL review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 6/10 | Token-level + factorial controls 框架相对 Grant et al. 2026 有方法论增量，但核心发现（fine-tuning 改 routing 不改 visual geometry）部分重复已有结论 |
| Quality | 7/10 | 统计方法严谨（bootstrap CI、FDR correction、permutation test、seed sensitivity），但消融 R² 与 trajectory d 的矛盾解释不够清晰 |
| Clarity | 7/10 | 结构清晰，"七项互补分析"框架有效，但 jargon 密度高（RSA、CKA、Cohen's d 等），某些关键解释反直觉且篇幅不足 |
| Significance | 5/10 | 对 ML interpretability 有中等贡献，但对 robot learning 无经过验证的 actionable insight |
| Relevance | 5/10 | 纯 representational analysis，无物理机器人实验、无 closed-loop 评估、无学习算法改进；更适合 NeurIPS/ICML |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 单模型单基准范围严重限制 generalizability
- 具体位置：Section 3.1, Section 5 (Limitations, line 27-28), 全文
- 问题：论文仅研究 OpenVLA-7B 一个模型，在 LIBERO-Goal 一个基准上做主实验（LIBERO-Spatial 为同一模拟器、同一机器人、同一动作空间的交叉验证）。Section 5 对 π₀（cross-attention）、RT-2（decoder-only）、更大 VLA 做了三个预测，但无一经过验证。VLA 领域正快速多样化（π₀ cross-attention、Octo diffusion heads、不同 embodiment/action space），单模型在桌面基准上的发现对其他架构范式的迁移性不确定。
- 为什么影响接收：CoRL 社区关注发现的实际泛化性。一个仅在 OpenVLA-7B + LIBERO 上的分析，读者很难判断哪些是该模型的特性、哪些是 VLA 的通用机制。
- 建议修改方向：至少在一个不同架构（如 π₀ 或 RT-2）或不同 embodiment 上验证核心 C2 发现（entry-exit routing pattern），即使只做 attention profile 比较也可以显著增强说服力。

**N2** [critical] 完全缺失 closed-loop / task-performance 验证
- 具体位置：Section 5, line 19 ("potential pruning or distillation targets"), line 24 ("L1 probes could monitor routing integrity"), line 28 ("closed-loop evaluation is future work")
- 问题：所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（routing monitoring、layer pruning/distillation、56% 参数潜在可删减）均为未验证的猜测。核心发现（L1 routing）与 task success rate 之间无任何因果链。probe R² 和 trajectory divergence (Cohen's d) 衡量的是表征质量和动作偏移，而非任务完成率。
- 为什么影响接收：CoRL 评审标准要求论文 "explicitly address a learning question for physical robots" 或 "test the proposed learning solution on physical robots"。本文两项都不满足。Section 5 的 design implications 是本文对 CoRL 最强的 relevance pitch，但全部未经验证。
- 建议修改方向：（1）基于 routing analysis 结论做 layer pruning/distillation，在 LIBERO 上跑 closed-loop success rate；（2）展示 L1 routing integrity metric 与 task success rate 的相关性；（3）至少其中一项可以将本文从纯分析论文提升为有 actionable robotics insight 的论文。

**N3** [critical] CoRL scope fit 存疑
- 具体位置：全文
- 问题：论文本质上是一篇 transformer mechanistic interpretability 论文，碰巧分析对象是 VLA。主要方法来自 NLP interpretability（probing, attention analysis, RSA）；主要 positioning 对标 NLP/ML 会议的 interp 工作（Elhage 2021, Olsson 2022, Wang 2023 等）；主要发现（routing reorganization, metric-dependent peaks）对 robot learning 的指导意义停留在 Discussion 的推测层面。
- 为什么影响接收：CoRL scope 要求 "relevance to robotic learning"，而本文的 robotics 关联仅是分析对象的选择（VLA 而非纯 LLM），而非实验内容或结论。在当前的 CoRL 投稿竞争中，纯 analysis 论文需要格外强的 actionable insight 才能说服 reviewer。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C1（architecture validation）占比失衡
- 具体位置：Abstract line 4, Introduction line 17, Section 4.2, Table 1, Contribution (i)
- 问题：C1 是 causal mask + frozen encoder 的必然结果，论文自己称之为 "sanity check"（Section 4.2, line 18）。然而 C1 占据了 Abstract 最长的 finding 描述、Introduction 的第一个 finding 段落、一个完整 subsection (4.2) + Table 1、以及 Contribution 列表的 (i)。对一个 "expected result"，这一权重过高。
- 建议：将 C1 精简为 Section 4.2 的一段话 + Table 1 的一行，释放空间给 C2 的更深入分析或 missing validation experiments。Abstract 和 Introduction 中减少 C1 篇幅。

**W2** [warning] Vision representation 的训练效果小到可能无实际意义
- 具体位置：Section 4.4, Table 8 (Appendix), Table 10 (Appendix)
- 问题：RSA best-vs-best Δρ = +0.017 (3%), LIBERO-Goal 上 non-significant (CI includes 0)。Image_mean R² Δ = +0.015 (p=0.006，borderline)。Same-layer L12 comparison (Δρ = +0.079) 混淆了 peak-shift effect 和 magnitude effect。论文声称 "training enhances decodability, not geometry"，但 decodability gains 也很小（readout Δ = +0.069 是 meaningful，但 image_mean Δ = +0.015 不是）。这意味着 VLA fine-tuning 对 vision representations 的改变非常有限，核心改变集中在 readout routing。论文虽然如实报告了这一点，但 framing 上未充分强调这对 "VLA fine-tuning 到底学了什么" 这个 headline question 的含义：答案可能是 "非常有限的东西"。

**W3** [warning] 消融 R² 解释反直觉且不充分
- 具体位置：Section 4.3 lines 65-67, Appendix A.7
- 问题：Instruction-dominant heads 消融使 R² 增加 +0.042，但 random subset 消融使 R² 增加更多（+0.077±0.013, z=-2.73, p=0.003）。论文解释："dominant heads carry organized routing signals (structured noise for the probe); random heads lack such organization"。这一解释反直觉：如果 dominant heads 是 functionally special for routing，消融它们应该造成更大（而非更小）的 probe disruption。用 trajectory divergence (Cohen's d = 0.65 vs 0.41) 和 R² 两个指标得出相反结论的做法，使读者难以判断哪个指标更可信。
- 建议：需要更清晰地解释为什么 R² 增加反映的是 routing signal 的移除（而非功能的破坏），并讨论 probe R² 作为衡量 routing function 的指标的局限性。

**W4** [warning] Counterfactual ordering 与 semantic distance claim 不完全一致
- 具体位置：Section 4.3 line 79, Table A7 (Appendix)
- 问题：论文声称 "the ordering follows semantic distance from the original instruction"。数据显示：empty d=0.968 > wrong task d=0.844 > paraphrased d=0.697 > shuffled d=0.625。但 paraphrased（不同词汇但保留原意）的 d 高于 shuffled（原词汇但打乱顺序），这与语义距离假说不一致：paraphrase 语义上更接近原始 instruction，应该产生更小的 d。实际数据表明模型对 lexical identity 比 syntactic structure 更敏感，这与 attention-based routing（依赖 token identity 而非 word order）一致，但论文未讨论这一点。

**W5** [warning] 竞争者工作的 positioning 不够深入
- 具体位置：Section 2, Related Work
- 问题：Swann et al. 2026 和 Buurmeijer et al. 2026 用 SAE 发现了 VLA 中的 interpretable features 和 memorized action sequences。论文 Related Work 仅提及一句（line 21），未讨论 SAE features 是否 corroborate 或 contradict L1 routing hypothesis。Häon et al. 2025 发现 "sparse semantic directions in VLA residual streams"，论文仅提及但未讨论与 attention-based routing mechanism 的关系。Grant et al. 2026 的三点差异化陈述（Related Work lines 24-25）清晰，但其他竞争者的差异化不足。

**W6** [warning] 缺失引用
- 具体位置：references.bib
- 问题：以下重要相关工作未被引用：
  - **Octo** (Ghosh et al. 2024)：主要开源 VLA，cross-attention 架构，与论文 Discussion 中对 π₀ 的预测直接相关
  - **Rizzardo et al. 2026**：VLA 内部分析方面的竞争者（Director 指定检查）
  - 46 篇引用对于 CoRL 论文在一个拥挤的 VLA 分析领域偏少
- 引用验证工具显示：6 篇 not_found（elhage2021、hewitt2019、bills2023language、templeton2024scaling、nostalgebraist2020、black2024_pi0），均为 blog posts 或特殊标题格式的论文，属于 OpenAlex 未收录，非虚假引用。5 篇 minor mismatch（first author 格式），无实质问题。

---

## 小问题（不影响接收）

- Abstract line 1: "but what fine-tuning changes at the representational level remains unclear" 稍显 awkward，建议 "but the representational changes induced by fine-tuning remain unclear"
- Section 4.3 footnote 1 (line 65): R² baseline 不同的解释放在脚注中容易被忽略，建议在正文中明确说明 within-experiment comparisons
- Appendix 中 figures 使用 `[h]` placement；部分 figure caption 较长但信息量高，整体可接受
- Generative AI 声明存在且符合要求
- 匿名化检查：无明显 de-anonymization（作者列为 "Anonymous"，无代码仓库链接）
- 页数：正文看起来在 8 页限制内（需 PDF 确认）
- Limitations section 存在且融入 Discussion

---

## Questions for Authors

Q1: 你们有条件在 π₀ 或 RT-2 等不同架构的 VLA 上验证 L1 routing pattern 吗？即使只做 32-layer attention profile 比较，也能大幅增强 generalizability claim。

Q2: 是否考虑过将 routing analysis 的结论用于 layer pruning，然后在 LIBERO 上跑 closed-loop success rate 来验证 "last 18 layers are pruning targets" 的声明？这对 CoRL 读者的价值远大于 probe R²。

Q3: 关于 W3（消融 R² 反直觉）：能否提供一个更详细的解释，说明为什么 ablating organized routing signals 对 probe 的影响小于 ablating random heads？是否有理论框架可以预测这一结果？

Q4: 关于 W4（counterfactual ordering）：paraphrased d=0.697 > shuffled d=0.625 是否表明 VLA 对 lexical identity 比 syntactic structure 更敏感？这似乎与 token-level attention routing mechanism 一致，但论文未讨论。

Q5: 论文 Discussion 中预测 cross-attention VLAs 不会有 L1 routing heads。如果这一预测成立，这意味着本文的核心发现 (C2) 仅适用于 decoder-only VLAs，这进一步缩小了 generalizability scope。你们如何看待这一 tension？

---

## Missing References

1. **Octo** (Ghosh et al. 2024): 开源 cross-attention VLA，与 Discussion 中对 cross-attention 架构的预测直接相关
2. **Rizzardo et al. 2026**: VLA 内部分析的竞争者工作
3. 建议补充近期 multimodal interpretability 论文以增加引用覆盖度

---

## 主要优势

1. **方法论严谨**：Factorial design（三条件 × 有无 instruction）是该领域少见的系统化设计。七项互补分析（causal + supporting + constraining）构成令人信服的证据链条。
2. **Robustness 检查充分**：seed sensitivity、demo subsampling、threshold sensitivity、distance metric invariance、linear vs MLP probe、cross-benchmark (LIBERO-Spatial) 验证。这一水平的 robustness 检查超过同领域大多数论文。
3. **核心发现（C2 routing）有价值**：Entry-exit routing pattern 与 Llama-2 base 的 mid-depth pattern 的对比是 genuine insight，且有多项 converging evidence 支持。
4. **诚实汇报**：C1 被标为 sanity check，C3 的 metric-dependent 性质被明确说明，CKA divergence 被如实报告而非隐藏。Limitations 段有实质内容。
5. **与 Grant et al. 2026 的差异化清晰**：token-level vs feature-level、per-layer decomposition、factorial controls 三点区别陈述明确（Related Work lines 24-25）。

---

## Overall Assessment

本文是一篇方法论扎实、数据分析严谨的 representational analysis 论文。核心贡献 C2（VLA fine-tuning 将 instruction routing 前置到 entry-exit layers）是有价值的发现，七项互补分析形成有说服力的证据链。然而，三个 critical 问题使其在 CoRL 的接收前景不乐观：（1）单模型单基准范围限制 generalizability；（2）完全缺失 closed-loop 验证使 robotics implications 停留在猜测层面；（3）论文本质上是 NLP-style mechanistic interpretability 工作，对 CoRL 的 scope fit 有限。如果作者能增加至少一项 closed-loop validation（如基于 routing analysis 的 layer pruning + task success 评估）和至少一个额外模型/架构的验证，本文将显著增强竞争力。当前版本更适合投往 NeurIPS/ICML 的 interpretability track。

Rating: **5/10** — Marginally below acceptance threshold
Confidence: **4/5**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-19T00:56:10.567773+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-19T00:56:10.820141+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-19T00:56:50.942228+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每个 Must-Fix 和 Should-Fix 条目，标注 **[AGREE]** 或 **[REBUT]**，并说明理由。如有 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\nOverall: 5/10 (Marginally below acceptance threshold)\nConfidence: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 单模型单基准范围严重限制 generalizability\n- 仅研究 OpenVLA-7B，在 LIBERO-Goal 上做主实验（LIBERO-Spatial 为同一模拟器的交叉验证）。Section 5 对 π₀、RT-2、更大 VLA 做了三个预测，但无一经过验证。VLA 领域正快速多样化，单模型发现的迁移性不确定。\n\n**N2** [critical] 完全缺失 closed-loop / task-performance 验证\n- 所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（routing monitoring、layer pruning/distillation、56% 参数潜在可删减）均为未验证的猜测。probe R² 和 trajectory divergence 衡量的是表征质量和动作偏移，而非任务完成率。CoRL 评审标准要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"。\n\n**N3** [critical] CoRL scope fit 存疑\n- 论文本质上是 transformer mechanistic interpretability 论文，碰巧分析对象是 VLA。主要方法来自 NLP interpretability；主要 positioning 对标 NLP/ML 的 interp 工作；主要发现对 robot learning 的指导意义停留在 Discussion 推测层面。更适合 NeurIPS/ICML。\n\n### Should-Fix 问题\n\n**W1** [warning] C1（architecture validation）占比失衡\n- C1 是 causal mask + frozen encoder 的必然结果，论文自己称之为 \"sanity check\"。但 C1 占据了 Abstract 最长的 finding 描述、Introduction 的第一个 finding 段落、一个完整 subsection + Table 1、以及 Contribution 列表的 (i)。权重过高。\n\n**W2** [warning] Vision representation 的训练效果小到可能无实际意义\n- RSA best-vs-best Δρ = +0.017 (3%), n.s.。image_mean R² Δ = +0.015 (p=0.006, borderline)。VLA fine-tuning 对 vision representations 的改变非常有限，核心改变集中在 readout routing。Framing 上未充分强调这对 headline question 的含义。\n\n**W3** [warning] 消融 R² 解释反直觉且不充分\n- Instruction-dominant heads 消融使 R² 增加 +0.042，random subset 增加更多 (+0.077±0.013)。论文解释 \"structured noise for the probe\" 反直觉。用 trajectory divergence 和 R² 两个指标得出相反结论，读者难以判断哪个更可信。\n\n**W4** [warning] Counterfactual ordering 与 semantic distance claim 不完全一致\n- paraphrased d=0.697 > shuffled d=0.625，但 paraphrase 语义上更接近原始 instruction。实际数据表明模型对 lexical identity 比 syntactic structure 更敏感。\n\n**W5** [warning] 竞争者工作的 positioning 不够深入\n- Swann et al. 2026 和 Buurmeijer et al. 2026 的差异化不足。Häon et al. 2025 与 attention-based routing mechanism 的关系未讨论。\n\n**W6** [warning] 缺失引用\n- Octo (Ghosh et al. 2024)、Rizzardo et al. 2026 未引用。46 篇引用对 CoRL 在拥挤的 VLA 分析领域偏少。\n\n---\n\n请逐条回应。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每个 Must-Fix 和 Should-Fix 条目，标注 **[AGREE]** 或 **[REBUT]**，并说明理由。如有 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\nOverall: 5/10 (Marginally below acceptance threshold)\nConfidence: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 单模型单基准范围严重限制 generalizability\n- 仅研究 OpenVLA-7B，在 LIBERO-Goal 上做主实验（LIBERO-Spatial 为同一模拟器的交叉验证）。Section 5 对 π₀、RT-2、更大 VLA 做了三个预测，但无一经过验证。VLA 领域正快速多样化，单模型发现的迁移性不确定。\n\n**N2** [critical] 完全缺失 closed-loop / task-performance 验证\n- 所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（routing monitoring、layer pruning/distillation、56% 参数潜在可删减）均为未验证的猜测。probe R² 和 trajectory divergence 衡量的是表征质量和动作偏移，而非任务完成率。CoRL 评审标准要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"。\n\n**N3** [critical] CoRL scope fit 存疑\n- 论文本质上是 transformer mechanistic interpretability 论文，碰巧分析对象是 VLA。主要方法来自 NLP interpretability；主要 positioning 对标 NLP/ML 的 interp 工作；主要发现对 robot learning 的指导意义停留在 Discussion 推测层面。更适合 NeurIPS/ICML。\n\n### Should-Fix 问题\n\n**W1** [warning] C1（architecture validation）占比失衡\n- C1 是 causal mask + frozen encoder 的必然结果，论文自己称之为 \"sanity check\"。但 C1 占据了 Abstract 最长的 finding 描述、Introduction 的第一个 finding 段落、一个完整 subsection + Table 1、以及 Contribution 列表的 (i)。权重过高。\n\n**W2** [warning] Vision representation 的训练效果小到可能无实际意义\n- RSA best-vs-best Δρ = +0.017 (3%), n.s.。image_mean R² Δ = +0.015 (p=0.006, borderline)。VLA fine-tuning 对 vision representations 的改变非常有限，核心改变集中在 readout routing。Framing 上未充分强调这对 headline question 的含义。\n\n**W3** [warning] 消融 R² 解释反直觉且不充分\n- Instruction-dominant heads 消融使 R² 增加 +0.042，random subset 增加更多 (+0.077±0.013)。论文解释 \"structured noise for the probe\" 反直觉。用 trajectory divergence 和 R² 两个指标得出相反结论，读者难以判断哪个更可信。\n\n**W4** [warning] Counterfactual ordering 与 semantic distance claim 不完全一致\n- paraphrased d=0.697 > shuffled d=0.625，但 paraphrase 语义上更接近原始 instruction。实际数据表明模型对 lexical identity 比 syntactic structure 更敏感。\n\n**W5** [warning] 竞争者工作的 positioning 不够深入\n- Swann et al. 2026 和 Buurmeijer et al. 2026 的差异化不足。Häon et al. 2025 与 attention-based routing mechanism 的关系未讨论。\n\n**W6** [warning] 缺失引用\n- Octo (Ghosh et al. 2024)、Rizzardo et al. 2026 未引用。46 篇引用对 CoRL 在拥挤的 VLA 分析领域偏少。\n\n---\n\n请逐条回应。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-19T00:57:20.186846+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29244
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-19T00:57:20.237880+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每个 Must-Fix 和 Should-Fix 条目，标注 **[AGREE]** 或 **[REBUT]**，并说明理由。如有 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\nOverall: 5/10 — Marginally below acceptance threshold\nConfidence: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Random-subset ablation 结果与核心叙事矛盾\n- 论文的核心 claim 是 L1 的 24 个 instruction-dominant heads 是 instruction routing 的功能载体。但 ablation 实验显示，移除这 24 个 dominant heads 使 action probe R² **增加** +0.042，而随机 24 heads 的 ablation R² 增加更大（+0.077）。(a) 移除 instruction routing 反而让 action 更容易解码；(b) dominant heads 的效应甚至弱于随机 heads。论文的解释（\"structured noise for the probe\"）是 post-hoc rationalization，缺乏独立验证。如果 instruction signal 真的是 \"结构化噪声\"，那么整个 routing 叙事都需要重新审视。\n\n**N2** [critical] \"Causal\" claim 在 open-loop 设定下不成立\n- 所有分析均为 representational/open-loop。Discussion §5 明确使用 \"Causal\" 标签分类证据，但真正的因果验证需要闭环评估（ablate → deploy → measure task success）。应将措辞改为 \"interventional\" 或 \"quasi-causal\"。\n\n**N3** [critical] Counterfactual instruction ordering 与 semantic distance 叙事不符\n- paraphrased (d=0.697) > shuffled (d=0.625)：paraphrased 在语义上应比 shuffled 更接近原始指令，但产生更大 divergence。说明模型对 token identity 比语义更敏感，支持 Grant et al. 的 \"language instructions largely ignored\" 结论，与本文叙事（instruction routing 有功能意义）形成张力。\n\n**N4** [critical] 统计功效不足以支撑核心比较\n- RSA bootstrap N=10 tasks。论文自己承认 \"n.s. result reflects limited statistical power\"。但主文仍将 Δρ=0.017 报告为 \"non-significant\" 并据此得出 \"training enhances decodability, not geometry\"。在 N=10 下不能基于 underpowered non-significance 得出 negative conclusion。\n\n### Should-Fix 问题\n\n**W1** [warning] Probe 严重过参数化\n- MLP probe N/params ≈ 0.06。虽然 linear probe 复现了定性模式，但主文报告的所有 R² 值均来自过参数化的 MLP probe。\n\n**W2** [warning] N=63,228 的独立性假设\n- 同一 demo 内的 frames 存在强时间自相关。Demo-level split 解决了泄露，但 bootstrap 比较中有效独立单元数远小于 63,228。\n\n**W3** [warning] Cohen's d 的独立性假设违反\n- Action tokens 在同一 trajectory 内强烈相关。将每个 action token 作为独立观测计算 d 会系统性高估 effect size。\n\n**W4** [warning] Pretrained Llama-2 base control 的有效性\n- Llama-2 base 从未见过 projected visual tokens。Appendix 诊断仅证明表征非退化，不证明与 VLA-trained 可比。Llama-2 base 在 L1 显示 9/32 instruction-dominant heads 可能仅因为 instruction tokens 是 in-distribution input，与 \"language pretraining seeds partial instruction routing\" 的解读不同。\n\n**W5** [warning] Specificity control 效果有限\n- Top-24 vs Bottom-24 有 16 heads 重叠。d ratio 仅 1.15×，特异性有限。\n\n**W6** [warning] 单模型范围\n- 仅研究 OpenVLA-7B。Discussion 对其他架构做了预测但均未验证。Framework 的泛化性仅在同一模型的两个 LIBERO suite 上验证过。\n\n---\n\n请逐条回应。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每个 Must-Fix 和 Should-Fix 条目，标注 **[AGREE]** 或 **[REBUT]**，并说明理由。如有 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\nOverall: 5/10 — Marginally below acceptance threshold\nConfidence: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Random-subset ablation 结果与核心叙事矛盾\n- 论文的核心 claim 是 L1 的 24 个 instruction-dominant heads 是 instruction routing 的功能载体。但 ablation 实验显示，移除这 24 个 dominant heads 使 action probe R² **增加** +0.042，而随机 24 heads 的 ablation R² 增加更大（+0.077）。(a) 移除 instruction routing 反而让 action 更容易解码；(b) dominant heads 的效应甚至弱于随机 heads。论文的解释（\"structured noise for the probe\"）是 post-hoc rationalization，缺乏独立验证。如果 instruction signal 真的是 \"结构化噪声\"，那么整个 routing 叙事都需要重新审视。\n\n**N2** [critical] \"Causal\" claim 在 open-loop 设定下不成立\n- 所有分析均为 representational/open-loop。Discussion §5 明确使用 \"Causal\" 标签分类证据，但真正的因果验证需要闭环评估（ablate → deploy → measure task success）。应将措辞改为 \"interventional\" 或 \"quasi-causal\"。\n\n**N3** [critical] Counterfactual instruction ordering 与 semantic distance 叙事不符\n- paraphrased (d=0.697) > shuffled (d=0.625)：paraphrased 在语义上应比 shuffled 更接近原始指令，但产生更大 divergence。说明模型对 token identity 比语义更敏感，支持 Grant et al. 的 \"language instructions largely ignored\" 结论，与本文叙事（instruction routing 有功能意义）形成张力。\n\n**N4** [critical] 统计功效不足以支撑核心比较\n- RSA bootstrap N=10 tasks。论文自己承认 \"n.s. result reflects limited statistical power\"。但主文仍将 Δρ=0.017 报告为 \"non-significant\" 并据此得出 \"training enhances decodability, not geometry\"。在 N=10 下不能基于 underpowered non-significance 得出 negative conclusion。\n\n### Should-Fix 问题\n\n**W1** [warning] Probe 严重过参数化\n- MLP probe N/params ≈ 0.06。虽然 linear probe 复现了定性模式，但主文报告的所有 R² 值均来自过参数化的 MLP probe。\n\n**W2** [warning] N=63,228 的独立性假设\n- 同一 demo 内的 frames 存在强时间自相关。Demo-level split 解决了泄露，但 bootstrap 比较中有效独立单元数远小于 63,228。\n\n**W3** [warning] Cohen's d 的独立性假设违反\n- Action tokens 在同一 trajectory 内强烈相关。将每个 action token 作为独立观测计算 d 会系统性高估 effect size。\n\n**W4** [warning] Pretrained Llama-2 base control 的有效性\n- Llama-2 base 从未见过 projected visual tokens。Appendix 诊断仅证明表征非退化，不证明与 VLA-trained 可比。Llama-2 base 在 L1 显示 9/32 instruction-dominant heads 可能仅因为 instruction tokens 是 in-distribution input，与 \"language pretraining seeds partial instruction routing\" 的解读不同。\n\n**W5** [warning] Specificity control 效果有限\n- Top-24 vs Bottom-24 有 16 heads 重叠。d ratio 仅 1.15×，特异性有限。\n\n**W6** [warning] 单模型范围\n- 仅研究 OpenVLA-7B。Discussion 对其他架构做了预测但均未验证。Framework 的泛化性仅在同一模型的两个 LIBERO suite 上验证过。\n\n---\n\n请逐条回应。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-19T00:57:21.755133+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1517
}
```

</details>

---


### Assistant

_source line 648 · 2026-05-19T00:57:24.507259+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 649 · 2026-05-19T00:57:27.188242+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**5/10，marginally below acceptance threshold**。

三个 critical 问题：
1. **单模型单基准**（仅 OpenVLA-7B + LIBERO）严重限制 generalizability
2. **无 closed-loop 验证**：所有 robotics implications（pruning、routing monitoring）均为未验证猜测
3. **CoRL scope fit 有限**：本质是 NLP-style mechanistic interpretability 论文，无物理机器人实验，无学习算法改进

主要优势是方法论严谨（factorial design + 七项互补分析 + 充分 robustness checks）和核心发现 C2（entry-exit routing pattern）的 converging evidence。建议增加 closed-loop validation 和多架构验证后投 NeurIPS/ICML，或补充这些内容后再投 CoRL。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 650 · 2026-05-19T00:57:31.842897+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 651 · 2026-05-19T00:58:28.882439+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 条目

**[AGREE] R2-N1: 单模型单基准范围严重限制 generalizability**

同意。这与我的 W6 一致。补充一点：论文在 LIBERO-Spatial 上的交叉验证（Appendix §A.10, Figure A.7）虽然复现了 inverted-U 和 cross-instruction probe 的定性模式，但这仍是同一模型 (OpenVLA-7B) 在同一模拟器 (LIBERO) 的不同 task suite 上的测试，不能算 model-level generalization。Discussion §5 的三条预测（π₀ 无 L1 routing heads、RT-2 有类似 entry-layer routing、larger VLAs 更平坦的 per-head contribution）是论文最有价值的可检验假设，但全部停留在推测。至少应验证一个预测（例如 RT-2 的 attention profile）来增强说服力。

---

**[AGREE] R2-N2: 完全缺失 closed-loop / task-performance 验证**

强烈同意。这与我的 N2 一致。进一步补充：论文中最具 actionable 意味的 claim 有三个——(a) L1 routing monitoring 可在部署时检测 routing integrity (Discussion §5 倒数第 2 段)；(b) L14-L32 约 56% 参数为 pruning/distillation targets (Discussion §5 第 3 段)；(c) instruction-discriminative tasks 对 L1 routing 依赖更强 (Table A.15)。这三个 claim 的实际价值完全取决于闭环验证。特别是 pruning claim：open-loop probe R² 在 L14+ 下降不等于这些层对 closed-loop task success 无贡献——后面的层可能负责 action token decoding 的 fine-grained timing（如 gripper 时机），这恰好是 R² 无法捕捉的。

---

**[REBUT] R2-N3: CoRL scope fit 存疑**

部分不同意，不应作为 critical/must-fix。

理由：

1. CoRL 2023 reviewer guidelines 明确列出 "Relevance" 作为评审维度，其定义为 "alignment with robot learning and CoRL audience interests"，而非要求必须有 real-robot experiments。CoRL 2024 的 scope 说明也接受 "results relevant to robot learning"，包含 theoretical 和 empirical 两类。

2. 论文分析的对象 (OpenVLA-7B) 和 benchmark (LIBERO) 均为 robotics community 的核心产物。与纯 NLP interpretability 工作的区别在于：(a) 分析的 token 类型包括 image tokens 和 action-generating readout tokens，这些在 NLP 中不存在；(b) probe target 是 7-D robot actions 而非 language prediction；(c) 发现的 entry-exit routing pattern 是 VLA fine-tuning 特有的，Llama-2 base 的 mid-depth pattern 恰好证明这不是 LLM 的通用属性。

3. CoRL 历史上接收过多篇纯分析/理解类论文（不含 real-robot experiments），只要其发现对 robot learning 有直接 implications。

4. 不过，R2 的底层担忧是合理的：论文的 positioning 确实过度对标 NLP interpretability 文献（Related Work §2 中 Elhage、Olsson、Wang、Meng、Belrose 等引用占了大量篇幅），而对 robotics-specific 的启示讨论不够具体。建议降级为 warning 而非 critical。

---

## Should-Fix 条目

**[AGREE] R2-W1: C1（architecture validation）占比失衡**

同意。论文在 §4.2 自己将 C1 定位为 "sanity check on the experimental framework"，但 C1 占据了：Abstract 第 4 行（最长的 finding 描述）、Introduction §1 第 17 行的 "First" 段落、§4.2 完整 subsection + Table 1、Contribution 列表的 (i)。如果作者认为这是预期结果和 framework validation，应压缩到 1-2 句话 + 一个 table，将 page budget 让给更有新意的 C2 和 C3。当前 framing 让读者误以为 C1 是一个实质性发现。

---

**[AGREE] R2-W2: Vision representation 训练效果小到可能无实际意义**

同意。补充定量证据：Table A.14 汇总了所有训练效果——image_mean RSA Δ=+0.017 (n.s.)、R² Δ=+0.015 (p=0.006, borderline under multiple comparisons)。与 last_preaction 的效果对比（R² Δ=+0.069, attention +46pp），vision pathway 的训练效果小一个数量级。论文的叙事应更直接地承认：VLA fine-tuning 对 visual representations 的改变在统计上微弱且可能无实际意义，核心改变完全集中在 readout token 的 routing 机制。当前 framing（§4.4 标题 "Training enhances decodability, not geometry"）虽然技术上准确，但用 "enhances" 来描述 image_mean R² Δ=+0.015 有夸大嫌疑。

---

**[AGREE] R2-W3: 消融 R² 解释反直觉且不充分**

强烈同意。这与我的 N1 (critical) 一致，我甚至认为应升级为 must-fix 而非 should-fix。核心矛盾：如果 instruction-dominant heads 携带功能性 routing signal，ablation 应该降低 action decodability (R² 下降)，但实验显示 R² 反而增加，且增幅小于 random ablation。"structured noise" 的解释需要独立验证——例如，可以检验 ablation 后 readout token 的 representation 维度是否降低（如果 instruction signal 占据了独立的子空间，移除后 effective dimensionality 下降，probe 更容易拟合）。没有这样的验证，"structured noise" 仅仅是一个 unfalsifiable 的 post-hoc story。

---

**[AGREE] R2-W4: Counterfactual ordering 与 semantic distance claim 不完全一致**

同意。这与我的 N3 一致。补充：如果论文能报告 4 种 perturbation 条件下 instruction tokens 的 token-level overlap rate（例如 shuffled 保留 100% tokens、paraphrased 可能仅保留 30-50%），读者就能判断 d ordering 反映的是 token identity sensitivity 还是 semantic sensitivity。当前数据实际上暗示 OpenVLA 对 lexical identity 比 semantic content 更敏感，这与 Grant et al. 和 Häon et al. 关于 VLA 语言理解肤浅的发现一致，但论文的 framing 回避了这一解读。

---

**[REBUT] R2-W5: 竞争者工作的 positioning 不够深入**

部分不同意。

Related Work §2 第 3 段对 Grant et al. [2026] 的差异化是充分的——明确列出三点区别（token-level vs feature-level、per-layer vs whole-model、factorial controls）。Swann et al. [2026] 和 Buurmeijer et al. [2026] 属于 SAE-based interpretability，与本文的 probing + attention analysis 方法正交，不需要逐一深入对比。

但我同意 Häon et al. [2025] 的处理确实不足。Häon et al. 发现了 VLA residual stream 中的 sparse semantic directions linked to action selection，这与本文的 L1 routing heads 发现存在直接互补关系（一个在 feature 层面，一个在 head 层面），应该讨论两者是否捕捉同一机制的不同视角。

---

**[AGREE] R2-W6: 缺失引用**

部分同意。Octo (Ghosh et al. 2024) 是 robotics community 的重要 VLA baseline，应该在 Related Work §2 第 1 段 (VLA 列表) 中被引用，尽管其架构（non-LLM-based）与本文分析对象不同。引用密度对于一篇 analysis/survey 性质的论文确实偏低——同类论文（如 Grant et al. 2026 的 mechanistic study）通常有 50-70 篇引用。

不过，"46 篇偏少" 的判断需要对照 CoRL 的平均引用量。CoRL 论文平均引用量通常低于 NeurIPS/ICML（因为 robotics 子领域相对集中），46 篇不一定构成硬伤。

---

## 总结

与 Reviewer 2 的主要共识：N1（单模型）、N2（无闭环验证）、W1-W4。
主要分歧：N3（scope fit）——我认为降级为 warning 更合适；W5（competitor positioning）——大部分已充分，仅 Häon et al. 需要补充。
我独有的 critical issues（R2 未覆盖）：N1（random-subset ablation 矛盾）、N3（counterfactual 升级为 critical）、N4（N=10 统计功效不足以支撑 negative conclusion）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 652 · 2026-05-19T00:58:39.484320+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 71

## Round 71

2 recorded events


### User

_source line 653 · 2026-05-19T00:58:42.168763+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **与 R2 共识**：N1（单模型）、N2（无闭环验证）、W1-W4 全部 AGREE
- **与 R2 分歧**：N3（CoRL scope fit）REBUT，建议降级为 warning；W5（competitor positioning）部分 REBUT，仅 Häon et al. 需补充
- **我独有的 critical issues**（R2 未覆盖）：random-subset ablation 结果与核心叙事矛盾、counterfactual ordering 暗示 token-level 而非 semantic sensitivity、N=10 统计功效不足以支撑 negative conclusion

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 654 · 2026-05-19T00:58:46.271363+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 72

## Round 72

10 recorded events


### User

_source line 655 · 2026-05-19T00:59:15.796308+00:00_

[Reviewer 2 审稿结果]:
逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 1

### Must-Fix 条目

**[AGREE with qualification] R1-N1: Random-subset ablation 与核心叙事的张力**

R1 指出的 R² 结果（dominant +0.042 < random +0.077）确实反直觉，我在自己的审稿中也将其列为 W3。但我不同意 R1 将此升级为 "整个 routing 叙事需要重新审视" 的程度。

理由：R² 与 trajectory divergence 的矛盾并非指向同一个量。probe R² 衡量的是从 frozen representation 解码 action 的容易程度（移除结构化信号反而可以简化解码）；Cohen's d 衡量的是 intervention 对 output trajectory 的功能影响（Section 4.3: dominant d=0.65 vs control d=0.41, Table A5）。后者与 routing function 的关联更直接。此外，dose-response curve（Figure A4, 8 conditions, monotonic d=0.48→0.64）、counterfactual analysis（Table A7, 4 conditions, d=0.63-0.97）、task-dependent routing（Table A11, p=0.033）三条独立证据线均支持 L1 routing 的功能意义，不依赖 R² ablation 结果。

**共识**：R² 解释确实是 post-hoc，论文应更明确讨论 R² 与 d 的分离机制。但将其定为推翻 routing narrative 的 critical issue 过重——routing claim 有至少五条 converging evidence，R² ablation 只是其中之一。建议降为 should-fix。

---

**[AGREE with nuance] R1-N2: "Causal" 术语在 open-loop 下的适用性**

R1 要求将 "Causal" 改为 "interventional" 或 "quasi-causal"，这在 robotics 语境下有道理。但需要注意：Discussion Section 5 使用 "Causal" 标签（第 8 行）是对标 mechanistic interpretability 文献的惯例——Meng et al. 2022 (ROME)、Wang et al. 2023 (IOI circuit) 均用 "causal tracing" 指代模型内部的 intervention 实验，而非 closed-loop deployment。论文的用法与这一领域惯例一致。

**共识**：CoRL 读者以 robotics 背景为主，"causal" 一词易引起对 closed-loop 因果的误解。改为 "interventional evidence" 是低成本高收益的修改。但这是 terminology issue，不构成 critical methodological flaw。建议降为 should-fix。

---

**[AGREE on ordering, REBUT on inference] R1-N3: Counterfactual ordering 与 semantic distance**

我在自己的审稿 W4 中提出了相同观察：paraphrased d=0.697 > shuffled d=0.625 与 "semantic distance" claim 不一致。这一点 R1 和我完全一致。

但 R1 进一步推断这 "支持 Grant et al. 的 language instructions largely ignored 结论，与本文叙事形成张力"——这我不同意。Table A7 显示：empty d=0.968, wrong task d=0.844, paraphrased d=0.697, shuffled d=0.625。所有条件均产生 substantial trajectory divergence（d > 0.6），这恰恰证明 instructions **are** influencing action generation，只是影响路径不走 semantic distance 而是走 lexical/token identity。这与 Grant et al. 的 "language largely ignored" 结论相矛盾而非支持。

**共识**：ordering 确实不符 semantic distance 叙事，论文应修正 Section 4.3 line 79 的表述。但数据本身支持 instruction-conditioned action generation（all d > 0.6），不支持 R1 的 "language ignored" 推断。

---

**[AGREE] R1-N4: 统计功效不足以支撑 negative conclusion**

R1 的统计论点完全正确。N=10 tasks 的 bootstrap 下，non-significant result (Δρ=0.017, CI includes 0) 不能等价于 "no effect"。论文在 Appendix A.14（cross-benchmark, LIBERO-Spatial: Δ=+0.023, p<0.001）自己也承认 "n.s. result on Goal reflects limited statistical power rather than a true null"。

但主文 Section 4.4 line 119 的措辞 "training enhances decodability, not geometry" 实质上是从 underpowered n.s. 得出了 negative claim。这是 inferential error。

**减缓因素**：LIBERO-Spatial 的 replication (p<0.001) 提供了 geometry gain 存在的证据，说明 LIBERO-Goal 的 n.s. 确实是 power 问题。论文应在主文中明确呈现 LIBERO-Spatial 的 significant result 作为对冲，并将 "not geometry" 改为 "limited geometric gain under current sample size"。

---

### Should-Fix 条目

**[REBUT] R1-W1: Probe 过参数化**

论文在 Appendix A.8（Section linear_probe）已直接回应此问题。Linear probe (N/params ≈ 2.2) 复现了 inverted-U pattern：trained image_mean peaks at L14 (R²=0.565), untrained declines monotonically from L0 (R²=0.517)。更关键的是，linear probe 下 trained-untrained gap **更大**（L14: Δ=+0.324 vs MLP L8: Δ=+0.015），说明 VLA training 使 action information 更 linearly decodable。Figure A6 (fig_linear_vs_mlp_probe.pdf) 直接对比了两种 probe 的 per-layer profile。

MLP probe 的过参数化是一个 valid concern，但论文已有充分的 robustness check。R1 的表述 "主文报告的所有 R² 值均来自过参数化的 MLP probe" 忽略了 Appendix 已提供 linear probe 作为验证。

---

**[AGREE partially] R1-W2: N=63,228 的独立性**

R1 正确指出 demo 内 frames 有强时间自相关。但论文的统计框架已部分处理了这一问题：RSA bootstrap 在 task level 重采样（Section 3.5: "resampling is performed at the task level, N=10, treating each task's pairwise RDM entries as a block"），probe 用 demo-level train/test split（Section 3.6: "demos 0-39 vs 40-49"）。有效独立单元数确实远小于 63,228，但分析的 blocking structure 已经将有效 N 降到了 task/demo 粒度，而非假装每个 frame 独立。

**共识**：论文应在 Method 或 Appendix 中明确说明有效独立单元数和 blocking 策略，避免 N=63,228 给读者错误印象。

---

**[AGREE] R1-W3: Cohen's d 的独立性假设违反**

这一点 R1 完全正确，我在自己的审稿中未充分关注。同一 trajectory 内的 action tokens 存在强时间自相关（连续 frames 的 action 高度相似），将每个 token 作为独立观测计算 Cohen's d 会系统性高估 effect size。论文报告的 d 值（0.48-0.97）的绝对值可能被 inflate。

不过，d 值之间的 **相对排序**（empty > wrong > paraphrased > shuffled > ablation > control）不太可能被自相关改变，因为自相关对所有条件的影响方向一致。定量 d 值存疑，但定性结论（routing 的 graded effect, dose-response 的 monotonicity）应仍成立。

---

**[AGREE partially, REBUT partially] R1-W4: Pretrained Llama-2 base control 的有效性**

R1 提出一个精细的替代解释：Llama-2 base 的 9/32 instruction-dominant heads 可能仅因为 instruction tokens 是 in-distribution text（而 image tokens 是 OOD），不代表 "language pretraining seeds partial routing"。

这一替代解释 plausible，但不影响核心发现：无论 9/32 的原因是 "text in-distribution bias" 还是 "pretraining seeds routing"，from pretrained (9/32) to VLA-trained (24/32) 的 shift (+15 heads, +21.2pp attention) 仍然是 VLA fine-tuning 的效应。Appendix A.9 (Figure A3, fig_ood_diagnostics.pdf) 的诊断虽然不能排除 R1 的解释，但三项指标（activation magnitude non-exploding, cosine similarity progressive decrease, PC variance stable）至少排除了 Llama-2 base representations 的退化假说。

**共识**：论文应在 Discussion 中提及 R1 的替代解释，并强调无论 baseline 9/32 的来源如何，pretrained→trained 的 delta 才是核心 claim。

---

**[AGREE] R1-W5: Specificity control 效果有限**

Table A12 (specificity_control): top-24 vs bottom-24 overlap 16 heads，d ratio 1.15× 确实modest。KL ratio (1.56×) 稍好但仍非 dramatic。论文自己的措辞 "graded, attention-ordered contribution" 已经是 conservative claim，与这一有限的 specificity 一致。但 R1 有理由指出这不构成 strong specificity evidence。

---

**[AGREE] R1-W6: 单模型范围**

与我的 N1 完全一致。这是本文最大的局限性之一。

---

### 总结

| R1 条目 | 我的判断 | 严重度调整建议 |
|---------|---------|--------------|
| N1 (ablation R² contradiction) | AGREE with qualification | 降为 W-level；routing claim 有五条独立证据，R² 是其中之一 |
| N2 ("causal" terminology) | AGREE with nuance | 降为 W-level；符合 interp 惯例，但 CoRL 语境下应改措辞 |
| N3 (counterfactual ordering) | AGREE on data, REBUT on inference | 维持 W-level；ordering 问题成立，但 "language ignored" 推断不成立 |
| N4 (statistical power) | AGREE | 维持 N-level；underpowered n.s. → negative conclusion 是 inferential error |
| W1 (probe overparameterization) | REBUT | Appendix A.8 已充分回应 |
| W2 (independence assumption) | AGREE partially | 维持 W-level |
| W3 (Cohen's d autocorrelation) | AGREE | 维持 W-level |
| W4 (Llama-2 base control) | AGREE partially | 维持 W-level；替代解释 plausible 但不影响 delta |
| W5 (specificity control) | AGREE | 维持 W-level |
| W6 (single model) | AGREE | 与我的 N1 一致 |

**与 R1 的主要分歧**：R1 的 N1 和 N2 我认为应降级——N1 因为 routing claim 的证据不只依赖 ablation R²；N2 因为术语使用符合 interp 领域惯例。R1 的 N3 推断（"supports language ignored"）与数据不符。R1 的 N4 我完全同意。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-19T00:59:43.674746+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'completed', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 (方法严谨性+实验设计) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 1 返回 Round 1 审稿结果'}, {'content': '收集 Reviewer 2 (新颖性+叙事+CoRL适配) Round 1 审稿结果', 'status': 'completed', 'activeForm': '等待 Reviewer 2 返回 Round 1 审稿结果'}, {'content': 'Step 2: 交叉分享——将各 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享与逐条回应收集'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'completed', 'activeForm': '分析 Reviewer 间共识与分歧'}, {'content': 'Step 4: 汇总报告 + Issue Tracker 更新 + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-19T00:59:43.675204+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---
