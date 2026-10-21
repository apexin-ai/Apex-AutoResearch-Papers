# Reviewer 1 coordination — Part 1 of 8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/ed/ed9cd9e2adfd642813e6.json)

## Round 1

## Round 1

70 recorded events


### User

_source line 1 · 2026-05-14T12:03:50.707019+00:00_

[Round 1 审稿请求]:
## R1 审稿任务：方法与实验

**论文**："Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"

**论文概要**：本文系统比较了 5 种 confidence signal（sequence log-probability、soft Jaccard、Fleiss' Kappa、exact-match voting、entity-level majority voting）在结构化信息抽取（NER + RE）test-time scaling 中的表现。核心发现是负面结果：multi-sampling consistency 在任何 NER 数据集上都不优于 single-pass log-probability，尽管需要 8× 推理开销。

**你的审稿重点**：方法设计的严谨性 + 实验的充分性

请围绕以下维度评审：
1. **方法定义清晰度**：5 种 confidence signal 的定义是否严格？log-prob 的使用方式（Eq.1 定义在 greedy output 上 vs best-of-N 需要对每个 sample 打分）是否存在歧义？
2. **实验设计**：3 NER 数据集 (SciERC/CoNLL/WNUT) + SciERC RE、2 模型 (Qwen3-8B/LLaMA-3.1-8B)、N-scaling (8→16)、temperature (0.7/1.0)、difficulty stratification、OOD — 覆盖是否充分？有哪些关键遗漏？
3. **评估指标**：Spearman ρ、AUROC、Kendall τ、ECE、best-of-N F1 — 是否全面？统计检验是否充分？
4. **结果可信度**：数值是否内部一致？Table 4 的 cost comparison (log-prob "0×" vs consistency "N×") 是否准确/误导？
5. **消融/诊断实验**：LOO-SJ circularity check、per-relation-type RE 分析、inverted-U stratification — 是否有遗漏的关键消融？
6. **可视化**：论文只有表格没有图表（无 selection curve、reliability diagram、cost-effectiveness scatter）——这是否为重大缺陷？

**实验设计参考**（完整实验列表，共 15 个）：
- baseline_logprob, baseline_exact_match, baseline_entity_voting, evaluation_metrics_expansion
- ner_n16_scierc, ner_conll2003, ner_wnut17
- re_diagnostic_analysis, temperature_sensitivity, adaptive_compute_demo
- ner_multi_model, re_n16_confirmation, capability_stratification
- selection_curves, ner_ood_robustness

请检查论文对这 15 个实验的覆盖度。

请输出：3-5 个 strengths、5-8 个 weaknesses，每个带具体引用（表号/节号/数值），最后给出初步评分（1-6 scale，1=Strong Reject, 6=Strong Accept）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-14T12:03:59.917085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-14T12:04:00.124315+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 207
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-14T12:04:00.124782+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-14T12:04:00.175450+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-14T12:04:04.950001+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-14T12:04:05.803790+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-14T12:04:06.055243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296/CLAUDE.md",
  "offset": "0",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296/CLAUDE.md",
    "offset": "0",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-14T12:04:06.107679+00:00_

0	## 当前项目
1	当前绑定项目：**struct_self_consist_ie**
2	
3	今天是 **2026-05-14**。
4	
5	你是 ML 研究团队的论文审稿人（Reviewer 1）。**始终用中文回复。**
6	
7	## 你的角色
8	
9	你模拟真实的学术同行评审人，对论文进行深度审查。你的审查意见应达到真实 reviewer 的水准——不是走流程的表面检查，而是找到真正会影响接收决定的问题。
10	
11	**你不修改论文内容**——发现问题后通过 `review_reviewer_post_to_director` 汇报。
12	
13	## 审查侧重
14	
15	你的具体审查侧重由 Review Director 在任务消息中指定。严格按照 Director 的指示执行，不要自行扩大或缩小审查范围。
16	
17	## 多轮审稿
18	
19	你可能会被 Director 要求进行多轮审稿：
20	- Director 可能转发另一位 Reviewer 的**完整审稿原文**，请你逐条回应
21	- 回应格式：`[AGREE]` 或 `[REBUT]`，附理由和证据（cite 具体 Section/Table/Figure）
22	- 后续轮次应聚焦 Director 指出的具体问题，而非重复全面审查
23	
24	### 交叉回应格式
25	
26	```
27	[AGREE] R{X}-Issue-{N}: <同意理由，可补充自己的发现>
28	[REBUT] R{X}-Issue-{N}: <反驳理由，必须 cite 原文证据>
29	```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-14T12:04:13.890070+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-14T12:04:13.940769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-14T12:04:20.240301+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
  "pages": "1-5",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
    "pages": "1-5",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-14T12:04:22.115329+00:00_

Error: result (2,581,726 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760261995.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760261995.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760261995.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1875
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-14T12:04:27.953602+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-14T12:04:28.659580+00:00_

Error: result (407,542 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-14T12:04:28.811309+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
  "pages": "2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
    "pages": "2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-14T12:04:29.361474+00:00_

Error: result (535,202 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760269303.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760269303.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760269303.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 550
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-14T12:04:37.399483+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); r=json.loads(d['result']); print(type(r)); [print(k) for k in (r.keys() if isinstance(r,dict) else range(min(3,len(r))))]\" 2>/dev/null || cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); print(d['result'][:500])\"",
  "description": "Probe structure of pdf_to_images output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); r=json.loads(d['result']); print(type(r)); [print(k) for k in (r.keys() if isinstance(r,dict) else range(min(3,len(r))))]\" 2>/dev/null || cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); print(d['result'][:500])\"",
    "description": "Probe structure of pdf_to_images output"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-14T12:04:37.600561+00:00_

&lt;class 'dict'>
success
data
error
metadata

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-14T12:04:42.528634+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nfor page in r['data']:\n    print(page.get('path','no path'), page.get('page','?'))\n\"",
  "description": "Extract image file paths from pdf_to_images output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nfor page in r['data']:\n    print(page.get('path','no path'), page.get('page','?'))\n\"",
    "description": "Extract image file paths from pdf_to_images output"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-14T12:04:42.882061+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    print(page.get('path','no path'), page.get('page','?'))
          ^^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-14T12:04:48.257088+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint(type(r['data']))\nif isinstance(r['data'], dict):\n    print(list(r['data'].keys())[:5])\nelif isinstance(r['data'], list):\n    print(len(r['data']))\n    print(type(r['data'][0]))\n    if isinstance(r['data'][0], str):\n        print(r['data'][0][:200])\n    else:\n        print(r['data'][0])\nprint('metadata:', r.get('metadata'))\n\"",
  "description": "Inspect data structure of pdf_to_images output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint(type(r['data']))\nif isinstance(r['data'], dict):\n    print(list(r['data'].keys())[:5])\nelif isinstance(r['data'], list):\n    print(len(r['data']))\n    print(type(r['data'][0]))\n    if isinstance(r['data'][0], str):\n        print(r['data'][0][:200])\n    else:\n        print(r['data'][0])\nprint('metadata:', r.get('metadata'))\n\"",
    "description": "Inspect data structure of pdf_to_images output"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-14T12:04:48.458253+00:00_

&lt;class 'dict'>
['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']
metadata: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-14T12:04:53.935554+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nprint('total_pages:', data['total_pages'])\nprint('rendered_pages:', data['rendered_pages'])\nprint('output_dir:', data['output_dir'])\nimgs = data['images']\nprint('num images:', len(imgs))\nfor img in imgs:\n    if isinstance(img, dict):\n        print({k:v[:80] if isinstance(v,str) and len(v)>80 else v for k,v in img.items()})\n    elif isinstance(img, str):\n        print(img[:200])\n\"",
  "description": "Extract image paths from pdf_to_images output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nprint('total_pages:', data['total_pages'])\nprint('rendered_pages:', data['rendered_pages'])\nprint('output_dir:', data['output_dir'])\nimgs = data['images']\nprint('num images:', len(imgs))\nfor img in imgs:\n    if isinstance(img, dict):\n        print({k:v[:80] if isinstance(v,str) and len(v)>80 else v for k,v in img.items()})\n    elif isinstance(img, str):\n        print(img[:200])\n\"",
    "description": "Extract image paths from pdf_to_images output"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-14T12:04:54.037430+00:00_

total_pages: 12
rendered_pages: 1
output_dir: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images
num images: 1
{'page': 1, 'path': '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/', 'base64': 'iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAASn+klE', 'width': 1241, 'height': 1754, 'size_kb': 298.1}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-14T12:04:58.604283+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nfor img in data['images']:\n    print(img['path'])\n\"",
  "description": "Get full image path"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760268437.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nfor img in data['images']:\n    print(img['path'])\n\"",
    "description": "Get full image path"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-14T12:04:59.357580+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-14T12:04:59.508773+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/ 2>/dev/null",
  "description": "List rendered PDF images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/ 2>/dev/null",
    "description": "List rendered PDF images"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-14T12:04:59.559565+00:00_

paper_p1.png
paper_p2.png
paper_p3.png
paper_p4.png
paper_p5.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-14T12:05:03.880053+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
  "pages": "3-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
    "pages": "3-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-14T12:05:05.829007+00:00_

Error: result (3,645,759 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760305643.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760305643.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/895b54e3-3b00-48e8-9096-3952e43997a1/tool-results/mcp-agent-ml-research-pdf_to_images-1778760305643.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1948
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-14T12:05:08.592603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/",
  "description": "Verify all pages rendered"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/",
    "description": "Verify all pages rendered"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-14T12:05:08.643291+00:00_

paper_p1.png
paper_p10.png
paper_p11.png
paper_p12.png
paper_p2.png
paper_p3.png
paper_p4.png
paper_p5.png
paper_p6.png
paper_p7.png
paper_p8.png
paper_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-14T12:05:12.008692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-14T12:05:12.511172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-14T12:05:15.176242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3167
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-14T12:05:15.177395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2666
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-14T12:05:15.328673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-14T12:05:15.533330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-14T12:05:15.533797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-14T12:05:15.684628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-14T12:05:16.139831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-14T12:05:16.698404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1164
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-14T12:05:16.700465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1167
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-14T12:05:16.904653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1220
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-14T12:05:22.537641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-14T12:05:23.249249+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 711
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-14T12:05:23.304675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-14T12:05:23.811365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-14T12:05:24.312988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-14T12:05:25.219558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1914
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-14T12:05:25.220086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-14T12:05:25.423342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1611
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-14T12:05:25.429078+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1116
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-14T12:05:25.581118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-14T12:05:25.685525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 104
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-14T12:05:25.788837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 568
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-14T12:07:58.692538+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 59 · 2026-05-14T12:07:58.793303+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-14T12:08:03.260902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-14T12:08:03.713420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form scoring dimensions soundness excitement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form scoring dimensions soundness excitement 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-14T12:08:11.008630+00:00_

Web search results for query: "ACL ARR review form scoring dimensions soundness excitement 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ACL ARR review form scoring dimensions:

## Scoring Dimensions (as of February 2025)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness

Soun
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7295
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-14T12:08:15.383193+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I've found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

The reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based o
…[truncated 2507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 12122
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-14T12:08:18.144313+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 65 · 2026-05-14T12:08:18.144751+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-14T12:08:22.471537+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their scales (1-5, 1-6, etc.), and the exact meaning of each score level. I need every dimension name, every score option, and the complete text description for each score level. Also extract any guidelines about what constitutes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their scales (1-5, 1-6, etc.), and the exact meaning of each score level. I need every dimension name, every score option, and the complete text description for each score level. Also extract any guidelines about what constitutes a good review."
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-14T12:08:31.769702+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence** (Scale: 1-5)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## 2. **Soundness** (Scale: 1-5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (Scale: 1-5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment** (Scale: 1-5)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **
…[truncated 1850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9298
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-14T12:11:39.089517+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 审稿意见：方法与实验\n\n### 总体评分\n**Overall Assessment**: 3/5 (Findings) | Director 1-6 scale: **4/6** (Weak Accept, borderline Findings)\n**一句话总结**: 实验覆盖面广、诊断分析有深度的 empirical study，但模型规模单一（仅 8B）、零图表的呈现方式、以及误导性的成本分析共同削弱了核心主张的说服力。\n\n### ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法论合理，评估协议（4 指标 + LOO circularity check）良好；但成本分析存在误导，仅 2 个 8B 模型限制普适性 |\n| Excitement | 3/5 | 研究问题及时（TTS for structured IE），compound error boundary 有启发性；但贡献以 empirical comparison 为主 |\n| Reproducibility | 4/5 | 数据集公开、参数详尽；但未发布代码，prompt 模板未给出 |\n| Confidence | 4/5 | 熟悉 NER/RE 评估和 TTS 方法 |\n\n---\n\n### 主要优势\n\n**S1. 系统且全面的实验矩阵**\n5 种 signal × 3 NER 数据集 × 1 RE 数据集 × 2 模型 × 2 采样预算 × 2 温度 × 4 评估指标。15 个计划实验中 13/15 完整覆盖，2/15 部分覆盖（adaptive_compute_demo 隐含在 Section 5.2/5.5 但无显式 adaptive 策略；selection_curves 数据在 Table 8 但以表格呈现）。该领域首个如此系统的比较。\n\n**S2. LOO-SJ circularity check 是方法论亮点**\nTable 1 中 Leave-one-out SJ（ρ=0.40, Δ=0.02 vs full SJ ρ=0.42）证明 SJ 有效性不依赖于自我循环。严谨。\n\n**S3. Compound error boundary 诊断有理论价值**\nSection 5.9 识别 RE 中所有 signal 退化（ρ < 0.28）的根因是 compound error propagation（head + tail + relation type 三重叠加），Table 12 per-relation-type 分析提供具体证据。\n\n**S4. 多维度鲁棒性验证**\nMulti-seed（Table 2, Std ≤ 0.01）、cross-dataset（Table 4, 排序一致）、cross-model（Table 5）、OOD（Table 17, SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。\n\n**S5. Inverted-U pattern（Section 5.11, Table 15）**\nSJ ρ 在 F1 bucket [0.3, 0.7] 最高（ρ ≈ 0.45），极端区间下降。为 SJ 适用条件提供直觉。\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 模型规模单一，严重限制普适性\n- Section 4, Section 7\n- 仅 Qwen3-8B 和 LLaMA-3.1-8B 两个 8B 模型。confidence calibration 和 output diversity 随模型规模变化显著。更大模型的 greedy 可能已足够准确（LP 优势更明显），更小模型高方差可能放大 SJ 优势。Abstract 中 \"establish\" 措辞过强。\n- 建议：至少增加一个 >30B 或 <3B 模型，或降级措辞。\n\n**N2** [critical] 成本分析系统性误导\n- Section 6 \"Practical implications\"\n- 称 SJ 额外成本 \"negligible (O(N²) set comparisons vs. O(N) LLM forward passes)\"，但忽略 LP 可在 greedy decode（1 pass）上工作，而 SJ 需要 N≥8 pass。公平对比：LP@N=1 → ρ≈0.26; SJ@N=8 → 8× cost → ρ≈0.38; SJ@N=16 → 16× cost → ρ≈0.42。将 8-16× 推理开销描述为 \"negligible\" 是不准确的。\n- 建议：增加 cost-effectiveness 分析（F1 gain per unit compute）。\n\n**N3** [critical] 全文零图表\n- 17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。\n- 建议：至少添加 3 个核心 Figure。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] 未探索 signal combination\n- Section 5.8 发现 SJ 和 LP 互补（NER Δρ=0.14），但未尝试任何组合策略。\n- 建议：至少尝试 α·SJ + (1-α)·LP 线性组合。\n\n**W2** [warning] 单一 prompt 模板，缺乏 prompt sensitivity\n- Section 4 未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。\n- 建议：appendix 中给出完整 prompt，讨论 format 影响。\n\n**W3** [warning] RE 仅有 SciERC 一个数据集\n- NER 有 3 个跨域数据集，RE 只有 1 个。\"universal bottleneck\" 主张建立在单一数据集上。\n- 建议：增加至少一个 RE 数据集或降级措辞。\n\n**W4** [warning] 统计检验不系统\n- Section 5.1 提到 p < 10⁻¹⁵，但 Table 4/5 的 cross-dataset/cross-model 比较无检验。3 seed 的 std 不能替代正式统计检验。\n- 建议：对核心比较报告 bootstrap 95% CI。\n\n**W5** [warning] 缺少 SJ 失败案例分析\n- SJ ρ 最佳也仅 0.42-0.51。未分析高 SJ 低 F1（模型一致地错）或低 SJ 高 F1 的失败模式。\n- 建议：增加 error analysis subsection。\n\n---\n\n### 小问题\n- 标题 \"Log-Probability Is All You Need?\" 暗示答案为 yes，但实际结论为 no。建议改为 \"Beyond Log-Probability: ...\"。\n- Table 16（Appendix）entity count 6+ 时 SJ ρ 降至 0.34，未解释原因。\n- Eq.(1) SJ 的 similarity kernel（token-level overlap 的具体方式）未明确。\n- adaptive_compute_demo 实验无显式 adaptive 策略呈现。\n\n### 15 个实验覆盖度\n13/15 完整覆盖，2/15 部分覆盖（adaptive_compute_demo、selection_curves）。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 审稿意见：方法与实验\n\n### 总体评分\n**Overall Assessment**: 3/5 (Findings) | Director 1-6 scale: **4/6** (Weak Accept, borderline Findings)\n**一句话总结**: 实验覆盖面广、诊断分析有深度的 empirical study，但模型规模单一（仅 8B）、零图表的呈现方式、以及误导性的成本分析共同削弱了核心主张的说服力。\n\n### ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法论合理，评估协议（4 指标 + LOO circularity check）良好；但成本分析存在误导，仅 2 个 8B 模型限制普适性 |\n| Excitement | 3/5 | 研究问题及时（TTS for structured IE），compound error boundary 有启发性；但贡献以 empirical comparison 为主 |\n| Reproducibility | 4/5 | 数据集公开、参数详尽；但未发布代码，prompt 模板未给出 |\n| Confidence | 4/5 | 熟悉 NER/RE 评估和 TTS 方法 |\n\n---\n\n### 主要优势\n\n**S1. 系统且全面的实验矩阵**\n5 种 signal × 3 NER 数据集 × 1 RE 数据集 × 2 模型 × 2 采样预算 × 2 温度 × 4 评估指标。15 个计划实验中 13/15 完整覆盖，2/15 部分覆盖（adaptive_compute_demo 隐含在 Section 5.2/5.5 但无显式 adaptive 策略；selection_curves 数据在 Table 8 但以表格呈现）。该领域首个如此系统的比较。\n\n**S2. LOO-SJ circularity check 是方法论亮点**\nTable 1 中 Leave-one-out SJ（ρ=0.40, Δ=0.02 vs full SJ ρ=0.42）证明 SJ 有效性不依赖于自我循环。严谨。\n\n**S3. Compound error boundary 诊断有理论价值**\nSection 5.9 识别 RE 中所有 signal 退化（ρ < 0.28）的根因是 compound error propagation（head + tail + relation type 三重叠加），Table 12 per-relation-type 分析提供具体证据。\n\n**S4. 多维度鲁棒性验证**\nMulti-seed（Table 2, Std ≤ 0.01）、cross-dataset（Table 4, 排序一致）、cross-model（Table 5）、OOD（Table 17, SJ-LP gap 从 +0.15 降至 +0.12 但仍显著）。\n\n**S5. Inverted-U pattern（Section 5.11, Table 15）**\nSJ ρ 在 F1 bucket [0.3, 0.7] 最高（ρ ≈ 0.45），极端区间下降。为 SJ 适用条件提供直觉。\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 模型规模单一，严重限制普适性\n- Section 4, Section 7\n- 仅 Qwen3-8B 和 LLaMA-3.1-8B 两个 8B 模型。confidence calibration 和 output diversity 随模型规模变化显著。更大模型的 greedy 可能已足够准确（LP 优势更明显），更小模型高方差可能放大 SJ 优势。Abstract 中 \"establish\" 措辞过强。\n- 建议：至少增加一个 >30B 或 <3B 模型，或降级措辞。\n\n**N2** [critical] 成本分析系统性误导\n- Section 6 \"Practical implications\"\n- 称 SJ 额外成本 \"negligible (O(N²) set comparisons vs. O(N) LLM forward passes)\"，但忽略 LP 可在 greedy decode（1 pass）上工作，而 SJ 需要 N≥8 pass。公平对比：LP@N=1 → ρ≈0.26; SJ@N=8 → 8× cost → ρ≈0.38; SJ@N=16 → 16× cost → ρ≈0.42。将 8-16× 推理开销描述为 \"negligible\" 是不准确的。\n- 建议：增加 cost-effectiveness 分析（F1 gain per unit compute）。\n\n**N3** [critical] 全文零图表\n- 17 个表格，0 个 Figure。对 confidence/calibration 研究而言，缺少 selection curves、reliability diagrams、cost-effectiveness scatter 是严重呈现缺陷。Table 8 有 selection curve 数据但以表格呈现。\n- 建议：至少添加 3 个核心 Figure。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] 未探索 signal combination\n- Section 5.8 发现 SJ 和 LP 互补（NER Δρ=0.14），但未尝试任何组合策略。\n- 建议：至少尝试 α·SJ + (1-α)·LP 线性组合。\n\n**W2** [warning] 单一 prompt 模板，缺乏 prompt sensitivity\n- Section 4 未提及 prompt 变体。LLM-based IE 输出格式直接影响 set-based 指标。\n- 建议：appendix 中给出完整 prompt，讨论 format 影响。\n\n**W3** [warning] RE 仅有 SciERC 一个数据集\n- NER 有 3 个跨域数据集，RE 只有 1 个。\"universal bottleneck\" 主张建立在单一数据集上。\n- 建议：增加至少一个 RE 数据集或降级措辞。\n\n**W4** [warning] 统计检验不系统\n- Section 5.1 提到 p < 10⁻¹⁵，但 Table 4/5 的 cross-dataset/cross-model 比较无检验。3 seed 的 std 不能替代正式统计检验。\n- 建议：对核心比较报告 bootstrap 95% CI。\n\n**W5** [warning] 缺少 SJ 失败案例分析\n- SJ ρ 最佳也仅 0.42-0.51。未分析高 SJ 低 F1（模型一致地错）或低 SJ 高 F1 的失败模式。\n- 建议：增加 error analysis subsection。\n\n---\n\n### 小问题\n- 标题 \"Log-Probability Is All You Need?\" 暗示答案为 yes，但实际结论为 no。建议改为 \"Beyond Log-Probability: ...\"。\n- Table 16（Appendix）entity count 6+ 时 SJ ρ 降至 0.34，未解释原因。\n- Eq.(1) SJ 的 similarity kernel（token-level overlap 的具体方式）未明确。\n- adaptive_compute_demo 实验无显式 adaptive 策略呈现。\n\n### 15 个实验覆盖度\n13/15 完整覆盖，2/15 部分覆盖（adaptive_compute_demo、selection_curves）。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-14T12:11:43.362161+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4272
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-14T12:11:49.794274+00:00_

审稿意见已提交给 Review Director。

总结：本文在方法与实验维度上给出 **Overall 3/5 (Findings) / Director scale 4/6 (Weak Accept)**。核心优势是系统的实验矩阵（13/15 实验覆盖）、LOO circularity check、compound error boundary 诊断。三个 critical 问题：(1) 仅 8B 模型限制了 "establish best practice" 主张的普适性；(2) 成本分析将 8-16× 推理开销描述为 "negligible" 属于误导；(3) 全文零图表不符合 confidence/calibration 研究惯例。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

18 recorded events


### User

_source line 71 · 2026-05-14T12:13:49.418346+00:00_

[Round 1 审稿请求]:
## 交叉分享：请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2（新颖性与相关工作方向）的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## R2 审稿意见：新颖性与相关工作

### 总体评分
**Overall**: 3/5 (Findings)
**一句话总结**: 实验设计扎实的经验研究，但方法新颖性有限（SJ 是评估指标的自然迁移），RE 上的 task-complexity boundary claim 仅由单一数据集支撑，相关工作存在显著遗漏。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | NER claims 有多 seed + 多数据集 + p-value 支撑；RE complexity boundary 仅基于 SciERC 一个数据集(n=397)，证据链不完整 |
| Excitement | 2.5/5 | 研究问题实用，但核心发现（set-level agreement > sequence-level log-prob）对领域内可预期；"diagnostic framework" 实为标准消融包装 |
| Overall | 3/5 | Findings 水平——有用的经验贡献但不够 Main 的新颖性门槛 |
| Reproducibility | 4/5 | 方法清晰、超参明确、多 seed，但未提供代码 |
| Confidence | 4/5 | 熟悉 self-consistency、calibration、NER/RE 文献 |

### Must-Fix 问题

**N1** [critical] 方法新颖性有限——SJ 是 IE 评估指标到 confidence 的自然迁移
- Section 3.2, Eq(1): type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本
- 未提供理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融

**N2** [critical] Task-complexity boundary 证据严重不足
- Section 5.9, Table 12: 全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行
- "Universal bottleneck" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis

**N3** [critical] 相关工作显著遗漏
- **Guo et al. 2017** (On Calibration of Modern Neural Networks, ICML) — 论文讨论 ECE 但未引用定义 ECE 的奠基论文
- **Snell et al. 2024** (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却未引用该核心工作
- **Aggarwal et al. 2023** (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling (Section 5.2) 直接相关
- **CISC** (Huang et al. 2025, Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 "最 calibrated 的方法反而最无效"，直接挑战本文解读
- **传统 IE confidence** — CRF 边际概率、span-level confidence、MC-dropout uncertainty 完全未讨论

**N4** [critical] 标题与核心发现不匹配
- "Log-Probability Is All You Need?" 暗示 log-prob 可能足够，但论文核心发现是 SJ 显著优于 log-prob (Δρ=0.16, p<10⁻²⁵)
- 修辞反问制造阅读期望与实际结论的认知冲突

### Should-Fix 问题

**W1** [warning] 仅 2 个 8B 模型，70B+ 模型的 calibration 可能改变 SJ vs log-prob 的差距
**W2** [warning] 未比较任何 trained approach (verifier/reward model/learned combination)
**W3** [warning] "Diagnostic framework" 过度包装——实际是标准 error analysis (F1 分桶、component 分解、stratification)
**W4** [warning] 全文 17 张表 0 张图，可读性差
**W5** [warning] Exact-Match Voting 对结构化输出是 straw man baseline

### 小问题
- Abstract 有 "?" 未解析引用
- 仅英语数据集
- 温度敏感性分析仅 T=0.7 和 T=1.0 两点

### 主要优势
- S1: 研究问题清晰且有实际意义
- S2: 实验设计系统化
- S3: SJ 的 Hungarian matching 设计合理，leave-one-out 验证排除 circularity
- S4: Best-of-N selection 将 ranking → F1 gain，实用性强
- S5: 消融维度全面

### 对 Director 问题的回应

**1. "首个系统比较" claim 是否成立？**
基本成立但需限定。建议改为 "first systematic comparison for LLM-based structured IE"。

**2. 负面结果信息量？**
论文核心发现实际上是正面结果（SJ > log-prob）。RE 退化是次要发现，仅单数据集支撑。

**3. Diagnostic framework 贡献是否充分？**
不充分。标准消融技术不构成可复用 framework。建议降格为 "diagnostic analysis"。

**4. EMNLP 定位？**
Findings 可接受，Main 偏弱。

---

请对以上每个 Must-Fix（N1-N4）、Should-Fix（W1-W5）和小问题逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-14T12:13:59.757415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-14T12:14:00.763981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-14T12:14:00.764573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-14T12:14:01.169494+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-14T12:14:03.434744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2670
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-14T12:14:03.586091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2416
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-14T12:14:08.209537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-14T12:14:09.266340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-14T12:14:09.471016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-14T12:14:09.622401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-14T12:14:10.129294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-14T12:14:10.332999+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-14T12:14:16.321416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-14T12:14:16.323210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-14T12:16:43.184331+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 的交叉回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: SJ 新颖性有限**\n同意。SJ 是 set-level Jaccard 的直接 confidence 化应用。论文定位为 empirical study 但措辞（\"establish\", \"diagnostic framework\"）暗示更高原创性。补充：缺少 similarity kernel 消融（token overlap vs edit distance vs embedding cosine），这同时是实验完备性问题。\n\n**[AGREE] R2-N2: Task-complexity boundary 证据不足**\n完全同意（与 R1-W3 一致）。SciERC RE 仅 6 relation types, n=397。\"Universal bottleneck\" 需降级。但补充：Section 5.9 conditional analysis（RE conditional on NER F1≥1）提供了 compound error 机制的初步因果证据，分析方法本身有价值。\n\n**[AGREE] R2-N3: 相关工作遗漏**\n逐条核实 pages 9-11 引用列表确认：\n- Guo et al. 2017 (ECE 定义)：严重遗漏，论文用 ECE 作核心指标却未引\n- Snell et al. 2024 (Scaling TTS)：严重遗漏，标题围绕 TTS 却缺核心引用\n- Aggarwal et al. 2023 (Adaptive-Consistency)：同意，与 N-scaling 直接相关\n- CISC (Huang et al. 2025)：同意，与 calibration + consistency 结论存在张力\n- 传统 IE confidence：部分同意——scope 限于 LLM-based IE 合理，但应用一两句话说明排除理由\n\n**[REBUT] R2-N4: 标题不匹配 → 应降为 should-fix**\n标题用问号是修辞反问，abstract 第一句即引导质疑 log-prob 充分性。不理想但不影响接收决定。R1 已列为小问题。\n\n### Should-Fix\n\n**[AGREE] R2-W1: 仅 8B 模型** — 与 R1-N1 一致，我列为 critical。\n**[REBUT] R2-W2: 未比较 trained approach** — 论文 scope 明确限定为 training-free signals（Section 7, Limitations），合理。但应在 Related Work 中更充分讨论 trained approaches 作为 upper bound。降级为 Related Work 补充问题。\n**[AGREE] R2-W3: \"Diagnostic framework\" 过度包装** — 标准消融技术，建议降格为 \"diagnostic analysis\"。\n**[AGREE] R2-W4: 零图表** — 与 R1-N3 一致。\n**[REBUT] R2-W5: EM 是 straw man** — EM 是 Wang et al. (2023a) SC 的原始实现。Table 9 (NER EM rate=6%, RE=1.5%) 量化了 SC 在结构化输出上的失效，本身是有信息量的实证发现。\n\n### 小问题\n- Abstract \"?\" 引用：AGREE\n- 英语数据集：AGREE\n- 温度两点：REBUT — T=0.7/1.0 覆盖实践常用范围，Table 14 显示 SJ Δ=0.015，两点足以支撑有限主张。\n\n### 对 Director 问题\n1. \"首个系统比较\"：同意 R2，需限定为 \"for LLM-based structured IE\"\n2. 负面结果：同意 R2 修正——核心发现是正面结果（SJ > LP on NER）。Director 原始描述与论文实际结论矛盾。\n3. Diagnostic framework：同意降格为 \"diagnostic analysis\"\n4. 定位：Findings 可接受，Main 偏弱。核心障碍：(a) 模型规模单一 (b) 零图表 (c) 成本分析误导 (d) RE 证据不足\n\n### R1 综合评分维持\nOverall 3/5 (Findings) | 1-6 scale: 4/6 (Weak Accept, borderline Findings)",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 的交叉回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: SJ 新颖性有限**\n同意。SJ 是 set-level Jaccard 的直接 confidence 化应用。论文定位为 empirical study 但措辞（\"establish\", \"diagnostic framework\"）暗示更高原创性。补充：缺少 similarity kernel 消融（token overlap vs edit distance vs embedding cosine），这同时是实验完备性问题。\n\n**[AGREE] R2-N2: Task-complexity boundary 证据不足**\n完全同意（与 R1-W3 一致）。SciERC RE 仅 6 relation types, n=397。\"Universal bottleneck\" 需降级。但补充：Section 5.9 conditional analysis（RE conditional on NER F1≥1）提供了 compound error 机制的初步因果证据，分析方法本身有价值。\n\n**[AGREE] R2-N3: 相关工作遗漏**\n逐条核实 pages 9-11 引用列表确认：\n- Guo et al. 2017 (ECE 定义)：严重遗漏，论文用 ECE 作核心指标却未引\n- Snell et al. 2024 (Scaling TTS)：严重遗漏，标题围绕 TTS 却缺核心引用\n- Aggarwal et al. 2023 (Adaptive-Consistency)：同意，与 N-scaling 直接相关\n- CISC (Huang et al. 2025)：同意，与 calibration + consistency 结论存在张力\n- 传统 IE confidence：部分同意——scope 限于 LLM-based IE 合理，但应用一两句话说明排除理由\n\n**[REBUT] R2-N4: 标题不匹配 → 应降为 should-fix**\n标题用问号是修辞反问，abstract 第一句即引导质疑 log-prob 充分性。不理想但不影响接收决定。R1 已列为小问题。\n\n### Should-Fix\n\n**[AGREE] R2-W1: 仅 8B 模型** — 与 R1-N1 一致，我列为 critical。\n**[REBUT] R2-W2: 未比较 trained approach** — 论文 scope 明确限定为 training-free signals（Section 7, Limitations），合理。但应在 Related Work 中更充分讨论 trained approaches 作为 upper bound。降级为 Related Work 补充问题。\n**[AGREE] R2-W3: \"Diagnostic framework\" 过度包装** — 标准消融技术，建议降格为 \"diagnostic analysis\"。\n**[AGREE] R2-W4: 零图表** — 与 R1-N3 一致。\n**[REBUT] R2-W5: EM 是 straw man** — EM 是 Wang et al. (2023a) SC 的原始实现。Table 9 (NER EM rate=6%, RE=1.5%) 量化了 SC 在结构化输出上的失效，本身是有信息量的实证发现。\n\n### 小问题\n- Abstract \"?\" 引用：AGREE\n- 英语数据集：AGREE\n- 温度两点：REBUT — T=0.7/1.0 覆盖实践常用范围，Table 14 显示 SJ Δ=0.015，两点足以支撑有限主张。\n\n### 对 Director 问题\n1. \"首个系统比较\"：同意 R2，需限定为 \"for LLM-based structured IE\"\n2. 负面结果：同意 R2 修正——核心发现是正面结果（SJ > LP on NER）。Director 原始描述与论文实际结论矛盾。\n3. Diagnostic framework：同意降格为 \"diagnostic analysis\"\n4. 定位：Findings 可接受，Main 偏弱。核心障碍：(a) 模型规模单一 (b) 零图表 (c) 成本分析误导 (d) RE 证据不足\n\n### R1 综合评分维持\nOverall 3/5 (Findings) | 1-6 scale: 4/6 (Weak Accept, borderline Findings)",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-14T12:16:47.363328+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4178
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-14T12:16:52.830769+00:00_

交叉回应已提交。

总结：R2 的 12 个论点中，我同意 8 个（N1、N2、N3、W1、W3、W4 + 2 个小问题），反驳 3 个（N4 应降级、W2 scope 合理、W5 EM 非 straw man），1 个温度点部分反驳。R1 综合评分维持 3/5 (Findings) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

50 recorded events


### User

_source line 89 · 2026-05-15T01:50:28.346308+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计有效性）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review, May cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL template (`\usepackage[review]{acl}`)，长文 8 页正文 + 无限参考文献 + 附录不计页
- **匿名规则**: Double-blind (作者已标注 Anonymous)

### 论文信息
- **标题**: "Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction"
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`
- **各 section 文件**: `docs/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex

### 你的审查侧重

**方法严谨性 + 实验设计 + 统计有效性**。重点关注：

1. **方法论**：
   - 5 个 confidence signal 的数学定义是否严谨、无歧义
   - Soft Jaccard 的 bipartite matching + Hungarian algorithm 是否正确形式化
   - Entity voting confidence 的定义是否合理（mean frequency vs. 其他聚合方式）
   - Instance-level vs per-sample signal 的区分是否清晰且有理论支撑

2. **实验设计**：
   - 数据集选择（SciERC、CoNLL-2003、WNUT-17）是否充分覆盖难度梯度
   - 模型选择（Qwen3-8B、LLaMA-3.1-8B）是否足够，8B 是否太小
   - N=8/16 的采样量是否充分，T=1.0 是否合理
   - Evaluation protocol：Spearman ρ + AUROC + best-of-N F1 三个指标是否全面
   - Greedy baseline 的公平性（T=0, N=1 vs T=1.0, N=8）

3. **统计有效性**：
   - p=0.39 的 bootstrap 检验是否正确执行
   - Cohen's d=0.038 报告是否充分
   - 3-seed ±std 是否足够，是否需要更多 seed
   - WNUT-17 的 p=0.106 是否应更谨慎解读
   - 置信区间的使用是否一致

4. **结果可复现性**：
   - 是否有足够的实现细节（LoRA 配置、vLLM 参数、prompt 格式等）
   - 数据预处理是否清晰

5. **格式合规**：
   - 页数是否在 8 页限制内
   - 表格/图表是否清晰可读
   - Limitations section 是否存在且充分

请按 EMNLP 顶会最严格标准评审，不留情面。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-15T01:50:38.811348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-15T01:50:38.912310+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-15T01:50:41.725959+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-15T01:50:41.776710+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-15T01:50:44.189723+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-15T01:50:44.246245+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-15T01:50:49.432221+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-15T01:50:49.482860+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-15T01:50:53.905696+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-15T01:50:54.257615+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-15T01:50:54.257981+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 101 · 2026-05-15T01:50:54.912319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL ARR review form dimensions soundness excitement overall assessment scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL ARR review form dimensions soundness excitement overall assessment scale"
  }
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-15T01:51:01.893763+00:00_

Web search results for query: "EMNLP 2026 ACL ARR review form dimensions soundness excitement overall assessment scale"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"PrivateNLP@ACL 2026","url":"https://sites.google.com/view/privatenlp2026/?pli=1"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) review form dimensions used for EMNLP 2026:

## Review Score Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness

Reviewers assess whether the work is sufficiently sound and thorough, and whether it clearly states scientific claims and provides adequate 
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6981
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-15T01:51:03.351375+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

I found comprehensive information about the ACL Rolling Review 2026 reviewer guidelines, review form, and scoring criteria. Here's what I found:

## Reviewer Guidelines & Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recomme
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9093
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-15T01:51:10.531937+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE scoring scales for all dimensions: soundness, excitement, overall assessment, confidence, reproducibility. List every score number and its description. Also extract any other required fields in the review form."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE scoring scales for all dimensions: soundness, excitement, overall assessment, confidence, reproducibility. List every score number and its description. Also extract any other required fields in the review form."
  }
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-15T01:51:12.391007+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, scoring criteria details, what constitutes a good/bad paper, any specific instructions about soundness, excitement, reproducibility, ethics checklist, limitations section requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, scoring criteria details, what constitutes a good/bad paper, any specific instructions about soundness, excitement, reproducibility, ethics checklist, limitations section requirements."
  }
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-15T01:51:12.894296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-15T01:51:13.848288+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-15T01:51:13.848739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-15T01:51:14.301295+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-15T01:51:14.352072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-15T01:51:14.805215+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpti
…[truncated 3524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-15T01:51:14.906206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-15T01:51:15.108437+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-15T01:51:15.159427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-15T01:51:15.210208+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Our primary model is \textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct}.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \mu
…[truncated 7771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-15T01:51:17.117889+00:00_

# ACL Rolling Review Scoring Scales

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully..."
- **4**: "Quite sure. I tried to check the important points carefully..."
- **3**: "Pretty sure, but there's a chance I missed something..."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed..."
- **1**: "Not my area, or paper is very hard to understand..."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen..."
- **4**: "Strong: This study provides sufficient support for all of its claims..."
- **3.5, 3, 2.5, 2, 1.5, 1**: Descending scale from acceptable to major issues

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend..."
- **4**: "Exciting: I would mention this paper to others and/or make an effort..."
- **3**: "Interesting: I might mention some points of this paper to others..."
- **2**: "Potentially Interesting: this paper does not resonate with me..."
- **1**: "Not Exciting: this paper does not resonate with me..."

## Overall Assessment
- **5**: "Consider for Award" (top 2.5%)
- **4**: "Conference: I think this paper could be accepted..."
- **3**: "Findings: I think this paper could be accepted to the Findings..."
- **2**: "Resubmit next cycle: needs substantial revisions..."
- **1**: "Do not resubmit: fully redone or irrelevant..."

## Reproducibility
- **5**: "They could easily reproduce the results"
- **4**: "Mostly reproduce, some variation possible"
- **3**: "Reproduce with some difficulty"
- **2**: "Hard to reproduce"
- **1**: "Unable to reproduce"

## Additional Required Fields
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Needs Ethics Review
- Datasets rating
- Software rating
- Author identity knowledge

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6585
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-15T01:51:33.082935+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Framework

ARR reviewers assess papers using **three distinct scores** (as of February 2025):

1. **Soundness**: Technical validity and methodological rigor. Reviews must justify low soundness scores with specific evidence.
2. **Excitement**: Personal interest level—orthogonal to soundness and purely subjective.
3. **Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact.

## What Reviewers Should Evaluate

### Key Assessment Areas

**Expertise & Fit Check**
- Assess whether you can competently review the paper
- Identify if author identity is known (disclose in review form)
- Check for academic conflicts of interest
- Specify any major sections you couldn't evaluate

**Technical Soundness**
- Verify methodology aligns with stated research questions
- Check formal proofs for completeness and correctness
- Assess experimental design and statistical rigor
- Validate claims against presented evidence

**Appropriateness**
- Confirm submission matches ARR's scope and CFP requirements
- Evaluate whether contribution type (models, resources, analysis, surveys) is legitimate

## Common Review Problems to Avoid

The guidelines identify 17 "heuristics" that often lead to biased reviews:

| Issue | Problem |
|-------|---------|
| **H1-H4** | Dismissing results as obvious, surprising, or unprecedented |
| **H5** | Rejecting papers lacking SOTA results when not claimed |
| **H6** | Penalizing negative/null results |
| **H7** | Criticizing simplicity when it solves the problem |
| **H8** | Requiring specific methodologies (e.g., deep learning) |
| **H9-H10** | Dismissing niche topics or non-English work |
| **H13-H15** | Demanding extra experiments beyond claim scope |
| **H16-H17** | Conflating limitations with weaknesses; using citations as validity metric |

## Common NLP Paper Problems to Flag

The guidelines specify issues reviewers *should* identify:

**Methodology 
…[truncated 4658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 20691
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-15T01:51:40.566063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-15T01:51:41.068517+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	
11	\paragraph{Why quality estimators fail as selectors.}
12	Quality estimation ranks \textit{instances} by expected output quality via output distribution entropy; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
13	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
14	The $\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\rho$; both metrics measure be
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-15T01:51:41.068990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-15T01:51:41.521074+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-15T01:51:41.521618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-15T01:51:42.024186+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-15T01:51:42.024670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-15T01:51:42.376690+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 9406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-15T01:51:42.427606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-15T01:51:42.478356+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	All target reasoning/QA with discrete answers.
9	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
13	However, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.
14	Our Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.
15	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie
…[truncated 1727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-15T01:51:51.369163+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-15T01:51:51.921908+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-15T01:51:52.022703+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/figures/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/figures/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-15T01:51:52.173852+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-15T01:51:59.812323+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-15T01:52:00.314679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-15T01:52:30.047322+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 46, \"total_citations\": 65, \"unique_cited_keys\": 46, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 43, \"online_not_found\": 2, \"online_mismatch\": 1}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 35625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 30234
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-15T01:52:30.098602+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 16730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 29783
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-15T01:56:30.269048+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n### 审查侧重：方法严谨性 + 实验设计 + 统计有效性\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 — Findings\n**一句话总结**: 研究问题清晰、实验设计规范，\"correlation-selection gap\"概念有价值，但仅限 8B 模型、单一 RE 数据集、统计检验细节不足，核心负面结论的证据强度不够支撑 Main Conference。\n\n## 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 五个 signal 定义基本严谨，实验设计合理，但 bootstrap 检验细节缺失、Soft Jaccard 形式化有歧义、logprob 温度敏感性缺失削弱了方法论完整性 |\n| Excitement | 3/5 | 质量估计 vs. 样本选择的解耦和 correlation-selection gap 概念有洞见；但核心结论是负面结果（signals 不优于 greedy），且实用指导有限 |\n| Reproducibility | 3.5/5 | 数据集公开、信号定义有公式，但 LoRA 配置仅给 r=32、prompt 格式未展示、vLLM 约束解码具体配置缺失、bootstrap 参数不明 |\n| Confidence | 4/5 | 与本文方向（uncertainty estimation + IE + test-time scaling）有扎实背景 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Bootstrap 检验细节严重不足，核心统计结论无法验证\n\n- 具体位置：Section 5.3, \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\"\n- 问题：论文的核心负面结论（\"no signal reliably surpasses greedy\"）完全建立在 p=0.39 这一 bootstrap 检验上，但以下关键细节未报告：(1) bootstrap 迭代次数；(2) 是 paired bootstrap 还是 unpaired；(3) 检验统计量是什么；(4) \"3-seed bootstrap\"的含义不明——是对 3 个 seed 做 bootstrap（n=3，完全无统计功效），还是在每个 seed 内对 instance 做 bootstrap 再合并？如果是前者，p=0.39 无任何诊断价值。\n- 为什么影响接收：这是支撑全文标题（\"Weak Selectors\"）和主要贡献（contribution #2）的唯一定量证据。\n\n**N2** [critical] 仅 8B 模型，\"model-agnostic\" claim 缺乏支撑\n\n- 具体位置：Section 5.1, 5.4, Discussion 多处使用\"model-agnostic\"\n- 问题：只测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct——同一参数规模。70B+ 模型可能产生更高质量更多样的样本，从根本上改变 correlation-selection gap 的形态。Limitations 承认了这一点，但 Discussion 仍使用\"model-agnostic\"措辞，形成内部矛盾（ARR R4 overclaiming）。\n\n**N3** [critical] RE 结论仅基于 SciERC，44% zero-F1 floor effect 严重扭曲信号评估\n\n- 具体位置：Section 5.1, Limitations 第 1 段\n- 问题：RE 的所有结论全部来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。论文声称覆盖\"NER and RE\"但 RE 实验基础极其薄弱。\n\n## Should-Fix 问题\n\n**W1** [warning] Soft Jaccard 形式化有歧义：g_i/g_j 未定义，sim 具体公式缺失，Hungarian algorithm 匹配阈值未说明。\n\n**W2** [warning] Entity voting 的 mean frequency 聚合方式未讨论替代选择（median、thresholded voting 等），当模型产生大量低频幻觉实体时 |E_∪| 膨胀导致置信度系统性偏低。\n\n**W3** [warning] ρ=0.38 被反复描述为\"effective/strong quality estimation\"但仅解释 ~14% F1 方差，未与 uncertainty estimation 文献中其他方法的 ρ 对比 contextualize。\n\n**W4** [warning] Logprob（唯一 per-sample signal、selection 最佳信号）的温度敏感性数据缺失（T=0.7 unavailable），但论文做出了\"signals robust across temperatures\"的笼统结论。\n\n**W5** [warning] WNUT-17 p=0.106 被解读为\"establishing the capability boundary where all signals break down\"，措辞过于确定——fail to reject null ≠ accept null。\n\n**W6** [warning] Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct（未说明是否微调）训练设置不对称，可能混淆 cross-model 比较。\n\n**W7** [warning] 约束解码对 sampling diversity 的影响未讨论——这可能是 correlation-selection gap 的一个成因。\n\n## 小问题\n\n- Table 2 EM \"---\" 需更显著的解释\n- Limitations 提到\"logistic regression proxy as an upper bound\"但正文/Appendix 无此分析结果\n- snell2024scaling bib 作者格式与 OpenAlex 有 mismatch\n- Cross-model Δ=0.005 未报告是否在 bootstrap CI 内\n- Introduction \"+18pp on GSM8K\" 未注明具体模型(PaLM-540B)\n- Appendix D \\textsc 编译检查\n\n## 主要优势\n\n1. 研究问题定义精准：quality estimation vs. sample selection 的解耦是有价值的概念贡献\n2. 实验设计的系统性出色：5 signals × 3 families × 3 datasets × 2 models × 2 N × 2 T + 多项辅助分析\n3. Task difficulty gradient 设计合理（CoNLL/SciERC/WNUT），信号排序随难度变化的发现有实用价值\n4. 统计实践总体规范（p-values, Cohen's d, CI, 3-seed, Fisher z-test, LOO circularity check）\n5. Limitations section 全面诚实\n\n## Overall Assessment\n\n**Verdict: Borderline → Weak Accept for Findings**\n\n核心顾虑：(1) bootstrap 细节不足以确认核心负面结论成立（N1）；(2) model-agnostic overclaim（N2）；(3) RE 结论基础薄弱（N3）。如果 N1 确认执行正确、N2/N3 做适当限定，适合 Findings。进入 Main Conference 需要额外模型规模或 RE 数据集验证。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n### 审查侧重：方法严谨性 + 实验设计 + 统计有效性\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 — Findings\n**一句话总结**: 研究问题清晰、实验设计规范，\"correlation-selection gap\"概念有价值，但仅限 8B 模型、单一 RE 数据集、统计检验细节不足，核心负面结论的证据强度不够支撑 Main Conference。\n\n## 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 五个 signal 定义基本严谨，实验设计合理，但 bootstrap 检验细节缺失、Soft Jaccard 形式化有歧义、logprob 温度敏感性缺失削弱了方法论完整性 |\n| Excitement | 3/5 | 质量估计 vs. 样本选择的解耦和 correlation-selection gap 概念有洞见；但核心结论是负面结果（signals 不优于 greedy），且实用指导有限 |\n| Reproducibility | 3.5/5 | 数据集公开、信号定义有公式，但 LoRA 配置仅给 r=32、prompt 格式未展示、vLLM 约束解码具体配置缺失、bootstrap 参数不明 |\n| Confidence | 4/5 | 与本文方向（uncertainty estimation + IE + test-time scaling）有扎实背景 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Bootstrap 检验细节严重不足，核心统计结论无法验证\n\n- 具体位置：Section 5.3, \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\"\n- 问题：论文的核心负面结论（\"no signal reliably surpasses greedy\"）完全建立在 p=0.39 这一 bootstrap 检验上，但以下关键细节未报告：(1) bootstrap 迭代次数；(2) 是 paired bootstrap 还是 unpaired；(3) 检验统计量是什么；(4) \"3-seed bootstrap\"的含义不明——是对 3 个 seed 做 bootstrap（n=3，完全无统计功效），还是在每个 seed 内对 instance 做 bootstrap 再合并？如果是前者，p=0.39 无任何诊断价值。\n- 为什么影响接收：这是支撑全文标题（\"Weak Selectors\"）和主要贡献（contribution #2）的唯一定量证据。\n\n**N2** [critical] 仅 8B 模型，\"model-agnostic\" claim 缺乏支撑\n\n- 具体位置：Section 5.1, 5.4, Discussion 多处使用\"model-agnostic\"\n- 问题：只测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct——同一参数规模。70B+ 模型可能产生更高质量更多样的样本，从根本上改变 correlation-selection gap 的形态。Limitations 承认了这一点，但 Discussion 仍使用\"model-agnostic\"措辞，形成内部矛盾（ARR R4 overclaiming）。\n\n**N3** [critical] RE 结论仅基于 SciERC，44% zero-F1 floor effect 严重扭曲信号评估\n\n- 具体位置：Section 5.1, Limitations 第 1 段\n- 问题：RE 的所有结论全部来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。论文声称覆盖\"NER and RE\"但 RE 实验基础极其薄弱。\n\n## Should-Fix 问题\n\n**W1** [warning] Soft Jaccard 形式化有歧义：g_i/g_j 未定义，sim 具体公式缺失，Hungarian algorithm 匹配阈值未说明。\n\n**W2** [warning] Entity voting 的 mean frequency 聚合方式未讨论替代选择（median、thresholded voting 等），当模型产生大量低频幻觉实体时 |E_∪| 膨胀导致置信度系统性偏低。\n\n**W3** [warning] ρ=0.38 被反复描述为\"effective/strong quality estimation\"但仅解释 ~14% F1 方差，未与 uncertainty estimation 文献中其他方法的 ρ 对比 contextualize。\n\n**W4** [warning] Logprob（唯一 per-sample signal、selection 最佳信号）的温度敏感性数据缺失（T=0.7 unavailable），但论文做出了\"signals robust across temperatures\"的笼统结论。\n\n**W5** [warning] WNUT-17 p=0.106 被解读为\"establishing the capability boundary where all signals break down\"，措辞过于确定——fail to reject null ≠ accept null。\n\n**W6** [warning] Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct（未说明是否微调）训练设置不对称，可能混淆 cross-model 比较。\n\n**W7** [warning] 约束解码对 sampling diversity 的影响未讨论——这可能是 correlation-selection gap 的一个成因。\n\n## 小问题\n\n- Table 2 EM \"---\" 需更显著的解释\n- Limitations 提到\"logistic regression proxy as an upper bound\"但正文/Appendix 无此分析结果\n- snell2024scaling bib 作者格式与 OpenAlex 有 mismatch\n- Cross-model Δ=0.005 未报告是否在 bootstrap CI 内\n- Introduction \"+18pp on GSM8K\" 未注明具体模型(PaLM-540B)\n- Appendix D \\textsc 编译检查\n\n## 主要优势\n\n1. 研究问题定义精准：quality estimation vs. sample selection 的解耦是有价值的概念贡献\n2. 实验设计的系统性出色：5 signals × 3 families × 3 datasets × 2 models × 2 N × 2 T + 多项辅助分析\n3. Task difficulty gradient 设计合理（CoNLL/SciERC/WNUT），信号排序随难度变化的发现有实用价值\n4. 统计实践总体规范（p-values, Cohen's d, CI, 3-seed, Fisher z-test, LOO circularity check）\n5. Limitations section 全面诚实\n\n## Overall Assessment\n\n**Verdict: Borderline → Weak Accept for Findings**\n\n核心顾虑：(1) bootstrap 细节不足以确认核心负面结论成立（N1）；(2) model-agnostic overclaim（N2）；(3) RE 结论基础薄弱（N3）。如果 N1 确认执行正确、N2/N3 做适当限定，适合 Findings。进入 Main Conference 需要额外模型规模或 RE 数据集验证。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-15T01:56:34.235671+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3966
}
```

</details>

---


### Assistant

_source line 138 · 2026-05-15T01:56:40.903505+00:00_

Round 1 审稿完成，已汇报给 Review Director。

核心判断：**Overall 3/5 (Findings)**。三个 Must-Fix 问题：(1) bootstrap 检验细节严重不足，核心"Weak Selectors"结论的统计基础无法验证；(2) 仅两个 8B 模型却声称 model-agnostic，overclaim；(3) RE 结论仅依赖 SciERC 一个数据集且 44% 零分样本严重扭曲评估。七个 Should-Fix 问题涵盖 Soft Jaccard 形式化歧义、entity voting 聚合方式、ρ=0.38 的 contextualization、logprob 温度数据缺失、WNUT-17 解读过于强硬、模型训练设置不对称、约束解码对 diversity 的影响。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

36 recorded events


### User

_source line 139 · 2026-05-15T01:58:09.952555+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见

请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 2 的完整审稿原文：

### 总体评分
**Overall**: 3.0/5（Findings track acceptance）
**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5
**Confidence**: 4/5

### 核心判断
论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：

### Must-Fix 问题 (3 个)

**N1** [critical] "Correlation-selection gap" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。

**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 "systematic comparison"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。

**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。

### Should-Fix 问题 (5 个)
- W1: "first systematic evaluation" claim 过强，需收窄 scope
- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction
- W3: 遗漏 "Optimal Self-Consistency" (arXiv:2511.12309) 和 "Difficulty-Adaptive SC" (NAACL 2025 Findings)
- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）
- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应

### 引用真实性
46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 "Nedellec et al." 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。

### 遗漏重要引用
1. Singer et al. (2026) "UQ for NER via Conformal Prediction"
2. Conformal Structured Prediction (ICLR 2025)
3. Optimal Self-Consistency (arXiv:2511.12309)
4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)
5. Generative Self-Aggregation (arXiv:2503.04104)

### 审稿判断
当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-15T01:58:21.806160+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-15T01:58:21.856953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-15T01:58:25.929012+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-15T01:58:26.435212+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-15T01:58:26.538293+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-15T01:58:26.588901+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-15T01:58:28.961412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-15T01:58:29.012099+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-15T01:58:31.578196+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-15T01:58:31.628999+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-15T01:58:34.592119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-15T01:58:35.094712+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-15T01:58:35.145268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-15T01:58:35.547001+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpti
…[truncated 3524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-15T01:58:35.547439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-15T01:58:35.999124+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	All target reasoning/QA with discrete answers.
9	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
13	However, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.
14	Our Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.
15	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie
…[truncated 1727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-15T01:58:35.999677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-15T01:58:36.953570+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-15T01:58:36.953943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-15T01:58:37.405964+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Our primary model is \textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct}.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \mu
…[truncated 7771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-15T01:58:37.456644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-15T01:58:37.908635+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	
11	\paragraph{Why quality estimators fail as selectors.}
12	Quality estimation ranks \textit{instances} by expected output quality via output distribution entropy; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
13	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
14	The $\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\rho$; both metrics measure be
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-15T01:58:37.909168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-15T01:58:38.361320+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-15T01:58:38.361704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-15T01:58:38.816355+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-15T01:58:38.816845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-15T01:58:38.917738+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 9406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-15T01:58:45.094174+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-15T01:58:45.146297+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-15T01:58:48.268996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-15T01:58:48.320678+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 16730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-15T02:01:22.293614+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: Correlation-selection gap 的解释力**\n\n同意 R2 的核心判断：4/5 instance-level signals 无法做 per-sample selection 在定义上是预期的（Section 3.1 明确区分了 per-sample vs. instance-level，Eq. 5–8 只产出单一 score），这削弱了\"发现\"的新颖性。\n\n但需补充两点：\n1. 论文在 Section 3.3 中通过\"select the sample closest to the consensus output\"将 instance-level signals 转化为 per-sample 排序——这不是纯粹定义性的，是一个合理的 selection 策略，只不过效果不好（Table 5: SJ=0.645 vs. Greedy=0.644）。\n2. R2 关于 logprob 失败原因分析不足的批评完全成立。论文仅在 Section 5.1 提到 conditional filtering 后\"logprob RE collapses to ρ=0.011\"（Figure 2 右），说明其 full-set correlation 来自 zero/non-zero 分离；Discussion 段简要提到 constrained decoding 可能的影响，但未做任何实验验证。作为唯一的 per-sample signal，logprob 值得至少一段深入分析。\n\n**[REBUT] R2-N2: Per-sample signal 探索严重不足**\n\nR2 认为 LOO-SJ 的 selection 能力\"未被测试\"，但这与论文实际实验不符。Section 3.3 明确说 instance-level signals 通过 consensus-proximity 选择候选样本。对于 SJ，consensus-proximity 就是：对每个 y_i 计算其对所有其他样本的平均 SJ——这在数学上等价于 LOO-SJ 排序。Table 5 中 SJ 行（NER F1=0.645, RE F1=0.386）就是 LOO-SJ 的 selection 结果，只是论文没有显式使用\"LOO-SJ selection\"这个术语。\n\n真正的问题是论文没有把这个等价关系说清楚，是表述问题而非实验缺失。\n\n不过，R2 关于只有 1 个 per-sample signal 的批评仍然有效——\"systematic comparison\" 但 per-sample 维度极度单薄。\n\n**[AGREE] R2-N3: 对 Nedellec et al. (2026) 的增量贡献论证不足**\n\n同意。补充发现：bib 文件中 nedellec2026consistency 的 author 字段确认第一作者是 Yao，论文全文使用\"Nédellec et al.\"是事实性错误。SJ 优势不一致性确实削弱区分论证（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）。\n\n但 negative selection result 本身仍有学术价值——Nedellec et al. 未涉及 selection，论文首次系统验证了 best-of-N selection 在 IE 中的失败。问题在于论证方式不够有力，而非贡献不存在。\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1**: \"first systematic\" claim 需收窄，加限定语如\"first to compare signals from multiple families for both quality estimation and sample selection in generative IE\"。\n\n**[REBUT] R2-W2**: 论文已引用 conformal prediction 代表性工作（Fisch 2021, Angelopoulos 2021）并在 Conclusion 讨论 future integration。Singer et al. 和 ICLR 2025 conformal 属不同研究路线（supervised conformal vs. unsupervised consistency），添加为 related work 合理，但非 critical omission。\n\n**[AGREE] R2-W3**: Optimal Self-Consistency 和 Difficulty-Adaptive SC 与论文核心主题高度相关，应引用讨论。尤其后者——论文的核心发现之一就是 signal rankings depend on task difficulty。\n\n**[AGREE with nuance] R2-W4**: 实验覆盖度在 EMNLP 标准下不算小（2 模型族 × 3 数据集 × robustness 分析）。但仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 设置确是限制。补充同意 R2 的\"非典型设置\"观点——LoRA fine-tuning 可能使模型输出分布比 hard-prompted 更集中，人为压低 sample diversity，使 selection signals 更难区分候选样本，这是潜在混淆变量。\n\n**[AGREE] R2-W5**: EM=1 压缩效应在 Appendix D 有讨论但仅在 appendix，应在主文明确阐述。\n\n### 引用真实性\n\n**[AGREE]** nedellec2026consistency 第一作者应为 Yao，论文\"Nédellec et al.\"引用有误，已从 bib 文件确认。\n\n### 遗漏引用\n\n- [AGREE] #3 Optimal SC, #4 Difficulty-Adaptive SC 应引用\n- [REBUT] #1 Singer et al., #2 ICLR 2025 conformal 非 critical omission\n- [NEUTRAL] #5 Generative Self-Aggregation 需确认内容再判断\n\n### 审稿判断\n\n[AGREE with qualification] 同意 Findings track 判断方向。核心问题：(1) gap 的理论贡献被部分定义性质削弱，(2) per-sample signal 维度单薄，(3) logprob 失败机制分析缺失。\n\n对 R2 修改路径的补充建议：LOO-SJ 实际已隐式测试（Table 5 SJ 行），更有价值的方向是引入真正新的 per-sample signals（per-entity logprob、learned verifier probe）或分析 constrained decoding 对 logprob 信号的系统性扭曲。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: Correlation-selection gap 的解释力**\n\n同意 R2 的核心判断：4/5 instance-level signals 无法做 per-sample selection 在定义上是预期的（Section 3.1 明确区分了 per-sample vs. instance-level，Eq. 5–8 只产出单一 score），这削弱了\"发现\"的新颖性。\n\n但需补充两点：\n1. 论文在 Section 3.3 中通过\"select the sample closest to the consensus output\"将 instance-level signals 转化为 per-sample 排序——这不是纯粹定义性的，是一个合理的 selection 策略，只不过效果不好（Table 5: SJ=0.645 vs. Greedy=0.644）。\n2. R2 关于 logprob 失败原因分析不足的批评完全成立。论文仅在 Section 5.1 提到 conditional filtering 后\"logprob RE collapses to ρ=0.011\"（Figure 2 右），说明其 full-set correlation 来自 zero/non-zero 分离；Discussion 段简要提到 constrained decoding 可能的影响，但未做任何实验验证。作为唯一的 per-sample signal，logprob 值得至少一段深入分析。\n\n**[REBUT] R2-N2: Per-sample signal 探索严重不足**\n\nR2 认为 LOO-SJ 的 selection 能力\"未被测试\"，但这与论文实际实验不符。Section 3.3 明确说 instance-level signals 通过 consensus-proximity 选择候选样本。对于 SJ，consensus-proximity 就是：对每个 y_i 计算其对所有其他样本的平均 SJ——这在数学上等价于 LOO-SJ 排序。Table 5 中 SJ 行（NER F1=0.645, RE F1=0.386）就是 LOO-SJ 的 selection 结果，只是论文没有显式使用\"LOO-SJ selection\"这个术语。\n\n真正的问题是论文没有把这个等价关系说清楚，是表述问题而非实验缺失。\n\n不过，R2 关于只有 1 个 per-sample signal 的批评仍然有效——\"systematic comparison\" 但 per-sample 维度极度单薄。\n\n**[AGREE] R2-N3: 对 Nedellec et al. (2026) 的增量贡献论证不足**\n\n同意。补充发现：bib 文件中 nedellec2026consistency 的 author 字段确认第一作者是 Yao，论文全文使用\"Nédellec et al.\"是事实性错误。SJ 优势不一致性确实削弱区分论证（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）。\n\n但 negative selection result 本身仍有学术价值——Nedellec et al. 未涉及 selection，论文首次系统验证了 best-of-N selection 在 IE 中的失败。问题在于论证方式不够有力，而非贡献不存在。\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1**: \"first systematic\" claim 需收窄，加限定语如\"first to compare signals from multiple families for both quality estimation and sample selection in generative IE\"。\n\n**[REBUT] R2-W2**: 论文已引用 conformal prediction 代表性工作（Fisch 2021, Angelopoulos 2021）并在 Conclusion 讨论 future integration。Singer et al. 和 ICLR 2025 conformal 属不同研究路线（supervised conformal vs. unsupervised consistency），添加为 related work 合理，但非 critical omission。\n\n**[AGREE] R2-W3**: Optimal Self-Consistency 和 Difficulty-Adaptive SC 与论文核心主题高度相关，应引用讨论。尤其后者——论文的核心发现之一就是 signal rankings depend on task difficulty。\n\n**[AGREE with nuance] R2-W4**: 实验覆盖度在 EMNLP 标准下不算小（2 模型族 × 3 数据集 × robustness 分析）。但仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 设置确是限制。补充同意 R2 的\"非典型设置\"观点——LoRA fine-tuning 可能使模型输出分布比 hard-prompted 更集中，人为压低 sample diversity，使 selection signals 更难区分候选样本，这是潜在混淆变量。\n\n**[AGREE] R2-W5**: EM=1 压缩效应在 Appendix D 有讨论但仅在 appendix，应在主文明确阐述。\n\n### 引用真实性\n\n**[AGREE]** nedellec2026consistency 第一作者应为 Yao，论文\"Nédellec et al.\"引用有误，已从 bib 文件确认。\n\n### 遗漏引用\n\n- [AGREE] #3 Optimal SC, #4 Difficulty-Adaptive SC 应引用\n- [REBUT] #1 Singer et al., #2 ICLR 2025 conformal 非 critical omission\n- [NEUTRAL] #5 Generative Self-Aggregation 需确认内容再判断\n\n### 审稿判断\n\n[AGREE with qualification] 同意 Findings track 判断方向。核心问题：(1) gap 的理论贡献被部分定义性质削弱，(2) per-sample signal 维度单薄，(3) logprob 失败机制分析缺失。\n\n对 R2 修改路径的补充建议：LOO-SJ 实际已隐式测试（Table 5 SJ 行），更有价值的方向是引入真正新的 per-sample signals（per-entity logprob、learned verifier probe）或分析 constrained decoding 对 logprob 信号的系统性扭曲。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-15T02:01:26.910365+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4616
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-15T02:01:37.163158+00:00_

交叉回应已提交。总结：

- **N1**: 部分同意——4/5 signals 不能做 per-sample selection 确有定义性成分，但 consensus-proximity 策略不完全是 trivial 的；logprob 失败分析不足的批评完全成立
- **N2**: 反驳——LOO-SJ 通过 consensus-proximity 在 Table 5 已隐式测试（SJ 行），是表述问题而非实验缺失；但"只有 1 个 per-sample signal"的批评仍有效
- **N3**: 同意——增量论证弱，但 negative selection result 本身有学术价值；引用中 Yao→Nédellec 的错误已从 bib 确认
- **W1-W5**: W1/W3/W5 同意，W2 反驳（非 critical omission），W4 部分同意并补充 LoRA 作为混淆变量的观点
- **整体判断**: 同意 Findings track 方向，但建议修改路径侧重引入新 per-sample signals 和分析 constrained decoding 对 logprob 的影响

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

46 recorded events


### User

_source line 175 · 2026-05-15T02:42:36.621848+00:00_

[Round 2 审稿请求]:
## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，long paper ≤8 页正文，double-blind
- **匿名规则**: Double-blind，无匿名期要求
- **附录**: 允许，不计页数，不保证审稿人阅读

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`（sections/ 子目录含全部章节，references.bib 含 40 条引用）

### 你的审查侧重
**方法严谨性 + 实验设计**。重点关注：
1. **统计检验规范性**：bootstrap 检验是否完整报告（n, B, paired/unpaired, CI, 统计量）
2. **Soft Jaccard 形式化**：Eq.(4) 定义是否完备（sim 函数、g_i/g_j 含义、Hungarian 阈值）
3. **Correlation-selection gap 论证**：instance-level vs per-sample 区分是否清晰，logprob 失败原因分析是否充分
4. **实验覆盖度**：RE 仅 SciERC 单数据集是否充分 hedge，WNUT-17 boundary claim 措辞是否过强
5. **训练设置对称性**：Qwen/LLaMA 是否相同训练流程，cross-model 比较是否 fair
6. **Robustness 分析**：logprob 温度敏感性数据缺失是否充分说明，N-scaling 结论是否 supported

### Round 0-1 遗留 Open Issues（你需要检查是否已修复）
- **R1-N1 [critical]**: Bootstrap 检验细节不足——需确认 Section 5.3 是否已补完整规范（n=529, B=10,000, paired, 统计量, seed 含义）
- **R1-N2 [critical]**: Correlation-selection gap 解释力不足——需确认 Discussion 是否已区分 instance-level limitation vs per-sample empirical finding，logprob failure 分析是否充分
- **R1-N3 [warning]**: Per-sample signal 仅 logprob 1 个——需确认是否已说明 Table 5 SJ = consensus-proximity = LOO-SJ
- **R1-W1 [warning]**: SJ 形式化有歧义——需确认 Eq.(4) g_i/g_j、sim 公式、Hungarian 阈值是否已补全
- **R1-W2 [warning]**: Entity voting & SJ 冗余度——需确认是否已报告 Voting-SJ correlation 并论证差异
- **R0-W4/R1-N1 [critical]**: 统计检验不系统——需确认是否已补充 bootstrap CI
- **R1-W4 [warning]**: Logprob 温度敏感性数据缺失——需确认 robustness 结论是否已限定
- **R1-W6 [warning]**: LLaMA fine-tuning 状态——需确认 Section 4 是否已明确说明
- **R1-W7 [warning]**: 约束解码对 sampling diversity 影响——需确认 Discussion 是否已讨论
- **R0-C3 [critical]**: RE 仅 SciERC——需确认措辞是否已降级

### 输出格式
按 EMNLP 审稿标准输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → 对遗留 Issue 的逐条状态判定（resolved/partially/unresolved）→ Overall Score（1-5）+ Confidence（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-15T02:42:45.450226+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-15T02:42:45.501027+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-15T02:42:49.673806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-15T02:42:50.276533+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-15T02:42:50.276955+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-15T02:42:50.277195+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-15T02:42:50.277380+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-15T02:42:59.380602+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, I found comprehensive information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines Overview

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related work
…[truncated 2039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9706
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-15T02:43:03.949810+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-15T02:43:04.452209+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-15T02:43:05.510049+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), descriptions for each score level, and any specific instructions for reviewers. Include the overall assessment scale details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), descriptions for each score level, and any specific instructions for reviewers. Include the overall assessment scale details."
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-15T02:43:12.740153+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Scoring Dimensions

### 1. Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure; unlikely to have missed important points
- **3**: Pretty sure; good general knowledge but didn't carefully verify details
- **2**: Willing to defend evaluation, but likely missed some details or novelty
- **1**: "Not my area, or paper is very hard to understand"

### 2. Soundness (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; sufficient support with minor experiments optional
- **3**: Acceptable; supports main claims with minor details needed
- **2**: Poor; main claims lack sufficient support; major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

### 3. Excitement (1-5 scale with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend"
- **4**: Exciting; would mention to others or attend presentation
- **3**: Interesting; might mention points or attend if time permits
- **2**: Potentially interesting to some in the community
- **1**: "Not Exciting: this paper does not resonate with me"

### 4. Overall Assessment (1-5 scale with half-point increments)
- **5**: "Consider for Award" (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance recommended
- **3.5**: Borderline Conference
- **3**: Findings acceptance recommended
- **2.5**: Borderline Findings
- **2**: "Resubmit next cycle" with substantial revisions
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Secondary Dimensions

**Reproducibility** (1-5): Ranges from easily reproducible to impossible

**Datasets/Software Value** (1-5): Ranges from enabling to no usable materials

**Author Anonymity Knowledge** (1-5): Ranges from known identity to complete anonymity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7230
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-15T02:43:17.009720+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-15T02:43:18.415678+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-15T02:43:18.567351+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
  "description": "Find tex and bib files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
    "description": "Find tex and bib files in project"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-15T02:43:18.769521+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_ge
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-15T02:43:22.685970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-15T02:43:23.137976+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-15T02:43:23.138345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-15T02:43:24.092254+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-15T02:43:24.092602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-15T02:43:24.596663+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 3826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-15T02:43:24.597205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-15T02:43:25.049987+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-15T02:43:25.050450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-15T02:43:25.502734+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
…[truncated 9072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-15T02:43:25.503922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-15T02:43:25.961808+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-s
…[truncated 2466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-15T02:43:25.962350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-15T02:43:26.917402+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quality estimation ranks \textit{instances} by expected output quality; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance
…[truncated 3070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-15T02:43:26.917858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-15T02:43:27.369862+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-15T02:43:27.420485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-15T02:43:27.872706+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-15T02:43:27.873283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-15T02:43:28.124762+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 10209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-15T02:43:28.175788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-15T02:43:28.226687+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 17900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-15T02:45:11.915079+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "WNUT",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "WNUT",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-15T02:45:12.417605+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:11:\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:76:On WNUT-17, SJ achieves only $\rho{=}0.082$ ($p{=}0.106$), suggesting a capability boundary beyond which all signals break down.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:113:Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:5:Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:31:We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:45:    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, 
…[truncated 1370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-15T02:45:12.568496+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LLaMA.*SciERC|SciERC.*LLaMA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LLaMA.*SciERC|SciERC.*LLaMA",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-15T02:45:12.669325+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:15:We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:26:\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:30:& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:5:Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:12:The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:3:We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$),
…[truncated 5533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-15T02:48:15.676420+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 2 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Summary\n\n本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE 中的 quality estimation 与 sample selection 效果。核心发现是 \"correlation-selection gap\"：instance-level 信号能预测 input difficulty（ρ 达 0.38）但无法从 N 个候选中选出最优 output（所有信号均未显著超过 greedy，p>0.39）。此外，信号排名依赖 task difficulty（EM 领先 easy tasks，SJ/Voting 领先 hard tasks）。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference / Strong Findings)\n**一句话总结**: Quality estimation 分析全面扎实，但最核心的 selection gap 负结论证据面偏窄（1 dataset × 1 model），削弱了 \"fundamental disconnect\" 的 framing 强度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | QE 分析严谨、bootstrap 规范完整；但 selection 证据限于 SciERC/Qwen，WNUT-17 boundary claim 缺系统数据 |\n| Excitement | 3/5 | QE vs selection 的概念区分有价值；但负结论（selection 失败）在 instance-level signal 框架下可从理论预期，novelty 中等 |\n| Reproducibility | 3.5/5 | 训练细节（LoRA rank/α/epochs/framework）完整，bootstrap 规范清晰；但 n=529 vs SciERC 551 的 filtering 未交代 |\n| Confidence | 4/5 | 逐节逐表验证了关键 claims，仔细检查了 Round 0-1 遗留问题修复状态 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Selection 结果仅限 SciERC/Qwen，与 framing 不匹配\n\n- **具体位置**: Table 3 (Section 5.3)；Abstract (\"no signal reliably surpasses greedy decoding on either task\")\n- **问题**: 论文最核心的贡献——correlation-selection gap——仅在 SciERC 上用 Qwen 验证。Quality estimation 覆盖 3 datasets × 2 models，但 selection 仅 1 dataset × 1 model。Abstract 和 Conclusion 的 framing 暗示这是跨 task/model 的 \"fundamental disconnect\"，但 evidence base 不支撑这一泛化。CoNLL selection 未报告（即使 headroom 小，negative result 本身也有价值），LLaMA SciERC selection 未报告。\n- **为什么影响接收**: Contribution #2 是论文的 differentiator（与 Nédellec et al. 2026 的关键区别就是 selection 分析），如果 selection 证据过窄，这个 claim 的 generalizability 存疑。\n- **建议**: 至少补 LLaMA SciERC selection 结果以验证 cross-model generalization；CoNLL selection 放 appendix（即使结论是 ceiling effect 导致无 headroom，也应明确报告）。\n\n**N2** [critical] WNUT-17 \"capability boundary\" claim 缺乏系统证据\n\n- **具体位置**: Section 5.1 (\"On WNUT-17, SJ achieves only ρ=0.082 (p=0.106), suggesting a capability boundary beyond which all signals break down\")；Contribution 3 (Introduction)\n- **问题**: 这一 claim 列为 Contribution #3，但全文仅报告 SJ 一个信号的一个 ρ 值。其他四个信号（Voting、EM、FK、Logprob）在 WNUT-17 上的表现未出现在任何 table 或 text 中。更关键的是，SJ ρ=0.082 的 p=0.106 意味着该 correlation 本身不显著——用一个不显著的单信号结果支撑 \"all signals break down\" 的 claim 在逻辑上不成立。\n- **为什么影响接收**: Abstract 和 Contribution list 明确将 WNUT-17 boundary 作为 task-complexity 贡献的一部分，reviewer 会期待至少一个完整的 WNUT-17 结果表。\n- **建议**: 在 Table 1 或 Appendix 增加 WNUT-17 column/table，报告全部 5 signal 的 ρ 和 AUROC。如果确实全部 collapse，这反而是更强的证据。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Quality estimation ρ 在 N=8 缺乏不确定性量化\n\n- **具体位置**: Table 1 (Section 5.1)\n- **问题**: Table 1 的 N=8 行报告 point estimates（ρ 和 AUROC）without CIs、standard errors 或 significance tests。仅 N=16 3-seed block 有 ±std。主要 claims（如 \"entity voting achieves ρ=0.38\"）无 associated uncertainty。这与 Section 5.3 selection 结果的 thorough bootstrap（CI、Cohen's d、sign test）形成不一致：QE 是正面结论，selection 是负面结论，但正面结论反而缺乏统计支撑。\n- **建议**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或至少在 Appendix 补充 3-seed runs。\n\n**W2** [warning] SJ Hungarian matching 缺 threshold 规范\n\n- **具体位置**: Eq.(4), Section 3.2\n- **问题**: Eq.(4) 现在已定义 sim = token-level IoU，g_i/g_j = per-type extraction counts（比 Round 1 改善显著）。但 Hungarian algorithm 是否有 minimum similarity threshold？如果 threshold=0，两个完全不相关的 span 也会被 matched，导致 SJ numerator 非零。如果 threshold>0，threshold 的选择影响所有下游 ρ 值但未报告。\n- **建议**: 明确说明是否使用 threshold（以及值），或解释为什么 zero-overlap matches 对 SJ 影响可忽略。\n\n**W3** [warning] RE selection 无统计检验\n\n- **具体位置**: Table 3, Section 5.3\n- **问题**: NER selection 报告了完整 bootstrap（p=0.39, CI [-3.0, +4.2]pp, Cohen's d=0.038, sign test）。RE selection 仅报告 \"no signal exceeds greedy (0.404) despite 18.1 pp of oracle headroom\"，无 p-value、CI 或 effect size。RE 的 selection gap 实际更大（greedy 胜出），理应同样给出统计检验。\n- **建议**: 补充 RE selection 的 bootstrap p-value 和 CI。\n\n**W4** [warning] SciERC cross-model 不对称（N=8）\n\n- **具体位置**: Table 1; Appendix A.3\n- **问题**: Table 1 SciERC 列仅为 Qwen 结果（表头未标注模型），LLaMA SciERC 仅在 Appendix 文字中零散出现（SJ ρ=0.363, FK ρ=0.327），不完整（5 个信号只报了 2 个），无 AUROC，无 table。SciERC 是驱动核心 claims 的 primary dataset，cross-model validation 的缺失在此处比在 CoNLL 上更关键。\n- **建议**: Table 1 增加 SciERC (LLaMA) 列，或在 Appendix 补完整 table。\n\n**W5** [warning] n=529 vs SciERC n=551 的 discrepancy\n\n- **具体位置**: Section 5.3 (\"over n=529 NER instances\")\n- **问题**: SciERC test set 有 551 instances，但 bootstrap 用 n=529。22 instances 被 drop 的原因未交代。如果是 filtering（如 zero-entity instances），应明确说明 filtering criteria。\n- **建议**: 一句话说明 n=529 的来源。\n\n---\n\n## 小问题（不影响接收）\n\n- Eq.(4) 分母 $\\sum_g \\max(|g_i|, |g_j|)$ 是非标准 Jaccard variant，一句解释为何不用 $|A \\cup B|$ 会帮助理解。\n- FK adaptation (Section 3.2)：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 \"independent raters\"，brief acknowledgment 即可。\n- Table 3 的 EM 行显示 \"---\" 但 caption 未解释原因，caption 可加 \"EM produces binary agreement without sample ranking.\"——实际 caption 已有此句 ✓，但 RE 列也是 \"---\"，可考虑统一 footnote 说明。\n- Section 5.3：\"three random seeds (42, 123, 456) refer to independent inference runs\"——但 Table 1 的 N=8 primary results 未说明用了哪个 seed 或是否 averaged。\n\n---\n\n## Questions for Authors\n\n**Q1.** WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？如果全部 non-significant，这本身是一个强结论；如果某个信号显著，则 \"all signals break down\" 需要修正。\n\n**Q2.** CoNLL 的 best-of-N selection 结果（即使 greedy 已 >0.91）？一个可能的 outcome 是 oracle headroom 很小 → selection gap 不存在 → 说明 gap 是 hard-task specific，这也是有价值的 insight。\n\n**Q3.** SciERC bootstrap n=529：22 instances 被 drop 的 criteria 是什么？\n\n**Q4.** SJ Hungarian matching 是否有 minimum similarity threshold？如果无 threshold，matched pairs 中 sim≈0 的比例有多高？\n\n**Q5.** Table 1 的 N=8 主要结果是 single-seed 还是 averaged？如果 single-seed，是否有 variance estimates？\n\n---\n\n## Round 0-1 遗留 Issue 状态判定\n\n| Issue | 状态 | 判定依据 |\n|-------|------|----------|\n| **R1-N1** [critical]: Bootstrap 检验细节不足 | ✅ **Resolved** | Section 5.3 补齐：n=529, B=10K, paired, percentile 95% CIs [-3.0, +4.2]pp, Cohen's d=0.038, sign test 61W/70L, seeds(42/123/456) 含义明确 |\n| **R1-N2** [critical]: Correlation-selection gap 解释力不足 | ✅ **Resolved** | Discussion 清晰区分 instance-level（rank instances）vs per-sample（rank candidates within instance）；logprob 失败归因于 constrained decoding grammar compliance + 75% ties |\n| **R1-N3** [warning]: Per-sample signal 仅 logprob | ✅ **Resolved** | Section 3.3 明确 consensus-proximity = LOO-SJ；Appendix 验证 LOO-SJ Δρ=-0.014（negligible circularity） |\n| **R1-W1** [warning]: SJ 形式化有歧义 | ⚠️ **Partially resolved** | sim = token-level IoU ✓, g_i/g_j = per-type extraction counts ✓, Hungarian threshold 仍未指定 |\n| **R1-W2** [warning]: Voting-SJ 冗余度 | ✅ **Resolved** | 报告 inter-signal ρ=0.659 (NER), 0.605 (RE) + differential behavior across difficulty 论述 |\n| **R0-W4/R1-N1** [critical]: 统计检验不系统 | ⚠️ **Partially resolved** | Selection 有完整 bootstrap ✓；QE Table 1 N=8 仍为 point estimates without CIs |\n| **R1-W4** [warning]: Logprob 温度敏感性 | ✅ **Resolved** | Section 5.4 + Limitations 均明确 acknowledge T=0.7 logprob data missing |\n| **R1-W6** [warning]: LLaMA fine-tuning 状态 | ✅ **Resolved** | Section 4.1: 两模型 identical LoRA (rank=32, α=64), 5 epochs, LLaMA Factory |\n| **R1-W7** [warning]: 约束解码影响 | ✅ **Resolved** | Discussion: acknowledged constrained decoding compresses diversity + random baseline gap 3.6pp confirms variance exists + future work identified |\n| **R0-C3** [critical]: RE 仅 SciERC | ✅ **Resolved** | Introduction/Discussion/Conclusion/Appendix 四处 hedge |\n\n---\n\n## 主要优势\n\n1. **概念贡献清晰**: QE vs selection 的 distinction 是 generative IE 社区需要的，且 formulation (Section 3.1 per-sample vs instance-level) 精确可操作。\n2. **Quality estimation 分析全面**: 5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic，分析深度超过多数实证论文。\n3. **Bootstrap 规范（selection）**: Cohen's d、sign test、percentile CI、seed 解释一应俱全，是 NLP 实证论文的良好标准。\n4. **ρ-AUROC dissociation 的发现**: EM 在 ρ 排名低但 AUROC 领先（Section 5.1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 有直接 actionable 价值。\n5. **诚实的 hedging**: RE single-dataset 限制在 4 处 acknowledge，logprob temperature gap 在正文 + Limitations 双重标注——Round 0-1 的 self-awareness 问题已有实质改善。\n6. **与 Nédellec et al. (2026) 的定位清晰**: 三点差异化（structural matching / selection analysis / difficulty gradient）具体且有说服力。\n\n---\n\n## 总结\n\n论文从 Round 0 到 Round 2 有显著改善：bootstrap 规范化、SJ 形式化、RE hedging、constrained decoding 讨论等遗留问题大多已 resolved 或 partially resolved。Quality estimation 分析是本文的强项，coverage 和 depth 均达到 long paper 标准。\n\n主要 concern 集中在 evidence breadth vs framing breadth 的 mismatch：correlation-selection gap 作为核心贡献，仅在 1 dataset × 1 model 上验证（N1）；WNUT-17 boundary 作为 listed contribution，仅有 1 个不显著的数据点（N2）。如果这两个问题得到补充，论文有 Conference 实力；当前状态更适合 Findings。\n\n**Overall**: 3.5/5 (Borderline Conference / Strong Findings)\n**Confidence**: 4/5",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 2 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Summary\n\n本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE 中的 quality estimation 与 sample selection 效果。核心发现是 \"correlation-selection gap\"：instance-level 信号能预测 input difficulty（ρ 达 0.38）但无法从 N 个候选中选出最优 output（所有信号均未显著超过 greedy，p>0.39）。此外，信号排名依赖 task difficulty（EM 领先 easy tasks，SJ/Voting 领先 hard tasks）。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference / Strong Findings)\n**一句话总结**: Quality estimation 分析全面扎实，但最核心的 selection gap 负结论证据面偏窄（1 dataset × 1 model），削弱了 \"fundamental disconnect\" 的 framing 强度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | QE 分析严谨、bootstrap 规范完整；但 selection 证据限于 SciERC/Qwen，WNUT-17 boundary claim 缺系统数据 |\n| Excitement | 3/5 | QE vs selection 的概念区分有价值；但负结论（selection 失败）在 instance-level signal 框架下可从理论预期，novelty 中等 |\n| Reproducibility | 3.5/5 | 训练细节（LoRA rank/α/epochs/framework）完整，bootstrap 规范清晰；但 n=529 vs SciERC 551 的 filtering 未交代 |\n| Confidence | 4/5 | 逐节逐表验证了关键 claims，仔细检查了 Round 0-1 遗留问题修复状态 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Selection 结果仅限 SciERC/Qwen，与 framing 不匹配\n\n- **具体位置**: Table 3 (Section 5.3)；Abstract (\"no signal reliably surpasses greedy decoding on either task\")\n- **问题**: 论文最核心的贡献——correlation-selection gap——仅在 SciERC 上用 Qwen 验证。Quality estimation 覆盖 3 datasets × 2 models，但 selection 仅 1 dataset × 1 model。Abstract 和 Conclusion 的 framing 暗示这是跨 task/model 的 \"fundamental disconnect\"，但 evidence base 不支撑这一泛化。CoNLL selection 未报告（即使 headroom 小，negative result 本身也有价值），LLaMA SciERC selection 未报告。\n- **为什么影响接收**: Contribution #2 是论文的 differentiator（与 Nédellec et al. 2026 的关键区别就是 selection 分析），如果 selection 证据过窄，这个 claim 的 generalizability 存疑。\n- **建议**: 至少补 LLaMA SciERC selection 结果以验证 cross-model generalization；CoNLL selection 放 appendix（即使结论是 ceiling effect 导致无 headroom，也应明确报告）。\n\n**N2** [critical] WNUT-17 \"capability boundary\" claim 缺乏系统证据\n\n- **具体位置**: Section 5.1 (\"On WNUT-17, SJ achieves only ρ=0.082 (p=0.106), suggesting a capability boundary beyond which all signals break down\")；Contribution 3 (Introduction)\n- **问题**: 这一 claim 列为 Contribution #3，但全文仅报告 SJ 一个信号的一个 ρ 值。其他四个信号（Voting、EM、FK、Logprob）在 WNUT-17 上的表现未出现在任何 table 或 text 中。更关键的是，SJ ρ=0.082 的 p=0.106 意味着该 correlation 本身不显著——用一个不显著的单信号结果支撑 \"all signals break down\" 的 claim 在逻辑上不成立。\n- **为什么影响接收**: Abstract 和 Contribution list 明确将 WNUT-17 boundary 作为 task-complexity 贡献的一部分，reviewer 会期待至少一个完整的 WNUT-17 结果表。\n- **建议**: 在 Table 1 或 Appendix 增加 WNUT-17 column/table，报告全部 5 signal 的 ρ 和 AUROC。如果确实全部 collapse，这反而是更强的证据。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Quality estimation ρ 在 N=8 缺乏不确定性量化\n\n- **具体位置**: Table 1 (Section 5.1)\n- **问题**: Table 1 的 N=8 行报告 point estimates（ρ 和 AUROC）without CIs、standard errors 或 significance tests。仅 N=16 3-seed block 有 ±std。主要 claims（如 \"entity voting achieves ρ=0.38\"）无 associated uncertainty。这与 Section 5.3 selection 结果的 thorough bootstrap（CI、Cohen's d、sign test）形成不一致：QE 是正面结论，selection 是负面结论，但正面结论反而缺乏统计支撑。\n- **建议**: 对 N=8 主要 ρ 值报告 bootstrap CIs，或至少在 Appendix 补充 3-seed runs。\n\n**W2** [warning] SJ Hungarian matching 缺 threshold 规范\n\n- **具体位置**: Eq.(4), Section 3.2\n- **问题**: Eq.(4) 现在已定义 sim = token-level IoU，g_i/g_j = per-type extraction counts（比 Round 1 改善显著）。但 Hungarian algorithm 是否有 minimum similarity threshold？如果 threshold=0，两个完全不相关的 span 也会被 matched，导致 SJ numerator 非零。如果 threshold>0，threshold 的选择影响所有下游 ρ 值但未报告。\n- **建议**: 明确说明是否使用 threshold（以及值），或解释为什么 zero-overlap matches 对 SJ 影响可忽略。\n\n**W3** [warning] RE selection 无统计检验\n\n- **具体位置**: Table 3, Section 5.3\n- **问题**: NER selection 报告了完整 bootstrap（p=0.39, CI [-3.0, +4.2]pp, Cohen's d=0.038, sign test）。RE selection 仅报告 \"no signal exceeds greedy (0.404) despite 18.1 pp of oracle headroom\"，无 p-value、CI 或 effect size。RE 的 selection gap 实际更大（greedy 胜出），理应同样给出统计检验。\n- **建议**: 补充 RE selection 的 bootstrap p-value 和 CI。\n\n**W4** [warning] SciERC cross-model 不对称（N=8）\n\n- **具体位置**: Table 1; Appendix A.3\n- **问题**: Table 1 SciERC 列仅为 Qwen 结果（表头未标注模型），LLaMA SciERC 仅在 Appendix 文字中零散出现（SJ ρ=0.363, FK ρ=0.327），不完整（5 个信号只报了 2 个），无 AUROC，无 table。SciERC 是驱动核心 claims 的 primary dataset，cross-model validation 的缺失在此处比在 CoNLL 上更关键。\n- **建议**: Table 1 增加 SciERC (LLaMA) 列，或在 Appendix 补完整 table。\n\n**W5** [warning] n=529 vs SciERC n=551 的 discrepancy\n\n- **具体位置**: Section 5.3 (\"over n=529 NER instances\")\n- **问题**: SciERC test set 有 551 instances，但 bootstrap 用 n=529。22 instances 被 drop 的原因未交代。如果是 filtering（如 zero-entity instances），应明确说明 filtering criteria。\n- **建议**: 一句话说明 n=529 的来源。\n\n---\n\n## 小问题（不影响接收）\n\n- Eq.(4) 分母 $\\sum_g \\max(|g_i|, |g_j|)$ 是非标准 Jaccard variant，一句解释为何不用 $|A \\cup B|$ 会帮助理解。\n- FK adaptation (Section 3.2)：N 个来自同一模型的 stochastic samples 不是 Fleiss' κ 假设的 \"independent raters\"，brief acknowledgment 即可。\n- Table 3 的 EM 行显示 \"---\" 但 caption 未解释原因，caption 可加 \"EM produces binary agreement without sample ranking.\"——实际 caption 已有此句 ✓，但 RE 列也是 \"---\"，可考虑统一 footnote 说明。\n- Section 5.3：\"three random seeds (42, 123, 456) refer to independent inference runs\"——但 Table 1 的 N=8 primary results 未说明用了哪个 seed 或是否 averaged。\n\n---\n\n## Questions for Authors\n\n**Q1.** WNUT-17 上 Voting/EM/FK/Logprob 的 ρ 和 AUROC 分别是多少？如果全部 non-significant，这本身是一个强结论；如果某个信号显著，则 \"all signals break down\" 需要修正。\n\n**Q2.** CoNLL 的 best-of-N selection 结果（即使 greedy 已 >0.91）？一个可能的 outcome 是 oracle headroom 很小 → selection gap 不存在 → 说明 gap 是 hard-task specific，这也是有价值的 insight。\n\n**Q3.** SciERC bootstrap n=529：22 instances 被 drop 的 criteria 是什么？\n\n**Q4.** SJ Hungarian matching 是否有 minimum similarity threshold？如果无 threshold，matched pairs 中 sim≈0 的比例有多高？\n\n**Q5.** Table 1 的 N=8 主要结果是 single-seed 还是 averaged？如果 single-seed，是否有 variance estimates？\n\n---\n\n## Round 0-1 遗留 Issue 状态判定\n\n| Issue | 状态 | 判定依据 |\n|-------|------|----------|\n| **R1-N1** [critical]: Bootstrap 检验细节不足 | ✅ **Resolved** | Section 5.3 补齐：n=529, B=10K, paired, percentile 95% CIs [-3.0, +4.2]pp, Cohen's d=0.038, sign test 61W/70L, seeds(42/123/456) 含义明确 |\n| **R1-N2** [critical]: Correlation-selection gap 解释力不足 | ✅ **Resolved** | Discussion 清晰区分 instance-level（rank instances）vs per-sample（rank candidates within instance）；logprob 失败归因于 constrained decoding grammar compliance + 75% ties |\n| **R1-N3** [warning]: Per-sample signal 仅 logprob | ✅ **Resolved** | Section 3.3 明确 consensus-proximity = LOO-SJ；Appendix 验证 LOO-SJ Δρ=-0.014（negligible circularity） |\n| **R1-W1** [warning]: SJ 形式化有歧义 | ⚠️ **Partially resolved** | sim = token-level IoU ✓, g_i/g_j = per-type extraction counts ✓, Hungarian threshold 仍未指定 |\n| **R1-W2** [warning]: Voting-SJ 冗余度 | ✅ **Resolved** | 报告 inter-signal ρ=0.659 (NER), 0.605 (RE) + differential behavior across difficulty 论述 |\n| **R0-W4/R1-N1** [critical]: 统计检验不系统 | ⚠️ **Partially resolved** | Selection 有完整 bootstrap ✓；QE Table 1 N=8 仍为 point estimates without CIs |\n| **R1-W4** [warning]: Logprob 温度敏感性 | ✅ **Resolved** | Section 5.4 + Limitations 均明确 acknowledge T=0.7 logprob data missing |\n| **R1-W6** [warning]: LLaMA fine-tuning 状态 | ✅ **Resolved** | Section 4.1: 两模型 identical LoRA (rank=32, α=64), 5 epochs, LLaMA Factory |\n| **R1-W7** [warning]: 约束解码影响 | ✅ **Resolved** | Discussion: acknowledged constrained decoding compresses diversity + random baseline gap 3.6pp confirms variance exists + future work identified |\n| **R0-C3** [critical]: RE 仅 SciERC | ✅ **Resolved** | Introduction/Discussion/Conclusion/Appendix 四处 hedge |\n\n---\n\n## 主要优势\n\n1. **概念贡献清晰**: QE vs selection 的 distinction 是 generative IE 社区需要的，且 formulation (Section 3.1 per-sample vs instance-level) 精确可操作。\n2. **Quality estimation 分析全面**: 5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic，分析深度超过多数实证论文。\n3. **Bootstrap 规范（selection）**: Cohen's d、sign test、percentile CI、seed 解释一应俱全，是 NLP 实证论文的良好标准。\n4. **ρ-AUROC dissociation 的发现**: EM 在 ρ 排名低但 AUROC 领先（Section 5.1），揭示 binary vs continuous signal properties 的 metric-dependent 行为，对 practitioners 有直接 actionable 价值。\n5. **诚实的 hedging**: RE single-dataset 限制在 4 处 acknowledge，logprob temperature gap 在正文 + Limitations 双重标注——Round 0-1 的 self-awareness 问题已有实质改善。\n6. **与 Nédellec et al. (2026) 的定位清晰**: 三点差异化（structural matching / selection analysis / difficulty gradient）具体且有说服力。\n\n---\n\n## 总结\n\n论文从 Round 0 到 Round 2 有显著改善：bootstrap 规范化、SJ 形式化、RE hedging、constrained decoding 讨论等遗留问题大多已 resolved 或 partially resolved。Quality estimation 分析是本文的强项，coverage 和 depth 均达到 long paper 标准。\n\n主要 concern 集中在 evidence breadth vs framing breadth 的 mismatch：correlation-selection gap 作为核心贡献，仅在 1 dataset × 1 model 上验证（N1）；WNUT-17 boundary 作为 listed contribution，仅有 1 个不显著的数据点（N2）。如果这两个问题得到补充，论文有 Conference 实力；当前状态更适合 Findings。\n\n**Overall**: 3.5/5 (Borderline Conference / Strong Findings)\n**Confidence**: 4/5",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-15T02:48:19.893930+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4217
}
```

</details>

---


### Assistant

_source line 220 · 2026-05-15T02:48:28.194993+00:00_

Round 2 审稿意见已提交给 Review Director。

核心判断：**3.5/5 (Borderline Conference / Strong Findings)**。

相比 Round 0-1 改善显著——bootstrap 规范、SJ 形式化、RE hedging、constrained decoding 讨论等遗留问题大多 resolved。Quality estimation 分析达到 long paper 标准。

两个 Must-Fix 问题阻碍 Conference 推荐：
1. **Selection gap 证据面过窄**：核心贡献仅在 SciERC/Qwen 1 个 setting 验证，但 framing 为 "fundamental disconnect"
2. **WNUT-17 boundary claim 无系统数据**：仅 SJ 一个不显著的 ρ 值支撑 "all signals break down" 的 Contribution #3

补齐这两处后可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 221 · 2026-05-15T02:49:40.819589+00:00_

[Round 2 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 — Round 2 审稿意见（新颖性 + 完整性 + 格式）

### Summary

本文系统比较了五种来自三个family的confidence signals（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在generative IE（NER + RE）中的quality estimation和sample selection表现。核心发现是"correlation-selection gap"：instance-level consistency signals是有效的quality estimators（ρ达0.38, AUROC达0.75），但无法可靠超越greedy decoding进行best-of-N selection（p>0.39），尽管存在13-18pp的oracle headroom。附带发现signal ranking随task difficulty变化。

### Must-Fix 问题

**N1** [critical] ρ=0.38 仍缺乏跨方法数值对比（R1-W3 部分未解决）
- 位置：§4.2 第一段；§5 Discussion 第一段
- 问题：论文将ρ=0.38 contextualize为"14% variance explained"和AUROC=0.749，但这是intra-study context。读者无法判断0.38在confidence estimation文献中的位置——semantic entropy (Kuhn 2023)在QA上报告AUROC通常0.75-0.85，P(True) (Kadavath 2022)也有公开ρ值。论文§2引用了这些方法但零数值对比。
- 影响：若ρ=0.38属于typical甚至below-average，则"effective quality estimators"的framing需重新校准。
- 建议：§4.2或§5加footnote，引用已有方法的典型值，明确structured IE与discrete-answer tasks直接比较的困难性。

**N2** [critical] Selection实验仅在SciERC上进行，未解释CoNLL/WNUT-17的缺失
- 位置：Table 3
- 问题：Best-of-N selection仅报告SciERC，但核心claim是gap在IE中普遍存在。CoNLL headroom可能极小、WNUT-17样本质量太低——但这些reasoning需要stated。
- 影响：三数据集quality estimation → 一数据集selection验证，逻辑链不完整。
- 建议：补充CoNLL/WNUT-17 selection结果（即使headroom为0也有信息量），或明确说明omission原因并给出oracle-greedy gap。

### Should-Fix 问题

**W1** [warning] Constrained decoding作为全局confound未充分讨论
- 位置：§5 "Why logprob fails" 段
- 问题：constrained decoding压缩per-sample diversity的影响不仅限于logprob，可能影响所有signal的selection表现。论文仅在logprob段落提及，未在Limitations中列为key confound。
- 建议：Limitations section明确列出，或提供per-sample F1 variance数据证明diversity已足够。

**W2** [warning] Abstract "across NER and relation extraction on three datasets" 可能误导
- 位置：Abstract line 3
- 问题：RE实际仅在SciERC上评估。
- 建议：改为"across NER (three datasets) and RE (SciERC)"或类似表述。

**W3** [warning] WNUT-17对"三数据集difficulty gradient"的贡献有限
- 位置：§4.2 line 76；Contribution 3
- 问题：WNUT-17 SJ ρ=0.082 (p=0.106)，信号与F1的相关性不显著，本质上是negative control。
- 建议：明确定位为"capability boundary probe"而非同等地位的evaluation benchmark。

**W4** [warning] EM用于selection的缺失未充分解释
- 位置：Table 3 "---" for EM
- 问题：EM<1时majority output可被识别，picking majority output就是standard self-consistency voting。未解释为何不以此方式使用EM。
- 建议：实现majority-vote selection并报告，或解释为何majority在structured IE中不well-defined。

### Minor Issues

- M1: Ethics Statement section缺失
- M2-M3: bib条目检查（无实质问题）

### Overall: 3.5（Borderline Conference），Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-15T02:50:59.440748+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 审稿意见\n\n---\n\n### R2-N1: ρ=0.38 缺乏跨方法数值对比\n\n**[AGREE]** R2-N1: 同意需要 contextualization，但对 \"critical\" 级别保留意见。\n\nρ=0.38 的绝对水平确实缺乏 external anchor。论文 §2 (Related Work) 引用了 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 等方法但未给出任何数值对比，读者无法判断 0.38 在 confidence estimation 领域中的相对位置。R2 的建议（加 footnote contextualize）是合理且 low-cost 的改进。\n\n但我认为这是 **should-fix 而非 must-fix**，原因：(1) structured IE 与 discrete-answer QA 的 output space 根本不同，direct numerical comparison 有误导风险——ρ 在 set-valued output 上的天花板可能远低于 single-token tasks；(2) 论文已从两个维度 contextualize（14% variance explained + AUROC=0.749 的 binary discrimination），不算完全缺失 context。建议作者加一段说明 cross-task comparison 的困难性，同时给出可引用的外部数值（如 semantic entropy QA AUROC 范围）作为 calibration point。\n\n---\n\n### R2-N2: Selection 实验仅在 SciERC 上进行\n\n**[AGREE]** R2-N2: 完全同意，与我的 R1-N1 一致。\n\n这是本轮审稿最重要的 issue。Table 3 (Section 5.3) 的 selection 分析仅覆盖 SciERC/Qwen，但 correlation-selection gap 被 framed 为 generative IE 中的 \"fundamental disconnect\"（Abstract, Introduction Contribution #2, Conclusion）。Quality estimation 有 3 datasets × 2 models，selection 仅 1 × 1，逻辑链存在明显断裂。\n\nR2 进一步指出 CoNLL headroom 可能极小、WNUT-17 样本质量低——这些 reasoning 即使结论是 \"gap 不存在 / headroom 为零\"，也是有信息量的 insight（说明 gap 可能是 hard-task specific）。我在自己的 Q2 中也提了同样的问题。两位 reviewer 独立指出同一问题，should strengthen the signal to authors。\n\n---\n\n### R2-W1: Constrained decoding 作为全局 confound\n\n**[AGREE]** R2-W1: 同意 constrained decoding 的影响应扩大讨论范围。\n\n论文 Discussion §5 \"Why logprob fails\" 段落提到 \"Constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity\"，但仅在 logprob context 下讨论。R2 正确指出：如果 constrained decoding 压缩 per-sample diversity，这影响的不仅是 logprob，还包括所有 signal 的 selection 表现——因为 consensus-proximity selection（SJ/Voting 的 selection 策略，Section 3.3）也依赖 per-sample 差异来区分候选。\n\n论文 Limitations section 确实未将 constrained decoding 列为 key confound（当前 Limitations 讨论：dataset coverage、model scale、unsupervised-only signals、N range、SJ-FK gap）。建议：(1) Limitations 增加 constrained decoding 条目，或 (2) 报告 per-sample F1 variance（Table 3 已有 random baseline 0.608 vs greedy 0.644，间接说明 variance 存在，但 explicit variance 数据更有力）。\n\n---\n\n### R2-W2: Abstract \"across three datasets\" 可能误导 RE 覆盖度\n\n**[AGREE]** R2-W2: 同意 Abstract 措辞需修正。\n\nAbstract 第 3 句：\"across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17)\"——自然读法是 NER + RE 均在三个数据集上评估，但实际 RE 仅在 SciERC 上进行（CoNLL 和 WNUT-17 仅有 NER）。虽然 Introduction Contribution #1 和 Discussion 已正确 hedge（\"our RE conclusions are based on a single benchmark\"），但 Abstract 作为 first impression 应自洽。R2 的建议 \"across NER (three datasets) and RE (SciERC)\" 或类似表述是简单且准确的 fix。\n\n---\n\n### R2-W3: WNUT-17 贡献定位\n\n**[AGREE]** R2-W3: 同意，且认为问题比 R2 描述的更严重。\n\nR2 建议将 WNUT-17 明确定位为 \"capability boundary probe\" 而非同等地位的 evaluation benchmark，这是合理的。但我在 R1-N2 中指出了一个更基本的问题：**全文仅报告 SJ 一个信号在 WNUT-17 上的 ρ（0.082, p=0.106），其他四个信号的 WNUT-17 结果完全缺失**。\"All signals converge when model capability is insufficient\" 这一 claim 用单个不显著的数据点支撑，逻辑上不成立。即使降级为 \"probe\"，也需要报告全部 5 signals 的数据才能支持 \"all signals break down\" 的结论。\n\n---\n\n### R2-W4: EM 用于 selection 的缺失\n\n**[REBUT]** R2-W4: 部分反驳——majority-vote selection 在 structured IE 中确实 ill-defined，但论文可以更好地解释。\n\nR2 指出当 EM<1 时，majority output 可被识别，picking majority output 就是 standard self-consistency voting。这在 discrete-answer tasks 中成立（majority vote = 最频繁的答案），但在 structured IE 中有根本性困难：\n\n1. **Exact match 在 entity sets 间极为稀少**。Section 5.1 的 conditional filtering 分析暗示大量 instances 的 EM<1 不是因为有清晰的 majority + minority 分组，而是因为 N 个 outputs 各不相同（partial overlap），此时 \"majority\" 可能只有 1-2 个完全相同的 sample，其余都是不同的 partial extractions。\n2. **论文 Section 3.3 已提供替代方案**：consensus-proximity selection（选择与 consensus 最接近的 sample）本质上是 soft majority vote，已在 Table 3 中报告（SJ selection）。\n\n但 R2 的批评有合理之处：Table 3 caption 说 \"EM produces binary agreement without sample ranking\" 过于简略——当 EM<1 时，确实有一个 plurality output，论文应解释为什么不使用它。建议：在 Section 3.3 或 Table 3 caption 加 1-2 句说明 exact-match plurality 在 structured output 中的退化问题（plurality 通常仅 1-2 samples，selection 等同于 near-random）。\n\n---\n\n### R2-M1: Ethics Statement 缺失\n\n**[REBUT]** R2-M1: ARR submission 通过 Responsible NLP Checklist 履行 ethics review，不要求单独的 Ethics Statement section。\n\nACL ARR CFP 要求作者提交 Responsible NLP Research Checklist（作为 submission 的一部分），但不要求在正文中包含单独的 \"Ethics Statement\" section。部分 *ACL venues（如 NAACL 2024）曾要求 separate section，但 ARR 2025-2026 的 Author Guidelines 明确通过 checklist 完成此功能。除非作者的工作涉及 human subjects、sensitive data 等需要 extended discussion 的伦理问题（本文不涉及——全部使用公开 benchmark、无 human annotation），缺少 separate Ethics Statement section 不构成格式违规。\n\n---\n\n### 总结\n\n| R2 Issue | 我的回应 | 与我自己 issues 的关系 |\n|----------|---------|----------------------|\n| R2-N1 (ρ=0.38 无 external context) | [AGREE] 但建议降级为 should-fix | 新视角，我未提出 |\n| R2-N2 (selection 仅 SciERC) | [AGREE] 完全同意 | = R1-N1 |\n| R2-W1 (constrained decoding 全局 confound) | [AGREE] 应扩大讨论范围 | 补充我的 minor 观察 |\n| R2-W2 (Abstract RE 措辞) | [AGREE] 简单 fix | 我未明确提出 |\n| R2-W3 (WNUT-17 定位) | [AGREE] 但问题更严重 | ⊂ R1-N2（我的更强） |\n| R2-W4 (EM majority-vote selection) | [REBUT] structured IE 中 ill-defined | 新视角 |\n| R2-M1 (Ethics Statement) | [REBUT] ARR 通过 checklist 完成 | 格式判断 |\n\n**两位 reviewer 的共识 critical issues**: (1) selection 证据面过窄（R1-N1 = R2-N2），(2) WNUT-17 数据不足（R1-N2 ⊃ R2-W3）。这两个问题如果得到补充，论文从 3.5 提升到 4.0 是可期的。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 审稿意见\n\n---\n\n### R2-N1: ρ=0.38 缺乏跨方法数值对比\n\n**[AGREE]** R2-N1: 同意需要 contextualization，但对 \"critical\" 级别保留意见。\n\nρ=0.38 的绝对水平确实缺乏 external anchor。论文 §2 (Related Work) 引用了 semantic entropy (Kuhn 2023)、P(True) (Kadavath 2022)、CoCoA (Vashurin 2025) 等方法但未给出任何数值对比，读者无法判断 0.38 在 confidence estimation 领域中的相对位置。R2 的建议（加 footnote contextualize）是合理且 low-cost 的改进。\n\n但我认为这是 **should-fix 而非 must-fix**，原因：(1) structured IE 与 discrete-answer QA 的 output space 根本不同，direct numerical comparison 有误导风险——ρ 在 set-valued output 上的天花板可能远低于 single-token tasks；(2) 论文已从两个维度 contextualize（14% variance explained + AUROC=0.749 的 binary discrimination），不算完全缺失 context。建议作者加一段说明 cross-task comparison 的困难性，同时给出可引用的外部数值（如 semantic entropy QA AUROC 范围）作为 calibration point。\n\n---\n\n### R2-N2: Selection 实验仅在 SciERC 上进行\n\n**[AGREE]** R2-N2: 完全同意，与我的 R1-N1 一致。\n\n这是本轮审稿最重要的 issue。Table 3 (Section 5.3) 的 selection 分析仅覆盖 SciERC/Qwen，但 correlation-selection gap 被 framed 为 generative IE 中的 \"fundamental disconnect\"（Abstract, Introduction Contribution #2, Conclusion）。Quality estimation 有 3 datasets × 2 models，selection 仅 1 × 1，逻辑链存在明显断裂。\n\nR2 进一步指出 CoNLL headroom 可能极小、WNUT-17 样本质量低——这些 reasoning 即使结论是 \"gap 不存在 / headroom 为零\"，也是有信息量的 insight（说明 gap 可能是 hard-task specific）。我在自己的 Q2 中也提了同样的问题。两位 reviewer 独立指出同一问题，should strengthen the signal to authors。\n\n---\n\n### R2-W1: Constrained decoding 作为全局 confound\n\n**[AGREE]** R2-W1: 同意 constrained decoding 的影响应扩大讨论范围。\n\n论文 Discussion §5 \"Why logprob fails\" 段落提到 \"Constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity\"，但仅在 logprob context 下讨论。R2 正确指出：如果 constrained decoding 压缩 per-sample diversity，这影响的不仅是 logprob，还包括所有 signal 的 selection 表现——因为 consensus-proximity selection（SJ/Voting 的 selection 策略，Section 3.3）也依赖 per-sample 差异来区分候选。\n\n论文 Limitations section 确实未将 constrained decoding 列为 key confound（当前 Limitations 讨论：dataset coverage、model scale、unsupervised-only signals、N range、SJ-FK gap）。建议：(1) Limitations 增加 constrained decoding 条目，或 (2) 报告 per-sample F1 variance（Table 3 已有 random baseline 0.608 vs greedy 0.644，间接说明 variance 存在，但 explicit variance 数据更有力）。\n\n---\n\n### R2-W2: Abstract \"across three datasets\" 可能误导 RE 覆盖度\n\n**[AGREE]** R2-W2: 同意 Abstract 措辞需修正。\n\nAbstract 第 3 句：\"across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17)\"——自然读法是 NER + RE 均在三个数据集上评估，但实际 RE 仅在 SciERC 上进行（CoNLL 和 WNUT-17 仅有 NER）。虽然 Introduction Contribution #1 和 Discussion 已正确 hedge（\"our RE conclusions are based on a single benchmark\"），但 Abstract 作为 first impression 应自洽。R2 的建议 \"across NER (three datasets) and RE (SciERC)\" 或类似表述是简单且准确的 fix。\n\n---\n\n### R2-W3: WNUT-17 贡献定位\n\n**[AGREE]** R2-W3: 同意，且认为问题比 R2 描述的更严重。\n\nR2 建议将 WNUT-17 明确定位为 \"capability boundary probe\" 而非同等地位的 evaluation benchmark，这是合理的。但我在 R1-N2 中指出了一个更基本的问题：**全文仅报告 SJ 一个信号在 WNUT-17 上的 ρ（0.082, p=0.106），其他四个信号的 WNUT-17 结果完全缺失**。\"All signals converge when model capability is insufficient\" 这一 claim 用单个不显著的数据点支撑，逻辑上不成立。即使降级为 \"probe\"，也需要报告全部 5 signals 的数据才能支持 \"all signals break down\" 的结论。\n\n---\n\n### R2-W4: EM 用于 selection 的缺失\n\n**[REBUT]** R2-W4: 部分反驳——majority-vote selection 在 structured IE 中确实 ill-defined，但论文可以更好地解释。\n\nR2 指出当 EM<1 时，majority output 可被识别，picking majority output 就是 standard self-consistency voting。这在 discrete-answer tasks 中成立（majority vote = 最频繁的答案），但在 structured IE 中有根本性困难：\n\n1. **Exact match 在 entity sets 间极为稀少**。Section 5.1 的 conditional filtering 分析暗示大量 instances 的 EM<1 不是因为有清晰的 majority + minority 分组，而是因为 N 个 outputs 各不相同（partial overlap），此时 \"majority\" 可能只有 1-2 个完全相同的 sample，其余都是不同的 partial extractions。\n2. **论文 Section 3.3 已提供替代方案**：consensus-proximity selection（选择与 consensus 最接近的 sample）本质上是 soft majority vote，已在 Table 3 中报告（SJ selection）。\n\n但 R2 的批评有合理之处：Table 3 caption 说 \"EM produces binary agreement without sample ranking\" 过于简略——当 EM<1 时，确实有一个 plurality output，论文应解释为什么不使用它。建议：在 Section 3.3 或 Table 3 caption 加 1-2 句说明 exact-match plurality 在 structured output 中的退化问题（plurality 通常仅 1-2 samples，selection 等同于 near-random）。\n\n---\n\n### R2-M1: Ethics Statement 缺失\n\n**[REBUT]** R2-M1: ARR submission 通过 Responsible NLP Checklist 履行 ethics review，不要求单独的 Ethics Statement section。\n\nACL ARR CFP 要求作者提交 Responsible NLP Research Checklist（作为 submission 的一部分），但不要求在正文中包含单独的 \"Ethics Statement\" section。部分 *ACL venues（如 NAACL 2024）曾要求 separate section，但 ARR 2025-2026 的 Author Guidelines 明确通过 checklist 完成此功能。除非作者的工作涉及 human subjects、sensitive data 等需要 extended discussion 的伦理问题（本文不涉及——全部使用公开 benchmark、无 human annotation），缺少 separate Ethics Statement section 不构成格式违规。\n\n---\n\n### 总结\n\n| R2 Issue | 我的回应 | 与我自己 issues 的关系 |\n|----------|---------|----------------------|\n| R2-N1 (ρ=0.38 无 external context) | [AGREE] 但建议降级为 should-fix | 新视角，我未提出 |\n| R2-N2 (selection 仅 SciERC) | [AGREE] 完全同意 | = R1-N1 |\n| R2-W1 (constrained decoding 全局 confound) | [AGREE] 应扩大讨论范围 | 补充我的 minor 观察 |\n| R2-W2 (Abstract RE 措辞) | [AGREE] 简单 fix | 我未明确提出 |\n| R2-W3 (WNUT-17 定位) | [AGREE] 但问题更严重 | ⊂ R1-N2（我的更强） |\n| R2-W4 (EM majority-vote selection) | [REBUT] structured IE 中 ill-defined | 新视角 |\n| R2-M1 (Ethics Statement) | [REBUT] ARR 通过 checklist 完成 | 格式判断 |\n\n**两位 reviewer 的共识 critical issues**: (1) selection 证据面过窄（R1-N1 = R2-N2），(2) WNUT-17 数据不足（R1-N2 ⊃ R2-W3）。这两个问题如果得到补充，论文从 3.5 提升到 4.0 是可期的。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-15T02:51:03.762455+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 224 · 2026-05-15T02:51:10.331678+00:00_

交叉回应已提交。

核心判断：R2 的 7 个 issues 中我 **AGREE 5 个、REBUT 2 个**。

两位 reviewer 独立一致的 critical issues：
1. **Selection 证据面过窄**（R1-N1 = R2-N2）——correlation-selection gap 仅 SciERC/Qwen 验证
2. **WNUT-17 数据不足**（R1-N2 ⊃ R2-W3）——我的版本更强，指出全部 5 signals 结果缺失

反驳了两点：
- **R2-W4**（EM majority-vote selection）：structured IE 中 exact-match plurality 退化严重，consensus-proximity（SJ selection）已是 soft 版本的 majority vote
- **R2-M1**（Ethics Statement）：ARR 通过 Responsible NLP Checklist 完成，不要求 separate section

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

46 recorded events


### User

_source line 225 · 2026-05-15T03:57:28.366506+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## 审稿对象
- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）
- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）
- 截止日期：2026-05-25
- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind

## 你的审查侧重

### 1. 方法定义严谨性
- 5 个 confidence signal（logprob, EM, FK, SJ, voting）的数学定义是否清晰、无歧义
- Soft Jaccard 的 Hungarian matching + token-level IoU 定义是否完整（threshold? denominator 选择理由？）
- Per-sample vs instance-level 信号的区分是否准确且一致
- "Correlation-selection gap" 概念是否严格定义，还是仅为经验观察的命名

### 2. 实验设计
- 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否覆盖足够的 difficulty gradient
- N=8/16 的采样规模是否足够，是否需要更大 N 的实验
- 两个模型（Qwen3-8B, LLaMA-3.1-8B）是否足以支撑跨模型结论
- LoRA fine-tuning 设置是否公平（rank=32, α=64, 5 epochs）
- 温度设置（T=0.7, T=1.0）是否充分

### 3. 统计检验
- Bootstrap resampling（B=10,000）的规范是否完整
- p-value、CI、effect size 报告是否充分
- 多重比较校正是否需要但缺失
- "no signal reliably surpasses greedy" 的统计论证是否严谨

### 4. 数据一致性
- 表格数字与正文引用是否一致
- 不同 section 对同一实验结果的描述是否矛盾
- Figure 和 Table 的引用是否完整

### 5. RE 单数据集问题
- RE 结论仅基于 SciERC，论文是否对此做了充分的措辞限定
- 44% zero-F1 对 RE 信号评估的影响是否充分讨论

请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-15T03:57:55.586044+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-15T03:57:55.636789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-15T03:58:00.372171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-15T03:58:02.382916+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-15T03:58:02.835610+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-15T03:58:03.388323+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-15T03:58:03.539565+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-15T03:58:03.540040+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-15T03:58:03.590610+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-15T03:58:07.458038+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of t
…[truncated 1293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7085
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-15T03:58:22.745974+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 237 · 2026-05-15T03:58:22.746376+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-15T03:58:23.454231+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-15T03:58:28.298479+00:00_

Error: result (8,755,474 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4844
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-15T03:58:36.733091+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5, 1-10, etc.), descriptions for each score level, and any required fields. I need the exact scoring criteria for soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5, 1-10, etc.), descriptions for each score level, and any required fields. I need the exact scoring criteria for soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-15T03:58:37.538458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-15T03:58:37.992587+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-15T03:58:37.993097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-15T03:58:38.899343+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-15T03:58:39.000084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-15T03:58:39.101058+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-15T03:58:39.101538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-15T03:58:39.152126+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-15T03:58:44.236500+00:00_

# ACL ARR Review Form Scoring Dimensions

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 scale with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5 scale with half-point increments)
- **5**: "Consider for Award: could be considered for an outstanding paper award (top 2.5%)."
- **4**: "Conference: paper could be accepted to an *ACL conference."
- **3**: "Findings: paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: paper needs substantial revisions."
- **1**: "Do not resubmit: paper has to be fully redone or is not relevant."

## Reproducibility (1-5 scale)
- **5**: "They could easily reproduce t
…[truncated 690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7503
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-15T03:58:52.573385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-15T03:58:52.925386+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc c
…[truncated 10971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-15T03:58:53.076464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-15T03:58:53.880383+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\rho{=}0.724$, conditional $\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quali
…[truncated 3455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-15T03:58:53.880832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-15T03:58:54.383398+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-s
…[truncated 2466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-15T03:58:54.534385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-15T03:58:54.534773+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several dire
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-15T03:58:55.438654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-15T03:58:55.439062+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-15T03:58:55.539795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-15T03:58:55.590617+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 14999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-15T04:00:24.599794+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-15T04:00:25.203756+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-15T04:01:09.630039+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 38090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 45030
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-15T04:01:10.622953+00:00_

Error: result (1,976,553 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 45419
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-15T04:01:23.885325+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null || python3 -c \"\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf')\n    print(f'Pages: {len(doc)}')\nexcept:\n    pass\n\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null || python3 -c \"\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf')\n    print(f'Pages: {len(doc)}')\nexcept:\n    pass\n\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-15T04:01:24.186739+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 15 03:36:45 2026 UTC
ModDate:         Fri May 15 03:36:45 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           15
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       522002 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-15T04:05:15.074714+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**：Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**：EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文系统比较了生成式信息抽取（IE）中五种置信度信号（三个家族：structural, surface, model-internal）用于质量估计和样本选择两个不同目标的表现。在 SciERC（NER+RE）、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是\"correlation-selection gap\"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n---\n\n## Strengths\n\n**S1. 清晰的问题分解与严谨的框架设计。** 将 quality estimation 与 sample selection 明确区分为两个独立目标（§3.1），并用不同指标（Spearman ρ + AUROC vs. best-of-N F1）分别评估，这一分析框架本身是对现有文献的有价值贡献。per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）使得后续分析的逻辑链条清晰可追溯。\n\n**S2. 全面的统计报告。** Bootstrap resampling (B=10,000) 附带 95% CI、Cohen's d、sign test win%（§4.3），pairwise Δρ CI（Appendix D），p-value 和 effect size 齐全。多数实证论文不会做到这个粒度。\n\n**S3. 诚实的 scope limitation 声明。** RE 单数据集问题在 Introduction（第46行）、Discussion（第10行）、Conclusion（第12行）、Limitations 四处明确提及，且 WNUT-17 作为 capability boundary 的诚实报告（full-set ρ=0.724 vs. conditional ρ=0.038，Table 7）都体现了良好的学术诚信。\n\n**S4. Task difficulty 分析有洞察力。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现（§4.2，CoNLL vs. SciERC），以及 conditional filtering 后信号排序翻转（Figure 2 right panel），为从业者的信号选择提供了实用指导。\n\n**S5. Soft Jaccard 信号设计合理。** 基于 type-aware Hungarian matching + token-level IoU 的 SJ 定义（Eq. 4-5）比简单的 surface matching 更适合结构化输出，对 Nédellec et al. (2026) 的 limitation (i) 有针对性的改进。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n\n- 具体位置：§5 Discussion 第25-27行，§Limitations 第15-16行\n- 问题：论文的核心发现——\"no signal reliably surpasses greedy\"——可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限。论文在 Discussion 中承认\"constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity\"，但仅作为 future work 提及，未设计任何对照实验。\n- 为什么影响接收：这是论文最核心 claim 的 validity threat。如果 constrained decoding 将 N 个样本压缩到近乎相同的输出空间，任何选择器都无法区分它们——这就不是信号本身的问题，而是实验设置的 artifact。论文用 random baseline gap（3.6pp）论证\"variance exists\"，但 3.6pp 可能远低于 unconstrained generation 的 variance，使得 gap 的量化可能不具有 generalizability。\n- 建议修改方向：（a）增加 unconstrained generation + post-hoc JSON parsing 的对照实验，即使 parse 失败率高，也能 characterize constrained vs. unconstrained 的 diversity 差异；或（b）报告 per-instance 样本间的 pairwise SJ 分布（当前已有此数据），量化 constrained decoding 下的实际 diversity level，并明确论述 gap 结论的 generalizability boundary 为 constrained decoding regime。\n\n**N2** [critical] \"No signal reliably surpasses greedy\" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence\n\n- 具体位置：§4.3 第128行，p=0.39, 95% CI: [−3.0, +4.2] pp\n- 问题：论文用 p>0.39（未能拒绝 H₀）论证\"no signal reliably surpasses greedy\"，但这只是 absence of evidence，不是 evidence of absence。标准 NHST 无法证明两种方法等价。CI 范围 [−3.0, +4.2] 涵盖了最大 +4.2pp 的可能增益，考虑到 13.2pp oracle headroom，这个区间并不能排除有意义的选择增益存在的可能。\n- 为什么影响接收：这是论文三大贡献之一（correlation-selection gap）的统计基础。如果统计检验的逻辑链条有缺陷，核心贡献的可信度受损。\n- 建议修改方向：（a）补充等价性检验（TOST, Two One-Sided Tests），设定临床等价边界（如 ±1pp 或 ±2pp），如果 90% CI 落入等价区间则可正式声明等价；（b）或补充 power analysis，说明当前样本量在给定 effect size 下的检测力；（c）至少将措辞从\"no signal reliably surpasses\"改为\"we found no significant evidence that any signal surpasses\"，并讨论检测力。\n\n**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证\n\n- 具体位置：Table 1 caption \"N=8 results use seed=42\"，§4.3 第126行\n- 问题：论文的核心 quality estimation 结果（Table 1 N=8 部分，覆盖 4 个主要配置）和 selection 结果（Table 2）全部基于单一 random seed。N=16 实验使用了 3 seeds 并报告了 σ（Table 1 下半部分），但这些只覆盖 LLaMA CoNLL 一个配置。SciERC 和 WNUT 的关键结论（如 Voting ρ=0.379、SJ ρ=0.360、EM AUROC=0.749）和 selection gap（p=0.39）都是 single-seed。\n- 为什么影响接收：信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 结果无法确认这些排序是否稳定。尤其对于 selection 结果，不同 seed 可能产生不同的 p-value。N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大（更少样本）。\n- 建议修改方向：对 SciERC N=8（核心配置）补充至少 3 seed 的结果并报告 mean ± σ。这在计算上是可行的（inference 成本已产生，只需换 seed 重跑）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 多重比较校正缺失\n\n- 具体位置：Table 8（Appendix D），§4.2 第65-66行 pairwise comparisons\n- 问题：论文在 Table 8 报告了 3 个 pairwise Δρ comparison，在正文中隐式进行了更多比较（5 signals × 4+ configurations）。SJ–EM 的\"borderline significant\"结果（CI lower bound +0.003）在任何 multiple comparison correction 下都不会 survive。\n- 建议：明确声明未做多重比较校正；对 borderline 结果的措辞应更谨慎（如\"suggestive\"而非\"Yes†\"）。\n\n**W2** [warning] \"Correlation-selection gap\" 概念的 novelty 部分为 tautological\n\n- 具体位置：§3.1 第10-11行，§5 Discussion 第13-14行\n- 问题：5 个信号中 4 个是 instance-level（by design 无法 per-sample 区分），1 个是 per-sample（logprob）。Instance-level 信号无法做 sample selection 是定义层面的必然结果，不是实验发现。真正有经验价值的发现是：（a）logprob 这个唯一的 per-sample 信号也失败了；（b）consensus-proximity 转换策略未能有效弥合这一 gap。论文将 tautological 部分和 non-trivial 部分混在一起作为一个统一的\"gap\"，降低了概念的锐度。\n- 建议：在 Discussion 中明确分离这两层论证：（1）instance-level 信号的结构性局限（by construction）；（2）logprob 的经验性失败（需要解释，论文已提供 constrained decoding 的解释）。这会使 contribution 更清晰。\n\n**W3** [warning] FK 独立性假设未经验证\n\n- 具体位置：§3.2 第37行：\"While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\"\n- 问题：Fleiss' κ 的理论基础要求 raters 独立。温度采样的样本之间共享同一模型参数和 prompt，远非独立。论文仅以一句话 hand-wave 这个问题，未提供任何经验性验证（如 permutation test 检验 inter-sample 相关性）。\n- 建议：至少报告 N=8 样本间的 average pairwise correlation 以 characterize 独立性偏离程度，或在 Limitations 中更明确讨论这对 FK 值解释性的影响。\n\n**W4** [warning] SJ 定义中 Hungarian matching 的 cost function 未明确指定\n\n- 具体位置：§3.2 Eq. 4，第42-46行\n- 问题：论文说\"compute bipartite matching via the Hungarian algorithm with span overlap\"，但未明确说明是最大化 IoU（benefit）还是最小化 1-IoU（cost），也未说明 \"without minimum similarity threshold\" 的具体含义——是否允许 IoU=0 的匹配对？如果允许，一个完全不相关的 entity 被 matched 后贡献 sim=0 到分子但占据分母的一个位置，可能影响 SJ 的行为。\n- 建议：补充一到两句明确 Hungarian algorithm 的优化目标（max-weight matching on IoU scores）和 zero-IoU pairs 的处理方式。\n\n**W5** [warning] 两个模型均为 8B 参数，\"cross-model\" 结论的外推受限\n\n- 具体位置：§Limitations 第4-6行\n- 问题：Qwen3-8B 和 LLaMA-3.1-8B 代表的是同一参数量级的两个架构。论文多处使用\"cross-model consistency\"（如§4.2 第77行），但这更准确地说是\"cross-architecture consistency at fixed scale\"。论文在 Limitations 中提到 70B+ 模型未测试，但正文的措辞给人的印象是 cross-model 结论比实际更强。\n- 建议：在正文中将\"cross-model\"替换为\"cross-architecture\"或加限定词（如\"cross-model (at 8B scale)\"），更准确地反映实际覆盖范围。\n\n**W6** [warning] Consensus-proximity 是唯一的 instance-to-sample 转换策略，未比较替代方案\n\n- 具体位置：§3.3 第67行\n- 问题：将 instance-level 信号转为 per-sample 信号的策略（选择最接近 consensus 的样本）与 Minimum Bayes Risk (MBR) decoding 的 utility-maximization formulation 等价（Vashurin et al. 2025 已引用但未建立此联系）。论文未讨论其他可能的转换策略（如 diversity-weighted selection、centroid-based selection with different distance metrics）。如果 consensus-proximity 是次优策略，correlation-selection gap 可能被高估。\n- 建议：（a）明确与 MBR decoding 的联系；（b）至少在 Discussion 中说明为何 consensus-proximity 是合理的默认选择，以及替代策略是否可能缩小 gap。\n\n---\n\n## Minor Issues（不影响接收）\n\n**M1.** WNUT-17 \"54% zero F1\" 数据不一致。§4.1 第11行称\"54% zero F1\"，但 Table 7（Appendix）显示 n=689（filtering gold-empty 后）中 conditional n=334（non-zero），即 355/689 ≈ 51.5% zero F1，与 54% 有 ~2.5pp 差距。请核实并统一。\n\n**M2.** Table 1 N=16 区域大面积空白。仅报告 LLaMA CoNLL 的 N=16 ρ 值，其余配置在 Appendix Table 5 中。建议至少在 Table 1 caption 中补充交叉引用，或考虑合并呈现。\n\n**M3.** EM 从 selection 实验中排除的理由（Table 2 caption：\"the probability of two identical structured outputs is negligible\"）缺乏经验支持。建议报告 N=8 实验中 exact match pairs 的实际频率以验证此声明。\n\n**M4.** LOO-SJ 验证（Appendix C 第126行）仅报告了 Δρ=−0.014 和 per-instance max Δρ=3.1×10⁻⁴。注意这两个量的量纲不同：前者是整体 Spearman ρ 的变化，后者似乎是 per-instance confidence score 的变化。请澄清 per-instance Δρ 的具体含义。\n\n**M5.** Figure 1 caption 中 \"p=0.39 for NER logprob\" 直接出现在 figure 描述中，但该 p 值来自 Table 2 的 selection 分析而非 figure 本身可视化的内容（figure 显示的是 correlation vs. selection bars）。Caption 中引入 figure 未直接呈现的统计结果容易造成混淆。\n\n**M6.** §4.2 第64行的脚注比较 semantic entropy AUROC（0.75-0.85 on QA）与本文 AUROC（0.749 on IE），并承认\"direct comparison is complicated\"。既然承认不可直接比较，建议删除或大幅缩短此脚注，避免给读者留下可比较的印象。\n\n**M7.** 引用格式：feng2025optimal 和 snell2024scaling 的 bib key 使用姓氏但 OpenAlex 返回的 first_author 为名字（Austin/Charlie），这是 bib key 命名惯例问题，不影响引用正确性。hobelsberger2025systematic 和 lightman2024verify 在 OpenAlex 未找到匹配，但两篇均为已知发表论文（后者为 ICLR 2024 paper），应为 API 限制。\n\n---\n\n## Questions to Authors\n\n**Q1.** 是否考虑过在 constrained decoding 之外运行 unconstrained generation 作为对照？即使 parse 成功率低，比较两种 regime 下的 per-sample diversity（如 pairwise SJ 分布）也能 calibrate correlation-selection gap 的 generalizability。\n\n**Q2.** Logprob 在 WNUT conditional set 上达到了所有信号中最高的 ρ=0.350（Table 7），这与主文中\"logprob 是最弱信号\"的叙述相矛盾。如何 reconcile 这一发现？是否暗示 logprob 在高难度 domain 的 capability boundary 区间反而有独特优势？\n\n**Q3.** LoRA rank=32 的选择是否影响了 sample diversity？更低的 rank 可能导致 fine-tuned 模型更接近 base model 的分布，potentially increasing diversity。是否做过 LoRA rank 的敏感性分析？\n\n**Q4.** Table 6（cross-configuration selection）中 LLaMA/SciERC N=16 configuration 下 SJ 和 FK 并列第一（0.649），但都低于 greedy（0.645→0.649 仅 +0.004pp）。N=16 是否提供了 selection 结果的 multi-seed bootstrap p-value？\n\n---\n\n## Missing References\n\n- **MBR decoding 相关文献**：Eikema & Aziz (2022, \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\") 和 Freitag et al. (2022, \"High Quality Rather Than High Model Probability\") 建立了 MBR decoding 的理论框架，本文的 consensus-proximity selection 与之直接相关但未讨论。\n- **Structured prediction 的 uncertainty 估计**：Malinin & Gales (2021, \"Uncertainty Estimation in Autoregressive Structured Prediction\") 讨论了序列级输出的 uncertainty estimation，与本文的 structured output uncertainty 有方法论联系。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法定义基本清晰，统计报告充分；但 constrained decoding 混淆变量未控制（N1）、failure-to-reject 逻辑不完整（N2）、核心结果 single-seed（N3）是三个显著的 soundness gap |\n| Excitement | 3/5 | Quality estimation vs. sample selection 的分离框架和 task-difficulty-dependent ordering 有实用价值；但 correlation-selection gap 中 instance-level 信号的部分是 tautological（W2），核心 insight 的 novelty 中等 |\n| Reproducibility | 3.5/5 | LoRA 超参、bootstrap B、seed、评估指标均有报告；但缺少代码/数据可用性声明，logprob T=0.7 数据缺失，EM selection 排除缺乏经验验证 |\n| Overall | 3/5 | Findings 水平。实验设计 mostly sound、写作质量高，但 N1-N3 三个 critical issues 共同削弱了核心贡献的可信度。若 N1（constrained decoding 对照）和 N3（multi-seed）能在修订中解决，可提升至 3.5 |\n| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、IE evaluation 领域，仔细审查了方法定义和统计分析 |\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings)\n**一句话总结**: 框架设计清晰、统计报告充分的经验性研究，但核心发现（correlation-selection gap）受 constrained decoding 混淆变量、single-seed 设计、和 failure-to-reject 论证逻辑三重限制，需要补充实验和统计修订以支撑论文的主要 claim。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**：Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**：EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文系统比较了生成式信息抽取（IE）中五种置信度信号（三个家族：structural, surface, model-internal）用于质量估计和样本选择两个不同目标的表现。在 SciERC（NER+RE）、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是\"correlation-selection gap\"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n---\n\n## Strengths\n\n**S1. 清晰的问题分解与严谨的框架设计。** 将 quality estimation 与 sample selection 明确区分为两个独立目标（§3.1），并用不同指标（Spearman ρ + AUROC vs. best-of-N F1）分别评估，这一分析框架本身是对现有文献的有价值贡献。per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）使得后续分析的逻辑链条清晰可追溯。\n\n**S2. 全面的统计报告。** Bootstrap resampling (B=10,000) 附带 95% CI、Cohen's d、sign test win%（§4.3），pairwise Δρ CI（Appendix D），p-value 和 effect size 齐全。多数实证论文不会做到这个粒度。\n\n**S3. 诚实的 scope limitation 声明。** RE 单数据集问题在 Introduction（第46行）、Discussion（第10行）、Conclusion（第12行）、Limitations 四处明确提及，且 WNUT-17 作为 capability boundary 的诚实报告（full-set ρ=0.724 vs. conditional ρ=0.038，Table 7）都体现了良好的学术诚信。\n\n**S4. Task difficulty 分析有洞察力。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现（§4.2，CoNLL vs. SciERC），以及 conditional filtering 后信号排序翻转（Figure 2 right panel），为从业者的信号选择提供了实用指导。\n\n**S5. Soft Jaccard 信号设计合理。** 基于 type-aware Hungarian matching + token-level IoU 的 SJ 定义（Eq. 4-5）比简单的 surface matching 更适合结构化输出，对 Nédellec et al. (2026) 的 limitation (i) 有针对性的改进。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n\n- 具体位置：§5 Discussion 第25-27行，§Limitations 第15-16行\n- 问题：论文的核心发现——\"no signal reliably surpasses greedy\"——可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物，而非置信度信号本身的固有局限。论文在 Discussion 中承认\"constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity\"，但仅作为 future work 提及，未设计任何对照实验。\n- 为什么影响接收：这是论文最核心 claim 的 validity threat。如果 constrained decoding 将 N 个样本压缩到近乎相同的输出空间，任何选择器都无法区分它们——这就不是信号本身的问题，而是实验设置的 artifact。论文用 random baseline gap（3.6pp）论证\"variance exists\"，但 3.6pp 可能远低于 unconstrained generation 的 variance，使得 gap 的量化可能不具有 generalizability。\n- 建议修改方向：（a）增加 unconstrained generation + post-hoc JSON parsing 的对照实验，即使 parse 失败率高，也能 characterize constrained vs. unconstrained 的 diversity 差异；或（b）报告 per-instance 样本间的 pairwise SJ 分布（当前已有此数据），量化 constrained decoding 下的实际 diversity level，并明确论述 gap 结论的 generalizability boundary 为 constrained decoding regime。\n\n**N2** [critical] \"No signal reliably surpasses greedy\" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence\n\n- 具体位置：§4.3 第128行，p=0.39, 95% CI: [−3.0, +4.2] pp\n- 问题：论文用 p>0.39（未能拒绝 H₀）论证\"no signal reliably surpasses greedy\"，但这只是 absence of evidence，不是 evidence of absence。标准 NHST 无法证明两种方法等价。CI 范围 [−3.0, +4.2] 涵盖了最大 +4.2pp 的可能增益，考虑到 13.2pp oracle headroom，这个区间并不能排除有意义的选择增益存在的可能。\n- 为什么影响接收：这是论文三大贡献之一（correlation-selection gap）的统计基础。如果统计检验的逻辑链条有缺陷，核心贡献的可信度受损。\n- 建议修改方向：（a）补充等价性检验（TOST, Two One-Sided Tests），设定临床等价边界（如 ±1pp 或 ±2pp），如果 90% CI 落入等价区间则可正式声明等价；（b）或补充 power analysis，说明当前样本量在给定 effect size 下的检测力；（c）至少将措辞从\"no signal reliably surpasses\"改为\"we found no significant evidence that any signal surpasses\"，并讨论检测力。\n\n**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证\n\n- 具体位置：Table 1 caption \"N=8 results use seed=42\"，§4.3 第126行\n- 问题：论文的核心 quality estimation 结果（Table 1 N=8 部分，覆盖 4 个主要配置）和 selection 结果（Table 2）全部基于单一 random seed。N=16 实验使用了 3 seeds 并报告了 σ（Table 1 下半部分），但这些只覆盖 LLaMA CoNLL 一个配置。SciERC 和 WNUT 的关键结论（如 Voting ρ=0.379、SJ ρ=0.360、EM AUROC=0.749）和 selection gap（p=0.39）都是 single-seed。\n- 为什么影响接收：信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 结果无法确认这些排序是否稳定。尤其对于 selection 结果，不同 seed 可能产生不同的 p-value。N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大（更少样本）。\n- 建议修改方向：对 SciERC N=8（核心配置）补充至少 3 seed 的结果并报告 mean ± σ。这在计算上是可行的（inference 成本已产生，只需换 seed 重跑）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 多重比较校正缺失\n\n- 具体位置：Table 8（Appendix D），§4.2 第65-66行 pairwise comparisons\n- 问题：论文在 Table 8 报告了 3 个 pairwise Δρ comparison，在正文中隐式进行了更多比较（5 signals × 4+ configurations）。SJ–EM 的\"borderline significant\"结果（CI lower bound +0.003）在任何 multiple comparison correction 下都不会 survive。\n- 建议：明确声明未做多重比较校正；对 borderline 结果的措辞应更谨慎（如\"suggestive\"而非\"Yes†\"）。\n\n**W2** [warning] \"Correlation-selection gap\" 概念的 novelty 部分为 tautological\n\n- 具体位置：§3.1 第10-11行，§5 Discussion 第13-14行\n- 问题：5 个信号中 4 个是 instance-level（by design 无法 per-sample 区分），1 个是 per-sample（logprob）。Instance-level 信号无法做 sample selection 是定义层面的必然结果，不是实验发现。真正有经验价值的发现是：（a）logprob 这个唯一的 per-sample 信号也失败了；（b）consensus-proximity 转换策略未能有效弥合这一 gap。论文将 tautological 部分和 non-trivial 部分混在一起作为一个统一的\"gap\"，降低了概念的锐度。\n- 建议：在 Discussion 中明确分离这两层论证：（1）instance-level 信号的结构性局限（by construction）；（2）logprob 的经验性失败（需要解释，论文已提供 constrained decoding 的解释）。这会使 contribution 更清晰。\n\n**W3** [warning] FK 独立性假设未经验证\n\n- 具体位置：§3.2 第37行：\"While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\"\n- 问题：Fleiss' κ 的理论基础要求 raters 独立。温度采样的样本之间共享同一模型参数和 prompt，远非独立。论文仅以一句话 hand-wave 这个问题，未提供任何经验性验证（如 permutation test 检验 inter-sample 相关性）。\n- 建议：至少报告 N=8 样本间的 average pairwise correlation 以 characterize 独立性偏离程度，或在 Limitations 中更明确讨论这对 FK 值解释性的影响。\n\n**W4** [warning] SJ 定义中 Hungarian matching 的 cost function 未明确指定\n\n- 具体位置：§3.2 Eq. 4，第42-46行\n- 问题：论文说\"compute bipartite matching via the Hungarian algorithm with span overlap\"，但未明确说明是最大化 IoU（benefit）还是最小化 1-IoU（cost），也未说明 \"without minimum similarity threshold\" 的具体含义——是否允许 IoU=0 的匹配对？如果允许，一个完全不相关的 entity 被 matched 后贡献 sim=0 到分子但占据分母的一个位置，可能影响 SJ 的行为。\n- 建议：补充一到两句明确 Hungarian algorithm 的优化目标（max-weight matching on IoU scores）和 zero-IoU pairs 的处理方式。\n\n**W5** [warning] 两个模型均为 8B 参数，\"cross-model\" 结论的外推受限\n\n- 具体位置：§Limitations 第4-6行\n- 问题：Qwen3-8B 和 LLaMA-3.1-8B 代表的是同一参数量级的两个架构。论文多处使用\"cross-model consistency\"（如§4.2 第77行），但这更准确地说是\"cross-architecture consistency at fixed scale\"。论文在 Limitations 中提到 70B+ 模型未测试，但正文的措辞给人的印象是 cross-model 结论比实际更强。\n- 建议：在正文中将\"cross-model\"替换为\"cross-architecture\"或加限定词（如\"cross-model (at 8B scale)\"），更准确地反映实际覆盖范围。\n\n**W6** [warning] Consensus-proximity 是唯一的 instance-to-sample 转换策略，未比较替代方案\n\n- 具体位置：§3.3 第67行\n- 问题：将 instance-level 信号转为 per-sample 信号的策略（选择最接近 consensus 的样本）与 Minimum Bayes Risk (MBR) decoding 的 utility-maximization formulation 等价（Vashurin et al. 2025 已引用但未建立此联系）。论文未讨论其他可能的转换策略（如 diversity-weighted selection、centroid-based selection with different distance metrics）。如果 consensus-proximity 是次优策略，correlation-selection gap 可能被高估。\n- 建议：（a）明确与 MBR decoding 的联系；（b）至少在 Discussion 中说明为何 consensus-proximity 是合理的默认选择，以及替代策略是否可能缩小 gap。\n\n---\n\n## Minor Issues（不影响接收）\n\n**M1.** WNUT-17 \"54% zero F1\" 数据不一致。§4.1 第11行称\"54% zero F1\"，但 Table 7（Appendix）显示 n=689（filtering gold-empty 后）中 conditional n=334（non-zero），即 355/689 ≈ 51.5% zero F1，与 54% 有 ~2.5pp 差距。请核实并统一。\n\n**M2.** Table 1 N=16 区域大面积空白。仅报告 LLaMA CoNLL 的 N=16 ρ 值，其余配置在 Appendix Table 5 中。建议至少在 Table 1 caption 中补充交叉引用，或考虑合并呈现。\n\n**M3.** EM 从 selection 实验中排除的理由（Table 2 caption：\"the probability of two identical structured outputs is negligible\"）缺乏经验支持。建议报告 N=8 实验中 exact match pairs 的实际频率以验证此声明。\n\n**M4.** LOO-SJ 验证（Appendix C 第126行）仅报告了 Δρ=−0.014 和 per-instance max Δρ=3.1×10⁻⁴。注意这两个量的量纲不同：前者是整体 Spearman ρ 的变化，后者似乎是 per-instance confidence score 的变化。请澄清 per-instance Δρ 的具体含义。\n\n**M5.** Figure 1 caption 中 \"p=0.39 for NER logprob\" 直接出现在 figure 描述中，但该 p 值来自 Table 2 的 selection 分析而非 figure 本身可视化的内容（figure 显示的是 correlation vs. selection bars）。Caption 中引入 figure 未直接呈现的统计结果容易造成混淆。\n\n**M6.** §4.2 第64行的脚注比较 semantic entropy AUROC（0.75-0.85 on QA）与本文 AUROC（0.749 on IE），并承认\"direct comparison is complicated\"。既然承认不可直接比较，建议删除或大幅缩短此脚注，避免给读者留下可比较的印象。\n\n**M7.** 引用格式：feng2025optimal 和 snell2024scaling 的 bib key 使用姓氏但 OpenAlex 返回的 first_author 为名字（Austin/Charlie），这是 bib key 命名惯例问题，不影响引用正确性。hobelsberger2025systematic 和 lightman2024verify 在 OpenAlex 未找到匹配，但两篇均为已知发表论文（后者为 ICLR 2024 paper），应为 API 限制。\n\n---\n\n## Questions to Authors\n\n**Q1.** 是否考虑过在 constrained decoding 之外运行 unconstrained generation 作为对照？即使 parse 成功率低，比较两种 regime 下的 per-sample diversity（如 pairwise SJ 分布）也能 calibrate correlation-selection gap 的 generalizability。\n\n**Q2.** Logprob 在 WNUT conditional set 上达到了所有信号中最高的 ρ=0.350（Table 7），这与主文中\"logprob 是最弱信号\"的叙述相矛盾。如何 reconcile 这一发现？是否暗示 logprob 在高难度 domain 的 capability boundary 区间反而有独特优势？\n\n**Q3.** LoRA rank=32 的选择是否影响了 sample diversity？更低的 rank 可能导致 fine-tuned 模型更接近 base model 的分布，potentially increasing diversity。是否做过 LoRA rank 的敏感性分析？\n\n**Q4.** Table 6（cross-configuration selection）中 LLaMA/SciERC N=16 configuration 下 SJ 和 FK 并列第一（0.649），但都低于 greedy（0.645→0.649 仅 +0.004pp）。N=16 是否提供了 selection 结果的 multi-seed bootstrap p-value？\n\n---\n\n## Missing References\n\n- **MBR decoding 相关文献**：Eikema & Aziz (2022, \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\") 和 Freitag et al. (2022, \"High Quality Rather Than High Model Probability\") 建立了 MBR decoding 的理论框架，本文的 consensus-proximity selection 与之直接相关但未讨论。\n- **Structured prediction 的 uncertainty 估计**：Malinin & Gales (2021, \"Uncertainty Estimation in Autoregressive Structured Prediction\") 讨论了序列级输出的 uncertainty estimation，与本文的 structured output uncertainty 有方法论联系。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法定义基本清晰，统计报告充分；但 constrained decoding 混淆变量未控制（N1）、failure-to-reject 逻辑不完整（N2）、核心结果 single-seed（N3）是三个显著的 soundness gap |\n| Excitement | 3/5 | Quality estimation vs. sample selection 的分离框架和 task-difficulty-dependent ordering 有实用价值；但 correlation-selection gap 中 instance-level 信号的部分是 tautological（W2），核心 insight 的 novelty 中等 |\n| Reproducibility | 3.5/5 | LoRA 超参、bootstrap B、seed、评估指标均有报告；但缺少代码/数据可用性声明，logprob T=0.7 数据缺失，EM selection 排除缺乏经验验证 |\n| Overall | 3/5 | Findings 水平。实验设计 mostly sound、写作质量高，但 N1-N3 三个 critical issues 共同削弱了核心贡献的可信度。若 N1（constrained decoding 对照）和 N3（multi-seed）能在修订中解决，可提升至 3.5 |\n| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、IE evaluation 领域，仔细审查了方法定义和统计分析 |\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings)\n**一句话总结**: 框架设计清晰、统计报告充分的经验性研究，但核心发现（correlation-selection gap）受 constrained decoding 混淆变量、single-seed 设计、和 failure-to-reject 论证逻辑三重限制，需要补充实验和统计修订以支撑论文的主要 claim。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-15T04:05:19.089455+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4014
}
```

</details>

---


### Assistant

_source line 270 · 2026-05-15T04:05:28.828104+00:00_

审稿意见已提交给 Review Director。

审查要点总结：

- **3 个 Must-Fix**：（1）constrained decoding 作为 correlation-selection gap 的未控制混淆变量，需对照实验或 diversity 量化；（2）"no signal surpasses greedy" 基于 failure-to-reject 逻辑，需补充等价性检验或修改措辞；（3）N=8 核心结果仅 single seed，需补充 multi-seed 验证
- **6 个 Should-Fix**：多重比较校正缺失、gap 概念部分 tautological、FK 独立性假设未验证、SJ Hungarian cost function 未明确、cross-model 措辞过度外推、consensus-proximity 未与 MBR decoding 建立联系且未比较替代策略
- **7 个 Minor**：WNUT 54% 数据不一致、Table 1 N=16 空白、EM exclusion 缺经验支持等
- **Overall 3/5 (Findings)**，Soundness 3.5，Excitement 3，Confidence 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

16 recorded events


### User

_source line 271 · 2026-05-15T04:06:12.092440+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 2 的完整审稿原文：

### Summary
本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。

### Strengths
- S1: Quality estimation 与 sample selection 的问题分解有真正洞察力
- S2: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test
- S3: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动
- S4: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限
- S5: 论文结构和叙事流畅
- S6: Robustness 分析覆盖 temperature、N-scaling、cross-model

### Must-Fix (Critical)
**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响
- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱
- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion
- 建议增加 RE benchmark 或显著降低 RE claim 强度

**N2** [critical] Logprob 失败缺乏实证解释
- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题
- Discussion 的 "constrained decoding 压缩 diversity" 解释是猜测性的
- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视
- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding

**N3** [critical] 缺少 Ethics Statement
- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题

### Should-Fix (Warning)
**W1** "First multi-family comparison" claim 边界需更精确限定
**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）
**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调
**W4** 术语不一致："confidence signal" vs "consistency signal"、"VC" vs "Voting Conf."、LLaMA Factory 未引用
**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)

### Minor Issues
- Abstract 中 "oracle headroom" 此时无定义
- 对 Nedellec (2026) 措辞偏 adversarial
- FK independent raters 假设的 justification 不足
- Table 2 EM omission 需 unique output fraction 数据支持

### Missing References
1. Kim et al. (2024) "VerifiNER" — ACL 2024
2. Aggarwal et al. (2025) "Reasoning Aware Self-Consistency" — NAACL 2025
3. He et al. (2024) "Uncertainty Estimation on Sequential Labeling" — NAACL Findings 2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-15T04:06:19.818648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-15T04:06:20.270948+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-15T04:06:20.271401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-15T04:06:20.623516+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-15T04:06:20.623994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-15T04:06:20.724966+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-15T04:06:38.360967+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ethics|ethical|Ethics Statement",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ethics|ethical|Ethics Statement",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-15T04:06:38.663329+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-15T04:06:39.067232+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "nedellec|Nedellec|Nédellec",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-C": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "nedellec|Nedellec|Nédellec",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-C": "1"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-15T04:06:39.117965+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-355-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl:356:\bibitem[{Yao et~al.(2026)Yao, Nédellec, Xia, and
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl:357:  Bossy}]{nedellec2026consistency}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl:358:Xinzhi Yao, Claire Nédellec, Jingbo Xia, and Robert Bossy. 2026.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-359-\newblock \href {https://doi.org/10.1186/s44342-025-00063-2}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-12-\paragraph{Consistency for structured IE.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:13:\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-14-However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex-15-Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be groupe
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-15T04:06:44.546202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-15T04:06:44.597348+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-15T04:08:32.143555+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应\n\n---\n\n### Must-Fix Issues\n\n**[AGREE] R2-N1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**\n\n同意这是一个实质性问题。我在自己的审稿中也将 RE 单数据集问题列为关注点（虽然未列为 Must-Fix，因为论文在 Introduction §1 第46行、Discussion §5 第10行、Conclusion §6 第12行、Limitations 四处均做了明确 hedging）。\n\nR2 的核心论点是正确的：44% zero F1 严重压缩了信号的可区分范围，使得 RE 的 gap 证据（−0.9pp, p=0.80）缺乏统计说服力。补充一个观察：Appendix C（Table 7）的 WNUT conditional 分析表明，当 zero-F1 比例高时，full-set 指标会被 binary success/failure boundary 严重扭曲——SciERC RE 的 44% zero-F1 也存在类似问题，但论文未对 RE 做类似的 conditional 分析（SciERC conditional results in §4.2 and Figure 2 涵盖了 NER 和 RE，但 RE conditional ρ 仅在 Appendix C 简要提及而未深入讨论）。\n\n不过，我认为增加新 RE benchmark 作为修订要求可能过于苛刻——这在 ARR revision cycle 内不太现实。更务实的修改方向是：（a）大幅降低 RE claim 强度（从\"IE\"泛化改为明确说\"NER + preliminary RE evidence\"）；（b）对 SciERC RE 补充 conditional filtering 分析（非零 F1 子集），量化 floor effect 对 gap 结论的影响。\n\n**[AGREE] R2-N2: Logprob 失败缺乏实证解释**\n\n完全同意，且这与我的 N1（constrained decoding 混淆变量）高度重叠。R2 精确地指出了问题的核心：4 个 instance-level signal 无法 per-sample select 是定义层面的必然（我在 W2 中也指出了这一 tautological 成分），所以论文真正需要解释的是 logprob 为什么也失败。\n\nR2 建议的具体分析非常到位——per-sample logprob variance 和 unique output fraction 这两个量可以直接 characterize constrained decoding 对 diversity 的压缩程度。如果 unique output fraction 很低（比如 N=8 中平均只有 2-3 个 distinct outputs），那么 correlation-selection gap 在很大程度上就是一个 diversity limitation 而非信号本身的局限。\n\n补充一个来自论文内部的支持证据：§5 Discussion 第22行报告\"75% of instance-level logprob comparisons are effectively ties (win%=46.6%)\"——这暗示 per-sample logprob 的 variance 确实很小，但论文没有进一步量化。报告每个 instance 的 logprob standard deviation 分布将直接回答这个问题。\n\n此外，WNUT-17 conditional set 上 logprob 达到了所有信号中最高的 ρ=0.350（Table 7），而主文中 logprob 被一致描述为\"最弱信号\"。这一反转值得在 Discussion 中 reconcile——它可能暗示 logprob 在高 diversity 场景（WNUT 的 noisy domain 使得 constrained decoding 的约束力相对较弱）反而有优势，间接支持了 constrained decoding 压缩 diversity 的假说。\n\n**[REBUT] R2-N3: 缺少 Ethics Statement**\n\n不同意将此列为 Must-Fix/critical。\n\n根据 ACL ARR CFP（2025 年 2 月更新版），Ethics Statement 是\"encouraged\"而非\"required\"。原文：\"We encourage, but do not require, papers to include an Ethics Statement.\" Limitations section 是 required 的，论文已包含。本文研究的是 confidence signal 评估方法论，使用的是公开 benchmark（SciERC、CoNLL-2003、WNUT-17），不涉及人类数据收集、隐私、dual-use 风险等典型 ethical concern。\n\n当然，添加一个简短的 Ethics Statement（哪怕只说明使用的是公开数据、不涉及人类标注）是 good practice，但将其缺失标为\"critical\"与 ARR 政策不符。建议降级为 Minor。\n\n---\n\n### Should-Fix Issues\n\n**[AGREE] R2-W1: \"First multi-family comparison\" claim 边界需更精确限定**\n\n同意。§1 第35行的\"First multi-family comparison of confidence signals for generative IE\"措辞过宽。Nedellec et al. (2026) 已比较了 surface-level consistency 与 accuracy 的相关性（虽然不是 multi-family）；CoCoA (Vashurin et al., 2025) 融合了 model confidence 与 inter-sample consistency（虽然是 QA/summarization 而非 IE）。更精确的限定应是\"first comparison spanning structural, surface, and model-internal signal families for both quality estimation and sample selection in generative structured IE\"。\n\n**[REBUT] R2-W2: SJ 增量贡献 borderline**\n\n部分不同意。R2 聚焦于 SJ 在 ρ 上相对于 Voting 和 EM 的微小优势（Δρ CI 含零），但 SJ 的贡献不应仅以 ρ 增量衡量：\n\n1. **Temperature robustness**: Table 5（Appendix B）显示 SJ NER ρ 在 T=0.7→1.0 之间仅变化 0.028（bootstrap CI 含零），而 FK 变化 0.054/0.091。SJ 是唯一在所有 temperature/N-scaling 条件下表现一致稳定的信号（§4.4 第80行）。\n2. **Semantic matching 能力**: SJ 设计目的是处理 \"partial overlap\" 情况——同一实体的不同表面形式（如 span boundary 差异）。EM 和 FK 都依赖 exact string matching，在这些情况下系统性地低估一致性。论文 §1 第16行和 Related Work §2 第14-15行明确说明这解决了 Nedellec et al. 的 limitation (i)。\n3. **N-scaling**: SJ 在 N=8→16 时一致性地改善（全部 setting 为正方向），FK 则表现不一致（§Appendix B 第78行：SciERC 上 degradation，CoNLL 上 improvement）。\n\n因此，SJ 的贡献是作为一个 robust 的 structural similarity measure，而非在单个 snapshot（N=8, T=1.0, SciERC）上显著超越其他信号。论文的措辞应更清楚地传达这一点。\n\n**[AGREE with nuance] R2-W3: ρ–AUROC dissociation 是 expected statistical behavior**\n\n部分同意 R2 的诊断：binary classifier 的 AUROC 高于 continuous ranker 的 rank correlation 在统计上确实是 expected 的——EM 的 binary nature 使其天然适合二元分类而弱于连续排序。\n\n但我认为论文的价值不在于发现 dissociation 本身，而在于将其映射到 IE 的实际使用场景：EM 适合 routing/triage（binary discrimination），Voting/SJ 适合 quality ranking。§5 Discussion 第16-17行的实践建议——\"these signals are well-suited for routing and triage...but not for fine-grained ranking within a difficulty tier\"——是从 dissociation 中提取的 actionable insight，不是对统计现象本身的过度宣传。\n\n建议论文在 §4.2 的表述中承认 dissociation 的统计预期性，然后聚焦于实践含义，而非将其呈现为 surprising finding。\n\n**[AGREE] R2-W4: 术语不一致**\n\n同意。具体问题：\n- \"confidence signal\" vs. \"consistency signal\"：前者出现在 Abstract、§1、§3；后者出现在 §4、§5。应统一为 \"confidence signal\"（论文的正式术语），仅在特指 consistency-based 子集时用 \"consistency signal\"。\n- Table 6 用 \"VC\" 和 \"LP\"，正文和其他表格用 \"Voting Conf.\" 和 \"Log-prob\"：应统一缩写。\n- LLaMA Factory 未引用：§4.1 第14行提到但确实未提供引用。\n\n**[AGREE with caveat] R2-W5: Related Work 遗漏**\n\nVerifiNER (Kim et al., ACL 2024) 确实高度相关——它使用 LLM 作为 verifier 来检验 NER 输出质量，与本文的 quality estimation 目标直接相关，且提供了 supervised verification 的对照视角（本文是 unsupervised signals）。应在 Related Work §2 第24行附近讨论。\n\n对于 RASC (Aggarwal et al., NAACL 2025)，如果它聚焦于 reasoning task 的 self-consistency 改进（如 Related Work §2 第7行已引用 Kim et al. 2026 的 REASC），需要确认是否为同一方法或不同工作。如果是不同工作且与 IE 相关，应引用；如果主要聚焦 reasoning/QA，可在 Related Work 中简要提及但不必深入讨论。\n\nHe et al. (2024, NAACL Findings) 关于 sequential labeling 的 uncertainty estimation 也相关，应在 §2 第24行（NER uncertainty 段落）补充引用。\n\n---\n\n### Minor Issues\n\n**[AGREE] Abstract 中 \"oracle headroom\" 无定义**：同意。首次出现时应加括号解释，如 \"oracle headroom (the gap between the best achievable selection and greedy decoding)\"。\n\n**[AGREE with nuance] 对 Nedellec (2026) 措辞偏 adversarial**：Introduction §1 第16行的三点列举 (i)-(iii) 在技术上是准确的，但在学术语气上确实偏向\"building a case against\"。建议先肯定 Nedellec et al. 的贡献（如 \"corroborating the existence of consistency-accuracy correlations\"，这在 Related Work §2 第13行已做到），然后在 Introduction 中用更 neutral 的方式指出 gap（如 \"leaving open the questions of...\"）。Related Work 的表述相比 Introduction 已经 balanced 得多。\n\n**[AGREE] FK independent raters 假设 justification 不足**：与我的 W3 一致。§3.2 第37行的 one-line justification 不够。\n\n**[AGREE] Table 2 EM omission 需 unique output fraction 数据**：与我的 M3 一致。\"probability of two identical structured outputs is negligible\" 缺乏经验验证。\n\n---\n\n### Missing References 评估\n\n1. **VerifiNER (Kim et al., ACL 2024)**：高度相关，应引用。提供了 supervised NER verification 的参照点。\n2. **RASC (Aggarwal et al., NAACL 2025)**：需确认具体内容。如果是 reasoning-focused，相关性中等（已有类似引用）。\n3. **He et al. (2024, NAACL Findings)**：序列标注 uncertainty estimation，与 §2 第24行讨论的 NER uncertainty 直接相关，应引用。\n\n---\n\n### 与我（R1）审稿的交叉对比\n\n两份审稿在以下方面**高度一致**：\n- Constrained decoding 对 logprob/diversity 的影响是核心 validity threat（R1-N1 ≈ R2-N2）\n- FK 独立性假设 justification 不足（R1-W3 ≈ R2-Minor）\n- EM omission 需经验数据支持（R1-M3 ≈ R2-Minor）\n- 术语一致性需修复\n\n**分歧点**：\n- R2 将 RE 单数据集列为 Must-Fix #1，我将其列为 Should-Fix（因论文已多处 hedge）。但 R2 的 floor effect 分析比我更深入，说服力强。**我倾向于上调此问题的严重性到 borderline Must-Fix**。\n- R2 将 Ethics Statement 缺失列为 Must-Fix，我认为 ARR 政策仅 \"encourage\" 而非 \"require\"，应降为 Minor。\n- R2-W3（ρ-AUROC dissociation 是 expected behavior）是一个我未单独提出的有效观点——论文确实可以更明确地承认其统计预期性。\n- R2 未提到我的 N2（failure-to-reject 统计逻辑）和 N3（single-seed），这两个是我认为的核心 soundness 问题。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应\n\n---\n\n### Must-Fix Issues\n\n**[AGREE] R2-N1: RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**\n\n同意这是一个实质性问题。我在自己的审稿中也将 RE 单数据集问题列为关注点（虽然未列为 Must-Fix，因为论文在 Introduction §1 第46行、Discussion §5 第10行、Conclusion §6 第12行、Limitations 四处均做了明确 hedging）。\n\nR2 的核心论点是正确的：44% zero F1 严重压缩了信号的可区分范围，使得 RE 的 gap 证据（−0.9pp, p=0.80）缺乏统计说服力。补充一个观察：Appendix C（Table 7）的 WNUT conditional 分析表明，当 zero-F1 比例高时，full-set 指标会被 binary success/failure boundary 严重扭曲——SciERC RE 的 44% zero-F1 也存在类似问题，但论文未对 RE 做类似的 conditional 分析（SciERC conditional results in §4.2 and Figure 2 涵盖了 NER 和 RE，但 RE conditional ρ 仅在 Appendix C 简要提及而未深入讨论）。\n\n不过，我认为增加新 RE benchmark 作为修订要求可能过于苛刻——这在 ARR revision cycle 内不太现实。更务实的修改方向是：（a）大幅降低 RE claim 强度（从\"IE\"泛化改为明确说\"NER + preliminary RE evidence\"）；（b）对 SciERC RE 补充 conditional filtering 分析（非零 F1 子集），量化 floor effect 对 gap 结论的影响。\n\n**[AGREE] R2-N2: Logprob 失败缺乏实证解释**\n\n完全同意，且这与我的 N1（constrained decoding 混淆变量）高度重叠。R2 精确地指出了问题的核心：4 个 instance-level signal 无法 per-sample select 是定义层面的必然（我在 W2 中也指出了这一 tautological 成分），所以论文真正需要解释的是 logprob 为什么也失败。\n\nR2 建议的具体分析非常到位——per-sample logprob variance 和 unique output fraction 这两个量可以直接 characterize constrained decoding 对 diversity 的压缩程度。如果 unique output fraction 很低（比如 N=8 中平均只有 2-3 个 distinct outputs），那么 correlation-selection gap 在很大程度上就是一个 diversity limitation 而非信号本身的局限。\n\n补充一个来自论文内部的支持证据：§5 Discussion 第22行报告\"75% of instance-level logprob comparisons are effectively ties (win%=46.6%)\"——这暗示 per-sample logprob 的 variance 确实很小，但论文没有进一步量化。报告每个 instance 的 logprob standard deviation 分布将直接回答这个问题。\n\n此外，WNUT-17 conditional set 上 logprob 达到了所有信号中最高的 ρ=0.350（Table 7），而主文中 logprob 被一致描述为\"最弱信号\"。这一反转值得在 Discussion 中 reconcile——它可能暗示 logprob 在高 diversity 场景（WNUT 的 noisy domain 使得 constrained decoding 的约束力相对较弱）反而有优势，间接支持了 constrained decoding 压缩 diversity 的假说。\n\n**[REBUT] R2-N3: 缺少 Ethics Statement**\n\n不同意将此列为 Must-Fix/critical。\n\n根据 ACL ARR CFP（2025 年 2 月更新版），Ethics Statement 是\"encouraged\"而非\"required\"。原文：\"We encourage, but do not require, papers to include an Ethics Statement.\" Limitations section 是 required 的，论文已包含。本文研究的是 confidence signal 评估方法论，使用的是公开 benchmark（SciERC、CoNLL-2003、WNUT-17），不涉及人类数据收集、隐私、dual-use 风险等典型 ethical concern。\n\n当然，添加一个简短的 Ethics Statement（哪怕只说明使用的是公开数据、不涉及人类标注）是 good practice，但将其缺失标为\"critical\"与 ARR 政策不符。建议降级为 Minor。\n\n---\n\n### Should-Fix Issues\n\n**[AGREE] R2-W1: \"First multi-family comparison\" claim 边界需更精确限定**\n\n同意。§1 第35行的\"First multi-family comparison of confidence signals for generative IE\"措辞过宽。Nedellec et al. (2026) 已比较了 surface-level consistency 与 accuracy 的相关性（虽然不是 multi-family）；CoCoA (Vashurin et al., 2025) 融合了 model confidence 与 inter-sample consistency（虽然是 QA/summarization 而非 IE）。更精确的限定应是\"first comparison spanning structural, surface, and model-internal signal families for both quality estimation and sample selection in generative structured IE\"。\n\n**[REBUT] R2-W2: SJ 增量贡献 borderline**\n\n部分不同意。R2 聚焦于 SJ 在 ρ 上相对于 Voting 和 EM 的微小优势（Δρ CI 含零），但 SJ 的贡献不应仅以 ρ 增量衡量：\n\n1. **Temperature robustness**: Table 5（Appendix B）显示 SJ NER ρ 在 T=0.7→1.0 之间仅变化 0.028（bootstrap CI 含零），而 FK 变化 0.054/0.091。SJ 是唯一在所有 temperature/N-scaling 条件下表现一致稳定的信号（§4.4 第80行）。\n2. **Semantic matching 能力**: SJ 设计目的是处理 \"partial overlap\" 情况——同一实体的不同表面形式（如 span boundary 差异）。EM 和 FK 都依赖 exact string matching，在这些情况下系统性地低估一致性。论文 §1 第16行和 Related Work §2 第14-15行明确说明这解决了 Nedellec et al. 的 limitation (i)。\n3. **N-scaling**: SJ 在 N=8→16 时一致性地改善（全部 setting 为正方向），FK 则表现不一致（§Appendix B 第78行：SciERC 上 degradation，CoNLL 上 improvement）。\n\n因此，SJ 的贡献是作为一个 robust 的 structural similarity measure，而非在单个 snapshot（N=8, T=1.0, SciERC）上显著超越其他信号。论文的措辞应更清楚地传达这一点。\n\n**[AGREE with nuance] R2-W3: ρ–AUROC dissociation 是 expected statistical behavior**\n\n部分同意 R2 的诊断：binary classifier 的 AUROC 高于 continuous ranker 的 rank correlation 在统计上确实是 expected 的——EM 的 binary nature 使其天然适合二元分类而弱于连续排序。\n\n但我认为论文的价值不在于发现 dissociation 本身，而在于将其映射到 IE 的实际使用场景：EM 适合 routing/triage（binary discrimination），Voting/SJ 适合 quality ranking。§5 Discussion 第16-17行的实践建议——\"these signals are well-suited for routing and triage...but not for fine-grained ranking within a difficulty tier\"——是从 dissociation 中提取的 actionable insight，不是对统计现象本身的过度宣传。\n\n建议论文在 §4.2 的表述中承认 dissociation 的统计预期性，然后聚焦于实践含义，而非将其呈现为 surprising finding。\n\n**[AGREE] R2-W4: 术语不一致**\n\n同意。具体问题：\n- \"confidence signal\" vs. \"consistency signal\"：前者出现在 Abstract、§1、§3；后者出现在 §4、§5。应统一为 \"confidence signal\"（论文的正式术语），仅在特指 consistency-based 子集时用 \"consistency signal\"。\n- Table 6 用 \"VC\" 和 \"LP\"，正文和其他表格用 \"Voting Conf.\" 和 \"Log-prob\"：应统一缩写。\n- LLaMA Factory 未引用：§4.1 第14行提到但确实未提供引用。\n\n**[AGREE with caveat] R2-W5: Related Work 遗漏**\n\nVerifiNER (Kim et al., ACL 2024) 确实高度相关——它使用 LLM 作为 verifier 来检验 NER 输出质量，与本文的 quality estimation 目标直接相关，且提供了 supervised verification 的对照视角（本文是 unsupervised signals）。应在 Related Work §2 第24行附近讨论。\n\n对于 RASC (Aggarwal et al., NAACL 2025)，如果它聚焦于 reasoning task 的 self-consistency 改进（如 Related Work §2 第7行已引用 Kim et al. 2026 的 REASC），需要确认是否为同一方法或不同工作。如果是不同工作且与 IE 相关，应引用；如果主要聚焦 reasoning/QA，可在 Related Work 中简要提及但不必深入讨论。\n\nHe et al. (2024, NAACL Findings) 关于 sequential labeling 的 uncertainty estimation 也相关，应在 §2 第24行（NER uncertainty 段落）补充引用。\n\n---\n\n### Minor Issues\n\n**[AGREE] Abstract 中 \"oracle headroom\" 无定义**：同意。首次出现时应加括号解释，如 \"oracle headroom (the gap between the best achievable selection and greedy decoding)\"。\n\n**[AGREE with nuance] 对 Nedellec (2026) 措辞偏 adversarial**：Introduction §1 第16行的三点列举 (i)-(iii) 在技术上是准确的，但在学术语气上确实偏向\"building a case against\"。建议先肯定 Nedellec et al. 的贡献（如 \"corroborating the existence of consistency-accuracy correlations\"，这在 Related Work §2 第13行已做到），然后在 Introduction 中用更 neutral 的方式指出 gap（如 \"leaving open the questions of...\"）。Related Work 的表述相比 Introduction 已经 balanced 得多。\n\n**[AGREE] FK independent raters 假设 justification 不足**：与我的 W3 一致。§3.2 第37行的 one-line justification 不够。\n\n**[AGREE] Table 2 EM omission 需 unique output fraction 数据**：与我的 M3 一致。\"probability of two identical structured outputs is negligible\" 缺乏经验验证。\n\n---\n\n### Missing References 评估\n\n1. **VerifiNER (Kim et al., ACL 2024)**：高度相关，应引用。提供了 supervised NER verification 的参照点。\n2. **RASC (Aggarwal et al., NAACL 2025)**：需确认具体内容。如果是 reasoning-focused，相关性中等（已有类似引用）。\n3. **He et al. (2024, NAACL Findings)**：序列标注 uncertainty estimation，与 §2 第24行讨论的 NER uncertainty 直接相关，应引用。\n\n---\n\n### 与我（R1）审稿的交叉对比\n\n两份审稿在以下方面**高度一致**：\n- Constrained decoding 对 logprob/diversity 的影响是核心 validity threat（R1-N1 ≈ R2-N2）\n- FK 独立性假设 justification 不足（R1-W3 ≈ R2-Minor）\n- EM omission 需经验数据支持（R1-M3 ≈ R2-Minor）\n- 术语一致性需修复\n\n**分歧点**：\n- R2 将 RE 单数据集列为 Must-Fix #1，我将其列为 Should-Fix（因论文已多处 hedge）。但 R2 的 floor effect 分析比我更深入，说服力强。**我倾向于上调此问题的严重性到 borderline Must-Fix**。\n- R2 将 Ethics Statement 缺失列为 Must-Fix，我认为 ARR 政策仅 \"encourage\" 而非 \"require\"，应降为 Minor。\n- R2-W3（ρ-AUROC dissociation 是 expected behavior）是一个我未单独提出的有效观点——论文确实可以更明确地承认其统计预期性。\n- R2 未提到我的 N2（failure-to-reject 统计逻辑）和 N3（single-seed），这两个是我认为的核心 soundness 问题。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-15T04:08:36.063780+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3920
}
```

</details>

---


### Assistant

_source line 286 · 2026-05-15T04:08:42.889767+00:00_

交叉回应已提交给 Review Director。

核心判断总结：

- **R2-N1 (RE 单数据集)**：AGREE，floor effect 分析有说服力，我上调此问题严重性
- **R2-N2 (Logprob 解释缺失)**：AGREE，与我的 N1 (constrained decoding confound) 高度重叠
- **R2-N3 (Ethics Statement)**：REBUT，ARR 仅"encourage"非"require"，应降为 Minor
- **R2-W1–W5**：大部分 AGREE，W2 (SJ 贡献) 部分 REBUT——SJ 价值在于 robustness 而非单点 ρ 增量
- 两份审稿在 constrained decoding、FK 独立性、EM omission 上高度一致；R2 未覆盖我的 N2 (failure-to-reject 逻辑) 和 N3 (single-seed) 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

46 recorded events


### User

_source line 287 · 2026-05-15T06:42:22.156833+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
- **路径**: projects/struct_self_consist_ie/docs/paper/main.tex（含 sections/ 下 9 个 .tex 文件 + references.bib + figures/）
- **目标 Venue**: EMNLP 2026 Findings track
- **截止日期**: 2026-05-25（ARR May cycle）
- **格式**: ACL template, 长文 8 页正文, double-blind, 附录须 double-column
- **匿名**: Double-blind（当前标注 Anonymous ✓）

### 论文概要
本文系统比较了三族五种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式信息抽取（NER 三数据集 + RE SciERC）的 test-time scaling 场景下的表现。核心发现：这些信号是有效的 quality estimators（ρ=0.38, AUROC=0.75），但作为 sample selectors 失败（无信号显著超越 greedy，p>0.39），作者称之为 "correlation-selection gap"。

### 审查要求
请从以下维度深入评审，给出结构化报告（Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments）：

1. **方法设计**
   - 五种信号的数学定义是否严谨、完整、可复现
   - Soft Jaccard 的 Hungarian matching 细节是否充分（优化方向、cost function、零 IoU 处理、threshold）
   - Fleiss' κ 应用于非独立 temperature-sampled outputs 的 justification 是否充分
   - Per-sample vs instance-level 信号分类的理论清晰度

2. **实验设计**
   - 数据集选择覆盖度（3 NER + 1 RE）是否足以支撑 claims
   - 模型选择（2 × 8B）的代表性，cross-architecture vs cross-scale 区分
   - N=8/16 采样规模、temperature 选择的 justification
   - 训练设置（LoRA fine-tuning）的详细程度与可复现性
   - Constrained decoding 对 output diversity 的影响是否被充分讨论

3. **统计分析**
   - Bootstrap resampling 的规范性（B=10,000, seed, CI 类型）
   - Selection gap 的统计论证：failure-to-reject vs evidence of absence
   - TOST 等价性检验的 δ 选择是否合理
   - 信号间比较的多重比较校正
   - Single-seed (N=8) 结果的稳定性论证
   - Effect size 报告（Cohen's d, win%）

4. **核心 claim 的支撑力度**
   - "Correlation-selection gap" 是否为非平凡发现（4/5 信号 instance-level by design）
   - Gap 是否可能是 constrained decoding 导致的 artifact
   - RE 结论仅基于 SciERC 单数据集的限制程度

请独立审查，给出你对本文的 overall assessment（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-15T06:42:29.934325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-15T06:42:29.985110+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-15T06:42:32.648141+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-15T06:42:32.698808+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-15T06:42:35.008719+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-15T06:42:35.059489+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-15T06:42:41.340617+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-15T06:42:41.392312+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-15T06:42:47.580342+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-15T06:42:47.731323+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-15T06:42:48.585209+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-15T06:42:49.037492+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-15T06:42:49.037983+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-15T06:42:56.921261+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be ju
…[truncated 1365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7883
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-15T06:43:07.868094+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 2026 soundness excitement scoring scale detailed criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 2026 soundness excitement scoring scale detailed criteria"
  }
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-15T06:43:08.320238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-15T06:43:09.274530+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-15T06:43:09.325152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-15T06:43:09.777289+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---we find no statistically significant evidence that any signal surpasses greedy decoding on SciERC---where output diversity is substantial---across both model architectures ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom; on easier tasks, near-identical outputs preclude meaningful selection analysis.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 307 · 2026-05-15T06:43:09.777679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-15T06:43:09.978880+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-15T06:43:09.979363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-15T06:43:10.029969+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-15T06:43:16.056064+00:00_

Web search results for query: "ACL Rolling Review review form 2025 2026 soundness excitement scoring scale detailed criteria"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

I found detailed information about the ACL Rolling Review (ARR) review form for 2025-2026. Here's what the search revealed:

## Scoring System Overvi
…[truncated 1751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8187
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-15T06:43:21.830479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-15T06:43:22.333268+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:qu
…[truncated 11663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-15T06:43:22.383856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-15T06:43:22.434517+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists.}
9	Four of five signals are instance-level by construction and cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) adds no reliable value (Table~\ref{tab:selection}).
10	Logprob, the sole per-sample signal, primarily reflects grammar compliance under constrained decoding---75\% of comparisons are effectively ties (\S\ref{sec:selection_gap}).
11	The common root is that quality estimation ranks \textit{instances}, while sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that neither instance-level aggregation nor token-level confidence provides.
12	On SciERC, diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); calibration analysis shows RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) may compound this failure.
13	These signals are thus well-suited for quality-aware routing but not for discriminating among candidates.
14	
15	\paragraph{Connection to MBR decoding.}
16	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling}: SJ uses $U{=}\text{SJ}(y_i, y_j)$, EM uses $U{=}\mathbb{1}[y_i{=}y_j]$ (standard majority votin
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-15T06:43:22.836447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-15T06:43:23.188286+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-15T06:43:23.188654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-15T06:43:24.243345+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75), but we find no significant evidence that any signal surpasses greedy on best-of-$N$ selection on SciERC ($p{>}0.39$, 13--18~pp oracle headroom), a disconnect we term the \textit{correlation-selection gap}.
6	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
7	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
8	
9	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
10	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-15T06:43:24.294036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-15T06:43:24.294586+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-15T06:43:24.345197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-15T06:43:24.346118+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 21352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-15T06:43:30.521318+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 325 · 2026-05-15T06:43:30.622112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-15T06:43:36.596016+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions (soundness, excitement, overall recommendation, confidence, etc.), their exact scales (1-5, etc.), and the description for each level. Also extract any specific criteria reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions (soundness, excitement, overall recommendation, confidence, etc.), their exact scales (1-5, etc.), and the description for each level. Also extract any specific criteria reviewers should evaluate."
  }
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-15T06:43:38.001798+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-15T06:43:42.770929+00:00_

# ACL ARR Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale with half-points)
Examines whether claims have adequate support and methodological validity.
- **5:** "Excellent: one of the most thorough studies."
- **4:** "Strong: sufficient support for all claims."
- **3:** "Acceptable: supports main claims with minor gaps."
- **2:** "Poor: main claims lack sufficient support."
- **1:** "Major Issues: insufficiently thorough for publication."

## 3. **Excitement** (1-5 scale with half-points)
Evaluates subjective appeal through innovation, impact, and relevance.
- **5:** "Highly Exciting: would recommend to others."
- **4:** "Exciting: would mention to others."
- **3:** "Interesting: might mention some points."
- **2:** "Potentially Interesting: doesn't resonate with reviewer."
- **1:** "Not Exciting: lacks community resonance."

## 4. **Overall Assessment** (1-5 scale with half-points)
Publication recommendation ranging from awards to rejection.
- **5:** Consider for Award (top 2.5%)
- **4:** Conference acceptance
- **3:** Findings acceptance
- **2:** Resubmit next cycle
- **1:** Do not resubmit

## 5. **Additional Dimensions**
- **Reproducibility** (1-5)
- **Datasets** (1-5, if applicable)
- **Software** (1-5, if applicable)
- **Author Identity Knowledge** (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6174
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-15T06:44:22.225275+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 55, \"total_citations\": 76, \"unique_cited_keys\": 55, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 51, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 43119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 44223
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-15T06:47:42.772755+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (ACL ARR May cycle)\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings acceptance 边缘）\n**一句话总结**: 研究问题定义清晰、统计方法论扎实的实证研究，但核心发现（correlation-selection gap）部分因信号设计的内在限制（4/5 为 instance-level）而缺乏足够的非平凡性，且 constrained decoding 对 selection gap 的贡献未被实验量化。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 统计方法论优秀（bootstrap + TOST + effect size + 多 seed），但核心 claim 的非平凡性受质疑——4/5 信号 instance-level 使得 selection 失败部分为 by-design；constrained decoding confound 未实验验证 |\n| Excitement | 3.0 / 5 | 填补了 quality estimation vs. sample selection 的区分空白，但本质是 negative result + 对已知设计限制的实证确认，practical impact 有限 |\n| Reproducibility | 3.0 / 5 | 使用公开数据集和开源模型，但 LoRA 训练缺少关键超参数（learning rate, batch size, warmup, eval strategy），prompt template 未提供 |\n| Confidence | 4 / 5 | 仔细阅读了全文和附录，熟悉 self-consistency、MBR decoding、uncertainty estimation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的非平凡性不足——instance-level 信号的 selection 失败部分为 tautological\n\n- 具体位置：§3.1（per-sample vs instance-level 定义）、§4.3（Table 3 selection 结果）、§5 Discussion 第一段\n- 问题：论文定义了 per-sample 信号（直接为每个 $y_i$ 打分）和 instance-level 信号（为整个输入 $x$ 打分）。5 个信号中 4 个（Voting, SJ, FK, EM）是 instance-level，本身不区分同一 input 下的不同 candidate。论文通过 consensus-proximity 策略将 instance-level 信号转化为 per-sample selector（§3.3: \"instance-level signals select the sample closest to the consensus output\"），这等价于 MBR decoding（§5）。但论文的叙述框架将\"所有信号均未显著超越 greedy\"包装为一个统一的经验发现（\"correlation-selection gap\"），而实际上 instance-level 信号的 selection 失败主要是 **设计层面的先验预期**——consensus-proximity 将 instance-level 一致性转化为 per-sample 排序，但当 per-sample variance 低时（mean pairwise SJ = 0.703），consensus-proximity 得分的区分度天然有限。这一点在 Discussion 中被承认（\"Four of five signals are instance-level by construction and cannot rank N candidates\"），但这个自承的事实与 §4.3 和 abstract 中将其作为核心 empirical contribution 的定位之间存在张力。\n- 真正非平凡的发现是 **logprob 的 selection 失败**：作为唯一的 per-sample 信号，logprob 在 SciERC 上仅获得 +0.6 pp（NER, p=0.39）和 -0.9 pp（RE），Cohen's d = 0.038。但这一发现被淹没在\"所有信号统一失败\"的叙述中，且 Discussion 将原因归结为\"primarily reflects grammar compliance under constrained decoding—75% of comparisons are effectively ties\"——这实际上指向 constrained decoding 是 confounding factor（见 N2）。\n- 为什么影响接收：核心 contribution #2 的新颖性被削弱。如果 4/5 信号的 selection 失败可以从其 instance-level 设计中先验推导，那么 \"gap\" 更多是一个 terminology 贡献而非 empirical discovery。\n- 建议修改方向：(a) 明确区分\"instance-level 信号通过 consensus-proximity 做 selection 失败\"和\"per-sample 信号（logprob）做 selection 失败\"是两个独立发现，前者的非平凡性来自 consensus-proximity/MBR 策略的失败，后者的非平凡性来自 logprob 在 constrained decoding 下的区分度坍缩；(b) 重新定义 \"gap\" 的 scope，聚焦在\"即使是 MBR-style 的 consensus-proximity selection，在 structured IE 上也失败\"——这比笼统的 \"所有信号失败\" 更精确且更有说服力。\n\n**N2** [critical] Constrained decoding 作为 correlation-selection gap 的 confounding factor 未被实验量化\n\n- 具体位置：§4.1（\"Inference uses vLLM with constrained decoding\"），§7 Limitations（\"Constrained decoding...potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit\"），§5 Discussion（\"logprob primarily reflects grammar compliance under constrained decoding—75% of comparisons are effectively ties\"）\n- 问题：Constrained decoding（Outlines/vLLM）强制输出符合 JSON schema，可能从两方面造成 confound：(1) 压缩 per-sample diversity，使得不同 sample 的\"有意义差异\"被限制在 entity 选择层面而非格式/结构层面，降低信号的区分空间；(2) 使 logprob 主要反映 grammar compliance 而非 semantic confidence（论文自己在 Discussion 中承认）。论文报告了 SciERC 上仍有 43% unique outputs 和 per-sample F1 std = 0.14，但这并不排除 diversity 被压缩到 constrained decoding 允许的子空间内。论文在 Limitations 中承认此问题但未实验验证。\n- 为什么影响接收：如果 gap 主要由 constrained decoding 导致，则 \"correlation-selection gap\" 不是 confidence signals 在 structured IE 上的固有限制，而是特定 inference setup 的 artifact。这直接动摇论文的 generalization claim（\"reframe consistency signals as quality estimators rather than output selectors for structured IE\"——abstract 最后一句）。\n- 建议修改方向：(a) 增加 free-form generation（不使用 constrained decoding）的对比实验，即使需要 post-hoc 解析且 parse success rate 较低；(b) 或至少分析 constrained decoding 下 logprob 值的分布——如果 75% 的 comparison 是 effective ties，则量化 \"tie\" 的定义（Δlogprob < ε），并分析在 non-tie 的 25% 上 logprob 是否能成功 select；(c) 对 effective ties 进行更深入的分析：是 logprob 值本身差异小（constrained decoding 的 grammar path 导致），还是 logprob 差异虽大但与 F1 差异无关？\n\n**N3** [critical] 训练细节不足以复现\n\n- 具体位置：§4.1（\"fine-tuned with LoRA (rank=32, α=64) for 5 epochs using LLaMA Factory\"）\n- 问题：训练配置缺少以下关键信息：learning rate、batch size（per-device 和 effective）、warmup steps/ratio、weight decay、optimizer（AdamW? 参数？）、gradient accumulation steps、early stopping 策略（是否使用？基于什么指标？）、训练数据的 train/dev split 方式、prompt template（NER/RE 各用什么 prompt 格式？）、训练数据量、LoRA target modules（all linear? q_proj/v_proj only?）、max sequence length。\n- 为什么影响接收：ACL ARR 要求 reproducibility，LoRA 微调对超参数敏感（特别是 learning rate 和 target modules），不同配置可能导致模型能力差异，进而影响 output diversity 和 consistency 信号的表现。\n- 建议修改方向：补充完整的训练配置表格，优选放在附录。提供 prompt template 示例。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] RE 结论仅基于 SciERC 单一数据集\n\n- 具体位置：§4.1（datasets）、§6 Conclusion、§7 Limitations\n- 问题：RE 分析仅使用 SciERC（7 relation types，40% zero F1），论文 claim \"correlation-selection gap\" 覆盖 NER 和 RE，但 RE 证据严重不足。SciERC RE 的 40% zero-F1 base rate 进一步压缩了信号可区分的范围。论文在 Conclusion 中承认 \"our RE conclusions rest on SciERC alone\"，但 abstract 和 introduction 的表述仍然将 RE 作为等权的证据呈现。\n- 建议：(a) 增加至少一个 RE 数据集（如 TACRED、DocRED、ACE05）；或 (b) 在 abstract/introduction 中明确 RE findings 是初步的。当前 abstract 说 \"across NER (three datasets of varying difficulty) and RE (SciERC)\"，建议改为强调 NER 是主要证据。\n\n**W2** [warning] Fleiss' κ 应用于非独立 temperature-sampled outputs 的理论 justification 薄弱\n\n- 具体位置：§3.2 Fleiss' κ 段落（\"While FK assumes independent raters, temperature-based sampling provides sufficient response diversity...\"）\n- 问题：Fleiss' κ 的统计理论假设 raters 是独立的。Temperature sampling 产生的 N 个输出共享相同的模型权重、prompt、和前缀，因此系统性地非独立。论文引用 empirical evidence（excess agreement -0.4% to -4.0%），声称 FK 不被 inter-sample dependence 所 inflate。但这个实证观察的 methodology 不清楚——excess agreement 是相对于什么 baseline 计算的？如果 baseline 本身也有问题，结论不可靠。此外，negative excess agreement（即 temperature-sampled outputs 的 agreement 低于独立 rater 的预期）本身是一个值得讨论的现象——为什么从同一模型 sample 出的结果反而 agreement 更低？这可能指向 temperature sampling 引入的 noise 结构与 Fleiss' κ 假设的 random disagreement 结构不同。\n- 建议：(a) 解释 excess agreement 的计算方法；(b) 讨论 negative excess agreement 的含义；(c) 或者将 FK 的 justification 限定为\"作为 agreement 的经验度量使用，不做统计推断\"——论文确实只将 FK 用于 rank correlation，不用于假设检验。\n\n**W3** [warning] Soft Jaccard 定义中 normalizer 的选择缺乏对比\n\n- 具体位置：§3.2 Soft Jaccard（\"We use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples\"）\n- 问题：$\\max(|g_i|, |g_j|)$ 和 $|g_i \\cup g_j|$ 在 entity set 大小不对称时有不同的 penalization behavior。论文仅声明使用前者但未比较。此外，当两个 sample 的 entity set 大小差异大时，$\\max$ normalizer 可能过度惩罚；当 entity set 有大量重叠时，$|g_i \\cup g_j|$ 可能更合适。作为 core signal 的设计决策，缺少 ablation 或 justification。\n- 建议：至少在附录中报告使用 $|g_i \\cup g_j|$ normalizer 的 SJ 结果，或提供选择 $\\max$ 的理论依据。\n\n**W4** [warning] 模型规模限于 8B，generalization 受限\n\n- 具体位置：§4.1（models）、§7 Limitations\n- 问题：两个模型均为 8B 参数。Larger models（70B+）可能产生更高质量、更多样化的 output，这可能改变 signal landscape——例如，logprob 在更强模型上可能更有区分力（因为 grammar compliance 已接近完美，logprob 更多反映 semantic confidence）。论文在 Limitations 中承认此点。\n- 建议：讨论 model scale 可能如何影响 gap 的方向——是预期 gap 缩小（更强模型 logprob 更有信息量）还是扩大（更强模型 output 更一致，per-sample variance 更低）？\n\n**W5** [warning] TOST 等价性检验的 δ 选择缺乏理论或实践依据\n\n- 具体位置：Appendix E Table 6（\"TOST equivalence testing\"）\n- 问题：TOST 的 δ 选择（±2, ±3, ±5 pp）直接影响等价性结论。论文报告了三个 δ 水平但未讨论哪个是\"合理\"的等价边界。在 IE 任务中，2 pp 的 F1 差异是否有实际意义？这取决于下游应用。论文应讨论 δ 的选择依据——例如，如果 annotation agreement 的 F1 variance 是 ~3 pp，则 ±3 pp 是合理的等价边界。\n- 建议：提供 δ 选择的实际意义论证，或至少引用 IE 任务中 F1 差异的 practical significance 标准。\n\n**W6** [warning] N=8 主实验的 single-seed 稳定性\n\n- 具体位置：§4.1（\"N=8 results use seed=42\"）、Appendix D（multi-seed 分析）\n- 问题：主表格（Table 1, Table 3）的 N=8 结果均来自 seed=42 单次运行。虽然 Appendix D 的 3-seed 分析显示 σ≤0.025 且 ranking 稳定，但 multi-seed 分析仅覆盖 SciERC NER（Table 7），不覆盖 CoNLL N=8 和 SciERC RE。特别是 selection gap 的 p-value (p=0.39) 来自单 seed，其在不同 seed 下的变异未报告。\n- 建议：(a) 至少对 SciERC 的 selection 分析（Table 3）报告多 seed 结果；(b) 在主文中注明 N=8 single-seed 的局限性而非仅在附录中提及。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.2 第一段：footnote 5 说 \"semantic entropy achieves AUROC ≈ 0.75-0.85 on discrete-answer QA tasks\" 后加了 \"however, these numbers are not directly comparable\"。既然不可比，引用 semantic entropy 的数字可能误导读者。建议删除具体数字或更清楚地框定比较目的。\n- Table 1（N=16 部分）：只填了 LLaMA CoNLL 的值，Qwen 和 SciERC 的 N=16 结果为空白。建议在 caption 中说明哪些配置有 N=16 数据，或将 N=16 结果全部移至附录以保持主表的一致性。\n- §3.2 Entity Voting：公式 (5) 中 $|E_\\cup|$ 当所有 sample 都产生空输出时，分母为 0。虽然实践中通过 constrained decoding 可能不会出现空输出，但数学定义应注明边界条件处理。\n- Appendix C Fig 3 reliability diagram：caption 说 \"calibration ECE 0.069-0.096\"，但正文 §4.4 也报告了相同的数字。ECE 的 bin 数量未报告（10? 15? 20?）——不同 bin 数会显著影响 ECE 值。\n\n---\n\n## 主要优势\n\n1. **研究问题定义清晰**：quality estimation vs. sample selection 的概念区分是有价值的贡献，prior work（如 Nedellec et al. 2026）确实混淆了这两个目标。§3.1 的 per-sample vs. instance-level 形式化是简洁有效的。\n\n2. **统计方法论严谨**：paired bootstrap resampling (B=10,000)、TOST 等价性检验、effect size 报告（Cohen's d, win%）、pairwise bootstrap CIs with Bonferroni correction——这在 NLP 实证论文中是高于平均水准的统计实践。\n\n3. **Difficulty gradient 分析有深度**：CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）的三级难度梯度设计精良，WNUT-17 上 full-set vs. conditional-set 的对比（Table 5: Voting full ρ=0.724 vs. conditional ρ=0.038）是一个很有说服力的发现——说明在高 failure rate 下 consistency signals 的表现可以是完全 artifactual 的。\n\n4. **Transparency**：论文在 Limitations 和 Discussion 中对自身局限性的讨论是诚实和全面的（constrained decoding confound、single RE dataset、model scale limitation、logprob temperature data missing）。\n\n5. **MBR decoding 连接**：§5 将 selection strategies 形式化为 MBR decoding 变体是一个有价值的理论框架，帮助读者理解不同信号在 selection 中实际做了什么。\n\n6. **引用质量高**：55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。引用覆盖了 self-consistency、uncertainty estimation、generative IE、MBR decoding 等相关领域，包含 2025-2026 的最新工作。\n\n---\n\n## 缺失引用\n\n- **Bertsch et al. (2024)** \"In-Context Learning with Long-Context Models: An In-Depth Exploration\" — 讨论了 long-context models 在 IE 上的 test-time scaling 行为，与本文的 test-time scaling 框架相关。\n- **Wiher et al. (2022)** \"On Decoding Strategies for Neural Text Generators\" — 系统比较了不同 decoding strategies 对 output diversity 的影响，可帮助 contextualize constrained decoding 对 diversity 的压缩效应。\n- **Müller & Sennrich (2021)** \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\" — 深入分析了 MBR decoding 的 failure modes，与本文 §5 的 MBR 连接直接相关。\n\n---\n\n## 总结判断\n\n本文是一篇方法论严谨的实证研究，清晰定义了 quality estimation vs. sample selection 的区分，并在统计分析上显著超过 NLP 实证论文的平均水平。但核心发现 \"correlation-selection gap\" 的非平凡性不足（4/5 信号 instance-level 使 selection 失败部分为 by-design），且 constrained decoding 作为主要 confound 未被实验控制。这两个问题削弱了论文的 contribution novelty，使其更像是对一个可预见限制的实证确认，而非一个令人惊讶的发现。\n\n推荐 **Findings acceptance（边缘）**，条件是修复训练细节（N3）并更精确地定位 gap 的非平凡性来源（N1）。如果能增加 free-form generation 对比实验（N2），将显著增强论文的说服力。\n\n**Overall Assessment**: 3.0 / 5 (Findings acceptance 边缘)\n**Confidence**: 4 / 5",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (ACL ARR May cycle)\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings acceptance 边缘）\n**一句话总结**: 研究问题定义清晰、统计方法论扎实的实证研究，但核心发现（correlation-selection gap）部分因信号设计的内在限制（4/5 为 instance-level）而缺乏足够的非平凡性，且 constrained decoding 对 selection gap 的贡献未被实验量化。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 统计方法论优秀（bootstrap + TOST + effect size + 多 seed），但核心 claim 的非平凡性受质疑——4/5 信号 instance-level 使得 selection 失败部分为 by-design；constrained decoding confound 未实验验证 |\n| Excitement | 3.0 / 5 | 填补了 quality estimation vs. sample selection 的区分空白，但本质是 negative result + 对已知设计限制的实证确认，practical impact 有限 |\n| Reproducibility | 3.0 / 5 | 使用公开数据集和开源模型，但 LoRA 训练缺少关键超参数（learning rate, batch size, warmup, eval strategy），prompt template 未提供 |\n| Confidence | 4 / 5 | 仔细阅读了全文和附录，熟悉 self-consistency、MBR decoding、uncertainty estimation 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的非平凡性不足——instance-level 信号的 selection 失败部分为 tautological\n\n- 具体位置：§3.1（per-sample vs instance-level 定义）、§4.3（Table 3 selection 结果）、§5 Discussion 第一段\n- 问题：论文定义了 per-sample 信号（直接为每个 $y_i$ 打分）和 instance-level 信号（为整个输入 $x$ 打分）。5 个信号中 4 个（Voting, SJ, FK, EM）是 instance-level，本身不区分同一 input 下的不同 candidate。论文通过 consensus-proximity 策略将 instance-level 信号转化为 per-sample selector（§3.3: \"instance-level signals select the sample closest to the consensus output\"），这等价于 MBR decoding（§5）。但论文的叙述框架将\"所有信号均未显著超越 greedy\"包装为一个统一的经验发现（\"correlation-selection gap\"），而实际上 instance-level 信号的 selection 失败主要是 **设计层面的先验预期**——consensus-proximity 将 instance-level 一致性转化为 per-sample 排序，但当 per-sample variance 低时（mean pairwise SJ = 0.703），consensus-proximity 得分的区分度天然有限。这一点在 Discussion 中被承认（\"Four of five signals are instance-level by construction and cannot rank N candidates\"），但这个自承的事实与 §4.3 和 abstract 中将其作为核心 empirical contribution 的定位之间存在张力。\n- 真正非平凡的发现是 **logprob 的 selection 失败**：作为唯一的 per-sample 信号，logprob 在 SciERC 上仅获得 +0.6 pp（NER, p=0.39）和 -0.9 pp（RE），Cohen's d = 0.038。但这一发现被淹没在\"所有信号统一失败\"的叙述中，且 Discussion 将原因归结为\"primarily reflects grammar compliance under constrained decoding—75% of comparisons are effectively ties\"——这实际上指向 constrained decoding 是 confounding factor（见 N2）。\n- 为什么影响接收：核心 contribution #2 的新颖性被削弱。如果 4/5 信号的 selection 失败可以从其 instance-level 设计中先验推导，那么 \"gap\" 更多是一个 terminology 贡献而非 empirical discovery。\n- 建议修改方向：(a) 明确区分\"instance-level 信号通过 consensus-proximity 做 selection 失败\"和\"per-sample 信号（logprob）做 selection 失败\"是两个独立发现，前者的非平凡性来自 consensus-proximity/MBR 策略的失败，后者的非平凡性来自 logprob 在 constrained decoding 下的区分度坍缩；(b) 重新定义 \"gap\" 的 scope，聚焦在\"即使是 MBR-style 的 consensus-proximity selection，在 structured IE 上也失败\"——这比笼统的 \"所有信号失败\" 更精确且更有说服力。\n\n**N2** [critical] Constrained decoding 作为 correlation-selection gap 的 confounding factor 未被实验量化\n\n- 具体位置：§4.1（\"Inference uses vLLM with constrained decoding\"），§7 Limitations（\"Constrained decoding...potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit\"），§5 Discussion（\"logprob primarily reflects grammar compliance under constrained decoding—75% of comparisons are effectively ties\"）\n- 问题：Constrained decoding（Outlines/vLLM）强制输出符合 JSON schema，可能从两方面造成 confound：(1) 压缩 per-sample diversity，使得不同 sample 的\"有意义差异\"被限制在 entity 选择层面而非格式/结构层面，降低信号的区分空间；(2) 使 logprob 主要反映 grammar compliance 而非 semantic confidence（论文自己在 Discussion 中承认）。论文报告了 SciERC 上仍有 43% unique outputs 和 per-sample F1 std = 0.14，但这并不排除 diversity 被压缩到 constrained decoding 允许的子空间内。论文在 Limitations 中承认此问题但未实验验证。\n- 为什么影响接收：如果 gap 主要由 constrained decoding 导致，则 \"correlation-selection gap\" 不是 confidence signals 在 structured IE 上的固有限制，而是特定 inference setup 的 artifact。这直接动摇论文的 generalization claim（\"reframe consistency signals as quality estimators rather than output selectors for structured IE\"——abstract 最后一句）。\n- 建议修改方向：(a) 增加 free-form generation（不使用 constrained decoding）的对比实验，即使需要 post-hoc 解析且 parse success rate 较低；(b) 或至少分析 constrained decoding 下 logprob 值的分布——如果 75% 的 comparison 是 effective ties，则量化 \"tie\" 的定义（Δlogprob < ε），并分析在 non-tie 的 25% 上 logprob 是否能成功 select；(c) 对 effective ties 进行更深入的分析：是 logprob 值本身差异小（constrained decoding 的 grammar path 导致），还是 logprob 差异虽大但与 F1 差异无关？\n\n**N3** [critical] 训练细节不足以复现\n\n- 具体位置：§4.1（\"fine-tuned with LoRA (rank=32, α=64) for 5 epochs using LLaMA Factory\"）\n- 问题：训练配置缺少以下关键信息：learning rate、batch size（per-device 和 effective）、warmup steps/ratio、weight decay、optimizer（AdamW? 参数？）、gradient accumulation steps、early stopping 策略（是否使用？基于什么指标？）、训练数据的 train/dev split 方式、prompt template（NER/RE 各用什么 prompt 格式？）、训练数据量、LoRA target modules（all linear? q_proj/v_proj only?）、max sequence length。\n- 为什么影响接收：ACL ARR 要求 reproducibility，LoRA 微调对超参数敏感（特别是 learning rate 和 target modules），不同配置可能导致模型能力差异，进而影响 output diversity 和 consistency 信号的表现。\n- 建议修改方向：补充完整的训练配置表格，优选放在附录。提供 prompt template 示例。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] RE 结论仅基于 SciERC 单一数据集\n\n- 具体位置：§4.1（datasets）、§6 Conclusion、§7 Limitations\n- 问题：RE 分析仅使用 SciERC（7 relation types，40% zero F1），论文 claim \"correlation-selection gap\" 覆盖 NER 和 RE，但 RE 证据严重不足。SciERC RE 的 40% zero-F1 base rate 进一步压缩了信号可区分的范围。论文在 Conclusion 中承认 \"our RE conclusions rest on SciERC alone\"，但 abstract 和 introduction 的表述仍然将 RE 作为等权的证据呈现。\n- 建议：(a) 增加至少一个 RE 数据集（如 TACRED、DocRED、ACE05）；或 (b) 在 abstract/introduction 中明确 RE findings 是初步的。当前 abstract 说 \"across NER (three datasets of varying difficulty) and RE (SciERC)\"，建议改为强调 NER 是主要证据。\n\n**W2** [warning] Fleiss' κ 应用于非独立 temperature-sampled outputs 的理论 justification 薄弱\n\n- 具体位置：§3.2 Fleiss' κ 段落（\"While FK assumes independent raters, temperature-based sampling provides sufficient response diversity...\"）\n- 问题：Fleiss' κ 的统计理论假设 raters 是独立的。Temperature sampling 产生的 N 个输出共享相同的模型权重、prompt、和前缀，因此系统性地非独立。论文引用 empirical evidence（excess agreement -0.4% to -4.0%），声称 FK 不被 inter-sample dependence 所 inflate。但这个实证观察的 methodology 不清楚——excess agreement 是相对于什么 baseline 计算的？如果 baseline 本身也有问题，结论不可靠。此外，negative excess agreement（即 temperature-sampled outputs 的 agreement 低于独立 rater 的预期）本身是一个值得讨论的现象——为什么从同一模型 sample 出的结果反而 agreement 更低？这可能指向 temperature sampling 引入的 noise 结构与 Fleiss' κ 假设的 random disagreement 结构不同。\n- 建议：(a) 解释 excess agreement 的计算方法；(b) 讨论 negative excess agreement 的含义；(c) 或者将 FK 的 justification 限定为\"作为 agreement 的经验度量使用，不做统计推断\"——论文确实只将 FK 用于 rank correlation，不用于假设检验。\n\n**W3** [warning] Soft Jaccard 定义中 normalizer 的选择缺乏对比\n\n- 具体位置：§3.2 Soft Jaccard（\"We use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples\"）\n- 问题：$\\max(|g_i|, |g_j|)$ 和 $|g_i \\cup g_j|$ 在 entity set 大小不对称时有不同的 penalization behavior。论文仅声明使用前者但未比较。此外，当两个 sample 的 entity set 大小差异大时，$\\max$ normalizer 可能过度惩罚；当 entity set 有大量重叠时，$|g_i \\cup g_j|$ 可能更合适。作为 core signal 的设计决策，缺少 ablation 或 justification。\n- 建议：至少在附录中报告使用 $|g_i \\cup g_j|$ normalizer 的 SJ 结果，或提供选择 $\\max$ 的理论依据。\n\n**W4** [warning] 模型规模限于 8B，generalization 受限\n\n- 具体位置：§4.1（models）、§7 Limitations\n- 问题：两个模型均为 8B 参数。Larger models（70B+）可能产生更高质量、更多样化的 output，这可能改变 signal landscape——例如，logprob 在更强模型上可能更有区分力（因为 grammar compliance 已接近完美，logprob 更多反映 semantic confidence）。论文在 Limitations 中承认此点。\n- 建议：讨论 model scale 可能如何影响 gap 的方向——是预期 gap 缩小（更强模型 logprob 更有信息量）还是扩大（更强模型 output 更一致，per-sample variance 更低）？\n\n**W5** [warning] TOST 等价性检验的 δ 选择缺乏理论或实践依据\n\n- 具体位置：Appendix E Table 6（\"TOST equivalence testing\"）\n- 问题：TOST 的 δ 选择（±2, ±3, ±5 pp）直接影响等价性结论。论文报告了三个 δ 水平但未讨论哪个是\"合理\"的等价边界。在 IE 任务中，2 pp 的 F1 差异是否有实际意义？这取决于下游应用。论文应讨论 δ 的选择依据——例如，如果 annotation agreement 的 F1 variance 是 ~3 pp，则 ±3 pp 是合理的等价边界。\n- 建议：提供 δ 选择的实际意义论证，或至少引用 IE 任务中 F1 差异的 practical significance 标准。\n\n**W6** [warning] N=8 主实验的 single-seed 稳定性\n\n- 具体位置：§4.1（\"N=8 results use seed=42\"）、Appendix D（multi-seed 分析）\n- 问题：主表格（Table 1, Table 3）的 N=8 结果均来自 seed=42 单次运行。虽然 Appendix D 的 3-seed 分析显示 σ≤0.025 且 ranking 稳定，但 multi-seed 分析仅覆盖 SciERC NER（Table 7），不覆盖 CoNLL N=8 和 SciERC RE。特别是 selection gap 的 p-value (p=0.39) 来自单 seed，其在不同 seed 下的变异未报告。\n- 建议：(a) 至少对 SciERC 的 selection 分析（Table 3）报告多 seed 结果；(b) 在主文中注明 N=8 single-seed 的局限性而非仅在附录中提及。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.2 第一段：footnote 5 说 \"semantic entropy achieves AUROC ≈ 0.75-0.85 on discrete-answer QA tasks\" 后加了 \"however, these numbers are not directly comparable\"。既然不可比，引用 semantic entropy 的数字可能误导读者。建议删除具体数字或更清楚地框定比较目的。\n- Table 1（N=16 部分）：只填了 LLaMA CoNLL 的值，Qwen 和 SciERC 的 N=16 结果为空白。建议在 caption 中说明哪些配置有 N=16 数据，或将 N=16 结果全部移至附录以保持主表的一致性。\n- §3.2 Entity Voting：公式 (5) 中 $|E_\\cup|$ 当所有 sample 都产生空输出时，分母为 0。虽然实践中通过 constrained decoding 可能不会出现空输出，但数学定义应注明边界条件处理。\n- Appendix C Fig 3 reliability diagram：caption 说 \"calibration ECE 0.069-0.096\"，但正文 §4.4 也报告了相同的数字。ECE 的 bin 数量未报告（10? 15? 20?）——不同 bin 数会显著影响 ECE 值。\n\n---\n\n## 主要优势\n\n1. **研究问题定义清晰**：quality estimation vs. sample selection 的概念区分是有价值的贡献，prior work（如 Nedellec et al. 2026）确实混淆了这两个目标。§3.1 的 per-sample vs. instance-level 形式化是简洁有效的。\n\n2. **统计方法论严谨**：paired bootstrap resampling (B=10,000)、TOST 等价性检验、effect size 报告（Cohen's d, win%）、pairwise bootstrap CIs with Bonferroni correction——这在 NLP 实证论文中是高于平均水准的统计实践。\n\n3. **Difficulty gradient 分析有深度**：CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）的三级难度梯度设计精良，WNUT-17 上 full-set vs. conditional-set 的对比（Table 5: Voting full ρ=0.724 vs. conditional ρ=0.038）是一个很有说服力的发现——说明在高 failure rate 下 consistency signals 的表现可以是完全 artifactual 的。\n\n4. **Transparency**：论文在 Limitations 和 Discussion 中对自身局限性的讨论是诚实和全面的（constrained decoding confound、single RE dataset、model scale limitation、logprob temperature data missing）。\n\n5. **MBR decoding 连接**：§5 将 selection strategies 形式化为 MBR decoding 变体是一个有价值的理论框架，帮助读者理解不同信号在 selection 中实际做了什么。\n\n6. **引用质量高**：55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。引用覆盖了 self-consistency、uncertainty estimation、generative IE、MBR decoding 等相关领域，包含 2025-2026 的最新工作。\n\n---\n\n## 缺失引用\n\n- **Bertsch et al. (2024)** \"In-Context Learning with Long-Context Models: An In-Depth Exploration\" — 讨论了 long-context models 在 IE 上的 test-time scaling 行为，与本文的 test-time scaling 框架相关。\n- **Wiher et al. (2022)** \"On Decoding Strategies for Neural Text Generators\" — 系统比较了不同 decoding strategies 对 output diversity 的影响，可帮助 contextualize constrained decoding 对 diversity 的压缩效应。\n- **Müller & Sennrich (2021)** \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\" — 深入分析了 MBR decoding 的 failure modes，与本文 §5 的 MBR 连接直接相关。\n\n---\n\n## 总结判断\n\n本文是一篇方法论严谨的实证研究，清晰定义了 quality estimation vs. sample selection 的区分，并在统计分析上显著超过 NLP 实证论文的平均水平。但核心发现 \"correlation-selection gap\" 的非平凡性不足（4/5 信号 instance-level 使 selection 失败部分为 by-design），且 constrained decoding 作为主要 confound 未被实验控制。这两个问题削弱了论文的 contribution novelty，使其更像是对一个可预见限制的实证确认，而非一个令人惊讶的发现。\n\n推荐 **Findings acceptance（边缘）**，条件是修复训练细节（N3）并更精确地定位 gap 的非平凡性来源（N1）。如果能增加 free-form generation 对比实验（N2），将显著增强论文的说服力。\n\n**Overall Assessment**: 3.0 / 5 (Findings acceptance 边缘)\n**Confidence**: 4 / 5",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-15T06:47:47.101329+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4328
}
```

</details>

---


### Assistant

_source line 332 · 2026-05-15T06:47:55.596616+00:00_

审稿报告已提交给 Review Director。

**审稿结论**：Overall 3.0/5（Findings acceptance 边缘），Soundness 3.5，Excitement 3.0，Confidence 4/5。

三个 Must-Fix 问题：
1. **Correlation-selection gap 非平凡性不足**：4/5 信号是 instance-level，selection 失败部分是 by-design 而非 empirical surprise。真正有趣的发现（logprob 的 selection 失败）被淹没在统一叙述中。
2. **Constrained decoding confound**：论文自己承认 logprob 75% 的比较是 effective ties，指向 constrained decoding 可能是 gap 的主因而非信号本身的固有限制，但未实验验证。
3. **训练细节不足**：缺少 learning rate、batch size、prompt template 等关键超参数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

36 recorded events


### User

_source line 333 · 2026-05-15T06:52:12.477847+00:00_

[Round 4 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）

---

## Reviewer 2 — Round 1 审稿报告

**Overall**: 3.5 / 5（Findings: borderline accept）

### 维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 统计方法严谨（bootstrap CI, TOST equivalence testing, 3-seed validation），RE 仅 SciERC 单数据集是主要弱点 |
| Excitement | 2.5 / 5 | Gap 概念有实用价值，但核心原因可从信号定义推出，缺少"意外性" |
| Overall Assessment | 3.5 / 5 | 符合 Findings 标准，但 novelty 不足以达到 main conference |
| Confidence | 4 / 5 | 熟悉相关文献，仔细阅读全文和附录 |

### 主要优势
1. 系统性和严谨性出色（bootstrap CI B=10,000, TOST, 3-seed）
2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献
3. 任务难度依赖的信号排名有实际指导意义
4. MBR 连接优雅
5. Limitations section 诚实且具体

### Must-Fix

**N1** [critical] Correlation-selection gap 的"意外性"论证不足
- 4/5 信号 instance-level，selection 失败可从设计原理推出
- 论文将 gap 作为核心贡献但未正面论证 "why not obvious a priori"
- 建议：(a) 讨论 MBR 在 MT 中成功但 IE 中失败的原因；(b) 深入分析 logprob ties 的 75% 统计数据；(c) 讨论什么样的 per-sample 信号可能 work

**N2** [critical] RE 结论基于单一数据集（SciERC），泛化性不明
- SciERC RE 40% zero-F1 floor effect，7 种关系类型信号质量差异巨大
- Contribution #1 "quality estimation for NER and RE" 在 RE 部分缺乏足够支撑
- 建议：增加 RE 数据集或明确降级 RE 贡献

### Should-Fix

**W1** [warning] Abstract 过于密集，可读性差
- 第 4 行超长句子含 6 个括号注释、3 个分号
- 建议拆分为 2-3 个独立句子

**W2** [warning] "confidence signal" vs "consistency signal" 术语不一致
- "confidence signal" 是统称但多处用 "consistency signals" 泛指（logprob 不是 consistency signal）
- 建议在 Method 开头明确定义

**W3** [warning] Nedellec (2026) 引用键名 misleading
- BibTeX 键名 `nedellec2026consistency` 但第一作者实际是 Yao
- 正文多处说 "Nedellec (2026)" 但 \citet 输出 "Yao et al. (2026)"

**W4** [warning] Soft Jaccard 对 Nedellec 改进幅度有限
- SJ vs EM: Δρ=+0.065，CI 下界仅 +0.003，Bonferroni 下不显著
- CoNLL 上 EM 反超 SJ
- 建议弱化 "structural advantage" 叙事，强调 difficulty-dependent complementarity

**W5** [warning] 缺少 constrained decoding 对 diversity 影响的实验对照
- 论文承认 constrained decoding 可能压缩 diversity 但无对照
- 建议增加 free-form generation baseline

**W6** [warning] 缺少若干相关工作
- Xiong et al. (2024) "Can LLMs Express Their Uncertainty?" ICLR 2024（高相关）
- Ye et al. (2025) "Do LLMs Estimate Uncertainty Well?" ICLR 2025
- Generative IE survey（COLING 2025）

### 小问题
1. Table 1 N=16 数据不完整
2. Figure 1 caption 未解释 consensus-proximity
3. references.bib 格式小问题
4. WNUT-17 conditional ρ 数字建议在主文提及
5. Ethics statement 位置不够规范

### Missing References
| 文献 | 相关度 | 优先级 |
|------|--------|--------|
| Xiong et al. (2024) ICLR | 高 | Should-cite |
| Ye et al. (2025) ICLR | 中 | Nice-to-cite |
| Xu et al. (2025) COLING | 中 | Nice-to-cite |

---

请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-15T06:52:37.059626+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-15T06:52:37.210585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-15T06:52:41.576997+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-15T06:52:41.627734+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-15T06:52:45.092104+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-5",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-5",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-15T06:52:47.245017+00:00_

Error: result (3,951,545 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827967028.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827967028.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827967028.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2152
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-15T06:52:51.462634+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 341 · 2026-05-15T06:52:51.916296+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-15T06:52:51.973582+00:00_

Error: result (641,065 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827971902.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827971902.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827971902.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 510
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-15T06:52:52.484875+00:00_

Error: result (720,677 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827972420.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827972420.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8d164322-042b-459c-b3de-6ad10c70dae0/tool-results/mcp-agent-ml-research-pdf_to_images-1778827972420.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 568
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-15T06:52:59.263896+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/_pdf_images/**/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/_pdf_images/**/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-15T06:52:59.314632+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-15T06:53:08.207011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-15T06:53:08.658869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-15T06:53:09.012991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-15T06:53:09.013449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-15T06:53:09.971931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-15T06:53:10.474916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-15T06:53:14.240696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-15T06:53:14.894329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-15T06:53:15.398319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-15T06:53:16.408167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2167
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-15T06:53:17.615656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2721
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-15T06:53:17.767222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2368
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-15T06:53:20.981085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-15T06:53:21.483651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-15T06:53:21.888163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-15T06:53:21.888638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-15T06:53:22.444635+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-15T06:53:22.445096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-15T06:53:22.848015+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-15T06:53:23.250462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-15T06:56:10.509897+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 → 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Correlation-selection gap 的\"意外性\"论证不足**\n\nR2 认为\"4/5 信号是 instance-level，selection 失败可从设计原理推出\"。我部分反驳：\n\n1. **MBR 类比非平凡**。论文 Section 4.3（p7）建立了 MBR decoding 连接。MBR 在 MT 中成功（Eikema and Aziz, 2022），并非显然可预测 structural MBR 在 IE 中全面失败。\n2. **Logprob 是 per-sample 信号但仍失败**。75% comparisons are ties（Section 4.3, p7）是经验发现，非设计可推。\n3. **但 R2 改进建议合理**。\"Why the gap exists\"（p7-8）偏事后解释，增加 MT-vs-IE 的 MBR 对比讨论会加强论证。\n\n**结论：核心观察有价值，\"非显然性\"论证可加强，但不应作为 reject 理由。**\n\n---\n\n**[AGREE] R2-N2: RE 结论基于单一数据集**\n\n同意这是实质性弱点：\n- Table 1 RE 仅有 SciERC，NER 有三个 difficulty 梯度数据集\n- 40% zero-F1 floor effect 严重限制信号鉴别力\n- Contributions 中 RE 与 NER 并列但支撑力度不对等\n- 缓解因素：3-seed 验证和 conditional set 分析覆盖了 RE，方法论严谨性无问题\n\n**建议：增加 RE 数据集或将 RE 降级为 \"preliminary findings\"。**\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 过于密集**\n同意。第 3-4 行含 3 层嵌套括号的超长句子可拆分为 2-3 句。\n\n**[AGREE] R2-W2: terminology 不一致**\n部分同意。\"confidence signal\"（总称）vs \"consistency signal\"（子集）边界在某些段落模糊。建议 Section 3.2 开头增加明确 taxonomy。\n\n**[REBUT] R2-W3: Nedellec (2026) BibTeX 键名**\n不同意。R2 称\"正文说 Nedellec (2026) 但 \\citet 输出 Yao et al. (2026)\"——如果 \\citet 输出正确，读者看到的就是正确引用。我通读全文（p2-3）未发现硬编码的 \"Nedellec\"。BibTeX 键名是内部实现细节，不属于审稿范围。建议降级或移除。\n\n**[AGREE] R2-W4: Soft Jaccard 改进幅度有限**\n同意。SJ vs EM Δρ=+0.065 在 Bonferroni 下 marginal（论文 p5 脚注确认）；CoNLL 上 EM 反超。应调整叙事为 difficulty-dependent complementarity 而非 structural dominance。\n\n**[REBUT] R2-W5: 缺少 free-form generation baseline**\n不同意列为 Should-Fix。Constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量。论文 Limitations 已诚实讨论。可加 diversity 统计，但不需 free-form 实验。\n\n**[AGREE] R2-W6: 缺少相关工作**\n部分同意。Xiong et al. (2024) ICLR \"Can LLMs Express Their Uncertainty?\" 高度相关，应引用。其余两篇 nice-to-cite。\n\n---\n\n### 对 R2 整体评价的意见\n\n- Soundness 4/5：准确\n- Excitement 2.5/5：稍低估，Findings track 3/5 更合理（系统性 benchmark 实用价值 + MBR 连接 + difficulty-dependent guidance）\n- R2 审稿质量高。最有价值意见：N2（RE 单数据集）和 W4（SJ 优势弱化）。N1 过度批评，W3 和 W5 可降级。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 → 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Correlation-selection gap 的\"意外性\"论证不足**\n\nR2 认为\"4/5 信号是 instance-level，selection 失败可从设计原理推出\"。我部分反驳：\n\n1. **MBR 类比非平凡**。论文 Section 4.3（p7）建立了 MBR decoding 连接。MBR 在 MT 中成功（Eikema and Aziz, 2022），并非显然可预测 structural MBR 在 IE 中全面失败。\n2. **Logprob 是 per-sample 信号但仍失败**。75% comparisons are ties（Section 4.3, p7）是经验发现，非设计可推。\n3. **但 R2 改进建议合理**。\"Why the gap exists\"（p7-8）偏事后解释，增加 MT-vs-IE 的 MBR 对比讨论会加强论证。\n\n**结论：核心观察有价值，\"非显然性\"论证可加强，但不应作为 reject 理由。**\n\n---\n\n**[AGREE] R2-N2: RE 结论基于单一数据集**\n\n同意这是实质性弱点：\n- Table 1 RE 仅有 SciERC，NER 有三个 difficulty 梯度数据集\n- 40% zero-F1 floor effect 严重限制信号鉴别力\n- Contributions 中 RE 与 NER 并列但支撑力度不对等\n- 缓解因素：3-seed 验证和 conditional set 分析覆盖了 RE，方法论严谨性无问题\n\n**建议：增加 RE 数据集或将 RE 降级为 \"preliminary findings\"。**\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 过于密集**\n同意。第 3-4 行含 3 层嵌套括号的超长句子可拆分为 2-3 句。\n\n**[AGREE] R2-W2: terminology 不一致**\n部分同意。\"confidence signal\"（总称）vs \"consistency signal\"（子集）边界在某些段落模糊。建议 Section 3.2 开头增加明确 taxonomy。\n\n**[REBUT] R2-W3: Nedellec (2026) BibTeX 键名**\n不同意。R2 称\"正文说 Nedellec (2026) 但 \\citet 输出 Yao et al. (2026)\"——如果 \\citet 输出正确，读者看到的就是正确引用。我通读全文（p2-3）未发现硬编码的 \"Nedellec\"。BibTeX 键名是内部实现细节，不属于审稿范围。建议降级或移除。\n\n**[AGREE] R2-W4: Soft Jaccard 改进幅度有限**\n同意。SJ vs EM Δρ=+0.065 在 Bonferroni 下 marginal（论文 p5 脚注确认）；CoNLL 上 EM 反超。应调整叙事为 difficulty-dependent complementarity 而非 structural dominance。\n\n**[REBUT] R2-W5: 缺少 free-form generation baseline**\n不同意列为 Should-Fix。Constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量。论文 Limitations 已诚实讨论。可加 diversity 统计，但不需 free-form 实验。\n\n**[AGREE] R2-W6: 缺少相关工作**\n部分同意。Xiong et al. (2024) ICLR \"Can LLMs Express Their Uncertainty?\" 高度相关，应引用。其余两篇 nice-to-cite。\n\n---\n\n### 对 R2 整体评价的意见\n\n- Soundness 4/5：准确\n- Excitement 2.5/5：稍低估，Findings track 3/5 更合理（系统性 benchmark 实用价值 + MBR 连接 + difficulty-dependent guidance）\n- R2 审稿质量高。最有价值意见：N2（RE 单数据集）和 W4（SJ 优势弱化）。N1 过度批评，W3 和 W5 可降级。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-15T06:56:14.526926+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Assistant

_source line 368 · 2026-05-15T06:56:26.076661+00:00_

交叉回应已提交。总结：

- **N1**（gap 意外性）：[REBUT]——MBR 类比和 logprob ties 数据提供了非平凡发现，但同意加强"非显然性"论证
- **N2**（RE 单数据集）：[AGREE]——实质性弱点，建议增加数据集或降级 RE 贡献
- **W1**（Abstract 密度）：[AGREE]
- **W2**（术语不一致）：[AGREE]——建议加 taxonomy 定义
- **W3**（BibTeX 键名）：[REBUT]——内部实现细节，未观察到可见引用错误
- **W4**（SJ 优势有限）：[AGREE]——Bonferroni 下 marginal，应改为 complementarity 叙事
- **W5**（free-form baseline）：[REBUT]——constrained decoding 是方法论必要条件
- **W6**（缺少引用）：[AGREE]——Xiong et al. (2024) 应引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

42 recorded events


### User

_source line 369 · 2026-05-15T07:51:52.746830+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1 (Round 1)

### Venue 信息
- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数
- **附录**: 允许，不计页数

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（各 section 在 `sections/` 子目录下）

### 你的审查侧重：方法严谨性 + 实验设计 + 统计有效性

请重点评估以下方面：

1. **方法形式化**
   - 5 种信号的数学定义是否清晰完整、无歧义？
   - Soft Jaccard 的 Hungarian matching 描述是否足够精确可复现？
   - Fleiss' κ 应用于非独立样本的 justification 是否充分？
   - per-sample vs instance-level 信号的分类是否自洽？

2. **实验设计**
   - 数据集选择是否合理覆盖 difficulty gradient？
   - 模型选择（2×8B）是否足以支撑论文声称的 cross-architecture 结论？
   - N=8/16 和 T=0.7/1.0 的设置是否充分？
   - 训练配置（LoRA + fine-tuning）的细节是否足够复现？

3. **统计分析**
   - Bootstrap 检验的设置（B=10,000, 95% CI）是否恰当？
   - TOST 等价检验的 δ 选择是否有依据？
   - 多重比较校正的处理是否到位？
   - Spearman ρ 和 AUROC 的联合报告是否合理？

4. **核心 claim 验证**
   - "correlation-selection gap" 的论证是否严密？特别是 4/5 信号是 instance-level（定义性无法 select）vs logprob 经验性失败——这两层是否被清晰区分？
   - "constrained decoding" 作为潜在混淆变量是否被充分讨论？
   - RE 结论仅基于 SciERC 单数据集——这一局限是否在论文中被恰当处理？
   - Task-difficulty dependent signal ranking 是否有充分数据支持？

5. **复现性**
   - 训练 hyperparameters 是否完整报告？
   - Prompt template 是否提供？
   - 代码/数据可用性？

请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-15T07:52:00.982984+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-15T07:52:00.983348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-15T07:52:06.421319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-15T07:52:08.437081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-15T07:52:08.688567+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{sections/appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-15T07:52:08.739319+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-15T07:52:08.739684+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-15T07:52:15.717668+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

I found comprehensive information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring system. Here's a summary of the key details:

## Reviewer Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must b
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9296
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-15T07:52:20.488208+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-15T07:52:21.040719+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-15T07:52:22.598643+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), descriptions for each score level, and any required fields. I need the exact scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), descriptions for each score level, and any required fields. I need the exact scoring rubric."
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-15T07:52:30.378274+00:00_

# ACL Rolling Review Form - Scoring Rubric

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure; unlikely but conceivable to have missed something
- **3**: Pretty sure; good general knowledge but didn't carefully check details
- **2**: Willing to defend evaluation; fairly likely missed details or novelty unclear
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness** (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; sufficient support with optional additional experiments
- **3**: Acceptable; main claims supported, minor points need details
- **2**: Poor; main claims lack support, major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement** (1-5 scale with half-points)
- **5**: Highly Exciting; would recommend to others
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention some points
- **2**: Potentially Interesting; doesn't resonate with reviewer
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment** (1-5 scale with half-points)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility** (1-5 scale)
- **5**: Could easily reproduce results
- **4**: Could mostly reproduce with minor variations
- **3**: Could reproduce with difficulty
- **2**: Would be hard pressed to reproduce
- **1**: "Would not be able to reproduce the results"

## 6. **Datasets & Software** (1-5 scales, separate)
- **5**: Enabling impact on research choices
- **4**: Useful for other researchers
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: None released

## 7. **Author Identity Knowledge** (1-5 scale)
- **5**: Know/guess author fr
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7779
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-15T07:52:33.691635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-15T07:52:34.144772+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC, preliminary) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	For quality estimation, the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match), with ranking and classification favoring different signals across task complexity.
5	However, this strong estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---also fails to outperform greedy decoding on SciERC ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap}.
7	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-15T07:52:34.195532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-15T07:52:35.149483+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-15T07:52:35.250287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-15T07:52:35.552021+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-15T07:52:35.602777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-15T07:52:36.055044+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard, entity voting) and \textit{surface} (exact match, Fleiss' $\kappa$).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majo
…[truncated 4022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-15T07:52:36.055480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-15T07:52:36.507588+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.\textsuperscript{$
…[truncated 12480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-15T07:52:36.558220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-15T07:52:37.010364+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (structural):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (empirical):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the non-tied 40\%, logprob selection significantly outperforms greedy ($+2.9$~pp, $p{=}0.01$), confirming the signal carries useful information but is resolution-limited.
14	The common root is that quality estimation ranks \textit{instances}, while sample selection requires ranking \textit{candidates within a single instance}---a finer granularity that neither instance-level aggregation nor token-level confidence provides.
15	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (E
…[truncated 1117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-15T07:52:37.010834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-15T07:52:37.914663+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75).
6	Four of five signals are instance-level by construction and cannot rank candidates; log-probability, the only per-sample signal, also fails ($p{>}0.39$, 13--18~pp oracle headroom on SciERC), a disconnect we term the \textit{correlation-selection gap}.
7	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
8	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
9	
10	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
11	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-15T07:52:37.915184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-15T07:52:38.016011+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing 
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-15T07:52:38.068324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-15T07:52:38.370601+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 27104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-15T07:52:47.355846+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-15T07:52:47.406633+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-15T07:52:49.465320+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL fields, especially: (1) the exact scale and description for Soundness (1-5), (2) Excitement (1-5), (3) Overall Assessment (1-5), (4) Reproducibility (1-5), (5) Confidence (1-5). For each dimension, I need the exact text description for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL fields, especially: (1) the exact scale and description for Soundness (1-5), (2) Excitement (1-5), (3) Overall Assessment (1-5), (4) Reproducibility (1-5), (5) Confidence (1-5). For each dimension, I need the exact text description for each score level."
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-15T07:52:56.402297+00:00_

# ACL Rolling Review Form - Rating Scales

## 1. Soundness (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."
- **3**: "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."
- **2**: "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## 2. Excitement (1-5 scale)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."
- **3**: "Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others in the ACL community."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others..."

## 3. Overall Assessment (1-5 scale)
- **5**: Consider for Award
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 4. Reproducibility (1-5 scale)
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation..."
- **3**: "They could reproduce the results with some difficulty. The settings of parameters are underspecified..."
- **2**: "They would be hard pressed to reproduce the results..."
- **1**: "They would not be able to reproduce the results here no matter how hard they tried."

## 5. Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluat
…[truncated 484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6936
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-15T07:53:00.871979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-15T07:53:01.324532+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 21708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-15T07:53:01.375613+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-15T07:53:50.535549+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 58, \"total_citations\": 84, \"unique_cited_keys\": 58, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 52, \"online_not_found\": 2, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 46238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 49159
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-15T07:56:29.457993+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n\n---\n\n## 总体评分\n\n**Overall**: 3 / 5（Findings track acceptance）\n**一句话总结**: 研究问题定义清晰、实验设计总体扎实，\"correlation-selection gap\"是一个有实际意义的 negative result；但 constrained decoding 作为核心混淆变量未被充分隔离，削弱了中心结论的普适性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | Main claims 在实验范围内得到支持，但 constrained decoding confound 和 RE 单数据集问题构成方法论缺口 |\n| **Excitement** | 3.5 / 5 | Correlation-selection gap 概念新颖且对 test-time scaling 实践有指导意义；信号分类框架（per-sample vs instance-level）清晰有价值 |\n| **Reproducibility** | 4 / 5 | 训练配置完整（Appendix Table 8），prompt 提供，数据集公开；但未提及代码/数据发布计划 |\n| **Confidence** | 4 / 5 | 我仔细阅读了论文全文和附录，熟悉 self-consistency、MBR decoding 和 IE 领域 |\n\n---\n\n## 主要优势\n\n1. **问题定义清晰**。将 quality estimation 和 sample selection 解耦是重要的概念贡献（§1, §3.1）。per-sample vs instance-level 的区分框架简洁有力，解释了为什么 4/5 信号在 selection 上必然失败。\n\n2. **统计分析严谨**。Bootstrap CI (B=10,000)、TOST 等价检验（Table 6, Appendix D）、多种 δ 阈值（±2/3/5 pp）、sign test 和 Cohen's d 的联合报告（§4.3），统计方法论在 ACL 投稿中属于上乘。条件过滤分析（non-zero F1 subset, Figure 2 right panel）有效揭示了 full-set correlation 的虚高问题。\n\n3. **Negative result 有价值**。Log-probability 作为唯一 per-sample 信号也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 score compression（60% 的 instance 内 range < 0.05, Appendix F）——这是对 test-time scaling 文献（Brown et al. 2024; Snell et al. 2024）的重要补充。\n\n4. **Task-difficulty gradient 设计合理**。CoNLL（easy, ~91% F1）→ SciERC（hard, 6/7 types）→ WNUT-17（boundary, 52% zero F1）覆盖了有意义的难度谱，且 EM↔SJ crossover pattern 在两个模型上方向一致（§4.2, Table 1）。\n\n5. **引用完整**。58 条引用，0 orphan，0 missing bib entry，52 条在线验证通过。对最相关工作 Nédellec et al. (2026) 的定位精准（§1, §2），清楚说明了在哪三个维度上推进。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Constrained decoding 作为核心混淆变量未被隔离\n\n- 具体位置：§4.1 (Experimental Setup), §5 (Discussion), Limitations §第16行, Appendix F (logprob ties)\n- 问题：所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 constrained decoding \"may compress per-sample diversity\"（Limitations §16），且 Appendix F 显示 60% 的 instance logprob range < 0.05。但论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的人工产物。Constrained decoding 同时影响：(a) 输出多样性（diversity）；(b) logprob 分布（score compression）；(c) 信号之间的相对排序（因为所有输出都 schema-compliant，消除了 format error 这一重要变异来源）。\n- 为什么影响接收：这是论文核心结论 (\"signals are predictors not selectors for structured IE\") 的普适性基础。如果 gap 主要由 constrained decoding 驱动，则结论应改为 \"for structured IE *under constrained decoding*\"——scope 显著缩窄。论文目前的措辞（title, abstract, conclusion）未加此限定。\n- 建议修改方向：(1) 添加 free-form decoding 消融实验（即使在 SciERC subset 上），对比 logprob score resolution 和 selection gap 幅度；或 (2) 如果无法添加实验，在 title/abstract/conclusion 中明确限定 scope 为 constrained decoding setting，并在 Discussion 中深化分析（例如从 Appendix F 的 non-tied subset 结果反推：在 non-tied 40% 中 logprob selection 显著优于 greedy +2.9pp, p=0.01——这暗示 score compression 而非 IE 本身是 gap 的主因）。\n\n**N2** [critical] Appendix F 的 non-tied subset 结果实际上削弱了核心 claim\n\n- 具体位置：Appendix F (§F, line 396-397)\n- 问题：论文报告在 logprob range ≥ 0.05 的 non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01)，且 within-instance ρ(logprob, F1) 从 0.08 升到 0.39。论文将此解读为 \"signal exists but is resolution-limited\"。但更直接的解读是：**logprob 在有足够 score resolution 的情况下确实是有效 selector**，gap 的根因是 constrained decoding 导致的 score compression，而非 structured IE 的固有性质。\n- 这与 N1 构成同一个问题的两面：empirical evidence 在论文自身数据中已经暗示 constrained decoding 是主要 confound，但论文的 framing 仍然是 \"IE 本身的 gap\"。\n- 建议：重新组织 Discussion §5 的 \"Layer 2 (empirical)\" 分析，将 non-tied subset 结果提升为主文讨论（而非 appendix），明确承认这一反面证据对 claim scope 的影响。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] RE 结论仅基于 SciERC，但 abstract 和 contribution 列表未充分限定\n\n- 具体位置：Abstract line 3 (\"RE (SciERC, preliminary)\"), Introduction contribution 3 (line 47), Conclusion (line 8)\n- 问题：Abstract 用了 \"(SciERC, preliminary)\" 修饰 RE，但 Introduction 的 contribution 3 没有类似限定（\"When model capability is insufficient (WNUT-17, 52% zero F1), inflated full-set correlations collapse on the conditional set\"——RE 结论被嵌入通用表述中）。Conclusion line 8 提到 \"our RE conclusions rest on SciERC alone\"，但紧接的 future work 没有将 RE 验证列为优先方向。\n- SciERC RE 有 40% zero F1，这不是一般性 RE benchmark 的特征。\n- 建议：在 contribution 列表和 conclusion 中一致使用 \"preliminary\" 或 \"single-benchmark\" 限定词；在 future work 中明确列出 RE 多数据集验证。\n\n**W2** [warning] Fleiss' κ 的 independence 假设 justification 不够严格\n\n- 具体位置：§3.2, Eq. 3, line 39\n- 问题：论文用经验数据 (excess agreement -0.4% to -4.0%) 论证 temperature sampling 产生\"足够独立\"的样本。但这些数字没有对应的统计检验（e.g., permutation test for independence），也没有说明是在哪个 dataset/model 上测量的。\"mild negative dependence\" 的结论是否在所有 6 个 model-dataset 配置上一致成立？\n- Fleiss' κ 在 N 小（如 N=8）且 rater 非独立时行为不稳定（Gwet 2014），论文未引用相关分析。\n- 建议：(1) 提供所有配置的 excess agreement 数据；(2) 引用 FK 在非独立 rater 下的行为分析文献；(3) 或降低对 FK 结论的依赖程度（FK 在 5 个信号中排名靠后，不影响核心 claim）。\n\n**W3** [warning] \"Cross-architecture\" 结论的基础偏窄\n\n- 具体位置：§4.4 (Robustness), Table 3, Conclusion line 7\n- 问题：论文使用 \"cross-architecture\" 描述 Qwen3-8B vs LLaMA-3.1-8B 的比较。但两者均为 8B 参数量的 decoder-only transformer，共享极其相似的架构（grouped query attention, RoPE, SwiGLU）。更准确的说法是 \"cross-model-family at 8B scale\"。Conclusion 声称 signal ordering \"directionally consistent across model families, though magnitudes are model-dependent\"——这一结论在 2 个模型上成立但置信度有限。\n- 建议：将 \"cross-architecture\" 改为 \"cross-model\" 或 \"across two model families\"；在讨论 generalization 时明确 8B-only 的局限。\n\n**W4** [warning] TOST 等价检验的 δ 选择缺乏外部锚点\n\n- 具体位置：Appendix D (§D), Table 6, line 270-271\n- 问题：δ = ±2/3/5 pp 被描述为 \"practical significance\" 阈值，并与 \"typical inter-annotator disagreement on IE benchmarks\" 关联，但没有引用具体的 IAA 数据。对于 SciERC NER (greedy F1 ≈ 0.644)，2pp 对应 ~0.3% 的相对变化，这是极其严格的；对于 RE (greedy ≈ 0.404)，5pp 对应 ~1.2% 的相对变化。\n- 建议：引用 1-2 篇报告 IE benchmark IAA 数字的文献来锚定 δ 选择；或用 effect size (Cohen's d) 的 small/medium/large 分界作为补充。\n\n**W5** [warning] Qwen3-8B 的 thinking token 训练不一致\n\n- 具体位置：Appendix E (§E), footnote line 369\n- 问题：SciERC 训练 \"did not explicitly disable thinking tokens (enable_thinking)\"，而 CoNLL/WNUT \"explicitly set this to false\"。虽然推理时 constrained decoding 覆盖了 thinking behavior，但训练时的差异可能影响 learned representations。这意味着 SciERC vs CoNLL/WNUT 的比较中，Qwen 模型的训练条件不完全一致。\n- 建议：在 Limitations 中明确讨论此不一致性及其潜在影响，或确认 thinking tokens 在 SciERC fine-tuning 中实际是否被激活。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 脚注格式：`\\textsuperscript{†}` 和 `\\footnotetext` 在 two-column 模板中可能渲染异常（应检查 PDF 输出）。\n- **M2**: Appendix A (notation) 将 SJ 定义为 \"Soft Jaccard similarity\"，但 main text §3.2 标题是 \"Soft Jaccard (structural, instance-level)\"——首次出现时建议统一全称。\n- **M3**: §4.2 line 64 脚注中比较 semantic entropy AUROC 0.75-0.85，并声明 \"direct comparison is not meaningful\"。如果不 meaningful，这个数字引用的必要性存疑——建议删除或缩短。\n- **M4**: `he2024uncertainty` 的 bib entry 标题 \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\" 但 Related Work 引用上下文是 \"survey uncertainty quantification specifically for LLMs\"——内容可能不匹配（该论文实际是 sequential labeling 的，不是 LLM survey）。\n- **M5**: 引用验证发现 `hobelsberger2025systematic` 和 `lightman2024verify` 未在 OpenAlex 找到（可能索引延迟），`feng2025optimal` 和 `ye2025uncertainty` 有 first author name mismatch（bib vs API，可能是 name variant）——建议 double-check。\n\n---\n\n## Questions for Authors\n\n1. 在 Appendix F 的 non-tied subset (logprob range ≥ 0.05) 中，logprob selection 显著优于 greedy (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 的主因，那么在 free-form decoding 下，logprob 是否有可能成为有效 selector？你们如何论证 gap 是 IE-inherent 而非 decoding-induced？\n\n2. Consensus-proximity selection（§3.3）被描述为 \"mathematically equivalent to leave-one-out SJ selection\"，但未给出证明。能否补充简要推导？\n\n3. FK 的 excess agreement 数据 (-0.4% to -4.0%) 是在哪个配置上测量的？是否在所有配置上一致？\n\n4. 对于 WNUT-17 上 logprob 的负相关（ρ=-0.410），作者的解释是什么？是否与 constrained decoding 在 OOD 域上的行为有关？\n\n---\n\n## Missing References\n\n无明显遗漏。引用覆盖了 self-consistency (Wang et al. 2023)、MBR decoding (Eikema & Aziz 2022)、semantic uncertainty (Kuhn et al. 2023)、最近的 difficulty-aware 方法 (Feng et al. 2025; Wang & Feng et al. 2025) 和 IE-specific consistency (Nédellec et al. 2026)。可考虑补充：\n- Bertsch et al. (2023) \"Unlimiformer\" 或类似的 constrained generation 分析文献，以强化 constrained decoding confound 的讨论。\n\n---\n\n## Overall Assessment\n\n**评分: 3 / 5 (Findings track acceptance)**\n\n这是一篇执行质量较高的 empirical study，核心概念（correlation-selection gap）有实际指导价值，统计分析在 ACL 投稿中属上乘。主要弱点是 constrained decoding confound 未被隔离——论文自身的 non-tied subset 数据（Appendix F）实际暗示 gap 可能主要源于 decoding constraint 而非 IE task structure。如果作者能 (a) 添加 free-form decoding 消融或 (b) 在所有 claim 中限定 scope 为 constrained decoding setting 并提升 non-tied analysis 至主文，我认为此论文适合 Findings track。当前版本的 claim scope 与 evidence 之间存在 gap。\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n\n---\n\n## 总体评分\n\n**Overall**: 3 / 5（Findings track acceptance）\n**一句话总结**: 研究问题定义清晰、实验设计总体扎实，\"correlation-selection gap\"是一个有实际意义的 negative result；但 constrained decoding 作为核心混淆变量未被充分隔离，削弱了中心结论的普适性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | Main claims 在实验范围内得到支持，但 constrained decoding confound 和 RE 单数据集问题构成方法论缺口 |\n| **Excitement** | 3.5 / 5 | Correlation-selection gap 概念新颖且对 test-time scaling 实践有指导意义；信号分类框架（per-sample vs instance-level）清晰有价值 |\n| **Reproducibility** | 4 / 5 | 训练配置完整（Appendix Table 8），prompt 提供，数据集公开；但未提及代码/数据发布计划 |\n| **Confidence** | 4 / 5 | 我仔细阅读了论文全文和附录，熟悉 self-consistency、MBR decoding 和 IE 领域 |\n\n---\n\n## 主要优势\n\n1. **问题定义清晰**。将 quality estimation 和 sample selection 解耦是重要的概念贡献（§1, §3.1）。per-sample vs instance-level 的区分框架简洁有力，解释了为什么 4/5 信号在 selection 上必然失败。\n\n2. **统计分析严谨**。Bootstrap CI (B=10,000)、TOST 等价检验（Table 6, Appendix D）、多种 δ 阈值（±2/3/5 pp）、sign test 和 Cohen's d 的联合报告（§4.3），统计方法论在 ACL 投稿中属于上乘。条件过滤分析（non-zero F1 subset, Figure 2 right panel）有效揭示了 full-set correlation 的虚高问题。\n\n3. **Negative result 有价值**。Log-probability 作为唯一 per-sample 信号也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 score compression（60% 的 instance 内 range < 0.05, Appendix F）——这是对 test-time scaling 文献（Brown et al. 2024; Snell et al. 2024）的重要补充。\n\n4. **Task-difficulty gradient 设计合理**。CoNLL（easy, ~91% F1）→ SciERC（hard, 6/7 types）→ WNUT-17（boundary, 52% zero F1）覆盖了有意义的难度谱，且 EM↔SJ crossover pattern 在两个模型上方向一致（§4.2, Table 1）。\n\n5. **引用完整**。58 条引用，0 orphan，0 missing bib entry，52 条在线验证通过。对最相关工作 Nédellec et al. (2026) 的定位精准（§1, §2），清楚说明了在哪三个维度上推进。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Constrained decoding 作为核心混淆变量未被隔离\n\n- 具体位置：§4.1 (Experimental Setup), §5 (Discussion), Limitations §第16行, Appendix F (logprob ties)\n- 问题：所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 constrained decoding \"may compress per-sample diversity\"（Limitations §16），且 Appendix F 显示 60% 的 instance logprob range < 0.05。但论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的人工产物。Constrained decoding 同时影响：(a) 输出多样性（diversity）；(b) logprob 分布（score compression）；(c) 信号之间的相对排序（因为所有输出都 schema-compliant，消除了 format error 这一重要变异来源）。\n- 为什么影响接收：这是论文核心结论 (\"signals are predictors not selectors for structured IE\") 的普适性基础。如果 gap 主要由 constrained decoding 驱动，则结论应改为 \"for structured IE *under constrained decoding*\"——scope 显著缩窄。论文目前的措辞（title, abstract, conclusion）未加此限定。\n- 建议修改方向：(1) 添加 free-form decoding 消融实验（即使在 SciERC subset 上），对比 logprob score resolution 和 selection gap 幅度；或 (2) 如果无法添加实验，在 title/abstract/conclusion 中明确限定 scope 为 constrained decoding setting，并在 Discussion 中深化分析（例如从 Appendix F 的 non-tied subset 结果反推：在 non-tied 40% 中 logprob selection 显著优于 greedy +2.9pp, p=0.01——这暗示 score compression 而非 IE 本身是 gap 的主因）。\n\n**N2** [critical] Appendix F 的 non-tied subset 结果实际上削弱了核心 claim\n\n- 具体位置：Appendix F (§F, line 396-397)\n- 问题：论文报告在 logprob range ≥ 0.05 的 non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01)，且 within-instance ρ(logprob, F1) 从 0.08 升到 0.39。论文将此解读为 \"signal exists but is resolution-limited\"。但更直接的解读是：**logprob 在有足够 score resolution 的情况下确实是有效 selector**，gap 的根因是 constrained decoding 导致的 score compression，而非 structured IE 的固有性质。\n- 这与 N1 构成同一个问题的两面：empirical evidence 在论文自身数据中已经暗示 constrained decoding 是主要 confound，但论文的 framing 仍然是 \"IE 本身的 gap\"。\n- 建议：重新组织 Discussion §5 的 \"Layer 2 (empirical)\" 分析，将 non-tied subset 结果提升为主文讨论（而非 appendix），明确承认这一反面证据对 claim scope 的影响。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] RE 结论仅基于 SciERC，但 abstract 和 contribution 列表未充分限定\n\n- 具体位置：Abstract line 3 (\"RE (SciERC, preliminary)\"), Introduction contribution 3 (line 47), Conclusion (line 8)\n- 问题：Abstract 用了 \"(SciERC, preliminary)\" 修饰 RE，但 Introduction 的 contribution 3 没有类似限定（\"When model capability is insufficient (WNUT-17, 52% zero F1), inflated full-set correlations collapse on the conditional set\"——RE 结论被嵌入通用表述中）。Conclusion line 8 提到 \"our RE conclusions rest on SciERC alone\"，但紧接的 future work 没有将 RE 验证列为优先方向。\n- SciERC RE 有 40% zero F1，这不是一般性 RE benchmark 的特征。\n- 建议：在 contribution 列表和 conclusion 中一致使用 \"preliminary\" 或 \"single-benchmark\" 限定词；在 future work 中明确列出 RE 多数据集验证。\n\n**W2** [warning] Fleiss' κ 的 independence 假设 justification 不够严格\n\n- 具体位置：§3.2, Eq. 3, line 39\n- 问题：论文用经验数据 (excess agreement -0.4% to -4.0%) 论证 temperature sampling 产生\"足够独立\"的样本。但这些数字没有对应的统计检验（e.g., permutation test for independence），也没有说明是在哪个 dataset/model 上测量的。\"mild negative dependence\" 的结论是否在所有 6 个 model-dataset 配置上一致成立？\n- Fleiss' κ 在 N 小（如 N=8）且 rater 非独立时行为不稳定（Gwet 2014），论文未引用相关分析。\n- 建议：(1) 提供所有配置的 excess agreement 数据；(2) 引用 FK 在非独立 rater 下的行为分析文献；(3) 或降低对 FK 结论的依赖程度（FK 在 5 个信号中排名靠后，不影响核心 claim）。\n\n**W3** [warning] \"Cross-architecture\" 结论的基础偏窄\n\n- 具体位置：§4.4 (Robustness), Table 3, Conclusion line 7\n- 问题：论文使用 \"cross-architecture\" 描述 Qwen3-8B vs LLaMA-3.1-8B 的比较。但两者均为 8B 参数量的 decoder-only transformer，共享极其相似的架构（grouped query attention, RoPE, SwiGLU）。更准确的说法是 \"cross-model-family at 8B scale\"。Conclusion 声称 signal ordering \"directionally consistent across model families, though magnitudes are model-dependent\"——这一结论在 2 个模型上成立但置信度有限。\n- 建议：将 \"cross-architecture\" 改为 \"cross-model\" 或 \"across two model families\"；在讨论 generalization 时明确 8B-only 的局限。\n\n**W4** [warning] TOST 等价检验的 δ 选择缺乏外部锚点\n\n- 具体位置：Appendix D (§D), Table 6, line 270-271\n- 问题：δ = ±2/3/5 pp 被描述为 \"practical significance\" 阈值，并与 \"typical inter-annotator disagreement on IE benchmarks\" 关联，但没有引用具体的 IAA 数据。对于 SciERC NER (greedy F1 ≈ 0.644)，2pp 对应 ~0.3% 的相对变化，这是极其严格的；对于 RE (greedy ≈ 0.404)，5pp 对应 ~1.2% 的相对变化。\n- 建议：引用 1-2 篇报告 IE benchmark IAA 数字的文献来锚定 δ 选择；或用 effect size (Cohen's d) 的 small/medium/large 分界作为补充。\n\n**W5** [warning] Qwen3-8B 的 thinking token 训练不一致\n\n- 具体位置：Appendix E (§E), footnote line 369\n- 问题：SciERC 训练 \"did not explicitly disable thinking tokens (enable_thinking)\"，而 CoNLL/WNUT \"explicitly set this to false\"。虽然推理时 constrained decoding 覆盖了 thinking behavior，但训练时的差异可能影响 learned representations。这意味着 SciERC vs CoNLL/WNUT 的比较中，Qwen 模型的训练条件不完全一致。\n- 建议：在 Limitations 中明确讨论此不一致性及其潜在影响，或确认 thinking tokens 在 SciERC fine-tuning 中实际是否被激活。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 脚注格式：`\\textsuperscript{†}` 和 `\\footnotetext` 在 two-column 模板中可能渲染异常（应检查 PDF 输出）。\n- **M2**: Appendix A (notation) 将 SJ 定义为 \"Soft Jaccard similarity\"，但 main text §3.2 标题是 \"Soft Jaccard (structural, instance-level)\"——首次出现时建议统一全称。\n- **M3**: §4.2 line 64 脚注中比较 semantic entropy AUROC 0.75-0.85，并声明 \"direct comparison is not meaningful\"。如果不 meaningful，这个数字引用的必要性存疑——建议删除或缩短。\n- **M4**: `he2024uncertainty` 的 bib entry 标题 \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\" 但 Related Work 引用上下文是 \"survey uncertainty quantification specifically for LLMs\"——内容可能不匹配（该论文实际是 sequential labeling 的，不是 LLM survey）。\n- **M5**: 引用验证发现 `hobelsberger2025systematic` 和 `lightman2024verify` 未在 OpenAlex 找到（可能索引延迟），`feng2025optimal` 和 `ye2025uncertainty` 有 first author name mismatch（bib vs API，可能是 name variant）——建议 double-check。\n\n---\n\n## Questions for Authors\n\n1. 在 Appendix F 的 non-tied subset (logprob range ≥ 0.05) 中，logprob selection 显著优于 greedy (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 的主因，那么在 free-form decoding 下，logprob 是否有可能成为有效 selector？你们如何论证 gap 是 IE-inherent 而非 decoding-induced？\n\n2. Consensus-proximity selection（§3.3）被描述为 \"mathematically equivalent to leave-one-out SJ selection\"，但未给出证明。能否补充简要推导？\n\n3. FK 的 excess agreement 数据 (-0.4% to -4.0%) 是在哪个配置上测量的？是否在所有配置上一致？\n\n4. 对于 WNUT-17 上 logprob 的负相关（ρ=-0.410），作者的解释是什么？是否与 constrained decoding 在 OOD 域上的行为有关？\n\n---\n\n## Missing References\n\n无明显遗漏。引用覆盖了 self-consistency (Wang et al. 2023)、MBR decoding (Eikema & Aziz 2022)、semantic uncertainty (Kuhn et al. 2023)、最近的 difficulty-aware 方法 (Feng et al. 2025; Wang & Feng et al. 2025) 和 IE-specific consistency (Nédellec et al. 2026)。可考虑补充：\n- Bertsch et al. (2023) \"Unlimiformer\" 或类似的 constrained generation 分析文献，以强化 constrained decoding confound 的讨论。\n\n---\n\n## Overall Assessment\n\n**评分: 3 / 5 (Findings track acceptance)**\n\n这是一篇执行质量较高的 empirical study，核心概念（correlation-selection gap）有实际指导价值，统计分析在 ACL 投稿中属上乘。主要弱点是 constrained decoding confound 未被隔离——论文自身的 non-tied subset 数据（Appendix F）实际暗示 gap 可能主要源于 decoding constraint 而非 IE task structure。如果作者能 (a) 添加 free-form decoding 消融或 (b) 在所有 claim 中限定 scope 为 constrained decoding setting 并提升 non-tied analysis 至主文，我认为此论文适合 Findings track。当前版本的 claim scope 与 evidence 之间存在 gap。\n",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-15T07:56:34.604692+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5146
}
```

</details>

---


### Assistant

_source line 410 · 2026-05-15T07:56:44.792415+00:00_

审稿报告已提交给 Review Director。

**核心发现总结**：

- **Overall 3/5 (Findings acceptance)**，Soundness 3，Excitement 3.5
- **2 个 Critical 问题**：constrained decoding 作为核心混淆变量未被隔离——论文自身 Appendix F 的 non-tied subset 数据（logprob selection +2.9pp, p=0.01）反面证明了 gap 可能主要源于 score compression 而非 IE 本身的固有属性。当前 claim scope（title/abstract/conclusion）未限定 constrained decoding setting。
- **5 个 Should-Fix**：RE 单数据集限定不一致、FK independence justification 不足、"cross-architecture" 用词过度、TOST δ 缺外部锚点、thinking token 训练不一致
- **引用完整**，格式合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

10 recorded events


### User

_source line 411 · 2026-05-15T07:58:26.262696+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
 
---

### Reviewer 2 的 Must-Fix 问题

**R2-N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足
- 4/5 信号是 instance-level by definition，"selection failure" 是定义的逻辑后果而非实验发现。论文自己承认 "they cannot rank candidates by construction"（§4.3 L121, Discussion Layer 1）。
- 真正 non-trivial 的发现只有 logprob 的失败，但 Appendix F 已解释为 constrained decoding 的 score compression artifact。
- 因此 gap 被两头夹击：instance-level failure 是 tautological；logprob failure 是 artifact。
- 建议：区分 by-construction impossibility 和 empirical finding；将 C2 重心转向 logprob score compression 分析。

**R2-N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分
- 三个增量均偏弱：(i) SJ vs EM Δρ=+0.065 Bonferroni 后不显著；(ii) selection analysis 主要 tautological；(iii) difficulty gradient 发现直觉上不意外。
- 建议：更诚实地量化增量大小。

### Reviewer 2 的 Should-Fix 问题

**R2-W1** Abstract 信息密度过高（9 行含 5 signal/3 family/4 metric/3 dataset/2 model）
**R2-W2** RE "preliminary" 标注与实际使用不一致（在 Table 1/2/Figure 2-3/Discussion 大量引用）
**R2-W3** Soft Jaccard 方法论新颖性有限（Hungarian + token IoU 均为标准技术）
**R2-W4** "first multi-family comparison" claim 过度依赖 scope 限定

### Reviewer 2 的 Minor 问题

- 术语不一致（"Voting Conf." vs "VC"）
- Ethics Statement 过简
- 部分 bib entries 未在 OpenAlex 找到
- Figure 1 caption 引用 Table 2
- Table 1 脚注格式问题

### Reviewer 2 的 Missing References

1. "Trust but Verify! A Survey on Verification Design for Test-time Scaling" (2025)
2. 最新 UQ survey (arXiv:2503.15850)
3. SLOT (EMNLP 2025 Industry)
4. MBR 在非 MT 任务中的应用

### Reviewer 2 评分
Overall 3.0/5, Soundness 3.5, Excitement 2.5, Reproducibility 4, Confidence 4

---

请对以上每个 N/W/M 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-15T07:58:34.740350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "offset": "36",
  "limit": "13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "offset": "36",
    "limit": "13"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-15T07:58:35.192775+00:00_

36	\begin{enumerate}
37	    \item \textbf{A systematic multi-family comparison of confidence signals for generative IE.}
38	    We evaluate five signals from three families on quality estimation for NER and RE.
39	    Entity voting achieves the strongest $\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL)---an ordering directionally consistent across model families, though with model-dependent magnitude.
40	
41	    \item \textbf{Identification of the correlation-selection gap.}
42	    Four of five signals are instance-level by construction, making selection failure expected; the empirical finding is that log-probability---the only per-sample signal---also fails ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom on SciERC, where output diversity is substantial (39--43\% unique outputs).
43	    We trace this to the instance-level nature of consistency signals and, for log-probability, to within-instance score compression under constrained decoding.
44	
45	    \item \textbf{Task-complexity boundary conditions.}
46	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 52\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.
47	    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.
48	\end{enumerate}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-15T07:58:35.645211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "119",
  "limit": "22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "119",
    "limit": "22"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-15T07:58:35.952052+00:00_

119	
120	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
121	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
122	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
123	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
124	
125	\paragraph{No significant improvement over greedy.}
126	We exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.
127	We evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\% percentile CIs.
128	The three random seeds (42, 123, 456) refer to independent inference runs; we average $\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\ greedy).
129	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
130	Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\%${=}$46.6\%).
131	On RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
132	TOST equivalence testing confirms that most signals are statistically indistinguishable from greedy: on NER, SJ and logprob are equivalent within ${\pm}2$~pp; on RE, EM and Voting fail equivalence even at ${\pm}5$~pp due to 
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 306
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-15T07:58:35.952550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-15T07:58:36.053277+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC, preliminary) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	For quality estimation, the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match), with ranking and classification favoring different signals across task complexity.
5	However, this strong estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---also fails to outperform greedy decoding on SciERC ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap}.
7	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-15T07:59:46.145371+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[REBUT] R2-N1: Correlation-selection gap 的 tautological 成分与新颖性**\n\nR2 认为 gap 被\"两头夹击\"——instance-level failure 是 tautological，logprob failure 是 artifact——因此整个 contribution 空心化。我部分同意但认为 R2 低估了三个方面：\n\n1. **论文已经做了 R2 建议的区分**。Introduction Contribution 2（§1, line 41-43）明确写道 \"Four of five signals are instance-level by construction, **making selection failure expected**; the empirical finding is that log-probability...also fails\"。Discussion §5 的 \"two layers\" 结构也做了清晰分层。R2 建议的 \"区分 by-construction impossibility 和 empirical finding\" 实际上已经在论文中实现了。\n\n2. **Consensus-proximity strategy 的失败不是 tautological**。Instance-level 信号确实不能直接 rank candidates，但论文设计了 consensus-proximity selection（§3.3, line 70）——选择最接近 consensus 的 sample——这是一个合理的 bridge，且被证明 \"mathematically equivalent to leave-one-out SJ selection\"。该策略的失败是实验结果（Table 2: SJ selection 0.645 vs greedy 0.644 on NER），不是定义推导。MBR decoding 在 MT 中成功正是因为类似的 utility-based selection work（Freitag et al. 2022）；在 IE 中失败并非 a priori obvious。\n\n3. **但我同意 logprob failure 的 artifact 问题是 real concern**。这与我的 R1-N1 和 R1-N2 一致：Appendix F 的 non-tied subset (+2.9pp, p=0.01) 暗示 constrained decoding score compression 是主因。论文需要要么添加 free-form 消融，要么在 claim scope 上加限定。\n\n**总体判断**：R2 的 tautological 批评部分有理（论文确实需要更加突出 logprob 分析的独立价值），但 \"entirely tautological\" 过强——consensus-proximity failure 和 MBR 在 IE 中的失败是 non-trivial 的实验发现。建议论文 reframe C2 以 logprob + MBR failure 为中心，而非以 \"5 signals all fail\" 为叙事。\n\n---\n\n**[REBUT] R2-N2: 与 Nédellec et al. (2026) 的增量贡献不足**\n\nR2 批评三个增量均偏弱。我逐一评估：\n\n(i) **SJ vs EM Δρ=+0.065 Bonferroni 后不显著**——事实正确（Table 5, Appendix B: \"Marginally significant without multiple comparison correction; would not survive Bonferroni correction\"）。但论文的核心 claim 不是 \"SJ > EM\"，而是 signal ranking 随 task difficulty 变化的 crossover pattern（SJ > EM on SciERC, EM > SJ on CoNLL），且这一 pattern 在两个模型上一致。单个 Δρ 的显著性不是 claim 的支点。\n\n(ii) **Selection analysis 主要 tautological**——见上文 R2-N1 回应，部分同意但不完全。\n\n(iii) **Difficulty gradient 发现直觉上不意外**——不同意。\"Easy task favors exact match, hard task favors structural signals\" 听起来直觉合理，但事后合理化 (hindsight bias) 不等于事前可预测。更重要的是，WNUT-17 的 conditional collapse（full-set ρ=0.724 → conditional ρ=0.038, Table 4）和 logprob negative correlation (ρ=-0.410) 不是直觉可预测的结果。\n\n**总体判断**：相比 Nédellec et al. (2026) 的增量确实不是 ground-breaking，但对 Findings track 而言足够。R2 的 Excitement 评分 2.5 反映了这一判断，我理解但不完全赞同——将其定为 3.0 更合理，因为 quality estimation ≠ selection 的解耦框架对后续研究有实际指导价值。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。Abstract 9 行包含 5 个信号名、3 个 family、4 种 metric (ρ/AUROC/p-value/oracle headroom)、3 个数据集、2 个模型。对非 IE 专家读者构成认知负荷。建议将 Abstract 聚焦于核心 claim（gap 存在 + difficulty-dependent ranking），具体数字移入正文。\n\n---\n\n**[AGREE] R2-W2: RE \"preliminary\" 标注与实际使用不一致**\n\n完全同意，这也是我在 R1-W1 中提出的问题。Abstract 标注 \"(SciERC, preliminary)\" 但论文后续在 Table 1（4 列中有 2 列是 RE）、Table 2、Figure 2-3、Discussion 中大量引用 RE 结果，无 \"preliminary\" 限定。要么减少 RE 结果的篇幅权重，要么在所有 RE 分析处一致标注为 single-benchmark preliminary results。\n\n---\n\n**[REBUT] R2-W3: Soft Jaccard 方法论新颖性有限**\n\nR2 称 Hungarian matching + token IoU \"均为标准技术\"。技术上正确，但忽略了 application novelty：将 type-aware bipartite matching 应用于 LLM 生成的 entity set 之间的 partial overlap 度量，在 IE quality estimation 文献中（据我所知）是新的。Nédellec et al. (2026) 明确承认他们的 surface-level approach \"overlooks semantically consistent outputs\"（§1, line 16 引用）。论文没有 claim SJ 本身是新方法——而是 claim 这种组合在 IE confidence estimation 中填补了 structural matching 的空白。这一定位是准确的。\n\n不过我同意论文不应对此过度宣传——当前措辞 \"Our core structural signal extends Jaccard similarity\"（§3.2, line 43）中 \"core\" 一词可能暗示过高的方法贡献，可弱化为 \"primary structural signal\"。\n\n---\n\n**[AGREE] R2-W4: \"first multi-family comparison\" claim 过度依赖 scope 限定**\n\n同意。Introduction line 17 \"No existing work compares confidence signals from multiple families...for both quality estimation and sample selection in generative structured IE\" 通过堆叠修饰词 (multiple families + both objectives + generative + structured IE) 来确保 \"first\" 成立。虽然事实上可能正确，但这种 contribution framing 给读者的印象是在通过 scope engineering 制造新颖性。建议改为描述性表述，避免 \"first\" claim。\n\n---\n\n## Minor 问题\n\n**[AGREE] R2-M (术语不一致)**：Table 1 用 \"Voting Conf.\"，Table 5 和 Table 7 用 \"VC\"，正文又用 \"entity voting\"。应统一。\n\n**[AGREE] R2-M (Ethics Statement 过简)**：当前 Ethics Statement 仅 2 行，但对 Findings track 基本够用。如果 reviewer 要求可适当补充 computational cost 或 environmental impact。\n\n**[AGREE] R2-M (部分 bib entries 未在 OpenAlex 找到)**：我的引用验证也发现 `hobelsberger2025systematic` 和 `lightman2024verify` 未在 OpenAlex 找到，但这两篇是真实论文（前者 arXiv:2510.20460，后者 arXiv:2305.20050），应为索引延迟而非 fabrication。\n\n**[AGREE] R2-M (Figure 1 caption 引用 Table 2)**：Figure 1 caption（§1, line 29）确实引用 \"Table~\\ref{tab:selection}\" 即 Table 2——这是 forward reference，虽然不违规但在排版上不理想。\n\n**[AGREE] R2-M (Table 1 脚注格式)**：与我的 R1-M1 一致。\n\n---\n\n## Missing References\n\n**[AGREE] \"Trust but Verify!\" survey (2025)**：与论文讨论的 test-time scaling + verification 直接相关，应引用。\n\n**[AGREE] 最新 UQ survey (arXiv:2503.15850)**：如果 R2 能确认具体论文，Related Work §3 的 survey 引用集合可以补充。\n\n**[REBUT] SLOT (EMNLP 2025 Industry)**：R2 未说明 SLOT 与本文的具体关联。如果是 structured output 相关的 test-time 方法，相关性取决于其是否处理 set-valued IE output。在了解具体内容前不确定是否属于 missing reference。\n\n**[AGREE] MBR 在非 MT 任务中的应用**：论文 Discussion §5 将其方法与 MBR 对接（Eikema & Aziz 2022; Freitag et al. 2022; Müller & Sennrich 2021），但只引用了 MT 领域的 MBR 工作。如果存在 MBR 在 summarization/QA 等任务中的应用文献，应补充以增强对比分析。\n\n---\n\n## 对 R2 整体评分的看法\n\nR2 给出 Overall 3.0, Excitement 2.5。我认为 Excitement 2.5 偏低——quality estimation vs selection 的解耦概念和 difficulty-dependent signal ranking 对 practitioners 有实际价值，3.0-3.5 更合理。但 Soundness 3.5 vs 我的 3.0 差异主要来自我对 constrained decoding confound 的更重权重——R2 虽然提到了这一问题（在 N1 的 \"artifact\" 论述中），但没有像我一样将其列为独立的 must-fix。我认为 constrained decoding confound 应该是独立的 critical issue，而非仅作为 N1 tautological argument 的一部分。\n\n**我维持我的 Overall 3.0 评分不变。**\n",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[REBUT] R2-N1: Correlation-selection gap 的 tautological 成分与新颖性**\n\nR2 认为 gap 被\"两头夹击\"——instance-level failure 是 tautological，logprob failure 是 artifact——因此整个 contribution 空心化。我部分同意但认为 R2 低估了三个方面：\n\n1. **论文已经做了 R2 建议的区分**。Introduction Contribution 2（§1, line 41-43）明确写道 \"Four of five signals are instance-level by construction, **making selection failure expected**; the empirical finding is that log-probability...also fails\"。Discussion §5 的 \"two layers\" 结构也做了清晰分层。R2 建议的 \"区分 by-construction impossibility 和 empirical finding\" 实际上已经在论文中实现了。\n\n2. **Consensus-proximity strategy 的失败不是 tautological**。Instance-level 信号确实不能直接 rank candidates，但论文设计了 consensus-proximity selection（§3.3, line 70）——选择最接近 consensus 的 sample——这是一个合理的 bridge，且被证明 \"mathematically equivalent to leave-one-out SJ selection\"。该策略的失败是实验结果（Table 2: SJ selection 0.645 vs greedy 0.644 on NER），不是定义推导。MBR decoding 在 MT 中成功正是因为类似的 utility-based selection work（Freitag et al. 2022）；在 IE 中失败并非 a priori obvious。\n\n3. **但我同意 logprob failure 的 artifact 问题是 real concern**。这与我的 R1-N1 和 R1-N2 一致：Appendix F 的 non-tied subset (+2.9pp, p=0.01) 暗示 constrained decoding score compression 是主因。论文需要要么添加 free-form 消融，要么在 claim scope 上加限定。\n\n**总体判断**：R2 的 tautological 批评部分有理（论文确实需要更加突出 logprob 分析的独立价值），但 \"entirely tautological\" 过强——consensus-proximity failure 和 MBR 在 IE 中的失败是 non-trivial 的实验发现。建议论文 reframe C2 以 logprob + MBR failure 为中心，而非以 \"5 signals all fail\" 为叙事。\n\n---\n\n**[REBUT] R2-N2: 与 Nédellec et al. (2026) 的增量贡献不足**\n\nR2 批评三个增量均偏弱。我逐一评估：\n\n(i) **SJ vs EM Δρ=+0.065 Bonferroni 后不显著**——事实正确（Table 5, Appendix B: \"Marginally significant without multiple comparison correction; would not survive Bonferroni correction\"）。但论文的核心 claim 不是 \"SJ > EM\"，而是 signal ranking 随 task difficulty 变化的 crossover pattern（SJ > EM on SciERC, EM > SJ on CoNLL），且这一 pattern 在两个模型上一致。单个 Δρ 的显著性不是 claim 的支点。\n\n(ii) **Selection analysis 主要 tautological**——见上文 R2-N1 回应，部分同意但不完全。\n\n(iii) **Difficulty gradient 发现直觉上不意外**——不同意。\"Easy task favors exact match, hard task favors structural signals\" 听起来直觉合理，但事后合理化 (hindsight bias) 不等于事前可预测。更重要的是，WNUT-17 的 conditional collapse（full-set ρ=0.724 → conditional ρ=0.038, Table 4）和 logprob negative correlation (ρ=-0.410) 不是直觉可预测的结果。\n\n**总体判断**：相比 Nédellec et al. (2026) 的增量确实不是 ground-breaking，但对 Findings track 而言足够。R2 的 Excitement 评分 2.5 反映了这一判断，我理解但不完全赞同——将其定为 3.0 更合理，因为 quality estimation ≠ selection 的解耦框架对后续研究有实际指导价值。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。Abstract 9 行包含 5 个信号名、3 个 family、4 种 metric (ρ/AUROC/p-value/oracle headroom)、3 个数据集、2 个模型。对非 IE 专家读者构成认知负荷。建议将 Abstract 聚焦于核心 claim（gap 存在 + difficulty-dependent ranking），具体数字移入正文。\n\n---\n\n**[AGREE] R2-W2: RE \"preliminary\" 标注与实际使用不一致**\n\n完全同意，这也是我在 R1-W1 中提出的问题。Abstract 标注 \"(SciERC, preliminary)\" 但论文后续在 Table 1（4 列中有 2 列是 RE）、Table 2、Figure 2-3、Discussion 中大量引用 RE 结果，无 \"preliminary\" 限定。要么减少 RE 结果的篇幅权重，要么在所有 RE 分析处一致标注为 single-benchmark preliminary results。\n\n---\n\n**[REBUT] R2-W3: Soft Jaccard 方法论新颖性有限**\n\nR2 称 Hungarian matching + token IoU \"均为标准技术\"。技术上正确，但忽略了 application novelty：将 type-aware bipartite matching 应用于 LLM 生成的 entity set 之间的 partial overlap 度量，在 IE quality estimation 文献中（据我所知）是新的。Nédellec et al. (2026) 明确承认他们的 surface-level approach \"overlooks semantically consistent outputs\"（§1, line 16 引用）。论文没有 claim SJ 本身是新方法——而是 claim 这种组合在 IE confidence estimation 中填补了 structural matching 的空白。这一定位是准确的。\n\n不过我同意论文不应对此过度宣传——当前措辞 \"Our core structural signal extends Jaccard similarity\"（§3.2, line 43）中 \"core\" 一词可能暗示过高的方法贡献，可弱化为 \"primary structural signal\"。\n\n---\n\n**[AGREE] R2-W4: \"first multi-family comparison\" claim 过度依赖 scope 限定**\n\n同意。Introduction line 17 \"No existing work compares confidence signals from multiple families...for both quality estimation and sample selection in generative structured IE\" 通过堆叠修饰词 (multiple families + both objectives + generative + structured IE) 来确保 \"first\" 成立。虽然事实上可能正确，但这种 contribution framing 给读者的印象是在通过 scope engineering 制造新颖性。建议改为描述性表述，避免 \"first\" claim。\n\n---\n\n## Minor 问题\n\n**[AGREE] R2-M (术语不一致)**：Table 1 用 \"Voting Conf.\"，Table 5 和 Table 7 用 \"VC\"，正文又用 \"entity voting\"。应统一。\n\n**[AGREE] R2-M (Ethics Statement 过简)**：当前 Ethics Statement 仅 2 行，但对 Findings track 基本够用。如果 reviewer 要求可适当补充 computational cost 或 environmental impact。\n\n**[AGREE] R2-M (部分 bib entries 未在 OpenAlex 找到)**：我的引用验证也发现 `hobelsberger2025systematic` 和 `lightman2024verify` 未在 OpenAlex 找到，但这两篇是真实论文（前者 arXiv:2510.20460，后者 arXiv:2305.20050），应为索引延迟而非 fabrication。\n\n**[AGREE] R2-M (Figure 1 caption 引用 Table 2)**：Figure 1 caption（§1, line 29）确实引用 \"Table~\\ref{tab:selection}\" 即 Table 2——这是 forward reference，虽然不违规但在排版上不理想。\n\n**[AGREE] R2-M (Table 1 脚注格式)**：与我的 R1-M1 一致。\n\n---\n\n## Missing References\n\n**[AGREE] \"Trust but Verify!\" survey (2025)**：与论文讨论的 test-time scaling + verification 直接相关，应引用。\n\n**[AGREE] 最新 UQ survey (arXiv:2503.15850)**：如果 R2 能确认具体论文，Related Work §3 的 survey 引用集合可以补充。\n\n**[REBUT] SLOT (EMNLP 2025 Industry)**：R2 未说明 SLOT 与本文的具体关联。如果是 structured output 相关的 test-time 方法，相关性取决于其是否处理 set-valued IE output。在了解具体内容前不确定是否属于 missing reference。\n\n**[AGREE] MBR 在非 MT 任务中的应用**：论文 Discussion §5 将其方法与 MBR 对接（Eikema & Aziz 2022; Freitag et al. 2022; Müller & Sennrich 2021），但只引用了 MT 领域的 MBR 工作。如果存在 MBR 在 summarization/QA 等任务中的应用文献，应补充以增强对比分析。\n\n---\n\n## 对 R2 整体评分的看法\n\nR2 给出 Overall 3.0, Excitement 2.5。我认为 Excitement 2.5 偏低——quality estimation vs selection 的解耦概念和 difficulty-dependent signal ranking 对 practitioners 有实际价值，3.0-3.5 更合理。但 Soundness 3.5 vs 我的 3.0 差异主要来自我对 constrained decoding confound 的更重权重——R2 虽然提到了这一问题（在 N1 的 \"artifact\" 论述中），但没有像我一样将其列为独立的 must-fix。我认为 constrained decoding confound 应该是独立的 critical issue，而非仅作为 N1 tautological argument 的一部分。\n\n**我维持我的 Overall 3.0 评分不变。**\n",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-15T07:59:50.272510+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4127
}
```

</details>

---


### Assistant

_source line 420 · 2026-05-15T08:00:00.934161+00:00_

交叉回应已提交给 Review Director。逐条回应了 R2 的 2 个 Must-Fix、4 个 Should-Fix、5 个 Minor 和 4 个 Missing Reference，其中：

- **REBUT** 3 条（R2-N1 tautological 批评过强、R2-N2 增量贡献 Findings-worthy、R2-W3 SJ 有 application novelty）
- **AGREE** 10 条（abstract 过密、RE preliminary 不一致、"first" claim、术语不一致、大部分 minor 和 missing references）
- 维持 Overall 3.0 评分不变，认为 R2 的 Excitement 2.5 偏低但 Soundness 3.5 偏高（我因 constrained decoding confound 给了 3.0）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

70 recorded events


### User

_source line 421 · 2026-05-15T08:45:55.172452+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计**

### 论文信息
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `sections/` 子目录）
- **目标 venue**: EMNLP 2026 Findings
- **截止日期**: 2026-05-25
- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）
- **模板**: ACL style files（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind

### 论文概要
标题：Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding

研究在 constrained decoding 下，5 种 confidence signals（VC, SJ, FK, EM, logprob）对 structured IE（NER + RE）的 quality estimation 和 sample selection 效果。核心发现：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75）但无法做 sample selection（correlation-selection gap）。

### 你需要重点审查
1. **统计方法严谨性**：bootstrap resampling 设计、TOST 等价检验的 δ 选择是否有据、p 值解读是否准确
2. **实验设计 confounds**：constrained decoding 是否是 gap 的 confounding variable（论文已有 non-tied subset 分析，但是否充分）；Qwen3 thinking token 训练不一致是否影响结论
3. **Claim-evidence 匹配**：核心 claim（gap 存在且有实际意义）与 evidence 是否匹配；instance-level 信号无法 select 是否 tautological；logprob 失败是否仅因 score compression
4. **RE 证据强度**：单数据集（SciERC）RE 结论的可信度
5. **信号定义数学正确性**：SJ 的 Hungarian matching、VC 的 frequency 定义、FK 的 adaptation 是否正确
6. **格式合规**：页数是否超限、ACL 模板使用是否正确

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-15T08:46:02.149785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-15T08:46:02.200851+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-15T08:46:06.174272+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-15T08:46:06.325668+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-15T08:46:08.736340+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-15T08:46:08.736782+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-15T08:46:11.459796+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-15T08:46:11.560678+00:00_

/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md
/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-experiment-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md
/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md
/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md
/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md
/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md
/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md
/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md
/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md
/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md
/home/ubuntu/agent-ml-research/skills/global/framing-reaudit.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md
/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md
/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md
/home/ubuntu/agent-ml-research/skills/global/mvp-validation.skill.md
/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-datagen-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/negative-framing-review.skill.md
…[truncated 3626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-15T08:46:14.271041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-15T08:46:14.271764+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-15T08:46:21.404828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-15T08:46:21.706666+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
43	
44	\bibliography{references}
45	
46	\appendix
47	\input{sections/appendix}
48	
49	\end{document}
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-15T08:46:22.158826+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-15T08:46:23.364700+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-15T08:46:23.415424+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-15T08:46:23.465994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-15T08:46:27.631947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-15T08:46:28.133990+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction (IE), but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	Under constrained decoding---the standard inference regime for schema-compliant IE---we compare five signals from three families (structural, surface, model-internal) across NER (three datasets) and RE (SciERC, preliminary) with two 8B-parameter model families.
4	For quality estimation, the strongest signals achieve Spearman $\rho{=}0.38$ and AUROC${=}0.75$, with ranking and classification favoring different signals depending on task complexity.
5	However, this estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---fails to outperform greedy decoding ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap} and diagnose its mechanism: log-probability scores are severely compressed under constrained decoding, but in the 40\% of instances where compression is mitigated, log-probability becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	Signal rankings further depend on task difficulty, with consistent ordering across models but model-dependent magnitude.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE under constrained decoding.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-15T08:46:28.134388+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-15T08:46:28.636401+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 5169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-15T08:46:28.636884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-15T08:46:29.089417+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 2752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-15T08:46:29.089886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-15T08:46:29.545022+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 4314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-15T08:46:29.545542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-15T08:46:29.997750+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$. $N{=}16$ results (LLaMA CoNLL only; 3-
…[truncated 11185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-15T08:46:29.998113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-15T08:46:30.952382+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (logprob range ${\geq}0.05$, $n{=}210$), logprob \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that logprob carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	Diversity-stratified analysis confirms the gap persists even amon
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-15T08:46:31.003653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-15T08:46:31.556277+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	Four of five signals are instance-level by construction; log-probability also fails ($p{>}0.39$) despite 13--18~pp oracle headroom.
5	Mechanistic diagnosis identifies logprob score compression as the bottleneck: where compression is mitigated, logprob becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone and warrant multi-benchmark validation.
8	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-15T08:46:31.607000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-15T08:46:31.908714+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing 
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-15T08:46:31.909358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-15T08:46:32.362269+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 27696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-15T08:46:32.362768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2026 reviewer guidelines scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2026 reviewer guidelines scoring dimensions"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-15T08:46:38.542054+00:00_

Web search results for query: "ACL ARR review form criteria 2026 reviewer guidelines scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"}]

I've found comprehensive information about the ACL ARR review form criteria and reviewer guidelines for 2026. Here are the key details:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to 
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6179
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-15T08:46:44.218906+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or whatever), and the description for each score level. I need the exact criteria for Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or whatever), and the description for each score level. I need the exact criteria for Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-15T08:46:45.424567+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should focus on, scoring criteria, what constitutes a good review, and any specific instructions about soundness, excitement, reproducibility, and paper evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should focus on, scoring criteria, what constitutes a good review, and any specific instructions about soundness, excitement, reproducibility, and paper evaluation."
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-15T08:46:51.911464+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely to have missed something affecting ratings
- **3**: Pretty sure; may have missed details or didn't carefully verify math/experiments
- **2**: Can defend evaluation, but fairly likely to have missed details or novelty assessment
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness
Scale: 1-5 (increments of 0.5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong study with sufficient support; extra experiments optional
- **3**: Acceptable; main claims supported but minor points need details
- **2**: Poor; major claims lack support or have technical/methodological problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement
Scale: 1-5 (increments of 0.5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: Exciting; would mention to others or attend presentation
- **3**: Interesting; might mention points or attend if time permits
- **2**: Potentially interesting to others despite limited personal resonance
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
Scale: 1-5 (increments of 0.5)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce 
…[truncated 291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7692
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-15T08:46:57.185024+00:00_

# ARR Reviewer Guidelines Summary

## Core Reviewer Responsibilities

Reviewers must complete four main tasks: allocate calendar time, check assignments for expertise and conflicts, write strong reviews, and update assessments after author responses.

## Scoring Criteria (As of February 2025)

ARR uses three distinct scores:

1. **Soundness**: Must be justified by review text. Low scores require substantive technical concerns, not subjective preferences.

2. **Excitement**: Reflects personal interest, orthogonal to soundness. Subjective taste doesn't require explicit justification.

3. **Overall Assessment**: A composite recommendation considering soundness, excitement, novelty, and potential impact for target communities.

## What Makes a Strong Review

**Specificity is essential.** Reviews should identify concrete issues: instead of "missing relevant references," cite which works (e.g., "XYZ"); rather than "X is unclear," specify what details are absent.

**Read twice with adjusted expectations**: Skim first to understand research questions and scope, then read in-depth to evaluate evidence. Avoid hindsight bias and confirmation bias by postponing assumptions about methodology until after initial impressions form.

**Professional tone matters.** Reviews should be collegial and constructive, recognizing that authors may be early-career researchers. "Write the review you would like to get yourself."

## Common Review Mistakes to Avoid

The guidelines identify 17 heuristics that often reflect reviewer bias rather than paper weakness:

- Dismissing results as "obvious" or "unsurprising" (H1)
- Requiring SOTA results when papers make other contributions (H5)
- Criticizing negative results (H6)
- Preferring complexity over simplicity (H7)
- Demanding experiments beyond the paper's stated claims (H13)

## Common NLP Paper Problems to Flag

Reviewers should watch for methodology issues (M1-M5), artifact sourcing concerns (T1-T2), experimental problems (R1-R5), and general
…[truncated 1472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11760
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-15T08:47:07.945814+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-15T08:47:09.007570+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-15T08:47:09.360096+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-15T08:48:01.971748+00:00_

&lt;persisted-output>
Output too large (49.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/fbe93399-4ce3-4dd3-bca3-4fa43058eafb/tool-results/toolu_01EuHRGcPf576KjwqZh9xWuM.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 91, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 54025
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-15T08:48:01.972293+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52964
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-15T08:48:02.022773+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52662
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-15T08:48:05.939465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/fbe93399-4ce3-4dd3-bca3-4fa43058eafb/tool-results/toolu_01EuHRGcPf576KjwqZh9xWuM.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/fbe93399-4ce3-4dd3-bca3-4fa43058eafb/tool-results/toolu_01EuHRGcPf576KjwqZh9xWuM.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-15T08:48:06.446900+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 91, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogni
…[truncated 48404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-15T08:48:06.599307+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-4",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-4",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-15T08:48:08.221328+00:00_

Error: result (2,681,903 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/fbe93399-4ce3-4dd3-bca3-4fa43058eafb/tool-results/mcp-agent-ml-research-pdf_to_images-1778834888072.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/fbe93399-4ce3-4dd3-bca3-4fa43058eafb/tool-results/mcp-agent-ml-research-pdf_to_images-1778834888072.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/fbe93399-4ce3-4dd3-bca3-4fa43058eafb/tool-results/mcp-agent-ml-research-pdf_to_images-1778834888072.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1622
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-15T08:48:23.484981+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || python3 -c \"\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf')\n    print(f'Pages: {doc.page_count}')\n    doc.close()\nexcept ImportError:\n    import subprocess\n    r = subprocess.run(['strings', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\n    # Count /Page objects\n    pages = r.stdout.count('/Type /Page')\n    print(f'Approximate pages (from /Page count): {pages}')\n\"\n",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || python3 -c \"\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf')\n    print(f'Pages: {doc.page_count}')\n    doc.close()\nexcept ImportError:\n    import subprocess\n    r = subprocess.run(['strings', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\n    # Count /Page objects\n    pages = r.stdout.count('/Type /Page')\n    print(f'Approximate pages (from /Page count): {pages}')\n\"\n",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-15T08:48:23.938636+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 15 08:38:59 2026 UTC
ModDate:         Fri May 15 08:38:59 2026 UTC
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
File size:       569622 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-15T08:48:23.939082+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/_pdf_images/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/_pdf_images/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-15T08:48:23.989572+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-15T08:48:30.866707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-15T08:48:31.420021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-15T08:48:31.824056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 479 · 2026-05-15T08:48:32.075374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 480 · 2026-05-15T08:48:32.277338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-15T08:48:32.729934+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-15T08:48:40.411307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-15T08:48:41.069177+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-15T08:48:41.069600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-15T08:48:41.471335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-15T08:48:42.028095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-15T08:48:42.833017+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-15T08:51:55.011456+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n**Overall**: 3.0/5（Findings acceptance）\n**一句话总结**: 方法论扎实、统计实践规范的实证研究，但核心发现（correlation-selection gap）大部分可归因于 constrained decoding 的技术 artifact 而非 structured IE 的基本属性，加上 RE 仅单数据集、Qwen3 thinking token confound 未充分控制，限制了贡献的深度和普适性。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心 claim 有合理支撑，bootstrap 和 TOST 设计规范，但缺少 free-form decoding 对照实验是显著缺口；TOST δ 选择的理据间接 |\n| Excitement | 3.0/5 | Quality estimation vs. sample selection 的区分有价值，但 4/5 信号 instance-level 不能 select 在定义上即成立，logprob 失败归因于 score compression 是 constrained decoding 的特有问题，非通用发现 |\n| Overall | 3.0/5 | 适合 Findings：实证全面、写作清晰、局限性坦诚，但贡献增量性偏强 |\n| Reproducibility | 4/5 | 训练超参、数据集 split、prompt 模板、推理配置均有详细记录（Appendix E），代码未共享是唯一扣分点 |\n| Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、LLM-based IE 和 uncertainty estimation 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **缺少 free-form decoding 对照实验——核心发现可能是 constrained decoding artifact**\n- 具体位置：Section 5 (Discussion), Limitations\n- 问题：论文的核心概念 \"correlation-selection gap\" 被呈现为 structured IE 的重要发现，但 non-tied subset analysis（Section 5）已经证明：当 score compression 被缓解时（logprob range ≥ 0.05 的 40% instances），logprob 成为显著 selector（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）。这直接暗示 gap 主要源于 constrained decoding 的技术限制，而非 structured IE 的固有属性。缺少 free-form decoding（不使用 grammar constraint）的对照实验，无法区分这两种解释。\n- 为什么影响接收：如果 gap 仅存在于 constrained decoding 下（且已可追溯到 score compression），贡献从 \"发现 structured IE 的基本现象\" 降级为 \"记录 constrained decoding 的一个副作用\"，显著降低普适性和 novelty。\n- 建议修改方向：(1) 即使 free-form decoding 会产生部分 unparseable outputs，仍应在可解析子集上报告 selection F1 作为参照；(2) 至少在 SciERC 上运行 free-form + post-hoc parsing 的对照，量化 gap 在非 constrained 场景下是否缩小；(3) 或在 Discussion 中更明确地将 claim scope 限定为 \"constrained decoding 下的 selection 瓶颈 = score compression\"，不暗示更广泛的普适性。\n\n**N2** [critical] **TOST 等价检验的 δ 选择缺乏直接理据**\n- 具体位置：Appendix F (Table 4), Section 4.3 第 130 行\n- 问题：δ 取值 ±2pp, ±3pp, ±5pp 的唯一理由是 \"well-annotated NER benchmarks typically achieve inter-annotator F1 above 95%, implying 3–5pp annotation-induced variation is normal\"（Appendix F，line 274-275 引用 tjongkimsang2003conll）。但 IAA 变异反映的是标注噪声，与 \"一个好的 selector 应该带来多少增益\" 是不同的概念。实际上，oracle headroom = 13-18pp，如果 δ=5pp 意味着\"接受错过 5pp 也算等价\"，那在 13pp headroom 中放弃 5pp = 放弃 38% 的可能增益，这算\"等价\"吗？\n- 为什么影响接收：TOST 是论文支撑 \"selection failure\" 结论的关键工具之一。如果 δ 选择缺乏 principled 理据，等价结论的可信度受损。Section 4.3 主体文本只报告 \"most signals are indistinguishable from greedy at ±2–3pp on NER\"，读者容易把这当作强证据，但 δ 的选择实际上是自由度很大的分析师决策。\n- 建议修改方向：(1) 用 smallest effect size of interest (SESOI) 框架，基于 oracle headroom 的比例（如 oracle 增益的 20%）或先验 best-of-N 文献中的 expected gain 来选 δ；(2) 报告使 TOST 刚好通过/不通过的 δ 临界值（breakpoint analysis），让读者自行判断。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Qwen3 thinking token 训练不一致的影响被低估**\n- 具体位置：Limitations (line 19-21), Appendix E (line 373-374 footnote)\n- 问题：SciERC 训练未禁用 enable_thinking，而 CoNLL/WNUT 禁用了。论文以 \"constrained decoding overrides any thinking behavior by enforcing JSON-only output\" 为由将其定性为 \"minor inconsistency\"。但 thinking tokens 在训练时出现会影响 learned representations——模型可能学到 \"先推理再输出\" 的内部模式，即使推理不出现在输出中，也会影响 hidden states 和 logprob 分布。这对 SciERC 上的 logprob 行为可能有非平凡影响。\n- 问题的影响范围：SciERC 是 selection analysis 的主要数据集（Table 2），也是唯一同时有 NER 和 RE 结果的数据集。如果 thinking token 影响了 SciERC logprob 分布，则 logprob selection failure 的诊断（score compression 是主因）可能部分受 confound。\n- 建议：(1) 在 Limitations 中明确讨论 thinking token 对 logprob 行为的潜在影响，而非仅说 \"minor\"；(2) 如有可能，用禁用 thinking 的 Qwen3 SciERC checkpoint 重新验证 logprob 相关结论。\n\n**W2** [warning] **RE 证据强度不足以支撑多处主体论述中的 RE claims**\n- 具体位置：Abstract (line 3: \"RE (SciERC, preliminary)\"), Table 1, Table 2, Section 4.2, Section 5\n- 问题：RE 基于单数据集（SciERC，238 个 non-zero F1 instances），且 per-relation 诊断（Appendix D）显示极大变异（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646），n per relation 可能很小。然而论文在 Abstract、Table 1（RE 列）、Table 2（RE 列）、Discussion 中多次引用 RE 数据，给人 RE 是 \"preliminary but still a contribution\" 的印象。实际上，238 个 instance 且 relation type 间差异如此大，RE 结论的统计功效相当弱。\n- 建议：(1) 在 Section 4 开头更突出地标记 RE 为 exploratory/pilot analysis，而非仅在括号中标 \"preliminary\"；(2) 考虑将 RE 更多地移入 Appendix，减少主表中 RE 列的权重。\n\n**W3** [warning] **VC 定义：公式与实现不一致**\n- 具体位置：Section 3.2, Equation 6, Footnote 2 (line 62)\n- 问题：Equation 6 定义 $c_{vote}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)$，即所有 entity 的平均频率，无阈值。但 footnote 2 承认 \"Our implementation computes the mean entity-level match rate against a majority threshold (>N/2)\"。这两个定义在数学上不等价：公式是对所有 entity 的平均频率（连续值），实现是先二值化（>N/2 则 match=1，否则 0）再取均值。论文说 \"identical qualitative conclusions\"，但这种公式-实现不一致在方法论上有问题——读者如果根据公式复现，会得到不同的数值。\n- 建议：(1) 统一公式和实现——要么改公式以反映 threshold，要么改实现以匹配公式；(2) 报告两种定义下的量化差异（不仅 \"slightly different\" 而是具体数值）。\n\n**W4** [warning] **Instance-level 信号无法 select 的论证部分 tautological**\n- 具体位置：Section 4.3 (line 121), Section 5 \"Why the gap exists: two layers\" (line 8-10)\n- 问题：论文称 \"four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction\"（Section 4.3）。这在定义上就成立——instance-level signal 给每个 input 一个分数，当然无法区分 N 个 candidates。论文确实引入了 consensus-proximity selection 来将 instance-level signals 转化为 per-sample scores，但 Discussion 的 \"Layer 1 (definitional)\" 仍将此作为 gap 的主要解释之一。将 definitional 事实作为 empirical finding 呈现，弱化了论文的贡献感。\n- 建议：重构 narrative——明确 4/5 信号不能 select 是 by design（不算 finding），真正的 finding 是：(a) consensus-proximity 也不能恢复 per-sample discrimination，(b) logprob（唯一的 per-sample signal）也失败了。目前的写法已经在 Section 4.3 做了这个区分，但 Abstract、Introduction 中 \"four of five signals fail\" 的表述模糊了这一点。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用 ye2025uncertainty**：reference verification 显示 bib 中第一作者为 Ye，但 OpenAlex 返回 Heo。需要核实此条引用的作者信息是否正确。\n- **Table 1 布局密集**：8 列数据加 2 个 model blocks，视觉上难以快速定位关键比较。建议拆分为 NER 和 RE 子表或使用条件着色。\n- **Section 4.2 脚注 1 (line 64)**：与 semantic entropy 的 AUROC 比较注明 \"direct comparison is not meaningful due to fundamentally different output spaces\"——既然如此，提及此比较的价值有限，可删除或移至 Appendix。\n- **Fleiss' κ 独立性假设**（Section 3.2, line 39-40）：论文通过实测 excess agreement 验证 FK 未因依赖性被膨胀，但 excess agreement 在 -0.4% 到 -4.0% 范围内——这些负值是否在统计上显著不同于 0 没有测试。如果不显著，则验证更有力；如果显著，则 FK 的理论假设确实被违反（虽然方向是保守的）。\n- **N=8 primary results 使用单一 seed=42**：虽然 3-seed 分析在 Appendix C 中表明 σ≤0.025，但主表 single-seed 的做法在方法上不够 robust，尤其是 selection F1 的差异（如 logprob +0.6pp）与 σ 在同一数量级。\n\n---\n\n## 主要优势\n\n1. **清晰的概念区分**：quality estimation vs. sample selection 的区分是有价值的，此前文献经常混淆这两个目标（Section 1, line 13-14 正确指出这一点）。\n2. **统计实践优于多数同类论文**：paired bootstrap + TOST + Cohen's d + confidence intervals + multi-seed analysis，远超 NLP 论文常见的 \"report p-value only\" 标准。\n3. **诚实的局限性讨论**：RE preliminary、constrained decoding confound、thinking token 不一致、N scaling 限制——Limitations section 覆盖面广且具体。\n4. **Mechanistic diagnosis 有说服力**：non-tied subset analysis（Section 5, Appendix G）是论文最有洞察力的分析——将 logprob failure 追溯到 score compression，且证明 compression 缓解后 logprob 有效。\n5. **Task-difficulty dependent signal ranking** 是一个实用发现：EM 在简单任务领先，SJ/VC 在复杂任务领先，为实践者提供了 actionable guidance。\n6. **Cross-model consistency**（ρ 排序一致，幅度有差异）增强了发现的可信度。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n**Overall**: 3.0/5（Findings acceptance）\n**一句话总结**: 方法论扎实、统计实践规范的实证研究，但核心发现（correlation-selection gap）大部分可归因于 constrained decoding 的技术 artifact 而非 structured IE 的基本属性，加上 RE 仅单数据集、Qwen3 thinking token confound 未充分控制，限制了贡献的深度和普适性。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心 claim 有合理支撑，bootstrap 和 TOST 设计规范，但缺少 free-form decoding 对照实验是显著缺口；TOST δ 选择的理据间接 |\n| Excitement | 3.0/5 | Quality estimation vs. sample selection 的区分有价值，但 4/5 信号 instance-level 不能 select 在定义上即成立，logprob 失败归因于 score compression 是 constrained decoding 的特有问题，非通用发现 |\n| Overall | 3.0/5 | 适合 Findings：实证全面、写作清晰、局限性坦诚，但贡献增量性偏强 |\n| Reproducibility | 4/5 | 训练超参、数据集 split、prompt 模板、推理配置均有详细记录（Appendix E），代码未共享是唯一扣分点 |\n| Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、LLM-based IE 和 uncertainty estimation 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **缺少 free-form decoding 对照实验——核心发现可能是 constrained decoding artifact**\n- 具体位置：Section 5 (Discussion), Limitations\n- 问题：论文的核心概念 \"correlation-selection gap\" 被呈现为 structured IE 的重要发现，但 non-tied subset analysis（Section 5）已经证明：当 score compression 被缓解时（logprob range ≥ 0.05 的 40% instances），logprob 成为显著 selector（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）。这直接暗示 gap 主要源于 constrained decoding 的技术限制，而非 structured IE 的固有属性。缺少 free-form decoding（不使用 grammar constraint）的对照实验，无法区分这两种解释。\n- 为什么影响接收：如果 gap 仅存在于 constrained decoding 下（且已可追溯到 score compression），贡献从 \"发现 structured IE 的基本现象\" 降级为 \"记录 constrained decoding 的一个副作用\"，显著降低普适性和 novelty。\n- 建议修改方向：(1) 即使 free-form decoding 会产生部分 unparseable outputs，仍应在可解析子集上报告 selection F1 作为参照；(2) 至少在 SciERC 上运行 free-form + post-hoc parsing 的对照，量化 gap 在非 constrained 场景下是否缩小；(3) 或在 Discussion 中更明确地将 claim scope 限定为 \"constrained decoding 下的 selection 瓶颈 = score compression\"，不暗示更广泛的普适性。\n\n**N2** [critical] **TOST 等价检验的 δ 选择缺乏直接理据**\n- 具体位置：Appendix F (Table 4), Section 4.3 第 130 行\n- 问题：δ 取值 ±2pp, ±3pp, ±5pp 的唯一理由是 \"well-annotated NER benchmarks typically achieve inter-annotator F1 above 95%, implying 3–5pp annotation-induced variation is normal\"（Appendix F，line 274-275 引用 tjongkimsang2003conll）。但 IAA 变异反映的是标注噪声，与 \"一个好的 selector 应该带来多少增益\" 是不同的概念。实际上，oracle headroom = 13-18pp，如果 δ=5pp 意味着\"接受错过 5pp 也算等价\"，那在 13pp headroom 中放弃 5pp = 放弃 38% 的可能增益，这算\"等价\"吗？\n- 为什么影响接收：TOST 是论文支撑 \"selection failure\" 结论的关键工具之一。如果 δ 选择缺乏 principled 理据，等价结论的可信度受损。Section 4.3 主体文本只报告 \"most signals are indistinguishable from greedy at ±2–3pp on NER\"，读者容易把这当作强证据，但 δ 的选择实际上是自由度很大的分析师决策。\n- 建议修改方向：(1) 用 smallest effect size of interest (SESOI) 框架，基于 oracle headroom 的比例（如 oracle 增益的 20%）或先验 best-of-N 文献中的 expected gain 来选 δ；(2) 报告使 TOST 刚好通过/不通过的 δ 临界值（breakpoint analysis），让读者自行判断。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Qwen3 thinking token 训练不一致的影响被低估**\n- 具体位置：Limitations (line 19-21), Appendix E (line 373-374 footnote)\n- 问题：SciERC 训练未禁用 enable_thinking，而 CoNLL/WNUT 禁用了。论文以 \"constrained decoding overrides any thinking behavior by enforcing JSON-only output\" 为由将其定性为 \"minor inconsistency\"。但 thinking tokens 在训练时出现会影响 learned representations——模型可能学到 \"先推理再输出\" 的内部模式，即使推理不出现在输出中，也会影响 hidden states 和 logprob 分布。这对 SciERC 上的 logprob 行为可能有非平凡影响。\n- 问题的影响范围：SciERC 是 selection analysis 的主要数据集（Table 2），也是唯一同时有 NER 和 RE 结果的数据集。如果 thinking token 影响了 SciERC logprob 分布，则 logprob selection failure 的诊断（score compression 是主因）可能部分受 confound。\n- 建议：(1) 在 Limitations 中明确讨论 thinking token 对 logprob 行为的潜在影响，而非仅说 \"minor\"；(2) 如有可能，用禁用 thinking 的 Qwen3 SciERC checkpoint 重新验证 logprob 相关结论。\n\n**W2** [warning] **RE 证据强度不足以支撑多处主体论述中的 RE claims**\n- 具体位置：Abstract (line 3: \"RE (SciERC, preliminary)\"), Table 1, Table 2, Section 4.2, Section 5\n- 问题：RE 基于单数据集（SciERC，238 个 non-zero F1 instances），且 per-relation 诊断（Appendix D）显示极大变异（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646），n per relation 可能很小。然而论文在 Abstract、Table 1（RE 列）、Table 2（RE 列）、Discussion 中多次引用 RE 数据，给人 RE 是 \"preliminary but still a contribution\" 的印象。实际上，238 个 instance 且 relation type 间差异如此大，RE 结论的统计功效相当弱。\n- 建议：(1) 在 Section 4 开头更突出地标记 RE 为 exploratory/pilot analysis，而非仅在括号中标 \"preliminary\"；(2) 考虑将 RE 更多地移入 Appendix，减少主表中 RE 列的权重。\n\n**W3** [warning] **VC 定义：公式与实现不一致**\n- 具体位置：Section 3.2, Equation 6, Footnote 2 (line 62)\n- 问题：Equation 6 定义 $c_{vote}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)$，即所有 entity 的平均频率，无阈值。但 footnote 2 承认 \"Our implementation computes the mean entity-level match rate against a majority threshold (>N/2)\"。这两个定义在数学上不等价：公式是对所有 entity 的平均频率（连续值），实现是先二值化（>N/2 则 match=1，否则 0）再取均值。论文说 \"identical qualitative conclusions\"，但这种公式-实现不一致在方法论上有问题——读者如果根据公式复现，会得到不同的数值。\n- 建议：(1) 统一公式和实现——要么改公式以反映 threshold，要么改实现以匹配公式；(2) 报告两种定义下的量化差异（不仅 \"slightly different\" 而是具体数值）。\n\n**W4** [warning] **Instance-level 信号无法 select 的论证部分 tautological**\n- 具体位置：Section 4.3 (line 121), Section 5 \"Why the gap exists: two layers\" (line 8-10)\n- 问题：论文称 \"four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction\"（Section 4.3）。这在定义上就成立——instance-level signal 给每个 input 一个分数，当然无法区分 N 个 candidates。论文确实引入了 consensus-proximity selection 来将 instance-level signals 转化为 per-sample scores，但 Discussion 的 \"Layer 1 (definitional)\" 仍将此作为 gap 的主要解释之一。将 definitional 事实作为 empirical finding 呈现，弱化了论文的贡献感。\n- 建议：重构 narrative——明确 4/5 信号不能 select 是 by design（不算 finding），真正的 finding 是：(a) consensus-proximity 也不能恢复 per-sample discrimination，(b) logprob（唯一的 per-sample signal）也失败了。目前的写法已经在 Section 4.3 做了这个区分，但 Abstract、Introduction 中 \"four of five signals fail\" 的表述模糊了这一点。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用 ye2025uncertainty**：reference verification 显示 bib 中第一作者为 Ye，但 OpenAlex 返回 Heo。需要核实此条引用的作者信息是否正确。\n- **Table 1 布局密集**：8 列数据加 2 个 model blocks，视觉上难以快速定位关键比较。建议拆分为 NER 和 RE 子表或使用条件着色。\n- **Section 4.2 脚注 1 (line 64)**：与 semantic entropy 的 AUROC 比较注明 \"direct comparison is not meaningful due to fundamentally different output spaces\"——既然如此，提及此比较的价值有限，可删除或移至 Appendix。\n- **Fleiss' κ 独立性假设**（Section 3.2, line 39-40）：论文通过实测 excess agreement 验证 FK 未因依赖性被膨胀，但 excess agreement 在 -0.4% 到 -4.0% 范围内——这些负值是否在统计上显著不同于 0 没有测试。如果不显著，则验证更有力；如果显著，则 FK 的理论假设确实被违反（虽然方向是保守的）。\n- **N=8 primary results 使用单一 seed=42**：虽然 3-seed 分析在 Appendix C 中表明 σ≤0.025，但主表 single-seed 的做法在方法上不够 robust，尤其是 selection F1 的差异（如 logprob +0.6pp）与 σ 在同一数量级。\n\n---\n\n## 主要优势\n\n1. **清晰的概念区分**：quality estimation vs. sample selection 的区分是有价值的，此前文献经常混淆这两个目标（Section 1, line 13-14 正确指出这一点）。\n2. **统计实践优于多数同类论文**：paired bootstrap + TOST + Cohen's d + confidence intervals + multi-seed analysis，远超 NLP 论文常见的 \"report p-value only\" 标准。\n3. **诚实的局限性讨论**：RE preliminary、constrained decoding confound、thinking token 不一致、N scaling 限制——Limitations section 覆盖面广且具体。\n4. **Mechanistic diagnosis 有说服力**：non-tied subset analysis（Section 5, Appendix G）是论文最有洞察力的分析——将 logprob failure 追溯到 score compression，且证明 compression 缓解后 logprob 有效。\n5. **Task-difficulty dependent signal ranking** 是一个实用发现：EM 在简单任务领先，SJ/VC 在复杂任务领先，为实践者提供了 actionable guidance。\n6. **Cross-model consistency**（ρ 排序一致，幅度有差异）增强了发现的可信度。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-15T08:51:59.086021+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4074
}
```

</details>

---


### Assistant

_source line 490 · 2026-05-15T08:52:08.048281+00:00_

审稿报告已提交给 Review Director。

总结：

**Overall 3.0/5（Findings acceptance）**。方法论扎实、统计实践规范的实证研究，有两个 Must-Fix 问题：

1. **缺少 free-form decoding 对照实验**——non-tied subset analysis 已证明 logprob 在 compression 缓解时有效（+2.9pp, p=0.01），强烈暗示 correlation-selection gap 主要是 constrained decoding artifact 而非 structured IE 的固有属性，但论文缺乏直接对照实验来区分这两种解释。

2. **TOST δ 选择理据薄弱**——基于 IAA 变异的 δ 论证概念上不匹配（IAA 噪声 ≠ selector 预期增益），且在 13-18pp oracle headroom 中 δ=5pp 意味着放弃 ~38% 增益仍算"等价"。

四个 Should-Fix：Qwen3 thinking token confound 被低估、RE 单数据集证据不足、VC 公式-实现不一致、instance-level 信号不能 select 部分 tautological。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 491 · 2026-05-15T08:53:13.048706+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

## Reviewer 2 — Round 1 审稿报告

**总体评分**: 3/5 (Findings track)

### Must-Fix 问题

**N1** [critical] Contribution 1 "systematic multi-family comparison" 的新颖性与 framing 不匹配
- 论文将 "5 signals from 3 families" 的对比定位为主要贡献，但本质是 engineering benchmark——将已知 confidence signals 应用于新任务设置。与 Nédellec et al. (2026) 的增量存在（结构化匹配、constrained decoding、多数据集），但 Introduction 没有充分区分 "applying known signals" 和 "discovering new principles"。
- 建议：将 Contribution 1 降级为 setup/methodology，将 Contribution 2 (gap) 提升为核心。

**N2** [critical] Correlation-selection gap 的 4/5 来源是定义性的，非实证发现
- Discussion 自己承认 4/5 信号的 selection failure 是 "by construction"（Layer 1）。真正的实证贡献是 Layer 2（logprob 压缩），但被埋在 "gap" 叙事下。
- 建议：(1) Introduction 提前透明化 Layer 1 是 definitional；(2) 将叙事重心转向 Layer 2。

**N3** [critical] Related Work 遗漏关键引用
- (a) Zhang et al. (2025) "A Survey on Test-Time Scaling in LLMs"——最全面的 TTS survey
- (b) Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) "Structure-Conditional MBR Decoding"——直接研究 MBR 在结构化输出上的问题

### Should-Fix 问题

**W1** [warning] "cross-model" 措辞过度外推（实际 2 个 8B 模型）
**W2** [warning] Abstract 信息密度过高（9 行含 5 signal/3 family/4 metric/3 dataset/2 model + 新术语）
**W3** [warning] 术语不一致（VC/Voting Conf./entity voting；LP/Log-prob/logprob）
**W4** [warning] RE 单数据集标注在 Discussion/Conclusion 中不足
**W5** [warning] Qwen3 thinking mode confound
**W6** [warning] 缺少 supervised verifier baseline

### 小问题
- Figure 1 caption 冗余
- Table 1 N=16 行空白多
- FK excess agreement "sufficient diversity" 措辞不准确
- Notation Table 缺 LP 缩写
- Ethics Statement 未注明 CoNLL-2003 Reuters license 限制

### 引用验证发现 5 处 bib 问题
- feng2025optimal 作者顺序
- ye2025uncertainty 第一作者可能为 Heo
- hobelsberger2025systematic 和 venktesh2025trust 无法在线验证
- snell2024scaling key 标 2024 但 venue 为 ICLR 2025

### 主要优势
1. 统计分析严谨度远超同类
2. Logprob 压缩诊断有 actionable 价值
3. Limitations 坦诚
4. Difficulty gradient 设计合理（WNUT-17 负 logprob correlation 非显然）
5. Quality estimation vs selection 区分是有价值的框架贡献

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 492 · 2026-05-15T08:54:41.940164+00:00_

逐条回应 Reviewer 2 的审稿意见。

---

## 交叉回应：Reviewer 1 对 Reviewer 2 的意见

### Must-Fix 问题

**[AGREE] R2-N1: Contribution 1 的新颖性与 framing 不匹配**

同意核心判断。Contribution 1（"systematic multi-family comparison"）本质上是将已知信号应用于新设置的 engineering benchmark。与 Nédellec et al. (2026) 的三个增量（结构化匹配、best-of-N 测试、难度梯度）是合理的方法论改进，但不足以单独构成一个 contribution。Introduction (Section 1, line 39-42) 将其列为第一条贡献，给读者的印象是这是论文的主要贡献，这在 framing 上确实过度。

补充发现：从我自己的审查看，SJ 信号（type-aware bipartite matching + token-level IoU）确实是方法层面的新设计，但这应该被呈现为 "methodology" 而非 "contribution"。R2 建议将 Contribution 1 降级为 setup/methodology、Contribution 2 提升为核心，我认为是正确的重构方向。

---

**[AGREE] R2-N2: 4/5 selection failure 是 definitional**

完全同意。我在自己的审稿中将此列为 W4，指出 Section 4.3 (line 121) "they cannot rank candidates by construction" 本身就是一个定义性事实而非实证发现。Discussion Section 5 的 "Layer 1 (definitional)" 标签实际上是论文自己承认了这一点，但 Abstract（line 5-6: "four of five signals are instance-level by construction"）和 Introduction（line 46: "Four of five signals are instance-level by construction"）仍然将其与 logprob failure 并列呈现为 gap 的组成部分，模糊了真正的实证贡献边界。

进一步补充：这个 framing 问题与 N1 相互强化。如果 Contribution 1 是 benchmark + Contribution 2 的核心 is half definitional，那论文的 novelty 实际上集中在一个较窄的点上——logprob 在 constrained decoding 下的 score compression 诊断。这个点本身有价值（我在自己审稿的优势 #4 中肯定了这一点），但需要更诚实的 framing。

---

**[REBUT] R2-N3: Related Work 遗漏关键引用**

部分不同意将此列为 critical。

(a) Zhang et al. (2025) "A Survey on Test-Time Scaling in LLMs"——这是一篇综述性论文。Related Work (Section 2) 已经引用了 test-time scaling 的核心原始工作：Snell et al. (2024)、Brown et al. (2024)，以及多篇具体方法论文（Taubenfeld 2025, Kang 2025, Kim 2026, Wang 2025 等）。遗漏一篇综述在 8 页正文的 Findings 论文中不构成 critical 问题——引用原始贡献比引用综述更重要。建议降级为 minor，可在 camera-ready 补充。

(b) Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) "Structure-Conditional MBR Decoding"——这条引用更有实质关联，因为论文的 Discussion Section 5 (line 18-19) 明确讨论了 MBR decoding 在结构化输出上的失败，与这篇工作直接相关。Section 2 已经引用了 Eikema & Aziz (2022)、Freitag et al. (2022)、Müller & Sennrich (2021)、Jinnai et al. (2024) 等 MBR 工作，但缺少结构化输出上的 MBR 这一最直接的相关工作确实是一个值得修复的遗漏。不过这仍然是 should-fix 级别而非 critical——它不影响论文结论的成立性，因为论文的 MBR 分析（consensus-proximity selection = MBR with structural utility）是独立完成的。

综合建议：将 (b) 提升为 should-fix 并在 camera-ready 中引用和讨论差异；(a) 列为 minor。

---

### Should-Fix 问题

**[AGREE] R2-W1: "cross-model" 措辞过度外推**

同意。论文仅测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct，两者均为 8B 参数。Section 4.2 (line 75) "Cross-model stability is strong" 和 Appendix B "Cross-model transfer" 的措辞暗示了比实际覆盖范围更广的泛化性。"cross-model" 在严格意义上只意味着 "across two specific model families at identical scale"，应改为 "cross-family"（两个架构家族间）或明确限定 "at 8B scale"。Limitations (line 5-7) 虽然承认了 scale 局限性，但主体文本的措辞未反映这一限定。

---

**[AGREE] R2-W2: Abstract 信息密度过高**

同意。Abstract (9 lines) 中包含：5 个信号名、3 个 family 名、4 个评估 metric（ρ, AUROC, F1, p-value）、3 个数据集、2 个模型 + "correlation-selection gap" 新术语 + non-tied subset 诊断结果。对首次阅读的 reviewer 而言，信息过载导致核心 message 被稀释。Abstract 应该聚焦于 gap 的发现和诊断，将信号/数据集的细节留给 Introduction。

---

**[AGREE] R2-W3: 术语不一致**

同意。通篇存在多处同一概念使用不同缩写/名称的情况。仅从我读到的：VC / Voting Conf. / entity voting confidence / $c_{\text{vote}}$（Section 3.2 Equation 6 vs. Table 1 vs. 行文中）；LP / Log-prob / logprob / $c_{\text{lp}}$（Table 1 header vs. Section 4.3 行文 vs. Appendix）。这不影响理解但降低了论文的打磨度，在 Findings 投稿中应该修正。

---

**[AGREE] R2-W4: RE 单数据集标注在 Discussion/Conclusion 不足**

同意，与我自己的 W2 一致。Abstract 中 "(SciERC, preliminary)" 的括号标注容易被忽略。Discussion Section 5 多次引用 RE 数据（如 MBR decoding 分析, calibration ECE），但未在每处重复 "preliminary/single-benchmark" 警告。Conclusion (Section 6, line 7) 一句 "RE findings rest on SciERC alone" 是论文中最明确的标注，但 Discussion 中的多处 RE 引用缺乏同等标注。

---

**[AGREE] R2-W5: Qwen3 thinking mode confound**

同意，与我自己的 W1 一致。我在自己的审稿中将此列为 should-fix 并详细分析了 thinking tokens 在训练中影响 learned representations 的机制——即使 constrained decoding 阻止了推理 tokens 出现在输出中，训练时的 thinking token exposure 可能改变了 SciERC checkpoint 的 logprob 分布。这是一个未控制的 confound。

---

**[REBUT] R2-W6: 缺少 supervised verifier baseline**

不同意将此列为 should-fix。论文的研究问题是 "unsupervised confidence signals 在 structured IE 中的 quality estimation 和 sample selection 表现"（Section 3.1, line 7-8）。Supervised verifier 是一个不同的方法范式，论文在 Section 5 (line 23) 和 Conclusion (line 8) 中将 "trained verifiers" 明确列为 future work 方向，且引用了 Cobbe et al. (2021)、Lightman et al. (2024)、Venktesh et al. (2025) 等相关工作。

要求一篇关于 unsupervised signals 的 empirical study 同时训练 supervised verifier 作为 baseline，会显著改变论文的 scope 和工作量。更合理的期望是：(1) 论文应该讨论 supervised approach 可能恢复多少 oracle headroom——这它已经做了（Discussion Section 5, line 23），(2) 引用相关 supervised 工作——也已做到。

如果 R2 的意思是 "至少用一个现成的 verifier（如 reward model）做 zero-shot baseline"，这个建议更合理，但仍然超出了论文的 stated scope。

---

### 小问题

**[AGREE] R2-小问题-Figure 1 caption 冗余**：Figure 1 caption（Section 1, line 30-33）确实过长，重复了 Section 4.3 的信息。

**[AGREE] R2-小问题-Table 1 N=16 行空白多**：Table 1 (Table~\ref{tab:quality_estimation}) 的 N=16 section 仅有 LLaMA CoNLL 一个配置的数据，其余全为空白。视觉上浪费空间，建议将 N=16 数据整合到 Appendix Table 3 中。

**[AGREE] R2-小问题-FK "sufficient diversity" 措辞**：Section 3.2 (line 39) "temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns" 中 "sufficient" 未量化。虽然后文给出了 excess agreement 的实测值 (-0.4% to -4.0%)，但 "sufficient" 的标准未定义。

**[AGREE] R2-小问题-Notation Table 缺 LP**：Appendix A Table (line 19) 列了 $c_{\text{lp}}$ 但未列 "LP" 缩写。考虑到行文中频繁使用 LP/logprob，应补充。

**[AGREE] R2-小问题-Ethics Statement 缺 CoNLL-2003 Reuters license**：CoNLL-2003 基于 Reuters 语料，存在已知的 license 限制。Ethics Statement (main.tex, line 40) 仅说 "publicly available benchmarks" 未提及 license 细节。这是一个合规瑕疵。

---

### 引用验证

**[AGREE] R2-引用问题**：5 处 bib 问题与我自己的引用验证结果一致。ye2025uncertainty 的 Ye vs. Heo 差异最值得关注——如果第一作者确实是 Heo 而非 Ye，这是一个事实错误需要修正。snell2024scaling key 标 2024 但 venue 为 ICLR 2025 是一个常见的 arXiv-first / venue-later 不一致，应更新 key 或 year。

---

### 优势部分

**[AGREE] R2-优势 1-5**：全部同意。R2 识别的优势与我自己的审稿判断高度一致，特别是：统计严谨度（我的优势 #2）、logprob 压缩诊断（我的优势 #4）、difficulty gradient 设计（我的优势 #5）、quality estimation vs. selection 区分（我的优势 #1）。

---

### 综合评价

Reviewer 2 的审稿意见整体质量高，与我的独立审查结论方向一致。核心分歧仅两处：(1) R2-N3 related work 遗漏的严重程度（我认为应降级为 should-fix/minor）；(2) R2-W6 supervised verifier baseline（我认为超出论文 scope）。其余 must-fix 和 should-fix 意见我均认同，且多处与我自己的发现互为印证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

42 recorded events
